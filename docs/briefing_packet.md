# PHANTOMSignal Briefing Packet

- Generated: 2026-07-14T15:27:58.650954+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 77
- Total items in window: 339
- Total clusters raw: 156
- Total clusters in packet: 65
- Dropped low score: 91
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
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
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
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
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
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 4
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
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
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
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
  - In window count: 0
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 5
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 4
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Active Countermeasures** (detection_response_operations)
  - URL: https://www.activecountermeasures.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 0
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
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
  - In window count: 3
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
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
  - In window count: 7
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 8
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
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
  - In window count: 2
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
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
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 19
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
  - In window count: 1
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 21
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 23
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
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
  - In window count: 3
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 28
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 18
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
  - In window count: 5
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

### phishing social eng targeting Microsoft 365
- Anchor signal: Microsoft 365
- Theme key: microsoft-365
- Cluster count: 4
- Article count: 9
- Cohesion: 0.2
- Shared strong signals: Microsoft 365
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, active_exploitation
  - affected_products: Microsoft 365, Okta
- Cluster IDs: 8d0224c08d, ef8f3ff932, 98dd5f4721, 91c24e6cda
- Links:
  - https://www.recordedfuture.com/blog/june-2026-cve-landscape
  - https://www.securityweek.com/rabbitmq-vulnerability-threatens-enterprise-systems/
  - https://www.huntress.com/blog/conditional-access-misconfigurations
  - https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/
  - https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html
  - https://www.securityweek.com/us-allies-warn-of-russian-cyberattacks-targeting-critical-infrastructure-routers/

### Google Cloud vulnerability activity
- Anchor signal: Google Cloud
- Theme key: google-cloud
- Cluster count: 3
- Article count: 4
- Cohesion: 0.545
- Shared strong signals: Google Cloud
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Google Cloud
- Cluster IDs: 5a4c062977, 480db84242, c8b407c1b8
- Links:
  - https://cloud.google.com/blog/products/identity-security/introducing-k8s-aibom-on-gke-for-automated-ai-bills-of-materials/
  - https://www.infosecurity-magazine.com/news/lidl-notifies-customers-of/
  - https://cloud.google.com/blog/products/databases/nexus-sdv-uses-bigtable-android-automotive-for-agentic-vehicles/

### CVE-2026-48939 exploitation activity
- Anchor signal: CVE-2026-48939
- Theme key: cve-2026-48939
- Cluster count: 2
- Article count: 2
- Cohesion: 0.394
- Shared strong signals: CVE-2026-48939
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation
  - affected_industries: government
  - cve_ids: CVE-2026-48939, CVE-2026-56291
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 08882287bf, 3e3af8b34c
- Links:
  - https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
  - https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-rce-flaws-in-joomla-extensions/

### CVE-2026-56291 exploitation activity
- Anchor signal: CVE-2026-56291
- Theme key: cve-2026-56291
- Cluster count: 2
- Article count: 2
- Cohesion: 0.394
- Shared strong signals: CVE-2026-56291
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation
  - affected_industries: government
  - cve_ids: CVE-2026-48939, CVE-2026-56291
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 08882287bf, 3e3af8b34c
- Links:
  - https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
  - https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-rce-flaws-in-joomla-extensions/

### Apple iOS/macOS vulnerability activity
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Apple iOS/macOS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Apple iOS/macOS
- Cluster IDs: 598aa947b4, 9d6bdd5305
- Links:
  - https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit
  - https://www.helpnetsecurity.com/2026/07/14/crashstealer-macos-infostealer-password-theft/
  - https://www.bleepingcomputer.com/news/security/new-crashstealer-malware-poses-as-apple-crash-reporting-tool/
  - https://thehackernews.com/2026/07/crashstealer-macos-malware-uses.html
  - https://www.huntress.com/blog/patch-management-strategy

### CVE-2026-48283 exploitation activity
- Anchor signal: CVE-2026-48283
- Theme key: cve-2026-48283
- Cluster count: 2
- Article count: 2
- Cohesion: 0.281
- Shared strong signals: CVE-2026-48283
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-48283, CVE-2026-48313
  - urgency_signals: preauth_unauth
- Cluster IDs: 8e87b71464, 843dce4060
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-9181/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48283-cve-2026-48313/

### CVE-2026-48313 exploitation activity
- Anchor signal: CVE-2026-48313
- Theme key: cve-2026-48313
- Cluster count: 2
- Article count: 2
- Cohesion: 0.281
- Shared strong signals: CVE-2026-48313
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-48283, CVE-2026-48313
  - urgency_signals: preauth_unauth
- Cluster IDs: 8e87b71464, 843dce4060
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-9181/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48283-cve-2026-48313/

### ShinyHunters: supply chain
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 2
- Article count: 3
- Cohesion: 0.283
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain
  - actor_attribution: ShinyHunters
- Cluster IDs: 7df2f246d4, c8e0a6559d
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/
  - https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
  - https://research.checkpoint.com/2026/13th-july-threat-intelligence-report/

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: 7df2f246d4, b835d1d4b1
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/
  - https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
  - https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/

### ransomware extortion targeting Palo Alto Networks
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 2
- Article count: 6
- Cohesion: 0.461
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, supply_chain, data_breach
  - affected_industries: critical_infrastructure, manufacturing_industrial
  - affected_products: Anthropic/Claude, Palo Alto Networks
  - urgency_signals: no_patch_yet
- Cluster IDs: 55bab88c91, 8c85eeaa7f
- Links:
  - https://www.securityweek.com/unpatched-claude-for-chrome-flaw-lets-extensions-read-gmail-calendar/
  - https://aws.amazon.com/blogs/security/enforce-zero-data-retention-on-amazon-bedrock-with-bedrock-projects-and-service-control-policies/
  - https://thehackernews.com/2026/07/thinking-fast-and-slow-in-soc-case-for.html
  - https://www.securityweek.com/7-severe-vulnerabilities-patched-in-vmware-avi-load-balancer/

### Cisco vulnerability activity
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 2
- Article count: 3
- Cohesion: 0.286
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Cisco
- Cluster IDs: 118be3a32e, df4e34a64d
- Links:
  - https://blog.talosintelligence.com/wolfssl-vulnerabilities/
  - https://www.infosecurity-magazine.com/news/uat-7810-china-apt-orb-proxy/
  - https://blog.talosintelligence.com/video-where-protection-starts-cisco-talos-intelligence-integrations/

### supply chain targeting npm
- Anchor signal: npm
- Theme key: npm
- Cluster count: 2
- Article count: 10
- Cohesion: 0.2
- Shared strong signals: npm
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain
  - affected_products: npm
- Cluster IDs: dc767c83a1, c8e0a6559d
- Links:
  - https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions
  - https://securitylabs.datadoghq.com/articles/compromised-asyncapi-npm-packages/
  - https://www.securityweek.com/multiple-jscrambler-packages-impacted-by-supply-chain-attack/
  - https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html
  - https://simonwillison.net/2026/Jul/13/datasette-code-frequency/#atom-everything
  - https://www.bleepingcomputer.com/news/security/hackers-backdoor-jscrambler-npm-package-with-infostealer-malware/
  - https://research.checkpoint.com/2026/13th-july-threat-intelligence-report/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (1)
- **M-Red-Team: AsyncAPI Supply Chain Compromise via GitHub Actions**
  - Cluster: dc767c83a1
  - Sources in window: 3
  - Window hours: 4.3
  - Cohort count: 3

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-55040 + Microsoft SharePoint (cluster b1e7573c37, first observation: True)
- Pair: CVE-2024-27822 + Apple iOS/macOS (cluster 598aa947b4, first observation: True)
- Pair: CVE-2026-41264 + Apple iOS/macOS (cluster 598aa947b4, first observation: True)
- Pair: CVE-2025-12352 + WordPress (cluster 08882287bf, first observation: True)
- Pair: CVE-2025-6389 + WordPress (cluster 08882287bf, first observation: True)
- Pair: CVE-2025-7852 + WordPress (cluster 08882287bf, first observation: True)
- Pair: CVE-2026-48939 + WordPress (cluster 08882287bf, first observation: True)
- Pair: CVE-2026-56291 + WordPress (cluster 08882287bf, first observation: True)
- Pair: CVE-2026-48939 + Ubiquiti UniFi (cluster 3e3af8b34c, first observation: True)
- Pair: CVE-2026-56291 + Ubiquiti UniFi (cluster 3e3af8b34c, first observation: True)
- Pair: CVE-2025-5777 + Anthropic/Claude (cluster aaaf47b0ea, first observation: True)
- Pair: CVE-2025-5777 + OpenAI/ChatGPT (cluster aaaf47b0ea, first observation: True)
- Pair: CVE-2026-12486 + Cisco (cluster 118be3a32e, first observation: True)
- Pair: CVE-2026-12488 + Cisco (cluster 118be3a32e, first observation: True)
- Pair: CVE-2026-25106 + Cisco (cluster 118be3a32e, first observation: True)

### Drift (4)
- **ShinyHunters** (cluster 7df2f246d4)
  - New industries: manufacturing_industrial, retail_ecommerce
  - New products: Microsoft Defender
  - Prior top industries: education, financial_services, government
  - Prior top products: Anthropic/Claude, Salesforce, npm
- **TeamPCP** (cluster 86ef70edb1)
  - New industries: (none)
  - New products: PyPI
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: GitHub, Kubernetes, npm
- **BlackCat/ALPHV** (cluster 85dc7136db)
  - New industries: critical_infrastructure
  - New products: (none)
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Citrix, Fortinet, Microsoft SharePoint
- **Scattered Spider** (cluster 53ef47508e)
  - New industries: (none)
  - New products: GitHub
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Anthropic/Claude, Apple iOS/macOS, Microsoft SharePoint

### Persistence (8)
- actor_attribution: ShinyHunters (weeks observed: 7, cluster 7df2f246d4)
- actor_attribution: TeamPCP (weeks observed: 6, cluster 86ef70edb1)
- cve_ids: CVE-2026-20230 (weeks observed: 5, cluster 8e87b71464)
- actor_attribution: Scattered Spider (weeks observed: 4, cluster 53ef47508e)
- cve_ids: CVE-2026-47729 (weeks observed: 3, cluster 8e87b71464)
- cve_ids: CVE-2025-5777 (weeks observed: 3, cluster aaaf47b0ea)
- cve_ids: CVE-2025-3248 (weeks observed: 3, cluster c8e0a6559d)
- actor_attribution: BlackCat/ALPHV (weeks observed: 3, cluster 85dc7136db)

### Tier inversion (0)

## Clusters

### Cluster b1e7573c37 — score 48

- Title: CVE-2026-55040: Microsoft SharePoint JWT Token Authentication Bypass (FIXED)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-14T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-55040, Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: Microsoft SharePoint
- cve_ids: CVE-2026-55040
- urgency_signals: poc_available, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: Microsoft SharePoint
- cve_ids: CVE-2026-55040
- urgency_signals: zero_day, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview Rapid7 Labs conducted a zero-day research project against Microsoft SharePoint, resulting in the discovery of two new vulnerabilities that, when chained together, achieve unauthenticated remote code execution (RCE) against a vulnerable SharePoint server. Today, both Rapid7 and Microsoft are disclosing the first vulnerability in this chain, the authentication bypass vulnerability CVE-2026-55040. The RCE component of the exploit chain is expected to be patched by Microsoft in the next update cycle for August 2026. The exploit chain was developed as an entry for the recent Pwn2Own Berlin hacking competition – part of Rapid7 Labs' continued effort to raise the bar in Vulnerability Intelligence and our commitment to the preemptive protection of our customers through original vulnerability research. A remote unauthenticated attacker can leverage CVE-2026-55040 to bypass authentication on a vulnerable SharePoint server and perform operations as a SharePoint site user or administrator
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-55040: Microsoft SharePoint JWT Token Authentication Bypass (FIXED) Stephen Fewer Jul 14, 2026 | Last updated on Jul 14, 2026 | 5 min read DISCOVER RAPID7 MDR Overview Rapid7 Labs conducted a zero-day research project against Microsoft SharePoint, resulting in the discovery of two new vulnerabilities that, when chained together, achieve unauthenticated remote code execution (RCE) against a vulnerable SharePoint server. Today, both Rapid7 and Microsoft are disclosing the first vulnerability in this chain, the authentication bypass vulnerability CVE-2026-55040. The RCE component of the exploit chain is expected to be patched by Microsoft in the next update cycle for August 2026. The exploit chain was developed as an entry for the recent Pwn2Own Berlin hacking competition – part of Rapid7 Labs' continued effort to raise the bar in Vulnerability Intelligence and our commitment to the preemptive protection of our customers through original vulnerability research. A remote unauthenticated attacker can leverage CVE-2026-55040 to bypass authentication on a vulnerable SharePoint server and perform operations as a SharePoint site user or administrator. The vulnerability is due to several issues in the JWT token validation pipeline. CVE-2026-55040 has a CVSSv3.1 score of 5.3 (Medium) , and a Common Weakness Enumeration (CWE) of CWE-1390: Weak Authentication . Product description Microsoft SharePoint is a ubiquitous, web-based collaboration and document management platform deeply integrated into the Microsoft 365 ecosystem. Serving as the central hub for corporate intranets, internal file sharing, and workflow automation, it is trusted by enterprises worldwide to store and manage vast repositories of sensitive business data. Because SharePoint acts as a critical bridge between internal users, active directories, and cloud infrastructure, vulnerabilities within its architecture present a high-risk attack surface. Impact By leveraging CVE-2026-55040, a remote unauthenticated attacker can assume the identity of any SharePoint site user; the prerequisite is the attacker must know in advance the user they wish to identify as. This can be achieved in a number of ways, including via a user’s Active Directory (AD) Security ID (SID), or via a user’s AD User Principal Name (UPN). A UPN is the primary logon name for a user in either Windows AD or Microsoft Entra ID, and is formatted similar to that of an email address, e.g. [email protected] . In the example screenshot below, with identifying information redacted, a Rapid7 Labs proof-of-concept script discovers potential SharePoint users via SID enumeration and then leverages CVE-2026-55040 to bypass authentication on the target SharePoint site to assume the identity of that user — ultimately identifying the SharePoint site administrator user account. Figure 1: The Rapid7 Labs PoC for CVE-2026-55040. ⠀ An attacker who successfully exploits CVE-2026-55040 can perform operations against the target SharePoint site as the user they identify as. Furthermore, this authentication bypass can be chained to additional vulnerabilities within the authenticated attack surface of the target site. Rapid7 Labs has chained the authentication bypass CVE-2026-55040 with a separate RCE vulnerability for unauthenticated RCE. Patching CVE-2026-55040 will successfully break this exploit chain. The RCE component has been disclosed to Microsoft and is expected to be patched in the scheduled August patch cycle. The chaining of vulnerabilities highlights that even though the authentication bypass has been assigned a medium severity CVSS score by Microsoft, the impact of successfully chaining a medium severity authentication bypass to an RCE component is significant. This also underscores the importance of patching vulnerabilities such as authentication bypasses, which can break complex and high impact exploit chains. Leveraging AI To develop our SharePoint exploit chain, Rapi
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-55040: Microsoft SharePoint JWT Token Authentication Bypass (FIXED)
  - Published: 2026-07-14T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed
  - Summary: Overview Rapid7 Labs conducted a zero-day research project against Microsoft SharePoint, resulting in the discovery of two new vulnerabilities that, when chained together, achieve unauthenticated remote code execution (RCE) against a vulnerable SharePoint server. Today, both Rapid7 and Microsoft are disclosing the first vulnerability in this chain, the authentication bypass vulnerability CVE-2026-55040. The RCE component of the exploit chain is expected to be patched by Microsoft in the next update cycle for August 2026. The exploit chain was developed as an entry for the recent Pwn2Own Berlin hacking competition – part of Rapid7 Labs' continued effort to raise the bar in Vulnerability Intelligence and our commitment to the preemptive protection of our customers through original vulnerability research. A remote unauthenticated attacker can leverage CVE-2026-55040 to bypass authentication on a vulnerable SharePoint server and perform operations as a SharePoint site user or administrator

### Cluster 598aa947b4 — score 40

- Title: Weekly Metasploit Update: Exploits for FlowiseAI CSV Agent and MacOS Package Kit
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-11T00:32:34+00:00
- Link: https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: Apple iOS/macOS, CVE-2026-41264

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security, credential_theft, web_shell_backdoor
- affected_industries: financial_services
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2024-27822, CVE-2026-41264
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ai_security, web_shell_backdoor
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-41264, CVE-2024-27822
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
More AI, more software, more bugs! AI, it's all you hear about nowadays and everyone's got an opinion on it. Here at Metasploit, we care less about those opinions and more about the growing attack surface all this new software brings with it (yeehaw exploits!). Take for example the new Flowise CSV Agent Prompt Injection RCE brought to you by Takahiro Yokoyama and zdi-disclosures. Flowise is an open-source tool that lets you build AI apps and chatbots using a visual, drag-and-drop canvas and CVE-2026-41264 is an unauthenticated RCE run method of the CSV_Agents class in Flowise. The vulnerability exists due insufficient sandboxing and an incomplete list of disallowed inputs. It allows unauthenticated attackers to upload a .csv file containing arbitrary python code and execute it. One moment you're using AI to help draft and email and the next moment you're getting pwn'd, what a world we live in! Happy Friday and happy hacking everyone. New module content (3) Apache .htaccess Persistence
```

#### Full body

```
Back to Blog Products and Tools Weekly Metasploit Update: Exploits for FlowiseAI CSV Agent and MacOS Package Kit Jack Heysel Jul 11, 2026 | Last updated on Jul 11, 2026 | 4 min read More AI, more software, more bugs! AI, it's all you hear about nowadays and everyone's got an opinion on it. Here at Metasploit, we care less about those opinions and more about the growing attack surface all this new software brings with it (yeehaw exploits!). Take for example the new Flowise CSV Agent Prompt Injection RCE brought to you by Takahiro Yokoyama and zdi-disclosures. Flowise is an open-source tool that lets you build AI apps and chatbots using a visual, drag-and-drop canvas and CVE-2026-41264 is an unauthenticated RCE run method of the CSV_Agents class in Flowise. The vulnerability exists due insufficient sandboxing and an incomplete list of disallowed inputs. It allows unauthenticated attackers to upload a .csv file containing arbitrary python code and execute it. One moment you're using AI to help draft and email and the next moment you're getting pwn'd, what a world we live in! Happy Friday and happy hacking everyone. New module content (3) Apache .htaccess Persistence Authors: 4ravind-b, msutovsky-r7, and wireghoul Type: Exploit Pull request: #21473 contributed by 4ravind-b Path: linux/persistence/apache_htaccess Description: Adds a new persistence module, exploits/linux/persistence/apache_htaccess, that plants wireghoul's mod_cgi .htaccess web shell on a Linux Apache target. Flowise CSV Agent Prompt Injection RCE Authors: Takahiro Yokoyama and zdi-disclosures Type: Exploit Pull request: #21407 contributed by Takahiro-Yoko Path: multi/http/flowise_auth_rce_cve_2026_41264 AttackerKB reference: CVE-2026-41264 Description: This adds a new exploit module for FlowiseAI Flowise (CVE-2026-41264). The CSV Agent feature evaluates LLM-generated Python code without proper sandboxing, allowing a prompt injection to achieve arbitrary code execution as the user running the server. Flowise versions 1.3.0 through 3.0.13 are affected. The module requires an API key with chatflows:create permission but does not require Flowise authentication to trigger the underlying flaw. macOS PackageKit ZSH Environment Privilege Escalation Authors: Mykola Grymalyuk and h00die Type: Exploit Pull request: #21499 contributed by h00die Path: osx/local/packagekit_zshenv_privesc AttackerKB reference: CVE-2024-27822 Description: This adds a new local privilege escalation module for macOS targeting CVE-2024-27822 in PackageKit.framework. When a PKG installer script uses a ZSH shebang, PackageKit runs it as root while inheriting the installing user's environment, causing ZSH to source the user's ~/.zshenv with root privileges. The module plants a payload in ~/.zshenv that fires only when running as root, then opens a minimal PKG with Installer.app; once the user approves the installation prompt and authenticates, the payload executes as root and a root session is returned. Affected versions are macOS 14.4, 13.6.6, 12.7.4, and 11 and earlier; the issue is patched in 14.5, 13.6.7, and 12.7.5. Enhancements and features (5) #21416 from g0tmi1k - This updates the Exploit::Remote::Ftp mixin to improve target fingerprinting. It now leverages recog to fingerprint targets from their banners and adds ftp_fingerprint and ftp_list_directory methods to assist with target enumeration. #21436 from g0tmi1k - Improved UX for reloading of library files. #21579 from zeroSteiner - This adds a few extra fields to some MCP Server tools to align with recent RPC changes in the framework. The msf_service_info tool now has resource and parents fields, the msf_vulnerability_info tool now has a resource field, the msf_note_info tool now has a data field, and the msf_credential_info tool now has new realm_key and realm_value fields. #21580 from Pushpenderrathore - This adds a Certificate Signing Request (CSR) Trace to the CertificateTrace functionality. Users can now opt to see the CSR get printed wh
```

#### Corroborating sources (4)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Weekly Metasploit Update: Exploits for FlowiseAI CSV Agent and MacOS Package Kit
  - Published: 2026-07-11T00:32:34+00:00
  - Link: https://www.rapid7.com/blog/post/pt-weekly-metasploit-update-exploits-for-flowiseai-csv-agent-and-macos-package-kit
  - Summary: More AI, more software, more bugs! AI, it's all you hear about nowadays and everyone's got an opinion on it. Here at Metasploit, we care less about those opinions and more about the growing attack surface all this new software brings with it (yeehaw exploits!). Take for example the new Flowise CSV Agent Prompt Injection RCE brought to you by Takahiro Yokoyama and zdi-disclosures. Flowise is an open-source tool that lets you build AI apps and chatbots using a visual, drag-and-drop canvas and CVE-2026-41264 is an unauthenticated RCE run method of the CSV_Agents class in Flowise. The vulnerability exists due insufficient sandboxing and an incomplete list of disallowed inputs. It allows unauthenticated attackers to upload a .csv file containing arbitrary python code and execute it. One moment you're using AI to help draft and email and the next moment you're getting pwn'd, what a world we live in! Happy Friday and happy hacking everyone. New module content (3) Apache .htaccess Persistence
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: New macOS malware steals passwords by posing as Apple’s crash-reporting tool
  - Published: 2026-07-14T13:46:10+00:00
  - Link: https://www.helpnetsecurity.com/2026/07/14/crashstealer-macos-infostealer-password-theft/
  - Summary: Jamf Threat Labs has uncovered a new macOS infostealer named CrashStealer that disguises itself as Apple’s crash-reporting tool to steal passwords, Keychain data, and cryptocurrency wallets. The malware was first spotted in May while it was still under development. By early July, Jamf was seeing in-the-wild detections, indicating it had moved into active use. “Unlike much of the commodity stealer activity on macOS, which is built on AppleScript droppers or thin Objective-C wrappers, CrashStealer is … More → The post New macOS malware steals passwords by posing as Apple’s crash-reporting tool appeared first on Help Net Security .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New CrashStealer malware poses as Apple crash reporting tool
  - Published: 2026-07-13T19:04:02+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-crashstealer-malware-poses-as-apple-crash-reporting-tool/
  - Summary: A new macOS information-stealing malware called CrashStealer pretends to be Apple's crash-reporting tool to steal credentials, keychain data, and crypto wallets. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CrashStealer macOS Malware Uses Notarized Dropper to Pass Gatekeeper Checks
  - Published: 2026-07-13T17:36:12+00:00
  - Link: https://thehackernews.com/2026/07/crashstealer-macos-malware-uses.html
  - Summary: Cybersecurity researchers have flagged a new macOS information stealer called CrashStealer that's capable of harvesting sensitive data from compromised systems. Unlike other information stealers that are built on AppleScript droppers or Objective-C-based wrappers, CrashStealer is implemented in native C++, according to Jamf Threat Labs. "It validates the victim's login password locally before

### Cluster 14c6bae9ae — score 29

- Title: Maximum-Severity Adobe ColdFusion Flaw Exploited Within Hours of Disclosure
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-08T14:47:46+00:00
- Link: https://orca.security/resources/blog/adobe-coldfusion-rce-flaw-cve-2026-48282/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48282

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, web_shell_backdoor
- affected_industries: financial_services, government, healthcare
- cve_ids: CVE-2026-48282
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: data_breach, web_shell_backdoor, active_exploitation
- affected_industries: healthcare, financial_services, government
- cve_ids: CVE-2026-48282
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A critical vulnerability (CVE-2026-48282, CVSS 10.0) was disclosed affecting Adobe ColdFusion, allowing attackers to achieve full remote code execution via a path traversal in the Remote Development Services (RDS) FILEIO handler. Due to the potential for complete server compromise and the confirmed in-the-wild exploitation, immediate patching is required. About CVE-2026-48282 The issue originates from the […]
```

#### Full body

```
A critical vulnerability ( CVE-2026-48282 , CVSS 10.0) was disclosed affecting Adobe ColdFusion, allowing attackers to achieve full remote code execution via a path traversal in the Remote Development Services (RDS) FILEIO handler. Due to the potential for complete server compromise and the confirmed in-the-wild exploitation, immediate patching is required. About CVE-2026-48282 The issue originates from the RDS FILEIO endpoint at /CFIDE/main/ide.cfm?ACTION=FILEIO, where insufficient path validation leads to arbitrary file write on the underlying file system. By sending a specially crafted HTTP request, attackers can upload a CFML webshell containing <cfexecute> tags, potentially gaining full remote code execution as the ColdFusion service account (NT AUTHORITY\SYSTEM on Windows). No authentication is required to exploit this issue when RDS authentication is disabled. Adobe addressed this flaw on June 30, 2026 as part of security bulletin APSB26-68, which resolved 11 ColdFusion vulnerabilities total, seven of which carried a CVSS score of 10.0. Users should upgrade to ColdFusion 2025 Update 10 or ColdFusion 2023 Update 21 immediately. Organizations that have not yet patched should also disable RDS unless strictly required, block external access to /CFIDE/administrator and RDS endpoints via WAF or firewall rules, and hunt for unauthorized .cfm, .cfc, .cfml, or .jsp files in the ColdFusion web root. Affected Systems The following components are affected: Adobe ColdFusion 2025, update 9 and earlier, and Adobe ColdFusion 2023, update 20 and earlier. These components are deployed across enterprise web application stacks, including government, financial, and healthcare organizations, particularly when RDS is enabled and RDS authentication is left in its default disabled state. Other applications relying on ColdFusion as a backend runtime may also be impacted. Risk Impact At the time of writing, a detailed technical analysis from WatchTowr is publicly available and serves as a functional exploitation guide. KEVIntel honeypots detected active exploitation within two hours of that analysis going public, and both the Canadian Centre for Cyber Security and the Centre for Cybersecurity Belgium have issued alerts. Shadowserver tracks approximately 750 to 800 internet-facing ColdFusion instances, though the actual vulnerable subset depends on RDS configuration. Regardless, the maximum severity score, the lack of authentication requirements, and the speed of exploitation make this vulnerability extremely high risk, especially in internet-facing deployments. Successful exploitation could allow attackers to deploy webshells for persistent access, execute arbitrary commands on the underlying operating system, and pivot laterally through the network, leading to service disruption, data exposure, or full infrastructure compromise. Organizations should also rotate credentials on any ColdFusion server that was internet-facing since the June 30 disclosure date. How Orca Can Help Orca enables customers to quickly identify assets running vulnerable versions of Adobe ColdFusion, understand their exposure in context, including internet accessibility, runtime reachability, and asset criticality, and prioritize remediation based on real risk rather than CVSS alone. Orca’s platform highlights affected assets directly in the alert view, helping security teams focus on the most critical remediation paths first. Related articles Product Info Post-Quantum Cryptography Is Here. Orca Can Help. Jul 10, 2026 Cloud Security Learning Cloud Risk Reduction Strategies for Fintech Jul 10, 2026 Report 2026 State of AI Security Report Jul 09, 2026 Stay in the loop Keep up to date with everything you need to know about cloud security and our latest research By submitting my email address I agree to the use of my personal data in accordance with Orca Security Privacy Policy . Personalized Demo See Orca Security in Action Gain visibility, achieve compliance, and prioritize ri
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Maximum-Severity Adobe ColdFusion Flaw Exploited Within Hours of Disclosure
  - Published: 2026-07-08T14:47:46+00:00
  - Link: https://orca.security/resources/blog/adobe-coldfusion-rce-flaw-cve-2026-48282/
  - Summary: A critical vulnerability (CVE-2026-48282, CVSS 10.0) was disclosed affecting Adobe ColdFusion, allowing attackers to achieve full remote code execution via a path traversal in the Remote Development Services (RDS) FILEIO handler. Due to the potential for complete server compromise and the confirmed in-the-wild exploitation, immediate patching is required. About CVE-2026-48282 The issue originates from the […]

### Cluster 7df2f246d4 — score 28

- Title: Defending SaaS-based applications against ShinyHunters OAuth abuse
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-07-13T22:02:41+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: cloud_abuse, phishing_social_eng, ransomware_extortion, supply_chain
- actor_attribution: ShinyHunters
- affected_industries: education, manufacturing_industrial, retail_ecommerce
- affected_products: Microsoft Defender, Salesforce
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, cloud_abuse
- actor_attribution: ShinyHunters
- affected_industries: manufacturing_industrial, education, retail_ecommerce
- affected_products: Salesforce, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Threat Intelligence identified threat actor activity with overlapping tradecraft commonly associated with ShinyHunters, including voice phishing (vishing), supply-chain compromise, and misconfigured guest access targeting SaaS-based applications. The post Defending SaaS-based applications against ShinyHunters OAuth abuse appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Social engineering Supply chain attack Vishing Content types Research Products and services Microsoft Defender Topics Actionable threat insights In a series of campaigns observed between mid-2025 and mid-2026, Microsoft identified threat actor activity with overlapping tradecraft commonly associated with ShinyHunters, including voice phishing (vishing), supply chain compromise, and misconfigured guest access to target customer SaaS-based applications such as Salesforce instances. The threat actors abused trusted OAuth relationships for unauthorized access, data exfiltration, and persistence. Three primary intrusion paths were observed including vishing techniques targeting OAuth consent, supply chain compromise through trusted workflows and integrations such as Salesloft and Gainsight, and exploitation of misconfigured guest access. Abuse of these access paths led to inherited user and application privileges, allowing successful enumeration and querying of customer relationship management (CRM) records while evading conventional authentication detections. These intrusion paths often led to persistent access and exfiltration of data at scale. This tradecraft highlights how a single entry point can rapidly expand to greater enterprise impacts. Microsoft observed activity associated with these techniques in many tenants from various industries such as retail, education and manufacturing. These findings reinforce the importance of monitoring OAuth-connected applications, validating third-party integrations, reviewing guest access configurations, and enabling Salesforce event monitoring. Leveraging this data, Microsoft consulted with Salesforce to improve granularity in telemetry for Defender for Cloud Apps with near-real-time detection, offering connected application attribution and expanded application permission insights. This activity was not the result of a vulnerability inherent to Salesforce. Rather, the threat actors abused trusted OAuth relationships for unauthorized access, data exfiltration, and persistence. Attack chain overview Threat actor campaigns targeting Salesforce customers and using tradecraft associated with ShinyHunters pose a high-impact risk to sensitive data and downstream SaaS ecosystems. These campaigns abuse OAuth trust relationships to operate within pre-existing, legitimate workflows. Figure 1. Commonly observed attack paths for SaaS applications. Observed activity can be grouped into three primary intrusion paths: Voice ‑ phishing-driven OAuth consent abuse In campaigns beginning in mid-2025, the threat actors conducted vishing attacks impersonating IT support personnel. Threat actors socially engineered employees into authorizing attacker-controlled connected apps within their Salesforce tenant. In several confirmed cases, threat actors guided users through the OAuth consent workflow to grant access to a malicious application disguised as a legitimate Salesforce Data Loader tool. After users granted consent, these highly privileged OAuth applications enabled threat actors to perform API calls on behalf of the victim user, facilitating: Enumeration of Salesforce instances belonging to targeted organizations Persistent access to Salesforce CRM data Possible lateral movement into other SaaS platforms through discovered credentials This intrusion path exploits the OAuth authorization flow of trusted SaaS services rather than relying on malware or credential replay. Threat actors exfiltrate data through sanctioned application access inherited from user privileges. SaaS supply ‑ chain compromise targeting trusted integrations Following initial access campaigns, threat actors escalated into supply‑chain-driven attacks targeting third‑party SaaS vendors offering popular solutions that integrate with Salesforce, often using OAuth tokens. In August 2025, compromised Salesloft Drift credentials enabled attackers to obtain connection secrets used by downstream SaaS applicati
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Defending SaaS-based applications against ShinyHunters OAuth abuse
  - Published: 2026-07-13T22:02:41+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/
  - Summary: Microsoft Threat Intelligence identified threat actor activity with overlapping tradecraft commonly associated with ShinyHunters, including voice phishing (vishing), supply-chain compromise, and misconfigured guest access targeting SaaS-based applications. The post Defending SaaS-based applications against ShinyHunters OAuth abuse appeared first on Microsoft Security Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity
  - Published: 2026-07-14T06:19:24+00:00
  - Link: https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
  - Summary: Attackers whose methods line up with the data-extortion group ShinyHunters have spent the past year walking into corporate Salesforce environments without exploiting a single flaw in the platform. The way in has been the trust the organization had already extended, usually through the OAuth connections that tie Salesforce to the apps and third-party vendors around it. In

### Cluster 8e87b71464 — score 23

- Title: CVE-2026-9181 | Esri ArcGIS Server Pre-Authentication Path Traversal Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-08T17:00:06+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-9181/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-9181

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-20230, CVE-2026-47729, CVE-2026-48283, CVE-2026-48313, CVE-2026-9181
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-9181, CVE-2026-48283, CVE-2026-48313, CVE-2026-20230, CVE-2026-47729
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-9181 is a critical path traversal vulnerability affecting Esri ArcGIS Server that could allow unauthenticated attackers to access sensitive files. Validate exposure with NodeZero® Rapid Response.
```

