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
    n = len(clusters)

    # 2. Signal-bucket grouping. For each non-ambiguous strong signal
    # (real CVE, real actor, non-generic target product) that appears in
    # ≥ min_size clusters, that signal IS a theme.
    #
    # This replaces v1's connected-components / union-find approach, which
    # had a transitive-merge bug: A shares Gogs with B, B shares
    # ShinyHunters with C, so A-B-C end up in one giant component with no
    # coherent dominant features. The signal-bucket approach yields one
    # Gogs theme and one ShinyHunters theme; a cluster involved in both
    # appears in both themes (correct — that *is* a coordinated campaign).
    #
    # After bucketing we de-duplicate: a theme whose cluster set is a
    # strict subset of another theme's cluster set is dropped (the
    # superset theme already represents it).
    signal_to_clusters = defaultdict(set)
    for i, ss in enumerate(strong_sets):
        for signal in ss:
            if signal in AMBIGUOUS_ANCHORS:
                continue
            signal_to_clusters[signal].add(i)

    raw_themes = []  # list of (signal, frozenset_of_cluster_indices)
    for signal, indices in signal_to_clusters.items():
        if len(indices) >= min_size:
            raw_themes.append((signal, frozenset(indices)))

    # Drop themes whose cluster set is a strict subset of another theme's
    # set. Tie-break: keep the theme whose signal is more specific
    # (CVE > Actor > Product). Without this, we'd surface both
    # "ShinyHunters" (5 clusters) and "ShinyHunters+Salesforce" (4 clusters)
    # as separate themes when the second is just a slice of the first.
    def _specificity(signal):
        if signal.startswith("CVE-"):
            return 3
        # Known actor names (best heuristic: not a product label)
        # — fall back to product = lowest specificity
        return 1 if signal in {"Anthropic/Claude", "OpenAI/ChatGPT", "GitHub", "Azure"} else 2

    raw_themes.sort(key=lambda t: (-len(t[1]), -_specificity(t[0])))
    kept_themes = []
    for signal, indices in raw_themes:
        is_subset = any(
            indices < kept_indices  # strict subset
            for _, kept_indices in kept_themes
        )
        if not is_subset:
            kept_themes.append((signal, indices))

    # Build the affinity-group descriptors for kept themes.
    edges_seen = {}  # (i, j) -> max jaccard observed (for cohesion)
    for i, j in combinations(range(n), 2):
        if not (strong_sets[i] and strong_sets[j]):
            continue
        if not (strong_sets[i] & strong_sets[j]):
            continue
        edges_seen[(i, j)] = weighted_jaccard(taxonomies[i], taxonomies[j])

    # 3. Build groups from kept_themes.
    groups = []
    for anchor_signal, indices_fs in kept_themes:
        indices = sorted(indices_fs)

        # Cohesion: mean weighted-jaccard among pairs in this theme, scaled
        # by tier weights so Tier 1 + Tier 4 corroboration outranks five
        # Tier 4 news rewrites of the same story.
        scores = []
        tier_weight_sum = 0.0
        for i, j in combinations(indices, 2):
            key = (min(i, j), max(i, j))
            sim = edges_seen.get(key, 0.0)
            ti = taxonomies[i].get("confidence_tier", "tier_4_news")
            tj = taxonomies[j].get("confidence_tier", "tier_4_news")
            tw = (TIER_WEIGHTS.get(ti, 0.3) + TIER_WEIGHTS.get(tj, 0.3)) / 2
            scores.append(max(sim, 0.2) * tw)
            tier_weight_sum += tw
        cohesion = sum(scores) / tier_weight_sum if tier_weight_sum else 0.0

        member_taxonomies = [taxonomies[i] for i in indices]
        dominant = _dominant_features(member_taxonomies)

        # Label preference: build from the anchor signal directly so the
        # theme always carries the strong signal in its name. Fall back to
        # generic label generator if the anchor signal alone is uninformative.
        label = _label_from_anchor(anchor_signal, dominant, member_taxonomies)
        if label is None:
            continue

        total_priority = sum(
            clusters[i].get("priority_score", clusters[i].get("score", 0))
            for i in indices
        )
        total_articles = sum(
            clusters[i].get("member_count", len(clusters[i].get("members", [])))
            for i in indices
        )

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
            "anchor_signal": anchor_signal,
            "anchor_cluster_index": anchor_idx,
            "cluster_indices": indices,
            "shared_strong_signals": [anchor_signal],
        })

    groups.sort(
        key=lambda g: g["total_priority"] * g["cluster_count"] * (0.5 + g["cohesion"]),
        reverse=True,
    )

    # 4. Rollup pass for elegance. When a CVE theme's clusters all belong
    # to a product theme on the same disclosure (e.g., three BitLocker CVEs
    # disclosed together, each producing its own CVE theme, plus the parent
    # "Microsoft BitLocker active exploitation" theme), collapse the CVE
    # themes into the product theme as `member_cves` metadata. The result:
    # one theme per real story, with the constituent CVEs surfaced as
    # detail rather than parallel themes.
    groups = _rollup_cve_themes_into_products(groups, taxonomies)

    # 5. Actor↔Product co-fold. When an actor theme and a product theme
    # cover overlapping cluster sets (the same campaign seen from two
    # angles — e.g., "ShinyHunters" and "Salesforce as ransomware target"),
    # the actor theme is the more specific framing. Fold the product theme
    # into the actor theme as `also_targets` metadata.
    groups = _rollup_product_into_actor(groups, taxonomies)

    return groups[:max_groups]


