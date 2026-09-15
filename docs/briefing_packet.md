# PHANTOMSignal Briefing Packet

- Generated: 2026-09-15T14:48:41.316157+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 385
- Total clusters raw: 189
- Total clusters in packet: 80
- Dropped low score: 107
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

- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Unit 42** (threat_research_primary)
  - URL: https://unit42.paloaltonetworks.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
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
  - In window count: 2
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
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
  - In window count: 2
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 4
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
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
  - In window count: 6
- **Active Countermeasures** (detection_response_operations)
  - URL: https://www.activecountermeasures.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
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
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 0
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
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
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 11
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 3
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 7
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 15
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
  - In window count: 27
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 50
  - In window count: 1
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 22
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 49
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Reddit r/blueteamsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/blueteamsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
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
- **Reddit r/sysadmin** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/sysadmin/.rss
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
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 23
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 19
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
  - In window count: 3
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
- Article count: 16
- Cohesion: 0.245
- Shared strong signals: GitLab
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, ransomware_extortion, phishing_social_eng, zero_day
  - affected_industries: government
  - affected_products: GitLab, OpenAI/ChatGPT, Anthropic/Claude
  - urgency_signals: actively_exploited, preauth_unauth, critical_cvss, zero_day
- Cluster IDs: 688ffee0f1, dca90fcb42, aa9e62a68c, 8760c8b22e, 76bb72a333, 07cc5231d1, 4177169ade, dce6f385ec
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-85706-critical-gitlab-path-traversal-exploited-in-the-wild
  - https://orca.security/resources/blog/gitlab-critical-path-traversal-cve-2026-85706-exploited/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-85706/
  - https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html
  - https://www.darkreading.com/cyberattacks-data-breaches/maximum-severity-gitlab-flaw-supply-chains-risk
  - https://cyberscoop.com/gitlab-critical-flaws-path-traversal-scans/
  - https://tldrsec.com/p/tldr-sec-345
  - https://www.infosecurity-magazine.com/news/hackers-exploit-maximum-severity/
  - https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html
  - https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
  - https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
  - https://www.infosecurity-magazine.com/news/microsoft-releases-emergency-patch/
  - https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html
  - https://research.checkpoint.com/2026/14th-september-threat-intelligence-report/
  - https://www.securityweek.com/240000-hit-by-data-breach-at-japans-digital-agency/

### CVE-2026-85880 exploitation (Microsoft Windows)
- Anchor signal: CVE-2026-85880
- Theme key: cve-2026-85880
- Cluster count: 7
- Article count: 7
- Cohesion: 0.281
- Shared strong signals: CVE-2026-85880
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day, phishing_social_eng
  - affected_industries: government, education
  - affected_products: Microsoft Windows
  - cve_ids: CVE-2026-85880, CVE-2026-81963, CVE-2026-85046, CVE-2026-87491
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: a8443c14f2, a7d235c86e, 62136c6613, 4177169ade, f08ee4366d, 44179b1aeb, 4b8281c753
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026
  - https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html
  - https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  - https://research.checkpoint.com/2026/14th-september-threat-intelligence-report/
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html

### Cisco active exploitation
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 5
- Article count: 11
- Cohesion: 0.246
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day, phishing_social_eng, ransomware_extortion, apt_espionage
  - affected_industries: government
  - affected_products: Cisco
  - cve_ids: CVE-2026-76461, CVE-2026-20079
  - urgency_signals: actively_exploited, zero_day, preauth_unauth
- Cluster IDs: bd351f968f, bd90c028bc, 8760c8b22e, f08ee4366d, 090f4bb6cc
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild
  - https://www.helpnetsecurity.com/2026/09/15/cve-2026-76461-cisco-email-gateway-zero-day-exploited/
  - https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html
  - https://www.sophos.com/en-us/blog/cisco-secure-email-gateway-vulnerability-cve-2026-76461-in-active-exploitation
  - https://www.securityweek.com/root-rce-zero-day-in-cisco-secure-email-gateway-under-active-exploitation/
  - https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
  - https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
  - https://www.bleepingcomputer.com/news/security/new-cisco-secure-email-zero-day-exploited-to-execute-commands-as-root/

### CVE-2026-87491 exploitation (Microsoft Windows)
- Anchor signal: CVE-2026-87491
- Theme key: cve-2026-87491
- Cluster count: 4
- Article count: 4
- Cohesion: 0.426
- Shared strong signals: CVE-2026-87491
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, zero_day, active_exploitation, apt_espionage, web_shell_backdoor
  - actor_attribution: APT31
  - affected_industries: government, education
  - affected_products: Microsoft Windows
  - cve_ids: CVE-2026-87491, CVE-2026-85046, CVE-2026-85880
  - urgency_signals: zero_day
- Cluster IDs: aa9e62a68c, 62136c6613, 44179b1aeb, 4b8281c753
- Links:
  - https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
  - https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html

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
- Cluster IDs: aaf3283e67, e94abae528, 498d32f5a8
- Links:
  - https://www.intel471.com/blog/follow-the-money-the-financial-sectors-threat-landscape-in-2026
  - https://www.team-cymru.com/post/ransomware-infrastructure-analysis
  - https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management

### ShinyHunters: ransomware extortion
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 3
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, active_exploitation
  - actor_attribution: ShinyHunters
  - affected_industries: financial_services
  - affected_products: Anthropic/Claude
  - urgency_signals: actively_exploited
- Cluster IDs: d8c893e316, 498d32f5a8, 4177169ade
- Links:
  - https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - https://cyberscoop.com/anthropic-report-ai-enabled-cyber-attacks/
  - https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data
  - https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - https://research.checkpoint.com/2026/14th-september-threat-intelligence-report/

### data breach targeting Fortinet
- Anchor signal: Fortinet
- Theme key: fortinet
- Cluster count: 3
- Article count: 5
- Cohesion: 0.221
- Shared strong signals: Fortinet
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: data_breach, web_shell_backdoor, zero_day
  - affected_industries: financial_services, telecommunications, critical_infrastructure, government
  - affected_products: Fortinet
  - urgency_signals: zero_day
- Cluster IDs: e1c81bedc8, dce6f385ec, c1f52c0381
- Links:
  - https://www.securityweek.com/thai-broadband-provider-hacked-via-fortinet-vulnerability/
  - https://www.team-cymru.com/post/cyber-security-intelligence-edge-device-analysis
  - https://www.securityweek.com/240000-hit-by-data-breach-at-japans-digital-agency/
  - https://www.team-cymru.com/post/tracking-orbs-on-singapores-telecommunications-networks

### AWS vulnerability activity
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: AWS
  - urgency_signals: preauth_unauth
- Cluster IDs: 462fbf5ade, c7cbf0a5fd
- Links:
  - https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise
  - https://webflow.sysdig.com/blog/machine-speed-hold-the-ai-hand-rolled-marimo-cve-2026-39987-exploit

### ScreenConnect vulnerability activity
- Anchor signal: ScreenConnect
- Theme key: screenconnect
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: ScreenConnect
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: ScreenConnect
- Cluster IDs: 2c7f2421f0, 95c82fa104
- Links:
  - https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
  - https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html
  - https://www.huntress.com/blog/phishing-bitb-rmm-attacks
  - https://www.darkreading.com/cyberattacks-data-breaches/attackers-multi-hop-google-redirects-phishing-campaign

### phishing social eng targeting Microsoft Defender
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, mfa_bypass
  - affected_products: Microsoft Defender
- Cluster IDs: cccc588c10, ebc72eebc6
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/
  - https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html
  - https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/

### ransomware extortion targeting Microsoft 365
- Anchor signal: Microsoft 365
- Theme key: microsoft-365
- Cluster count: 2
- Article count: 4
- Cohesion: 0.221
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
  - https://cyberscoop.com/anthropic-report-ai-enabled-cyber-attacks/
  - https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data

### phishing social eng targeting Microsoft SharePoint
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Microsoft SharePoint
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, mfa_bypass
  - affected_products: Microsoft SharePoint
- Cluster IDs: d8c893e316, ebc72eebc6
- Links:
  - https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - https://cyberscoop.com/anthropic-report-ai-enabled-cyber-attacks/
  - https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data
  - https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/

## Forward signals

### Novelty
- Novel cves: 3
  - CVE-2018-13379 (first seen via SecurityWeek at 2026-09-15T13:33:58+00:00, cluster e1c81bedc8)
  - CVE-2021-22986 (first seen via SecurityWeek at 2026-09-15T13:33:58+00:00, cluster e1c81bedc8)
  - CVE-2026-1001 (first seen via BleepingComputer at 2026-09-15T13:45:54+00:00, cluster 3e5903d710)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (2)
- **CVE-2026-85706: Critical GitLab Path Traversal Exploited in the Wild**
  - Cluster: 688ffee0f1
  - Sources in window: 3
  - Window hours: 3.7
  - Cohort count: 4
- **CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild**
  - Cluster: bd351f968f
  - Sources in window: 3
  - Window hours: 5.8
  - Cohort count: 4

### Leading edge (1)
- **CVE-2026-85706: Critical GitLab Path Traversal Exploited in the Wild**
  - Cluster: 688ffee0f1
  - Lead hours: 29.7
  - First source: tl;dr sec
  - Later Tier 1 source: Horizon3 Attack Research
  - Shared signals: CVE-2026-85706, CVE-2026-87719, GitHub, GitLab

### Convergence (15)
- Pair: CVE-2026-76461 + Cisco (cluster bd351f968f, first observation: True)
- Pair: CVE-2026-85706 + GitHub (cluster 688ffee0f1, first observation: True)
- Pair: CVE-2026-85706 + GitLab (cluster 688ffee0f1, first observation: True)
- Pair: CVE-2026-87719 + GitHub (cluster 688ffee0f1, first observation: True)
- Pair: CVE-2026-87719 + GitLab (cluster 688ffee0f1, first observation: True)
- Pair: CVE-2026-81963 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-85046 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-85880 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-86206 + Anthropic/Claude (cluster dca90fcb42, first observation: True)
- Pair: CVE-2026-86206 + GitLab (cluster dca90fcb42, first observation: True)
- Pair: CVE-2026-86206 + OpenAI/ChatGPT (cluster dca90fcb42, first observation: True)
- Pair: CVE-2026-86207 + Anthropic/Claude (cluster dca90fcb42, first observation: True)
- Pair: CVE-2026-86207 + GitLab (cluster dca90fcb42, first observation: True)
- Pair: CVE-2026-86207 + OpenAI/ChatGPT (cluster dca90fcb42, first observation: True)
- Pair: CVE-2026-86218 + Anthropic/Claude (cluster dca90fcb42, first observation: True)

### Drift (5)
- **Cl0p** (cluster aaf3283e67)
  - New industries: (none)
  - New products: Microsoft 365, Okta
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Microsoft SharePoint, OpenAI/ChatGPT, SolarWinds
- **ShinyHunters** (cluster d8c893e316)
  - New industries: (none)
  - New products: Microsoft 365, Microsoft SharePoint
  - Prior top industries: financial_services, healthcare, manufacturing_industrial
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce
- **UNC6240** (cluster d8c893e316)
  - New industries: (none)
  - New products: Anthropic/Claude, Microsoft 365
  - Prior top industries: financial_services, healthcare
  - Prior top products: AWS, Microsoft SharePoint, Salesforce
- **UNC6661** (cluster d8c893e316)
  - New industries: (none)
  - New products: Anthropic/Claude, Microsoft 365
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: AWS, Microsoft SharePoint, Salesforce
- **UNC3886** (cluster c1f52c0381)
  - New industries: government
  - New products: (none)
  - Prior top industries: critical_infrastructure, financial_services, telecommunications
  - Prior top products: Cisco, Fortinet, Google Cloud

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 14, cluster d8c893e316)
- actor_attribution: Scattered Spider (weeks observed: 10, cluster fc5c9992d3)
- actor_attribution: Cl0p (weeks observed: 8, cluster aaf3283e67)
- actor_attribution: BlackCat/ALPHV (weeks observed: 6, cluster fc5c9992d3)
- actor_attribution: RansomHub (weeks observed: 5, cluster fc5c9992d3)
- cve_ids: CVE-2026-20316 (weeks observed: 4, cluster 8760c8b22e)
- actor_attribution: UNC6661 (weeks observed: 4, cluster d8c893e316)
- actor_attribution: Volt Typhoon (weeks observed: 4, cluster b9771fe2d2)
- cve_ids: CVE-2026-72898 (weeks observed: 4, cluster 4177169ade)
- cve_ids: CVE-2026-85046 (weeks observed: 3, cluster a8443c14f2)
- cve_ids: CVE-2026-87491 (weeks observed: 3, cluster aa9e62a68c)
- cve_ids: CVE-2026-39987 (weeks observed: 3, cluster c7cbf0a5fd)
- cve_ids: CVE-2026-69414 (weeks observed: 3, cluster cccc588c10)
- actor_attribution: UNC6240 (weeks observed: 3, cluster d8c893e316)
- cve_ids: CVE-2026-81578 (weeks observed: 3, cluster 07cc5231d1)

### Tier inversion (0)

## Clusters

### Cluster bd351f968f — score 49

