#!/usr/bin/env python3
"""
Aggregate RSS feeds, cluster related items, fetch full content for survivors,
and produce a briefing packet ready for LLM analysis.

Outputs:
  docs/feed.json              - raw normalized feed data (transparency)
  docs/briefing_packet.json   - the curated input for the analysis agent
"""

import argparse
import hashlib
import json
import os
import re
import socket
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from urllib.parse import urlparse

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup

# Local modules
from taxonomy import extract_taxonomy
from affinity import find_affinity_groups

socket.setdefaulttimeout(15)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Default lookback window in hours. Override with:
#   - CLI flag:  python aggregate.py --lookback-hours 36
#   - Env var:   LOOKBACK_HOURS=36 python aggregate.py
#   - GitHub Actions workflow_dispatch input (see aggregate.yml)
# Common values: 24 (one day), 36 (overnight buffer), 168 (one week, default), 336 (two weeks).
DEFAULT_LOOKBACK_HOURS = 168

# Items per feed pulled from RSS (before lookback filtering).
# Set to 100 as a defensive cap. Most feeds return 10-30 entries regardless,
# so 100 is rarely the binding constraint. High-volume feeds (BleepingComputer,
# Reddit, The Hacker News) cap their RSS output below this and may not return
# a full week of content even at the cap. That's accepted tradeoff. Their
# stories typically reach you via corroboration from Tier 1 research feeds
# (Unit 42, Talos, Mandiant, etc.), which have lower publication volume and
# fit comfortably within this cap.
ITEMS_PER_FEED = 100

# Cohort tier weights for the priority score.
# Higher tier = higher signal weight in ranking.
COHORT_WEIGHTS = {
    "threat_research_primary": 10,
    "government_authoritative": 9,
    "offensive_vulnerability_research": 9,
    "detection_response_operations": 8,
    "cloud_identity_infrastructure": 7,
    "ai_security_agentic_risk": 7,
    "ransomware_ecrime_financial_crime": 7,
    "policy_strategy_geopolitics": 5,
    "practitioner_analysis": 5,
    "cyber_news_breach_reporting": 4,
    "reddit_practitioner_osint": 2,
}

# Keyword signals that boost priority. Tuned for "this matters today" content.
SIGNAL_KEYWORDS = {
    # Exploitation urgency
    r"\bactively\s+exploited\b": 8,
    r"\bzero[\s-]?day\b": 8,
    r"\bin[\s-]the[\s-]wild\b": 6,
    r"\bemergency\s+patch\b": 6,
    r"\bunauthenticated\b": 4,
    r"\bremote\s+code\s+execution\b|\bRCE\b": 5,
    r"\bpre[\s-]auth\b": 5,
    # Scale / impact
    r"\bransomware\b": 4,
    r"\bsupply[\s-]chain\b": 5,
    r"\bdata\s+breach\b": 3,
    r"\bnation[\s-]state\b": 4,
    r"\bAPT\d+\b": 4,
    # Specificity
    r"\bCVE-\d{4}-\d{4,7}\b": 6,
    r"\bCVSS\s*[:\s]\s*9\.|\bCVSS\s*[:\s]\s*10\b": 4,
    # AI / emerging
    r"\bprompt\s+injection\b": 3,
    r"\bagentic\b|\bagent\s+abuse\b": 3,
    r"\bmodel\s+poisoning\b": 3,
}

# Noise penalties — patterns that suggest marketing or low-signal content.
NOISE_PATTERNS = {
    r"\bwebinar\b": -3,
    r"\bjoin\s+us\s+at\b": -3,
    r"\bregister\s+now\b": -3,
    r"\b(introducing|announcing)\s+(our|the)\s+new\b": -2,
    r"\bgartner\s+magic\s+quadrant\b": -3,
    r"\baward\b.*\b(winner|recognized)\b": -2,
    r"\bpartner(ship)?\s+with\b": -2,
}

# Clustering similarity threshold (0-1). Higher = stricter.
CLUSTER_THRESHOLD = 0.55

# User-Agent for full-article fetches.
UA = "Mozilla/5.0 (compatible; CTI-Aggregator/1.0; +https://github.com)"

# Max full-fetch attempts. We only full-fetch the top N cluster representatives
# to keep the briefing packet bounded and respectful to source sites.
# Scaled up for week-long windows; the agent will still only surface 10-15 cards.
MAX_FULL_FETCH = 60

# Minimum priority score for a cluster to survive into the briefing packet.
# Filters out the long tail of low-signal items at large lookback windows.
# Lower this if you want more raw context; raise it to be more ruthless.
MIN_CLUSTER_SCORE = 8

