"""
Forward-looking signal extraction across PHANTOMSignal runs.

This module is what makes the feed see around corners. It maintains state
across runs (docs/signals_state.json) and computes signals that no
single-snapshot view can produce:

  - novelty       : CVEs / actors / products appearing for the first time
  - velocity      : multi-source bursts within a tight time window
  - leading_edge  : Reddit/practitioner cohort posts that precede Tier 1
                    coverage of the same strong signal
  - convergence   : previously-uncorrelated CVEs/actors now co-occurring
  - drift         : an actor's industry-mix or product-mix shifting over time
  - persistence   : CVEs that keep surfacing weeks after initial disclosure
                    (the long-tail-exploitation tell)
  - tier_inversion: Tier 5 chatter knowing a story before Tier 1 publishes

The state file is small (curated to last 90 days of observations) and is
safe to commit alongside feed.json. It is the memory the feed otherwise
lacks.

Usage from aggregate.py:

    from signals import SignalState, compute_signals

    state = SignalState.load(Path("docs/signals_state.json"))
    signals_block = compute_signals(briefing, state)
    state.update_from_briefing(briefing)
    state.save(Path("docs/signals_state.json"))

    briefing["forward_signals"] = signals_block
"""

import json
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path


# Window for "first time seen" — anything not seen in this trailing window
# counts as novel.
NOVELTY_WINDOW_DAYS = 28

# Tight time window for high-velocity bursts (hours)
VELOCITY_WINDOW_HOURS = 6

# Minimum sources to call a story high-velocity
VELOCITY_MIN_SOURCES = 3

# Lead time required for a leading-edge call (Reddit/practitioner ahead of Tier 1)
LEADING_EDGE_MIN_HOURS = 6
LEADING_EDGE_MAX_HOURS = 96

# Persistence: signals seen across this many runs / weeks
PERSISTENCE_WEEK_MIN = 3

# State retention
STATE_RETENTION_DAYS = 90


def _now():
    return datetime.now(timezone.utc)


