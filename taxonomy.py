"""
Deterministic taxonomy enrichment for CTI items.

v2 rewrite. Fixes the contamination class of bugs in v1:

  1. PROXIMITY-ANCHORED EXTRACTION
     A product or actor tag now requires the term to appear within
     PROXIMITY_WINDOW tokens of a threat-language anchor (exploit, patch,
     vulnerability, attack, compromise, ...). This kills the "page nav
     mentions GitHub once" false positive without losing real signal.

  2. ROLE DISAMBIGUATION
     Each product tag is annotated with its inferred role:
       - target    : the thing being attacked
       - tool      : the thing being used to attack (e.g., "Claude wrote the exploit")
       - vendor    : the entity publishing the advisory
       - mention   : context only, no role inferred
     Affinity grouping should ignore non-target roles.

  3. HARD CAPS
     Max 3 products and max 5 CVEs per article. Beyond that the article is
     almost certainly a roundup or a polluted scrape, and using all of them
     to compute affinity will smear the cluster's identity.

  4. BODY-ONLY OPERATION
     The aggregator must pass clean body text (already stripped of nav/footer/
     aside/script). This module assumes that and never tries to compensate.
     If you start tagging from rendered HTML again, you'll get v1's behavior
     back.

  5. CONFIDENCE PER TAG
     Each tag carries a confidence score. Tags below MIN_CONFIDENCE are
     dropped from the canonical taxonomy and surfaced only in `weak_tags`
     for transparency and tuning.
"""

import re
from collections import defaultdict


# ---------------------------------------------------------------------------
# Anchors and lexicons
# ---------------------------------------------------------------------------

# A tag is only kept if its term appears within PROXIMITY_WINDOW characters
# of one of these anchor terms.
PROXIMITY_WINDOW = 180

# Anchors that indicate the surrounding text is about an attack, vulnerability,
# patch, or defensive operation. Tags within window of any of these are
# treated as "in-context" and earn confidence.
THREAT_ANCHORS = (
    r"vulnerab\w+", r"exploit\w*", r"attack\w*", r"compromis\w+",
    r"breach\w*", r"intrusion", r"malware", r"ransomware", r"backdoor",
    r"web\s?shell", r"infostealer", r"trojan", r"botnet", r"rootkit",
    r"phish\w+", r"smish\w+", r"vish\w+",
    r"zero[-\s]?day", r"n[-\s]?day",
    r"patch\w*", r"hotfix", r"advisor\w+", r"disclos\w+",
    r"CVE-\d{4}-\d{4,7}", r"CVSS",
    r"actively\s+exploited", r"in\s+the\s+wild",
    r"RCE", r"LPE", r"SSRF", r"XXE", r"deserialization", r"injection",
    r"path\s+traversal", r"auth(?:entication)?\s+bypass", r"privilege\s+escalation",
    r"hijack\w*", r"takeover", r"impersonat\w+",
    r"C2", r"command[-\s]and[-\s]control",
    r"IoC", r"indicator", r"detection", r"hunting", r"telemetry",
)

# Anchors that indicate a vendor/product is being discussed as a *tool* used
# by attackers (or, importantly, by researchers acting on attackers' behalf).
# A product tag near these and FAR FROM target-anchors gets role=tool.
TOOL_ANCHORS = (
    r"used\s+to\s+(?:generate|write|create|build|produce|craft)",
    r"asked\s+\w+\s+to\b",
    r"AI[-\s]assisted", r"AI[-\s]generated", r"AI[-\s]built", r"AI[-\s]powered\s+(?:exploit|malware|phishing)",
    r"jailbroken", r"jailbreak", r"agentic\s+(?:exploit|attack)",
    r"prompted\s+\w+\s+to", r"abuse[ds]?\s+\w+\s+to",
)

# Anchors that indicate the surrounding entity is the vendor publishing
# advisory or research, not the target.
VENDOR_ANCHORS = (
    r"\b(?:wrote|posted|published|reported|disclosed|disclosed)\s+by\b",
    r"\bsaid\s+(?:in\s+)?(?:a\s+)?(?:blog|post|advisory|statement|bulletin)\b",
    r"according\s+to\s+\w+\s+research\w*",
    r"researchers?\s+at\b",
)

