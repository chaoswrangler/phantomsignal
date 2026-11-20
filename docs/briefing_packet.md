# PHANTOMSignal Briefing Packet

- Generated: 2026-11-20T02:10:30.457718+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 76
- Total items in window: 354
- Total clusters raw: 173
- Total clusters in packet: 80
- Dropped low score: 93
- Dropped overflow: 0

## Cohort metadata

### threat_research_primary
- Description: Primary vendor and research-team intelligence with strong technical depth.
- Source count: 16
- Weight: 10

### government_authoritative
- Description: Authoritative English-language public-sector sources for advisories, vulnerabilities, standards, and public guidance.
- Source count: 2
- Weight: 9

### offensive_vulnerability_research
- Description: High-signal vulnerability research, offensive security analysis, and exploitability-focused sources.
- Source count: 9
- Weight: 10

### detection_response_operations
- Description: Practitioner-oriented sources focused on detection, response, hunting, MDR, and security operations.
- Source count: 11
- Weight: 8

### cloud_identity_infrastructure
- Description: Cloud, identity, SaaS, and infrastructure security research with emphasis on modern attack surfaces.
- Source count: 9
- Weight: 7

### ai_security_agentic_risk
- Description: AI security, LLM exploitation, model integrity, agentic system risk, and AI governance sources.
- Source count: 7
- Weight: 6

### ransomware_ecrime_financial_crime
- Description: Cybercrime, ransomware, extortion, fraud, and illicit financial ecosystem reporting.
- Source count: 4
- Weight: 7

### cyber_news_breach_reporting
- Description: Cybersecurity news, breach reporting, and industry trend coverage. Useful for awareness, not sufficient alone for technical claims.
- Source count: 8
- Weight: 4

### policy_strategy_geopolitics
- Description: Policy, strategy, cyber norms, geopolitics, national security, and regulatory interpretation.
- Source count: 1
- Weight: 5

### practitioner_analysis
- Description: Independent practitioner, researcher, and analyst voices. Best used for framing, interpretation, and reality checks.
- Source count: 6
- Weight: 5

### reddit_practitioner_osint
- Description: Reddit-based practitioner chatter and operational OSINT. Useful for weak signals, field texture, and reality checks, but never sufficient alone for technical claims.
- Source count: 7
- Weight: 2

## Feed status

- **Unit 42** (threat_research_primary)
  - URL: https://unit42.paloaltonetworks.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: fetch_error
  - Item count: 0
  - In window count: 0
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 3
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 5
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 9
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 0
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 1
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 0
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Active Countermeasures** (detection_response_operations)
  - URL: https://www.activecountermeasures.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 10
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 8
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 2
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 9
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 9
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 3
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 50
  - In window count: 2
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 20
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 19
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 23
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/blueteamsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/blueteamsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/sysadmin** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/sysadmin/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Reddit r/msp** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/msp/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/netsecstudents** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsecstudents/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/AskNetsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/AskNetsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 50
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 28
- **Embrace the Red** (ai_security_agentic_risk)
  - URL: https://embracethered.com/blog/index.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **tl;dr sec** (practitioner_analysis)
  - URL: https://tldrsec.com/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Risky Business News** (practitioner_analysis)
  - URL: https://risky.biz/feeds/risky-business-news/
  - Status: ok
  - Item count: 100
  - In window count: 7
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 4

## Affinity groups (themes)

### AWS vulnerability activity
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 6
- Article count: 12
- Cohesion: 0.312
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: AWS
  - urgency_signals: preauth_unauth
- Cluster IDs: fb549f1298, 5d7989058d, 5ab917fdb9, efdc801eef, dd10fb744d, 717ae538c3
- Links:
  - https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html
  - https://blog.cloudflare.com/nginx2root/
  - https://webflow.sysdig.com/blog/runtime-security-for-amazon-eks-auto-mode
  - https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion
  - https://aws.amazon.com/blogs/security/detecting-cross-cloud-lateral-movement-with-aws-security-hub/
  - https://tldrsec.com/p/tldr-sec-355
  - https://www.infosecurity-magazine.com/news/java4shell-vulnerability-remote/
  - https://trustedsec.com/blog/accuracy-through-volume-of-fire
  - https://aws.amazon.com/blogs/security/how-aws-security-incident-response-triages-your-security-findings/

### Atlassian Confluence exploitation (CVE-2026-114938)
- Anchor signal: Atlassian Confluence
- Theme key: atlassian-confluence
- Cluster count: 4
- Article count: 16
- Cohesion: 0.314
- Shared strong signals: Atlassian Confluence
- Member CVEs: CVE-2026-114938
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Atlassian Confluence, Atlassian Jira
  - cve_ids: CVE-2026-114938
  - urgency_signals: preauth_unauth, actively_exploited
- Cluster IDs: a162d593b3, 7c92294871, 2e72543ef9, efdc801eef
- Links:
  - https://www.rapid7.com/blog/post/etr-rapid7-detected-exploitation-of-cve-2026-90436-against-atlassian-confluence-data-center-n-able-n-central-also-exploited
  - https://www.securityweek.com/critical-apache-roller-axis-vulnerabilities-exploited-in-attacks/
  - https://webflow.sysdig.com/blog/java4shell-cve-2026-114938-pre-auth-rce-in-openjdk
  - https://blog.talosintelligence.com/java4shell/
  - https://www.rapid7.com/blog/post/etr-cve-2026-114938-reported-critical-pre-authentication-remote-code-execution-java-17
  - https://www.sophos.com/en-us/blog/java4shell-could-allow-remote-code-execution
  - https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html
  - https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938/
  - https://blog.cloudflare.com/java4shell-waf-protection/
  - https://www.wiz.io/blog/cve-2026-114938-rce-java4shell-openjdk
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-114938/
  - https://orca.security/resources/research/java4shell-critical-openjdk-base64-decoder-flaw-could-allow-unauthenticated-remote-code-execution/
  - https://www.greynoise.io/blog/global-event-java4shell-cve-2026-114938-live-activity-report
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-132165/
  - https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html
  - https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/
  - https://www.infosecurity-magazine.com/news/java4shell-vulnerability-remote/

### CVE-2026-126714 exploitation activity
- Anchor signal: CVE-2026-126714
- Theme key: cve-2026-126714
- Cluster count: 4
- Article count: 5
- Cohesion: 0.346
- Shared strong signals: CVE-2026-126714
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-126714, CVE-2026-129289, CVE-2026-115560
  - urgency_signals: preauth_unauth
- Cluster IDs: 63382dfd81, 8002a9fab4, e76dca6b32, 0e89231e39
- Links:
  - https://orca.security/resources/research/php-patches-7-critical-flaws-including-session-and-php-fpm-remote-code-execution-cve-2026-115560-cve-2026-129289/
  - https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html
  - https://www.wiz.io/blog/phpaftershell-critical-php-rce-vulnerabilities-cve-2026-126714
  - https://www.bleepingcomputer.com/news/security/php-security-updates-fix-18-flaws-including-critical-rce-bugs/
  - https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html

### supply chain targeting PyPI
- Anchor signal: PyPI
- Theme key: pypi
- Cluster count: 4
- Article count: 12
- Cohesion: 0.353
- Shared strong signals: PyPI
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain
  - affected_industries: critical_infrastructure
  - affected_products: PyPI, Azure
- Cluster IDs: dec648cd5c, e329a9b51c, 31919ab83e, c5a930f76b
- Links:
  - https://securelist.com/operation-shadowcloud-gitdoor/122004/
  - https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/
  - https://www.elastic.co/security-labs/threat-command/we-caught-the-agent-framework-pypi-compromise-six-minutes-after-it-published
  - https://simonwillison.net/2026/Nov/15/datasette/
  - https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html
  - https://orca.security/resources/research/microsoft-agent-framework-pypi-supply-chain-attack-versions-1-26-1-and-1-26-2-steal-cloud-credentials/
  - https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/
  - https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html
  - https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi
  - https://openssf.org/blog/2026/11/17/clearer-security-signals-making-attestations-comprehensible-for-pypi-users/

### Google Cloud active exploitation
- Anchor signal: Google Cloud
- Theme key: google-cloud
- Cluster count: 4
- Article count: 4
- Cohesion: 0.21
- Shared strong signals: Google Cloud
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_industries: financial_services
  - affected_products: Google Cloud, Linux kernel
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: f170b6e701, fb549f1298, ab440398cd, cf875bad92
- Links:
  - https://orca.security/resources/research/cve-2026-119618-critical-apache-http-2-race-condition-enables-unauthenticated-remote-code-execution/
  - https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://cloud.google.com/blog/products/networking/gke-dataplane-v2-in-place-migration/

### CVE-2026-123007 exploitation activity
- Anchor signal: CVE-2026-123007
- Theme key: cve-2026-123007
- Cluster count: 3
- Article count: 11
- Cohesion: 0.273
- Shared strong signals: CVE-2026-123007
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-123007, CVE-2026-123633, CVE-2026-121810, CVE-2026-123634
  - urgency_signals: preauth_unauth
- Cluster IDs: 8f2a86fb37, dff990f28a, 5d7989058d
- Links:
  - https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed
  - https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities
  - https://www.helpnetsecurity.com/2026/11/19/nginx2root-nginx-vulnerabilities/
  - https://orca.security/resources/research/two-critical-nginx-http-2-flaws-could-allow-unauthenticated-remote-code-execution/
  - https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html
  - https://webflow.sysdig.com/blog/nginx2root
  - https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/
  - https://cloud.google.com/blog/products/application-development/lessons-from-building-sashiko-an-agentic-code-review-system/
  - https://openssf.org/podcast/2026/11/18/whats-in-the-soss-podcast-78-s3e30-from-signal-processing-to-open-source-security-sal-kimmich-on-linux-kernel-defense/
  - https://blog.cloudflare.com/nginx2root/

### CVE-2026-123633 exploitation activity
- Anchor signal: CVE-2026-123633
- Theme key: cve-2026-123633
- Cluster count: 3
- Article count: 11
- Cohesion: 0.273
- Shared strong signals: CVE-2026-123633
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-123007, CVE-2026-123633, CVE-2026-121810, CVE-2026-123634
  - urgency_signals: preauth_unauth
- Cluster IDs: 8f2a86fb37, dff990f28a, 5d7989058d
- Links:
  - https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed
  - https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities
  - https://www.helpnetsecurity.com/2026/11/19/nginx2root-nginx-vulnerabilities/
  - https://orca.security/resources/research/two-critical-nginx-http-2-flaws-could-allow-unauthenticated-remote-code-execution/
  - https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html
  - https://webflow.sysdig.com/blog/nginx2root
  - https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/
  - https://cloud.google.com/blog/products/application-development/lessons-from-building-sashiko-an-agentic-code-review-system/
  - https://openssf.org/podcast/2026/11/18/whats-in-the-soss-podcast-78-s3e30-from-signal-processing-to-open-source-security-sal-kimmich-on-linux-kernel-defense/
  - https://blog.cloudflare.com/nginx2root/

### CVE-2026-114924 exploitation activity
- Anchor signal: CVE-2026-114924
- Theme key: cve-2026-114924
- Cluster count: 2
- Article count: 4
- Cohesion: 0.375
- Shared strong signals: CVE-2026-114924
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-114924, CVE-2026-114925
  - urgency_signals: actively_exploited
- Cluster IDs: 2e72543ef9, c30cd1e74e
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-132165/
  - https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html
  - https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-114924-cve-2026-114925/

### CVE-2026-114925 exploitation activity
- Anchor signal: CVE-2026-114925
- Theme key: cve-2026-114925
- Cluster count: 2
- Article count: 4
- Cohesion: 0.375
- Shared strong signals: CVE-2026-114925
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-114924, CVE-2026-114925
  - urgency_signals: actively_exploited
- Cluster IDs: 2e72543ef9, c30cd1e74e
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-132165/
  - https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html
  - https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-114924-cve-2026-114925/

### CVE-2026-115560 exploitation activity
- Anchor signal: CVE-2026-115560
- Theme key: cve-2026-115560
- Cluster count: 3
- Article count: 4
- Cohesion: 0.276
- Shared strong signals: CVE-2026-115560
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-115560, CVE-2026-109619, CVE-2026-126714, CVE-2026-129289, CVE-2026-129474
  - urgency_signals: preauth_unauth
- Cluster IDs: 63382dfd81, e76dca6b32, ead43f4f6d
- Links:
  - https://orca.security/resources/research/php-patches-7-critical-flaws-including-session-and-php-fpm-remote-code-execution-cve-2026-115560-cve-2026-129289/
  - https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html
  - https://www.bleepingcomputer.com/news/security/php-security-updates-fix-18-flaws-including-critical-rce-bugs/
  - https://www.securityweek.com/php-patches-seven-critical-rce-vulnerabilities/

### active exploitation targeting Linux kernel
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 3
- Article count: 6
- Cohesion: 0.2
- Shared strong signals: Linux kernel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Linux kernel, Google Cloud
  - urgency_signals: preauth_unauth
- Cluster IDs: fb549f1298, dff990f28a, cf875bad92
- Links:
  - https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html
  - https://webflow.sysdig.com/blog/nginx2root
  - https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/
  - https://cloud.google.com/blog/products/application-development/lessons-from-building-sashiko-an-agentic-code-review-system/
  - https://openssf.org/podcast/2026/11/18/whats-in-the-soss-podcast-78-s3e30-from-signal-processing-to-open-source-security-sal-kimmich-on-linux-kernel-defense/
  - https://cloud.google.com/blog/products/networking/gke-dataplane-v2-in-place-migration/

### CVE-2026-119618 exploitation activity
- Anchor signal: CVE-2026-119618
- Theme key: cve-2026-119618
- Cluster count: 2
- Article count: 4
- Cohesion: 0.208
- Shared strong signals: CVE-2026-119618
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-119618
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 2e72543ef9, f170b6e701
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-132165/
  - https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html
  - https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/
  - https://orca.security/resources/research/cve-2026-119618-critical-apache-http-2-race-condition-enables-unauthenticated-remote-code-execution/

## Forward signals

### Novelty
- Novel cves: 3
  - CVE-2026-118899 (first seen via Cloudflare Security at 2026-11-20T01:58:29+00:00, cluster 5d7989058d)
  - CVE-2026-129182 (first seen via SecurityWeek at 2026-11-19T15:54:20+00:00, cluster ead43f4f6d)
  - CVE-2026-129481 (first seen via SecurityWeek at 2026-11-19T15:54:20+00:00, cluster ead43f4f6d)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (5)
- **Java4Shell (CVE-2026-114938): Pre-auth RCE in OpenJDK, and the challenge of image and feature bloat**
  - Cluster: 7c92294871
  - Sources in window: 3
  - Window hours: 4.1
  - Cohort count: 5
- **CVE-2026-123890: Critical Authentication Bypass in VMware vCenter**
  - Cluster: 81c7eb6f97
  - Sources in window: 3
  - Window hours: 1.2
  - Cohort count: 4
- **Operation ShadowCloud: cloud service–based backdoors targeting government networks in Asia and Africa. Part 1**
  - Cluster: dec648cd5c
  - Sources in window: 3
  - Window hours: 3.7
  - Cohort count: 4
- **CVE-2026-123007: Critical NGINX HTTP/2 Integer Underflow Leads to RCE (FIXED)**
  - Cluster: 8f2a86fb37
  - Sources in window: 3
  - Window hours: 3.1
  - Cohort count: 3
- **CVE-2026-132165 | Drupal Core Installer Remote Code Execution Vulnerability**
  - Cluster: 2e72543ef9
  - Sources in window: 3
  - Window hours: 4.7
  - Cohort count: 2

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-90436 + Atlassian Confluence (cluster a162d593b3, first observation: True)
- Pair: CVE-2026-123007 + Docker (cluster 8f2a86fb37, first observation: True)
- Pair: CVE-2026-123633 + Docker (cluster 8f2a86fb37, first observation: True)
- Pair: CVE-2026-102764 + VMware (cluster 81c7eb6f97, first observation: True)
- Pair: CVE-2026-123890 + UNC5221 (cluster 81c7eb6f97, first observation: True)
- Pair: CVE-2026-123890 + VMware (cluster 81c7eb6f97, first observation: True)
- Pair: CVE-2026-59309 + UNC5221 (cluster 81c7eb6f97, first observation: True)
- Pair: UNC5221 + VMware (cluster 81c7eb6f97, first observation: True)
- Pair: CVE-2026-114938 + Atlassian Confluence (cluster 7c92294871, first observation: True)
- Pair: CVE-2026-114938 + Atlassian Jira (cluster 7c92294871, first observation: True)
- Pair: CVE-2026-114938 + Cisco (cluster 7c92294871, first observation: True)
- Pair: CVE-2026-114938 + OpenAI/ChatGPT (cluster 7c92294871, first observation: True)
- Pair: CVE-2026-114924 + Drupal (cluster 2e72543ef9, first observation: True)
- Pair: CVE-2026-114925 + Drupal (cluster 2e72543ef9, first observation: True)
- Pair: CVE-2026-114938 + Drupal (cluster 2e72543ef9, first observation: True)

### Drift (5)
- **UNC5221** (cluster 81c7eb6f97)
  - New industries: (none)
  - New products: VMware
  - Prior top industries: critical_infrastructure, financial_services, manufacturing_industrial
  - Prior top products: Citrix, Ivanti, Palo Alto Networks
- **Cl0p** (cluster 6e155d51ef)
  - New industries: (none)
  - New products: Android
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Anthropic/Claude, OpenAI/ChatGPT, SolarWinds
- **LockBit** (cluster 6e155d51ef)
  - New industries: government
  - New products: Android
  - Prior top industries: critical_infrastructure, financial_services, manufacturing_industrial
  - Prior top products: Cisco, GitHub, OpenAI/ChatGPT
- **ShinyHunters** (cluster 6e155d51ef)
  - New industries: (none)
  - New products: Android
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Anthropic/Claude, OpenAI/ChatGPT, Salesforce
- **Scattered Spider** (cluster 93f35981b4)
  - New industries: manufacturing_industrial
  - New products: GitHub, GitLab
  - Prior top industries: government, healthcare, legal_professional
  - Prior top products: Apple iOS/macOS, Microsoft Defender, Snowflake

### Persistence (11)
- actor_attribution: Cl0p (weeks observed: 13, cluster 6e155d51ef)
- actor_attribution: ShinyHunters (weeks observed: 13, cluster 6e155d51ef)
- actor_attribution: UNC5221 (weeks observed: 10, cluster 81c7eb6f97)
- actor_attribution: Scattered Spider (weeks observed: 10, cluster 93f35981b4)
- actor_attribution: LockBit (weeks observed: 8, cluster 6e155d51ef)
- cve_ids: CVE-2026-109618 (weeks observed: 5, cluster 63382dfd81)
- cve_ids: CVE-2026-109619 (weeks observed: 5, cluster 63382dfd81)
- cve_ids: CVE-2026-102764 (weeks observed: 4, cluster 81c7eb6f97)
- cve_ids: CVE-2026-84869 (weeks observed: 4, cluster 865bc835a9)
- cve_ids: CVE-2026-119618 (weeks observed: 3, cluster 2e72543ef9)
- cve_ids: CVE-2026-115560 (weeks observed: 3, cluster 63382dfd81)

### Tier inversion (0)

## Clusters

### Cluster a162d593b3 — score 68

- Title: Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-16T18:14:14+00:00
- Link: https://www.rapid7.com/blog/post/etr-rapid7-detected-exploitation-of-cve-2026-90436-against-atlassian-confluence-data-center-n-able-n-central-also-exploited
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Atlassian Confluence, CVE-2026-90436

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Atlassian Confluence
- cve_ids: CVE-2026-90436
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: Atlassian Confluence
- cve_ids: CVE-2026-90436
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On November 6, 2026, the Apache Software Foundation disclosed CVE-2026-90436 , a critical unsafe reflection vulnerability ( CWE-470 ) in Axis 1.x that allows for unauthenticated remote code execution (RCE). Apache Axis is a Simple Object Access Protocol (SOAP) implementation used for the creation of Java Web services. CISA has assigned CVE-2026-90436 a CVSS score of 9.8 Critical . Since the initial November 6 disclosure, it has transpired that some versions of Atlassian Confluence Data Center and N-able N-central use the affected Axis library and are vulnerable to CVE-2026-90436. Both products require a non-default configuration in order to be vulnerable. CVE-2026-90436 is now being actively exploited in the wild against both known affected products. On November 13, 2026, Rapid7 MDR detected exploitation of CVE-2026-90436 against Atlassian Confluence Data Center in a customer environment. Separately, on November 13, 2026, N-able reported exploitation in the wild against N-cent
```

#### Full body

```
Emergent Threat Response Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited Rapid7 Nov 16, 2026 | Last updated on Nov 19, 2026 | 6 min read Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited Table of contents Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited Table of contents Overview On November 6, 2026, the Apache Software Foundation disclosed CVE-2026-90436 , a critical unsafe reflection vulnerability ( CWE-470 ) in Axis 1.x that allows for unauthenticated remote code execution (RCE). Apache Axis is a Simple Object Access Protocol (SOAP) implementation used for the creation of Java Web services. CISA has assigned CVE-2026-90436 a CVSS score of 9.8 Critical . Since the initial November 6 disclosure, it has transpired that some versions of Atlassian Confluence Data Center and N-able N-central use the affected Axis library and are vulnerable to CVE-2026-90436. Both products require a non-default configuration in order to be vulnerable. CVE-2026-90436 is now being actively exploited in the wild against both known affected products. On November 13, 2026, Rapid7 MDR detected exploitation of CVE-2026-90436 against Atlassian Confluence Data Center in a customer environment. Separately, on November 13, 2026, N-able reported exploitation in the wild against N-central for a vulnerability that strongly correlates to CVE-2026-90436. A proof-of-concept exploit that leverages CVE-2026-90436 and targets N-central was published on November 12, 2026, as part of a series of public zero-day disclosures against N-central. On November 17, 2026, a Metasploit exploit module was released. The module exploits CVE-2026-90436 to achieve unauthenticated remote code execution against vulnerable Atlassian Confluence Data Center instances when “Remote API (XML-RPC & SOAP)” is enabled. On November 18, 2026, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2026-90436 to its Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation. Rapid7 recommends remediating exposed systems on an emergency basis outside of normal patching cycles. MDR observed exploitation On November 13, 2026, Rapid7's MDR team responded to a surge of alerts firing on the abnormal child processes launched by an Atlassian Confluence server. A review of the Confluence access logs revealed unauthenticated POST requests to /plugins/servlet/soap-axis1/confluenceservice-v2 , each returning an HTTP 500 (Internal Server Error). Despite the error responses, endpoint telemetry showed Confluence's Java process launching Bash and curl as the dedicated confluence service account, within seconds of these requests. The attacker proceeded to run hundreds of hex-encoded shell commands and scripts fetched from temporary Pinggy and Cloudflare Tunnel domains. Each command wrapped its output in labeled delimiters, and carried sequential task IDs, a structure that suggests the use of AI-assisted automated tooling. From this foothold, the attacker enumerated the host, network, Confluence configuration, encryption keys, and database settings. Just over three minutes after the first observed execution, the attackers were authenticating to MySQL with Confluence's own database credentials, querying page bodies, application links, and attachments with names associated with credentials, tokens, VPN configurations, and private keys. The attacker's scripts, likely AI-generated, then targeted files in Confluence's default location for uploaded page attachments ( /var/atlassian/application-data/confluence/attachments/v4/ ), parsed Office documents, searched for credentials, and hunted for payment card numbers, using Luhn checks to filter out false positives. The attacker continued extensive enumeration, mapping various internal services. They used a Confluen
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited
  - Published: 2026-11-16T18:14:14+00:00
  - Link: https://www.rapid7.com/blog/post/etr-rapid7-detected-exploitation-of-cve-2026-90436-against-atlassian-confluence-data-center-n-able-n-central-also-exploited
  - Summary: Overview On November 6, 2026, the Apache Software Foundation disclosed CVE-2026-90436 , a critical unsafe reflection vulnerability ( CWE-470 ) in Axis 1.x that allows for unauthenticated remote code execution (RCE). Apache Axis is a Simple Object Access Protocol (SOAP) implementation used for the creation of Java Web services. CISA has assigned CVE-2026-90436 a CVSS score of 9.8 Critical . Since the initial November 6 disclosure, it has transpired that some versions of Atlassian Confluence Data Center and N-able N-central use the affected Axis library and are vulnerable to CVE-2026-90436. Both products require a non-default configuration in order to be vulnerable. CVE-2026-90436 is now being actively exploited in the wild against both known affected products. On November 13, 2026, Rapid7 MDR detected exploitation of CVE-2026-90436 against Atlassian Confluence Data Center in a customer environment. Separately, on November 13, 2026, N-able reported exploitation in the wild against N-cent
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks
  - Published: 2026-11-19T12:13:24+00:00
  - Link: https://www.securityweek.com/critical-apache-roller-axis-vulnerabilities-exploited-in-attacks/
  - Summary: Attackers are targeting Confluence Data Center through an Axis flaw and Apache is warning of attacks against Roller. The post Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks appeared first on SecurityWeek .

### Cluster 8f2a86fb37 — score 48

- Title: CVE-2026-123007: Critical NGINX HTTP/2 Integer Underflow Leads to RCE (FIXED)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-18T13:56:42+00:00
- Link: https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: CVE-2026-123007, Docker

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- affected_products: Docker
- cve_ids: CVE-2026-123007, CVE-2026-123633
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- affected_products: Docker
- cve_ids: CVE-2026-123007
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview Today, both Rapid7 and F5 are disclosing CVE-2026-123007 , a critical integer underflow vulnerability affecting nginx HTTP/2, which can allow for unauthenticated remote code execution (RCE) against affected servers under certain conditions. CVE ID Description CWE CVSSv4 CVE-2026-123007 HTTP/2 flow-control memory corruption permitting worker-context RCE CWE-191 (Integer Underflow) 9.2 (Critical) nginx can miscalculate how much response data an HTTP/2 client has allowed it to send. A remote, unauthenticated client can exploit this error by cancelling queued response data, then make nginx use an invalid length when copying a later response. The resulting memory corruption can disclose data, interrupt service, and execute code with the nginx worker process's permissions. Impact Rapid7 has developed a proof-of-concept to demonstrate leveraging CVE-2026-123007 for unauthenticated RCE against a vulnerable linux/amd64 Docker image running nginx version 1.31.8 , as shown below in Figur
```

#### Full body

```
Rapid7 Intelligence CVE-2026-123007: Critical NGINX HTTP/2 Integer Underflow Leads to RCE (FIXED) Stephen Fewer Nov 18, 2026 | Last updated on Nov 18, 2026 | 19 min read DISCOVER RAPID7 MDR CVE-2026-123007: Critical NGINX HTTP/2 Integer Underflow Leads to RCE (FIXED) Table of contents CVE-2026-123007: Critical NGINX HTTP/2 Integer Underflow Leads to RCE (FIXED) DISCOVER RAPID7 MDR Table of contents Overview Today, both Rapid7 and F5 are disclosing CVE-2026-123007 , a critical integer underflow vulnerability affecting nginx HTTP/2, which can allow for unauthenticated remote code execution (RCE) against affected servers under certain conditions. CVE ID Description CWE CVSSv4 CVE-2026-123007 HTTP/2 flow-control memory corruption permitting worker-context RCE CWE-191 (Integer Underflow) 9.2 (Critical) nginx can miscalculate how much response data an HTTP/2 client has allowed it to send. A remote, unauthenticated client can exploit this error by cancelling queued response data, then make nginx use an invalid length when copying a later response. The resulting memory corruption can disclose data, interrupt service, and execute code with the nginx worker process's permissions. Impact Rapid7 has developed a proof-of-concept to demonstrate leveraging CVE-2026-123007 for unauthenticated RCE against a vulnerable linux/amd64 Docker image running nginx version 1.31.8 , as shown below in Figure 1. The target nginx server’s configuration had http2 on and TLS enabled. Note that for brevity, video playback is at 8x speed. Figure 1: Video demonstrating unauthenticated RCE against NGINX 1.31.8 via CVE-2026-123007 Leveraging CVE-2026-123007 for RCE requires a significant amount of network traffic to be transmitted, approximately 128 GB of HTTP/2 data. Both available network bandwidth and connection timeouts will place practical limitations on Internet exploitation. In the above example shown in Figure 1, exploitation takes two and a half minutes. The approximate timings to transmit the required network data over a 10 Gbit/s network is two minutes, while on a 1 Gbit/s network it is seventeen minutes. Due to nginx’s default one hour connection lifetime, a network slower than approximately 300 Mbit/s will take over the one hour connection limit threshold and will not be able to succeed. Additionally, should an HTTP/2 connection be proxied, the precise attacker-controlled HTTP/2 frames being transmitted will likely not be retransmitted in a way that satisfies exploiting the vulnerability. Finally, the exploitation strategy developed depends on a specific x86-64 glibc EVEX/YMM memcpy implementation selected at runtime, based on the avx512f and avx512vl CPU features. Alternative RCE exploitation strategies may be viable, but none are currently known. Credit This vulnerability was discovered by Stephen Fewer, Senior Principal Security Researcher at Rapid7 , and is being disclosed in accordance with Rapid7's vulnerability disclosure policy . Technical analysis The version of nginx tested was a linux/amd64 Docker image for nginx version 1.31.8 ( nginx@sha256:5ab5b0b01097420873a3f3330f44248e34a3c2a3e8d5ee30658aeae8cb7435da ), and ran with an exposed HTTPS service and http2 enabled. How a client controls HTTP/2 response data HTTP/2 carries messages called frames over a connection. Each request and response belongs to a numbered stream, so one connection can carry several exchanges at once. Response-body bytes are carried in DATA frames. For this vulnerability, nginx is the sender and the remote client is the receiver. The client grants nginx permission, or flow-control credit, to send a certain number of DATA bytes. nginx tracks the remaining credit in two counters: one for each stream and one shared by the connection. Sending DATA must be permitted by both counters. These HTTP/2 counters are separate from TCP's receive window. The client grants more credit by sending a WINDOW_UPDATE frame containing a positive increment. A stream identifier of zero increas
```

#### Corroborating sources (5)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-123007: Critical NGINX HTTP/2 Integer Underflow Leads to RCE (FIXED)
  - Published: 2026-11-18T13:56:42+00:00
  - Link: https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed
  - Summary: Overview Today, both Rapid7 and F5 are disclosing CVE-2026-123007 , a critical integer underflow vulnerability affecting nginx HTTP/2, which can allow for unauthenticated remote code execution (RCE) against affected servers under certain conditions. CVE ID Description CWE CVSSv4 CVE-2026-123007 HTTP/2 flow-control memory corruption permitting worker-context RCE CWE-191 (Integer Underflow) 9.2 (Critical) nginx can miscalculate how much response data an HTTP/2 client has allowed it to send. A remote, unauthenticated client can exploit this error by cancelling queued response data, then make nginx use an invalid length when copying a later response. The resulting memory corruption can disclose data, interrupt service, and execute code with the nginx worker process's permissions. Impact Rapid7 has developed a proof-of-concept to demonstrate leveraging CVE-2026-123007 for unauthenticated RCE against a vulnerable linux/amd64 Docker image running nginx version 1.31.8 , as shown below in Figur
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Unauthenticated Remote Code Execution in NGINX: CVE-2026-123633 and CVE-2026-123007
  - Published: 2026-11-18T15:13:20+00:00
  - Link: https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities
  - Summary: Two critical HTTP/2 flaws can allow attackers to compromise NGINX servers, putting the websites, APIs, and sensitive data they handle at risk.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: NGINX2Root: F5 patches five critical NGINX vulnerabilities
  - Published: 2026-11-19T18:25:50+00:00
  - Link: https://www.helpnetsecurity.com/2026/11/19/nginx2root-nginx-vulnerabilities/
  - Summary: F5 has patched five critical vulnerabilities in NGINX, the world’s most widely used open-source web server, that can allow remote code execution under certain conditions. Dubbed “NGINX2Root” by Xint researchers, two of the bunch (CVE-2026-123633 and CVE-2026-123007) were also independently unearthed and reported by Rapid7, Wiz, Ikotas Labs, Palo Alto Networks and Metnir researchers. There’s no evidence that any of them has been exploited in the wild, and none were on CISA’s Known Exploited Vulnerabilities … More → The post NGINX2Root: F5 patches five critical NGINX vulnerabilities appeared first on Help Net Security .
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Two Critical NGINX HTTP/2 Flaws Could Allow Unauthenticated Remote Code Execution
  - Published: 2026-11-18T17:05:26+00:00
  - Link: https://orca.security/resources/research/two-critical-nginx-http-2-flaws-could-allow-unauthenticated-remote-code-execution/
  - Summary: F5 has disclosed two critical vulnerabilities in NGINX, CVE-2026-123633 and CVE-2026-123007, both in the HTTP/2 module (ngx_http_v2_module). Both are rated 9.2 under CVSS 4.0 (8.1 under CVSS 3.1) and can be triggered remotely without authentication on NGINX servers with HTTP/2 enabled. Successful exploitation can crash NGINX worker processes, corrupt memory and potentially lead to remote […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: 10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on Servers
  - Published: 2026-11-18T18:31:17+00:00
  - Link: https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html
  - Summary: A flaw in NGINX's HTTP/2 support can allow an attacker to run code on servers with HTTP/2 enabled, without needing to log in. The decade-old flaw, CVE-2026-123007, dubbed "nginx2root," has been present in NGINX's open-source code since version 1.9.5, released on September 22, 2015. Fixed versions 1.31.9 and 1.30.7 came out today. F5, the company behind NGINX, says attackers can run code where

### Cluster 81c7eb6f97 — score 45

- Title: CVE-2026-123890: Critical Authentication Bypass in VMware vCenter
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-19T21:06:24+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-123890-critical-authentication-bypass-vmware-vcenter
- Fetch status: ok
- Member count: 7
- Corroborating source count: 6
- Strong signals: CVE-2026-123890, CVE-2026-59309, VMware

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, zero_day
- actor_attribution: UNC5221
- affected_industries: manufacturing_industrial
- affected_products: VMware
- cve_ids: CVE-2026-102764, CVE-2026-123890, CVE-2026-59309
- urgency_signals: critical_cvss, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: VMware
- cve_ids: CVE-2026-123890, CVE-2026-59309
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On November 19, 2026, Broadcom published VMware Security Advisory VMSA-2026-0009 , addressing five vulnerabilities in VMware products. The most severe of these, CVE-2026-123890 , is an authentication bypass using an alternate path or channel ( CWE-288 ) in the VMware Directory Service component of vCenter. Broadcom assigned the vulnerability a critical CVSSv3 score of 9.8 . A malicious actor with network access to an affected vCenter deployment may exploit CVE-2026-123890 without credentials to bypass authentication and gain unauthorized access to the system as the Administrator user. Mandiant privately reported the issue to Broadcom. Also, Mandiant/Google Threat Intelligence confirmed in-the-wild exploitation of CVE-2026-123890 by Chinese state-linked threat actor ARMORY CASTLE as early as September 2026. CVE-2026-123890 is distinct from the vCenter authentication bypass vulnerability CVE-2026-59309 that Broadcom addressed earlier in 2026. The vendor FAQ states that all vCent
```

#### Full body

```
Emergent Threat Response CVE-2026-123890: Critical Authentication Bypass in VMware vCenter Rapid7 Nov 19, 2026 | Last updated on Nov 19, 2026 | 3 min read CVE-2026-123890: Critical Authentication Bypass in VMware vCenter Table of contents CVE-2026-123890: Critical Authentication Bypass in VMware vCenter Table of contents Overview On November 19, 2026, Broadcom published VMware Security Advisory VMSA-2026-0009 , addressing five vulnerabilities in VMware products. The most severe of these, CVE-2026-123890 , is an authentication bypass using an alternate path or channel ( CWE-288 ) in the VMware Directory Service component of vCenter. Broadcom assigned the vulnerability a critical CVSSv3 score of 9.8 . A malicious actor with network access to an affected vCenter deployment may exploit CVE-2026-123890 without credentials to bypass authentication and gain unauthorized access to the system as the Administrator user. Mandiant privately reported the issue to Broadcom. Also, Mandiant/Google Threat Intelligence confirmed in-the-wild exploitation of CVE-2026-123890 by Chinese state-linked threat actor ARMORY CASTLE as early as September 2026. CVE-2026-123890 is distinct from the vCenter authentication bypass vulnerability CVE-2026-59309 that Broadcom addressed earlier in 2026. The vendor FAQ states that all vCenter systems below the versions fixed by VMSA-2026-0009 require the new update, including systems that already received the earlier fix. Broadcom characterizes the vCenter update as an emergency change requiring prompt action. Mitigation guidance Vendor-provided updates are available for CVE-2026-123890. Broadcom lists no workaround, and the patches cannot be applied using vCenter Quick Patch. Organizations should prioritize upgrading vCenter on an emergency basis, outside of normal patch cycles, using the standard update mechanism for their deployment. VMware Product Affected Version Fixed Version / Patch VMware Cloud Foundation / vSphere Foundation 9.1.x.x 9.1.1.0200 VMware Cloud Foundation / vSphere Foundation 9.0.x.x 9.0.2.0200 VMware vCenter Server 8.0 8.0 U3m VMware vCenter Server 7.0 Contact Broadcom Support (extended-support customers) VMware Cloud Foundation 5.x 5.2.5 VMware Telco Cloud Platform 3.0, 4.x, 5.0.x, 5.1.x, 5.2 8.0 U3m — KB463116 VMware Telco Cloud Infrastructure 3.0 8.0 U3m — KB463116 The fixes are cumulative. The vCenter 8.0 U3m and 9.0.2.0200 updates introduce a “Back-in-Time” restriction that blocks upgrades to VMware Cloud Foundation 9.1.1 ; Broadcom advises customers in an active upgrade to review the vendor FAQ and interoperability matrix. Updating vCenter temporarily makes its management interfaces unavailable, but Broadcom states that running virtual machine and container workloads continue to operate. For the latest affected-version and mitigation guidance, please refer to Broadcom's security advisory and supplemental FAQ . Rapid7 customers Exposure Command, Vulnerability Management, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-123890 on VMware vCenter Server with an unauthenticated vulnerability check expected to be available in the Nov 20, 2026 content release. Updates November 19, 2026 : Initial publication. Article tags Emergent Threat Response Explore more from Rapid7 Vulnerability & Exploit Database Rapid7s curated database of vulnerabilities, featuring exploit modules and check methods integrated into the Metasploit Framework. Search the database Rapid7 Intelligence The threat research behind the alerts: adversary tracking, curated intelligence, and flagship threat reports. Explore the research Rapid7 MDR Gain 24x7 XDR monitoring, remediation, and DFIR from experts that extend your team to help secure your extended ecosystem. Explore MDR Exposure management Get continuous assessment of your attack surface with the critical context to validate and extinguish vulnerabilities and policy gaps. See how it works
```

#### Corroborating sources (6)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-123890: Critical Authentication Bypass in VMware vCenter
  - Published: 2026-11-19T21:06:24+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-123890-critical-authentication-bypass-vmware-vcenter
  - Summary: Overview On November 19, 2026, Broadcom published VMware Security Advisory VMSA-2026-0009 , addressing five vulnerabilities in VMware products. The most severe of these, CVE-2026-123890 , is an authentication bypass using an alternate path or channel ( CWE-288 ) in the VMware Directory Service component of vCenter. Broadcom assigned the vulnerability a critical CVSSv3 score of 9.8 . A malicious actor with network access to an affected vCenter deployment may exploit CVE-2026-123890 without credentials to bypass authentication and gain unauthorized access to the system as the Administrator user. Mandiant privately reported the issue to Broadcom. Also, Mandiant/Google Threat Intelligence confirmed in-the-wild exploitation of CVE-2026-123890 by Chinese state-linked threat actor ARMORY CASTLE as early as September 2026. CVE-2026-123890 is distinct from the vCenter authentication bypass vulnerability CVE-2026-59309 that Broadcom addressed earlier in 2026. The vendor FAQ states that all vCent
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: ARMORY CASTLE Exploits vSphere
  - Published: 2026-11-19T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere/
  - Summary: Written by: Jayson Frost, Bryce Greathouse, Dhanesh Kizhakkinan, John Palmisano, Steve Rasch, Daniel Sislo, John Wolfram Introduction On Oct. 15, 2026, Mandiant and Google Threat Intelligence Group (GTIG) published a blog post detailing recent activity in which the suspected PRC-nexus threat actor ARMORY CASTLE (formerly tracked as UNC5221) exploited CVE-2026-102764, a zero-day vulnerability in BeyondTrust Remote Support, which was patched in BT26-05 . We also described some of the threat actor’s post-exploitation operations. In this blog we describe additional post-compromise activity involving the exploitation of a vulnerability in VMware vCenter and the deployment of additional malware families. On Nov. 19, 2026, VMware disclosed CVE-2026-123890, which impacts VMware vCenter Server deployments. vSphere consists of both ESXi (the hypervisor) and vCenter Server. The vCenter server is a centralized platform deployed as a Photon Linux virtual appliance and is used to configure, control,
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: ARMORY CASTLE Exploits vSphere
  - Published: 2026-11-19T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere/
  - Summary: Written by: Jayson Frost, Bryce Greathouse, Dhanesh Kizhakkinan, John Palmisano, Steve Rasch, Daniel Sislo, John Wolfram Introduction On Oct. 15, 2026, Mandiant and Google Threat Intelligence Group (GTIG) published a blog post detailing recent activity in which the suspected PRC-nexus threat actor ARMORY CASTLE (formerly tracked as UNC5221) exploited CVE-2026-102764, a zero-day vulnerability in BeyondTrust Remote Support, which was patched in BT26-05 . We also described some of the threat actor’s post-exploitation operations. In this blog we describe additional post-compromise activity involving the exploitation of a vulnerability in VMware vCenter and the deployment of additional malware families. On Nov. 19, 2026, VMware disclosed CVE-2026-123890, which impacts VMware vCenter Server deployments. vSphere consists of both ESXi (the hypervisor) and vCenter Server. The vCenter server is a centralized platform deployed as a Photon Linux virtual appliance and is used to configure, control,
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: VMware patches vCenter zero-day exploited in attacks since September
  - Published: 2026-11-20T00:26:25+00:00
  - Link: https://www.bleepingcomputer.com/news/security/vmware-patches-vcenter-zero-day-exploited-in-attacks-since-september/
  - Summary: Broadcom has released security updates to fix a critical VMware vCenter Server authentication bypass vulnerability that Chinese-linked hackers have exploited in zero-day attacks since September 2026. [...]
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT
  - Published: 2026-11-19T19:21:06+00:00
  - Link: https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/
  - Summary: Google says a China-linked espionage group exploited a critical VMware vCenter authentication bypass before Broadcom released a patch. The post Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical VMware vCenter Flaw (CVSS 9.8) Lets Network Attackers Bypass Authentication
  - Published: 2026-11-19T15:11:06+00:00
  - Link: https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html
  - Summary: A critical flaw in VMware vCenter lets an attacker with network access bypass authentication and gain unauthorized access to the system, Broadcom, which owns VMware, said in an advisory published today. Fixed versions are out for all supported branches, and the company lists no workaround. vCenter is the central console for managing an organization's ESX hosts and virtual machines. The

### Cluster 7c92294871 — score 40

- Title: Java4Shell (CVE-2026-114938): Pre-auth RCE in OpenJDK, and the challenge of image and feature bloat
- Source: Sysdig (detection_response_operations)
- Published: 2026-11-18T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/java4shell-cve-2026-114938-pre-auth-rce-in-openjdk
- Fetch status: ok
- Member count: 13
- Corroborating source count: 11
- Strong signals: CVE-2026-114938

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- affected_products: Atlassian Confluence, Atlassian Jira, Cisco, OpenAI/ChatGPT
- cve_ids: CVE-2026-114938
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT, Atlassian Jira, Atlassian Confluence
- cve_ids: CVE-2026-114938
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
On 11/17/26, Oracle and OpenJDK shipped fixes for Java4Shell (CVE-2026-114938), a heap memory corruption bug in the AVX-512 accelerated Base64 decoder.
```

#### Full body

```
threat-research This is some text inside of a div block. < back to blog Java4Shell (CVE-2026-114938): Pre-auth RCE in OpenJDK, and the challenge of image and feature bloat Published by: Crystal Morin Sr. Cybersecurity Strategist @ linkedin Subscribe to Threat Research Read more research Published: November 18, 2026 Table of contents TRT in your inbox Get security briefings from the Threat Research Team New campaigns, attacker techniques, and detection guidance — straight to your inbox. Subscribe falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more DISCLAIMER: This blog reflects public findings as of 1:36 UTC, Nov. 18, 2026, and it will be updated as new information is released. Java promised that users would never have to think about memory again. Java's Base64 decoder, however, had other plans. On November 17, 2026, Oracle and OpenJDK shipped fixes for Java4Shell ( CVE-2026-114938 ), a heap memory corruption bug in the AVX-512 accelerated Base64 decoder. Calif, the firm that discovered the vulnerability , says that with 64 A characters and one = , a remote attacker with no credentials can overwrite heap memory, leak it Heartbleed-style, and in the products they tested, get remote code execution (RCE). Calif made a suggestion that Java4Shell’s Base64 optimization and the Squidbleed flaw that they also discovered are calls for vibe-uncoding, or the use of AI to find and remove system bloat to reduce an attack surface. This is the same point that’s been made in multiple Sysdig Cloud Native Security and Usage Reports since 2023 with regard to image bloat. Let’s explore what's confirmed, what's still theoretical, and why after combating and cleaning up image bloat for years, the next fight appears to be feature bloat. Important facts to know now about Java4Shell What: Heap out-of-bounds write in OpenJDK's x86-64 Base64 intrinsic. Pre-authentication on common login paths. Who: OpenJDK 17.0.6 and later (17, 21, 25, 27) on x86-64 CPUs with AVX-512 VBMI. ARM is out. Java 11 and standard Java 8 are out. Oracle also lists the Java 8 performance build (8u511b33-perf) as vulnerable. Severity: 9.2 critical on CVSS 4.0 per Calif, and 8.1 on CVSS 3.1 per OpenJDK's advisory. Exploitation: Calif confirms working RCE in Keycloak, Jira, Confluence, Artifactory, Jenkins, and PingFederate without authorization, plus five more post-auth. The researcher says OpenAI Codex helped find the bug in an hour and build an exploit in two hours for less than $200. Calif stated the exploit will not be publicly shared until organizations have patched the vulnerability. Fix: Oracle builds ending in .1 , or -XX:-UseBASE64Intrinsics as the bridge. What happened Time Event Nov 12 Oracle's pre-release notice: 11 Java SE fixes, all remotely exploitable without authentication, max CVSS 3.1 of 8.1. No CVE IDs. Nov 17 Calif says the bug leaked ahead of the patch and moves its disclosure to 1 p.m. PT (21:00). Confirmed discussions about the report appear on X as early as 10:22. Nov 17, 17:44 UTC OpenJDK's advisory lists CVE-2026-114938 as hotspot/compiler, affecting 17, 21, 25, and 27. Nov 17, 17:53 UTC CISA KEV catalog is released. CVE not included. Nov 17, 20:00 UTC A lab reproduction of the overflow is published and says RCE isn't proven. Nov 17, 21:00 UTC Calif publishes its write-up, with RCE demos across named products. Who's affected by Java4Shell Calif's list of vulnerable builds is broad because everything downstream of OpenJDK inherits the code: Amazon Corretto, Eclipse Temurin, Microsoft Build of OpenJDK, Azul Zulu, BellSoft Liberica, SAP SapMachine, Red Hat OpenJDK, Oracle OpenJDK, Oracle Java SE, and Oracle GraalVM for JDK. Line Vulnerable (Oracle Java SE) Fixed (Oracle) Java 8 performance build 8u511b33-perf 8u513 Java 17 17.0.21.0.3 17.0.21.1 Java 21 21.0.13.0.3 21.0.13.1 Java 25 25.0.5.0.3 25.0.5.1 Java 27
```

#### Corroborating sources (11)

- **Sysdig** (detection_response_operations)
  - Title: Java4Shell (CVE-2026-114938): Pre-auth RCE in OpenJDK, and the challenge of image and feature bloat
  - Published: 2026-11-18T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/java4shell-cve-2026-114938-pre-auth-rce-in-openjdk
  - Summary: On 11/17/26, Oracle and OpenJDK shipped fixes for Java4Shell (CVE-2026-114938), a heap memory corruption bug in the AVX-512 accelerated Base64 decoder.
- **Cisco Talos** (threat_research_primary)
  - Title: CVE-2026-114938: Critical vulnerability in OpenJDK Java
  - Published: 2026-11-18T01:53:03+00:00
  - Link: https://blog.talosintelligence.com/java4shell/
  - Summary: Cisco Talos is tracking the disclosure of a critical vulnerability in OpenJDK Java (CVE-2026-114938), dubbed “Java4Shell,” with a CVSS 4.0 score of 9.2 that may lead to unauthenticated remote code execution (RCE).
- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-114938: Reported Critical Pre-authentication Remote Code Execution in Java 17
  - Published: 2026-11-17T18:26:55+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-114938-reported-critical-pre-authentication-remote-code-execution-java-17
  - Summary: Overview On November 17, 2026, Oracle released patches for CVE-2026-114938 , a heap-based buffer overflow ( CWE-122 ) in the hardware-accelerated Base64 decoder used by OpenJDK and its downstream distributions, such as Oracle Java SE, and Oracle GraalVM. The vulnerability, dubbed “ Java4Shell ” by finders Calif, can allow an unauthenticated remote attacker to crash a Java application or execute code with the privileges of its Java process. Oracle rates the vulnerability High, with a CVSS v3.1 score of 8.1 and high attack complexity, in its November security advisory . Affected OpenJDK runtimes enable the vulnerable Base64 optimization by default when the Java virtual machine (JVM) can use the required x86-64 CPU features, including AVX-512 VBMI. A Java application exposes the flaw when it passes untrusted data to that optimized decoder. For example, a web service may decode HTTP Basic credentials before it checks the username and password. Red Hat reports no known exposure on ARM64 or
- **Sophos X-Ops** (detection_response_operations)
  - Title: 'Java4Shell' vulnerability (CVE-2026-114938) could allow remote code execution
  - Published: 2026-11-17T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/java4shell-could-allow-remote-code-execution
  - Summary: Categories: Threat Research Tags: advisory, vulnerability, Oracle, Java
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Java4Shell Flaw (CVE-2026-114938) Enables Pre-Auth RCE in Jira, Jenkins, Keycloak and More
  - Published: 2026-11-18T11:55:49+00:00
  - Link: https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html
  - Summary: A Java flaw called Java4Shell can let attackers without an account run their own code on Jira, Jenkins, Keycloak, and three other widely used applications, says Calif, the security research firm that disclosed it this week. The flaw is present in Java 17.0.6 and later, and the vulnerable code runs only on x86-64 Intel and AMD chips that support the AVX-512 VBMI feature. Tracked as
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Java4Shell: Remote Code Execution in OpenJDK (CVE-2026-114938)
  - Published: 2026-11-17T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938/
  - Summary: Learn how CVE-2026-114938 corrupts memory in OpenJDK’s AVX-512 Base64 decoder, which deployments are affected, and how to mitigate it.
- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: How Cloudflare WAF helps protect against Java4Shell (CVE-2026-114938)
  - Published: 2026-11-18T14:52:10+00:00
  - Link: https://blog.cloudflare.com/java4shell-waf-protection/
  - Summary: Java4Shell is a critical memory-corruption flaw in OpenJDK's Base64 decoder that can lead to remote code execution. Cloudflare has released six WAF managed rules for paid plans that logs matching requests by default. Patch your Java runtimes now.
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: CVE-2026-114938 OpenJDK RCE (Java4Shell): Everything You Need to Know
  - Published: 2026-11-17T22:29:57+00:00
  - Link: https://www.wiz.io/blog/cve-2026-114938-rce-java4shell-openjdk
  - Summary: Detect and mitigate Java4Shell (CVE-2026-114938), a critical 9.2 RCE vulnerability affecting OpenJDK and major Java-based applications.
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-114938 | Technical Details
  - Published: 2026-11-18T00:31:13+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-114938/
  - Summary: CVE-2026-114938, known as Java4Shell, is a high-severity heap buffer overflow in Java's Base64 decoder. Exploitation depends on specific processor, runtime, and application conditions.
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: “Java4Shell”: Critical OpenJDK Base64 Decoder Flaw Could Allow Unauthenticated Remote Code Execution
  - Published: 2026-11-17T20:35:45+00:00
  - Link: https://orca.security/resources/research/java4shell-critical-openjdk-base64-decoder-flaw-could-allow-unauthenticated-remote-code-execution/
  - Summary: A critical vulnerability dubbed “Java4Shell” (CVE-2026-114938) has been reported in OpenJDK. According to early reports, it lets unauthenticated attackers achieve remote code execution by sending a crafted Base64 string to a Java application running on x86 servers with AVX-512 support. Early reports rate it 9.2 under CVSS 4.0. Java runs a large share of enterprise […]
- **GreyNoise** (cloud_identity_infrastructure)
  - Title: Global Event: Java4Shell (CVE-2026-114938) Live Activity Report
  - Published: 2026-11-18T00:00:00+00:00
  - Link: https://www.greynoise.io/blog/global-event-java4shell-cve-2026-114938-live-activity-report
  - Summary: GreyNoise is monitoring scanning and exploitation attempts against CVE-2026-114938, also known as "Java4Shell," a memory-corruption vulnerability in OpenJDK's Base64 decoder.

### Cluster 2e72543ef9 — score 38

- Title: CVE-2026-132165 | Drupal Core Installer Remote Code Execution Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-11-19T17:49:52+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-132165/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-132165, Drupal

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Drupal
- cve_ids: CVE-2026-114924, CVE-2026-114925, CVE-2026-114938, CVE-2026-119618, CVE-2026-132165
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Drupal
- cve_ids: CVE-2026-132165, CVE-2026-114924, CVE-2026-114925, CVE-2026-114938, CVE-2026-119618
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-132165 is a critical remote code execution vulnerability in the Drupal core installer. Under specific conditions, an unauthenticated attacker can reach install.php and attempt to reinstall a running site.
```

#### Full body

```
CVE-2026-132165 Drupal Core Installer Remote Code Execution Vulnerability CVE-2026-132165 is a critical remote code execution vulnerability in the installer shipped with Drupal core. Under specific conditions, an attacker with no credentials can reach install.php and attempt to reinstall a running site, which can lead to site takeover or remote code execution. Some exploit paths are blocked if the web server cannot write to or change permissions on settings.php, and Drupal states that only uncommon module configurations are exploitable. Drupal rates the issue Critical at 18/25 on its own risk scale in advisory SA-CORE-2026-017 ; NVD has not yet published a CVSS v3.1 score. Drupal’s advisory does not report exploitation in the wild. Technical Details Drupal core ships install.php, the script used to install a new site. Under specific conditions on an already-installed site, an attacker can invoke that installer and begin a reinstallation. The installation process writes configuration and runs site setup logic with the privileges of the web server, so driving it against a live site can hand an attacker administrative control of the site or code execution on the host. Drupal’s advisory notes that some exploit paths are mitigated when the web server cannot write to or change permissions on settings.php, the file that holds database credentials and site configuration. Attack vector: Network; the site’s install.php must be reachable by the attacker. Authentication: None required; Drupal states the flaw can be exploited by anonymous users. User interaction: None reported. Impact: Site takeover and remote code execution; Drupal rates confidentiality and integrity impact as total. Drupal risk score: 18/25 (Critical), risk vector AC:Complex/A:None/CI:All/II:All/E:Proof/TD:Uncommon Internet exposure is not required. Any attacker who can reach a site’s install.php, including from an internal network or a staging environment, can attempt the attack. Stop Guessing, Start Proving Schedule a demo Affected Versions & Patch Affected Drupal core before 10.6.22 Drupal core 11.0.0 through 11.3.21 Drupal core 11.4.0 through 11.4.12 Drupal 8, Drupal 9, Drupal 10.5.x and below, and Drupal 11.2.x and below are end-of-life and receive no security coverage; those sites must upgrade to a supported branch. Fixed Drupal 10.6.22 Drupal 11.3.22 Drupal 11.4.13 Mitigations Drupal recommends blocking public access to /core/install.php in the web server configuration or in the .htaccess file in the site root, and ensuring the web server cannot write to or change permissions on settings.php. Drupal advises keeping installer access restricted after upgrading as well. Drupal states that Drupal Steward customers are protected from known attack vectors but should still upgrade. These steps are workarounds, not a fix; only the patched releases resolve the vulnerability. Timeline November 18, 2026: Drupal published advisory SA-CORE-2026-017 and released Drupal 10.6.22, 11.3.22, and 11.4.13. November 19, 2026: Public reporting on the vulnerability; no in-the-wild exploitation reported. References Drupal Security Advisory SA-CORE-2026-017 BleepingComputer: Drupal patches critical RCE flaw, warns exploits may surface quickly SecurityOnline: CVE-2026-132165 Drupal Remote Code Execution Fixed in 11.4.13 Read about other CVEs CVE-2026-114924 / CVE-2026-114925 CVE-2026-114924 and CVE-2026-114925 are critical Oracle E-Business Suite vulnerabilities that, chained, let a remote attacker with no credentials run operating… Read more CVE-2026-114938 CVE-2026-114938, known as Java4Shell, is a high-severity heap buffer overflow in Java's Base64 decoder. Exploitation depends on specific processor, runtime,… Read more CVE-2026-119618 CVE-2026-119618 is a critical race condition in Apache HTTP Server's mod_http2 that can lead to remote code execution without credentials.… Read more NodeZero ® Platform Implement a continuous find, fix, and verify loop with NodeZero The NodeZero ® platfor
```

#### Corroborating sources (3)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-132165 | Drupal Core Installer Remote Code Execution Vulnerability
  - Published: 2026-11-19T17:49:52+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-132165/
  - Summary: CVE-2026-132165 is a critical remote code execution vulnerability in the Drupal core installer. Under specific conditions, an unauthenticated attacker can reach install.php and attempt to reinstall a running site.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Drupal Patches Critical Installer Flaw That Could Give Unauthenticated Attackers Control of Sites
  - Published: 2026-11-19T14:33:06+00:00
  - Link: https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html
  - Summary: Under specific conditions, a critical vulnerability in Drupal core can allow an attacker without login credentials to use the built-in installer to attempt to reinstall a site. That can lead to a site takeover or remote code execution, and the project rates the vulnerable configurations as uncommon. Fixed releases for all supported branches shipped yesterday. The Drupal Security Team disclosed
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Drupal patches critical RCE flaw, warns exploits may surface quickly
  - Published: 2026-11-19T13:08:08+00:00
  - Link: https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/
  - Summary: The Drupal Security Team has patched a critical remote code execution vulnerability that can let attackers take over vulnerable sites. [...]

### Cluster f170b6e701 — score 29

- Title: CVE-2026-119618: Critical Apache HTTP/2 Race Condition Enables Unauthenticated Remote Code Execution
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-11-16T17:49:55+00:00
- Link: https://orca.security/resources/research/cve-2026-119618-critical-apache-http-2-race-condition-enables-unauthenticated-remote-code-execution/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-119618

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- affected_products: Anthropic/Claude, GitHub, Google Cloud
- cve_ids: CVE-2026-119618
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- affected_products: Google Cloud, Anthropic/Claude, GitHub
- cve_ids: CVE-2026-119618
- urgency_signals: actively_exploited, preauth_unauth, critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
A critical vulnerability in Apache HTTP Server’s mod_http2 module, tracked as CVE-2026-119618 (CVSS 9.8), allows attackers to achieve unauthenticated remote code execution on any server with HTTP/2 enabled. Because exploitation can lead to full server compromise without any authentication, immediate patching is required. The fix is Apache HTTP Server 2.4.71. CVE-2026-119618 at a glance CVE […]
```

#### Full body

```
A critical vulnerability in Apache HTTP Server’s mod_http2 module, tracked as CVE-2026-119618 (CVSS 9.8), allows attackers to achieve unauthenticated remote code execution on any server with HTTP/2 enabled. Because exploitation can lead to full server compromise without any authentication, immediate patching is required. The fix is Apache HTTP Server 2.4.71. CVE-2026-119618 at a glance CVE ID CVE-2026-119618 Severity CVSS 9.8 (Critical) Weakness Race condition (CWE-362) leading to heap memory corruption Vulnerable component assign_headers() function in mod_http2 Authentication required None Affected versions Apache HTTP Server 2.4.55 through 2.4.70; standalone mod_h2 2.0.8 through 2.0.42 Fixed version Apache HTTP Server 2.4.71 Exploitation status Reliable public exploit demonstrated; no confirmed in-the-wild exploitation at the time of writing Temporary workaround Disable HTTP/2 by removing h2 and h2c from the Protocols directive What is CVE-2026-119618? CVE-2026-119618 is a race condition in the assign_headers() function of mod_http2, the module that handles HTTP/2 in Apache HTTP Server. The function runs concurrently using shared resources without proper synchronization (CWE-362), and that gap leads to heap memory corruption. How attackers exploit the mod_http2 race condition Attackers send specially crafted HTTP/2 requests that trigger the race condition. The resulting heap corruption lets them execute arbitrary code with the privileges of the web server process, potentially leading to full infrastructure compromise. No authentication is required to exploit this issue. Which Apache HTTP Server versions are affected? The following components are affected: Apache HTTP Server mod_http2, versions 2.4.55 through 2.4.70 Standalone mod_h2 releases 2.0.8 through 2.0.42 Apache HTTP Server is one of the most widely deployed web servers in the world, and HTTP/2 can be enabled server-wide or per virtual host via the Protocols directive. That means a server can be exposed even if HTTP/2 was only switched on for a single site. The standalone mod_h2 repository on GitHub has been archived since June 2026, so no standalone fix is available for those releases. Is CVE-2026-119618 being exploited in the wild? At the time of writing, public research has demonstrated a reliable exploit against a default mod_http2 configuration, but no confirmed in-the-wild exploitation has been reported. Regardless, the severity and ease of exploitation make this vulnerability high risk, especially in internet-facing deployments. The vulnerability was independently discovered by Anthropic’s OSS Scanner (reported October 26, 2026) and Google Cloud Vulnerability Research (reported November 3, 2026), underscoring the broad interest in this attack surface. What can attackers do after exploiting CVE-2026-119618? Successful exploitation could allow attackers to: Execute arbitrary code on the web server Pivot to internal networks and backend systems Move laterally across the environment, potentially reaching full infrastructure compromise The business consequences include service disruption and data exposure. Given the wormable potential of this flaw, due to the ubiquity of Apache HTTP Server and its unauthenticated attack surface, organizations should treat remediation as an urgent priority. How to fix CVE-2026-119618 Upgrade to Apache HTTP Server 2.4.71 Upgrade to Apache HTTP Server 2.4.71 immediately, prioritizing public-facing servers with HTTP/2 enabled. For standalone mod_h2 users, migrating to the bundled mod_http2 in Apache 2.4.71 is the recommended path forward. Patch status by Linux distribution Distribution Status Red Hat Enterprise Linux 9 Fixed: mod_http2 update (RHSA-2026:98981) Red Hat Enterprise Linux 10 Fixed: mod_http2 update (RHSA-2026:98978) Red Hat Enterprise Linux 6, 7, and 8 Not affected Debian unstable (sid) Fixed: apache2 2.4.71-1 Debian bookworm, trixie, and forky Vulnerable, no fix yet Amazon Linux 2, 2023, and 2027 Preview Fix pending Standa
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: CVE-2026-119618: Critical Apache HTTP/2 Race Condition Enables Unauthenticated Remote Code Execution
  - Published: 2026-11-16T17:49:55+00:00
  - Link: https://orca.security/resources/research/cve-2026-119618-critical-apache-http-2-race-condition-enables-unauthenticated-remote-code-execution/
  - Summary: A critical vulnerability in Apache HTTP Server’s mod_http2 module, tracked as CVE-2026-119618 (CVSS 9.8), allows attackers to achieve unauthenticated remote code execution on any server with HTTP/2 enabled. Because exploitation can lead to full server compromise without any authentication, immediate patching is required. The fix is Apache HTTP Server 2.4.71. CVE-2026-119618 at a glance CVE […]

### Cluster c30cd1e74e — score 28

- Title: CVE-2026-114924 / CVE-2026-114925 | Oracle E-Business Suite Authorization Bypass & Remote Code Execution Vulnerabilities
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-11-19T19:35:51+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-114924-cve-2026-114925/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-114924, CVE-2026-114925

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-114924, CVE-2026-114925
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-114924, CVE-2026-114925
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-114924 and CVE-2026-114925 are critical Oracle E-Business Suite vulnerabilities that, chained, let a remote attacker with no credentials run operating system commands on the application tier over HTTP.
```

#### Full body

```
CVE-2026-114924 / CVE-2026-114925 Oracle E-Business Suite Authorization Bypass & Remote Code Execution Vulnerabilities CVE-2026-114924 and CVE-2026-114925 are critical vulnerabilities in Oracle E-Business Suite, Oracle’s on-premises ERP platform. CVE-2026-114924 is an authorization bypass in the Core component of Oracle Application Object Library; CVE-2026-114925 is a remote code execution flaw in the REST Services component of Oracle Applications Framework. Chained, they let a remote attacker with no credentials execute operating system commands on the EBS application tier over HTTP. Both affect supported versions 12.2.3-12.2.15 and were fixed in the Oracle Critical Security Patch Update of November 2026 . Oracle rates each vulnerability 9.8 (Critical) under CVSS v3.1. Oracle’s advisory does not report exploitation in the wild, and neither CVE appears in CISA’s Known Exploited Vulnerabilities catalog. Horizon3 attack researchers reverse engineered the patch. Technical Details Oracle Application Object Library provides the shared function-authorization layer that other E-Business Suite modules build on. CVE-2026-114924 lets crafted HTTP requests bypass those authorization checks and reach protected EBS REST functions, which run with APPS database privileges. CVE-2026-114925 is in the REST Services component of Oracle Applications Framework, where a request handler instantiates Java classes named in request input without restricting which classes are permitted — the pattern that turns a REST call into code execution on the application tier. Chaining the bypass to that handler removes the credential requirement, giving command execution as the account that runs the EBS application server. Weakness: CWE-306, Missing Authentication for a Critical Function Attack vector: Network — HTTP access to an EBS web tier Authentication: None User interaction: None Impact: Takeover of the affected component, with High confidentiality, integrity and availability impact CVSS v3.1: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (9.8, Critical, scored by Oracle) Internet exposure is not required: any attacker who can reach an EBS HTTP endpoint from an internal, partner, or supplier network can attempt the chain. Stop Guessing, Start Proving Schedule a demo Affected Versions & Patch Affected Oracle Application Object Library (Core), Oracle E-Business Suite supported versions 12.2.3-12.2.15 — CVE-2026-114924 Oracle Applications Framework (REST Services), Oracle E-Business Suite supported versions 12.2.3-12.2.15 — CVE-2026-114925 Fixed Oracle E-Business Suite installations patched with the Critical Security Patch Update of November 2026. Oracle does not publish a fixed version number for these CVEs; patch numbers are listed in the Oracle E-Business Suite Patch Availability Document linked from the advisory. Mitigations Oracle’s advisory publishes no workaround for either vulnerability; the November 2026 patch is the fix. Until it can be applied, restrict network access to Oracle E-Business Suite HTTP and REST endpoints with firewall rules or network segmentation. That limits who can reach the vulnerable endpoints, but it does not remove the vulnerability and does not stop an attacker who already has access to a network segment that reaches EBS. It is a workaround, not a fix. Timeline November 17, 2026: Oracle published the Critical Security Patch Update for November 2026, including patches for both vulnerabilities. November 17, 2026: The CVE records for CVE-2026-114924 and CVE-2026-114925 were published. November 17, 2026: CIS and the MS-ISAC published advisory 2026-135 covering the Oracle update. November 18, 2026: CISA recorded an SSVC decision of “Exploitation: none” for both CVEs. References Oracle Critical Security Patch Update Advisory – November 2026 Text Form of Oracle CSPU November 2026 Risk Matrices NIST NVD Record: CVE-2026-114924 NIST NVD Record: CVE-2026-114925 CIS / MS-ISAC Advisory 2026-135: Multiple Vulnerabilities in Oracle Products C
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-114924 / CVE-2026-114925 | Oracle E-Business Suite Authorization Bypass & Remote Code Execution Vulnerabilities
  - Published: 2026-11-19T19:35:51+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-114924-cve-2026-114925/
  - Summary: CVE-2026-114924 and CVE-2026-114925 are critical Oracle E-Business Suite vulnerabilities that, chained, let a remote attacker with no credentials run operating system commands on the application tier over HTTP.

### Cluster 63382dfd81 — score 27

- Title: PHP Patches 7 Critical Flaws, Including Session and PHP-FPM Remote Code Execution (CVE-2026-115560, CVE-2026-129289)
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-11-19T16:11:36+00:00
- Link: https://orca.security/resources/research/php-patches-7-critical-flaws-including-session-and-php-fpm-remote-code-execution-cve-2026-115560-cve-2026-129289/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-115560, CVE-2026-129289

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-115560, CVE-2026-126714, CVE-2026-129289
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-115560, CVE-2026-129289, CVE-2026-109618, CVE-2026-109619, CVE-2026-126714
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
On November 19, 2026, the PHP project released PHP 8.2.36, 8.3.37, 8.4.28 and 8.5.13, fixing 17 vulnerabilities. Seven are rated critical by the PHP project (CVSS 4.0 9.2), including CVE-2026-115560, a session serializer mismatch that can lead to remote code execution, and CVE-2026-129289, a PHP-FPM request smuggling flaw that lets an unauthenticated attacker forge a […]
```

#### Full body

```
On November 19, 2026, the PHP project released PHP 8.2.36, 8.3.37, 8.4.28 and 8.5.13, fixing 17 vulnerabilities. Seven are rated critical by the PHP project (CVSS 4.0 9.2), including CVE-2026-115560, a session serializer mismatch that can lead to remote code execution, and CVE-2026-129289, a PHP-FPM request smuggling flaw that lets an unauthenticated attacker forge a backend request and execute attacker-controlled PHP code. PHP 8.6.0, released the same day, already includes the fixes. PHP runs a large share of the world’s websites and web applications, in virtual machines, containers and managed platforms alike. CVE-2026-115560 was pre-announced in October, a few days after the PHP2Shell fixes (CVE-2026-109618, CVE-2026-109619), with the mitigation of disabling session upload progress. Today’s release publishes its full details and fixes it alongside 16 other vulnerabilities. Several of them need specific configurations, but the release as a whole affects every supported PHP branch. PHP November 2026 security release: key facts Fact Detail CVEs 17 in total; critical: CVE-2026-115560, CVE-2026-129289, CVE-2026-126714, CVE-2026-129496, CVE-2026-129481, CVE-2026-129474, CVE-2026-129182 Type Deserialization of untrusted data (CWE-502) in the session extension; HTTP request smuggling (CWE-444) in PHP-FPM; several use-after-free bugs Severity Rated critical by the PHP project (CVSS 4.0 9.2) for all seven; NVD score pending Required configuration CVE-2026-115560: session upload progress enabled and mismatched session serializers. CVE-2026-129289: PHP-FPM behind a front end that reuses FastCGI connections Affected versions PHP 8.2.0 to 8.2.35, 8.3.0 to 8.3.36, 8.4.0 to 8.4.27 and 8.5.0 to 8.5.12 (some CVEs affect only some branches) Fixed versions 8.2.36, 8.3.37, 8.4.28, 8.5.13; PHP 8.6.0 includes the fixes Exposure Internet-facing PHP applications; exploitability depends on configuration and on the application Workaround Set session.upload_progress.enabled = 0 (CVE-2026-115560); disable FastCGI connection reuse on the front end (CVE-2026-129289); other CVEs have their own workarounds Exploitation No known in-the-wild exploitation; a public proof of concept exists for CVE-2026-115560 in a lab setup What is CVE-2026-115560? CVE-2026-115560 is a flaw in PHP’s session upload progress feature. When a client uploads a file, PHP writes the upload’s progress into the user’s session, including a value the client controls. PHP supports several session serialization formats, and if that data is written in one format (php_serialize or php_binary) and later read in another (php), the reader can treat attacker-supplied bytes as serialized object data. This can happen when an application switches session.serialize_handler at runtime before calling session_start(), or when separate applications, PHP-FPM pools, virtual hosts or command-line jobs with different settings share the same session storage. If the reading application has a suitable deserialization gadget chain, the attacker can execute code with the privileges of the PHP worker. According to the PHP advisory, the original report demonstrated command execution with a Guzzle gadget on PHP 8.2.35, 8.3.36, 8.4.27 and 8.5.12, and with a Monolog gadget. The fix turns session upload progress off by default and blocks runtime changes to session settings while the feature is enabled. An explicit session.upload_progress.enabled = 1 in existing configuration still overrides the new default, and the PHP project notes that matching serializers across separate configurations is still the administrator’s responsibility. What is CVE-2026-129289? CVE-2026-129289 is an HTTP request smuggling flaw in PHP-FPM. When an application opens php://input but does not read the request body to the end, PHP can leave the unread bytes on a persistent FastCGI connection. An attacker can place a crafted FastCGI message in that body, and PHP-FPM accepts it as a new request that the web server never created or authorized. Th
```

#### Corroborating sources (2)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: PHP Patches 7 Critical Flaws, Including Session and PHP-FPM Remote Code Execution (CVE-2026-115560, CVE-2026-129289)
  - Published: 2026-11-19T16:11:36+00:00
  - Link: https://orca.security/resources/research/php-patches-7-critical-flaws-including-session-and-php-fpm-remote-code-execution-cve-2026-115560-cve-2026-129289/
  - Summary: On November 19, 2026, the PHP project released PHP 8.2.36, 8.3.37, 8.4.28 and 8.5.13, fixing 17 vulnerabilities. Seven are rated critical by the PHP project (CVSS 4.0 9.2), including CVE-2026-115560, a session serializer mismatch that can lead to remote code execution, and CVE-2026-129289, a PHP-FPM request smuggling flaw that lets an unauthenticated attacker forge a […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PHP Fixes 7 Critical Flaws, Including Bugs That Could Allow Remote Code Execution
  - Published: 2026-11-19T15:18:07+00:00
  - Link: https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html
  - Summary: The PHP Foundation has released security updates to address multiple critical security flaws that could be exploited to achieve remote code execution on affected deployments, including CVE-2026-115560. The release of the patch follows an advance notice in which the project maintainers alerted users to multiple critical vulnerabilities affecting all supported PHP versions under specific

### Cluster 1a9bc5bf69 — score 25

- Title: COLD RELIC: A Case Study in Impersonation and Compromise
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-11-17T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: UNC4057

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng
- actor_attribution: UNC4057
- affected_industries: government
- affected_products: Google Workspace
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- actor_attribution: UNC4057
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Josh Murchie, John Wolfram, Joseph Spero, Peter Ukhanov, Fernando Tomlinson, Jr., Wesley Shields Introduction Over the past year, Mandiant has responded to a series of linked intrusions demonstrating how Russian cyber espionage group COLD RELIC (formerly tracked as COLDRIVER and UNC4057; also known as Star Blizzard, Callisto, and Gossamer Bear) turns a single cloud compromise into a springboard for ongoing third party compromise and espionage. Most recently, Mandiant investigated a 2026 compromise at a US-based organization where COLD RELIC directly weaponized data, the corporate staff directory, and identities stolen during a late-2025 compromise, which Mandiant also investigated, at a separate US-based organization. COLD RELIC is a Russian state-sponsored threat group that the US Department of Justice (DOJ) has assessed operates within Russia's Federal Security Service (FSB). The group is known for implementing sophisticated phishing and malware campaigns with the aim to
```

#### Full body

```
Threat Intelligence COLD RELIC: A Case Study in Impersonation and Compromise November 17, 2026 Google Threat Intelligence Group Mandiant Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Written by: Josh Murchie, John Wolfram, Joseph Spero, Peter Ukhanov, Fernando Tomlinson, Jr., Wesley Shields Introduction Over the past year, Mandiant has responded to a series of linked intrusions demonstrating how Russian cyber espionage group COLD RELIC (formerly tracked as COLDRIVER and UNC4057; also known as Star Blizzard, Callisto, and Gossamer Bear) turns a single cloud compromise into a springboard for ongoing third party compromise and espionage. Most recently, Mandiant investigated a 2026 compromise at a US-based organization where COLD RELIC directly weaponized data, the corporate staff directory, and identities stolen during a late-2025 compromise, which Mandiant also investigated, at a separate US-based organization. COLD RELIC is a Russian state-sponsored threat group that the US Department of Justice (DOJ) has assessed operates within Russia's Federal Security Service (FSB). The group is known for implementing sophisticated phishing and malware campaigns with the aim to gain access to information of strategic or political relevance to the Russian government, as well as to leverage compromised access to target compromised individuals’ broader social and professional networks. Once COLD RELIC compromises a target, it uses stolen emails and data to establish authentic pretexts and impersonate contacts when reaching out to subsequent targets. While COLD RELIC has largely maintained a low profile, yielding minimal public reporting relative to other Russia-nexus threat actors, it has been highly successful at compromising high-value targets (including government officials, defense contractors, and non-governmental organizations (NGOs) across Europe and North America) while maintaining a consistent operational tempo. While Google Threat Intelligence Group (GTIG) has tracked and disrupted COLD RELIC phishing campaigns since 2015, recent Mandiant incident response investigations have uncovered critical new insights into the group’s social engineering and post-compromise tradecraft. We are sharing this end-to-end analysis—along with actionable detection and hardening guidance—to help organizations defend against COLD RELIC’s ongoing use of stolen pretexts, localized residential proxies, and cross-cloud identity abuse. As part of our efforts to thwart this threat actor, we issue Government-backed attack alerts when we detect COLD RELIC targeting Google accounts. COLD RELIC remains an active threat; GTIG has observed evidence of new phishing operations as recently as November 2026. Threat Detail Over more than a decade of tracking COLD RELIC alongside Mandiant incident response investigations, we have observed the group continually refine how it leverages data harvested from one intrusion to enable follow-on operations against downstream targets. In late 2025, COLD RELIC downloaded a large volume of data from a US-based organization, searching for names, email addresses, and email archives, likely to fulfill broader intelligence requirements. In 2026, Mandiant investigated a subsequent COLD RELIC intrusion at a second US-based organization where phishing URL parameters and impersonation pretexts indicated that COLD RELIC likely leveraged contact and relationship context from the first organization to target the second. One of the hallmarks of COLD RELIC phishing campaigns is the use of a compromised website as the initial link that will redirect the target to the actual phishing domain. This provides COLD RELIC with a layer of misdirection and hides their phishing domains, while also giving them a chance to fingerprint anyone visiting the link to determine if they should be redirected or not. A COLD RELIC phishing link usually contains a parameter on the end of it with a value that is
```

#### Corroborating sources (3)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: COLD RELIC: A Case Study in Impersonation and Compromise
  - Published: 2026-11-17T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/
  - Summary: Written by: Josh Murchie, John Wolfram, Joseph Spero, Peter Ukhanov, Fernando Tomlinson, Jr., Wesley Shields Introduction Over the past year, Mandiant has responded to a series of linked intrusions demonstrating how Russian cyber espionage group COLD RELIC (formerly tracked as COLDRIVER and UNC4057; also known as Star Blizzard, Callisto, and Gossamer Bear) turns a single cloud compromise into a springboard for ongoing third party compromise and espionage. Most recently, Mandiant investigated a 2026 compromise at a US-based organization where COLD RELIC directly weaponized data, the corporate staff directory, and identities stolen during a late-2025 compromise, which Mandiant also investigated, at a separate US-based organization. COLD RELIC is a Russian state-sponsored threat group that the US Department of Justice (DOJ) has assessed operates within Russia's Federal Security Service (FSB). The group is known for implementing sophisticated phishing and malware campaigns with the aim to
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: COLD RELIC: A Case Study in Impersonation and Compromise
  - Published: 2026-11-17T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise/
  - Summary: Written by: Josh Murchie, John Wolfram, Joseph Spero, Peter Ukhanov, Fernando Tomlinson, Jr., Wesley Shields Introduction Over the past year, Mandiant has responded to a series of linked intrusions demonstrating how Russian cyber espionage group COLD RELIC (formerly tracked as COLDRIVER and UNC4057; also known as Star Blizzard, Callisto, and Gossamer Bear) turns a single cloud compromise into a springboard for ongoing third party compromise and espionage. Most recently, Mandiant investigated a 2026 compromise at a US-based organization where COLD RELIC directly weaponized data, the corporate staff directory, and identities stolen during a late-2025 compromise, which Mandiant also investigated, at a separate US-based organization. COLD RELIC is a Russian state-sponsored threat group that the US Department of Justice (DOJ) has assessed operates within Russia's Federal Security Service (FSB). The group is known for implementing sophisticated phishing and malware campaigns with the aim to
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Russian COLD RELIC Hackers Use Stolen Google Workspace Data to Breach Second U.S. Organization
  - Published: 2026-11-18T05:58:04+00:00
  - Link: https://thehackernews.com/2026/11/russian-cold-relic-hackers-use-stolen.html
  - Summary: The Russia-linked cyber espionage group known as Cold Relic (formerly COLDRIVER and UNC4057) has been observed weaponizing a single cloud compromise into a launchpad for a series of linked intrusions resulting in third-party compromise. Google's Mandiant and Threat Intelligence Group (GTIG) said it investigated a 2026 compromise at a U.S.-based organization in which the adversary leveraged

### Cluster 581cf0398c — score 24

- Title: Scans for LiteLLM/Starlette (CVE-2026-42271, CVE-2026-48710), (Mon, Nov 16th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-11-16T13:11:04+00:00
- Link: https://isc.sans.edu/diary/rss/33522
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-42271, CVE-2026-48710

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-42271, CVE-2026-48710
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Primary article taxonomy
- cve_ids: CVE-2026-42271, CVE-2026-48710
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Summary

```
This weekend, we started seeing requests for /mcp-rest/test/tools/list hitting our honeypots. These requests appear to attempt to exploit CVE-2026-42271 and CVE-2026-48710. Horizon3.ai published a short write-up about how these vulnerabilities can be chained to achieve remote code execution without authentication [Horizon3]
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Scans for LiteLLM/Starlette (CVE-2026-42271, CVE-2026-48710), (Mon, Nov 16th)
  - Published: 2026-11-16T13:11:04+00:00
  - Link: https://isc.sans.edu/diary/rss/33522
  - Summary: This weekend, we started seeing requests for /mcp-rest/test/tools/list hitting our honeypots. These requests appear to attempt to exploit CVE-2026-42271 and CVE-2026-48710. Horizon3.ai published a short write-up about how these vulnerabilities can be chained to achieve remote code execution without authentication [Horizon3]

### Cluster dd7ae8db6f — score 23

- Title: Which Holes Can Attackers Really Bite Into?
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-11-18T23:54:45+00:00
- Link: https://horizon3.ai/intelligence/infographics/which-holes-can-attackers-really-bite-into/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Security gaps can hide in unpatched systems, weak passwords, or controls that do less than expected. This infographic outlines five questions CISOs and security teams can answer with autonomous penetration testing to see what attackers can actually exploit.
```

#### Full body

```
Which Holes Can Attackers Really Bite Into? Horizon3 November 18, 2026 Infographics Security gaps can hide in an unpatched system, a weak password, or a control that does less than expected. Autonomous penetration testing goes beyond identifying potential weaknesses: it actively tests whether they can be exploited and chained together to reach sensitive data or critical systems. This infographic outlines five questions CISOs and security teams can answer through autonomous penetration testing. Key Takeaways: Five Questions Testing Can Answer Which weaknesses should you fix first? Severity scores alone cannot tell you what attackers can exploit. Testing reveals exploitable exposure, helping you prioritize fixes based on what attackers could reach. What could an attacker access with a compromised account? Weak passwords and exposed credentials can give attackers a foothold. Testing reveals whether they can escalate privileges and move laterally to access systems and sensitive data. Which weaknesses connect into a path to critical assets? An overlooked system may become a stepping stone. Attackers can chain vulnerabilities, credentials, and misconfigurations together to reach sensitive data or critical systems. Do your controls block the activity you expect them to stop? Configuration and coverage gaps can limit a control’s effectiveness. Testing shows whether attack activity can succeed despite the defenses in place. Can you show leadership what improved? A closed ticket records completed work. Retesting verifies the fix worked, giving leadership clear evidence of reduced exposure and remaining weaknesses. Why These Insights Matter Together, these questions shift the conversation from what could be wrong to what attackers can actually do. Exploitable weaknesses, connected attack paths, control gaps, and verified fixes give leaders evidence to prioritize remediation and track real progress: find the holes, then verify the fixes. Download the Infographic Download the infographic to see all five questions and how autonomous penetration testing helps answer them. Download the infographic How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Which Holes Can Attackers Really Bite Into?
  - Published: 2026-11-18T23:54:45+00:00
  - Link: https://horizon3.ai/intelligence/infographics/which-holes-can-attackers-really-bite-into/
  - Summary: Security gaps can hide in unpatched systems, weak passwords, or controls that do less than expected. This infographic outlines five questions CISOs and security teams can answer with autonomous penetration testing to see what attackers can actually exploit.

### Cluster dec648cd5c — score 22

- Title: Operation ShadowCloud: cloud service–based backdoors targeting government networks in Asia and Africa. Part 1
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-17T08:00:37+00:00
- Link: https://securelist.com/operation-shadowcloud-gitdoor/122004/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 6
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, supply_chain, web_shell_backdoor
- affected_industries: critical_infrastructure, government
- affected_products: Azure, GitHub, Microsoft SharePoint, PyPI
- urgency_signals: actively_exploited
- content_type: event_promotion, news_report, threat_research
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor, active_exploitation
- affected_industries: government, critical_infrastructure
- affected_products: GitHub, Microsoft SharePoint
- urgency_signals: actively_exploited
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Summary

```
In part 1 of our analysis of the recently uncovered Operation ShadowCloud, we discuss the initial infection stage, the GitDoor backdoor using GitHub as a C2, and the shellcode families it loads.
```

#### Full body

```
Content menu Close Subscribe Threat Response Table of Contents Introduction Initial infection Loaders Type 1 Loader (MD5 32151547d912488ac5242731057170a3) Type 2 Loader (MD5 e63ec733393e4e7e3424cbff918003a3) Backdoors GitDoor (MD5 552f0a9cc5fc3755721fa49be05e8035) Command processing Custom shellcodes GitHub repositories Conclusion Indicators of Compromise MeshAgent Type 1 Loader Type 2 Loader Encrypted Payload GitDoor GraphDoor Legitimate executables MeshAgent C2 Legitimate Cloud Storage GitHub repositories Authors Saurabh Sharma Noushin Shabab Introduction In early 2026, we identified a new, active intrusion campaign that we have named Operation ShadowCloud . The threat actor behind it is abusing the legitimate MeshAgent utility to drop two brand-new backdoors. These implants hide their command‑and‑control (C2) traffic behind cloud services Microsoft SharePoint, GitHub, and Ably , allowing the implants to blend in with normal traffic, effectively evading network-based detections. We’ve called the implants GraphDoor and GitDoor , reflecting the cloud platform they use for C2. While their C2 protocols differ, the two backdoors share key capabilities: On‑demand plug-in download : fetching additional modules as needed In‑memory shellcode injection : loading malicious code directly into memory to extend functionality without touching the disk The threat actor specifically deploys a modified Erfrp client and Ably messaging service-based plug-ins to proxy traffic between infected systems and C2 servers. In addition to the plug-ins, we uncovered several shellcode families, most of them delivered as COFF (Common Object File Format) binaries. Our analysis reveals a sophisticated, modular toolset actively maintained and updated with multiple observed backdoor versions in the wild. We found victims in Asia and Africa, primarily within the government sector. In a recent brief, Sophos touched on a fragment of this campaign. In this two‑part blog, we dive deeper, detailing the backdoors’ C2 communication methods, the assortment of shellcode families and plug-ins that the threat actor delivers to the compromised machines, and the infrastructure we observed supporting the operation. We also highlight the attribution clues: This article (Part 1 of the story) deals with the initial infection vector, the GitDoor backdoor, and various shellcode families the threat actor drops onto target machines. Part 2 provides details on the GraphDoor backdoor and the plug-in suite (Keylogging, Process Listing, Screen Capturing, Modified Erfrp Proxy, and Ably Channel Proxy) and examines the evidence that points to links with Chinese‑speaking threat groups. Initial infection During our investigation, we uncovered two separate instances of the MeshCentral Agent (MD5: 74b025084026d8d9a64661bf995d835b), which were launched inside a Taiwanese organization. MeshCentral is a web‑based tool that provides remote‑desktop control, command‑line access, and file‑management capabilities. The exact entry point that let the attackers install the agent is unknown, but evidence points to the reuse of a prior infection already present on the network. The MeshCentral Agent was hard‑coded to reach a remote server at wss://27.102.66[.]162:443/agent.ashx . Once the C2 session was established, the adversary used the agent to drop three additional items on the endpoint: A legitimate binary used for DLL sideloading A malicious loader DLL responsible for unpacking and executing further code An encrypted file containing the core payload 1st Instance C:\windows\system32\start.exe: legitimate Sandboxie Start binary C:\windows\system32\sbiedll.dll: malicious loader C:\windows\system32\config.ini: encrypted backdoor file 2nd Instance C:\Windows\system32\dts\pc\apo4x\dtsapo4service.exe: legitimate Python application binary C:\Windows\System32\dts\pc\apo4x\python39.dll: malicious loader C:\Windows\system32\dts\pc\apo4x\config.ini: encrypted backdoor file 1 2 3 4 5 6 7 8 9 1st Instance C : \ wi
```

#### Corroborating sources (6)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Operation ShadowCloud: cloud service–based backdoors targeting government networks in Asia and Africa. Part 1
  - Published: 2026-11-17T08:00:37+00:00
  - Link: https://securelist.com/operation-shadowcloud-gitdoor/122004/
  - Summary: In part 1 of our analysis of the recently uncovered Operation ShadowCloud, we discuss the initial infection stage, the GitDoor backdoor using GitHub as a C2, and the shellcode families it loads.
- **Microsoft Security Blog** (threat_research_primary)
  - Title: The risks of device code authentication for AI coding agents
  - Published: 2026-11-17T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/
  - Summary: Lab research shows how device code phishing, a technique that applies to any device-flow client, can extend to AI coding agents, using GitHub Copilot CLI as an illustrative example. The post The risks of device code authentication for AI coding agents appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: The risks of device code authentication for AI coding agents
  - Published: 2026-11-17T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/
  - Summary: Lab research shows how device code phishing, a technique that applies to any device-flow client, can extend to AI coding agents, using GitHub Copilot CLI as an illustrative example. The post The risks of device code authentication for AI coding agents appeared first on Microsoft Security Blog .
- **Elastic Security Labs** (detection_response_operations)
  - Title: We caught the agent-framework PyPI compromise six minutes after it published
  - Published: 2026-11-18T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/we-caught-the-agent-framework-pypi-compromise-six-minutes-after-it-published
  - Summary: Versions 1.26.1 and 1.26.2 stole Azure, Azure DevOps and GitHub Actions tokens from a .pth hook that ran on every Python launch, so if either one touched a build agent or a laptop, assume every secret on that host is gone.
- **Simon Willison** (ai_security_agentic_risk)
  - Title: datasette 1.0a43
  - Published: 2026-11-15T23:20:27+00:00
  - Link: https://simonwillison.net/2026/Nov/15/datasette/
  - Summary: Release: datasette 1.0a43 I've been leaning hard into Claude Fable 5.2 to help knock things off the 1.0 milestone , which is now 53% complete. The biggest 1.0 item in this release is streaming support for output renderers - the built-in TSV and CSV export mechanisms now use this as well, and plugins can register themselves as capable of streaming every row in a table in one go via the new Response.stream() method. There are a couple of security fixes, one of which I deemed deserving of a GitHub advisory : private stored queries could be exposed, granting access to the title and SQL of the query (but not allowing that query to be executed). There are dozens of smaller improvements. The row page JSON representation finally has a design suitable for 1.0 . A new <datasette-copy-button> Web Component provides copy-schema in various places. JSON in columns on the row page can be pretty-printed. There's a new DatasetteModal.confirm() JavaScript utility method. Plus dozens of bug fixes, includ
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New GitDoor and GraphDoor Backdoors Turn GitHub and SharePoint Into Covert C2 Channels
  - Published: 2026-11-17T11:20:18+00:00
  - Link: https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html
  - Summary: Government sectors in Asia and Africa have been targeted by an active cyber intrusion campaign that delivers to previously undocumented backdoors that leverage legitimate services like Microsoft SharePoint and GitHub for command‑and‑control (C2). The activity has been codenamed Operation ShadowCloud by Kaspersky. The Russian cybersecurity company said it identified the campaign in early 2026.

### Cluster b2f367d9d1 — score 21

- Title: From view-only access to container root: five vulnerabilities in ONLYOFFICE Docs (FIXED)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-16T16:24:38+00:00
- Link: https://www.rapid7.com/blog/post/ve-from-view-only-access-to-container-root-five-vulnerabilities-in-onlyoffice-docs-fixed
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-110385, CVE-2026-113627, CVE-2026-113630, CVE-2026-113631, CVE-2026-97727

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- cve_ids: CVE-2026-110385, CVE-2026-113627, CVE-2026-113630, CVE-2026-113631, CVE-2026-97727
- urgency_signals: poc_available, preauth_unauth
- content_type: threat_research
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- cve_ids: CVE-2026-113627, CVE-2026-110385, CVE-2026-97727, CVE-2026-113630, CVE-2026-113631
- urgency_signals: preauth_unauth, poc_available
- content_type: threat_research
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview As part of our research into Zimbra Collaboration Suite , Rapid7 reported five findings in ONLYOFFICE Docs. An attacker with view-only access to a document can chain vulnerabilities in ONLYOFFICE Docs to execute arbitrary operating system commands as root inside the official DocumentServer container. The findings also expose server files and document data that the viewer never displays, even when downloading is disabled. CVE Finding CVSS CVE-2026-113627 DocBuilder native file read and Session JWT forgery 7.1 High CVE-2026-110385 DocBuilder SaveFile conversion parameter injection and code execution 8.7 High CVE-2026-97727 Complete-save format path traversal and arbitrary file write 6.5 Medium CVE-2026-113630 Root-helper command injection 7.8 High CVE-2026-113631 View-only export of non-rendered document data 6.5 Medium ONLYOFFICE confirmed on October 23, 2026 that all five findings were fixed in Document Server 10.0. The changelog describes the release's security changes. Proof
```

#### Full body

```
Rapid7 Intelligence From view-only access to container root: five vulnerabilities in ONLYOFFICE Docs (FIXED) Jonah Burgess Nov 16, 2026 | Last updated on Nov 16, 2026 | 28 min read From view-only access to container root: five vulnerabilities in ONLYOFFICE Docs (FIXED) Table of contents From view-only access to container root: five vulnerabilities in ONLYOFFICE Docs (FIXED) Table of contents Overview As part of our research into Zimbra Collaboration Suite , Rapid7 reported five findings in ONLYOFFICE Docs. An attacker with view-only access to a document can chain vulnerabilities in ONLYOFFICE Docs to execute arbitrary operating system commands as root inside the official DocumentServer container. The findings also expose server files and document data that the viewer never displays, even when downloading is disabled. CVE Finding CVSS CVE-2026-113627 DocBuilder native file read and Session JWT forgery 7.1 High CVE-2026-110385 DocBuilder SaveFile conversion parameter injection and code execution 8.7 High CVE-2026-97727 Complete-save format path traversal and arbitrary file write 6.5 Medium CVE-2026-113630 Root-helper command injection 7.8 High CVE-2026-113631 View-only export of non-rendered document data 6.5 Medium ONLYOFFICE confirmed on October 23, 2026 that all five findings were fixed in Document Server 10.0. The changelog describes the release's security changes. Proof-of-concept code is available on the accompanying Github repository . Product description ONLYOFFICE Docs provides online viewers and editors for documents, spreadsheets, presentations, forms and PDFs. It supports collaborative editing and can integrate with applications that store and share files. An integrating application, for example Zimbra Collaboration Suite, supplies an opening configuration identifying the document and the user's permissions, signed with the Browser key. This client-visible credential is referred to below as the Editor JWT. After opening a document, DocumentServer issues a Session JWT for reconnecting and saving. Incoming service requests, including document-building jobs, are validated using ONLYOFFICE's Inbox JWT key. DocumentServer can also send generated document output to the integrating application's callback URL. Credit This assessment and the exploit-chain research were conducted by Jonah Burgess (CryptoCat), Senior Security Researcher at Rapid7 . The findings are being disclosed in accordance with Rapid7's vulnerability disclosure policy . Testing setup Rapid7 tested the official onlyoffice/documentserver:9.4.0 image with package onlyoffice-documentserver 9.4.0-129 . DocumentServer ran as the ds account. JWT validation remained enabled, and no authentication check, private-address filter, or vendor code was disabled or modified. Browser and Inbox validation used the same effective signing key. Our analysis of the vendor supplied fixes compares the v9.4.0.129 and v10.0.0.169 tags of ONLYOFFICE/server , ONLYOFFICE/core and ONLYOFFICE/document-server-package . Rapid7 also performed targeted checks on package 10.0.0-169 . For the conditional WOPI test on 9.4.0-129 , Rapid7 enabled only WOPI_ENABLED=true and left the shipped WOPI IP filter unchanged at its default allow-all rule. Exploitation was demonstrated only on 9.4.0-129; the broader affected-version range is unknown. Impact View-only document access can lead to command execution as ds and then root inside the official container. The two exploit chains use different file-write stages. With WOPI enabled and an attacker-controlled source reachable and permitted by its IP filter, the same DocBuilder authorization failure provides an unauthenticated entry. Separately, a viewer denied download can obtain a reconstructed DOCX containing custom XML, custom properties and field instructions that the viewer never displayed. Editor JWT authorizes native file reads and session JWT forgery (CVE-2026-113627) An attacker with view-only access to a document can use /docbuilder to steal fil
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: From view-only access to container root: five vulnerabilities in ONLYOFFICE Docs (FIXED)
  - Published: 2026-11-16T16:24:38+00:00
  - Link: https://www.rapid7.com/blog/post/ve-from-view-only-access-to-container-root-five-vulnerabilities-in-onlyoffice-docs-fixed
  - Summary: Overview As part of our research into Zimbra Collaboration Suite , Rapid7 reported five findings in ONLYOFFICE Docs. An attacker with view-only access to a document can chain vulnerabilities in ONLYOFFICE Docs to execute arbitrary operating system commands as root inside the official DocumentServer container. The findings also expose server files and document data that the viewer never displays, even when downloading is disabled. CVE Finding CVSS CVE-2026-113627 DocBuilder native file read and Session JWT forgery 7.1 High CVE-2026-110385 DocBuilder SaveFile conversion parameter injection and code execution 8.7 High CVE-2026-97727 Complete-save format path traversal and arbitrary file write 6.5 Medium CVE-2026-113630 Root-helper command injection 7.8 High CVE-2026-113631 View-only export of non-rendered document data 6.5 Medium ONLYOFFICE confirmed on October 23, 2026 that all five findings were fixed in Document Server 10.0. The changelog describes the release's security changes. Proof

### Cluster fb549f1298 — score 21

- Title: Critical Apache Roller RCE Flaw Under Active Exploitation, No Authentication Required
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-18T17:10:45+00:00
- Link: https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-129448

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor, zero_day
- affected_industries: financial_services, telecommunications
- affected_products: AWS, Google Cloud, Linux kernel
- cve_ids: CVE-2026-118383, CVE-2026-129448, CVE-2026-82384
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor, active_exploitation
- affected_industries: financial_services, telecommunications
- affected_products: AWS, Linux kernel, Google Cloud
- cve_ids: CVE-2026-129448, CVE-2026-82384, CVE-2026-118383
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical security flaw in Apache Roller, an open-source, Java-based blogging platform, has come under active exploitation in the wild, according to the Apache Software Foundation (ASF) The vulnerability, tracked as CVE-2026-129448 (CVSS score: 9.8), is a case of unauthenticated deserialization in the XML-RPC endpoint that could lead to remote code execution. "Deserialization of Untrusted
```

#### Full body

```
Critical Apache Roller RCE Flaw Under Active Exploitation, No Authentication Required  Ravie Lakshmanan  Nov 18, 2026 Vulnerability / Cyber Attack A critical security flaw in Apache Roller , an open-source, Java-based blogging platform, has come under active exploitation in the wild, according to the Apache Software Foundation (ASF) The vulnerability, tracked as CVE-2026-129448 (CVSS score: 9.8), is a case of unauthenticated deserialization in the XML-RPC endpoint that could lead to remote code execution. "Deserialization of Untrusted Data in Apache Roller versions 4.0.0 through 6.1.4 allows an unauthenticated remote attacker to execute arbitrary code," project maintainers said . "The XML-RPC endpoint accepts vendor extension types and deserializes them before authenticating the requester." ASF also noted that the vulnerability is the same as CVE-2026-82384 (CVSS score: 9.8), which was patched in September 2026 and listed only Apache Roller 6.1.5 as affected. "This issue is being actively exploited," it added. ASF did not share any details on how the vulnerability is being exploited, or who is being targeted as part of these efforts. A security researcher named n0mi1k has been credited with finding the flaw, and Matt Raible has been acknowledged for reporting it. Users are advised to upgrade to Apache Roller 6.1.6 or later, which disables the extension types and rejects XML-RPC requests when the XML-RPC feature is disabled. If immediate patching is not an option, it's recommended to set "enabledForExtensions" to "false" in WEB-INF/web.xml, or remove the "/roller-services/xmlrpc" servlet mapping, and then restart Roller. "Disabling XML-RPC in the administration UI is not enough, because older versions deserialize the request before checking that setting," ASF noted. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Apache , Application Security , Cyber Attack , Insecure Deserialization , remote code execution , Vulnerability ⚡ Top Stories This Week Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs FBI Says North Korean Hackers Stole Over $400 Million in Crypto Using Deepfake Video Calls SilentAir Hijacks Asian Telecom Networks to Intercept SMS 2FA Codes and Spy on Taiwanese Users Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More Stories New SignDrop Zero-Day Exploit Turns Windows CLFS Security Feature Into SYSTEM Access Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass Critical Red Hat Quay Flaw Lets Attackers Read and Overwrite All Private Container Images in a Registry Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across Processes in VMs New N-central Exploits Work Against Patched Servers, Enable Root RCE and Windows SYSTEM Access Critical Pre-Auth MongoDB Flaw (CVE-2026-118383) Can Crash Lagging Servers on Failover Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely AntiFox AI Pentesting Platform Linked to Attacks That Accessed AWS Production Secrets Over 35,000 Grok-Built Apps Exposed Online, Some Leaking Confidential Data and Passwords Microsoft Patches 1,259 Flaws, Including Exploited Outlook Bug That May Expose NTLMv2 Hashes Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches SGLang RCE Exploit Breaches NEAR AI, Steals Data From 18 Agents and About 100 Users Hackers Exploit Critical Xen Orchestra Auth Bypass Flaw to Gain Admin Access Binance War
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Apache Roller RCE Flaw Under Active Exploitation, No Authentication Required
  - Published: 2026-11-18T17:10:45+00:00
  - Link: https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html
  - Summary: A critical security flaw in Apache Roller, an open-source, Java-based blogging platform, has come under active exploitation in the wild, according to the Apache Software Foundation (ASF) The vulnerability, tracked as CVE-2026-129448 (CVSS score: 9.8), is a case of unauthenticated deserialization in the XML-RPC endpoint that could lead to remote code execution. "Deserialization of Untrusted

### Cluster 41a2f8271e — score 19

- Title: Exploited Puppet flaw puts the server that configures your endpoint fleet at risk (CVE-2026-115731)
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-11-19T13:07:41+00:00
- Link: https://www.helpnetsecurity.com/2026/11/19/puppet-enterprise-vulnerability-cve-2026-115731-exploited/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-115731

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: GitHub
- cve_ids: CVE-2026-115731, CVE-2026-115732
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: GitHub
- cve_ids: CVE-2026-115731, CVE-2026-115732
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Attackers are exploiting CVE-2026-115731, a critical remote code execution vulnerability in Perforce Puppet Enterprise, an enterprise solution used by IT teams to centralize and automatize endpoint management. Details about the in-the-wild attacks have yet to be made public, but the US Cybersecurity and Infrastructure Security Agency (CISA) added the flaw to its Known Exploited Vulnerabilities catalog on Tuesday and ordered US federal civilian agencies to address it by December 1, 2026. Perforce Puppet explained Perforce … More → The post Exploited Puppet flaw puts the server that configures your endpoint fleet at risk (CVE-2026-115731) appeared first on Help Net Security .
```

#### Full body

```
Zeljka Zorz , Editor-in-Chief, Help Net Security November 19, 2026 Share Exploited Puppet flaw puts the server that configures your endpoint fleet at risk (CVE-2026-115731) Attackers are exploiting CVE-2026-115731, a critical remote code execution vulnerability in Perforce Puppet Enterprise, an enterprise solution used by IT teams to centralize and automatize endpoint management. Details about the in-the-wild attacks have yet to be made public, but the US Cybersecurity and Infrastructure Security Agency (CISA) added the flaw to its Known Exploited Vulnerabilities catalog on Tuesday and ordered US federal civilian agencies to address it by December 1, 2026. Perforce Puppet explained Perforce Puppet works on a client-server model: a central Puppet Server holds the configuration code that describes how each managed machine should be set up, and a Puppet agent installed on every endpoint periodically checks in with the server, retrieves its configuration and applies it. Agents and server authenticate each other with certificates issued by the Puppet Server’s own certificate authority (CA). About CVE-2026-115731 CVE-2026-115731 is a deserialization of untrusted data vulnerability in Puppet’s report-processing code, i.e., the part of Puppet Server that ingests the reports agents send back after each configuration run. A client holding any certificate signed by the Puppet CA can submit a report containing a crafted rich-data type via a PUT request and get the server to execute arbitrary code with the privileges of the Puppet Server service user, CISA explained. It might seem that requiring a signed agent certificate is a meaningful barrier to exploitation, but if the CA signs certificate requests without strong verification (e.g., when autosigning is enabled) an unauthenticated attacker on the network could obtain a certificate and exploit the flaw. “If exploited, this vulnerability could allow an attacker to run arbitrary code on the Puppet Server with the privileges of its service account. This could give the attacker access to sensitive data held on the server (Confidentiality), let them modify data and configuration on the server (Integrity), or disrupt the service (Availability),” Centre for Cybersecurity Belgium noted . Patch and check for evidence of compromise CVE-2026-115731 affects : Puppet Enterprise 2023.8.0 before 2023.8.13, 2025.0.0 before 2025.12.1, and 2026.0.0 before 2026.0.1 Puppet Core 8.x before 8.22.2 and 9.0.0 before 9.1.3 OpenVox, a community-maintained open-source Puppet fork, is also affected: OpenVox Agent versions before 9.3.0 and 8.32.0 and OpenVox Server versions before 9.2.0 and 8.18.0 are vulnerable. Perforce released security updates fixing CVE-2026-115731 and CVE-2026-115732, a certificate name authorization bypass flaw that was also reported by Alain Rödel of Neodyme AG, on November 3. “Customers should upgrade to the latest applicable security release and then restart the server as soon as possible. Fixed versions are Puppet Enterprise/Advanced 2026.0.1, 2025.12.1, or 2023.8.13, and Puppet Core 9.1.3 or 8.22.2,” the company said and advised customers who are unable to upgrade immediately to review their autosign configuration and authorization rules as a temporary mitigation. Patching should be a priority for any organization that relies on autosigning or whose Puppet Server is reachable from untrusted networks (it listens on port 8140 by default). Admins should also check the list of signed certificates for nodes they don’t recognize and look for unexpected processes, files or outbound connections tied to the Puppet Server service user. If the server shows signs of compromise, patching is not enough: the CA should be treated as compromised and rebuilt. The OpenVox project’s GitHub advisory , published alongside the fixes, includes a proof-of-concept malicious report (in the form of a JSON event) that runs a shell command on the OpenVox / Puppet server. “In configuration with autosign (which is comm
```

#### Corroborating sources (2)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Exploited Puppet flaw puts the server that configures your endpoint fleet at risk (CVE-2026-115731)
  - Published: 2026-11-19T13:07:41+00:00
  - Link: https://www.helpnetsecurity.com/2026/11/19/puppet-enterprise-vulnerability-cve-2026-115731-exploited/
  - Summary: Attackers are exploiting CVE-2026-115731, a critical remote code execution vulnerability in Perforce Puppet Enterprise, an enterprise solution used by IT teams to centralize and automatize endpoint management. Details about the in-the-wild attacks have yet to be made public, but the US Cybersecurity and Infrastructure Security Agency (CISA) added the flaw to its Known Exploited Vulnerabilities catalog on Tuesday and ordered US federal civilian agencies to address it by December 1, 2026. Perforce Puppet explained Perforce … More → The post Exploited Puppet flaw puts the server that configures your endpoint fleet at risk (CVE-2026-115731) appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hackers Exploiting Critical Puppet RCE Flaw Affecting Enterprise Management Servers
  - Published: 2026-11-18T08:24:31+00:00
  - Link: https://thehackernews.com/2026/11/hackers-exploiting-critical-puppet-rce.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a critical security flaw impacting Perforce Puppet, an enterprise infrastructure-as-code (IaC) and configuration management platform, to its Known Exploited Vulnerabilities (KEV) catalog, citing reports of active exploitation. The vulnerability, tracked as CVE-2026-115731 (CVSS score: 9.4), is a case of

### Cluster 865bc835a9 — score 18

- Title: CVE-2026-84869 in ScreenConnect Exploited to Run Malicious Files on MSP Technician Accounts
- Source: Huntress (detection_response_operations)
- Published: 2026-11-16T18:00:00+00:00
- Link: https://www.huntress.com/blog/cve-2026-84869-screenconnect-technician-exploitation
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: CVE-2026-84869, ScreenConnect

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: financial_services
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, ScreenConnect
- cve_ids: CVE-2026-84869
- urgency_signals: no_patch_yet
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: financial_services
- affected_products: ScreenConnect, Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-84869
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Huntress confirmed CVE-2026-84869 exploitation against MSP technicians via ScreenConnect. See the attack chain, IOCs, and how to protect your team.
```

#### Full body

```
Home Blog CVE-2026-84869 in ScreenConnect Exploited to Run Malicious Files on MSP Technician Accounts Published: November 16, 2026 CVE-2026-84869 in ScreenConnect Exploited to Run Malicious Files on MSP Technician Accounts By: John Hammond Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways Huntress has confirmed in-the-wild exploitation of CVE-2026-84869, a ScreenConnect client flaw that allows a guest to run a malicious file on a connecting technician's host. On November 12, 2026, we observed one managed service provider's (MSP) technician's workstation exploited to run a guest-pushed batch file, which then reported to a Telegram bot, downloaded an installer from masterdarky[.]com , and started a rogue ScreenConnect client pointing at the attacker's own relay, all in about 9 seconds. On November 13, we observed a second technician's client run an attacker "canary" file. Our hunt found that in October, at least four more technicians were exposed to guest-pushed files, including a path-traversal attempt to drop Sync.bat into a technician's Startup folder. Attackers appear to be spraying servers blindly: Since October 20, we've seen at least 688,000 guest "run file" requests for update*.bat hit 42 MSP ScreenConnect servers from 29 IP addresses, waiting for any technician to join. We recommend updating every technician's ScreenConnect host client to 26.6.5 or later now, and hunting for the host client spawning scripts from its Temp folder. What Is CVE-2026-84869? ConnectWise disclosed CVE-2026-84869 on September 8, 2026, with a CVSS score of 9.9, and CISA added the CVE to its Known Exploited Vulnerabilities catalog on September 11. ConnectWise's advisory stated that in both Support and Access sessions, a guest could trigger file-transfer actions that the technician's host client processed without authorization or confirmation, including running the file with elevated rights. ConnectWise listed 26.6.5 as the fixed version for host clients and Access agents, and recommended removing the TransferFiles permission as an interim mitigation. Figure 1: CVE-2026-84869 file transfer spray campaign by the numbers In the days leading up to CVE-2026-84869's disclosure, Huntress stood up a Rapid Response to worm-like activity that spawned rogue ScreenConnect clients and dropped malicious VBScript files across several customer environments. On November 11, we stood up another Rapid Response to more worm-like activity where an attacker used Run commands on cloud-hosted panels to install rogue ScreenConnect clients and session-cookie relays on hundreds of managed endpoints. The malware, called SCKit, appears to be leveraging a vulnerable third-party extension on the server side of ScreenConnect and not directly exploiting CVE-2026-84869, but attempting to stage it as a "relay trap" for subsequent technician connections. This most recent activity is distinct from a separate campaign we reported on November 13 that planted unauthorized guest sessions disguised with crypto exchange names on more than 100 MSP ScreenConnect servers. While we did not observe the attacker using the unauthorized sessions in this manner, the crypto exchange names may be intended to lure a technician into opening the session and running a malicious file on their client. An MSP technician's workstation typically holds RMM consoles, saved credentials, and access to every customer, making it an exceptionally attractive target. When a technician joins a remote session, their ScreenConnect host client and the guest machine can exchange files. Normally, the technician decides what moves and what runs. A malicious guest exploiting CVE-2026-84869 can push a file to the technician's machine and get the technician's own client to run it. From the technician's view, no prompt appears. They only have to join the session, whether from an attacker-controlled machine or a real customer's support session that the attacker has slipped into as an extra guest. Hunt
```

#### Corroborating sources (2)

- **Huntress** (detection_response_operations)
  - Title: CVE-2026-84869 in ScreenConnect Exploited to Run Malicious Files on MSP Technician Accounts
  - Published: 2026-11-16T18:00:00+00:00
  - Link: https://www.huntress.com/blog/cve-2026-84869-screenconnect-technician-exploitation
  - Summary: Huntress confirmed CVE-2026-84869 exploitation against MSP technicians via ScreenConnect. See the attack chain, IOCs, and how to protect your team.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ConnectWise Warns ScreenConnect Attacks Continue as SCKit Targets Unpatched Systems
  - Published: 2026-11-17T06:29:27+00:00
  - Link: https://thehackernews.com/2026/11/connectwise-warns-screenconnect-attacks.html
  - Summary: ConnectWise on Monday said it completed its investigation into unauthorized access targeting partner ScreenConnect environments, and recommended customers to ensure that the technician client is running version 26.6.5 or later. The company said additional activity targeting on-premises environments continues to be reported where the identified third-party extensions remain enabled and

### Cluster b9147f3603 — score 17

- Title: Borrowed Code, Real Consequences: What OPTIMJACK Teaches Us
- Source: Unit 42 (threat_research_primary)
- Published: 2026-11-17T20:43:14+00:00
- Link: https://unit42.paloaltonetworks.com/optimjack-supply-chain-attack/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The OPTIMJACK supply chain attack demonstrates how a compromised vendor script can expose websites, highlighting the need for strict segmentation. The post Borrowed Code, Real Consequences: What OPTIMJACK Teaches Us appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights General General Borrowed Code, Real Consequences: What OPTIMJACK Teaches Us 3 min read Related Products Unit 42 Incident Response By: Sherrod DeGrippo Published: November 17, 2026 Categories: General Insights Tags: JavaScript Malicious injection attack Payload Software supply-chain attack Share Introduction On Nov. 16, 2026, a threat actor exploited a vulnerability in Optimizely's Web Experimentation platform to inject malicious JavaScript into customer accounts. Nicknamed OPTIMJACK, this campaign delivered that code to visitors of at least 178 organizations' websites. The tampered code was delivered directly from the vendor's legitimate content delivery network (CDN), under the vendor's own security certificate. Enterprises invest heavily in hardening their core web infrastructure. A single compromised third-party tool can undermine that work. OPTIMJACK is a reminder that any vendor script with dynamic execution privileges on your site is part of your direct production code. Threat actors know that third-party apps are the path of least resistance into lucrative environments. Defenders can respond with a fundamental principle that security engineering has relied on from the beginning: segmentation. What Happened in OPTIMJACK On Nov. 16th, 2026, the attacker exploited the vulnerability to place malicious JavaScript in the custom Project JavaScript field of customer accounts. Because the tampered snippets were served from the vendor's legitimate CDN under its own certificate, at least 178 organizations, including well-known media, technology and financial services brands, unknowingly served the code to their visitors. Once the code loaded in a visitor's browser, it did three things: Cryptocurrency wallet swapping: It replaced wallet addresses that visitors copied with the attacker's own Payment card skimming: It collected card details from checkout forms Mobile exploit delivery: It attempted to deliver the Coruna and DarkSword exploit kits to iPhones and iPads Optimizely patched the flaw, removed the injected code and secured affected accounts early on November 17. Trusted Vendors Are the Path of Least Resistance Websites are not a single monolith. They are dynamic assemblies of dozens of third-party scripts, analytics tags and optimization tools. That diversity drives speed, but it also introduces new vectors of attack through the software supply chain. When attackers compromise a single trusted vendor upstream, they bypass the perimeter defenses that vendor's customers have built. The choice of malicious payload also matters. Swapping valid cryptocurrency wallet addresses on a page is a quick and persistent way to direct ill-gotten payments to a threat actor. Segmentation Is the Strongest Step Available Today If a third-party script executes on your page, it effectively has the same privileges as your own developers. Organizations need to architect their sites with that assumption in mind. The best thing security teams can do right now is apply strict segmentation. The goal is simple— a compromised vendor script should never be able to touch sensitive user inputs. Methods of accomplishing this goal include: Remove non-essential tags from sensitive pages: Strip all non-essential marketing, experimentation and analytics tags from authentication and checkout pages Isolate payment collection: Place payment collection inside hardened, cross-origin iframes Segmentation has been a cornerstone of good security engineering since the beginning. What Affected Organizations Should Know Even with the flaw patched, affected websites still need to act. Security teams should take these steps now: Audit all project modifications made while the malicious code was available Double-check all code that may have been altered during that period Treat exposed payment data as potentially compromised, including payment card details entered into checkout forms on affected pages Conclusion OPTIMJACK is a reminder that any
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Borrowed Code, Real Consequences: What OPTIMJACK Teaches Us
  - Published: 2026-11-17T20:43:14+00:00
  - Link: https://unit42.paloaltonetworks.com/optimjack-supply-chain-attack/
  - Summary: The OPTIMJACK supply chain attack demonstrates how a compromised vendor script can expose websites, highlighting the need for strict segmentation. The post Borrowed Code, Real Consequences: What OPTIMJACK Teaches Us appeared first on Unit 42 .

### Cluster e32ee3fa56 — score 17

- Title: Breaking: “ruby2ßhell” or ruby2shell One-Byte Heap Overflow in Ruby Could Allow Remote Code Execution in Rails and Popular Self-Hosted Apps
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-11-19T10:56:26+00:00
- Link: https://orca.security/resources/blog/ruby2shell-ruby-heap-overflow-rce/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-132825

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: GitHub, GitLab
- cve_ids: CVE-2026-132825
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: GitHub, GitLab
- cve_ids: CVE-2026-132825
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A heap-based buffer overflow in Ruby’s string case conversion, tracked as CVE-2026-132825 and dubbed “ruby2ßhell”, has been disclosed. The Ruby core team rates the issue critical and states that changing the case of a crafted string may allow remote code execution, adding that it is aware of proof-of-concept exploits that can trigger code execution in […]
```

#### Full body

```
A heap-based buffer overflow in Ruby’s string case conversion, tracked as CVE-2026-132825 and dubbed “ruby2ßhell”, has been disclosed. The Ruby core team rates the issue critical and states that changing the case of a crafted string may allow remote code execution, adding that it is aware of proof-of-concept exploits that can trigger code execution in some scenarios. Fixed versions, Ruby 3.3.14, 3.4.13 and 4.0.10, were released on November 18, 2026. Ruby powers a large number of web applications and widely used self-hosted platforms. According to the researchers who published the ruby2ßhell write-up, the flaw is reachable without authentication in default Ruby on Rails and classic-style Sinatra applications, as well as in self-hosted software such as GitLab, GitHub Enterprise Server, Mastodon and Discourse. The vulnerable code has been present since Ruby 2.4.0. The same Ruby release also fixes six additional memory-safety vulnerabilities in Ruby’s regular expression engine and string case conversion. ruby2ßhell (CVE-2026-132825): key facts Fact Detail CVE CVE-2026-132825 (GitHub advisory GHSA-34m4-m9fh-gqp5) Type One-byte heap-based buffer overflow (CWE-122 / CWE-193) in string case conversion Severity Rated critical by the Ruby core team; NVD score pending Trigger Changing the case (e.g., upcase) of a crafted string in certain single-byte encodings, such as ISO-8859-1 or Windows-1252; UTF-8 strings are not affected Affected Ruby versions 3.3.13 and earlier; 3.4.0 to 3.4.12; 4.0.0 to 4.0.9 (end-of-life versions back to 2.4.0, according to the researchers) Fixed Ruby versions 3.3.14, 3.4.13, 4.0.10 (released November 18, 2026) Exposure According to the researchers: reachable without authentication in default Rails and classic-style Sinatra apps, and in GitLab, GitHub Enterprise Server, Mastodon, Discourse and other self-hosted software Workaround None published; upgrade Ruby (and self-hosted software that bundles Ruby) Exploitation No known in-the-wild exploitation; the Ruby team is aware of non-public PoCs, and the researchers plan to publish a PoC about a week after disclosure What is ruby2ßhell (CVE-2026-132825)? The flaw is in how Ruby converts the case of strings in several single-byte encodings, including ISO-8859-1, ISO-8859-2 and other ISO-8859 variants, and Windows-1250, Windows-1252, Windows-1254 and Windows-1257. In these encodings, the German sharp s (“ß”, byte 0xDF) becomes two characters (“SS”) when upper-cased, but Ruby checked for only one byte of room in the output buffer. A crafted string containing enough of these characters makes Ruby write one byte past the end of a heap buffer. The researchers note that the issue can be reached through upcase, swapcase, downcase(:fold) and casecmp?, while UTF-8 strings take a different code path and are not affected. Although the overflow is only a single byte, heap memory corruption of this kind can be leveraged for code execution. The Ruby core team states that it is aware of PoCs that use the flaw to trigger remote code execution in some scenarios. The Ruby team rates the advisory critical, and the researchers describe unauthenticated remote exposure in common frameworks; organizations should treat internet-facing Ruby applications as at risk. Which Ruby versions are affected? Ruby branch Affected versions Fixed version Ruby 4.0 4.0.0 to 4.0.9 4.0.10 Ruby 3.4 3.4.0 to 3.4.12 3.4.13 Ruby 3.3 3.3.13 and earlier 3.3.14 Ruby 3.2 and earlier Affected (back to 2.4.0, according to the researchers) No fix: end of life, upgrade to a supported branch Ruby 3.2 and earlier have reached end of life and will not receive these fixes. Ruby is often bundled inside applications and container images, so self-hosted platforms (such as GitLab, GitHub Enterprise Server, Mastodon, Discourse, OpenProject and Chatwoot, which the researchers list as affected in their latest versions at the time of disclosure) need their own vendor updates. Linux distributions may ship the fix as a patched packag
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Breaking: “ruby2ßhell” or ruby2shell One-Byte Heap Overflow in Ruby Could Allow Remote Code Execution in Rails and Popular Self-Hosted Apps
  - Published: 2026-11-19T10:56:26+00:00
  - Link: https://orca.security/resources/blog/ruby2shell-ruby-heap-overflow-rce/
  - Summary: A heap-based buffer overflow in Ruby’s string case conversion, tracked as CVE-2026-132825 and dubbed “ruby2ßhell”, has been disclosed. The Ruby core team rates the issue critical and states that changing the case of a crafted string may allow remote code execution, adding that it is aware of proof-of-concept exploits that can trigger code execution in […]

### Cluster dff990f28a — score 17

- Title: NGINX2Root: Five RCE bugs in NGINX, a Linux kernel path to root, and how to detect exploitation
- Source: Sysdig (detection_response_operations)
- Published: 2026-11-19T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/nginx2root
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: Linux kernel

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Linux kernel
- cve_ids: CVE-2026-113425, CVE-2026-121810, CVE-2026-123007, CVE-2026-123633, CVE-2026-123634
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Linux kernel
- cve_ids: CVE-2026-123633, CVE-2026-123007, CVE-2026-123634, CVE-2026-121810, CVE-2026-113425
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
threat-research This is some text inside of a div block. < back to blog NGINX2Root: Five RCE bugs in NGINX, a Linux kernel path to root, and how to detect exploitation Published by: Sysdig Threat Research Team @ linkedin Subscribe to Threat Research Read more research Published: November 19, 2026 Table of contents TRT in your inbox Get security briefings from the Threat Research Team New campaigns, attacker techniques, and detection guidance — straight to your inbox. Subscribe falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more On November 18, 2026, F5 published CVE records for five memory-safety bugs in NGINX, and the project shipped fixes the same day in NGINX 1.31.9 (mainline) and 1.30.7 (stable). Each bug allows an unauthenticated remote attacker to corrupt memory in an NGINX worker process, and all five carry a CVSS 4.0 score of 9.2. Xint, one of the teams that reported the bugs, published a write-up dubbing the set of vulnerabilities “NGINX2Root.” Xint also chained one of the NGINX bugs with a previously unknown Linux kernel bug in the Stream Control Transmission Protocol (SCTP) to get root on the host, including from inside a Docker container running the official NGINX image. At the time of publication for this blog, there has been no public proof-of-concept (PoC) or reported in-the-wild exploitation. However, several teams found the HTTP/2 bugs independently, and both Xint and Wiz researchers say they’ve built working exploits that bypass address space layout randomization (ASLR). Also, the Linux kernel bug has not yet been assigned a CVE, nor has a fix been released. The Sysdig Threat Research Team (TRT) reviewed the disclosures and tested post-exploitation activity in a lab to help defenders understand who is exposed, what they can do before a fixed package reaches every host, and what runtime detection can see. This blog covers the five NGINX bugs, the kernel half of the chain, and what defenders can do now. Timeline All dates are in UTC. Date Event Oct. 11 Xint finds the vulnerabilities. Oct. 16 Xint reports them to F5 through HackerOne. Oct. 21 Wiz Research reports confirmed remote code execution (RCE), with an ASLR bypass, for CVE-2026-123633 to F5. Oct. 27 Xint's reports reach the NGINX development team. Nov. 10 Xint finishes validating the patches. Nov. 18 F5 publishes the five CVE records, NGINX 1.31.9 and 1.30.7 are released, and Xint and Wiz publish their research. Nov. 18 Debian and Ubuntu list every supported release as vulnerable, with no fixed package yet. The vulnerabilities and affected NGINX versions CVE Component Reachable when NGINX rating Vulnerable (NGINX Open Source) CVE-2026-123007 HTTP/2 flow control: integer underflow leading to a heap buffer overflow HTTP/2 is enabled Major 1.9.5 – 1.31.8 CVE-2026-123633 HTTP/2 use-after-free HTTP/2 is enabled, requests are proxied to an upstream, and the worker is low on worker_connections Medium 1.19.7 – 1.31.8 CVE-2026-123634 Resolver use-after-free The proxied server name uses variables, and an SSI or mirror subrequest resolves the same name Medium 0.6.18 – 1.31.8 CVE-2026-121810 HTTP/3 use-after-free HTTP/3 (QUIC) is enabled and requests are proxied to an upstream Medium 1.25.0 – 1.31.8 CVE-2026-113425 Mail proxy use-after-free The mail proxy runs with proxy on and auth_http Major 0.5.33 – 1.31.8 All five CVE records have been assigned the same scores: 8.1 (High) on CVSS 3.1 and 9.2 (Critical) on CVSS 4.0. NGINX2Root is network-based, doesn’t require authentication, and is relatively complex. F5 describes the impact as a worker crash or memory corruption, with code execution where ASLR is disabled or can be bypassed. All five are data-plane bugs, and F5 states there is no control-plane exposure. The fixed releases are NGINX 1.31.9 and 1.30.7. For NGINX Plus, they are 37.3.0.1 and 37.0.8.1 (37.2.0.1 and 37
```

#### Corroborating sources (4)

- **Sysdig** (detection_response_operations)
  - Title: NGINX2Root: Five RCE bugs in NGINX, a Linux kernel path to root, and how to detect exploitation
  - Published: 2026-11-19T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/nginx2root
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Critical NGINX ‘NGINX2Root’ bugs let attackers hijack servers
  - Published: 2026-11-19T14:57:24+00:00
  - Link: https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/
  - Summary: Two critical NGINX vulnerabilities dubbed "nginx2root" allow unauthenticated attackers to execute code remotely on vulnerable web servers, with researchers demonstrating how the flaws can be chained with a Linux kernel bug to gain root access. [...]
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Sashiko: Lessons from building an agentic code review system for Linux
  - Published: 2026-11-18T17:00:00+00:00
  - Link: https://cloud.google.com/blog/products/application-development/lessons-from-building-sashiko-an-agentic-code-review-system/
  - Summary: The speed of development in large open-source projects has always been limited by code review, not code generation. Even as coding agents get better at writing code, they do not accelerate development on their own. This is especially true of patches to the Linux kernel. Without a way to build trust in proposed changes, more generated code simply piles up in front of the same small group of human maintainers. Some of those patches are solid changes, just written faster; many others are plausible-looking "AI slop" sent by contributors who do not fully understand the systems they are modifying. And the influx of AI-generated security reports, many of which are duplicates or inaccurate, only adds to maintainers’ load. Linux runs billions of Android phones, most cloud providers, and nearly every supercomputer. It spans more than 35 million lines of code, and over 85,000 changes land every year. Automated build bots and fuzzers like Syzkaller catch build errors and crashes, but code review h
- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: What’s in the SOSS? Podcast #78 – S3E30 From Signal Processing to Open Source Security: Sal Kimmich on Linux Kernel Defense
  - Published: 2026-11-18T19:17:12+00:00
  - Link: https://openssf.org/podcast/2026/11/18/whats-in-the-soss-podcast-78-s3e30-from-signal-processing-to-open-source-security-sal-kimmich-on-linux-kernel-defense/
  - Summary: Discover kernel-level defense strategies, nono.sh sandboxing, and AI data security with security architect Sal Kimmich on What's in the SOSS? Podcast #78.

### Cluster 3a3ebdb83e — score 16

- Title: Operation ShadowCloud: cloud service–based backdoors targeting government networks in Asia and Africa. Part 2
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-17T08:00:43+00:00
- Link: https://securelist.com/operation-shadowcloud-graphdoor/122005/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_industries: government
- affected_products: Microsoft SharePoint
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_industries: government
- affected_products: Microsoft SharePoint
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Summary

```
In part 2 of our analysis of the recently uncovered Operation ShadowCloud, we discuss the GraphDoor backdoor, additional plug-ins, and technical attribution.
```

#### Full body

```
Content menu Close Subscribe Threat Response Table of Contents Introduction GraphDoor (MD5 14ec33ea808e697870d00c5e434c2952) Plug-ins Keylogger (kl.ts) Process Listing (pr.ts) Screenshot Capturing (scr.ts) Move Directory (moveDir.ts) Proxy Channel (channel.ts) Ably Channel (abchannel.ts) Ably2 Channel (ab2channel.ts) Attribution Infrastructure Conclusion Indicators of Compromise GraphDoor SharePoint site Proxy C2 server Cobalt Strike domains Authors Saurabh Sharma Noushin Shabab Introduction The first part of the blog focused on the initial infection chain, examined the GitDoor backdoor’s command‑and‑control protocol, and cataloged the diverse shellcode families the actors drop onto compromised hosts. In this part, we will walk through the GraphDoor backdoor and the suite of plug-ins loaded, including patched Erfrp and Ably proxy plug-ins, and highlight the attribution clues that tie the operation to Chinese‑speaking threat groups. GraphDoor (MD5 14ec33ea808e697870d00c5e434c2952) The malware begins by opening a named pipe that it will reuse for later communications, building the pipe’s name from its own PID in the form \\.\pipe\p%lu (where %lu is the process ID as an unsigned long integer). Once the backdoor contacts its C2 server and downloads the required plug-ins, those plug-ins write their status reports to the same pipe. After the pipe is set up, the backdoor creates a directory named Intel_Log inside the system’s ProgramData folder. Inside that folder, it generates a subdirectory whose name is a randomly generated GUID, yielding a full path like C:\ProgramData\Intel_Log\<random‑GUID> . Next, the malware starts gathering system information to send back to the attacker. It resolves the needed Windows APIs at runtime by hashing DLL and function names with the DJB2 algorithm. To invoke these APIs covertly, the backdoor installs a vectored exception handler that contains a miniature routine for the desired call, then deliberately raises an exception. The handler catches the exception, runs the routine, and thus calls the target API. Using this indirect call technique, the malware harvests the following information from the victim machine: Network adapter details Version of the operating system A randomly generated GUID for the infected machine Public IP Private IP Username Host name Current directory (where the backdoor is executed from) PID of its own module A list of all the running processes In addition to the victim information, the backdoor also decrypts a set of embedded configuration parameters (see the list below) and appends them to the victim data. The resulting information is then encrypted with AES, Base64‑encoded, and transmitted to the command‑and‑control server. "type":"serv" "client_version":"1.2.7" "dhj_exe":"javaw.exe" "execution_method":"normal" "is_need_lock":"false" The malware first opens a TLS connection to login.microsoftonline.com on port 443. Once the TLS handshake completes, it decrypts three hard‑coded, AES-encrypted strings. These values become the components of the authentication request: UUID path segment Client ID (application registration) Client secret It also generates a random X‑CSRF‑TOKEN, decrypts a preset User‑Agent string and several other hard-coded strings, and then issues a POST request to login.microsoftonline.com (see the example below). This call authenticates the malicious application – not a user – and returns an access token that the backdoor later uses to communicate with the Microsoft Graph API. POST /8f50c589-a4d6-4df4-95bb-2fb7f5983fe5/oauth2/v2.0/token HTTP/1.1 Host: login.microsoftonline.com Accept: application/json User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 Safari/537.36 X-CSRF-TOKEN: %Randomly generated value% Content-Length: %size of the data% Content-Type: application/x-www-form-urlencoded Connection: close "client_id=<redacted>&scope=https://graph.microsoft.com/.default&grant_type=client_credentia
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Operation ShadowCloud: cloud service–based backdoors targeting government networks in Asia and Africa. Part 2
  - Published: 2026-11-17T08:00:43+00:00
  - Link: https://securelist.com/operation-shadowcloud-graphdoor/122005/
  - Summary: In part 2 of our analysis of the recently uncovered Operation ShadowCloud, we discuss the GraphDoor backdoor, additional plug-ins, and technical attribution.

### Cluster 5fccd3b124 — score 16

- Title: High volume phishing campaign uses Microsoft 365 outage lures to target multiple industry sectors
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-11-17T00:08:41+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/11/16/high-volume-phishing-campaign-uses-microsoft-365-outage-lures-target-multiple-industry-sectors-2/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: Microsoft 365

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng
- affected_industries: government
- affected_products: Microsoft 365, Microsoft Defender, Microsoft Entra
- content_type: news_report
- confidence_tier: tier_1_government, tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft
- affected_products: Microsoft 365, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Threat Intelligence observed a high-volume phishing campaign using Microsoft 365 outage-themed lures to target organizations across multiple sectors worldwide. The post High volume phishing campaign uses Microsoft 365 outage lures to target multiple industry sectors appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Credential theft Incident Response Phishing Social engineering Threats intelligence Cyberattacker techniques, tools, and infrastructure Cybercrime Social engineering and phishing Content types Research Products and services Microsoft Defender Microsoft Defender for Office 365 Microsoft Defender XDR Topics Actionable threat insights Threat intelligence On November 13, 2026, Microsoft Threat Intelligence observed a coordinated, high-volume phishing campaign targeting organizations across multiple sectors worldwide. The threat actors used phishing emails disguised as legitimate Microsoft 365 service-health notifications to lure recipients into clicking a malicious link. The messages created a false sense of urgency by claiming that emails had been held during a service disruption and would be deleted within 24 hours unless the recipient took action to restore them. This is consistent with historical attacker campaigns which continuously look for notable global events to exploit in their social engineering lures. Microsoft identified the threat actor’s use of specific sender domain names, randomized outage subjects, recipient-specific tracking links, and a common non-Microsoft destination to make the messages appear relevant while complicating simple pattern matching. We assess that the activity was likely credential phishing; however, the available evidence does not confirm credential capture, malware delivery, or post-compromise activity. Multiple threat actors may continue to look for ways to exploit notable global events in any social engineering pretext. If credentials were entered, organizations should consider the risk of account compromise, mailbox access, business email compromise, internal phishing, inbox-rule manipulation, and access to cloud collaboration data. Microsoft Defender blocks malicious domains used in this campaign, and Microsoft Defender for Office 365 blocks and quarantines phishing emails. We will continue to monitor this campaign and other related threats. Security teams can use Microsoft Defender for Office 365 and Microsoft Defender XDR capabilities to investigate messages, URLs, clicks, and potential follow-on activity. Phishing attack overview Microsoft analyzed the email lures sent on November 13, 2026: the emails used the subject pattern “Outage – <random token>” and display names built from a three-character, organization-style prefix followed by “Outage Notification” or “Service Health.” Example subject line: Outage – aF7vG6 Example display names: MSF Outage Notification AMZ Service Health One example email body referenced a purported Exchange Online incident on November 12 and claimed that four messages were held after the outage. The urgency of a 24-hour deletion deadline and the prominent “RESTORE MESSAGES” call to action were intended to drive immediate interaction. The activity used distinct sender domains, including: moments-notice[.]com, planetmaison[.]com and newbooker[.]com. The messages also used email-delivery and link-tracking infrastructure to generate recipient-specific URLs. In multiple samples, click-tracking links led to reallifeaccounting[.]com or reallifeaccounting[.]com/themelist0.html. The sample set was link-based: no QR codes or non-EML attachments were observed, and Microsoft did not identify evidence of executable, archive, document, or other malware payload delivery. The off-brand destination and Microsoft 365 impersonation support an assessment of likely credential phishing, but the available evidence did not include the final page source, credential fields, credential-submission telemetry, or post-compromise activity. Microsoft therefore has not attributed the campaign to a named threat actor or malware family. Figure 1. Sample of one of the Microsoft 365 outage-themed phishing lures. Attack chain overview Figure 2. Observed attack chain for the Microsoft 365 outage-themed phishing campaign. Delivery: A user receives an email from t
```

#### Corroborating sources (5)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: High volume phishing campaign uses Microsoft 365 outage lures to target multiple industry sectors
  - Published: 2026-11-17T00:08:41+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/16/high-volume-phishing-campaign-uses-microsoft-365-outage-lures-target-multiple-industry-sectors-2/
  - Summary: Microsoft Threat Intelligence observed a high-volume phishing campaign using Microsoft 365 outage-themed lures to target organizations across multiple sectors worldwide. The post High volume phishing campaign uses Microsoft 365 outage lures to target multiple industry sectors appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: High volume phishing campaign uses Microsoft 365 outage lures to target multiple industry sectors
  - Published: 2026-11-17T00:08:41+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/16/high-volume-phishing-campaign-uses-microsoft-365-outage-lures-target-multiple-industry-sectors-2/
  - Summary: Microsoft Threat Intelligence observed a high-volume phishing campaign using Microsoft 365 outage-themed lures to target organizations across multiple sectors worldwide. The post High volume phishing campaign uses Microsoft 365 outage lures to target multiple industry sectors appeared first on Microsoft Security Blog .
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Java4Shell, NGINX2Shell and more: Why we are not at "Yellow", (Wed, Nov 18th)
  - Published: 2026-11-18T19:54:50+00:00
  - Link: https://isc.sans.edu/diary/rss/33532
  - Summary: About a month ago, we went to Infocon Yellow for the first time in a few years. We decided to address the php2shell vulnerability and alert our readers to its significant impact. Following php2shell, we had a number of vulnerabilities and events that may also have scored high enough to trigger an Infocon "Yellow" [infocon]. In the last few days, we had a major Microsoft 365 outage, a critical vulnerability in Java, and a critical vulnerability in NGINX, which was disclosed today.
- **Huntress** (detection_response_operations)
  - Title: Huntress Delivers 24/7 Response for Microsoft Defender Incidents Across Endpoints and Microsoft 365
  - Published: 2026-11-17T14:00:00+00:00
  - Link: https://www.huntress.com/blog/huntress-response-for-microsoft-defender-incidents-across-endpoints-and-microsoft-365
  - Summary: The Huntress Agentic Security Platform now sees incidents from Defender for Identity, Defender for Office 365, Defender for Cloud Apps, and Entra ID Protection. The new data already helped uncover a token-replay campaign that hit 97 accounts at 79 organizations.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Rubrik Configuration Resilience rolls back unauthorized Microsoft 365 changes
  - Published: 2026-11-19T10:56:44+00:00
  - Link: https://www.helpnetsecurity.com/2026/11/19/rubrik-configuration-resilience-for-microsoft-365/
  - Summary: Rubrik announced Configuration Resilience for Microsoft 365, a new offering that protects the key settings governing Microsoft applications such as Microsoft 365, Purview and Defender, and rolls back changes to them with a single action. By continuously safeguarding Microsoft 365 configurations, Rubrik equips organizations with a one-click undo button to reverse unauthorized system modifications before attackers can steal sensitive data. Rubrik Security Cloud handles recovery of identity, configuration and data for Microsoft 365 from a … More → The post Rubrik Configuration Resilience rolls back unauthorized Microsoft 365 changes appeared first on Help Net Security .

### Cluster 8002a9fab4 — score 14

- Title: phpAfterShell and Critical PHP RCE Vulnerabilities: Everything You Need To Know
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-11-19T21:46:23+00:00
- Link: https://www.wiz.io/blog/phpaftershell-critical-php-rce-vulnerabilities-cve-2026-126714
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-126714, CVE-2026-129289
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-126714, CVE-2026-129289
- urgency_signals: actively_exploited, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Detect and mitigate phpAfterShell, and additional critical vulnerabilities from PHP's November release that may enable remote code execution.
```

#### Full body

```
On November 19, 2026, the PHP group published security updates addressing 17 vulnerabilities across all actively supported branches (PHP 8.2, 8.3, 8.4, and 8.5). Seven of these flaws are rated Critical (CVSS 9.2) and present direct pathways to unauthenticated remote code execution (RCE). Security teams are advised to identify and patch exposed PHP deployments, as earlier mitigation efforts implemented during October's response to "PHP2Shell" do not provide protection against all of these new exploit vectors. As of yet, no exploitation in the wild has been observed by Wiz or mentioned in public reporting. What are these vulnerabilities? phpAfterShell: File-Based Session Handling (CVE-2026-126714) Reported by depthfirst, this vulnerability exists in PHP’s default file-based session handler ( session.save_handler = files ). When PHP writes session update progress (such as during unauthenticated file uploads), the file-write process is not atomic. If a PHP worker process is abruptly stopped during this write, due to memory limits or timeout settings, it can leave behind a partially written, malformed session file. When a subsequent request calls session_start() , PHP attempts to deserialize this file. If the file's contents are carefully structured, this deserialization process can be manipulated to trigger an object deserialization primitive. This behavior bypasses the initial parameters set during October's PHP2Shell patches, making a fresh update necessary to secure file-based session pipelines. PHP-FPM Request Smuggling (CVE-2026-129289) This issue centers on how PHP-FPM processes unread request-body bytes before reusing a persistent connection. In environments where the front-end web server (such as Nginx or Apache) is configured to keep FastCGI connections open to the FPM backend, an unauthenticated user can structure a request to append a secondary, hidden FastCGI request within the request body. Because the backend does not discard the leftover bytes, the subsequent request handled over that same connection executes the smuggled instructions. This allows a request to bypass front-end routing rules and execute with the privileges of the active FPM worker. Wiz Research data: what’s the risk to cloud environments? The overall risk depends largely on your environment's configuration. PHP remains widely used, powering approximately 70% of websites with known server-side languages. While the technical severity of these bugs is high, executing them successfully requires specific conditions. For instance, phpAfterShell (CVE-2026-126714) requires file-based sessions (the PHP default) and relies on finding an exploitable gadget chain in the application's code (which isn’t guaranteed to exist in every application) to achieve code execution. Importantly, the vast majority of the other critical vulnerabilities in this release require non-default configurations or uncommon setups, such as enabling runtime-mixed session serializers, enabling PHP 8.5 exception arguments ( zend.exception_ignore_args = 0 ), or writing startup warnings to a file-based error log on non-thread-safe builds. This ultimately means that default installations are naturally insulated from many of these vectors. Which products are affected? Affected Versions Patched Versions Support Status PHP 8.5 < 8.5.13 8.5.13 Active Support PHP 8.4 < 8.4.28 8.4.28 Active Support PHP 8.3 < 8.3.37 8.3.37 Active Support PHP 8.2 < 8.2.36 8.2.36 Security-only support (Ends December 2026) PHP 8.1 and earlier No Official Fix End-of-Life (EOL). These versions do not receive security backports. Which actions should security teams take? A. Plan a Routine Upgrade Plan to update your PHP installations to 8.5.13, 8.4.28, 8.3.37, or 8.2.36 (or 8.6.0). Rebuild affected container images and restart the PHP-FPM master service or web server process to ensure the newly patched binaries are active in memory. B. Temporary Configuration Adjustments (If patching is delayed) Disable Session Upload Progr
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: phpAfterShell and Critical PHP RCE Vulnerabilities: Everything You Need To Know
  - Published: 2026-11-19T21:46:23+00:00
  - Link: https://www.wiz.io/blog/phpaftershell-critical-php-rce-vulnerabilities-cve-2026-126714
  - Summary: Detect and mitigate phpAfterShell, and additional critical vulnerabilities from PHP's November release that may enable remote code execution.

### Cluster e329a9b51c — score 14

- Title: Microsoft Agent Framework PyPI Supply-Chain Attack: Versions 1.26.1 and 1.26.2 Steal Cloud Credentials
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-11-18T17:36:20+00:00
- Link: https://orca.security/resources/research/microsoft-agent-framework-pypi-supply-chain-attack-versions-1-26-1-and-1-26-2-steal-cloud-credentials/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: PyPI

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: Azure, PyPI
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: PyPI, Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A critical supply-chain compromise was discovered affecting Microsoft’s agent-framework PyPI meta-package, where versions 1.26.1 and 1.26.2 were injected with credential-stealing malware capable of harvesting cloud identity tokens, API keys, and sensitive credentials from developer workstations, CI/CD pipelines, and cloud build hosts. Due to the package’s approximately 190,000 monthly downloads and the breadth of targeted credentials, […]
```

#### Full body

```
A critical supply-chain compromise was discovered affecting Microsoft’s agent-framework PyPI meta-package, where versions 1.26.1 and 1.26.2 were injected with credential-stealing malware capable of harvesting cloud identity tokens, API keys, and sensitive credentials from developer workstations, CI/CD pipelines, and cloud build hosts. Due to the package’s approximately 190,000 monthly downloads and the breadth of targeted credentials, immediate remediation is required for any environment that installed the compromised versions. Agent-framework compromise at a glance Affected package: agent-framework on PyPI, versions 1.26.1 and 1.26.2 Last clean version: 1.26.0 Not affected: agent-framework-core and 22 other sibling packages Exposure window: November 17, 2026, 20:35 to approximately 21:20 UTC Payload: a Python .pth startup hook that harvests credentials on every interpreter launch Exfiltration: zlib-compressed, base64-encoded JSON posted to a webhook.site URL Status: malicious versions quarantined by PyPI; no CVE assigned What happened in the agent-framework supply-chain attack Both malicious versions were published within a 33-minute window on November 17, 2026 (20:35 to 21:08 UTC) and removed by approximately 21:20 UTC. The attack was entirely in packaging. Neither malicious release changed Agent Framework code or pulled in a rogue dependency. Instead, each version added a Python .pth startup hook file that executes on every Python interpreter launch, even if Agent Framework is never imported. How the .pth startup hook runs and evades detection The collector forks a detached background process, sets a flag to prevent re-execution in child processes, and silently harvests credentials. Version 1.26.2 restored the legitimate __init__.py byte-for-byte to evade diff-based detection while moving the payload to a new top-level module. What credentials does the agent-framework malware steal? The malware actively requested fresh credential tokens rather than only copying stored secrets. Targeted credentials include: Environment variables matching sensitive substrings (TOKEN, SECRET, KEY, AZURE, AWS, GITHUB, OPENAI, HF_, and more) from the current process and up to 300 other processes via /proc/*/environ Azure managed-identity tokens for 12 Azure resources (ARM, Microsoft Graph, Key Vault, Storage, ML, AI Foundry, Container Registry, Azure DevOps) via IMDS and identity endpoints Azure DevOps SYSTEM_ACCESSTOKEN and OIDC tokens for federated identity GitHub Actions OIDC tokens (version 1.26.2 only) when workflows have id-token: write permissions Credential files including Azure CLI state, .npmrc, pip.conf, .netrc, .git-credentials, Docker config.json, Hugging Face tokens, and .env files All harvested data was exfiltrated via zlib-compressed, base64-encoded JSON posted to a webhook.site URL. Which agent-framework versions and environments are affected? The following components are affected: agent-framework versions 1.26.1 and 1.26.2 on PyPI. The last clean version is 1.26.0. The dependency agent-framework-core and 22 other sibling packages were checked and are not affected. Any environment that installed the compromised versions during the exposure window is at risk, including through loose version pins such as agent-framework>=1.26. This spans developer workstations, CI/CD pipelines (Azure DevOps, GitHub Actions), and cloud build hosts running Python. At the time of writing, the malicious versions have been quarantined by PyPI and the Microsoft publisher account has been secured. No CVE has been assigned. Why stolen cloud and CI/CD credentials raise the stakes Successful exploitation allows attackers to obtain cloud identity tokens that grant access to Azure resources, steal CI/CD pipeline secrets that could enable lateral movement across repositories and infrastructure, and harvest stored credentials that could lead to full infrastructure compromise across multiple cloud providers. The attack also demonstrates sophisticated evasion tec
```

#### Corroborating sources (3)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Microsoft Agent Framework PyPI Supply-Chain Attack: Versions 1.26.1 and 1.26.2 Steal Cloud Credentials
  - Published: 2026-11-18T17:36:20+00:00
  - Link: https://orca.security/resources/research/microsoft-agent-framework-pypi-supply-chain-attack-versions-1-26-1-and-1-26-2-steal-cloud-credentials/
  - Summary: A critical supply-chain compromise was discovered affecting Microsoft’s agent-framework PyPI meta-package, where versions 1.26.1 and 1.26.2 were injected with credential-stealing malware capable of harvesting cloud identity tokens, API keys, and sensitive credentials from developer workstations, CI/CD pipelines, and cloud build hosts. Due to the package’s approximately 190,000 monthly downloads and the breadth of targeted credentials, […]
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Microsoft’s Agent Framework PyPI package compromised to steal credentials
  - Published: 2026-11-18T16:58:42+00:00
  - Link: https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/
  - Summary: Hackers compromised Microsoft's official Agent Framework Python package on PyPI, publishing two malicious versions designed to steal cloud credentials and other sensitive information from developers' systems. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials
  - Published: 2026-11-18T06:45:26+00:00
  - Link: https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html
  - Summary: Threat actors have compromised Microsoft's agent-framework package to push a credential stealer, according to reports from Aikido, Chainguard, Endor Labs, OX Security, SafeDep, Socket, StepSecurity, and Google-owned Wiz. The malicious versions, 1.26.1 and 1.26.2, were published 33 minutes apart on November 17, 2026, and are designed to run a credential stealer on every Python start. As of

### Cluster caf7a0d960 — score 12

- Title: YARA-X 1.23.0 Release, (Sun, Nov 15th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-11-15T18:17:27+00:00
- Link: https://isc.sans.edu/diary/rss/33496
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
YARA-X&#39&#x3b;s 1.23.0 release brings 4 improvements and 16 bugfixes.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: YARA-X 1.23.0 Release, (Sun, Nov 15th)
  - Published: 2026-11-15T18:17:27+00:00
  - Link: https://isc.sans.edu/diary/rss/33496
  - Summary: YARA-X&#39&#x3b;s 1.23.0 release brings 4 improvements and 16 bugfixes.

### Cluster 66ad4c7848 — score 12

- Title: What Is Preemptive MDR? A Guide For Security Leaders
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-19T15:58:53+00:00
- Link: https://www.rapid7.com/blog/post/dr-what-is-preemptive-mdr-security-leaders-guide
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
When an MDR provider contains a compromised endpoint, your team needs to know whether the weakness that enabled the attack exists elsewhere and who is responsible for addressing it. Without that follow-through, the immediate incident may be resolved while another attacker still has a way in. Preemptive managed detection and response (MDR) is Rapid7's approach to connecting exposure context, threat intelligence, AI-assisted investigation, and human expertise. It supports proactive cybersecurity by helping teams prioritize weaknesses before exploitation, investigate threats with a clearer understanding of risk, and use their findings to strengthen defenses. How does preemptive MDR differ from traditional MDR? Managed detection and response provides security specialists who monitor, investigate, and respond to threats around the clock. Many services also include proactive threat hunting and recommendations to improve security. Preemptive MDR connects that work more directly to what makes
```

#### Full body

```
MDR Must-Haves What Is Preemptive MDR? A Guide For Security Leaders Emma Burdett Nov 19, 2026 | Last updated on Nov 19, 2026 | 4 min read DISCOVER RAPID7 MDR What Is Preemptive MDR? A Guide For Security Leaders Table of contents What Is Preemptive MDR? A Guide For Security Leaders DISCOVER RAPID7 MDR Table of contents When an MDR provider contains a compromised endpoint, your team needs to know whether the weakness that enabled the attack exists elsewhere and who is responsible for addressing it. Without that follow-through, the immediate incident may be resolved while another attacker still has a way in. Preemptive managed detection and response (MDR) is Rapid7's approach to connecting exposure context, threat intelligence, AI-assisted investigation, and human expertise. It supports proactive cybersecurity by helping teams prioritize weaknesses before exploitation, investigate threats with a clearer understanding of risk, and use their findings to strengthen defenses. How does preemptive MDR differ from traditional MDR? Managed detection and response provides security specialists who monitor, investigate, and respond to threats around the clock. Many services also include proactive threat hunting and recommendations to improve security. Preemptive MDR connects that work more directly to what makes an organization vulnerable. When analysts investigate suspicious activity on a server, knowing that it is internet-facing, supports a critical application, and has a vulnerability under active exploitation helps them assess urgency and determine where to look next. In Rapid7’s model, exposure findings inform investigation and remediation priorities, while investigations reveal weaknesses that need attention. Security leaders gain a clearer connection between the threats their provider handles and the conditions their organization needs to address. Within a broader preemptive cybersecurity strategy, MDR connects exposure information with the people investigating and responding to threats. The aim is to reduce opportunities for compromise and intervene before an attack causes harm, while retaining the expertise to contain and recover from incidents. How exposure context and proactive threat hunting inform MDR By combining information about assets, vulnerabilities, business criticality, and attacker behavior, preemptive MDR helps teams decide which weaknesses require action first. Exposure context also informs targeted hunting and the investigation of suspicious activity. Consider a hypothetical organization running an internet-facing application affected by a newly disclosed vulnerability. The security team needs to establish whether the vulnerable software is present, what the application supports, and whether attackers are exploiting the weakness. Those findings can guide remediation priorities and targeted hunting for signs of compromise. If suspicious activity appears, analysts investigate it with an understanding of the affected system and the potential route an attacker could take through the environment. Depending on the evidence, the response may involve containing a system, examining related accounts, or expanding the investigation to other assets. The organization’s remediation teams also need clear recommendations about the underlying exposure. What the investigation reveals then feeds back into detection rules, hunting priorities, and response procedures. This gives leaders a way to track an identified risk through investigation, action, and outstanding work, with clearer ownership at each stage. What role does AI play in preemptive MDR? Before analysts can assess a potential threat, they often need to retrieve logs, examine user activity, and connect evidence across several systems. AI can accelerate this work by gathering and correlating information for review. Agentic investigation capabilities can perform elements of that process in parallel, test possible explanations, and organize findings. Their usefulness depends o
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: What Is Preemptive MDR? A Guide For Security Leaders
  - Published: 2026-11-19T15:58:53+00:00
  - Link: https://www.rapid7.com/blog/post/dr-what-is-preemptive-mdr-security-leaders-guide
  - Summary: When an MDR provider contains a compromised endpoint, your team needs to know whether the weakness that enabled the attack exists elsewhere and who is responsible for addressing it. Without that follow-through, the immediate incident may be resolved while another attacker still has a way in. Preemptive managed detection and response (MDR) is Rapid7's approach to connecting exposure context, threat intelligence, AI-assisted investigation, and human expertise. It supports proactive cybersecurity by helping teams prioritize weaknesses before exploitation, investigate threats with a clearer understanding of risk, and use their findings to strengthen defenses. How does preemptive MDR differ from traditional MDR? Managed detection and response provides security specialists who monitor, investigate, and respond to threats around the clock. Many services also include proactive threat hunting and recommendations to improve security. Preemptive MDR connects that work more directly to what makes

### Cluster e92ec6df64 — score 12

- Title: Spying on Governments with Zero Lines of Malware: A Custom SoftEther Bridge in Webworm’s Toolkit
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-19T15:05:34+00:00
- Link: https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Introduction For a threat actor, the perfect malware is one they don’t have to write, and already does all they need. One example of this is shown by the China-aligned APT known as Webworm, which has been known to deploy the open-source SoftEther VPN into the networks of compromised governmental organizations to maintain low-profile, long-term access. After this was publicly documented and defenders could keep an eye out for this tactic, the actor presumably started thinking of ways to make their covert access stealthier. In this post, we share our analysis of what we believe to be a so-far unknown custom SoftEther-based tool, which implements various tricks to hide itself from security tools, and which we attribute to Webworm with moderate confidence. We additionally provide guidance and tooling for detecting its presence on a system and extracting the configuration(s) associated with it. Technical analysis To illustrate how the tool works, we will use the only public sample of this t
```

#### Full body

```
Government Spying on Governments with Zero Lines of Malware: A Custom SoftEther Bridge in Webworm’s Toolkit Milan Spinka Nov 19, 2026 | Last updated on Nov 19, 2026 | 7 min read DISCOVER RAPID7 MDR Spying on Governments with Zero Lines of Malware: A Custom SoftEther Bridge in Webworm’s Toolkit Table of contents Spying on Governments with Zero Lines of Malware: A Custom SoftEther Bridge in Webworm’s Toolkit DISCOVER RAPID7 MDR Table of contents Introduction For a threat actor, the perfect malware is one they don’t have to write, and already does all they need. One example of this is shown by the China-aligned APT known as Webworm, which has been known to deploy the open-source SoftEther VPN into the networks of compromised governmental organizations to maintain low-profile, long-term access. After this was publicly documented and defenders could keep an eye out for this tactic, the actor presumably started thinking of ways to make their covert access stealthier. In this post, we share our analysis of what we believe to be a so-far unknown custom SoftEther-based tool, which implements various tricks to hide itself from security tools, and which we attribute to Webworm with moderate confidence. We additionally provide guidance and tooling for detecting its presence on a system and extracting the configuration(s) associated with it. Technical analysis To illustrate how the tool works, we will use the only public sample of this tool we are aware of, which can be found in our IoCs list ( 90e7… ). The sample is a Windows PE32+ file targeting the x64 architecture. Based on cleartext strings and constants in the binary, we identified it as a (modified) build of the SoftEther VPN Bridge executable, specifically version 4.44, build 9807. Similarly, the PDB path included in the executable reads C:\Users\Administrator\Desktop\SoftEtherVPN_Stable\SoftEtherVPN_Stable\SoftEtherVPN_Stable\src\DebugFiles\pdb\x64_Release\vpnbridge.pdb . As such, the tool doesn’t hide its identity from reverse engineers, only external interactions. The first and most trivial change the threat actor implements is in the PE metadata. Here we learn that the OriginalFileName of this binary is netcapa.exe , and it brands itself as “Network Monitor Software” published by a company named “Network Systems Solutions Inc.“. The only field unchanged against the stock SoftEther executable ( vpnbridge_x64.exe ) is the Version , which reads 4, 44, 0, 9807 . Next, we wanted to identify any functionality added or modified by the threat actor. The SoftEther bridge alone is a powerful tool to maintain remote access to a compromised network, but we wanted to know if perhaps there was a backdoor to give the threat actor direct command execution on the infected host. For that reason we checked out the corresponding tag in the public “SoftEtherVPN_Stable” repository on GitHub and compared it to the decompiled sample. Internal rebranding The rebranding apparent in the exposed metadata extends into internal strings used in debug banners, service names, registry keys, the contents of the server’s HTTP 401 error page, or firewall rule names, where occurrences of “SoftEther VPN” are replaced by “NtMonitor VPN”. However, the renaming is inconsistent; for example, the service name used by the entry point is still SEVPNBRIDGE , and many registry key paths still reference the “SoftEther Project”. Network stealth Stock SoftEther VPN Mayaqua/Network.h defines HTTP endpoints used by the protocol: HTTP_VPN_TARGET "/vpnsvc/vpn.cgi" HTTP_VPN_TARGET2 "/vpnsvc/connect.cgi" NtMonitor replaces these endpoints with much more innocent-sounding names, in particular: HTTP_VPN_TARGET "/update/alive.cgi" HTTP_VPN_TARGET2 "/update/picture.cgi" A client initiating a connection to a SoftEther VPN server will send a handshake request to HTTP_VPN_TARGET2 along with a "watermark", i.e. a byte pattern proving that the client is speaking the correct VPN protocol. Otherwise, the server answers with a decoy HTTP respon
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Spying on Governments with Zero Lines of Malware: A Custom SoftEther Bridge in Webworm’s Toolkit
  - Published: 2026-11-19T15:05:34+00:00
  - Link: https://www.rapid7.com/blog/post/tr-spying-on-governments-no-malware-custom-webworms-toolkit-softether-bridge
  - Summary: Introduction For a threat actor, the perfect malware is one they don’t have to write, and already does all they need. One example of this is shown by the China-aligned APT known as Webworm, which has been known to deploy the open-source SoftEther VPN into the networks of compromised governmental organizations to maintain low-profile, long-term access. After this was publicly documented and defenders could keep an eye out for this tactic, the actor presumably started thinking of ways to make their covert access stealthier. In this post, we share our analysis of what we believe to be a so-far unknown custom SoftEther-based tool, which implements various tricks to hide itself from security tools, and which we attribute to Webworm with moderate confidence. We additionally provide guidance and tooling for detecting its presence on a system and extracting the configuration(s) associated with it. Technical analysis To illustrate how the tool works, we will use the only public sample of this t

### Cluster 5d7989058d — score 12

- Title: nginx2root: Five new nginx vulnerabilities, and how Cloudflare protects origins from the worst of them
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-11-20T01:58:29+00:00
- Link: https://blog.cloudflare.com/nginx2root/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: AWS, Azure, Palo Alto Networks
- cve_ids: CVE-2026-118899, CVE-2026-121810, CVE-2026-123007, CVE-2026-123633, CVE-2026-123634
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Palo Alto Networks, AWS, Azure
- cve_ids: CVE-2026-123007, CVE-2026-123633, CVE-2026-118899, CVE-2026-121810, CVE-2026-123634
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Five memory corruption bugs in nginx, called nginx2root, can let an unauthenticated attacker run code on a server. Here’s how they work, and why origins behind Cloudflare's proxy are shielded from the most serious of these bugs.
```

#### Full body

```
On November 18, 2026, F5 and nginx.org disclosed ten vulnerabilities in nginx. Five of them, detailed by the Xint research team and published under the name nginx2root , are memory corruption flaws that an unauthenticated attacker can use to crash an nginx worker or, per Xint's research, run commands on the server. Xint also found a Linux kernel bug that turns that foothold into root on the host, including from inside a Docker container. Other teams found the two HTTP/2 bugs independently: F5 also credits Rapid7, Wiz Research and Ikotas Labs for CVE-2026-123007, and Metnir, Wiz Research, and Palo Alto Networks Unit 42 for CVE-2026-123633. nginx is an HTTP web server that also serves as reverse proxy, content cache, load balancer, TCP/UDP proxy server, and mail proxy server. nginx runs a large share of the world's web servers, so this is a patch-now event. But if your nginx server is reachable only through Cloudflare's proxy, attackers cannot reach the vulnerable code paths for the most serious of these bugs, giving you protection while you update your servers. Here is where Cloudflare stands, what that protection covers, where it stops, and how the bugs work. The short version Cloudflare's edge is not affected. Â Much of the proxy that handles customer traffic at our edge now runs on FL2, written in Rust. We reviewed the parts still built on our heavily modified nginx fork against all five bugs before disclosure, and an update closing the related code paths finished rolling out globally before the vulnerabilities were published. The same releases fix five other nginx CVEs, including CVE-2026-118899, an infinite loop while reading a request body over TLS 1.3. Origins behind Cloudflare's HTTP proxy are shielded from the HTTP/2 and HTTP/3 attacks. Â For proxied hostnames, Cloudflare terminates every client HTTP/2 and HTTP/3 connection at our edge and opens a separate connection to your origin. The attacker's frames never reach your nginx. The resolver and mail proxy vulnerabilities depend on specific configuration. Â Many configurations of nginx will not be vulnerable, but the safest way to be sure is to update your install or disable features. You should still patch. Â Update to nginx 1.30.7 or 1.31.9 (or your vendor's fixed build) and restart. Some configurations, covered below, are not protected by the proxy. What was disclosed nginx2root is five independent bugs. Each one works on its own and each one needs a different configuration. CVE Bug class Affected configuration First affected release CVE-2026-123007 Integer overflow leading to out-of-bounds heap read/write HTTP/2 enabled 1.9.5 (2015) CVE-2026-123633 Use-after-free HTTP/2 with proxy_pass Â to a backend, worker low on worker_connections 1.19.7 CVE-2026-121810 Use-after-free HTTP/3 (QUIC) with proxy_pass Â to a backend 1.25.0 CVE-2026-123634 Use-after-free resolver Â + proxy_pass Â with variables + a subrequest ( mirror Â or SSI) 0.6.18 CVE-2026-113425 Use-after-free Mail proxy with proxy on Â and auth_http 0.5.33 F5 rates each one High (CVSS 3.1: 8.1) and Critical (CVSS 4.0: 9.2), and notes that code execution requires disabling or bypassing ASLR Â (Address Space Layout Randomization). For CVE-2026-123007, Xint's write-up shows how it leaked memory addresses to do exactly that. CVE-2026-123007 is the one to worry about most. It only needs HTTP/2 turned on, which is commonly enabled on TLS deployments, and it has been in every nginx release since HTTP/2 support shipped in 1.9.5. Xint ran the exploit over the public Internet against servers on AWS, GCP and Azure. Xint searched Shodan on November 10, before the disclosure, and found 56.7 million hosts matching product:nginx . Of the 11.94 million that reported a version, 98.9% fell in the affected range. As of November 19, Censys's nginx2root exposure tracker Â counts about 8.8 million services running a potentially affected version with HTTP/2 enabled. Version strings don't prove a host is vulnerable, since distributions
```

#### Corroborating sources (2)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: nginx2root: Five new nginx vulnerabilities, and how Cloudflare protects origins from the worst of them
  - Published: 2026-11-20T01:58:29+00:00
  - Link: https://blog.cloudflare.com/nginx2root/
  - Summary: Five memory corruption bugs in nginx, called nginx2root, can let an unauthenticated attacker run code on a server. Here’s how they work, and why origins behind Cloudflare's proxy are shielded from the most serious of these bugs.
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - Title: nginx2root: Five new nginx vulnerabilities, and how Cloudflare protects origins from the worst of them
  - Published: 2026-11-20T01:58:29+00:00
  - Link: https://blog.cloudflare.com/nginx2root/
  - Summary: Five memory corruption bugs in nginx, called nginx2root, can let an unauthenticated attacker run code on a server. Here’s how they work, and why origins behind Cloudflare's proxy are shielded from the most serious of these bugs.

### Cluster 5ab917fdb9 — score 12

- Title: Runtime security for Amazon EKS Auto Mode with Sysdig
- Source: Sysdig (detection_response_operations)
- Published: 2026-11-19T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/runtime-security-for-amazon-eks-auto-mode
- Fetch status: ok
- Member count: 6
- Corroborating source count: 4
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- affected_products: AWS, Kubernetes
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis

#### Primary article taxonomy
- affected_products: Kubernetes, AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Sysdig integrates with Amazon EKS Auto Mode hands node management to AWS, giving you immutable, Bottlerocket-based nodes with read-only root filesystems and no kernel module loading. But the shared responsibility model still applies: what happens inside your workloads at runtime is on you. This post explains how Sysdig Secure uses Universal eBPF and Falco-powered detection to deliver real-time runtime security on EKS Auto Mode. It covers deploying Host Shield, following nodes as AWS adds and replaces them, and catching threats with full Kubernetes context that static scanning alone can miss.
```

#### Full body

```
kubernetes-container-security This is some text inside of a div block. < back to blog Runtime security for Amazon EKS Auto Mode with Sysdig Published by: Eric Carter Product Marketing Director Merin Eralil ISV Security Partner Solutions Architect at AWS @ Amazon Web Services linkedin Subscribe to Threat Research GET A DEMO Published: November 19, 2026 Table of contents TRT in your inbox Get security briefings from the Threat Research Team New campaigns, attacker techniques, and detection guidance — straight to your inbox. Subscribe falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more If you use Amazon Elastic Kubernetes Service ( Amazon EKS ) Auto Mode, you benefit from AWS-managed infrastructure, but you still need runtime security for your workloads. Amazon EKS Auto Mode lets AWS run your Kubernetes cluster infrastructure: compute, networking, storage, load balancing, and node patching. That removes a lot of toil. Because AWS operates the nodes for you in a managed model, nodes are identical, predictable, and immutable, with read-only root filesystems and strict security controls. This post covers what that means for runtime security, and how to deploy and use Sysdig Secure with EKS Auto Mode using Universal eBPF. What changes with Amazon EKS Auto Mode With standard EKS, AWS manages the control plane, and you manage the worker nodes. Auto Mode extends AWS's responsibility to the nodes and the core cluster capabilities: Compute provisioning, autoscaling, andconsolidation Pod and service networking, and load balancing Block storage integration and CoreDNS Node patching, replacement, and lifecyclemanagement Nodes are AWS-managed appliances: a locked-down, container-focused OS (Bottlerocket-based) with a read-only root filesystem and SELinux enforcement. Nodes are replaced regularly, so they never drift. See the Auto Mode documentation for the full list of managed components. Shared responsibility still applies AWS manages You manage Auto Mode EC2 instances and lifecycle Node OS patching and replacement Compute autoscaling and capacity Core networking, load balancing, storage AWS-managed cluster capabilities Application code, images, runtime configuration Workloads, availability, disruption budgets VPC design, subnets, routing, security groups IAM, Kubernetes RBAC, workload identities Vulnerabilities, secrets, policies, runtime behavior AWS's security guidance for Auto Mode and best practices cover the AWS side. This post covers the last row: what happens inside your workloads at runtime. Why Auto Mode needs a different agent approach Auto Mode nodes don't allow kernel module loading for security reasons. Because Bottlerocket fully supports eBPF (Extended Berkeley Packet Filter), Sysdig uses eBPF as the primary mechanism for runtime security. A Universal eBPF driver embedded in the Sysdig Host Shield (agent) enables a real-time approach to monitoring system activity safely within the kernel using system calls as a source of truth. Learn more about kernel-level security monitoring. Getting started Sysdig deploys as a Kubernetes workload, so it follows Auto Mode nodes as AWS adds and replaces them. Nothing runs on the host outside Kubernetes. Follow these steps to get set up: Create an Auto Mode cluster , or enable Auto Mode on an existing one, and connect with kubectl . Get your Sysdig access key and region from your Sysdig Secure tenant. Keep the key in a Kubernetes Secret, not in manifests. Install Sysdig with Universal eBPF. Use the Kubernetes onboarding workflow in Sysdig Secure (Host Shield for node-level protection, Cluster Shield for cluster-level components), and set: host: driver: universal_ebpf (See Understand Agent Drivers for requirements.) Make sure egress allows the Sysdig collector endpoints for your region. Verify. Run the following and confirm the active driver is
```

#### Corroborating sources (4)

- **Sysdig** (detection_response_operations)
  - Title: Runtime security for Amazon EKS Auto Mode with Sysdig
  - Published: 2026-11-19T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/runtime-security-for-amazon-eks-auto-mode
  - Summary: Sysdig integrates with Amazon EKS Auto Mode hands node management to AWS, giving you immutable, Bottlerocket-based nodes with read-only root filesystems and no kernel module loading. But the shared responsibility model still applies: what happens inside your workloads at runtime is on you. This post explains how Sysdig Secure uses Universal eBPF and Falco-powered detection to deliver real-time runtime security on EKS Auto Mode. It covers deploying Host Shield, following nodes as AWS adds and replaces them, and catching threats with full Kubernetes context that static scanning alone can miss.
- **Elastic Security Labs** (detection_response_operations)
  - Title: 56 AWS API calls in 141 milliseconds: Inside an AI-run intrusion
  - Published: 2026-11-13T15:27:20+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion
  - Summary: A CyberStrikeAI server spent 16 days in four AWS accounts using eight identities, and the CloudTrail record shows why six detection rules each caught only part of it.
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Detecting cross-cloud lateral movement with AWS Security Hub
  - Published: 2026-11-18T22:28:45+00:00
  - Link: https://aws.amazon.com/blogs/security/detecting-cross-cloud-lateral-movement-with-aws-security-hub/
  - Summary: Most organizations run a multicloud estate, and so do the attackers targeting them. An adversary who compromises an identity in one provider follows that identity wherever it leads, including across a federated trust into a second cloud service provider. The signals enumerating this scenario are rarely missing; the problem is that they live in separate […]
- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #355 - Cyber Chaos Monkey, Offsec Harness Index, Top 10 AWS Security Research of 2026
  - Published: 2026-11-19T15:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-355
  - Summary: Shopify's AI agent system that continuously attacks their production infra, list of open-source offensive AI agent harnesses, la creme de la cloud 2026

### Cluster 837820075f — score 11

- Title: 30 Years of Gatekeeper Asymmetry Doom: The Paradox that Makes Powerful LLMs More Vulnerable
- Source: Check Point Research (threat_research_primary)
- Published: 2026-11-19T13:19:10+00:00
- Link: https://research.checkpoint.com/2026/30-years-of-gatekeeper-asymmetry-doom-the-paradox-that-makes-powerful-llms-more-vulnerable/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Abstract We give an exposition for a principle of gatekeeper asymmetry doom in information security, which states that “If the system vetting adversarial input has strictly less power than the system processing that input, without leveraging some hard problem, this will inevitably lead to doom.” We list a variety of examples where one can see […] The post 30 Years of Gatekeeper Asymmetry Doom: The Paradox that Makes Powerful LLMs More Vulnerable appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 24 Android Malware 23 Artificial Intelligence 6 ChatGPT 3 Check Point Research Publications 484 Cloud Security 1 CPRadio 44 Crypto 3 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 434 How To Guides 13 Ransomware 7 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 30 Years of Gatekeeper Asymmetry Doom: The Paradox that Makes Powerful LLMs More Vulnerable November 19, 2026 https://research.checkpoint.com/2026/30-years-of-gatekeeper-asymmetry-doom-the-paradox-that-makes-powerful-llms-more-vulnerable/ Abstract We give an exposition for a principle of gatekeeper asymmetry doom in information security, which states that “If the system vetting adversarial input has strictly less power than the system processing that input, without leveraging some hard problem, this will inevitably lead to doom.” We list a variety of examples where one can see this principle in action, including the limits of static binary classification, the proliferation of sandbox evasions and our own ‘PuzzleMask’ research for bypassing external AI guardrails, as well as a short exposition of how the Time Hierarchy Theorem also exemplifies this same principle. We conclude with a recommendation that “doomed” attack surfaces should be noticed and the gap be narrowed down as much as possible, by upgrading gatekeeper power or making use of its existing power more comprehensively. We note that frontier LLMs (with scaffolding, extended reasoning, code execution in the chain of thought, and so on) have significant power in this sense and can meaningfully contribute to narrowing “doom” gaps, though ultimately, they themselves are still subject to this principle. Introduction In the same spirit of Moxie Marlinspike’s Cryptographic Doom Principle [1], the Gatekeeper Asymmetry Doom principle states that: If the system vetting adversarial input has strictly less power than the system processing that input, without leveraging some hard problem, this will inevitably lead to doom. By the mention of ‘leveraging a hard problem’ we mean to exclude e.g. signature verification for binary files, which is many times simpler than executing the file but can still, at least in a certain theoretical world, determine whether the binary is malicious or not. The principle might be phrased more glibly as “every quick sanity check involves either cryptography or a silent prayer.” From now on, rather than writing out “gatekeeper asymmetry doom” every time, we will simply refer to “doom” for short. We’ll start with examples that are more on the “warm-up” side and gradually go from those to less intuitive ones where the application of the principle is more surprising. Examples Hash Comparison A good warm-up example to start with is the one burned into the psyche of every infosec practitioner in some fundamental post-traumatic sense. At some point during the 1990s, the silent thought must have come to someone in the industry that malware was solved. You could collect all the hashes of malicious binaries in a large database and then a gatekeeper, called in this case an “antivirus,” would check each executed binary against the known list of ‘bad’ hashes. Of course, new threats would emerge periodically, and the list would have to be updated, but this was a caveat – not a dealbreaker. The gap between the gatekeeper’s power and the target’s power here was truly huge. The target in this case is the full Turing-complete execution of a binary, and the gatekeeper is a simple observation of whether the binary is in some set of known files. The procedure effectively strips all other file data and precludes it from consideration, and the threat actors’ counter was infamous and trivial: for each compiled binary, randomize the value of some non-load-bearing byte. This is more a precursor to Gatekeeper Asymmetry than the proper thing itself: what’s doing the work in motivating hash compariso
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 30 Years of Gatekeeper Asymmetry Doom: The Paradox that Makes Powerful LLMs More Vulnerable
  - Published: 2026-11-19T13:19:10+00:00
  - Link: https://research.checkpoint.com/2026/30-years-of-gatekeeper-asymmetry-doom-the-paradox-that-makes-powerful-llms-more-vulnerable/
  - Summary: Abstract We give an exposition for a principle of gatekeeper asymmetry doom in information security, which states that “If the system vetting adversarial input has strictly less power than the system processing that input, without leveraging some hard problem, this will inevitably lead to doom.” We list a variety of examples where one can see […] The post 30 Years of Gatekeeper Asymmetry Doom: The Paradox that Makes Powerful LLMs More Vulnerable appeared first on Check Point Research .

### Cluster 31919ab83e — score 11

- Title: Microsoft agent-framework Compromised: Credential Stealer Targets Azure and CI Pipelines
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-11-17T22:03:37+00:00
- Link: https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Azure

#### Cluster taxonomy (union across members)
- affected_products: Azure, PyPI
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Azure, PyPI
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Summary

```
On November 17, 2026 at 20:35 UTC, versions 1.26.1 & 1.26.2 of the Microsoft PyPI package agent-framework were published with an added credential stealer. The package gets almost 200k downloads a month. The malicious versions have since been quarantined.
```

#### Full body

```
At 20:35 UTC on November 17, 2026, a malicious version ( 1.26.1 ) of the agent-framework package (Microsoft Agent Framework) was uploaded to PyPI. A second version, 1.26.2 , followed at 21:08 UTC. As of 21:30 UTC, both versions were no longer available on PyPI. The package gets about 41,000 downloads a week. The most recent safe version is 1.26.0. When a malicious version is installed, it drops a .pth file into the site-packages root ( agent_framework_meta.pth in 1.26.1, af_runtime_diag.pth in 1.26.2). Python runs .pth files on every interpreter start, so the credential stealer runs whenever Python starts in that environment, even if agent-framework is never imported. Updated Nov 18 14:00 UTC - Updated root cause and analyzed exfiltrated data. Wiz promptly reported these findings to Microsoft on the 17th. Root Cause The attacker's tooling reported its own progress to the same publicly accessible webhook it used for exfiltration, which let Wiz Research observe part of the operation. A timeline of the attack, highlighting information disclosed via attacker use of webhook[.]site The attacker appears to have compromised a client certificate and private key for Microsoft ESRP (Engineering System Release Pipeline), the internal service Microsoft uses to sign and publish this package. Their first publish attempt, from AWS, was rejected by ESRP's IP filtering. A second attempt from Microsoft-owned IP space succeeded. How the credentials were obtained is not yet known. The tooling identifies itself as Cairn , an open-source AI penetration-testing framework : it staged the package at /tmp/cairn_pkg and sent a CAIRN_ESRP_PROBE2 connectivity probe. Before publishing, the attacker ran the stealer on their own machine. That run captured an AI coding agent configuration that appears to be the open-source Pi harness backed by a GLM-family model ( pi_glm53 ), routed through a local proxy. Earlier this year, another Microsoft Python package, durabletask , was compromised after its PyPI token was stolen. We have not linked the two incidents. Timeline (UTC) Time Event 2026-11-12 18:25 Legitimate 1.26.0 published (wheel + sdist, alongside agent-framework-core 1.26.0) 2026-11-17 20:35 Malicious 1.26.1 published 2026-11-17 ~21:08 Malicious 1.26.2 published 2026-11-17 ~21:30 1.26.1 & 1.26.2 no longer available on PyPI Payload agent_framework_meta.pth contains one line: import agent_framework_meta In 1.26.1, agent_framework_meta/__init__.py then calls _telemetry._start() . The stealer forks into a detached session ( os.setsid() ), or falls back to a daemon thread where fork isn't available. It sets _AF_TEL=1 to avoid running again in child processes. The file and function names ( _telemetry , "Lightweight runtime diagnostics hook", user-agent af-runtime-diagnostics/1 ) are made to look like legitimate SDK telemetry. Credential Stealer The stealer is focused on Azure and Azure DevOps. It collects: Environment variables with names containing strings such as TOKEN, SECRET, PASSWORD, KEY, AZURE, AWS, GITHUB, OPENAI, HF_, FOUNDRY, NPM, PIP, NUGET, SYSTEM, BUILD, AGENT Other processes' environments : secret-looking values read from up to 300 /proc/*/environ files Credential files (up to 60): Azure CLI (~/.azure/) .npmrc, pip.conf, .netrc, .git-credentials, .docker/config.json Hugging Face tokens Azure DevOps agent .credentials .env and JSON files under /app and /workspace Azure DevOps OIDC tokens : if SYSTEM_ACCESSTOKEN and SYSTEM_OIDCREQUESTURI are set, it requests an OIDC token for api://AzureADTokenExchange Azure managed-identity tokens from IMDS or the App Service identity endpoint for 12 resources: ARM, Graph, Key Vault, Storage, Cognitive Services, Azure AI/ML, Search, Container Registry, Azure DevOps, and AzureADTokenExchange Azure instance metadata Everything is put into one JSON document, zlib-compressed, base64-encoded, and sent in one HTTPS POST to webhook[.]site . The URL is hardcoded and the payload has no fallback channel. Failures are silentl
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Microsoft agent-framework Compromised: Credential Stealer Targets Azure and CI Pipelines
  - Published: 2026-11-17T22:03:37+00:00
  - Link: https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi
  - Summary: On November 17, 2026 at 20:35 UTC, versions 1.26.1 & 1.26.2 of the Microsoft PyPI package agent-framework were published with an added credential stealer. The package gets almost 200k downloads a month. The malicious versions have since been quarantined.

### Cluster c5a930f76b — score 11

- Title: Clearer Security Signals: Making Attestations Comprehensible for PyPI Users
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-11-17T19:12:02+00:00
- Link: https://openssf.org/blog/2026/11/17/clearer-security-signals-making-attestations-comprehensible-for-pypi-users/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: critical_infrastructure
- affected_products: PyPI
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: critical_infrastructure
- affected_products: PyPI
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
To help developers and package consumers better understand software supply-chain security, the OpenSSF Securing Software Repositories Working Group created an Attestations Style Guide—and its recommendations are now live on PyPI with redesigned project pages and a dedicated security tab.
```

#### Full body

```
By Nicole Harris and Dustin Ingram Attestations provide a verifiable record of a software artifact’s provenance: where and how a package was built or published, and which identity or workflow was responsible. When package registries such as PyPI, RubyGems, and npm began supporting attestations, it marked a major milestone in software supply-chain security. But introducing attestations is only part of the challenge. For users to benefit from them, they need to understand what they demonstrate, what their limitations are, and how to interpret them when evaluating a package. Because attestations are relatively new, little guidance existed for presenting this information effectively. Early registry implementations often left users to interpret dense, unfamiliar metadata without explaining its practical significance. To address this gap, the OpenSSF funded the Securing Software Repositories Working Group to develop an Attestations Style Guide , researching and documenting best practices for communicating attestations to end users. Today, we’re pleased to announce that the first implementation of the style guide’s recommendations is live on the Python Package Index (PyPI), featuring redesigned project pages and a dedicated security tab. Phase 1: Cross-Ecosystem Research and the Initial Style Guide Led by Superbloom Design , in collaboration with Kabu Creative and the Securing Software Repositories Working Group , this phase involved qualitative research with open source maintainers, security researchers, and package consumers. Through interviews and observations, the team explored how users evaluate package security, what they understand about attestations, and how they interpret existing registry interfaces. Findings and Recommendations The research revealed that users approach package security with different levels of knowledge, priorities, and expectations. Security specialists often know what information they need to assess a package, while less experienced users may lack the context to interpret technical details. Several recurring themes emerged: Security information needs context. An attestation or status indicator alone doesn’t explain what it demonstrates or how users should interpret it. Clear explanations and guidance on what to do next are essential. Terminology matters. Unfamiliar technical concepts, such as provenance and attestations, need clear explanations and links to supporting information. Package trust is multifaceted. Users consider a variety of signals when assessing a package, including project activity, download counts, maintainer reputation, source code, checksums, and build information. Attestations are one part of this broader picture. Most users prioritize utility above security. Security information is important, but shouldn’t displace the details users need to assess whether a package is suitable for their needs. These findings informed the OpenSSF Attestations Style Guide . It provides recommendations for page layout, information hierarchy, labels, and status indicators, alongside guidance on terminology, explanatory text, and supporting documentation. Phase 2: PyPI Implementation With principles for displaying attestations established, the OpenSSF funded a second phase of the project: implementing the style guide’s recommendations on the Python Package Index (PyPI). Kabu Creative carried out this work in collaboration with the PyPI team, and investigated how the style guide should be adapted for PyPI’s use cases, including: Different Types of Attestations: How should PyPI distinguish between PyPI Publish attestations, which provide evidence about the publishing process, and SLSA Build Provenance attestations, which describe how a release file was built? Multiple Release Files: How should provenance be communicated when a release contains multiple files, some of which may have attestations while others may not? Changes in Provenance: How can PyPI highlight changes in provenance that might warrant inve
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: Clearer Security Signals: Making Attestations Comprehensible for PyPI Users
  - Published: 2026-11-17T19:12:02+00:00
  - Link: https://openssf.org/blog/2026/11/17/clearer-security-signals-making-attestations-comprehensible-for-pypi-users/
  - Summary: To help developers and package consumers better understand software supply-chain security, the OpenSSF Securing Software Repositories Working Group created an Attestations Style Guide—and its recommendations are now live on PyPI with redesigned project pages and a dedicated security tab.

### Cluster e76dca6b32 — score 11

- Title: PHP security updates fix 18 flaws, including critical RCE bugs
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-19T16:28:23+00:00
- Link: https://www.bleepingcomputer.com/news/security/php-security-updates-fix-18-flaws-including-critical-rce-bugs/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos, phishing_social_eng
- cve_ids: CVE-2026-115560, CVE-2026-126714, CVE-2026-129289, CVE-2026-129474, CVE-2026-129496
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, ddos
- cve_ids: CVE-2026-129289, CVE-2026-129474, CVE-2026-129496, CVE-2026-126714, CVE-2026-115560
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The PHP development team released security updates addressing 18 vulnerabilities, including critical flaws that could allow unauthenticated attackers to remotely execute code on vulnerable servers. [...]
```

#### Full body

```
PHP security updates fix 18 flaws, including critical RCE bugs By Lawrence Abrams November 19, 2026 11:28 AM 0 The PHP dev team released security updates for 18 vulnerabilities, including critical flaws that could allow unauthenticated attackers to remotely execute code on vulnerable servers. The updates were released Thursday, November 19, for all supported PHP branches, with PHP 8.5.13, 8.4.28, 8.3.37, and 8.2.36 now available. Security firm Aikido reports that the updates address 18 CVEs affecting PHP's core engine, session handling, PHP-FPM, CGI, and other components. One of the most serious flaws, tracked as CVE-2026-129289, is a critical PHP-FPM request smuggling vulnerability with a CVSS score of 9.2. According to Aikido, the flaw allows unauthenticated attackers to execute PHP code remotely on vulnerable servers that reuse connections to PHP-FPM under certain conditions. The vulnerability affects certain nginx, Apache, HAProxy, and LSAPI configurations that reuse backend connections to PHP-FPM. Standard nginx and Apache configurations that do not reuse backend connections are not affected by the attack. Other important vulnerabilities fixed in the updates include: CVE-2026-129474: A use-after-free vulnerability involving magic method backtraces that could lead to remote code execution. CVE-2026-129496: A timezone cache use-after-free vulnerability that could lead to remote code execution. CVE-2026-126714: A vulnerability involving partially overwritten session files that could lead to remote code execution. CVE-2026-115560: A session serializer mismatch vulnerability that could lead to remote code execution. CVE-2026-129291: A PHP-FPM epoll use-after-free vulnerability that could lead to local privilege escalation. CVE-2026-128090: A PHAR OpenSSL signature bypass vulnerability involving an algorithm downgrade. Additional fixes address memory corruption, information disclosure, cross-site scripting, denial-of-service issues, and potentially unsafe handling of HTTPS and FTPS URLs. The releases follow a warning issued Wednesday by the PHP security team that the upcoming updates would address vulnerabilities affecting all supported PHP versions, with the highest severity rated critical. "The issues rated CRITICAL require either non-default configuration or uncommon setups," the PHP security team warned . One of the vulnerabilities, CVE-2026-115560, was already disclosed in an October 23 informational advisory and relates to how PHP handles session data under certain configurations, potentially leading to remote code execution. As a temporary mitigation, PHP recommended disabling session upload progress by setting session.upload_progress.enabled=0 and restarting PHP workers. This setting was also recommended to mitigate the recent PHP2Shell flaws . For CVE-2026-129289, administrators who cannot immediately install the security updates can mitigate the vulnerability by disabling persistent backend connections between their web servers and PHP-FPM, ensuring connections are closed after each request. Aikido warns that these mitigations do not address all vulnerabilities fixed in the November updates and recommends ensuring PHP-FPM and LSAPI listeners are not directly exposed to untrusted networks. Although the official security updates are limited to supported PHP branches, third-party maintainer Ondrej Surý has also released patched packages for unsupported PHP versions dating back to PHP 5.6. Aikido has similarly released hardened PHP container images containing backported security fixes for unsupported versions, including PHP 5.6, 7.0, 7.1, 7.2, 7.4, and 8.1. PHP administrators are urged to upgrade to PHP 8.5.13, 8.4.28, 8.3.37, or 8.2.36, depending on their supported branch, to address the newly disclosed vulnerabilities. Uncover email threats your existing defenses may miss. Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud. See what
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: PHP security updates fix 18 flaws, including critical RCE bugs
  - Published: 2026-11-19T16:28:23+00:00
  - Link: https://www.bleepingcomputer.com/news/security/php-security-updates-fix-18-flaws-including-critical-rce-bugs/
  - Summary: The PHP development team released security updates addressing 18 vulnerabilities, including critical flaws that could allow unauthenticated attackers to remotely execute code on vulnerable servers. [...]

### Cluster efdc801eef — score 11

- Title: Java4Shell Vulnerability Allows Remote Attacks on Major Java Apps
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-11-18T12:35:00+00:00
- Link: https://www.infosecurity-magazine.com/news/java4shell-vulnerability-remote/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: AWS, Atlassian Confluence, Atlassian Jira
- cve_ids: CVE-2026-114938
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Atlassian Jira, Atlassian Confluence, AWS
- cve_ids: CVE-2026-114938
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
A critical OpenJDK vulnerability could expose major Java applications to remote code execution, prompting CISA to urge organizations implement mitigations
```

#### Full body

```
Infosecurity Magazine Home » News » Java4Shell Vulnerability Allows Remote Attacks on Major Java Apps Java4Shell Vulnerability Allows Remote Attacks on Major Java Apps News 18 November 2026 Written by Kevin Poireault Reporter , Infosecurity Magazine Follow @Kpoireault Connect on LinkedIn Weeks after PHP2Shell , another critical vulnerability has been leaked before its planned disclosure and authorities are now urging organizations to apply patches. The new vulnerability, known as ‘Java4Shell’ and tracked as CVE-2026-114938, is a memory corruption vulnerability in Open Java Development Kit (OpenJDK), an open-source implementation of the Java Platform, Standard Edition (Java SE) co-maintained by Oracle and a global community of developers and companies, such as Red Hat, Amazon and Microsoft. OpenJDK runs most Java applications. The vulnerability was found by California-based security firm Calif, which published details on November 17 after some information was leaked before coordinated disclosure. The flaw affects OpenJDK 17, 21, 25 and 27 and is rated with a high-severity score of 8.1 by Oracle (using CVSS v3.1) and a critical severity score of 9.2 by Calif (using CVSS v4.0). The exploitation of Java4Shell can allow unauthenticated attackers corrupt memory in Java servers with a single malformed message. According to a write-up from Calif , the blast radius of a potential exploit could be broad, with many Java-based applications built on OpenJDK also vulnerable. Services vulnerable to a remote code execution (RCE) attack which has exploited Java4Shell include Keycloak, Atlassian’s products like Jira and Confluence, JFrog Artifactory, Jenkins and PingFederate as well as many distributions based on OpenJDK: Amazon Corretto Eclipse Temurin Microsoft Build of OpenJDK Azul Zulu BellSoft Liberica SAP SapMachine Red Hat OpenJDK Oracle OpenJDK Oracle Java SE Oracle GraalVM for JDK Other services can also be vulnerable to a Java4Shell exploit, but only if the attacker is able to authenticate. These include Apache Kafka Broker, Apache Solr, Elasticsearch, Gerrit and Spinnaker. Maintainers of OpenJDK have published a fix, but each Java vendor will ship its fixed build on its own schedule. The US Cybersecurity and Infrastructure Security Agency (CISA) published an emergency advisory on November 17 urging organizations to apply patches as soon as they are available. Java4Shell: A Hardware-Bound Exploit Despite the criticality and widespread impact of Java4Shell, several security firms noted that the vulnerability is difficult to exploit. In two separate reports, VulnCheck and Endor Labs highlighted that exploitation of the vulnerability is hardware-specific, depending on the Java version, the underlying server processor and the application running on it. Both research teams noted that the flaw affects CPUs supporting AVX-512 VBMI instructions, while ARM-based servers, including AWS Graviton, are not affected. VulnCheck said its researchers had successfully reproduced the vulnerability on Ice Lake hardware, adding that processors without AVX-512 VBMI and BW support use an alternative decoding path that does not contain the defect. Endor Labs noted that the affected processors include recent Intel and AMD server chips, which account for much of current cloud capacity. As of November 18, no attacks exploiting the vulnerability had been reported in the wild. CISA Mitigation Recommendations CISA recommended the following mitigation measures: Identify affected Java installations: review software inventories for Java Development Kits (JDKs) and Java runtimes, including those bundled with third-party applications, container images and appliances, as they may not appear as separate inventory entries Apply security patches: install relevant Java and vendor patches as soon as they become available, prioritizing internet-facing systems Implement safeguards: where immediate patching is not possible, implement temporary safeguards, such as validating and
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Java4Shell Vulnerability Allows Remote Attacks on Major Java Apps
  - Published: 2026-11-18T12:35:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/java4shell-vulnerability-remote/
  - Summary: A critical OpenJDK vulnerability could expose major Java applications to remote code execution, prompting CISA to urge organizations implement mitigations

### Cluster 656ea1ba73 — score 10

- Title: SCKit abuses ScreenConnect to deploy remote access and target technician sessions
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-11-13T21:31:44+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_products: Microsoft Defender, ScreenConnect
- tools_used: Microsoft Defender, ScreenConnect
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: Microsoft Defender, ScreenConnect
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
SCKit abuses ScreenConnect to deploy unauthorized remote access and target technicians. Explore the attack chain, mitigations, and Microsoft Defender XDR hunting. The post SCKit abuses ScreenConnect to deploy remote access and target technician sessions appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Credential theft Lateral movement Malware Vulnerability Threats intelligence Cyberattacker techniques, tools, and infrastructure Vulnerabilities and exploits Content types Research Products and services Microsoft Defender Microsoft Defender for Endpoint Microsoft Defender XDR Topics Actionable threat insights Incident response Threat intelligence Beginning on November 11, 2026, ConnectWise reported an active campaign of a threat actor gaining unauthorized access to cloud-hosted ConnectWise ScreenConnect instances belonging to managed service providers (MSPs). Microsoft Threat Intelligence has confirmed ConnectWise’s reported activity and we have also observed threat actors abusing ScreenConnect, a legitimate remote-support application, to install unauthorized remote-access clients and deploy a malicious worm, SCKit, on ConnectWise customer managed endpoints. Additionally, Microsoft analyzed the malicious worm’s behavior: deployment starts with commands issued through ScreenConnect to silently install an identical client connected to threat actor-controlled infrastructure. A batch launcher retrieves a PowerShell decoder that decrypts and extracts SCKit using device-specific key material. The toolkit establishes persistence through scheduled tasks and registry Run entries and deploys RelayTrap, a component designed to deliver a malicious payload to a connecting technician. We have identified that the worm targets IT support technician workstations using the hijacked authenticated ScreenConnect Session and uses the victim’s management console to distribute payloads to other managed devices. The resulting access to either target enables threat actors to remotely administer affected endpoints, execute commands, and deploy further tools independently of the legitimate support instance. Defenders should investigate technician workstations and downstream affected endpoints. Removing an unauthorized client alone does not remove the toolkit’s persistence or invalidate exposed web sessions. In this blog, we examine SCKit’s attack chain and payload components and provide mitigation guidance, indicators of compromise, and Microsoft Defender XDR advanced hunting queries to help organizations identify and disrupt this activity. ScreenConnect architecture and attack surfaces ScreenConnect, formerly ConnectWise Control, is a remote-support and access platform used by MSPs to administer customer devices, often alongside remote monitoring and management (RMM) software. Its operating model has three parts: Management instance. A cloud-hosted or on-premises ScreenConnect server provides the web console and manages sessions. Its relay service carries communication between the technician and endpoint clients. Technician workstation. Support staff sign in to the console through a browser and launch a local host client for interactive support. Customer endpoint. An installed guest, or access, client maintains unattended access and executes commands delivered through ScreenConnect. An Access session provides persistent, unattended access through the installed client. A Support session is a temporary connection that an end user joins for assistance. ScreenConnect also supports remote commands from the web console without an interactive technician session. The endpoint client receives the command and runs it on the customer device; the technician workstation is not an intermediary for that execution. Reported server-side entry through extensions Extensions are add-ons installed on the ScreenConnect server to add features or integrate with other products, including ticketing and RMM tools. ConnectWise Automate was formerly named LabTech; Labtech Plus is a third-party extension, not the Automate product itself. The RMM+ extension family exposes remote-command APIs protected by a separately configured passphrase rather than the technician’s normal console sign-in. ConnectWise’s advisory describes a reported authenticatio
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: SCKit abuses ScreenConnect to deploy remote access and target technician sessions
  - Published: 2026-11-13T21:31:44+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/
  - Summary: SCKit abuses ScreenConnect to deploy unauthorized remote access and target technicians. Explore the attack chain, mitigations, and Microsoft Defender XDR hunting. The post SCKit abuses ScreenConnect to deploy remote access and target technician sessions appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: SCKit abuses ScreenConnect to deploy remote access and target technician sessions
  - Published: 2026-11-13T21:31:44+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/
  - Summary: SCKit abuses ScreenConnect to deploy unauthorized remote access and target technicians. Explore the attack chain, mitigations, and Microsoft Defender XDR hunting. The post SCKit abuses ScreenConnect to deploy remote access and target technician sessions appeared first on Microsoft Security Blog .

### Cluster 6e155d51ef — score 10

- Title: The State of Ransomware Q3 2026
- Source: Check Point Research (threat_research_primary)
- Published: 2026-11-17T22:01:28+00:00
- Link: https://research.checkpoint.com/2026/the-state-of-ransomware-q3-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion
- actor_attribution: Cl0p, LockBit, ShinyHunters
- affected_industries: financial_services, government
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, data_breach
- actor_attribution: ShinyHunters, LockBit, Cl0p
- affected_industries: financial_services, government
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Ransomware reached record levels in Q3 2026, but the scale of activity is only part of what changed. The ecosystem producing those attacks is becoming increasingly fragmented: more ransomware brands are claiming victims, the top groups account for a smaller share of overall activity, and several major organizations are pushing back against high-value ransom demands. […] The post The State of Ransomware Q3 2026 appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 24 Android Malware 23 Artificial Intelligence 6 ChatGPT 3 Check Point Research Publications 484 Cloud Security 1 CPRadio 44 Crypto 3 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 434 How To Guides 13 Ransomware 7 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 The State of Ransomware Q3 2026 November 18, 2026 https://research.checkpoint.com/2026/the-state-of-ransomware-q3-2026/ Ransomware reached record levels in Q3 2026, but the scale of activity is only part of what changed. The ecosystem producing those attacks is becoming increasingly fragmented: more ransomware brands are claiming victims, the top groups account for a smaller share of overall activity, and several major organizations are pushing back against high-value ransom demands. At the same time, established operators such as Qilin and The Gentlemen remain firmly at the top, creating a landscape where strong leaders coexist with an increasingly crowded field of ransomware groups. Key observed findings Q3 2026 was the highest-volume quarter on record, with 2,830 victims published on data leak sites. July recorded 964 victims, August reached 1,042, and September recorded 824. The ransomware ecosystem became more fragmented. The top 10 groups’ share of victims fell for the third consecutive quarter, from 71% in Q1 to 58% in Q2 and 49% in Q3. For the first time, groups outside the top ten collectively accounted for the majority of observed victims. The number of active ransomware brands continued to grow. 117 distinct brands claimed at least one victim in Q3, up from 91 in Q2. Of these, 51 had not claimed a victim in Q2, and 42 made their first observed victim claims during Q3. Qilin remained on top with The Gentlemen still close by. Following the ending of Q2, when for the first time in 2026 Qilin briefly relinquished the leading position in favor of The Gentlemen for one month, Qilin reclaimed first place in July and August, before being overtaken yet again by The Gentlemen in September. Eventually Qilin remained in top position for yet another quarter by a narrow gap. LockBit’s decline continued throughout 2026. Once one of the most prolific ransomware operations, LockBit recorded fewer victims in each successive quarter and fell out of the top ten altogether in Q3. Several major organizations rejected high-value extortion demands. Stadler Rail, the Berlin state government and Manchester Airports Group were among the high-profile organizations that publicly refused ransom demands during the quarter. Ransomware payment patterns continued to diverge. Average payments fell 45% quarter over quarter to just over $1 million, while the median increased 167% to $400,000, pointing to different dynamics between routine payments and the largest extortion demands. The ShinyHunters-Clop dispute exposed rivalry within the ransomware ecosystem. ShinyHunters reportedly breached and defaced Clop’s leak site and demanded a public apology alongside payment, while Q3 also brought increased law-enforcement pressure against cybercriminal operations. To read the full findings, access the State of Ransomware Q3 2026 report from Check Point Research here . GO UP BACK TO ALL POSTS POPULAR POSTS Artificial Intelligence ChatGPT Check Point Research Publications OPWNAI : Cybercriminals Starting to Use ChatGPT Check Point Research Publications Threat Research Hacking Fortnite Accounts Artificial Intelligence ChatGPT Check Point Research Publications OpwnAI: AI That Can Save the Day or HACK it Away BLOGS AND PUBLICATIONS Check Point Research Publications Global Cyber Attack Reports Threat Research February 17, 2020 “The Turkish Rat” Evolved Adwind in a Massive Ongoing Phishing Campaign Check Point Research Publications August 11, 2017 “The Next WannaCry” Vulnerability is Here Check Point Research Publications March 12, 2026 “Handala Hack” – Unveiling Group’s Modus Operandi
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: The State of Ransomware Q3 2026
  - Published: 2026-11-17T22:01:28+00:00
  - Link: https://research.checkpoint.com/2026/the-state-of-ransomware-q3-2026/
  - Summary: Ransomware reached record levels in Q3 2026, but the scale of activity is only part of what changed. The ecosystem producing those attacks is becoming increasingly fragmented: more ransomware brands are claiming victims, the top groups account for a smaller share of overall activity, and several major organizations are pushing back against high-value ransom demands. […] The post The State of Ransomware Q3 2026 appeared first on Check Point Research .

### Cluster 6411ea2e82 — score 10

- Title: 16th November – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-11-16T14:44:36+00:00
- Link: https://research.checkpoint.com/2026/16th-november-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ransomware_extortion
- affected_industries: government, manufacturing_industrial
- affected_products: Apple iOS/macOS, ScreenConnect, VMware
- tools_used: SolarWinds
- cve_ids: CVE-2026-116928, CVE-2026-123039, CVE-2026-124194, CVE-2026-125350
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, active_exploitation
- affected_industries: government, manufacturing_industrial
- affected_products: ScreenConnect, VMware, Apple iOS/macOS
- tools_used: SolarWinds
- cve_ids: CVE-2026-123039, CVE-2026-124194, CVE-2026-116928, CVE-2026-125350
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 16th November, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES TSMC, a major Taiwanese semiconductor manufacturer, has confirmed a data breach at an unnamed cloud provider that exposed information about current and former employees. A hacker advertised 6.9 GB of allegedly stolen […] The post 16th November – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 16th November – Threat Intelligence Report November 16, 2026 https://research.checkpoint.com/2026/16th-november-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 16th November, please download our Threat Intelligence Bulletin . TOP ATTACKS AND BREACHES TSMC, a major Taiwanese semiconductor manufacturer, has confirmed a data breach at an unnamed cloud provider that exposed information about current and former employees. A hacker advertised 6.9 GB of allegedly stolen employee data on a cybercrime forum. According to the company, TSMC’s own systems and customer data were unaffected. Danish shipping and logistics giant Maersk confirmed unauthorized access and data theft from a legacy system inherited through an acquisition. The WhiteArmor extortion group claimed to have stolen approximately 100GB of information and demanded $5 million. Maersk stated that its other systems and customer operations remained unaffected. Japan’s Osaka city government disclosed a data breach exposing more than one million email addresses after attackers compromised a third-party email distribution service. The November 2 attack affected nearly 400 customers of the provider, exposing approximately 77 million addresses and enabling the distribution of fraudulent emails. ConnectWise, a US-based IT management software provider, disclosed attacks targeting its ScreenConnect remote access platform. Attackers compromised managed service provider environments and deployed malicious remote access tools on at least 288 endpoints across 48 organizations. The campaign may have involved the abuse of third-party extensions. AI THREATS Researchers analyzed a suspected AI-assisted intrusion targeting a US retailer. After security tools blocked the attacker’s initial commands, the intruder switched to apparently AI-generated scripts. The attacker extracted credentials from SolarWinds Orion monitoring software configuration files and accessed another server within minutes, demonstrating rapid adaptation during the intrusion. Researchers revealed an autonomous intrusion campaign in which attackers used DeepSeek and Zhipu GLM AI agents against at least 19 organizations during 25 operations. The campaign compromised 10 targets, including semiconductor, defense, and civil-society organizations, exposing credentials and sensitive information, including more than one million personal records. Researchers uncovered an exposed server belonging to Silent Lynx, a cyberespionage group targeting Central Asian governments. The attackers used a DeepSeek-powered AI agent to automate reconnaissance, data collection, and evidence removal. Compromised systems included Tajikistan’s railway network and government document infrastructure containing thousands of sensitive files. VULNERABILITIES AND PATCHES Check Point Research has traced attacks exploiting PHP2Shell through the Mobile Access portals of unpatched Check Point Security Gateways. Attackers then exploited CVE-2026-123039 to escalate privileges, achieved persistence, and in some cases wiped a VMware ESXi host. The first wave of attacks targeted Israeli organizations before expanding worldwide, and the tooling shows similarities to China-linked malware. Microsoft released November security updates fixing more than 1,000 vulnerabilities, including an actively exploited Outlook flaw, CVE-2026-124194, that can expose authentication data and enable user impersonation. The release also fixes 48 critical code-execution flaws, including CVE-2026-116928, which could let malicious email attachments run code without being opened. Google patched CVE-2026-125350, a high-severity vulnerability affecting Chrome’s XML processing component that has been exploited in active attacks. The November security update addresses nine vulnerabilities across supported platforms, including Windows, macOS, Linux, and Android. The fixes address security w
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 16th November – Threat Intelligence Report
  - Published: 2026-11-16T14:44:36+00:00
  - Link: https://research.checkpoint.com/2026/16th-november-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 16th November, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES TSMC, a major Taiwanese semiconductor manufacturer, has confirmed a data breach at an unnamed cloud provider that exposed information about current and former employees. A hacker advertised 6.9 GB of allegedly stolen […] The post 16th November – Threat Intelligence Report appeared first on Check Point Research .

### Cluster e260def6a2 — score 10

- Title: GTA VI isn’t out yet – and the scams are already in full swing
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-11-13T10:00:00+00:00
- Link: https://www.welivesecurity.com/en/cybersecurity/gta-vi-isnt-out-yet-scams-full-swing/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Cybercriminals attempt to cash in on the hype around the game, luring fans with malware-laced downloads and ‘early access’ that doesn’t exist
```

#### Full body

```
Digital Security GTA VI isn’t out yet – and the scams are already in full swing Cybercriminals attempt to cash in on the hype around the game, luring fans with malware-laced downloads and ‘early access’ that doesn’t exist Editor 13 Nov 2026 • , 13 min. read On November 19 th , 2026, Grand Theft Auto VI will be released for PlayStation 5 and Xbox Series X|S. But cybercriminals aren’t waiting for launch day. They have long been capitalizing on the hype around what’s arguably the most anticipated game of the decade, using fake leaks, malware-laced downloads, bogus online stores with rock-bottom prices, and fraudulent “early access” schemes to lure eager fans. Security experts at ESET expect such scams to proliferate as the release approaches and the holiday shopping season gets underway. Key points of this blogpost: GTA VI launches on November 19 th , 2026, for PlayStation 5 and Xbox Series X|S. Rockstar hasn’t announced a PC version, playable demo, beta, or early-access program. Fake GTA VI downloads can pose a serious security risk. Researchers found installers and “leaked” builds that carry infostealers, remote-access trojans, and destructive malware. A convincing storefront doesn’t guarantee a legitimate offer. Be wary of unusually low prices, cryptocurrency-only payments, and offers of a PC version or early access that contradict Rockstar’s official information. The risks are likely to shift around launch and the holiday shopping season , with pre-load scams, fake gift cards and bundles, and eventually bogus cheats, mods, and “PC version” downloads providing new lures. What’s real: the official facts It’s easy to see why the franchise makes such an attractive lure: Grand Theft Auto is one of the most successful entertainment properties of all time, with more than 470 million units sold worldwide, according to Rockstar Games. Before taking a closer look at the scams tied to GTA VI, let’s establish what Rockstar has actually announced. Pre-orders opened on June 25 th . According to Rockstar Games’ official pre-order announcement , the Standard Edition is priced at $79.99 in the United States, while the Ultimate Edition costs $99.99. Players who pre-order a digital copy have been able to pre-load the game since November 10 th . What Rockstar has not announced is just as important, particularly with so many fraudulent offers circulating online: there is currently no official beta, playable demo, or early-access program that would let players start playing GTA VI before release day. Nor has Rockstar announced a PC version, PC release date, or system requirements. This makes the official information a useful reality check: offers built around a supposed PC version, beta, demo, or early access are promising something Rockstar has never confirmed. Table 1. GTA VI scams at a glance Scam type What to watch out for What attackers are after Credential phishing Fake Rockstar, PlayStation, Xbox, or Steam login pages Gaming-account credentials, passwords, and other personal information Fake beta or early access Invitations to register, log in, pay a fee, or download software to access a nonexistent GTA VI beta, demo, or early-access version Credentials, money, personal data, or malware installation Crypto scams Fake GTA VI giveaways, token airdrops, investment opportunities, or “VIP access” requiring cryptocurrency Cryptocurrency payments or access to victims’ crypto assets Fake stores and pre-orders Cloned or impersonating storefronts offering GTA VI copies, keys, bundles, or versions that have not been officially announced Payment-card details, personal information, or direct payments Malware delivery Fake launchers, leaked builds, beta installers, APKs, cracks, cheats, or preload tools Installation of infostealers, remote-access trojans, or other malware Leaks fuel the hype The enormous anticipation for GTA VI has also made every new leak a magnet for attention. On August 18 th , an entity calling itself CyberLeek began releasing what i
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: GTA VI isn’t out yet – and the scams are already in full swing
  - Published: 2026-11-13T10:00:00+00:00
  - Link: https://www.welivesecurity.com/en/cybersecurity/gta-vi-isnt-out-yet-scams-full-swing/
  - Summary: Cybercriminals attempt to cash in on the hype around the game, luring fans with malware-laced downloads and ‘early access’ that doesn’t exist

### Cluster 0da83d7c79 — score 10

- Title: The forced audit: how AuditTeam’s OpsAgent framework masks ransomware as consulting
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-18T07:00:07+00:00
- Link: https://securelist.com/auditteam-opsagent-forced-audit/122031/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: critical_infrastructure
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: critical_infrastructure
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
How does a ransomware gang sell a “forced audit”? We break down AuditTeam’s OpsAgent implant, its Rust rewrite, and the extortion model demanding a consulting fee to delete stolen data.
```

#### Full body

```
Content menu Close Subscribe Threat Response Table of Contents Background Technical details Loaders OpsAgent main implant Commands description Additional modules AV/EDR killer module Cryptor module OpsAgent-rs (Rust version) Infrastructure Victims Attribution Conclusions Indicators of compromise File hashes File paths Authors Vladimir Nestor AuditTeam is an active threat group that uses the OpsAgent framework to compromise organizations across at least seven countries and territories. The campaign began in January 2026 and remained active through October 2026, at a minimum. In its ransom note, AuditTeam demands an “Audit & Consulting fee” in exchange for vulnerability reports. During this period, the group has infected dozens of organizations in Russia, Italy, the Philippines, Hong Kong, Senegal, Finland and China. The group’s leak site also claims victims in seven additional countries. OpsAgent provides file system management, process injection, privilege escalation, keylogging, screenshot capture, and network pivoting. During the campaign OpsAgent was transitioned from C++ to Rust while adding new capabilities including interactive shells and WebSocket upgrades. Its command-and-control domains use Amazon CloudFront subdomains, which OpsAgent discovers via a public GitHub repository. Two specialized modules extend its functionality. An antivirus/endpoint detection and response (AV/EDR) killer module installs a digitally signed Beijing Jiangmin Antivirus driver to terminate security products. A cryptor module encrypts files using AES-CBC or ChaCha20 with X25519 key exchange and targets database processes for termination prior to doing so. Background On March 10, 2026, we discovered suspicious activity targeting an organization in Hong Kong. The tool used was OpsAgent, a framework designed to resemble a penetration testing utility. Further investigation revealed attacks in additional countries, prompting an active research phase. This implant offers extensive operator capabilities, including host reconnaissance, shellcode injection via named pipes, and lateral movement through agent networks based on compromised hosts. Analysis indicates OpsAgent was used by AuditTeam. The group was first mentioned publicly by dbdigest.com in March 2026. On June 25, 2026, DeXpose reported that AuditTeam had claimed responsibility for an attack on a Russian organization and listed it on its leak site. AuditTeam leaves a ransom note threatening to release stolen data unless a fee is paid. They call this fee the “Audit & Consulting fee.” According to the note, payment results in a vulnerability report being delivered to the victim instead of leaking the stolen data archive to the public internet. While the note does not mention file encryption, it is left by the cryptor module. Therefore, if a victim sees the note, their files are already encrypted. The ransom note GitHub commit history shows the campaign started on January 5, 2026. The leak site lists its first victim on February 21, 2026. Dozens of machines across at least seven countries were infected. On August 19, 2026, a C2 domain for the new OpsAgent version was added to the public repository and subsequently used in attacks. AuditTeam activity timeline Technical details Loaders OpsAgent uses multiple loader variants during its campaign. All discovered loaders unpack OpsAgent by parsing the MZ header and transferring execution to the entry point of the unpacked payload. The C loader was discovered in April 2026. It injects shellcode into msiexec.exe using standard API calls: CreateProcessA , VirtualAllocEx , WriteProcessMemory , and CreateRemoteThread . The .NET loader was found in June 2026. It uses NtQueueApcThread instead of direct process creation for injection. It contains strings such as DApc , DProtect , DResume , and msiexec.exe . Both the C and .NET loaders inject shellcode into a separate target process. They are also protected by OLLVM obfuscation with control-flow flattening ena
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: The forced audit: how AuditTeam’s OpsAgent framework masks ransomware as consulting
  - Published: 2026-11-18T07:00:07+00:00
  - Link: https://securelist.com/auditteam-opsagent-forced-audit/122031/
  - Summary: How does a ransomware gang sell a “forced audit”? We break down AuditTeam’s OpsAgent implant, its Rust rewrite, and the extortion model demanding a consulting fee to delete stolen data.

### Cluster a46657a5b4 — score 10

- Title: Ransomware at the hypervisor layer: how attackers use ESXi and vCenter features for malicious purposes
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-13T09:00:43+00:00
- Link: https://securelist.com/esxi-ransomware/121959/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky experts analyze a recent ransomware incident and discuss why the hypervisor layer remains difficult to monitor, what common access paths adversaries use to reach it, and how to protect your ESXi systems.
```

#### Full body

```
Content menu Close Subscribe Threat Response Table of Contents Why the hypervisor changes ransomware economics The visibility asymmetry How attackers reach the virtualization layer Vulnerability exploitation Active Directory integration Recommendation for defenders Credential reuse from the Windows estate Backup infrastructure as a credential bridge Persistence on the management plane Turning vCenter into an offensive control plane Why ESXi configuration change via vCenter is a trust-boundary failure High-fidelity detection opportunity Notes on ESXi abuse: living-off-the-land tools and controls to monitor Inside the ESXi impact phase Stopping virtual machines before impact Payload delivery and FlowSsh behavior The three-hour self-test window Pre-impact detection opportunity Detonation command and evidence confidence Partial overwrite and what 2 KB actually implies Destroying the recovery path first Detection and investigation High-confidence detection opportunities Example correlation logic Incident response at the virtualization layer First 30 minutes after incident discovery Containment priorities Architecture hardening derived from the case Treat vCenter as Tier 0 Separate virtualization identities from ordinary enterprise administration Keep direct ESXi management paths narrow Make the logging path independent of the affected host Design backup as a separate security boundary Conclusion MITRE ATT&CK mapping Incident indicators Minimum virtualization forensic collection set Authors Elsayed Elrefaei Mohamed Ghobashy Our Global Emergency Response Team (GERT) recently investigated an engagement in which an adversary destroyed an organization’s virtualization estate over a 10-day period. The campaign targeted four ESXi hosts, every virtual machine hosted on them, both vCenter Server Appliances, and all connected backup infrastructure. The ransom notes identified the attacker as the BlackNevas group, first observed in November 2024. What’s interesting about this attack is that no virtualization layer vulnerabilities were exploited: no guest-to-host escapes, no hypervisor memory corruption. Every action taken against ESXi was executed through legitimate VMware management interfaces. In September 2021, the Babuk ransomware source code was leaked online, including its ESXi version, which made ESXi ransomware accessible to cybercriminals with relatively low technical skills. At least ten subsequent ransomware families have leveraged this leaked code, including groups that otherwise lacked the expertise to develop ESXi-compatible ransomware lockers from scratch. We saw multiple operators using Babuk-derived ESXi lockers along with the leaked LockBit Windows builds. It is worth noting that while the Babuk ESXi version may target both old and up-to-date systems, the target organizations run unsupported ESXi versions, making them easier to attack. This article examines why the hypervisor layer remains difficult to monitor, what common access paths adversaries use to reach it, and how they establish persistence on the management plane. We’ll also look into the architecture of ESXi encryptors, the deliberate destruction of backup infrastructure, and the log sources that enable post-incident reconstruction. At the end of this article, we’ll provide indicators of compromise recovered during the investigation. Ten days of dwell time from initial access to the destructive phase. Timeline reconstructed from incident evidence Why the hypervisor changes ransomware economics Virtualization enables cost-effective and efficient resource management, simplifies simultaneous updates and policy enforcement. However, at the same time it reduces the number of control points and enables broader impact in case of a cyberattack. In non-virtualized environments, a single guest compromise normally affects one operating system. Compromise of the virtualization management plane gives the attacker access to many hypervisor hosts, while direct impact on an ESXi d
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Ransomware at the hypervisor layer: how attackers use ESXi and vCenter features for malicious purposes
  - Published: 2026-11-13T09:00:43+00:00
  - Link: https://securelist.com/esxi-ransomware/121959/
  - Summary: Kaspersky experts analyze a recent ransomware incident and discuss why the hypervisor layer remains difficult to monitor, what common access paths adversaries use to reach it, and how to protect your ESXi systems.

### Cluster 315e580651 — score 10

- Title: Regional Insights: 2027 State of Threat Intelligence
- Source: Recorded Future (threat_research_primary)
- Published: 2026-11-19T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/2027-soti-regional-summaries
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Regional findings from the 2027 State of Threat Intelligence report: how security teams in North America, EMEA, APJ, and LATAM use intelligence and AI.
```

#### Full body

```
Regional Insights: 2027 State of Threat Intelligence Recorded Future’s 2027 State of Threat Intelligence report surveyed 768 security professionals worldwide on how they use threat intelligence today, how they apply AI to it, and where they plan to invest. The report presents the global findings. The regional executive summaries in this blog cover insights from the same survey, breaking data down by global region into dedicated briefs covering the specific conclusions for cybersecurity leaders in North America , EMEA , APJ , and LATAM . Start with your region to see how your peers are approaching threat intelligence, and read the others for a wider view. North America (United States and Canada) In North America, threat intelligence now informs decisions well beyond the security organization. Five teams consume it on average, and 85% of organizations surveyed have teams outside core security using it , including risk management (54%), fraud prevention (44%), and risk and compliance (44%). With intelligence supporting this many teams, 81% plan to invest more in the next 12 months. The challenge is getting the right intelligence to each of those teams in a form they can act on. Doing that depends on how well intelligence comes together, and this is an ongoing effort for many programs. Most surveyed organizations (63%) draw on four or more intelligence vendors. Only 21% combine that external intelligence with their own internal telemetry in a single platform, where analysts can see which threats apply to their environment. Consolidation plans reflect this. Of the 76% planning to consolidate, the largest share are doing it to improve correlation across signals (40%), compared with only 8% who cite cost. Moving intelligence from those sources to risk owners is also largely manual. 54% put intelligence into action manually across tools and processes. Among organizations sharing intelligence outside security, 38% rely on ad hoc messages or scheduled reports. Manual handoffs make it harder to see what risk owners did with the intelligence and whether it worked. While 98% measure program value, 28% track whether triggered actions were effective. Only 22% report closed-loop operationalization, where stakeholders act on intelligence, the results are validated, and those results inform the program’s priorities and collection. AI is already part of this work for nearly all respondents ( 98% ), and 60% use agents that take actions inside their intelligence tools. Leaders become more cautious as the stakes rise: comfort with letting AI act falls from 71% for summarization to 56% for enforcement actions. The leading barriers are lack of auditability (40%) and unproven accuracy (31%). 73% say intelligence regularly feeds their AI and automation systems or is a core input to them. That makes the quality and correlation of their intelligence a factor in how far they can trust AI to act. Risk owners can come from procurement, legal, fraud, corporate security, or communications. Threat intelligence innovation means getting the intelligence to the right person to make decisions and take action based on that intelligence. Rich LaTulip North America Field CISO at Recorded Future This summary draws on responses from 347 North American security professionals . They were part of a global survey of 768 that asked how organizations use threat intelligence, apply AI to it, and plan future investments. The full report covers how intelligence is expanding across the business, what full visibility requires, and what stands between teams and proven impact. Europe, Middle East, and Africa (EMEA) Across EMEA, threat intelligence now informs decisions well beyond the security organization, and leaders plan to extend it further. 86% of organizations surveyed have teams outside core security using it , and 35% name expanding intelligence to more teams as a top priority for the next two years. Budgets support that goal. Half (50%) spend more than $500K a year on exte
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Regional Insights: 2027 State of Threat Intelligence
  - Published: 2026-11-19T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/2027-soti-regional-summaries
  - Summary: Regional findings from the 2027 State of Threat Intelligence report: how security teams in North America, EMEA, APJ, and LATAM use intelligence and AI.

### Cluster 5ce28a4ea0 — score 10

- Title: What Is Threat Intelligence Worth? 142 Security Teams Did the Math.
- Source: Recorded Future (threat_research_primary)
- Published: 2026-11-17T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/threat-intelligence-roi
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure, education, financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: financial_services, critical_infrastructure, education
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We surveyed 142 Recorded Future customers on the value of threat intelligence. See the highlights, then get the full ROI Report.
```

#### Full body

```
What Is Threat Intelligence Worth? 142 Security Teams Did the Math. Your board doesn't ask how many alerts your team closed. It wants to know what your security investments are worth in terms it already uses: revenue protected, losses avoided, and costs reduced. That question is hard to answer when attacks are faster and cheaper to scale, the attack surface reaches well past the perimeter, and teams are expected to do more without more headcount. We wanted real numbers on the value Recorded Future customers have experienced, so we partnered with UserEvidence to publish our 2027 ROI Report. It was built from a survey that asked 142 Recorded Future customers about the returns they're seeing. The average result is a 468% annual ROI.* Here's a first look at how they get there. Visibility comes first: 75% found risks they didn't know they had Security teams can't act on what they can't see. Many of the biggest blind spots sit outside the corporate network, where typosquatted domains, leaked credentials, and vendor exposure never trigger an internal alert. Of the customers surveyed, 75% gained visibility into previously unknown risks, the most commonly reported outcome. Among those who gained new visibility, 72% identified lookalike domains before they were weaponized, and 67% caught compromised credentials circulating on dark web markets. For Citizens Financial Group, that outside-in view of exposed credentials means a smaller attack surface and fewer openings for attackers: The ability to identify compromised credentials has reduced our attack surface and helped to mitigate the potential of initial access. Jordan Carpenter Senior Cyber Threat Intelligence Analyst, Citizens Financial Group Style padding-top-0,padding-bottom-0 Efficiency follows: An Average of 28 hours back every week When intelligence arrives already collected, enriched, and scored, analysts spend their time acting on it instead of assembling it. Teams reported reclaiming an average of 28 hours per week across seven core security workflows. They also shifted an average of 26% of tasks from senior to junior analysts, freeing experienced staff for higher-value actions like proactive threat hunting and expanding threat coverage across more attack surfaces. Most are putting that recovered time to work: 70% plan to reinvest it in proactive threat hunting. Then business risk drops Faster, better-informed teams stop threats earlier. Customers reported mean time to detect falling 48% and mean time to remediate falling 50%. They also reported fewer fraud losses, less downtime, and lower cyber insurance premiums. These are the outcomes a CFO and a board often recognize. The posture shift is clear in the sentiment data as well. 90% say Recorded Future has strengthened their overall security posture, and 85% say it helped them move from reactive to proactive. For South Carolina Critical Infrastructure Cybersecurity, reduced business risk translates into tens if not hundreds of thousands of dollars in savings: Without Recorded Future intelligence, these exposures would have remained unknown until an adversary operationalized them, at which point the cost shifts from a brief remediation call to a full incident response engagement, which for a mid-size municipality or school district can easily exceed $50,000–$200,000 in recovery costs alone. Ryan Cummings Cyber Threat Intelligence Analyst, South Carolina Critical Infrastructure Cybersecurity Style padding-top-0,padding-bottom-0 Value that's hard to get elsewhere For every outcome we measured, a clear majority said they could not have fully achieved it without Recorded Future. That includes faster detection: 82% said they couldn't have fully achieved it on their own without Recorded Future. What's in the full report The ROI Report shows exactly how the 468% is calculated, including the dollar value behind each category, the assumptions, and the customer stories that bring the data to life. It also covers: How customers are using
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: What Is Threat Intelligence Worth? 142 Security Teams Did the Math.
  - Published: 2026-11-17T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/threat-intelligence-roi
  - Summary: We surveyed 142 Recorded Future customers on the value of threat intelligence. See the highlights, then get the full ROI Report.

### Cluster 8721dda70c — score 10

- Title: The challenge of defending against bulletproof dead drops on public blockchains
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-11-18T11:00:00+00:00
- Link: https://blog.talosintelligence.com/the-challenge-of-defending-against-bulletproof-dead-drops-on-public-blockchains/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The evolution of malware command-and-control (C2) infrastructure has shifted away from fragile, centralized servers and hardcoded domains toward resilient, decentralized blockchain networks that eliminate single points of failure.
```

#### Full body

```
The challenge of defending against bulletproof dead drops on public blockchains By Chetan Raghuprasad Wednesday, November 18, 2026 06:00 On The Radar The evolution of malware command-and-control (C2) infrastructure has shifted away from fragile, centralized servers and hardcoded domains toward resilient, decentralized blockchain networks that eliminate single points of failure. Threat actors are leveraging immutable public ledgers such as Bitcoin transactions, EVM smart contracts via techniques like EtherHiding, TRON wallets, and Solana memo programs to store, mask, and persistently update their operational endpoints. By executing read-only remote procedure call (RPC) queries to retrieve encrypted C2 configurations directly into compromised endpoint memory, adversaries can continuously bypass traditional perimeter defenses and domain seizures. Modern cybersecurity requires a fundamental shift away from static domain blocklists toward monitoring anomalous outbound JSON-RPC traffic, analyzing endpoint memory, and treating blockchain infrastructure as an active threat communication channel. The command-and-control (C2) channel is the operational backbone of any persistent malware campaign. It is also the most fragile component. The moment an actor's C2 infrastructure is identified and reported to the hosting provider, the domain registrar, or law enforcement, the campaign's operational capability collapses. This fundamental asymmetry, where defenders need to identify only a single infrastructure link to disrupt an operation, has driven a multi-decade arms race in resilience techniques, spanning from fast flux DNS evasion to decentralized and peer-to-peer architectures. Traditional C2 infrastructure where malware beacons to a hardcoded domain or IP address is volatile by design. Security researchers or incident responders who identify the C2 address can trigger a response. The hosting provider can null-route the IP addresses and the domain registrars can suspend malicious domains under abuse policies, law enforcement can obtain court orders compelling infrastructure seizure, and threat intelligence vendors push blocklist updates that cut off the malware from its C2 links across several compromised endpoints simultaneously. This single point of failure model renders sophisticated malware families inactive once their C2 is identified and sinkholed. By redirecting malware traffic to researcher-controlled servers, researchers can not only disrupt the botnet but map the full victim community, gather forensic telemetry, and notify affected organizations. The arms race Threat actors have progressively hardened their C2 infrastructure through several evasion techniques to outpace defensive capabilities. Amongst these techniques, some of the popular approaches include the employment of domain generation algorithms (DGA), content delivery network (CDN) domain fronting, peer-to-peer (P2P) architecture, and dead drop resolvers. DGAs replace static, hardcoded server domains with dynamically generated domains. Malware programmed with a shared mathematical seed computes hundreds or thousands of pseudorandom domain names on a scheduled basis, systematically attempting to resolve each one until it establishes contact with an address registered by the threat actor. While this technique prevents defenders from neutralizing an entire operation by simply seizing or blocklisting a single domain, defenders counteracted DGAs by reverse engineering the generation algorithms, predicting future domains for proactive sinkholing, and applying machine learning models to detect algorithmically generated strings within enterprise DNS queries. The CDN domain fronting technique evolved to bypass perimeter inspection mechanisms by exploiting discrepancies between the transport and application layers of encrypted web traffic. By initiating a TLS handshake with a legitimate, reputable domain hosted on a major CDN and specifying a covert, malicious host inside the enc
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: The challenge of defending against bulletproof dead drops on public blockchains
  - Published: 2026-11-18T11:00:00+00:00
  - Link: https://blog.talosintelligence.com/the-challenge-of-defending-against-bulletproof-dead-drops-on-public-blockchains/
  - Summary: The evolution of malware command-and-control (C2) infrastructure has shifted away from fragile, centralized servers and hardcoded domains toward resilient, decentralized blockchain networks that eliminate single points of failure.

### Cluster 912dd8fe31 — score 10

- Title: ARTEX and beyond: AI-enabled penetration testing platforms
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-11-13T20:57:13+00:00
- Link: https://blog.talosintelligence.com/artex-and-beyond/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, ransomware_extortion
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft, active_exploitation
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
AI-enabled penetration testing and red team frameworks can automate and chain reconnaissance, vulnerability testing, and follow-on actions, lowering the skill threshold for attackers and accelerating intrusions when the tools are misused.
```

#### Full body

```
ARTEX and beyond: AI-enabled penetration testing platforms By Cisco Talos Friday, November 13, 2026 15:57 Threat Advisory Cisco Talos is tracking the growing in-the-wild usage of AI-enabled penetration testing frameworks. AI-enabled penetration testing and red team frameworks can automate and chain reconnaissance, vulnerability testing, and follow-on actions, lowering the skill threshold for attackers and accelerating intrusions when the tools are misused. Talos has seen full automation of the attack chain by these frameworks, which not only use free and open-source tools, like nmap and nuclei, but also take advantage of internet mapping services like Censys and Shodan, CAPTCHA bypass services, credential leak management services, residential proxies, and even hash cracking services. This is the case of Hephaestus, which we mentioned in our previous report . Although these frameworks all have the same purpose, they come in different flavors. Some, like Hephaestus, are command line tools which can be deployed with a single script on a VPS and are completely controllable via Telegram. PentAGI has a web interface to monitor the agent activity with a full attack chain graph design and monitoring. Talos found more than 700 instances of currently reachable PentAGI instances on the internet. HexStrike AI integrates with many different clients like Claude Code, VS Code, or any other client that supports MCP. One such framework making waves, ARTEX, has enabled threat actors to scale offensive operations, compressing work that may have previously taken skilled teams hours or days into activity that can unfold at machine speed. Talos’ analysis of ARTEX-associated IP addresses identified a diverse set of tools concurrently present on that infrastructure, reinforcing ARTEX’s role in a broader and varied threat environment. AI-enabled frameworks: A new reality Before we delve into ARTEX, it is clear that these frameworks are the new reality. Their evolution will most likely include autonomous lateral movement followed by data identification and exfiltration. The precursor of this can already be seen in the victim prioritization of the Volta Infostealer, described in detail in this Talos report . It is highly likely that future attack chains involving these frameworks will culminate in data exfiltration and ransomware activation, all being done autonomously by one of these frameworks. Such evolutions present new challenges to defenders: It reduces the time it takes to detect a compromise without any known indicators of compromise (IOCs). We provide guidance to help overcome this challenge in the Recommendations section. After malicious activity is identified, it is crucial to contain the incidents. These frameworks work at speeds that can make it impossible for human operators to identify, assess and react in time to disrupt the attack. These frameworks make mitigation and containment, along with a battle-tested cybersecurity incident response plan, imperative for organizations' resiliency. Defenders using AI can be a force multiplier to provide much-needed improvements, both in the speed and scale of response to such attacks. ARTEX ARTEX is an AI-enabled penetration testing framework developed under the pseudonym Autumn-27 and published on GitHub in July 2026. An operator gives it a target and objective, a planner agent breaks the objective into tasks, worker agents perform them using security tools, and the framework records assets, findings, and progress in a shared graph. ARTEX can use different large language models (LLMs) and requires relatively little operator input after a task begins. It was designed for authorized security testing, but recent public reporting documented its use in both criminal and targeted intrusion campaigns within weeks of its release. It is important to note that ARTEX is not natively bundled with any traditional command-and-control (C2) framework, though the Model Context Protocol (MCP) extensibility layer mea
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: ARTEX and beyond: AI-enabled penetration testing platforms
  - Published: 2026-11-13T20:57:13+00:00
  - Link: https://blog.talosintelligence.com/artex-and-beyond/
  - Summary: AI-enabled penetration testing and red team frameworks can automate and chain reconnaissance, vulnerability testing, and follow-on actions, lowering the skill threshold for attackers and accelerating intrusions when the tools are misused.

### Cluster 35c455e95d — score 10

- Title: Horizon3 Brings Autonomous Pentesting to Defense Customers Through IL4 Authorization
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-11-18T15:10:00+00:00
- Link: https://horizon3.ai/news/press-release/horizon3-brings-autonomous-pentesting-to-defense-customers-through-il4-authorization/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
NodeZero for Defense Internal Pentesting is now authorized and available to eligible Department of War customers in Impact Level 4 (IL4) environments. Defense teams can use it to identify exploitable paths through their internal networks, prioritize fixes based on mission risk, and verify that those fixes block the paths.
```

#### Full body

```
Horizon3 Brings Autonomous Pentesting to Defense Customers Through IL4 Authorization Business Wire November 18, 2026 Press Releases NodeZero for Defense Internal Pentesting capability is immediately available to help Department of War teams uncover exploitable attack paths and verify remediation San Francisco, November 18, 2026 — Horizon3 announced today that the Impact Level 4 (IL4) offering of NodeZero, NodeZero for Defense, is authorized and immediately available to Department of War (DOW) customers. The milestone gives defense teams a production-safe way to identify how attackers could compromise internal networks, prioritize the weaknesses that put missions at risk, and verify that remediation blocks those attack paths. NodeZero for Defense is included as a core service offering in the IL4 authorization appendix, building on the established NodeZero for Government, its FedRAMP Class D (High) foundation, to support defense customers with IL4 requirements. The authorization announced today specifically covers Internal Pentesting with Risk Based Exposure Management within the approved environment and scope. “An authorization opens the door, but what matters to mission leaders is what their teams can do with it,” said Snehal Antani, CEO and co-founder of Horizon3. “A single compromised account or exposed system can give an adversary a foothold. Defense teams need to know where that foothold could lead and which fixes will stop the adversary’s progress. Bringing the NodeZero for Defense Internal Pentesting capability into IL4 environments gives those teams a repeatable way to answer those questions and prove their defenses are improving.” From an Initial Foothold to Mission Impact Individual findings rarely explain the full risk to a mission. A weak password, excessive privilege, or misconfigured system may become more consequential when an attacker connects it with other weaknesses to reach critical assets. NodeZero for Defense assesses internal networks from a NodeZero host deployed within the customer’s private environment. Its autonomous penetration testing identifies exploitable paths an attacker could use after gaining an initial foothold, showing how vulnerabilities, credentials, and misconfigurations can combine to enable lateral movement, privilege escalation, and access to sensitive systems or data. That context helps security teams direct remediation toward demonstrated exposure. Rather than treating every finding as an isolated task, teams can identify changes that break attack paths and address weaknesses contributing to multiple routes to compromise. As fixes are applied, targeted retesting verifies whether those changes blocked the identified paths. Repeated assessments help teams evaluate exposure as their environments change and provide mission leaders with evidence of what was exploitable, what was fixed, and what requires further attention. Expanding Access to Continuous Security Validation The IL4 milestone extends Horizon3’s work to make autonomous security validation accessible to federal and defense organizations. Through its deployment, NodeZero for Defense enables eligible defense teams to incorporate repeatable internal penetration testing into their security programs and use verified results to guide risk decisions. NodeZero for Defense authorized Internal Pentesting capability is available now to Department of War customers. To discuss deployment requirements, visit horizon3.ai/vertical/federal/ . About Horizon3 Horizon3, the AI-Native Proactive Security Company behind NodeZero®, shifts the advantage from attackers to defenders by giving organizations the power to fight AI with AI. NodeZero, the World’s Best AI Hacker™, autonomously tests defenses at machine speed, safely uncovers and prioritizes exploitable attack paths, instantly verifies fixes, and drives a continuous hack, fix, verify loop. More than 7,000 organizations, including global defense agencies, Fortune 10 enterprises, multinational ba
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Horizon3 Brings Autonomous Pentesting to Defense Customers Through IL4 Authorization
  - Published: 2026-11-18T15:10:00+00:00
  - Link: https://horizon3.ai/news/press-release/horizon3-brings-autonomous-pentesting-to-defense-customers-through-il4-authorization/
  - Summary: NodeZero for Defense Internal Pentesting is now authorized and available to eligible Department of War customers in Impact Level 4 (IL4) environments. Defense teams can use it to identify exploitable paths through their internal networks, prioritize fixes based on mission risk, and verify that those fixes block the paths.

### Cluster 3fa9ec72bf — score 10

- Title: Open by Default, Already Occupied: Threat Actors are Renting your Compute
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-18T14:38:55+00:00
- Link: https://www.rapid7.com/blog/post/tr-self-hosted-ai-renting-compute-exposed-servers
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: OpenAI/ChatGPT
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Full body

```
$ curl http://<exposed-host>:11434 /api/tags llama3.1:8b qwen3.6:27b glm-5.3:cloud nomic-embed-text:latest deepseek-v4-pro:cloud 103.249.201[.]108:9882/trigger/benign:latest gemma4:e4b zzvitals-beacon:latest huihui_ai/Qwen3.8-abliterated:latest gpt-4o:latest claude-3-opus:latest tinyllama:latest kimi-k2.7-code:cloud verif_sys:latest <tunnel>.trycloudflare[.]com/read/x5fa4534:b1 qwen2.5-coder:7b pwn_ctl_<this-host-ip>_ae52…:latest minimax-m3:cloud ttl[.]sh/dsv40110/dsv4probe:24h bge-m3:latest <tunnel>/L2V0Yy9zaGFkb3c → /etc/shadow Huihui-CyberStrike-OffSec-35B-abliterated smollm2:135m ops-verify:latest mistral-large-4:cloud <tunnel>/L3Byb2Mvc2VsZi9lbnZpcm9u → /proc/self/environ qwen3-embedding:0.6b gpt-4o:latest-copy-test local model cloud-routed or uncensored left by a third party Sample of model names returned by exposed Ollama servers. Green: left by a third party; outlined: cloud-routed or uncensored. Host-identifying parts redacted, infrastructure defanged. More than half of the exposed Ollama servers in this scan have already been touched by someone who is not the owner. I don't mean theoretically vulnerable. I mean visibly used: model names that are really callback addresses, tags stamped with the server's own IP, and Base64 strings that decode to /etc/shadow . Exposure statistics normally describe a risk. These model lists describe activity. An unauthenticated /api/tags call is a read-only request, and on thousands of machines it returns something close to a visitors' log. Below is what the data shows, where I think it points, and what I would do about it on Monday morning. I've labelled claims as [Observed] , [Interpretation] or [Hypothesis] so you can see where the evidence stops. First, the number I don't trust The scanner reported 14,064 findings across 11,891 IP addresses and labelled 14,060 of them vulnerable, 387 critical. If I put that in a headline it would travel well. It would also be wrong. [ Observed ] 148 IP addresses return the exact same fingerprint: Grafana on 3000, Jupyter on 8888, Ollama on three ports, each serving one model, llama3.1:8b . They sit with five different hosting providers in five countries. Another 281 addresses answer as two to five different products on the same port. Real servers rarely do that. Sensors and catch-all responders do it all day. [ Interpretation ] These are most likely deception infrastructure, run by researchers, vendors or threat actors watching who comes knocking. Remove those 429 addresses and the critical findings drop from 387 to 39. MLflow falls from 126 to 4. Honeypots look extremely vulnerable. That's the whole job description. Figure 1 What the scanner flagged versus what holds up Findings per product before and after removing the 148-host identical fleet and IP:port pairs that answer as multiple products. Ollama 8,193 flagged 7,675 hold up Streamlit 4,939 flagged 4,700 hold up Grafana 475 flagged 123 hold up Jupyter Notebook 265 flagged 38 hold up MLflow 126 flagged 4 hold up JupyterHub 66 flagged 11 hold up Streamlit, Grafana and JupyterHub results are presence checks (a health endpoint answers). They prove exposure, not compromise. Default-credential labels on Grafana were inferred by the scanner, not tested. Two more corrections before we go further. A Streamlit health check returning ok tells you an app is on the internet, not that it is exploitable. And the target list was pre-selected: 58% of the 20,354 hosts produced a finding, which is far above any internet-wide base rate. So treat the totals as a sample of a much larger population, not a census. What survives is still uncomfortable: 7,714 findings on 7,627 hosts where an AI or notebook API answered without authentication , almost all of them Ollama. Only 0.3% of all findings were served over HTTPS. The lesson for anyone producing exposure numbers, us included: if you count banners and health checks, you measure how the internet presents itself. You don't measure how it behaves. This is rented comput
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Open by Default, Already Occupied: Threat Actors are Renting your Compute
  - Published: 2026-11-18T14:38:55+00:00
  - Link: https://www.rapid7.com/blog/post/tr-self-hosted-ai-renting-compute-exposed-servers

### Cluster af8584c920 — score 10

- Title: Who Has Access to Claude? Bring AI Identity and Access Context Into Surface Command
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-17T14:26:29+00:00
- Link: https://www.rapid7.com/blog/post/em-claude-access-brings-ai-context-into-surface-command-asm-easm
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: data_breach
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Approving an AI service is only the starting point. As employees adopt Claude and their responsibilities change, security teams need to know who has access, which users hold administrative privileges, and whether those roles and group memberships still reflect the work they do. IBM’s 2025 Cost of a Data Breach Report found that, among studied organizations reporting an AI-related breach, 97% lacked proper AI access controls. The finding highlights a broader challenge: AI adoption needs security practices that extend beyond the initial approval, supported by information teams can use to review access with administrators and service owners. Rapid7 Surface Command now integrates with Claude’s Compliance API, bringing supported organization, user, role, group, and settings information into the same platform teams use to understand other assets and identities. The integration helps security teams make enterprise Claude access part of their existing review practices. Bring enterprise AI acce
```

#### Full body

```
Artificial Intelligence Who Has Access to Claude? Bring AI Identity and Access Context Into Surface Command Rapid7 Nov 17, 2026 | Last updated on Nov 17, 2026 | 3 min read DISCOVER SURFACE COMMAND Who Has Access to Claude? Bring AI Identity and Access Context Into Surface Command Table of contents Who Has Access to Claude? Bring AI Identity and Access Context Into Surface Command DISCOVER SURFACE COMMAND Table of contents Approving an AI service is only the starting point. As employees adopt Claude and their responsibilities change, security teams need to know who has access, which users hold administrative privileges, and whether those roles and group memberships still reflect the work they do. IBM’s 2025 Cost of a Data Breach Report found that, among studied organizations reporting an AI-related breach, 97% lacked proper AI access controls. The finding highlights a broader challenge: AI adoption needs security practices that extend beyond the initial approval, supported by information teams can use to review access with administrators and service owners. Rapid7 Surface Command now integrates with Claude’s Compliance API, bringing supported organization, user, role, group, and settings information into the same platform teams use to understand other assets and identities. The integration helps security teams make enterprise Claude access part of their existing review practices. Bring enterprise AI access into your security view An account list tells security teams who is present, while roles and group memberships help explain how access is organized and where further review may be needed. Surface Command’s integration with Claude’s Compliance API brings together: Organizations and users: Visibility into the Claude organization and its associated user accounts. Roles and groups: Context to understand users’ assigned roles and group memberships. Organizational settings: Available configuration information to support review of the enterprise Claude environment. With those details in Surface Command, practitioners can examine Claude identities alongside the other assets and identities they manage. That gives them a clearer basis for working with service owners to evaluate whether access remains appropriate as teams and responsibilities change. The integration focuses on administrative visibility. It does not ingest Claude conversation content, provide threat detection on Claude activity, or control Claude’s behavior. From a user record to an informed access review Consider a security practitioner reviewing administrative access to Claude. In Surface Command, they can inspect an imported user’s details, review their organization role and administrative status, and examine their group memberships. The relationship graph provides a visual view of how that user connects to the organization and its groups, making those associations easier to follow. The practitioner can then work with the service owner to confirm whether administrative privileges are still needed, whether group memberships reflect current responsibilities, and whether those assignments align with the organization’s access model. Surface Command provides information to support the review, while the team applies its policies and judgment to determine whether a change is needed. Support AI adoption with clearer accountability As Claude becomes part of everyday work, reviewing its users and access relationships becomes part of managing the environment. Bringing that information into Surface Command helps security practitioners and service owners work from a shared understanding of assigned roles and group memberships. It supports more informed access decisions and helps security leaders incorporate enterprise AI into established oversight practices. Get started with Claude and Surface Command today The integration is available through the Anthropic connector in the Rapid7 Extension Library. Using Claude’s Compliance API requires a Compliance API key and the appropriate en
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Who Has Access to Claude? Bring AI Identity and Access Context Into Surface Command
  - Published: 2026-11-17T14:26:29+00:00
  - Link: https://www.rapid7.com/blog/post/em-claude-access-brings-ai-context-into-surface-command-asm-easm
  - Summary: Approving an AI service is only the starting point. As employees adopt Claude and their responsibilities change, security teams need to know who has access, which users hold administrative privileges, and whether those roles and group memberships still reflect the work they do. IBM’s 2025 Cost of a Data Breach Report found that, among studied organizations reporting an AI-related breach, 97% lacked proper AI access controls. The finding highlights a broader challenge: AI adoption needs security practices that extend beyond the initial approval, supported by information teams can use to review access with administrators and service owners. Rapid7 Surface Command now integrates with Claude’s Compliance API, bringing supported organization, user, role, group, and settings information into the same platform teams use to understand other assets and identities. The integration helps security teams make enterprise Claude access part of their existing review practices. Bring enterprise AI acce

### Cluster 1ff0ebb45e — score 10

- Title: MDR Pricing: Comparing Asset-Based and Ingestion-Based Costs
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-13T16:37:29+00:00
- Link: https://www.rapid7.com/blog/post/dr-mdr-pricing-comparing-asset-ingestion-based-ingestion-costs
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
When comparing MDR pricing, it helps to understand what the same annual budget would buy from each provider. Two proposals with similar prices may give analysts access to different evidence, retain it for different periods, or leave your team with different responsibilities. Those differences can affect what happens when you need to investigate a compromised account or trace an attacker’s low-and-slow activity across your environment. For security leaders weighing asset-based against ingestion-based pricing, a useful comparison starts with the systems you need to protect and the logs required to investigate threats. Giving providers the same requirements and budget helps expose the decisions behind each quote, including what you would need to exclude or pay more to include. Asset-based vs. ingestion-based MDR pricing Under asset-based pricing, the charge is tied to a defined population of assets. You need to establish how the provider counts workstations, servers, cloud resources, and
```

#### Full body

```
MDR Must-Haves MDR Pricing: Comparing Asset-Based and Ingestion-Based Costs Emma Burdett Nov 13, 2026 | Last updated on Nov 13, 2026 | 7 min read DISCOVER RAPID7 MDR MDR Pricing: Comparing Asset-Based and Ingestion-Based Costs Table of contents MDR Pricing: Comparing Asset-Based and Ingestion-Based Costs DISCOVER RAPID7 MDR Table of contents When comparing MDR pricing, it helps to understand what the same annual budget would buy from each provider. Two proposals with similar prices may give analysts access to different evidence, retain it for different periods, or leave your team with different responsibilities. Those differences can affect what happens when you need to investigate a compromised account or trace an attacker’s low-and-slow activity across your environment. For security leaders weighing asset-based against ingestion-based pricing, a useful comparison starts with the systems you need to protect and the logs required to investigate threats. Giving providers the same requirements and budget helps expose the decisions behind each quote, including what you would need to exclude or pay more to include. Asset-based vs. ingestion-based MDR pricing Under asset-based pricing, the charge is tied to a defined population of assets. You need to establish how the provider counts workstations, servers, cloud resources, and other systems, alongside which data sources and service capabilities the price includes. A predictable asset count can help with budgeting, but the proposal still needs to explain any integration limits or additional service charges. At Rapid7, an asset is defined as any physical or virtual endpoint or server running a supported operating system within the monitored environment. With ingestion-based pricing, some of the cost depends on the volume of data collected or processed. The comparison needs to account for the included allowance, how billable volume is measured, and what happens when usage increases. Retention, search, and supporting infrastructure may also contribute to the overall cost, depending on the commercial model. At Rapid7, MDR customers have access to 13 months hot storage of logs as standard. Whichever approach you are evaluating, include the technology, analysts, and response support needed to deliver the service. A SIEM ingestion charge on its own cannot be compared directly with an MDR subscription that includes investigation and response. Both proposals need to account for the work your organization expects the provider to perform - this clarity is key to a successful partnership. How to make a like-for-like MDR pricing comparison Give each provider the same asset inventory, required data sources, retention needs, and response expectations, then ask what fits within your annual budget. Any exclusions should be visible in the proposal, so you can judge their operational consequences before committing. For example, one proposal might accommodate endpoint and identity data while requiring you to limit high-volume network sources. Another might accommodate those sources but lack an investigation capability your team needs. Looking at an MDR price per endpoint or per gigabyte will not resolve that difference; you need to see how the service uses the available data. Use these questions during an initial demonstration to turn the pricing discussion into a practical comparison. Comparison area What to ask the provider Evidence to request Rapid7’s approach Breadth of collection Which required sources fit within this budget? A list of included sources, exclusions, and extra charges. Asset-based pricing with unlimited ingestion, supporting native and third-party telemetry across endpoint, cloud, identity, email, and network. Confirm coverage for your required sources in the proposal. Depth of collection Which events and fields are collected, filtered, or summarized? Sample records showing what reaches the investigation platform. Rapid7 ingests and normalizes telemetry from supported technologies.
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: MDR Pricing: Comparing Asset-Based and Ingestion-Based Costs
  - Published: 2026-11-13T16:37:29+00:00
  - Link: https://www.rapid7.com/blog/post/dr-mdr-pricing-comparing-asset-ingestion-based-ingestion-costs
  - Summary: When comparing MDR pricing, it helps to understand what the same annual budget would buy from each provider. Two proposals with similar prices may give analysts access to different evidence, retain it for different periods, or leave your team with different responsibilities. Those differences can affect what happens when you need to investigate a compromised account or trace an attacker’s low-and-slow activity across your environment. For security leaders weighing asset-based against ingestion-based pricing, a useful comparison starts with the systems you need to protect and the logs required to investigate threats. Giving providers the same requirements and budget helps expose the decisions behind each quote, including what you would need to exclude or pay more to include. Asset-based vs. ingestion-based MDR pricing Under asset-based pricing, the charge is tied to a defined population of assets. You need to establish how the provider counts workstations, servers, cloud resources, and

### Cluster 3bcd6761c3 — score 10

- Title: GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-11-16T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, supply_chain
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage, active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Aurora Blum, Kelli Vanderlee, Jess Xia, David Mainor Executive Summary As threat actors increasingly move beyond basic prompting to deploying autonomous multi-agent frameworks , automated vulnerability exploitation pipelines, and alternative monetization schemes like LLMJacking , the adversarial AI landscape has reached a critical inflection point. In this update, Google Threat Intelligence Group (GTIG) and Mandiant examine how adversaries across the cyber crime, espionage, and information operations spectrum are operationalizing generative AI to compress attack timelines, scale operations, and execute multi-stage intrusions at machine speed. Key trends over the last quarter include: Shift to Autonomous Workflows and Multi-Agent Frameworks: Adversary tradecraft has continued to transition beyond manual prompting to deploying autonomous multi-agent offensive frameworks—such as ARTEX , CAIRN, CyberStrikeAI, and PentAGI—to execute multi-stage intrusions at greater operational
```

#### Full body

```
Threat Intelligence GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold November 16, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Written by: Aurora Blum, Kelli Vanderlee, Jess Xia, David Mainor Executive Summary As threat actors increasingly move beyond basic prompting to deploying autonomous multi-agent frameworks , automated vulnerability exploitation pipelines, and alternative monetization schemes like LLMJacking , the adversarial AI landscape has reached a critical inflection point. In this update, Google Threat Intelligence Group (GTIG) and Mandiant examine how adversaries across the cyber crime, espionage, and information operations spectrum are operationalizing generative AI to compress attack timelines, scale operations, and execute multi-stage intrusions at machine speed. Key trends over the last quarter include: Shift to Autonomous Workflows and Multi-Agent Frameworks: Adversary tradecraft has continued to transition beyond manual prompting to deploying autonomous multi-agent offensive frameworks—such as ARTEX , CAIRN, CyberStrikeAI, and PentAGI—to execute multi-stage intrusions at greater operational velocity. Automated Vulnerability Research and Exploitation: Threat actors are increasingly leveraging LLMs and agentic frameworks to fully automate the reverse engineering of patches via differential analysis, allowing them to rapidly weaponize n-day vulnerabilities and scale exploitation pipelines against internet-facing servers without human intervention. Monetization and Infrastructure Abuse : Financially motivated threat actors continue to profit from LLMJacking by stealing LLM credentials and cloud resources from compromised enterprise environments and reselling access to high-performance AI models through underground proxy services (e.g., LLM Mixers). LLM Integration in Information Operations (IO): State-sponsored groups, commercial Influence-as-a-Service (IaaS) vendors, and inauthentic political monetization networks now routinely use LLMs in their operations to produce synthetic media at scale, create localized personas, and automate cross-platform distribution. Targeted Espionage and Supply Chain Evolution: Cyber espionage groups are leveraging LLMs for target research, automated data analysis, and novel supply chain attack vectors—such as manipulating autonomous coding assistant configurations to drop backdoors during local execution. Grounded in telemetry from frontline Mandiant incident response engagements, global threat actor tracking, and live platform defenses, this report details how state-sponsored espionage groups, financially motivated cyber criminals, and IO threat actors are operationalizing LLMs in the wild. At Google, we are committed to developing AI boldly and responsibly. Our multifaceted defense strategy integrates proactive model-level safeguards, specialized threat intelligence, and targeted containment protocols to protect our customers and infrastructure. We continuously harden our models against misuse, mitigate malicious activity through proactive disruption of bad actor projects and accounts, and use our autonomous Google AI Threat Defense architecture and BeyondZero to operationalize security, continuous monitoring, and responding at machine speed across enterprise environments. Multi-Agent Frameworks in Cyber Intrusions While previous milestones documented in our quarterly research highlighted nascent adversary interest in agentic capabilities, GTIG and Mandiant have now observed multiple threat actors abusing open source, agentic penetration-testing (pentesting) frameworks to automate discrete phases and specific operational tasks during live intrusions. Threat actor adoption of these frameworks represents a paradigm shift towards intrusions occurring at machine speed, with the automated chaining of complex attack paths scaling operations significantly. W
```

#### Corroborating sources (1)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold
  - Published: 2026-11-16T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold/
  - Summary: Written by: Aurora Blum, Kelli Vanderlee, Jess Xia, David Mainor Executive Summary As threat actors increasingly move beyond basic prompting to deploying autonomous multi-agent frameworks , automated vulnerability exploitation pipelines, and alternative monetization schemes like LLMJacking , the adversarial AI landscape has reached a critical inflection point. In this update, Google Threat Intelligence Group (GTIG) and Mandiant examine how adversaries across the cyber crime, espionage, and information operations spectrum are operationalizing generative AI to compress attack timelines, scale operations, and execute multi-stage intrusions at machine speed. Key trends over the last quarter include: Shift to Autonomous Workflows and Multi-Agent Frameworks: Adversary tradecraft has continued to transition beyond manual prompting to deploying autonomous multi-agent offensive frameworks—such as ARTEX , CAIRN, CyberStrikeAI, and PentAGI—to execute multi-stage intrusions at greater operational

### Cluster d022c23d6b — score 10

- Title: Policy and Disclosure: 2026 Edition
- Source: Google Project Zero (offensive_vulnerability_research)
- Published: 2026-11-13T08:00:00+00:00
- Link: https://projectzero.google/2026/11/disclosure-policy.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure, active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Since 2021, Project Zero has followed a “90 + 30” vulnerability disclosure policy, allowing vendors up to 90 days to remediate a vulnerability plus an extra 30 days “soak time” for patch rollout. Our goal was to encourage faster patching and give vendors time to deliver patches to users. The advent of AI-assisted vulnerability discovery and exploitation has changed the threat landscape such that the vulnerability remediation timeline encouraged by our disclosure policy is clearly insufficient. LLMs have increased the speed at which attackers can find and exploit vulnerabilities, alongside the risk that multiple parties, including malicious ones, discover the same bug. A vulnerability reported today presents a much higher immediate risk to users than one reported last year. In this new environment, it is crucial that vendors move towards remediating vulnerabilities faster.
```

#### Full body

```
Since 2021, Project Zero has followed a â90 + 30â vulnerability disclosure policy, allowing vendors up to 90 days to remediate a vulnerability plus an extra 30 days âsoak timeâ for patch rollout. Our goal was to encourage faster patching and give vendors time to deliver patches to users. The advent of AI-assisted vulnerability discovery and exploitation has changed the threat landscape such that the vulnerability remediation timeline encouraged by our disclosure policy is clearly insufficient. LLMs have increased the speed at which attackers can find and exploit vulnerabilities, alongside the risk that multiple parties, including malicious ones, discover the same bug. A vulnerability reported today presents a much higher immediate risk to users than one reported last year. In this new environment, it is crucial that vendors move towards remediating vulnerabilities faster. LLMs have also decreased the time it takes for attackers to reverse engineer and exploit a vulnerability based on a patch, to the extent that zero patch-to-exploitation time is a reasonable, though imperfect, model of attacker behavior. Patch soak time is no longer meaningful in a world where attackers can almost immediately determine bug details from a patch, and can put users at risk by creating a false sense of secrecy. âPatch gapâ is the time between a fix being released for a security vulnerability and the user installing the relevant update. It is equally crucial that vendors reduce patch gap, either by reducing patch rollout time or using other strategies to protect users while remediation is in progress. LLMs have also increased the volume of vulnerabilities that Project Zero reports. We are finding several vulnerabilities a week in targets where we once found a few vulnerabilities a year. Aspects of our policy that require vendor negotiation or agreement, including determining whether a bug is fixed and whether grace period applies, are quickly becoming unmanageable. Today, we are announcing a new vulnerability disclosure policy, created with the following goals in mind: Encourage faster vulnerability remediation Encourage vendors to reduce âpatch gapâ Allow for the policy to be automated by both Project Zero and vendors Our new policy: âFull Xâ Vulnerabilities will be disclosed X days after they are reported to the vendor. Starting today, our policy is âFull 90â, i.e. vulnerabilities will be disclosed 90 days after they are reported to the vendor. On February 2, 2027, we will move to a âFull 60â policy where vulnerabilities are disclosed after 60 days. On January 3, 2028, we will move to a âFull 30â policy where vulnerabilities are disclosed after 30 days. We are also removing most âspecial casesâ from our disclosure policy, including grace period and variant policy. The only exceptions to our new policy are: Vulnerabilities actively exploited in the wild -- ITW vulnerabilities will be handled according to Googleâs application security vulnerability disclosure policy Public vulnerabilities -- Project Zero may make details of a vulnerability public, at our discretion, if the details have already been made public by others Vendor request -- We will make vulnerability details public if the vendor we reported it to requests it Why reduce remediation time gradually? Project Zero solicited feedback from the vendors we report the most vulnerabilities to as a part of developing this new policy. An overarching concern was that immediately changing the policy could harm users by making unfixed vulnerabilities available to attackers while vendors are in the process of improving their remediation processes and technology. While the benefits of delaying disclosure are declining due to the increased probability that attackers will discover a vulnerability during the embargo period, we still feel there are benefits in the short term. In addition, vendors mentioned two more subtle concerns. One was that an overly-aggressive dis
```

#### Corroborating sources (1)

- **Google Project Zero** (offensive_vulnerability_research)
  - Title: Policy and Disclosure: 2026 Edition
  - Published: 2026-11-13T08:00:00+00:00
  - Link: https://projectzero.google/2026/11/disclosure-policy.html
  - Summary: Since 2021, Project Zero has followed a “90 + 30” vulnerability disclosure policy, allowing vendors up to 90 days to remediate a vulnerability plus an extra 30 days “soak time” for patch rollout. Our goal was to encourage faster patching and give vendors time to deliver patches to users. The advent of AI-assisted vulnerability discovery and exploitation has changed the threat landscape such that the vulnerability remediation timeline encouraged by our disclosure policy is clearly insufficient. LLMs have increased the speed at which attackers can find and exploit vulnerabilities, alongside the risk that multiple parties, including malicious ones, discover the same bug. A vulnerability reported today presents a much higher immediate risk to users than one reported last year. In this new environment, it is crucial that vendors move towards remediating vulnerabilities faster.

### Cluster 30a4dbcb71 — score 10

- Title: Navigating Vulnerability Hysteria in the AI Era
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-11-19T19:46:44+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/navigating-vulnerability-hysteria-ai-era
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
This installment of the Reporters' Notebook video series examines the fallout from recent high-severity flaw disclosures, exploring how fears of AI-assisted exploits trigger widespread panic, operational disruptions, and growing warning fatigue.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Navigating Vulnerability Hysteria in the AI Era
  - Published: 2026-11-19T19:46:44+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/navigating-vulnerability-hysteria-ai-era
  - Summary: This installment of the Reporters' Notebook video series examines the fallout from recent high-severity flaw disclosures, exploring how fears of AI-assisted exploits trigger widespread panic, operational disruptions, and growing warning fatigue.

### Cluster a4a11d6f47 — score 10

- Title: Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote Takeover Without Login
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-16T12:34:21+00:00
- Link: https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: government
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Six flaws in Danfoss AK-SM800A refrigeration controllers could let a remote attacker take over a controller without logging in, Dutch security consultancy Midnight Blue said earlier this week. No patch is available, and the researchers say the newest firmware, version 5.4.0, does not fix the flaws. Government cybersecurity agencies in Belgium, Ireland and Germany told operators this week to
```

#### Full body

```
Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote Takeover Without Login  Swati Khandelwal  Nov 16, 2026 Vulnerability / Operational Technology Six flaws in Danfoss AK-SM800A refrigeration controllers could let a remote attacker take over a controller without logging in, Dutch security consultancy Midnight Blue said earlier this week. No patch is available, and the researchers say the newest firmware, version 5.4.0, does not fix the flaws. Government cybersecurity agencies in Belgium, Ireland and Germany told operators this week to take the controllers' management interfaces off the internet. For a controller left on the internet, updating the firmware, changing default passwords or turning on Strict mode is not enough on its own, the Belgian and Irish agencies said. Strict mode is a login protection that requires encrypted connections and session tokens, but one of the six flaws is in the gateway that enforces it. The AK-SM800A runs a store's fridges and freezers, and maintenance firms can manage it remotely. Such controllers were targeted in attacks in France starting October 11, and in a second wave across Europe that began last week. The attacks caused unwanted defrost cycles and destroyed stock. Germany's federal IT security agency, the BSI, says in a security notice that the AK-SM800A was involved in earlier incidents in which refrigeration units in several countries were tampered with. The agency has no information about any exploitation of the six new flaws, and neither other agencies nor researchers link the flaws to those incidents. The researchers examined firmware version 5.3.2, then the newest, and say every version up to and including it is affected. No CVE identifiers have been assigned. The researchers are keeping technical details private while they work on disclosure with Danfoss, the Danish company that makes the controllers. The vendor lists software package 5.4.0, dated November, as its newest release for the AK-SM800A. Its 5.4.0 readme and November update guide cover upgrade steps, and the guide adds a stricter password rule. Neither mentions a fix for any vulnerability. In a follow-up statement carried by trade publication Cooling Post, the researchers said 5.4.0 does not patch the flaws: "It's not really possible either because according to the file timestamp this firmware was likely built on October 29, before the second wave of cyber attacks and well before our vulnerability reports." The German agency first said in a press release this week that 5.4.0 was not affected. Later the same day, it changed that in a corrected statement : it cannot rule out for now that 5.4.0 is affected. The vendor's advisory page lists no advisory for the six flaws as of today, and no date for a fix has been published. Midnight Blue researcher Carlo Meijer found the six flaws in less than an hour of manual review, using firmware the vendor offers for download, and described them in a technical write-up . Five of the flaws are in web request handlers that do not require a login, inside a program that runs as root. Through one of them, the researchers ran code as root on older firmware, version 3.3.0, and they found the same bugs in 5.3.2. Strict mode closes almost all of the controller's web attack surface to users who have not logged in, including the flaw used in that demonstration. The sixth flaw is in the gateway that enforces Strict mode, a separate program that blocks every request except the login until a user has logged in. When the researchers ran firmware 5.3.2 in an emulator with Strict mode on, that flaw crashed the gateway. The crash could be turned into code execution with more work, the researchers say, and the gateway lacks basic exploit defenses such as stack canaries. With code running as root, an attacker could change the controller's settings, start defrost cycles and hide that activity from its logs. The controllers do not use secure boot, the researchers found, so an attacker co
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Six Unpatched Danfoss Refrigeration Controller Flaws Could Allow Remote Takeover Without Login
  - Published: 2026-11-16T12:34:21+00:00
  - Link: https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html
  - Summary: Six flaws in Danfoss AK-SM800A refrigeration controllers could let a remote attacker take over a controller without logging in, Dutch security consultancy Midnight Blue said earlier this week. No patch is available, and the researchers say the newest firmware, version 5.4.0, does not fix the flaws. Government cybersecurity agencies in Belgium, Ireland and Germany told operators this week to

### Cluster 3de0698531 — score 9

- Title: Why threat hunting should matter to every board
- Source: NCSC UK (government_authoritative)
- Published: 2026-11-17T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/blogs/why-threat-hunting-should-matter-to-every-board
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
Monitoring alone cannot detect every threat. Proactive threat hunting can expose gaps in defences and help organisations learn from others facing common threats.
```

#### Full body

```
Blog Post Download & print article PDF Download & print article PDF Why threat hunting should matter to every board Monitoring alone cannot detect every threat. Proactive threat hunting can expose gaps in defences and help organisations learn from others facing common threats. Patrick B J Studios via Getty Images Boards should have confidence that their organisation can detect and investigate emerging cyber threats, including activity that existing security alerts may miss. Organisations use a range of cyber security controls. They use security products, receive threat intelligence and monitor alerts from trusted providers. Many have well-developed processes for responding to known threats. But these measures can’t tell you everything about your ability to detect an attack. When a new attacker technique is identified, ask: could we detect this technique if it was used against us? If your organisation can’t answer that question, it may have gaps in its visibility or detection capability. As attackers use AI to operate at greater speed and scale, identifying and addressing these gaps becomes increasingly important. Organisations need to be able to identify signs of malicious activity early, rather than relying solely on detecting an attack once its effects become apparent. Threat hunting can help organisations test their ability to detect relevant attacker activity and expose gaps in their defences. This blog is for boards of organisations that monitor their systems for cyber threats, either themselves or through a third-party provider. It explains why threat hunting matters as threats evolve, and how boards can support their organisation to learn from what it finds and turn those insights into stronger cyber defences. Monitoring cannot detect every threat Security monitoring is fundamental to effective cyber defence. It helps organisations identify potentially malicious activity using established detections and alerts. But not every threat will trigger an existing alert. This is where threat hunting can help. Threat hunting is the proactive search for signs of cyber threats or intrusion that existing security rules and alerts may have missed. A hunt starts with a question or hypothesis, based on factors such as attacker behaviour or threat intelligence, and uses available security data to look for evidence. Threat hunting complements security monitoring; it doesn’t replace it. Focus on attacker behaviour Cyber defenders have traditionally made extensive use of indicators of compromise (IoCs), such as malicious IP addresses, domains, file hashes, or malware signatures. These are useful but they can change quickly. Attacker behaviours can be more enduring. Security professionals describe these behaviours as tactics, techniques and procedures (TTPs) . Put simply, TTPs describe how an attacker operates, rather than what specific tools or infrastructure they use. An IP address may change overnight. A technique for moving through a network may remain relevant for much longer. Focusing on attacker behaviour can therefore provide a more durable basis for detection. Threat hunting allows defenders to use knowledge of these behaviours to ask whether they can see evidence of them in their own environment. For more detail on how threat hunting works in practice, including the use of attacker TTPs, read our blog on observability and threat hunting . You can’t hunt what you can’t see Threat hunting depends on observability : having a clear and detailed view of what is happening across your organisation’s networks, systems and services. To investigate whether a particular attacker technique could be present, defenders need the right security data. Systems need to record relevant activity, and defenders need access to that data. Without it, they may be unable to see evidence that a technique has been used. This means a threat hunt can reveal more than malicious activity. It can also identify gaps in an organisation's visibility and detection c
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: Why threat hunting should matter to every board
  - Published: 2026-11-17T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/blogs/why-threat-hunting-should-matter-to-every-board
  - Summary: Monitoring alone cannot detect every threat. Proactive threat hunting can expose gaps in defences and help organisations learn from others facing common threats.

### Cluster b753f6689d — score 9

- Title: A phishing page interested in MX records, (Tue, Nov 17th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-11-17T10:56:38+00:00
- Link: https://isc.sans.edu/diary/rss/33526
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
I&#;x26;#;xe2;&#;x26;#;x80;&#;x26;#;x99;ve mentioned before in some of my diaries that it can be instructive to look at what appear to be &#;x26;#;xe2;&#;x26;#;x80;&#;x26;#;x9c;generic&#;x26;#;xe2;&#;x26;#;x80;&#;x26;#;x9d; phishing messages in detail from time to time, since some of them might prove not to be as generic as they initially appear. I came across a good example of this while going over phishing messages delivered to our handler inbox over the past few weeks, when a message that, at first glance, appeared to be a fairly ordinary attempt at stealing e-mail credentials turned out to lead to a page interested in collecting a little more information than just the victim&#;x26;#;39;s password.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: A phishing page interested in MX records, (Tue, Nov 17th)
  - Published: 2026-11-17T10:56:38+00:00
  - Link: https://isc.sans.edu/diary/rss/33526
  - Summary: I&#;x26;#;xe2;&#;x26;#;x80;&#;x26;#;x99;ve mentioned before in some of my diaries that it can be instructive to look at what appear to be &#;x26;#;xe2;&#;x26;#;x80;&#;x26;#;x9c;generic&#;x26;#;xe2;&#;x26;#;x80;&#;x26;#;x9d; phishing messages in detail from time to time, since some of them might prove not to be as generic as they initially appear. I came across a good example of this while going over phishing messages delivered to our handler inbox over the past few weeks, when a message that, at first glance, appeared to be a fairly ordinary attempt at stealing e-mail credentials turned out to lead to a page interested in collecting a little more information than just the victim&#;x26;#;39;s password.

### Cluster dd10fb744d — score 9

- Title: Accuracy Through Volume of Fire
- Source: TrustedSec (detection_response_operations)
- Published: 2026-11-19T05:00:00+00:00
- Link: https://trustedsec.com/blog/accuracy-through-volume-of-fire
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>Autonomous offensive frameworks don’t need novel exploits to get in; they can get results through persistence and volume. In this blog, we explain how they work, where they fall short, and which defenses slow them down.</p>
```

#### Full body

```
Blog Accuracy Through Volume of Fire November 19, 2026 Accuracy Through Volume of Fire Written by Justin Elze Artificial Intelligence (AI) Table of contents Stop Giving Automated Testing Unlimited Room Running the Framework Creates Its Own Attack Surface Internal Networks Change the Constraints Make the Volume Hit Walls ARTEX and similar LLM-driven pentesting frameworks can find weaknesses, follow leads, and turn ordinary exposure into useful attack paths. Incident reporting now shows attackers using them successfully. The practical questions are what these tools actually do, what you can learn by running them yourself, and where defenders can interrupt the work. When I say volume of fire, I mean the number and breadth of attempts a framework can make, including follow-up requests that change based on earlier results. An LLM makes that follow-up cheaper to sustain. It can also improve a hypothesis as evidence comes in. That does not make every conclusion correct, and attempts made against a live target create opportunities to detect or block the activity. Familiar Tools With LLM Follow-Up ARTEX is an LLM-driven pentesting and offensive command-and-control platform that coordinates agents and exposes a web console. The framework gives a model tools to inspect targets and act on the results. PentAGI, HexStrike AI, and Cairn appear in the same reporting, although their implementations differ. ARTEX is a useful example of the broader shift from running a scanner to automating the investigation that follows. Google Threat Intelligence Group and Mandiant's October 30 report documents these frameworks in intrusion investigations. Its ARTEX examples include rapid AWS permission probing and hundreds of logged events while pursuing command execution on a web server. That is evidence of operational use, rather than a claim that every model or default configuration will produce the same results. Successful and noisy can describe the same intrusion. The Scanner is Only the Beginning The common attacker workflow is straightforward, though details differ. Discover assets with tools such as subfinder, identify reachable web services with httpx, enumerate services with Nmap, run nuclei templates, and use ffuf or similar tooling to discover content and parameters. HexStrike's documented tool inventory includes all of them. Selection and order vary by framework. Very little of the network behavior is new. The useful change comes after the initial output. In an agent workflow, the LLM selects an action, the framework executes it, and the result becomes input for the next decision. It might inspect a response, adjust a request with curl or a browser, write a small script, or investigate an exposed file. A discovered secret becomes another hypothesis: Is it valid, and what can it access? The operator still has to decide which questions can be answered within scope and what evidence is sufficient. The model supplies reasoning and proposed actions. The framework supplies tools, execution, state, and permissions. The deployment supplies the actual access. Changing any of those can change the outcome, so a framework name alone tells you very little about how capable a particular run will be. Microsoft's November 6 ARTEX reporting describes familiar clients, including Nmap, curl, Python HTTP clients, and Playwright. It also shows Storm-3358 pairing ARTEX with conventional automated tools to scan Internet-exposed systems and exploit flaws such as anonymous file upload and SSRF. The framework can change its requests and approach in response to failure. Recognizing a default user agent helps, but it is a starting signal rather than a durable boundary. Calling this a scanner or wrapper undersells the automated follow-up. A model can turn an otherwise abandoned lead into a useful attack path. It still needs a reachable target, suitable tools, and any permissions required by the action. It can also spend an impressive number of tokens investigating a false po
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: Accuracy Through Volume of Fire
  - Published: 2026-11-19T05:00:00+00:00
  - Link: https://trustedsec.com/blog/accuracy-through-volume-of-fire
  - Summary: <p>Autonomous offensive frameworks don’t need novel exploits to get in; they can get results through persistence and volume. In this blog, we explain how they work, where they fall short, and which defenses slow them down.</p>

### Cluster 717ae538c3 — score 9

- Title: How AWS Security Incident Response triages your security findings
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-11-19T19:20:58+00:00
- Link: https://aws.amazon.com/blogs/security/how-aws-security-incident-response-triages-your-security-findings/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
AWS Security Incident Response continuously triages the threat findings from Amazon GuardDuty and AWS Security Hub CSPM, but most of that work never shows up as a case. If cases are all you look at, it’s hard to tell whether the service is working at all, and that’s the question I hear most often when […]
```

#### Full body

```
AWS Security Blog How AWS Security Incident Response triages your security findings AWS Security Incident Response continuously triages the threat findings from Amazon GuardDuty and AWS Security Hub CSPM , but most of that work never shows up as a case. If cases are all you look at, it’s hard to tell whether the service is working at all, and that’s the question I hear most often when I help customers onboard. The Proactive response dashboard gives you a high-level view of this activity, and this post takes you behind the numbers to show what happens to an individual finding. In this post, I walk you through what happens to a finding after it’s ingested by the service, what gets triaged, where each finding is sent, and how a triage decision becomes a case. I then show you how to confirm triage is working day-to-day, so your team can focus on the findings that require attention. The process flow is shown in Figure 1. Figure 1: AWS Security Incident Response triage flow, from ingestion through to one of three outcomes Ingestion AWS Security Incident Response ingests threat findings from GuardDuty through Amazon EventBridge rules that are automatically deployed to your accounts during the onboarding process . If you send third-party detection findings to Security Hub CSPM from tools such as CrowdStrike, Trend Micro, or Lacework, their threat detection findings are also ingested. Each of those findings must carry complete payload information such as resource ID, account ID, timestamp, and threat details. GuardDuty findings are ingested directly, so these findings aren’t re-ingested through Security Hub CSPM and there’s no duplication. Triage The service triages findings that indicate an active threat, such as compromised credentials, cryptomining, or data exfiltration. These represent activity that’s underway or has already occurred. Posture and compliance findings aren’t triaged. A misconfiguration or a failed benchmark check reflects the state of your environment rather than an active threat, so those findings remain for your team to address through your existing remediation process. Outcomes For each threat finding, the service runs an automated triage process. It evaluates the finding payload, related AWS activity from AWS CloudTrail and Amazon VPC Flow Logs , AWS threat intelligence, and the context you provide about your environment. The service then maps the finding against a profile of known-good activity. What fits the profile is treated as expected, and what doesn’t is flagged for a closer look. What happens next depends on that outcome. A finding is sent to one of three places: Archived, no action needed – Automated triage or an AWS Security Incident Response engineer confirms the activity is benign or expected. The finding is archived in GuardDuty, with no case and no customer contact. A proactive case is opened – Triage can’t confirm the activity is benign. This is either Unconfirmed Activity (the service needs you to confirm whether it’s expected) or Inappropriate/Unintended Activity (confirmed activity that needs your action). A proactive case is opened, your incident response team is engaged, and the finding stays Current until it’s resolved. Retained for your review, no case – Posture-related findings, such as overly permissive policies, configuration, or missing encryption, aren’t threats. By design, they stay Current without archiving and no case is created. When a proactive case is opened, you respond to it in the AWS Management Console for AWS Security Incident Response under Cases , where you can communicate directly with the team, share context, and resolve or reopen the case. Timely responses also help the service learn your environment, which helps reduce false positives over time. For the full workflow, see Responding to an AWS generated case . The preceding outcomes use GuardDuty terms, because it’s the primary source. Third-party findings ingested through Security Hub CSPM follow the same triage logic,
```

#### Corroborating sources (1)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: How AWS Security Incident Response triages your security findings
  - Published: 2026-11-19T19:20:58+00:00
  - Link: https://aws.amazon.com/blogs/security/how-aws-security-incident-response-triages-your-security-findings/
  - Summary: AWS Security Incident Response continuously triages the threat findings from Amazon GuardDuty and AWS Security Hub CSPM, but most of that work never shows up as a case. If cases are all you look at, it’s hard to tell whether the service is working at all, and that’s the question I hear most often when […]

### Cluster bd953decf0 — score 9

- Title: How Chain, Our AI Workspace, Helps Investigators Fight Crime
- Source: Chainalysis (ransomware_ecrime_financial_crime)
- Published: 2026-11-19T15:08:06+00:00
- Link: https://www.chainalysis.com/blog/how-chain-our-ai-workspace-helps-investigators-fight-crime/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The biggest hack in crypto history is also likely the most complex. Binance’s attackers are weaponizing automation in their race… The post How Chain, Our AI Workspace, Helps Investigators Fight Crime appeared first on Chainalysis .
```

#### Full body

```
Company News Chainalysis Supports HyperEVM with Automatic Token Support September 3, 2026
```

#### Corroborating sources (1)

- **Chainalysis** (ransomware_ecrime_financial_crime)
  - Title: How Chain, Our AI Workspace, Helps Investigators Fight Crime
  - Published: 2026-11-19T15:08:06+00:00
  - Link: https://www.chainalysis.com/blog/how-chain-our-ai-workspace-helps-investigators-fight-crime/
  - Summary: The biggest hack in crypto history is also likely the most complex. Binance’s attackers are weaponizing automation in their race… The post How Chain, Our AI Workspace, Helps Investigators Fight Crime appeared first on Chainalysis .

### Cluster ead43f4f6d — score 9

- Title: PHP Patches Seven Critical RCE Vulnerabilities
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-19T15:54:20+00:00
- Link: https://www.securityweek.com/php-patches-seven-critical-rce-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-109619, CVE-2026-115560, CVE-2026-129182, CVE-2026-129474, CVE-2026-129481
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-115560, CVE-2026-129481, CVE-2026-109619, CVE-2026-129182, CVE-2026-129474
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Successful exploitation could allow attackers to crash the worker process and execute code with the PHP worker’s privileges. The post PHP Patches Seven Critical RCE Vulnerabilities appeared first on SecurityWeek .
```

#### Full body

```
PHP on Thursday rolled out a fresh set of security patches as part of its four-week update schedule, including fixes for seven critical-severity remote code execution (RCE) vulnerabilities. First in line is CVE-2026-115560 , which was publicly disclosed last month, two days after PHP2Shell patches landed. Residing in the session upload progress feature, it could be triggered to write attacker data using one session serialization format and then read it using another. “A mismatched decoder can interpret part of a session key as serialized object data. An application with a suitable object gadget chain can then execute code with the privileges of the PHP worker,” PHP’s advisory reads. Next in line is CVE-2026-129481 , described as a use-after-free that occurs after a session shutdown has been interrupted, and which PHP describes as an incomplete fix for CVE-2026-109619, one of the two PHP2Shell flaws fixed in October and now widely exploited. “An attacker who can cause an application’s session cleanup to fail in this way may corrupt memory or crash a reused PHP worker. The use-after-free could potentially lead to remote code execution, but code execution through this specific field has not been demonstrated,” PHP notes, adding that PHP 8.2 is not affected. Another use-after-free, CVE-2026-129182 , covers additional exploitation scenarios for CVE-2026-109619, an RCE via stale global state. According to PHP, however, RCE via these scenarios has not been demonstrated. Advertisement. Scroll to continue reading. Impacting PHP 8.5 and later, CVE-2026-129474 is a use-after-free weakness that could allow an unauthenticated attacker to cause a fatal error and achieve RCE. “Exploitation depends on the application and requires control over enough request data to influence memory allocation, a reachable magic method call, and a fatal error at the relevant point,” PHP says. Attackers able to influence session contents and interrupt the write of serialized data to a session file may trigger the deserialization of attacker-controlled content when the session is next opened. Tracked as CVE-2026-126714 , the flaw could lead to RCE via a suitable object gadget chain in the application. PHP also patched CVE-2026-129289 , a PHP-FPM request smuggling issue caused by PHP reading a request-body stream lazily, treating a request body as handled during request shutdown and skipping the normal cleanup that discards unread input. “PHP can fail to discard unread bytes from an HTTP request body before reusing a persistent PHP-FPM or LSAPI connection. In PHP-FPM, an unauthenticated attacker can make those bytes form a separate FastCGI request, bypass front-end routing and execute attacker-controlled PHP code with the privileges of the worker,” PHP explains. The seventh critical-severity vulnerability patched today, CVE-2026-129496 , resides in the timezone cache. PHP can retain a reference to it when writing a diagnostic to a PHP error log file during process startup, and a later diagnostic can access the freed cache before it is reset. “On affected configurations, a remote attacker can trigger memory corruption, cause a worker to crash, and potentially execute arbitrary code with the privileges of the PHP worker,” PHP explains. PHP 8.6.0 and PHP 8.5.13 were rolled out with fixes for all critical bugs and for 10 high and medium-severity flaws. Patches for most issues were also included in PHP 8.4.28, PHP 8.3.37, and PHP 8.2.36. More information is available on PHP’s news archive page. Related: PHP Readies Critical Security Updates to Patch Another RCE Flaw Related: Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release Related: Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks Related: Splunk Patches Nearly 140 Flaws Across Three Core Products Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecur
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: PHP Patches Seven Critical RCE Vulnerabilities
  - Published: 2026-11-19T15:54:20+00:00
  - Link: https://www.securityweek.com/php-patches-seven-critical-rce-vulnerabilities/
  - Summary: Successful exploitation could allow attackers to crash the worker process and execute code with the PHP worker’s privileges. The post PHP Patches Seven Critical RCE Vulnerabilities appeared first on SecurityWeek .

### Cluster 93f35981b4 — score 9

- Title: Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-19T13:12:20+00:00
- Link: https://www.securityweek.com/hackers-exploit-cisco-expressway-vulnerability-soon-after-poc-release/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- actor_attribution: Scattered Spider
- affected_industries: manufacturing_industrial
- affected_products: GitHub, GitLab
- cve_ids: CVE-2026-76466
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- actor_attribution: Scattered Spider
- affected_industries: manufacturing_industrial
- affected_products: GitHub, GitLab
- cve_ids: CVE-2026-76466
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Attackers hacked clustered Cisco Expressway devices at a Russian organization and prepared tooling for lateral movement. The post Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release appeared first on SecurityWeek .
```

#### Full body

```
Hackers exploited a critical Cisco Expressway vulnerability to breach a Russian organization soon after proof-of-concept (PoC) exploit code was released publicly, according to cybersecurity firm F6. Expressway gateways allow remote employees, partners, and third-party users to securely connect to an organization’s collaboration services, including video calls, voice calls, and instant messaging. Tracked as CVE-2026-76466 (CVSS score of 9.8), the flaw can be exploited without authentication by remote attackers with network access to a device, allowing them to execute commands as root. It affects virtual and appliance versions of Expressway Core and Expressway Edge, but only when the devices are clustered. Cisco, which disclosed the issue on October 21, said it resides in the Expressway database service feature and stems from persistent cookies. An attacker possessing the persistent cookies could reach the database service and issue certain remote procedure call (RPC) commands, gaining the ability to run root-level commands on the underlying operating system. Expressway X15.5.20 resolves the vulnerability. There are no workarounds, and customers on X14 or earlier releases need to move to a fixed release, Cisco says. Advertisement. Scroll to continue reading. The advisory has not been revised since its initial release and still states that Cisco is unaware of public announcements or malicious use of the flaw. However, a PoC exploit has since been posted on GitHub, and F6 says the attack it investigated came shortly after. According to F6, the attackers first breached two Expressway X15.5.3 devices exposed to the internet. They then pivoted from one of them to two other cluster nodes sitting on the organization’s internal network. After securing root privileges, the attackers prepared tools for lateral movement. These included custom Python scripts designed to scan the network, locate SMB resources, interact with SQL Server and WinRM, and search GitLab repositories, aiming to exfiltrate credentials and other sensitive information. F6 determined that the attackers modified the scripts on the fly, during the attack. “The source code contained characteristic comments and descriptions of fixes indicating the use of an AI assistant,” the company says. F6 did not name the victim or attribute the attack to a known threat actor. To detect exploitation, F6 points to the Erlang system log on Expressway devices. The security firm has also published IP addresses and file paths associated with the attack in a Russian-language press release. Although Cisco lists no workarounds, F6 recommends that organizations unable to patch immediately block connections to TCP ports 4371–4372 at the firewall, except from the IP addresses of trusted cluster nodes. SecurityWeek has reached out to Cisco for comment on F6’s findings and will update this article if the company responds. Related : Java4Shell Exploitation Attempts Begin as Vendors Rush Out Advisories Related : F5 Patches Critical NGINX2Root Flaws as PoC Exploits Go Public Related : PHP Readies Critical Security Updates to Patch Another RCE Flaw Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs Java4Shell Exploitation Attempts Begin as Vendors Rush Out Advisories Last of Five Defendants Sentenced in US Scattered Spider Hacking Case Microsoft Takes Perception Agentic Security Platform Out of Preview Microsoft Agent Framework Releases Poisoned With Credential Stealer Java4Shell Vulnerability Puts Enterprise Applications at Risk of Takeover Market Research Giant Ipsos Investig
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release
  - Published: 2026-11-19T13:12:20+00:00
  - Link: https://www.securityweek.com/hackers-exploit-cisco-expressway-vulnerability-soon-after-poc-release/
  - Summary: Attackers hacked clustered Cisco Expressway devices at a Russian organization and prepared tooling for lateral movement. The post Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release appeared first on SecurityWeek .

### Cluster ab440398cd — score 9

- Title: What’s new with Google Cloud
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-11-19T17:00:00+00:00
- Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, healthcare
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: healthcare, financial_services
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Nov 16 - Nov 20 Why your AI agent keeps forgetting: a 15 minute build on agent memory Agents that resend the full conversation get slower and more expensive, and agents that keep nothing forget users between sessions. In the latest AI Agent Clinic episode, Google Cloud engineer Laxmi Harikumar and developer Miles Libbey add long term memory to a voice agent built with Agent Development Kit (ADK). They compare 4 memory options (flat prompting, RAG, knowledge graphs and Memory Bank in Gemini platform) and show 3 ways to keep context small. Watch the episode and get the code. Cut background agent costs in half with th
```

#### Full body

```
Inside Google Cloud What’s new with Google Cloud November 19, 2026 Google Cloud Content & Editorial Try Gemini today The front door to AI in the workplace Try now Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . Nov 16 - Nov 20 Why your AI agent keeps forgetting: a 15 minute build on agent memory Agents that resend the full conversation get slower and more expensive, and agents that keep nothing forget users between sessions. In the latest AI Agent Clinic episode, Google Cloud engineer Laxmi Harikumar and developer Miles Libbey add long term memory to a voice agent built with Agent Development Kit (ADK). They compare 4 memory options (flat prompting, RAG, knowledge graphs and Memory Bank in Gemini platform) and show 3 ways to keep context small. Watch the episode and get the code. Cut background agent costs in half with the deferred tier on Gemini platform The deferred service tier is generally available (GA) on the Gemini platform for the Interactions API , Agent Development Kit (ADK) , and Deep Research . Running multi-hour background loops through synchronous real-time inference introduces unnecessary cost and triggers 429 resource exhaustion errors at peak. Static batch inference offers a 50% discount only when all prompts sit in a fixed input file upfront, which breaks dynamic tool loops. On the Gemini platform, the new deferred service tier brings batch economics to dynamic, stateful, multi-turn agents. Instead of competing with live chat traffic, the scheduler routes latency-tolerant agent turns to spare global capacity at half the cost. Set service_tier="deferred" in ADK RunConfig or client.interactions.create() across gemini-4-argon, gemini-4-carbon, gemini-3.x models, and gemini-deep-research-1.0. Read the guides for the Interactions API , ADK , and Deep Research . 50% discount and cache savings: Completed turns receive 50% off Standard PayGo rates and stack with prompt caching. Cancelled, expired, or failed turns incur no charges. Managed queuing and state: During peak traffic, the platform queues and retries turns server-side with zero 429 errors. Pass previous_interaction_id to chain turns and retain warm prompt caches. Nov 9 - Nov 13 More frontier model choice on Google Cloud: Anthropic’s Claude Fable 5.2 and Meta’s Muse model series. Developers now have even more flexibility to build, deploy, and scale with the right model for every workload on Google Cloud. Anthropic’s Claude Fable 5.2 is now generally available in the Model Garden, bringing frontier intelligence to complex coding, scientific research, and multi-agent orchestration. Plus, Meta’s newest models— Muse Spark 1.3 , Muse Wonder , and the efficient Muse Ember —are now available in public preview, giving teams seamless access to both proprietary and open-weight capabilities with enterprise-grade security. Explore the models in the model garden today. Next-Generation SecOps: SentinelOne and Google Cloud Google Cloud and SentinelOne joined forces to solve the threat scaling challenge with a fundamentally re-architected integration. As a Google Unified Security (GUS) Recommended endpoint detection and response (EDR) partner, SentinelOne pairs Google Security Operations through an optimized direct integration and streamlined data schemas, delivering essential endpoint telemetry visibility to SecOps detection and agentic SOC pipelines while significantly reducing the total cost of ownership of the integration. Read more Layered LLM guardrails on Apigee: Static rules, Model Armor, and NeMo Guardrails No single LLM guardrail catches every threat. A new technical guide and demo showcase how to use Apigee as an AI gateway to stack three complementary layers—determin
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: What’s new with Google Cloud
  - Published: 2026-11-19T17:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - Summary: Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Nov 16 - Nov 20 Why your AI agent keeps forgetting: a 15 minute build on agent memory Agents that resend the full conversation get slower and more expensive, and agents that keep nothing forget users between sessions. In the latest AI Agent Clinic episode, Google Cloud engineer Laxmi Harikumar and developer Miles Libbey add long term memory to a voice agent built with Agent Development Kit (ADK). They compare 4 memory options (flat prompting, RAG, knowledge graphs and Memory Bank in Gemini platform) and show 3 ways to keep context small. Watch the episode and get the code. Cut background agent costs in half with th

### Cluster cf875bad92 — score 9

- Title: Introducing in-place migration to GKE Dataplane V2
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-11-19T17:00:00+00:00
- Link: https://cloud.google.com/blog/products/networking/gke-dataplane-v2-in-place-migration/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Kubernetes

#### Cluster taxonomy (union across members)
- affected_products: Google Cloud, Kubernetes, Linux kernel
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Kubernetes, Google Cloud, Linux kernel
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
GKE Dataplane V2 is Google Cloud’s next-generation networking dataplane for Google Kubernetes Engine (GKE), built on extended Berkeley Packet Filter ( eBPF ) and open-source Cilium to replace traditional iptables routing and kube-proxy . We built GKE Dataplane V2 to meet the performance, scalability, and security demands of modern cloud-native workloads. GKE customers consistently tell us that while they want to adopt GKE Dataplane V2 for its performance and scale, migrating production clusters carrying stateful workloads and established IP allocations has been challenging, often requiring a disruptive parallel cluster setup. Today, we are pleased to introduce the preview of in-place migration , allowing you to transition eligible VPC-native clusters from GKE Dataplane V1 to GKE Dataplane V2 directly. Let’s take a look at what GKE Dataplane V2 brings to the table and how to start migrating your environment to it. Why GKE Dataplane V2? GKE Dataplane V2 is built on the extended Berkeley
```

#### Full body

```
Networking Introducing in-place migration to GKE Dataplane V2 November 19, 2026 Shrikant Kelkar Product Manager Mark St. John Software Engineer Try Gemini today The front door to AI in the workplace Try now GKE Dataplane V2 is Google Cloud’s next-generation networking dataplane for Google Kubernetes Engine (GKE), built on extended Berkeley Packet Filter ( eBPF ) and open-source Cilium to replace traditional iptables routing and kube-proxy . We built GKE Dataplane V2 to meet the performance, scalability, and security demands of modern cloud-native workloads. GKE customers consistently tell us that while they want to adopt GKE Dataplane V2 for its performance and scale, migrating production clusters carrying stateful workloads and established IP allocations has been challenging, often requiring a disruptive parallel cluster setup. Today, we are pleased to introduce the preview of in-place migration , allowing you to transition eligible VPC-native clusters from GKE Dataplane V1 to GKE Dataplane V2 directly. Let’s take a look at what GKE Dataplane V2 brings to the table and how to start migrating your environment to it. Why GKE Dataplane V2? GKE Dataplane V2 is built on the extended Berkeley Packet Filter (eBPF) and open-source Cilium, with features specifically tuned for performance, scalability, and deep integration with Google Cloud networking. Consider the following capabilities: Scale and performance: By handling packet processing with eBPF maps in the Linux kernel instead of linear iptables rules, GKE Dataplane V2 supports clusters of up to 15,000 nodes with network policy enforcement (and up to 65,000 nodes when network policy enforcement is disabled, which requires recreating clusters). This architecture also handles the high Pod churn, fast sandbox provisioning, and network identity scaling required by large agentic AI workloads . High-throughput accelerator networking: Serves as the foundational networking layer for GPU and Cloud TPU clusters on GKE, helping keep accelerators computing rather than waiting on network initialization. It also powers capabilities like GKE managed DRANET for Dynamic Resource Allocation (DRA) of network devices. Network security and observability: With GKE Dataplane V2, standard Kubernetes NetworkPolicy enforcement and hierarchical ClusterNetworkPolicy work directly in the kernel with optimized performance. GKE Dataplane V2 also provides the underlying dataplane for sidecarless GKE ambient networking , while GKE Dataplane V2 observability delivers native network policy logging , live traffic topology, and Hubble flow metrics. The in-place migration workflow Instead of having to manually move workloads to a new cluster, GKE now automates the transition across three stages, as described in the GKE Dataplane V2 migration guide : 1. Eligibility and preflight checks: Before starting, verify that your Pod IP ranges have enough capacity to recreate the nodes by using GKE IP address utilization insights , and check Active Assist for incompatible configurations like custom eBPF programs on managed interfaces. 2. Initiate the migration: Once you’ve verified the preflight checks, start the migration with a single Google Cloud CLI update command. To initiate the migration on an eligible cluster, run: Loading... gcloud container clusters update CLUSTER_NAME \ --location=LOCATION \ --enable-dataplane-v2 3. Automated rollout and finalization: GKE updates your node pools to GKE Dataplane V2 while respecting your configured maintenance windows, exclusions, and upgrade strategies. To move faster, you can also patch specific node pools manually, or roll back to GKE Dataplane V1 at any time prior to finalization. In-place migration supports VPC-native clusters running GKE 1.35 or later (see the migration guide for exact version requirements). It does not support routes-based clusters or clusters running Calico. Get started In-place migration to GKE Dataplane V2 is available now in preview. During this time, we re
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Introducing in-place migration to GKE Dataplane V2
  - Published: 2026-11-19T17:00:00+00:00
  - Link: https://cloud.google.com/blog/products/networking/gke-dataplane-v2-in-place-migration/
  - Summary: GKE Dataplane V2 is Google Cloud’s next-generation networking dataplane for Google Kubernetes Engine (GKE), built on extended Berkeley Packet Filter ( eBPF ) and open-source Cilium to replace traditional iptables routing and kube-proxy . We built GKE Dataplane V2 to meet the performance, scalability, and security demands of modern cloud-native workloads. GKE customers consistently tell us that while they want to adopt GKE Dataplane V2 for its performance and scale, migrating production clusters carrying stateful workloads and established IP allocations has been challenging, often requiring a disruptive parallel cluster setup. Today, we are pleased to introduce the preview of in-place migration , allowing you to transition eligible VPC-native clusters from GKE Dataplane V1 to GKE Dataplane V2 directly. Let’s take a look at what GKE Dataplane V2 brings to the table and how to start migrating your environment to it. Why GKE Dataplane V2? GKE Dataplane V2 is built on the extended Berkeley

### Cluster 06bffa03c1 — score 9

- Title: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-13T16:53:08+00:00
- Link: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-6460

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-6460
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-6460
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server. The flaw, tracked as CVE-2026-6460, has a CVSS score of 8.8. Any code run this way has the rights of the operating
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE
  - Published: 2026-11-13T16:53:08+00:00
  - Link: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
  - Summary: A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server. The flaw, tracked as CVE-2026-6460, has a CVSS score of 8.8. Any code run this way has the rights of the operating

### Cluster d4e16d24ed — score 9

- Title: PHP Releases Patches to Fix 18 Vulnerabilities
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-11-19T15:28:00+00:00
- Link: https://www.infosecurity-magazine.com/news/php-releases-patches-fix-18/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
PHP has released security updates addressing 18 vulnerabilities, including critical remote code execution flaws affecting session handling
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: PHP Releases Patches to Fix 18 Vulnerabilities
  - Published: 2026-11-19T15:28:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/php-releases-patches-fix-18/
  - Summary: PHP has released security updates addressing 18 vulnerabilities, including critical remote code execution flaws affecting session handling

### Cluster 7806aed11f — score 9

- Title: Risky Bulletin: Cyberattack grounds German UAVs
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-11-16T00:04:19+00:00
- Link: https://risky.biz/RBNEWS634/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Germany grounds UAVs after a supply chain attack, a threat actor accessed Barracuda’s cloud for two days, the US AI task force asks for regulatory leniency and the FBI disrupts a North Korean face-swapping operation.
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Cyberattack grounds German UAVs
  - Published: 2026-11-16T00:04:19+00:00
  - Link: https://risky.biz/RBNEWS634/
  - Summary: Germany grounds UAVs after a supply chain attack, a threat actor accessed Barracuda’s cloud for two days, the US AI task force asks for regulatory leniency and the FBI disrupts a North Korean face-swapping operation.

### Cluster c4123302e0 — score 9

- Title: Risky Bulletin: Chinese APT exploits SS7, Diameter to spy on targets
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-11-13T03:03:12+00:00
- Link: https://risky.biz/RBNEWS633/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
A Chinese APT exploits the SS7 and Diameter protocols, a remote code execution bug hits Apache, Brazil’s largest port suffers a cyberattack, and Europol takes down three malware operations.
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Chinese APT exploits SS7, Diameter to spy on targets
  - Published: 2026-11-13T03:03:12+00:00
  - Link: https://risky.biz/RBNEWS633/
  - Summary: A Chinese APT exploits the SS7 and Diameter protocols, a remote code execution bug hits Apache, Brazil’s largest port suffers a cyberattack, and Europol takes down three malware operations.

### Cluster 939768379a — score 8

- Title: Threat Hunting On The Network: An Active Search for Risks on the Wire
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-11-18T21:57:58+00:00
- Link: https://www.blackhillsinfosec.com/threat-hunting-network/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
All threat hunters are looking for evidence of nefarious activity, hopefully before an incident happens. Threat hunting on the network involves actively searching through packet data for malicious activity. Threat hunting on an endpoint depends more heavily on logs. Think of it as on the wire (or in the air) versus on a host itself. Don’t worry, you don’t have to look through every packet in a pcap file. That would make your head explode!
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: Threat Hunting On The Network: An Active Search for Risks on the Wire
  - Published: 2026-11-18T21:57:58+00:00
  - Link: https://www.blackhillsinfosec.com/threat-hunting-network/
  - Summary: All threat hunters are looking for evidence of nefarious activity, hopefully before an incident happens. Threat hunting on the network involves actively searching through packet data for malicious activity. Threat hunting on an endpoint depends more heavily on logs. Think of it as on the wire (or in the air) versus on a host itself. Don’t worry, you don’t have to look through every packet in a pcap file. That would make your head explode!

### Cluster 5630cc40c4 — score 8

- Title: Patches released for critical ‘NGINX2Root’ vulnerabilities
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-11-18T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/patches-released-for-critical-nginx2root-vulnerabilities
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Categories: Threat Research Tags: advisory, vulnerability, NGINX
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Patches released for critical ‘NGINX2Root’ vulnerabilities
  - Published: 2026-11-18T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/patches-released-for-critical-nginx2root-vulnerabilities
  - Summary: Categories: Threat Research Tags: advisory, vulnerability, NGINX

### Cluster 4043ac4b49 — score 8

- Title: Hijacked Optimizely snippets served malicious code on major websites
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-11-17T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/hijacked-optimizely-snippets-served-malicious-code
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>Organizations using Optimizely Web Experimentation should check their projects for code injected on November 16</p> Categories: Threat Research Tags: advisory, Optimizely
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Hijacked Optimizely snippets served malicious code on major websites
  - Published: 2026-11-17T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/hijacked-optimizely-snippets-served-malicious-code
  - Summary: <p>Organizations using Optimizely Web Experimentation should check their projects for code injected on November 16</p> Categories: Threat Research Tags: advisory, Optimizely

### Cluster bfd8c8319c — score 8

- Title: GeoVision Camera Software Abused to Deploy XMRig Cryptominer
- Source: Huntress (detection_response_operations)
- Published: 2026-11-13T14:00:00+00:00
- Link: https://www.huntress.com/blog/geovision-camera-software-xmrig-cryptominer
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Attackers abused publicly exposed GeoVision camera software at 13 organizations, tried to disable Defender, and deployed XMRig. Get the IoCs and next steps.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: GeoVision Camera Software Abused to Deploy XMRig Cryptominer
  - Published: 2026-11-13T14:00:00+00:00
  - Link: https://www.huntress.com/blog/geovision-camera-software-xmrig-cryptominer
  - Summary: Attackers abused publicly exposed GeoVision camera software at 13 organizations, tried to disable Defender, and deployed XMRig. Get the IoCs and next steps.

### Cluster 4c69eaf1ae — score 8

- Title: Internet traffic and attacks during the 2026 U.S. midterm elections
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-11-19T14:00:00+00:00
- Link: https://blog.cloudflare.com/internet-traffic-2026-us-election/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
On November 3, 2026 U.S. voters headed to the polls. Here’s what Cloudflare data across more than 1,400 protected sites tells us about Election Day Internet traffic and cyberattacks.
```

#### Corroborating sources (1)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: Internet traffic and attacks during the 2026 U.S. midterm elections
  - Published: 2026-11-19T14:00:00+00:00
  - Link: https://blog.cloudflare.com/internet-traffic-2026-us-election/
  - Summary: On November 3, 2026 U.S. voters headed to the polls. Here’s what Cloudflare data across more than 1,400 protected sites tells us about Election Day Internet traffic and cyberattacks.

### Cluster 8abd30c818 — score 8

- Title: European Commission confirms cyberattack, says hackers used AI tool
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-11-19T15:15:00+00:00
- Link: https://therecord.media/european-commission-confirms-cyberattack-using-ai
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
POLITICO had reported CERT-EU had identified the attackers’ use of ARTEX, an open-source AI hacking platform that the FBI last week warned was being used both by criminals and state-sponsored groups.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: European Commission confirms cyberattack, says hackers used AI tool
  - Published: 2026-11-19T15:15:00+00:00
  - Link: https://therecord.media/european-commission-confirms-cyberattack-using-ai
  - Summary: POLITICO had reported CERT-EU had identified the attackers’ use of ARTEX, an open-source AI hacking platform that the FBI last week warned was being used both by criminals and state-sponsored groups.

### Cluster 43abe38f10 — score 8

- Title: Data breach impacts 40 Irish credit unions in reported IT provider hack
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-18T19:39:33+00:00
- Link: https://www.bleepingcomputer.com/news/security/data-breach-impacts-40-irish-credit-unions-in-reported-it-provider-hack/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A reported cyberattack on Wellington IT has exposed sensitive information belonging to members of 50 credit unions, the majority of which are located in Ireland. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Data breach impacts 40 Irish credit unions in reported IT provider hack
  - Published: 2026-11-18T19:39:33+00:00
  - Link: https://www.bleepingcomputer.com/news/security/data-breach-impacts-40-irish-credit-unions-in-reported-it-provider-hack/
  - Summary: A reported cyberattack on Wellington IT has exposed sensitive information belonging to members of 50 credit unions, the majority of which are located in Ireland. [...]

### Cluster ef3091db9b — score 8

- Title: StepSecurity Secures $20 Million to Expand Supply Chain Protection
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-19T12:23:34+00:00
- Link: https://www.securityweek.com/stepsecurity-secures-20-million-to-expand-supply-chain-protection/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The company will use the funds to accelerate the development and distribution of its security platform. The post StepSecurity Secures $20 Million to Expand Supply Chain Protection appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: StepSecurity Secures $20 Million to Expand Supply Chain Protection
  - Published: 2026-11-19T12:23:34+00:00
  - Link: https://www.securityweek.com/stepsecurity-secures-20-million-to-expand-supply-chain-protection/
  - Summary: The company will use the funds to accelerate the development and distribution of its security platform. The post StepSecurity Secures $20 Million to Expand Supply Chain Protection appeared first on SecurityWeek .

### Cluster 59177f6aa4 — score 8

- Title: PostgreSQL 19 Released
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-11-19T20:43:57+00:00
- Link: https://simonwillison.net/2026/Nov/19/postgresql-19/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
PostgreSQL 19 Released Most years PostgreSQL ships a new release in September, but this year's release came two months later thanks mainly to the flurry of issues that the PostgreSQL team needed to address as part of the ongoing AI-reported vulnerability apocalypse. This release was definitely worth the wait. My favorite new feature is this one: For applications that send reads to standbys, PostgreSQL 19 adds "read-your-writes" consistency with the new WAIT FOR LSN command. A session on a standby can use WAIT FOR LSN to wait until the standby has replayed the write-ahead log (WAL) up to a specific log sequence number (LSN) before running a query, so the application can read data it just wrote on the primary. In practice, that looks like this: UPDATE movie SET genre = 'Dramatic' WHERE genre = 'Drama'; SELECT pg_current_wal_insert_lsn(); That returns a value like 0/0306EE20 . Store that somewhere (a signed cookie would work) such that on a subsequent request your application can do: WAIT
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: PostgreSQL 19 Released
  - Published: 2026-11-19T20:43:57+00:00
  - Link: https://simonwillison.net/2026/Nov/19/postgresql-19/
  - Summary: PostgreSQL 19 Released Most years PostgreSQL ships a new release in September, but this year's release came two months later thanks mainly to the flurry of issues that the PostgreSQL team needed to address as part of the ongoing AI-reported vulnerability apocalypse. This release was definitely worth the wait. My favorite new feature is this one: For applications that send reads to standbys, PostgreSQL 19 adds "read-your-writes" consistency with the new WAIT FOR LSN command. A session on a standby can use WAIT FOR LSN to wait until the standby has replayed the write-ahead log (WAL) up to a specific log sequence number (LSN) before running a query, so the application can read data it just wrote on the primary. In practice, that looks like this: UPDATE movie SET genre = 'Dramatic' WHERE genre = 'Drama'; SELECT pg_current_wal_insert_lsn(); That returns a value like 0/0306EE20 . Store that somewhere (a signed cookie would work) such that on a subsequent request your application can do: WAIT

### Cluster 3ecbd923ae — score 8

- Title: Credential stealer slipped into Microsoft’s official Python agent framework
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-11-19T12:53:44+00:00
- Link: https://www.helpnetsecurity.com/2026/11/19/microsoft-agent-framework-package-pypi-compromised/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Two releases of Microsoft’s official agent-framework package on the Python Package Index (PyPI) carried code that steals cloud and CI/CD credentials from developers’ systems. Agent Framework is Microsoft’s open-source toolkit for building AI agents and running them in workflows. Three supply chain security companies, StepSecurity, OX Security and Socket, caught the malicious versions and shared their analysis. “On November 17, 2026, versions 1.26.1 and 1.26.2 of the official Microsoft agent-framework package on PyPI were published … More → The post Credential stealer slipped into Microsoft’s official Python agent framework appeared first on Help Net Security .
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Credential stealer slipped into Microsoft’s official Python agent framework
  - Published: 2026-11-19T12:53:44+00:00
  - Link: https://www.helpnetsecurity.com/2026/11/19/microsoft-agent-framework-package-pypi-compromised/
  - Summary: Two releases of Microsoft’s official agent-framework package on the Python Package Index (PyPI) carried code that steals cloud and CI/CD credentials from developers’ systems. Agent Framework is Microsoft’s open-source toolkit for building AI agents and running them in workflows. Three supply chain security companies, StepSecurity, OX Security and Socket, caught the malicious versions and shared their analysis. “On November 17, 2026, versions 1.26.1 and 1.26.2 of the official Microsoft agent-framework package on PyPI were published … More → The post Credential stealer slipped into Microsoft’s official Python agent framework appeared first on Help Net Security .

### Cluster acebd671e8 — score 8

- Title: Ransomware Attacks Increase Behind AI, but Payments Decline
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-11-16T19:56:05+00:00
- Link: https://www.darkreading.com/threat-intelligence/ransomware-attacks-increase-ai-payments-decline
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Large language models and other AI systems allow a growing number of ransomware groups to create convincing phishing emails and identify sensitive data quickly.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Ransomware Attacks Increase Behind AI, but Payments Decline
  - Published: 2026-11-16T19:56:05+00:00
  - Link: https://www.darkreading.com/threat-intelligence/ransomware-attacks-increase-ai-payments-decline
  - Summary: Large language models and other AI systems allow a growing number of ransomware groups to create convincing phishing emails and identify sensitive data quickly.

### Cluster 0e89231e39 — score 8

- Title: phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-19T16:59:56+00:00
- Link: https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-126714

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-126714
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-126714
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
PHP's default file-based session storage can be made to return objects an attacker chose, by cutting off a session write at the right moment. When combined with a second weakness, such as a suitable gadget chain in the app, those objects can allow the attacker to run code on the server. Today's PHP releases fix the flaw, called phpAfterShell. The flaw is tracked as CVE-2026-126714 and rated
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution
  - Published: 2026-11-19T16:59:56+00:00
  - Link: https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html
  - Summary: PHP's default file-based session storage can be made to return objects an attacker chose, by cutting off a session write at the right moment. When combined with a second weakness, such as a suitable gadget chain in the app, those objects can allow the attacker to run code on the server. Today's PHP releases fix the flaw, called phpAfterShell. The flaw is tracked as CVE-2026-126714 and rated

### Cluster 93c948071f — score 8

- Title: Ruby Releases Fixes for 7 Regex and String Flaws, Warns 5 Have Proof-of-Concept RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-19T08:42:11+00:00
- Link: https://thehackernews.com/2026/11/ruby-releases-fixes-for-7-regex-and.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Ruby contains seven memory-safety flaws in its regular expression engine and its string case-conversion code. For five of them, its maintainers say, proof-of-concept exploits, or PoCs, have shown that crafted input can run code on the machine. "We are aware of PoCs that prove some of them can be used to trigger remote code execution," the maintainers said. The project released fixed versions
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Ruby Releases Fixes for 7 Regex and String Flaws, Warns 5 Have Proof-of-Concept RCE
  - Published: 2026-11-19T08:42:11+00:00
  - Link: https://thehackernews.com/2026/11/ruby-releases-fixes-for-7-regex-and.html
  - Summary: Ruby contains seven memory-safety flaws in its regular expression engine and its string case-conversion code. For five of them, its maintainers say, proof-of-concept exploits, or PoCs, have shown that crafted input can run code on the machine. "We are aware of PoCs that prove some of them can be used to trigger remote code execution," the maintainers said. The project released fixed versions

### Cluster 204ad62b40 — score 8

- Title: Researcher Demonstrates Database RCE Exploits Affecting PostgreSQL, MySQL and Oracle
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-19T08:14:00+00:00
- Link: https://thehackernews.com/2026/11/researcher-demonstrates-database-rce.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Low-privilege database accounts that cannot read a single application table can still be used to run code on the database server itself, a researcher has shown, by reaching memory-corruption bugs in the engine code behind ordinary SQL. The exploits, published yesterday, are the researcher's proofs of concept against PostgreSQL, MySQL and ClickHouse, plus a separate Oracle chain that needs no
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researcher Demonstrates Database RCE Exploits Affecting PostgreSQL, MySQL and Oracle
  - Published: 2026-11-19T08:14:00+00:00
  - Link: https://thehackernews.com/2026/11/researcher-demonstrates-database-rce.html
  - Summary: Low-privilege database accounts that cannot read a single application table can still be used to run code on the database server itself, a researcher has shown, by reaching memory-corruption bugs in the engine code behind ordinary SQL. The exploits, published yesterday, are the researcher's proofs of concept against PostgreSQL, MySQL and ClickHouse, plus a separate Oracle chain that needs no

### Cluster 3ade03443a — score 8

- Title: AI Cuts Vulnerability Discovery from Nine Months to 90 Hours
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-11-16T09:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/ai-cut-vulnerability-discover-nine/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Forescout report claims to have found 66 new flaws in just 90 hours using AI
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: AI Cuts Vulnerability Discovery from Nine Months to 90 Hours
  - Published: 2026-11-16T09:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/ai-cut-vulnerability-discover-nine/
  - Summary: Forescout report claims to have found 66 new flaws in just 90 hours using AI

### Cluster 22d75f84e0 — score 8

- Title: Inside the loop: Five AI attack frameworks that never ask permission
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-11-13T16:00:00+00:00
- Link: https://www.elastic.co/security-labs/threat-command/agentic-offensive-frameworks-detection-artex
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Five agentic offensive frameworks act in bursts of two to 25 seconds, and none enforces authorization in code. What ARTEX, CyberStrikeAI, Cairn, PentAGI, and HexStrike leave in your telemetry, and the ES|QL hunt that catches them.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Inside the loop: Five AI attack frameworks that never ask permission
  - Published: 2026-11-13T16:00:00+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/agentic-offensive-frameworks-detection-artex
  - Summary: Five agentic offensive frameworks act in bursts of two to 25 seconds, and none enforces authorization in code. What ARTEX, CyberStrikeAI, Cairn, PentAGI, and HexStrike leave in your telemetry, and the ES|QL hunt that catches them.
