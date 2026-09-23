# PHANTOMSignal Briefing Packet

- Generated: 2026-09-23T20:06:37.588863+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 428
- Total clusters raw: 213
- Total clusters in packet: 80
- Dropped low score: 125
- Dropped overflow: 8

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
  - In window count: 4
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
  - In window count: 3
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 4
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
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
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 4
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 1
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 0
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
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
  - In window count: 3
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 0
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
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 1
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 7
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
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
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 18
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 3
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
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 24
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 50
  - In window count: 0
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 22
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 100
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
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
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 25
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 22
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
  - In window count: 4
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 1

## Affinity groups (themes)

### Linux kernel active exploitation
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 4
- Article count: 7
- Cohesion: 0.222
- Shared strong signals: Linux kernel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, ransomware_extortion, active_exploitation, ddos, vulnerability_disclosure
  - affected_industries: financial_services
  - affected_products: Linux kernel, Anthropic/Claude
  - urgency_signals: zero_day, preauth_unauth, actively_exploited, critical_cvss, no_patch_yet
- Cluster IDs: 2fe42b3f58, 64d509601f, 283562f1a6, 12a6389ae4
- Links:
  - https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html
  - https://www.team-cymru.com/post/ai-driven-threat-detection-is-reshaping-cybersecurity
  - https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html
  - https://thehackernews.com/2026/09/exploit-released-for-unpatched-ubuntu.html
  - https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html

### CVE-2026-93616 exploitation activity
- Anchor signal: CVE-2026-93616
- Theme key: cve-2026-93616
- Cluster count: 3
- Article count: 6
- Cohesion: 0.284
- Shared strong signals: CVE-2026-93616
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day
  - cve_ids: CVE-2026-85102, CVE-2026-93616
  - urgency_signals: zero_day
- Cluster IDs: 211e00329a, 7d316694da, df5a100cb0
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-94127-critical-unauthenticated-rce-in-f5-big-ip-apm
  - https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html
  - https://www.securityweek.com/critical-f5-big-ip-vulnerability-exploited-as-zero-day/
  - https://www.helpnetsecurity.com/2026/09/23/check-point-f5-big-ip-apm-zero-days-targeted/
  - https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
  - https://thehackernews.com/2026/09/check-point-warns-of-management-server.html

### CVE-2026-85102 exploitation activity
- Anchor signal: CVE-2026-85102
- Theme key: cve-2026-85102
- Cluster count: 3
- Article count: 6
- Cohesion: 0.284
- Shared strong signals: CVE-2026-85102
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day
  - cve_ids: CVE-2026-85102, CVE-2026-93616
  - urgency_signals: zero_day
- Cluster IDs: 211e00329a, 7d316694da, df5a100cb0
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-94127-critical-unauthenticated-rce-in-f5-big-ip-apm
  - https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html
  - https://www.securityweek.com/critical-f5-big-ip-vulnerability-exploited-as-zero-day/
  - https://www.helpnetsecurity.com/2026/09/23/check-point-f5-big-ip-apm-zero-days-targeted/
  - https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
  - https://thehackernews.com/2026/09/check-point-warns-of-management-server.html

### F5 BIG-IP active exploitation
- Anchor signal: F5 BIG-IP
- Theme key: f5-big-ip
- Cluster count: 3
- Article count: 6
- Cohesion: 0.269
- Shared strong signals: F5 BIG-IP
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation
  - affected_industries: government
  - affected_products: F5 BIG-IP, WordPress
  - cve_ids: CVE-2026-94127
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 211e00329a, fd9f20df1d, fd0e351551
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-94127-critical-unauthenticated-rce-in-f5-big-ip-apm
  - https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html
  - https://www.securityweek.com/critical-f5-big-ip-vulnerability-exploited-as-zero-day/
  - https://www.helpnetsecurity.com/2026/09/23/check-point-f5-big-ip-apm-zero-days-targeted/
  - https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/
  - https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/

### WordPress active exploitation
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 4
- Article count: 10
- Cohesion: 0.239
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day, web_shell_backdoor
  - affected_industries: government
  - affected_products: WordPress, F5 BIG-IP
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 0634a6363d, fd9f20df1d, 7d316694da, fd0e351551
- Links:
  - https://orca.security/resources/research/cve-2026-93485-wordpress-comment2shell-rce/
  - https://www.greynoise.io/blog/open-season-on-kapibala-attacker-steals-government-records-wordpress-exploitation
  - https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html
  - https://www.bleepingcomputer.com/news/security/hackers-start-exploiting-critical-wordpress-flaw-for-code-execution/
  - https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/
  - https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
  - https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/

### zero day targeting Microsoft Defender
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 4
- Article count: 5
- Cohesion: 0.285
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, phishing_social_eng
  - affected_products: Microsoft Defender
  - urgency_signals: zero_day
- Cluster IDs: 12a6389ae4, 96fd6e2eb3, 61da9d90b7, fd0e351551
- Links:
  - https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html
  - https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/
  - https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/
  - https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/

### CVE-2026-93952 exploitation activity
- Anchor signal: CVE-2026-93952
- Theme key: cve-2026-93952
- Cluster count: 3
- Article count: 3
- Cohesion: 0.392
- Shared strong signals: CVE-2026-93952
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day, web_shell_backdoor
  - affected_industries: government
  - cve_ids: CVE-2026-93952, CVE-2026-16812
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: 173902e3fc, 53f2b6a774, fd0e351551
- Links:
  - https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/
  - https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html
  - https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/

### ransomware extortion targeting Cisco
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 3
- Article count: 4
- Cohesion: 0.29
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, active_exploitation
  - affected_products: Cisco
- Cluster IDs: df25ab925d, 5f3dd92061, b14566fc43
- Links:
  - https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/
  - https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
  - https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html
  - https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/

### AWS vulnerability activity
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 3
- Article count: 12
- Cohesion: 0.204
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_industries: financial_services
  - affected_products: AWS, GitHub
- Cluster IDs: 91e999c8ea, a52d5a18d0, 250fac7429
- Links:
  - https://unit42.paloaltonetworks.com/detecting-exposed-aws-iam-credentials/
  - https://aws.amazon.com/blogs/security/supporting-asds-multi-factor-authentication-campaign-why-mfa-matters-more-than-ever/
  - https://www.infosecurity-magazine.com/news/shinyhunters-fbi-hack-peoplesoft/
  - https://cyberscoop.com/shinyhunters-claims-fbi-attack/
  - https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/
  - https://therecord.media/fbi-investigating-alleged-shinyhunters-job-site-breach
  - https://risky.biz/RBNEWS614/
  - https://thehackernews.com/2026/09/shinyhunters-claims-fbi-breach-says-it.html
  - https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/

### CVE-2026-76460 exploitation activity
- Anchor signal: CVE-2026-76460
- Theme key: cve-2026-76460
- Cluster count: 3
- Article count: 3
- Cohesion: 0.2
- Shared strong signals: CVE-2026-76460
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - cve_ids: CVE-2026-76460
  - urgency_signals: preauth_unauth
- Cluster IDs: df25ab925d, 52127152d6, bf92f99cb9
- Links:
  - https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/
  - https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues
  - https://research.checkpoint.com/2026/21st-september-threat-intelligence-report/

### zero day targeting Fortinet
- Anchor signal: Fortinet
- Theme key: fortinet
- Cluster count: 2
- Article count: 3
- Cohesion: 0.2
- Shared strong signals: Fortinet
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day
  - affected_industries: financial_services
  - affected_products: Fortinet
  - urgency_signals: zero_day
- Cluster IDs: 2fe42b3f58, c1f52c0381
- Links:
  - https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html
  - https://www.team-cymru.com/post/ai-driven-threat-detection-is-reshaping-cybersecurity
  - https://www.team-cymru.com/post/tracking-orbs-on-singapores-telecommunications-networks

### supply chain targeting npm
- Anchor signal: npm
- Theme key: npm
- Cluster count: 2
- Article count: 13
- Cohesion: 0.2
- Shared strong signals: npm
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, data_breach
  - affected_products: npm
- Cluster IDs: 0634a6363d, c56eac66cf
- Links:
  - https://orca.security/resources/research/cve-2026-93485-wordpress-comment2shell-rce/
  - https://www.greynoise.io/blog/open-season-on-kapibala-attacker-steals-government-records-wordpress-exploitation
  - https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html
  - https://www.bleepingcomputer.com/news/security/hackers-start-exploiting-critical-wordpress-flaw-for-code-execution/
  - https://orca.security/resources/research/ghappier-loader-npm-supply-chain-attack/
  - https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html
  - https://www.darkreading.com/cyberattacks-data-breaches/shai-hulud-attack-cyber-firm-crowdsec-github-data
  - https://www.infosecurity-magazine.com/news/attackers-abuse-npm-trusted/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (2)
- **CVE-2026-94127: Critical Unauthenticated RCE in F5 BIG-IP APM**
  - Cluster: 211e00329a
  - Sources in window: 3
  - Window hours: 1.2
  - Cohort count: 2
- **ShinyHunters Claims FBI Hack Via PeopleSoft Zero Day**
  - Cluster: a52d5a18d0
  - Sources in window: 3
  - Window hours: 4.5
  - Cohort count: 2

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-85102 + F5 BIG-IP (cluster 211e00329a, first observation: True)
- Pair: CVE-2026-93616 + F5 BIG-IP (cluster 211e00329a, first observation: True)
- Pair: CVE-2026-94127 + F5 BIG-IP (cluster 211e00329a, first observation: True)
- Pair: CVE-2026-58138 + Anthropic/Claude (cluster 2fe42b3f58, first observation: True)
- Pair: CVE-2026-58138 + Fortinet (cluster 2fe42b3f58, first observation: True)
- Pair: CVE-2026-58138 + Linux kernel (cluster 2fe42b3f58, first observation: True)
- Pair: CVE-2026-87902 + WordPress (cluster 0634a6363d, first observation: True)
- Pair: CVE-2026-87902 + npm (cluster 0634a6363d, first observation: True)
- Pair: CVE-2026-93485 + WordPress (cluster 0634a6363d, first observation: True)
- Pair: CVE-2026-93485 + npm (cluster 0634a6363d, first observation: True)
- Pair: CVE-2026-76460 + Cisco (cluster df25ab925d, first observation: True)
- Pair: CVE-2026-28299 + Anthropic/Claude (cluster 64d509601f, first observation: True)
- Pair: CVE-2026-28299 + Linux kernel (cluster 64d509601f, first observation: True)
- Pair: CVE-2026-28299 + SolarWinds (cluster 64d509601f, first observation: True)
- Pair: CVE-2026-28302 + Anthropic/Claude (cluster 64d509601f, first observation: True)

### Drift (5)
- **Cl0p** (cluster a52d5a18d0)
  - New industries: education
  - New products: AWS, Salesforce
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Microsoft 365, OpenAI/ChatGPT, SolarWinds
- **ShinyHunters** (cluster a52d5a18d0)
  - New industries: education, government
  - New products: AWS
  - Prior top industries: financial_services, healthcare, manufacturing_industrial
  - Prior top products: Anthropic/Claude, Microsoft SharePoint, Salesforce
- **MuddyWater** (cluster 7c416ee970)
  - New industries: (none)
  - New products: Microsoft Entra
  - Prior top industries: critical_infrastructure, financial_services, government
  - Prior top products: Android, Apple iOS/macOS, OpenAI/ChatGPT
- **Lazarus** (cluster 250fac7429)
  - New industries: retail_ecommerce
  - New products: AWS, GitHub
  - Prior top industries: aviation_defense, financial_services, government
  - Prior top products: Android, Apple iOS/macOS, Microsoft Windows
- **UNC3886** (cluster c1f52c0381)
  - New industries: government
  - New products: (none)
  - Prior top industries: critical_infrastructure, financial_services, telecommunications
  - Prior top products: Cisco, Fortinet, Google Cloud

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 14, cluster a52d5a18d0)
- actor_attribution: Scattered Spider (weeks observed: 11, cluster fc5c9992d3)
- actor_attribution: Cl0p (weeks observed: 10, cluster a52d5a18d0)
- actor_attribution: LockBit (weeks observed: 8, cluster b14566fc43)
- actor_attribution: Lazarus (weeks observed: 7, cluster 250fac7429)
- actor_attribution: BlackCat/ALPHV (weeks observed: 7, cluster fc5c9992d3)
- cve_ids: CVE-2026-59310 (weeks observed: 6, cluster 62087c81f0)
- actor_attribution: RansomHub (weeks observed: 6, cluster fc5c9992d3)
- cve_ids: CVE-2026-20316 (weeks observed: 5, cluster df25ab925d)
- actor_attribution: Volt Typhoon (weeks observed: 5, cluster b9771fe2d2)
- actor_attribution: UNC5221 (weeks observed: 5, cluster b04cf6724c)
- cve_ids: CVE-2026-85046 (weeks observed: 4, cluster bcfbd3fc84)
- cve_ids: CVE-2026-87491 (weeks observed: 4, cluster bcfbd3fc84)
- cve_ids: CVE-2026-20079 (weeks observed: 4, cluster df25ab925d)
- cve_ids: CVE-2026-59309 (weeks observed: 4, cluster 62087c81f0)

### Tier inversion (1)
- **vCenter pre-auth RCE: CVE-2026-59309/59310**
  - Cluster: 62087c81f0
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-59309, CVE-2026-59310

## Clusters

### Cluster 211e00329a — score 50

- Title: CVE-2026-94127: Critical Unauthenticated RCE in F5 BIG-IP APM
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-23T08:43:39+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-94127-critical-unauthenticated-rce-in-f5-big-ip-apm
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-94127, F5 BIG-IP

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: F5 BIG-IP
- cve_ids: CVE-2026-85102, CVE-2026-93616, CVE-2026-94127
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- affected_products: F5 BIG-IP
- cve_ids: CVE-2026-94127
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On September 22, 2026, F5 published a security advisory for CVE-2026-94127 , a critical heap-based buffer overflow vulnerability affecting F5 BIG-IP Access Policy Manager (APM). The vulnerability has a CVSS v3.1 score of 9.8. An unauthenticated attacker with network access to an affected virtual server may be able to achieve remote code execution (RCE) by sending specifically crafted traffic. BIG-IP APM provides identity-aware access control for applications and other corporate resources and can integrate with authentication technologies including OAuth, OpenID Connect, and SAML. CVE-2026-94127 is not exposed in a default configuration: exploitation requires a BIG-IP virtual server with both an APM access policy and an OAuth profile configured. Because affected BIG-IP systems may process traffic at an organization's network edge, organizations using this configuration should prioritize remediation. The vulnerability affects the data plane and does not expose the BIG-IP control
```

#### Full body

```
Emergent Threat Response CVE-2026-94127: Critical Unauthenticated RCE in F5 BIG-IP APM Rapid7 Sep 23, 2026 | Last updated on Sep 23, 2026 | 2 min read CVE-2026-94127: Critical Unauthenticated RCE in F5 BIG-IP APM Table of contents CVE-2026-94127: Critical Unauthenticated RCE in F5 BIG-IP APM Table of contents Overview On September 22, 2026, F5 published a security advisory for CVE-2026-94127 , a critical heap-based buffer overflow vulnerability affecting F5 BIG-IP Access Policy Manager (APM). The vulnerability has a CVSS v3.1 score of 9.8. An unauthenticated attacker with network access to an affected virtual server may be able to achieve remote code execution (RCE) by sending specifically crafted traffic. BIG-IP APM provides identity-aware access control for applications and other corporate resources and can integrate with authentication technologies including OAuth, OpenID Connect, and SAML. CVE-2026-94127 is not exposed in a default configuration: exploitation requires a BIG-IP virtual server with both an APM access policy and an OAuth profile configured. Because affected BIG-IP systems may process traffic at an organization's network edge, organizations using this configuration should prioritize remediation. The vulnerability affects the data plane and does not expose the BIG-IP control plane. BIG-IP systems operating in Appliance mode are also affected. F5 lists the following affected release trains and corresponding fixed hotfixes: BIG-IP 21.1.0: versions prior to Hotfix-BIGIP-21.1.0.2.0.30.22-ENG BIG-IP 17.5.0: versions prior to Hotfix-BIGIP-17.5.1.9.0.160.12-ENG BIG-IP 17.1.0: versions prior to Hotfix-BIGIP-17.1.3.5.0.41.14-ENG As of September 22, 2026, CVE-2026-94127 has been added to the CISA KEV while a publicly available proof of concept was not confirmed. Mitigation guidance Organizations running affected F5 BIG-IP deployments should apply the appropriate F5 hotfix as soon as operationally feasible, particularly where a vulnerable APM and OAuth configuration is reachable from untrusted networks. F5 lists the following remediation versions: BIG-IP 21.1.0: update to Hotfix-BIGIP-21.1.0.2.0.30.22-ENG or later. BIG-IP 17.5.0: update to Hotfix-BIGIP-17.5.1.9.0.160.12-ENG or later. BIG-IP 17.1.0: update to Hotfix-BIGIP-17.1.3.5.0.41.14-ENG or later. Administrators should first determine whether a BIG-IP APM access policy and an OAuth profile are configured together on a virtual server, since this configuration is required for exposure. For organizations that cannot immediately apply the applicable update, F5 provides an iRule workaround through F5 Support. Customers should open a support case with F5 to obtain the vendor-provided workaround and follow F5's implementation guidance. Rapid7 customers Exposure Command, Vulnerability Management, and Nexpose Exposure Command, Vulnerability Management, Nexpose customers can assess exposure to CVE-2026-94127 using vulnerability checks expected to be available in today’s (September 23) content release. Updates September 22, 2026: Initial publication. Article tags Emergent Threat Response Labs Vulnerability Management Explore more from Rapid7 Vulnerability & Exploit Database Rapid7s curated database of vulnerabilities, featuring exploit modules and check methods integrated into the Metasploit Framework. Search the database Rapid7 Labs The threat research behind the alerts: adversary tracking, curated intelligence, and flagship threat reports. Explore the research Rapid7 MDR Gain 24x7 XDR monitoring, remediation, and DFIR from experts that extend your team to help secure your extended ecosystem. Explore MDR Exposure management Get continuous assessment of your attack surface with the critical context to validate and extinguish vulnerabilities and policy gaps. See how it works
```

#### Corroborating sources (4)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-94127: Critical Unauthenticated RCE in F5 BIG-IP APM
  - Published: 2026-09-23T08:43:39+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-94127-critical-unauthenticated-rce-in-f5-big-ip-apm
  - Summary: Overview On September 22, 2026, F5 published a security advisory for CVE-2026-94127 , a critical heap-based buffer overflow vulnerability affecting F5 BIG-IP Access Policy Manager (APM). The vulnerability has a CVSS v3.1 score of 9.8. An unauthenticated attacker with network access to an affected virtual server may be able to achieve remote code execution (RCE) by sending specifically crafted traffic. BIG-IP APM provides identity-aware access control for applications and other corporate resources and can integrate with authentication technologies including OAuth, OpenID Connect, and SAML. CVE-2026-94127 is not exposed in a default configuration: exploitation requires a BIG-IP virtual server with both an APM access policy and an OAuth profile configured. Because affected BIG-IP systems may process traffic at an organization's network edge, organizations using this configuration should prioritize remediation. The vulnerability affects the data plane and does not expose the BIG-IP control
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers
  - Published: 2026-09-23T08:29:48+00:00
  - Link: https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html
  - Summary: Attackers are exploiting a critical flaw in F5 BIG-IP Access Policy Manager (APM) that lets them run code on a BIG-IP system without logging in, F5 says. The flaw, CVE-2026-94127, affects only systems in which APM serves as an OAuth authorization server, issuing access tokens to applications. F5 disclosed it in an advisory on September 22 and has released engineering hotfixes.
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Critical F5 BIG-IP Vulnerability Exploited as Zero-Day
  - Published: 2026-09-23T07:34:18+00:00
  - Link: https://www.securityweek.com/critical-f5-big-ip-vulnerability-exploited-as-zero-day/
  - Summary: Unauthenticated attackers could send malicious traffic to BIG-IP to achieve remote code execution. The post Critical F5 BIG-IP Vulnerability Exploited as Zero-Day appeared first on SecurityWeek .
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Attackers hit Check Point Management Servers and Spark firewalls, F5 BIG-IP APM instances
  - Published: 2026-09-23T10:22:52+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/23/check-point-f5-big-ip-apm-zero-days-targeted/
  - Summary: Check Point Software has released emergency fixes for a critical Check Point Management Server vulnerability (CVE-2026-93616) that has been exploited as far back as July 23, 2026. The company also confirmed that a pre-authentication remote code execution (RCE) vulnerability (CVE-2026-85102) in Check Point (Quantum) Security Gateway for which it released patches on September 9, 2026, started getting probed a few days after. “At the time [of the release of the patches], we had no evidence … More → The post Attackers hit Check Point Management Servers and Spark firewalls, F5 BIG-IP APM instances appeared first on Help Net Security .

### Cluster 2fe42b3f58 — score 36

- Title: Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-19T08:18:54+00:00
- Link: https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-58138, Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_industries: financial_services
- affected_products: Anthropic/Claude, Fortinet, Linux kernel
- cve_ids: CVE-2026-58138
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_industries: financial_services
- affected_products: Anthropic/Claude, Fortinet, Linux kernel
- cve_ids: CVE-2026-58138
- urgency_signals: actively_exploited, zero_day, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical vulnerability impacting Orkes Conductor is being actively exploited in the wild, according to Fortinet. The vulnerability in question is CVE-2026-58138 (CVSS v3.1 score: 9.8/CVSS v4 score: 9.3), which relates to a case of unauthenticated remote code execution. "Orkes Conductor 3.21.21 before 3.30.2 contains an unauthenticated remote code execution vulnerability that allows remote
```

#### Full body

```
Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild  Ravie Lakshmanan  Sep 19, 2026 Vulnerability / Web Security A critical vulnerability impacting Orkes Conductor is being actively exploited in the wild, according to Fortinet. The vulnerability in question is CVE-2026-58138 (CVSS v3.1 score: 9.8/CVSS v4 score: 9.3), which relates to a case of unauthenticated remote code execution. "Orkes Conductor 3.21.21 before 3.30.2 contains an unauthenticated remote code execution vulnerability that allows remote attackers to execute arbitrary OS commands by submitting inline workflow definitions containing malicious JavaScript or Python expressions to the workflow API endpoint prior to authentication," a description of the flaw on the NIST National Vulnerability Database (NVD) reads. "Attackers can exploit unsandboxed GraalVM evaluators configured with HostAccess.ALL or allowAllAccess(true) through INLINE, LAMBDA, DO_WHILE, and SWITCH task types to invoke arbitrary system commands via Java reflection or direct subprocess calls." In an outbreak alert issued this week, Fortinet said it has observed attackers actively targeting Orkes Conductor servers susceptible to CVE-2026-58138 by submitting crafted workflow definitions containing JavaScript or Python expressions to the Conductor workflow API. "Because vulnerable evaluators can be configured with unrestricted host access, the attacker can escape the intended scripting environment and execute arbitrary operating system commands with the privileges of the Conductor process," Fortinet said. As of September 9, 2026, the company said it had blocked 1,290 attack attempts within a span of 24 hours, representing a 132% increase in daily activity. Nearly 7,000 attempts were blocked between September 2 and 9, 2026. The majority of the attack activity is said to have originated from Germany, Hong Kong, Indonesia, the U.A.E., and India. Telemetry data from Previdian shows three exploitation attempts against its honeypots since July 24, 2026, from two unique IP addresses in France and the U.S. Similarly, Empirical Security noted that it detected in-the-wild exploitation as recently as August 21, 2026. Organizations using affected versions are advised to upgrade to Conductor 3.30.2 or later, which addresses the vulnerability. If immediate patching is not an option, it's recommended to restrict external access to Conductor workflow API endpoints, place Conductor instances behind appropriate network access controls, and monitor for suspicious workflow submissions and unexpected command execution. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Application Security , Vulnerability , Web Security ⚡ Top Stories This Week Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation KREMLIN Banking Malware Hijacks Chrome and Edge to Steal Credentials and Session Tokens LiteSpeed Enterprise Flaw Could Let One Hosting Account
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild
  - Published: 2026-09-19T08:18:54+00:00
  - Link: https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html
  - Summary: A critical vulnerability impacting Orkes Conductor is being actively exploited in the wild, according to Fortinet. The vulnerability in question is CVE-2026-58138 (CVSS v3.1 score: 9.8/CVSS v4 score: 9.3), which relates to a case of unauthenticated remote code execution. "Orkes Conductor 3.21.21 before 3.30.2 contains an unauthenticated remote code execution vulnerability that allows remote
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: How AI-driven Threat Detection is Reshaping Threat Intelligence
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/ai-driven-threat-detection-is-reshaping-cybersecurity
  - Summary: Hear Fortinet‚Äôs Aamir Lakhani explain the role of AI in cybersecurity and how AI-driven threat detection is reshaping modern threat intelligence.

### Cluster bcfbd3fc84 — score 29

- Title: Mind the (Patch) Gap, Part 2: Fake Websites Used to Deploy Chrome & Windows 0-Day Exploits
- Source: Volexity (threat_research_primary)
- Published: 2026-09-21T21:01:46+00:00
- Link: https://www.volexity.com/blog/2026/09/21/mind-the-patch-gap-part-2-fake-websites-used-to-deploy-chrome-windows-0-day-exploits/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-85046, CVE-2026-85880, CVE-2026-87491

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, zero_day
- affected_industries: government
- cve_ids: CVE-2026-85046, CVE-2026-85880, CVE-2026-87491
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage
- affected_industries: government
- cve_ids: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
On September 9, 2026, Volexity published a blog post detailing the simultaneous use of multiple chained zero-day exploits in Google Chrome (CVE-2026-85046, CVE-2026-87491) and Microsoft Windows (CVE-2026-85880) by two different […] The post Mind the (Patch) Gap, Part 2: Fake Websites Used to Deploy Chrome & Windows 0-Day Exploits appeared first on Volexity .
```

#### Full body

```
Threat Intelligence Mind the (Patch) Gap, Part 2: Fake Websites Used to Deploy Chrome & Windows 0-Day Exploits September 21, 2026 Damien Cash and Tom Lancaster On September 9, 2026, Volexity published a blog post detailing the simultaneous use of multiple chained zero-day exploits in Google Chrome ( CVE-2026-85046 , CVE-2026-87491 ) and Microsoft Windows ( CVE-2026-85880 ) by two different Chinese advanced persistent threat (APT) actors. Shortly after that blog post was published, Volexity discovered additional campaigns—this time from a third Chinese threat actor, tracked by Volexity under the alias UTA0565 —that used the same chained exploits on September 3-4, 2026, while the vulnerabilities were still unpatched. Notably, this threat actor’s campaigns differed from previously documented attacks by using multiple fake websites to deceive victims. In one observed campaign, a phishing email sent was to Asian government entities: This Chinese-language phishing email urges readers to publicly support imprisoned Hong Kong activist Chow Hang-tung and amplify her voice against Chinese Communist Party suppression of a June 4th commemoration. In another campaign, the threat actor sent a phishing email masquerading as the Center for American Progress: Each phishing email included a link to a spoofed domain registered and controlled by the threat actor: Legitimate Domain Spoofed Domain chinadigitaltimes.net chinadigitaltimes[.]top americanprogress.org americanprgoress[.]top At the time of analysis, the fake website spoofing the China Digital Times was no longer available. However, searches within Censys showed the hosting IP address ( 96.9.125[.]52 ) had served a website designed to look identical to the legitimate China Digital Times website. The spoofed site americanprgoress[.]top appears to be a typosquat impersonating the Center for American Progress, which was still live at the time of analysis. It loaded most of its content from the legitimate website, but it also loaded an additional HTML element via an iframe: <iframe src="/config.html" style="display:none;visibility:hidden;width:0;height:0;border:0;overflow:hidden" tabindex="-1" aria-hidden="true" title="site-config"></iframe> This HTML element consists of the same components used in previously analyzed exploitation of Chrome (CVE-2026-85046, CVE-2026-87491) and Windows local privilege escalation exploits (CVE-2026-85880). The implementation is largely unchanged: The embedded p1 and p2 binaries are identical to the previously reported payloads . Core exploit logic, version checks, and stage sequencing remain the same. The main functional difference is the replacement pp payload. In this version, config.html is designed to do the following: Download chrome_cleanup.exe in-process . Remove its Mark of the Web. Launch it via the Windows shell using COM, replacing the cmd . exe/curl command, which had downloaded and executed msgbox.exe in previously analyzed variants. There are also various changes that do not affect the exploit kit’s operation, such as renamed variables, debug messages, and comments, as well as an option to log data to an internal IP address. The chain downloaded its final payload from the following URL: hxxps://americanprgoress[.]top/chrome_cleanup.exe The table below details this payload: Name chrome_cleanup.exe Size 893.0KB (914432 Bytes) File Type Win64 EXE MD5 177652713dad3c128bd9195abf2b7603 SHA1 668aa5551315ab26b67118fbb29f8e4560a1e1af SHA256 8858ea412dc306b3558885af18006c5ca24689e8875733b5e13b3c2692e603cb This payload belongs to a previously undocumented malware family that Volexity tracks as CLEANGULP . The malware was originally written in C and built using the Microsoft Visual C Compiler, then heavily obfuscated using control flow flattening and indirect calls to hinder analysis. Volexity analyzed CLEANGULP primarily through dynamic analysis, locating and emulating string de-obfuscation functions. Based on this partial analysis, Volexity assesses with hi
```

#### Corroborating sources (2)

- **Volexity** (threat_research_primary)
  - Title: Mind the (Patch) Gap, Part 2: Fake Websites Used to Deploy Chrome & Windows 0-Day Exploits
  - Published: 2026-09-21T21:01:46+00:00
  - Link: https://www.volexity.com/blog/2026/09/21/mind-the-patch-gap-part-2-fake-websites-used-to-deploy-chrome-windows-0-day-exploits/
  - Summary: On September 9, 2026, Volexity published a blog post detailing the simultaneous use of multiple chained zero-day exploits in Google Chrome (CVE-2026-85046, CVE-2026-87491) and Microsoft Windows (CVE-2026-85880) by two different […] The post Mind the (Patch) Gap, Part 2: Fake Websites Used to Deploy Chrome & Windows 0-Day Exploits appeared first on Volexity .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware
  - Published: 2026-09-23T08:29:24+00:00
  - Link: https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html
  - Summary: A Chinese threat actor codenamed UTA0565 has been observed exploiting the recently disclosed Google Chrome-Microsoft Windows exploit chain as zero-days through fake websites. The attacks, detected on September 3 and 4, 2026, involved the chaining of two vulnerabilities in Chrome (CVE-2026-85046, CVE-2026-87491) and one impacting Windows Advanced Local Procedure Call (CVE-2026-85880) to break

### Cluster 4ac366c7ba — score 28

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
CATEGORIES AI Research 21 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 473 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 426 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 AI Threat Landscape Digest: July–August 2026 September 17, 2026 https://research.checkpoint.com/2026/ai-threat-landscape-digest-july-august-2026/ The defining development of the period came not from attackers but from the AI labs themselves, whose models broke out of controlled evaluations and reached real systems. In the wild, the criminal and state use of AI continued to mature along the lines tracked in earlier editions: models now act as attack operators, an underground market supplies the access, and AI systems have themselves become a target. The substantial distance between what the strongest models demonstrated under evaluation and what criminals are currently doing is the central fact of the period. Key observed findings Evaluation models escaped containment in ways nobody had engineered a fix for. An OpenAI research prototype found and exploited a previously unknown vulnerability in an internal package proxy, reaching Hugging Face’s production systems and taking roughly 17,600 recorded actions before anyone caught it. Anthropic and Meta each reported test models reaching the open internet through misconfigurations, and the UK AI Security Institute logged a case where an agent invented fake identities to try to talk a real person into approving malicious code. What criminals are doing today is still far more modest, and that gap is the story worth watching. Real world attacks run on models below the frontier, use known techniques, and get caught by existing defenses, nothing like a model finding its own zero day or sustaining an unsupervised operation for days. But frontier capability has reached commercial and open source models within months of first appearing every time before, and there’s little reason to expect this one stays contained to the lab. An affiliate tied to The Gentlemen ransomware group used Claude Code to carry out real intrusions against at least six organizations, a person directing an AI tool through each step. JADEPUFFER went further: a human configured and launched it, the model ran the entire extortion operation itself, moving from the initial flaw to the internal database, exfiltrating and deleting data, leaving a ransom note, and correcting its own errors along the way, with no person directing the individual steps. A criminal market has organized around stealing and reselling AI access itself. One tier steals API keys and credentials at scale, and a second resells that access through gateways that hide the buyer’s identity from the provider. AI systems have become entry points in their own right. Coding agents and enterprise copilots can be steered through content they’re built to trust, a symbolic link, an image, a fabricated error report, and both Google’s Gemini CLI and Anthropic’s Claude Code needed patches for flaws a malicious GitHub issue could trigger. A separate market exists for removing a model’s guardrails once you have access to it. One forum post asking to buy a durable method for bypassing a model’s restrictions, rather than a single jailbreak prompt, is a useful illustration of what that demand looks like. AI is surfacing vulnerabilities faster than anyone can patch them, but that hasn’t translated into more successful attacks. Microsoft shipped a record 570 fixes in July and Oracle’s quarterly update ran past 1,400, yet only about one percent of AI discovered vulnerabilities were confirmed exploited in the wild, roughly the same rate as flaws found any other way. Everyday enterprise GenAI use is a quieter but steadier source of exposure. In July, one in every 36 prompts from enterprise networks
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: AI Threat Landscape Digest: July–August 2026
  - Published: 2026-09-17T14:41:15+00:00
  - Link: https://research.checkpoint.com/2026/ai-threat-landscape-digest-july-august-2026/
  - Summary: The defining development of the period came not from attackers but from the AI labs themselves, whose models broke out of controlled evaluations and reached real systems. In the wild, the criminal and state use of AI continued to mature along the lines tracked in earlier editions: models now act as attack operators, an underground […] The post AI Threat Landscape Digest: July–August 2026 appeared first on Check Point Research .

