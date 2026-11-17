# PHANTOMSignal Briefing Packet

- Generated: 2026-11-17T03:35:53.814432+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 76
- Total items in window: 344
- Total clusters raw: 171
- Total clusters in packet: 75
- Dropped low score: 96
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

- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Unit 42** (threat_research_primary)
  - URL: https://unit42.paloaltonetworks.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 4
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
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: fetch_error
  - Item count: 0
  - In window count: 0
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 2
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
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
  - In window count: 1
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 1
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
  - Status: ok
  - Item count: 10
  - In window count: 1
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
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
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 6
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 1
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 8
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
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
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
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
  - In window count: 1
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 1
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
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
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
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 20
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
  - In window count: 7
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 2
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
- **Reddit r/netsecstudents** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsecstudents/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 3
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 50
- **Reddit r/AskNetsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/AskNetsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 28
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Embrace the Red** (ai_security_agentic_risk)
  - URL: https://embracethered.com/blog/index.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 14
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
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 3

## Affinity groups (themes)

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 6
- Article count: 14
- Cohesion: 0.312
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: 26581d7b17, 5fccd3b124, fba6e81cad, d59d57a2e0, 656ea1ba73, 5b374473ad
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/
  - https://www.microsoft.com/en-us/security/blog/2026/11/16/high-volume-phishing-campaign-uses-microsoft-365-outage-lures-target-multiple-industry-sectors-2/
  - https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/
  - https://www.securityweek.com/microsoft-rules-out-cyberattack-in-outage-warns-of-phishing-campaign/
  - https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/
  - https://www.bleepingcomputer.com/news/linux/new-noisytcp-linux-kernel-flaw-lets-attackers-crash-servers/
  - https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html
  - https://www.helpnetsecurity.com/2026/11/16/geovision-camera-software-vulnerabilities/
  - https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/
  - https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/

### CVE-2026-123039 exploitation (VMware)
- Anchor signal: CVE-2026-123039
- Theme key: cve-2026-123039
- Cluster count: 4
- Article count: 5
- Cohesion: 0.233
- Shared strong signals: CVE-2026-123039
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, web_shell_backdoor, data_breach
  - affected_industries: government
  - affected_products: VMware
  - cve_ids: CVE-2026-123039, CVE-2026-109618, CVE-2026-109619
  - urgency_signals: no_patch_yet
- Cluster IDs: 2cab26404c, 6411ea2e82, 37e6854c04, ab668646b3
- Links:
  - https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
  - https://research.checkpoint.com/2026/16th-november-threat-intelligence-report/
  - https://www.securityweek.com/recent-unrealircd-vulnerability-exploited-in-attacks/
  - https://thehackernews.com/2026/11/attackers-exploit-unrealircd-flaw-that.html
  - https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html

### ransomware extortion targeting Android
- Anchor signal: Android
- Theme key: android
- Cluster count: 3
- Article count: 4
- Cohesion: 0.239
- Shared strong signals: Android
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, web_shell_backdoor
  - affected_industries: financial_services
  - affected_products: Android
- Cluster IDs: 877727aec7, 7cc91e5ade, 2cab26404c
- Links:
  - https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/
  - https://securelist.com/malware-report-q3-2026-mobile-statistics/121844/
  - https://www.darkreading.com/mobile-security/arcticrat-cybercrime-gang-profiles-victim-finances-ai
  - https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/

### Palo Alto Networks active exploitation
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 3
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, ransomware_extortion
  - affected_products: Palo Alto Networks
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: a1853faf68, 2cab26404c, e8815d20df
- Links:
  - https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html
  - https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
  - https://securelist.com/malware-report-q3-2026-pc-iot-statistics/121843/
  - https://isc.sans.edu/diary/rss/33518

### active exploitation targeting ScreenConnect
- Anchor signal: ScreenConnect
- Theme key: screenconnect
- Cluster count: 3
- Article count: 9
- Cohesion: 0.2
- Shared strong signals: ScreenConnect
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: ScreenConnect
- Cluster IDs: 865bc835a9, 6411ea2e82, 656ea1ba73
- Links:
  - https://www.huntress.com/blog/cve-2026-84869-screenconnect-technician-exploitation
  - https://www.sophos.com/en-us/blog/malicious-screenconnect-deployments-observed
  - https://thehackernews.com/2026/11/sckit-malware-targets-screenconnect.html
  - https://research.checkpoint.com/2026/16th-november-threat-intelligence-report/
  - https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/

### Linux kernel vulnerability activity
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 3
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Linux kernel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_industries: manufacturing_industrial
  - affected_products: Linux kernel
- Cluster IDs: eb92172155, fba6e81cad, d7028f613a
- Links:
  - https://tldrsec.com/p/tldr-sec-354
  - https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/
  - https://www.bleepingcomputer.com/news/linux/new-noisytcp-linux-kernel-flaw-lets-attackers-crash-servers/
  - https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html
  - https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html

### Apple iOS/macOS exploitation (CVE-2026-124194)
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 5
- Article count: 4
- Cohesion: 0.242
- Shared strong signals: Apple iOS/macOS
- Member CVEs: CVE-2026-124194
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, ransomware_extortion, data_breach
  - affected_products: Apple iOS/macOS
  - cve_ids: CVE-2026-124194, CVE-2026-125350
  - urgency_signals: actively_exploited
- Cluster IDs: e1f9a19221, 75a070b13c, e8815d20df, 6411ea2e82, ed2e51b312
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-november-2026
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-november-2026/
  - https://securelist.com/malware-report-q3-2026-pc-iot-statistics/121843/
  - https://isc.sans.edu/diary/rss/33518
  - https://research.checkpoint.com/2026/16th-november-threat-intelligence-report/
  - https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/

### Google Cloud vulnerability activity
- Anchor signal: Google Cloud
- Theme key: google-cloud
- Cluster count: 2
- Article count: 9
- Cohesion: 0.2
- Shared strong signals: Google Cloud
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Google Cloud
- Cluster IDs: f170b6e701, 188566384e
- Links:
  - https://orca.security/resources/research/cve-2026-119618-critical-apache-http-2-race-condition-enables-unauthenticated-remote-code-execution/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-119618/
  - https://webflow.sysdig.com/blog/httpd-cve-2026-119618-detecting-heap-corruption-and-rce-in-apache-http-server-mod-http2
  - https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability
  - https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html
  - https://cloud.google.com/blog/products/identity-security/inside-the-new-data-boundary-experience/
  - https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html

### active exploitation targeting Cisco
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 2
- Article count: 2
- Cohesion: 0.35
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Cisco
- Cluster IDs: 75a070b13c, 912dd8fe31
- Links:
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-november-2026/
  - https://blog.talosintelligence.com/artex-and-beyond/

### Citrix vulnerability activity
- Anchor signal: Citrix
- Theme key: citrix
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Citrix
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Citrix
  - urgency_signals: preauth_unauth
- Cluster IDs: a1853faf68, cb75cedcf6
- Links:
  - https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html
  - https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html

### Microsoft 365 vulnerability activity
- Anchor signal: Microsoft 365
- Theme key: microsoft-365
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Microsoft 365
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft 365
- Cluster IDs: 5fccd3b124, ed2e51b312
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/11/16/high-volume-phishing-campaign-uses-microsoft-365-outage-lures-target-multiple-industry-sectors-2/
  - https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/
  - https://www.securityweek.com/microsoft-rules-out-cyberattack-in-outage-warns-of-phishing-campaign/
  - https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/

### Ivanti vulnerability activity
- Anchor signal: Ivanti
- Theme key: ivanti
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Ivanti
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Ivanti
- Cluster IDs: 2cab26404c, ed2e51b312
- Links:
  - https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
  - https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (0)

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-90436 + Atlassian Confluence (cluster a162d593b3, first observation: True)
- Pair: CVE-2026-119618 + Anthropic/Claude (cluster f170b6e701, first observation: True)
- Pair: CVE-2026-119618 + GitHub (cluster f170b6e701, first observation: True)
- Pair: CVE-2026-119618 + Google Cloud (cluster f170b6e701, first observation: True)
- Pair: CVE-2026-84869 + OpenAI/ChatGPT (cluster 865bc835a9, first observation: True)
- Pair: CVE-2013-2165 + Citrix (cluster a1853faf68, first observation: True)
- Pair: CVE-2013-2165 + F5 BIG-IP (cluster a1853faf68, first observation: True)
- Pair: CVE-2013-2165 + Palo Alto Networks (cluster a1853faf68, first observation: True)
- Pair: CVE-2020-7961 + Citrix (cluster a1853faf68, first observation: True)
- Pair: CVE-2020-7961 + F5 BIG-IP (cluster a1853faf68, first observation: True)
- Pair: CVE-2020-7961 + Palo Alto Networks (cluster a1853faf68, first observation: True)
- Pair: CVE-2021-35464 + Citrix (cluster a1853faf68, first observation: True)
- Pair: CVE-2021-35464 + F5 BIG-IP (cluster a1853faf68, first observation: True)
- Pair: CVE-2021-35464 + Palo Alto Networks (cluster a1853faf68, first observation: True)
- Pair: CVE-2026-111793 + Citrix (cluster a1853faf68, first observation: True)

### Drift (2)
- **UNC5221** (cluster 2cab26404c)
  - New industries: (none)
  - New products: Android
  - Prior top industries: critical_infrastructure, financial_services, manufacturing_industrial
  - Prior top products: Citrix, Ivanti, Palo Alto Networks
- **Cl0p** (cluster d7028f613a)
  - New industries: telecommunications
  - New products: Linux kernel
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Anthropic/Claude, OpenAI/ChatGPT, SolarWinds

### Persistence (9)
- actor_attribution: Cl0p (weeks observed: 13, cluster d7028f613a)
- actor_attribution: UNC5221 (weeks observed: 9, cluster 2cab26404c)
- actor_attribution: LockBit (weeks observed: 8, cluster a46657a5b4)
- cve_ids: CVE-2026-15409 (weeks observed: 5, cluster e8815d20df)
- cve_ids: CVE-2026-109618 (weeks observed: 4, cluster 2cab26404c)
- cve_ids: CVE-2026-109619 (weeks observed: 4, cluster 2cab26404c)
- cve_ids: CVE-2026-15410 (weeks observed: 4, cluster e8815d20df)
- cve_ids: CVE-2026-84869 (weeks observed: 3, cluster 865bc835a9)
- cve_ids: CVE-2026-0257 (weeks observed: 3, cluster e8815d20df)

### Tier inversion (1)
- **PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE**
  - Cluster: 06bffa03c1
  - Primary source: The Hacker News
  - Strong signals: CVE-2026-116322, CVE-2026-6460

## Clusters

### Cluster a162d593b3 — score 64

- Title: Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-16T18:14:14+00:00
- Link: https://www.rapid7.com/blog/post/etr-rapid7-detected-exploitation-of-cve-2026-90436-against-atlassian-confluence-data-center-n-able-n-central-also-exploited
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Atlassian Confluence, CVE-2026-90436

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Atlassian Confluence
- cve_ids: CVE-2026-90436
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

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
Emergent Threat Response Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited Rapid7 Nov 16, 2026 | Last updated on Nov 16, 2026 | 4 min read Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited Table of contents Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited Table of contents Overview On November 6, 2026, the Apache Software Foundation disclosed CVE-2026-90436 , a critical unsafe reflection vulnerability ( CWE-470 ) in Axis 1.x that allows for unauthenticated remote code execution (RCE). Apache Axis is a Simple Object Access Protocol (SOAP) implementation used for the creation of Java Web services. CISA has assigned CVE-2026-90436 a CVSS score of 9.8 Critical . Since the initial November 6 disclosure, it has transpired that some versions of Atlassian Confluence Data Center and N-able N-central use the affected Axis library and are vulnerable to CVE-2026-90436. Both products require a non-default configuration in order to be vulnerable. CVE-2026-90436 is now being actively exploited in the wild against both known affected products. On November 13, 2026, Rapid7 MDR detected exploitation of CVE-2026-90436 against Atlassian Confluence Data Center in a customer environment. Separately, on November 13, 2026, N-able reported exploitation in the wild against N-central for a vulnerability that strongly correlates to CVE-2026-90436. A proof-of-concept exploit that leverages CVE-2026-90436 and targets N-central was published on November 12, 2026, as part of a series of public zero-day disclosures against N-central. Rapid7 recommends remediating exposed systems on an emergency basis outside of normal patching cycles. Mitigation guidance Prioritize internet-accessible instances with the relevant APIs enabled, and check internal deployments as well. Apply the product-specific actions below, then investigate systems that were exposed for evidence of compromise. Axis 1.x through 1.4 is affected but has reached end of life (EOL) and Apache does not plan to publish a fixed Axis 1.x release. Apache recommends moving to another SOAP engine (for example, Apache Axis 2) or using an Axis 1.x build with this patch applied. Organizations using products that are affected by this issue should follow the product vendor's specific remediation instructions. Atlassian Confluence Data Center Atlassian lists versions 1.x through to 9.x as affected when “Remote API (XML-RPC & SOAP)” is enabled. Version 9.2.28 is the fixed release. The setting has been off by default for new installations since version 3.0. Confluence version 10.x and later removed the feature so are not vulnerable, and Atlassian Cloud is unaffected. Affected users should upgrade to version 9.2.28 or a current unaffected 10.x release. If patching must wait, an administrator can open “General Configuration” and “Further Configuration”, edit the settings, clear “Remote API (XML-RPC & SOAP)”, and save. The change takes effect without restarting Confluence, but integrations using the API may stop working. Follow the Confluence advisory for the latest fixes and mitigation instructions. N-able N-central On-premises administrators should confirm that “Legacy API” is disabled, even on 2026.4 HF2. N-able states that it is off by default, and provides instructions for disabling Legacy API . Its November 13 guidance says hosted environments received temporary protections directly; customers in both hosting models must still follow the vendor's Agent and Probe upgrade guidance. N-able also temporarily disabled the Intune integration as a precaution. Refer to the N-able security update for these responsibilities. N-able says 2026.4 HF3 will permanently remove Legacy API access . Its November 16 rollout notice states that hosted upgrades have been completed, and on-premises general availability is bei
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 Detected Exploitation of CVE-2026-90436 against Atlassian Confluence Data Center, N-able N-central also Exploited
  - Published: 2026-11-16T18:14:14+00:00
  - Link: https://www.rapid7.com/blog/post/etr-rapid7-detected-exploitation-of-cve-2026-90436-against-atlassian-confluence-data-center-n-able-n-central-also-exploited
  - Summary: Overview On November 6, 2026, the Apache Software Foundation disclosed CVE-2026-90436 , a critical unsafe reflection vulnerability ( CWE-470 ) in Axis 1.x that allows for unauthenticated remote code execution (RCE). Apache Axis is a Simple Object Access Protocol (SOAP) implementation used for the creation of Java Web services. CISA has assigned CVE-2026-90436 a CVSS score of 9.8 Critical . Since the initial November 6 disclosure, it has transpired that some versions of Atlassian Confluence Data Center and N-able N-central use the affected Axis library and are vulnerable to CVE-2026-90436. Both products require a non-default configuration in order to be vulnerable. CVE-2026-90436 is now being actively exploited in the wild against both known affected products. On November 13, 2026, Rapid7 MDR detected exploitation of CVE-2026-90436 against Atlassian Confluence Data Center in a customer environment. Separately, on November 13, 2026, N-able reported exploitation in the wild against N-cent

### Cluster f170b6e701 — score 37

- Title: CVE-2026-119618: Critical Apache HTTP/2 Race Condition Enables Unauthenticated Remote Code Execution
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-11-16T17:49:55+00:00
- Link: https://orca.security/resources/research/cve-2026-119618-critical-apache-http-2-race-condition-enables-unauthenticated-remote-code-execution/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: CVE-2026-119618

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- affected_products: Anthropic/Claude, GitHub, Google Cloud
- cve_ids: CVE-2026-119618
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

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

#### Corroborating sources (5)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: CVE-2026-119618: Critical Apache HTTP/2 Race Condition Enables Unauthenticated Remote Code Execution
  - Published: 2026-11-16T17:49:55+00:00
  - Link: https://orca.security/resources/research/cve-2026-119618-critical-apache-http-2-race-condition-enables-unauthenticated-remote-code-execution/
  - Summary: A critical vulnerability in Apache HTTP Server’s mod_http2 module, tracked as CVE-2026-119618 (CVSS 9.8), allows attackers to achieve unauthenticated remote code execution on any server with HTTP/2 enabled. Because exploitation can lead to full server compromise without any authentication, immediate patching is required. The fix is Apache HTTP Server 2.4.71. CVE-2026-119618 at a glance CVE […]
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-119618 | Apache HTTP Server mod_http2 Race Condition Remote Code Execution Vulnerability
  - Published: 2026-11-12T20:17:28+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-119618/
  - Summary: CVE-2026-119618 is a critical race condition in Apache HTTP Server's mod_http2 that can lead to remote code execution without credentials. Fixed in 2.4.71. See affected versions, mitigations, and the NodeZero Rapid Response test.
- **Sysdig** (detection_response_operations)
  - Title: HTTPd (CVE-2026-119618): Detecting heap corruption and RCE in Apache HTTP Server mod_http2
  - Published: 2026-11-13T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/httpd-cve-2026-119618-detecting-heap-corruption-and-rce-in-apache-http-server-mod-http2
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Critical RCE Vulnerability in Apache HTTP Server: Everything You Need To Know
  - Published: 2026-11-11T19:49:10+00:00
  - Link: https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability
  - Summary: Detect and mitigate CVE-2026-119618, a critical RCE vulnerability in Apache HTTP Server. According to Wiz data, 64% of cloud environments have resources vulnerable to CVE-2026-119618. Immediate patching is advised.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely
  - Published: 2026-11-12T05:12:26+00:00
  - Link: https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html
  - Summary: A critical flaw in Apache HTTP Server's HTTP/2 module, mod_http2, can let a remote attacker run code on the server. Tracked as CVE-2026-119618, it affects versions 2.4.55 through 2.4.70 and is fixed in version 2.4.71, released yesterday. Only servers with HTTP/2 enabled are affected, according to Red Hat, which ships the server as part of Red Hat Enterprise Linux. An attacker who can reach the

### Cluster e1f9a19221 — score 36

- Title: Patch Tuesday - November 2026
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-10T21:55:37+00:00
- Link: https://www.rapid7.com/blog/post/em-patch-tuesday-november-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- cve_ids: CVE-2026-119952, CVE-2026-124194
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- cve_ids: CVE-2026-124194, CVE-2026-119952
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Microsoft is publishing 1,092 own-product vulnerabilities on November 2026 Patch Tuesday, including 745 vulnerabilities in Windows. Until a few months ago, these volumes would have been unimaginable, but if anything, this month feels like a slight reprieve. The jury is still out on whether patching many more vulnerabilities will lead to better security outcomes; every code change to resolve a known vulnerability could easily introduce new hidden treasure for researchers or threat actors to unearth in the future. Despite the vast uptick in volume during 2026, there has been no accompanying increase in the number of vulnerabilities known to be exploited in the wild. Microsoft is aware of exploitation in the wild for just one of the vulnerabilities published today, with no known public disclosure at all this month. Outlook: zero-day spoofing Imagine coming home and checking your mailbox to find a postcard. You admire the non-specific image of a tropical beach at sunset, and flip it over t
```

#### Full body

```
Patch Tuesday Patch Tuesday - November 2026 Adam Barnett Nov 10, 2026 | Last updated on Nov 12, 2026 | 179 min read Patch Tuesday - November 2026 Table of contents Patch Tuesday - November 2026 Table of contents Microsoft is publishing 1,092 own-product vulnerabilities on November 2026 Patch Tuesday, including 745 vulnerabilities in Windows. Until a few months ago, these volumes would have been unimaginable, but if anything, this month feels like a slight reprieve. The jury is still out on whether patching many more vulnerabilities will lead to better security outcomes; every code change to resolve a known vulnerability could easily introduce new hidden treasure for researchers or threat actors to unearth in the future. Despite the vast uptick in volume during 2026, there has been no accompanying increase in the number of vulnerabilities known to be exploited in the wild. Microsoft is aware of exploitation in the wild for just one of the vulnerabilities published today, with no known public disclosure at all this month. Outlook: zero-day spoofing Imagine coming home and checking your mailbox to find a postcard. You admire the non-specific image of a tropical beach at sunset, and flip it over to scan the handwriting on the back, which looks vaguely familiar. It’s addressed to you, but you can’t make out the signature, and the message is short and generic. Is that real handwriting, or has this been printed? Probably marketing material. You put the card in the recycling and, since life is busy, you move on and forget about it. Somehow, you remain entirely unaware that, immediately after reading the postcard, you took out your phone and sent high-resolution images of your front door key to a number you’ve never contacted before. Is this sketch just some rather questionable science fiction? Yes, hopefully, but what if that non-specific postcard was instead a malicious file in your Outlook inbox? Now we’re talking about CVE-2026-124194 , an exploited-in-the-wild spoofing vulnerability. Merely opening a specially crafted malicious file causes Outlook to silently connect to an attacker-controlled location and leak the user’s NTLM v2 hash. All supported versions of classic Outlook receive patches. The relatively low CVSS v3.1 base score of 6.5 does not tell the full story here, since this vulnerability provides value for both commodity attackers working to harvest initial access at scale, and also more targeted campaigns by more sophisticated threat actors. The NTLM v2 hash can be relayed live to impersonate the user against another service, at least where those services do not implement adequate safeguards such as message signing for SMB or LDAP , as well as Extended Protection for Authentication for Exchange or Active Directory Certificate Services . Alternatively, the NTLM v2 hash can be cracked offline by a motivated attacker to retrieve the underlying credential. The Preview Pane is not a vector, which will help limit the real-world impact somewhat. Windows Schannel: critical pre-auth RCE A pre-authentication remote code execution (RCE) vulnerability in Windows will always attract attention. CVE-2026-119952 allows an attacker to execute code on a target system by sending specially crafted malicious packets. Since the vulnerable component is Schannel, which is Microsoft’s implementation of Transport Layer Security (TLS) , attackers may not have to look very far to find vulnerable endpoints. The advisory provides some comfort by pointing out that specific conditions are required for exploitability, which reduces the likelihood of broad exploitation, but the advisory still assesses exploitation as more likely, so Microsoft presumably expects that the development of reliable exploit code is feasible. In many cases, there will be no need for an attacker to have an existing foothold on the same subnet. The execution context likely depends on the vulnerable service, which points to the evergreen need for least privilege architecture, but
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Patch Tuesday - November 2026
  - Published: 2026-11-10T21:55:37+00:00
  - Link: https://www.rapid7.com/blog/post/em-patch-tuesday-november-2026
  - Summary: Microsoft is publishing 1,092 own-product vulnerabilities on November 2026 Patch Tuesday, including 745 vulnerabilities in Windows. Until a few months ago, these volumes would have been unimaginable, but if anything, this month feels like a slight reprieve. The jury is still out on whether patching many more vulnerabilities will lead to better security outcomes; every code change to resolve a known vulnerability could easily introduce new hidden treasure for researchers or threat actors to unearth in the future. Despite the vast uptick in volume during 2026, there has been no accompanying increase in the number of vulnerabilities known to be exploited in the wild. Microsoft is aware of exploitation in the wild for just one of the vulnerabilities published today, with no known public disclosure at all this month. Outlook: zero-day spoofing Imagine coming home and checking your mailbox to find a postcard. You admire the non-specific image of a tropical beach at sunset, and flip it over t

### Cluster 581cf0398c — score 25

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

### Cluster c3ba4b41d5 — score 25