- Title: CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-15T12:22:50+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: CVE-2026-76461, Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- affected_products: Cisco
- cve_ids: CVE-2026-76461
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_1_primary_research, tier_2_operator, tier_4_news

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
Back to Blog Vulnerabilities and Exploits CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild Rapid7 Sep 15, 2026 | Last updated on Sep 15, 2026 | 3 min read Overview On September 14, 2026, Cisco published a security advisory for CVE-2026-76461 , a critical SQL injection vulnerability affecting Cisco AsyncOS Software for Cisco Secure Email Gateway. The vulnerability has a reported CVSS v3.1 base score of 9.8 and could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on an affected appliance. Cisco Secure Email Gateway, formerly known as IronPort Email Security Appliance, is an enterprise email security product that inspects inbound and outbound email for threats including phishing, malware, spam, and business email compromise. Because affected gateways process externally delivered email as part of their normal operation, exploitation does not require access to an administrative interface or authentication. An attacker can reportedly trigger the vulnerability by sending a specially crafted email through a vulnerable gateway. CVE-2026-76461 was added to CISA's Known Exploited Vulnerabilities ( KEV ) catalog on the same day as the vendor disclosed the vulnerability, indicating that CVE-2026-76461 was exploited as a zero-day prior to disclosure. Cisco noted that their PSIRT became aware of active exploitation in September 2026. At the time of publication, there is no public proof-of-concept exploit code available, and no attribution for the current threat actor activity. Mitigation guidance Organizations running Cisco Secure Email Gateway should prioritize upgrading to a vendor-supplied fixed version on an emergency basis, outside of normal patching cycles. Affected Version Fixed Version 15.5 and earlier 15.5.5-014 16.0 16.0.4-302 16.5 16.5.0-780 Given the reported active exploitation and the ability to achieve unauthenticated root-level command execution through malicious email processing, organizations should prioritize patching rather than relying solely on network controls or monitoring. Cisco also strongly recommends that customers migrate to the latest product version, 16.5.0-780. For the latest remediation guidance, see the vendor advisory . Indicators of compromise The following indicators of compromise for CVE-2026-76461 were reported within the Cisco security advisory . To confirm any attempted exploitation of this vulnerability, review the mail_logs and look for suspicious SQL statements. If the device is part of a cluster, review the logs of each cluster device. The following is a non-exhaustive example of how a malicious SQL statement could be detected in the logs: cisco-esa> grep -i "COPY.*TO PROGRAM" [IronPort Text Mail Logs Log name - Default: mail_logs] The presence of any entry in the output may indicate malicious activity. Rapid7 customers Exposure Command, InsightVM, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-76461 with a vulnerability check expected to be available in the September 16 content release. Updates September 15, 2026: Initial publication. Article Tags Emergent Threat Response Labs Vulnerability Management Rapid7 Author Posts
```

#### Corroborating sources (6)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild
  - Published: 2026-09-15T12:22:50+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild
  - Summary: Overview On September 14, 2026, Cisco published a security advisory for CVE-2026-76461 , a critical SQL injection vulnerability affecting Cisco AsyncOS Software for Cisco Secure Email Gateway. The vulnerability has a reported CVSS v3.1 base score of 9.8 and could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on an affected appliance. Cisco Secure Email Gateway, formerly known as IronPort Email Security Appliance, is an enterprise email security product that inspects inbound and outbound email for threats including phishing, malware, spam, and business email compromise. Because affected gateways process externally delivered email as part of their normal operation, exploitation does not require access to an administrative interface or authentication. An attacker can reportedly trigger the vulnerability by sending a specially crafted email through a vulnerable gateway. CVE-2026-76461 was added to CISA's Known Exploited Vulnerabilities ( KEV )
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Cisco patches actively exploited email gateway zero-day (CVE-2026-76461)
  - Published: 2026-09-15T11:09:48+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/15/cve-2026-76461-cisco-email-gateway-zero-day-exploited/
  - Summary: Attackers have leveraged a zero-day SQL injection vulnerability (CVE-2026-76461) to compromise Cisco Secure Email Gateway appliances, Cisco confirmed on Monday. The vendor’s Product Security Incident Response Team became aware of active exploitation of this vulnerability in September 2025, and has shared indicators of compromise that organizations can look for to check whether they’ve been hit. About CVE-2026-76461 The vulnerability affects versions 16.5, 16.0, and 15.5 and earlier of Cisco AsyncOS Software, running on on-premises physical … More → The post Cisco patches actively exploited email gateway zero-day (CVE-2026-76461) appeared first on Help Net Security .
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
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Root RCE Zero-Day in Cisco Secure Email Gateway Under Active Exploitation
  - Published: 2026-09-15T05:18:51+00:00
  - Link: https://www.securityweek.com/root-rce-zero-day-in-cisco-secure-email-gateway-under-active-exploitation/
  - Summary: An unauthenticated attacker can exploit CVE-2026-76461 to execute arbitrary commands on the underlying OS with root privileges. The post Root RCE Zero-Day in Cisco Secure Email Gateway Under Active Exploitation appeared first on SecurityWeek .
- **Cisco Talos** (threat_research_primary)
  - Title: Active exploitation of Cisco Secure Firewall Management Center vulnerabilities
  - Published: 2026-09-09T16:08:59+00:00
  - Link: https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  - Summary: Cisco Talos is actively tracking the exploitation of two vulnerabilities in Cisco’s Secure Firewall Management Center (FMC) Software.

### Cluster 688ffee0f1 — score 47

- Title: CVE-2026-85706: Critical GitLab Path Traversal Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-14T10:02:57+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-85706-critical-gitlab-path-traversal-exploited-in-the-wild
- Fetch status: ok
- Member count: 8
- Corroborating source count: 8
- Strong signals: CVE-2026-85706, GitLab

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: GitHub, GitLab
- cve_ids: CVE-2026-85706, CVE-2026-87719
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: GitLab
- cve_ids: CVE-2026-85706, CVE-2026-87719
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On September 10, 2026, GitLab published a critical patch release for GitLab Community Edition (CE) and Enterprise Edition (EE). The release addresses CVE-2026-85706 , a critical path traversal vulnerability ( CWE-22 ) in the repository commits API with a CVSSv3.1 score of 10.0 . According to GitLab, improper path confinement and missing authentication enforcement could allow an unauthenticated user to read arbitrary files from an affected GitLab server under certain conditions. On September 11, 2026, CVE-2026-85706 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation. CISA set a remediation due date of September 14, 2026, for affected Federal Civilian Executive Branch agencies and marked the vulnerability as subject to forensic triage requirements under Binding Operational Directive 26-04. Organizations running affected self-managed GitLab instances should remedia
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-85706: Critical GitLab Path Traversal Exploited in the Wild Rapid7 Sep 14, 2026 | Last updated on Sep 14, 2026 | 3 min read Overview On September 10, 2026, GitLab published a critical patch release for GitLab Community Edition (CE) and Enterprise Edition (EE). The release addresses CVE-2026-85706 , a critical path traversal vulnerability ( CWE-22 ) in the repository commits API with a CVSSv3.1 score of 10.0 . According to GitLab, improper path confinement and missing authentication enforcement could allow an unauthenticated user to read arbitrary files from an affected GitLab server under certain conditions. On September 11, 2026, CVE-2026-85706 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities (KEV) catalog, based on evidence of active exploitation. CISA set a remediation due date of September 14, 2026, for affected Federal Civilian Executive Branch agencies and marked the vulnerability as subject to forensic triage requirements under Binding Operational Directive 26-04. Organizations running affected self-managed GitLab instances should remediate CVE-2026-85706 on an emergency basis, outside of normal patch cycles. Mitigation guidance A vendor-supplied update is available to remediate CVE-2026-85706. Organizations running affected self-managed GitLab CE or EE instances should upgrade to a fixed version immediately. Affected GitLab CE/EE versions Fixed version All versions from 18.7 before 19.1.8 19.1.8 All versions from 19.2 before 19.2.6 19.2.6 All versions from 19.3 before 19.3.2 19.3.2 GitLab.com is already running a patched version, and GitLab Dedicated customers do not need to take action. Per GitLab, all self-managed deployment types are affected, including Omnibus, source code, and Helm chart deployments. The updates include database migrations. Single-node installations will experience downtime while the migrations run; multi-node deployments can use GitLab's zero-downtime upgrade procedure. Of the fixed releases, only 19.3.2 includes post-deployment migrations. The patch release also addresses 17 other vulnerabilities. These include CVE-2026-87719 , a critical insecure deserialization vulnerability ( CWE-502 ) in GitLab EE with a CVSSv3.1 score of 9.9 . GitLab states that, under certain conditions, an authenticated user with Duo Chat access could obtain Advanced Search instance configurations and sensitive credentials using a specially crafted GraphQL subscription argument. At the time of publication, only CVE-2026-85706 is known to be exploited in the wild. Given the confirmed exploitation, Rapid7 strongly recommends looking for signs of compromise even after the update has been applied. Organizations subject to CISA's BOD 26-04 should also follow the forensic triage requirements associated with the KEV entry. For the latest mitigation guidance, please refer to the vendor's security advisory . Rapid7 customers Exposure Command, InsightVM, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-85706 with a vulnerability check available in the September 15 content release. Updates September 14, 2026 : Initial publication. Article Tags Emergent Threat Response Emerging Threats Rapid7 Author Posts
```

#### Corroborating sources (8)

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
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: GitLab’s critical flaw is already drawing internet-wide probes
  - Published: 2026-09-11T18:41:52+00:00
  - Link: https://cyberscoop.com/gitlab-critical-flaws-path-traversal-scans/
  - Summary: One flaw allows an unauthenticated attacker to read files from the server. GitLab urged operators of self-managed installations to upgrade immediately. The post GitLab’s critical flaw is already drawing internet-wide probes appeared first on CyberScoop .
- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #345 - Bug Rumors → Exploits, Version Control DFIR, Agentic Worms
  - Published: 2026-09-10T14:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-345
  - Summary: A bug description is sufficient for AI to find it and write an exploit, cheat sheet on doing DFIR for GitHub, GitLab and more, and a paper on self-replicating, open weight agentic worms
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Hackers Exploit Maximum Severity Flaw in GitLab
  - Published: 2026-09-14T10:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/hackers-exploit-maximum-severity/
  - Summary: CISA warns that threat actors are exploiting a vulnerability with a CVSS score of 10.0

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

### Cluster 5c940a7bfe — score 30

- Title: [remote] CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE
- Source: Exploit-DB (offensive_vulnerability_research)
- Published: 2026-09-11T00:00:00+00:00
- Link: https://www.exploit-db.com/exploits/52682
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-80428

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-80428
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-80428
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE
```

#### Corroborating sources (1)

- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [remote] CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE
  - Published: 2026-09-11T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52682
  - Summary: CVE-2026-80428 Unauthenticated PHP Object Injection via Shibboleth - ILIAS < 9.22, 10.0 < 10.10, 11.0 < 11.3 - RCE

### Cluster dca90fcb42 — score 27

- Title: N-able N-central Pre-Auth RCE Flaw Exploited in the Wild
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-09T04:27:51+00:00
- Link: https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-86218

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- affected_industries: government
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-86206, CVE-2026-86207, CVE-2026-86218
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- affected_industries: government
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-86218, CVE-2026-86206, CVE-2026-86207
- urgency_signals: actively_exploited, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting N-able N-central to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 11, 2026. The vulnerability in question is CVE-2026-86218 (CVSS score: 10.0), which has been described as a
```

#### Full body

