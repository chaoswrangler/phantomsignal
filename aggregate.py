#!/usr/bin/env python3
"""
Aggregate RSS feeds, cluster related items, fetch full content for survivors,
and produce a briefing packet ready for LLM analysis.

Outputs:
  docs/feed.json              - raw normalized feed data (transparency)
  docs/feed.html              - human-readable HTML view of feed.json
  docs/briefing_packet.json   - the curated input for the analysis agent
"""

import argparse
import hashlib
import html
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

# Local modules (v2)
from taxonomy import extract_taxonomy
from affinity import find_affinity_groups
from scoring import score_item, cluster_corroboration_boost
from signals import SignalState, compute_signals

socket.setdefaulttimeout(15)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_LOOKBACK_HOURS = 168
ITEMS_PER_FEED = 100
CLUSTER_THRESHOLD = 0.55
UA = "Mozilla/5.0 (compatible; CTI-Aggregator/1.0; +https://github.com)"
MAX_FULL_FETCH = 60
MIN_CLUSTER_SCORE = 8
MAX_CLUSTERS_IN_PACKET = 80
BODY_CHAR_LIMIT = 4000


# ---------------------------------------------------------------------------
# Feed parsing
# ---------------------------------------------------------------------------

def clean_text(s):
    if not s:
        return ""
    soup = BeautifulSoup(s, "html.parser")
    text = soup.get_text(separator=" ")
    return re.sub(r"\s+", " ", unescape(text)).strip()


def parse_feed(name, url, cohort, lookback_hours):
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
            "category": cohort,
            "title": title,
            "link": link,
            "published": pub_date.isoformat() if pub_date else None,
            "published_dt": pub_date,
            "summary": summary,
            "author": clean_text(entry.get("author", "")),
            "in_window": bool(pub_date and pub_date >= cutoff),
        }
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
# Full-article fetching
# ---------------------------------------------------------------------------

def fetch_article(url):
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

    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
        tag.decompose()

    candidates = soup.find_all(["article", "main"])
    if candidates:
        body = max(candidates, key=lambda t: len(t.get_text()))
    else:
        body = soup.body or soup

    text = re.sub(r"\s+", " ", body.get_text(separator=" ")).strip()
    return text[:BODY_CHAR_LIMIT], "ok"


# ---------------------------------------------------------------------------
# Clustering
# ---------------------------------------------------------------------------

def tokenize(text):
    stop = {
        "the", "a", "an", "and", "or", "of", "in", "on", "to", "for",
        "with", "is", "are", "was", "were", "by", "as", "at", "from",
        "that", "this", "it", "be", "has", "have", "new", "blog", "post",
    }
    tokens = re.findall(r"[a-z0-9]{3,}", text.lower())
    return {t for t in tokens if t not in stop}


def extract_strong_signals(item):
    tax = item.get("taxonomy") or {}
    signals = set()
    signals.update(tax.get("cve_ids", []))
    signals.update(tax.get("actor_attribution", []))
    role_map = tax.get("role_map", {})
    for p in tax.get("affected_products", []):
        if role_map.get(p, "target") == "target":
            signals.add(p)
    return signals


def similarity(a, b):
    if a["strong_signals"] and a["strong_signals"] & b["strong_signals"]:
        return 1.0
    if not a["tokens"] or not b["tokens"]:
        return 0.0
    intersection = a["tokens"] & b["tokens"]
    union = a["tokens"] | b["tokens"]
    return len(intersection) / len(union) if union else 0.0


def cluster_items(items):
    for item in items:
        text = f"{item['title']} {item['summary']}"
        item["tokens"] = tokenize(text)
        item["strong_signals"] = extract_strong_signals(item)

    items_sorted = sorted(items, key=lambda x: x["score"], reverse=True)
    clusters = []

    for item in items_sorted:
        best_cluster = None
        best_sim = 0.0

        for cluster in clusters:
            sim = similarity(item, cluster["rep"])
            if sim > best_sim:
                best_sim = sim
                best_cluster = cluster

        if best_cluster and best_sim >= CLUSTER_THRESHOLD:
            best_cluster["members"].append(item)
        else:
            clusters.append({
                "rep": item,
                "members": [item],
                "score": item["score"],
            })

    for cluster in clusters:
        cluster["score"] = cluster["rep"]["score"] + cluster_corroboration_boost(cluster["members"])

    return clusters