- Title: Exploit Attempts for GPUStack Authentication Bypass (CVE-2026-102895), (Thu, Nov 12th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-11-12T11:56:24+00:00
- Link: https://isc.sans.edu/diary/rss/33514
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-102895

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-102895
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Primary article taxonomy
- cve_ids: CVE-2026-102895
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Summary

```
CVE-2026-102895 is a trivial authentication-bypass vulnerability. GPUStack is also an attractive target. It is open-source software that manages clusters of GPUs, which are typically used to run AI workloads. All versions of GPUStack prior to 2.2.0, which was released at the end of June. This vulnerability was not made public until the end of July, and the CVE was assigned on November 4th.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Exploit Attempts for GPUStack Authentication Bypass (CVE-2026-102895), (Thu, Nov 12th)
  - Published: 2026-11-12T11:56:24+00:00
  - Link: https://isc.sans.edu/diary/rss/33514
  - Summary: CVE-2026-102895 is a trivial authentication-bypass vulnerability. GPUStack is also an attractive target. It is open-source software that manages clusters of GPUs, which are typically used to run AI workloads. All versions of GPUStack prior to 2.2.0, which was released at the end of June. This vulnerability was not made public until the end of July, and the CVE was assigned on November 4th.

### Cluster 26581d7b17 — score 24

- Title: Trained to betray: How post-training supply chain attacks hijack coding agents
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-11-12T17:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Microsoft Defender

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, supply_chain, web_shell_backdoor
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, ai_security, web_shell_backdoor
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Defender Research and the AI Red Team discuss how poisoned datasets and poisoned model checkpoints can trigger remote code execution and other malicious activities. The post Trained to betray: How post-training supply chain attacks hijack coding agents appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Supply chain attack Threats intelligence AI threats Supply chain attacks Content types Research Products and services Microsoft Defender Topics Actionable threat insights AI and agents Threat intelligence As organizations increasingly deploy specialized AI agents, trust cannot depend solely on a model behaving as expected during evaluation or normal use. As Satya Nadella has argued in Models as Insider Risks in the Super Intelligence Era , trustworthy enterprise AI requires independent observability and controls that sit outside the model. Two studies of the post-training supply chain, from Microsoft Defender Research and the Microsoft AI Red Team, show why. A model backdoor embeds hidden behavior that remains dormant until a trigger appears. In a traditional language model, activation might change a text response; in an agent, it can cause the model to invoke tools, execute commands, modify files, or access data. The two studies examine attacks with different levels of access. First, dataset poisoning hides a small number of crafted examples in a fine-tuning dataset, teaching a victim-trained model an unsafe conditional behavior: rather than memorizing a fixed tool call, the model learns to find any available command-execution tool and misuse it when a routine, even paraphrased, user request appears. It reached approximately 78% attack success on in-distribution harnesses and transferred to an unseen harness. Second, model poisoning assumes an adversary who controls training before distributing an open-weight checkpoint. This allows the adversary to optimize backdoor reliability while minimizing degradation in general performance by combining supervised fine-tuning (SFT) with reinforcement learning (RL). In this setting, average success on unseen repositories reached 84.1% to 94.8%, with additional transfer across coding harnesses. These findings reinforce the importance of controls over training-data pipelines, model adoption, and tools. Introduction Coding and terminal agents do more than generate text. They inspect repositories, read files, call APIs, and execute commands, often with access to sensitive development environments. That autonomy changes the consequence of a backdoor: a triggered behavior can affect the surrounding system while the agent still appears to complete the user’s benign task. The trigger itself may not look malicious. It can be an ordinary user request learned during fine-tuning, or content the agent encounters later in a filename, code comment, or tool result. Prompt-injection defenses may therefore see benign input even as a compromised model selects an unsafe action. Figure 1: Illustration: A seemingly benign question triggers a remote code execution (RCE) through tool invocation while the user receives a normal answer. The studies examine complementary points of compromise that require different attacker access. Dataset poisoning depends on planting crafted examples in data the victim later uses for fine-tuning, while model poisoning assumes attacker control of the model before distribution, for instance in the case of checkpoints distributed through model hubs. The strategies differ in their advantages and limitations. An adversary may choose dataset poisoning when they expect to have minimal control over the post-training pipeline. Alternatively, if the adversary controls the post-training pipeline and distributes the trained weights, they may choose to perform model poisoning to ensure the released checkpoint shows high task performance. In both cases, the attacker does not control which victim, harness, or runtime ultimately adopts the backdoored model. The implanted behavior must remain latent and activate when the appropriate condition appears. Both attacks exploit trust in post-training artifacts. Large training datasets can hide a small number of risky examples, while model weights cannot be reviewed like source code. Once a model is connected to tool
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Trained to betray: How post-training supply chain attacks hijack coding agents
  - Published: 2026-11-12T17:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/
  - Summary: Microsoft Defender Research and the AI Red Team discuss how poisoned datasets and poisoned model checkpoints can trigger remote code execution and other malicious activities. The post Trained to betray: How post-training supply chain attacks hijack coding agents appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Trained to betray: How post-training supply chain attacks hijack coding agents
  - Published: 2026-11-12T17:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/
  - Summary: Microsoft Defender Research and the AI Red Team discuss how poisoned datasets and poisoned model checkpoints can trigger remote code execution and other malicious activities. The post Trained to betray: How post-training supply chain attacks hijack coding agents appeared first on Microsoft Security Blog .

### Cluster ff829a216f — score 24

- Title: Hackers Exploit Critical Xen Orchestra Auth Bypass Flaw to Gain Admin Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-10T18:12:21+00:00
- Link: https://thehackernews.com/2026/11/hackers-exploit-critical-xen-orchestra.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
French software company Vates VMS has warned of a critical security vulnerability in Xen Orchestra that it said is being actively exploited in the wild. The authentication bypass flaw, which does not yet have a CVE identifier, is tracked as VSA-2026-062. "REST cookie parsing turns authenticationToken=j:%7B%7D into {}," Vates VMS said in an alert. "REST authentication passes that object to the
```

#### Full body

```
Hackers Exploit Critical Xen Orchestra Auth Bypass Flaw to Gain Admin Access  Ravie Lakshmanan  Nov 10, 2026 Vulnerability / Cyber Attack French software company Vates VMS has warned of a critical security vulnerability in Xen Orchestra that it said is being actively exploited in the wild. The authentication bypass flaw, which does not yet have a CVE identifier, is tracked as VSA-2026-062 . "REST cookie parsing turns authenticationToken=j:%7B%7D into {}," Vates VMS said in an alert. "REST authentication passes that object to the XO token provider without requiring a string." "The token collection treats {} as an unfiltered lookup and returns its first token; the provider authenticates as that token's owner if it is unexpired. The authenticated /rest/v0/users/me/authentication_tokens route then returns reusable login token IDs." In other words, the vulnerability can allow an attacker to bypass authentication by sending a specially crafted cookie and perform arbitrary actions with "Admin" privileges, ultimately resulting in arbitrary code execution on managed pools and a full XCP-ng node takeover as root. Vates VMS said it's seeing the vulnerability being actively exploited by a threat actor from the following IP address and TOR domain - 91.211.251[.]112:8001 , which has been flagged as a RedLine Stealer command-and-control (C2) server on VirusTotal ustar3rqxgnskzgnwkgpofgtvxevm6cx3lxdbwt4mndtveqyaohid[.]onion:3333 It's unclear when the activity started and if the vulnerability was exploited as a zero-day. Other indicators of compromise are listed below - HTTP requests containing authenticationToken=j:%7B%7D or authenticationToken=j:{} A running virtual machine named pivot2 Virtual machines configured using "hvm_serial: file" parameter Suspicious files named /etc/cron.d/zz-ustar2, /etc/cron.d/zz-ustar, /.ustar5, and /.ustar6 The issue has been addressed in Xen Orchestra 6.9.1 and 6.10.0 for the stable and latest channels, as well as xo-server versions 5.211.2 and 5.213.1. If immediate patching is not an option, the following mitigations are advised - Avoid exposing Xen Orchestra instances on the internet Block the IP address and domain associated with malicious activity Block the empty token in a web application firewall (WAF) or a reverse proxy Rotate all passwords and secrets in Vates VMS if indicators of compromise are detected Filip Magic (@mad31k) and Christoffer Olsen from TDC NET Security have been credited with discovering and reporting the flaw. Update Vates VMS has disclosed in a separate advisory that the vulnerability is being exploited in conjunction with a second flaw tracked as VSA-2026-063. Successful exploitation of the flaw could allow an unprivileged user to import a malicious VM (i.e., an XVA file) using a crafted keys parameter and compromise an XCP-ng host. "Xen Orchestra sends requests as pool-admin to XAPI, the pool-admin role is fully privileged and allow to configure various aspects of the system and forwards the stream to XAPI without reading or modifying ova.xml," the company said . "An unprivileged user with vm.import (JSON-RPC), sr/import:vm (REST API), network/action:create or network/action:update privilege can import a raw XVA with crafted following keys as demonstrated in XSA-489 and XSA-530: VBD.other_config:backend-local, VM.other-config:is_system_domain, [and] VM.platform:hvm_serial." The shortcoming affects Xen Orchestra Appliance and Xen Orchestra versions 6.10.1 and before. A fix for the vulnerability is currently in the works. As temporary mitigations, it's recommended to restrict authorized VM import only to the Admin user, and disable any users which have been configured with the below privileges - vm.import sr/import:vm network/action:create network/action:update "This path has been abused by a threat actor operating initially from 91.211.251[.]112:8001 and ustar3rqxgnskzgnwkgpofgtvxevm6cx3lxdbwt4mndtveqyaohid[.]onion:3333 (via TOR) using Admin privilege (VSA-2026-062)," Vates VMS sa
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hackers Exploit Critical Xen Orchestra Auth Bypass Flaw to Gain Admin Access
  - Published: 2026-11-10T18:12:21+00:00
  - Link: https://thehackernews.com/2026/11/hackers-exploit-critical-xen-orchestra.html
  - Summary: French software company Vates VMS has warned of a critical security vulnerability in Xen Orchestra that it said is being actively exploited in the wild. The authentication bypass flaw, which does not yet have a CVE identifier, is tracked as VSA-2026-062. "REST cookie parsing turns authenticationToken=j:%7B%7D into {}," Vates VMS said in an alert. "REST authentication passes that object to the

### Cluster b2f367d9d1 — score 23

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

### Cluster 920bb59e09 — score 22

- Title: AI Is Both Target and Tool for Threat Actors
- Source: Recorded Future (threat_research_primary)
- Published: 2026-11-11T00:00:00+00:00
- Link: https://www.recordedfuture.com/research/ai-cyber-threat-trends-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, credential_theft, phishing_social_eng, ransomware_extortion, supply_chain
- affected_industries: government
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, credential_theft, apt_espionage, active_exploitation
- affected_industries: government
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Discover 2026 trends in AI-enabled cyber threats, supply-chain vulnerabilities, state-sponsored agentic attacks, and key mitigations.
```

#### Full body

```
AI Is Both Target and Tool for Threat Actors Summary Artificial intelligence (AI)-enabled attacks are accelerating, with AI as both a target and a force multiplier. Of the 103 AI-enabled incidents analyzed for this report, most involve AI accelerating familiar attack types (supply-chain compromise, phishing, extortion) and making them more convincing. The use of AI is evident throughout the attack lifecycle, though full automation remains rare. Note: The period of analysis for this report is between July 31, 2025 and July 31, 2026. Developer tools are a prime target. Because AI coding assistants and proxy packages often have privileged access to credentials and code, threat actors use them as footholds for mass credential theft and lateral movement across downstream environments. State-sponsored actors are beginning to experiment with agentic capabilities. Most of the state-sponsored activity in this report falls within Recorded Future’s AI Malware Maturity Model Level 2–3 (AI-assisted malware development), with one notable exception: a campaign against Taiwanese government entities that employed up to eight AI agents with limited human intervention. Fully autonomous attacks remain rare, likely for both maturity and operational-risk reasons. Human oversight still appears necessary for reliable outcomes, which may limit the full automation of cyberattacks, especially in sensitive operations where an agent's error can have outsized consequences. This restraint is unlikely to hold. As agentic techniques mature and diffuse across the threat landscape, autonomous and orchestrated campaigns are likely to become more frequent, alongside a growing underground market for illicit access to commercial models and rising "noise" from low-level automated intrusions that complicate the detection of serious threats. Figure 1: Five trends in offensive use of AI (Source: Recorded Future) Analysis The Data Offensive use of AI remains a serious concern for cyber defenders, especially as recent advances in AI capabilities are increasing the risk of autonomous attacks. To better understand the risk, Insikt Group identified 103 incidents between July 31, 2025, and July 31, 2026, in which AI was part of a malicious campaign. To qualify, events had to be: Documented incidents that are searchable in the Recorded Future intelligence graph Confirmed as using AI as the attack vector, tool, or target Carried out by malicious actors in the wild, not as proofs-of-concept or security research Of the 103 incidents identified, 32 involved the use of AI in malware or to orchestrate offensive cyber operations. These incidents were categorized along Recorded Future’s AI Malware Maturity Model (AIM3) , which evaluates how AI is used in malicious or offensive software. The remaining 71 incidents were sorted into one of four categories that best describe how AI was abused: Targeting AI systems, infrastructure, or data: Attacks where AI platforms, tools, or companies are the direct target rather than a means of attack AI as lure or delivery vector: Social engineering that uses AI's current hype and popularity as bait to deliver malware, rather than exploiting anything technical about AI itself AI-assisted deception, fraud, or influence: AI used as a tool by the attacker to make fraud, phishing, or influence operations more convincing and personalized to the target audience Abuse or hijacking of AI agents/services: Misuse of legitimate AI systems' own capabilities, rather than a single dominant technique Figures 2 and 3: AI-related attacks documented by Insikt Group from July 2025 to July 2026 (Source: Recorded Future) Roughly one-third of the incidents across both datasets are financially motivated. Espionage cases are concentrated in the AIM3 dataset, with 9 of the 32 incidents attributed to state-sponsored intelligence collection. In one notable case, the threat actor was an AI agent that carried out an attack in order to pass a security benchmark. The remaining 23
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: AI Is Both Target and Tool for Threat Actors
  - Published: 2026-11-11T00:00:00+00:00
  - Link: https://www.recordedfuture.com/research/ai-cyber-threat-trends-2026
  - Summary: Discover 2026 trends in AI-enabled cyber threats, supply-chain vulnerabilities, state-sponsored agentic attacks, and key mitigations.

### Cluster 927a1ad310 — score 21

- Title: Critical vulnerabilities in N-able N-central prompt hosted shutdown
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-10T14:20:34+00:00
- Link: https://www.rapid7.com/blog/post/etr-critical-vulnerabilities-in-n-able-n-central-prompt-hosted-shutdown
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-125878, CVE-2026-125879, CVE-2026-125880, CVE-2026-125881, CVE-2026-125883
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-125883, CVE-2026-125878, CVE-2026-125879, CVE-2026-125880, CVE-2026-125881
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On November 9, 2026, N-able announced that it was responding to the public disclosure of critical vulnerabilities affecting N-central , its remote monitoring and management (RMM) platform. In a public disclosure titled Able2Shell, an independent researcher has published details and proof-of-concept (PoC) code covering 33 issues. According to the disclosure, the issues include unauthenticated remote code execution (RCE), privilege escalation to root, credential disclosure, and unauthorized account creation. One unauthenticated chain combines XML external entity (XXE) and session-handling weaknesses to execute code as the nable service account. Other demonstrated chains involve an administrator viewing malicious patch metadata or use ProductAdmin credentials. Rapid7 Intelligence is currently triaging the newly published details. Before the hotfix release on November 10, N-able reported scanning activity associated with the published PoC code and said it had no evidence that any
```

#### Full body

```
Emergent Threat Response Critical vulnerabilities in N-able N-central prompt hosted shutdown Rapid7 Nov 10, 2026 | Last updated on Nov 11, 2026 | 4 min read Critical vulnerabilities in N-able N-central prompt hosted shutdown Table of contents Critical vulnerabilities in N-able N-central prompt hosted shutdown Table of contents Overview On November 9, 2026, N-able announced that it was responding to the public disclosure of critical vulnerabilities affecting N-central , its remote monitoring and management (RMM) platform. In a public disclosure titled Able2Shell, an independent researcher has published details and proof-of-concept (PoC) code covering 33 issues. According to the disclosure, the issues include unauthenticated remote code execution (RCE), privilege escalation to root, credential disclosure, and unauthorized account creation. One unauthenticated chain combines XML external entity (XXE) and session-handling weaknesses to execute code as the nable service account. Other demonstrated chains involve an administrator viewing malicious patch metadata or use ProductAdmin credentials. Rapid7 Intelligence is currently triaging the newly published details. Before the hotfix release on November 10, N-able reported scanning activity associated with the published PoC code and said it had no evidence that any customer environment had been successfully exploited. The vendor advised keeping N-central deployments offline while it developed and validated a hotfix. Hosted N-central classic environments were offline, according to the same notice. That notice did not yet include CVE identifiers or CVSS scores. N-central is used by managed service providers (MSPs) and enterprise IT teams to administer endpoints and infrastructure. Compromise of an RMM server can put downstream managed environments at risk. N-central has previously been targeted through separate vulnerabilities, including an authentication bypass covered by Rapid7 in August 2026 . Given the platform's administrative reach and the availability of public exploit code, Rapid7 recommends treating the current disclosure as an emergency. Update #1: On November 10, 2026, N-able released N-central 2026.4 Hotfix 2 (build 2026.4.1.26 ), addressing seven CVEs. The vendor plans a follow-up hotfix with further security updates. On November 11, N-able confirmed that hosted N-central servers across all regions had been successfully upgraded. Mitigation guidance Rapid7 strongly recommends that organizations operating on-premises N-central servers upgrade to N-central 2026.4 Hotfix 2 (build 2026.4.1.26 ) on an emergency basis outside of normal patching cycles, and keep servers offline until successfully upgraded. Hosted servers are upgraded by N-able. Customers in both hosted and on-premises environments must also upgrade their Agents and Probes. To maintain communication, upgrade Agents first, then Probes, following the vendor's compatibility guidance for the Patch Management Engine (PME). Affected versions: The researcher reports testing N-central Appliance 2026.4.0.31 . N-able's current notice does not specify the full affected-version range. Fixed versions: N-central 2026.4 Hotfix 2 (build 2026.4.1.26 ) addresses the seven CVEs listed below. According to N-able's release notes , the hotfix addresses: CVE Description CVE-2026-125883 Multiple XXE vulnerabilities CVE-2026-125878 Multiple OGNL injection vulnerabilities CVE-2026-125879 Local privilege escalation to root through nable -writable syslog-ng configuration CVE-2026-125880 Stored XSS through MMS3 patch metadata in an administrator context CVE-2026-125881 Schema-hint SSRF through service-import schema validation CVE-2026-125882 RCE through file-repository upload path traversal; credited to Nate Fair, Sprocket Security CVE-2026-91000 Local privilege escalation through insecure IPC channels Further security updates are planned in a follow-up hotfix. Organizations should monitor the vendor's guidance and apply subsequent fixes as th
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Critical vulnerabilities in N-able N-central prompt hosted shutdown
  - Published: 2026-11-10T14:20:34+00:00
  - Link: https://www.rapid7.com/blog/post/etr-critical-vulnerabilities-in-n-able-n-central-prompt-hosted-shutdown
  - Summary: Overview On November 9, 2026, N-able announced that it was responding to the public disclosure of critical vulnerabilities affecting N-central , its remote monitoring and management (RMM) platform. In a public disclosure titled Able2Shell, an independent researcher has published details and proof-of-concept (PoC) code covering 33 issues. According to the disclosure, the issues include unauthenticated remote code execution (RCE), privilege escalation to root, credential disclosure, and unauthorized account creation. One unauthenticated chain combines XML external entity (XXE) and session-handling weaknesses to execute code as the nable service account. Other demonstrated chains involve an administrator viewing malicious patch metadata or use ProductAdmin credentials. Rapid7 Intelligence is currently triaging the newly published details. Before the hotfix release on November 10, N-able reported scanning activity associated with the published PoC code and said it had no evidence that any

### Cluster a3d4fba69b — score 20

- Title: CVE-2026-118383: Use-after-free vulnerability in MongoDB
- Source: Datadog Security Labs (cloud_identity_infrastructure)
- Published: 2026-11-11T00:00:00+00:00
- Link: https://securitylabs.datadoghq.com/articles/cve-2026-118383-mongodb-server-use-after-free/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-118383

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-118383
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-118383
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
We reproduced CVE-2026-118383, a critical use-after-free in MongoDB Server's primary catch-up process that unauthenticated clients can set up, and explain how to detect and remediate it.
```

#### Full body

```
Sebastian Obregoso Senior Security Researcher Eslam Salem Manager, Security Research Nick Frichette Staff Security Researcher Greg Foss Manager, Threat Detection & Research Julie Agnes Sparks Senior Security Engineer Key points and observations CVE-2026-118383 is a critical use-after-free in MongoDB Server's primary catch-up process, with a CVSS v4.0 score of 9.5. It affects replica set members, including those used by shards and config servers. Standalone mongod instances are unaffected. Remote unauthenticated exploitation is possible, but only during a specific window that the attacker does not have visibility into. We reproduced a crash (segmentation fault) on MongoDB Server 8.0.34. An unauthenticated client can set up the crash with two ping requests, because vulnerable servers accept ping before login. Turning on authentication does not prevent this. Upgrade every affected replica set member to a fixed release. Restricting network access can reduce exposure while you upgrade. What happened MongoDB announced a security update on November 10 . The company said it found the vulnerability internally and was not aware of exploitation attempts at the time of its announcement. The advisory describes a use-after-free when a newly elected replica set primary completes catch-up. During catch-up, the member applies operations it missed before accepting writes as primary. The vulnerability affects ordinary replica set members. It also affects the replica set members used by shards and config servers in sharded clusters. A standalone mongod does not perform replica set primary catch-up and is not affected by this vulnerability. The advisory rates the issue Critical and says the server may terminate unexpectedly or, under certain conditions, execute arbitrary code in the server process. How to know if you are affected The issue affects replica set members, including shard and config server replica set members in sharded clusters. Standalone mongod instances are not affected. The MongoDB fix releases are: MongoDB Server branch First fixed release 9.0 9.0.7 8.3 8.3.16 8.0 8.0.37 7.0 7.0.48 6.0 6.0.30 5.0 5.0.35 4.4 4.4.32 Upgrade to the fixed release for your branch, or use a distributor package that includes the fix. Verify the version running on every member after the upgrade, including members in containers and any members that were offline during maintenance. MongoDB says Atlas clusters are upgraded automatically during maintenance. It urges customers who defer maintenance to apply the upgrade promptly. Until you can upgrade, restrict network access to MongoDB to the specific systems that need access to it. This limits who can send the unauthenticated requests, but it does not fix the use-after-free. Exploitation window and likelihood When a replica set member wins an election, it first catches up on writes it missed, then starts accepting new ones. The bug is in the cleanup at the end of that catch-up step. Before any election happens, an attacker can leave two stale âwaitersâ on a member. A waiter is a pending notification MongoDB creates when a request asks to wait until replication reaches a certain point. Planting them does not crash the server by itself. The diagram below traces an election timeline and marks where the crash fires. Plant during steady state : The attacker sends two unauthenticated ping requests that include a readConcern.afterOpTime value to a reachable, vulnerable replica set member. The waiters don't expire. They stay in place until the member restarts, rolls back, or steps down from primary. Reach catch-up : Later, the same member has to win an election while it is behind another member. The attacker can't cause the lag or the election. Both have to happen on their own, for example during maintenance or an outage. Crash when catch-up ends : When catch-up finishes, the new primary runs its cleanup twice, uses memory it has already freed, and crashes before it accepts any writes. Once the first two steps a
```

#### Corroborating sources (2)

- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: CVE-2026-118383: Use-after-free vulnerability in MongoDB
  - Published: 2026-11-11T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/cve-2026-118383-mongodb-server-use-after-free/
  - Summary: We reproduced CVE-2026-118383, a critical use-after-free in MongoDB Server's primary catch-up process that unauthenticated clients can set up, and explain how to detect and remediate it.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Pre-Auth MongoDB Flaw (CVE-2026-118383) Can Crash Lagging Servers on Failover
  - Published: 2026-11-12T09:25:00+00:00
  - Link: https://thehackernews.com/2026/11/critical-pre-auth-mongodb-flaw-cve-2026.html
  - Summary: A critical flaw in MongoDB Server allows an unauthenticated attacker to send two requests that trigger a crash on the database server. The crash occurs only if that server is later chosen to take over as the main server while it still lacks some recent changes. MongoDB, the company that makes the database, released fixed versions earlier this week. The affected servers are members of a replica

### Cluster 865bc835a9 — score 20

- Title: CVE-2026-84869 in ScreenConnect Exploited to Run Malicious Files on MSP Technician Accounts
- Source: Huntress (detection_response_operations)
- Published: 2026-11-16T18:00:00+00:00
- Link: https://www.huntress.com/blog/cve-2026-84869-screenconnect-technician-exploitation
- Fetch status: ok
- Member count: 6
- Corroborating source count: 3
- Strong signals: CVE-2026-84869, ScreenConnect

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: financial_services
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, ScreenConnect
- cve_ids: CVE-2026-84869
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

#### Corroborating sources (3)

- **Huntress** (detection_response_operations)
  - Title: CVE-2026-84869 in ScreenConnect Exploited to Run Malicious Files on MSP Technician Accounts
  - Published: 2026-11-16T18:00:00+00:00
  - Link: https://www.huntress.com/blog/cve-2026-84869-screenconnect-technician-exploitation
  - Summary: Huntress confirmed CVE-2026-84869 exploitation against MSP technicians via ScreenConnect. See the attack chain, IOCs, and how to protect your team.
- **Sophos X-Ops** (detection_response_operations)
  - Title: Malicious ScreenConnect deployments observed
  - Published: 2026-11-11T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/malicious-screenconnect-deployments-observed
  - Summary: Categories: Threat Research Tags: advisory, connectwise, ScreenConnect
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SCKit Malware Turns ScreenConnect Support Sessions Into Potential MSP Attack Paths
  - Published: 2026-11-12T13:08:28+00:00
  - Link: https://thehackernews.com/2026/11/sckit-malware-targets-screenconnect.html
  - Summary: The ongoing campaign targeting ConnectWise ScreenConnect deployments involves the exploitation of a now-patched critical security flaw in the remote access software, and not a new vulnerability, it has emerged. Blackpoint Cyber's Adversary Pursuit Group (APG), which shared the details with The Hacker News, said the recovered attacker toolkit exploits CVE-2026-84869 (CVSS score: 9.9), an

### Cluster 8213947947 — score 19

- Title: November Patch Tuesday: An Overflowing Cornucopia of CVEs
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-11-10T22:26:51+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/november-patch-tuesday-cornucopia-cves
- Fetch status: fetch_failed:HTTPError
- Member count: 2
- Corroborating source count: 2
- Strong signals: Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Microsoft SharePoint
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: Microsoft SharePoint
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Microsoft serves up an actively exploited Outlook zero-day, and a wave of critical Exchange, SharePoint, Windows Search, and LDAP bugs that exhausted defenders need to prioritize fast.
```

#### Corroborating sources (2)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: November Patch Tuesday: An Overflowing Cornucopia of CVEs
  - Published: 2026-11-10T22:26:51+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/november-patch-tuesday-cornucopia-cves
  - Summary: Microsoft serves up an actively exploited Outlook zero-day, and a wave of critical Exchange, SharePoint, Windows Search, and LDAP bugs that exhausted defenders need to prioritize fast.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Patches 1,259 Flaws, Including Exploited Outlook Bug That May Expose NTLMv2 Hashes
  - Published: 2026-11-11T08:17:53+00:00
  - Link: https://thehackernews.com/2026/11/microsoft-patches-1259-flaws-including.html
  - Summary: Microsoft on Tuesday released patches for a total of 1,259 vulnerabilities spanning its software portfolio, the second consecutive month where the patch volume has exceeded 1,000 flaws. These cover 726 flaws in Windows, 174 in Office, 61 in Developer Tools, 59 in SQL Server, 53 in Developer Tools, and 27 in SharePoint Server. The patches also include 165 non-Microsoft-issued CVE identifiers.

### Cluster a1853faf68 — score 18

- Title: Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-11T06:04:02+00:00
- Link: https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-20320

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: telecommunications
- affected_products: Citrix, F5 BIG-IP, Palo Alto Networks
- cve_ids: CVE-2013-2165, CVE-2020-7961, CVE-2021-35464, CVE-2026-111793, CVE-2026-20320
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: telecommunications
- affected_products: Palo Alto Networks, F5 BIG-IP, Citrix
- cve_ids: CVE-2026-20320, CVE-2026-111793, CVE-2013-2165, CVE-2020-7961, CVE-2021-35464
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) Tuesday added two security flaws impacting Cisco BroadWorks and Openwave Messaging Webtop Media Transcoder to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. Details of the vulnerabilities are below - CVE-2026-20320 (CVSS score: 7.5) - An improper restriction of XML external entity
```

#### Full body

```
Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches  Ravie Lakshmanan  Nov 11, 2026 Vulnerability / Enterprise Security The U.S. Cybersecurity and Infrastructure Security Agency (CISA) Tuesday added two security flaws impacting Cisco BroadWorks and Openwave Messaging Webtop Media Transcoder to its Known Exploited Vulnerabilities ( KEV ) catalog, citing evidence of active exploitation. Details of the vulnerabilities are below - CVE-2026-20320 (CVSS score: 7.5) - An improper restriction of XML external entity reference vulnerability in the Open Client Interface (OCI) XML Parser of Cisco BroadWorks that could allow an unauthenticated, remote attacker to read sensitive configuration information on an affected system with the privileges of the Cisco BroadWorks user. (Fixed in August 2026) CVE-2026-111793 (CVSS score: 4.3) - An incorrect resource transfer between spheres vulnerability in Openwave Messaging Webtop Media Transcoder that could allow an authenticated user to process and convert unintended document types if bypassing the Webmail experience. (Fixed in October 2026) The addition of CVE-2026-111793 to the KEV catalog follows an alert issued by Japan Vulnerability Notes (JPN), which noted in an advisory that the "developer states that attacks exploiting the vulnerability have been observed." The vulnerability information portal also warned that an authenticated attacker could exploit the vulnerability to upload a specially crafted file and obtain sensitive information. As for CVE-2026-20320, the security defect has been put to use as part of an agentic attack campaign dubbed Operation Snowball in which an unknown Chinese-speaking threat actor leveraged an autonomous framework built using a jailbroken version of the DeepSeek Flash model to target a European telecom provider and 13 companies hosted on its infrastructure. The activity resulted in the enumeration of hundreds of assets, extraction of dozens of credential sets, and exfiltration of thousands of rows of subscriber billing and device records from the provider's internal billing platform over a two-week period, according to Malbear Labs. The AI agent has capabilities to exploit a portfolio of known security vulnerabilities spanning a wide range of products, including - JBoss RichFaces ( CVE-2013-2165 ) Liferay CE/DXP ( CVE-2020-7961 ) ForgeRock OpenAM ( CVE-2021-35464 ) Linux ( CVE-2021-4034 ) SAP NetWeaver ( CVE-2022-22536 ) Cisco Expressway ( CVE-2023-20269 ) Citrix NetScaler( CVE-2023-4966 ) Qlik Sense ( CVE-2023-41265 , CVE-2023-41266 ) PAN-OS GlobalProtect ( CVE-2024-3400 , CVE-2024-9474 ) Adobe Experience Manager ( CVE-2025-54249 ) Broadcom VMware Cloud Director ( CVE-2026-2003 , CVE-2026-2004 , CVE-2026-2005 , CVE-2026-2006 ) Claris FileMaker Server ( CVE-2026-86934 ), and F5 BIG-IP ( CVE-2026-41225 ) "The primary target on the telecommunications provider's infrastructure was the BroadWorks XSP (eXtended Services Platform), Release 23.0.1.1075, running on port 2208," Malbear Labs said . "The agent exploited CVE-2026-20320, an unauthenticated XXE in the BroadWorks OCI XML parser." "From the XSP host, the agent recovered the system identity private key, three SSL credential sets, and three additional private keys with certificate matches confirmed. The system identity key is used by the BroadWorks platform to authenticate between its own components; possessing it allows impersonation of the XSP in inter-component communication." The activity has also been characterized by the use of reconnaissance tools, Sliver for post-exploitation, Chisel, along with web shells like Behinder for persistent access. "This is a threat actor who delegated the intrusion to an AI and checked in asynchronously to review progress," Malbear Labs added. The primary agent ran continuously, issued parallel tasks to worker agents, maintained a coherent operational plan across the full campaign, and adapted to defensive controls without pausing for operator inp
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches
  - Published: 2026-11-11T06:04:02+00:00
  - Link: https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) Tuesday added two security flaws impacting Cisco BroadWorks and Openwave Messaging Webtop Media Transcoder to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. Details of the vulnerabilities are below - CVE-2026-20320 (CVSS score: 7.5) - An improper restriction of XML external entity

### Cluster 5fccd3b124 — score 18

- Title: High volume phishing campaign uses Microsoft 365 outage lures to target multiple industry sectors
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-11-17T00:08:41+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/11/16/high-volume-phishing-campaign-uses-microsoft-365-outage-lures-target-multiple-industry-sectors-2/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: Microsoft 365

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, supply_chain
- affected_products: Microsoft 365, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

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

#### Corroborating sources (4)

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
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: FBI warns ARTEX AI hacking tool is powering global cyberattacks
  - Published: 2026-11-15T18:29:53+00:00
  - Link: https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/
  - Summary: The FBI is warning that hackers are using an AI-powered penetration testing framework called ARTEX to automate cyberattacks against organizations worldwide, including a recent ConnectWise supply-chain breach that compromised Microsoft 365 customer environments. [...]
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Microsoft Rules Out Cyberattack in Outage, Warns of Phishing Campaign
  - Published: 2026-11-16T08:15:12+00:00
  - Link: https://www.securityweek.com/microsoft-rules-out-cyberattack-in-outage-warns-of-phishing-campaign/
  - Summary: Phishing emails posing as Microsoft 365 service notices referenced the real outage incident and threatened to delete held messages. The post Microsoft Rules Out Cyberattack in Outage, Warns of Phishing Campaign appeared first on SecurityWeek .

### Cluster 75a070b13c — score 17

- Title: Microsoft Patch Tuesday for November 2026 — Snort rules and prominent vulnerabilities
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-11-11T01:41:17+00:00
- Link: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-november-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Cisco
- cve_ids: CVE-2026-113862, CVE-2026-118146, CVE-2026-118148, CVE-2026-118207, CVE-2026-124194
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Cisco
- cve_ids: CVE-2026-124194, CVE-2026-113862, CVE-2026-118146, CVE-2026-118148, CVE-2026-118207
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft has released its monthly security update for November 2026, which includes 1328 vulnerabilities affecting a range of products, including 60 that Microsoft marked as "critical." Out of 60 "critical" vulnerabilities, 45 are remote code execution (RCE) vulnerabilities.
```

#### Full body

```
Microsoft Patch Tuesday for November 2026 — Snort rules and prominent vulnerabilities By Cisco Talos Tuesday, November 10, 2026 20:41 Patch Tuesday Microsoft has released its monthly security update for November 2026, which includes 1095 vulnerabilities affecting a range of products, including 64 that Microsoft marked as "critical." Microsoft notes that 1 of the vulnerabilities disclosed this month have been exploited in the wild CVE-2026-124194 affects Microsoft Office Outlook. CVE-2026-124194 is a spoofing vulnerability involving Product UI does not Warn User of Unsafe Actions and has a CVSS base score of 6.5. Out of 64 "critical" vulnerabilities, 48 are remote code execution (RCE) vulnerabilities. Microsoft considers exploitation of the following vulnerabilities more likely: CVE-2026-113862 affects Windows Network Address Translation (NAT). CVE-2026-113862 is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.1. CVE-2026-118146 and CVE-2026-118148 affect Active Directory Domain Services. CVE-2026-118146 is a remote code execution vulnerability involving Incorrect Authorization and has a CVSS base score of 8.8. CVE-2026-118148 is an elevation of privilege vulnerability involving Incorrect Authorization and has a CVSS base score of 7.5. CVE-2026-118207 affects Microsoft Exchange Server. CVE-2026-118207 is a remote code execution vulnerability involving Use of Incorrectly-Resolved Name or Reference and has a CVSS base score of 8.8. CVE-2026-119952 affects Windows Schannel. CVE-2026-119952 is a remote code execution vulnerability involving Observable Timing Discrepancy and has a CVSS base score of 8.1. Microsoft considers exploitation of the following vulnerabilities less likely: CVE-2026-109459 and CVE-2026-119967 affect Windows Message Queuing Queue Manager. CVE-2026-109459 is a remote code execution vulnerability involving Heap-based Buffer Overflow and has a CVSS base score of 8.1. CVE-2026-119967 is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.1. CVE-2026-110043 , CVE-2026-110068 and CVE-2026-111309 affect Microsoft Office Outlook. CVE-2026-110043 is a remote code execution vulnerability involving Heap-based Buffer Overflow and has a CVSS base score of 8.8. CVE-2026-110068 is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.8. CVE-2026-111309 is a remote code execution vulnerability involving Release of Invalid Pointer or Reference and has a CVSS base score of 8.8. CVE-2026-110047 , CVE-2026-110067 , CVE-2026-111285 and CVE-2026-124185 affect Microsoft Office Word. CVE-2026-110047 is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.8. CVE-2026-110067 is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.8. CVE-2026-111285 is a remote code execution vulnerability involving Heap-based Buffer Overflow and has a CVSS base score of 8.8. CVE-2026-124185 is a remote code execution vulnerability involving Use of Uninitialized Resource and has a CVSS base score of 7.5. CVE-2026-111289 and CVE-2026-120003 affect Microsoft Office. CVE-2026-111289 is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.8. CVE-2026-120003 is a remote code execution vulnerability involving Heap-based Buffer Overflow and has a CVSS base score of 8.8. CVE-2026-112967 affects Windows Xbox Live Networking Service. CVE-2026-112967 is a remote code execution vulnerability involving Heap-based Buffer Overflow and has a CVSS base score of 9.8. CVE-2026-113752 affects Windows Print Spooler Components. CVE-2026-113752 is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 7.5. CVE-2026-113753 , CVE-2026-113856 , CVE-2026-113860 , CVE-2026-113861 , CVE-2026-113865 , CVE-2026-119947 , CVE-2026-119960 and CVE-2026-113864 affect Windows Hyper-V. CVE-2026-113753 is an
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Microsoft Patch Tuesday for November 2026 — Snort rules and prominent vulnerabilities
  - Published: 2026-11-11T01:41:17+00:00
  - Link: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-november-2026/
  - Summary: Microsoft has released its monthly security update for November 2026, which includes 1328 vulnerabilities affecting a range of products, including 60 that Microsoft marked as "critical." Out of 60 "critical" vulnerabilities, 45 are remote code execution (RCE) vulnerabilities.

### Cluster 3bcd6761c3 — score 17

- Title: GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-11-16T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, supply_chain
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

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

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold
  - Published: 2026-11-16T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold/
  - Summary: Written by: Aurora Blum, Kelli Vanderlee, Jess Xia, David Mainor Executive Summary As threat actors increasingly move beyond basic prompting to deploying autonomous multi-agent frameworks , automated vulnerability exploitation pipelines, and alternative monetization schemes like LLMJacking , the adversarial AI landscape has reached a critical inflection point. In this update, Google Threat Intelligence Group (GTIG) and Mandiant examine how adversaries across the cyber crime, espionage, and information operations spectrum are operationalizing generative AI to compress attack timelines, scale operations, and execute multi-stage intrusions at machine speed. Key trends over the last quarter include: Shift to Autonomous Workflows and Multi-Agent Frameworks: Adversary tradecraft has continued to transition beyond manual prompting to deploying autonomous multi-agent offensive frameworks—such as ARTEX , CAIRN, CyberStrikeAI, and PentAGI—to execute multi-stage intrusions at greater operational
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: GTIG AI Threat Tracker: Agentic Threat Activity Crosses a Significant Threshold
  - Published: 2026-11-16T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold/
  - Summary: Written by: Aurora Blum, Kelli Vanderlee, Jess Xia, David Mainor Executive Summary As threat actors increasingly move beyond basic prompting to deploying autonomous multi-agent frameworks , automated vulnerability exploitation pipelines, and alternative monetization schemes like LLMJacking , the adversarial AI landscape has reached a critical inflection point. In this update, Google Threat Intelligence Group (GTIG) and Mandiant examine how adversaries across the cyber crime, espionage, and information operations spectrum are operationalizing generative AI to compress attack timelines, scale operations, and execute multi-stage intrusions at machine speed. Key trends over the last quarter include: Shift to Autonomous Workflows and Multi-Agent Frameworks: Adversary tradecraft has continued to transition beyond manual prompting to deploying autonomous multi-agent offensive frameworks—such as ARTEX , CAIRN, CyberStrikeAI, and PentAGI—to execute multi-stage intrusions at greater operational

### Cluster 6ed7d76d5e — score 16

- Title: Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors
- Source: Unit 42 (threat_research_primary)
- Published: 2026-11-12T15:00:31+00:00
- Link: https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government, manufacturing_industrial
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government, manufacturing_industrial
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Summary

```
Our analysis of how attackers used the open-source Cairn AI agent framework to autonomously breach semiconductor, defense and civic targets. The post Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors 8 min read Related Products Advanced IP Defense Advanced URL Filtering Cloud-Delivered Security Services Cortex Cortex Agentic Endpoint Security Cortex XDR Cortex XSIAM Idira Unit 42 AI Security Assessment Unit 42 Continuous Frontier AI Defense Unit 42 Deep and Dark Web Service Unit 42 Incident Response Unit 42 Threat Intelligence Services By: Unit 42 Published: November 12, 2026 Categories: Malware Threat Research Tags: API DeepSeek Exploits Guardrails Penetration testing Privilege escalation VPN Share Executive Summary From August–September 2026, Chinese-speaking attackers used an open-source AI penetration testing framework called Cairn to autonomously conduct 25 operations against at least 19 organizations. The attackers weaponized Cairn by pairing it with Chinese AI models Zhipu GLM and DeepSeek. The attackers supplied a target and a goal, then Cairn planned, executed and recorded results on its own. These attacks achieved unauthorized access or data retrieval at 10 of the targeted organizations, including: Accessing dozens of valid credentials Mass exposing personal data (exceeding one million records at one organization) Retrieving military and government identities Creating persistent administrator accounts in a production system Modifying a live industry standards-ballot document We assess with moderate confidence that this activity represents China-nexus intelligence collection, which we currently track as CL-STA-1238. This article details how attackers used Cairn to target three key sectors: Advanced semiconductor manufacturing U.S. defense policy Civil society Palo Alto Networks customers are better protected from the threats discussed above through the following products and services: Advanced URL Filtering and Advanced IP Defense Cortex XDR and XSIAM Cortex Agentic Endpoint Security Idira Identity and Access Management (IAM) Idira Privileged Access Management (PAM) The Unit 42 AI Security Assessment can help identify and mitigate complex AI-enabled risks. Unit 42 Continuous Frontier AI Defense is an offensive security service designed to assist organizations with continuously discovering hidden and unknown exposures in dynamic environments, validate real-world exploitability across attack paths through agentic testing and expert analysis, and provide prioritized remediation and virtual patching guidance to accelerate risk mitigation. Organizations can access tailored adversary intelligence, direct analyst consultations and specialized exposure tracking through Unit 42 Threat Intel Services and its Deep and Dark Web Service . If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics AI , Agentic AI , Supply Chain Technical Analysis Cairn Framework The attackers behind CL-STA-1238 orchestrated their campaign using the publicly available penetration testing framework Cairn . An AI model drives each Cairn “agent worker.” Cairn coordinates its activities through a shared “blackboard.” Agents read the blackboard and write their findings back as a fact-intent graph, while human operators can inject “hints” at any time to help guide the operations if needed. Confirmed findings accumulate as immutable facts and the agent queues its next actions as intents. Attackers ran a customized fork of Cairn from a server hosted in Hong Kong ( 154.44.31[.]4 , AS979, NetLab Global) and hosted an attack egress and staging node in the U.S. ( 82.29.129[.]54 , AS142036, Hosteons Pte. Ltd.). Figure 1 below shows a screenshot of the controller login page of the attackers' Cairn framework. Figure 1. Attacker-operated Cairn login page. For each operation, the attackers created a task with a one-line goal, such as: 以拿到实质性高价值权限为止，包括但不限于webshell、ssh、源码、key、用户信息、凭据等，最好是可以进入内网 Translation: "Obtain substantive high-value access,
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors
  - Published: 2026-11-12T15:00:31+00:00
  - Link: https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/
  - Summary: Our analysis of how attackers used the open-source Cairn AI agent framework to autonomously breach semiconductor, defense and civic targets. The post Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors appeared first on Unit 42 .

### Cluster 877727aec7 — score 16

- Title: Not All That Glitters Is Gold: Tracking CopperDragon’s Sparrow Framework Around the Globe
- Source: Check Point Research (threat_research_primary)
- Published: 2026-11-10T14:01:14+00:00
- Link: https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion, web_shell_backdoor
- affected_industries: critical_infrastructure, financial_services, government, telecommunications
- affected_products: Android, OpenAI/ChatGPT
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage, web_shell_backdoor
- affected_industries: financial_services, government, critical_infrastructure, telecommunications
- affected_products: Android, OpenAI/ChatGPT
- content_type: threat_research
- confidence_tier: tier_1_primary_research

#### Summary

```
Key Points Introduction Over the past year, Check Point Research investigated a series of intrusion campaigns targeting several dozens of high-profile organizations across Latin America, Asia, and Europe. These campaigns initially appeared to be independent operations, each using different backdoors, post-exploitation tools and operational pace. However, we identified numerous connections between the tools and their […] The post Not All That Glitters Is Gold: Tracking CopperDragon’s Sparrow Framework Around the Globe appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 23 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 482 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 434 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 Not All That Glitters Is Gold: Tracking CopperDragon’s Sparrow Framework Around the Globe November 10, 2026 https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/ Key Points During a year-long investigation, Check Point Research identified three distinct operational clusters spanning Latin America, Asia, and Europe targeting telecommunications providers, government organizations, military entities, research institutions, and critical infrastructure. The clusters , SilentDelivery, OceanGate and DarkWire , are linked through shared infrastructure features and malware code similarities within the Sparrow malware framework. We track the entity behind the Sparrow framework as CopperDragon , a potential digital quartermaster supporting China-nexus threat actors, including FamousSparrow , Earth Estries , TropicTrooper , UAT-9244 , and others. Each cluster employed a different toolset and different initial access techniques, including compromising internet-facing infrastructure and highly selective watering-hole attacks. The compromised websites that were used for watering hole attacks were of government, shipping, and IT and research sectors. Our research uncovered several previously undocumented tools and new details about the Sparrow framework, including Windows and Linux variants, passive backdoor capabilities , and a connection to the Melofee backdoor. Introduction Over the past year, Check Point Research investigated a series of intrusion campaigns targeting several dozens of high-profile organizations across Latin America, Asia, and Europe. These campaigns initially appeared to be independent operations, each using different backdoors, post-exploitation tools and operational pace. However, we identified numerous connections between the tools and their infrastructure which linked them to the same Sparrow malware ecosystem. We track the entity behind these campaigns as CopperDragon , which may serve as a digital quartermaster supporting a number of China-nexus threat actors that use the Sparrow cross-platform malware framework for Linux and Windows. What is CopperDragon? FamousSparrow is a threat actor that was first identified in 2021, whose main backdoor is SparrowDoor . Since then, multiple vendors have reported on related activity and malware variants, including CrowDoor , HemiGate , and TernDoor . Over time, it became apparent that this other activity was not necessarily carried out by the original FamousSparrow group. Instead, reporting pointed to several distinct actors using a shared toolset, potentially supplied by the same entity. These actors include FamousSparrow , Earth Estries , TropicTrooper , UAT-9244 , and others. FamousSparrow was previously also linked to Salt Typhoon, but the relationship details remain unclear. Based on the apparent tool-sharing, we began tracking the entity behind the Sparrow framework as CopperDragon , its possible developer and supplier. In this report, we examine three distinct activity clusters targeting major telecommunications providers , government organizations , and military entities . Together, these operations provide a broader view of the connected and evolving espionage ecosystem linked to CopperDragon : SilentDelivery uses highly selective watering-hole attacks that distribute the SquadC backdoor through Trojanized MSI installers masquerading as certificate repair utilities. This cluster focuses on Europe and Asia regions. OceanGate focuses primarily on Asian organizations and uses a variant of SparrowDoor . The actor first com
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: Not All That Glitters Is Gold: Tracking CopperDragon’s Sparrow Framework Around the Globe
  - Published: 2026-11-10T14:01:14+00:00
  - Link: https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/
  - Summary: Key Points Introduction Over the past year, Check Point Research investigated a series of intrusion campaigns targeting several dozens of high-profile organizations across Latin America, Asia, and Europe. These campaigns initially appeared to be independent operations, each using different backdoors, post-exploitation tools and operational pace. However, we identified numerous connections between the tools and their […] The post Not All That Glitters Is Gold: Tracking CopperDragon’s Sparrow Framework Around the Globe appeared first on Check Point Research .

### Cluster eb92172155 — score 16

- Title: [tl;dr sec] #354 - ARTEX & Agentic Hacking in the Wild, The Patchless Window, Backporting Security Fixes
- Source: tl;dr sec (practitioner_analysis)
- Published: 2026-11-12T15:30:00+00:00
- Link: https://tldrsec.com/p/tldr-sec-354
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: healthcare, manufacturing_industrial
- affected_products: Linux kernel, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: healthcare, manufacturing_industrial
- affected_products: OpenAI/ChatGPT, Linux kernel
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
ARTEX be hacking errybody up in here, the critical gap between when a patch is public and defenders respond, and how stable releases may be missing many patches
```

#### Full body

```
0 tl;dr sec Posts [tl;dr sec] #354 - ARTEX & Agentic Hacking in the Wild, The Patchless Window, Backporting Security Fixes [tl;dr sec] #354 - ARTEX & Agentic Hacking in the Wild, The Patchless Window, Backporting Security Fixes ARTEX be hacking errybody up in here, the critical gap between when a patch is public and defenders respond, and how stable releases may be missing many patches Clint Gibler November 12, 2026 Hey there, I hope you’ve been doing well! 🤗 Family Movie Time I have some fun Halloween anecdotes but I haven’t had time to write them up yet so I’ll save them for next week. Instead, I’ll quickly reflect on this wholesome meme I saw recently: It reminds me of a very fond memory I have of when I was a wee lad, say 6 or under, about how my parents and I would watch movies together. My dad would sit on one side of the couch and extend his legs down the rest of the couch, then my mom would sit on top of him and do the same, and then I’d sit on her and do the same, like we were a bunch of matryoshka Russian nesting dolls. It was very comforting. There’s something nice about that closeness and familiarity. A part of me is wistful that this isn’t as much a thing when you’re older. I guess you get to live it again for a time, when you have kids. Feel free to share a sweet memory you had with your parents as a kid, or that you have with your kid(s) now 🙂 Sponsor 🚨 65% of threat intel teams say noise is their #1 problem (Sponsor) Alert noise and false positives were the most common challenge (65%) among surveyed enterprise intel leaders in Flashpoint’s 2026 Enterprise Threat Intelligence Report, followed by analyst bandwidth (55%). As one healthcare leader put it, “we can’t hire our way out of that problem.” Flashpoint Ignite force-multiplies the team you already have, turning noisy alerts into actionable defenses. Tour the platform to discover how Ignite supports faster investigation and decision-making through advanced search, customized alerts, finished intelligence, dashboards, analyst support, and integrated AI. 👉 Tour the Flashpoint platform 👈 Agreed, focusing on the signal of what matters is key 👌 AppSec The Vulnpocalypse - Good News and Bad News Phil Venables examines the "vulnapocalypse" challenge where AI-driven vulnerability discovery is creating massive triage workloads, but argues the real bottleneck isn't finding or fixing vulnerabilities in code, it's deploying those fixes across diverse, complex infrastructures including edge devices, medical equipment, and industrial systems. He breaks down vulnerability remediation into four stages (discovery, fix development, testing/staging, deployment) and notes that while AI accelerates stages 1-2, stage 4 deployment often consumes 60% of effort due to certification requirements, infrastructure complexity, and reliability risks. Phil proposes solutions including policy intent systems that auto-enforce configurations, AI-driven compensating controls that adjust WAFs/firewalls based on vulnerability context, patch intelligence to predict breaking changes, and faster rollback capabilities with incremental deployment percentages (5% → 20% → … 100%) to catch issues earlier. 💡 Fantastic blog as always from Phil. I like the style of the intro bullets, alternating “the good news is” and “the bad news is.” I’ve also been finding that the vulnerability fix deployment is a big percent of the effort and problem. Great discussion of the challenges and opportunity at each vulnerability remediation stage. Backporting security fixes to stable releases Trail of Bits’ Artem Dinaburg calls attention to the challenge of actually getting fixes to users, as stable releases (e.g. Ubuntu Long Term Support) often contain thousands of known, unfixed CVEs that AI agents can easily exploit. Using Codex with GPT-5.6, Trail of Bits identified and backported security fixes to stable Linux kernel branches and distributions, successfully getting 142 fixes representing 90 CVEs applied to stable kernel
```

#### Corroborating sources (1)

- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #354 - ARTEX & Agentic Hacking in the Wild, The Patchless Window, Backporting Security Fixes
  - Published: 2026-11-12T15:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-354
  - Summary: ARTEX be hacking errybody up in here, the critical gap between when a patch is public and defenders respond, and how stable releases may be missing many patches

### Cluster fba6e81cad — score 16

- Title: Lessons from 59 Linux Kernel Bug Reports
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-11-11T16:55:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: Linux kernel

#### Cluster taxonomy (union across members)
- affected_products: Linux kernel, Microsoft Defender
- urgency_signals: poc_available
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- affected_products: Linux kernel, Microsoft Defender
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft FORGE Lab researchers used codename MDASH to investigate Linux kernel vulnerabilities, resulting in 59 upstream bug reports, 33 assigned CVEs, and 38 merged fixes. The research includes eight demonstrated local root privilege-escalation exploits and examines the challenges of turning AI-generated findings into validated vulnerabilities and upstream fixes. The post Lessons from 59 Linux Kernel Bug Reports appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Frontier AI models Linux Threats intelligence Vulnerabilities and exploits Content types Research Products and services Microsoft Defender Topics Actionable threat insights AI and agents At Microsoft’s FORGE Lab , we used codename MDASH to scan a subset of Linux kernel subsystems from late May to mid-June 2026. One full-time researcher and one intern led this three-month effort, which has so far produced 59 public upstream reports and 33 assigned CVEs . We confirmed working root privilege-escalation exploits for eight of those CVEs, and fixes for 38 of our reports have been merged into mainline. Finding the bugs was only part of the work. The initial scans produced 26,502 raw findings in about two weeks, but turning those results into reproducible bugs, upstream reports, and patches took months of expert investigation and collaboration with Linux maintainers. In this post, we look back at how we went from thousands of potential findings to validated vulnerabilities and upstream fixes, and what we learned about scaling vulnerability discovery with AI. From scans to reports We focused on several core kernel subsystems, such as networking, filesystems, and security modules. Our selection criteria were straightforward: we picked security-sensitive components with no obvious dependence on specialized hardware, making QEMU-based validation simple and unified. Code scanning mainly used Sonnet 4.6 (71.1% of code-scanning tokens), GPT-5.4 (20.1%), and GPT-5.5 (7.1%). The codename MDASH scans produced 26,502 raw scan findings in about two weeks on two servers (64 cores/256 GB RAM and 32 cores/128 GB RAM), but turning that output into patches and reports took months of expert work. We filtered out low-confidence claims using codename MDASH’s confidence levels and separate fast screening agents we built, reducing the pool to 11,769 candidates. PoC-generating agents then attempted reproduction in QEMU, mainly using GPT-5.5 (77.3% of reproduction tokens), Opus 4.6 (13.2%), and GPT-5.5-cyber (9.4%). Experts then reviewed the 621 cases with PoC evidence to identify root causes, merge duplicates, and prepare upstream submissions. Figure 1 . Scan-to-report workflow. 26,502 raw findings → 11,769 screened candidates → 621 PoC-backed cases → 59 upstream reports. Where the 621 cases went Roughly one public upstream report landed from every ten PoC-backed cases: 59 reports from 621 cases (9.5%). Across those cases, the main reasons for not filing a separate new report were: 266 (42.8%) shared a root cause with another case, so one patch could fix them together. 163 (26.2%) were not reported after review, mostly due to limited security impact. 133 (21.4%) were already reported or fixed upstream. Submission timing explains many of the 133 overlaps. Most of the 621 cases were new when the scans finished (though some may already have been in flight by others). Our first public report went out on June 27, 2026, more than five weeks after scanning started. By September 1, 55 of the 59 had been posted to the public lists; the other four were reported privately during the same window and routed to the public lists by mid-October. Getting fixes merged Upstream Linux typically requires vulnerability reports to come with a working patch. Agents helped draft initial fixes, but human validation, subsystem understanding, and iterating with maintainers during review remained essential. So far, fixes for 38 of our reports have been merged into upstream mainline—half on the first submission, and the rest after one to four revisions. Reaching a mainline release from the first public patch took a median of 41 days (up to 108 days), and we are still working with maintainers on the remaining reports. How old the bugs were Interestingly, most of the bugs we reported had been in the kernel for years. Across the 59 reports, the average bug was 8.1 years old when we first reported it publicly. One of the oldest, a cls_u32 shift-out-of-bo
```

#### Corroborating sources (3)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Lessons from 59 Linux Kernel Bug Reports
  - Published: 2026-11-11T16:55:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/
  - Summary: Microsoft FORGE Lab researchers used codename MDASH to investigate Linux kernel vulnerabilities, resulting in 59 upstream bug reports, 33 assigned CVEs, and 38 merged fixes. The research includes eight demonstrated local root privilege-escalation exploits and examines the challenges of turning AI-generated findings into validated vulnerabilities and upstream fixes. The post Lessons from 59 Linux Kernel Bug Reports appeared first on Microsoft Security Blog .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New NoisyTCP vulnerability lets attackers crash Linux servers
  - Published: 2026-11-16T09:30:04+00:00
  - Link: https://www.bleepingcomputer.com/news/linux/new-noisytcp-linux-kernel-flaw-lets-attackers-crash-servers/
  - Summary: An 11-year-old Linux kernel vulnerability, dubbed NoisyTCP, affects almost all Linux distributions and lets attackers crash systems running Nginx, Apache, and SSH servers with default configurations. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More Stories
  - Published: 2026-11-12T18:02:51+00:00
  - Link: https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html
  - Summary: A search result isn't always safe. An access request isn't always harmless. And a familiar account doesn't always mean a familiar person is using it. Simple things to remember. Yet a surprising amount of this week's trouble starts right there. Attackers are using fake websites, stolen access, and trusted tools to get into places they shouldn't be. AI is helping them build attacks faster, while

### Cluster 7cc91e5ade — score 16

- Title: IT threat evolution in Q3 2026. Mobile statistics
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-10T08:00:17+00:00
- Link: https://securelist.com/malware-report-q3-2026-mobile-statistics/121844/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Android

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- affected_products: Android
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- affected_industries: financial_services
- affected_products: Android
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Q3 2026 mobile threat statistics for Android malware, adware, and unwanted software, plus the most notable malware found during the quarter.
```

#### Full body

```
Content menu Close Subscribe Threat Response Table of Contents The quarter in figures Quarterly highlights Mobile threat statistics TOP 20 types of mobile malware Mobile banking Trojans TOP 10 mobile bankers Authors Anton Kivva IT threat evolution in Q3 2026. Non-mobile statistics IT threat evolution in Q3 2026. Mobile statistics The mobile section of the quarterly cyberthreat report includes statistics on malware, adware, and potentially unwanted software for Android, as well as descriptions of the most notable threats for Android and iOS discovered during the reporting period. These statistics are based on detection alerts from Kaspersky products, collected from users who consented to provide statistical data to Kaspersky Security Network. The quarter in figures According to Kaspersky Security Network, in Q3 2026: More than 1.66 million attacks involving mobile malware, adware, or unwanted software were blocked. The Trojan-Banker category was the prevalent mobile malware threat with a 31.63% share of all detected malicious apps. Over 378,000 malicious installation packages were detected, including 119,688 mobile banking Trojan packages. Quarterly highlights In July, we discovered a malicious app targeting Brazilian users that may have used AI to automate fraud. The app was disguised as Google Play Protect, a suite of security services for Android devices. Malicious app imitating Google Play Protect The app’s code used the DistilBERT model to interpret natural-language commands sent from the C2 server. Traces left in the code suggest the server-side commands may also have been generated by a large language model (LLM). In August, we discovered a Trojan that analyzed images saved in the device’s gallery and took screenshots to look for banking data, including CVV codes. The malware used an on-device AI model to classify images. The app could also update this model, which gave the scammers a way to expand the Trojan’s functionality. In the third quarter, the infamous subscription Trojan detected as Trojan.AndroidOS.Subscriber.bh made it into Google Play again. This time, it was disguised as an app for creating keyboard themes. Subscription Trojan disguised as a keyboard theme app The Trojan opened a subscription link in a hidden WebView and intercepted the message containing the confirmation code. According to our data, the scammers mainly targeted users in Thailand. There were also new attacks on iOS users. In August, researchers at Socket discovered 13 infected PHP packages in the Packagist repository. The malicious payload injected links to fraudulent casinos into sites that used these packages and, on iOS devices only, a hidden iframe that loaded the DarkSword exploit kit. The attack delivered a spyware module that stole keychain contents, Wi-Fi passwords, SMS messages, photos, and other personal data. Other modules found in this campaign were used to steal crypto wallet data and the seed phrases used to recover them. SlowMist researchers found the same DarkSword exploit chain used in a fake app, FomoPeek. FomoPeek was published in the App Store, presenting itself as a crypto wallet tracker. The malware was designed to steal data from notes and crypto wallet apps. Also in August, we discovered infected versions of popular iOS apps distributed through Telegram (link in Russian). To install such an app, the attackers asked users to buy a developer certificate. The modified versions contained a malicious module that collected device information, took screenshots, and sent this data to a server. Mobile threat statistics The downward trend in attacks on mobile devices involving malware, adware, or unwanted software continued: the number fell to 1,668,368 in Q3 from 1,996,823 in Q2. Attacks on users of Kaspersky mobile solutions, Q1 2025 – Q3 2026 ( download ) In the third quarter, this decline was driven in part by fewer adware attacks, which we examine in more detail below. The number of Android malware samples grew compared to
```

#### Corroborating sources (2)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: IT threat evolution in Q3 2026. Mobile statistics
  - Published: 2026-11-10T08:00:17+00:00
  - Link: https://securelist.com/malware-report-q3-2026-mobile-statistics/121844/
  - Summary: Q3 2026 mobile threat statistics for Android malware, adware, and unwanted software, plus the most notable malware found during the quarter.
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: ArcticRAT Cybercrime Gang Profiles Victim Finances With AI
  - Published: 2026-11-13T20:20:27+00:00
  - Link: https://www.darkreading.com/mobile-security/arcticrat-cybercrime-gang-profiles-victim-finances-ai
  - Summary: The Android malware has expanded from focusing on cryptocurrency theft to full device control, and the attackers have added advanced analysis of stolen information.

### Cluster 7d41d4d72e — score 16

- Title: Git security vulnerabilities announced
- Source: GitHub Security Lab (offensive_vulnerability_research)
- Published: 2026-11-10T18:00:00+00:00
- Link: https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- affected_industries: critical_infrastructure
- affected_products: GitHub
- cve_ids: CVE-2026-105437, CVE-2026-111760, CVE-2026-113408, CVE-2026-114467, CVE-2026-114469
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ddos
- affected_products: GitHub
- cve_ids: CVE-2026-111760, CVE-2026-113408, CVE-2026-114467, CVE-2026-114469, CVE-2026-105437
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Git is releasing updates addressing six security vulnerabilities affecting recursive clones, reference handling, merges, binary patches, and imports. Here is what users need to know. The post Git security vulnerabilities announced appeared first on The GitHub Blog .
```

#### Full body

```
Elijah Newren · @newren November 10, 2026 | 5 minutes Share: Today, the Git project is releasing new versions to address six security vulnerabilities. These include arbitrary code execution when recursively cloning a malicious repository, writes to unintended files, and memory corruption when processing merges or binary patches. The fixes are included in Git 2.56.1 , with backports to Git 2.55.1, 2.54.1, 2.53.1, 2.52.1, 2.51.3, and 2.50.2. We recommend updating to Git 2.56.1 or the patched release for your maintenance series, and updating any applications that bundle Git. Vulnerabilities in Git CVE-2026-111760: Code execution during recursive clones Git checks paths before writing files into a working tree, including rejecting paths that would overwrite its own repository metadata. However, an integer truncation in Git’s index handling can cause an extremely long path to pass validation under one name and then be written using a shorter name. An attacker can use this discrepancy to replace a submodule’s .git file with a symbolic link pointing to a directory containing malicious configuration or hooks . When Git subsequently uses that directory, it can execute attacker-controlled code during a recursive clone. The fix rejects extremely long index entry paths before their lengths can be truncated. [ Advisory ] CVE-2026-113408: Path traversal through a server’s advertised HEAD When cloning an empty repository using Git protocol v2, the server can advertise a HEAD symref pointing to an unborn branch (one that has no commits yet). Git did not validate the symref’s target before storing it locally. A malicious server can supply a name containing path-traversal components. With the files reference backend, a later operation that updates the branch can write outside the intended reference directory. Git now validates the advertised target before accepting it. The release also validates other reference names and symbolic-reference targets received through protocol v2. [ Advisory ] CVE-2026-114467: Stack corruption when removing signatures When stripping GPG signatures from a message, Git assumed there would be at most two signatures. A specially crafted message containing more than two signatures can cause Git to write past the end of a fixed-size stack array. This can be triggered by merging a tag containing more than two signatures, causing memory corruption and a potential denial of service. Hosting services that perform these merges on behalf of users can also be affected. The fix removes the fixed-size array and handles messages with any number of signatures. [ Advisory ] CVE-2026-114469: Out-of-bounds reads when applying binary patches Git rejects patches larger than approximately 1 GiB because its patch application code cannot safely handle larger inputs. However, this check only considered the size of the patch as supplied. Binary patches are compressed and encoded, so a relatively small patch can expand beyond that limit. A crafted patch can bypass the input-size check and cause an out-of-bounds read, crashing Git. Git now also checks the declared uncompressed size before processing a binary patch. [ Advisory ] CVE-2026-105437: Heap corruption during large merges Git’s merge machinery calculates how much memory it needs for a merge result before writing the output. That calculation can overflow when the result is very large, including when many conflicts are combined with a large conflict-marker-size attribute. The overflow can cause Git to allocate a buffer that is too small, then write outside it, corrupting heap memory. This affects applications and hosting services that use Git to merge untrusted content, as well as local merges. The fix uses size-appropriate types and checked arithmetic, rejecting merges whose output size cannot be represented safely. [ Advisory ] CVE-2026-114466: Filesystem access through fast-import streams git fast-import reads a stream of commands to build a repository. Some commands can access files
```

#### Corroborating sources (4)

- **GitHub Security Lab** (offensive_vulnerability_research)
  - Title: Git security vulnerabilities announced
  - Published: 2026-11-10T18:00:00+00:00
  - Link: https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/
  - Summary: Git is releasing updates addressing six security vulnerabilities affecting recursive clones, reference handling, merges, binary patches, and imports. Here is what users need to know. The post Git security vulnerabilities announced appeared first on The GitHub Blog .
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Don't just flag it, fix it: How to run CodeMender in your pull requests
  - Published: 2026-11-10T17:00:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/how-to-run-codemender-in-your-pull-requests/
  - Summary: As many developers use agentic tools to create more code faster than ever before, the code has gotten more complex and they’re taking longer to find and fix software flaws. Helping to address that pressure is a key concern at Google. We know that software development velocity is increasing, as much as 2x for some teams , and the average developer fix time for software flaws expanded from approximately 59 days a decade ago to more than 170 days in 2025, according to the Mandiant M-Trends 2026 Report . CodeMender: AI powered vulnerability fixes right in GitHub PRs To help you secure more code, more quickly, we’ve built CodeMender, our autonomous code-security agent that can find and fix software flaws at machine speed. We also know that developer tools only succeed if they fit into existing routines. That’s why CodeMender, part of our AI Threat Defense platform , brings automated code fixes directly into the developer workflow. Today, we’re sharing this reference architecture that wires
- **Simon Willison** (ai_security_agentic_risk)
  - Title: datasette 1.0a43
  - Published: 2026-11-15T23:20:27+00:00
  - Link: https://simonwillison.net/2026/Nov/15/datasette/
  - Summary: Release: datasette 1.0a43 I've been leaning hard into Claude Fable 5.2 to help knock things off the 1.0 milestone , which is now 53% complete. The biggest 1.0 item in this release is streaming support for output renderers - the built-in TSV and CSV export mechanisms now use this as well, and plugins can register themselves as capable of streaming every row in a table in one go via the new Response.stream() method. There are a couple of security fixes, one of which I deemed deserving of a GitHub advisory : private stored queries could be exposed, granting access to the title and SQL of the query (but not allowing that query to be executed). There are dozens of smaller improvements. The row page JSON representation finally has a design suitable for 1.0 . A new <datasette-copy-button> Web Component provides copy-schema in various places. JSON in columns on the row page can be pretty-printed. There's a new DatasetteModal.confirm() JavaScript utility method. Plus dozens of bug fixes, includ
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attacker Used 4,837 Hijacked GitHub Accounts to Run a CI Secret Stealer in 1,806+ Repositories
  - Published: 2026-11-12T06:42:47+00:00
  - Link: https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html
  - Summary: Starting Tuesday, an attacker used stolen credentials for 4,837 GitHub accounts to plant a secret stealer in repositories those accounts could write to, according to Aikido Security, a security software company. The stealer is built to take the secrets and cloud credentials that a repository's CI workflows can reach. It ran in at least 1,806 repositories, where the attacker has likely collected

### Cluster 2cab26404c — score 15

- Title: PHP2Shell Exploitation on Check Point Gateway
- Source: Check Point Research (threat_research_primary)
- Published: 2026-11-12T13:56:37+00:00
- Link: https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-109618

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, web_shell_backdoor
- actor_attribution: UNC5221
- affected_industries: financial_services
- affected_products: Android, Ivanti, Palo Alto Networks
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-123039
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, web_shell_backdoor
- actor_attribution: UNC5221
- affected_industries: financial_services
- affected_products: Ivanti, Android, Palo Alto Networks
- cve_ids: CVE-2026-109618, CVE-2026-123039, CVE-2026-109619
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Key findings Introduction We have now confirmed that, in late October 2026, approximately one week after a security fix became available, activity originating from 130.94.19[.]204 targeted Israeli organizations through vulnerable Mobile Access portals on Check Point Security Gateways. Evidence suggested some cases of a successful compromise, with exploitation activity consistent with PHP2Shell, associated with CVE-2026-109618 […] The post PHP2Shell Exploitation on Check Point Gateway appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 23 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 482 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 434 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 PHP2Shell Exploitation on Check Point Gateway November 12, 2026 https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/ Key findings Beginning on 30 October 2026, an attacker executed scanning and exploitation activity against organizations with unpatched Check Point Security Gateways, using Mobile Access portals with PHP2Shell as initial access followed by CVE-2026-123039. The first wave, on October 30, targeted Israeli organizations and included destructive activity against some of them. A broader second wave on November 2 targeted organizations across multiple countries and sectors, with no evidence of destructive activity In the investigated intrusion, PHP2Shell provided initial access, followed by privilege escalation through the DynamicCLI interface, tracked as CVE-2026-123039. The attackers then deployed PHP webshells, the persistent TSGA backdoor and its embedded TSProxy networking component. The attackers pivoted from the gateway to a VMware ESXi host over SSH, deployed the destroy_v6 wiper, and left politically themed DREAM_ANNEXATION.txt notes during the destructive stage. TSGA and TSProxy are modified variants of PhiliKit, a malware framework previously documented in attacks exploiting Ivanti vulnerabilities. Both tools share distinctive code, configuration, and cryptographic material with the framework Although ESET associated PhiliKit with China nexus UNC5221, the evidence does not allow us to assess with high confidence the true nature of this operation. Several scenarios remain plausible: the identified actor ran the entire campaign, acted solely as an initial access broker, or took part in a false-flag operation. It is also possible that the destructive activity served as a smoke screen. The note left during the destructive activity uses the Dream Security brand. Dream had recently published research on PHP2Shell exploitation of Palo Alto Networks devices by China nexus actors. While this timing raises the possibility of retaliation, the available evidence does not establish a clear motive. Introduction We have now confirmed that, in late October 2026, approximately one week after a security fix became available, activity originating from 130.94.19[.]204 targeted Israeli organizations through vulnerable Mobile Access portals on Check Point Security Gateways. Evidence suggested some cases of a successful compromise, with exploitation activity consistent with PHP2Shell, associated with CVE-2026-109618 and CVE-2026-109619. Following initial access, the attacker escalated privileges from the portal service account to root by exploiting CVE-2026-123039 , a local privilege-escalation vulnerability in the DynamicCLI IPC interface. The attacker then used privileged command execution to deploy PHP webshells and establish persistence. A second scanning wave on November 2 nd targeted some Israeli organizations previously targeted during the first wave, alongside additional organizations worldwide, with no apparent focus on Israel. Neither wave showed a clear sector preference, suggesting opportunistic initial-access attempts rather than sector-specific targeting. Infection Flow On October 30, 2026, the first signs of exploitation appeared on the targeted Check Point Mobile Access gateways. PHP session artifacts were created under /opt/CPcvpn-R81.20/tmp/, including session files containing the upload_progress_pwn marker associated with the exploitation activity. During the same window, the portal’s Apache/PHP workers experienced hundreds of segmentation faults, providing additional evidence of repeated exploitatio
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: PHP2Shell Exploitation on Check Point Gateway
  - Published: 2026-11-12T13:56:37+00:00
  - Link: https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
  - Summary: Key findings Introduction We have now confirmed that, in late October 2026, approximately one week after a security fix became available, activity originating from 130.94.19[.]204 targeted Israeli organizations through vulnerable Mobile Access portals on Check Point Security Gateways. Evidence suggested some cases of a successful compromise, with exploitation activity consistent with PHP2Shell, associated with CVE-2026-109618 […] The post PHP2Shell Exploitation on Check Point Gateway appeared first on Check Point Research .

### Cluster 40142a0f30 — score 13

- Title: Cursor Supply Chain Attack Started at Fireworks AI
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-16T15:45:43+00:00
- Link: https://www.securityweek.com/cursor-supply-chain-attack-started-at-fireworks/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain, zero_day
- affected_industries: education
- affected_products: Anthropic/Claude, Google Cloud, OpenAI/ChatGPT
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, zero_day, data_breach
- affected_industries: education
- affected_products: Anthropic/Claude
- urgency_signals: zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The attacker stole an access key from Fireworks and used it to exfiltrate credentials that enabled them to push malicious Claude Code extension copies. The post Cursor Supply Chain Attack Started at Fireworks AI appeared first on SecurityWeek .
```

#### Full body

```
Credentials compromised in the hack of AI inference platform Fireworks AI allowed attackers to steal more secrets and push malicious Claude Code extension copies, Cursor says. The supply chain attack was discovered on October 29 and resulted in threat actors making two modified versions of the anthropic.claude-code extension (2.1.312 and 2.1.313) available through the Cursor VS Code Extension Marketplace for roughly 11 hours. Anthropic was never hacked, and all the malicious activity occurred in Cursor’s environment, the company explains. Instead, Cursor was hit after Fireworks was hacked twice in October. First, internal Fireworks credentials were used to access Fireworks stored secrets and account and billing information. Then, a third-party cloud provider was compromised, Fireworks development machines were reached, and customer data was stolen. A Cursor access key issued to Fireworks was compromised in one of these incidents and the attacker used it to copy data from a read-only storage bucket, including unredacted credentials that opened the door to SaaS tools used by Cursor. “From these tools they accessed select archived non-production Cursor source code repositories (some containing business contact information), limited customer support data and email conversations, product usage metrics and contact details, summaries of some coding agent conversations, and some credentials users had sent to the Cursor support team,” Cursor explains . Advertisement. Scroll to continue reading. While Cursor blocked the attacker’s access immediately after discovering the unauthorized activity, the attacker used secrets exfiltrated from the company’s internal systems to place “malicious, unauthorized copies of Anthropic’s Claude Code extension directly on the cache used to serve the Cursor VS Code extension marketplace.” The malware was never present in the Open VSX marketplace source, but was served to the users who requested the cached versions of the extension. According to Cursor, at most 5,000 users were affected. “If customers installed or updated to the tampered version Anthropic.claude-code 2.1.312 or 2.1.313 from the Cursor VS Code extension marketplace during the exposure window, we ask customers to follow the steps in our security notice . Uninstalling the extension alone may not be enough,” Cursor notes. The company considers the incident contained, as it has not seen attacker activity in its environment since November 1. Notion and Uber also disclosed data breaches stemming from the Fireworks compromise. Related: Maersk Confirms Data Theft Amid $5 Million Extortion Attempt Related: Revolve Puts Data Breach Victim Count at 1.5 Million Related: Iris Plaza Breach May Have Exposed Data of 7.7 Million Customers Related: Over 3 Million People Hit by Frontline Education Data Breach Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Law Enforcement Disrupts Gootloader, CastleRAT, and StealC Infrastructure Citrix Patches 10 Critical NetScaler Vulnerabilities Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’ PHP2Shell Exploited in Destructive Check Point Gateway Attacks Hackers Exploit New N-central Zero-Day Hours After PoC Publication Chrome, Firefox Updates Patch Over 180 Vulnerabilities Daylight Lands $80 Million for AI-Powered Security Operations Notion Customer Data Compromised in Fireworks AI Hack Latest News Trump Administration Moves to Block China From Indirect Access to American AI Technology Google Project Zero Sets Course for 30-Day Disclosure Deadline Barracuda Hacked Amid Surge in Artex-Powered Cyberattacks Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch Recent UnrealIRCd Vulnerability Exploited in Attacks Hackers Probe Newly Disclosed Flaws in Copeland Refrigeration Controllers Uber Data Bre
```

#### Corroborating sources (6)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Cursor Supply Chain Attack Started at Fireworks AI
  - Published: 2026-11-16T15:45:43+00:00
  - Link: https://www.securityweek.com/cursor-supply-chain-attack-started-at-fireworks/
  - Summary: The attacker stole an access key from Fireworks and used it to exfiltrate credentials that enabled them to push malicious Claude Code extension copies. The post Cursor Supply Chain Attack Started at Fireworks AI appeared first on SecurityWeek .
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Prompting Claude Fable 5.2
  - Published: 2026-11-10T05:34:14+00:00
  - Link: https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/
  - Summary: Claude Fable 5.2 pays close attention to who owns the code it works on. In Anthropic’s testing on small coding tasks, the model tended to add to the existing structure when the prompt said nothing about ownership or presented the code base as someone else’s, even when that duplicated existing code. When the prompt said the code base was the model’s own, it often consolidated duplicated code and sometimes made related fixes without being asked. If you want the model to improve the structure as it works, say that the code is its own: You are the owner and long-term maintainer of this codebase, and its design is up to you. The ownership sentence makes the model much more likely to consolidate duplicated code into one shared function. In Anthropic’s testing on small coding tasks, the model consolidated duplicated code in under 10 percent of runs without the sentence and in about 75 percent of runs with it. — Prompting Claude Fable 5.2 , Anthropic documentation Tags: prompt-engineering , an
- **Just Security** (policy_strategy_geopolitics)
  - Title: Just the Docs: Nonprofits Sue Five Frontier AI Companies to Freeze Development, Citing Cyberattack and Catastrophic Risks
  - Published: 2026-11-13T20:51:22+00:00
  - Link: https://www.justsecurity.org/164494/nonprofits-lawsuit-freeze-frontier-ai-development/?utm_source=rss&utm_medium=rss&utm_campaign=nonprofits-lawsuit-freeze-frontier-ai-development
  - Summary: Four nonprofits sue Anthropic, Google, Meta, OpenAI, and SpaceXSI seeking to freeze frontier AI development over cyberattack and catastrophic risks. The post Just the Docs: Nonprofits Sue Five Frontier AI Companies to Freeze Development, Citing Cyberattack and Catastrophic Risks appeared first on Just Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cursor Says Stolen Fireworks AI Key Led to Trojanized Claude Code Extension Incident
  - Published: 2026-11-15T08:22:04+00:00
  - Link: https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html
  - Summary: The compromise of Anthropic's official Claude Code extension on Cursor's extension marketplace was the result of the theft of an access key that was exposed in the wake of a breach targeting Fireworks AI. "An attacker obtained an access key we had issued to Fireworks," Cursor said in a Friday update. "The key was exposed by Fireworks, and the attacker used it to copy data from a read-only
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Anthropic's Glasswing Finds Many Vulnerabilities Yet Delivers Few Fixes, Researcher Says
  - Published: 2026-11-11T16:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/anthropic-glasswing/
  - Summary: VulnCheck’s Patrick Garrity has found that seven months on, Project Glasswing resulted in only 217 vulnerabilities getting fixed, despite thousands reported
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: What’s new with Google Cloud
  - Published: 2026-11-13T17:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - Summary: Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Nov 9 - Nov 13 More frontier model choice on Google Cloud: Anthropic’s Claude Fable 5.2 and Meta’s Muse model series. Developers now have even more flexibility to build, deploy, and scale with the right model for every workload on Google Cloud. Anthropic’s Claude Fable 5.2 is now generally available in the Model Garden, bringing frontier intelligence to complex coding, scientific research, and multi-agent orchestration. Plus, Meta’s newest models— Muse Spark 1.3 , Muse Wonder , and the efficient Muse Ember —are now available in public preview, giving teams seamless access to both proprietary and open-weight capabil

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

### Cluster e8815d20df — score 12

- Title: IT threat evolution in Q3 2026. Non-mobile statistics
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-10T08:00:37+00:00
- Link: https://securelist.com/malware-report-q3-2026-pc-iot-statistics/121843/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Apple iOS/macOS

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, data_breach, ransomware_extortion
- affected_products: Apple iOS/macOS, Palo Alto Networks, SonicWall
- cve_ids: CVE-2025-60710, CVE-2026-0257, CVE-2026-15409, CVE-2026-15410, CVE-2026-45659
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_government, tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, active_exploitation
- affected_products: Palo Alto Networks, SonicWall, Apple iOS/macOS
- cve_ids: CVE-2026-0257, CVE-2026-15409, CVE-2026-15410, CVE-2026-45659, CVE-2025-60710
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Key trends and statistics on malware targeting Windows and macOS computers and Internet of Things (IoT) devices in Q3 2026.
```

#### Full body

```
Content menu Close Subscribe Threat Response Table of Contents Quarterly figures Ransomware Quarterly trends and highlights Threat actor disruption Vulnerabilities and attacks The most prolific groups Number of new ransomware variants Number of users attacked by ransomware Trojans TOP 10 countries and territories attacked by ransomware Trojans TOP 10 most common families of ransomware Trojans Miners Number of new miner variants Number of users attacked by miners TOP 10 countries and territories attacked by miners Attacks on macOS Quarterly highlights TOP 20 threats to macOS TOP 10 countries and territories by share of attacked users IoT threat statistics Distribution by protocol TOP 10 threats delivered to IoT devices Attacks on IoT honeypots Attacks via web resources TOP 10 countries and territories that served as sources of web-based attacks Countries and territories where users faced the greatest risk of online infection Local threats Countries and territories where users faced the highest risk of local infection Authors AMR IT threat evolution in Q3 2026. Non-mobile statistics IT threat evolution in Q3 2026. Mobile statistics The statistics in this report are based on detection verdicts returned by Kaspersky products unless otherwise stated. The information was provided by Kaspersky users who consented to sharing statistical data. Quarterly figures In Q3 2026: Kaspersky products blocked more than 311 million attacks launched from online resources. Web Anti-Virus responded to 47 million unique links. File Anti-Virus blocked more than 23 million malicious and potentially unwanted objects. There were 4470 new ransomware variants discovered. More than 81,000 users experienced ransomware attacks. 15% of all ransomware victims whose data was published on threat actors’ data leak sites (DLSs) were victims of Qilin. More than 217,000 users were targeted by miners. Ransomware Quarterly trends and highlights Threat actor disruption In August, the creator and lead administrator of the Ransom Cartel ransomware-as-a-service (RaaS) operation was sentenced to 16 years in prison. The convict developed the ransomware Trojan and at the time of his arrest played a central role in the RaaS operation: running the affiliate program, recruiting affiliates, supplying them with information and attack tools, working with initial access brokers, communicating with victims, and processing payments. In September, a member of the Ryuk RaaS group was sentenced to two years in prison and three years of supervised release. In 2019 and 2020, he and his accomplices breached organizations’ networks and encrypted data with the Ryuk Trojan. According to public reports, hundreds of workstations and servers were compromised. According to the prosecution, the attacker received a total of about 1610 BTC in ransom payments from victims. Also in September, a member of the Conti RaaS group was sentenced to four years in prison. He was charged with attacking companies in 2021 and 2022. In addition to carrying out attacks, he developed part of the group’s malware toolkit. Vulnerabilities and attacks In July, researchers published a report on the Qilin group exploiting the CVE-2026-0257 vulnerability in Palo Alto Networks firewall software. The vulnerability allowed attackers to bypass authentication and compromise victims’ networks without valid accounts. CISA published information in its Known Exploited Vulnerabilities Catalog (KEV) on several CVEs actively exploited by ransomware groups: CVE-2026-15409 / CVE-2026-15410 in SonicWall SMA1000 remote access gateways. CISA doesn’t specify which groups exploited these vulnerabilities, but researchers have linked this activity to INC Ransom. CVE-2026-45659 in Microsoft SharePoint Server allowed an authenticated, low-privileged attacker to achieve remote code execution. CVE-2025-60710 in Microsoft Windows allowed attackers to escalate privileges locally. CVE-2026-59310 in VMware vCenter enabled unauthenticated remote code ex
```

#### Corroborating sources (2)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: IT threat evolution in Q3 2026. Non-mobile statistics
  - Published: 2026-11-10T08:00:37+00:00
  - Link: https://securelist.com/malware-report-q3-2026-pc-iot-statistics/121843/
  - Summary: Key trends and statistics on malware targeting Windows and macOS computers and Internet of Things (IoT) devices in Q3 2026.
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Macfinger ClickFix campaign sends DownTheDRAIN infostealer for macOS, (Fri, Nov 13th)
  - Published: 2026-11-13T03:41:41+00:00
  - Link: https://isc.sans.edu/diary/rss/33518
  - Summary: Introduction

### Cluster 608d640230 — score 12

- Title: 56 AWS API calls in 141 milliseconds: Inside an AI-run intrusion
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-11-13T15:27:20+00:00
- Link: https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- affected_products: AWS
- tools_used: Fortinet
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: AWS
- tools_used: Fortinet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A CyberStrikeAI server spent 16 days in four AWS accounts using eight identities, and the CloudTrail record shows why six detection rules each caught only part of it.
```

#### Full body

```
Threat Command 56 AWS API calls in 141 milliseconds: Inside an AI-run intrusion A CyberStrikeAI server spent 16 days in four AWS accounts using eight identities, and the CloudTrail record shows why six detection rules each caught only part of it. November 13, 2026 Samir Bousseaden Bryan Porras Blanch Terrance DeJesus Threat Intelligence Detection Engineering + 1 Jump to Share One server read 56 EC2 user data scripts in 141 milliseconds. Then it went quiet for 14 days and came back. That gap did more damage than the burst, because fixed correlation windows cannot span two weeks. Between September 30 and October 16, 2026, a CyberStrikeAI server worked through stolen AWS credentials in a familiar sequence: validate identities, harvest secrets from Secrets Manager, pull EC2 user data, decrypt an SSM parameter, send a remote command. Every one of those is a call a legitimate role makes every day. Nothing in CloudTrail looked urgent at the time. CyberStrikeAI is an open-source platform that pairs LLM agents with offensive security tools. Will Thomas at Team Cymru counted 21 IPs running it in early 2026 , all of them aimed at Fortinet edge devices. This is the first case we have seen of the same tooling turned on AWS. We call this AI-assisted on the strength of the tool attribution and the machine-speed behavior in the logs. We cannot prove an LLM agent was making the decisions, and we do not know how the attacker obtained the credentials. Key findings from the CyberStrikeAI AWS intrusion Between Sep 30 and Oct 16, 2026, one CyberStrikeAI server (43[.]240[.]29[.]11) used credentials from eight AWS identities (five IAM users and three EC2 instance roles) across four accounts and generated 78 alerts. app-role sent 56 user data requests in 141 milliseconds, part of 58 user data retrieval alerts (74% of the total), which points to automated tooling. On Oct 2, container-role read an encrypted SSM parameter and issued an SSM SendCommand 29 seconds later. The audit log does not show what the command was or whether it succeeded. 43[.]240[.]29[.]28 and 43[.]240[.]29[.]33 serve a CyberStrikeAI page on port 8080 with the same self-signed certificate as 43[.]240[.]29[.]11, which ties the three servers together. As of November, none of the three is serving that interface, so treat the IPs as indicators for retrospective hunting. All 78 alerts were medium or low severity and only made sense once correlated by source IP. How the CyberStrikeAI server moved through four AWS accounts Threat infrastructure and the eight AWS identities used One CyberStrikeAI server used credentials belonging to eight IAM identities across four AWS accounts over 16 days, with activity on four of those days. Account and identity names are replaced with aliases. Attribute Value Source IP 43[.]240[.]29[.]11 Attribution CyberStrikeAI server (confirmed) Target cloud AWS Accounts involved 4 (Accounts A to D) IAM identities used 8 EC2 instances whose role credentials were used 3 Total alerts 78 Campaign duration 16 days (Sep 30 to Oct 16) Alias Type Account Actions Alerts Active window app-role EC2 instance role A GetSecretValue, DescribeInstanceAttribute 60 Sep 30 to Oct 1 logship-user-1 IAM user A, C GetCallerIdentity 5 Sep 30 to Oct 16 logship-user-2 IAM user B GetCallerIdentity 3 Sep 30 to Oct 16 email-svc-user IAM user A GetCallerIdentity, GetSessionToken 3 Sep 30 nonprod-role EC2 instance role A GetSecretValue 2 Oct 1 cert-renew-user IAM user A GetCallerIdentity 2 Sep 30 to Oct 1 container-role EC2 instance role A GetParameter, SendCommand 2 Oct 2 named-user IAM user D GetSessionToken 1 Oct 16 The three role sessions were named after EC2 instance IDs, so the credentials came from instance profiles. Using them from an outside IP means they were taken from the instances, for example through SSRF or host compromise. How we attributed the IP to CyberStrikeAI Internet scan data shows 43[.]240[.]29[.]11 serving a CyberStrikeAI web interface with a self-signed CyberStrikeAI cert
```

#### Corroborating sources (3)

- **Elastic Security Labs** (detection_response_operations)
  - Title: 56 AWS API calls in 141 milliseconds: Inside an AI-run intrusion
  - Published: 2026-11-13T15:27:20+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion
  - Summary: A CyberStrikeAI server spent 16 days in four AWS accounts using eight identities, and the CloudTrail record shows why six detection rules each caught only part of it.
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Digital sovereignty at re:Invent 2026: Sessions you won’t want to miss
  - Published: 2026-11-10T18:10:41+00:00
  - Link: https://aws.amazon.com/blogs/security/digital-sovereignty-at-reinvent-2026-sessions-you-wont-want-to-miss/
  - Summary: AWS re:Invent returns to Las Vegas for cloud and AI’s biggest week from November 30–December 4, 2026. This year we have over 2,200 sessions, 70 percent of which are interactive, led by experts from Amazon Web Services (AWS), our customers, and our partners. With that much to choose from, we’ve pulled together the sessions built […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: AntiFox AI Pentesting Platform Linked to Attacks That Accessed AWS Production Secrets
  - Published: 2026-11-11T15:34:27+00:00
  - Link: https://thehackernews.com/2026/11/antifox-ai-pentesting-platform-linked.html
  - Summary: Cybersecurity researchers have disclosed details of a campaign in which an emerging agentic penetration testing platform called AntiFox has been used to steal Amazon Web Services (AWS) credentials and pivot laterally into compromised environments. "In several recently observed intrusions, Alibaba Cloud systems hosting AntiFox interfaces were associated with confirmed malicious actions against

### Cluster 6411ea2e82 — score 11

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

### Cluster 250249bdb2 — score 11

- Title: Shadow AI Generated Apps: Find Them in the Cloud and Code You Already Scan
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-11-10T13:00:00+00:00
- Link: https://orca.security/resources/blog/shadow-ai-generated-apps-find-them-in-the-cloud-and-code-you-already-scan/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2025-48757

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude
- cve_ids: CVE-2025-48757
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Anthropic/Claude
- cve_ids: CVE-2025-48757
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The Orca Research Pod recently found that 51% of organizations have adopted AI to build software, yet 81% have critical vulnerabilities in AI packages (Hacker Valley News, 2026). In 2025, CVE-2025-48757 showed how a single missing database policy in AI-generated Supabase projects exposed data across more than 170 production apps. None of these apps went […]
```

#### Full body

```
The Orca Research Pod recently found that 51% of organizations have adopted AI to build software, yet 81% have critical vulnerabilities in AI packages ( Hacker Valley News , 2026). In 2025, CVE-2025-48757 showed how a single missing database policy in AI-generated Supabase projects exposed data across more than 170 production apps. None of these apps went through a pull request or a security review. People outside engineering built them, often over a weekend, from accounts the security team had never seen. When we introduced AI AppGen Security , we made the case that AI app builders turned every employee into a builder, and that the platforms those apps run on need security built for how they work. We started with integrations for Claude Enterprise and Vercel. The first question we heard from security teams: how do I connect a platform I don’t know we use? Nobody files a ticket for a budget-forecasting app built on Lovable, and the marketing team’s campaign portal never reached architecture review. You can’t connect what you’ve never heard of. AI app builders leave fingerprints in the DNS, workloads, code, and cloud identities Orca already scans agentlessly. Orca now flags them, so you can find AI-built apps nobody told you about and see what data they can reach. Below, we walk through why your current tools miss these apps, how Orca finds them, and what to do once you know. Why the usual discovery paths miss AI-generated apps You’d expect at least one of your existing tools to catch these apps. Here’s why none of them do. Secure web gateways and CASBs see the visit, not the app. They can tell you an employee opened Lovable or Replit. They can’t tell you what was deployed, what data it holds, or whether it requires a login. SSPM sees sign-ups through your identity provider. It reads IdP logs and OAuth grants, which shows the SaaS your employees signed up for with a work email. An app built from a personal account never touches your IdP. AppSec scans the repositories you point it at. If a builder’s bot created the repo in a workspace security has never seen, nobody points anything at it. Cloud security sees the evidence but doesn’t connect it to the service. A CNAPP already inventories the DNS record, the IAM user, and the package on the VM. Until now, a subdomain resolving into a builder’s IP range was just an address, and an IAM user created by an app builder was just an IAM user. The data was there. Nothing tied it to the service behind it. Every one of these tools waits for someone to connect a system, a user, or a repo first. The apps that matter most are the ones nobody connected to. How does Orca find apps nobody reported? Services that run outside your environment still leave traces inside it. Orca already scans your cloud accounts, workloads, repositories, and external attack surface, so the traces are already in its data. A fingerprint is an observed trace that ties an asset you own to an external service. Orca stores each one in its unified data model, where you can query it like any other asset. Each one records the service, the type of evidence, the exact value that matched, and when Orca first saw it. To find these fingerprints, there’s no new agent to deploy, no vendor API to authorize, and nothing for the builder to opt into. Here’s where the evidence comes from: Your external attack surface. DNS records whose values point into a builder’s or host’s infrastructure, vendor domain-verification records, and response headers showing a site is set up to load inside a builder’s live editor. Your workloads. SideScanning already inventories installed packages and reads files across VMs and container images. Some builder packages only work inside the builder’s own development environment, so if one shows up on a workload, the project started there. File markers matter as much as packages, because production builds often strip out dependency manifests. Without file markers, package inventory can come back empty on the ver
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Shadow AI Generated Apps: Find Them in the Cloud and Code You Already Scan
  - Published: 2026-11-10T13:00:00+00:00
  - Link: https://orca.security/resources/blog/shadow-ai-generated-apps-find-them-in-the-cloud-and-code-you-already-scan/
  - Summary: The Orca Research Pod recently found that 51% of organizations have adopted AI to build software, yet 81% have critical vulnerabilities in AI packages (Hacker Valley News, 2026). In 2025, CVE-2025-48757 showed how a single missing database policy in AI-generated Supabase projects exposed data across more than 170 production apps. None of these apps went […]

### Cluster 37e6854c04 — score 11

- Title: Recent UnrealIRCd Vulnerability Exploited in Attacks
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-16T11:15:48+00:00
- Link: https://www.securityweek.com/recent-unrealircd-vulnerability-exploited-in-attacks/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-114713

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, supply_chain, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, GitHub
- cve_ids: CVE-2026-114713, CVE-2026-123039
- urgency_signals: poc_available, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft, zero_day, data_breach
- affected_industries: government
- affected_products: Anthropic/Claude, GitHub
- cve_ids: CVE-2026-114713, CVE-2026-123039
- urgency_signals: zero_day, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Tracked as CVE-2026-114713, the high-severity flaw allows attackers to execute commands with server/IRCOp privileges. The post Recent UnrealIRCd Vulnerability Exploited in Attacks appeared first on SecurityWeek .
```

#### Full body

```
Threat actors started exploiting a high-severity vulnerability in the open source Internet Relay Chat (IRC) server UnrealIRCd one day after public disclosure. Tracked as CVE-2026-114713 (CVSS score: 8.6), the flaw is described as an improper neutralization of delimiters and allows attackers to execute commands with server/IRCOp privileges. The issue exists because the labeled-response module “does not escape the IRCv3 ‘label’ message tag when echoing it into replies, which allows any user on a network with two or more linked servers to inject server-to-server commands that are executed with server authority,” according to a NIST advisory . Patches for CVE-2026-114713 and eight other bugs were released on November 7 in UnrealIRCd version 6.2.7.1. A hot patch was also rolled out. According to UnrealIRCd project leader, developer, and maintainer Bram Matthys, this is the most severe security defect discovered in UnrealIRCd. “Any ordinary user can KILL, GLINE, and do many more bad things. This is the most critical issue found in UnrealIRCd in the past 15 years,” Matthys said . Advertisement. Scroll to continue reading. Matthys has provided instructions on how to update to UnrealIRCd 6.2.7.1 or apply the hot patch and warned that UnrealIRCd 5 and previous releases have reached End of Life (EoL) and won’t receive a fix. “It is likely that several bugs that are fixed in 6.2.7.1 go all the way back to 3.2.x,” Matthys said. On November 8, he warned that hackers had already started probing vulnerable UnrealIRCd instances, urging immediate patching. “We are seeing bad guys exploiting this issue on the internet right now. Hopefully everyone has hot-patched or updated their server, or at the very least has the spamfilter workaround deployed. If not, do so ASAP,” Matthys said. On November 13, the US cybersecurity agency CISA added CVE-2026-114713 to its Known Exploited Vulnerabilities ( KEV ) list, giving federal agencies only three days to address it, in line with BOD 26-04 requirements. CISA also added CVE-2026-123039 to KEV. A high-severity flaw affecting multiple Check Point products, it has been exploited in destructive attacks against Israeli organizations, Check Point warned last week. Related: Citrix Patches 10 Critical NetScaler Vulnerabilities Related: Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’ Related: Hackers Exploit New N-central Zero-Day Hours After PoC Publication Related: Apache Patches Critical HTTP Server RCE Found by Anthropic, Google Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Law Enforcement Disrupts Gootloader, CastleRAT, and StealC Infrastructure Citrix Patches 10 Critical NetScaler Vulnerabilities Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’ PHP2Shell Exploited in Destructive Check Point Gateway Attacks Hackers Exploit New N-central Zero-Day Hours After PoC Publication Chrome, Firefox Updates Patch Over 180 Vulnerabilities Daylight Lands $80 Million for AI-Powered Security Operations Notion Customer Data Compromised in Fireworks AI Hack Latest News Trump Administration Moves to Block China From Indirect Access to American AI Technology Cursor Supply Chain Attack Started at Fireworks AI Google Project Zero Sets Course for 30-Day Disclosure Deadline Barracuda Hacked Amid Surge in Artex-Powered Cyberattacks Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch Hackers Probe Newly Disclosed Flaws in Copeland Refrigeration Controllers Uber Data Breach Impacts 150,000 People Tor Updates DoS Defenses Again as Relay Attacks Continue Trending Attacker Targets 60,000 GitHub Repositories in Credential Theft Campaign Amplifier Security Emerges From Stealth With AI Copilot, Human-in-the-Loop Automation No Signs of Hacking in FAA Ground Stop as FBI Reportedly Probes Software Upda
```

#### Corroborating sources (2)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Recent UnrealIRCd Vulnerability Exploited in Attacks
  - Published: 2026-11-16T11:15:48+00:00
  - Link: https://www.securityweek.com/recent-unrealircd-vulnerability-exploited-in-attacks/
  - Summary: Tracked as CVE-2026-114713, the high-severity flaw allows attackers to execute commands with server/IRCOp privileges. The post Recent UnrealIRCd Vulnerability Exploited in Attacks appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit UnrealIRCd Flaw That Enables Server-Level Command Injection
  - Published: 2026-11-14T12:38:35+00:00
  - Link: https://thehackernews.com/2026/11/attackers-exploit-unrealircd-flaw-that.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday added a high-severity security flaw impacting UnrealIRCd, an open-source Internet Relay Chat (IRC) server, to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation. The vulnerability, tracked as CVE-2026-114713 (CVSS score: 8.6), is a case of improper neutralization of delimiters

### Cluster d59d57a2e0 — score 11

- Title: Unpatched GeoVision camera software gave cryptojackers a side door into 13 organizations
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-11-16T10:07:57+00:00
- Link: https://www.helpnetsecurity.com/2026/11/16/geovision-camera-software-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, cryptojacking
- affected_industries: financial_services
- affected_products: Microsoft Defender
- cve_ids: CVE-2024-11120, CVE-2024-6047
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: cryptojacking, active_exploitation
- affected_industries: financial_services
- affected_products: Microsoft Defender
- cve_ids: CVE-2024-6047, CVE-2024-11120
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Attackers used GeoVision camera management software to break into Windows machines at 13 organizations and turn them into cryptocurrency miners, Huntress warned in a threat advisory. GeoVision is a Taiwanese surveillance and access control company with customers in 110 countries. The victims work in various industries, and most of the intrusions happened between November 8 and 10. Every time, the activity started with a service that belongs to GeoVision’s software, and a Shodan search of … More → The post Unpatched GeoVision camera software gave cryptojackers a side door into 13 organizations appeared first on Help Net Security .
```

#### Full body

```
Sinisa Markovic , Managing Editor, Help Net Security November 16, 2026 Share Unpatched GeoVision camera software gave cryptojackers a side door into 13 organizations Attackers used GeoVision camera management software to break into Windows machines at 13 organizations and turn them into cryptocurrency miners , Huntress warned in a threat advisory. GeoVision is a Taiwanese surveillance and access control company with customers in 110 countries. The victims work in various industries, and most of the intrusions happened between November 8 and 10. Every time, the activity started with a service that belongs to GeoVision’s software, and a Shodan search of the victims’ external IP addresses turned up GeoVision devices and management interfaces exposed to the internet. Antivirus disabled, miner installed After getting in, the attackers ran a series of scripts that checked whether Microsoft Defender was running. One of them downloaded a kernel driver that had been abused before in bring-your-own-vulnerable-driver (BYOVD) attacks to tamper with antivirus software. “At this stage of the attack, we also observed attackers configuring three IFEO Debugger hijacks, which abuse a Windows troubleshooting feature. Image File Execution Options (IFEO) lets administrators configure a “debugger” to start when a particular executable is launched. The setting is stored in the Windows Registry under a key named for that executable,” the researchers wrote. The hijacks redirected three Windows security processes to systray.exe, most likely to stop them from starting. The attackers then installed a custom loader, which on some machines was set to run every 15 minutes and at boot. The loader downloaded XMRig, an open-source cryptominer popular with threat actors. An outdated build with known flaws The advisory didn’t name a vulnerability, CVE or product version. Past in-the-wild exploitation of GeoVision products, such as CVE-2024-6047 and CVE-2024-11120 , targeted end-of-life embedded devices, so Help Net Security asked Huntress whether the affected hosts were running supported, up-to-date GeoVision releases, and whether the attacker used a known flaw, an undisclosed one, or weak or default credentials. A review of a sample of the affected hosts found they were running GV-VMS 17.4.8.0, a build compiled on April 24, 2024, Anthony Gibbs, Security Operations Analyst at Huntress, told Help Net Security. That version is older than V17.4.8.58, GeoVision’s fixed release. “GeoVision’s April 2026 advisory identifies three unauthenticated remote-code-execution vulnerabilities in the WebCam Server functionality affecting this version (GV-VMS 17.4.8.0), making exploitation of a known flaw the most likely explanation,” said Austin Worline, Senior Security Operations Analyst at Huntress. “We haven’t determined at this time, which of the three CVEs was used or confirmed whether GeoVision considered these installations supported,” Worline added. A loader built to outlast its servers The loader includes a BitTorrent Mainline DHT client and a PKARR resolver, which let the operator find current server addresses through a public key and move to new infrastructure without losing access to the infected machines. We asked Huntress whether it had seen this technique in other cryptomining campaigns, and whether it suggests the operator wants to keep these footholds for other purposes, such as selling access. “We’d describe the loader as botnet-like: its DHT and PKARR capabilities let the operator find updated server addresses and deliver new payloads. The resilience goal is similar to EtherHiding, though the mechanism differs: this loader uses BitTorrent DHT and PKARR for server discovery,” Gibbs explained. “In this activity, we observed it downloading XMRig. The ability to retrieve other payloads could support uses beyond mining, including potentially selling access, but we have not seen evidence that access was sold or used for another purpose in these incidents.” “Personall
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Unpatched GeoVision camera software gave cryptojackers a side door into 13 organizations
  - Published: 2026-11-16T10:07:57+00:00
  - Link: https://www.helpnetsecurity.com/2026/11/16/geovision-camera-software-vulnerabilities/
  - Summary: Attackers used GeoVision camera management software to break into Windows machines at 13 organizations and turn them into cryptocurrency miners, Huntress warned in a threat advisory. GeoVision is a Taiwanese surveillance and access control company with customers in 110 countries. The victims work in various industries, and most of the intrusions happened between November 8 and 10. Every time, the activity started with a service that belongs to GeoVision’s software, and a Shodan search of … More → The post Unpatched GeoVision camera software gave cryptojackers a side door into 13 organizations appeared first on Help Net Security .

### Cluster a4a11d6f47 — score 11

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

### Cluster 06bffa03c1 — score 11

- Title: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-13T16:53:08+00:00
- Link: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-6460

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-116322, CVE-2026-6460
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-6460, CVE-2026-116322
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server. The flaw, tracked as CVE-2026-6460, has a CVSS score of 8.8. Any code run this way has the rights of the operating
```

#### Full body

```
PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE  Swati Khandelwal  Nov 13, 2026 Vulnerability / Database Security A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server. The flaw, tracked as CVE-2026-6460 , has a CVSS score of 8.8. Any code run this way has the rights of the operating system user that runs PostgreSQL. All versions before 18.7, 17.12, 16.16, 15.20, and 14.25 are affected. The PostgreSQL Global Development Group, which publishes the database's releases, has not reported any attacks using the flaw. CISA's assessment in the CVE record also lists exploitation as none. The flaw involves composite types, which are types built from named fields, each with its own data type. A field's type can be changed while older values of that type are still held in other parts of the server. The server could then read an old value as if it had the new type. The fix, described in the project's release notes , adds version checks so the server can detect a value that no longer matches its type. Security researcher Mehmet Ince described a working exploit for the flaw, demonstrated on PostgreSQL 18.6, in a technical writeup published this week. His method is to prepare a query that holds a value, change the type of one of the value's fields, and then run the query. The writeup includes the SQL that crashes an unpatched server this way and a second step that leaks memory addresses. It does not include the SQL for the final step, which makes the server run a command. He wrote that he could "trigger this crash as a lowest-privileged login role." The project's security advisory describes the attacker only as someone who can create objects, without saying which privileges that takes. Red Hat, which ships PostgreSQL packages, says in its CVE assessment that an attacker needs a database login with the ability to create or modify objects. None of these sources says whether an account with only default privileges can go beyond the crash to run code. Ince traces the root of the flaw to May 5, 2004, when PostgreSQL gained the ability to change a column's type. His technique for running code relies on a later change made on May 14, 2015. He also adapted the exploit for managed PostgreSQL services and privately shared proofs of concept with their security teams in August. The providers he worked with include AWS (Aurora and RDS), Microsoft (Azure PostgreSQL), Google (AlloyDB), Supabase, Databricks, and Ubicloud. The writeup does not give each service's current patch status. The project credits more than a dozen reporters for CVE-2026-6460 , including the researcher, and credits him on five other flaws in the same release. The project rates 32 of the 52 flaws at 8.8, the highest score in the release. Based on the scores in its vulnerability index , only one flaw in the server requires neither a login nor any user action. That flaw, CVE-2026-116322 , lets an unauthenticated client trigger a restart of PostgreSQL 18 servers. Several other fixes are in client tools. A crafted archive can make pg_restore run code as the user running it. A compromised source server can make psql run code through the restore script in pg_dump's tar output. What Administrators Should Do Update the server to 18.7, 17.12, 16.16, 15.20, or 14.25, matching your major version. Rebuild or update every C-language extension at the same time as the server. Extensions built against older releases still load, but they "may not be protected from the vulnerabilities fixed in this release," according to a repository notice from the project's RPM package maintainers. Some extensions will also need source-code changes. Extensions rebuilt for the new releases can fail to load on older servers. Extension packages in the project's RP
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE
  - Published: 2026-11-13T16:53:08+00:00
  - Link: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
  - Summary: A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server. The flaw, tracked as CVE-2026-6460, has a CVSS score of 8.8. Any code run this way has the rights of the operating
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: prepared statements prevents SQLi. But it also helped me to exploit a 22 years old PostgreSQL 0-day RCE (CVE-2026-6460)
  - Published: 2026-11-12T16:21:24+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xuh3jj/prepared_statements_prevents_sqli_but_it_also/
  - Summary: submitted by /u/wtfse [link] [comments]

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

### Cluster 5b374473ad — score 10

- Title: The global socket: how threat actors are weaponizing GSocket for stealthy C2
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-11-11T19:49:57+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Defender
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Microsoft Defender
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Threat actors are deploying GSocket on compromised Linux servers to keep encrypted remote access after the original vulnerability is patched. Learn how to detect, investigate, and remediate this activity. The post The global socket: how threat actors are weaponizing GSocket for stealthy C2 appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Linux Threats intelligence Cyberattacker techniques, tools, and infrastructure Vulnerabilities and exploits Content types Research Products and services Microsoft Defender Topics Actionable threat insights Threat intelligence Microsoft observed multiple incidents in which threat actors deployed GSocket, an open source remote access tool, on compromised Linux servers. Threat actors used Gsocket to maintain access even after the vulnerabilities used for initial compromise were remediated. This turned a single web application compromise into persistent access that outlasted the remediation of the original vulnerabilities. Defenders investigating affected hosts should look for evidence of GSocket deployment, persistence, privilege escalation, and outbound connections, rather than treating application patching alone as complete remediation. Microsoft Defender for Endpoint telemetry shows this activity growing over recent months and concentrated on web applications and hosting environments. GSocket relays traffic through a shared public network, so there is no threat actor-owned IP address or domain to block. When one RCE stops being just one RCE Exploiting a web application vulnerability gives a threat actor command execution in the context of the web server process. That access lasts only while the vulnerability remains unpatched and the service keeps running. Patching the application or restarting the service can remove it. To keep access, threat actors typically add a persistence mechanism, and each common option has drawbacks. SSH keys added to authorized_keys are easy for administrators to find during an audit. Reverse shells depend on threat actor-controlled servers that defenders can block or sinkhole. Custom implants require ongoing development and maintenance. The same trade-offs apply when initial access comes through remote access services or cloud shell sessions. GSocket addresses these drawbacks, which helps explain why multiple unrelated threat actors have adopted it. Shared relay infrastructure. Traffic passes through the Global Socket Relay Network, a public relay service. The threat actor does not register or host any infrastructure, so there is no threat actor-owned IP address or domain to block. Organizations can still restrict access to the relay itself. Outbound-only connections. The compromised host and the operator both connect outbound to the relay, which bridges the two sessions. The host needs no inbound listener or public IP address, and network address translation does not prevent the connection. Inbound firewall rules do not see this traffic, although egress filtering and outbound monitoring can. Built-in evasion and persistence. The deployment script can rename the process, stage files in memory-backed directories, and install persistence that survives a reboot, without additional development by the threat actor. The same relay model that supports legitimate remote administration also gives threat actors a way to maintain access without operating dedicated C2 infrastructure. Once GSocket runs on a compromised server, the server and the operator each connect outbound to the Global Socket Relay Network, which pairs the two sessions over an end-to-end encrypted channel. Figure 1: After code execution on an internet-facing application, GSocket is deployed and both ends connect outward to the relay. Because GSocket runs independently of the exploited application, patching the vulnerability does not remove the relay client or its persistence. Microsoft Defender for Endpoint telemetry shows that this activity is not limited to a single compromise. From March through August 2026, devices with GSocket-related detections increased 356.2%, although the increase was not consistent month to month. Figure 2: Growth in GSocket-related detections from March to August, measured against the March baseline. Web applications and hosting accounted for 87.1% of attributable Microsoft Def
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: The global socket: how threat actors are weaponizing GSocket for stealthy C2
  - Published: 2026-11-11T19:49:57+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/
  - Summary: Threat actors are deploying GSocket on compromised Linux servers to keep encrypted remote access after the original vulnerability is patched. Learn how to detect, investigate, and remediate this activity. The post The global socket: how threat actors are weaponizing GSocket for stealthy C2 appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: The global socket: how threat actors are weaponizing GSocket for stealthy C2
  - Published: 2026-11-11T19:49:57+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/
  - Summary: Threat actors are deploying GSocket on compromised Linux servers to keep encrypted remote access after the original vulnerability is patched. Learn how to detect, investigate, and remediate this activity. The post The global socket: how threat actors are weaponizing GSocket for stealthy C2 appeared first on Microsoft Security Blog .

### Cluster 6cd0ca5dbb — score 10

- Title: Detecting sleeper agents hiding in AI model neurons
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-11-10T23:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/11/10/detecting-sleeper-agents-hiding-in-ai-model-neurons/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Research has released new threat research detailing how a capable agent model could be turned into a sleeper agent by editing fewer than ten neurons to inject a short payload; Microsoft Research has also found that this threat is detectable by frontier agents, which can identify anomalous weight edits. The post Detecting sleeper agents hiding in AI model neurons appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Threats intelligence AI threats Content types Research Topics Threat intelligence Microsoft Research has released new threat research detailing how a capable agent model could be turned into a sleeper agent by editing fewer than 10 neurons to inject a short payload. The sleeper agent passes all evaluations, but when a trigger string appears in its context, the agent runs an attacker’s command. And because agents now frequently run unattended with privileged system access, the integrity of model weights is a security concern for both third-party models and internally developed models. Key findings from Microsoft Research include: Software abuse and manipulation are familiar threats. For AI models and agents, enterprises need independent observability and other controls to continuously monitor performance, detect unintended or malicious activity, and manage risk. Satya Nadella recently outlined this approach in a blog post . A backdoored model can pass evaluations. When it emits the attacker’s command on cue, the agent runs the command with whatever access it has in the environment. The attack needs inference-only compute. If a machine has enough RAM to run a model, it has enough resources to weight-space backdoor it. Claude Code with Opus 4.5 discovered most of this threat autonomously. Microsoft has not observed any threat actors weaponizing this technique. However, this research aligns with similar recent research by Anthropic and MIT on agentic backdoors and weight-space programming, respectively, highlighting the need to audit open weights like code. Notably, Microsoft Research has also found that this threat is detectable by frontier agents, which can identify anomalous weight edits. Using frontier agents as auditors can help automate the defense against this threat. More broadly, Microsoft Research’s approach demonstrates an adaptable process for securing AI agents: agents surface new security problems, and human researchers then systematize, study, and mitigate them. Learn more from the Microsoft Research Blog: Lazare, veni foras: Reprogramming dormant neurons to backdoor AI agents Mitigation and protection guidance Microsoft recommends the following mitigations to defend against this threat as part of a broader defense-in-depth approach. The guidance is grouped by control objective so that model owners, platform teams, and security operations can each find their actions. Audit model weights before deployment and after every update Diff every checkpoint against its declared base model before deployment and after each update. Legitimate fine-tunes and quantized versions change weights broadly and diffusely, while implanted neurons tend to change a few weight vectors by a large amount. Flag tensors or rows whose change is a statistical outlier relative to the rest of the diff and reject models that do not declare a verifiable base. Use frontier AI agents as auditors in the model intake pipeline. Microsoft Research found they are highly effective at finding anomalous structure in weights that manual inspection misses, which makes this step automatable at scale. Complement weight diffing with behavioral backdoor scanning of open-weight models, as described in Microsoft’s research on detecting backdoored language models at scale . Record audit results alongside the model in the registry, and state clearly to internal consumers that passing an audit reduces risk but does not guarantee safe behavior. Secure model hubs and publishers Display provenance and audit status publicly before a checkpoint can be downloaded or served through an API. Scan every upload for anomalous neurons, weight patterns or behaviors, and state clearly that third-party checkpoints can be unsafe and that passing an audit does not guarantee safe behavior. Treat every third-party model as untrusted until audited Source checkpoints only from the original publisher, verify the publisher’s published file hashes, and treat all t
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Detecting sleeper agents hiding in AI model neurons
  - Published: 2026-11-10T23:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/10/detecting-sleeper-agents-hiding-in-ai-model-neurons/
  - Summary: Microsoft Research has released new threat research detailing how a capable agent model could be turned into a sleeper agent by editing fewer than ten neurons to inject a short payload; Microsoft Research has also found that this threat is detectable by frontier agents, which can identify anomalous weight edits. The post Detecting sleeper agents hiding in AI model neurons appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Detecting sleeper agents hiding in AI model neurons
  - Published: 2026-11-10T23:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/10/detecting-sleeper-agents-hiding-in-ai-model-neurons/
  - Summary: Microsoft Research has released new threat research detailing how a capable agent model could be turned into a sleeper agent by editing fewer than ten neurons to inject a short payload; Microsoft Research has also found that this threat is detectable by frontier agents, which can identify anomalous weight edits. The post Detecting sleeper agents hiding in AI model neurons appeared first on Microsoft Security Blog .

### Cluster 467554e7d8 — score 10

- Title: ARTEX and AI-Powered Red Teaming Tools: What Defenders Need to Know
- Source: Unit 42 (threat_research_primary)
- Published: 2026-11-11T23:00:53+00:00
- Link: https://unit42.paloaltonetworks.com/artex-and-ai-powered-red-teaming-tools/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: retail_ecommerce
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: retail_ecommerce
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Learn what Unit 42 discovered about attacker use of AI-powered red team tools, and how to mitigate these attacks. The post ARTEX and AI-Powered Red Teaming Tools: What Defenders Need to Know appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights General General ARTEX and AI-Powered Red Teaming Tools: What Defenders Need to Know 6 min read Related Products Cortex Cortex XDR Cortex XSIAM Unit 42 Deep and Dark Web Service Unit 42 Incident Response Unit 42 Threat Intelligence Services By: Cuong Dinh Richard Emerson Samantha Stallings Ofek Lahiani Ben Magee Published: November 11, 2026 Categories: General Insights Tags: GenAI LLM Penetration testing Share A rapidly expanding ecosystem of AI-enabled tools such as ARTEX and CyberStrikeAI — marketed for red teaming and penetration testing — are being used by attackers to execute offensive operations autonomously. Their footprint is already substantial. Unit 42 has observed ARTEX used in intrusion attempts against multiple targets . Our Incident Response team investigated multiple intrusions in which the attacker’s server hosted an ARTEX console or used infrastructure and user agents associated with ARTEX. Separately, Unit 42 Managed Threat Hunting tracked a coordinated ARTEX campaign against customer cloud environments in sectors worldwide, including retail and consulting. External scrutiny has already disrupted project lifecycles: the author of ARTEX recently made the repository closed-source and ceased public development to prevent misuse . Emerging alternatives are rapidly filling the void, introducing new capabilities that threat actors will inevitably co-opt. Here, we share our observations of how attackers are using AI-powered red team tools, along with our recommendations for how defenders can mitigate. Why Is ARTEX Such an Effective Tool for Attackers? ARTEX and other red-teaming platforms are free, quick to deploy and need little more than access to a large language model (LLM). ARTEX is an open-source, multi-agent AI penetration testing framework first published in mid-2026. It has been widely forked since. Attackers can use ARTEX to evaluate responses, adapt when something fails and keep pursuing their objective. They can target the identity workflows and APIs that organizations expose to the internet, and then use the associated credentials and trust relationships to reach the cloud. AI-Powered Red Teaming and Pentesting Ecosystem Infrastructure As of October 2026, Unit 42 identified 1,323 internet-facing hosts running CyberStrikeAI and 609 running ARTEX. Notably, 21 hosts were running both at the same time. Unit 42 analyzed 14 tools across the pentesting and red-teaming tool ecosystem, highlighting 12 emerging tools alongside CyberStrikeAI and ARTEX. These tools can be broken down into four categories of AI assisted red team activities. Category Tools Goal Reconnaissance and attack-surface management ARL, ARL-Next, Scope Sentry, Nemo, XingRin, OpenEASD Identify what assets exist, what is exposed and what changes Agent-led testing and vulnerability hunting CyberStrikeAI, ARTEX, Cairn, PentAGI, AutoHunter Manage what should be investigated and how the system can act on it Source-code auditing and verification DeepAudit, AIxVuln Identify where source code might be vulnerable and what supports that finding AI-system security assessment AI-Infra-Guard Identify if AI infrastructure, agents, tools and model interfaces are vulnerable or unreliable Table 1. Tool categories. Implications For Defenders Defenders should be aware of the following implications of AI-powered red teaming platforms: Lowered Skill Floor for Attackers Adversaries no longer require specialized tradecraft to execute multi-stage, adaptive penetration testing. Off-the-shelf tooling combined with LLMs like DeepSeek allows financially motivated actors to launch and manage dozens of complex, concurrent network intrusions for minimal compute cost. Risk of Internet-Exposed Assets Any internet-exposed asset, regardless of organizational size or sector, is equally likely to be impacted by automated, persistent intrusion attempts. Attackers using the autonomous AI penetration testing framework ARTEX are turning public password r
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: ARTEX and AI-Powered Red Teaming Tools: What Defenders Need to Know
  - Published: 2026-11-11T23:00:53+00:00
  - Link: https://unit42.paloaltonetworks.com/artex-and-ai-powered-red-teaming-tools/
  - Summary: Learn what Unit 42 discovered about attacker use of AI-powered red team tools, and how to mitigate these attacks. The post ARTEX and AI-Powered Red Teaming Tools: What Defenders Need to Know appeared first on Unit 42 .

### Cluster 568f4783d6 — score 10

- Title: LABScon26 Replay | Let’s Get Physical: Why Cybersecurity Needs Hardware-Based Security to Survive AI
- Source: SentinelOne Labs (threat_research_primary)
- Published: 2026-11-12T14:00:02+00:00
- Link: https://www.sentinelone.com/labs/labscon26-replay-let-s-get-physical-why-cybersecurity-needs-hardware-based-security-to-survive-ai/
- Fetch status: fetch_failed:HTTPError
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
Adyen’s Dino Dai Zovi shows how hardware security proven in payments can contain AI-driven attacks, even when vulnerabilities cannot be patched.
```

#### Corroborating sources (1)

- **SentinelOne Labs** (threat_research_primary)
  - Title: LABScon26 Replay | Let’s Get Physical: Why Cybersecurity Needs Hardware-Based Security to Survive AI
  - Published: 2026-11-12T14:00:02+00:00
  - Link: https://www.sentinelone.com/labs/labscon26-replay-let-s-get-physical-why-cybersecurity-needs-hardware-based-security-to-survive-ai/
  - Summary: Adyen’s Dino Dai Zovi shows how hardware security proven in payments can contain AI-driven attacks, even when vulnerabilities cannot be patched.

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

### Cluster 5d95fceb7e — score 10

- Title: Transcending the trust boundaries: how a cloud pentest works
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-12T10:00:53+00:00
- Link: https://securelist.com/how-a-cloud-pentest-works/121921/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Kubernetes

#### Cluster taxonomy (union across members)
- affected_products: Kubernetes
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Kubernetes
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
This is the first article in a series on cloud penetration testing. We'll cover the three cloud layers (External, Overlay, and Underlay), common architectures (OpenStack and Kubernetes), typical attack chains, and real-world incidents.
```

#### Full body

```
Content menu Close Subscribe Threat Response Table of Contents Key points Key terms What a pentester needs to check Cloud platform as a research target The hotel analogy and the three cloud layers Where the trust boundaries lie Attacker model and three research goals 1. Code execution first 2. Credentials first 3. Administrative or service context Sorting out the architectural zoo OpenStack-like infrastructure Kubernetes-based platforms Custom control plane and configuration management systems Mixed-stack platform How to choose the next trust boundary Typical attack chains and real-world incidents 1. From a managed database to other users’ data 2. From a Kubernetes pod to other users’ data 3. From a public operation to changes in internal cloud resources 4. Virtual machine escape What counts as a pentest result Safe confirmation of impact Conclusion What’s in the next article Authors Matvey Bukhtoyarov Denis Stepanov Kaspersky Security Services Users trust a cloud provider to configure and maintain their IT services, including data storage. In turn, the provider guarantees that hosted services will stay up and that data will remain strictly confidential. To demonstrate that their platforms are secure, providers choose different strategies: some run bug bounty programs, some rely on regular internal audits, and some bring in external research teams. However, cloud pentest methodology still has plenty of blind spots: there’s no single standard, and the outcome depends on the experience and skill of the team. Most pentests in this area have historically focused on the external layer: the management console, customer interfaces, APIs, and the basic network perimeter. This layer is important, but it’s only the surface. In this introductory article, we share our approach to penetration testing of cloud environments, which we’ve developed over several years and dozens of projects. We don’t claim to cover every possible scenario. Instead, we want to show the reasoning behind our pentests and highlight less obvious points that are easy to miss. Key points Cloud infrastructure is more complex than a traditional web application. To simplify, you can think of it as a hotel with three zones: the booking website (External, the outermost layer), the guest rooms (Overlay, the logical layer), and the staff area (Underlay, the infrastructure or base layer). A cloud service is well protected if the trust boundaries between these zones cannot be breached. A cloud pentest’s value isn’t measured by the number of vulnerabilities found or by the mere fact that code ran. Remote command execution in an isolated tenant container is only the beginning of a pentest, not the end. The main goal is to assess whether an attacker can violate trust boundaries. The assessment should answer five critical questions: Can an attacker read, modify, or delete other tenants’ data? Can they take over the provider’s IAM service account? Does compromising a runtime environment lead to the attack spreading to other resources and services? Can the provider’s internal resources be affected from low-trust segments? Is a virtual environment escape possible? A negative result is still a result. If a pentester cannot move from the tenant plane to the provider overlay, that is a valuable finding. It shows which protection boundaries work in practice and which rely only on assumptions and need additional controls. However, it does not prove that the trust boundary is impossible to cross or that no other attack paths exist. Key terms Below, we explain some specific terms that are most often used in cloud infrastructures. Show definitions Tenant (think of a renter in an apartment building) is a logically isolated unit within a cloud platform. Examples include a user (such as an organization), a separate project or cloud account, or another unit of administrative and resource isolation. Tenant plane is the set of IT services and data that a tenant manages directly: virtual machines,
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Transcending the trust boundaries: how a cloud pentest works
  - Published: 2026-11-12T10:00:53+00:00
  - Link: https://securelist.com/how-a-cloud-pentest-works/121921/
  - Summary: This is the first article in a series on cloud penetration testing. We'll cover the three cloud layers (External, Overlay, and Underlay), common architectures (OpenStack and Kubernetes), typical attack chains, and real-world incidents.

### Cluster ec59c47880 — score 10

- Title: Citrus Ransomware: VLESS for traffic, Sn00py for encryption, and LLMs lending a hand
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-11T10:00:25+00:00
- Link: https://securelist.com/citrus-ransomware/121879/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- cve_ids: CVE-2026-54121
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- cve_ids: CVE-2026-54121
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We break down the Citrus Ransomware group's attacks: the attackers' TTPs and tooling, including VLESS traffic tunneling and LLM use, plus their links to Toy Ghouls.
```

#### Full body

```
Content menu Close Subscribe Threat Response Table of Contents Initial Access: attacks through contractors Execution: commands, LLMs, and Impacket Persistence: scheduled tasks Privilege Escalation: vulnerabilities and configuration flaws Stealth: covering tracks and masquerading Defense Impairment: weak access policies for security tools play into attackers’ hands Credential Access: mimikatz, a keylogger, and extraction of credentials from files Discovery: the standard toolkit Local discovery Remote discovery Lateral Movement: SSH, RDP, and WinRM Command and Control: delivering tools to the system Creating tunnels with Xray Installing AnyDesk Collection & Exfiltration: data from messaging apps Impact: Sn00py ransomware Trojan Links to Toy Ghouls Conclusion Indicators of compromise Authors Stanislav Larinsky Vladislav Vlasov Boris Trefilov In recent years, cyberthreats have increasingly taken a hybrid approach, combining time-tested techniques for advancing through infrastructure, modern methods of evading network filters, and automation powered by large language models. This is also the approach of Citrus Ransomware, a previously undocumented group whose toolset includes VLESS tunnels (used to disguise traffic as regular HTTPS) and a ransomware Trojan from the Sn00py family. The attackers also integrate LLMs (large language models) into the process of infrastructure compromise. In this article, we review the tactics and techniques the group used in recent incidents. Initial Access: attacks through contractors The attackers gain initial access to victims’ infrastructure through compromised contractors. They use credentials stolen from these contractors’ employees to connect to corporate VPNs or directly to internet-facing terminal servers over RDP. Execution: commands, LLMs, and Impacket The attackers run commands on compromised systems through the standard Windows command interpreter and PowerShell. As the attack progresses, they create and run PowerShell scripts, batch files, and commands generated by LLMs. One example of the latter is the commands below, which disable the account of one of the administrators. Comment translation # Disable account # Verify result Both commands come with comments, something attackers rarely bother with, so the comments very likely point to LLM use. And the models did more than generate commands. The attackers also produced full scripts, complete with the comments typical of LLM output. Comment translation # Creating background tasks for each computer with a thread limit # Concurrent task limit control # Quick ping The fragment above comes from a script Citrus used to enumerate active user sessions on domain systems. Besides LLMs, the attackers use atexec, a classic tool from the Impacket collection, to create scheduled tasks that run commands on hosts: Task name Launched executable file sIErKswD C:\Windows\System32\..\System32\cmd.exe PpMBCCSR C:\Windows\system32\cmd.exe QwZtLmNp C:\Windows\..\Windows\System32\cmd.exe We did not see the exact commands behind these tasks, but Group Policy was refreshed after they ran, so they most likely executed gpupdate /force . When the group compromises 1C:Enterprise servers, it uses external data processors (1C-Shell) to run commands. Persistence: scheduled tasks Citrus uses scheduled tasks to launch its malicious tools automatically. The attackers create the tasks manually through PowerShell: On systems that are not regularly rebooted, such as terminal servers, they sometimes run their tools without establishing persistence at all. Privilege Escalation: vulnerabilities and configuration flaws In every case we know of, the contractor domain account used for initial access had very limited privileges, so the attackers tried to escalate them. To do this, they attempted to exploit the authentication bypass vulnerability CVE-2026-54121 (Certighost) ; these attempts created machine accounts with telltale names in Active Directory, such as: GHOSTAUFTAFGS GHOSTCZ
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Citrus Ransomware: VLESS for traffic, Sn00py for encryption, and LLMs lending a hand
  - Published: 2026-11-11T10:00:25+00:00
  - Link: https://securelist.com/citrus-ransomware/121879/
  - Summary: We break down the Citrus Ransomware group's attacks: the attackers' TTPs and tooling, including VLESS traffic tunneling and LLM use, plus their links to Toy Ghouls.

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

### Cluster b999342a06 — score 10

- Title: Five Findings From the 2027 State of Threat Intelligence
- Source: Recorded Future (threat_research_primary)
- Published: 2026-11-12T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/state-of-threat-intelligence-2027
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
What 768 security professionals told us about consolidation, ROI, and AI. Get five takeaways from the 2027 State of Threat Intelligence.
```

#### Full body

```
Five Findings From the 2027 State of Threat Intelligence Worth Noting for the Year Ahead The much anticipated State of Threat Intelligence report has just been published. The State of Threat Intelligence report is based on a survey Recorded Future conducted with UserEvidence of 768 cybersecurity professionals at enterprises with at least 1,000 employees. It’s the latest edition in our annual report series, where we gauge how threat intelligence is currently being used, funded, and measured. When I first saw the results of this year’s survey, a few findings stood out to me as especially relevant for anyone who runs, funds, or relies on a threat intelligence program and is planning for the year ahead. Here are my top five findings and why. 1. Cost is the least common reason to consolidate A strong majority of respondents (79%) said they plan to consolidate threat intelligence vendors in the next year. That alone is no huge surprise, especially given that respondents reported using an average of five different vendors. Cost would be a reasonable guess for why, but reducing costs actually ranked last of five drivers, at 5%. The drivers that ranked higher point to what teams want from consolidation: Improving correlation across signals (34%) : connecting intelligence across threat domains and internal telemetry into one view of risk. Bringing siloed tools together (29%) : ensuring different risk owners can efficiently act on intelligence. Simplifying operations (22%) : fewer interfaces and handoffs so teams can act on intelligence sooner. Reducing vendor-management overhead (9%) : fewer vendors to evaluate and renew. Overall investment is still rising: 83% plan to increase threat intelligence spending in the next 12 months. Teams are consolidating to get better results from their intelligence, not to cut spend. That puts the focus on outcomes. Jason Steer, CISO at Recorded Future, framed the risk well: consolidation only counts “if that provider has the same or better outcomes.” For anyone evaluating vendors this year, that’s the bar to consider. Especially as teams expand the reach of their threat intelligence programs and support more stakeholders across the enterprise, they’re pursuing vendors that provide coverage across the risk domains that matter for those teams, but equally important that friction is not created in that pursuit of breadth, and that the organization is able to see how threats across disparate domains actually connect. 2. Only 25% have external intelligence and internal telemetry in one place Correlation is the top consolidation driver, yet only a quarter of respondents say external intelligence and internal telemetry reside in one place. The rest break down as follows: 52% are partially integrated across some tools. 18% rely on manual correlation by analysts. 5% keep the two in separate workflows. Poor integration with existing tools and workflows was also the most-cited pain point with current vendors. This doesn’t mean every team needs to move everything into a single tool. What often matters is whether external intelligence can be correlated with internal signals across the tools a team already uses, without an analyst doing it by hand. Collective Insights® is built for this: it pulls detections from a team’s existing security tools and enriches them with Recorded Future intelligence. For the 70% who are partially integrated or correlating manually, it’s worth identifying where that manual handoff still happens. 3. Confidence in ROI is high, but few measure cost savings Nearly every respondent (99%) formally measures the value of their threat intelligence program, and 57% say they are very confident in their ability to quantify its ROI. But when asked how they measure value, more than half (58%) of that very confident group did not include cost savings. Across all respondents, 39% measure cost savings, and 31% measure whether triggered actions actually worked. The most common metrics are operational: Enha
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Five Findings From the 2027 State of Threat Intelligence
  - Published: 2026-11-12T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/state-of-threat-intelligence-2027
  - Summary: What 768 security professionals told us about consolidation, ROI, and AI. Get five takeaways from the 2027 State of Threat Intelligence.

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

### Cluster ee8fcca0b6 — score 10

- Title: Ransomware Attacks Increase Behind AI, But Payments Decline
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-11-16T19:56:05+00:00
- Link: https://www.darkreading.com/threat-intelligence/ransomware-attacks-increase-ai-payments-decline
- Fetch status: fetch_failed:HTTPError
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
  - Title: Ransomware Attacks Increase Behind AI, But Payments Decline
  - Published: 2026-11-16T19:56:05+00:00
  - Link: https://www.darkreading.com/threat-intelligence/ransomware-attacks-increase-ai-payments-decline
  - Summary: Large language models and other AI systems allow a growing number of ransomware groups to create convincing phishing emails and identify sensitive data quickly.

### Cluster ab668646b3 — score 10

- Title: Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-13T08:05:49+00:00
- Link: https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- affected_products: VMware
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-123039
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- affected_products: VMware
- cve_ids: CVE-2026-123039, CVE-2026-109618, CVE-2026-109619
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
An unknown threat actor has been observed targeting unpatched Check Point Security Gateways to obtain initial access via the PHP2Shell vulnerabilities and then a previously unreported local privilege escalation flaw in Gaia OS to deploy a backdoor called TSGA. The activity, detailed by Check Point, began on October 30, 2026, and targeted Israeli organizations, with a broader follow-up
```

#### Full body

```
Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files  Ravie Lakshmanan  Nov 13, 2026 Vulnerability / Cyber Espionage An unknown threat actor has been observed targeting unpatched Check Point Security Gateways to obtain initial access via the PHP2Shell vulnerabilities and then a previously unreported local privilege escalation flaw in Gaia OS to deploy a backdoor called TSGA . The activity, detailed by Check Point, began on October 30, 2026, and targeted Israeli organizations, with a broader follow-up wave on November 2, 2026, that targeted organizations across multiple countries and sectors. Some of the organizations singled out in the first wave have also been at the receiving end of destructive actions that include the deployment of wiper malware. "PHP2Shell provided initial access, followed by privilege escalation through the DynamicCLI interface, tracked as CVE-2026-123039 ," Check Point said. "The attackers then deployed PHP web shells, the persistent TSGA backdoor, and its embedded TSProxy networking component." "The attackers pivoted from the gateway to a VMware ESXi host over SSH, deployed the destroy_v6 wiper, and left politically themed DREAM_ANNEXATION.txt notes during the destructive stage." CVE-2026-123039 (CVSS score: 7.8) is a missing authorization flaw that could enable privilege escalation to root in the DynamicCLI process, enabling any authenticated local user to run arbitrary commands by writing a single request to the socket. "The issue is a local privilege escalation and requires the attacker to already have local code execution on the appliance," Check Point said, adding it "observed an active exploit of this vulnerability against a couple of dozen customers." The issue impacts versions R82.20, R82.10, R82, R81.20, R81.10, and R81 of the following products - Check Point Force Firewalls Check Point Management and Log Servers Multi-Domain Security Management and Multi-Domain Log Server Maestro Orchestrator "In late October 2026, approximately one week after a security fix became available, activity originating from 130.94.19[.]204 targeted Israeli organizations through vulnerable Mobile Access portals on Check Point Security Gateways," Check Point said. "Evidence suggested some cases of a successful compromise, with exploitation activity consistent with PHP2Shell , associated with CVE-2026-109618 and CVE-2026-109619 ." After obtaining initial access, the unknown hacking group is said to have escalated privileges from the portal service account to root by weaponizing CVE-2026-123039 and deploying PHP web shells with an aim to establish persistent access. The web shells support command execution and file upload capabilities. The November 2, 2026, wave is said to have targeted some Israeli organizations that had already been targeted in the first wave, alongside other organizations worldwide, without demonstrating any specific geographic or sector preference, indicating an opportunistic initial-access effort. The access afforded by the web shell paves the way for TSGA, a standalone passive backdoor that also includes a second component called TSProxy. TSGA, deployed as slot_CPconfigdaemon, has been described as a Linux gateway implant with Check Point-specific functionality, offering encrypted remote access, configuration theft, backup and snapshot persistence, process injection, and binary firewall-log tampering. "[TSProxy's] injection code loads this library into selected appliance processes, where it intercepts networking functions to handle specially marked attacker connections while allowing ordinary traffic to continue," Check Point said. "This combines a persistent standalone backdoor with concealed access through existing appliance services." Some of the other post-exploitation actions observed are listed below - Deploying the gogo scanner on the gateway to discover internal assets and services across the network. Moving laterally to a VMware ESXi host o
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files
  - Published: 2026-11-13T08:05:49+00:00
  - Link: https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html
  - Summary: An unknown threat actor has been observed targeting unpatched Check Point Security Gateways to obtain initial access via the PHP2Shell vulnerabilities and then a previously unreported local privilege escalation flaw in Gaia OS to deploy a backdoor called TSGA. The activity, detailed by Check Point, began on October 30, 2026, and targeted Israeli organizations, with a broader follow-up

### Cluster cb75cedcf6 — score 10

- Title: Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-12T15:38:49+00:00
- Link: https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-120868, Citrix

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- affected_products: Citrix
- cve_ids: CVE-2026-107407, CVE-2026-107408, CVE-2026-107409, CVE-2026-107410, CVE-2026-120868
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos
- affected_products: Citrix
- cve_ids: CVE-2026-120868, CVE-2026-107407, CVE-2026-107408, CVE-2026-107409, CVE-2026-107410
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Citrix has released patches for multiple critical security flaws impacting NetScaler ADC, Citrix NetScaler Gateway, and NetScaler Console that could lead to denial-of-service (DoS) or an authentication bypass. The critical vulnerabilities that impact NetScaler ADC and NetScaler Gateway are listed below - CVE-2026-120868 (CVSS score: 9.3) - A memory overflow vulnerability in Packet
```

#### Full body

```
Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass  Ravie Lakshmanan  Nov 12, 2026 Vulnerability / Network Security Citrix has released patches for multiple critical security flaws impacting NetScaler ADC, Citrix NetScaler Gateway, and NetScaler Console that could lead to denial-of-service (DoS) or an authentication bypass. The critical vulnerabilities that impact NetScaler ADC and NetScaler Gateway are listed below - CVE-2026-120868 (CVSS score: 9.3) - A memory overflow vulnerability in Packet Processing can lead to unpredictable or erroneous behavior or DoS. (All NetScaler ADC and NetScaler Gateway deployments) CVE-2026-107407 (CVSS score: 9.3) - A memory overflow vulnerability in SMPP traffic can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC configured with a Load Balancing or Content Switching virtual server of type SMPP) CVE-2026-107408 (CVSS score: 9.3) - A memory corruption vulnerability in DNS / DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC configured for DNS load balancing and recursive DNS resolution) CVE-2026-107409 (CVSS score: 9.3) - A memory corruption vulnerability in DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured with DNS Load Balancing over HTTPS) CVE-2026-107410 (CVSS score: 9.3) - A memory overflow in NetScaler Push can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as Load Balancing virtual server of type PUSH) CVE-2026-107412 (CVSS score: 9.5) - Multiple memory overflow vulnerabilities can lead to unpredictable or erroneous behavior and DoS. (NetScaler configured as a Gateway or an AAA virtual server) CVE-2026-107415 (CVSS score: 9.3) - A memory overflow vulnerability in Email OTP authentication can lead to unpredictable or erroneous behavior or DoS. (NetScaler ADC or NetScaler Gateway configured with an Email Action) CVE-2026-111344 (CVSS score: 9.3) - A memory overflow vulnerability in Endpoint Analysis (EPA/EPAS) can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as a VPN virtual server or an authentication (AAA) virtual server with Endpoint Analysis) CVE-2026-120864 (CVSS score: 9.3) - A memory overflow vulnerability in ICA proxy can lead to unpredictable or erroneous behavior or DoS. (NetScaler configured as a Gateway VPN virtual server, an AAA virtual server, or a CR virtual server of type HDX) All the issues have been patched in the following versions - Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.57 and later releases Citrix NetScaler ADC and Citrix NetScaler Gateway 13.1-64.39 and later releases of 13.1 Citrix NetScaler ADC 14.1-FIPS 14.1-73.58 FIPS and later releases of 14.1-FIPS Citrix NetScaler ADC 13.1-FIPS and 13.1-NDcPP 13.1-37.293 and later releases of 13.1-FIPS and 13.1-NDcPP Also addressed by Citrix are a number of flaws in NetScaler Console and Secure Access Client for Windows and Linux - CVE-2026-120869 (CVSS score: 9.4) - An improper authentication vulnerability in NetScaler Console can allow an unauthenticated attacker to bypass authentication controls to access restricted resources on the appliance. (Fixed in NetScaler Console 14.1-74.34 and later) CVE-2026-118268 (CVSS score: 8.5) - An improper privilege management vulnerability in Secure Access Client for Windows can allow a low-privileged user to escalate privileges to SYSTEM. (Fixed in Secure Access Client for Windows 26.11.1.6 and later) CVE-2026-118269 (CVSS score: 8.5) - An improper privilege management vulnerability in Secure Access Client for Linux can allow a low-privileged user to gain root privileges. (Fixed in Secure Access Client for Linux 26.10.4 and later) The security updates, Citrix said, follow a deeper review of its codebase by integrating artificial intelligence (AI)-assisted code analysis to detect and resolve vulnerabilities with an aim to harden the products before potential threats co
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass
  - Published: 2026-11-12T15:38:49+00:00
  - Link: https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html
  - Summary: Citrix has released patches for multiple critical security flaws impacting NetScaler ADC, Citrix NetScaler Gateway, and NetScaler Console that could lead to denial-of-service (DoS) or an authentication bypass. The critical vulnerabilities that impact NetScaler ADC and NetScaler Gateway are listed below - CVE-2026-120868 (CVSS score: 9.3) - A memory overflow vulnerability in Packet

