# PHANTOMSignal Briefing Packet

- Generated: 2026-08-05T19:44:17.628994+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 74
- Total items in window: 355
- Total clusters raw: 138
- Total clusters in packet: 67
- Dropped low score: 71
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
  - In window count: 5
- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 7
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 4
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 3
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 1
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 0
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 0
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Active Countermeasures** (detection_response_operations)
  - URL: https://www.activecountermeasures.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 7
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 2
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 9
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 6
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 5
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 19
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 29
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 24
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
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
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Reddit r/netsecstudents** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsecstudents/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/msp** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/msp/.rss
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
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 25
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 16
- **tl;dr sec** (practitioner_analysis)
  - URL: https://tldrsec.com/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Embrace the Red** (ai_security_agentic_risk)
  - URL: https://embracethered.com/blog/index.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Risky Business News** (practitioner_analysis)
  - URL: https://risky.biz/feeds/risky-business-news/
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 0

## Affinity groups (themes)

### Palo Alto Networks exploitation (4 CVEs)
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 7
- Article count: 5
- Cohesion: 0.249
- Shared strong signals: Palo Alto Networks
- Member CVEs: CVE-2026-18556, CVE-2026-18577, CVE-2026-34486, CVE-2026-9198
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - affected_industries: government
  - affected_products: Palo Alto Networks
  - cve_ids: CVE-2026-18556, CVE-2026-18577, CVE-2026-34486, CVE-2026-9198
  - urgency_signals: preauth_unauth
- Cluster IDs: 65ab16fa91, e9b42737b7, 213b4e62b3, 1af5ed51b6, ebb24cd9dd, d1c29125d3, f0542a4609
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-18577-n-able-n-central-authentication-bypass-exploited-in-the-wild
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-18556-cve-2026-18577/
  - https://thehackernews.com/2026/08/cisa-adds-exploited-n-able-n-central.html
  - https://www.sophos.com/en-us/blog/nable-ncentral-exploitation-results-in-rmm-tool-deployment
  - https://www.darkreading.com/vulnerabilities-threats/attackers-exploit-n-able-patch-bypass-flaw
  - https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html
  - https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-langflow-n-central-apache-tomcat-flaws/
  - https://www.securityweek.com/cisa-warns-of-exploited-langflow-n-central-and-tomcat-vulnerabilities/
  - https://unit42.paloaltonetworks.com/malware-bypass-dns-direct-to-ip/
  - https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/
  - https://orca.security/resources/blog/10-best-tenable-alternatives/

### supply chain targeting npm
- Anchor signal: npm
- Theme key: npm
- Cluster count: 3
- Article count: 27
- Cohesion: 0.2
- Shared strong signals: npm
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, ransomware_extortion
  - actor_attribution: TeamPCP
  - affected_industries: financial_services
  - affected_products: npm
- Cluster IDs: 4c8ed8c5fa, 61004037ea, 1b822e43c0
- Links:
  - https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
  - https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
  - https://www.bleepingcomputer.com/news/security/hotel-wi-fi-attacks-use-custom-malware-to-breach-microsoft-365-accounts/
  - https://www.infosecurity-magazine.com/news/captivecrunch-midnight-blizzard/
  - https://orca.security/resources/blog/compromised-keyv-npm-supply-chain-attack/
  - https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/
  - https://isc.sans.edu/diary/rss/33218
  - https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/
  - https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack
  - https://securelist.com/cloud-platforms-in-phishing/120832/
  - https://cyberscoop.com/supply-chain-attack-malware-mini-shai-hulud-teampcp/
  - https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
  - https://www.securityweek.com/over-400-npm-packages-infected-in-chaindrop-supply-chain-attack/
  - https://www.bleepingcomputer.com/news/security/new-xcsset-variant-targets-macos-devs-via-compromised-xcode-projects/
  - https://securitylabs.datadoghq.com/articles/npm-worm-compromises-popular-npm-packages/
  - https://www.infosecurity-magazine.com/news/aws-north-korea-axios-npm-supply/
  - https://risky.biz/RBNEWS595/
  - https://www.securityweek.com/311000-impacted-by-brown-health-medical-group-ma-data-breach/

### AWS vulnerability activity
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 3
- Article count: 29
- Cohesion: 0.2
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: AWS, Apple iOS/macOS
- Cluster IDs: 61004037ea, ff79c00af4, 37a54c4646
- Links:
  - https://orca.security/resources/blog/compromised-keyv-npm-supply-chain-attack/
  - https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/
  - https://isc.sans.edu/diary/rss/33218
  - https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/
  - https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack
  - https://securelist.com/cloud-platforms-in-phishing/120832/
  - https://cyberscoop.com/supply-chain-attack-malware-mini-shai-hulud-teampcp/
  - https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
  - https://www.securityweek.com/over-400-npm-packages-infected-in-chaindrop-supply-chain-attack/
  - https://www.bleepingcomputer.com/news/security/new-xcsset-variant-targets-macos-devs-via-compromised-xcode-projects/
  - https://securitylabs.datadoghq.com/articles/npm-worm-compromises-popular-npm-packages/
  - https://www.infosecurity-magazine.com/news/aws-north-korea-axios-npm-supply/
  - https://risky.biz/RBNEWS595/
  - https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/
  - https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/
  - https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
  - https://www.bleepingcomputer.com/news/security/new-doublecup-clickfix-service-hides-malware-in-browser-cache-images/
  - https://aws.amazon.com/blogs/security/extend-amazon-inspector-sbom-generator-with-plugins/
  - https://risky.biz/RBNEWSSI138/

### VMware exploitation (2 CVEs)
- Anchor signal: VMware
- Theme key: vmware
- Cluster count: 2
- Article count: 2
- Cohesion: 0.485
- Shared strong signals: VMware
- Member CVEs: CVE-2026-59309, CVE-2026-59310
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: VMware
  - cve_ids: CVE-2026-59309, CVE-2026-59310
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 4a06e44c92, fe05850866
- Links:
  - https://www.rapid7.com/blog/post/etr-critical-vmware-vcenter-vulnerabilities-allow-authentication-bypass-and-remote-code-execution-cve-2026-59309-cve-2026-59310
  - https://research.checkpoint.com/2026/3rd-august-threat-intelligence-report/

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 3
- Article count: 3
- Cohesion: 0.333
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: b9f78fb1fa, f0542a4609, d00e5766ff
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/08/04/129-seconds-disruption-microsoft-defender-stops-ransomware-qnet/
  - https://orca.security/resources/blog/10-best-tenable-alternatives/
  - https://orca.security/resources/blog/7-best-rapid7-alternatives/

### ransomware extortion targeting SonicWall
- Anchor signal: SonicWall
- Theme key: sonicwall
- Cluster count: 3
- Article count: 5
- Cohesion: 0.237
- Shared strong signals: SonicWall
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, data_breach, zero_day
  - affected_industries: government, healthcare, financial_services
  - affected_products: SonicWall, Google/Gemini
  - urgency_signals: zero_day
- Cluster IDs: 1af5ed51b6, 1b822e43c0, 097b1c162f
- Links:
  - https://www.securityweek.com/cisa-warns-of-exploited-langflow-n-central-and-tomcat-vulnerabilities/
  - https://www.securityweek.com/311000-impacted-by-brown-health-medical-group-ma-data-breach/
  - https://cyberscoop.com/inc-ransomware-sonicwall-zero-day-attacks/
  - https://thehackernews.com/2026/08/inc-ransomware-emerges-as-dominant.html

### Kubernetes vulnerability activity
- Anchor signal: Kubernetes
- Theme key: kubernetes
- Cluster count: 2
- Article count: 21
- Cohesion: 0.2
- Shared strong signals: Kubernetes
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Kubernetes
- Cluster IDs: 61004037ea, c7d4f5e8ea
- Links:
  - https://orca.security/resources/blog/compromised-keyv-npm-supply-chain-attack/
  - https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/
  - https://isc.sans.edu/diary/rss/33218
  - https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/
  - https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack
  - https://securelist.com/cloud-platforms-in-phishing/120832/
  - https://cyberscoop.com/supply-chain-attack-malware-mini-shai-hulud-teampcp/
  - https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
  - https://www.securityweek.com/over-400-npm-packages-infected-in-chaindrop-supply-chain-attack/
  - https://www.bleepingcomputer.com/news/security/new-xcsset-variant-targets-macos-devs-via-compromised-xcode-projects/
  - https://securitylabs.datadoghq.com/articles/npm-worm-compromises-popular-npm-packages/
  - https://www.infosecurity-magazine.com/news/aws-north-korea-axios-npm-supply/
  - https://risky.biz/RBNEWS595/
  - https://www.elastic.co/security-labs/ai-agent-attack-detection-hugging-face-breach

### CVE-2026-20316 exploitation activity
- Anchor signal: CVE-2026-20316
- Theme key: cve-2026-20316
- Cluster count: 2
- Article count: 2
- Cohesion: 0.269
- Shared strong signals: CVE-2026-20316
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_industries: government
  - cve_ids: CVE-2026-20316
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 7ef6c747eb, fe05850866
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20316/
  - https://research.checkpoint.com/2026/3rd-august-threat-intelligence-report/

### LockBit: ransomware extortion
- Anchor signal: LockBit
- Theme key: lockbit
- Cluster count: 2
- Article count: 2
- Cohesion: 0.731
- Shared strong signals: LockBit
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - actor_attribution: LockBit
- Cluster IDs: b00983247a, f6cd02268d
- Links:
  - https://securelist.com/incidents-at-brazilian-educational-institutions/120803/
  - https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/

### Cisco vulnerability activity
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Cisco
- Cluster IDs: 7ef6c747eb, 582de97f0f
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20316/
  - https://www.sophos.com/en-us/blog/2608-volatility-interlock

### Microsoft SharePoint active exploitation
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Microsoft SharePoint
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Microsoft SharePoint
  - urgency_signals: actively_exploited, poc_available
- Cluster IDs: 213b4e62b3, b138851666
- Links:
  - https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-langflow-n-central-apache-tomcat-flaws/
  - https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html

### Fortinet vulnerability activity
- Anchor signal: Fortinet
- Theme key: fortinet
- Cluster count: 2
- Article count: 2
- Cohesion: 0.333
- Shared strong signals: Fortinet
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Fortinet
- Cluster IDs: d00e5766ff, f0d6d20493
- Links:
  - https://orca.security/resources/blog/7-best-rapid7-alternatives/
  - https://thehackernews.com/2026/08/quickfox-supply-chain-attack-delivers.html

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (1)
- **Compromised keyv Maintainer Account Triggers Massive npm Supply Chain Attack**
  - Cluster: 61004037ea
  - Sources in window: 3
  - Window hours: 4.7
  - Cohort count: 5

### Leading edge (1)
- **Compromised keyv Maintainer Account Triggers Massive npm Supply Chain Attack**
  - Cluster: 61004037ea
  - Lead hours: 32.1
  - First source: Risky Business News
  - Later Tier 1 source: Kaspersky Securelist
  - Shared signals: AWS, Anthropic/Claude, Apple iOS/macOS, GitHub, Kubernetes, TeamPCP, npm

### Convergence (15)
- Pair: CVE-2026-59309 + VMware (cluster 4a06e44c92, first observation: True)
- Pair: CVE-2026-59310 + VMware (cluster 4a06e44c92, first observation: True)
- Pair: APT29 + Microsoft 365 (cluster 4c8ed8c5fa, first observation: True)
- Pair: APT29 + PyPI (cluster 4c8ed8c5fa, first observation: True)
- Pair: APT29 + SolarWinds (cluster 4c8ed8c5fa, first observation: True)
- Pair: APT29 + npm (cluster 4c8ed8c5fa, first observation: True)
- Pair: TeamPCP + Microsoft 365 (cluster 4c8ed8c5fa, first observation: True)
- Pair: TeamPCP + SolarWinds (cluster 4c8ed8c5fa, first observation: True)
- Pair: UNC4736 + Microsoft 365 (cluster 4c8ed8c5fa, first observation: True)
- Pair: UNC4736 + PyPI (cluster 4c8ed8c5fa, first observation: True)
- Pair: UNC4736 + SolarWinds (cluster 4c8ed8c5fa, first observation: True)
- Pair: UNC4736 + npm (cluster 4c8ed8c5fa, first observation: True)
- Pair: CVE-2026-18556 + Citrix (cluster e9b42737b7, first observation: True)
- Pair: CVE-2026-18556 + GitHub (cluster e9b42737b7, first observation: True)
- Pair: CVE-2026-18556 + Palo Alto Networks (cluster e9b42737b7, first observation: True)

### Drift (5)
- **APT29** (cluster 4c8ed8c5fa)
  - New industries: (none)
  - New products: Microsoft 365
  - Prior top industries: (none)
  - Prior top products: PyPI, SolarWinds, npm
- **TeamPCP** (cluster 4c8ed8c5fa)
  - New industries: (none)
  - New products: Microsoft 365, SolarWinds
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: GitHub, PyPI, npm
- **UNC4736** (cluster 4c8ed8c5fa)
  - New industries: (none)
  - New products: Microsoft 365
  - Prior top industries: (none)
  - Prior top products: PyPI, SolarWinds, npm
- **LockBit** (cluster b00983247a)
  - New industries: education, financial_services
  - New products: (none)
  - Prior top industries: critical_infrastructure, government, manufacturing_industrial
  - Prior top products: Citrix, Fortinet, ScreenConnect
- **ShinyHunters** (cluster 37a54c4646)
  - New industries: (none)
  - New products: AWS
  - Prior top industries: education, financial_services, government
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce

### Persistence (8)
- actor_attribution: ShinyHunters (weeks observed: 10, cluster 37a54c4646)
- actor_attribution: TeamPCP (weeks observed: 8, cluster 4c8ed8c5fa)
- cve_ids: CVE-2026-33017 (weeks observed: 7, cluster e9b42737b7)
- actor_attribution: LockBit (weeks observed: 5, cluster b00983247a)
- actor_attribution: APT29 (weeks observed: 3, cluster 4c8ed8c5fa)
- cve_ids: CVE-2026-0770 (weeks observed: 3, cluster 213b4e62b3)
- cve_ids: CVE-2026-59726 (weeks observed: 3, cluster fe05850866)
- cve_ids: CVE-2026-15409 (weeks observed: 3, cluster 097b1c162f)

### Tier inversion (1)
- **Stored XSS in Django's admin via an unvalidated URLField display path (CVE-2026-15920)**
  - Cluster: cd780b1305
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-15920

## Clusters

### Cluster 65ab16fa91 — score 56

- Title: CVE-2026-18577: N-able N-central Authentication Bypass Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-08-04T11:11:54+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-18577-n-able-n-central-authentication-bypass-exploited-in-the-wild
- Fetch status: ok
- Member count: 6
- Corroborating source count: 5
- Strong signals: CVE-2026-18556, CVE-2026-18577

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-18556, CVE-2026-18577
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-18577, CVE-2026-18556
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On August 2, 2026, N-able published a security advisory for CVE-2026-18577 , an authentication bypass vulnerability affecting N-central that was discovered being exploited in-the-wild after an incomplete fix for an earlier authentication bypass issue, CVE-2026-18556 was disclosed. CVE-2026-18577 allows a remote unauthenticated attacker to bypass authentication and obtain administrative control of vulnerable N-central servers in affected deployments. N-able N-central is a widely deployed Remote Monitoring and Management (RMM) platform used by managed service providers (MSPs) and enterprise IT teams to centrally administer servers, workstations, network devices, and other managed assets. Because the platform operates with extensive administrative privileges across customer environments, successful compromise of an N-central server can provide attackers with an efficient path to compromise downstream managed systems. According to N-able, exploitation of CVE-2026-18577 has been ob
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-18577: N-able N-central Authentication Bypass Exploited in the Wild Rapid7 Aug 4, 2026 | Last updated on Aug 4, 2026 | 3 min read Overview On August 2, 2026, N-able published a security advisory for CVE-2026-18577 , an authentication bypass vulnerability affecting N-central that was discovered being exploited in-the-wild after an incomplete fix for an earlier authentication bypass issue, CVE-2026-18556 was disclosed. CVE-2026-18577 allows a remote unauthenticated attacker to bypass authentication and obtain administrative control of vulnerable N-central servers in affected deployments. N-able N-central is a widely deployed Remote Monitoring and Management (RMM) platform used by managed service providers (MSPs) and enterprise IT teams to centrally administer servers, workstations, network devices, and other managed assets. Because the platform operates with extensive administrative privileges across customer environments, successful compromise of an N-central server can provide attackers with an efficient path to compromise downstream managed systems. According to N-able, exploitation of CVE-2026-18577 has been observed in the wild since August 1, 2026 . Following successful exploitation, attackers leveraged the platform's Take Control functionality to remotely access managed endpoints, and deployed Cloudflare Tunnel (cloudflared) to establish persistent remote access. On August 3, 2026, CVE-2026-18577 was added to CISA’s Known Exploited Vulnerability (KEV) catalog. Mitigation guidance Organizations operating vulnerable N-central deployments should prioritize remediation on an urgent basis, outside of normal patching schedules. Hosted N-central environments are upgraded automatically by the vendor, while on-premise deployments require manual remediation. Affected versions: All versions of N-able N-central up to and including version 2026.3.1, prior to Hotfix 1. Fixed version: N-able N-central 2026.3.1 Hotfix 1 (2026.3.1.7). The vendor also recommends: Upgrading N-central agents after applying the server hotfix. Reviewing systems for indicators of compromise. Contacting N-able Support immediately if evidence of compromise is discovered. Engaging internal incident response teams if malicious activity is identified. For further information, see the vendor advisory . IOCs N-able has published several artifacts that administrators should investigate during incident response. Endpoint Artifacts: Presence of a Cloudflared service. A suspicious svchost.exe located within the user's Documents folder. Network Indicators: Administrators should review historical network logs for inbound or outbound communication involving the malicious IP addresses identified by the vendor: 173[.]249[.]252[.]200 87[.]249[.]138[.]34 37[.]19[.]210[.]32 37[.]153[.]90[.]88 92[.]118[.]112[.]181 68[.]235[.]46[.]214 Organizations should also review: Authentication logs Administrative account creation or modification Take Control session activity Remote management logs Windows service installation events To assist affected organizations running N-central, the vendor has provided a detection template for CVE-2026-18577, which organizations can use to help identify potential compromise. Rapid7 customers Exposure Command, InsightVM, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-18577 with a vulnerability check available in the August 4 content release. Note that potential check type must be enabled in the scan template before scanning. Updates August 4, 2026: Initial publication. August 4, 2026: Updated Rapid7 customers section to reflect the availability of vulnerability checks. Article Tags Emergent Threat Response Labs Vulnerability Management Rapid7 Author Posts
```

#### Corroborating sources (5)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-18577: N-able N-central Authentication Bypass Exploited in the Wild
  - Published: 2026-08-04T11:11:54+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-18577-n-able-n-central-authentication-bypass-exploited-in-the-wild
  - Summary: Overview On August 2, 2026, N-able published a security advisory for CVE-2026-18577 , an authentication bypass vulnerability affecting N-central that was discovered being exploited in-the-wild after an incomplete fix for an earlier authentication bypass issue, CVE-2026-18556 was disclosed. CVE-2026-18577 allows a remote unauthenticated attacker to bypass authentication and obtain administrative control of vulnerable N-central servers in affected deployments. N-able N-central is a widely deployed Remote Monitoring and Management (RMM) platform used by managed service providers (MSPs) and enterprise IT teams to centrally administer servers, workstations, network devices, and other managed assets. Because the platform operates with extensive administrative privileges across customer environments, successful compromise of an N-central server can provide attackers with an efficient path to compromise downstream managed systems. According to N-able, exploitation of CVE-2026-18577 has been ob
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-18556 and CVE-2026-18577 | N-able N-central Authentication Bypass Vulnerabilities
  - Published: 2026-08-05T18:54:10+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-18556-cve-2026-18577/
  - Summary: CVE-2026-18556 and CVE-2026-18577 are authentication bypass vulnerabilities affecting N-able N-central. NodeZero® Rapid Response safely validates exposure and verifies remediation.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Adds Exploited N-able N-central Flaw to KEV After Customer Compromises
  - Published: 2026-08-04T07:00:13+00:00
  - Link: https://thehackernews.com/2026/08/cisa-adds-exploited-n-able-n-central.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a high-severity security flaw impacting N-able N-central to its Known Exploited Vulnerabilities (KEV) catalog following reports of active exploitation in the wild. The vulnerability, tracked as CVE-2026-18577 (CVSS score: 8.2), is a case of incomplete patching for CVE-2026-18556 (CVSS score: 8.2) that allows
- **Sophos X-Ops** (detection_response_operations)
  - Title: N-able N-central exploitation results in RMM tool deployment
  - Published: 2026-08-04T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/nable-ncentral-exploitation-results-in-rmm-tool-deployment
  - Summary: After compromising systems via CVE-2026-18577, threat actors use the additional RMM tools and network tunnels to establish persistent remote access Categories: Threat Research Tags: RMM, N-able, vulnerability
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Attackers Exploit N-able Patch Bypass Flaw on RMM Servers
  - Published: 2026-08-03T21:21:11+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/attackers-exploit-n-able-patch-bypass-flaw
  - Summary: Over the weekend, the vendor discovered another vector of authentication bypass CVE-2026-18577 that gives attackers administrator access.

### Cluster 4a06e44c92 — score 38

- Title: Critical VMware vCenter Vulnerabilities Allow Authentication Bypass and Remote Code Execution (CVE-2026-59309, CVE-2026-59310)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-30T10:35:21+00:00
- Link: https://www.rapid7.com/blog/post/etr-critical-vmware-vcenter-vulnerabilities-allow-authentication-bypass-and-remote-code-execution-cve-2026-59309-cve-2026-59310
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-59309, CVE-2026-59310, VMware

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: VMware
- cve_ids: CVE-2026-59309, CVE-2026-59310
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: VMware
- cve_ids: CVE-2026-59309, CVE-2026-59310
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 29, 2026, Broadcom published security advisory VMSA-2026-0006 addressing multiple vulnerabilities in several VMWare products. Included in the advisory are two critical remotely exploitable vulnerabilities affecting VMware vCenter Server: CVE-2026-59309 and CVE-2026-59310 . Both vulnerabilities carry CVSSv3.1 base scores of 9.8 and can be exploited by unauthenticated attackers with network access to a vulnerable vCenter Server. CVE CVSSv3.1 Description Summary CVE-2026-59309 9.8 (Critical) An authentication bypass vulnerability in the VMware Directory Service of vCenter that could allow a remote attacker to bypass authentication and gain unauthorized access to the vCenter management plane. CVE-2026-59310 9.8 (Critical) A directory traversal vulnerability in the vCenter Syslog server that could allow an attacker with network access to execute arbitrary code. VMware vCenter Server provides centralized management for VMware vSphere environments, allowing administrators to
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits Critical VMware vCenter Vulnerabilities Allow Authentication Bypass and Remote Code Execution (CVE-2026-59309, CVE-2026-59310) Rapid7 Jul 30, 2026 | Last updated on Aug 4, 2026 | 3 min read Overview On July 29, 2026, Broadcom published security advisory VMSA-2026-0006 addressing multiple vulnerabilities in several VMWare products. Included in the advisory are two critical remotely exploitable vulnerabilities affecting VMware vCenter Server: CVE-2026-59309 and CVE-2026-59310 . Both vulnerabilities carry CVSSv3.1 base scores of 9.8 and can be exploited by unauthenticated attackers with network access to a vulnerable vCenter Server. CVE CVSSv3.1 Description Summary CVE-2026-59309 9.8 (Critical) An authentication bypass vulnerability in the VMware Directory Service of vCenter that could allow a remote attacker to bypass authentication and gain unauthorized access to the vCenter management plane. CVE-2026-59310 9.8 (Critical) A directory traversal vulnerability in the vCenter Syslog server that could allow an attacker with network access to execute arbitrary code. VMware vCenter Server provides centralized management for VMware vSphere environments, allowing administrators to manage ESXi hosts, virtual machines, resource allocation, availability, and other virtualization infrastructure from a central control plane. Compromise of vCenter can therefore provide an attacker with significant control over the virtualized environment and its associated workloads. Both vulnerabilities are particularly significant because exploitation does not require prior authentication. However, an attacker must have network access to the affected vCenter services. Management interfaces such as vCenter are commonly restricted to internal or dedicated management networks, which can reduce exposure to internet-based attacks but does not mitigate the risk from an attacker who has already established access to an organization’s network. At the time of publication, there is no known evidence of exploitation or scanning in the wild for either CVE-2026-59309 or CVE-2026-59310. There is also currently no known public proof-of-concept exploit code. However, vCenter Server has appeared on CISA’s KEV list ten times in the past for other vulnerabilities, so it is known that attackers target critical issues in this product. Customers running affected VMWare products are urged to patch on an urgent basis before exploitation in-the-wild occurs. Mitigation guidance Organizations running VMware vCenter Server should prioritize applying the updates identified by Broadcom in VMSA-2026-0006 on an urgent basis. Broadcom states that there are no workarounds for CVE-2026-59309 or CVE-2026-59310, making vendor-provided updates the primary remediation. VMware Product Component Version Running On Fixed Version VMware Cloud Foundation, VMware vSphere Foundation vCenter 9.1.x.x Any 9.1.0.0300 VMware Cloud Foundation, VMware vSphere Foundation vCenter 9.0.x.x Any 9.0.2.0100 VMware vCenter N/A 8.0 Any 8.0 U3k VMware Cloud Foundation vCenter 5.x Any Async patch to 8.0 U3k VMware Telco Cloud Platform vCenter 3.0, 4.x, 5.0.x, 5.1.x Any Refer to KB449886 VMware Telco Cloud Infrastructure vCenter 3.0 Any Refer to KB449886 For the latest mitigation guidance, please refer to the vendor advisory . Rapid7 customers Exposure Command, InsightVM, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-59309 and CVE-2026-59310 on VMware vCenter Server, Cloud Foundation, and vSphere Foundation products with unauthenticated vulnerability checks expected to be available in the July 30 content release. Updates July 30, 2026: Initial publication. July 30, 2026: Updated customers section to reflect availability of vulnerability checks. August 4, 2026: Updated CVE links. Article Tags Emergent Threat Response Labs Rapid7 Author Posts
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Critical VMware vCenter Vulnerabilities Allow Authentication Bypass and Remote Code Execution (CVE-2026-59309, CVE-2026-59310)
  - Published: 2026-07-30T10:35:21+00:00
  - Link: https://www.rapid7.com/blog/post/etr-critical-vmware-vcenter-vulnerabilities-allow-authentication-bypass-and-remote-code-execution-cve-2026-59309-cve-2026-59310
  - Summary: Overview On July 29, 2026, Broadcom published security advisory VMSA-2026-0006 addressing multiple vulnerabilities in several VMWare products. Included in the advisory are two critical remotely exploitable vulnerabilities affecting VMware vCenter Server: CVE-2026-59309 and CVE-2026-59310 . Both vulnerabilities carry CVSSv3.1 base scores of 9.8 and can be exploited by unauthenticated attackers with network access to a vulnerable vCenter Server. CVE CVSSv3.1 Description Summary CVE-2026-59309 9.8 (Critical) An authentication bypass vulnerability in the VMware Directory Service of vCenter that could allow a remote attacker to bypass authentication and gain unauthorized access to the vCenter management plane. CVE-2026-59310 9.8 (Critical) A directory traversal vulnerability in the vCenter Syslog server that could allow an attacker with network access to execute arbitrary code. VMware vCenter Server provides centralized management for VMware vSphere environments, allowing administrators to

### Cluster 4c8ed8c5fa — score 32

- Title: Batten Down Your Packages: Mitigation Guidance for Supply Chain Compromise
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-07-30T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: APT29, SolarWinds, UNC4736

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, credential_theft, phishing_social_eng, ransomware_extortion, supply_chain
- actor_attribution: APT29, TeamPCP, UNC4736
- affected_products: Microsoft 365, PyPI, SolarWinds, npm
- attack_techniques: T1195.001
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, apt_espionage
- actor_attribution: APT29, TeamPCP, UNC4736
- affected_products: SolarWinds, PyPI, npm
- attack_techniques: T1195.001
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Kelli Vanderlee, Stuart Carrera For years, the cybersecurity industry's understanding of software supply chain compromise has been anchored by a few watershed events, including Russian cyber espionage actor ICE RELIC’s (formerly known as APT29) 2020 compromise of SolarWinds and North Korean cyber espionage actor UNC4736's 2023 compromise of 3CX . However, Google Threat Intelligence Group (GTIG) has been tracking growth in threat activity targeting open source software repositories to conduct supply chain compromises over the past several years. A series of large scale open source software supply chain compromise campaigns in 2025 and the first half of 2026 underscore how important it is that organizations implement defensive strategies that directly address this threat vector. In this blog post, GTIG and Mandiant discuss trends we have observed in threat actor use of software supply chain compromise, and provide mitigation and hardening recommendations that incorporate insi
```

#### Full body

```
Threat Intelligence Batten Down Your Packages: Mitigation Guidance for Supply Chain Compromise July 30, 2026 Google Threat Intelligence Group Mandiant Mandiant Services Stop attacks, reduce risk, and advance your security. Contact Mandiant Written by: Kelli Vanderlee, Stuart Carrera For years, the cybersecurity industry's understanding of software supply chain compromise has been anchored by a few watershed events, including Russian cyber espionage actor ICE RELIC’s (formerly known as APT29) 2020 compromise of SolarWinds and North Korean cyber espionage actor UNC4736's 2023 compromise of 3CX . However, Google Threat Intelligence Group (GTIG) has been tracking growth in threat activity targeting open source software repositories to conduct supply chain compromises over the past several years. A series of large scale open source software supply chain compromise campaigns in 2025 and the first half of 2026 underscore how important it is that organizations implement defensive strategies that directly address this threat vector. In this blog post, GTIG and Mandiant discuss trends we have observed in threat actor use of software supply chain compromise, and provide mitigation and hardening recommendations that incorporate insights we have developed as a result of supporting customers through recent campaigns in which threat actors manipulated open source packages. Open Source Supply Chain Compromise Grows in Volume and Impact in 2025 and Early 2026 The majority of the most impactful and far-reaching supply chain compromise incidents that GTIG tracked in 2025 and early 2026 involved the compromise of code repositories, software dependencies and developer tools (T1195.001). Open source supply chain compromises offer attackers the same efficiency, scale, and initial stealth as traditional supply chain compromises, but typically require significantly less planning and resources to execute. However, open source supply chain compromises are also noisy once enabled; malicious open source packages are often discovered and publicized much more quickly than traditional supply chain compromises. GTIG assesses with high confidence that the growth in very large-scale, open-source supply chain compromise campaigns , including use of worms and iterative compromises in 2025 and early 2026, represent a significant expansion in use of this tactic compared to prior years. We anticipate that threat actors will emulate the tactics of these campaigns and contribute to growth in open-source supply chain compromise through the rest of 2026 and years to come. GTIG identified several notable supply chain compromises in 2025 and early 2026 that we believe exemplify this trend of exceptionally large campaigns, as measured by size and/or impact (Figure 1). Figure 1: Notable open source supply chain compromises, 2025 - early 2026 For example from February to May 2026, UNC6780 (aka "TeamPCP") conducted extensive open source supply chain compromises targeting ecosystems like PyPI, npm, and Docker Hub. Initial infection vectors varied across incidents, and included abuse of the pull_request_target GitHub Actions trigger to obtain base repository secrets and write permissions. The threat actor typically used compromised packages to deploy credential stealers, including SANDCLOCK, to obtain high value secrets. In incident response engagements, we observed UNC6780 attempting to pivot from compromised artificial intelligence (AI) software to broader network environments. UNC6780 has monetized stolen credentials through either direct sale of the stolen data, or through partnerships with ransomware and data theft extortion groups. In March 2026, GTIG observed the introduction of a malicious dependency in the legitimate axios package. GTIG analysis and the maintainer's post mortem indicate that the maintainer account was compromised via social engineering and used to publish the updated versions. We identified the malicious dependency as a dropper that deploys the WAVESHA
```

#### Corroborating sources (6)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Batten Down Your Packages: Mitigation Guidance for Supply Chain Compromise
  - Published: 2026-07-30T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
  - Summary: Written by: Kelli Vanderlee, Stuart Carrera For years, the cybersecurity industry's understanding of software supply chain compromise has been anchored by a few watershed events, including Russian cyber espionage actor ICE RELIC’s (formerly known as APT29) 2020 compromise of SolarWinds and North Korean cyber espionage actor UNC4736's 2023 compromise of 3CX . However, Google Threat Intelligence Group (GTIG) has been tracking growth in threat activity targeting open source software repositories to conduct supply chain compromises over the past several years. A series of large scale open source software supply chain compromise campaigns in 2025 and the first half of 2026 underscore how important it is that organizations implement defensive strategies that directly address this threat vector. In this blog post, GTIG and Mandiant discuss trends we have observed in threat actor use of software supply chain compromise, and provide mitigation and hardening recommendations that incorporate insi
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Batten Down Your Packages: Mitigation Guidance for Supply Chain Compromise
  - Published: 2026-07-30T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
  - Summary: Written by: Kelli Vanderlee, Stuart Carrera For years, the cybersecurity industry's understanding of software supply chain compromise has been anchored by a few watershed events, including Russian cyber espionage actor ICE RELIC’s (formerly known as APT29) 2020 compromise of SolarWinds and North Korean cyber espionage actor UNC4736's 2023 compromise of 3CX . However, Google Threat Intelligence Group (GTIG) has been tracking growth in threat activity targeting open source software repositories to conduct supply chain compromises over the past several years. A series of large scale open source software supply chain compromise campaigns in 2025 and the first half of 2026 underscore how important it is that organizations implement defensive strategies that directly address this threat vector. In this blog post, GTIG and Mandiant discuss trends we have observed in threat actor use of software supply chain compromise, and provide mitigation and hardening recommendations that incorporate insi
- **Microsoft Security Blog** (threat_research_primary)
  - Title: CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft
  - Published: 2026-07-31T21:01:37+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
  - Summary: Storm-2945, a sub-cluster of the Russian threat actor Midnight Blizzard, has been observed compromising the sign-in portals of hospitality-related organizations such as hotels since May 2026 in order to deliver malware to travelers and steal credentials in an operation we call CaptiveCrunch. The post CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft
  - Published: 2026-07-31T21:01:37+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
  - Summary: Storm-2945, a sub-cluster of the Russian threat actor Midnight Blizzard, has been observed compromising the sign-in portals of hospitality-related organizations such as hotels since May 2026 in order to deliver malware to travelers and steal credentials in an operation we call CaptiveCrunch. The post CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft appeared first on Microsoft Security Blog .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hotel Wi-Fi attacks use custom malware to breach Microsoft 365 accounts
  - Published: 2026-08-04T00:17:15+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hotel-wi-fi-attacks-use-custom-malware-to-breach-microsoft-365-accounts/
  - Summary: Microsoft has linked a global campaign targeting hospitality Wi-Fi networks to the Russian threat actor Midnight Blizzard, also known as APT29. [...]
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Midnight Blizzard Targets Travelers via Captive Portals
  - Published: 2026-08-03T14:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/captivecrunch-midnight-blizzard/
  - Summary: Russian actor Storm-2945 hijacked hotel captive portals to push fake updates and steal tokens

### Cluster 513073eb52 — score 30