#### Full body

```
CVE-2026-9181 Esri ArcGIS Server Pre-Authentication Path Traversal Vulnerability CVE-2026-9181 is a critical pre-authentication path traversal vulnerability affecting Esri ArcGIS Server 12.0 and prior. The vulnerability exists in the ArcGIS Server REST Uploads resource, where insufficient validation of crafted path parameters allows an unauthenticated remote attacker to traverse outside the intended directory boundary. Successful exploitation could allow an attacker to access sensitive files on the ArcGIS Server system without requiring valid credentials. The vulnerability has a CVSS v3.1 base score of 9.8 (Critical) . Technical Details CVE-2026-9181 is a path traversal vulnerability (CWE-22) within the ArcGIS Server REST Uploads resource. By supplying a crafted itemName parameter, an attacker can bypass path validation and traverse outside the intended upload directory. Successful exploitation could allow an unauthenticated attacker to access sensitive files on the ArcGIS Server system. The vulnerability is remotely exploitable over the network, requires no authentication, and requires no user interaction. Vendor: Esri Product: ArcGIS Server Vulnerability Class: Path Traversal (CWE-22) Authentication Required: None Attack Vector: Network CVSS v3.1 Base Score: 9.8 (Critical) Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this vulnerability can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether exploitation is possible. Patch immediately: Apply the ArcGIS Server Security 2026 Update 2 Patch or the vendor-recommended mitigation. Re-run the test: Confirm the vulnerability is no longer exploitable after remediation. Affected Versions & Patch Affected ArcGIS Server 12.0 and prior Fixed Esri recommends customers running the following supported releases install the ArcGIS Server Security 2026 Update 2 Patch : ArcGIS Server 12.0 ArcGIS Server 11.5 ArcGIS Server 11.4 ArcGIS Server 11.3 ArcGIS Server 11.1 Mitigations Apply the ArcGIS Server Security 2026 Update 2 Patch as soon as possible. The security update is cumulative and does not require previous ArcGIS Server security patches to be installed. If immediate patching is not possible, Esri recommends implementing the Web Application Firewall (WAF) guidance described in the ArcGIS Enterprise Hardening Guide until the security update can be applied. Timeline May 27, 2026: Esri published the May 2026 ArcGIS Security Bulletin describing CVE-2026-9181. May 27, 2026: Esri released the ArcGIS Server Security 2026 Update 2 Patch. May 27, 2026: Esri recommended ArcGIS Enterprise customers apply the security update within two weeks to reduce exposure. July 8, 2026: Horizon3.ai Rapid Response test. References Esri May 2026 ArcGIS Security Bulletin ArcGIS Server Security 2026 Update 2 Patch CVE.org Record: CVE-2026-9181 NIST National Vulnerability Database: CVE-2026-9181 Read about other CVEs CVE-2026-48283 / CVE-2026-48313 CVE-2026-48283 / CVE-2026-48313: Adobe ColdFusion Pre-Authentication Unrestricted File Upload and Path Traversal Vulnerabilities Read more CVE-2026-20230 CVE-2026-20230 is a critical server-side request forgery vulnerability affecting Cisco Unified CM. Successful exploitation may lead to root-level compromise, and… Read more CVE-2026-47729 CVE-2026-47729 (Squidbleed) can expose credentials, cookies, API keys, and session tokens from memory in vulnerable Squid proxy deployments. Read more NodeZero ® Platform Implement a continuous find, fix, and verify loop with NodeZero The NodeZero ® platform empowers your organization to reduce your security risks by autonomously finding exploitable weaknesses in your network, giving you detailed guidance around how to priortize and fix the
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-9181 | Esri ArcGIS Server Pre-Authentication Path Traversal Vulnerability
  - Published: 2026-07-08T17:00:06+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-9181/
  - Summary: CVE-2026-9181 is a critical path traversal vulnerability affecting Esri ArcGIS Server that could allow unauthenticated attackers to access sensitive files. Validate exposure with NodeZero® Rapid Response.

### Cluster 08882287bf — score 20

- Title: iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-13T05:36:02+00:00
- Link: https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48939

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: government
- affected_products: WordPress
- cve_ids: CVE-2025-12352, CVE-2025-6389, CVE-2025-7852, CVE-2026-48939, CVE-2026-56291
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: government
- affected_products: WordPress
- cve_ids: CVE-2026-48939, CVE-2026-56291, CVE-2025-6389, CVE-2025-7852, CVE-2025-12352
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added two maximum-severity security flaws impacting iCagenda and Balbooa extensions for Joomla to its Known Exploited Vulnerabilities (KEV) catalog, following reports of zero-day exploitation in the wild. The vulnerabilities, both rated 10.0 on the CVSS scoring system, are below - CVE-2026-48939 - A vulnerability in the
```

#### Full body

```
iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days  Ravie Lakshmanan  Jul 13, 2026 Vulnerability / Web Security The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added two maximum-severity security flaws impacting iCagenda and Balbooa extensions for Joomla to its Known Exploited Vulnerabilities ( KEV ) catalog, following reports of zero-day exploitation in the wild. The vulnerabilities, both rated 10.0 on the CVSS scoring system, are below - CVE-2026-48939 - A vulnerability in the iCagenda extension for Joomla that allows the upload of arbitrary files via the file attachment feature, leading to PHP code upload and execution. CVE-2026-56291 - A vulnerability in the Balbooa Forms extension for Joomla that allows the upload of arbitrary files, leading to remote code execution. According to mySites.guru, a cloud-based dashboard service for managing WordPress and Joomla websites, CVE-2026-48939 is said to have been exploited as a zero-day since June 15, 2026, in automated attacks aimed at Joomla sites on which iCagenda is installed. It resides in the "Submit an Event" form functionality, which lets users propose events for the calendar. "We first saw it in a client's access log: an automated scanner identifying itself as 'icagenda-batch/1.0' grabbed a token, posted a malicious upload to the submit endpoint, then fetched the planted shell at the exact path the component writes attachments to," mySites.guru said . The flaw impacts the following versions - 4.x versions up to and including 4.0.7 Legacy 3.x versions from 3.2.1 up to and including 3.9.14 JoomliC has since released updates to address the issue in iCagenda versions 4.0.8 and 3.9.15. Site owners are advised to check for suspicious PHP files in the "images/icagenda/frontend/attachments/" folder and remove them. MySites.guru said it also observed zero-day exploitation of CVE-2026-56291, which affects Balbooa Forms versions up to and including 2.4.0. It has been patched in version 2.4.1. "Up to and including version 2.4.0, its frontend attachment upload had a serious flaw: it accepted a file from any anonymous visitor, with no login, no CSRF token, and no check on the file type," it said . "An attacker could upload a PHP file into a public folder and then run it, which is unauthenticated remote code execution, the worst outcome a web flaw can have." The vulnerability was discovered by mySites.guru on July 8, 2026, following a live attack on one of its customers. It has shared the following indicators of compromise - Look in the Balbooa Forms upload folder (by default "images/baforms/uploads") for any file that is not an image or document, especially anything ending in PHP Check the Joomla user list for suspicious administrator accounts Audit the set for recently modified or unfamiliar PHP files across the site In light of active exploitation, Federal Civilian Executive Branch (FCEB) agencies have until July 13, 2026, to implement the fixes in their networks. Australia Warns of Global Campaign Targeting Vulnerable CMS Systems The disclosure comes as the Australian Cyber Security Centre (ACSC) issued an alert warning of a global exploitation campaign targeting various vulnerabilities in content management systems (CMS) and plugins. "As part of this campaign, malicious cyber actors are actively scanning websites for opportunities to deploy web shells, leveraging various vulnerabilities affecting CMS software and plugins," the agency said . "These vulnerabilities primarily allow unauthenticated file upload, remote code execution, server side request forgery or deserialization." Once deployed, the web shells serve as conduits for remote access and control of the targeted web servers. Some of the identified security vulnerabilities are listed below - Sneeit Framework ( CVE-2025-6389 ) WPBookit (WordPress) ( CVE-2025-7852 ) Gravity Forms (WordPress) ( CVE-2025-12352 ) Craft CMS ( CVE-2025-32432 ) Ninja Forms (WordPress) ( CVE-2026-0740 ) Ma
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days
  - Published: 2026-07-13T05:36:02+00:00
  - Link: https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added two maximum-severity security flaws impacting iCagenda and Balbooa extensions for Joomla to its Known Exploited Vulnerabilities (KEV) catalog, following reports of zero-day exploitation in the wild. The vulnerabilities, both rated 10.0 on the CVSS scoring system, are below - CVE-2026-48939 - A vulnerability in the

### Cluster 843dce4060 — score 19

- Title: CVE-2026-48283 / CVE-2026-48313 | Adobe ColdFusion Pre-Authentication Unrestricted File Upload and Path Traversal Vulnerabilities
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-07T17:25:19+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48283-cve-2026-48313/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48283, CVE-2026-48313

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: education, financial_services, government, healthcare
- cve_ids: CVE-2026-48283, CVE-2026-48313
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: healthcare, financial_services, government, education
- cve_ids: CVE-2026-48283, CVE-2026-48313
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-48283 / CVE-2026-48313: Adobe ColdFusion Pre-Authentication Unrestricted File Upload and Path Traversal Vulnerabilities
```

#### Full body

```
CVE-2026-48283 / CVE-2026-48313 Adobe ColdFusion Pre-Authentication Unrestricted File Upload and Path Traversal Vulnerabilities Adobe has released security updates for multiple vulnerabilities affecting Adobe ColdFusion, including two Critical vulnerabilities tracked as CVE-2026-48283 and CVE-2026-48313 . CVE-2026-48283 is an unauthenticated unrestricted file upload vulnerability that can lead to remote code execution, while CVE-2026-48313 is an unauthenticated path traversal vulnerability in the ColdFusion CKEditor filemanager connector that can expose sensitive files outside the intended directory structure. Both vulnerabilities affect Adobe ColdFusion 2025 Update 9 and earlier and Adobe ColdFusion 2023 Update 20 and earlier. Adobe has stated it is not aware of either vulnerability being exploited in the wild at the time of publication. Technical Details Adobe ColdFusion is a commercial web application development platform widely used across government, healthcare, financial services, higher education, and enterprise environments to build and host dynamic web applications. CVE-2026-48283 is an unauthenticated unrestricted file upload vulnerability (CWE-434) that can result in arbitrary code execution. A remote attacker can upload a malicious file to a vulnerable ColdFusion server without authentication or user interaction, resulting in code execution in the context of the current ColdFusion service account. The vulnerability has a CVSS v3.1 score of 10.0 (Critical) . CVE-2026-48313 is an unauthenticated path traversal vulnerability (CWE-22) affecting the ColdFusion CKEditor filemanager connector. Successful exploitation allows an attacker to read sensitive files outside the intended directory structure and perform limited file writes. Configuration files containing credentials or other sensitive information may also be exposed, enabling additional compromise. The vulnerability has a CVSS v3.1 score of 9.3 (Critical) . Both vulnerabilities have a changed scope, meaning successful exploitation can impact resources beyond the vulnerable ColdFusion instance itself. Although Adobe has not observed exploitation in the wild, both vulnerabilities require no authentication and are remotely exploitable, making them high-priority patching targets. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether these vulnerabilities can be exploited in your environment. The test executes real attack techniques without causing damage, giving security teams immediate clarity into whether vulnerable Adobe ColdFusion instances are actually exploitable. Run the Rapid Response test: Launch the Rapid Response test from the NodeZero platform to determine whether CVE-2026-48283 or CVE-2026-48313 can be exploited in your environment. Patch immediately: Upgrade to Adobe ColdFusion 2025 Update 10 or Adobe ColdFusion 2023 Update 21, or implement Adobe’s recommended mitigations if immediate patching is not possible. Re-run the test: Confirm the vulnerabilities are no longer exploitable after remediation. Affected versions & patch Affected Adobe ColdFusion 2025 Update 9 and earlier Adobe ColdFusion 2023 Update 20 and earlier Fixed Adobe ColdFusion 2025 Update 10 Adobe ColdFusion 2023 Update 21 Mitigations Adobe recommends updating affected ColdFusion installations immediately. If immediate patching is not possible, organizations should restrict network access to ColdFusion administration interfaces and file upload functionality until the updates can be applied. Timeline June 30, 2026: Adobe published Security Bulletin APSB26-68 and disclosed CVE-2026-48283 and CVE-2026-48313. June 30, 2026: Adobe released ColdFusion 2025 Update 10 and ColdFusion 2023 Update 21 to remediate the vulnerabilities. June 30, 2026: Adobe reported it was not aware of any exploitation of either vulnerability in the wild. July 1, 2026: Public reporting highlighted th
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-48283 / CVE-2026-48313 | Adobe ColdFusion Pre-Authentication Unrestricted File Upload and Path Traversal Vulnerabilities
  - Published: 2026-07-07T17:25:19+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48283-cve-2026-48313/
  - Summary: CVE-2026-48283 / CVE-2026-48313: Adobe ColdFusion Pre-Authentication Unrestricted File Upload and Path Traversal Vulnerabilities

### Cluster 3e3af8b34c — score 18

- Title: CISA warns of actively exploited RCE flaws in Joomla extensions
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-13T15:20:16+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-rce-flaws-in-joomla-extensions/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor, zero_day
- affected_industries: government
- affected_products: Ubiquiti UniFi
- cve_ids: CVE-2026-48939, CVE-2026-56291
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor, active_exploitation
- affected_industries: government
- affected_products: Ubiquiti UniFi
- cve_ids: CVE-2026-48939, CVE-2026-56291
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning that attackers are exploiting vulnerabilities in the iCagenda and Balbooa Forms extensions for Joomla to achieve remote code execution through arbitrary file uploads. [...]
```

#### Full body

```
CISA warns of actively exploited RCE flaws in Joomla extensions By Bill Toulas July 13, 2026 11:20 AM 0 The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning that attackers are exploiting vulnerabilities in the iCagenda and Balbooa Forms extensions for Joomla to achieve remote code execution through arbitrary file uploads. The agency has categorized the flaws as a maximum priority , ordering federal agencies to apply available security updates and/or mitigations within three days, with the deadline set for today. The first flaw, tracked as CVE-2026-48939, is an arbitrary file upload flaw impacting the iCagenda extension used for registering and scheduling events and creating calendars. An attacker can exploit the vulnerability to upload arbitrary files to the web server, including PHP scripts, which can lead to data theft, web shell installation, and complete website compromise by achieving remote code execution (RCE). “iCagenda contains an unrestricted upload of file with dangerous type vulnerability that allows the upload of arbitrary files in the file attachment feature, ultimately resulting in PHP code upload and execution,” CISA warns in its entry in the Known Exploited Vulnerabilities ( KEV ) catalog. The second flaw added to KEV is CVE-2026-56291, an arbitrary file upload issue in the Balbooa Forms extension for Joomla. Balbooa Forms is a drag-and-drop form builder for creating contact forms on Joomla sites, with file upload support. According to CISA, this functionality can be used to upload dangerous file types, such as executable files, leading to RCE and full website takeover. According to website management and security platform mySites.guru, both flaws were exploited in automated attacks before vendors released a patch. For iCagenda, attacks were observed just a few hours before the release of version 4.0.8, which addressed CVE-2026-48939. The management service says that the CVE-2026-56291 vulnerability in Balbooa Forms was exploited as a zero-day , leveraged in attacks since July 8, a day before the vendor released a fix for the issue. Website administrators managing Joomla sites should check for the presence of iCagenda and Balbooa Forms and take action where needed to protect their assets. The flaws are fixed in iCagenda version 4.0.8 and 3.9.15, released on June 15-16, and Balbooa Forms version 2.4.1, released on July 9. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: CISA orders feds to prioritize patching Langflow auth bypass flaw Critical Langflow RCE flaw exploited to hack AI app servers CISA warns of max severity Ubiquiti flaws exploited in attacks CISA sets urgent deadline to fix Cisco flaw exploited in attacks CISA orders feds to patch max severity Joomla plugin flaw by Friday
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA warns of actively exploited RCE flaws in Joomla extensions
  - Published: 2026-07-13T15:20:16+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-warns-of-actively-exploited-rce-flaws-in-joomla-extensions/
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning that attackers are exploiting vulnerabilities in the iCagenda and Balbooa Forms extensions for Joomla to achieve remote code execution through arbitrary file uploads. [...]

### Cluster dc767c83a1 — score 18

- Title: M-Red-Team: AsyncAPI Supply Chain Compromise via GitHub Actions
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-07-14T10:33:36+00:00
- Link: https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions
- Fetch status: ok
- Member count: 9
- Corroborating source count: 6
- Strong signals: GitHub, npm

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, ddos, supply_chain, web_shell_backdoor
- affected_industries: financial_services
- affected_products: GitHub, npm
- tools_used: OpenAI/ChatGPT
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: GitHub, npm
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Detect and mitigate malicious @asyncapi npm packages linked to the latest npm supply chain attack.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo On July 14, 2026, an attacker opened 37 pull requests to the AsyncAPI generator repository. Almost all attempted to add a fake charity donation page. Camouflage in the noise, a single PR exploited a misconfigured GitHub Actions workflow to steal a highly privileged Personal Access Token. Four malicious npm packages (five total versions) were published under the @asyncapi namespace . The packages contain a multi-stage payload that establishes persistence and connects to command and control infrastructure. Combined, these packages see over three million downloads a week. In this case, the payload executes on import/require, not install. This does not appear directly connected to the previous compromise of @asyncapi in the Shai-Hulud 2.0 attack. What Happened? The attacker exploited a vulnerability class known as a "pwn request" in GitHub Actions. The asyncapi/generator repository contained a workflow file that used pull_request_target to trigger on pull requests, but then checked out the pull request's code rather than the base branch. The vulnerable workflow This is dangerous because pull_request_target runs in the context of the base repository with full access to secrets. When the workflow checks out attacker-controlled code from the pull request and executes it, those secrets become accessible. Unfortunately, the potential for this vulnerability had been identified months before the attack . On April 29, a contributor opened a PR investigating the issue with a proof-of-concept payload. On May 17, they followed up a proposed fix that split the workflow into two separate jobs to isolate secret access from untrusted code. That fix was still open, unmerged, when the attacker struck 58 days later. At 05:08 UTC, the attacker opened PR #2155 containing a markdown file with obfuscated JavaScript hidden after approximately 1,000 bytes of whitespace. The payload was designed to scan the GitHub Actions runner's environment for secrets and exfiltrate them to a dead-drop URL on the rentry.co pastebin. Automated Review flagging the malicious payload Automated review flagged the obfuscation and while the PR was never merged, the damage was already done. The workflow completed at 05:16 UTC and the attacker was able to retrieve the stolen credentials. The compromised token appears to be a PAT belonging to asyncapi-bot , a service account with access across the AsyncAPI organization. Malicious Packages Published Using the stolen PAT, the attacker pushed a malicious commit directly to the `next` branch at 06:58 UTC . This triggered the release workflow, which published the initial three compromised packages to npm at 07:10 UTC. The attacker then pivoted to the asyncapi/spec-json-schemas repository, pushing 11 commits between 07:51 and 08:28 UTC. Two additional malicious versions of @asyncapi/specs were published. Malicious commits to asyncapi/spec-json-schemas All five versions contain the same payload injected into different files. The malicious code is hidden on the first line of legitimate source files, padded with whitespace to push it off-screen in most editors. Connections to other attacks The payload shares some technical characteristics with the Miasma malware framework previously documented in supply chain attacks. The obfuscation layer uses javascript-obfuscator with a custom base64 alphabet, the same configuration seen in prior incidents. The Stage 3 runtime explicitly self-identifies as "M-RED-TEAM v6.4" in code comments describing beacon encryption and C2 communication protocols. The extracted configuration file sets giteaPackagesOrg to "miasma-test-org." The payload uses miasma-monitor.service within the persistence code. The Nostr relay C2 uses "miasma” branded tags. However, the Rentry dead-drop URL uses the slug "elzotebo," matching naming patterns from the prt-scan campaign, which has been linked to previous pull request-based attacks. The prt-scan campaign has not been linked to Miasma. Beyo
```

#### Corroborating sources (6)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: M-Red-Team: AsyncAPI Supply Chain Compromise via GitHub Actions
  - Published: 2026-07-14T10:33:36+00:00
  - Link: https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions
  - Summary: Detect and mitigate malicious @asyncapi npm packages linked to the latest npm supply chain attack.
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Compromised AsyncAPI packages on npm deliver malware
  - Published: 2026-07-14T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/compromised-asyncapi-npm-packages/
  - Summary: A commit to the AsyncAPI generator GitHub repository injected obfuscated JavaScript into four npm packages with a combined weekly download volume of over 3 million. Here's what we know and how to check if you're affected.
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Multiple Jscrambler Packages Impacted by Supply Chain Attack
  - Published: 2026-07-14T09:04:39+00:00
  - Link: https://www.securityweek.com/multiple-jscrambler-packages-impacted-by-supply-chain-attack/
  - Summary: A threat actor poisoned several Jscrambler NPM package versions to drop a cross-platform credential stealer. The post Multiple Jscrambler Packages Impacted by Supply Chain Attack appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Compromised jscrambler 8.14.0 npm Release Drops Rust Infostealer During Install
  - Published: 2026-07-11T17:59:26+00:00
  - Link: https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html
  - Summary: The jscrambler npm package was compromised, and simply installing its 8.14.0 release runs an infostealer on your machine. Published on July 11, 2026, the malicious version carries a preinstall hook that drops and executes a native binary, one build each for Windows, macOS, and Linux. Socket flagged the release six minutes after it was published. If you or one of your
- **Simon Willison** (ai_security_agentic_risk)
  - Title: datasette code-frequency chart on GitHub
  - Published: 2026-07-13T21:45:27+00:00
  - Link: https://simonwillison.net/2026/Jul/13/datasette-code-frequency/#atom-everything
  - Summary: datasette code-frequency chart on GitHub Out of curiosity I decided to see if I could find a useful illustration of the impact of coding agents and Opus 4.5 class models on my own output. The best I've found so far is this GitHub chart of frequency of code changes to my Datasette open source project: The big spike in activity at the end aligns with Opus 4.8, GPT-5.5, Fable 5 and GPT-5.6 Sol. Tags: github , ai , datasette , generative-ai , llms , ai-assisted-programming , coding-agents
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hackers backdoor Jscrambler npm package with infostealer malware
  - Published: 2026-07-13T19:44:19+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hackers-backdoor-jscrambler-npm-package-with-infostealer-malware/
  - Summary: The Jscrambler client-side web security company disclosed that a threat actor published a malicious version of its npm package that has been downloaded almost 1,500 times. [...]

### Cluster aaaf47b0ea — score 16

- Title: CitrixBleed 2 (CVE-2025-5777) 7Steps to Dragonforce Ransomware | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-07-09T14:00:00+00:00
- Link: https://www.huntress.com/blog/citrixbleed-2-dragonforce-ransomware
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2025-5777

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion, web_shell_backdoor
- affected_products: Anthropic/Claude, Citrix, OpenAI/ChatGPT
- cve_ids: CVE-2025-5777
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, web_shell_backdoor
- affected_products: Citrix, Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2025-5777
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Huntress has observed a series of strikingly similar intrusions beginning with CitrixBleed 2 exploitation, employing novel local privilege escalation techniques, and ending in Dragonforce ransomware.
```

#### Full body

```
Home Blog Seven Steps to Ransomware: CitrixBleed 2 Weaponized by Initial Access Brokers Published: July 9, 2026 Seven Steps to Ransomware: CitrixBleed 2 Weaponized by Initial Access Brokers By: Michael Tigges Anna Pham Anton Ovrutsky Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways Huntress investigated a half-dozen intrusions across unrelated organizations in the first half of 2026 and found the same repeatable seven-step attack chain, suggesting a highly standardized operator playbook rather than one-off compromises. The intrusions began with exploitation of CitrixBleed 2 (CVE-2025-5777), where malformed pre-auth login requests leaked NetScaler memory and enabled attackers to steal and replay valid session tokens, making MFA effectively irrelevant once a live session was hijacked. After gaining access, the attacker followed a consistent post-compromise pattern: escalate to SYSTEM through a registry-symlink/AppMgmt privilege-escalation trick, create rogue local admin accounts, and establish persistence with legitimate remote access tools like ScreenConnect and Zoho Assist. In the most advanced case, the operation ended with DragonForce ransomware deployment, which is why the blog's main takeaway is urgent action: patch exposed NetScaler appliances, retain and review logs, terminate outstanding sessions, and audit for suspicious accounts and remote-management tooling. A special thanks to the Huntress Security Operations Center (SOC) personnel, for without them we'd be describing the below incidents with far more painful details– and Lindsey Welch, who tirelessly proofreads our content on a moment's notice. Additionally, this blog was authored with AI assistance. Introduction Across the first half of 2026, the Huntress Tactical Response unit worked a string of intrusions that all rhymed: an edge Citrix NetScaler gateway, sudden anomalous access to the environment, a tidy privilege-escalation, a fake "Citrix" administrator account, off-the-shelf remote-access software, and when the operator got what they wanted—Dragonforce ransomware. Huntress assesses with high confidence that an Initial Access Broker (IAB) is weaponizing CVE-2025-5777 (CitrixBleed 2) to gain access to Citrix environments, ultimately with the goal of deploying ransomware. In our observations, the ransomware deployed was Dragonforce, but public and private reporting finds indicators of other ransomware groups using this cluster as well, which forms the basis of our Initial Access Broker assessment. Background If you've investigated cybersecurity incidents for long enough, you know that most intrusions look a little different from one another. You learn to live with ambiguity: an RMM here, a phishing lure there, a webshell on a forgotten IIS box. Every so often, though, you work two cases back-to-back and feel a prickle of recognition—the same odd command line, the same throwaway account name, the same misconfiguration the attacker leaned on. Then you work a third. And a fourth. That is what happened with the cluster we're calling, internally and unimaginatively, the Citrix NetScaler cluster . In the first half of 2026 (between January and June) we responded to a half-dozen incidents at unrelated organizations—different industries, different managed service providers, different parts of the country—that were so mechanically similar that by the latest case we could predict the next artifact before we pulled the log that contained it. We knew the account name the operator would create. We knew the service they'd abuse. We even knew the workstation name we'd find leaking through a printer mapping, because it was the same workstation name every single time. Figure 1: Predictability and clustered behavior often presents the smoking gun for initial access. Cybersecurity company Sophos has additionally tracked the cluster we've observed as STAC3725 , echoing various analyses that we've presented in this article, and serves as an excellent va
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: CitrixBleed 2 (CVE-2025-5777) 7Steps to Dragonforce Ransomware | Huntress
  - Published: 2026-07-09T14:00:00+00:00
  - Link: https://www.huntress.com/blog/citrixbleed-2-dragonforce-ransomware
  - Summary: Huntress has observed a series of strikingly similar intrusions beginning with CitrixBleed 2 exploitation, employing novel local privilege escalation techniques, and ending in Dragonforce ransomware.

### Cluster 118be3a32e — score 16

- Title: WolfSSL, GeoVision, VTK vulnerabilities
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-09T18:52:29+00:00
- Link: https://blog.talosintelligence.com/wolfssl-vulnerabilities/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Cisco

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, vulnerability_disclosure
- affected_industries: healthcare
- affected_products: Cisco
- cve_ids: CVE-2026-12486, CVE-2026-12488, CVE-2026-25106, CVE-2026-28739, CVE-2026-33091
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- affected_industries: healthcare
- affected_products: Cisco
- cve_ids: CVE-2026-28739, CVE-2026-25106, CVE-2026-33091, CVE-2026-12488, CVE-2026-12486
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in WolfSSF, fourteen in GeoVision, and one vulnerability in VTK-DICOM. The vulnerabilities mentioned in this blog post have been patched by their respective vendors, in adherence to Cisco’s third-party vulnerability disclosure policy . For
```

#### Full body

```
WolfSSL, GeoVision, VTK vulnerabilities By Kri Dontje Thursday, July 9, 2026 14:52 Vulnerability Roundup Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in WolfSSF, fourteen in GeoVision, and one vulnerability in VTK-DICOM. The vulnerabilities mentioned in this blog post have been patched by their respective vendors, in adherence to Cisco’s third-party vulnerability disclosure policy . For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from Snort.org , and our latest Vulnerability Advisories are always posted on Talos Intelligence’s website . WolfSSL vulnerabilities Discovered by Ankur Tyagi of Cisco Talos. WolfSSL aims to provide "lightweight and embedded security solutions" for both individual and business needs. WolfSSL is an open-source product to provide secure data transfer. Talos discovered two improper input validation vulnerabilities ( TALOS-2026-2409 (CVE-2026-28739) and TALOS-2026-2410 (CVE-2026-25106)) and one integer underflow vulnerability ( TALOS-2026-2408 (CVE-2026-33091)) in WolfSSL. GeoVision vulnerabilities Discovered by Philippe Laulheret of Cisco Talos. GeoVision specializes in security technologies, including cameras and monitoring solutions, access control, and machine-identification. Talos released 14 advisories for GeoVision vulnerabilities, covering 37 CVEs: TALOS-2026-2411 (CVE-2026-12488) memory corruption vulnerabilities TALOS-2026-2379 (CVE-2026-12486, CVE-2026-12849, CVE-2026-12850, CVE-2026-12851) OS command injection vulnerabilities TALOS-2026-2377 (CVE-2026-12485, CVE-2026-12846, CVE-2026-12847, CVE-2026-12848) buffer overflow vulnerabilities TALOS-2026-2369 (CVE-2026-42370) stack overflow vulnerability TALOS-2026-2333 (CVE-2026-7372, CVE-2026-42369) stack overflow vulnerabilities TALOS-2026-2329 (CVE-2026-42368) privilege escalation vulnerability TALOS-2026-2328 (CVE-2026-42367) privilege escalation vulnerability TALOS-2026-2327 (CVE-2026-7371, CVE-2026-42366) reflected cross-site scripting (XSS) vulnerabilities TALOS-2025-2326 (CVE-2026-42364) OS command injection vulnerability TALOS-2025-2332 (CVE-2026-42365) guessable session cookie vulnerability TALOS-2025-2322 (CVE-2026-7161) insufficient encryption vulnerability TALOS-2026-2375 (CVE-2026-57273, CVE-2026-57274, CVE-2026-57275, CVE-2026-57276, CVE-2026-57277, CVE-2026-57278) stack-based buffer overflow vulnerabilities TALOS-2026-2373 (CVE-2026-13131, CVE-2026-13132, CVE-2026-57264, CVE-2026-57265, CVE-2026-57266, CVE-2026-57267, CVE-2026-57268, CVE-2026-57269, CVE-2026-57270, CVE-2026-57271, CVE-2026-57272) out-of-bounds read vulnerabilities TALOS-2026-2370 (CVE-2026-13125) lack of authentication vulnerability VTK-DICOM vulnerability Discovered by Emmanuel Tacheau of Cisco Talos. The Virtualization Toolkit (VTK) is an open source software solution for handling scientific data, for use in tools for 3D rendering. The VTK-DICOM API is specifically to allow VTK users to parse Digital Imaging and Communications in Medicine (DICOM) medical data. Talos found one vulnerability in VTK-DICOM, TALOS-2026-2366 (CVE-2026-22879), which is a heap-based buffer overflow vulnerability. Share this post Related Content MediaArea heap-based buffer overflow vulnerabilities May 27, 2026 10:00 Talos researchers find 4 heap-based buffer overflow vulnerabilities in MediaArea's MediaInfoLib. TP-Link, Photoshop, OpenVPN, Norton VPN vulnerabilities May 19, 2026 11:39 Cisco Talos’ Vulnerability Discovery & Research team recently disclosed eight vulnerabilities in TP-Link, and one each in Adobe Photoshop, OpenVPN, and Gen Digital's Norton VPN. Foxit, LibRaw vulnerabilities April 16, 2026 15:00 Cisco Talos’ Vulnerability Discovery & Research team recently disclosed one Foxit Reader vulnerability, and six LibRaw file reader vulnerabilities. The vulnerabilities mentioned in this blog post have been patched by their respective vendors, all in adherence to Cisco’s third-pa
```

#### Corroborating sources (2)

- **Cisco Talos** (threat_research_primary)
  - Title: WolfSSL, GeoVision, VTK vulnerabilities
  - Published: 2026-07-09T18:52:29+00:00
  - Link: https://blog.talosintelligence.com/wolfssl-vulnerabilities/
  - Summary: Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three vulnerabilities in WolfSSF, fourteen in GeoVision, and one vulnerability in VTK-DICOM. The vulnerabilities mentioned in this blog post have been patched by their respective vendors, in adherence to Cisco’s third-party vulnerability disclosure policy . For
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: China-Linked APT Expands Proxy Network With New Malware
  - Published: 2026-07-08T14:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/uat-7810-china-apt-orb-proxy/
  - Summary: Cisco Talos said China-linked APT UAT-7810 is growing its proxy relay network with new malware

### Cluster 55bab88c91 — score 14

- Title: Unpatched Claude for Chrome Flaw Lets Extensions Read Gmail, Calendar
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-14T13:00:00+00:00
- Link: https://www.securityweek.com/unpatched-claude-for-chrome-flaw-lets-extensions-read-gmail-calendar/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 3
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- affected_industries: critical_infrastructure, government, manufacturing_industrial
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, Palo Alto Networks
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- affected_industries: government, critical_infrastructure, manufacturing_industrial
- affected_products: Anthropic/Claude, Palo Alto Networks
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A ClaudeBleed-linked vulnerability reportedly persists across eight patches, exposing potentially sensitive data to other extensions. The post Unpatched Claude for Chrome Flaw Lets Extensions Read Gmail, Calendar appeared first on SecurityWeek .
```