### Cluster c1406e4930 — score 10

- Title: Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-12T08:20:37+00:00
- Link: https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, telecommunications
- cve_ids: CVE-2026-123863, CVE-2026-123864, CVE-2026-123865, CVE-2026-123866, CVE-2026-123874
- urgency_signals: preauth_unauth
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: financial_services, telecommunications
- cve_ids: CVE-2026-123863, CVE-2026-123866, CVE-2026-123864, CVE-2026-123865, CVE-2026-123874
- urgency_signals: preauth_unauth
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A flaw fixed in Node.js this week lets unauthenticated clients crash servers that use the runtime's built-in HTTP/2 support on the 24.x and 26.x release lines. A second HTTP/2 flaw can cause a server to send a client pieces of its memory, including responses intended for other connections. Fixed versions were released for all three supported lines: 22.23.5, 24.22.3, and 26.13.1. The crash
```

#### Full body

```
Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data  Swati Khandelwal  Nov 12, 2026 Vulnerability / Web Security A flaw fixed in Node.js this week lets unauthenticated clients crash servers that use the runtime's built-in HTTP/2 support on the 24.x and 26.x release lines. A second HTTP/2 flaw can cause a server to send a client pieces of its memory, including responses intended for other connections. Fixed versions were released for all three supported lines: 22.23.5, 24.22.3, and 26.13.1. The crash flaw, CVE-2026-123863 , needs only a default HTTP/2 server that replies before the request body has fully arrived. The Node.js project calls that behavior typical. The crash works over both TLS and cleartext connections. The memory flaw, CVE-2026-123866, affects all three lines. From 24.22.0 and 26.9.0 onward, a client alone can trigger it. On 22.x and older 24.x and 26.x builds, it can still be triggered when the server itself closes a stream partway through a response, for example after an idle timeout. A separate flaw in Node.js HTTPS servers, CVE-2026-123864, can allow an unauthenticated client to read memory from other connections, "including TLS private keys and other users' requests," the project says. It affects all three supported lines. The flaw needs a handler that calls res.flushHeaders() before the request body has fully arrived and later calls res.end() with data. Reading the leaked memory also needs a route that sends back or stores a request body. Plain HTTP servers built with node:http are not affected. The release fixes 16 vulnerabilities in Node.js itself, seven of them rated high. The other four high-rated flaws, and the servers they affect, are: CVE-2026-123865 : a client can make any default HTTP/2 server hold memory and file descriptors permanently, on all three lines. CVE-2026-123874 : a client can corrupt server memory on 24.x and 26.x when the server serves files with stream.respondWithFile() or stream.respondWithFD(). On all three lines, canceling such downloads can also crash the server (CVE-2026-123875, rated medium). CVE-2026-126051 : a client can crash a TLS server on 24.x and 26.x if the server uses the SNICallback, OCSPRequest, newSession or resumeSession hooks, or server.addContext(). CVE-2026-123872 : on a TLS server with stricter client-certificate rules for some hostnames, a client approved for another hostname can switch to a stricter one during TLS 1.2 renegotiation without meeting its rules. All three lines are affected. The eight flaws above are all in Node.js's own HTTP/2, HTTPS and TLS server code, so they matter where a Node.js process accepts those connections itself. Updating to the fixed version for each line is the only fix in the project's security advisory . It lists no workaround for servers that cannot update yet. End-of-life lines, including 20.x and 25.x, get no fix in this release, and the project says such versions are always affected. The advisory does not report any attacks using the flaws. It also does not say whether servers that met the conditions for the HTTPS flaw should replace their TLS keys or other secrets after updating. Five of the flaws, including CVE-2026-123863 and CVE-2026-123864, were reported by Chris Rohlf in collaboration with Claude and Anthropic Research, according to the advisory. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  network security , Vulnerability , Web Security ⚡ Top Stories This Week Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs FBI Says North Korean Hackers Stole Over $400 Million in Crypto Using Deepfake Video Calls SilentAir Hijacks Asian Telecom N
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data
  - Published: 2026-11-12T08:20:37+00:00
  - Link: https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html
  - Summary: A flaw fixed in Node.js this week lets unauthenticated clients crash servers that use the runtime's built-in HTTP/2 support on the 24.x and 26.x release lines. A second HTTP/2 flaw can cause a server to send a client pieces of its memory, including responses intended for other connections. Fixed versions were released for all three supported lines: 22.23.5, 24.22.3, and 26.13.1. The crash