- Title: KindaRails2Shell: CVE-2026-66066, Critical Arbitrary File Read and Possible Remote Code Execution in Ruby on Rails
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-30T16:11:10+00:00
- Link: https://www.rapid7.com/blog/post/etr-kindarails2shell-cve-2026-66066-critical-arbitrary-file-read-and-possible-remote-code-execution-in-ruby-on-rails
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: CVE-2026-66066

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-66066
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-66066
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 29, 2026, the Ruby on Rails project published a security advisory for CVE-2026-66066 , a critical vulnerability affecting Active Storage image processing when used in conjunction with the libvips image processing library. The vulnerability has a CVSSv4 score of 9.5 and is classified as Initialization of a Resource with an Insecure Default ( CWE-1188 ). An unauthenticated attacker may be able to leverage CVE-2026-66066 and read files accessible to the Rails application process, potentially exposing secrets that could enable remote code execution (RCE) or access to connected systems. An application is affected when it uses libvips for Active Storage image processing and accepts image uploads from untrusted users. Rails notes that generating image variants is not a separate requirement for exposure. Vips is the default Active Storage variant processor for applications configured with Rails 7.0 or later defaults. According to Ethiack , only the Vips processor is affected;
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits KindaRails2Shell: CVE-2026-66066, Critical Arbitrary File Read and Possible Remote Code Execution in Ruby on Rails Rapid7 Labs Jul 30, 2026 | Last updated on Aug 3, 2026 | 6 min read Overview On July 29, 2026, the Ruby on Rails project published a security advisory for CVE-2026-66066 , a critical vulnerability affecting Active Storage image processing when used in conjunction with the libvips image processing library. The vulnerability has a CVSSv4 score of 9.5 and is classified as Initialization of a Resource with an Insecure Default ( CWE-1188 ). An unauthenticated attacker may be able to leverage CVE-2026-66066 and read files accessible to the Rails application process, potentially exposing secrets that could enable remote code execution (RCE) or access to connected systems. An application is affected when it uses libvips for Active Storage image processing and accepts image uploads from untrusted users. Rails notes that generating image variants is not a separate requirement for exposure. Vips is the default Active Storage variant processor for applications configured with Rails 7.0 or later defaults. According to Ethiack , only the Vips processor is affected; applications using Magick are not affected through the reported vector. As of July 30, 2026, Rapid7 is not aware of exploitation in the wild. Ethiack and GMO Flatt Security, who independently reported the vulnerability, have withheld proof-of-concept code and details of the full attack chain. Public code claiming to exploit CVE-2026-66066 exists, but it is unclear how closely it corresponds to the full attack chain reported privately to Rails. According to the Rails Security Announcement , additional details will be disclosed no later than August 28, 2026. Rapid7 recommends remediating affected applications on an urgent basis, outside of normal patch cycles. Update #1 : On July 31, 2026, Rails published technical details and forensic tools earlier than its planned August 28 disclosure date after several researchers reverse-engineered the attack and published proof-of-concept code. Technical overview libvips uses operations to load and save image formats, including operations backed by third-party libraries. Some are marked "unfuzzed" or "untrusted" because they are unsafe for untrusted content. According to Rails, Active Storage did not disable these operations before processing user-supplied files, which may allow a crafted upload to trigger an unsafe operation and disclose files readable by the application. The attack details published by Rails describe a chain in which an attacker creates a blob through Active Storage's direct-upload endpoint with a false image content type and obtains a genuine signed variation_key from a page that renders an Active Storage representation. A crafted file identifies itself to libvips as a MATLAB level 5 file but to libmatio as a MAT 7.3 HDF5 container. HDF5's External File List then reads bytes from an attacker-selected path, which are rendered as image pixels and returned in the resulting variant. This known chain also requires the deployed libvips build to include the matload operation. For this documented chain, the Active Storage direct-upload route must be reachable. When Active Storage routes are mounted, the direct-upload route is present by default even if the application's own interface does not use direct uploads. Rapid7 testing found that ordinary server-side attachment does not satisfy this chain because Rails re-identifies the crafted file as MATLAB data before variant processing. The arbitrary file-read stage does not require knowledge of secret_key_base or a forged variation key. Rapid7 also verified an RCE escalation in which recovered Rails signing material is used to forge an ImageProcessing 1.x variation; this path does not require Marshal deserialization. The Rails patch that remediates CVE-2026-66066, disables untrusted operations during Active Storage initialization.
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: KindaRails2Shell: CVE-2026-66066, Critical Arbitrary File Read and Possible Remote Code Execution in Ruby on Rails
  - Published: 2026-07-30T16:11:10+00:00
  - Link: https://www.rapid7.com/blog/post/etr-kindarails2shell-cve-2026-66066-critical-arbitrary-file-read-and-possible-remote-code-execution-in-ruby-on-rails
  - Summary: Overview On July 29, 2026, the Ruby on Rails project published a security advisory for CVE-2026-66066 , a critical vulnerability affecting Active Storage image processing when used in conjunction with the libvips image processing library. The vulnerability has a CVSSv4 score of 9.5 and is classified as Initialization of a Resource with an Insecure Default ( CWE-1188 ). An unauthenticated attacker may be able to leverage CVE-2026-66066 and read files accessible to the Rails application process, potentially exposing secrets that could enable remote code execution (RCE) or access to connected systems. An application is affected when it uses libvips for Active Storage image processing and accepts image uploads from untrusted users. Rails notes that generating image variants is not a separate requirement for exposure. Vips is the default Active Storage variant processor for applications configured with Rails 7.0 or later defaults. According to Ethiack , only the Vips processor is affected;

### Cluster 1bbada40f0 — score 29

- Title: The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software
- Source: Unit 42 (threat_research_primary)
- Published: 2026-08-04T13:00:11+00:00
- Link: https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, zero_day
- urgency_signals: poc_available, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day
- urgency_signals: zero_day, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
Frontier AI is reshaping vulnerability discovery. Learn how our NOVA system found 14,000+ unknown vulnerabilities across the open-source software supply chain. The post The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights Vulnerabilities Vulnerabilities The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software 11 min read Related Products Unit 42 AI Security Assessment Unit 42 Frontier AI Defense Unit 42 Incident Response By: Xu Zou Published: August 4, 2026 Categories: General Insights Vulnerabilities Tags: AI Frontier AI Vulnerability Exploitation Zero-day Share Executive Summary Frontier AI is fundamentally shifting the dynamics of cybersecurity — accelerating both how vulnerabilities are discovered and how quickly they can be exploited. Our vulnerability research team built an autonomous vulnerability discovery, validation and reporting system that we call Network and Open-Source Vulnerability Analyzer (NOVA), an agentic research system that leverages proprietary AI harnesses powered by multiple leading frontier AI models. Our goal with this research is twofold: (1) contribute to improving the security of the software supply chain; and (2) ensure our customers are protected from vulnerabilities in the AI era. In just two months, NOVA analyzed 3,915 open-source software (OSS) projects and uncovered 14,090 confirmed vulnerabilities, 99.4% of which were previously unreported and 40% of them designated as high or critical severity. Nearly every frontier and open-weight model evaluated could find real vulnerabilities, with the strongest results coming from an ensemble of models, specialized security tools, and automated harnesses working together. These initial results illustrate just how dramatic the impact of AI is on the vulnerability landscape. In response to these significant results, we are actively partnering with open-source maintainers and clearinghouses such as Lightwell and Akrites to responsibly disclose these vulnerabilities and ensure they are patched upstream quickly and securely. Securing the broader open-source supply chain ultimately protects the entire software ecosystem and benefits everyone. Our experience with NOVA highlights a clear structural change: the patch window has collapsed. When vulnerability discovery accelerates, the time between disclosure and potential exploitation shrinks dramatically. And attackers need not have access to the latest frontier AI model to reverse engineer patches and develop exploits automatically. This new reality also makes virtual patching an even more important defense strategy in the AI era, and is a key driving force behind our recently announced Advanced Virtual Patching , the next evolution in network vulnerability protection. Advanced Virtual Patching is designed to operate at the speed of AI to keep pace with the new normal of higher rates of vulnerability discovery and compressed attack windows. By harnessing frontier AI to discover unknown vulnerabilities, and deploying protections in hours, we are collapsing the exposure window from the industry-average 55 days it takes to deploy a traditional patch down into a near-zero window of exposure. Our new “vaulted protection” technology enables us to deliver protections ahead of patch availability in a safe and responsible manner. In addition to these protections available with our network security platform, we recommend that organizations deploy relevant best practices, including vulnerability management, zero-trust network architecture, software supply chain security, and other attack surface reduction best practices. NOVA: Fully Automated Novel Vulnerability Discovery and Validation Our vulnerability research team built a fully autonomous vulnerability discovery system requiring no human in the loop until final review. We call this the Network and Open-Source Vulnerability Analyzer (NOVA). For each project we analyzed, NOVA performed the following functions: Review of the project history Reading the source code Identification of vulnerability candidates Creation of a working proof of concept (PoC) Deterministic validation of whether the vulnerability is t
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software
  - Published: 2026-08-04T13:00:11+00:00
  - Link: https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/
  - Summary: Frontier AI is reshaping vulnerability discovery. Learn how our NOVA system found 14,000+ unknown vulnerabilities across the open-source software supply chain. The post The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software appeared first on Unit 42 .

### Cluster e9b42737b7 — score 29

- Title: CISA Flags Langflow RCE, Tomcat, and N-central Flaws as Actively Exploited
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-05T07:40:39+00:00
- Link: https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-9198

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Citrix, GitHub, Palo Alto Networks
- cve_ids: CVE-2026-18556, CVE-2026-18577, CVE-2026-33017, CVE-2026-34486, CVE-2026-9198
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Citrix, GitHub, Palo Alto Networks
- cve_ids: CVE-2026-9198, CVE-2026-34486, CVE-2026-18556, CVE-2026-18577, CVE-2026-33017
- urgency_signals: actively_exploited, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on August 5, 2026, added three flaws to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation in the wild. The list of vulnerabilities is as follows - CVE-2026-9198 (CVSS score: 9.8) - A code injection vulnerability in Langflow that allows unauthenticated attackers to achieve full remote
```

#### Full body

```
CISA Flags Langflow RCE, Tomcat, and N-central Flaws as Actively Exploited  Ravie Lakshmanan  Aug 05, 2026 Vulnerability / Patch Management The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on August 5, 2026, added three flaws to its Known Exploited Vulnerabilities ( KEV ) catalog, citing evidence of active exploitation in the wild. The list of vulnerabilities is as follows - CVE-2026-9198 (CVSS score: 9.8) - A code injection vulnerability in Langflow that allows unauthenticated attackers to achieve full remote code execution on default Langflow deployments. (Fixed in July 2026 with version 1.10.1) CVE-2026-34486 (CVS score: 7.5) - A missing encryption of sensitive data vulnerability in Apache Tomcat that allows a bypass of EncryptInterceptor, a cluster component that adds pre-shared key encryption to messages sent between cluster nodes. (Fixed in April 2026 with versions 11.0.21, 10.1.54, and 9.0.117) Also added to the KEV catalog is CVE-2026-18556 (CVSS score: 8.2), an authentication bypass vulnerability in N-able N-central. It's worth noting that an incomplete fix for this issue prompted N-able to issue a fresh patch, which is tracked as CVE-2026-18577 (CVSS score: 8.2). While CVE-2026-18577 was placed in the KEV catalog on Monday, the latest development signals that both vulnerabilities are being exploited by threat actors. There are currently no details on how the Langflow flaw is being exploited. However, security defects in the open-source artificial intelligence (AI) application development platform have been repeatedly weaponized by bad actors in recent months. The exploitation of CVE-2026-34486, on the other hand, has been attributed to an AI-enabled autonomous hacking campaign orchestrated by a Chinese-speaking threat actor operating under the aliases knaithe and KnYuan. The threat actor, based in Zhuhai, China, is said to have leveraged DeepSeek, via the Hermes Agent framework, as an offensive operator to target internet-exposed devices. When initial attempts to exploit a Langflow flaw (CVE-2026-33017, CVSS 9.8) breach failed due to the target environment's restrictive configurations, the AI agent is said to have conducted autonomous research to identify other higher-value vulnerabilities, including flaws in n8n, to find a way in. Separately, the Chinese-speaking adversary has been found conducting manual operations using known vulnerabilities in Citrix NetScaler (CVE-2026-3055), Marimo (CVE-2026-39987), Apache Tomcat (CVE-2026-34486), and IKE VPN (CVE-2026-33824) endpoints. "This actor attempted to exploit over 460 targets, leveraging a mix of autonomous and manual techniques," Palo Alto Networks Unit 42 said . "What's interesting is that the actor appeared to allow DeepSeek to narrow the targeting scope, likely to conserve AI compute." "This autonomous process of target identification, sampling and narrowing of scope is notable because the system executed hundreds of hours of manual targeting analysis in mere minutes, while also managing its own compute resources." CVE-2026-34486 has also been weaponized in attacks mounted by a China-nexus threat actor targeting government and commercial infrastructure across more than 100 countries to deliver SNOWLIGHT , a lightweight, C-based Linux dropper and loader . The campaign is assessed to have taken place between late April and early June 2026. The activity was discovered by SOCRadar following an analysis of an exposed adversary-operated staging server containing reconnaissance lists, nine weaponized CVEs, a cracked Chinese version of Cobalt Strike dubbed GoCobaltStrike, tunneling tooling, and other payloads. "The toolkit comprises a purpose-built reconnaissance pipeline, eleven distinct exploit chains, two tunneling tools, and four C2/RAT/malware families, including a verified SNOWLIGHT instance," the cybersecurity company said . "These components were primarily assembled using public GitHub proof-of-concepts, alongside one pirated commercial C2 produ
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Flags Langflow RCE, Tomcat, and N-central Flaws as Actively Exploited
  - Published: 2026-08-05T07:40:39+00:00
  - Link: https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on August 5, 2026, added three flaws to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation in the wild. The list of vulnerabilities is as follows - CVE-2026-9198 (CVSS score: 9.8) - A code injection vulnerability in Langflow that allows unauthenticated attackers to achieve full remote

### Cluster 61004037ea — score 27

- Title: Compromised keyv Maintainer Account Triggers Massive npm Supply Chain Attack
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-08-05T14:13:47+00:00
- Link: https://orca.security/resources/blog/compromised-keyv-npm-supply-chain-attack/
- Fetch status: ok
- Member count: 20
- Corroborating source count: 14
- Strong signals: GitHub, TeamPCP, npm

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass, phishing_social_eng, supply_chain
- actor_attribution: TeamPCP
- affected_industries: financial_services
- affected_products: AWS, Anthropic/Claude, Apple iOS/macOS, GitHub, Kubernetes, npm
- content_type: incident_report, news_report
- confidence_tier: tier_1_government, tier_1_primary_research, tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- actor_attribution: TeamPCP
- affected_industries: financial_services
- affected_products: npm, GitHub, Kubernetes
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Summary

```
A compromised GitHub maintainer account was used to publish malicious versions of 10 widely-used npm packages in the keyv and cacheable ecosystem, collectively downloaded over 619 million times per month. The attack, attributed to the TeamPCP threat group, deployed a descendant of the “Mini” Shai-Hulud malware family that harvests cloud credentials, GitHub tokens, SSH keys, […]
```

#### Full body

```
Table of contents Technical Overview Affected Systems Risk Impact How Orca Can Help A compromised GitHub maintainer account was used to publish malicious versions of 10 widely-used npm packages in the keyv and cacheable ecosystem, collectively downloaded over 619 million times per month. The attack, attributed to the TeamPCP threat group, deployed a descendant of the “Mini” Shai-Hulud malware family that harvests cloud credentials, GitHub tokens, SSH keys, and CI/CD secrets from developer workstations and build environments. A worm-like self-propagation mechanism has extended the blast radius to over 868 additional packages totaling more than 2 billion monthly installs. Technical Overview On August 4, 2026, attackers gained control of the GitHub account behind keyv, one of the most depended-upon packages in the npm ecosystem. The attacker pushed malicious files (setup.mjs and Math_Symbol.js) directly to the main branch and immediately cut new releases. Because the releases were built through the compromised account’s GitHub Actions workflows, the poisoned versions were published to npm with valid provenance signatures, bypassing standard supply chain integrity checks . The malware operates as a two-stage dropper. A preinstall hook executes setup.mjs, which downloads the Bun JavaScript runtime to run the obfuscated Math_Symbol.js payload (728 KB). Once executed, the payload harvests sensitive credentials and configuration from the host system, including: npm registry authentication tokens from .npmrc GitHub CLI tokens (classic PATs, session tokens, OIDC tokens) AWS access keys and session tokens from ~/.aws/credentials HashiCorp Vault client tokens SSH keys Kubernetes and Terraform configurations AI configuration files (Claude Code, VS Code, Codex) Cryptocurrency wallets Cloud environment metadata and CI/CD secrets Stolen data is encrypted and exfiltrated to GitHub repositories created under compromised identities. Affected Systems The following primary packages are affected: keyv (6.0.0), cacheable, cache-manager (7.2.10), cacheable-request (13.0.20), flat-cache, file-entry-cache, @cacheable/node-cache, @cacheable/memory, @cacheable/utils (2.5.1), and ecto. These packages underpin caching infrastructure across the JavaScript ecosystem and are used by millions of applications, build pipelines, and CI/CD environments worldwide. The attack includes a worm-like self-propagation mechanism: any maintainer who installed a compromised package had their npm tokens stolen, which the attacker then used to publish poisoned versions of that maintainer’s own packages. This resulted in at least 868 additional packages (1,381 versions) being compromised, including packages from organizations such as Deliveroo, Picsart, Qlik, Ornikar, and HubSync. Risk Impact Any developer, build system, or CI/CD runner that installed or updated any of the affected packages after the malicious versions were published on August 4, 2026 should be treated as potentially compromised. Organizations should take the following steps immediately: Remove affected package versions from all development, build, and CI/CD environments Treat any system that installed a compromised package as potentially breached and rebuild from a clean state Rotate all exposed credentials: cloud provider keys (AWS, Azure, GCP), GitHub tokens, SSH keys, Kubernetes configs, Terraform credentials, npm tokens, and Vault tokens Review cloud and source code environments for unauthorized access Check for file artifacts indicating compromise: /tmp/bun-dl-*/, node_modules/keyv/Math_Symbol.js Block IOC domains: npm-cache[.]com, eth-mainnet.nodereal[.]io, go.getblock[.]io, eth.llamarpc[.]com Enable dependency allowlisting, package integrity verification, and provenance controls At the time of writing, active exploitation is confirmed and ongoing. The worm propagation mechanism means that the number of compromised packages continues to grow. The severity of this incident and the breadth of credential t
```

#### Corroborating sources (14)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Compromised keyv Maintainer Account Triggers Massive npm Supply Chain Attack
  - Published: 2026-08-05T14:13:47+00:00
  - Link: https://orca.security/resources/blog/compromised-keyv-npm-supply-chain-attack/
  - Summary: A compromised GitHub maintainer account was used to publish malicious versions of 10 widely-used npm packages in the keyv and cacheable ecosystem, collectively downloaded over 619 million times per month. The attack, attributed to the TeamPCP threat group, deployed a descendant of the “Mini” Shai-Hulud malware family that harvests cloud credentials, GitHub tokens, SSH keys, […]
- **Microsoft Security Blog** (threat_research_primary)
  - Title: ChainDrop supply chain compromise: Anatomy of a self-propagating worm
  - Published: 2026-08-04T23:46:41+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/
  - Summary: A credential-stealing worm hidden in more than 400 compromised npm packages automatically spread across software ecosystems by republishing malicious updates. This analysis details the attack chain, affected environments, and practical guidance for detection, hunting, and remediation. The post ChainDrop supply chain compromise: Anatomy of a self-propagating worm appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: ChainDrop supply chain compromise: Anatomy of a self-propagating worm
  - Published: 2026-08-04T23:46:41+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/
  - Summary: A credential-stealing worm hidden in more than 400 compromised npm packages automatically spread across software ecosystems by republishing malicious updates. This analysis details the attack chain, affected environments, and practical guidance for detection, hunting, and remediation. The post ChainDrop supply chain compromise: Anatomy of a self-propagating worm appeared first on Microsoft Security Blog .
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Don't Revoke That Token Yet: Inside the keyv/cacheable npm Worm, (Wed, Aug 5th)
  - Published: 2026-08-05T17:56:15+00:00
  - Link: https://isc.sans.edu/diary/rss/33218
  - Summary: When you learn that a compromised package executed on one of your build hosts, muscle memory takes over: revoke the npm token, rotate the GitHub PAT, cycle the cloud keys. That reflex has been correct in almost every supply-chain incident I have worked. In the keyv / cacheable compromise that has been unfolding since yesterday, it is the one thing you should not do first â€” because revoking the stolen token is exactly what arms the payload.
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Amazon identifies North Korean hacker group behind open-source supply chain attacks
  - Published: 2026-07-29T21:00:12+00:00
  - Link: https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/
  - Summary: Amazon is sharing new findings about how a threat actor linked to the Democratic People’s Republic of Korea (DPRK) is targeting open source software libraries, the shared building blocks that companies around the world use to develop applications. Amazon Threat Intelligence has linked several recent compromises of popular Node Package Manager (NPM) libraries to the […]
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: keyv and cacheable npm Package Hijacked in Supply Chain Attack
  - Published: 2026-08-04T11:25:22+00:00
  - Link: https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack
  - Summary: Wiz Research is actively investigating an ongoing software supply chain attack affecting multiple keyv/cacheable npm packages.
- **Kaspersky Securelist** (threat_research_primary)
  - Title: How legitimate cloud platforms enable phishers to bypass MFA
  - Published: 2026-08-04T12:00:12+00:00
  - Link: https://securelist.com/cloud-platforms-in-phishing/120832/
  - Summary: We cover a cloud-based AitM attack scenario leveraging service workers and Ultraviolet, and provide detailed phishing hosting statistics across platforms like Cloudflare Workers, Vercel, Netlify, GitHub Pages, and IPFS.
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Massive supply-chain attack compromises 440 packages under four hours
  - Published: 2026-08-04T22:07:35+00:00
  - Link: https://cyberscoop.com/supply-chain-attack-malware-mini-shai-hulud-teampcp/
  - Summary: Researchers from multiple security firms observed a variant of Mini Shai-Hulud, self-replicating malware linked to TeamPCP, in all the affected packages. The post Massive supply-chain attack compromises 440 packages under four hours appeared first on CyberScoop .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Leaked n8n API Tokens Exposed Live Instances to Credential Theft
  - Published: 2026-08-05T10:35:29+00:00
  - Link: https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
  - Summary: GitGuardian researchers found 321 n8n instances accepting API tokens exposed in public GitHub commits and demonstrated four ways attackers could use them to access sensitive data and downstream credentials without exploiting a software vulnerability. We scanned public GitHub commits for exposed n8n API tokens and identified 4,576 unique credentials associated with 1,255 hostnames. Of the 896
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Over 400 NPM Packages Infected in ChainDrop Supply Chain Attack
  - Published: 2026-08-05T08:56:58+00:00
  - Link: https://www.securityweek.com/over-400-npm-packages-infected-in-chaindrop-supply-chain-attack/
  - Summary: The malware was designed to steal and exfiltrate secrets, and to propagate itself via stolen NPM and GitHub credentials. The post Over 400 NPM Packages Infected in ChainDrop Supply Chain Attack appeared first on SecurityWeek .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New XCSSET variant targets macOS devs via compromised Xcode projects
  - Published: 2026-08-04T19:03:09+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-xcsset-variant-targets-macos-devs-via-compromised-xcode-projects/
  - Summary: A new version of the XCSSET malware is targeting thousands of macOS users through compromised Xcode projects and GitHub repositories. [...]
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Worm compromises hundreds of popular npm packages
  - Published: 2026-08-04T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/npm-worm-compromises-popular-npm-packages/
  - Summary: On August 4, 2026, several popular npm packages, including 'keyv', were compromised to deliver malware.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: AWS Blames North Korean Group for Axios and Other npm Supply Chain Attacks
  - Published: 2026-07-31T09:50:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/aws-north-korea-axios-npm-supply/
  - Summary: AWS has linked North Korea to the axios campaign to other attacks on npm libraries
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Anthropic models also did the hacky-hacky
  - Published: 2026-08-03T03:52:50+00:00
  - Link: https://risky.biz/RBNEWS595/
  - Summary: Anthropic models also did the hacky-hacks, Coldcard was hacked for $70 million in Bitcoin, npm adds publish-time malware scanning, and Russia is behind the recent hotel WiFi hacks.

### Cluster 7ef6c747eb — score 23

- Title: CVE-2026-20316 | Cisco Secure Firewall Management Center Static Credential Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-31T21:13:01+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20316/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-20316, Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-20316, CVE-2026-60167, CVE-2026-6516
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-20316, CVE-2026-6516, CVE-2026-60167
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-20316 is a high-severity static credential vulnerability affecting Cisco Secure Firewall Management Center that allows unauthenticated access through a built-in account. NodeZero® Rapid Response safely validates exposure and verifies remediation.
```

#### Full body

```
Cisco Secure Firewall Management Center Static Credential Vulnerability CVE-2026-20316 is a static credential vulnerability affecting Cisco Secure Firewall Management Center (FMC), Cisco’s centralized management platform for Secure Firewall deployments. The vulnerability allows a remote, unauthenticated attacker to authenticate to the FMC web interface using a hard-coded low-privileged account. Cisco has assigned the vulnerability a CVSS score of 8.9 (High) and confirmed active exploitation in the wild. The vulnerability was discovered by Horizon3’s attack research team and has been added to CISA’s Known Exploited Vulnerabilities (KEV) Catalog. Technical Details CVE-2026-20316 is a CWE-259: Use of Hard-coded Password vulnerability in the Cisco Secure Firewall Management Center web interface. The flaw allows a remote, unauthenticated attacker to log in using a built-in static account present on affected systems. While the account provides only low-privileged access, Cisco states that attackers may combine this vulnerability with other Cisco Secure FMC vulnerabilities to elevate privileges and further compromise the management platform. Cisco assigns the vulnerability a CVSS 8.9 (High) score and a Security Impact Rating (SIR) of High because of the risk posed by chaining this vulnerability with additional flaws. The following Cisco products are not affected: Cloud-Delivered Firewall Management Center (cdFMC) Firewall Device Manager (FDM) Secure Firewall ASA Software Secure Firewall Threat Defense (FTD) Software Security Cloud Control (SCC) Cisco has confirmed active exploitation. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this vulnerability can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate evidence of exposure. Run the Rapid Response test: Launch the test from the NodeZero platform to determine whether affected Cisco Secure Firewall Management Center instances are vulnerable. Patch immediately: Apply the Cisco hot fix for your software release. Re-run the test: Confirm the vulnerability is no longer exploitable after remediation. Indicators of Compromise Cisco recommends checking affected appliances for evidence of compromise. Indicator Type Description Command cat /var/log/messages | grep license File If /var/tmp/license.tmp appears in the output, contact Cisco TAC and rotate all credentials, keys, and certificates stored on the affected FMC appliance. Affected Versions & Patch Affected 7.0.0–7.0.9 7.2.0–7.2.11 7.3.0–7.3.1.2 7.4.0–7.4.7 7.6.0–7.6.5 7.7.0–7.7.12 10.0.0–10.0.1 Fixed Cisco has released hot fixes for each affected software branch through Cisco Software Center. Mitigations There are no workarounds. Organizations should immediately install the appropriate hot fix and investigate any indicators of compromise. If compromise is suspected, Cisco recommends rotating all credentials, certificates, and keys managed by the affected FMC appliance. Timeline July 30, 2026: Cisco published its security advisory for CVE-2026-20316 and released hot fixes for affected Cisco Secure Firewall Management Center software. July 30, 2026: Cisco confirmed active exploitation of the vulnerability. July 30, 2026: CISA added CVE-2026-20316 to the Known Exploited Vulnerabilities (KEV) Catalog with an August 1, 2026 remediation deadline for Federal Civilian Executive Branch agencies. July 30, 2026: Horizon3 released a NodeZero Rapid Response test. References Cisco Security Advisory CISA Known Exploited Vulnerabilities Catalog CVE.org Record – CVE-2026-20316 NIST National Vulnerability Database – CVE-2026-20316 Read about other CVEs CVE-2026-6516 CVE-2026-6516 is a critical pre-authentication vulnerability affecting ManageEngine ADAudit Plus. Learn how to validate exposure and verify remediation with NodeZero… Read more CVE-2026-60167, CVE
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-20316 | Cisco Secure Firewall Management Center Static Credential Vulnerability
  - Published: 2026-07-31T21:13:01+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20316/
  - Summary: CVE-2026-20316 is a high-severity static credential vulnerability affecting Cisco Secure Firewall Management Center that allows unauthenticated access through a built-in account. NodeZero® Rapid Response safely validates exposure and verifies remediation.

### Cluster 974cdece8d — score 23

- Title: This month in security with Tony Anscombe – July 2026 edition
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-07-31T14:14:15+00:00
- Link: https://www.welivesecurity.com/en/videos/month-security-tony-anscombe-july-2026/
- Fetch status: ok
- Member count: 12
- Corroborating source count: 10
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion, supply_chain
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: incident_report, news_report
- confidence_tier: tier_1_government, tier_1_primary_research, tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
OpenAI models going rogue, the first documented agentic ransomware operation, and an emergent AI-driven supply chain threat made for a packed July roundup
```

#### Full body

```
Video This month in security with Tony Anscombe – July 2026 edition OpenAI models going rogue, the first documented agentic ransomware operation, and an emergent AI-driven supply chain threat made for a packed July roundup Editor 31 Jul 2026 With July coming to a close, ESET Chief Security Evangelist Tony Anscombe looks back at some of the top cybersecurity stories that made the news over the past month and offers insights that they may hold for your own cyber-defenses. Here's some of what caught Tony's attention this month: OpenAI models went rogue and autonomously broke into AI collaboration platform Hugging Face in what OpenAI described as "an unprecedented cyber incident". Researchers at Sysdig have documented what they assess to be the first case of an end-to-end ransomware operation executed by an agentic threat actor. The company named it JADEPUFFER . Cybercriminals are taking advantage of a new large language model (LLM)-driven attack vector called " phantom squatting " by purchasing domains linked to legitimate brands, then using them to intercept traffic directed there by AI systems. What can organizations do to stop phantom squatting from harming their brands, and what other lessons do these incidents hold for defenders? Watch Tony's video to find out and be sure to check out the June 2026 edition of his monthly security news roundup for more insights. Before you go, learn about the first AI-powered ransomware, named PromptLock and discovered by ESET researchers last year. To learn more about cutting-edge AI defense layers, read the AI at ESET white paper. Connect with us on Facebook , X , LinkedIn and Instagram . Let us keep you up to date Sign up for our newsletters Related Articles Video This month in security with Tony Anscombe – June 2026 edition Video This month in security with Tony Anscombe – June 2026 edition Video This month in security with Tony Anscombe – May 2026 edition Video This month in security with Tony Anscombe – May 2026 edition Video This month in security with Tony Anscombe – April 2026 edition Video This month in security with Tony Anscombe – April 2026 edition Similar Articles ESET research First known AI-powered ransomware uncovered by ESET Research ESET research PromptSpy ushers in the era of Android threats using GenAI Share Article Discussion
```

#### Corroborating sources (10)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: This month in security with Tony Anscombe – July 2026 edition
  - Published: 2026-07-31T14:14:15+00:00
  - Link: https://www.welivesecurity.com/en/videos/month-security-tony-anscombe-july-2026/
  - Summary: OpenAI models going rogue, the first documented agentic ransomware operation, and an emergent AI-driven supply chain threat made for a packed July roundup
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Phishing Campaigns Targeting AI Solutions Providers, (Sat, Aug 1st)
  - Published: 2026-08-01T07:22:32+00:00
  - Link: https://isc.sans.edu/diary/rss/33206
  - Summary: Most phishing campaigns rely on the fact that the victim is afraid to loose "something": money, access to information, ... Many brands have been impersonated by campaigns but I spotted some phishing emails that focus on AI services like ChatGPT.
- **Schneier on Security** (practitioner_analysis)
  - Title: More on the OpenAI Agent’s Attack on Hugging Face
  - Published: 2026-08-03T17:02:46+00:00
  - Link: https://www.schneier.com/blog/archives/2026/08/more-on-the-openai-agents-attack-on-hugging-face.html
  - Summary: Hugging Face has published a detailed timeline of the attack. From the summary: The agent was running an internal OpenAI cyber-capability evaluation based on the ExploitGym benchmark, which tasks an AI agent with finding and exploiting software vulnerabilities. OpenAI ran this on its own infrastructure, and the ExploitGym maintainers and their infrastructure had no involvement in the deployment or operation of that evaluation environment. As far as we were able to infer, across the course of being evaluated on this benchmark, the agent inferred that Hugging Face may host that benchmark’s models, datasets, and reference solutions. We believe the entire intrusion was, from the agent’s point of view, an attempt to cheat the evaluation: reach our production systems and steal the test solutions rather than solve the challenge on its own...
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: AI Agents Targeted Real People and Projects During Cybersecurity Tests
  - Published: 2026-08-05T10:33:41+00:00
  - Link: https://www.securityweek.com/ai-security-institute-reports-anthropic-and-openai-models-going-rogue-against-organizations/
  - Summary: AI Security Institute reports Anthropic and OpenAI models going rogue against real people, organizations, and open source projects. The post AI Agents Targeted Real People and Projects During Cybersecurity Tests appeared first on SecurityWeek .
- **Simon Willison** (ai_security_agentic_risk)
  - Title: July 2026 newsletter
  - Published: 2026-08-02T04:12:41+00:00
  - Link: https://simonwillison.net/2026/Aug/2/july-newsletter/#atom-everything
  - Summary: The June edition of my sponsors-only monthly newsletter is out. If you are a sponsor (or if you start a sponsorship now) you can access it here . This month: Accidental cyberattacks by OpenAl and Anthropic models under test GPT-5.6 Sol, Terra, and Luna Claude Opus 5 Kimi K3 and DeepSeek-V4-Flash-0731 Open letters about Al development A fireside chat and a podcast Reigniting my interest in MCP Other model releases My projects What I'm using at the moment Here's a copy of the June newsletter as a preview of what you'll get. Pay $10/month to stay a month ahead of the free copy! Tags: newsletter
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: OpenAI Disrupts Poipet Scam Network Using ChatGPT Across Multiple Fraud Schemes
  - Published: 2026-08-05T18:33:47+00:00
  - Link: https://thehackernews.com/2026/08/openai-disrupts-poipet-scam-network.html
  - Summary: OpenAI said it disrupted a Cambodia-based scam operation that used its generative artificial intelligence (AI) chatbot ChatGPT to facilitate a wide range of investment, romance, gambling, and law enforcement impersonation schemes. To that end, it banned a coordinated network of ChatGPT accounts likely originating from Southeast Asia and operating from the city of Poipet, a region with extensive
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Frontier Models Engage in Unsanctioned Behavior During Testing
  - Published: 2026-08-05T08:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/frontier-models-unsanctioned/
  - Summary: Anthropic and OpenAI models attacked “real people and organizations” during AI Security Institute tests
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: OpenAI, Anthropic AI agents targeted real people and systems in cyber tests
  - Published: 2026-08-04T23:39:59+00:00
  - Link: https://www.bleepingcomputer.com/news/security/openai-anthropic-ai-agents-targeted-real-people-and-systems-in-cyber-tests/
  - Summary: OpenAI and Anthropic have confirmed that their AI models were involved in separate, newly disclosed third-party cybersecurity testing incidents that resulted in a real website being breached and social engineering attacks against people outside the intended testing boundaries. [...]
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: AISI, OpenAI report more ‘unsanctioned’ model hacks
  - Published: 2026-08-04T22:46:25+00:00
  - Link: https://cyberscoop.com/aisi-openai-report-unsanctioned-ai-model-hacks/
  - Summary: Following similar reports by OpenAI and Anthropic, the UK’s top AI testing lab and a private cybersecurity tester say their models exploited parts of the open internet. The post AISI, OpenAI report more ‘unsanctioned’ model hacks appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: OpenAI's Rogue Model Claims More Victims Beyond Hugging Face
  - Published: 2026-07-29T19:48:12+00:00
  - Link: https://www.darkreading.com/application-security/openai-rogue-model-claims-more-victims-beyond-hugging-face
  - Summary: OpenAI's goal-seeking agent compromised a Modal customer environment and others during its sandbox escape.

### Cluster b1e900a5a7 — score 18

- Title: Escaping Linux Sandboxes via PipeWire (CVE-2026-5674)
- Source: Embrace the Red (ai_security_agentic_risk)
- Published: 2026-07-30T16:00:00+00:00
- Link: https://embracethered.com/blog/posts/2026/pipewire-flatpak-linux-sandbox-escape-cve-2026-5674/
- Fetch status: ok
- Member count: 9
- Corroborating source count: 7
- Strong signals: Anthropic/Claude, CVE-2026-5674

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, phishing_social_eng, web_shell_backdoor
- affected_industries: government
- affected_products: Anthropic/Claude
- cve_ids: CVE-2025-60616, CVE-2026-5674
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- affected_products: Anthropic/Claude
- cve_ids: CVE-2026-5674, CVE-2025-60616
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
This post walks through a sandbox escape from a Flatpak application via PipeWire. The vulnerability was discovered using my automated research pipeline with Claude Code and Opus 4.6 back in April 2026. It was an exciting find, as this was the first bug I submitted to Red Hat. Claude Code was also excited finding this: Once discovered, I repro’d it manually to make sure it’s legit and then submitted it to Red Hat.
```

