"""
Affinity grouping for CTI clusters.

Different from clustering. Clustering says "these articles are the same story."
Affinity grouping says "these stories belong to the same theme."

Example:
  Cluster A: ShinyHunters posts Canvas LMS data (5 articles)
  Cluster B: ShinyHunters claims Zendesk-adjacent breach (3 articles)
  Cluster C: Snowflake-tenant breach via OAuth abuse (4 articles)
  -> Affinity group: "ShinyHunters SaaS data theft wave"
     because actor=ShinyHunters appears in A+B and threat_category=data_breach
     appears in all three, with overlapping affected_industries.

Algorithm:
  1. Build a feature vector per cluster from its taxonomy.
  2. Compute pairwise similarity using weighted Jaccard over feature buckets.
     Strong-signal buckets (actor, CVE, product) weight more than weak ones
     (industry, geography).
  3. Greedy agglomeration: start with each cluster as its own group, merge
     pairs above threshold, repeat until stable.
  4. Filter groups smaller than min_size; name remaining groups by their
     dominant features.

This is intentionally simple. A graph-community algorithm would be more
elegant but overkill for the data volume and harder to debug.
"""

from collections import Counter, defaultdict
from itertools import combinations


# Weight of each taxonomy axis when computing similarity.
# Strong, specific signals dominate; broad context signals fill in.
FEATURE_WEIGHTS = {
    "cve_ids": 4.0,              # Same CVE = very strong affinity signal
    "actor_attribution": 3.5,    # Same actor = strong
    "affected_products": 3.0,    # Same product = strong
    "threat_categories": 2.0,    # Same category = medium
    "attack_techniques": 2.0,    # Same MITRE technique = medium
    "affected_industries": 1.5,  # Same industry = weak-medium
    "urgency_signals": 1.0,      # Same urgency type = weak
    "geographic_scope": 0.5,     # Same geography = weak
}

# Default affinity threshold. Higher = stricter grouping, smaller groups.
# 0.25 is a reasonable floor; 0.4+ is conservative; 0.15 is aggressive.
DEFAULT_AFFINITY_THRESHOLD = 0.25

# Minimum cluster count for an affinity group to surface in the output.
MIN_GROUP_SIZE = 2

# Maximum number of affinity groups to publish.
MAX_GROUPS = 12

# A cluster needs at least this many populated taxonomy axes (excluding
# always-present content_type and confidence_tier) to be eligible for
# grouping. Prevents thinly-tagged clusters from collapsing into noise.
MIN_POPULATED_AXES = 2

# Axes that count toward MIN_POPULATED_AXES — the "real" content axes.
GROUPING_AXES = (
    "cve_ids", "actor_attribution", "affected_products",
    "threat_categories", "attack_techniques", "affected_industries",
)


def _feature_set(cluster_taxonomy, axis):
    """Return a set of tagged values for one taxonomy axis on a cluster."""
    return set(cluster_taxonomy.get(axis, []))


def weighted_jaccard(tax_a, tax_b):
    """
    Compute weighted Jaccard similarity between two cluster taxonomies.

    For each axis, |intersection| / |union| weighted by FEATURE_WEIGHTS,
    then normalized by total possible weight contributed by axes where
    either side had data.
    """
    score = 0.0
    weight_norm = 0.0

    for axis, weight in FEATURE_WEIGHTS.items():
        a = _feature_set(tax_a, axis)
        b = _feature_set(tax_b, axis)
        union = a | b
        if not union:
            continue  # axis is empty on both sides, doesn't contribute either way
        intersection = a & b
        axis_score = len(intersection) / len(union)
        score += axis_score * weight
        weight_norm += weight

    if weight_norm == 0:
        return 0.0
    return score / weight_norm


def _cluster_taxonomy(cluster):
    """
    Aggregate taxonomy across all members of a cluster.
    Returns a single taxonomy dict with union of tags from every member.
    """
    aggregated = defaultdict(set)
    for member in cluster["members"]:
        tax = member.get("taxonomy") or {}
        for axis, values in tax.items():
            if isinstance(values, list):
                aggregated[axis].update(values)
            elif isinstance(values, str):
                aggregated[axis].add(values)
    return {k: sorted(v) for k, v in aggregated.items()}