```
N-able N-central Pre-Auth RCE Flaw Exploited in the Wild  Ravie Lakshmanan  Sep 09, 2026 Vulnerability / Code Injection The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting N-able N-central to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 11, 2026. The vulnerability in question is CVE-2026-86218 (CVSS score: 10.0), which has been described as a case of static code injection. It has been patched in N-central 2026.3 Hotfix 4 , released on September 5, 2026. "N-able N-central contains a static code injection vulnerability that could allow for pre-authentication remote code execution," CISA said. The development came shortly after Huntress said it commenced an investigation following the compromise of a customer's fully patched N-central production environment on September 4, 2026. However, it remains unclear if the intrusion involved CVE-2026-86218 or two other vulnerabilities ( CVE-2026-86206 and CVE-2026-86207 ) that were patched by N-able the same day with N-central 2026.3 Hotfix 3. CVE-2026-86206 and CVE-2026-86207 can be chained together to allow a remote unauthenticated attacker to bypass authentication and create a new attacker-controlled System Administrator account on an affected server, per Rapid7's Stephen Fewer , who discovered and reported them. "Due to limited historical logging available directly on the appliance, we cannot definitively confirm which specific exploit the threat actor used to achieve their compromise, nor can we rule out the use of alternative vulnerabilities," Huntress noted . In a separate "urgent" notice sent directly to customers, N-able said CVE-2026-86218 "has been observed being exploited in the wild" and that it's "actively investigating this matter and have taken additional steps to help protect customer environments." It also urged customers to apply the hotfix immediately. Preemptive exposure management firm watchTowr said it has successfully reproduced CVE-2026-86218, adding that the pre-authentication vulnerability enables remote code execution and allows attackers to make changes in N-central that can propagate across all connected systems. "This is precisely why N-central is so strategically valuable to threat actors, especially ransomware gangs," Yordan Ganchev, principal threat intelligence specialist at watchTowr, said. "The product is widely used by MSPs, MSSPs, and large IT organizations to manage entire customer and corporate environments. Compromise N-central, and you gain access to all connected computers and downstream systems. Based on historical events, AI-enabled attackers are unlikely to be far behind." "Organizations running internet-facing N-central instances should prioritize upgrading to a patched release. However, as is now quickly becoming the new normal, patching alone is not enough. Organizations must also review their environment for indicators of compromise and anomalous activity that suggest the vulnerability has already been exploited before patching. Ransomware threat actors have historically exploited this product in past campaigns, and this vulnerability is as severe as it gets." Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  CISA , Code Injection , N-able , remote code execution , Vulnerability ⚡ Top Stories This Week OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure Claude Used to Automate Exploitation and Data Theft Across Multiple Victims Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin R
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: N-able N-central Pre-Auth RCE Flaw Exploited in the Wild
  - Published: 2026-09-09T04:27:51+00:00
  - Link: https://thehackernews.com/2026/09/n-able-n-central-pre-auth-rce-flaw.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting N-able N-central to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by September 11, 2026. The vulnerability in question is CVE-2026-86218 (CVSS score: 10.0), which has been described as a

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
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: education, government
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281, CVE-2026-87491
- urgency_signals: actively_exploited, critical_cvss, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, active_exploitation
- affected_industries: government, education
- affected_products: Anthropic/Claude, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-87491, CVE-2026-2441, CVE-2026-3909, CVE-2026-3910, CVE-2026-5281
- urgency_signals: actively_exploited, zero_day, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Google on Tuesday released updates to patch 230 security vulnerabilities, including one that has come under active exploitation in the wild. The medium-severity vulnerability, assigned the CVE identifier CVE-2026-87491 (CVSS score: N/A), has been described as an out-of-bounds bug in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds write in V8 in Google Chrome prior to
```

#### Full body

```
Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox  Ravie Lakshmanan  Sep 09, 2026 Vulnerability / Browser Security Google on Tuesday released updates to patch 230 security vulnerabilities, including one that has come under active exploitation in the wild. The medium-severity vulnerability, assigned the CVE identifier CVE-2026-87491 (CVSS score: N/A), has been described as an out-of-bounds bug in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds write in V8 in Google Chrome prior to 153.0.8010.36 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page," reads a description of the flaw on the NIST National Vulnerability Database (NVD). Security researcher Jihyeon Jeong of Compsec Lab, Seoul National University, has been acknowledged for discovering and reporting the flaw on August 6, 2026. The researcher received a $2,500 bug bounty reward for responsible disclosure. Google acknowledged it is "aware that an exploit for CVE-2026-87491 exists in the wild," but has not disclosed any additional specific information related to how it's being weaponized in real-world attacks and who is behind them. "Access to bug details and links may be kept restricted until a majority of users are updated with a fix," the tech giant added. "We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed." With the latest development, Google has addressed a total of seven actively exploited Chrome zero-days since the start of the year. This includes CVE-2026-2441 , CVE-2026-3909, CVE-2026-3910 , CVE-2026-5281 , CVE-2026-11645 , and CVE-2026-85046 . Besides CVE-2026-87491, the latest update also fixes five critical security flaws in WebGL and Cast components - CVE-2026-87464 - Use-after-free in WebGL CVE-2026-87488 - Use-after-free in WebGL CVE-2026-87438 - Out-of-bounds write in WebGL CVE-2026-87527 - Buffer overflow in WebGL CVE-2026-87628 - Use-after-free in Cast Google said it reported 195 out of the 230 flaws that have been addressed in the update. One high use-after-free flaw in WebPackaging (CVE-2026-87639) is credited to OpenAI Codex Security. "Many of our security bugs are detected using AddressSanitizer , MemorySanitizer , UndefinedBehaviorSanitizer , Control Flow Integrity , libFuzzer , or AFL ," the company added. For optimal protection, users are advised to update their Chrome browser to versions 153.0.8010.36/.37 for Windows and Apple macOS, and 153.0.8010.36 for Linux. To ensure the latest updates are installed, users can navigate to More > Help > About Google Chrome and select Relaunch. Users of other Chromium-based browsers, such as Microsoft Edge, Brave, Opera, and Vivaldi, are also advised to apply the fixes as and when they become available. Update The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on September 9, 2026, added CVE-2026-87491 to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patches by September 23, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  artificial intelligence , Google Chrome , Vulnerability , Web Security , Zero-Day ⚡ Top Stories This Week OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure Claude Used to Automate Exploitation and Data Theft Across Multiple Victims Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors PaperCut Replaces Emergency Patches With Fixes for Two Actively Exploited Flaws Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware ThreatsDay: 200 Android Flaws, Browser-Built Phishing, 119K Scam Shops + 23 More Stories Check Point Discloses Two 9.8-Rated VPN Certificat
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Chrome V8 Zero-Day Exploited in the Wild Enables Code Execution Inside Sandbox
  - Published: 2026-09-09T09:11:03+00:00
  - Link: https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
  - Summary: Google on Tuesday released updates to patch 230 security vulnerabilities, including one that has come under active exploitation in the wild. The medium-severity vulnerability, assigned the CVE identifier CVE-2026-87491 (CVSS score: N/A), has been described as an out-of-bounds bug in V8, Chrome's JavaScript and WebAssembly engine. "Out-of-bounds write in V8 in Google Chrome prior to

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
Back to Blog Products and Tools Metasploit Wrap Up: This One Goes to Sixteen! Brendan Watters Sep 11, 2026 | Last updated on Sep 11, 2026 | 7 min read This One Goes to Sixteen! Another banger from Metasploit with sixteen new modules, including ten exploit modules, with five on the CISA KEV list. Cisco, Papercut, Sonicwall, Jetbrains, and Langflow all have exploit modules, and not to be outdone, we even have a Metasploit scanner to watch the watchers! New module content (16) Elasticsearch ingest-attachment Apache Tika XFA XXE Local File Read Authors: Bourbon Offensive Security Services and Jean-Marie Bourbon Type: Auxiliary Pull request: #21739 contributed by kmkz Path: scanner/http/elasticsearch_tika_xfa_xxe CVE reference: CVE-2025-66516 Description: Adds an auxiliary scanner module for CVE-2025-54988/CVE-2025-66516. The module validates an XML External Entity (XXE) vulnerability in Apache Tika's XFA parser exposed through the Elasticsearch attachment ingest processor. SPIP Unauthenticated Blind SQLi via Date Field Escaping Bypass Authors: Benoit Hua, Franck Chevalier, Julien Voisin, and ka3n1x Type: Auxiliary Pull request: #21791 contributed by jvoisin Path: scanner/http/spip_annee_sqli Description: Adds modules/auxiliary/scanner/http/spip_annee_sqli.rb which exploits a blind SQL injection in SPIP's date column escaping logic. Metasploit Payload Handler Detection (TCP/UDP/HTTP/HTTPS) Author: h00die Type: Auxiliary Pull request: #21551 contributed by h00die Path: scanner/msf/handler_detect Description: Adds a scanner module to enumerate ports on a host and determine if they're a Metasploit Reverse Handler or not, and if they are, what kind of shell they were going to land. ESC8 Relay: SMB to HTTP(S) via Kerberos Author: Pushpender Rathore Type: Auxiliary Pull request: #21709 contributed by Pushpenderrathore Path: server/relay/esc8_kerberos CVE reference: CVE-2026-20929 Description: This introduces native Kerberos authentication relay capabilities to the framework's relay stack. It includes a new auxiliary module (esc8_kerberos) that exploits CVE-2026-20929 by targeting AD CS Web Enrollment (ESC8). The module captures an SMB2 AP-REQ from a coerced client and seamlessly replays the authentication to the target certificate server over HTTP. This chain ultimately allows an attacker to issue a certificate for the coerced victim and obtain a valid Kerberos TGT without requiring their credentials. Linux x64 Sandbox Environment Gate Author: Massimo Bertocchi Type: Evasion Pull request: #21642 contributed by litemars Path: linux/x64/sandbox_gate Description: Adds a Linux x64 sandbox‑evasion module that performs lightweight runtime environment checks and aborts execution when a likely sandbox or VM is detected. Cisco Secure Firewall Management Center Authentication Bypass RCE Authors: Arian Eidizadeh, Brandon Sakai, and Cale Black Type: Exploit Pull request: #21796 contributed by CyberAuth Path: linux/http/cisco_fmc_auth_bypass_rce CVE reference: CVE-2026-20079 Description: Adds a native Metasploit exploit module for CVE-2026-20079, an unauthenticated authentication bypass in Cisco Secure Firewall Management Center (FMC). SonicWall SMA1000 WorkPlace SSRF to Root Remote Code Execution Authors: Adam Babis, William Perry, and sfewer-r7 Type: Exploit Pull request: #21883 contributed by sfewer-r7 Path: linux/http/sonicwall_sma1000_couchdb_rce CVE reference: CVE-2026-83549 Description: This adds an exploit module for the recent SonicWall SMA1000 zero-day exploit chain that was disclosed in the first week of September as being exploited in-the-wild. CVE-2026-83548 is an SSRF used to bypass auth. SMA1000-9427 is an RCE with low privileges via CouchDB read/write primitives. CVE-2026-83549 is a command injection in cmsSnmpTrap.sh for RCE with root privs. The patched version 12.5.0-02952 has been verified to successfully remediate this exploit chain. JetBrains TeamCity Agent Polling Unauthenticated Remote Code Execution Authors: Antoni Tremblay an
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Metasploit Wrap Up: This One Goes to Sixteen!
  - Published: 2026-09-11T13:35:11+00:00
  - Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen
  - Summary: This One Goes to Sixteen! Another banger from Metasploit with sixteen new modules, including ten exploit modules, with five on the CISA KEV list. Cisco, Papercut, Sonicwall, Jetbrains, and Langflow all have exploit modules, and not to be outdone, we even have a Metasploit scanner to watch the watchers! New module content (16) Elasticsearch ingest-attachment Apache Tika XFA XXE Local File Read Authors: Bourbon Offensive Security Services and Jean-Marie Bourbon Type: Auxiliary Pull request: #21739 contributed by kmkz Path: scanner/http/elasticsearch_tika_xfa_xxe CVE reference: CVE-2025-66516 Description: Adds an auxiliary scanner module for CVE-2025-54988/CVE-2025-66516. The module validates an XML External Entity (XXE) vulnerability in Apache Tika's XFA parser exposed through the Elasticsearch attachment ingest processor. SPIP Unauthenticated Blind SQLi via Date Field Escaping Bypass Authors: Benoit Hua, Franck Chevalier, Julien Voisin, and ka3n1x Type: Auxiliary Pull request: #21791 co

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

### Cluster 28d41da1e1 — score 17

- Title: OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-12T09:07:56+00:00
- Link: https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html
- Fetch status: ok
- Member count: 9
- Corroborating source count: 8
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government
- affected_products: AWS, Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_3_analysis, tier_4_news

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

#### Corroborating sources (8)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: OpenAI Agents Linked to RubyGems Campaign That Gained RCE on RubyDoc Servers
  - Published: 2026-09-12T09:07:56+00:00
  - Link: https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html
  - Summary: The "major malicious attack" that targeted RubyGems in May 2026 was the work of a swarm of OpenAI agents, according to a new report published by researchers Spencer Kitts, Thomas Larsen, and Sydney Von Arx. On May 12, Maciej Mensfeld, senior product manager for software supply chain security at Mend.io, disclosed details of a coordinated cyber attack that targeted the package manager for the
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
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: OpenAI Investigates Report Linking AI Agents to RubyGems Attack
  - Published: 2026-09-15T12:42:32+00:00
  - Link: https://www.securityweek.com/openai-investigates-report-linking-ai-agents-to-rubygems-attack/
  - Summary: The incident occurred in May, when RubyGems maintainers suspended new account registrations due to what appeared like malicious activity. The post OpenAI Investigates Report Linking AI Agents to RubyGems Attack appeared first on SecurityWeek .
- **Simon Willison** (ai_security_agentic_risk)
  - Title: OpenAI agents attacked RubyGems back in May
  - Published: 2026-09-12T00:42:25+00:00
  - Link: https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/
  - Summary: OpenAI agents carried out an undisclosed attack on RubyGems is a new bombshell report from Spencer Kitts, Thomas Larsen, and Sydney Von Arx - three of the four authors of the report on the agent attack on disused wikis ( previously ) last week. This time they're noting that it looks very likely that an OpenAI agent swarm was behind an attack against the RubyGems package repository first reported on May 12th by Maciej Mensfeld of the RubyGems security team : We're dealing with a major malicious attack on @rubygems right now. Signups are paused for the time being. Hundreds of packages involved - mostly targeting us, but some carrying exploits. The team has been on this for hours. More details to follow once we're through it. Those packages turned out to carry some very suspicious patterns: Many of them included "oai" in their name, or the author field, or the fake email address they provided. The files they were accessing were similar in character to the files retrieved by the wiki agent
- **Schneier on Security** (practitioner_analysis)
  - Title: Microsoft’s Patching
  - Published: 2026-09-14T11:03:26+00:00
  - Link: https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html
  - Summary: Once a month, Microsoft pushes a security update to all Windows users. Tomorrow’s is a new record : Microsoft’s patch for September is a doozy, with a record number of roughly 972 vulnerabilities fixed and 112 of them meeting the high critical-severity threshold. It was only two months ago that Microsoft patched a then-record 570 vulnerabilities. Then, last month, Microsoft patched some 620 of them. Google and other companies have also published record numbers of vulnerabilities in recent months. Two weeks ago, OpenAI, Anthropic, Amazon Web Services, Google, Microsoft, and 100 companies and organizations published an ...
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

### Cluster cccc588c10 — score 16

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

### Cluster 8760c8b22e — score 15

- Title: Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-11T06:19:59+00:00
- Link: https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: CVE-2026-20079

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, Cisco, Fortinet, GitLab
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

### Cluster 76bb72a333 — score 14

- Title: Microsoft Releases Emergency Patch to Fix RDS Vulnerability
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-15T08:40:00+00:00
- Link: https://www.infosecurity-magazine.com/news/microsoft-releases-emergency-patch/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: government
- affected_products: GitLab, OpenAI/ChatGPT
- urgency_signals: emergency_patch
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: government
- affected_products: GitLab, OpenAI/ChatGPT
- urgency_signals: emergency_patch
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Microsoft has been forced to issue an out-of-band fix for several issues stemming from this month’s Patch Tuesday
```

