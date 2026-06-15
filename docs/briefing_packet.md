# PHANTOMSignal Briefing Packet

- Generated: 2026-06-15T18:44:12.964647+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 77
- Total items in window: 351
- Total clusters raw: 154
- Total clusters in packet: 65
- Dropped low score: 89
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
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
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
  - In window count: 3
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 1
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 8
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
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
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 5
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 0
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
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
  - In window count: 0
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 20
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
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 2
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
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
  - In window count: 5
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
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
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 19
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 2
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
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
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
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 22
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 22
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
  - In window count: 7
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
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 48
- **Reddit r/AskNetsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/AskNetsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/netsecstudents** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsecstudents/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 27
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 23
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
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 0

## Affinity groups (themes)

### ShinyHunters: zero day
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 6
- Article count: 17
- Cohesion: 0.304
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, ransomware_extortion, data_breach, active_exploitation, phishing_social_eng
  - actor_attribution: ShinyHunters
  - affected_industries: education, healthcare, government
  - urgency_signals: zero_day, actively_exploited
- Cluster IDs: a0d790eb01, d1241978fa, c17e8e6642, fce5a342cc, 6c95e6291d, ed292da257
- Links:
  - https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273
  - https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-35273/
  - https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html
  - https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/
  - https://cyberscoop.com/oracle-peoplesoft-zero-day-vulnerability-shinyhunters-extortion/
  - https://www.darkreading.com/vulnerabilities-threats/shinyhunters-oracle-zero-day-higher-ed
  - https://risky.biz/RBNEWS576/
  - https://www.darkreading.com/vulnerabilities-threats/exchange-flaw-attackers-spoof-email-address
  - https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
  - https://www.reddit.com/r/netsec/comments/1u4jjia/the_axios_npm_compromise_was_visible_in_registry/
  - https://cloud.google.com/blog/topics/developers-practitioners/how-i-learned-go-in-a-day-with-antigravity-20-and-how-you-can-do-the-same/
  - https://www.securityweek.com/ransomware-attack-shuts-down-mills-of-australias-second-largest-sugar-producer/
  - https://www.securityweek.com/maine-disables-data-breach-portal-due-to-fake-submissions/

### Ivanti active exploitation
- Anchor signal: Ivanti
- Theme key: ivanti
- Cluster count: 6
- Article count: 15
- Cohesion: 0.232
- Shared strong signals: Ivanti
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day, phishing_social_eng, ransomware_extortion
  - affected_products: Ivanti, Anthropic/Claude, Microsoft Defender
  - urgency_signals: zero_day, actively_exploited
- Cluster IDs: 0678a0cc99, 00640fa234, b9c17f29cd, 9f943550b8, fce5a342cc, 5da6b03ed1
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry
  - https://labs.watchtowr.com/more-evidence-that-words-dont-mean-what-we-thought-they-meant-ivanti-sentry-pre-auth-os-command-injection-cve-2026-10520/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-10520/
  - https://www.reddit.com/r/netsec/comments/1u1neao/more_evidence_that_words_dont_mean_what_we/
  - https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html
  - https://www.darkreading.com/vulnerabilities-threats/max-severity-ivanti-sentry-flaw-exploited-24-hours
  - https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html
  - https://orca.security/resources/blog/cve-2026-5027-langflow-path-traversal-rce/
  - https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html
  - https://www.infosecurity-magazine.com/news/google-patch-chrome-vulnerability/
  - https://www.infosecurity-magazine.com/news/check-point-critical-auth-bypass/
  - https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
  - https://www.reddit.com/r/netsec/comments/1u4jjia/the_axios_npm_compromise_was_visible_in_registry/
  - https://cloud.google.com/blog/topics/developers-practitioners/how-i-learned-go-in-a-day-with-antigravity-20-and-how-you-can-do-the-same/
  - https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html

### active exploitation targeting AWS
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 5
- Article count: 8
- Cohesion: 0.271
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: AWS, Google Cloud
- Cluster IDs: 643755a74a, 1714548889, 56111b9aeb, b6bc3df279, 1674209ab9
- Links:
  - https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/
  - https://orca.security/resources/blog/cve-2026-20253-splunk-enterprise-rce-unauthenticated-file-operations/
  - https://www.reddit.com/r/netsec/comments/1u46wbb/why_use_applevel_auth_when_every_database_has/
  - https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html
  - https://aws.amazon.com/blogs/security/icymi-may-2026-aws-security/
  - https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/
  - https://webflow.sysdig.com/blog/how-attackers-are-jailbreaking-llms-with-ctf-framing-and-how-to-catch-them
  - https://trustedsec.com/blog/how-to-train-your-dragons-analysts

### Microsoft Defender active exploitation
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 4
- Article count: 6
- Cohesion: 0.291
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation, phishing_social_eng, credential_theft, ransomware_extortion
  - affected_products: Microsoft Defender, Anthropic/Claude, Ivanti
  - cve_ids: CVE-2026-11645
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 00640fa234, b9c17f29cd, fb86222de5, 5da6b03ed1
- Links:
  - https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html
  - https://orca.security/resources/blog/cve-2026-5027-langflow-path-traversal-rce/
  - https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html
  - https://www.infosecurity-magazine.com/news/google-patch-chrome-vulnerability/
  - https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks/
  - https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html

### CVE-2026-50751 exploitation activity
- Anchor signal: CVE-2026-50751
- Theme key: cve-2026-50751
- Cluster count: 3
- Article count: 9
- Cohesion: 0.243
- Shared strong signals: CVE-2026-50751
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, active_exploitation, zero_day
  - affected_industries: government, healthcare
  - affected_products: Anthropic/Claude
  - cve_ids: CVE-2026-50751
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: ccc49ba760, d1241978fa, 9f943550b8
- Links:
  - https://labs.watchtowr.com/marking-your-own-homework-check-point-remote-access-vpn-ikev1-authentication-bypass-cve-2026-50751/
  - https://www.reddit.com/r/netsec/comments/1u3m7yj/marking_your_own_homework_check_point_remote/
  - https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/
  - https://cyberscoop.com/oracle-peoplesoft-zero-day-vulnerability-shinyhunters-extortion/
  - https://www.darkreading.com/vulnerabilities-threats/shinyhunters-oracle-zero-day-higher-ed
  - https://risky.biz/RBNEWS576/
  - https://www.infosecurity-magazine.com/news/check-point-critical-auth-bypass/

### Palo Alto Networks vulnerability activity
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 4
- Article count: 7
- Cohesion: 0.2
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Palo Alto Networks
- Cluster IDs: 2974abda18, fce5a342cc, 56111b9aeb, 09b4827a59
- Links:
  - https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
  - https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html
  - https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
  - https://www.reddit.com/r/netsec/comments/1u4jjia/the_axios_npm_compromise_was_visible_in_registry/
  - https://cloud.google.com/blog/topics/developers-practitioners/how-i-learned-go-in-a-day-with-antigravity-20-and-how-you-can-do-the-same/
  - https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/
  - https://www.bleepingcomputer.com/news/security/phpbb-forum-fixes-auth-bypass-bug-lurking-for-a-decade/

### Google Cloud vulnerability activity
- Anchor signal: Google Cloud
- Theme key: google-cloud
- Cluster count: 3
- Article count: 5
- Cohesion: 0.294
- Shared strong signals: Google Cloud
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Google Cloud, AWS
- Cluster IDs: e90454cc0b, 56111b9aeb, 1674209ab9
- Links:
  - https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research/
  - https://www.securityweek.com/chinese-hackers-target-medical-military-and-ai-research-in-north-america/
  - https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/
  - https://trustedsec.com/blog/how-to-train-your-dragons-analysts

### Fortinet vulnerability activity
- Anchor signal: Fortinet
- Theme key: fortinet
- Cluster count: 2
- Article count: 7
- Cohesion: 0.2
- Shared strong signals: Fortinet
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Fortinet
- Cluster IDs: 0678a0cc99, 09b4827a59
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry
  - https://labs.watchtowr.com/more-evidence-that-words-dont-mean-what-we-thought-they-meant-ivanti-sentry-pre-auth-os-command-injection-cve-2026-10520/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-10520/
  - https://www.reddit.com/r/netsec/comments/1u1neao/more_evidence_that_words_dont_mean_what_we/
  - https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html
  - https://www.darkreading.com/vulnerabilities-threats/max-severity-ivanti-sentry-flaw-exploited-24-hours
  - https://www.bleepingcomputer.com/news/security/phpbb-forum-fixes-auth-bypass-bug-lurking-for-a-decade/

### CVE-2026-41091 exploitation activity
- Anchor signal: CVE-2026-41091
- Theme key: cve-2026-41091
- Cluster count: 2
- Article count: 7
- Cohesion: 0.2
- Shared strong signals: CVE-2026-41091
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: GitHub
  - cve_ids: CVE-2026-41091
  - urgency_signals: actively_exploited, poc_available
- Cluster IDs: c1b5a1d701, d1241978fa
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026
  - https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/
  - https://cyberscoop.com/oracle-peoplesoft-zero-day-vulnerability-shinyhunters-extortion/
  - https://www.darkreading.com/vulnerabilities-threats/shinyhunters-oracle-zero-day-higher-ed
  - https://risky.biz/RBNEWS576/

### CVE-2026-42271 exploitation activity
- Anchor signal: CVE-2026-42271
- Theme key: cve-2026-42271
- Cluster count: 2
- Article count: 2
- Cohesion: 0.275
- Shared strong signals: CVE-2026-42271
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-42271
  - urgency_signals: actively_exploited
- Cluster IDs: 5aa5b8e746, b6bc3df279
- Links:
  - https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html
  - https://webflow.sysdig.com/blog/how-attackers-are-jailbreaking-llms-with-ctf-framing-and-how-to-catch-them

### CVE-2026-27022 exploitation activity
- Anchor signal: CVE-2026-27022
- Theme key: cve-2026-27022
- Cluster count: 2
- Article count: 7
- Cohesion: 0.2
- Shared strong signals: CVE-2026-27022
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - cve_ids: CVE-2026-27022
- Cluster IDs: d1241978fa, 3e3984a344
- Links:
  - https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/
  - https://cyberscoop.com/oracle-peoplesoft-zero-day-vulnerability-shinyhunters-extortion/
  - https://www.darkreading.com/vulnerabilities-threats/shinyhunters-oracle-zero-day-higher-ed
  - https://risky.biz/RBNEWS576/
  - https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/

### Microsoft Windows vulnerability activity
- Anchor signal: Microsoft Windows
- Theme key: microsoft-windows
- Cluster count: 2
- Article count: 3
- Cohesion: 0.2
- Shared strong signals: Microsoft Windows
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Windows
- Cluster IDs: 2974abda18, 655ad7f913
- Links:
  - https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
  - https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-june-2026-snort-rules-and-prominent-vulnerabilities/

## Forward signals

### Novelty
- Novel cves: 6
  - CVE-2026-20262 (first seen via BleepingComputer at 2026-06-15T17:12:42+00:00, cluster fb86222de5)
  - CVE-2026-40217 (first seen via The Hacker News at 2026-06-15T16:39:01+00:00, cluster 29fcf4633f)
  - CVE-2026-47101 (first seen via The Hacker News at 2026-06-15T16:39:01+00:00, cluster 29fcf4633f)
  - CVE-2026-47102 (first seen via The Hacker News at 2026-06-15T16:39:01+00:00, cluster 29fcf4633f)
  - CVE-2026-42589 (first seen via Sysdig at 2026-06-15T00:00:00+00:00, cluster b6bc3df279)
  - CVE-2026-44336 (first seen via Sysdig at 2026-06-15T00:00:00+00:00, cluster b6bc3df279)
- Novel actors: 1
  - UNC6508 (first seen via Google Cloud Threat Intelligence at 2026-06-15T14:00:00+00:00, cluster e90454cc0b)
- Novel products: 0

### Velocity bursts (1)
- **Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research**
  - Cluster: e90454cc0b
  - Sources in window: 3
  - Window hours: 0.1
  - Cohort count: 3

### Leading edge (1)
- **15th June – Threat Intelligence Report**
  - Cluster: d1241978fa
  - Lead hours: 80.9
  - First source: Risky Business News
  - Later Tier 1 source: Check Point Research
  - Shared signals: Anthropic/Claude, CVE-2026-27022, CVE-2026-35273, CVE-2026-41091, CVE-2026-45657, CVE-2026-50751, GitHub, Microsoft BitLocker, Salesforce, ShinyHunters, npm

### Convergence (15)
- Pair: CVE-2013-3821 + ShinyHunters (cluster a0d790eb01, first observation: True)
- Pair: CVE-2013-3821 + UNC6240 (cluster a0d790eb01, first observation: True)
- Pair: CVE-2013-3821 + Azure (cluster a0d790eb01, first observation: True)
- Pair: CVE-2017-3548 + ShinyHunters (cluster a0d790eb01, first observation: True)
- Pair: CVE-2017-3548 + UNC6240 (cluster a0d790eb01, first observation: True)
- Pair: CVE-2017-3548 + Azure (cluster a0d790eb01, first observation: True)
- Pair: CVE-2026-35273 + ShinyHunters (cluster a0d790eb01, first observation: True)
- Pair: CVE-2026-35273 + UNC6240 (cluster a0d790eb01, first observation: True)
- Pair: CVE-2026-35273 + Azure (cluster a0d790eb01, first observation: True)
- Pair: ShinyHunters + Azure (cluster a0d790eb01, first observation: True)
- Pair: UNC6240 + Azure (cluster a0d790eb01, first observation: True)
- Pair: CVE-2026-20253 + AWS (cluster 643755a74a, first observation: True)
- Pair: CVE-2020-15505 + Fortinet (cluster 0678a0cc99, first observation: True)
- Pair: CVE-2020-15505 + Ivanti (cluster 0678a0cc99, first observation: True)
- Pair: CVE-2023-38035 + Fortinet (cluster 0678a0cc99, first observation: True)

### Drift (4)
- **ShinyHunters** (cluster a0d790eb01)
  - New industries: (none)
  - New products: Azure
  - Prior top industries: education, government, telecommunications
  - Prior top products: Google/Gemini, Microsoft Windows, npm
- **MuddyWater** (cluster 00640fa234)
  - New industries: (none)
  - New products: Anthropic/Claude, Ivanti, Microsoft Defender
  - Prior top industries: (none)
  - Prior top products: Android, GitHub, Microsoft 365
- **Handala** (cluster fce5a342cc)
  - New industries: healthcare
  - New products: Ivanti
  - Prior top industries: critical_infrastructure, financial_services, government
  - Prior top products: Fortinet, Palo Alto Networks, npm
- **Silent Ransom Group** (cluster 6c95e6291d)
  - New industries: education, government, healthcare, manufacturing_industrial
  - New products: (none)
  - Prior top industries: critical_infrastructure, financial_services, legal_professional
  - Prior top products: OpenAI/ChatGPT, SolarWinds, WordPress

### Persistence (1)
- actor_attribution: ShinyHunters (weeks observed: 3, cluster a0d790eb01)

### Tier inversion (2)
- **LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers**
  - Cluster: 29fcf4633f
  - Primary source: The Hacker News
  - Strong signals: CVE-2026-40217, CVE-2026-47101, CVE-2026-47102
- **NPM 12 Will Change Script Execution Behavior to Prevent Supply Chain Attacks**
  - Cluster: fce5a342cc
  - Primary source: SecurityWeek
  - Strong signals: Handala, ShinyHunters

## Clusters

### Cluster a0d790eb01 — score 69

- Title: Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-12T13:43:04+00:00
- Link: https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: CVE-2026-35273

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters, UNC6240
- affected_industries: education, telecommunications
- affected_products: Azure
- cve_ids: CVE-2013-3821, CVE-2017-3548, CVE-2026-35273
- urgency_signals: actively_exploited, critical_cvss, emergency_patch, no_patch_yet, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach, active_exploitation
- actor_attribution: ShinyHunters, UNC6240
- affected_industries: telecommunications, education
- affected_products: Azure
- cve_ids: CVE-2026-35273, CVE-2013-3821, CVE-2017-3548
- urgency_signals: actively_exploited, zero_day, emergency_patch
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On June 10, 2026, Oracle published a security alert for CVE-2026-35273 , a critical vulnerability in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools. Oracle released an out-of-band patch the same day as the advisory, underscoring the urgency of remediation. The vulnerability has a CVSSv3.1 score of 9.8 and is remotely exploitable without authentication. Per the vendor advisory, successful exploitation may result in remote code execution (RCE). TrendAI has classified the underlying flaw as a server-side request forgery ( CWE-918 ). PeopleTools versions 8.61 and 8.62 are affected. CVE-2026-35273 was reported to Oracle through TrendAI's Zero Day Initiative. According to a report published by Mandiant on June 11, 2026, this vulnerability has been exploited in the wild as a zero-day prior to the vendor security alert , with active exploitation observed between May 27 and June 9, 2026, predating Oracle's advisory by two weeks. The vulnerability was
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273) Jonah Burgess Jun 12, 2026 | Last updated on Jun 12, 2026 | 5 min read Overview On June 10, 2026, Oracle published a security alert for CVE-2026-35273 , a critical vulnerability in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools. Oracle released an out-of-band patch the same day as the advisory, underscoring the urgency of remediation. The vulnerability has a CVSSv3.1 score of 9.8 and is remotely exploitable without authentication. Per the vendor advisory, successful exploitation may result in remote code execution (RCE). TrendAI has classified the underlying flaw as a server-side request forgery ( CWE-918 ). PeopleTools versions 8.61 and 8.62 are affected. CVE-2026-35273 was reported to Oracle through TrendAI's Zero Day Initiative. According to a report published by Mandiant on June 11, 2026, this vulnerability has been exploited in the wild as a zero-day prior to the vendor security alert , with active exploitation observed between May 27 and June 9, 2026, predating Oracle's advisory by two weeks. The vulnerability was added to the CISA KEV on June 12, 2026. Mandiant has attributed the campaign to UNC6240 (ShinyHunters), a financially motivated cybercriminal collective known for data theft and extortion. ShinyHunters has been linked to breaches across cloud services, SaaS platforms, and telecommunications providers, frequently exploiting weak authentication controls, stolen credentials, and cloud misconfigurations rather than deploying sophisticated malware. Based on information published by Mandiant, the campaign heavily targeted the higher education sector; 68 percent of the more than 100 notified organizations were universities and colleges. The observed exploitation targeted PeopleSoft's Environment Management Hub (PSEMHUB) endpoints, and data stolen during the campaign was published on the ShinyHunters Data Leak Site (DLS) on June 9, 2026. The /PSIGW/HttpListeningConnector URI path appears in both the indicators of compromise for this campaign and in a PeopleSoft exploit chain for CVE-2013-3821 , detailed by Lexfo in 2017 . A related XML External Entity (XXE) vulnerability, CVE-2017-3548 , targeted a different Integration Gateway connector ( PeopleSoftServiceListeningConnector ) under the same /PSIGW/ path. Technical overview TrendAI's detection signatures for CVE-2026-35273 classify the underlying vulnerability as an SSRF. These include IPS Rule 1012580 ("Oracle Peoplesoft PeopleTools SSRF Vulnerability") and DDI Rule 5855 ("Peoplesoft PeopleTools Environment Management Hub (PSEMHUB) SSRF Exploit"). Mandiant describes CVE-2026-35273 as a critical remote code execution vulnerability, indicating that the SSRF serves as the mechanism through which code execution is achieved. Based on Mandiant's analysis, two endpoints are involved in exploitation: /PSEMHUB/hub and /PSIGW/HttpListeningConnector . The exploit chain may also cause the target system to make outbound SMB connections (TCP port 445) to external destinations, potentially allowing attackers to capture Windows machine-account NetNTLM hashes. Post-exploitation activity observed by Mandiant included the deployment of MeshCentral (an open-source, and self-hosted web-based remote monitoring and management platform) remote management agents configured to masquerade as Microsoft Azure services (e.g., meshagent64-azure-ops.exe ), with C2 communications directed to wss://azurenetfiles[.]net:443/agent.ashx . The attackers performed internal reconnaissance of PeopleSoft configurations, deployed lateral movement scripts, and exfiltrated data using zstd compression. Mitigation guidance Organizations running PeopleTools versions 8.61 or 8.62 should apply the vendor-supplied patch on an emergency basis, without waiting for a regular patch cycle to occur. Oracle has characterized this as a high-priority risk reduction measure. In addition
```

#### Corroborating sources (5)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273)
  - Published: 2026-06-12T13:43:04+00:00
  - Link: https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273
  - Summary: Overview On June 10, 2026, Oracle published a security alert for CVE-2026-35273 , a critical vulnerability in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools. Oracle released an out-of-band patch the same day as the advisory, underscoring the urgency of remediation. The vulnerability has a CVSSv3.1 score of 9.8 and is remotely exploitable without authentication. Per the vendor advisory, successful exploitation may result in remote code execution (RCE). TrendAI has classified the underlying flaw as a server-side request forgery ( CWE-918 ). PeopleTools versions 8.61 and 8.62 are affected. CVE-2026-35273 was reported to Oracle through TrendAI's Zero Day Initiative. According to a report published by Mandiant on June 11, 2026, this vulnerability has been exploited in the wild as a zero-day prior to the vendor security alert , with active exploitation observed between May 27 and June 9, 2026, predating Oracle's advisory by two weeks. The vulnerability was
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit
  - Published: 2026-06-11T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/
  - Summary: Introduction Mandiant and Google Threat Intelligence Group (GTIG) have identified an active compromise and extortion campaign attributed to UNC6240 (ShinyHunters) targeting Oracle PeopleSoft application infrastructure. The activity was observed between May 27, 2026, and June 9, 2026 and is consistent with the exploitation of CVE-2026-35273 , a critical remote code execution vulnerability (CVSS 9.8) in the Environment Management component. The exploitation of this vulnerability directly aligns with the observed targeting of Environment Management Hub (PSEMHUB) endpoints. Because this activity predates Oracle's June 10, 2026 advisory, the vulnerability was exploited as a zero-day. Upon becoming aware of active scanning and exploitation, we initiated notifications to over 100 global organizations whose IP addresses correlated with potentially vulnerable endpoints. Most of these organizations were based in the United States, and 68 percent operated within the higher education sector. Subse
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-35273 | Oracle PeopleSoft PeopleTools Unauthenticated Remote Code Execution Vulnerability | Active Exploitation
  - Published: 2026-06-12T20:04:24+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-35273/
  - Summary: CVE-2026-35273 is a critical unauthenticated remote code execution vulnerability affecting Oracle PeopleSoft PeopleTools. Threat intelligence confirms active exploitation by ShinyHunters prior to disclosure.
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit
  - Published: 2026-06-11T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/
  - Summary: Introduction Mandiant and Google Threat Intelligence Group (GTIG) have identified an active compromise and extortion campaign attributed to UNC6240 (ShinyHunters) targeting Oracle PeopleSoft application infrastructure. The activity was observed between May 27, 2026, and June 9, 2026 and is consistent with the exploitation of CVE-2026-35273 , a critical remote code execution vulnerability (CVSS 9.8) in the Environment Management component. The exploitation of this vulnerability directly aligns with the observed targeting of Environment Management Hub (PSEMHUB) endpoints. Because this activity predates Oracle's June 10, 2026 advisory, the vulnerability was exploited as a zero-day. Upon becoming aware of active scanning and exploitation, we initiated notifications to over 100 global organizations whose IP addresses correlated with potentially vulnerable endpoints. Most of these organizations were based in the United States, and 68 percent operated within the higher education sector. Subse
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ShinyHunters Exploits Oracle PeopleSoft Zero-Day (CVE-2026-35273) to Breach Universities
  - Published: 2026-06-11T20:29:23+00:00
  - Link: https://thehackernews.com/2026/06/shinyhunters-exploits-oracle-peoplesoft.html
  - Summary: The ShinyHunters extortion crew exploited an unpatched flaw in Oracle PeopleSoft to break into enterprise systems, steal data, and demand payment to keep it private. The campaign hit universities hardest. Google's Mandiant attributes it to the group it tracks as UNC6240, and dates the activity between May 27 and June 9. Oracle did not publish its advisory until June 10, so the bug was a

### Cluster 643755a74a — score 48

- Title: Why Use App-Level Auth When Every Database Has Auth? (Splunk Enterprise CVE-2026-20253 Pre-Auth RCE)
- Source: watchTowr Labs (offensive_vulnerability_research)
- Published: 2026-06-12T20:35:13+00:00
- Link: https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-20253

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: AWS
- cve_ids: CVE-2026-20253
- urgency_signals: critical_cvss, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: AWS
- cve_ids: CVE-2026-20253
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Three posts? In three days? Are we insane? We're home alone, there's no one to stop us, and we're up past bedtime. So, we need to talk about Splunk. On June 10th, Splunk published this CVE-2026-20253 advisory : It has everything that we
```

#### Full body

```
Three posts? In three days? Are we insane? We're home alone, there's no one to stop us, and we're up past bedtime. So, we need to talk about Splunk. On June 10th, Splunk published this CVE-2026-20253 advisory : It has everything that we love: No authentication requirements, An almost full-mark CVSS score, Claims to be a security product, Vulnerability name longer than the average piece of spaghetti. We immediately had questions, though: No explicit mention of RCE, But a CVSS score of 9.8 suggests something is possible. Is this a default-install vulnerability, or does it require star/moon alignment? Only one way to find out? As always, watchTowr clients gain industry-first access to our research days before publication to validate their exposure, accompanied by Active Defense capabilities to autonomously mitigate exposure. This research is a glimpse into the capability that powers our Preemptive Exposure Management solution, and gets organizations ahead of inevitable in-the-wild exploitation: the watchTowr Platform. What Is A Splunk? We thought you’d never ask. Splunk Enterprise is a software platform for searching, monitoring, and analyzing machine-generated data at scale. It ingests logs, metrics, and event data from across an organization's IT environment - servers, applications, network devices, and security tools - and indexes it so it can be queried in near real time using Splunk's Search Processing Language (SPL). Teams use it to build dashboards, trigger alerts, and investigate operational or security issues from a single repository. Splunk Enterprise acts as the core engine of the wider Splunk ecosystem, supporting use cases from infrastructure monitoring to security information and event management (SIEM). So, now you know. Thanks, Mythos. So, Is It Vulnerable By Default? Well, friends, let’s take a look. As we can read in the advisory, the vulnerability exists in something called the “PostgreSQL Sidecar Service Endpoint”. We are not Splunk experts (thankfully, for those around us), but we have been forced to realize that Splunk comes in many shapes and forms. For example: Splunk Enterprise On-Premise (installed manually) on Windows - PostgreSQL Sidecar Service is not installed by default. Splunk Enterprise On-Premise (installed manually) on Windows - PostgreSQL Sidecar Service is installed, but not enabled by default. Splunk Enterprise on AWS - PostgreSQL Sidecar Service is installed and enabled by default. Tl;dr Splunk Enterprise on AWS is vulnerable out of the box. Going further through the advisory, we can see that the vulnerability affects Splunk versions 10 and above. Again, not experts, but we’re led to believe that the concept of a ‘Sidecar’ was introduced in Splunk version 10, so the stars are aligning and making sense. Below is a list of vulnerable and “different” versions from the official advisory: With that, we have enough information to begin our usual drama, and so we dug in. Finding The Vulnerable Service As discussed, the advisory has already provided us with a good selection of hints. The first (it’s in the title) indicates that the vulnerability exists within the PostgreSQL Sidecar Service. A quick Google search revealed that all the Sidecar Services should be deployed in the /opt/splunk/var/run/supervisor/pkg-run/ directory: The one with the postgres in its name felt like a good initial candidate: Knowing that it should be running by default, we quickly decided to confirm that this was the case, and whether it was exposing anything to a network interface: ss -tupln | grep -i splunk-postgres tcp LISTEN ... 127.0.0.1:5435 0.0.0.0:* users:(("splunk-postgres",pid=4067,fd=12)) tcp LISTEN ... 127.0.0.1:33669 0.0.0.0:* users:(("splunk-postgres",pid=4067,fd=3)) This was a promising start. We had a very large splunk-postgres binary to stare at, and we knew it was listening on several ports, including 5435 . There was one small problem: those ports were only bound to the loopback interface. Years of vulnerab
```

#### Corroborating sources (4)

- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: Why Use App-Level Auth When Every Database Has Auth? (Splunk Enterprise CVE-2026-20253 Pre-Auth RCE)
  - Published: 2026-06-12T20:35:13+00:00
  - Link: https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/
  - Summary: Three posts? In three days? Are we insane? We're home alone, there's no one to stop us, and we're up past bedtime. So, we need to talk about Splunk. On June 10th, Splunk published this CVE-2026-20253 advisory : It has everything that we
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Critical Splunk Enterprise Vulnerabilities Allow Unauthenticated File Operations and Remote Code Execution
  - Published: 2026-06-11T17:01:23+00:00
  - Link: https://orca.security/resources/blog/cve-2026-20253-splunk-enterprise-rce-unauthenticated-file-operations/
  - Summary: Executive Summary A critical vulnerability (CVE-2026-20253, CVSS 9.8) was disclosed alongside three additional high-severity flaws affecting Splunk Enterprise, Splunk Cloud Platform, and the Splunk Secure Gateway app, allowing attackers to perform unauthenticated arbitrary file creation/truncation, remote code execution, stored cross-site scripting, and server-side request forgery. Due to the potential for full infrastructure compromise in enterprise […]
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Why Use App-Level Auth When Every Database Has Auth? (Splunk Enterprise CVE-2026-20253 Pre-Auth RCE) - watchTowr Labs
  - Published: 2026-06-12T20:37:06+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u46wbb/why_use_applevel_auth_when_every_database_has/
  - Summary: submitted by /u/dx7r__ [link] [comments]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication
  - Published: 2026-06-13T13:23:03+00:00
  - Link: https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html
  - Summary: Splunk has released security updates to address a critical security flaw in Splunk Enterprise that could be exploited to conduct unauthenticated file operations and even remote code execution. The vulnerability, tracked as CVE-2026-20253, is rated 9.8 on the CVSS scoring system. "In Splunk Enterprise versions below 10.2.4 and 10.0.7, an unauthenticated user could create or truncate arbitrary

### Cluster 0678a0cc99 — score 44