# ---------------------------------------------------------------------------
# Briefing packet assembly
# ---------------------------------------------------------------------------

def cluster_id(rep):
    seed = f"{rep['title']}|{rep['link']}"
    return hashlib.sha1(seed.encode()).hexdigest()[:10]


def build_briefing_packet(clusters, all_items, feed_status, cohort_metadata, lookback_hours):
    clusters_sorted = sorted(clusters, key=lambda c: c["score"], reverse=True)
    total_clusters_raw = len(clusters_sorted)

    clusters_filtered = [c for c in clusters_sorted if c["score"] >= MIN_CLUSTER_SCORE]
    dropped_low_score = total_clusters_raw - len(clusters_filtered)

    clusters_kept = clusters_filtered[:MAX_CLUSTERS_IN_PACKET]
    dropped_overflow = len(clusters_filtered) - len(clusters_kept)

    print(f"\nCluster pipeline:")
    print(f"  Raw clusters:           {total_clusters_raw}")
    print(f"  Dropped (score < {MIN_CLUSTER_SCORE}): {dropped_low_score}")
    print(f"  Dropped (overflow):     {dropped_overflow}")
    print(f"  Kept in packet:         {len(clusters_kept)}")

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

    briefing_clusters = []
    for c in clusters_kept:
        rep = c["rep"]
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

    raw_groups = find_affinity_groups(briefing_clusters)
    kept_cluster_ids = [c["cluster_id"] for c in briefing_clusters]
    affinity_groups = []
    for g in raw_groups:
        theme_links = []
        for ci in g["cluster_indices"]:
            cluster = briefing_clusters[ci]
            primary_link = cluster.get("primary", {}).get("link")
            if primary_link:
                theme_links.append(primary_link)
            for cs in cluster.get("corroborating_sources", []):
                link = cs.get("link")
                if link and link not in theme_links:
                    theme_links.append(link)

        theme_key = re.sub(r"[^a-zA-Z0-9._-]+", "-", g["anchor_signal"]).strip("-").lower()

        affinity_groups.append({
            "label": g["label"],
            "anchor_signal": g["anchor_signal"],
            "theme_key": theme_key,
            "dominant_features": g["dominant_features"],
            "cluster_count": g["cluster_count"],
            "article_count": g["article_count"],
            "cohesion": g["cohesion"],
            "shared_strong_signals": g.get("shared_strong_signals", []),
            "member_cves": sorted(set(g.get("member_cves", []))),
            "also_targets": sorted(set(g.get("also_targets", []))),
            "cluster_ids": [kept_cluster_ids[i] for i in g["cluster_indices"]],
            "links": theme_links,
        })

    print(f"\nAffinity groups detected: {len(affinity_groups)}")
    for g in affinity_groups[:5]:
        print(f"  - {g['label']} ({g['cluster_count']} clusters, {g['article_count']} articles)")

    state_path = Path("docs/signals_state.json")
    state = SignalState.load(state_path)
    forward_signals = compute_signals({"clusters": briefing_clusters}, state)
    state.update_from_briefing({"clusters": briefing_clusters})
    state.save(state_path)

    print(f"\nForward signals:")
    print(f"  Novel CVEs:      {len(forward_signals['novelty']['cves'])}")
    print(f"  Novel actors:    {len(forward_signals['novelty']['actors'])}")
    print(f"  Velocity bursts: {len(forward_signals['velocity'])}")
    print(f"  Leading edge:    {len(forward_signals['leading_edge'])}")
    print(f"  Tier inversions: {len(forward_signals['tier_inversion'])}")

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
        "forward_signals": forward_signals,
    }


def _aggregate_cluster_taxonomy(members):
    aggregated = defaultdict(set)
    for m in members:
        tax = m.get("taxonomy") or {}
        for axis, values in tax.items():
            if isinstance(values, list):
                aggregated[axis].update(values)
            elif isinstance(values, str):
                aggregated[axis].add(values)
    return {k: sorted(v) for k, v in aggregated.items()}