def find_affinity_groups(
    clusters,
    threshold=DEFAULT_AFFINITY_THRESHOLD,
    min_size=MIN_GROUP_SIZE,
    max_groups=MAX_GROUPS,
):
    """
    Find affinity groups across clusters.

    Args:
        clusters: list of cluster dicts (each with 'members' and per-member 'taxonomy')
        threshold: minimum pairwise affinity to merge clusters into a group
        min_size: minimum number of clusters to surface a group
        max_groups: cap on number of groups returned

    Returns:
        List of affinity group dicts, sorted by importance (size * mean score).
    """
    if not clusters:
        return []

    # 1. Compute aggregate taxonomy per cluster.
    taxonomies = [_cluster_taxonomy(c) for c in clusters]

    # 2. Mark clusters as eligible for grouping. A cluster needs at least
    #    MIN_POPULATED_AXES content axes populated. Thinly-tagged clusters
    #    are still kept in the output as standalone, but won't be merged.
    def _is_eligible(tax):
        populated = sum(1 for axis in GROUPING_AXES if tax.get(axis))
        return populated >= MIN_POPULATED_AXES

    eligible = [_is_eligible(t) for t in taxonomies]

    # 3. Build pairwise similarity edges above threshold, eligible-only.
    n = len(clusters)
    edges = []
    for i, j in combinations(range(n), 2):
        if not (eligible[i] and eligible[j]):
            continue
        s = weighted_jaccard(taxonomies[i], taxonomies[j])
        if s >= threshold:
            edges.append((i, j, s))

    # 4. Union-find for connected components above threshold.
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
    edge_scores_by_pair = {(i, j): s for i, j, s in edges}
    for i, j, _ in edges:
        union(i, j)

    # 5. Collect components.
    components = defaultdict(list)
    for i in range(n):
        components[find(i)].append(i)

    # 6. Build affinity group descriptors for components above min_size.
    groups = []
    for root, indices in components.items():
        if len(indices) < min_size:
            continue

        scores = []
        for i, j in combinations(indices, 2):
            key = (min(i, j), max(i, j))
            if key in edge_scores_by_pair:
                scores.append(edge_scores_by_pair[key])
        cohesion = sum(scores) / len(scores) if scores else 0.0

        member_taxonomies = [taxonomies[i] for i in indices]
        dominant = _dominant_features(member_taxonomies)
        label = _label_from_dominant(dominant)

        # Reject groups that degenerate to a generic label — these are
        # spurious matches on weak signals.
        if label == "uncategorized theme":
            continue

        total_priority = sum(clusters[i].get("score", 0) for i in indices)
        total_articles = sum(len(clusters[i]["members"]) for i in indices)

        groups.append({
            "label": label,
            "dominant_features": dominant,
            "cluster_count": len(indices),
            "article_count": total_articles,
            "cohesion": round(cohesion, 3),
            "total_priority": total_priority,
            "cluster_indices": indices,
        })

    # 7. Rank by combined importance.
    groups.sort(
        key=lambda g: g["total_priority"] * g["cluster_count"] * (0.5 + g["cohesion"]),
        reverse=True,
    )

    return groups[:max_groups]


def _dominant_features(taxonomies):
    """
    For a set of cluster taxonomies, find the most common values per axis.
    Returns dict {axis: [top_values]}.
    """
    counters = defaultdict(Counter)
    for tax in taxonomies:
        for axis, values in tax.items():
            if isinstance(values, list):
                counters[axis].update(values)

    dominant = {}
    n = len(taxonomies)
    for axis, ctr in counters.items():
        # Surface values appearing in at least 40% of the constituent clusters.
        threshold_count = max(2, int(0.4 * n))
        top = [v for v, c in ctr.most_common(5) if c >= threshold_count]
        if top:
            dominant[axis] = top

    return dominant


def _label_from_dominant(dominant):
    """
    Build a human-readable label from dominant features.
    Prefers actor + product, then actor + category, then category + product.
    """
    actors = dominant.get("actor_attribution", [])
    products = dominant.get("affected_products", [])
    categories = dominant.get("threat_categories", [])
    industries = dominant.get("affected_industries", [])

    # Best: actor + product (e.g., "ShinyHunters / Canvas LMS")
    if actors and products:
        return f"{actors[0]} targeting {products[0]}"

    # Next: actor + category (e.g., "Scattered Spider data breaches")
    if actors and categories:
        cat = categories[0].replace("_", " ")
        return f"{actors[0]} {cat} activity"

    # Next: actor alone if specific
    if actors:
        return f"{actors[0]} campaign activity"

    # Next: category + product (e.g., "ransomware targeting VMware ESXi")
    if categories and products:
        cat = categories[0].replace("_", " ")
        return f"{cat} targeting {products[0]}"

    # Next: category + industry
    if categories and industries:
        cat = categories[0].replace("_", " ")
        ind = industries[0].replace("_", " ")
        return f"{cat} affecting {ind}"

    # Fallback: category alone
    if categories:
        cat = categories[0].replace("_", " ")
        return f"{cat} activity"

    return "uncategorized theme"