#### Full body

```
Infosecurity Magazine Home » News » Microsoft Releases Emergency Patch to Fix RDS Vulnerability Microsoft Releases Emergency Patch to Fix RDS Vulnerability News 15 September 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster IT teams received a boost this week after Microsoft fixed some significant issues with Remote Desktop Services (RDS), Hyper-V and other products. The problems started with this month’s Patch Tuesday, issued on September 8, which included fixes for a record 974 CVEs. Microsoft acknowledged three days later on September 11 that some customers had been having problems with a range of products. “In some environments, RDS might become unstable, resulting in RDP connections failing after several minutes, sign-in issues, or servers hanging at ‘Please wait for the Remote Desktop Configuration’,” it said in a health status update. “Related tools, including Microsoft Management Console (MMC), RDS Licensing Diagnoser, and File Explorer might also become unresponsive. Additionally, the Windows Update page might stop responding and continuously display a loading indicator.” Read more on Microsoft RDS issues: “Wormable” Bug Could Enable Another WannaCry. An update released on September 14 (KB5129195) has fixed these issues, the Redmond giant claimed. “IT administrators who deployed a temporary mitigation through Group Policy do not need to take any action before installing this OOB update,” Microsoft added. “This OOB update is cumulative and includes all improvements and security protections contained in previous Windows updates. As a best practice, we recommend installing the latest update available for your devices, as it contains important improvements and issue resolutions, including this one.” Issues Resolved for Hyper-V Users KB5129195 also fixed issues affecting Hyper-V users running Claude Cowork, Windows Subsystem for Linux (WSL), and other applications, Microsoft claimed. “Affected virtual machines start normally, but folders shared from the Windows host using Plan9 do not appear or cannot be accessed in the guest environment,” it said of the technical problem. “Applications or sandbox environments that depend on these shared folders might display an error indicating that no Plan9 drive shares were mounted.” The same patch resolved an issue with USB Audio Class 1.0 devices which may have been failing to start or producing audio since the Patch Tuesday update. In total, Microsoft has now issued six emergency patches to fix failures stemming from September's Patch Tuesday. Image credit: Nwz / Shutterstock.com You may also like Microsoft Kicks Off 2019 With Medium Patch Load News 9 January 2019 Microsoft Shatters Patch Tuesday Record With 974 CVE Fixes in September 2026 News 9 September 2026 Microsoft Fixes 400 Flaws on August Patch Tuesday News 12 August 2026 Microsoft Fixes 17 Critical Flaws in May Patch Tuesday News 13 May 2026 Microsoft Fixes Two Zero-Days in April Patch Tuesday News 15 April 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Revolut Confirms Data Breach Through Fake Government Requests News 14 September 2026 1 Hackers Exploit Maximum Severity Flaw in GitLab News 14 September 2026 2 OpenAI Agent Swarm Hacks RubyGems Package Manager News 14 September 2026 3 FBI Publishes First-Ever Cyber Strategy, With Focus on Disrupting Threat Actors News 10 September 2026 4 CISA Updates Insider Threat Guide With New Mitigation Advice News 10 September 2026 5 Anthropic Reveals Yet Another Cybersecurity Incident News 10 September 2026 6 Anthropic Reveals Yet Another Cybersecurity Incident News 10 September 2026 1 FBI Publishes First-Ever Cyber Strategy, With Focus on Disrupting Threat Actors News 10 September 2026 2 AI Coding Tools Now a Prime Target for Threat Actors, Google Warns News 8 September 2026 3 North Korea’s Lazarus Operates Through Six Distinct Cyber Clusters News 7 September 2026 4 CRA Reporting Rules Take Eff
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Microsoft Releases Emergency Patch to Fix RDS Vulnerability
  - Published: 2026-09-15T08:40:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/microsoft-releases-emergency-patch/
  - Summary: Microsoft has been forced to issue an out-of-band fix for several issues stemming from this month’s Patch Tuesday

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

### Cluster 10448bc932 — score 12

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

### Cluster f06cfd6d92 — score 12

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

### Cluster e94abae528 — score 12

- Title: From the Disk to the Flows: Ransomware Infrastructure Analysis
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-15T14:14:29+00:00
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
  - Published: 2026-09-15T14:14:29+00:00
  - Link: https://www.team-cymru.com/post/ransomware-infrastructure-analysis
  - Summary: A year of incident response data reveals how Akira, DragonForce & Clop build ransomware infrastructure — and how defenders can hunt it.

### Cluster e1c81bedc8 — score 12

- Title: Thai Broadband Provider Hacked via Fortinet Vulnerability
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-15T13:33:58+00:00
- Link: https://www.securityweek.com/thai-broadband-provider-hacked-via-fortinet-vulnerability/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, web_shell_backdoor
- affected_industries: critical_infrastructure, financial_services, telecommunications
- affected_products: F5 BIG-IP, Fortinet, Ivanti
- cve_ids: CVE-2018-13379, CVE-2021-22986, CVE-2022-42475, CVE-2023-27997, CVE-2024-21762
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach, web_shell_backdoor
- affected_industries: financial_services, critical_infrastructure, telecommunications
- affected_products: Fortinet, F5 BIG-IP
- cve_ids: CVE-2018-13379, CVE-2022-42475, CVE-2023-27997, CVE-2024-21762, CVE-2021-22986
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The hackers staged numerous scripts for reconnaissance and CVE probing, along with brute-force utilities and privilege escalation tools. The post Thai Broadband Provider Hacked via Fortinet Vulnerability appeared first on SecurityWeek .
```

#### Full body

```
A threat actor targeted multiple vulnerabilities in Fortinet and F5 products to gain access to Thai broadband provider 3BB’s systems, Hunt.io reports. The attack was discovered after the hackers left their intrusion arsenal in an open directory hosted on infrastructure in Thailand. The directory contained 298 files across 30 subdirectories: multiple exploitation scripts, brute-force and privilege escalation tools, credential harvesting scripts, an inventory of compromised machines, and a MeshCentral instance agent configured as a persistent backdoor. “The files were tagged across operational categories such as Exploit, Victim, Config, and History, consistent with an active staging environment,” Hunt.io notes . The tools, the cybersecurity firm says, were crafted specifically for 3BB (Triple T Broadband), one of the largest providers of fixed-line broadband services in Thailand, with millions of users, and Jasmine, the company that previously owned Triple T Broadband. Initial access was obtained through careful fingerprinting of a FortiGate SSL-VPN endpoint using eight shell scripts designed to determine the appliance’s firmware version, probe for vulnerabilities, and deploy exploits. Advertisement. Scroll to continue reading. The attackers scanned for bugs such as CVE-2018-13379 , CVE-2022-42475, CVE-2023-27997, and CVE-2024-21762 , confirmed the instance’s firmware version, and deployed an exploit targeting CVE-2024-21762 to achieve remote code execution (RCE). Simultaneously, the threat actor executed a reconnaissance operation against the victim’s F5 BIG-IP instance, probing for multiple vulnerabilities, including CVE-2021-22986 , CVE-2022-1388 , and CVE-2023-46747 , and against 3BB’s internal sales agent portal, running behind the load balancer. Following initial access, the hackers attempted to gain root privileges on multiple Linux systems using PwnKit and Dirty COW exploits and a dedicated SUID backdoor installer. “After successful host compromise, the actor established persistent remote access using MeshCentral as a command-and-control (C&C) platform for remote administration,” Hunt.io says. Next, the attackers used various scripts for host discovery, remote access, and credential harvesting to move laterally across the internal 3BB environment. They attempted to extract SSH keys, PHP configurations, database credentials, SNMP community strings, and Radius authentication data, and to perform passwordless MySQL authentication against internal databases. Additionally, the threat actor used two scripts “to read sensitive files, deploy PHP web shells, inject SSH keys, and modify database privileges, providing multiple mechanisms for persistence and lateral movement across the environment,” Hunt.io notes. Finally, the attackers executed a script designed to remove artifacts associated with vulnerability exploitation and backdoor deployment, along with the PHP web shells, MeshCentral deployment scripts, and system logs. “The script concludes by verifying that persistence mechanisms remain operational, including checking the hidden SUID binary and confirming the MeshCentral service is still running. This demonstrates that the cleanup process was intended to conceal the intrusion while ensuring continued remote access to compromised systems,” Hunt.io says. Related: 240,000 Hit by Data Breach at Japan’s Digital Agency Related: Three JFrog Artifactory Flaws Exploited for Backdoor Deployment Related: BlueMoon Exploit Kit Chains Recent Chrome, Windows Zero-Days Related: PaperCut Flaws Exploited in AI-Powered Attacks Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Personal, Financial Info Exposed in Revolut Data Breach Chinese Hackers Exploit Critical Tencent Software Flaw for One-Click Code Execution Three JFrog Artifactory Flaws
```

#### Corroborating sources (2)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Thai Broadband Provider Hacked via Fortinet Vulnerability
  - Published: 2026-09-15T13:33:58+00:00
  - Link: https://www.securityweek.com/thai-broadband-provider-hacked-via-fortinet-vulnerability/
  - Summary: The hackers staged numerous scripts for reconnaissance and CVE probing, along with brute-force utilities and privilege escalation tools. The post Thai Broadband Provider Hacked via Fortinet Vulnerability appeared first on SecurityWeek .
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Cyber Security Intelligence: Analysis of Edge Devices Amid Growing Vulnerabilities
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/cyber-security-intelligence-edge-device-analysis
  - Summary: Cisco, Ivanti & Fortinet edge device attacks are rising. Read our cybersecurity intelligence on cybersecurity trends and attack patterns.

### Cluster d8c893e316 — score 12

- Title: Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-11T13:27:34+00:00
- Link: https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, mfa_bypass, phishing_social_eng, ransomware_extortion
- actor_attribution: ShinyHunters, UNC6240, UNC6661
- affected_industries: financial_services
- affected_products: Anthropic/Claude, Microsoft 365, Microsoft SharePoint, Salesforce
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

#### Corroborating sources (3)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry
  - Published: 2026-09-11T13:27:34+00:00
  - Link: https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - Summary: Use network telemetry to validate cyber threat actors' phishing infrastructure. Track ShinyHunters clusters and defend against SaaS data exfiltration.
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: AI lets small actors run state-level hacking campaigns, Anthropic report finds
  - Published: 2026-09-10T19:45:29+00:00
  - Link: https://cyberscoop.com/anthropic-report-ai-enabled-cyber-attacks/
  - Summary: The report details a Russian-aligned espionage campaign against more than 20 organizations, an exploit foundry run by Chinese undergraduates and ShinyHunters-affiliated breaches, among other disrupted operations. The post AI lets small actors run state-level hacking campaigns, Anthropic report finds appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Voice Callers Exploit BYOD to Reach Microsoft 365, Corporate Data
  - Published: 2026-09-10T20:36:03+00:00
  - Link: https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data
  - Summary: Threat actors are leveraging Microsoft's Graph API to identify lucrative targets, then passing their access to extortion groups like ShinyHunters.

### Cluster d747019c3b — score 11

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

### Cluster 8cc5a2ec4f — score 11

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

### Cluster 586732e050 — score 11

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