#### Full body

```
This post walks through a sandbox escape from a Flatpak application via PipeWire. The vulnerability was discovered using my automated research pipeline with Claude Code and Opus 4.6 back in April 2026. It was an exciting find, as this was the first bug I submitted to Red Hat. Claude Code was also excited finding this: Once discovered, I repro’d it manually to make sure it’s legit and then submitted it to Red Hat. Let’s dive into it. PipeWire and PulseAudio PipeWire is the default audio server on all modern Linux desktops now. Fedora, Ubuntu 24.04+, Debian 13,… It replaced PulseAudio but maintains backward compatibility. Flatpak apps that need audio request --socket=pulseaudio . At the core, a basic “Hello World” app with standard audio permission breaks out of the sandbox and gets full access to the user’s desktop, files, and credentials. The same attack applies to other Linux sandbox tech that connects a socket to PipeWire (e.g. Docker, etc..). Let’s look at the vulns and exploit. The Vulnerabilities The escape relies on three separate issues. 1. Authentication Cookie Is Never Validated PulseAudio code contains cookie-based authentication. This is not a typical web cookie, just a name for an authentication token. It’s a 256-byte random value that lives at ~/.config/pulse/cookie , and clients must present it to connect. PipeWire reads the cookie from the client, checks the length is 256 bytes, and then just… throws it away. The relevant code in pulse-server.c : if (len != NATIVE_COOKIE_LENGTH) return -EINVAL; client->version = version; client->authenticated = true; // cookie value never compared The cookie variable is never referenced again after being read. Any 256 bytes of garbage will do. No comments in the code explain why the value is set to true . The original PulseAudio validates the cookie, however PipeWire does not. I looked through the git history. This has been the behavior since the PulseAudio compatibility layer was first implemented. 2. Module Loading Is Enabled by Default #define DEFAULT_ALLOW_MODULE_LOADING "true" Any “authenticated” client can send LOAD_MODULE to load arbitrary PipeWire modules. A config option ( pulse.allow-module-loading ) was added in May 2024, but it defaults to true . Since authentication is broken, this means any process with socket access can load modules. 3. dlopen() With No Path Validation When module-ladspa-sink is loaded, it takes a plugin= parameter and calls dlopen() on it directly: handle = dlopen (path, RTLD_NOW); There is no path validation or directory allowlist. So, we can load arbitrary libraries. ELF constructors ( __attribute__((constructor)) ) run immediately on dlopen() . This is the same pattern as CVE-2025-60616 in FFmpeg’s LADSPA loader. Oh, and if you are wondering what LADSPA means, it stands for Linux Audio Developer's Simple Plugin API . That’s something new I learned along the way. The Sandbox Escape Flatpak’s --socket=pulseaudio grants access to the PulseAudio socket. Combined with any host-writable path (like --filesystem=/tmp in the demo), an app can escape the sandbox. The exploit chain: Write a malicious .so to a host-visible path (e.g. /tmp ) Connect to the PulseAudio socket Send PA_COMMAND_AUTH with 256 bytes of garbage Send PA_COMMAND_LOAD_MODULE module-ladspa-sink plugin=/tmp/payload.so PipeWire, running outside the sandbox , calls dlopen() on the .so The constructor executes in the user’s full context (outside the sandbox) The app has no home directory access, no display access, no network. Yet after the exploit it can read your files, launch apps on your desktop, and access your credentials. Note that PipeWire runs as a user-level service, not root. This is a sandbox escape, not privilege escalation. But the attacker goes from “sandboxed, can only play audio” to “full, unrestricted user context.” Proof of Concept I built a Flatpak app called net.wuzzi.Hello that demonstrates this. It looks completely harmless: $ flatpak info --show-permissions net.wuzz
```

#### Corroborating sources (7)

- **Embrace the Red** (ai_security_agentic_risk)
  - Title: Escaping Linux Sandboxes via PipeWire (CVE-2026-5674)
  - Published: 2026-07-30T16:00:00+00:00
  - Link: https://embracethered.com/blog/posts/2026/pipewire-flatpak-linux-sandbox-escape-cve-2026-5674/
  - Summary: This post walks through a sandbox escape from a Flatpak application via PipeWire. The vulnerability was discovered using my automated research pipeline with Claude Code and Opus 4.6 back in April 2026. It was an exciting find, as this was the first bug I submitted to Red Hat. Claude Code was also excited finding this: Once discovered, I repro’d it manually to make sure it’s legit and then submitted it to Red Hat.
- **The Record** (cyber_news_breach_reporting)
  - Title: Anthropic AI agent faked identities, phished real developers in UK government hacking test
  - Published: 2026-08-05T13:00:00+00:00
  - Link: https://therecord.media/anthropic-ai-hacking-uk
  - Summary: An artificial intelligence agent built by Anthropic independently planted malicious code in a real software project and sent phishing emails to developers during a U.K. government security evaluation, according to Britain’s AI Security Institute.
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Open letters about AI development
  - Published: 2026-08-02T04:16:52+00:00
  - Link: https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything
  - Summary: Open letters about AI development I wrote this summary of the past few weeks of open letters as a section of my sponsors-only newsletter but I've decided to share it here as well. Open Weights and American AI Leadership was shepherded by Microsoft, dated July 24th, and signed by 235 AI-adjacent companies including NVIDIA (see Jensen's first ever tweet ), Amazon, Y Combinator, The Linux Foundation, and (a later signer) OpenAI. It's clearly an argument designed to counter any instincts by the current US government to ban or limit open weight models over "safety" concerns - a reasonable consideration given what happened to Claude Fable 5 ! Relying solely on closed models is not inherently safe: they can be breached, misused, or fail in ways that outsiders cannot detect. And concentrating advanced AI capabilities behind a small number of closed models compounds that risk. It results in a small number of single points of failure, weakens competition, and leaves critical technology in the ha
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Claude Mythos 5 Tried to Backdoor a Real Open-Source Project in Testing, Then Vouched for Itself
  - Published: 2026-08-05T07:53:50+00:00
  - Link: https://thehackernews.com/2026/08/claude-mythos-5-tried-to-backdoor-real.html
  - Summary: An agent running Anthropic's Claude Mythos 5 spent 34 hours trying to get a malware dropper merged into a real open-source project during a cyber evaluation by the UK's AI Security Institute. When a bystander publicly warned that the code was malicious, the agent denied it, force-pushed a rewritten branch history to erase the evidence, and posted from a second account it controlled to vouch for
- **Schneier on Security** (practitioner_analysis)
  - Title: Anthropic’s Opus 5 Is Better at Resisting Prompt Injection
  - Published: 2026-07-31T17:23:16+00:00
  - Link: https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html
  - Summary: The chart is interesting. On the IPI benchmark, Opus 5 improved over Opus 4.8, reducing the probability of an attacker succeeding within 15 attempts from 5.5% to 2.0%, and from 0.5% to 0.2% on 1 attempt. It also improved on Sonnet 5 (5.9% at k=15) and Mythos 5 (2.6%), making it the most robust model evaluated. Opus 5 also outperformed all non-Claude models on this benchmark. The most robust non-Claude model was Muse Spark at 16.5% within 15 attempts—more than eight times Opus 5’s rate. The most capable GPT 5.6 variant, Sol, was comparable to its predecessor GPT 5.5 (20.0% versus 20.8% within 15 attempts), and was 10 times as likely to be successfully attacked as Claude Opus 5 at 2.0%. The other GPT 5.6 variants are less robust, at 30.4% (Terra) and 43.9% (Luna). A single attempt against GPT 5.6 Sol succeeded 3.1% of the time, higher than the 2.0% an attacker achieved against Opus 5 after fifteen attempts...
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Anthropic: Claude Attacks Result of Security Gaps, Not Model Issues
  - Published: 2026-08-03T20:31:12+00:00
  - Link: https://www.darkreading.com/cyber-risk/anthropic-ai-issues-result-security-gaps
  - Summary: Last month's incidents in which the AI model breached real-world systems derived from over-permissioning, especially with Internet access.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Anthropic Reveals Claude Escaped Testing, Breaching Three Companies
  - Published: 2026-07-31T08:35:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/anthropic-claude-breached-three/
  - Summary: Anthropic has revealed that Claude AI models compromised third-party organizations

### Cluster ff79c00af4 — score 18

- Title: From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-08-05T15:48:39+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 5
- Strong signals: Apple iOS/macOS

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_industries: financial_services
- affected_products: AWS, Apple iOS/macOS
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
A macOS ClickFix campaign shifted tactics from openly serving infostealer lures to hiding them behind a browser-fingerprinting gate. The change makes malicious infrastructure harder to detect while giving defenders new hunting opportunities. The post From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags ClickFix Content types Research Products and services Microsoft Defender Topics Actionable threat insights Threat intelligence Microsoft Threat Intelligence observed a macOS ClickFix campaign distributing infostealers, including MacSync and Atomic Stealer (AMOS) , through a large cluster of look-alike domains. The campaign evolved from broadly serving ClickFix lures to using a server-side browser-fingerprinting gate that shows the lure primarily to visitors whose environment appears consistent with a genuine macOS browser. This cloaking limits visibility for crawlers, sandboxes, and some automated analysis workflows. The blog details the domain pattern, fingerprinting checks, infection chain, detection coverage, and hunting pivots that defenders can use to identify related activity. Activity overview Microsoft Threat Intelligence has been tracking a macOS ClickFix operation that distributes information-stealing malware through a large family of algorithmically named domains. Over several weeks of monitoring, Microsoft observed a notable shift in tradecraft: the same infrastructure moved from openly serving the malicious command in the served page’s HTML source to concealing the lure behind a server-side fingerprinting gate that reveals the payload only to visitors the server assesses as a genuine macOS target. The chain ultimately delivers information stealers such as MacSync or Atomic Stealer (AMOS). This activity is consistent with the broader shift in macOS ClickFix tradecraft that Microsoft Threat Intelligence previously documented , in which threat actors instruct users to run Terminal commands that retrieve remotely hosted content rather than the traditional approach of delivering a disk image for manual installation. The cluster described here is notable for two reasons: its domains are mass-produced by a recognizable name generator, and it adopted server-side cloaking on existing infrastructure, giving defenders a clear before-and-after view of the same operation. In this blog, we describe the campaign’s domain-generation pattern, the two delivery phases we observed, the fingerprinting gate that now fronts the infrastructure, and the end-to-end infection chain. We also provide hunting guidance, mitigation recommendations, and defanged indicators of compromise. How ClickFix works ClickFix is a social-engineering technique where attackers persuade users to copy and run a command in Terminal instead of downloading a traditional macOS application. The lure usually appears as a fake verification step, software update, download error, or CAPTCHA, with the command disguised as something required to complete the action. Because execution starts from a user-run Terminal command rather than a downloaded app bundle, the flow can avoid parts of the normal macOS application trust path, including quarantine handling, code-signing evaluation, and notarization checks typically applied to downloaded applications. In this campaign, ClickFix remains the delivery mechanism, but the important change is that the lure is no longer shown to every visitor. The page first profiles the visitor through a browser-fingerprinting gate and primarily requests consistent with a genuine macOS browser environment receive the fake “Download for macOS” page and copied Terminal command. Figure 1a – The counterfeit “Download for macOS” page served to a qualifying visitor by a cloaked gate (apricotfilepoint[.]com). The page displays a forged “Verified Publisher” badge and offers a one-click Copy of an obfuscated curl one-liner. Delivery is conditional. During analysis, the same URLs returned different content to different requests. In some case the macOS ClickFix lure, and in others an apparently benign decoy page. In our testing, a request presenting a Windows browser received a decoy page such as a fake browser-extension or VPN landing page (Figure 1b) or a page impersonating an unrelated business such as a logistics and
```

#### Corroborating sources (5)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide
  - Published: 2026-08-05T15:48:39+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/
  - Summary: A macOS ClickFix campaign shifted tactics from openly serving infostealer lures to hiding them behind a browser-fingerprinting gate. The change makes malicious infrastructure harder to detect while giving defenders new hunting opportunities. The post From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide
  - Published: 2026-08-05T15:48:39+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/
  - Summary: A macOS ClickFix campaign shifted tactics from openly serving infostealer lures to hiding them behind a browser-fingerprinting gate. The change makes malicious infrastructure harder to detect while giving defenders new hunting opportunities. The post From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide appeared first on Microsoft Security Blog .
- **Unit 42** (threat_research_primary)
  - Title: The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version
  - Published: 2026-07-31T10:00:18+00:00
  - Link: https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/
  - Summary: Analysis of XCSSET v40 reveals a macOS malware targeting developers via Xcode. Unit 42 used advanced pattern matching and AI to decode its logic. The post The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version appeared first on Unit 42 .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Chinese Threat Actor Uses Leaked DarkSword Kit to Deploy GHOSTBLADE on iOS
  - Published: 2026-08-03T10:49:06+00:00
  - Link: https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
  - Summary: An unknown Chinese-speaking threat actor has been observed running a campaign targeting Apple iOS devices by leveraging a publicly leaked version of the DarkSword exploit kit. Attack surface management platform Censys said it identified the threat actor running more than 100 web properties, most of which are fake Amazon Web Services (AWS) sign-in pages on a domain that also hosts the exploit
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New DOUBLECUP ClickFix service hides malware in browser cache images
  - Published: 2026-08-03T20:01:22+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-doublecup-clickfix-service-hides-malware-in-browser-cache-images/
  - Summary: A new Russian loader-as-a-service named DOUBLECUP uses ClickFix attacks to hide malicious code in PNG images cached by victims' browsers, ultimately delivering CountLoader to Windows and macOS devices and a new remote access trojan named DeviceManager to Windows systems. [...]

### Cluster 213b4e62b3 — score 17

- Title: CISA warns of hackers exploiting Langflow, N-central, Apache Tomcat flaws
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-05T15:51:33+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-langflow-n-central-apache-tomcat-flaws/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- affected_industries: government
- affected_products: Microsoft SharePoint
- cve_ids: CVE-2026-0770, CVE-2026-18576, CVE-2026-29146, CVE-2026-34486, CVE-2026-9198
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- affected_industries: government
- affected_products: Microsoft SharePoint
- cve_ids: CVE-2026-9198, CVE-2026-0770, CVE-2026-18576, CVE-2026-34486, CVE-2026-29146
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency is giving federal agencies three days to mitigate vulnerabilities in IBM Langflow, N-central, and Apache Tomcat, all actively exploited. [...]
```

#### Full body

```
CISA warns of hackers exploiting Langflow, N-central, Apache Tomcat flaws By Ionut Ilascu August 5, 2026 11:51 AM 1 The U.S. Cybersecurity and Infrastructure Security Agency is giving federal agencies three days to mitigate vulnerabilities in IBM Langflow, N-central, and Apache Tomcat, all actively exploited. ​Tracked as CVE-2026-9198, the security issue in IBM’s Langflow visual framework for building AI agents is the most severe, with a critical rating of 9.8 out of 10. It allows an unauthenticated attacker to execute remotely on default Langflow deployments by chaining two API endpoints to bypass login and run code. In late July, multiple fully functional proof-of-concept (PoC) exploits for CVE-2026-9198 emerged in the public space, with complete instructions on how they can be leveraged. Two weeks ago, CISA issued an alert for another critical Langflow vulnerability (CVE-2026-0770) being exploited in attacks to gain remote code execution with root privileges. The vulnerability in N-able’s remote monitoring and management platform N-central is identified as CVE-2026-18576 and allows attackers to hijack administrative accounts without authentication. The flaw received a high-severity rating and has been patched by the vendor. However, the fix was insufficient, and threat actors found a new way to exploit it. N-able warned customers on August 1st that hackers were actively exploiting the new vulnerability , which received the identifier CVE-2026-18576. An emergency hotfix was released on Sunday. The company urged customers to install it as the flaw impacted all versions of N-central before 2026.3. The Apache Tomcat vulnerability, tracked as CVE-2026-34486 , has a high-severity score of 7.5. It stems from an incomplete fix for CVE-2026-29146, a critical vulnerability with a severity rating of 9.8 that is described as the missing encryption of sensitive data. On July 30, researchers at Palo Alto Networks Unit 42 reported that a Chinese-speaking threat actor tried to exploit the CVE-2026-34486 vulnerability in a manual campaign to plant reverse shells on nine Apache Tomcat servers. CISA confirmed that threat actors are leveraging all three flaws in attacks and added them to its catalog of Known Exploited Vulnerabilities (KEV). However, the agency did not share what types of attacks are leveraging them, noting that it is unknown if they are used in ransomware campaigns. CISA has ordered federal agencies to apply available mitigations for the three targeted products by the end of Friday, July 7th. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: CISA orders urgent action on actively exploited Langflow RCE flaw Critical Langflow RCE flaw exploited to hack AI app servers CISA: Microsoft SharePoint RCE flaw now actively exploited CISA sets urgent deadline to fix Cisco flaw exploited in attacks CISA orders feds to patch max severity Joomla plugin flaw by Friday
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA warns of hackers exploiting Langflow, N-central, Apache Tomcat flaws
  - Published: 2026-08-05T15:51:33+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-langflow-n-central-apache-tomcat-flaws/
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency is giving federal agencies three days to mitigate vulnerabilities in IBM Langflow, N-central, and Apache Tomcat, all actively exploited. [...]

### Cluster 854ba4d3df — score 14

- Title: Dealing with AI-Generated Extortion
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-30T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/ai-generated-extortion
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Combat AI-generated extortion and fake ransomware leaks. Learn how organizations can verify data authenticity using robust governance and threat intelligence.
```

#### Full body

```
Dealing with AI-Generated Extortion Proving a Negative How do you prove a negative in cybersecurity? How do you prove that you weren’t attacked, or that there is no intruder in your network? These are questions that security teams have been forced to ask for a while, but there is a new question that is becoming increasingly common: How do you prove that files weren’t stolen from your network? Or, even more of a challenge, how do you prove that files weren’t stolen from your partners, vendors, or their partners or vendors? This is a surprisingly challenging question to answer. Finding the answer is also more difficult because data governance has not been the traditional purview of security teams. Data governance has long been thought of as a compliance problem, unfortunately that is no longer the case. Security teams are now, whether they want to be or not, need to consider data governance. This means they have to be able to confidently say whether leaked data is real or not. How do you do that? History of Ransomware What we call ransomware has evolved over the years. Ransomware has gone from largely focused on encryption to a combination of encryption and data theft to today’s reality where data theft alone is the most common version of a “ransomware” attack. Threat actors have figured out that managing encryption keys is challenging, stealing data and holding it hostage is significantly easier. They’ve also figured out that stealing the right data can be just as profitable as encryption and, as we’ve seen from ransomware trends, switching to data theft only allows groups to accelerate the number of attacks. Compare the number of victims from 2024 to 2025 in the Recorded Future® Ransomware dashboard with a noticeable rise in ransomware trends. Figure 1: Rise in ransomware trends increasing from 2024 to 2025 (Source: Recorded Future) Enter 0APT If data theft is easier than encryption, then just making up data using generative AI is even easier than that. Which is what we saw with “0APT” (their name, not a designation that Recorded Future provided), who created a list of victims that were completely made up, including fake leaked data. From Insikt Group® reporting at the time: In late January 2026, Insikt Group reported the launch of 0APT Blog, an extortion blog operated by 0APT Ransomware Group, which allegedly runs an affiliate program via its ransomware-as-a-service (RaaS) model. As of February 5, 2026, the extortion blog listed 61 breached victims, with operators stating they planned to leak an additional 115 victims located in multiple countries and operating across various sectors and industries. Insikt Group identified multiple reports regarding the functionality of 0APT ransomware and listed victims, indicating that the ransomware is fake and that all their victims listed on the blog were AI-generated. Among the primary reasons discussed include: Multiple uploaded files were empty. Low-programming practices, including a combination of AI-generated scripts and unprofessional web development. Source code analysis found that some comments were in Hindi and Urdu, which likely indicates that the operators of 0APT ransomware are based in Southern Asia, while the majority of top-tier ransomware groups primarily operate from Russia or a nation within the Commonwealth of Independent States (CIS). Such a large number of victims compromised within a very short period can be carried out by a well-established, organized ransomware group; however, 0APT Blog states that the threat group is currently recruiting penetration testers with network access to join their RaaS affiliate program. 0APT is not alone; other groups are starting to latch on to this trend (ransomware groups are really good at copying each other). ALP-001 is another threat group that surfaced in March with questionable data that may have been AI-generated. According to Reliaquest reporting at the time: The main significance of 0APT and ALP-001 is not that they’re estab
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Dealing with AI-Generated Extortion
  - Published: 2026-07-30T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/ai-generated-extortion
  - Summary: Combat AI-generated extortion and fake ransomware leaks. Learn how organizations can verify data authenticity using robust governance and threat intelligence.

### Cluster c7d4f5e8ea — score 13

- Title: Exploring the Hugging Face Breach: mapping AI agent tactics to Elastic Defend
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-31T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/ai-agent-attack-detection-hugging-face-breach
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: Kubernetes, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: OpenAI/ChatGPT, Kubernetes
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Every stage of the Hugging Face breach maps to Elastic Defend and SIEM rules already shipping, from worker RCE and credential harvest to self-migrating C2 and GenAI detection.
```

#### Full body

```
31 July 2026 • Elastic Security Labs Exploring the Hugging Face Breach: mapping AI agent tactics to Elastic Defend Every stage of the Hugging Face breach maps to Elastic Defend and SIEM rules already shipping, from worker RCE and credential harvest to self-migrating C2 and GenAI detection. 16 min read Detection Engineering , Generative AI Hugging Face reconstructed more than 17,000 attacker events from a July 2026 intrusion driven by an autonomous artificial intelligence (AI) agent. The path was familiar: untrusted dataset content abused a processing worker (file disclosure, then code execution), credential harvest, then multi-cluster lateral movement. Production Elastic Defend behavior rules and Elastic Security detection (SIEM) rules already watch those types of behaviors. This post maps each stage to detections you can enable today. On July 16, 2026, Hugging Face disclosed that a malicious dataset abused its dataset-processing pipeline. A follow-on technical timeline (July 27) clarifies the two vectors against the same config-driven loader in a production Kubernetes worker pod: an HDF5 external raw-storage page that disclosed local files (including environment secrets and worker source), then Jinja2 template injection that achieved code execution. From that foothold, the agent escalated toward node and cluster-level access, harvested cloud and cluster credentials, and moved laterally across roughly July 9-13 UTC (~17,600 reconstructed actions). Hugging Face rebuilt the timeline with its own large language model (LLM) analysis agents after hosted frontier APIs blocked forensic payloads via safety guardrails. On July 21, 2026, OpenAI stated that its evaluation models (including GPT-5.6 Sol and a more capable pre-release model) drove the activity during an internal cyber-capability evaluation on ExploitGym , with reduced cyber refusals enabled for testing. These models identified and exploited a zero-day vulnerability in a package-registry cache proxy, escaped OpenAI’s research environment, reached the open internet, and then targeted Hugging Face while running internal benchmarking of these models on cybersecurity evaluation tasks. Hugging Face reported that the only customer content accessed was ExploitGym/CyberGym challenge solutions in five datasets, with no evidence of tampering with other customer-facing Hub models, datasets, Spaces, or packages. In this post, we: Summarize the July 2026 Hugging Face agentic intrusion and how it intersects with OpenAI's ExploitGym evaluation escape. Map each stage of the campaign to production Elastic Defend behavior rules and Elastic Security detection rules you can enable today. Show why outcome detections (credential paths, unusual destinations, persistence under GenAI parents) beat whole-tool trust of agent or worker process trees. Highlight LLM-based attack-chain triage and GenAI-parented Defend correlation on Elastic Stack 9.3.0+ for agentic alert volume. Key takeaways Elastic Defend behavior rules and Elastic Security detection rules cover multiple stages of this attack chain. Initial access was pipeline abuse on an AI data-processing worker (local file disclosure, then template-injection RCE). Production Defend and SIEM rules that watch workers spawning shells, interpreters, and downloaders still apply. Prefer outcome detections (credential paths, unusual destinations, persistence under GenAI parents) over whole-tool trust of agent or worker process trees. Agentic campaigns spike alert volume. Enable production LLM attack-chain triage and GenAI-parented Defend correlation (Stack 9.3.0+); tune noisy mechanics by lineage and keep credential and egress outcomes hot. Following the lead from the Hugging Face team, we created an interactive view into the incident using Elastic Defend’s technologies, based on publicly available information. You can check it out here: Hugging Face incident interactive timeline Scope note: This post maps behaviors described in public disclosures to Elasti
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Exploring the Hugging Face Breach: mapping AI agent tactics to Elastic Defend
  - Published: 2026-07-31T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/ai-agent-attack-detection-hugging-face-breach
  - Summary: Every stage of the Hugging Face breach maps to Elastic Defend and SIEM rules already shipping, from worker RCE and credential harvest to self-migrating C2 and GenAI detection.

### Cluster edbf0872b0 — score 13

- Title: 10 Best Qualys Alternatives for Cloud Security and Vulnerability Management in 2026
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-08-05T12:50:00+00:00
- Link: https://orca.security/resources/blog/10-best-qualys-alternatives/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Security teams running Qualys today face a widening disconnect between what the platform was built for, traditional network and compliance-driven vulnerability management, and what modern cloud environments demand. This guide covers ten alternatives spanning full cloud-native platforms, direct vulnerability management replacements, and single-module point tools so you can match the right option to the gap […]
```

#### Full body

```
Table of contents Why Do Teams Look for Qualys Alternatives? What Should You Look for in a Qualys Alternative? 1. Orca Security — Best Overall for a Single Agentless Platform Replacing Qualys VMDR, CSPM, and CWPP 2. Wiz — Closest Agentless, Cloud-Native Competitor to Orca 3. Palo Alto Networks (Prisma Cloud / Cortex Cloud) — Broadest Multi-Module Platform Consolidation 4. CrowdStrike Falcon Cloud Security — Best for Teams Already Standardized on Falcon 5. Upwind — Best for Runtime-First Cloud Detection and Response 6. Tenable — Closest Like-for-Like Replacement for Qualys VMDR 7. Rapid7 InsightVM — Best for Teams Wanting VM Plus Automated Remediation Workflows 8. Invicti — Best for Replacing Qualys TotalAppSec (DAST) Specifically 9. Snyk — Best for Shift-Left, Developer-First AppSec Coverage 10. NinjaOne — Best for Replacing Qualys’s Patch Management Module Only How Do You Choose the Right Qualys Alternative for Your Team? Where Orca Fits Frequently Asked Questions about Qualys Alternatives Security teams running Qualys today face a widening disconnect between what the platform was built for, traditional network and compliance-driven vulnerability management, and what modern cloud environments demand. This guide covers ten alternatives spanning full cloud-native platforms, direct vulnerability management replacements, and single-module point tools so you can match the right option to the gap you actually need to close. Why Do Teams Look for Qualys Alternatives? The issue with Qualys isn’t that it doesn’t work. It’s that the platform’s scope and cost structure were designed for a different era of infrastructure, and the gaps show as teams move into elastic, multi-cloud environments. The specific gaps driving teams to evaluate alternatives cluster around three areas: Cost and complexity. Each capability is a separate module to buy and operate, and per-asset pricing makes total cost hard to forecast in autoscaling environments. Deployment and operating model. Qualys spans several scan modes, agentless snapshot, Cloud Agents, network and API scans, and container sensors, so reaching full depth means choosing, deploying, and tuning the right mode per environment. Context over scores. TruRisk ranks findings, but teams increasingly want to know which exposures are reachable and lead to sensitive data, not just which score highest. Understanding the types of cloud security tools available today helps clarify which of these gaps matters most for your environment. What Should You Look for in a Qualys Alternative? Before comparing individual products, establish a consistent evaluation framework. The five criteria below cover the dimensions where Qualys alternatives differ most meaningfully. A team building a mature cloud security program should weigh each based on their current infrastructure mix and operational capacity. Criteria What It Means Agentless vs. agent-based deployment Whether the platform requires installing and maintaining agents on every workload, or can scan infrastructure without persistent software on each asset. Module breadth beyond core VM Coverage across CSPM, CWPP, CIEM, API security, and application security, not just vulnerability scanning. Unified data model vs. bolted-on point tools Whether findings from different security domains feed into a single correlated data model, or exist as separate views stitched together after the fact. Reachability and context Whether the platform scores each finding by what an attacker can reach and whether it leads to sensitive data, rather than static CVSS in isolation. Pricing model and transparency Whether pricing is flat-rate, per-asset, or sales-led/undisclosed, and how predictably costs scale as your environment grows. 1. Orca Security — Best Overall for a Single Agentless Platform Replacing Qualys VMDR, CSPM, and CWPP Orca Security replaces Qualys’s fragmented module stack, VMDR, TotalCloud, WAS, with a single platform built on a Unified Data Model. Where Qualys requires s
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: 10 Best Qualys Alternatives for Cloud Security and Vulnerability Management in 2026
  - Published: 2026-08-05T12:50:00+00:00
  - Link: https://orca.security/resources/blog/10-best-qualys-alternatives/
  - Summary: Security teams running Qualys today face a widening disconnect between what the platform was built for, traditional network and compliance-driven vulnerability management, and what modern cloud environments demand. This guide covers ten alternatives spanning full cloud-native platforms, direct vulnerability management replacements, and single-module point tools so you can match the right option to the gap […]

### Cluster 1af5ed51b6 — score 13

- Title: CISA Warns of Exploited Langflow, N-central, and Tomcat Vulnerabilities
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-05T09:44:50+00:00
- Link: https://www.securityweek.com/cisa-warns-of-exploited-langflow-n-central-and-tomcat-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- affected_industries: financial_services, government, healthcare
- affected_products: Google/Gemini, Palo Alto Networks, SonicWall
- cve_ids: CVE-2026-18556, CVE-2026-18577, CVE-2026-29146, CVE-2026-34486, CVE-2026-9198
- urgency_signals: poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- affected_industries: healthcare, financial_services, government
- affected_products: SonicWall, Google/Gemini, Palo Alto Networks
- cve_ids: CVE-2026-9198, CVE-2026-18556, CVE-2026-18577, CVE-2026-34486, CVE-2026-29146
- urgency_signals: zero_day, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The flaws can be exploited for remote code execution, authentication bypass, and EncryptInterceptor bypass. The post CISA Warns of Exploited Langflow, N-central, and Tomcat Vulnerabilities appeared first on SecurityWeek .
```

#### Full body

```
The US Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday warned that threat actors have been exploiting three vulnerabilities in IBM Langflow OSS, N-able N-central, and Apache Tomcat. Tracked as CVE-2026-9198 (CVSS score of 9.8), the Langflow OSS bug allows unauthenticated attackers to chain two API endpoints for remote code execution. It was disclosed on July 17, when IBM rolled out patches for it, in Langflow OSS version 1.10.1, warning that all default deployments are affected. “The vulnerability combined two distinct issues: an unauthenticated endpoint that issued superuser bearer tokens to any network caller, and a code validation endpoint that executed arbitrary Python code. An attacker could chain these vulnerabilities by first obtaining a superuser token from the auto-login endpoint, then using that token to submit malicious code to the validation endpoint,” IBM warned . Proof-of-concept (PoC) code targeting the security defect was published roughly a week after the public disclosure, and CISA added the CVE to its Known Exploited Vulnerabilities ( KEV ) catalog on August 4. The N-able N-central bug flagged as exploited is tracked as CVE-2026-18556 (CVSS score of 7.4) and described as an authentication bypass. Advertisement. Scroll to continue reading. According to N-able, threat actors exploited the issue as a zero-day to gain administrative access and connect to systems managed through the remote monitoring and management (RMM) platform. The initial fix for CVE-2026-18556 was incomplete, and threat actors bypassed it. As the exploitation activity intensified at the end of July, N-able rolled out a hotfix, issuing CVE-2026-18577 for the patch bypass. Both CVE-2026-18556 and CVE-2026-18577 are now in CISA’s KEV list. Tracked as CVE-2026-34486 (CVSS score of 7.5), the third vulnerability added to the KEV catalog on Tuesday is an EncryptInterceptor bypass in Apache Tomcat that was patched in April. The flaw was introduced in March, with the patch for CVE-2026-29146, a padding oracle issue in EncryptInterceptor, an optional channel interceptor that encrypts messages transmitted between nodes in Tomcat clusters. “The fix moved one line of code. That line turned the encryption layer from fail-closed to fail-open, and opened a direct path to unauthenticated remote code execution on every cluster member,” StrigaAI , which identified the bug, explains. On deployments with EncryptInterceptor configured, only messages encrypted using a shared key should be decrypted and passed to the deserialization layer. Due to the bypass, however, upon failed decryption, the attacker-controlled code was forwarded up the interceptor chain unmodified. Last week, SOCRadar warned that CVE-2026-34486 had been exploited by a Chinese threat actor in attacks involving the Snowlight malware family, while Palo Alto Networks observed the vulnerability being exploited by Chinese hackers in an AI-enabled autonomous hacking campaign. In line with BOD 26-04 requirements, CISA is urging federal agencies to patch all three vulnerabilities by August 7. Related: TP-Link Omada ZTP Vulnerabilities Chain Into Full Network Takeover Related: Gemini Agent-to-Agent Attack Method Exposed Secrets, Enabled Pull Request Tampering Related: Decades-Old BMC Vulnerability Exposes Thousands of Data Centers to Attacks Related: Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Oligo Raises $60 Million for Runtime Security Zenity Raises $125 Million in Series C Funding Gemini Agent-to-Agent Attack Method Exposed Secrets, Enabled Pull Request Tampering Decades-Old BMC Vulnerability Exposes Thousands of Data Centers to Attacks 150,000 Impacted by Madera Community Hospital Data Breach River Bank Says Hac
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: CISA Warns of Exploited Langflow, N-central, and Tomcat Vulnerabilities
  - Published: 2026-08-05T09:44:50+00:00
  - Link: https://www.securityweek.com/cisa-warns-of-exploited-langflow-n-central-and-tomcat-vulnerabilities/
  - Summary: The flaws can be exploited for remote code execution, authentication bypass, and EncryptInterceptor bypass. The post CISA Warns of Exploited Langflow, N-central, and Tomcat Vulnerabilities appeared first on SecurityWeek .

### Cluster 3e123aa6ec — score 12

- Title: Immigration Policy: The Backdoor to Transnational Repression
- Source: Citizen Lab (threat_research_primary)
- Published: 2026-08-05T13:45:26+00:00
- Link: https://citizenlab.ca/immigration-policy-the-backdoor-to-transnational-repression/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Citizen Lab researchers write that restrictive immigration policies are incompatible with attempts to counter transnational repression. The post Immigration Policy: The Backdoor to Transnational Repression appeared first on The Citizen Lab .
```