# Maximum clusters to include in the briefing packet (post-filter, post-sort).
# The agent's job is to pick 10-15 from this set, not from 200.
MAX_CLUSTERS_IN_PACKET = 80

# Output size cap for the briefing packet items (chars per article body).
BODY_CHAR_LIMIT = 4000


# ---------------------------------------------------------------------------
# Feed parsing
# ---------------------------------------------------------------------------

def clean_text(s):
    """Strip HTML, collapse whitespace."""
    if not s:
        return ""
    soup = BeautifulSoup(s, "html.parser")
    text = soup.get_text(separator=" ")
    return re.sub(r"\s+", " ", unescape(text)).strip()


def parse_feed(name, url, cohort, lookback_hours):
    """Fetch and parse a single feed. Return list of normalized items + status."""
    try:
        parsed = feedparser.parse(url, agent=UA)
    except Exception as e:
        print(f"  ERROR fetching {name}: {e}", file=sys.stderr)
        return [], "fetch_error"

    if parsed.bozo and not parsed.entries:
        return [], "parse_error"

    items = []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)

    for entry in parsed.entries[:ITEMS_PER_FEED]:
        pub_date = None
        for field in ("published_parsed", "updated_parsed"):
            t = getattr(entry, field, None)
            if t:
                try:
                    pub_date = datetime(*t[:6], tzinfo=timezone.utc)
                    break
                except (TypeError, ValueError):
                    continue

        title = clean_text(entry.get("title", ""))
        summary = clean_text(entry.get("summary", ""))[:1000]
        link = entry.get("link", "")

        if not title or not link:
            continue

        item = {
            "source": name,
            "cohort": cohort,
            "category": cohort,  # backward-compat alias for build-page.js
            "title": title,
            "link": link,
            "published": pub_date.isoformat() if pub_date else None,
            "published_dt": pub_date,
            "summary": summary,
            "author": clean_text(entry.get("author", "")),
            "in_window": bool(pub_date and pub_date >= cutoff),
        }
        # Enrich with structured taxonomy (deterministic, no LLM).
        # full_body is not available at this stage; taxonomy will be re-enriched
        # for cluster representatives after full-fetch to improve recall.
        item["taxonomy"] = extract_taxonomy(
            title=title,
            summary=summary,
            source=name,
            cohort=cohort,
            full_body="",
        )
        items.append(item)

    return items, "ok"


# ---------------------------------------------------------------------------
# Full-article fetching (only for cluster representatives)
# ---------------------------------------------------------------------------

def fetch_article(url):
    """Pull an article and return readable body text. Bounded, polite."""
    try:
        r = requests.get(
            url,
            headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"},
            timeout=10,
            allow_redirects=True,
        )
        r.raise_for_status()
    except Exception as e:
        return "", f"fetch_failed:{type(e).__name__}"

    if "text/html" not in r.headers.get("Content-Type", ""):
        return "", "not_html"

    try:
        soup = BeautifulSoup(r.text, "html.parser")
    except Exception:
        return "", "parse_failed"

    # Strip nav/footer/script noise.
    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
        tag.decompose()

    # Prefer article tag, then main, then largest text block.
    candidates = soup.find_all(["article", "main"])
    if candidates:
        body = max(candidates, key=lambda t: len(t.get_text()))
    else:
        body = soup.body or soup

    text = re.sub(r"\s+", " ", body.get_text(separator=" ")).strip()
    return text[:BODY_CHAR_LIMIT], "ok"


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_item(item):
    """Compute priority score for an item. Higher = more important."""
    score = COHORT_WEIGHTS.get(item["cohort"], 3)

    haystack = f"{item['title']} {item['summary']}".lower()

    for pattern, weight in SIGNAL_KEYWORDS.items():
        if re.search(pattern, haystack, re.IGNORECASE):
            score += weight

    for pattern, weight in NOISE_PATTERNS.items():
        if re.search(pattern, haystack, re.IGNORECASE):
            score += weight  # weight is negative

    # Recency bonus — fresher items rank higher within the window.
    if item.get("published_dt"):
        age_hours = (datetime.now(timezone.utc) - item["published_dt"]).total_seconds() / 3600
        if age_hours < 6:
            score += 4
        elif age_hours < 12:
            score += 2
        elif age_hours < 24:
            score += 1

    return score


# ---------------------------------------------------------------------------
# Clustering
# ---------------------------------------------------------------------------