### Cluster ed2e51b312 — score 10

- Title: Microsoft Fixes Nearly 1,100 Security Vulnerabilities
- Source: Krebs on Security (practitioner_analysis)
- Published: 2026-11-10T21:55:03+00:00
- Link: https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Apple iOS/macOS, Ivanti, Microsoft 365
- cve_ids: CVE-2026-124194, CVE-2026-125350
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: Microsoft 365, Apple iOS/macOS, Ivanti
- cve_ids: CVE-2026-124194, CVE-2026-125350
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Microsoft did another four-digit patch drop today, releasing updates to fix almost 1,100 security vulnerabilities in its Windows operating systems and supported software. This month's Patch Tuesday addresses 63 critical flaws -- including a zero-day in Microsoft Outlook -- and comes amid important security updates from other software makers, including Adobe, Apple, Google and Mozilla.
```

#### Full body

```
Microsoft did another four-digit patch drop today, releasing updates to fix almost 1,100 security vulnerabilities in its Windows operating systems and supported software. This month’s Patch Tuesday addresses 63 critical flaws — including a zero-day in Microsoft Outlook — and comes amid important security updates from other software makers, including Adobe , Apple , Google and Mozilla . Image: Shutterstock.com. Diorama by @zepp1969. November’s patch release from Redmond tackles 1,093 vulnerabilities, fixing 63 “critical” flaws that can be exploited to seize control over a Windows system with little or no help from users. Nearly half of those critical bugs are remote code execution vulnerabilities. Overall, 535 of the flaws addressed this month allow an attacker to elevate their privileges on a vulnerable device. This latest round of updates means Microsoft has shipped more than 5,100 security patches so far this year, a staggering number considering that a year ago Microsoft was averaging around 100 patches per month. Microsoft credits advances in artificial intelligence for helping to find (and fix) such a large volume of security bugs in recent months. Last month, Microsoft pushed more than 1,400 fixes. According to Redmond, just one of the flaws is already seeing active exploitation: CVE-2026-124194 , a spoofing bug in Outlook. The advisory for CVE-2026-124194 says it affects Microsoft 365 Apps for Enterprise and editions of Microsoft Office . Several other major software makers pushed security updates this week to fix critical weaknesses in their products. Apple on Monday released out-of-cycle security updates to fix at least nine vulnerabilities in iOS/iPadOS , macOS , watchOS and visionOS . Among the weaknesses reportedly fixed in Apple’s release include an iMessage flaw that could let a remote attacker join a group chat and receive its messages; the updates also fix a separate iMessage flaw that could let someone added to a group access messages sent before they joined. Lee Neely , an instructor at the SANS Institute , noted that Apple backported the fix to iOS 18. “I take notice when Apple releases fixes to more than two versions,” Neely wrote in a SANS newsletter today. “You really need to get to version 27.2.1 of their OSes and push folks who are holding onto devices which cannot run the current version. The best plan often involves setting an upgrade date for old hardware. Run through all your Apple devices and make sure everything is up to date, don’t assume the fixes went out automatically.” Google this week released Chrome version 157.0.8103.50 , which resolves nine security holes, including CVE-2026-125350 , the sixth zero-day vulnerability this year for Chrome (this bug also is being patched in Chromium-based browsers like Edge). The latest Chrome version follows its November 3 release, which fixed 213 vulnerabilities. A new version of Mozilla Firefox out today ( Firefox 160 ) resolves almost 100 CVEs, about half of them high severity. Adobe today released patches for at least 110 vulnerabilities across a range of products, with nearly half of the flaws rated high severity. Adobe said there is no evidence any of the security holes it addressed this month are being actively exploited. Chris Goettl , vice president of product management at Ivanti , said it’s easy for security teams at large enterprises to feel overwhelmed by the volume and criticality of patches from Microsoft lately. But he notes that while some 95,000 vulnerabilities have been assigned CVEs this year across all vendors, only 217 have so far this year been added to the Known Exploited Vulnerabilities (KEV) list maintained by the U.S. Cybersecurity and Infrastructure Security Agency (CISA). “Roughly four in ten of this year’s exploited vulnerabilities sit in operating systems, endpoint software, browsers, and server platforms, which a continuous patch strategy can close quickly,” Goettl said.”The rest calls for exposure management alongside patchi
```

#### Corroborating sources (1)

- **Krebs on Security** (practitioner_analysis)
  - Title: Microsoft Fixes Nearly 1,100 Security Vulnerabilities
  - Published: 2026-11-10T21:55:03+00:00
  - Link: https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/
  - Summary: Microsoft did another four-digit patch drop today, releasing updates to fix almost 1,100 security vulnerabilities in its Windows operating systems and supported software. This month's Patch Tuesday addresses 63 critical flaws -- including a zero-day in Microsoft Outlook -- and comes amid important security updates from other software makers, including Adobe, Apple, Google and Mozilla.

### Cluster 188566384e — score 10

- Title: Inside the new Google Cloud Data Boundary experience
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-11-16T08:05:00+00:00
- Link: https://cloud.google.com/blog/products/identity-security/inside-the-new-data-boundary-experience/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: government
- affected_products: Google Cloud, Google/Gemini
- urgency_signals: zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_industries: government
- affected_products: Google Cloud, Google/Gemini
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Digital sovereignty is evolving from a standard compliance requirement into a powerful strategic advantage for regulated industries worldwide. From European frameworks designed to meet sovereign standards (DORA, EHDS, GDPR) to FedRAMP/ILs/ITARs in the U.S., or expanding mandates across Asia-Pacific and the Middle East, organizations can build deeper global trust through clear governance over data locality, encryption keys and system access. Historically, achieving that level of control meant accepting an impossible tradeoff: rely on rigid legacy architectures that lacked access to frontier AI innovation, or stitch together brittle, manual guardrails that slowed developer velocity. Google Cloud Data Boundary helps remove that compromise. Built directly onto Google Cloud’s global commercial infrastructure, Data Boundary delivers software-defined, AI-assisted governance. This allows organizations to move at commercial speed with verifiable sovereign controls built in from day one. Today,
```