#### Full body

```
Date Published August 5, 2026 Topics Digital Transnational Repression Law & Policy immigration , transnational repression Mentions Siena Anstis Marcus Michaelsen Kate Pundyk Share Citizen Lab researchers Siena Anstis, Marcus Michaelsen, and Kate Pundyk write for the Foreign Policy Centre that the increasingly restrictive migration policies of democratic countries are incompatible with their claims of countering transnational repression. The authors argue that “host states cannot claim to counter repression across borders while ignoring the role their immigration policies play in enabling it.” Read More in: Digital Transnational Repression LATEST This submission analyzes Bill C-22, the Lawful Access Act, which would enact broad surveillance obligations and reforms in Canada. Issues include: the bill’s sweeping scope, significant constitutional and human rights risks, transparency and accountability deficits, and dangers to encryption and Canada’s cybersecurity. We recommend entirely withdrawing several elements of the bill and suggest amendments to mitigate harms. June 2, 2026 Law & Policy News + Updates → Podcast Kate Robertson on the Risks That Lie Behind Canada’s Unexpected Signing of the UN Cybercrime Convention JULY 31, 2026 research → External Publication How to Combat Transnational Repression JULY 2, 2026 event Confronting Transnational Repression Building Knowledge and Solidarities Across Communities, Civil Society, and Academia JUNE 22, 2026
```

#### Corroborating sources (1)

- **Citizen Lab** (threat_research_primary)
  - Title: Immigration Policy: The Backdoor to Transnational Repression
  - Published: 2026-08-05T13:45:26+00:00
  - Link: https://citizenlab.ca/immigration-policy-the-backdoor-to-transnational-repression/
  - Summary: Citizen Lab researchers write that restrictive immigration policies are incompatible with attempts to counter transnational repression. The post Immigration Policy: The Backdoor to Transnational Repression appeared first on The Citizen Lab .

### Cluster b3d539d300 — score 12

- Title: Can AI do novel security research? Meet the HTTP Terminator
- Source: PortSwigger Research (offensive_vulnerability_research)
- Published: 2026-08-05T19:30:00+00:00
- Link: https://portswigger.net/research/http-terminator
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
Abstract We all know AI can find bugs. After a decade of research, I asked a harder question: can an autonomous system invent new attack techniques, and use them to hack live websites at scale? Buildi
```

#### Full body

```
Can AI do novel security research? Meet the HTTP Terminator James Kettle Director of Research @albinowax Published: Wednesday, 5 August 2026 at 19:30 UTC Updated: Wednesday, 5 August 2026 at 19:33 UTC Abstract We all know AI can find bugs. After a decade of research, I asked a harder question: can an autonomous system invent new attack techniques, and use them to hack live websites at scale? Building this sounded like a bad idea, so I did it. It worked - I'll share an arsenal of new HTTP desync triggers, gadgets, and exploits that compromised banks, security solutions, and government infrastructure. Then I'll trace each discovery chain back through the HTTP Terminator, showing how to turn your personal expertise into an autonomous weapon - and the dark arts required to make it lethal. I'll also share discoveries from beyond the autonomy horizon - some only reachable with a tight human/AI research loop, and others beyond AI's reach entirely. These include a powerful undisclosed recon technique, and anomalies that hint at new attack classes offering alternative paths to critical impact. I'll analyze the discovery process, sharing detailed experiments that probe the boundaries of what AI can and can't discover. You'll leave with new exploits from desync triggers to undisclosed attack classes, and a blueprint for turning your instincts into an autonomous research cascade. And yes, I'll open-source the HTTP Terminator. This whitepaper is also available as a printable PDF . If you've seen the size of the scrollbar and you're about to ask for an AI summary, you may prefer to read the executive summary instead. This research was presented at Black Hat USA 2026 and DEF CON 34 , and this page will be updated with the recording once it's available - follow PortSwigger Research on X , LinkedIn or RSS to get notified when it lands. Contents Introduction Defining novel HTTP desync research HTTP Terminator Design Ideation The technique rediscovery test Scaling ideation with micro-inspiration Evaluation The core evaluation primitive Evaluation case-study Novel desync triggers Weaponization Autonomous RQP Turning the environment into the weapon Making iteration viable The stacked-response problem The dangling-byte technique Cascade Anomaly detection cascade Chasing an autonomous cascade Status-line Injection Range Cache Poisoning Shared-Parser Confusion Scanning for inspiration Conclusion The blueprint Tool releases Defense Takeaways Introduction Automation is often focused on efficiency but I believe that when it's approached just right, automation can enable outcomes that were previously impossible. This research is about chasing that promise of something more. The primary objective of this project was to discover the new frontier of automation-driven security research. I've been practicing automation-driven research for a long time, and could see that generative AI had moved the frontier substantially. I also aimed to build a blueprint to help other researchers quickly adopt this new approach. My secondary objective was to push the "fully autonomous research" concept to complete failure by exceeding the capabilities of current SOTA models. By doing this, I aimed to show where a human in the loop can still add significant value (as opposed to just building the loop, then stepping back). Finally, I aimed to discover factors that make a research topic unsuitable for an AI-driven approach. This would be valuable to people who prefer to stick with a classic, fully-manual research approach and want to minimize the risk of collision with an AI-enhanced researcher. Defining novel HTTP desync research We've all seen experts claiming AI can't do original security research. One of the many risks of my project was that people might claim that the system's discoveries weren't actually original. To minimize this risk I choose the topic I was most qualified for - HTTP Desync Attacks. I repopularized this attack class back in 2019, and in total I've done f
```

#### Corroborating sources (1)

- **PortSwigger Research** (offensive_vulnerability_research)
  - Title: Can AI do novel security research? Meet the HTTP Terminator
  - Published: 2026-08-05T19:30:00+00:00
  - Link: https://portswigger.net/research/http-terminator
  - Summary: Abstract We all know AI can find bugs. After a decade of research, I asked a harder question: can an autonomous system invent new attack techniques, and use them to hack live websites at scale? Buildi

### Cluster 24e0f0f990 — score 12

- Title: A few notes on AWS Nitro Enclaves: KMS integration
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-08-05T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/08/05/a-few-notes-on-aws-nitro-enclaves-kms-integration/
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
Nitro Enclaves and Key Management Service (KMS) feel like a natural fit: since the KMS can verify attestation documents generated by the enclaves, developers can offload key management tasks from their applications to the AWS-managed service. But integrating an external service with your trusted enclaves comes with new threats, even if that service comes from the same provider. In this blog post—the third in our series on Nitro Enclaves, following our posts on attack surface and images and attestation —we catalog passive and active attack classes against the enclave-KMS communication channel, and cover the operational risks that persist even when the cryptography is correct. Intro to KMS The KMS is an AWS service that provides a unified public API for creating and managing keys backed by HSMs to the broader AWS ecosystem. There are three main key types supported by KMS that devs need to care about: Customer-managed keys (CMK) Data keys (DK, symmetric) Data key pairs (asymmetric) CMKs n
```

#### Full body

```
Page content Nitro Enclaves and Key Management Service (KMS) feel like a natural fit: since the KMS can verify attestation documents generated by the enclaves, developers can offload key management tasks from their applications to the AWS-managed service. But integrating an external service with your trusted enclaves comes with new threats, even if that service comes from the same provider. In this blog post—the third in our series on Nitro Enclaves, following our posts on attack surface and images and attestation —we catalog passive and active attack classes against the enclave-KMS communication channel, and cover the operational risks that persist even when the cryptography is correct. Intro to KMS The KMS is an AWS service that provides a unified public API for creating and managing keys backed by HSMs to the broader AWS ecosystem. There are three main key types supported by KMS that devs need to care about: Customer-managed keys (CMK) Data keys (DK, symmetric) Data key pairs (asymmetric) CMKs never leave KMS. You request KMS to perform cryptographic operations (like encryption or signing) for you. Data keys and key pairs are generated in KMS, are not stored in KMS, and are intended for programmatic uses. For symmetric keys, the KMS gives you a plaintext key and the same key encrypted to CMK. Your application performs encryptions, removes the plaintext key, and stores the key encrypted to a CMK along the ciphertexts; this pattern is called envelope encryption . For asymmetric keys, the KMS gives you a plaintext key pair and the private key encrypted to CMK. Your application creates signatures or encrypts data, deletes the private key, and keeps the public key and encrypted private key (along with signatures/ciphertexts). Both types of data keys can be used with Decrypt operation to get plaintext keys again. S t o r a g e s t { o E r _ e d ( k E , _ C d } k , C ) E n c l a v G e e { n d e k C D p r , = e l a E e c a t _ n r i e d c y n D k ( p t a = d t e t e k ( { x a n , c d t K c p m k = e ( l k } d y c a _ e ( m i i c c k n d ( m , t , d k d e E k _ k x _ , i ) t d C d } ) k ) ) ) K M S Figure 1: Basic KMS operations. cmk_id is an ID (ARN) of CMK key, cmk is the actual key used, enc / dec are any encryption/decryption algorithms, GenerateDataKey and Decrypt are KMS operations. Access to keys is subject to authorization policies , including key policies, IAM policies, and grants. Cross-account access for keys can be enabled. Keys can be identified in multiple ways : ARN, Id, Alias ARN, and Alias name. Keys are usually per-region (single-region), but multi-region keys can be created too. Enclave-KMS communication There are two mechanisms that are in play when integrating KMS with Nitro Enclaves: KMS policies restricting access to CMKs to specific enclaves (by PCR values) KMS encrypting responses to enclave’s public keys In the first mechanism, the key policy may authorize access to only requests that contain fresh and correctly signed attestation documents with the expected PCR values. Enclaves have to generate attestations and include them in requests to KMS. Note that the enclave still needs IAM credentials to access KMS in the first place. The second mechanism is about enclaves sending asymmetric public keys (inside the attestation documents) to KMS, and KMS encrypting part of the responses to the key. This mechanism is supposed to ensure that only the requesting enclave can see output from KMS. Only a few KMS operations support these two mechanisms. The operations are: GenerateDataKey , GenerateDataKeyPair Decrypt DeriveSharedSecret GenerateRandom Note the absence of the Encrypt operation: enclaves can request this operation, but without the attestation-based security mechanisms. CMKs cannot be used directly by enclaves for encryption without missing on the attestation checks. This means cryptography operations are supposed to be implemented via data keys, and not directly via CMKs. S t o r a g e s t { o E r _ e d ( k
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: A few notes on AWS Nitro Enclaves: KMS integration
  - Published: 2026-08-05T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/08/05/a-few-notes-on-aws-nitro-enclaves-kms-integration/
  - Summary: Nitro Enclaves and Key Management Service (KMS) feel like a natural fit: since the KMS can verify attestation documents generated by the enclaves, developers can offload key management tasks from their applications to the AWS-managed service. But integrating an external service with your trusted enclaves comes with new threats, even if that service comes from the same provider. In this blog post—the third in our series on Nitro Enclaves, following our posts on attack surface and images and attestation —we catalog passive and active attack classes against the enclave-KMS communication channel, and cover the operational risks that persist even when the cryptography is correct. Intro to KMS The KMS is an AWS service that provides a unified public API for creating and managing keys backed by HSMs to the broader AWS ecosystem. There are three main key types supported by KMS that devs need to care about: Customer-managed keys (CMK) Data keys (DK, symmetric) Data key pairs (asymmetric) CMKs n

### Cluster ad2bf1153f — score 12

- Title: Agentic vulnerability management, end to end: 2,731 findings, one approved fix
- Source: Sysdig (detection_response_operations)
- Published: 2026-08-04T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/agentic-vulnerability-management-end-to-end-2-731-findings-one-approved-fix
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Atlassian Jira

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_products: Anthropic/Claude, Atlassian Jira
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_products: Atlassian Jira, Anthropic/Claude
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
AI agents took a 119,443-finding backlog, traced 2,731 SLA breaches to one base-image fix, and opened a real Jira ticket. A human clicked Approve. That click is the whole autonomy debate, settled in one UI element.
```

#### Full body

```
< back to blog Agentic vulnerability management, end to end: 2,731 findings, one approved fix Published by: Blair Howard @ linkedin GET A DEMO Published: August 4, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more How Sysdig agentic cloud security works TL;DR: In a live Sysdig Secure AI session, agents triaged a 119,443-finding backlog, traced 2,731 SLA-breaching findings to a single base-image fix, and a human approved the resulting Jira ticket, DEJI-342. The same agents run headless in Claude through Sysdig's MCP server . Anyone who has owned a vulnerability program knows the uncomfortable part: The findings were never the problem. Knowing is easy. A scanner will happily hand you six figures of findings by lunchtime. The problem is the distance between knowing and doing: mapping a CVE to the workloads it actually affects, hunting down an owner, opening the ticket, and tracking the SLA. That distance is measured in analyst hours, and analysts are the scarcest resource in the building. That gap was "survivable" when attackers moved at human speed. They don't anymore. The Sysdig Threat Research Team recently documented JADEPUFFER, the first agentic ransomware operation , an extortion campaign driven end to end by an LLM. And our 2026 Cloud-Native Security Report put a number on the shift: Attackers now weaponize disclosed vulnerabilities within hours. The old pain didn't change. The clock did. This is where the agentic model changes the math. Below is a walkthrough of Sysdig Secure AI working on one of the hardest jobs in security, captured from a live environment. If you'd rather watch than read, here's the video version: You set the operating orders Agents don't get free rein. They get goals. Setup starts the way any risk conversation should: Tag your high-value assets, then define SLA windows per severity. In this environment, criticals and highs must be remediated within 30 days. Sysdig Secure AI SLA policy editor Remediation windows per severity. These become the agents' operating orders. Goals become standing plans Secure AI turns those policies into standing plans; in this case, SLA Compliance and Reduce Exposure Time . This is the shift that's easy to miss: The agents aren't working a task list. They're working toward an outcome. That difference is everything. A task queue is something you fill, drain, and refill, and the moment it's empty, the work stops. A plan is a goal the agents pursue continuously, and the goal is yours . It comes from your team's SLAs, your risk tolerance, and your definition of acceptable exposure. You set the purpose, and the agents drive toward it day after day, without anyone reloading the queue. The agent works the metric, not the ticket queue Open the SLA Compliance plan and the agent reports like a colleague. It will tell you things like current value 28.3%, up 2.9 points versus the prior day, with the reasoning written out: what the plan tracks, which findings count toward the metric, and how the queue was ranked. It maintains a ranked list of the jobs that move the metric the most. No analyst had to notice anything for this queue to exist. The verdict: Runtime context, not CVSS guesswork The top-ranked job resolves to a verdict a human can act on: One Node.js image ( node:17.9.1-bullseye ) is carrying 2,731 SLA-breaching findings, 273 of them critical, and the oldest is 90 days past the deadline. A maintained Node 17 base image resolves them. This is runtime insights doing the prioritization rather than a spreadsheet of CVSS scores. This particular plan ranks by the severity of the worst SLA breach and limits itself to findings that already have a published fix, so the queue only contains work your team could ship today. Other plans lean on different runtime signals: Reduce Exposure Time ranks by risk score, findi
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: Agentic vulnerability management, end to end: 2,731 findings, one approved fix
  - Published: 2026-08-04T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/agentic-vulnerability-management-end-to-end-2-731-findings-one-approved-fix
  - Summary: AI agents took a 119,443-finding backlog, traced 2,731 SLA breaches to one base-image fix, and opened a real Jira ticket. A human clicked Approve. That click is the whole autonomy debate, settled in one UI element.

### Cluster 725e4c357a — score 11

- Title: Hype vs. Reality: What the Hugging Face Incident Means for AI Safety
- Source: Recorded Future (threat_research_primary)
- Published: 2026-08-05T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/hugging-face-ai-safety
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, supply_chain, zero_day
- affected_products: OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft, zero_day
- affected_products: OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Discover the security lessons from the recent incident where autonomous AI agents breached Hugging Face infrastructure.
```

#### Full body

```
Hype vs. Reality: What the Hugging Face Incident Means for AI Safety Agentic defense will be essential to countering agentic offense. However, defenders must actively mitigate the risk of autonomous systems operating outside of their expected parameters. In July 2026, OpenAI disclosed that models undergoing an internal cybersecurity evaluation had escaped their testing environment and compromised part of Hugging Face’s production infrastructure. OpenAI characterized the event as an “unprecedented cyber incident.” The incident should put security leaders on alert, but not for the reasons OpenAI suggests. One concern is that OpenAI’s agents demonstrated the ability to autonomously carry out an end-to-end cyberattack, placing the models at the highest level of autonomy within Recorded Future’s AIM3 framework. However, the greater concern is that the model operators did not sufficiently monitor for or prepare to mitigate unauthorized agentic activity. Enterprises using agents for security and other purposes should see the Hugging Face incident as a warning about what happens when agents are set loose without safeguards against adverse outcomes. What Happened The incident began during an OpenAI evaluation designed to measure advanced cyber capabilities. The evaluation involved GPT-5.6 Sol and an even more capable internal research prototype that OpenAI says was not intended for public release. Because the objective was to test their maximum offensive potential, the models were operated with reduced security guardrails (normally used to prevent high-risk activity). According to OpenAI , the models spent substantial computing resources searching for a path to the internet. They exploited a zero-day vulnerability in Artifactory, the package-registry cache proxy available in the evaluation environment, and then performed privilege escalation and lateral movement within OpenAI’s research environment until they reached a node with internet access. Once online, the models inferred that Hugging Face might contain models, datasets, or solutions associated with ExploitGym, the benchmark they had been instructed to solve. OpenAI says the agents then chained stolen credentials, zero-day vulnerabilities, and remote code execution paths to obtain test solutions from a Hugging Face production database. Hugging Face’s technical reconstruction covers roughly 17,600 recovered agent actions, grouped into approximately 6,280 clusters, between July 9 and July 13, 2026. Although most attempts failed, the agent still gained administrative access to internal and production systems, accessed some source-code repositories, and used a stolen credential to connect external systems to the company network. Hugging Face found no evidence that its public models, datasets, services, packages, or published software supply chain were altered. It says the only customer content accessed comprised five datasets, apparently related to ExploitGym or CyberGym. A Capability Breakthrough and a Control Failure Most coverage of this incident has framed it as a breakthrough in model capabilities, since it is the first known instance of a model apparently independently conducting an end-to-end cyberattack. The underlying techniques were largely familiar to those used in human-led cyberattacks: vulnerability exploitation, credential theft, staging, remote code execution, lateral movement, and abuse of privileged or trusted access. What was notable was the agents’ ability to select and chain those steps autonomously across a long-running operation. This represents a significant shift in the speed and scale of future incidents. An autonomous agent can execute thousands of actions, test multiple paths, and continue working without the fatigue, coordination costs, or time constraints that limit human operators. In this case, most of the roughly 17,600 recovered actions were associated with failed paths. The operation was noisy and failure-prone, but it needed only a small number of
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Hype vs. Reality: What the Hugging Face Incident Means for AI Safety
  - Published: 2026-08-05T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/hugging-face-ai-safety
  - Summary: Discover the security lessons from the recent incident where autonomous AI agents breached Hugging Face infrastructure.

### Cluster 94fd56afbc — score 11

- Title: What's new in Elastic Defend: 800+ vulnerable driver rules, automated troubleshooting, and ARM support
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-31T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/vulnerable-driver-detection-elastic-defend-byovd
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Elastic Defend automatically generates and instantly deploys vulnerable driver YARA rules from VirusTotal, LOLDrivers and Microsoft's blocklist, closing the gap BYOVD attacks depend on. Plus a new troubleshooting skill and ARM endpoint protection.
```

#### Full body

```
31 July 2026 • Pedro Jaramillo • Roxana Gheorghe • Mia LaVada What's new in Elastic Defend: 800+ vulnerable driver rules, automated troubleshooting, and ARM support Elastic Defend automatically generates and instantly deploys vulnerable driver YARA rules from VirusTotal, LOLDrivers and Microsoft's blocklist, closing the gap BYOVD attacks depend on. Plus a new troubleshooting skill and ARM endpoint protection. 5 min read Product Updates , Detection Engineering We know you’re tired of hearing how every vendor is going to finally help you solve alert fatigue. Well, one way we’re improving alert fatigue is from a slightly different angle, better prevention at the endpoint. Because stopping more at the endpoint means fewer alerts ever raised. We have three endpoint enhancements, all contributing to better endpoint prevention: To be even more proactive about Bring Your Own Vulnerable Driver (BYOVD) attacks, we’re continuously monitoring public vulnerable driver disclosures and automatically generating endpoint protections To improve your endpoint management efficiency, Automatic Troubleshooting is now available as a skill via Elastic Agent Builder To expand our coverage surface, Elastic Defend is now available for Windows on ARM Let’s dig into each one. What is a BYOVD attack and how does it bypass endpoint protection? BYOVD is a technique attackers use to gain kernel-level access on Windows machines by abusing legitimately signed drivers, letting them bypass defenses meant to block unauthorized code. Windows requires low-level software drivers that run in the kernel to be digitally signed, so rather than trying to sneak in something unsigned, attackers bring a driver that's already signed and trusted, but that has a known security flaw. That flaw is enough to disable security software or tamper with memory, and once an attacker has that level of access, security tools can no longer reliably protect the host. This combination is why BYOVD has become so appealing to ransomware operators. The technique started as tradecraft mostly reserved for advanced state actors and red teams. Elastic Security Labs has tracked its shift into a routine step ransomware crews now use to tamper with or shut down endpoint security software before deploying their payload, as detailed in Stopping Vulnerable Driver Attacks . Now, why does timing matter here? BYOVD attacks have depended on one thing for years: the delay between a vulnerable driver's public disclosure and a vendor shipping coverage for it. The moment a vulnerable driver becomes public knowledge, attackers already know about it. When it takes a vendor an entire product release to ship a protection, that gap is exactly what the technique depends on. To close this gap, Elastic Security Labs Threat Command, Elastic's security research team now continuously monitors public vulnerable driver disclosure sources, including VirusTotal, the LOLDrivers catalog, and Microsoft's Vulnerable Driver Block List, and automatically generates and instantly deploys detection rules. Because we know any delay could be the difference between an exposed endpoint and a secured one, we’ve decoupled this coverage from any release cycle and publish the protections in the open. How Elastic automatically generates vulnerable driver YARA rules Elastic Security Labs has published detection coverage for vulnerable drivers for years. That coverage now runs through an always-on process that adds new drivers to the protections library as they're disclosed. An always- on process means coverage ships continuously, not whenever the next major release happens to land, and it doesn’t require an update or setting change. A driver flagged today becomes a driver Elastic Defend recognizes. Elastic Security Labs Threat Command monitors three public sources for newly disclosed vulnerable and malicious drivers: VirusTotal The community-run LOLDrivers catalog Microsoft's Vulnerable Driver Block List No single source catches everything, so t
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: What's new in Elastic Defend: 800+ vulnerable driver rules, automated troubleshooting, and ARM support
  - Published: 2026-07-31T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/vulnerable-driver-detection-elastic-defend-byovd
  - Summary: Elastic Defend automatically generates and instantly deploys vulnerable driver YARA rules from VirusTotal, LOLDrivers and Microsoft's blocklist, closing the gap BYOVD attacks depend on. Plus a new troubleshooting skill and ARM endpoint protection.

### Cluster f7c0990e5f — score 11

- Title: OpenSSF Community Day Europe 2026: Schedule Highlights & What to Expect
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-07-29T20:03:12+00:00
- Link: https://openssf.org/blog/2026/07/29/openssf-community-day-europe-2026-schedule-highlights-what-to-expect/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government, legal_professional, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government, manufacturing_industrial, legal_professional
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
OpenSSF Community Day Europe 2026 (October 6 in Prague), focuses on open source software security, regulatory compliance like the EU CRA, and AI supply chain risks. The one-day event features technical sessions on tools like VEX, Gemara, and Sigstore, offering direct collaboration with maintainers and security experts.
```

#### Full body

```
By Angelah Liu, Linux Foundation TL;DR: OpenSSF Community Day Europe 2026 (October 6 in Prague), focuses on open source software security, regulatory compliance like the EU CRA, and AI supply chain risks. The one-day event features technical sessions on tools like VEX, Gemara, and Sigstore, offering direct collaboration with maintainers and security experts. Between evolving regulatory mandates like the EU Cyber Resilience Act (CRA) and the rise of AI-driven vulnerabilities, securing open source code has become a baseline requirement for engineering teams, not an afterthought. The official Schedule for OpenSSF Community Day Europe 2026 is now live. Co-located with Open Source Summit Europe in Prague on October 6, 2026, this single-day event brings together open source maintainers, security researchers, enterprise contributors, and policy experts for a full day of technical exchange. Whether you’re looking to harden your CI/CD pipelines, get ahead of upcoming compliance frameworks, or simply talk shop with the maintainers behind the tools you rely on, this year’s schedule has a lot to offer. Session Highlights Keynote: Welcome & Opening Remarks Steve Fernandez, General Manager of OpenSSF at the Linux Foundation, kicks things off at 9:00 CEST with the opening keynote , setting the tone and priorities for the day ahead. EU Regulations & Governance Right after lunch, Roman Zhukov (Red Hat), Daniel Appelquist, Madalin Neag (OpenSSF), and Megan Knight (Arm) take the stage at 13:55 CEST for Operationalizing the CRA and Shaping OpenSSF’s Community Roadmap . The CRA is reshaping how open source projects handle vulnerability management and maintainer liability, and this session is where the legal language turns into something developers can actually build into their workflows. AI Infrastructure & Supply Chain Provenance AI is playing a double role in security right now: an automated tool for finding bugs faster, and a new surface area attackers are learning to exploit. Three sessions dig into that tension from different angles. Jeff Diecks and Laura Guazzelli from OpenSSF open the topic at 10:55 CEST with Preparing for the Vulnpocalypse: Using OSS-CRS To Find and Fix Bugs Before They Find You , covering automated vulnerability discovery at scale. At 11:20 CEST, Dmitry Tantsur (Red Hat) and Tuomo Tanskanen (Ericsson) will shift the focus to infrastructure with Defending Bare-Metal: Lessons Learnt From AI Security Analysis of Metal3 and OpenStack Ironic . And later in the afternoon, at 16:30 CEST, Sheng Sun and Sarah Evans (both of Dell Technologies) tackle the machine learning supply chain itself in Verifiable AI Provenance: Closing the Attestation Gap in the Machine Learning Supply Chain , asking how teams can actually verify what went into a model before it reaches production. Tooling & Supply Chain Standards Good security policy only goes as far as the tooling that puts it into practice. Hannah Braswell (Red Hat) walks through that idea at 11:45 CEST in From First PR To Hardening Guide: Structured Security With Gemara , showing how the Gemara framework brings structure to governance, risk, and compliance work. Later, at 16:50 CEST, Yuta Kiyoumi (Honda Motor Co., Ltd.) and Akihiko Takahashi (Fujitsu) bring a real-world manufacturing lens to the conversation with Applying VEX To Vulnerability Information Sharing in Multi-tier Automotive Supply Chains , showing how Honda uses the Vulnerability Exploitability eXchange (VEX) standard to track risk across hardware and software tiers alike. Community & Interactive Sessions Not everything on the schedule is a deep technical dive. At 15:15 CEST, OpenSSF’s Adrianne Marcum and CRob return with GAME SHOW!! Part Dva!! for a lighter, interactive take on community learning. And closing out the day at 17:10 CEST, Ejiro Oghenekome, Victoria Ottah, Sal Kimmich (OpenUK), CRob (OpenSSF), and Amir Montazery (OSTIF) come together for Securing Africa’s Open Source Ecosystem , a conversation about maintainer
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: OpenSSF Community Day Europe 2026: Schedule Highlights & What to Expect
  - Published: 2026-07-29T20:03:12+00:00
  - Link: https://openssf.org/blog/2026/07/29/openssf-community-day-europe-2026-schedule-highlights-what-to-expect/
  - Summary: OpenSSF Community Day Europe 2026 (October 6 in Prague), focuses on open source software security, regulatory compliance like the EU CRA, and AI supply chain risks. The one-day event features technical sessions on tools like VEX, Gemara, and Sigstore, offering direct collaboration with maintainers and security experts.

### Cluster 2b2ae045a4 — score 11

- Title: Veeam, Terraform MCP, Django Patch Critical Flaws, Led by CVSS 10.0 Cross-Tenant Bug
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-05T14:27:30+00:00
- Link: https://thehackernews.com/2026/08/veeam-terraform-mcp-django-patch.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- cve_ids: CVE-2026-32998, CVE-2026-58067, CVE-2026-58071, CVE-2026-58072, CVE-2026-58073
- urgency_signals: critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos
- cve_ids: CVE-2026-58073, CVE-2026-58072, CVE-2026-58067, CVE-2026-58071, CVE-2026-32998
- urgency_signals: preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
HashiCorp, Veeam, and the Django Software Foundation have patched 11 vulnerabilities across Terraform MCP Server, Veeam Service Provider Console, and Django. The three most serious: An unauthenticated flaw in Veeam's console that hands over a managed agent's credentials, rated 9.5 A cross-tenant flaw in HashiCorp's MCP server that lets one user's Terraform token be reused for later users'
```

#### Full body

```
Veeam, Terraform MCP, Django Patch Critical Flaws, Led by CVSS 10.0 Cross-Tenant Bug  Swati Khandelwal  Aug 05, 2026 Vulnerability / Software Security HashiCorp, Veeam, and the Django Software Foundation have patched 11 vulnerabilities across Terraform MCP Server, Veeam Service Provider Console, and Django. The three most serious: An unauthenticated flaw in Veeam's console that hands over a managed agent's credentials, rated 9.5 A cross-tenant flaw in HashiCorp's MCP server that lets one user's Terraform token be reused for later users' requests, scored a maximum 10.0 on its CVE record A flaw in GeoDjango's spatial lookups that can write a file to disk and, on some setups, run code, reachable by a staff user with view permission on a registered model containing a spatial field Each has a fix available now. Operators should update Terraform MCP Server to version 1.1.0 or later, Veeam Service Provider Console to 9.3.0.35057, and Django to 6.0.8 or 5.2.17. Exposure is configuration-dependent: HashiCorp's bugs affect Streamable HTTP rather than stdio, Veeam's flaws affect version 9 builds before 9.3, and Django's documented admin attack path requires a staff account with view permission for a model containing a spatial field. None of the three advisories says the flaws are under active exploitation, and as of August 5, 2026, none of the eleven CVEs appears in CISA's Known Exploited Vulnerabilities catalog, and no public proof-of-concept has surfaced. Impersonate an agent, take its credentials Veeam Service Provider Console, the multi-tenant console that hosting firms and managed service providers use to run and monitor customer backups, got four fixes in build 9.3.0.35057, detailed in a security bulletin published August 4 . Two are critical. Veeam released the build on July 29. The one to watch is CVE-2026-58073 (CVSS score: 9.5), which lets an unauthenticated attacker impersonate a managed agent and obtain that agent's credentials. Its CVSS vector rates attack complexity as high. The second critical flaw, CVE-2026-58072 (CVSS score: 9.0), is an arbitrary file write on the management server that can lead to remote code execution and requires a low-privilege account. The 9.5 reads as the worst of the two because it needs no login, but its high attack complexity is the reason the vector is not a straight-line exploit; unauthenticated here does not mean easy. Two high-severity bugs round out the set: CVE-2026-58067 , an unauthenticated memory-exhaustion denial of service, and CVE-2026-58071 , which exposes the proxied appliance API as Portal Administrator during a short window after an administrator session begins. All four affect VSPC 9.2.1.33875 and every earlier version 9 build. The fix is the upgrade to 9.3.0.35057. This is the second critical patch cycle for the console in roughly three months. In May, Veeam fixed CVE-2026-32998 , a 9.4-rated remote code execution bug tied to alarm script execution. One tenant's token, reused for the next HashiCorp's Terraform MCP server, which connects AI assistants to Terraform over the Model Context Protocol, carries three related flaws in its Streamable HTTP transport, disclosed July 28 and fixed in version 1.1.0 . HashiCorp released the fixed build on July 14, followed by version 1.2.0 on August 4. Deployments that run only in stdio mode, the local single-user setup, are unaffected. The bugs live in the multi-user HTTP mode meant for centralized, shared deployments, the configuration HashiCorp promoted when it made the server generally available in June . The most severe is CVE-2026-16498 (CVSS score: 10.0), a cross-tenant credential-reuse bug in stateless HTTP mode. The underlying MCP library does not assign unique session identifiers, and the server's credential cache relied on those identifiers to tell users apart. One user's Terraform token could therefore be reused for later users' requests regardless of the token they supplied. The root is an assumption about the layer beneath the
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Veeam, Terraform MCP, Django Patch Critical Flaws, Led by CVSS 10.0 Cross-Tenant Bug
  - Published: 2026-08-05T14:27:30+00:00
  - Link: https://thehackernews.com/2026/08/veeam-terraform-mcp-django-patch.html
  - Summary: HashiCorp, Veeam, and the Django Software Foundation have patched 11 vulnerabilities across Terraform MCP Server, Veeam Service Provider Console, and Django. The three most serious: An unauthenticated flaw in Veeam's console that hands over a managed agent's credentials, rated 9.5 A cross-tenant flaw in HashiCorp's MCP server that lets one user's Terraform token be reused for later users'

### Cluster 1f7c3a3d86 — score 11

- Title: Strategic Attack on Iran: Airpower’s Promises, Limits, and Lessons
- Source: Just Security (policy_strategy_geopolitics)
- Published: 2026-08-05T13:14:58+00:00
- Link: https://www.justsecurity.org/151394/strategic-attack-on-iran-airpowers-promises-limits-and-lessons/?utm_source=rss&utm_medium=rss&utm_campaign=strategic-attack-on-iran-airpowers-promises-limits-and-lessons
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
Operation Epic Fury demonstrates that airpower is both essential and insufficient. A review of what the campaign reveals about airpower's promises, limits and lessons in Iran. The post Strategic Attack on Iran: Airpower’s Promises, Limits, and Lessons appeared first on Just Security .
```

#### Corroborating sources (1)

- **Just Security** (policy_strategy_geopolitics)
  - Title: Strategic Attack on Iran: Airpower’s Promises, Limits, and Lessons
  - Published: 2026-08-05T13:14:58+00:00
  - Link: https://www.justsecurity.org/151394/strategic-attack-on-iran-airpowers-promises-limits-and-lessons/?utm_source=rss&utm_medium=rss&utm_campaign=strategic-attack-on-iran-airpowers-promises-limits-and-lessons
  - Summary: Operation Epic Fury demonstrates that airpower is both essential and insufficient. A review of what the campaign reveals about airpower's promises, limits and lessons in Iran. The post Strategic Attack on Iran: Airpower’s Promises, Limits, and Lessons appeared first on Just Security .

### Cluster ebb24cd9dd — score 10