def _parse_dt(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None


class SignalState:
    """Persistent memory of strong-signal observations across runs."""

    def __init__(self, observations=None, last_run=None):
        # observations[axis][value] = list of {"ts": iso, "cohort": ..., "tier": ..., "industries": [...], "products": [...]}
        self.observations = observations or {
            "cve_ids": defaultdict(list),
            "actor_attribution": defaultdict(list),
            "affected_products": defaultdict(list),
        }
        # Co-occurrence: pairs of (axis_a:value_a, axis_b:value_b) -> list of ts
        self.co_occurrence = defaultdict(list)
        self.last_run = last_run

    @classmethod
    def load(cls, path):
        if not path.exists():
            return cls()
        try:
            with open(path) as f:
                raw = json.load(f)
        except (IOError, json.JSONDecodeError):
            return cls()

        obs = {axis: defaultdict(list) for axis in ("cve_ids", "actor_attribution", "affected_products")}
        for axis in obs:
            for k, v in raw.get("observations", {}).get(axis, {}).items():
                obs[axis][k] = v

        state = cls(observations=obs, last_run=raw.get("last_run"))
        for k, v in raw.get("co_occurrence", {}).items():
            state.co_occurrence[k] = v
        return state

    def save(self, path):
        self._prune_old()
        payload = {
            "last_run": _now().isoformat(),
            "observations": {axis: dict(d) for axis, d in self.observations.items()},
            "co_occurrence": dict(self.co_occurrence),
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(payload, f, indent=2, default=str)

    def _prune_old(self):
        cutoff = _now() - timedelta(days=STATE_RETENTION_DAYS)
        for axis, d in self.observations.items():
            for k in list(d.keys()):
                d[k] = [obs for obs in d[k] if _parse_dt(obs["ts"]) and _parse_dt(obs["ts"]) > cutoff]
                if not d[k]:
                    del d[k]
        for k in list(self.co_occurrence.keys()):
            self.co_occurrence[k] = [
                ts for ts in self.co_occurrence[k]
                if _parse_dt(ts) and _parse_dt(ts) > cutoff
            ]
            if not self.co_occurrence[k]:
                del self.co_occurrence[k]

    def first_seen(self, axis, value):
        history = self.observations.get(axis, {}).get(value, [])
        if not history:
            return None
        return min(_parse_dt(h["ts"]) for h in history if _parse_dt(h["ts"]))

    def is_novel(self, axis, value, ts):
        """Has this value never been observed before `ts` minus NOVELTY_WINDOW?"""
        first = self.first_seen(axis, value)
        if first is None:
            return True
        return (ts - first).days < 1  # really fresh

    def update_from_briefing(self, briefing):
        for cluster in briefing.get("clusters", []):
            ts = _parse_dt(cluster.get("primary", {}).get("published")) or _now()
            tax = cluster.get("taxonomy") or {}
            tier = cluster.get("primary", {}).get("taxonomy", {}).get("confidence_tier", "tier_4_news")
            cohort = cluster.get("primary", {}).get("cohort", "")
            industries = tax.get("affected_industries", [])
            products = tax.get("affected_products", [])

            for axis in ("cve_ids", "actor_attribution", "affected_products"):
                for value in tax.get(axis, []):
                    self.observations[axis][value].append({
                        "ts": ts.isoformat(),
                        "cohort": cohort,
                        "tier": tier,
                        "industries": industries,
                        "products": products,
                    })

            # Co-occurrence updates
            strong_pairs = []
            for cve in tax.get("cve_ids", []):
                for actor in tax.get("actor_attribution", []):
                    strong_pairs.append(f"cve_ids:{cve}|actor_attribution:{actor}")
                for prod in tax.get("affected_products", []):
                    strong_pairs.append(f"cve_ids:{cve}|affected_products:{prod}")
            for actor in tax.get("actor_attribution", []):
                for prod in tax.get("affected_products", []):
                    strong_pairs.append(f"actor_attribution:{actor}|affected_products:{prod}")
            for pair_key in strong_pairs:
                self.co_occurrence[pair_key].append(ts.isoformat())


# ---------------------------------------------------------------------------
# Signal computation
# ---------------------------------------------------------------------------

def compute_signals(briefing, state):
    """Return a dict of forward-looking signals for this briefing."""
    return {
        "novelty": _compute_novelty(briefing, state),
        "velocity": _compute_velocity(briefing),
        "leading_edge": _compute_leading_edge(briefing, state),
        "convergence": _compute_convergence(briefing, state),
        "drift": _compute_drift(briefing, state),
        "persistence": _compute_persistence(briefing, state),
        "tier_inversion": _compute_tier_inversion(briefing, state),
    }


def _compute_novelty(briefing, state):
    """Strong signals appearing for the first time in the trailing window."""
    novel_cves = []
    novel_actors = []
    novel_products = []

    for cluster in briefing.get("clusters", []):
        tax = cluster.get("taxonomy") or {}
        pub_ts = _parse_dt(cluster.get("primary", {}).get("published")) or _now()
        for cve in tax.get("cve_ids", []):
            first = state.first_seen("cve_ids", cve)
            if first is None:
                novel_cves.append({
                    "value": cve,
                    "cluster_id": cluster.get("cluster_id"),
                    "first_source": cluster.get("primary", {}).get("source"),
                    "first_published": pub_ts.isoformat(),
                })
        for actor in tax.get("actor_attribution", []):
            first = state.first_seen("actor_attribution", actor)
            if first is None:
                novel_actors.append({
                    "value": actor,
                    "cluster_id": cluster.get("cluster_id"),
                    "first_source": cluster.get("primary", {}).get("source"),
                    "first_published": pub_ts.isoformat(),
                })
        for prod in tax.get("affected_products", []):
            first = state.first_seen("affected_products", prod)
            if first is None:
                novel_products.append({
                    "value": prod,
                    "cluster_id": cluster.get("cluster_id"),
                    "first_source": cluster.get("primary", {}).get("source"),
                    "first_published": pub_ts.isoformat(),
                })

    return {
        "cves": novel_cves[:20],
        "actors": novel_actors[:20],
        "products": novel_products[:20],
    }


def _compute_velocity(briefing):
    """Clusters where >=N independent cohorts published within VELOCITY_WINDOW_HOURS."""
    fast_clusters = []
    for cluster in briefing.get("clusters", []):
        members = cluster.get("corroborating_sources", []) or cluster.get("members", [])
        if len(members) < VELOCITY_MIN_SOURCES:
            continue
        timestamps = sorted(filter(None, (_parse_dt(m.get("published")) for m in members)))
        if len(timestamps) < VELOCITY_MIN_SOURCES:
            continue
        # Find the tightest VELOCITY_MIN_SOURCES-wide window
        for i in range(len(timestamps) - VELOCITY_MIN_SOURCES + 1):
            window = timestamps[i:i + VELOCITY_MIN_SOURCES]
            span_h = (window[-1] - window[0]).total_seconds() / 3600
            if span_h <= VELOCITY_WINDOW_HOURS:
                cohort_count = len(set(m.get("cohort") for m in members))
                fast_clusters.append({
                    "cluster_id": cluster.get("cluster_id"),
                    "title": cluster.get("primary", {}).get("title"),
                    "sources_in_window": VELOCITY_MIN_SOURCES,
                    "window_hours": round(span_h, 1),
                    "cohort_count": cohort_count,
                })
                break

    fast_clusters.sort(key=lambda c: (-c["cohort_count"], c["window_hours"]))
    return fast_clusters[:10]


def _compute_leading_edge(briefing, state):
    """Reddit/practitioner cohort published before Tier 1 saw the same signal."""
    candidates = []
    for cluster in briefing.get("clusters", []):
        tax = cluster.get("taxonomy") or {}
        strong = (set(tax.get("cve_ids", []))
                  | set(tax.get("actor_attribution", []))
                  | set(tax.get("affected_products", [])))
        if not strong:
            continue

        members = cluster.get("corroborating_sources", []) or cluster.get("members", [])
        # Find earliest Reddit/practitioner publication and earliest Tier 1
        earliest_chatter = None
        earliest_tier1 = None
        for m in members:
            ts = _parse_dt(m.get("published"))
            cohort = m.get("cohort", "")
            if not ts:
                continue
            if cohort in ("reddit_practitioner_osint", "practitioner_analysis"):
                if earliest_chatter is None or ts < earliest_chatter[0]:
                    earliest_chatter = (ts, m)
            if cohort in ("threat_research_primary", "offensive_vulnerability_research", "government_authoritative"):
                if earliest_tier1 is None or ts < earliest_tier1[0]:
                    earliest_tier1 = (ts, m)

        if earliest_chatter and earliest_tier1:
            lead_h = (earliest_tier1[0] - earliest_chatter[0]).total_seconds() / 3600
            if LEADING_EDGE_MIN_HOURS <= lead_h <= LEADING_EDGE_MAX_HOURS:
                candidates.append({
                    "cluster_id": cluster.get("cluster_id"),
                    "title": cluster.get("primary", {}).get("title"),
                    "lead_hours": round(lead_h, 1),
                    "first_source": earliest_chatter[1].get("source"),
                    "later_tier1_source": earliest_tier1[1].get("source"),
                    "shared_signals": sorted(strong),
                })
    candidates.sort(key=lambda c: -c["lead_hours"])
    return candidates[:10]


def _compute_convergence(briefing, state):
    """Strong-signal pairs co-occurring for the first time, or rarely seen together."""
    converging = []
    for cluster in briefing.get("clusters", []):
        tax = cluster.get("taxonomy") or {}
        cves = tax.get("cve_ids", [])
        actors = tax.get("actor_attribution", [])
        products = tax.get("affected_products", [])
        ts = _parse_dt(cluster.get("primary", {}).get("published")) or _now()
        recent_cutoff = ts - timedelta(days=14)

        pairs_this_cluster = []
        for c in cves:
            for a in actors:
                pairs_this_cluster.append(("cve_ids", c, "actor_attribution", a))
            for p in products:
                pairs_this_cluster.append(("cve_ids", c, "affected_products", p))
        for a in actors:
            for p in products:
                pairs_this_cluster.append(("actor_attribution", a, "affected_products", p))

        for axis_a, val_a, axis_b, val_b in pairs_this_cluster:
            key = f"{axis_a}:{val_a}|{axis_b}:{val_b}"
            history = state.co_occurrence.get(key, [])
            # First-time-ever co-occurrence is the strongest convergence signal
            prior = [h for h in history if _parse_dt(h) and _parse_dt(h) < recent_cutoff]
            if not prior:
                converging.append({
                    "cluster_id": cluster.get("cluster_id"),
                    "pair": f"{val_a} + {val_b}",
                    "first_observation": True,
                })
    return converging[:15]


def _compute_drift(briefing, state):
    """An actor's industry or product targeting shifting compared to prior history."""
    drift = []
    seen_actors = set()
    for cluster in briefing.get("clusters", []):
        tax = cluster.get("taxonomy") or {}
        actors = tax.get("actor_attribution", [])
        current_industries = set(tax.get("affected_industries", []))
        current_products = set(tax.get("affected_products", []))

        for actor in actors:
            if actor in seen_actors:
                continue
            seen_actors.add(actor)
            history = state.observations.get("actor_attribution", {}).get(actor, [])
            if len(history) < 3:
                continue  # not enough prior observations to detect drift

            prior_industries = Counter()
            prior_products = Counter()
            for h in history:
                for ind in h.get("industries", []):
                    prior_industries[ind] += 1
                for p in h.get("products", []):
                    prior_products[p] += 1

            top_prior_industries = {i for i, _ in prior_industries.most_common(3)}
            top_prior_products = {p for p, _ in prior_products.most_common(3)}

            new_industries = current_industries - top_prior_industries
            new_products = current_products - top_prior_products

            if new_industries or new_products:
                drift.append({
                    "actor": actor,
                    "cluster_id": cluster.get("cluster_id"),
                    "new_industries": sorted(new_industries),
                    "new_products": sorted(new_products),
                    "prior_top_industries": sorted(top_prior_industries),
                    "prior_top_products": sorted(top_prior_products),
                })
    return drift[:10]


def _compute_persistence(briefing, state):
    """CVEs / actors / products that keep appearing across multiple weeks.

    The long-tail-exploitation tell. A CVE first published 6 weeks ago but
    still appearing in fresh clusters this week = ongoing campaign, not a
    blip.
    """
    persisting = []
    now = _now()
    for cluster in briefing.get("clusters", []):
        tax = cluster.get("taxonomy") or {}
        for axis in ("cve_ids", "actor_attribution"):
            for value in tax.get(axis, []):
                history = state.observations.get(axis, {}).get(value, [])
                weeks_seen = set()
                for h in history:
                    ts = _parse_dt(h.get("ts"))
                    if ts:
                        weeks_seen.add(ts.isocalendar()[1])
                if len(weeks_seen) >= PERSISTENCE_WEEK_MIN:
                    persisting.append({
                        "axis": axis,
                        "value": value,
                        "cluster_id": cluster.get("cluster_id"),
                        "weeks_observed": len(weeks_seen),
                    })
    # Dedupe by (axis, value)
    seen = set()
    deduped = []
    for p in sorted(persisting, key=lambda x: -x["weeks_observed"]):
        key = (p["axis"], p["value"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(p)
    return deduped[:15]


def _compute_tier_inversion(briefing, state):
    """Clusters where Tier 5 chatter is the primary anchor and no Tier 1 has covered."""
    inversions = []
    for cluster in briefing.get("clusters", []):
        members = cluster.get("corroborating_sources", []) or cluster.get("members", [])
        tiers = set()
        for m in members:
            tax = m.get("taxonomy") or {}
            tiers.add(tax.get("confidence_tier", "tier_4_news"))

        has_tier1 = any(t.startswith("tier_1") for t in tiers)
        is_chatter_anchored = "tier_5_chatter" in tiers and not has_tier1

        tax = cluster.get("taxonomy") or {}
        strong = (set(tax.get("cve_ids", []))
                  | set(tax.get("actor_attribution", [])))
        if is_chatter_anchored and strong:
            inversions.append({
                "cluster_id": cluster.get("cluster_id"),
                "title": cluster.get("primary", {}).get("title"),
                "primary_source": cluster.get("primary", {}).get("source"),
                "strong_signals": sorted(strong),
            })
    return inversions[:10]