#### Full body

```
Security & Identity Inside the new Google Cloud Data Boundary experience November 16, 2026 Nitin Garg Engineering Director, Regulated Cloud Ruchi Khurana Group Product Manager, Regulated Cloud Try Gemini today The front door to AI in the workplace Try now Digital sovereignty is evolving from a standard compliance requirement into a powerful strategic advantage for regulated industries worldwide. From European frameworks designed to meet sovereign standards (DORA, EHDS, GDPR) to FedRAMP/ILs/ITARs in the U.S., or expanding mandates across Asia-Pacific and the Middle East, organizations can build deeper global trust through clear governance over data locality, encryption keys and system access. Historically, achieving that level of control meant accepting an impossible tradeoff: rely on rigid legacy architectures that lacked access to frontier AI innovation, or stitch together brittle, manual guardrails that slowed developer velocity. Google Cloud Data Boundary helps remove that compromise. Built directly onto Google Cloud’s global commercial infrastructure, Data Boundary delivers software-defined, AI-assisted governance. This allows organizations to move at commercial speed with verifiable sovereign controls built in from day one. Today, we’re announcing a new and updated experience in Data Boundary. Google Cloud Data Boundary combines technical controls across residency, access, and encryption with ongoing monitoring and operational assurance. What’s new in Data Boundary Data Boundary streamlines how security, data and AI teams configure, test and scale governance across their cloud footprint. Below are the key highlights for the new experience: End-to-end visibility into sovereign controls: Browse and deploy pre-configured regional and industry frameworks with clear visibility into mapped technical controls, severities and remediation steps. Flexible hierarchy-wide enforcement: Apply preventative guardrails across organizations, complex nested folders and projects — on both net-new and existing workloads — to block out-of-policy API calls and configuration drift. Dry run posture validation: Dry run any framework in monitor mode across live existing workloads to identify drift and violations before enabling active enforcement. Compliance customization: Frameworks and controls customization according to your organization's needs. Use Gemini in Google Cloud to customize controls and generate remediation logic to help reduce manual compliance toil. Accelerated compliance with machine-readable evidence: Continuously monitor posture, record immutable exception justifications, run scheduled audits and export machine-readable audit evidence to help fast-track certification workflows. Turn compliance and digital sovereignty into a business accelerator In an era of evolving global regulations and rapid AI transformation, compliance and sovereignty should accelerate your innovation, not hold you back. Google Cloud Data Boundary helps you deploy frontier AI, scale globally across commercial regions, and meet stringent regulatory requirements — with greater control and visibility over your data, your keys and your operations. Here are six steps to get started with Data Boundary today: You can access the Data Boundary directly from your Google Cloud console . Navigate to the Compliance tab in your Google Cloud console, and select Frameworks to begin with. Select existing or configure your own compliance : Browse 40+ public sector, industry and sovereign AI control packages, or customize guardrails to match your specific organizational policies. Select your regions : Designate precise geographic boundaries and data residency restrictions across 29 global commercial regions. Evaluate workloads in dry-run mode : E nforce controls at either the folder or the project level. If you already have an active BigQuery or Gemini project running, you can turn on dry run mode to evaluate how controls behave across existing resources without disrupting li
```