def _rollup_product_into_actor(groups, taxonomies):
    """When an actor theme and a product theme heavily overlap, the actor
    theme wins and the product becomes a 'also_targets' note on the actor.

    Heuristic: if actor theme A and product theme P share ≥60% of P's
    clusters AND P's anchor product appears as a dominant product in A,
    fold P into A.
    """
    absorbed = set()

    actor_groups = [
        g for g in groups
        if not g["anchor_signal"].startswith("CVE-")
        and any(tok in g["anchor_signal"] for tok in KNOWN_ACTOR_TOKENS)
    ]
    product_groups = [
        g for g in groups
        if not g["anchor_signal"].startswith("CVE-")
        and not any(tok in g["anchor_signal"] for tok in KNOWN_ACTOR_TOKENS)
    ]

    for prod_g in product_groups:
        prod_indices = set(prod_g["cluster_indices"])
        if not prod_indices:
            continue

        for actor_g in actor_groups:
            if id(actor_g) in absorbed:
                continue
            actor_indices = set(actor_g["cluster_indices"])
            actor_dominant_products = actor_g.get("dominant_features", {}).get("affected_products", [])

            overlap = len(prod_indices & actor_indices) / len(prod_indices)

            if overlap >= 0.6 and prod_g["anchor_signal"] in actor_dominant_products:
                # Skip if the parent's label already names this product
                # (the product is the anchor of the actor theme's label).
                if prod_g["anchor_signal"] not in actor_g.get("label", ""):
                    actor_g.setdefault("also_targets", []).append(prod_g["anchor_signal"])
                # Union the cluster sets regardless — the campaign overlap is real
                merged = sorted(actor_indices | prod_indices)
                actor_g["cluster_indices"] = merged
                actor_g["cluster_count"] = len(merged)
                absorbed.add(id(prod_g))
                break

    return [g for g in groups if id(g) not in absorbed]