- Title: Almost Half of Malware Samples Communicate Direct to IP
- Source: Unit 42 (threat_research_primary)
- Published: 2026-08-04T12:50:53+00:00
- Link: https://unit42.paloaltonetworks.com/malware-bypass-dns-direct-to-ip/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, supply_chain, web_shell_backdoor
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, web_shell_backdoor
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Nearly half of C2 malware bypasses DNS by connecting directly to IP addresses. Zero trust IP enforcement secures networks against these threats. The post Almost Half of Malware Samples Communicate Direct to IP appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Almost Half of Malware Samples Communicate Direct to IP 9 min read Related Products Advanced DNS Security Advanced URL Filtering Advanced WildFire Cloud-Delivered Security Services Cortex Cortex XDR Cortex XSIAM Unit 42 Incident Response By: Shu Wang Zhanhao Chen Daiping Liu Published: August 4, 2026 Categories: Malware Threat Research Tags: Command and Control D2IP Exfiltration IoT botnets IP traffic Mozi Phorpiex Ransomware SectopRAT Zero trust IP ZT-IP Share Executive Summary Malware samples often bypass DNS entirely, communicating directly to IP addresses instead. Our analysis of 4 million dynamic analysis reports indicates that almost half (45.32%) of malware samples with any command-and-control (C2) activity made at least one direct-to-IP (D2IP) address connection. Measured as a fraction of all C2 connection attempts, D2IP traffic accounts for 23.17% of the total. A wide variety of threats — including ransomware droppers, peer-to-peer (P2P) botnets and supply chain risks — communicate directly with hard-coded IP addresses, bypassing DNS entirely and evading DNS-based defenses altogether. This article introduces zero trust IP (ZT-IP), which is a network-level enforcement approach that applies zero trust principles to IP-based traffic. The enforcement approach verifies whether outbound connection destinations were ever sanctioned by a DNS response. We validate this approach against real-world network traffic and samples, demonstrating how ZT-IP successfully surfaces threats including: Phorpiex ransomware droppers connecting directly to C2 IP addresses A persistent data exfiltration campaign using a custom obfuscated HTTP GET request Mozi P2P botnet payloads delivered to internet-of-things (IoT) devices without DNS Palo Alto Networks customers are better protected from the threats discussed here through the following products and services: Advanced WildFire Advanced URL Filtering and Advanced DNS Security Cortex XDR and XSIAM If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Malware , DNS , Ransomware The DNS Visibility Gap DNS security has become a cornerstone of enterprise threat defense. By monitoring and filtering DNS queries, security teams can block malware from reaching known-bad domains and use sinkholing to disrupt C2 communications before they establish a foothold. This approach is effective when malware plays by the rules of relying on DNS for domain resolution. However, many types of malware do not. For example, a backdoor malware sample made no DNS query at all before initiating a WebSocket connection directly to an IP address. Disassembly via Ghidra revealed why. The destination address wss://154.92.19[.]71:39989 was hard coded into the binary as a Unicode string. This is not an isolated edge case. Without the DNS resolution step in network communications, malware is invisible to DNS-based security controls, protective DNS sinkholing and DNS anomaly detection systems. The connection simply appears as raw IP traffic with no prior context. Prevalence of IP Traffic in Malware We analyzed over 4 million Advanced WildFire dynamic analysis reports for a 30-day period to quantify how prevalent this behavior truly is. We filtered out connections to common legitimate services, internal addresses and DNS resolvers. After doing that, we found that 20.11% of malware samples exhibited C2 activity. The contrast with benign samples is striking. Only 1% of benign samples establish connections to untrusted IP addresses after applying the same filtering criteria. Those that do average just 1.6 such connections per sample. This is a small fraction of the activity observed in malware. Among malware with C2 connections, TCP dominates (94.43% prevalence, averaging 4.17 unique C2 IP addresses per sample). UDP is present in 17.50% of cases but contacts far more IP addresses per sample (averag
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Almost Half of Malware Samples Communicate Direct to IP
  - Published: 2026-08-04T12:50:53+00:00
  - Link: https://unit42.paloaltonetworks.com/malware-bypass-dns-direct-to-ip/
  - Summary: Nearly half of C2 malware bypasses DNS by connecting directly to IP addresses. Zero trust IP enforcement secures networks against these threats. The post Almost Half of Malware Samples Communicate Direct to IP appeared first on Unit 42 .

### Cluster d1c29125d3 — score 10

- Title: Pass the Passkey: A Novel Attack Surface in Passwordless Authentication
- Source: Unit 42 (threat_research_primary)
- Published: 2026-08-03T10:00:35+00:00
- Link: https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_products: Google Cloud, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: Palo Alto Networks, Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Explore how passkey implementation gaps undermine security when relying parties fail to validate the User Verified flag, reducing MFA to a single factor. The post Pass the Passkey: A Novel Attack Surface in Passwordless Authentication appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Pass the Passkey: A Novel Attack Surface in Passwordless Authentication 17 min read Related Products Cortex Cortex Cloud By: Arie Olshtein Published: August 3, 2026 Categories: Malware Threat Research Tags: Google authenticator Google Chrome Google Cloud Identity Key Passkey Passwordless Share Executive Summary This article analyzes new attack classes against passwordless authentication, focusing on Google’s synced passkey ecosystem and the Cloud Authenticator used by desktop clients. The attacks demonstrate how malware on a compromised endpoint can misuse onboarding, recovery and device trust workflows to take over passkey-protected accounts. We show how an attacker can authenticate without user interaction, bypass user verification requirements and extract all synced passkey private keys. After decades of breaches and billions in losses, the attack vectors that defined the era of passwords and shared secrets are finally starting to fade. Passkeys replace passwords and traditional multi-factor authentication (MFA) with public-key cryptography, decreasing entire classes of attacks that have dominated the threat landscape for years. With no shared secret to steal, reuse or phish, many of an attacker’s most reliable tools are becoming obsolete. This represents a significant disruption for the credential theft market. Attackers, however, persist. They evolve, and defenders must prepare for a new generation of attacks. As passkeys become widely adopted and scale to billions of accounts, defenders must prepare for new attack surfaces, some of which we disclose in our research. This article is part 3 in our series examining passkey adoption from a security perspective. If you haven’t read the previous parts, we recommend starting here: Part 1: The Art of the Invisible Key – Passkey Global Breakthrough Part 2: Google Authenticator: The Hidden Mechanisms of Passwordless Authentication Palo Alto Networks customers are better protected from this new attack vector through the following products and services: Cortex Cloud Identity Security Idira Threat Detection and Response Idira Endpoint Privilege Manager Idira Privilege Access Management If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Google Authenticator , Cloud , Malware Setting the Stage Google’s synced passkey implementation is particularly instructive due to its scale and how it creates a higher standard for private key protection in two critical ways: Private keys are generated and used within a cloud-enclave isolation environment Hardware-backed, client-device-bound keys control access to cloud-based cryptographic operations, attesting to the user’s presence on a trusted device This article builds on the architectural analysis from Part 1 and Part 2 of our previous articles in this series. We now shift from how passkeys are built and deployed to how attackers can misuse them. We present three novel attacks that enable account takeover of passkey-protected accounts. Each attack challenges a different core assumption of passkey authentication security. When a client authenticates with a passkey, the following is expected: Users provide explicit consent on the device to verify user presence For MFA, users must also unlock the device to verify biometric (i.e., something you are) or knowledge-based (i.e., something you know) authentication factors Passkey private keys cannot be shared or copied The Google documentation reflects these core assumptions, describing the passkey login process as a secure alternative to passwords (as shown in Figure 1). Figure 1. Google documentation describes passkeys as requiring device access, device unlock, and non-shareable credentials. Challenging these expectations is a category of attacks we've nicknamed Pass-ta-key. This playful, layered name blends the word passkey and the phrase “pass the key,” with a
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Pass the Passkey: A Novel Attack Surface in Passwordless Authentication
  - Published: 2026-08-03T10:00:35+00:00
  - Link: https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/
  - Summary: Explore how passkey implementation gaps undermine security when relying parties fail to validate the User Verified flag, reducing MFA to a single factor. The post Pass the Passkey: A Novel Attack Surface in Passwordless Authentication appeared first on Unit 42 .

### Cluster 75acd25c40 — score 10

- Title: Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks
- Source: Unit 42 (threat_research_primary)
- Published: 2026-07-30T10:00:52+00:00
- Link: https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT, Anthropic/Claude, GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 details a Chinese speaking threat actor combining autonomous AI scanning across seven vulnerabilities with manual exploitation. Read more. The post Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Vulnerabilities Vulnerabilities Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks 10 min read Related Products Advanced Threat Prevention Advanced WildFire Cloud-Delivered Security Services Cortex Cortex XDR Cortex Xpanse Cortex XSIAM Next-Generation Firewall Unit 42 AI Security Assessment Unit 42 Frontier AI Defense Unit 42 Incident Response By: Andy Piazza Published: July 30, 2026 Categories: Threat Research Vulnerabilities Tags: ChatGPT Claude code CVEs DeepSeek Exploitation Hermes Agent Share Executive Summary Unit 42 identified an AI-enabled autonomous hacking campaign carried out by a Chinese-speaking threat actor. They targeted infrastructure using seven vulnerabilities, combining autonomous AI-driven enumeration with manual exploitation that achieved confirmed impact. The actor, operating under the aliases knaithe and KnYuan , leveraged DeepSeek , via the Hermes Agent framework, as their autonomous offensive operator. They orchestrated this operator via Telegram for the following activities: Independently enumerating targets and their vulnerabilities using FOFA Sourcing exploit tools Initiating attacks without human intervention In parallel with their use of DeepSeek as their autonomous operator platform, the actor configured multiple large language models (LLMs) ( Qwen , GLM, Kimi, MiniMax). We also identified limited usage and testing of Western platforms. This includes Claude Code for connectivity testing and proxy validation. There were also signs of usage of Codex on exploit development directories. This limited usage is consistent with evaluating the AI-market to identify their preferred tool set. When initial exploitation failed due to the target environment's restrictive configurations, their Hermes Agent autonomously conducted searches for known critical-severity Common Vulnerabilities and Exposures (CVEs). It initially surveyed 10 product families, scanning GitHub for trending proofs of concept (PoCs) and prioritizing vulnerabilities by attack surface. This research led the agent to pivot to higher-value vulnerabilities, the seven covered in Table 2 below. While the observed campaign had limited impacts, the workflow confirms a functional, end-to-end autonomous offensive capability. Palo Alto Networks customers are better protected from the threats described here through the following products and services: Cortex XDR and XSIAM Cortex Xpanse Next-Generation Firewall with Advanced Threat Prevention The Unit 42 AI Security Assessment and Unit 42 Frontier AI Defense service can help identify and mitigate complex AI-enabled risks. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics GenAI , Vulnerabilities , LLM Technical Analysis We gained unique insights into this autonomous attack capability when the autonomous agent inadvertently exposed its infrastructure by starting a file server in its home directory. This revealed the full operational environment to our threat researchers. This visibility enabled us to understand their full tool set, how the attackers orchestrated multiple AI platforms and gave us a peek into their targeting. Based on our analysis of their session logs and configuration files, the actor primarily used the Hermes Agent with DeepSeek as its reasoning agent for the attack phase of this campaign. Their Hermes Agent conducted autonomous vulnerability enumeration, downloaded public exploit code from the internet and attempted exploits against targets. Additionally, the threat actor leveraged the following tools in a limited capacity, likely indicating an ongoing assessment of the AI market for their use cases: Claude Code: The actor only used this for connectivity testing and proxy validation. Session history (10 entries across three sessions) contained only /model checks, connectivity tests and one npm install request. Codex : There were signs
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks
  - Published: 2026-07-30T10:00:52+00:00
  - Link: https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/
  - Summary: Unit 42 details a Chinese speaking threat actor combining autonomous AI scanning across seven vulnerabilities with manual exploitation. Read more. The post Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks appeared first on Unit 42 .

### Cluster b9f78fb1fa — score 10

- Title: 128 Seconds to disruption: Microsoft Defender stops ransomware at QNET
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-08-04T17:54:04+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/08/04/129-seconds-disruption-microsoft-defender-stops-ransomware-qnet/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Microsoft Defender

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, ransomware_extortion
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Defender automatically isolated a compromised QNET endpoint in 128 seconds, stopping a multi-stage attack before the payload could persist or spread. The post 128 Seconds to disruption: Microsoft Defender stops ransomware at QNET appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Defender Topics Actionable threat insights Detection and protection success stories Microsoft Defender’s attack disruption now includes device isolation, a new response action that extends autonomous protection directly to compromised endpoints. At QNET, an attacker initiated a multi-stage attack using a legitimate Windows tool on a compromised endpoint to retrieve a malicious remote payload–a classic living-off-the-land (LOL) technique that often evades traditional containment. By automatically enforcing the new device isolation action on the compromised endpoint, Defender attack disruption stopped the attack dead in its tracks. From the first high-severity alert to completed isolation, after only 128 seconds, Defender cut off the attack chain before the second-stage payload could establish persistence or move beyond the host. The growing threat: when the endpoint is the blast radius Attack disruption has proven highly effective at stopping multistage, cross-domain attacks by disrupting the attacker’s ability to move across the environment. In many identity-driven attack scenarios, containing the compromised user is enough to shut down the attack chain, preventing lateral movement and limiting the attacker’s ability to access additional systems, identities, and resources. However, we are increasingly seeing a different class of high-severity incidents that begin with initial access directly on the device. Once adversaries establish a foothold on an endpoint, they can plant multiple persistence mechanisms and continue operating locally on the machine. This means that acting against the user’s identity alone is no longer enough to dismantle the threat. In these scenarios, the attacker has multiple ways to communicate and operate on the device beyond the user entity; the malicious code is already executing locally on the machine. The attacker doesn’t have to move laterally immediately; they can establish persistence, steal credentials, inject into processes, and prepare follow-on stages directly from the compromised endpoint itself. Previously, stopping these attacks required manual triage and response, giving attackers time to advance. Device isolation closes this gap by automatically correlating signals, assessing the threat, and isolating the compromised device within seconds. Traditional response approaches often depend on static playbooks triggered by individual alerts and maintained through manual tuning. Attack disruption instead uses AI-driven correlation and real-time analysis to identify multi-stage attacks by connecting signals across the environment before taking action. Device isolation is enforced only when the disruption pipeline reaches a high-confidence verdict—a threshold maintained at 99% precision. What is device isolation? When Microsoft Defender determines with high confidence that an endpoint is compromised, it isolates the device to immediately stop attacker activity and reduce the risk of further impact, such as data exfiltration and lateral movement. What happens during device Isolation When a device is isolated, all external network connectivity is blocked while maintaining access to required security services like Microsoft Defender for Endpoint. Selective isolation is supported, allowing customer-defined services or exclusions to continue functioning. Automatic device isolation is scoped to the affected device (supported today on onboarded MDE workstations), time-limited, and operator-controlled. Security teams can review context, take follow-up actions, and manually release isolation when it’s safe to do so. Why it matters Device isolation is a powerful containment control because it disrupts the attack regardless of how the device was compromised or what the attacker planned to do next. A single action cuts off network access, breaking lateral movement, command and control, credential theft, and rapid encryption–
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: 128 Seconds to disruption: Microsoft Defender stops ransomware at QNET
  - Published: 2026-08-04T17:54:04+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/08/04/129-seconds-disruption-microsoft-defender-stops-ransomware-qnet/
  - Summary: Microsoft Defender automatically isolated a compromised QNET endpoint in 128 seconds, stopping a multi-stage attack before the payload could persist or spread. The post 128 Seconds to disruption: Microsoft Defender stops ransomware at QNET appeared first on Microsoft Security Blog .

### Cluster b00983247a — score 10

- Title: An analysis of incidents at Brazilian educational institutions
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-08-03T13:00:17+00:00
- Link: https://securelist.com/incidents-at-brazilian-educational-institutions/120803/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion
- actor_attribution: LockBit
- affected_industries: education, financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng
- actor_attribution: LockBit
- affected_industries: financial_services, education
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky expert provides statistics and details on several incident response cases at educational institutions in Brazil, as well as tips for schools and universities on how to stay safe.
```

#### Full body

```
Table of Contents Introduction Key findings and statistics Interesting cases Case 01 – Leaked LockBit builder Case 02 – DragonForce deployed via AnyDesk Case 03 – Python keylogger used by an insider Conclusions and recommendations Observed TTPs Authors Cristian Souza Introduction Because of the amount of data that can be obtained and the high impact that successful attacks may have, educational institutions are frequent targets of cybercriminals. Both public and private schools and universities rely on software for managing personally identifiable information (PII) that is often insecure or insufficiently tested against known vulnerabilities. In addition, machines used by multiple people without accountability can be vulnerable to insider threats. The complexity of academic environments amplifies this risk. Unlike corporate networks, educational institutions have to provide a network that supports students, professors, researchers, administrative staff, third-party contractors, and visitors. Each of these groups has different security requirements and access control levels, making it difficult to enforce consistent security policies. A security breach can have severe consequences since it may expose vast amounts of sensitive information, such as social security numbers (CPF in Brazil), addresses, phone numbers, and even parents’ names. Armed with this information, attackers can attempt phishing attacks and impersonate the victims in SIM swapping attacks, a common practice in Brazil. In this article, we provide details about attacks on educational institutions in Brazil observed by our Global Emergency Response Team (GERT) since 2025. We share general statistics, common threats, initial access vectors, and the impact of such violations. Additionally, we present some interesting cases encountered by our team and the identified TTPs. Finally, we offer recommendations to help institutions protect themselves against future attacks. Key findings and statistics Our dataset encompasses incident response cases from January 2025 to June 2026. As the chart below shows, the majority of attacks targeted institutions in São Paulo state, Brazil’s most populous state and a significant center of economic and financial activity. We also had cases in Rio de Janeiro and Pernambuco. Geographical distribution of incident response requests at educational institutions ( download ) Of the customers who requested incident response, 60% were private institutions and 40% were public institutions. Private and public institutions ( download ) The most frequent reasons for requesting IR services were related to suspicious endpoint activities, encrypted files, and the presence of suspicious files. Incident response request reasons ( download ) High-severity incidents accounted for 40% of the total cases, while the remaining 60% were medium severity. Distribution of incidents by severity ( download ) The high-severity incidents were mainly related to ransomware attacks. Interestingly, private institutions were the most targeted by ransomware, while incidents in public institutions were mostly related to suspicious endpoint activity and privilege escalation attempts. The most common ransomware families found in our dataset were DragonForce and LockBit 3 , whose builder was leaked back in 2022. By using the leaked LockBit builder with a valid privileged account, attackers can build variants capable of disabling defenses and erasing logs. The most common initial access vectors included the use of valid accounts, exploitation of public-facing applications, and insiders. Initial access vectors ( download ) For privilege escalation, the attackers often relied on Potato variants (GodPotato, SweetPotato, and BadPotato). We also observed attackers using tools like AnyDesk for remote access, PsExec for lateral movement within compromised infrastructures, and AV-killer malware to terminate the system’s defenses. The latter was mainly used in ransomware-related incidents
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: An analysis of incidents at Brazilian educational institutions
  - Published: 2026-08-03T13:00:17+00:00
  - Link: https://securelist.com/incidents-at-brazilian-educational-institutions/120803/
  - Summary: Kaspersky expert provides statistics and details on several incident response cases at educational institutions in Brazil, as well as tips for schools and universities on how to stay safe.

### Cluster 1d6332ec8a — score 10

- Title: Network Anomaly Detection in KATA
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-31T10:00:25+00:00
- Link: https://securelist.com/tr/network-anomaly-detection-in-kata/120892/
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
An analysis of how Network Anomaly Detection (NAD) rules work within Kaspersky Anti Targeted Attack, using Kerberoasting and DNS tunneling attacks as examples.
```

#### Full body

```
Threat Response Table of Contents Introduction Kerberoasting attack detection by KATA Why standard tools have a hard time detecting Kerberoasting Creating a Network Anomaly Detection rule Detecting DNS tunneling in KATA How DNS tunnels work DNS tunneling detection logic Prebuilt rules for detecting network anomalies in KATA Conclusion Introduction Once the attacker has breached the corporate network, subsequent stages of the attack often involve leveraging standard domain infrastructure protocols: using Kerberos, running DNS queries, accessing internal services, opening network shares, and other common networking actions. Because this activity is virtually indistinguishable from legitimate network traffic, it is extremely difficult to detect it with traditional network attack detection tools. Kerberoasting and DNS tunneling have long ceased to be exotic techniques. They are becoming standard methods in modern attacks because they allow attackers to execute critical compromise stages while remaining undetected by traditional security tools. A clear example of this trend is seen in latest campaigns, employing both Kerberoasting and DNS tunneling . Traditional network security tools perform well when the attack features a distinct and identifiable indicator: a characteristic query string, a known malicious traffic pattern, or the source code of an already discovered exploit. While this approach to threat detection remains effective, it cannot always be applied to discovering network attacks that blend seamlessly with legitimate traffic inside a corporate network. Instead of searching for explicit indicators of attack, Network Anomaly Detection (NAD) analyzes all traffic for suspicious artifacts that deviate from the host’s typical network activity. Within Kaspersky’s solution portfolio, this technology is implemented specifically in the Kaspersky Anti Targeted Attack (KATA) platform. The system analyzes network traffic data (DNS, DCE/RPC, Kerberos and other packets) and extracts key parameters used to identify anomalous behavior. This approach enables searching for attacks on domain controllers, signs of traffic tunneling and exfiltration, C2 communications, and other scenarios that may point to compromise of network infrastructure. However, Network Anomaly Detection is not built on a single, universal set of indicators. Each attack scenario employs tailored detection models that account for the specifics of the corresponding network protocol, typical host behavior, and characteristic deviations from that baseline. This article examines two practical examples – detecting Kerberoasting and DNS tunneling – to demonstrate how these principles are implemented in KATA’s NAD rules and why this approach proves more effective than traditional signature-based analysis. Kerberoasting attack detection by KATA Why standard tools have a hard time detecting Kerberoasting The Kerberoasting attack leverages the standard operational logic of the Kerberos protocol. The attacker identifies service accounts configured with a Service Principal Name (SPN), requests a Ticket-Granting Service (TGS) ticket for them, and attempts to crack the password offline using a dictionary attack against the retrieved ticket. If the password is weak or hasn’t been changed in a long time, the adversary can bruteforce it to get it in cleartext. Subsequently, these compromised credentials can be leveraged for both vertical and horizontal movement across the network. The essence of a Kerberoasting attack is that an adversary possessing a compromised low-privileged account and a valid Ticket-Granting Ticket (TGT) for that account can request TGS tickets with weakened encryption for service accounts with SPNs. Crucially, it doesn’t matter whether the compromised account actually holds access permissions for those services. Having obtained these tickets, the attacker can then take them offline and bruteforce the service account’s password by trying to decrypt the correspond
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Network Anomaly Detection in KATA
  - Published: 2026-07-31T10:00:25+00:00
  - Link: https://securelist.com/tr/network-anomaly-detection-in-kata/120892/
  - Summary: An analysis of how Network Anomaly Detection (NAD) rules work within Kaspersky Anti Targeted Attack, using Kerberoasting and DNS tunneling attacks as examples.

### Cluster ba4ef137f5 — score 10

- Title: OctLurk and SilkLurk: newly identified tailored backdoors in cyber-espionage campaign in Central Asia
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-30T11:00:12+00:00
- Link: https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: critical_infrastructure, government, healthcare
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: healthcare, government, critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Our experts discovered OctLurk and SilkLurk, backdoors operating primarily in memory, targeting Central Asia. They inject plugins to launch shells, scan networks, dump credentials, and keylogging.
```

#### Full body

```
Table of Contents Introduction OctLurk OctLurk Deployment LurkPoxy Deployment OctLurk loader OctLurk backdoor Post-compromise activity Victim fingerprinting Event log collection Credential harvesting Impacket — secretsdump Keylogger Browser Password Decryptor Remote access : Pandora FMS agents (Pandora RC agent) Network scan: FSCAN Email harvesting LurkProxy SilkLurk Deployment SilkLurk loader SilkLurk backdoor Post-compromise activity Second-stage payload PlugX Infrastructure Attribution Conclusions Indicators of Compromise Backdoor domains and IPs OctLurk C2 LurkProxy C2 SilkLurk C2 Loaders OctLurk loader SilkLurk loader PlugX dropper PlugX loader OctLurk backdoor OctLurk File Manager plugin OctLurk Command Shell plugin OctLurk Interaction Manager plugin Impacket’s secretsdump (not available) Keylogger Browser password stealer FSCAN Batch scripts (not available) Archive utilities WinRAR 7zip File paths OctLurk file paths SilkLurk file paths PlugX file paths WinRAR and 7z file paths Authors Saurabh Sharma Yaroslav Kikel Introduction We have been tracking two new backdoors, OctLurk and SilkLurk , observed in attacks against government organizations primarily in Central Asia since January 2025. Identified victims are located in Afghanistan, Kyrgyzstan, Tajikistan, Uzbekistan, Kazakhstan, and the Syrian Arab Republic. These organizations operate across several sectors, including healthcare, research, government offices, ministries of foreign affairs, logistics, law‑enforcement agencies, urban planning and facilities management, and public educational establishments. The backdoor loaders are customized for each victim and use information from the victim’s machine to decrypt the payload. Both the loaders and the backdoors are heavily obfuscated, making analysis more complicated. OctLurk and SilkLurk can download and inject additional plugins to perform further malicious actions, including launching command shells, performing file system activity, synthesizing keyboard and mouse events, network scanning, credential dumping, keylogging, password theft from browsers, email collection, and remote access. Furthermore, the attackers deployed a specialized utility we named LurkProxy , which we also cover in this report. While it has a highly similar architecture to the OctLurk backdoor, it is not a backdoor itself. Our investigation shows that the same threat actor operates both SilkLurk and OctLurk , and some victims infected with SilkLurk also contain OctLurk. We assess with medium confidence that the same actor is behind both backdoors, and that they are Chinese‑speaking. However, at the time of publication, we couldn’t attribute this activity to any known group. OctLurk OctLurk Deployment The attacker created a scheduled task named GoogleUpDate on remote machines using admin credentials. The task runs once with System account privileges right after it was created, executing the batch script located at C:\Users\<username>\Videos\1.bat (MD5 6ecf84fb18f6747ed08d7598364d853a ). Prior to executing the task, the actor queries its status. It is then run, as shown below. The 1.bat script creates a service named NgcCIntSvc , which loads the loader DLL named oleasapi.dll (MD5 082d49ef9f14e6811d68c7e0e82e5069 ). The ServiceMain parameter in the service’s registry entry is set to invoke the RegisterService function of oleasapi.dll as shown below. LurkPoxy Deployment In another case, the attacker at first checked connectivity to the domain dns[.]ssentialserv[.]xyz as shown below. At the time of our research, the domain was resolving to the address 154[.]196[.]162[.]76 which is used as a LurkProxy C2 server. After confirming that the C2 server was reachable, the attacker executed the batch script C:\Users\[username]\Desktop\auto.bat (MD5 b874123a80fc4f40e06872b9cb54ebc6 ). The script created a service named Cusrxsrv , which loads a DLL named msbasesysdc.dll . In the service registry, the ServiceMain parameter was set to call the RegisterService fu
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: OctLurk and SilkLurk: newly identified tailored backdoors in cyber-espionage campaign in Central Asia
  - Published: 2026-07-30T11:00:12+00:00
  - Link: https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/
  - Summary: Our experts discovered OctLurk and SilkLurk, backdoors operating primarily in memory, targeting Central Asia. They inject plugins to launch shells, scan networks, dump credentials, and keylogging.

### Cluster f6cd02268d — score 10

- Title: Toy Ghouls’ new toy: the GenieLocker ransomware
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-30T08:00:57+00:00
- Link: https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky experts dissect GenieLocker: new custom ransomware variants for Windows, Linux, and ESXi systems. We found this family in attacks by Toy Ghouls, a financially motivated extortion group.
```

#### Full body

```
Table of Contents Introduction Technical details Modus operandi Initial Access Discovery and Credential Access Lateral Movement and Command and Control Impact Encryption Trojan for Windows Arguments and launch Anti-debugging Preparing for encryption File encryption and cryptography Encryption Trojan for ESXi and Linux ESXi and Linux features File encryption Victims Conclusions Indicators of compromise GenieLocker for Windows GenieLocker for Linux and ESXi C2 Authors Fedor Sinitsyn Yanis Zinchenko Introduction The new GenieLocker ransomware family has been active since March 2026. It has been used in attacks against organizations in the Russian Federation, primarily in the manufacturing sector, and attributed to the Toy Ghouls group by open-source intelligence (link in Russian). The Toy Ghouls, also known as Bearlyfy, Labubu and Laboo.boo, is a financially motivated extortion group, which previously relied on third-party encryption Trojans like RedAlert, LockBit, and Babuk. GenieLocker, apparently a custom design, upgrades their toolkit and reduces their reliance on third-party software. We discovered multiple samples of this Trojan in two variants: PE builds for Windows and ELF builds for Linux and ESXi. Technical details Modus operandi We described typical TTPs and modus operandi of the Toy Ghouls threat actor in the previous post (link in Russian). In this article, we aim to thoroughly describe the capabilities of Windows and Linux builds of the custom encryption Trojan GenieLocker. To give more context, we will also provide a brief overview of the attack that took place at the end of March 2026, where GenieLocker was deployed on the victim’s systems. Initial Access During the incident, the attackers first entered the environment through an OpenVPN connection originating from an external partner’s network. They likely exploited the trusted relationship with that partner and used stolen, yet still valid, credentials to connect. Discovery and Credential Access After breaching the target’s network, the attackers installed additional tools on the compromised hosts, including OpenSSH, socks5.exe, SoftPerfect Network Scanner, and Mimikatz. They employed SoftPerfect Network Scanner for discovery and used Mimikatz to dump credentials. Forensic analysis also shows that they accessed the KeePassXC password manager already installed on several compromised machines, likely attempting to extract the stored credentials from the KeePass databases. Lateral Movement and Command and Control Lateral movement was performed by using RDP to reach Windows machines and SSH for Linux servers. The widespread deployment of the encryption Trojan was conducted with the legitimate utilities PsExec and PAExec. Additionally, the attackers established a reverse SSH tunnel to communicate with their command‑and‑control server. Impact During the impact phase, the attackers encrypted files on the compromised Windows machines with the PE version of the GenieLocker ransomware. On the compromised Linux and ESXi servers, they stopped active virtual machines and encrypted their disks using the ELF version of GenieLocker. The tactics, techniques, and procedures seen here match those documented in earlier attacks attributed to the Toy Ghouls group. As in those prior incidents, forensic analysis found no evidence of data exfiltration, which is typical behavior for this threat actor. Toy Ghouls have not employed a double‑extortion model and do not run a data‑leak website. Encryption Trojan for Windows The Windows version of GenieLocker (MD5: 5d62c1349b8981c396c9a23f4f8f053c) is primarily written in C, but compiled with the C++ libraries using Microsoft Visual C/C++. The malware incorporates several ransom‑related capabilities, including process termination, service shutdown, debugger evasion, and a sophisticated encryption routine. For its cryptographic operations, it relies on the open‑source libsodium library. Aligned with the recent trend supported by our expertise,
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Toy Ghouls’ new toy: the GenieLocker ransomware
  - Published: 2026-07-30T08:00:57+00:00
  - Link: https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/
  - Summary: Kaspersky experts dissect GenieLocker: new custom ransomware variants for Windows, Linux, and ESXi systems. We found this family in attacks by Toy Ghouls, a financially motivated extortion group.

### Cluster fe05850866 — score 10

- Title: 3rd August – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-08-03T13:15:55+00:00
- Link: https://research.checkpoint.com/2026/3rd-august-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: critical_infrastructure, financial_services, government, manufacturing_industrial
- affected_products: Anthropic/Claude, VMware
- cve_ids: CVE-2026-20316, CVE-2026-59309, CVE-2026-59310, CVE-2026-59726, CVE-2026-63077
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: financial_services, government, critical_infrastructure, manufacturing_industrial
- affected_products: Anthropic/Claude, VMware
- cve_ids: CVE-2026-59726, CVE-2026-20316, CVE-2026-59309, CVE-2026-59310, CVE-2026-63077
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 27th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Minnesota IT Services has confirmed coordinated cyberattacks affecting more than 30 community water utilities across the state. The incidents briefly disrupted a treatment plant in Braham and affected industrial control systems. Officials reported […] The post 3rd August – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 3rd August – Threat Intelligence Report August 3, 2026 https://research.checkpoint.com/2026/3rd-august-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 27th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Minnesota IT Services has confirmed coordinated cyberattacks affecting more than 30 community water utilities across the state. The incidents briefly disrupted a treatment plant in Braham and affected industrial control systems. Officials reported that drinking water safety was not affected. While the attack was not officially attributed, federal officials previously posted warning regarding targeting of critical infrastructure by Iranian-affiliated threat actors. Bank of Baroda, a major Indian bank, has disclosed an email account compromise that exposed internal communications and attachments. Reports claim more than 700GB of customer files, loan documents, and audit records were leaked, although the bank has not confirmed the reported volume. Core banking systems were unaffected. Amgen, a US biotechnology company that develops medicines for serious illnesses, has confirmed a breach involving cloud environments operated by third-party providers. Attackers exfiltrated proprietary corporate information and patient health data. The company reported no disruption to manufacturing, financial reporting, products, or its ability to supply medicines. Angola’s largest telecommunications provider, Unitel, has suffered a cyberattack that disrupted voice, mobile data, and internet services for millions of customers. The outage also affected electronic payments shortly before the company’s stock market debut. Network data indicated that internal systems were disabled while external routers remained online. AI THREATS Anthropic has disclosed that Claude-based cybersecurity models gained unauthorized access to systems belonging to three outside organizations during controlled evaluations. The models moved beyond intended test environments and reached sensitive production assets. Anthropic identified the incidents while reviewing testing practices following separate autonomous AI security failures. Researchers have published details of CVE-2026-59726, a critical vulnerability in the Ruflo AI agent platform. An unauthenticated attacker could abuse its exposed Model Context Protocol bridge to execute commands, steal API keys, access conversations, and alter stored AI memory. Ruflo addressed the issue in version 3.16.3. Researchers surfaced a privacy issue in Anthropic’s Claude sharing feature that allowed publicly shared conversations and artifacts to be indexed by search engines. Indexed content reportedly included personal information, resumes, financial records, access codes, API keys, and clinical trial material that users may not have expected to become searchable. VULNERABILITIES AND PATCHES Cisco has addressed CVE-2026-20316, an actively exploited vulnerability in Secure Firewall Management Center. The flaw allows unauthenticated attackers to access a built-in low-privileged account and retrieve sensitive information from affected systems. Cisco released hotfixes after exploitation was identified, and the vulnerability was added to CISA’s catalog. Broadcom has released patches for five vulnerabilities affecting VMware vCenter, ESX, Workstation, and Fusion. Three critical flaws could allow authentication bypass, arbitrary code execution, or escape from a virtual machine to its host. The issues include CVE-2026-59309 and CVE-2026-59310, both carrying CVSS scores of 9.8. JetBrains has released fixes for CVE-2026-63077, a critical authentication bypass affecting all TeamCity On-Premises versions. A remote unauthenticated attacker could execute code with TeamCity server privileges and compromise connected build environments. The flaw is fixed in versions 2025.11.7 and 2026.1.3. TeamCity Cloud was not
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 3rd August – Threat Intelligence Report
  - Published: 2026-08-03T13:15:55+00:00
  - Link: https://research.checkpoint.com/2026/3rd-august-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 27th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Minnesota IT Services has confirmed coordinated cyberattacks affecting more than 30 community water utilities across the state. The incidents briefly disrupted a treatment plant in Braham and affected industrial control systems. Officials reported […] The post 3rd August – Threat Intelligence Report appeared first on Check Point Research .

### Cluster ef0ff97611 — score 10