def tokenize(text):
    """Lowercase tokens, drop short/common words."""
    stop = {
        "the", "a", "an", "and", "or", "of", "in", "on", "to", "for",
        "with", "is", "are", "was", "were", "by", "as", "at", "from",
        "that", "this", "it", "be", "has", "have", "new", "blog", "post",
    }
    tokens = re.findall(r"[a-z0-9]{3,}", text.lower())
    return {t for t in tokens if t not in stop}


def extract_strong_signals(text):
    """Pull CVE IDs, actor names, product names — high-signal anchors for clustering."""
    signals = set()
    # CVEs
    signals.update(m.upper() for m in re.findall(r"CVE-\d{4}-\d{4,7}", text, re.IGNORECASE))
    # APT / actor patterns
    signals.update(m.upper() for m in re.findall(r"\bAPT\d+\b", text, re.IGNORECASE))
    signals.update(m for m in re.findall(r"\b(?:Lazarus|Volt Typhoon|Salt Typhoon|Scattered Spider|LockBit|BlackCat|ALPHV|Cl0p|Akira|RansomHub|Volt|Mustang Panda|Kimsuky|Lapsus\$?)\b", text, re.IGNORECASE))
    return signals


def similarity(a, b):
    """Hybrid similarity: strong signal match dominates, token overlap fills in."""
    # Strong signals (CVE, actor) — if any match, almost certainly the same story.
    if a["strong_signals"] and a["strong_signals"] & b["strong_signals"]:
        return 1.0

    if not a["tokens"] or not b["tokens"]:
        return 0.0

    intersection = a["tokens"] & b["tokens"]
    union = a["tokens"] | b["tokens"]
    return len(intersection) / len(union) if union else 0.0


def cluster_items(items):
    """Greedy clustering. Items sorted by score; each new item joins best cluster or starts one."""
    # Precompute tokens and strong signals per item.
    for item in items:
        text = f"{item['title']} {item['summary']}"
        item["tokens"] = tokenize(text)
        item["strong_signals"] = extract_strong_signals(text)

    items_sorted = sorted(items, key=lambda x: x["score"], reverse=True)
    clusters = []

    for item in items_sorted:
        best_cluster = None
        best_sim = 0.0

        for cluster in clusters:
            # Compare against cluster representative (highest scoring member).
            sim = similarity(item, cluster["rep"])
            if sim > best_sim:
                best_sim = sim
                best_cluster = cluster

        if best_cluster and best_sim >= CLUSTER_THRESHOLD:
            best_cluster["members"].append(item)
            # Cluster score boosts with corroboration.
            best_cluster["score"] += 2
        else:
            clusters.append({
                "rep": item,
                "members": [item],
                "score": item["score"],
            })

    return clusters


# ---------------------------------------------------------------------------
# Briefing packet assembly
# ---------------------------------------------------------------------------

def cluster_id(rep):
    """Stable cluster identifier."""
    seed = f"{rep['title']}|{rep['link']}"
    return hashlib.sha1(seed.encode()).hexdigest()[:10]


