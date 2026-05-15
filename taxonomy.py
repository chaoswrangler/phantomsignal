"""
Taxonomy extraction for CTI items.

Pattern-based, deterministic enrichment. No LLM calls.
Maintain the dictionaries below; everything else is mechanical.

Public surface:
    extract_taxonomy(title, summary, source, cohort, full_body="") -> dict
"""

import re
from collections import Counter

# ---------------------------------------------------------------------------
# Threat categories — the "what kind of threat is this" axis
# ---------------------------------------------------------------------------
# Order matters: higher-specificity patterns first so they don't get
# pre-empted by broader categories.
THREAT_CATEGORIES = {
    "ransomware": [
        r"\bransomware\b", r"\bdouble[\s-]extortion\b", r"\bdata[\s-]extortion\b",
        r"\b(?:LockBit|BlackCat|ALPHV|Cl0p|Akira|RansomHub|BlackBasta|Royal|Play|Medusa|Qilin|Hunters International|RansomEXX)\b",
    ],
    "data_breach": [
        r"\bdata[\s-]breach\b", r"\bdatabase[\s-]leak\b",
        r"\b\d[\d,]*\s*(?:million|billion)\s+(?:\w+\s+){0,3}(?:records|users|accounts|customers|individuals|people)\b",
        r"\bexposed\s+(?:customer|user|employee|student|patient)\s+data\b",
        r"\bcredentials\s+(?:leaked|exposed|stolen|dumped)\b",
        r"\b(?:posted|leaked|dumped)\s+(?:on|to)\s+(?:a\s+)?(?:hacking|leak|data\s+leak|criminal)\s+forum\b",
    ],
    "supply_chain": [
        r"\bsupply[\s-]chain\s+(attack|compromise|breach)\b", r"\bdependency\s+confusion\b",
        r"\bmalicious\s+(package|npm|pypi|gem|crate)\b", r"\btyposquat", r"\bSBOM\b",
    ],
    "zero_day": [
        r"\bzero[\s-]?day\b", r"\b0[\s-]?day\b", r"\bin[\s-]the[\s-]wild\s+exploit",
        r"\bunpatched\s+vulnerability\b",
    ],
    "active_exploitation": [
        r"\bactively\s+exploited\b", r"\bexploited\s+in\s+the\s+wild\b",
        r"\bobserved\s+exploitation\b", r"\bmass\s+exploitation\b",
    ],
    "vulnerability_disclosure": [
        r"\bCVE-\d{4}-\d{4,7}\b", r"\bCVSS\b", r"\bvulnerability\s+(disclosed|patched|discovered)\b",
        r"\bsecurity\s+advisory\b", r"\bpatch\s+(released|available|tuesday)\b",
    ],
    "malware": [
        r"\bmalware\b", r"\binfostealer\b", r"\bbackdoor\b", r"\btrojan\b",
        r"\brootkit\b", r"\bbotnet\b", r"\bloader\b", r"\bdropper\b", r"\bworm\b",
        r"\bRAT\b(?!\w)", r"\brootkits?\b",
    ],
    "phishing_social_eng": [
        r"\bphish(ing|ed)?\b", r"\bspear[\s-]phish", r"\bvishing\b", r"\bsmishing\b",
        r"\bsocial\s+engineering\b", r"\bBEC\b", r"\bbusiness\s+email\s+compromise\b",
        r"\bcallback\s+phishing\b", r"\bMFA\s+fatigue\b", r"\bMFA\s+bombing\b",
    ],
    "credential_attack": [
        r"\bcredential\s+(stuff|theft|harvest|stealer|dump)", r"\btoken\s+theft\b",
        r"\bsession\s+(hijack|theft|cookie\s+theft)\b", r"\bOAuth\s+abuse\b",
        r"\bpass[\s-]the[\s-](hash|ticket)\b", r"\bgolden\s+ticket\b",
    ],
    "nation_state": [
        r"\bnation[\s-]state\b", r"\bstate[\s-]sponsored\b", r"\bstate[\s-]backed\b",
        r"\bAPT\d+\b", r"\bcyber\s+espionage\b",
    ],
    "ddos": [
        r"\bDDoS\b", r"\b(?:distributed[\s-])?denial[\s-]of[\s-]service\b", r"\bbotnet\s+attack\b",
    ],
    "cloud_attack": [
        r"\bcloud\s+(attack|compromise|breach)\b", r"\bS3\s+bucket\b", r"\bIAM\s+(abuse|misconfig)",
        r"\bcontainer\s+escape\b", r"\bKubernetes\s+(attack|compromise)\b",
    ],
    "identity_attack": [
        r"\bidentity\s+(attack|compromise|abuse)\b", r"\bEntra\s+(ID\s+)?abuse\b",
        r"\bConditional\s+Access\s+bypass\b", r"\bAzure\s+AD\s+(attack|compromise)\b",
        r"\bSAML\s+(forge|abuse|attack)\b", r"\bJWT\s+(forge|manipulation)\b",
    ],
    "ai_security": [
        r"\bprompt\s+injection\b", r"\bjailbreak\b", r"\bmodel\s+(poisoning|abuse|exploitation)\b",
        r"\bagentic\s+(risk|abuse|attack)\b", r"\bLLM\s+(abuse|exploit|attack)\b",
        r"\bAI\s+(agent|model)\s+(abuse|attack)\b", r"\bMCP\s+(abuse|attack|server)\b",
    ],
    "iot_ot": [
        r"\bICS\b", r"\bSCADA\b", r"\bOT\s+(security|attack|network)\b",
        r"\bIoT\s+(attack|compromise|botnet)\b", r"\bPLC\b", r"\bindustrial\s+control",
    ],
    "policy_regulation": [
        r"\bSEC\s+(rule|filing|disclosure)\b", r"\bGDPR\b", r"\bHIPAA\b",
        r"\bexecutive\s+order\b", r"\bsanctions\b", r"\bCISA\s+(directive|advisory)\b",
    ],
}