# Product names → canonical labels. Order matters: longest match wins.
# Keep this list tight and curated. Catch-all regexes are worse than
# missing tags.
PRODUCTS = [
    # AI platforms
    (r"\bAnthropic\b|\bClaude\s+(?:Code|Desktop|Sonnet|Opus|Haiku|Mythos)?", "Anthropic/Claude"),
    (r"\bOpenAI\b|\bChatGPT\b|\bGPT-?\d", "OpenAI/ChatGPT"),
    (r"\bGoogle\s+Gemini\b|\bGemini\s+(?:Pro|Flash|Code)?", "Google/Gemini"),
    (r"\bMicrosoft\s+Copilot\b|\bCopilot\s+(?:Cowork|Studio|Pro|for)\b|\bM365\s+Copilot\b", "Microsoft/Copilot"),
    (r"\bCursor\b(?=\s+(?:IDE|editor|code|agent))", "Cursor"),
    # Source control / dev tooling
    (r"\bGitHub\s+(?:Actions|Enterprise|Codespaces|Copilot)\b|\bGitHub\b(?!\.com/)", "GitHub"),
    (r"\bGitLab\b", "GitLab"),
    (r"\bGitea\b", "Gitea"),
    (r"\bGogs\b", "Gogs"),
    (r"\bnpm\b|\bNode\s+Package\s+Manager\b", "npm"),
    (r"\bPyPI\b", "PyPI"),
    (r"\bcrates\.io\b|\bCargo\b(?=\s+(?:registry|package))", "crates.io"),
    (r"\bPackagist\b", "Packagist"),
    # Cloud / identity / SaaS
    (r"\bMicrosoft\s+Entra(?:\s+ID)?\b|\bEntra\s+ID\b|\bAzure\s+AD\b", "Microsoft Entra"),
    (r"\bOkta\b", "Okta"),
    (r"\bSalesforce\b", "Salesforce"),
    (r"\bSnowflake\b", "Snowflake"),
    (r"\bAWS\b|\bAmazon\s+Web\s+Services\b", "AWS"),
    (r"\bAzure\b(?!\s+AD)", "Azure"),
    (r"\bGoogle\s+Cloud\s+Platform\b|\bGCP\b|\bGoogle\s+Cloud\b", "Google Cloud"),
    (r"\bSharePoint\b", "Microsoft SharePoint"),
    (r"\bMicrosoft\s+365\b|\bO365\b|\bOffice\s+365\b", "Microsoft 365"),
    (r"\bGoogle\s+Workspace\b", "Google Workspace"),
    # Edge / network appliances
    (r"\bFortinet\b|\bFortiGate\b|\bFortiOS\b|\bFortiClient\s+EMS\b", "Fortinet"),
    (r"\bIvanti\b|\bConnect\s+Secure\b|\bPolicy\s+Secure\b", "Ivanti"),
    (r"\bPalo\s+Alto\s+Networks?\b|\bPAN-OS\b|\bGlobalProtect\b", "Palo Alto Networks"),
    (r"\bCisco\b(?=\s+(?:ASA|FTD|IOS|SD-WAN|Secure|vManage|Webex|Talos))", "Cisco"),
    (r"\bF5\s+(?:BIG-IP|Networks)\b", "F5 BIG-IP"),
    (r"\bSonicWall\b", "SonicWall"),
    (r"\bCitrix\b(?=\s+(?:ADC|Gateway|NetScaler))", "Citrix"),
    # Endpoint / OS
    (r"\bMicrosoft\s+Defender\b|\bDefender\s+(?:XDR|for\s+Endpoint|ATP)\b", "Microsoft Defender"),
    (r"\bBitLocker\b", "Microsoft BitLocker"),
    (r"\bWindows\s+(?:11|10|Server|Cloud\s+Filter)\b|\bWindows\b(?=\s+(?:kernel|driver))", "Microsoft Windows"),
    (r"\bmacOS\b|\bApple\s+(?:iOS|macOS)\b", "Apple iOS/macOS"),
    (r"\bAndroid\b(?=\s+(?:OS|kernel|device|app|malware))", "Android"),
    (r"\bLinux\s+kernel\b", "Linux kernel"),
    # Virtualization / containers
    (r"\bVMware\s+(?:ESXi|vCenter|Workstation)\b|\bvSphere\b", "VMware"),
    (r"\bDocker\b(?=\s+(?:image|container|registry|hub))", "Docker"),
    (r"\bKubernetes\b|\bk8s\b", "Kubernetes"),
    # Other
    (r"\bConfluence\b", "Atlassian Confluence"),
    (r"\bJira\b", "Atlassian Jira"),
    (r"\bDrupal\b", "Drupal"),
    (r"\bWordPress\b", "WordPress"),
    (r"\bScreenConnect\b|\bConnectWise\s+ScreenConnect\b", "ScreenConnect"),
    (r"\bSolarWinds\b", "SolarWinds"),
    (r"\bUbiquiti\b|\bUniFi\b|\bUDM\b|\bUDMP\b", "Ubiquiti UniFi"),
    (r"\bLiteSpeed\b", "LiteSpeed"),
    (r"\bcPanel\b", "cPanel"),
    (r"\bKnowledgeDeliver\b|\bDigital\s+Knowledge\b", "KnowledgeDeliver LMS"),
    (r"\bChromaDB\b", "ChromaDB"),
    (r"\bKopia\b", "Kopia"),
    (r"\bXWiki\b", "XWiki"),
]