def build_briefing_packet(clusters, all_items, feed_status, cohort_metadata, lookback_hours):
    """Build the structured input for the analysis agent."""
    # Sort clusters by score desc, apply floor, apply cap.
    clusters_sorted = sorted(clusters, key=lambda c: c["score"], reverse=True)
    total_clusters_raw = len(clusters_sorted)

    # Filter: drop clusters below the signal floor.
    clusters_filtered = [c for c in clusters_sorted if c["score"] >= MIN_CLUSTER_SCORE]
    dropped_low_score = total_clusters_raw - len(clusters_filtered)

    # Cap at the maximum packet size.
    clusters_kept = clusters_filtered[:MAX_CLUSTERS_IN_PACKET]
    dropped_overflow = len(clusters_filtered) - len(clusters_kept)

    print(f"\nCluster pipeline:")
    print(f"  Raw clusters:           {total_clusters_raw}")
    print(f"  Dropped (score < {MIN_CLUSTER_SCORE}): {dropped_low_score}")
    print(f"  Dropped (overflow):     {dropped_overflow}")
    print(f"  Kept in packet:         {len(clusters_kept)}")

    # Full-fetch the top N cluster reps in parallel.
    to_fetch = clusters_kept[:MAX_FULL_FETCH]
    print(f"\nFull-fetching {len(to_fetch)} cluster representatives...")

    with ThreadPoolExecutor(max_workers=8) as ex:
        future_to_cluster = {
            ex.submit(fetch_article, c["rep"]["link"]): c for c in to_fetch
        }
        for future in as_completed(future_to_cluster):
            c = future_to_cluster[future]
            try:
                body, status = future.result()
            except Exception as e:
                body, status = "", f"error:{type(e).__name__}"
            c["rep"]["full_body"] = body
            c["rep"]["fetch_status"] = status
            # Re-enrich taxonomy with the full body for better recall.
            if body:
                c["rep"]["taxonomy"] = extract_taxonomy(
                    title=c["rep"]["title"],
                    summary=c["rep"]["summary"],
                    source=c["rep"]["source"],
                    cohort=c["rep"]["cohort"],
                    full_body=body,
                )
            symbol = "OK" if status == "ok" else "SKIP"
            print(f"  [{symbol}] {c['rep']['source']}: {c['rep']['title'][:70]}")

    # Assemble briefing clusters.
    briefing_clusters = []
    for c in clusters_kept:
        rep = c["rep"]
        # Collect all unique sources corroborating this cluster.
        corroborating = []
        seen_sources = set()
        for m in c["members"]:
            if m["source"] not in seen_sources:
                seen_sources.add(m["source"])
                corroborating.append({
                    "source": m["source"],
                    "cohort": m["cohort"],
                    "title": m["title"],
                    "link": m["link"],
                    "published": m["published"],
                    "summary": m["summary"],
                    "taxonomy": m.get("taxonomy", {}),
                })

        # Aggregate taxonomy across all cluster members (union of tags).
        cluster_tax = _aggregate_cluster_taxonomy(c["members"])

        briefing_clusters.append({
            "cluster_id": cluster_id(rep),
            "priority_score": c["score"],
            "member_count": len(c["members"]),
            "corroborating_source_count": len(corroborating),
            "strong_signals": sorted(rep["strong_signals"]),
            "taxonomy": cluster_tax,
            "primary": {
                "source": rep["source"],
                "cohort": rep["cohort"],
                "title": rep["title"],
                "link": rep["link"],
                "published": rep["published"],
                "summary": rep["summary"],
                "full_body": rep.get("full_body", ""),
                "fetch_status": rep.get("fetch_status", "not_attempted"),
                "taxonomy": rep.get("taxonomy", {}),
            },
            "corroborating_sources": corroborating,
        })

    # Detect affinity groups across the clusters in the packet.
    # Pass the kept clusters (which still have member taxonomies attached).
    raw_groups = find_affinity_groups(clusters_kept)
    # Map cluster indices to cluster_ids for the packet output.
    kept_cluster_ids = [cluster_id(c["rep"]) for c in clusters_kept]
    affinity_groups = []
    for g in raw_groups:
        affinity_groups.append({
            "label": g["label"],
            "dominant_features": g["dominant_features"],
            "cluster_count": g["cluster_count"],
            "article_count": g["article_count"],
            "cohesion": g["cohesion"],
            "cluster_ids": [kept_cluster_ids[i] for i in g["cluster_indices"]],
        })

    print(f"\nAffinity groups detected: {len(affinity_groups)}")
    for g in affinity_groups[:5]:
        print(f"  - {g['label']} ({g['cluster_count']} clusters, {g['article_count']} articles)")

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lookback_hours": lookback_hours,
        "lookback_human": _humanize_window(lookback_hours),
        "total_feeds": len(feed_status),
        "feeds_ok": sum(1 for s in feed_status.values() if s["status"] == "ok"),
        "total_items_in_window": sum(1 for i in all_items if i["in_window"]),
        "total_clusters_raw": total_clusters_raw,
        "total_clusters_in_packet": len(briefing_clusters),
        "dropped_low_score": dropped_low_score,
        "dropped_overflow": dropped_overflow,
        "cohort_metadata": cohort_metadata,
        "feed_status": feed_status,
        "clusters": briefing_clusters,
        "affinity_groups": affinity_groups,
    }


def _aggregate_cluster_taxonomy(members):
    """Union taxonomy tags across cluster members."""
    aggregated = defaultdict(set)
    for m in members:
        tax = m.get("taxonomy") or {}
        for axis, values in tax.items():
            if isinstance(values, list):
                aggregated[axis].update(values)
            elif isinstance(values, str):
                aggregated[axis].add(values)
    return {k: sorted(v) for k, v in aggregated.items()}


def _humanize_window(hours):
    """Render the lookback as a human-friendly string for the agent."""
    if hours <= 24:
        return f"{hours} hours"
    days = hours / 24
    if days == int(days):
        days = int(days)
    return f"{days} day{'s' if days != 1 else ''}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def serializable(item):
    """Strip non-JSON-serializable fields."""
    out = {k: v for k, v in item.items() if k not in ("published_dt", "tokens", "strong_signals")}
    return out


