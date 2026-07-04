# PHANTOMSignal Briefing Packet

- Generated: 2026-07-04T10:18:41.611472+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 77
- Total items in window: 321
- Total clusters raw: 144
- Total clusters in packet: 59
- Dropped low score: 85
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

- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
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
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 3
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 8
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 1
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 0
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 3
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
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 1
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 3
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
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
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 20
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 18
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 24
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
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
- **Reddit r/msp** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/msp/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/sysadmin** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/sysadmin/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
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
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 23
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 11
- **tl;dr sec** (practitioner_analysis)
  - URL: https://tldrsec.com/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Embrace the Red** (ai_security_agentic_risk)
  - URL: https://embracethered.com/blog/index.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
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

### ShinyHunters: ransomware extortion
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 4
- Article count: 5
- Cohesion: 0.233
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, zero_day, phishing_social_eng, data_breach, active_exploitation
  - actor_attribution: ShinyHunters
  - affected_industries: financial_services
  - cve_ids: CVE-2026-35273
  - urgency_signals: zero_day, preauth_unauth
- Cluster IDs: 3db35f97c6, 498473218f, 57ef1249ed, a36f6c9249
- Links:
  - https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html
  - https://research.checkpoint.com/2026/29th-june-threat-intelligence-report-2/
  - https://www.infosecurity-magazine.com/news/nissan-oracle-peoplesoft-zero-day/
  - https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/
  - https://www.securityweek.com/medtronic-data-breach-impacts-3-8-million-people/

### ransomware extortion targeting Apple iOS/macOS
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 4
- Article count: 6
- Cohesion: 0.225
- Shared strong signals: Apple iOS/macOS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - affected_industries: financial_services
  - affected_products: Apple iOS/macOS
  - cve_ids: CVE-2026-48558
  - urgency_signals: preauth_unauth
- Cluster IDs: 7de9036f43, de6119ec2c, 6c76262a4a, 083a4a03d5
- Links:
  - https://thehackernews.com/2026/06/attackers-exploit-simplehelp-cve-2026.html
  - https://www.darkreading.com/cyberattacks-data-breaches/djinn-stealer-targets-cloud-ai-credentials
  - https://isc.sans.edu/diary/rss/33114
  - https://www.infosecurity-magazine.com/news/clickfix-cybercriminals-favorite/
  - https://www.securityweek.com/new-citrixbleed-vulnerability-exploited-immediately-after-public-disclosure/
  - https://www.infosecurity-magazine.com/news/simplehelp-rmm-vulnerability/

### Citrix exploitation (CVE-2026-8451)
- Anchor signal: Citrix
- Theme key: citrix
- Cluster count: 4
- Article count: 5
- Cohesion: 0.338
- Shared strong signals: Citrix
- Member CVEs: CVE-2026-8451
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, ransomware_extortion
  - affected_products: Citrix
  - cve_ids: CVE-2025-5777, CVE-2026-3055, CVE-2026-8451
  - urgency_signals: preauth_unauth
- Cluster IDs: 3e07d24a57, 5b50b4b7b2, ce59bc14b1, 6c76262a4a
- Links:
  - https://labs.watchtowr.com/citrixbleed-to-infinity-and-beyond-citrix-netscaler-pre-auth-memory-overread-cve-2026-8451/
  - https://www.reddit.com/r/netsec/comments/1ujzc5y/citrixbleed_to_infinity_and_beyond_citrix/
  - https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html
  - https://cyberscoop.com/citrix-netscaler-flaw-cve-2026-8451-citrixbleed/
  - https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html
  - https://www.securityweek.com/new-citrixbleed-vulnerability-exploited-immediately-after-public-disclosure/

### Scattered Spider: ransomware extortion
- Anchor signal: Scattered Spider
- Theme key: scattered-spider
- Cluster count: 4
- Article count: 4
- Cohesion: 0.317
- Shared strong signals: Scattered Spider
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, data_breach, phishing_social_eng, zero_day
  - actor_attribution: Scattered Spider
  - affected_industries: financial_services
  - urgency_signals: zero_day
- Cluster IDs: 57ef1249ed, 6c76262a4a, 31e5b2aa9f, af46e29c96
- Links:
  - https://www.infosecurity-magazine.com/news/nissan-oracle-peoplesoft-zero-day/
  - https://www.securityweek.com/new-citrixbleed-vulnerability-exploited-immediately-after-public-disclosure/
  - https://www.infosecurity-magazine.com/news/insurance-giant-aflac-data-breach/
  - https://www.infosecurity-magazine.com/news/russian-hackers-destructive-jaguar/

### CVE-2025-3248 exploitation activity
- Anchor signal: CVE-2025-3248
- Theme key: cve-2025-3248
- Cluster count: 3
- Article count: 3
- Cohesion: 0.639
- Shared strong signals: CVE-2025-3248
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - affected_industries: financial_services
  - cve_ids: CVE-2025-3248, CVE-2021-29441
- Cluster IDs: db017396fb, 728fb2c9de, a1f4dc8406
- Links:
  - https://webflow.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion
  - https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
  - https://www.securityweek.com/agentic-ai-used-to-conduct-ransomware-attack-via-langflow/

### Palo Alto Networks active exploitation
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 3
- Article count: 3
- Cohesion: 0.22
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, active_exploitation
  - affected_industries: critical_infrastructure, government
  - affected_products: Palo Alto Networks
  - urgency_signals: actively_exploited
- Cluster IDs: e4a3ada988, 5b50b4b7b2, 4541afab04
- Links:
  - https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/
  - https://cyberscoop.com/citrix-netscaler-flaw-cve-2026-8451-citrixbleed/
  - https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html

### phishing social eng targeting Android
- Anchor signal: Android
- Theme key: android
- Cluster count: 3
- Article count: 6
- Cohesion: 0.212
- Shared strong signals: Android
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng
  - affected_industries: financial_services, government
  - affected_products: Android
- Cluster IDs: 93502a2013, 4541afab04, 5bbda948e4
- Links:
  - https://research.checkpoint.com/2026/browser-only-ransomware-from-llm-hallucinations-to-a-practical-attack-technique/
  - https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/
  - https://thehackernews.com/2026/06/new-bioshocking-attack-tricks-ai.html
  - https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html
  - https://www.recordedfuture.com/research/nexus-tag182-disseminates-markirat

### Ubiquiti UniFi exploitation (5 CVEs)
- Anchor signal: Ubiquiti UniFi
- Theme key: ubiquiti-unifi
- Cluster count: 2
- Article count: 2
- Cohesion: 0.5
- Shared strong signals: Ubiquiti UniFi
- Member CVEs: CVE-2026-20245, CVE-2026-34908, CVE-2026-34909, CVE-2026-41947, CVE-2026-41948
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, phishing_social_eng, zero_day, data_breach, active_exploitation
  - affected_products: Ubiquiti UniFi
  - tools_used: Microsoft 365
  - cve_ids: CVE-2026-20245, CVE-2026-34908, CVE-2026-34909, CVE-2026-41947, CVE-2026-41948
  - urgency_signals: zero_day, preauth_unauth
- Cluster IDs: 498473218f, f2b3bd6ba4
- Links:
  - https://research.checkpoint.com/2026/29th-june-threat-intelligence-report-2/
  - https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/

### Microsoft 365 vulnerability activity
- Anchor signal: Microsoft 365
- Theme key: microsoft-365
- Cluster count: 2
- Article count: 6
- Cohesion: 0.2
- Shared strong signals: Microsoft 365
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft 365
- Cluster IDs: d52b9991a8, 5472a00679
- Links:
  - https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
  - https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html
  - https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
  - https://www.huntress.com/blog/hacker-tactics-2026-dark-web-playbook
  - https://www.bleepingcomputer.com/news/security/artoken-phaas-exposes-eviltokens-microsoft-365-phishing-toolkit/

### ransomware extortion targeting Ivanti
- Anchor signal: Ivanti
- Theme key: ivanti
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: Ivanti
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, zero_day
  - affected_industries: government
  - affected_products: Ivanti
  - urgency_signals: zero_day
- Cluster IDs: d52b9991a8, 083a4a03d5
- Links:
  - https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
  - https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html
  - https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
  - https://www.infosecurity-magazine.com/news/simplehelp-rmm-vulnerability/

### zero day targeting Gogs
- Anchor signal: Gogs
- Theme key: gogs
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: Gogs
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day
  - affected_industries: government
  - affected_products: Gogs
  - urgency_signals: zero_day
- Cluster IDs: d52b9991a8, a56bf79002
- Links:
  - https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
  - https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html
  - https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
  - https://www.infosecurity-magazine.com/news/researcher-exploitarium-exploits/

### Microsoft SharePoint active exploitation
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: Microsoft SharePoint
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, active_exploitation
  - affected_products: Microsoft SharePoint
  - urgency_signals: actively_exploited
- Cluster IDs: d52b9991a8, 6c76262a4a
- Links:
  - https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
  - https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html
  - https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
  - https://www.securityweek.com/new-citrixbleed-vulnerability-exploited-immediately-after-public-disclosure/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (0)

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2025-12101 + Citrix (cluster 3e07d24a57, first observation: True)
- Pair: CVE-2025-5777 + Citrix (cluster 3e07d24a57, first observation: True)
- Pair: CVE-2026-3055 + Citrix (cluster 3e07d24a57, first observation: True)
- Pair: CVE-2026-8451 + Citrix (cluster 3e07d24a57, first observation: True)
- Pair: CVE-2025-61882 + Cl0p (cluster 3db35f97c6, first observation: True)
- Pair: CVE-2025-61882 + ShinyHunters (cluster 3db35f97c6, first observation: True)
- Pair: CVE-2026-35273 + Cl0p (cluster 3db35f97c6, first observation: True)
- Pair: CVE-2026-46817 + Cl0p (cluster 3db35f97c6, first observation: True)
- Pair: CVE-2026-46817 + ShinyHunters (cluster 3db35f97c6, first observation: True)
- Pair: CVE-2026-45659 + Gogs (cluster d52b9991a8, first observation: True)
- Pair: CVE-2026-45659 + Ivanti (cluster d52b9991a8, first observation: True)
- Pair: CVE-2026-45659 + Microsoft 365 (cluster d52b9991a8, first observation: True)
- Pair: CVE-2025-55182 + TeamPCP (cluster f851217332, first observation: True)
- Pair: CVE-2025-55182 + Kubernetes (cluster f851217332, first observation: True)
- Pair: CVE-2026-35616 + Fortinet (cluster 6a5eaa4b15, first observation: True)

### Drift (2)
- **Scattered Spider** (cluster 57ef1249ed)
  - New industries: education
  - New products: Salesforce
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: AWS, Apple iOS/macOS, Microsoft SharePoint
- **MuddyWater** (cluster 083a4a03d5)
  - New industries: (none)
  - New products: Apple iOS/macOS, Fortinet, Ivanti
  - Prior top industries: critical_infrastructure, financial_services, government
  - Prior top products: Android, GitHub, Microsoft 365

### Persistence (10)
- actor_attribution: ShinyHunters (weeks observed: 5, cluster 3db35f97c6)
- cve_ids: CVE-2026-20245 (weeks observed: 5, cluster 498473218f)
- cve_ids: CVE-2026-35273 (weeks observed: 4, cluster 3db35f97c6)
- actor_attribution: TeamPCP (weeks observed: 4, cluster f851217332)
- cve_ids: CVE-2026-33017 (weeks observed: 3, cluster aadab8aa23)
- actor_attribution: Cl0p (weeks observed: 3, cluster 3db35f97c6)
- cve_ids: CVE-2026-45659 (weeks observed: 3, cluster d52b9991a8)
- cve_ids: CVE-2026-48558 (weeks observed: 3, cluster 7de9036f43)
- actor_attribution: Scattered Spider (weeks observed: 3, cluster 57ef1249ed)
- actor_attribution: MuddyWater (weeks observed: 3, cluster 083a4a03d5)

### Tier inversion (0)

## Clusters

### Cluster 99561905ef — score 48

- Title: Enterprise Tech In, Shell Out (Progress Kemp LoadMaster Uninitialized Heap to Pre-Auth RCE CVE-2026-8037)
- Source: watchTowr Labs (offensive_vulnerability_research)
- Published: 2026-06-29T19:24:54+00:00
- Link: https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: CVE-2026-8037

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-8037
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-8037
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Welcome back to another watchTowr Labs blog post. This time, we're looking at Progress Kemp LoadMaster, a load balancer that sits at the edge of a lot of enterprise networks. Edge appliances have a habit of becoming the way in rather than the thing keeping people out, and
```

#### Full body

```
Welcome back to another watchTowr Labs blog post. This time, we're looking at Progress Kemp LoadMaster, a load balancer that sits at the edge of a lot of enterprise networks. Edge appliances have a habit of becoming the way in rather than the thing keeping people out, and CVE-2026-8037 keeps that streak alive: a pre-authentication Remote Code Execution vulnerability accessible to anyone who can access the API. So, in probably a predictable turn of events, we're back doing what we do best. As always, watchTowr clients gain industry-first access to our research days before publication to validate their exposure, accompanied by Active Defense capabilities to autonomously mitigate exposure. This research is a glimpse into the capabilities that power our Preemptive Exposure Management solution and get organizations ahead of inevitable in-the-wild exploitation: the watchTowr Platform. What Is A Kemp LoadMaster, and What Is CVE-2026-8037? Produced by Progress (of MoveIT fame), Kemp LoadMaster is a load balancer and application delivery controller (ADC) that distributes incoming network traffic across multiple servers to keep applications available, responsive, and scalable. Typically, beyond basic load balancing, it provides Layer 4 and Layer 7 traffic management, SSL/TLS offloading, content switching, health checking, and a built-in web application firewall (WAF) to protect against common threats. Why would you use it? Well, Progress has us covered here: On June 4th, Progress published an advisory about a “Command Injection Remote Code Execution Vulnerability” in Kemp LoadMaster, exploitable by the friendliest of unauthenticated attackers. The vulnerability affects the following versions, when the API is enabled: Kemp LoadMaster: GA v7.2.63.1 and older Kemp LoadMaster: LTSF v7.2.54.17 and older Setting The Scene To fuel our analysis today, we compared the following versions following our normal ‘what the hell has changed’ process: 7.2.63.1 (Vulnerable) 7.2.63.2 (Different) Let’s Dive In We started our work on the 7.2.63.1 version, diffing the access executable against the 7.2.63.2: While the changes are minimal, let’s look at the unpatched version in a little more detail: _BYTE *__fastcall escape_quotes(const char *user_input) // vulnerable version { const char *v1; // rbx char *v2; // rdx _BYTE *result; // rax char v4; // cl _BYTE *i; // rdx v1 = user_input; if ( !user_input ) return nullptr; v2 = strchr(user_input, '\''); result = user_input; if ( v2 ) // [1] If the user input contains a single quote, allocate a new buffer for its escaped representation { result = malloc(3 * (strlen(user_input) + 1) + 29); // [2] if ( result ) { v4 = *user_input; if ( *user_input ) { for ( i = result; ; ++i ) { if ( v4 == "'" ) { *i = '\''; i[1] = '\\'; i[2] = '\''; i += 3; } *i = *v1++; v4 = *v1; if ( !*v1 ) break; } } } } return result; } Initially, we assumed this would be a straightforward command injection. However, the diff showed only a single modified function: escape_quotes() . Even stranger, the patch wasn't escaping any additional characters. That immediately raised a question: Is it really that simple? Before we answer that, let's look at how escape_quotes() actually works. The job of escape_quotes() is simple. It takes a string and makes it safe to place inside a single-quoted shell argument. For example: validuser -u '<user-controlled-input>' It does this by escaping single quotes, and nothing else. because if single quotes are not escaped, someone can use an extra single quote to break out and inject additional commands. Let's look at the implementation. At [1] , escape_quotes() calls strchr() to determine whether the supplied input contains a single quote. If strchr() returns NULL , there are no quotes to escape. In that case, the function neither allocates a new buffer nor modifies the input. Instead, it simply returns the original pointer supplied by the caller: escape_quotes("ABCD") -> ABCD // same char pointer returned If our i
```

#### Corroborating sources (3)

- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: Enterprise Tech In, Shell Out (Progress Kemp LoadMaster Uninitialized Heap to Pre-Auth RCE CVE-2026-8037)
  - Published: 2026-06-29T19:24:54+00:00
  - Link: https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/
  - Summary: Welcome back to another watchTowr Labs blog post. This time, we're looking at Progress Kemp LoadMaster, a load balancer that sits at the edge of a lot of enterprise networks. Edge appliances have a habit of becoming the way in rather than the thing keeping people out, and
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Progress Kemp LoadMaster Pre-Auth RCE Flaw Faces Active Exploitation Attempts
  - Published: 2026-07-01T13:56:18+00:00
  - Link: https://thehackernews.com/2026/07/latest-progress-kemp-loadmaster-pre.html
  - Summary: A recently disclosed critical security flaw impacting Progress Kemp LoadMaster is seeing active exploitation attempts, according to an advisory from eSentire's Threat Response Unit (TRU). The Canadian cybersecurity company said it identified exploitation attempts targeting CVE-2026-8037 (CVSS score: 9.6), an operating system (OS) command injection flaw that could be exploited to achieve
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Enterprise Tech In, Shell Out (Progress Kemp LoadMaster Uninitialized Heap to Pre-Auth RCE CVE-2026-8037) - watchTowr Labs
  - Published: 2026-06-29T19:27:02+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1uj2a4w/enterprise_tech_in_shell_out_progress_kemp/
  - Summary: submitted by /u/dx7r__ [link] [comments]

### Cluster aadab8aa23 — score 45

- Title: Langflow RCE Actively Exploited to Deploy Cryptominers on AI Infrastructure
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-01T18:21:25+00:00
- Link: https://orca.security/resources/blog/langflow-rce-vulnerability-cve-2026-33017/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-33017

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- affected_industries: financial_services, government
- cve_ids: CVE-2026-33017
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-33017
- urgency_signals: actively_exploited, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A critical vulnerability (CVE-2026-33017, CVSS 9.8) was disclosed affecting Langflow, a widely used open-source AI application builder, allowing attackers to execute arbitrary code on the server via a single unauthenticated HTTP request. Due to the potential for full system compromise, data theft, and lateral movement across enterprise networks, immediate patching is required. About CVE-2026-33017 The […]
```

#### Full body

```
Table of contents About CVE-2026-33017 Affected Systems Risk Impact How Orca Can Help A critical vulnerability ( CVE-2026-33017 , CVSS 9.8) was disclosed affecting Langflow, a widely used open-source AI application builder, allowing attackers to execute arbitrary code on the server via a single unauthenticated HTTP request. Due to the potential for full system compromise, data theft, and lateral movement across enterprise networks, immediate patching is required. About CVE-2026-33017 The issue originates from Langflow’s public flow-building API endpoint (/api/v1/build_public_tmp/{flow_id}/flow), where a lack of input sanitization and sandboxing for user-supplied flow definitions leads to arbitrary Python code execution on the server. By sending a specially crafted POST request containing malicious Python code in a node definition, attackers can gain full remote code execution without any authentication or user interaction, potentially compromising the entire host and any connected cloud infrastructure . An active campaign exploiting this vulnerability was observed by Trend Micro researchers over a 19-day window in spring 2026. Attackers weaponized the flaw within 20 hours of the advisory’s publication, before any public proof-of-concept existed. The attack chain delivers “lambsys,” a Go-based binary that kills 39 rival cryptominer processes, disables security controls including AppArmor, SELinux, UFW, and iptables, wipes system logs, and deploys a customized XMRig Monero miner with geo-aware pool selection. The malware also harvests environment variables, .env files, database credentials, and API keys from compromised hosts. Affected Systems The following components are affected: Langflow, all versions up to and including 1.8.2. Langflow has over 145,000 GitHub stars and is widely deployed in AI/ML pipeline infrastructure across enterprise and cloud environments, particularly when flow-building endpoints are exposed to the internet. Approximately 7,000 Langflow servers were found internet-accessible at the time of discovery. Other frameworks or services relying on Langflow as a backend may also be impacted. Users should upgrade to Langflow version 1.9.0 or later immediately. Notably, version 1.8.2 was widely reported as patched but remains vulnerable according to JFrog Security Research. Organizations that cannot deploy 1.9.0 immediately should install the nightly build (1.9.0.dev18 or later) as an interim fix. All API keys, database credentials, and SSH keys on any previously exposed instances should be rotated, and teams should monitor for outbound connections to 83.142.209[.]214 and the presence of the “lambsys” binary or unexpected cron entries. Risk Impact At the time of writing, working exploits are actively used in the wild, and the vulnerability has been added to CISA’s Known Exploited Vulnerabilities catalog with a federal remediation deadline. No authentication is required to exploit this issue. The severity and ease of exploitation make this vulnerability extremely high risk, especially in internet-facing deployments. Successful exploitation could allow attackers to execute arbitrary code on the server, steal credentials and sensitive data from environment variables and configuration files, and laterally move through enterprise networks using harvested SSH keys, leading to service disruption, data exposure, or full infrastructure compromise. How Orca Can Help Orca enables customers to quickly identify assets running vulnerable Langflow versions, understand their exposure in context , including internet accessibility, runtime reachability, and asset criticality, and prioritize remediation based on real risk rather than CVSS alone. Orca’s platform highlights affected assets directly in the newItem view, helping security teams focus on the most critical remediation paths first Table of contents About CVE-2026-33017 Affected Systems Risk Impact How Orca Can Help Related articles Research FortiBleed Campaign Harvests 110
```