#### Full body

```
AI security firm Manifold says two vulnerabilities it reported to Anthropic in May remain exploitable in the latest version of Claude for Chrome, the company’s agentic browser extension. According to Manifold, the flaws let a malicious browser extension trigger Claude into taking actions on a user’s behalf without any genuine click or approval from the victim. An attacker could exploit them to read Gmail messages, Google Docs documents, and calendar entries. The core issue is related to a fix Anthropic shipped earlier this year in response to a similar vulnerability dubbed ClaudeBleed . That update restricted which prompts an outside webpage could feed into Claude, narrowing the extension’s exposure to a fixed set of pre-approved tasks. Manifold found that the mechanism used to activate those tasks doesn’t verify whether a click actually came from a real user, meaning another extension can fake the interaction and set the process in motion. In the extension’s default setting, the attack triggers a confirmation prompt before anything sensitive happens. However, if a user has enabled the extension’s more autonomous mode (‘Act without asking’), the attacker’s action can proceed without any visible warning. Manifold also flagged a second, related design gap: a way for Claude’s side panel to launch directly into that no-confirmation mode based on a parameter in its own URL, with no user action required to unlock it. Advertisement. Scroll to continue reading. The researchers noted that this is not something an attacker can currently exploit, since only the extension itself is meant to construct that URL. But they argue it’s a structural risk, and any future bug that lets an outside script influence how that URL gets built could hand an attacker silent control over a user’s connected accounts. Manifold reported its findings to Anthropic on May 21, shortly after the public disclosure of the ClaudeBleed research. The AI giant described the list of pre-approved tasks as an initial mitigation for ClaudeBleed until a complete fix is rolled out. However, Manifold says none of the eight versions released since appear to patch the vulnerabilities, including the latest 1.0.80. SecurityWeek has reached out to Anthropic for comment. Related : ‘HalluSquatting’ Turns AI Hallucinations Into Botnet Delivery Mechanism Related : UK Government Rolls Out Agentic AI Defense Plan Alongside Industry Pledge Related : AI Coding Tools Tricked Into Hacking Developer Machine via Decades-Old Technique Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs Centers Laboratory Data Breach Affects 540,000 Individuals Third US Security Expert Sentenced to Prison for Helping Ransomware Gang China, India-Linked Hackers Both Targeted Same Pakistani Police Force ‘HalluSquatting’ Turns AI Hallucinations Into Botnet Delivery Mechanism Palo Alto Networks Patches 13 Vulnerabilities Microsoft Patches Defender ‘RoguePlanet’ Vulnerability AI Coding Tools Tricked Into Hacking Developer Machine via Decades-Old Technique Google Patches 382 Chrome Vulnerabilities Latest News 7 Severe Vulnerabilities Patched in VMware Avi Load Balancer SAP Patches Critical Vulnerabilities in NetWeaver, Approuter, Commerce Cloud US, Allies Warn of Russian Cyberattacks Targeting Critical Infrastructure Routers Valarian Raises $50 Million for Sovereign Infrastructure Control Layer Multiple Jscrambler Packages Impacted by Supply Chain Attack Pentagon Suspends CMMC Phase 2 as It Rethinks Contractor Cybersecurity Rules Hacker Conversations: Jesse McGraw (GhostExodus), From Blackhat
```