#### Corroborating sources (2)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Inside the new Google Cloud Data Boundary experience
  - Published: 2026-11-16T08:05:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/inside-the-new-data-boundary-experience/
  - Summary: Digital sovereignty is evolving from a standard compliance requirement into a powerful strategic advantage for regulated industries worldwide. From European frameworks designed to meet sovereign standards (DORA, EHDS, GDPR) to FedRAMP/ILs/ITARs in the U.S., or expanding mandates across Asia-Pacific and the Middle East, organizations can build deeper global trust through clear governance over data locality, encryption keys and system access. Historically, achieving that level of control meant accepting an impossible tradeoff: rely on rigid legacy architectures that lacked access to frontier AI innovation, or stitch together brittle, manual guardrails that slowed developer velocity. Google Cloud Data Boundary helps remove that compromise. Built directly onto Google Cloud’s global commercial infrastructure, Data Boundary delivers software-defined, AI-assisted governance. This allows organizations to move at commercial speed with verifiable sovereign controls built in from day one. Today,
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across Processes in VMs
  - Published: 2026-11-12T12:09:14+00:00
  - Link: https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html
  - Summary: Google Cloud VMs on AMD Turin chips need a guest OS patch and a stop-and-start to protect against three CPU side-channel flaws, Google said this week. The company has already applied mitigations against attacks between VMs, and between VMs and the host. Inside a VM, the flaws may let an attacker with code on the same processor core infer data from other processes or the kernel. The affected