def briefing_to_markdown(briefing):
    """Render the briefing dict as markdown. Preserves every field of the JSON.

    The markdown is structured so an LLM agent can parse it the same way it
    would parse the JSON — headings map to top-level sections, bullet lists
    map to objects, and code fences wrap free-form text (titles, summaries,
    full bodies) so embedded markdown in source content doesn't get treated
    as document structure.
    """
    lines = []

    # --- Metadata header -----------------------------------------------------
    lines.append("# PHANTOMSignal Briefing Packet")
    lines.append("")
    lines.append(f"- Generated: {briefing.get('generated_at', '')}")
    lines.append(f"- Lookback hours: {briefing.get('lookback_hours', '')}")
    lines.append(f"- Lookback human: {briefing.get('lookback_human', '')}")
    lines.append(f"- Total feeds: {briefing.get('total_feeds', 0)}")
    lines.append(f"- Feeds OK: {briefing.get('feeds_ok', 0)}")
    lines.append(f"- Total items in window: {briefing.get('total_items_in_window', 0)}")
    lines.append(f"- Total clusters raw: {briefing.get('total_clusters_raw', 0)}")
    lines.append(f"- Total clusters in packet: {briefing.get('total_clusters_in_packet', 0)}")
    lines.append(f"- Dropped low score: {briefing.get('dropped_low_score', 0)}")
    lines.append(f"- Dropped overflow: {briefing.get('dropped_overflow', 0)}")
    lines.append("")

    # --- Cohort metadata -----------------------------------------------------
    lines.append("## Cohort metadata")
    lines.append("")
    for cohort_name, meta in (briefing.get("cohort_metadata") or {}).items():
        lines.append(f"### {cohort_name}")
        lines.append(f"- Description: {meta.get('description', '')}")
        lines.append(f"- Source count: {meta.get('source_count', 0)}")
        lines.append(f"- Weight: {meta.get('weight', 0)}")
        lines.append("")

    # --- Feed status ---------------------------------------------------------
    lines.append("## Feed status")
    lines.append("")
    for name, st in (briefing.get("feed_status") or {}).items():
        lines.append(f"- **{name}** ({st.get('cohort', '')})")
        lines.append(f"  - URL: {st.get('url', '')}")
        lines.append(f"  - Status: {st.get('status', '')}")
        lines.append(f"  - Item count: {st.get('item_count', 0)}")
        lines.append(f"  - In window count: {st.get('in_window_count', 0)}")
    lines.append("")

    # --- Affinity groups -----------------------------------------------------
    lines.append("## Affinity groups (themes)")
    lines.append("")
    for g in briefing.get("affinity_groups", []):
        lines.append(f"### {g.get('label', 'unnamed theme')}")
        lines.append(f"- Anchor signal: {g.get('anchor_signal', '')}")
        lines.append(f"- Theme key: {g.get('theme_key', '')}")
        lines.append(f"- Cluster count: {g.get('cluster_count', 0)}")
        lines.append(f"- Article count: {g.get('article_count', 0)}")
        lines.append(f"- Cohesion: {g.get('cohesion', 0)}")
        shared = g.get("shared_strong_signals") or []
        lines.append(f"- Shared strong signals: {', '.join(shared) if shared else '(none)'}")
        cves = g.get("member_cves") or []
        lines.append(f"- Member CVEs: {', '.join(cves) if cves else '(none)'}")
        also = g.get("also_targets") or []
        lines.append(f"- Also targets: {', '.join(also) if also else '(none)'}")
        dom = g.get("dominant_features") or {}
        if dom:
            lines.append("- Dominant features:")
            for axis, vals in dom.items():
                if isinstance(vals, list) and vals:
                    lines.append(f"  - {axis}: {', '.join(vals)}")
        cluster_ids = g.get("cluster_ids") or []
        lines.append(f"- Cluster IDs: {', '.join(cluster_ids) if cluster_ids else '(none)'}")
        links = g.get("links") or []
        if links:
            lines.append("- Links:")
            for link in links:
                lines.append(f"  - {link}")
        lines.append("")

    # --- Forward signals -----------------------------------------------------
    fs = briefing.get("forward_signals") or {}
    if fs:
        lines.append("## Forward signals")
        lines.append("")

        novelty = fs.get("novelty") or {}
        lines.append("### Novelty")
        for axis in ("cves", "actors", "products"):
            entries = novelty.get(axis) or []
            lines.append(f"- Novel {axis}: {len(entries)}")
            for entry in entries:
                lines.append(
                    f"  - {entry.get('value', '')} "
                    f"(first seen via {entry.get('first_source', '')} "
                    f"at {entry.get('first_published', '')}, "
                    f"cluster {entry.get('cluster_id', '')})"
                )
        lines.append("")

        velocity = fs.get("velocity") or []
        lines.append(f"### Velocity bursts ({len(velocity)})")
        for v in velocity:
            lines.append(f"- **{v.get('title', '')}**")
            lines.append(f"  - Cluster: {v.get('cluster_id', '')}")
            lines.append(f"  - Sources in window: {v.get('sources_in_window', 0)}")
            lines.append(f"  - Window hours: {v.get('window_hours', 0)}")
            lines.append(f"  - Cohort count: {v.get('cohort_count', 0)}")
        lines.append("")

        leading = fs.get("leading_edge") or []
        lines.append(f"### Leading edge ({len(leading)})")
        for le in leading:
            lines.append(f"- **{le.get('title', '')}**")
            lines.append(f"  - Cluster: {le.get('cluster_id', '')}")
            lines.append(f"  - Lead hours: {le.get('lead_hours', 0)}")
            lines.append(f"  - First source: {le.get('first_source', '')}")
            lines.append(f"  - Later Tier 1 source: {le.get('later_tier1_source', '')}")
            shared = le.get("shared_signals") or []
            lines.append(f"  - Shared signals: {', '.join(shared) if shared else '(none)'}")
        lines.append("")

        convergence = fs.get("convergence") or []
        lines.append(f"### Convergence ({len(convergence)})")
        for c in convergence:
            lines.append(
                f"- Pair: {c.get('pair', '')} "
                f"(cluster {c.get('cluster_id', '')}, "
                f"first observation: {c.get('first_observation', False)})"
            )
        lines.append("")

        drift = fs.get("drift") or []
        lines.append(f"### Drift ({len(drift)})")
        for d in drift:
            lines.append(f"- **{d.get('actor', '')}** (cluster {d.get('cluster_id', '')})")
            new_ind = d.get("new_industries") or []
            new_prod = d.get("new_products") or []
            prior_ind = d.get("prior_top_industries") or []
            prior_prod = d.get("prior_top_products") or []
            lines.append(f"  - New industries: {', '.join(new_ind) if new_ind else '(none)'}")
            lines.append(f"  - New products: {', '.join(new_prod) if new_prod else '(none)'}")
            lines.append(f"  - Prior top industries: {', '.join(prior_ind) if prior_ind else '(none)'}")
            lines.append(f"  - Prior top products: {', '.join(prior_prod) if prior_prod else '(none)'}")
        lines.append("")

        persistence = fs.get("persistence") or []
        lines.append(f"### Persistence ({len(persistence)})")
        for p in persistence:
            lines.append(
                f"- {p.get('axis', '')}: {p.get('value', '')} "
                f"(weeks observed: {p.get('weeks_observed', 0)}, "
                f"cluster {p.get('cluster_id', '')})"
            )
        lines.append("")

        inversion = fs.get("tier_inversion") or []
        lines.append(f"### Tier inversion ({len(inversion)})")
        for ti in inversion:
            lines.append(f"- **{ti.get('title', '')}**")
            lines.append(f"  - Cluster: {ti.get('cluster_id', '')}")
            lines.append(f"  - Primary source: {ti.get('primary_source', '')}")
            sigs = ti.get("strong_signals") or []
            lines.append(f"  - Strong signals: {', '.join(sigs) if sigs else '(none)'}")
        lines.append("")

    # --- Clusters ------------------------------------------------------------
    lines.append("## Clusters")
    lines.append("")
    for c in briefing.get("clusters", []):
        cid = c.get("cluster_id", "")
        rep = c.get("primary") or {}
        lines.append(f"### Cluster {cid} — score {c.get('priority_score', 0)}")
        lines.append("")
        lines.append(f"- Title: {rep.get('title', '')}")
        lines.append(f"- Source: {rep.get('source', '')} ({rep.get('cohort', '')})")
        lines.append(f"- Published: {rep.get('published', '')}")
        lines.append(f"- Link: {rep.get('link', '')}")
        lines.append(f"- Fetch status: {rep.get('fetch_status', '')}")
        lines.append(f"- Member count: {c.get('member_count', 0)}")
        lines.append(f"- Corroborating source count: {c.get('corroborating_source_count', 0)}")
        strong = c.get("strong_signals") or []
        lines.append(f"- Strong signals: {', '.join(strong) if strong else '(none)'}")
        lines.append("")

        # Aggregate cluster taxonomy
        ctax = c.get("taxonomy") or {}
        if ctax:
            lines.append("#### Cluster taxonomy (union across members)")
            for axis, vals in ctax.items():
                if isinstance(vals, list) and vals:
                    lines.append(f"- {axis}: {', '.join(str(v) for v in vals)}")
            lines.append("")

        # Primary-article taxonomy (more detailed than aggregate)
        ptax = rep.get("taxonomy") or {}
        if ptax:
            lines.append("#### Primary article taxonomy")
            for axis, vals in ptax.items():
                if axis in ("role_map", "weak_tags"):
                    continue  # debug-only fields, skip from agent-facing markdown
                if isinstance(vals, list):
                    if vals:
                        lines.append(f"- {axis}: {', '.join(str(v) for v in vals)}")
                elif vals:
                    lines.append(f"- {axis}: {vals}")
            lines.append("")

        # Summary
        summary = (rep.get("summary") or "").strip()
        if summary:
            lines.append("#### Summary")
            lines.append("")
            lines.append("```")
            lines.append(summary)
            lines.append("```")
            lines.append("")

        # Full body
        body = (rep.get("full_body") or "").strip()
        if body:
            lines.append("#### Full body")
            lines.append("")
            lines.append("```")
            lines.append(body)
            lines.append("```")
            lines.append("")

        # Corroborating sources
        corr = c.get("corroborating_sources") or []
        if corr:
            lines.append(f"#### Corroborating sources ({len(corr)})")
            lines.append("")
            for cs in corr:
                lines.append(f"- **{cs.get('source', '')}** ({cs.get('cohort', '')})")
                lines.append(f"  - Title: {cs.get('title', '')}")
                lines.append(f"  - Published: {cs.get('published', '')}")
                lines.append(f"  - Link: {cs.get('link', '')}")
                cs_sum = (cs.get("summary") or "").strip()
                if cs_sum:
                    lines.append(f"  - Summary: {cs_sum}")
            lines.append("")

    return "\n".join(lines)