# ---------------------------------------------------------------------------
# Threat actors — including aliases and ecosystem groups
# ---------------------------------------------------------------------------
# Each canonical name maps to a list of patterns/aliases.
# Add new actors here as they become relevant.
ACTOR_DICTIONARY = {
    # Ransomware groups
    "LockBit": [r"\bLockBit\s*[2-4]?\.?\d?\b", r"\bLockBitSupp\b"],
    "BlackCat/ALPHV": [r"\bBlackCat\b", r"\bALPHV\b"],
    "Cl0p": [r"\bCl0p\b", r"\bClop\b"],
    "Akira": [r"\bAkira\s+(ransomware|group)\b"],
    "RansomHub": [r"\bRansomHub\b"],
    "BlackBasta": [r"\bBlack\s*Basta\b"],
    "Qilin": [r"\bQilin\b", r"\bAgenda\s+ransomware\b"],
    "Medusa": [r"\bMedusa\s+(ransomware|group)\b"],
    "Hunters International": [r"\bHunters\s+International\b"],
    "Play": [r"\bPlay\s+ransomware\b"],
    # ecrime / extortion
    "ShinyHunters": [r"\bShinyHunters\b", r"\bShiny\s+Hunters\b"],
    "Scattered Spider": [r"\bScattered\s+Spider\b", r"\bUNC3944\b", r"\bMuddled\s+Libra\b", r"\bOktapus\b"],
    "Lapsus$": [r"\bLapsus\$?\b", r"\bDEV-0537\b"],
    "FIN7": [r"\bFIN7\b"],
    "TA505": [r"\bTA505\b"],
    "TA577": [r"\bTA577\b"],
    "TA866": [r"\bTA866\b"],
    # Nation-state actors
    "APT28/Fancy Bear": [r"\bAPT28\b", r"\bFancy\s+Bear\b", r"\bSofacy\b", r"\bSTRONTIUM\b", r"\bForest\s+Blizzard\b"],
    "APT29/Cozy Bear": [r"\bAPT29\b", r"\bCozy\s+Bear\b", r"\bMidnight\s+Blizzard\b", r"\bNOBELIUM\b"],
    "APT41": [r"\bAPT41\b", r"\bBarium\b", r"\bWinnti\b", r"\bBrass\s+Typhoon\b"],
    "Volt Typhoon": [r"\bVolt\s+Typhoon\b"],
    "Salt Typhoon": [r"\bSalt\s+Typhoon\b"],
    "Flax Typhoon": [r"\bFlax\s+Typhoon\b"],
    "Mustang Panda": [r"\bMustang\s+Panda\b", r"\bTwill\s+Typhoon\b", r"\bBronze\s+President\b"],
    "Kimsuky": [r"\bKimsuky\b", r"\bEmerald\s+Sleet\b", r"\bVelvet\s+Chollima\b"],
    "Lazarus": [r"\bLazarus\s+Group\b", r"\bLazarus\b(?!\s+University)", r"\bHidden\s+Cobra\b", r"\bDiamond\s+Sleet\b"],
    "Sandworm": [r"\bSandworm\b", r"\bSeashell\s+Blizzard\b", r"\bVoodoo\s+Bear\b"],
    "Charming Kitten": [r"\bCharming\s+Kitten\b", r"\bAPT35\b", r"\bMint\s+Sandstorm\b"],
    "MuddyWater": [r"\bMuddyWater\b", r"\bMango\s+Sandstorm\b", r"\bSeedworm\b"],
    "Andariel": [r"\bAndariel\b", r"\bOnyx\s+Sleet\b"],
    "Earth Estries": [r"\bEarth\s+Estries\b"],
}

