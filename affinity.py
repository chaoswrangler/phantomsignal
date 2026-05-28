"""
Affinity grouping for CTI clusters — v2.

Differences from v1:

  1. STRONG-SIGNAL REQUIREMENT
     Two clusters can only merge if they share at least one strong signal
     (CVE, actor, or specific product as TARGET). Mere category overlap is
     not enough. This kills the "GitHub + zero_day + Anthropic/Claude" false
     positives that v1 produced.

  2. ROLE-AWARE FEATURE SETS
     Products tagged as `tool` or `vendor` (e.g., Claude as exploit-writing
     tool, GitHub as hosting platform) are excluded from the affinity feature
     vector. Only `target` products count.

  3. REPRESENTATIVE-ONLY MATCHING
     v1 took the union of every member's taxonomy. One polluted member
     poisoned the cluster's fingerprint. v2 uses the cluster representative's
     taxonomy only (the one we full-fetched and re-enriched), plus a curated
     union from corroborating sources that share the rep's strong signals.

  4. CONFIDENCE-WEIGHTED COHESION
     Cohesion now factors in the confidence_tier of cluster members. A theme
     anchored by Tier 1 research with Tier 4 corroboration scores higher than
     a theme made of five Tier 4 news stories alone.

  5. LABEL DISAMBIGUATION
     Labels now distinguish role:
       - "{Actor} targeting {Product}"           (actor + product target)
       - "{Actor} {category} activity"            (actor + category)
       - "{Category} targeting {Product}"        (category + product target)
       - "{Product} exploitation wave"           (product + active_exploitation urgency)
     Generic labels like "malware activity" are rejected entirely.
"""

from collections import Counter, defaultdict
from itertools import combinations


# Strong-signal axes: must share at least one of these to merge.
STRONG_SIGNAL_AXES = ("cve_ids", "actor_attribution", "affected_products")

# Feature weights for the similarity computation.
FEATURE_WEIGHTS = {
    "cve_ids": 5.0,              # Same CVE = strongest possible signal
    "actor_attribution": 4.0,
    "affected_products": 3.0,    # target products only
    "threat_categories": 1.5,
    "attack_techniques": 2.0,
    "affected_industries": 1.0,
    "urgency_signals": 0.5,
    "geographic_scope": 0.3,
}

# Confidence tier weights — Tier 1 corroboration is worth more than Tier 4.
TIER_WEIGHTS = {
    "tier_1_primary_research": 1.0,
    "tier_1_offensive_research": 1.0,
    "tier_1_government": 0.95,
    "tier_2_operator": 0.7,
    "tier_3_analysis": 0.5,
    "tier_4_news": 0.35,
    "tier_5_chatter": 0.15,
}

DEFAULT_AFFINITY_THRESHOLD = 0.28
MIN_GROUP_SIZE = 2
MAX_GROUPS = 12

# AI vendor names that should never anchor an affinity group on their own.
# These get over-tagged because they appear in roundups, methodology
# references, and meta-discussion. Require an additional strong signal.
AMBIGUOUS_ANCHORS = {
    "Anthropic/Claude",
    "OpenAI/ChatGPT",
    "Google/Gemini",
    "Microsoft/Copilot",
    "GitHub",     # often mentioned as hosting infra, not as target
    "Azure",      # often mentioned as deployment substrate
}


def _strong_signal_set(taxonomy):
    """Return the union of strong-signal values from one cluster's taxonomy."""
    signals = set()
    for axis in STRONG_SIGNAL_AXES:
        signals.update(taxonomy.get(axis, []))
    # Remove ambiguous-only matches: if the only signal is an ambiguous
    # anchor, treat as no strong signal.
    if signals and signals.issubset(AMBIGUOUS_ANCHORS):
        return set()
    return signals


def _representative_taxonomy(cluster):
    """Use the rep's taxonomy as the canonical fingerprint.

    Selectively union strong signals from corroborating members that share
    at least one strong signal with the rep. This prevents drift while
    still capturing additional CVEs/actors named by corroboration.
    """
    rep = cluster.get("primary") or cluster.get("rep") or {}
    rep_tax = dict(rep.get("taxonomy") or {})
    rep_strong = _strong_signal_set(rep_tax)

    if not rep_strong:
        # Rep has no strong signal — return rep tax as-is, no union.
        return rep_tax

    # Find corroborating members that share at least one strong signal
    members = cluster.get("corroborating_sources") or cluster.get("members") or []
    extra_cves = set(rep_tax.get("cve_ids", []))
    extra_actors = set(rep_tax.get("actor_attribution", []))
    extra_products = set(rep_tax.get("affected_products", []))
    for m in members:
        m_tax = m.get("taxonomy") or {}
        m_strong = _strong_signal_set(m_tax)
        if m_strong & rep_strong:
            # This member is genuinely the same story — pull strong signals
            extra_cves.update(m_tax.get("cve_ids", []))
            extra_actors.update(m_tax.get("actor_attribution", []))
            extra_products.update(m_tax.get("affected_products", []))

    if extra_cves:
        rep_tax["cve_ids"] = sorted(extra_cves)
    if extra_actors:
        rep_tax["actor_attribution"] = sorted(extra_actors)
    if extra_products:
        rep_tax["affected_products"] = sorted(extra_products)
    return rep_tax


def weighted_jaccard(tax_a, tax_b):
    """Weighted Jaccard, biased toward strong-signal axes."""
    score = 0.0
    weight_norm = 0.0
    for axis, weight in FEATURE_WEIGHTS.items():
        a = set(tax_a.get(axis, []))
        b = set(tax_b.get(axis, []))
        union = a | b
        if not union:
            continue
        intersection = a & b
        score += (len(intersection) / len(union)) * weight
        weight_norm += weight
    return score / weight_norm if weight_norm else 0.0