def items_to_rss(raw_feed, site_url="https://chaoswrangler.github.io/phantomsignal/"):
    """Render the in-window item list as RSS 2.0 XML for Outlook / Feedly / etc.

    Spec: RSS 2.0 with atom:link self-reference (recommended by RSS Best
    Practices Profile and required by some validators / readers).

    Notes:
      - Dates are RFC 822 format via email.utils.format_datetime(). Outlook
        is strict on this — ISO 8601 dates silently fail to register pubDate.
      - <description> is CDATA-wrapped so the summary doesn't need character
        escaping. summaries are already plain text (clean_text strips HTML),
        but CDATA insulates against future changes.
      - <guid> uses the article URL with isPermaLink="true" so Outlook
        de-duplicates correctly even if the same article appears twice
        across runs.
      - <source> element attributes the original RSS feed the item came
        from, which Outlook displays in its source column.
      - Items already filtered (out_of_scope, low_signal) by main(); we
        consume raw_feed["items"] directly which has the filter applied.
    """
    from email.utils import format_datetime
    from datetime import datetime, timezone

    feed_status = raw_feed.get("feed_status") or {}
    items = raw_feed.get("items") or []

    # Sort newest first, defensively
    def _parse(p):
        if not p:
            return datetime.min.replace(tzinfo=timezone.utc)
        try:
            return datetime.fromisoformat(p.replace("Z", "+00:00"))
        except (ValueError, TypeError):
            return datetime.min.replace(tzinfo=timezone.utc)

    items = sorted(items, key=lambda i: _parse(i.get("published")), reverse=True)

    # Build channel-level dates
    now = datetime.now(timezone.utc)
    last_build = format_datetime(now)

    rss_url = site_url.rstrip("/") + "/rss.xml"
    n_items = len(items)
    n_sources = sum(1 for s in feed_status.values() if s.get("status") == "ok")
    lookback_human = raw_feed.get("lookback_human", "")

    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">')
    parts.append("<channel>")
    parts.append("<title>PHANTOMSignal Feed</title>")
    parts.append(f"<link>{_xml_escape(site_url)}</link>")
    parts.append(f'<atom:link href="{_xml_escape(rss_url)}" rel="self" type="application/rss+xml" />')
    parts.append(
        "<description>"
        f"Curated CTI from {n_sources} sources over {_xml_escape(lookback_human)}. "
        "Filtered for relevance, deduplicated, tagged by threat category and likely affected industry."
        "</description>"
    )
    parts.append("<language>en-us</language>")
    parts.append(f"<lastBuildDate>{last_build}</lastBuildDate>")
    parts.append("<generator>PHANTOMSignal aggregator</generator>")
    parts.append("<ttl>60</ttl>")

    for item in items:
        title = item.get("title", "")
        link = item.get("link", "")
        summary = item.get("summary", "")
        published = item.get("published")
        source_name = item.get("source", "")
        cohort = item.get("cohort", "")

        # pubDate in RFC 822
        pub_dt = _parse(published)
        if pub_dt == datetime.min.replace(tzinfo=timezone.utc):
            pub_rfc822 = last_build  # fallback for items without dates
        else:
            pub_rfc822 = format_datetime(pub_dt)

        # Description: summary plus a small taxonomy footer if useful
        tax = item.get("taxonomy") or {}
        tags = []
        for axis in ("affected_products", "actor_attribution", "cve_ids", "threat_categories"):
            vals = tax.get(axis) or []
            tags.extend(vals)
        # Dedupe while preserving order, cap at 8 tags
        seen = set()
        deduped = []
        for t in tags:
            if t not in seen:
                seen.add(t)
                deduped.append(t)
        deduped = deduped[:8]

        description_html = _xml_escape(summary)
        if deduped:
            tag_html = " · ".join(_xml_escape(t) for t in deduped)
            description_html = f"{description_html}<br/><br/><em>Tags: {tag_html}</em>"

        source_rss_url = (feed_status.get(source_name) or {}).get("url", "")

        parts.append("<item>")
        parts.append(f"<title>{_xml_escape(title)}</title>")
        parts.append(f"<link>{_xml_escape(link)}</link>")
        parts.append(f"<description><![CDATA[{description_html}]]></description>")
        parts.append(f"<pubDate>{pub_rfc822}</pubDate>")
        parts.append(f'<guid isPermaLink="true">{_xml_escape(link)}</guid>')
        if source_rss_url:
            parts.append(f'<source url="{_xml_escape(source_rss_url)}">{_xml_escape(source_name)}</source>')
        else:
            parts.append(f'<dc:creator>{_xml_escape(source_name)}</dc:creator>')
        if cohort:
            parts.append(f"<category>{_xml_escape(cohort)}</category>")
        # Surface taxonomy categories too so Outlook category filters work
        for tag in deduped[:4]:
            parts.append(f"<category>{_xml_escape(tag)}</category>")
        parts.append("</item>")

    parts.append("</channel>")
    parts.append("</rss>")

    return "\n".join(parts)