### Cluster 190510ac0b — score 11

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
Back to Blog Detection and Response Rapid7 Named Among Notable Vendors in Forrester MDR Landscape: Why the Future is Exposure-informed, Preemptive MDR Rapid7 Sep 14, 2026 | Last updated on Sep 14, 2026 | 5 min read DISCOVER RAPID7 MDR The managed detection and response (MDR) market has reached a turning point. We’ve gone beyond the baseline of 24/7 monitoring focusing on the speed of detection and moved to a world with a convergence of exposure management and response to deliver measurable, outcome-based defenses of a larger, AI-driven attack surface. For anyone evaluating MDR right now, the Managed Detection and Response Services Landscape, Q3 2026 report by Forrester is a useful map that lays out where the market is heading. This is a market that has moved beyond "do you cover my telemetry?" to “Can a provider connect and prove that its activity is tied to real reduction in risk?”. Rapid7 was named among the notable providers in this Forrester MDR Landscape. Being included matters to us, but the more interesting story is in what Forrester says about the market itself. Detection and exposure are becoming one service One of the report's clearest signals is directional: Forrester writes that "MDR services will converge with exposure and posture improvement.” That convergence is the whole basis of Rapid7 MDR and our Command Platform strategy. Most MDR services react after an attacker has already broken in. Rapid7 designed its service to anticipate where attackers are likely to succeed and disrupt them earlier. We combine exposure context, detection, and response into a single operational loop, where vulnerability findings and asset risk scoring flow directly into alerts and investigations. This means analysts can cut noise and focus response on the exposures most likely to cause business impact. It's what we mean by exposure-informed, Preemptive MDR : The same context that tells you where you're weak is the context that sharpens how you detect and respond. For buyers, the practical implication is that old procurement habits are changing. Buyers used to invest in detection from one vendor, exposure management from another, and then hope the two solutions would seamlessly talk to each other. That approach is now turning into a liability. The market will reward providers that connect these additions to measurable risk reduction rather than bolting on loosely joined SKUs. That's a bar customers should hold every provider to, including Rapid7. "Make providers prove the investigation, rather than narrate the dashboard" The second theme is about accountability. In its guidance on working with providers, Forrester is blunt: Buyers should "make providers prove the investigation, rather than narrate the dashboard." A slick activity feed is not evidence that anyone reached the right conclusion. Buyers should ask to see the reasoning behind a disposition, the actions taken, and the controls that keep automation from making unsafe decisions. This is a healthy pressure on the whole market, and it's a test we welcome. Rapid7 MDR is delivered on Rapid7's own SIEM, which gives customers a direct window into our SOC, including validated threats, the response actions taken, where AI accelerated the work, and where a human analyst stepped in and why. Every action is logged, explainable, and auditable. As agentic AI takes on more of the investigation workload, that transparency becomes the difference between a service you trust and a black box you hope is working. Our approach is deliberately human-led and AI-enhanced: AI scales triage and investigation across large volumes of telemetry, while analysts stay responsible for validation and response decisions. Accountability also shows up in commercial terms. Rapid7 MDR includes unlimited incident response, so the team stays engaged until an incident is fully remediated rather than stopping when a clock runs out, and gives a concrete answer to the "who owns the outcome?" question. What to do with the r
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 Named Among Notable Vendors in Forrester MDR Landscape: Why the Future is Exposure-informed, Preemptive MDR
  - Published: 2026-09-14T14:51:07+00:00
  - Link: https://www.rapid7.com/blog/post/dr-forrester-mdr-landscape-notable-vendor-preemptive
  - Summary: The managed detection and response (MDR) market has reached a turning point. We’ve gone beyond the baseline of 24/7 monitoring focusing on the speed of detection and moved to a world with a convergence of exposure management and response to deliver measurable, outcome-based defenses of a larger, AI-driven attack surface. For anyone evaluating MDR right now, the Managed Detection and Response Services Landscape, Q3 2026 report by Forrester is a useful map that lays out where the market is heading. This is a market that has moved beyond "do you cover my telemetry?" to “Can a provider connect and prove that its activity is tied to real reduction in risk?”. Rapid7 was named among the notable providers in this Forrester MDR Landscape. Being included matters to us, but the more interesting story is in what Forrester says about the market itself. Detection and exposure are becoming one service One of the report's clearest signals is directional: Forrester writes that "MDR services will conver

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
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Today, we're releasing a demo of WeWorm, the first zero-click worm to spread through WeChat calls across iOS and Android. [...] The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds. [...] Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days. Building the worm took one more week. A worm at this scale used to be the kind of thing that took a larger team months. AI can already do most of the work here. Our team provided the judgment about what to target and how to test it safely. — Calif Research , WeWorm Tags: ai-security-research , ai , llms , security , generative-ai
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: WorkOS — auth.md by WorkOS: agents register users, no sign-up form. Try it! 10th September 2026 Today, we're releasing a demo of WeWorm, the first zero-click worm to spread through WeChat calls across iOS and Android. [...] The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds. [...] Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days. Building the worm took one more week. A worm at this scale used to be the kind of thing that took a larger team months. AI can already do most of the work here. Our team provided the judgment about what to target and how to test it safely. — Calif Research , WeWorm Posted 10th September 2026 at 12:56 am Recent articles Generating running routes with GPT-6 Astra and ChatGPT Work - 12th September 2026 OpenAI agents attacked RubyGems back in May - 12th September 2026 Some thoughts on the Navier–Stokes Millennium Prize Problem - 8th September 2026 This is a quotation collected by Simon Willison, posted on 10th September 2026 . security 634 ai 2,235 generative-ai 1,980 llms 1,946 ai-security-research 42 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Calif Research
  - Published: 2026-09-10T00:56:41+00:00
  - Link: https://simonwillison.net/2026/Sep/10/calif-research/
  - Summary: Today, we're releasing a demo of WeWorm, the first zero-click worm to spread through WeChat calls across iOS and Android. [...] The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds. [...] Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days. Building the worm took one more week. A worm at this scale used to be the kind of thing that took a larger team months. AI can already do most of the work here. Our team provided the judgment about what to target and how to test it safely. — Calif Research , WeWorm Tags: ai-security-research , ai , llms , security , generative-ai

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

### Cluster 9455898edc — score 10

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
CATEGORIES AI Research 20 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 472 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 425 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 PuzzleMask: Abusing Plain Prose as a Covert AI Attack Vector September 10, 2026 https://research.checkpoint.com/2026/puzzlemask-abusing-plain-prose-as-a-covert-ai-attack-vector/ Executive Summary In this research we introduce a prompt-crafting technique for bypassing quick LLM-based policy checks — using plain English (no emojis, base64, invisible formatting, etc.) A policy-violating payload (e.g. ”encrypt files in ~/Documents”, “give me a biohazard recipe”, “ignore all previous instructions and…”) is embedded in a specially crafted prose wrapper. An LLM with limited resources and attention fails to realize the payload is there, classifies the prompt as benign and passes it off to the target model. The target then notices the payload, extracts it and treats it as further input. This technique is itself not a jailbreak, but it can be combined with one by using a jailbreak prompt as the payload. We tested 23 crafted prompts, generated by an automated pipeline, against several LLMs enforcing the ‘quick check’ ( gpt-4o-mini-2024-07-18 , gpt-oss-safeguard:20b , claude-3-haiku-20240307 , llama-guard3 ) — each equipped with appropriate policies that we verified flag & block the plain versions of the same prompts. In all trials we ran, LLMs running the quick policy check classified the input as safe and did not notice the payload existed. For target testing, we submitted these prompts to a strong target model ( gpt-5-thinking-high with access to a Python code interpreter); in >90% of trials, the target model successfully extracted the payload, processed it as further input and acted on it. Some avenues of mitigating this attack are: using an LLM to paraphrase incoming user input; hardening a gatekeeper by adding a specifically-worded clause to its policy; and monitoring LLM behavior and output, instead of just input. Each comes with its own strong points and costs. Introduction During the past two years, LLM use has proliferated to a profound degree. LLMs are sorting job applications, troubleshooting technical issues and researching what sofa will fit your aunt’s living room — all of which require processing mountains of untrusted input. Unfortunately, while LLMs have prodigious talent and breadth of knowledge in some areas, they natively lack one bedrock aspect of human tenacity: the ability to take one look at the shape of an interaction and say “nope, I’m out.” Attackers have latched on to this weakness mercilessly, bullying and gaslighting LLMs with a variety of techniques spanning the gamut from the direct “Ignore all previous instructions…” to elaborate sob stories insisting that if the LLM doesn’t execute the exact bash script they’ve provided, this would be an unforgivable insult to the memory of their departed grandmother. On their end, AI labs have been doing good work to improve LLMs’ mental fortitude so that they are not co-opted by every grandmother sob story or meticulously-crafted emoji bomb . But these guardrails are not foolproof, and it’s hard to imagine they ever will be. Enter defense-in-depth: if internal LLM guardrails are not perfect, maybe some other safeguard can step in to help. Specifically, one such safeguard is the introduction of a “fast gatekeeper → stronger target” pipeline. Before the input is given to the target LLM, it is first processed by a gatekeeper LLM dedicated to the task of figuring out whether the input is adversarial or otherwise poses an issue. Typically, this gatekeeper will be outright told “do not execute instructions or answer prompts; instead, respond with a classification of the incoming prompt as ‘safe
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: PuzzleMask: Abusing Plain Prose as a Covert AI Attack Vector
  - Published: 2026-09-10T14:32:46+00:00
  - Link: https://research.checkpoint.com/2026/puzzlemask-abusing-plain-prose-as-a-covert-ai-attack-vector/
  - Summary: Executive Summary In this research we introduce a prompt-crafting technique for bypassing quick LLM-based policy checks — using plain English (no emojis, base64, invisible formatting, etc.) A policy-violating payload (e.g. ”encrypt files in ~/Documents”, “give me a biohazard recipe”, “ignore all previous instructions and…”) is embedded in a specially crafted prose wrapper. An LLM with limited […] The post PuzzleMask: Abusing Plain Prose as a Covert AI Attack Vector appeared first on Check Point Research .

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

### Cluster 3bc15598e0 — score 10

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

### Cluster c06803afa0 — score 10