- Title: “Keep going, bro. You’ve got this!” A data-driven look at how adversaries are weaponizing AI
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-08-04T10:00:11+00:00
- Link: https://blog.talosintelligence.com/keep-going-bro-youve-got-this-a-data-driven-look-at-how-adversaries-are-weaponizing-ai/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- tools_used: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ddos
- tools_used: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Talos has collected prompt logs from threat actor endpoints running various applications, such as Claude Code, CodeX, Cursor, or Gemini. This blog is an analysis of the ways we've seen bad actors leveraging cloud-based AI.
```

#### Full body

```
“Keep going, bro. You’ve got this!” A data-driven look at how adversaries are weaponizing AI By Nick Biasini , Dmytro Korzhevin , Jaeson Schultz , Vanja Svajcer , Vitor Ventura , Arnaud Zobec Tuesday, August 4, 2026 06:00 AI Threat Spotlight Threats Actor usage of AI is exploding. By analyzing artifacts left behind, Talos has created a detailed analysis of how we are seeing adversaries leverage the technology to include development, force multiplication, and vulnerability research. Based on the evidence Talos gathered, guardrails did not provide much protection, with most actors able to convince the models to comply despite the lack of sophisticated techniques or encoding. The pre-existing skill of the actor has a large impact on what they can accomplish with AI. Talos observed novice users able to create malicious capabilities, albeit with limited capabilities and success. Advanced users were able to build astonishing capabilities, pushing the models to create sophisticated and complex outputs. Artificial intelligence (AI) and associated language models are now ubiquitous and heavily used in both personal and professional contexts to streamline tasks and expand capabilities. With AI being used everywhere and by almost everyone, one of the biggest questions is how malicious actors are taking advantage. Fortunately, actors make mistakes and chatbots leave artifacts. Leveraging cloud-based AI models leaves behind a variety of artifacts, most notably a prompt log. These logs can take on a variety of shapes and sizes, but they are left on endpoints that are running various applications, such as Claude Code, CodeX, Cursor, or Gemini. Over the course of our research, we’ve collected a significant corpus of these files and can start discussing the ways we see bad actors leveraging these technologies. In conducting the research, three categories of activity emerged. One was using AI as a malicious software engineer, leveraging AI to write (in some cases) very sophisticated code with clear malicious intentions. Another was actors leveraging AI to scale criminal operations and campaigns. Finally, there were a lot of actors leveraging it for bug bounty or vulnerability research, rapidly accelerating their capabilities of discovery and disclosure. Each category demonstrates how threat actors are currently leveraging AI. Within each category is a wide disparity in sophistication based on the knowledge level of the actors involved. We tried to include use cases to cover the breadth of what we found. Takeaways and high-level findings With the recent disclosures from Hugging Face and OpenAI , it's clear the era of agentic attackers has effectively arrived. In that incident, the models were operating inside a sanctioned evaluation with safeguards deliberately relaxed — but they autonomously escaped their sandbox, found and chained real vulnerabilities, and compromised production infrastructure to reach their objective. The capabilities exist; the only missing ingredient is malicious intent, and it's a matter of time before threat actors supply it. For defenders, this is a wake-up call: Vulnerabilities will surface faster, exploitation will happen sooner, and the actors behind it won't need rest or downtime. As the case studies below show, the central challenge for guardrails right now is supporting legitimate dual-use work — red teaming and vulnerability research — without empowering malicious actors. One of the immediate takeaways is that guardrails are not functioning as expected. We did not encounter any sophisticated encoding or techniques designed to trick the models — most of the time it was a simple “I'm allowed to do this,” and the model complied. When guardrails did engage, they accomplished little. In one instance, we watched an actor abandon a censored model and pivot to an uncensored version, which completed the task without question. In another, a model pushed back on a distributed denial-of-service (DDoS) operator, but by that po
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: “Keep going, bro. You’ve got this!” A data-driven look at how adversaries are weaponizing AI
  - Published: 2026-08-04T10:00:11+00:00
  - Link: https://blog.talosintelligence.com/keep-going-bro-youve-got-this-a-data-driven-look-at-how-adversaries-are-weaponizing-ai/
  - Summary: Talos has collected prompt logs from threat actor endpoints running various applications, such as Claude Code, CodeX, Cursor, or Gemini. This blog is an analysis of the ways we've seen bad actors leveraging cloud-based AI.

### Cluster d2bbfb6b89 — score 10

- Title: Black Hat special: Rewind and revisit
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-30T10:00:08+00:00
- Link: https://blog.talosintelligence.com/black-hat-special-rewind-and-revisit/
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
Amy looks back at the incredible journeys that brought past guests to the world of threat intelligence.
```

#### Full body

```
Black Hat special: Rewind and revisit By Amy Ciminnisi Thursday, July 30, 2026 06:00 Humans of Talos Cybersecurity is rarely a straight line. In this special Black Hat edition of Humans of Talos, Amy looks back at the incredible journeys that brought past guests to the world of threat intelligence. From forensic labs and newsrooms to the kitchen line, we’re revisiting the stories and lessons that define the people behind the threat intelligence. Heading to Black Hat? We have a presence within the Cisco and Splunk booth (2633) during Black Hat where you can chat to us about our latest threat research and incident response, and grab the newest Snorty. Check out our schedule here . Want more episodes? Watch the full episode , and don’t forget to subscribe to our YouTube channel for the next Humans of Talos. Share this post Related Content Martin Lee: Running through the Arctic (and the threat landscape) July 1, 2026 06:00 Ever wonder how someone goes from studying human viruses to leading cybersecurity teams? In this Humans of Talos, we’re joined by Martin Lee, EMEA Lead, to talk about his journey into the industry. Winning the cyber marathon with Tony Giandomenico June 4, 2026 08:05 Tony Giandomenico, Senior Director of Product Management, joins Amy to discuss the Talos Threat Hunting launch what he's excited about for the future of cybersecurity, and, of course, his Ironman triathlons. Breaking things to keep them safe with Philippe Laulheret May 13, 2026 06:00 Philippe shares his unique journey from French engineering school to the front lines of cybersecurity, explaining how his lifelong love for solving puzzles helps him uncover critical security flaws before they can be exploited.
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Black Hat special: Rewind and revisit
  - Published: 2026-07-30T10:00:08+00:00
  - Link: https://blog.talosintelligence.com/black-hat-special-rewind-and-revisit/
  - Summary: Amy looks back at the incredible journeys that brought past guests to the world of threat intelligence.

### Cluster 432a5ea542 — score 10

- Title: How TTEC Turned Hidden Attack Paths Into Audit-Ready Security Validation
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-08-03T15:37:27+00:00
- Link: https://horizon3.ai/customer-story/ttec-security-validation-customer-story/
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
Discover how TTEC used NodeZero autonomous pentesting to uncover hidden attack paths, expose risky credentials, strengthen audit readiness, and validate real-world security risk across a complex global enterprise.
```

#### Full body

```
How TTEC Turned Hidden Attack Paths Into Audit-Ready Security Validation Horizon3 Customer Stories Security teams don’t struggle because they lack vulnerability data. They struggle because hidden attack paths, exposed credentials, and forgotten assets often remain invisible until an attacker finds them. TTEC, a global leader in customer experience (CX), needed a way to validate what attackers could actually exploit across a rapidly changing enterprise environment while producing evidence that could withstand increasing audit and customer scrutiny. This customer story explores how TTEC used autonomous pentesting to uncover overlooked attack paths, strengthen security operations, and simplify audit readiness. Key Insight Traditional penetration testing identified vulnerabilities. NodeZero uncovered how seemingly unrelated weaknesses could be chained together into real attack paths while automatically generating the evidence needed to validate remediation. By adopting autonomous pentesting, TTEC gained: Visibility into hidden attack paths traditional testing missed Faster discovery of exposed credentials and forgotten assets Continuous validation of real-world exploitability Stronger audit evidence with time-stamped remediation history Significant time savings compared to previous penetration testing workflows What You’ll Learn Why hidden credentials and legacy assets create exploitable attack paths How autonomous pentesting uncovers chained attacks that manual testing may overlook Ways to validate real exploitability instead of relying solely on vulnerability findings How credential discovery strengthens offensive security programs Why continuous testing produces more meaningful security validation How built-in remediation history simplifies audit preparation How to prioritize security work based on attacker impact rather than vulnerability volume Why It Matters Enterprise environments evolve constantly. New applications are deployed, infrastructure changes, credentials accumulate, and forgotten systems remain online longer than expected. Attackers only need one overlooked weakness to begin chaining their way toward critical assets. Organizations that improve resilience don’t just identify vulnerabilities—they continuously validate whether those vulnerabilities can actually be exploited and maintain evidence that demonstrates risk reduction over time. TTEC transformed autonomous pentesting into an operational security capability that strengthens both defensive readiness and audit confidence. Download the customer story to see how TTEC uncovered hidden attack paths, strengthened security validation, and simplified audit readiness with autonomous pentesting. ce. Download the Customer Story How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: How TTEC Turned Hidden Attack Paths Into Audit-Ready Security Validation
  - Published: 2026-08-03T15:37:27+00:00
  - Link: https://horizon3.ai/customer-story/ttec-security-validation-customer-story/
  - Summary: Discover how TTEC used NodeZero autonomous pentesting to uncover hidden attack paths, expose risky credentials, strengthen audit readiness, and validate real-world security risk across a complex global enterprise.

### Cluster 35c2b2988b — score 10

- Title: Horizon3 Raises $250M Series E at $2B+ Valuation to Lead the “AI vs. AI” Cybersecurity Era
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-08-03T13:04:33+00:00
- Link: https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Horizon3, the AI-Native Proactive Security Company behind NodeZero®, the World’s Best AI Hacker™, today announced a $250 million Series E at a valuation of more than $2 billion.
```

#### Full body

```
Horizon3 Raises $250M Series E at $2B+ Valuation to Lead the “AI vs. AI” Cybersecurity Era Business Wire August 3, 2026 Press Releases NightDragon and NEA Co-Lead Oversubscribed Round; Company triples valuation and surpasses 7,000 customers amid 120% ARR growth SAN FRANCISCO — August 3, 2026 — Horizon3, the AI-Native Proactive Security Company behind NodeZero®, the World’s Best AI Hacker™, today announced a $250 million Series E at a valuation of more than $2 billion, tripling its valuation from $650 million at Series D in just over a year. The oversubscribed round was co-led by existing investors NightDragon and NEA, with participation from seven new investors and five returning backers. The capital underscores accelerating global demand for safe, autonomous security validation as AI-driven cyberattacks escalate. “We invented the concept of AI Hackers and spent six years earning the right to autonomously pentest the most critical and sensitive networks in the world — with no humans in the loop,” said Snehal Antani, Co-Founder and CEO of Horizon3. “Our massive data moat – built on 310,000 tests safely executed in production – combined with thousands of radical champions who love our product, has allowed us to achieve consistent top-tier financial and operational metrics. This round gives us the fuel to scale aggressively as the definitive leader of the AI vs. AI era.” A Defining Moment for Autonomous Security Cyberattacks now move at the speed of AI, and traditional defenses cannot keep pace. Horizon3’s NodeZero platform closes that gap by autonomously and safely attacking an organization’s own production environment. It reveals exactly how adversaries chain together misconfigurations, weak credentials, and identity gaps to compromise critical systems, provides fix guidance, and instantly verifies remediation. Additionally, as NodeZero tests an environment, it can optimally deploy honeypots that are the cheapest, fastest, and most effective way of detecting AI attackers and prove they are inside. This unique approach has powered 120% year-over-year ARR growth as Horizon3 now protects over 7,000 organizations globally including multinational banks, major healthcare networks, and four Fortune 10 enterprises. Vetted, tested, and operational across large, classified government agencies and enterprises in the most highly regulated industries in the world, Horizon3 is FedRAMP® High authorized and helps organizations meet DORA, NIS 2, NIST CSF 2.0, HIPAA, SOC 2, and GDPR regulatory requirements. The company was also recently named the Fastest Growing Cybersecurity Company in North America by the Deloitte Technology Fast 500 and named one of the Most Innovative companies by Fast Company in 2026. Premier Global Investor Syndicate and Board Additions The Series E round was co-led by existing investors NightDragon and NEA, with participation from a syndicate of new and returning strategic and institutional investors: New investors: Acrew Capital, Blue Cloud Ventures, Demeter Group, EDBI (Singapore), PSG, SAIC, and Sapphire Ventures Existing investors: Craft Ventures, Prosperity7 Ventures, Qualcomm Ventures, Ridge Ventures, and SignalFire As part of the investment, Dave DeWalt, Founder and CEO of NightDragon and former CEO of FireEye and McAfee, and Morgan Kyauk, Managing Director at NightDragon, will join Horizon3’s Board of Directors. “Horizon3 coined the concept of cyber warfare being AI vs. AI, and that future has arrived,” said Dave DeWalt. “Snehal and his team have built an unparalleled proactive security platform that is fundamentally reshaping how the world defends its data. I am thrilled to join the board to help Horizon3 secure the world’s most critical infrastructure and enterprises at scale.” “Horizon3 has demonstrated textbook operational excellence,” said Morgan Kyauk. “They have built an incredibly efficient, highly scalable go-to-market motion that will be further amplified by NightDragon’s ecosystem of partners, advisors,
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Horizon3 Raises $250M Series E at $2B+ Valuation to Lead the “AI vs. AI” Cybersecurity Era
  - Published: 2026-08-03T13:04:33+00:00
  - Link: https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/
  - Summary: Horizon3, the AI-Native Proactive Security Company behind NodeZero®, the World’s Best AI Hacker™, today announced a $250 million Series E at a valuation of more than $2 billion.

### Cluster b1e5db3b13 — score 10

- Title: Building secure Uniswap v4 hooks
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-07-30T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/07/30/building-secure-uniswap-v4-hooks/
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
Uniswap v4 hooks let developers add custom behavior to pools, including dynamic fees, custom accounting, and external integrations. This flexibility moves some security responsibilities into application and hook code. The Cork and Bunni exploits are two app-level incidents that show what can go wrong in that code. Together, they account for more than $20M in losses. Neither incident stemmed from a flaw in the Uniswap v4 core protocol or the PoolManager; both arose from application-specific authorization and accounting logic built around hooks. After analyzing dozens of findings from Trail of Bits audits (including our Uniswap v4-core security review ), public reports from other firms, and the Solodit database, I’ve identified seven recurring failure patterns in application and hook code, including missing caller checks and accounting bugs that still satisfy the PoolManager’s settlement invariant. Builders can use these patterns as a secure-development checklist; auditors can use them t
```

#### Full body

```
Page content Uniswap v4 hooks let developers add custom behavior to pools, including dynamic fees, custom accounting, and external integrations. This flexibility moves some security responsibilities into application and hook code. The Cork and Bunni exploits are two app-level incidents that show what can go wrong in that code. Together, they account for more than $20M in losses. Neither incident stemmed from a flaw in the Uniswap v4 core protocol or the PoolManager; both arose from application-specific authorization and accounting logic built around hooks. After analyzing dozens of findings from Trail of Bits audits (including our Uniswap v4-core security review ), public reports from other firms, and the Solodit database, I’ve identified seven recurring failure patterns in application and hook code, including missing caller checks and accounting bugs that still satisfy the PoolManager’s settlement invariant. Builders can use these patterns as a secure-development checklist; auditors can use them to focus their review. What the PoolManager guarantees If you’re familiar with Uniswap v3, where each pool was a separate contract, v4 inverts the model. All pool state now lives in a singleton PoolManager contract, with each pool represented in its storage. Uniswap v4 adds hooks: independent contracts that execute custom logic at specific points in the swap and liquidity lifecycle. Figure 1: Pools live inside the singleton PoolManager, and multiple pools can use the same hook contract. Here’s what a pool looks like in v4: struct PoolKey { Currency currency0; Currency currency1; uint24 fee; int24 tickSpacing; IHooks hooks; } Figure 2: A pool's PoolKey includes both currencies, the fee, tick spacing, and the hook address ( v4-core/src/types/PoolKey.sol ). Notice that the hook address ( IHooks hooks; ) is part of the pool’s identity. If you change any of these fields, you’re talking to a different pool. This matters because trusting the wrong PoolKey means trusting the wrong pool. v4 also introduces a session-based model that works like a flash loan. Your contract calls unlock() on the PoolManager, which triggers a callback into your code. At the end, the PoolManager checks that no unsettled currency deltas remain: function unlock(bytes calldata data) external returns (bytes memory result) { Lock.unlock(); // ... callback execution happens here ... if (NonzeroDeltaCount.read() != 0) revert CurrencyNotSettled(); Lock.lock(); } Figure 3: Simplified PoolManager.unlock() flow: unlock the session, execute the callback, and revert unless all currency deltas settle to zero ( v4-core/src/PoolManager.sol ). Figure 4: A periphery or hook calls PoolManager.unlock(), handles unlockCallback(), and calls swap() inside the unlocked session. The PoolManager enforces v4’s protocol mechanics, including pool initialization rules, swap and liquidity math, hook-callback sequencing, and end-of-session settlement. Hook developers are responsible for validating the application-specific assumptions their hooks add. Each hook must decide: Who can call its privileged paths Which pools are legitimate How custom balances and deltas should be accounted for Whether external integrations can fail or reenter safely 1. Anyone can call your hook Hook callbacks are external functions on your contract. If you don’t check the caller, an attacker can call those callbacks directly with malicious parameters. A loose unlockCallback path can also reach internal actions that should never be callable. The fix: use BaseHook for hook entrypoints and SafeCallback for unlockCallback . Together, they enforce caller checks on the callback paths they cover: modifier onlyPoolManager() { if (msg.sender != address(poolManager)) revert NotPoolManager(); _; } Figure 5: onlyPoolManager restricts hook callbacks to the configured PoolManager. Add an equivalent caller check only on paths those contracts don’t cover. Real-world example: The Cork exploit (~$12M, May 2025) shows why this check matte
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: Building secure Uniswap v4 hooks
  - Published: 2026-07-30T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/07/30/building-secure-uniswap-v4-hooks/
  - Summary: Uniswap v4 hooks let developers add custom behavior to pools, including dynamic fees, custom accounting, and external integrations. This flexibility moves some security responsibilities into application and hook code. The Cork and Bunni exploits are two app-level incidents that show what can go wrong in that code. Together, they account for more than $20M in losses. Neither incident stemmed from a flaw in the Uniswap v4 core protocol or the PoolManager; both arose from application-specific authorization and accounting logic built around hooks. After analyzing dozens of findings from Trail of Bits audits (including our Uniswap v4-core security review ), public reports from other firms, and the Solodit database, I’ve identified seven recurring failure patterns in application and hook code, including missing caller checks and accounting bugs that still satisfy the PoolManager’s settlement invariant. Builders can use these patterns as a secure-development checklist; auditors can use them t

### Cluster 1b822e43c0 — score 10

- Title: 311,000 Impacted by Brown Health Medical Group-MA Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-05T11:35:23+00:00
- Link: https://www.securityweek.com/311000-impacted-by-brown-health-medical-group-ma-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- affected_industries: financial_services, government, healthcare
- affected_products: Google/Gemini, SonicWall, npm
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- affected_industries: healthcare, financial_services, government
- affected_products: SonicWall, npm, Google/Gemini
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers stole personal information, medical records, and financial information from the organization’s server. The post 311,000 Impacted by Brown Health Medical Group-MA Data Breach appeared first on SecurityWeek .
```

#### Full body

```
Lifespan Physician Group of Massachusetts, doing business as Brown Health Medical Group-MA, is notifying over 311,000 individuals that their personal, medical, and financial information was stolen in a data breach. The incident occurred in December 2025 at its Hawthorn location. It involved a historic file server, the healthcare organization says in a sample notification letter filed with the Massachusetts Office of Consumer Affairs and Business Regulation. While the practice’s electronic health record system was not affected, Brown Health Medical Group-MA determined on June 22, 2026, that the attackers accessed files containing personal information. The potentially compromised information, it says, includes names, contact information, dates of birth, Social Security numbers, driver’s license numbers, government ID numbers, medical and disability-related records, financial account information, and credit/debit card numbers. Personnel and human resources records, including payroll and compensation information, and licensure or credentialing information, were also compromised. “Not all categories of information were impacted for all individuals,” Brown Health Medical Group-MA says. Advertisement. Scroll to continue reading. The healthcare organization says it isolated the affected server immediately after identifying the incident, has implemented additional safeguards, and is re-training its employees. Brown Health Medical Group-MA notified the US Department of Health and Human Services (HHS) that 311,760 people were affected by the data breach. Of these, 290,357 are Massachusetts residents. The organization is providing the impacted individuals with two years of free fraud detection and identity protection and restoration services. Brown Health Medical Group-MA has not named the threat actor behind the attack, and SecurityWeek has not seen any known ransomware or extortion groups claiming responsibility for the incident. Related: 150,000 Impacted by Madera Community Hospital Data Breach Related: Cyberattack Hits Liechtenstein’s Register of People Behind Companies and Foundations Related: River Bank Says Hackers Deleted Data Stolen in Ransomware Attack Related: Brinks Home Discloses Data Breach as Hackers Leak Files Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Oligo Raises $60 Million for Runtime Security Zenity Raises $125 Million in Series C Funding Gemini Agent-to-Agent Attack Method Exposed Secrets, Enabled Pull Request Tampering Decades-Old BMC Vulnerability Exposes Thousands of Data Centers to Attacks 150,000 Impacted by Madera Community Hospital Data Breach River Bank Says Hackers Deleted Data Stolen in Ransomware Attack Brinks Home Discloses Data Breach as Hackers Leak Files Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks Latest News How a $50,000 Exploit Chain Turned Bixby Against Samsung Phones Black Hat USA 2026 – Summary of Vendor Announcements (Part 3) The Fourth Battlefield: The Growing Role of Cyber Operations in Global Conflict New Attack Methods Enable Malware to Hijack Passkey-Protected Accounts Cybersecurity Alliance Drafts SAFE Guidelines for Sharing AI Incident Data AI Agents Targeted Real People and Projects During Cybersecurity Tests CISA Warns of Exploited Langflow, N-central, and Tomcat Vulnerabilities Over 400 NPM Packages Infected in ChainDrop Supply Chain Attack Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Rethinking Cyber Defense for AI-Speed Attacks August 18, 2026 Join this live webinar as we explore if detection-first security operations can keep pace with AI, or if it’s time to rethink prevention as the strongest defa
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 311,000 Impacted by Brown Health Medical Group-MA Data Breach
  - Published: 2026-08-05T11:35:23+00:00
  - Link: https://www.securityweek.com/311000-impacted-by-brown-health-medical-group-ma-data-breach/
  - Summary: Hackers stole personal information, medical records, and financial information from the organization’s server. The post 311,000 Impacted by Brown Health Medical Group-MA Data Breach appeared first on SecurityWeek .

### Cluster 3569b34b72 — score 10

- Title: Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-05T11:04:23+00:00
- Link: https://thehackernews.com/2026/08/critical-gitea-flaw-let-unauthenticated.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-59774, Gitea

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Docker, Gitea
- cve_ids: CVE-2026-20896, CVE-2026-27771, CVE-2026-59774, CVE-2026-60004
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Gitea, Docker
- cve_ids: CVE-2026-59774, CVE-2026-60004, CVE-2026-20896, CVE-2026-27771
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
An unauthenticated attacker can read any file the service account can access on Gitea, the self-hosted Git platform, in versions 1.22.1 through 1.27.0. No login, no repository write access. A public repository and crafted Org-mode markup are enough. The flaw is fixed in Gitea 1.27.1. The file-read flaw is tracked as CVE-2026-59774, rated Critical with a CVSS score of 9.8, and received its
```

#### Full body

```
Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup  Swati Khandelwal  Aug 05, 2026 Vulnerability / DevOps An unauthenticated attacker can read any file the service account can access on Gitea , the self-hosted Git platform, in versions 1.22.1 through 1.27.0. No login, no repository write access. A public repository and crafted Org-mode markup are enough. The flaw is fixed in Gitea 1.27.1. The file-read flaw is tracked as CVE-2026-59774 , rated Critical with a CVSS score of 9.8, and received its formal advisory on August 2. Gitea 1.27.1 also patches CVE-2026-60004 , a separate remote code execution bug covered in a prior THN report . Gitea said Cloud instances would be upgraded automatically during the release maintenance window. Self-hosted administrators should move to 1.27.1 immediately. The file-read bug is not direct one-request remote code execution. Gitea says it can become command execution if an attacker reads app.ini , extracts INTERNAL_TOKEN , injects a Git hook through the internal logger, and triggers that hook during an anonymous clone. That chain is described in Gitea's advisory ; The Hacker News found no independently published exploit demonstrating it. Upgrading is necessary but may not be sufficient after suspected exposure. If logs show the markup endpoint was reached on an affected build, treat credentials readable by the Gitea service account as exposed and rotate the internal token, OAuth material, JWT signing material, and database credentials before considering the instance clean. No badge required The file-read path runs through Gitea's markup rendering endpoint, POST /{owner}/{repo}/markup . The route allows optional sign-in, resolves the repository, and checks reader access. An anonymous request clears that check against any public repository with its code unit enabled. That precondition limits the unauthenticated exposure: an instance with no public repositories has no anonymous attack path through this endpoint. The break is in Gitea's Org-mode renderer. Gitea 1.27.0 initialized go-org with org.New() and did not replace the library's default ReadFile callback. In go-org 1.9.1, that callback is ioutil.ReadFile . Org-mode's #+INCLUDE directive accepts absolute paths and passes them to the callback. An attacker submits Org-mode markup, selects Mode: file , and receives files the service account can read. The fix landed in PR #38642 and was backported in PR #38645. Gitea now overrides ReadFile so an Org-mode include path is returned as plain rendered content instead of being resolved from the server filesystem. The patch added a regression test for include-path rendering. CVE-2026-59774 was found by XBOW Security , an autonomous offensive security system, and triaged by Guido Leo . Shai Rod, known online as NightRang3r, independently reported the same issue. What administrators should check Gitea did not publish formal detection guidance in the advisory. Review anonymous POST requests to /{owner}/{repo}/markup , especially requests selecting Org-mode rendering or submitting absolute filesystem paths. If the advisory's escalation path was attempted, check repository hook directories for unexpected executable files. Gitea's advisory reports no exploitation in the wild, and as of August 5, 2026, CVE-2026-59774 had not appeared on CISA's Known Exploited Vulnerabilities catalog. The file-read primitive was publicly previewed before its formal advisory, according to a prior THN report. The token-to-hook command-execution chain remains single-sourced to Gitea's advisory. The flaw follows a dense stretch of Gitea security work. In June, Gitea patched a critical reverse-proxy authentication bypass in Docker images, CVE-2026-20896 , that threat actors were observed probing 13 days after disclosure. In May, a container-registry access-control flaw, CVE-2026-27771 , was estimated to affect more than 30,000 deployments across over 30 countries. Found this article interesting? F
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup
  - Published: 2026-08-05T11:04:23+00:00
  - Link: https://thehackernews.com/2026/08/critical-gitea-flaw-let-unauthenticated.html
  - Summary: An unauthenticated attacker can read any file the service account can access on Gitea, the self-hosted Git platform, in versions 1.22.1 through 1.27.0. No login, no repository write access. A public repository and crafted Org-mode markup are enough. The flaw is fixed in Gitea 1.27.1. The file-read flaw is tracked as CVE-2026-59774, rated Critical with a CVSS score of 9.8, and received its

### Cluster 5fb34094f6 — score 9