def _xml_escape(s):
    """Escape for XML element content and attribute values."""
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def _humanize_window(hours):
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
    out = {k: v for k, v in item.items() if k not in ("published_dt", "tokens", "strong_signals")}
    return out


def resolve_lookback_hours():
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
    feed_html_output = Path("docs/feed.html")
    briefing_output = Path("docs/briefing_packet.json")
    briefing_md_output = Path("docs/briefing_packet.md")
    rss_output = Path("docs/rss.xml")
    feed_output.parent.mkdir(parents=True, exist_ok=True)

    with open(feeds_file) as f:
        config = yaml.safe_load(f)

    cohorts = config.get("source_cohorts", {})

    from scoring import COHORT_BASE
    cohort_metadata = {}
    fetch_tasks = []
    for cohort_name, cohort_data in cohorts.items():
        sources = cohort_data.get("sources", [])
        cohort_metadata[cohort_name] = {
            "description": cohort_data.get("description", ""),
            "source_count": len(sources),
            "weight": COHORT_BASE.get(cohort_name, 3),
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

    window_items = [i for i in all_items if i["in_window"]]

    filtered_dropped = {"out_of_scope": 0, "low_signal": 0}
    cti_items = []
    for item in window_items:
        ct = (item.get("taxonomy") or {}).get("content_type")
        if ct in filtered_dropped:
            item["filtered"] = ct
            filtered_dropped[ct] += 1
            continue
        cti_items.append(item)
    window_items = cti_items
    for k, n in filtered_dropped.items():
        if n:
            print(f"Filtered {n} {k} items")

    for item in window_items:
        item["score"] = score_item(item)

    print(f"\nScored {len(window_items)} items in {lookback_hours}h window")

    clusters = cluster_items(window_items)
    print(f"Clustered into {len(clusters)} stories")

    briefing = build_briefing_packet(clusters, all_items, feed_status, cohort_metadata, lookback_hours)

    raw_feed = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lookback_hours": lookback_hours,
        "lookback_human": _humanize_window(lookback_hours),
        "total_items": len(all_items),
        "feed_status": feed_status,
        "cohorts": cohort_metadata,
        "cohort_metadata": cohort_metadata,
        "affinity_groups": briefing.get("affinity_groups", []),
        "forward_signals": briefing.get("forward_signals", {}),
        "items": [serializable(i) for i in sorted(
            (it for it in all_items if it.get("filtered") not in ("out_of_scope", "low_signal")),
            key=lambda x: x.get("published") or "0",
            reverse=True
        )],
    }

    # Write raw feed.json.
    with open(feed_output, "w") as f:
        json.dump(raw_feed, f, indent=2, ensure_ascii=False, default=str)

    # Also emit a human-readable HTML view of the raw feed.
    pretty = json.dumps(raw_feed, indent=2, ensure_ascii=False, default=str)
    feed_html = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<title>PHANTOMSignal feed.json</title>'
        '<style>body{margin:0;background:#0b0f14;color:#e8f4ff;'
        "font-family:'JetBrains Mono',Consolas,monospace}"
        'pre{margin:0;padding:24px;font-size:13px;line-height:1.5;'
        'white-space:pre-wrap;word-break:break-word}</style></head>'
        f'<body><pre>{html.escape(pretty)}</pre></body></html>'
    )
    feed_html_output.write_text(feed_html, encoding="utf-8")

    # Write briefing packet (JSON + markdown for the agent).
    with open(briefing_output, "w") as f:
        json.dump(briefing, f, indent=2, ensure_ascii=False, default=str)
    briefing_md_output.write_text(briefing_to_markdown(briefing), encoding="utf-8")

    # Write RSS 2.0 feed for Outlook / Feedly / generic readers.
    # All in-window items (post-filter), newest first, with taxonomy tags
    # surfaced as categories so reader-side filtering works.
    rss_output.write_text(items_to_rss(raw_feed), encoding="utf-8")

    ok = briefing["feeds_ok"]
    print(f"\nDone.")
    print(f"  Feeds OK:           {ok}/{len(feed_status)}")
    print(f"  Items in window:    {briefing['total_items_in_window']}")
    print(f"  Clusters in packet: {briefing['total_clusters_in_packet']}")
    print(f"  Full-fetched:       {sum(1 for c in briefing['clusters'] if c['primary']['fetch_status'] == 'ok')}")
    print(f"  Outputs:            {feed_output}, {feed_html_output}, {briefing_output}, {briefing_md_output}, {rss_output}")


if __name__ == "__main__":
    main()