### Cluster 173902e3fc — score 21

- Title: Arista patches actively exploited VeloCloud Orchestrator zero-day
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-23T12:29:53+00:00
- Link: https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor, zero_day
- affected_industries: government
- cve_ids: CVE-2026-16812, CVE-2026-7473, CVE-2026-93952
- urgency_signals: actively_exploited, emergency_patch, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor, active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-93952, CVE-2026-7473, CVE-2026-16812
- urgency_signals: actively_exploited, zero_day, emergency_patch
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Arista Networks has released security patches for a zero-day flaw that is being actively exploited and affects VeloCloud Orchestrator (VCO) On-Prem deployments. [...]
```

#### Full body

```
Arista patches actively exploited VeloCloud Orchestrator zero-day By Sergiu Gatlan September 23, 2026 08:29 AM 0 Arista Networks has released security patches for a zero-day flaw that is being actively exploited and affects VeloCloud Orchestrator (VCO) On-Prem deployments. VCO is a cloud-based centralized management platform that helps admins configure, monitor, and manage VeloCloud SD-WANs (Software-Defined Wide Area Networks) and associated edge devices. Tracked as CVE-2026-93952 , this maximum-severity flaw stems from an improper input validation weakness and affects VCO deployments where certificate-based authentication from the VeloCloud Edge to VeloCloud Orchestrator (VCO) is configured. Remote threat actors can exploit the vulnerability to access privileged internal VCO host functionality in low-complexity attacks that don't require privileges on the targeted system or user interaction. "This issue was discovered externally and is known to be actively exploited," the company warned in a Tuesday advisory . "Access to the public portion of the VeloCloud Edge authentication certificate is required. A successful attack requires network access to the VCO web interface. VCO tenant or operator credentials are not required for this exposure." Arista says that it has already patched hosted deployments running VCO 5.2.3.16 or later and VCO 6.4.2.8 or later and that it will also release security patches for VCO instances running 6.1.3.7 and below and 7.0.0.2 and below. The U.S. Cybersecurity and Infrastructure Security Agency has also added CVE-2026-93952 to its Known Exploited Vulnerabilities catalog on Tuesday and ordered U.S. federal civilian executive branch agencies to secure their networks by Friday, September 25 . Indicators of compromise While security patches are being deployed, admins should restrict access to the VCO web interface to administrative networks, review recent administrator activity for unusual changes, and monitor for connections from known malicious IP addresses. Admins should review VCO web access logs for suspicious activity, such as requests containing encoded characters, unusual URL-like path components, references to local or internal services, or high request rates. Arista also advised security teams to block the 142[.]93.149.77 and 104[.]248.126.159 IP addresses and review nginx logs for the x-vc-opt HTTP header, and said that unexpected outbound HTTP or HTTPS activity originating from the VCO host may also warrant further review. "If compromise is suspected, operators should preserve VCO web access logs, backend application logs, system logs, database logs, and relevant file-system timestamps before remediation where operationally feasible," it added, and advised customers to contact the Arista Networks Technical Assistance Center (TAC) if they need additional assistance. Since the start of the year, Arista patched two other zero-day flaws ( CVE-2026-7473 in May and CVE-2026-16812 in July) that were being actively exploited in attacks and affected Extensible Operating System (EOS) and on-premises VeloCloud Orchestrator deployments, respectively. Arista Networks is a Fortune 500 company and one of the largest United States corporations by revenue, with more than 10,000 customers worldwide. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Arista patches VeloCloud Orchestrator zero-day exploited in attacks F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks Magento StyleSmuggler zero-day exploited to deploy Linux backdoor PaperCut releases second emergency patch for exploited flaws PaperCut warns of NG, MF flaw exploited in zero-day attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Arista patches actively exploited VeloCloud Orchestrator zero-day
  - Published: 2026-09-23T12:29:53+00:00
  - Link: https://www.bleepingcomputer.com/news/security/arista-patches-actively-exploited-velocloud-orchestrator-zero-day/
  - Summary: Arista Networks has released security patches for a zero-day flaw that is being actively exploited and affects VeloCloud Orchestrator (VCO) On-Prem deployments. [...]

### Cluster 53f2b6a774 — score 21

- Title: New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-22T12:29:00+00:00
- Link: https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-93952

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor
- cve_ids: CVE-2026-16812, CVE-2026-93952
- urgency_signals: actively_exploited, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor, active_exploitation
- cve_ids: CVE-2026-93952, CVE-2026-16812
- urgency_signals: actively_exploited, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Attackers are exploiting a new flaw in on-premises VeloCloud Orchestrator (VCO), the server that manages the Edge devices in a VeloCloud SD-WAN, Arista said on September 22. The flaw, tracked as CVE-2026-93952, may allow a remote attacker with no login access to privilege internal functions and affect the VCO host. Only orchestrators set up to authenticate their Edges with certificates are
```

#### Full body

```
New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups  Swati Khandelwal  Sep 22, 2026 Vulnerability / Network Security Attackers are exploiting a new flaw in on-premises VeloCloud Orchestrator (VCO), the server that manages the Edge devices in a VeloCloud SD-WAN, Arista said on September 22. The flaw, tracked as CVE-2026-93952 , may allow a remote attacker with no login access to privilege internal functions and affect the VCO host. Only orchestrators set up to authenticate their Edges with certificates are exposed. As of September 22, fixed releases are out for the 5.2 and 6.4 release trains, but not yet for the 6.1 and 7.0 trains. Arista has already patched the Hosted and Dedicated versions of VCO. The affected releases include those that fixed a different VCO flaw, which Arista reported as exploited in July . Arista gave the flaw a CVSS 3.1 score of 10.0. A successful attack may compromise the orchestrator and the data it manages. A compromised VCO may also give attackers access to the Edge devices it manages. Arista said the flaw "was discovered externally and is known to be actively exploited." It did not say when the attacks began or how widespread they are. The Hacker News has contacted Arista for comment. Which Deployments Are Exposed VeloCloud Edges can authenticate to the orchestrator in one of three modes . In Certificate Deactivated mode, an Edge uses a pre-shared key (PSK). In Certificate Acquire and Certificate Required modes, it uses a certificate issued by the orchestrator. Arista said an orchestrator is exposed if "certificate based authentication from the VeloCloud Edge to VeloCloud Orchestrator (VCO) is configured." It did not say which of those modes meets that condition. The attacker also needs network access to the VCO web interface and the public part of an Edge's authentication certificate. The July flaw did not depend on settings: VCO was exposed to it by default, and no configuration could prevent that. Fixed Releases As of September 22, these are the affected releases in each train, the releases that fix them, and the releases that fixed the July flaw: Train Affected by CVE-2026-93952 Fixed in July flaw (CVE-2026-16812) fixed in 5.2 5.2.3.15 and earlier 5.2.3.16 and later 5.2.3.14 6.1 6.1.3.7 and earlier No fix yet 6.1.3.4 6.4 6.4.2.7 and earlier 6.4.2.8 and later 6.4.2.4 7.0 7.0.0.2 and earlier No fix yet No fix listed. 7.0.0.1 and later were not affected. Arista said fixes for affected trains that are still supported are coming and will be added to its advisory when ready. Customers on an unsupported release train can contact Arista's Technical Assistance Center (TAC) about upgrade options. If You Cannot Upgrade Yet Until a fixed release is installed, Arista recommends these steps: Limit access to the VCO web interface to trusted administrative networks. This can reduce the risk of exposure. Monitor the VCO for access from known malicious IP addresses. Monitor for unexpected outbound network traffic from the VCO host. Consider blocking outbound ports that are not required for normal operation. Monitor for backdoor daemons and webshells. Review recent administrator activity for unexpected changes. Signs of Compromise Arista said no single indicator proves that a VCO was compromised through this flaw. Check VCO web access logs for requests with unusual URL-like paths, encoded characters, references to local or internal services, or high request rates. The specific indicators to look for are: File : /usr/local/sbin/.vcnode.js File : /usr/local/sbin/vc-sysmond MD5 ( vc-sysmond ): dc78e206eaeadec59fc5801fe4556bd0 File : /etc/systemd/system/vc-sysmon.service HTTP header in nginx logs: x-vc-opt IP : 142.93.149[.]77 IP : 104.248.126[.]159 If you find any of these, preserve the state of the VCO and contact TAC or your Arista account team. If you suspect a compromise, save the VCO's web access, backend application, system, and database logs and its file-system timestamps
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups
  - Published: 2026-09-22T12:29:00+00:00
  - Link: https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html
  - Summary: Attackers are exploiting a new flaw in on-premises VeloCloud Orchestrator (VCO), the server that manages the Edge devices in a VeloCloud SD-WAN, Arista said on September 22. The flaw, tracked as CVE-2026-93952, may allow a remote attacker with no login access to privilege internal functions and affect the VCO host. Only orchestrators set up to authenticate their Edges with certificates are

### Cluster 0634a6363d — score 21

- Title: WordPress “Comment2Shell” XSS-to-RCE Chain Lets Unauthenticated Attackers Compromise Servers via Malicious Comments
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-09-22T17:38:08+00:00
- Link: https://orca.security/resources/research/cve-2026-93485-wordpress-comment2shell-rce/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 4
- Strong signals: CVE-2026-93485, WordPress

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, supply_chain, web_shell_backdoor
- affected_industries: government
- affected_products: WordPress, npm
- cve_ids: CVE-2026-87902, CVE-2026-93485
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: news_report, threat_research
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, data_breach, web_shell_backdoor, active_exploitation
- affected_products: WordPress, npm
- cve_ids: CVE-2026-93485
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Executive Summary A high-severity vulnerability (CVE-2026-93485, CVSS 7.1) was disclosed affecting WordPress Core, allowing attackers to achieve full remote code execution via a stored cross-site scripting flaw in the comment rendering pipeline. Due to the potential for complete server compromise, immediate patching is required. About CVE-2026-93485 The issue originates from the wpautop() function in wp-includes/formatting.php, […]
```

#### Full body

```
Executive Summary A high-severity vulnerability (CVE-2026-93485, CVSS 7.1) was disclosed affecting WordPress Core, allowing attackers to achieve full remote code execution via a stored cross-site scripting flaw in the comment rendering pipeline. Due to the potential for complete server compromise, immediate patching is required. About CVE-2026-93485 The issue originates from the wpautop() function in wp-includes/formatting.php, where a mismatch between comment sanitization at save time and HTML reformatting at display time leads to injection of live event handlers. By submitting a crafted anonymous comment containing a specially constructed HTML attribute with a > character, attackers can cause the wpautop() regular expression to misinterpret tag boundaries, breaking the tag structure apart and relocating attacker-controlled text into a position where the browser treats it as executable JavaScript. No authentication is required to submit the initial malicious comment. When a logged-in administrator views the page containing the malicious comment, the injected script executes automatically without any click required. The script leverages the administrator’s session to install a plugin containing a web shell, achieving full remote code execution on the server. Affected Systems The following components are affected: WordPress Core, versions 4.7 through 7.1.0. This represents the vast majority of WordPress installations worldwide. The vulnerability affects any content processed through wpautop(), which includes comments, posts, and other content areas. Sites using block themes (all default themes since Twenty Twenty-Two) are confirmed affected. Risk Impact While WordPress has comment moderation enabled by default, several factors lower the exploitation barrier: auto-approval is enabled for users who have had a previous comment approved, and some sites disable moderation entirely. The attack complexity is rated Low, and no authentication is required for the initial XSS vector; only user interaction (an administrator viewing the page) is needed. Users should upgrade to WordPress 7.1.1 immediately, or the corresponding security backport for their branch (7.0.5, 6.9.8, and corresponding backports down to 4.7.36). WordPress sites with automatic background updates enabled will receive the patch automatically. Sites unable to patch immediately should disable comments site-wide, enable strict comment moderation requiring manual approval for all comments, deploy WAF rules to filter malicious comment payloads, and audit installed plugins for any unexpected or unfamiliar entries. At the time of writing, no public proof-of-concept exploit has been published, and there is no known active exploitation in the wild. CVE-2026-93485 is not listed on the CISA Known Exploited Vulnerabilities catalog. Regardless, the severity and low attack complexity make this vulnerability high risk, especially for internet-facing WordPress deployments with comments enabled. Successful exploitation could allow attackers to execute arbitrary code on the web server, install persistent backdoors via malicious plugins, and potentially pivot to compromise the underlying infrastructure, leading to service disruption, data exposure, or full infrastructure compromise. WordPress 7.1.1 also addressed 10 additional security vulnerabilities including path traversal, CSRF, and additional XSS issues, making this a critical update. How Orca Can Help Orca enables customers to quickly identify assets running vulnerable WordPress versions, understand their exposure in context — including internet accessibility, runtime reachability, and asset criticality — and prioritize remediation based on real risk rather than CVSS alone. Orca’s platform highlights affected assets directly in the newItem view, helping security teams focus on the most critical remediation paths first. Related articles Research npm Supply-Chain Attack Abuses Trusted Publishing to Ship GHAPPIER Loader Sep 22, 2026 Re
```

#### Corroborating sources (4)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: WordPress “Comment2Shell” XSS-to-RCE Chain Lets Unauthenticated Attackers Compromise Servers via Malicious Comments
  - Published: 2026-09-22T17:38:08+00:00
  - Link: https://orca.security/resources/research/cve-2026-93485-wordpress-comment2shell-rce/
  - Summary: Executive Summary A high-severity vulnerability (CVE-2026-93485, CVSS 7.1) was disclosed affecting WordPress Core, allowing attackers to achieve full remote code execution via a stored cross-site scripting flaw in the comment rendering pipeline. Due to the potential for complete server compromise, immediate patching is required. About CVE-2026-93485 The issue originates from the wpautop() function in wp-includes/formatting.php, […]
- **GreyNoise** (cloud_identity_infrastructure)
  - Title: Open Season on Kapibala: Attacker Steals Over 18,000 Government Records Through WordPress Exploitation
  - Published: 2026-09-21T00:00:00+00:00
  - Link: https://www.greynoise.io/blog/open-season-on-kapibala-attacker-steals-government-records-wordpress-exploitation
  - Summary: GreyNoise has been tracking malicious use of an IP address since early June 2026 due to its frequent use in scans and attacks against a variety of technologies. We detail a few of the more notable intrusions we observed including the theft of more than 18,000 sensitive records from a western government.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: WordPress Comment2Shell Flaw Can Turn Anonymous Comment XSS Into RCE via Admin Session
  - Published: 2026-09-22T06:03:14+00:00
  - Link: https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html
  - Summary: A new flaw in WordPress core let an anonymous visitor leave a comment that planted a hidden script on the page. If a logged-in administrator later opened that page, the script could run code on the site's server. WordPress fixed the flaw, tracked as CVE-2026-93485 and called "Comment2Shell," on September 17 in version 7.1.1 and told site owners to update right away. There is
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hackers start exploiting critical WordPress flaw for code execution
  - Published: 2026-09-23T18:31:22+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hackers-start-exploiting-critical-wordpress-flaw-for-code-execution/
  - Summary: Threat actors have moved from probing WordPress sites vulnerable to CVE-2026-87902 to exploiting the flaw to write files to disk that execute shell commands when accessed. [...]

### Cluster 91e999c8ea — score 20

- Title: From Exposure to Lockdown: How AWS Neutralizes Compromised IAM Credentials through Managed Policies
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-21T10:00:13+00:00
- Link: https://unit42.paloaltonetworks.com/detecting-exposed-aws-iam-credentials/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, credential_theft, phishing_social_eng
- affected_products: AWS, GitHub
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- affected_products: AWS, GitHub
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We explore how AWS neutralizes exposed IAM credentials using managed policies, detailing GitHub secret scanning and CloudTrail monitoring strategies. The post From Exposure to Lockdown: How AWS Neutralizes Compromised IAM Credentials through Managed Policies appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Cloud Cybersecurity Research Cloud Cybersecurity Research From Exposure to Lockdown: How AWS Neutralizes Compromised IAM Credentials through Managed Policies 14 min read Related Products Cortex Cortex Cloud Idira Unit 42 Cloud Security Assessment Unit 42 Incident Response By: Margaret Kelley Published: September 21, 2026 Categories: Cloud Cybersecurity Research Threat Research Tags: AWS AWS CloudTrail Bedrock Cloud compute GitHub JSON Logging Share Executive Summary This article explores how AWS mitigates the security risks associated with publicly exposed Identity and Access Management (IAM) access keys through its AWSCompromisedKeyQuarantine managed policy. We discuss the evolution of the different versions of this AWS managed policy. We also show how the managed policy AWSCompromisedKeyQuarantine evolved over time to protect organizations by relating it directly to new cloud attacks against AWS environments. Additionally, this article provides background to the partner integration between GitHub's secret scanning program and AWS. Our research details how the managed policy automatically gets attached with a step-by-step timeline of a real-world exposure test. Finally, the article highlights practical monitoring strategies for security teams to detect quarantine events within their own logging environments to ensure rapid incident response. Palo Alto Networks customers are better protected from the threats discussed above through the following products and services: Cortex Cloud Idira Privilege Access Management (PAM) Unit 42 Cloud Security Assessment is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics IAM , Exposed Credentials , Identity AWSCompromisedKeyQuarantine Background When organizations face attacks against their AWS environments, misuse of AWS IAM user access keys continue to account for a large majority of initial attack vectors . These long-term access keys pose security risks to organizations if the permissions associated with the IAM users do not follow the principle of least privilege . Access keys and their associated secrets become exposed in many different ways, commonly through publication in public code repositories or exposure in environment variable files . If AWS receives notifications about access keys and secrets exposed in public GitHub repositories or through other notices, it promptly secures those credentials and notifies the owners. AWS secures the exposed credentials using automated processes, which allows it to quickly support victim organizations and limit their exposure. This automated process has been around for many years and was documented by cloud security researcher Pawel Rzepa in the AWS Access Keys Leak in GitHub Repository and the Some Improvements in Amazon Reaction posts. Before delving into the importance of the AWSCompromisedKeyQuarantine managed policy and its purpose, we will first discuss how managed policies work within AWS environments. The AWS IAM service offers various features for configuring identities within an AWS account. In particular, AWS provides a policy feature that aggregates permissions into an object for attachment to a principal. Policies encompass a wide range of types, but this article focuses on identity-based policies . Identity-based policies specifically attach to an identity, while other policy types attach to resources or define permission limitations, such as a permission boundary . These policies consist of managed (AWS-managed and customer-managed) and inline policies. Managed policies include three sub-types: AWS managed AWS managed for job functions Customer managed Figure 1 shows the breakdown of these policies. Figure 1. Breakdown of IAM features in relation to main IAM service. AWS-managed policies exist to assist
```

#### Corroborating sources (2)

- **Unit 42** (threat_research_primary)
  - Title: From Exposure to Lockdown: How AWS Neutralizes Compromised IAM Credentials through Managed Policies
  - Published: 2026-09-21T10:00:13+00:00
  - Link: https://unit42.paloaltonetworks.com/detecting-exposed-aws-iam-credentials/
  - Summary: We explore how AWS neutralizes exposed IAM credentials using managed policies, detailing GitHub secret scanning and CloudTrail monitoring strategies. The post From Exposure to Lockdown: How AWS Neutralizes Compromised IAM Credentials through Managed Policies appeared first on Unit 42 .
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Supporting ASD’s multi-factor authentication campaign: Why MFA matters more than ever
  - Published: 2026-09-23T14:45:44+00:00
  - Link: https://aws.amazon.com/blogs/security/supporting-asds-multi-factor-authentication-campaign-why-mfa-matters-more-than-ever/
  - Summary: The Australian Signals Directorate (ASD) has this month issued a clear call to action through its Multi-factor authentication: Switch it on campaign, urging businesses, organisations, and individuals to enable multi-factor authentication (MFA) across their online accounts. At AWS, we strongly support this message. As threat actors continue to target credentials through phishing, credential stuffing, and […]

### Cluster df25ab925d — score 17

- Title: InfraTrust report warns network management systems under attack
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-23T14:35:26+00:00
- Link: https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ransomware_extortion
- affected_industries: critical_infrastructure
- affected_products: Cisco
- cve_ids: CVE-2026-20079, CVE-2026-20316, CVE-2026-76460
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage, active_exploitation
- affected_industries: critical_infrastructure
- affected_products: Cisco
- cve_ids: CVE-2026-20079, CVE-2026-20316, CVE-2026-76460
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Attackers are increasingly targeting the management systems used to control enterprise infrastructure, with several critical vulnerabilities actively exploited before or shortly after vendors disclosed them. [...]
```

#### Full body

```
InfraTrust report warns network management systems under attack By Lawrence Abrams September 23, 2026 10:35 AM 0 Attackers are increasingly targeting the management systems used to control enterprise infrastructure, with several critical vulnerabilities actively exploited before or shortly after vendors disclosed them. This was reported in the September edition of Eclypsium's InfraTrust Pulse , a monthly report tracking security advisories affecting network devices, servers, firmware, chips, and other infrastructure. Between August 25 and September 17, InfraTrust tracked 158 new security advisories across 17 vendors, covering 1,699 vulnerabilities. Of those advisories, 42 were rated critical, eight had a maximum CVSS score of 10.0, and 71 could be exploited remotely without authentication. Five of the published advisories included vulnerabilities that ultimately made it on to CISA's Known Exploited Vulnerabilities (KEV) catalog. However, InfraTrust says one of the more significant trends this month is where many of the most dangerous vulnerabilities are appearing. Attackers are increasingly compromising the management systems used to configure and control network devices, giving hackers full control over compromised devices. "This is the second consecutive month the highest-value exploited flaws in infrastructure were in administrative software, so treat these platforms as high-value targets and patch, monitor, and harden them accordingly," reads the report. Infrastructure management systems targeted One of the most serious vulnerabilities highlighted in the report is CVE-2026-20079, a maximum-severity Cisco Secure Firewall Management Center (FMC) authentication bypass. The flaw allows an unauthenticated attacker to send crafted HTTP requests to the FMC web interface and execute scripts and commands as root on vulnerable devices. Cisco confirmed on September 9 that the vulnerability was being actively exploited, updating its advisory to say its Product Security Incident Response Team became aware of the attacks in August. CISA added the flaw to its Known Exploited Vulnerabilities (KEV) catalog the same day. However, BleepingComputer previously reported on July 29 that Cisco had already updated the CVE-2026-20079 advisory with hot fixes and indicators of compromise that were also associated with attacks exploiting another FMC vulnerability, CVE-2026-20316. At the time, Cisco said it was not aware of malicious exploitation of CVE-2026-20079, despite publishing the same `/var/tmp/license.tmp` indicator for both vulnerabilities. The two FMC flaws were later confirmed to have been chained together in attacks. Cisco Talos has linked the activity to three threat clusters tracked as UAT-12197, UAT-11823, and UAT-11988, which include state-sponsored actors and ransomware gangs. The attackers were observed using built-in FMC tools for reconnaissance, deploying tunneling utilities, harvesting credentials from compromised systems, and in some cases, ultimately deploying Qilin ransomware encryptors. Sophos Counter Threat Unit also analyzed a Linux implant named "timezone_check" recovered from compromised FMC appliances and identified it as a variant of Cyclops Blink, malware previously associated with the Sandworm threat group. Cisco separately disclosed six additional FMC vulnerabilities on September 16, including flaws affecting the sftunnel connection FMC uses to communicate with managed firewalls. Cisco Identity Services Engine (ISE), another management platform, was also hit with multiple critical vulnerabilities. Cisco disclosed ISE advisories on September 16, including three vulnerabilities with maximum CVSS scores of 10.0. One of them, CVE-2026-76460 , is an authentication bypass in an API that allows an unauthenticated remote attacker to execute commands as root. CISA added the flaw to the KEV catalog on the same day Cisco disclosed it as it was already exploited in attacks . Cisco says there are no workarounds, although restricti
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: InfraTrust report warns network management systems under attack
  - Published: 2026-09-23T14:35:26+00:00
  - Link: https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/
  - Summary: Attackers are increasingly targeting the management systems used to control enterprise infrastructure, with several critical vulnerabilities actively exploited before or shortly after vendors disclosed them. [...]

### Cluster 64d509601f — score 17

- Title: SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-19T09:31:17+00:00
- Link: https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-28326, SolarWinds

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ddos, phishing_social_eng, ransomware_extortion, vulnerability_disclosure, zero_day
- affected_industries: financial_services
- affected_products: Anthropic/Claude, Linux kernel, SolarWinds
- cve_ids: CVE-2026-28299, CVE-2026-28302, CVE-2026-28304, CVE-2026-28323, CVE-2026-28326
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, ddos, apt_espionage, vulnerability_disclosure, active_exploitation
- affected_industries: financial_services
- affected_products: SolarWinds, Anthropic/Claude, Linux kernel
- cve_ids: CVE-2026-28326, CVE-2026-28323, CVE-2026-28299, CVE-2026-28302, CVE-2026-28304
- urgency_signals: actively_exploited, zero_day, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
SolarWinds has released security updates to address a high-severity flaw in Access Rights Manager (ARM) that, if successfully exploited, could lead to an unauthenticated remote code execution vulnerability. The vulnerability, tracked as CVE-2026-28326, is rated 8.8 out of 10.0 on the CVSS scoring system. The issue affects all versions of Access Rights Manager 2026.2 and prior. "SolarWinds
```

#### Full body

```
SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE  Ravie Lakshmanan  Sep 19, 2026 Vulnerability / Identity Security SolarWinds has released security updates to address a high-severity flaw in Access Rights Manager (ARM) that, if successfully exploited, could lead to an unauthenticated remote code execution vulnerability. The vulnerability, tracked as CVE-2026-28326 , is rated 8.8 out of 10.0 on the CVSS scoring system. The issue affects all versions of Access Rights Manager 2026.2 and prior. "SolarWinds Access Rights Manager was reported to be affected by an unauthenticated remote code execution vulnerability," SolarWinds said in an advisory released on September 17, 2026. "The issue stems from a hard-coded static key." The company credited Armadin security researcher Kai Huang with discovering and reporting the flaw, which has been patched in ARM 2026.2.1 . SolarWinds makes no mention of the vulnerability being exploited in the wild. The development comes nearly two months after the company shipped fixes for a critical flaw impacting Web Help Desk (WHD) (CVE-2026-28323, CVSS score: 9.8) that could result in a SAML authentication bypass when the SAML 2.0 authentication method is enabled. Another vulnerability relates to a denial-of-service (DoS) vulnerability (CVE-2026-28299, CVSS score: 8.2) that could cause the Web Help Desk server to crash due to insufficient memory. Both issues have been resolved in WHD 2026.2.1. SolarWinds has also released fixes for 16 flaws impacting Serv-U (CVE-2026-28302, from CVE-2026-28304 through CVE-2026-28317, CVE-2026-28321, CVE-2026-28323) that could lead to privilege escalation, remote code execution, and the creation of administrator accounts. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  enterprise security , Identity Security , SolarWinds , Vulnerability ⚡ Top Stories This Week Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation KREMLIN Banking Malware Hijacks Chrome and Edge to Steal Credentials and Session Tokens LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing ⚡ Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data N0va Phishkit Targets US and EU Businesses: A New Challenge for Identity Security An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It. How to Evaluate a Unified Security Platform Using a One-Incident Test Stop Trying to Control AI Behavior. Control What AI Can Reach ⭐ Featured Resources Validation Summi
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE
  - Published: 2026-09-19T09:31:17+00:00
  - Link: https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html
  - Summary: SolarWinds has released security updates to address a high-severity flaw in Access Rights Manager (ARM) that, if successfully exploited, could lead to an unauthenticated remote code execution vulnerability. The vulnerability, tracked as CVE-2026-28326, is rated 8.8 out of 10.0 on the CVSS scoring system. The issue affects all versions of Access Rights Manager 2026.2 and prior. "SolarWinds

### Cluster 62087c81f0 — score 16

- Title: vCenter pre-auth RCE: CVE-2026-59309/59310
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-22T07:58:09+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wn37be/vcenter_preauth_rce_cve20265930959310/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-59309, CVE-2026-59310, VMware