def _rollup_cve_themes_into_products(groups, taxonomies):
    """Fold per-CVE themes into their parent product theme.

    Heuristic (in priority order):
      1. STRICT FOLD: CVE theme's cluster set is a subset of a product
         theme's cluster set → fold (strongest signal).
      2. SOFT FOLD: CVE theme's dominant product matches a product theme's
         anchor AND ≥50% cluster overlap → fold (handles residual tagging
         noise where the same disclosure produced slightly different
         cluster sets per CVE).

    The folded theme's CVE is recorded on the parent as a `member_cves`
    entry. The standalone CVE theme is dropped from the output.
    """
    absorbed = set()

    for g in groups:
        if not g["anchor_signal"].startswith("CVE-"):
            continue
        if id(g) in absorbed:
            continue
        cve_indices = set(g["cluster_indices"])
        cve_dominant_products = [
            p for p in g.get("dominant_features", {}).get("affected_products", [])
            if p not in AMBIGUOUS_ANCHORS
        ]

        best_parent = None
        best_overlap = 0.0

        for parent in groups:
            if parent is g or id(parent) in absorbed:
                continue
            if parent["anchor_signal"].startswith("CVE-"):
                continue
            if parent["anchor_signal"] in AMBIGUOUS_ANCHORS:
                continue

            parent_indices = set(parent["cluster_indices"])
            if not parent_indices:
                continue

            overlap = len(cve_indices & parent_indices) / len(cve_indices)

            # Strict fold: CVE clusters fully contained in parent
            if cve_indices.issubset(parent_indices):
                best_parent = parent
                best_overlap = 1.0
                break

            # Soft fold: parent's anchor product is in this CVE theme's
            # dominant products AND substantial overlap
            if (parent["anchor_signal"] in cve_dominant_products
                    and overlap >= 0.5
                    and overlap > best_overlap):
                best_parent = parent
                best_overlap = overlap

        if best_parent is not None:
            best_parent.setdefault("member_cves", []).append(g["anchor_signal"])
            # Union the cluster sets — soft fold may bring in CVE-only clusters
            merged_indices = sorted(set(best_parent["cluster_indices"]) | cve_indices)
            best_parent["cluster_indices"] = merged_indices
            best_parent["cluster_count"] = len(merged_indices)
            absorbed.add(id(g))

    rolled = []
    for g in groups:
        if id(g) in absorbed:
            continue
        if g.get("member_cves"):
            cves = sorted(set(g["member_cves"]))
            if len(cves) == 1:
                g["label"] = f"{g['anchor_signal']} exploitation ({cves[0]})"
            else:
                g["label"] = f"{g['anchor_signal']} exploitation ({len(cves)} CVEs)"
        rolled.append(g)
    return rolled


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


# Known actor labels (used by _label_from_anchor to pick label phrasing).
# Anything else is treated as a product target for label purposes.
KNOWN_ACTOR_TOKENS = (
    "Scattered Spider", "ShinyHunters", "LockBit", "BlackCat", "ALPHV",
    "Cl0p", "Akira", "RansomHub", "Rhysida", "Play", "Black Basta",
    "Medusa", "Volt Typhoon", "Salt Typhoon", "Flax Typhoon",
    "Mustang Panda", "APT28", "APT29", "APT41", "Lazarus", "Kimsuky",
    "APT37", "APT38", "MuddyWater", "Nimbus Manticore", "Ghostwriter",
    "Cloud Atlas", "Handala", "NoName057", "Silent Ransom Group",
    "TeamPCP", "JINX-0164", "Lapsus$",
)


def _label_from_anchor(anchor_signal, dominant, taxonomies):
    """Build a theme label using the anchor signal that defines this theme.

    The anchor is the strong signal (CVE / actor / target product) that
    bucket-grouping selected this set of clusters on. Labels surface that
    signal first so a reader instantly sees which exact actor/CVE/product
    the theme is about.
    """
    # CVE anchor: "CVE-X exploitation [(Product)]"
    if anchor_signal.startswith("CVE-"):
        products = [p for p in dominant.get("affected_products", []) if p not in AMBIGUOUS_ANCHORS]
        if products:
            return f"{anchor_signal} exploitation ({products[0]})"
        return f"{anchor_signal} exploitation activity"

    # Actor anchor: "{Actor} [+ Product / category]"
    if any(actor_tok in anchor_signal for actor_tok in KNOWN_ACTOR_TOKENS):
        products = [p for p in dominant.get("affected_products", []) if p not in AMBIGUOUS_ANCHORS and p != anchor_signal]
        categories = dominant.get("threat_categories", [])
        if products:
            return f"{anchor_signal} targeting {products[0]}"
        if categories:
            cat = categories[0].replace("_", " ")
            return f"{anchor_signal}: {cat}"
        return f"{anchor_signal} campaign activity"

    # Product anchor: "{Product} {category-or-urgency}"
    urgency = dominant.get("urgency_signals", [])
    categories = dominant.get("threat_categories", [])
    if "active_exploitation" in urgency or "actively_exploited" in urgency:
        return f"{anchor_signal} active exploitation"
    if categories:
        cat = categories[0].replace("_", " ")
        return f"{cat} targeting {anchor_signal}"
    return f"{anchor_signal} vulnerability activity"