# Generic APT-N pattern that doesn't match a named actor — extracted separately as fallback.
APT_GENERIC = re.compile(r"\b(APT\d+)\b")

# ---------------------------------------------------------------------------
# Affected products / vendors — the "what was hit" axis
# ---------------------------------------------------------------------------
PRODUCT_DICTIONARY = {
    # Network / edge
    "Fortinet": [r"\bFortinet\b", r"\bFortiGate\b", r"\bFortiManager\b", r"\bFortiAnalyzer\b", r"\bFortiOS\b"],
    "Palo Alto Networks": [r"\bPalo\s+Alto\s+Networks\b", r"\bPAN-OS\b", r"\bGlobalProtect\b"],
    "Cisco": [r"\bCisco\s+(ASA|IOS|Talos|Firepower|Meraki|Webex)\b"],
    "Citrix": [r"\bCitrix\b", r"\bNetScaler\b", r"\bADC\b(?=.*Citrix)"],
    "Ivanti": [r"\bIvanti\b", r"\bConnect\s+Secure\b", r"\bPulse\s+Secure\b", r"\bPolicy\s+Secure\b"],
    "F5": [r"\bF5\s+(BIG-IP|Networks)\b", r"\bBIG-IP\b"],
    "Check Point": [r"\bCheck\s+Point\b", r"\bQuantum\s+Security\b"],
    "SonicWall": [r"\bSonicWall\b"],
    "Juniper": [r"\bJuniper\s+(Networks|Junos)\b"],
    # Microsoft ecosystem
    "Microsoft Windows": [r"\bWindows\s+(10|11|Server|Defender)\b", r"\bMSRC\b"],
    "Microsoft Exchange": [r"\bExchange\s+Server\b", r"\bMicrosoft\s+Exchange\b"],
    "Microsoft 365": [r"\bMicrosoft\s+365\b", r"\bOffice\s+365\b", r"\bM365\b"],
    "Azure": [r"\bAzure\s+(AD|Active\s+Directory|Functions|Storage)?\b"],
    "Entra ID": [r"\bEntra\s+ID\b", r"\bAzure\s+AD\b"],
    "SharePoint": [r"\bSharePoint\b"],
    "Teams": [r"\bMicrosoft\s+Teams\b"],
    # Cloud
    "AWS": [r"\bAWS\b", r"\bAmazon\s+Web\s+Services\b", r"\bEC2\b", r"\bS3\b"],
    "Google Cloud": [r"\bGoogle\s+Cloud\b", r"\bGCP\b"],
    "Kubernetes": [r"\bKubernetes\b", r"\bk8s\b"],
    # Identity
    "Okta": [r"\bOkta\b"],
    "Auth0": [r"\bAuth0\b"],
    "Duo": [r"\bDuo\s+Security\b"],
    # Collaboration / SaaS
    "Slack": [r"\bSlack\b(?!\s+command)"],
    "Salesforce": [r"\bSalesforce\b"],
    "Snowflake": [r"\bSnowflake\b"],
    "GitHub": [r"\bGitHub\b"],
    "GitLab": [r"\bGitLab\b"],
    "Atlassian": [r"\bAtlassian\b", r"\bJira\b", r"\bConfluence\b", r"\bBitbucket\b"],
    "Canvas LMS": [r"\bCanvas\s+(LMS|Instructure)\b", r"\bInstructure\b"],
    "Zendesk": [r"\bZendesk\b"],
    # Developer / Infrastructure
    "Docker": [r"\bDocker\b"],
    "Jenkins": [r"\bJenkins\b"],
    "npm": [r"\bnpm\b"],
    "PyPI": [r"\bPyPI\b"],
    "VMware": [r"\bVMware\b", r"\bvCenter\b", r"\bvSphere\b", r"\bESXi\b"],
    # Mobile / endpoint
    "Apple iOS/macOS": [r"\biOS\b", r"\bmacOS\b", r"\bApple\s+(Security|Silicon)\b"],
    "Android": [r"\bAndroid\b(?=.*(?:security|patch|vulnerability|exploit))"],
    "Chrome": [r"\bChrome\b(?=.*(?:vulnerability|exploit|patch|security))", r"\bV8\b"],
    "Firefox": [r"\bFirefox\b(?=.*(?:vulnerability|exploit|patch|security))"],
    # AI ecosystem
    "OpenAI/ChatGPT": [r"\bOpenAI\b", r"\bChatGPT\b"],
    "Anthropic/Claude": [r"\bAnthropic\b", r"\bClaude\b(?!\s+(?:Monet|Debussy|Levi-Strauss))"],
    "GitHub Copilot": [r"\bGitHub\s+Copilot\b", r"\bCopilot\s+(CLI|Workspace)\b"],
    "Cursor": [r"\bCursor\b(?=.*(?:AI|editor|agent|code))"],
}