- Title: Botnet Hunting for Vulnerabilities in Diagnostic Tools, (Tue, Aug 4th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-08-04T12:46:19+00:00
- Link: https://isc.sans.edu/diary/rss/33214
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
This morning, I noticed specific sources "hunting" for vulnerabilities in URLs that I haven&#;x26;#;39;t noticed before. All of these URLs appear to be associated with diagnostic tools:
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Botnet Hunting for Vulnerabilities in Diagnostic Tools, (Tue, Aug 4th)
  - Published: 2026-08-04T12:46:19+00:00
  - Link: https://isc.sans.edu/diary/rss/33214
  - Summary: This morning, I noticed specific sources "hunting" for vulnerabilities in URLs that I haven&#;x26;#;39;t noticed before. All of these URLs appear to be associated with diagnostic tools:

### Cluster d737a53686 — score 9

- Title: Benchmarking the Agentic SOC: How we evaluate LLMs for security workflows
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-08-04T23:59:59+00:00
- Link: https://www.elastic.co/security-labs/llm-benchmarking-agentic-soc
- Fetch status: ok
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
Public leaderboards can't tell you which LLM to trust in your SOC, so Elastic built an evaluation framework that grades models on the work (tool calls, execution traces, blind judging) across Agent Builder, Attack Discovery, and automatic migration.
```

#### Full body

```
4 August 2026 • Dhrumil Patel Benchmarking the Agentic SOC: How we evaluate LLMs for security workflows Public leaderboards can't tell you which LLM to trust in your SOC, so Elastic built an evaluation framework that grades models on the work (tool calls, execution traces, blind judging) across Agent Builder, Attack Discovery, and automatic migration. 15 min read Generative AI , Internals An agentic SOC is only as good as the model driving it. The moment you let an LLM triage an alert, hunt across your telemetry, or author a detection rule, the question stops being "is this a smart model?" and becomes something much more specific: will it pick the right skill, call the right tool in the right order, and reach the right disposition without inventing a result it never actually checked? That is not a question a general-purpose leaderboard can answer. A model can top every public benchmark and still confidently tell you a malicious loader is "clean" because it narrated a VirusTotal verdict instead of calling VirusTotal. In a SOC, that is not a rounding error. That is a missed intrusion. So we built an evaluation framework to answer the question directly. It seeds a realistic intrusion into a live Elastic deployment, drives every available model through the same set of security tasks against the same agent, captures not just what each model said but every tool it called and every parameter it passed, and then judges the results blind. This post explains how it works and why we built it the way we did. The results themselves are published and continuously updated in the Large language model performance matrix for Elastic Security . Why generic LLM benchmarks fail for agents for security Public leaderboards measure knowledge and chat quality. They ask a model to recall facts, solve a puzzle, or write a tidy paragraph. Those are real capabilities, but they are the wrong proxy for agentic security work. Inside an agent, the model is not writing prose. It is making decisions: Which skill does this task need? Alert triage and entity risk-scoring are different jobs with different tools. Which tool, with which parameters, in which order? A hash goes to VirusTotal; an on-call question goes to the schedule; a case gets opened once, with the right fields. Is the output grounded? Did the model actually run the query and read the result, or did it produce a plausible answer with an empty trace? The most dangerous failure mode in an agentic SOC is the confident, fluent, wrong answer that was never grounded in a tool call. Generic benchmarks reward exactly that, because they only see the final text. To evaluate a SOC agent honestly, you have to grade the work, not the writing. What we actually need to measure We anchored the evaluation on the concrete capabilities a security analyst relies on, most of them built-in Agent Builder skills we shipped in Elastic Security. (For the product side of that story, see our companion post on the five Agent Builder skills in Elastic Security .) That gives us seven capability categories: Category What it tests Alert analysis Triage an alert, reach the correct disposition, pull related alerts, enrich with threat intel Entity analytics Investigate hosts and users with purpose-built entity lookups and risk context Threat hunting Generate and run queries against process, file, and network telemetry to find specific artifacts Detection rules Author a working detection rule, grounded in research when asked Workflow authoring Produce a valid, executable automation workflow (verified by actually running it) Triggering workflows Call the correct backed action for the task (hash lookup, on-call, case creation) Multi-step Chain several steps in the right order, carrying findings forward without skipping or fabricating These categories deliberately straddle two levels of the agent. Alert analysis, entity analytics, threat hunting, and detection rules are built-in Agent Builder skills; workflow authoring exercises the platf
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Benchmarking the Agentic SOC: How we evaluate LLMs for security workflows
  - Published: 2026-08-04T23:59:59+00:00
  - Link: https://www.elastic.co/security-labs/llm-benchmarking-agentic-soc
  - Summary: Public leaderboards can't tell you which LLM to trust in your SOC, so Elastic built an evaluation framework that grades models on the work (tool calls, execution traces, blind judging) across Agent Builder, Attack Discovery, and automatic migration.

### Cluster 6d386738b7 — score 9

- Title: Context-Backed Attacker’s-Eye Testing with Orca’s Attack Surface Red Agent
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-08-05T12:50:00+00:00
- Link: https://orca.security/resources/blog/attack-surface-red-agent/
- Fetch status: ok
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
Key Findings Attack Surface Risks in Fast-Paced Cloud Environments Teams that build fast don’t stop building outside of business hours, or between pentest cycles. New applications and services constantly get deployed, subdomains get spun up for a campaign and forgotten, APIs get exposed for a partner integration and never fully locked down. Every one of […]
```

#### Full body

```
Table of contents Key Findings Attack Surface Risks in Fast-Paced Cloud Environments Why Traditional Testing Approaches Break Down On-Demand, Attacker’s-Eye Testing with Orca’s Attack Surface Red Agent Where the Context Advantage Comes From Expanding the AI Agent Pod Security for the Companies that Build Schedule an Orca Security Demo Key Findings Building fast means shipping constant change: new applications, new services, new subdomains, new endpoints, new integrations. Every one of those is a potential new entry point, and most organizations only learn what’s actually exposed after a scan cycle, a bug bounty report, or an incident. The gap isn’t just calendar cadence. It’s that you can’t test something you shipped an hour ago without waiting on the next scheduled pentest or scanner cycle. Orca launches the Attack Surface Red Agent, an on-demand, AI DAST and AI Penetration testing that probes your organization’s external attack surface with an attacker’s-eye view to detect things such as broken authorization, exposed services, and more, the moment you need answers. It’s informed by cloud context Orca already has about the underlying assets, so findings arrive with real risk context instead of a raw scan output.That context, assembled before a single probe is sent, is what turns an on-demand test into something you can trust. The Attack Surface Red Agent belongs to Orca’s Red Pod, one of the purpose-built agent families (Red, Blue, Green) that make up Orca’s Core Agents, with Custom Agents available for teams who want to build their own. Attack Surface Risks in Fast-Paced Cloud Environments Teams that build fast don’t stop building outside of business hours, or between pentest cycles. New applications and services constantly get deployed, subdomains get spun up for a campaign and forgotten, APIs get exposed for a partner integration and never fully locked down. Every one of these is a normal, healthy byproduct of shipping quickly, but every one of them is also a potential entry point. Most security teams find out about them well after the fact, such as during an annual penetration test, in a bug bounty submission, or worse, during an active incident. Traditional external attack surface penetration testing was built for a slower world. A pentest firm scopes an engagement, runs it over a few weeks, and delivers a report weeks later. A scanner runs on a schedule and flags what it can see at that moment. Both approaches produce a snapshot, and snapshots go stale the moment something in the environment changes, which, for a team that’s constantly building, is constantly. The gap isn’t a lack of scanning tools. It’s that when something new ships, there’s no good way to test it right then, informed by everything you already know about the environment. What’s needed is a way to test what’s exposed on demand or on your own schedule, with real risk context behind every finding, instead of waiting on the next engagement to roll around. Why Traditional Testing Approaches Break Down Scheduled penetration tests are valuable for what they are: a deeply scoped, expert-led engagement that produces validated, high-confidence findings. Their real limitation isn’t depth, it’s cadence. A pentest captures the environment as it existed during a defined window, typically once or twice a year, so everything shipped after the engagement wraps goes unwatched until the next one. Standalone attack surface scanners close part of that cadence gap by running far more often, sometimes daily. What most of them lack is context. A newly discovered endpoint gets flagged the same way whether it sits in front of a disposable test environment or a production database, because the scanner has no visibility into the cloud infrastructure behind it. The result is another queue of unprioritized findings. The market has good answers for depth and good answers for frequency, but not both at once. What teams need is a balance of both, with deep context, the moment they act
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Context-Backed Attacker’s-Eye Testing with Orca’s Attack Surface Red Agent
  - Published: 2026-08-05T12:50:00+00:00
  - Link: https://orca.security/resources/blog/attack-surface-red-agent/
  - Summary: Key Findings Attack Surface Risks in Fast-Paced Cloud Environments Teams that build fast don’t stop building outside of business hours, or between pentest cycles. New applications and services constantly get deployed, subdomains get spun up for a campaign and forgotten, APIs get exposed for a partner integration and never fully locked down. Every one of […]

### Cluster f0542a4609 — score 9

- Title: 10 Best Tenable Alternatives in 2026
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-08-05T12:50:00+00:00
- Link: https://orca.security/resources/blog/10-best-tenable-alternatives/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Defender, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Microsoft Defender, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Many security teams adopted Tenable for network and infrastructure vulnerability management, and it still does that job well. But as cloud estates grow to include containers, serverless functions, and infrastructure-as-code pipelines, the gap between what Tenable covers and what teams actually need to protect becomes harder to ignore. That gap, not any fundamental product failure, […]
```

#### Full body

```
Table of contents Why Do Teams Look for Tenable Alternatives? What Should You Look for in a Tenable Alternative? 1. Orca Security — Best Overall for Cloud-Native Risk Beyond Network Vulnerability Management Key Features 2. Wiz — Closest Agentless Cloud-Native Peer 3. Palo Alto Networks Cortex — Broadest Platform Consolidation (ASM + Exposure + SOC) 5. SentinelOne Singularity — Best for Unified Endpoint Protection Plus AI-Driven Investigation 6. Qualys — Closest Like-for-Like VM Replacement 7. Microsoft Defender Vulnerability Management — Best for Microsoft-Centric Security Stacks 8. Rapid7 — Best for SecOps Teams Needing VM Plus SIEM 9. Aikido Security — Broadest Developer-First Code-to-Cloud Platform 10. Snyk — Best for Developer-First Open Source and Code Scanning How Do You Choose the Right Tenable Alternative for Your Team? Where Orca Fits Frequently Asked Questions about Tenable Alternatives Many security teams adopted Tenable for network and infrastructure vulnerability management, and it still does that job well. But as cloud estates grow to include containers, serverless functions, and infrastructure-as-code pipelines, the gap between what Tenable covers and what teams actually need to protect becomes harder to ignore. That gap, not any fundamental product failure, is what sends architects looking for alternatives. This article evaluates ten Tenable alternatives across cloud-native platforms, endpoint-rooted solutions, traditional VM replacements, and developer-first tools. Each entry states who it fits best and where it falls short, so you can match the right option to your team’s actual workload. Why Do Teams Look for Tenable Alternatives? Tenable has genuine strengths: CIEM and identity analysis capabilities, and network vulnerability scanning remain market standards. The challenge is that cloud-native security requires coverage Tenable wasn’t originally built to provide. Teams building a mature cloud security program find three specific scope gaps that drive the search for alternatives: Workload and runtime depth. Cloud Exposure and Hexa AI add runtime signals, but they don’t match the full agentless workload depth, malware, secrets, exploitability-ranked vulnerabilities, and PII in one pass, that purpose-built cloud platforms deliver. Attack path analysis. Tenable surfaces toxic combinations on a single asset, but doesn’t model the multi-stage lateral movement across misconfigurations, identities, workloads, and data that shows how an attacker reaches crown-jewel assets. Application security beyond IaC. Tenable covers IaC scanning, but there is no native SAST, SCA, secrets detection, or code-to-runtime tracing, so full-lifecycle AppSec still needs a separate toolchain. These gaps don’t make Tenable a bad product. They make it an incomplete one for teams operating multi-cloud, container-heavy environments. What Should You Look for in a Tenable Alternative? Before comparing individual tools, it helps to have a consistent evaluation rubric. The five criteria below apply whether you’re looking for a full platform replacement or a specialized complement. For a deeper look at how agentless cloud security vendors stack up against these criteria, the differences are worth understanding before you shortlist. Criteria What It Means Cloud-native platform breadth Coverage spans CSPM, CWPP, and container/serverless workloads, not just network-level VM scanning. Unified data model Findings from posture, workload, identity, and code scanning feed a single risk model rather than siloed dashboards from bolted-on acquisitions. Attack path and exploitability context The platform maps how individual findings chain together into real attack paths, prioritized by exploitability and asset criticality. Developer workflow fit Security findings surface in pull requests, CI/CD pipelines, and IDE integrations, not just SOC consoles. Pricing transparency Licensing is predictable and tied to assets or workloads, not gated behind opaque enterpr
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: 10 Best Tenable Alternatives in 2026
  - Published: 2026-08-05T12:50:00+00:00
  - Link: https://orca.security/resources/blog/10-best-tenable-alternatives/
  - Summary: Many security teams adopted Tenable for network and infrastructure vulnerability management, and it still does that job well. But as cloud estates grow to include containers, serverless functions, and infrastructure-as-code pipelines, the gap between what Tenable covers and what teams actually need to protect becomes harder to ignore. That gap, not any fundamental product failure, […]

### Cluster d00e5766ff — score 9

- Title: 7 Best Rapid7 Alternatives for Cloud Security and Exposure Management in 2026
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-08-05T12:50:00+00:00
- Link: https://orca.security/resources/blog/7-best-rapid7-alternatives/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Fortinet, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Microsoft Defender, Fortinet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
When your vulnerability findings are scattered across InsightVM, InsightCloudSec, InsightIDR, and Exposure Command, the real problem isn’t any single product. It’s the lack of a unified view that tells you which exposures an attacker could actually reach before your next audit or incident. This article walks through seven Rapid7 alternatives, ranked from the most complete […]
```

#### Full body

```
Table of contents Why Do Teams Look for Rapid7 Alternatives? What Should You Look for in a Rapid7 Alternative? 1. Orca Security — Best Overall for Unified, Agentless Cloud Exposure Management Key Features 2. Tenable — Closest Like-for-Like Vulnerability Management Replacement 3. Qualys — Best for Compliance-Driven Vulnerability and Patch Operations 4. CrowdStrike Falcon Exposure Management — Best for Teams Already Standardized on Falcon 5. Wiz — Closest Agentless Cloud-Native Peer 6. Microsoft Defender Vulnerability Management — Best for Microsoft-Centric Environments 7. Fortinet FortiSIEM — Best for OT and Air-Gapped Environments Needing On-Prem SIEM Flexibility How Do You Choose the Right Rapid7 Alternative for Your Team? Where Orca Fits Frequently Asked Questions about Rapid7 Alternatives When your vulnerability findings are scattered across InsightVM, InsightCloudSec, InsightIDR, and Exposure Command, the real problem isn’t any single product. It’s the lack of a unified view that tells you which exposures an attacker could actually reach before your next audit or incident. This article walks through seven Rapid7 alternatives, ranked from the most complete cloud-native replacement to the most specialized. You’ll get a consistent evaluation rubric, honest trade-offs for each option (including Orca’s own gaps), and a decision table so you can match the right tool to your team’s actual needs. Why Do Teams Look for Rapid7 Alternatives? Rapid7 is a capable product. It’s a collection of products that weren’t designed as one platform. Teams typically start evaluating alternatives when they realize the fragmented module stack creates scope gaps that compound over time, especially as cloud footprints grow beyond a single provider. For organizations building a cloud security program at scale , these gaps become harder to manage with each new workload. The most common pain points include: Multi-cloud consistency. Confirm depth of coverage across Azure, GCP, and OCI, since parity across providers is a common gap for tools that started single-cloud. Kubernetes and container depth. Runtime coverage for containers and Kubernetes comes through a third-party runtime layer in Rapid7’s premium tier rather than natively, which adds cost and another moving part as clusters scale. More products to operate. Reaching full coverage means running and correlating several separate products, each with its own console and data model, so the stack gets heavier to operate as your environment grows. What Should You Look for in a Rapid7 Alternative? Before comparing vendors, it helps to agree on what you’re evaluating. The rubric below applies to every alternative in this article, so you can score them consistently rather than comparing marketing claims. For a deeper look at the agentless dimension specifically, see this guide to evaluating agentless cloud security vendors . Criteria What It Means Cloud-native platform breadth Coverage extends beyond traditional network and endpoint vulnerability management into cloud workloads, identities, data, and AI resources. Unified data model Risk data flows through a single model rather than being stitched together from bolted-on modules with separate databases. Attack path and exploitability context The platform maps how an attacker could chain vulnerabilities, misconfigurations, and identity weaknesses to reach critical assets. Multi-cloud maturity Consistent depth across AWS, Azure, GCP, and OCI, not just one provider with the others added as afterthoughts. Pricing transparency A single SKU or predictable pricing structure versus stacked modules where costs compound as you add capabilities. 1. Orca Security — Best Overall for Unified, Agentless Cloud Exposure Management Orca replaces Rapid7’s four-product stack with a single agentless platform that covers hosts, containers, serverless functions, data stores, and AI workloads from one console. Where Rapid7 requires you to correlate findings across InsightVM, Insig
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: 7 Best Rapid7 Alternatives for Cloud Security and Exposure Management in 2026
  - Published: 2026-08-05T12:50:00+00:00
  - Link: https://orca.security/resources/blog/7-best-rapid7-alternatives/
  - Summary: When your vulnerability findings are scattered across InsightVM, InsightCloudSec, InsightIDR, and Exposure Command, the real problem isn’t any single product. It’s the lack of a unified view that tells you which exposures an attacker could actually reach before your next audit or incident. This article walks through seven Rapid7 alternatives, ranked from the most complete […]

### Cluster 5be40a98b2 — score 9

- Title: 9 Best CrowdStrike Alternatives in 2026
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-08-05T12:50:00+00:00
- Link: https://orca.security/resources/blog/9-best-crowdstrike-alternatives/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
CrowdStrike Falcon is a strong endpoint detection and response platform, but cloud security architects and CISOs often find that its agent-based architecture leaves gaps in agentless workload depth, full-lifecycle application security, and unified AI security. If your cloud footprint has grown beyond what Falcon’s EDR heritage was designed to cover, you’re likely evaluating options that […]
```

#### Full body

```
Table of contents Why Do Teams Look for CrowdStrike Alternatives? What Should You Look for in a CrowdStrike Alternative? 1. Orca Security — Best Overall for Cloud-Native Risk Beyond Endpoint Protection Key Features 2. Wiz — Closest Agentless Cloud-Native Peer 3. Palo Alto Networks Cortex — Broadest SOC and Platform Consolidation 4. SentinelOne — Best Autonomous, Agent-Based Endpoint Swap 5. Fortinet — Best for Security Fabric and On-Premises/Air-Gapped Environments 6. Tenable — Best for Exposure Management and Vulnerability-First Programs 7. Netwrix — Best for Identity Governance and Compliance Evidence 8. Exabeam — Best for SIEM- and UEBA-Driven Security Operations 9. AnySecura — Best for Data-Centric and Insider Risk Protection How Do You Choose the Right CrowdStrike Alternative for Your Team? Where Orca Fits Frequently Asked Questions about CrowdStrike Alternatives CrowdStrike Falcon is a strong endpoint detection and response platform, but cloud security architects and CISOs often find that its agent-based architecture leaves gaps in agentless workload depth, full-lifecycle application security, and unified AI security. If your cloud footprint has grown beyond what Falcon’s EDR heritage was designed to cover, you’re likely evaluating options that address those specific blind spots. This article breaks down nine CrowdStrike alternatives across distinct categories, from cloud-native platforms to endpoint-first swaps to specialized complements. You’ll get a structured evaluation rubric, honest trade-off assessments for each tool, and a buyer-decision table to match your team’s primary gap to the right solution. Why Do Teams Look for CrowdStrike Alternatives? CrowdStrike Falcon remains one of the strongest agent-based endpoint detection and response platforms available. The reason teams explore alternatives isn’t a product failure. It’s an architectural scope gap rooted in Falcon’s EDR heritage. As organizations expand into multi-cloud environments, serverless workloads, and API-driven architectures, the areas where Falcon’s coverage thins out become more visible. The most common gaps driving evaluation include: Agentless workload depth. Falcon’s agentless mode covers inventory and posture, but runtime protection still requires the Falcon sensor on each workload. In environments full of ephemeral containers and auto-scaling groups, that sensor coverage is never fully closed, so the deepest workload protection lags the environment. API security. Falcon maps application APIs through ASPM’s runtime application analysis, but that is tied to instrumented applications rather than dedicated, agentless discovery of managed and shadow APIs across the cloud estate. Full-lifecycle AppSec depth. Falcon offers IaC scanning, but lacks integrated SAST, SCA, secrets detection, and container image scanning with traceability from cloud runtime back to the developer’s code. Unified AI security. Falcon’s AI security is split across Falcon AIDR, Falcon Shield, and Project QuiltWorks, so the consolidation story breaks down where AI risk lives. What Should You Look for in a CrowdStrike Alternative? Before comparing individual vendors, it helps to establish clear evaluation criteria. A structured rubric keeps the process grounded in your actual gaps rather than vendor marketing. The five criteria below cover the dimensions where CrowdStrike alternatives most commonly differentiate themselves. For a deeper look at building your evaluation process, Orca’s cloud security program maturity guide offers a useful framework. Criteria What It Means Agentless deployment and coverage breadth Can the platform discover and assess cloud workloads, containers, and serverless functions without installing or maintaining agents? Unified data model vs. bolted-on point tools Does the platform correlate findings across workloads, identities, data, and APIs in a single model, or does it stitch together separate acquisitions? Native AppSec and API security depth Does the p
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: 9 Best CrowdStrike Alternatives in 2026
  - Published: 2026-08-05T12:50:00+00:00
  - Link: https://orca.security/resources/blog/9-best-crowdstrike-alternatives/
  - Summary: CrowdStrike Falcon is a strong endpoint detection and response platform, but cloud security architects and CISOs often find that its agent-based architecture leaves gaps in agentless workload depth, full-lifecycle application security, and unified AI security. If your cloud footprint has grown beyond what Falcon’s EDR heritage was designed to cover, you’re likely evaluating options that […]

### Cluster 1b8e0b0f32 — score 9

- Title: Flaws in Google APK for Python Unlock Agent-to-Agent Attack
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-08-05T18:03:31+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/flaws-google-apk-python-agent-to-agent-attack
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, supply_chain
- affected_industries: government
- affected_products: GitHub
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, ai_security
- affected_industries: government
- affected_products: GitHub
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Google has fixed the issues, which exploited a trust boundary between two AI agents with different privilege levels to trigger automation that could compromise the supply chain.
```

#### Full body

```
Vulnerabilities & Threats Threat Intelligence Cyber Risk Cyberattacks & Data Breaches News Flaws in Google APK for Python Unlock Agent-to-Agent Attack Google has fixed the issues, which exploited a trust boundary between two AI agents with different privilege levels to trigger automation that could compromise the supply chain. Elizabeth Montalbano , Contributing Writer August 5, 2026 4 Min Read Source: Brain Light via Alamy Stock Photo AI agents can be weaponized against each other using prompt injections via a chain of flaws in Google's open source Agent Development Kit (ADK) for Python, potentially disrupting the software supply chain and demonstrating yet another new attack vector introduced by the emerging technology. Researchers from Pillar Security discovered the flaws, present in the ADK's adk-python repository, which allowed a low-privileged, public-facing agent in a workflow to trigger commands that could be executed by a high-privileged one, according a report published on Aug. 4. This means that potentially malicious, untrusted text — such as a pull request or issue — could be performed by a trusted AI agent with repository privileges. "Pillar Security researchers have identified the first practical, real-world case of agent-to-agent exploitation in a multi-agent system in a real production environment, a class of attack not seen in real production systems until now," Dan Lisichkin, cybersecurity researcher for Pillar, wrote in the report this week. Related: Attackers Exploit N-able Patch Bypass Flaw on RMM Servers The attack was especially problematic because it relied on prompt injections embedded in GitHub pull requests to exploit a trust boundary between two AI agents with different privilege levels, according to Pillar. In their proof-of-concept (PoC) exploit, the researchers showed that a public-facing AI agent reviewing pull requests could be manipulated into triggering a maintainer-only AI agent capable of performing privileged actions. This created a pathway to approve or execute malicious code in continuous integration (CI)/continuous delivery (CD) workflows that affect the development process and thus the software supply chain, Lisichkin said. This scenario, in which one AI agent can be used to attack another, turned "a benign automation into a path that ends in a potential software supply chain compromise," he wrote. Attack Flow and Remediation Google's ADK for Python has been downloaded more than 90 million times and is widely used by developers who work with Gemini, Google's large language model (LLM). Pillar credited Google for a prompt response to the flaws, which were reported in early June and remediated on July 9 and July 21, respectively. Google did not immediately respond to requests for comment by Dark Reading today. Specifically, the researchers showed that a malicious embedded prompt could persuade the agent to publish a specially formatted @gemini-cli command, according to the report. "That comment was then recognized by a dispatcher workflow and routed to a more privileged Gemini-based automation," Lisichkin wrote. Related: 'Certighost' Flaw Haunts Microsoft Active Directory Certificates The finding demonstrates how interactions between AI agents are now emerging as a new privilege-escalation attack surface. Pillar's discovery comes hot on the heels of the emergence of autonomous LLM attacks , introducing yet another threat type against which defenders need to secure AI agents and systems. While the flaws were characterized as a prompt injection issue — a common attack vector for LLMs and AI agents — the real issue it created for how organizations are using AI agents "is delegation," says Ryan McCurdy, vice president of marketing at database governance firm Liquibase. “Enterprises are starting to put multiple AI agents into software delivery with different tools, permissions, and levels of authority," he says. "This research shows why governing each agent independently isn't enough. Organiz
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Flaws in Google APK for Python Unlock Agent-to-Agent Attack
  - Published: 2026-08-05T18:03:31+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/flaws-google-apk-python-agent-to-agent-attack
  - Summary: Google has fixed the issues, which exploited a trust boundary between two AI agents with different privilege levels to trigger automation that could compromise the supply chain.

### Cluster b138851666 — score 9

- Title: Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-01T07:12:42+00:00
- Link: https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48449

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security
- affected_industries: manufacturing_industrial
- affected_products: GitHub, Microsoft SharePoint, OpenAI/ChatGPT
- cve_ids: CVE-2026-48390, CVE-2026-48395, CVE-2026-48396, CVE-2026-48448, CVE-2026-48449
- urgency_signals: actively_exploited, critical_cvss, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ai_security, active_exploitation
- affected_industries: manufacturing_industrial
- affected_products: Microsoft SharePoint, GitHub, OpenAI/ChatGPT
- cve_ids: CVE-2026-48449, CVE-2026-48448, CVE-2026-48395, CVE-2026-48396, CVE-2026-48390
- urgency_signals: actively_exploited, poc_available, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Adobe has released security updates to address a maximum-severity security flaw in Campaign Classic (ACC), its enterprise-focused marketing automation platform, that could result in arbitrary code execution. The vulnerability, tracked as CVE-2026-48449, carries a severity score of 10.0 on the CVSS scoring system. It has been described as a case of incorrect authorization that could result in
```

#### Full body

```
Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction  Ravie Lakshmanan  Aug 01, 2026 Vulnerability / Enterprise Security Adobe has released security updates to address a maximum-severity security flaw in Campaign Classic (ACC), its enterprise-focused marketing automation platform, that could result in arbitrary code execution. The vulnerability, tracked as CVE-2026-48449 , carries a severity score of 10.0 on the CVSS scoring system. It has been described as a case of incorrect authorization that could result in arbitrary code execution in the context of the current user without requiring any user interaction. The update also resolves another high-severity flaw ( CVE-2026-48448 , CVSS score: 8.6) stemming from SQL injection that could pave the way for arbitrary file reads. "This update addresses critical vulnerabilities that could result in arbitrary code execution and arbitrary file system read," Adobe said in an advisory. The company noted that it's not aware of any of the flaws being exploited in the wild. Both shortcomings have been addressed in ACC v7: 7.4.3 build 9398 for Windows and Linux. Separately, Adobe has also shipped updates to remediate eight critical-rated flaws in Adobe Bridge that could lead to privilege escalation and arbitrary code execution - CVE-2026-48395 (CVSS score: 8.6) - An untrusted search path vulnerability that leads to arbitrary code execution CVE-2026-48396 (CVSS score: 8.6) - An incorrect authorization vulnerability that leads to arbitrary code execution CVE-2026-48390 (CVSS score: 8.6) - An incorrect authorization vulnerability that leads to privilege escalation CVE-2026-48391 (CVSS score: 8.2) - An untrusted search path vulnerability that leads to arbitrary code execution CVE-2026-48374 (CVSS score: 7.8) - A path traversal vulnerability that leads to arbitrary code execution CVE-2026-48392 (CVSS score: 7.8) - An out-of-bounds write vulnerability that leads to arbitrary code execution CVE-2026-48393 (CVSS score: 7.8) - An out-of-bounds write vulnerability that leads to arbitrary code execution CVE-2026-48394 (CVSS score: 7.8) - An out-of-bounds write vulnerability that leads to arbitrary code execution Adobe credited security researcher Kieran ("kaiksi") with discovering and reporting CVE-2026-48390, CVE-2026-48391, CVE-2026-48395, CVE-2026-48396, and CVE-2026-48374, and "yjdfy" for CVE-2026-48392, CVE-2026-48393, and CVE-2026-48394. Users are advised to apply the latest updates for optimal protection. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Adobe , Application Security , Code Execution , enterprise security , Linux security , privilege escalation , SQL Injection , Vulnerability , Windows Security ⚡ Top Stories This Week New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents OpenAI Says Its AI Models Escaped Sandbox, Targeted Hugging Face to Cheat Benchmark Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data Ubuntu snap-confine Flaw Could Give Local Users Root on Default Desktop Installs Nine-Year-Old RefluXFS Linux Flaw Gives Local Users Root on Default RHEL Installs Attackers Weaponize GitHub Actions Runners to Target cPanel and WHM Servers Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files ThreatsDay: Android Spyware, PLC Attacks, AI Image Prompt Injection + 12 More Stories Kimi K3 Agents Found Redis Zero-Days and Built RCE Exploit, Researchers Say Hacker Runs Hermes AI Agent Unattended
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction
  - Published: 2026-08-01T07:12:42+00:00
  - Link: https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html
  - Summary: Adobe has released security updates to address a maximum-severity security flaw in Campaign Classic (ACC), its enterprise-focused marketing automation platform, that could result in arbitrary code execution. The vulnerability, tracked as CVE-2026-48449, carries a severity score of 10.0 on the CVSS scoring system. It has been described as a case of incorrect authorization that could result in

### Cluster cd780b1305 — score 9

- Title: Stored XSS in Django's admin via an unvalidated URLField display path (CVE-2026-15920)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-08-05T14:38:12+00:00
- Link: https://www.reddit.com/r/netsec/comments/1vg9704/stored_xss_in_djangos_admin_via_an_unvalidated/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-15920

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-15920
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-15920
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/Sandwich_1337 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Stored XSS in Django's admin via an unvalidated URLField display path (CVE-2026-15920)
  - Published: 2026-08-05T14:38:12+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vg9704/stored_xss_in_djangos_admin_via_an_unvalidated/
  - Summary: submitted by /u/Sandwich_1337 [link] [comments]

### Cluster 37a54c4646 — score 9

- Title: Extend Amazon Inspector SBOM Generator with Plugins
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-07-30T17:22:54+00:00
- Link: https://aws.amazon.com/blogs/security/extend-amazon-inspector-sbom-generator-with-plugins/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: ShinyHunters
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis

#### Primary article taxonomy
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Amazon Inspector is an automated vulnerability management service that continually scans Amazon Web Services (AWS) workloads for software vulnerabilities. The vulnerability management capabilities of Amazon Inspector are powered by an asset inventory engine known as the Amazon Inspector SBOM Generator (inspector-sbomgen), a standalone command-line tool that produces a software bill of materials (SBOM) from container […]
```

#### Full body

```
AWS Security Blog Extend Amazon Inspector SBOM Generator with Plugins Amazon Inspector is an automated vulnerability management service that continually scans Amazon Web Services (AWS) workloads for software vulnerabilities. The vulnerability management capabilities of Amazon Inspector are powered by an asset inventory engine known as the Amazon Inspector SBOM Generator (inspector-sbomgen), a standalone command-line tool that produces a software bill of materials (SBOM) from container images, directories, archives, local systems, compiled binaries, and more. Over the past two years, we’ve expanded inspector-sbomgen’s coverage across dozens of programming language ecosystems, operating systems, and widely deployed applications. We’re pleased to announce a new capability for builders using inspector-sbomgen: a plugin system for writing your own custom package collectors that you can use right away, without requiring source code compilation nor waiting for an official release. You can download the latest version of inspector-sbomgen from the Amazon Inspector User Guide . In this post, we walk you through what the inspector-sbomgen plugin system does, why we built it, and how you can write your first plugin in a few minutes. Along the way, we also cover how plugin-generated package components integrate with Amazon Inspector for vulnerability scanning, and we explore the plugin safety model, which helps ensure security-hardened and predictable plugin behavior. Why we built a plugin system Software ecosystems are dynamic. New language package managers, lockfile formats, and end user applications ship constantly, and many are adopted quickly, in some cases with little security scrutiny. That leaves security teams with a visibility gap: production workloads running software that their SBOM tooling doesn’t yet recognize. Customers have asked us to inventory many of these ecosystems directly, and until recently, the only path to support was to open a feature request and wait for the inspector-sbomgen team to onboard the ecosystem and deploy a new release. The inspector-sbomgen plugin system changes that. With plugins, you can: Onboard ecosystems that inspector-sbomgen doesn’t support out of the box. New open source ecosystems, niche or fast-moving package formats, and internal or proprietary tooling can all be inventoried without modifying inspector-sbomgen. Prototype detection for an ecosystem quickly. We designed a plugin system that is friendly to developers and AI coding assistants alike. Plugins are written in Lua, loaded at runtime, and require no Go toolchain nor compilation. You can use the built in test harness to iterate on a plugin and see results immediately. Build on a stable foundation. The plugin API abstracts away artifact-type differences, so you write your detection logic once and it works seamlessly across container images, archives, local systems, and more. And because plugins stay decoupled from the internals of sbomgen, the core tool’s regression surface stays small. Internally, we’ve used the plugin system to ship new ecosystem coverage faster than before. In our 1.13 release , more than 20 ecosystems that were previously implemented in Go, including Apache Tomcat, NGINX, MySQL, Redis, WordPress, and the OpenSSH toolchain, are now embedded as plugins inside the sbomgen binary. The same release also added more than ten brand-new ecosystems as plugins, including Apache Cassandra, Apache Struts, Conda, Swift packages, and AI-agent collectors (Amazon Q Developer, Kiro CLI, Claude Code, GitHub Copilot, and Ollama). How inspector-sbomgen plugins work Sbomgen plugins follow a two-step pipeline: Discovery – Scan the artifact’s file system to identify files that contain installed package metadata. Collection – Open each discovered file, parse file contents, and publish findings into the SBOM. Under the hood, an event bus connects discovery and collection plugins. Discovery plugins publish events listing discovered files, a
```

#### Corroborating sources (2)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Extend Amazon Inspector SBOM Generator with Plugins
  - Published: 2026-07-30T17:22:54+00:00
  - Link: https://aws.amazon.com/blogs/security/extend-amazon-inspector-sbom-generator-with-plugins/
  - Summary: Amazon Inspector is an automated vulnerability management service that continually scans Amazon Web Services (AWS) workloads for software vulnerabilities. The vulnerability management capabilities of Amazon Inspector are powered by an asset inventory engine known as the Amazon Inspector SBOM Generator (inspector-sbomgen), a standalone command-line tool that produces a software bill of materials (SBOM) from container […]
- **Risky Business News** (practitioner_analysis)
  - Title: Sponsored: The intrusion signals hiding in plain sight
  - Published: 2026-08-03T00:22:38+00:00
  - Link: https://risky.biz/RBNEWSSI138/
  - Summary: In this sponsored interview James Wilson chats with Permiso CTO Ian Ahl about detecting ShinyHunters-style attackers as they move through cloud and SaaS environments. Ian explains how ordinary-looking events such as a password reset, a new MFA device, unusual searches and a first-time AWS role assumption can combine to reveal an intrusion. Permiso’s platform connects these signals across identity providers, cloud platforms and SaaS applications. They also discuss how AI is helping attackers move from initial access to extortion in just four hours.

### Cluster f0a862553c — score 9

- Title: CosmosEscape: Taking Over Every Database in Azure Cosmos DB
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-07-30T12:00:01+00:00
- Link: https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Azure

#### Cluster taxonomy (union across members)
- affected_products: Azure, Microsoft/Copilot
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: Azure, Microsoft/Copilot
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A critical vulnerability chain in Azure Cosmos DB enabled full read and write access to every Cosmos DB database.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo Wiz Research uncovered CosmosEscape , a critical vulnerability in Azure’s flagship database service, Azure Cosmos DB, via its Gremlin API. The vulnerability could have been exploited to compromise every database in the service, including Microsoft's own internal databases - potentially enabling a cross-service attack. Through CosmosEscape, attackers could have acquired what we’ve dubbed the Cosmos Master Key - a platform-wide secret that granted two incredibly powerful capabilities: Takeover - retrieving the primary key of any Cosmos DB account on demand, resulting in full read & write access. Enumeration - listing all databases on the service with the ability to filter by specific organization identifiers like subscription and tenant IDs. Chained together, these capabilities could have enabled precision targeting at platform scale: from identifying a specific organization's databases to compromising them, all from publicly accessible endpoints. Cosmos DB is used internally across Microsoft - services like Microsoft Entra ID , Microsoft Teams , and Microsoft Copilot all store data in Cosmos DB. Their databases were potentially accessible via this vulnerability. Microsoft has now fully remediated the issue, including eliminating the Cosmos Master Key. Microsoft also introduced new guardrails to Cosmos DB to prevent similar attacks. Figure 1: CosmosEscape’s impact This research was assisted by an early version of Atlas , our AI vulnerability researcher. Expect more from Atlas soon. Required Actions Microsoft has fully remediated this issue. No customer action is required. Microsoft conducted a thorough investigation and found no evidence of exploitation of this vulnerability beyond the research described in this blog. From a Single Query to Unlocking Every Database Cosmos DB supports multiple query APIs, and among them is Gremlin , a popular graph query language: // Find all users over 30 and return their friends ' names g.V().hasLabel(' user ').has(' age ', gt(30)).out(' knows ').values(' name ') While running Gremlin queries against Cosmos DB, we noticed a suspicious .NET exception. Since most open-source Gremlin stacks are JVM-based, the exception suggested that Cosmos DB was using a custom Gremlin engine . This was interesting - unlike standard SQL, where the engine maps queries to a fixed set of built-in operations, Gremlin servers often compile queries into executable code and run it in a restricted environment. Historically, these sandboxes haven't held up well . We suspected Cosmos DB's Gremlin sandbox may be vulnerable as well. And it was. Cosmos DB's engine translated Gremlin queries into .NET code, enforcing a set of restrictions designed to prevent queries from reaching beyond Gremlin operations. These restrictions, however, didn't sufficiently account for .NET reflection - allowing us to develop file read, write, and ultimately arbitrary code execution primitives, all through queries against our own database. The following image shows the output of a specially crafted Gremlin query ran against our database, resulting in the hostname command being executed on the Cosmos DB backend: Figure 2: Executing hostname on the Cosmos DB backend via the Gremlin API. See the full query in our upcoming BlackHat USA talk. By bypassing the Gremlin sandbox, we’ve gained code execution on the DB Gateway , a service that executes customer queries on their behalf, running on multi-tenant Service Fabric clusters. Looking around, customer databases weren’t hosted on these clusters, but the DB Gateway still had to reach them somehow. It turned out that it did so like any Cosmos DB client would - using the target account’s primary key , which grants full read-write access to the account’s databases. But how can the DB Gateway retrieve the primary key of our Cosmos DB account? The Cosmos Master Key Through credentials available on the cluster, the DB Gateway accessed a signing key that could retrieve the re
```

#### Corroborating sources (2)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: CosmosEscape: Taking Over Every Database in Azure Cosmos DB
  - Published: 2026-07-30T12:00:01+00:00
  - Link: https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db
  - Summary: A critical vulnerability chain in Azure Cosmos DB enabled full read and write access to every Cosmos DB database.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database
  - Published: 2026-07-30T13:34:09+00:00
  - Link: https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html
  - Summary: A now-patched vulnerability in Azure Cosmos DB could have let an attacker escape the service's Gremlin query sandbox and obtain full read and write access to databases across customer tenants, according to Wiz. Wiz, which codenamed the chain CosmosEscape, said the exploit chain began with a crafted query against a Gremlin database controlled by the attacker. From there, code execution on a

### Cluster c99323e585 — score 8

- Title: Max-severity Exchange server flaw under active exploitation by Kremlin hackers
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-07-30T19:01:12+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/max-severity-exchange-server-flaw-under-active-exploitation-kremlin-hackers
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor, zero_day
- cve_ids: CVE-2026-42897
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor
- cve_ids: CVE-2026-42897
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
Text settings Story text Size Small Standard Large Width * Standard Wide Links Standard Orange * Subscribers only Learn more Minimize to nav Russian state hackers are using a maximum-severity vulnerability in Microsoft Outlook’s Exchange Server to backdoor unpatched machines and steal credentials and other confidential information from them, security researchers said Thursday. The attacks are coming from TA488, a tracking name for a group working on behalf of the Kremlin, Proofpoint researchers said Thursday . Proofpoint and the National Security Agency jointly warned last week that the group, also tracked as Laundry Bear and Void Blizzard, had been carrying out similar attacks by exploiting a zero-day vulnerability in an email service from Zimbra. The revelation that TA488 is also exploiting the Exchange Server vulnerability to install advanced malware when a user does nothing other than open an email sent to an Outlook Web Access (OWA) account has elevated the group’s profile and assessments of its abilities. Doubling down “TA488 is doubling down on the use of ‘half-click’ exploits—where opening the email is enough to trigger compromise—with significantly improved loading mechanisms, techniques, and malware, signaling an improvement in the group’s tradecraft and capability,” Proofpoint researchers wrote. “This novel infection chain ends with a previously unknown JavaScript browser-based implant we call OWAReaper, purpose-built for persistent access inside OWA.” The vulnerability, tracked as CVE-2026-42897, is a cross-site-scripting vulnerability, usually abbreviated as XSS, that Microsoft provided mitigation advice for in May and patched in July. Microsoft gave it a maximum severity rating. The vulnerability, which stems from a failure to properly filter HTML embedded in an email, allows malicious JavaScript execution. Proofpoint said that TA488 may have exploited it as a zero-day. The malicious JavaScript installs a novel, custom-built browser extension that gives attackers persistent access to victims’ OWA accounts. Proofpoint said it was the most sophisticated backdoor the company has ever seen delivered through a half-click exploit. The company has named it OWAReaper. Company researchers explained: OWAReaper is executed entirely in the Outlook Web Access (OWA) reading pane. Upon execution, it uses Outlook APIs to rewrite the email on the Exchange server and remove the exploit content. Simultaneously, it disables OWA pop-ups and right-click ability while it runs. OWAReaper then creates a session key, unique to each target, and begins gathering the target’s email address, username and Outlook settings. It then creates two invisible input elements in the DOM and waits for the browser’s autofill to enter the username and password to gather the user’s OWA saved credentials. OWAReaper then writes an encrypted version of itself, and a decryption wrapper, into the browser’s localStorage, under settings fields in the PageDataPayload.OwaUserDefaultSettings key. This is a legitimate key used by OWA in its page rendering, where OWA evaluates OwaFrontendSyncState itself as part of its own sync restore flow. Every time the user opens an OWA tab in the browser, the normal OWA sync process automatically executes OWAReaper. In many cases, the backdoor can go on to steal OAuth tokens and, from there, gain full access to the mailbox of any authenticated user on the same network. “This persistent access lives on the server side and requires deliberate removal from the Exchange server; credential rotation and even full re-imaging of the targeted user’s device will not evict the actor,” Proofpoint said. It’s not clear if machines compromised by OWAReaper are disinfected once Microsoft’s July patch or a separate Exchange Emergency Mitigation service is installed. Proofpoint is advising affected users to revoke and audit their Exchange Web Services tokens for unauthorized add-ins and to (1) remove folder permissions to default users, (2) clear
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Max-severity Exchange server flaw under active exploitation by Kremlin hackers
  - Published: 2026-07-30T19:01:12+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/max-severity-exchange-server-flaw-under-active-exploitation-kremlin-hackers

### Cluster 582de97f0f — score 8

- Title: 2608-volatility-interlock
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-08-04T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/2608-volatility-interlock
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: critical_infrastructure, education, healthcare
- affected_products: Cisco, OpenAI/ChatGPT
- cve_ids: CVE-2026-20131
- attack_techniques: T1189
- urgency_signals: zero_day
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, web_shell_backdoor
- affected_industries: healthcare, critical_infrastructure, education
- affected_products: Cisco, OpenAI/ChatGPT
- cve_ids: CVE-2026-20131
- attack_techniques: T1189
- urgency_signals: zero_day
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Summary

```
<p>Multiple legitimate DFIR tools abused by GOLD EMBRACE double-extortion specialists</p> Categories: Threat Research
```

#### Full body

```
Interlock ransomware gang creates volatile situation Multiple legitimate DFIR tools abused by GOLD EMBRACE double-extortion specialists Written by Sergio Bestulic , Andrew Bonwell , Karla Soler , Michael Warner Threat Research Share This Link Copied In March 2026, the Sophos Emergency Incident Response (EIR) team investigated an incident in which we observed the use of the legitimate IR memory analysis tool Volatility3 by the ransomware threat actor Interlock. Use of legitimate tools in attacks such as these continues an unfortunate trend we first noted last year. Interlock, which Sophos Counter Threat Unit (CTU) researchers track as GOLD EMBRACE , emerged in September 2024. It has been spotted worldwide but currently focuses on North American and European targets in the critical infrastructure, healthcare, and education sectors. It practices double extortion -- stealing sensitive data before encrypting systems, then threatening to leak information on its "Worldwide Secrets Blog" if its demands are not met. Rather than operating as Ransomware-as-a-Service, Interlock appears to be the handiwork of a small, dedicated team of operators that develops its own malware and conducts its own attacks. Noteworthy tactics, techniques, and procedures (TTPs) include the use of ClickFix-style social-engineering methods , a custom-built remote-access trojan (RAT) called "NodeSnake" or (alternately) "Interlock RAT," and a PHP-based backdoor for cross-platform persistence (in addition to targeting of Windows and FreeBSD systems). More recently, Interlock has been actively exploiting CVE-2026-20131 , a critical-severity zero-day vulnerability in Cisco Secure Firewall Management Center (FMC) Software. Activity overview The adversary’s Volatility3 activity occurred on the customer’s Patient Zero device (that is, the first system the threat actor was able to compromise to establish a foothold in the target’s environment) prior to the start of our engagement. The customer’s environment comprises both Sophos-managed servers and (at the time) Defender-managed endpoints, though it was discovered that not all endpoints were in fact running protection of any sort. Patient Zero was a Defender-managed endpoint running Windows 10. On that machine, we observed credential access-related activity to extract NTLM hashes, LM hashes (legacy hashes if enabled), and user account information via this command: vol.exe -f .\mem.raw windows.hashdump.Hashdump In a legitimate use scenario, use of this command could be expected as part of a DFIR investigation, a security assessment, or malware analysis. However, adversarial use of Volatility3 would leave similar traces. In this situation, the customer knew of no legitimate Volatility3 use on their system. The team also observed the following command: vol.exe -f .\mem.raw windows.cachedump.Cachedump This command attempts to extract cached domain credentials from memory -- username and hash pairs, as well as information on previously logged-in domain users. We also saw the threat actor use WinPmem, a legitimate physical memory acquisition tool made by Velocidex (the company originally behind Velociraptor, now owned by Rapid7), to collect the memory capture: winpmem_mini_x64_rc2.exe mem.raw Diary of an attack chain The interval between initial access and lateral movement to the domain controller in this case took slightly over 26 hours – longer than average , but not much time at all in human terms. Interestingly, as we see below, the attacker took a 24-hour break before redoubling the effort – basically, establishing persistence on the Patient Zero machine, putting a pin in it, and circling back with a fresh plan of attack the next day. Initial Access | T1189 - Drive-by Compromise On Day 1 of the attack, an end-user device was linked by a ChatGPT search for Dynamics 365 to a reputable web property that is believed to have been compromised at the time with a ClickFix lure. The end user was seeking a legitimate software appli
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: 2608-volatility-interlock
  - Published: 2026-08-04T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/2608-volatility-interlock
  - Summary: <p>Multiple legitimate DFIR tools abused by GOLD EMBRACE double-extortion specialists</p> Categories: Threat Research

### Cluster 2654cf7196 — score 8

- Title: Agents vs. agents: how we triage HackerOne reports for $2 each, 85% as well as a human
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-08-04T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/ai-vulnerability-triage-bug-bounty-hackerone
- Fetch status: ok
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
LLMs made it cheap to flood bug bounty programs with submissions. Here's how Elastic built an AI triage agent that matches human decisions 85% of the time, including the architecture, threat model and calibration against 3,300 real reports
```

#### Full body

```
4 August 2026 • Ioannis Kakavas Agents vs. agents: how we triage HackerOne reports for $2 each, 85% as well as a human LLMs made it cheap to flood bug bounty programs with submissions. Here's how Elastic built an AI triage agent that matches human decisions 85% of the time, including the architecture, threat model and calibration against 3,300 real reports 15 min read Generative AI , Internals Large language models (LLMs) made it trivially cheap to generate vulnerability reports. In the first half of 2026 alone, our HackerOne bug bounty program received over 1,390 reports, more than the full-year totals for 2024 and 2025 combined. Every one of them still requires human attention, so we decided to put agents against agents. If AI can generate reports at near-zero cost, AI should triage them at near-zero cost, too. The system we built agrees with human security engineers 85% of the time, validated against 764 known-outcome reports, with triage rules calibrated iteratively against our full corpus of over 3,300. A typical report costs roughly $2 to triage. It runs an eight-stage analysis pipeline, and then a separate adversarial review independently challenges every conclusion. When reproduction is warranted, findings are reproduced in sandboxed Elastic Stack environments on ephemeral virtual machines (VMs) that self-destruct after 30 minutes. A human still makes the final call on every report. HackerOne runs its own AI-assisted triage at submission time, and we use it as a first gate: Only reports that HackerOne's AI marks as send_to_validation reach our pipeline, so we're not paying to re-triage what HackerOne already handles well. The problem: Triage doesn't scale linearly Bug bounty programs have a structural scaling problem. The cost of submitting a report is near zero, but the cost of triaging one is not. A senior security engineer spends 30 to 60 minutes on a typical report: reading the submission, assessing validity against product-specific context, scoring severity, determining if reproduction is feasible, and often spinning up an environment to verify the claim. Multiply that across hundreds of reports per year, and triage becomes a significant operational cost. At Elastic, our bug bounty program on HackerOne has historically received 600 to 850 reports per year. That number is rising sharply: In the first half of 2026, we saw a huge increase in the number of AI generated reports we receive. The majority of analyst time goes toward reports that will ultimately be closed as informative or not applicable. That was already a challenge before LLMs entered the picture. The 2026 spike is the thesis made concrete: AI lowering the cost of report generation to near zero directly shows up in submission volume, while the signal-to-noise ratio drops. We set out to build an AI agent that could handle the mechanical parts of triage, flag the reports that genuinely need human judgment, and reproduce the rest automatically. AI triage architecture: Two VMs, two skills, one orchestrator The system breaks triage into two compute-isolated phases, each running on a separate ephemeral Google Cloud Platform (GCP) VM. This separation was a deliberate architectural choice, for cost (analysis needs a small machine; reproduction needs a larger one) and for security: The analysis VM never runs untrusted code, and the reproduction VM never needs access to the full report corpus or triage history. Phase 1: Analysis runs on an e2-standard-2 VM (2 vCPU, 8GB RAM). Claude processes the report through an eight-stage assessment pipeline, and then a separate adversarial review skill independently challenges the analysis. There are no Docker containers involved, and the system doesn’t execute any code. The VM shuts down after 30 minutes, regardless of state. Phase 2: Reproduction runs on an e2-standard-4 VM (4 vCPU, 16GB RAM) only when the analysis recommends it. This VM provisions an Elastic Stack via Docker Compose, executes researcher-described steps insi
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Agents vs. agents: how we triage HackerOne reports for $2 each, 85% as well as a human
  - Published: 2026-08-04T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/ai-vulnerability-triage-bug-bounty-hackerone
  - Summary: LLMs made it cheap to flood bug bounty programs with submissions. Here's how Elastic built an AI triage agent that matches human decisions 85% of the time, including the architecture, threat model and calibration against 3,300 real reports

### Cluster 032b6e7e8b — score 8

- Title: SOC case management and detection rule history in Elastic Security
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-08-03T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/soc-case-management-detection-rule-history
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Elastic Security now tracks every detection rule change with one-click rollback and makes case data queryable out of the box, so SOC teams get audit trails and reporting without configuring anything.
```

#### Full body

```
3 August 2026 • Kseniia Ignatovych • Melissa Burpo SOC case management and detection rule history in Elastic Security Elastic Security now tracks every detection rule change with one-click rollback and makes case data queryable out of the box, so SOC teams get audit trails and reporting without configuring anything. 3 min read Product Updates Elastic Security now tracks every change to a detection rule and lets you roll back to any previous version with one click. The same history log gives compliance teams a timestamped audit trail that's immutable and append-only. Case data is queryable across 3 global indices (down from 12 per space), so SOC managers can build dashboards on closure rates, assignment load, and case volume without configuring anything. A rebuilt template system gives analysts structured, investigation-specific fields at case creation, so the data feeding those dashboards is consistent from the start. Detection rule change history with one-click rollback Detection rules change constantly. Analysts add exceptions, engineers tune them, detection logic shifts to adapt to new threats. Until now, that history was gone the moment it happened. If a reliable rule stopped firing, there was no built-in way to see what changed, who changed it, or when, which is a debugging problem and a compliance problem in one. In 9.5, Detection Rules History Management ships as GA. A History section on the rule details page shows a complete, chronological log of every saved rule state: who made the change, when, and the revision number. From there, you can preview any historical revision, compare it to the previous version, and restore it with a single click. The log is immutable and append-only, and it captures changes made through the UI or the API. Compliance teams get a defensible, timestamped audit trail for ISO 27001, SOC 2, and DORA standards without any manual export or configuration. Detection engineers get a real undo button: no custom scripts, no digging through audit logs. SOC case management: templates and case analytics Cases are where investigations land, but the data inside them has rarely been reliable enough to learn from. Custom fields were limited in type and count. The same fields appeared on every case regardless of what the analyst was investigating. Building dashboards required manual index configuration that most teams never completed, so case data stayed useful in the moment and hard to aggregate at scale. In 9.5, we rebuilt the template system to fix how data goes in and made cases queryable out of the box for everything downstream. Investigation-specific case templates with custom fields Admins can now define templates for specific investigation types. A "Compromised Account" case collects different information than a "Service Outage" case. Admins build templates using a YAML editor with an Actions menu helper and a live preview panel. Analysts pick the right template for their investigation, see only the fields that apply, and fill in what's actually relevant. The previous cap of 10 templates was a ceiling for enterprise SOCs managing phishing, malware, insider threat, compliance audits, and more. That limit is gone, along with the cap on custom fields. Seven new field types are also now available, including: Checkboxes Radio buttons A user picker A date/time picker Any field can be marked required before case closure, so regulated teams can enforce that fields like "Root Cause" or "Closing Reason" get filled in before a case closes. A Field Library lets admins define reusable fields once and apply them across templates. Queryable case analytics on every deployment Cases as Data, Elastic Security's case analytics feature, exposes case activity in dedicated analytics indices so teams can build dashboards tracking case volume, closure rates, time to close, and assignment load, rather than relying on the case UI alone. We shipped Cases as Data as a tech preview in 9.2, but it required manual configuration, wa
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: SOC case management and detection rule history in Elastic Security
  - Published: 2026-08-03T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/soc-case-management-detection-rule-history
  - Summary: Elastic Security now tracks every detection rule change with one-click rollback and makes case data queryable out of the box, so SOC teams get audit trails and reporting without configuring anything.

### Cluster 30fd684148 — score 8

- Title: Elastic goes all-in on Hacker Summer Camp at Black Hat and DEF CON in Las Vegas
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-31T23:59:59+00:00
- Link: https://www.elastic.co/security-labs/elastic-security-black-hat-defcon-2026
- Fetch status: ok
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
Attack Discovery turns raw alerts into validated threats and Elastic Defend closes vulnerable driver gaps as fast as they're disclosed. Watch it all run against real attacks at the booth.
```

#### Full body

```
31 July 2026 • Jackie McGuire Elastic goes all-in on Hacker Summer Camp at Black Hat and DEF CON in Las Vegas Attack Discovery turns raw alerts into validated threats and Elastic Defend closes vulnerable driver gaps as fast as they're disclosed. Watch it all run against real attacks at the booth. 7 min read Product Updates , Detection Engineering At Elastic, we know that the best way to build security tools is to bring them to the community, have security pros use them, and let them tell us what features and functionality matter and why. This year, we’re excited to do this at Black Hat and DEFCON, the weeklong security marathon affectionately known as Hacker Summer Camp. Our smartest technical experts and practitioners will be at Black Hat showing off our latest innovations, sponsoring and hosting events to help security experts and leaders connect, and at DEFCON’s Blue Team Village with our new Capture the Flag challenge to help defenders sharpen their investigation skills. This community-powered innovation is evident in everything we do. Elastic is a security tool built by security users, for security users. We’ve sat in the seat. We’ve worked the queue at 2 a.m. We’ve chased an alert that turned out to be nothing and missed the one that turned out to be everything. What we're continually building and improving is the security operations center (SOC) we wished we'd had back then. This means agents that carry the machine-speed work, leave critical judgment to analysts, and a platform that connects the two. With Elastic, machine speed and human judgment work together in a single loop. Stopping more at the endpoint reduces the number of alerts. Those that remain surface the real threats, and you can validate them before they reach a queue. The work underneath is increasingly automated. Each piece makes the next one lighter, and none of it asks you to hand judgment over to a black box. Alert Zero: From alert queue to validated threats Every SOC is chasing a queue worked down to what actually matters, the SOC's version of “inbox zero.” When we built our suite of tools, our goal was Alert Zero , a state that always felt out of reach. It’s a goal that teams move toward, with agents and analysts working together. It doesn’t mean zero alerts or replacing the analysts. How Attack Discovery investigates alerts like an analyst Attack Discovery has always pulled related alerts together into a single view of an attack. Now it goes further, working through them the way a human analyst would: Threat-hunts raw events beyond the initial alerts. Checks entity risk for the users and hosts involved. Corroborates findings across other data sources. Classifies the event as a validated attack. Your team gets a short list of validated attacks to work, instead of a wall of raw alerts to triage. Closing detection gaps with auto-drafted rules When Attack Discovery finds something that your rules missed, it drafts a detection rule to close the gap and hands it to an analyst to approve, helping to make the entire workflow more efficient and to reduce the source of false positives. Security teams need the how, not just the what , and Attack Discovery shows its work, so you can see how it got to each answer and recommended action. Every step of the reasoning is visible, so an analyst knows why an alert became an attack. You can run it however fits your team, whether you kick it off yourself or set a recurring cadence. You can even trigger it from Elastic Workflows. A separate alert analysis workflow addresses the volume from the other side, differentiating between likely false and true positives, so analysts lose fewer hours to low-fidelity alerts, and leaving Attack Discovery a cleaner set to investigate. Elastic Defend endpoint protection: vulnerable driver coverage and Windows on ARM Fewer alerts reach the queue when more threats are stopped on the device, so prevention starts at the endpoint. Vulnerable driver coverage that keeps pace with disclosure E
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Elastic goes all-in on Hacker Summer Camp at Black Hat and DEF CON in Las Vegas
  - Published: 2026-07-31T23:59:59+00:00
  - Link: https://www.elastic.co/security-labs/elastic-security-black-hat-defcon-2026
  - Summary: Attack Discovery turns raw alerts into validated threats and Elastic Defend closes vulnerable driver gaps as fast as they're disclosed. Watch it all run against real attacks at the booth.

### Cluster a90be9d647 — score 8

- Title: Alert Zero: AI-driven alert triage and attack investigation for the agentic SOC
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-31T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/agentic-soc-alert-triage-alertzero
- Fetch status: ok
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
Elastic Security 9.5 gives SOC teams AI that handles first-pass alert triage and investigation, so analysts can get back to threat hunting and detection engineering instead of working through queue noise.
```

#### Full body

```
31 July 2026 • David Elgut Alert Zero: AI-driven alert triage and attack investigation for the agentic SOC Elastic Security 9.5 gives SOC teams AI that handles first-pass alert triage and investigation, so analysts can get back to threat hunting and detection engineering instead of working through queue noise. 10 min read Product Updates , Generative AI It's 9 a.m. Monday, the start of your shift. You begin the day like any other Monday: You open the queue, and the wall of alerts is already waiting. New alerts land between 9:05 and 9:10 a.m., while you close yesterday’s. You're already drowning, and you haven’t even had a chance to refill your coffee. You know that you won’t be able to get to things that really need prioritization. Threat hunting stays deferred, and detection engineering waits. Incident response practice never quite starts. This is the default security operations center (SOC) day for a lot of teams, and that probably includes yours. The concept of Alert Zero addresses this problem. It doesn’t mean that the analysts' queue will always remain at zero; new alerts will always come in, and some will still need a human in the loop to review and do deeper investigations. The goal is to keep that queue from dictating the analyst’s day. Instead of walking into a wall of alerts, the team starts with a smaller set of work that genuinely needs attention, giving analysts more time to hunt, tune rules, and investigate the threats that matter most. Alert Zero is about moving toward that kind of shift, and Elastic Security 9.5 gives teams practical tools to do it. With 9.5, Elastic is bringing together three pieces that can move your SOC closer to Alert Zero without requiring you to build and maintain a complex agent architecture yourself: The Security alert analysis workflow helps separate predictable false-positive noise from alerts that deserve attention. Attack Discovery investigates the alerts worth pursuing and turns them into grounded attack narratives. Elastic Workflows provides the automation layer that brings these capabilities into the playbooks your team already trusts. You choose where to start and how much to automate. You also choose where a human still needs to approve the next step. That’s what an agentic SOC should look like in practice: agents handling more of the repetitive work, while analysts stay in control and the queue keeps moving closer to zero. Suggested flow What is Alert Zero, and how does it reduce SOC alert fatigue? Alert Zero is a state that your SOC works toward over time, and 9.5 ships the pieces that make real progress toward making this practical. It isn’t a feature that you simply turn on. Most teams already automate some alert handling, whether that’s through playbooks or another automation method, but the hardest and most expensive work is usually what remains: true positives, unclear cases, and groups of related alerts that need human judgment. That’s where queues grow and analysts burn out. It’s also where gaps in your detections are easiest to miss. Getting closer to Alert Zero changes what a security analyst’s shift can feel like. Senior analysts can spend more time investigating real risk instead of repeatedly gathering host, user, and alert context that the platform can collect for them. The queue gets shorter without turning false positives into incidents, and detection engineers can use lessons from real investigations to improve coverage. That’s the flow that every team wants and the one that the queue usually keeps out of reach. None of this means handing the SOC over to autopilot. Analysts still make the decisions that matter. This is what we can’t stress enough. We want you to be making decisions on the things that actually matter, not automating your critical thinking away. Agents help with the first pass of triage and investigation, and you decide how much autonomy they receive. Process still matters, but Elastic Security 9.5 gives teams more practical tools for making tha
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Alert Zero: AI-driven alert triage and attack investigation for the agentic SOC
  - Published: 2026-07-31T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/agentic-soc-alert-triage-alertzero
  - Summary: Elastic Security 9.5 gives SOC teams AI that handles first-pass alert triage and investigation, so analysts can get back to threat hunting and detection engineering instead of working through queue noise.

### Cluster cf618761a2 — score 8

- Title: TP-Link patches Omada ZTP flaws allowing hackers to breach networks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-04T22:18:20+00:00
- Link: https://www.bleepingcomputer.com/news/security/tp-link-patches-omada-ztp-flaws-allowing-hackers-to-breach-networks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2025-15544, CVE-2025-7850, CVE-2025-7851, CVE-2025-9289, CVE-2025-9293
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2025-7850, CVE-2025-7851, CVE-2025-9289, CVE-2025-9293, CVE-2025-15544
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
TP-Link has patched 15 vulnerabilities in the zero-touch provisioning (ZTP) mechanism of its Omada network devices that could be chained with previously disclosed flaws to achieve remote code execution (RCE). [...]
```

#### Full body

```
TP-Link patches Omada ZTP flaws allowing hackers to breach networks By Bill Toulas August 4, 2026 06:18 PM 0 TP-Link has patched 15 vulnerabilities in the zero-touch provisioning (ZTP) mechanism of its Omada network devices that could be chained with previously disclosed flaws to achieve remote code execution (RCE). The flaws were uncovered by Forescout’s Vedere Labs researchers, who published the full details at the Black Hat USA security conference earlier today. Omada is TP-Link’s business networking product line that includes Wi-Fi access points, Ethernet and PoE switches, internet gateways, and VPN routers. They are typically used by small to medium-sized businesses, although TP-Link also markets pro-grade deployments for enterprises. ZTP is a way to deploy network devices without manually configuring each one on-site, allowing an IT team or managed service provider (MSP) to prepare everything remotely based on a predetermined configuration. Omada deployment diagram Source: Forescout Some of the 15 flaws Forescout discovered also impact various TP-Link products and services, such as IP cameras, smart home IoT devices, mobile applications, and cloud accounts. The issues include hard-coded cryptographic keys, information disclosure, remote code execution, device hijacking and spoofing, client-side code execution, and interception or compromise of encrypted communications. Forescout says attackers could combine the new flaws with two previously disclosed command-injection vulnerabilities to compromise Omada’s chain of trust and infiltrate networks. “The vulnerabilities fall into four impact categories: client-side code execution, information disclosure, device hijacking and spoofing, and compromise of encrypted communications,” Forescout explains . “Combined with two previously disclosed CVEs (CVE-2025-7850 and CVE-2025-7851), these flaws enable concrete attacks that let attackers infiltrate networks through controllers and client devices.” TP-Link’s advisory lists 15 newly disclosed flaws, of which 11 received the following identifiers: CVE-2025-9289 through CVE-2025-9293 CVE-2025-15544 CVE-2025-15627 through CVE-2025-15631 The remaining four findings did not receive a tracking number. They concern device adoption based only on knowing the serial number, default credentials used during initial adoption, predictable serial numbers, and files made available via unauthenticated temporary download links. In one attack scenario Forescout described, a remote attacker could enumerate predictable device serial numbers to obtain MAC addresses and identify devices awaiting adoption. The attacker could then impersonate one of those devices, exploit a race condition during cloud adoption, and authenticate using default credentials. This would cause the controller to disclose the device configuration, including a cleartext username, an unsalted MD5 password hash, and potentially VPN keys. The attacker could also inject JavaScript into the controller’s administrative interface to phish an administrator and steal their cloud-controller credentials. Having stolen the credentials, the attacker can then reconfigure managed devices, create VPN tunnels into the internal network, and exploit previously disclosed command-injection flaws to compromise network equipment. Overview of the race condition attack Source: Forescout The flaws affect Omada Controllers, Gateways, Switches, Access Points, OLT platforms, Cloud services, and TP-Link mobile applications. Forescout reports identifying over 1,800 internet-accessible Omada controllers, despite such deployments generally not being intended for direct internet exposure. As for the Android applications, Omada and Omada Guard have 1.1 downloads on Google Play, while TP-Link apps collectively have 3 to 7 million active accounts. Users are advised to visit TP-Link’s Omada download portal to source the latest firmware images for their device model. Additionally, it is recommended to use strong, unique a
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: TP-Link patches Omada ZTP flaws allowing hackers to breach networks
  - Published: 2026-08-04T22:18:20+00:00
  - Link: https://www.bleepingcomputer.com/news/security/tp-link-patches-omada-ztp-flaws-allowing-hackers-to-breach-networks/
  - Summary: TP-Link has patched 15 vulnerabilities in the zero-touch provisioning (ZTP) mechanism of its Omada network devices that could be chained with previously disclosed flaws to achieve remote code execution (RCE). [...]

### Cluster 097b1c162f — score 8

- Title: Prolific ransomware group behind SonicWall zero-day attacks
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-08-04T15:20:06+00:00
- Link: https://cyberscoop.com/inc-ransomware-sonicwall-zero-day-attacks/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: SonicWall

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, data_breach, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: SonicWall
- cve_ids: CVE-2026-15409, CVE-2026-15410
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach, apt_espionage, active_exploitation
- affected_industries: government
- affected_products: SonicWall
- cve_ids: CVE-2026-15409, CVE-2026-15410
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
INC ransomware wasn’t the first group to exploit the zero-days, but it’s been the most assertive and effective in chaining both vulnerabilities to steal and encrypt data for extortion. The post Prolific ransomware group behind SonicWall zero-day attacks appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Researchers said INC ransomware, one of the most active ransomware groups globally, has been the main attacker exploiting a pair of SonicWall zero-days soon after they were disclosed last month. The prolific ransomware-as-a-service operation wasn’t the first group to exploit the flaws, which were actively exploited for three weeks before the vendor disclosed and patched the defects July 14, but it has been the most assertive and concerning group to target and chain both vulnerabilities together for full access. “Since public disclosure, INC ransomware has emerged as the most commonly named threat actor actively weaponizing this vulnerability chain,” Brett Deroche, director of incident response at Rapid7, told CyberScoop. “While Inc is the name driving the post-disclosure wave, we can’t attribute the full body of exploitation to INC specifically.” SonicWall did not respond to a request for comment. Advertisement The SonicWall vulnerabilities — CVE-2026-15409 and CVE-2026-15410 — are the latest in a series of security issues confronting the vendor’s customers, including actively exploited zero-days, previously disclosed defects , and an attack last year that allowed a state-sponsored threat group to steal the firewall configurations of every SonicWall customer . Just last week, Huntress researchers spotted an attack spree that compromised 30 SonicWall customers in less than two days. Ransomware groups have taken a special interest in SonicWall. Ten of the 17 SonicWall defects added to the Cybersecurity and Infrastructure Security Agency’s known exploited vulnerabilities (KEV) catalog since late 2021 are known to be used in ransomware campaigns. INC ransomware, which has claimed nearly 900 victims across 71 countries since it was first discovered three years ago, is just the latest financially-motivated group to target SonicWall customers. Researchers haven’t determined how many organizations have been impacted by the latest SonicWall zero-days, including attacks linked to INC ransomware. Advertisement “Attribution here isn’t a single clean answer. The earliest exploitation we observed, beginning June 22, traced back to common hosted infrastructure, though those attacks were largely unsuccessful,” Deroche said. “INC’s confirmed activity that we’ve observed came after public disclosure, using different infrastructure and moving from initial access to ransomware deployment in short order. That’s a meaningfully different operational tempo and skill level than what we saw pre-disclosure,” he added. Deroche said Rapid7 has successfully prevented data theft and encryption in the majority of recent cases, yet noted ransomware was deployed in at least one case the security vendor observed. Yet, there could be other attacks outside the purview of Rapid7’s telemetry. INC ransomware has listed multiple new alleged victims on its data leak site, including organizations and government agencies in Australia, the United States, the United Arab Emirates, Colombia and Switzerland, Resecurity said in a blog post Saturday. The company said it has aided several victims with incident response, and learned multiple victims received emails and phone calls from alleged hackers who pressured them to engage in negotiations. Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops SonicWall’s headquarters in Milpitas, California. (Getty Images) SonicWall’s headquarters in Milpitas, California. (Getty Images) Palo Alto Networks headquarters in Silicon Valley; Palo Alto Networks, Inc. is an American multinational cyber security company. (Getty Images) Latest Podcasts What the Section 702 lapse means for cybersecurity Why Cybersecurity is at the heart of the US-China AI race A builder’s view of the AI arms race What the post-quantum executive order means for CISOs Government AISI, OpenAI report more
```

#### Corroborating sources (2)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Prolific ransomware group behind SonicWall zero-day attacks
  - Published: 2026-08-04T15:20:06+00:00
  - Link: https://cyberscoop.com/inc-ransomware-sonicwall-zero-day-attacks/
  - Summary: INC ransomware wasn’t the first group to exploit the zero-days, but it’s been the most assertive and effective in chaining both vulnerabilities to steal and encrypt data for extortion. The post Prolific ransomware group behind SonicWall zero-day attacks appeared first on CyberScoop .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: INC Ransomware Emerges as Dominant Actor Exploiting SonicWall SMA 1000 Flaws
  - Published: 2026-08-03T16:15:13+00:00
  - Link: https://thehackernews.com/2026/08/inc-ransomware-emerges-as-dominant.html
  - Summary: The INC Ransomware operation has emerged as the "dominant threat actor" exploiting the recently disclosed security flaws in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances. In a report published over the weekend, Resecurity said it observed the INC Ransomware accelerating its activity since the beginning of August 2026, listing multiple victims on its data leak site. Per

### Cluster d8000d9d61 — score 8

- Title: New OVSwrap Linux Kernel Flaw Lets Local Users Gain Root via Open vSwitch
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-05T11:43:27+00:00
- Link: https://thehackernews.com/2026/08/new-ovswrap-linux-kernel-flaw-lets.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-64531

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-64531
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-64531
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A memory corruption flaw in the Linux kernel's Open vSwitch datapath gives ordinary local users a path to root on a broad set of default-configured distributions, and a public exploit ships with pre-built records for roughly 800 kernel builds. The vulnerability, tracked as CVE-2026-64531 (CVSS score: 7.8) and codenamed OVSwrap by its discoverer, was disclosed by security researcher Asim
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New OVSwrap Linux Kernel Flaw Lets Local Users Gain Root via Open vSwitch
  - Published: 2026-08-05T11:43:27+00:00
  - Link: https://thehackernews.com/2026/08/new-ovswrap-linux-kernel-flaw-lets.html
  - Summary: A memory corruption flaw in the Linux kernel's Open vSwitch datapath gives ordinary local users a path to root on a broad set of default-configured distributions, and a public exploit ships with pre-built records for roughly 800 kernel builds. The vulnerability, tracked as CVE-2026-64531 (CVSS score: 7.8) and codenamed OVSwrap by its discoverer, was disclosed by security researcher Asim

### Cluster f0d6d20493 — score 8

- Title: QuickFox Supply Chain Attack Delivers FDMTP Backdoor via Trojanized Windows Installer
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-05T05:47:19+00:00
- Link: https://thehackernews.com/2026/08/quickfox-supply-chain-attack-delivers.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, web_shell_backdoor
- affected_products: Fortinet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, web_shell_backdoor
- affected_products: Fortinet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cybersecurity researchers have disclosed what has been described as a "long-standing supply chain attack" on QuickFox, a virtual private network (VPN) and network acceleration tool designed for overseas Chinese users. According to Fortinet FortiGuard Labs, the supply chain attack has been ongoing since at least August 2025 and involves a trojanized version of the application to deliver FDMTP, a
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: QuickFox Supply Chain Attack Delivers FDMTP Backdoor via Trojanized Windows Installer
  - Published: 2026-08-05T05:47:19+00:00
  - Link: https://thehackernews.com/2026/08/quickfox-supply-chain-attack-delivers.html
  - Summary: Cybersecurity researchers have disclosed what has been described as a "long-standing supply chain attack" on QuickFox, a virtual private network (VPN) and network acceleration tool designed for overseas Chinese users. According to Fortinet FortiGuard Labs, the supply chain attack has been ongoing since at least August 2025 and involves a trojanized version of the application to deliver FDMTP, a

### Cluster 9a554b7f81 — score 8

- Title: HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-31T16:39:31+00:00
- Link: https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, web_shell_backdoor
- affected_industries: legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, web_shell_backdoor
- affected_industries: legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Cybersecurity researchers have shed light on a previously undocumented Go-based loader framework called HollowFrame and a Rust-based malware family tracked as Matryoshka. According to Blackpoint Cyber, the intrusion sequence begins with a spear-phishing message containing a link to an encrypted archive, which holds a Windows Shortcut (LNK). Executing the file triggers a multi-stage chain that
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm
  - Published: 2026-07-31T16:39:31+00:00
  - Link: https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
  - Summary: Cybersecurity researchers have shed light on a previously undocumented Go-based loader framework called HollowFrame and a Rust-based malware family tracked as Matryoshka. According to Blackpoint Cyber, the intrusion sequence begins with a spear-phishing message containing a link to an encrypted archive, which holds a Windows Shortcut (LNK). Executing the file triggers a multi-stage chain that

### Cluster 272846cbef — score 8

- Title: Paperclip AI Flaws Let Unauthenticated Attackers Run Commands
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-08-05T14:30:00+00:00
- Link: https://www.infosecurity-magazine.com/news/paperclip-ai-vulnerabilities-rce/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
3 Paperclip flaws exposed data & allowed unauthenticated command execution in two deployment modes
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Paperclip AI Flaws Let Unauthenticated Attackers Run Commands
  - Published: 2026-08-05T14:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/paperclip-ai-vulnerabilities-rce/
  - Summary: 3 Paperclip flaws exposed data & allowed unauthenticated command execution in two deployment modes

### Cluster 02097b7a9a — score 8

- Title: UK’s Police National Legal Database Reveals Data Breach
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-08-04T08:40:00+00:00
- Link: https://www.infosecurity-magazine.com/news/uks-police-national-legal-database/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The UK’s Police National Legal Database and Ask the Police service have been breached
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: UK’s Police National Legal Database Reveals Data Breach
  - Published: 2026-08-04T08:40:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/uks-police-national-legal-database/
  - Summary: The UK’s Police National Legal Database and Ask the Police service have been breached

### Cluster 4bf27bba6f — score 8

- Title: Chinese Hacker Uses DeepSeek AI to Orchestrate Vulnerability Exploits
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-31T15:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/chinese-hacker-deepseek-ai/
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
A Chinese-speaking threat actor has been using DeepSeek’s AI models to orchestrate cyber-attacks targeting Asian organizations
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Chinese Hacker Uses DeepSeek AI to Orchestrate Vulnerability Exploits
  - Published: 2026-07-31T15:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/chinese-hacker-deepseek-ai/
  - Summary: A Chinese-speaking threat actor has been using DeepSeek’s AI models to orchestrate cyber-attacks targeting Asian organizations

### Cluster e0762dc924 — score 8

- Title: New Linux Bridge STP Vulnerability
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-08-05T09:04:29+00:00
- Link: https://www.reddit.com/r/netsec/comments/1vg20wg/new_linux_bridge_stp_vulnerability/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: Linux kernel

#### Cluster taxonomy (union across members)
- affected_products: Linux kernel
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- affected_products: Linux kernel
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
A use-after-free vulnerability in the Linux kernel bridge (net/bridge) Spanning Tree Protocol (STP) implementation. A bridge that is administratively down while kernel STP is enabled, together with a port driven into the LEARNING state, arms periodic STP timers without an IFF_UP guard. The teardown path taken by dellink never synchronously deletes those timers, so the backing net_device (which embeds struct net bridge as private data) is freed with a timer list still queued on a per-CPU timer base. The result is a slab use-after-free in the kmalloc-cg-8k cache. submitted by /u/SSDisclosure [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: New Linux Bridge STP Vulnerability
  - Published: 2026-08-05T09:04:29+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vg20wg/new_linux_bridge_stp_vulnerability/
  - Summary: A use-after-free vulnerability in the Linux kernel bridge (net/bridge) Spanning Tree Protocol (STP) implementation. A bridge that is administratively down while kernel STP is enabled, together with a port driven into the LEARNING state, arms periodic STP timers without an IFF_UP guard. The teardown path taken by dellink never synchronously deletes those timers, so the backing net_device (which embeds struct net bridge as private data) is freed with a timer list still queued on a per-CPU timer base. The result is a slab use-after-free in the kmalloc-cg-8k cache. submitted by /u/SSDisclosure [link] [comments]