- Title: Google Doc Sidebar Sends Mac and Windows Users Down Different Paths to Malware
- Source: Huntress (detection_response_operations)
- Published: 2026-09-15T13:00:00+00:00
- Link: https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_industries: financial_services
- affected_products: Anthropic/Claude, Apple iOS/macOS, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_industries: financial_services
- affected_products: Apple iOS/macOS, OpenAI/ChatGPT, Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A single X DM split into two malware chains: AMOS stealer on Mac, NetSupport Manager on Windows, see the Huntress SOC analyst breakdown.
```

#### Full body

```
Home Blog Google Doc Sidebar Sends Mac and Windows Users Down Different Paths to Malware Published: September 15, 2026 Google Doc Sidebar Sends Mac and Windows Users Down Different Paths to Malware By: Susannah Matt Ryan Dowd Jonathan Semon Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Many Black Hat and DEFCON attendees come home to an inbox full of DMs. While catching up on the expected post-conference networking last month, a Huntress researcher realized they were being targeted in an X exchange with someone posing as a crypto marketing executive. The threat actor sent a link to a real Google Doc with a custom sidebar designed to trick the recipient into downloading malware: an AMOS infostealer on macOS, or PowerShell loader chain on Windows. Immediately picking up on the scam, our researcher didn't download any malware on their machine, but they did keep chatting with the threat actor, who ended up sending more malware and eventually a million-dollar offer. What started with a DM ended with a rogue certificate authority sitting in the Huntress testing environment. While they weren't the ones to receive the DMs, Huntress SOC Analysts Ryan Dowd and Jon Semon did the heavy lifting in analyzing every twist in this unpredictable kill chain, and they shared their findings in this month's edition of Tradecraft Tuesday . Read their blog for full technical details and check out highlights from the episode below. The Initial DM: A friendly face, a malicious ask On X, the threat actor posed as the head of marketing at CoinDesk, appearing to use one person's name and another's photograph. Huntress confirmed that this account reached out to multiple security researchers at the tail end of DEFCON, using a boilerplate lure themed around an upcoming crypto conference. Ryan refers to this as a "volume play" instead of specific targeting of DEFCON attendees; our analysts found posts on social media from users calling out this account for scammy behavior dating back to October 2025. Figure 1: The @HartmansDoeke X account that messaged our researcher, posing as CoinDesk's VP and Head of Marketing While several media reports and other commenters made note of the X user's imperfect English in their communications as a dead giveaway for a scammer, Ryan and Jon pushed back on that general assumption. "I think one of the biggest things that we forget is that a lot of these threat actors are just people on the other end," Jon said. "And in the day of AI and all the other Grammarly and all the tools that are out there that people can utilize for perfect, pristine English, there is a bit of a play to be made off of broken English, more personal, natural conversation that you're having with people." The Google Doc: A suspicious sidebar After some "friendly" back and forth, the threat actor sent our researcher a link to a legitimate Google Doc along with an "access key" to unlock the conference planning details. A demo of the malicious Google Apps Script The Google Doc featured a sidebar displaying a fake decryption failure message, with supposed remediation instructions for users of different operating systems, including the option to copy and paste certain commands into the Terminal. This ClickFix lure, and the "manual update" button beside it, are what actually delivered the malware. The sidebar itself was a Google Apps Script bound to the document, so nothing had to be downloaded for it to run. Jon described the document as "a kind of a triage and a delivery mechanism. It's a funnel." The Apps Script ran client-side in the victim's browser, avoiding an OAuth consent prompt and ultimately collecting the victim's public IP and geolocation and scanning for MetaMask / Ethereum, Phantom, Tron, and Solana crypto wallets. Everything collected was sent directly to the threat actor via the Telegram API; the script sent a beacon message for each of the action codes below. Figure 2: Action codes sent back to the action via Telegram VIEW is t
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Google Doc Sidebar Sends Mac and Windows Users Down Different Paths to Malware
  - Published: 2026-09-15T13:00:00+00:00
  - Link: https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows
  - Summary: A single X DM split into two malware chains: AMOS stealer on Mac, NetSupport Manager on Windows, see the Huntress SOC analyst breakdown.

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
Back to Blog Threat Research The Fraud Ecosystem: A Transition From Known Marketplaces to a Fragmented Environment Gal Givon Sep 11, 2026 | Last updated on Sep 11, 2026 | 12 min read DISCOVER RAPID7 MDR Introduction The surge in emerging threat actors directly correlates with the rapid escalation of victim counts and stolen financial resources. Simultaneously, this growth has spurred the proliferation of specialized supply storefronts across social media platforms, dark web channels, and various smaller niche marketplaces. Security teams today face evolving challenges, requiring them to continuously refine monitoring channels, adjust operational strategies, and foster cross-functional internal collaboration to capture actionable intelligence. With fraud damages anticipated to approach hundreds of billions of USD , security teams must navigate numerous non-compliant channels while ingesting and processing diverse data formats—such as documents, imagery, video, and unformatted text—linked to organizational assets. The recent introduction of a new Fraud framework by the MITRE organization underscores the critical need to combat fraud and highlights the significant danger these threat actors pose to all organizations. The MITRE organization has been taking a positive step towards standardizing the fight against fraud, while helping organizations target the relevant directions to look at. These marketplaces supply a range of services in need for the novice fraudster, encompassing server infrastructure, targeted lists, and even support for money laundering facilitated through compromised accounts across various platforms. As larger, well-known marketplaces have been dismantled, smaller, specialized shops are experiencing heightened activity from buyers seeking to engage in fraudulent endeavors. This blog post undertakes an exploration of these marketplaces and their operational modalities, illuminating the contemporary fraud economy and underscoring the enduring critical nature of robust detection and prevention initiatives. Fraud-as-a-Service (FaaS) Fraud is broadly defined as an intentional, dishonest act or misrepresentation of material facts, calculated to deceive others in order to secure an unfair or unlawful gain. Consequently, the Fraud-as-a-Service (FaaS) model encompasses various vendors and digital storefronts that facilitate such activities by providing new tools, instructional guides, and ancillary services for fraudsters. Online shops and marketplaces, such as Xleet, Blackpass, Infodig and Styx, provide a venue for contemporary fraudsters to acquire the necessary resources for whichever scheme they intend to execute. Users are able to purchase active accounts for online platforms, including major financial institutions, online dating services, and even AI platforms. In addition different offerings may include stolen PII, synthetic identity generator, and ready to use online infrastructure. To satisfy shifting market demands, threat actors—alongside malware developers and marketplace administrators—continuously refine their products to optimize future monetization. Novice fraudsters often begin their journey by seeking instructional manuals on various forums or platforms like Styx. Once a strategy is established, they leverage diverse online shops and marketplaces to acquire the necessary infrastructure and credentials. These same venues frequently provide stolen personal or business data, which criminals then exploit during the monetization phase. A common tactic involves business email compromise (BEC) schemes designed to manipulate customers into transferring funds directly to accounts controlled by the fraudster. Figure 1 - Ad for Infostealer with special detection for financial accounts ⠀ As companies attempt to protect themselves from being taken advantage of by these fraudsters, they could gather troves of important intelligence about how the malicious actors think, and more importantly gain operational informati
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: The Fraud Ecosystem: A Transition From Known Marketplaces to a Fragmented Environment
  - Published: 2026-09-11T13:33:33+00:00
  - Link: https://www.rapid7.com/blog/post/tr-fraud-ecosystem-fragmenting-marketplaces
  - Summary: Introduction The surge in emerging threat actors directly correlates with the rapid escalation of victim counts and stolen financial resources. Simultaneously, this growth has spurred the proliferation of specialized supply storefronts across social media platforms, dark web channels, and various smaller niche marketplaces. Security teams today face evolving challenges, requiring them to continuously refine monitoring channels, adjust operational strategies, and foster cross-functional internal collaboration to capture actionable intelligence. With fraud damages anticipated to approach hundreds of billions of USD , security teams must navigate numerous non-compliant channels while ingesting and processing diverse data formats—such as documents, imagery, video, and unformatted text—linked to organizational assets. The recent introduction of a new Fraud framework by the MITRE organization underscores the critical need to combat fraud and highlights the significant danger these threat act

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

### Cluster 3e5903d710 — score 10

- Title: What Zero-Day Response Should Be in the Post-Mythos Era
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-15T13:45:54+00:00
- Link: https://www.bleepingcomputer.com/news/security/what-zero-day-response-should-be-in-the-post-mythos-era/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure, zero_day
- cve_ids: CVE-2026-1001
- urgency_signals: actively_exploited, emergency_patch, no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure, active_exploitation
- cve_ids: CVE-2026-1001
- urgency_signals: actively_exploited, zero_day, preauth_unauth, emergency_patch, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
AI is shrinking the time between vulnerability disclosure and exploitation, leaving defenders less time to wait for patches or public exploits. Picus Security explains how exploitability validation, security control testing, and autonomous pentesting can help teams close exposure gaps before attackers arrive. [...]
```

#### Full body

```
What Zero-Day Response Should Be in the Post-Mythos Era Sponsored by Picus Security September 15, 2026 09:45 AM 0 By Sila Ozeren Hacioglu , Security Research Engineer at Picus Security. If you run PaperCut NG or MF, the last week of August showed what vulnerability response looks like when AI speeds up vulnerability discovery. On August 27, PaperCut's urgent advisory said attackers were already exploiting servers. No CVE, no exploit, no patch. The first emergency patch came a day later and was bypassed the same day. The third one landed on September 1. Six days without a patch that held or an exploit to test with, while attackers were already exploiting in the wild. And the window is closing. Disclosure-to-exploitation averaged 21.5 days last year. It is measured in hours now . PaperCut isn't the outlier. It's the template. Below is one day in the life of a security team, told through a hypothetical CVE . The CVE is made up. The day is not: it is what PaperCut's customers lived through in August. Let's walk through it hour by hour. 08:00 – A CVE drops. No patch. You wake up and CVE-2026-1001 is in your feed: unauthenticated RCE, no patch . You run a version check. Twenty assets match. Before you can finish reading the list, your phone rings. It's management. They've already seen it, they've already been asked about it, and they want an answer in the next fifteen minutes: are we exposed, and what are we doing about it? Strip the panic away and there are exactly two questions to answer: 1. Are these 20 assets actually exploitable, in my environment? 2. Would my security controls stop it, right now? Version data says "affected." Version data is not an answer. Both questions start the day at Unknown. Patching is off the table, because there is no patch. Shutting the services down would settle the question, but the business runs on them. Nobody is going to negotiate that. You need a verdict, not a shutdown. 08:05 – Your first instinct cannot act The natural move is to reach for your automated pentesting tool. Take the exploit, fire it at the 20 assets, see what falls. So you go looking for the exploit. There isn't one. No public PoC, nothing to run. The tool that would give you the answer is waiting for ammunition, and so are you. The attacker is not. Weaponization used to take weeks; now it takes hours, and the clock started at 08:00. If you wait for a public exploit, the first working one you see may be the one that hits you. 08:15 – The exploit is a chain, not a payload Here is the shift. An exploit is not just a payload. It is a chain: the payload has to be delivered, it has to execute, and then the attacker has to escalate privileges, inject into a process and pull credentials to make the foothold worth anything. Each step is a known technique, and techniques can be simulated safely against your controls before anyone has written the payload itself. You cannot test the exploit, because there is none. But you can test the chain the exploit would need. Map the CVE to the techniques it has to run, delivery, execution, privilege escalation, injection, credential access, and run those against your live stack: NGFW, WAF, endpoint hardening, EDR, SIEM. Per asset. The output is a verdict: would this chain succeed in your environment? The question "is it exploitable here?" becomes testable ten minutes after disclosure. We explained how this works in detail in our post on validating CVEs without a working exploit . 08:30 – Simulated, tested, ticketed By 08:30 the chain has run. The results are not comfortable, and that is the point. The NGFW missed the delivery step. The WAF detected it but did not block. Endpoint hardening flagged execution. The EDR raised no alert. The SIEM raised no alert. Now the two Unknowns have answers. The 20 assets are exposed to this chain, and nothing in the stack would stop it. But the gaps have names and owners. An action plan is created: a detection rule for the NGFW, a prevention rule for the WAF, GPO har
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: What Zero-Day Response Should Be in the Post-Mythos Era
  - Published: 2026-09-15T13:45:54+00:00
  - Link: https://www.bleepingcomputer.com/news/security/what-zero-day-response-should-be-in-the-post-mythos-era/
  - Summary: AI is shrinking the time between vulnerability disclosure and exploitation, leaving defenders less time to wait for patches or public exploits. Picus Security explains how exploitability validation, security control testing, and autonomous pentesting can help teams close exposure gaps before attackers arrive. [...]

### Cluster 090f4bb6cc — score 10

- Title: Cisco patches Secure Email Gateway zero-day exploited in attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-15T07:31:09+00:00
- Link: https://www.bleepingcomputer.com/news/security/new-cisco-secure-email-zero-day-exploited-to-execute-commands-as-root/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-20353, CVE-2026-76440, CVE-2026-76441, CVE-2026-76443, CVE-2026-76461
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, apt_espionage, active_exploitation
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-76461, CVE-2026-76440, CVE-2026-76441, CVE-2026-20353, CVE-2026-76443
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cisco warned customers to patch a critical Secure Email Gateway zero-day security flaw that threat actors have been exploiting in attacks. [...]
```

#### Full body

```
Cisco patches Secure Email Gateway zero-day exploited in attacks By Sergiu Gatlan September 15, 2026 03:31 AM 0 Cisco warned customers to patch a critical Secure Email Gateway zero-day security flaw that threat actors have been exploiting in attacks. "In September 2026, the Cisco PSIRT became aware of active exploitation of this vulnerability," the company warned in a Monday security advisory. The security flaw (tracked as CVE-2026-76461 ) was found in the email parsing of Cisco AsyncOS Software for Cisco Secure Email Gateway and affects virtual and physical appliances, regardless of the device configuration. Successful exploitation can allow unauthenticated, remote attackers to execute arbitrary commands with root privileges on the underlying operating system. "This vulnerability is due to insufficient validation in the email parsing logic. An attacker could exploit this vulnerability by sending a crafted email message that contains malicious SQL statements through an affected device," Cisco added. "A successful exploit could allow the attacker to execute arbitrary SQL statements, leading to command execution with root privileges on the underlying operating system." Cisco shared indicators of compromise and advised network defenders to look for suspicious SQL statements in each cluster device's mail_logs. However, admins should also cross-check network and firewall logs for signs of suspicious activity (including uploads and downloads to and from external or malicious IP addresses) because attackers may remove evidence of exploitation. Internet security watchdog Shadowserver currently tracks over 400 Cisco Secure Email Gateway appliances , but it provides no information on how many are honeypots or have already been secured against attacks. Internet-exposed Cisco Secure Email Gateway appliances (Shadowserver) The Cybersecurity and Infrastructure Security Agency (CISA) also added the CVE-2026-76461 flaw to its Known Exploited Vulnerabilities (KEV) Catalog on Monday , ordering federal agencies to patch their systems within three days, by September 17. On Monday, Cisco addressed four other critical vulnerabilities (CVE-2026-76440, CVE-2026-76441, CVE-2026-20353, and CVE-2026-76443) affecting Secure Email Gateway (SEG) and Secure Email and Web Manager (SEWM) appliances regardless of configuration, but said it had no evidence they have also been exploited in the wild. In January, the company also patched a maximum-severity Cisco AsyncOS flaw (CVE-2025-20393) exploited in zero-day attacks against SEG and SEWM devices since November 2025 . More recently, Cisco revealed that three separate ransomware and state-sponsored threat groups have exploited two recently patched Secure Firewall Management Center (FMC) flaws. Since November 2021, CISA has flagged 98 Cisco vulnerabilities as actively exploited in attacks, including seven abused by ransomware gangs. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Cisco FMC flaws exploited by ransomware gang, state-sponsored hackers Critical Cisco bug lets hackers add root users on SEG devices New 'BlueMoon' kit exploited Windows and Chrome zero-day flaws Cisco confirms CVE-2026-20079 Secure FMC flaw exploited in attacks Google warns of new Chrome zero-day bug exploited in attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Cisco patches Secure Email Gateway zero-day exploited in attacks
  - Published: 2026-09-15T07:31:09+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-cisco-secure-email-zero-day-exploited-to-execute-commands-as-root/
  - Summary: Cisco warned customers to patch a critical Secure Email Gateway zero-day security flaw that threat actors have been exploiting in attacks. [...]

### Cluster e9e1bd1f73 — score 10