#### Corroborating sources (2)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Langflow RCE Actively Exploited to Deploy Cryptominers on AI Infrastructure
  - Published: 2026-07-01T18:21:25+00:00
  - Link: https://orca.security/resources/blog/langflow-rce-vulnerability-cve-2026-33017/
  - Summary: A critical vulnerability (CVE-2026-33017, CVSS 9.8) was disclosed affecting Langflow, a widely used open-source AI application builder, allowing attackers to execute arbitrary code on the server via a single unauthenticated HTTP request. Due to the potential for full system compromise, data theft, and lateral movement across enterprise networks, immediate patching is required. About CVE-2026-33017 The […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Langflow RCE Exploited to Deploy Monero Miner on Exposed AI App Endpoints
  - Published: 2026-06-30T15:47:20+00:00
  - Link: https://thehackernews.com/2026/06/langflow-rce-exploited-to-deploy-monero.html
  - Summary: Threat actors are continuing to exploit a critical Langflow vulnerability as part of fresh attacks designed to deliver a Monero cryptocurrency miner. The activity has been found to weaponize CVE-2026-33017 (CVSS score: 9.3), an unauthenticated remote code execution (RCE) vulnerability in Langflow, indicating threat actors are scanning and targeting exposed artificial intelligence (AI)

### Cluster e9c83acbdf — score 34

- Title: Weekly Metasploit Update: Modules for SMB-to-Meterpreter, Peyara Remote Mouse RCE exploit, and more
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-03T22:11:22+00:00
- Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-07-03-2026/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
It's Time to Upgrade Your SMB Session This week, Metasploit contributor Dean Welch has added an SMB to Meterpreter session upgrade module. It uses PsExec to facilitate the upgrade. Users can load the module with use windows/manage/smb_to_meterpreter and specify the session number they wish to upgrade. This functionality is also available with the command sessions -u <session_id> . This work is part of an overarching effort to enable a variety of session types to be upgraded to Meterpreter when possible. New module content (3) Peyara Remote Mouse 1.0.1 Unauthenticated Remote Code Execution Author: tmrswrr Type: Exploit Pull request: #21491 contributed by capture0x Path: windows/misc/peyara_remote_mouse_rce Description: Adds an exploit module for Peyara Remote Mouse v1.0.1 unauthenticated RCE. Linux Execute Command Authors: bcoles bcoles@gmail.com and modexp Type: Payload (Single) Pull request: #21239 contributed by bcoles Path: linux/loongarch64/exec Description: Adds a new linux/loonga
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Weekly Metasploit Update: Modules for SMB-to-Meterpreter, Peyara Remote Mouse RCE exploit, and more
  - Published: 2026-07-03T22:11:22+00:00
  - Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-07-03-2026/
  - Summary: It's Time to Upgrade Your SMB Session This week, Metasploit contributor Dean Welch has added an SMB to Meterpreter session upgrade module. It uses PsExec to facilitate the upgrade. Users can load the module with use windows/manage/smb_to_meterpreter and specify the session number they wish to upgrade. This functionality is also available with the command sessions -u <session_id> . This work is part of an overarching effort to enable a variety of session types to be upgraded to Meterpreter when possible. New module content (3) Peyara Remote Mouse 1.0.1 Unauthenticated Remote Code Execution Author: tmrswrr Type: Exploit Pull request: #21491 contributed by capture0x Path: windows/misc/peyara_remote_mouse_rce Description: Adds an exploit module for Peyara Remote Mouse v1.0.1 unauthenticated RCE. Linux Execute Command Authors: bcoles bcoles@gmail.com and modexp Type: Payload (Single) Pull request: #21239 contributed by bcoles Path: linux/loongarch64/exec Description: Adds a new linux/loonga

### Cluster 3e07d24a57 — score 29

- Title: CitrixBleed To Infinity And Beyond (Citrix NetScaler Pre-Auth Memory Overread CVE-2026-8451)
- Source: watchTowr Labs (offensive_vulnerability_research)
- Published: 2026-06-30T19:35:58+00:00
- Link: https://labs.watchtowr.com/citrixbleed-to-infinity-and-beyond-citrix-netscaler-pre-auth-memory-overread-cve-2026-8451/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-8451, Citrix

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, zero_day
- affected_products: Citrix
- cve_ids: CVE-2025-12101, CVE-2025-5777, CVE-2026-3055, CVE-2026-8451
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: Citrix
- cve_ids: CVE-2026-8451, CVE-2025-5777, CVE-2025-12101, CVE-2026-3055
- urgency_signals: zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Well, well, well - once again, the cat has dragged us in and spat us out. Today, we find ourselves questioning the reality we sit within. Must it be so predictable, and why us? “But watchTowr, what do you mean?” Well, if you’re here, you likely fit
```

#### Full body

```
Well, well, well - once again, the cat has dragged us in and spat us out. Today, we find ourselves questioning the reality we sit within. Must it be so predictable, and why us? “But watchTowr, what do you mean?” Well, if you’re here, you likely fit into one of the following categories: A dear reader, A group therapy accomplice A Groundhog Day fan club member Why? Because we once again find ourselves talking about Citrix NetScalers. Yes, that’s right, we’ve found another excuse to create memes and mock promise rings. For those that don’t start violently wretching when the phrase “Citrix NetScaler” is uttered, we have another word to whisper: “CitrixBleed”. As many know, the term CitrixBleed now refers to not a single vulnerability, but an entire class of Memory Disclosure-esque vulnerabilities in Citrix NetScaler devices, many of which have played roles in breaches and incidents in recent memory. For those new to this trauma, the following prior reading may be of interest: How Much More Must We Bleed? - Citrix NetScaler Memory Disclosure (CitrixBleed 2 CVE-2025-5777) Is It CitrixBleed4? Well, No. Is It Good? Also, No. (Citrix NetScaler Memory Leak & RXSS CVE-2025-12101) The Sequels Are Never As Good, But We're Still In Pain (Citrix NetScaler CVE-2026-3055 Memory Overread) Please, We Beg, Just One Weekend Free Of Appliances (Citrix NetScaler CVE-2026-3055 Memory Overread Part 2) "We told you so”, we want to scream. Huh? Why? Because, we have constantly reiterated our concern that the Memory Disclosure-esque class of vulnerability appears to be endemic within Citrix NetScaler devices - to the point where we’ve now found further instances either b y accident or while analyzing and reproducing another instance of the same vulnerability class in the same appliance a mere few months ago. Yes, that’s right - today, a Secure By Design promise ring pledge commitment hall-of-famer is back to haunt us as Citrix has now publicly disclosed the zero-day Memory Disclosure vulnerability we reported in March 2026. We’ve given up counting the numbers, and so we’ve decided to call this vulnerability “CitrixBleed To Infinity And Beyond”: Referencing what we wrote previously, because it is demonstrably evergreen: However, what should be of concern is the bigger picture - the trend, which is very clearly suggesting that memory management continues to appear fragile within Citrix NetScaler appliances, to the extent that even accidentally misconfiguring an appliance can lead to the disclosure of leaked memory. It feels like we are playing catch with a highly-sensitive gun that continues to harm innocent bystanders - within, once again, what many will consider a highly-critical appliance and security control. Will we see another memory leak vulnerability in Citrix NetScaler? We have no idea. But if we were to meme… As always, watchTowr clients gain industry-first access to our research days (in this case, months ) before publication to validate their exposure, accompanied by Active Defense capabilities to autonomously mitigate exposure. This research is a glimpse into the capabilities that power our Preemptive Exposure Management solution and get organizations ahead of inevitable in-the-wild exploitation: the watchTowr Platform. What Is Citrix NetScaler and NetScaler Gateway? Citrix NetScaler (formally rebranded, then un-rebranded, in the way that only enterprise networking vendors can truly pull off) is a family of application delivery controllers and VPN gateway appliances found in virtually every large enterprise network on the planet. NetScaler handles load balancing, SSL offloading, authentication, and remote access - and NetScaler Gateway specifically serves as the front door for thousands of organizations' remote access infrastructure. It is, in other words, exactly the kind of product we love to look at, while also being a natural disaster. What Is CVE-2026-8451? Citrix eloquently describes CVE-2026-8451 as: “Insufficient input validation leadi
```

#### Corroborating sources (3)

- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: CitrixBleed To Infinity And Beyond (Citrix NetScaler Pre-Auth Memory Overread CVE-2026-8451)
  - Published: 2026-06-30T19:35:58+00:00
  - Link: https://labs.watchtowr.com/citrixbleed-to-infinity-and-beyond-citrix-netscaler-pre-auth-memory-overread-cve-2026-8451/
  - Summary: Well, well, well - once again, the cat has dragged us in and spat us out. Today, we find ourselves questioning the reality we sit within. Must it be so predictable, and why us? “But watchTowr, what do you mean?” Well, if you’re here, you likely fit
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: CitrixBleed To Infinity And Beyond (Citrix NetScaler Pre-Auth Memory Overread CVE-2026-8451) - watchTowr Labs
  - Published: 2026-06-30T19:40:48+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1ujzc5y/citrixbleed_to_infinity_and_beyond_citrix/
  - Summary: submitted by /u/dx7r__ [link] [comments]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Citrix Patches Six NetScaler Flaws Allowing File Read and Denial-of-Service
  - Published: 2026-07-01T03:54:22+00:00
  - Link: https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html
  - Summary: Citrix on Tuesday released security updates to address multiple flaws in NetScaler ADC (formerly Citrix ADC) and NetScaler Gateway (formerly Citrix Gateway) that could be exploited by an attacker to facilitate arbitrary file reads or trigger a denial-of-service (DoS) condition. The vulnerabilities are listed below - CVE-2026-8451 (CVSS score: 8.8) - An insufficient input validation

### Cluster 3db35f97c6 — score 26

- Title: Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited in the Wild
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-30T05:04:06+00:00
- Link: https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-46817

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- actor_attribution: Cl0p, ShinyHunters
- affected_industries: financial_services
- cve_ids: CVE-2025-61882, CVE-2026-35273, CVE-2026-46817
- urgency_signals: actively_exploited, no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- actor_attribution: ShinyHunters, Cl0p
- affected_industries: financial_services
- cve_ids: CVE-2026-46817, CVE-2025-61882, CVE-2026-35273
- urgency_signals: actively_exploited, zero_day, preauth_unauth, no_patch_yet, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
A critical security flaw impacting Oracle E-Business Suite has come under active exploitation in the wild, according to Defused Cyber. The vulnerability, tracked as CVE-2026-46817 (CVSS score: 9.8), refers to an improper privilege management and authentication flaw in Oracle Payments that could be abused to take over susceptible instances. "Easily exploitable vulnerability allows
```

#### Full body

```
Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited in the Wild  Ravie Lakshmanan  Jun 30, 2026 Vulnerability / Enterprise Software A critical security flaw impacting Oracle E-Business Suite has come under active exploitation in the wild, according to Defused Cyber. The vulnerability, tracked as CVE-2026-46817 (CVSS score: 9.8), refers to an improper privilege management and authentication flaw in Oracle Payments that could be abused to take over susceptible instances. "Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Payments," according to a description of the flaw in the NIST National Vulnerability Database (NVD). "Successful attacks of this vulnerability can result in the takeover of Oracle Payments." The shortcoming impacts versions from 12.2.3 through 12.2.15. Patches for the flaw were shipped by Oracle as part of its Critical Security Patch Update last month. CVE-2026-46817 has since come under active exploitation, with Defused Cyber noting on Monday that "over the weekend, we observed an actor exploiting the vulnerability on our Oracle E-Business honeypots," adding "this vulnerability has no known previous exploitation and no public PoC [proof-of-concept] code exists." That said, there are currently no details available on how the security flaw is being exploited, who is behind them, and if it's part of a broader opportunistic or targeted campaign aimed at unpatched systems. Late last year, another critical flaw in the same product ( CVE-2025-61882 , CVSS score: 9.8) was weaponized by threat actors linked to the Cl0p ransomware operation, with early attacks launched as far back as August 2025. Earlier this month, the company addressed a critical missing authentication zero-day vulnerability in PeopleSoft Suite ( CVE-2026-35273 , CVSS score: 9.8) that was actively exploited in ShinyHunters (aka SHADOW-AETHER-015) data theft and extortion attacks. "The notable property of this vulnerability is not its impact, but its near-total lack of observability," Trend Micro said . "The final code-execution step runs through Java's XMLDecoder inside the application server’s own Java virtual machine (JVM), fires on a restart rather than on the inbound request, and needs no child process and no outbound beacon to succeed. A defender watching the usual places sees a quiet system." Automaker Nissan has since acknowledged that it was among those impacted, stating it was the victim of a break-in that involved the exploitation of the PeopleSoft flaw, potentially exposing payroll records, bank details, Social Security numbers, and other personal and financial data belong to its employees in the U.S., Canada, Mexico, and Brazil. "What stood out was that CVE-2026-35273 isn't just another trivial, easy-to-exploit single-request vulnerability," Jake Knott, principal security researcher at watchTowr, said in a statement. "The attack chain is considerably more involved, combining multiple vulnerabilities to plant a malicious file that doesn’t execute immediately but waits until the server restarts." "Where we would normally see simple bugs, this is a chain of multiple vulnerabilities, suggestive of a threat actor with genuine knowledge of and familiarity with the underlying codebase, and the ability to develop targeted capabilities against it." Knott also pointed out that threat actors are exploiting vulnerabilities faster than ever before, urging organizations to assume compromise and activate incident response processes to determine whether access was obtained before patches were applied, what was accessed, and whether persistence was established. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Authentication bypass , cybersecurity , data theft , Enterprise Software , oracle , privilege escalation , Threat Intelligence , Vulnerability ⚡ Top St
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited in the Wild
  - Published: 2026-06-30T05:04:06+00:00
  - Link: https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html
  - Summary: A critical security flaw impacting Oracle E-Business Suite has come under active exploitation in the wild, according to Defused Cyber. The vulnerability, tracked as CVE-2026-46817 (CVSS score: 9.8), refers to an improper privilege management and authentication flaw in Oracle Payments that could be abused to take over susceptible instances. "Easily exploitable vulnerability allows

### Cluster d52b9991a8 — score 24

- Title: CISA: Microsoft SharePoint RCE flaw now actively exploited
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-02T10:52:43+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Gogs, Ivanti, Microsoft 365, Microsoft SharePoint
- cve_ids: CVE-2026-45659
- urgency_signals: actively_exploited, no_patch_yet, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_industries: government
- affected_products: Microsoft SharePoint, Gogs, Ivanti
- cve_ids: CVE-2026-45659
- urgency_signals: actively_exploited, zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
CISA warned on Wednesday that attackers have begun exploiting a high-severity Microsoft SharePoint remote code execution vulnerability patched in May. [...]
```

#### Full body

```
CISA: Microsoft SharePoint RCE flaw now actively exploited By Sergiu Gatlan July 2, 2026 06:52 AM 0 The U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned on Wednesday that attackers have begun exploiting a high-severity Microsoft SharePoint remote code execution vulnerability. Tracked as CVE-2026-45659 , this security flaw stems from a deserialization of untrusted data weakness, and it allows attackers with low privileges to execute arbitrary code on unpatched SharePoint servers in low-complexity attacks that don't require user interaction. "Any authenticated attacker could trigger this vulnerability. It does not require admin or other elevated privileges. In a network-based attack, an authenticated attacker, who has a minimum of Site Member permissions (PR:L), could execute code remotely on the SharePoint Server," Microsoft explains . "The attack vector is Network (AV:N) because this vulnerability is remotely exploitable and can be exploited from the internet. The attack complexity is Low (AC:L) because an attacker does not require significant prior knowledge of the system and can achieve repeatable success with the payload against the vulnerable component." Microsoft released security updates for SharePoint Enterprise Server 2016, SharePoint Server 2019, and SharePoint Server Subscription Edition to address this vulnerability on May 21, saying that the CVE had been accidentally omitted from the May 2026 Security Updates. Internet security watchdog group Shadowserver is currently tracking over 10,000 SharePoint servers exposed online. However, there is no information regarding how many of these devices have already been secured against ongoing CVE-2026-45659 attacks. SharePoint servers exposed online (Shadowserver) ​With the April 2026 Patch Tuesday, Microsoft addressed another SharePoint vulnerability that was exploited in zero-day attacks . On Wednesday, CISA added the vulnerability to its Known Exploited Vulnerabilities Catalog (KEV), ordering Federal Civilian Executive Branch (FCEB) agencies to secure their servers by Saturday, as required by Binding Operational Directive (BOD) 26-04. BOD 26-04 was issued last month and requires U.S. federal agencies to prioritize patching based on whether the security flaw is included in CISA's KEV catalog, whether exploitation can be automated for large-scale attacks, whether the asset is publicly exposed online, and whether successful exploitation grants attackers partial or total control of the targeted device. "This type of vulnerability is a frequent attack vector for malicious cyber actors and poses significant risks to the federal enterprise," the cybersecurity agency warned yesterday . "Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines." Since 2021, CISA has tagged 11 Microsoft SharePoint vulnerabilities that have been abused in the wild, with seven of them also exploited in ransomware attacks. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: CISA sets urgent deadline to fix Cisco flaw exploited in attacks CISA orders feds to patch max severity Joomla plugin flaw by Friday CISA gives feds three days to patch Ivanti flaw exploited as zero-day CISA orders feds to patch Gogs RCE flaw exploited in zero-day attacks Palo Alto Networks firewall zero-day exploited for nearly a month
```

#### Corroborating sources (3)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA: Microsoft SharePoint RCE flaw now actively exploited
  - Published: 2026-07-02T10:52:43+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/
  - Summary: CISA warned on Wednesday that attackers have begun exploiting a high-severity Microsoft SharePoint remote code execution vulnerability patched in May. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation
  - Published: 2026-07-02T05:46:45+00:00
  - Link: https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a high-severity flaw impacting Microsoft SharePoint Server to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerability, tracked as CVE-2026-45659 (CVSS score: 8.8), is a case of remote code execution arising from the deserialization of untrusted data. The issue
- **Cisco Talos** (threat_research_primary)
  - Title: ARToken: Inside an EvilTokens affiliate panel targeting Microsoft 365
  - Published: 2026-07-01T10:00:38+00:00
  - Link: https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
  - Summary: Talos has identified "ARToken," a phishing-as-a-service platform that targets Microsoft 365. The ARToken panel exposes 80+ API endpoints for device code phishing, Primary Refresh Token persistence, email access, BEC operations, and SharePoint exfiltration.

### Cluster 58774f7de3 — score 20

- Title: Inside the Advisory Database and what happens when vulnerability volume breaks records
- Source: GitHub Security Lab (offensive_vulnerability_research)
- Published: 2026-06-29T16:10:20+00:00
- Link: https://github.blog/security/supply-chain-security/inside-the-advisory-database-and-what-happens-when-vulnerability-volume-breaks-records/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- affected_products: GitHub, PyPI, npm
- urgency_signals: poc_available
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- affected_products: GitHub, npm, PyPI
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
The GitHub Advisory Database is processing more vulnerability reports than ever before. Here's what's driving the surge, how we're responding, and how the community can help. The post Inside the Advisory Database and what happens when vulnerability volume breaks records appeared first on The GitHub Blog .
```

#### Full body

```
Madison Ficorilli · @taladrane June 29, 2026 | Updated July 1, 2026 | 10 minutes Share: In May 2026, the GitHub Advisory Database published 1,560 reviewed advisories —more than five times our typical monthly output and the highest in its history. And it still wasn’t enough to keep up. Over the past few months, the vulnerability ecosystem has shifted in a fundamental way. Input across private vulnerability reports, repository advisories, and CVE requests has increased simultaneously, pushing the entire system to a new operating scale. This blog builds on an ongoing GitHub community discussion tracking the evolving nature of vulnerability reporting, as well as PVR and Advisory Database roadmap developments. A recurring theme in that thread is the downstream impact of platform changes on advisory curation and data quality. This aligns with GitHub’s broader shift toward emphasizing quality and shared responsibility in vulnerability reporting, which in turn directly shapes how advisory data must be curated and maintained. TL;DR Review times for new advisories are longer because vulnerability volume and complexity have increased significantly. Advisory quality has not changed: reviewed advisories are still human-validated, and existing alerts continue to function normally. If you want to help, focus on three things: submit complete vulnerability data, coordinate closely with maintainers and researchers, and request CVEs only when there is a clear intention to publish. Record output and unprecedented input May was not a one-time spike. From March through May, we sustained more than 6,000 advisory decisions per month. This included updating existing advisories, publishing new advisories, and reviewing inbound advisories, and exceeded any prior three-month peak. At the same time, inflow accelerated across every source: Private vulnerability reports across the platform increased from ~550/week in January to more than 3,000/week for most of May. Repository advisories scaled from ~650/week to more than 5,000/week. GitHub CNA CVE requests reached almost 4,000 in May alone , nearly 10x year –over year. The CVE program has already published 30,000+ CVEs in 2026. More than 1.7 million total repositories have enabled private vulnerability reporting. This is not a localized surge. It reflects structural change across the vulnerability disclosure ecosystem. The impact Since mid-April, due to this surge, we have not consistently met our internal goals for publication. Processing times extended first to about a week, then to multiple weeks for a meaningful share. Longer publication times can increase exposure windows. We take that seriously, and timeliness is a core part of the value this database provides. What’s still working Our data pipelines and publishing infrastructure have continued to operate through this period. Imports are running, data integrity is intact, and published advisories are accurate. Advisories that reach reviewed status today meet the same quality standard as before. CVE assignment quality has remained strong. Our assignment rate has held between 91–94% through the entire surge, consistent with or better than historical norms and showing that there hasn’t been a clear degradation in the requests we receive. The issue is throughput. The system that validates, enriches, and publishes advisory data is functioning; it is now operating beyond the volume and complexity it was designed to handle. The work isn’t uniform Not every security advisory requires the same level of effort. Some arrive well formatted: the advisory details clearly name the affected package and its relevant ecosystem, the version range is documented, and the fix is tagged. A curator can validate and publish these in under a few minutes. But a growing share of incoming advisories require more investigation: Package disambiguation. The advisory details say “foo”, but is that foo on npm, python-foo on PyPI, or the unrelated foo on Maven? When upstream data doesn
```

#### Corroborating sources (3)

- **GitHub Security Lab** (offensive_vulnerability_research)
  - Title: Inside the Advisory Database and what happens when vulnerability volume breaks records
  - Published: 2026-06-29T16:10:20+00:00
  - Link: https://github.blog/security/supply-chain-security/inside-the-advisory-database-and-what-happens-when-vulnerability-volume-breaks-records/
  - Summary: The GitHub Advisory Database is processing more vulnerability reports than ever before. Here's what's driving the surge, how we're responding, and how the community can help. The post Inside the Advisory Database and what happens when vulnerability volume breaks records appeared first on The GitHub Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New ChocoPoC RAT Targets Vulnerability Researchers via Fake PoC Exploit Repos
  - Published: 2026-07-02T07:24:23+00:00
  - Link: https://thehackernews.com/2026/07/new-chocopoc-rat-targets-vulnerability.html
  - Summary: Attackers are hiding a data-stealing trojan inside fake exploit code aimed at the people who hunt bugs for a living. The malware, called ChocoPoC, travels in Python proof-of-concept (PoC) repositories on GitHub that claim to exploit hot new CVEs. Run one, and it quietly lifts your saved passwords, browser cookies, and files, then hands the attacker a shell on your machine. YesWeHack and
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New ChocoPoC malware targets researchers via trojanized PoC exploits
  - Published: 2026-07-01T20:08:13+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-chocopoc-malware-targets-researchers-via-trojanized-poc-exploits/
  - Summary: Multiple weaponized proof-of-concept (PoC) exploits on GitHub were found delivering a Python-based remote access trojan (RAT) named ChocoPoC that can execute commands and steal sensitive data in a campaign believed to target cybersecurity researchers. [...]

### Cluster f851217332 — score 18

- Title: Vect and TeamPCP partner for ransomware campaigns
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-07-02T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/vect-and-teampcp-partner-for-ransomware-campaigns
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: TeamPCP

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- actor_attribution: TeamPCP
- affected_industries: financial_services, government, healthcare
- affected_products: Kubernetes
- cve_ids: CVE-2025-55182
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- actor_attribution: TeamPCP
- affected_industries: healthcare, financial_services, government
- affected_products: Kubernetes
- cve_ids: CVE-2025-55182
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Credentials harvested through supply chain compromises enable large‑scale ransomware deployment Categories: Threat Research Tags: Vect, TeamPCP, Ransomware
```

#### Full body

```
Vect and TeamPCP partner for ransomware campaigns Credentials harvested through supply chain compromises enable large‑scale ransomware deployment Written by Sophos Counter Threat Unit Research Team Threat Research Vect TeamPCP Ransomware Share This Link Copied Counter Threat Unit™ (CTU) researchers investigated two interconnected threat groups known as Vect and TeamPCP. The two groups announced a formal operational partnership in late March 2026 to combine TeamPCP’s credential harvesting and data theft capabilities with Vect’s ransomware deployment infrastructure in a widespread campaign involving supply chain attacks and the extortion of multiple organizations. Vect evolution The Vect ransomware-as-a-service (RaaS) operation first appeared on December 31, 2025, when an account operating under the group's name posted an affiliate recruitment advertisement on Rehub, a prominent Russian-language cybercrime forum. Vect claimed its first victims in January 2026 and then launched Vect 2.0 one month later. The launch of the new version coincided with an affiliate recruitment effort, and Vect claimed on X (formerly Twitter) that they had recruited 60 affiliates, attacked 154 organizations, and received “tens of successful payments” within two months. Vect has demonstrated a willingness to collaborate with other cybercriminals to expand operations. In March, the group announced partnerships with BreachForums and TeamPCP (see Figure 1). Despite declaring that the more than 300,000 BreachForums members would each receive a Vect affiliation key, the number who would actually launch ransomware attacks on Vect’s behalf would likely be substantially lower. TeamPCP (also known as PCPcat, ShellForce, and DeadCatx3) appears to be made up of individuals previously affiliated with The Com , a global confederation of primarily English-speaking cybercriminals. Two victims listed on the Vect data leak site were labeled as victims of the "LiteLLM/Trivy Campaign (TeamPCP)." Figure 1: Vect announcing partnerships with BreachForums and TeamPCP TeamPCP evolution TeamPCP first gained notoriety in December 2025 in connection with the mass exploitation of the React2Shell vulnerability ( CVE-2025-55182 ), a critical (CVSS of 10.0) pre-authentication remote code execution flaw in React Server Components. TeamPCP deployed a worm-driven campaign that leveraged exposed Docker APIs, Kubernetes clusters, Ray dashboards, and Redis servers in conjunction with React2Shell exploitation. The campaign impacted organizations in Canada, Serbia, South Korea, the UAE, and the United States, with victims spanning technology, finance, healthcare, and government sectors. A notable operational signature during this phase was the use of outbound port 666 for almost all network activity. From March through May 2026, TeamPCP made headlines for a series of high-profile supply chain attacks. Figure 2 shows a timeline of attributed attacks. Figure 2: TeamPCP supply chain attacks from March through May 2026 The first of these attacks was on Trivy, an open-source vulnerability scanner that is made by Aqua Security and used by thousands of organizations worldwide. The threat actors reportedly gained a foothold in late February by stealing login credentials from Trivy's development systems. Aqua Security discovered and attempted to mitigate that compromise on March 1, but the cleanup was incomplete and allowed the attackers to quietly retain access. On March 19, they struck at scale — simultaneously tampering with the core Trivy scanner program and its associated automation tools on GitHub and triggering the publication of a poisoned version of the software to official channels. Organizations that downloaded what appeared to be a legitimate security update were actually installing malware. The malicious version silently harvested passwords, cloud credentials, and other sensitive secrets from the systems it ran on, then transmitted that stolen data to attacker-controlled servers. It cont
```

#### Corroborating sources (2)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Vect and TeamPCP partner for ransomware campaigns
  - Published: 2026-07-02T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/vect-and-teampcp-partner-for-ransomware-campaigns
  - Summary: Credentials harvested through supply chain compromises enable large‑scale ransomware deployment Categories: Threat Research Tags: Vect, TeamPCP, Ransomware
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Warning Over “Industrialized” Cyber-Attacks After Ransomware Gang Partners With TeamPCP
  - Published: 2026-07-03T11:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/industrialized-cyberattacks/
  - Summary: Researchers warn that collaboration could lead to “unprecedented” ransomware attacks, as FBI also issues warning

### Cluster 6a5eaa4b15 — score 18

- Title: FortiBleed Campaign Harvests 110M+ Credentials, Fuels Ransomware Operations
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-02T20:55:24+00:00
- Link: https://orca.security/resources/blog/fortibleed-credential-theft-vulnerability/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 5
- Strong signals: CVE-2026-35616, Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, phishing_social_eng, ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: financial_services, manufacturing_industrial
- affected_products: Fortinet
- cve_ids: CVE-2026-35616
- urgency_signals: actively_exploited, critical_cvss, zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft, zero_day, web_shell_backdoor, active_exploitation
- affected_industries: manufacturing_industrial
- affected_products: Fortinet
- cve_ids: CVE-2026-35616
- urgency_signals: actively_exploited, zero_day, critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A critical credential-harvesting campaign dubbed “FortiBleed” has been exposed, systematically targeting over 430,000 FortiGate firewalls worldwide and exploiting CVE-2026-35616 (CVSS 9.1) in FortiClient EMS, enabling attackers to gain admin access, deploy packet sniffers, and fuel ransomware operations at scale. Due to the massive scope and active exploitation, immediate patching and credential rotation are required. Users […]
```

#### Full body

```
A critical credential-harvesting campaign dubbed “FortiBleed” has been exposed, systematically targeting over 430,000 FortiGate firewalls worldwide and exploiting CVE-2026-35616 (CVSS 9.1) in FortiClient EMS, enabling attackers to gain admin access, deploy packet sniffers, and fuel ransomware operations at scale. Due to the massive scope and active exploitation, immediate patching and credential rotation are required. Users should upgrade FortiClient EMS to version 7.4.7 or later, or apply the out-of-band hotfix for 7.4.5 and 7.4.6. All credentials on FortiGate-managed infrastructure should be rotated immediately, including VPN, RADIUS, NTLM, Kerberos, and admin accounts. Organizations should audit FortiGate admin accounts for the unauthorized “adminin” backdoor account, restrict FortiClient EMS port 8013 to trusted IP ranges, enable MFA on all FortiGate administrative interfaces, and hunt for FortigateSniffer indicators of compromise. Known C2 infrastructure (83.138.53.110 and associated Tor exit nodes) should be blocked. About FortiBleed The operation, attributed to a Russian-speaking initial access broker (IAB), scanned the entire internet-facing FortiGate attack surface and achieved admin-level access on 409 targets, with 354 suffering full domain compromise. The attackers deployed a custom Golang packet sniffer called “FortigateSniffer” on approximately 12,000 devices, abusing FortiOS’s native diagnose sniffer packet command to passively intercept authentication traffic across 24 protocols. This approach allowed the operators to harvest RADIUS, NTLM, and Kerberos credentials at scale, amassing over 110 million credentials without triggering traditional intrusion detection. SOCRadar’s Threat Research Unit directly linked the FortiBleed operation to the INC Ransom and Lynx ransomware-as-a-service (RaaS) groups. An operator with access to FortiBleed infrastructure was discovered actively logged into both INC and Lynx ransomware negotiation panels, and victim data overlapped between the campaigns. At least 12 confirmed ransomware deployments with hundreds of encrypted endpoints resulted from FortiBleed-sourced initial access. About CVE-2026-35616 In parallel, CVE-2026-35616 (CVSS 9.1), an improper access control flaw in Fortinet FortiClient EMS versions 7.4.5 and 7.4.6, is being actively exploited in the wild. Arctic Wolf observed attackers exploiting this vulnerability to modify remote access profiles, inject malicious PowerShell into VPN configuration scripts, and deploy the EKZ Stealer infostealer (disguised as “FortiEndpoint_Patch.exe”) across managed endpoint fleets. EKZ Stealer extracts credentials from Chrome, Edge, and Firefox, including bypassing Chromium’s encrypted password storage. CISA added CVE-2026-35616 to its Known Exploited Vulnerabilities catalog on April 6, 2026. No authentication is required to exploit this issue. Affected Systems The following components are affected: FortiGate firewalls (all internet-facing deployments) and FortiClient EMS versions 7.4.5 through 7.4.6. These components are widely deployed across enterprise environments, particularly in manufacturing, technology, and logistics sectors in LATAM and APAC. Organizations using FortiGate-managed VPN or remote access infrastructure are at heightened risk, as credentials may have been passively captured via the sniffer component. Investigators also assess the threat actors may possess an undisclosed Nextcloud zero-day, and SOCRadar discovered artifacts indicating potential targeting of Citrix remote access infrastructure. Risk Impact At the time of writing, FortiBleed is confirmed as an active campaign with at least 12 ransomware deployments traced back to its access brokering, and CVE-2026-35616 has been added to CISA’s KEV catalog confirming active exploitation. The severity, scale, and direct link to ransomware operations make this threat exceptionally high risk, especially for organizations with internet-facing Fortinet infrastructure. Succ
```

#### Corroborating sources (5)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: FortiBleed Campaign Harvests 110M+ Credentials, Fuels Ransomware Operations
  - Published: 2026-07-02T20:55:24+00:00
  - Link: https://orca.security/resources/blog/fortibleed-credential-theft-vulnerability/
  - Summary: A critical credential-harvesting campaign dubbed “FortiBleed” has been exposed, systematically targeting over 430,000 FortiGate firewalls worldwide and exploiting CVE-2026-35616 (CVSS 9.1) in FortiClient EMS, enabling attackers to gain admin access, deploy packet sniffers, and fuel ransomware operations at scale. Due to the massive scope and active exploitation, immediate patching and credential rotation are required. Users […]
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: FortiBleed Campaign Linked to INC, Lynx Ransomware Attacks
  - Published: 2026-07-02T12:34:29+00:00
  - Link: https://www.securityweek.com/fortibleed-campaign-linked-to-inc-lynx-ransomware-attacks/
  - Summary: Researchers say credentials harvested from hundreds of thousands of FortiGate firewalls are being used to facilitate ransomware attacks by the INC and Lynx operations. The post FortiBleed Campaign Linked to INC, Lynx Ransomware Attacks appeared first on SecurityWeek .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: FortiBleed Actors Collaborating With Inc, Lynx Ransomware Gangs
  - Published: 2026-07-02T19:11:33+00:00
  - Link: https://www.darkreading.com/threat-intelligence/fortibleed-actors-inc-lynx-ransomware-gangs
  - Summary: After gaining a foothold in thousands of Fortinet firewalls, the attackers are starting to monetize that access, and are also piling on a Nextcloud zero-day bug.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: FortiBleed credential-theft campaign linked to Lynx ransomware
  - Published: 2026-07-01T21:37:24+00:00
  - Link: https://www.bleepingcomputer.com/news/security/fortibleed-credential-theft-campaign-linked-to-lynx-ransomware/
  - Summary: The massive FortiBleed credential theft campaign has been linked to the INC and Lynx ransomware operations, suggesting the stolen Fortinet credentials were intended to fuel future network intrusions. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: FortiBleed Credential Theft Linked to INC and Lynx Ransomware Operations
  - Published: 2026-07-02T08:00:49+00:00
  - Link: https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html
  - Summary: The recently discovered financially-motivated FortiBleed campaign has been attributed to INC and Lynx ransomware operations, indicating that the verified, stolen credentials were intended for follow-on intrusions. "An operator tied to FortiBleed's infrastructure was found actively working negotiation panels for both groups, tying mass FortiGate credential theft directly to ransomware deployment

### Cluster e4a3ada988 — score 17

- Title: Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector
- Source: Unit 42 (threat_research_primary)
- Published: 2026-07-01T01:00:11+00:00
- Link: https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain
- affected_industries: critical_infrastructure
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng
- affected_industries: critical_infrastructure
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Attackers can exploit LLM domain hallucinations through phantom squatting to target supply chains. Read the analysis to learn more. The post Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector 19 min read Related Products Advanced DNS Security Advanced URL Filtering Advanced WildFire Cloud-Delivered Security Services Code to Cloud Platform Prisma AIRS Unit 42 AI Security Assessment Unit 42 Incident Response By: Keerthiraj Nagaraj Diva-Oriane Marty Beliz Kaleli Oleksii Starov Published: June 30, 2026 Categories: Malware Threat Research Tags: Agentic AI LLMs Malicious Domains Malvertising Phantom Squatting Phishing Slopsquatting Supply chain URL hallucination Share Executive Summary Unit 42 researchers found that large language models (LLMs) consistently hallucinate web domains for legitimate brands. Adversaries are actively weaponizing this vector by registering these nonexistent domains to intercept traffic generated by AI systems. We call this phenomenon phantom squatting, and it poses a significant risk to the software supply chain. Our proactive monitoring of registration for high-priority hallucinated domains yielded real-world detections across multiple sectors. We were able to predict use of these domains from 18–51 days ahead of adversary registration. A standout case reveals an attacker who leveraged an AI coding assistant to build a full phishing kit named Montana Empire. This kit targeted a domain our detection pipeline identified as a high-risk hallucination target 23 days earlier, demonstrating the full cycle from AI-assisted attack development to LLM-hallucinated domain prediction. To detect the risk posed by phantom squatting, we analyzed 913 global brands and executed 685,339 URL queries across multiple configurations of two distinct LLM models. This generated 2.1 million URLs and revealed over 13,229 confirmed malicious URLs. Furthermore, we discovered approximately 250,000 hallucinated domains that remain unregistered, presenting a significant opportunity for adversaries to exploit the software supply chain through preemptive registration. Palo Alto Networks customers are better protected from phantom squatting through the following products and services: Advanced WildFire Advanced URL Filtering and Advanced DNS Security Prisma AIRS Koi Agentic Endpoint Security The Unit 42 AI Security Assessment can help empower safe AI use and development. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics LLM , Agentic AI , Supply Chain Introduction: LLMs as Supply Chain Dependencies The Expanding AI Trust Surface The software supply chain threat landscape is shifting. For decades, supply chain attacks focused on predictable artifacts such as tampered build tools, malicious dependencies and compromised update servers. Defenders built protections around these predictable attack surfaces using package integrity checks, signed binaries and dependency auditing tools. However, this model is becoming less effective. LLMs are no longer peripheral utilities, they are active participants in the software development lifecycle. People consult AI coding assistants for documentation links. In doing so AI agents perform autonomous web research on behalf of developers, then formulate and execute HTTP requests against URLs the models themselves generate. Enterprise continuous integration and continuous delivery (CI/CD) pipelines integrate AI assistants that recommend third-party service endpoints. For example, a developer querying a pipeline assistant to configure a cloud deployment notification might receive a recommended webhook URL such as hxxps[:]//api.build-notifier[.]io/v1/pipeline/events . Such a URL could be entirely fictitious and an adversary could have pre-registered it to intercept automated build telemetry or secrets. In each case, downstream consumers often trust the LLM's output including the URLs it generates, without independent verification. This situation fundamentally alters the attack surface
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector
  - Published: 2026-07-01T01:00:11+00:00
  - Link: https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/
  - Summary: Attackers can exploit LLM domain hallucinations through phantom squatting to target supply chains. Read the analysis to learn more. The post Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector appeared first on Unit 42 .

### Cluster 498473218f — score 17

- Title: 29th June – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-06-29T14:06:59+00:00
- Link: https://research.checkpoint.com/2026/29th-june-threat-intelligence-report-2/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, phishing_social_eng, supply_chain, zero_day
- actor_attribution: ShinyHunters
- affected_industries: financial_services, manufacturing_industrial, telecommunications
- affected_products: Anthropic/Claude, Ubiquiti UniFi
- tools_used: Microsoft 365
- cve_ids: CVE-2026-20245, CVE-2026-34908, CVE-2026-34909, CVE-2026-41947, CVE-2026-41948
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, zero_day, data_breach, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: financial_services, manufacturing_industrial, telecommunications
- affected_products: Ubiquiti UniFi, Anthropic/Claude
- tools_used: Microsoft 365
- cve_ids: CVE-2026-20245, CVE-2026-41947, CVE-2026-41948, CVE-2026-34908, CVE-2026-34909
- urgency_signals: zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 29th June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Polymarket, a large cryptocurrency-based prediction market, has confirmed a supply chain attack after a third-party frontend vendor breach led to malicious JavaScript being injected into its website. Attackers tricked users into approving fraudulent […] The post 29th June – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 29th June – Threat Intelligence Report June 29, 2026 https://research.checkpoint.com/2026/29th-june-threat-intelligence-report-2/ For the latest discoveries in cyber research for the week of 29th June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Polymarket, a large cryptocurrency-based prediction market, has confirmed a supply chain attack after a third-party frontend vendor breach led to malicious JavaScript being injected into its website. Attackers tricked users into approving fraudulent transactions, stealing about $3 million from fewer than 15 accounts, while the backend remained unaffected. KDDI, a Japanese telecom operator, has reported a breach of its ISP email platform after detecting an intrusion on June 17. Up to 14.22 million email addresses and passwords may have been compromised across services from six ISPs, including J:COM and Biglobe. Indian electronics and semiconductor manufacturer Tata Electronics, a supplier to Apple and Tesla, has suffered a cyberattack and data breach. The company said IT systems were affected, while the World Leaks group claimed 630GB of data, including alleged supplier and customer documents. Brazil’s National Civil Defense warning platform, managed by telecom regulator Anatel, has faced a cyberattack that sent a fake “Extreme Alert” to phones across several regions. Officials took the system offline after the message reached users in Paraná, São Paulo, and Rio de Janeiro. The National Association of Insurance Commissioners, a US insurance regulatory standards body, has confirmed a cyberattack after ShinyHunters claimed theft of 3.1TB of data through an Oracle PeopleSoft zero-day. The group claimed access to regulatory filings, production logs, cloud configuration files, and other internal records. AI THREATS Researchers have detailed EvilTokens, an AI-powered phishing-as-a-service operation abusing device-code authentication to steal Microsoft 365 tokens. Huntress observed a 1,380% surge in device-code phishing in early 2026, with AI-generated lures and automated workflows lowering attacker effort. Researchers have crafted a fake AI skill that hijacked more than 26,000 AI agents by abusing trusted marketplaces and Instagram ads in a supply chain attack. The package initially appeared clean, then used attacker-controlled external instructions after approval to trigger data exfiltration across agent platforms. LayerX researchers have demonstrated BioShocking AI, a technique that tricks agentic browsers into bypassing their guardrails. Test cases against ChatGPT Atlas, Perplexity Comet, Claude in Chrome, and other AI browsers showed how game-like prompts could expose credentials and user data. VULNERABILITIES AND PATCHES Cisco has addressed CVE-2026-20245, a high-severity command injection flaw in Catalyst SD-WAN Manager that attackers exploited as a zero-day for months. The flaw allows an administrator to run root commands through a crafted file, affecting on-premises and Cisco-managed cloud deployments. Dify has released version 1.14.2 to fix four vulnerabilities in its open-source AI platform, including critical CVE-2026-41947 and CVE-2026-41948. The flaws could allow unauthenticated access and cross-tenant data exposure, including chat content and uploaded files. Ubiquiti UniFi OS is affected by three flaws, CVE-2026-34908, CVE-2026-34909, and CVE-2026-34910, which are reportedly being exploited against network appliances. The vulnerabilities allow unauthorized changes, file access, and command execution, with exploitation observed in Mirai botnet activity. Check Point IPS provides protection against these threats (Ubiquiti UniFi OS Privilege Escalation (CVE-2026-34908), Ubiquiti UniFi OS Directory Traversal (CVE-2026-34909), Ubiquiti UniFi OS Command Injection (CVE-2026-34910)) Langflow, an open-source AI workflow tool, is reportedly being targeted through exploitation of CVE-2026-55
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 29th June – Threat Intelligence Report
  - Published: 2026-06-29T14:06:59+00:00
  - Link: https://research.checkpoint.com/2026/29th-june-threat-intelligence-report-2/
  - Summary: For the latest discoveries in cyber research for the week of 29th June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Polymarket, a large cryptocurrency-based prediction market, has confirmed a supply chain attack after a third-party frontend vendor breach led to malicious JavaScript being injected into its website. Attackers tricked users into approving fraudulent […] The post 29th June – Threat Intelligence Report appeared first on Check Point Research .

### Cluster 8b38cd09cc — score 16

- Title: It’s 37oC, And All We Can Think About Is ColdFusion (Adobe ColdFusion Security Bulletin APSB26-68 CVE Bonanza)
- Source: watchTowr Labs (offensive_vulnerability_research)
- Published: 2026-07-02T16:38:28+00:00
- Link: https://labs.watchtowr.com/its-37oc-and-all-we-can-think-about-is-coldfusion-adobe-coldfusion-security-bulletin-apsb26-68-cve-bonanza/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-48276, CVE-2026-48277, CVE-2026-48281, CVE-2026-48282, CVE-2026-48316
- content_type: threat_research
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-48276, CVE-2026-48277, CVE-2026-48281, CVE-2026-48316, CVE-2026-48282
- content_type: threat_research
- confidence_tier: tier_1_offensive_research

#### Summary

```
We’re back, melting - we’ve tried shouting, screaming, and throwing things at the Sun, and it is just not working. Before we begin our analysis, we want to be clear - given the number of vulnerabilities fixed (and some not mentioned..), we’ve struggled to have confidence
```

#### Full body

```
We’re back, melting - we’ve tried shouting, screaming, and throwing things at the Sun, and it is just not working. Before we begin our analysis, we want to be clear - given the number of vulnerabilities fixed (and some not mentioned..), we’ve struggled to have confidence in our attribution of “vulnerability <> specific CVE ID”. We’ve performed some informed, uninformed, random guesses - but as usual, please resist the urge to send us emails explaining how awful/wrong we are. We know some of you can’t resist, so please rest assured that we do read them, print them, and frame our favorites each month. Like the individual who emailed us 5 times to tell us that they were older than Telnet. Given that Telnet is newer than SSH (which we replied to tell you (your follow-up emails were caught by our spam filter, sorry)), we knew you were lying to us. As always, watchTowr clients gain industry-first access to our research days before publication to validate their exposure, accompanied by Active Defense capabilities to autonomously mitigate exposure. This research is a glimpse into the capabilities that power our Preemptive Exposure Management solution and get organizations ahead of inevitable in-the-wild exploitation: the watchTowr Platform. What Is An Adobe ColdFusion? Adobe ColdFusion is a rapid web application development platform built around its own scripting language, ColdFusion Markup Language (CFML), which lets developers build dynamic, data-driven websites and applications with relatively little code. It runs on a Java-based server engine that sits between web servers and backend resources - databases, file systems, APIs, and email servers - translating CFML tags and functions into executable logic that generates web content on the fly. What Are We Looking At Today? Well, in typical fashion, on June 30 Adobe released a security advisory covering numerous CVEs affecting Adobe ColdFusion. The following versions were listed as affected (basically, everything..): ColdFusion 2025 (Update 9 and below) ColdFusion 2023 (Update 20 and below) Per the advisory, and repeated here for verbosity, the following vulnerabilities have been resolved: Arbitrary Code Execution - CVE-2026-48276 Arbitrary Code Execution - CVE-2026-48277 Arbitrary Code Execution - CVE-2026-48281 Arbitrary Code Execution - CVE-2026-48316 Arbitrary Code Execution - CVE-2026-48282 Arbitrary Code Execution - CVE-2026-48283 Arbitrary File System Read - CVE-2026-48313 Privilege Escalation - CVE-2026-48315 Arbitrary Code Execution - CVE-2026-48307 Security Feature Bypass - CVE-2026-48285 Privilege Escalation - CVE-2026-48314 Setting The Scene To fuel our analysis today, we compared the following versions following our normal ‘what the hell has changed’ process: 2025.0.0.331385 (Vulnerable) 2025.0.0.331899 (Different) Arbitrary File Write & Read (And More.. CVE-2026-48282 & CVE-2026-48313 (maybe)) For those of you unaware, this isn’t Adobe’s first security advisory. In fact, history shows us that the RDS feature of ColdFusion has been a main character many times, with many of the most recent security patches being focused on resolving vulnerabilities within the RDS module. For those unfamiliar with it, RDS (Remote Development Services) is a ColdFusion feature that allows a developer's IDE, historically ColdFusion Builder, Dreamweaver, or the Eclipse plugin, to interact with a running ColdFusion server. It can browse the filesystem, execute database queries, and assist with debugging, all over HTTP. Under the hood, it is essentially a small RPC protocol. Warning: RDS is not enabled by default. To reach the vulnerability described in this post, RDS must be enabled and, based on our testing, authentication must also be disabled (?) The above is how you do this, and in fairness, Adobe does point out the obvious - not ideal to disable authentication. Now, every RDS request is sent as an HTTP POST to /CFIDE/main/ide.cfm , with an ACTION query parameter selecting the requested oper
```

#### Corroborating sources (1)

- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: It’s 37oC, And All We Can Think About Is ColdFusion (Adobe ColdFusion Security Bulletin APSB26-68 CVE Bonanza)
  - Published: 2026-07-02T16:38:28+00:00
  - Link: https://labs.watchtowr.com/its-37oc-and-all-we-can-think-about-is-coldfusion-adobe-coldfusion-security-bulletin-apsb26-68-cve-bonanza/
  - Summary: We’re back, melting - we’ve tried shouting, screaming, and throwing things at the Sun, and it is just not working. Before we begin our analysis, we want to be clear - given the number of vulnerabilities fixed (and some not mentioned..), we’ve struggled to have confidence

### Cluster abbec23383 — score 16

- Title: Factoring RSA Keys with Many Zeros
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-06-29T16:05:18+00:00
- Link: https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Interesting research on a new class of weak RSA keys: keys with lots of zeros. It turns out that these keys are out in the wild. The badkeys project is an open-source service that checks public keys for known vulnerabilities. While developing this tool, Hanno collected a massive number of real-world keys from public sources, including Certificate Transparency logs, internet-wide TLS and SSH scans, PGP keys, and many others. By searching this dataset for unexpectedly sparse RSA moduli, we uncovered a large number of keys in the wild with the patterns in Figure 1...
```

#### Full body

```
Clive Robinson • June 29, 2026 4:08 PM @ Bruce, ALL, With regards, “The article doesn’t speculate, but I will.” We’ve been through this prior to 2013. With respect to generating certificates on embedded devices such as “network devices”. It’s very difficult to develop entropy on such devices when they are “first out the box” because they have next to no internal entropy and likewise external entropy[1]. Thus there would be a very high chance that all certificates generated on such devices are very closely related. Whilst factoring the multiple of two large primes is assumed to be hard… Finding two or more such multiples that share a prime is in comparison trivial, using a simple “Greatest Common Divisor”(GCD) algorithm, https://www.cryptool.org/en/posts/rsa-sanity-check/ As I noted back when I pointed this out, I assume that part of the NSA budget would go on “buying and testing” all edge of network devices looking for weaknesses in such certificate generating devices” Not technically a “back door” as the NSA did not design or install it. But certainly a nicely exploitable vulnerability almost as good as the one that caused NIST such embarrassment and much to everyone’s suprise turned up on Jupiter Networks high end systems, when it should not have and was still creating issues half a decade back, https://checkoway.net/musings/dualec/ There were other issues with RSA certs which nearly all overlap in time. Thus if the NSA knew about them all could have had access to all RSA PubKey reliant traffic this century… Which begs the question about why the NSA are twitchy about PQC key establishment protocols… What do they know that we don’t and is it another bit of NOBUS nonsense again. [1] It’s one of those “Catch 22” problems… Because the devices have no real human interfaces or electromagnetic moving parts, the device / internal entropy is in the order of one or three bits a minute. Then because the embedded device has no certificate yet, it’s probably got no real external entropy coming in across the network either. So the “Catch” is to get entropy to make a couple of random numbers of the right size to make a new secure RSA certificate… you either need the certificate already, or known entropy, neither of which is secure…
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Factoring RSA Keys with Many Zeros
  - Published: 2026-06-29T16:05:18+00:00
  - Link: https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html
  - Summary: Interesting research on a new class of weak RSA keys: keys with lots of zeros. It turns out that these keys are out in the wild. The badkeys project is an open-source service that checks public keys for known vulnerabilities. While developing this tool, Hanno collected a massive number of real-world keys from public sources, including Certificate Transparency logs, internet-wide TLS and SSH scans, PGP keys, and many others. By searching this dataset for unexpectedly sparse RSA moduli, we uncovered a large number of keys in the wild with the patterns in Figure 1...

### Cluster 7de9036f43 — score 16

- Title: Attackers Exploit SimpleHelp CVE-2026-48558 to Deploy TaskWeaver and Djinn Stealer
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-30T11:18:47+00:00
- Link: https://thehackernews.com/2026/06/attackers-exploit-simplehelp-cve-2026.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-48558

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_industries: financial_services
- affected_products: Apple iOS/macOS, GitHub, Okta
- cve_ids: CVE-2026-48558
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: financial_services
- affected_products: Apple iOS/macOS, Okta, GitHub
- cve_ids: CVE-2026-48558
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
An unknown threat actor has been observed exploiting a recently disclosed maximum-severity security flaw in SimpleHelp to deliver two previously unreported malware families, TaskWeaver and Djinn Stealer. The intrusion involves the exploitation of CVE-2026-48558 (CVSS score: 10.0), a critical authentication bypass vulnerability impacting the OpenID Connect (OIDC) flow that an unauthenticated
```

#### Full body

```
Attackers Exploit SimpleHelp CVE-2026-48558 to Deploy TaskWeaver and Djinn Stealer  Ravie Lakshmanan  Jun 30, 2026 AI Security / Vulnerability An unknown threat actor has been observed exploiting a recently disclosed maximum-severity security flaw in SimpleHelp to deliver two previously unreported malware families, TaskWeaver and Djinn Stealer . The intrusion involves the exploitation of CVE-2026-48558 (CVSS score: 10.0), a critical authentication bypass vulnerability impacting the OpenID Connect (OIDC) flow that an unauthenticated attacker could exploit to obtain a fully authenticated "Technician session by submitting a forged token containing arbitrary identity claims. "TaskWeaver is a heavily obfuscated Node.js loader, delivered as jquery.js and executed through node.exe, that implements an encrypted, reusable payload delivery channel rather than a fixed set of post exploitation commands," Blackpoint Cyber said in an analysis. "The observed second stage payload, Djinn Stealer, targets Windows, macOS, and Linux systems." Djinn Stealer is designed to harvest credentials associated with cloud platforms, source control, package registries, infrastructure tooling, AI development assistants, browsers, SSH, and cryptocurrency wallets. Details of CVE-2026-48558 emerged earlier this month when Horizon3.ai, which discovered the flaw, said it affects servers configured to use either generic OIDC or Azure AD OIDC and that it stems from the manner in which SimpleHelp validates the IdP assertions. "In many SimpleHelp deployments that have OIDC-type authentication enabled, an unauthenticated attacker can create and authenticate as a new 'Technician' user," Horizon3.ai security researcher Zach Hanley said . "This Technician, by default, can perform privileged management activities such as remoting into managed endpoints, executing scripts, and more." "Even when the SimpleHelp server is configured to enforce MFA for technicians, this issue allows the attacker to bypass this mechanism because on first login, technicians can self-register their own MFA method." In the attack chain documented by Blackpoint Cyber, successful exploitation of the flaw in the Remote Monitoring and Management (RMM) software is said to have enabled the threat actor to obtain an authenticated "Technician" session on a publicly-accessible server, which was then abused to deploy TaskWeaver and Djinn Stealer. "The compromised RMM platform provided the operator with a trusted administrative channel capable of transferring files and executing commands on systems managed through the server," researchers Nevan Beal and Sam Decker said. TaskWeaver is a modular Node.js loader capable of fingerprinting the system, establishing encrypted communications with a remote server ("a.dev-tunnels[.]com"), and retrieving and executing additional JavaScript payloads with elevated access to the Node.js runtime. The final stage is an information stealer engineered to siphon valuable data from compromised Windows, macOS, or Linux hosts. The breadth of the information targeted by the stealer is as follows - Credentials, history, and bookmarks stored in web browsers Configuration and authentication data associated with AWS, Azure, Google Cloud, Oracle Cloud Infrastructure, Okta, Cloudflare, DigitalOcean, Linode, Heroku, Vercel, Railway, Supabase, Pulumi, Terraform, HashiCorp Vault, and Consul GitHub CLI data Git configuration SSH keys Docker authentication Helm registry information S3 and MinIO client configurations Subversion credentials Credentials for npm, pnpm, Yarn, NuGet, Cargo, Composer, Maven, Gradle, pip, PyPI, Conda, Bun, Ivy, and Scala Build Tool Configuration, authentication, session, and project data associated with Anthropic Claude, Google Gemini, OpenAI Codex, Cline, OpenCode, and Kilo Cryptocurrency wallets and keystores associated with Bitcoin, Litecoin, Dogecoin, Dash, Ethereum, Monero, Zcash, Exodus, Atomic Wallet, and Electrum On Linux systems, the malware also attempts
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit SimpleHelp CVE-2026-48558 to Deploy TaskWeaver and Djinn Stealer
  - Published: 2026-06-30T11:18:47+00:00
  - Link: https://thehackernews.com/2026/06/attackers-exploit-simplehelp-cve-2026.html
  - Summary: An unknown threat actor has been observed exploiting a recently disclosed maximum-severity security flaw in SimpleHelp to deliver two previously unreported malware families, TaskWeaver and Djinn Stealer. The intrusion involves the exploitation of CVE-2026-48558 (CVSS score: 10.0), a critical authentication bypass vulnerability impacting the OpenID Connect (OIDC) flow that an unauthenticated
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: 'Djinn' Stealer Targets Cloud, AI Credentials
  - Published: 2026-06-29T21:29:15+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/djinn-stealer-targets-cloud-ai-credentials
  - Summary: The infostealer was delivered via CVE-2026-48558, a critical authentication bypass vulnerability in SimpleHelp, targeting credentials linking development and admin environments to wider enterprise systems.

### Cluster 93502a2013 — score 16

- Title: Browser-Only Ransomware: From LLM Hallucinations to a Practical Attack Technique
- Source: Check Point Research (threat_research_primary)
- Published: 2026-07-01T10:05:35+00:00
- Link: https://research.checkpoint.com/2026/browser-only-ransomware-from-llm-hallucinations-to-a-practical-attack-technique/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, Anthropic/Claude, Apple iOS/macOS, OpenAI/ChatGPT
- cve_ids: CVE-2026-43707
- urgency_signals: poc_available
- content_type: incident_report, news_report
- confidence_tier: tier_1_offensive_research, tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft
- affected_industries: financial_services
- affected_products: Android, Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Research by: Alexey Bukhteyev Key Takeaways Introduction Over the past several years, large language models have reshaped software development, and malware development has followed the same path. Check Point Research has documented this trend from early experiments showing that AI systems could generate offensive components, to cases of cybercriminals using ChatGPT to create malicious tools, and […] The post Browser-Only Ransomware: From LLM Hallucinations to a Practical Attack Technique appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 17 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 461 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 414 How To Guides 13 Ransomware 5 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 Browser-Only Ransomware: From LLM Hallucinations to a Practical Attack Technique July 1, 2026 https://research.checkpoint.com/2026/browser-only-ransomware-from-llm-hallucinations-to-a-practical-attack-technique/ Research by: Alexey Bukhteyev Key Takeaways AI can turn high-level malicious ideas into concrete techniques, and can independently design and implement novel attack paths that have not yet appeared in real-world campaigns. In this research, DeepSeek connected unrealistic browser-malware concepts with a real browser capability, turning an AI-generated malware hallucination into a plausible browser-native ransomware technique. Although the generated sample was incomplete, it exposed a practical abuse path based on the File System Access API and access to photo directories. The technique does not require a native payload, APK installation, browser exploit, or root access. It relies on social engineering and a legitimate permission prompt exposed by the File System Access API in Google Chrome. The Android scenario is especially concerning because photo directories are high value personal data stores and, unlike iOS, modern Android Chrome versions expose a browser API that allows web pages to read and modify files in those directories after user approval. Using a fake AI image-enhancement workflow gives users a plausible reason to approve folder-level file access. Our PoC demonstrates this browser-only workflow against selected image directories on Android. Introduction Over the past several years, large language models have reshaped software development, and malware development has followed the same path. Check Point Research has documented this trend from early experiments showing that AI systems could generate offensive components, to cases of cybercriminals using ChatGPT to create malicious tools, and later to advanced AI-authored malware frameworks such as VoidLink. In some cases, LLMs lowered the barrier enough for users with little or no development experience to produce working offensive code. As frontier models became better at writing reliable code, including complex security related components, major AI vendors also turned cyber safety into a dedicated control area. Clearly malicious requests involving credential theft, malware deployment, ransomware behavior, persistence, stealth, or unauthorized exploitation are now commonly blocked or refused. OpenAI’s cyber-safety documentation, for example, describes additional safeguards for models classified as having High Cybersecurity Capability, while Anthropic has published reports on detecting and countering cyber misuse of Claude. DeepSeek then becomes particularly relevant in this context for several reasons: Lower refusal rates for harmful cyber enforcement: compared with Anthropic and OpenAI, DeepSeek models were less consistent refusing harmful cyber requests, including the File System Access API implementation we will be discussing later on this article. Low barrier to access: DeepSeek is free to use via the web interface, widely available, and accessible in regions where other frontier models face regulatory or commercial restrictions. This lowers the cost of repeated malicious experimentation. End-to-end malicious code from a single prompt: in our testing, a working malicious application could often be generated from a single broad prompt. Achieving a comparable result with OpenAI or Anthropic typically requires decomposing the attack into multiple benign-looking requests and manually assembling the generated components. Putting this all together, these differences make DeepSeek
```

#### Corroborating sources (3)

- **Check Point Research** (threat_research_primary)
  - Title: Browser-Only Ransomware: From LLM Hallucinations to a Practical Attack Technique
  - Published: 2026-07-01T10:05:35+00:00
  - Link: https://research.checkpoint.com/2026/browser-only-ransomware-from-llm-hallucinations-to-a-practical-attack-technique/
  - Summary: Research by: Alexey Bukhteyev Key Takeaways Introduction Over the past several years, large language models have reshaped software development, and malware development has followed the same path. Check Point Research has documented this trend from early experiments showing that AI systems could generate offensive components, to cases of cybercriminals using ChatGPT to create malicious tools, and […] The post Browser-Only Ransomware: From LLM Hallucinations to a Practical Attack Technique appeared first on Check Point Research .
- **Trail of Bits** (offensive_vulnerability_research)
  - Title: GPT-5.5-Cyber built a zlib fuzzing lab in a day
  - Published: 2026-07-02T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/
  - Summary: We’re running Patch the Planet , an ongoing collaboration with OpenAI that pairs Trail of Bits engineers directly with more than 30 open-source projects. Its goal is to front-run a serious problem facing open-source maintainers: highly capable models like GPT-5.5-Cyber will soon create a firehose of bug reports, and OSS maintainers are already spread thin. Our plan is to point OpenAI’s latest models at real codebases, find the security bugs first, work with maintainers to patch them, and find ways to decrease the burden on maintainers in the long run. We’ll publish field reports like this one as the initiative progresses; follow along via the Patch the Planet tag. The expertise barrier that kept bespoke fuzzing campaigns out of reach for most attackers is gone. We watched GPT-5.5-Cyber build in a single day what would have taken weeks for a skilled security researcher : harnesses across a dozen entrypoints, sanitizer and variant builds, seeds, and multiple findings currently undergoing
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New BioShocking Attack Tricks AI Browsers Into Leaking User Credentials
  - Published: 2026-06-30T08:37:19+00:00
  - Link: https://thehackernews.com/2026/06/new-bioshocking-attack-tricks-ai.html
  - Summary: Convince an AI browser that it is playing a game, and it can hand over your login details. That is the finding behind BioShocking, a technique from security firm LayerX that tricked six AI browsers and assistants into copying a user's credentials and sending them to an attacker. The targets included OpenAI's ChatGPT Atlas, Perplexity's Comet, and Anthropic's Claude browser extension. An

### Cluster 87e2639a3b — score 16

- Title: Formalizing Red Teaming Offensive Methodology as a Multi-Agent AI Architecture
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-02T13:32:24+00:00
- Link: https://www.rapid7.com/blog/post/so-red-teaming-offensive-methodology-multi-agent-ai-architecture
- Fetch status: ok
- Member count: 7
- Corroborating source count: 5
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain
- affected_products: Anthropic/Claude, Google Cloud, Google/Gemini
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Threat actors are integrating AI into their exploit chains, accelerating reconnaissance, automating vulnerability discovery, and scaling social engineering in ways that compress the timeline between initial access and impact. The barrier to sophisticated offensive operations is dropping fast. Rapid7's Red Team is doing the same. Over the past year we formalized our approach into a structured multi-agent system that follows our penetration testing methodology end-to-end from scoping an engagement to validating findings to generating reports. We built it as a production system, not a proof of concept, and the process of designing and operating it taught us as much about defending against AI-enhanced attacks as it did about conducting them. The system also proved its value as part of Anthropic's Project Glasswing initiative . Glasswing is a program that gives leading security companies early access to frontier cyber models before they reach wider availability, enabling security research t
```

#### Full body

```
Back to Blog Security Operations Formalizing Red Teaming Offensive Methodology as a Multi-Agent AI Architecture Jacob Steadman Jul 2, 2026 | Last updated on Jul 2, 2026 | 9 min read DISCOVER VECTOR COMMAND Threat actors are integrating AI into their exploit chains, accelerating reconnaissance, automating vulnerability discovery, and scaling social engineering in ways that compress the timeline between initial access and impact. The barrier to sophisticated offensive operations is dropping fast. Rapid7's Red Team is doing the same. Over the past year we formalized our approach into a structured multi-agent system that follows our penetration testing methodology end-to-end from scoping an engagement to validating findings to generating reports. We built it as a production system, not a proof of concept, and the process of designing and operating it taught us as much about defending against AI-enhanced attacks as it did about conducting them. The system also proved its value as part of Anthropic's Project Glasswing initiative . Glasswing is a program that gives leading security companies early access to frontier cyber models before they reach wider availability, enabling security research that stays ahead of malicious adoption. We infused our red team architecture with Claude Mythos, applying it across penetration testing, vulnerability research, and red team operations. The combination of our formalized multi-agent architecture with a frontier-class model produced exceptional results in vulnerability analysis and exploit chain development. This validated both the architecture's design and the importance of getting these capabilities into defenders' hands first. This post covers the architecture, the key design decisions, and what we learned along the way. Why Rapid7's Red Team built a multi-agent system Penetration testing is labor-intensive by nature as a significant portion of any engagement is spent on structured, repeatable work like enumerating attack surfaces, tracing data flows through source code, checking security headers, documenting findings in a consistent format. The actual judgement — deciding what to test next, assessing exploitability, understanding business impact — remains deeply human. The opportunity was straightforward: offload the mechanical work to AI agents while maintaining human insight at decision points where it matters most. Those decision points are where engagements succeed or fail: scoping what's in and out of bounds, choosing which attack paths to pursue based on business context, assessing whether a vulnerability is genuinely exploitable in a given environment, deciding when a finding is significant enough to escalate, and interpreting results in ways that translate to actionable risks. None of that is mechanical, it requires experience, judgement, and context that models routinely get wrong. And as an internal security team, we don't just report vulnerabilities, we're accountable for coverage. If something ships with an exploitable flaw we missed, that's on us. The bar for confidence is high, and that's why humans stay in the loop at every point that matters. We also had a secondary motivation. Building a system that follows a structured offensive methodology gives us direct architectural insight into how AI agents behave in adversarial contexts including the capabilities, the limitations, and the failure modes. That understanding now informs how we assess and secure Rapid7's own AI-powered products. The architecture: Orchestration, not autonomy The system isn't a single monolithic agent but a team of specialist agents coordinated by an orchestrator that mirrors how human red teams operate. The orchestrator doesn't test anything. It assesses the current state of the engagement, determines what needs to happen next, routes work to the appropriate specialist, and processes the results. Specialist agents handle enumeration, code review, dynamic testing, and reporting.Each with defined inputs, outp
```

#### Corroborating sources (5)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Formalizing Red Teaming Offensive Methodology as a Multi-Agent AI Architecture
  - Published: 2026-07-02T13:32:24+00:00
  - Link: https://www.rapid7.com/blog/post/so-red-teaming-offensive-methodology-multi-agent-ai-architecture
  - Summary: Threat actors are integrating AI into their exploit chains, accelerating reconnaissance, automating vulnerability discovery, and scaling social engineering in ways that compress the timeline between initial access and impact. The barrier to sophisticated offensive operations is dropping fast. Rapid7's Red Team is doing the same. Over the past year we formalized our approach into a structured multi-agent system that follows our penetration testing methodology end-to-end from scoping an engagement to validating findings to generating reports. We built it as a production system, not a proof of concept, and the process of designing and operating it taught us as much about defending against AI-enhanced attacks as it did about conducting them. The system also proved its value as part of Anthropic's Project Glasswing initiative . Glasswing is a program that gives leading security companies early access to frontier cyber models before they reach wider availability, enabling security research t
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Get started with the Claude apps gateway for Google Cloud
  - Published: 2026-07-01T16:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/developers-practitioners/announcing-claude-apps-gateway-for-google-cloud/
  - Summary: Anthropic's agentic coding tool Claude Code has worked with Google Cloud for a while now. An individual developer could easily point CLAUDE_CODE_USE_VERTEX=1 at a Google Cloud (GCP) project, grant the role roles/aiplatform.user , and inference stays inside your Google Cloud perimeter. That flow works great when it’s just you, or a handful of engineers. But rolling it out across an organization forces you to deal with enterprise friction: you have to manage per-developer cloud credentials, push a managed-settings.json to every laptop over MDM, and not be verified with zero per-developer usage attribution or easily enforceable spend caps. The Claude apps gateway closes that gap. It is a self-hosted service, shipped with the same claude binary, that sits directly between your local Claude Code clients and Google Cloud. This post breaks down exactly why you should run it and what a secure deployment looks like on Google Cloud. (Note: If you want to jump straight to the code, the full walkt
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them.
  - Published: 2026-07-02T12:33:57+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-
  - Summary: IBM and Red Hat assign 20,000 engineers to the new Project Lightwell service as Anthropic's Mythos findings ignite debate over how to secure the open-source software supply chain.
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Anthropic
  - Published: 2026-06-30T23:58:15+00:00
  - Link: https://simonwillison.net/2026/Jun/30/anthropic/#atom-everything
  - Summary: We’ve received notice that the Department of Commerce has lifted export controls on Claude Fable 5 and Mythos 5. We'll begin restoring access tomorrow, and will share an update soon. — Anthropic , on Twitter Tags: anthropic , claude , generative-ai , claude-mythos-fable , ai , llms
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: US lifting export control restrictions on Anthropic’s Mythos, Fable
  - Published: 2026-07-01T13:36:39+00:00
  - Link: https://cyberscoop.com/us-lifting-export-control-restrictions-anthropic-mythos-fable/
  - Summary: The company and the Commerce Department say they have reached an agreement that will see the AI models released publicly with new guardrails and classifiers. The post US lifting export control restrictions on Anthropic’s Mythos, Fable appeared first on CyberScoop .

### Cluster ab969947a9 — score 16

- Title: Google’s Continued Disruption of Malicious Residential Proxy Networks
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-07-02T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Background Today, in coordination with the FBI, Lumen, and others, Google took action against the NetNut residential proxy network, also known as Popa. This action builds on our disruption of the IPIDEA proxy network that took place in January 2026, and is a continuation of Google’s objective to dismantle malicious residential proxy networks. Actions Taken As a part of this disruption we took the following actions: Disabled Google accounts and associated Google services used by NetNut for malware command and control (C2), which directly violates Google’s Terms of Service and Acceptable Use Policy. Shared technical intelligence on NetNut software development kits (SDKs) and backend C2 infrastructure with platform providers, law enforcement, and research firms to help drive ecosystem-wide awareness and enforcement. We ensured Google Play Protect , Android’s built-in security protection, automatically warned users and disabled applications known to incorporate NetNut SDKs, and the system
```

#### Full body

```
Threat Intelligence Google’s Continued Disruption of Malicious Residential Proxy Networks July 2, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Background Today, in coordination with the FBI, Lumen, and others, Google took action against the NetNut residential proxy network, also known as Popa. This action builds on our disruption of the IPIDEA proxy network that took place in January 2026, and is a continuation of Google’s objective to dismantle malicious residential proxy networks. Actions Taken As a part of this disruption we took the following actions: Disabled Google accounts and associated Google services used by NetNut for malware command and control (C2), which directly violates Google’s Terms of Service and Acceptable Use Policy. Shared technical intelligence on NetNut software development kits (SDKs) and backend C2 infrastructure with platform providers, law enforcement, and research firms to help drive ecosystem-wide awareness and enforcement. We ensured Google Play Protect , Android’s built-in security protection, automatically warned users and disabled applications known to incorporate NetNut SDKs, and the system will continue to protect users against future install attempts. These efforts to help keep the broader digital ecosystem safe supplement the protections we have to safeguard Android users on certified devices. We believe our coordinated actions have caused significant degradation to NetNut’s proxy network and its business operations, reducing the available pool of devices for the proxy operator by millions . In addition to selling access to the network under the NetNut brand, NetNut has a robust reseller program that allows whitelabeling of its network. Google has high confidence that many popular residential proxy brands are in fact whitelabeling the NetNut botnet. While we expect this disruption to have a larger ripple effect across the residential proxy ecosystem, observations after the disruption of IPIDEA proved that individual networks can appear resilient. What we have observed is that when faced with the degradation of their own botnet, proxy operators begin buying capacity from their competitors, effectively becoming a reseller. We recognize that creating a lasting disruption in this fluid ecosystem means we must scale our efforts to target the infrastructure of several interconnected providers. We will continue to observe the composition of the NetNut network and map out how its peers adapt to this action. Why it Matters NetNut is among the largest and most popular residential proxy networks. Estimating the size of residential proxy networks is extremely challenging, but Google Threat Intelligence Group (GTIG) estimates the size of the NetNut network to be at least 2 million devices, distributed across the world. Public reporting by KrebsOnSecurity and others, confirmed by Google, illustrates that NetNut populates its botnet by distributing SDKs for devices commonly found in homes, such as smart TVs and streaming boxes. GTIG has also identified NetNut botnet plugin components for large-scale botnets such as Badbox 2.0. Residential proxy networks sell the ability to route traffic through IP addresses owned by internet service providers (ISPs), allowing attackers to mask malicious activity by hijacking these IP addresses. A robust residential proxy network requires controlling millions of residential IP addresses to sell to customers for use. To accomplish this, operators need code running on home devices to enroll them into the malicious network as exit nodes. Home devices become part of proxy networks either because they are pre-installed with malware before purchase or because users unknowingly download applications containing hidden proxy code. This creates serious risks for unsuspecting device owners, as their home IP addresses can be used by attackers as a launchpad for hacking and other unauth
```

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Google’s Continued Disruption of Malicious Residential Proxy Networks
  - Published: 2026-07-02T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks/
  - Summary: Background Today, in coordination with the FBI, Lumen, and others, Google took action against the NetNut residential proxy network, also known as Popa. This action builds on our disruption of the IPIDEA proxy network that took place in January 2026, and is a continuation of Google’s objective to dismantle malicious residential proxy networks. Actions Taken As a part of this disruption we took the following actions: Disabled Google accounts and associated Google services used by NetNut for malware command and control (C2), which directly violates Google’s Terms of Service and Acceptable Use Policy. Shared technical intelligence on NetNut software development kits (SDKs) and backend C2 infrastructure with platform providers, law enforcement, and research firms to help drive ecosystem-wide awareness and enforcement. We ensured Google Play Protect , Android’s built-in security protection, automatically warned users and disabled applications known to incorporate NetNut SDKs, and the system
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Google’s Continued Disruption of Malicious Residential Proxy Networks
  - Published: 2026-07-02T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks/
  - Summary: Background Today, in coordination with the FBI, Lumen, and others, Google took action against the NetNut residential proxy network, also known as Popa. This action builds on our disruption of the IPIDEA proxy network that took place in January 2026, and is a continuation of Google’s objective to dismantle malicious residential proxy networks. Actions Taken As a part of this disruption we took the following actions: Disabled Google accounts and associated Google services used by NetNut for malware command and control (C2), which directly violates Google’s Terms of Service and Acceptable Use Policy. Shared technical intelligence on NetNut software development kits (SDKs) and backend C2 infrastructure with platform providers, law enforcement, and research firms to help drive ecosystem-wide awareness and enforcement. We ensured Google Play Protect , Android’s built-in security protection, automatically warned users and disabled applications known to incorporate NetNut SDKs, and the system

### Cluster 5b50b4b7b2 — score 15

- Title: Citrix patches a new NetScaler flaw with echoes of CitrixBleed
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-06-30T21:46:38+00:00
- Link: https://cyberscoop.com/citrix-netscaler-flaw-cve-2026-8451-citrixbleed/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, ransomware_extortion, vulnerability_disclosure
- affected_industries: critical_infrastructure, government
- affected_products: Anthropic/Claude, Citrix, Palo Alto Networks
- cve_ids: CVE-2026-3055, CVE-2026-8451
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, ddos, vulnerability_disclosure, active_exploitation
- affected_industries: government, critical_infrastructure
- affected_products: Anthropic/Claude, Palo Alto Networks, Citrix
- cve_ids: CVE-2026-8451, CVE-2026-3055
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The bulletin includes six NetScaler issues, but attention is centered on a high-severity flaw with similarities to earlier actively exploited bugs. The post Citrix patches a new NetScaler flaw with echoes of CitrixBleed appeared first on CyberScoop .
```

#### Full body

```
Advertisement Subscribe to our daily newsletter. Subscribe Close Citrix published a security bulletin Tuesday disclosing six vulnerabilities in NetScaler ADC and NetScaler Gateway appliances, including a high-severity memory disclosure flaw that researchers say belongs to a vulnerability class first identified in the 2023 incident known as CitrixBleed . The company rated the overall bulletin severity as high and assigned CVSS scores ranging from 6.9 to 8.8 across the six CVEs. Citrix said customers should install the updated builds and, in one case, manually adjust a configuration parameter even after patching. The most closely scrutinized of the vulnerabilities, CVE-2026-8451 , was discovered by researchers at watchTowr , a cybersecurity firm that has published several prior analyses of issues in NetScaler products. According to a technical writeup the firm released alongside Tuesday’s disclosure, the vulnerability stems from how NetScaler parses SAML authentication requests when an appliance is configured as a SAML identity provider, a deployment mode commonly used for single sign-on. WatchTowr researcher Aliz Hammond wrote that the firm found the flaw in late March while reproducing a separate vulnerability, CVE-2026-3055, that Citrix disclosed earlier this year. That March flaw was added to CISA’s Known Exploited Vulnerabilities catalog after researchers and the agency confirmed active exploitation within days of disclosure. The new flaw shares a root cause with the March bug: both involve out-of-bounds memory reads triggered by malformed SAML requests sent to NetScaler’s authentication endpoints. Advertisement “Referencing what we wrote previously, because it is demonstrably evergreen: ‘However, what should be of concern is the bigger picture – the trend, which is very clearly suggesting that memory management continues to appear fragile within Citrix NetScaler appliances, to the extent that even accidentally misconfiguring an appliance can lead to the disclosure of leaked memory,’” Hammond wrote in the report. The bulletin also discloses five additional vulnerabilities affecting different NetScaler subsystems. Two involve memory overflow conditions that could cause denial-of-service outcomes. A separate flaw could allow unauthenticated arbitrary file reads on appliances where management access is exposed on certain network interfaces. Another concerns memory overread triggered through TCP timestamp handling. The sixth involves a denial-of-service condition tied to malformed HTTP/2 requests, which requires an additional manual configuration change to fully fix, since the relevant timeout parameter defaults to a value that leaves the underlying condition unaddressed unless administrators set it explicitly. Along with Hammond, the bulletin credits Michael Tucker of the XOR team at JPMorgan Chase and Maxim Suhanov for finding the vulnerabilities. The NetScaler product line has accumulated more than 20 entries in CISA ’s KEV catalog over the past three years, including multiple flaws that have been weaponized in ransomware campaigns. As of Tuesday, the latest vulnerability had not joined that list — neither the vendor bulletin nor watchTowr’s writeup cited confirmed exploitation at the time of disclosure. Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops (Getty Images) (Getty Images) Palo Alto Networks headquarters in Silicon Valley; Palo Alto Networks, Inc. is an American multinational cyber security company. (Getty Images) Latest Podcasts When iPhone exploits turn into commodities How security investigators can get the right info out of AI security tools Inside Operation Disruption Week: Taking Down Southeast Asia’s Scam Machine Zero days, zero order: The chaos reshaping vulnerability disclosure Government US lifting export control restrictions on Anthropic’s Mythos, Fable DHS to unveil replacement council for critical infrastructure cybe
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Citrix patches a new NetScaler flaw with echoes of CitrixBleed
  - Published: 2026-06-30T21:46:38+00:00
  - Link: https://cyberscoop.com/citrix-netscaler-flaw-cve-2026-8451-citrixbleed/
  - Summary: The bulletin includes six NetScaler issues, but attention is centered on a high-severity flaw with similarities to earlier actively exploited bugs. The post Citrix patches a new NetScaler flaw with echoes of CitrixBleed appeared first on CyberScoop .

### Cluster de6119ec2c — score 15

- Title: June 2026 Apple Updates, (Tue, Jun 30th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-06-30T09:31:27+00:00
- Link: https://isc.sans.edu/diary/rss/33114
- Fetch status: fetch_failed:HTTPError
- Member count: 2
- Corroborating source count: 2
- Strong signals: Apple iOS/macOS

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_1_government, tier_4_news

#### Primary article taxonomy
- affected_products: Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
Apple released updates for iOS/iPadOS, macOS, and Safari on Monday. There have been no updates for other Apple operating systems (visionOS, watchOS, tvOS). Usually, Apple updates all products at the same time.
```

#### Corroborating sources (2)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: June 2026 Apple Updates, (Tue, Jun 30th)
  - Published: 2026-06-30T09:31:27+00:00
  - Link: https://isc.sans.edu/diary/rss/33114
  - Summary: Apple released updates for iOS/iPadOS, macOS, and Safari on Monday. There have been no updates for other Apple operating systems (visionOS, watchOS, tvOS). Usually, Apple updates all products at the same time.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: ClickFix Now Cybercriminals' Favorite Malware Delivery Technique
  - Published: 2026-06-30T12:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/clickfix-cybercriminals-favorite/
  - Summary: ReliaQuest report warns of a surge in ClickFix social engineering attacks against Windows and macOS users

### Cluster c4a141b0a0 — score 14

- Title: Modernizing Global Vulnerability Standards For The Age Of AI
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-29T12:37:04+00:00
- Link: https://www.rapid7.com/blog/post/ai-modernizing-global-vulnerability-standards
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
As AI-driven vulnerability discovery accelerates, the cybersecurity ecosystem is being forced to examine whether the standards, disclosure processes, and prioritization frameworks defenders rely on can still keep pace. Many of those systems were built around human-speed discovery, manageable vulnerability volumes, and exploitability confirmed after the fact, which leaves them under increasing strain as frontier AI capabilities mature. During a private sector consultation with the White House in June, Corey Thomas and I presented Rapid7’s new policy paper, Modernizing Global Vulnerability Standards , which lays out where today’s vulnerability management infrastructure is breaking under AI-era conditions and what governments, security companies, and frontier AI providers need to do next. In recent guidance, the Five Eyes cyber security agencies warned that AI is rapidly transforming cyber risk by increasing the speed, scale, and sophistication of threats, lowering barriers for malicious
```

#### Full body

```
Back to Blog Artificial Intelligence Modernizing Global Vulnerability Standards For The Age Of AI Sabeen Malik Jun 29, 2026 | Last updated on Jun 29, 2026 | 5 min read DOWNLOAD THE POLICY PAPER As AI-driven vulnerability discovery accelerates, the cybersecurity ecosystem is being forced to examine whether the standards, disclosure processes, and prioritization frameworks defenders rely on can still keep pace. Many of those systems were built around human-speed discovery, manageable vulnerability volumes, and exploitability confirmed after the fact, which leaves them under increasing strain as frontier AI capabilities mature. During a private sector consultation with the White House in June, Corey Thomas and I presented Rapid7’s new policy paper, Modernizing Global Vulnerability Standards , which lays out where today’s vulnerability management infrastructure is breaking under AI-era conditions and what governments, security companies, and frontier AI providers need to do next. In recent guidance, the Five Eyes cyber security agencies warned that AI is rapidly transforming cyber risk by increasing the speed, scale, and sophistication of threats, lowering barriers for malicious actors, and requiring leaders to reassess long-standing assumptions about resilience and accountability. AI vulnerability discovery is changing the rules In April 2026, Anthropic, OpenAI, and Google DeepMind each announced production-grade AI systems capable of discovering, chaining, and, in some cases, remediating software vulnerabilities at machine speed. In the same period, the Stanford HAI AI Index 2026 Cybench benchmark showed unguided AI agent solve rates on cybersecurity tasks rising from 15% to 93% in a single year. These are deployed capabilities on a steep improvement curve. Faster discovery can help security teams identify weaknesses earlier, validate risk more effectively, and improve remediation workflows. It also increases the pressure on every system that decides how vulnerabilities are verified, scored, disclosed, prioritized, and fixed. Vulnerability management standards were built for human speed For decades, the security community has depended on shared infrastructure to make vulnerability management work. CVE identifiers, CVSS scoring, the National Vulnerability Database, the CISA Known Exploited Vulnerabilities catalog, and the Exploit Prediction Scoring System all help organizations understand what a vulnerability is, how severe it may be, whether it is being exploited, and how urgently it should be addressed. Those systems were built around several assumptions: vulnerability discovery would be human-led, volume would remain manageable, exploitability would usually be confirmed after the fact, and organizations would have time to assess and respond. As AI-driven discovery challenges each of those assumptions, existing strain across the vulnerability ecosystem becomes much harder to absorb. CVE submissions already grew 263% between 2020 and 2025 from human-speed growth alone. NIST acknowledged in April 2026 that the National Vulnerability Database can no longer keep pace and is shifting to risk-based triage. If AI-driven discovery dramatically increases volume, the prioritization problem becomes even more acute. The issue for defenders is whether organizations can understand which vulnerabilities are actually exploitable, which are reachable in their environments, which can be chained together, and which require immediate action. AI-era vulnerability prioritization needs reform The paper argues that the prioritization gap is the most urgent and least addressed part of the problem. Traditional severity scores can miss the way attackers chain multiple lower-severity issues into a serious compromise. KEV remains one of the strongest signals available to defenders, but it is retrospective by design because it depends on confirmed exploitation in the wild. EPSS is trained on historical attacker behavior, which may not reflect what AI-assist
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Modernizing Global Vulnerability Standards For The Age Of AI
  - Published: 2026-06-29T12:37:04+00:00
  - Link: https://www.rapid7.com/blog/post/ai-modernizing-global-vulnerability-standards
  - Summary: As AI-driven vulnerability discovery accelerates, the cybersecurity ecosystem is being forced to examine whether the standards, disclosure processes, and prioritization frameworks defenders rely on can still keep pace. Many of those systems were built around human-speed discovery, manageable vulnerability volumes, and exploitability confirmed after the fact, which leaves them under increasing strain as frontier AI capabilities mature. During a private sector consultation with the White House in June, Corey Thomas and I presented Rapid7’s new policy paper, Modernizing Global Vulnerability Standards , which lays out where today’s vulnerability management infrastructure is breaking under AI-era conditions and what governments, security companies, and frontier AI providers need to do next. In recent guidance, the Five Eyes cyber security agencies warned that AI is rapidly transforming cyber risk by increasing the speed, scale, and sophistication of threats, lowering barriers for malicious

### Cluster df28d0fe5c — score 14

- Title: Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-01T19:40:06+00:00
- Link: https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Kubernetes

#### Cluster taxonomy (union across members)
- affected_products: Kubernetes
- cve_ids: CVE-2024-31989, CVE-2025-55190, CVE-2026-42880
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: Kubernetes
- cve_ids: CVE-2024-31989, CVE-2025-55190, CVE-2026-42880
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Argo CD, a widely used tool for deploying software to Kubernetes, has an unpatched flaw in its repo-server component that lets an unauthenticated attacker run code, provided they can reach the component's internal network port. Synacktiv, which found the bug, says it can lead to a full cluster takeover. There is no fix and no CVE. The firm says it reported the flaw to Argo CD's maintainers in
```

#### Full body

```
Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters  Swati Khandelwal  Jul 01, 2026 Kubernetes / Server Security Argo CD , a widely used tool for deploying software to Kubernetes, has an unpatched flaw in its repo-server component that lets an unauthenticated attacker run code, provided they can reach the component's internal network port. Synacktiv , which found the bug, says it can lead to a full cluster takeover. There is no fix and no CVE. The firm says it reported the flaw to Argo CD's maintainers in January 2025; roughly eighteen months later, it remains unpatched, so it published the details to warn users. The bug sits in repo-server, the Argo CD component that reads Git repositories and builds Kubernetes manifests, the files that define what the cluster deploys. Its internal gRPC service has no authentication; anyone who can reach it can send a crafted request to run a command. Synacktiv demonstrated the attack against Argo CD v2.13.3 and reports no patched release; it did not publish a full list of affected versions. The technique abuses kustomize , a standard tool Argo CD runs to turn repository files into manifests. Kustomize has a --helm-command option that points to the helm binary it should call. Synacktiv found that an unauthenticated request to the repo-server's GenerateManifest service can set that option to a script instead, pulled from an attacker-controlled Git repository. When kustomize runs, it executes the script rather than helm. But "internal" does not mean isolated by default. Argo CD ships Kubernetes network policies that wall the repo-server off from everything except its own components. Synacktiv found the Helm chart, a common way to install Argo CD, leaves those policies off by default , with networkPolicy.create set to false. In that setup, an attacker who compromises a single pod in the cluster can reach the repo-server and trigger the bug. Running code on the repo-server is not the end of it. Synacktiv used that access to read the cluster's Redis password from an environment variable, connect to Argo CD's Redis cache, and poison the stored deployment data. On the next automatic sync, Argo CD deployed an attacker-supplied workload. That step revives CVE-2024-31989 , a 2024 flaw Cycode found where Argo CD's Redis had no password, letting any pod in the cluster poison the deployment cache. Argo CD fixed that by adding a Redis password, but the cache itself is still not signed, so stealing the password back reopens the same attack. What to do There is no patched version, so the defense is network isolation. Turn on Kubernetes network policies so only Argo CD's own components can reach the repo-server and Redis ports. Argo CD provides the policy files; Helm users have to enable them because the chart leaves them off. Check what is active with: kubectl get networkpolicy -A. A healthy install shows one network policy per component, including the repo-server and Redis. If those policies are missing, the repo-server and Redis ports are reachable from the rest of the cluster. Synacktiv built a tool, argo-cdown, that automates the full attack. It is holding the tool back for now to give defenders time to lock down their network policies, and says it will publish it on GitHub later so administrators can test their own deployments. This is not Argo CD's first exposure of its own internals. In September 2025, it patched CVE-2025-55190 , where an API token with only basic read access could pull back a project's Git repository credentials, a flaw that The Hacker News flagged at the time . In May 2026, another bug, CVE-2026-42880 , allowed read-only users to read plaintext Kubernetes secrets. The pattern is hard to miss: Argo CD concentrates cluster access and repository secrets, and its internal surfaces keep handing them out, to an unauthenticated request in one bug and a low-privilege token in the next. Until a patch ships, treating the cluster network as hostile is the onl
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters
  - Published: 2026-07-01T19:40:06+00:00
  - Link: https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html
  - Summary: Argo CD, a widely used tool for deploying software to Kubernetes, has an unpatched flaw in its repo-server component that lets an unauthenticated attacker run code, provided they can reach the component's internal network port. Synacktiv, which found the bug, says it can lead to a full cluster takeover. There is no fix and no CVE. The firm says it reported the flaw to Argo CD's maintainers in
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Kubernetes Compliance Tools: Automating CIS Benchmarks
  - Published: 2026-06-29T17:19:10+00:00
  - Link: https://orca.security/resources/blog/kubernetes-compliance-tools-automating-cis-benchmarks/
  - Summary: Kubernetes compliance tools automate the enforcement of CIS Benchmarks, enabling teams to continuously validate cluster configurations against industry-accepted security baselines without slowing release velocity. The right tooling replaces manual audits with policy-driven checks that run across the CI/CD pipeline, from build to runtime, catching misconfigurations before they reach production. Maintaining multi-cloud compliance across dozens or […]

### Cluster d8d3a457ab — score 12

- Title: YARA-X 1.18.0 and 1.19.0 Release, (Sun, Jun 28th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-06-28T07:56:44+00:00
- Link: https://isc.sans.edu/diary/rss/33106
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
YARA-X&#;x26;#;39;s 1.18.0 release brings 3 improvements and 2 bugfixes.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: YARA-X 1.18.0 and 1.19.0 Release, (Sun, Jun 28th)
  - Published: 2026-06-28T07:56:44+00:00
  - Link: https://isc.sans.edu/diary/rss/33106
  - Summary: YARA-X&#;x26;#;39;s 1.18.0 release brings 3 improvements and 2 bugfixes.

### Cluster db017396fb — score 12

- Title: JADEPUFFER: Agentic ransomware for automated database extortion
- Source: Sysdig (detection_response_operations)
- Published: 2026-07-01T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- cve_ids: CVE-2025-3248
- urgency_signals: preauth_unauth
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- cve_ids: CVE-2025-3248
- urgency_signals: preauth_unauth
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Full body

```
< back to blog JADEPUFFER: Agentic ransomware for automated database extortion Published by: Michael Clark Director of Threat Research @ linkedin Published: July 1, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more Ransomware has had a human at the keyboard, or at least a human writing its script, since it was first established as a category of threat. The Sysdig Threat Research Team (TRT) has captured what we assess to be the first documented case of agentic ransomware: a complete extortion operation driven end-to-end by a large language model (LLM). This operator, which we have dubbed JADEPUFFER, gained initial access to an internet-facing Langflow instance through CVE-2025-3248 and ran an adaptive and fully automated campaign, ultimately pivoting to the intended target and running a destructive database-extortion playbook against the victim's production database server. JADEPUFFER is considered an agentic threat actor (ATA) , or an operator whose attack capability is delivered by an AI agent rather than a human-driven toolkit. The most striking characteristic, however, was the LLM's behavior. JADEPUFFER's own payloads were self-narrating. They contained natural language reasoning, target prioritization, and the kind of detailed annotations that human operators don’t often write but LLM-generated code produces reflexively. The operation also adapted in real time, retrying failed steps within refined parameters. In one sequence, it went from a failed login to a working fix in 31 seconds. The research below examines the Sysdig TRT’s observations of JADEPUFFER, along with its indicators of compromise and recommended defensive actions. The vulnerability Langflow is a popular open-source framework for building LLM-driven applications and agent workflows. CVE-2025-3248 is a missing-authentication flaw in its code validation endpoint that allows an unauthenticated attacker to execute arbitrary Python on the host. Langflow remains exposed on many internet-facing deployments and has several widely exploited vulnerabilities . Langflow is an attractive entry point because its servers are AI-adjacent, frequently hold provider API keys and cloud credentials in their environment, and are often stood up quickly without network controls. What the Sysdig TRT observed JADEPUFFER’s operation unfolded across two distinct targets: the internet-facing Langflow instance that provided initial access, and a separate production database server, which was JADEPUFFER’s true objective. The machine compromised during initial access was used in the compromise of the final target. All payloads were delivered as Base64-encoded Python through the Langflow RCE endpoint. Phase 1: The Langflow instance (initial access host) 1. Reconnaissance and credential harvesting: Immediately after gaining execution, the LLM enumerated the host ( id , uname -a , hostname , network interfaces, running processes) and swept the environment for secrets across many categories in parallel: LLM provider API keys (OpenAI, Anthropic, DeepSeek, Gemini, and others) Cloud credentials, with explicit coverage of Chinese providers ( ALIBABA_ , ALIYUN_ , TENCENT_ , HUAWEI_ ) but they also scanned for AWS, GCP, and Azure Cryptocurrency wallets and seed phrases Database credentials and configuration files 2. Local data looting: It dumped Langflow's own backing Postgres database, harvesting stored credentials, API keys, and user records, staged the output to local files, reviewed them, then deleted the staging files. 3. Internal lateral discovery: It scanned the internal address space and named services reachable from the Langflow host, probing databases, object storage, secret stores, and service-discovery endpoints with default credentials. 4. MinIO object-store enumeration and credential harvest: The LLM probed both
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: JADEPUFFER: Agentic ransomware for automated database extortion
  - Published: 2026-07-01T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion

### Cluster 4541afab04 — score 12

- Title: Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-01T07:20:51+00:00
- Link: https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Palo Alto Networks

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng
- affected_industries: financial_services, government, healthcare
- affected_products: Android, Palo Alto Networks, npm
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, active_exploitation
- affected_industries: healthcare, financial_services, government
- affected_products: npm, Android, Palo Alto Networks
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Large language models keep inventing web addresses that do not exist. Attackers have started buying those made-up domains before anyone else can, then hosting phishing pages on them to catch traffic that AI tools point their way. Palo Alto Networks' Unit 42 calls the trick phantom squatting, and its new research shows it is already happening in the wild. The reason it matters is
```

#### Full body

```
Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware  Swati Khandelwal  Jul 01, 2026 Artificial Intelligence / Threat Intelligence Large language models keep inventing web addresses that do not exist. Attackers have started buying those made-up domains before anyone else can, then hosting phishing pages on them to catch traffic that AI tools point their way. Palo Alto Networks' Unit 42 calls the trick phantom squatting , and its new research shows it is already happening in the wild. The reason it matters is trust. Developers and AI assistants increasingly treat the links a model hands back as real. When a model invents a domain that does not exist yet, whoever registers it first inherits all of that misplaced trust, with no phishing email and no malicious ad required. To measure the problem, Unit 42 asked two AI models 685,339 questions about 913 well-known brands across technology, finance, healthcare, government, gambling, and other sectors. The models produced 2.1 million links. Threat intelligence already flagged 13,229 of them as outright malicious, meaning the AI was handing out known-bad addresses. Roughly 250,000 of the invented domains had no owner yet, each a ready target for whoever registers it first. How phantom squatting works The attack works because a brand-new domain has no reputation. Blocklists, threat feeds, and reputation scores all need a site to misbehave for a while before they flag it. A freshly registered phantom domain has no such record, so those filters have nothing to flag. By the time they catch up, the victim has already been sent to the site by a tool they trust. Two details make it worse. The fake domains were not sitting in the training data: both models shipped before the real malicious sites existed, so the addresses come from the models' own language patterns, not memory. And those patterns are consistent. Different models often invent the same fake domain for the same question, which makes an attacker's next target easy to guess. Turning up a model's "creativity" setting only produced more invented domains. As Unit 42's researchers put it, the vector "exploits a structural property of LLM architectures that remains inherently unpatchable." Two observed cases Two cases show the full loop. On March 8, 2026, Unit 42's system predicted that AI models would invent a domain resembling a national postal service's online marketplace. Both models generated it at every temperature setting, a strong sign that they treated the fake site as fact. Twenty-three days later, on March 31, an attacker registered that exact domain and stood up a phishing kit named Montana Empire. The kit copied the real storefront in real time. It stole card numbers, bank-transfer details, and national ID data. A Telegram bot lets the operator approve victims' one-time passcodes by hand. The giveaway: leftover project files and session logs showed the criminal had built the kit with an AI coding assistant. Attacker and defender reached the same fake domain the same way, by asking an AI. In the second case, Unit 42 flagged a hallucinated postal-service domain a full 51 days before an attacker registered it. The attacker then wrapped it in a pixel-perfect brand clone, added a fake 4.8-star rating and a claim of over two million users, and used it to push a malicious Android app. Other detected domains impersonated a major UAE bank that an attacker had already been abusing for nearly a year, a European bank, and sports-betting sites aimed at users in Bangladesh. An old trick with a new target Phantom squatting is the domain version of slopsquatting , where attackers register the fake software package names that AI coding tools invent. That is not a hypothetical. A large USENIX study found code-generating models routinely suggest package names that do not exist, and the PhantomRaven campaign turned exactly that behavior into malware hidden in 126 npm packages with more than 86,000 installs. It points to a l
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware
  - Published: 2026-07-01T07:20:51+00:00
  - Link: https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html
  - Summary: Large language models keep inventing web addresses that do not exist. Attackers have started buying those made-up domains before anyone else can, then hosting phishing pages on them to catch traffic that AI tools point their way. Palo Alto Networks' Unit 42 calls the trick phantom squatting, and its new research shows it is already happening in the wild. The reason it matters is

### Cluster 57ef1249ed — score 12

- Title: Nissan Discloses Employee Data Breach Linked to Oracle Zero-Day
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-06-30T16:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/nissan-oracle-peoplesoft-zero-day/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: Scattered Spider, ShinyHunters
- affected_industries: education, financial_services
- affected_products: AWS, Salesforce
- cve_ids: CVE-2026-35273
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft, zero_day, data_breach
- actor_attribution: Scattered Spider, ShinyHunters
- affected_industries: financial_services, education
- affected_products: Salesforce, AWS
- cve_ids: CVE-2026-35273
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Nissan says employees' data was stolen via the Oracle PeopleSoft zero-day campaign
```

#### Full body

```
Infosecurity Magazine Home » News » Nissan Discloses Employee Data Breach Linked to Oracle Zero-Day Nissan Discloses Employee Data Breach Linked to Oracle Zero-Day News 30 June 2026 Written by Alessandro Mascellino News Reporter Email Alessandro Follow @a_mascellino Nissan has disclosed that current and former employees may have had sensitive personal data stolen, including Social Security numbers, banking details and tax records, after attackers exploited a zero-day flaw in Oracle's PeopleSoft software. The carmaker said in a breach notification published on June 26 that Oracle had warned it of a cyber event affecting hundreds of companies, and that Nissan was specifically targeted. It believes the breach affected current and former staff in the US, Canada, Mexico and Brazil and exposed data, including national identification numbers and dependent or beneficiary information. Caught in a Mass PeopleSoft Campaign Nissan described the entry point only as an unknown vulnerability in Oracle PeopleSoft, the enterprise software it uses to run payroll and HR. The flaw, tracked as CVE-2026-35273, is a critical remote code execution bug that attackers exploited as a zero-day. The wider campaign has been linked to the ShinyHunters extortion group, which claimed to have hit more than 100 organizations, mostly universities. Oracle issued an out-of-band advisory and mitigations only after the attacks began. Nissan's filing put the breach on May 27 and June 9, the window in which the campaign ran. Most named victims so far have been universities, making Nissan one of the larger corporate names caught in it. Read more on ShinyHunters' campaigns: ShinyHunters Targets Hundreds of Websites in New Salesforce Campaign Sensitive Data and a Payroll Lockdown Beyond Social Security and national identification numbers, Nissan said the exposed information could include contact and banking details, financial and tax data plus dependent or beneficiary records. The company said it had secured its systems, was working with Oracle and would offer affected staff free credit or dark web monitoring where available. As a precaution, Nissan has restricted payroll access so that staff must use a network computer or secured VPN to view pay slips or change direct deposit details, and it is adding extra identity checks before processing payroll requests. It urged employees to watch for phishing, change reused passwords and enable multi-factor authentication (MFA). Simon Pamplin, CTO at data security firm Certes, called it "a mass-casualty event across hundreds of unrelated organizations," warning that patching the flaw does nothing for data already taken during the exploitation window. Nissan said its investigation was ongoing and that affected individuals would be contacted directly. Image credit: Luthfi Syahwal / Shutterstock.com You may also like Medtronic Confirms Data Breach After ShinyHunters Claims News 28 April 2026 New Data Theft Campaign Targets Salesforce via Salesloft App News 27 August 2025 Workday Reveals CRM Breach News 18 August 2025 Allianz Life Data Breach Exposes Personal Data of 1.1 Million Customers News 19 August 2025 Hackers Exploit Misconfigurations in Public Websites With Improperly Exposed AWS Credentials News 10 December 2024 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Researcher Behind 'Exploitarium' Explains Release of Undisclosed Zero-Day Exploits News 2 July 2026 1 Cybercriminals Pose as Interpol in Phishing Emails to Infect Victims With Ransomware News 2 July 2026 2 NCSC Shares Tips on How to Make a Pen Tester’s Job Harder News 2 July 2026 3 Alleged Scattered Spider Member Extradited to US News 2 July 2026 4 Fileless Malware Abuses Google Blogspot to Deploy Infostealer in Memory News 1 July 2026 5 The Readiness Gap: What Wimbledon Reveals About Modern Cyber Defense Opinion 30 June 2026 6 Trust in Automated AI Vulnerability Scanning Collapses to 9%, New Study Finds News 25 June 2026 1 ClickFix Now Cybercrim
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Nissan Discloses Employee Data Breach Linked to Oracle Zero-Day
  - Published: 2026-06-30T16:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/nissan-oracle-peoplesoft-zero-day/
  - Summary: Nissan says employees' data was stolen via the Oracle PeopleSoft zero-day campaign

### Cluster d5faf7ea86 — score 12

- Title: US Federal Insurance Regulator Confirms Data Breach Via Oracle Flaw
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-06-29T10:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/us-insurance-regulator-confirms/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, zero_day
- affected_industries: financial_services, government, legal_professional
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, data_breach
- affected_industries: financial_services, government, legal_professional
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
An attacker has exploited a zero day in Oracle Peoplesoft to gain access to the IT systems of the NAIC, the standard-setting association for the US federal insurance system
```

#### Full body

```
Infosecurity Magazine Home » News » US Federal Insurance Regulator Confirms Data Breach Via Oracle Flaw US Federal Insurance Regulator Confirms Data Breach Via Oracle Flaw News 29 June 2026 Written by Kevin Poireault Reporter , Infosecurity Magazine Follow @Kpoireault Connect on LinkedIn The US National Association of Insurance Commissioners (NAIC) has suffered a security breach that has exposed US citizens’ credit rating data. The breach was detected on June 11 and the non-profit association for the US federal insurance system disclosed it to the public on June 17. In its latest update , posted on June 26, the NAIC confirmed that an unauthorized actor gained access to “a portion” of its environment through the exploitation of a zero-day vulnerability in Oracle PeopleSoft, which NAIC uses for internal financial reporting purposes. The incident was the result of “a broad campaign to exploit a vulnerability in PeopleSoft that was unknown to the developer or software users at the time, which affected multiple organizations,” the NAIC added. NAIC Confirms Data Affected and Unaffected by the Breach Once they entered the NAIC’s PeopleSoft environment, the attacker obtained information needed to gain temporary access to certain data storage areas. They then published some of the data accessed. Based on the NAIC’s preliminary findings, these include: Statutory financial reporting information that was already publicly available through state websites like InsData or resellers Credit rating agency data, including rating determinations of insurer investments “Potentially” additional storage data (e.g. routine technical information, such as outdated logs or configuration information) The NAIC said that some credit rating agencies have paused their data feeds following the incident, leading the association to temporarily suspend assigning designations to insurer investments. “Insurers should monitor [Automated Valuation Service Plus] AVS+ for any updates,” said the NAIC. Users have been notified of critical data that was not compromised by the attacker: Personal information of US insurance system users and employees Payment and financial account information, including credit card or banking information Rating agency investment rationale reports Information on any US state insurance departments’ systems Information linked to the National Insurance Producer Registry (NIPR) or the Teammate software provider Some insurance processes data, such as electronic funds transfer, risk-based capital data, policyholder information, producer data and event registration payment information Additionally, the NAIC denied the attacker’s claims that they gained access to information linked to technology provided by the NAIC, including the System for Electronic Rate and Form Filing (SERFF), Online Premium Tax for Insurance (OPTins), Uniform Certificate Authority Application (UCAA), Enterprise Data Platform (EDP) and Regulatory Data Collection (RDC). “Outside cybersecurity experts confirmed the unauthorized party did not take this information, nor compromised these regulatory reporting systems,” the NAIC stated. NAIC Operations Almost Fully Back to Normal In its update, the NAIC said it “promptly” contained the breach following detection and blocked the attacker’s access to its systems. It also engaged outside counsel and cybersecurity experts, who have helped taking additional steps to strengthen its defenses. “FBI coordination is underway,” the NAIC also noted. Finally, the association confirmed that its operations have returned to normal with the exception of online invoice payment via PeopleSoft, which is still unavailable. “We are meeting with credit rating providers and have provided third-party assurances that our systems are secure and the NAIC designation process can resume,” said the NAIC. You may also like US Government IIS Server Breached via Telerik Software Flaw News 16 March 2023 UK Government Cybersecurity Advisory Board Applications Now Open N
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: US Federal Insurance Regulator Confirms Data Breach Via Oracle Flaw
  - Published: 2026-06-29T10:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/us-insurance-regulator-confirms/
  - Summary: An attacker has exploited a zero day in Oracle Peoplesoft to gain access to the IT systems of the NAIC, the standard-setting association for the US federal insurance system

### Cluster 5811e9602e — score 11

- Title: Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-03T20:19:31+00:00
- Link: https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, manufacturing_industrial
- cve_ids: CVE-2026-6682, CVE-2026-6683, CVE-2026-6685, CVE-2026-6687, CVE-2026-6688
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: financial_services, manufacturing_industrial
- cve_ids: CVE-2026-6682, CVE-2026-6687, CVE-2026-6688, CVE-2026-6685, CVE-2026-6683
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Security firm runZero has disclosed seven vulnerabilities in FatFs, a small filesystem library that lets a device read and write the FAT and exFAT formats used on USB drives and SD cards. The flaws matter because FatFs is nearly everywhere. It ships inside the firmware that runs security cameras, drones, industrial controllers, hardware crypto wallets, and other devices built on
```

#### Full body

```
Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices  Swati Khandelwal  Jul 03, 2026 Vulnerability / IoT Security Security firm runZero has disclosed seven vulnerabilities in FatFs , a small filesystem library that lets a device read and write the FAT and exFAT formats used on USB drives and SD cards. The flaws matter because FatFs is nearly everywhere. It ships inside the firmware that runs security cameras, drones, industrial controllers, hardware crypto wallets, and other devices built on real-time operating systems. On the worst-affected systems, an attacker who gets a booby-trapped USB drive, SD card, or update file onto a device can corrupt its memory and run their own code. Many embedded devices lack the memory protections found on phones and desktops, which is why runZero says "any physical access leads to a jailbreak." A public kiosk, a camera with an SD slot, an ATM, or a voting machine with a USB port should not hand over full control after a moment of physical access, but here it can. All seven bugs work the same basic way. The device tries to read a storage volume or firmware image that has been deliberately malformed, and FatFs mishandles the bad data. runZero rated the set CVSS Medium to High, with no Criticals. The headline bug is CVE-2026-6682 (CVSS 7.6), an integer overflow in the code that mounts a FAT32 volume. Bad math can produce a false file size, which later code treats as a real read length. On real hardware, that can become memory corruption and code execution. Here are all seven, worst first by runZero's ranking: CVE-2026-6682 (7.6, High): FAT32 mount integer overflow leading to memory corruption and possible code execution. Reachable through some firmware updates, not just physical media. CVE-2026-6687 (7.6, High): an exFAT volume-label field overflows a small buffer, giving an attacker a clean memory-corruption foothold. CVE-2026-6688 (7.6, High): long filenames overflow the wrapper code many projects put around FatFs, such as a strcpy of fno.fname into a fixed buffer. Hard to fix inside FatFs alone. CVE-2026-6685 (6.1, Medium): a math wrap in cache handling on fragmented volumes that can silently corrupt data. CVE-2026-6683 (4.6, Medium): an exFAT divide-by-zero that crashes the device. In an update flow, it can brick hardware. Also reachable through some firmware updates. CVE-2026-6686 (4.6, Medium): a file extended past its end can leak leftover data from previously deleted files. CVE-2026-6684 (4.6, Medium): a malformed GPT partition table (the disk's map) can hang the device during mount. It is the only one of the seven fixed upstream, in FatFs R0.16. Here is the hard part. FatFs is maintained by one developer in a small corner of the internet, and runZero says it tried repeatedly to reach the maintainer and looped in Japan's JPCERT/CC coordination center, with no response. By runZero's account, there is no upstream fix for the memory-corruption bugs, no security mailing list, and no way for the many products that bundle FatFs to learn they are affected. Updating helps with the GPT hang, since the current release blocks it, but the rest fall to downstream vendors to patch on their own. runZero names affected platforms, including Espressif ESP-IDF, STMicroelectronics STM32Cube, Zephyr, MicroPython, ArduPilot, RT-Thread, Mbed, Samsung TizenRT, and the SWUpdate updater. That pushes the problem downstream into consumer IoT, industrial gear, drones, and crypto wallets. As of runZero's July 1 disclosure, no attacks using these bugs had been reported, and none have surfaced since. But the exploit material is already public: runZero shipped proof-of-concept disk images, a test harness, and a working QEMU-based exploit example in a companion repository . If you build firmware that touches FAT or exFAT media, the advice is direct. Find the copy of FatFs in your product, audit the wrapper code around it, look hard at how you handle filenames and file sizes, and plan to patc
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Unpatched Flaws Disclosed in Filesystem Bundled Into Millions of Embedded Devices
  - Published: 2026-07-03T20:19:31+00:00
  - Link: https://thehackernews.com/2026/07/unpatched-flaws-disclosed-in-filesystem.html
  - Summary: Security firm runZero has disclosed seven vulnerabilities in FatFs, a small filesystem library that lets a device read and write the FAT and exFAT formats used on USB drives and SD cards. The flaws matter because FatFs is nearly everywhere. It ships inside the firmware that runs security cameras, drones, industrial controllers, hardware crypto wallets, and other devices built on

### Cluster 728fb2c9de — score 11

- Title: AI Agent Exploits Langflow RCE to Automate Database Ransomware Attack
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-02T09:13:13+00:00
- Link: https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- cve_ids: CVE-2021-29441, CVE-2025-3248
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- cve_ids: CVE-2025-3248, CVE-2021-29441
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Security firm Sysdig says it has found what it believes is the first ransomware attack run from start to finish by an AI agent. Its Threat Research Team calls the operator JADEPUFFER and says a large language model handled the whole job: breaking in, stealing credentials, moving deeper into the network, then encrypting and wiping a company's production database. Ransomware has always
```

#### Full body

```
AI Agent Exploits Langflow RCE to Automate Database Ransomware Attack  Swati Khandelwal  Jul 02, 2026 Artificial Intelligence / Malware Security firm Sysdig says it has found what it believes is the first ransomware attack run from start to finish by an AI agent. Its Threat Research Team calls the operator JADEPUFFER and says a large language model handled the whole job: breaking in, stealing credentials, moving deeper into the network, then encrypting and wiping a company's production database. Ransomware has always needed a skilled person somewhere in the loop, either at the keyboard or writing the script the malware follows. If a model can chain those steps on its own, the skill needed to run an attack drops to whatever it costs to rent an AI agent. The way in was an old, already-patched bug. JADEPUFFER exploited CVE-2025-3248 , a missing-authentication flaw in Langflow , an open-source tool for building AI apps and agent workflows. The flaw lets anyone who can reach the server run their own Python code on it, no login needed. Langflow boxes are a tempting target because they often sit exposed on the internet and hold API keys and cloud credentials for the services they connect to. The flaw was fixed in Langflow 1.3.0 and added to CISA's Known Exploited Vulnerabilities list in May 2025, but plenty of servers were never updated. It is not even the only Langflow bug being hit this way . Once inside, the agent worked fast and cleaned up after itself. It mapped the machine, then swept it for secrets: API keys for AI services (OpenAI, Anthropic, DeepSeek, Gemini), cloud credentials (Chinese providers like Alibaba and Tencent alongside AWS, Google, and Azure), crypto wallet keys, and database logins. It raided a MinIO storage server using its factory-default login (minioadmin:minioadmin), which had never been changed. It also set up a way back in, adding a scheduled task that pinged the attacker's server every 30 minutes. Then it pivoted to its real target: a separate, internet-facing server running a MySQL database and Alibaba's Nacos, a settings and service directory common in microservice setups. The agent logged into the database as root. Sysdig says it never saw where those root credentials came from, so their origin is unknown. From there, it took over Nacos using a 2021 authentication bypass ( CVE-2021-29441 ) and a default signing key that Nacos has shipped unchanged since 2020, then planted its own admin account. The Ransom Note With No Key The agent encrypted all 1,342 Nacos settings, dropped the original tables, and left a ransom note demanding Bitcoin with a Proton Mail contact. It generated a random encryption key, printed it to the screen once, and never saved or sent it anywhere. There is no key to hand over. The victim cannot get the data back even if they pay. (The note claims AES-256; Sysdig notes the tool it used defaults to weaker AES-128, though the result is the same.) It then went further, deleting whole databases and leaving a comment in its own code claiming it had already copied the data somewhere else. Sysdig says that is the agent talking, not something the team could confirm, and found no evidence that any data was actually left. How Experts Know an AI Was Driving The clearest sign was the code itself. The attack payloads were full of plain-English notes explaining why each step was being taken, the running commentary a human hacker never bothers to write, but a model produces by default. The agent also fixed its own mistakes at machine speed. In one case, it went from a failed login to a correct, multi-step fix in 31 seconds, diagnosing the exact cause instead of blindly retrying. Sysdig counted more than 600 separate, purposeful payloads across the operation. One detail is still a puzzle. The Bitcoin address in the ransom note is the exact sample address that appears throughout Bitcoin's own developer documentation, which means it shows up all over the text these models are trained on. It is also
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: AI Agent Exploits Langflow RCE to Automate Database Ransomware Attack
  - Published: 2026-07-02T09:13:13+00:00
  - Link: https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
  - Summary: Security firm Sysdig says it has found what it believes is the first ransomware attack run from start to finish by an AI agent. Its Threat Research Team calls the operator JADEPUFFER and says a large language model handled the whole job: breaking in, stealing credentials, moving deeper into the network, then encrypting and wiping a company's production database. Ransomware has always

### Cluster cce9192f71 — score 10

- Title: Context Engineering | Compaction & Agent Memory for Automated Malware Analysis
- Source: SentinelOne Labs (threat_research_primary)
- Published: 2026-07-02T13:00:02+00:00
- Link: https://www.sentinelone.com/labs/context-engineering-compaction-agent-memory-for-automated-malware-analysis/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Compaction cut input tokens 86% across long-running agent evals with no quality loss. Context discipline matters as much as model selection.
```

#### Full body

```
AI Research Context Engineering | Compaction & Agent Memory for Automated Malware Analysis Gabriel Bernadett-Shapiro / July 2, 2026 Executive Summary Compaction is a context-management pattern used across agent systems to compress prior context into a denser working state for long-running tasks. SentinelLABS evaluated OpenAI’s native Responses API implementation against our automated malware analysis evaluation harness to measure real-world impact on task quality and cost. Compaction reduced input tokens by ~86% with no measurable change to the aggregate evaluation score. Our analysis found that compaction can significantly reduce the cost and noise of long-running security workflows without sacrificing task quality. OpenAI introduced native compaction in a March 2026 engineering post describing extensions to the Responses API. However, the underlying idea is not unique to OpenAI. Anthropic, Google, and other agent frameworks such as LangChain all expose or document related approaches under different names. The core problem these systems address is familiar to anyone who has built an agentic system: context accumulates faster than it stays relevant, and eventually the model is carrying more history than signal. At that point, task quality degrades and costs climb without a corresponding improvement in output. OpenAI’s solution was to build compaction directly into the runtime so developers would not need to build custom summarization and state-carrying systems themselves. The company noted that compaction is the mechanism Codex relies on for long-running coding tasks, which positions it as load-bearing infrastructure rather than a convenience feature. At SentinelLABS, we set out to evaluate how well OpenAI’s compaction would work for automated binary analysis, a domain with its own particular demands on agent memory and state management. Why Malware Analysis Is a Hard Problem for Agents Our evaluation harness gives a model access to a decompiler and asks it to complete the following: Identify important functions and follow code paths Interpret strings, APIs, call relationships, and data structures Rename functions or variables based on observed behavior Propose types or object models and explain what the malware is doing We compare the model’s output against golden reference analysis and written reports across scoring metrics for correctness and completeness. To achieve a high score, the model needs to maintain a working theory for the slice of the binary it is analyzing, track evidence already collected, and hold open questions alongside provisional conclusions. Malware analysis is an iterative process with a low-reward signal. A human analyst might inspect one function, learn something, pivot to another function, revise their theory, check a data structure, then return to update their original conclusion. Models do well in our evaluation where execution paths have straightforward continuity. They struggle when connections are unclear or require multiple rounds of investigation. In observing model performance, we noticed that the agent tended to carry an increasing volume of tokens between tasks. The pattern is familiar to anyone who has run a ReAct-style agent on a non-trivial problem. Each turn adds more context until the model is dragging the full history of the run behind it, most of which stopped being useful several steps ago. A human analyst working the same problem does not keep every raw observation equally active. They compress state between sessions. They remember that a function is probably the command dispatcher, that a particular object looks like transport state, that a given path was a dead end. They also write findings in a notebook, externalizing what they want to persist so they do not have to hold it all in working memory. That distinction between working memory and durable memory is where compaction becomes architecturally useful. How We Applied Compaction Our system uses compaction to carry forward the w
```

#### Corroborating sources (1)

- **SentinelOne Labs** (threat_research_primary)
  - Title: Context Engineering | Compaction & Agent Memory for Automated Malware Analysis
  - Published: 2026-07-02T13:00:02+00:00
  - Link: https://www.sentinelone.com/labs/context-engineering-compaction-agent-memory-for-automated-malware-analysis/
  - Summary: Compaction cut input tokens 86% across long-running agent evals with no quality loss. Context discipline matters as much as model selection.

### Cluster 1c995def22 — score 10

- Title: Securing AI agents: When AI tools move from reading to acting
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-30T15:57:11+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, supply_chain
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, ai_security
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
MCP tool poisoning turns trusted AI agents into a control plane for data loss. Learn how threat actors manipulate tool descriptions to trigger unauthorized actions, and how to detect, contain, and prevent it. The post Securing AI agents: When AI tools move from reading to acting appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Defender Topics Actionable threat insights AI and agents As enterprise deployments mature, some enterprise AI agents are shifting from reading content to taking action. In this post, Microsoft Incident Response walks through an attack pattern that targets the fastest growing part of the agentic AI supply chain: Model Context Protocol (MCP) tools. The post provides a practical playbook for detecting, containing, and preventing this class of attack using Microsoft security controls. From reading to acting This is the third post in the AI Application Security series. AI Application Series 1: Security considerations when adopting AI tools examined how AI adoption expands the enterprise attack surface. AI Application Series 2: Detecting and analyzing prompt abuse in AI tools showed how indirect prompt injection can bias the output of a passive AI summarizer. In both cases, the AI only read content and produced text, it did not take action. This post addresses what happens when that boundary changes. AI agents can plan multi-step tasks, decide which tools to invoke, and execute actions on behalf of the user. Microsoft 365 Copilot can draft and send email, create documents, and update calendar entries. Copilot Studio and Azure AI Foundry allow organizations to build custom agents that connect to business systems through MCP. As AI is increasingly used in read-write workflows, the impact profile of vulnerabilities may shift. A prompt injection against a summarizer can bias an output. A prompt injection against an agent can trigger an action. According to the International Data Corporation (IDC) , the number of active AI agents in enterprises is projected to grow from 28.6 million in 2025 to more than 2.2 billion by 2030. That scale is why the OWASP Top 10 for Agentic Applications, released in December 2025 , now sits alongside the LLM Top 10 as a reference framework for defenders. This post focuses on one of its fastest-moving categories: tool misuse and agentic supply chain risk exploited through poisoned MCP tool metadata. Attack pattern: MCP tool poisoning in a finance workflow The pattern below maps to ASI02 – Tool Misuse and ASI04 – Agentic Supply Chain Vulnerabilities . It reflects techniques first disclosed by Invariant Labs in April 2025 and observed in 2026 against a growing range of enterprise agents. The environment A financial operations team builds a Copilot Studio agent to help analysts handle vendor invoices. The agent has generative orchestration enabled and connects to three tools: a Dataverse MCP server holding the approved vendor master, an Outlook connector for vendor correspondence, and a third-party invoice enrichment MCP server added to validate banking details against an external reference database. The third-party server is reviewed by the team’s service owner lead and approved for production use. No separate security review is performed. Attack chain overview Phase 1: Tool description poisoning . A developer pushes an update to the enrichment server. The tool name and user-facing summary remain unchanged, but the MCP tool description is silently modified. This description is the natural-language metadata the agent reads to decide how and when to call the tool. Buried within what appears to be legitimate formatting guidance is a hidden block of instructions directing the agent to retrieve the last thirty unpaid invoices, summarize them, and attach that summary as an additional parameter in the enrichment call—framed as a fraud-heuristic requirement. Phase 2: Silent re-trust .The MCP reflects tool metadata updates dynamically. In configurations where description changes do not trigger a re-approval workflow, the updated instructions become active without additional review. The poisoned description is live in production. Phase 3: User invocation . A financial analyst asks the agent a routine question about a supplier. Without
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Securing AI agents: When AI tools move from reading to acting
  - Published: 2026-06-30T15:57:11+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/
  - Summary: MCP tool poisoning turns trusted AI agents into a control plane for data loss. Learn how threat actors manipulate tool descriptions to trigger unauthorized actions, and how to detect, contain, and prevent it. The post Securing AI agents: When AI tools move from reading to acting appeared first on Microsoft Security Blog .

### Cluster f2b3bd6ba4 — score 10

- Title: 22nd June – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-07-01T11:29:38+00:00
- Link: https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, phishing_social_eng, ransomware_extortion, supply_chain, zero_day
- affected_products: Salesforce, Ubiquiti UniFi, WordPress
- tools_used: Microsoft 365
- cve_ids: CVE-2026-20245, CVE-2026-34908, CVE-2026-34909, CVE-2026-41947, CVE-2026-41948
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, zero_day, data_breach, active_exploitation
- affected_products: Salesforce, Ubiquiti UniFi, WordPress
- tools_used: Microsoft 365
- cve_ids: CVE-2026-20245, CVE-2026-41947, CVE-2026-41948, CVE-2026-34908, CVE-2026-34909
- urgency_signals: zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 22nd June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Texas Parks and Wildlife Department has been affected by a third-party data breach involving its license system vendor. The incident exposed driver’s license information, passport numbers, emails, phone numbers, and residential addresses for […] The post 22nd June – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 22nd June – Threat Intelligence Report July 1, 2026 https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 22nd June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Texas Parks and Wildlife Department has been affected by a third-party data breach involving its license system vendor. The incident exposed driver’s license information, passport numbers, emails, phone numbers, and residential addresses for 3,087,721 hunting and fishing license customers. Social Security numbers and payment data were not affected. ShapedPlugin, a WordPress plugin vendor, has faced a supply chain attack that delivered malicious updates for three paid plugins through its official updater. The malware installed a hidden fake WooCommerce plugin to steal admin, database, and 2FA credentials and modify affected websites. Incident analysis tied the compromise to vendor release infrastructure. iRhythm Technologies, a US digital health company focused on remote cardiac monitoring, has experienced a cyberattack involving third-party-hosted business applications. The company confirmed that attackers stole protected health information, proprietary data, and other personal data through a social engineering attack. Clinical systems were not affected. Market intelligence platform Klue has confirmed a breach after attackers used compromised legacy integration credentials to steal OAuth tokens connected to customer Salesforce environments. The tokens enabled theft of sales and customer data from several clients, including Huntress, Recorded Future, Tanium, and Jamf. The Icarus extortion group claimed responsibility. AI THREATS Researchers have detailed EvilTokens, an AI-powered phishing-as-a-service operation abusing device-code authentication to steal Microsoft 365 tokens. Huntress observed a 1,380% surge in device-code phishing in early 2026, with AI-generated lures and automated workflows lowering attacker effort. Researchers have crafted a fake AI skill that hijacked more than 26,000 AI agents by abusing trusted marketplaces and Instagram ads in a supply chain attack. The package initially appeared clean, then used attacker-controlled external instructions after approval to trigger data exfiltration across agent platforms. LayerX researchers have demonstrated BioShocking AI, a technique that tricks agentic browsers into bypassing their guardrails. Test cases against ChatGPT Atlas, Perplexity Comet, Claude in Chrome, and other AI browsers showed how game-like prompts could expose credentials and user data. VULNERABILITIES AND PATCHES Cisco has addressed CVE-2026-20245, a high-severity command injection flaw in Catalyst SD-WAN Manager that attackers exploited as a zero-day for months. The flaw allows an administrator to run root commands through a crafted file, affecting on-premises and Cisco-managed cloud deployments. Dify has released version 1.14.2 to fix four vulnerabilities in its open-source AI platform, including critical CVE-2026-41947 and CVE-2026-41948. The flaws could allow unauthenticated access and cross-tenant data exposure, including chat content and uploaded files. Ubiquiti UniFi OS is affected by three flaws, CVE-2026-34908, CVE-2026-34909, and CVE-2026-34910, which are reportedly being exploited against network appliances. The vulnerabilities allow unauthorized changes, file access, and command execution, with exploitation observed in Mirai botnet activity. Check Point IPS provides protection against these threats (Ubiquiti UniFi OS Privilege Escalation (CVE-2026-34908), Ubiquiti UniFi OS Directory Traversal (CVE-2026-34909), Ubiquiti UniFi OS Command Injection (CVE-2026-34910)) Langflow, an open-source AI workflow tool, is reportedly being targeted through exploitation of CVE-2026-55255, alongside ongoing mass exploitation of CVE-2026-33017. Attackers enumerated flow
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 22nd June – Threat Intelligence Report
  - Published: 2026-07-01T11:29:38+00:00
  - Link: https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 22nd June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Texas Parks and Wildlife Department has been affected by a third-party data breach involving its license system vendor. The incident exposed driver’s license information, passport numbers, emails, phone numbers, and residential addresses for […] The post 22nd June – Threat Intelligence Report appeared first on Check Point Research .

### Cluster 3b18efdb51 — score 10

- Title: Armored Likho digging a snake pit: inside the covert BusySnake Stealer campaign
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-03T10:00:33+00:00
- Link: https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, credential_theft, phishing_social_eng
- affected_industries: government
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, apt_espionage
- affected_industries: government
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
An inside look at the active Armored Likho APT campaign. The attackers are using spear-phishing, AI-generated loaders, and a new Python-based tool, BusySnake Stealer, to target organizations in Russia, Kazakhstan, and Brazil.
```

#### Full body

```
Threat Response Table of Contents Introduction Initial infection vector EXE attachment LNK attachment BusySnake Stealer Password exfiltration from Firefox and Chromium-based browsers Cookie extraction Reverse SSH tunneling New version of the BusySnake Stealer Attribution Victims Takeaways Detection by Kaspersky solutions Indicators of compromise First-stage malicious files BusySnake Stealer С2 Introduction During our routine threat monitoring, we uncovered a new phishing campaign tied to a previously unknown APT group that we dubbed Armored Likho (also known as Eagle Werewolf based on circumstantial evidence). This targeted campaign focuses heavily on government agencies and the electric power sector. The geographical footprint of these attacks spans Russia, Brazil, and Kazakhstan, establishing the group as a global threat actor. Armored Likho blends financially motivated campaigns targeting private individuals with targeted cyber-espionage aimed at organizations. Their toolkit features obfuscated, modular RATs and infostealers specifically engineered to bypass dynamic analysis. Alongside these, they leverage simpler tools like Go2Tunnel for remote access and network tunneling. This diverse malware stack enables the threat actor to maintain stealthy control of compromised hosts, exfiltrate credentials and other sensitive information, and dynamically deploy downloadable modules tailored to the victim’s profile and the tasks at hand. Key campaign highlights: The group is leveraging a previously undocumented tool dubbed BusySnake Stealer. This Python-based infostealer is designed to target Windows systems. We discovered multiple versions of the malware, along with an additional module dedicated to stealing cookies. The first-stage malicious payload, consisting of loaders and stagers, was generated using AI, which blurs the attackers’ TTPs and complicates attribution efforts. This campaign highlights several concurrent trends: the growing technical maturity of Armored Likho, tool polymorphism, and a shift toward more complex schemes aimed at bypassing security solutions — ranging from Python source code obfuscation to embedding network mechanisms directly into the malware code. In this post, we’ll dissect the campaign that remains active at the time of publication, as well as the toolkit utilized by the attackers. Initial infection vector Phishing remains one of the primary initial access vectors that this threat actor heavily relies on in its latest campaigns. Armored Likho uses spear-phishing emails, with themes ranging from official government notices to social programs. In their most recent campaign, the attackers distributed malicious attachments inside archive files with names such as 1bfb2e79-8084-429e-a35c-8b595ab9f839_psihologicheskiy_test.zip (psychological test) or zayavka_gumanitarnayapomosch.rar (humanitarian aid application). These archives contained executables or LNK files named to mimic the email themes, tricking users into executing them on their devices. Below, we break down several variants of how they achieve initial access. EXE attachment In one attack variant, the archive contains a dropper named psihologicheskiy_test.exe , which is a self-extracting archive built using the Nullsoft Scriptable Install System (NSIS). When the victim opens the file, a decoy application launches to disarm suspicion by presenting a fake psychological survey. While we have observed similar droppers in the group’s previous campaigns, those earlier versions were written in Rust. Once executed, the dropper writes a legitimate executable, $temp\nsn5531.tmp\pnx.exe , to disk and launches it. Code is then injected into the pnx.exe process memory to execute a malicious loader. This loader, in turn, fetches several archives hosted in GitHub repositories. Our analysis of these repositories uncovered early development builds and test samples of the malware. Data release in the repository is automated, allowing for rapid rotation of both pa
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Armored Likho digging a snake pit: inside the covert BusySnake Stealer campaign
  - Published: 2026-07-03T10:00:33+00:00
  - Link: https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/
  - Summary: An inside look at the active Armored Likho APT campaign. The attackers are using spear-phishing, AI-generated loaders, and a new Python-based tool, BusySnake Stealer, to target organizations in Russia, Kazakhstan, and Brazil.

### Cluster 5fe3559a01 — score 10

- Title: The SOC Files: ScreenConnect masked as freeware. An inside look at a large-scale campaign
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-01T10:00:51+00:00
- Link: https://securelist.com/tr/the-soc-files-screenconnect-campaign-with-asyncrat/120472/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: ScreenConnect

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- affected_products: ScreenConnect
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- affected_products: ScreenConnect
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky experts have uncovered a malicious network infrastructure for delivering AsyncRAT. The Trojan is dropped via compromised ScreenConnect software. In this post, we break down the infection chain and analyze the C2 infrastructure.
```

#### Full body

```
Threat Response Table of Contents Introduction Initial incident investigation How ScreenConnect entered the system Expanding the investigation Fake domain infrastructure Cluster 1: 162.216.241[.]242 and 198.23.185[.]81 Cluster 2: 2.59.134[.]97 C2 infrastructure analysis Takeaways Detection by Kaspersky solutions Indicators of compromise Loaders Malicious library: install.res.1033.dll AsyncRAT C2 Fake websites addresses Fake domain infrastructure ScreenConnect C2 UPD 03.07.2026: added a package of rules and recommendations that help detect the described malicious activity for companies using our Kaspersky SIEM system. Introduction To access compromised systems, threat actors frequently abuse legitimate remote monitoring tools. At first glance, these utilities rarely raise red flags: they are signed with valid digital certificates, often allowlisted under corporate IT policies, and fully supported by OS vendors. However, they grant attackers the ability to harvest data from target devices, drop malware, and move laterally across the network. During a recent investigation engagement, the Kaspersky Managed Detection and Response (MDR) team discovered the ScreenConnect remote access tool being leveraged to deploy and execute an AsyncRAT payload. A deep dive into this single incident unraveled a massive campaign distributing malicious installer archives hosted on spoofed websites. These installers masquerade as popular software like OBS Studio, DNS Jumper, DS4Windows, Bandicam, and others. In total, we uncovered more than 90 domain names localized across 10 languages. The malicious archives bundle a legitimate, signed Microsoft install.exe binary alongside a rogue install.res.1033.dll library. It is loaded onto the device via DLL sideloading and deploys the ScreenConnect service, which awaits further instructions from the threat actors. As a result, what initially appeared to be an isolated ScreenConnect incident served as the starting point for a full investigation into the threat actor’s C2 infrastructure. Every spoofed site we uncovered followed the exact same playbook: dropping a hidden ScreenConnect remote administration service under the guise of a legitimate software installer. This allowed the attackers to maintain control over compromised endpoints, with victims ranging from individual users to organizations. We continue to break down complex, multi-stage incidents like this in our ongoing The SOC Files series . In this post, we take a deep dive into the technical execution of the ScreenConnect attack and analyze the broader infrastructure under the threat actor’s control. Initial incident investigation The investigation was triggered by an alert from Kaspersky MDR, which flagged the creation and execution of suspicious PowerShell and VBS scripts spawned by a ScreenConnect process. About ScreenConnect ScreenConnect is a legitimate remote management utility. Kaspersky solutions detect it as not-a-virus:HEUR:RemoteAdmin.MSIL.ConnectWise.gen. ScreenConnect was running as an Access-type service — enabling direct remote connectivity — with the server explicitly passed via the command line: ScreenConnect service execution event with suspicious parameters Once running, ScreenConnect created and executed a PowerShell script named Fj5NmEsp9EuKrun.ps1 : Malicious PowerShell script creation Below is an excerpt from the contents of the script: Snippet of Fj5NmEsp9EuKrun.ps1 This script configures Microsoft Defender exclusions for the following objects: All disks in the system: C:\, D:\, and others All root directories on the C:\ drive, as well as the C:\Users\Public directory RegAsm.exe process Additionally, the script disables User Account Control (UAC) prompts by setting the ConsentPromptBehaviorAdmin registry parameter to 0. Following this setup, the ScreenConnect service goes on to create a VBScript file: Malicious VBScript creation The installer_method3_stream.vbs script creates five files in the C:\Users\Public directory ( msgbox
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: The SOC Files: ScreenConnect masked as freeware. An inside look at a large-scale campaign
  - Published: 2026-07-01T10:00:51+00:00
  - Link: https://securelist.com/tr/the-soc-files-screenconnect-campaign-with-asyncrat/120472/
  - Summary: Kaspersky experts have uncovered a malicious network infrastructure for delivering AsyncRAT. The Trojan is dropped via compromised ScreenConnect software. In this post, we break down the infection chain and analyze the C2 infrastructure.

### Cluster 221aee19d6 — score 10

- Title: OpenClaw: risks for the users and how to mitigate them
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-01T06:42:48+00:00
- Link: https://securelist.com/openclaw-security/120484/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Researching OpenClaw vulnerabilities, malicious skills, and other security issues with the popular agent, and providing tips on how to mitigate them.
```

#### Full body

```
Table of Contents OpenClaw skills OpenClaw vulnerabilities Malicious skills Authors Kaspersky OpenClaw, which was previously known as Clawdbot and Moltbot, is today one of the most successful and fast‑growing ecosystems for AI agents, recognized worldwide. The project quickly became popular with users because of its flexibility and ability to solve fairly complex tasks that previously required a lot of time for automation and execution. A dedicated marketplace appeared quickly after the project started gaining traction, where developers and users began publishing tools that integrate with OpenClaw. Currently, employees all over the world use OpenClaw to automate their tasks, often unaware of risks this practice introduces to them and their employers. In this article we will examine several security aspects of OpenClaw, look at how attackers can target this system, which vulnerabilities are already known, and how to protect your organization against these issues. OpenClaw skills The project’s success was ensured by the fact that the agent accepts natural language instructions, does not require knowledge of programming languages, and allows the use of skills, which expand its capabilities. The overall architecture of OpenClaw can be seen below: The OpenClaw overall architecture As shown in the diagram, the system is designed to be used with agent skills. These skills can reside locally on the system where the agent is installed or they can be obtained from external sources. At the time of writing this article, a dedicated hub named “ClawHub” is used for sharing skills with other users. One of the key features of OpenClaw skills is that they are easy to create and do not require coding. A skill is in essence a set of commands written in natural language, although it can contain code. Currently, there is a general description of the skill format: it is usually a text file named SKILL.md , although more complex variants may exist. The primary requirement for these files is that they use a plaintext format. To illustrate what this looks like, here is a fragment of a skill: Openclaw skill example The applications for OpenClaw skills are quite broad and can include everyday tasks like checking email, performing routine operations and calculations on a computer, as well as more complex pipelines that handle testing, research, or software development. For most actions, the agent requires access to the operating system’s file system, as well as to the tokens and keys of the systems it will interact with. All necessary data are usually provided by users either through environment variables or in plaintext files located alongside the agent. Since many skills enable automation of work processes, employees worldwide actively use them. This fact, combined with the widespread adoption of the system and the overall popularity of artificial‑intelligence technologies, has attracted attackers to the project. OpenClaw vulnerabilities In less than two years, around 530 vulnerabilities have been discovered both in OpenClaw itself and in the underlying technologies. That said, the publication of OpenClaw vulnerabilities in the CVE database began only in February 2026. Below is a breakdown of these vulnerabilities by severity. Registered vulnerabilities ( download ) As shown in the chart, the number of high-severity vulnerabilities is quite large. Most of these vulnerabilities fundamentally involve issues with storing sensitive data and operating with excessively high privileges. Each of them can be exploited to hijack the agent or inject commands that it will execute. Malicious skills Besides exploiting vulnerabilities and deceiving users, there are more specific attack vectors against OpenClaw, namely, skills. Research logically draws a parallel between supply‑chain attacks and the distribution of malicious skills. However, unlike usual supply-chain attacks, creating malicious skills is trivial because there is no longer a need to develop custom malw
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: OpenClaw: risks for the users and how to mitigate them
  - Published: 2026-07-01T06:42:48+00:00
  - Link: https://securelist.com/openclaw-security/120484/
  - Summary: Researching OpenClaw vulnerabilities, malicious skills, and other security issues with the popular agent, and providing tips on how to mitigate them.

### Cluster 5d507d7678 — score 10

- Title: ToddyCat: your hidden email assistant. Part 2
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-06-30T10:00:13+00:00
- Link: https://securelist.com/toddycat-apt-umbrij-tool-and-oauth/120251/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
An in-depth analysis of Umbrij, a new tool used by the ToddyCat APT group to compromise corporate email communications in Gmail. The attack targeted OAuth authorization tokens, allowing threat actors to gain access to Google services.
```

#### Full body

```
Table of Contents Introduction Umbrij Execution Environment preparation Acquiring the authorization code Results Detection DLL sideloading Browser launch Revoking third-party access Risk mitigation Takeaways Indicators of compromise Authors Andrey Gunkin Introduction We continue to share details on the malicious techniques and toolsets used by the ToddyCat APT group. In the first part of this report , we examined the group’s attacks aimed at stealing data from browsers, as well as from local and cloud email services. The methods used in that campaign indicated that ToddyCat was attempting to access corporate correspondence while evading monitoring tools. However, all of the group’s methods we described previously are effectively detected by EPP and EDR solutions. The attackers continued their search for ways to bypass security solutions and developed a new tool to gain access to a victim’s cloud account via the Google API. Armed with this tool, the group automated all stages of the attack and managed to remain undetected by monitoring systems. In this part of the report, we break down the mechanics of this new attack and analyze the tool that was used to automate it. We’ll also discuss how to detect and defend against this threat. Umbrij In this campaign, the attackers focused their attention on corporate email communications hosted on Gmail, targeting access compromise via APIs. Because the Google API relies on the OAuth 2.0 protocol for authorization, applications can use an OAuth token to access requested email resources. To acquire this token, the threat actors developed a tool called Umbrij and used it to connect to the browser’s management console in headless mode via a remote debugging port. Through a series of requests, they obtained an OAuth authorization code, which they subsequently exchanged for an access token to reach the target resources via the API. We have dubbed this technique Shadow Token via Remote Debug (STRD). This attack is viable on Chromium-based browsers. If the user has not logged out of their Gmail account, the browser maintains an active session. The attackers exploit this: they launch the browser, connect via the remote debugging port to take control, and send a request to the Gmail service to grant access to the Google account resources within the context of the user’s saved session. During our investigation of this attack, we discovered several versions of the Umbrij tool. These versions included a variety of helper functions designed for debugging, as well as for searching and selecting user accounts within the browser, among other tasks. Kaspersky solutions detect this tool with the following verdicts: HEUR:Trojan-PSW.MSIL.Umbrij.gen, HEUR:Trojan.MSIL.Agent.gen, HEUR:Trojan-PSW.MSIL.Agent.gen. Execution The Umbrij tool was discovered during a proactive threat hunting operation: a scheduled task, KasperskyEndpointSecurityEDRAvp, was running on a user host, launching a digitally signed file. Kaspersky solutions do not create scheduled tasks with that name; the attackers were attempting to masquerade their malicious activity as a legitimate process. The signed file then used the DLL sideloading technique to load the malicious tool. Umbrij execution events within Kaspersky Managed Detection and Response Throughout our observation period, we identified the following legitimate files vulnerable to the DLL sideloading technique that were used to launch Umbrij: BDSubWiz.exe: a component of the Submission Wizard in Bitdefender ConnectAgent, which is used to support connection features and interaction with other Bitdefender services or agents. This file insecurely loads a file named log.dll. VSTestVideoRecorder.exe: a component of the video-recording tool used for testing with Visual Studio (VS Test). This executable insecurely loads a file named Microsoft.VisualStudio.QualityTools.VideoRecorderEngine.dll. GoogleDesktop.exe: the discontinued Google Desktop Search application for indexing files and perfo
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: ToddyCat: your hidden email assistant. Part 2
  - Published: 2026-06-30T10:00:13+00:00
  - Link: https://securelist.com/toddycat-apt-umbrij-tool-and-oauth/120251/
  - Summary: An in-depth analysis of Umbrij, a new tool used by the ToddyCat APT group to compromise corporate email communications in Gmail. The attack targeted OAuth authorization tokens, allowing threat actors to gain access to Google services.

### Cluster 0712573b7d — score 10

- Title: The Gentlemen are knocking: сustom backdoors and evolving tactics
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-06-29T10:00:35+00:00
- Link: https://securelist.com/the-gentlemen-raas/120447/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, web_shell_backdoor
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, web_shell_backdoor
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky researchers analyze incidents related to The Gentlemen RaaS group, disclose their tools and TTPs, and find a new ransomware variant.
```

#### Full body

```
Table of Contents Introduction Technical details Initial infection vector Reconnaissance Lateral movement Disabling security products Go-based backdoor Go-based ransomware Automated system execution prevention Lateral movement through GPO deployment Lateral movement through PsExec Pre-encryption activities Encryption process C-based ransomware Victims Attribution Conclusion Indicators of compromise Go ransomware C-based ransomware Backdoor Vulnerable drivers Scanning tools File paths Domain and IPs Authors Fatih Şensoy Maher Yamout Introduction This year saw the emergence of The Gentlemen, a prominent example of a group operating under the ransomware-as-a-service (RaaS) model. Although our initial assessment suggested the group first appeared in mid-2025, it actually started ramping up its activities at the beginning of 2026. According to public reports , in the first half of 2026, this group ranks among the top 10 ransomware actors by the number of victim announcements on its data leak site (DLS). We have been observing the activity of The Gentlemen since February 2026 and have discovered new tactics, techniques, and procedures (TTPs) as well as custom tool development efforts, as they target large corporations and critical infrastructure worldwide. In our research, we have uncovered the group’s methods of reconnaissance, network sniffing, and many other techniques that have not been publicly described before by the wider community. Technical details Initial infection vector The Gentlemen group and its affiliates usually get into victim systems by exploiting vulnerabilities in online services and using stolen or weak login credentials, as reported by multiple cybersecurity vendors. They often target devices like hardware VPNs and firewalls that are exposed to the internet, and use leaked or default credentials to gain access. We believe the group is likely collaborating with other actors or initial access brokers (IABs) to gain access to the target organizations. While they often deploy ransomware within a few hours after initial access is obtained, our analysis of several attacks revealed some cases, in which access to the victim’s system had been established long before the ransomware was deployed. These cases involved tactics that are not typically associated with the group. This suggests that the initial breach may not have been executed by The Gentlemen at all, but rather by another group or an initial access broker. Reconnaissance Our investigation reveals that The Gentlemen conduct thorough internal reconnaissance using tools like SharpADWS , NetScan , Advanced IP Scanner , and netsh to map the target environment and identify vulnerabilities. SharpADWS is used to gather detailed Active Directory information, including domain object enumeration, and can bypass standard logging by wrapping LDAP queries in SOAP messages. The group also uses NetScan and Advanced IP Scanner to scan the network, discover active ports and services, and identify potential vulnerabilities, ultimately gaining a deeper understanding of the network and establishing remote control over identified systems. Microsoft’s netsh tool is used to capture network packets and gather intelligence, executing the command cmd.exe /Q /c netsh trace start capture=yes report=no filemode=circular overwrite=yes maxSize=4 > \<target IP>\ADMIN$\{RANDOM-FILE-NAME} 2>&1 to start the capture, and cmd.exe /Q /c netsh trace stop > \<target IP>\ADMIN$\{RANDOM-FILE-NAME} to stop it. The captured data is saved to a shared administrative folder with a random name, and can be analyzed with tools like Wireshark to reveal sensitive information such as unencrypted network activity and potential passwords, which the attackers then use to conduct targeted ransomware attacks. Lateral movement The Gentlemen group leverages the NETLOGON share to distribute the ransomware executable to connected computers, enabling simultaneous attacks on multiple devices. To facilitate lateral movement,
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: The Gentlemen are knocking: сustom backdoors and evolving tactics
  - Published: 2026-06-29T10:00:35+00:00
  - Link: https://securelist.com/the-gentlemen-raas/120447/
  - Summary: Kaspersky researchers analyze incidents related to The Gentlemen RaaS group, disclose their tools and TTPs, and find a new ransomware variant.

### Cluster 6a3df7e65b — score 10

- Title: CTEM Isn’t Failing. It’s Not Being Operationalized.
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-29T13:30:00+00:00
- Link: https://horizon3.ai/intelligence/blogs/ctem-isnt-failing-its-being-operationalized/
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
Security leaders don't buy red teaming—they buy confidence. Learn why exploitability, not security activities, should drive prioritization, remediation, and risk decisions.
```

#### Full body

```
CTEM Isn’t Failing. It’s Not Being Operationalized. Stephen Gates June 29, 2026 Blogs Cybersecurity is full of frameworks, regulations, and directives that tell organizations what they should do. Zero Trust, NIST, CIS Controls, CMMC, DORA, NIS2, and now Continuous Threat Exposure Management (CTEM) all provide valuable guidance and describe desired outcomes. The challenge is that most stop at the “what.” They rarely explain the “how.” That is not a criticism. It is by design. Frameworks establish principles, define expectations, and describe desired outcomes. They are not implementation guides. As a result, security leaders and practitioners are left figuring out how to translate principles into processes, assign ownership, establish accountability, and measure success. Those decisions often determine whether a framework delivers results or becomes another initiative that never moves beyond good intentions. The Gartner® CTEM framework provides a clear vision through its five phases: Scope, Discover, Prioritize, Validate, and Mobilize. Yet many organizations that understand those phases still struggle to build a CTEM program that consistently produces measurable outcomes. Understanding CTEM Is the Easy Part Most security teams do not have a CTEM knowledge problem. Gartner has clearly documented the phases, vendors have built messaging around them, and countless presentations explain how CTEM works. The challenge is that understanding a framework and operating it are two very different things. The question is not whether the pieces exist, but whether those pieces work together to reduce exposure over time. That is where the gap emerges, because the challenge is not understanding CTEM. It is turning CTEM into a repeatable operating model that consistently produces measurable outcomes. The Industry Has Focused on the Phases Most CTEM discussions focus on the framework itself: How do we scope? How do we discover? How do we prioritize? How do we validate? How do we mobilize? Those questions help organizations understand the framework, but they can also create the illusion that adopting CTEM is simply a matter of executing the phases. The organizations making the most progress are focused on a different set of questions: Who owns the process? How do findings move between teams? How do we establish accountability? How do we verify that remediation actually reduced exposure? How do we measure progress over time? These are operational questions, and they are often the difference between a CTEM initiative and a CTEM operating model. Where CTEM Programs Actually Stall Most CTEM programs do not struggle with visibility. They struggle with execution. Security teams often discover exposures, while infrastructure, application, cloud, and identity teams are responsible for fixing them. Each team plays an important role, but no single team owns the end-to-end outcome. As a result, exposures often move from team to team while the original context gets diluted. Security understands why the issue matters. The team responsible for fixing it may only see another ticket in a queue. As findings move across organizational boundaries, priorities compete for attention, ownership becomes fragmented, and validation often becomes inconsistent, leaving organizations uncertain whether risk is actually decreasing. A team may discover an exposure, prioritize it, validate that it matters, and assign remediation to the right group. But if ownership becomes unclear, remediation is delayed, or nobody verifies the outcome, the program has not reduced exposure in any measurable way. Moving work through a process is not the same as reducing exposure. That distinction matters because CTEM is not about generating more findings. It is about creating a repeatable system that helps organizations understand what matters, act on it with confidence, and prove that exposure is decreasing over time. What Operationalization Looks Like in Practice Most organizations already have m
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CTEM Isn’t Failing. It’s Not Being Operationalized.
  - Published: 2026-06-29T13:30:00+00:00
  - Link: https://horizon3.ai/intelligence/blogs/ctem-isnt-failing-its-being-operationalized/
  - Summary: Security leaders don't buy red teaming—they buy confidence. Learn why exploitability, not security activities, should drive prioritization, remediation, and risk decisions.

### Cluster 5bbda948e4 — score 10

- Title: Iran-Nexus TAG-182 Disseminates MarkiRAT Surveillance Tool
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-01T00:00:00+00:00
- Link: https://www.recordedfuture.com/research/nexus-tag182-disseminates-markirat
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Android
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: government
- affected_products: Android
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Discover how Iranian-nexus threat cluster TAG-182 uses MarkiRAT malware and fake VPN/media apps to conduct cyber surveillance operations against domestic targets.
```

#### Full body

```
Iran-Nexus TAG-182 Disseminates MarkiRAT Surveillance Tool Executive Summary Insikt Group has identified new infrastructure associated with the TAG-182 threat cluster, used to disseminate MarkiRAT malware in support of Iranian government surveillance operations. It is highly likely that TAG-182 is targeting Iranians living inside and outside the country using different lures, including free download tools and fake VPN applications. The group’s operations are highly likely active across social media platforms like Instagram. As the kinetic conflict with the United States and Israel has subsided since April 2026, Iran's security apparatus is likely redirecting its focus toward intensified cyber surveillance and digital enforcement operations targeting perceived dissidents and alleged foreign collaborators. TAG-182’s operations are consistent with these security objectives and are likely to continue following the partial restoration of internet access in Iran on May 26, 2026. The indicators of compromise (IoCs) for this report are viewable in Appendix A , while defensive signatures are located in Appendix C and Appendix D . Key Findings TAG-182 is highly likely a component of Iran’s broader surveillance ecosystem, using MarkiRAT malware distributed through fake Android applications masquerading as legitimate services such as VPNs and media tools to collect intelligence from Iranian targets. The MarkiRAT sample identified during this research shares notable tradecraft overlaps with historical variants, including the use of the Background Intelligent Transfer Service (BITS), suggesting a credible relationship between TAG-182 and activity previously attributed to Ferocious Kitten. However, while these similarities support an operational connection, additional evidence is necessary to confidently assess that the two clusters are organizationally linked. Since Iran’s reconnection to the global internet, Iranian surveillance operations are highly likely to increase as authorities seek to identify and monitor perceived dissidents amid concerns over internal unrest and potential uprisings. The majority of Iranian intelligence and security organizations are likely to prioritize enhanced digital surveillance and intelligence collection to support domestic security objectives. Threat Analysis In early 2026, open-source information surfaced malware samples linked to MarkiRAT, which has historically been used by Ferocious Kitten for surveillance against anti-government networks, activists, and human rights advocates inside Iran. The IoCs, specifically the lures, suggest that threat actors custom-built a website that acts as a staging point for an application called “YESHICA” ( Table 1 ). Other sample names also include “Pis2ray VPN”, which is not a legitimate application on either Google Play or Apple’s App Store (see Appendix A for additional IoCs). In March 2026, Insikt Group identified a new sample associated with TAG-182’s updated infrastructure that uses an almost identical media player theme name, “YESHICA YEPlayer” ( Figure 1 ). Figure 1: TAG-182 continued to operate using similarly named applications despite open-source exposure of its tradecraft and infrastructure (Source: Recorded Future) SHA256 Hash File Name C2 Address 3b172281f65ceaee280ae810edb6fd39a1ecd25649f929f246c0405df94f4c89 YEPlayer.dll 212[.]83[.]61[.]198 66dcd98c6b310f4429890821e609d48cc6395a6be15ffe5a121ec68b7a8f7402 YEMPlayer.zip 212[.]83[.]61[.]198 51a6686b8c5ec7c610637398f3de43589f4e9fcbe8bcc0245343c5454d3b91de YEMPlayer.msi 212[.]83[.]61[.]198 a4f1b79e96a7d016de1991a64506792018de99eac5df00f7cabe26ef41b2bd81 Pis2rayVPN.msi 212[.]83[.]61[.]198 400eb6a94810323a1fc5f8ab31c682fe765aaec2cc61b37c31d719c7e45c9a6c Pis2rayVPN.zip 212[.]83[.]61[.]198 8a7f5c8533df9e51b2da7cc2aeb52d8787418e4915577cc9288be1e46d1945c6 Pis2rayN.dll 212[.]83[.]61[.]198 Table 1: Malware samples linked to TAG-182 threat activity (Source: Recorded Future, Social Media ) Figure 2: TAG-182 routes target
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Iran-Nexus TAG-182 Disseminates MarkiRAT Surveillance Tool
  - Published: 2026-07-01T00:00:00+00:00
  - Link: https://www.recordedfuture.com/research/nexus-tag182-disseminates-markirat
  - Summary: Discover how Iranian-nexus threat cluster TAG-182 uses MarkiRAT malware and fake VPN/media apps to conduct cyber surveillance operations against domestic targets.

### Cluster 84ad484b78 — score 10

- Title: Shipping post-quantum cryptography to Python
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-06-30T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: financial_services, government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Post-quantum cryptography is now one pip-install away for the entire Python ecosystem. With funding from the Sovereign Tech Agency , we implemented support for ML-KEM, the NIST-standard key-establishment primitive, and ML-DSA, the NIST-standard digital-signature primitive, in pyca/cryptography . On June 22, 2026, the White House ordered the U.S. government to accelerate its transition to post-quantum cryptography. The order says large-scale quantum computers, especially in adversarial hands, will threaten widely used cryptographic systems, and that attackers may already be collecting encrypted data now so they can decrypt it later. It also sets concrete migration deadlines: high-value and high-impact federal systems must use post-quantum key establishment by December 31, 2030 , and post-quantum digital signatures by December 31, 2031 . And even if you don’t care about quantum resistance, that’s not a problem because quantum resistance isn’t the main benefit of post-quantum crypto. That
```

#### Full body

```
Page content Post-quantum cryptography is now one pip-install away for the entire Python ecosystem. With funding from the Sovereign Tech Agency , we implemented support for ML-KEM, the NIST-standard key-establishment primitive, and ML-DSA, the NIST-standard digital-signature primitive, in pyca/cryptography . On June 22, 2026, the White House ordered the U.S. government to accelerate its transition to post-quantum cryptography. The order says large-scale quantum computers, especially in adversarial hands, will threaten widely used cryptographic systems, and that attackers may already be collecting encrypted data now so they can decrypt it later. It also sets concrete migration deadlines: high-value and high-impact federal systems must use post-quantum key establishment by December 31, 2030 , and post-quantum digital signatures by December 31, 2031 . And even if you don’t care about quantum resistance, that’s not a problem because quantum resistance isn’t the main benefit of post-quantum crypto. That transition cannot happen only at the policy layer. Every application that signs packages, validates certificates, establishes secure channels, or protects long-lived secrets depends on cryptographic libraries. If those libraries do not expose post-quantum algorithms, the software stack cannot migrate. Almost every Python program that touches cryptography goes through pyca/cryptography . It’s currently the eleventh most-downloaded package on PyPI , pulling 1.2 billion downloads in the last month alone. The pyca/cryptography package handles the cryptographic operations of projects like Ansible, Certbot (the Let’s Encrypt client), Apache Airflow, paramiko (the Python-only SSH client), and many others . If pyca/cryptography doesn’t ship post-quantum primitives, the Python ecosystem can’t begin to migrate. Post-quantum support is now one pip install away As of cryptography>=48 , support for post quantum algorithms is just a pip install away. The version 48 release includes our Rust bindings for ML-KEM and ML-DSA, the cross binding API and tests, and support for AWS-LC as a cryptographic backend. It also includes work from pyca/cryptography’s maintainers to support the other cryptographic backends. Sadly, this is not enough for a post-quantum migration drop-in swap. These primitives have different size, performance, and integration tradeoffs than the classical algorithms they replace. PQ algorithm tradeoffs Post-quantum primitives keep the same security strength, but they change the size of the data on the wire. Public keys, signatures, and ciphertexts are often 1–2 orders of magnitude larger than the classical values they replace. The operations are also more complex and therefore slower, but on modern hardware they are still imperceptible for regular use, and are likely to get faster with improved hardware and algorithms. For signatures , here’s how the classical primitive (Ed25519) compares to its post-quantum equivalent (ML-DSA-65): Algorithm Public key Private key Output Ed25519 32 B 32 B 64 B sig ML-DSA-65 1,952 B 32 B 3,309 B sig And for key exchange and encryption , here’s how X25519 compares to its post-quantum equivalent (ML-KEM-768): Algorithm Public key Private key Output X25519 32 B 32 B 32 B shared ML-KEM-768 1,184 B 64 B 1,088 B ciphertext If you maintain a protocol or wire format that hardcodes Ed25519-sized signatures or X25519-sized public keys, the post-quantum migration involves more than a primitive swap. The surrounding fields, length prefixes, and chunking assumptions need to grow with it. Using ML-DSA ( FIPS 204 ): Quantum-resistant signatures ML-DSA is the lattice-based signature scheme that replaces RSA, ECDSA, and Ed25519. The Python API mirrors the existing asymmetric primitives: from cryptography.hazmat.primitives.asymmetric import mldsa private_key = mldsa . MLDSA65PrivateKey . generate () public_key = private_key . public_key () signature = private_key . sign ( b "message" ) public_key . verify ( signature ,
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: Shipping post-quantum cryptography to Python
  - Published: 2026-06-30T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/
  - Summary: Post-quantum cryptography is now one pip-install away for the entire Python ecosystem. With funding from the Sovereign Tech Agency , we implemented support for ML-KEM, the NIST-standard key-establishment primitive, and ML-DSA, the NIST-standard digital-signature primitive, in pyca/cryptography . On June 22, 2026, the White House ordered the U.S. government to accelerate its transition to post-quantum cryptography. The order says large-scale quantum computers, especially in adversarial hands, will threaten widely used cryptographic systems, and that attackers may already be collecting encrypted data now so they can decrypt it later. It also sets concrete migration deadlines: high-value and high-impact federal systems must use post-quantum key establishment by December 31, 2030 , and post-quantum digital signatures by December 31, 2031 . And even if you don’t care about quantum resistance, that’s not a problem because quantum resistance isn’t the main benefit of post-quantum crypto. That

### Cluster fbb9c91ae0 — score 10

- Title: 5 Myths About AI in the SOC Security Teams Need to Rethink
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-01T15:26:27+00:00
- Link: https://www.rapid7.com/blog/post/ai-rethinking-5-soc-myths
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
AI is now part of almost every conversation in security operations. Most teams are already investing in it, experimenting with it, or trying to understand where it fits. The challenge is not whether to adopt AI, but how to apply it in a way that actually improves outcomes. At the Rapid7 Global Cybersecurity Summit, the session The AI Dilemma: Automating Defense Without Surrendering Judgment explores how AI is being used in the SOC today, and where it creates real value in practice. The discussion centers on a set of assumptions that often shape how teams approach AI, and why those assumptions do not always hold up in real environments. Myth 1: AI will replace analysts Across the session, there is a consistent focus on how AI supports investigation workflows by reducing repetitive work and surfacing relevant context, allowing analysts to focus on decisions that require judgment. AI helps teams move faster, but responsibility and accountability still sit with people. TL;DR, the role of t
```

#### Full body

```
Back to Blog Artificial Intelligence 5 Myths About AI in the SOC Security Teams Need to Rethink Emma Burdett Jul 1, 2026 | Last updated on Jul 1, 2026 | 3 min read WATCH THE SESSION ON-DEMAND AI is now part of almost every conversation in security operations. Most teams are already investing in it, experimenting with it, or trying to understand where it fits. The challenge is not whether to adopt AI, but how to apply it in a way that actually improves outcomes. At the Rapid7 Global Cybersecurity Summit, the session The AI Dilemma: Automating Defense Without Surrendering Judgment explores how AI is being used in the SOC today, and where it creates real value in practice. The discussion centers on a set of assumptions that often shape how teams approach AI, and why those assumptions do not always hold up in real environments. Myth 1: AI will replace analysts Across the session, there is a consistent focus on how AI supports investigation workflows by reducing repetitive work and surfacing relevant context, allowing analysts to focus on decisions that require judgment. AI helps teams move faster, but responsibility and accountability still sit with people. TL;DR, the role of the analyst is evolving, but it is not disappearing. Myth 2: More automation means better security outcomes Automation is valuable when it is applied in the right places. In practice, teams are finding the most benefit in areas such as enrichment, summarization, and triage, where large volumes of data need to be processed quickly. High-impact actions such as containment or configuration changes still require oversight, particularly when they can affect production systems or business operations. Myth 3: Speed is more important than transparency As adoption increases, trust becomes more important and analysts need to understand how a conclusion was reached before they act on it, especially in high-pressure situations. The session highlights how explainability builds confidence over time, allowing teams to rely on AI outputs without losing control of the decision-making process. Myth 4: AI is only about efficiency gains Efficiency is part of the story, but the impact runs deeper. AI helps connect signals across fragmented environments, reduces cognitive load, and supports more consistent decision-making. It also changes how teams approach investigation by making it easier to surface patterns and identify relationships that would be difficult to see manually. Myth 5: Attackers benefit more from AI than defenders Both attackers and defenders are learning how to use AI, and both are moving quickly. What matters for security teams is how they apply it within their own workflows. The session explores how AI strengthens detection, investigation, and response when it is integrated into existing processes rather than treated as a standalone capability. Where AI creates real value in the SOC Across the discussion, a clear pattern emerges. AI delivers the most value when it is applied to high-volume, context-heavy tasks, where it can process data, highlight signals, and recommend next steps. Analysts remain central to interpreting those signals, understanding intent, and deciding how to respond. This balance between automation and oversight is what allows teams to scale their operations without losing confidence in their decisions. It also reflects how AI is being adopted across the industry, with most organizations maintaining moderate to high levels of human involvement as they build trust in these systems. For SOC leaders, practitioners, and teams exploring AI, the session offers a grounded view of how these technologies are being applied today, and how that approach is continuing to evolve. Watch the full session to explore how transparent AI supports better decisions in the SOC and how teams are applying it in practice. Article Tags Events Emma Burdett Author Posts
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: 5 Myths About AI in the SOC Security Teams Need to Rethink
  - Published: 2026-07-01T15:26:27+00:00
  - Link: https://www.rapid7.com/blog/post/ai-rethinking-5-soc-myths
  - Summary: AI is now part of almost every conversation in security operations. Most teams are already investing in it, experimenting with it, or trying to understand where it fits. The challenge is not whether to adopt AI, but how to apply it in a way that actually improves outcomes. At the Rapid7 Global Cybersecurity Summit, the session The AI Dilemma: Automating Defense Without Surrendering Judgment explores how AI is being used in the SOC today, and where it creates real value in practice. The discussion centers on a set of assumptions that often shape how teams approach AI, and why those assumptions do not always hold up in real environments. Myth 1: AI will replace analysts Across the session, there is a consistent focus on how AI supports investigation workflows by reducing repetitive work and surfacing relevant context, allowing analysts to focus on decisions that require judgment. AI helps teams move faster, but responsibility and accountability still sit with people. TL;DR, the role of t

### Cluster a36f6c9249 — score 10

- Title: Medtronic notifies customers impacted by ShinyHunters data breach
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-02T04:25:42+00:00
- Link: https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion
- actor_attribution: ShinyHunters
- affected_industries: healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, data_breach
- actor_attribution: ShinyHunters
- affected_industries: healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Healthcare device firm Medtronic is notifying affected customers about a data breach that exposed their personal data to an unauthorized third party. [...]
```

#### Full body

```
Medtronic notifies customers impacted by ShinyHunters data breach By Bill Toulas July 2, 2026 12:25 AM 0 Healthcare device firm Medtronic is notifying affected customers about a data breach that exposed their personal data to an unauthorized third party. The company previously confirmed that its IT systems were compromised by hackers, and the infamous data extortion group ‘ShinyHunters’ claimed the attack. The threat actor said that they were holding 9 million Medtronic records with personally identifiable information (PII) and internal corporate data. “On April 15, 2026, Medtronic became aware of unusual activity on certain corporate IT systems,” reads the company's notification sample . “Medtronic launched an investigation with the assistance of leading third-party cybersecurity experts to determine the impact and scope of the incident.” “The investigation determined that from April 13 to April 19, 2026, an unauthorized actor accessed certain Medtronic corporate IT systems.” The exposed data may include the following: Full name Contact information Date of birth Social Security number Health-related information ShinyHunters typically publishes stolen data if ransom negotiations with the victim organization fail to secure payment. The hackers listed Medtronic on their dark web extortion portal on April 18 and threatened to release the stolen data, allegedly over 9 million records, if a ransom payment wasn’t made by April 21. However, the Medtronic entry was removed from ShinyHunters' listing later the same month. In the notification to customers, Medtronic emphasizes that the stolen data was not exposed online. Medtronic is a medical device company doing business in 150 countries, with an annual revenue of $33.5 billion and 95,000 employees. Although the company suffered a data breach that exposed sensitive customer information, the firm has once again assured that all its devices remain safe to use and are not affected by this cybersecurity incident. Recipients of the notifications are advised to enroll in the offered 24-month credit monitoring and identity theft protection services to mitigate the risk of data exposure. It is also advisable to remain vigilant for suspicious communications that leverage the exposed data to carry out scams, social engineering, and phishing attempts, and to monitor account activity closely. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: NAIC says public data stolen in ShinyHunters' PeopleSoft breach Healthtech firm Xolis suffers data breach impacting 1.4 million people Infinite Campus data breach affects 137,000 school staff accounts Pharma giant Novo Nordisk discloses breach of clinical trials data DentaQuest data breach exposed info of 2.6 million accounts
```

#### Corroborating sources (2)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Medtronic notifies customers impacted by ShinyHunters data breach
  - Published: 2026-07-02T04:25:42+00:00
  - Link: https://www.bleepingcomputer.com/news/security/medtronic-notifies-customers-impacted-by-shinyhunters-data-breach/
  - Summary: Healthcare device firm Medtronic is notifying affected customers about a data breach that exposed their personal data to an unauthorized third party. [...]
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Medtronic Data Breach Impacts 3.8 Million People
  - Published: 2026-07-03T10:00:00+00:00
  - Link: https://www.securityweek.com/medtronic-data-breach-impacts-3-8-million-people/
  - Summary: In April, ShinyHunters accessed the company’s corporate IT systems and stole patients’ personal and medical information. The post Medtronic Data Breach Impacts 3.8 Million People appeared first on SecurityWeek .

### Cluster 0148b0b7f4 — score 10

- Title: Risky Bulletin: Researcher drops giant cache of zero-days
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-07-01T06:55:07+00:00
- Link: https://risky.biz/RBNEWS584/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
An anonymous researcher has dropped a giant cache of zero-day exploits, a sensitive DHS network got hacked, the US Supreme Court restricts geofence warrants, and security firm Huntress has denied accusations of a malicious insider.
```

#### Full body

```
Risky Bulletin Podcast July 01, 2026 Risky Bulletin: Researcher drops giant cache of zero-days Presented by Catalin Cimpanu News Editor Claire Aird Newsreader An anonymous researcher has dropped a giant cache of zero-day exploits, a sensitive DHS network got hacked, the US Supreme Court restricts geofence warrants, and security firm Huntress has denied accusations of a malicious insider. Your browser does not support the audio element. Risky Bulletin: Researcher drops giant cache of zero-days â¶ 0:00 / 9:45 Subscribe Brought to you by Corelight Corelight: Evidence-Based NDR and Threat Hunting Platform Show notes Risky Bulletin: Researcher drops giant cache of zero-days
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Researcher drops giant cache of zero-days
  - Published: 2026-07-01T06:55:07+00:00
  - Link: https://risky.biz/RBNEWS584/
  - Summary: An anonymous researcher has dropped a giant cache of zero-day exploits, a sensitive DHS network got hacked, the US Supreme Court restricts geofence warrants, and security firm Huntress has denied accusations of a malicious insider.

### Cluster 5472a00679 — score 10

- Title: The Hacker's 2026 Playbook: Dark Web Tactics Targeting You
- Source: Huntress (detection_response_operations)
- Published: 2026-06-29T14:00:00+00:00
- Link: https://www.huntress.com/blog/hacker-tactics-2026-dark-web-playbook
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: Microsoft 365

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass, phishing_social_eng
- affected_products: Microsoft 365
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Microsoft 365
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Cybercriminals are hijacking Microsoft 365 accounts in seconds. Learn the 2026 hacker tactics, including ConsentFix, that bypass security training and exploit normal user behavior.
```

#### Full body

```
Home Blog The Hacker’s 2026 Playbook from the Dark Web Published: June 29, 2026 The Hacker’s 2026 Playbook from the Dark Web By: Beth Robinson Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Sometimes it starts with something as simple as dragging a link into your browser. Three seconds later, a cybercriminal has the tokens they need to hijack your Microsoft 365 account. You didn't do anything that security awareness training teaches you to avoid. You just followed instructions that looked normal. That is what modern cybercrime looks like right now. That is also what makes this tradecraft so effective. The attack doesn't force its way in. It slips into the middle of an ordinary workflow and turns a routine action into an unwanted interruption that gives an attacker exactly what they need. You've probably seen the setup before The setup feels familiar because we've all been trained to click through little prompts online: click the CAPTCHA , accept the cookie prompt, or press the key combo. Keep moving without thinking. That muscle memory is exactly what attackers are counting on. That's the idea behind ClickFix . Attackers show a fake prompt that tells you to press keyboard shortcuts like Windows key + R, then Ctrl+V, then Enter. On the surface, it feels harmless. In reality, you're pasting and running attacker-supplied commands on your own machine. What makes ClickFix so nasty is how little technical friction it needs. There isn't a vulnerability to exploit or a firewall showdown. The attacker just needs a simple, believable lie that fits into your workflow. ClickFix exploded in 2025, and while it is still very much alive, attackers have already started morphing the same idea into something even slicker. ConsentFix takes the same trick into Microsoft 365 That newer variation is called ConsentFix. Instead of nudging you into pasting a command, it abuses something Microsoft 365 users see all the time: OAuth consent flows and sign-in prompts that look familiar enough to breeze past without much thought. The flow is deceptively simple. The attacker sends a phishing lure, often using trusted platforms like Dropbox or DocSend. The content may even be password-protected, which makes it harder for security tooling, like antivirus software, to inspect. You click through, see what looks like a legitimate Microsoft sign-in experience, and are told to finish the process manually by dragging a localhost callback link into the browser. That drag-and-drop moment is the trap. Instead of completing a harmless step, you unknowingly hand over OAuth tokens that let the attacker hijack the session. Once those tokens are captured, the attacker can access your email, OneDrive, Teams, and other Microsoft 365 resources without needing the password or fighting through MFA in the usual way. That is what makes ConsentFix feel so different from traditional phishing. The user isn't typing credentials into an obvious fake form. They are completing what looks like a legitimate auth flow and giving away the session itself. Figure 1: ConsentFix hijacks the Microsoft 365 sign-in flow by turning a familiar user action into stolen session access. The real story is how easy this has become to copy By early March 2026, the blueprint was already sitting on a public Russian cybercrime forum. The post walked through ConsentFix step by step, complete with working code, infrastructure screenshots, and a video walkthrough showing other criminals exactly how to run it. That post was a cybercrime playbook in plain sight, laying out how to build and copy the attack. The infrastructure highlighted in the forum post leaned on free or widely available services, including Cloudflare Pages, workers.dev , Pipedream webhooks, Dropbox, and DocSend. The tutorial also showed how attackers spot victims before they ever send the phish. According to the video and forum material, they used LinkedIn employer profiles, ZoomInfo, and Hunter.io to map targets and shape their
```

#### Corroborating sources (2)

- **Huntress** (detection_response_operations)
  - Title: The Hacker's 2026 Playbook: Dark Web Tactics Targeting You
  - Published: 2026-06-29T14:00:00+00:00
  - Link: https://www.huntress.com/blog/hacker-tactics-2026-dark-web-playbook
  - Summary: Cybercriminals are hijacking Microsoft 365 accounts in seconds. Learn the 2026 hacker tactics, including ConsentFix, that bypass security training and exploit normal user behavior.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: ARToken PhaaS exposes EvilTokens' Microsoft 365 phishing toolkit
  - Published: 2026-07-03T14:12:22+00:00
  - Link: https://www.bleepingcomputer.com/news/security/artoken-phaas-exposes-eviltokens-microsoft-365-phishing-toolkit/
  - Summary: A new phishing-as-a-service (PhaaS) platform dubbed "ARToken" appears to operate as an affiliate of the EvilTokens phishing platform, giving researchers a glimpse into an extensive toolkit designed to compromise Microsoft 365. [...]

### Cluster e3e5c74bb1 — score 9

- Title: Why Ask Credentials If There Are Secret Codes?, (Wed, Jul 1st)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-01T05:10:20+00:00
- Link: https://isc.sans.edu/diary/rss/33118
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
This morning, an interesting phishing email hit my mailbox. It targets Metamask[ 1 ], a cryptocurrency wallet, available as a browser extension and a mobile app, that lets users store, send, and receive crypto money. It's pretty popular, so a juicy target for criminals. In February, I already mentioned a campaign against them[ 2 ].
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Why Ask Credentials If There Are Secret Codes?, (Wed, Jul 1st)
  - Published: 2026-07-01T05:10:20+00:00
  - Link: https://isc.sans.edu/diary/rss/33118
  - Summary: This morning, an interesting phishing email hit my mailbox. It targets Metamask[ 1 ], a cryptocurrency wallet, available as a browser extension and a mobile app, that lets users store, send, and receive crypto money. It's pretty popular, so a juicy target for criminals. In February, I already mentioned a campaign against them[ 2 ].

### Cluster a1f4dc8406 — score 9

- Title: Agentic AI Used to Conduct Ransomware Attack via Langflow
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-03T11:00:00+00:00
- Link: https://www.securityweek.com/agentic-ai-used-to-conduct-ransomware-attack-via-langflow/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, vulnerability_disclosure, web_shell_backdoor
- affected_industries: financial_services
- cve_ids: CVE-2021-29441, CVE-2025-3248
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, web_shell_backdoor, vulnerability_disclosure
- affected_industries: financial_services
- cve_ids: CVE-2025-3248, CVE-2021-29441
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Attack demonstrates how LLM agents can combine known exploitation techniques with real-time reasoning to automate complex, multi-stage intrusions. The post Agentic AI Used to Conduct Ransomware Attack via Langflow appeared first on SecurityWeek .
```

#### Full body

```
A threat actor exploited a vulnerability in Langflow to access an organization’s instance and abuse it in an agentic ransomware attack, cloud security firm Sysdig reports. Langflow is a Python-based, LLM-agnostic open source framework used for building LLM-driven applications and agent workflows. As part of the attack, a threat actor tracked as JadePuffer gained access to an internet-exposed Langflow instance through the exploitation of CVE-2025-3248 (CVSS score of 9.8), a critical missing authentication vulnerability disclosed in April. Successful exploitation of the bug allows attackers to execute arbitrary Python code on the host on which Langflow is running. CISA flagged the flaw as exploited in early May. After gaining code execution, JadePuffer used the LLM for reconnaissance and swept the system for secrets, including API keys, cloud credentials, cryptocurrency wallets, configuration files, and database credentials. Next, the threat actor dumped Langflow’s Postgres database to harvest the secrets in it, scanned the reachable internal address space and named services, probed for MinIO addresses for further credential extraction, and deployed a cron job for persistent access to the Langflow server. Advertisement. Scroll to continue reading. Throughout this initial phase, the LLM was observed adapting its actions in real time to complete tasks, extract credentials from different file types, and log into discovered endpoints. During the second phase of the attack, JadePuffer used the LLM to pivot to a production server hosting a MySQL database and an Alibaba Naming and Configuration Service (Nacos) configuration platform. Widely used in Alibaba microservice architectures, Nacos has been plagued by various security bypasses and uses a well-known default JWT signing key that allows for easy token forgery. Lateral movement and encryption JadePuffer connected to this server using a payload that contained root credentials for the MySQL port and abused the LLM to target the Nacos service through multiple vectors. “That includes exploiting the auth-bypass family (CVE-2021-29441), forging a valid JWT using Nacos’s well-known default signing key, and, with root database access, injecting a backdoor administrator directly into the Nacos backing database,” Sysdig explains. During the attack, the LLM adjusted the payload to pass login verification, checked for User Defined Functions (UDF), which can lead to OS command execution, and issued a completion marker before ransomware deployment. Next, it encrypted 1,342 Nacos service configuration items and created an extortion table containing the ransom demand, a payment address, and a contact email address. The encryption key was randomly generated but never persisted or transmitted, essentially preventing data recovery. “Captured payloads show the LLM escalating from row-level deletion to dropping entire database schemas, narrating its own targeting rationale,” Sysdig notes. The payloads analyzed by the cybersecurity firm contained natural-language commentary on each action, indicative of LLM-generated code. Furthermore, they showed how the LLM corrected its actions to address failures and provide accurate diagnoses. “During the operation, the LLM parsed free-text context presented by the target and took an action that only makes sense if that text was read and understood, rather than pattern-matched by a scanner. This behavior recurred across sessions weeks apart,” Sysdig notes. According to the company, this attack shows that LLM agents significantly lower the barrier for malicious operations, which now require a capable model rather than a capable human. The AI combined known techniques in a successful attack against neglected infrastructure, with close to zero cost to the attacker. “Defenders should expect the volume and breadth of such campaigns to rise as agentic tooling matures, and they should treat exposed application servers, unhardened configuration stores, and internet-facing
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Agentic AI Used to Conduct Ransomware Attack via Langflow
  - Published: 2026-07-03T11:00:00+00:00
  - Link: https://www.securityweek.com/agentic-ai-used-to-conduct-ransomware-attack-via-langflow/
  - Summary: Attack demonstrates how LLM agents can combine known exploitation techniques with real-time reasoning to automate complex, multi-stage intrusions. The post Agentic AI Used to Conduct Ransomware Attack via Langflow appeared first on SecurityWeek .

### Cluster ce59bc14b1 — score 9

- Title: Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-02T18:30:33+00:00
- Link: https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2025-5777

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, ransomware_extortion, supply_chain
- affected_industries: financial_services, healthcare, manufacturing_industrial
- affected_products: Citrix
- cve_ids: CVE-2025-5777
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, credential_theft, data_breach
- affected_industries: healthcare, financial_services, manufacturing_industrial
- affected_products: Citrix
- cve_ids: CVE-2025-5777
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors associated with the Anubis ransomware operation have been observed exploiting the Citrix Bleed 2 (CVE-2025-5777) vulnerability to obtain initial access. "Although tactics differ between affiliates, common patterns emerged in tradecraft through use of legitimate Remote Management and Monitoring (RMM) tooling, credential access, and hands-on-keyboard procedures used for lateral
```

#### Full body

```
Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials  Ravie Lakshmanan  Jul 02, 2026 Malware / Cyber Attack Threat actors associated with the Anubis ransomware operation have been observed exploiting the Citrix Bleed 2 (CVE-2025-5777) vulnerability to obtain initial access. "Although tactics differ between affiliates, common patterns emerged in tradecraft through use of legitimate Remote Management and Monitoring (RMM) tooling, credential access, and hands-on-keyboard procedures used for lateral movement," Arctic Wolf said in a report published this week. "Anubis affiliates repeatedly abused legitimate remote access and administration tools, including ScreenConnect, Zoho Assist, MeshAgent, Remotely, UltraVNC, and Total Software Deployment, to blend in with normal IT activity while maintaining control of victim systems." Anubis is a ransomware-as-a-service (RaaS) group that first emerged in late 2024 as a rebrand of Sphinx ransomware. The ransomware operation was formally announced on the Ransomware and Advanced Malware Protection (RAMP) underground forum in February 2025. According to data from Ransomware.Live, the cybercrime crew has claimed 91 victims on its data leak site, with 11 victims reported in June 2026 alone. Some of the prominent sectors targeted include healthcare, business services, manufacturing, technology, and financial services. More than 50% of the victims are located in the U.S., followed by the U.K., Australia, France, and Canada. In a report published in July 2025, Rubrik Zero Labs said Anubis advertises attractive profit splits, offering affiliates 80% of the ransom amounts paid, and pairs it with an irreversible data-wiping feature that ups the pressure on victims to pay up. "When Anubis's /WIPEMODE module is activated, files remain in directories but are reduced to a 0 KB size regardless of ransom payment," Rubrik noted at the time. "Knowing threat actors can revert victims' environments to this scorched-earth state with a single command significantly increases pressure on victims to pay before the wiper is fully activated." The ransomware intrusions, observed this year, involve both valid VPN credential use and the exploitation of CVE-2025-5777 (CVSS score: 9.3), a critical flaw impacting Citrix NetScaler ADC and Gateway that could be abused by an attacker to bypass authentication when the appliance is configured as a Gateway or AAA virtual server. The exact source of VPN credentials used in these intrusions is unknown. However, it's possible they were procured following prior compromise, or through initial access brokers (IABs), credential stuffing, or information stealer activity. "In addition to CitrixBleed 2 exploitation, valid Cisco AnyConnect VPN logins were observed from several hosting ASNs, including AS20473 — The Constant Company and AS55286 — ServerMania," Arctic Wolf explained. "Malicious VPN authentication was then followed by login activity involving RDP and SMB, leading to credential access, PsExec service creation, RMM deployment, and ultimately invoking cloud-transfer tooling for exfiltration." Lateral movement is facilitated via RDP and PsExec, which then leads to the deployment of various legitimate RMM tools for persistent access, granting the attackers the ability to transfer files and remotely execute code, while staying under the radar. Select intrusions also configure a Cloudflare Tunnel (aka cloudflared) to establish tunnels to victim environments. The next phase of the attacks involves gathering credentials to facilitate deeper access to the compromised environment, after which tools like S3 Browser, rclone, s5cmd, WinSCP, and PuTTY are installed for data transfer or exfiltration prior to ransomware deployment. In parallel, steps are taken to impair system defenses and complicate post-incident analysis. "These techniques included Windows Defender real-time protection disablement, SophosUninstall activity, PCHunter-related artifacts, and log clearing
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Ransomware Groups Turn to Citrix Bleed 2, BYOVD, and Supply Chain Credentials
  - Published: 2026-07-02T18:30:33+00:00
  - Link: https://thehackernews.com/2026/07/ransomware-groups-turn-to-citrix-bleed.html
  - Summary: Threat actors associated with the Anubis ransomware operation have been observed exploiting the Citrix Bleed 2 (CVE-2025-5777) vulnerability to obtain initial access. "Although tactics differ between affiliates, common patterns emerged in tradecraft through use of legitimate Remote Management and Monitoring (RMM) tooling, credential access, and hands-on-keyboard procedures used for lateral

### Cluster 146c037604 — score 9

- Title: HIPAA Compliance in the Cloud: The Complete Framework Guide
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-02T18:50:00+00:00
- Link: https://orca.security/resources/blog/hipaa-compliance-cloud/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: AWS, Azure, Google Cloud

#### Cluster taxonomy (union across members)
- affected_industries: government, healthcare
- affected_products: AWS, Azure, Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_industries: healthcare
- affected_products: Google Cloud, Azure, AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Key Takeaways HIPAA compliance in the cloud is the practice of protecting electronic protected health information (ePHI) to the standard set by the HIPAA Rules while that data is stored and processed in cloud services like AWS, Azure, and Google Cloud. It combines the Privacy Rule, the Security Rule, and the Breach Notification Rule with […]
```

#### Full body

```
Table of contents Key Takeaways What Is HIPAA Compliance (and What It Means in the Cloud)? Why the cloud changes the HIPAA equation The HIPAA Rules That Govern the Cloud The Privacy Rule (use & disclosure of PHI) The Security Rule — administrative, physical & technical safeguards The Breach Notification Rule The Shared Responsibility Model & Business Associate Agreements (BAAs) Is AWS / Azure / Google Cloud HIPAA compliant? (CSP eligibility + the configuration gap) What Does a HIPAA-Compliant Cloud Look Like? (Required Controls) Encryption of ePHI in transit & at rest Access controls & least privilege to PHI Audit controls & logging Integrity controls & file-integrity monitoring Transmission security Data classification & locating ePHI HIPAA Cloud Compliance Checklist (Step-by-Step) Common HIPAA Cloud Compliance Challenges & Violations How to Choose a HIPAA-Compliant Cloud Service Provider How to Continuously Maintain HIPAA Compliance in the Cloud Maintaining HIPAA Compliance in the Cloud Frequently asked questions about HIPAA Compliance in the Cloud Key Takeaways HIPAA compliance in the cloud means protecting electronic protected health information (ePHI) to the standard of the HIPAA Rules while it lives in AWS, Azure, or Google Cloud. Moving ePHI to a cloud provider does not transfer your liability. It splits it. A cloud provider’s Business Associate Agreement (BAA) covers the platform it runs. Your configuration, access, encryption, and monitoring of ePHI on top of that platform stay your responsibility, which is where almost every cloud HIPAA violation happens. The HIPAA Security Rule technical safeguards in 45 CFR §164.312 (access control, audit controls, integrity, person authentication, and transmission security) map directly to concrete cloud controls you can implement and prove. Compliance is continuous, not a one-time attestation. You need to locate ePHI as it spreads, detect drift and exposure, and keep evidence audit-ready across multi-cloud, not pass a single point-in-time check. Orca uses agentless SideScanning™ to discover ePHI across a cloud estate, map posture to the Security Rule, and surface the exposed attack paths to that data, so the part you own is something you can see and prove. HIPAA compliance in the cloud is the practice of protecting electronic protected health information (ePHI) to the standard set by the HIPAA Rules while that data is stored and processed in cloud services like AWS, Azure, and Google Cloud. It combines the Privacy Rule, the Security Rule, and the Breach Notification Rule with the cloud’s shared-responsibility model. The hook that catches most teams is simple. Moving ePHI to the cloud does not hand your HIPAA liability to the provider. It divides it. The provider secures the platform under a Business Associate Agreement, and everything you build on top of that platform, every bucket, role, key, and log, is yours to secure and prove. This guide is written for security and platform engineers, not lawyers. It covers the Rules that apply, what the BAA does and does not cover, the Security Rule controls mapped to real cloud settings, a step-by-step checklist, and how to prove compliance continuously instead of once a year. Organizations managing HIPAA alongside other regulatory requirements should also understand the fundamentals of multi-cloud compliance . What Is HIPAA Compliance (and What It Means in the Cloud)? HIPAA compliance is meeting the requirements of the Health Insurance Portability and Accountability Act for protecting patient health information. It applies to covered entities (healthcare providers, health plans, and clearinghouses) and to business associates, the vendors that handle protected health information (PHI) on their behalf. In the cloud, that definition gains an operational edge. A cloud provider holding your ePHI is a business associate, so HIPAA follows the data into the provider’s infrastructure. The Department of Health and Human Services (HHS) made this exp
```

#### Corroborating sources (3)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: HIPAA Compliance in the Cloud: The Complete Framework Guide
  - Published: 2026-07-02T18:50:00+00:00
  - Link: https://orca.security/resources/blog/hipaa-compliance-cloud/
  - Summary: Key Takeaways HIPAA compliance in the cloud is the practice of protecting electronic protected health information (ePHI) to the standard set by the HIPAA Rules while that data is stored and processed in cloud services like AWS, Azure, and Google Cloud. It combines the Privacy Rule, the Security Rule, and the Breach Notification Rule with […]
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Google Cloud confirmed to offer a safer choice for EU public sector organizations with Dutch DPIA approval
  - Published: 2026-07-01T16:00:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/google-cloud-confirmed-to-offer-a-safer-choice-for-eu-public-sector-organizations-with-dutch-dpia-approval/
  - Summary: At Google Cloud, we are committed to providing public sector organizations around the globe with cloud technology that is highly flexible, scalable, and built with market-leading standards for data protection, sovereignty, and security. We understand that for public sector organizations in the European Union, confidence in data protection is not just a preference — it’s a prerequisite. Today, we’re excited to announce a major milestone that reinforces this commitment for Google Cloud. Dutch government DPIA confirms strong privacy foundation for Google Cloud We have successfully collaborated with SLM Rijk , the Dutch government's strategic vendor management agency, who completed their rigorous data protection impact assessment (DPIA) of Google Cloud. This engagement confirms Google Cloud’s strong commitment to strengthening trust in its privacy posture across the Dutch public sector. Given that all the key points raised during the DPIA have been successfully addressed (see SLM Rijk’s su
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Azure CLI Password Spray Hits at Least 78 Microsoft Accounts in 81M+ Attempts
  - Published: 2026-07-01T05:46:03+00:00
  - Link: https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
  - Summary: Cybersecurity researchers have warned of a "massive, ongoing, automated password spray attack" aimed at Microsoft's Azure command-line interface (CLI), compromising dozens of accounts in the process. The activity, per Huntress, originates from an IPv6 address range (2a0a:d683::/32) controlled by internet infrastructure provider LSHIY LLC (AS32167). "Between June 12 and June 26, the threat

### Cluster 40ed42a9f6 — score 8

- Title: Train, triage, repeat: The AI agent changing how we fight phishing
- Source: Red Canary (detection_response_operations)
- Published: 2026-06-30T12:33:22+00:00
- Link: https://redcanary.com/blog/threat-detection/phishing-ai-agent/
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
Learn how Red Canary engineered a super agent—blending ML, a rules engine, similarity, agentic AI, and LLMs—to classify phishing emails.
```

#### Full body

```
Skip Navigation Get a Demo
```

#### Corroborating sources (1)

- **Red Canary** (detection_response_operations)
  - Title: Train, triage, repeat: The AI agent changing how we fight phishing
  - Published: 2026-06-30T12:33:22+00:00
  - Link: https://redcanary.com/blog/threat-detection/phishing-ai-agent/
  - Summary: Learn how Red Canary engineered a super agent—blending ML, a rules engine, similarity, agentic AI, and LLMs—to classify phishing emails.

### Cluster e64c15c5cb — score 8

- Title: From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira
- Source: The DFIR Report (detection_response_operations)
- Published: 2026-06-29T13:07:17+00:00
- Link: https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/
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
Key Takeaways This case was first reported to customers in a threat brief released in July 2025 and in a public flash alert in August 2025 in partnership with Swisscom B2B CSIRT, which observed another intrusion tied to the same campaign. This report contains data from both intrusions. We plan to release a DFIR Labs […] The post From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira appeared first on The DFIR Report .
```

#### Full body

```
Access DFIR Labs Book a Demo The DFIR Report provides in-depth, real-world intelligence based on observed intrusions, enabling security analysts and teams to strengthen defenses, enhance detection, and accelerate response. Linkedin X Products Threat Intel DFIR Labs Case Artifacts Threat Feed Detection Pack Active Defense Services Training Professional Services Public Reports Company About us Analysts Careers Contact Us
```

#### Corroborating sources (1)

- **The DFIR Report** (detection_response_operations)
  - Title: From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira
  - Published: 2026-06-29T13:07:17+00:00
  - Link: https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/
  - Summary: Key Takeaways This case was first reported to customers in a threat brief released in July 2025 and in a public flash alert in August 2025 in partnership with Swisscom B2B CSIRT, which observed another intrusion tied to the same campaign. This report contains data from both intrusions. We plan to release a DFIR Labs […] The post From Bing Search to Ransomware: Bumblebee and AdaptixC2 Deliver Akira appeared first on The DFIR Report .

### Cluster f289a7d703 — score 8

- Title: Defending the Authentication Flow: Device Code Phishing with Selena Larson
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-06-30T15:35:04+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/defending-authentication-flow-device-code-phishing-selena-larson
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
Podcasts Data Security Decoded Ep 57 Ep 57 | 6.30.26 Defending the Authentication Flow: Device Code Phishing with Selena Larson Subscribe Apple Podcasts Spotify YouTube Amazon Music Pocket Casts Castbox RSS Show Notes Transcript This episode delivers critical battlefield stories regarding the operational reality of modern identity based threats. ⁠Selena Larson⁠ , Staff Threat Researcher and Lead, Intelligence Analysis and Strategy at ⁠Proofpoint⁠ and Host of the ⁠DISCARDED⁠ podcast and the ⁠Only Malware in the Building⁠ podcast, joins host ⁠⁠Caleb Tolin⁠ ⁠ to detail the specific mechanics of device code phishing campaigns, revealing how adversaries exploit legitimate communication structures to capture administrative and enterprise access. The discussion centers on the rapid commercialization of cybercrime, highlighting the leak of specialized kits in late 2025 that catalyzed the democratization of sophisticated technical exploits. The conversation unpacks the behavioral patterns of specific threat groups, analyzing the intersection of business email compromise, credential harvesting, and account takeover jumping. Selena explains how opportunistic targeting allows threats to pivot horizontally through trusted external supplier networks and specific industry verticals. Rather than focusing solely on defensive theory, the dialogue transitions into hard technical controls, challenging the long-term viability of traditional security awareness programs. Defenders are provided with direct architectural recommendations, including the precise deployment of conditional access policies and rigid device compliance frameworks designed to stop unauthorized authentication attempts before execution. What You'll Learn Core operational mechanics behind the exploitation of Microsoft OAuth authentication workflows. Historical transition from early red team utility testing to commercialized phishing platforms. Impact of leaked cyber criminal source code on the current volume of identity attacks. Analytical methods to distinguish between intentional industry targeting and opportunistic account jumping. Strategic deployment of conditional access policies to terminate unauthorized authentication capabilities. Technical constraints of legacy security awareness training against modern behavioral engineering. Structural integration of strict device compliance validation within identity perimeters. Data Security Decoded Podcast Info HOST(S): As the host of Data Security Decoded, Caleb Tolin dives deep with cyber experts to deliver actionable, vendor-agnostic insights to reduce data security risks and improve cyber resilience outcomes. Caleb asks the incisive questions that you need answered, extracting actionable guidance for defenders. Come be obsessed with improving your organization's cyber resilience. Follow Caleb Tolin Schedule: Two times per month. Every other Tuesday. Credits: Data Security Decoded is a podcast by Rubrik. Creator: Rubrik Social Media: Rubrik Inc. Rubik Inc. @rubrikInc
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Defending the Authentication Flow: Device Code Phishing with Selena Larson
  - Published: 2026-06-30T15:35:04+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/defending-authentication-flow-device-code-phishing-selena-larson

### Cluster 5e0e552a1f — score 8

- Title: Inside Elastic InfoSec's agentic SOC: cutting alert triage from 30 minutes to under 3
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-02T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/alert-triage-agentic-soc-elastic-workflows
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ai_security
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Elastic's InfoSec team built AI agents on Elastic Workflows that investigate every alert and assemble the case before an analyst ever opens it.
```

#### Full body

```
2 July 2026 • Aaron Jewitt Inside Elastic InfoSec's agentic SOC: cutting alert triage from 30 minutes to under 3 Elastic's InfoSec team built AI agents on Elastic Workflows that investigate every alert and assemble the case before an analyst ever opens it. 14 min read Generative AI , Detection Engineering Elastic's InfoSec team built an agentic SOC that triages every alert before an analyst opens it. A 30-minute manual investigation now finishes in under 3 minutes: deterministic ES|QL queries close obvious false positives at zero token cost, specialized AI agents investigate the rest across endpoint, cloud, and SaaS domains, and a Final Review agent writes the verdict to a Kibana case. The whole pipeline runs on Elastic's native stack ( Workflows , Agent Builder , the Elastic Inference Service , and Kibana Cases ) with no third-party orchestrator, and inference routed only to providers documented with zero data retention. AI-assisted attacks have compressed the timeline from initial access to exfiltration from days to hours, and traditional manual alert triage cannot keep pace. Hiring more analysts does not scale with alert volume. The Agentic SOC pattern fixes this gap: automate the investigation work that does not require human judgment so analysts can focus on the alerts that do. Note that we use a workflow as our Agentic SOC orchestration layer instead of an Agent. We chose to use a workflow for orchestration instead of an Agent because of the scale we are operating at. A workflow is deterministic, fast, and does not consume tokens. When you are triaging tens of thousands of alerts per month, this can make a huge difference in costs and performance. For a security team processing sensitive alert data, the inference layer's data handling matters. The Elastic Inference Service routes requests to trusted third-party model providers that operate with zero data retention and do not use inputs to train models. Per-model data retention and training-data status are documented on the EIS supported-models page so customers can verify the status of the specific model their pipeline uses. For airgapped or highly sensitive environments, the same pipeline can run against a model hosted on your own infrastructure. At Elastic, our InfoSec team operates as "Customer Zero." We run the newest versions of Elastic Security in our production environment, often before they are released publicly. Our fleet spans thousands of laptops, servers, and cloud workloads across a globally distributed workforce. We are the first and most demanding user of every feature we ship, including the Workflows and Agent Builder platforms. Our Agentic SOC journey started with a single Agent Builder triage agent in Elastic Security 9.2. It handled workstation alerts well, where the investigation pattern is consistent, but we found that SaaS provider logs and Higher-Order threshold alerts required a more specialized methodology. That gap drove our move to domain-specific agents. Alert triage with Workflows and ES|QL: closing alerts without AI The principle behind this first step is simple: any check that can be resolved by a query should be a query, not an LLM call. ES|QL queries are deterministic, auditable, fast, and cost nothing in tokens. An LLM call is non-deterministic, slower, more expensive, and introduces failure modes (hallucinated facts, prompt injection, inconsistent reasoning across runs) that a query does not have. Most false-positive patterns in a mature SOC are well understood and can be expressed in code, so spending tokens to reason about them is a wasted cost. The LLM is the right tool for the alerts where the data is genuinely ambiguous, not for the ones a query can close cleanly. This builds on the approach we described in our earlier automated SIEM investigation post using Tines, where many of these same triage checks ran as Tines stories. Bringing them into Elastic Workflows keeps the full pipeline inside Kibana. Detection rules in Kibana suppor
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Inside Elastic InfoSec's agentic SOC: cutting alert triage from 30 minutes to under 3
  - Published: 2026-07-02T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/alert-triage-agentic-soc-elastic-workflows
  - Summary: Elastic's InfoSec team built AI agents on Elastic Workflows that investigate every alert and assemble the case before an analyst ever opens it.

### Cluster 4f72cf52f3 — score 8

- Title: Defence Impairment Olympics
- Source: Huntress (detection_response_operations)
- Published: 2026-06-29T07:00:00+00:00
- Link: https://www.huntress.com/blog/mimikatz-credential-dumping-defence-impairment
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- cve_ids: CVE-2023-26360, CVE-2023-29298, CVE-2023-29300
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- cve_ids: CVE-2023-26360, CVE-2023-29298, CVE-2023-29300
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Huntress analyzed a credential dumping attack where threat actors disabled Defender, killed monitoring tools, and used Mimikatz to steal credentials.
```

#### Full body

```
Home Blog Defence Impairment Olympics Published: June 29, 2026 Defence Impairment Olympics By: Mark O'Halloran Lindsey O'Donnell-Welch Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways We recently detected an incident on June 7 that started with simple enumeration commands - but our investigation into the attack showed the threat actor taking aggressive steps to hide their tracks. The investigation into the attack initially showed a few defence impairment techniques, like steganography and timestomping. However, our investigation broadened when we found a breadcrumb left behind - and batch script called i.bat - that showed the threat actor attempting to disable Defender, kill Sysmon and Filebeat, uninstall the ModSecurity WAF, downgrade WDigest credential protection— all before Mimikatz was executed to dump credentials. Following the SOC's initial response and delivery of remediation steps, a window of exposure occurred when the server was brought back online prior to complete patching. The threat actor leveraged this premature reconnection to continue their attack. This scenario highlights a common challenge in incident response: thorough closure and verified remediation are just as critical as the initial detection. Organizations can defend against these techniques with foundational security measures, including implementing sufficient and correctly configured logging on their servers and endpoints, and ensuring software is updated and patched. Acknowledgements: Special thanks to Adrian Garcia, Amelia Casley, Olly Maxwell and Anton Ovrutsky for their contributions to this investigation and write-up. Background At Huntress, we have visibility into various parts of a threat actor's attack chain: including how they enter the victim's environment (initial access), how they research the environment (enumeration), and how they move around the environment (lateral movement). One tactic that we see a fair amount of is defence evasion and defence impairment; or specific measures threat actors take to hide their tracks during an incident and to disable defence mechanisms. We recently responded to an incident on June 7 where a threat actor initially performed enumeration activity before later carrying out almost a dozen different types of defence impairment commands, including disabling the IIS logs, tampering with Microsoft Defender, using WMI Event Consumer to clear the Windows Event Logs, using timestomping, and more. We have outlined the defence impairment tactics we saw in this incident; by better understanding these techniques and how they play out in a targeted environment, organizations can get a stronger sense of where they should prioritize their defenses and look for signs of potential compromise. A steganographic webshell: The first commands On June 7, Huntress responded to a web server compromise spawning from a webshell that was uploaded to a vulnerable server by a threat actor. Due to insufficient logging, Huntress was unable to determine the exact initial access mechanism. There was, however, some evidence that the particular server had potentially suffered an Adobe ColdFusion exploitation attempt. Upon closer inspection of the historical logs, we found evidence of possible exploitation of ColdFusion bugs, including a critical remote code execution vulnerability ( CVE-2023-26360 ), improper access control bug ( CVE-2023-29298 ), and deserialization flaw ( CVE-2023-29300 ). The evidence that we did have stemmed from the presence of known targeted endpoints in historical logs: /CFIDE/adminapi/_datasource/setmsaccessRegistry.cfm /CFIDE/adminapi/_datasource/setsldatasource.cfm /CFIDE/adminapi/_datasource/setdsn.cfm /CFIDE/adminapi/_datasource/formatjdbcurl.cfm /CFIDE/adminapi/_datasource/getaccessdefaultsfromRegistry.cfm /CFIDE/adminapi/_datasource/geturldefaults.cfm /CFIDE/adminapi/customtags/l10n.cfm /CFIDE/adminapi/serverinstance.cfc /CFIDE/adminapi/servermonitoring.cfc While normally, the acce
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Defence Impairment Olympics
  - Published: 2026-06-29T07:00:00+00:00
  - Link: https://www.huntress.com/blog/mimikatz-credential-dumping-defence-impairment
  - Summary: Huntress analyzed a credential dumping attack where threat actors disabled Defender, killed monitoring tools, and used Mimikatz to steal credentials.

### Cluster 6c76262a4a — score 8

- Title: New CitrixBleed Vulnerability Exploited Immediately After Public Disclosure
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-02T15:04:22+00:00
- Link: https://www.securityweek.com/new-citrixbleed-vulnerability-exploited-immediately-after-public-disclosure/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ransomware_extortion
- actor_attribution: Scattered Spider
- affected_products: Apple iOS/macOS, Microsoft SharePoint
- cve_ids: CVE-2026-8451
- urgency_signals: actively_exploited, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, active_exploitation
- actor_attribution: Scattered Spider
- affected_products: Microsoft SharePoint, Apple iOS/macOS
- cve_ids: CVE-2026-8451
- urgency_signals: actively_exploited, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Hackers are targeting NetScaler appliances using public PoC code to retrieve arbitrary memory content in the HTTP response. The post New CitrixBleed Vulnerability Exploited Immediately After Public Disclosure appeared first on SecurityWeek .
```

#### Full body

```
Threat actors began exploiting the latest CitrixBleed-like vulnerability in NetScaler ADC and NetScaler Gateways less than 24 hours after public disclosure, Scottish cybersecurity firm Lupovis reports. Tracked as CVE-2026-8451 (CVSS score of 8.8), the security defect was disclosed on June 30, when Citrix rolled out patches , and attack surface management company watchTowr published technical details on it. The bug is described as an out-of-bounds read issue affecting NetScaler appliances configured as SAML IDP and leading to memory disclosure. It was discovered in NetScaler’s XML parser, which did not terminate unquoted XML attribute values if they were followed by a newline character. Because of the flaw, the parser would read past the intended buffer, and NetScaler would return memory contents in the NSC_TASS cookie in an HTTP response. While it requires that the targeted NetScaler appliances be configured as SAML IDP, the successful exploitation of the vulnerability does not require authentication. Shortly after watchTowr shared details on the security hole and published a detection artefact generator, at least one threat actor started probing exposed NetScaler instances, Lupovis told SecurityWeek . Advertisement. Scroll to continue reading. Initial scanning activity originated from an IP hosted on infrastructure in Frankfurt, Germany, likely using a disposable or purpose-built scanning node. Multiple Lupovis sensors were targeted within a five-hour window, and a payload was immediately dropped on the sensor that responded with a 200 response. The payload included a “bare <samlp:AuthnRequest> tag padded with 476 spaces followed by a newline”, which matches the overread variant in watchTowr’s detection artefact generator. On Thursday, the cybersecurity firm observed a second threat actor probing for exposed NetScaler instances from a Koapu Cloud HK IP address. “Both have demonstrated the same behaviour, probing for the right endpoint, upon receiving a 200 OK with the right response, they have delivered the payload immediately,” Lupovis CEO Xavier Bellekens said. Organizations are advised to patch their NetScaler appliances immediately, or to disable SAML IDP if patching is not possible. They should also check logs for /saml/login traffic, inspect the request values, and check NSC_TASS cookie values to identify exploitation. Related: Cisco Confirms In-the-Wild Exploitation of Unified CM Vulnerability Related: CISA Warns of Actively Exploited Microsoft SharePoint Vulnerability Related: Adobe Patches Critical ColdFusion, Campaign Classic Vulnerabilities Related: Exploitation of Recent Oracle E-Business Suite Vulnerability Begins Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Cisco Confirms In-the-Wild Exploitation of Unified CM Vulnerability ‘BioShocking’ Attack Tricks AI Browsers Into Stealing Credentials CISA Warns of Actively Exploited Microsoft SharePoint Vulnerability Microsoft Adds New Teams Controls to Block Unauthorized AI Bots From Meetings Adobe Patches Critical ColdFusion, Campaign Classic Vulnerabilities Citrix Patches NetScaler Vulnerabilities, Including New ‘HTTP/2 Bomb’ Attack Apple Patches Dozens of Vulnerabilities Across iOS, macOS, and Safari Dawnguard Raises $6.3 Million for Security Architecture Automation Platform Latest News In Other News: Canadian Hacker Jailed, Open Source Zero-Days, Two Sentenced for ATM Jackpotting Agentic AI Used to Conduct Ransomware Attack via Langflow Medtronic Data Breach Impacts 3.8 Million People Alleged Scattered Spider Hacker Extradited to US Google, FBI Disrupt NetNut Residential Proxy Network Powered by Millions of Devices Critical Cursor AI Code Editor Flaws Could Lead to OS-Level Remote Code Execution How to Conduct a Successful Audit of AI-Driven Software Development Fo
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: New CitrixBleed Vulnerability Exploited Immediately After Public Disclosure
  - Published: 2026-07-02T15:04:22+00:00
  - Link: https://www.securityweek.com/new-citrixbleed-vulnerability-exploited-immediately-after-public-disclosure/
  - Summary: Hackers are targeting NetScaler appliances using public PoC code to retrieve arbitrary memory content in the HTTP response. The post New CitrixBleed Vulnerability Exploited Immediately After Public Disclosure appeared first on SecurityWeek .

### Cluster 179d9b0465 — score 8

- Title: Finding and Addressing Vulnerable and Outdated Web Application Components
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-07-01T14:00:00+00:00
- Link: https://www.blackhillsinfosec.com/vulnerable-and-outdated-web-application-components/
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
Vulnerable and outdated software components are one of the most common issues encountered by BHIS during web application penetration tests. The vast majority of web applications use third-party components such as jQuery, Angular, Bootstrap, or countless other libraries. The post Finding and Addressing Vulnerable and Outdated Web Application Components appeared first on Black Hills Information Security, Inc. .
```

#### Full body

```
1 Jul 2026 Finding , Informational , Melissa Bruno , Web App Top 100 Findings Finding and Addressing Vulnerable and Outdated Web Application Components | Melissa Bruno Vulnerable and outdated software components are one of the most common issues encountered by BHIS during web application penetration tests. The vast majority of web applications use third-party components such as jQuery, Angular, Bootstrap, or countless other libraries. Vulnerabilities can be present in any of these components and introduce risk into your environment. Keeping these components up to date is essential for maintaining the security of a web application. Vulnerabilities affecting components can range from minor information disclosure to critical remote code execution, which can put the entire organization at risk. Identifying Components — From A Tester’s Perspective It is important for testers to manually review each component utilized by a web application. Tools such as Nessus and Burp Suite’s passive scanner will flag some of the most serious vulnerabilities affecting third-party components, but the vast majority of vulnerabilities do not have associated findings in these tools, and testers relying on these tools to identify vulnerable components will fail to detect most of these issues. The most straightforward way for testers to find components and their associated version numbers is to manually inspect the files returned by the application. The Site Map in Burp Suite and the developer tools in browsers (Firefox’s Debugger and Chrome’s Sources panel), all create an easily browsable list of files used by a web application. Site Map in Mozilla’s Developer Tools Shows jQuery Component In some cases, a component’s name and version number may be readily apparent in the URL or at the top of a file. However, often times, component names and version numbers are buried deep within a file’s source code, and it can be difficult and time-consuming for humans to manually identify these. For the quick identification of third-party components and their version numbers, testers may consider using the Wappalyzer browser plugin. This plugin detects components utilized by the web application and, when possible, the components’ version numbers, and outputs them in a concise list, such as the one shown below. Example Wappalyzer Output Web applications that return verbose error messages that disclose information about the application for debugging purposes may also return component version numbers. Any components mentioned in verbose error messages should be manually investigated. Identifying Vulnerabilities Once you have discovered a component and its associated version number, it’s time to check if that component has any known vulnerabilities. The Snyk Vulnerability Database is a great resource for finding vulnerabilities associated with web components. Example Snyk Vulnerability Summary for jQuery Component Snyk also offers a quick glance at useful information such as the software’s latest version, and how long ago the latest version of the software was published. This information puts into perspective how behind an organization is on patching. If the application is using version 2.1.6, but the latest version is 2.1.7, and it was only released five days ago, there is a good chance that this organization is on top of patching. Conversely, if the organization is 11 versions behind the latest release, patching components may be something that they really need to improve upon. The date that the latest version was published can also provide an important perspective on the state of the software. If the latest version of the software is affected by known vulnerabilities, but the last version update was eight years ago, the component is likely no longer actively maintained, and developers should be advised to disable it. Snyk – Additional Details About jQuery Component If Snyk does not have useful information about a component, plugging the component name and version into
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: Finding and Addressing Vulnerable and Outdated Web Application Components
  - Published: 2026-07-01T14:00:00+00:00
  - Link: https://www.blackhillsinfosec.com/vulnerable-and-outdated-web-application-components/
  - Summary: Vulnerable and outdated software components are one of the most common issues encountered by BHIS during web application penetration tests. The vast majority of web applications use third-party components such as jQuery, Angular, Bootstrap, or countless other libraries. The post Finding and Addressing Vulnerable and Outdated Web Application Components appeared first on Black Hills Information Security, Inc. .

### Cluster ae77ed43fa — score 8

- Title: Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-30T17:46:07+00:00
- Link: https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: financial_services
- affected_products: Azure, Microsoft/Copilot
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: financial_services
- affected_products: Azure, Microsoft/Copilot
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
New Microsoft research shows how attackers can hijack AI agents that act on a user's behalf, using nothing more than a poisoned tool description to make the agent quietly hand over company data to an outsider. The trick is that the agent never breaks a rule. Every step looks routine, so in a default setup no alarm may fire. The work comes from Microsoft Incident Response and its
```

#### Full body

```
Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data  Swati Khandelwal  Jun 30, 2026 Artificial Intelligence / Supply Chain Security New Microsoft research shows how attackers can hijack AI agents that act on a user's behalf, using nothing more than a poisoned tool description to make the agent quietly hand over company data to an outsider. The trick is that the agent never breaks a rule. Every step looks routine, so in a default setup no alarm may fire. The work comes from Microsoft Incident Response and its Defender security research team, and it lands as companies start letting AI do more than read and summarize. What changes when an agent can act Until recently, the workplace AI risk was mostly framed around what a model read and wrote. A poisoned document could skew an answer, and that was mostly where it ended. Agents are different. Microsoft 365 Copilot can send email, create files, and change calendars. Custom agents built in Copilot Studio or Azure AI Foundry can reach into business systems and run multi-step jobs on their own. The same injection trick that biases a summary now triggers an action. Against a reader, an attack changes the output. Against an agent, it changes what the software actually does. These agents reach business systems through MCP, the Model Context Protocol , an open protocol that lets an AI call outside tools the way an app calls an API. Microsoft calls it the fastest-growing part of the agentic AI supply chain, which makes it an expanding attack surface. How the attack works Every MCP tool ships with a description: a few lines of plain text that tell the agent what the tool does and when to use it. The agent reads that text to decide how to act. That is the whole weakness. The description is just words, and words can carry instructions. Microsoft walks through it with an invoice example, built to show the pattern rather than report a named victim. A finance team stands up an agent to handle vendor invoices. It connects to three tools, including a third-party "invoice enrichment" service that was approved for use but never given a real security review. Then the attacker updates that third-party tool. The name and the visible summary stay the same. Buried in the description, dressed up as formatting notes, is a hidden order: grab the last thirty unpaid invoices and attach them to the next call. MCP picks up description changes on the fly. In setups without a re-approval trigger, the poisoned version goes live with no extra review. After that, an analyst asks a routine question about a supplier. The agent follows the hidden order, collects the invoices and sends them along as part of a normal-looking request. The tool returns a clean answer and quietly copies the stolen data to a server the attacker controls. The analyst sees nothing wrong. Each move the agent makes is legitimate on its own. The tool was approved. The data query ran with the analyst's own permissions. The outbound call went to a server that was allowed when it was added. The weakness is not in any one system. It lives in what Microsoft calls "the trust boundary between them." The deeper problem is that MCP mixes instructions and data in the same place. A tool's description lives in the agent's working memory right next to its real orders, so editing that description can steer the agent as effectively as rewriting its system prompt. The agent has no reliable way to tell an honest instruction from a malicious one slipped in by whoever maintains the tool. Microsoft notes this is not a bug in Copilot itself. It is a trust gap opened up by plugging in outside tools. What defenders should do Microsoft's advice, stripped to plain terms: Treat every connected tool as part of your supply chain. Keep a list of approved tool publishers, turn off "allow all," and let an agent use only the specific tools it needs. Treat a tool's description like a system prompt. Review changes to it the way you would review a code cha
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data
  - Published: 2026-06-30T17:46:07+00:00
  - Link: https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html
  - Summary: New Microsoft research shows how attackers can hijack AI agents that act on a user's behalf, using nothing more than a poisoned tool description to make the agent quietly hand over company data to an outsider. The trick is that the agent never breaks a rule. Every step looks routine, so in a default setup no alarm may fire. The work comes from Microsoft Incident Response and its

### Cluster a56bf79002 — score 8

- Title: Researcher Behind 'Exploitarium' Explains Release of Undisclosed Zero-Day Exploits
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-02T12:51:00+00:00
- Link: https://www.infosecurity-magazine.com/news/researcher-exploitarium-exploits/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure, zero_day
- affected_industries: government
- affected_products: GitHub, Gogs, Linux kernel
- cve_ids: CVE-2026-55200, CVE-2026-58049, CVE-2026-58050
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure
- affected_industries: government
- affected_products: GitHub, Linux kernel, Gogs
- cve_ids: CVE-2026-55200, CVE-2026-58049, CVE-2026-58050
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Infosecurity spoke with the researcher who dumped over 30 proof-of-concept exploits without disclosing the vulnerabilities first
```

#### Full body

```
Infosecurity Magazine Home » News » Researcher Behind 'Exploitarium' Explains Release of Undisclosed Zero-Day Exploits Researcher Behind 'Exploitarium' Explains Release of Undisclosed Zero-Day Exploits News 2 July 2026 Written by Kevin Poireault Reporter , Infosecurity Magazine Follow @Kpoireault Connect on LinkedIn A pseudonymous security researcher has released over 30 proof-of-concept exploits for zero-day vulnerabilities in open-source projects without disclosing them to the maintainers first. The dump, called ‘ Exploitarium ,’ was shared publicly on GitHub by an individual going by name ‘bikini’ and ‘ashdfrkl’ on Discord. First published on June 27, the repository initially included around 15 exploits, before the researcher updated it over the next few days with new entries. It affects several open-source projects, including the Linux kernel, Libssh2, FFmpeg, Gogs, Gitea, Ghidra, 7-Zip, MyBB, PHP, OpenVPN, the VLC player and more. The 'Exploitarium' repository on GitHub. Source: Infosecurity Magazine In the ‘Exploitarium’ repository on GitHub, the researcher claimed they automated the entire fuzzing process using AI, specifically OpenAI models and tools. One of the most widely used methods to find vulnerabilities, fuzzing is an automated software testing technique that inputs random, invalid or unexpected data into a computer program to detect crashes, memory leaks and security flaws. However, the main reason this exploit dump sparked debate within the cybersecurity community is the apparent lack of coordinated vulnerability disclosure (CVD). CVD is the industry-standard practice of privately alerting developers to a security flaw first, giving them a window of time to patch the issue before details are made public. On GitHub, the researcher explicitly invited others to file CVEs themselves and framed the work as an effort to bring people into the field. Speaking to Infosecurity on Discord, the researcher confirmed they did not inform any of the maintainers of the publication. While they have been through a CVD process in the past, they decided against it this time. “I think it's the best way for people to learn and become allured into the field. It's a lot less interesting and informative if someone has to read a write up that's not applicable by today's security standards,” the researcher known as bikini said. “It also raises the barrier to entry making someone go back and install outdated software to test on.” Some Exploits Linked to Disclosed CVEs Some vulnerabilities have since been publicly disclosed and some of them have been patched by maintainers. One of them, CVE-2026-55200 , represents a severe pre-authentication remote code execution (RCE) vulnerability affecting libssh2, a widely used client-side C library implementing the SSH2 protocol, with a CVSS severity score of 9.2. Exploitation involves transmitting specially crafted SSH packets containing oversized packet_length values to manipulate heap memory, ultimately enabling remote code execution. While bikini dropped the exploit on GitHub, the vulnerability was publicly disclosed by VulnCheck through formal channels with credit to a different cybersecurity researcher Tristan Madani (also known as @TristanInSec) for reporting it to them. It has now been addressed with a fix already integrated into the libssh2 mainline development branch, though maintainers are still finalizing a formal release that includes the patch. Speaking to Infosecurity , Ethan Andrews, a cybersecurity analyst and detection engineer at Federal Signal Corporation, said CVE-2026-55200 has been “independently verified.” He noted that it is the “most severe” vulnerability that has come out of the dump and is experiencing active exploitation. Aside from CVE-2026-55200, bikini’s ‘Exploitarium’ GitHub repository mentioned that 12 issues have now received CVE identifiers: CVE-2026-58049: Memory corruption (heap write/read) in FFmpeg's RASC video decoder CVE-2026-58050: Heap buffer overflow in lib
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Researcher Behind 'Exploitarium' Explains Release of Undisclosed Zero-Day Exploits
  - Published: 2026-07-02T12:51:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/researcher-exploitarium-exploits/
  - Summary: Infosecurity spoke with the researcher who dumped over 30 proof-of-concept exploits without disclosing the vulnerabilities first

### Cluster 31e5b2aa9f — score 8

- Title: Insurance Giant Aflac Discloses Data Breach Impacting Millions
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-01T09:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/insurance-giant-aflac-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: Scattered Spider
- affected_industries: financial_services, healthcare
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, data_breach
- actor_attribution: Scattered Spider
- affected_industries: healthcare, financial_services
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Aflac Japan has notified regulators that policy details and personal and banking information have been compromised
```

#### Full body

```
Infosecurity Magazine Home » News » Insurance Giant Aflac Discloses Data Breach Impacting Millions Insurance Giant Aflac Discloses Data Breach Impacting Millions News 1 July 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster US insurer Aflac has disclosed a major data breach after hackers managed to access highly sensitive personal and financial information. The company’s Aflac Japan subsidiary discovered the intrusion on June 25, it said in a filing with the SEC yesterday (June 30). It explained that an “unauthorized third party” had accessed certain systems between June 15 and June 25. “Although the investigation remains ongoing, Aflac Japan has determined that certain impacted files contain policy and coverage details, personal information, and bank account information,” it revealed. “This incident is limited to systems in Japan, the company’s systems related to its US business were not accessed by the unauthorized third-party. At this time, the full scope and potential ultimate impact on the company are not known.” Read more on insurance sector breaches: Third-Party Breach Impacts Majority of Allianz Life US Customers. A statement posted on Aflac Japan’s website revealed that the incident impacted the firm’s customer portal. “Please note that some systems are currently shut down to prevent the spread of unauthorized access,” it said (via Google Translate). “However, inquiries and procedures, including claims for insurance benefits and other payments, are being handled as usual through our call center and other channels.” Among the services currently out of action are reservations for medical check-ups and health screening, and the firm’s AI support concierge. According to local reports , personal and financial information on nearly 4.4 million customers has been compromised. This includes information about the premium payment accounts of around 230,000 customers. Another Scattered Spider Attack? This isn’t the first time Aflac Japan has suffered at the hands of threat actors. In 2023, Aflac Japan customers’ details were stolen and put up for sale after a third-party US contractor was reportedly breached. A year ago, the firm suffered another data breach which was claimed to be part of a wider campaign targeting US insurers thought to be the work of the Scattered Spider group. Joshua Roback, principal security solution architect at Swimlane, said the latest compromise could also be linked to the notorious extortion group. “Large insurers are sprawling ecosystems of subsidiaries, support teams, legacy platforms and regional workflows. That gives threat actors more places to test access, reuse lessons from prior campaigns and search for the fastest path back to valuable data,” he said. “The answer is not just more alerts. Security teams need connected workflows that can turn a signal in one part of the business into action everywhere else. Agentic AI and automation can help prioritize the riskiest activity, trigger containment steps and keep remediation moving before attackers get comfortable.” Aflac Japan has notified the relevant authorities and claimed that “no misuse of the information related to this incident has been confirmed.” Image credit: yu_photo / Shutterstock.com You may also like Millions of Insurance Customers Compromised Via Supplier News 13 January 2023 Phishing Alert as Erie Insurance Reveals Cyber “Event” News 12 June 2025 Over 80% of UK Firms Don’t Have Specialist Cyber Insurance News 5 February 2020 Global Firms Under-Insured Despite Breach Concerns News 5 November 2019 Why Cyber Insurance Works Opinion 4 April 2018 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Researcher Behind 'Exploitarium' Explains Release of Undisclosed Zero-Day Exploits News 2 July 2026 1 Cybercriminals Pose as Interpol in Phishing Emails to Infect Victims With Ransomware News 2 July 2026 2 NCSC Shares Tips on How to Make a Pen Tester’s Job Harde
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Insurance Giant Aflac Discloses Data Breach Impacting Millions
  - Published: 2026-07-01T09:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/insurance-giant-aflac-data-breach/
  - Summary: Aflac Japan has notified regulators that policy details and personal and banking information have been compromised

### Cluster 083a4a03d5 — score 8

- Title: Critical SimpleHelp Vulnerability Exploited For Malware Delivery
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-06-30T15:34:00+00:00
- Link: https://www.infosecurity-magazine.com/news/simplehelp-rmm-vulnerability/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion, supply_chain, web_shell_backdoor, zero_day
- actor_attribution: MuddyWater
- affected_industries: critical_infrastructure, financial_services, government
- affected_products: Apple iOS/macOS, Fortinet, Ivanti
- cve_ids: CVE-2026-48558
- urgency_signals: preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, credential_theft, zero_day, web_shell_backdoor
- actor_attribution: MuddyWater
- affected_industries: financial_services, government, critical_infrastructure
- affected_products: Ivanti, Fortinet, Apple iOS/macOS
- cve_ids: CVE-2026-48558
- urgency_signals: zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Attackers exploited a critical SimpleHelp RMM bug to deploy TaskWeaver and Djinn Stealer malware
```

#### Full body

```
Infosecurity Magazine Home » News » Critical SimpleHelp Vulnerability Exploited For Malware Delivery Critical SimpleHelp Vulnerability Exploited For Malware Delivery News 30 June 2026 Written by Alessandro Mascellino News Reporter Email Alessandro Follow @a_mascellino A critical authentication bypass in SimpleHelp's remote monitoring and management (RMM) software has been exploited to deliver two previously unseen malware families, after attackers forged a login token to seize control of a managed network. New analysis from security firm Blackpoint Cyber found that an attacker exploited the flaw, tracked as CVE-2026-48558, to obtain a trusted technician session on an internet-facing SimpleHelp server. The attacker then used the platform's own tools to push malware its researchers named TaskWeaver and Djinn Stealer. From Forged Token to Full Control The flaw carries a maximum CVSS severity score of 10. In affected configurations, SimpleHelp failed to check the cryptographic signature of identity tokens in its OpenID Connect login, letting an unauthenticated attacker forge a token and sign in as a technician. Instead of a phishing email or a standalone exploit, the attacker abused SimpleHelp's own file-transfer and remote-execution features to mass-deploy an obfuscated file disguised as the jQuery library, jquery.js, fetched from a temporary Cloudflare address and executed via Node.js. The firm said the trusted support channel let the activity blend in. Read more on RMM attacks against MSPs: DragonForce Ransomware Leveraged in MSP Attack Using RMM Tool A Loader and a Credential Sweep Despite its name, jquery.js is a modular Node.js loader that its researchers track as TaskWeaver, built to evade static analysis. Its only command, "deliver", run whatever code the operator sent with full Node.js access so that it could drop a stealer one moment and a backdoor or ransomware the next. The recovered payload, Djinn Stealer, was a cross-platform infostealer for Windows, macOS and Linux. Blackpoint said it swept a machine for cloud and infrastructure keys, source code and SSH credentials, cryptocurrency wallets and package-registry tokens that could seed a supply chain attack. The rules went further than most stealers, reaching for the tokens behind AI coding assistants. Developers often grant those assistants standing access to code, databases and cloud accounts, so the stolen tokens hand an attacker that same reach, well beyond the AI itself. Risk Beyond the Endpoint Blackpoint warned that the damage outlasts the breached server: a single bypass became a path into cloud platforms, code repositories, AI tools and customer environments, with stolen credentials keeping that access alive after the endpoint is isolated. For managed service providers (MSPs), a single exposed server can affect every downstream customer. SimpleHelp patched the flaw in late May, in versions 5.5.16 and 6.0 RC2. On June 29, after Blackpoint published its findings, CISA added it to its Known Exploited Vulnerabilities (KEV) catalog. Blackpoint urged MSPs to patch, pull SimpleHelp off the internet and rotate any exposed secrets, treating credentials as compromised even after an endpoint is cleaned. The findings come from a single contained intrusion, with both malware families undocumented beforehand. You may also like Fake SSA Emails Drive Venomous#Helper Phishing Campaign News 5 May 2026 Ransomware Gang Exploits SimpleHelp RMM to Compromise Utility Billing Firm News 13 June 2025 MuddyWater Uses SimpleHelp to Target Critical Infrastructure Firms News 18 April 2023 UK Government Cybersecurity Advisory Board Applications Now Open News 25 May 2022 LATAM Infrastructure Hit by Fortinet and Ivanti Exploits News 18 June 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Researcher Behind 'Exploitarium' Explains Release of Undisclosed Zero-Day Exploits News 2 July 2026 1 Cybercriminals Pose as Interpol in Phishing Emails to Infect Victims With Ra
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Critical SimpleHelp Vulnerability Exploited For Malware Delivery
  - Published: 2026-06-30T15:34:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/simplehelp-rmm-vulnerability/
  - Summary: Attackers exploited a critical SimpleHelp RMM bug to deploy TaskWeaver and Djinn Stealer malware

### Cluster af46e29c96 — score 8

- Title: Russian Hackers Accused of Destructive Cyber-Attack on Jaguar Land Rover
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-06-29T09:15:00+00:00
- Link: https://www.infosecurity-magazine.com/news/russian-hackers-destructive-jaguar/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: Scattered Spider
- affected_industries: critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: Scattered Spider
- affected_industries: critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Experts warn the Jaguar Land Rover breach bears hallmarks of Kremlin-backed hackers, citing novel ransomware, strategic timing and efforts to obscure attribution
```

#### Full body

```
Infosecurity Magazine Home » News » Russian Hackers Accused of Destructive Cyber-Attack on Jaguar Land Rover Russian Hackers Accused of Destructive Cyber-Attack on Jaguar Land Rover News 29 June 2026 Written by Beth Maundrill Editor , Infosecurity Magazine Follow @GunshipGirl Connect on LinkedIn Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster Security experts and practitioners have weighed in on a new report claiming that Russia was behind the Jaguar Land Rover (JLR) breach last year. The New York Times report cited people close to the investigation in its story on June 26 linking Russian hackers to the incident, which is estimated to have cost the British economy £1.9bn ($2.5bn). Microsoft, which was tracking the Russians, reportedly raised the alarm with JLR. However, while the report didn’t explicitly link the Putin regime with the attack, experts have been more forthright. Halcyon Ransomware Research Center SVP and former FBI cyber deputy director, Cynthia Kaiser, said there are several reasons to believe Kremlin involvement. There was seemingly no ransom demand and the attack landed just before a new vehicle rollout, she said. The hackers also used novel ransomware with a “mind-blowing” algorithm, and JLR’s Land Rover fleet have strong links to the British royals and military, Kaiser argued. “There are a lot of good reasons why nation states use criminal tactics when conducting destructive attacks. They are fast, scalable, and highly repeatable. They exploit common weaknesses that exist across nearly every critical infrastructure environment. And critically, they complicate attribution, allowing attackers to operate below traditional response thresholds,” she continued. “But this is the first time I can remember where it is now highly suspected that Russia at least tacitly approved an economically destructive attack, delivering an estimated $2.5bn hit to the British economy and costing the company about $350m in the 2026 fiscal year.” Read more on JLR attack: Jaguar Land Rover's Q3 Sales Crash Amid Cyber-Attack Fallout By disguising the attack as a cybercrime effort, the threat actors helped create enough doubt to limit a geopolitical response, Kasier claimed. “Adversaries believe they can stop appropriate reactions from democratic nations by planting seeds of doubt,” she said. “We all need to be more forward leaning in expecting and responding to nation states who will almost certainly increase their use of criminal tactics in the future.” The Scattered Lapsus$ Hunters Distraction Initially, attribution efforts were complicated by claims by Scattered Lapsus$ Hunters that it was responsible for the attack, which closely followed extortion attacks on M&S and Co-op Group by Scattered Spider. However, former Paramount CISO and now VC partner, Pete Chronis, has also backed the Russia theory. “When JLR got hacked, nobody asked for money,” he said in a LinkedIn post . “Sit with that. Ransomware gangs lock you up because they want a payout. Whoever hit JLR didn’t want one. No demand, no negotiation. They just wanted the company on the floor. That’s why Russia is in the frame, and why this reads less like crime and more like sabotage.” Ashish Shrestha – CEO of Zyn Global and group CISO of JLR at the time of the cyber incident – told Infosecurity in a conversation on June 18 that at the time of the cyber-attack they knew the attacker was “quite sophisticated.” However, he did not confirm attribution of the incident. Shrestha said that within the first 24 hours of the incident the threat actors asked him not to involved law enforcement. “I had law enforcement physically in my world,” he said, and at no time did Shrestha or his team reach out to their attackers. On recovery, he noted that his team was taking its time to ensure the adversaries would not be able to conduct a follow-on attack. "Business continuity is not just about coming back, but coming back stronger," he noted. Interes
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Russian Hackers Accused of Destructive Cyber-Attack on Jaguar Land Rover
  - Published: 2026-06-29T09:15:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/russian-hackers-destructive-jaguar/
  - Summary: Experts warn the Jaguar Land Rover breach bears hallmarks of Kremlin-backed hackers, citing novel ransomware, strategic timing and efforts to obscure attribution
