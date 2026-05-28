"""
Scoring v2 for CTI items and clusters.

Replaces the score_item() and cluster-score-boost logic in aggregate.py.

Design goals:

  1. CONFIDENCE TIER IS MULTIPLICATIVE, NOT ADDITIVE
     v1 added a small constant per cohort (10 for Tier 1, 4 for Tier 4).
     Keyword hits then floated Tier 4 above Tier 1 because press releases
     are denser in buzzwords. v2 multiplies the keyword signal by the
     confidence tier, so vendor noise can't out-score primary research.

  2. CONTENT-TYPE FLOOR
     If the article is classified as `vendor_announcement` or
     `event_promotion`, the score is hard-capped at 4. These never belong
     in the top 10 regardless of their length.

  3. ATOMIC-INDICATOR BOOST
     Articles that contain MITRE T-IDs, KQL/Sigma/YARA keywords, file
     paths, command-line snippets, or specific IOCs get a substantive
     boost. These are the articles defenders can actually act on.

  4. CORROBORATION-WEIGHTED CLUSTER BOOST
     v1 added +2 per corroborating source. v2 weights the boost by the
     diversity of cohorts represented (a Tier 1 + Tier 4 + Reddit story
     is stronger than three Tier 4 stories).

  5. RECENCY IS GENTLE
     v1 added up to +4 for recency. That's enough to lift Tier 4 over
     Tier 1 just by being fresh. v2 caps recency at +2 and only applies
     it within Tier-similar comparisons.
"""

import re
from datetime import datetime, timezone


CONFIDENCE_TIER_MULTIPLIER = {
    "tier_1_primary_research": 1.4,
    "tier_1_offensive_research": 1.4,
    "tier_1_government": 1.3,
    "tier_2_operator": 1.1,
    "tier_3_analysis": 0.9,
    "tier_4_news": 0.7,
    "tier_5_chatter": 0.4,
}

# Base cohort score floors (independent of content)
COHORT_BASE = {
    "threat_research_primary": 10,
    "offensive_vulnerability_research": 10,
    "government_authoritative": 9,
    "detection_response_operations": 8,
    "cloud_identity_infrastructure": 7,
    "ai_security_agentic_risk": 6,
    "ransomware_ecrime_financial_crime": 7,
    "policy_strategy_geopolitics": 5,
    "practitioner_analysis": 5,
    "cyber_news_breach_reporting": 4,
    "reddit_practitioner_osint": 2,
}

# Urgency / exploitation signals (matched against title+summary+body head)
URGENCY_SIGNALS = {
    r"\bactively\s+exploited\b": 10,
    r"\bin[-\s]the[-\s]wild\b": 7,
    r"\bzero[-\s]?day\b": 6,
    r"\bunauthenticated\s+RCE\b|\bpre[-\s]?auth\s+RCE\b": 9,
    r"\bremote\s+code\s+execution\b|\bRCE\b": 5,
    r"\bauth\s+bypass\b|\bauthentication\s+bypass\b": 6,
    r"\bemergency\s+patch\b|\bout[-\s]of[-\s]band\b": 7,
    r"\bno\s+patch\b|\bunpatched\b|\bnot\s+fixed\b": 6,
    r"\bCVSS\s*[:\s]?\s*(?:9\.\d|10(?:\.0)?)\b": 5,
    r"\bsupply[-\s]chain\b": 5,
    r"\bnation[-\s]state\b|\bstate[-\s]sponsored\b|\bAPT\d+\b": 4,
    r"\bproof[-\s]of[-\s]concept\s+exploit\b|\bPoC\s+(?:released|published|available)\b": 5,
}

# Indicator-density signals: rewards content with actionable IOCs and
# detection content.
INDICATOR_SIGNALS = {
    r"\bT\d{4}(?:\.\d{3})?\b": 2,                  # MITRE T-IDs
    r"\bKQL\b|let\s+\w+\s*=\s*\w+": 3,              # KQL queries
    r"\bSigma\s+rule\b|detection:\s*\n": 3,         # Sigma rules
    r"\bYARA\b|rule\s+\w+\s*\{": 3,                 # YARA rules
    r"\bsha(?:1|256)\s*[:=]\s*[a-f0-9]{32,}": 2,    # hashes
    r"\b[\\/](?:Users|home|tmp|var|etc)[\\/]\w+": 2, # filesystem paths
    r"\bC:\\\\Windows\\\\|\bHKLM\\\\|\bHKCU\\\\": 2, # Windows artifacts
    r"\bcurl\s+-\w+\s+http|\bpowershell\s+-": 2,     # command-line snippets
    r"\bregsvr32\b|\brundll32\b|\bwmic\b|\bcertutil\b": 2,  # LOLBins
}