# ---------------------------------------------------------------------------
# Industries — derived from victim names and content
# ---------------------------------------------------------------------------
INDUSTRY_DICTIONARY = {
    "healthcare": [
        r"\bhospital\b", r"\bhealthcare\b", r"\bmedical\s+(records?|center|practice)\b",
        r"\bpatient\s+data\b", r"\bHIPAA\b", r"\bClinical\b", r"\bpharma(ceutical)?\b",
    ],
    "financial_services": [
        r"\bbank\b", r"\bbanking\b", r"\bfinancial\s+(services|institution)\b",
        r"\bcredit\s+(card|union)\b", r"\bSWIFT\b", r"\binsurance\b",
        r"\bfintech\b", r"\bpayment\s+processor\b",
    ],
    "government_public_sector": [
        r"\bgovernment\b", r"\bfederal\s+agency\b", r"\bmunicipality\b",
        r"\bstate\s+department\b", r"\bDoD\b", r"\bdefense\s+department\b",
        r"\bcity\s+of\s+\w+\b(?=.*(?:hack|breach|attack))",
    ],
    "education": [
        r"\buniversity\b", r"\bcollege\b(?!\s+football)", r"\bschool\s+district\b",
        r"\bK-12\b", r"\bhigher\s+ed", r"\bCanvas\s+LMS\b", r"\bstudent\s+data\b",
    ],
    "technology": [
        r"\btech\s+(giant|company)\b", r"\bsoftware\s+company\b",
        r"\bsemiconductor\b", r"\bSaaS\s+(provider|company)\b",
    ],
    "manufacturing_industrial": [
        r"\bmanufacturer\b", r"\bindustrial\b(?!\s+control)",
        r"\bautomotive\b", r"\baerospace\b", r"\bsupply\s+chain\s+(disruption|attack)\b",
    ],
    "energy_utilities": [
        r"\benergy\s+(company|sector)\b", r"\butility\b", r"\bpower\s+(grid|company)\b",
        r"\boil\s+and\s+gas\b", r"\belectric\s+(utility|grid)\b",
    ],
    "telecommunications": [
        r"\btelecom(munication)?s?\b", r"\b(AT&T|Verizon|T-Mobile|Comcast|Vodafone|Orange|BT)\b",
        r"\bISP\b", r"\bwireless\s+carrier\b",
    ],
    "retail_ecommerce": [
        r"\bretail(er)?\b", r"\be-?commerce\b", r"\bpoint\s+of\s+sale\b", r"\bPOS\b",
    ],
    "media_entertainment": [
        r"\bmedia\s+company\b", r"\bbroadcaster\b", r"\bnews\s+outlet\b",
        r"\bentertainment\s+(industry|company)\b",
    ],
    "transportation_logistics": [
        r"\bairline\b", r"\bshipping\s+(company|line)\b", r"\bport\s+of\s+\w+\b",
        r"\blogistics\b", r"\btransportation\s+(sector|company)\b",
    ],
    "legal_professional_services": [
        r"\blaw\s+firm\b", r"\bconsulting\s+firm\b", r"\baccounting\s+firm\b",
    ],
}