- Title: CVE-2026-10520, CVE-2026-10523 - Multiple critical vulnerabilities affecting Ivanti Sentry
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-10T10:21:07+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: CVE-2026-10520, CVE-2026-10523, Ivanti

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Fortinet, Ivanti
- cve_ids: CVE-2020-15505, CVE-2023-38035, CVE-2026-10520, CVE-2026-10523, CVE-2026-25089
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Ivanti
- cve_ids: CVE-2026-10520, CVE-2026-10523, CVE-2023-38035, CVE-2020-15505
- urgency_signals: preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On June 9, 2026, Ivanti published a security advisory for two critical vulnerabilities affecting Ivanti Sentry (formerly known as MobileIron Sentry), which per the vendor website is an “in-line gateway that manages, encrypts, and secures traffic between the mobile device and back-end enterprise systems”. The most severe issue, CVE-2026-10520 , is an OS command injection vulnerability with a CVSS score of 10.0 that allows a remote unauthenticated attacker to achieve remote code execution (RCE) with root privileges. The second vulnerability, CVE-2026-10523 , is an authentication bypass vulnerability with a CVSS score of 9.9 that allows a remote unauthenticated attacker to create arbitrary administrative accounts and obtain full administrative access. Ivanti has stated that they are not aware of any customers being exploited by either of these vulnerabilities at the time of disclosure. CVE CVSSv3.1 CWE CVE-2026-10520 10.0 (Critical) OS Command Injection ( CWE-78 ) CVE-2026-10523
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-10520, CVE-2026-10523 - Multiple critical vulnerabilities affecting Ivanti Sentry Rapid7 Jun 10, 2026 | Last updated on Jun 12, 2026 | 3 min read Overview On June 9, 2026, Ivanti published a security advisory for two critical vulnerabilities affecting Ivanti Sentry (formerly known as MobileIron Sentry), which per the vendor website is an “in-line gateway that manages, encrypts, and secures traffic between the mobile device and back-end enterprise systems”. The most severe issue, CVE-2026-10520 , is an OS command injection vulnerability with a CVSS score of 10.0 that allows a remote unauthenticated attacker to achieve remote code execution (RCE) with root privileges. The second vulnerability, CVE-2026-10523 , is an authentication bypass vulnerability with a CVSS score of 9.9 that allows a remote unauthenticated attacker to create arbitrary administrative accounts and obtain full administrative access. Ivanti has stated that they are not aware of any customers being exploited by either of these vulnerabilities at the time of disclosure. CVE CVSSv3.1 CWE CVE-2026-10520 10.0 (Critical) OS Command Injection ( CWE-78 ) CVE-2026-10523 9.9 (Critical) Authentication Bypass Using an Alternate Path or Channel ( CWE-288 ) On June 10, 2026, watchTowr published a technical analysis of CVE-2026-10520 that includes a proof-of-concept (PoC) exploit for unauthenticated RCE. Given the trivial nature of exploitation and the availability of a public PoC, exploitation in-the-wild is likely to begin. Ivanti Sentry has featured on the CISA KEV list twice in the past (for the vulnerabilities CVE-2023-38035 and CVE-2020-15505), so we know threat actors will likely target this product. On June 11, 2026, CVE-2026-10520 was added to the U.S. Cybersecurity and Infrastructure Security Agency’s (CISA) list of known exploited vulnerabilities (KEV), based on evidence of active exploitation. With active exploitation now occurring, organizations running affected versions of Ivanti Sentry should remediate these issues on an urgent basis, outside of normal patching cycles. Technical overview for CVE-2026-10520 Based upon the technical analysis by watchTowr, CVE-2026-10520 resides in the ConfigServiceController class within the Sentry web application, which is accessible via a POST request to the unauthenticated endpoint /mics/api/v2/sentry/mics-config/handleMessage . The handleMessage endpoint accepts an attacker supplied message parameter that is parsed as an internal configuration command. This ultimately results in arbitrary OS command execution as root with an attacker control OS command. Shown below is an example HTTP request generated by the public PoC to execute the id command on an affected system: POST /mics/api/v2/sentry/mics-config/handleMessage HTTP/1.1 Host: [redacted] User-Agent: python-requests/2.33.0 Accept-Encoding: gzip, deflate Accept: */* Connection: keep-alive Content-Type: application/x-www-form-urlencoded Content-Length: 161 message=execute+system+%2Fconfiguration%2Fsystem%2Fcommandexec+%3Ccommandexec%3E%3Cindex%3E1%3C%2Findex%3E%3Creqandres%3Eid%3C%2Freqandres%3E%3C%2Fcommandexec%3E Mitigation guidance A vendor-supplied update is available to remediate both CVE-2026-10520 and CVE-2026-10523. The following versions of Ivanti Sentry are affected: Ivanti Sentry 10.7.0 and below Ivanti Sentry 10.6.1 and below Ivanti Sentry 10.5.1 and below The following fixed versions of Ivanti Sentry remediate both vulnerabilities: Ivanti Sentry 10.7.1 Ivanti Sentry 10.6.2 Ivanti Sentry 10.5.2 Given the critical severity of these vulnerabilities, the availability of a public PoC exploit for CVE-2026-10520, and the unauthenticated attack vector, Rapid7 strongly recommends updating affected Ivanti Sentry appliances on an urgent basis, outside of normal patching cycles. For the latest mitigation guidance, please refer to the vendor's security advisory . Rapid7 customers Exposure Command, InsightVM, and Nexpose Ex
```

#### Corroborating sources (6)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-10520, CVE-2026-10523 - Multiple critical vulnerabilities affecting Ivanti Sentry
  - Published: 2026-06-10T10:21:07+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-10520-cve-2026-10523-multiple-critical-vulnerabilities-affecting-ivanti-sentry
  - Summary: Overview On June 9, 2026, Ivanti published a security advisory for two critical vulnerabilities affecting Ivanti Sentry (formerly known as MobileIron Sentry), which per the vendor website is an “in-line gateway that manages, encrypts, and secures traffic between the mobile device and back-end enterprise systems”. The most severe issue, CVE-2026-10520 , is an OS command injection vulnerability with a CVSS score of 10.0 that allows a remote unauthenticated attacker to achieve remote code execution (RCE) with root privileges. The second vulnerability, CVE-2026-10523 , is an authentication bypass vulnerability with a CVSS score of 9.9 that allows a remote unauthenticated attacker to create arbitrary administrative accounts and obtain full administrative access. Ivanti has stated that they are not aware of any customers being exploited by either of these vulnerabilities at the time of disclosure. CVE CVSSv3.1 CWE CVE-2026-10520 10.0 (Critical) OS Command Injection ( CWE-78 ) CVE-2026-10523
- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: More Evidence That Words Don't Mean What We Thought They Meant (Ivanti Sentry Pre-Auth OS Command Injection CVE-2026-10520)
  - Published: 2026-06-10T00:52:20+00:00
  - Link: https://labs.watchtowr.com/more-evidence-that-words-dont-mean-what-we-thought-they-meant-ivanti-sentry-pre-auth-os-command-injection-cve-2026-10520/
  - Summary: Today, Ivanti published an advisory. “No way?” we hear you say. "Yes way!" Today’s advisory outlines two vulnerabilities in Ivanti’s Sentry product, appealing directly to our inner desire for sophisticated server-side, pre-authenticated vulnerabilities. CVE-2026-10520 An OS Command Injection
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-10520 | Ivanti Sentry Pre-Authenticated OS Command Injection Vulnerability |
  - Published: 2026-06-11T15:35:02+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-10520/
  - Summary: CVE-2026-10520 is a critical pre-authenticated OS command injection vulnerability in Ivanti Sentry that allows remote attackers to execute arbitrary commands as root.
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: More Evidence That Words Don't Mean What We Thought They Meant (Ivanti Sentry Pre-Auth OS Command Injection CVE-2026-10520) - watchTowr Labs
  - Published: 2026-06-10T00:54:34+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u1neao/more_evidence_that_words_dont_mean_what_we/
  - Summary: submitted by /u/dx7r__ [link] [comments]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities
  - Published: 2026-06-10T15:10:59+00:00
  - Link: https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html
  - Summary: Fortinet, Ivanti, and SAP have released security updates to address multiple critical security vulnerabilities that could result in arbitrary code execution and information disclosure. The security flaw patched by Fortinet relates to a command injection vulnerability in FortiSandbox, FortiSandbox Cloud, and FortiSandbox PaaS WEB UI. It's tracked as CVE-2026-25089 (CVSS score: 9.1). "An
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Max-Severity Ivanti Flaw Exploited 24 Hours After Disclosure
  - Published: 2026-06-11T18:43:57+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/max-severity-ivanti-sentry-flaw-exploited-24-hours
  - Summary: Initial methods suggest attackers had likely mapped out Ivanti's asset landscape upfront and acted quickly once the exploit became public.

### Cluster 00640fa234 — score 33

- Title: Langflow Vulnerability CVE-2026-5027 Exploited for Unauthenticated RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-10T15:00:59+00:00
- Link: https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-5027

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, phishing_social_eng, zero_day
- actor_attribution: MuddyWater
- affected_products: Anthropic/Claude, Ivanti, Microsoft Defender
- cve_ids: CVE-2025-34291, CVE-2026-0770, CVE-2026-21445, CVE-2026-33017, CVE-2026-5027
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage, active_exploitation
- actor_attribution: MuddyWater
- affected_products: Anthropic/Claude, Ivanti, Microsoft Defender
- cve_ids: CVE-2026-5027, CVE-2026-0770, CVE-2026-33017, CVE-2026-21445, CVE-2025-34291
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
A high-severity security flaw in Langflow, an open-source low-code platform to build artificial intelligence (AI) applications, has come under active exploitation in the wild, according to findings from VulnCheck. The vulnerability in question is CVE-2026-5027 (CVSS score: 8.8), a case of path traversal that could allow an attacker to write files to arbitrary locations. "The 'POST /api/v2/
```

#### Full body

```
Langflow Vulnerability CVE-2026-5027 Exploited for Unauthenticated RCE  Ravie Lakshmanan  Jun 10, 2026 Vulnerability / Open Source A high-severity security flaw in Langflow, an open-source low-code platform to build artificial intelligence (AI) applications, has come under active exploitation in the wild, according to findings from VulnCheck. The vulnerability in question is CVE-2026-5027 (CVSS score: 8.8), a case of path traversal that could allow an attacker to write files to arbitrary locations. "The 'POST /api/v2/files' endpoint does not sanitize the 'filename' parameter from the multipart form data, allowing an attacker to write files to arbitrary locations on the filesystem using path traversal sequences ('../')," Tenable, which discovered the flaw, said in an alert released in late March 2026. The cybersecurity company said it attempted to contact the project maintainers three times in January and February 2026, before disclosing details of the issue on March 27. Caitlin Condon, vice president of security research at VulnCheck, said in a LinkedIn post that the vulnerability enables remote code execution. "Because Langflow enables unauthenticated auto-login by default, no credentials are required to reach the vulnerable endpoint, and a single unauthenticated request is sufficient to obtain a valid session token before proceeding with exploitation," Condon added. Exploitation efforts so far appear to weaponize the bug to write test files on victim systems. Data from Censys shows that there are about 7,000 Langflow instances publicly exposed on the internet, with a majority of them located in North America. The attack effort follows a flurry of exploitation activity targeting other Langflow vulnerabilities this year, including CVE-2026-0770 , CVE-2026-33017 , CVE-2026-21445 , and CVE-2025-34291 , the last of which has been weaponized by the Iranian state-sponsored group known as MuddyWater. "The activity underscores a growing trend of attackers targeting the infrastructure and tooling that organizations use to build and deploy AI applications," the company said in a statement shared with The Hacker News. Update When reached for comment regarding the patch status, Tenable told The Hacker News via email that the project maintainer of the langflow-base package confirmed the vulnerability was addressed in Langflow version 1.9.0 released on April 15, 2026 . Users are advised to update to the latest version for optimal protection. (The story was updated after publication to include details of the patch availability.) Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  AI , Censys , cybersecurity , exploitation , Langflow , MuddyWater , Open Source , Path Traversal , remote code execution , Vulnerability ⚡ Top Stories This Week Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities Cybersecurity Stars Awards 2026: Winners Announced Across 95 Categories ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories New GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files Agentjacking Attack Tricks AI Coding Agents Into Running Malicious Code China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication U.S. Orders Anthropic to Suspend Fable 5 and Mythos 5 Access for Foreign Nationals Over 400 Arch Linux AUR Packages Hijacked to Deploy
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Langflow Vulnerability CVE-2026-5027 Exploited for Unauthenticated RCE
  - Published: 2026-06-10T15:00:59+00:00
  - Link: https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html
  - Summary: A high-severity security flaw in Langflow, an open-source low-code platform to build artificial intelligence (AI) applications, has come under active exploitation in the wild, according to findings from VulnCheck. The vulnerability in question is CVE-2026-5027 (CVSS score: 8.8), a case of path traversal that could allow an attacker to write files to arbitrary locations. "The 'POST /api/v2/
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Critical Langflow Path Traversal Flaw Exploited for Unauthenticated RCE
  - Published: 2026-06-11T17:03:15+00:00
  - Link: https://orca.security/resources/blog/cve-2026-5027-langflow-path-traversal-rce/
  - Summary: Executive Summary A high-severity vulnerability (CVE-2026-5027, CVSS 8.8) was disclosed affecting Langflow, an open-source low-code platform widely used for building AI applications, allowing attackers to achieve remote code execution via a path traversal in the file upload endpoint. Due to the potential for full system compromise and the trivial nature of exploitation, immediate patching is […]

### Cluster 5aa5b8e746 — score 31

- Title: LiteLLM Flaw CVE-2026-42271 Exploited in the Wild, Chains to Unauthenticated RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-09T06:26:14+00:00
- Link: https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-42271

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-42208, CVE-2026-42271, CVE-2026-48710
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-42271, CVE-2026-48710, CVE-2026-42208
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a high-severity flaw impacting BerriAI LiteLLM to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerability, tracked as CVE-2026-42271 (CVSS score: 8.7), is a command injection vulnerability that could allow any authenticated user to run arbitrary commands on the
```

#### Full body

```
LiteLLM Flaw CVE-2026-42271 Exploited in the Wild, Chains to Unauthenticated RCE  Ravie Lakshmanan  Jun 09, 2026 Vulnerability / Artificial Intelligence The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a high-severity flaw impacting BerriAI LiteLLM to its Known Exploited Vulnerabilities ( KEV ) catalog, citing evidence of active exploitation. The vulnerability, tracked as CVE-2026-42271 (CVSS score: 8.7), is a command injection vulnerability that could allow any authenticated user to run arbitrary commands on the host. It affects the following version of the LiteLLM Python package - >= 1.74.2 < 1.83.7 "Two endpoints used to preview an MCP server before saving it - POST /mcp-rest/test/connection and POST /mcp-rest/test/tools/list - accepted a full server configuration in the request body, including the command, args, and env fields used by the stdio transport," according to a description of the flaw shared by BerriAI. "When called with a stdio configuration, the endpoints attempted to connect, which spawned the supplied command as a subprocess on the proxy host with the privileges of the proxy process." The maintainers of the open-source AI gateway and Python SDK said the endpoints were secured only by means of a valid proxy API key, as a result of which any authenticated user, including privileged internal-user keys, could execute arbitrary commands on a susceptible system. As part of the patches released in version 1.83.7, both the test endpoints now require the PROXY_ADMIN role, making it consistent with the save endpoint. LiteLLM Unauthenticated Remote Code Execution via Starlette Host Header Validation Bypass Last week, Horizon3.ai said it chained CVE-2026-42271 with CVE-2026-48710 (CVSS score: 6.5), a " BadHost " host header validation bypass vulnerability affecting Starlette , a lightweight Asynchronous Server Gateway Interface (ASGI) framework, to completely sidestep authentication and achieve remote code execution against vulnerable LiteLLM deployments. "CVE-2026-48710 can be used to bypass the authentication mechanism entirely in LiteLLM deployments whose dependency tree includes Starlette versions ≤ 1.0.0," Horizon3.ai said . "This transforms the vulnerability into unauthenticated remote code execution with no credentials required." Successful weaponization of the exploit chain could allow attackers to run arbitrary commands on the LiteLLM host, access model provider credentials, siphon API keys and secrets stored by the proxy, move laterally into connected AI infrastructure, and even compromise downstream systems integrated with the gateway. Per Horizon3.ai, the chained vulnerability has a combined CVSS score of 10.0, making it critical in nature. There is currently no information on how CVE-2026-42271 is being exploited, the identity of the threat actor(s) behind the efforts, who are targeted, how widespread these attacks are, or if the activity has successfully compromised any instances. It's also unclear if the attacks observed in the wild are leveraging the exploit chain. Users are advised to update LiteLLM to version 1.83.7 or later and Starlette to version 1.0.1 or later. If immediate patching is not an option, the following mitigations are recommended - Block POST /mcp-rest/test/connection and POST /mcp-rest/test/tools/list at the reverse proxy or API gateway. Restrict network access to trusted segments. Rotate credentials stored by the proxy. Review logs for unusual Host header activity and subprocess execution events. The development comes a little over a month after a critical SQL injection flaw in LiteLLM ( CVE-2026-42208 , CVSS score: 9.3) came under active exploitation within 36 hours of the bug becoming public knowledge. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  API Security , artificial intelligence , CISA , Command Injection , cybersecur
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: LiteLLM Flaw CVE-2026-42271 Exploited in the Wild, Chains to Unauthenticated RCE
  - Published: 2026-06-09T06:26:14+00:00
  - Link: https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a high-severity flaw impacting BerriAI LiteLLM to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerability, tracked as CVE-2026-42271 (CVSS score: 8.7), is a command injection vulnerability that could allow any authenticated user to run arbitrary commands on the

### Cluster 62e6b1535e — score 29

- Title: CVE-2026-48558 | SimpleHelp OIDC Authentication Bypass Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-15T16:05:47+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48558/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: CVE-2026-48558

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Entra
- cve_ids: CVE-2026-48558
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: Microsoft Entra
- cve_ids: CVE-2026-48558
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-48558 is an authentication bypass vulnerability affecting SimpleHelp OIDC deployments. The flaw may allow attackers to create unauthorized Technician accounts and gain privileged access to managed endpoints.
```

#### Full body

```
CVE-2026-48558 SimpleHelp OIDC Authentication Bypass Vulnerability SimpleHelp has released patches for CVE-2026-48558, an authentication bypass vulnerability affecting deployments configured to use OpenID Connect (OIDC) authentication. The issue stems from how SimpleHelp validates identity provider assertions, allowing an unauthenticated attacker to create and authenticate as a new Technician account under certain configurations. Because Technician accounts can remotely access managed endpoints, execute scripts, and perform administrative actions, successful exploitation can lead to significant compromise of a managed environment. Horizon3.ai identified and responsibly disclosed the vulnerability to SimpleHelp. Technical Details The vulnerability affects SimpleHelp servers configured to use either generic OIDC or Azure AD OIDC authentication. An attacker can create and authenticate as a new Technician user when the following conditions exist: OIDC is enabled, and at least one OIDC authentication provider is configured on the SimpleHelp server. At least one TechnicianGroup is associated with the OIDC provider. “Allow group authenticated logins” is enabled on the TechnicianGroup. Successful exploitation allows an attacker to: Create a new Technician account. Bypass technician MFA enrollment requirements by registering their own MFA device during first login. Access managed endpoints through the SimpleHelp platform. Execute scripts and perform privileged technician actions. According to Horizon3.ai’s research, approximately 14,000 SimpleHelp servers were exposed to the internet at the time of disclosure, with roughly 7.2% of sampled servers configured to use the vulnerable OIDC authentication method. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this authentication bypass can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether unauthorized Technician account creation is possible. Patch immediately: Upgrade to a fixed SimpleHelp release and review OIDC authentication configurations. Re-run the test: Confirm the vulnerability is no longer exploitable after remediation. Indicators of Compromise Administrators should review all group-authenticated Technician accounts by navigating to: Administration → Technicians → Gear Icon → Show Group Authenticated Users Investigate any unfamiliar technician names or email addresses. Review server logs for evidence of unauthorized technician registration, including entries similar to: Registering technician login for rapidresponse-4b611bdd@horizon3.ai / (Technicians) Configuration save requested (Forged Attacker - rapidresponse-4b611bdd@horizon3.ai [(Technicians)] [New Anon]) Relevant log locations: Indicator Type Description /opt/SimpleHelp/logs/server.log Log File Primary SimpleHelp server log /opt/SimpleHelp/logs/<YYYYMMDD-HHMMSS>/server.log Log File Historical server logs Registering technician login for ... Log Entry Evidence of technician creation Configuration save requested ... [New Anon] Log Entry Potential unauthorized technician registration Affected Versions & Patch Affected: SimpleHelp deployments configured with OIDC authentication that meet the vulnerable configuration requirements described above. Patch: Upgrade to the patched versions (SimpleHelp 5.5.16 or SimpleHelp 6.0 RC2) per SimpleHelp’s security update. If patching cannot be performed immediately, restrict Technician authentication to approved source IP addresses per Horizon3.ai researchers’ recommendation: Administration → Login Security Timeline May 21, 2026 — Horizon3.ai discovered the authentication bypass vulnerability and it was assigned CVE-2026-48558. May 21, 2026 — Researchers validated exploitability in real-world
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-48558 | SimpleHelp OIDC Authentication Bypass Vulnerability
  - Published: 2026-06-15T16:05:47+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48558/
  - Summary: CVE-2026-48558 is an authentication bypass vulnerability affecting SimpleHelp OIDC deployments. The flaw may allow attackers to create unauthorized Technician accounts and gain privileged access to managed endpoints.

### Cluster ccc49ba760 — score 29

- Title: Marking Your Own Homework (Check Point Remote Access VPN IKEv1 Authentication Bypass CVE-2026-50751)
- Source: watchTowr Labs (offensive_vulnerability_research)
- Published: 2026-06-12T05:17:20+00:00
- Link: https://labs.watchtowr.com/marking-your-own-homework-check-point-remote-access-vpn-ikev1-authentication-bypass-cve-2026-50751/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-50751

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- affected_industries: government
- cve_ids: CVE-2026-50751
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_5_chatter

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-50751
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
It is yet another day in this parallel universe of security, where the devices we bolt onto the edge of our networks to keep the bad people out are, with remarkable consistency, the exact thing that let the bad people in. While we’ve seemingly had a breather from
```

#### Full body

```
It is yet another day in this parallel universe of security, where the devices we bolt onto the edge of our networks to keep the bad people out are, with remarkable consistency, the exact thing that let the bad people in. While we’ve seemingly had a breather from traditional SSL VPN exploitation season (you know, the one where every edge appliance vendor takes it in turns to have a very bad week ), it’s now time to pull up a chair and welcome ourselves back to another group therapy session. Welcome back to another watchTowr Labs blog post. On the 8th of June 2026, Check Point released hotfixes for a pair of vulnerabilities in their Mobile Access/SSL VPN, Remote Access VPN, and Spark Firewall products, specifically within the "deprecated" IKEv1 VPN code. The headline act was CVE-2026-50751, with a CVSS score of 9.3 for an Authentication Bypass. For the AI threat intel bots scraping our posts every few minutes (yes, we know), these vulnerabilities align with CWE-1337 Fun Fridays. Naturally, when the words “VPN” and “Authentication Bypass” are in the vicinity, a CISA KEV listing is not far behind - and this time is no exception. Various sources indicate that this vulnerability has been exploited in the wild since 7th May 2026 (roughly a month before anyone received a patch), and that, per Check Point, there were "a few dozen targeted organizations". Apparently, at least one incident has been linked to a Qilin ransomware affiliate. Once again, naturally, the advisory is verbose, describing the root cause as a "logic flaw in how certificates are validated during the IKEv1 key exchange". Spoiler alert: The gateway lets the client choose how carefully to check its credentials. The client chooses "don't bother". The gateway doesn't bother. That is indeed a logic flaw. As always, watchTowr clients gain industry-first access to our research days before publication to validate their exposure, accompanied by Active Defense capabilities to autonomously mitigate exposure. This research is a glimpse into the capability that powers our Preemptive Exposure Management solution, and gets organizations ahead of inevitable in-the-wild exploitation: the watchTowr Platform. What Is CVE-2026-50751, And What Is A Check Point? For the three readers who have not had the pleasure: Check Point is in the cybersecurity business, and sells (amongst other things) Security Gateways, the firewall/VPN appliances that sit at the perimeter of an enormous number of corporate and government networks. The Remote Access VPN and Mobile Access blades are what let your remote workforce dial into the corporate network from a coffee shop. The affected list is a depressing parade of Gaia versions: R80.20.X , R80.40 , R81 , R81.10 , R81.10.X , R81.20 , R82 , R82.00.X , and R82.10 . If you are out of luck and running an End-Of-Support version, you get what you deserve as a former paying customer: no hotfix at all. While this is very doom and gloom, there are a number of prerequisites to exploitation: The target accepts legacy Remote Access clients. IKEv1 is permitted (not IKEv2-only). Machine certificate authentication is not mandatory. While these sound like unlikely pre-requisites, given that "support our older clients" is a sentence uttered in every enterprise on earth, the victim pool appears to be narrowed down to.. a great many of them. Setting The Scene To fuel our analysis today, we compared the following versions following our normal ‘what the hell has changed’ process: R82.10 Jumbo Hotfix Take 19 (Vulnerable) R82.10 Jumbo Hotfix Take 19 + sk185033 hotfix (Different) "Deprecated", They Said Deprecated is one of those words that gives us warm fuzzy feelings, as it does a lot of emotional lifting. While not as explicit as many other vendors sometimes are in blaming their customers, it communicates one thing: “you probably shouldn’t have been using this function”. Just what you want to hear as Qilin says “what’s up” in a .txt on your desktop, probably. Anyway. To the di
```

#### Corroborating sources (2)

- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: Marking Your Own Homework (Check Point Remote Access VPN IKEv1 Authentication Bypass CVE-2026-50751)
  - Published: 2026-06-12T05:17:20+00:00
  - Link: https://labs.watchtowr.com/marking-your-own-homework-check-point-remote-access-vpn-ikev1-authentication-bypass-cve-2026-50751/
  - Summary: It is yet another day in this parallel universe of security, where the devices we bolt onto the edge of our networks to keep the bad people out are, with remarkable consistency, the exact thing that let the bad people in. While we’ve seemingly had a breather from
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Marking Your Own Homework (Check Point Remote Access VPN IKEv1 Authentication Bypass CVE-2026-50751) - watchTowr Labs
  - Published: 2026-06-12T05:23:23+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u3m7yj/marking_your_own_homework_check_point_remote/
  - Summary: submitted by /u/dx7r__ [link] [comments]

### Cluster c1b5a1d701 — score 27

- Title: Patch Tuesday - June 2026
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-09T21:04:53+00:00
- Link: https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- affected_products: GitHub
- tools_used: Linux kernel
- cve_ids: CVE-2026-33825, CVE-2026-41091, CVE-2026-45498, CVE-2026-45585
- urgency_signals: actively_exploited, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure, active_exploitation
- affected_products: GitHub
- tools_used: Linux kernel
- cve_ids: CVE-2026-33825, CVE-2026-45585, CVE-2026-45498, CVE-2026-41091
- urgency_signals: actively_exploited, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Microsoft is publishing 200 vulnerabilities on June 2026 Patch Tuesday . Microsoft is not aware of exploitation in the wild for any of these vulnerabilities, and is aware of public disclosure for three. This is similar to last month’s Patch Tuesday, however several of last month’s vulnerabilities ended up on CISA KEV in the days following their publication. So far this month, Microsoft has provided patches to address 360 browser vulnerabilities, which is an order of magnitude more than has been typical in any given month over the past few years. As usual, browser vulns are not included in the Patch Tuesday count above. Indeed, the vast, and presumably sustained, uptick in the number of browser vulnerabilities has led to Microsoft no longer enumerating Chromium CVEs in the Security Update Guide. Other vulnerability categories, especially Linux kernel vulnerabilities, are seeing a similar increase in AI-assisted vulnerability reports. What's the opposite of coordinated disclosure? In rec
```

#### Full body

```
Back to Blog Exposure Management Patch Tuesday - June 2026 Adam Barnett Jun 9, 2026 | Last updated on Jun 9, 2026 | 30 min read Microsoft is publishing 200 vulnerabilities on June 2026 Patch Tuesday . Microsoft is not aware of exploitation in the wild for any of these vulnerabilities, and is aware of public disclosure for three. This is similar to last month’s Patch Tuesday, however several of last month’s vulnerabilities ended up on CISA KEV in the days following their publication. So far this month, Microsoft has provided patches to address 360 browser vulnerabilities, which is an order of magnitude more than has been typical in any given month over the past few years. As usual, browser vulns are not included in the Patch Tuesday count above. Indeed, the vast, and presumably sustained, uptick in the number of browser vulnerabilities has led to Microsoft no longer enumerating Chromium CVEs in the Security Update Guide. Other vulnerability categories, especially Linux kernel vulnerabilities, are seeing a similar increase in AI-assisted vulnerability reports. What's the opposite of coordinated disclosure? In recent weeks, an independent vulnerability researcher going by the pseudonym Nightmare Eclipse has attracted significant attention by publishing details of six Microsoft vulnerabilities, including elevation of privilege vulnerabilities in Defender, and a Secure Boot disk encryption bypass. The researcher provided full proof-of-concept code for some, and provided significant-but-incomplete detail around the path to exploitation for others. Microsoft has confirmed that these disclosures were not coordinated, and it is clear that the relationship between this researcher and Microsoft is less than cordial. Two of the disclosures emerged in the hours after last month’s Patch Tuesday, which provides maximum visibility, while limiting Microsoft’s ability to respond without out-of-cycle patches. At time of writing, Microsoft has provided mitigation advice and patches for CVE-2026-33825 , CVE-2026-45585 , CVE-2026-45498 , and CVE-2026-41091 , leaving only two elevation of privilege vulnerabilities unpatched, known as MiniPlasma and GreenPlasma. However, a recent blog post by Nightmare Eclipse with the title “7” has been widely interpreted to mean that there is at least one more vulnerability to come. The post contained no content other than an image of Albert Vesker, a character from the Resident Evil video game series who formerly worked as a researcher for a technology corporation before going rogue. Any inference around the possible meaning of the image is left as an exercise for the reader. Given the timing of last month’s disclosures in the hours following Patch Tuesday, a further high-friction disclosure today would perhaps be unsurprising. Indeed, a new blog post and a new GitHub account from the same researcher have emerged in the hours following Microsoft’s publication of the June 2026 Patch Tuesday updates. The apparent seventh disclosure is nicknamed RoguePlanet, and appears to describe another elevation of privilege to SYSTEM in Defender. It is not at all difficult to understand why Microsoft and many blue team practitioners are deeply alarmed by the partial or even full disclosure of proof-of-concept code for an ongoing series of vulnerabilities affecting fully-patched Windows systems. However, multiple leading voices in the broader vulnerability disclosure community have expressed concern that Microsoft’s invocation of the Digital Crimes Unit in a May 27, 2026 blog post may yet prove counterproductive, especially if it causes other researchers to back away from mutually beneficial engagements with MSRC. A few days later, MSRC issued a further statement clarifying that they have no intention of pursuing action against security researchers, but only those who break the law or engage in malicious activity causing real harm. For now, one safe conclusion is that this unusually sensational Microsoft vulnerability management
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Patch Tuesday - June 2026
  - Published: 2026-06-09T21:04:53+00:00
  - Link: https://www.rapid7.com/blog/post/em-patch-tuesday-june-2026
  - Summary: Microsoft is publishing 200 vulnerabilities on June 2026 Patch Tuesday . Microsoft is not aware of exploitation in the wild for any of these vulnerabilities, and is aware of public disclosure for three. This is similar to last month’s Patch Tuesday, however several of last month’s vulnerabilities ended up on CISA KEV in the days following their publication. So far this month, Microsoft has provided patches to address 360 browser vulnerabilities, which is an order of magnitude more than has been typical in any given month over the past few years. As usual, browser vulns are not included in the Patch Tuesday count above. Indeed, the vast, and presumably sustained, uptick in the number of browser vulnerabilities has led to Microsoft no longer enumerating Chromium CVEs in the Security Update Guide. Other vulnerability categories, especially Linux kernel vulnerabilities, are seeing a similar increase in AI-assisted vulnerability reports. What's the opposite of coordinated disclosure? In rec

### Cluster 886a4df09d — score 27

- Title: Factoring "short-sleeve" RSA keys with polynomials
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-06-12T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
What happens when the bits of an RSA private key are heavily biased toward 0 instead of being randomly generated? The public key’s bits could be biased enough for us to detect these incorrectly generated keys in the wild. Together with Hanno Böck of the badkeys project, we found hundreds of unique keys that not only have this property, but can be quickly factored. We also found the bug that led to many of these keys and analyzed historical data to track the issue over time. Surprisingly, the pattern of 0 bits is often highly structured, allowing us to develop a powerful polynomial-based cryptanalytic technique that exploits the pattern. Figure 1: Two patterns of RSA moduli with repeated blocks of 0 bits seen in real-world examples. These “short-sleeve” keys, named for how the 0 bits don’t fully cover the limbs of the big integers, largely fell into two patterns. Pattern 1 remains unexplained, but we traced pattern 2 to a type mismatch in big-integer code from old versions of the Comple
```

#### Full body

```
Page content What happens when the bits of an RSA private key are heavily biased toward 0 instead of being randomly generated? The public key’s bits could be biased enough for us to detect these incorrectly generated keys in the wild. Together with Hanno Böck of the badkeys project, we found hundreds of unique keys that not only have this property, but can be quickly factored. We also found the bug that led to many of these keys and analyzed historical data to track the issue over time. Surprisingly, the pattern of 0 bits is often highly structured, allowing us to develop a powerful polynomial-based cryptanalytic technique that exploits the pattern. Figure 1: Two patterns of RSA moduli with repeated blocks of 0 bits seen in real-world examples. These “short-sleeve” keys, named for how the 0 bits don’t fully cover the limbs of the big integers, largely fell into two patterns. Pattern 1 remains unexplained, but we traced pattern 2 to a type mismatch in big-integer code from old versions of the CompleteFTP file transfer software. The CompleteFTP bug also generated vulnerable short-sleeve DSA keys, and we recovered 603 unique RSA private keys and 74 DSA keys from internet scans. If you used CompleteFTP to generate host keys between December 2016 and December 2023, CompleteFTP has released a tool to check whether your keys need to be regenerated. How we found the weak keys The badkeys project is an open-source service that checks public keys for known vulnerabilities. While developing this tool, Hanno collected a massive number of real-world keys from public sources, including Certificate Transparency logs, internet-wide TLS and SSH scans, PGP keys, and many others. By searching this dataset for unexpectedly sparse RSA moduli, we uncovered a large number of keys in the wild with the patterns in Figure 1. Both patterns include several regularly spaced blocks of all zeros interleaved with seemingly random data. Pattern 1 appears in CT logs for certificates issued to several large organizations, including Yahoo and Verizon , and on some devices running NetApp software. Fortunately, these certificates have already expired, but we still shared our findings with these companies. We wanted to learn more about which product could be responsible for generating these keys, but we did not hear back. Pattern 2 appears on SSH hosts running the CompleteFTP software from EnterpriseDT. The underlying vulnerability affects RSA keys generated using versions 10.0.0–12.0.0 (Dec 2016–Mar 2019) and DSA keys generated with v10.0.0–23.0.4 (Dec 2016–Dec 2023). These vulnerabilities affect a small minority of hosts on the internet, but the more interesting takeaway is that independent cryptographic implementations failed in similar ways. More implementations may include the same bugs, and so it’s worth tailoring cryptanalytic algorithms for this particular type of failure. Factoring with polynomials Cryptographic algorithms often need integers hundreds or thousands of bits long, and they represent these “big integers” using an array of smaller machine-sized values, called limbs . If we interpret pattern 1 as a sequence of 128-bit limbs, or 32-bit limbs in pattern 2, the repeated blocks of zeros correspond to a single block of zeros in each limb. Only a small contiguous subset of the limb is filled with random bits, and the rest of the limb is uncovered, hence the nickname “short-sleeve keys.” By exploiting this mathematical structure in the limbs of these moduli, we replace the hard problem of factoring integers with the easy problem of factoring polynomials. That is, we take the modulus $n$ with unknown factors $p$ and $q$, express it as a polynomial $f_n(x)$ with small coefficients, factor $f_n(x)$ into $f_p(x)$ and $f_q(x)$, and convert these factors into $p$ and $q$. The technique of converting between integers and polynomials is common, including doing fast polynomial multiplication , but sadly, few resources describe how to use it for fast integer fac
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: Factoring "short-sleeve" RSA keys with polynomials
  - Published: 2026-06-12T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/
  - Summary: What happens when the bits of an RSA private key are heavily biased toward 0 instead of being randomly generated? The public key’s bits could be biased enough for us to detect these incorrectly generated keys in the wild. Together with Hanno Böck of the badkeys project, we found hundreds of unique keys that not only have this property, but can be quickly factored. We also found the bug that led to many of these keys and analyzed historical data to track the issue over time. Surprisingly, the pattern of 0 bits is often highly structured, allowing us to develop a powerful polynomial-based cryptanalytic technique that exploits the pattern. Figure 1: Two patterns of RSA moduli with repeated blocks of 0 bits seen in real-world examples. These “short-sleeve” keys, named for how the 0 bits don’t fully cover the limbs of the big integers, largely fell into two patterns. Pattern 1 remains unexplained, but we traced pattern 2 to a type mismatch in big-integer code from old versions of the Comple

### Cluster 2974abda18 — score 25

- Title: Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257
- Source: Unit 42 (threat_research_primary)
- Published: 2026-06-09T14:05:42+00:00
- Link: https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-0257, Palo Alto Networks

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Microsoft Windows, Palo Alto Networks
- cve_ids: CVE-2026-0257
- urgency_signals: actively_exploited, poc_available
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Palo Alto Networks, Microsoft Windows
- cve_ids: CVE-2026-0257
- urgency_signals: actively_exploited, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
We include indicators of activity and mitigations for PAN-OS vulnerability CVE-2026-0257. The post Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257 appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center High Profile Threats Vulnerabilities Vulnerabilities Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257 3 min read Related Products Advanced URL Filtering Cortex Cortex Xpanse GlobalProtect Next-Generation Firewall By: Andy Piazza Unit 42 Published: June 9, 2026 Categories: High Profile Threats Vulnerabilities Tags: CVE-2026-0257 Vulnerability Share Palo Alto Networks Unit 42 has observed active exploitation of PAN-OS vulnerability CVE-2026-0257 by an unidentified threat actor attempting to access GlobalProtect. This security flaw involves an authentication bypass in the portal and gateway components of vulnerable versions of PAN-OS ® software, which could allow unauthorized attackers to circumvent security controls and initiate VPN connections. This CVE was added to the Known Exploited Vulnerability (KEV) catalog on May 29. No post-access behavior or lateral movement has been identified as of this time. Only a small portion of the probed devices actually established VPN sessions, resulting in gateway-connected events. We advise organizations to proactively hunt for the indicators of the activity specified in this report and activate incident response protocols for any successful gateway-connected events linked to these indicators. Additionally, we strongly recommend reviewing the security advisory for CVE-2026-0257 , following the available workarounds and mitigations or upgrading to a version that includes a fix for this issue. For pre-Proof of Concept release (May 29, 2026) activities, search for these IP addresses in GlobalProtect logs to look for successful login connection: 23.128.228[.]6 104.207.144[.]154 146.19.216[.]119 146.19.216[.]120 146.19.216[.]125 179.43.172[.]213 185.195.232[.]139 198.12.106[.]60 202.144.192[.]47 Search GlobalProtect logs for successful gateway-connected events from any IP address using suspicious host IDs or device names, including but not limited to: aa:bb:cc:dd:ee:ff 00:11:22:33:44:55 WINDOWS-LAPTOP-001 DESKTOP-GP01 GP-CLIENT As part of post-PoC release monitoring, search GlobalProtect logs for successful gateway-connected events matching the following hard-coded client configuration values from the PoC code. endpoint_os_version : Microsoft Windows 10 Pro 64-bit source_user_info.domain : empty We encourage organizations to consult the official Palo Alto Networks Security Advisory for additional details about the vulnerability, impacted products and configuration guidance. We also recommend reading Rapid7 ’s technical analysis about the exploitation activity they observed in the wild. Palo Alto Networks Cortex Xpanse is able to identify publicly exposed PAN-OS gateways and GlobalProtect portals. Palo Alto Networks has shared our findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the Cyber Threat Alliance . We will update this threat brief as more relevant information becomes available. The products listed below can help protect PANW customers against exploits targeting CVE-2026-0257. Palo Alto Networks Product Protections for PAN-OS CVE-2026-0257 Palo Alto Networks customers can leverage a variety of product protections and updates to identify and defend against this threat. If you think you might have been compromised or have an urgent matter, get in touch with the Unit 42 Incident Response team or call: North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42) UK: +44.20.3743.3660 Europe and Middle East: +31.20.299.3130 Asia: +65.6983.8730 Japan: +81.50.1790.0200 Australia: +61.2.4062.7950 India: 000 800 050 45107 South Korea: +82.080.467.8774 Cloud-Delivered Security Services for the Next-Generation Firewall Advanced URL Filtering can identify known IP addresses associated with this activity as malicious. Cortex AgentiX Security analysts can use natural language to prompt the Cortex AgentiX Threat
```

#### Corroborating sources (2)

- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257
  - Published: 2026-06-09T14:05:42+00:00
  - Link: https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
  - Summary: We include indicators of activity and mitigations for PAN-OS vulnerability CVE-2026-0257. The post Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257 appeared first on Unit 42 .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw
  - Published: 2026-06-15T06:17:32+00:00
  - Link: https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html
  - Summary: Palo Alto Networks has revealed that it has observed "active exploitation" of a recently disclosed PAN-OS vulnerability by an unknown threat actor to obtain unauthorized access to GlobalProtect portals. The vulnerability in question is CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway components of PAN-OS software that could be exploited by bad

### Cluster b9c17f29cd — score 24

- Title: Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-09T11:58:49+00:00
- Link: https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-11645

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, phishing_social_eng, zero_day
- affected_products: Anthropic/Claude, Ivanti, Microsoft Defender
- cve_ids: CVE-2026-11645, CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, zero_day, active_exploitation
- affected_products: Anthropic/Claude, Ivanti, Microsoft Defender
- cve_ids: CVE-2026-11645, CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Google has released security updates to address 74 vulnerabilities, including one that has come under active exploitation in the wild. The high-severity vulnerability, tracked as CVE-2026-11645 (CVSS score: 8.8), has been described as an out-of-bounds memory access in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds read and write in V8 in Google Chrome prior to 149.0.7827.103
```

#### Full body

```
Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now  Ravie Lakshmanan  Jun 09, 2026 Vulnerability / Browser Security Google has released security updates to address 74 vulnerabilities, including one that has come under active exploitation in the wild. The high-severity vulnerability, tracked as CVE-2026-11645 (CVSS score: 8.8), has been described as an out-of-bounds memory access in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds read and write in V8 in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page," reads a description of the flaw in the NIST's National Vulnerability Database (NVD). A security researcher named "303f06e3" has been credited with discovering and reporting the flaw on April 27, 2026. The researcher has been awarded a bug bounty of $55,000 for responsible disclosure. As is customary in these cases, Google acknowledged that an "exploit for CVE-2026-11645 exists in the wild," but stopped short of sharing additional specifics to ensure that a majority of the users are updated with a fix and to prevent further exploitation. With the latest development, Google has addressed a total of five actively exploited Chrome zero-days since the start of the year. This includes CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, and CVE-2026-5281. For optimal protection, users are advised to update their Chrome browser to versions 149.0.7827.102/.103 for Windows and Apple macOS, and 149.0.7827.102 for Linux. To make sure the latest updates are installed, users can navigate to More > Help > About Google Chrome and select Relaunch. Users of other Chromium-based browsers, such as Microsoft Edge, Brave, Opera, and Vivaldi, are also advised to apply the fixes as and when they become available. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  browser security , Code Execution , cybersecurity , Google Chrome , V8 , Vulnerability , Zero-Day ⚡ Top Stories This Week Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities Cybersecurity Stars Awards 2026: Winners Announced Across 95 Categories ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories New GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files Agentjacking Attack Tricks AI Coding Agents Into Running Malicious Code China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication U.S. Orders Anthropic to Suspend Fable 5 and Mythos 5 Access for Foreign Nationals Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit ⭐ Featured Resources Get the 2026 Guide to Govern and Secure Enterprise AI Agents at Scale [Watch Demo] See Which Security Gaps Attackers Could Exploit First AI Can’t Stop Every Attack. Learn How Zero Trust Can Block What’s Unknown Have You Outgrown Your MDR? 7 Warning Signs Every CISO Should Check
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now
  - Published: 2026-06-09T11:58:49+00:00
  - Link: https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html
  - Summary: Google has released security updates to address 74 vulnerabilities, including one that has come under active exploitation in the wild. The high-severity vulnerability, tracked as CVE-2026-11645 (CVSS score: 8.8), has been described as an out-of-bounds memory access in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds read and write in V8 in Google Chrome prior to 149.0.7827.103
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Google Releases Patch for Chrome Vulnerability Exploited in the Wild
  - Published: 2026-06-09T10:15:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/google-patch-chrome-vulnerability/
  - Summary: The flaw, CVE-2026-11645, can allow a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page

### Cluster 2110e56ddb — score 22

- Title: Critical PhpSpreadsheet RCE Patch Bypass Puts Millions at Risk
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-06-11T17:02:11+00:00
- Link: https://orca.security/resources/blog/cve-2026-45034-phpspreadsheet-rce-patch-bypass/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-45034

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- cve_ids: CVE-2026-34084, CVE-2026-45034
- urgency_signals: actively_exploited, critical_cvss, poc_available
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- cve_ids: CVE-2026-45034, CVE-2026-34084
- urgency_signals: actively_exploited, poc_available, critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Executive Summary A critical vulnerability (CVE-2026-45034, CVSS 9.8) was disclosed affecting PhpSpreadsheet, the widely-used PHP library with over 312 million downloads, allowing attackers to achieve remote code execution via a bypass of the previous wrapper protection mechanism. Due to the potential for full server compromise and data exposure, immediate patching is required. About the Vulnerability: […]
```

#### Full body

```
Executive Summary A critical vulnerability ( CVE-2026-45034 , CVSS 9.8) was disclosed affecting PhpSpreadsheet, the widely-used PHP library with over 312 million downloads, allowing attackers to achieve remote code execution via a bypass of the previous wrapper protection mechanism. Due to the potential for full server compromise and data exposure, immediate patching is required. About the Vulnerability: CVE-2026-45034 The issue originates from the File::prohibitWrappers() function introduced to fix CVE-2026-34084 , where a quirk in PHP’s parse_url() function leads to a complete bypass of stream wrapper detection. When a path contains three or more slashes after the scheme (e.g., phar:///path/to/exploit.phar/dummy.csv), parse_url() returns false instead of the expected scheme string. This causes the is_string($scheme) check to be skipped entirely, while PHP’s stream layer still recognizes the path as a valid phar wrapper. By sending a specially crafted filename containing triple slashes to IOFactory::load(), attackers can trigger automatic phar metadata deserialization on PHP 7.x, potentially gaining full remote code execution. On PHP 8.x, the same technique yields a file read primitive, with RCE restored if the application later invokes Phar::getMetadata(). No authentication is required to exploit this issue when the filename argument is user-controlled. The following versions are affected: phpoffice/phpspreadsheet, all 1.x versions through 1.30.4 These components are used by thousands of PHP applications and frameworks that rely on PhpSpreadsheet for reading and writing Excel, CSV, and other spreadsheet formats, particularly when file upload or import functionality is enabled. Other frameworks or services relying on PhpSpreadsheet’s IOFactory::load() with user-supplied filenames may also be impacted. Risk Impact At the time of writing, a working proof-of-concept and full exploit chain (exploit.phar) are publicly available, disclosed by researcher @everping . While no confirmed exploitation in the wild has been reported yet, the public availability of the PoC significantly increases the likelihood of active exploitation. Organizations that previously patched against CVE-2026-34084 should be aware that the earlier patch was proven incomplete. Successful exploitation could allow attackers to execute arbitrary code on the server, read sensitive files from the filesystem, and potentially pivot to compromise additional infrastructure, leading to service disruption, data exposure, or full infrastructure compromise. Mitigation Recommendations Upgrade to the following patched version immediately: PhpSpreadsheet 1.30.5, which addresses this bypass Additionally: Organizations that previously patched against CVE-2026-34084 should verify they have also applied this latest fix, as the earlier patch was proven incomplete Replace parse_url()-based wrapper detection with string containment checks (such as str_contains($filename, ‘://’)) in any custom validation code Ensure that IOFactory::load() never receives unsanitized user-controlled filenames How can Orca help? Orca enables customers to quickly identify assets running vulnerable versions of PhpSpreadsheet , understand their exposure in context, including internet accessibility, runtime reachability , and asset criticality, and prioritize remediation based on real risk rather than CVSS alone. Orca’s platform highlights affected assets directly in the newItem view, helping security teams focus on the most critical remediation paths first. Related articles Cloud Security Learning What to Look for in Container Security Tools Jun 15, 2026 Cloud Security Learning Cloud Application Security Best Practices for DevSecOps Jun 12, 2026 Cloud Security Learning Cloud Security Tools: 10 Types Explained for Teams Jun 12, 2026 Stay in the loop Keep up to date with everything you need to know about cloud security and our latest research By submitting my email address I agree to the use of my personal da
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Critical PhpSpreadsheet RCE Patch Bypass Puts Millions at Risk
  - Published: 2026-06-11T17:02:11+00:00
  - Link: https://orca.security/resources/blog/cve-2026-45034-phpspreadsheet-rce-patch-bypass/
  - Summary: Executive Summary A critical vulnerability (CVE-2026-45034, CVSS 9.8) was disclosed affecting PhpSpreadsheet, the widely-used PHP library with over 312 million downloads, allowing attackers to achieve remote code execution via a bypass of the previous wrapper protection mechanism. Due to the potential for full server compromise and data exposure, immediate patching is required. About the Vulnerability: […]

### Cluster d1241978fa — score 22

- Title: 15th June – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-06-15T13:40:44+00:00
- Link: https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 5
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters
- affected_industries: education, government, healthcare
- affected_products: Anthropic/Claude, GitHub, Microsoft BitLocker, Salesforce, npm
- cve_ids: CVE-2026-27022, CVE-2026-35273, CVE-2026-41091, CVE-2026-45657, CVE-2026-50751
- urgency_signals: actively_exploited, no_patch_yet, poc_available, zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, data_breach, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: healthcare, education
- affected_products: Microsoft BitLocker, Anthropic/Claude, GitHub
- cve_ids: CVE-2026-35273, CVE-2026-27022, CVE-2026-50751, CVE-2026-45657, CVE-2026-41091
- urgency_signals: actively_exploited, zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 15th June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES The University of Nottingham, a UK research university, has suffered a data breach after ShinyHunters accessed its student records system. The incident affected about 454,600 current and former students and exposed contact details, […] The post 15th June – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 15th June – Threat Intelligence Report June 15, 2026 https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 15th June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES The University of Nottingham, a UK research university, has suffered a data breach after ShinyHunters accessed its student records system. The incident affected about 454,600 current and former students and exposed contact details, passport numbers, enrollment information, and fee payment records later appeared online. According to analysts, this breach is part of a larger wave of attacks targeting more than 100 organizations by ShinyHunters, exploiting CVE-2026-35273, a critical zero-day vulnerability in Oracle PeopleSoft that allows remote code execution. Check Point IPS provides protection against this threat (Oracle PeopleSoft Enterprise PeopleTools Server-Side Request Forgery (CVE-2026-35273)) Mackay Sugar, Australia’s second-largest sugar producer, has been hit by a cyberattack that disrupted operations and shut down its Farleigh and Racecourse mills in Queensland. The company instructed growers to stop harvesting and suspended cane haulage while temporary measures were deployed to maintain essential operations. Danish pharmaceutical giant Novo Nordisk has disclosed a breach after attackers accessed internal IT systems and copied pseudonymized clinical trial data from research systems. The exposed information included patient IDs, trial participation details, limited health data, and some healthcare professionals’ contact information. AI THREATS Check Point Research has demonstrated exploitable flaws in LangGraph, an open-source framework for stateful AI agents. Researchers chained SQL injection and unsafe deserialization issues to achieve remote code execution, with patches issued for SQLite, core, and Redis checkpointer components in affected deployments. Check Point IPS provides protection against this threat (LangChain LangGraph SQL Injection (CVE-2026-27022)) Researchers highlighted a China-based phishing-as-a-service network, Outsider, that allegedly used Gemini to generate fake websites and support SMS phishing campaigns. Google filed a lawsuit after linking the operation to thousands of phishing sites, more than 1.5 million URLs, and large-scale victim targeting. Researchers warned that prompt-injection attacks against Anthropic’s Claude Code GitHub Action could leak CI/CD workflow secrets. Malicious issue or pull request text can instruct the agent to read environment variables and expose API keys, enabling workflow abuse and impersonation inside software repositories. VULNERABILITIES AND PATCHES Check Point Research has identified active exploitation of CVE-2026-50751, a critical authentication bypass vulnerability affecting Check Point Remote Access VPN and Mobile Access deployments configured to use the deprecated IKEv1 key exchange protocol. Attacks began in May and increased in early June, affecting a limited number of organizations, with one case tied to Qilin ransomware activity. Check Point IPS provides protection against this threat (IKEv1 Remote Access Authentication Bypass PoC Exploit (CVE-2026-50751)) Microsoft released its largest Patch Tuesday update to date, addressing more than 200 Windows and Defender vulnerabilities amid an AI-driven surge in vulnerability discovery. The fixes include CVE-2026-45657, a critical Windows flaw with a CVSS score of 9.8 that could enable network-based propagation, CVE-2026-41091, which has been actively exploited to gain full system control, and CVE-2026-50507, a BitLocker bypass vulnerability. Veeam has released security updates to fix a critical flaw affecting Backup & Replication. The vulnerability allows an authenticated domain user to execute code remotely on a domain-joined backup server, exposing sensitive backup infrast
```

#### Corroborating sources (5)

- **Check Point Research** (threat_research_primary)
  - Title: 15th June – Threat Intelligence Report
  - Published: 2026-06-15T13:40:44+00:00
  - Link: https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 15th June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES The University of Nottingham, a UK research university, has suffered a data breach after ShinyHunters accessed its student records system. The incident affected about 454,600 current and former students and exposed contact details, […] The post 15th June – Threat Intelligence Report appeared first on Check Point Research .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Council of Europe investigates ShinyHunters data breach claims
  - Published: 2026-06-15T16:37:11+00:00
  - Link: https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/
  - Summary: The Council of Europe, the continent's oldest intergovernmental body, is probing claims of a data breach made by the ShinyHunters extortion group over the weekend. [...]
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: ShinyHunters is actively extorting universities after exploiting an unpatched Oracle flaw
  - Published: 2026-06-12T16:12:34+00:00
  - Link: https://cyberscoop.com/oracle-peoplesoft-zero-day-vulnerability-shinyhunters-extortion/
  - Summary: Oracle still hasn't patched the vulnerability the group has been using in its attacks since late May. The post ShinyHunters is actively extorting universities after exploiting an unpatched Oracle flaw appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: ShinyHunters Uses Oracle Zero-Day to Rampage Higher Ed
  - Published: 2026-06-12T20:26:32+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/shinyhunters-oracle-zero-day-higher-ed
  - Summary: A major bug in Oracle's ERP software disproportionately affected American universities, and hackers have capitalized by stealing gobs of data.
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: CISA tightens patching rules amid bug deluge
  - Published: 2026-06-12T04:49:28+00:00
  - Link: https://risky.biz/RBNEWS576/
  - Summary: CISA changes federal patching rules due to AI, a House Republican was hacked by Russia, ShinyHunters go on an Oracle hacking spree, and npm will block auto-run install scripts by default.

### Cluster e90454cc0b — score 22

- Title: Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-06-15T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: UNC6508

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- actor_attribution: UNC6508
- affected_industries: healthcare
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- actor_attribution: UNC6508
- affected_industries: healthcare
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Patrick Whitsell, John McGuiness Google Threat Intelligence Group (GTIG) has identified a sophisticated campaign attributed to UNC6508, a People's Republic of China (PRC)-nexus threat actor, targeting institutions in the North American academic, medical, and military research community. While remaining undetected for over a year, the threat actor compromised externally facing web applications, deployed bespoke malware, pivoted to sensitive internal systems, and abused enterprise administrative tools for covert data exfiltration. The threat actor had broad collection aspirations, including sensitive defense intelligence related to national security, Indo-Pacific command operations, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, and medical research. GTIG disrupted the malicious infrastructure associated with this threat actor. Working with Mandiant Consulting, we notified the affected organizations upon detection and offered our assistance with
```

#### Full body

```
Threat Intelligence Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research June 15, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Written by: Patrick Whitsell, John McGuiness Google Threat Intelligence Group (GTIG) has identified a sophisticated campaign attributed to UNC6508, a People's Republic of China (PRC)-nexus threat actor, targeting institutions in the North American academic, medical, and military research community. While remaining undetected for over a year, the threat actor compromised externally facing web applications, deployed bespoke malware, pivoted to sensitive internal systems, and abused enterprise administrative tools for covert data exfiltration. The threat actor had broad collection aspirations, including sensitive defense intelligence related to national security, Indo-Pacific command operations, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, and medical research. GTIG disrupted the malicious infrastructure associated with this threat actor. Working with Mandiant Consulting, we notified the affected organizations upon detection and offered our assistance with remediation. We have updated Google Security Operations (SecOps) with relevant intelligence, enabling defenders to identify indicators of compromise (IOCs) within their networks. We encourage all users and customers to follow recommended best practices for third-party Identity Providers (IdP) and ensure 2-Step Verification (2SV) is enabled across all accounts. Campaign Overview The campaign targeted a diverse set of national, state, and private medical entities. These organizations comprise world-renowned clinical providers, premier academic centers, North American military health institutions, professional advocacy groups, and health regulatory bodies. Their research areas span a broad spectrum of modern medicine, from molecular discovery and clinical drug trials to state-level public health policy and military readiness. They employ thousands of people with a combined research budget in the billions of dollars. The earliest known compromise occurred in September 2023, after which GTIG observed a consistent operational pattern. The threat actor exploited externally facing REDCap (Research Electronic Data Capture) servers and deployed custom malware named INFINITERED to capture legitimate REDCap login credentials. Then, after remaining undetected for more than a year, UNC6508 used the captured credentials to access the victim’s internal network. The threat actor was also observed using the novel technique of manipulating domain content compliance rules for data exfiltration. Lastly, UNC6508 used sophisticated operations security (OpSec) techniques to conceal and obfuscate their activity. GTIG collaborated closely with Mandiant Consulting, the FLARE team, and Workspace Security on this effort to combine our threat intelligence, incident response, and reverse engineering expertise across Google Cloud. This enabled us to develop a complete picture of the attack lifecycle from initial compromise to complete mission. GTIG also extends thanks to the affected organizations for their cooperation and the valuable post-exploitation insights they shared. Prevention, Detection, and Remediation GTIG recommends defenders implement the following security measures, across all Cloud enterprise platforms, to mitigate this threat: Secure Admin Accounts : Enforce phishing-resistant 2-Step Verification (2SV) for enterprise administrator accounts, including through third-party Identity Providers. Advanced Protection : Consider enrolling highly sensitive accounts in our Advanced Protection Program for additional safeguards against malware and phishing attacks. Prevent Cookie Theft : Enforce Device Bound Session Credentials (DBSC) with CAA for high
```

#### Corroborating sources (3)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research
  - Published: 2026-06-15T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research/
  - Summary: Written by: Patrick Whitsell, John McGuiness Google Threat Intelligence Group (GTIG) has identified a sophisticated campaign attributed to UNC6508, a People's Republic of China (PRC)-nexus threat actor, targeting institutions in the North American academic, medical, and military research community. While remaining undetected for over a year, the threat actor compromised externally facing web applications, deployed bespoke malware, pivoted to sensitive internal systems, and abused enterprise administrative tools for covert data exfiltration. The threat actor had broad collection aspirations, including sensitive defense intelligence related to national security, Indo-Pacific command operations, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, and medical research. GTIG disrupted the malicious infrastructure associated with this threat actor. Working with Mandiant Consulting, we notified the affected organizations upon detection and offered our assistance with
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research
  - Published: 2026-06-15T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research/
  - Summary: Written by: Patrick Whitsell, John McGuiness Google Threat Intelligence Group (GTIG) has identified a sophisticated campaign attributed to UNC6508, a People's Republic of China (PRC)-nexus threat actor, targeting institutions in the North American academic, medical, and military research community. While remaining undetected for over a year, the threat actor compromised externally facing web applications, deployed bespoke malware, pivoted to sensitive internal systems, and abused enterprise administrative tools for covert data exfiltration. The threat actor had broad collection aspirations, including sensitive defense intelligence related to national security, Indo-Pacific command operations, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, and medical research. GTIG disrupted the malicious infrastructure associated with this threat actor. Working with Mandiant Consulting, we notified the affected organizations upon detection and offered our assistance with
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Chinese Hackers Target Medical, Military, and AI Research in North America
  - Published: 2026-06-15T14:07:45+00:00
  - Link: https://www.securityweek.com/chinese-hackers-target-medical-military-and-ai-research-in-north-america/
  - Summary: Google’s Threat Intelligence Group has been tracking the cyberespionage group as UNC6508 since early 2025. The post Chinese Hackers Target Medical, Military, and AI Research in North America appeared first on SecurityWeek .

### Cluster 8946d31fb3 — score 21

- Title: The First AI State-Sponsored Attack: What It Means for Defenders
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-10T07:50:48+00:00
- Link: https://horizon3.ai/intelligence/blogs/first-ai-state-sponsored-attack-threat-model/
- Fetch status: ok
- Member count: 8
- Corroborating source count: 6
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, supply_chain
- affected_industries: critical_infrastructure, financial_services, government, manufacturing_industrial
- affected_products: Anthropic/Claude, GitHub
- content_type: incident_report, news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Anthropic/Claude, GitHub
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
In November 2025, Anthropic disclosed the first AI-orchestrated state-sponsored cyberattack. Here's what GTG-1002 actually changes for security teams.
```

#### Full body

```
The First AI State-Sponsored Attack: What It Means for Defenders Horizon3.ai June 10, 2026 Blogs On November 13, 2025, Anthropic disclosed what it called the first documented case of a large-scale cyberattack executed largely without human intervention. A Chinese state-sponsored group it tracks as GTG-1002 had manipulated its Claude model into running the majority of an espionage campaign against roughly 30 organizations — autonomously, with human operators stepping in only at a handful of decision points. The headline traveled fast. What most of the coverage skipped is the part that matters to defenders: what the AI actually did, how the attackers pulled it off, and why the answer doesn’t change your defensive priorities so much as compress the timeline for acting on them. This is a measured read of what the first AI-orchestrated state-sponsored attack does and doesn’t change, and what security teams should do about it now. What Was the First AI-Orchestrated State-Sponsored Attack? According to Anthropic’s report , the company detected the operation in mid-September 2025 and attributed it with high confidence to a Chinese state-sponsored group designated GTG-1002. The campaign targeted around 30 entities including large technology firms, financial institutions, chemical manufacturers, and government agencies, and a handful of intrusions succeeded before the activity was disrupted. The mechanics are the interesting part. The attackers didn’t ask the model for advice or for fragments of malware. They built an orchestration framework on top of the Model Context Protocol (MCP) that decomposed the intrusion into a sequence of small, individually benign-looking tasks, and they bypassed the model’s safety controls by social-engineering it into believing it was a cybersecurity firm performing authorized defensive testing. Under that framing, the AI handled an estimated 80–90% of the tactical work across the full kill chain: reconnaissance, vulnerability discovery, exploitation, lateral movement, credential harvesting, and data exfiltration. The pattern it executed was not exotic. In a closely related documented chain, an AI agent discovered a Server-Side Request Forgery (SSRF) vulnerability, stole cloud credentials, compromised a database, then pivoted through misconfigured GitHub Actions to reach remote code execution and repository takeover. No single critical CVE was required. The compromise came from connecting ordinary weaknesses in the right order. The novelty wasn’t the techniques. It was that an AI executed nearly the entire attack lifecycle with humans only at the decision gates. How Significant Was It, Really? It’s worth being honest about the controversy, because your board may have already read about it. Anthropic’s disclosure drew immediate skepticism from parts of the security community . Researchers questioned the absence of published indicators of compromise, argued the 80–90% autonomy figure was overstated, and noted that the operational impact was likely limited because existing detections already catch the open-source tooling involved. At least one prominent AI researcher dismissed the announcement as regulatory positioning. Those criticisms are fair, and a serious security leader should hold them. But they argue about the wrong variable. Whether the campaign was 90% autonomous or closer to 40%, the direction of travel is the same: the barrier that historically separated nation-state actors from less-resourced groups — the human cost of elite offensive research and operations — is the thing AI erodes. Reconnaissance, lure development, and attack-path mapping that once required dedicated analysts working for days become a concurrent, cheap process. Whether the attack was 90% autonomous or 40% is the wrong debate. The barrier that’s falling is the human cost of offensive expertise. Does AI Create New Vulnerability Classes, or Just Exploit Existing Ones Faster? It exploits the existing ones faster. AI-orchestrated att
```

#### Corroborating sources (6)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: The First AI State-Sponsored Attack: What It Means for Defenders
  - Published: 2026-06-10T07:50:48+00:00
  - Link: https://horizon3.ai/intelligence/blogs/first-ai-state-sponsored-attack-threat-model/
  - Summary: In November 2025, Anthropic disclosed the first AI-orchestrated state-sponsored cyberattack. Here's what GTG-1002 actually changes for security teams.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories
  - Published: 2026-06-11T13:20:41+00:00
  - Link: https://thehackernews.com/2026/06/threatsday-bulletin-worm-code-leaked-ai.html
  - Summary: It's been one of those weeks. You expect the usual noise: recycled malware, sloppy attacks, another easy target getting hit. Instead, there's a supply chain attack kit in a public repo, a $5,000-a-month RAT that clones browsers, and research showing AI agents can be tricked into leaking real credentials. The bigger problem is how polished this all looks now. Mule networks run like SaaS.
- **Simon Willison** (ai_security_agentic_risk)
  - Title: "They screwed us": Personality clashes sent Anthropic's models offline
  - Published: 2026-06-15T14:57:33+00:00
  - Link: https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything
  - Summary: "They screwed us": Personality clashes sent Anthropic's models offline Lots of "source familiar with the administration's thinking" and "source close to Anthropic" in this Axios piece, which is the best collection of behind-the-scenes gossip I've seen about the US government export control Mythos/Fable story so far. Logan Graham ( I lead the Frontier Red Team at Anthropic ), Dave Orr (Head of Safeguards, previously a Director of Engineering at Google DeepMind), and blog favorite Nicholas Carlini are reported to be meeting with the Commerce Department today in D.C. Good luck to them! (I just noticed Logan was "Special Adviser to the Prime Minister" in the Boris Johnson era, covering AI, science, and technology policy - so significant political experience.) This closing notes doesn't give me much optimism that we'll be getting Fable back any time soon: The bottom line : One option is to make sure Anthropic's models can't be jailbroken — though perfect jailbreak resistance may be impossib
- **The Record** (cyber_news_breach_reporting)
  - Title: Anthropic says US government forced it to disable cybersecurity AI models
  - Published: 2026-06-15T12:31:00+00:00
  - Link: https://therecord.media/anthropic-says-gov-forced-it-to-disable-cyber-ai-models
  - Summary: According to the company, the directive cited national security authorities. It appears to be the first time such authorities have been used to curtail the export of AI models rather than chips or hardware.
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Anthropic disables new models after government calls them a national security concern
  - Published: 2026-06-13T18:29:36+00:00
  - Link: https://cyberscoop.com/us-government-anthropic-fable-5-mythos-5-export-controls/
  - Summary: The Commerce Department’s expert control decree led to the company shutting off access to Fable 5 and Mythos 5 worldwide, drawing sharp criticism from researchers and industry analysts. The post Anthropic disables new models after government calls them a national security concern appeared first on CyberScoop .
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: MeshCentral: From XSS to RCE
  - Published: 2026-06-13T20:34:17+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u51f9t/meshcentral_from_xss_to_rce/
  - Summary: Using Claude Code to find and weaponise an XSS in MeshCentral using a rogue client, resulting in RCE. submitted by /u/kev-thehermit [link] [comments]

### Cluster 82878a14f9 — score 17

- Title: Trust No Skill: Integrity Verification for AI Agent Supply Chains
- Source: Unit 42 (threat_research_primary)
- Published: 2026-06-11T10:00:24+00:00
- Link: https://unit42.paloaltonetworks.com/ai-agent-supply-chain-risks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, supply_chain
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Protect enterprise AI agents from supply chain risks by auditing third-party skills for hidden vulnerabilities and multi-stage attack chains. The post Trust No Skill: Integrity Verification for AI Agent Supply Chains appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Trust No Skill: Integrity Verification for AI Agent Supply Chains 7 min read Related Products Code to Cloud Platform Prisma AIRS Unit 42 AI Security Assessment By: Yuhao Wu Tony Li Hongliang Liu Published: June 11, 2026 Categories: Malware Threat Research Tags: AI agents Credential exfiltration LLMs OpenClaw Supply chain Share Executive Summary AI agents now extend their capabilities by installing third-party skills the way smartphones install apps. Anyone can publish a skill to a public registry. Anyone can install one into a production agent. And until now, no automated tool has verified what a skill does before it gains privileged access to credentials, files and shell commands inside that agent. We introduce Behavioral Integrity Verification (BIV), an audit primitive that compares what a skill claims to do against what it does, across all three of its surfaces: Metadata Executable code Natural-language instructions Applied at registry scale, BIV finds that most skills deviate from declared behavior. The vast majority of those gaps are sloppy documentation, not malice. But a smaller, dangerous slice carries multi-stage attack chains, where individually benign-looking capabilities combine into credential theft, remote code execution or silent data exfiltration. The agent-skill ecosystem now stands where mobile applications and browser extensions were a decade ago. Extensibility has outpaced the supply-chain audit primitives that should gate it. Security teams running large language model (LLM) agents in production should inventory the third-party skills installed and require a behavioral-integrity check before installation rather than after. Palo Alto Networks customers are better protected from this type of issue through the following products and services: Prisma AIRS The Unit 42 AI Security Assessment can help empower safe AI use and development. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics LLM , AI Agents , Supply Chain Background Enterprises now deploy LLM agents to automate tasks across code generation, IT operations, customer support and internal workflows. These agents are extended with skills, the agent equivalent of an app: a small package that bundles executable code with a YAML manifest and a natural-language SKILL.md file telling the agent when and how to use it. Once installed, a skill runs inside the agent's privileged context. It can read environment variables, call external services, write files and execute shell commands on behalf of the organization. Public agent-skill registries now host tens of thousands of these packages. Anyone can publish. Anyone can install. The platforms that came before, package managers, mobile app stores and browser extension marketplaces, all eventually grew automated audit ecosystems after attackers turned the openness against users. The agent-skill ecosystem has not. The audit problem in this ecosystem differs from anything earlier platforms faced. A skill's behavior splits across three modalities: Metadata Executable code Natural-language instructions The metadata declares what the skill is supposed to do. The code and instructions together drive what it does. No existing scanner reads all three, and the registry has no automated way to verify that the two sides match. BIV is the audit primitive that compares them. The Method: Declared Vs. Actual Behavior BIV asks one question of every skill: Does what it says match what it does? To answer that question consistently across tens of thousands of skills, BIV needed a shared vocabulary. We used a fixed taxonomy of 29 capabilities organized into seven families: Network File system Process execution Environment Encoding Credentials Instruction-level threats Two parallel tracks populate the taxonomy: The declared track reads the metadata. Deterministic parsers handle structural fields l
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Trust No Skill: Integrity Verification for AI Agent Supply Chains
  - Published: 2026-06-11T10:00:24+00:00
  - Link: https://unit42.paloaltonetworks.com/ai-agent-supply-chain-risks/
  - Summary: Protect enterprise AI agents from supply chain risks by auditing third-party skills for hidden vulnerabilities and multi-stage attack chains. The post Trust No Skill: Integrity Verification for AI Agent Supply Chains appeared first on Unit 42 .

### Cluster 3e3984a344 — score 17

- Title: From SQLi to RCE – Exploiting LangGraph’s Checkpointer
- Source: Check Point Research (threat_research_primary)
- Published: 2026-06-11T13:37:11+00:00
- Link: https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- cve_ids: CVE-2025-67644, CVE-2026-27022, CVE-2026-28277
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- cve_ids: CVE-2025-67644, CVE-2026-28277, CVE-2026-27022
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
By Yarden Porat AI agents need memory. Frameworks like LangGraph provide it through checkpointers – persistence layers that store execution state. But what happens when that persistence layer isn’t locked down? Key Points Background LangGraph is an open-source framework for building stateful, multi-agent AI systems with built-in persistence. It’s an extension of LangChain, with over […] The post From SQLi to RCE – Exploiting LangGraph’s Checkpointer appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 16 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 459 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 412 How To Guides 13 Ransomware 5 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 From SQLi to RCE – Exploiting LangGraph’s Checkpointer June 11, 2026 https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/ By Yarden Porat AI agents need memory. Frameworks like LangGraph provide it through checkpointers – persistence layers that store execution state. But what happens when that persistence layer isn’t locked down? Key Points Check Point Research analyzed LangGraph , an open-source framework for stateful AI agents with over 50 million monthly downloads, and uncovered three vulnerabilities in its persistence layer. Two of them chain into remote code execution : a SQL injection in the SQLite checkpointer ( CVE-2025-67644 ) and an unsafe msgpack deserialization ( CVE-2026-28277 ). A third, parallel issue ( CVE-2026-27022 ) introduces the same injection class into the Redis checkpointer. Who’s at risk: teams self-hosting LangGraph with the SQLite or Redis checkpointer, where the application exposes get_state_history() with a user-controlled filter . LangChain’s managed cloud service, LangSmith Deployment (formerly LangGraph Platform), runs PostgreSQL and is not vulnerable. LangChain patched all three issues. Users should update to langgraph-checkpoint-sqlite 3.0.1+ , langgraph 1.0.10+ , and langgraph-checkpoint-redis 1.0.2+ . Background LangGraph is an open-source framework for building stateful, multi-agent AI systems with built-in persistence. It’s an extension of LangChain, with over 50 million monthly downloads according to PyPI stats. Checkpointers are LangGraph’s persistence layer that stores execution state at each step. LangGraph supports two checkpointer implementations: SQLite and PostgreSQL. Vulnerability #1: SQL Injection (CVE-2025-67644) The SQLite Checkpointer Database Schema: The SQLite checkpointer uses an internal table called checkpoints with the following structure: CREATE TABLE checkpoints ( thread_id TEXT NOT NULL, checkpoint_ns TEXT NOT NULL DEFAULT '', checkpoint_id TEXT NOT NULL, parent_checkpoint_id TEXT, type TEXT, checkpoint BLOB, metadata BLOB, PRIMARY KEY (thread_id, checkpoint_ns, checkpoint_id) ); The metadata column stores additional contextual information about each checkpoint in JSON format. For example: { "user_id": "alice", "step": 1, "source": "input" } The list() Function and Filtering: When calling the list() function on sqliteSaver (the checkpointer), the filter parameter is used to query checkpoints based on their metadata: def list( self, config: RunnableConfig | None, *, filter: dict[str, Any] | None = None, # Used to filter by metadata before: RunnableConfig | None = None, limit: int | None = None, ) -> Iterator[CheckpointTuple]: The filter parameter is passed to an internal function called _metadata_predicate , which constructs the SQL WHERE clause to query checkpoints by their metadata fields. # process metadata query for query_key, query_value in filter.items(): operator, param_value = _where_value(query_value) predicates.append( f"json_extract(CAST(metadata AS TEXT), '$.{query_key}') {operator}" ) param_values.append(param_value) return (predicates, param_values) The Injection The vulnerability exists in how _metadata_predicate handles the query_key from the filter dictionary. Notice this critical line: f"json_extract(CAST(metadata AS TEXT), '$.{query_key}') {operator}" An attacker-controlled filter could provide a query_key with a ' character that will escape the JSON path string and inject arbitrary SQL code. Injection -> Arbitrary Deserialization To understand how SQL injection leads to arbitrary deserialization, we need to see the complete picture
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: From SQLi to RCE – Exploiting LangGraph’s Checkpointer
  - Published: 2026-06-11T13:37:11+00:00
  - Link: https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/
  - Summary: By Yarden Porat AI agents need memory. Frameworks like LangGraph provide it through checkpointers – persistence layers that store execution state. But what happens when that persistence layer isn’t locked down? Key Points Background LangGraph is an open-source framework for building stateful, multi-agent AI systems with built-in persistence. It’s an extension of LangChain, with over […] The post From SQLi to RCE – Exploiting LangGraph’s Checkpointer appeared first on Check Point Research .

### Cluster 9f943550b8 — score 17

- Title: Check Point Warns Critical Auth Bypass Bug Exploited in the Wild
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-06-09T09:30:00+00:00
- Link: https://www.infosecurity-magazine.com/news/check-point-critical-auth-bypass/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security, ransomware_extortion, zero_day
- affected_industries: financial_services, government, healthcare
- affected_products: Anthropic/Claude, Cisco, Ivanti
- cve_ids: CVE-2026-50751, CVE-2026-50752
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, ai_security, active_exploitation
- affected_industries: healthcare, financial_services, government
- affected_products: Ivanti, Cisco, Anthropic/Claude
- cve_ids: CVE-2026-50751, CVE-2026-50752
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Check Point says a critical vulnerability in its Remote Access VPN and Mobile Access solutions has been exploited by Qilin
```

#### Full body

```
Infosecurity Magazine Home » News » Check Point Warns Critical Auth Bypass Bug Exploited in the Wild Check Point Warns Critical Auth Bypass Bug Exploited in the Wild News 9 June 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster Check Point has urged customers to patch a critical zero-day vulnerability in its Remote Access VPN and Mobile Access solutions that is being actively exploited. CVE-2026-50751 is an authentication bypass flaw that affects deployments configured to use the deprecated IKEv1 key exchange protocol. The security vendor revealed on June 8 that in one case, an affiliate of the Qilin ransomware group has exploited the flaw in “post-compromise activity.” “An attacker can bypass user authentication by exploiting a logic flow weakness in the Remote Access and Mobile Access certificate validation and establish a remote access VPN connection without a valid user password,” Check Point said. “Check Point has observed active exploitation of this vulnerability in the wild.” Read more on Check Point: Cybercriminals Exploit CheckPoint Antivirus Driver in Malicious Campaign. The flaw has been exploited since May 7, but attempts increased in early June, according to the writeup. Check Point launched in investigation on June 4 and said attacks have so far been limited to a “few dozen targeted organizations” globally. “Based on the post-exploitation activity we observed, we assess with medium confidence that the actor behind the exploitation of CVE-2026-50751 is financially motivated, uses Qilin ransomware,” it continued. “We believe that this threat actor infrastructure is exploiting other VPN-related vulnerabilities such as the ones published by Palo Alto, Fortinet and F5.” The affiliate apparently used dedicated virtual private server (VPS) infrastructure to carry out the attacks, with some IPs hosted by Kaupo Cloud HK, Shock Hosting, and Vultr Holdings. Another Vulnerability Discovered While Check Point was investigating CVE-2026-50751, which has a CVSS score of 9.3, it found another vulnerability. CVE-2026-50752 has a score of 7.4 and is not currently being exploited by threat actors, the vendor claimed. “CVE-2026-50752 impacts certificate validation in deprecated IKEv1 key exchange and may allow man-in-the-middle interference with site-to-site VPN communications under specific conditions,” it explained. “Check Point has not observed exploitation of this vulnerability in the wild; customers are advised to apply updates to mitigate potential exposure.” Customers are urged to update all affected products with the published hotfix. You may also like Check Point Urges VPN Configuration Review Amid Attack Spike News 28 May 2024 VPN and RDP Exploitation the Most Common Attack Technique News 29 June 2023 CISA Issues Emergency Directive Over Exploited Cisco SD-WAN Flaws News 12 March 2026 Ivanti Zero-Days Exploited By Multiple Actors Globally News 16 January 2024 Global Cyber-Attacks Rise by 7% in Q1 2023 News 28 April 2023 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Anthropic Rolls Out Claude Security for AI Vulnerability Scanning News 1 May 2026 1 North Korean Hackers Use Fake Coding Tasks to Steal Crypto News 8 June 2026 2 Infosecurity Europe: Practical Lessons From Lloyds' Agentic AI Security Playbook News 5 June 2026 3 Shadow AI is Exposing the Same Governance Failures Cybersecurity Teams Have Ignored For Years Opinion 10 June 2026 4 Infosecurity Europe: Reactive Security Is Failing Healthcare Organizations, Experts Warn News 5 June 2026 5 Infosecurity Europe: Mythos Outperforms GPT5.5 on Google Chrome Vulnerability Exploits, Says New Benchmark News 4 June 2026 6 Infosecurity Europe: Mythos Outperforms GPT5.5 on Google Chrome Vulnerability Exploits, Says New Benchmark News 4 June 2026 1 North Korean Hackers Use Fake Coding Tasks to Steal Crypto News 8 June 2026 2 Infosecurity Europe: Prompt Injection Remains Unsolved, OWASP Research
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Check Point Warns Critical Auth Bypass Bug Exploited in the Wild
  - Published: 2026-06-09T09:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/check-point-critical-auth-bypass/
  - Summary: Check Point says a critical vulnerability in its Remote Access VPN and Mobile Access solutions has been exploited by Qilin

### Cluster e002a0d5e1 — score 16

- Title: Reconstructing AI activity in investigations
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-09T17:35:06+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/09/reconstructing-ai-activity-investigations/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: Azure, Microsoft 365

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, data_breach, phishing_social_eng, ransomware_extortion
- affected_products: Anthropic/Claude, Azure, GitHub, Microsoft 365, Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, data_breach, ai_security
- affected_products: Anthropic/Claude, GitHub, Azure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Learn how to investigate AI activity in Microsoft 365 Copilot and Azure AI services using a structured, telemetry-driven approach. This playbook helps security teams reconstruct events, assess data exposure, and detect potential threats faster. The post Reconstructing AI activity in investigations appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Topics Actionable threat insights AI and agents AI systems are now part of everyday work. Investigators need a consistent way to reconstruct what happened within them. Security teams are already investigating activity involving Microsoft 365 Copilot and Azure AI services—from prompt injection attempts to unexpected data access. Those signals are observable. Without structure, they do not form a coherent account of what occurred. AI interactions generate telemetry across Microsoft Purview, Defender, and Sentinel. That telemetry captures who initiated an interaction, when it occurred, and which resources were involved. It provides the foundation for reconstructing AI activity in enterprise environments. It’s turning those signals into an investigation. To help address that challenge, we’ve published a new investigator playbook for Microsoft 365 Copilot and Azure AI services. The playbook provides a structured approach for investigating AI-related activity using the telemetry already available across Microsoft security products. The methodology follows a scope–context–signal sequence. Investigations begin by identifying who interacted with AI systems, when the activity occurred, and which services were involved. From there, investigators expand into resource context: what the system accessed, what data may have been exposed, and how that activity aligns with expected behavior. Detection signals, including prompt injection attempts, anomalous usage patterns, or credential exposure alerts, are then evaluated within that broader chain of activity. AI telemetry is constructed metadata-first, providing identity, time, and resource context across interactions. That structure is what moves investigations from isolated signals to a coherent account of what occurred. When analyzed together, those elements allow investigators to establish what happened, understand the impact, and determine whether activity reflects normal usage, policy violations, or indicators of compromise. The playbook operationalizes this approach across Microsoft 365 Copilot and Azure AI services. It brings together the required configuration, queries, and detection patterns into a single working model — covering schema references, KQL queries, and detection logic — enabling investigators to follow AI activity across tools with fewer ad hoc pivots. It also extends that model to agent-based systems, where the investigative picture expands: which agents are deployed, how they are configured, what data they are authorized to access, and whether that authorization was used as expected. The outcome is practical. Response teams can move from isolated signals to a reconstructed account of observed activity: scoping AI usage, understanding what data was accessed during interactions, and assessing whether observed behavior is consistent with normal usage, policy violations, or indicators of active threat conditions across Microsoft security services. As AI becomes part of everyday business workflows, response teams need the same investigative rigor they apply to endpoints, identities, and cloud infrastructure. The ability to determine what happened, what data was involved, and whether activity was authorized is quickly becoming a core incident response capability. The playbook gives you the tools to answer it. Download it here: https://aka.ms/AIIRplaybook Related posts June 8 17 min read AI brands as bait: How threat actors are using the AI hype in social engineering As threat actors operationalize AI to accelerate attacks, they are also leveraging the wider global interest around AI itself as a social engineering lure. June 5 10 min read Securing CI/CD in an agentic world: Claude Code Github action case Microsoft Threat Intelligence identified a prompt injection pathway in Claude Code GitHub Action that allowed access to workflow secrets under specific conditions. June 4 6 min read Updating the taxonomy of failure modes i
```

#### Corroborating sources (4)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Reconstructing AI activity in investigations
  - Published: 2026-06-09T17:35:06+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/09/reconstructing-ai-activity-investigations/
  - Summary: Learn how to investigate AI activity in Microsoft 365 Copilot and Azure AI services using a structured, telemetry-driven approach. This playbook helps security teams reconstruct events, assess data exposure, and detect potential threats faster. The post Reconstructing AI activity in investigations appeared first on Microsoft Security Blog .
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Holding blobs for ransom: Four methods for Azure Storage ransomware
  - Published: 2026-06-15T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/azure-blob-storage-ransomware-four-methods/
  - Summary: This post explores four vectors for threat actors to abuse Azure Storage to maliciously encrypt victim blobs, including step-by-step explanations and event codes for detection.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New attack turned Microsoft 365 Copilot into 1-click data theft tool
  - Published: 2026-06-15T13:00:00+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-attack-turned-microsoft-365-copilot-into-1-click-data-theft-tool/
  - Summary: A critical vulnerability chain dubbed SearchLeak in Microsoft 365 Copilot Enterprise could allow attackers to steal sensitive data from a target's mailbox, OneDrive, or SharePoint account through a specially crafted URL. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes
  - Published: 2026-06-15T15:09:05+00:00
  - Link: https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html
  - Summary: A single click on a trusted Microsoft link could have let an attacker pull emails, calendar details, and indexed files out of Microsoft 365 Copilot Enterprise Search. Researchers at Varonis Threat Labs chained three bugs into a one-click exfiltration path they call SearchLeak. Because the link pointed to a real microsoft.com domain, traditional anti-phishing and URL filtering tools were

### Cluster 642ef55777 — score 13

- Title: 16 Best Open Source Application Security Tools 2026
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-06-11T14:36:41+00:00
- Link: https://orca.security/resources/blog/open-source-application-security-tools/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: GitHub, GitLab
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: GitLab, GitHub
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Most application breaches do not begin with a zero-day exploit. They start with an exposed secret, a vulnerable dependency, or insecure code that reached production unnoticed. Open source application security tools help security teams identify these issues before attackers do. The tools covered in this article are organized by the specific layer they address, not […]
```

#### Full body

```
Table of contents What are application security tools, and why are they important? The top OSS application security tools by category Top OSS SCA tools Top secret scanning tools Top SAST tools Top DAST tools Top penetration testing tools Core features of a good OSS AppSec tool Contextual risk scoring and exploitability Runtime awareness and traceability Scalability and performance on large codebases Up-to-date vulnerability and compliance coverage How to choose the right OSS AppSec tools for your stack Incorporating OSS AppSec tools into a larger security strategy How Orca Security enhances open source AppSec tools Frequently asked questions about Open Source Application Security Tools Most application breaches do not begin with a zero-day exploit. They start with an exposed secret, a vulnerable dependency, or insecure code that reached production unnoticed. Open source application security tools help security teams identify these issues before attackers do. The tools covered in this article are organized by the specific layer they address, not by popularity or marketing positioning. Each entry covers what the tool actually scans, the specific vulnerability classes it finds, how it integrates into a CI/CD pipeline, and where its coverage ends. Understanding the coverage boundary of each tool is as important as understanding what it covers, because gaps between tools are where production vulnerabilities persist. Key takeaways OWASP Dependency-Check identifies known CVEs in dependencies for Java, .NET, JavaScript, Python, Ruby, PHP, and Node.js projects during Maven and Gradle build processes. SonarQube performs static analysis on source code across more than 30 languages to detect injection flaws, XSS, and authentication issues in pull requests. OWASP ZAP tests running web applications for runtime vulnerabilities such as SQL injection, cross-site scripting, and server-side request forgery through automated scans. TruffleHog scans Git repositories and CI/CD pipelines for exposed secrets and verifies whether detected credentials remain active through API checks. Semgrep runs custom static analysis rules to find framework-specific vulnerabilities across more than 30 programming languages in GitHub Actions and GitLab CI. sqlmap automates the detection and exploitation of SQL injection vulnerabilities in web applications during authorized penetration tests on major database systems. GitGuardian monitors GitHub organizations for exposed credentials in repositories and pull requests with real-time notifications to repository administrators. Tool Category Primary Function Best For OWASP Dependency-Check SCA Dependency CVEs Dependency security TruffleHog Secret Scanning Credential exposure Secret detection SonarQube SAST Source code analysis Code security OWASP ZAP DAST Runtime testing Web app testing sqlmap Pentesting SQL injection validation Exploit verification What are application security tools, and why are they important? Application security tools are software systems that identify, assess, and help remediate security vulnerabilities in application code, dependencies, runtime behavior, and supporting infrastructure across the software development lifecycle (SDLC). The category is important because applications are a primary attack surface in modern cloud environments. The 2026 Verizon DBIR found that exploitation of software vulnerabilities became the leading initial access vector in confirmed breaches, accounting for 31% of incidents and surpassing credential abuse for the first time in the report’s history. Common causes include unpatched dependencies, exposed credentials, application-layer vulnerabilities, and exploitable misconfigurations that create pathways for attackers to gain initial access. Application security tools that operate at the code and dependency layer enable detection before deployment. Tools that operate at the runtime layer detect vulnerabilities that only manifest in a running application. Both layers are
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: 16 Best Open Source Application Security Tools 2026
  - Published: 2026-06-11T14:36:41+00:00
  - Link: https://orca.security/resources/blog/open-source-application-security-tools/
  - Summary: Most application breaches do not begin with a zero-day exploit. They start with an exposed secret, a vulnerable dependency, or insecure code that reached production unnoticed. Open source application security tools help security teams identify these issues before attackers do. The tools covered in this article are organized by the specific layer they address, not […]

### Cluster d6a5b3220c — score 13

- Title: Sponsored: Understanding CI/CD attack paths
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-06-12T04:28:07+00:00
- Link: https://risky.biz/RBNEWSSI131/
- Fetch status: ok
- Member count: 8
- Corroborating source count: 6
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, zero_day
- affected_products: GitHub, Microsoft Defender, npm
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
In this sponsored episode, James Wilson chats with SpecterOps CTO Jared Atkinson about the central role that GitHub has played in recent supply chain compromises. GitHub is where code gets built, tested, and shipped to devices, cloud, and on-prem environments. Understanding the paths an attacker can use to get into GitHub, and where they can pivot to from there, is essential to securing your GitHub repos and CI/CD pipelines.
```

#### Full body

```
Risky Bulletin Podcast June 12, 2026 Sponsored: Understanding CI/CD attack paths Presented by James Wilson Technology Editor In this sponsored episode, James Wilson chats with SpecterOps CTO Jared Atkinson about the central role that GitHub has played in recent supply chain compromises. GitHub is where code gets built, tested, and shipped to devices, cloud, and on-prem environments. Understanding the paths an attacker can use to get into GitHub, and where they can pivot to from there, is essential to securing your GitHub repos and CI/CD pipelines. Your browser does not support the audio element. Sponsored: Understanding CI/CD attack paths â¶ 0:00 / 15:48 Subscribe Brought to you by SpecterOps Know Your Adversary
```

#### Corroborating sources (6)

- **Risky Business News** (practitioner_analysis)
  - Title: Sponsored: Understanding CI/CD attack paths
  - Published: 2026-06-12T04:28:07+00:00
  - Link: https://risky.biz/RBNEWSSI131/
  - Summary: In this sponsored episode, James Wilson chats with SpecterOps CTO Jared Atkinson about the central role that GitHub has played in recent supply chain compromises. GitHub is where code gets built, tested, and shipped to devices, cloud, and on-prem environments. Understanding the paths an attacker can use to get into GitHub, and where they can pivot to from there, is essential to securing your GitHub repos and CI/CD pipelines.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows
  - Published: 2026-06-10T05:22:01+00:00
  - Link: https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html
  - Summary: The anonymous security researcher going by the name Chaotic Eclipse (aka Nightmare-Eclipse) has released a proof-of-concept (PoC) exploit for yet another Microsoft Defender zero-day named RoguePlanet. "The exploit is a race condition, so it's a hit or miss," the researcher, who published the exploit under a new GitHub account "MSNightmare" said. "I have managed to get a 100% success rate on
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Miasma Supply Chain Worm Burrows Into 73 Microsoft Repositories
  - Published: 2026-06-09T19:33:45+00:00
  - Link: https://www.darkreading.com/application-security/miasma-supply-chain-worm-73-microsoft-repositories
  - Summary: The attacks stemmed from a GitHub account that was also compromised in a previous Miasma attack on Microsoft last month.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: GitHub to Update npm to Thwart Software Supply Chain Attacks
  - Published: 2026-06-12T13:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/github-update-npm-supply-chain/
  - Summary: NPM, part of GitHub, announced a new version of the npm package manager with several security improvements, including disabling install scripts
- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: Mini Shai-Hulud: Where SLSA’s Boundaries Fall
  - Published: 2026-06-10T18:49:33+00:00
  - Link: https://openssf.org/blog/2026/06/10/mini-shai-hulud-where-slsas-boundaries-fall/
  - Summary: The “Mini Shai-Hulud” attack chained a GitHub Actions workflow misconfiguration, cache poisoning, and OIDC token extraction to publish malicious packages through legitimate CI/CD pipelines.
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Free Compromise Detection for GitHub Repos - Tracebit Community Edition
  - Published: 2026-06-12T15:12:18+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u3y1zo/free_compromise_detection_for_github_repos/
  - Summary: submitted by /u/tracebit [link] [comments]

### Cluster 5af9a64c84 — score 12

- Title: Beyond the Score: Using AI to Translate CVEs into Real-World Business Risk
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-15T14:44:28+00:00
- Link: https://www.rapid7.com/blog/post/ai-beyond-the-score-translating-cves-into-real-business-risk
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: legal_professional
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: legal_professional
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Security leaders rarely struggle to gather data, but they often struggle to turn that data into something clear and meaningful for the business. In a typical week, a CISO might receive a report listing hundreds or even thousands of vulnerabilities, most of them accompanied by CVSS scores that make the entire list look urgent, while also managing the wider set of operational, regulatory, and strategic demands that already come with the role. That difficulty becomes more obvious when the same information has to be carried into the boardroom, where the questions are rarely about CVE IDs or exploit counts in isolation. What leadership wants to understand is whether the organization’s revenue, uptime, legal exposure, or broader resilience could be affected, and how quickly those risks need to be addressed. This is where many security programs lose momentum, because the technical view of severity does not always line up neatly with the business view of consequence. Bridging that gap has trad
```

#### Full body

```
Back to Blog Artificial Intelligence Beyond the Score: Using AI to Translate CVEs into Real-World Business Risk Rapid7 Jun 15, 2026 | Last updated on Jun 15, 2026 | 7 min read DISCOVER RAPID7 MDR Security leaders rarely struggle to gather data, but they often struggle to turn that data into something clear and meaningful for the business. In a typical week, a CISO might receive a report listing hundreds or even thousands of vulnerabilities, most of them accompanied by CVSS scores that make the entire list look urgent, while also managing the wider set of operational, regulatory, and strategic demands that already come with the role. That difficulty becomes more obvious when the same information has to be carried into the boardroom, where the questions are rarely about CVE IDs or exploit counts in isolation. What leadership wants to understand is whether the organization’s revenue, uptime, legal exposure, or broader resilience could be affected, and how quickly those risks need to be addressed. This is where many security programs lose momentum, because the technical view of severity does not always line up neatly with the business view of consequence. Bridging that gap has traditionally been slow, manual work, which is one reason AI is starting to matter more in vulnerability management: it can help translate technical findings into business context that is clearer, faster to act on, and easier for leadership to understand. Why CVSS alone does not reflect real-world business risk For years, the industry has relied on CVSS as a quick way to judge urgency, and while the framework does account for factors such as attack vector, attack complexity, and other attack requirements, the score is still calculated in isolation and often misses the conditions that shape real risk inside an organization. A CVSS 9.8 vulnerability affecting a legacy printer in a segmented branch office may look critical on paper, but it is unlikely to carry the same business impact as a 7.5 vulnerability affecting an internet-facing database that holds sensitive customer data. One of the long-standing weaknesses of static scoring is that it tells you how severe a flaw may be in theory, but not how much disruption it could cause in your own environment, how exposed the affected asset is, or how closely it is tied to a revenue-generating or business-critical process. That is where AI becomes more useful, because it can add the missing context that helps security teams judge not just how serious a vulnerability looks, but how much it matters in practice. Machine learning models can now process a much broader set of inputs, including attacker activity, exploit availability, internal network topology, and the business value attached to the asset or process involved. Rather than leaving teams with a static queue of scores, that creates a live view of risk shaped by reachability, exposure, and business consequence, making it easier to separate technical severity from actual organizational risk. How AI helps connect vulnerabilities to business impact One of the more practical ways AI can improve vulnerability management is by helping security teams connect technical findings to the parts of the business they actually affect. A vulnerability tied to an obscure IP address may not mean much on its own, but the picture changes quickly when that asset is identified as part of a regional payment system, a customer-facing portal, or a supply chain application the business depends on. That kind of asset attribution has traditionally taken time, context, and manual investigation. AI can help shorten that process by linking technical findings to business function much more quickly. Instead of relying only on severity scores or yesterday’s alerts, AI can weigh a broader set of signals, including exploit activity, attacker behavior, asset exposure, and internal topology, which gives security teams a more grounded way to judge where risk is most likely to become operationally si
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Beyond the Score: Using AI to Translate CVEs into Real-World Business Risk
  - Published: 2026-06-15T14:44:28+00:00
  - Link: https://www.rapid7.com/blog/post/ai-beyond-the-score-translating-cves-into-real-business-risk
  - Summary: Security leaders rarely struggle to gather data, but they often struggle to turn that data into something clear and meaningful for the business. In a typical week, a CISO might receive a report listing hundreds or even thousands of vulnerabilities, most of them accompanied by CVSS scores that make the entire list look urgent, while also managing the wider set of operational, regulatory, and strategic demands that already come with the role. That difficulty becomes more obvious when the same information has to be carried into the boardroom, where the questions are rarely about CVE IDs or exploit counts in isolation. What leadership wants to understand is whether the organization’s revenue, uptime, legal exposure, or broader resilience could be affected, and how quickly those risks need to be addressed. This is where many security programs lose momentum, because the technical view of severity does not always line up neatly with the business view of consequence. Bridging that gap has trad

### Cluster 1714548889 — score 12

- Title: ICYMI: May 2026 @AWS Security
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-06-08T21:00:11+00:00
- Link: https://aws.amazon.com/blogs/security/icymi-may-2026-aws-security/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Read all about the latest AWS security features, compliance updates, and hands-on resources in our new, monthly digest posts. You’ll find expert blog posts, new service capabilities, code samples, and workshops. AWS Security Blog posts This month’s AWS Security Blog posts covered AI security, network protection, identity management, compliance frameworks, and supply chain security. Read […]
```

#### Full body

```
AWS Security Blog ICYMI: May 2026 @AWS Security Read all about the latest AWS security features, compliance updates, and hands-on resources in our new, monthly digest posts. You’ll find expert blog posts, new service capabilities, code samples, and workshops. AWS Security Blog posts This month’s AWS Security Blog posts covered AI security, network protection, identity management, compliance frameworks, and supply chain security. Read on for practical guidance on securing agentic AI workflows, filtering network traffic by category, defending against supply chain attacks, and more. AI Security Security posture improvement in the AI era Author: Celeste Bishop | Published: May 1, 2026 Learn to use the Security Health Improvement Program (SHIP) to strengthen security fundamentals across 10 core use cases for confident AI adoption. Enabling AI sovereignty on AWS Author: Stéphane Israël | Published: May 12, 2026 Learn how AWS delivers control and choice across the AI stack to help customers meet digital and AI sovereignty requirements. The AWS AI Security Framework: Securing AI with the right controls, at the right layers, at the right phases Authors: Riggs Goodman III, Christopher Rae | May 15, 2026 A structured framework that helps security leaders align the right security controls to the right AI use case, at the right layer, at the right deployment phase. Why Policy in Amazon Bedrock AgentCore chose Cedar for securing agentic workflows Authors: Liana Hadarean, Jean-Baptiste Tristan | May 20, 2026 Learn how Cedar’s deterministic authorization, automated reasoning, and formal verification capabilities secure agentic AI tool invocations through Amazon Bedrock AgentCore Gateway. Infrastructure security Securing open proxies in your AWS environment Author: Dodd Mitchell | Published: May 4, 2026 Learn to identify and secure open proxies in your AWS environment to prevent abuse, protect your IP reputation, and control costs. Introducing AI traffic analysis dashboards for AWS WAF Authors: Christopher Jen, Eitav Arditti, Kaustubh Phatak | Published: May 5, 2026 A new dashboard providing visibility into AI bot and agent activity including bot identification, intent classification, and access pattern analysis. Simplifying policy management with URL and Domain Category filtering on AWS Network Firewall Authors: Lawton Pittenger, Sofía Aluma-Santos, Eric Fortenbery, Mostafa Elkhouly | May 28, 2026 Learn to use AWS Network Firewall’s URL and domain category filtering to control access to website categories like AI services, manage exceptions for approved domains, and monitor traffic patterns with Amazon CloudWatch Logs Insights. Why and how to migrate to a Transit Gateway-attached AWS Network Firewall Authors: Frank Phillis, Lawton Pittenger | May 28, 2026 Learn to migrate your centralized AWS Network Firewall deployment to a AWS Transit Gateway -attached model, eliminating the inspection Amazon VPC and enabling flexible cost allocation. Identity Regional routing for AWS access portals: Implementing custom vanity domains for IAM Identity Center Authors: Georgi Baghdasaryan, Laura Reith, Sowjanya Rajavaram | May 14, 2026 Learn to build a custom vanity domain with latency-based routing and automated failover for IAM Identity Center multi-Region access portals. Automating identity lifecycle and security with AWS Directory Service APIs Authors: Ali Alzand, Kevin Sookhan | May 21, 2026 Learn to use the new AWS Directory Service Data APIs with Amazon GuardDuty and AWS Step Functions to automate identity lifecycle management and respond to security threats. Governance and compliance Announcing the ISO 31000:2018 Risk Management on AWS compliance guide Authors: Jesse McMahan, Akanksha Chaturvedi, Mayur Jadhav, Juan Rodriguez, Sana Rahman | Published: May 1, 2026 A compliance guide providing practical guidance for establishing a risk management program using ISO 31000:2018 principles in AWS environments. New compliance guide available: ISO/IEC 42001:20
```

#### Corroborating sources (1)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: ICYMI: May 2026 @AWS Security
  - Published: 2026-06-08T21:00:11+00:00
  - Link: https://aws.amazon.com/blogs/security/icymi-may-2026-aws-security/
  - Summary: Read all about the latest AWS security features, compliance updates, and hands-on resources in our new, monthly digest posts. You’ll find expert blog posts, new service capabilities, code samples, and workshops. AWS Security Blog posts This month’s AWS Security Blog posts covered AI security, network protection, identity management, compliance frameworks, and supply chain security. Read […]

### Cluster 5f8a2fb9b0 — score 12

- Title: Vulnerability management is reaching the limits of human scale
- Source: Sysdig (detection_response_operations)
- Published: 2026-06-10T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/vulnerability-management-is-reaching-the-limits-of-human-scale
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- affected_products: Anthropic/Claude
- cve_ids: CVE-2026-39987
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure, active_exploitation
- affected_products: Anthropic/Claude
- cve_ids: CVE-2026-39987
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Full body

```
< back to blog Vulnerability management is reaching the limits of human scale Published by: Sysdig Team @ linkedin GET THE REPORT Published: June 10, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more Our 2026 Cloud-Native Security and Usage Report confirms that security teams are taking vulnerabilities seriously, with a 75% YoY reduction in exploitable in-use vulnerabilities. However, it also revealed a concerning trend: Vulnerabilities are growing, and teams are struggle to keep up. Are we reaching the limit of human scale? And, if so, what can security teams do to catch up? An exponential growth in vulnerabilities The MITRE Corporation tracks reported vulnerabilities on cve.org . The trend is scary, showing an exponential growth in recent years: To help our users navigate this issue, we introduced Risk Spotlight in 2022. This tool assists Sysdig users in identifying vulnerabilities that are in use, have an existing exploit, and have a fix available. A 75% reduction in this kind of vulnerability year-over-year among our users demonstrates how effective Risk Spotlight is. This metric also highlights the impact that security tools have when they align with the user’s needs. However, in-use vulnerabilities, including those without a known exploit, have plateaued at 5% since last year. This shows that while teams are doing great work prioritizing, they struggle to address the overall exponential increase in vulnerabilities. As a result, there is a huge gap with the in-use vulnerabilities without known exploits. What is new this year is that the absence of a known exploit no longer guarantees security. An exploit can be crafted and weaponized within a few hours with the use of AI, as the Sysdig Threat Research Team (TRT) and Project Glasswing are proving over the last few weeks. AI is changing how we think of vulnerabilities Dealing with vulnerabilities running in production is becoming increasingly important as the window between vulnerability disclosure and exploit weaponization collapses. According to VulnCheck: In 2018, attackers took nearly a year to weaponize vulnerabilities. By 2023, it was only eight days. At the end of 2025, React2Shell was being actively exploited just hours after its disclosure . And earlier in 2026, it took less than 10 hours for CVE-2026-39987 with no proof of concept to use as reference. And now, we’ve seen how AI is expanding to cybersecurity. On the one hand, Anthropic’s Project Glasswing is an AI capable of detecting software vulnerabilities, deemed too risky for the general public. On the other hand, we’ve recently seen how an AI-assisted cloud intrusion achieves admin access in 8 minutes . We expect that, as attackers continue to use AI in their operations, vulnerability weaponization will approach near‑real time. With this scenario in mind, focusing solely on vulnerabilities being actively exploited is no longer enough, and runtime security takes on greater importance as a last line of defense. The next step in automation Slowly, but steadily, organizations have realized the value in stateful detections and also shifted to automated response actions for modern threats. According to our 2026 Cloud-Native Security and Usage Report , the adoption of automated response is surging: More than 70% of organizations use behavior‑based detections across 91% of environments to improve signal quality. 140% more organizations auto-kill processes when detection is triggered. However, to cope with the exponential growth of vulnerabilities and break through the 5% ceiling, organizations need a paradigm shift in their tools. More and more, AI is becoming not only the natural next step in automation, but economically and operationally justified. We believe that autonomous remediation, driven by agentic AI and executed within human‑driven
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: Vulnerability management is reaching the limits of human scale
  - Published: 2026-06-10T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/vulnerability-management-is-reaching-the-limits-of-human-scale

### Cluster fb86222de5 — score 12

- Title: Cisco fixes SD-WAN vManage flaw exploited in zero-day attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-15T17:12:42+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-20262

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Cisco, Microsoft Defender
- cve_ids: CVE-2026-20122, CVE-2026-20128, CVE-2026-20133, CVE-2026-20182, CVE-2026-20262
- urgency_signals: actively_exploited, no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_industries: government
- affected_products: Microsoft Defender, Cisco
- cve_ids: CVE-2026-20262, CVE-2026-20133, CVE-2026-20128, CVE-2026-20122, CVE-2026-20182
- urgency_signals: actively_exploited, zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cisco has released security updates to address a vulnerability in the Catalyst SD-WAN Manager, tracked as CVE-2026-20262, that was exploited in attacks to escalate to root privileges. [...]
```

#### Full body

```
Cisco fixes SD-WAN vManage flaw exploited in zero-day attacks By Sergiu Gatlan June 15, 2026 01:12 PM 0 Cisco has released security updates to address a vulnerability in the Catalyst SD-WAN Manager, tracked as CVE-2026-20262, that was exploited in attacks to escalate to root privileges. Formerly known as SD-WAN vManage, this network management software allows admins to manage up to 6,000 SD-WAN devices from a single dashboard. The now-patched zero-day security flaw affects all deployment types, regardless of device configuration, including on-prem deployments, Cisco SD-WAN Cloud-Pro, Cisco SD-WAN Cloud (Cisco Managed), and Cisco SD-WAN for Government (FedRAMP). Cisco said the issue stems from insufficient validation of user-supplied input during file uploads, which can allow low-privilege remote attackers to execute arbitrary commands as root by sending crafted HTTP requests to an affected API endpoint. "A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file or overwrite any file on the filesystem of an affected system," Cisco said in a Monday advisory . "An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected API endpoint of the affected system. A successful exploit could allow the attacker to create or overwrite any file on the underlying operating system. This file could later be used to elevate to root." Cisco said its Product Security Incident Response Team (PSIRT) became aware of the exploitation of CVE-2026-20262 earlier this month and "strongly" advised customers to patch their systems. Cisco Catalyst SD-WAN Release First Fixed Release 20.9.9.1 and earlier 20.9.9.2 20.12.7.1 and earlier 20.12.7.2 20.15.4.4 and earlier 20.15.4.5 20.15.5.2 and earlier 20.15.5.3 20.18.3 20.18.3.1 26.1.1.1 and earlier 26.1.1.2 While the company did not share any details on these attacks, it shared indicators of compromise (IOCs) warning admins to check their SD-WAN vmanage-server, vmanage-appserver, and serviceproxy-access logs for attempts to upload index.jsp and .war files. In February, Cisco patched another Catalyst SD-WAN Manager information disclosure security flaw (CVE-2026-20133), flagged as actively exploited in late April, and, two weeks later, warned of two more flaws (CVE-2026-20128 and CVE-2026-20122) that were abused in the wild . Last month, it also tagged a maximum-severity Catalyst SD-WAN Controller authentication-bypass flaw (CVE-2026-20182) as actively exploited as a zero-day to gain admin privileges on unpatched devices. More recently, in early June, Cisco warned of one more unpatched Catalyst SD-WAN Manager zero-day (CVE-2026-20245) that was exploited in attacks, allowing attackers to gain root privileges. Over the last several years, the Cybersecurity and Infrastructure Security Agency (CISA) tagged 91 Cisco vulnerabilities as abused in the wild, five of them in Cisco Catalyst SD-WAN Manager and six others exploited in ransomware attacks. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Cisco warns of unpatched SD-WAN zero-day exploited in attacks Cisco warns of new critical SD-WAN flaw exploited in zero-day attacks CISA flags new SD-WAN flaw as actively exploited in attacks Oracle mitigates PeopleSoft zero-day exploited in data theft attacks Microsoft Defender 'RoguePlanet' zero-day grants SYSTEM privileges
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Cisco fixes SD-WAN vManage flaw exploited in zero-day attacks
  - Published: 2026-06-15T17:12:42+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks/
  - Summary: Cisco has released security updates to address a vulnerability in the Catalyst SD-WAN Manager, tracked as CVE-2026-20262, that was exploited in attacks to escalate to root privileges. [...]

### Cluster c17e8e6642 — score 12

- Title: Microsoft Exchange Flaw Lets Attackers Spoof Any Email Address
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-06-09T20:20:00+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/exchange-flaw-attackers-spoof-email-address
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- actor_attribution: ShinyHunters
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- actor_attribution: ShinyHunters
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
“Ghost-Sender" is the result of a widespread misconfiguration, according to researchers, and evidence indicates it's being actively abused in the wild.
```

#### Full body

```
Vulnerabilities & Threats Сloud Security Identity & Access Management Security Application Security News Microsoft Exchange Flaw Lets Attackers Spoof Any Email Address “Ghost-Sender" is the result of a widespread misconfiguration, according to researchers, and evidence indicates it's being actively abused in the wild. Alexander Culafi , Senior News Writer , Dark Reading June 9, 2026 4 Min Read Source: HadelProductions via Getty Images A weakness in certain configurations of Microsoft Exchange enables attackers to send an email from any user to a vulnerable organization. That's according to Swiss cybersecurity firm InfoGuard, which published research today concerning a new vulnerability it described as "Ghost-Sender." Specifically, organizations that use Exchange Online or on-premises in hybrid mode with a third-party mail server or spam filter as its mail exchange (MX) record are vulnerable to this level of spoofing . MX Records are a type of DNS record that directs email messages to the specific server responsible for an organization's domain. "This is regardless of the configured SPF, DKIM, and DMARC policies of the spoofed sender's domain, and the emails are delivered without any further warning," InfoGuard puts in a blog post . "It is possible to send emails from anyone, including external and internal email addresses. For internal senders, Outlook even resolves the sender's profile picture," InfoGuard adds, showing one example where a user received an email claiming to be from Microsoft's official noreply account. An attacker could send fake bills from an official billing email to an organization or conduct phishing attacks or fraud using the internal CEO's actual email address. Related: ShinyHunters Uses Oracle Zero-Day to Rampage Higher Ed Researchers claim this is a widespread misconfiguration, and that while mitigations are available, fewer than half of organizations with an external-facing MX record have a mitigation applied. More concerning, "Based on information provided by Microsoft support, this issue or an adjacent one appears to be actively being abused," the blog post read. InfoGuard claimed Microsoft deployed and rolled back a mitigation to the spoofing attack it observed. How Ghost-Sender Works By default, InfoGuard says, Exchange Online accepts any incoming emails if an external MX record is used by the organization. All an attacker needs to do at that point is send a one-line PowerShell command that sends an email from whatever user the attacker wishes. "If an external MX record is used and no further configurations are made, the organization is vulnerable to Ghost-Sender," InfoGuard says. It's so simple and straightforward that the company even created a testing tool to scan domains and send emails to authorized users. The researchers say Microsoft's own configuration analyzer fails to show warnings or recommendations, nor does it offer any other warnings that a configuration may be vulnerable. Enhanced filtering allegedly doesn't prevent the issue either, nor do the "Strict" and "Standard" Exchange protection settings. Related: Claude Fable 5 Doesn't Change the Mythos Security Story Organizations using Exchange Online or on-premises Microsoft Exchange in hybrid mode can mitigate the threat of Ghost-Sender in one of two ways. They can set up a partner organization connector that applies to emails being sent to any organization or rejects emails based on IP or certificate-based validation. Or, organizations can create a mail flow rule that "quarantines all emails where the X-MS-Exchange-Organization-AuthAs header is not set to Internal and where the IP address does not belong to one expected to send emails to Exchange Online (such as the mail server the MX record points to)." Organizations can test the quality of the mitigations through the aforementioned testing tool InfoGuard provided. Researchers also recommend disabling the Direct Send feature because doing so protects against internal spoofing on its
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Microsoft Exchange Flaw Lets Attackers Spoof Any Email Address
  - Published: 2026-06-09T20:20:00+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/exchange-flaw-attackers-spoof-email-address
  - Summary: “Ghost-Sender" is the result of a widespread misconfiguration, according to researchers, and evidence indicates it's being actively abused in the wild.

### Cluster 29fcf4633f — score 12

- Title: LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-15T16:39:01+00:00
- Link: https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-40217, CVE-2026-47101, CVE-2026-47102
- urgency_signals: critical_cvss
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: ai_security
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-47101, CVE-2026-47102, CVE-2026-40217
- urgency_signals: critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
A default low-privilege account on a LiteLLM proxy can climb to full admin and run code on the server by chaining three vulnerabilities, researchers at Obsidian Security disclosed LiteLLM is a widely deployed open-source AI gateway that brokers calls to more than 100 model providers behind one OpenAI-compatible interface. A server takeover exposes every provider key it holds, the secrets that
```

#### Full body

```
LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers  Swati Khandelwal  Jun 15, 2026 Artificial Intelligence / Vulnerability A default low-privilege account on a LiteLLM proxy can climb to full admin and run code on the server by chaining three vulnerabilities, researchers at Obsidian Security disclosed LiteLLM is a widely deployed open-source AI gateway that brokers calls to more than 100 model providers behind one OpenAI-compatible interface. A server takeover exposes every provider key it holds, the secrets that decrypt its stored credentials, and every prompt and response passing through it. Obsidian rates the full chain CVSS 9.9, in the Critical range. BerriAI , the maintainer, included the complete fix set in LiteLLM v1.83.14-stable, which GitHub lists as released May 2. Upgrade to that release or later to close the three-CVE chain. The three bugs The first link is CVE-2026-47101 , an authorization bypass. When a regular user (an internal_user) generates a virtual API key, LiteLLM stores the caller-supplied allowed_routes field without checking it against the user's role. The field is supposed to narrow what a key can do. Instead, the proxy also treats it as a fallback grant, so a non-admin can mint a key with allowed_routes: ["/*"], a wildcard that reaches every route, including admin-only ones. The same unchecked write shows up on the other key-management endpoints, which is why the fix took three pull requests to land. With the route gate bypassed, the handlers behind it become reachable. Several of them assume the gate has already done the screening, which opens two paths. One is CVE-2026-47102 , privilege escalation. The /user/update endpoint lets a user edit their own record, but does not restrict which fields they can write. A self-update with user_role: "proxy_admin" is accepted and saved, promoting the caller to full proxy admin. An org_admin can hit this endpoint through a legitimate, intended code path with no bypass required; a default internal_user reaches it after CVE-2026-47101. VulnCheck, which assigned the CVE, scores it 8.7 under CVSS 4.0, 8.8 under 3.1. The other is CVE-2026-40217 , a sandbox escape in the Custom Code Guardrail, which compiles and runs admin-supplied Python. The production endpoints ran the code through exec() with no source-level filtering. When exec() gets a globals dict without __builtins__, Python silently injects the full builtins module, which hands the code __import__, open, and eval. A plain payload calling os.system was then enough for a reverse shell. A separate path on the /guardrails/test_custom_code playground endpoint, found independently by X41 D-Sec , defeated a regex deny-list through runtime bytecode rewriting. Both ended in server-side code execution. What an attacker gets LiteLLM sits at a chokepoint, so the reach is wide. A full chain exposes the master key, the salt key that decrypts stored credentials, and the database URL. It also exposes every configured provider key, for OpenAI, Anthropic, Gemini, Bedrock, Azure, and the rest. Keys in config or environment are plaintext; keys in the database are encrypted but recoverable with the salt key. Everything sent through the gateway, prompts and responses, becomes readable, which in real deployments is where PII, source code, internal tickets, and pasted secrets end up. If the proxy also runs as a Model Context Protocol (MCP) or agent gateway, OAuth tokens and tool credentials are in scope too. The sharper risk is not what an attacker reads but what they can rewrite. The gateway sits on the wire between an AI agent and the model, so a compromise lets it alter responses in transit. Obsidian demonstrated this against Claude Code routed through a compromised proxy. This is not prompt injection . Instead of persuading the model to misbehave, the attacker uses LiteLLM's built-in callback mechanism, an extension point that fires on every request and never shows up in the admin UI. The callback
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers
  - Published: 2026-06-15T16:39:01+00:00
  - Link: https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html
  - Summary: A default low-privilege account on a LiteLLM proxy can climb to full admin and run code on the server by chaining three vulnerabilities, researchers at Obsidian Security disclosed LiteLLM is a widely deployed open-source AI gateway that brokers calls to more than 100 model providers behind one OpenAI-compatible interface. A server takeover exposes every provider key it holds, the secrets that
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: PromptSnatcher: AdBlocker stealing Ai Chats - 90k installs
  - Published: 2026-06-13T22:11:13+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u53o6l/promptsnatcher_adblocker_stealing_ai_chats_90k/
  - Summary: Two Chrome extensions presenting as adblockers also intercept every prompt and response on ChatGPT, Claude, Gemini, Copilot, Grok, Perplexity, DeepSeek, and Meta AI, exfiltrating them to operator-controlled servers. They also check whether you're a paid user on 5 of the 8 platforms (ChatGPT, Claude, Perplexity, Copilot, Gemini). Both share the same capture engine, payload format, and partnerId. Two brands, one operation . Smart Adblocker - Chrome Web Store ` iojpcjjdfhlcbgjnpngcmaojmlokmeii `, 80k users Adblock for Browser - Chrome Web Store ` jcbjcocinigpbgfpnhlpagidbmlngnnn `, 10k users Report covers the IOCs, live remote config, reproduction curl, and full target breakdown. Full write-up: MalExt Sentry - Malicious Browser Extension Tracker Chrome Web Store abuse reports filed. submitted by /u/Huge-Skirt-6990 [link] [comments]

### Cluster 93df5bfc62 — score 12

- Title: Risky Bulletin: Arch Linux supply chain attack hits 1,900 packages
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-06-15T05:53:18+00:00
- Link: https://risky.biz/RBNEWS577/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: WordPress

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain
- affected_products: WordPress
- content_type: news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng
- affected_products: WordPress
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Almost 2,000 Arch Linux packages have been infected with malware in a supply chain attack, FISA surveillance powers expire for the first time since 2008, the FBI takes down a Chinese phishing service, and a major supply chain attack hits the WordPress ecosystem.
```

#### Full body

```
Risky Bulletin Podcast June 15, 2026 Risky Bulletin: Arch Linux supply chain attack hits 1,900 packages Presented by Catalin Cimpanu News Editor Claire Aird Newsreader Almost 2,000 Arch Linux packages have been infected with malware in a supply chain attack, FISA surveillance powers expire for the first time since 2008, the FBI takes down a Chinese phishing service, and a major supply chain attack hits the WordPress ecosystem. Your browser does not support the audio element. Risky Bulletin: Arch Linux supply chain attack hits 1,900 packages â¶ 0:00 / 11:14 Subscribe Brought to you by Ent AI Protect the people, secure the system. Show notes Risky Bulletin: Arch Linux supply chain attack spreads to 1,900+ AUR packages
```

#### Corroborating sources (4)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Arch Linux supply chain attack hits 1,900 packages
  - Published: 2026-06-15T05:53:18+00:00
  - Link: https://risky.biz/RBNEWS577/
  - Summary: Almost 2,000 Arch Linux packages have been infected with malware in a supply chain attack, FISA surveillance powers expire for the first time since 2008, the FBI takes down a Chinese phishing service, and a major supply chain attack hits the WordPress ecosystem.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: OptinMonster WordPress plugin hacked in CDN supply-chain attack
  - Published: 2026-06-15T17:37:07+00:00
  - Link: https://www.bleepingcomputer.com/news/security/optinmonster-wordpress-plugin-hacked-in-cdn-supply-chain-attack/
  - Summary: WordPress plugins OptinMonster, TrustPulse, and PushEngage have been compromised in a supply-chain attack impacting Awesome Motive-s content distribution network (CDN). [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Popular WordPress Plugin Scripts Tampered to Plant Hidden Backdoors on Sites
  - Published: 2026-06-15T09:59:38+00:00
  - Link: https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html
  - Summary: An attacker tampered with trusted JavaScript files used by WordPress sites running PushEngage, OptinMonster, and TrustPulse, turning those files into a way to break into the sites. When a site administrator was logged in as the file loaded, the code created an admin account under the attacker's control and installed a hidden plugin that opened a way back in. Ordinary visitors did not trigger it
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Attackers Hijack Popular WordPress Plugins to Deploy Backdoors
  - Published: 2026-06-15T17:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/wordpress-plugin-supply-chain/
  - Summary: Tampered OptinMonster and sister plugins plant hidden backdoors on 1.2 million WordPress sites

### Cluster f99fcc5f45 — score 11

- Title: NIS2 is raising the bar. Here’s how to turn readiness into resilience.
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-15T17:29:15+00:00
- Link: https://www.rapid7.com/blog/post/so-nis2-compliance-turn-readiness-into-resilience
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
The NIS2 directive asks covered organizations to take a more structured approach to risk management, governance, supply chain security, and incident reporting. It expands the scope of who may be covered, raises expectations around management body accountability, introduces clearer and more enforceable requirements, and increases pressure on organizations to show that security is being managed in a consistent, defensible way. Reporting timelines are one of the most visible parts of that shift, with early warning required within 24 hours of awareness for significant incidents, incident notification within 72 hours, and a final report within one month. It also arrived in a landscape that is still uneven, with member states continuing to implement the directive in different ways across the EU. That combination has created a familiar challenge for CISOs and security teams, as the questions coming from boards and leadership are no longer just about whether the organization understands the re
```

#### Full body

```
Back to Blog Security Operations NIS2 is raising the bar. Here’s how to turn readiness into resilience. Sabeen Malik Jun 15, 2026 | Last updated on Jun 15, 2026 | 4 min read DISCOVER RAPID7 MDR The NIS2 directive asks covered organizations to take a more structured approach to risk management, governance, supply chain security, and incident reporting. It expands the scope of who may be covered, raises expectations around management body accountability, introduces clearer and more enforceable requirements, and increases pressure on organizations to show that security is being managed in a consistent, defensible way. Reporting timelines are one of the most visible parts of that shift, with early warning required within 24 hours of awareness for significant incidents, incident notification within 72 hours, and a final report within one month. It also arrived in a landscape that is still uneven, with member states continuing to implement the directive in different ways across the EU. That combination has created a familiar challenge for CISOs and security teams, as the questions coming from boards and leadership are no longer just about whether the organization understands the regulation, but whether it can meet the requirements in practice. NIS2 reaches into risk management, reporting, governance, and supply chain oversight, which means readiness depends on how well security works across the business, not just on how well a policy is written. That is why the most useful way to think about NIS2 is as an operational resilience exercise. Compliance still matters, of course, and teams need to know what the directive requires. What tends to make the difference over time is whether security leaders can connect those requirements to the real conditions of the environment: what is exposed, where ownership sits, how incident response works in practice, how supply chain risk is monitored, and how quickly the organization can move when something material happens. Regulations are easier to absorb than operating model changes. A team may understand that NIS2 raises expectations around governance and incident handling, while still finding it difficult to answer basic questions quickly when pressure rises. Which business services are most critical? Which third parties matter most? Who owns the decision when a serious issue lands? How prepared are we to investigate, communicate, and report inside the timelines the directive expects? Those are the questions that separate a compliance project from a resilience program. That is also why we have been building practical content to help teams move from interpretation to action. Our ebook is the best place to start if you want the wider context. It is designed to help security leaders understand what NIS2 means in practical terms, how to think about the directive beyond a narrow checklist, and how to connect compliance obligations to a broader resilience strategy. If your team needs a stronger narrative for internal stakeholders, or a clearer way to explain why NIS2 should influence operational priorities, the ebook is the most useful first read. Next, our NIS2 Readiness Toolkit is built for teams that want to assess where they are and what to do next. iIt is as a way to bridge the gap between NIS2 requirements and operational reality, with a focus on risk, reporting, and governance. It is designed to help teams spot gaps, focus effort, and simplify the path from regulatory complexity to a more defensible security strategy. In other words, it gives you a practical framework for understanding where readiness is strong, where it is uneven, and what deserves attention first. Our infographic, seen below, is the quickest asset to use when you need to communicate one of the most tangible parts of NIS2: the 24-hour reporting requirement. Some stakeholders need the long-form explanation. Others need a practical view of what has to happen between incident awareness and early notification. The infographic helps
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: NIS2 is raising the bar. Here’s how to turn readiness into resilience.
  - Published: 2026-06-15T17:29:15+00:00
  - Link: https://www.rapid7.com/blog/post/so-nis2-compliance-turn-readiness-into-resilience
  - Summary: The NIS2 directive asks covered organizations to take a more structured approach to risk management, governance, supply chain security, and incident reporting. It expands the scope of who may be covered, raises expectations around management body accountability, introduces clearer and more enforceable requirements, and increases pressure on organizations to show that security is being managed in a consistent, defensible way. Reporting timelines are one of the most visible parts of that shift, with early warning required within 24 hours of awareness for significant incidents, incident notification within 72 hours, and a final report within one month. It also arrived in a landscape that is still uneven, with member states continuing to implement the directive in different ways across the EU. That combination has created a familiar challenge for CISOs and security teams, as the questions coming from boards and leadership are no longer just about whether the organization understands the re

### Cluster e95ce78b9a — score 11

- Title: Maine forced to take down data breach portal after fake notices filed with authorities
- Source: Graham Cluley (practitioner_analysis)
- Published: 2026-06-15T13:23:44+00:00
- Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/maine-take-down-data-breach-portal
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: data_breach
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
The US state of Maine has taken its public data breach notification portal offline after someone submitted fraudulent breach disclosures impersonating two well-known technology companies. Read more in my article on the Hot for Security blog.
```

#### Full body

```
Industry News Data Breach 2 min read Maine forced to take down data breach portal after fake notices filed with authorities Graham CLULEY June 15, 2026 The US state of Maine has taken its public data breach notification portal offline after someone submitted fraudulent breach disclosures impersonating two well-known technology companies. As Bleeping Computer reported last week, fraudulent data breach disclosures were submitted to Maine's official breach portal and publicly posted before their legitimacy could be verified, prompting the named companies to deny the claims. The first fake notification targeted the popular messaging platform Discord, used by hundreds of millions of people worldwide. The notification, which claimed that 10 million people had been impacted by a data breach, was riddled with clues that should have made anyone question its legitimacy: it included a Gmail contact address, a placeholder phone number, and a consumer notification date of January 1st, 2000. Furthermore, it lacked an example notification letter to affected customers - something that is standard practice in legitimate breach filings. However, somewhat more convincing was a fake breach notice that targeted the multiplayer social virtual reality platform VRChat. The filing claimed that hackers had gained access to the company's cloud environment in May, and the data of more than 2.4 million users had been exposed. The fabricated VRChat breach notification listed compromised data including usernames, email addresses, VRChat+ subscription status, login history, device identifiers, IP addresses, and linked Steam or Meta account IDs, according to Bleeping Computer . However, that notification was submitted under the fake name "Scott Caruso" using the email address scaruso(at)vrchat.com. Charles Tupper, Head of Community at VRChat, confirmed to BleepingComputer that the notification was fraudulent: "VRChat did not submit this Notice of Data Incident, and the employee/email cited does not exist. We have no reason to believe that our data or systems have been compromised." In a statement, the office of the Maine Attorney General confirmed that it had "no knowledge of any recent legitimate data breach reports from either VRChat or Discord." So, what had gone wrong? It appears that the abuse of the system was possible because the Maine data breach reporting system lacked a proper verification mechanism. Anyone could submit a breach notification form and have it added to the portal website without verification. Which means that anybody who wanted to cause reputational damage to a company could submit a convincing-looking breach notice and have it published. The portal has temporarily disabled public access to the breach notification database while it reviews its procedures to reduce the chances of similar abuse in the future. And, of course, the false reports of breaches at VRChat and Discord have now been removed. It is not currently known who was behind the false submissions, and whether the targets were chosen deliberately or not. Perhaps worryingly, it also remains unclear how many (if any) other fraudulent breach notices may have been submitted through the portal before public access to it was suspended. Hopefully when the portal is brought back online its security will have been tightened, as many journalists do rely upon services like this to notify the general public about data breaches which occur and companies and organisations. tags Industry News Data Breach Author Graham CLULEY Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s. View all posts You might also like Bookmarks
```

#### Corroborating sources (1)

- **Graham Cluley** (practitioner_analysis)
  - Title: Maine forced to take down data breach portal after fake notices filed with authorities
  - Published: 2026-06-15T13:23:44+00:00
  - Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/maine-take-down-data-breach-portal
  - Summary: The US state of Maine has taken its public data breach notification portal offline after someone submitted fraudulent breach disclosures impersonating two well-known technology companies. Read more in my article on the Hot for Security blog.

### Cluster fce5a342cc — score 11

- Title: NPM 12 Will Change Script Execution Behavior to Prevent Supply Chain Attacks
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-06-13T15:52:58+00:00
- Link: https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: npm

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion, supply_chain, zero_day
- actor_attribution: Handala, ShinyHunters
- affected_industries: government, healthcare
- affected_products: Ivanti, Palo Alto Networks, npm
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, zero_day
- actor_attribution: ShinyHunters, Handala
- affected_industries: healthcare, government
- affected_products: npm, Palo Alto Networks, Ivanti
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
By default, npm install will no longer execute scripts from dependencies, unless explicitly allowed. The post NPM 12 Will Change Script Execution Behavior to Prevent Supply Chain Attacks appeared first on SecurityWeek .
```

#### Full body

```
In response to a recent wave of supply chain attacks targeting the NPM ecosystem, GitHub announced that scripts from dependencies will no longer be executed by default. Multiple major incidents that occurred over the past several months, mainly associated with TeamPCP and the Shai-Hulud self-replicating worm, have been abusing the default, automatic execution of scripts from dependencies during npm install to infect thousands of developers with malware. To better protect users, starting with NPM version 12, which is expected to arrive in July, script execution will be blocked by default, GitHub announced. “ npm install will no longer execute preinstall , install , or postinstall scripts from dependencies unless they are explicitly allowed in your project,” the code-sharing platform explains . The change will also impact native node-gyp builds, such as packages that have a binding.gyp and no explicit install script, as well as prepare scripts from git, file, and link dependencies. The recent Shai-Hulud Miasma attacks relied on a weaponized binding.gyp file. To check how the upcoming change will impact their projects, developers can run npm approve-scripts –allow-scripts-pending , and allow the packages they trust and block the rest, to obtain an allowlist that is written to package.json . Advertisement. Scroll to continue reading. Once the JSON is committed, developers using NPM version 11.16.0 or above will receive warnings if their install routine executes scripts. Additionally, GitHub explains, Git dependencies (direct or transitive) will no longer be resolved at npm install, unless explicitly allowed. “This closes a code-execution path where a Git dependency’s .npmrc could override the Git executable, even with –ignore-scripts ,” the platform notes. Similarly, dependencies from remote URLs will no longer be resolved in NPM version 12. This includes HTTPS tarballs (direct or transitive), but developers can allow them via the –allow-remote flag, which has been available since version 11.15.0. “Upgrade to NPM 11.16.0 or later, run your normal install, and review the warnings. Use npm approve-scripts –allow-scripts-pending to see which packages have scripts, approve the ones you trust, and commit the updated package.json. After that, only the scripts you approved keep running once you upgrade,” GitHub notes. Related: Over 5,500 GitHub Repositories Infected in ‘Megalodon’ Supply Chain Attack Related: Supply Chain Attack Hits 32 Red Hat NPM Packages Related: GitHub Confirms Hack Impacting 3,800 Internal Repositories Related: Grafana Says Codebase and Other Data Stolen via TanStack Supply Chain Attack Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Iranian Cyber Group Handala Claims Cal Water Hack Ivanti Sentry Exploitation Attempts Hitting Honeypots Chrome 149 Update Patches 28 Vulnerabilities CISA Directs Federal Agencies to Prioritize Security Patches Based on Risk Hackers Exploit Langflow Vulnerability for Remote Code Execution Splunk, Palo Alto Networks Patch Severe Vulnerabilities ‘GreatXML’ Zero-Day Exploit Bypasses BitLocker Cyera Raises $600 Million at $12 Billion Valuation Latest News Ransomware Attack Shuts Down Mills of Australia’s Second-Largest Sugar Producer Chinese Hackers Target Medical, Military, and AI Research in North America NewCore Emerges From Stealth Mode With $66 Million in Funding Ukrainian Man Pleads Guilty in US to Conti Ransomware Charges Ozempic Maker Novo Nordisk Says Hackers Breached IT Systems French Government Messaging Platform Breached by Mysterious ‘Misere’ Hacker ShinyHunters Claims Council of Europe Hack FBI, Google Dismantle ‘Outsider Enterprise’ Phishing Service Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends,
```

#### Corroborating sources (3)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: NPM 12 Will Change Script Execution Behavior to Prevent Supply Chain Attacks
  - Published: 2026-06-13T15:52:58+00:00
  - Link: https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
  - Summary: By default, npm install will no longer execute scripts from dependencies, unless explicitly allowed. The post NPM 12 Will Change Script Execution Behavior to Prevent Supply Chain Attacks appeared first on SecurityWeek .
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: The Axios npm compromise was visible in registry metadata before anyone ran npm install
  - Published: 2026-06-13T06:35:01+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u4jjia/the_axios_npm_compromise_was_visible_in_registry/
  - Summary: submitted by /u/GapLimp8396 [link] [comments]
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: How I learned Go in a Day with Antigravity 2.0 and How You Can Do the Same
  - Published: 2026-06-15T09:29:00+00:00
  - Link: https://cloud.google.com/blog/topics/developers-practitioners/how-i-learned-go-in-a-day-with-antigravity-20-and-how-you-can-do-the-same/
  - Summary: I have been exploring how to reclaim my software stack from NPM dependency overhead and replace my resource-intensive Node.js runtime with a compiled, single-binary Go CLI. The result of my efforts is skl , a fast tool we use for managing Agent Skills, that launches in 2ms and uses only 11MB of memory. But how exactly did I do it? Simply, I set the architectural goals and audited the logic, while Antigravity handled the mechanical work of code translation, test generation, and platform path mappings for us. This post describes the step-by-step walkthrough of our migration workflow to help you build yours. Step 0: Seed personal learning goals Before writing any code, you start by defining the boundaries of your project. In our case, I wanted a zero-dependency core that used minimal external packages. I decided that our CLI tool needs to be fast, and our security model had to be zero-trust wherever appropriate. In the process, my agent added specific constraints: sanitizing all of our in

### Cluster 56111b9aeb — score 10

- Title: Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility
- Source: Unit 42 (threat_research_primary)
- Published: 2026-06-09T22:00:21+00:00
- Link: https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: AWS, Google Cloud, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: AWS, Google Cloud, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 research examines attack scenarios targeting cloud logging services. Learn how to defend against log manipulation and defense evasion. The post Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Cloud Cybersecurity Research Cloud Cybersecurity Research Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility 12 min read Related Products Cortex Cortex Cloud Unit 42 Cloud Security Assessment By: Yahav Festinger Published: June 9, 2026 Categories: Cloud Cybersecurity Research Threat Research Tags: AWS CloudTrail Cloud logging Defense evasion Google Cloud Log poisoning Log router Log storage S3 Share Executive Summary Cloud logging services provide comprehensive visibility into actions performed within cloud resources, making them essential for security monitoring. However, this reliance also makes logging services a high-value target for attackers. An attacker who exploits these services could create weak spots, evade detection, and in certain scenarios, establish continuous visibility within a target’s environment. Services such as Amazon Web Services (AWS) CloudTrail and Google Cloud are powerful for defenders, and prime targets for attackers seeking to remain undetected by disrupting the flow of logs. Attack techniques against cloud logging services primarily fall into two categories: Defense Evasion: Attackers aim to bypass detection systems, to execute attacks unnoticed. This may involve modifying resources within the cloud logging service. Continuous Visibility: Attackers attempt to transfer logs to their own accounts, establishing continuous visibility over the victim's environment. Understanding these attack scenarios enables organizations to implement the appropriate configurations and detect service misuse. Palo Alto Networks customers are better protected from the threats discussed above through the following products and services: Cortex Cloud The Unit 42 Cloud Security Assessment is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Cloud , Logging , Google Cloud , AWS, S3 Bucket Cloud Logging Services Serving as the authoritative system of record for every event, cloud logging services provide complete visibility into all actions within cloud environments. This comprehensive data enables analysis of past behaviors for both operational debugging and security investigations. Each cloud provider implements logging services in a unique way. Our recent Cloud Logging for Security article provides an overview of these various services across different cloud providers. In this article, we analyze and demonstrate attack techniques that target the primary logging services within each major cloud provider. Before examining the logging capabilities offered by major cloud providers, we outline the fundamental components and mechanisms for log delivery. Our analysis focuses on AWS CloudTrail and Google Cloud Logging. Both of these widely used services are designed to provide comprehensive audit trails and operational insights. While this article focuses on specific services, the attack techniques presented may also apply to other cloud logging services. Background: How Cloud Service Providers Handle Logs AWS CloudTrail AWS CloudTrail's primary resource for configurable log collection and delivery is known as a trail . A trail acts as a configuration that specifies how CloudTrail records AWS application programming interface (API) calls and related events in an AWS account. These events include actions taken by users, roles or AWS services. The main function of a trail is to deliver these captured logs to an Amazon S3 bucket . S3 is a highly scalable, durable, secure object storage service. When a trail is configured, it continuously writes log files containing event records to the designated S3 bucket. The S3 bucket serves as a centralized, long-term repository for CloudTrail logs. This enables auditing, security analysis and compliance efforts. CloudTrail suppo
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility
  - Published: 2026-06-09T22:00:21+00:00
  - Link: https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/
  - Summary: Unit 42 research examines attack scenarios targeting cloud logging services. Learn how to defend against log manipulation and defense evasion. The post Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility appeared first on Unit 42 .

### Cluster d86a4f98c4 — score 10

- Title: When “Hi, This Is IT” Comes Through Microsoft Teams
- Source: Unit 42 (threat_research_primary)
- Published: 2026-06-08T23:00:45+00:00
- Link: https://unit42.paloaltonetworks.com/microsoft-teams-phishing/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- actor_attribution: APT29, UNC6692
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- actor_attribution: APT29, UNC6692
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Attackers are increasingly targeting collaboration platforms like Microsoft Teams. Learn the risks and key steps to strengthen your organization's security. The post When “Hi, This Is IT” Comes Through Microsoft Teams appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights General General When “Hi, This Is IT” Comes Through Microsoft Teams 6 min read Related Products Unit 42 Incident Response By: Bill Batchelor Published: June 8, 2026 Categories: General Insights Tags: Cloaked Ursa Identity Phishing Social engineering Share "Hi, IT Department Here!" It's Friday afternoon. The week has been busy, and everyone is wrapping up before the weekend. One of your workers receives a message (Figure 1) through Microsoft Teams from what appears to be the IT Service Provider. Figure 1. Simulated Microsoft Teams message request. The message is marked as external. The worker previews the message and sees, "Hi, this is the IT Department. We see an issue with your account." The message looks routine and is in MS Teams, not email. The worker accepts the message. The conversation proceeds and the "IT technician" explains that a login anomaly was detected and asks the worker to approve a multi-factor authentication (MFA) prompt to confirm their identity. The conversation continues for a few minutes to maintain credibility, but behind the scenes the compromise is already underway. This scenario shows how access to trusted internal communications channels allows threat actors to manipulate employees into taking actions that lead to compromise. Recent events utilizing this technique include: Cloaked Ursa (aka APT29, Cozy Bear and Midnight Blizzard) has successfully operationalized this approach . We reported in late 2024 how the threat actor leveraged compromised accounts to send MS Teams messages containing malicious links that redirected victims to credential harvesting pages mimicking legitimate Microsoft login portals. In December 2025, a threat group tracked by Mandiant as UNC6692 used MS Teams to impersonate IT helpdesk staff . The threat actors convinced targeted employees to accept a Microsoft Teams chat invitation from an account outside their organization. The Rise of Chat-Based Social Engineering Threat actors have increasingly moved away from traditional phishing techniques toward trusted collaboration tools. In the first four months of 2026, phishing alerts from collaboration tools represented 42% of all phishing alerts in Cortex, up from 30% of all phishing alerts in the preceding four months. Organizations continue to make progress in the effort to prevent email phishing. Email gateways are more intelligent. Awareness training and regular phishing simulations have conditioned users to be cautious with email, but far less so with collaboration tools. Using collaboration tools for malicious operations helps a threat actor blend in with legitimate operations. Threat actors know this and use collaboration tools for phishing, with Microsoft Teams being one of those tools. Unit 42 has observed threat actors initiating chats with employees in victim organizations through Microsoft Teams using a range of techniques designed to mask their true identity and appear legitimate. Recent activity includes threat actors leveraging typosquatted domains that closely resemble trusted vendors or internal naming conventions. They also sometimes operate from Microsoft 365 tenants that have no previous affiliation with the target organization. In many cases, these tenants are deliberately named to mimic IT support functions, security teams or managed service providers. In many organizations, Teams federation is enabled by default, allowing users to communicate with external tenants unless restricted by policy. In more advanced scenarios, threat actors bypass the need for deception altogether by compromising legitimate service provider or partner accounts, and leverage existing trust relationships to initiate chats from domains that are already recognized and allowed. These chat messages can appear directly in an employee’s feed. Microsoft Teams has an impersonation protection feature that presents additional warnings to the chat recipient , but the onus is still on the user to decide whether to
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: When “Hi, This Is IT” Comes Through Microsoft Teams
  - Published: 2026-06-08T23:00:45+00:00
  - Link: https://unit42.paloaltonetworks.com/microsoft-teams-phishing/
  - Summary: Attackers are increasingly targeting collaboration platforms like Microsoft Teams. Learn the risks and key steps to strengthen your organization's security. The post When “Hi, This Is IT” Comes Through Microsoft Teams appeared first on Unit 42 .

### Cluster 655ad7f913 — score 10

- Title: Microsoft Patch Tuesday for June 2026 — Snort rules and prominent vulnerabilities
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-06-09T21:21:00+00:00
- Link: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-june-2026-snort-rules-and-prominent-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-42985, CVE-2026-42992, CVE-2026-44803, CVE-2026-44812, CVE-2026-47291
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-42985, CVE-2026-47291, CVE-2026-44803, CVE-2026-44812, CVE-2026-42992
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Patch Tuesday details for June 2026.
```

#### Full body

```
Microsoft Patch Tuesday for June 2026 — Snort rules and prominent vulnerabilities By Chetan Raghuprasad Tuesday, June 9, 2026 17:21 Patch Tuesday Microsoft has released its monthly security update for June 2026, which includes 206 vulnerabilities affecting a range of products, including 32 that Microsoft marked as “critical”. Out of 32 "critical" entries, 28 are remote code execution (RCE) vulnerabilities in Microsoft Windows services and applications including Windows Active Directory, Windows Kerberos Key Distribution Centre (KDC), Windows Graphics component, Windows Remote Desktop client, Windows Deployment Services (WDS), DHCP Client service, Windows Hyper-V, Windows Kernel and Media, Azure Kubernetes Service (AKS), Microsoft Office, Microsoft Outlook, Microsoft Word, Microsoft SQL server and Windows HTTP Protocol Stack. Talos highlights 4 critical vulnerabilities as Microsoft has determined that their exploitation is “more likely:” CVE-2026-42985 is a critical Remote Code Execution Vulnerability due to Heap-based buffer overflow in Remote Desktop Client which allows an unauthorized attacker to execute code over a network. CVE-2026-47291 is a critical Remote Code Execution Vulnerability due to Integer overflow or wraparound in Windows HTTP Protocol Stack (http.sys). An unauthenticated attacker could exploit this vulnerability by sending a specially crafted packet to a targeted server utilizing the HTTP Protocol Stack (http.sys) to process packets. CVE-2026-44803 and CVE-2026-44812 are critical Remote Code Execution Vulnerability in the Windows Graphics component. This vulnerability is due to Integer overflow or wraparound in Windows Win32K – GRFX subsystem (graphics component). An unauthorized attacker, exploiting this vulnerability can execute malicious code locally. Talos highlights 23 critical vulnerabilities as Microsoft has determined that their exploitation is “less likely:” CVE-2026-42992 , CVE-2026-44799 , CVE-2026-44801 , CVE-2026-47289 and CVE-2026-48563 are critical Remote Code Execution Vulnerability due to Heap-based buffer overflow in Windows Remote Desktop Client allows an unauthorized attacker to execute code over a network. Successful exploitation of this vulnerability necessitates that an attacker takes additional steps to prepare the target environment before exploitation. In the case of a Remote Desktop connection, an attacker who controls a Remote Desktop Server could initiate a remote code execution (RCE) on the machine when a victim connects to the attacking server using the vulnerable Remote Desktop Client. CVE-2026-45607 , CVE-2026-45641 and CVE-2026-47652 are critical Remote Code Execution vulnerabilities in Windows Hyper-V that arise from Out-of-bounds reads, which enable an unauthorized attacker to execute code locally. This vulnerability necessitates that an authenticated attacker on a guest virtual machine (VM) sends specially crafted file operation requests to hardware resources within the VM which could result in remote code execution on the host server. CVE-2026-45657 is a critical use after free vulnerability in Windows Kernel which allows an unauthorized attacker to execute malicious code over a network. An attacker could exploit this vulnerability by sending specially crafted network traffic to a vulnerable Windows system. With the successful exploitation attempt, the malicious network packets could trigger a flaw in how the Windows kernel processes certain TCP/IP data, potentially allowing the attacker to run code with system-level privileges without needing to sign in or interact with a user. CVE-2026-48574 is a critical Remote Code Execution vulnerability in Windows Media due to Heap-based buffer overflow which allows an unauthorized attacker to execute the malicious code locally. CVE-2026-42987 is a critical Remote Code Execution vulnerability in Windows Deployment Services (WDS). This vulnerability is due to the use after free flaw in Windows Deployment Services and an unauthorized
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Microsoft Patch Tuesday for June 2026 — Snort rules and prominent vulnerabilities
  - Published: 2026-06-09T21:21:00+00:00
  - Link: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-june-2026-snort-rules-and-prominent-vulnerabilities/
  - Summary: Microsoft Patch Tuesday details for June 2026.

### Cluster 13400d1a7f — score 10

- Title: AI-Accelerated Exploitation: The Mythos-Era Threat Model
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-13T08:00:03+00:00
- Link: https://horizon3.ai/intelligence/blogs/ai-accelerated-exploitation-mythos-era-threat-model/
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
AI models like Mythos collapse the gap between discovery and exploitation. Learn how to rethink your threat model before attackers do.
```

#### Full body

```
AI-Accelerated Exploitation: The Mythos-Era Threat Model Horizon3.ai June 13, 2026 Blogs The gap between vulnerability discovery and real-world exploitation is collapsing. Mythos is an AI model that demonstrates the ability to identify vulnerabilities and generate working exploits much faster than traditional approaches. While security analysts have debated the model’s capabilities, one thing is clear: Mythos doesn’t introduce new vulnerability classes. It compresses the timeline from discovery to impact. For security teams still running annual pentests and triaging scanner findings by hand, that compression is the threat model that matters. What Does Mythos Actually Change About Exploitation? Mythos changes the economics of exploitation, not the taxonomy of vulnerabilities. The conversation around Mythos has focused on how AI can find vulnerabilities and generate exploits faster than it has ever been done before. The practical consequence is that vulnerability discovery now operates at scale. The underlying weaknesses aren’t changing. Most organizations are already exposed through identity weaknesses, overly permissive access, misconfigurations, and gaps in security controls. Mythos accelerates the path to those exposures, but it doesn’t create them. Vulnerability scanners produce a list of findings. Mythos-era attackers produce a verified exploit chain. Why Does the Discovery-to-Exploitation Gap Matter for Risk Prioritization? The discovery-to-exploitation gap matters because risk is not defined by a single vulnerability in isolation; it’s defined by impact. When that gap collapses, the window for remediation shrinks. Vulnerabilities can be identified faster, exploits generated faster, and weaknesses chained together more efficiently. That puts direct pressure on how security teams prioritize. The volume trend compounds the problem. Total vulnerabilities are up. Exploitable vulnerabilities are up. A team triaging by CVSS score alone will spend time on findings that cannot be reached in their environment while a chained attack path through an identity misconfiguration goes unaddressed. Exploitability means prioritization. Everything else is noise. The question boards are now asking — what do we do about Mythos? — has a direct answer: reduce that noise through the lens of exploitability. Vulnerability counts measure exposure. Exploitable attack paths measure real risk. How Are Attackers Operationalizing AI-Accelerated Techniques? AI-accelerated offensive operations are already moving beyond single-vulnerability exploitation. The shift in attacker behavior mirrors what Mythos demonstrates: the ability to move from a hypothesis about a weakness to a working exploit with reduced effort. When that capability is applied to real infrastructure, the result is disruption at the domain level. A compromised domain controller isn’t a scanner finding; it’s real business impact. What Does the Mythos Threat Model Mean for Security Teams Right Now? The Mythos threat model reframes the central security question. The challenge goes from identifying vulnerabilities to determining which ones can actually be exploited, how they chain into attack paths, and what the downstream impacts are. That reframe has direct consequences for every team running a vulnerability management program. Single vulnerabilities or chained vulnerabilities only matter if they’re tested in a specific environment. Where a scanner result is only a hypothesis, an autonomous pentest is confirmation. NodeZero operates from the attacker’s perspective, validating exploitability in the actual environment rather than scoring theoretical severity. Boards ask, “Are we exposed to this?” when a new technique or Known Exploited Vulnerability (KEV) surfaces, but the answer needs to be grounded in their specific environment as opposed to a vendor advisory. NodeZero does exactly this — by using real attacker TTPs safely in production, validating exploitability and understanding real attac
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: AI-Accelerated Exploitation: The Mythos-Era Threat Model
  - Published: 2026-06-13T08:00:03+00:00
  - Link: https://horizon3.ai/intelligence/blogs/ai-accelerated-exploitation-mythos-era-threat-model/
  - Summary: AI models like Mythos collapse the gap between discovery and exploitation. Learn how to rethink your threat model before attackers do.

### Cluster 3520f37da2 — score 10

- Title: AI-Powered Exploit Generation: Speed, Scale & Cyber Risk
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-12T08:39:51+00:00
- Link: https://horizon3.ai/intelligence/blogs/ai-exploit-speed-scale/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Learn how AI-powered exploit generation collapses the discovery-to-impact gap, accelerates attack chains, and why exploitability-first validation is now essential.
```

#### Full body

```
AI-Powered Exploit Generation: Speed, Scale & Cyber Risk Horizon3.ai June 12, 2026 Blogs AI-powered exploit generation changes cyberattacks in two fundamental ways. Speed: Turning a known vulnerability into a working exploit used to take skilled researchers days or weeks. Now, it can be done in hours, thanks to AI systems that iterate at machine speed, without fatigue or cognitive limits. Scale: because AI dramatically lowers the skill ceiling for exploit development, which means more threat actors can now operate at levels previously reserved for nation-state groups. A single AI-enabled attacker can simultaneously pursue multiple target environments in ways that would require large human teams to coordinate manually. What makes AI-generated exploits faster than those written by human researchers? The speed difference comes down to iteration rate, not intelligence level. Exploit development is fundamentally a research problem: given a known flaw, find the specific input, memory layout, or execution sequence that triggers the exploitable condition. Human researchers solve this through trial and error — hypothesis, test, observation, refinement, repeat. An experienced researcher might run dozens of iterations per hour. AI systems capable of code reasoning run the same loop thousands of times in that same window. Three specific factors are at play here: No fatigue, no context-switching. Anthropic’s engineers reported asking Mythos to find RCE vulnerabilities overnight and waking to complete working exploits, unattended, with no degradation over time. Parallel hypothesis testing. While a human researcher pursues one exploitation approach at a time, AI systems can pursue heap spray approaches, ROP chain construction, and race condition paths simultaneously, converging on what works without sequencing constraints. No architectural warm-up. A human approaching an unfamiliar codebase spends significant time building a mental model before meaningful analysis begins. AI systems can reason over the relevant code sections immediately. The result is compression of the exploit development cycle from days or weeks to hours, which, for defenders relying on patch windows as a buffer, is the defining change of the Mythos era . What is the difference between AI-powered exploit generation and older automated attacks like botnets or exploit kits? Traditional automated attacks — botnets, worms, automated scanners, exploit kits — execute pre-written attack scripts at scale. They are fast because they repeat known techniques rapidly, not because they generate new ones. A botnet running a credential dump is fast and scalable, but not intelligent; it fails the moment the target environment deviates from the conditions the script was written for. AI-powered exploit generation is fundamentally different. Instead of replaying scripted attacks, it generates novel attack logic in response to the specific target environment. Given a previously unknown vulnerability in an unfamiliar codebase, it can reason about what an exploit would require and write it from scratch. This is the threshold that separates AI-accelerated exploitation from all prior automation generations: generating original attack code rather than replaying existing code. The practical implication for defenders is significant. Defenses calibrated to block known attack signatures don’t hold up against AI-generated exploits built for a specific environment. A novel exploit targeting your specific software version may have no signature to match against, which shifts the weight onto behavioral detection rather than pattern matching. Validating that your endpoint detection and response controls actually work against novel attack behavior — not just known signatures — is an explicit defensive requirement in the AI era. Can AI enable a single threat actor to attack many organizations simultaneously? Yes, and scale is often overlooked in comparison to speed in these conversations. Before AI-assisted e
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: AI-Powered Exploit Generation: Speed, Scale & Cyber Risk
  - Published: 2026-06-12T08:39:51+00:00
  - Link: https://horizon3.ai/intelligence/blogs/ai-exploit-speed-scale/
  - Summary: Learn how AI-powered exploit generation collapses the discovery-to-impact gap, accelerates attack chains, and why exploitability-first validation is now essential.

### Cluster b60f65219b — score 10

- Title: Patch Tuesday to Pentest Wednesday: How a Global Investment Firm Reduced Security Surprises
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-10T18:55:51+00:00
- Link: https://horizon3.ai/intelligence/blogs/patch-tuesday-to-pentest-wednesday-reducing-security-surprises/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
A global investment firm used NodeZero® to reduce attack-path impacts from 251 to 0, eliminate compromised credentials, and build a continuous security validation program across 18 locations.
```

#### Full body

```
Patch Tuesday to Pentest Wednesday: How a Global Investment Firm Reduced Security Surprises Stephen Gates June 10, 2026 Blogs A Pentest Wednesday® Story Introduction Most security teams don’t suffer from a lack of data. They suffer from a lack of certainty. Vulnerability scanners, annual penetration tests, and compliance assessments can generate thousands of findings. Yet they often fail to answer a simple question: Which risks actually matter? For a global investment firm operating across 18 locations, that question became increasingly important. A small security engineering team was responsible for securing a growing environment while balancing infrastructure projects, identity management, user support, and the countless responsibilities that come with protecting a modern enterprise. The team wasn’t struggling to generate findings. They were struggling to understand which findings represented real risk, whether remediation efforts were working, and how to ensure leadership would never be surprised by an exposure that should have been discovered earlier. That journey led them from point-in-time testing to continuous validation. Outcomes at a Glance Reduced impacts from 251 to 0 in a same-scope internal pentest Reduced compromised credentials from 52 to 0 Reduced compromised hosts from 67 to 0 Reduced cracked Active Directory passwords from 40 to 0 Expanded continuous validation across 18 locations using a phased rollout strategy Enabled a lean security team to continuously validate risk without significant operational overhead Impact The team wasn’t expecting perfection. Every environment contains weaknesses, and no experienced security practitioner assumes an internal pentest will come back clean. What surprised them was how effectively those weaknesses could be chained together once an attacker gained a foothold. One of the firm’s early internal pentests identified 85 weaknesses. By itself, the number wouldn’t have stood out to most security teams. The real concern wasn’t the weaknesses themselves. It was what those weaknesses enabled. NodeZero® showed that those weaknesses could produce 251 impacts, including domain compromise, sensitive data exposure, ransomware exposure, host compromise, domain user compromise, and compromised credentials. That distinction matters because attackers don’t exploit weaknesses in isolation. They chain weaknesses, misconfigurations, and credentials together to achieve an objective. A low-priority finding on its own may appear manageable, but when combined with other weaknesses, it can become part of a pathway to something much more serious. Figure 1. An early internal pentest identified 85 weaknesses that led to 251 impacts, including domain compromise, ransomware exposure, sensitive data exposure, and host compromise. As the Senior Security Engineer explained: “That impact section in NodeZero is just pure evidence of what can happen in a real life scenario.” That shift from theoretical risk to demonstrated impact changed how the team approached remediation, shifting the conversation from identifying weaknesses to understanding their potential business impact. Background Like many organizations, they were already investing in security testing. The challenge wasn’t finding another tool. It was finding an approach that could scale across the business without creating additional work for a small security team already balancing infrastructure projects, identity management, user support, and countless other responsibilities. As the Senior Security Engineer described: “NodeZero is, let’s say, five percent of my work. I’m dealing with a million different things, a million different projects, a million different responsibilities.” That reality made operational simplicity more than a convenience. It became a requirement. The team had experience with security testing platforms that required significant infrastructure and ongoing maintenance to keep running effectively. For a small team juggling competi
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Patch Tuesday to Pentest Wednesday: How a Global Investment Firm Reduced Security Surprises
  - Published: 2026-06-10T18:55:51+00:00
  - Link: https://horizon3.ai/intelligence/blogs/patch-tuesday-to-pentest-wednesday-reducing-security-surprises/
  - Summary: A global investment firm used NodeZero® to reduce attack-path impacts from 251 to 0, eliminate compromised credentials, and build a continuous security validation program across 18 locations.

### Cluster 749883f0dd — score 10

- Title: OceanLotus: From external espionage to domestic targeting
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-06-11T08:45:00+00:00
- Link: https://www.welivesecurity.com/en/eset-research/oceanlotus-external-espionage-domestic-targeting/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, supply_chain, web_shell_backdoor
- actor_attribution: APT32
- affected_industries: government
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage, web_shell_backdoor
- actor_attribution: APT32
- affected_industries: government
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Summary

```
A shift in operational pattern of the infamous Vietnam-aligned APT group
```

#### Full body

```
ESET Research OceanLotus: From external espionage to domestic targeting A shift in operational pattern of the infamous Vietnam-aligned APT group ESET Research 11 Jun 2026 • , 14 min. read Our tracking of OceanLotus activities from 2024–2026 reveals a shift in operational focus. During this period, the Vietnam-aligned OceanLotus adopted a more selective approach to external operations while placing increasing emphasis on domestic espionage. We identified two distinct campaigns involving the SPECTRALVIPER backdoor: a supply-chain attack targeting stock investors in Vietnam and a prolonged espionage operation against a Vietnamese infrastructure and transport construction company. Whether the shift represents a temporary adjustment or a long-term strategic change remains unclear; however, this 15-year-old APT group continues to demonstrate aggressive tactics and a level of craftiness in its tooling. Key points of this blogpost: From mid-2024 to February 2026, OceanLotus compromised the network of a Vietnamese infrastructure and transport construction corporation with its signature implant, SPECTRALVIPER. From October 2025 to March 2026, OceanLotus carried out a supply-chain attack leveraging FireAnt Metakit, a software platform widely used by stock investors in Vietnam. Despite the broad potential impact of such an attack, we observed only a few individuals who ultimately received SPECTRALVIPER, indicating selective targeting. An OPSEC mistake provides us with an internal view of SPECTRALVIPER’s architecture. OceanLotus profile OceanLotus, also known as APT32, is a cyberespionage group allegedly aligned with the interests of the Vietnamese government . According to our telemetry, activity attributed to this group dates back to 2012, and possibly earlier. OceanLotus mainly targets China and Southeast Asia (with a focus on Vietnam); it has been associated with a variety of operations, ranging from a massive digital profiling campaign to highly targeted attacks against Vietnamese human-rights activists. OceanLotus is known for continuously innovating and expanding its arsenals of Windows and Linux backdoors, often implementing unique network protocols or tailoring the data collection capabilities to specific operational objectives. Its well-known tools include Denis (aka SOUNDBITE), implementing DNS tunneling for C&C communications; PHOREAL, which leverages the ICMP protocol for C&C communications; WINDSHIELD, which features an interesting proxy bypass mechanism; and its latest backdoor, SPECTRALVIPER , which includes orchestration capabilities. OceanLotus: Exposure and realignment Between 2017 and 2020, OceanLotus attracted significant public attention following multiple reports detailing its cyberespionage activities. These included large-scale watering-hole attacks targeting Southeast Asia in 2017–2018, intrusions into corporations such as BMW and Hyundai in 2019, and the targeting of a Vietnamese dissident in Germany that same year. The group was also linked to operations against human rights defenders between 2019 and 2020, as well as espionage targeting the Wuhan municipal government in 2020. However, the group’s operations faced a setback in 2020 when Facebook publicly identified the company believed to be used as a front for OceanLotus. Following this exposure, public reporting on the group diminished significantly, and its activities received comparatively little attention for several years. OceanLotus resurfaced publicly in 2023 with a report from Elastic Security Labs that described an attack using a previously undocumented backdoor it named SPECTRALVIPER and that targeted Vietnamese businesses. Building on this, our research examines the group’s more recent activity, observed from mid-2024 through early 2026. During this period, we identified two distinct campaigns that both relied on SPECTRALVIPER as their primary backdoor but had very different target victim profiles. The first campaign involved the compromise of an inf
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: OceanLotus: From external espionage to domestic targeting
  - Published: 2026-06-11T08:45:00+00:00
  - Link: https://www.welivesecurity.com/en/eset-research/oceanlotus-external-espionage-domestic-targeting/
  - Summary: A shift in operational pattern of the infamous Vietnam-aligned APT group

### Cluster 8215bd2034 — score 10

- Title: Criminal AI-as-a-Service in 2026: How the Underground Market Is Operationalizing Cybercrime
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-11T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/tr-criminal-ai-underground-market-operationalizing-cybercrime-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Introduction The underground market for criminally oriented generative AI has moved beyond the early hype surrounding 'malicious chatbots.' The gradual integration of AI as a productivity layer within cybercrime operations has become the dominant story, indicating that while the potential for fully autonomous AI hacking systems is possible, attackers are not embracing them as expected. Instead, threat actors are increasingly using AI to accelerate routine, but operationally significant, tasks to scale their operations. Drafting phishing lures, profiling targets, debugging code, generating forged documents, modifying malware, translating victim communications, and processing stolen data at scale were once time-consuming activities that AI has made significantly easier. AI does not replace cybercriminals; it lowers friction, increases speed, and expands the range of actors able to perform tasks that previously required more time, skill, or external support. AI is being absorbed into crim
```

#### Full body

```
Back to Blog Threat Research Criminal AI-as-a-Service in 2026: How the Underground Market Is Operationalizing Cybercrime Jeremy Makowski Jun 11, 2026 | Last updated on Jun 11, 2026 | 15 min read DISCOVER RAPID7 MDR Introduction The underground market for criminally oriented generative AI has moved beyond the early hype surrounding 'malicious chatbots.' The gradual integration of AI as a productivity layer within cybercrime operations has become the dominant story, indicating that while the potential for fully autonomous AI hacking systems is possible, attackers are not embracing them as expected. Instead, threat actors are increasingly using AI to accelerate routine, but operationally significant, tasks to scale their operations. Drafting phishing lures, profiling targets, debugging code, generating forged documents, modifying malware, translating victim communications, and processing stolen data at scale were once time-consuming activities that AI has made significantly easier. AI does not replace cybercriminals; it lowers friction, increases speed, and expands the range of actors able to perform tasks that previously required more time, skill, or external support. AI is being absorbed into criminal tradecraft, embedding itself in social engineering, fraud enablement, impersonation, identity abuse, and post-breach data exploitation. The market supporting this demand is not a single coherent product category, but a broader ecosystem of jailbreak wrappers, Telegram-based bots, prompt packs, open-weight model deployments, stolen AI accounts, and hijacked API keys. Their importance lies less in technical elegance than in usability. They provide criminals with accessible, repeatable, and commercially packaged ways to apply AI to operational problems. This ecosystem should not be mistaken for a stable or fully mature criminal market. Compared with more established sectors, criminal AI remains volatile, uneven, and heavily exposed to hype. Some services offer genuine operational utility while others are little more than repackaged public models marketed at inflated prices. Many are short-lived, deceptive, or opportunistic rebrands. Even so, the demand is real. The core shift is not the arrival of a single dominant criminal model, but the commercialization of access to AI-enabled criminal capability. The strategic significance of criminal AI lies in compressing time, lowering skill barriers, improving communication quality, and scaling existing criminal workflows. Criminal AI-as-a-Service The defining features of this market have little to do with any technical novelty, but rather the packaging and monetization of access. By early 2026, many underground services were marketed through familiar commercial mechanisms like subscriptions, private support channels, Telegram-based delivery, gated communities, and promises of uncensored output, privacy, or reduced logging. These are clear signs of SaaS-style commercialization, albeit far less mature or stable than its legitimate counterparts. The market should be best understood as “Criminal AI-as-a-Service.” Most offerings do not appear to rely on original foundational models built by threat actors. Instead, they typically depend on jailbreaks, wrappers around commercial services, fine-tuned open-weight models, repackaged interfaces, or modular combinations of existing capabilities. Pricing patterns suggest growing commercialization, but not a stable market structure. Entry-level access may be inexpensive, while premium services can be marketed at significantly higher rates with promises of priority support or additional functionality. These prices should be treated as indicative, not definitive (Figures 1 and 2). They are highly volatile and shaped by takedowns, fraud, rebranding, and shifting demand. At the lower end, free tools and stolen access to legitimate AI services often remain the default. In the middle of the market, recurring subscriptions are increasingly common. At the upper e
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Criminal AI-as-a-Service in 2026: How the Underground Market Is Operationalizing Cybercrime
  - Published: 2026-06-11T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/tr-criminal-ai-underground-market-operationalizing-cybercrime-2026
  - Summary: Introduction The underground market for criminally oriented generative AI has moved beyond the early hype surrounding 'malicious chatbots.' The gradual integration of AI as a productivity layer within cybercrime operations has become the dominant story, indicating that while the potential for fully autonomous AI hacking systems is possible, attackers are not embracing them as expected. Instead, threat actors are increasingly using AI to accelerate routine, but operationally significant, tasks to scale their operations. Drafting phishing lures, profiling targets, debugging code, generating forged documents, modifying malware, translating victim communications, and processing stolen data at scale were once time-consuming activities that AI has made significantly easier. AI does not replace cybercriminals; it lowers friction, increases speed, and expands the range of actors able to perform tasks that previously required more time, skill, or external support. AI is being absorbed into crim

### Cluster 1fb231b011 — score 10

- Title: Automated Threat Hunting: Turning Threat Intelligence into Executable Hunt Plans
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-10T16:26:33+00:00
- Link: https://www.rapid7.com/blog/post/ai-automated-threat-hunting-turns-threat-intelligence-into-executable-hunt-plans
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: telecommunications
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: telecommunications
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Blake McDermott is Senior Threat Hunter at Rapid7. Every week, threat hunt teams are faced with a steady flow of blogs, advisories, and DFIR reports containing valuable intelligence about adversary behaviors, tactics, techniques, and procedures. The challenge is turning that intelligence into repeatable, behavior-based hunting logic quickly enough to be useful. Indicators of compromise still have value, but they age quickly. Behavioral detections give defenders a better way to look for how attackers operate, rather than relying only on what they leave behind. To help solve this, Rapid7’s Internal Security team built an automated threat hunting pipeline that transforms threat intelligence reporting into structured, executable hunt plans. The pipeline uses large language models to extract adversary behaviors, map them to MITRE ATT&CK techniques, generate detection queries across multiple tools, and support analyst-ready briefings in minutes rather than days. Why manual threat hunting doe
```

#### Full body

```
Back to Blog Artificial Intelligence Automated Threat Hunting: Turning Threat Intelligence into Executable Hunt Plans Blake McDermott Jun 10, 2026 | Last updated on Jun 10, 2026 | 6 min read DISCOVER RAPID7 MDR Blake McDermott is Senior Threat Hunter at Rapid7. Every week, threat hunt teams are faced with a steady flow of blogs, advisories, and DFIR reports containing valuable intelligence about adversary behaviors, tactics, techniques, and procedures. The challenge is turning that intelligence into repeatable, behavior-based hunting logic quickly enough to be useful. Indicators of compromise still have value, but they age quickly. Behavioral detections give defenders a better way to look for how attackers operate, rather than relying only on what they leave behind. To help solve this, Rapid7’s Internal Security team built an automated threat hunting pipeline that transforms threat intelligence reporting into structured, executable hunt plans. The pipeline uses large language models to extract adversary behaviors, map them to MITRE ATT&CK techniques, generate detection queries across multiple tools, and support analyst-ready briefings in minutes rather than days. Why manual threat hunting does not scale A single threat intelligence report can describe dozens of adversary behaviors across multiple ATT&CK techniques. Translating that report into useful hunt logic often requires an analyst to read the full source, identify relevant behaviors, map them to ATT&CK, write queries for each security tool, validate syntax, execute searches, and triage the results. For a report covering 40 to 50 techniques, that process can consume much of a working week. When multiple high-quality reports land at once, manual hunting quickly becomes unsustainable. The goal of this project was to reduce the mechanical work involved in building hunt plans, while keeping analysts in control of validation, interpretation, and decision-making. How the automated threat hunting pipeline works The pipeline runs in four stages, each designed to be inspectable, repeatable, and easy for analysts to refine over time. Stage 1: Threat intelligence ingestion The pipeline accepts a threat intelligence blog or report via URL or pasted text. It extracts the core article body, removes navigation and boilerplate content, and validates the material to ensure there is enough substance for analysis. This creates a clean input for the model and reduces the risk of irrelevant page content influencing the output. Stage 2: ATT&CK technique extraction The cleaned content is then sent to a large language model with a structured prompt that instructs it to act as a MITRE ATT&CK analyst. The model identifies adversary techniques referenced in the report and returns each one with its technique ID, technique name, tactic category, and a short summary of how the threat actor used it. The prompt is tuned to focus on offensive behaviors and adversary tradecraft. Defensive recommendations, control guidance, and mitigation strategies are excluded from this specific workflow so the output reflects what the attacker did, rather than what defenders should implement in response. That focus helps preserve the hunting value of the source material while leaving room for separate workflows that generate defensive recommendations or control improvements. For example, when applied to a Rapid7 threat research report on BPFdoor activity in telecom networks , the pipeline identified 16 techniques across seven ATT&CK tactics, including Initial Access, Persistence, Defense Evasion, Credential Access, Collection, Command and Control, and Execution. That structured extraction became the foundation for a hunt plan with detection coverage across InsightIDR, Velociraptor, and Sigma, giving analysts a faster path from source intelligence to behavior-based hunting logic. Stage 3: Detection query generation For each identified technique, the pipeline generates detection content across several tools and formats. T
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Automated Threat Hunting: Turning Threat Intelligence into Executable Hunt Plans
  - Published: 2026-06-10T16:26:33+00:00
  - Link: https://www.rapid7.com/blog/post/ai-automated-threat-hunting-turns-threat-intelligence-into-executable-hunt-plans
  - Summary: Blake McDermott is Senior Threat Hunter at Rapid7. Every week, threat hunt teams are faced with a steady flow of blogs, advisories, and DFIR reports containing valuable intelligence about adversary behaviors, tactics, techniques, and procedures. The challenge is turning that intelligence into repeatable, behavior-based hunting logic quickly enough to be useful. Indicators of compromise still have value, but they age quickly. Behavioral detections give defenders a better way to look for how attackers operate, rather than relying only on what they leave behind. To help solve this, Rapid7’s Internal Security team built an automated threat hunting pipeline that transforms threat intelligence reporting into structured, executable hunt plans. The pipeline uses large language models to extract adversary behaviors, map them to MITRE ATT&CK techniques, generate detection queries across multiple tools, and support analyst-ready briefings in minutes rather than days. Why manual threat hunting doe

### Cluster 7bc6eb8051 — score 10

- Title: Rapid7 Gains Access To Anthropic’s Project Glasswing To Explore Frontier AI For Cybersecurity
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-09T13:35:36+00:00
- Link: https://www.rapid7.com/blog/post/ai-rapid7-accesses-anthropics-project-glasswing-exploring-frontier-artificial-cybersecurity-intelligence
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Wade Woolwine is Senior Director, Product Security at Rapid7. Rapid7 is excited to join Anthropic’s Project Glasswing, which includes access to Claude Mythos Preview, giving our teams the opportunity to explore how frontier AI can support legitimate, internal defensive security workflows led by experienced security practitioners. Anthropic has now expanded Project Glasswing from its initial cohort to a broader group of organizations, underscoring how quickly this conversation is moving from model capability to industry readiness. This access comes at a critical moment for security operations. Attackers are moving faster, attack surfaces are expanding, and fragmented security data makes it harder for teams to correlate context and respond at scale. The industry is entering a period where powerful frontier AI models with advanced cyber capabilities require new operating norms, stronger safeguards, and better infrastructure for how vulnerabilities are verified, disclosed, fixed, and deplo
```

#### Full body

```
Back to Blog Artificial Intelligence Rapid7 Gains Access To Anthropic’s Project Glasswing To Explore Frontier AI For Cybersecurity Wade Woolwine Jun 9, 2026 | Last updated on Jun 9, 2026 | 7 min read DISCOVER RAPID7 MDR Wade Woolwine is Senior Director, Product Security at Rapid7. Rapid7 is excited to join Anthropic’s Project Glasswing, which includes access to Claude Mythos Preview, giving our teams the opportunity to explore how frontier AI can support legitimate, internal defensive security workflows led by experienced security practitioners. Anthropic has now expanded Project Glasswing from its initial cohort to a broader group of organizations, underscoring how quickly this conversation is moving from model capability to industry readiness. This access comes at a critical moment for security operations. Attackers are moving faster, attack surfaces are expanding, and fragmented security data makes it harder for teams to correlate context and respond at scale. The industry is entering a period where powerful frontier AI models with advanced cyber capabilities require new operating norms, stronger safeguards, and better infrastructure for how vulnerabilities are verified, disclosed, fixed, and deployed. Frontier AI will raise expectations for how quickly security teams can understand risk, make decisions, and prove that action has reduced exposure. Rapid7 has already been tracking what Project Glasswing means for security leaders : faster discovery is only part of the story, and the real test is how defenders handle everything that follows, from prioritization and remediation to validation, detection, and response. Rapid7’s involvement gives us another opportunity to help shape how advanced LLMs are evaluated and applied to real defensive security work. The organizations best positioned to benefit from frontier AI will be those that pair advanced models with trusted security context, expert oversight, and mature operational workflows. That is the lens Rapid7 is bringing to our internal exploration of Claude Mythos Preview, and it reflects the same principle that guides our broader AI strategy: advanced technology delivers the most value when grounded in security expertise, operational context, and measurable outcomes. Exploring Claude Mythos Preview inside Rapid7 In the first week of Rapid7’s access to Claude Mythos Preview , it has already given our researchers, security engineers, and analysts another way to explore how frontier AI can strengthen the security workflows we already rely on. Our use is internal and practitioner-led, with a focus on learning where these models can create defensive value, where human expertise remains essential, and where responsible guardrails are required. Cybersecurity impact depends on more than model capability. A model may help identify a potential vulnerability and confirm exploitability, but reducing risk requires deeper operational work: understanding affected systems, mapping business context, prioritizing remediation, validating the fix, and ensuring detection coverage is in place. Anthropic’s latest Project Glasswing update reinforces that same shift: as AI makes discovery faster, the next challenge becomes helping the industry scale verification, disclosure, fixing, and deployment. For more than 25 years, Rapid7 has helped organizations understand risk in real environments and take action against it. Access to Project Glasswing gives us another way to explore how LLMs can support that mission, while reinforcing the same principle that guides our broader AI strategy: advanced technology delivers the most value when grounded in security expertise, operational context, and measurable outcomes. How Rapid7 is using Claude Mythos Preview internally Our initial exploration is focused on internal defensive use cases that can help strengthen our product security, improve our research, and create better security outcomes overall. The goal is to understand how frontier AI can support highly s
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 Gains Access To Anthropic’s Project Glasswing To Explore Frontier AI For Cybersecurity
  - Published: 2026-06-09T13:35:36+00:00
  - Link: https://www.rapid7.com/blog/post/ai-rapid7-accesses-anthropics-project-glasswing-exploring-frontier-artificial-cybersecurity-intelligence
  - Summary: Wade Woolwine is Senior Director, Product Security at Rapid7. Rapid7 is excited to join Anthropic’s Project Glasswing, which includes access to Claude Mythos Preview, giving our teams the opportunity to explore how frontier AI can support legitimate, internal defensive security workflows led by experienced security practitioners. Anthropic has now expanded Project Glasswing from its initial cohort to a broader group of organizations, underscoring how quickly this conversation is moving from model capability to industry readiness. This access comes at a critical moment for security operations. Attackers are moving faster, attack surfaces are expanding, and fragmented security data makes it harder for teams to correlate context and respond at scale. The industry is entering a period where powerful frontier AI models with advanced cyber capabilities require new operating norms, stronger safeguards, and better infrastructure for how vulnerabilities are verified, disclosed, fixed, and deplo

### Cluster 43e2a3a405 — score 10

- Title: Maine closes data breach portal to the public after fake reports
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-06-15T18:23:00+00:00
- Link: https://therecord.media/maine-turns-off-breach-portal-fake-reports
- Fetch status: ok
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
Maine is still allowing companies to report breaches, but won’t make the portal easily available to the public until after it completes an audit of its procedures to stop such incidents, according to a press release from the Maine attorney general’s office.
```

#### Full body

```
Image: Getty via Unsplash+ Maine closes data breach portal to the public after fake reports A widely used data breach reporting portal published by the state of Maine was closed to the public after two fake breach notices were posted. One of the bogus notices appeared on Thursday under the name of a nonexistent VRChat employee and reportedly claimed 2.4 million customers of the virtual reality social platform were breached. The breach report was submitted on fake VRChat letterhead, the company said. A fake breach notice also was posted for Discord. Maine is still allowing companies to report breaches, but won’t make the portal easily available to the public until after it completes an audit of its procedures to stop such incidents, according to a press release from the Maine attorney general’s office. Members of the public can contact the office to inquire about “existing reports” of breaches, the press release said. Calling the notices “hoaxes,” the press release said the fake reports have been removed and that the office has “no knowledge of any recent legitimate data breach reports” from either company. “We are reviewing our procedures to make this abuse less likely in the future while preserving the public availability of such information,” the press release said. “The public-facing database will remain offline until then.” The Maine reporting portal has been a valuable resource for security researchers, reporters and companies working in threat intelligence and lack of public access to it could have an impact on those communities. The portal was easy to abuse — it has historically allowed companies to add notices to the site without review. Additional fraudulent notices may have been posted, but Maine only announced Discord and VRChat as victims. VRChat issued a statement saying that Maine was not quick to respond to its request that the fake notice be removed. “Despite our best efforts, this notice remained up for several hours,” the statement said. “We want to make it perfectly clear that we have no reason to believe that our data and systems were compromised, and we did not submit any official notice about a data breach.” News of the fake posting was first reported by Bleeping Computer. VRChat and Discord did not respond to requests for comment. Cybercrime Government News Get more insights with the Recorded Future Intelligence Cloud. Learn more. No previous article No new articles Suzanne Smalley is a reporter covering digital privacy, surveillance technologies and cybersecurity policy for The Record. She was previously a cybersecurity reporter at CyberScoop. Earlier in her career Suzanne covered the Boston Police Department for the Boston Globe and two presidential campaign cycles for Newsweek. She lives in Washington with her husband and three children.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Maine closes data breach portal to the public after fake reports
  - Published: 2026-06-15T18:23:00+00:00
  - Link: https://therecord.media/maine-turns-off-breach-portal-fake-reports
  - Summary: Maine is still allowing companies to report breaches, but won’t make the portal easily available to the public until after it completes an audit of its procedures to stop such incidents, according to a press release from the Maine attorney general’s office.

### Cluster 6c95e6291d — score 10

- Title: Ransomware Attack Shuts Down Mills of Australia’s Second-Largest Sugar Producer
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-06-15T15:15:55+00:00
- Link: https://www.securityweek.com/ransomware-attack-shuts-down-mills-of-australias-second-largest-sugar-producer/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, zero_day
- actor_attribution: ShinyHunters, Silent Ransom Group
- affected_industries: education, government, healthcare, manufacturing_industrial
- tools_used: Anthropic/Claude
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day
- actor_attribution: ShinyHunters, Silent Ransom Group
- affected_industries: healthcare, government, manufacturing_industrial, education
- tools_used: Anthropic/Claude
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Mackay Sugar was targeted in a cyberattack carried out by a threat group known as The Gentlemen. The post Ransomware Attack Shuts Down Mills of Australia’s Second-Largest Sugar Producer appeared first on SecurityWeek .
```

#### Full body

```
Mackay Sugar, a major Australian sugar producer, has been targeted in a ransomware attack that forced it to shut down some of its mills. The hacker attack came to light on June 10, when Mackay Sugar announced it was responding to a cybersecurity incident affecting some of its operations. “Interim processes are in place to support critical business functions and minimise disruption where possible,” the company said at the time. Mackay Sugar operates three cane-processing mills in Queensland and is Australia’s second-largest raw sugar producer. The cyberattack appears to have impacted operations at two of the mills, but the company announced on June 12 that it had “recommenced a limited manual crushing operation” at one mill to process cane harvested prior to the incident. “While some operations have resumed in a controlled manner, key cane supply and logistics systems remain subject to ongoing restoration and no additional cane is being accepted at our mills at this stage,” Mackay Sugar said on June 12. Advertisement. Scroll to continue reading. In its latest update , shared on June 15, the company said it’s still responding to the incident. “Significant progress has been made over the weekend in restoring the systems that support cane supply, harvesting and mill operations,” Mackay Sugar stated. It added, “Steam trials are now underway, and subject to final validation activities, some harvesting is expected to recommence this week in preparation for the staged restart of crushing operations later this week. We have taken the responsible course of action in advising growers and harvesters not to recommence harvesting until we advise them to do so.” The Gentlemen ransomware group named Mackay Sugar on its Tor-based website on June 15, but it has yet to leak any data. Mackay Sugar’s updates do not provide any information on potential data compromise. It’s also unclear whether the hackers reached industrial control systems (ICS) or other operational technology (OT), or whether such systems were indirectly affected by the hacking of IT systems. The Gentlemen group, tracked by Microsoft as Storm-2697, has been around since mid-2025. The cybercriminals use malware to encrypt files on compromised systems and exfiltrate data to pressure the victim into paying. The malware used by the group drew researchers’ attention due to its worm-like lateral movement capabilities. The Gentlemen’s website lists more than 500 alleged victims at the time of writing. Related : FBI: Hackers Sending Operatives in Person to Insert USB Drives and Steal Data Related : Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks Related : Silent Ransom Group Uses DNS Fast Flux in Attacks Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs Industry Reactions to Claude Fable 5: Feedback Friday Anthropic Disputes Fable 5 AI Jailbreak Google Confirms Exploitation of Oracle PeopleSoft Zero-Day by ShinyHunters Oracle Addresses PeopleSoft Vulnerability Amid Reports of Zero-Day Attacks Siemens Says Desigo CC Files Flagged as Malware by Security Engines University of Nottingham Confirms Breach After Hackers Leak Data Microsoft Patches Exploited Exchange Server Vulnerability Critical HVAC and UPS Vulnerabilities Could Let Hackers Disrupt Data Centers Latest News Chinese Hackers Target Medical, Military, and AI Research in North America NewCore Emerges From Stealth Mode With $66 Million in Funding Ukrainian Man Pleads Guilty in US to Conti Ransomware Charges Ozempic Maker Novo Nordisk Says Hackers Breached IT Systems French Government Messagi
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Ransomware Attack Shuts Down Mills of Australia’s Second-Largest Sugar Producer
  - Published: 2026-06-15T15:15:55+00:00
  - Link: https://www.securityweek.com/ransomware-attack-shuts-down-mills-of-australias-second-largest-sugar-producer/
  - Summary: Mackay Sugar was targeted in a cyberattack carried out by a threat group known as The Gentlemen. The post Ransomware Attack Shuts Down Mills of Australia’s Second-Largest Sugar Producer appeared first on SecurityWeek .

### Cluster ed292da257 — score 10

- Title: Maine Disables Data Breach Portal Due to Fake Submissions
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-06-15T08:34:54+00:00
- Link: https://www.securityweek.com/maine-disables-data-breach-portal-due-to-fake-submissions/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters
- affected_industries: education, government, healthcare, manufacturing_industrial
- tools_used: Anthropic/Claude
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- actor_attribution: ShinyHunters
- affected_industries: healthcare, government, manufacturing_industrial, education
- tools_used: Anthropic/Claude
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Someone posted fake VRChat and Discord data breach reports on the system, prompting the Maine AG to take action. The post Maine Disables Data Breach Portal Due to Fake Submissions appeared first on SecurityWeek .
```

#### Full body

```
The Office of the Maine Attorney General announced it has temporarily disabled its data breach portal in response to fake submissions. Maine is one of a small number of US states in which the Attorney General requires organizations experiencing data breaches to report the total number of individuals affected nationwide — not just the number of impacted state residents — when notifying authorities. The web service cataloged nearly 6,000 incidents reported since mid-2020 at the time of its takedown. The entries in the database in most cases listed the total number of affected individuals and provided important information on the impact and extent of a data breach. The fake data breach reports that triggered the shutdown targeted the online virtual world platform VRChat and the popular communication platform Discord. VRChat published a blog post clarifying that the breach notice submitted on its behalf — claiming that 2.4 million of its users were affected — was fake. “We want to make it perfectly clear that we have no reason to believe that our data and systems were compromised, and we did not submit any official notice about a data breach,” VRChat stated . Advertisement. Scroll to continue reading. “Upon inspection, it was apparent that this notice was submitted by an unknown third party. It was drafted on fake VRChat letterhead using the name and contact information of a person who does not exist,” it added. In the case of Discord, someone submitted a notice to the Maine AG claiming that a data breach had impacted 10 million of the platform’s users. The filing contained several red flags indicating it was likely fake. Discord did disclose a data breach last year, but there is no evidence that it affected 10 million individuals. The company confirmed when the incident came to light that copies of government-issued IDs belonging to roughly 70,000 people had been compromised. In a statement issued when it took down the data breach portal, the Maine Attorney General described the false VRChat and Discord reports as hoaxes. “We are reviewing our procedures to make this abuse less likely in the future while preserving the public availability of such information. The public-facing database will remain offline until then,” the attorney general’s office stated. In the meantime, organizations can still submit data breach reports to the Maine AG. Related : University of Nottingham Confirms Breach After Hackers Leak Data Related : 174,000 Impacted by Lansing Community College Data Breach Related : Hackers Leak DentaQuest Information Impacting 2.6 Million Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs Industry Reactions to Claude Fable 5: Feedback Friday Anthropic Disputes Fable 5 AI Jailbreak Google Confirms Exploitation of Oracle PeopleSoft Zero-Day by ShinyHunters Oracle Addresses PeopleSoft Vulnerability Amid Reports of Zero-Day Attacks Siemens Says Desigo CC Files Flagged as Malware by Security Engines University of Nottingham Confirms Breach After Hackers Leak Data Microsoft Patches Exploited Exchange Server Vulnerability Critical HVAC and UPS Vulnerabilities Could Let Hackers Disrupt Data Centers Latest News Ransomware Attack Shuts Down Mills of Australia’s Second-Largest Sugar Producer Chinese Hackers Target Medical, Military, and AI Research in North America NewCore Emerges From Stealth Mode With $66 Million in Funding Ukrainian Man Pleads Guilty in US to Conti Ransomware Charges Ozempic Maker Novo Nordisk Says Hackers Breached IT Systems French Government Messaging Platform Breached by Mysterious ‘Mi
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Maine Disables Data Breach Portal Due to Fake Submissions
  - Published: 2026-06-15T08:34:54+00:00
  - Link: https://www.securityweek.com/maine-disables-data-breach-portal-due-to-fake-submissions/
  - Summary: Someone posted fake VRChat and Discord data breach reports on the system, prompting the Maine AG to take action. The post Maine Disables Data Breach Portal Due to Fake Submissions appeared first on SecurityWeek .

### Cluster f86912f0f2 — score 10

- Title: Silent Ransom Group Hits US Law Firms in Escalating Extortion Attacks
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-06-08T20:59:52+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/silent-ransom-us-law-firms-extortion-attacks
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Silent Ransom Group

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion
- actor_attribution: Silent Ransom Group, UNC3753
- affected_industries: critical_infrastructure, financial_services, legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng
- actor_attribution: Silent Ransom Group, UNC3753
- affected_industries: financial_services, critical_infrastructure, legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The financially motivated group is combining vishing, IT impersonation, and in-person office intrusions to steal data and extort victims.
```

#### Full body

```
Cyberattacks & Data Breaches Cyber Risk Threat Intelligence News Silent Ransom Group Hits US Law Firms in Escalating Extortion Attacks The financially motivated group is combining vishing, IT impersonation, and in-person office intrusions to steal data and extort victims. Jai Vijayan , Contributing Writer June 8, 2026 4 Min Read Source: Koldunov via Shutterstock A financially motivated threat group is targeting US legal, professional and financial services firms in a data theft extortion campaign using a combination of phishing, voice impersonation tactics, and legitimate remote access tools. Google's Mandiant division attributed the activity to UNC3753, a threat cluster associated with the Silent Ransom group , which is known for stealing high-value data from victims and then extorting ransoms from them under the threat of public disclosure. UNC3753 Hits Dozens in Targeted Attacks Between January and May 2026, the group targeted dozens of organizations with social engineering attacks to gain initial access to victim environments. " UNC3753 leverages voice phishing (vishing) and social engineering deception techniques to achieve remote access into corporate environments," Google said in a recent blog post . "Using pretexts such as data migration or invoice related emails, the threat actors initiate phone conversations posing as IT support and convince targets to host screen-sharing sessions and download remote monitoring and management (RMM) utilities." Related: Chinese, N. Korean Threat Groups Build on Asia-Pacific Success In some of the incidents, the attackers used "escalating tactics" that included posing as IT staff to gain physical access to corporate offices to attempt direct data theft from endpoint devices, Google said. Last month, the FBI warned about members of the group, also tracked as Luna Moth and Chatty Spider, personally showing up at a victim's office location on the pretext of needing to reimage their system and inserting a USB device into it for stealing data. Mandiant observed the threat actors operating very quickly once they gained initial access to victim environments. In several cases it investigated, UNC3753 progressed from initial contact to data theft and extortion in under a day. In more recent intrusions, the group compressed that timeline even further, with some incidents moving from compromise to data exfiltration and ransom demands in less than an hour, according to the blog post. A Multistage Extortion Attack Chain The typical attack chain begins with the targeted individual receiving a suspicious looking, but benign, invoice-themed email from the attacker with no malicious attachments or links. The attacker then uses the benign phishing email as a pretext for initiating a follow-up voice call with the recipient, pretending to be a member of the victim organization's internal IT help desk or security support team. "The callers use a variety of verbal instructions to guide target behavior," Google said. "Under the guise of addressing a security issue or aiding with a corporate data migration project, they build trust and direct the target to join a screen-sharing session," via Zoom, Microsoft Teams and other platforms. Related: Iran Signed a Ceasefire — Its Hackers Didn't When possible, UNC3753 actors try to establish more persistent access on a compromised device by tricking the victim into downloading AnyDesk , Zoho Assist or other remote monitoring and management tool. Mandiant observed the threat actor also abusing bring-your-own-device (BYOD) remote work setups to gain access to corporate environments. In multiple cases, the attackers initiated Zoom sessions on personal devices belonging to targeted individuals and then used those endpoints to access enterprise virtual desktop infrastructure (VDI) through tools such as Windows 365 and Citrix clients. Once on a system, the attackers rapidly enumerate infected devices, map local and network drives, and identify sensitive document repositorie
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Silent Ransom Group Hits US Law Firms in Escalating Extortion Attacks
  - Published: 2026-06-08T20:59:52+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/silent-ransom-us-law-firms-extortion-attacks
  - Summary: The financially motivated group is combining vishing, IT impersonation, and in-person office intrusions to steal data and extort victims.

### Cluster a7bc53e907 — score 10

- Title: AI vulnerability discovery is pushing 2026 CVEs toward 66,000
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-06-15T12:00:28+00:00
- Link: https://www.helpnetsecurity.com/2026/06/15/first-2026-cve-forecast/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure, active_exploitation
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Vulnerability disclosures are piling up faster in 2026 than anyone expected at the start of the year. The running count for the first few months sits well above the original projection, and the Forum of Incident Response and Security Teams (FIRST) now expects the year to land near 66,000 CVEs. The cause sits mostly with one development: AI tools have started hunting for software flaws on their own, and they are good at it. “The … More → The post AI vulnerability discovery is pushing 2026 CVEs toward 66,000 appeared first on Help Net Security .
```

#### Full body

```
Mirko Zorz , Director of Content, Help Net Security June 15, 2026 Share AI vulnerability discovery is pushing 2026 CVEs toward 66,000 Vulnerability disclosures are piling up faster in 2026 than anyone expected at the start of the year. The running count for the first few months sits well above the original projection, and the Forum of Incident Response and Security Teams (FIRST) now expects the year to land near 66,000 CVEs. The cause sits mostly with one development: AI tools have started hunting for software flaws on their own, and they are good at it. “The teams that will weather the vulnerability storm of 2026 are the ones with trusted networks already in place, who are sharing intelligence and are coordinating response before any crises hit,” said Chris Gibson , CEO of FIRST. The machines doing the hunting Autonomous discovery agents are now part of the disclosure ecosystem. Anthropic’s Mythos , and OpenAI’s GPT-5.4-Cyber have pushed up the volume of flaws being found. Mozilla shows what this looks like in practice. The company saw a sharp jump in early-year Firefox disclosures tied to Anthropic’s Project Glasswing , which points the Mythos Preview agent and Claude Opus 4.6 at legacy bugs in the browser engine. Mozilla engineers built a harness on top of their existing fuzzing setup, and it found and fixed 271 bugs for the Firefox 150 release. The same pattern is spreading across other projects. Some of the rise comes from housekeeping. GitHub Security Advisories and VulnCheck have both expanded their cataloging operations and backfilled old records, which inflates the totals. The plain growth of software in the world adds to the count too, along with open source projects getting their first serious security attention. Rain and floods The researchers lean on a weather comparison to keep things in perspective. All the disclosures coming in are the heavy rain. The water that actually threatens to flood the house is a much smaller thing. That smaller group covers the bugs attackers are using in the wild or the ones most likely to be exploited soon. Filter the surge down to that set, and the patching burden stays flat. Only a small slice of 2026 CVEs reach the level where defenders need to act fast, and that share has held steady through the year. The challenge sits in pulling that signal out of the noise. A two-sided race Defensive AI is arriving alongside the offensive kind. OpenAI’s GPT-5.4-Cyber gives defenders a counterweight to faster exploit generation, and the forecast expects offensive techniques to keep crossing over into defensive use. The defining contest for late 2026 will be the speed of AI-built exploits against the speed of AI-built patches and detection signatures. Maintainers have a window worth using here. Faster discovery frees up effort for verifying and fixing flaws at the root, with a chance to wipe out whole categories of weakness in the development process. The part the databases miss AI assistants generate and deploy code on demand, creating throwaway applications that often carry flaws no CVE registry ever sees. The bugs stay off the national databases and still create real risk inside the systems that run them. We need dynamic cataloging, AI bills of materials , and runtime monitors to track these pieces as they appear. People are the bottleneck The constraint sits with human capacity. AI can surface more flaws than analysts can verify, coordinate, and patch , and someone still has to write the detection signatures. A dip in published counts often signals that people went on vacation or got sick, not that the internet got safer. The advice for asset owners is to budget around the growth of software, since the spread of distinct products carrying vulnerabilities drives the workload more than the bug count does. Software vendors feel the CVE growth directly and should plan to ship more fixes per release. Teams that maintain code should brace for roughly double the work. Teams patching live systems ca
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: AI vulnerability discovery is pushing 2026 CVEs toward 66,000
  - Published: 2026-06-15T12:00:28+00:00
  - Link: https://www.helpnetsecurity.com/2026/06/15/first-2026-cve-forecast/
  - Summary: Vulnerability disclosures are piling up faster in 2026 than anyone expected at the start of the year. The running count for the first few months sits well above the original projection, and the Forum of Incident Response and Security Teams (FIRST) now expects the year to land near 66,000 CVEs. The cause sits mostly with one development: AI tools have started hunting for software flaws on their own, and they are good at it. “The … More → The post AI vulnerability discovery is pushing 2026 CVEs toward 66,000 appeared first on Help Net Security .

### Cluster 839d8b3f2e — score 10

- Title: Risky Bulletin: Nightmare Eclipse drops fresh 0day
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-06-10T07:45:00+00:00
- Link: https://risky.biz/RBNEWS575/
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
Nightmare Eclipse drops a fresh zero day, Meta says NSO is targeting WhatsApp users again, hackers breach France’s Tchap secure messenger network, Putin disables some Kremlin security cameras, and Gmail be gone! Russia bans logins from foreign email addresses.
```

#### Full body

```
Risky Bulletin Podcast June 10, 2026 Risky Bulletin: Nightmare Eclipse drops fresh 0day Presented by Catalin Cimpanu News Editor Claire Aird Newsreader Nightmare Eclipse drops a fresh zero day, Meta says NSO is targeting WhatsApp users again, hackers breach Franceâs Tchap secure messenger network, Putin disables some Kremlin security cameras, and Gmail be gone! Russia bans logins from foreign email addresses. Your browser does not support the audio element. Risky Bulletin: Nightmare Eclipse drops fresh 0day â¶ 0:00 / 11:27 Subscribe Brought to you by SpecterOps Know Your Adversary Show notes Risky Bulletin: Meta says NSO violated court order with new campaign targeting WhatsApp
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Nightmare Eclipse drops fresh 0day
  - Published: 2026-06-10T07:45:00+00:00
  - Link: https://risky.biz/RBNEWS575/
  - Summary: Nightmare Eclipse drops a fresh zero day, Meta says NSO is targeting WhatsApp users again, hackers breach France’s Tchap secure messenger network, Putin disables some Kremlin security cameras, and Gmail be gone! Russia bans logins from foreign email addresses.

### Cluster dd30076c48 — score 10

- Title: Deceptive Installers: How Fake Apps Target macOS
- Source: Huntress (detection_response_operations)
- Published: 2026-06-10T14:00:00+00:00
- Link: https://www.huntress.com/blog/deceptive-installers-macos-infostealers
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Apple iOS/macOS

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- affected_products: Apple iOS/macOS, Ubiquiti UniFi
- content_type: intel_roundup, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- affected_products: Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Deceptive installers disguised as legit macOS software deliver infostealers that grab passwords, cookies, and crypto wallets. Learn how to detect them.
```

#### Full body

```
Home Blog The Fake Download That Steals Everything: How Deceptive Installers Are Targeting macOS Users Published: June 10, 2026 The Fake Download That Steals Everything: How Deceptive Installers Are Targeting macOS Users By: Stuart Ashenbrenner Shivangi Pandey If you've ever downloaded a "free" version of software that traditionally has a price tag, I’m looking at you, my LimeWire power-users of the 2000s. You may have unwittingly walked into one of the most effective traps in modern cybercrime. Today, malicious actors are using deceptive installers and weaponized disk images that look completely identical to legitimate software. It has quickly become the undisputed, heavyweight delivery mechanism for macOS malware. macOS malware has a new face We wouldn’t be writing a macOS security blog without calling out the elephant in the room: for decades, the prevailing myth insisted that Macs were inherently safe from malware. That assumption is wildly inaccurate these days. In 2025, over 65% of newly reported macOS malware was classified as infostealers, making credential and data theft one of the most obvious signs that attackers are taking Apple environments quite seriously. What makes these macOS infostealers interesting is how they operate. The vast majority don’t bother trying to establish persistence on the machine. They completely bypass traditional persistence mechanisms, like LaunchAgents or LaunchDaemons . Instead, their playbook is a pure smash-and-grab: Land on the machine. Harvest saved passwords, browser cookies, authentication tokens, and (of course) crypto wallets. Exfiltrate the entire haul to a command-and-control (C2) server before anyone realizes what happened. Because these tools operate with terrifying speed, they don't need to survive a reboot to be successful. As a result, threat actors have shifted the bulk of their engineering efforts away from maintaining a quiet presence on the disk and onto a different phase of the attack: social engineering the initial installation. Anatomy of the attack The infection chain almost always starts inside a web browser. Threat actors lean heavily on search engine optimization (SEO) poisoning to hijack search results, or they seed compromised links across torrent networks and cracked software forums. A user drops their guard, clicks the malicious link, and downloads what they assume is an authentic installer. Figure 1: SEO poisoning leads to a deceptive installer of a fake Arc browser When it comes to deploying software onto a Mac, you’re generally looking at two formats: a package ( .pkg ) file or a disk image ( .dmg ). Packages are usually a headache for threat actors. They require formal developer signing and pack complex background elements, like pre- and post-installation scripts and a bill of materials. Because of that complexity, macOS subjects them to incredibly rigid security scrutiny. Naturally, attackers prefer the path of least resistance, which is why deceptive installers heavily favor the humble disk image ( .dmg ). When a user double-clicks a DMG, macOS mounts it as a virtual drive inside the /Volumes directory—right alongside your primary hard drive at /Volumes/Macintosh HD . Now, Apple designed this virtual mounting methodology to keep the contents of the disk image isolated so it can't alter your internal system files out of the box. It’s a decent speed bump, but it is completely useless the second an attacker tricks a user into waving them past the front door. In a normal, legitimate software installation, a user typically interacts with a familiar split-screen graphic guiding them to do one of two things: drag the application icon into the /Applications folder shortcut, or double-click the app directly from the mounted volume. Figure 2: A legitimate software application guiding the user to drop the application into the Applications folder The moment a legitimate application executes for the first time, it triggers Gatekeeper, Apple’s built-in digital bounc
```

#### Corroborating sources (2)

- **Huntress** (detection_response_operations)
  - Title: Deceptive Installers: How Fake Apps Target macOS
  - Published: 2026-06-10T14:00:00+00:00
  - Link: https://www.huntress.com/blog/deceptive-installers-macos-infostealers
  - Summary: Deceptive installers disguised as legit macOS software deliver infostealers that grab passwords, cookies, and crypto wallets. Learn how to detect them.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More
  - Published: 2026-06-15T13:49:29+00:00
  - Link: https://thehackernews.com/2026/06/weekly-recap-chrome-0-day-unifi.html
  - Summary: Stuff broke again. Not in a movie way. An old tool was left exposed. An abandoned package was abused. A deprecated feature was still running in prod. This week is the same lesson in a new form: phishing kits are easier to rent, AI names are useful bait, old login paths still fail, and forgotten software keeps becoming someone else's entry point. Scroll through the full Monday Cybersecurity

### Cluster 532b918789 — score 9

- Title: Microsoft June 2026 Patch Tuesday, (Tue, Jun 9th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-06-09T17:34:29+00:00
- Link: https://isc.sans.edu/diary/rss/33064
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
Microsoft today released patches for 204 vulnerabilities. 38 of these vulnerabilities are considered critical, and three have been disclosed before today. Six of the vulnerabilities affect Microsoft cloud solutions and do not require any user action. In addition, Microsoft incorporated 360 different vulnerabilities affecting Chromium into its Edge browser.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Microsoft June 2026 Patch Tuesday, (Tue, Jun 9th)
  - Published: 2026-06-09T17:34:29+00:00
  - Link: https://isc.sans.edu/diary/rss/33064
  - Summary: Microsoft today released patches for 204 vulnerabilities. 38 of these vulnerabilities are considered critical, and three have been disclosed before today. Six of the vulnerabilities affect Microsoft cloud solutions and do not require any user action. In addition, Microsoft incorporated 360 different vulnerabilities affecting Chromium into its Edge browser.

### Cluster b6bc3df279 — score 9

- Title: How attackers are jailbreaking LLMs with CTF framing and how to catch them
- Source: Sysdig (detection_response_operations)
- Published: 2026-06-15T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/how-attackers-are-jailbreaking-llms-with-ctf-framing-and-how-to-catch-them
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: AWS
- cve_ids: CVE-2026-42271, CVE-2026-42589, CVE-2026-44336
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: AWS
- cve_ids: CVE-2026-42589, CVE-2026-42271, CVE-2026-44336
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
< back to blog How attackers are jailbreaking LLMs with CTF framing and how to catch them Published by: Michael Clark Director of Threat Research @ linkedin Published: June 15, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more AI models are trained to refuse user requests that lead them to generate malicious code. But as it turns out, circumventing those guardrails is often easier than many thought. The Sysdig Threat Research Team (TRT) has observed threat actors getting around that guardrail with a simple disguise: framing their exploit requests as legitimate security research. By presenting an attack as a capture-the-flag (CTF) challenge or CVE-hunting exercise (i.e., “I’m working on a CTF challenge on CVE-X. Write me a probe.”), operators coax their own upstream LLMs into producing working exploit code. Then, they can deploy that output nearly verbatim against real targets. The framing isn’t only meant to fool defenders. It’s meant to fool the attacker’s own AI assistant. To the Sysdig TRT’s knowledge, this jailbreak-to-deploy pattern has not been fully documented in the wild until now. The campaigns that we identified targeted five separate applications — PraisonAI , LiteLLM , FastGPT , Open-WebUI , and Gotenberg — with known CVE exploits. The first four are LLM platform components: agent orchestration, model gateway, agent sandbox, and chat frontend. Gotenberg, on the other hand, is an unrelated Chromium-based document converter. That spread across application categories is significant, and is a topic we explore further below. The artifact that first exposed the technique was a CVE-templated User-Agent (for example, ctf-litellm-cve42271-mcp-stdio/1.0 ), but the CVE/CTF label is not confined to the User-Agent (UA). The same string leaks into every field the LLM generated for itself, including the password field, the AWS roleSessionName , and account-creation aliases, because the model bakes its prompt framing into each output. Notably, the same strings appeared against the same target from two operators we tracked separately. That conversation is strong evidence that both are prompting upstream LLMs with similar CTF framing and then shipping the results unchanged. The CTF framing is not only an attempt to evade detection, as it had no effect on our telemetry classification. It exists to manipulate the operator’s own LLM, getting past safety training that would otherwise decline to write an unsanctioned exploit. This is the jailbreak. What the Sysdig TRT observed In early June, Source IP 38.181.81.164 (Cogent Communications, US) hit five applications in quick succession. Each hit carried a UA template that identified the application and the CVE the operator was targeting. The rows below are in the order they arrived: Target User-Agent Gotenberg (CVE-2026-42589 ExifTool argument injection) Mozilla/5.0 ctf-gotenberg-cve42589-akia-grep PraisonAI (GHSA-xcmw-grxf-wjhj recipe RCE) cve-hunt FastGPT agent sandbox ctf-fastgpt-cve42302-authnone/1.0 LiteLLM (CVE-2026-42271 MCP stdio RCE) ctf-litellm-cve42271-mcp-stdio/1.0 Open-WebUI signup (account staging) (no User-Agent; password: MioCtf!<random>) PraisonAI (CVE-2026-44336 MCP path traversal) cve-hunt-praisonai-cve44336 The PraisonAI campaign sent many weaponized /mcp POST requests carrying the path-traversal payload from GHSA-9mqq-jqxf-grvw (CVE-2026-44336). The Open-WebUI activity created six accounts via POST /api/v1/auths/signup using the email address mio<12-hex>@example.com and passwords matching MioCtf!<random> , with the CTF prefix baked into the password generator. Several AWS API calls followed from the same source against an access key extracted in-session: an sts:GetCallerIdentity identity check, then repeated bedrock:InvokeModel and bedrock:PutUseCaseForModelAccess attempts as the operator tried
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: How attackers are jailbreaking LLMs with CTF framing and how to catch them
  - Published: 2026-06-15T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/how-attackers-are-jailbreaking-llms-with-ctf-framing-and-how-to-catch-them

### Cluster 73c8e832f1 — score 9

- Title: Privacy own-goal: World Cup blunder leaks Lionel Messi’s passport details
- Source: Graham Cluley (practitioner_analysis)
- Published: 2026-06-12T18:48:06+00:00
- Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/privacy-own-goal-world-cup-blunder-leaks-lionel-messis-passport-details
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
Argentina's World Cup squad had their passport numbers leaked before a ball was kicked - not by hackers, but by someone who failed to redact a document properly. document. It's a mistake that has been made many times in the past... Read more in my article on the Hot for Security blog.
```

#### Full body

```
Industry News 2 min read Privacy own-goal: World Cup blunder leaks Lionel Messi's passport details Graham CLULEY June 12, 2026 According to media reports , a security blunder carelessly leaked the passport details of every player in Argentina's World Cup squad ahead of Tuesday's warm-up friendly against Iceland. And, for once, there wasn't a hacker to blame. The passport numbers of players, including star Lionel Messi, should have been redacted on an official team sheet before being released to the media and public, but at Alabama's Jordan-Hare Stadium it was circulated without sensitive information being obscured. All 11 starters on the team as well as the substitutes, were caught up in the breach which occurred before a match played before 88,000 spectators. But why are passport numbers on a World Cup team sheet at all? Under FIFA regulations , teams must provide passport numbers around an hour before a match kicks off. Referees and match officials require the information to verify that the players on the pitch are who the team claims, and that they are eligible to play. In the past, football teams have been caught fielding fraudulently naturalised players, and the passport check is one of the mechanisms designed to catch it before a match rather than afterwards. So the passport numbers belong in the information handed to the referee. But where it definitely does not belong is in the copy handed out to journalists, who typically receive a redacted version instead. In Argentina's case, however, that skip appears to have been skipped entirely. Passport details are, of course, valuable to criminals as they can be used for identity theft, for the forging of travel documents, or simply building a profile of a wealthy target. Depressingly, the Argentinian players can be added to the list of incidents where organisations believed that they had hidden sensitive information, only to discover they had done nothing of the sort. For instance, in January 2019, lawyers for former Trump campaign chief Paul Manafort failed to properly redact evidence filed in federal court. Although the documents appeared to contain redactions in the form of rectangular black boxes, the underlying text remained accessible to anyone who copy-pasted the docuemnts' contents, revealing that Manafort had shared Trump polling data with an alleged Russian intelligence associate, and had lied about it to federal investigators. Later, in 2023, during an antitrust hearing, Sony supplied a document that included confidential details on publisher margins, Call of Duty revenues, and game development costs. Details that Sony did not wish to be shared had been redacted with a black Sharpie marker, but some of them became visible when scanned in. Most recently, and most worryingly, the US Department of Justice released millions of files related to Jeffrey Epstein in December 2025, some of which used superficial black boxes to obscure information, while leaving underlying data accessible. What unites all of these incidents is the same problem. People confuse the appearance of redaction with actual redaction. A black box drawn over text in an electronic document does not necessarily mean that the text can no longer be accessed. The solution is always the same - whether you are an individual, a company, a government department, or working behind the scenes at the World Cup. Before releasing any document containing sensitive data, verify that the data has actually gone - not just covered up. Otherwise you could be scoring a privacy own-goal, and putting other people's security at risk. tags Industry News Author Graham CLULEY Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s. View all posts You might also like Bookmarks
```

#### Corroborating sources (1)

- **Graham Cluley** (practitioner_analysis)
  - Title: Privacy own-goal: World Cup blunder leaks Lionel Messi’s passport details
  - Published: 2026-06-12T18:48:06+00:00
  - Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/privacy-own-goal-world-cup-blunder-leaks-lionel-messis-passport-details
  - Summary: Argentina's World Cup squad had their passport numbers leaked before a ball was kicked - not by hackers, but by someone who failed to redact a document properly. document. It's a mistake that has been made many times in the past... Read more in my article on the Hot for Security blog.

### Cluster 5da6b03ed1 — score 9

- Title: Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-09T16:39:47+00:00
- Link: https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-44963

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, phishing_social_eng, ransomware_extortion, zero_day
- affected_products: Anthropic/Claude, Ivanti, Microsoft Defender
- cve_ids: CVE-2026-11645, CVE-2026-44963
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft, zero_day, active_exploitation
- affected_products: Anthropic/Claude, Ivanti, Microsoft Defender
- cve_ids: CVE-2026-44963, CVE-2026-11645
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Veeam has released security patches to address a critical flaw in its Backup & Replication software that could result in remote code execution. Tracked as CVE-2026-44963, the vulnerability carries a CVSS score of 9.4 out of a maximum of 10.0. "A vulnerability allowing remote code execution (RCE) on the Backup Server by an authenticated domain user," Veeam said in a Tuesday advisory. It
```

#### Full body

```
Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code  Ravie Lakshmanan  Jun 09, 2026 Vulnerability / Backup Software Veeam has released security patches to address a critical flaw in its Backup & Replication software that could result in remote code execution. Tracked as CVE-2026-44963 , the vulnerability carries a CVSS score of 9.4 out of a maximum of 10.0. "A vulnerability allowing remote code execution (RCE) on the Backup Server by an authenticated domain user," Veeam said in a Tuesday advisory. It credited watchTowr researcher Sina Kheirkhah for responsibly discovering and reporting the issue. It impacts Veeam Backup & Replication 12.3.2.4465 and all earlier versions of 12 builds. Veeam has noted that the vulnerability does not affect any version 13.x build of the backup software due to architectural changes introduced in version 13. The shortcoming has been addressed in Veeam Backup & Replication version 12.3.2.4854. In March 2026, Veeam resolved multiple critical vulnerabilities in Backup & Replication software that, if successfully exploited, could result in remote code execution. It's essential that users update to the latest version for optimal version, particularly given that prior vulnerabilities in the program have been exploited by bad actors, including ransomware groups. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Backup software , cybersecurity , ransomware , remote code execution , Veeam , Vulnerability ⚡ Top Stories This Week Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities Cybersecurity Stars Awards 2026: Winners Announced Across 95 Categories ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories New GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files Agentjacking Attack Tricks AI Coding Agents Into Running Malicious Code China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication U.S. Orders Anthropic to Suspend Fable 5 and Mythos 5 Access for Foreign Nationals Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit ⭐ Featured Resources Get the 2026 Guide to Govern and Secure Enterprise AI Agents at Scale [Watch Demo] See Which Security Gaps Attackers Could Exploit First AI Can’t Stop Every Attack. Learn How Zero Trust Can Block What’s Unknown Have You Outgrown Your MDR? 7 Warning Signs Every CISO Should Check
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code
  - Published: 2026-06-09T16:39:47+00:00
  - Link: https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html
  - Summary: Veeam has released security patches to address a critical flaw in its Backup & Replication software that could result in remote code execution. Tracked as CVE-2026-44963, the vulnerability carries a CVSS score of 9.4 out of a maximum of 10.0. "A vulnerability allowing remote code execution (RCE) on the Backup Server by an authenticated domain user," Veeam said in a Tuesday advisory. It

### Cluster 7c21419055 — score 9

- Title: [tl;dr sec] #332 - I've Joined OpenAI, fwd:cloudsec, AWS Well Architected Supply Chain Security
- Source: tl;dr sec (practitioner_analysis)
- Published: 2026-06-11T14:30:00+00:00
- Link: https://tldrsec.com/p/tldr-sec-332
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: critical_infrastructure
- affected_products: GitHub, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: critical_infrastructure
- affected_products: GitHub, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Why I joined OpenAI to lead Cyber efforts, playlist of the latest cloud security talks, AWS' supply chain best practices
```

#### Full body

```
0 tl;dr sec Posts [tl;dr sec] #332 - I've Joined OpenAI, fwd:cloudsec, AWS Well Architected Supply Chain Security [tl;dr sec] #332 - I've Joined OpenAI, fwd:cloudsec, AWS Well Architected Supply Chain Security Why I joined OpenAI to lead Cyber efforts, playlist of the latest cloud security talks, AWS' supply chain best practices Clint Gibler June 11, 2026 Hey there, I hope you’ve been doing well! 🤔 New Job, Who Dis? TL;DR : I’ve joined OpenAI to lead their Cyber efforts. I’m joined by Mike Aiello , an awesome security executive and human. Mike was previously CTO at Secureworks, led product for Google Cloud Security from 0 → $B’s in revenue, and CISO at Goldman Sachs. I was going to write a post describing all the details about joining, my thought process, etc. but it turns out there’s a lot to do at OpenAI and I’ve gotten very busy 😅 The post is started but not finished, will share when I can. So here’s the short version. Why I was very happy at Semgrep and wasn’t looking for new opportunities, but when an OpenAI recruiter reached out, it seemed like a once in a lifetime company and opportunity that I couldn’t pass by. During the interview process, when I spoke with my potential colleagues, I was impressed by how they were incredibly smart and kind, and genuinely, earnestly, cared about making a positive impact on the world. Several people, without me bringing it up, expressed to me that as models get better, they feel a moral responsibility to do what they can to secure the world’s software. And now from the inside, I can see that the sentiment was genuine, and not a facade (you always wonder as an outsider). OpenAI has easily already spent millions securing open source and critical infrastructure that they haven’t yet claimed PR cred for doing. I’ve long talked about the power of secure by design and eliminating vulnerability classes . Being at OpenAI makes that feel tractable in a way it never has before. I’m optimistic we, the security community, can meaningfully raise the world’s security bar over the next few years. Seriously. Lastly, how I think about the decision is also well expressed by my friend Rami McCarthy , who, like with many things, annoyingly wrote a better version of what I would write in his post on joining Wiz . Similarly, I hope to “ work for the security industry, at OpenAI. ” I shared a LinkedIn post with a bit more details, feel free to say hi or share thoughts there 👋 P.S. tl;dr sec will continue, don’t worry. Also, I will continue to include high quality content from Anthropic, that is also unchanged. More on that below. Sponsor 📣 State of SDLC Report 2026 The 2026 SDLC Security Report analyzed real-world development environments, codebases, and SDLC infrastructure to understand how risk is evolving and how software is built and shipped. The TL;DR: Risk isn’t primarily driven by rare vulnerabilities. It scales through reuse, permissions, and automation across the SDLC. The report explores: AI copilots and developer tooling risk Dependency concentration and supply chain exposure Secret leakage trends CI/CD and GitHub Actions attack paths Learn how SDLC risk is reshaping application security. 👉 Get the State of SDLC Report 👈 Hm interesting, neat to see the SDLC is evolving and how it’s affecting AppSec 🤔 I like the stats and figures. AppSec 1-Click GitHub Token Stealing via a VSCode Bug Ammar Askar describes a bug in which clicking a github.dev link could steal a GitHub token with read/write access to all your private repos, by chaining a Jupyter notebook payload that exploits VS Code webview's did-keydown event forwarding to install a malicious extension. Neat write-up! How We Cut Semgrep’s Taint Analysis Time by 75% Semgrep's Austin Theriault walks through how the taint analysis engine was redesigned to run once instead of twice, cutting scan times by up to 75%. Taint analysis is used for vulnerabilities like SQL injection by tracking user input as it flows through code from sources to sinks, with pr
```

#### Corroborating sources (1)

- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #332 - I've Joined OpenAI, fwd:cloudsec, AWS Well Architected Supply Chain Security
  - Published: 2026-06-11T14:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-332
  - Summary: Why I joined OpenAI to lead Cyber efforts, playlist of the latest cloud security talks, AWS' supply chain best practices

### Cluster 9195174ea0 — score 8

- Title: How threat hunting evolves at scale
- Source: Red Canary (detection_response_operations)
- Published: 2026-06-11T13:09:00+00:00
- Link: https://redcanary.com/blog/threat-detection/threat-hunting-scaled/
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
We offer a practical roadmap for evolving informal, ad hoc threat hunting practices into a mature, scalable program
```

#### Full body

```
Skip Navigation Get a Demo
```

#### Corroborating sources (1)

- **Red Canary** (detection_response_operations)
  - Title: How threat hunting evolves at scale
  - Published: 2026-06-11T13:09:00+00:00
  - Link: https://redcanary.com/blog/threat-detection/threat-hunting-scaled/
  - Summary: We offer a practical roadmap for evolving informal, ad hoc threat hunting practices into a mature, scalable program

### Cluster 6cd576c4e1 — score 8

- Title: JS-Tap v3: Endpoint Post-Exploitation With JavaScript Implants
- Source: TrustedSec (detection_response_operations)
- Published: 2026-06-12T04:00:00+00:00
- Link: https://trustedsec.com/blog/js-tap-v3-endpoint-post-exploitation-with-javascript-implants
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
<p>When I first wrote JS-Tap, the goal was to provide red teamers with a generic JavaScript payload that works without prior knowledge of a web application and without an authenticated user running it. Instrument the…</p>
```

#### Full body

```
Blog JS-Tap v3: Endpoint Post-Exploitation With JavaScript Implants June 12, 2026 JS-Tap v3: Endpoint Post-Exploitation With JavaScript Implants Written by Drew Kirkpatrick Application Security Assessment Red Team Adversarial Attack Simulation Penetration Testing Table of contents The New Beacons Also New in v3 Wrapping Up Demo Video When I first wrote JS-Tap, the goal was to provide red teamers with a generic JavaScript payload that works without prior knowledge of a web application and without an authenticated user running it. Instrument the client side, collect loot, attack the application with stolen creds. That original payload, what I now call the DOM beacon, still works just fine, but in the past year, I wanted to expand the reach of JS-Tap. JavaScript, sadly, has escaped the web application DOM and is now used extensively in desktop applications and software. Browser extensions are JavaScript. Electron desktop apps (Slack, Signal, VS Code, Discord, lots of the corporate tooling you'll find on a workstation) are JavaScript. The new wave of CLI tools built on Node and Bun, including the AI coding assistants everyone is suddenly running, are JavaScript. Here’s the part that makes all of this worse—all of these application environments run JavaScript with less sandboxing than the browser DOM where the original JS-Tap payload lives. The same monkeypatching tricks JS-Tap has always used to intercept network calls and scrape data work in these environments, too—except now, there's no Same-Origin Policy in the way, and in many cases, there's full access to the underlying operating system. So, JS-Tap v3 grows beyond the browser to post-exploitation of the endpoint. It introduces three (3) new beacon types, all reporting back to the same JS-Tap C2, integrated for your engagement data collection needs. The New Beacons BEX Beacon (Browser Extension) The BEX beacon is JS-Tap as a browser extension, for Chrome, Chromium, Edge, and Firefox across Windows, Linux, and Mac. The DOM beacon lives inside a single page, and the BEX beacon sits at the browser level and sees all. Because it runs with extension privileges rather than page privileges, it sidesteps a lot of what limits the DOM beacon. It captures cookies across all domains, including httpOnly cookies , which the DOM beacon simply can't touch. It grabs localStorage, sessionStorage, and request headers and tracks browsing across every tab. Note that there are very important scoping settings about what domains the BEX beacon is allowed to work on, compiled in and critical for use in an engagement. Make sure you have that scoping conversation with your client before you use this in an assessment. The BEX beacon also works as a dropper. From the JS-Tap portal, you can task it to inject a full DOM beacon into a specific domain being used in that browser. A DOM beacon spawned this way gets pixel-perfect screenshots through the extension's captureVisibleTab API instead of relying on the html2canvas library baked into the DOM beacon. The BEX beacon also allows proxying of network traffic through the beacon. Figure 1: BEX Beacon Capturing HttpOnly Session Cookies Pair the BEX beacon with the optional new Sidecar , a small Go binary installed alongside the extension and used via the browser's native messaging feature, and you get OS-level file browsing and command execution from a browser extension. There is an OPSEC tradeoff here. Native messaging is the least stealthy of the OS-access options in JS-Tap v3 beacons, since it requires a registered native host and a separate binary on disk, and the Atom and V8 beacons get host access in cleaner ways. For situations where the browser extension is your foothold, it is very powerful if you’re in a position to install Sidecar alongside the BEX extension. Figure 2: Sidecar File Browser Figure 3: Sidecar Shell Pop-Out Atom Beacon (Electron App Implant) The Atom beacon is an implant for Electron desktop applications. You patch it into the target ap
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: JS-Tap v3: Endpoint Post-Exploitation With JavaScript Implants
  - Published: 2026-06-12T04:00:00+00:00
  - Link: https://trustedsec.com/blog/js-tap-v3-endpoint-post-exploitation-with-javascript-implants
  - Summary: <p>When I first wrote JS-Tap, the goal was to provide red teamers with a generic JavaScript payload that works without prior knowledge of a web application and without an authenticated user running it. Instrument the…</p>

### Cluster 4537ab9a34 — score 8

- Title: Hardening Intune: The Implementation Guide
- Source: TrustedSec (detection_response_operations)
- Published: 2026-06-11T04:00:00+00:00
- Link: https://trustedsec.com/blog/hardening-intune-the-implementation-guide
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, zero_day
- affected_industries: government
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day
- affected_industries: government
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>Part 2: Step-by-Step Configuration for Every ControlThis is Part 2 of a two-part series on Intune security hardening. Part 1 covers the attacks we have seen against this types of platforms, why platform administration…</p>
```

#### Full body

```
Blog Hardening Intune: The Implementation Guide June 11, 2026 Hardening Intune: The Implementation Guide Written by Carlos Perez Incident Response Mobile Security Assessment Table of contents Prerequisites: Microsoft Graph PowerShell Phase 1: Immediate Actions Phase 2: Short-Term Hardening Phase 3: Medium-Term Hardening Phase 4: Detection Appendix: Running the Full Audit Implementation Checklist Closing Thought Part 2: Step-by-Step Configuration for Every Control This is Part 2 of a two-part series on Intune security hardening. Part 1 covers the attacks we have seen against this types of platforms, why platform administration roles are Tier 0 assets, and the controls you need. This post walks you through how to implement each one. In Part 1 , I made the case that these attacks are not an Intune vulnerability, it is a access governance failure. In most incident the attacker compromises an Intune administrator account, created a new Global Admin, and used the platform's built-in remote wipe capability to factory reset devices in the most destructive cases. No malware, no zero-day, just a legitimate management feature executed from a compromised privileged account. I laid out 11 controls and a prioritized quick-win list. This post is the implementation guide. For each control, I will walk through the configuration path, decision points, and a validation test so you can confirm it is working. I am organizing these in the order I would implement them during a hardening engagement, not the order they appeared in Part 1. Implementation Sequence The order matters. Some controls are prerequisites for others, and some produce immediate risk reduction with minimal operational disruption. Here is how I sequence these in engagements: Phase 1: Immediate (Day 1, no dependencies) 1. Audit and remove standing Global Admin and Intune Administrator role assignments 2. Enable PIM on Intune-related roles 3. Enable Multi-Admin Approval for destructive actions 4. Review Graph API app registrations Phase 2: Short-term (Week 1-2, requires planning) 5. Enforce phishing-resistant MFA via Conditional Access authentication strength 6. Configure RBAC custom roles and scope tags 7. Lock down Intune portal access with Conditional Access Phase 3: Medium-term (Week 2-4, requires testing) 8. Deploy Privileged Access Workstations and configure redundancy 9. Enforce script signing and lock down Win32 app deployment 10. Harden device enrollment restrictions Phase 4: Detection (can run in parallel) 11. Deploy Sentinel analytics rule and configure telemetry pipeline Prerequisites: Microsoft Graph PowerShell Throughout this guide, I provide PowerShell commands alongside the portal navigation steps. Some of these are faster and more thorough than clicking through the GUI, especially for auditing and enumeration. You will need the Microsoft Graph PowerShell SDK installed. I have packaged all of the PowerShell in this post as a module of advanced functions: Invoke-IntuneSecurityAudit.ps1 . Download the module, dot-source it, and every function is available with full Get-Help documentation and -Verbose output. # Install the Graph PowerShell SDK (if not already installed) Install-Module Microsoft.Graph -Scope CurrentUser # Dot-source the audit module . .\Invoke-IntuneSecurityAudit.ps1 # Connect with read-only scopes for the audit Connect-IntuneSecurityAudit -Verbose # If you need write scopes later for configuration changes Connect-IntuneSecurityAudit -IncludeWriteScopes -Verbose Every function uses [CmdletBinding()] and Write-Verbose so you can control output verbosity. Use -Verbose to see progress and detail, or omit it for clean pipeline output suitable for Export-Csv or further processing. You will be prompted for permissions when connecting: Figure 1 - Permission Request Phase 1: Immediate Actions 1. Audit and Remove Standing Privileged Access Why this is first: Every other control assumes you know who has privileged access today. You cannot enable PIM on roles that
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: Hardening Intune: The Implementation Guide
  - Published: 2026-06-11T04:00:00+00:00
  - Link: https://trustedsec.com/blog/hardening-intune-the-implementation-guide
  - Summary: <p>Part 2: Step-by-Step Configuration for Every ControlThis is Part 2 of a two-part series on Intune security hardening. Part 1 covers the attacks we have seen against this types of platforms, why platform administration…</p>

### Cluster 1674209ab9 — score 8

- Title: How to Train Your (Dragons) Analysts - A TrustedSec Guide to Picking the Perfect Purple Team
- Source: TrustedSec (detection_response_operations)
- Published: 2026-06-09T04:00:00+00:00
- Link: https://trustedsec.com/blog/how-to-train-your-dragons-analysts
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: AWS, Azure, Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: AWS, Google Cloud, Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>Whether it be the advent of AI technologies, new Red-Team techniques and exploits, or new patches and emergent defensive technologies, it’s pretty clear to all of us operating within technology fields that the landscape…</p>
```

#### Full body

```
Blog How to Train Your (Dragons) Analysts - A TrustedSec Guide to Picking the Perfect Purple Team June 09, 2026 How to Train Your (Dragons) Analysts - A TrustedSec Guide to Picking the Perfect Purple Team Written by Megan Nilsen Purple Team Adversarial Detection & Countermeasures Table of contents TrustedSec Engagement Overview How to Pick your Perfect Match Conclusion Whether it be the advent of AI technologies, new Red-Team techniques and exploits, or new patches and emergent defensive technologies, it’s pretty clear to all of us operating within technology fields that the landscape of computing and cyber-security is ever evolving. In order to stay up to date with all that’s going on, the TrustedSec Purple Team has been hard at work renovating and improving our assessments to better service the needs of our clients and the broader security community. This blog post will walk you through the types of Purple Team assessments that we offer, how to choose the assessment that will meet your security team where they are, and offer the best path forward to improvement. TrustedSec Engagement Overview Live Fire Exercise (LFX) The Live Fire Exercise is an active testing engagement in which TrustedSec consultants execute a pre-designed playbook of attack scenarios within your environment, and then, in tandem with the client’s Blue Team, leverage the generated telemetry to test, validate, and evaluate logging within the clients defensive tooling (EDR, SIEM, IDPS). The LFX comes in two models: live bootcamp style assessments, and ad-hoc assessments which allow TrustedSec consultants to perform the same work, but with more scheduling flexibility. Detection Validation and Review Assessment (DVR) The Detection Validation and Review Assessment is another active testing style assessment that targets a specific and defined list of client-built detections. In this ad-hoc style engagement, TrustedSec will test and validate that existing detections can fire and will provide tangible recommendations to improve logic or recommend additional detections if a gap in coverage is identified. Defense Validation and SIEM Ingestion Review (DVSIR) TrustedSec's Defense Validation is a structured assessment designed to quantify the effectiveness of an organization's defensive controls. The engagement begins with a Detection and Alerting Interview, where consultants collaborate with the organization to identify its primary security goals, high-priority systems, and business-critical data. A SIEM Configuration Review is then performed to assess whether the organization’s SIEM has sufficient visibility into environmental logging, aiming to reduce unnecessary event logging to maximize the usability of the SIEM. Adversarial Detection and Countermeasures Engagement (AD&C) and General Variants The AD&C assessment features live attack scenario execution and custom, high-fidelity detections written directly within your SIEM or EDR platform. We also evaluate the security posture surrounding those scenarios and provide tangible guidance for how to improve. This exercise comes in two models: live bootcamp style assessments, or an ad-hoc assessment. To tailor your experience, we also offer multiple AD&C Assessment variants, such as: Phases: Our standard playbooks. A great place to start if you’re new to working with us. MITRE Focused: Know your environment? If there are specific gaps pertaining to a specific phase of the MITRE framework (e.g. Lateral Movement, Discovery), this is a great assessment for having a more targeted evaluation of the problem area. Cloud: Looking for detection engineering for AWS, GCP, Azure- or other cloud platforms? This is the right assessment for you! Blue Team Guidance: Looking to review and cover gaps from an existing pentest or Red Team? This assessment focuses on walking through key techniques and issues from the report, leveraging the work that has already been done to close existing gaps in detection or prevention. ADS: Want an AD&C but
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: How to Train Your (Dragons) Analysts - A TrustedSec Guide to Picking the Perfect Purple Team
  - Published: 2026-06-09T04:00:00+00:00
  - Link: https://trustedsec.com/blog/how-to-train-your-dragons-analysts
  - Summary: <p>Whether it be the advent of AI technologies, new Red-Team techniques and exploits, or new patches and emergent defensive technologies, it’s pretty clear to all of us operating within technology fields that the landscape…</p>

### Cluster fa2566aa3e — score 8

- Title: Maine disables data breach notification portal after fake disclosures
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-12T19:33:32+00:00
- Link: https://www.bleepingcomputer.com/news/security/maine-disables-data-breach-notification-portal-after-fake-disclosures/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: critical_infrastructure, education
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: critical_infrastructure, education
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Maine has taken its public data breach reporting portal offline after fraudulent breach disclosures were published on the state's website, prompting a review of procedures to prevent abuse in the future. [...]
```

#### Full body

```
Maine disables data breach notification portal after fake disclosures By Lawrence Abrams June 12, 2026 03:33 PM 0 Maine has taken its public data breach reporting portal offline after fraudulent breach disclosures were published on the state's website, prompting a review of procedures to prevent abuse in the future. Yesterday, BleepingComputer reported that fake data breach disclosures had been submitted to Maine's official breach notification portal impersonating Discord and the multiplayer social virtual reality platform VRChat. At the time, VRChat told BleepingComputer the filing was fraudulent and had been submitted using the name of a fictitious employee. In a statement published Friday, the Maine Attorney General's Office acknowledged that data breach "hoaxes" were submitted through the state's reporting system. "The Office of the Maine Attorney General has been made aware of an apparent abuse of our data breach reporting system," the statement reads . "After conversations with VRChat, one of two affected companies, it has become clear that the reported data breaches were hoaxes submitted by an unknown entity unrelated to either company. These false reports have been removed from the database. We have no knowledge of any recent legitimate data breach reports from either VRChat or Discord." The Attorney General's Office says it has now temporarily disabled public access to the breach notification database while it reviews reporting procedures to reduce similar abuse in the future. Prior to the shutdown, submitted breach notices were automatically published to the public database. "We don’t have any independent knowledge of the breaches, the submitting entity fills out the information and it goes directly onto the site. We will review the one you’ve flagged, thank you," Maine Attorney General's Office told BleepingComputer. The notice states that companies can continue to submit breach notifications through the reporting service, but members of the public seeking copies of disclosures must now contact the Attorney General's Office directly. Maine's data breach portal is commonly used by journalists, researchers, and threat intelligence firms to monitor newly disclosed security incidents and determine whether organizations are reporting cyberattacks or data breaches affecting consumers. The incident demonstrates how automatically published breach disclosures can be abused to spread misinformation and damage a company's reputation. The fraudulent VRChat filing claimed the company suffered a data breach impacting over 2.4 million people and included a fabricated employee contact name in the disclosure. After BleepingComputer contacted VRChat about the filing, the company confirmed the disclosure was fake and stated it had not submitted the notice to Maine authorities. BleepingComputer also contacted Discord about the fraudulent notice submitted to the site but did not receive a response. It is unclear how many additional fraudulent breach notices may have been submitted through the portal before the state suspended public access to the database. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Maine breach portal abused to publish fake data breach disclosures Infinite Campus data breach affects 137,000 school staff accounts Ex-school district employee jailed for hacks on former employer Japanese energy firm loses drive with data of 10.9 million clients Pharma giant Novo Nordisk discloses breach of clinical trials data
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Maine disables data breach notification portal after fake disclosures
  - Published: 2026-06-12T19:33:32+00:00
  - Link: https://www.bleepingcomputer.com/news/security/maine-disables-data-breach-notification-portal-after-fake-disclosures/
  - Summary: Maine has taken its public data breach reporting portal offline after fraudulent breach disclosures were published on the state's website, prompting a review of procedures to prevent abuse in the future. [...]

### Cluster 09b4827a59 — score 8

- Title: phpBB forum fixes auth bypass bug lurking for a decade
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-12T18:19:34+00:00
- Link: https://www.bleepingcomputer.com/news/security/phpbb-forum-fixes-auth-bypass-bug-lurking-for-a-decade/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, vulnerability_disclosure
- affected_products: Fortinet, Palo Alto Networks, SonicWall
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft, vulnerability_disclosure
- affected_products: Fortinet, Palo Alto Networks, SonicWall
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A 10-year-old authentication bypass vulnerability discovered in the phpBB forum software allows an attacker to log in as any user, including administrators. [...]
```

#### Full body

```
phpBB forum fixes auth bypass bug lurking for a decade By Bill Toulas June 12, 2026 02:19 PM 1 A 10-year-old authentication bypass vulnerability discovered in the phpBB forum software allows an attacker to log in as any user, including administrators. The flaw does not have an identifier and is trivial to exploit with a single HTTP request. It impacts phpBB versions 4.0.0-a2 or 3.3.16 and below. Researchers at application security company Aikido found the bug on June 2nd and reported it through the developer's HackerOne Vulnerability Disclosure Program. phpBB responded to the report immediately and addressed the problem on June 6 in version 3.3.17 of the software. According to Aikido, the flaw was introduced to phpBB’s codebase 10 years ago, impacting all versions of the 3.x and 4.x release branches, up to 3.3.16 and 4.0.0-a2. For the 4.x release, there’s no fix available yet. phpBB is a PHP-based free and open-source web forum platform that enjoyed peak popularity in the 2000s and early 2010s. Today, it is still powering thousands of forums worldwide. Aikido says that exploiting the bug requires no special configuration, as it can be triggered on the default settings. “The vulnerability is exploitable in the default configuration and requires no special knowledge,” reads Aikido's report . “If you are on version 4.0.0-a2 or 3.3.16 and below, upgrade immediately to master (no safe 4.x release yet) and 3.3.17, respectively, to avoid compromise.” Administrator access could allow attackers to view all private messages stored on the forum, create, modify, or delete content and user accounts, impersonate staff, or deface the sites. Picking targets is also straightforward, as the member list on phpBB forums is public by default. Aikido notes that remote code execution (RCE) is not possible due to a separate password check that protects the Admin Control Panel. The researchers withheld all technical details for now to allow forum administrators enough time to apply the security updates and even contacted administrators of large phpBB-based forums to alert them directly. One thing to note is that the update may cause forums using OAuth authentication to break, because the OAuth redirect handler has moved to a new location, but this should be a simple fix in most cases. Aikido promised to publish the full details of the flaw in a future report, but did not provide a specific timeline. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Palo Alto GlobalProtect VPN auth bypass flaw now exploited in attacks SAP fixes critical flaws in NetWeaver and Commerce Cloud Hackers exploit FortiClient EMS flaw to push infostealer malware Hackers bypass SonicWall VPN MFA due to incomplete patching Hackers exploit auth bypass flaw in Burst Statistics WordPress plugin
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: phpBB forum fixes auth bypass bug lurking for a decade
  - Published: 2026-06-12T18:19:34+00:00
  - Link: https://www.bleepingcomputer.com/news/security/phpbb-forum-fixes-auth-bypass-bug-lurking-for-a-decade/
  - Summary: A 10-year-old authentication bypass vulnerability discovered in the phpBB forum software allows an attacker to log in as any user, including administrators. [...]

### Cluster 2442286632 — score 8

- Title: CISA directive orders agencies to prioritize vulnerability patching in a new way
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-06-10T16:07:11+00:00
- Link: https://cyberscoop.com/cisa-vulnerability-remediation-directive-bod-26-04/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: government
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: government
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
A vulnerability that meets all four criteria would need to be fixed within three days, for instance. The post CISA directive orders agencies to prioritize vulnerability patching in a new way appeared first on CyberScoop .
```

#### Full body

```
Advertisement Subscribe to our daily newsletter. Subscribe Close The Cybersecurity and Infrastructure Security Agency on Wednesday ordered federal agencies to prioritize vulnerabilities based on four criteria, as part of push to “patch smarter, not harder.” Federal agencies should emphasize patches for vulnerabilities that affect a publicly exposed asset, allow an attacker to fully automate exploitation, give attackers the ability to take over control of a system or relate to evidence of active, real-world exploitation, CISA declared. CISA acting director Nick Andersen previewed the binding operational directive (BOD) Tuesday, framing it as a rethinking of vulnerability management more broadly. “This Directive provides clear definitions, timelines and criteria that enhances transparency, predictability and agencies’ resource planning to execute more effective vulnerability remediation,” Andersen said in a statement. “CISA is leading and collaborating with federal civilian agencies to stay ahead of our adversaries as tactics, technologies and vulnerabilities change.” Advertisement BOD 26-04 sets forth timelines for how quickly agencies must fix a vulnerability based on how many of the four criteria it meets. If it meets all four, for example, agencies need to fix it within three days and carry out a “forensic triage” to assess whether their systems were compromised. More generally, agencies must immediately update their vulnerability management policies, including establishing a process for ongoing remediation of known, exploited vulnerabilities (KEVs) on CISA’s “must-patch” list. Within 60 days, agencies need to update their processes for remediating common vulnerabilities, and within 180 days, agencies must meet the order’s remediation timelines. The directive is motivated in part by how artificial intelligence is shifting the window from vulnerability discovery to weaponization, and CISA said it reflects priorities in an executive order on AI that President Donald Trump signed last week. BODs aren’t mandatory for anyone outside of federal agencies, but CISA encourages the private sector to embrace them. CISA officials said in a blog post about the need to “patch smarter, not harder” that “defenders are already struggling to keep up.” “Artificial intelligence is assisting both researchers and adversaries in identifying flaws in software, vastly increasing the pace at which new vulnerabilities are discovered,” wrote Chris Butera, acting executive assistant director for cybersecurity, and Jonathan Spring , senior technical adviser. “Per Verizon’s 2026 Data Breach Investigations Report, only 26% of vulnerabilities on CISA’s Known Exploited Vulnerabilities (KEV) Catalog were fully remediated by organizations in 2025, a drop from the previous year’s 38%. The median time for full resolution rose to 43 days.” Advertisement The move from weeks to days for agencies to patch the most urgent vulnerabilities is something CISA has discussed with some agencies to see if it’s doable, Butera told reporters Wednesday. At one large agency CISA analyzed, just 1% of vulnerabilities fell into the 3-day window, while 60% could be deferred to the next system upgrade. “We’ve engaged with a few federal agencies ahead of this directive and tried to socialize some of these new time frames,” he said. “We really believe we should be able to free up some time to patch the most urgent vulnerabilities faster, while allowing for more regular patch cycles for some of the lower risk vulnerabilities.” Patrick Garrity, a security researcher at VulnCheck, said the CISA directive joins similar guidance out of India and the United Kingdom. “It’s clear the momentum is growing and pushing in the right direction,” he told CyberScoop. “The new directive aligns exactly with the approach we’ve been taking with customers for years, leveraging exploit intelligence to focus on the subset of vulnerabilities that enterprises, governments and vendors really need to address. Wh
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: CISA directive orders agencies to prioritize vulnerability patching in a new way
  - Published: 2026-06-10T16:07:11+00:00
  - Link: https://cyberscoop.com/cisa-vulnerability-remediation-directive-bod-26-04/
  - Summary: A vulnerability that meets all four criteria would need to be fixed within three days, for instance. The post CISA directive orders agencies to prioritize vulnerability patching in a new way appeared first on CyberScoop .

### Cluster 6415032017 — score 8

- Title: Check Point VPN Flaw Exploited Since Early May
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-06-08T20:28:35+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/check-point-vpn-flaw-exploited-early-may
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A newly discovered, critical zero-day vulnerability is under attack; a Qilin ransomware affiliate has been blamed for at least one incident.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Check Point VPN Flaw Exploited Since Early May
  - Published: 2026-06-08T20:28:35+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/check-point-vpn-flaw-exploited-early-may
  - Summary: A newly discovered, critical zero-day vulnerability is under attack; a Qilin ransomware affiliate has been blamed for at least one incident.

### Cluster b9fc8f1b1a — score 8

- Title: New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-11T17:46:32+00:00
- Link: https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Two security teams have shown, in separate research published this week, that OpenClaw, the popular self-hosted AI agent, can be driven to run attacker-controlled code or hand over sensitive data through ordinary-looking inputs. Imperva buried instructions inside shared contacts, vCards, and location pins that the agent executed without the victim ever seeing them. Varonis built a test agent on
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets
  - Published: 2026-06-11T17:46:32+00:00
  - Link: https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html
  - Summary: Two security teams have shown, in separate research published this week, that OpenClaw, the popular self-hosted AI agent, can be driven to run attacker-controlled code or hand over sensitive data through ordinary-looking inputs. Imperva buried instructions inside shared contacts, vCards, and location pins that the agent executed without the victim ever seeing them. Varonis built a test agent on

### Cluster dd24bfa583 — score 8

- Title: AI Broke Vulnerability Management. That's Why CISOs Are Moving Budget to BAS.
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-11T11:30:00+00:00
- Link: https://thehackernews.com/2026/06/ai-broke-vulnerability-management-thats.html
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
For thirty years, vulnerability management ran on a buffer: the months between when a vulnerability was found and when someone could figure out how to weaponize it. The solution was straightforward enough; triage by severity, schedule the fix, validate, and move on. The buffer was what made that work. Today, that buffer is gone. AI didn't make your team slower. It changed the other side of the
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: AI Broke Vulnerability Management. That's Why CISOs Are Moving Budget to BAS.
  - Published: 2026-06-11T11:30:00+00:00
  - Link: https://thehackernews.com/2026/06/ai-broke-vulnerability-management-thats.html
  - Summary: For thirty years, vulnerability management ran on a buffer: the months between when a vulnerability was found and when someone could figure out how to weaponize it. The solution was straightforward enough; triage by severity, schedule the fix, validate, and move on. The buffer was what made that work. Today, that buffer is gone. AI didn't make your team slower. It changed the other side of the

### Cluster 8d3bbb4957 — score 8

- Title: Extortion-Only Attacks Increase, With Data Theft Dominating Ransomware Claims
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-06-11T10:20:00+00:00
- Link: https://www.infosecurity-magazine.com/news/extortion-only-attacks-surge/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Extortion-only attacks are increasing as data theft drives most ransomware claims, with many organizations unable to stop stolen data from being exposed
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Extortion-Only Attacks Increase, With Data Theft Dominating Ransomware Claims
  - Published: 2026-06-11T10:20:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/extortion-only-attacks-surge/
  - Summary: Extortion-only attacks are increasing as data theft drives most ransomware claims, with many organizations unable to stop stolen data from being exposed

### Cluster b7b0b1454f — score 8

- Title: Critical phpBB Flaw Lets Attackers Hijack Any Account with One Request
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-06-09T14:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/phpbb-authentication-bypass/
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
Critical phpBB authentication bypass lets attackers hijack any account with one request
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Critical phpBB Flaw Lets Attackers Hijack Any Account with One Request
  - Published: 2026-06-09T14:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/phpbb-authentication-bypass/
  - Summary: Critical phpBB authentication bypass lets attackers hijack any account with one request