# Known threat actors. Same rule: curated > regex catch-all.
ACTORS = [
    (r"\bScattered\s+Spider\b|\bMuddled\s+Libra\b|\bUNC3944\b", "Scattered Spider"),
    (r"\bShinyHunters?\b", "ShinyHunters"),
    (r"\bLockBit\b", "LockBit"),
    (r"\bBlackCat\b|\bALPHV\b", "BlackCat/ALPHV"),
    (r"\bCl0p\b|\bClop\b", "Cl0p"),
    (r"\bAkira\b(?=\s+ransomware)", "Akira"),
    (r"\bRansomHub\b", "RansomHub"),
    (r"\bRhysida\b", "Rhysida"),
    (r"\bPlay\b(?=\s+ransomware)", "Play"),
    (r"\bBlack\s+Basta\b", "Black Basta"),
    (r"\bMedusa\b(?=\s+(?:ransomware|gang|group))", "Medusa"),
    (r"\bVolt\s+Typhoon\b", "Volt Typhoon"),
    (r"\bSalt\s+Typhoon\b", "Salt Typhoon"),
    (r"\bFlax\s+Typhoon\b", "Flax Typhoon"),
    (r"\bMustang\s+Panda\b", "Mustang Panda"),
    (r"\bAPT\s?28\b|\bFancy\s+Bear\b", "APT28"),
    (r"\bAPT\s?29\b|\bCozy\s+Bear\b|\bMidnight\s+Blizzard\b", "APT29"),
    (r"\bAPT\s?41\b|\bWinnti\b", "APT41"),
    (r"\bLazarus\s+(?:Group)?\b", "Lazarus"),
    (r"\bKimsuky\b", "Kimsuky"),
    (r"\bAPT\s?37\b|\bReaperGroup\b", "APT37"),
    (r"\bAPT\s?38\b", "APT38"),
    (r"\bMuddyWater\b", "MuddyWater"),
    (r"\bNimbus\s+Manticore\b|\bScreening\s+Serpens\b|\bUNC1549\b", "Nimbus Manticore"),
    (r"\bGhostwriter\b|\bUAC-0057\b|\bUNC1151\b", "Ghostwriter"),
    (r"\bCloud\s+Atlas\b", "Cloud Atlas"),
    (r"\bHandala\s+Hack\s+Team\b|\bHandala\b", "Handala"),
    (r"\bNoName057\(?16\)?\b|\bNoName057\b", "NoName057(16)"),
    (r"\bSilent\s+Ransom\s+Group\b|\bLuna\s+Moth\b", "Silent Ransom Group"),
    (r"\bTeamPCP\b", "TeamPCP"),
    (r"\bJINX-0164\b", "JINX-0164"),
    # Generic UNC/APT pattern - low priority, surface as weak tag
    (r"\bAPT\d+\b", None),   # captured below in unknown_apt fallback
    (r"\bUNC\d+\b", None),
]