### Cluster 8612af1425 — score 9

- Title: Microsoft Patch Tuesday November 2026, (Tue, Nov 10th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-11-11T18:28:43+00:00
- Link: https://isc.sans.edu/diary/rss/33508
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
Microsoft continues its AI-induced patch surge, addressing 1,260 different vulnerabilities this month. 68 of these vulnerabilities are considered critical. 167 of the vulnerabilities are Chromium issues affecting Microsoft Edge.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Microsoft Patch Tuesday November 2026, (Tue, Nov 10th)
  - Published: 2026-11-11T18:28:43+00:00
  - Link: https://isc.sans.edu/diary/rss/33508
  - Summary: Microsoft continues its AI-induced patch surge, addressing 1,260 different vulnerabilities this month. 68 of these vulnerabilities are considered critical. 167 of the vulnerabilities are Chromium issues affecting Microsoft Edge.

### Cluster 94b6512e69 — score 9

- Title: Optimizely supply chain attack infects major brands' sites with malware
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-17T02:12:17+00:00
- Link: https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-infects-major-brands-sites-with-malware/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: GitLab, Salesforce

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: financial_services
- affected_products: GitLab, Salesforce
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: financial_services
- affected_products: Salesforce, GitLab
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A suspected supply chain attack targeting Optimizely has led to malicious JavaScript being loaded on numerous popular websites, including Zoom, CNN, Fox News, BBC, Salesforce, and GitLab, exposing visitors to scripts designed to steal cryptocurrency and payment information and exploit vulnerabilities in iOS devices. [...]
```

#### Full body

```
Optimizely supply chain attack infects major brands' sites with malware By Lawrence Abrams November 16, 2026 09:12 PM 0 A suspected supply chain attack targeting Optimizely has led to malicious JavaScript being loaded on numerous popular websites, including Zoom, CNN, Fox News, BBC, Salesforce, and GitLab, exposing visitors to scripts designed to steal cryptocurrency and payment information and exploit vulnerabilities in iOS devices. Optimizely is a digital experience and experimentation platform that organizations use to test and personalize their websites, with its JavaScript files loaded into customers' webpages to deliver this functionality. The attack was first uncovered by security researcher Scott Helme, who reported Monday that his team had identified 188 infected Optimizely JavaScript files belonging to 178 organizations after analyzing 1,611 scripts used by the platform. According to Helme's analysis, attackers inserted malicious code into Optimizely customer projects, causing JavaScript files hosted on the company's content delivery network (CDN) to load malware on websites that used the service. BleepingComputer independently confirmed that the malicious script loaded, or attempted to load, on numerous affected websites using scans recorded by urlscan.io, including Zoom , KLM , GitLab , BBC , Scheels , CNN , American Girl , ManageBuilding , Smartsheet , Stamps.com , and Salesforce . Other affected websites include Fox News , Mutual of Omaha , American Eagle , Air France , Change.org , Optimizely , HSBC Insurance , Bitly , IG , and UNICEF USA . BleepingComputer analyzed copies of the modified Optimizely JavaScript files and confirmed that attackers had injected code designed to load an additional malicious script from https://1688360[.]cc/track.js . The injected code used several methods to load the payload, with some files referencing the malicious URL directly, while others used Base64 encoding and JavaScript's atob() function to decode the URL. Helme also identified a variation that could execute an embedded copy of the malicious code if the remote script was blocked. Malicious JavaScript injected on CNN.com loaded from an Optimizely script Source: BleepingComputer An analysis of the malicious track.js file revealed several capabilities, which Helme also documented in his investigation: Cryptocurrency hijacking: Monitors webpages for cryptocurrency wallet addresses and replaces them with attacker-controlled addresses to steal transfers. Payment card skimming: Searches for credit card numbers, expiration dates, and security codes entered into webpages, and attempts to transmit the captured information to https://1688360[.]cc/card.php . iOS exploit delivery: Loads additional malicious JavaScript targeting iPhones and iPads. Helme identified these secondary payloads as the Coruna and DarkSword exploit kits , which target different iOS versions. The malicious script also contains functionality to collect browser cookies, webpage URLs, and screenshots, which can be transmitted to the attackers. Helme's investigation found that cryptocurrency wallets embedded in the track.js script received approximately $7,000 in transactions on November 16, indicating the cryptocurrency clipboard-hijacking component had succeeded in stealing cryptocurrency payments. Below is the full list of cryptocurrency addresses seen by BleepingComputer: Cryptocurrency Wallet Address Amount Received Transactions Bitcoin (BTC) 19g9rZcPeiz8rUvyWpTRyXXhPnjsWrc3kW 0.08298 BTC (~$5,380) 7 Litecoin (LTC) ltc1q3wp7g6ds0ggg6fl6kncpa4sepn0q3qfacgred5 17.02 LTC (~$762) 3 TRON (TRX / USDT) THvs6p56XkUiMkJeSc51cAP64u2RsTYqxa 662.9 USDT + 184 TRX (~$719) 50 Ethereum (ETH) 0xC4026b06D82b0F0B363eda0642D61CfbDc17884e 0.074 ETH (~$100) 6 BNB Smart Chain (USDT) 0xC4026b06D82b0F0B363eda0642D61CfbDc17884e 82 USDT (~$82) 2 Solana (SOL) FVtL8NMYS9PA1v3HE67XUGCtGA9JaZUvqav2fU2LrV5n 0 0 TON UQAgM1VqSZQiJLSG5w-ovurq5CZdxLEK3_7CMmwALTA5e09p 0 0 Bitcoin Cash (BCH) qzkaaf8n
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Optimizely supply chain attack infects major brands' sites with malware
  - Published: 2026-11-17T02:12:17+00:00
  - Link: https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-infects-major-brands-sites-with-malware/
  - Summary: A suspected supply chain attack targeting Optimizely has led to malicious JavaScript being loaded on numerous popular websites, including Zoom, CNN, Fox News, BBC, Salesforce, and GitLab, exposing visitors to scripts designed to steal cryptocurrency and payment information and exploit vulnerabilities in iOS devices. [...]

### Cluster 05bbbee14f — score 9

- Title: Uber Data Breach Impacts 150,000 People
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-16T11:02:48+00:00
- Link: https://www.securityweek.com/uber-data-breach-impacts-150000-people/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, phishing_social_eng, supply_chain, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, GitHub
- urgency_signals: poc_available, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, credential_theft, zero_day, data_breach
- affected_industries: government
- affected_products: Anthropic/Claude, GitHub
- urgency_signals: zero_day, poc_available
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers compromised a third-party services provider and stole names, addresses, and driver’s license numbers. The post Uber Data Breach Impacts 150,000 People appeared first on SecurityWeek .
```

#### Full body

```
Uber is notifying roughly 150,000 drivers that their personal information was stolen in a data breach involving a third-party services provider. The company learned of the incident on October 9 and immediately severed its data connections with the provider and launched an investigation. On October 13, the investigation determined that the hackers used compromised service provider credentials on October 7 to access data Uber had shared with the provider. According to Uber, the hackers accessed images of driver’s licenses and personal information such as names, addresses, dates of birth, driver’s license numbers, and government-issued ID numbers. The company says that the data was stored in an environment created and managed by Uber’s Cloud Security team. While alerts were enabled, none were triggered because the threat actor used valid credentials. “The service provider’s compromised credentials did not provide access to other Uber systems. The investigation remains ongoing,” the company said. Advertisement. Scroll to continue reading. Uber has filed data breach notifications with multiple US states, including California, Iowa, Massachusetts, South Carolina, Texas, and Vermont, and reportedly notified the Texas Attorney General’s Office that a total of 149,346 people were affected. Uber is providing the potentially affected individuals with free credit monitoring and fraud assistance services. Uber did not identify the service provider in its breach notifications, but a company spokesperson confirmed to TechCrunch that the incident involved Fireworks AI, a cloud platform for running and fine-tuning open source AI models. Fireworks initially said it had found no evidence that customer personal information, models or datasets had been accessed. However, in a November 9 update , the company acknowledged that the breach also affected account and billing information, as well as some customer datasets and incomplete models. SecurityWeek has emailed Uber for additional information on the data breach and will update this article if the company responds. Related: Notion Customer Data Compromised in Fireworks AI Hack Related: Apify Confirms Customer Data Accessed in Cyberattack Related: Iris Plaza Breach May Have Exposed Data of 7.7 Million Customers Related: Amplifon Americas Data Breach Impacts 1.3 Million Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Law Enforcement Disrupts Gootloader, CastleRAT, and StealC Infrastructure Citrix Patches 10 Critical NetScaler Vulnerabilities Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’ PHP2Shell Exploited in Destructive Check Point Gateway Attacks Hackers Exploit New N-central Zero-Day Hours After PoC Publication Chrome, Firefox Updates Patch Over 180 Vulnerabilities Daylight Lands $80 Million for AI-Powered Security Operations Notion Customer Data Compromised in Fireworks AI Hack Latest News Trump Administration Moves to Block China From Indirect Access to American AI Technology Cursor Supply Chain Attack Started at Fireworks AI Google Project Zero Sets Course for 30-Day Disclosure Deadline Barracuda Hacked Amid Surge in Artex-Powered Cyberattacks Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch Recent UnrealIRCd Vulnerability Exploited in Attacks Hackers Probe Newly Disclosed Flaws in Copeland Refrigeration Controllers Tor Updates DoS Defenses Again as Relay Attacks Continue Trending Attacker Targets 60,000 GitHub Repositories in Credential Theft Campaign Amplifier Security Emerges From Stealth With AI Copilot, Human-in-the-Loop Automation No Signs of Hacking in FAA Ground Stop as FBI Reportedly Probes Software Update Microsoft Rules Out Cyberattack in Outage, Warns of Phishing Campaign Apache Patches Critical HTTP Server RCE Found by Anthropic, Google Apple Rev
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Uber Data Breach Impacts 150,000 People
  - Published: 2026-11-16T11:02:48+00:00
  - Link: https://www.securityweek.com/uber-data-breach-impacts-150000-people/
  - Summary: Hackers compromised a third-party services provider and stole names, addresses, and driver’s license numbers. The post Uber Data Breach Impacts 150,000 People appeared first on SecurityWeek .

### Cluster bf6b5c1d3c — score 9

- Title: New OpenSSH Vulnerability
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-11-10T12:02:38+00:00
- Link: https://www.schneier.com/blog/archives/2026/11/new-openssh-vulnerability.html
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
It’s a bad one , and it’s been in the code for a decade: A newly disclosed flaw involving OpenSSH and musl, dubbed “*sshole,” allows attackers to log in to certain Alpine Linux and other musl-based Linux accounts configured to block password authentication simply by entering an oversized password. “Oversized” means longer than 256 bytes. Details . Slashdot thread . And another news article .
```

#### Full body

```
Clive Robinson • November 10, 2026 11:22 AM @ ALL, The name given to the vulnerability of “*sshole” is not supposed to be seen as “rude”. The “sshole” is actually a contractin of “SSH hole”. The lead “ ” is part of what makes the vulnerability work. And is based on the *nix password file, where the “ ” was placed in the password field to indicate an account was not to be loged into from the login programe The reason for the lead “*” is it was not a valid character in the password field and thus could be used for “in band signalling” Some of you are possibly old enough to remember the arguments about which was better “C strings or Pascal strings”. C strings used in-band signalling such that a string could be any length, but it alway terminated in the ASCII NUL character (from 1962 that had significant use in “super encryption” devices based on “One Time Tapes from earlier Baudot and ITU 2). Pascal strings used out-of-band signalling, put simply the lead byte was used to store the length of the string. The had advantages and disadvantages. An advantage was that string math was faster, and the first character of the string was not at position zero but position on that was easier for many people to get there heads around and more importantly all characters were valid. The downside was the string had to be 255 or less characters long. Which at first does not appear much of a disadvantage, but when you dig in, it quickly becomes clear that code is easier to make more general with unlimited length strings and is faster and takes up less program “code” store/memory and alows easy machine code tricks… The other issue back then was “return values” from functions. Originally it was a type int that was the size of the machine dataword. For reasons to long to relate this turned out to be a bad idea… So “in band signalling” became the norm under *nix with an integer holding a return / error code. Actual data was usually returned in a memory array that the calling code passed a pointer to into the function. Security wise this is a bad way to do things even though it can be quite efficient.
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: New OpenSSH Vulnerability
  - Published: 2026-11-10T12:02:38+00:00
  - Link: https://www.schneier.com/blog/archives/2026/11/new-openssh-vulnerability.html
  - Summary: It’s a bad one , and it’s been in the code for a decade: A newly disclosed flaw involving OpenSSH and musl, dubbed “*sshole,” allows attackers to log in to certain Alpine Linux and other musl-based Linux accounts configured to block password authentication simply by entering an oversized password. “Oversized” means longer than 256 bytes. Details . Slashdot thread . And another news article .

### Cluster 08ec474efa — score 9

- Title: The Transaction Is the Last Step, Not the First
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-11-16T20:35:19+00:00
- Link: https://www.team-cymru.com/post/fraud-defense-ft3-attack-patterns
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
Waiting for the transaction to catch fraud? You're already too late. Learn how tracking attack patterns in threat intelligence stops actors early.
```

#### Full body

```
3 min read September 2, 2026 The Transaction Is the Last Step, Not the First Most fraud programs are built to catch fraud where it becomes visible: at the transaction. That's also the most expensive place to catch it. By the time a payment is flagged, the infrastructure behind it has already been built, the targeting has already happened, and the account has likely already been compromised. That gap, between where fraud is detected and where it actually originates, is the problem Team Cymru's Fraud Defense Intelligence work is built to close. Six stages happen before a loss is booked Fraud doesn't start at checkout. It moves through a kill chain: infrastructure is stood up, targets are identified, engagement occurs, accounts are compromised, and only then does monetization occur. Most fraud programs are built to engage at the last two stages of that chain, the transaction and the monetization that follows it. Five stages run before a loss is booked. Most programs only engage at the last two. That leaves a wide window where infrastructure intelligence, not transaction data, is what actually helps. NetFlow data, passive DNS, BGP routing intelligence, IP and domain analysis, certificate data, and malware intelligence can surface the infrastructure behind a fraud operation well before it reaches a payment processor. Investigators can move from an isolated indicator, a suspicious IP or domain, to the relationships, infrastructure, and historical activity surrounding it, exposing the broader operation rather than just the transaction in front of them. Why this matters right now Fraud is not a static target. Adversary infrastructure gets reused, adversary tactics get shared, and the operators behind one fraud campaign are frequently behind several others running in parallel. Static, transaction-level detection sees each of these as an isolated event. Infrastructure-level visibility sees them as one operation. That's the layer where Team Cymru works: providing the infrastructure intelligence that lets fraud teams and threat hunters trace an operation backward, from the payment to the compromise, to the infrastructure that made it possible, and forward again into detections, mitigations, and disruption. Our Pure Signal Command platform brings that discovery, understanding, and action into a single investigative workflow, with APIs and MCP integration built for teams that need to move fast and act on what they find. This is also why we've been an active supporter of the industry's move toward shared, structured fraud intelligence. Standardized frameworks that describe fraud adversary behavior across its full lifecycle, not just at the point of transaction, make this kind of infrastructure-first investigation faster and more consistent across organizations. It's why we've supported the development of FT3, the fraud taxonomy created by Vincent Passaro at Stripe , with engineering resources and infrastructure intelligence as it evolves into FT3 2.0. And it's the same reason we continue to invest engineering resources and threat research directly into the practitioner communities where fraud intelligence gets built and tested. "Some of the most important advances in security don't begin inside a company or a product roadmap; they begin with practitioners solving real problems together," said Joe Sander, CEO of Team Cymru. "Our role is to support that work: providing engineering resources, intelligence and infrastructure visibility where we can be useful, and helping sustain the trusted communities where practitioners share what they know," said Mike Barry, VP of Engineering at Team Cymru. "The goal is not ownership. It is making it easier for good people doing difficult work to learn from one another and build something stronger together." Visibility before the transaction Fraud will always eventually show up in a payment. But by the time it does, the more valuable window for stopping it has usually already closed. Getting visibility into t
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: The Transaction Is the Last Step, Not the First
  - Published: 2026-11-16T20:35:19+00:00
  - Link: https://www.team-cymru.com/post/fraud-defense-ft3-attack-patterns
  - Summary: Waiting for the transaction to catch fraud? You're already too late. Learn how tracking attack patterns in threat intelligence stops actors early.

### Cluster 186ec3fa79 — score 9

- Title: WhiteArmor gang claims responsibility for latest cyber attack on shipping giant Maersk
- Source: Graham Cluley (practitioner_analysis)
- Published: 2026-11-12T15:12:29+00:00
- Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/whitearmor-gang-cyberattack-maersk
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- affected_industries: manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- affected_industries: manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
Shipping giant Maersk has confirmed that one of its systems was broken into by hackers who have stolen data. The WhiteArmor gang has claimed responsbility for the attack. Read more in my article on the Hot for Security blog.
```

#### Full body

```
Industry News Data Breach 2 min read WhiteArmor gang claims responsibility for latest cyber attack on shipping giant Maersk Graham CLULEY November 12, 2026 Shipping giant Maersk has confirmed that one of its systems was broken into by hackers who have stolen data. In a statement published yesterday on its website, the company said that it had detected the unauthorised access to a "local legacy system". The Danish company has not said which system was hit, what data was taken, or when the security breach occurred. The firm has, however, said that it has seen no sign that the breach involved other Maersk systems, or that shipments have been impacted. To date, Maersk says that it has not seen any evidence that any sensitive information has been breached. Responsibility for the attack has been claimed by the WhiteArmor cybercrime group, which has listed Maersk on its dark web leak site. There it demanded a ransom equivalent to US $5 million be paid within 30 days, for the 100GB worth of data it claims to have stolen from a platform built by LF Logistics, a firm that Maersk acquired in 2022. WhiteArmor is a relatively new cyber-extortion group, having emerged late last month, but it is already claiming more than a dozen victims on its leak site including Chinese electronics and home appliance manufacturer Hisense . According to WhiteArmor, its data haul from Maersk includes nearly 30,000 driver records, plaintext passwords, purchase orders, advance shipping notices, signed delivery receipts, and 27,842 mobile device records containing phone numbers, email addresses, and IMEI numbers. While Maersk has not confirmed the veracity of the hackers' claims, it is advising customers and partners to treat unexpected messages about the security breach with caution, and to always verify with a trusted contact at the company before taking any action. Regular readers of the Hot for Security blog will be well aware that this is not Maersk's first brush with cybercrime. In 2017, the company was hit by the NotPetya malware attack which forced the firm to reinstall more than 4000 servers and 45,000 workstations, and ended up costing it up to US $300 million. On this occasion the breach appears to have happened because of IT systems inherited from an acquisition. As such it serves as a salutary reminder that when you buy a company you also buy its IT systems, and any security problems which may lurk within them. tags Industry News Data Breach Author Graham CLULEY Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s. View all posts You might also like Bookmarks
```

#### Corroborating sources (1)

- **Graham Cluley** (practitioner_analysis)
  - Title: WhiteArmor gang claims responsibility for latest cyber attack on shipping giant Maersk
  - Published: 2026-11-12T15:12:29+00:00
  - Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/whitearmor-gang-cyberattack-maersk
  - Summary: Shipping giant Maersk has confirmed that one of its systems was broken into by hackers who have stolen data. The WhiteArmor gang has claimed responsbility for the attack. Read more in my article on the Hot for Security blog.

### Cluster d7028f613a — score 9

- Title: PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-12T11:33:15+00:00
- Link: https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-126325

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, web_shell_backdoor, zero_day
- actor_attribution: Cl0p
- affected_industries: financial_services, manufacturing_industrial, telecommunications
- affected_products: Linux kernel
- cve_ids: CVE-2026-12569, CVE-2026-126325
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, web_shell_backdoor
- actor_attribution: Cl0p
- affected_industries: financial_services, manufacturing_industrial, telecommunications
- affected_products: Linux kernel
- cve_ids: CVE-2026-126325, CVE-2026-12569
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325, carries a CVSS v4 score of 9.2 out of a maximum of 10.0. It has been described as a case of improper input validation and deserialization of untrusted data that could result in
```

#### Full body

```
PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution  Ravie Lakshmanan  Nov 12, 2026 Vulnerability / Enterprise Security PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325 , carries a CVSS v4 score of 9.2 out of a maximum of 10.0. It has been described as a case of improper input validation and deserialization of untrusted data that could result in remote code execution via crafted requests. "A critical remote code execution (RCE) vulnerability has been reported in PTC Windchill and PTC FlexPLM," according to a description of the flaw on CVE.org. "The vulnerability may be exploited through the deserialization of untrusted data." The CVE record lists the following versions as affected - PTC Windchill: 11.0 M030, 11.1 M020, 11.2.1.0, 12.0.2.0, 12.1.2.0, 13.0.2.0, 13.1.0.0, 13.1.1.0, 13.1.2.0, 13.1.3.0, 13.1.4.0 PTC FlexPLM: 11.0 M030, 11.1 M020, 11.2.1.0, 12.0.2.0, 12.1.2.0, 13.0.2.0, 13.1.0.0, 13.1.1.0, 13.1.2.0, 13.1.3.0 "If your Windchill or FlexPLM environment is hosted by PTC, the patches have been applied on their behalf. No action is required on your part," PTC said in a statement posted on its website. "If your Windchill or FlexPLM environment is not hosted by PTC, we urge you to apply the patch as soon as possible to help protect your systems." The disclosure comes nearly five months after another critical remote code execution (RCE) issue in Windchill and FlexPLM ( CVE-2026-12569 , CVSS score: 9.3) came under active exploitation. Then, in July 2026, it emerged that threat actors linked to the Cl0p ransomware operation were weaponizing the flaw as part of a data extortion campaign designed to drop JSP web shells and exfiltrate sensitive product data from manufacturing companies and industrial enterprises. "PTC software is a textbook target for initial access brokers and ransomware operators and a significant enabler of triple extortion campaigns," Yordan Ganchev, principal threat intelligence specialist at watchTowr, said in a statement shared with The Hacker News. "It allows malicious actors to reach far and wide within victim networks, encrypt and exfiltrate proprietary data, and disrupt industrial processes. In many cases, the impact across these environments has downstream implications for time-sensitive manufacturing, logistics, and fulfillment processes, resulting in material costs per hour of downtime." Organizations running PTC Windchill and FlexPLM products are recommended to patch exposed systems as soon as possible and monitor for signs of code execution, backdoor access, or web shells on the host. If patching is not an immediate option, it's essential to apply network restrictions to limit the risk of compromise. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  enterprise security , Software Security , Vulnerability ⚡ Top Stories This Week Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs FBI Says North Korean Hackers Stole Over $400 Million in Crypto Using Deepfake Video Calls SilentAir Hijacks Asian Telecom Networks to Intercept SMS 2FA Codes and Spy on Taiwanese Users Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More Stories New SignDrop Zero-Day Exploit Turns Windows CLFS Security Feature Into SYSTEM Access Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass Critical Red Hat Quay Flaw Lets Attackers Read
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution
  - Published: 2026-11-12T11:33:15+00:00
  - Link: https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html
  - Summary: PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325, carries a CVSS v4 score of 9.2 out of a maximum of 10.0. It has been described as a case of improper input validation and deserialization of untrusted data that could result in

### Cluster 3ade03443a — score 9

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

### Cluster 9a2bede6cc — score 8

- Title: Log Analysis Field Guide: Tips for Spotting Patterns and Red Flags
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-11-11T21:57:25+00:00
- Link: https://www.blackhillsinfosec.com/log-analysis-guide/
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
Imagine you’re a detective, but your crime scene is made of timestamps, IP addresses, and login attempts instead of fingerprints and DNA. Log analysis is the art of reading digital breadcrumbs that attackers leave behind—every click, connection, and failed password gets recorded automatically. Here are some tips for learning how to survey and when to pull out the magnifying glass.
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: Log Analysis Field Guide: Tips for Spotting Patterns and Red Flags
  - Published: 2026-11-11T21:57:25+00:00
  - Link: https://www.blackhillsinfosec.com/log-analysis-guide/
  - Summary: Imagine you’re a detective, but your crime scene is made of timestamps, IP addresses, and login attempts instead of fingerprints and DNA. Log analysis is the art of reading digital breadcrumbs that attackers leave behind—every click, connection, and failed password gets recorded automatically. Here are some tips for learning how to survey and when to pull out the magnifying glass.

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

### Cluster 07872cc4cb — score 8

- Title: Crafty Microsoft Teams Booking Flow Disguises Device Code Phishing
- Source: Huntress (detection_response_operations)
- Published: 2026-11-12T14:00:00+00:00
- Link: https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing
- Fetch status: not_attempted
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
Threat actors used a convincing Microsoft Teams meeting-booking lure to conceal device code phishing and trick victims into authorizing attacker access.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Crafty Microsoft Teams Booking Flow Disguises Device Code Phishing
  - Published: 2026-11-12T14:00:00+00:00
  - Link: https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing
  - Summary: Threat actors used a convincing Microsoft Teams meeting-booking lure to conceal device code phishing and trick victims into authorizing attacker access.

### Cluster a9ccd4b20f — score 8

- Title: Beyond the clipboard: The evolving tradecraft of ClickFix
- Source: Huntress (detection_response_operations)
- Published: 2026-11-10T14:00:00+00:00
- Link: https://www.huntress.com/blog/the-evolving-tradecraft-of-clickfix
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
ClickFix techniques are evolving. Huntress breaks down four attack chains: lateral movement, hidden PNG payloads, Node.js RATs and cache seeing.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Beyond the clipboard: The evolving tradecraft of ClickFix
  - Published: 2026-11-10T14:00:00+00:00
  - Link: https://www.huntress.com/blog/the-evolving-tradecraft-of-clickfix
  - Summary: ClickFix techniques are evolving. Huntress breaks down four attack chains: lateral movement, hidden PNG payloads, Node.js RATs and cache seeing.

### Cluster c7bc99be1d — score 8

- Title: Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-16T12:48:03+00:00
- Link: https://www.securityweek.com/telegram-widgets-hit-by-rce-demos-malware-warning-days-after-launch/
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
Kaspersky suspects exploitation of Telegram’s new widgets to deliver WebRAT, as researchers demo RCE and Pavel Durov disputes the claims. The post Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch
  - Published: 2026-11-16T12:48:03+00:00
  - Link: https://www.securityweek.com/telegram-widgets-hit-by-rce-demos-malware-warning-days-after-launch/
  - Summary: Kaspersky suspects exploitation of Telegram’s new widgets to deliver WebRAT, as researchers demo RCE and Pavel Durov disputes the claims. The post Telegram Widgets Hit by RCE Demos, Malware Warning Days After Launch appeared first on SecurityWeek .

### Cluster 4da0cee80b — score 8

- Title: US seizes North Korean hacking infrastructure, $1.2 billion in cryptocurrency stolen from Binance
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-11-13T00:32:19+00:00
- Link: https://cyberscoop.com/us-seizes-north-korea-hacking-infrastructure-binance/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: APT38

#### Cluster taxonomy (union across members)
- actor_attribution: APT38
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- actor_attribution: APT38
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The infrastructure, said to belong to APT38, contained footage used to fool victims over video calls. The post US seizes North Korean hacking infrastructure, $1.2 billion in cryptocurrency stolen from Binance appeared first on CyberScoop .
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: US seizes North Korean hacking infrastructure, $1.2 billion in cryptocurrency stolen from Binance
  - Published: 2026-11-13T00:32:19+00:00
  - Link: https://cyberscoop.com/us-seizes-north-korea-hacking-infrastructure-binance/
  - Summary: The infrastructure, said to belong to APT38, contained footage used to fool victims over video calls. The post US seizes North Korean hacking infrastructure, $1.2 billion in cryptocurrency stolen from Binance appeared first on CyberScoop .

### Cluster 5361d6efa7 — score 8

- Title: Extortion Group Luna Moth Flits Into Law Firms a Second Time
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-11-12T20:09:41+00:00
- Link: https://www.darkreading.com/data-privacy/extortion-luna-moth-law-firms-second-time
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
The cybercriminals are retargeting law firms that refused to pay its first ransom, with a social engineering con aimed at stealing Microsoft access tokens.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Extortion Group Luna Moth Flits Into Law Firms a Second Time
  - Published: 2026-11-12T20:09:41+00:00
  - Link: https://www.darkreading.com/data-privacy/extortion-luna-moth-law-firms-second-time
  - Summary: The cybercriminals are retargeting law firms that refused to pay its first ransom, with a social engineering con aimed at stealing Microsoft access tokens.

### Cluster b1d2c9c697 — score 8

- Title: New SignDrop Zero-Day Exploit Turns Windows CLFS Security Feature Into SYSTEM Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-12T17:50:27+00:00
- Link: https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html
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
Public exploit code released earlier this week claims that a local Windows user can gain SYSTEM privileges through the Common Log File System driver. The proof of concept, called SignDrop, targets a log-authentication feature added to the driver last year. It abuses how clfs.sys creates companion files when a privileged process opens a prepared log, using path redirection to take control of
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New SignDrop Zero-Day Exploit Turns Windows CLFS Security Feature Into SYSTEM Access
  - Published: 2026-11-12T17:50:27+00:00
  - Link: https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html
  - Summary: Public exploit code released earlier this week claims that a local Windows user can gain SYSTEM privileges through the Common Log File System driver. The proof of concept, called SignDrop, targets a log-authentication feature added to the driver last year. It abuses how clfs.sys creates companion files when a privileged process opens a prepared log, using path redirection to take control of

### Cluster b5894c9450 — score 8

- Title: Critical Zoom Workplace Flaw Could Allow Unauthenticated Remote Privilege Escalation
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-11T16:12:46+00:00
- Link: https://thehackernews.com/2026/11/critical-zoom-workplace-flaw-could.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-108186

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-108186
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-108186
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Zoom has released software updates to address two security flaws impacting Zoom Workplace for Windows, including a critical bug that could result in privilege escalation on affected systems. The vulnerabilities are listed below - CVE-2026-108186 (CVSS score: 9.6) - An improper input validation vulnerability that could allow an unauthenticated user to conduct an escalation of privilege via
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Zoom Workplace Flaw Could Allow Unauthenticated Remote Privilege Escalation
  - Published: 2026-11-11T16:12:46+00:00
  - Link: https://thehackernews.com/2026/11/critical-zoom-workplace-flaw-could.html
  - Summary: Zoom has released software updates to address two security flaws impacting Zoom Workplace for Windows, including a critical bug that could result in privilege escalation on affected systems. The vulnerabilities are listed below - CVE-2026-108186 (CVSS score: 9.6) - An improper input validation vulnerability that could allow an unauthenticated user to conduct an escalation of privilege via

### Cluster 97a136a081 — score 8

- Title: Maersk Reveals Data Breach as Extortion Group Demands $5m
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-11-12T08:49:00+00:00
- Link: https://www.infosecurity-magazine.com/news/maersk-data-breach-extortion-group/
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
Maersk has revealed a threat actor extracted data from one of its legacy systems
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Maersk Reveals Data Breach as Extortion Group Demands $5m
  - Published: 2026-11-12T08:49:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/maersk-data-breach-extortion-group/
  - Summary: Maersk has revealed a threat actor extracted data from one of its legacy systems

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

### Cluster 66b9493205 — score 8

- Title: 0% GPU utilization: How SANSAR hides Linux cryptomining
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-11-12T10:48:47+00:00
- Link: https://www.elastic.co/security-labs/threat-command/sansar-linux-cryptomining-malware
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Elastic Security Labs analyzes SANSAR, a Linux cryptomining orchestrator that manages miners over Tor, alongside a kernel rootkit, GPU monitoring hooks and a backdoor that retrieves its C2 address from Ethereum.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: 0% GPU utilization: How SANSAR hides Linux cryptomining
  - Published: 2026-11-12T10:48:47+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/sansar-linux-cryptomining-malware
  - Summary: Elastic Security Labs analyzes SANSAR, a Linux cryptomining orchestrator that manages miners over Tor, alongside a kernel rootkit, GPU monitoring hooks and a backdoor that retrieves its C2 address from Ethereum.