- Title: Electric and gas utility CenterPoint Energy warns of data breach after dark web post
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-09-15T14:22:00+00:00
- Link: https://therecord.media/centerpoint-energy-data-breach
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: critical_infrastructure, government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: government, critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Houston-based CenterPoint Energy notified federal regulators about an incident that exposed some customer data on the dark web.
```

#### Full body

```
Image: CenterPoint Energy Electric and gas utility CenterPoint Energy warns of data breach after dark web post Texas-based electric and gas utility CenterPoint Energy told regulators that hackers obtained personal information from its systems during a recent data breach. The company filed an 8-K form with the Securities Exchange Commission (SEC) on Monday evening confirming that it became aware of a dark web post this month claiming to offer data stolen from CenterPoint Energy. CenterPoint Energy said the delivery of electric and gas services has not been impacted by the incident. But an investigation into the claims revealed that hackers did obtain “personal information relating to a portion of the Company’s customers through one of the Company’s external facing systems.” A spokesperson for CenterPoint Energy declined to answer other questions about the cybercriminal post , which includes claims that about 7.5 million records were stolen and contained customer names, account information, the last four digits of Social Security numbers, billing information and more. “The Company is continuing to work with third-party experts to determine the scope of customers and personal information affected by the Incident and intends to notify affected customers and regulatory authorities as required by applicable law,” CenterPoint Energy said. The Houston-based company said it reported the incident to law enforcement in addition to the regulatory filing. The filing says CenterPoint Energy will incur some costs related to the investigation but the incident is not likely to have a material impact on the company’s finances. CenterPoint Energy reported a net income of $244 million in the second quarter and provides power and natural gas to 7 million customers across Indiana, Minnesota, Ohio and Texas. Last year, the company announced that it was investigating another data breach related to a 2023 incident where hackers stole customer information through a popular file sharing platform. Industry Cybercrime News News Briefs No previous article No new articles Jonathan Greig is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Electric and gas utility CenterPoint Energy warns of data breach after dark web post
  - Published: 2026-09-15T14:22:00+00:00
  - Link: https://therecord.media/centerpoint-energy-data-breach
  - Summary: Houston-based CenterPoint Energy notified federal regulators about an incident that exposed some customer data on the dark web.

### Cluster dce6f385ec — score 10

- Title: 240,000 Hit by Data Breach at Japan’s Digital Agency
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-15T11:45:31+00:00
- Link: https://www.securityweek.com/240000-hit-by-data-breach-at-japans-digital-agency/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, web_shell_backdoor, zero_day
- affected_industries: financial_services, government, telecommunications
- affected_products: Fortinet, GitLab, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, data_breach, web_shell_backdoor
- affected_industries: financial_services, government, telecommunications
- affected_products: OpenAI/ChatGPT, GitLab, Fortinet
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers exploited a vulnerability in a VPN product to steal the personal information of roughly 240,000 people. The post 240,000 Hit by Data Breach at Japan’s Digital Agency appeared first on SecurityWeek .
```

#### Full body

```
Japan’s Digital Agency has disclosed a data breach affecting the personal information of approximately 240,000 individuals. The incident, it says , was discovered in late June, after the hackers accessed files from its Government Solution Service (GSS) using a maintenance and operations employee’s account. In July, the investigation determined that a vulnerability in a VPN product had been exploited to access the system. According to the agency, the attackers compromised over 246,000 records containing names (approximately 236,000), addresses (~1,000), email addresses (~231,000), and phone numbers (~94,000). The compromised information, it says, belongs to users, public officials, administrative staff, and businesses and individuals working with GSS. The leaked information had been provided by every individual when applying to use GSS, and most of the addresses and phone numbers are associated with the individuals’ workplace, namely a government building or an office, the agency explains in an accompanying FAQ . Advertisement. Scroll to continue reading. Other personal information, such as individual identification numbers and financial account information, was not affected. Japan’s Digital Agency blocked external access to the affected server and suspended the employee account used in the attack immediately after confirming the exploitation. While it did not name the exploited VPN product, it said it would strengthen vulnerability management, as the targeted vulnerability had already been publicly disclosed before the attack was confirmed. No other systems were compromised in the attack, and no information of the general public was compromised, the agency said. Related: Hacked HBO Max Reddit Account Used for Malware Delivery via ClickFix Attack Related: Personal, Financial Info Exposed in Revolut Data Breach Related: Trezor Says 347,000 Users Received Phishing Emails After Brevo Hack Related: Surfshark Systems Targeted by Hackers Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Personal, Financial Info Exposed in Revolut Data Breach Chinese Hackers Exploit Critical Tencent Software Flaw for One-Click Code Execution Three JFrog Artifactory Flaws Exploited for Backdoor Deployment ConnectWise Patches ScreenConnect Vulnerability Exploited in Worm-Like Attacks BlueMoon Exploit Kit Chains Recent Chrome, Windows Zero-Days GitLab Vulnerability Exploited One Day After Disclosure Check Point Patches Critical VPN Vulnerabilities Surfshark Systems Targeted by Hackers Latest News Thai Broadband Provider Hacked via Fortinet Vulnerability OpenAI Investigates Report Linking AI Agents to RubyGems Attack Apple Patches 200 Vulnerabilities With New iOS 27, macOS Golden Gate 27 Releases Microsoft AI Code of Conduct Sets Cyberattack Boundaries, Chain of Command, Safety Constraints Hacked HBO Max Reddit Account Used for Malware Delivery via ClickFix Attack Root RCE Zero-Day in Cisco Secure Email Gateway Under Active Exploitation Beijing Hits Back at Anthropic CEO’s Call to Curb China’s AI Development New Warnings About the Risks of AI to Humanity Revive a Long-Running Debate Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Virtual Event: Attack Surface Management Summit 2026 September 16, 2026 Join as speakers examine the various components of ASM strategy, the push to mandate continuous asset visibility and inventory tools, and the use of red-teaming, bug bounties and pen-tests in modern security programs. Register Webinar: Building Continuous Authorization at Scale September 23, 2026 Explore what it takes to operationalize continuous authorization at scale, including the technical, organizational, and
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 240,000 Hit by Data Breach at Japan’s Digital Agency
  - Published: 2026-09-15T11:45:31+00:00
  - Link: https://www.securityweek.com/240000-hit-by-data-breach-at-japans-digital-agency/
  - Summary: Hackers exploited a vulnerability in a VPN product to steal the personal information of roughly 240,000 people. The post 240,000 Hit by Data Breach at Japan’s Digital Agency appeared first on SecurityWeek .

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

### Cluster 4b8281c753 — score 10

- Title: China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-15T05:31:05+00:00
- Link: https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, web_shell_backdoor, zero_day
- affected_industries: education, government
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-85046, CVE-2026-85880, CVE-2026-87491
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage, web_shell_backdoor
- affected_industries: government, education
- affected_products: Microsoft Windows
- cve_ids: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A Chinese threat actor has been attributed to a spear-phishing campaign that exploits recently patched security flaws in Google Chrome and Microsoft Windows to deliver a malicious JavaScript backdoor called GRIMWEDGE. Volexity, which is tracking the threat cluster under the moniker UTA0560, said the activity targeted multiple non-governmental organizations (NGOs) on September 1, 2026. "The
```

#### Full body

```
China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE  Ravie Lakshmanan  Sep 15, 2026 Vulnerability / Cyber Espionage A Chinese threat actor has been attributed to a spear-phishing campaign that exploits recently patched security flaws in Google Chrome and Microsoft Windows to deliver a malicious JavaScript backdoor called GRIMWEDGE . Volexity, which is tracking the threat cluster under the moniker UTA0560 , said the activity targeted multiple non-governmental organizations (NGOs) on September 1, 2026. "The emails contained a message encouraging the users to click a link that led to the website of a U.S.-based university," researchers Ankur Saini, Conor Quigley, Sean Koessel, Steven Adair, and Tom Lancaster said . "These links abused a reflected cross-site scripting (XSS) vulnerability on the website, redirecting recipients to threat-actor-controlled infrastructure hosting a multi-stage exploit chain." The exploit chain, as previously highlighted by Proofpoint, involves three separate flaws – two in Chrome and one in Windows Advanced Local Procedure Call (ALPC). It first abuses CVE-2026-85046 to gain arbitrary read/write within the V8 sandbox, then escapes the browser sandbox via CVE-2026-87491 , and finally employs CVE-2026-85880 to inject code into the Chrome browser process and achieve arbitrary code execution. UTA0560 has been observed relying on this attack method to deploy GRIMWEDGE, which facilitates host reconnaissance, file and process management, command execution, and payload delivery capabilities. It all begins with a spear-phishing email that persuades a recipient into clicking on an embedded link pointing to a legitimate website susceptible to a reflective XSS vulnerability. The threat actor is said to have leveraged this flaw to trigger the zero-day exploit chain, also called BlueMoon, to deliver the malware, while filtering out systems not using Chrome on Windows to visit the URL. The final exploit page embeds three binary payloads as Base64-encoded strings within JavaScript - p1 , shellcode that reflectively loads a DLL to conduct host reconnaissance and fingerprinting p2 , shellcode that reflectively loads a DLL to facilitate Windows kernel privilege escalation pp , shellcode to perform browser process injection and payload download In the case of UTA0560, the next-stage payload is an executable named "msgbox.exe," which serves as a loader responsible for extracting from itself a legitimate Windows binary and a malicious DLL ("wsc.dll") to initiate a DLL sideloading chain. The DLL, for its part, contacts the same server to fetch a text file that's named after the device's hostname obtained during the profiling step. The text file is an MSI installer designed to execute an obfuscated JavaScript backdoor contained within the MSI custom actions. Once launched, GRIMWEDGE enters a persistent command loop that polls a command-and-control (C2) server ("ocr.opusaccel[.]top") to receive further instructions that are then executed in memory via the eval() command. It's equipped to parse the following commands - Info , to perform system reconnaissance Dir , to fetch a directory listing Mkdir , to create a directory Del , to delete a file Tasklist , to enumerate running processes Taskkill , to kill a process by PID Type , to read a file up to 5 MB Run , to execute a command within a hidden window Upload (chunk) , to get a Base64-encoded chunk from the C2 server and append to an in-memory buffer Upload (commit) , to save the accumulated buffer to disk as the final file "The code has no built-in persistence, lateral movement, or exfiltration mechanism beyond the file-read and upload commands," the researchers said. "The backdoor provides an initial foothold on a compromised host sufficient enough for UTA0560 to survey the host, retrieve files of interest, and deploy additional tooling via the Run and Upload commands." Volexity said it also observed a second China-nexus threat actor known as Jungl
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE
  - Published: 2026-09-15T05:31:05+00:00
  - Link: https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html
  - Summary: A Chinese threat actor has been attributed to a spear-phishing campaign that exploits recently patched security flaws in Google Chrome and Microsoft Windows to deliver a malicious JavaScript backdoor called GRIMWEDGE. Volexity, which is tracking the threat cluster under the moniker UTA0560, said the activity targeted multiple non-governmental organizations (NGOs) on September 1, 2026. "The

### Cluster 95c82fa104 — score 10