def find_affinity_groups(
    clusters,
    threshold=DEFAULT_AFFINITY_THRESHOLD,
    min_size=MIN_GROUP_SIZE,
    max_groups=MAX_GROUPS,
):
    if not clusters:
        return []

    # 1. Build representative taxonomies and strong-signal sets per cluster.
    taxonomies = [_representative_taxonomy(c) for c in clusters]
    strong_sets = [_strong_signal_set(t) for t in taxonomies]

    # 2. Edges: must share a strong signal AND meet similarity threshold.
    n = len(clusters)
    edges = []
    for i, j in combinations(range(n), 2):
        if not (strong_sets[i] and strong_sets[j]):
            continue
        if not (strong_sets[i] & strong_sets[j]):
            continue  # no shared strong signal, never merge
        sim = weighted_jaccard(taxonomies[i], taxonomies[j])
        if sim >= threshold:
            edges.append((i, j, sim))

    # 3. Union-find for connected components.
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    edges.sort(key=lambda e: -e[2])
    edge_scores = {(i, j): s for i, j, s in edges}
    for i, j, _ in edges:
        union(i, j)

    components = defaultdict(list)
    for i in range(n):
        components[find(i)].append(i)

    # 4. Build groups for components above min_size.
    groups = []
    for root, indices in components.items():
        if len(indices) < min_size:
            continue

        # Cohesion: mean edge weight within component, weighted by tier.
        scores = []
        tier_weight_sum = 0.0
        tier_weight_count = 0
        for i, j in combinations(indices, 2):
            key = (min(i, j), max(i, j))
            if key in edge_scores:
                ti = taxonomies[i].get("confidence_tier", "tier_4_news")
                tj = taxonomies[j].get("confidence_tier", "tier_4_news")
                tw = (TIER_WEIGHTS.get(ti, 0.3) + TIER_WEIGHTS.get(tj, 0.3)) / 2
                scores.append(edge_scores[key] * tw)
                tier_weight_sum += tw
                tier_weight_count += 1
        cohesion = (
            sum(scores) / tier_weight_sum if tier_weight_sum else 0.0
        )

        member_taxonomies = [taxonomies[i] for i in indices]
        dominant = _dominant_features(member_taxonomies)
        label = _label_from_dominant(dominant, member_taxonomies)
        if label is None:
            continue  # rejected as too generic

        total_priority = sum(clusters[i].get("priority_score", clusters[i].get("score", 0)) for i in indices)
        total_articles = sum(
            clusters[i].get("member_count", len(clusters[i].get("members", []))) for i in indices
        )

        # Pick the best (highest-tier) cluster as the group anchor
        anchor_idx = max(
            indices,
            key=lambda k: TIER_WEIGHTS.get(taxonomies[k].get("confidence_tier", "tier_4_news"), 0)
                          + 0.001 * clusters[k].get("priority_score", clusters[k].get("score", 0)),
        )

        groups.append({
            "label": label,
            "dominant_features": dominant,
            "cluster_count": len(indices),
            "article_count": total_articles,
            "cohesion": round(cohesion, 3),
            "total_priority": total_priority,
            "anchor_cluster_index": anchor_idx,
            "cluster_indices": indices,
            "shared_strong_signals": sorted(
                set.intersection(*(strong_sets[i] for i in indices))
                if all(strong_sets[i] for i in indices) else set()
            ),
        })

    groups.sort(
        key=lambda g: g["total_priority"] * g["cluster_count"] * (0.5 + g["cohesion"]),
        reverse=True,
    )
    return groups[:max_groups]


def _dominant_features(taxonomies):
    counters = defaultdict(Counter)
    for tax in taxonomies:
        for axis, values in tax.items():
            if isinstance(values, list):
                counters[axis].update(values)

    dominant = {}
    n = len(taxonomies)
    for axis, ctr in counters.items():
        threshold_count = max(2, int(0.5 * n))  # require majority, not 40%
        top = [v for v, c in ctr.most_common(5) if c >= threshold_count]
        if top:
            dominant[axis] = top
    return dominant


def _label_from_dominant(dominant, taxonomies):
    """Build a label. Reject if it would be generic or anchor-ambiguous."""
    actors = [a for a in dominant.get("actor_attribution", []) if not a.startswith("UNC") and not a.startswith("APT")]
    if not actors:
        actors = dominant.get("actor_attribution", [])
    products = [p for p in dominant.get("affected_products", []) if p not in AMBIGUOUS_ANCHORS]
    categories = dominant.get("threat_categories", [])
    cves = dominant.get("cve_ids", [])
    urgency = dominant.get("urgency_signals", [])

    # Anchor on CVE if multiple stories share a specific CVE
    if cves and len(cves) == 1:
        if products:
            return f"{cves[0]} exploitation ({products[0]})"
        return f"{cves[0]} exploitation activity"

    if actors and products:
        return f"{actors[0]} targeting {products[0]}"

    if actors and categories:
        cat = categories[0].replace("_", " ")
        return f"{actors[0]}: {cat}"

    if actors:
        return f"{actors[0]} campaign activity"

    if products and "active_exploitation" in urgency:
        return f"{products[0]} active exploitation"

    if categories and products:
        cat = categories[0].replace("_", " ")
        return f"{cat} targeting {products[0]}"

    # Reject everything below this — too generic to be useful.
    return None
