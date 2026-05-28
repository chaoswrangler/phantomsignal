const fs = require("fs");
const path = require("path");

const feedPath = path.join(__dirname, "../docs/feed.json");
const outputPath = path.join(__dirname, "../docs/index.html");
const briefPath = path.join(__dirname, "../docs/brief/index.html");

const briefExists = fs.existsSync(briefPath);

const LOOKBACK_DAYS = 7;

const feed = JSON.parse(fs.readFileSync(feedPath, "utf8"));

const excludedNonEnglishSources = new Set([
  "CERT-FR Avis",
  "CERT-FR Alerts"
]);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function stripHtml(value) {
  return String(value ?? "")
    .replace(/<[^>]*>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function formatCategory(value) {
  const labels = {
    threat_research_primary: "Threat Research",
    ai_security_agentic_risk: "AI Security & Agentic Risk",
    government_authoritative: "Government & Authoritative",
    offensive_vulnerability_research: "Offensive Vulnerability Research",
    detection_response_operations: "Detection & Response Operations",
    cloud_identity_infrastructure: "Cloud, Identity & Infrastructure",
    ransomware_ecrime_financial_crime: "Ransomware, eCrime & Financial Crime",
    cyber_news_breach_reporting: "Cyber News & Breach Reporting",
    policy_strategy_geopolitics: "Policy, Strategy & Geopolitics",
    practitioner_analysis: "Practitioner Analysis",
    reddit_practitioner_osint: "Reddit Practitioner OSINT"
  };

  if (labels[value]) return labels[value];

  return String(value ?? "uncategorized")
    .replaceAll("_", " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

function slugify(value) {
  return String(value ?? "general")
    .toLowerCase()
    .replace(/_/g, "-")
    .replace(/[^a-z0-9-]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function formatDate(value) {
  if (!value) return "";

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return value;
  }

  return date.toLocaleString("en-US", {
    timeZone: "America/New_York",
    year: "numeric",
    month: "short",
    day: "2-digit",
    hour: "numeric",
    minute: "2-digit",
    timeZoneName: "short"
  });
}

function domainFromUrl(url) {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return "";
  }
}

function externalLinkAttrs() {
  return 'target="_blank" rel="noopener noreferrer"';
}

function getCutoffDate(days = LOOKBACK_DAYS) {
  const cutoff = new Date();
  cutoff.setDate(cutoff.getDate() - days);
  return cutoff;
}

function getItemTime(item) {
  const date = new Date(item.published || item.updated || item.date || 0);
  return Number.isNaN(date.getTime()) ? 0 : date.getTime();
}

function isWithinLookbackWindow(item, days = LOOKBACK_DAYS) {
  const itemTime = getItemTime(item);

  if (!itemTime) {
    return false;
  }

  return itemTime >= getCutoffDate(days).getTime();
}

function containsMostlyLatinText(value) {
  const text = String(value ?? "").replace(/\s+/g, "");

  if (!text) {
    return true;
  }

  const latinMatches = text.match(/[A-Za-z0-9]/g) || [];
  const cyrillicMatches = text.match(/[\u0400-\u04FF]/g) || [];
  const arabicMatches = text.match(/[\u0600-\u06FF]/g) || [];
  const cjkMatches = text.match(/[\u3040-\u30FF\u3400-\u9FFF]/g) || [];

  const nonLatinCount =
    cyrillicMatches.length +
    arabicMatches.length +
    cjkMatches.length;

  return nonLatinCount === 0 || latinMatches.length >= nonLatinCount * 2;
}

function isEnglishEnoughItem(item) {
  const source = item.source || "";
  const title = item.title || "";
  const summary = stripHtml(item.summary || "");

  if (excludedNonEnglishSources.has(source)) {
    return false;
  }

  const combinedText = `${title} ${summary}`;

  if (!containsMostlyLatinText(combinedText)) {
    return false;
  }

  return true;
}

function isProductMarketingOrPositioning(item) {
  const title = String(item.title || "").toLowerCase();
  const summary = stripHtml(item.summary || "").toLowerCase();
  const source = String(item.source || "").toLowerCase();
  const category = String(item.category || "").toLowerCase();
  const text = `${title} ${summary} ${source} ${category}`;

  const productMarketingTerms = [
    "announcing",
    "announces",
    "announcement",
    "launches",
    "launched",
    "introducing",
    "introduced",
    "general availability",
    "generally available",
    "now available",
    "available now",
    "new feature",
    "new features",
    "product update",
    "platform update",
    "monthly update",
    "release notes",
    "roadmap",
    "preview",
    "public preview",
    "private preview",
    "customer story",
    "case study",
    "partner",
    "partners with",
    "partnership",
    "integrated with",
    "integration",
    "webinar",
    "event recap",
    "conference",
    "keynote",
    "award",
    "recognition",
    "magic quadrant",
    "market guide",
    "buyers guide",
    "best practices for using",
    "how to get started",
    "how we help",
    "protect your business with",
    "modernize your security",
    "transform your security",
    "accelerate your security",
    "secure your ai journey",
    "trusted ai",
    "responsible ai",
    "customer success",
    "business value",
    "roi",
    "total economic impact",
    "forrester",
    "gartner",
    "leader in",
    "named a leader",
    "wins award",
    "named winner",
    "product-led",
    "product led"
  ];

  const productNounTerms = [
    "our platform",
    "our product",
    "our solution",
    "our customers",
    "our partners",
    "our latest",
    "new capability",
    "new capabilities",
    "security solution",
    "security platform",
    "cloud security platform",
    "ai security platform",
    "this release",
    "this update",
    "this feature",
    "this capability"
  ];

  return (
    productMarketingTerms.some((term) => text.includes(term)) ||
    productNounTerms.some((term) => text.includes(term))
  );
}

function isThreatIntelRelevant(item) {
  const title = String(item.title || "").toLowerCase();
  const summary = stripHtml(item.summary || "").toLowerCase();
  const category = String(item.category || "").toLowerCase();
  const source = String(item.source || "").toLowerCase();
  const text = `${title} ${summary} ${source}`;

  const allowedCategories = [
    "threat_research_primary",
    "offensive_vulnerability_research",
    "detection_response_operations",
    "ransomware_ecrime_financial_crime",
    "cyber_news_breach_reporting",
    "reddit_practitioner_osint"
  ];

  const allowedAiSecurityTerms = [
    "prompt injection",
    "agentic",
    "ai agent",
    "ai agents",
    "llm",
    "model abuse",
    "model exploitation",
    "remote code execution",
    "rce",
    "vulnerability",
    "exploit",
    "exploitation",
    "oauth",
    "token theft",
    "credential",
    "malware",
    "phishing",
    "supply chain",
    "mcp",
    "coding agent",
    "claude code",
    "copilot cli",
    "cursor",
    "gemini cli"
  ];

  const ctiTerms = [
    "active exploitation",
    "actively exploited",
    "exploited in the wild",
    "in the wild",
    "zero-day",
    "zero day",
    "0-day",
    "rce",
    "remote code execution",
    "privilege escalation",
    "vulnerability",
    "cve-",
    "cvss",
    "exploit",
    "exploitation",
    "malware",
    "ransomware",
    "backdoor",
    "stealer",
    "infostealer",
    "loader",
    "worm",
    "botnet",
    "trojan",
    "phishing",
    "credential theft",
    "credential stealer",
    "token theft",
    "oauth",
    "apt",
    "state-sponsored",
    "state sponsored",
    "nation-state",
    "nation state",
    "campaign",
    "intrusion",
    "breach",
    "compromise",
    "ioc",
    "iocs",
    "indicator",
    "indicators",
    "tactics",
    "techniques",
    "procedures",
    "ttp",
    "ttps",
    "detection",
    "hunting",
    "threat actor",
    "espionage",
    "supply chain attack",
    "supply-chain attack",
    "cloud secrets",
    "cloud credentials",
    "initial access",
    "persistence",
    "lateral movement",
    "command and control",
    "c2",
    "exfiltration",
    "dll sideloading",
    "webshell",
    "web shell",
    "implant",
    "post-exploitation",
    "post exploitation"
  ];

  const explicitNonCtiTerms = [
    "world passkey day",
    "passwordless authentication",
    "monthly digest",
    "icymi",
    "funding",
    "raises $",
    "trial pitting",
    "risks to humanity",
    "scholarship program",
    "new leader",
    "data center deal",
    "sub-millisecond",
    "certifications",
    "supply chain decisions",
    "customer service agents",
    "big words",
    "unplug your way to better code",
    "presentation tool",
    "keynote",
    "conference",
    "webinar today",
    "public good",
    "board room",
    "operator",
    "socially cohesive",
    "democracy",
    "political violence",
    "early edition",
    "podcast",
    "forecasting",
    "prediction markets"
  ];

  if (isProductMarketingOrPositioning(item)) {
    return false;
  }

  if (explicitNonCtiTerms.some((term) => text.includes(term))) {
    return false;
  }

  const categoryAllowed = allowedCategories.includes(category);
  const hasCtiTerm = ctiTerms.some((term) => text.includes(term));

  if (categoryAllowed && hasCtiTerm) {
    return true;
  }

  if (category === "ai_security_agentic_risk") {
    return allowedAiSecurityTerms.some((term) => text.includes(term));
  }

  return false;
}

function isBreachOrThreatInsight(item) {
  const title = String(item.title || "").toLowerCase();
  const summary = stripHtml(item.summary || "").toLowerCase();
  const category = String(item.category || "").toLowerCase();
  const source = String(item.source || "").toLowerCase();
  const text = `${title} ${summary} ${category} ${source}`;

  const breachTerms = [
    "breach",
    "breached",
    "data breach",
    "data leak",
    "leaked",
    "leak",
    "exposed",
    "exposure",
    "stolen",
    "stole",
    "theft",
    "compromised",
    "compromise",
    "intrusion",
    "incident",
    "unauthorized access",
    "exfiltration",
    "extortion",
    "ransomware",
    "victim",
    "victims"
  ];

  const threatTerms = [
    "active exploitation",
    "actively exploited",
    "exploited in the wild",
    "in the wild",
    "zero-day",
    "zero day",
    "0-day",
    "cve-",
    "rce",
    "remote code execution",
    "privilege escalation",
    "exploit",
    "exploitation",
    "malware",
    "backdoor",
    "stealer",
    "infostealer",
    "loader",
    "trojan",
    "botnet",
    "phishing",
    "credential theft",
    "credential stealer",
    "token theft",
    "oauth abuse",
    "supply chain attack",
    "supply-chain attack",
    "campaign",
    "threat actor",
    "apt",
    "state-sponsored",
    "state sponsored",
    "nation-state",
    "nation state",
    "initial access",
    "persistence",
    "lateral movement",
    "command and control",
    "c2",
    "webshell",
    "web shell",
    "implant",
    "post-exploitation",
    "post exploitation",
    "iocs",
    "indicator of compromise",
    "indicators of compromise",
    "ttps",
    "tactics techniques and procedures"
  ];

  const insightSources = [
    "bleepingcomputer",
    "the hacker news",
    "securityweek",
    "the record",
    "cyberscoop",
    "mandiant",
    "unit 42",
    "crowdstrike",
    "sentinelone",
    "red canary",
    "huntress",
    "cisa",
    "microsoft",
    "google",
    "wiz",
    "expel",
    "proofpoint",
    "talos",
    "sophos",
    "rapid7",
    "watchtowr",
    "arctic wolf",
    "elastic",
    "zscaler",
    "cloudflare",
    "sucuri",
    "malwarebytes",
    "greynoise",
    "exploit-db"
  ];

  const hasBreachSignal = breachTerms.some((term) => text.includes(term));
  const hasThreatSignal = threatTerms.some((term) => text.includes(term));

  const isThreatCategory =
    category.includes("threat") ||
    category.includes("ransomware") ||
    category.includes("ecrime") ||
    category.includes("offensive") ||
    category.includes("breach") ||
    category.includes("detection") ||
    category.includes("cloud") ||
    category.includes("identity");

  const isCredibleInsightSource = insightSources.some((sourceName) =>
    source.includes(sourceName)
  );

  return (hasBreachSignal || hasThreatSignal) && (isThreatCategory || isCredibleInsightSource);
}

function normalizeText(value) {
  return String(value ?? "")
    .toLowerCase()
    .replace(/https?:\/\/\S+/g, "")
    .replace(/[^a-z0-9\s]/g, " ")
    .replace(/\b(the|a|an|and|or|to|of|in|on|for|with|from|by|at|is|are|was|were|as|this|that|it|its|into|about|after|before|new|how|why|what|will|can|could|should|would|their|there|they|them|your|you|our|out|over|under)\b/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function normalizeForDedupe(value) {
  return String(value ?? "")
    .toLowerCase()
    .replace(/https?:\/\/\S+/g, " ")
    .replace(/\bcve-\d{4}-\d{4,7}\b/g, " CVE_TOKEN ")
    .replace(/\bzero[-\s]?day\b/g, "zero day")
    .replace(/\brce\b/g, "remote code execution")
    .replace(/\biocs?\b/g, "indicator")
    .replace(/\bttps?\b/g, "tactics techniques procedures")
    .replace(/\bmalware campaign\b/g, "campaign")
    .replace(/\bransomware attack\b/g, "ransomware")
    .replace(/\bdata breach\b/g, "breach")
    .replace(/[^a-z0-9\s]/g, " ")
    .replace(/\b(the|a|an|and|or|to|of|in|on|for|with|from|by|at|is|are|was|were|as|this|that|it|its|into|about|after|before|new|how|why|what|will|can|could|should|would|their|there|they|them|your|you|our|out|over|under|says|said|report|reports|reported|researcher|researchers|warn|warns|warning|analysis|blog|post|article|security|cyber|cybersecurity)\b/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function getKeywords(item) {
  const text = normalizeText(`${item.title || ""} ${stripHtml(item.summary || "")}`);

  return text
    .split(" ")
    .filter((word) => word.length > 4)
    .slice(0, 24);
}

function getDedupeTokens(item) {
  const text = normalizeForDedupe(`${item.title || ""} ${stripHtml(item.summary || "")}`);

  return text
    .split(" ")
    .filter((word) => word.length > 3)
    .slice(0, 80);
}

function extractCves(item) {
  const text = `${item.title || ""} ${stripHtml(item.summary || "")}`.toLowerCase();
  return [...new Set(text.match(/\bcve-\d{4}-\d{4,7}\b/g) || [])];
}

function extractNamedSignals(item) {
  const text = `${item.title || ""} ${stripHtml(item.summary || "")}`.toLowerCase();

  const patterns = [
    "ivanti",
    "citrix",
    "fortinet",
    "palo alto",
    "pan-os",
    "sonicwall",
    "sharepoint",
    "exchange",
    "confluence",
    "jira",
    "chrome",
    "firefox",
    "windows",
    "linux",
    "vmware",
    "esxi",
    "microsoft",
    "google",
    "aws",
    "azure",
    "okta",
    "entra",
    "duo",
    "salesforce",
    "github",
    "npm",
    "pypi",
    "docker",
    "kubernetes",
    "north korea",
    "north korean",
    "lazarus",
    "kimsuky",
    "muddywater",
    "sandworm",
    "volt typhoon",
    "lockbit",
    "akira",
    "clop",
    "black basta",
    "ransomhub",
    "scattered spider",
    "shinyhunters",
    "clickfix",
    "vidar",
    "lumma",
    "redline",
    "remcos",
    "qakbot",
    "emotet",
    "cobalt strike",
    "asyncrat",
    "darkgate",
    "amadyey",
    "latrodectus"
  ];

  return patterns.filter((pattern) => text.includes(pattern));
}

function canonicalUrl(url) {
  try {
    const parsed = new URL(url);
    parsed.hash = "";

    const removableParams = [
      "utm_source",
      "utm_medium",
      "utm_campaign",
      "utm_term",
      "utm_content",
      "fbclid",
      "gclid",
      "mc_cid",
      "mc_eid"
    ];

    for (const param of removableParams) {
      parsed.searchParams.delete(param);
    }

    return parsed.toString().replace(/\/$/, "");
  } catch {
    return "";
  }
}

function jaccardSimilarity(a, b) {
  const setA = new Set(a);
  const setB = new Set(b);

  if (!setA.size || !setB.size) {
    return 0;
  }

  let intersection = 0;

  for (const value of setA) {
    if (setB.has(value)) {
      intersection++;
    }
  }

  const union = new Set([...setA, ...setB]).size;
  return intersection / union;
}

function tokenOverlapScore(aTokens, bTokens) {
  const a = new Set(aTokens);
  const b = new Set(bTokens);

  if (!a.size || !b.size) {
    return 0;
  }

  let intersection = 0;

  for (const token of a) {
    if (b.has(token)) {
      intersection++;
    }
  }

  const smaller = Math.min(a.size, b.size);
  return intersection / smaller;
}

function jaccardTokenScore(aTokens, bTokens) {
  const a = new Set(aTokens);
  const b = new Set(bTokens);

  if (!a.size || !b.size) {
    return 0;
  }

  let intersection = 0;

  for (const token of a) {
    if (b.has(token)) {
      intersection++;
    }
  }

  const union = new Set([...a, ...b]).size;
  return intersection / union;
}

function areLikelyDuplicateItems(a, b) {
  const aUrl = canonicalUrl(a.link || a.url || "");
  const bUrl = canonicalUrl(b.link || b.url || "");

  if (aUrl && bUrl && aUrl === bUrl) {
    return true;
  }

  const aTitle = normalizeForDedupe(a.title || "");
  const bTitle = normalizeForDedupe(b.title || "");

  if (aTitle && bTitle && aTitle === bTitle) {
    return true;
  }

  const aCves = extractCves(a);
  const bCves = extractCves(b);
  const sharedCves = aCves.filter((cve) => bCves.includes(cve));

  const aSignals = extractNamedSignals(a);
  const bSignals = extractNamedSignals(b);
  const sharedSignals = aSignals.filter((signal) => bSignals.includes(signal));

  const aTokens = getDedupeTokens(a);
  const bTokens = getDedupeTokens(b);

  const titleSimilarity = jaccardTokenScore(
    getDedupeTokens({ title: a.title || "", summary: "" }),
    getDedupeTokens({ title: b.title || "", summary: "" })
  );

  const fullJaccard = jaccardTokenScore(aTokens, bTokens);
  const overlap = tokenOverlapScore(aTokens, bTokens);

  if (sharedCves.length && (titleSimilarity >= 0.25 || fullJaccard >= 0.22 || overlap >= 0.45)) {
    return true;
  }

  if (sharedSignals.length >= 2 && (titleSimilarity >= 0.32 || fullJaccard >= 0.28 || overlap >= 0.5)) {
    return true;
  }

  if (titleSimilarity >= 0.62) {
    return true;
  }

  if (fullJaccard >= 0.48 || overlap >= 0.72) {
    return true;
  }

  return false;
}

function dedupeItems(items) {
  const sorted = items
    .slice()
    .sort((a, b) => {
      const scoreDiff = scoreItem(b) - scoreItem(a);

      if (scoreDiff !== 0) {
        return scoreDiff;
      }

      return getItemTime(b) - getItemTime(a);
    });

  const selected = [];

  for (const item of sorted) {
    const duplicate = selected.some((existing) => areLikelyDuplicateItems(item, existing));

    if (!duplicate) {
      selected.push(item);
    }
  }

  return selected;
}

function getThemeKey(item) {
  const title = String(item.title || "").toLowerCase();
  const summary = stripHtml(item.summary || "").toLowerCase();
  const source = String(item.source || "").toLowerCase();
  const text = `${title} ${summary} ${source}`;

  const themeRules = [
    {
      key: "ivanti_epmm_exploitation",
      label: "Ivanti EPMM Exploitation",
      patterns: ["ivanti", "epmm", "endpoint manager mobile"]
    },
    {
      key: "palo_alto_pan_os_zero_day",
      label: "Palo Alto / PAN-OS Zero-Day Activity",
      patterns: ["palo alto", "pan-os", "pan os", "cve-2026-0300"]
    },
    {
      key: "pcpjack_cloud_credential_theft",
      label: "PCPJack / Cloud Credential Theft",
      patterns: ["pcpjack", "teampcp", "credential stealer"]
    },
    {
      key: "clickfix_social_engineering",
      label: "ClickFix / Social Engineering Malware Delivery",
      patterns: ["clickfix", "vidar", "fake captcha", "captcha-gated", "captcha gated"]
    },
    {
      key: "ai_agent_framework_rce",
      label: "AI Agent Framework RCE",
      patterns: ["prompts become shells", "ai agent frameworks", "remote code execution", "rce vulnerabilities in ai agent"]
    },
    {
      key: "ai_coding_agent_risk",
      label: "AI Coding Agent Risk",
      patterns: ["claude code", "cursor", "copilot cli", "gemini cli", "ai coding", "coding agent", "trustfall", "cline", "mcp", "oauth tokens"]
    },
    {
      key: "ai_model_security_research",
      label: "AI Model Security Research",
      patterns: ["prompt injection", "model", "llm", "agentic", "vision-language", "vlm", "adversarial", "ai security bug", "ai-generated security"]
    },
    {
      key: "north_korea_it_workers",
      label: "North Korean IT Worker Schemes",
      patterns: ["north korea", "north korean", "laptop farm", "it workers"]
    },
    {
      key: "iran_muddywater_chaos_ransomware",
      label: "Iran / MuddyWater / Chaos Ransomware",
      patterns: ["iranian", "muddywater", "chaos ransomware", "mois"]
    },
    {
      key: "crypto_theft_financial_crime",
      label: "Crypto Theft / Financial Crime",
      patterns: ["crypto", "cryptocurrency", "blockchain", "heist", "laundering", "chainalysis", "wallet"]
    },
    {
      key: "identity_credential_theft",
      label: "Identity / Credential Theft",
      patterns: ["credential", "credentials", "oauth", "token", "password", "service account", "suspicious login"]
    },
    {
      key: "browser_security",
      label: "Browser Security",
      patterns: ["chrome", "firefox", "browser", "extension", "edge", "safari"]
    },
    {
      key: "cloud_security_threats",
      label: "Cloud Security Threats",
      patterns: ["aws", "azure", "google cloud", "cloud", "container", "kubernetes", "saas", "multicloud", "cloud secrets", "cloud credentials"]
    },
    {
      key: "active_exploitation_vulnerabilities",
      label: "Active Exploitation / Vulnerabilities",
      patterns: ["active exploitation", "actively exploited", "zero-day", "0-day", "exploit", "exploitation", "rce", "privilege escalation", "cve", "critical-severity", "high-severity"]
    },
    {
      key: "ransomware_ecrime_malware",
      label: "Ransomware / eCrime / Malware",
      patterns: ["ransomware", "extortion", "botnet", "malware", "stealer", "backdoor", "worm", "loader", "trojan"]
    },
    {
      key: "phishing_social_engineering",
      label: "Phishing / Social Engineering",
      patterns: ["phishing", "social engineering", "qr code", "captcha", "tycoon", "bec", "business email compromise"]
    },
    {
      key: "data_security_dlp",
      label: "Data Security / DLP",
      patterns: ["dlp", "data protection", "data security", "sensitive data", "purview", "copy/paste"]
    },
    {
      key: "reddit_practitioner_chatter",
      label: "Reddit Practitioner Chatter",
      patterns: ["reddit", "r/netsec", "r/cybersecurity", "r/sysadmin", "r/msp", "r/blueteamsec"]
    }
  ];

  const matchedRule = themeRules.find((rule) =>
    rule.patterns.some((pattern) => text.includes(pattern))
  );

  if (matchedRule) {
    return matchedRule;
  }

  return {
    key: "other_recent_threat_signal",
    label: "Other Recent Threat Signal"
  };
}

function getThreatCategory(item) {
  const title = String(item.title || "").toLowerCase();
  const summary = stripHtml(item.summary || "").toLowerCase();
  const category = String(item.category || "").toLowerCase();
  const source = String(item.source || "").toLowerCase();
  const text = `${title} ${summary} ${category} ${source}`;

  const rules = [
    {
      key: "breach_incident",
      label: "Breach / Incident",
      priority: 100,
      patterns: [
        "breach",
        "data breach",
        "data leak",
        "leaked",
        "exposed",
        "stolen",
        "unauthorized access",
        "intrusion",
        "incident",
        "compromised",
        "exfiltration"
      ]
    },
    {
      key: "active_exploitation",
      label: "Active Exploitation",
      priority: 95,
      patterns: [
        "active exploitation",
        "actively exploited",
        "exploited in the wild",
        "in the wild",
        "zero-day",
        "zero day",
        "0-day",
        "weaponized",
        "mass exploitation"
      ]
    },
    {
      key: "vulnerability_exploitability",
      label: "Vulnerability / Exploitability",
      priority: 85,
      patterns: [
        "cve-",
        "rce",
        "remote code execution",
        "privilege escalation",
        "proof-of-concept",
        "poc exploit",
        "exploit",
        "exploitation",
        "critical vulnerability",
        "high-severity vulnerability"
      ]
    },
    {
      key: "ransomware_extortion",
      label: "Ransomware / Extortion",
      priority: 80,
      patterns: [
        "ransomware",
        "extortion",
        "double extortion",
        "encryptor",
        "ransom note",
        "leak site",
        "victim"
      ]
    },
    {
      key: "malware_infrastructure",
      label: "Malware / Infrastructure",
      priority: 75,
      patterns: [
        "malware",
        "backdoor",
        "loader",
        "stealer",
        "infostealer",
        "trojan",
        "botnet",
        "worm",
        "implant",
        "command and control",
        "c2"
      ]
    },
    {
      key: "phishing_social_engineering",
      label: "Phishing / Social Engineering",
      priority: 70,
      patterns: [
        "phishing",
        "social engineering",
        "bec",
        "business email compromise",
        "clickfix",
        "fake captcha",
        "qr code",
        "credential harvesting"
      ]
    },
    {
      key: "identity_cloud_abuse",
      label: "Identity / Cloud Abuse",
      priority: 65,
      patterns: [
        "credential theft",
        "token theft",
        "oauth",
        "session hijacking",
        "cloud credentials",
        "service account",
        "identity provider",
        "idp",
        "sso",
        "mfa bypass",
        "aws",
        "azure",
        "google cloud",
        "kubernetes"
      ]
    },
    {
      key: "apt_geopolitical",
      label: "APT / Geopolitical",
      priority: 60,
      patterns: [
        "apt",
        "state-sponsored",
        "state sponsored",
        "nation-state",
        "nation state",
        "espionage",
        "china-linked",
        "russia-linked",
        "iran-linked",
        "north korea",
        "north korean"
      ]
    },
    {
      key: "ai_security",
      label: "AI Security",
      priority: 55,
      patterns: [
        "prompt injection",
        "llm",
        "agentic",
        "ai agent",
        "model exploitation",
        "model abuse",
        "mcp",
        "coding agent",
        "claude code",
        "copilot cli",
        "cursor",
        "gemini cli"
      ]
    },
    {
      key: "detection_response",
      label: "Detection / Response",
      priority: 45,
      patterns: [
        "detection",
        "hunting",
        "sigma",
        "yara",
        "suricata",
        "incident response",
        "dfir",
        "forensics",
        "telemetry"
      ]
    },
    {
      key: "policy_strategy",
      label: "Policy / Strategy",
      priority: 20,
      patterns: [
        "regulation",
        "policy",
        "law",
        "sanctions",
        "advisory",
        "guidance",
        "framework",
        "strategy"
      ]
    }
  ];

  const matches = rules
    .filter((rule) => rule.patterns.some((pattern) => text.includes(pattern)))
    .sort((a, b) => b.priority - a.priority);

  if (matches.length) {
    return {
      key: matches[0].key,
      label: matches[0].label
    };
  }

  return {
    key: "other_threat_signal",
    label: "Other Threat Signal"
  };
}

function getIndustryTags(item) {
  const title = String(item.title || "").toLowerCase();
  const summary = stripHtml(item.summary || "").toLowerCase();
  const source = String(item.source || "").toLowerCase();
  const category = String(item.category || "").toLowerCase();
  const text = `${title} ${summary} ${source} ${category}`;

  const industryRules = [
    {
      key: "financial_services",
      label: "Financial Services",
      patterns: [
        "bank",
        "banks",
        "banking",
        "credit union",
        "fintech",
        "payment",
        "payments",
        "swift",
        "atm",
        "insurance",
        "brokerage",
        "crypto",
        "cryptocurrency",
        "exchange",
        "wallet",
        "trading",
        "financial"
      ]
    },
    {
      key: "healthcare",
      label: "Healthcare",
      patterns: [
        "hospital",
        "healthcare",
        "health care",
        "clinic",
        "patient",
        "medical",
        "pharma",
        "pharmaceutical",
        "biotech",
        "hipaa",
        "ehr",
        "electronic health record"
      ]
    },
    {
      key: "government_public_sector",
      label: "Government & Public Sector",
      patterns: [
        "government",
        "federal",
        "state agency",
        "municipal",
        "city government",
        "public sector",
        "defense",
        "military",
        "dod",
        "election",
        "embassy",
        "ministry",
        "public administration"
      ]
    },
    {
      key: "education",
      label: "Education",
      patterns: [
        "school",
        "schools",
        "university",
        "universities",
        "college",
        "campus",
        "student",
        "students",
        "k-12",
        "district",
        "education"
      ]
    },
    {
      key: "critical_infrastructure",
      label: "Critical Infrastructure",
      patterns: [
        "critical infrastructure",
        "energy",
        "utility",
        "utilities",
        "electric",
        "power grid",
        "water",
        "wastewater",
        "pipeline",
        "oil",
        "gas",
        "telecom",
        "transportation",
        "rail",
        "airport",
        "aviation",
        "maritime",
        "port"
      ]
    },
    {
      key: "technology_saas",
      label: "Technology & SaaS",
      patterns: [
        "saas",
        "software",
        "developer",
        "developers",
        "github",
        "npm",
        "pypi",
        "open source",
        "cloud",
        "aws",
        "azure",
        "google cloud",
        "kubernetes",
        "container",
        "api",
        "oauth",
        "token",
        "identity provider",
        "idp",
        "msp",
        "managed service provider"
      ]
    },
    {
      key: "retail_ecommerce",
      label: "Retail & eCommerce",
      patterns: [
        "retail",
        "ecommerce",
        "e-commerce",
        "merchant",
        "pos",
        "point of sale",
        "shopping",
        "customer data",
        "payment card",
        "loyalty program"
      ]
    },
    {
      key: "manufacturing_industrial",
      label: "Manufacturing & Industrial",
      patterns: [
        "manufacturing",
        "manufacturer",
        "industrial",
        "factory",
        "plant",
        "ot",
        "ics",
        "scada",
        "plc",
        "supply chain",
        "automotive",
        "aerospace"
      ]
    },
    {
      key: "media_communications",
      label: "Media & Communications",
      patterns: [
        "media",
        "journalist",
        "newsroom",
        "broadcast",
        "telecommunications",
        "telecom",
        "isp",
        "mobile carrier",
        "satellite"
      ]
    },
    {
      key: "legal_professional_services",
      label: "Legal & Professional Services",
      patterns: [
        "law firm",
        "legal",
        "consulting",
        "consultancy",
        "accounting",
        "audit firm",
        "professional services"
      ]
    }
  ];

  const matched = industryRules.filter((rule) =>
    rule.patterns.some((pattern) => text.includes(pattern))
  );

  if (matched.length) {
    return matched.map(({ key, label }) => ({ key, label }));
  }

  return [{ key: "cross_industry", label: "Cross-Industry" }];
}

function groupItemsByIndustry(items) {
  const groups = new Map();

  for (const item of items) {
    const industries = getIndustryTags(item);

    for (const industry of industries) {
      if (!groups.has(industry.key)) {
        groups.set(industry.key, {
          key: industry.key,
          label: industry.label,
          items: []
        });
      }

      groups.get(industry.key).items.push(item);
    }
  }

  return Array.from(groups.values())
    .map((group) => ({
      ...group,
      items: group.items.sort((a, b) => scoreItem(b) - scoreItem(a)),
      newest: Math.max(...group.items.map(getItemTime))
    }))
    .sort((a, b) => {
      if (b.items.length !== a.items.length) {
        return b.items.length - a.items.length;
      }

      return b.newest - a.newest;
    });
}

function groupItemsByThreatCategory(items) {
  const groups = new Map();

  for (const item of items) {
    const threatCategory = getThreatCategory(item);

    if (!groups.has(threatCategory.key)) {
      groups.set(threatCategory.key, {
        key: threatCategory.key,
        label: threatCategory.label,
        items: []
      });
    }

    groups.get(threatCategory.key).items.push(item);
  }

  return Array.from(groups.values())
    .map((group) => ({
      ...group,
      items: group.items.sort((a, b) => scoreItem(b) - scoreItem(a)),
      newest: Math.max(...group.items.map(getItemTime))
    }))
    .sort((a, b) => {
      if (b.items.length !== a.items.length) {
        return b.items.length - a.items.length;
      }

      return b.newest - a.newest;
    });
}

function groupItemsBySourceCohort(items) {
  const groups = new Map();

  for (const item of items) {
    const key = item.category || "uncategorized";
    const label = formatCategory(key);

    if (!groups.has(key)) {
      groups.set(key, {
        key,
        label,
        items: []
      });
    }

    groups.get(key).items.push(item);
  }

  return Array.from(groups.values())
    .map((group) => ({
      ...group,
      items: group.items.sort((a, b) => scoreItem(b) - scoreItem(a)),
      newest: Math.max(...group.items.map(getItemTime))
    }))
    .sort((a, b) => {
      if (b.items.length !== a.items.length) {
        return b.items.length - a.items.length;
      }

      return b.newest - a.newest;
    });
}

function scoreItem(item) {
  const title = String(item.title || "");
  const summary = stripHtml(item.summary || "");
  const category = String(item.category || "").toLowerCase();
  const source = String(item.source || "").toLowerCase();
  const text = `${title} ${summary}`.toLowerCase();

  let score = 0;

  const itemTime = getItemTime(item);

  if (itemTime) {
    const ageHours = (Date.now() - itemTime) / 36e5;

    if (ageHours <= 12) score += 80;
    else if (ageHours <= 24) score += 65;
    else if (ageHours <= 48) score += 45;
    else if (ageHours <= 72) score += 30;
    else if (ageHours <= 168) score += 15;
  }

  if (category.includes("threat")) score += 35;
  if (category.includes("offensive")) score += 28;
  if (category.includes("ransomware") || category.includes("ecrime")) score += 26;
  if (category.includes("detection")) score += 22;
  if (category.includes("cloud") || category.includes("identity")) score += 14;
  if (category.includes("reddit")) score -= 25;

  const highImpactTerms = [
    "breach",
    "data breach",
    "data leak",
    "stolen",
    "compromised",
    "intrusion",
    "incident",
    "unauthorized access",
    "exfiltration",
    "extortion",
    "active exploitation",
    "actively exploited",
    "exploited in the wild",
    "zero-day",
    "0-day",
    "rce",
    "remote code execution",
    "ransomware",
    "malware",
    "stealer",
    "infostealer",
    "backdoor",
    "supply chain attack",
    "campaign",
    "threat actor",
    "apt",
    "state-sponsored",
    "nation-state"
  ];

  for (const term of highImpactTerms) {
    if (text.includes(term)) {
      score += 14;
    }
  }

  const majorTerms = [
    "credential",
    "token",
    "oauth",
    "phishing",
    "mcp",
    "cve",
    "critical",
    "cloud credentials",
    "initial access",
    "persistence",
    "lateral movement",
    "command and control",
    "c2",
    "webshell",
    "implant",
    "iocs",
    "indicators",
    "ttps",
    "detection",
    "hunting"
  ];

  for (const term of majorTerms) {
    if (text.includes(term)) {
      score += 8;
    }
  }

  const prioritySources = [
    "microsoft",
    "google",
    "mandiant",
    "openai",
    "anthropic",
    "cisa",
    "crowdstrike",
    "sentinelone",
    "palo alto",
    "unit 42",
    "red canary",
    "huntress",
    "wiz",
    "bleepingcomputer",
    "the hacker news",
    "securityweek",
    "help net security",
    "the record",
    "cyberscoop",
    "talos",
    "sophos",
    "rapid7",
    "watchtowr",
    "greynoise",
    "cloudflare"
  ];

  for (const vendor of prioritySources) {
    if (source.includes(vendor)) {
      score += 6;
    }
  }

  if (isProductMarketingOrPositioning(item)) {
    score -= 200;
  }

  return score;
}

function selectTopUniqueInsights(items, limit = 10) {
  const candidates = items
    .filter((item) => item.title || item.summary)
    .filter(isThreatIntelRelevant)
    .filter(isBreachOrThreatInsight)
    .filter((item) => !isProductMarketingOrPositioning(item));

  const deduped = dedupeItems(candidates);

  const selected = [];
  const threatCategoryCounts = new Map();
  const themeCounts = new Map();

  for (const item of deduped) {
    const threatCategory = getThreatCategory(item).key;
    const theme = getThemeKey(item).key;

    const threatCategoryCount = threatCategoryCounts.get(threatCategory) || 0;
    const themeCount = themeCounts.get(theme) || 0;

    if (threatCategoryCount >= 3) {
      continue;
    }

    if (themeCount >= 2) {
      continue;
    }

    selected.push(item);
    threatCategoryCounts.set(threatCategory, threatCategoryCount + 1);
    themeCounts.set(theme, themeCount + 1);

    if (selected.length >= limit) {
      break;
    }
  }

  return selected;
}

function renderFilterChip({ label, key, type, count }) {
  return `<button class="filter-chip" type="button" data-filter-type="${escapeHtml(type)}" data-filter-key="${escapeHtml(key)}">${escapeHtml(label)} <span>${escapeHtml(count)}</span></button>`;
}

function buildInsight(item, index) {
  const title = item.title || "Untitled item";
  const summary = stripHtml(item.summary || "");
  const source = item.source || "Unknown source";
  const category = item.category || "uncategorized";
  const link = item.link || item.url || "";
  const published = item.published || "";
  const theme = getThemeKey(item);
  const threatCategory = getThreatCategory(item);
  const industries = getIndustryTags(item);

  const insightText = summary
    ? summary.slice(0, 360)
    : `Relevant threat signal from ${source} in ${formatCategory(category)}.`;

  return `
    <article
      class="insight"
      data-category="${escapeHtml(category)}"
      data-source="${escapeHtml(source)}"
      data-theme="${escapeHtml(theme.key)}"
      data-threat-category="${escapeHtml(threatCategory.key)}"
      data-industries="${escapeHtml(industries.map((industry) => industry.key).join(" "))}"
      data-affinity-themes="${escapeHtml(Array.from(linkToThemes[link] || []).join(" "))}"
    >
      <div class="rank">#${index + 1}</div>
      <div class="insight-body">
        <div class="insight-meta">
          <span>${escapeHtml(threatCategory.label)}</span>
          <span>${escapeHtml(theme.label)}</span>
          <span>${escapeHtml(source)}</span>
          ${published ? `<time datetime="${escapeHtml(published)}">${escapeHtml(formatDate(published))}</time>` : ""}
        </div>
        <div class="tag-row">
          <button class="threat-tag" type="button" data-filter-type="threat" data-filter-key="${escapeHtml(threatCategory.key)}">${escapeHtml(threatCategory.label)}</button>
          ${industries
            .map((industry) => `<button class="industry-tag" type="button" data-filter-type="industry" data-filter-key="${escapeHtml(industry.key)}">${escapeHtml(industry.label)}</button>`)
            .join("")}
        </div>
        <h3>${link ? `<a href="${escapeHtml(link)}" ${externalLinkAttrs()}>${escapeHtml(title)}</a>` : escapeHtml(title)}</h3>
        <p>${escapeHtml(insightText)}</p>
      </div>
    </article>
  `;
}

function renderLineItem(item, index) {
  const title = item.title || "Untitled item";
  const link = item.link || item.url || "";
  const source = item.source || "Unknown source";
  const category = item.category || "uncategorized";
  const author = item.author || "";
  const published = item.published || "";
  const summary = stripHtml(item.summary || "");
  const compactSummary = summary.length > 280 ? `${summary.slice(0, 280)}...` : summary;
  const theme = getThemeKey(item);
  const threatCategory = getThreatCategory(item);
  const industries = getIndustryTags(item);

  return `
    <li
      class="feed-line"
      id="item-${escapeHtml(index)}"
      data-source="${escapeHtml(source)}"
      data-category="${escapeHtml(category)}"
      data-theme="${escapeHtml(theme.key)}"
      data-threat-category="${escapeHtml(threatCategory.key)}"
      data-industries="${escapeHtml(industries.map((industry) => industry.key).join(" "))}"
      data-affinity-themes="${escapeHtml(Array.from(linkToThemes[link] || []).join(" "))}"
      data-published="${escapeHtml(published)}"
      itemscope
      itemtype="https://schema.org/Article"
    >
      <div class="line-main">
        <h4 itemprop="headline">
          ${link ? `<a href="${escapeHtml(link)}" itemprop="url" ${externalLinkAttrs()}>${escapeHtml(title)}</a>` : escapeHtml(title)}
        </h4>
        ${compactSummary ? `<p itemprop="description">${escapeHtml(compactSummary)}</p>` : ""}
        <div class="tag-row">
          <button class="threat-tag" type="button" data-filter-type="threat" data-filter-key="${escapeHtml(threatCategory.key)}">${escapeHtml(threatCategory.label)}</button>
          ${industries
            .map((industry) => `<button class="industry-tag" type="button" data-filter-type="industry" data-filter-key="${escapeHtml(industry.key)}">${escapeHtml(industry.label)}</button>`)
            .join("")}
        </div>
      </div>

      <dl class="line-meta">
        <div>
          <dt>Source</dt>
          <dd itemprop="publisher">${escapeHtml(source)}</dd>
        </div>
        <div>
          <dt>Cohort</dt>
          <dd>${escapeHtml(formatCategory(category))}</dd>
        </div>
        ${author ? `
        <div>
          <dt>Author</dt>
          <dd>${escapeHtml(author)}</dd>
        </div>` : ""}
        <div>
          <dt>Published</dt>
          <dd><time datetime="${escapeHtml(published)}" itemprop="datePublished">${escapeHtml(formatDate(published))}</time></dd>
        </div>
        <div>
          <dt>URL</dt>
          <dd>${link ? `<a href="${escapeHtml(link)}" ${externalLinkAttrs()}>${escapeHtml(domainFromUrl(link) || link)}</a>` : "None"}</dd>
        </div>
      </dl>
    </li>
  `;
}

const allItems = Array.isArray(feed.items) ? feed.items : [];

const languageFilteredItems = allItems.filter(isEnglishEnoughItem);
const dateFilteredItems = languageFilteredItems.filter((item) => isWithinLookbackWindow(item, LOOKBACK_DAYS));

const items = dateFilteredItems
  .filter(isThreatIntelRelevant)
  .sort((a, b) => getItemTime(b) - getItemTime(a));

const cohorts = feed.cohorts || {};
const rawFeedStatus = feed.feed_status || {};
const generatedAt = feed.generated_at || new Date().toISOString();
const affinityGroups = Array.isArray(feed.affinity_groups) ? feed.affinity_groups : [];

const feedStatus = Object.fromEntries(
  Object.entries(rawFeedStatus).filter(([sourceName]) => {
    return !excludedNonEnglishSources.has(sourceName);
  })
);

const okSources = Object.values(feedStatus).filter((source) => source.status === "ok").length;
const totalSources = Object.keys(feedStatus).length;

const parseErrors = Object.entries(feedStatus)
  .filter(([, source]) => source.status && source.status !== "ok")
  .map(([name, source]) => ({ name, ...source }));

const latestItems = items.slice().sort((a, b) => getItemTime(b) - getItemTime(a));
const dedupedLatestItems = dedupeItems(latestItems);
const topInsights = selectTopUniqueInsights(dedupedLatestItems, 10);
const industryGroups = groupItemsByIndustry(dedupedLatestItems);
const threatCategoryGroups = groupItemsByThreatCategory(dedupedLatestItems);
const sourceCohortGroups = groupItemsBySourceCohort(dedupedLatestItems);

const languageFilteredOutCount = allItems.length - languageFilteredItems.length;
const dateFilteredOutCount = languageFilteredItems.length - dateFilteredItems.length;
const ctiFilteredOutCount = dateFilteredItems.length - items.length;
const dedupeFilteredOutCount = items.length - dedupedLatestItems.length;
const totalFilteredOutCount = allItems.length - dedupedLatestItems.length;

const threatCategoryNav = threatCategoryGroups
  .map((threatCategory) =>
    renderFilterChip({
      label: threatCategory.label,
      key: threatCategory.key,
      type: "threat",
      count: threatCategory.items.length
    })
  )
  .join("");

const industryNav = industryGroups
  .map((industry) =>
    renderFilterChip({
      label: industry.label,
      key: industry.key,
      type: "industry",
      count: industry.items.length
    })
  )
  .join("");

const cohortFilterNav = sourceCohortGroups
  .map((cohort) =>
    renderFilterChip({
      label: cohort.label,
      key: cohort.key,
      type: "cohort",
      count: cohort.items.length
    })
  )
  .join("");

const cohortCards = Object.entries(cohorts)
  .map(([key, cohort]) => {
    const count = dedupedLatestItems.filter((item) => item.category === key).length;

    return `
      <button class="cohort-card" type="button" data-filter-type="cohort" data-filter-key="${escapeHtml(key)}">
        <h3>${escapeHtml(formatCategory(key))}</h3>
        <p>${escapeHtml(cohort.description || "")}</p>
        <div class="small-meta">${escapeHtml(cohort.source_count || 0)} configured sources · ${escapeHtml(count)} rendered items</div>
      </button>
    `;
  })
  .join("");

function formatDominantFeatures(dominant, opts = {}) {
  if (!dominant || typeof dominant !== "object") return "";
  const parts = [];
  const axisLabels = {
    actor_attribution: "Actor",
    affected_products: "Product",
    affected_industries: "Industry",
    threat_categories: "Category",
    cve_ids: "CVE",
    attack_techniques: "Technique",
  };
  // Skip CVE row when the theme already names its CVEs via member_cves
  // rollup — avoids redundant display.
  const skipAxes = new Set(opts.skipAxes || []);
  for (const axis of ["actor_attribution", "affected_products", "threat_categories", "affected_industries", "cve_ids", "attack_techniques"]) {
    if (skipAxes.has(axis)) continue;
    const values = dominant[axis];
    if (Array.isArray(values) && values.length) {
      const display = values.slice(0, 3).map((v) => v.replace(/_/g, " ")).join(", ");
      parts.push(`<span class="theme-feature"><strong>${axisLabels[axis]}:</strong> ${escapeHtml(display)}</span>`);
    }
  }
  return parts.join("");
}

function formatThemeRollups(group) {
  // Surface rollup metadata produced by affinity.py's rollup passes:
  //   member_cves  — CVEs folded into this product theme
  //   also_targets — products folded into this actor theme
  // These are the elegance pass: one theme per real story, with the
  // constituent CVEs/targets surfaced as detail rather than as parallel
  // themes that duplicate cluster sets.
  const parts = [];
  const cves = Array.isArray(group.member_cves) ? Array.from(new Set(group.member_cves)).sort() : [];
  const targets = Array.isArray(group.also_targets) ? Array.from(new Set(group.also_targets)).sort() : [];
  if (cves.length) {
    parts.push(`<span class="theme-feature"><strong>CVEs in theme:</strong> ${escapeHtml(cves.join(", "))}</span>`);
  }
  if (targets.length) {
    parts.push(`<span class="theme-feature"><strong>Also targets:</strong> ${escapeHtml(targets.join(", "))}</span>`);
  }
  return parts.join("");
}

// Build a link -> [theme_key, ...] map so feed items can be tagged with
// every theme they belong to. One item can belong to multiple themes
// when actor↔product rollups overlap.
const linkToThemes = {};
for (const group of affinityGroups) {
  const key = group.theme_key || (group.anchor_signal || group.label || "").toLowerCase().replace(/[^a-z0-9._-]+/g, "-").replace(/^-+|-+$/g, "");
  if (!key) continue;
  for (const link of group.links || []) {
    if (!linkToThemes[link]) linkToThemes[link] = new Set();
    linkToThemes[link].add(key);
  }
}

const themeCards = affinityGroups
  .map((group) => {
    const cohesionPct = Math.round((group.cohesion || 0) * 100);
    const hasMemberCves = Array.isArray(group.member_cves) && group.member_cves.length > 0;
    const features = formatDominantFeatures(group.dominant_features, {
      skipAxes: hasMemberCves ? ["cve_ids"] : [],
    });
    const rollups = formatThemeRollups(group);
    const themeKey = group.theme_key || (group.anchor_signal || group.label || "").toLowerCase().replace(/[^a-z0-9._-]+/g, "-").replace(/^-+|-+$/g, "");
    return `
      <button class="theme-card" type="button" data-filter-type="theme" data-filter-key="${escapeHtml(themeKey)}" aria-label="Filter corpus by theme: ${escapeHtml(group.label)}">
        <div class="theme-tag">Detected Theme · ${cohesionPct}% cohesion</div>
        <h3>${escapeHtml(group.label)}</h3>
        <p>
          <span class="theme-count">${escapeHtml(group.article_count)} articles</span> across
          <span class="theme-count">${escapeHtml(group.cluster_count)} stories</span>
        </p>
        ${features ? `<p class="theme-features">${features}</p>` : ""}
        ${rollups ? `<p class="theme-rollups">${rollups}</p>` : ""}
      </button>
    `;
  })
  .join("");

function renderPanelHeader({ tag, title, status }) {
  return `
    <div class="panel-header">
      <div class="panel-header-elbow" aria-hidden="true"></div>
      <div class="panel-header-content">
        <div class="panel-header-tag">${escapeHtml(tag)}</div>
        <h2>${escapeHtml(title)}</h2>
      </div>
      ${status ? `
      <div class="panel-header-status">
        <span class="status-dot" aria-hidden="true"></span>
        <span class="status-label">${escapeHtml(status)}</span>
      </div>` : ""}
    </div>
  `;
}

const activeThemesSection = affinityGroups.length > 0 ? `
    <section class="themes-panel" id="active-themes">
      ${renderPanelHeader({ tag: "Tactical Cluster Analysis", title: "Active Themes", status: `${affinityGroups.length} detected` })}
      <p class="panel-intro">
        Affinity groups detected across the article corpus. Where multiple distinct stories share an actor, product, vulnerability, or threat category, they are surfaced here as a single theme. Cohesion reflects how tightly the constituent stories share taxonomy. Use themes to spot coordinated campaigns, recurring attacker behavior, or sector-targeted activity that the Top 10 list alone can miss.
      </p>
      <div class="themes-grid">
        ${themeCards}
      </div>
    </section>
` : "";

const articleCorpus = `
  <section class="panel" id="article-corpus">
    ${renderPanelHeader({ tag: "Filterable Corpus", title: "Article Corpus", status: `${dedupedLatestItems.length} items` })}
    <p class="panel-intro" id="active-filter-label">
      Showing ${dedupedLatestItems.length} deduplicated CTI items from the last ${LOOKBACK_DAYS} days. Use the filters to assemble views by threat category, industry, or source cohort.
    </p>

    <div class="filter-toolbar" aria-label="Dynamic filters">
      <button class="filter-chip active" type="button" data-filter-type="all" data-filter-key="all">All <span>${dedupedLatestItems.length}</span></button>
      ${threatCategoryNav}
      ${industryNav}
      ${cohortFilterNav}
    </div>

    <ol class="feed-lines dynamic-feed-lines" id="dynamic-feed-lines">
      ${dedupedLatestItems
        .map((item, index) => renderLineItem(item, `deduped-${index}`))
        .join("")}
    </ol>
  </section>
`;

// =========================================================
// SEARCH RESULTS PANEL — hidden by default, populated by JS.
// =========================================================
const searchResultsSection = `
  <section class="search-results-panel" id="search-results" aria-live="polite">
    ${renderPanelHeader({ tag: "Reconnaissance Query", title: "Search Results", status: "Awaiting input" })}
    <p class="panel-intro" id="search-results-summary">
      Enter a term in the search box above to find matches across every item in the feed.
    </p>
    <div class="search-results-list" id="search-results-list"></div>
  </section>
`;

// =========================================================
// ALL FEED ITEMS — compact running list of every item.
// =========================================================
function renderCompactRow(item) {
  const title = item.title || "Untitled item";
  const link = item.link || item.url || "";
  const source = item.source || "Unknown source";
  const published = item.published || "";
  const timestamp = getItemTime(item);
  return `
    <div class="all-feed-row" data-published="${escapeHtml(published)}" data-timestamp="${timestamp}" data-source="${escapeHtml(source)}" data-title="${escapeHtml(title.toLowerCase())}">
      <a class="feed-title" href="${escapeHtml(link)}" ${externalLinkAttrs()} title="${escapeHtml(title)}">${escapeHtml(title)}</a>
      <span class="feed-source">${escapeHtml(source)}</span>
      <time class="feed-date" datetime="${escapeHtml(published)}">${escapeHtml(formatDate(published))}</time>
    </div>
  `;
}

const allFeedItemsSection = `
  <section class="feed-list-panel" id="all-feed-items">
    ${renderPanelHeader({ tag: "Unfiltered Stream", title: "All Feed Items", status: `${dedupedLatestItems.length} entries` })}
    <p class="panel-intro">
      The complete running list of every deduplicated item in the feed. Loaded in newest-first order. Use the toggles to re-sort.
    </p>
    <div class="all-feed-sort" role="toolbar" aria-label="Sort feed items">
      <span class="all-feed-sort-label">Sort:</span>
      <button class="sort-toggle active" type="button" data-sort="date-desc">Newest first</button>
      <button class="sort-toggle" type="button" data-sort="date-asc">Oldest first</button>
      <button class="sort-toggle" type="button" data-sort="source-asc">Source A→Z</button>
      <button class="sort-toggle" type="button" data-sort="source-desc">Source Z→A</button>
      <button class="sort-toggle" type="button" data-sort="title-asc">Title A→Z</button>
    </div>
    <div class="all-feed-table" id="all-feed-table">
      ${dedupedLatestItems.map(renderCompactRow).join("")}
    </div>
  </section>
`;

// =========================================================
// ALL SOURCES — static reference list, grouped by cohort.
// =========================================================
const sourcesByCohort = {};
for (const [sourceName, statusInfo] of Object.entries(feedStatus)) {
  const cohortKey = statusInfo.cohort || "uncategorized";
  if (!sourcesByCohort[cohortKey]) {
    sourcesByCohort[cohortKey] = [];
  }
  sourcesByCohort[cohortKey].push({
    name: sourceName,
    url: statusInfo.url || "",
    status: statusInfo.status || "unknown",
  });
}

// Sort source names within each cohort
for (const cohortKey of Object.keys(sourcesByCohort)) {
  sourcesByCohort[cohortKey].sort((a, b) => a.name.localeCompare(b.name));
}

// Order cohorts using the feed's cohort metadata, falling back to alphabetical
const cohortOrder = Object.keys(cohorts).length
  ? Object.keys(cohorts)
  : Object.keys(sourcesByCohort).sort();

const allSourcesBlocks = cohortOrder
  .filter((cohortKey) => sourcesByCohort[cohortKey] && sourcesByCohort[cohortKey].length)
  .map((cohortKey) => {
    const sources = sourcesByCohort[cohortKey];
    const items = sources
      .map((src) => {
        const statusClass = src.status === "ok" ? "" : "error";
        const display = src.url
          ? `<a href="${escapeHtml(src.url)}" ${externalLinkAttrs()}>${escapeHtml(src.name)}</a>`
          : escapeHtml(src.name);
        return `<li><span class="src-status ${statusClass}" aria-hidden="true"></span>${display}</li>`;
      })
      .join("");
    return `
      <div class="sources-cohort-block">
        <h4>${escapeHtml(formatCategory(cohortKey))}</h4>
        <ul>${items}</ul>
      </div>
    `;
  })
  .join("");

const allSourcesSection = `
  <section class="sources-list-panel" id="all-sources">
    ${renderPanelHeader({ tag: "Source Roster", title: "All Sources", status: `${totalSources} configured` })}
    <p class="panel-intro">
      Every configured source in the PHANTOMSignal feed, grouped by ingestion cohort. Status indicator shows whether the source parsed successfully on the most recent aggregator run.
    </p>
    <div class="sources-list-grid">
      ${allSourcesBlocks}
    </div>
  </section>
`;


const parseErrorBlock = parseErrors.length
  ? `
    <section class="status-panel warning" id="source-health">
      <h2>Source Health and Filter Summary</h2>
      <p>
        These sources did not parse successfully during the last feed build. This section is placed at the bottom so the page reads as a threat insights brief first.
      </p>
      <ul>
        ${parseErrors
          .map((source) => {
            const url = source.url || "";
            return `<li><strong>${escapeHtml(source.name)}</strong>: ${escapeHtml(source.status)}${url ? ` · <a href="${escapeHtml(url)}" ${externalLinkAttrs()}>${escapeHtml(url)}</a>` : ""}</li>`;
          })
          .join("")}
      </ul>

      <h3>Filter Summary</h3>
      <ul>
        <li>${escapeHtml(languageFilteredOutCount)} removed by language/source rules.</li>
        <li>${escapeHtml(dateFilteredOutCount)} removed by date window.</li>
        <li>${escapeHtml(ctiFilteredOutCount)} removed as non-CTI.</li>
        <li>${escapeHtml(dedupeFilteredOutCount)} removed by deduplication.</li>
        <li>${escapeHtml(totalFilteredOutCount)} total items filtered out before rendering.</li>
      </ul>
    </section>
  `
  : `
    <section class="status-panel" id="source-health">
      <h2>Source Health and Filter Summary</h2>
      <p>No parse warnings were reported during the last feed build.</p>

      <h3>Filter Summary</h3>
      <ul>
        <li>${escapeHtml(languageFilteredOutCount)} removed by language/source rules.</li>
        <li>${escapeHtml(dateFilteredOutCount)} removed by date window.</li>
        <li>${escapeHtml(ctiFilteredOutCount)} removed as non-CTI.</li>
        <li>${escapeHtml(dedupeFilteredOutCount)} removed by deduplication.</li>
        <li>${escapeHtml(totalFilteredOutCount)} total items filtered out before rendering.</li>
      </ul>
    </section>
  `;

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "ItemList",
  name: "PHANTOMSignal Feed",
  description:
    "Threat signal. Not threat noise. Curated cyber news and threat insight feed. Items are limited to the last 7 days, filtered for CTI relevance, deduplicated, tagged by likely affected industry and threat category, and dynamically filterable.",
  dateModified: generatedAt,
  numberOfItems: dedupedLatestItems.length,
  itemListElement: dedupedLatestItems.map((item, index) => ({
    "@type": "ListItem",
    position: index + 1,
    item: {
      "@type": "Article",
      headline: item.title || "Untitled item",
      url: item.link || item.url || "",
      datePublished: item.published || "",
      author: item.author || "",
      publisher: item.source || "",
      articleSection: getThreatCategory(item).label,
      description: stripHtml(item.summary || ""),
      keywords: [
        ...getKeywords(item),
        getThreatCategory(item).label,
        ...getIndustryTags(item).map((industry) => industry.label)
      ].join(", ")
    }
  }))
};

const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>PHANTOMSignal Feed</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="PHANTOMSignal: threat signal, not threat noise. Curated English-language Cyber News and Threat Insights feed. Last 7 days only. CTI-relevant items only. Deduplicated and dynamically filterable by threat category, industry, and source cohort.">
  <meta name="robots" content="index, follow">

  <script type="application/ld+json">
${JSON.stringify(jsonLd, null, 2)}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500;700&display=swap" rel="stylesheet">

  <style>
    /* =========================================================
       PHANTOMSignal — Cyberpunk-LCARS Theme
       Operational bridge UI for cyber threat reconnaissance.
       Star Trek bridge structure, cyberpunk midnight palette.
       ========================================================= */

    :root {
      color-scheme: dark;

      /* Base atmosphere */
      --bg-0: #02050d;
      --bg-1: #060d1d;
      --bg-2: #0a1428;
      --bg-3: #0e1c3a;

      /* Panel surfaces */
      --panel: rgba(10, 22, 44, 0.86);
      --panel-2: rgba(14, 28, 56, 0.92);
      --panel-3: rgba(18, 36, 70, 0.88);

      /* Lines and dividers */
      --line: rgba(0, 217, 255, 0.18);
      --line-strong: rgba(0, 217, 255, 0.42);
      --line-soft: rgba(167, 199, 247, 0.12);

      /* Type colors */
      --text: #e8f4ff;
      --text-bright: #ffffff;
      --muted: #8fa6c8;
      --muted-2: #5e7595;

      /* Accent palette */
      --cyan: #00d9ff;
      --cyan-dim: #0099b8;
      --blue: #4d8fff;
      --jade: #3affc4;
      --amber: #ff9050;
      --rose: #ff5cf0;
      --pink: #ff7ec3;
      --lavender: #a78cff;
      --mint: #52ff9e;
      --warning: #ffd060;
      --danger: #ff4d6d;

      /* Section accent colors — each panel gets its operational color */
      --section-top10: var(--amber);
      --section-themes: var(--jade);
      --section-cohorts: var(--lavender);
      --section-corpus: var(--cyan);
      --section-feed: var(--pink);
      --section-sources: var(--mint);
      --section-health: var(--warning);
      --section-search: var(--rose);

      /* Type families */
      --font-display: 'Orbitron', 'JetBrains Mono', sans-serif;
      --font-body: 'IBM Plex Sans', system-ui, sans-serif;
      --font-mono: 'JetBrains Mono', 'Consolas', monospace;

      /* LCARS structural radii */
      --r-elbow-lg: 28px;
      --r-elbow-md: 18px;
      --r-elbow-sm: 8px;
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
      scroll-padding-top: 110px;
    }

    body {
      margin: 0;
      font-family: var(--font-body);
      font-weight: 400;
      color: var(--text);
      line-height: 1.55;
      letter-spacing: 0.005em;
      background:
        radial-gradient(ellipse 80rem 50rem at 12% -10%, rgba(0, 217, 255, 0.10), transparent 60%),
        radial-gradient(ellipse 70rem 40rem at 88% 4%, rgba(167, 140, 255, 0.08), transparent 60%),
        radial-gradient(ellipse 60rem 40rem at 50% 100%, rgba(58, 255, 196, 0.05), transparent 60%),
        linear-gradient(180deg, var(--bg-0), var(--bg-1) 40%, var(--bg-2));
      min-height: 100vh;
      position: relative;
      overflow-x: hidden;
    }

    /* Subtle grid + scanlines for cyberpunk atmosphere */
    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      background-image:
        linear-gradient(rgba(0, 217, 255, 0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 217, 255, 0.025) 1px, transparent 1px);
      background-size: 56px 56px;
      mask-image: radial-gradient(ellipse 100rem 70rem at 50% 30%, black, transparent 90%);
    }

    body::after {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      background: repeating-linear-gradient(
        180deg,
        transparent 0,
        transparent 3px,
        rgba(0, 217, 255, 0.012) 3px,
        rgba(0, 217, 255, 0.012) 4px
      );
    }

    main, .sticky-header { position: relative; z-index: 1; }

    a {
      color: var(--cyan);
      text-decoration: none;
      transition: color 120ms ease, text-shadow 120ms ease;
    }

    a:hover {
      color: var(--text-bright);
      text-shadow: 0 0 12px rgba(0, 217, 255, 0.6);
    }

    code, .mono {
      font-family: var(--font-mono);
      color: var(--cyan);
      font-size: 0.92em;
    }

    button {
      font: inherit;
      cursor: pointer;
    }

    /* =========================================================
       STICKY HEADER — tactical command bar
       ========================================================= */

    .sticky-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      width: 100%;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      background: linear-gradient(180deg, rgba(2, 5, 13, 0.94), rgba(6, 13, 29, 0.88));
      border-bottom: 1px solid var(--line-strong);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.55), 0 1px 0 rgba(0, 217, 255, 0.2) inset;
    }

    .sticky-header-inner {
      display: grid;
      grid-template-columns: auto minmax(180px, 1fr) auto;
      align-items: center;
      gap: 18px;
      padding: 14px max(20px, calc((100vw - 1240px) / 2));
    }

    .sticky-title {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      color: var(--text-bright);
      font-family: var(--font-display);
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-size: 0.95rem;
      text-decoration: none;
      padding: 6px 14px;
      border-radius: var(--r-elbow-sm);
      background: linear-gradient(90deg, rgba(0, 217, 255, 0.16), transparent);
      border-left: 3px solid var(--cyan);
    }

    .sticky-title::before {
      content: "◤";
      color: var(--cyan);
      font-size: 0.85em;
      filter: drop-shadow(0 0 6px rgba(0, 217, 255, 0.7));
    }

    .sticky-title:hover {
      text-shadow: 0 0 12px rgba(0, 217, 255, 0.7);
    }

    /* Search in sticky header */
    .header-search {
      position: relative;
      display: flex;
      align-items: center;
      max-width: 460px;
      width: 100%;
    }

    .header-search::before {
      content: "⌖";
      position: absolute;
      left: 12px;
      color: var(--cyan);
      font-size: 1rem;
      pointer-events: none;
      filter: drop-shadow(0 0 4px rgba(0, 217, 255, 0.6));
    }

    .header-search input {
      width: 100%;
      padding: 9px 38px 9px 36px;
      background: rgba(0, 217, 255, 0.06);
      border: 1px solid var(--line);
      border-radius: var(--r-elbow-sm);
      color: var(--text-bright);
      font-family: var(--font-mono);
      font-size: 0.85rem;
      letter-spacing: 0.04em;
      outline: none;
      transition: border-color 140ms ease, background 140ms ease, box-shadow 140ms ease;
    }

    .header-search input::placeholder {
      color: var(--muted-2);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 0.72rem;
    }

    .header-search input:focus {
      border-color: var(--cyan);
      background: rgba(0, 217, 255, 0.10);
      box-shadow: 0 0 0 3px rgba(0, 217, 255, 0.14), 0 0 24px rgba(0, 217, 255, 0.18);
    }

    .header-search-clear {
      position: absolute;
      right: 6px;
      top: 50%;
      transform: translateY(-50%);
      background: transparent;
      border: none;
      color: var(--muted);
      font-family: var(--font-mono);
      font-size: 0.85rem;
      padding: 4px 8px;
      border-radius: 4px;
      display: none;
    }

    .header-search-clear:hover {
      color: var(--rose);
      background: rgba(255, 92, 240, 0.08);
    }

    .header-search.has-query .header-search-clear {
      display: inline-flex;
    }

    .sticky-actions {
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-end;
      gap: 6px;
    }

    .sticky-actions a {
      color: var(--muted);
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      padding: 6px 11px;
      border-radius: 4px;
      border: 1px solid transparent;
      transition: all 120ms ease;
    }

    .sticky-actions a:hover {
      color: var(--cyan);
      border-color: var(--line);
      background: rgba(0, 217, 255, 0.07);
      text-shadow: none;
    }

    /* =========================================================
       MAIN LAYOUT
       ========================================================= */

    main {
      width: min(1240px, calc(100% - 32px));
      margin: 0 auto;
      padding: 36px 0 80px;
    }

    /* =========================================================
       HERO MASTHEAD
       ========================================================= */

    .hero {
      position: relative;
      border: 1px solid var(--line);
      background:
        linear-gradient(135deg, rgba(14, 28, 56, 0.92), rgba(6, 13, 29, 0.92)),
        radial-gradient(circle at 0% 0%, rgba(0, 217, 255, 0.18), transparent 50%);
      border-radius: var(--r-elbow-lg) 4px var(--r-elbow-lg) 4px;
      padding: 38px 40px 36px;
      box-shadow: 0 32px 80px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(0, 217, 255, 0.06) inset;
      overflow: hidden;
      margin-bottom: 28px;
    }

    .hero::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 6px;
      height: 100%;
      background: linear-gradient(180deg, var(--cyan), var(--blue), transparent);
    }

    .hero::after {
      content: "";
      position: absolute;
      top: 20px;
      right: 24px;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--cyan);
      box-shadow: 0 0 16px var(--cyan);
      animation: pulse 2.4s ease-in-out infinite;
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.5; transform: scale(0.85); }
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      color: var(--cyan);
      font-family: var(--font-mono);
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.22em;
      font-size: 0.72rem;
      margin-bottom: 18px;
      padding: 4px 10px 4px 0;
    }

    .eyebrow::before {
      content: "▮▮▮";
      letter-spacing: -2px;
      color: var(--cyan);
      filter: drop-shadow(0 0 6px rgba(0, 217, 255, 0.5));
    }

    h1 {
      margin: 0;
      font-family: var(--font-display);
      font-weight: 900;
      font-size: clamp(2.6rem, 7vw, 5.6rem);
      letter-spacing: -0.02em;
      line-height: 0.95;
      color: var(--text-bright);
      text-shadow: 0 0 40px rgba(0, 217, 255, 0.25);
      overflow-wrap: anywhere;
      hyphens: none;
    }

    .byline {
      display: inline-flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin: 18px 0 0;
      padding: 6px 12px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--jade);
      background: linear-gradient(90deg, rgba(58, 255, 196, 0.08), rgba(58, 255, 196, 0.0) 80%);
      border-left: 2px solid var(--jade);
      border-radius: 0 4px 4px 0;
      max-width: 100%;
    }

    .byline-tag {
      font-weight: 600;
      letter-spacing: 0.2em;
      color: var(--jade);
      opacity: 0.7;
      padding-right: 8px;
      border-right: 1px solid rgba(58, 255, 196, 0.3);
    }

    .byline-name {
      color: var(--text-bright);
      font-weight: 600;
      letter-spacing: 0.1em;
    }

    .byline-sep {
      opacity: 0.4;
      letter-spacing: 0;
    }

    .byline-link {
      color: var(--jade);
      text-decoration: none;
      transition: color 140ms ease, text-shadow 140ms ease;
    }

    .byline-link:hover {
      color: var(--text-bright);
      text-shadow: 0 0 8px rgba(58, 255, 196, 0.6);
    }

    .byline-arrow {
      display: inline-block;
      transition: transform 140ms ease;
    }

    .byline-link:hover .byline-arrow {
      transform: translate(2px, -2px);
    }

    .subtitle {
      color: var(--muted);
      max-width: 920px;
      font-size: 1.02rem;
      margin: 22px 0 0;
      line-height: 1.6;
    }

    .stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
      margin-top: 32px;
    }

    .stat {
      position: relative;
      border: 1px solid var(--line);
      background: rgba(0, 217, 255, 0.04);
      border-radius: var(--r-elbow-md) 4px var(--r-elbow-md) 4px;
      padding: 18px 18px 18px 22px;
      border-left: 3px solid var(--cyan);
    }

    .stat strong {
      display: block;
      font-family: var(--font-display);
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-bright);
      line-height: 1;
      margin-bottom: 6px;
    }

    .stat span {
      color: var(--muted);
      font-family: var(--font-mono);
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    /* =========================================================
       UTILITY NAV
       ========================================================= */

    .utility-links {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 0 0 30px;
    }

    .button-link {
      border: 1px solid var(--line);
      background: rgba(0, 217, 255, 0.05);
      color: var(--text);
      border-radius: 4px var(--r-elbow-sm) 4px var(--r-elbow-sm);
      padding: 9px 14px;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      transition: all 140ms ease;
    }

    .button-link:hover {
      border-color: var(--cyan);
      background: rgba(0, 217, 255, 0.12);
      color: var(--text-bright);
      text-shadow: none;
      transform: translateY(-1px);
    }

    /* =========================================================
       SECTION PANEL FRAMEWORK — LCARS elbow construction
       ========================================================= */

    .panel,
    .insights-panel,
    .themes-panel,
    .search-results-panel,
    .feed-list-panel,
    .sources-list-panel {
      position: relative;
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: var(--r-elbow-lg) 4px var(--r-elbow-lg) 4px;
      padding: 0 0 26px;
      margin-bottom: 24px;
      overflow: hidden;
    }

    /* LCARS-style elbow header bar — colored block + section label */
    .panel-header {
      display: grid;
      grid-template-columns: 14px 1fr auto;
      gap: 16px;
      align-items: stretch;
      padding: 0 26px 0 0;
      margin-bottom: 18px;
      min-height: 64px;
    }

    .panel-header-elbow {
      background: var(--section-color, var(--cyan));
      border-radius: var(--r-elbow-lg) 0 0 4px;
      position: relative;
    }

    .panel-header-elbow::after {
      content: "";
      position: absolute;
      left: 14px;
      top: 0;
      width: 22px;
      height: 6px;
      background: var(--section-color, var(--cyan));
      border-radius: 0 0 4px 0;
    }

    .panel-header-content {
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 18px 0 14px 8px;
    }

    .panel-header-content h2 {
      margin: 0;
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.4rem;
      letter-spacing: 0.02em;
      color: var(--text-bright);
      line-height: 1.1;
    }

    .panel-header-tag {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      color: var(--section-color, var(--cyan));
      margin-bottom: 6px;
    }

    .panel-header-tag::before {
      content: "◤";
    }

    .panel-header-status {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 0 0 0 24px;
    }

    .panel-header-status .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--section-color, var(--cyan));
      box-shadow: 0 0 10px var(--section-color, var(--cyan));
    }

    .panel-header-status .status-label {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--muted);
    }

    .panel-intro {
      color: var(--muted);
      margin: 0 26px 22px;
      max-width: 920px;
      font-size: 0.96rem;
    }

    /* Section color modifiers */
    #top-insights { --section-color: var(--section-top10); }
    #active-themes { --section-color: var(--section-themes); }
    #source-cohorts { --section-color: var(--section-cohorts); }
    #article-corpus { --section-color: var(--section-corpus); }
    #all-feed-items { --section-color: var(--section-feed); }
    #all-sources { --section-color: var(--section-sources); }
    #source-health { --section-color: var(--section-health); }
    #search-results { --section-color: var(--section-search); }

    /* =========================================================
       SEARCH RESULTS PANEL
       ========================================================= */

    #search-results {
      display: none;
    }

    #search-results.visible {
      display: block;
    }

    .search-empty {
      padding: 22px 26px;
      color: var(--muted);
      font-style: italic;
      font-family: var(--font-mono);
      font-size: 0.88rem;
    }

    .search-results-list {
      padding: 0 26px;
      display: grid;
      gap: 10px;
    }

    .search-result-item {
      border: 1px solid var(--line);
      background: rgba(255, 92, 240, 0.04);
      border-radius: 4px var(--r-elbow-sm) 4px var(--r-elbow-sm);
      padding: 14px 16px;
      border-left: 3px solid var(--rose);
    }

    .search-result-item h4 {
      margin: 0 0 6px;
      font-size: 1rem;
      line-height: 1.32;
    }

    .search-result-item h4 a {
      color: var(--text-bright);
    }

    .search-result-item h4 a:hover {
      color: var(--rose);
    }

    .search-result-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-top: 6px;
    }

    .search-result-meta strong {
      color: var(--rose);
      font-weight: 500;
    }

    .search-snippet {
      color: var(--muted);
      font-size: 0.9rem;
      margin: 4px 0 0;
    }

    .search-snippet mark {
      background: rgba(255, 92, 240, 0.22);
      color: var(--text-bright);
      padding: 0 2px;
      border-radius: 2px;
    }

    /* =========================================================
       TOP 10 INSIGHTS
       ========================================================= */

    .insight-list {
      display: grid;
      gap: 14px;
      padding: 0 26px;
    }

    .insight {
      display: grid;
      grid-template-columns: 64px 1fr;
      gap: 18px;
      border: 1px solid var(--line);
      background: rgba(255, 144, 80, 0.03);
      border-radius: 4px var(--r-elbow-md) 4px var(--r-elbow-md);
      padding: 18px;
      border-left: 3px solid var(--amber);
      transition: border-color 140ms ease, background 140ms ease;
    }

    .insight:hover {
      border-color: rgba(255, 144, 80, 0.5);
      background: rgba(255, 144, 80, 0.06);
    }

    .rank {
      display: grid;
      place-items: center;
      width: 56px;
      height: 56px;
      border-radius: 4px var(--r-elbow-md) 4px var(--r-elbow-md);
      background: rgba(255, 144, 80, 0.12);
      border: 1px solid rgba(255, 144, 80, 0.42);
      color: var(--amber);
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.1rem;
      letter-spacing: 0.02em;
    }

    .insight-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      color: var(--muted);
      font-family: var(--font-mono);
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-bottom: 8px;
    }

    .insight-meta time {
      color: var(--amber);
    }

    .insight h3 {
      margin: 0 0 10px;
      font-size: 1.08rem;
      font-weight: 600;
      line-height: 1.35;
      letter-spacing: -0.005em;
    }

    .insight h3 a {
      color: var(--text-bright);
    }

    .insight h3 a:hover {
      color: var(--amber);
      text-shadow: 0 0 12px rgba(255, 144, 80, 0.5);
    }

    .insight p {
      margin: 0;
      color: #d3def0;
      font-size: 0.96rem;
    }

    /* =========================================================
       THEMES PANEL
       ========================================================= */

    .themes-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
      padding: 0 26px;
    }

    .theme-card {
      border: 1px solid var(--line);
      background: rgba(58, 255, 196, 0.03);
      border-radius: 4px var(--r-elbow-md) 4px var(--r-elbow-md);
      padding: 16px;
      border-left: 3px solid var(--jade);
      /* button-as-card */
      width: 100%;
      text-align: left;
      color: var(--text);
      font: inherit;
      cursor: pointer;
      transition: border-color 140ms ease, background 140ms ease, transform 140ms ease;
    }

    .theme-card:hover,
    .theme-card.active {
      border-color: rgba(58, 255, 196, 0.6);
      background: rgba(58, 255, 196, 0.08);
      transform: translateY(-2px);
    }

    .theme-card.active {
      border-left-width: 4px;
    }

    .theme-card:focus-visible {
      outline: 2px solid var(--jade);
      outline-offset: 2px;
    }

    .theme-card h3 {
      margin: 0 0 8px;
      color: var(--text-bright);
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: -0.005em;
    }

    .theme-card .theme-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-mono);
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--jade);
      margin-bottom: 8px;
    }

    .theme-card .theme-tag::before {
      content: "◆";
    }

    .theme-card p {
      margin: 0;
      color: var(--muted);
      font-size: 0.88rem;
    }

    .theme-card .theme-count {
      color: var(--jade);
      font-family: var(--font-mono);
      font-weight: 500;
    }

    /* =========================================================
       COHORT GRID
       ========================================================= */

    .cohort-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 14px;
      padding: 0 26px;
    }

    .cohort-card {
      display: block;
      text-align: left;
      width: 100%;
      border: 1px solid var(--line);
      background: rgba(167, 140, 255, 0.03);
      border-radius: 4px var(--r-elbow-md) 4px var(--r-elbow-md);
      padding: 16px;
      color: var(--text);
      cursor: pointer;
      border-left: 3px solid var(--lavender);
      transition: border-color 140ms ease, background 140ms ease, transform 140ms ease;
    }

    .cohort-card:hover,
    .cohort-card.active {
      border-color: rgba(167, 140, 255, 0.6);
      background: rgba(167, 140, 255, 0.08);
      transform: translateY(-2px);
    }

    .cohort-card h3 {
      margin: 0 0 8px;
      font-size: 1rem;
      font-weight: 600;
      color: var(--text-bright);
      letter-spacing: -0.005em;
    }

    .cohort-card p {
      margin: 0 0 12px;
      color: var(--muted);
      font-size: 0.9rem;
    }

    .small-meta {
      color: var(--lavender);
      font-family: var(--font-mono);
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    /* =========================================================
       ARTICLE CORPUS — filterable feed lines
       ========================================================= */

    .filter-toolbar {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      padding: 0 26px;
      margin-bottom: 20px;
    }

    .filter-chip,
    .threat-tag,
    .industry-tag {
      border: 1px solid var(--line);
      background: rgba(0, 217, 255, 0.05);
      color: var(--text);
      border-radius: 4px;
      padding: 6px 10px;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      cursor: pointer;
      transition: all 120ms ease;
    }

    .filter-chip:hover,
    .filter-chip.active {
      border-color: var(--cyan);
      background: rgba(0, 217, 255, 0.14);
      color: var(--text-bright);
    }

    .filter-chip.active {
      box-shadow: 0 0 0 1px var(--cyan) inset;
    }

    .filter-chip span {
      color: var(--cyan);
      margin-left: 5px;
      font-weight: 700;
    }

    .filter-chip.active span {
      color: var(--text-bright);
    }

    .threat-tag {
      border-color: rgba(77, 143, 255, 0.32);
      background: rgba(77, 143, 255, 0.08);
      color: #c9dbff;
    }

    .threat-tag:hover {
      border-color: var(--blue);
      background: rgba(77, 143, 255, 0.18);
    }

    .industry-tag {
      border-color: rgba(167, 140, 255, 0.3);
      background: rgba(167, 140, 255, 0.08);
      color: #d8d0ff;
    }

    .industry-tag:hover {
      border-color: var(--lavender);
      background: rgba(167, 140, 255, 0.18);
    }

    .feed-lines {
      list-style: none;
      padding: 0 26px;
      margin: 0;
      display: grid;
      gap: 10px;
    }

    .feed-line {
      border: 1px solid var(--line);
      background: var(--panel-2);
      border-radius: 4px var(--r-elbow-sm) 4px var(--r-elbow-sm);
      padding: 16px 18px;
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(260px, 32%);
      gap: 22px;
      border-left: 3px solid var(--line-strong);
      transition: border-color 140ms ease;
    }

    .feed-line:hover {
      border-left-color: var(--cyan);
    }

    .feed-line[hidden] {
      display: none;
    }

    .feed-line h4 {
      margin: 0 0 6px;
      font-size: 1rem;
      font-weight: 600;
      line-height: 1.35;
      letter-spacing: -0.005em;
    }

    .feed-line h4 a {
      color: var(--text-bright);
    }

    .feed-line h4 a:hover {
      color: var(--cyan);
    }

    .feed-line p {
      margin: 0;
      color: #c5d4ec;
      font-size: 0.92rem;
    }

    .line-meta {
      margin: 0;
      display: grid;
      gap: 6px;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--muted);
      align-content: start;
    }

    .line-meta div {
      display: grid;
      grid-template-columns: 80px minmax(0, 1fr);
      gap: 8px;
    }

    .line-meta dt {
      font-weight: 500;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-size: 0.66rem;
      padding-top: 2px;
    }

    .line-meta dd {
      margin: 0;
      color: #cddbef;
      overflow-wrap: anywhere;
    }

    .line-meta time {
      color: var(--cyan);
    }

    /* =========================================================
       ALL FEED ITEMS — compact running list
       ========================================================= */

    .all-feed-sort {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      padding: 0 26px;
      margin-bottom: 14px;
    }

    .all-feed-sort-label {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--muted);
      margin-right: 4px;
    }

    .sort-toggle {
      border: 1px solid var(--line);
      background: rgba(255, 126, 195, 0.06);
      color: var(--text);
      border-radius: 4px;
      padding: 6px 10px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      cursor: pointer;
      transition: all 120ms ease;
    }

    .sort-toggle:hover {
      border-color: rgba(255, 126, 195, 0.5);
      background: rgba(255, 126, 195, 0.12);
      color: var(--text-bright);
    }

    .sort-toggle.active {
      border-color: var(--pink);
      background: rgba(255, 126, 195, 0.18);
      color: var(--text-bright);
      box-shadow: 0 0 0 1px var(--pink) inset;
    }

    .all-feed-table {
      padding: 0 26px;
      display: grid;
      gap: 4px;
    }

    .all-feed-row {
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(150px, 200px) minmax(140px, 160px);
      gap: 16px;
      align-items: baseline;
      padding: 10px 12px;
      border-bottom: 1px solid var(--line-soft);
      font-size: 0.92rem;
      transition: background 100ms ease;
    }

    .all-feed-row:hover {
      background: rgba(255, 126, 195, 0.05);
    }

    .all-feed-row .feed-title {
      color: var(--text);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .all-feed-row .feed-title:hover {
      color: var(--pink);
      text-shadow: none;
    }

    .all-feed-row .feed-source {
      color: var(--muted);
      font-family: var(--font-mono);
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    .all-feed-row .feed-date {
      color: var(--pink);
      font-family: var(--font-mono);
      font-size: 0.74rem;
      text-align: right;
      letter-spacing: 0.04em;
    }

    /* =========================================================
       ALL SOURCES — static reference list
       ========================================================= */

    .sources-list-grid {
      padding: 0 26px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
    }

    .sources-cohort-block {
      border: 1px solid var(--line);
      background: rgba(82, 255, 158, 0.025);
      border-radius: 4px var(--r-elbow-sm) 4px var(--r-elbow-sm);
      padding: 14px 16px;
      border-left: 3px solid var(--mint);
    }

    .sources-cohort-block h4 {
      margin: 0 0 10px;
      font-family: var(--font-display);
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--mint);
    }

    .sources-cohort-block ul {
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      gap: 5px;
    }

    .sources-cohort-block li {
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 8px;
      align-items: baseline;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--text);
    }

    .sources-cohort-block li .src-status {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--mint);
      box-shadow: 0 0 6px rgba(82, 255, 158, 0.5);
      align-self: center;
    }

    .sources-cohort-block li .src-status.error {
      background: var(--danger);
      box-shadow: 0 0 6px rgba(255, 77, 109, 0.5);
    }

    .sources-cohort-block li a {
      color: var(--text);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .sources-cohort-block li a:hover {
      color: var(--mint);
      text-shadow: none;
    }

    /* =========================================================
       SOURCE HEALTH WARNING PANEL
       ========================================================= */

    .status-panel {
      border: 1px solid rgba(255, 208, 96, 0.42);
      background:
        linear-gradient(135deg, rgba(255, 208, 96, 0.08), rgba(255, 208, 96, 0.02));
      border-radius: var(--r-elbow-lg) 4px var(--r-elbow-lg) 4px;
      padding: 26px 30px;
      margin-top: 42px;
      border-left: 3px solid var(--warning);
    }

    .status-panel h2 {
      margin: 0 0 14px;
      font-family: var(--font-display);
      color: var(--warning);
      letter-spacing: 0.02em;
      font-size: 1.2rem;
    }

    .status-panel h2::before {
      content: "⚠ ";
      color: var(--warning);
    }

    .status-panel h3 {
      margin: 22px 0 10px;
      color: var(--warning);
      font-family: var(--font-display);
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .status-panel p,
    .status-panel li {
      color: #ffe4a8;
    }

    .status-panel ul {
      padding-left: 22px;
    }

    .status-panel code {
      color: var(--warning);
    }

    /* =========================================================
       FOOTER
       ========================================================= */

    footer {
      color: var(--muted-2);
      margin-top: 40px;
      padding: 28px 0 0;
      border-top: 1px solid var(--line);
      font-size: 0.86rem;
      font-family: var(--font-mono);
    }

    footer code {
      color: var(--cyan);
    }

    .footer-credit {
      margin-top: 18px;
      padding-top: 16px;
      border-top: 1px solid var(--line-soft);
      color: var(--muted);
      font-family: var(--font-mono);
      font-size: 0.78rem;
      letter-spacing: 0.04em;
    }

    .footer-credit a {
      color: var(--cyan);
    }

    .footer-credit a:hover {
      color: var(--text-bright);
    }

    /* =========================================================
       RESPONSIVE
       ========================================================= */

    @media (max-width: 980px) {
      .feed-line {
        grid-template-columns: 1fr;
      }

      .insight {
        grid-template-columns: 1fr;
      }

      .all-feed-row {
        grid-template-columns: 1fr auto;
        gap: 6px;
      }

      .all-feed-row .feed-date {
        grid-column: 2;
        grid-row: 1;
        text-align: right;
      }

      .all-feed-row .feed-source {
        grid-column: 1 / -1;
        font-size: 0.74rem;
      }
    }

    @media (max-width: 720px) {
      html {
        scroll-padding-top: 168px;
      }

      .sticky-header-inner {
        grid-template-columns: 1fr;
        gap: 10px;
        padding: 12px 16px;
      }

      .sticky-actions {
        justify-content: flex-start;
      }

      .hero {
        padding: 28px 22px;
      }

      h1 {
        /* Floor must be small enough that "PHANTOMSignal Feed" doesn't
           overflow a ~360px viewport at weight 900. The vw scale takes
           over above that. */
        font-size: clamp(1.6rem, 9vw, 3.4rem);
        line-height: 1.0;
      }

      .byline {
        font-size: 0.66rem;
        padding: 5px 10px;
        gap: 8px;
      }

      .byline-tag {
        padding-right: 6px;
      }

      .panel-header {
        grid-template-columns: 10px 1fr;
        padding: 0 18px 0 0;
        min-height: 56px;
      }

      .panel-header-status {
        display: none;
      }

      .panel-intro,
      .insight-list,
      .themes-grid,
      .cohort-grid,
      .filter-toolbar,
      .feed-lines,
      .all-feed-table,
      .sources-list-grid,
      .search-results-list {
        padding-left: 18px;
        padding-right: 18px;
      }

      .line-meta div {
        grid-template-columns: 1fr;
        gap: 2px;
      }
    }
  </style>
</head>

<body>
  <div class="sticky-header">
    <div class="sticky-header-inner">
      <a href="#top" class="sticky-title">PHANTOMSignal</a>

      <div class="header-search" id="header-search">
        <input
          type="search"
          id="search-input"
          placeholder="Search feed · title · description · tags"
          autocomplete="off"
          spellcheck="false"
          aria-label="Search the PHANTOMSignal feed"
        >
        <button class="header-search-clear" type="button" id="search-clear" aria-label="Clear search">✕</button>
      </div>

      <div class="sticky-actions">
        ${briefExists ? '<a href="./brief/" target="_blank" rel="noopener noreferrer">Brief</a>' : ''}
        <a href="./feed.json" target="_blank" rel="noopener noreferrer">JSON</a>
        <a href="#active-themes">Themes</a>
        <a href="#top-insights">Top 10</a>
        <a href="#source-cohorts">Cohorts</a>
        <a href="#article-corpus">Corpus</a>
        <a href="#all-feed-items">All Items</a>
        <a href="#all-sources">Sources</a>
        <a href="#source-health">Health</a>
      </div>
    </div>
  </div>

  <main id="top">
    <header class="hero">
      <div class="eyebrow">PHANTOMSignal · Threat signal. Not threat noise.</div>
      <h1>PHANTOMSignal Feed</h1>
      <p class="byline">
        <span class="byline-tag">SIG</span>
        <span class="byline-name">Raae Wolfram</span>
        <span class="byline-sep" aria-hidden="true">·</span>
        <a class="byline-link" href="https://www.linkedin.com/in/raaewolfram/" ${externalLinkAttrs()}>Connect on LinkedIn <span class="byline-arrow" aria-hidden="true">↗</span></a>
      </p>
      <p class="subtitle">
        Curated English-language Cyber News and Threat Insights from the last ${LOOKBACK_DAYS} days. Items are filtered for CTI relevance, aggressively deduplicated, tagged by threat category and likely affected industry, and dynamically assembled by filter.
      </p>

      <div class="stats" aria-label="Feed status summary">
        <div class="stat">
          <strong>${escapeHtml(dedupedLatestItems.length)}</strong>
          <span>Deduplicated items · last ${LOOKBACK_DAYS} days</span>
        </div>
        <div class="stat">
          <strong>${escapeHtml(totalSources)}</strong>
          <span>Configured English-language sources</span>
        </div>
        <div class="stat">
          <strong>${escapeHtml(okSources)}</strong>
          <span>Healthy sources</span>
        </div>
      </div>
    </header>

    <nav class="utility-links" aria-label="Feed navigation">
      ${briefExists ? `<a class="button-link" href="./brief/" ${externalLinkAttrs()}>Latest PHANTOMSignal Brief</a>` : ''}
      <a class="button-link" href="./feed.json" ${externalLinkAttrs()}>Raw JSON feed</a>
      <a class="button-link" href="#active-themes">Active Themes</a>
      <a class="button-link" href="#top-insights">Top 10</a>
      <a class="button-link" href="#source-cohorts">Source Cohorts</a>
      <a class="button-link" href="#article-corpus">Article Corpus</a>
      <a class="button-link" href="#all-feed-items">All Feed Items</a>
      <a class="button-link" href="#all-sources">All Sources</a>
      <a class="button-link" href="#source-health">Source Health</a>
    </nav>

    ${searchResultsSection}

    ${activeThemesSection}

    <section class="insights-panel" id="top-insights">
      ${renderPanelHeader({ tag: "Priority Alpha", title: "Top 10 Breaches and Threat Insights", status: `${topInsights.length} surfaced` })}
      <p class="panel-intro">
        These items are selected from the last ${LOOKBACK_DAYS} days only, filtered for breach activity, active exploitation, malware, intrusion activity, vulnerability exploitation, credential theft, ransomware, phishing, or other concrete threat signal. Product announcements, positioning posts, launch content, partnerships, webinars, and generic platform messaging are excluded.
      </p>
      <div class="insight-list">
        ${topInsights.map(buildInsight).join("")}
      </div>
    </section>

    <section class="panel" id="source-cohorts">
      ${renderPanelHeader({ tag: "Ingestion Lanes", title: "Source Cohorts", status: `${Object.keys(cohorts).length} lanes` })}
      <p class="panel-intro">
        Source cohorts describe where the signal came from. Click a tile to assemble the matching deduplicated articles in the Article Corpus below. Cohorts are ingestion lanes, not the article taxonomy.
      </p>
      <div class="cohort-grid">
        ${cohortCards}
      </div>
    </section>

    ${articleCorpus}

    ${allFeedItemsSection}

    ${allSourcesSection}

    ${parseErrorBlock}

    <footer>
      <p>
        This page is generated from <code>docs/feed.json</code>. The rendered HTML is designed for human review,
        search indexing, and M365 Agent Builder knowledge ingestion. The rendered page is English-only, limited to the last ${LOOKBACK_DAYS} days, CTI-filtered, deduplicated, industry-tagged, threat-categorized, and dynamically filterable.
      </p>
      <p>
        Generated at: ${escapeHtml(formatDate(generatedAt))}
      </p>
      <p class="footer-credit">
        Created by Raae Wolfram &middot; <a href="https://www.linkedin.com/in/raaewolfram/" target="_blank" rel="noopener noreferrer">Connect on LinkedIn</a>
      </p>
    </footer>
  </main>

  <script id="phantomsignal-data" type="application/json">
${JSON.stringify(
  dedupedLatestItems.map((item, index) => ({
    id: `deduped-${index}`,
    title: item.title || "",
    summary: stripHtml(item.summary || "").slice(0, 400),
    source: item.source || "",
    link: item.link || item.url || "",
    published: item.published || "",
    threatCategory: getThreatCategory(item).label,
    industries: getIndustryTags(item).map((i) => i.label),
    cohortLabel: formatCategory(item.category || ""),
  }))
)}
  </script>

  <script>
    // -----------------------------------------------------------
    // Filter behavior (existing — preserved)
    // -----------------------------------------------------------
    const filterButtons = Array.from(document.querySelectorAll(".filter-toolbar [data-filter-type][data-filter-key], .cohort-card[data-filter-type][data-filter-key], .theme-card[data-filter-type][data-filter-key], .insight [data-filter-type][data-filter-key], .feed-line [data-filter-type][data-filter-key]"));
    const feedItems = Array.from(document.querySelectorAll("#dynamic-feed-lines .feed-line"));
    const activeFilterLabel = document.getElementById("active-filter-label");

    function labelForButton(button) {
      if (!button) {
        return "All";
      }
      // For theme cards, prefer the h3 inside the card over the full textContent
      const headline = button.querySelector ? button.querySelector("h3") : null;
      if (headline && headline.textContent) {
        return headline.textContent.trim();
      }
      return button.textContent.replace(/\\s+\\d+$/, "").trim();
    }

    function applyFilter(type, key, button) {
      let visibleCount = 0;

      for (const item of feedItems) {
        const itemThreatCategory = item.dataset.threatCategory || "";
        const itemCohort = item.dataset.category || "";
        const itemIndustries = (item.dataset.industries || "").split(" ").filter(Boolean);
        const itemAffinityThemes = (item.dataset.affinityThemes || "").split(" ").filter(Boolean);

        const shouldShow =
          type === "all" ||
          (type === "threat" && itemThreatCategory === key) ||
          (type === "industry" && itemIndustries.includes(key)) ||
          (type === "cohort" && itemCohort === key) ||
          (type === "theme" && itemAffinityThemes.includes(key));

        item.hidden = !shouldShow;

        if (shouldShow) {
          visibleCount++;
        }
      }

      // Update active state on filter-toolbar buttons inside Article Corpus
      const toolbarButtons = document.querySelectorAll(".filter-toolbar .filter-chip");
      for (const candidate of toolbarButtons) {
        candidate.classList.remove("active");
        if (candidate.dataset.filterType === type && candidate.dataset.filterKey === key) {
          candidate.classList.add("active");
        }
      }

      // Update active state on theme cards so the user can see which
      // theme is currently filtering the corpus.
      const themeButtons = document.querySelectorAll(".theme-card[data-filter-type='theme']");
      for (const candidate of themeButtons) {
        candidate.classList.remove("active");
        if (type === "theme" && candidate.dataset.filterKey === key) {
          candidate.classList.add("active");
        }
      }

      if (activeFilterLabel) {
        const label = labelForButton(button);
        activeFilterLabel.textContent =
          type === "all"
            ? "Showing all deduplicated CTI items from the last ${LOOKBACK_DAYS} days."
            : \`Showing \${visibleCount} deduplicated item\${visibleCount === 1 ? "" : "s"} for \${label}.\`;
      }

      const corpus = document.getElementById("article-corpus");
      if (corpus) {
        corpus.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    }

    for (const button of filterButtons) {
      button.addEventListener("click", () => {
        applyFilter(button.dataset.filterType, button.dataset.filterKey, button);
      });
    }

    // -----------------------------------------------------------
    // Search behavior
    // -----------------------------------------------------------
    const searchInput = document.getElementById("search-input");
    const searchClear = document.getElementById("search-clear");
    const headerSearch = document.getElementById("header-search");
    const searchResultsSection = document.getElementById("search-results");
    const searchResultsList = document.getElementById("search-results-list");
    const searchResultsSummary = document.getElementById("search-results-summary");

    let searchData = [];
    try {
      const dataEl = document.getElementById("phantomsignal-data");
      if (dataEl) {
        searchData = JSON.parse(dataEl.textContent);
      }
    } catch (e) {
      console.error("Failed to parse PHANTOMSignal search data", e);
    }

    function escapeHtmlBrowser(value) {
      return String(value || "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }

    function escapeRegex(value) {
      return value.replace(/[.*+?^\${}()|[\\]\\\\]/g, "\\\\$&");
    }

    function highlightMatch(text, query) {
      if (!query) return escapeHtmlBrowser(text);
      const re = new RegExp(escapeRegex(query), "gi");
      return escapeHtmlBrowser(text).replace(re, (m) => \`<mark>\${m}</mark>\`);
    }

    function makeSnippet(text, query, len = 220) {
      if (!text) return "";
      const lower = text.toLowerCase();
      const q = query.toLowerCase();
      const idx = lower.indexOf(q);
      if (idx === -1 || text.length <= len) {
        return text.slice(0, len);
      }
      const start = Math.max(0, idx - 60);
      const end = Math.min(text.length, start + len);
      const snippet = (start > 0 ? "…" : "") + text.slice(start, end) + (end < text.length ? "…" : "");
      return snippet;
    }

    function formatDateBrowser(iso) {
      if (!iso) return "";
      try {
        const d = new Date(iso);
        if (isNaN(d.getTime())) return iso;
        return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
      } catch (e) {
        return iso;
      }
    }

    function runSearch(rawQuery) {
      const query = (rawQuery || "").trim();

      if (!query) {
        searchResultsSection.classList.remove("visible");
        searchResultsList.innerHTML = "";
        searchResultsSummary.textContent = "Enter a term in the search box above to find matches across every item in the feed.";
        headerSearch.classList.remove("has-query");
        return;
      }

      headerSearch.classList.add("has-query");

      const q = query.toLowerCase();
      const matches = searchData.filter((item) => {
        if ((item.title || "").toLowerCase().includes(q)) return true;
        if ((item.summary || "").toLowerCase().includes(q)) return true;
        if ((item.source || "").toLowerCase().includes(q)) return true;
        if ((item.threatCategory || "").toLowerCase().includes(q)) return true;
        if ((item.cohortLabel || "").toLowerCase().includes(q)) return true;
        if ((item.industries || []).some((ind) => ind.toLowerCase().includes(q))) return true;
        return false;
      });

      searchResultsSection.classList.add("visible");

      if (matches.length === 0) {
        searchResultsList.innerHTML = \`<div class="search-empty">No matches for "\${escapeHtmlBrowser(query)}". Try a shorter or more general term.</div>\`;
        searchResultsSummary.textContent = \`No matches for "\${query}".\`;
        return;
      }

      searchResultsSummary.textContent = \`\${matches.length} match\${matches.length === 1 ? "" : "es"} for "\${query}".\`;

      searchResultsList.innerHTML = matches
        .map((item) => {
          const snippet = makeSnippet(item.summary || "", query);
          const tagsLine = [item.threatCategory, item.cohortLabel, item.source].filter(Boolean).join(" · ");
          return \`
            <article class="search-result-item">
              <h4><a href="\${escapeHtmlBrowser(item.link)}" target="_blank" rel="noopener noreferrer">\${highlightMatch(item.title || "Untitled", query)}</a></h4>
              <div class="search-result-meta">
                <span>\${escapeHtmlBrowser(tagsLine)}</span>
                <strong>\${escapeHtmlBrowser(formatDateBrowser(item.published))}</strong>
              </div>
              \${snippet ? \`<p class="search-snippet">\${highlightMatch(snippet, query)}</p>\` : ""}
            </article>
          \`;
        })
        .join("");
    }

    let searchTimer = null;
    if (searchInput) {
      searchInput.addEventListener("input", (e) => {
        clearTimeout(searchTimer);
        searchTimer = setTimeout(() => runSearch(e.target.value), 120);
      });
      searchInput.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
          searchInput.value = "";
          runSearch("");
          searchInput.blur();
        }
      });
    }
    if (searchClear) {
      searchClear.addEventListener("click", () => {
        searchInput.value = "";
        runSearch("");
        searchInput.focus();
      });
    }

    // -----------------------------------------------------------
    // All Feed Items — client-side sorting
    // -----------------------------------------------------------
    const allFeedTable = document.getElementById("all-feed-table");
    const sortToggles = Array.from(document.querySelectorAll(".sort-toggle"));

    function sortAllFeedItems(mode) {
      if (!allFeedTable) return;
      const rows = Array.from(allFeedTable.querySelectorAll(".all-feed-row"));

      const comparators = {
        "date-desc": (a, b) => Number(b.dataset.timestamp || 0) - Number(a.dataset.timestamp || 0),
        "date-asc":  (a, b) => Number(a.dataset.timestamp || 0) - Number(b.dataset.timestamp || 0),
        "source-asc": (a, b) => {
          const sa = (a.dataset.source || "").toLowerCase();
          const sb = (b.dataset.source || "").toLowerCase();
          if (sa < sb) return -1;
          if (sa > sb) return 1;
          // secondary: newest first within same source
          return Number(b.dataset.timestamp || 0) - Number(a.dataset.timestamp || 0);
        },
        "source-desc": (a, b) => {
          const sa = (a.dataset.source || "").toLowerCase();
          const sb = (b.dataset.source || "").toLowerCase();
          if (sa > sb) return -1;
          if (sa < sb) return 1;
          return Number(b.dataset.timestamp || 0) - Number(a.dataset.timestamp || 0);
        },
        "title-asc": (a, b) => {
          const ta = a.dataset.title || "";
          const tb = b.dataset.title || "";
          if (ta < tb) return -1;
          if (ta > tb) return 1;
          return 0;
        },
      };

      const comparator = comparators[mode] || comparators["date-desc"];
      rows.sort(comparator);

      // Re-attach in new order; appendChild moves existing nodes.
      for (const row of rows) {
        allFeedTable.appendChild(row);
      }
    }

    for (const toggle of sortToggles) {
      toggle.addEventListener("click", () => {
        for (const t of sortToggles) t.classList.remove("active");
        toggle.classList.add("active");
        sortAllFeedItems(toggle.dataset.sort);
      });
    }
  </script>
</body>
</html>`;

fs.writeFileSync(outputPath, html);

console.log(`Generated ${outputPath}`);
console.log(`Rendered ${dedupedLatestItems.length} deduplicated CTI items from the last ${LOOKBACK_DAYS} days.`);
console.log(`Selected ${topInsights.length} unique breach/threat insights.`);
console.log(`Mapped items across ${industryGroups.length} industry groupings.`);
console.log(`Mapped items across ${threatCategoryGroups.length} threat categories.`);
console.log(`Mapped items across ${sourceCohortGroups.length} source cohorts.`);
console.log(`Filtered out ${languageFilteredOutCount} items by language/source rules.`);
console.log(`Filtered out ${dateFilteredOutCount} items outside the date window.`);
console.log(`Filtered out ${ctiFilteredOutCount} non-CTI items.`);
console.log(`Removed ${dedupeFilteredOutCount} duplicate or near-duplicate items.`);
console.log(`Detected ${parseErrors.length} source warnings.`);