#### Corroborating sources (3)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Unpatched Claude for Chrome Flaw Lets Extensions Read Gmail, Calendar
  - Published: 2026-07-14T13:00:00+00:00
  - Link: https://www.securityweek.com/unpatched-claude-for-chrome-flaw-lets-extensions-read-gmail-calendar/
  - Summary: A ClaudeBleed-linked vulnerability reportedly persists across eight patches, exposing potentially sensitive data to other extensions. The post Unpatched Claude for Chrome Flaw Lets Extensions Read Gmail, Calendar appeared first on SecurityWeek .
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Enforce zero data retention on Amazon Bedrock with Bedrock Projects and service control policies
  - Published: 2026-07-07T18:18:52+00:00
  - Link: https://aws.amazon.com/blogs/security/enforce-zero-data-retention-on-amazon-bedrock-with-bedrock-projects-and-service-control-policies/
  - Summary: With the introduction of models that require data sharing with third-party providers—such as Claude Fable 5—organizations need a way to centrally enforce data retention policies. Amazon Bedrock gives you control over whether your prompts and model outputs are retained after an inference request completes. You might need a way to enforce your retention settings across […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Thinking Fast and Slow in the SOC: The Case for Combining Autonomous AI with Analyst Copilots
  - Published: 2026-07-13T11:37:05+00:00
  - Link: https://thehackernews.com/2026/07/thinking-fast-and-slow-in-soc-case-for.html
  - Summary: A few days ago, I was sitting with the CISO of a Fortune 50 company, walking through how his security team was thinking about AI agents in the SOC. Smart team. Serious program. They had already connected Claude to a few detection tools and were seeing real value in specific investigations. But as we mapped out the broader architecture, something kept nagging at me. The design they were building

### Cluster e5476c476d — score 13

- Title: What’s in the SOSS? Podcast #65 – S3E17 Signing the Future: Securing AI and ML Artifacts with Mihai Maruseac
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-07-14T13:32:32+00:00
- Link: https://openssf.org/podcast/2026/07/14/whats-in-the-soss-podcast-65-s3e17-signing-the-future-securing-ai-and-ml-artifacts-with-mihai-maruseac/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
In this episode of What’s in the SOSS?, host Yesenia Yser sits down with Mihai Maruseac (OpenAI) to discuss the OpenSSF Model Signing (OMS) specification, securing the AI/ML supply chain, and establishing a cryptographic chain of custody for models and datasets.
```

#### Full body

```
Summary In this episode of What’s in the SOSS?, host Yesenia Yser sits down with Mihai Maruseac, the lead of the OpenSSF AI/ML Working Group and Security and Privacy expert at OpenAI, to dive deep into the unique security challenges facing artificial intelligence. Unlike traditional software packages, AI models cannot simply be inspected for malware by looking at their weights – malicious code only exposes itself upon execution. Mihai outlines how the community is answering this threat through the evolution of the OpenSSF Model Signing (OMS) specification. Discover how OMS creates an unshakeable chain of custody for models, data sets, and agent workflows, the structural shift toward implementation-agnostic toolchains, and what the future looks like for a fully realized, end-to-end secure AI supply chain. Listen on Apple Podcasts Listen on Spotify Listen on Overcast Listen on Pocket Casts Conversation Highlights 00:22 – Welcome: Yesenia introduces AI/ML Working Group lead Mihai Maruseac. 00:51 – From TensorFlow to OpenAI: Mihai’s journey navigating open source security and AI. 01:47 – Core Risks of Model Tampering: A look at hidden risks inside uninspectable model weights. 03:27 – Establishing Chain of Custody: How cryptographic signatures verify file integrity from training to deployment. 05:04 – Evolution of the OMS Spec: Why the community standardized on forward-compatible, framework-agnostic formats. 07:17 – Tracking Iteration (v1.1 & v1.2): An overview of newly introduced security keys and community features. 08:26 – Choosing Your PKI Tooling: Why the OMS specification remains highly flexible for users. 10:22 – Real-World Integration: Early success stories with Kaggle, NVIDIA, and the path to PyTorch. 12:42 – Looking Ahead to Version 2: Overcoming “attestation sprawl” by unifying multiple security claims. 15:29 – The Ideal AI Supply Chain: Using signed artifacts with GUAC to automatically map vulnerabilities. 17:09 – How to Get Involved: Immediate opportunities to contribute to signature format convergence. 18:11 – Rapid Fire Segment: Mihai shares his favorite retro games, hiking, and love for Vim. 19:37 – Final Words of Advice: Why contributors of all skill levels are welcome to join. Episode Links Mihai Maruseac’s LinkedIn Page OpenSSF Model Signing (OMS) OpenSSF Model Signing Spec GitHub Repo OpenSSF AI/ML Working Group OpenSSF Guide: Visualizing Secure MLOps (MLSecOps): A Practical Guide for Building Robust AI/ML Pipeline Security Graph for Understanding Artifact Composition (GUAC) Sigstore In-toto Ollama Get involved with the OpenSSF Subscribe to the OpenSSF newsletter Follow the OpenSSF on LinkedIn Transcript Intro Music & Promo Clip (00:00) “We have the same problem that exists with traditional software. The difference with AI is that you cannot inspect the models, looking at the weights, you cannot determine if the model is malicious or not. You will discover that only when you execute the model. We have to make sure that we can create a chain of custody between model being released, me being trained and the model being used.” Yesenia (00:22) Hello and welcome to What’s in the SOSS? An OpenSSF podcast where we talk to interesting people throughout the open source ecosystem, sharing their journey, experiences, and wisdom. Soy Yesenia, one of your hosts, and today I have the utmost pleasure of having Mihai here who is a fabulous contributor to the open source space among one of the many groups that I’m not going to spoil them, but you gotta listen to share that which one. Welcome, Mihai. I’d love for you to introduce yourself to the audience. Mihai Maruseac (00:51) Hello, Hello, thank you for having me. So I am Mihai Maruseac and I’ve been working a lot on open source. I am now leading the AI/ML Working Group under OpenSSF. I worked on TensorFlow Security, then Supply Chain Security under Google Open Source Security Team. And now I’m going to work on security and privacy at OpenAI, so everywhere AI and security. Yese
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: What’s in the SOSS? Podcast #65 – S3E17 Signing the Future: Securing AI and ML Artifacts with Mihai Maruseac
  - Published: 2026-07-14T13:32:32+00:00
  - Link: https://openssf.org/podcast/2026/07/14/whats-in-the-soss-podcast-65-s3e17-signing-the-future-securing-ai-and-ml-artifacts-with-mihai-maruseac/
  - Summary: In this episode of What’s in the SOSS?, host Yesenia Yser sits down with Mihai Maruseac (OpenAI) to discuss the OpenSSF Model Signing (OMS) specification, securing the AI/ML supply chain, and establishing a cryptographic chain of custody for models and datasets.

### Cluster 80fad3eb43 — score 13

- Title: “Stern,” Likely Most Prolific Ransomware Operator Ever, Sanctioned by EU as Action Targets Billions in Ransomware Damage
- Source: Chainalysis (ransomware_ecrime_financial_crime)
- Published: 2026-07-14T15:24:02+00:00
- Link: https://www.chainalysis.com/blog/cyber-sanctions-trickbot-administrator-july-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Summary The United States, United Kingdom, and European Union announced sanctions targeting nation-state hackers, cybercriminals, and their enablers in one… The post “Stern,” Likely Most Prolific Ransomware Operator Ever, Sanctioned by EU as Action Targets Billions in Ransomware Damage appeared first on Chainalysis .
```

#### Full body

```
Crime Inside a Sandwich Attack: Lessons From the $7.5 Million Heist Against JaredfromSubway.eth June 26, 2026
```

#### Corroborating sources (1)

- **Chainalysis** (ransomware_ecrime_financial_crime)
  - Title: “Stern,” Likely Most Prolific Ransomware Operator Ever, Sanctioned by EU as Action Targets Billions in Ransomware Damage
  - Published: 2026-07-14T15:24:02+00:00
  - Link: https://www.chainalysis.com/blog/cyber-sanctions-trickbot-administrator-july-2026/
  - Summary: Summary The United States, United Kingdom, and European Union announced sanctions targeting nation-state hackers, cybercriminals, and their enablers in one… The post “Stern,” Likely Most Prolific Ransomware Operator Ever, Sanctioned by EU as Action Targets Billions in Ransomware Damage appeared first on Chainalysis .

### Cluster 5a4c062977 — score 13

- Title: Securing the AI supply chain on GKE: Introducing k8s-aibom for automated AI BOMs
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-07-13T16:00:00+00:00
- Link: https://cloud.google.com/blog/products/identity-security/introducing-k8s-aibom-on-gke-for-automated-ai-bills-of-materials/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
How should your security team manage shadow AI? Workloads deployed by developers without formal registration can often evade traditional security scanners, because organizations are reluctant to slow down development and compromise stability by demanding privileged Daemonsets, kernel-level access, and manual pod-spec edits. To break this deadlock, today we are open-sourcing k8s-aibom . This lightweight, unprivileged Kubernetes controller continuously monitors the cluster API and container environments to automatically detect running AI runtimes (like vLLM and Triton) and generate standard CycloneDX Machine Learning Bill of Materials (ML-BOMs). By providing automated, audit-grade visibility directly from runtime execution — regardless of whether the workload was formally registered — k8s-aibom can help teams safely move AI projects from pilot to production without developer integration friction. The architecture of zero friction k8s-aibom is designed from the ground up to respect both t
```

#### Full body

```
Security & Identity Securing the AI supply chain on GKE: Introducing k8s-aibom for automated AI BOMs July 13, 2026 Glen Messenger Group Product Manager Try Gemini Enterprise Business Edition today The front door to AI in the workplace Try now How should your security team manage shadow AI? Workloads deployed by developers without formal registration can often evade traditional security scanners, because organizations are reluctant to slow down development and compromise stability by demanding privileged Daemonsets, kernel-level access, and manual pod-spec edits. To break this deadlock, today we are open-sourcing k8s-aibom . This lightweight, unprivileged Kubernetes controller continuously monitors the cluster API and container environments to automatically detect running AI runtimes (like vLLM and Triton) and generate standard CycloneDX Machine Learning Bill of Materials (ML-BOMs). By providing automated, audit-grade visibility directly from runtime execution — regardless of whether the workload was formally registered — k8s-aibom can help teams safely move AI projects from pilot to production without developer integration friction. The architecture of zero friction k8s-aibom is designed from the ground up to respect both the CISO mandate for total visibility and the SRE mandate for cluster stability. It deploys as a single, unprivileged Deployment in the k8s-aibom-system namespace. It involves zero developer friction — no sidecars, no eBPF kernel modules, no privileged DaemonSets, and no modifications to existing developer pod specifications. k8s-aibom watches for AI workloads and produces BOMs. The discovery pipeline executes through four clear stages: Scrape cluster workloads : The controller continuously monitors KServe resources, Deployments, StatefulSets, DaemonSets, and Jobs across the cluster. Identify AI stacks : Advanced pattern matching inspects container images, environment variables, and command-line arguments to detect serving runtimes (vLLM, Triton Inference Server, TGI, Ollama), autonomous agent frameworks (LangChain, AutoGen, CrewAI), vector databases and RAG stores (Milvus, Qdrant, pgvector), as well as distributed training jobs and evaluation harnesses. Generate standard manifests : The controller compiles the discovered artifacts into formal OWASP CycloneDX 1.6 Machine Learning Bill of Materials (ML-BOM) documents. Export to sinks : The controller attaches the resulting ML-BOM directly to the custom resource status (status.bomDocument) of an in-cluster AIBOM Custom Resource (CR) and routes it to optional external sinks, including Google Cloud Storage buckets and external webhook endpoints. Application teams do not need to modify their pod specifications, inject sidecar containers, or alter their continuous integration and continuous delivery (CI/CD) pipelines. Furthermore, k8s-aibom treats the Kubernetes cluster state as a pure functional input: Identical cluster inputs produce byte-identical ML-BOM documents. This deterministic property makes k8s-aibom an ideal fit for GitOps workflows, enabling site-reliability engineers (SREs) to perform exact diffs and trigger precise change-detection alerts when AI dependencies drift. Where existing AIBOM tooling falls short Many AI BOM solutions offer build-time scanners producing BOMs from artifacts at rest. These tools help you track the code that was intended to be deployed. Commercial AI security platforms extend the picture with cloud-native posture management, but typically through external scanning shaped around vendor-specific data models. Few, if any, of these tools help compliance reviewers, security operations (SecOps) teams, and platform engineers understand what is running right now, what is it connected to, and how can we verify those assertions. We purpose-built k8s-aibom to bridge that gap. It produces BOMs from live cluster observation rather than artifact scanning, emits standards-conformant CycloneDX 1.6 ML-BOMs that integrate with the broader OWASP
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Securing the AI supply chain on GKE: Introducing k8s-aibom for automated AI BOMs
  - Published: 2026-07-13T16:00:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/introducing-k8s-aibom-on-gke-for-automated-ai-bills-of-materials/
  - Summary: How should your security team manage shadow AI? Workloads deployed by developers without formal registration can often evade traditional security scanners, because organizations are reluctant to slow down development and compromise stability by demanding privileged Daemonsets, kernel-level access, and manual pod-spec edits. To break this deadlock, today we are open-sourcing k8s-aibom . This lightweight, unprivileged Kubernetes controller continuously monitors the cluster API and container environments to automatically detect running AI runtimes (like vLLM and Triton) and generate standard CycloneDX Machine Learning Bill of Materials (ML-BOMs). By providing automated, audit-grade visibility directly from runtime execution — regardless of whether the workload was formally registered — k8s-aibom can help teams safely move AI projects from pilot to production without developer integration friction. The architecture of zero friction k8s-aibom is designed from the ground up to respect both t

### Cluster 8c85eeaa7f — score 13

- Title: 7 Severe Vulnerabilities Patched in VMware Avi Load Balancer
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-14T13:55:41+00:00
- Link: https://www.securityweek.com/7-severe-vulnerabilities-patched-in-vmware-avi-load-balancer/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, phishing_social_eng, ransomware_extortion, supply_chain
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: Anthropic/Claude, Palo Alto Networks
- cve_ids: CVE-2026-47865, CVE-2026-47866, CVE-2026-47867, CVE-2026-47868, CVE-2026-47871
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, data_breach, active_exploitation
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: Anthropic/Claude, Palo Alto Networks
- cve_ids: CVE-2026-47865, CVE-2026-47866, CVE-2026-47867, CVE-2026-47868, CVE-2026-47871
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The flaws can be exploited for authentication bypass, remote code execution, privilege escalation, and directory traversal. The post 7 Severe Vulnerabilities Patched in VMware Avi Load Balancer appeared first on SecurityWeek .
```

#### Full body

```
Broadcom announced on Tuesday that new VMware Avi Load Balancer updates patch several critical and high-severity vulnerabilities. VMware Avi Load Balancer is a software-defined platform that provides load balancing, application security, and analytics for applications in hybrid and multi-cloud environments. According to Broadcom, two external researchers recently discovered that the VMware product is affected by seven potentially serious vulnerabilities. Filip Waeytens of NATO’s technology and cyber hub has been credited with discovering CVE-2026-47865, a critical authentication bypass issue that allows an attacker with network access to breach the Avi control plane. Waeytens also discovered three high-severity vulnerabilities that can allow an attacker to bypass authentication, execute arbitrary code, and escalate privileges to root. Network or local access is required for the exploitation of these flaws, which are tracked as CVE-2026-47866, CVE-2026-47867 and CVE-2026-47868. Lang Khuong Duy of Viettel IDC discovered two high-severity Avi Load Balancer bugs that can be exploited for directory traversal attacks (CVE-2026-47871) and privilege escalation (CVE-2026-47870). Advertisement. Scroll to continue reading. Both Lang and Waeytens have been credited by Broadcom for responsibly reporting CVE-2026-47869, a high-severity remote code execution vulnerability that can be exploited by an authenticated attacker with network access. Broadcom’s advisory does not mention in-the-wild exploitation for any of these vulnerabilities. However, it’s important that organizations install the latest updates, as it’s not uncommon for threat actors to exploit VMware product flaws in their attacks. Related : High-Severity Vulnerability Patched in VMware Fusion Related : VMware Aria Operations Vulnerability Could Allow Remote Code Execution Related : 2024 VMware Flaw Now in Attackers’ Crosshairs Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs Centers Laboratory Data Breach Affects 540,000 Individuals Third US Security Expert Sentenced to Prison for Helping Ransomware Gang China, India-Linked Hackers Both Targeted Same Pakistani Police Force ‘HalluSquatting’ Turns AI Hallucinations Into Botnet Delivery Mechanism Palo Alto Networks Patches 13 Vulnerabilities Microsoft Patches Defender ‘RoguePlanet’ Vulnerability AI Coding Tools Tricked Into Hacking Developer Machine via Decades-Old Technique Google Patches 382 Chrome Vulnerabilities Latest News Unpatched Claude for Chrome Flaw Lets Extensions Read Gmail, Calendar SAP Patches Critical Vulnerabilities in NetWeaver, Approuter, Commerce Cloud US, Allies Warn of Russian Cyberattacks Targeting Critical Infrastructure Routers Valarian Raises $50 Million for Sovereign Infrastructure Control Layer Multiple Jscrambler Packages Impacted by Supply Chain Attack Pentagon Suspends CMMC Phase 2 as It Rethinks Contractor Cybersecurity Rules Hacker Conversations: Jesse McGraw (GhostExodus), From Blackhat Hacker to Redemption Cybersecurity M&A Roundup: 37 Deals Announced in June 2026 Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Why Email Security Keeps Failing (And What Has to Change) July 8, 2026 Join this live webinar as we break down why email-layer defenses alone can't keep pace with the modern phishing ecosystem, how agentic AI is changing the capacity equation for security teams, and more. Register Virtual Event: 2026 Cloud S
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 7 Severe Vulnerabilities Patched in VMware Avi Load Balancer
  - Published: 2026-07-14T13:55:41+00:00
  - Link: https://www.securityweek.com/7-severe-vulnerabilities-patched-in-vmware-avi-load-balancer/
  - Summary: The flaws can be exploited for authentication bypass, remote code execution, privilege escalation, and directory traversal. The post 7 Severe Vulnerabilities Patched in VMware Avi Load Balancer appeared first on SecurityWeek .

### Cluster df4e34a64d — score 12

- Title: [Video] Where protection starts: Cisco Talos Intelligence Integrations
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-14T10:47:18+00:00
- Link: https://blog.talosintelligence.com/video-where-protection-starts-cisco-talos-intelligence-integrations/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Every day, defenders make high-consequence decisions with incomplete information. Learn how Cisco Talos Intelligence Integrations help reduce uncertainty by turning the latest threat intelligence into proactive protections across Cisco technologies.
```

#### Full body

```
[Video] Where protection starts: Cisco Talos Intelligence Integrations By Hazel Burton Tuesday, July 14, 2026 06:47 The Need to Know Cybersecurity has always involved elements of uncertainty. Every day, security teams are asked to make decisions with incomplete information, while attackers rely on defenders not being able to see the full picture. What defenders haven't always had to deal with is attackers using AI to rewrite malicious commands on the fly, malware that adapts its code upon every installation, and models that can search through decades of vulnerable code and exposed interfaces to uncover new opportunities for exploitation. While none of that changes the fundamental purpose of cybersecurity — to understand and act on what's happening in your environment — it does make that picture harder and harder to build. Is a newly registered domain part of an attack? Is that outbound connection normal? Is that user behavior unusual? Cisco Talos Intelligence Integrations helps answer those questions. Across Cisco’s security and enterprise technologies, Talos’ reputation and detection integrations continuously apply the latest threat intelligence to identify and block malicious activity. Our latest video introduces some of the Talosians behind the integrations and explains how they work. If you'd like to learn more about the technologies behind Talos Intelligence Integrations, you'll find a more detailed overview on the Cisco Security website. Share this post Related Content Agentic AI security: Why you need to know about autonomous agents now March 11, 2026 06:00 There are many benefits and security risks of deploying agentic AI within organizations. This blog emphasizes the importance of robust risk management and threat modeling to defend against both internal operational errors and potential malicious exploitation. How Cisco Talos powers the solutions protecting your organization January 7, 2026 06:00 What happens under the hood of Cisco's security portfolio? Our reputation and detection services apply Talos' real-time intelligence to detect and block threats. Here's how. Cybersecurity on a budget: Strategies for an economic downturn October 29, 2025 06:00 This blog offers practical strategies, creative defenses, and talent management advice to help your business stay secure when every dollar counts.
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: [Video] Where protection starts: Cisco Talos Intelligence Integrations
  - Published: 2026-07-14T10:47:18+00:00
  - Link: https://blog.talosintelligence.com/video-where-protection-starts-cisco-talos-intelligence-integrations/
  - Summary: Every day, defenders make high-consequence decisions with incomplete information. Learn how Cisco Talos Intelligence Integrations help reduce uncertainty by turning the latest threat intelligence into proactive protections across Cisco technologies.

### Cluster 86ef70edb1 — score 12

- Title: The serpent’s tongue: Luring the Python out of its den
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-14T10:00:06+00:00
- Link: https://blog.talosintelligence.com/the-serpents-tongue-luring-the-python-out-of-its-den/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: PyPI

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- actor_attribution: TeamPCP
- affected_products: GitHub, PyPI
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain
- actor_attribution: TeamPCP
- affected_products: GitHub, PyPI
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
This blog examines the full lifecycle of a Python package, from hosting on repositories such as PyPI or custom web servers, through source and wheel distribution formats, to the final installation into virtual or system-wide Python environments.
```

#### Full body

```
The serpent’s tongue: Luring the Python out of its den By Onur Mustafa Erdogan , Darin Smith Tuesday, July 14, 2026 06:00 Threat Spotlight Python's popularity, readable syntax, and extensive third-party library ecosystem make it an attractive target for threat actors seeking to compromise developer devices and infrastructure. Malicious packages and supply-chain attacks are increasingly common, exploiting the trust built into Python's packaging ecosystem to execute payloads at the moment of installation, without any direct interaction from the victim. This blog examines the full lifecycle of a Python package, from hosting on repositories such as PyPI or custom web servers, through source and wheel distribution formats, to the final installation into virtual or system-wide Python environments. Each technique is assessed for persistence, supported build methods, and distribution compatibility. We conclude with practical defensive measures, including dependency auditing tools, version pinning strategies, installation time controls, and general best practices for minimizing supply-chain risk. Due to the friendly nature of its syntax, extensive capabilities, and wide range of libraries, Python’s adoption by the developer community has been steadily increasing. Both the StackOverflow Developer Survey and the first party package repository PyPi’s download stats indicate rapidly growing usage, especially for data science, AI, and backend projects. Python has a very vibrant community of modules that can be easily installed using various package indexes. Unfortunately, this convenience comes with an additional burden. Malicious packages and supply chain infection are also increasingly common, as threat actors attempt to utilize these modules to infect as many victim devices as possible, abusing the very trust that the community is built upon. GitHub’s 2025 security data highlights the accelerating threat to the software supply chain, noting a 69% year-over-year increase in published malware advisories. Notably for Python developers, 17% of all reviewed advisories in the GitHub Advisory Database are now related to the Pip ecosystem, reflecting a significant targeting of Python-based environments. The threat actor group TeamPCP has also utilized software supply chain attacks, including misuse of Python modules, to compromise Microsoft’s GitHub subsidiary and carry out 20 “waves” of supply chain attacks according to Wired. Users often believe that for a malicious payload to be executed they need to directly interact with the infected piece of code (e.g., providing it with a sensitive input, executing its entry point, or importing it to a working project). In reality, Python packages can establish a foothold simply through installation. While analyzing these techniques in detail, we will take a deeper look at the background process of package installation for Python. This will help understand the threat landscape for Python packages, including legitimate components adversaries try to alter for their benefit. Journey of a Python package Figure 1. Layers of Python package installation. The process of moving a Python package from a remote repository to a local machine involves three distinct layers. While these layers are interconnected, they provide a useful abstraction for understanding the installation process: Hosting layer: Defines the location where the package is published Distribution layer: Specifies the file formats supported by the package Installation layer: Dictates the method of deployment for the package Hosting packages Python packages can be installed from various remote repositories. PyPI (Python Package Index): PyPI is the official repository for Python packages. The native package manager, pip, uses PyPI by default. Package details are accessible via a JSON API at “https://pypi.org/pypi/<package-name>/json”. During installation, the PyPI frontend redirects users to “files.pythonhosted.org”, where the actual files are stored.
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: The serpent’s tongue: Luring the Python out of its den
  - Published: 2026-07-14T10:00:06+00:00
  - Link: https://blog.talosintelligence.com/the-serpents-tongue-luring-the-python-out-of-its-den/
  - Summary: This blog examines the full lifecycle of a Python package, from hosting on repositories such as PyPI or custom web servers, through source and wheel distribution formats, to the final installation into virtual or system-wide Python environments.

### Cluster 1e00f96258 — score 12

- Title: Rapid7 and Mindshare Partner to Accelerate Cyber Resilience Across the Middle East
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-14T08:00:00+00:00
- Link: https://www.rapid7.com/blog/post/c-rapid7-mindware-middle-east-cybersecurity-partnership
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Gopan Sivasankaran is Regional Director, Middle East & Africa, at Rapid7 From AI adoption and cloud-first strategies to smart cities and critical infrastructure modernization, organizations across the United Arab Emirates are embracing innovation at an unprecedented rate. The country truly is setting the pace for digital transformation. Against this backdrop of rapid innovation, today's security teams are managing increasingly complex environments while defending against more sophisticated, AI-enabled threats. In this environment, business leaders still expect security to enable innovation, not slow it down. They're pushed to reduce risk, improve visibility across expanding attack surfaces, and respond faster than ever before, with limited resources now table stakes. This shift is changing what organizations expect from their cybersecurity partners, with customers no longer wanting disconnected tools or transactional relationships. They’re instead craving trusted advisors who can help
```

#### Full body

```
Back to Blog Culture Rapid7 and Mindshare Partner to Accelerate Cyber Resilience Across the Middle East Gopan Sivasankaran Jul 14, 2026 | Last updated on Jul 14, 2026 | 4 min read DISCOVER RAPID7 MDR Gopan Sivasankaran is Regional Director, Middle East & Africa, at Rapid7 From AI adoption and cloud-first strategies to smart cities and critical infrastructure modernization, organizations across the United Arab Emirates are embracing innovation at an unprecedented rate. The country truly is setting the pace for digital transformation. Against this backdrop of rapid innovation, today's security teams are managing increasingly complex environments while defending against more sophisticated, AI-enabled threats. In this environment, business leaders still expect security to enable innovation, not slow it down. They're pushed to reduce risk, improve visibility across expanding attack surfaces, and respond faster than ever before, with limited resources now table stakes. This shift is changing what organizations expect from their cybersecurity partners, with customers no longer wanting disconnected tools or transactional relationships. They’re instead craving trusted advisors who can help simplify security operations, strengthen cyber resilience, and deliver measurable outcomes. That's why Rapid7 is excited to announce a new strategic, Middle East-spanning distribution partnership with Mindware . A shared commitment to the region The Middle East continues to establish itself as one of the world's most ambitious digital economies. As organizations invest in cloud technologies, AI, and connected infrastructure, cybersecurity has become a critical foundation for sustainable growth. This is precisely why Rapid7 has continued to invest in the Middle East: We recognize the region's growing importance to the global cybersecurity landscape, and this new partnership with Mindware represents another important step in that journey. This collaboration is about more than expanding our channel presence, it's about investing in the partners helping organizations navigate an increasingly complex security landscape. Mindware has built a strong reputation as one of the Middle East's leading value-added distributors, combining deep regional expertise with technical enablement, professional services, and an extensive partner ecosystem. Together, we're creating a framework that helps partners grow their cybersecurity practices while delivering greater value to customers. Building stronger security operations Security teams today face a common challenge: too many tools, too many alerts, and not enough time. Organizations are increasingly looking for platforms that bring exposure management, threat detection, and response together to improve visibility and reduce operational complexity. Rapid7's AI-powered cybersecurity operations platform helps organizations unify security operations, reduce risk, and respond to threats with greater speed and confidence. Combined with Mindware's regional market knowledge, partner enablement capabilities, and technical expertise, this partnership will make it easier for organizations across the Middle East to access modern cybersecurity operations through trusted local partners. For those partners, this creates new opportunities to expand managed services, strengthen technical capabilities, and help customers modernize their security operations while supporting long-term business growth. Local expertise alongside global innovation The most successful cybersecurity partnerships combine global innovation with local knowledge. Organizations want world-class technology, but they also expect partners who understand their business environment, regulatory landscape, and operational priorities. By combining Rapid7's cybersecurity innovation with Mindware's established regional ecosystem, we're helping partners fortify and deliver solutions capable of addressing today's unprecedented security challenges and threats. Together, we'll
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 and Mindshare Partner to Accelerate Cyber Resilience Across the Middle East
  - Published: 2026-07-14T08:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/c-rapid7-mindware-middle-east-cybersecurity-partnership
  - Summary: Gopan Sivasankaran is Regional Director, Middle East & Africa, at Rapid7 From AI adoption and cloud-first strategies to smart cities and critical infrastructure modernization, organizations across the United Arab Emirates are embracing innovation at an unprecedented rate. The country truly is setting the pace for digital transformation. Against this backdrop of rapid innovation, today's security teams are managing increasingly complex environments while defending against more sophisticated, AI-enabled threats. In this environment, business leaders still expect security to enable innovation, not slow it down. They're pushed to reduce risk, improve visibility across expanding attack surfaces, and respond faster than ever before, with limited resources now table stakes. This shift is changing what organizations expect from their cybersecurity partners, with customers no longer wanting disconnected tools or transactional relationships. They’re instead craving trusted advisors who can help

### Cluster 4480c0b8b7 — score 12

- Title: GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-09T10:43:09+00:00
- Link: https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cybersecurity researchers have flagged a new ransomware family called GodDamn that employs the PoisonX kernel driver to neutralize security software as part of its defense evasion strategy. According to a new report published by the Threat Hunter Team from Symantec, the ransomware was first publicly spotted in the wild on May 21, 2026. It's assessed to be a rebrand of the Beast ransomware,
```

#### Full body

```
GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses  Ravie Lakshmanan  Jul 09, 2026 Malware / Endpoint Security Cybersecurity researchers have flagged a new ransomware family called GodDamn that employs the PoisonX kernel driver to neutralize security software as part of its defense evasion strategy. According to a new report published by the Threat Hunter Team from Symantec, the ransomware was first publicly spotted in the wild on May 21, 2026. It's assessed to be a rebrand of the Beast ransomware, which, in turn, was an enhanced version of Monster , a Delphi-based ransomware that surfaced in March 2022. Broadcom's cybersecurity arm is tracing the developer behind these ransomware families under the moniker Hyadina. In one attack orchestrated by the ransomware operation in early June 2026, the threat actors are said to have leveraged AnyDesk for remote access and used a NirSoft-based credential harvesting toolkit before deploying the ransomware. The exact initial access vector is unknown. The credential harvester is designed to extract sensitive data from common web browsers, Windows Credential Manager, cached domain credentials, VNC sessions, email clients, Wi-Fi profiles, and live network traffic. Also put to use in the attack is a user-mode defense evasion tool that's dressed as a Symantec product ("symantec.exe") and the PoisonX kernel driver ("g11.sys") to disable endpoint defenses in what's called a bring your own vulnerable driver (BYOVD) attack. "However, the PoisonX driver seems to be slightly more unusual, in that it appears to be a malicious driver that its developers succeeded in getting signed by Microsoft, and it is now being used by ransomware attackers," the Symantec Threat Hunter Team said in a report shared with The Hacker News. It's worth noting that PoisonX is one of the eight drivers adopted by the operators of The Gentlemen ransomware-as-a-service (RaaS) scheme in its custom GentleKiller tool that it hands out to affiliates for impairing system defenses prior to executing the encryptor. "Vulnerable drivers are the attacker's most reliable route in," Broadcom noted last month. "The attacker, having gained administrator privileges, can drop a flawed but validly signed driver onto the target machine. Because the driver is signed, Windows loads it automatically." "The most common action is to kill the processes belonging to antivirus (AV) or endpoint detection and response (EDR) products, stripping the machine of its defenses. Some variants are more subtle. Attackers may strip the security agent of the rights it needs to function correctly, leaving it running but unable to act. Others tamper directly with the kernel's internal records so that the security product no longer receives notifications about what is happening on the machine, effectively making it blind." The attack is also characterized by the use of PsExec to facilitate lateral movement, followed by setting up AnyDesk on each of those reachable hosts and registering it as an auto-start Windows service to survive reboots. On some machines, the entire AnyDesk setup is handled by a PowerShell script pre-staged on the system drive, suggesting the use of a reusable installer to streamline the process. "After completing the AnyDesk setup on each host, the attackers terminated the running AnyDesk process, waited briefly, then rebooted the machine," Symantec said. "By the end of June 2, this deployment sequence had been repeated across at least 10 hosts within the targeted organization." The cybersecurity company said GodDamn ransomware was first detected on June 3 on a separate network segment associated with a distinct organizational unit, causing the files to be renamed with the victim's name as the extension instead of the ".God8Damn" extension used in other attacks carried out by Hyadina. According to a report released by CYFIRMA, the ransom note dropped at the end of the intrusion urges victims to contact them either via email or t
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses
  - Published: 2026-07-09T10:43:09+00:00
  - Link: https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html
  - Summary: Cybersecurity researchers have flagged a new ransomware family called GodDamn that employs the PoisonX kernel driver to neutralize security software as part of its defense evasion strategy. According to a new report published by the Threat Hunter Team from Symantec, the ransomware was first publicly spotted in the wild on May 21, 2026. It's assessed to be a rebrand of the Beast ransomware,

### Cluster 174e783389 — score 11

- Title: AI Security Report 2026
- Source: Check Point Research (threat_research_primary)
- Published: 2026-07-14T00:51:31+00:00
- Link: https://research.checkpoint.com/2026/ai-security-report-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, apt_espionage, data_breach, phishing_social_eng, ransomware_extortion, supply_chain
- affected_industries: financial_services, government
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, data_breach, apt_espionage, ai_security
- affected_industries: financial_services, government
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For years, the cyber security industry tracked AI as a force multiplier: something that made existing attack techniques faster, cheaper, and more accessible. That framing was accurate. But the Annual AI Security Report 2026 from Check Point Research documents a transition that goes further. AI has crossed from assistant to operator. Where it once helped attackers prepare, it now runs the […] The post AI Security Report 2026 appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 17 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 463 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 416 How To Guides 13 Ransomware 5 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 AI Security Report 2026 July 14, 2026 https://research.checkpoint.com/2026/ai-security-report-2026/ For years, the cyber security industry tracked AI as a force multiplier: something that made existing attack techniques faster, cheaper, and more accessible. That framing was accurate. But the Annual AI Security Report 2026 from Check Point Research documents a transition that goes further. AI has crossed from assistant to operator. Where it once helped attackers prepare, it now runs the operation. Key observed findings AI has crossed from development aid to live attack operator. It now does the hands-on work inside live intrusions, from China-nexus espionage campaigns to a criminal breach of multiple Mexican government agencies and has spread from nation states to ordinary cyber criminals. AI now builds deployment-ready malware and attack suites. Its involvement is often invisible in the finished artifact: one developer used an AI environment to produce VoidLink, an 88,000-line command-and-control offensive framework, in under a week. Attackers prefer commercial models, and now abuse them by exploiting the agentic architecture, not just single prompts. Most actors favor jailbroken mainstream models over self-hosted ones, and the durable bypass is now a planted configuration file an agent loads and trusts across sessions. An AI-enabled criminal tooling market has matured. Phishing-as-a-service kits now embed a language model with the jailbreak built in, and conversational AI voice-agent services run vishing and one-time-passcode theft at scale. Virtual Identity is no longer a reliable trust anchor. Voice, face, documents, and live video are now cheap to forge convincingly and are widely used in attacks taking multi-channel social engineering to a new level of integration. AI itself is an expanding attack surface. Models cannot always separate data from instructions and content they process might influence the model’s behavior; the surrounding stack adds ordinary software vulnerabilities and supply-chain risk, all in a rapidly evolving ecosystem where security practices not always mature. Indirect prompt injection is on the rise. Detections of longer malicious payloads increased sharply, rising roughly fivefold between March and May 2026 and approaching 1% of observed prompts in May. Longer payloads are more typical of content-borne and agentic attack paths, this pattern suggests that indirect prompt injection is becoming more operationally relevant. Enterprise data leakage through GenAI is persistent and growing risk . High-risk prompts doubled from 2% to 4% during the last year, while organizations used an average of 10 AI applications each month, many without official approval. Data exposure risks are not evenly distributed across the verticals . Sector-level analysis reveals that AI-related data exposure risks are not evenly distributed across the verticals, and correlate both with AI usage patterns and security maturity. Business Services recorded the highest rate of high-risk GenAI prompts at 5.91%, meaning nearly one in every 17 AI interactions carried a significant risk of sensitive data exposure. To read the full findings, access the AI Security Report 2026 from Check Point Research here. GO UP BACK TO ALL POSTS POPULAR POSTS Artificial Intelligence ChatGPT Check Point Research Publications OPWNAI : Cybercriminals Starting to Use ChatGPT Check Point Research Publications Threat Research Hacking Fortnite Accounts Artificial Intelligence ChatGPT Check Point Research Publications OpwnAI: AI That Can Save the Day or HACK it Away BLOGS AND PUBLI
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: AI Security Report 2026
  - Published: 2026-07-14T00:51:31+00:00
  - Link: https://research.checkpoint.com/2026/ai-security-report-2026/
  - Summary: For years, the cyber security industry tracked AI as a force multiplier: something that made existing attack techniques faster, cheaper, and more accessible. That framing was accurate. But the Annual AI Security Report 2026 from Check Point Research documents a transition that goes further. AI has crossed from assistant to operator. Where it once helped attackers prepare, it now runs the […] The post AI Security Report 2026 appeared first on Check Point Research .

### Cluster 4dacf306cd — score 11

- Title: Meeting the ECB’s AI-Enabled Cybersecurity Mandate with NodeZero®
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-13T17:35:36+00:00
- Link: https://horizon3.ai/downloads/factsheets/meeting-the-ecbs-ai-enabled-cybersecurity-mandate-with-nodezero/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: financial_services
- affected_products: Kubernetes
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: financial_services
- affected_products: Kubernetes
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
The ECB now expects significant institutions to demonstrate AI-ready cyber resilience. Learn how NodeZero helps validate exploitable risk, verify remediation, and support an evidence-backed action plan.
```

#### Full body

```
Meeting the ECB’s AI-Enabled Cybersecurity Mandate with NodeZero® Horizon3.ai July 13, 2026 Factsheets AI-enabled attackers are dramatically reducing the time between vulnerability discovery and exploitation. For significant institutions supervised by the European Central Bank, that acceleration now requires a clear, evidence-backed response. The ECB has directed significant institutions to submit a board-level action plan addressing AI-accelerated cyber threats by October 31, 2026 . The plan must demonstrate how institutions are strengthening cyber resilience across six focus areas, from attack-surface visibility and vulnerability management to operational resilience and supply-chain assurance. The NodeZero® Proactive Security Platform maps directly to these priorities through continuous, production-safe autonomous pentesting that validates what attackers can actually exploit. Continuously discover and assess internet-facing, cloud, Kubernetes, internal, and third-party assets Prioritize remediation based on verified attack paths rather than vulnerability volume alone Verify patches and security improvements with rapid retesting and recurring autonomous pentests Strengthen monitoring and detection with NodeZero Tripwires™, Rapid Response, and Threat Actor Intelligence Validate identity security, network segmentation, endpoint controls, and defense-in-depth strategies Produce executive and regulatory-ready evidence supporting ECB, DORA, and NIS2 requirements Demonstrate business impact through full attack-chain emulation, High-Value Targeting, and Advanced Data Pilfering™ Measure security trends and remediation performance over time with NodeZero Insights™ NodeZero helps institutions move beyond point-in-time assessments and theoretical vulnerability findings. By continuously identifying exploitable exposure, validating remediation, and documenting measurable improvements, security teams can build an ECB action plan grounded in proof of real resilience. Download the Meeting the ECB’s AI-Enabled Cybersecurity Mandate with NodeZero Factsheet to see how Horizon3.ai maps NodeZero capabilities to each of the ECB’s six cybersecurity focus areas. Download as PDF How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Meeting the ECB’s AI-Enabled Cybersecurity Mandate with NodeZero®
  - Published: 2026-07-13T17:35:36+00:00
  - Link: https://horizon3.ai/downloads/factsheets/meeting-the-ecbs-ai-enabled-cybersecurity-mandate-with-nodezero/
  - Summary: The ECB now expects significant institutions to demonstrate AI-ready cyber resilience. Learn how NodeZero helps validate exploitable risk, verify remediation, and support an evidence-backed action plan.

### Cluster b47b034408 — score 11

- Title: Vulnerability in FIFA’s Network
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-07-14T11:06:51+00:00
- Link: https://www.schneier.com/blog/archives/2026/07/vulnerability-in-fifas-network.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Summary

```
FIFA’s network was vulnerable to anyone with even minimal access.
```

#### Full body

```
Vulnerability in FIFA’s Network FIFA’s network was vulnerable to anyone with even minimal access. Tags: hacking , sports , vulnerabilities Posted on July 14, 2026 at 7:06 AM • 3 Comments
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Vulnerability in FIFA’s Network
  - Published: 2026-07-14T11:06:51+00:00
  - Link: https://www.schneier.com/blog/archives/2026/07/vulnerability-in-fifas-network.html
  - Summary: FIFA’s network was vulnerable to anyone with even minimal access.

### Cluster bfabcf1e25 — score 10

- Title: No Manners Here: The Ruthless Rise of The Gentlemen Ransomware
- Source: Unit 42 (threat_research_primary)
- Published: 2026-07-10T22:00:39+00:00
- Link: https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: manufacturing_industrial, retail_ecommerce
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach, web_shell_backdoor
- affected_industries: manufacturing_industrial, retail_ecommerce
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 explores The Gentlemen ransomware operations, revealing the affiliate model driving its rapid growth. Learn more here. The post No Manners Here: The Ruthless Rise of The Gentlemen Ransomware appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights Hospitality Hacks and Retail Reality Checks Hospitality Hacks and Retail Reality Checks No Manners Here: The Ruthless Rise of The Gentlemen Ransomware 5 min read Related Products Unit 42 Incident Response By: Matt Brady Published: July 10, 2026 Categories: Hospitality Hacks and Retail Reality Checks Insights Tags: Howling Scorpius RaaS Spikey Scorpius Share Executive Summary The Gentlemen (aka Storm-2697 ) is a Ransomware-as-a-Service (RaaS) program active since at least July 2025. Public reporting indicates that the operators were likely active months earlier as an affiliate (known as ArmCorp) of Qilin RaaS, which Unit 42 tracks as Spikey Scorpius. Their ransomware variants are written in both C and Go programming languages , enabling the threat actors to spread their encryptors across different operating systems and virtual infrastructure. Figure 1 below illustrates the desktop wallpaper used by the ransomware after deployment. Figure 1. Image of The Gentlemen ransomware’s wallpaper. Source: Krebs on Security. Additional public reporting revealed that the operators (roughly 20 of them) likely morphed from a private entity into a RaaS model on or about September 2025. While traditional RaaS models typically offer affiliates a 70% to 80% cut of paid ransoms, The Gentlemen offer an unprecedented 90% payout. Background Unit 42 and other security researchers have observed The Gentlemen’s usage of a wide variety of initial access techniques similar to other RaaS operators since their inception, including the exploitation of vulnerabilities in edge devices (firewalls, VPNs), brute force attacks, obtaining leaked and/or stolen credentials and collaborating with initial access brokers (IABs). More recently, researchers have identified The Gentlemen’s usage of a custom Go-based backdoor , an EDR killer framework dubbed “ GentleKiller ” and the suspected usage of an unspecified zero-day vulnerability exploit to amplify their defense evasion capabilities. In May 2026, The Gentlemen announced a partnership with HasanBroker's BreachForums as a means to recruit affiliates, penetration testers and IABs. Figure 2 illustrates this announcement. Figure 2. Image of partnership announcement between BreachForums and The Gentlemen. Source: Gurucul. Additional information about The Gentlemen and their operational structure has emerged in recent months, following the leak of an internal database by an alleged insider in May 2026. Data Leak Site Insights One of the most alarming trends observed thus far in 2026 by Unit 42 and other security researchers is the sheer increase in volume of total victims claimed by The Gentlemen in comparison to 2025. Through July 7, one reputable source had counted a total of 580 victims claimed by The Gentlemen across 77 countries since their inception. Of those 580 victims, 103 operated within the manufacturing industry, a commonly targeted sector given the need for organizations to maintain operational uptime. Figure 3 below represents the total number of victims claimed by The Gentlemen in 2025 compared to both Qilin and Akira, tracked by Unit 42 as Howling Scorpius, which led all RaaS programs in victims claimed last year. Figure 3. Chart depicting total victims claimed by prominent RaaS programs in 2025. Source: Unit 42. In comparison to the above statistics, Figure 4 below represents the total number of victims claimed by The Gentlemen thus far in 2026 (through July 3) compared to both Qilin and Akira. Figure 4. Chart depicting total victims claimed by prominent RaaS programs in 2026. Source: Unit 42. When comparing the last six months of 2025 to the first six months of 2026, the number of victims claimed by The Gentlemen increased by slightly more than 6x. What makes this even more concerning is that these threat actors were only active for the last four months of 2025. Figure 5 below further illustrates the victims claimed by The Gentlemen per month since August 2025, one month p
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: No Manners Here: The Ruthless Rise of The Gentlemen Ransomware
  - Published: 2026-07-10T22:00:39+00:00
  - Link: https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/
  - Summary: Unit 42 explores The Gentlemen ransomware operations, revealing the affiliate model driving its rapid growth. Learn more here. The post No Manners Here: The Ruthless Rise of The Gentlemen Ransomware appeared first on Unit 42 .

### Cluster b835d1d4b1 — score 10

- Title: GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-07-09T15:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, web_shell_backdoor
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, web_shell_backdoor
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
GigaWiper is a destructive backdoor that combines multiple wiping and ransomware-like capabilities into a single operational platform. This blog analyzes how the malware incorporates code from several previously separate malware families and provides guidance to help defenders detect and defend against similar threats. The post GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Malware Threats intelligence Cyberattacker techniques, tools, and infrastructure Content types Research Products and services Microsoft Defender Microsoft Defender for Endpoint Topics Threat intelligence In October 2025, Microsoft Threat Intelligence identified destructive wiping activity and uncovered a sophisticated Go programming language (Golang)-based backdoor we now track as GigaWiper, a versatile implant that combines robust command-and-control (C2) capabilities with multiple destructive payloads, including disk wiping, fake ransomware, and system-level sabotage. GigaWiper is particularly notable for its makeup. It’s not a single, purpose-built tool, but an amalgamation of separate malware families that were folded into GigaWiper as on-demand backdoor commands, giving threat actors the flexibility to choose their mode of destruction: A standalone wiper that operates at the physical disk level, overwriting raw disk content and removing partition metadata. A destructive command that derives from Crucio ransomware and encrypts files with randomly generated keys that are never saved, making decryption impossible. A wiping command that reimplements the logic of FlockWiper, a C-based malware reimplemented in Golang with additional multi-pass secure wiping. The consolidation of multiple destructive capabilities into a modular backdoor reflects a notable shift in wiper malware, which are typically designed purely to destroy rather than to extort and carry real-world consequences. GigaWiper exemplifies threat actors investing in operational efficiency, merging standalone tools into unified platforms that reduce their deployment footprint while expanding their destructive capabilities. GigaWiper is tracked by Google Threat Intelligence Group (GTIG) and Binary Defense as BLUERABBIT. In this blog, we provide a code-level analysis of GigaWiper’s architecture. We’re sharing these findings, along with Microsoft Defender detections and mitigation recommendations, to enable organizations and the security community to investigate and defend against GigaWiper and similar destructive threats. A wiper inside a backdoor Beginning in October 2025, Microsoft Threat Intelligence started observing compromised environments being wiped with destructive tooling. Looking closely at the intrusions, we observed two types of GigaWiper samples: Standalone wiper binaries Larger binaries with robust backdoor functionality Both sample types are unstripped portable executable (PE) files written in Golang. Comparing the two samples showed that the standalone wiper’s code is fully embedded inside the backdoor as one of the commands. The standalone wiper binary The standalone wiper is an unstripped PE written in Golang. Instead of deleting individual files, it wipes at the physical disk level. It identifies physical drives, determines which drive contains the Windows installation, removes partition references from other drives, overwrites raw disk content, and then reboots the system. The wiper starts by enumerating physical disks through Windows Management Instrumentation (WMI) using the following query, giving it the device identifiers and disk metadata it needs before deciding how to handle each drive: Figure 1. Query for enumerating physical disks through WMI The malware then calls main.FindWindowsDrive to determine which physical disk contains the Windows installation (for example, \\.\PHYSICALDRIVE0 ). With that drive identified, it iterates the remaining disk list and calls main.unallocateDrive on each non-Windows drive to remove their partition references. This is achieved with DeviceIoControl and IOCTL_DISK_CREATE_DISK , which reinitializes the disk’s partitioning metadata and effectively wipes the existing partition table entries. If successful, the malware prints to the console “Partitions removed successfully.” Next, it proceeds to wipe each drive. It calls main.writeRandToDrive to overwrite each drive in chunks
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware
  - Published: 2026-07-09T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/
  - Summary: GigaWiper is a destructive backdoor that combines multiple wiping and ransomware-like capabilities into a single operational platform. This blog analyzes how the malware incorporates code from several previously separate malware families and provides guidance to help defenders detect and defend against similar threats. The post GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware
  - Published: 2026-07-09T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/
  - Summary: GigaWiper is a destructive backdoor that combines multiple wiping and ransomware-like capabilities into a single operational platform. This blog analyzes how the malware incorporates code from several previously separate malware families and provides guidance to help defenders detect and defend against similar threats. The post GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware appeared first on Microsoft Security Blog .

### Cluster 4a0789d0ad — score 10

- Title: One Target, Two Flags | Rival Espionage Actors Converge On Pakistani Law Enforcement
- Source: SentinelOne Labs (threat_research_primary)
- Published: 2026-07-09T12:55:00+00:00
- Link: https://www.sentinelone.com/labs/one-target-china-india-espionage-converge-on-pakistani-law-enforcement/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
China and India ran separate espionage operations against the same Pakistani police force, each drawn by different stakes in Pakistan's internal security.
```

#### Full body

```
Adversary One Target, Two Flags | Rival Espionage Actors Converge On Pakistani Law Enforcement Aleksandar Milenkoski & Julian-Ferdinand Vögele / July 9, 2026 Executive Summary SentinelLABS has been tracking sustained cyberespionage activity against several Pakistani law enforcement organizations, taking place from February 2024 to April 2026. All these actors converged on Balochistan Police over this period, bringing both a partner and an adversary of Pakistan to the same police force in a province shaped by a separatist insurgency and the regional tensions it has drawn in. At Balochistan Police, the compromised assets included servers hosting web applications that manage police and citizen data, such as criminal and biometric records. A suspected China-nexus actor planted implants in one of the web applications, which serves both police staff and citizens, weaponizing a tool of Pakistan’s police digitalization against its users. Pakistani law enforcement organizations attract cyber collection because they hold information on Pakistan’s internal security that regional powers have an incentive to pursue. For China, the likely primary concern is the safety of its nationals, the target of repeated deadly attacks Pakistan has failed to prevent, leading Beijing to assess that threat for itself rather than rely on its partner alone. For India, the strongest motive is probably its rivalry with Pakistan, with Balochistan Police offering insight into the security posture of a Pakistani province prominent in wider mutual accusations over cross-border support for militancy. Overview Suspected China- and India-nexus threat actors carried out intrusions into several Pakistani law enforcement organizations between 2024 and 2026. Our analysis of C2 netflow data revealed that suspected China- and India-nexus threat actors operating PlugX, ShadowPad, Cobalt Strike, and Remcos infrastructure have converged on this victim class. All of these threat actors were active against Balochistan Police, the principal police force serving the Pakistani province of the same name, at various points between 2024 and 2026. The affected assets spanned network appliances and servers hosting web applications that manage biometric records, hotel and tenant registrations linked to national identity records, criminal case files, and personnel records. A suspected China-nexus threat actor also compromised one of these web applications, deploying custom implants masquerading as a portal update. The application is used by police staff and by citizens interacting with law enforcement through it, and the compromise put both user groups within the threat actor’s reach. When multiple cyberespionage actors operate against law enforcement institutions of a single state, the convergence itself is a signal of target value. What draws them is a particular kind of institution: one that holds the government’s internal security picture, what it knows about the threats inside its borders, and how it acts against them. Each of the states suspected to be behind the activities covered in this post has its own stake in the threats monitored by Pakistani law enforcement. Strategic Motives | Distrust and Accusations The China-nexus activity is most likely motivated primarily by concern for the safety of Chinese nationals. Their presence across Pakistan is substantial, tied in large part to the China-Pakistan Economic Corridor (CPEC), Beijing’s flagship Belt and Road infrastructure program in the country. Chinese nationals have been the target of repeated deadly attacks, some of which were claimed by the Balochistan Liberation Army (BLA), a Baloch separatist group opposed to China’s presence in the Pakistani resource-rich southwest. Notable attacks include the October 2024 Karachi airport attack and the March 2024 suicide bombing in northwestern Pakistan. The attacks have fueled explicit Chinese dissatisfaction with Pakistani counter-militancy performance. In October 2024, China’s Ambass
```

#### Corroborating sources (1)

- **SentinelOne Labs** (threat_research_primary)
  - Title: One Target, Two Flags | Rival Espionage Actors Converge On Pakistani Law Enforcement
  - Published: 2026-07-09T12:55:00+00:00
  - Link: https://www.sentinelone.com/labs/one-target-china-india-espionage-converge-on-pakistani-law-enforcement/
  - Summary: China and India ran separate espionage operations against the same Pakistani police force, each drawn by different stakes in Pakistan's internal security.

### Cluster c8e0a6559d — score 10

- Title: 13th July – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-07-13T13:06:08+00:00
- Link: https://research.checkpoint.com/2026/13th-july-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain, web_shell_backdoor
- actor_attribution: ShinyHunters
- affected_industries: financial_services
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, npm
- cve_ids: CVE-2025-3248, CVE-2026-11405, CVE-2026-53359
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach, web_shell_backdoor
- actor_attribution: ShinyHunters
- affected_industries: financial_services
- affected_products: npm, Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2025-3248, CVE-2026-11405, CVE-2026-53359
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 13th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES U.S. auto insurer AssuranceAmerica has disclosed a data breach affecting approximately 7 million people. Attackers targeted an employee and used compromised credentials to access company systems, stealing names, contact information, driver’s license […] The post 13th July – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 13th July – Threat Intelligence Report July 13, 2026 https://research.checkpoint.com/2026/13th-july-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 13th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES U.S. auto insurer AssuranceAmerica has disclosed a data breach affecting approximately 7 million people. Attackers targeted an employee and used compromised credentials to access company systems, stealing names, contact information, driver’s license numbers, insurance policy and account data, vehicle information, and claims details. Latvia’s state-owned forestry company Latvijas Valsts Meži has suffered a ransomware attack that disrupted mapping, hunting, contractor, and customer systems. Attackers exploited a system that had remained unpatched for two years and leaked approximately 44GB of internal documents, credentials, cryptographic keys, source code, and email correspondence. Injective Labs, a developer of blockchain and cryptocurrency software, has experienced a supply chain compromise after attackers accessed its SDK project and published malicious npm packages. The affected releases exfiltrated cryptocurrency wallet private keys and seed phrases when developers used legitimate key-generation functions embedded in the compromised software. Moody Bible Institute, a U.S. faith-based educational institution, has disclosed a data breach affecting more than 2.3 million donors, students, alumni, and supporters. The ShinyHunters extortion group published allegedly stolen information, including names, dates of birth, residential addresses, email addresses, and phone numbers. AI THREATS Researchers profiled JadePuffer, an autonomous ransomware operation that used a large language model to conduct an intrusion without direct human control. The operation exploited CVE-2025-3248 in an exposed Langflow instance, accessed a production MySQL server, exfiltrated selected information, deleted the database, and issued an extortion demand. Researchers showed that malicious instructions hidden inside open-source project files could achieve remote code execution through Anthropic Claude Code and OpenAI Codex. When operating with automated permissions, the coding agents processed the instructions and executed attacker-controlled scripts, demonstrating a risk that may affect other autonomous development tools. Researchers disclosed Rogue Agent, a vulnerability in Google Dialogflow CX that allowed users with limited agent-editing permission to insert persistent malicious code. The injected code could capture and exfiltrate chatbot conversations. Google addressed the issue, and no known customer environments were compromised through the vulnerability. VULNERABILITIES AND PATCHES Multiple Tenda router models are affected by CVE-2026-11405, an undocumented authentication backdoor that provides administrative access through a hidden password. The flaw affects several FH1201, W15E, AC10, AC5, and AC6 firmware versions and allows attackers to bypass configured credentials and modify device and network settings. Linux maintainers have patched CVE-2026-53359, a critical vulnerability in the Kernel-based Virtual Machine hypervisor. A malicious guest virtual machine could corrupt host kernel memory and potentially escape into the host environment. The flaw affects Intel and AMD x86 systems and is particularly relevant to shared cloud infrastructure. U-Boot has addressed six vulnerabilities affecting signature verification of Flattened Image Tree files used during secure boot. Two flaws could enable arbitrary code execution while a device loads a supposedly verified image, and four could cause crashes. The affected bootloader is widely used in routers, cameras, and embedded controllers. Opera has addressed a critical vulnerability in the Opera GX browser that allowed malicious websites to install browser modificatio
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 13th July – Threat Intelligence Report
  - Published: 2026-07-13T13:06:08+00:00
  - Link: https://research.checkpoint.com/2026/13th-july-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 13th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES U.S. auto insurer AssuranceAmerica has disclosed a data breach affecting approximately 7 million people. Attackers targeted an employee and used compromised credentials to access company systems, stealing names, contact information, driver’s license […] The post 13th July – Threat Intelligence Report appeared first on Check Point Research .

### Cluster ca7dbcaa1e — score 10

- Title: Winning 54% of the time
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-09T18:00:06+00:00
- Link: https://blog.talosintelligence.com/winning-54-of-the-time/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
With Wimbledon's help, Hazel argues against the popular myth that "Attackers only need to be right once, but defenders need to be right 100% of the time."
```

#### Full body

```
Winning 54% of the time By Hazel Burton Thursday, July 9, 2026 14:00 Threat Source newsletter Welcome to this week’s Threat Source newsletter. There’s a fairly cliché phrase in cybersecurity that I’m sure our audience is familiar with: Attackers only need to be right once, whereas defenders need to be right 100% of the time. I guess it captures the asymmetry of this industry, but I’ve never been entirely comfortable with the phrase because it assumes cybersecurity is a game of perfection. One mistake and it's over. I’ve been watching a lot of Wimbledon this week, as I have done since childhood. In fact, I believe my first words were, “C’mon Tim!” (For our non-U.K. audience, I’m referring to tennis player Tim Henman, who made four Wimbledon semi-finals in the late 90s and early 2000s and has a hill in the Wimbledon grounds named after him). Of the “big three” (or the “big four” if you’re Scottish), my favourite was always Rafa Nadal, but I have to admit there’s no one who could deliver a one-handed backhand quite like Roger Federer. I bet that when he swats at a fly, the fly apologises and claps its wings. As I saw him sitting in the Royal Box entirely on his own this week, watching tennis out of pure love of the game while everyone else scoffed their strawberries and cream in the comfort of hospitality, I remembered the commencement speech he gave at Dartmouth a couple of years ago. He told the students that, across his entire career, he won 80% of his matches. But of all the total points he played, he won 54% of them. Tennis is a long game (no one can tell you that more than Novak Djokovic and Felix Auger Aliassime who just played the longest quarter final in Wimbledon’s history last night). And, mathematically in tennis, you can lose more points and overall games than your opponent and still win the match. Which point you win matters more than the total amount of points you win. If you go to the IBM SlamTracker right now, you’ll see all sorts of stats around when players choose to attack, how often they successfully convert those attacking positions into points, and how often they win points they looked destined to lose (the “steal” score). Tennis is hundreds of small decisions: When to attack, when to defend, when to be patient, when to let the point develop. Not all of those decisions pan out because, well, you’re playing against an opponent who’s also making decisions within the point… and not a brick wall. In the SOC, it’s also about making thousands of judgement calls, using whatever hand you’re dealt. And with more context, you’re able to know your environment better and make better decisions. You can test more assumptions and follow a hypothesis that might lead somewhere, or nowhere at all. Because that’s the job, and perfection is a myth. The one big thing Cisco Talos’ latest findings on the China-nexus threat actor UAT-7810 shows they are expanding their Operational Relay Box (ORB) networks with a fresh suite of custom malware. The group exploits known vulnerabilities in unpatched Ruckus and ASUS routers to deploy new tools, including the upgraded "LONGLEASH" and "DOGLEASH" backdoors. UAT-7810 builds these covert networks to provide infrastructure for other APT groups to launch attacks against high-value targets. Why do I care? ORB networks create a massive blind spot. They allow secondary threat actors to mask their origins and route malicious traffic through seemingly innocuous nodes. By compromising edge devices like wireless routers, UAT-7810 builds a highly evasive, decentralized proxy network that easily bypasses traditional perimeter defenses. The active development of sophisticated, multi-platform tools like LONGLEASH shows this group is heavily investing in making their infrastructure incredibly resilient and hard to dismantle. So now what? Because UAT-7810 relies on exploiting n-day vulnerabilities, defenders must ensure all edge devices, particularly Ruckus and ASUS routers, are fully patched. Monitor net
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Winning 54% of the time
  - Published: 2026-07-09T18:00:06+00:00
  - Link: https://blog.talosintelligence.com/winning-54-of-the-time/
  - Summary: With Wimbledon's help, Hazel argues against the popular myth that "Attackers only need to be right once, but defenders need to be right 100% of the time."

### Cluster 9814bfc594 — score 10

- Title: Operationalizing CTEM: A Practical Playbook for Continuous Threat Exposure Management
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-08T17:20:21+00:00
- Link: https://horizon3.ai/downloads/whitepapers/operationalizing-ctem-practical-playbook/
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
Learn how to operationalize Continuous Threat Exposure Management (CTEM) with a practical framework for validating exploitability, prioritizing real risk, verifying remediation, and continuously reducing your organization's attack surface.
```

#### Full body

```
Operationalizing CTEM: A Practical Playbook for Continuous Threat Exposure Management Horizon3.ai | July 8, 2026 | Whitepapers Download the Whitepaper Table of Contents How to Move from CTEM Theory to Measurable Risk Reduction The Gartner® Continuous Threat Exposure Management (CTEM) framework provides a clear vision for reducing cyber risk. Yet many organizations still struggle to turn that vision into a repeatable operating model that consistently reduces attacker opportunity. The challenge isn’t understanding CTEM. It’s operationalizing it. Most CTEM resources explain the framework. This playbook explains how to operationalize it. Drawing on real-world experience helping organizations continuously reduce cyber exposure, this practical playbook shows how to connect people, processes, and technology into a repeatable operating model that delivers measurable outcomes. Inside the Playbook Learn how to: Build a practical operating model for CTEM. Apply the CTEM operating loop across your entire attack surface. Prioritize remediation based on proven business impact. Measure whether exposure is decreasing over time. Assess your organization’s CTEM maturity and identify practical next steps. Who Should Read This This playbook is designed for: Chief Information Security Officers (CISOs) Security Architects Exposure Management and Vulnerability Management Leaders Security Operations and Engineering Teams Cloud, Infrastructure, and IT teams responsible for remediation Whether you’re launching a CTEM initiative or looking to mature an existing program, this playbook provides practical guidance for turning strategy into execution. Download the Playbook CTEM is more than a framework. It’s an operating model for continuously reducing attacker opportunity. Download Operationalizing CTEM: A Practical Playbook for Continuous Threat Exposure Management and learn how leading security organizations are moving beyond visibility to achieve measurable risk reduction. Not seeing the form? Open the standalone form . Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Operationalizing CTEM: A Practical Playbook for Continuous Threat Exposure Management
  - Published: 2026-07-08T17:20:21+00:00
  - Link: https://horizon3.ai/downloads/whitepapers/operationalizing-ctem-practical-playbook/
  - Summary: Learn how to operationalize Continuous Threat Exposure Management (CTEM) with a practical framework for validating exploitability, prioritizing real risk, verifying remediation, and continuously reducing your organization's attack surface.

### Cluster 8d0224c08d — score 10

- Title: June 2026 CVE Landscape
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-10T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/june-2026-cve-landscape
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Fortinet, Ivanti, Microsoft 365
- cve_ids: CVE-2020-17103, CVE-2022-0492, CVE-2025-55182, CVE-2026-25939, CVE-2026-35616
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Microsoft 365, Fortinet, Ivanti
- cve_ids: CVE-2026-35616, CVE-2026-25939, CVE-2020-17103, CVE-2022-0492, CVE-2025-55182
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
In June 2026, Insikt Group® identified 60 high-impact vulnerabilities that should be prioritized for remediation, 30 of which had a Very Critical Recorded Future Risk Score. This represents a 49% increase from last month.
```

#### Full body

```
June 2026 CVE Landscape In June 2026, Insikt Group® identified 60 high-impact vulnerabilities that should be prioritized for remediation , 30 of which had a Very Critical Recorded Future Risk Score. This represents a 49% increase from last month. 23 of the 60 vulnerabilities were included in the US Cybersecurity and Infrastructure Security Agency (CISA)’s Known Exploited Vulnerabilities (KEV) catalog, 34 were reported by vendors, and three were primarily surfaced through honeypot data. The 60 vulnerabilities in this report affected products from 36 vendors, with Microsoft accounting for approximately 18% of the vulnerabilities. The remaining exposure was concentrated across a range of enterprise software, security products, network infrastructure, developer tooling, and cloud platform vendors. Insikt Group created Nuclei templates to detect two of the vulnerabilities featured in this month’s report: CVE-2026-35616 affecting Fortinet FortiClient EMS and CVE-2026-25939 affecting Frangoteam FUXA. These are available to Recorded Future customers via the Recorded Future Intelligence Operations Platform. Quick reference: June 2026 Vulnerability Table All 57 vulnerabilities below were actively exploited in June 2026. This table does not include the three CVEs associated with honeypot activity, which are available to Recorded Future customers via the CVE Monthly report, in the platform. The table below also provides examples of public PoCs identified by Insikt Group. These PoCs were not tested for accuracy or efficacy. Vulnerability management teams should exercise caution and verify the validity of PoCs before testing. # Vulnerability Risk Score Vendor/Product KEV Malware Analysis RCE PoC 1 CVE-2020-17103 99 Microsoft Windows 10/11 and Windows Server 2019 ✓ ✓ Link 2 CVE-2022-0492 99 Linux Kernel ✓ ✓ Link 3 CVE-2025-55182 99 Meta React Server Components packages ✓ ✓ ✓ Link 4 CVE-2025-67038 99 Lantronix EDS5000 ✓ 5 CVE-2025-8088 99 WinRAR ✓ ✓ ✓ Link 6 CVE-2026-10520 99 Ivanti Sentry ✓ ✓ ✓ Link 7 CVE-2026-11645 99 Google Chromium V8 and Chrome ✓ ✓ ✓ Link 8 CVE-2026-12569 99 PTC Windchill, Windchill PDMLink, and FlexPLM ✓ ✓ 9 CVE-2026-20230 99 Cisco Unified Communications Manager ✓ ✓ Link 10 CVE-2026-20245 99 Cisco Catalyst SD-WAN Manager and Controller ✓ ✓ ✓ Link 11 CVE-2026-20253 99 Splunk Enterprise ✓ ✓ Link 12 CVE-2026-20262 99 Cisco Catalyst SD-WAN Manager ✓ ✓ Link 13 CVE-2026-21509 99 Microsoft 365 Apps for Enterprise and Office 2016 ✓ (available to Recorded Future Customers) ✓ Link 14 CVE-2026-28318 99 SolarWinds Serv-U ✓ ✓ Link 15 CVE-2026-33825 99 Microsoft Defender Antimalware Platform ✓ (available to Recorded Future Customers) ✓ Link 16 CVE-2026-34908 99 Ubiquiti UniFi OS, UniFi OS Server, UDM, and UDM-Pro ✓ ✓ Link 17 CVE-2026-34909 99 Ubiquiti UniFi OS, UniFi OS Server, Express 7, and UDM ✓ ✓ Link 18 CVE-2026-34910 99 Ubiquiti UniFi OS, UniFi OS Server, UDM, and UDM-Pro ✓ ✓ ✓ Link 19 CVE-2026-35273 99 Oracle PeopleSoft Enterprise PeopleTools ✓ ✓ Link 20 CVE-2026-39808 99 FortiSandbox PaaS ✓ (available to Recorded Future Customers) ✓ ✓ Link 21 CVE-2026-41089 99 Microsoft Windows Server 2012 ✓ (available to Recorded Future Customers) ✓ ✓ Link 22 CVE-2026-42271 99 BerriAI LiteLLM ✓ ✓ ✓ Link 23 CVE-2026-48558 99 SimpleHelp ✓ ✓ Link 24 CVE-2026-48907 99 Joomla Content Editor (JCE) extension for Joomla ✓ ✓ Link 25 CVE-2026-50751 99 Check Point Security Gateway, Quantum Security Gateway, and Spark Firewalls ✓ ✓ Link 26 CVE-2026-54420 99 LiteSpeed cPanel Plugin ✓ ✓ Link 27 CVE-2026-7473 99 Arista EOS ✓ ✓ Link 28 CVE-2021-26855 89 Microsoft Exchange Server 2016 and 2019 ✓ ✓ ✓ Link 29 CVE-2021-36260 89 Hikvision Firmware ✓ ✓ ✓ Link 30 CVE-2022-40684 89 Fortinet FortiOS, FortiProxy, and FortiSwitchManager ✓ ✓ Link 31 CVE-2023-20198 89 Cisco IOS XE Software ✓ ✓ Link 32 CVE-2024-21182 89 Oracle WebLogic Server ✓ ✓ Link 33 CVE-2024-21762 89 Fortinet FortiProxy and FortiOS ✓ ✓ ✓ Link 34 CVE-2025-48595 89 Android Framework ✓ ✓ ✓ Link 35 CVE-
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: June 2026 CVE Landscape
  - Published: 2026-07-10T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/june-2026-cve-landscape
  - Summary: In June 2026, Insikt Group® identified 60 high-impact vulnerabilities that should be prioritized for remediation, 30 of which had a Very Critical Recorded Future Risk Score. This represents a 49% increase from last month.

### Cluster caac5571c6 — score 10

- Title: The Threat Isn’t the Frontier Model
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-08T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/build-defensive-ai-agents
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: financial_services, government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: financial_services, government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The real AI threat isn't frontier models. It's cheap local models getting easier to run. Here's why CISOs should build defensive agents now, before attackers scale.
```

#### Full body

```
The Threat Isn’t the Frontier Model Quantization is the Clock Summer ‘26 vibes: international flights, Riyadh heat, and plentiful CISO conversations. Every conversation (regardless of geographic location or industry vertical) currently begins and ends with AI strategy. Let’s unpack the nuance. Every executive should be contemplating two questions at this moment : Are we building, testing, and scaling agents for the coming onslaught of AI-enabled adversary activity? Do we have the breadth of intelligence necessary to move at machine speed? Why Agents and Why Now? Timing is everything in life. So the question is: why invest in agents for defensive workflows now? Two premises need to be explained here. First, let’s focus on financially motivated adversaries that don’t receive a government paycheck (directly or indirectly). The state-sponsored adversaries have a different set of resources at their disposal. There are controlled cases where Frontier AI models enable autonomous adversarial activity in malware generation or holistic intrusion chains. Even the Five Eyes are officially warning about adversarial use of frontier models. Yet the onslaught of offensive agents hasn’t materialized yet. Like the Uruk-hai attacking Helm’s Deep in The Lord of the Rings , we expect the wave is coming, but the automated army hasn’t arrived. Why not? Frontier models may be susceptible to context poisoning over time, but it’s difficult to use them at any scale for automated offensive operations. The guardrails are sufficient for the moment. Adversaries are also caught between the OPSEC tension of using third-party APIs (which increases attribution risk) and investing the resources to build local open-source models. While much has been made of open-source model capabilities, the reality is that time, effort, and financial resources are required to use them effectively for offensive campaigns. To get nerdy for a second (because the details are important), a recent experiment with LibreChat and Dolphin-llama3:14b (uncensored LLM) on a $3K local server (containing a reasonable Nvidia GPU with 16GB of VRAM ) revealed that simple tasks like coding a new web shell are still out of reach. The level of effort and hardware required to build a local resource capable of orchestrating effective autonomous attack agents will only decrease over time. Quantization is the clock defenders should be watching. A reductive quantization explanation in this AI context is using less memory by rounding billions of numbers (weights) rather than maintaining precision, thereby shrinking an AI model’s size. Even though the model is slightly less capable, it’s still useful for most tasks. Quantization drives the hardware bar down, and the lower that bar falls, the sooner opportunistic actors can execute attacks at scale. The danger for defenders isn’t the headline-grabbing frontier models; it’s the ease with which adversaries can deploy effective local models on modest hardware. Based on the previous 18 months of advances , the next 6-12 months will likely yield similar advances in open-source model capabilities with minimal hardware investment. That’s when opportunistic actors start staging at scale. Which brings us back to protecting the proverbial house with defensive AI agents. Now is the time to build , not ponder. We don’t jump into self-driving cars until we have some confidence that the edge cases have been worked out. Similarly, the agentic workflow edge cases can’t be discovered and solved without iteration and testing. Smart CISOs are building an AI control plane (in collaboration with adjacent business units) to enable transparency into AI token consumption, project ROI visibility, and code security . Building and testing agents is part of a larger control-plane project and is particularly time-sensitive. Sandwiched between data availability and information security regulations, CISOs need to generate trust and confidence in agents. Humans may stay in the decision l
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: The Threat Isn’t the Frontier Model
  - Published: 2026-07-08T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/build-defensive-ai-agents
  - Summary: The real AI threat isn't frontier models. It's cheap local models getting easier to run. Here's why CISOs should build defensive agents now, before attackers scale.

### Cluster d77ec8e022 — score 10

- Title: Pandora’s Container Part 1: Unpacking Azure Container Security
- Source: TrustedSec (detection_response_operations)
- Published: 2026-07-14T04:00:00+00:00
- Link: https://trustedsec.com/blog/pandoras-container-part-1-unpacking-azure-container-security
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Azure

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_products: Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>Azure container services are everywhere. Their attack surface? Often overlooked. In Part 1 of this blog series, we walk through offensive techniques targeting registries, token keys, and container instances in Azure.</p>
```

#### Full body

```
Blog Pandora’s Container Part 1: Unpacking Azure Container Security July 14, 2026 Pandora’s Container Part 1: Unpacking Azure Container Security Written by Justin Mahon Cloud Penetration Testing Penetration Testing Table of contents Container Registries Identifying Roles and Registries Checking if Admin User is Enabled Enabling Admin User & Retrieving Passwords Pushing, Pulling and Tagging Dissecting Docker Images Modifying a Task With a Managed Identity Creating a Malicious YAML File Running the Task Token Keys and Scope Maps Creating a Token Change Image “How it’s Supposed to Work” My Method for Exfiltration Building a Custom Dockerfile Restart the Container With the Modified Image Exfil to Listener With ngrok Reverse Shell With ngrok Containers have become a foundational component of modern Azure environments. However, the attack surface introduced by services such as container registries, container apps, container instances, and container jobs is often underexplored. This blog series examines common attack techniques targeting Azure container services, including registries, secrets, jobs, keys, container instances, and container apps. During testing, I found that a standard reverse shell approach for container image replacement did not work reliably. I developed an alternative technique that embeds IMDS token theft and secret exfiltration directly into a Dockerfile's entrypoint, eliminating the need for a persistent reverse shell connection. Again, another shoutout to the AzRTE course by HackTricks for their amazing content. The course covered a lot of material and helped me understand Azure container security, identity abuse, and more. Pre-Requisites This blog assumes you at least have reader rights over the container assets. I have included a link to my GitHub repo with scripts you can run from CloudShell to enumerate these permissions. https://github.com/OffsecPierogi/Azure The following permissions are used for this demo: Microsoft.ContainerRegistry/registries/read Microsoft.ContainerRegistry/registries/write Microsoft.ContainerRegistry/registries/listCredentials/action Microsoft.ContainerRegistry/registries/pull/read Microsoft.ContainerRegistry/registries/push/write Microsoft.ContainerRegistry/registries/tasks/read Microsoft.ContainerRegistry/registries/tasks/write Microsoft.ContainerRegistry/registries/runs/write Microsoft.ContainerRegistry/registries/tokens/read Microsoft.ContainerRegistry/registries/tokens/write Microsoft.ContainerRegistry/registries/scopeMaps/write Microsoft.ContainerInstance/containerGroups/restart/action Microsoft.ContainerInstance/containerGroups/write Microsoft.ContainerRegistry/registries/generateCredentials/action The following built-in roles in Azure RBAC have all or some of these permissions assigned to them by default. Owner Contributor AcrPull AcrPush Figure 1 - Evil Kitty Container Registries Container Registries (ACR) store and distribute container images in Azure. They can be private (requiring auth) or public. As an attacker, a misconfigured registry lets you pull proprietary images, push backdoored containers or overwrite tags to hijack deployments. Enabling Admin Keys & Secret Hunting Container registries store and distribute container images. Admin keys allow you to log in as admin and conduct actions on behalf of one. Required Permissions: Microsoft.ContainerRegistry/registries/write Microsoft.ContainerRegistry/registries/listCredentials/action Microsoft.ContainerRegistry/registries/push/write Full access can also be achieved through having the Contributor role assigned over the resources (used here in the blog) or ACRPush/ACRPull permissions in the data plane. If an attacker gets access to a registry, these are some of the things they can do. Full Registry Access: Pull any image - steal your proprietary container images and code Push malicious images - inject backdoored containers into your registry Delete images/repositories - wipe out your entire registry List all repositories
```

#### Corroborating sources (2)

- **TrustedSec** (detection_response_operations)
  - Title: Pandora’s Container Part 1: Unpacking Azure Container Security
  - Published: 2026-07-14T04:00:00+00:00
  - Link: https://trustedsec.com/blog/pandoras-container-part-1-unpacking-azure-container-security
  - Summary: <p>Azure container services are everywhere. Their attack surface? Often overlooked. In Part 1 of this blog series, we walk through offensive techniques targeting registries, token keys, and container instances in Azure.</p>
- **Sysdig** (detection_response_operations)
  - Title: No single pane of glass: Anatomy of an Azure permission takeover
  - Published: 2026-07-14T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/no-single-pane-of-glass-anatomy-of-an-azure-permission-takeover
  - Summary: The Sysdig Threat Research Team recently observed an attacker walk one credential through five Azure permission systems. In this blog, we’ll explore how.

### Cluster f0cefbafc4 — score 10

- Title: Security Teams Are Ready To Become More Preemptive. What’s Holding Them Back?
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-08T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/dr-teams-ready-for-preemptive-security-mdr-survey
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
The shift toward preemptive security is underway, but most organizations are still navigating the realities of limited resources, fragmented tools, and emerging AI risk. At Rapid7’s recent Global Security Summit , we surveyed attendees to better understand where security leaders and practitioners stand today, what is shaping their priorities, and what they need to move forward. Their responses offer a candid view into the current state of security operations: ambitious, increasingly AI-aware, and ready for change, but still working through the practical challenges of getting there. For many teams, the direction is clear: security needs to become more proactive, more connected, and more resilient. Attackers are moving quickly, environments are expanding, and teams are under pressure to reduce risk before it turns into business disruption. But the survey results show that most organizations are still somewhere in the middle of that journey. Where organizations are today One of the cleare
```

#### Full body

```
Back to Blog Detection and Response Security Teams Are Ready To Become More Preemptive. What’s Holding Them Back? Emma Burdett Jul 2, 2026 | Last updated on Jul 2, 2026 | 5 min read DISCOVER RAPID7 MDR The shift toward preemptive security is underway, but most organizations are still navigating the realities of limited resources, fragmented tools, and emerging AI risk. At Rapid7’s recent Global Security Summit , we surveyed attendees to better understand where security leaders and practitioners stand today, what is shaping their priorities, and what they need to move forward. Their responses offer a candid view into the current state of security operations: ambitious, increasingly AI-aware, and ready for change, but still working through the practical challenges of getting there. For many teams, the direction is clear: security needs to become more proactive, more connected, and more resilient. Attackers are moving quickly, environments are expanding, and teams are under pressure to reduce risk before it turns into business disruption. But the survey results show that most organizations are still somewhere in the middle of that journey. Where organizations are today One of the clearest findings is that security operations are increasingly collaborative. According to the survey, 57% of respondents operate in a hybrid internal and MDR model. That reflects a reality many teams know well: internal expertise remains essential, but external support can help extend coverage, add specialist knowledge, and support faster response when internal resources are stretched. This hybrid model also speaks to the complexity security teams are managing. Modern environments span cloud, identity, endpoints, applications, third parties, and expanding attack surfaces. Keeping watch across all of it requires more than tooling alone. It requires the right mix of people, process, visibility, and support. At the same time, many organizations are still working to connect the dots across their security ecosystem. Two-thirds of respondents said their security capabilities are only partially integrated. For analysts, partial integration often means more manual work: switching between tools, stitching together context, and making decisions with an incomplete picture. When teams are jumping between systems, manually stitching together context, or working from incomplete data, it becomes harder to act at the speed modern threats demand. The survey also showed that only 10% of respondents describe their organization as “highly proactive” in predicting and preventing threats, which points to the reality of where many teams are today. The ambition is there, but becoming truly preemptive takes time, integration, and operational maturity. Most organizations are still balancing the day-to-day demands of reactive response with the longer-term work of building a more proactive security model. Confidence levels tell a similar story. 59% of respondents said they are only somewhat confident in their organization’s ability to prevent attacks before impact. Security teams understand what is at stake, but many still lack full confidence that they can consistently stop threats before they affect the business. AI is a priority, but trust matters AI was, of course, another major theme in the survey. Interest is high, especially when it comes to improving efficiency, accelerating triage, and helping teams manage growing volumes of data and alerts, but adoption is still developing. 52% of respondents said AI is in early-stage exploration within their security operations. AI has clear potential in the SOC and across security operations, from summarizing investigations to enriching alerts, supporting prioritization, and helping analysts move faster. But security teams have to be deliberate about how they apply it. In high-pressure environments where accuracy, context, and accountability matter, AI needs to earn trust. The survey results show that trust is still a key consideration
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Security Teams Are Ready To Become More Preemptive. What’s Holding Them Back?
  - Published: 2026-07-08T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/dr-teams-ready-for-preemptive-security-mdr-survey
  - Summary: The shift toward preemptive security is underway, but most organizations are still navigating the realities of limited resources, fragmented tools, and emerging AI risk. At Rapid7’s recent Global Security Summit , we surveyed attendees to better understand where security leaders and practitioners stand today, what is shaping their priorities, and what they need to move forward. Their responses offer a candid view into the current state of security operations: ambitious, increasingly AI-aware, and ready for change, but still working through the practical challenges of getting there. For many teams, the direction is clear: security needs to become more proactive, more connected, and more resilient. Attackers are moving quickly, environments are expanding, and teams are under pressure to reduce risk before it turns into business disruption. But the survey results show that most organizations are still somewhere in the middle of that journey. Where organizations are today One of the cleare

### Cluster 3dba733830 — score 10

- Title: NATO logistics, Ukrainian troops are top subjects of Russian camera hacks, advisory says
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-07-14T13:55:00+00:00
- Link: https://therecord.media/russian-intelligence-compromising-cameras-nato-ukraine-netherlands
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: manufacturing_industrial
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: manufacturing_industrial
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Dutch intelligence officials report that at least one Russian agency is compromising internet-connected cameras across Europe to spy on military logistics and Ukrainian personnel.
```

#### Full body

```
An M142 HIMARS driver in an artillery unit of 7th Rapid Response Corps of the Armed Forces of Ukraine. Image: General Staff of the Armed Forces of Ukraine via Facebook NATO logistics, Ukrainian troops are top subjects of Russian camera hacks, advisory says Russian state-backed hackers are systematically compromising internet-connected security cameras across Europe and Ukraine to gather intelligence on NATO military logistics and identify Ukrainian troops for battlefield targeting, Dutch intelligence agencies warned. In a public advisory , the Netherlands' General Intelligence and Security Service (AIVD) and Military Intelligence and Security Service (MIVD) said at least one Russian intelligence service has been carrying out cyber-espionage operations against internet-accessible cameras in the Netherlands, other NATO and EU member states and Ukraine. The goal is to collect intelligence of military value, including activity on military transport routes and weapons shipments destined for Ukraine. In Ukraine, the agencies said, hacked cameras have in some cases been used to locate Ukrainian military personnel, with the intelligence subsequently supporting attempts to kill soldiers and destroy equipment. The Dutch agencies said they also identified a small number of compromised cameras positioned along military logistics routes in the Netherlands as part of the broader operation. "As a key transit country, the Netherlands is an important espionage target due to its geographic location and its support for Ukraine," the July 10 advisory said. Moscow has repeatedly denied conducting malicious cyber operations against Western countries. Tracking NATO logistics According to the advisory, the attackers scan the internet for exposed devices, identify IP cameras based on manufacturer information and exploit weak security, including default passwords, outdated firmware and default configurations. The hackers then automatically analyze video feeds using image-recognition software to identify military vehicles and their cargo. Beyond the war, the Dutch intelligence services assess that Russia is also using the cameras to collect militarily relevant intelligence inside NATO and EU countries even when it is unrelated to Ukraine. While they said they have not observed Moscow using such information to support military attacks outside Ukraine, the campaign "demonstrates Russia's ability to collect operational intelligence that could be used in a future conflict." "The number of cyber espionage operations conducted by Russian state actors in support of military operations has steadily increased since the beginning of the war against Ukraine," the advisory said. The advisory urged organizations operating internet-connected cameras to strengthen their security by changing default credentials, keeping firmware up to date and reviewing device configurations. It also advised organizations to consider cameras’ country of origin. "Countries including China, Russia, and Iran actively conduct offensive cyber programs targeting Dutch interests," the advisory said. Nation-state News Technology Get more insights with the Recorded Future Intelligence Cloud. Learn more. No previous article No new articles Daryna Antoniuk is a reporter for Recorded Future News based in Ukraine. She writes about cybersecurity startups, cyberattacks in Eastern Europe and the state of the cyberwar between Ukraine and Russia. She previously was a tech reporter for Forbes Ukraine. Her work has also been published at Sifted, The Kyiv Independent and The Kyiv Post.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: NATO logistics, Ukrainian troops are top subjects of Russian camera hacks, advisory says
  - Published: 2026-07-14T13:55:00+00:00
  - Link: https://therecord.media/russian-intelligence-compromising-cameras-nato-ukraine-netherlands
  - Summary: Dutch intelligence officials report that at least one Russian agency is compromising internet-connected cameras across Europe to spy on military logistics and Ukrainian personnel.

### Cluster 85dc7136db — score 10

- Title: US sanctions VPN, malware providers for enabling ransomware attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-14T09:40:13+00:00
- Link: https://www.bleepingcomputer.com/news/security/us-sanctions-vpn-malware-providers-linked-to-ransomware-gangs/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, zero_day
- actor_attribution: BlackCat/ALPHV
- affected_industries: critical_infrastructure, financial_services, government
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day
- actor_attribution: BlackCat/ALPHV
- affected_industries: financial_services, government, critical_infrastructure
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Treasury Department's Office of Foreign Assets Control (OFAC) sanctioned two individuals and one entity for enabling ransomware attacks against U.S. organizations. [...]
```

#### Full body

```
US sanctions VPN, malware providers for enabling ransomware attacks By Sergiu Gatlan July 14, 2026 05:40 AM 0 The U.S. Treasury Department's Office of Foreign Assets Control (OFAC) sanctioned two individuals and one entity for enabling ransomware attacks against U.S. organizations. On Monday, OFAC designated First VPN Service (1VPNS) , a virtual private network provider that sold services to ransomware groups, and its administrator, Dmytro Rashevskyi. Since it surfaced in 2014, 1VPNS has advertised on cybercriminal forums that it keeps no logs of user activity or identities and would not cooperate with law enforcement. Rashevskyi allegedly used false identities (e.g., "Maksim Sorin" and "Roman Chabanenko") to acquire infrastructure from companies that would otherwise have refused service due to complaints of abuse. The sanctions come after European law enforcement took down 1VPNS's website and infrastructure in May with support from the FBI's Boston Field Office, as part of a joint action dubbed "Operation Saffron" led by French and Dutch authorities. The 1VPNS investigation began in December 2021, with law enforcement officers infiltrating the VPN's infrastructure and collecting its user database before it was dismantled. Throughout the joint operation, the authorities seized 33 servers linked to 1VPNs across 27 countries, arrested its administrator, and exposed thousands of users associated with ransomware, fraud, and other malicious activity worldwide. At the time, Europol also said that the VPN service's name had surfaced in nearly every major cybercrime investigation it supported. Victims of ransomware attacks involving 1VPNS' infrastructure included U.S. businesses, hospitals, financial services firms, and municipal governments. This week, the Treasury Department also sanctioned Belarusian national Yegeniy Vladimirovich Silayev, who sells cryptors (also known as crypters), which are tools that help ransomware and other malware evade detection by security software. Officials estimate that ransomware operations using 1VPNS and Silayev cryptors have caused billions of dollars in losses to businesses and critical infrastructure providers across the United States. "These actors supplied ransomware groups with tools to hide their identities, disguise malicious software, and evade detection — enabling attacks that have caused billions of dollars in losses to U.S. critical infrastructure providers," said State Department spokesperson Thomas Pigott. "By targeting not just ransomware operators but the service providers and tool suppliers who make their attacks possible, the United States and its partners are dismantling the broader networks that sustain cybercriminal activity worldwide." OFAC said the action was coordinated with the United Kingdom's Foreign, Commonwealth & Development Office. Under these sanctions, all property of the designated individuals and entities within U.S. jurisdiction is blocked, while U.S. persons and businesses are barred from transactions involving them. On Monday, the European Union and the United Kingdom also jointly sanctioned dozens of Russian individuals and entities , accusing Russia of coordinating a network of hacking groups linked to cyberattacks across Europe. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Police seize “First VPN” service used in ransomware, data theft attacks Former ransomware negotiator gets 4 years for BlackCat attacks CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day Check Point links VPN zero-day attacks to Qilin ransomware gang U.S. sanctions Nobitex crypto exchange used by Iranian ransomware actors
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: US sanctions VPN, malware providers for enabling ransomware attacks
  - Published: 2026-07-14T09:40:13+00:00
  - Link: https://www.bleepingcomputer.com/news/security/us-sanctions-vpn-malware-providers-linked-to-ransomware-gangs/
  - Summary: The U.S. Treasury Department's Office of Foreign Assets Control (OFAC) sanctioned two individuals and one entity for enabling ransomware attacks against U.S. organizations. [...]

### Cluster ef8f3ff932 — score 10

- Title: RabbitMQ Vulnerability Threatens Enterprise Systems
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-13T12:00:00+00:00
- Link: https://www.securityweek.com/rabbitmq-vulnerability-threatens-enterprise-systems/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng
- affected_products: Microsoft 365, Microsoft Entra, Okta
- cve_ids: CVE-2026-57219, CVE-2026-57221
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, active_exploitation
- affected_products: Okta, Microsoft 365, Microsoft Entra
- cve_ids: CVE-2026-57219, CVE-2026-57221
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Unauthenticated attackers could obtain the broker's confidential OAuth client secret, allowing them to take control of the broker. The post RabbitMQ Vulnerability Threatens Enterprise Systems appeared first on SecurityWeek .
```

#### Full body

```
A vulnerability in RabbitMQ could allow attackers to obtain the broker’s confidential OAuth secret, potentially posing a serious threat to enterprises, according to cybersecurity firm Miggo. RabbitMQ is a popular open source message broker that routes, buffers, and distributes messages, enabling asynchronous communication between applications. Tracked as CVE-2026-57219 (CVSS score of 8.7), the security defect impacts an open management endpoint that returns the OAuth secret to anyone, without authentication. The bug was discovered in an obsolete endpoint in RabbitMQ’s management web interface, and could be triggered in configurations where the administrator had set up the broker’s confidential password for identity provider authentication. “Anyone who could reach the management port could fetch it, then, where the OAuth grant makes the secret usable, impersonate the broker to the identity provider and obtain an administrator token,” Miggo says. In configurations that use the exposed secret, which is the standard when an OAuth 2/OIDC provider such as Auth0, Azure AD/Entra ID, Keycloak, or UAA is used, an attacker could obtain the administrator token to gain control of users, messages, queues, and broker settings, the company explains. Advertisement. Scroll to continue reading. If no client secret has been configured, the deployment is not affected, as there is no secret to leak. RabbitMQ instances with no management plugin are not affected either. “The risk is sharpest wherever the management port is reachable by an untrusted network: cloud or multi-tenant setups, or a management UI accidentally exposed to the internet,” Miggo says . CVE-2026-57219 was introduced in early 2024 in RabbitMQ version 3.13.0, and has been addressed in versions 4.3.0, 4.2.6, 4.1.11, 4.0.20, and 3.13.15. The updates also address CVE-2026-57221 (CVSS score of 5.3), a medium-severity missing authorization flaw that allows any authenticated user to enumerate queues and exchanges, and to read their statistics. According to Miggo, the vulnerability could be used to map an organization’s virtual host, infer business activity, and gather intelligence for future attacks. The flaw poses a risk to multi-tenant environments where the same virtual host is shared between multiple applications or teams. Organizations should update their RabbitMQ deployments immediately, block access to vulnerable instances if patching is not possible, ensure the management interface is not exposed to the internet, implement segmentation, and rotate the OAuth client secret, although there is no evidence of the flaw’s in-the-wild exploitation. “Neither of these RabbitMQ bugs is exotic. They sat in the codebase for over two years. They are precisely the kind of quiet, systemic inconsistency that hides in mature, widely deployed software: the kind a human reviewer reads past, and a single-pass tool fails to compare against everything around it,” Miggo notes. *Updated with the correct CVE identifier. Related: Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns Related: Attackers Could Exploit AI Vision Models Using Imperceptible Image Changes Related: SIM Swaps Expose a Critical Flaw in Identity Security Related: Predator Spyware Turns Failed Attacks Into Intelligence for Future Exploits Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Zimbra Patches Critical Code Execution Vulnerability Organizations Warned of Exploited Joomla Extension Vulnerabilities Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns Ghost Accounts Abuse GitHub API in Mass Recon Campaign Okta Warns of Vishing Attacks Targeting Microsoft 365 Customers GigaWiper Combines Multiple Malware for System-Level Sabotage Network of 200 GitHub Repositories Used for
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: RabbitMQ Vulnerability Threatens Enterprise Systems
  - Published: 2026-07-13T12:00:00+00:00
  - Link: https://www.securityweek.com/rabbitmq-vulnerability-threatens-enterprise-systems/
  - Summary: Unauthenticated attackers could obtain the broker's confidential OAuth client secret, allowing them to take control of the broker. The post RabbitMQ Vulnerability Threatens Enterprise Systems appeared first on SecurityWeek .

### Cluster ce7170bd38 — score 10

- Title: Felons, Fraudsters Flog Offensive Cybersecurity Startup
- Source: Krebs on Security (practitioner_analysis)
- Published: 2026-07-08T12:31:39+00:00
- Link: https://krebsonsecurity.com/2026/07/felons-fraudsters-flog-offensive-cybersecurity-startup/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: education, government, telecommunications
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: government, telecommunications, education
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
A cybersecurity startup dangling millions of dollars to acquire zero-day security vulnerabilities in popular software is run by a pair of far-right conspiracy theorists and convicted felons whose most recent ventures included fake intelligence companies and a now-defunct AI-based lobbying platform they operated under assumed names.
```

#### Full body

```
A cybersecurity startup dangling millions of dollars to acquire zero-day security vulnerabilities in popular software is run by a pair of far-right conspiracy theorists and convicted felons whose most recent ventures included fake intelligence companies and a now-defunct AI-based lobbying platform they operated under assumed names. The X/Twitter account IRIS C2 (@C2IRIS) has gained more than 4,000 followers since its creation in January 2025, posting frequently about security vulnerabilities, AI and software exploits. IRIS C2 says it is a company in McLean, Va. that sells offensive cybersecurity capabilities. The IRIS C2 website dangles the possibility of million-dollar payouts for exploits to attract talent. “Our business model is this,” reads a pinned post on top of the IRIS C2 account on X. “Attract the very best vulnerability researchers and exploit developers in the world to join our company. This mostly revolves around junior engineers with raw talent/extremely high IQ. We don’t care if they have a college degree/industry experience.” The website linked in that profile — irisc2[.]com — says the company is hiring for a number of open positions, and a recent post on its LinkedIn page enthuses about an overwhelming number of applications from potential employees. The website claims IRIS C2 is in the business of acquiring “zero-day exploits, individual primitives, partial chains, and full capabilities across all major platforms. Payouts range from $10,000 to $7 million depending on target, reliability, and operational value.” The government contracting portal g2exchange.com reports that irisc2[.]com is operated by a business based in Virginia called Calvexa Group LLC . The “contact” link on the website for Calvexa Group — calvexagroup[.]com — forwards visitors to irisc2[.]com. G2Exchange shows that while Calvexa Group LLC is registered as a federal contractor, it does not appear to be working on any direct government contracts. A search on the Arlington, Va. address listed in the incorporation records for Calvexa Group LLC finds the property is occupied by Jack Burkman , the 60-year-old founder and managing partner of the lobbying firm Burkman & Associates . When approached with questions about IRIS C2, Burkman referred further inquiries to his longtime associate, 28-year-old Jacob Wohl . Jack Burkman (left) and Jacob Wohl, at a press conference in August 2020. Image: Wikipedia. Burkman and Wohl have a storied history of creating fake intelligence companies and using them to spread false claims about and frame public figures, including fabricated sexual assault claims against then FBI director Robert Mueller , and Pete Buttigieg , then mayor of South Bend, Indiana and a Democratic candidate for the presidency. In 2019, Burkman and Wohl held press conferences falsely alleging extramarital affairs by Sen. Elizabeth Warren (D-Mass.) and then-2020 presidential candidate Kamala Harris . In the wake of the 2020 presidential election, Wohl and Burkman were prosecuted by multiple U.S. states for making thousands of robocalls to residents of battleground states and disseminating false claims about mail-in ballots. They were indicted in Cleveland on 15 felony counts of orchestrating a robocall scheme aimed at suppressing the black vote in Detroit, and were sentenced in late 2025 to probation after their appeals to dismiss the charges were rejected. In 2022, Wohl and Burkman both pleaded guilty to a single felony charge of telecommunications fraud in Ohio, and sentenced to a fine, probation, and community service. In March 2023, a judge in a New York civil case ruled that Wohl and Burkman had violated federal and state civil rights laws, and the two agreed to pay a $1 million settlement. In June 2023, the Federal Communications Commission (FCC) imposed a $5.1 million fine against Wohl and Burkman for their robocall campaigns, at the time the largest fine ever sought by the FCC under the Telephone Consumer Protection Act. Jacob “Jay” Wo
```

#### Corroborating sources (1)

- **Krebs on Security** (practitioner_analysis)
  - Title: Felons, Fraudsters Flog Offensive Cybersecurity Startup
  - Published: 2026-07-08T12:31:39+00:00
  - Link: https://krebsonsecurity.com/2026/07/felons-fraudsters-flog-offensive-cybersecurity-startup/
  - Summary: A cybersecurity startup dangling millions of dollars to acquire zero-day security vulnerabilities in popular software is run by a pair of far-right conspiracy theorists and convicted felons whose most recent ventures included fake intelligence companies and a now-defunct AI-based lobbying platform they operated under assumed names.

### Cluster 53ef47508e — score 10

- Title: RabbitMQ Flaws Could Leak OAuth Secrets and Expose Cross-Tenant Queue Metadata
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-14T13:48:07+00:00
- Link: https://thehackernews.com/2026/07/rabbitmq-flaws-could-leak-oauth-secrets.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass
- actor_attribution: Scattered Spider
- affected_industries: financial_services
- affected_products: GitHub
- cve_ids: CVE-2026-57219, CVE-2026-57221
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: mfa_bypass
- actor_attribution: Scattered Spider
- affected_industries: financial_services
- affected_products: GitHub
- cve_ids: CVE-2026-57219, CVE-2026-57221
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Cybersecurity researchers have disclosed details of two access control-related flaws impacting the RabbitMQ message broker service that could allow attackers to leak OAuth client secrets, expose enterprise messaging infrastructure to takeover risks, and bypass tenant boundaries. Miggo's security team, which discovered and reported the flaws, said one "leaks the broker's confidential OAuth
```

#### Full body

```
RabbitMQ Flaws Could Leak OAuth Secrets and Expose Cross-Tenant Queue Metadata  Ravie Lakshmanan  Jul 14, 2026 Vulnerability / Network Security Cybersecurity researchers have disclosed details of two access control-related flaws impacting the RabbitMQ message broker service that could allow attackers to leak OAuth client secrets, expose enterprise messaging infrastructure to takeover risks, and bypass tenant boundaries. Miggo's security team, which discovered and reported the flaws, said one "leaks the broker's confidential OAuth secret to an unauthenticated attacker in a single request, a direct path to full broker takeover in the configurations that use that secret." The second vulnerability allows any logged-in user to silently read other tenants' data. Both shortcomings are said to have been present in the codebase since early 2024, impacting RabbitMQ release lines from 3.13.0 and later. They have been addressed in versions 4.3.0, 4.2.6, 4.1.11, 4.0.20, and 3.13.15. There is no evidence of active exploitation of either of the vulnerabilities prior to the public disclosure. A brief description of the two flaws is below - CVE-2026-57219 (CVSS score: 8.7) - An obsolete HTTP API endpoint ("GET /api/auth") that reveals client secret on RabbitMQ installations that had OAuth 2 configured to use the management.oauth_client_secret configuration key, allowing an attacker to exchange it for an administrator token and obtain full control of every message, queue, user, and broker setting. CVE-2026-57221 (CVSS score: 5.3) - A missing authorization that allows any authenticated user who can connect to a virtual host to enumerate all queue and exchange names in that virtual host and read queue message counts and consumer counts, regardless of their actual permissions. "The endpoint's authorization check was hard-coded to always allow the request, unlike every other sensitive management endpoint," Miggo said about CVE-2026-57219. "The risk is sharpest wherever the management port is reachable by an untrusted network: cloud or multi-tenant setups, or a management UI accidentally exposed to the internet." Besides patching to the latest versions, it's advised to rotate the OAuth client secret if the management interface is reachable over the internet, limit access to port 15672 to prevent the management interface from being reachable over the network, separate tenants by virtual host, and implement firewall rules to block access to the vulnerable endpoint on unpatched instances. The disclosure comes as RabbitMQ maintainers addressed two critical-severity flaws that could result in a TLS client-authentication bypass (CVSS score: 9.1) and allow an attacker in an adversary-in-the-middle (AitM) position to forge JSON Web Key Set (JWKS) responses and cause the broker to accept arbitrary JWTs (CVSS score: 9.2). Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  API Security , Application Security , Cloud security , enterprise security , Identity and Access Management , network security , Open Source Security , Vulnerability ⚡ Top Stories This Week 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots RedWing MaaS Packages Android Bank Fraud as a Telegram Rental Service 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros GitHub Copilot Refuses Harmful Requests in Chat, Then Writes Them in Code New HalluSquatting Attack Could Trick AI Coding Assistants Into Installing Botnet Malware GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents Top AI Agents Built to Catch Malicious Code Can Be Tricked Into Run
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: RabbitMQ Flaws Could Leak OAuth Secrets and Expose Cross-Tenant Queue Metadata
  - Published: 2026-07-14T13:48:07+00:00
  - Link: https://thehackernews.com/2026/07/rabbitmq-flaws-could-leak-oauth-secrets.html
  - Summary: Cybersecurity researchers have disclosed details of two access control-related flaws impacting the RabbitMQ message broker service that could allow attackers to leak OAuth client secrets, expose enterprise messaging infrastructure to takeover risks, and bypass tenant boundaries. Miggo's security team, which discovered and reported the flaws, said one "leaks the broker's confidential OAuth

### Cluster aa4a893323 — score 10

- Title: Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-10T11:47:43+00:00
- Link: https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos
- affected_industries: legal_professional
- cve_ids: CVE-2026-42530
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos, active_exploitation
- affected_industries: legal_professional
- cve_ids: CVE-2026-42530
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A single wrong variable on one line in XQUIC, Alibaba's QUIC and HTTP/3 library, lets any remote client crash the server with a short burst of completely legal traffic. There is no patch. FoxIO researcher Sébastien Féry disclosed the flaw on July 8 and nicknamed it XRING. He says it needs no login and no malformed packets: about 260 bytes of ordinary QPACK traffic takes the server
```

#### Full body

```
Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers  Swati Khandelwal  Jul 10, 2026 Vulnerability / Server Security A single wrong variable on one line in XQUIC, Alibaba's QUIC and HTTP/3 library, lets any remote client crash the server with a short burst of completely legal traffic. There is no patch. FoxIO researcher Sébastien Féry disclosed the flaw on July 8 and nicknamed it XRING. He says it needs no login and no malformed packets: about 260 bytes of ordinary QPACK traffic takes the server process down. XQUIC is open-source, so the risk is not Alibaba's alone: any server that embeds it and serves HTTP/3 with the default QPACK settings is exposed. That includes Tengine, Alibaba's Nginx-based web server, which FoxIO says fronts the company's cloud and CDN on sites including Taobao and Alipay. Every release through v1.9.4, the latest, is affected. There is no fixed release and no CVE as of July 10. Until a fix ships, operators can set SETTINGS_QPACK_MAX_TABLE_CAPACITY to 0, which turns off QPACK's dynamic table, or drop HTTP/3 support entirely. The bug lives in how HTTP/3 compresses headers. To avoid sending the same header (say, user-agent) over and over, HTTP/3 uses QPACK. It keeps a shared table that the client directs the server to build up and resize through a dedicated control channel, the encoder stream. XQUIC stores that table's bytes in a ring buffer , a fixed block of memory where data wraps from the end back to the start once it fills. When the client asks to grow the table, XQUIC allocates a bigger buffer and copies the old data across. That copy has four cases, depending on whether the data wraps in the old buffer, the new one, both, or neither. In one of them, the code sizes the leftover tail data against the new, larger buffer's capacity instead of the old one's. It overcounts badly. Grow a 64-byte table with the write cursor near the end, and resize to 65, and XQUIC decides there are 70 tail bytes to move when there are really 6. That wrong number flows into a memory copy. The copy length comes from subtracting the overcount from a smaller value. Because that length is an unsigned size_t, it underflows and wraps to a near-maximum number, and the copy runs off the end of memory. In FoxIO's release build on Ubuntu 26.04, glibc's _FORTIFY_SOURCE=2 caught the bad length and killed the process. Without that check, the copy writes out of bounds, from the old buffer past the end of the new one. Féry showed a crash but did not test whether that corruption could be exploited further. None of the values in the attack breaks QPACK's rules. XQUIC advertises a 16 KiB dynamic-table limit by default; the payload asks for 64 bytes, then 65. The client only has to drive the table into the exact wrapped layout that hits the faulty branch. FoxIO says the mistake has been in XQUIC since its first public release in January 2022, and a proof of concept is public . XRING is the latest in a string of remote crashes in HTTP/2 and HTTP/3 stacks. Three weeks earlier, THN reported a use-after-free in NGINX's HTTP/3 module (CVE-2026-42530) that a remote, unauthenticated client could reach through the same QPACK encoder stream XRING abuses, a different bug class on the same attack surface. In June, Calif's HTTP/2 Bomb caused remote denial of service against Nginx, Apache, IIS, and Envoy by abusing HPACK, HTTP/2's header compression, and the predecessor to QPACK. In February, HAProxy patched two QUIC crashes , one an integer underflow during token validation, the same type of bug behind XRING, though it needed a malformed packet where XRING needs none. That difference is the point: legal input, one arithmetic slip, a dead server. FoxIO demonstrated a crash, not code execution, and reported no exploitation in the wild. It says it emailed Alibaba on April 7 through the project's security policy, which promises a reply within three working days, then followed up four more times through May 9 without an answer before going
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers
  - Published: 2026-07-10T11:47:43+00:00
  - Link: https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html
  - Summary: A single wrong variable on one line in XQUIC, Alibaba's QUIC and HTTP/3 library, lets any remote client crash the server with a short burst of completely legal traffic. There is no patch. FoxIO researcher Sébastien Féry disclosed the flaw on July 8 and nicknamed it XRING. He says it needs no login and no malformed packets: about 260 bytes of ordinary QPACK traffic takes the server

### Cluster 480db84242 — score 10

- Title: Lidl Notifies Customers of Third-Party Data Breach
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-14T09:43:00+00:00
- Link: https://www.infosecurity-magazine.com/news/lidl-notifies-customers-of/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng
- affected_industries: education, financial_services, retail_ecommerce
- affected_products: Google Cloud
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, data_breach
- affected_industries: financial_services, education, retail_ecommerce
- affected_products: Google Cloud
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Supermarket giant Lidl has revealed details of a supplier breach impacting customer data
```

#### Full body

```
Infosecurity Magazine Home » News » Lidl Notifies Customers of Third-Party Data Breach Lidl Notifies Customers of Third-Party Data Breach News 14 July 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster Lidl has warned customers in several European countries to beware of phishing messages after revealing that their personal information may have been stolen from a third-party IT provider. The supermarket giant, owned by German retail conglomerate Schwarz Group, said customers in Germany, Belgium and the Netherlands were impacted by the incident. In a note to Belgian and Dutch customers , Lidl said it found out about the incident last week. “Despite high IT security standards, unidentified individuals were briefly able to access a separately stored file containing customer data and steal some of it. The online shop system itself was not affected,” it explained. Read more on retail breaches: Food Retailer Ahold Delhaize Discloses Data Breach Impacting 2.2 Million Lidl said that customers of its online store were affected, with stolen data including full names, phone numbers, email addresses, dates of birth and customer numbers. “At this time, we can rule out the possibility that passwords, billing and delivery addresses, bank details, or other payment information are affected,” it continued. “Your customer account has not been compromised. Although we currently have no concrete evidence of data misuse, we are warning you, as a precaution, against possible phishing or identity theft attempts.” Lidl said its IT service provider “reacted immediately” to restore the security of the impacted systems and engage forensics experts to investigate further. The relevant authorities have also been contacted. Customer Vigilance is Required Lidl warned of potential follow-on phishing attacks from fraudsters who may now be in possession of the stolen data. “Always verify the sender's authenticity,” it said. “If you notice anything unusual, do not disclose any data or click on any unknown links.” Boris Cipot, principal security engineer at app security firm Black Duck, praised Lidl for its speedy response and transparency. “That kind of candor presents the appropriate posture under GDPR,” he continued. “The real test now is follow-through: how quickly they complete the forensic investigation, how clearly they communicate updates as the scope becomes known, and how rigorously they reassess the security requirements they place on their service providers going forward.” Cipot urged customers to change their passwords out of caution, enable multi-factor authentication wherever it's offered, and be on high alert. “Attackers will absolutely weaponize this stolen data to craft convincing scams in the weeks and months ahead,” he added. “Monitor your bank and card statements closely, and consider a credit freeze if you're in a jurisdiction where that's available." You may also like West Ham Supporters’ Personal Details Leaked on Club Website News 9 March 2021 Improving Cybersecurity within Higher Education Opinion 2 February 2021 Cybersecurity Incidents Account for a Third of ICO Reports in 2020 News 4 September 2020 Augusta Health Center Reveals Historic Breach News 21 August 2018 Crafting Scams with AI: a Devastating New Vector Blog 29 March 2023 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Russian State Hackers Target Vulnerable Routers Worldwide, Joint Advisory Warns News 13 July 2026 1 Progress Software Warns of "External Security Threat" to ShareFile News 13 July 2026 2 75% CISOs Fear Executives Don’t Understand Cybersecurity Risks Employees Face News 9 July 2026 3 NCSC Touts National Scale, AI-Powered “Cyber Shield” for Defense News 8 July 2026 4 Novel OAuth Client ID Spoofing Technique Targets Cloud Environments News 13 July 2026 5 Suspected Chinese Threat Group Targets Universities via Vulnerable Roundcube Servers News 7 July 2026 6 Google Cloud's New CISO Ch
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Lidl Notifies Customers of Third-Party Data Breach
  - Published: 2026-07-14T09:43:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/lidl-notifies-customers-of/
  - Summary: Supermarket giant Lidl has revealed details of a supplier breach impacting customer data

### Cluster 98dd5f4721 — score 10

- Title: Conditional Access Misconfigurations Exposed 55 Orgs with MFA On
- Source: Huntress (detection_response_operations)
- Published: 2026-07-09T14:00:00+00:00
- Link: https://www.huntress.com/blog/conditional-access-misconfigurations
- Fetch status: ok
- Member count: 6
- Corroborating source count: 3
- Strong signals: Microsoft 365

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass, phishing_social_eng, ransomware_extortion
- affected_products: Azure, Microsoft 365, Okta
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Microsoft 365, Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Two Microsoft 365 attacks got through Conditional Access policies that seemed fully configured. Learn what went wrong and how Huntress Managed ISPM catches these gaps first.
```

#### Full body

```
Home Blog Railway. LSHIY. Different Auth Flows, but the Same Lesson We Keep Skipping Published: July 9, 2026 Railway. LSHIY. Different Auth Flows, but the Same Lesson We Keep Skipping By: Aimee Simpson Scott Riley Rich Mozeleski Summarize with AI Summarize ChatGPT Claude Perplexity Google AI In March 2026, our SOC caught a surge of anomalous Microsoft 365 logins across dozens of organizations simultaneously. The source: a handful of IP addresses belonging to Railway.com , a developer PaaS platform most security teams have never had reason to think about. The technique: device code phishing, where attackers generate a legitimate Microsoft authentication code and trick users into entering it, handing over a valid OAuth token that lasts up to 90 days. No password stolen. No malware installed. MFA completed by the victim, so the attacker gets full access. By the time we published our Railway investigation , 344 organizations had been hit across the US, Canada, Australia, New Zealand, and Germany. Three months later, our SOC spotted a different kind of surge: 81 million login attempts from an IPv6 range controlled by a company called LSHIY LLC, resulting in 78 compromised accounts across 64 organizations. The technique this time was ROPC, or Resource Owner Password Credentials, a deprecated OAuth flow that takes a username and password directly at the /token endpoint and mints a fresh user token without ever triggering an MFA prompt in most cases. Different attacks. Different infrastructure. But both campaigns got through because of the same category of misconfiguration: auth flows that most Microsoft 365 environments have never explicitly blocked, and Conditional Access policies that looked correct but weren't. Railway: A token harvesting factory with clean IP addresses Device code phishing is effective because it doesn't try to beat MFA. It sidesteps it. Microsoft's OAuth device code flow was designed for input-constrained devices like smart TVs and printers that can't do an interactive login. Attackers weaponize it by generating device codes themselves, embedding them in phishing lures, and collecting the resulting OAuth tokens when victims authenticate. The victim may complete MFA. It doesn't matter. The token is already gone. Figure 1: Device code phishing used as a tactic What made Railway dangerous wasn't the technique, which Huntress has tracked for a while . It was the infrastructure. Railway is a legitimate developer PaaS platform. Its IP ranges are clean. Microsoft Identity Protection has no reason to score a login from Railway as risky. Attackers effectively got a cloud-hosted token harvesting engine with trusted IP reputation built in, and just three Railway IP addresses accounted for roughly 84% of all attack traffic. A small number of deployed applications were doing a lot of damage. The lures were built to scale, too. Construction RFP themes dominated, which tracks given that the construction industry runs on third-party document requests. Some phishing chains ran through triple-wrapped URLs using Cisco, Trend Micro, and Microsoft's own SafeLinks in sequence. The email arrived with a trusted vendor domain in the link, and the filtering stack passed it. That campaign was later attributed to EvilTokens, a Phishing-as-a-Service platform Huntress tracked in partnership with Flare.io . EvilTokens is a commercial product, with a storefront, AI-assisted lure generation, 24/7 support team, and customer reviews included. Device code phishing at this scale is now something you can subscribe to. Read our full EvilTokens breakdown → LSHIY: MFA was on. It just wasn't working right. The LSHIY campaign arrived differently. No phishing lures or social engineering. Just attackers replaying validated credentials via the ROPC flow against Azure CLI at a massive scale. ROPC is a legacy OAuth method that bypasses the authorization endpoint and goes straight to the /token endpoint with a username and password. Because it never hits the a
```

#### Corroborating sources (3)

- **Huntress** (detection_response_operations)
  - Title: Conditional Access Misconfigurations Exposed 55 Orgs with MFA On
  - Published: 2026-07-09T14:00:00+00:00
  - Link: https://www.huntress.com/blog/conditional-access-misconfigurations
  - Summary: Two Microsoft 365 attacks got through Conditional Access policies that seemed fully configured. Learn what went wrong and how Huntress Managed ISPM catches these gaps first.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New phishing kits target Microsoft 365 accounts, evade MFA
  - Published: 2026-07-14T12:49:00+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/
  - Summary: Two new phishing kits, Jalisco and OmegaLord, have been discovered in attacks targeting Microsoft 365 accounts, using techniques that defeat multi-factor authentication (MFA). [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Forg365 PhaaS Targets Microsoft 365 with Device Code and AitM Session Theft
  - Published: 2026-07-13T13:03:33+00:00
  - Link: https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html
  - Summary: A new phishing-as-a-service (PhaaS) operation called Forg365 is using a combination of device code phishing, adversary-in-the-middle (AitM) tactics, antibot evasion, artificial intelligence (AI)-assisted lure creation, and post-compromise mailbox operations targeting Microsoft 365 accounts. Distributed via Telegram and costing $400 a month (or $3,800 per year), attack chains leverage phishing

### Cluster 685ef943c5 — score 9

- Title: UK and Allies urge critical sectors to improve defences against Russian intelligence targeting
- Source: NCSC UK (government_authoritative)
- Published: 2026-07-13T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/news/uk-and-allies-urge-critical-sectors-to-improve-defences-against-russian-intelligence-targeting
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
New advisory highlights Russian state cyber actors’ global exploitation of poorly configured routers
```

#### Full body

```
News Download & print article PDF Download & print article PDF UK and Allies urge critical sectors to improve defences against Russian intelligence targeting New advisory highlights Russian state cyber actors’ global exploitation of poorly configured routers The UK and international allies strongly urge action to better defend against the threat from Russian state intelligence actors Advice follows the opportunistic exploitation of inadequately configured routers and network devices by Centre 16 of Russia’s Federal Security Service (FSB) Warning comes as the UK sanctions Russian state and criminal networks for cyber and hybrid operations and calls out the FSB for a reckless attack on Poland’s energy grid. Organisations in critical infrastructure sectors are being supported to better understand and defend against malicious activity, as the UK and international partners today call out techniques used by Russian Intelligence Services Alongside 18 agencies from 12 countries, the National Cyber Security Centre (NCSC) – a part of GCHQ – has published a new advisory highlighting the methods of Federal Security Service (FSB) Centre 16 cyber actors, who are exploiting vulnerable routers and opportunistically targeting networks belonging to critical national infrastructure (CNI) globally. Sectors most at risk from this global targeting, including communications, defence, energy, financial services, government and healthcare, are subsequently being urged to take action. This includes recommendations to use SNMPv3 and disable legacy SNMP versions, implement strong and unique passwords for network devices, and restrict access to management protocols through appropriate access controls. Centre 16, also known as Berserk Bear, Energetic Bear, Crouching Yeti, Dragonfly, Ghost Blizzard and Static Tundra, has been seen hunting for vulnerable routers by scanning the internet for devices that still use default or weak Simple Network Management Protocol (SNMP) passwords and community strings. Whilst the actor primarily uses SNMP scans to locate and compromise vulnerable routers, they have also exploited well-known vulnerabilities relating to Cisco devices, Cisco’s Smart Install (SMI) feature and web-portal flaws to gain control of network devices. Jonathon Ellison, NCSC Director of National Resilience said: The NCSC, alongside our international partners, have repeatedly exposed the advanced tools and coordinated campaigns of Russian cyber actors who persistently seek to exploit any vulnerability they encounter. “Today’s joint advisory provides decisive, actionable directions from the global security community that network defenders should implement to protect against Russian Intelligence operations and secure the UK’s critical infrastructure. “I’d strongly encourage all organisations, especially those entrusted with UK critical networks, to adopt these recommended measures immediately, thereby reducing the risk of compromise. Organisations are also encouraged to obtain Cyber Essentials certification, the government-backed scheme for all organisations to show they meet the recognised UK minimum standard for cyber security, and make use of the updated Cyber Assessment Framework , enabling them to assess their security maturity, address vulnerabilities and build their resilience against increasing threats. The advisory has been published on the same day as the UK government has sanctioned 24 individuals and entities behind destructive cyber and hybrid operations including cyber criminals involved in proxy networks linked to the Russian Intelligence Services. The UK together with EU member states has also today formally attributed the December 2025 attack on Poland’s energy grid to Russia’s FSB Centre 16 – an attack that if it had been successful could have caused 500,000 civilians to lose electricity. The NCSC has co-sealed this new advisory alongside agencies from Australia, Canada, Czech Republic, Denmark, Estonia, Finland, France, Italy, New Zealan
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: UK and Allies urge critical sectors to improve defences against Russian intelligence targeting
  - Published: 2026-07-13T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/news/uk-and-allies-urge-critical-sectors-to-improve-defences-against-russian-intelligence-targeting
  - Summary: New advisory highlights Russian state cyber actors’ global exploitation of poorly configured routers

### Cluster acd4fc9884 — score 9

- Title: Wireshark 4.6.7 Released, (Sat, Jul 11th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-11T09:07:06+00:00
- Link: https://isc.sans.edu/diary/rss/33146
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
Wireshark release 4.6.7 fixes 12 vulnerabilities and 16 bugs.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Wireshark 4.6.7 Released, (Sat, Jul 11th)
  - Published: 2026-07-11T09:07:06+00:00
  - Link: https://isc.sans.edu/diary/rss/33146
  - Summary: Wireshark release 4.6.7 fixes 12 vulnerabilities and 16 bugs.

### Cluster 2ab29cfc79 — score 9

- Title: My Stack Simulator, (Wed, Jul 8th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-10T15:52:27+00:00
- Link: https://isc.sans.edu/diary/rss/33138
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
The stack is a memory region where a program stores temporary data -&#;x26;#;xc2;&#;x26;#;xa0;like local variables and return addresses. Think of the stack as a pile of plates in your kitchen: you can only add a new plate to the top, and you can only take one away from the top too. Programs use this same "last in, first out" principle to keep track of what they&#;x26;#;39;re doing. Every time a function is called, the program pushes a new plate onto the stack containing things like local variables and the address to return to once the function finishes. When the function is done, that plate is popped off the top, and execution resumes exactly where it left off. This simple mechanism is what allows programs to call functions&#;x26;#;xc2;&#;x26;#;xa0;within functions, and always find their way back -&#;x26;#;xc2;&#;x26;#;xa0;but it&#;x26;#;39;s also precisely why a stack that grows too large, or gets overwritten with unexpected data, becomes a favorite target for attackers looking to hij
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: My Stack Simulator, (Wed, Jul 8th)
  - Published: 2026-07-10T15:52:27+00:00
  - Link: https://isc.sans.edu/diary/rss/33138
  - Summary: The stack is a memory region where a program stores temporary data -&#;x26;#;xc2;&#;x26;#;xa0;like local variables and return addresses. Think of the stack as a pile of plates in your kitchen: you can only add a new plate to the top, and you can only take one away from the top too. Programs use this same "last in, first out" principle to keep track of what they&#;x26;#;39;re doing. Every time a function is called, the program pushes a new plate onto the stack containing things like local variables and the address to return to once the function finishes. When the function is done, that plate is popped off the top, and execution resumes exactly where it left off. This simple mechanism is what allows programs to call functions&#;x26;#;xc2;&#;x26;#;xa0;within functions, and always find their way back -&#;x26;#;xc2;&#;x26;#;xa0;but it&#;x26;#;39;s also precisely why a stack that grows too large, or gets overwritten with unexpected data, becomes a favorite target for attackers looking to hij

### Cluster 5985a2820d — score 9

- Title: "Comment stuffing" in an HTML phishing attachment as a mechanism for evading AI-based detection?, (Fri, Jul 10th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-10T09:09:29+00:00
- Link: https://isc.sans.edu/diary/rss/33144
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
Anyone who deals with phishing messages caught by basic security filters knows that most phishing samples tend to blend into one another, since only a small set of techniques and approaches keeps reappearing in them. That is precisely why it is worth pausing on the occasional message that does something a little out of the ordinary.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: "Comment stuffing" in an HTML phishing attachment as a mechanism for evading AI-based detection?, (Fri, Jul 10th)
  - Published: 2026-07-10T09:09:29+00:00
  - Link: https://isc.sans.edu/diary/rss/33144
  - Summary: Anyone who deals with phishing messages caught by basic security filters knows that most phishing samples tend to blend into one another, since only a small set of techniques and approaches keeps reappearing in them. That is precisely why it is worth pausing on the occasional message that does something a little out of the ordinary.

### Cluster a7c8d38805 — score 9

- Title: Authenticate legitimate AI agent traffic with AWS WAF Bot Control
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-07-14T15:18:42+00:00
- Link: https://aws.amazon.com/blogs/security/authenticate-legitimate-ai-agent-traffic-with-aws-waf-bot-control/
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
As AI agents and automated tools increasingly access web applications, distinguishing legitimate bot traffic from malicious attempts has become a critical security challenge. Traditional approaches such as IP-based filtering and reverse DNS lookups fail in multi-tenant systems (such as Amazon Bedrock AgentCore) where thousands of distinct workloads share the same IP space. Attackers can easily […]
```

#### Full body

```
AWS Security Blog Authenticate legitimate AI agent traffic with AWS WAF Bot Control As AI agents and automated tools increasingly access web applications, distinguishing legitimate bot traffic from malicious attempts has become a critical security challenge. Traditional approaches such as IP-based filtering and reverse DNS lookups fail in multi-tenant systems (such as Amazon Bedrock AgentCore ) where thousands of distinct workloads share the same IP space. Attackers can easily spoof user agents, and manual allowlists don’t scale with growing demand. Web Bot Authentication (WBA), available in AWS WAF Bot Control since November 2025, solves this challenge by implementing cryptographic signatures that provide tamper-proof verification of bot identities. WBA uses asymmetric cryptography to verify that a request comes from an authorized automated agent, relying on two active Internet Engineering Task Force (IETF) drafts: a directory draft for sharing public keys, and a protocol draft defining how keys attach crawler identity to HTTP requests. With WBA, you can confidently identify trusted automated access while maintaining granular control through WAF labels, creating a more secure and manageable ecosystem for both bot operators and website owners. AWS WAF Bot Control respects WBA verification status by default, automatically allowing verified AI agent traffic. This post provides a deeper technical guide to implementing WBA with AWS WAF. You learn how WBA works, explore the new labels and capabilities it introduces, and walk through a step-by-step implementation—including signing code—to authenticate bot traffic using cryptographic signatures. How Web Bot Authentication works with AWS WAF WBA uses asymmetric cryptography to verify bot identities through HTTP message signatures. The process works as follows: Bot registration – Bot operators publish their public keys in a signature directory. AWS WAF regularly polls these directories and maintains a valid key registry. Request signing – Each bot operator’s request is signed using their private key following the IETF standard HTTP Message Signatures (RFC 9421) . Verification – AWS WAF verifies signatures against known public keys associated with the bot operator and appends labels related to verification status. A typical WBA-signed request includes headers like the following: Signature-Agent: https://signature-agent.test Signature-Input: sig2=("@authority" "signature-agent") ;created=1735689600 ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U" ;alg="ed25519" ;expires=1735693200 ;nonce="e8N7S2MFd/qrd6T2R3tdfA..." ;tag="web-bot-auth" Signature: sig2=:jdq0SqOwHdyHr9+r5jw3iYZH6aNGKijYp/EstF4RQ.. The following sequence diagram shows how AWS WAF verifies bot signatures and applies labels for allow or block decisions. Figure 1 – AWS WAF Web Bot Authentication verification flow The workflow shown in figure 1 includes the following steps: A bot sends a signed request to Amazon CloudFront and is inspected by AWS WAF Bot Control AWS WAF Bot Control retrieves the bot operator’s public key from the signature directory AWS WAF Bot Control verifies the ed25519 signature AWS WAF Bot Control appends a verification label ( verified , invalid , expired , or unknown_bot ) AWS WAF Bot Control evaluates rules using the label to allow or block the request. New capabilities added to AWS WAF With the addition of WBA, the following capabilities were added to AWS WAF. Cryptographic bot verification When a bot sends a request, it includes HTTP message signatures that AWS WAF validates at the edge using the AWS WAF Bot Control rule group (version 4.0 and later). This validation process adds minimal latency to requests while providing cryptographic certainty about the bot’s identity. HTTP Message Signatures is an open IETF standard ( RFC 9421 ) that defines a mechanism for signing and verifying HTTP messages using asymmetric keys—in practice, this means a bot cryptographically signs specific headers and metada
```

#### Corroborating sources (1)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Authenticate legitimate AI agent traffic with AWS WAF Bot Control
  - Published: 2026-07-14T15:18:42+00:00
  - Link: https://aws.amazon.com/blogs/security/authenticate-legitimate-ai-agent-traffic-with-aws-waf-bot-control/
  - Summary: As AI agents and automated tools increasingly access web applications, distinguishing legitimate bot traffic from malicious attempts has become a critical security challenge. Traditional approaches such as IP-based filtering and reverse DNS lookups fail in multi-tenant systems (such as Amazon Bedrock AgentCore) where thousands of distinct workloads share the same IP space. Attackers can easily […]

### Cluster 88d76f4fd8 — score 9

- Title: Lessons Learned from CISA’s Recent GitHub Leak
- Source: Krebs on Security (practitioner_analysis)
- Published: 2026-07-13T15:03:28+00:00
- Link: https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, vulnerability_disclosure
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: data_breach, vulnerability_disclosure
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
The Cybersecurity and Infrastructure Security Agency (CISA) has issued a postmortem on a data leak in which a contractor published dozens of internal CISA credentials -- including AWS Govcloud keys -- in a public GitHub repository for almost six months before being notified by KrebsOnSecurity. Experts say the gaps identified in the agency's initial response provide important lessons that all security teams should absorb.
```

#### Full body

```
The Cybersecurity and Infrastructure Security Agency (CISA) has issued a postmortem on a recent data leak in which a contractor published dozens of internal CISA credentials — including AWS Govcloud keys — in a public GitHub repository for almost six months before being notified by KrebsOnSecurity. Experts say the gaps identified in the agency’s initial response provide important lessons that all security teams should absorb. On May 15, 2026, the security firm GitGuardian asked for help in notifying CISA about the existence of a public GitHub repository called “Private CISA” that included 844 MB of sensitive CISA-related data. One of the exposed files, titled “importantAWStokens,” included the administrative credentials to three Amazon AWS GovCloud servers. Another file — “AWS-Workspace-Firefox-Passwords.csv” — listed plaintext usernames and passwords for dozens of internal CISA systems. CISA quickly acknowledged our initial alert, but took more than 48 hours to invalidate the AWS keys and many other important secrets leaked in the GitHub repo. In its report on the data leak , CISA said the complexities of the agency’s systems and interconnections with federal and industry partners caused its key rotation to take longer than anticipated. “Drawing on this experience, CISA encourages others to maintain mature and well-tested key management capabilities,” the report notes. CISA also admitted it can do better when it comes to responding to security incident notifications from external parties. The postmortem stresses that clear and distinct reporting channels are essential to ensure that incidents affecting the organization itself are handled differently from those involving its products or customers. “In CISA’s case, these channels were not well defined, leading the security researcher to try multiple avenues – including emailing the contractor, submitting through CISA’s vulnerability disclosure platform (which is intended for vulnerabilities impacting the broader cybersecurity community), and ultimately involving a reporter,” reads the analysis written by Preston Werntz and Brad Libbey , the acting chief information officer and acting chief information security officer at CISA, respectively. CISA said it is refining its reporting channels to make them easier and faster for researchers. “Additionally, while many researchers rely on the security.txt file, organizations can ensure clarity by publishing reporting instructions in multiple prominent locations,” the CISA authors wrote. Guillaume Valadon , the GitGuardian researcher who first contacted KrebsOnSecurity about the exposed CISA credentials, said CISA ignored nine automated alerts about the exposed credentials prior to our notification on May 15. Valadon’s company constantly scans public code repositories at GitHub and elsewhere for exposed secrets, automatically alerting the offending accounts of any apparent sensitive data exposures. “Letting nine notification emails go unanswered is how a one-day incident becomes a six-month exposure,” Valadon wrote in an analysis of CISA’s report. “Make it trivial to report a leak about you, not just about your products. The person reporting a leak to you is not the threat. Publish a security.txt , but do not stop there. Put reporting instructions in several prominent places, and make sure a report about your own infrastructure does not land in a product-bug queue.” The report’s authors also emphasized the importance of continuously scanning public code repositories like GitHub for exposed secrets, and said CISA has since rotated all secrets and created an action plan to improve management of developer secrets and to better monitor for them going forward. The report notes that while CISA had developed a playbook for responding to cybersecurity incidents, that playbook somehow didn’t include what to do in situations involving GitHub or other cloud services. Valadon said the report validates the need to scan continuously — not just quarter
```

#### Corroborating sources (1)

- **Krebs on Security** (practitioner_analysis)
  - Title: Lessons Learned from CISA’s Recent GitHub Leak
  - Published: 2026-07-13T15:03:28+00:00
  - Link: https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/
  - Summary: The Cybersecurity and Infrastructure Security Agency (CISA) has issued a postmortem on a data leak in which a contractor published dozens of internal CISA credentials -- including AWS Govcloud keys -- in a public GitHub repository for almost six months before being notified by KrebsOnSecurity. Experts say the gaps identified in the agency's initial response provide important lessons that all security teams should absorb.

### Cluster 09c50b3a4b — score 9

- Title: Friday Squid Blogging: “Squidbleed” Vulnerability
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-07-10T21:07:13+00:00
- Link: https://www.schneier.com/blog/archives/2026/07/friday-squid-blogging-squidbleed-vulnerability.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- affected_industries: government
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Summary

```
In a rare combined cybersecurity/squid post, a twenty-nine-year-old squid proxy bug can leak HTTP requests. As usual, you can also use this squid post to talk about the security stories in the news that I haven’t covered. Blog moderation policy.
```

#### Full body

```
ResearcherZero • July 11, 2026 4:18 AM De-funding public access to government records and data. The National Archives and Records Administration is closing its facilities in Chicago, San Francisco and Seattle. Staffing was additionally cut by more than 500 employees. Funding has been in dire circumstances for many years and the administration is operating with a reduced budget which hampers its ability to properly function. In 2024 a major report on the status of the National Archives and Records Administration (NARA) warned that NARA desperately needed more funding in order to continue reviewing and declassifying records and meet Freedom of Information requests requirements. As electronic records add to the problem of paper records already overwhelming NARA, the lack of staffing, adequate equipment and infrastructure has seen the backlog of requests grow to the point where requests can become stuck in queues of 12 years waiting to be processed. Many records will now no longer make it to the National Archives. That information will become lost to the public. As public record and federal data access is reduced for the public, or becomes entirely unavailable in many cases, the Trump administration is amassing data for itself to further its own interests and amass even greater power and control. Abrupt changes to how data is collected, have altered once comparable datasets and how information can be looked at over time, obscuring and distorting how different data might be interpreted. Now the Trump administration has begun closing public records facilities containing historical records, gutting the National Archives and deleting or removing access to federal data. Important programs that collect vital statistics and information are being de-funded, wound back and ended. Scientific and historical data is also being deleted as the Trump administration makes changes to government websites, agencies and services. The cost of filing FOI requests has become out of reach for many. Only corporations and the wealthy will have the time and money necessary. Changes to how census and economic data are collected will add to the reduction in data that is available to the public. Removal of scientific and historical information worsens the problem. As facts disappear and access to historical records is lost, fabrications, misinformation and lies will fill the gaps. Without the paper trail , the public cannot hold government accountable for its actions. This is taking place while the government consolidates data for itself and massively expands its surveillance capabilities. When history is rewritten, citizens can find themselves written out of it without warning, as the foundations of society shift around them and administrative errors alter reality. For members of the public to protect their rights, property and liberty, access to public records can be essential. Without that access, the ability of citizens to defend themselves from unreasonable or criminal actions becomes far more difficult. Proving ownership, ancestry or events – perhaps might become impossible – if the documentation required to ascertain certain facts, is no longer accessible or perhaps no longer exists.
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Friday Squid Blogging: “Squidbleed” Vulnerability
  - Published: 2026-07-10T21:07:13+00:00
  - Link: https://www.schneier.com/blog/archives/2026/07/friday-squid-blogging-squidbleed-vulnerability.html
  - Summary: In a rare combined cybersecurity/squid post, a twenty-nine-year-old squid proxy bug can leak HTTP requests. As usual, you can also use this squid post to talk about the security stories in the news that I haven’t covered. Blog moderation policy.

### Cluster aad8380132 — score 9

- Title: Smashing Security podcast #475: JadePuffer – the AI that ran a ransomware attack all by itself
- Source: Graham Cluley (practitioner_analysis)
- Published: 2026-07-08T23:19:18+00:00
- Link: https://grahamcluley.com/smashing-security-podcast-475/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
A 15-year-old boy asked a chatbot for help - and cancelled nearly 47,000 anime streaming subscriptions in under four hours. Meanwhile, researchers have documented the first fully autonomous, agentic AI-driven ransomware attack, "JadePuffer". What does this tell us about the future of cybersecurity? Also, Apple's "Hide My Email" feature turns out to hide rather less than it promises - despite Apple knowing it has a problem for over a year. All this and more in this episode of the "Smashing Security" podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Zoë Rose.
```

#### Full body

```
Graham Cluley @ 12:19 am, July 9, 2026 @grahamcluley.com / grahamcluley A 15-year-old boy asked a chatbot for help – and cancelled nearly 47,000 anime streaming subscriptions in under four hours. Meanwhile, researchers have documented the first fully autonomous, agentic AI-driven ransomware attack, “JadePuffer”. What does this tell us about the future of cybersecurity? Also, Apple’s “Hide My Email” feature turns out to hide rather less than it promises – despite Apple knowing it has a problem for over a year. All this and more in this episode of the “Smashing Security” podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Zoë Rose. Smashing Security #475 JadePuffer - the AI that ran a ransomware attack all by itself ↺ 15 ↻ 30 0:00 Learn more 0:00 0:00 0:00 1× Show full transcript ▼ This transcript was generated automatically, probably contains mistakes, and has not been manually verified. ZOE ROSE We need an LLM that says, here's how to do it. And don't forget to consider these things. Unknown No, no, we don't need that actually, Zoe. We don't need any help for the criminals in covering up the tracks. Interesting. Interesting that you should suggest that. Smashing Security, episode 475. JadePuffer, the AI that ran a ransomware attack all by itself. With Graham Cluley and special guest Zoe Rose. Hello, hello, and welcome to Smashing Security episode 475. My name's Graham Cluley. ZOE ROSE And I'm Zoe Rose. GRAHAM CLULEY Hello, Zoe. Welcome back to the show. It's been a while since you've been on. How are you doing? ZOE ROSE Well, usually when I join, something massive has happened. GRAHAM CLULEY Right. ZOE ROSE At the moment, I have not acquired another child or a pet. GRAHAM CLULEY So, well done. ZOE ROSE Yeah. GRAHAM CLULEY So for those who don't know Zoe, what are you? I mean, people who haven't heard of you before, what do you do exactly? ZOE ROSE That's a good question. What do I do? I work in security and pretend I know what I'm talking about half the time. GRAHAM CLULEY Oh, okay. It seems fair enough. And you work for a big company? ZOE ROSE I have a bloody long title now, actually. That's the change. That's what's new. My title has massively increased. GRAHAM CLULEY Okay, give us your title. Let's hear it. ZOE ROSE All right. It is C-Cert, which if you know what that stands for, it has more words, but we'll just stick to some letters. Security Operations Development Manager. GRAHAM CLULEY Wow. ZOE ROSE Yeah. GRAHAM CLULEY Security Operations Development Manager, like SODOM, is basically what you're saying. Unknown Yeah, sure. GRAHAM CLULEY Interesting. Well, before we kick off, let's thank this week's wonderful sponsors, Arctic Wolf, NordLayer, and Vanta. We'll be hearing more about them later on in the podcast. This week on Smashing Security, we're not going to be talking about how a Greek politician investigating spyware had his own mobile phone hacked. You'll hear no discussion of how a US Department of Homeland Security information sharing database has been accessed by hackers. And we won't even mention how hackers are using a fake World Cup t-shirt offer to spread malware. So Zoe, what are you going to be talking about this week? ZOE ROSE I'm going to talk about Apple's Hide My Email isn't actually as hidden as it sounds like. GRAHAM CLULEY And I'm going to be telling the tale of how a 15-year-old with a chatbot became a cybercriminal and what happens when the AI just does the whole job itself. All this and much more coming up on this episode of Smashing Security. JOE Graham, am I right in thinking that Arctic Wolf are sponsoring the show this week? GRAHAM CLULEY You are right, Joe. They've just published a new report, 2026 State of the Cybersecurity Attack Surface, and they analysed over 800,000 real IT assets to find out how exposed organisations actually are. JOE And I'm guessing everything is hunky-dory. GRAHAM CLULEY No, not so much. The reality is they found 1 in 3 IT assets is
```

#### Corroborating sources (1)

- **Graham Cluley** (practitioner_analysis)
  - Title: Smashing Security podcast #475: JadePuffer – the AI that ran a ransomware attack all by itself
  - Published: 2026-07-08T23:19:18+00:00
  - Link: https://grahamcluley.com/smashing-security-podcast-475/
  - Summary: A 15-year-old boy asked a chatbot for help - and cancelled nearly 47,000 anime streaming subscriptions in under four hours. Meanwhile, researchers have documented the first fully autonomous, agentic AI-driven ransomware attack, "JadePuffer". What does this tell us about the future of cybersecurity? Also, Apple's "Hide My Email" feature turns out to hide rather less than it promises - despite Apple knowing it has a problem for over a year. All this and more in this episode of the "Smashing Security" podcast with cybersecurity expert and keynote speaker Graham Cluley, and special guest Zoë Rose.

### Cluster 8ca1179b44 — score 9

- Title: [tl;dr sec] #336 - Autonomous Vulnerability Hunting, GuardDog 3.0, Are Bug Bounties Cooked?
- Source: tl;dr sec (practitioner_analysis)
- Published: 2026-07-09T14:30:00+00:00
- Link: https://tldrsec.com/p/tldr-sec-336
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: GitHub, Gitea
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: GitHub, Gitea
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Summary

```
An MCP powered system that's continuously finding and reproducing vulns, improvements to Datadog's OSS malware hunting tool, Hakluke muses on the future of bug bounty
```

#### Full body

```
0 tl;dr sec Posts [tl;dr sec] #336 - Autonomous Vulnerability Hunting, GuardDog 3.0, Are Bug Bounties Cooked? [tl;dr sec] #336 - Autonomous Vulnerability Hunting, GuardDog 3.0, Are Bug Bounties Cooked? An MCP powered system that's continuously finding and reproducing vulns, improvements to Datadog's OSS malware hunting tool, Hakluke muses on the future of bug bounty Clint Gibler July 09, 2026 Hey there, I hope you’ve been doing well! 🎆 Amurrica Day I love how peak America the 4th of July is, with tons of outdoor grilling, people wearing red, white, and blue, and of course fireworks. In some circles, it’s not cool to be patriotic right now. While we have and will continue to make mistakes as a country, I think we can still be proud of the good parts, while striving to do better. I think everyone should be proud of where they came from, and what makes that place unique. This year I watched the Pier 39 fireworks from a nearby rooftop while a DJ blasted Katy Perry’s song Firework (not the Moulin Rouge musical version). Watching fireworks in San Francisco is often a futile endeavor, given the high likelihood that what you actually get to see is some slight glimmers in the ever present fog. Still, it was fun. Though I must say getting home was a disaster - tons of traffic on narrow roads, and frequent traffic jams due to Waymos. I think it took like 2.5 hours to get home, when I could have walked home in an hour. I considered jumping out of the car and tucking and rolling, and by that I mean calmly stepping out and standing, as we were basically parked. Wherever you were, I hope you had a fun and connecting weekend with family and friends 🤗 P.S. If you or a friend is an excellent software engineer, my team at OpenAI is hiring: job description . Early access to models, infinite tokens, and even higher ambition. We’re aiming to secure the world and Patch the Planet. You in? Sponsor 📣 What If Every Threat Report Came With the Hunt Already Done? A vendor report drops a new TTP into your Slack. Somewhere in it is what actually matters to your environment, and knowing where to look is the real skill, not typing the query. HUMAN Security built hunting agents in BlinkOps that read the report, cut straight to what is relevant, then hit every system in your stack, SIEM, EDR, cloud logs, combining deterministic logic with LLM. No blind spots left uninspected. What comes back is not a guess. It is the real blast radius, exposed. We recorded the full process. 👉 Watch the Process Behind a Threat Hunting Agent 👈 From threat intel → to hunt across your SIEM, EDR, and more + automatically feeding confirmed threats into detection engineering is pretty cool. This is a great area where AI can scale defensive work. AppSec Exploitarium: Mass Disclosure of Zero-Day Proof-of-Concepts Ethan Andrews describes how an anonymous GitHub researcher named "bikini" published Exploitarium , an archive of over 130 proof-of-concept exploits and vulnerability write-ups dropped without informing vendors, covering targets like libssh2, Gitea, 7-Zip, Docker, OpenVPN Connect, VLC, and nmap. 💡 As more people gain the ability to find serious vulnerabilities, we might see more drops like this 😅 Important to speed up triage and patching for maintainers, as well as companies. Are bug bounties cooked? Luke Stephens (Hakluke) disagrees that bug bounties are cooked despite AI reshaping the field. Critical bugs used to take years of intuition and target knowledge, but now the same bugs are within reach of anyone with a frontier model subscription, so supply is up while demand isn't and payouts are down. He isn't worried about HackerOne and Bugcrowd training on submissions or pre-cleaning bugs, since hackers already compete against internal security teams' AI, top hunters' automation, and offensive AI startups like XBOW, Ethiack, and Penligent. What worries him is cost, since frontier model tokens now run top hunters hundreds to thousands a month, and if that becomes the ticket to c
```

#### Corroborating sources (1)

- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #336 - Autonomous Vulnerability Hunting, GuardDog 3.0, Are Bug Bounties Cooked?
  - Published: 2026-07-09T14:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-336
  - Summary: An MCP powered system that's continuously finding and reproducing vulns, improvements to Datadog's OSS malware hunting tool, Hakluke muses on the future of bug bounty

### Cluster eb43b37f29 — score 8

- Title: Vulnify: Giving Your Agents a CVE Brain
- Source: TrustedSec (detection_response_operations)
- Published: 2026-07-09T04:00:00+00:00
- Link: https://trustedsec.com/blog/vulnify-giving-your-agents-a-cve-brain
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
<p>The CVE brain your AI agent has been missing. In this blog, we introduce Vulnify, an open-source tool that stitches eight authoritative vulnerability databases into a single offline source of truth for CVE intelligence.</p>
```

#### Full body

```
Blog Vulnify: Giving Your Agents a CVE Brain July 09, 2026 Vulnify: Giving Your Agents a CVE Brain Written by Brandon McGrath Artificial Intelligence (AI) Table of contents How It Got Built What's Actually In It? One CVE The Explorer Talking to It: The MCP Server Actually Using It You Don't Have to Use MCP Wrapping Up When building agentic components for pentesting, CVEs are inevitably going to come up. I never found anything that matched what I needed; I did not want "search the web and hope," but actual answers bound to a technology, and the ability to answer questions like “Does this version of this package have this CVE?”, “Is there a public exploit?”, “and “Where is it?” By packaging all that up, agents can get a head start on the scope of the product they’re looking at. Prior to this work, there are a few ways it can be fudged. The first is by letting the agent search the web with Tavily . It sort of works, but it is slow and non-deterministic, and the agent ends up reading vendor marketing and blogspam to find a CVSS score that lives in a database somewhere. Or, even worse, the 1,000 free credits a month don’t scale - I don’t fancy Yet-Another-Subscription . The second is by bolting on a scanner like Nuclei . Nuclei is great at templated detection against a live host. But we may not always want to point heavy tools at a product right away. Following the approach of recon and light poking first, Nuclei doesn’t fit. The third is by hitting NVD and vendor APIs live. This is the closest-to-right solution, but painful to do deterministically and a waste of tokens to let agents figure it out. NVD also throttles you to about five (5) requests every 30 seconds without a key. Furthermore, every source has its own schema, and nothing joins together well. None of these solve the problem, they work around it and are probably fine for smaller projects, but they do not satisfy my stability and reproducibility requirements, let alone save tokens. This is where Vulnify comes in. It is an MCP-capable server set on top of one (1) normalized SQLite database that stitches the authoritative sources together and hands the agent a clean, joined answer. One (1) caveat up front, Vulnify is point-in-time. It needs to pull data every so often to stay relevant; I am working on something CICD-able for this in the future. How It Got Built Before I discuss the internals, I want to make a foreword on writing bigger projects with agentic workflows. I find that LLMs are great at extending a codebase that already has a strong opinion baked in. If you let an agent loose on a new project with no guardrails or guidelines, you will see all sorts of weird and wonderful coding styles. My personal approach, and the approach used to build Vulnify, is to manually build v0.1. I know, writing code in 2026—wow. But, by doing so, I get to lay the groundwork for coding paradigms: how docstrings are laid out, how functions are named, data models, and generally writing the code how I like to. Then, I pass an agent (Claude, in my case) over top of it to learn it, write docs, and update CLAUDE.md and memory; whatever it needs to ensure it matches my style. Then, over time, I introduce subagents to reinforce that pre-commit. If this first pre-pass is done in a strong model like Opus 4.8, then all subsequent work can be done with something like Sonnet, or even local models in some cases. From there, it is spec-driven , one (1) feature at a time: plan, grill, and build. Plan is a written spec with scope and acceptance criteria. Grill is where I stress-test that plan against the real codebase before a line is written and the load-bearing constraints and awkward edge cases turn up on paper, where they are cheap to fix. Build is implementing in slices to contain scope and context. Doing all this keeps the codebase coherent because a human set the taste, and the tooling enforces it. It does not get re-argued by every agent that shows up. What's Actually In It? Vulnify is one (1)
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: Vulnify: Giving Your Agents a CVE Brain
  - Published: 2026-07-09T04:00:00+00:00
  - Link: https://trustedsec.com/blog/vulnify-giving-your-agents-a-cve-brain
  - Summary: <p>The CVE brain your AI agent has been missing. In this blog, we introduce Vulnify, an open-source tool that stitches eight authoritative vulnerability databases into a single offline source of truth for CVE intelligence.</p>

### Cluster 9d6bdd5305 — score 8

- Title: Effective Patch Management Strategies: 7 Best Practices | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-07-13T15:00:00+00:00
- Link: https://www.huntress.com/blog/patch-management-strategy
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure, zero_day
- affected_products: Anthropic/Claude, Apple iOS/macOS, OpenAI/ChatGPT
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure, active_exploitation
- affected_products: Apple iOS/macOS, Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Stop letting bad actors exploit old bugs. Build a practical patch management strategy to keep them out and learn to stay secure without all the fluff.
```

#### Full body

```
Home Blog Effective Patch Management Strategies: 7 Best Practices and Benefits Published: July 13, 2026 Effective Patch Management Strategies: 7 Best Practices and Benefits By: Brenda Buckman Summarize with AI Summarize ChatGPT Claude Perplexity Google AI A patch management strategy is a structured approach to identifying, testing, and deploying software updates across your environment. Having a dedicated strategy matters because ad hoc patching leaves gaps, and gaps are what attackers look for. Most security incidents don't start with a sophisticated attack. They start with a known vulnerability that never got patched. In fact, patching is one of the most direct ways to disrupt an attack before it starts. A weaponized exploit targeting a vulnerability your team already patched has nowhere to go. A patch management strategy is a structured approach to identifying, testing, deploying, and verifying software updates across your environment. Having a dedicated strategy matters because ad hoc patching leaves gaps—and those exposed systems are exactly what attackers look for. Learn how to build a patch management strategy that holds up under real operational pressure, not just on paper. You'll find a step-by-step framework, best practices, and common mistakes to avoid before they cost you. What is patch management? Patch management is a proactive security discipline. It's the process of identifying, evaluating, and applying updates to software, operating systems, and firmware across your environment. But it goes well beyond clicking "install" on a notification and moving on. Think of it this way: A patch dropping is just the starting gun. Before anything touches production, your team needs to know what systems are affected, how urgent the fix actually is, and whether the update could break something else in the process. That whole workflow, from discovery to verified deployment, is what patch management actually covers. IT teams typically manage three categories of updates: OS patches (Windows, Linux, macOS): Core system updates that often carry the highest security risks Third-party application patches : Browsers, productivity tools, plugins, and other software that threat actors frequently exploit because they're easy to overlook Firmware and driver updates : Lower-level updates for hardware like network switches, servers, and endpoints that can introduce risk if left unaddressed The lifecycle spans from initial discovery through final verification that a vulnerability is actually gone. Each stage carries its own risks and requires its own judgment call. Security patches vs. bug fixes vs. feature updates Not all updates are equal, and treating them the same way is a recipe for patch fatigue or, worse, a broken production system. Here's how they stack up: Security patches Bug fixes Feature updates Purpose Close known vulnerabilities Correct unintended behavior Add new functionality Trigger Vulnerability disclosure or active exploit Software defect or crash report Product roadmap or user request Urgency High to critical Low to medium Low Testing requirements Expedited but still necessary Standard Thorough Risk High if delayed Moderate Low to moderate User impact Usually minimal Minimal to moderate Can change workflows Who owns Security team drives, IT deploys IT or dev team Change management or IT The core tension here is speed vs. stability. Security patches often need aggressive timelines because attackers move fast once a vulnerability is public. A zero-day vulnerability can go from disclosed to actively exploited within hours, leaving little room for a slow approval process. Feature updates, on the other hand, can usually afford a longer wait time. Rolling them out too fast without testing is how you end up with a broken workflow that's harder to fix than the patch was worth. 7 steps to building a patch management strategy from the ground up A solid patch management strategy is a repeatable system your team can actually execute
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Effective Patch Management Strategies: 7 Best Practices | Huntress
  - Published: 2026-07-13T15:00:00+00:00
  - Link: https://www.huntress.com/blog/patch-management-strategy
  - Summary: Stop letting bad actors exploit old bugs. Build a practical patch management strategy to keep them out and learn to stay secure without all the fluff.

### Cluster cf781d85e9 — score 8

- Title: Threat Actors Achieve Persistence After SQL Injection
- Source: Huntress (detection_response_operations)
- Published: 2026-07-13T13:00:00+00:00
- Link: https://www.huntress.com/blog/sql-injection-attacker-persistence
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
See how a threat actor used SQL injection and BadIIS to gain persistence, disable Windows Defender, and quietly install a cryptominer.
```

#### Full body

```
Home Blog Home Field Advantage: How Attackers Reshape Victim Environments Published: July 13, 2026 Home Field Advantage: How Attackers Reshape Victim Environments By: Harlan Carvey Lindsey O'Donnell-Welch Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways After gaining initial access, threat actors sometimes spend time modifying the compromised environment before pursuing their end goals. That means establishing persistence, concealing activity, and deploying tools designed to make detection and eviction significantly more difficult. Huntress analysts recently investigated an incident where a threat actor made an exceptionally broad range of post-compromise modifications across an organization, including installing BadIIS modules, adding new users accounts, and more. For defenders, post-compromise behavior is just as important to monitor as initial access attempts. Identifying root cause, reducing attack surface, and maintaining visibility into endpoint activity are all critical to fully removing a threat actor from the environment. Acknowledgments: Special thanks to the efforts of Stephanie Fairless for the contributions to this investigation. "The call is coming from inside the house." Defenders often prioritize preventing threat actors from getting in, whether through vulnerability exploitation or exposed Remote Desktop Protocol (RDP) instances. But equally (if not more) important is what happens when an attacker has already made their way in. While some attackers go straight for the kill – exfiltrating data, encrypting files, or otherwise – many take a more strategic approach to mold the compromised environments to suit their needs first. They'll proactively tweak things within the environment to hide their tracks or work in some persistence. That might look like enabling the built-in Windows Guest account. It might be running Windows CLI commands like tasklist /svc to sniff out what processes a victim might be running. At Huntress, our SOC focuses on these measures with a laser focus, because they often provide hints for what happened during an incident and may even reveal new parts of an attack that weren't initially detected. In this blog post we will break down a June incident where a threat actor took aggressive steps to modify the environment after gaining initial access, in hopes of shedding light on some of these overlooked tactics. Initial Access: the first MSSQL detections During a recent incident for an organization in the tech sector, Huntress analysts observed a threat actor making more modifications to the compromised environment than usually observed during incidents of a similar nature. The June 26 incident started with the Huntress SOC detecting and reporting malicious activity via a Microsoft SQL Server (MSSQL) instance ( sqlservr.exe ). Digging deeper into the investigation, Huntress analysts discovered that the threat actor did not access the MSSQL instance directly, but instead was able to locate a web page (the IIS web server was also installed on the endpoint) where user input was not being properly validated. As a result, based on this evidence we determined that the threat actor was able to access the endpoint by successfully exploiting an SQL injection vulnerability. Teeing things up: recon and persistence Through this avenue, the threat actor used base64-encoded PowerShell to download various scripts, which we will delve into later in this blog post. Next, the actor carried out some recon: they ran tasklist /svc to determine what processes were running and available on the endpoint. This legitimate Windows command can help attackers identify potentially valuable services. That allows them to plan their next moves for what to target next – or even understand what services exist that they can potentially spoof with malicious processes. In this case, threat actors also used a PowerShell command to send the output of tasklist /svc to 334thribetlhkyo977gqrcht1k7bvdj2[.]oasti
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Threat Actors Achieve Persistence After SQL Injection
  - Published: 2026-07-13T13:00:00+00:00
  - Link: https://www.huntress.com/blog/sql-injection-attacker-persistence
  - Summary: See how a threat actor used SQL injection and BadIIS to gain persistence, disable Windows Defender, and quietly install a cryptominer.

### Cluster eee3f3e905 — score 8

- Title: Guide to System Hardening: Checklist & Best Practices [2026] | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-07-10T13:00:00+00:00
- Link: https://www.huntress.com/blog/system-hardening-checklist
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Threat actors want an easy way in. Use this practical system-hardening checklist to close gaps and learn how to secure your environment today.
```

#### Full body

```
Home Blog The Complete Guide to System Hardening: Checklist and Best Practices Published: July 10, 2026 The Complete Guide to System Hardening: Checklist and Best Practices By: Brenda Buckman Summarize with AI Summarize ChatGPT Claude Perplexity Google AI System hardening is the process of configuring systems to reduce the ways an attacker can get in or move around once they're inside. A system hardening checklist gives IT teams a structured way to work through that process, covering areas like user accounts, network configuration, patch management, and logging. Think of it as a practical starting point for closing the gaps left by default settings. Your security is only as strong as your weakest link, or in this case, your weakest configuration. A system hardening checklist gives IT teams a practical, repeatable way to close the gaps attackers target: default credentials, open ports, unnecessary services, and misconfigured permissions. It's one of the most foundational elements of good cyber hygiene , and one of the most common oversights when teams are stretched thin. The problem is that hardening isn't a one-time task. Configurations drift, new systems get added, and exceptions pile up. This guide walks through every major category of hardening, from user accounts and network configuration to logging and physical security controls, so you have a clear starting point and a process you can actually maintain. What is system hardening? System hardening is the process of configuring systems to reduce the ways an attacker can get in or move around once they're inside. Think open ports, default accounts, unused services, or weak settings. Every one of those is a potential entry point, and hardening closes them off before someone can take advantage. It's also worth distinguishing between hardening and patching , because the two are often confused: Patching fixes known vulnerabilities in software Hardening changes how a system is configured, making those vulnerabilities harder to reach or exploit in the first place Both are important parts of vulnerability management , and neither one substitutes for the other. Why system hardening matters Out-of-the-box systems aren't built with security as the priority. They're built for ease of use, which means they often ship with open ports, enabled services, and default credentials that attackers actively scan for. Misconfigurations consistently rank among the top causes of breaches , and default settings are one of the most common culprits. There's also a compliance angle worth noting. Cybersecurity frameworks like CIS Benchmarks, NIST SP 800-53, and DISA STIGs all include hardening requirements, and organizations subject to HIPAA, PCI DSS, or CMMC need documented hardening practices to pass audits. Essentially, you need to meet a baseline of protections so that if a cyber event happens, you can clearly show that you've done your due diligence. Ultimately, a hardened system is tougher to compromise, cheaper to defend, and less likely to become the entry point for a ransomware attack or data breach. The work you put in up front pays off every time an attacker moves on to an easier target. The complete system hardening checklist This is the practical core of system hardening: A step-by-step checklist organized by category that IT admins can work through systematically. Not every item will apply to every environment, so use this as a starting point and adapt it to the systems you're hardening. For the most detailed guidance, cross-reference the relevant CIS Benchmark for your specific OS or platform. Description Type Governance User account and access controls Disable default accounts, enforce password policies, apply least privilege, and enable MFA for privileged access OS hardening CIS Benchmarks, NIST SP 800-53 Network configuration Restrict traffic with default-deny rules, disable unused ports and protocols, and segment networks to limit lateral movement Network hardening CIS Benchmarks, NIS
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Guide to System Hardening: Checklist & Best Practices [2026] | Huntress
  - Published: 2026-07-10T13:00:00+00:00
  - Link: https://www.huntress.com/blog/system-hardening-checklist
  - Summary: Threat actors want an easy way in. Use this practical system-hardening checklist to close gaps and learn how to secure your environment today.

### Cluster ec6ada1c31 — score 8

- Title: Reduce Human Risk | Build a Strong Security Awareness Training Program | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-07-09T20:00:00+00:00
- Link: https://www.huntress.com/blog/what-is-a-security-awareness-training-program
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, data_breach, phishing_social_eng, ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: education
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, data_breach, apt_espionage, web_shell_backdoor
- affected_industries: education
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Build a security awareness training program that actually changes user behavior. Huntress Managed SAT delivers engaging content, phishing sims, and results.
```

#### Full body

```
Home Blog What Is a Security Awareness Training Program? Last Updated: July 9, 2026 What Is a Security Awareness Training Program? By: Lizzie Danielson James O’Leary Summarize with AI Summarize ChatGPT Claude Perplexity Google AI 68% of data breaches start with a person making a mistake. Not a sophisticated zero-day exploit. Not a nation-state backdoor. A person clicking the wrong link, reusing a password, or trusting an email that looked just real enough. One of the most effective ways to stop a cyberattack is to implement a security awareness training program. Every employee, from the C-suite to the interns, needs to know how to spot a suspicious email, where to report it, and why it’s so critical. The average cost of a data breach is now firmly in the multi-million-dollar range, about $4.44 million globally and $10.22 million in the U.S., according to IBM’s 2025 Cost of a Data Breach Report. Here's the uncomfortable truth: your people are the biggest risk to your organization’s security. But they're also your strongest defense; if you train them right. In this article, we’ll break down why security awareness training is an essential component for building a strong cybersecurity culture within your organization What is a security awareness training program? A security awareness training program teaches employees how to spot and respond to cybersecurity threats: phishing emails, weak passwords, social engineering, malware, ransomware — and gives them practical steps to avoid them. Think of it this way: without a formal program, you're just hoping employees know what to do. A comprehensive training program does more than just run phishing tests; it provides ongoing education and engaging content that builds a baseline of security knowledge across your organization. Your employees are the first line of defense. By fostering a culture of security through training, you empower them to protect the business. The value of security training is immense—organizations spend far more time, money, and resources cleaning up after a data breach than they do preventing one. 15 must-have components of an effective behavior security awareness training program Ready to build a program that actually works? Here are the 16 essential components every security awareness training program should include. 1. Engaging training content If you want employees to retain what they learn, the content has to be fun and relatable. Ditch the "death by PowerPoint" presentations. Your employees should walk away saying they actually enjoyed the training. Implementation guidance: Topics: Cover modern cyber threats like phishing, social engineering, ransomware, password security, and multi-factor authentication (MFA). Format: Use a mix of videos, interactive quizzes, realistic phishing simulatoins, and hands-on learning experiences. Message: Clearly explain why security awareness is so important for the organization and for them personally. 2. Realistic phishing simulator Phishing simulations are one of the most effective ways to assess the impact of your training. The 2025 Verizon Data Breach Investigations Report reveals that 60% of data breaches involve the human element, including phishing attacks, highlighting the critical need for continuous employee education. Implementation guidance: Frequency: Run phishing tests at least monthly. Relevance: Use templates that mimic real-world phishing scams and tradecraft. Goal: Train employees in a safe environment, allowing them to learn from their mistakes without real-world consequences. 3. A simple way to report phishing Employees need a one-click solution to report suspicious emails . Whether they're on a desktop or a mobile device, the process should be simple and consistent. This allows your IT security team to be notified immediately and respond to potential company-wide threats. 4. Learning Management System (LMS) You need a centralized system to record, track, and distribute training content to all employees, inc
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Reduce Human Risk | Build a Strong Security Awareness Training Program | Huntress
  - Published: 2026-07-09T20:00:00+00:00
  - Link: https://www.huntress.com/blog/what-is-a-security-awareness-training-program
  - Summary: Build a security awareness training program that actually changes user behavior. Huntress Managed SAT delivers engaging content, phishing sims, and results.

### Cluster 7a5a1701ad — score 8

- Title: AI-Coded Malware | Analyzing Vibe-Coded AD Enumeration | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-07-08T14:00:00+00:00
- Link: https://www.huntress.com/blog/ai-coded-malware-vibe-coding-active-directory
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Windows
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Microsoft Windows
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Threat actors are now using AI to generate custom PowerShell scripts for Active Directory attacks. Our team analyzed real vibe-coded malware and what it means for defenders.
```

#### Full body

```
Home Blog Analyzing AI-Augmented Network Enumeration Published: July 8, 2026 Analyzing AI-Augmented Network Enumeration By: Jevon Ang Dray Agha Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways We recently came across an incident in early June where a threat actor used a vibe-coded PowerShell script for Active Directory (AD) enumeration. The script looked for the Domain Controller (DC) and mapped users, computers, and domains, before creating a directory and exporting out a number of files, and finally creating AD_Report.html to measure the success of the enumeration attempt. AI-assisted tradecraft continues to change the threat landscape. Defenders should focus on the fundamental behaviors of the attack lifecycle, because while AI can change the code syntax, it can't easily change the underlying parts of an attack, like enumeration. AI-augmented tradecraft is changing the threat landscape that defenders have operated in. For years, defenders have relied on identifying the signatures and behaviors of off-the-shelf offensive tooling, like BloodHound, PowerSploit, or Cobalt Strike. But a new trend is emerging—"vibe coded" malware—and this is shifting how the attacker and detection landscapes operate. Vibe coding is the process of writing software not by manually typing syntax but by iteratively prompting AI with natural language until the output matches the desired function. It has equipped mediocre threat actors with the ability to generate bespoke, single-use scripts. We recently got a first-hand look at this when we recovered a PowerShell script used by a threat actor as part of an incident on June 3. A deep dive into its contents reveals a fascinating case study of how cybercriminals are weaponising AI to map Active Directory (AD) environments. In this blog, we offer a breakdown of the script, why it is undeniably AI-generated, and what this means for the future of threat detection. The attack chain with an AI-assisted twist One thing to emphasize here is that AI isn't changing the game by any means during this incident. The underlying attack chain still resembles the tried-and-tested smash-and-grab playbook we've seen for years. This core methodology has remained consistent, but it is now being selectively augmented by AI. This hybrid approach prioritises aggression and speed over stealth, allowing threat actors to execute highly damaging campaigns faster than ever. The RDP Pivot: The attack kicked off when the threat actor established RDP access (context suggested initial access via the VPN) onto a domain-joined Windows Server with a set of pre-compromised credentials. The Tool Staging: Operating via interactive command prompts, the attacker staged their operations and toolsets in ( C:\ProgramData\ ), which is a nefariously common staging area. The Vibe-Coded Recon: Within minutes of establishing the RDP session, the attacker dropped and executed their bespoke, AI-generated payload ( C:\ProgramData\Untitled1.ps1 ). This was their opening move, to map the Active Directory environment. The Smash-and-Grab: Roughly half an hour later, they deployed C:\ProgramData\s5cmd.exe. s5cmd is a legitimate, high-speed command-line tool for Amazon S3 operations, which we have seen being abused frequently for data exfiltration. The Second Bite: After securing the initial payload from the compromised server, the attacker went back to the well. They deployed SharpShares.exe , a known enumeration tool , deliberately filtering out common administrative shares to hunt for further user-accessible data repositories. While investigating the incident, we identified and fully recreated Untitled1.ps1 using Huntress SIEM telemetry—Event ID 4104 in the Microsoft-Windows-PowerShell/Operational , which contains blocks of PowerShell scripts that have been deployed. Here's what we found (and for those who would like to follow along themselves, you can find the full script at: Loading Gist... Anatomy of the AI-Generated recon too
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: AI-Coded Malware | Analyzing Vibe-Coded AD Enumeration | Huntress
  - Published: 2026-07-08T14:00:00+00:00
  - Link: https://www.huntress.com/blog/ai-coded-malware-vibe-coding-active-directory
  - Summary: Threat actors are now using AI to generate custom PowerShell scripts for Active Directory attacks. Our team analyzed real vibe-coded malware and what it means for defenders.

### Cluster 0fefb209ee — score 8

- Title: Key findings from the 2026 Public Sector M-Trends report and beyond
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-07-13T16:00:00+00:00
- Link: https://cloud.google.com/blog/topics/public-sector/key-findings-from-the-2026-public-sector-m-trends-report-and-beyond/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, apt_espionage
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
In 2026, the public sector is no longer defending a traditional perimeter. Instead, they are defending a complex web of interconnected trust relationships against adversaries that now operate at machine speed. We recently published the 2026 Public Sector Threat Landscape: M-Trends and Beyond report, which distills more than 500,000 hours of frontline incident investigations conducted by Mandiant in 2025, specifically tailored to the mission-critical needs of public sector leaders. Key findings from the report and what they mean for the public sector The most alarming trend in this year’s M-Trends data is the 22-second hand-off: the median time between an initial access broker establishing a foothold and the hand-off to a ransomware operator. This extreme compression of the attack cycle renders traditional, human-speed triage obsolete. When an infection on a municipal workstation can move to an encrypted network before a human analyst can even open a ticket, the strategic mandate for re
```

#### Full body

```
Public Sector Key findings from the 2026 Public Sector M-Trends report and beyond July 13, 2026 Fernando Tomlinson Jr. Head of Incident Response Jose Valerio Lead Threat Intelligence Advisor, Public Sector Google Public Sector Newsletter Essential public sector updates with Google Cloud insights. Subscribe In 2026, the public sector is no longer defending a traditional perimeter. Instead, they are defending a complex web of interconnected trust relationships against adversaries that now operate at machine speed. We recently published the 2026 Public Sector Threat Landscape: M-Trends and Beyond report, which distills more than 500,000 hours of frontline incident investigations conducted by Mandiant in 2025, specifically tailored to the mission-critical needs of public sector leaders. Key findings from the report and what they mean for the public sector The most alarming trend in this year’s M-Trends data is the 22-second hand-off: the median time between an initial access broker establishing a foothold and the hand-off to a ransomware operator. This extreme compression of the attack cycle renders traditional, human-speed triage obsolete. When an infection on a municipal workstation can move to an encrypted network before a human analyst can even open a ticket, the strategic mandate for resilience must pivot toward machine-speed defense. Additionally, the report uncovered several emerging "boundaries of trust" that adversaries are systematically exploiting: The persistence paradox: State-sponsored espionage actors are pursuing multi-year persistence, with some remaining undetected for over five years. This "persistence paradox" directly challenges standard 90-day telemetry retention policies, often leaving agencies unable to quantify the full impact of a breach. The virtualization stack: Attackers are moving "down the stack" to target the virtualization management plane. Techniques like "snapshot mounting" allow attackers to bypass guest-level security tools, creating snapshots of domain controllers to steal databases offline. The SaaS domino effect: At the state and local levels, the reliance on third-party cloud tools has turned integrations into threat vectors. Exploiting non-human identities (NHIs) like service accounts and OAuth tokens allows a single compromise to trigger a chain reaction across an entire agency network. The vishing surge: Voice phishing (vishing) has surged to 11% of global infections. These highly effective social engineering attacks target government help desks to reset passwords or enroll unauthorized devices. This proves that the ‘human element’—the administrative trust placed in help desk staff and IT administrators—is now a primary vector for establishing initial access. A mandate for continuous verification Looking ahead, resilience in the public sector will require more than a compliance checklist; it demands a cultural pivot to continuous verification—a security doctrine where trust is never assumed and must be constantly re-validated. Success is no longer just defined by the absence of a breach, but also by an agency’s ability to remain operational while under active attack. At Google, we provide the technical architecture to make continuous verification a reality through three core capabilities. Identity as the new perimeter: Through Chrome Enterprise Premium , we replace traditional VPNs with context-aware access. We verify the user’s identity and the security posture of their device for every single application request, ensuring that access is only granted under the right conditions. Agentic defense: We enable agencies to ingest and analyze massive telemetry datasets in real-time using Google Security Operations , which includes threat-centric case management, interactive, context-rich alert graphing, and automatic stitching together of entities. This allows for the "Machine-Speed" detection required to spot an adversary within the 22-second hand-off window, turning manual triage into automat
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Key findings from the 2026 Public Sector M-Trends report and beyond
  - Published: 2026-07-13T16:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/public-sector/key-findings-from-the-2026-public-sector-m-trends-report-and-beyond/
  - Summary: In 2026, the public sector is no longer defending a traditional perimeter. Instead, they are defending a complex web of interconnected trust relationships against adversaries that now operate at machine speed. We recently published the 2026 Public Sector Threat Landscape: M-Trends and Beyond report, which distills more than 500,000 hours of frontline incident investigations conducted by Mandiant in 2025, specifically tailored to the mission-critical needs of public sector leaders. Key findings from the report and what they mean for the public sector The most alarming trend in this year’s M-Trends data is the 22-second hand-off: the median time between an initial access broker establishing a foothold and the hand-off to a ransomware operator. This extreme compression of the attack cycle renders traditional, human-speed triage obsolete. When an infection on a municipal workstation can move to an encrypted network before a human analyst can even open a ticket, the strategic mandate for re

### Cluster c8b407c1b8 — score 8

- Title: Building the AI-defined vehicle with Android, Google Cloud, and Nexus SDV
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-07-13T16:00:00+00:00
- Link: https://cloud.google.com/blog/products/databases/nexus-sdv-uses-bigtable-android-automotive-for-agentic-vehicles/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- affected_industries: manufacturing_industrial
- affected_products: Google Cloud, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: manufacturing_industrial
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The automotive industry is moving from building hardware-centric platforms toward building their own sophisticated Software-Defined Vehicle (SDV) architectures. For OEMs, a vehicle is no longer just a way to go from point A to point B, but an intelligent, connected node within an AI-native ecosystem! With its partners, Google’s Android and Google Cloud are at the forefront of this transition. Android’s open source Automotive OS (AAOS) SDV implements the AI-defined vehicle while Google Cloud provides scalable infrastructure including a full suite of AI integration tools, leveraging services like Bigtable for automotive and manufacturing telematics at scale. Valtech, a Google Cloud partner, uses Google technologies as part of its Nexus SDV platform , establishing a full end-to-end connected vehicle system that enables truly agentic mobility, offering automotive OEMs a ready-to-use, end-to-end foundation for the next generation of connected vehicles. Let’s take a look at how this all come
```

#### Full body

```
Databases Building the AI-defined vehicle with Android, Google Cloud, and Nexus SDV July 13, 2026 Peter Ivanov Managing Director, Valtech Mobility Matt Crowley Group Product Manager, Android Automotive, Google Try Gemini Enterprise Business Edition today The front door to AI in the workplace Try now The automotive industry is moving from building hardware-centric platforms toward building their own sophisticated Software-Defined Vehicle (SDV) architectures. For OEMs, a vehicle is no longer just a way to go from point A to point B, but an intelligent, connected node within an AI-native ecosystem! With its partners, Google’s Android and Google Cloud are at the forefront of this transition. Android’s open source Automotive OS (AAOS) SDV implements the AI-defined vehicle while Google Cloud provides scalable infrastructure including a full suite of AI integration tools, leveraging services like Bigtable for automotive and manufacturing telematics at scale. Valtech, a Google Cloud partner, uses Google technologies as part of its Nexus SDV platform , establishing a full end-to-end connected vehicle system that enables truly agentic mobility, offering automotive OEMs a ready-to-use, end-to-end foundation for the next generation of connected vehicles. Let’s take a look at how this all comes together. The vehicle side: AAOS SDV As the foundational in-vehicle platform, Google’s open source AAOS SDV platform abstracts core functions into reusable services independent of physical hardware, establishing a modular Service-Oriented Architecture (SOA). By decoupling non-safety domains like climate control, lighting, and diagnostics from Electronic Control Units (ECUs), the AAOS SDV platform introduces dynamic runtime service discovery. With this, the SDV can easily discover what services are running (e.g., the odometer, HVAC, sunroof, motorized seats, electric windows, etc.) and their status. To accelerate development, engineering teams leverage the Android Cuttlefish emulator to build digital twins in the cloud, simulating high-frequency sensor streams to validate these decoupled services bit-for-bit before physical silicon is ready. Valtech Nexus SDV utilizes this AAOS SDV middleware layer to discover, map, and manage vehicle resources, structuring and streaming high-frequency telemetry data straight into Bigtable. Compare this to the prior state of affairs, where OEMs outsourced system software to a variety of suppliers, each with their own pipelines, protocols, and data stored in separate silos. Crucially, this model decouples services from the heavy main infotainment stack, so they can run independently, even when the vehicle is off and parked. This allows functions like remote vehicle monitoring to remain active even when the primary infotainment system is powered down, ensuring continuous telemetry access without draining the vehicle’s 12V battery or main EV battery pack. This tight integration between the AAOS SDV platform and Nexus SDV enables a number of agentic AI and innovative first-party solutions. Unlike traditional sandboxed infotainment tools, multimodal AI agents can utilize the service discovery layer to safely interact with the physical car and process complex, intent-based requests. For example, an AI agent could automatically adjust climate zones, window actuators, or interior lighting based on a conversation with the driver, or in response to climate sensors, as in this clip: By linking this on-vehicle service layer managed by Nexus SDV with historical fleet telemetry stored in Bigtable, you deliver deeply integrated experiences that unlock new mobility solutions. Now let’s take a quick look at the Cloud side. The Google Cloud side: AI-native mobility Beyond SDV, we are rapidly moving toward AI-defined vehicles, or AIDV, where AI is core to a vehicle's operational logic. To be AI-native means being autonomous by design, with AI embedded at every architectural level. With this level of AI, the system can perceive environm
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Building the AI-defined vehicle with Android, Google Cloud, and Nexus SDV
  - Published: 2026-07-13T16:00:00+00:00
  - Link: https://cloud.google.com/blog/products/databases/nexus-sdv-uses-bigtable-android-automotive-for-agentic-vehicles/
  - Summary: The automotive industry is moving from building hardware-centric platforms toward building their own sophisticated Software-Defined Vehicle (SDV) architectures. For OEMs, a vehicle is no longer just a way to go from point A to point B, but an intelligent, connected node within an AI-native ecosystem! With its partners, Google’s Android and Google Cloud are at the forefront of this transition. Android’s open source Automotive OS (AAOS) SDV implements the AI-defined vehicle while Google Cloud provides scalable infrastructure including a full suite of AI integration tools, leveraging services like Bigtable for automotive and manufacturing telematics at scale. Valtech, a Google Cloud partner, uses Google technologies as part of its Nexus SDV platform , establishing a full end-to-end connected vehicle system that enables truly agentic mobility, offering automotive OEMs a ready-to-use, end-to-end foundation for the next generation of connected vehicles. Let’s take a look at how this all come

### Cluster 91c24e6cda — score 8

- Title: US, Allies Warn of Russian Cyberattacks Targeting Critical Infrastructure Routers
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-14T10:51:01+00:00
- Link: https://www.securityweek.com/us-allies-warn-of-russian-cyberattacks-targeting-critical-infrastructure-routers/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, supply_chain, web_shell_backdoor
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- affected_products: Anthropic/Claude, Microsoft 365, Okta
- cve_ids: CVE-2008-4128, CVE-2018-0171
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, apt_espionage, web_shell_backdoor
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- affected_products: Anthropic/Claude, Okta, Microsoft 365
- cve_ids: CVE-2008-4128, CVE-2018-0171
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Multiple state-sponsored APTs are compromising poorly secured devices across critical infrastructure sector networks. The post US, Allies Warn of Russian Cyberattacks Targeting Critical Infrastructure Routers appeared first on SecurityWeek .
```

#### Full body

```
Russian state-sponsored advanced persistent threat (APT) actors are targeting networking devices to compromise critical infrastructure worldwide, the US and its allies warn. The activity involves scanning for poorly secured devices, mainly routers, for exploitation, government agencies from the US, Australia, Canada, the Czech Republic, Denmark, Estonia, Finland, Italy, New Zealand, Poland, Sweden, and the UK say in a joint advisory (PDF). According to the authoring agencies, Russian Federal Security Service (FSB) Center 16 threat actors, such as Berserk Bear, Energetic Bear, Crouching Yeti, Dragonfly, Ghost Blizzard, and Static Tundra, have been seen engaging in these attacks. The activity targets critical infrastructure organizations across the communication, defense industrial base, energy, financial, government, and healthcare and public health sectors. Using proxies, the threat actors send Simple Network Management Protocol (SNMP) set-requests to IP ranges, instructing the SNMP agents on the target devices to copy configurations to a file and transfer it, usually over Trivial File Transfer Protocol (TFTP), to a virtual private server (VPS) or a compromised FTP server. Additionally, the threat actors have been observed exploiting known vulnerabilities in Cisco devices, including CVE-2008-4128 and CVE-2018-0171 , which lead to arbitrary code and command execution. Advertisement. Scroll to continue reading. “Many of these TTPs overlap with activity by other malicious cyber actors, such as Salt Typhoon ,” the authoring agencies note. Network defenders are advised to disable Cisco Smart Install on all devices, disable SNMPv1 and SNMPv2, use SNMPv3 with modern encryption standards, use unique passwords for accounts on network devices, configure credentials to be stored securely, and monitor for and alert on logins using local accounts. Defenders should also restrict access to SNMP Object Identifiers (OIDs), restrict management protocols, deny external communications on specific ports on edge firewalls and devices, and keep network device software and firmware updated to patch known vulnerabilities. The NSA recently published an advisory on reducing the risk of SNMP abuse. Related: EU Targets Russian Intelligence Officers Accused of Running a Yearslong Cyber Spying Campaign Related: US Offers $10 Million Bounty for Russian State Hackers as Messaging App Attacks Evolve Related: Russian APT Deploys ‘StockStay’ Backdoor Against Ukrainian Targets Related: Russian Spies Are Aggressively Seeking Western Technology as Sanctions Bite, Officials Say Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire RabbitMQ Vulnerability Threatens Enterprise Systems Zimbra Patches Critical Code Execution Vulnerability Organizations Warned of Exploited Joomla Extension Vulnerabilities Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns Ghost Accounts Abuse GitHub API in Mass Recon Campaign Okta Warns of Vishing Attacks Targeting Microsoft 365 Customers GigaWiper Combines Multiple Malware for System-Level Sabotage Network of 200 GitHub Repositories Used for Malware Infection Latest News 7 Severe Vulnerabilities Patched in VMware Avi Load Balancer Unpatched Claude for Chrome Flaw Lets Extensions Read Gmail, Calendar SAP Patches Critical Vulnerabilities in NetWeaver, Approuter, Commerce Cloud Valarian Raises $50 Million for Sovereign Infrastructure Control Layer Multiple Jscrambler Packages Impacted by Supply Chain Attack Pentagon Suspends CMMC Phase 2 as It Rethinks Contractor Cybersecurity Rules Hacker Conversations: Jesse McGraw (GhostExodus), From Blackhat Hacker to Redemption Cybersecurity M&A Roundup: 37 Deals Announced in June 2026 Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay inf
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: US, Allies Warn of Russian Cyberattacks Targeting Critical Infrastructure Routers
  - Published: 2026-07-14T10:51:01+00:00
  - Link: https://www.securityweek.com/us-allies-warn-of-russian-cyberattacks-targeting-critical-infrastructure-routers/
  - Summary: Multiple state-sponsored APTs are compromising poorly secured devices across critical infrastructure sector networks. The post US, Allies Warn of Russian Cyberattacks Targeting Critical Infrastructure Routers appeared first on SecurityWeek .

### Cluster eaade871e6 — score 8

- Title: Armenian national pleads guilty to Ryuk ransomware attacks
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-07-10T20:13:27+00:00
- Link: https://cyberscoop.com/karen-vardanyan-armenian-ryuk-ransomware-guilty/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion
- actor_attribution: Scattered Spider
- affected_industries: critical_infrastructure, education, government, healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage
- actor_attribution: Scattered Spider
- affected_industries: healthcare, government, critical_infrastructure, education
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Karen Vardanyan faces up to 15 years in federal prison and agreed to pay nearly $1.2 million in restitution. The post Armenian national pleads guilty to Ryuk ransomware attacks appeared first on CyberScoop .
```

#### Full body

```
Advertisement Subscribe to our daily newsletter. Subscribe Close An Armenian national who was extradited from Ukraine to the United States last year pleaded guilty to participating in a series of attacks in 2019 and 2020 involving Ryuk ransomware, the Justice Department said Thursday. Karen Serobovich Vardanyan pleaded guilty to computer fraud and conspiracy to commit fraud and extortion. He agreed to pay nearly $1.2 million million in restitution and faces up to 15 years in jail. The 34-year-old admitted to participating in cybercrime from November 2019 to April 2020 when he and his co-conspirators deployed Ryuk ransomware against three U.S.-based organizations while living in Ukraine and Russia. Vardanyan’s victims include a Michigan-based company that paid a ransom of nearly $1.2 million in January 2020, a Watsonville, Oregon-based technology company that was attacked in December 2019 and a Texas-based school breached in February 2020. Advertisement Prosecutors previously accused Vardanyan and his co-conspirators — Ukrainian nationals Oleg Nikolayevich Lyulyava and Andrii Leonydovich Prykhodchenko, and Armenian national Levon Georgiyovych Avetisyan — of illegally accessing computer networks to deploy Ryuk ransomware on hundreds of compromised servers and workstations between March 2019 and September 2020. Ryuk ransomware was prevalent in 2019 and 2020, infecting thousands of victims globally across the private sector, state and local municipalities, local school districts and critical infrastructure, including a wave of attacks on U.S. hospitals. Victims of Ryuk ransomware attacks include Hollywood Presbyterian Medical Center , Universal Health Services , Electronic Warfare Associates , a North Carolina water utility and multiple U.S. newspapers. Ryuk ransomware operators extorted victim companies by demanding ransom payments in Bitcoin in exchange for decryption keys. Justice Department officials said Vardanyan and his co-conspirators received about 1,160 bitcoins — valued at more than $15 million at the time — in ransom payments from victim companies. Vardanyan, as part of his guilty plea, also acknowledged that his conviction will have immigration consequences resulting in removal from the United States after serving his sentence. Advertisement The U.S. District Court for the District of Oregon has yet to schedule his sentencing. Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops The Department of Justice building is seen in Washington, DC, on August 9, 2022. (Photo by Stefani Reynolds / AFP) (Photo by STEFANI REYNOLDS/AFP via Getty Images) Gwengoat, iStock/Getty Images Plus (Getty Images) Latest Podcasts When iPhone exploits turn into commodities What the post-quantum executive order means for CISOs How security investigators can get the right info out of AI security tools Inside Operation Disruption Week: Taking Down Southeast Asia’s Scam Machine Government CISA looks to remedy ailments from big May credential leak French nonprofit starts global intelligence and research hub for AI cyber threats US Army websites defaced with pro-Kurdish sentiments, insults to Trump Someone infected a spyware probe overseer with spyware Technology AI-generated code has made security debt a governance problem Deepfake CSAM lawsuit against xAI, Grok expands US lifting export control restrictions on Anthropic’s Mythos, Fable Supreme Court delivers ‘major win’ for tech privacy in Chatrie ruling Threats Interpol cybercrime crackdown nets 5,800 arrests across 97 countries Suspected Chinese espionage group used a Roundcube exploit chain to burrow into universities Alleged longstanding member of Scattered Spider extradited to US Researchers spot exploitation of another critical Oracle defect Policy Trump budget boss Russell Vought open to re-staffing CISA DHS to unveil replacement council for critical infrastructure cybersecurity Warner bill would create feder
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Armenian national pleads guilty to Ryuk ransomware attacks
  - Published: 2026-07-10T20:13:27+00:00
  - Link: https://cyberscoop.com/karen-vardanyan-armenian-ryuk-ransomware-guilty/
  - Summary: Karen Vardanyan faces up to 15 years in federal prison and agreed to pay nearly $1.2 million in restitution. The post Armenian national pleads guilty to Ryuk ransomware attacks appeared first on CyberScoop .

### Cluster 6b9fe41d07 — score 8

- Title: CISA looks to remedy ailments from big May credential leak
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-07-10T18:54:28+00:00
- Link: https://cyberscoop.com/cisa-credential-leak-forensic-report/
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
A major credential leak spurred the Cybersecurity and Infrastructure Security Agency to strengthen protections for its sensitive materials, improve how researchers can report agency vulnerabilities and develop plans for similar incidents, the agency said in a forensic report released Thursday. The blog post outlines CISA’s response to the leak that the researcher who discovered it […] The post CISA looks to remedy ailments from big May credential leak appeared first on CyberScoop .
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: CISA looks to remedy ailments from big May credential leak
  - Published: 2026-07-10T18:54:28+00:00
  - Link: https://cyberscoop.com/cisa-credential-leak-forensic-report/
  - Summary: A major credential leak spurred the Cybersecurity and Infrastructure Security Agency to strengthen protections for its sensitive materials, improve how researchers can report agency vulnerabilities and develop plans for similar incidents, the agency said in a forensic report released Thursday. The blog post outlines CISA’s response to the leak that the researcher who discovered it […] The post CISA looks to remedy ailments from big May credential leak appeared first on CyberScoop .

### Cluster 8fa37afed0 — score 8

- Title: Microsoft Reins in RoguePlanet Zero-Day Threat
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-09T20:21:19+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/microsoft-rogueplanet-zero-day-threat
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- urgency_signals: zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The researcher known as "Nightmare-Eclipse" published a proof-of-concept (PoC) exploit for the Windows Defender vulnerability in early June after dropping several other Microsoft zero-days.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Microsoft Reins in RoguePlanet Zero-Day Threat
  - Published: 2026-07-09T20:21:19+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/microsoft-rogueplanet-zero-day-threat
  - Summary: The researcher known as "Nightmare-Eclipse" published a proof-of-concept (PoC) exploit for the Windows Defender vulnerability in early June after dropping several other Microsoft zero-days.

### Cluster 152995b5e9 — score 8

- Title: Finding the “Goldilocks” Zone: A Practical Approach to Alert Triage
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-07-08T14:00:00+00:00
- Link: https://www.blackhillsinfosec.com/the-goldilocks-zone/
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
We're all petrified about missing a critical event or misclassifying an alert, but when we're talking about incident response (IR), there are often hundreds if not thousands of alerts to parse through. It's easy to get caught up with one alert because it feels "too hot" or maybe not spend enough time looking into something that initially seems "too cold." The post Finding the “Goldilocks” Zone: A Practical Approach to Alert Triage appeared first on Black Hills Information Security, Inc. .
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: Finding the “Goldilocks” Zone: A Practical Approach to Alert Triage
  - Published: 2026-07-08T14:00:00+00:00
  - Link: https://www.blackhillsinfosec.com/the-goldilocks-zone/
  - Summary: We're all petrified about missing a critical event or misclassifying an alert, but when we're talking about incident response (IR), there are often hundreds if not thousands of alerts to parse through. It's easy to get caught up with one alert because it feels "too hot" or maybe not spend enough time looking into something that initially seems "too cold." The post Finding the “Goldilocks” Zone: A Practical Approach to Alert Triage appeared first on Black Hills Information Security, Inc. .

### Cluster 8f97c174fa — score 8

- Title: Attackers Exploit 'Ill Bloom' Vulnerability to Drain Over $5 Million From Cryptocurrency Wallets
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-10T09:00:05+00:00
- Link: https://thehackernews.com/2026/07/attackers-exploit-ill-bloom.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: financial_services
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Security firm Coinspect has disclosed a crypto wallet flaw it calls Ill Bloom, and attackers are already using it. The flaw is in how some wallet software generated its recovery phrase, the words that control the money. When that phrase is made with weak randomness, an attacker can work it out and take everything it controls. The firm has confirmed one coordinated sweep on May 27
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit 'Ill Bloom' Vulnerability to Drain Over $5 Million From Cryptocurrency Wallets
  - Published: 2026-07-10T09:00:05+00:00
  - Link: https://thehackernews.com/2026/07/attackers-exploit-ill-bloom.html
  - Summary: Security firm Coinspect has disclosed a crypto wallet flaw it calls Ill Bloom, and attackers are already using it. The flaw is in how some wallet software generated its recovery phrase, the words that control the money. When that phrase is made with weak randomness, an attacker can work it out and take everything it controls. The firm has confirmed one coordinated sweep on May 27

### Cluster cdaff85c13 — score 8

- Title: Russian State Hackers Target Vulnerable Routers Worldwide, Joint Advisory Warns
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-13T10:40:00+00:00
- Link: https://www.infosecurity-magazine.com/news/russian-state-hackers-vulnerable/
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
Cybersecurity agencies from 12 countries have warned that Russian state-backed hackers are actively targeting vulnerable routers using weak SNMP credentials
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Russian State Hackers Target Vulnerable Routers Worldwide, Joint Advisory Warns
  - Published: 2026-07-13T10:40:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/russian-state-hackers-vulnerable/
  - Summary: Cybersecurity agencies from 12 countries have warned that Russian state-backed hackers are actively targeting vulnerable routers using weak SNMP credentials