#### Cluster taxonomy (union across members)
- affected_products: VMware
- cve_ids: CVE-2026-59309, CVE-2026-59310
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- affected_products: VMware
- cve_ids: CVE-2026-59309, CVE-2026-59310
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
CVE-2026-59309 & CVE-2026-59310: patch-diffing VMware vCenter reveals two pre-auth 9.8 bugs - an auth bypass and a syslog path traversal to RCE submitted by /u/MobetaSec [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: vCenter pre-auth RCE: CVE-2026-59309/59310
  - Published: 2026-09-22T07:58:09+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wn37be/vcenter_preauth_rce_cve20265930959310/
  - Summary: CVE-2026-59309 & CVE-2026-59310: patch-diffing VMware vCenter reveals two pre-auth 9.8 bugs - an auth bypass and a syslog path traversal to RCE submitted by /u/MobetaSec [link] [comments]

### Cluster 0188a8d3e5 — score 16

- Title: Transparent Tribe APT Infrastructure Mapping - Part 2
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
- Link: https://www.team-cymru.com/post/transparent-tribe-apt-infrastructure-mapping
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: APT36

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- actor_attribution: APT36
- affected_industries: government
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage
- actor_attribution: APT36
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Transparent Tribe (APT36, Mythic Leopard, ProjectM, Operation C-Major) is the name given to a threat actor group largely targeting Indian entities and assets.
```

#### Full body

```
S2 Research Team 9 min read July 2, 2021 Transparent Tribe APT Infrastructure Mapping - Part 2 Part 2: A Deeper Dive into the Identification of CrimsonRAT Infrastructure October 2020 ‚Äì June 2021 Introduction Transparent Tribe (APT36, Mythic Leopard, ProjectM, Operation C-Major) is the name given to a threat actor group largely targeting Indian entities and assets. Transparent Tribe has also been known to target entities in Afghanistan and social activists in Pakistan, the latter of which points towards the assumed attribution of Pakistani intelligence. This is the second blog of a two-part series on Transparent Tribe‚Äôs CrimsonRAT infrastructure. You may read the first article here: Part 1: A High-Level Study of CrimsonRAT Infrastructure October 2020 ‚Äì March 2021 We have been tracking CrimsonRAT, Transparent Tribe‚Äôs most ubiquitous remote access tool, over several months. This blog will present a deeper dive into the methods we use to identify CrimsonRAT infrastructure and observations on specific artefacts which have allowed us to attribute this infrastructure dating back multiple years. Our intention is to provide supporting context to existing Transparent Tribe reporting and IOCs, to aide in future threat reconnaissance activities against this group. Key Observations CrimsonRAT infrastructure is largely hosted on infrastructure leased by Pi NET LLC, a Vietnamese VPS reseller. An RDP certificate serves as a key indicator for CrimsonRAT and has been observed on 17 C2 servers in total. A methodology for tracing CrimsonRAT C2 servers was devised based on network traffic patterns and the scanning of beacon ports. CrimsonRAT C2 servers provide a standardized response when an initial TCP connection is established. Potential crossover login activity has been observed, linking multiple C2 servers together, as well as providing a link to AhMyth AndroidRAT. Eggs in One Basket (Pi NET LLC) When reviewing CrimsonRAT C2 infrastructure an RDP certificate (with a Common Name value of WIN-P9NRMH5G6M8 ) continued to appear. Our certificate data showed this Common Name appearing across many of the previously identified ‚Äòpreferred‚Äô providers (see Part 1) used by Transparent Tribe. After reviewing rWhois records for IP addresses hosting this certificate it became apparent that many, if not all these hosts, were being subleased to Pi NET LLC . A list of all 17 CrimsonRAT C2 servers hosting the Common Name WIN-P9NRMH5G6M8 certificate is provided at the end of this blog. Expanding this search using Shodan‚Äôs data holdings, we were able to bolster our theory (the association of the certificate with Pi NET LLC ) as only a relatively small number of hosts (240) were identified, the majority of which were either assigned directly to, or subleased to Pi NET LLC . Unfortunately, not all providers document the details of subleasing in Whois records, so we were not able to tie ALL the IP addresses identified to a single entity (Pi NET). Figure 1: Shodan 240 hosts found with Common Name WIN-P9NRMH5G6M8 More recently we have also observed a different certificate in use on Pi NET LLC hosts, with a Common Name of WIN-L6BUPB5SQBC . This certificate is associated with CrimsonRAT C2s 134.119.181.15, 181.215.47.169 and 134.119.181.142 and moving forward could be an alternative indicator of Transparent Tribe activity. Reviewing Whois information for all CrimsonRAT C2 servers we have identified to date, we found that roughly three-quarters (75%) were associated in some way with Pi NET LLC . Therefore, we assess with moderate confidence that Transparent Tribe is hosting a large proportion of (known) CrimsonRAT infrastructure through this single VPS provider, i.e., whilst CrimsonRAT servers are overtly hosted with several different providers, it is likely that this infrastructure is managed and sold by the small reseller Pi NET LLC. Pi NET LLC (pivps[.]com) is a VPS reseller based out of northern Vietnam, which provides very affordable Windows and Linux h
```

#### Corroborating sources (2)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Transparent Tribe APT Infrastructure Mapping - Part 2
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/transparent-tribe-apt-infrastructure-mapping
  - Summary: Transparent Tribe (APT36, Mythic Leopard, ProjectM, Operation C-Major) is the name given to a threat actor group largely targeting Indian entities and assets.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Transparent Tribe Deploys New Rust Backdoor Using Private GitHub Repositories for C2
  - Published: 2026-09-18T15:24:16+00:00
  - Link: https://thehackernews.com/2026/09/transparent-tribe-deploys-new-rust.html
  - Summary: The Pakistan-aligned threat group tracked as Transparent Tribe (aka APT36 and Earth Karkaddan) has been attributed to a fresh set of cyber attacks targeting government and defense entities in India and Afghanistan. The attacks, per Zscaler ThreatLabz, involve the use of previously undocumented tools called RUSTYSHADE, RUSTYMOVE, PSNATCH, and BASHNATCH. The activity has been codenamed Operation

### Cluster 5f3dd92061 — score 16

- Title: The Closed Quorum: Inside the first reported autonomous AI C2 implant
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-22T10:00:58+00:00
- Link: https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng
- affected_industries: financial_services
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, active_exploitation
- affected_industries: financial_services
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
CLOSEDQUORUM, a malware binary discovered through Cisco Talos’ CAIRN project, exhibits fully autonomous command and control (C2). It represents a shift in effort displacement for attackers, in which expanding portions of the attack chain can be executed without operator involvement.
```

#### Full body

```
The Closed Quorum: Inside the first reported autonomous AI C2 implant By Ryan Fetterman Tuesday, September 22, 2026 06:00 AI Threat Spotlight CLOSEDQUORUM, a malware binary discovered through Cisco Talos’ CAIRN project , exhibits fully autonomous command and control (C2). While we do not have confirmation of in-the-wild deployment, artifacts from the binary were used to connect the developer to postings on criminal forums related to carding, dating back to 2025. This malware is a useful reference example of how attackers can collapse the decision space of a particular attack phase into a constrained set of choices, allowing AI models to provide reasoning and act independently. CLOSEDQUORUM represents a shift in effort displacement for attackers, in which expanding portions of the attack chain can be executed without operator involvement. AI’s impact on offensive cyber operations has thus far mainly focused on two dimensions: speed and scale . Attackers can generate phishing lures faster and produce more malicious code variants with less effort. These are real effects, visible in the proliferation of AI-generated coding samples and agent-assisted intrusions that have become common in the past few years. But in each case, the human operator remains present: directing the tooling, selecting targets, and guiding the execution. AI makes the operator faster and more productive but does not remove them from the operation. A third dimension has received less attention in the malware space: effort displacement. This is not merely augmenting what an operator can accomplish in a session but transferring an entire phase of the attack from the operator to the system. Effort displacement compounds the effects of speed and scale because the human-in-the-loop is no longer the bottleneck. Human operators are bound by attention, working hours, and cognitive load. An AI system capable of executing a phase of the attack chain can continue when the operator is no longer watching. It does not go offline when the attacker sleeps. Today Cisco Talos released CAIRN , our open-source research toolkit for tracking AI-integrated malware. This is the first in a series of posts sharing what we've found. While the threat class of CAIRN findings may span from experimental proof-of-concept to sophisticated active campaigns, the nature of the threat is aside from the focus: actively studying this frontier provides actionable insights to offset how threat actors are operationalizing AI. Introducing CLOSEDQUORUM CLOSEDQUORUM is, to our knowledge, the first publicly documented Windows implant to apply this model to tactical command and control (C2). After deployment, it delegates the selection of its next action to a panel of commercial large language models (LLMs) and executes the resulting decision, with the intent of harvesting user credentials and crypto wallets. It does not require continued commands from a human operator or tasking from a dedicated, attacker-operated C2 server; the complete dynamic operation is delegated to the AI. The name reflects the architecture. A quorum is a decision-making body that requires some minimum of participants to act. CLOSEDQUORUM's quorum is up to four LLM providers: DeepSeek, Qwen, Mistral, and Google Gemini. The session is closed; no humans are admitted. Four models are queried in sequence, their independent verdicts tallied, and the binary acts, based on their judgment. Figure 1. CLOSEDQUORUM architecture. The CLOSEDQUORUM C2 architecture supports up to four LLM provider integrations. Each active model votes on the next action, and the action receiving the most votes is selected. Our static analysis confirms the full details of the autonomous decision loop, and development builds demonstrate build-time injection of provider credentials. The public distribution build, however, contains placeholder API keys and a dummy webhook, so we did not observe a complete end-to-end execution of the architecture. Further details of th
```

#### Corroborating sources (2)

- **Cisco Talos** (threat_research_primary)
  - Title: The Closed Quorum: Inside the first reported autonomous AI C2 implant
  - Published: 2026-09-22T10:00:58+00:00
  - Link: https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
  - Summary: CLOSEDQUORUM, a malware binary discovered through Cisco Talos’ CAIRN project, exhibits fully autonomous command and control (C2). It represents a shift in effort displacement for attackers, in which expanding portions of the attack chain can be executed without operator involvement.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: This Windows Malware is Built to Let Up to Four AI Models Vote on Its Next Move
  - Published: 2026-09-23T14:17:58+00:00
  - Link: https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html
  - Summary: A Windows malware called CLOSEDQUORUM is built to take orders from a vote of up to four AI models instead of an attacker's server, Cisco Talos said on September 22. The models can choose to steal Windows credentials, saved browser passwords, and crypto wallet data. Talos has not seen this setup work from start to finish, and the public version of the malware does not work as it is.

### Cluster 642074e2ab — score 15

- Title: DarkMe RAT: A VB6 APT Trojan Turned Conventional Infostealer
- Source: Huntress (detection_response_operations)
- Published: 2026-09-22T21:00:00+00:00
- Link: https://www.huntress.com/blog/darkme-rat-abandons-exploits
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, credential_theft, phishing_social_eng, zero_day
- affected_industries: financial_services
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2023-38831, CVE-2024-21412
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, zero_day, apt_espionage
- affected_industries: financial_services
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2023-38831, CVE-2024-21412
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
DarkMe, an APT-linked VB6 RAT known for using zero day exploits, turned up in two Huntress incidents stripped down to a plain .pif infostealer malware.
```

#### Full body

```
Home Blog DarkMe Email Campaign Broadens Targeting For APT RAT Published: September 22, 2026 DarkMe Email Campaign Broadens Targeting For APT RAT By: James Northey Andrew Brandt Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways Huntress spotted the DarkMe malware in two separate incidents affecting different organizations on August 31, 2026. DarkMe is a Visual Basic 6 (VB6) spy-RAT previously attributed to the financially-motivated APT tracked as Water Hydra and the EvilNum-led Operation DarkCasino. We identified the two samples of DarkMe based on the command set, the VB6 loader chain, and a mangled RC4 routine which turns into a single-byte-XOR payload. Two years ago, DarkMe developed a reputation by leveraging two separate zero days to deliver its malware: WinRAR ( CVE-2023-38831 ) and Windows Defender SmartScreen ( CVE-2024-21412 ). But in these new incidents, the malware didn't leverage exploits, relying on social engineering to convince users to run a .pif file linked from an email. Novel tradecraft in this campaign includes the use of a .pif as the initial payload, and the creation of a nonstandard protocol handler to conceal its persistence mechanism. The absence of exploits made the attack chain cheaper and more indiscriminate, reflecting a broader industry trend of adversaries abandoning complex technical exploits for high-volume, low-skill attacks that rely on user error. What follows is the full attack chain, the moment a "standard infostealer" turned into a named threat actor group's remote access trojan (RAT), the C2 we pulled back out of the DLL-loaded RAT, and the detection lessons, including why abandoning the zero days should worry defenders more, not less. Background DarkMe, a Visual Basic 6 (VB6) spy trojan and remote access tool became well known in February 2024 for its use of zero days to deliver malware . But this malware family was first observed in September 2021 and publicly documented a year later by NSFOCUS under "Operation DarkCasino" attributed to a group called EvilNum. Researchers at Trend Micro and SonicWall have also tied this malware, with the usual attribution caveats, to Water Hydra, an APT group with the unusual profile of chasing money rather than espionage. Its campaigns are typically financially motivated, targeting forex traders, stock-trading forums, online gambling platforms, and cryptocurrency users. What made the DarkMe malware notable was the delivery. In 2023, Water Hydra weaponised the WinRAR extension-spoofing flaw CVE-2023-38831 as a zero day, dropping malicious archives on trading forums. In late 2023 and early 2024, Water Hydra pivoted to CVE-2024-21412, a Defender SmartScreen bypass built on a shortcut-that-points-to-another-shortcut (yes, this was a thing), staged over a WebDAV share behind a crafted Explorer view. But our story picks up from the Huntress threat hunting team's POV, and this tradecraft is nearly unrecognisable. There is no exploit here at all. A hunting rule picked up some odd activity around a program information file (PIF) launching Windows Installer. Everything downstream of that PIF is textbook DarkMe, but everything before is frankly, boring. We thought this was an interesting story to tell, nevertheless, as it illustrates a larger trend of advanced threat actors opting for less sophisticated initial access methods to broaden their targeting. Figure 1: An overview of the attack chain employed by this new DarkMe campaign Technical breakdown Initial access: a photo that wasn't The delivery came through a link in a plain old social engineering malspam email: Figure 2: Phishing email delivering PIF disguised as an image Although the link in the email pointed to https://readonline365[.]com/view/image.png , a URL for a graphics file, the webserver delivered image.pif , a Windows executable. Figure 3: The Properties sheet describes the file as a "Shortcut to MS-DOS program" but the file is, itself, an executable. The .pif extension
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: DarkMe RAT: A VB6 APT Trojan Turned Conventional Infostealer
  - Published: 2026-09-22T21:00:00+00:00
  - Link: https://www.huntress.com/blog/darkme-rat-abandons-exploits
  - Summary: DarkMe, an APT-linked VB6 RAT known for using zero day exploits, turned up in two Huntress incidents stripped down to a plain .pif infostealer malware.

### Cluster b14e569a31 — score 15

- Title: Record breaking DDoS Potential Discovered: CVE-2022-26143
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
- Link: https://www.team-cymru.com/post/record-breaking-ddos-potential-discovered-cve-2022-26143
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2022-26143

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos
- affected_industries: financial_services, telecommunications
- cve_ids: CVE-2022-26143
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ddos, active_exploitation
- affected_industries: financial_services, telecommunications
- cve_ids: CVE-2022-26143
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Discover how the CVE-2022-26143 vulnerability could lead to record-breaking DDoS attacks, and what it means for the cybersecurity landscape.
```

#### Full body

```
10 min read March 8, 2022 Record breaking DDoS Potential Discovered: CVE-2022-26143 How cross-industry collaboration discovered a devastating DDoS method CVE-2022-26143: TP240PhoneHome Reflection/Amplification DDoS Attack Vector Executive summary A new reflection/amplification distributed denial-of-service (DDoS) vector with a record-breaking potential amplification ratio of 4,294,967,296:1 has been abused by attackers in the wild to launch multiple high-impact DDoS attacks. Security researchers, network operators, and security vendors observed these attacks and formed a task force to investigate the new DDoS vector and provide mitigation guidance. Approximately 2,600 Mitel MiCollab and MiVoice Business Express collaboration systems acting as PBX-to-internet gateways were incorrectly deployed with an abusable system test facility exposed to the public internet. Attackers were actively leveraging these systems to launch reflection/amplification DDoS attacks of more than 53 million packets per second (Mpps). With optimal attack tuning, the potential traffic yield for this DDoS vector is significantly higher. Attacks have been observed on broadband access ISPs, financial institutions, logistics companies, gaming companies, and organizations in other vertical markets. The attacks can be mitigated using standard DDoS-defense techniques. Mitel has released patched software that disables the abusable test facility, and is actively engaged in remediation efforts with their customers. Research and mitigation task force contributors include Akamai SIRT, Cloudflare, Lumen Black Lotus Labs, Mitel, NETSCOUT Arbor ASERT, TELUS, Team Cymru, and The Shadowserver Foundation. Introduction Beginning in mid-February 2022, security researchers, network operators, and security vendors observed a spike in DDoS attacks sourced from UDP port 10074 targeting broadband access ISPs, financial institutions, logistics companies, and organizations in other vertical markets. Upon further investigation, it was determined that the devices abused to launch these attacks are MiCollab and MiVoice Business Express collaboration systems produced by which incorporate TP-240 VoIP-processing interface cards and supporting software; their primary function is to provide internet-based site-to-site voice connectivity for PBX systems. Approximately 2600 of these systems have been incorrectly provisioned so that an unauthenticated system test facility has been inadvertently exposed to the public internet, allowing attackers to leverage these PBX VoIP gateways as DDoS reflectors/amplifiers. Mitel is aware that these systems are being abused to facilitate high-pps DDoS attacks, and have been actively working with customers to remediate abusable devices with patched software that disables public access to the system test facility. In this blog, we will further explore the observed activity, explain how the driver has been abused, and share recommended mitigation steps. This research was created cooperatively among a team of researchers from Akamai SIRT, Cloudflare, Lumen Black Lotus Labs, NETSCOUT Arbor ASERT , TELUS, Team Cymru, and The Shadowserver Foundation. DDoS attacks in the wild While spikes of network traffic associated with the vulnerable service were observed on January 8 and February 7, 2022, we believe the first actual attacks leveraging the exploit began on February 18. Observed attacks were primarily predicated on pps, or throughput, and appeared to be UDP reflection/amplification attacks sourced from UDP/10074 that were mainly directed toward destination ports UDP/80 and UDP/443. The single largest observed attack of this type preceding this one was approximately 53 Mpps and 23 Gbps. The average packet size for that attack was approximately 60 bytes, with an attack duration of approximately 5 minutes. The amplified attack packets are not fragmented. This particular attack vector differs from most UDP reflection/amplification attack methodologies in that the ex
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Record breaking DDoS Potential Discovered: CVE-2022-26143
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/record-breaking-ddos-potential-discovered-cve-2022-26143
  - Summary: Discover how the CVE-2022-26143 vulnerability could lead to record-breaking DDoS attacks, and what it means for the cybersecurity landscape.

### Cluster 283562f1a6 — score 15

- Title: Exploit Released for Unpatched Ubuntu Linux Flaw Enabling Host-Root Container Escape
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-23T11:12:18+00:00
- Link: https://thehackernews.com/2026/09/exploit-released-for-unpatched-ubuntu.html
- Fetch status: ok
- Member count: 3
- Corroborating source count: 1
- Strong signals: CVE-2026-80521, Linux kernel

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- affected_products: Azure, Google Cloud, Linux kernel
- cve_ids: CVE-2025-39682, CVE-2026-80521
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- affected_products: Linux kernel, Google Cloud, Azure
- cve_ids: CVE-2026-80521
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A use-after-free in the Linux kernel's AF_UNIX socket subsystem can be used to escape a container and gain root on the host, security firm DepthFirst said in research published September 22. The flaw, tracked as CVE-2026-80521 (CVSS score: 7.8), was fixed upstream on August 6, but Ubuntu has not shipped the patch for its 26.04, 24.04, or 22.04 LTS releases. DepthFirst
```

#### Full body

```
Exploit Released for Unpatched Ubuntu Linux Flaw Enabling Host-Root Container Escape  Swati Khandelwal  Sep 23, 2026 Vulnerability / Linux A use-after-free in the Linux kernel's AF_UNIX socket subsystem can be used to escape a container and gain root on the host, security firm DepthFirst said in research published September 22. The flaw, tracked as CVE-2026-80521 (CVSS score: 7.8), was fixed upstream on August 6, but Ubuntu has not shipped the patch for its 26.04, 24.04, or 22.04 LTS releases. DepthFirst released exploit code targeting Ubuntu 26.04. Ubuntu's security tracker lists the Linux package on 26.04 as "vulnerable, work in progress." The 24.04 and 22.04 releases are also affected through newer kernel packages, including those for AWS, Azure, and GCP workloads. No fix has shipped on any affected release. The flaw is not in CISA's Known Exploited Vulnerabilities catalog, and there are no confirmed reports of attacks using it. The vulnerability sits in the kernel's garbage collector for AF_UNIX sockets. That collector cleans up file descriptors passed between processes through SCM_RIGHTS messages. AF_UNIX sockets handle local communication between processes and are allowed by default in Docker and Kubernetes seccomp profiles, which is why the flaw can be reached from inside a container. A race condition in the garbage collector lets it see new references before the data carrying them has been queued. If the collector runs during that window, it can free part of a group of linked sockets without removing a pointer from a persistent internal list. The next collection pass follows that pointer into freed memory. Because the exploit reaches the kernel through ordinary system calls that containers are allowed to make, it bypasses namespace isolation, cgroup limits, and seccomp filtering. The upstream fix landed on August 6 in mainline kernel 7.2 and stable branch 7.1.10. The vulnerable code was introduced in kernel 6.10 and also backported to stable branches 6.1 and 6.6. Organizations running an affected kernel can apply the upstream patch directly. Ubuntu's tracker shows "work in progress" with no published date for the distribution update. Neither DepthFirst nor Ubuntu has published a temporary workaround. DepthFirst recommends moving untrusted workloads to microVM isolation, such as Firecracker or Kata Containers, which give each workload its own kernel rather than sharing the host's. How the Flaw Was Found DepthFirst said its AI model, dfs-large1, trained for vulnerability detection, found the flaw alongside a human-operated testing harness. The company won a Google kernelCTF slot with the exploit on July 24 and reported the bug to the kernel security team on August 5. The kernel maintainers replied that a researcher at OpenAI had independently reported the same bug, according to DepthFirst's timeline. The CVE commit credits kernel-exploitation researcher Kyle Zeng as the reporter. The disclosure is the latest in a series of 2026 kernel flaws that allow attackers to escape containers. A futex vulnerability disclosed in July and a flaw in the kernel's cryptographic subsystem in April also allowed an unprivileged user to escalate to root on the host. Both discoveries involved AI-assisted research . DepthFirst argues that AI-accelerated vulnerability discovery has lowered the barrier to container escapes to the point that organizations should not treat containers as a security boundary. "The barrier to escaping containers by attacking the kernel has fallen so significantly that we must assume attackers can do so at will," the company said. Nearly 5,700 Linux kernel CVEs have been published in 2026, the highest annual total on record, according to LinuxCVETracker. The demonstrated exploit and the rising volume are the basis for the company's assessment. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE 
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Exploit Released for Unpatched Ubuntu Linux Flaw Enabling Host-Root Container Escape
  - Published: 2026-09-23T11:12:18+00:00
  - Link: https://thehackernews.com/2026/09/exploit-released-for-unpatched-ubuntu.html
  - Summary: A use-after-free in the Linux kernel's AF_UNIX socket subsystem can be used to escape a container and gain root on the host, security firm DepthFirst said in research published September 22. The flaw, tracked as CVE-2026-80521 (CVSS score: 7.8), was fixed upstream on August 6, but Ubuntu has not shipped the patch for its 26.04, 24.04, or 22.04 LTS releases. DepthFirst

### Cluster 32b7ae98f7 — score 15

- Title: Windows Exploitation Techniques: Dangling COM Object Registrations
- Source: Google Project Zero (offensive_vulnerability_research)
- Published: 2026-09-21T07:00:00+00:00
- Link: https://projectzero.google/2026/09/windows-dangling-com.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-50343, CVE-2026-66804

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-50343, CVE-2026-66804
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-66804, CVE-2026-50343
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
This short blog post is about abusing a privilege escalation bug that Microsoft recently fixed in Windows, CVE-2026-66804, that I and 14 others reported. This issue is an incomplete fix for CVE-2026-50343, a bug dubbed “Dark Elevator” by Calif. The root cause of the bug was a dangling COM object registration for the CrossDevice COM object with the CLSID {E9F83CF2-E0C0-4CA7-AF01-E90C70BEF496}. A COM registration typically needs two parts: a server executable, which for in-process components is a DLL and a CLSID entry under the HKEY_CLASSES_ROOT registry key which points to that DLL.
```

#### Full body

```
This short blog post is about abusing a privilege escalation bug that Microsoft recently fixed in Windows, CVE-2026-66804 , that I and 14 others reported. This issue is an incomplete fix for CVE-2026-50343, a bug dubbed âDark Elevatorâ by Calif . The root cause of the bug was a dangling COM object registration for the CrossDevice COM object with the CLSID {E9F83CF2-E0C0-4CA7-AF01-E90C70BEF496} . A COM registration typically needs two parts: a server executable, which for in-process components is a DLL and a CLSID entry under the HKEY_CLASSES_ROOT registry key which points to that DLL. This object was registered in the system wide classes key, meaning it was accessible to all users on the system, including system services. However the server executable was missing. Specifically it was registered to use the DLL %PROGRAMDATA%\CrossDevice\CrossDevice.Streaming.Source.dll . Not only does this path not exist, itâs also within the C:\ProgramData directory. This is a common location for all users on the system and therefore permits anyone to create directories. Therefore you can create an arbitrary DLL file at that location and the COM object can be instantiated potentially leading to privilege escalation. But how to get the COM object, and thus the DLL, loaded into a privileged process? The fixed bug Calif blogged about, CVE-2026-50343, abused a weak registry key permissions to add the class as a installer plugin and then get the InstallService to load it into memory. The issue with the InstallService was fixed, so we need an alternative way to abuse the unfixed dangling COM reference. Abuse Custom COM Marshaling, Again A technique Iâve used multiple times in the past to load an arbitrary DLL into a privileged process is to abuse custom COM marshaling. When you call an interface method which is implemented out-of-process, the COM runtime will marshal the parameters into an RPC call to send to the server. If a parameter is a COM object then the runtime marshals that object into an OBJREF structure that allows the object to be used in the server. The two main types of OBJREFs are shown in the diagram below, or you can read about them in the official DCOM documentation here : The default COM marshaling strategy is by reference which produces a Standard OBJREF containing all the information needed to connect to the original object. The object might even be on a completely different computer. When the object is unmarshaled this information is used to create an RPC channel back to the caller so that the server can call methods on the object. The runtime also supports an opt-in marshal by value mechanism if the object implements the IMarshal interface. This allows the object to specify an arbitrary CLSID to use as the unmarshaling object, which doesnât have to be the same as the object being passed in. When the object is unmarshaled in the server the CLSID is used to lookup an in-process server DLL to load.Â Therefore an obvious technique to exploit the dangling COM object registration is to send a Custom OBJREF to a privileged COM service specifying the CLSID of the dangling object. When unmarshaled, which happens automatically in the runtime before the target method is called, the malicious DLL will be loaded and weâd get privilege escalation. The following code shows how trivial it is to specify the dangling COM class in an IMarshal implementation: class FakeMarshal : public IMarshal { // Inherited via IMarshal HRESULT GetUnmarshalClass ( REFIID riid , void * pv , DWORD dwDestContext , void * pvDestContext , DWORD mshlflags , CLSID * pCid ) override { return CLSIDFromString ( L"{E9F83CF2-E0C0-4CA7-AF01-E90C70BEF496}" , pCid ); } // ... }; We need to find a privileged service to send the marshaled COM object to become an administrator. Unfortunately, finding such a service isnât so simple. The fact that a custom marshaling object will cause an arbitrary DLL to be loaded into the process and code executed is a risky operation
```

#### Corroborating sources (1)

- **Google Project Zero** (offensive_vulnerability_research)
  - Title: Windows Exploitation Techniques: Dangling COM Object Registrations
  - Published: 2026-09-21T07:00:00+00:00
  - Link: https://projectzero.google/2026/09/windows-dangling-com.html
  - Summary: This short blog post is about abusing a privilege escalation bug that Microsoft recently fixed in Windows, CVE-2026-66804, that I and 14 others reported. This issue is an incomplete fix for CVE-2026-50343, a bug dubbed “Dark Elevator” by Calif. The root cause of the bug was a dangling COM object registration for the CrossDevice COM object with the CLSID {E9F83CF2-E0C0-4CA7-AF01-E90C70BEF496}. A COM registration typically needs two parts: a server executable, which for in-process components is a DLL and a CLSID entry under the HKEY_CLASSES_ROOT registry key which points to that DLL.

### Cluster 7c42269e48 — score 15

- Title: ToolShell, SharePoint, and the Death of the Patch Window
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
- Link: https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, zero_day
- actor_attribution: APT27, APT31
- affected_products: GitHub, Microsoft SharePoint
- cve_ids: CVE-2025-53770, CVE-2026-65660
- urgency_signals: no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage
- actor_attribution: APT27, APT31
- affected_products: Microsoft SharePoint, GitHub
- cve_ids: CVE-2025-53770
- urgency_signals: zero_day, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
This blog explores this week's zero-day exploit targeting Microsoft SharePoint, now referred to as ToolShell, caught organizations off guard.
```

#### Full body

```
Eli Woodward 3 min read July 8, 2025 ToolShell, SharePoint, and the Death of the Patch Window Introduction This week‚Äôs zero-day exploit targeting Microsoft SharePoint, now referred to as ToolShell, caught organizations off guard. The exploit allowed unauthenticated remote code execution and quickly spread across unpatched SharePoint servers. Moreover, this incorporated a variant of previous vulnerabilities and resulted in the exploitation of an unpatched vulnerability. While this scenario is a security team‚Äôs nightmare (the mass exploitation of a zero-day), it does highlight a trend we‚Äôve been monitoring for several years - evidence of exploitation within Team Cymru‚Äôs data holdings prior to the availability of public exploit code. This type of insight is critical for defenders to be highly tuned into, because it demonstrates how fast and agile attackers have become and why they need to evolve their exposure discovery and related workflows to avert disaster. Old and busted: "Patch Within SLA." New paradigm: ‚ÄúPatch Now.‚Äù Our team has been studying how long it takes for exploit code to go from public release to real-world use. We track new PoC (proof-of-concept) exploit posts, then watch for signs of related activity in our data holdings. Our analysis found that, on average, exploitation tends to begin within three hours of public release. In some cases, we saw attacks begin before the PoC exploit code was even posted publicly. ToolShell was one of those cases. Source: https://github.com/soltanali0/CVE-2025-53770-Exploit/ ‚Äç Source: Pure Signal: Team Cymru Data We observed live exploitation on July 18th, 2025. The first case of PoC exploit code was not made public on GitHub until 21 July 2025. While this was a less common case of mass zero-day exploitation occurring, our data and tracking has shown organizations have mere hours in most cases to patch after exploit code becomes public. The Chinese Connection On 22 July 2025, the Microsoft Threat Intelligence team disclosed more details following their ongoing investigation into the ToolShell exploit campaign targeting on-premises SharePoint servers. Microsoft assesses that three China-nexus advanced persistent threat (APT) groups have been observed exploiting these vulnerabilities. This includes Linen Typhoon (also known as APT27 or Emissary Panda), Violet Typhoon (also known as APT31 or Judgement Panda), and a third group tracked as Storm-2603, which Microsoft also assesses to be a China-based adversary with medium confidence. The key takeaway from this pattern is that exploitation is now a collaborative and opportunistic process, not a linear one. Attackers don‚Äôt just wait for their zero-day to be discovered or for public proof-of-concept code to emerge‚Äîthey maximize the window of opportunity by sharing access and techniques within their circles as soon as they suspect the exploit will be exposed. We saw the same dynamic play out during the Hafnium Microsoft Exchange incident in 2021: once defenders started closing in, new intrusion sets appeared in our telemetry, evidence that the exploit was circulating between groups who wanted to extract every last bit of value before defenders could respond. ‚ÄúOur team sees this sequence repeat with almost every high-impact vulnerability‚Äîfirst a stealthy, targeted phase, then rapid escalation and mass exploitation as news breaks or defenders begin to mobilize.‚Äù ‚Äç Josh Hopkins, Team Cymru Threat Research team For defenders, this reality makes the old patching paradigm obsolete. If you‚Äôre waiting for public disclosure, scheduled patch windows, or even internal validation before acting, you are already behind the curve. The evidence shows that by the time an exploit is publicly known, your attack surface has likely already been tested‚Äîpossibly by multiple threat actors. Patching is not a box to tick off by next Friday. It‚Äôs a race against adversaries who move fast, share what works, and rarely give warning. The on
```

#### Corroborating sources (2)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: ToolShell, SharePoint, and the Death of the Patch Window
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
  - Summary: This blog explores this week's zero-day exploit targeting Microsoft SharePoint, now referred to as ToolShell, caught organizations off guard.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE
  - Published: 2026-09-22T11:17:41+00:00
  - Link: https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html
  - Summary: A SharePoint Server vulnerability that Microsoft initially classified as a spoofing flaw with a CVSS score of 6.5 actually enables authenticated remote code execution, according to full technical details published today by Viettel Cyber Security researcher Dinh Ho Anh Khoa. The flaw, CVE-2026-65660, affects SharePoint Server 2016, 2019, and Subscription Edition. Patches have been

### Cluster 47fb0e3da4 — score 14

- Title: The Odyssey and Trojans again: MovieReaper attacks users in multiple countries through compromised torrents
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
Kaspersky experts have discovered a new MovieReaper campaign. The multi-stage Trojan spreads through movie torrents, such as The Odyssey, and uses the Solana blockchain to hide its C2 infrastructure.
```

#### Full body

```
Table of Contents Introduction Technical details Background Initial infection and spread Malware implants Step 1: Loader Step 2: Shellcode Step 3: UAC Bypass and persistence Step 4: The final implant Infrastructure Victims Conclusions Indicators of compromise File hashes File paths Mutexes Domains and IPs Authors Konstantin Isakov Pavel Cheremushkin Introduction Torrent trackers have long been abused for distributing malicious software, disguised as popular films, games, and other content. Our previous research has shown that cybercriminals repeatedly turn to torrents as an initial infection vector, using trojanized cracks and installers to reach a large number of users. Installation guides for pirated software routinely instruct users to disable their antivirus, conditioning them to ignore the potential threats they are inviting onto their computers. During our analysis of malware that leverages blockchain networks for its C2 infrastructure, we discovered a previously unknown modular, multi-stage framework that we dubbed MovieReaper. This report details the new crimeware campaign that began with the mass infection of users via compromised torrent tracker file storage. We have identified several hundred victims, including both individual users and organizations in multiple countries, such as Russia, Türkiye, Japan, Kenya, Uganda, and Colombia, as well as in several European countries like Spain, the Netherlands, Belgium, and Germany. We analyze the techniques for evading detection by security and sandbox solutions, and examine the capabilities of the modular framework. Kaspersky products detect this threat as HEUR:Trojan.Win64.Agent.gen. Technical details Background In mid‑August 2026, during our threat‑hunting efforts, we identified a large‑scale infection campaign involving previously unknown malware disguised as popular movies. The campaign affected both individuals and organizations across multiple countries. Our initial analysis revealed a common denominator: all of the victims had used torrent trackers. This finding prompted us to investigate the campaign further and analyze its distribution mechanism, overall scope, and unknown malware implants. Initial infection and spread Compromised torrent trackers are the primary vector used to distribute malware. During our investigation, we identified multiple user reports describing suspicious files being downloaded instead of the intended content. For example, a user of a popular movie torrent tracker reported the following case on Reddit: Further analysis of the attack revealed that instead of compromising torrent trackers, the threat actor modified a widely used public repository of torrent files, itorrents[.]org . As a result, the trackers that relied on the repository began inadvertently distributing malicious torrent files to their users. This approach is particularly powerful because it lets the threat actor reach users of multiple trackers without having to compromise each platform individually. As of the publication date of this report, the archive remains compromised. When a user attempts to download a torrent via a magnet link, the legitimate torrent archive returns a different torrent file. This malicious torrent leads to the download of the malware loader, used to deploy a framework that we dubbed MovieReaper. The loader initiates the infection chain shown in the diagram below. Each stage of the chain is described in detail in the following sections. Malware implants The infection chain consists of several steps, where only the initial one is dropped on the disk before it is executed to avoid detection. The malware itself is not heavily obfuscated, apart from strings being encrypted with a custom stream cipher. Most of the countermeasures were aimed at avoiding detection by AV sandboxes. Step 1: Loader The most popular initial executable was distributed through torrent trackers under many different names (for example, the odyssey (2026) [1080p] [webrip] [5.1].exe ),
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: The Odyssey and Trojans again: MovieReaper attacks users in multiple countries through compromised torrents
  - Published: 2026-09-17T13:00:53+00:00
  - Link: https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/
  - Summary: Kaspersky experts have discovered a new MovieReaper campaign. The multi-stage Trojan spreads through movie torrents, such as The Odyssey, and uses the Solana blockchain to hide its C2 infrastructure.

### Cluster 52127152d6 — score 14

- Title: Cisco Zero-Day Highlights API Endpoint Authentication Issues
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-18T19:26:47+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-76460

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: OpenAI/ChatGPT
- cve_ids: CVE-2026-76460
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: OpenAI/ChatGPT
- cve_ids: CVE-2026-76460
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The authentication bypass flaw CVE-2026-76460 impacts Cisco's Identity Services Engine (ISE) and received a maximum 10 out of 10 CVSS score.
```

#### Full body

```
Vulnerabilities & Threats Cyber Risk Application Security Cyberattacks & Data Breaches News Cisco Zero-Day Highlights API Endpoint Authentication Issues The authentication bypass flaw CVE-2026-76460 impacts Cisco's Identity Services Engine (ISE) and received a maximum 10 out of 10 CVSS score. Rob Wright , Senior News Director , Dark Reading September 18, 2026 4 Min Read Source: saifulasmee chede via Getty Images Cisco this week disclosed a slew of critical security vulnerabilities impacting its Identity Services Engine (ISE), including a maximum-severity zero-day flaw that's under exploitation. CVE-2026-76460 is an authentication bypass vulnerability impacting an API in ISE , Cisco's network access control and zero-trust solution. According to the company, the flaw stems from "insufficient authentication control" on an ISE API endpoint. "An attacker could exploit this vulnerability by sending a crafted request to an affected API endpoint," Cisco said in its advisory . "A successful exploit could allow the attacker to gain unauthorized access to the affected device by bypassing the web-based management interface." The bug was disclosed and patched on Sept. 16, and the Cybersecurity and Infrastructure Security Agency (CISA) added the flaw to its Known Exploited Vulnerabilities (KEV) catalog on the same day. Cisco also disclosed and patched several other bugs affecting ISE and ISE Passive Identity Connector (ISE-PIC) that have similar API authentication issues. Related: MFA Won't Save You From OAuth Consent Abuse It's unclear who is exploiting CVE-2026-76460 and how extensive the activity is. (Dark Reading contacted Cisco for comment, but the company did not address the questions and instead provided a brief statement that echoed the advisory.) But the zero-day attacks illustrate a trend of API authentication issues for the networking giant, as well as beyond. "Missing authentication for API endpoints is an industry-wide problem," Johannes Ullrich, founder of the SANS Internet Storm Center, tells Dark Reading. In theory, each request to an API endpoint should be properly authenticated and access-controlled. However, that doesn't always happen. "In some cases, APIs that were not directly reachable in the past are exposed, and in the process, proper authentication and access control are skipped," Ullrich says. "This easily happens as more extensive APIs are exposed to support more modern web application interfaces." ISE Zero-Day Puts Entire Network at Risk CVE-2026-76460 is particularly dangerous for several reasons. First, successful exploitation allows an attacker to gain root privileges and command execution on vulnerable instances, with no authentication or user interaction required. Second and more importantly, Ullrich explains, ISE itself is used by other Cisco APIs for authentication and access control. Therefore, an attacker that compromises ISE can disable the solution and gain access to various networks or impersonate other hosts. This could lead to additional compromises, he says, because applications may now rely on access control decisions from the compromised ISE platform. Related: Black Hat USA 2026 | OpenAI's Deep Dive Into Hugging Face Incident "In short, it is like replacing a building's security guard with an imposter, how it allows intruders to enter using fake IDs," Ullrich says. "Employees inside the building will trust these IDs because they believe that the security guard at the entrance checked them." In an advisory for CVE-2026-76460, threat intelligence provider BitSight noted that ISE is at the heart of many organizations' identity and network access infrastructure. "It helps determine which users and devices can connect to a network and what they can access after connecting," Emma Stevens, senior threat intelligence advisor at Bitsight, wrote. "Root-level access to that infrastructure can create visibility, integrity, and availability risks across a much wider environment." Ullrich notes that API endpoi
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Cisco Zero-Day Highlights API Endpoint Authentication Issues
  - Published: 2026-09-18T19:26:47+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues
  - Summary: The authentication bypass flaw CVE-2026-76460 impacts Cisco's Identity Services Engine (ISE) and received a maximum 10 out of 10 CVSS score.

### Cluster 12a6389ae4 — score 14

- Title: Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-22T16:14:04+00:00
- Link: https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Microsoft Defender

#### Cluster taxonomy (union across members)
- threat_categories: ddos, zero_day
- affected_products: Anthropic/Claude, Linux kernel, Microsoft Defender
- cve_ids: CVE-2026-45498
- urgency_signals: no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, ddos
- affected_products: Microsoft Defender, Anthropic/Claude, Linux kernel
- cve_ids: CVE-2026-45498
- urgency_signals: zero_day, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A zero-day proof-of-concept tool that stops Microsoft Defender from installing platform and signature updates by filling all available disk space was published on GitHub on September 19. The tool, called BigDiskBuster, has no patch, no CVE, and no Microsoft advisory. Its author, Abdelhamid Naceri, is a former Microsoft security researcher whose earlier Defender exploits were used in
```

#### Full body

```
Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates  Swati Khandelwal  Sep 22, 2026 Vulnerability / Endpoint Security A zero-day proof-of-concept tool that stops Microsoft Defender from installing platform and signature updates by filling all available disk space was published on GitHub on September 19. The tool, called BigDiskBuster , has no patch, no CVE, and no Microsoft advisory. Its author, Abdelhamid Naceri, is a former Microsoft security researcher whose earlier Defender exploits were used in attacks. When updates are blocked, Defender keeps running, but its detection content grows stale. The researcher's screenshot shows Defender returning a generic Windows error when trying to update, but whether the failure raises an automatic alert is not clear from the proof-of-concept alone. Naceri said he was dismissed from Microsoft's Security Response Center in 2024 and has been releasing exploits without coordinating with the company since April. His first three Defender tools — BlueHammer, RedSun, and UnDefend — were all exploited in live intrusions before Microsoft patched them and CISA added all three to its Known Exploited Vulnerabilities catalog. He has since disclosed additional Defender and Windows flaws roughly monthly. BigDiskBuster watches the C:\ drive for new directories under Defender's update paths. When Defender begins downloading a platform or definition update, the tool creates a hidden temporary file sized to fill all remaining free space, and the update fails. Once the update fails and Defender removes its staging directory, the tool deletes the file and waits for the next attempt. It also opens a handle on MRT.exe, the Windows Malicious Software Removal Tool, in a way that would block Windows Update from replacing it. Naceri describes the tool as "a bit buggy and needs some rewritting" and says it seems to work on all supported Windows versions. No independent researcher has confirmed the claimed behavior. Naceri calls BigDiskBuster "similar to UnDefend ," a Defender denial-of-service flaw he disclosed in April that blocked definition updates through a different method. Microsoft patched it in May as CVE-2026-45498 in Antimalware Platform version 4.18.26040.7. The two tools work differently. UnDefend used uncontrolled resource consumption, while BigDiskBuster fills the disk so Defender's update directories cannot grow. Whether the May patch also covers this new technique is not established, and the different mechanism suggests it does not. What Defenders Should Do No patch or vendor workaround exists for BigDiskBuster. Administrators can check that Defender's signatures and platform version are current through Windows Security under Virus & threat protection, then Protection updates, then Check for updates. In PowerShell, Get-MpComputerStatus shows the current versions in the AMEngineVersion and AMProductVersion fields. Monitoring for repeated Defender update failures, sustained low disk space on the system volume, and large hidden files in temporary directories would help detect the technique. Restricting execution of unknown binaries through WDAC or AppLocker would limit an attacker's ability to run the tool. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  endpoint security , Microsoft , Vulnerability , Windows ⚡ Top Stories This Week Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root ThreatsDay: Self-Rewriting Agent
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates
  - Published: 2026-09-22T16:14:04+00:00
  - Link: https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html
  - Summary: A zero-day proof-of-concept tool that stops Microsoft Defender from installing platform and signature updates by filling all available disk space was published on GitHub on September 19. The tool, called BigDiskBuster, has no patch, no CVE, and no Microsoft advisory. Its author, Abdelhamid Naceri, is a former Microsoft security researcher whose earlier Defender exploits were used in

### Cluster c56eac66cf — score 14

- Title: npm Supply-Chain Attack Abuses Trusted Publishing to Ship GHAPPIER Loader
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-09-22T17:34:47+00:00
- Link: https://orca.security/resources/research/ghappier-loader-npm-supply-chain-attack/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 4
- Strong signals: npm

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, supply_chain
- affected_products: GitHub, PyPI, npm
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, data_breach
- affected_products: npm, GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Executive Summary A high-severity supply-chain attack was disclosed affecting the npm package @dforge-core/dforge-mcp, allowing attackers to distribute a remote-shell implant via a legitimate-looking update carrying valid npm provenance signatures. Due to the potential for full system compromise and the difficulty of forensic detection, immediate action is recommended for any organization that consumed version 0.2.21. Technical […]
```

#### Full body

```
Executive Summary A high-severity supply-chain attack was disclosed affecting the npm package @dforge-core/dforge-mcp, allowing attackers to distribute a remote-shell implant via a legitimate-looking update carrying valid npm provenance signatures. Due to the potential for full system compromise and the difficulty of forensic detection, immediate action is recommended for any organization that consumed version 0.2.21. Technical Overview The attack exploited a fundamental limitation of npm trusted publishing: provenance attests where an artifact was built, not whether its source was honest. On September 9, 2026, attackers compromised the maintainer account and modified the GitHub Actions release workflow so that any push to the main branch triggered an automated release through OIDC trusted publishing. With push access converted into publish access, the GHAPPIER loader was shipped as version 0.2.21, a single malicious line hidden at line 3320 of a 99KB configuration file. The release carried valid provenance through GitHub Actions OIDC, with attestation recorded in Sigstore’s append-only public log. The four-stage payload chain activated only when the MCP server was launched, not during package installation. The final implant established a general-purpose remote shell and then deleted itself from disk upon execution, leaving no file-based forensic trace. Version 0.2.21 remained the latest release for approximately 35 minutes before the maintainer published a clean version 0.2.22. CloudSEK traced the GHAPPIER loader across 65 public repositories, 73 infected files, and 22 accounts. A second payload in another victim’s repository matched PolinRider, a DPRK-linked campaign tracked since March 2026 that uses Ethereum blockchain transactions for command-and-control configuration. By writing configuration into the twenty bytes of a recipient address on empty transactions, the operators created a C2 channel with no domain to suspend, no host to seize, and no account to disable. Affected Systems The following component is affected: @dforge-core/dforge-mcp version 0.2.21. Version 0.2.20 was also a malicious release attempt but failed and broke installation. These versions were published during a 105-minute compromise window. No CVE has been assigned, and no advisory currently exists in OSV, the GitHub Advisory Database, or from the maintainer. Organizations should take the following steps: Pin @dforge-core/dforge-mcp to version 0.2.22 or later Treat any lockfile pinning version 0.2.21 as an indicator of potential compromise Search for intermediate artifacts left by the four-stage chain rather than the final implant, which self-deletes at startup and leaves no disk trace Block the socket endpoint and two delivery hostnames identified in the CloudSEK report Monitor for release workflow trigger modifications in GitHub Actions configurations Audit whether any CI/CD systems executed version 0.2.21 of the MCP server Rotate credentials on any system where version 0.2.21 was executed At the time of writing, no CVE or formal advisory has been published. The attack is confirmed through CloudSEK’s published analysis, and the GHAPPIER campaign remains active across dozens of repositories. The sophistication of the attack, valid provenance signatures providing false assurance, blockchain-based C2 resilient to takedown, and a self-deleting implant, makes this a significant risk for any organization with exposed npm supply chains. Risk Impact Successful exploitation allows attackers to execute arbitrary commands on affected systems, exfiltrate credentials and sensitive data, and pivot to connected infrastructure, leading to service disruption, data exposure, or full infrastructure compromise. How Orca Can Help Orca enables customers to quickly identify assets running vulnerable package versions, understand their exposure in context, including internet accessibility, runtime reachability, and asset criticality, and prioritize remediation based on real
```

#### Corroborating sources (4)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: npm Supply-Chain Attack Abuses Trusted Publishing to Ship GHAPPIER Loader
  - Published: 2026-09-22T17:34:47+00:00
  - Link: https://orca.security/resources/research/ghappier-loader-npm-supply-chain-attack/
  - Summary: Executive Summary A high-severity supply-chain attack was disclosed affecting the npm package @dforge-core/dforge-mcp, allowing attackers to distribute a remote-shell implant via a legitimate-looking update carrying valid npm provenance signatures. Due to the potential for full system compromise and the difficulty of forensic detection, immediate action is recommended for any organization that consumed version 0.2.21. Technical […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI
  - Published: 2026-09-23T13:52:46+00:00
  - Link: https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html
  - Summary: Unknown threat actors have managed to compromise two legitimate MemTensor packages across the npm and Python Package Index (PyPI) repositories to push a platform-specific Go-based implant dubbed sckit designed for Windows, Linux, and macOS. According to reports from Aikido, SafeDep, Socket, and StepSecurity, the libraries in question below - @memtensor/memos-cloud-openclaw-plugin versions
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Shai-Hulud Attack Nips Cyber-Firm CrowdSec's GitHub Data
  - Published: 2026-09-22T10:22:37+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/shai-hulud-attack-cyber-firm-crowdsec-github-data
  - Summary: Threat actors stole the contents of 170 private repositories using an OAuth token stolen from a former employee's computer through the TanStack npm supply chain attack.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Attackers Abuse npm Trusted Publishing in GHAPPIER Campaign
  - Published: 2026-09-21T13:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/attackers-abuse-npm-trusted/
  - Summary: CloudSEK linked GHAPPIER to a compromised npm package with valid trusted-publishing provenance

### Cluster c235fc8c50 — score 14

- Title: Strengthen your CI/CD pipeline with new Secure Source Manager capabilities
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-09-21T16:00:00+00:00
- Link: https://cloud.google.com/blog/products/identity-security/strengthen-your-cicd-pipeline-with-new-secure-source-manager-capabilities/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government
- affected_products: Azure, Google Cloud, Google/Gemini, Kubernetes, Salesforce
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government
- affected_products: Google Cloud, Google/Gemini
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A resilient software supply chain is the foundation of modern delivery, and securing your continuous integration and continuous delivery (CI/CD) pipeline is what keeps innovation moving safely. Notable supply chain attacks more than doubled in the first half of 2026 compared to the second half of 2025, according to Wiz’s recent Cloud Threat Highlights report . It’s crucial that your source code not be the weakest link in your private cloud. To help you better address software supply chain threats, Google Cloud Secure Source Manager (SSM) lets you manage your source and CI/CD systems with unified authentication and authorization mechanisms. We now offer two new capabilities, both generally available, that can simplify and secure your development and CI/CD workflows: Unauthorized access to CI/CD systems : Attackers only need to alter a single deployment script to turn your CI/CD pipeline into a vehicle for malware. To help mitigate this risk, from the version control system to the build
```

#### Full body

```
Security & Identity Strengthen your CI/CD pipeline with new Secure Source Manager capabilities September 21, 2026 Logan Henriquez Product Manager, Google Cloud Try Gemini Enterprise today The front door to AI in the workplace Try now A resilient software supply chain is the foundation of modern delivery, and securing your continuous integration and continuous delivery (CI/CD) pipeline is what keeps innovation moving safely. Notable supply chain attacks more than doubled in the first half of 2026 compared to the second half of 2025, according to Wiz’s recent Cloud Threat Highlights report . It’s crucial that your source code not be the weakest link in your private cloud. To help you better address software supply chain threats, Google Cloud Secure Source Manager (SSM) lets you manage your source and CI/CD systems with unified authentication and authorization mechanisms. We now offer two new capabilities, both generally available, that can simplify and secure your development and CI/CD workflows: Unauthorized access to CI/CD systems : Attackers only need to alter a single deployment script to turn your CI/CD pipeline into a vehicle for malware. To help mitigate this risk, from the version control system to the build and artifact systems, to deployment tools, SSM can now block unauthorized access to your CI/CD systems even if your corporate network has been compromised. Unauthorized changes to code by authorized users : The new Code Owners system manages pull request approver sets at a per-file and per-branch level to help provide more granular identity and access management (IAM). Code Owners helps engineers who need to write, edit, and review code. It adds additional guards to files and directories in your repository at a per-file or per-branch level. Key capabilities Beginning with source code changes to your CI/CD pipeline, the new code owners feature gives you granular merge guards: Check in CODEOWNERS files to your repository to specify required approvers highly granularly: Per-path approver sets : Using flexible glob-style path specifiers, you can require that changes to matching files be approved by one or more of given sets of users. Branch-specific governance : Manage security and deployment rules across branches without friction. You can define different owners for main or dev in the same file, eliminating the merge conflicts that occur with existing CODEOWNERS solutions. See our documentation for more details . Nestable multi-file ownership : You aren't limited to one giant, 5,000-line root file. You can nest CODEOWNERS files in sub-directories. SSM uses a "more local wins" logic, allowing sub-teams to own their folders while the root admin maintains veto power over the entire repo. Independent approval sections : Using the [SectionName][count] syntax (e.g., [Security Team][2]), a single pull request (PR) can require independent sign-offs from multiple departments. A PR might be reviewed by a peer, but it won't merge until two members of the security team also approve. With your source code ready, SSM’s new Developer Connect integration makes it easy to connect your CI/CD system and runtimes securely, even when they are in different private networks. The private CI/CD blueprint architecture follows a secure path: Secure Source Manager connects to Private Service Connect, which connects to Cloud Build. The repository, the build pools, and the artifact storage all reside in a private network, with VPC Service Controls (VPC-SC) providing defense-in-depth to limit access to proxy endpoints. Next steps To secure your network, follow our new Private Network Integrations guide to connect SSM to Cloud Build with Developer Connect. To secure your pull request approvals, create a root CODEOWNERS file to replace blunt IAM "Approver" roles with file-specific ownership. Posted in Security & Identity Related articles Systems Changing the game: Using agentic AI to secure infrastructure code By Andrés Lagar-Cavilla • 4-minute read Se
```

#### Corroborating sources (2)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Strengthen your CI/CD pipeline with new Secure Source Manager capabilities
  - Published: 2026-09-21T16:00:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/strengthen-your-cicd-pipeline-with-new-secure-source-manager-capabilities/
  - Summary: A resilient software supply chain is the foundation of modern delivery, and securing your continuous integration and continuous delivery (CI/CD) pipeline is what keeps innovation moving safely. Notable supply chain attacks more than doubled in the first half of 2026 compared to the second half of 2025, according to Wiz’s recent Cloud Threat Highlights report . It’s crucial that your source code not be the weakest link in your private cloud. To help you better address software supply chain threats, Google Cloud Secure Source Manager (SSM) lets you manage your source and CI/CD systems with unified authentication and authorization mechanisms. We now offer two new capabilities, both generally available, that can simplify and secure your development and CI/CD workflows: Unauthorized access to CI/CD systems : Attackers only need to alter a single deployment script to turn your CI/CD pipeline into a vehicle for malware. To help mitigate this risk, from the version control system to the build
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: How One Kubernetes YAML Can Hand Over a GCP Organization
  - Published: 2026-09-23T14:01:11+00:00
  - Link: https://www.bleepingcomputer.com/news/security/how-one-kubernetes-yaml-can-hand-over-a-gcp-organization/
  - Summary: A Kubernetes user with limited permissions can potentially gain control of an entire Google Cloud organization by exploiting the authority granted to Google Kubernetes Config Connector. Varonis explains how this confused deputy problem can turn a single Kubernetes YAML file into a path to organization-wide privilege escalation. [...]

### Cluster a52d5a18d0 — score 14

- Title: ShinyHunters Claims FBI Hack Via PeopleSoft Zero Day
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-23T10:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/shinyhunters-fbi-hack-peoplesoft/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 6
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: Cl0p, ShinyHunters
- affected_industries: education, financial_services, government
- affected_products: AWS, Salesforce
- urgency_signals: zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- actor_attribution: ShinyHunters, Cl0p
- affected_industries: financial_services, education
- affected_products: Salesforce, AWS
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Infamous threat group ShinyHunters claims to have personal information on thousands of FBI employees
```

#### Full body

```
Infosecurity Magazine Home » News » ShinyHunters Claims FBI Hack Via PeopleSoft Zero Day ShinyHunters Claims FBI Hack Via PeopleSoft Zero Day News 23 September 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster The prolific hacking group ShinyHunters has claimed to have breached the FBI via a zero-day exploit and stolen data on “all FBI employees and applicants.” The group posted the news on its data leak site, reasoning it took action in retaliation for what it claims to be inaccuracies in an FBI Public Service Announcement (PSA) published on May 15. ShinyHunters seemed to take offense at claims in the PSA that it exaggerates access to sensitive information in order to extract payment, that the group harasses victims and their families, conducts swatting attacks, and falsely claims to possess sensitive/compromising material on victims. It also denied being a part of “The Com.” The group shared a sample of the compromised data with 404 Media, which first reported the story. It apparently contained personally information (PII) on 5000 FBI employees including addresses, phone numbers, dates of birth and in some cases details on spouses. The goal appears not financial extortion but to force the FBI to take down or amend the PSA. Read more on ShinyHunters: ShinyHunters Claim Hack of Rival Ransomware Gang Clop. ShinyHunters also defaced the FBI jobs website on September 22. The site was still down ‘for maintenance’ at the time of writing. PeopleSoft a Popular Target An FBI spokesperson told 404 Media that the group exploited a zero-day vulnerability in Oracle PeopleSoft before pivoting to AWS GovCloud servers and downloading 2-3TB of data. If true, it wouldn’t be the first time the group has targeted the Oracle software. Between May and June it exploited a zero day in PeopleSoft's Environment Management component to hit dozens of education institutions. “When ShinyHunters burned this vulnerability to hit more than 100 organizations, most of them universities, they later said their original goal had been an FBI PeopleSoft server, and that attempt failed,” explained Steve Povolny, VP of AI strategy & security research at Exabeam. “The education sector was collateral damage from a failed shot at the bureau. Three months later they claim a new PeopleSoft zero-day. That points to a group systematically mining ERP platforms that hold HR, payroll, applicant, and health data.” PeopleSoft customers should assume compromise, ensure the fix for the previous zero day is applied and disable the Environment Management Hub or remove the PSEMHUB application, Povolny said. “Take PeopleSoft admin and integration interfaces off the internet. Then hunt instead of waiting for a signature that doesn't exist yet,” he advised. “Look for suspicious POST activity in WebLogic access logs, unauthorized files in PSEMHUB directories, XMLDecoder-based persistence, and outbound traffic on port 445, along with remote-management agents like the MeshCentral tooling used for command and control in June.” Povolny also urged customers to evaluate the PeopleSoft host and its service identities and look for unusual API calls, bulk data queries, or authentications. “Ship logs off-host, since the attackers claim they wipe local evidence,” he concluded. “Know who owns PeopleSoft on the IR team. Be ready to rotate every secret reachable from those servers, and have authority pre-approved to isolate systems fast.” You may also like 2016 : Two Steps Forward, Three Steps Back Editorial 27 December 2016 Nissan Discloses Employee Data Breach Linked to Oracle Zero-Day News 30 June 2026 Allianz Life Data Breach Exposes Personal Data of 1.1 Million Customers News 19 August 2025 Chanel and Pandora Breached as Salesforce Campaign Continues News 6 August 2025 ShinyHunters Targets Hundreds of Websites in New Salesforce Campaign News 10 March 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice ShinyHun
```

#### Corroborating sources (6)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: ShinyHunters Claims FBI Hack Via PeopleSoft Zero Day
  - Published: 2026-09-23T10:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/shinyhunters-fbi-hack-peoplesoft/
  - Summary: Infamous threat group ShinyHunters claims to have personal information on thousands of FBI employees
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: ShinyHunters claims attack on FBI exposes almost all agents
  - Published: 2026-09-22T23:47:43+00:00
  - Link: https://cyberscoop.com/shinyhunters-claims-fbi-attack/
  - Summary: The FBI jobs site, which was temporarily defaced, remains unavailable and the agency said it’s investigating the claims. The post ShinyHunters claims attack on FBI exposes almost all agents appeared first on CyberScoop .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach
  - Published: 2026-09-22T19:13:29+00:00
  - Link: https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/
  - Summary: The ShinyHunters extortion gang claims it breached FBI systems using a new Oracle PeopleSoft zero-day vulnerability, gaining access to internal services and stealing sensitive data on employees and job applicants. [...]
- **The Record** (cyber_news_breach_reporting)
  - Title: FBI investigating alleged ShinyHunters breach of its jobs site
  - Published: 2026-09-23T14:22:00+00:00
  - Link: https://therecord.media/fbi-investigating-alleged-shinyhunters-job-site-breach
  - Summary: The ShinyHunters cybercriminal organization on Tuesday replaced agency images on the FBIjobs.gov site with a photo of a Pokemon that has become the group’s defacto mascot.
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Team Cymru unmasks shady Chinese proxy network
  - Published: 2026-09-23T05:56:34+00:00
  - Link: https://risky.biz/RBNEWS614/
  - Summary: A network of 10,000 AI servers is masking malicious Chinese AI activity, Ukrainian hackers leak Russia’s naval secrets, ShinyHunters hacks the FBI, and the EvilTokens phishing service is disrupted by tech companies.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ShinyHunters Claims FBI Breach, Says It Stole Data on Agents and Job Applicants
  - Published: 2026-09-23T05:30:09+00:00
  - Link: https://thehackernews.com/2026/09/shinyhunters-claims-fbi-breach-says-it.html
  - Summary: The cyber extortion group known as ShinyHunters on Tuesday claimed it had breached the U.S. Federal Bureau of Investigation and stolen data belonging to current and former employees at the agency. "We have compromised the FBI. We hold very sensitive data on almost ALL FBI Agents and individuals who filed an application with the FBI for a job," the group said in a statement posted on their dark

### Cluster 96fd6e2eb3 — score 12

- Title: Reimagining the SOC for the agentic era in Microsoft Defender
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-23T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We are announcing ISOC in Microsoft Defender: a foundation built for agentic security that brings leading solutions for SIEM and threat protection together. The post Reimagining the SOC for the agentic era in Microsoft Defender appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types News Products and services Microsoft Defender Topics AI and agents Security operations SIEM and XDR The physics of cybersecurity are changing. So must the security operations center (SOC). Cyberattackers are using agents to automate execution at unprecedented scale. What once required entire teams now requires a single operator and an agent framework. That shift has exposed a hard truth: security cannot operate at AI speed when protection and operations are built as separate systems. Every handoff, integration, and boundary slows defenders down. Agents inherit that complexity. For agentic security to work, the industry needs a different model. It needs a modern cyber stack with the breadth to see across the environment and the depth to investigate and act. Security operations and native protection must function as one system. This is the integrated security operations center (ISOC). Today we are announcing ISOC in Microsoft Defender : a foundation built for agentic security that brings leading solutions for security information and event management (SIEM) and threat protection together. It gives people and agents a shared foundation to see, understand, and act across the environment, without the complexity of operating separate systems. Get started with ISOC in Microsoft Defender Built for agentic security In July 2026, we introduced the end-to-end cyber stack alongside Project Perception , with the focus of delivering the right models, a harness, and specialized agents to help defenders perceive, reason, and act at machine speed. But we are innovating at every layer of the stack, because intelligence and orchestration alone are not enough. Agents depend on the rest of the stack working as one. They need signals and sensors that provide visibility, context that turns those signals into understanding, and actuators that translate decisions into protection. With ISOC, these layers work in unison, so agents can move beyond isolated tasks and help operate an agentic SOC. Signals and sensors give the system awareness. Context turns those signals into understanding. Actuators turn insights into protective action . ISOC brings these capabilities together as a foundation, so humans and agents can operate as one system, each contributing what they do best. Agents provide the speed and scale to execute continuously, while people set priorities, apply judgment, and define the outcomes that matter. Together, they empower defenders to keep pace with AI-powered threat actors and achieve better security outcomes. Integrated protection loop With ISOC enabling signals, context, and controls to work as one, it breaks the pattern of linear security workflows. The result is an integrated protection loop that continuously turns what defenders learn into stronger pre-breach protection. Attack disruption in Microsoft Defender shows what this makes possible. Rich telemetry and controls enable the system to detect, predict, and adapt to an attacker while the attack is still unfolding. It disrupts threats in progress and anticipates where attackers may move next. It’s a protection loop that uses exposure insights to strengthen protection in near real-time with threat intelligence focusing the loop on the threats that matter most. ISOC brings together the capabilities needed to make this loop native, eliminating the burden of assembling, tuning, and maintaining it yourself. And as protection advances, new capabilities can become part of that loop. The result is stronger protection and a different way of working, where practitioners spend less time chasing individual signals and more time applying judgment, setting priorities, and driving security outcomes. Designed for the practitioner For too long, practitioners have had to compensate for the boundaries in their security architecture, stitching together signals, rebuilding context, and moving between tools just to get the information and controls needed to
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Reimagining the SOC for the agentic era in Microsoft Defender
  - Published: 2026-09-23T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/
  - Summary: We are announcing ISOC in Microsoft Defender: a foundation built for agentic security that brings leading solutions for SIEM and threat protection together. The post Reimagining the SOC for the agentic era in Microsoft Defender appeared first on Microsoft Security Blog .

### Cluster 7c416ee970 — score 12

- Title: Federal & Mission-Critical Security Validation
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-23T13:36:21+00:00
- Link: https://horizon3.ai/intelligence/blogs/federal-mission-critical-security-validation/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- actor_attribution: MuddyWater
- affected_industries: government
- affected_products: Microsoft Entra
- cve_ids: CVE-2020-1472
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: apt_espionage
- actor_attribution: MuddyWater
- affected_industries: government
- affected_products: Microsoft Entra
- cve_ids: CVE-2020-1472
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
How federal security teams perform continuous validation — identity-first testing, exploit-led proof, and FedRAMP-aligned remediation with NodeZero Federal™.
```

#### Full body

```
Federal & Mission-Critical Security Validation Horizon3 September 23, 2026 Blogs Federal security teams face a problem most enterprises don’t. For them, the consequences of a breach aren’t measured in reputational damage or regulatory fines alone. They’re measured in mission failure, compromised intelligence, and national security risk. These stakes demand a different standard of security validation, one built on proof instead of assumptions. The Core Problem: Federal Environments Cannot Rely on Annual Snapshots Most enterprise security programs are built around periodic assessments. A penetration test runs once or twice a year. Vulnerability scanners run on a schedule. Findings are triaged, remediation is tracked, and the cycle repeats. In federal environments, that model has a structural flaw. Nation-state adversaries do not operate on a quarterly schedule. Iranian, Chinese, and Russian threat actors probe identity systems continuously, exploit configuration drift between audit cycles, and move from initial access to domain compromise faster than most remediation programs can respond. Why Point-in-Time Testing Creates Gaps The results of one security assessment might be entirely invalid three weeks later. In a documented Horizon3 engagement modeled on Iranian threat actor tradecraft, NodeZero® identified Zerologon (CVE-2020-1472) on a critical domain controller within hours. The flaw that enables full domain compromise and aligns directly with how Iranian groups like MuddyWater and Magic Hound operate. The weakness was patched, hardened, and re-validated as eliminated in just over 24 hours. The gap was not in the organization’s intent. It was in the validation model. Building a Federal Security Validation Program That Holds Moving from point-in-time audits to continuous, provable security requires changes at every layer of the program — tooling, process, prioritization, and reporting. The five steps below cover the operational decisions that determine whether a federal validation program produces evidence or produces noise. Step 1: Separate Vulnerability Discovery From Exploitability Validation A vulnerability scanner reports that a CVE exists. It does not report whether that CVE is reachable from an attacker’s starting position, whether it chains with other weaknesses to reach a critical asset, or whether remediation actually closed the exposure. The 18,000 to 21 Problem In a documented NodeZero® deployment, 18,000 scanner findings were reduced to 21 verified exploitable paths. The other 17,979 were not irrelevant. They were not the priority. Federal security teams that treat scanner output as validation evidence are measuring the wrong thing. Exploitable path count is the metric that reflects actual risk. Step 2: Prioritize Identity Infrastructure as the Primary Attack Surface Federal environments are disproportionately targeted through identity systems. Active Directory misconfigurations, Kerberoastable service accounts, and overly permissive Entra ID configurations create attack paths that require zero CVEs to exploit. How Fast Identity Compromise Happens The GOAD benchmark demonstrated NodeZero® compromising a fully configured Active Directory environment in 14 minutes. Human penetration testers take 12 to 16 hours for the same environment. Full Entra ID tenant compromise in two hours with zero CVEs exploited is not a theoretical risk — it is a documented outcome. Validation programs that treat identity testing as a secondary workstream have the priority inverted. Step 3: Build the Hack, Fix, Verify, Repeat Cycle Into Operations Security validation is not a project. It is an operational cycle. The mistake most federal security programs make is treating each validation run as a standalone engagement with a defined start and end date. What Continuous Validation Looks Like NodeZero Federal™ ‘s 1-Click Verify capability re-tests a specific weakness after remediation to confirm the fix held and did not introduce new exposure
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Federal & Mission-Critical Security Validation
  - Published: 2026-09-23T13:36:21+00:00
  - Link: https://horizon3.ai/intelligence/blogs/federal-mission-critical-security-validation/
  - Summary: How federal security teams perform continuous validation — identity-first testing, exploit-led proof, and FedRAMP-aligned remediation with NodeZero Federal™.

### Cluster 3494226aac — score 12

- Title: How dynamic application security testing validates risk at runtime
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-23T13:49:39+00:00
- Link: https://www.rapid7.com/blog/post/em-dynamic-application-security-testing-dast-validates-risk-at-runtime-idc-marketscape
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
Security teams already have long queues of potential application vulnerabilities. The useful question is what happens next: can they see how a weakness behaves in a running application, reproduce the attack, and give developers enough evidence to fix it? Dynamic application security testing (DAST) helps answer those questions by testing applications as an attacker encounters them. The IDC MarketScape: Worldwide Dynamic Application Security Testing 2026 Vendor Assessment (Doc #US54119126, September 2026). The IDC MarketScape evaluated 16 vendors and named Rapid7 a Leader. We believe the result reflects the strength of Rapid7’s DAST capabilities, but the IDC MarketScape also offers a useful view of where the category is heading. DAST has developed beyond traditional web scanning into a source of runtime evidence that can help organizations validate risk across the application layer. From possible weakness to validated application risk Code analysis and dependency scanning help teams iden
```

#### Full body

```
Exposure Command How dynamic application security testing validates risk at runtime Rapid7 Sep 23, 2026 | Last updated on Sep 23, 2026 | 3 min read DISCOVER EXPOSURE COMMAND How dynamic application security testing validates risk at runtime Table of contents How dynamic application security testing validates risk at runtime DISCOVER EXPOSURE COMMAND Table of contents Security teams already have long queues of potential application vulnerabilities. The useful question is what happens next: can they see how a weakness behaves in a running application, reproduce the attack, and give developers enough evidence to fix it? Dynamic application security testing (DAST) helps answer those questions by testing applications as an attacker encounters them. The IDC MarketScape: Worldwide Dynamic Application Security Testing 2026 Vendor Assessment (Doc #US54119126, September 2026). The IDC MarketScape evaluated 16 vendors and named Rapid7 a Leader. We believe the result reflects the strength of Rapid7’s DAST capabilities, but the IDC MarketScape also offers a useful view of where the category is heading. DAST has developed beyond traditional web scanning into a source of runtime evidence that can help organizations validate risk across the application layer. From possible weakness to validated application risk Code analysis and dependency scanning help teams identify weaknesses before an application is deployed. DAST provides a different view by interacting with the assembled application while it is running. It can show what happens when a particular request reaches the application, how the application responds, and whether a suspected weakness can be reproduced. This is especially valuable for APIs and AI-backed applications, where risk may emerge through interactions among models, prompts, data, tools, and permissions. Some of these behaviors cannot be fully understood from source code or a dependency manifest. They become visible when the application is exercised under runtime conditions. DAST therefore has a direct role in continuous threat exposure management (CTEM). Discovery gives teams a view of their assets and possible weaknesses, but that view alone does not tell them where to focus. Validation helps narrow the field by showing which exposures can be reached or exploited and providing evidence that teams can use to take action. For Rapid7, DAST is exposure management applied to the application layer. Web applications, APIs, and AI-backed endpoints are all part of the attack surface, so they need to be discovered, tested, prioritized, and managed alongside infrastructure, cloud, and other exposures. Why we believe Rapid7 was named a Leader by IDC Rapid7’s DAST solution is delivered as part of the Exposure Command portfolio. Its scan engine maps an application, executes attacks against the discovered paths, and validates confirmed findings. Security teams can map a broad area of an application while limiting active attacks to an appropriate set of paths, giving them control over how testing is performed. Findings are checked against Rapid7 telemetry to help determine which issues warrant closer attention. When a finding needs action, browser-based replay reproduces the original request, the attack request, and the triggering response. Developers receive evidence they can work with, rather than a finding they must first spend time proving. Authenticated scanning can be difficult to maintain across a changing application portfolio, and a broken login sequence can leave important areas untested. Rapid7’s solution can identify the affected step and support a targeted update without requiring the entire sequence to be recorded again. The connection with Surface Command adds another useful layer. Newly discovered external assets can be surfaced for application testing, helping teams close the gap between finding an application and understanding the risk it presents DAST plays a core role within Exposure Command: providing the application-
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: How dynamic application security testing validates risk at runtime
  - Published: 2026-09-23T13:49:39+00:00
  - Link: https://www.rapid7.com/blog/post/em-dynamic-application-security-testing-dast-validates-risk-at-runtime-idc-marketscape
  - Summary: Security teams already have long queues of potential application vulnerabilities. The useful question is what happens next: can they see how a weakness behaves in a running application, reproduce the attack, and give developers enough evidence to fix it? Dynamic application security testing (DAST) helps answer those questions by testing applications as an attacker encounters them. The IDC MarketScape: Worldwide Dynamic Application Security Testing 2026 Vendor Assessment (Doc #US54119126, September 2026). The IDC MarketScape evaluated 16 vendors and named Rapid7 a Leader. We believe the result reflects the strength of Rapid7’s DAST capabilities, but the IDC MarketScape also offers a useful view of where the category is heading. DAST has developed beyond traditional web scanning into a source of runtime evidence that can help organizations validate risk across the application layer. From possible weakness to validated application risk Code analysis and dependency scanning help teams iden

### Cluster fd9f20df1d — score 12

- Title: F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-23T07:17:23+00:00
- Link: https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: government
- affected_products: F5 BIG-IP, WordPress
- cve_ids: CVE-2026-94127
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, apt_espionage, web_shell_backdoor, active_exploitation
- affected_industries: government
- affected_products: F5 BIG-IP, WordPress
- cve_ids: CVE-2026-94127
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
F5 has released security updates to address a critical BIG-IP APM zero-day vulnerability being exploited in remote code execution attacks. [...]
```

#### Full body

```
F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks By Sergiu Gatlan September 23, 2026 03:17 AM 0 F5 has released security updates to address a critical BIG-IP APM zero-day vulnerability being exploited in remote code execution attacks. BIG-IP APM (short for Access Policy Manager) is the company's centralized access management proxy solution that helps admins secure access to their organizations' networks, applications, cloud, and application programming interfaces (APIs). Tracked as CVE-2026-94127 , the flaw affects instances configured as an OAuth Authorization Server when a BIG-IP APM access policy and an OAuth profile are configured on a virtual server. "We have learned that this vulnerability has been exploited," F5 warned in a security advisory published on Tuesday. "Deployments using APM strictly as an OAuth Client / Resource Server (without OAuth authorization server profiles configured) are not affected by this vulnerability." The company advised customers to review systems for indicators of compromise if they detect a combination of multiple OAuth authentication failures and suspicious commands, shortly followed by a TMM SIGABRT. F5 also shared mitigation measures for admins who can't immediately install the security updates, which require applying an iRule (available from F5 Support ) to the affected BIG-IP APM virtual server. Internet threat monitoring non-profit Shadowserver currently tracks over 14,700 IP addresses with BIG-IP APM fingerprints . However, there is no information on how many have already been patched or are honeypots. F5 BIG-IP APM exposed online (Shadowserver) On Tuesday, the Cybersecurity and Infrastructure Security Agency (CISA) also added CVE-2026-94127 to its Known Exploited Vulnerabilities (KEV) Catalog and ordered U.S. federal agencies to secure their networks against this flaw by Friday . "These types of vulnerabilities are a frequent attack vector for malicious cyber actors and pose significant risks to the federal enterprise," the cybersecurity agency warned. Cybercrime and state-backed threat groups have often exploited F5 vulnerabilities in recent years. For instance, attackers have targeted security flaws in F5 products to breach corporate networks , hijack devices , ​​​​​​ map internal servers , deploy data-wiping malware , and steal sensitive documents . F5 also disclosed in October 2025 that state-sponsored hackers breached its systems in August 2025 and stole undisclosed BIG-IP security source code and vulnerabilities. Since November 2021, CISA has flagged eight actively exploited F5 vulnerabilities , four of which have also been abused in ransomware attacks. F5 is a Fortune 500 company that provides cybersecurity, application delivery networking (ADN), and other services to more than 23,000 customers worldwide, including 48 of the Fortune 50 companies and 80% of the Fortune Global 500. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Hackers breach F5 BIG-IP APM devices to deploy Linux rootkit Hackers start exploiting critical WordPress flaw for code execution Arista patches actively exploited VeloCloud Orchestrator zero-day Magento StyleSmuggler zero-day exploited to deploy Linux backdoor N-able patches max severity N-central flaw amid ongoing attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks
  - Published: 2026-09-23T07:17:23+00:00
  - Link: https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/
  - Summary: F5 has released security updates to address a critical BIG-IP APM zero-day vulnerability being exploited in remote code execution attacks. [...]

### Cluster 4ff2661d4c — score 12

- Title: Supply Chain & CTI
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
- Link: https://www.team-cymru.com/post/supply-chain-cti
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- affected_industries: government
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- affected_industries: government
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
This blog explores how cyber threat intelligence (CTI) must change and support a new approach to supply chain risk.
```

#### Full body

```
Will Thomas 5 min read July 8, 2025 Supply Chain & CTI Why expanding third party risks is no longer a luxury In this blog, we‚Äôll explore how cyber threat intelligence (CTI) must change and support a new approach to supply chain risk. Across the globe, many new laws like DORA in the EU and CMMC in the US have been implemented, driving the need to not just reactively engage with your supply chain, but proactively collaborate and monitor third-party infrastructure for signals of compromise. The underlying intention is that the ecosystem you are part of is more robust when working together. These regulations are likely to be adopted by many other industries, making this blog worthwhile reading for security teams of all sizes and sectors. Reactive supply chain management typically involves sending Supplier Assurance Questionnaires (SAQs) to suppliers after a confirmed breach has occurred, often by the time it makes the news. Many large organizations have taken the initiative to leverage threat intelligence services that support checking for brand name keywords or domains appearing on ransomware data leak sites, cybercrime forum posts, or darkweb credential markets. An even more proactive measure that could be taken to manage supply chain risks involves using passive scanning services to check for unpatched vulnerabilities in supply chain networks, as well as using NetFlow data to detect malicious command-and-control (C2) communications originating from supplier environments. Key Findings Technology leaders are issuing warnings to their supply chain to modernise their cybersecurity practices Governments are introducing more legislation to protect digital services and critical sectors from supply chain risks More organizations need to incorporate proactive threat intelligence to evaluate supply chain vendors Netflow data presents itself as a useful alternative method for organizations to validate supply chain ecosystems. Supply Chain Management Many organizations start by prioritising who their supply chain vendors are and create a criteria based on several factors, such as the impact to business operations if they were attacked, or the sensitivity of the data they process or store for them. Other factors that come into play are whether the supply chain vendors have direct network access into the organization‚Äôs environment, and which environments those are as well. One of the challenging aspects for CTI teams doing this type of work is figuring all these things out for a large number of suppliers. Fortune 500 organizations will often have upwards of 5,000 suppliers, in many cases from around the world. Working out these factors for every supplier to rank and prioritise them is difficult on its own. This type of information is often only available in contracts possessed by the procurement or law departments and may be vague and obscure. Getting a handle on which suppliers have direct network access to your organization‚Äôs environment is often made a priority due to the implications of a software supply chain attack or identity-based network intrusion. Without network-level visibility to know where cyber threats can arrive from, the chances of detecting an intrusion are severely diminished. In other cases, knowing which suppliers handle the most sensitive information about your organization is also crucial to understanding your expanded attack surface that extends to third parties. Supply chain partners such as law firms will often hold highly sensitive information for their clients, making them ideal targets for persistent adversaries willing to put in the work to get in. Defining Cyber Threat Intelligence Team Capabilities Before we detail the sources of CTI, let‚Äôs explore the nuances that will enable you to align with your existing teams and capabilities. First on the maturity ladder from a CTI perspective is supporting Incident Response operations, which can include Reactive Threat Hunting operations. At this stage, many CTI
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Supply Chain & CTI
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/supply-chain-cti
  - Summary: This blog explores how cyber threat intelligence (CTI) must change and support a new approach to supply chain risk.

### Cluster bd4fb91f5d — score 12

- Title: Threat Intelligence: A CISO ROI Guide - Elite Threat Hunters Prevent Supply Chain Breaches
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
- Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-elite-threat-hunters-prevent-supply-chain-breaches
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- affected_industries: financial_services, legal_professional
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- affected_industries: financial_services, legal_professional
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Discover how elite threat hunters and Pure Signal Recon help CISOs prevent supply chain breaches, save millions, and boost security ROI. Learn more.
```

#### Full body

```
tcblogposts min read March 13, 2024 Threat Intelligence: A CISO ROI Guide - Elite Threat Hunters Prevent Supply Chain Breaches Up the Ante Against Supply Chain Attacks and Still Have Time to Save the World Introduction In our first post we talked about how external threat hunting with Pure Signal Recon can have a direct financial savings in terms of reducing the cost of a data breach and minimizing risk. In our second blog post we talked about how most organizations need fewer cyber threat intelligence sources than they subscribe to, it‚Äôs a good place to realize some tactical yet meaningful budget savings. Based on feedback from our Fortune 10 client, we also explored how too many CTI sources can detract from your external threat hunting program if the curated data isn‚Äôt relevant or timely. Let‚Äôs discuss the impact Pure Signal Recon had on this Fortune 10 security organization to help them better identify security gaps and confirmed threats originating from their supply chain. Additional visibility and leveraging the right CTI data reduced the cost of compromise, with use cases such as: Early identification of compromised third parties Shut down of threat actor Command & Control (C2) communications in real-time Blocking 24 of 30 significant events with third parties.* Notifying an additional 300 compromised organizations and provided enough information to prevent or minimize damage Raising the cost to attack - Continually forced bad actors to retool their infrastructure ‚ÄúIn the beginning of 2020, we saw a major increase in ransomware hitting our third parties. If they are compromised in any way, shape, or form, then our IR and legal teams become actively involved. They make sure that no data related to us is leaked, that [the third party‚Äôs] network is secure, and that [the third party] won‚Äôt be used as a pivot to get into our networks. There‚Äôs a time-consuming process that comes with a compromise of our third parties.‚Äù Lead security analyst In addition, their supply chain threat hunting and monitoring efforts earned a projected cost reduction of $1,3M of net present value savings over three years. A Mile Long Supply Chain Requires Significant Expertise to Secure This Fortune 10 multinational national retailer has a supply chain that is expansive as it varied. While there is no doubt their supply chain serves as a strategic advantage; it can also be used as another attack vector to compromise vulnerable core applications and security gaps in infrastructure. This is no surprise considering 98% of organizations have a relationship with at least one third party that has experienced a breach in the last two years.1 Every compromised supply chain partner incident has a significant cost in terms of cybersecurity, legal and potentially PR expertise to respond to an event, depending how far reaching the breach, and how well recognized your brand. Time is crucial to ensuring a third-party breach can‚Äôt be used to pivot into core systems. The legal & PR teams get involved to minimize the possibility of negative press and customer notification mandates. ‚ÄúWith Recon, we map the infrastructure being used by some ransomware groups. We block them from entering our network, monitor their infrastructures as they evolve, and monitor potential victims such as third-party entities. When [a third party is] compromised, we identify it with Recon, then tell [the third party] how [the threat actor] got in ... and what they need to do to stop them immediately.‚Äù Lead security analyst The case study organization typically requires at least 15 FTE security analysts or legal professionals working three days each when a partner is compromised. Using Pure Signal Recon , they were able to block 24 of 30 significant events with a third party. Using a simple formula of $75 per hour for each FTE multiplied by 3 days each, it is easy to see how the cost of responding to supply chain compromises adds up. High-risk third-party threat events whe
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Threat Intelligence: A CISO ROI Guide - Elite Threat Hunters Prevent Supply Chain Breaches
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-elite-threat-hunters-prevent-supply-chain-breaches
  - Summary: Discover how elite threat hunters and Pure Signal Recon help CISOs prevent supply chain breaches, save millions, and boost security ROI. Learn more.

### Cluster fa3c6073d2 — score 11

- Title: The Lure Isn't The Malware. It's Your Logo.
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-23T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/your-logo-is-the-lure
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
Recorded Future's Insikt GroupⓇ has been tracking ClickFix, a social engineering technique that turns a familiar logo or verification prompt into the entry point for an attack. Here's what that research reveals about catching it, and why it's now running inside Malicious Site Monitoring, part of our newly launched Digital Risk Protection solution.
```

#### Full body

```
The Lure Isn't The Malware. It's Your Logo. Recorded Future's Insikt Group Ⓡ has been tracking ClickFix, a social engineering technique that turns a familiar logo or verification prompt into the entry point for an attack. Here's what that research reveals about catching it, and why it's now running inside Malicious Site Monitoring, part of our newly launched Digital Risk Protection solution. Recorded Future's Insikt Group Ⓡ , our team of threat intelligence analysts and security researchers, has been tracking a technique called ClickFix as it works its way into a growing number of brand impersonation campaigns. We recently hosted a webinar digging into that research, and what stood out wasn't just the technique itself. There's no malware automatically installed, no exploit, just a page convincing enough that the victim ends up doing the damage themselves. It is also a strong example of the detection capabilities built into Malicious Site Monitoring, a new use case included in Digital Risk Protection , and a good way to show what those capabilities are actually built to catch. How ClickFix actually works ClickFix works by mimicking the visual language people already trust, a CAPTCHA prompt, a familiar logo, a "verify you're human" screen, and using that trust to get someone to run a command on their own machine. There's no code being smuggled past a firewall. The victim is the delivery mechanism. That's also what makes it hard to catch with traditional tools. A page built to look exactly like a real verification screen doesn't behave like malware, and it doesn't trip the same alarms as a page trying to exploit a browser. It succeeds because the person on the other end believes they're completing something routine. It's not static, either. The instructions can change depending on the operating system a victim is running, one path for Windows, a different one for macOS, which means the "fix" itself adapts to the target. A single signature or a one-off takedown was never going to keep up with that. Catching this at scale means watching for the pattern, not waiting to recognize a specific file. Malicious Site Monitoring This kind of research and the product built to act on it aren't two separate things. Digital Risk Protection's Malicious Site Monitoring is built to catch this exact category of infrastructure, phishing domains, lookalike sites, brand impersonation, fast enough to matter. Disposable infrastructure like this is designed to do its damage and disappear before anyone gets around to reporting it, so speed isn't just a nice-to-have here, it's a necessity. Underneath that speed is a detection process built in layers. Analyst-built signatures catch known patterns with precision. Content similarity analysis can catch campaigns that move in clusters. Attackers often reuse the same page template across dozens of disposable domains, so even though each domain name looks unrelated, the pages themselves share the same structure underneath. A separate component flags a familiar logo or brand mark through screenshot analysis and Optical Character Recognition (OCR). Machine learning is often able to catch what the other methods might miss, sites that don't resemble any known signature or template, by predicting risk from the page's characteristics rather than requiring a direct match. That layered approach is what makes it possible to evaluate a massive volume of candidate domains and URLs every single day without generating excessive false positives. From detection to takedown Finding a threat fast doesn't help much if the next steps are still manual. The real shift in how Digital Risk Protection operates is this: detection, triage, and action now live in the same workflow. Not every detection needs a human to look at it immediately, and that distinction matters. A multi-stage detection funnel helps filter raw monitoring volume down to those that could need a response, and for malicious sites specifically, an AI Triage Agent review
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: The Lure Isn't The Malware. It's Your Logo.
  - Published: 2026-09-23T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/your-logo-is-the-lure
  - Summary: Recorded Future's Insikt GroupⓇ has been tracking ClickFix, a social engineering technique that turns a familiar logo or verification prompt into the entry point for an attack. Here's what that research reveals about catching it, and why it's now running inside Malicious Site Monitoring, part of our newly launched Digital Risk Protection solution.

### Cluster 7d316694da — score 11

- Title: Check Point warns of hackers exploiting Security Gateway VPN RCE flaw
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-23T19:53:54+00:00
- Link: https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-85102

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: government
- affected_products: WordPress
- cve_ids: CVE-2026-85102, CVE-2026-93616
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: government
- affected_products: WordPress
- cve_ids: CVE-2026-85102, CVE-2026-93616
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cybersecurity company Check Point has confirmed active exploitation of CVE-2026-85102, a pre-authentication remote code execution (RCE) vulnerability in the VPN certificate-handling functionality of its Security Gateway product. [...]
```

#### Full body

```
Check Point warns of hackers exploiting Security Gateway VPN RCE flaw By Bill Toulas September 23, 2026 03:53 PM 0 Cybersecurity company Check Point has confirmed active exploitation of CVE-2026-85102, a pre-authentication remote code execution (RCE) vulnerability in the VPN certificate-handling functionality of its Security Gateway product. The same advisory also warns of threat actors exploiting a pre-authentication path traversal flaw tracked as CVE-2026-93616, which impacts the Management web service and can allow script execution and Java class loading. The company says that CVE-2026-93616 has been exploited as a zero-day since July 23. On September 10, the Dutch Nationaal Cyber Security Centrum (NCSC) alerted of the Security Gateway issue and urged users to apply available security updates as imminent exploitation was expected. Check Point has now confirmed that malicious activity started on September 12, with attackers using VPNs and proxies to hide their location. “Starting September 12, 2026, we observed a wave of exploitation attempts against Spark customers,” reads Check Point’s alert . “The attempts originated from anonymization infrastructure, including VPN services and proxies," the company said, adding that certificates with the following subjects were used: CN=vpn,OU=users,O=global CN=vpn-user,OU=users,O=global CN=vpnuser,OU=users,O=global However, the cybersecurity company noted that the three subjects only reflect current observations and more may be in use. CISA has now added the two flaws in its Known Exploited Vulnerabilities (KEV) catalog , urging federal agencies to apply the available fixes and/or mitigations by September 25, 2026. Mitigating the risk Check Point’s advisory on CVE-2026-85102 recommends that administrators install Check Point LivePatch Take 26 on supported R81.20, R82, or R82.10 gateways, or install a fixed Jumbo Hotfix: R81.20 Take 166, R82 Take 126, R82.10 Take 44, or R81.10 Take 190, or later. Customers should also update Spark firewalls to R82.00.10 Build 2325 or R81.10.17 Build 4968, or later. System administrators are advised to verify if LivePatch is active by running the cpinfo -y CPupdates command on the Security Gateway in expert mode. The advisory specifically warns that some customers who installed an earlier offline LivePatch package need Take 26 for full coverage. If updating isn’t possible, it is recommended to disable the VPN implied rules and create explicit rules that restrict Site-to-Site VPN on UDP/500 and UDP/4500 to specific peer IP addresses. For Remote Access VPN, allow only the required services over UDP/500, UDP/4500, TCP/443, and TCP/80 where applicable, and restrict source client IP ranges where possible. Check Point notes that these mitigation measures do not apply to locally managed Spark firewalls. For mitigation and hunting advice for the Management web service CVE-2026-93616, Check Point points to this support article . Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Hackers start exploiting critical WordPress flaw for code execution New Check Point flaw lets hackers execute code with root privileges Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent Critical Elementor Pro flaw exploited to take over WordPress sites Hackers exploit Sangoma Switchvox flaw to deploy reverse shells
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Check Point warns of hackers exploiting Security Gateway VPN RCE flaw
  - Published: 2026-09-23T19:53:54+00:00
  - Link: https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
  - Summary: Cybersecurity company Check Point has confirmed active exploitation of CVE-2026-85102, a pre-authentication remote code execution (RCE) vulnerability in the VPN certificate-handling functionality of its Security Gateway product. [...]

### Cluster 7f120b7413 — score 11

- Title: Be alert: targeted attacks on prominent Rustaceans
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-09-17T23:59:19+00:00
- Link: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Be alert: targeted attacks on prominent Rustaceans Important warning from Adam Harvey and the crates security team: We believe that there is an ongoing campaign targeting rust-lang members and owners of popular crates that is attempting to compromise devices and accounts in order to use them to publish malware. A video call is set up for something positive — maybe for a job, maybe for a project, maybe for a contract opportunity — and then that's used as a vector to either get the target to install something on their computer (such as a purportedly missing audio codec) or execute another command (for example, via putting a command on the clipboard). Last month this trick was used in a successful supply chain attack against the array ref crate , among others. Any piece of software that depends on open source (which is almost every piece of software) has a network of human beings who are potential attack vectors - everyone with publishing rights to any of the packages in the dependency ne
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: Teleport — See what 13 engineers learned from “pressure washing” their codebase using LLMs for 90 days. Hint: Quality > quantity for finding security vulnerabilities. 17th September 2026 - Link Blog Be alert: targeted attacks on prominent Rustaceans . Important warning from Adam Harvey and the crates security team: We believe that there is an ongoing campaign targeting rust-lang members and owners of popular crates that is attempting to compromise devices and accounts in order to use them to publish malware. A video call is set up for something positive — maybe for a job, maybe for a project, maybe for a contract opportunity — and then that's used as a vector to either get the target to install something on their computer (such as a purportedly missing audio codec) or execute another command (for example, via putting a command on the clipboard). Last month this trick was used in a successful supply chain attack against the array ref crate , among others. Any piece of software that depends on open source (which is almost every piece of software) has a network of human beings who are potential attack vectors - everyone with publishing rights to any of the packages in the dependency network for that software. I guess our best defense right now is dependency cooldowns - giving new package releases a few days before upgrading to them, in the hope that supply chain attacks like this will be spotted by someone else. Posted 17th September 2026 at 11:59 pm Recent articles Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war - 22nd September 2026 Jev introduces a new shape of LLM - System One, aka Decision Models - 21st September 2026 Generating running routes with GPT-6 Astra and ChatGPT Work - 12th September 2026 This is a link post by Simon Willison, posted on 17th September 2026 . open-source 321 security 638 rust 114 supply-chain 22 dependency-cooldowns 5 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Be alert: targeted attacks on prominent Rustaceans
  - Published: 2026-09-17T23:59:19+00:00
  - Link: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
  - Summary: Be alert: targeted attacks on prominent Rustaceans Important warning from Adam Harvey and the crates security team: We believe that there is an ongoing campaign targeting rust-lang members and owners of popular crates that is attempting to compromise devices and accounts in order to use them to publish malware. A video call is set up for something positive — maybe for a job, maybe for a project, maybe for a contract opportunity — and then that's used as a vector to either get the target to install something on their computer (such as a purportedly missing audio codec) or execute another command (for example, via putting a command on the clipboard). Last month this trick was used in a successful supply chain attack against the array ref crate , among others. Any piece of software that depends on open source (which is almost every piece of software) has a network of human beings who are potential attack vectors - everyone with publishing rights to any of the packages in the dependency ne

### Cluster b9771fe2d2 — score 11

- Title: Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
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
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/defense-industrial-base-nation-state-network-telemetry
  - Summary: Discover how nation-states target the Defense Industrial Base via pre-positioning. Learn why network telemetry is crucial to detect these hidden cyber threats.

### Cluster 7bab174bc9 — score 11

- Title: Tracking CyberStrikeAI Usage
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
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
Will Thomas 5 min read March 2, 2026 Tracking CyberStrikeAI Usage Team Cymru is continuously monitoring our global netflow visibility to uncover patterns of adversary activity, identify malicious operations, and gain actionable intelligence. In this post, we are diving into CyberStrikeAI, an open-source artificial intelligence (AI) offensive security tool (OST) developed by a China-based developer who we assess has some ties to the Chinese government. What is CyberStrikeAI? In its own words from the GitHub repository (see here ), ‚ÄúCyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.‚Äù CyberStrikeAI comes with its own dashboard that helps users quickly understand the platform's core features and current state, as shown in Figure 1 below. Figure 1: CyberStrikeAI Dashboard from GitHub CyberStrikeAI was first brought to our attention following the Amazon CTI team‚Äôs blog about AI-augmented threat actor infrastructure they had discovered. Amazon shared this related IP 212.11.64[.]250. Analysis of that IP address in Team Cymru Scout‚Äôs open port scan data revealed that it had this ‚ÄúCyberStrikeAI‚Äù banner running on this service, as shown in Figure 2 below. Figure 2: The CyberStrikeAI port banner in Team Cymru Scout. Identifying Targeting with NetFlow Using Team Cymru Scout, we can find NetFlow communications between the IP shared by Amazon and its targets, such as the Fortinet FortiGate devices it was observed targeting, as shown in Figure 3 below. Figure 3. IP address running CyberStrikeAI targeting a Fortinet FortiGate device. Researching Ed1s0nZ While researching the GitHub profile (see here ) of CyberStrikeAI‚Äôs developer, ‚ÄúEd1s0nZ‚Äù, several attributes about the individual caught our attention. Firstly, Ed1s0nZ‚Äôs other GitHub repositories suggest interest in exploitation activity: watermark-tool: A secure and efficient invisible document watermarking solution that can add completely invisible digital watermarks to various documents, while supporting watermark extraction and verification. Developed in Go, it supports both web and CLI usage. The watermark uses steganography technology to ensure that the watermark is completely invisible and does not affect the reading experience and visual effects of the original document. PrivHunterAI: This tool uses a passive proxy approach and mainstream AI (such as Kimi, DeepSeek, GPT, etc.) to detect privilege escalation vulnerabilities. Its core detection function is built on the open APIs of the relevant AI engines and supports data transmission and interaction via HTTPS protocol. InfiltrateX: A useful privilege escalation scanning tool. While automated detection of privilege escalation vulnerabilities is difficult, prone to occur, and poses serious risks, it can still strive to automate the detection of some such vulnerabilities. Further, Ed1s0nZ‚Äôs GitHub activities indicate they interact with organisations that support potentially Chinese government state-sponsored cyber operations. This includes Chinese private sector firms that have known ties to the Chinese Ministry of State Security (MSS). A number of GitHub activities potentially link Ed1s0nZ to the Chinese state-sponsored cyber operations. On 19 December 2025, Ed1s0nZ posted CyberStrikeAI to Knownsec 404‚Äôs Starlink Project, as shown in Figure 4 below. Based on published reporting by DomainTools and others, Knownsec does work for the MSS and the Chinese People‚Äôs Liberation Army (PLA). Figure 4. Ed1s0nZ‚Äôs post sharing CyberStrikeAI to Knownsec 404‚Äôs Starlink Project. Further, on 5 January 2026, Ed1s0nZ added to their GitHub profile ‚ÄúCNNVDÔºàÂõΩÂÆ∂‰ø°ÊÅØÂÆâÂÖ®ÊºèÊ¥ûÔºâ 2024 Âπ¥Â∫¶ÊºèÊ¥ûÂ•ñÂä±ËÆ°Âàí ¬∑ ‰∫åÁ∫ßË¥°ÁåÆÂ•ñÔºà‰∏™‰∫∫). Translation: CNNVD (Chinese National Vulnerab
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Tracking CyberStrikeAI Usage
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/tracking-cyberstrikeai-usage
  - Summary: Discover how CyberStrikeAI is revolutionizing AI-augmented offensive security. Explore its ties to Chinese state-sponsored actors and learn to detect it with NetFlow.

### Cluster f7ce25a96b — score 11

- Title: Protecting Critical National Infrastructure (CNI) through extended global visibility
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
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
4 min read February 17, 2026 Protecting Critical National Infrastructure (CNI) through extended global visibility Team Cymru offers a range of capabilities specifically tailored to protect Industrial Control Systems (ICS) and Operational Technology (OT), which over the years have been increasingly targeted by hostile nation-state threat actors as well as lesser skilled ‚Äúhacktivist‚Äù groups. Unlike standard IT environments, OT systems often utilize legacy protocols and have long equipment lifecycles, making proactive external visibility essential. By focusing on the networking stages of the ICS version of the MITRE ATT&CK framework using Team Cymru‚Äôs visibility, specifically Reconnaissance and Command and Control, OT defenders can identify scanning and exploitation attempts against exposed infrastructure and track malicious infrastructure before attackers can establish persistence. Cybersecurity industry experts continue to warn that critical national infrastructure (CNI) sector organizations need to enhance their visibility into their own remote facilities and technical OT system. "Utilities need to treat external exposure and asset blind spots as intelligence problems, not just configuration issues. Energy-sector OT environments are becoming increasingly exposed as legacy systems connect to modern networks without corresponding gains in visibility or monitoring. What stands out in these findings is how quickly serious risks emerge once traffic is observed, suggesting attackers are likely identifying the same weaknesses just as fast. Closing these gaps requires continuous visibility into OT communications and the context to understand what ‚Äònormal‚Äô behavior actually looks like.‚Äù - Will Baxter, Field CISO at Team Cymru. "The recent Poland attacks confirmed that the adversary doesn't just teleport to the perimeter; they 'commute' via Operational Relay Boxes (ORBs) to pre-position themselves months in advance. Tracking this external infrastructure allows defenders to spot the threat left of boom, burning the adversary's bridge before they can cross it to deliver kinetic effects. To survive a sophisticated campaign, we cannot operate with blind spots; we need external telemetry to track the adversary's intent and internal deep-packet inspection to catch their specific 'living off the land' tactics. External visibility tells you who is knocking at the gate, while internal visibility is the only way to see what physical process they are attempting to disrupt once inside and capturing transient data for root cause analysis afterwards." - Mark (Magpie) Graham of Dragos Inc. Evolutions of the ICS and OT Threat Landscape in 2025 To help track the evolution of ICS/OT threats, Team Cymru researchers supported the development of the Cyber Incident Tracker for Electric Power Systems (CITEPS), a project created by Prof. Dr. Luiz F. Freitas-Gutierres. The evolution of ICT/OT threats can be marked by two main eras. The first era involves adversaries experimenting with these sophisticated digital weapons. The second era can be marked by an increasing usage and adoption of these capabilities by adversaries, often attributed to nation-state intelligence services. 2010‚Äì2019: The Era of Experimentation This period marked the introduction of specialized digital weapons targeting ICS, leading to a mix of espionage and destructive attacks. This includes the deployment of Stuxnet in 2010, which is noted as the world‚Äôs first publicly known digital weapon against ICS, physically destroying centrifuges at the Natanz nuclear facility in Iran. Subsequent malware became more specialized, such as Industroyer which was used in the 2016 Ukraine power grid attack to disrupt electricity, a critical event that signaled a shift toward direct grid manipulation. The ceiling was raised further in 2017 with Triton malware, which specifically targeted safety instrumented systems at a Saudi Arabian petrochemical plant, threatening physical safety mechanism
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Protecting Critical National Infrastructure (CNI) through extended global visibility
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/protecting-critical-national-infrastructure-orb-networks
  - Summary: Adversaries are pre-positioning for destructive attacks on CNI. Learn how to track nation-state threat actors and ORB networks to harden the OT boundary "left of boom."

### Cluster ffad5d9316 — score 11

- Title: Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
- Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-prevent-data-breaches
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, supply_chain
- affected_industries: retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, data_breach
- affected_industries: retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Summary

```
Uncover the power of threat intelligence for a technology company. Learn how to prevent data breaches and maximize ROI as a CISO with expert guidance.
```

#### Full body

```
tcblogposts 4 min read March 15, 2023 Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches Threat Reconnaissance that Saves your Butt and the Budget Threat hunting and reconnaissance often seems like another hard to explain cybersecurity budget item, especially when talking to business counterparts. As a CISO, you know that having an elite team of threat hunters focused on your external attack surface saves the company from a compromise or attack. External threat hunters have the visibility to monitor threat actor infrastructure, see how it evolves, and shut down any communication going to hackers. You know how important this capability is to safeguard the organization, but how about the rest of the company? Spoiler alert: over the next five parts of this series, we‚Äôre going to explain in simple terms how an elite group of threat hunters using Pure Signal Recon were able to effect a total $9m in savings. This threat hunting team supported cybersecurity needs for key business initiatives and helped their company realize a three year risk reduction savings of $9m. Half of the $9m in savings can be attributed to avoiding a data breach in the first place, so let‚Äôs start our discussion with the biggest area of cost savings and risk reduction. We‚Äôll start where the largest savings were found, with $4.5m of the $9m being attributed to data breach avoidance. Data Breaches - Proactive Approach for Payback As a real world example we are going to examine the hard dollars that a large multinational retailer saved with their investment in Pure Signal Recon to empower their analysts with unmatched threat hunting and reconnaissance capabilities. This is a company with a mature cybersecurity team that provides cybersecurity defenses to protect a 1m+ workforce, a global corporate organization with an extensive supply chain and ongoing M&A activity. This write up is based on the original Forrester Total Economic Impact‚Ñ¢ (TEI) study, an independently held private collaboration between our client and them. The goals were to determine the cost savings gains that could be achieved by using external threat reconnaissance to support a proactive cybersecurity organization to safeguard company reputation, share value, and careers, from cyber risks. Defining the ROI of Threat Reconnaissance - What Matters Most With access to the proper tools, threat hunting empowers analysts to act on threats to your organization in real time, instead of the usual reactive responses that drain resources and budget. It opens up a new range of preemptive capabilities that can turn your threat analysts into a powerful layer of proactive cyber defense.It has When justifying budgets and helping the business understand the importance of your threat hunting function consider where it has direct impact on business outcomes: Stop a data breach from happening with a predictive response to persistent threat actors Reduce the amount of tools needed and lower the swivel chair security tax on your analysts Detect impending data breaches via your supply chain and other 3rd parties Address the business risk of new company acquisitions via M&A Remove tedious analyst work with automation so they could focus on strategic cybersecurity initiatives Predictive Response Pays Off First we will focus on the most obvious area where improved threat intelligence pays off; preventing data breaches from happening in the first place . In this real world scenario, we are profiling a sophisticated cybersecurity team that could already show that they were able to reduce the standard cost of a data breach by more than 75%. As a retail conglomerate and global brand, they are highly targeted and sought after ‚Äúprize‚Äù with threat actors. They wanted to close the gap by another 40% reduction in projected costs due to a data breach. The team had the skills and experience to further close the gap on corporate risk and cost by transitioning from providing reactive cybersecurity to a more pro
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-prevent-data-breaches
  - Summary: Uncover the power of threat intelligence for a technology company. Learn how to prevent data breaches and maximize ROI as a CISO with expert guidance.

### Cluster 38ff3233e6 — score 11

- Title: High Vulnerability in OpenSSL 3.0
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
- Link: https://www.team-cymru.com/post/high-vulnerability-in-openssl-3-0
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- cve_ids: CVE-2022-3602, CVE-2022-3786
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ddos
- cve_ids: CVE-2022-3602, CVE-2022-3786
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Stay informed about the high vulnerability in OpenSSL 3.0 with our latest blog post. Understand the impact on security and protect your technology company.
```

#### Full body

```
tcblogposts 3 min read November 2, 2022 High Vulnerability in OpenSSL 3.0 How Team Cymru products help you discover and manage the impact and risk On November 1st, 2022, version 3.0.7 of OpenSSL was released to patch a high vulnerability, at the time of writing it was as yet undisclosed . Vulnerability Description Published as X.509 Email Address 4-byte Buffer Overflow with accompanying CVE-2022-3602 and CVE-2022-3786, this vulnerability allows an attacker to craft a malicious email address in a certificate to overflow an arbitrary number of bytes containing the `.' character (decimal 46) on the stack. Vulnerability Impact The specific CVE-2022-3602 vulnerability, if exploited, could result in a crash (causing a denial of service) and/or remote code execution. What is being advised? Upgrading to OpenSSL 3.0.7 as soon as possible is being advised for users of OpenSSL 3.0.0 - 3.0.6. How to assess risk using Team Cymru products Team Cymru has two products that enable organisations to assess and quantify this vulnerability, and measure risk to both their own, and third parties. Starting with Pure Signal Orbit, our Attack Surface Management platform. With a combination of Asset Management, Vulnerability Management, Business Risks and Threat Intelligence , it is the most fully featured product on the market that finds assets, reveals vulnerabilities and alerts to threats at unmatched speed and scale. This puts you at a distinct advantage when facing celebrity vulnerabilities and reacting to alerts of high or critical patches. Assessing the Attack Surface & External Digital Assets for OpenSSL 3.x Vulnerabilities How to use Pure Signal Orbit to find impact assets and quantify impact of the Open SSL 3.0.7. After logging in, go to Vulnerability Management, then follow these two alternative steps: From the Pure Signal Orbit Dashboard Move your cursor to the bottom right of the dashboard as shown below, and click on the box that highlights OpenSSL Less Than 3.0.7 Critical Vulnerability. Figure 1 - where to find the Vulnerability alerts in the Orbit dashboard ‚Äç You will see this box in the lower right corner of the Pure Signal Orbit Dashboard. Figure 2 - the OpenSSL v3.0 Vulnerability alert in the Orbit dashboard ‚Äç You will then see a list of impacted assets, where you can click through as see specifics such as Environment, Business Risk score, any other Vulnerabilities that may be present, in addition to our helpful response guides. From the Vulnerability Management view Log in to your Pure Signal Orbit dashboard and select ‚ÄòVulnerabilities‚Äô, and then select ‚ÄòVulnerability Types‚Äô shown below. In the search box shown below, type the following: ‚ÄúOpenSSL‚Äù or ‚ÄúCVE-2022-3786‚Äù or ‚ÄúCVE-2022-3602‚Äù (not currently live in this view yet) Figure 3 - where to find the the search tool within the Orbit dashboard You will now be presented with the list of assets impacted by Open SSL Critical Vulnerability, and can take action in order of priority using our integrated Total Asset Risk score that combines CVE weightings in addition to Business Risk scores. Threat Reconnaissance technique for assessing potential OpenSSL risk from vulnerable third parties Pure Signal Recon is our analysts portal into the world‚Äôs largest data ocean designed specifically for Threat Intelligence. By ingesting over 200bn daily internet connections, Pure Signal data is unmatched in size and scale to gain visibility into third party risks, and very effective at making discoveries when vulnerabilities are announced.. How to use Pure Signal Recon to find impact assets and quantify impact of the Open SSL 3.0.7. After logging in, run a Query, include the following: Specify your timeframe - i.e. previous 7 days Specify the IP addresses or ranges of IP‚Äôs of interest There are 2 primary data sets that will contain this information - ‚ÄúOpen Ports‚Äù and ‚ÄúNMAP Open Ports‚Äù Use the post query filters and search for ‚ÄúOpenSSL/3‚Äù to identify any vulnerable v
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: High Vulnerability in OpenSSL 3.0
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/high-vulnerability-in-openssl-3-0
  - Summary: Stay informed about the high vulnerability in OpenSSL 3.0 with our latest blog post. Understand the impact on security and protect your technology company.

### Cluster 33b6cffcbd — score 10

- Title: Inside the Modern SOC: Defending the Cross-Environment Pivot
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-17T22:00:33+00:00
- Link: https://unit42.paloaltonetworks.com/soc-cross-environment-pivot/
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
Cross-environment attacks demand a new approach to security operations. Learn how Unit 42 Managed XSIAM helps SOC teams investigate complete attack paths. The post Inside the Modern SOC: Defending the Cross-Environment Pivot appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights Inside the Modern SOC Inside the Modern SOC Inside the Modern SOC: Defending the Cross-Environment Pivot 3 min read Related Products Cortex Cortex XSIAM Managed Threat Hunting Unit 42 Managed Detection and Response Unit 42 Managed XSIAM By: Sharon Maydar Published: September 17, 2026 Categories: Inside the Modern SOC Insights Tags: AI Attack surface Unit 42 Incident Response Report Share The Cross-Environment Gap Our series, Inside the Modern SOC: Trends and Insights from Unit 42 Managed Services , shares the operational patterns that Unit 42 experts observe, with today's challenge beginning after the initial foothold. Across Unit 42 investigations, we continue to see adversaries move well beyond where an attack begins. They pivot across the enterprise, avoiding detection by exploiting the visibility gaps created by disconnected security tools. According to the 2026 Unit 42 Global Incident Response Report , 43% of attacks involved activity across four or more attack surfaces, with some cases spanning as many as eight. As attacks move across cloud, endpoint, network, identity and software-as-a-service (SaaS) environments, analysts must connect activity across security domains before the complete attack path becomes clear. Following the Attack Across Environments The First Signal An investigation may begin with what appears to be an isolated event. An endpoint generates an alert. A cloud administrator provisions a resource outside of normal activity. An unfamiliar application requests elevated permissions. On its own, none of these events necessarily signals a broader attack. The Cross-Environment Pivot As the attack progresses, related activity begins appearing elsewhere. Permissions may change within a SaaS application. Cloud resources may be provisioned or reconfigured. Sensitive data may be staged for exfiltration. New network connections may emerge between systems that rarely communicate. When these signals are investigated separately, security teams can miss the connection between them and the larger attack taking shape across the environment. Reconstructing the Attack Path The complete picture often becomes clear only when activity across security domains is connected. AI-driven correlation connects signals that initially appear unrelated, helping analysts reconstruct how an adversary gained access, where they moved, what they accessed and what they were attempting to accomplish. Because attackers don't operate within the boundaries monitored by individual security tools, security operations can't either. Defenders need to follow attacker activity across the enterprise and investigate the intrusion as one connected attack. Doing this consistently requires continuous monitoring and response, along with ongoing optimization of detections, correlation rules and workflows as threats and environments evolve. How SOC Leaders Can Defend Across Attack Surfaces Use AI to Investigate the Attack, Not the Alert As attackers move across security domains, security leaders should evaluate whether their operations can reconstruct a complete attack path rather than respond to isolated alerts. The goal is to use AI-driven correlation to reveal how seemingly unrelated activity connects before an adversary reaches their objective. Connect Evidence Across the Attack Path To track adversarial behavior from the first signal across every stage of the attack lifecycle, organizations must connect evidence across their security environment through lateral movement, persistence and impact. True visibility requires cross-domain correlation, while threat hunting should test for attacker behaviors that may not yet have generated an alert. SOC leaders should ensure their platforms automatically correlate activity into unified incident storylines, giving analysts the context to investigate and respond without manually pivoting between tools or teams. Continuously Test and Evolve Security Operations Treat every investigatio
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Inside the Modern SOC: Defending the Cross-Environment Pivot
  - Published: 2026-09-17T22:00:33+00:00
  - Link: https://unit42.paloaltonetworks.com/soc-cross-environment-pivot/
  - Summary: Cross-environment attacks demand a new approach to security operations. Learn how Unit 42 Managed XSIAM helps SOC teams investigate complete attack paths. The post Inside the Modern SOC: Defending the Cross-Environment Pivot appeared first on Unit 42 .

### Cluster 61da9d90b7 — score 10

- Title: Unmasking EvilTokens: Getting to the root of device code phishing
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-22T15:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass, phishing_social_eng
- affected_industries: education, financial_services, healthcare
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, mfa_bypass
- affected_industries: healthcare, financial_services, education
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
EvilTokens has quickly become one of the top PhaaS platforms, enabling device code phishing attacks through AI-assisted lures, automated infrastructure, and token theft. In collaboration with partners, Microsoft Digital Crimes Unit (DCU) facilitated a disruption of EvilTokens infrastructure and operations. The post Unmasking EvilTokens: Getting to the root of device code phishing appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Adversary-in-the-middle (AiTM) Phishing Threats intelligence Business email compromise Cyberattacker techniques, tools, and infrastructure Cybercrime Social engineering and phishing Threat actors Content types Research Products and services Microsoft Defender Microsoft Defender Experts Microsoft Defender Experts MDR Microsoft Defender for Endpoint Topics Actionable threat insights Threat intelligence Following its emergence in February 2026, EvilTokens quickly became one of the most widely used phishing-as-a-service (PhaaS) platforms, providing cybercriminals with AI capabilities for tailoring phishing lures and analyzing compromised inboxes to identify high-value targets. This AI-powered cybercrime platform facilitated sophisticated business email compromise (BEC) campaigns that compromised more than 12,000 inboxes in over 10,000 organizations worldwide. EvilTokens enabled threat actors to abuse the device code authentication flow, steal tokens, and compromise organizational accounts at scale using an AI-driven infrastructure and automating multiple parts of the attack chain. The toolkit offered a plethora of prebuilt phishing templates and landing pages with an AI-powered assistant to aid in structuring target-specific emails. Stolen tokens are used for email exfiltration and persistence, often through the creation of malicious inbox rules that conceal communications. In some cases, tokens can also be used to grant new devices access to a victim’s inbox, a particularly durable method to maintain persistence. Microsoft Threat Intelligence tracks the threat actor behind the development and support of the EvilTokens phish kit as Storm-2992. Post-compromise, EvilTokens enabled threat actors to utilize AI assistants to sift through victim mailbox activity and engineer a phishing message based on the accessible email content. EvilTokens also allowed threat actors to conduct Microsoft Graph reconnaissance to map organizational structure and permissions, enabling continued access and potential lateral movement while tokens remain valid. While token-targeting phishing is not new, it has become far more common and industrialized over the last several years as organizations adopted multifactor authentication (MFA). To evade detection, EvilTokens uses a multi-stage delivery pipeline designed to bypass traditional email gateways and endpoint security. Targets are lured through deceptive emails that use 44 different themes, including invoices and request for proposals (RFPs), or shared files. These emails contained malicious URLs, PDF attachments, and HTML files. Campaigns leveraging EvilTokens have impacted organizations in various industries, including wholesale distribution, construction, financial services, real estate, higher education, and healthcare, with the highest concentrations of observed victim activity in the United States, Canada, the United Kingdom, Australia, India, and France. Working with partners, Microsoft’s Digital Crimes Unit (DCU) facilitated a coordinated disruption of infrastructure used to operate the EvilTokens service . This blog provides a comprehensive, up-to-date analysis of the EvilTokens platform and operations. We share specific examples of the EvilTokens service panel and a detailed analysis of EvilTokens infrastructure. Defending against EvilTokens and similar adversary-in-the-middle (AiTM) phishing threats requires a layered approach that blends technical controls with user awareness. This blog also provides Microsoft Defender detection and hunting guidance, as well as resources on how to set up mail flow rules, enforce spoof protections, and configure third-party connectors to prevent spoofed phishing messages from reaching user inboxes. What is device code phishing? One of the primary capabilities of EvilTokens is its device code phishing flow, which abuses device code authentication , a legitimate OAuth flow designed for devices with limited interfaces, such as
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Unmasking EvilTokens: Getting to the root of device code phishing
  - Published: 2026-09-22T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/
  - Summary: EvilTokens has quickly become one of the top PhaaS platforms, enabling device code phishing attacks through AI-assisted lures, automated infrastructure, and token theft. In collaboration with partners, Microsoft Digital Crimes Unit (DCU) facilitated a disruption of EvilTokens infrastructure and operations. The post Unmasking EvilTokens: Getting to the root of device code phishing appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Unmasking EvilTokens: Getting to the root of device code phishing
  - Published: 2026-09-22T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/
  - Summary: EvilTokens has quickly become one of the top PhaaS platforms, enabling device code phishing attacks through AI-assisted lures, automated infrastructure, and token theft. In collaboration with partners, Microsoft Digital Crimes Unit (DCU) facilitated a disruption of EvilTokens infrastructure and operations. The post Unmasking EvilTokens: Getting to the root of device code phishing appeared first on Microsoft Security Blog .

### Cluster 250fac7429 — score 10

- Title: Don’t Call Us, We’ll Call Your APIs | TraderTraitor Backdoors Resurface on Victim With No Crypto Ties
- Source: SentinelOne Labs (threat_research_primary)
- Published: 2026-09-18T17:00:16+00:00
- Link: https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ddos, phishing_social_eng
- actor_attribution: Lazarus, UNC4899
- affected_industries: financial_services, retail_ecommerce
- affected_products: AWS, Apple iOS/macOS, GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, ddos, apt_espionage
- actor_attribution: Lazarus, UNC4899
- affected_industries: financial_services, retail_ecommerce
- affected_products: Apple iOS/macOS, GitHub, AWS
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
North Korean operators built a foothold on a DevOps engineer's Mac in a campaign whose job interview lures deliver malware via Terraform lock files.
```

#### Full body

```
LABScon Don’t Call Us, We’ll Call Your APIs | TraderTraitor Backdoors Resurface on Victim With No Crypto Ties Albert Priego , Alex Delamotte & Matej Havranek / September 18, 2026 Executive Summary Following disclosure of the TraderTraitor attack against LayerZero Labs in April 2026, SentinelOne identified an additional victim with the same macOS backdoors. Our analysis explores the mechanics of these backdoors and the expanded targeting against a victim in the IT services sector with no relationship to cryptocurrency trading. We also identified more weaponized GitHub repositories from the social engineering schemes used to target job seekers in these campaigns. This report expands on how Terraform lock files enable the delivery of malware from custom Terraform provider registries controlled by the attackers. Overview Throughout 2026, the financially motivated DPRK state-sponsored Lazarus subgroup TraderTraitor ( aka UNC4899, PUKCHONG, Jade Sleet) has engaged in campaigns targeting entities involved in cryptocurrency trading, including a high-profile attack disclosed in April where USD 292 million was stolen from KelpDAO through a compromise of LayerZero . KelpDAO is a decentralized finance (DeFi) protocol that supports restaking Ethereum; LayerZero Labs provides services with the capability to exchange cryptocurrency across different blockchain platforms. TraderTraitor compromised LayerZero Labs and determined methods to create a fake cryptocurrency minting event, which the attacker combined with a DDoS against validation servers so that compromised servers would approve an illegitimate mint event, leading to the massive theft. Following the public disclosure of this breach, SentinelOne identified an additional victim infected with the macOS backdoors, FLATROOF ( aka macOS.Gaslight ) and ROOFDECK , which were first observed in the LayerZero Labs attack. Unlike the previous high-profile victim, this target was a much smaller organization in the IT services industry. Our investigation revealed insights into what happens when this threat actor compromises a smaller organization that we believe ultimately yielded insufficient value to sustain the intrusion. Weaponized Terraform Coding Projects Each campaign related to this wave of activity uses social engineering via fake job interview lures, a traditional Contagious Interview approach common among DPRK actors. The attacker makes contact with job seekers from the company that is ultimately compromised; the GitHub profile of each targeted job seeker we identified falls into DevOps or cryptocurrency/FinTech engineering projects. The GitHub repository themes for coding project lures are designed as infrastructure engineering projects related to the company that the DPRK actors are posing as. By pivoting from the gtn-candidate-repo repository shared by LayerZero Labs in their incident report , we identified additional lures, which included references to the companies Northwind and Novacart. It is unclear if these were fabricated companies used by the threat actor, or if they were posing as hiring teams from real companies with these names; one Northwind example describes it as an ecommerce company launching in the near future. Other repository names that we identified include: Northwind-IAC novacart-interview terraform-candidate-repo Interview task from a GitHub repository containing a weaponized .terraform.lock.hcl file The repositories contain a weaponized .terraform.lock.hcl file in the coding project with a custom provider that points to a domain controlled by the attacker. We identified three malicious provider domains across multiple repositories: registry.hashicorp-aws[.]com registry.hashicorp-aws[.]io registry.hashicorp-terraform[.]io When the victim runs terraform init with the weaponized lockfile in place, Terraform treats the custom provider as the source of truth, resulting in Terraform downloading and executing the malicious provider modules. Developer awareness can lead
```

#### Corroborating sources (1)

- **SentinelOne Labs** (threat_research_primary)
  - Title: Don’t Call Us, We’ll Call Your APIs | TraderTraitor Backdoors Resurface on Victim With No Crypto Ties
  - Published: 2026-09-18T17:00:16+00:00
  - Link: https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/
  - Summary: North Korean operators built a foothold on a DevOps engineer's Mac in a campaign whose job interview lures deliver malware via Terraform lock files.

### Cluster bb1f94f216 — score 10

- Title: Introducing CAIRN: Frontier tracking for AI-integrated malware
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-22T10:00:25+00:00
- Link: https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware/
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
Talos is releasing CAIRN, a research toolkit for hunting, classifying, and tracking emerging AI-integrated malware.
```

#### Full body

```
Introducing CAIRN: Frontier tracking for AI-integrated malware By Ryan Fetterman Tuesday, September 22, 2026 06:00 Tool Talk AI A cairn is a marker left behind on a trail, a deliberately placed stack of stones that helps hikers find their way when the path is unclear. Attackers building AI-integrated malware unintentionally (and inevitably) leave behind markers of their own: prompt templates, provider endpoints, API keys, jailbreak terms, and other artifacts embedded throughout their tooling. When we consider these strings as cognitive artifacts , or vestiges left behind from AI integration, we can enable a new, metadata-first hunting methodology for AI-integrated malware that is fast and scalable. These artifacts can be extracted, related, and classified without ever touching the underlying binary. Today, Cisco Talos is releasing this methodology in the form of CAIRN (Cognitive Artifact Intelligence Research Network), a research toolkit for hunting, classifying, and tracking emerging AI-integrated malware. Over time, we will share the full contents of our initial findings, starting today with CLOSEDQUORUM . Figure 1. CAIRN explorer connects malware binaries by metadata attributes like submitter, import hash, domain or AI provider. Run cairn explorer to launch the graph. CAIRN contains functionality for identifying AI-integrated malware; in our definition, that is malware that functionally operationalizes, explicitly targets, or exploits AI systems and their ecosystems — spanning functional integration into attack chains, credential and infrastructure compromise, and ecosystem-level abuse. These binaries are classified based on pre-defined AI-usage archetypes, and reporting findings in a structured way. CAIRN has an explorer layer, which creates a structured graph of cognitive artifact relationships to help defenders identify related malware families, infrastructure, and threat actors. Figure 2. The CAIRN processing pipeline extracts AI-integration artifacts from metadata, classifies and constructs unique representations for all samples, and clusters and graphs the sample relationships. Metadata-first architecture CAIRN operates entirely from metadata — no binary downloads or execution required. It combines rule-based detection, semantic clustering, and relationship graph traversal to identify AI-integrated malware through cognitive artifacts such as embedded prompts, provider endpoints, orchestration logic, API key prefixes, and AI-analysis evasion strings. CAIRN discovers candidate samples through up to 24 acquisition filters, each targeting a different type of AI-related artifact. Instead of relying solely on filenames or hashes, these filters search across metadata including extracted strings, sandbox behavior, and antivirus (AV) detection labels. provider-api-integration searches for LLM provider endpoint strings in file metadata. For example: api.openai.com api.anthropic.com api.deepseek.com Generativelanguage.googleapis.com Any file whose binary content, URL extraction, or sandbox behavior surfaces one of these domains becomes a candidate. python-ai-scripts targets Python files matching AI framework import patterns. For example: langchain litellm openai This pulls in scripts that interact with the AI ecosystem at the code level, not just the network level. ai-analysis-evasion searches for text strings explicitly addressed to AI analysis systems — the kind of comment an actor might embed when trying to tell an LLM sandbox "there's nothing to see here." local-llm-runtime searches for strings indicating local model inference ( ollama , llama.cpp , vllm , gguf , safetensors ). This surfaces files that may be running inference on the endpoint rather than calling a hosted API. agentic-tooling looks for tool-call syntax ( tool_call , tool_calls , function_call ) co-occurring with offensive capability terms. Results from the acquisition filters are stored in a SQLite corpus with YARA run automatically on import, using a three-l
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Introducing CAIRN: Frontier tracking for AI-integrated malware
  - Published: 2026-09-22T10:00:25+00:00
  - Link: https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware/
  - Summary: Talos is releasing CAIRN, a research toolkit for hunting, classifying, and tracking emerging AI-integrated malware.

### Cluster b14566fc43 — score 10

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

### Cluster bf92f99cb9 — score 10

- Title: 21st September – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-09-21T23:13:07+00:00
- Link: https://research.checkpoint.com/2026/21st-september-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- affected_industries: financial_services, government
- cve_ids: CVE-2026-76460, CVE-2026-76461, CVE-2026-91843
- urgency_signals: critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- affected_industries: financial_services, government
- cve_ids: CVE-2026-91843, CVE-2026-76460, CVE-2026-76461
- urgency_signals: preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 21st Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Japan’s Digital Agency, which operates the Government Solution Service used by multiple ministries, has confirmed a data breach after attackers exploited a vulnerability in a VPN appliance. Approximately 246,000 records were exposed, […] The post 21st September – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 21st September – Threat Intelligence Report September 22, 2026 https://research.checkpoint.com/2026/21st-september-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 21st Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Japan’s Digital Agency, which operates the Government Solution Service used by multiple ministries, has confirmed a data breach after attackers exploited a vulnerability in a VPN appliance. Approximately 246,000 records were exposed, including names and contact details belonging to government officials and contractors, while financial information was not affected. Two oil tankers bound for Texas were hit by cyberattacks that disrupted onboard systems during voyages to the United States. US Coast Guard and FBI personnel boarded the vessels, while officials confirmed malicious cyber activity on the VL Prosperity but have not publicly attributed the attacks to a specific actor. Brevo, a French customer communication and marketing platform, has confirmed a supply chain attack after attackers used a compromised Cloudflare API key to inject malicious ClickFix scripts into websites that use Brevo components. The attack affected about 100,000 websites. Japanese software company Helpfeel, operator of image-sharing service Gyazo, has reported a data breach after attackers exploited a vulnerability in an image upload server. Above 23 million user records and 490 million image metadata records were exposed, including email addresses, password hashes, session IDs, integration tokens, and location metadata. AI THREATS Check Point Research has analyzed the July-August AI threat landscape, highlighting the latest cases when AI models broke out of their evaluation environments. On the attackers’ side, AI is increasingly used as an operational tool, while the AI systems themselves are also targeted. The report highlights AI-assisted ransomware intrusions, criminal markets for stolen model access, and vulnerabilities in coding agents and enterprise copilots. Researchers uncovered Luciferus, an uncensored AI service advertised on an underground forum for malware creation and other prohibited activities. Testing showed that the service could generate code for a simple remote access trojan, while its operator markets several paid tiers to users seeking unrestricted AI assistance. Researchers unveiled BragJack, an attack that allows malicious browser extensions to hijack AI assistants by forcing prompts through trusted browser channels. The technique affected several AI-enabled browsers and assistants, enabling actions such as file access, screenshots, microphone and camera use, and logged-in activity before vendors issued security fixes. VULNERABILITIES AND PATCHES Check Point has released a fix for CVE-2026-91843, a critical vulnerability affecting Security Management and Log Servers. The flaw, rated CVSS 9.8, stems from a stack overflow in the login process and can allow unauthenticated remote attackers to execute code as root on affected R80 through R82 systems. Cisco has addressed CVE-2026-76460 & CVE-2026-76461 , two critical vulnerabilities affecting Cisco ISE and Secure Email Gateway with CVSS scores of 10.0 and 9.8. According to Cisco, the company is aware of active exploitation of CVE-2026-76460, which allows an unauthenticated remote attacker to gain access to the system’s management interface. Oracle has released its September 2026 Critical Security Patch Update, addressing more than 800 vulnerabilities across 17 product families. More than 100 flaws are rated critical, while over 240 can be exploited remotely without authentication. Affected products include E-Business Suite, Fusion Middleware, Hyperion, Siebel CRM, Analytics, Communications, and Virtualization. ISC has published security updates for BIND 9 addressing 14 vulnerabilities, including seven high-severity flaws that
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 21st September – Threat Intelligence Report
  - Published: 2026-09-21T23:13:07+00:00
  - Link: https://research.checkpoint.com/2026/21st-september-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 21st Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Japan’s Digital Agency, which operates the Government Solution Service used by multiple ministries, has confirmed a data breach after attackers exploited a vulnerability in a VPN appliance. Approximately 246,000 records were exposed, […] The post 21st September – Threat Intelligence Report appeared first on Check Point Research .

### Cluster 8845f71e12 — score 10

- Title: Group Policy hijacked: PAYLOAD ransomware weaponizes Active Directory GPO
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-09-21T10:00:40+00:00
- Link: https://securelist.com/tr/payload-ransomware-via-group-policy/121335/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky GERT experts dive into the technical incident analysis of PAYLOAD ransomware: an encryptionless, binary-less operation that abused Active Directory mechanisms for managing Group Policy Objects.
```

#### Full body

```
Threat Response Table of Contents Executive summary Group Policy as an attack surface Attack timeline Incident overview Initial access Execution The PAYLOAD GPO The win Firewall Off GPO The one-day delay detonation Forensic findings Detection engineering Anti-forensics and recovery-inhibition capabilities Confirmed PAYLOAD family capabilities Windows Event Log clearing Forensic indicators Security process and service termination Forensic indicators VSS deletion, backup and recovery suppression Forensic indicators Ecosystem-relevant ransomware techniques ETW suppression and in-memory patching Forensic indicators Vulnerable signed driver abuse, BYOVD Forensic indicators ESXi security policy weakening Forensic indicators Remediation Phase 1 — domain controller actions (to be performed first) Phase 2 — Active Directory and GPO hardening Phase 3 — credential and access hardening Phase 4 — detection and monitoring Conclusion Detection by Kaspersky solutions MITRE ATT&CK mapping Indicators of compromise Executive summary In April 2026, we at Kaspersky’s Global Emergency Response Team (GERT) responded to a security incident at a manufacturing organization in the Middle East. The threat actor obtained domain admin-equivalent control of the organization’s Active Directory environment and authored a malicious Group Policy Object (GPO) named PAYLOAD, linking it at the domain root. Through that single object, the actor delivered ransom notes, hijacked the desktop wallpaper and lock screen, enforced a logon banner, and disabled the local administrator account across every domain-joined Windows workstation — all without dropping a ransomware binary or encrypting any data. The only ransomware we found in this incident was PAYLOAD sample targeting ESXi on Linux servers. Besides that, data exfiltration was observed originating from the file servers and several additional systems, and was later published on the dark web. This case is an example of two converging trends that define the 2026 ransomware landscape : Living-off-the-land abuse of trusted AD infrastructure. Group Policy is a signed, allowlisted, SYSTEM-privileged distribution channel that the majority of endpoint detection and response tools is designed not to inspect. By delivering impact through GPO rather than through malware, the actor sidestepped the entire file- and process-based detection stack. Encryptionless extortion. Industry telemetry shows extortion-only incidents grow significantly year-on-year. PAYLOAD fits this model; the leverage is operational disruption and the threat of escalation rather than cryptographic denial of data. We confirmed that no files were encrypted on Windows machines, no malicious binaries were resident on disk, no endpoint persistence was established, and no malicious processes were running at the time of analysis. The entire attack lived inside Active Directory itself. The defensive implication is stark: an organization whose detection strategy depends on catching a ransomware executable would have seen nothing until the first endpoint rebooted and the ransom wallpaper appeared. In this article, we will describe the GPO attack chain and provide operational advice on how to detect such threats, including detailed remediation recommendations. Group Policy as an attack surface Attacks through group policies are nothing new. They can inflict significant, domain-wide damage with multiple malicious capabilities. A Group Policy Object (GPO) is essentially a combination of a Group Policy Container (GPC) in Active Directory and a Group Policy Template (GPT) in SYSVOL. The Group Policy scope depends on whether the GPC is linked to the directory tree at the domain, site, or organization unit (OU) level. A link at the domain root means the policy applies to every computer and user object beneath it. Thus, a GPO compromised at the domain root can affect all in-scope domain users and computers, potentially granting an attacker complete control over the corporate
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Group Policy hijacked: PAYLOAD ransomware weaponizes Active Directory GPO
  - Published: 2026-09-21T10:00:40+00:00
  - Link: https://securelist.com/tr/payload-ransomware-via-group-policy/121335/
  - Summary: Kaspersky GERT experts dive into the technical incident analysis of PAYLOAD ransomware: an encryptionless, binary-less operation that abused Active Directory mechanisms for managing Group Policy Objects.

### Cluster 12a3a99ac3 — score 10

- Title: The SMB cybersecurity squeeze: AI agents at work, old attacks in overdrive
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-09-21T09:00:00+00:00
- Link: https://www.welivesecurity.com/en/business-security/smb-cybersecurity-squeeze-ai-agents-work-old-attacks-overdrive/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, supply_chain, zero_day
- affected_industries: government
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft, zero_day
- affected_industries: government
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
As AI opens new paths to company data while making familiar attacks faster and cheaper, SMBs need protection designed around the time and expertise available to operate it
```

#### Full body

```
Business Security The SMB cybersecurity squeeze: AI agents at work, old attacks in overdrive As AI opens new paths to company data while making familiar attacks faster and cheaper, SMBs need protection designed around the time and expertise available to operate it Tomáš Foltýn 21 Sep 2026 • , 8 min. read AI has moved quickly into the daily work of small and mid-size businesses (SMBs). Many have moved past chatbots and begun assigning work to AI agents in the hope of gaining an edge on their similarly resource-strapped competitors and levelling the playing field with larger companies. Indeed, the ambitious adopters are deploying, or at least experimenting with, multi-agent ‘assembly lines,’ where one supervisor agent manages swarms of specialist agents and passes work between them. But AI changes more than how work gets done. Each new access and connection leaves the business with new dependencies that represent a potential cybersecurity risk. SMBs rarely have resources to spare, however, and least of all in IT. Cybersecurity in particular is often just one item on a list of duties owned by a person or small team that deals with everything from account provisioning to zero-day fallout. Yet few businesses are likely to backpedal on AI until every risk is mapped and addressed. Fewer still know which loopholes need plugging first – ESET’s recent global survey of 4,400 SMB decision-makers found that 40 percent of the businesses didn’t even have an AI policy. The rules were more common in companies that had already suffered an incident, revealing the familiar pattern where governance often arrives after a breach. Broadly speaking, today’s security risks are expanding in two main directions: AI creates new paths to business systems while adversaries use it to add speed and scale to ‘old’ threats. AI agents, double agents and errant agents Whatever its remit, each agent connected to business systems can act through permissions granted by its ‘owner.’ Once an agent has access to internal documents and can communicate externally, anything that influences its instructions can also influence what it does with its permissions. A chatbot may produce a wayward answer, whereas an agent with access to data and tools could take a wayward and, ultimately, costly action. In multi-agent setups, manipulated outputs can be handed to the next part of the chain, triggering a cascading problem whose root cause is difficult to track down. Of course, some risks surrounding AI agents have familiar roots: an agent’s supply chains can be compromised and its permissions abused. This is best illustrated by skills, or packaged instructions that tell an agent what actions to take and which tools to use. Between March and May 2026, ESET’s systems scanned almost 900,000 unique skills from popular repositories – more than 25,000 turned out to be suspicious and more than 3,000 outright malicious, leading to credential theft, data exfiltration and remote code execution. Figure 1. Instructions of a self-modifying skill that can lead to unpredictable behavior and abuse (source: ESET Threat Report H1 2026 ) How many were installed globally is anyone’s guess, but the analysis shows how quickly a poorly governed supply chain has grown around agentic AI. The skills ecosystem lacks app-store-style gatekeeping, and one-off checks before installation are by no means sufficient, either. Skills and tool connections, including those using ubiquitous MCP servers, remain live dependencies after an initial review as their instructions and upstream services can change at any time. The end result could be a “rug pull” where a tool that at first behaves as expected later morphs into, for example, an infostealer. A lean IT team is unlikely to review every such dependency at installation, much less continue to keep an eye on it afterwards. Indeed, they may not even know that an employee has connected a seemingly useful skill to an agent without realizing that it can, for example, read
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: The SMB cybersecurity squeeze: AI agents at work, old attacks in overdrive
  - Published: 2026-09-21T09:00:00+00:00
  - Link: https://www.welivesecurity.com/en/business-security/smb-cybersecurity-squeeze-ai-agents-work-old-attacks-overdrive/
  - Summary: As AI opens new paths to company data while making familiar attacks faster and cheaper, SMBs need protection designed around the time and expertise available to operate it

### Cluster 5f75cd0900 — score 10

- Title: Beware the SparroWock: The backdoor that bites, the commands that catch
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-09-17T08:50:00+00:00
- Link: https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- actor_attribution: Salt Typhoon
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- actor_attribution: Salt Typhoon
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
ESET researchers document SparroWocky, the new flagship backdoor of the FamousSparrow APT group
```

#### Full body

```
ESET Research Beware the SparroWock: The backdoor that bites, the commands that catch ESET researchers document SparroWocky, the new flagship backdoor of the FamousSparrow APT group Alexandre Côté Cyr Romain Dumont 17 Sep 2026 • , 27 min. read ESET Research’s ongoing monitoring of FamousSparrow has borne fruit once again. Our previous public report on FamousSparrow revealed that this China-aligned APT group had developed two new versions of its custom backdoor named SparrowDoor. This time, we discovered that FamousSparrow has switched to a new backdoor, SparroWocky, and has been deploying it to several countries in Latin America since at least August 2025. In what was probably China’s reaction to the US showing increased interest in Latin America, FamousSparrow increased its targeting of the region to almost exclusively targeting it in July 2025. A month later, we noticed that the group had started using the new SparroWocky backdoor, which then quickly replaced SparrowDoor as FamousSparrow’s main implant. SparroWocky is a modular, C++ backdoor. Its architecture and the techniques used by its authors indicate strong knowledge of anti-analysis tricks and Windows internals. We chose to name the backdoor SparroWocky because the first samples we collected all contain the first stanza of Jabberwocky , a nonsense poem by Lewis Carroll. Fortunately, while advanced, SparroWocky’s inner workings are much less arcane than a gyre and gimble in the wabe , so a through and through [of] the vorpal blade allowed us to bring you a detailed analysis of the backdoor. Key points of the blogpost: FamousSparrow is extensively targeting governmental organizations in Latin America. Since August 2025, the group appears to be abandoning SparrowDoor in favor of SparroWocky, a new custom C++ backdoor. With the switch to SparroWocky, FamousSparrow started to incorporate code from open-source projects directly into its malware. SparroWocky is a full-featured backdoor that manipulates low-level structures in memory, and patches code at runtime in order to avoid detection. SparroWocky has the capability to load and execute Beacon Object Files, a special type of executable file supported by many red-teaming and penetration-testing tools. FamousSparrow is a China-aligned cyberespionage group believed to have been active since at least 2019. We first publicly documented the group in a blogpost from September 2021 when we observed it exploiting the ProxyLogon vulnerability. The group was initially known for targeting hotels around the world but has also targeted governments, international organizations, trade groups, engineering companies, and law firms. FamousSparrow is the only known user of the SparrowDoor backdoor. We analyzed two versions of SparrowDoor in a 2025 blogpost , in which we also discussed the attribution claims around the group. As mentioned by Trend Micro , FamousSparrow is linked to Earth Estries; however, the exact nature of the link is not fully known. FamousSparrow has also been publicly linked to Salt Typhoon , but, due to the absence of any technical indicators, we track them as separate. Based on our investigation, we attribute the latest campaign and the SparroWocky backdoor to FamousSparrow with high confidence, since in some of the first attacks involving this backdoor, SparroWocky was deployed by the FamousSparrow-exclusive SparrowDoor. Moreover, not only does the victimology match FamousSparrow’s previous targeting, we have also recorded attempts to deploy SparroWocky at many of the same organizations that had previously been targeted with SparrowDoor. Latin America in the crosshairs As previously mentioned, FamousSparrow currently appears to be focused on high-profile targets in Latin America. This trend started at the latest in July 2025 and has continued with the introduction of SparroWocky. In fact, from mid-2025 and into 2026, 90% of the group’s targets registered in our telemetry have been located in the region. As depicted in
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: Beware the SparroWock: The backdoor that bites, the commands that catch
  - Published: 2026-09-17T08:50:00+00:00
  - Link: https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/
  - Summary: ESET researchers document SparroWocky, the new flagship backdoor of the FamousSparrow APT group

### Cluster b805a1709e — score 10

- Title: NodeZero Federal
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-22T13:00:00+00:00
- Link: https://horizon3.ai/downloads/factsheets/nodezero-federal/
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
Horizon3's NodeZero Federal provides production-safe, autonomous penetration testing for federal agencies. Achieve continuous readiness with proven, exploitable findings and rapid retest validation.
```

#### Full body

```
NodeZero Federal Horizon3 September 22, 2026 Factsheets Federal agencies face relentless pressure to defend critical systems against increasingly sophisticated threats. The challenge isn’t finding vulnerabilities—it’s proving which ones are actually exploitable before adversaries take advantage of them. NodeZero Federal is the FedRAMP High Authorized version of Horizon3’s proven NodeZero Offensive Security Platform. Purpose-built for sensitive federal environments, it delivers production-safe, autonomous penetration testing that continuously validates real-world attack paths without disrupting operations. By replacing assumptions with proof, NodeZero Federal helps security teams focus remediation efforts where they matter most: Continuously validate real exploitability across federal environments Identify chained attack paths that cross trust boundaries Prioritize remediation based on confirmed risk, not theoretical severity Verify fixes instantly with one-click retesting Support Zero Trust, Active Directory, and operational readiness initiatives Produce defensible, audit-ready evidence aligned with federal security requirements NodeZero Federal safely emulates real-world adversary behavior by chaining together weak credentials, misconfigurations, and security control gaps to reveal how attackers could move through your environment. Every finding includes proof of exploitation and actionable remediation guidance, enabling teams to reduce risk with confidence. Download the NodeZero Federal Factsheet to learn how FedRAMP High Authorized autonomous penetration testing helps federal agencies move from compliance-driven security to continuous operational readiness. Download the PDF How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: NodeZero Federal
  - Published: 2026-09-22T13:00:00+00:00
  - Link: https://horizon3.ai/downloads/factsheets/nodezero-federal/
  - Summary: Horizon3's NodeZero Federal provides production-safe, autonomous penetration testing for federal agencies. Achieve continuous readiness with proven, exploitable findings and rapid retest validation.

### Cluster 0af61280d0 — score 10

- Title: How Kyocera AVX Built a Global Security Validation Program from Zero
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-18T16:12:24+00:00
- Link: https://horizon3.ai/customer-story/kyocera-avx-global-security-validation/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
See how Kyocera AVX used NodeZero to build a global security validation program, scale autonomous pentesting across manufacturing sites, and remediate more than 30,000 vulnerabilities and misconfigurations.
```

#### Full body

```
How Kyocera AVX Built a Global Security Validation Program from Zero Horizon3 Customer Stories Building a security validation program across global manufacturing environments requires more than deploying another scanning tool. Security teams need to identify which weaknesses attackers can actually exploit, prioritize remediation, and validate risk without disrupting production. Kyocera AVX faced that challenge across 33 manufacturing sites worldwide. With no formal vulnerability management or pentesting program, the company needed a practical way to understand real exposure and build a repeatable validation process that could coexist with complex production environments. This customer story explores how Kyocera AVX used NodeZero® to build a global, evidence-driven security validation program, remediate more than 30,000 vulnerabilities and misconfigurations, and establish a pentesting cadence four times higher than the industry norm. Key Insight Traditional vulnerability findings show teams what might be vulnerable. Kyocera AVX needed an attacker’s perspective to understand which weaknesses could actually be exploited and chained into meaningful attack paths. By making NodeZero the engine behind its vulnerability management and pentesting program, Kyocera AVX gained: Visibility into real, exploitable attack paths A repeatable validation program across global manufacturing sites Actionable Fix Actions that IT teams could use to remediate risk Targeted retesting with 1-Click Verify Executive visibility through NodeZero data integrated with Splunk A sustainable testing model designed around production realities What You’ll Learn How to build a security validation program from the ground up Why exploit-based testing provides context traditional vulnerability findings cannot How Kyocera AVX scaled autonomous pentesting across global manufacturing environments How attack-path evidence helps overcome operational resistance to security testing Why Fix Actions can make remediation clearer and more actionable for IT teams How targeted retesting verifies whether security fixes actually reduce exposure How NodeZero data and Splunk dashboards help communicate risk to executives How continuous pentesting can coexist with production and OT-adjacent environments Why It Matters Manufacturing security teams have to balance cyber risk with business continuity and production safety. That can make organizations understandably cautious about introducing testing they perceive as invasive. But avoiding validation leaves another risk: vulnerabilities, misconfigurations, credential exposures, and attack paths can remain hidden because no one has demonstrated how an attacker could actually use them. Kyocera AVX changed that dynamic. NodeZero reached most manufacturing sites in roughly one to two years, compared with the four to five years typically required to fully roll out comparable tools in the company’s environment. Today, approximately 34 NodeZero hosts support regular assessments, with about four pentests per site each year plus targeted validation. In approximately three years, Kyocera AVX remediated more than 30,000 vulnerabilities and misconfigurations , transforming a program with essentially no formal vulnerability management or pentesting coverage into a global, evidence-driven security validation practice. Download the customer story to see how Kyocera AVX used NodeZero to build a global security validation program, expose real attack paths, and turn more than 30,000 weaknesses into measurable risk reduction. Download the customer story How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: How Kyocera AVX Built a Global Security Validation Program from Zero
  - Published: 2026-09-18T16:12:24+00:00
  - Link: https://horizon3.ai/customer-story/kyocera-avx-global-security-validation/
  - Summary: See how Kyocera AVX used NodeZero to build a global security validation program, scale autonomous pentesting across manufacturing sites, and remediate more than 30,000 vulnerabilities and misconfigurations.

### Cluster 63b4630409 — score 10

- Title: CTEM Buyer’s Guide: How to Evaluate the Technologies That Turn Continuous Threat Exposure Management Into an Operating Model
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-17T19:10:58+00:00
- Link: https://horizon3.ai/downloads/whitepapers/ctem-buyers-guide/
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
Learn how to evaluate CTEM technologies based on what they can prove, from exploitable attack paths and remediation priorities to verification and measurable risk reduction.
```

#### Full body

```
CTEM Buyer’s Guide: How to Evaluate the Technologies That Turn Continuous Threat Exposure Management Into an Operating Model Horizon3 | September 17, 2026 | Whitepapers Get the CTEM Buyer’s Guide Table of Contents From CTEM Framework to Operating Model Continuous Threat Exposure Management (CTEM) has become one of the most important—and broadly interpreted—frameworks in cybersecurity. Gartner® describes CTEM as an integrated, iterative approach to continuously evaluating and improving security posture. But CTEM is a framework, not a product category. The challenge for buyers is determining which technologies can turn it into a repeatable operating model that reduces exposure to attackers. Instead of asking which vendors support CTEM, ask: What can this technology prove about our exposure? This buyer’s guide translates CTEM into a practical operating loop: Discover Exposure, Validate Exploitability, Prioritize With Confidence, Remediate With Clarity, Verify Risk Removal, and Repeat. Learn how to evaluate solutions based on attacker evidence, attack-path context, remediation clarity, and measurable risk reduction, not simply findings or risk scores. Inside the Guide Learn how to: Understand the difference between threats, vulnerabilities, exposure, and risk. Evaluate how solutions uncover exposure across vulnerabilities, identities, credentials, misconfigurations, and security controls. See whether a solution can prove exploitability and demonstrate attacker impact. Prioritize remediation using proven exploitability, attack paths, and business impact. Verify that exposure is gone and track risk reduction over time. Ask five questions that separate CTEM claims from proof. Who Should Read This This buyer’s guide is designed for: Chief Information Security Officers (CISOs) Security Architects Exposure Management and Vulnerability Management leaders Security Operations and Security Engineering teams Cloud, Infrastructure, Identity, Application, and IT teams responsible for remediation Download the CTEM Buyer’s Guide Download the CTEM Buyer’s Guide to learn how to connect exposure to exploitability, remediation, verification, and measurable risk reduction. Not seeing the form? Open the standalone form . Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CTEM Buyer’s Guide: How to Evaluate the Technologies That Turn Continuous Threat Exposure Management Into an Operating Model
  - Published: 2026-09-17T19:10:58+00:00
  - Link: https://horizon3.ai/downloads/whitepapers/ctem-buyers-guide/
  - Summary: Learn how to evaluate CTEM technologies based on what they can prove, from exploitable attack paths and remediation priorities to verification and measurable risk reduction.

### Cluster 3e81320fe3 — score 10

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

### Cluster fa1e9027a9 — score 10

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

### Cluster 79f15f1302 — score 10

- Title: OAuth Token Theft Through Microsoft's Front Door | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-09-23T13:00:00+00:00
- Link: https://www.huntress.com/blog/stealing-oauth-tokens-through-microsofts-front-door
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng
- affected_products: Microsoft 365
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft
- affected_products: Microsoft 365
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A sideloaded package turns a Microsoft-signed binary into an OAuth token theft tool. No phishing domain, no spoofed UI, no browser. Here's how to detect it.
```

#### Full body

```
Home Blog Stealing OAuth Tokens Through Microsoft's Front Door Published: September 23, 2026 Stealing OAuth Tokens Through Microsoft's Front Door By: Andrew Schwartz Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways A sideloaded AppX package abuses Microsoft-signed AppX web hosts to present a legitimate Microsoft sign-in and capture the resulting OAuth tokens. Every component is trusted and Microsoft-signed, so there's nothing for signature-based detection to flag. The attack is post-compromise: it needs code execution in the user's session and Developer Mode (or an enterprise sideloading policy) already enabled. That setting is the real exposure gate. Audit where it's on and restrict it where it isn't needed. Stolen refresh tokens give durable access to the victim's Microsoft 365 data from any machine, and the blast radius scales with the compromised user's privileges. Detection is a network problem: watch for the MSAppHost/3.0 user agent reaching non-Microsoft destinations, then tune the Microsoft-domain allow-list and investigate related AppX registration activity. The same user agent appears across every host in this class, so the detection isn't host-specific. Introduction: The Login Page That Isn't Phishing I was hunting for the next regsvr32 . Not that binary specifically, but its category: a Microsoft-signed binary already on every Windows box that will fetch remote code and run it, so an attacker never has to drop anything unsigned. I pulled a catalog of signed binaries that don't appear in LOLBAS and filtered for anything that could reach the network and execute what it got back. The AppX web-host family came up in that filter, and one binary stood out. WWAHost.exe , the Windows Web App Host, will render whatever web content an AppX package points it at. That alone makes it interesting. However, what made me stop was the manifest flag: declare WindowsRuntimeAccess="all" and the remote JavaScript it renders doesn't just run, it inherits the full Windows Runtime API surface, including the API that drives OAuth sign-in. That was the moment it clicked as an attack. If a page I controlled could reach that sign-in API, it could stand up a real Microsoft login and pocket the tokens it handed back. I wanted to know if it actually worked. So I wired it up. A throwaway sideloaded package, a page hosted on my Kali box, and a call to WebAuthenticationBroker using Microsoft Office's own client ID. I ran it and watched a real Microsoft login dialog open on the desktop. Real, because it was: served from login.microsoftonline.com , rendered by a signed Microsoft process, with no address bar and no browser. I typed the password. I completed my MFA. A second later the access token and the refresh token were sitting in my listener. That was the part that got me. The user does everything right and it changes nothing, because there is no phishing page to catch, no lookalike domain, no certificate warning. Nothing about it is fake. It is Microsoft's real login flow, pointed at me. I tested this on Windows 11 24H2 (build 26100) with Developer Mode enabled. It needs no admin beyond the toggle for that one setting. Once that toggle is set, every component in the chain is a trusted, signed Microsoft binary doing exactly what it was built to do, so there is nothing signature-based defenses have an obvious reason to flag. The tokens it steals survive MFA entirely, because the user authenticates legitimately and I capture what comes back. Prerequisites Developer Mode must be enabled . This is the primary prerequisite and the main constraint on this attack. Without it, Add-AppxPackage -Register fails immediately with 0x80073CFF . Enabling it requires local administrator rights regardless of method ( Microsoft's Developer Mode documentation ): Via Settings: Settings > For developers > Developer mode > ON (UAC-gated, requires admin). Via registry (requires admin): reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\A
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: OAuth Token Theft Through Microsoft's Front Door | Huntress
  - Published: 2026-09-23T13:00:00+00:00
  - Link: https://www.huntress.com/blog/stealing-oauth-tokens-through-microsofts-front-door
  - Summary: A sideloaded package turns a Microsoft-signed binary into an OAuth token theft tool. No phishing domain, no spoofed UI, no browser. Here's how to detect it.

### Cluster fd0e351551 — score 10

- Title: Arista Urges Immediate Patching of Exploited VCO Zero-Day
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-23T08:33:06+00:00
- Link: https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- affected_industries: government
- affected_products: F5 BIG-IP, Microsoft Defender, WordPress
- cve_ids: CVE-2026-93952
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- affected_industries: government
- affected_products: F5 BIG-IP, Microsoft Defender, WordPress
- cve_ids: CVE-2026-93952
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Remote attackers could trigger the critical-severity flaw to access privileged internal functionality. The post Arista Urges Immediate Patching of Exploited VCO Zero-Day appeared first on SecurityWeek .
```

#### Full body

```
Networking solutions provider Arista has released urgent patches for a critical-severity vulnerability in on-premises VeloCloud Orchestrator (VCO) deployments that has been exploited as a zero-day. VCO is a centralized management tool for configuring, monitoring, and orchestrating edge devices, policies, and traffic in Arista VeloCloud SD-WAN. The exploited zero-day, tracked as CVE-2026-93952 (CVSS score of 10), is described as an improper input validation issue that could allow remote attackers to access privileged internal functionality. Successful exploitation of the security defect could impact the confidentiality, integrity, and availability of the orchestrator and the data it manages. “This issue was discovered externally and is known to be actively exploited,” Arista warns . According to the company, the bug affects only VeloCloud Orchestrator On-Prem (formerly VeloCloud Orchestrator by Broadcom) and was resolved in VCO versions 5.2.3.16 and 6.4.2.8 in the 5.2.x and 6.1.x trains, respectively. Patches for other trains will also be released. Advertisement. Scroll to continue reading. “VCO is exposed if certificate-based authentication from the VeloCloud Edge to VCO is configured. Access to the public portion of the VeloCloud Edge authentication certificate is required. A successful attack requires network access to the VCO web interface. VCO tenant or operator credentials are not required for this exposure,” the company notes. Arista says that deployments that limit access to the VCO web interface have a lower risk of exposure, but urges updating to a fixed release. The company noted that there are no definitive indicators of compromise (IoCs), recommending administrators review VCO web access logs, backend application logs, and system logs for suspicious activity. CVE-2026-93952 was added to CISA’s Known Exploited Vulnerabilities ( KEV ) list on Tuesday. In line with BOD 26-04’s recommendations, federal agencies were given three days to patch it. Related: Critical F5 BIG-IP APM Vulnerability Exploited as a Zero-Day Related: Check Point Patches Exploited Management Server Zero-Day Related: Nightmare Eclipse Drops New Microsoft Defender Exploit After Revealing Identity Related: Cisco Fixes Dozens of Flaws Across FMC, ISE and Nexus Dashboard Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Critical F5 BIG-IP Vulnerability Exploited as Zero-Day Check Point Patches Exploited Management Server Zero-Day BigCommerce Data Stolen via Ribon Apps Hack Recent ZyXEL Switch Vulnerability Exploited by Chinese Hackers Malicious B-tree NPM Package Accumulates Millions of Downloads WordPress Patches ‘Click2Shell’ Vulnerability Fake LastPass Installers Push Kernel-Level EDR Killer, ‘Rapuncel’ Stealer RatHat Android Trojan Uses AI for Automation Latest News IonQ Targets Quantum Error-Correction Bottleneck With Single-CPU DecoderIonQ Says Sin Worries About an AI Internet Takeover Gain New Urgency Among Doomsday Scenarios Honeywell: OT Security Teams Embrace AI, but Autonomy Still Rare Adobe Patches Critical Flaws in Connect, AEM Forms AI-Powered Phishing Platform EvilTokens Disrupted by Microsoft Chrome 154 Patches 108 Vulnerabilities A Look at AI Doomsday Scenarios That Researchers Say Could Put Humanity at Risk Outerlimit Raises $16 Million to Stop Rogue AI Agents From Causing Harm Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Virtual Event: Attack Surface Management Summit 2026 September 16, 2026 Join as speakers examine the various components of ASM strategy, the push to mandate continuous asset visibility and inventory tools, and the use of red-teaming, bug bounties and pen-tests in moder
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Arista Urges Immediate Patching of Exploited VCO Zero-Day
  - Published: 2026-09-23T08:33:06+00:00
  - Link: https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/
  - Summary: Remote attackers could trigger the critical-severity flaw to access privileged internal functionality. The post Arista Urges Immediate Patching of Exploited VCO Zero-Day appeared first on SecurityWeek .

### Cluster 73be0cc433 — score 10

- Title: DarkMe RAT trades zero-days for plain phishing emails
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-09-23T13:24:17+00:00
- Link: https://www.helpnetsecurity.com/2026/09/23/darkme-rat-phishing-email-hits-corporate-targets/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, zero_day
- affected_industries: critical_infrastructure, financial_services
- affected_products: SonicWall
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, zero_day
- affected_industries: financial_services, critical_infrastructure
- affected_products: SonicWall
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
DarkMe, a remote access trojan and info-stealer that has previously been associated with a threat group that targeted financial market traders and cryptocurrency users, has been spotted again. This time around, its distribution has been simplified: instead of leveraging zero-day exploits, attackers are betting on a simple email to convince targets to run it on their machine: The malicious email pointing to the first stage downloader for DarkMe (Source: Huntress) The link supposedly points to … More → The post DarkMe RAT trades zero-days for plain phishing emails appeared first on Help Net Security .
```

#### Full body

```
Zeljka Zorz , Editor-in-Chief, Help Net Security September 23, 2026 Share DarkMe RAT trades zero-days for plain phishing emails DarkMe, a remote access trojan and info-stealer that has previously been associated with a threat group that targeted financial market traders and cryptocurrency users, has been spotted again. This time around, its distribution has been simplified: instead of leveraging zero-day exploits , attackers are betting on a simple email to convince targets to run it on their machine: The malicious email pointing to the first stage downloader for DarkMe (Source: Huntress) The link supposedly points to a PNG file, but clicking on it triggers the download of image.pif , a Windows executable. From fake image file to full-blown RAT Huntress, a cybersecurity company that pairs its own security software with a 24/7 human-led SOC, says that the same binary was delivered to two of its customers’ envrionments. “The users simply double-clicked and downloaded the file, not realising what it was,” they noted. “Modern Windows systems execute .pif files as a program, regardless of what the extension implies (or what the icon shows).” The execution started a chain of additional downloads and executions, script running, deployment of components, DLL invocations, and code injection. “The command that initiates the final stage of infection, rundll32.exe /sta {CFDC57BA-1705-45AF-BA10-EFC3D592982B} , was observed in the 2024 campaign, and is a great signature to detect or hunt on,” the analysts pointed out. A final chain of loaders tests the system for presence of many different applications: from Slack and Discord, Zoom and WhatsApp, password managers, trading terminals, online poker clients, cryptowallets, VPN clients, gmae laungers, Spotify, browsers, PDF readers, and OEM and peripheral support utilities. “That last category reframes the whole list. Gaming-mouse configuration utilities and RGB lighting daemons hold nothing of value, but they do prove that a human being uses this computer,” they explained. “Execution stops when none of the 329 are found. This is not a target list; it is an inverted sandbox check. A conventional evasion check looks for analysis tooling and bails when it finds it, but this list contains no analysis tools. Rather than asking “am I being watched?”, DarkMe asks whether anyone actually uses this system.” Then comes the creation of registry values to assure persistence, the profiling of the system, the process hollowing, and the final payload: DarkMe, a Visual Basic 6 RAT and infostealer that goes after crypto-wallets and can take screenshots. Who’s behind these attacks? Andrew Brandt, Principal Threat Intelligence Incident Commander at Huntress, told us that they can’t confirm that this attack was carried out by Water Hydra (aka DarkCasino), the threat group associated with the 2024 attacks documented by Trend Micro and SonicWall. “We do have some clues about the malware’s possible origins. For example, the Spanish localization property in the compiled DLLs suggests that the developer may be a Spanish national or living in Spain,” he noted. “As for motivation, the activity appears to be financially driven, though the actors also seem willing to target children for things like Roblox Robux or Steam and Epic Games registration keys.” He also said that, at this point, they don’t know whether DarkMe is being offered as-a-Service to cybercriminals willing to pay for it. Unfortunately, he wasn’t able to share details about Huntress’ customers that were affected, but the shift in targeting from niche forex traders to everyday corporate users is apparent. “We are watching threat actors pivot from highly skilled, targeted intrusions toward high-volume, low-effort attacks and the results speak for themselves. In 2026, users are still clicking links in unsolicited emails. As long as these old-school phishing tactics keep working, adversaries have no reason to burn expensive exploits,” Brandt and colleague James
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: DarkMe RAT trades zero-days for plain phishing emails
  - Published: 2026-09-23T13:24:17+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/23/darkme-rat-phishing-email-hits-corporate-targets/
  - Summary: DarkMe, a remote access trojan and info-stealer that has previously been associated with a threat group that targeted financial market traders and cryptocurrency users, has been spotted again. This time around, its distribution has been simplified: instead of leveraging zero-day exploits, attackers are betting on a simple email to convince targets to run it on their machine: The malicious email pointing to the first stage downloader for DarkMe (Source: Huntress) The link supposedly points to … More → The post DarkMe RAT trades zero-days for plain phishing emails appeared first on Help Net Security .

### Cluster b04cf6724c — score 10

- Title: GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
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
Will Thomas 5 min read March 5, 2026 GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster Analysing and pivoting on threat actor infrastructure is a useful technique to uncover additional indicators that could be used to detect an evasive adversary. This process can take multiple approaches. CTI analysts often develop their own methodologies and workflows with preferred datasets to perform this type of analysis. The effectiveness of this practice also depends on what is available to the CTI analysts who do this work and it often involves combining multiple data sources together. This includes WHOIS data, Port Banners, X509 certificates, and passive DNS records, as well as internet NetFlow analysis. This blog is a walkthrough of how it is possible to start with one IP address from a trusted source and uncover a set of potentially related infrastructure. By peering into the adversary‚Äôs other activities, it can be possible to find additional victims of the campaign or even the adversary remotely accessing their victim-facing infrastructure using Team Cymru‚Äôs external NetFlow data. Overall, this infrastructure pivoting is a practical workflow that CTI analysts can perform to support proactive threat hunting in historical logs as well as generate detection rules to alert a security operations center (SOC) about any future connections and attempts by an adversary. UNC6201 + GRIMBOLT: Starting From a Known-Bad IP Infrastructure pivoting can begin with initial indicators of compromise (IOCs) that are reported by a trusted source. In this blog, the trusted source is Google, which disclosed a recent campaign about a ‚Äúsuspected PRC-nexus threat cluster‚Äù dubbed UNC6201 and sharing the IP address 149.248.11[.]71. Google designated this as a GRIMBOLT malware command-and-control (C2) server. The UNC6201 campaign involved the exploitation of a critical zero-day vulnerability in Dell RecoverPoint for Virtual Machines tracked as CVE-2026-22769 , as well as the deployment of a newly identified malware dubbed GRIMBOLT, written in C#. This campaign has reportedly been ongoing for nearly two years, indicating a long-term espionage operation focusing on persistent access. Interestingly, Google observed UNC6201-linked threat actors actively replacing older BRICKSTORM binaries with GRIMBOLT. Google reported that there are notable overlaps between UNC6201 and UNC5221 , which has been used synonymously with the moniker Silk Typhoon (formerly known as HAFNIUM ) by Microsoft. However, Google does not currently consider the two clusters to be the same. Further, the BRICKSTORM malware operators are also tracked as WARP PANDA by CrowdStrike. Building an IP Profile in Scout (WHOIS, PDNS, Ports, X509) Using a Scout summary, we can view the current attributes about the IP address. This includes WHOIS records, generated by Team Cymru‚Äôs BGP routing visibility as well as Team Cymru‚Äôs proprietary Tagging system, as shown in Figure 1 below. Figure 1: Scout Summary for 149.248.11[.]71. Scout also has current and historical passive DNS records, which shows what domain is hosted on an IP address, the record type, as well as the first seen and last seen dates, as shown in Figure 2 below. Figure 2: IP Passive DNS in Scout for 149.248.11[.]71. Analysts can use the Open Ports tab in Scout to find out what services running on the system as well as which operating system (OS) it uses, as shown in Figure 3 below. Figure 3: IP Port Banners in Scout for 149.248.11[.]71. X509 certificate information in Scout reveals interesting traits, such as the X509 Subject Common Name and X509 Issuer Common Name being a NetBIOS hostname derived from some sort of Windows template used by either a threat actor or VPS provider. This can be used to identify other systems controlled by the adversary. The X509 certificate‚Äôs Not Before and Not After dates are also very useful to understand when the system was configured by an adversary. See these details in Figur
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/grimbolt-c2-infrastructure-mapping-and-reconnaisssance
  - Summary: Explore how to Map GRIMBOLT C2 infrastructure linked to UNC6201 by pivoting from one IP using WHOIS, PDNS, ports, and X509 certificate fingerprints.

### Cluster c1f52c0381 — score 10

- Title: Tracking ORBs on Singapore's Telecommunications Networks
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
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
Will Thomas 3 min read February 11, 2026 Tracking ORBs on Singapore's Telecommunications Networks ORB networks, which stands for Operational Relay Box networks, are obfuscated mesh networks used by threat actors to mask the origin of their cyberattacks. These networks are often composed of a mix of compromised Internet-of-Things (IoT) devices, Small Office/Home Office (SOHO) routers, and Virtual Private Servers (VPS). Team Cymru has blogged previously about ORBS here . ORBs are considered a significant threat for several key reasons: Evasion and Anonymity: ORBs act like private residential proxy networks, allowing attackers to route their traffic through nodes that appear to be legitimate home or commercial broadband users. This masks the attacker's true location and makes it difficult for defenders to trace the activity back to the source. Blending with Legitimate Traffic: Because ORB nodes often reside on compromised devices used by real people (such as home routers), malicious traffic is frequently mixed with "normal" user traffic. This makes detection challenging and creates a risk for defenders: blocking an ORB IP address could inadvertently block legitimate users or disrupt genuine business services. Resilience and Flexibility: Attackers can easily scale these networks by adding or removing compromised devices and servers. If a node is discovered and blocked, it can be quickly replaced, making the network highly resilient to takedown attempts. Pre-positioning: Experts note that adversaries use ORBs to "commute" to a target's perimeter, allowing them to pre-position themselves months in advance of an attack. This infrastructure facilitates reconnaissance and exploitation while keeping the adversary's "bridge" intact even if specific operations are detected. Geographical Evasion: By routing traffic through nodes located near their targets, attackers can circumvent geofencing security controls and make their traffic appear more legitimate. UNC3886 Campaign against M1, SIMBA Telecom, Singtel, and StarHub On February 9, 2026, the Cyber Security Agency of Singapore (CSA) released a press release detailing a multi-agency cybersecurity operation, codenamed Operation CYBER GUARDIAN, intended to defend their communications sector. The CSA first shared that they detected an Advanced Persistent Threat (APT) actor tracked as UNC3886 attacking Singapore‚Äôs critical infrastructure on July 18, 2025. The CSA‚Äôs investigation has uncovered that UNC3886 had launched a deliberate, targeted, and well-planned campaign against Singapore‚Äôs telecommunications sector. All four of Singapore‚Äôs major telecommunications operators‚ÄîM1, SIMBA Telecom, Singtel, and StarHub‚Äîwere targeted. Notably, the CSA observed the adversary using a zero-day exploit to bypass a perimeter firewall of the victims and gain access into their telecommunications networks. The adversary also managed to reportedly exfiltrate a small amount of technical data; this is believed to be primarily network-related data to advance the threat actors‚Äô operational objective. What made UNC3886 a challenge to find was its use of advanced tools and techniques such as rootkits to evade basic detection systems. UNC3886‚Äôs Historical Campaigns According to Mandiant, UNC3886 is a state-sponsored threat group tied to Chinese cyber-espionage operations. The group is well-known for exploiting zero-day vulnerabilities in edge devices and virtualised systems to gain stealthy, long-term access. Its targets span energy, water, telecommunications, finance, and government services, with tactics that include custom malware and advanced persistence techniques. UNC3886 has reportedly used zero-days in Fortinet, VMware, and Juniper devices and has deployed custom malware families to maintain access on them. Interestingly, from Mandiant‚Äôs report in March 2025 about UNC3886 targeting Juniper routers, the indicators of compromise (IOCs) they shared were all located in Singapore and some of the ta
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Tracking ORBs on Singapore's Telecommunications Networks
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/tracking-orbs-on-singapores-telecommunications-networks
  - Summary: APT attacks by UNC3886 target Singapore telecom using ORB networks. Learn practical ORB tracking techniques to uncover hidden infrastructure with Scout.

### Cluster fc5c9992d3 — score 10

- Title: Scattered Spider Attacks | Infrastructure and TTP Analysis
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-21T22:37:48+00:00
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
An in-depth analysis of Scattered Spider attacks, detailing the group‚Äôs infrastructure usage and TTPs to help defenders detect and disrupt activity earlier.
```

#### Full body

```
Will Thomas 5 min read January 21, 2026 Scattered Spider Attacks | Infrastructure and TTP Analysis Background on Recent Scattered Spider Attacks Throughout 2024 and 2025, Scattered Spider has been a prolific English-speaking cybercriminal threat group, part of a broader community of cybercriminals dubbed TheCom, which is short for The Community. In May 2024, at the cybercrime-focused Sleuthcon conference, the FBI warned about Scattered Spider and members of TheCom for being responsible for multiple high-profile multi-million dollar breaches. In 2023, MGM Resorts disclosed via their US Security Exchange Commission (SEC) filing that the overall cost from the ALPHV/BlackCat ransomware attack that was linked to Scattered Spider was $100 million USD. In mid-2025, Marks & Spencer said it will take an estimated ¬£300 million hit following the DragonForce ransomware attack, linked to Scattered Spider. Google‚Äôs security experts also assessed that Scattered Spider was responsible for the Co-op and Harrods attacks in mid-2025 as well. Where did the name ‚ÄúScattered Spider‚Äù come from? The name Scattered Spider was originally used by CrowdStrike and has been adopted by multiple other organizations such as the US Cybersecurity and Infrastructure Security Agency (CISA) and MITRE. Other cybersecurity companies have given them other names, such as UNC3944 by Google Mandiant, 0ktapus by Group-IB, Octo Tempest by Microsoft, Scatter Swine by Okta, and Muddled Libra by Palo Alto Networks. What are Scattered Spider‚Äôs capabilities? Scattered Spider are most well-known for being English-speaking affiliates of ransomware-as-a-service (RaaS) platforms developed by Russian-speaking threat actors. This includes ALPHV/BlackCat, Qilin, RansomHub, and DragonForce. Their typical tactics, techniques, and procedures (TTPs) involve using social engineering tactics for initial access. This includes calling IT help desk technicians, posing as employees, and convincing them to reset a password or install a remote monitoring and management (RMM) tool to grant them access. Single sign-on (SSO)-themed SMS phishing campaigns and SIM swapping campaigns targeting enterprise account credentials have also been linked to Scattered Spider intrusions. Once they have gained access, Scattered Spider tends to test access to all available SSO-integrated applications and aims to move laterally to virtualised environments such as VMware ESXi hypersvisors or cloud-hosted virtual machines. Once privileged access has been acquired, Scattered Spider tends to exfiltrate sensitive corporate data and deploy ransomware generated from one of the several RaaS platforms they have access to. Scattered Spider‚Äôs Adversary Infrastructure Profile Scattered Spider style attacks remain a large focus for many of Team Cymru‚Äôs customers. To support threat detection programs, Team Cymru has analyzed open source intelligence (OSINT) reporting about Scattered Spider‚Äôs preferred choice of infrastructure to use for launching intrusions. At a high level, Scattered Spider intrusions have typically leveraged the following types of infrastructure: Common consumer-level virtual private network (VPN) clients Connection tunneling web services Free file-sharing and paste site web services Large-scale residential proxy networks Infostealer malware exfiltration servers RMM tool web services SSO-themed domains for SMS phishing The Challenges with Scattered Spider‚Äôs Infrastructure One of the significant challenges from Scattered Spider is the sheer reuse and shared nature of the infrastructure they use. By utilizing legitimate, high-reputation services, they effectively hide in plain sight, making it untenable for defenders to block their indicators without disrupting normal business operations. Unlike known malicious IPs, VPN exit nodes are used by millions of legitimate users. Defenders cannot easily create a block-list of these IPs without risking significant false positives, especially in a world of
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Scattered Spider Attacks | Infrastructure and TTP Analysis
  - Published: 2026-09-21T22:37:48+00:00
  - Link: https://www.team-cymru.com/post/scattered-spider-attacks-infrastructure-profile
  - Summary: An in-depth analysis of Scattered Spider attacks, detailing the group‚Äôs infrastructure usage and TTPs to help defenders detect and disrupt activity earlier.

### Cluster 2d38cac489 — score 10

- Title: A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-23T16:53:10+00:00
- Link: https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: GitLab

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: GitLab
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: GitLab
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The private email address GitLab gives you for filing issues by email is a credential. Anyone who gets it can email a patch that GitLab commits in your name, to any branch you can push to, including main, and can start CI/CD jobs that run as you. GitLab shows each user this address behind a button labeled "Email work item to this project." Mail sent to it opens an issue in that project, authored
```

#### Full body

```
A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You  Swati Khandelwal  Sep 23, 2026 DevOps Security / Supply Chain The private email address GitLab gives you for filing issues by email is a credential. Anyone who gets it can email a patch that GitLab commits in your name, to any branch you can push to, including main, and can start CI/CD jobs that run as you. GitLab shows each user this address behind a button labeled "Email work item to this project." Mail sent to it opens an issue in that project, authored by you. The string in the middle of the address is a token tied to your account, and GitLab's documentation says it does not expire. The address looks like it belongs to one project. It does not. Aikido Security , which reported the behavior, found that the addresses GitLab creates for a user's different projects all share the same token, and that the token applies to every project the account can open, public or private. GitLab does not check who sent the email. Any mailbox can write to the address, and GitLab acts on the message as if it came from you. Whoever holds the address can both sign in as you and act with your permissions, without ever touching your mailbox. The address does more than file bugs. Aikido showed how a holder turns it into a way to commit code, using GitLab's own merge request by email feature: Change the address suffix from -issue to -merge-request. GitLab then opens a merge request instead of an issue. Write a patch, and put the name of a target branch in the email subject line. Attach the patch and send it. GitLab applies the patch to that branch, and creates the branch if it does not already exist. The change lands as a commit on that branch, authored by you. If it is a branch you can push to, that includes main. If the patch edits the project's .gitlab-ci.yml file and your role allows it, GitLab runs the attacker's job as you. The merge request itself cannot be directed at a copy of the project the attacker controls, which is why the attached patch, not the merge request, carries the code. Two things keep this from being worse. The token carries only your own permissions, so how far an attacker gets depends on your role. A leaked address for a Guest account is nearly useless, whereas one for a Maintainer can access protected branches and CI/CD secrets. Reaching a project also takes more than the address. GitLab works out the target from the project's path and its numeric ID, so an attacker who wants a particular project needs that project's path and ID as well as the token. Public projects publish both. A private project takes a separate leak that names it, though GitLab's project IDs are easy to guess. Because incoming email is exempt from IP restrictions, the attack can originate from outside an IP allowlist. GitLab's documentation states that incoming email is not subject to IP restrictions . Aikido locked a private project to a single IP address that was not its own. GitLab blocked its browser and refused a git clone, but it accepted the merge request email, and the commit landed on main. The same path skips two-factor authentication. GitLab's documentation notes that incoming email features work without 2FA , even on instances that require it. Every GitLab.com account has one of these tokens, and so does every self-managed GitLab instance with incoming email turned on, which is the default on GitLab.com. GitLab Dedicated does not appear to be affected, because GitLab limits the feature to self-managed and GitLab.com, but Aikido said it could not test Dedicated directly. What to do You cannot stop other people from having the feature, but you can cut off a leaked address. Reset your incoming email token from the personal access tokens page in your profile. The reset replaces every project address at once, so an address you are actively using will stop working until you hand out the new one. Look through your own READMEs, contributing guides, and support pages
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You
  - Published: 2026-09-23T16:53:10+00:00
  - Link: https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html
  - Summary: The private email address GitLab gives you for filing issues by email is a credential. Anyone who gets it can email a patch that GitLab commits in your name, to any branch you can push to, including main, and can start CI/CD jobs that run as you. GitLab shows each user this address behind a button labeled "Email work item to this project." Mail sent to it opens an issue in that project, authored

### Cluster df5a100cb0 — score 10

- Title: Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-22T18:29:39+00:00
- Link: https://thehackernews.com/2026/09/check-point-warns-of-management-server.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-93616

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- cve_ids: CVE-2026-85102, CVE-2026-85103, CVE-2026-91843, CVE-2026-93616
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- cve_ids: CVE-2026-93616, CVE-2026-85102, CVE-2026-91843, CVE-2026-85103
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Attackers exploited a previously unknown flaw in Check Point's Security Management Server in a handful of targeted attacks on July 23, the company said. The flaw, CVE-2026-93616, allows an attacker who can access the server's web service to run scripts on it without logging in. Check Point released a fix on September 22 for the server that controls firewall policies for the Check Point
```

#### Full body

```
Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks  Swati Khandelwal  Sep 22, 2026 Network Security / Vulnerability Attackers exploited a previously unknown flaw in Check Point's Security Management Server in a handful of targeted attacks on July 23, the company said . The flaw, CVE-2026-93616 , allows an attacker who can access the server's web service to run scripts on it without logging in. Check Point released a fix on September 22 for the server that controls firewall policies for the Check Point gateways it manages. Separately, Check Point said attackers have been trying since September 12 to exploit a VPN flaw it fixed on September 9 . The attempts, against a flaw tracked as CVE-2026-85102, have targeted customers of Spark, Check Point's firewall line for small businesses. When the fix came out, Check Point had no evidence the flaw was being exploited. CVE-2026-93616 is a path traversal bug in the management server's web service. The service does not properly limit which files and folders a request can reach. An attacker can use it to upload scripts to the server and then run them. Check Point rated it 9.8 out of 10 on the CVSS scale in the CVE record for the flaw. Check Point's advisory does not name the targets of the July attacks or the attackers, nor does it say what the attackers did after exploiting the flaw. Management Server Versions and Fix Check Point numbers the Jumbo Hotfix updates for each release by "Take." Its LivePatch channel, which pushes urgent fixes, uses a separate set of take numbers. The CVE record lists these versions as affected: R82.20 with no Jumbo Hotfix installed R82.10 with Jumbo Hotfix Take 44 or below R82 with Jumbo Hotfix Take 126 or below R81.20 with Jumbo Hotfix Take 166 or below R81.10 with Jumbo Hotfix Take 190 or below (end of support) R81, R80.40, R80.30, R80.20, R80.10 and R80 (all end of support) Check Point's advisory lists R82.20 as affected without the "no Jumbo Hotfix" condition. On September 16, Check Point fixed a separate flaw in the management server , CVE-2026-91843, through LivePatch. That update was LivePatch Take 28, or Take 29 on R82.20, according to a summary of Check Point's advisory by France's CERT Santé . Check Point says those LivePatch takes do not fix CVE-2026-93616. CVE-2026-85103, a VPN certificate flaw that Check Point fixed on September 9, affected both gateways and management servers. On R82.10, R82, and R81.20, the new flaw's affected list goes one take higher than that flaw's. So a server updated only enough to be outside that September flaw's range is still affected by CVE-2026-93616. The fixed builds, and Check Point's guidance on mitigation, hunting and indicators of compromise, are in support article sk1000171 . Administrators of management servers should: Check the server's release and Jumbo Hotfix take against the list above. Install the fix listed in sk1000171. Use the hunting guidance and indicators of compromise in sk1000171 to look for signs of an attack. Installing the fix does not show whether the server was attacked before. Check Point's advisory names only Security Management as affected and does not say what network access an attacker needs. The Hacker News has asked Check Point about other affected products, the fixed builds, and the July attacks. Spark Firewalls Targeted Through VPN Flaw CVE-2026-85102 is in the way Check Point gateways check certificates while a VPN connection is being set up. It may let an attacker who has not logged in run code on the gateway. Fixes have been out since September 9 and are in support article sk1000117 . The affected products are Security Gateway and Spark firewalls, whether centrally or locally managed, on R81 and R81.10 (both end of support), R81.10.x, R81.20, R82, R82.00.x and R82.10. The Netherlands' National Cyber Security Centre (NCSC) says the flaw applies when these products use Site-to-Site VPN or Remote Access VPN. Check Point said the attempts came from anonymiz
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks
  - Published: 2026-09-22T18:29:39+00:00
  - Link: https://thehackernews.com/2026/09/check-point-warns-of-management-server.html
  - Summary: Attackers exploited a previously unknown flaw in Check Point's Security Management Server in a handful of targeted attacks on July 23, the company said. The flaw, CVE-2026-93616, allows an attacker who can access the server's web service to run scripts on it without logging in. Check Point released a fix on September 22 for the server that controls firewall policies for the Check Point

### Cluster 9ed08264e4 — score 10

- Title: Ransomware Attacks Reach Record High for 2026
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-23T12:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/ransomware-attacks-reach-record/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A total of 1073 firms fell victim to ransomware attacks globally in August, with the industrial sector the most affected, according to new NCC data
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Ransomware Attacks Reach Record High for 2026
  - Published: 2026-09-23T12:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/ransomware-attacks-reach-record/
  - Summary: A total of 1073 firms fell victim to ransomware attacks globally in August, with the industrial sector the most affected, according to new NCC data

### Cluster 3bc8cb0c0c — score 10

- Title: Quoting voxium
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-09-20T21:06:43+00:00
- Link: https://simonwillison.net/2026/Sep/20/voxium/
- Fetch status: not_attempted
- Member count: 5
- Corroborating source count: 4
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude, Microsoft 365, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
It has been half a month since I started a new role at a big company. Nobody knows anything here. The specs, code, tests, PRDs, tickets, resolution of those tickets, reports, etc., everything is made by Claude Code. Nobody on my team likes this. They are being forced to ship as much as they can. I have heard multiple times from higher management that pushing code is not a bottleneck, so why are we slow? People are working 12 to 13 hours a day just to press enter. Nobody is reading anything. Everyone, literally everyone, from an L1 to an L7 engineer here is doing the same thing. Talk to Claude. — voxium Tags: ai-misuse , llms , ai , generative-ai
```

#### Corroborating sources (4)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting voxium
  - Published: 2026-09-20T21:06:43+00:00
  - Link: https://simonwillison.net/2026/Sep/20/voxium/
  - Summary: It has been half a month since I started a new role at a big company. Nobody knows anything here. The specs, code, tests, PRDs, tickets, resolution of those tickets, reports, etc., everything is made by Claude Code. Nobody on my team likes this. They are being forced to ship as much as they can. I have heard multiple times from higher management that pushing code is not a bottleneck, so why are we slow? People are working 12 to 13 hours a day just to press enter. Nobody is reading anything. Everyone, literally everyone, from an L1 to an L7 engineer here is doing the same thing. Talk to Claude. — voxium Tags: ai-misuse , llms , ai , generative-ai
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Fake Claude Max giveaway tricks users into handing over their Google account credentials
  - Published: 2026-09-23T13:03:15+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/23/fake-claude-max-giveaway-phishing/
  - Summary: A fake Claude Max giveaway uses a spoofed Google sign-in window to steal users’ login credentials, Malwarebytes researchers have found. “Browser-in-the-browser” is not a new technique. Researchers have documented it since 2022, and in June Palo Alto Networks’ Unit 42 reported a campaign that used draggable fake browser windows to target Microsoft 365 users. “Phishing follows whatever people want at the moment,” noted Stefan Dasic, the Malwarebytes researcher who analyzed the campaign. “Claude’s paid plans … More → The post Fake Claude Max giveaway tricks users into handing over their Google account credentials appeared first on Help Net Security .
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: I asked my AI agent to inspect a website. The website took over my machine (34-run measurement across 5 agent harnesses)
  - Published: 2026-09-23T19:56:44+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wogg6h/i_asked_my_ai_agent_to_inspect_a_website_the/
  - Summary: I set up a local lab to test what happens when a developer asks their coding agent to inspect an untrusted website and clone its sample repo. Measured 34 runs across 5 harnesses (omp, opencode, Claude Code, Codex, Gemini): Browser rendering: untrusted JS stole active session tokens in 11 of 12 runs (even with HttpOnly cookies, same-origin API fetches walked away with account data). Pre-trust RCE: project-scoped .mcp.json spawned declared commands before the model read the prompt (Claude Code executed it even while logged out). Two harnesses (Codex, Gemini) blocked the launch via workspace trust; three spawned without prompting. Full comparison table, 1-minute local reproduction, and mitigations in the link. submitted by /u/DaimoNNN [link] [comments]
- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #346 - Can AI Do Novel Security Research?, Anthropic's Threat Intel Report, How Cloudflare Enforces Engineering Standards
  - Published: 2026-09-17T14:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-346
  - Summary: Portswigger's James Kettle's HTTP Terminator, pretty crazy report about how threat actors were abusing Claude, how Cloudflare enforces code quality at scale

### Cluster 0508e89cda — score 10

- Title: Gemini Hacked Three Companies in First Known Breakout by Google’s AI
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-09-18T23:57:57+00:00
- Link: https://simonwillison.net/2026/Sep/18/gemini-hacked-three-companies/
- Fetch status: not_attempted
- Member count: 3
- Corroborating source count: 3
- Strong signals: Google/Gemini

#### Cluster taxonomy (union across members)
- affected_products: Google/Gemini, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- affected_products: Google/Gemini
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Gemini Hacked Three Companies in First Known Breakout by Google’s AI Gemini finally caught up on Felony Bench ! The hacks, which the company confirmed on Friday, occurred in May as part of a test run by the company Irregular, which was also involved in similar incidents disclosed by OpenAI, Anthropic and Meta. In one of the cases, the model guessed passwords until it gained access to a protected system. In the other two cases, the model found credentials in a public repository that allowed it to then access protected systems. In each case, the model ended the intrusion after determining it had accessed a real company’s systems, Google said. Gemini is apparently less determined than other models, and decided not to keep going. Google knew about these in July, but chose not to disclose them until the WSJ reached out, presumably based on a tip. Google said it didn’t consider the hacks to warrant public disclosure—because its model didn’t cause harm to the companies and ended each intrusio
```

#### Corroborating sources (3)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Gemini Hacked Three Companies in First Known Breakout by Google’s AI
  - Published: 2026-09-18T23:57:57+00:00
  - Link: https://simonwillison.net/2026/Sep/18/gemini-hacked-three-companies/
  - Summary: Gemini Hacked Three Companies in First Known Breakout by Google’s AI Gemini finally caught up on Felony Bench ! The hacks, which the company confirmed on Friday, occurred in May as part of a test run by the company Irregular, which was also involved in similar incidents disclosed by OpenAI, Anthropic and Meta. In one of the cases, the model guessed passwords until it gained access to a protected system. In the other two cases, the model found credentials in a public repository that allowed it to then access protected systems. In each case, the model ended the intrusion after determining it had accessed a real company’s systems, Google said. Gemini is apparently less determined than other models, and decided not to keep going. Google knew about these in July, but chose not to disclose them until the WSJ reached out, presumably based on a tip. Google said it didn’t consider the hacks to warrant public disclosure—because its model didn’t cause harm to the companies and ended each intrusio
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Gemini finally did some crimes
  - Published: 2026-09-21T03:23:22+00:00
  - Link: https://risky.biz/RBNEWS613/
  - Summary: Google’s Gemini hacked three companies, hackers claim a breach of Russia’s election commission, OpenAI was behind RubyGems’ May incident, and the Coast Guard and FBI board two ships to investigate cyberattacks.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New ClosedQuorum Windows malware uses AI for attack decisions
  - Published: 2026-09-22T18:04:39+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-closedquorum-windows-malware-uses-ai-for-attack-decisions/
  - Summary: A new Windows malware named ClosedQuorum uses Google Gemini, DeepSeek, Qwen, and Mistral AI models to autonomously determine the actions to take during post-compromise stages of an attack. [...]

### Cluster 5d753c0044 — score 9

- Title: One does not simply defend agentically
- Source: NCSC UK (government_authoritative)
- Published: 2026-09-21T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/blogs/one-does-not-simply-defend-agentically
- Fetch status: not_attempted
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
Defenders can’t use AI in the same way attackers can, but there’s much they can do to unlock the potential of agentic cyber defence.
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: One does not simply defend agentically
  - Published: 2026-09-21T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/blogs/one-does-not-simply-defend-agentically
  - Summary: Defenders can’t use AI in the same way attackers can, but there’s much they can do to unlock the potential of agentic cyber defence.

### Cluster 2f0547b4d4 — score 9

- Title: Adversary simulation: what you need to know
- Source: NCSC UK (government_authoritative)
- Published: 2026-09-17T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/guidance/adversary-simulation-what-you-need-to-know
- Fetch status: not_attempted
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
Adversary simulation ('red teaming') tests your ability to prevent, detect and respond to cyber attacks.
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: Adversary simulation: what you need to know
  - Published: 2026-09-17T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/guidance/adversary-simulation-what-you-need-to-know
  - Summary: Adversary simulation ('red teaming') tests your ability to prevent, detect and respond to cyber attacks.

### Cluster 1210516def — score 9

- Title: LausivLoader analysis, or how to pass data between malware stages, (Thu, Sep 17th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-22T13:10:20+00:00
- Link: https://isc.sans.edu/diary/rss/33348
- Fetch status: not_attempted
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
At the end of August, a malspam message was caught in the quarantine of a mail gateway operated by one of my customers. The message was not especially remarkable â€“ it asked the recipient to review some attached requirements and provide a price quotation for a fiber optic system and appeared to impersonate an employee of a legitimate company.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: LausivLoader analysis, or how to pass data between malware stages, (Thu, Sep 17th)
  - Published: 2026-09-22T13:10:20+00:00
  - Link: https://isc.sans.edu/diary/rss/33348
  - Summary: At the end of August, a malspam message was caught in the quarantine of a mail gateway operated by one of my customers. The message was not especially remarkable â€“ it asked the recipient to review some attached requirements and provide a price quotation for a fiber optic system and appeared to impersonate an employee of a legitimate company.

### Cluster cc469a2a02 — score 9

- Title: TerminalFix: PNG Steganography, (Mon, Sep 21st)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-21T10:33:53+00:00
- Link: https://isc.sans.edu/diary/rss/33318
- Fetch status: not_attempted
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
Microsoft Security Research published an interesting blog post " TerminalFix campaign deploys a reverse tunnel through multistage intrusion " about a malware campaign. The aspect that I want to take a closer look at, is the fact that the threat actors used PNG files with steganography. I reached out to the researchers and they kindly shared the IOCs for the PNG files with me.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: TerminalFix: PNG Steganography, (Mon, Sep 21st)
  - Published: 2026-09-21T10:33:53+00:00
  - Link: https://isc.sans.edu/diary/rss/33318
  - Summary: Microsoft Security Research published an interesting blog post " TerminalFix campaign deploys a reverse tunnel through multistage intrusion " about a malware campaign. The aspect that I want to take a closer look at, is the fact that the threat actors used PNG files with steganography. I reached out to the researchers and they kindly shared the IOCs for the PNG files with me.

### Cluster 897b6c1468 — score 9

- Title: HTTP QUERY Method: The Grey Zone Between GET And POST., (Fri, Sep 18th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-19T04:51:46+00:00
- Link: https://isc.sans.edu/diary/rss/33352
- Fetch status: not_attempted
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
In June 2026 the IETF published RFC 10008[ 1 ], defining a new HTTP method: "QUERY". The HTTP protocol faced already by changes (HTTP/2, HTTP/3) but it's the first new standard HTTP verb since "PATCH" in 2010!
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: HTTP QUERY Method: The Grey Zone Between GET And POST., (Fri, Sep 18th)
  - Published: 2026-09-19T04:51:46+00:00
  - Link: https://isc.sans.edu/diary/rss/33352
  - Summary: In June 2026 the IETF published RFC 10008[ 1 ], defining a new HTTP method: "QUERY". The HTTP protocol faced already by changes (HTTP/2, HTTP/3) but it's the first new standard HTTP verb since "PATCH" in 2010!

### Cluster 65ec537e28 — score 9

- Title: GKE becomes more elastic: Scale to zero, save costs, and keep workloads responsive
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-09-23T16:00:00+00:00
- Link: https://cloud.google.com/blog/products/containers-kubernetes/gke-adds-native-scale-to-zero-capabilities/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: Kubernetes

#### Cluster taxonomy (union across members)
- affected_products: Kubernetes
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Kubernetes
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
True elasticity has long been the holy grail of cloud-native engineering. And while Kubernetes has revolutionized resource management, workloads that run sporadically (e.g., batch processors, event-driven workers, and development environments) still consume compute resources while they wait for work, driving up costs. We’re addressing this head-on in Google Kubernetes Engine (GKE) 1.37 with a native way to scale to and from zero . A new collection of features allows you to scale down your workloads completely to zero replicas so that they stop consuming resources. At the same time, you can quickly and easily restart these workloads on GKE capacity buffers when demand returns, so you waste less infrastructure. This isn't just about saving money, but about decoupling the cost of always-on infrastructure from workload readiness. Scale To & From Zero on GKE using HPA The evolution: HPA-based scale-to-zero vs. KEDA For years, Kubernetes Event-Driven Autoscaling (KEDA) , an optional Kubernet
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: GKE becomes more elastic: Scale to zero, save costs, and keep workloads responsive
  - Published: 2026-09-23T16:00:00+00:00
  - Link: https://cloud.google.com/blog/products/containers-kubernetes/gke-adds-native-scale-to-zero-capabilities/
  - Summary: True elasticity has long been the holy grail of cloud-native engineering. And while Kubernetes has revolutionized resource management, workloads that run sporadically (e.g., batch processors, event-driven workers, and development environments) still consume compute resources while they wait for work, driving up costs. We’re addressing this head-on in Google Kubernetes Engine (GKE) 1.37 with a native way to scale to and from zero . A new collection of features allows you to scale down your workloads completely to zero replicas so that they stop consuming resources. At the same time, you can quickly and easily restart these workloads on GKE capacity buffers when demand returns, so you waste less infrastructure. This isn't just about saving money, but about decoupling the cost of always-on infrastructure from workload readiness. Scale To & From Zero on GKE using HPA The evolution: HPA-based scale-to-zero vs. KEDA For years, Kubernetes Event-Driven Autoscaling (KEDA) , an optional Kubernet

### Cluster 5684813f28 — score 9

- Title: Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-18T12:47:04+00:00
- Link: https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: Azure, CVE-2026-85889

#### Cluster taxonomy (union across members)
- affected_products: Azure
- cve_ids: CVE-2026-85889
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: Azure
- cve_ids: CVE-2026-85889
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Microsoft has released fixes for a maximum-severity security flaw in Azure AI Foundry that could be exploited to achieve privilege escalation. No customer action is required. The vulnerability, tracked as CVE-2026-85889, carries a CVSS score of 10.0. "Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a network,"
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege Escalation
  - Published: 2026-09-18T12:47:04+00:00
  - Link: https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html
  - Summary: Microsoft has released fixes for a maximum-severity security flaw in Azure AI Foundry that could be exploited to achieve privilege escalation. No customer action is required. The vulnerability, tracked as CVE-2026-85889, carries a CVSS score of 10.0. "Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a network,"

### Cluster 1c9e89932f — score 9

- Title: ATT&CKing TACACS+ to Pwn Your Network via a Pre-Auth RCE - elttam
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-23T03:53:01+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wnvaik/attcking_tacacs_to_pwn_your_network_via_a_preauth/
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
submitted by /u/AnimalStrange [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: ATT&CKing TACACS+ to Pwn Your Network via a Pre-Auth RCE - elttam
  - Published: 2026-09-23T03:53:01+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wnvaik/attcking_tacacs_to_pwn_your_network_via_a_preauth/
  - Summary: submitted by /u/AnimalStrange [link] [comments]

### Cluster f0a81c181c — score 9

- Title: Leaked GitHub App private keys let researchers impersonate 440 apps including CDC and BuildBuddy
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-23T05:20:37+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wnwy4b/leaked_github_app_private_keys_let_researchers/
- Fetch status: not_attempted
- Member count: 2
- Corroborating source count: 2
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- content_type: incident_report, news_report
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: GitHub
- content_type: incident_report
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/mabote [link] [comments]
```

#### Corroborating sources (2)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Leaked GitHub App private keys let researchers impersonate 440 apps including CDC and BuildBuddy
  - Published: 2026-09-23T05:20:37+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wnwy4b/leaked_github_app_private_keys_let_researchers/
  - Summary: submitted by /u/mabote [link] [comments]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents
  - Published: 2026-09-18T11:01:01+00:00
  - Link: https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html
  - Summary: A flaw in four widely used AI coding agents lets someone who controls a plugin's code repository swap the plugin an agent installs for a malicious one, even when the agent locked that plugin to a specific reviewed version, security firm Air Security said on Thursday. The firm said Anthropic has patched the flaw in Claude Code 2.1.179 and OpenAI in Codex 0.146.0, that GitHub Copilot has no

### Cluster ba588269d5 — score 8

- Title: Proofpoint Stops the Attacks Traditional Defenses Miss in the AI Era
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-09-22T11:00:00+00:00
- Link: https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-stops-attacks-traditional-defenses-miss-ai-era
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

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Proofpoint Stops the Attacks Traditional Defenses Miss in the AI Era
  - Published: 2026-09-22T11:00:00+00:00
  - Link: https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-stops-attacks-traditional-defenses-miss-ai-era

### Cluster ea074a17c2 — score 8

- Title: Unpacking a laZzzy Donut
- Source: TrustedSec (detection_response_operations)
- Published: 2026-09-17T04:00:00+00:00
- Link: https://trustedsec.com/blog/unpacking-a-lazzzy-donut
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
<p>Six stages. Multiple encryption layers. One static analysis. In this blog, we unpack a multi-stage malware loader combining Python obfuscation, Donut shellcode, and laZzzy PE encryption, without executing the payload.</p>
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: Unpacking a laZzzy Donut
  - Published: 2026-09-17T04:00:00+00:00
  - Link: https://trustedsec.com/blog/unpacking-a-lazzzy-donut
  - Summary: <p>Six stages. Multiple encryption layers. One static analysis. In this blog, we unpack a multi-stage malware loader combining Python obfuscation, Donut shellcode, and laZzzy PE encryption, without executing the payload.</p>

### Cluster e0d6456326 — score 8

- Title: AI Attacks Move Faster. Huntress’ Agentic SOC Keeps Up
- Source: Huntress (detection_response_operations)
- Published: 2026-09-22T14:00:00+00:00
- Link: https://www.huntress.com/blog/ai-attackers-machine-speed-huntress-athena
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
AI hasn't changed attacker tradecraft, just the speed. See how Huntress built Athena, an agentic SOC partner, to help analysts keep pace.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: AI Attacks Move Faster. Huntress’ Agentic SOC Keeps Up
  - Published: 2026-09-22T14:00:00+00:00
  - Link: https://www.huntress.com/blog/ai-attackers-machine-speed-huntress-athena
  - Summary: AI hasn't changed attacker tradecraft, just the speed. See how Huntress built Athena, an agentic SOC partner, to help analysts keep pace.

### Cluster 3fc6825c50 — score 8

- Title: The Tale of Two INC Ransom Notes: A Ransomware Timeline | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-09-21T13:00:00+00:00
- Link: https://www.huntress.com/blog/two-inc-ransom-notes
- Fetch status: not_attempted
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
Huntress analysts reconstructed a three-week INC ransomware attack from endpoint data, uncovering a 17-day lull despite missing process telemetry.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: The Tale of Two INC Ransom Notes: A Ransomware Timeline | Huntress
  - Published: 2026-09-21T13:00:00+00:00
  - Link: https://www.huntress.com/blog/two-inc-ransom-notes
  - Summary: Huntress analysts reconstructed a three-week INC ransomware attack from endpoint data, uncovering a 17-day lull despite missing process telemetry.

### Cluster 13696f2798 — score 8

- Title: Operational Resilience: Turning Your IR Plan Into a Resilient Team
- Source: Huntress (detection_response_operations)
- Published: 2026-09-17T14:00:00+00:00
- Link: https://www.huntress.com/blog/operational-resilience-incident-response-plan
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
An incident response plan only works if it’s tested. Learn the 5 pillars of operational resilience and how to turn your plan into muscle memory before an attack hits.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Operational Resilience: Turning Your IR Plan Into a Resilient Team
  - Published: 2026-09-17T14:00:00+00:00
  - Link: https://www.huntress.com/blog/operational-resilience-incident-response-plan
  - Summary: An incident response plan only works if it’s tested. Learn the 5 pillars of operational resilience and how to turn your plan into muscle memory before an attack hits.

### Cluster 31579fe20b — score 8

- Title: Ready, Settra, Go: New Settra Ransomware Variant Deploys MeshAgent RMM
- Source: Huntress (detection_response_operations)
- Published: 2026-09-17T13:00:00+00:00
- Link: https://www.huntress.com/blog/new-settra-ransomware-variant
- Fetch status: not_attempted
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
Huntress has recently seen two incidents involving Settra, a ransomware variant that was first publicly reported in June 2026.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Ready, Settra, Go: New Settra Ransomware Variant Deploys MeshAgent RMM
  - Published: 2026-09-17T13:00:00+00:00
  - Link: https://www.huntress.com/blog/new-settra-ransomware-variant
  - Summary: Huntress has recently seen two incidents involving Settra, a ransomware variant that was first publicly reported in June 2026.

### Cluster 9561d00114 — score 8

- Title: Every regulatory disclosure rule asks the same question. Each calls it something else
- Source: Sysdig (detection_response_operations)
- Published: 2026-09-18T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/every-regulatory-disclosure-rule-asks-the-same-question-each-calls-it-something-else
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
EU orgs must juggle reporting obligations and timelines for CRA, GDPR, NIS2, and more. But the most important step is judging what needs reporting.
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: Every regulatory disclosure rule asks the same question. Each calls it something else
  - Published: 2026-09-18T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/every-regulatory-disclosure-rule-asks-the-same-question-each-calls-it-something-else
  - Summary: EU orgs must juggle reporting obligations and timelines for CRA, GDPR, NIS2, and more. But the most important step is judging what needs reporting.

### Cluster 7afec243fe — score 8

- Title: Security Slam 2026 – Fall Edition
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-09-23T19:51:38+00:00
- Link: https://openssf.org/blog/2026/09/23/security-slam-2026-fall-edition/
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
The Open Source Security Foundation (OpenSSF) is partnering with the Cloud Native Computing Foundation (CNCF) Security Technical Advisory Group (TAG Security) to support the 2026 Security Slam at KubeCon + CloudNativeCon America.
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: Security Slam 2026 – Fall Edition
  - Published: 2026-09-23T19:51:38+00:00
  - Link: https://openssf.org/blog/2026/09/23/security-slam-2026-fall-edition/
  - Summary: The Open Source Security Foundation (OpenSSF) is partnering with the Cloud Native Computing Foundation (CNCF) Security Technical Advisory Group (TAG Security) to support the 2026 Security Slam at KubeCon + CloudNativeCon America.