def resolve_lookback_hours():
    """Resolve the lookback window from CLI arg > env var > default."""
    parser = argparse.ArgumentParser(description="CTI feed aggregator and briefing packet builder.")
    parser.add_argument(
        "--lookback-hours",
        type=int,
        default=None,
        help=f"How far back to consider items (default: {DEFAULT_LOOKBACK_HOURS}). "
             "Common: 24, 36, 168 (1 week), 336 (2 weeks).",
    )
    args, _ = parser.parse_known_args()

    if args.lookback_hours is not None:
        return args.lookback_hours, "cli"

    env_val = os.environ.get("LOOKBACK_HOURS")
    if env_val:
        try:
            return int(env_val), "env"
        except ValueError:
            print(f"WARNING: invalid LOOKBACK_HOURS={env_val!r}, using default", file=sys.stderr)

    return DEFAULT_LOOKBACK_HOURS, "default"


def main():
    lookback_hours, source = resolve_lookback_hours()

    feeds_file = Path("feeds.yaml")
    feed_output = Path("docs/feed.json")
    briefing_output = Path("docs/briefing_packet.json")
    feed_output.parent.mkdir(parents=True, exist_ok=True)

    with open(feeds_file) as f:
        config = yaml.safe_load(f)

    cohorts = config.get("source_cohorts", {})

    cohort_metadata = {}
    fetch_tasks = []
    for cohort_name, cohort_data in cohorts.items():
        sources = cohort_data.get("sources", [])
        cohort_metadata[cohort_name] = {
            "description": cohort_data.get("description", ""),
            "source_count": len(sources),
            "weight": COHORT_WEIGHTS.get(cohort_name, 3),
        }
        for source_entry in sources:
            fetch_tasks.append((source_entry, cohort_name))

    print(f"Fetching {len(fetch_tasks)} feeds across {len(cohorts)} cohorts...")
    print(f"Lookback window: {lookback_hours} hours ({_humanize_window(lookback_hours)}) [from {source}]\n")

    all_items = []
    feed_status = {}

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = {
            executor.submit(parse_feed, src["name"], src["url"], cohort, lookback_hours): (src, cohort)
            for src, cohort in fetch_tasks
        }
        for future in as_completed(futures):
            src, cohort = futures[future]
            try:
                items, status = future.result()
            except Exception as e:
                print(f"  ERROR: {src['name']}: {e}", file=sys.stderr)
                items, status = [], "fetch_error"

            in_window = sum(1 for i in items if i["in_window"])
            symbol = "OK" if status == "ok" else "FAIL"
            print(f"  [{symbol}] {src['name']:40s} ({cohort}): {len(items)} items, {in_window} in window")

            feed_status[src["name"]] = {
                "url": src["url"],
                "cohort": cohort,
                "status": status,
                "item_count": len(items),
                "in_window_count": in_window,
            }
            all_items.extend(items)

    # Score items in the lookback window.
    window_items = [i for i in all_items if i["in_window"]]
    for item in window_items:
        item["score"] = score_item(item)

    print(f"\nScored {len(window_items)} items in {lookback_hours}h window")

    # Cluster.
    clusters = cluster_items(window_items)
    print(f"Clustered into {len(clusters)} stories")

    # Build briefing packet (this also full-fetches top reps).
    briefing = build_briefing_packet(clusters, all_items, feed_status, cohort_metadata, lookback_hours)

    # Write raw feed.json (all items, for transparency / debugging).
    raw_feed = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lookback_hours": lookback_hours,
        "lookback_human": _humanize_window(lookback_hours),
        "total_items": len(all_items),
        "feed_status": feed_status,
        "cohorts": cohort_metadata,           # build-page.js reads feed.cohorts
        "cohort_metadata": cohort_metadata,   # kept for any new tooling
        "affinity_groups": briefing.get("affinity_groups", []),
        "items": [serializable(i) for i in sorted(
            all_items,
            key=lambda x: x.get("published") or "0",
            reverse=True
        )],
    }
    with open(feed_output, "w") as f:
        json.dump(raw_feed, f, indent=2, ensure_ascii=False, default=str)

    # Write briefing packet.
    with open(briefing_output, "w") as f:
        json.dump(briefing, f, indent=2, ensure_ascii=False, default=str)

    ok = briefing["feeds_ok"]
    print(f"\nDone.")
    print(f"  Feeds OK:           {ok}/{len(feed_status)}")
    print(f"  Items in window:    {briefing['total_items_in_window']}")
    print(f"  Clusters in packet: {briefing['total_clusters_in_packet']}")
    print(f"  Full-fetched:       {sum(1 for c in briefing['clusters'] if c['primary']['fetch_status'] == 'ok')}")
    print(f"  Outputs:            {feed_output}, {briefing_output}")


if __name__ == "__main__":
    main()