# ---------------------------------------------------------------------------
# MITRE ATT&CK technique IDs
# ---------------------------------------------------------------------------
MITRE_TECHNIQUE = re.compile(r"\b(T\d{4}(?:\.\d{3})?)\b")

# ---------------------------------------------------------------------------
# Geographic scope — coarse, from victim or actor mentions
# ---------------------------------------------------------------------------
GEOGRAPHIC_DICTIONARY = {
    "united_states": [r"\b(United States|U\.S\.|USA|American)\b"],
    "europe": [r"\b(Europe|EU|European Union)\b"],
    "uk": [r"\b(United Kingdom|U\.K\.|British|England|Britain)\b"],
    "russia": [r"\bRussian?\b"],
    "china": [r"\bChin(a|ese)\b"],
    "north_korea": [r"\bNorth\s+Korea(n)?\b", r"\bDPRK\b"],
    "iran": [r"\bIran(ian)?\b"],
    "ukraine": [r"\bUkrain(e|ian)\b"],
    "israel": [r"\bIsrael(i)?\b"],
    "asia_pacific": [r"\bAPAC\b", r"\bAsia-?Pacific\b"],
    "latin_america": [r"\bLatin\s+America\b", r"\bLatAm\b"],
}

# ---------------------------------------------------------------------------
# Urgency signals — the "how time-sensitive" axis
# ---------------------------------------------------------------------------
URGENCY_SIGNALS = {
    "actively_exploited": [r"\bactively\s+exploited\b", r"\bexploited\s+in\s+the\s+wild\b"],
    "zero_day": [r"\bzero[\s-]?day\b", r"\b0[\s-]?day\b"],
    "poc_available": [r"\bproof[\s-]of[\s-]concept\b", r"\bPoC\b", r"\bexploit\s+code\s+(public|available|released)\b"],
    "patch_available": [r"\bpatch\s+(released|available)\b", r"\bsecurity\s+update\s+available\b"],
    "no_patch_yet": [r"\bno\s+patch\b", r"\bunpatched\b", r"\bworkaround\s+only\b"],
    "mass_exploitation": [r"\bmass\s+(exploitation|scanning)\b", r"\bwidespread\s+exploitation\b"],
    "cisa_kev": [r"\bCISA\s+(KEV|Known\s+Exploited)\b", r"\bKnown\s+Exploited\s+Vulnerabilities\b"],
    "emergency_directive": [r"\bemergency\s+(patch|directive)\b", r"\bout[\s-]of[\s-]band\s+patch\b"],
    "preauth_unauth": [r"\bpre[\s-]auth\b", r"\bunauthenticated\b"],
}

# ---------------------------------------------------------------------------
# Content type — what kind of artifact is this
# ---------------------------------------------------------------------------
CONTENT_TYPE_PATTERNS = {
    "threat_research": [r"\bthreat\s+(research|intelligence|analysis)\b", r"\bcampaign\s+analysis\b"],
    "vulnerability_disclosure": [r"\bCVE-\d{4}-\d{4,7}\b", r"\bsecurity\s+advisory\b"],
    "incident_report": [r"\bincident\s+report\b", r"\bbreach\s+(disclosure|notification)\b"],
    "detection_writeup": [r"\bdetection\s+(rule|writeup|guidance|engineering)\b", r"\bhunting\s+(query|guide)\b"],
    "policy_analysis": [r"\bpolicy\s+(analysis|brief)\b", r"\bregulatory\s+(update|change)\b"],
    "news_report": [r"\b(reported|reports|sources\s+say)\b"],
}