# Marketing / event noise — strong negatives
NOISE_PATTERNS = {
    r"\b(?:unveils|introduces|launches|announces)\s+(?:its\s+|the\s+|new\s+)?": -8,
    r"\bnow\s+available\b": -4,
    r"\bgeneral\s+availability\b|\bGA\s+release\b": -5,
    r"\bgartner\s+(?:magic\s+quadrant|peer\s+insights)\b": -6,
    r"\bnamed\s+a\s+leader\b": -5,
    r"\bappoint\w+\s+\w+\s+as\b": -5,
    r"\bwebinar\b|\bregister\s+now\b": -6,
    r"\bjoin\s+us\s+at\b": -5,
    r"\bsponsored\s+by\b|\bbrought\s+to\s+you\s+by\b": -4,
}

# Content type floors / caps
CONTENT_TYPE_CAP = {
    "vendor_announcement": 4,
    "event_promotion": 3,
}

CONTENT_TYPE_BOOST = {
    "threat_research": 6,
    "vulnerability_disclosure": 4,
    "incident_report": 4,
    "intel_roundup": 1,
}


def score_item(item):
    """Compute v2 priority score for an item.

    Args:
      item: dict with keys title, summary, source, cohort, published_dt,
            taxonomy (output of taxonomy.extract_taxonomy).
    Returns:
      int score.
    """
    tax = item.get("taxonomy") or {}
    tier = tax.get("confidence_tier", "tier_4_news")
    tier_mult = CONFIDENCE_TIER_MULTIPLIER.get(tier, 0.7)
    content_type = tax.get("content_type", "news_report")

    # Hard cap for marketing
    if content_type in CONTENT_TYPE_CAP:
        return CONTENT_TYPE_CAP[content_type]

    # Base from cohort
    score = COHORT_BASE.get(item.get("cohort"), 3)

    haystack = " ".join(filter(None, [
        item.get("title", ""),
        item.get("summary", ""),
        (item.get("full_body") or "")[:2000],
    ])).lower()

    # Urgency signals — multiplied by tier
    urgency_raw = 0
    for pattern, weight in URGENCY_SIGNALS.items():
        if re.search(pattern, haystack, re.IGNORECASE):
            urgency_raw += weight
    score += int(urgency_raw * tier_mult)

    # Indicator density — these are intrinsic to the article quality, no tier mult
    indicator_score = 0
    for pattern, weight in INDICATOR_SIGNALS.items():
        if re.search(pattern, haystack, re.IGNORECASE):
            indicator_score += weight
    score += min(indicator_score, 12)  # cap so a code-heavy article doesn't dominate

    # Specific tag boosts (also tier-multiplied)
    tag_score = 0
    if tax.get("cve_ids"):
        tag_score += 4
    if tax.get("actor_attribution"):
        tag_score += 3
    if "actively_exploited" in tax.get("urgency_signals", []):
        tag_score += 6
    if "no_patch_yet" in tax.get("urgency_signals", []):
        tag_score += 4
    if "preauth_unauth" in tax.get("urgency_signals", []):
        tag_score += 3
    score += int(tag_score * tier_mult)

    # Content type boosts
    score += CONTENT_TYPE_BOOST.get(content_type, 0)

    # Noise penalties (not tier-multiplied — vendor noise from Tier 1 is
    # still vendor noise)
    for pattern, weight in NOISE_PATTERNS.items():
        if re.search(pattern, haystack, re.IGNORECASE):
            score += weight

    # Gentle recency bonus
    pub_dt = item.get("published_dt")
    if pub_dt:
        age_h = (datetime.now(timezone.utc) - pub_dt).total_seconds() / 3600
        if age_h < 12:
            score += 2
        elif age_h < 24:
            score += 1

    return max(0, score)


def cluster_corroboration_boost(members):
    """Boost a cluster score by the diversity of cohorts corroborating it.

    Three Tier-4 news rewrites of the same press release shouldn't boost the
    same as a Tier-1 advisory + a Tier-2 operator writeup + a Tier-4 news.
    """
    cohorts = set(m.get("cohort") for m in members)
    n_cohorts = len(cohorts)
    if n_cohorts <= 1:
        return 0

    # Reward cross-tier presence
    tiers_present = set()
    for m in members:
        tax = m.get("taxonomy") or {}
        tiers_present.add(tax.get("confidence_tier", "tier_4_news"))

    tier1_present = any(t.startswith("tier_1") for t in tiers_present)
    tier2_present = "tier_2_operator" in tiers_present
    tier4_present = "tier_4_news" in tiers_present

    boost = 0
    if tier1_present and (tier2_present or tier4_present):
        boost += 6  # Tier 1 + corroboration is gold
    elif n_cohorts >= 3:
        boost += 4
    elif n_cohorts == 2:
        boost += 2

    return boost