INDUSTRIES = [
    (r"\bhealthcare\b|\bhospital\b|\bmedical\b|\bclinic\b|\bpatient\s+data\b", "healthcare"),
    (r"\bfinanc(?:e|ial)\b|\bbank(?:ing)?\b|\bfintech\b|\bcrypto(?:currency)?\b", "financial_services"),
    (r"\bgovern\w+|\bfederal\b|\bmunicipal\b|\bstate\s+agency\b|\bpublic\s+sector\b", "government"),
    (r"\bcritical\s+infrastructure\b|\benergy\b|\butilit\w+|\bwater\s+treatment\b|\boil\s+and\s+gas\b", "critical_infrastructure"),
    (r"\bmanufactur\w+|\bindustrial\b|\bOT\s+network\b|\bICS\b|\bSCADA\b|\bPLC\b", "manufacturing_industrial"),
    (r"\btelecom\w*|\bISP\b|\bbroadband\b|\bcellular\b", "telecommunications"),
    (r"\baviation\b|\bairline\b|\baerospace\b|\bdefense\s+contractor\b", "aviation_defense"),
    (r"\beducation\b|\buniversit\w+|\bcolleg\w+|\bschool\s+district\b|\bk-12\b", "education"),
    (r"\bretail\b|\be-?commerce\b|\bpoint[-\s]of[-\s]sale\b|\bPOS\b", "retail_ecommerce"),
    (r"\blegal\b|\blaw\s+firm\b|\bcounsel\b", "legal_professional"),
    (r"\bmedia\s+(?:company|organization)\b|\bbroadcast\w+|\bnews\s+(?:agency|organization)", "media_communications"),
]

THREAT_CATEGORIES = [
    (r"\bransomware\b|\bextortion\b|\bdouble[-\s]extortion\b", "ransomware_extortion"),
    (r"\bsupply[-\s]chain\b(?:\s+attack|\s+compromis)?", "supply_chain"),
    (r"\bphish\w+|\bsmish\w+|\bvish\w+|\bsocial\s+engineering\b", "phishing_social_eng"),
    (r"\bcredential\s+theft\b|\binfostealer\b|\bcredential\s+stuffing\b|\btoken\s+theft\b|\bsession\s+hijack\w+", "credential_theft"),
    (r"\bzero[-\s]?day\b", "zero_day"),
    (r"\bdata\s+breach\b|\bdata\s+leak\b|\bdata\s+exposure\b", "data_breach"),
    (r"\bDDoS\b|\bdenial[-\s]of[-\s]service\b", "ddos"),
    (r"\bAPT\b|\bstate[-\s]sponsored\b|\bnation[-\s]state\b|\bespionage\b", "apt_espionage"),
    (r"\bcryptojack\w+|\bcoin\s?mining\b|\bgpu\s+mining\b", "cryptojacking"),
    (r"\bprompt\s+injection\b|\bmodel\s+poisoning\b|\bagent\s+(?:abuse|drift|hijack)\b|\bagentic\s+exfiltration\b", "ai_security"),
    (r"\bweb\s?shell\b|\bbackdoor\b", "web_shell_backdoor"),
    (r"\bcloud\s+(?:misconfig|abuse|attack)\b|\bcloud[-\s]native\s+attack\b|\bOAuth\s+abuse\b", "cloud_abuse"),
    (r"\bMFA\s+(?:bypass|prompt\s+bombing|fatigue)\b|\bAiTM\b|\badversary[-\s]in[-\s]the[-\s]middle\b", "mfa_bypass"),
    (r"\bvulnerability\s+disclos\w+|\badvisor\w+\s+released\b", "vulnerability_disclosure"),
    (r"\bactive(?:ly)?\s+exploited\b|\bin[-\s]the[-\s]wild\b|\bexploitation\s+observed\b", "active_exploitation"),
]

# Things that should never trigger a target tag, even with proximity.
# These are common page-furniture phrases that produced false positives in v1.
NEGATIVE_PRODUCT_CONTEXTS = (
    r"sign\s+(?:in|up)\s+with\s+\w+",
    r"discuss\s+with\s+Claude",
    r"available\s+on\s+(?:GitHub|GitLab)",
    r"hosted\s+on\s+GitHub",
    r"source\s+code\s+on\s+GitHub",
    r"open[-\s]source(?:d)?\s+on\s+GitHub",
    r"follow\s+(?:us|the\s+\w+)\s+on\s+\w+",
    r"published\s+on\s+\w+",
    r"sponsored\s+by\b",
)