# ---------------------------------------------------------------------------
# Confidence tiers based on source cohort
# ---------------------------------------------------------------------------
COHORT_CONFIDENCE_TIER = {
    "threat_research_primary": "tier_1_primary_research",
    "government_authoritative": "tier_1_government",
    "offensive_vulnerability_research": "tier_1_offensive_research",
    "detection_response_operations": "tier_2_operator",
    "cloud_identity_infrastructure": "tier_2_operator",
    "ai_security_agentic_risk": "tier_2_operator",
    "ransomware_ecrime_financial_crime": "tier_2_operator",
    "policy_strategy_geopolitics": "tier_3_analysis",
    "practitioner_analysis": "tier_3_analysis",
    "cyber_news_breach_reporting": "tier_4_news",
    "reddit_practitioner_osint": "tier_5_chatter",
}


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------

def _match_dictionary(text, dictionary):
    """Return list of canonical names whose patterns match the text."""
    hits = []
    for canonical, patterns in dictionary.items():
        for p in patterns:
            if re.search(p, text, re.IGNORECASE):
                hits.append(canonical)
                break  # one match per canonical is enough
    return hits


def _match_simple(text, simple_dict):
    """For dicts mapping label -> list of patterns. Returns list of labels matched."""
    return _match_dictionary(text, simple_dict)


def extract_cve_ids(text):
    """Extract all CVE IDs, normalized to uppercase."""
    return sorted(set(m.upper() for m in re.findall(r"CVE-\d{4}-\d{4,7}", text, re.IGNORECASE)))


def extract_mitre_techniques(text):
    """Extract MITRE ATT&CK technique IDs (Txxxx or Txxxx.xxx)."""
    return sorted(set(MITRE_TECHNIQUE.findall(text)))


def extract_actors(text):
    """Extract named actors, plus generic APT-N matches not covered by the dictionary."""
    named = _match_dictionary(text, ACTOR_DICTIONARY)

    # Generic APT-N capture for actors not yet in the dictionary.
    generic_apts = set(APT_GENERIC.findall(text))
    # Strip ones already covered (e.g., APT28 is covered as "APT28/Fancy Bear")
    covered_apt_numbers = {"APT28", "APT29", "APT41"}
    extras = sorted(generic_apts - covered_apt_numbers)

    return sorted(set(named)) + extras


def extract_taxonomy(title, summary, source, cohort, full_body=""):
    """
    Return a structured taxonomy dict for one item.

    Args:
        title:     item title
        summary:   item summary (RSS-provided, may be short)
        source:    feed source name
        cohort:    cohort name (e.g., 'threat_research_primary')
        full_body: full article body if fetched (better recall)

    Returns:
        dict with keys: threat_categories, actor_attribution, affected_industries,
        affected_products, cve_ids, attack_techniques, geographic_scope,
        urgency_signals, content_type, confidence_tier
    """
    # Build the text corpus to search over.
    # Weight title heavier by including it twice — improves precision on short feeds.
    haystack_parts = [title, title, summary, full_body or ""]
    haystack = " ".join(p for p in haystack_parts if p)

    return {
        "threat_categories": _match_simple(haystack, THREAT_CATEGORIES),
        "actor_attribution": extract_actors(haystack),
        "affected_industries": _match_simple(haystack, INDUSTRY_DICTIONARY),
        "affected_products": _match_simple(haystack, PRODUCT_DICTIONARY),
        "cve_ids": extract_cve_ids(haystack),
        "attack_techniques": extract_mitre_techniques(haystack),
        "geographic_scope": _match_simple(haystack, GEOGRAPHIC_DICTIONARY),
        "urgency_signals": _match_simple(haystack, URGENCY_SIGNALS),
        "content_type": _classify_content_type(haystack, cohort),
        "confidence_tier": COHORT_CONFIDENCE_TIER.get(cohort, "tier_unknown"),
    }


def _classify_content_type(text, cohort):
    """Return the most specific content type label that applies."""
    matches = _match_simple(text, CONTENT_TYPE_PATTERNS)
    if matches:
        # Specificity ordering: prefer threat_research > vulnerability > incident > detection > policy > news
        priority = ["threat_research", "vulnerability_disclosure", "incident_report",
                    "detection_writeup", "policy_analysis", "news_report"]
        for p in priority:
            if p in matches:
                return p
    # Fall back to cohort-based default.
    if cohort in ("cyber_news_breach_reporting",):
        return "news_report"
    if cohort in ("policy_strategy_geopolitics",):
        return "policy_analysis"
    return "uncategorized"