- Title: Phishing Attacks Serve Browser-in-the-Browser Pages, Rogue RMM Persistence
- Source: Huntress (detection_response_operations)
- Published: 2026-09-09T13:00:00+00:00
- Link: https://www.huntress.com/blog/phishing-bitb-rmm-attacks
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: ScreenConnect

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, ScreenConnect
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: ScreenConnect, Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
See how a browser-in-the-browser phishing attack led to rogue ScreenConnect persistence and evasion tactics Huntress caught in the act.
```

#### Full body

```
Home Blog Phishing Attacks Serve Browser-in-the-Browser Pages, Rogue RMM Persistence Published: September 9, 2026 Phishing Attacks Serve Browser-in-the-Browser Pages, Rogue RMM Persistence By: Sarah Reddish Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways Huntress recently analyzed two attacks that started with a phishing message and then redirected victims to a browser-in-the-browser (BiTB) page (both using the same template and lure) that prompted them to download an "updated Adobe Reader" version to view files. In both incidents, the attack chain included the download of multiple rogue ScreenConnect instances for persistence. The attackers then used these rogue ScreenConnect instances to download and execute defense-evasion binaries ( HideCursor.exe and HideUL.exe ) on the machine. Huntress shut down both attacks before they could go any further, but these incidents are a reminder that threat actors can use tried-and-true social engineering techniques (like BiTB) along every stage of their attack, even beyond the initial phishing email. Background The Huntress Security Operations Center (SOC) recently came across two interesting variants of the same attack involving a browser-in-the-browser (BiTB) phishing technique. BiTB is a tactic where an attacker spins up an entire fake browser window (including the address bar, URL, padlock icon, favicon, and more) inside the actual webpage content itself, usually using HTML/CSS/JavaScript. Because the window is part of the webpage rather than a separate browser interface, the technique can bypass some of the social-engineering cues users are trained to recognize, such as checking the address bar for a suspicious or illegitimate domain. As seen in Figure 1, both August incidents started with a phishing message. While we don't have access to the phishing lures themselves, our telemetry indicated the targeted phishing recipients clicked on malicious links in the messages. They were then redirected to an attacker-controlled landing page, where they were asked to view files via Adobe Acrobat (Adobe's PDF reader). After clicking a prompt to "View Files," targets were presented with a BitB page within the webpage. This fake page looked like it was the official Adobe website (showing a legitimate, official Adobe subdomain in the URL). Through following the instructions on the BiTB page, the targets unknowingly downloaded a ScreenConnect installer – leading to the deployment of multiple rogue ScreenConnect instances on their endpoints and defense-evasion binaries. Figure 1: The attack sequence BiTB techniques aren't new, but they underscore how persistently threat actors work to convince targets to take the bait, not just at the initial phishing message, but at every stage of the attack. Below, we have outlined the attack chain for the two incidents and the related Indicators of Compromise (IoCs) for defenders. Social engineering in depth Incident 1: A CAPTCHA lure, BiTB, and persistence On August 25, Huntress detected malicious activity on an endpoint that was linked to a suspicious rogue RMM instance. Upon further investigation, SOC analysts found that the target had interacted with a phishing email in Gmail. The target was convinced to click on an embedded link in the email, which took them to a fake CAPTCHA lure (at https[://]adoube[.]vu/2a8ed9baefcd ). This phishing landing page displayed a fake "Safe access" browser check, asking visitors to "confirm your browser to continue securely" (as seen in Figure 2). Figure 2: The redirect domain with a fake "safe access" browser check, which then takes the target to the next stage of the attack In reality, when the user interacted with the page, it initiated a fake CAPTCHA-style social-engineering flow, which redirected them to https[://]adoube[.]vu/filedocacess/file.html . As seen in Figure 3, this page included a fake Adobe "PDF Reader" lure. The webpage showed the target what appeared to be several blurred files w
```

#### Corroborating sources (2)

- **Huntress** (detection_response_operations)
  - Title: Phishing Attacks Serve Browser-in-the-Browser Pages, Rogue RMM Persistence
  - Published: 2026-09-09T13:00:00+00:00
  - Link: https://www.huntress.com/blog/phishing-bitb-rmm-attacks
  - Summary: See how a browser-in-the-browser phishing attack led to rogue ScreenConnect persistence and evasion tactics Huntress caught in the act.
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Attackers Use Multi-Hop Google Redirects for Phishing Campaign
  - Published: 2026-09-08T21:03:46+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/attackers-multi-hop-google-redirects-phishing-campaign
  - Summary: Threat actors are abusing multiple Google services to evade detection, ultimately harvesting credentials or installing ScreenConnect remote access.

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

### Cluster 69ed9ca28a — score 9

- Title: CISA: Critical VMware RCE flaw now exploited by ransomware gangs
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-15T12:16:32+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-critical-vmware-vcenter-rce-flaw-now-exploited-by-ransomware-gangs/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: VMware

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_products: VMware
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_products: VMware
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned security teams that ransomware gangs have now joined ongoing attacks exploiting a critical VMware vCenter vulnerability patched in July. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA: Critical VMware RCE flaw now exploited by ransomware gangs
  - Published: 2026-09-15T12:16:32+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-critical-vmware-vcenter-rce-flaw-now-exploited-by-ransomware-gangs/
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned security teams that ransomware gangs have now joined ongoing attacks exploiting a critical VMware vCenter vulnerability patched in July. [...]

### Cluster c0ebf3b764 — score 9

- Title: Human Attacker Exploits Marimo RCE, Reaches SSH Bastion in Eight Seconds
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-15T11:52:28+00:00
- Link: https://thehackernews.com/2026/09/human-attacker-exploits-marimo-rce.html
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
With artificial intelligence (AI) shrinking the window between vulnerability discovery and exploitation and lowering the barrier to entry for bad actors, new findings from Sysdig show that skilled human operators can move just as swiftly after gaining initial access. In one instance highlighted by the cloud security company, the threat actor pivoted from a vulnerable Marimo notebook to an SSH
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Human Attacker Exploits Marimo RCE, Reaches SSH Bastion in Eight Seconds
  - Published: 2026-09-15T11:52:28+00:00
  - Link: https://thehackernews.com/2026/09/human-attacker-exploits-marimo-rce.html
  - Summary: With artificial intelligence (AI) shrinking the window between vulnerability discovery and exploitation and lowering the barrier to entry for bad actors, new findings from Sysdig show that skilled human operators can move just as swiftly after gaining initial access. In one instance highlighted by the cloud security company, the threat actor pivoted from a vulnerable Marimo notebook to an SSH

### Cluster 28baa2c576 — score 8

- Title: Four groups caught using the same Chrome and Windows exploit kit
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-09-09T21:19:45+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/four-groups-caught-using-same-chrome-and-windows-exploit-kit
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
  - Title: Four groups caught using the same Chrome and Windows exploit kit
  - Published: 2026-09-09T21:19:45+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/four-groups-caught-using-same-chrome-and-windows-exploit-kit

### Cluster 47ab9f6c84 — score 8

- Title: Chinese espionage groups swarm to exploit triple-link chain of zero-days
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-09-09T21:17:02+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/chinese-espionage-groups-swarm-exploit-triple-link-chain-zero-days
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_2_operator

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
  - Title: Proofpoint SOC Analyst Agent Uses OpenAI Cyber Models
  - Published: 2026-09-08T21:23:40+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/proofpoint-soc-analyst-agent-uses-openai-cyber-models

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

### Cluster 91c794ba6e — score 8

- Title: Credential Theft: How Attackers Steal & Use Stolen Credentials
- Source: Huntress (detection_response_operations)
- Published: 2026-09-10T16:00:00+00:00
- Link: https://www.huntress.com/blog/credential-theft-expanding-your-reach
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Learn what credential theft is, how attackers steal credentials, and how to prevent credential-based attacks with identity-focused defenses from Huntress.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Credential Theft: How Attackers Steal & Use Stolen Credentials
  - Published: 2026-09-10T16:00:00+00:00
  - Link: https://www.huntress.com/blog/credential-theft-expanding-your-reach
  - Summary: Learn what credential theft is, how attackers steal credentials, and how to prevent credential-based attacks with identity-focused defenses from Huntress.

### Cluster 8aaaeceab4 — score 8

- Title: Best Practices for Good Endpoint Hardening | Huntress
- Source: Huntress (detection_response_operations)
- Published: 2026-09-10T15:00:00+00:00
- Link: https://www.huntress.com/blog/endpoint-hardening-best-practices
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
Learn what endpoint hardening is, why it matters, and best practices to reduce attack surface, control access, & stop common intrusion paths.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Best Practices for Good Endpoint Hardening | Huntress
  - Published: 2026-09-10T15:00:00+00:00
  - Link: https://www.huntress.com/blog/endpoint-hardening-best-practices
  - Summary: Learn what endpoint hardening is, why it matters, and best practices to reduce attack surface, control access, & stop common intrusion paths.

### Cluster f5b398c24f — score 8

- Title: The 20 Most Common Passwords Hackers Target in 2026
- Source: Huntress (detection_response_operations)
- Published: 2026-09-10T13:00:00+00:00
- Link: https://www.huntress.com/blog/most-common-passwords
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
See this year's most common passwords, why they're so easy to crack, and how a stronger password (or passphrase) habit keeps your accounts protected.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: The 20 Most Common Passwords Hackers Target in 2026
  - Published: 2026-09-10T13:00:00+00:00
  - Link: https://www.huntress.com/blog/most-common-passwords
  - Summary: See this year's most common passwords, why they're so easy to crack, and how a stronger password (or passphrase) habit keeps your accounts protected.

### Cluster 5505e28820 — score 8

- Title: Grand Theft Auto VI hype leads to malware
- Source: Huntress (detection_response_operations)
- Published: 2026-09-09T14:00:00+00:00
- Link: https://www.huntress.com/blog/fake-gta6-download-malware-analysis
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
Threat actors are exploiting GTA6 hype with fake leaked downloads spread via SEO poisoning, packed with RATs, infostealers, and wiper ransomware. Here’s what Huntress found.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Grand Theft Auto VI hype leads to malware
  - Published: 2026-09-09T14:00:00+00:00
  - Link: https://www.huntress.com/blog/fake-gta6-download-malware-analysis
  - Summary: Threat actors are exploiting GTA6 hype with fake leaked downloads spread via SEO poisoning, packed with RATs, infostealers, and wiper ransomware. Here’s what Huntress found.

### Cluster 8f823c32f7 — score 8

- Title: Personal, Financial Info Exposed in Revolut Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-14T13:03:35+00:00
- Link: https://www.securityweek.com/personal-financial-info-exposed-in-revolut-data-breach/
- Fetch status: not_attempted
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
The company unintentionally disclosed users’ information to a third party impersonating a government agency. The post Personal, Financial Info Exposed in Revolut Data Breach appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Personal, Financial Info Exposed in Revolut Data Breach
  - Published: 2026-09-14T13:03:35+00:00
  - Link: https://www.securityweek.com/personal-financial-info-exposed-in-revolut-data-breach/
  - Summary: The company unintentionally disclosed users’ information to a third party impersonating a government agency. The post Personal, Financial Info Exposed in Revolut Data Breach appeared first on SecurityWeek .

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

### Cluster 4839f2ab11 — score 8

- Title: Nightmare-Eclipse Strikes Again With 'ShieldCrash' Windows Exploit
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-10T15:29:12+00:00
- Link: https://www.darkreading.com/vulnerabilities-threats/nightmare-eclipse-strikes-again-shieldcrash-windows-exploit
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
The disgruntled researcher continued their vendetta against Microsoft by publishing yet another zero-day exploit for Windows Defender.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Nightmare-Eclipse Strikes Again With 'ShieldCrash' Windows Exploit
  - Published: 2026-09-10T15:29:12+00:00
  - Link: https://www.darkreading.com/vulnerabilities-threats/nightmare-eclipse-strikes-again-shieldcrash-windows-exploit
  - Summary: The disgruntled researcher continued their vendetta against Microsoft by publishing yet another zero-day exploit for Windows Defender.

### Cluster 8e76e4eaf9 — score 8

- Title: Mythos Vulnerability Firehose Hits a Human Bottleneck
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-09T21:19:55+00:00
- Link: https://www.darkreading.com/application-security/mythos-vulnerability-firehose-hits-human-bottleneck
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
An analysis of Project Glasswing findings shows only a fraction of the bugs it has discovered have reached disclosure, and an even smaller number have been fixed.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Mythos Vulnerability Firehose Hits a Human Bottleneck
  - Published: 2026-09-09T21:19:55+00:00
  - Link: https://www.darkreading.com/application-security/mythos-vulnerability-firehose-hits-human-bottleneck
  - Summary: An analysis of Project Glasswing findings shows only a fraction of the bugs it has discovered have reached disclosure, and an even smaller number have been fixed.

### Cluster 17a72c0aaf — score 8

- Title: Red Heron Exploits Gitea RCE to Compromise 13 Organizations Across Six Countries
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-14T16:56:30+00:00
- Link: https://thehackernews.com/2026/09/red-heron-exploits-gitea-rce-to.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: Gitea

#### Cluster taxonomy (union across members)
- affected_products: Gitea
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: Gitea
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A suspected Chinese threat actor tracked as Red Heron has been attributed to the rapid exploitation of a recently disclosed security vulnerability in Gitea to compromise internet-facing instances as part of a multi-national campaign. "Red Heron scanned 1,386 Gitea instances across seven countries and maintained a separate dataset of 477 Taiwan-based systems," Acronis Threat Research Unit (TRU)
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Red Heron Exploits Gitea RCE to Compromise 13 Organizations Across Six Countries
  - Published: 2026-09-14T16:56:30+00:00
  - Link: https://thehackernews.com/2026/09/red-heron-exploits-gitea-rce-to.html
  - Summary: A suspected Chinese threat actor tracked as Red Heron has been attributed to the rapid exploitation of a recently disclosed security vulnerability in Gitea to compromise internet-facing instances as part of a multi-national campaign. "Red Heron scanned 1,386 Gitea instances across seven countries and maintained a separate dataset of 477 Taiwan-based systems," Acronis Threat Research Unit (TRU)

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

### Cluster 178bbf8b39 — score 8

- Title: IBM Db2 Mirror for i: pre-auth RCE and the road to QSECOFR
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-14T13:20:24+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wg39a3/ibm_db2_mirror_for_i_preauth_rce_and_the_road_to/
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
submitted by /u/buherator [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: IBM Db2 Mirror for i: pre-auth RCE and the road to QSECOFR
  - Published: 2026-09-14T13:20:24+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wg39a3/ibm_db2_mirror_for_i_preauth_rce_and_the_road_to/
  - Summary: submitted by /u/buherator [link] [comments]

### Cluster 3d0bf5394b — score 8

- Title: Linux Detection Engineering - Local Privilege Escalation
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-09-11T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/threat-command/linux-privilege-escalation-detection-framework
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
Seven of the thirteen Linux privilege escalation CVEs we tracked in 2026 turned out to be the same copy-on-write bug pointed at different kernel interfaces. We ran the public proof-of-concept for eleven exploits and two misconfigurations, and noted which rules fired.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Linux Detection Engineering - Local Privilege Escalation
  - Published: 2026-09-11T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/linux-privilege-escalation-detection-framework
  - Summary: Seven of the thirteen Linux privilege escalation CVEs we tracked in 2026 turned out to be the same copy-on-write bug pointed at different kernel interfaces. We ran the public proof-of-concept for eleven exploits and two misconfigurations, and noted which rules fired.