# Non-CTI patterns. Items matching any of these are flagged with content_type
# "out_of_scope" and should be filtered out of the public feed entirely.
# These match cybersecurity-adjacent keywords (online, social media, identity)
# but are not threat intelligence content — they're general-crime reporting,
# personal-tragedy stories, or human-interest pieces that the feed should
# never surface alongside actual CTI.
#
# Erring on the side of false-positives here is correct. Worst case is a
# legitimate CTI item being dropped because it mentions one of these terms;
# that's fixable with a noise_exempt check (e.g., if a story also names a
# threat actor or CVE, keep it). The reverse — letting non-CTI items reach
# the page — is much worse, particularly for content involving minors or
# personal harm.
OUT_OF_SCOPE_PATTERNS = (
    # Child exploitation / CSAM / luring — never display, never tag
    r"\b(?:child|minor|underage|teen)\s+(?:exploit|abuse|porn|sex(?:ual)?|luring|enticement|grooming)\b",
    r"\b(?:CSAM|child\s+sexual\s+abuse\s+material)\b",
    r"\b(?:luring|enticement|grooming|sextort\w+)\s+(?:of\s+)?(?:children|minors|kids|teens)\b",
    r"\b(?:coerce\w*|manipulat\w+)\s+(?:children|minors|kids|teens)\b",
    r"\bsexually\s+explicit\s+(?:images|videos|content)\b",
    r"\bpredator\s+(?:targeting|contacting)\s+(?:children|minors|kids)\b",
    # Personal-crime / domestic violence / stalking of individuals
    r"\bdomestic\s+(?:violence|abuse|partner)\b",
    r"\bstalk\w+\s+(?:victim|individual|partner|spouse|ex-?)\b(?!.*(?:campaign|operation|APT))",
    # General criminal prosecution unrelated to cyber threats
    r"\bsentenced\s+to\s+\d+\s+years?\b.*\b(?:luring|exploitation|child|minor)\b",
)

# Confidence thresholds
MIN_CONFIDENCE = 0.4
HIGH_CONFIDENCE = 0.8

# Hard caps post-extraction
MAX_PRODUCTS = 3
MAX_CVES = 5
MAX_ACTORS = 3
MAX_INDUSTRIES = 4

# Compile once
THREAT_ANCHOR_RE = re.compile("|".join(THREAT_ANCHORS), re.IGNORECASE)
TOOL_ANCHOR_RE = re.compile("|".join(TOOL_ANCHORS), re.IGNORECASE)
VENDOR_ANCHOR_RE = re.compile("|".join(VENDOR_ANCHORS), re.IGNORECASE)
NEGATIVE_CONTEXT_RE = re.compile("|".join(NEGATIVE_PRODUCT_CONTEXTS), re.IGNORECASE)
OUT_OF_SCOPE_RE = re.compile("|".join(OUT_OF_SCOPE_PATTERNS), re.IGNORECASE)
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)
MITRE_TID_RE = re.compile(r"\bT\d{4}(?:\.\d{3})?\b")

CONFIDENCE_TIER_MAP = {
    "threat_research_primary": "tier_1_primary_research",
    "offensive_vulnerability_research": "tier_1_offensive_research",
    "government_authoritative": "tier_1_government",
    "detection_response_operations": "tier_2_operator",
    "cloud_identity_infrastructure": "tier_2_operator",
    "ai_security_agentic_risk": "tier_2_operator",
    "ransomware_ecrime_financial_crime": "tier_2_operator",
    "practitioner_analysis": "tier_3_analysis",
    "policy_strategy_geopolitics": "tier_3_analysis",
    "cyber_news_breach_reporting": "tier_4_news",
    "reddit_practitioner_osint": "tier_5_chatter",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _anchored_matches(text, term_re, anchor_re, window=PROXIMITY_WINDOW):
    """Find matches of term_re that are within `window` chars of any anchor.

    Returns list of (term_match_str, position, anchor_distance).
    """
    anchors = [(m.start(), m.end()) for m in anchor_re.finditer(text)]
    if not anchors:
        return []

    hits = []
    for m in term_re.finditer(text):
        pos = m.start()
        # nearest anchor distance
        nearest = min(
            (max(0, pos - aend, astart - m.end()) for astart, aend in anchors),
            default=10 ** 9,
        )
        if nearest <= window:
            hits.append((m.group(0), pos, nearest))
    return hits


def _classify_role(text, term_pos, term_len):
    """Decide if a product mention near a threat anchor is target/tool/vendor.

    Walks the surrounding ±120 chars and checks which anchor class fires.
    """
    span_start = max(0, term_pos - 120)
    span_end = min(len(text), term_pos + term_len + 120)
    window = text[span_start:span_end]

    if NEGATIVE_CONTEXT_RE.search(window):
        return "mention"
    if TOOL_ANCHOR_RE.search(window):
        return "tool"
    if VENDOR_ANCHOR_RE.search(window):
        return "vendor"
    if THREAT_ANCHOR_RE.search(window):
        return "target"
    return "mention"


def _confidence(role, distance_to_anchor, in_first_paragraph):
    """Confidence score for a tag.

    Higher when role is unambiguous, close to anchor, and in first paragraph.
    """
    base = {
        "target": 0.85,
        "tool": 0.7,
        "vendor": 0.5,
        "mention": 0.25,
    }[role]
    proximity_bonus = max(0.0, 0.15 * (1 - distance_to_anchor / PROXIMITY_WINDOW))
    first_para_bonus = 0.1 if in_first_paragraph else 0.0
    return min(1.0, base + proximity_bonus + first_para_bonus)


def _first_paragraph_end(text, cutoff=600):
    """Approximate end of first paragraph or first 600 chars, whichever first."""
    para = text.find("\n\n")
    if para == -1 or para > cutoff:
        return cutoff
    return para


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def extract_taxonomy(title, summary, source, cohort, full_body=""):
    """Extract a structured taxonomy from an article.

    Returns a dict with:
      threat_categories, actor_attribution, affected_industries,
      affected_products, cve_ids, attack_techniques, urgency_signals,
      content_type, confidence_tier,
      role_map (product -> role), weak_tags (dropped low-confidence tags)
    """
    # Build the haystack. Title and summary get double-weight by appearing
    # in the "first paragraph" region.
    body = (full_body or "").strip()
    haystack = "\n\n".join(filter(None, [title, summary, body]))
    fp_end = _first_paragraph_end(haystack)

    # Extract CVEs. Cap at MAX_CVES. Preference: CVEs in title/summary first.
    cves_seen = []
    for m in CVE_RE.finditer(haystack):
        cve = m.group(0).upper()
        if cve not in cves_seen:
            cves_seen.append(cve)
    # Prefer CVEs that appear in the first paragraph
    first_para_cves = [c for c in cves_seen if c in haystack[:fp_end]]
    other_cves = [c for c in cves_seen if c not in first_para_cves]
    cve_ids = (first_para_cves + other_cves)[:MAX_CVES]

    # MITRE techniques — require co-location with "MITRE", "ATT&CK", or
    # "technique" context to avoid false positives on product model
    # numbers like "T3000" or "T2000" that aren't actual technique IDs.
    mitre_context = re.search(r"\b(?:MITRE|ATT&?CK|technique\w*|tactic\w*|TTPs?)\b", haystack, re.IGNORECASE)
    if mitre_context:
        mitre_tids = sorted({m.group(0) for m in MITRE_TID_RE.finditer(haystack)})
    else:
        mitre_tids = []

    # Products with role and confidence
    product_tags = []  # list of (label, role, confidence)
    for pattern, label in PRODUCTS:
        term_re = re.compile(pattern, re.IGNORECASE)
        hits = _anchored_matches(haystack, term_re, THREAT_ANCHOR_RE)
        if not hits:
            continue
        # Use the best (highest-confidence) hit for this product
        best = None
        for term, pos, dist in hits:
            role = _classify_role(haystack, pos, len(term))
            conf = _confidence(role, dist, pos < fp_end)
            if not best or conf > best[2]:
                best = (label, role, conf)
        product_tags.append(best)

    # Sort by confidence, dedupe by label
    product_tags.sort(key=lambda t: -t[2])
    seen_labels = set()
    deduped = []
    for label, role, conf in product_tags:
        if label in seen_labels:
            continue
        seen_labels.add(label)
        deduped.append((label, role, conf))
    product_tags = deduped

    # Split into accepted target tags and weak/other tags
    target_products = [(l, c) for l, r, c in product_tags if r == "target" and c >= MIN_CONFIDENCE]
    tool_products = [(l, c) for l, r, c in product_tags if r == "tool" and c >= MIN_CONFIDENCE]
    weak_products = [(l, r, c) for l, r, c in product_tags if c < MIN_CONFIDENCE or r in ("vendor", "mention")]

    affected_products = [l for l, _ in target_products[:MAX_PRODUCTS]]
    tools_used = [l for l, _ in tool_products[:MAX_PRODUCTS]]

    # Role map for downstream consumers (affinity must use this to ignore tools)
    role_map = {l: r for l, r, _ in product_tags}

    # Actors. Same proximity-anchored approach; actors mentioned near threat
    # context get tagged. No role disambiguation — an actor mentioned in CTI
    # context is always a subject, not a tool.
    actor_tags = []
    for pattern, label in ACTORS:
        if label is None:
            continue
        term_re = re.compile(pattern, re.IGNORECASE)
        hits = _anchored_matches(haystack, term_re, THREAT_ANCHOR_RE)
        if hits:
            actor_tags.append(label)
    # Unknown APT/UNC fallback - capture if uncategorized
    for term in re.findall(r"\bAPT\d+\b|\bUNC\d{3,4}\b", haystack):
        if term not in actor_tags and len(actor_tags) < MAX_ACTORS:
            actor_tags.append(term)
    actor_attribution = actor_tags[:MAX_ACTORS]

    # Industries
    industries = []
    for pattern, label in INDUSTRIES:
        if re.search(pattern, haystack, re.IGNORECASE) and label not in industries:
            industries.append(label)
    affected_industries = industries[:MAX_INDUSTRIES]

    # Categories
    categories = []
    for pattern, label in THREAT_CATEGORIES:
        if re.search(pattern, haystack, re.IGNORECASE) and label not in categories:
            categories.append(label)
    threat_categories = categories

    # Urgency signals
    urgency = []
    if re.search(r"\bactively\s+exploited\b|\bin\s+the\s+wild\b", haystack, re.IGNORECASE):
        urgency.append("actively_exploited")
    if re.search(r"\bzero[-\s]?day\b", haystack, re.IGNORECASE):
        urgency.append("zero_day")
    if re.search(r"\bunauthenticated\b|\bpre[-\s]?auth\b", haystack, re.IGNORECASE):
        urgency.append("preauth_unauth")
    if re.search(r"\bemergency\s+patch\b|\bout[-\s]of[-\s]band\s+patch\b", haystack, re.IGNORECASE):
        urgency.append("emergency_patch")
    if re.search(r"\bno\s+patch\b|\bnot\s+(?:fixed|patched)\b|\bunpatched\b", haystack, re.IGNORECASE):
        urgency.append("no_patch_yet")
    if re.search(r"\bPoC\b|\bproof[-\s]of[-\s]concept\s+(?:exploit|code)\b", haystack, re.IGNORECASE):
        urgency.append("poc_available")
    if re.search(r"\bCVSS\s*[:\s]?\s*(?:9\.\d|10(?:\.0)?)\b", haystack, re.IGNORECASE):
        urgency.append("critical_cvss")

    # Content type heuristic. Pass the extracted taxonomy so the classifier
    # can spot low-signal items that have NO CTI anchors at all (no CVE,
    # no actor, no target product, no threat-category match, no urgency
    # signals). Those are dropped from the feed even if they're nominally
    # CTI-adjacent (Reddit chatter, career questions, hardware retirements).
    content_type = _classify_content_type(
        title=title,
        body=haystack,
        source=source,
        cohort=cohort,
        threat_categories=threat_categories,
        actor_attribution=actor_attribution,
        affected_products=affected_products,
        cve_ids=cve_ids,
        urgency=urgency,
        mitre_tids=mitre_tids,
    )

    confidence_tier = CONFIDENCE_TIER_MAP.get(cohort, "tier_5_chatter")

    return {
        "threat_categories": threat_categories,
        "actor_attribution": actor_attribution,
        "affected_industries": affected_industries,
        "affected_products": affected_products,
        "tools_used": tools_used,
        "cve_ids": cve_ids,
        "attack_techniques": mitre_tids,
        "urgency_signals": urgency,
        "content_type": content_type,
        "confidence_tier": confidence_tier,
        "role_map": role_map,
        "weak_tags": {"products": [(l, r, round(c, 2)) for l, r, c in weak_products]},
    }


def _classify_content_type(title, body, source, cohort="",
                           threat_categories=None, actor_attribution=None,
                           affected_products=None, cve_ids=None,
                           urgency=None, mitre_tids=None):
    """Identify what kind of article this is.

    Differentiates vendor announcements (low signal) from primary research
    (high signal) from incident reports from analysis pieces. Short-circuits
    to "out_of_scope" for cybersecurity-adjacent content that isn't actually
    CTI (child exploitation prosecutions, personal crime, etc.), and to
    "low_signal" for items that nominally come from a CTI feed but have
    no CTI anchors at all (Reddit chatter, career questions, hardware
    retirement posts, general IT operations).
    """
    t = title.lower()
    b = body.lower()[:1500]  # head of body only

    # Out-of-scope check first. If this matches, the item should be
    # dropped from the feed entirely. We keep an escape hatch: if the
    # body also contains a clear CTI anchor (CVE, threat actor name,
    # cybersecurity-product context), the item is legitimate CTI that
    # happens to discuss these topics (e.g., a story about a CSAM
    # distribution platform takedown that names specific malware).
    combined = f"{t} {b}"
    if OUT_OF_SCOPE_RE.search(combined):
        has_cti_anchor = (
            CVE_RE.search(combined)
            or re.search(r"\b(?:APT\d+|UNC\d+|ransomware\s+gang|threat\s+actor|botnet|C2|malware\s+family)\b", combined, re.IGNORECASE)
            or re.search(r"\b(?:phishing\s+kit|infostealer|RAT|backdoor|exploit\s+kit)\b", combined, re.IGNORECASE)
        )
        if not has_cti_anchor:
            return "out_of_scope"

    # Low-signal check: items with NO CTI anchors at all. This catches the
    # long tail of Reddit chatter — career advice, vendor pricing, hardware
    # retirement posts, customer-service-training questions — that match
    # the feed's source list but contribute nothing of CTI substance.
    #
    # An item is low_signal when none of these hold:
    #   - has a CVE
    #   - has a named threat actor
    #   - has a target product (something attackable)
    #   - has a threat category (ransomware, supply_chain, etc.)
    #   - has an urgency signal (actively exploited, 0-day, etc.)
    #   - has a MITRE technique ID
    #   - title or body contains a generic-but-CTI-relevant term (malware,
    #     vulnerability, exploit, attack, breach, phishing, ransomware,
    #     etc.) — this catches Tier 1 articles that may not have specific
    #     CVEs/actors named but are clearly CTI in subject
    has_structured_signal = bool(
        (cve_ids or [])
        or (actor_attribution or [])
        or (affected_products or [])
        or (threat_categories or [])
        or (urgency or [])
        or (mitre_tids or [])
    )
    if not has_structured_signal:
        GENERIC_CTI_TERMS = re.compile(
            r"\b(?:malware|vulnerab\w+|exploit\w*|attack(?:er|ed|ing|s)?|breach\w*|"
            r"phish\w+|ransomware|hacker\w*|intrusion\w*|compromise\w+|backdoor\w*|"
            r"trojan|infostealer|botnet|web\s?shell|patch\b|advisor\w+|disclos\w+|"
            r"threat\s+(?:actor|intel|hunting|research)|red\s+team|blue\s+team|"
            r"detection\s+engineer\w+|incident\s+response|SOC\b|SIEM\b|EDR\b|XDR\b|"
            r"hunting\s+quer\w+|KQL\b|sigma\s+rule\b|YARA\b)",
            re.IGNORECASE,
        )
        if not GENERIC_CTI_TERMS.search(combined):
            # Reddit cohorts get a slightly looser pass: the cohort itself
            # is signal, so we only drop them when they're truly off-topic.
            # But "basic customer service training" with no CTI terms IS
            # truly off-topic.
            return "low_signal"

    # Vendor announcement patterns — kill this dead
    if any(p in t for p in [
        "unveils", "introduces", "announces", "launches",
        "now available", "general availability", "ga release",
        "partnership with", "named a leader", "magic quadrant",
        "earnings", "investor", "appoints", "hires",
    ]):
        return "vendor_announcement"

    # Webinar / event
    if any(p in t for p in ["webinar", "virtual event", "register now", "join us"]):
        return "event_promotion"

    # Vulnerability disclosure
    if "CVE-" in title or "vulnerability" in t or "advisory" in t:
        return "vulnerability_disclosure"

    # Incident / breach
    if any(p in t for p in [
        "data breach", "confirmed breach", "attack on", "compromised",
        "ransomware attack", "extortion", "leak", "exfiltrated",
    ]):
        return "incident_report"

    # Original threat research
    if any(p in b[:600] for p in [
        "we discovered", "our research", "we identified",
        "our analysis", "we observed", "we analyzed",
        "this post details", "in this report we",
    ]):
        return "threat_research"

    # Roundup / weekly
    if any(p in t for p in ["weekly recap", "intelligence insights", "threat landscape", "weekly wrap"]):
        return "intel_roundup"

    return "news_report"
