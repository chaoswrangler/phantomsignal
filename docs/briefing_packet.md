# PHANTOMSignal Briefing Packet

- Generated: 2026-06-23T20:20:29.171257+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 77
- Total items in window: 299
- Total clusters raw: 132
- Total clusters in packet: 52
- Dropped low score: 80
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

- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Unit 42** (threat_research_primary)
  - URL: https://unit42.paloaltonetworks.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 9
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 1
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 4
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 9
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
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
  - In window count: 2
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 3
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 0
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
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
  - In window count: 1
- **Active Countermeasures** (detection_response_operations)
  - URL: https://www.activecountermeasures.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 20
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
  - In window count: 2
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 14
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 5
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
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 0
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
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
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 14
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
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
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
  - In window count: 6
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 0
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
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
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 43
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 28
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 14
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

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 5
- Article count: 13
- Cohesion: 0.32
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_industries: financial_services
  - affected_products: Microsoft Defender
- Cluster IDs: 63edb37821, 165b535ec0, f4c821a558, 75ea622200, bc04521832
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
  - https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
  - https://www.infosecurity-magazine.com/news/lookalike-npm-package-postcss/
  - https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/
  - https://www.microsoft.com/en-us/security/blog/2026/06/17/crypto-clipper-uses-tor-worm-like-propagation-for-persistence-control/
  - https://www.microsoft.com/en-us/security/blog/2026/06/17/beyond-the-benchmark-advancing-security-at-ai-speed/
  - https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html

### WordPress active exploitation
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 5
- Article count: 11
- Cohesion: 0.207
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, web_shell_backdoor, active_exploitation, phishing_social_eng, data_breach
  - affected_industries: government
  - affected_products: WordPress
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: d1df71d8fb, 5858b86279, 8a24d06359, e293ff297b, bc04521832
- Links:
  - https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html
  - https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/
  - https://securitylabs.datadoghq.com/articles/detecting-the-klue-supply-chain-attack-in-salesforce/
  - https://www.darkreading.com/cyberattacks-data-breaches/salesforce-data-thefts-klue-app-compromise
  - https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
  - https://www.infosecurity-magazine.com/news/klue-breach-compromise/
  - https://www.securityweek.com/canadian-electricity-provider-london-hydro-discloses-data-breach/
  - https://www.securityweek.com/ffmpeg-pixelsmash-flaw-allows-rce-on-video-players-media-servers-nas-appliances/
  - https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html

### supply chain targeting Fortinet
- Anchor signal: Fortinet
- Theme key: fortinet
- Cluster count: 3
- Article count: 8
- Cohesion: 0.2
- Shared strong signals: Fortinet
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, phishing_social_eng, data_breach
  - affected_products: Fortinet
- Cluster IDs: 55705936f5, f2b3bd6ba4, 8a24d06359
- Links:
  - https://risky.biz/RBNEWS579/
  - https://www.helpnetsecurity.com/2026/06/23/fortibleed-investigation-remediation/
  - https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/
  - https://cyberscoop.com/fortinet-fortisandbox-vulnerabilities-exploits/
  - https://www.darkreading.com/cyberattacks-data-breaches/sweeping-credential-harvesting-heist-compromises-30k-fortinet-devices
  - https://www.infosecurity-magazine.com/news/operation-escaneo-cloudsek-latam/
  - https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/
  - https://www.securityweek.com/canadian-electricity-provider-london-hydro-discloses-data-breach/

### Microsoft Entra vulnerability activity
- Anchor signal: Microsoft Entra
- Theme key: microsoft-entra
- Cluster count: 3
- Article count: 3
- Cohesion: 0.257
- Shared strong signals: Microsoft Entra
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Entra
- Cluster IDs: ecad4b1a4b, e2ef0ac5b5, 41719728a2
- Links:
  - https://horizon3.ai/intelligence/blogs/autonomy-is-earned-not-claimed/
  - https://securitylabs.datadoghq.com/articles/agent-id-inside-agent-compromise/
  - https://www.elastic.co/security-labs/aad-graph-activity-logs-threat-detection

### supply chain targeting npm
- Anchor signal: npm
- Theme key: npm
- Cluster count: 2
- Article count: 8
- Cohesion: 0.2
- Shared strong signals: npm
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain
  - affected_industries: financial_services
  - affected_products: npm
- Cluster IDs: 63edb37821, 8a24d06359
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
  - https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
  - https://www.infosecurity-magazine.com/news/lookalike-npm-package-postcss/
  - https://www.securityweek.com/canadian-electricity-provider-london-hydro-discloses-data-breach/

### ransomware extortion targeting Salesforce
- Anchor signal: Salesforce
- Theme key: salesforce
- Cluster count: 2
- Article count: 6
- Cohesion: 0.2
- Shared strong signals: Salesforce
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, data_breach
  - affected_products: Salesforce
- Cluster IDs: 5858b86279, f2b3bd6ba4
- Links:
  - https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/
  - https://securitylabs.datadoghq.com/articles/detecting-the-klue-supply-chain-attack-in-salesforce/
  - https://www.darkreading.com/cyberattacks-data-breaches/salesforce-data-thefts-klue-app-compromise
  - https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
  - https://www.infosecurity-magazine.com/news/klue-breach-compromise/
  - https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/

### CVE-2026-8461 exploitation activity
- Anchor signal: CVE-2026-8461
- Theme key: cve-2026-8461
- Cluster count: 2
- Article count: 2
- Cohesion: 0.526
- Shared strong signals: CVE-2026-8461
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-8461
- Cluster IDs: e293ff297b, 531d8dfe1d
- Links:
  - https://www.securityweek.com/ffmpeg-pixelsmash-flaw-allows-rce-on-video-players-media-servers-nas-appliances/
  - https://www.bleepingcomputer.com/news/security/ffmpeg-fixes-pixelsmash-flaw-in-widely-used-video-decoder/

### Google Cloud vulnerability activity
- Anchor signal: Google Cloud
- Theme key: google-cloud
- Cluster count: 2
- Article count: 3
- Cohesion: 0.2
- Shared strong signals: Google Cloud
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Google Cloud
- Cluster IDs: 115f04b624, 512ea8982c
- Links:
  - https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/
  - https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/
  - https://risky.biz/SRB171/

### Kubernetes vulnerability activity
- Anchor signal: Kubernetes
- Theme key: kubernetes
- Cluster count: 2
- Article count: 9
- Cohesion: 0.2
- Shared strong signals: Kubernetes
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Kubernetes
- Cluster IDs: b8988e5561, 512ea8982c
- Links:
  - https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html
  - https://trustedsec.com/blog/modern-web-application-content-discovery
  - https://www.darkreading.com/cyberattacks-data-breaches/crypto-heist-fake-reputation-boosting-campaign
  - https://www.infosecurity-magazine.com/news/gitbait-github-pages-sheetbest/
  - https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/
  - https://risky.biz/SRB171/

### ai security targeting Microsoft 365
- Anchor signal: Microsoft 365
- Theme key: microsoft-365
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Microsoft 365
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ai_security
  - affected_products: Microsoft 365
- Cluster IDs: 5362786b4f, f2b3bd6ba4
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/
  - https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (2)
- **Introducing Patch the Planet**
  - Cluster: 9a4b23feba
  - Sources in window: 3
  - Window hours: 4.9
  - Cohort count: 3
- **Scattered Spider Hackers Plead Guilty on Day 1 of Trial**
  - Cluster: d29e7e479c
  - Sources in window: 3
  - Window hours: 3.5
  - Cohort count: 2

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-34413 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-34414 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-34415 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-41459 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-41679 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-50656 + Anthropic/Claude (cluster 63edb37821, first observation: True)
- Pair: CVE-2026-50656 + Apple iOS/macOS (cluster 63edb37821, first observation: True)
- Pair: CVE-2026-50656 + Microsoft Defender (cluster 63edb37821, first observation: True)
- Pair: CVE-2026-50656 + npm (cluster 63edb37821, first observation: True)
- Pair: CVE-2026-48907 + WordPress (cluster d1df71d8fb, first observation: True)
- Pair: CVE-2026-25089 + Fortinet (cluster f2b3bd6ba4, first observation: True)
- Pair: CVE-2026-25089 + Microsoft 365 (cluster f2b3bd6ba4, first observation: True)
- Pair: CVE-2026-25089 + Salesforce (cluster f2b3bd6ba4, first observation: True)
- Pair: CVE-2026-39808 + Fortinet (cluster f2b3bd6ba4, first observation: True)
- Pair: CVE-2026-39808 + Microsoft 365 (cluster f2b3bd6ba4, first observation: True)

### Drift (2)
- **Scattered Spider** (cluster d29e7e479c)
  - New industries: government
  - New products: (none)
  - Prior top industries: aviation_defense, financial_services, healthcare
  - Prior top products: AWS, Fortinet, Ivanti
- **ShinyHunters** (cluster 8a24d06359)
  - New industries: financial_services, manufacturing_industrial
  - New products: Fortinet, WordPress
  - Prior top industries: education, government, healthcare
  - Prior top products: Anthropic/Claude, GitHub, npm

### Persistence (3)
- actor_attribution: ShinyHunters (weeks observed: 4, cluster 8a24d06359)
- cve_ids: CVE-2026-11645 (weeks observed: 4, cluster bc04521832)
- cve_ids: CVE-2026-25089 (weeks observed: 3, cluster f2b3bd6ba4)

### Tier inversion (3)
- **F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution**
  - Cluster: bfe56aaca6
  - Primary source: The Hacker News
  - Strong signals: CVE-2026-42055, CVE-2026-42530, CVE-2026-42945
- **CVE-2026-25860 turn XSS to RCE**
  - Cluster: 5fa1fc890c
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-25860
- **CVE-2026-5667: Unauthenticated Remote Control of Mitsubishi MAC-577IF-2E WiFi Adapters via Probe Request Reconnaissance**
  - Cluster: 41256d55c8
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-5667

## Clusters

### Cluster 77122429c6 — score 38

- Title: Weekly Metasploit Update: NTLM Relay Priv Esc, MCP Server Integration, Paperclip AI RCE Chain, and more
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-19T17:08:23+00:00
- Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-19-06-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-41679

#### Cluster taxonomy (union across members)
- affected_products: Linux kernel
- cve_ids: CVE-2026-34413, CVE-2026-34414, CVE-2026-34415, CVE-2026-41459, CVE-2026-41679
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: Linux kernel
- cve_ids: CVE-2026-41679, CVE-2026-41459, CVE-2026-34413, CVE-2026-34415, CVE-2026-34414
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
This week's release includes five new modules, including a full unauthenticated RCE chain for Paperclip AI and a VS Code extension persistence technique. On the post-exploitation side, the new windows/local/ntlm_relay_2_self module coerces the local machine account to authenticate via OpenEncryptedFileRaw (WebDAV), relays that NTLM authentication to a Domain Controller's LDAP service, then uses the resulting LDAP session to write Shadow Credentials and obtain a Kerberos service ticket as Administrator via S4U2Proxy, enabling PsExec back to itself for SYSTEM access. On the enhancement side, the new MCP server plugin lets AI tools assist operators directly within a running msfconsole instance, and module check codes now return richer detail for users. New module content (5) Paperclip AI RCE using a chain of six API calls (CVE-2026-41679) Authors: Sagilayani https://github.com/sagilayani and h00die-gr3y h00die.gr3y@gmail.com Type: Exploit Pull request: #21547 contributed by h00die-gr3y Pa
```

#### Full body

```
Back to Blog Products and Tools Weekly Metasploit Update: NTLM Relay Priv Esc, MCP Server Integration, Paperclip AI RCE Chain, and more Alan David Foster Jun 19, 2026 | Last updated on Jun 19, 2026 | 5 min read This week's release includes five new modules, including a full unauthenticated RCE chain for Paperclip AI and a VS Code extension persistence technique. On the post-exploitation side, the new windows/local/ntlm_relay_2_self module coerces the local machine account to authenticate via OpenEncryptedFileRaw (WebDAV), relays that NTLM authentication to a Domain Controller's LDAP service, then uses the resulting LDAP session to write Shadow Credentials and obtain a Kerberos service ticket as Administrator via S4U2Proxy, enabling PsExec back to itself for SYSTEM access. On the enhancement side, the new MCP server plugin lets AI tools assist operators directly within a running msfconsole instance, and module check codes now return richer detail for users. New module content (5) Paperclip AI RCE using a chain of six API calls (CVE-2026-41679) Authors: Sagilayani https://github.com/sagilayani and h00die-gr3y [email protected] Type: Exploit Pull request: #21547 contributed by h00die-gr3y Path: linux/http/paperclipai_unauth_rce_cve_2026_41679 AttackerKB reference: CVE-2026-41679 Description: Adds an exploit module for CVE-2026-41679 which exploits Paperclip. An unauthenticated attacker can achieve full remote code execution on any network-accessible Paperclip instance running in authenticated mode with default configuration. The entire chain is six API calls. Xerte Online Toolkits Arbitrary File Upload - Unauthenticated Media Upload Author: bootstrapbool [email protected] Type: Exploit Pull request: #21371 contributed by bootstrapbool Path: multi/http/xerte_unauthenticated_mediaupload AttackerKB reference: CVE-2026-41459 Description: Exploits authentication failure ( CVE-2026-34413 ), extension blacklist ( CVE-2026-34415 ), and path traversal ( CVE-2026-34414 ) vulnerabilities in Xerte Online Toolkits versions 3.15 and earlier. VS Code Extension Persistence Author: h00die Type: Exploit Pull request: #21465 contributed by h00die Path: multi/persistence/vscode_extension Description: Adds a new persistence module that achieves persistence by installing a malicious extension into a user's VS Code extensions directory. The next time the target opens VS Code, the extension executes and delivers a shell back to the attacker. NTLM Relay to Self (HTTP to LDAP) - Post Exploitation Author: jheysel-r7 Type: Exploit Pull request: #21430 contributed by jheysel-r7 Path: windows/local/ntlm_relay_2_self Description: Adds a module that exploits the NTLMRelay2Self attack. It requires a low-privilege user session on a Windows host. Linux Kernel __ptrace_may_access() Exit Race Change File Disclosure Authors: 0xdeadbeefnetwork and bhaskarbhar Type: Post Pull request: #21472 contributed by bhaskarbhar Path: linux/gather/cve_2026_46333_chage AttackerKB reference: CVE-2026-46333 Description: Adds a post module that leverages CVE-2026-46333, a vulnerability in the Linux kernel whereby a race condition exists when tearing down a process. A local attacker can exploit this to obtain file handles they would not otherwise have access to. In the exploit, this is leveraged to leak the contents of the /etc/shadow file. Enhancements and features (7) #21254 from golem445 - Nmap imports will include domain name if supplied by the user for the scan. #21259 from g0tmi1k - Adds a number of enhancements to msfconsole's search functionality by cleaning up some inconsistencies and giving users the option to hide the child elements of search results with the -c flag. Also introduces two global options, SearchSort and SearchChildMode , that users can set and forget in order to control ascending/descending search results and whether or not child items appear under search results respectively. #21367 from g0tmi1k - Adds a number of enhancements to the rexec_login module inclu
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Weekly Metasploit Update: NTLM Relay Priv Esc, MCP Server Integration, Paperclip AI RCE Chain, and more
  - Published: 2026-06-19T17:08:23+00:00
  - Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-19-06-2026
  - Summary: This week's release includes five new modules, including a full unauthenticated RCE chain for Paperclip AI and a VS Code extension persistence technique. On the post-exploitation side, the new windows/local/ntlm_relay_2_self module coerces the local machine account to authenticate via OpenEncryptedFileRaw (WebDAV), relays that NTLM authentication to a Domain Controller's LDAP service, then uses the resulting LDAP session to write Shadow Credentials and obtain a Kerberos service ticket as Administrator via S4U2Proxy, enabling PsExec back to itself for SYSTEM access. On the enhancement side, the new MCP server plugin lets AI tools assist operators directly within a running msfconsole instance, and module check codes now return richer detail for users. New module content (5) Paperclip AI RCE using a chain of six API calls (CVE-2026-41679) Authors: Sagilayani https://github.com/sagilayani and h00die-gr3y h00die.gr3y@gmail.com Type: Exploit Pull request: #21547 contributed by h00die-gr3y Pa

### Cluster 03eea66307 — score 27

- Title: CVE-2026-50751 | Check Point Security Gateway Improper Authentication Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-16T20:34:54+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-50751/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-50751

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- cve_ids: CVE-2026-50751
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- cve_ids: CVE-2026-50751
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-50751 is an authentication bypass vulnerability affecting Check Point Security Gateway VPN services. Check Point has confirmed active exploitation against vulnerable deployments.
```

#### Full body

```
CVE-2026-50751 Check Point Security Gateway Improper Authentication Vulnerability CVE-2026-50751 is an authentication bypass vulnerability affecting Check Point Security Gateway Remote Access VPN and Mobile Access services. The flaw exists in deprecated IKEv1 Remote Access and Mobile Access certificate validation logic and can allow a remote attacker to establish a VPN session without supplying a valid password. Check Point has confirmed active exploitation in the wild and reported a limited number of targeted organizations globally, including at least one post-compromise case linked to a Qilin ransomware affiliate. Technical Details The vulnerability affects the authentication process used by deprecated IKEv1-based Remote Access VPN deployments. A successful attacker can: Establish a VPN session without valid user credentials Gain an initial foothold inside the target environment Conduct follow-on activity including lateral movement and privilege escalation Deploy additional tooling or ransomware-related payloads after access is established Check Point notes that successful exploitation grants VPN access but additional actions are required before an attacker can access internal resources or elevate privileges. The vendor reports exploitation activity beginning on May 7, 2026, with activity increasing in early June and prompting public disclosure and remediation guidance. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this authentication bypass can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether unauthorized VPN access is possible. Patch immediately: Apply Check Point’s recommended hotfixes and mitigation guidance for affected Security Gateways. Re-run the test: Confirm the vulnerability is no longer exploitable after remediation. Indicators of Compromise Indicator Type Description 45.77.149.152 IP Address Suspicious infrastructure identified by Check Point 209.182.225.136 IP Address Suspicious infrastructure identified by Check Point 38.60.157.139 IP Address Suspicious infrastructure identified by Check Point 162.33.177.101 IP Address Suspicious infrastructure identified by Check Point 45.76.26.42 IP Address Suspicious infrastructure identified by Check Point 144.208.127.155 IP Address Suspicious infrastructure identified by Check Point 38.54.88.201 IP Address Suspicious infrastructure identified by Check Point 38.54.107.167 IP Address Suspicious infrastructure identified by Check Point 66.42.99.200 IP Address Suspicious infrastructure identified by Check Point 52fda5c1b9704544f32ee98d9060e689 File Hash Associated with observed malicious activity 51d39aa39478beeac94f2d12f682ecce File Hash Associated with observed malicious activity Check Point also reported additional malicious infrastructure identified between June 9 and June 11, 2026. Affected versions & patch Affected Check Point lists the following as affected: Mobile Access / SSL VPN deployments Remote Access VPN deployments Spark Firewall deployments R80.20.X (End of Support) R80.40 (End of Support) R81 (End of Support) R81.10 (End of Support) R81.10.X R81.20 R82 R82.00.X R82.10 Patch Update all affected Security Gateways using Check Point’s released hotfixes. Follow Check Point’s alternative remote-access mitigation guidance if immediate patching is not possible. Prioritize systems exposing IKEv1-based Remote Access VPN services to the Internet. Timeline May 7, 2026 — Check Point reports exploitation activity begins. Early June 2026 — Exploitation activity increases against vulnerable deployments. June 8, 2026 — Check Point publishes its security advisory and mitigation guidance. June 9–11, 2026 — Check Point publishes additional suspicious IP infrastructure associa
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-50751 | Check Point Security Gateway Improper Authentication Vulnerability
  - Published: 2026-06-16T20:34:54+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-50751/
  - Summary: CVE-2026-50751 is an authentication bypass vulnerability affecting Check Point Security Gateway VPN services. Check Point has confirmed active exploitation against vulnerable deployments.

### Cluster 63edb37821 — score 23

- Title: From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet
- Source: Microsoft Threat Intelligence (threat_research_primary)
- Published: 2026-06-18T03:43:04+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 4
- Strong signals: Microsoft Defender, npm

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain, zero_day
- affected_industries: financial_services
- affected_products: Anthropic/Claude, Apple iOS/macOS, Microsoft Defender, npm
- cve_ids: CVE-2026-50656
- urgency_signals: zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: financial_services
- affected_products: npm, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
A poisoned npm package infected 140+ projects with a hidden payload. This report highlights how to detect, hunt, and defend against supply chain attacks using Microsoft Defender and actionable threat intelligence. The post From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Malware npm Content types Research Products and services Microsoft Defender Topics Actionable threat insights Threat intelligence June 19, 2026 update: Microsoft assesses with high confidence that this activity is attributable to Sapphire Sleet , a North Korean state actor that primarily targets the financial sector. The infrastructure and post-compromise TTPs observed in this campaign are consistent with previously documented Sapphire Sleet activity. Sapphire Sleet also conducted a separate npm supply chain compromise affecting Axios , a popular JavaScript HTTP client, in April 2026 . Microsoft Threat Intelligence observed a large-scale npm supply chain attack affecting 140+ packages across the mastra and @mastra scopes on the npm registry. Microsoft shared its findings with the npm security team, the compromised packages have been removed and the attacker’s publish access to the @mastra scope has been revoked. The compromise originated from the takeover of the ehindero npm maintainer account, which had publish rights across the Mastra ecosystem and was used to publish poisoned package versions that introduced easy-day-js, a malicious typosquat of the popular dayjs library. Microsoft assesses with high confidence that this activity is attributable to Sapphire Sleet . Once installed, easy-day-js triggered a postinstall hook that executed an obfuscated dropper script, disabled Transport Layer Security (TLS) certificate verification, contacted attacker-controlled command-and-control (C2) infrastructure, downloaded a second-stage payload, and executed the payload as a detached hidden process. The activity followed a coordinated staged delivery pattern, with a clean bait version published first, followed by a weaponized version and rapid publication of the compromised Mastra packages. Because the payload executes during installation, any developer workstation or continuous integration and continuous delivery (CI/CD) pipeline that ran npm install or npm update after the compromised versions were published was potentially exposed, regardless of whether the package was imported in application code. This created risk to credentials, tokens, build environments, and downstream software integrity. Microsoft Defender Antivirus, Microsoft Defender for Endpoint, and Microsoft Defender XDR provide detections and hunting coverage for suspicious Node.js execution, malicious package behavior, reflective code loading, persistence activity and command-and-control communication. Attack chain overview Figure 1. End-to-end attack chain from npm account takeover through mass dependency injection to second-stage payload execution. At a high level, the attack progressed through seven phases: Account compromise: The threat actor gained control of the ehindero npm account, a listed maintainer with publish rights across the entire @mastra scope. Typosquat creation: The threat actor published easy-day-js , a package impersonating the legitimate dayjs library (57M+ weekly downloads), using a coordinating anonymous email account). Mass poisoning: Using the compromised account, the threat actor published new versions of 140+packages across the @mastra scope, each injected with easy-day-js@^1.11.21 as a new dependency. All poisoned versions were tagged as latest. Delivery: Developers and CI/CD pipelines running npm install automatically resolved to the compromised versions. The semantic versioning (SemVer) range ^1.11.21 resolved to 1.11.22, the version containing the malicious postinstall hook. Execution: The postinstall hook executed an obfuscated 4,572-byte dropper that disabled TLS verification, dropped tracking markers, and contacted the C2 server. Second-stage payload: The dropper fetched executable code from the C2 server, wrote it as a randomly named .js file, and spawned it as a fully detached, window-hidden Node.js process. Post-compromise tradecraft: On systems where the implant established C2 communication, Sapp
```

#### Corroborating sources (4)

- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet
  - Published: 2026-06-18T03:43:04+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
  - Summary: A poisoned npm package infected 140+ projects with a hidden payload. This report highlights how to detect, hunt, and defend against supply chain attacks using Microsoft Defender and actionable threat intelligence. The post From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet appeared first on Microsoft Security Blog .
- **Microsoft Security Blog** (threat_research_primary)
  - Title: From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet
  - Published: 2026-06-18T03:43:04+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
  - Summary: A poisoned npm package infected 140+ projects with a hidden payload. This report highlights how to detect, hunt, and defend against supply chain attacks using Microsoft Defender and actionable threat intelligence. The post From package to postinstall payload: Inside the Mastra npm supply chain compromise by Sapphire Sleet appeared first on Microsoft Security Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: 145 Mastra npm Packages Compromised via Hijacked Contributor Account
  - Published: 2026-06-17T07:38:24+00:00
  - Link: https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
  - Summary: As many as 145 npm packages associated with the Mastra namespace ("@mastra/*"), a popular open-source JavaScript and TypeScript framework for building artificial intelligence (AI) applications, have been compromised as part of a software supply chain attack codenamed easy-day-js, per findings from Endor Labs, JFrog, OX Security, SafeDep, Socket, StepSecurity, and Synk. "A single npm account (
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Lookalike npm Package Hides a Multi-Stage Windows RAT
  - Published: 2026-06-23T15:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/lookalike-npm-package-postcss/
  - Summary: JFrog found an npm package impersonating postcss-selector-parser to drop a multi-stage Windows RAT

### Cluster cacd9474df — score 20

- Title: Introducing the Red Agent POV Series
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-06-17T14:33:41+00:00
- Link: https://www.wiz.io/blog/red-agent-pov-series
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
An inside look at how the Red Agent, our AI-Powered Attacker, uncovers complex, exploitable risks in the wild
```

#### Full body

```
Wiz Pricing Get a demo Get a demo Malicious actors are actively weaponizing AI to scan and exploit public-facing environments at unprecedented speed and scale. To stay ahead, defenders have had to evolve- and AI-powered offensive security has made massive leaps. Current frontier models, paired with our purpose-built agent harness, are already finding real, exploitable, multi-step chains on a daily basis. With these models, AI-powered offensive security is now able to find flaws that would have seemed out of reach for automated testing just a year ago. These flaws are non-trivial even for expert pentesters and bug bounty hunters working manually. This is why we built the Red Agent , our AI-powered pentester that operates at machine speed to help teams stay ahead in the AI era. By continuously reasoning about application behavior, it synthesizes the kind of complex, logic-driven vulnerabilities and multi-step attack chains that human testers take days of manual work to uncover. When adversaries are continuously scanning your perimeter with AI, relying on periodic manual testing will not keep up. For security and offensive teams, turning on the Red Agent is an immediate necessity to find and close your critical exploitable risks before adversaries find them. We are excited to introduce a new blog series from the Wiz Research team, , where we pull back the curtain to give you an inside look at how the Red Agent uncovers these complex, exploitable risks in production. Throughout this series, we will focus on specific bug classes discovered by the Red Agent and share real examples of how it reasons through APIs and finds context-driven vulnerabilities. Today, we are launching the first blog in this series, detailing how the Red Agent uncovered a critical SSRF vulnerability in production systems. What is the Red Agent? The Red Agent is Wiz's AI-powered pentester, built to continuously discover logic-driven vulnerabilities and misconfigurations across publicly facing environments. It condenses what traditionally took human testers hours or days of manual work into an autonomous, continuous process, operating at machine speed without sacrificing depth. The Red Agent does so by reasoning about the application- it builds hypotheses from failed probes, accumulates constraints from blocked attempts, and synthesizes multi-step attack paths that only emerge from understanding how an application actually behaves. When a request gets blocked, the Red Agent uses that as a data point to narrow the solution space for the next attempt. This allows it to uncover sophisticated attack chains at scale, giving defenders the ability to find and remediate critical risks before adversaries can exploit them. Red Agent in the wild To give an idea of what defending at machine speed looks like, we looked at the aggregate data from the Red Agent’s performance over a one-month period. Operating at a scale that would be impossible for a human alone, the Red Agent completed hundreds of thousands of autonomous scans across ~1,000 environments. In that window, it surfaced over 17,000 unique findings which included over 5,500 high and critical vulnerabilities , which represent validated, multi-step attack chains in production environments. Here is a high-level look at the key takeaways from those findings: Access control remains the dominant failure mode Authorization and access control flaws remain the single biggest gap in modern cloud applications. 54% of all unique findings stemmed from broken access control. This includes authentication bypasses, unrestricted access to components or sensitive information, IDOR/BOLA, BFLA, and default credentials. These represent real, production applications that are routinely shipped with entirely unprotected management APIs and exposed internal endpoints. Leaked secrets present a massive, high-severity footprint Insecure secrets expand the blast radius across cloud environments exponentially. Among all exposed secrets discove
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Introducing the Red Agent POV Series
  - Published: 2026-06-17T14:33:41+00:00
  - Link: https://www.wiz.io/blog/red-agent-pov-series
  - Summary: An inside look at how the Red Agent, our AI-Powered Attacker, uncovers complex, exploitable risks in the wild

### Cluster f8c213c0bd — score 19

- Title: CVE-2024-40766: The Patch Fixed the Bug. Nobody Fixed the Configuration., (Tue, Jun 23rd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-06-23T03:02:34+00:00
- Link: https://isc.sans.edu/diary/rss/33094
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2024-40766

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2024-40766
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Primary article taxonomy
- cve_ids: CVE-2024-40766
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Summary

```
The vulnerability
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: CVE-2024-40766: The Patch Fixed the Bug. Nobody Fixed the Configuration., (Tue, Jun 23rd)
  - Published: 2026-06-23T03:02:34+00:00
  - Link: https://isc.sans.edu/diary/rss/33094
  - Summary: The vulnerability

### Cluster d1df71d8fb — score 18

- Title: CISA Warns of Actively Exploited Joomla JCE Flaw Allowing PHP Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-17T05:50:46+00:00
- Link: https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48907

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, supply_chain, web_shell_backdoor
- affected_industries: government
- affected_products: WordPress
- cve_ids: CVE-2026-48907
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, web_shell_backdoor, active_exploitation
- affected_industries: government
- affected_products: WordPress
- cve_ids: CVE-2026-48907
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting Widget Factory Joomla Content Editor (JCE) to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerability, tracked as CVE-2026-48907 (CVSS score: 10.0), is a case of improper access control that could facilitate arbitrary
```

#### Full body

```
CISA Warns of Actively Exploited Joomla JCE Flaw Allowing PHP Code Execution  Ravie Lakshmanan  Jun 17, 2026 Vulnerability / Supply Chain Attack The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting Widget Factory Joomla Content Editor (JCE) to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerability, tracked as CVE-2026-48907 (CVSS score: 10.0), is a case of improper access control that could facilitate arbitrary code execution. "Widget Factory Joomla Content Editor contains an improper access control vulnerability which could allow for upload and execution of PHP code via the creation of new editor profiles for unauthenticated users," CISA said . According to a description of the vulnerability published on CVE.org, the issue resides in the JCE editor extension for Joomla, allowing a bad actor to create new editor profiles for unauthenticated users, effectively paving the way for PHP code upload and execution. The issue impacts JCE versions from 1.0.0 through 2.9.99.4. It has been patched in version 2.9.99.5, released on June 3, 2026. In its release notes, Widget Factory said "insufficient access controls permitted unauthenticated users to upload editor profiles." "The vulnerability is being actively exploited, working exploit code is public, and the attacks are automated, so a site with no public registration is not safe," Joomla said last week. "One important point: updating closes the entry point but does not clean a site that was already compromised. If you were hit before updating, the update will not remove what the attacker left behind." The content management system (CMS) provider has urged users to look for suspicious editor profiles and audit web server access logs for unauthenticated requests to the profile import task, "index.php?option=com_jce&task=profiles.import." Phil E. Taylor of mySites.guru has revealed that the vulnerability is being weaponized to import a rogue editor profile and use it to drop a web shell, granting the attackers a persistent backdoor on the server. Federal Civilian Executive Branch (FCEB) agencies have been ordered to apply the fixes by June 19, 2026. Multiple Campaigns Target WordPress Sites The disclosure comes as Sansec detailed a new supply chain attack campaign that targeted over 1 million sites using OptinMonster, TrustPulse, and PushEngage WordPress plugins, with the threat actors injecting malicious JavaScript that "waits for a logged-in administrator, creates a backdoor admin account, and installs a self-hiding backdoor plugin." In another campaign, unknown attackers have been found to compromise a WordPress site to embed a fake WordPress plugin named "Beloved PBN Entegrasyonu" that stealthily beaconed the site's URL to an external API upon every page load and injected arbitrary HTML or JavaScript returned by the server into the web page's footer. Exactly how the attackers breached the website is unclear, but the access is said to have enabled them to stage two PHP web shells as raw executable code with the "wp_posts" database records and granted them the ability to interact with the scripts over HTTP. This, in turn, facilitated unrestricted read/write access to the entire server file system without requiring any authentication. Specifically, the database-resident payloads allow the threat actor to perform file actions, such as read, write, edit, or delete any file on the server, browse directories across the entire server, change file permissions, rename files, create new files and folders, and upload files from their own computer. "Every visitor to the compromised site received injected PBN outbound links in their page source on every page load, directly damaging the site's search rankings and risking a manual penalty in Google Search Console," Sucuri researcher Puja Srivastava said . "The campaign is operated by a Turkish-speaking threat actor and is bu
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: CISA Warns of Actively Exploited Joomla JCE Flaw Allowing PHP Code Execution
  - Published: 2026-06-17T05:50:46+00:00
  - Link: https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday added a maximum-severity security flaw impacting Widget Factory Joomla Content Editor (JCE) to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerability, tracked as CVE-2026-48907 (CVSS score: 10.0), is a case of improper access control that could facilitate arbitrary

### Cluster 165b535ec0 — score 17

- Title: AutoJack: How a single page can RCE the host running your AI agent
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-19T00:17:54+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/
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
AutoJack is a novel exploit chain showing how a single malicious webpage can turn an AI browsing agent into a remote code execution vector on the host machine. By abusing trust in localhost, missing authentication, and unsafe parameter handling, attackers can trigger arbitrary process execution through AutoGen Studio’s MCP WebSocket. The research highlights a broader pattern - when agents can browse untrusted content and access local services, traditional boundaries like localhost are no longer secure. The post AutoJack: How a single page can RCE the host running your AI agent appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Defender Topics Actionable threat insights AI and agents Ongoing research into AI agent framework security identified an exploit chain in AutoGen Studio (AutoGen’s open-source prototyping user interface) that allows untrusted web content rendered by a browsing agent to reach a local Model Context Protocol (MCP) WebSocket and spawn arbitrary processes on the host. The technique, which we call AutoJack, jacks the agent into becoming the attacker’s last-mile delivery vehicle by crossing the localhost trust boundary that many developer tools rely on. We reported the behavior to the Microsoft Security Response Center (MSRC); following the report the maintainers hardened the upstream main branch in commit b047730. This issue was identified and addressed during development. The affected MCP WebSocket surface was never included in a Python Package Index (PyPI) release, so users who install AutoGen Studio from PyPI aren’t exposed to this specific chain. The broader lesson is general: if an agent can browse untrusted pages and also talk to privileged local services, loopback can become an attack surface and control planes must be authenticated, authorized, and isolated. Why we are looking at agent frameworks Modern AI agents are not just text generators. They read files, browse pages, call APIs, and shell out to tools. That is exactly what makes them useful, and exactly why there is investment in finding systemic execution risks in the frameworks that wire models to tools. Earlier in this series we covered RCE primitives in Microsoft Semantic Kernel . In this post we move one layer up the stack to an infrastructure and developer-facing prototyping surface and show how the same agent capabilities that make these tools valuable for experimentation can become a delivery channel for remote code execution when the prototype runs without safeguards. The takeaway is not to avoid prototypes. It is this: when an agent on your core server or laptop can browse the open web and communicate with privileged local services, localhost stops being a trust boundary. Defenders need to plan for that, and these findings show why. What is AutoGen Studio AutoGen Studio is a user interface (UI) on top of AutoGen , Microsoft Research’s framework for multi-agent systems. It lets developers compose agents, attach tools, including MCP servers, and run quick experiments. Its documentation is clear about intended use. In other words, it is a research prototype with expected developer-experience tradeoffs: defaults tuned for ease of iteration rather than hardened deployment. The AutoJack chain at a glance The explanation below is for demonstrative purposes only. The exploit chain doesn’t work on current builds. It is included here so that defenders can recognize the pattern in other agent frameworks. The exploit chain composes three independent weaknesses in AutoGen Studio’s MCP WebSocket surface: Origin allowlist trusts localhost – but a local agent is localhost (CWE-1385 – Missing Origin Validation in WebSockets): The MCP WebSocket only accepts connections whose Origin is http://127.0.0.1 or http://localhost. That blocks a browser pointed at evil.com. It does not block JavaScript that is rendered by a headless browser owned by an AutoGen agent on the same machine . Authentication middleware is opt-out for MCP paths (CWE-306 – Missing Authentication for Critical Function): The auth middleware in AutoGen Studio explicitly skipped /api/mcp/* (and /api/ws/*) on the assumption that these would do their own checks. The MCP WebSocket handler did not implement that follow-up check. As a result, the MCP WebSocket accepted connections without any authentication regardless of the auth mode configured for the rest of the app. StdioServerParams from the URL is executed verbatim (CWE-78 – Improper Neutralization of Special Elements used in an OS Command): The endpoint accepted a server_params
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: AutoJack: How a single page can RCE the host running your AI agent
  - Published: 2026-06-19T00:17:54+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/
  - Summary: AutoJack is a novel exploit chain showing how a single malicious webpage can turn an AI browsing agent into a remote code execution vector on the host machine. By abusing trust in localhost, missing authentication, and unsafe parameter handling, attackers can trigger arbitrary process execution through AutoGen Studio’s MCP WebSocket. The research highlights a broader pattern - when agents can browse untrusted content and access local services, traditional boundaries like localhost are no longer secure. The post AutoJack: How a single page can RCE the host running your AI agent appeared first on Microsoft Security Blog .

### Cluster 9a4b23feba — score 16

- Title: Introducing Patch the Planet
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-06-22T16:50:00+00:00
- Link: https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: GitHub, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: GitHub, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
What happens when you clear dozens of Trail of Bits engineers’ schedules, pair them with every open-source maintainer they can contact, and unleash the latest frontier models like GPT-5.5-Cyber on critical open-source targets? Thanks to our partnership with OpenAI and its Daybreak initiative, we can report that the impact is hundreds of discovered bugs, 64 pull requests, and 51 issues filed across 19 projects (with many more still undergoing coordinated disclosure). That was just the first week of Patch the Planet . Frontier models like GPT-5.5-Cyber are producing a firehose of security findings, and already-stretched maintainers must sift through all of it to separate real vulnerabilities from plausible-sounding false positives. Patch the Planet is different: with our experts orchestrating and triaging findings, we handle the work of fixing and hardening the code alongside the people who maintain it. The first week of Patch the Planet covered 19 projects across cryptography, networkin
```

#### Full body

```
Page content What happens when you clear dozens of Trail of Bits engineers’ schedules, pair them with every open-source maintainer they can contact, and unleash the latest frontier models like GPT-5.5-Cyber on critical open-source targets? Thanks to our partnership with OpenAI and its Daybreak initiative, we can report that the impact is hundreds of discovered bugs, 64 pull requests, and 51 issues filed across 19 projects (with many more still undergoing coordinated disclosure). That was just the first week of Patch the Planet . Frontier models like GPT-5.5-Cyber are producing a firehose of security findings, and already-stretched maintainers must sift through all of it to separate real vulnerabilities from plausible-sounding false positives. Patch the Planet is different: with our experts orchestrating and triaging findings, we handle the work of fixing and hardening the code alongside the people who maintain it. The first week of Patch the Planet covered 19 projects across cryptography, networking, language infrastructure, and software supply chain. Among these 19 projects were cURL, NATS, pyca, Sigstore, aiohttp, the Go project, freenginx, Python and python.org, urllib3, PyPI, SimpleX, Valkey, and RustCrypto. Over 30 projects have joined the initiative so far, and we’re rapidly expanding it to include more; if you maintain an open-source project, apply to join ! Live look at the Trail of Bits engineering teams Anyone can file an issue, flex, and walk away. We showed up with the patches: 37 are already merged, and many more are in flight. These merges go beyond just fixing bugs: we’re adding new tests and fuzzing harnesses, CI security scanning, supply-chain tooling, correctness fixes, and features maintainers had been meaning to get to. The goal of Patch the Planet is to leave essential open-source projects measurably better off. We brought patches, not just bug reports We’re reporting public findings on GitHub , including 64 total pull requests. We also filed 51 issues, 19 of which are already closed with a fix. This public tally undercounts the work, since several projects take reports through private channels like HackerOne, GitHub security advisories, mailing lists, and private forks, and most of these have not been released publicly yet. What’s in those pull requests matters more than the count. At python.org, we added a CI workflow built on zizmor , an open-source GitHub Actions static analyzer, fixed all of the issues it flagged, and integrated it into their CI. In RustCrypto, we contributed correctness fixes to the big-integer library that higher-level cryptography is built on, alongside genuine feature work in review: serde encoding support and HPKE DHKEM suite IDs. Other patches were plain engineering help: storage-accounting and service-restart fixes in SimpleX, a clearer admin-quarantine confirmation in PyPI’s Warehouse, and supply-chain improvements like SBOM sidecars for Python’s Windows artifacts. We will also be upstreaming many testing improvements and new testing campaigns. Arguably, our best contributions are not even bug or security fixes. Keeping track of all of this is a bot we call Patchy. Patchy monitors every project, posts each new finding and merged patch to our Slack, and, for reasons we consider scientifically sound, reintroduces the common use of goblins, gremlins, and assorted creatures . Here’s Patchy’s description of an issue that has been patched : Patchy’s description of an issue that has been patched When a patch lands, Patchy celebrates with a triumphant PATCHY HAPPY . Making Patchy happy is really what drives us. Bug patched, Patchy happy A few highlights from the week The week produced more than we can fit in this post, but here are some quick highlights. A fuzzing lab built in a day. Given a narrow goal (find remotely exploitable bugs) and no instructions on how, GPT-5.5-Cyber decided that reading the source of one of the most-reviewed C libraries in existence was a poor use of tokens
```

#### Corroborating sources (6)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: Introducing Patch the Planet
  - Published: 2026-06-22T16:50:00+00:00
  - Link: https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/
  - Summary: What happens when you clear dozens of Trail of Bits engineers’ schedules, pair them with every open-source maintainer they can contact, and unleash the latest frontier models like GPT-5.5-Cyber on critical open-source targets? Thanks to our partnership with OpenAI and its Daybreak initiative, we can report that the impact is hundreds of discovered bugs, 64 pull requests, and 51 issues filed across 19 projects (with many more still undergoing coordinated disclosure). That was just the first week of Patch the Planet . Frontier models like GPT-5.5-Cyber are producing a firehose of security findings, and already-stretched maintainers must sift through all of it to separate real vulnerabilities from plausible-sounding false positives. Patch the Planet is different: with our experts orchestrating and triaging findings, we handle the work of fixing and hardening the code alongside the people who maintain it. The first week of Patch the Planet covered 19 projects across cryptography, networkin
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: OpenAI Refocuses Cybersecurity Efforts on Patching Over Discovery
  - Published: 2026-06-23T11:07:02+00:00
  - Link: https://www.securityweek.com/openai-refocuses-cybersecurity-efforts-on-patching-over-discovery/
  - Summary: OpenAI has expanded its Daybreak cybersecurity initiative with a new suite of tools and partnerships. The post OpenAI Refocuses Cybersecurity Efforts on Patching Over Discovery appeared first on SecurityWeek .
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: OpenAI wants AI to fix vulnerabilities, not just find them
  - Published: 2026-06-23T08:49:01+00:00
  - Link: https://www.helpnetsecurity.com/2026/06/23/openai-expanded-daybreak-cybersecurity-initiative/
  - Summary: OpenAI expanded Daybreak, its cybersecurity initiative that combines AI models, Codex Security, security researchers, maintainers, industry partners, and access controls to support vulnerability discovery and remediation. Organizations can use the initiative to identify, validate, and fix software vulnerabilities, while developers, maintainers, and security teams can use its tools to strengthen defensive security capabilities. Codex Security scan (Source: OpenAI) Codex Security targets remediation bottlenecks Advances in vulnerability discovery are exposing more issues, increasing the pressure on … More → The post OpenAI wants AI to fix vulnerabilities, not just find them appeared first on Help Net Security .
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: OpenAI Expands Daybreak to Help Defenders Patch Flaws
  - Published: 2026-06-23T14:15:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/openai-daybreak-gpt-5-5-cyber/
  - Summary: OpenAI expanded Daybreak with a full GPT-5.5-Cyber release to help defenders patch software flaws
- **Risky Business News** (practitioner_analysis)
  - Title: Sponsored: Trail of Bits and OpenAI patch the planet
  - Published: 2026-06-23T04:17:44+00:00
  - Link: https://risky.biz/RBNEWSSI133/
  - Summary: In this sponsored interview James Wilson chats with Trail of Bits founder and CEO Dan Guido about its newly announced partnership with OpenAI. Together, they’ve started a new initiative called “Patch the Planet” to support open source maintainers. Being an open source maintainer is more difficult than ever. Just using frontier models to keep up with all the bug reports isn’t enough. Trail of Bits wants to help maintainers by combining its deep cybersecurity expertise with OpenAI’s GPT 5.5 Cyber. As Dan points out in this interview, this isn’t just about helping maintainers find and fix bugs. They’re spending just as much time on SDLC improvements, architecture changes, and the foundations needed to make open source sustainable in the AI era.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: OpenAI Expands Daybreak With GPT-5.5-Cyber to Help Defenders Patch Security Flaws
  - Published: 2026-06-23T03:56:58+00:00
  - Link: https://thehackernews.com/2026/06/openai-expands-daybreak-with-gpt-55.html
  - Summary: OpenAI on Monday said it's releasing an improved version of its GPT‑5.5‑Cyber model to trusted defenders as part of the Daybreak initiative the artificial intelligence (AI) company announced last month. Calling GPT‑5.5‑Cyber its "strongest model yet for finding and helping patch software vulnerabilities," OpenAI said the model can "sustain deeper analysis across large codebases" to

### Cluster 5858b86279 — score 15

- Title: LastPass confirms data breach in Klue supply chain attack
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-23T13:58:25+00:00
- Link: https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: Salesforce

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion, supply_chain
- affected_products: Salesforce, WordPress
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, data_breach
- affected_products: Salesforce, WordPress
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
LastPass announced that hackers accessed customer data from its Salesforce environment after stealing the company's OAuth tokens in the Klue supply chain attack earlier this month. [...]
```

#### Full body

```
LastPass confirms data breach in Klue supply chain attack By Bill Toulas June 23, 2026 09:58 AM 0 LastPass announced that hackers accessed customer data from its Salesforce environment after stealing the company's OAuth tokens in the Klue supply chain attack earlier this month. The password management platform says its products, services, and infrastructure were not affected by the incident and that customer vaults remained secure. “On June 12th, LastPass was made aware of an incident that occurred at Klue (klue.com), a third-party market intelligence platform utilized by our go-to-market teams, which integrates with our Salesforce and Gong systems,” LastPass says . "We immediately launched an investigation and learned that, as part of this incident, an unauthorized actor was able to obtain OAuth tokens Klue held for many of its customers, including LastPass.” “The threat actor then used these credentials to access LastPass customer data within our Salesforce environment.” The investigation into the incident did not reveal any evidence that the attacker accessed Gong-related data, which typically includes customer calls and emails. According to LastPass, the following data may have been exposed: Customer names Phone numbers Email addresses Physical addresses Support case information Sales/CRM-related data Attackers may leverage the above information in phishing and social engineering attacks. The general recommendation for users is to be cautious of unsolicited communications over the phone or email, especially those that request sensitive details. The master password should not be shared with anyone. The Klue supply chain attack was claimed by the Icarus extortion group , who compromised the infrastructure of the AI-powered market intelligence platform and stole OAuth tokens that connected customers' Salesforce environments. Icarus hackers gained access to Klue's infrastructure using compromised legacy credentials for an integration service. This gave them access to OAuth tokens that connected Klue to various third-party services. The incident impacted multiple organizations , including Recorded Future, Tanium, Jamf, Sprout Social, Gong, and Insurity. The threat actor exfiltrated Customer Relationship Management (CRM) data and launched an extortion campaign. LastPass has disabled employee access to Klue, rotated the exposed API/OAuth tokens, and notified law enforcement while the investigation is underway. The company also warned about the threat actors using the sender domains baccarat.com[.]au, robinskitchen.com[.]au, house[.]com.au, noting that only communications from the official support channels should be trusted. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Klue OAuth breach victim list grows as Icarus hackers claim attack Klue OAuth breach linked to 'Icarus' Salesforce data theft attacks ShapedPlugin update flow hacked to infect WordPress sites OptinMonster WordPress plugin hacked in CDN supply-chain attack Infinite Campus data breach affects 137,000 school staff accounts
```

#### Corroborating sources (5)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: LastPass confirms data breach in Klue supply chain attack
  - Published: 2026-06-23T13:58:25+00:00
  - Link: https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/
  - Summary: LastPass announced that hackers accessed customer data from its Salesforce environment after stealing the company's OAuth tokens in the Klue supply chain attack earlier this month. [...]
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Detecting the Klue supply chain attack in Salesforce instances
  - Published: 2026-06-22T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/detecting-the-klue-supply-chain-attack-in-salesforce/
  - Summary: We summarize the Klue supply chain attack and provide detection guidance for Salesforce environments monitored by Datadog Cloud SIEM.
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Salesforce Data Thefts Continue via Klue App Compromise
  - Published: 2026-06-18T16:49:04+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/salesforce-data-thefts-klue-app-compromise
  - Summary: Klue's Battlecards is now the third integrated application that has been compromised to steal customers' Salesforce data, and victims include Huntress, the cybersecurity vendor.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Salesforce Disables Klue App Integration After OAuth Token Abuse Exposes Customer Data
  - Published: 2026-06-19T09:03:57+00:00
  - Link: https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
  - Summary: Salesforce has revealed that it disabled the Klue Battlecards app integration within its platform in response to a security incident impacting the competitive intelligence company on June 11, 2026. To that end, organizations will be unable to connect to Salesforce via the app until further notice, the American cloud-based software company noted in an alert published this week. "Salesforce took
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Klue Breach Enables Hackers to Compromise Cybersecurity Firms via OAuth Tokens
  - Published: 2026-06-22T10:15:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/klue-breach-compromise/
  - Summary: At least four cybersecurity firms confirmed they have been affected by a breach of business intelligence platform Klue via Salesforce integration

### Cluster 55705936f5 — score 15

- Title: Risky Bulletin: Creds for 74,000 Fortinet devices leaked
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-06-19T05:23:40+00:00
- Link: https://risky.biz/RBNEWS579/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: Fortinet, Ivanti
- content_type: incident_report, news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: Fortinet
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
A LOT of Fortinet creds have leaked online, Canada’s spy agency allowed to remove a botnet from Canadian devices, a supply chain attack hits the Mastra AI framework, and Europol disrupts SocGolish.
```

#### Full body

```
Risky Bulletin Podcast June 19, 2026 Risky Bulletin: Creds for 74,000 Fortinet devices leaked Presented by Catalin Cimpanu News Editor Claire Aird Newsreader A LOT of Fortinet creds have leaked online, Canadaâs spy agency allowed to remove a botnet from Canadian devices, a supply chain attack hits the Mastra AI framework, and Europol disrupts SocGolish. Your browser does not support the audio element. Risky Bulletin: Creds for 74,000 Fortinet devices leaked â¶ 0:00 / 11:00 Subscribe Brought to you by Ent AI Protect the people, secure the system. Show notes Risky Bulletin: Canadaâs spy agency allowed to remove a botnet from Canadian devices
```

#### Corroborating sources (6)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Creds for 74,000 Fortinet devices leaked
  - Published: 2026-06-19T05:23:40+00:00
  - Link: https://risky.biz/RBNEWS579/
  - Summary: A LOT of Fortinet creds have leaked online, Canada’s spy agency allowed to remove a botnet from Canadian devices, a supply chain attack hits the Mastra AI framework, and Europol disrupts SocGolish.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: What the Fortibleed campaign means for organizations running FortiGate firewalls
  - Published: 2026-06-23T14:46:57+00:00
  - Link: https://www.helpnetsecurity.com/2026/06/23/fortibleed-investigation-remediation/
  - Summary: A massive credential-harvesting campaign targeting FortiGate firewalls has exposed thousands of organizations to potential network compromise, and a trove of attacker tools, scripts, and credentials left inadvertently exposed on a server has given researchers an unusually detailed look at how the operation worked. Analysts from ZenoX and CloudSEK have pieced together the full attack chain from the FortiBleed leak, revealing a sophisticated, highly automated pipeline that in some cases achieved full domain-level control of victim … More → The post What the Fortibleed campaign means for organizations running FortiGate firewalls appeared first on Help Net Security .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: FortiBleed campaign used custom FortiGate sniffer to steal credentials
  - Published: 2026-06-22T20:01:02+00:00
  - Link: https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/
  - Summary: Security firm SOCRadar says the large-scale FortiBleed campaign targeting Fortinet FortiGate devices used custom sniffers to harvest authentication secrets from compromised firewalls and steal credentials. [...]
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Attackers hit pair of critical Fortinet vulnerabilities the vendor disclosed in April
  - Published: 2026-06-17T15:42:46+00:00
  - Link: https://cyberscoop.com/fortinet-fortisandbox-vulnerabilities-exploits/
  - Summary: Multiple firms have observed active exploitation of the FortiSandbox defects, and warn that the attacks originate from multiple sources, not a single campaign. The post Attackers hit pair of critical Fortinet vulnerabilities the vendor disclosed in April appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Sweeping Credential-Harvesting Heist Compromises 30K+ Fortinet Devices
  - Published: 2026-06-17T14:06:34+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/sweeping-credential-harvesting-heist-compromises-30k-fortinet-devices
  - Summary: Attackers are actively targeting various sectors across nearly 200 countries and already have compiled a list of working credentials for tens of thousands of compromised devices.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: LATAM Infrastructure Hit by Fortinet and Ivanti Exploits
  - Published: 2026-06-18T11:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/operation-escaneo-cloudsek-latam/
  - Summary: CloudSEK maps Operation Escaneo, a campaign hitting Latin American infrastructure via perimeter bugs

### Cluster a5fdf7dc6d — score 13

- Title: From vulnerability report to CVE draft in minutes: how Elastic automated security advisories with AI
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-06-23T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/security-advisory-automation-rag-elastic-agent-builder
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
How Elastic's security team built an AI agent with RAG against MITRE's CWE and CAPEC catalogues to draft CVE advisories from raw vulnerability reports, including the full prompt and crawler configs.
```

#### Full body

```
23 June 2026 • Paul McCann From vulnerability report to CVE draft in minutes: how Elastic automated security advisories with AI How Elastic's security team built an AI agent with RAG against MITRE's CWE and CAPEC catalogues to draft CVE advisories from raw vulnerability reports, including the full prompt and crawler configs. 11 min read Generative AI Elastic's InfoSec Product Security Team built a generative AI agent using Elastic Agent Builder that drafts complete CVE security advisories (CWE classification, CAPEC methodology, CVSS scoring, and mitigation guidance) directly from raw vulnerability reports. The agent uses RAG against the MITRE CWE and CAPEC catalogues indexed in Elasticsearch, which grounds its output in authoritative data and prevents hallucinated classification IDs. ESA-2026-01 is already in production as an example of output that went through this pipeline. Here's how we built it. How security advisories are drafted manually (and why it's slow) At Elastic, we manage the lifecycle of product vulnerabilities using the PSIRT Service Framework , which defines four stages: discovery, triage, remediation, and disclosure. Each security advisory starts from a vulnerability report received during the discovery phase, and those reports vary widely in quality — translating them into something customers can consume is time-consuming. We draft the security advisory during the disclosure phase, ahead of a planned product release that contains the fix. The advisory is then published as an Elastic Security Advisory (ESA) , with an assigned CVE ID, in the Elastic Security Announcements forum, where anyone can review the disclosed vulnerabilities and the associated mitigations. Each disclosure also gets published into the CVE Program , from which downstream national and regional databases ingest it automatically, including the US National Vulnerability Database (NIST), the EU's European Vulnerability Database (ENISA), and Japan's Japan Vulnerability Notes (JPCERT/CC). To keep our output consistent, we follow the standard Common Vulnerabilities and Exposures (CVE) description template: [PROBLEMTYPE] in [COMPONENT] in [VENDOR] [PRODUCT] [VERSION] on [PLATFORMS] allows [ATTACKER] to [IMPACT] via [VECTOR] The PROBLEMTYPE is identified using a Common Weakness Enumeration (CWE) entry, and the Vector is described using a Common Attack Pattern Enumeration and Classification (CAPEC) entry. Substituting the correct CWE and CAPEC for each vulnerability, the template becomes: [Common Weakness Enumeration] in [COMPONENT] in [VENDOR] [PRODUCT] [VERSION] on [PLATFORMS] allows [ATTACKER] to [IMPACT] via [Common Attack Pattern Enumeration and Classification] The bulk of the manual effort goes into distilling a long, often technically dense vulnerability report into a concise, accurate advisory with a clear impact assessment for customers. Identifying the correct CWE and CAPEC classifications on top of that makes the process convoluted and drawn-out. This is where automation has the most to offer. Automating security advisory drafts with Elastic Agent Builder and RAG To streamline this process, our InfoSec Product Security Team developed a solution that uses an LLM to automatically generate the standardized sentence for security advisories. This solution involves two key steps: Ingesting vulnerability categorization data: Hallucination is a well-documented failure mode for LLMs operating without authoritative grounding. The OWASP Top 10 for LLM Applications (LLM09) lists it as a top risk category, and it was the original motivation for Retrieval-Augmented Generation. We saw it directly in our early experiments: when asked to assign CWE and CAPEC IDs unaided, the model frequently produced plausible-looking but non-existent entries. To prevent this, we used the Elastic Crawler to scrape the CWE and CAPEC websites and ingest the data into two Elasticsearch indices: web-crawl-mitre-cwe-software and web-crawl-mitre-capec-software . Building the gen
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: From vulnerability report to CVE draft in minutes: how Elastic automated security advisories with AI
  - Published: 2026-06-23T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/security-advisory-automation-rag-elastic-agent-builder
  - Summary: How Elastic's security team built an AI agent with RAG against MITRE's CWE and CAPEC catalogues to draft CVE advisories from raw vulnerability reports, including the full prompt and crawler configs.

### Cluster a009d3696a — score 13

- Title: Bridging the Gap Between Code and Research: Why SCORED ’26 Matters for Open Source Security
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-06-23T19:31:53+00:00
- Link: https://openssf.org/blog/2026/06/23/bridging-the-gap-between-code-and-research-why-scored-26-matters-for-open-source-security/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: critical_infrastructure, education
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: critical_infrastructure, education
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Let’s be completely honest about how we’ve historically handled security research: academia and open source practitioners have basically been living on two different planets. That’s why we created SCORED (the Workshop on Software Supply Chain Offensive and Defensive Research). It’s a complete reimagining of the traditional academic model.
```

#### Full body

```
By Justin Cappos, OpenSSF Ambassador, Professor at New York University Introduction: The Evolving Threat Landscape Let’s be completely honest about how we’ve historically handled security research: academia and open source practitioners have basically been living on two different planets. In academia, the primary incentive is publishing, and the magic word is novelty. Because of that, there’s a strong tendency for researchers to write papers that build on what other academics think the problems are, without ever really talking to the people maintaining real-world projects. Meanwhile, open source software is now used in a staggering 98% of all codebases. It is literally the digital foundation of the modern world, and we desperately need more people with the dedicated time and energy to look deeply at its vulnerabilities. But a paper doesn’t secure a repository if a maintainer can’t actually deploy it. That’s why we created SCORED (the Workshop on Software Supply Chain Offensive and Defensive Research) . It’s a complete reimagining of the traditional academic model. We aren’t interested in purely theoretical breakthroughs; we want to publish and promote work that has immediate, practical value to the open source community. Why Co-Location is a Massive Win for the Ecosystem To fix a disconnect, you have to put people in the same room. By co-locating SCORED ’26 with OpenSSF Community Day Europe 2026 in Prague, we are physically bringing academics face-to-face with the cutting edge of open source ecosystems. But the bridge goes deeper than just sharing a venue. We’ve deliberately built our program committee to be heavily drawn from both university faculties and active open source maintainers. We’ve also introduced something I’m incredibly excited about: the Security-in-Practice (SIP) Track. Alongside traditional 11-page research papers, this track features 20-minute talks designed specifically for industry practitioners and maintainers. Personally, I learn an immense amount from hearing from the folks running day-to-day operations for infrastructure like Sigstore or PyPI. Their real-world friction points are exactly what should be guiding academic focus. By bringing practitioners into the fold, we can bust open academic misconceptions and make sure research is actually helpful. 2026 Focus Areas: Solving Tomorrow’s Attack Vectors Today For our 2026 Call for Papers (CFP) , we are focusing heavily on areas where we can drive immediate conflux between research and reality. AI Supply Chains : AI usage has absolutely exploded, making its supply chain security a massive, obvious priority. Reproducible Builds: This tackles one of the most prevalent attack vectors we’ve seen over the last few years. Academics are already deeply engaged here, and we want to cross-pollinate that knowledge with practitioners. Dataset Benchmarking (like SBOMs) : Without effective data, it’s impossible to know what to protect first. Better datasets give us the macro-level visibility we need to understand the overall health – and the hidden weaknesses – of the open source ecosystem. It’s how we move from constantly reacting to fires to proactively preventing them. Call to Action: Shape the Future of Open Source Trust If you’re an academic or a practitioner sitting on the fence about submitting your work before the July 12th deadline, here is my direct pitch to you: If you bring your work to SCORED, it will be scrutinized by the exact community of people who should actually adopt it. This isn’t about padding a resume with another paper; it’s a genuine opportunity to ensure your research has a measurable, positive impact on the real world. Speaking from experience, finding out that code you helped research is protecting millions of users is immensely rewarding. SCORED ’26 Deadlines & Details Submission Deadline (Papers & SIP Talks): July 12, 2026 Author Notification Date: August 22, 2026 Final Materials Due: August 30, 2026 Conference Date: October 6, 2026 Location
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: Bridging the Gap Between Code and Research: Why SCORED ’26 Matters for Open Source Security
  - Published: 2026-06-23T19:31:53+00:00
  - Link: https://openssf.org/blog/2026/06/23/bridging-the-gap-between-code-and-research-why-scored-26-matters-for-open-source-security/
  - Summary: Let’s be completely honest about how we’ve historically handled security research: academia and open source practitioners have basically been living on two different planets. That’s why we created SCORED (the Workshop on Software Supply Chain Offensive and Defensive Research). It’s a complete reimagining of the traditional academic model.

### Cluster bfe56aaca6 — score 13

- Title: F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-18T17:32:14+00:00
- Link: https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-42530

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos
- cve_ids: CVE-2026-42055, CVE-2026-42530, CVE-2026-42945
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: ddos, active_exploitation
- cve_ids: CVE-2026-42530, CVE-2026-42055, CVE-2026-42945
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems. The vulnerabilities are listed below - CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is
```

#### Full body

```
F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution  Ravie Lakshmanan  Jun 18, 2026 Vulnerability / Cloud Security F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems. The vulnerabilities are listed below - CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is configured to use the HTTP/3 QUIC module to reopen a QPACK encoder stream by means of a specially crafted HTTP/3 session, and execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. CVE-2026-42055 (CVSS v4 score: 9.2) - A heap-based buffer overflow vulnerability in the ngx_http_proxy_v2_module and ngx_http_grpc_module modules that could be triggered by a remote unauthenticated attacker when the proxy_http_version to 2 or grpc_pass directives are used to proxy HTTP/2 traffic, the ignore_invalid_headers directive is set to off, and the large_client_header_buffers directive size is larger than 2 MB, and execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Both shortcomings have been patched in the following versions - CVE-2026-42530 - NGINX Open Source 1.31.0 - 1.31.1 (Fixed in 1.31.2) NGINX Gateway Fabric 2.0.0 - 2.6.3 (Fixed in 2.6.4) NGINX Gateway Fabric 1.3.0 - 1.6.2 NGINX Instance Manager 2.17.0 - 2.22.0 NGINX Ingress Controller 5.0.0 - 5.5.0 NGINX Ingress Controller 4.0.0 - 4.0.1 NGINX Ingress Controller 3.5.0 - 3.7.2 CVE-2026-42055 - NGINX Plus 37.0.0 - 37.0.1 (Fixed in 37.0.2.1) NGINX Plus R33 - R36 (Fixed in R36 P6) NGINX Open Source 1.31.1 (Fixed in 1.31.2) NGINX Open Source 1.30.0 - 1.30.2 (Fixed in 1.30.3) NGINX Instance Manager 2.17.0 - 2.22.0 F5 WAF for NGINX 5.9.0 - 5.13.1 NGINX App Protect WAF 5.2.0 - 5.8.0 NGINX App Protect WAF 4.10.0 - 4.16.0 F5 DoS for NGINX 4.9.0 NGINX App Protect DoS 4.3.0 - 4.7.0 NGINX Gateway Fabric 2.0.0 - 2.6.3 (Fixed in 2.6.4) NGINX Gateway Fabric 1.3.0 - 1.6.2 NGINX Ingress Controller 5.0.0 - 5.5.0 NGINX Ingress Controller 4.0.0 - 4.0.1 NGINX Ingress Controller 3.5.0 - 3.7.2 As mitigations, F5 has outlined the following actions - CVE-2026-42530 - Disable HTTP/3 CVE-2026-42055 - Remove the ignore_invalid_headers off directive from the configuration, or reduce the large_client_header_buffers directive size below 2 MB Although F5 makes no mention of the vulnerabilities being exploited in the wild, security flaws in F5 products have been repeatedly exploited by bad actors. As recently as last month, another critical security defect in NGINX Plus and NGINX Open Source ( CVE-2026-42945 , CVSS score: 9.2), also called NGINX Rift, came under active exploitation within days after public disclosure. Update CyStack's Trung Nguyen, who is credited as one of the researchers behind discovering and reporting both the flaws, described CVE-2026-42530 as resulting from a "lifetime mismatch," which could then trigger the use-after-free primitive. "A pointer that belongs to the HTTP/3 session, which lives for the duration of the connection, ends up holding memory that belongs to a unidirectional stream that lives only for a moment," Nguyen said . "When that stream closes, the memory is freed, but the session-level pointer is still there and is still treated as valid." CVE-2026-42055, on the other hand, is a heap overflow that causes attacker-controlled HPACK data to be written to unauthorized memory regions without requiring any authentication. The oversized requests can be exploited to cause repeated worker process crashes, resulting in a sustained denial-of-service (DoS). "The request builder reserves a fixed 4 bytes for the length prefix of an HPACK string, but the HPACK varint encoder emits 5 bytes when the length value exceeds 2097278," Nguyen explained . "E
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution
  - Published: 2026-06-18T17:32:14+00:00
  - Link: https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html
  - Summary: F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems. The vulnerabilities are listed below - CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Use-after-free in the QPACK encoder of nginx HTTP/3 - CVE-2026-42530
  - Published: 2026-06-19T19:15:45+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1uab0j6/useafterfree_in_the_qpack_encoder_of_nginx_http3/
  - Summary: submitted by /u/everping [link] [comments]

### Cluster 61b6596951 — score 12

- Title: Why SIEM is Moving Toward Unified Security Operations: Rapid7 Named a Major Player in IDC MarketScape
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-23T17:03:34+00:00
- Link: https://www.rapid7.com/blog/post/dr-siem-moving-toward-unified-security-operations-rapid7-named-idc-marketscape-major-player
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
Rapid7 has been named a Major Player in the IDC MarketScape: Worldwide SIEM 2026 Vendor Assessment (#US54126826, June 2026). This is the first IDC SIEM MarketScape to bring the enterprise and SMB markets into a single evaluation, and we believe it arrives at a time when the way teams buy and run a SOC is changing quickly. Security teams are no longer evaluating detection and response in isolation. They want their threat data, automation, and view of the attack surface working together, rather than spread across a stack of disconnected tools. We believe Incident Command reflects that shift by bringing threat data, automation, and attack surface context into one platform instead of leaving teams to work across disconnected tools. It also speaks to a broader change in security operations, where context matters more, speed matters more, and teams need a clearer path from alert to action. That same direction runs through Rapid7’s wider point of view on preemptive security: exposure, detecti
```

#### Full body

```
Back to Blog Detection and Response Why SIEM is Moving Toward Unified Security Operations: Rapid7 Named a Major Player in IDC MarketScape Rapid7 Jun 23, 2026 | Last updated on Jun 23, 2026 | 4 min read DISCOVER NEXT-GEN SIEM Rapid7 has been named a Major Player in the IDC MarketScape: Worldwide SIEM 2026 Vendor Assessment (#US54126826, June 2026). This is the first IDC SIEM MarketScape to bring the enterprise and SMB markets into a single evaluation, and we believe it arrives at a time when the way teams buy and run a SOC is changing quickly. Security teams are no longer evaluating detection and response in isolation. They want their threat data, automation, and view of the attack surface working together, rather than spread across a stack of disconnected tools. We believe Incident Command reflects that shift by bringing threat data, automation, and attack surface context into one platform instead of leaving teams to work across disconnected tools. It also speaks to a broader change in security operations, where context matters more, speed matters more, and teams need a clearer path from alert to action. That same direction runs through Rapid7’s wider point of view on preemptive security: exposure, detection, and response work better when they inform each other through shared context, AI, and human expertise. Incident Command brings detection, response, and exposure context together Incident Command brings SIEM, SOAR, attack surface management, and threat intelligence together on a shared data model. That gives analysts access to asset risk, vulnerability data, and exposure context during an investigation, so they can understand whether a detection affects a high-risk, internet-facing asset without having to jump between separate products. According to the IDC MarketScape, “Incident Command is a strong fit for midmarket to enterprise organizations that want a fully integrated security operations platform with predictable costs.” The teams we talk to are tired of stitching tools together and dealing with surprise ingestion bills. They want fewer blind spots, faster investigations, and a clearer answer to what is urgent and what to do next. Incident Command addresses that by bringing exposure context, threat intelligence, and response automation into the SIEM workflow, helping teams investigate faster and act with more clarity. For organizations looking for additional managed coverage, Rapid7 MDR is available as a separate offering. As attacks move faster and environments become harder to manage, security operations work better when exposure, threat, and response data are connected through an open platform that gives teams the context they need to move with more speed and clarity. AI and automation, pressure-tested by a global SOC Many vendors talk about AI in the SOC. For customers, the more important question is how those capabilities are developed, tested, and refined so they are useful in real investigations rather than just sounding good in a product story. We believe the IDC MarketScape called out what that means in Rapid7’s case: “AI models and automation capabilities are tested in the MDR SOC before release to product customers, providing a feedback loop between managed service outcomes and product development that organizations without their own MDR equivalent cannot replicate.” Our MDR analysts work real incidents across thousands of customer environments every day. The detections, triage models, and automation that come out of that work are tested against live attacks before they reach product customers. That feedback loop helps make the AI Engine more useful in practice by handling repetitive work such as classifying alerts, compiling evidence, and surfacing next steps, while analysts spend their time on the decisions that actually require human judgment. That balance also reflects Rapid7’s broader platform story: AI-powered, backed by human expertise. What we believe this IDC MarketScape recognition says about the f
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Why SIEM is Moving Toward Unified Security Operations: Rapid7 Named a Major Player in IDC MarketScape
  - Published: 2026-06-23T17:03:34+00:00
  - Link: https://www.rapid7.com/blog/post/dr-siem-moving-toward-unified-security-operations-rapid7-named-idc-marketscape-major-player
  - Summary: Rapid7 has been named a Major Player in the IDC MarketScape: Worldwide SIEM 2026 Vendor Assessment (#US54126826, June 2026). This is the first IDC SIEM MarketScape to bring the enterprise and SMB markets into a single evaluation, and we believe it arrives at a time when the way teams buy and run a SOC is changing quickly. Security teams are no longer evaluating detection and response in isolation. They want their threat data, automation, and view of the attack surface working together, rather than spread across a stack of disconnected tools. We believe Incident Command reflects that shift by bringing threat data, automation, and attack surface context into one platform instead of leaving teams to work across disconnected tools. It also speaks to a broader change in security operations, where context matters more, speed matters more, and teams need a clearer path from alert to action. That same direction runs through Rapid7’s wider point of view on preemptive security: exposure, detecti

### Cluster 115f04b624 — score 11

- Title: The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration
- Source: Unit 42 (threat_research_primary)
- Published: 2026-06-22T22:00:04+00:00
- Link: https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: AWS, Azure, Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Azure, AWS, Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 research details how attackers could exploit global name uniqueness in bucket hijacking to redirect cloud data streams across major CSPs. The post The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Cloud Cybersecurity Research Cloud Cybersecurity Research The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration 13 min read Related Products Cortex Cortex Cloud Unit 42 Cloud Security Assessment Unit 42 Incident Response By: Yahav Festinger Published: June 22, 2026 Categories: Cloud Cybersecurity Research Threat Research Tags: AWS Bucket hijacking Cloud data exfiltration Cloud logging CSPs Google Cloud IAM Microsoft Azure Privilege escalation Share Executive Summary We recently identified a bucket hijacking technique impacting multiple services across major cloud service providers (CSPs). The attack technique exploits a fundamental architectural flaw that is common across cloud providers and could potentially affect other cloud providers as well. Our research reveals that an attacker can silently compromise an organization's active data streams by rerouting data into an external storage bucket. Because a storage bucket name is globally unique, an attacker can simply delete the bucket and then recreate it under the attacker's own account using the same name. This therefore creates a global namespace risk. This bucket hijacking reroutes critical logs and sensitive data directly to the attacker’s environment. We have shared these findings with Google Cloud, Amazon Web Services (AWS), and Microsoft Azure. We have not yet identified a real-world threat actor using this attack technique. However, we recommend organizations take steps now to head off the potential impact, particularly since we anticipate that real-world attempts to use this attack technique would be difficult to detect. Palo Alto Networks customers are better protected from the threats discussed above through the following products and services: Cortex Cloud Unit 42 Cloud Security Assessment can help turn cloud complexity into actionable security insights. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Cloud Logging , Google Cloud , AWS , Microsoft Azure Key Architectural Elements Enabling the Attack Before detailing the attack methodology, it’s important to understand several architectural elements that, when combined, make bucket hijacking possible. Data Stream Overview A data stream is an automated, continuous pipeline designed for high-volume data movement between services. Once configured, these streams operate autonomously in the background to push telemetry, audit logs or objects from a source environment to a designated storage destination for processing and long-term retention. Major CSPs facilitate automated data streams. These streams serve as critical nodes for routing, processing and backing up data within an organization's infrastructure, such as: A cloud logging sink in Google Cloud acts as a router for log entries, directing them to a chosen destination. While primarily used to route and store logs in centralized log buckets for purposes like analysis and retention, a sink can also export logs to a Google Cloud Storage (GCS) bucket. Bucket replication in AWS is a feature that automatically duplicates data from a source S3 bucket to a designated destination S3 bucket. Global Uniqueness of Bucket Names Cloud environments often stream data into buckets such as an S3 bucket in AWS or a GCS bucket in Google Cloud. Because bucket names are typically unique across the entire cloud provider, no two users can have the same bucket name. This design simplifies data stream establishment by providing a single, predictable target. However, it also creates a shared namespace where a destination's identity is tied solely to its name, rather than to a specific, immutable account owner. This characteristic is the foundational logic behind our discovery. Permissions to Modify Data Stream Destinations The data stream is frequently defined by a routing resource that is configured with a specific destinatio
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration
  - Published: 2026-06-22T22:00:04+00:00
  - Link: https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/
  - Summary: Unit 42 research details how attackers could exploit global name uniqueness in bucket hijacking to redirect cloud data streams across major CSPs. The post The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration appeared first on Unit 42 .

### Cluster f371ac3a1c — score 11

- Title: The Purchase Scam Tactic Headed for the World Cup | Recorded Future
- Source: Recorded Future (threat_research_primary)
- Published: 2026-06-23T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/world-cup-purchase-scam-tactics
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
A purchase scam tactic hijacks organic search through compromised sites, and it’s built to scale into 2026 FIFA World Cup fraud. How it works and how to respond.
```

#### Full body

```
The Purchase Scam Tactic Headed for the World Cup Recorded Future's Payment Fraud Intelligence team continues to monitor a purchase scam tactic that pulls victims from organic search rather than paid ads by compromising legitimate websites. The scam domains never appear in search results themselves, which means the operations are likely hidden from standard search monitoring and could survive the takedown of any single domain or merchant account. The same tactic is already surfacing in World Cup-themed fraud, and it’s positioned to scale across event-driven scams through 2026. Why this matters now Major sporting events concentrate consumer demand. Fans rush to buy tickets, merchandise, and travel in a short window, and purchase scams follow that demand wherever it spikes. Recorded Future's Payment Fraud Intelligence team has been analyzing a purchase scam tactic built for exactly this kind of event-driven demand. The tactic amounts to SEO poisoning of legitimate websites. What’s most notable isn’t the scam itself but how it finds victims: through organic search results captured by compromising legitimate websites, without the scammers ever buying ads or acquiring their own domains to rank. Purchase scams, briefly As explained in this report , the basic purchase scam model is simple. A site advertises real-looking goods at steep discounts, takes payment, and never ships the product. The usual draw is social media advertising that points to brand impersonation sites. For many victims of purchase scams, the crime doesn’t stop there. The fraudsters operating the scams also steal the payment card data of their “customers,” resulting in a string of unauthorized charges if the theft isn’t quickly noticed. Figures 1-2: Search results showing potential purchase scam pages injected into legitimate websites, and the purchase scam website that visitors are redirected to (Source: Recorded Future) How the tactic works Getting a brand-new scam domain to rank highly in search results normally requires expensive search engine optimization work. By embedding redirects on legitimate, well-ranked sites, scammers can route organic traffic to purchase scam domains without needing to invest in SEO themselves. The Payment Fraud Intelligence team has observed that scammers are using a consistent four-step pattern: Gain unauthorized access to a legitimate website. Plant fake product listings and metadata for search crawlers on that site. Co-opt the site's existing search ranking to attract shoppers. Redirect visitors who arrive from a search result to the scam domains. The redirect is selective: The injected code only fires for visitors who arrive from a search result carrying a specific tracking parameter. Regular visitors and the site's own administrators see the real site, so the compromise often stays undetected. This conditional behavior is a form of cloaking, and it’s what makes the activity so hard to spot. Additionally, there’s a second layer of concealment. The scam domains themselves aren’t indexed by search engines. Only the compromised pages are indexed, so the infrastructure that actually takes payment stays out of view of researchers and security monitoring. Why it’s effective and hard to defend against The economics favor the attacker. The tactic captures organic search traffic without scammers having to pay for the ads or SEO that ranking normally demands, and it generally evades both ad-platform detection and standard search monitoring. Resilience is built in. Operators rotate domains, branding, and content from shared templates, and they distribute payments across several merchant accounts, so the operation can survive the takedown of any single domain or account. The approach monetizes traditionally lower-value targets. When fraudsters scan for vulnerable websites and compromised admin credentials, they seek e-commerce websites with checkout pages that can be infected with e-skimmers. With this purchase scam scheme, the fraudsters fi
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: The Purchase Scam Tactic Headed for the World Cup | Recorded Future
  - Published: 2026-06-23T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/world-cup-purchase-scam-tactics
  - Summary: A purchase scam tactic hijacks organic search through compromised sites, and it’s built to scale into 2026 FIFA World Cup fraud. How it works and how to respond.

### Cluster b9a7dc6e90 — score 11

- Title: Build your own vulnerability harness
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-06-18T17:59:40+00:00
- Link: https://blog.cloudflare.com/build-your-own-vulnerability-harness/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
We break down the technical architecture behind our multi-stage vulnerability discovery harness and automated triage loop. Learn how we manage state controls, squash false positives through adversarial review, and route around LLM context limits.
```

#### Full body

```
Build your own vulnerability harness 2026-06-18 Dan Jones Alexandra Godoi Grant Bourzikas 17 min read A few weeks ago, we published our initial findings from Project Glasswing , looking at what happens when you point frontier security models at an enterprise codebase. We also explored how our defensive structures adapt to protect our infrastructure and customers from threats posed by frontier AI . Since then, the AI ecosystem has continued to shift rapidly â developers who've built tightly around a single model have already experienced what happens when that model is no longer available or gets superseded by a more capable one. These market shifts only reinforce our core thesis: no matter which underlying model is leading the pack on any given day, the future of agentic workflows will not be found in standalone models, prompts, or single-agent sessions. Moving from a localized security "skill" to a continuous, fleet-wide scanning pipeline requires an architecture where models are treated as interchangeable components. Relying on a single model inherently limits defensive coverage, as the same system will tend to look at code paths through the exact same lens. To counter this, models should be frequently interchanged and cross-tested. By varying the models across the pipeline â such as using one model for initial discovery and an entirely different one for validation â we can ensure that vulnerabilities are cross-checked by distinct sets of logic. Furthermore, a true enterprise-scale harness must look beyond isolated repositories to trace vulnerabilities across cross-repo dependencies, ultimately filtering thousands of raw candidates down to a trusted, triaged queue of actionable fixes. This post serves as a practical look at how to build that model-agnostic layer, focusing on how we manage state controls, eliminate false positives, and coordinate end-to-end triage at scale. Two objections, up front The first post made the case for why generic coding agents can't do this job. The main issue is that agents only hold one hypothesis at a time, fill their context window after covering a sliver of a real repo, and then lose information during context compaction. For more details, read that post . Before we move forward, we would like to answer two likely questions. "Why not use subagents instead of a harness?" Subagents are useful, and they are a good starting point. But security analysis needs hundreds of separate investigations that survive across runs, don't share a context window, and can be re-scoped and cross-referenced later. It needs persistence, deduplication, resumability, and eventually fleet-wide dependency tracing. That's an orchestration problem, and a prompt can't get you there. "Is this blog post just an ad for frontier models?" No. Our approach centers on the harness, not the model. When it comes to vulnerability discovery, we run it with whatever frontier model is currently best at what we need. When we point different models at the same target, they each turn up a different share of the bugs. The harness is the bit that lasts. If you build your own system, design it to be model-agnostic from day one. This will allow you the freedom to use any model of choice without constraints. It all starts with a skill We started with a ~450-line security-audit skill that we ran on a single repository, and adjusted the prompts until we surfaced real bugs. Later, we added the orchestration that became the plumbing of the entire system. The real value lives in the prompts themselves, and our prompts continue to carry the initial skill's attacker scenarios, bug classes, and anti-pattern detections nearly unchanged. The skill was written to run a 7-phase audit in one session: Three parallel research agents do recon and write an architecture.md . One Hunter agent runs per class attack, trying to break the code rather than review it. Adversarial validators try to disprove each finding. The survivors are written up as a human-re
```

#### Corroborating sources (1)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: Build your own vulnerability harness
  - Published: 2026-06-18T17:59:40+00:00
  - Link: https://blog.cloudflare.com/build-your-own-vulnerability-harness/
  - Summary: We break down the technical architecture behind our multi-stage vulnerability discovery harness and automated triage loop. Learn how we manage state controls, squash false positives through adversarial review, and route around LLM context limits.

### Cluster d29e7e479c — score 11

- Title: Scattered Spider Hackers Plead Guilty on Day 1 of Trial
- Source: Krebs on Security (practitioner_analysis)
- Published: 2026-06-23T16:12:49+00:00
- Link: https://krebsonsecurity.com/2026/06/scattered-spider-hackers-plead-guilty-on-day-1-of-trial/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: Scattered Spider

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion
- actor_attribution: Scattered Spider
- affected_industries: financial_services, government, healthcare
- content_type: news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng
- actor_attribution: Scattered Spider
- affected_industries: healthcare, financial_services, government
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Two men pleaded guilty in the United Kingdom this week to criminal charges stemming from an August 2024 cyberattack that crippled Transport for London, the entity responsible for the public transport network in the Greater London area. The duo were key members of a prolific cybercrime group known as Scattered Spider, and their guilty pleas came on the first day of what was expected to be a six-week trial.
```

#### Full body

```
Two men pleaded guilty in the United Kingdom this week to criminal charges stemming from an August 2024 cyberattack that crippled Transport for London , the entity responsible for the public transport network in the Greater London area. The duo were key members of a prolific cybercrime group known as Scattered Spider , and their guilty pleas came on the first day of what was expected to be a six-week trial. Owen Flowers (left) 18, and Thalha Jubair, 20. Image: UK National Crime Agency (NCA). Thalha Jubair , 20, of East London and 18-year-old Owen Flowers of Walsall admitted conspiring to commit unauthorized acts against Transport for London computer systems and causing risk of serious damage to human welfare. According to a report from the BBC, Flowers alone admitted to being part of a conspiracy to hack into U.S. based healthcare providers SSM Health Care Corporation and Sutter Health in September 2024. Jubair is also wanted by U.S. law enforcement agencies. In September 2025, prosecutors in New Jersey unsealed an indictment alleging Jubair and other Scattered Spider members committed computer fraud, wire fraud, and money laundering in relation to 120 computer network intrusions involving 47 U.S. entities between May 2022 and September 2025, and that the group’s victims paid at least $115 million in ransom payments. In July 2025, KrebsOnSecurity reported that Flowers and Jubair were arrested in the United Kingdom in connection with Scattered Spider ransom attacks against the retailers Marks & Spencer and Harrods , and the British food retailer Co-op Group . Multiple sources familiar with those investigations said Flowers was the Scattered Spider member who anonymously gave interviews to the media in the days after the group’s September 2023 ransomware attacks disrupted operations at Las Vegas casinos operated by MGM Resorts and Caesars Entertainment . According to prosecutors, Jubair co-ran a bustling Telegram channel called Star Chat , the home of a SIM-swapping group that used voice- and SMS-based phishing attacks to steal credentials from employees at the major wireless providers in the U.S. and U.K. The group would then use that access to sell a service that could redirect a target’s phone number to a device the attackers controlled and intercept the victim’s calls and text messages (including one-time codes for multi-factor authentication). A receipt from Star Fraud Chat’s SIM-swapping service targeting a T-Mobile customer after the group gained access to internal T-Mobile employee tools. “Rocket Ace” was one of Jubair’s hacker handles, according to U.S. prosecutors. New Jersey prosecutors also allege Jubair also was involved in a mass SMS phishing campaign during the summer of 2022 that stole single sign-on credentials from employees at hundreds of companies. That weeks-long SMS phishing campaign led to intrusions and data thefts at more than 130 organizations, including LastPass , DoorDash , Mailchimp , Plex and Signal . KrebsOnSecurity reported last year that one of Jubair’s alter egos at age 15 was “ Everlynn ,” a hacker who sold fraudulent “emergency data requests” that used compromised police and government email addresses to demand subscriber data (e.g. username, IP/email address) from major tech companies, claiming the requests concerned urgent matters of life and death and could not wait for a court order. In April 2026, 24-year-old British national and Scattered Spider member Tyler “Tylerb” Buchanan pleaded guilty to wire fraud conspiracy and aggravated identity theft for participating in the group’s SMS phishing spree in the summer of 2022. The government said Buchanan, Jubair and others used the credentials harvested in that phishing campaign to steal at least $8 million in cryptocurrency from victims throughout the United States. Buchanan is currently scheduled to be sentenced on October 2. In August 2025, 20-year-old Scattered Spider member from Florida named Noah Michael Urban was sentenced to 10 years in
```

#### Corroborating sources (4)

- **Krebs on Security** (practitioner_analysis)
  - Title: Scattered Spider Hackers Plead Guilty on Day 1 of Trial
  - Published: 2026-06-23T16:12:49+00:00
  - Link: https://krebsonsecurity.com/2026/06/scattered-spider-hackers-plead-guilty-on-day-1-of-trial/
  - Summary: Two men pleaded guilty in the United Kingdom this week to criminal charges stemming from an August 2024 cyberattack that crippled Transport for London, the entity responsible for the public transport network in the Greater London area. The duo were key members of a prolific cybercrime group known as Scattered Spider, and their guilty pleas came on the first day of what was expected to be a six-week trial.
- **The Record** (cyber_news_breach_reporting)
  - Title: Two Scattered Spider members plead guilty over cyberattack that crippled London transit
  - Published: 2026-06-23T13:00:00+00:00
  - Link: https://therecord.media/guilty-plea-tfl-cyberattack-scattered-spider-members
  - Summary: A 20-year-old and an 18-year-old admitted to infiltrating the network of Transport for London in 2024, disrupting public transportation services for months.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Two Scattered Spider hackers plead guilty over Transport for London cyberattack
  - Published: 2026-06-23T09:59:48+00:00
  - Link: https://www.helpnetsecurity.com/2026/06/23/transport-london-cyberattack-scattered-spider-members-plead-guilty/
  - Summary: Two members of the notorious hacker group Scattered Spider have pleaded guilty to charges related to a 2024 cyberattack on Transport for London (TfL) that resulted in £29 million in loss and recovery costs. Thalha Jubair, 20, from London, and Owen Flowers, 18, from Walsall, pleaded guilty at a court hearing in London to offences under the UK’s Computer Misuse Act and will be sentenced on July 16. TfL, the public body responsible for much … More → The post Two Scattered Spider hackers plead guilty over Transport for London cyberattack appeared first on Help Net Security .
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Scattered Spider Teens Convicted of TfL Cyber-Attack
  - Published: 2026-06-23T09:29:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/scattered-spider-teens-convicted/
  - Summary: Two young British men have pleaded guilty to hacking Transport for London as part of a Scattered Spider plot

### Cluster b8988e5561 — score 11

- Title: GitHub Updates actions/checkout to Block Common Pwn Request Attack Patterns
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-23T14:22:03+00:00
- Link: https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html
- Fetch status: ok
- Member count: 7
- Corroborating source count: 4
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain
- affected_industries: financial_services
- affected_products: GitHub, Kubernetes, WordPress
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: GitHub, Kubernetes
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
GitHub is moving to strengthen software supply chain security by updating "actions/checkout" to block pwn request attacks that exploit the risky use of the "pull_request_target workflow" trigger to run malicious code with the workflow's full privileges. Effective June 18, 2026, the latest version of "actions/checkout," the official GitHub action for checking out a repository into the
```

#### Full body

```
GitHub Updates actions/checkout to Block Common Pwn Request Attack Patterns  Ravie Lakshmanan  Jun 23, 2026 Workflow Security / Software Supply Chain GitHub is moving to strengthen software supply chain security by updating " actions/checkout " to block pwn request attacks that exploit the risky use of the "pull_request_target workflow" trigger to run malicious code with the workflow's full privileges. Effective June 18, 2026, the latest version of "actions/checkout," the official GitHub action for checking out a repository into the workflow's runner, refuses common pwn request patterns by default. The change is expected to be backported to all currently supported major versions on July 16, 2026. "Actions/checkout v7 refuses to fetch fork pull request code in pull_request_target and workflow_run workflows (the latter only when workflow_run.event is a pull_request* event)," it added . The refusal occurs when the pull request is from a fork, and any of the following criteria is met, unless workflow authors explicitly opt out of it by setting the " allow-unsafe-pr-checkout " flag to "true" in "actions/checkout" - repository: resolves to the fork pull request' repository ref: matches refs/pull/number/head or refs/pull/number/merge ref: resolves to a fork pull request's head or merge commit SHA The change is aimed at preventing the most common form of pwn requests in the Actions ecosystem. As a result, "actions/checkout" will fail for "pull_request_target events" from forks with insecure inputs. "Pull_request_target" is a workflow trigger that's automatically run without requiring manual approval when a pull request is opened or reopened, or when the head branch of the pull request is updated. It's important to note that the event runs in the context of the default branch of the base repository, potentially exposing secrets and a privileged GITHUB_TOKEN with both read and write permissions. "Running untrusted code on the pull_request_target trigger may lead to security vulnerabilities," GitHub notes in its documentation. "These vulnerabilities include cache poisoning and granting unintended access to write privileges or secrets." The danger arises when a "pull_request_target" is combined with "actions/checkout" to download and execute code submitted by an untrusted fork. Should a bad actor submit a pull request containing malicious scripts and the workflow checks out and runs the code, it can allow the attacker to steal the GITHUB_TOKEN and other secrets, leading to what's called a pwn request attack . "Workflows triggered by pull_request_target run with the base repository's GITHUB_TOKEN, secrets, and default-branch cache access," GitHub said. "Checking out the head of an unreviewed pull request from a fork inside one of these workflows typically lets attacker-controlled code execute with the workflow's full privileges." In recent months, a number of software chain attacks have weaponized this behavior. The most severe of them was the compromise of multiple packages associated with the Nx build system as part of a campaign codenamed s1ngularity, as well as the breach of PostHog , TanStack , and the popular Emacs package, " kubernetes-el/kubernetes-el ." "Pull_request_target was designed for trusted automation around pull requests, such as labeling, commenting, or applying project metadata," Socket said. "But the checkout step controls which code actually lands in the runner workspace. If it pulls code from a forked pull request, the workflow can end up running attacker-controlled code with the base repository's privileges." That said, the Microsoft-owned subsidiary emphasized that pwn requests triggered via other event types besides pull_request_target (e.g., issue_comment) or through other means, such as git or the GitHub CLI, are out of scope of this change. "This change only blocks checkouts of the fork pull request head and merge commits," it added. "It does not block checkouts of other untrusted repositories. For example, s
```

#### Corroborating sources (4)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: GitHub Updates actions/checkout to Block Common Pwn Request Attack Patterns
  - Published: 2026-06-23T14:22:03+00:00
  - Link: https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html
  - Summary: GitHub is moving to strengthen software supply chain security by updating "actions/checkout" to block pwn request attacks that exploit the risky use of the "pull_request_target workflow" trigger to run malicious code with the workflow's full privileges. Effective June 18, 2026, the latest version of "actions/checkout," the official GitHub action for checking out a repository into the
- **TrustedSec** (detection_response_operations)
  - Title: Modern Web Application Content Discovery
  - Published: 2026-06-18T04:00:00+00:00
  - Link: https://trustedsec.com/blog/modern-web-application-content-discovery
  - Summary: <p>Staring at a web app with no links and no navigation? In this blog, we break down modern content discovery, from forced browsing and web crawling to Google dorking and GitHub recon.</p>
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Crypto Heist Fueled by Elaborate Fake Reputation-Boosting Campaign
  - Published: 2026-06-22T16:10:10+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/crypto-heist-fake-reputation-boosting-campaign
  - Summary: Attackers are using multiple online channels — including GitHub, YouTube, and VirusTotal — to build an illusion of trust to spread a cross-platform clipboard hijacker.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Serverless Phishing Kit on GitHub Targets Mexican Banks
  - Published: 2026-06-17T14:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/gitbait-github-pages-sheetbest/
  - Summary: GitBait phishing kit abuses GitHub Pages and the SheetBest API to steal Mexican banking credentials

### Cluster 84319555f9 — score 10

- Title: Threat Brief: Mitigating Large-Scale Credential Attacks
- Source: Unit 42 (threat_research_primary)
- Published: 2026-06-20T02:05:33+00:00
- Link: https://unit42.paloaltonetworks.com/large-scale-credential-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We provide guidance for preparing for and mitigating large-scale credential attacks, focusing on recent campaigns targeting security vendors' devices. The post Threat Brief: Mitigating Large-Scale Credential Attacks appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center High Profile Threats General General Threat Brief: Mitigating Large-Scale Credential Attacks 4 min read Related Products Next-Generation Firewall Unit 42 Incident Response By: Andy Piazza Published: June 19, 2026 Categories: General High Profile Threats Tags: Credential theft Fortibleed Password spraying Share Unit 42 is aware of a large-scale password spraying and credential theft campaign (“FortiBleed”) against Fortinet devices. We observed attempts targeting MSSQL devices as well, and have seen reports of Sophos devices also being targeted. While this activity is not targeting Palo Alto Networks devices, Unit 42 has observed suspicious login attempts in customer telemetry and we are providing this report out of an abundance of caution to ensure our customers have the latest intelligence and product recommendations to protect, detect and respond to attacks to their network. The threat actors are using a curated password list to attempt password spraying against services exposed to the internet. Unit 42 assesses that the initial password list for this activity was likely developed through a mix of previous breaches, including the successful exploitation of vulnerabilities. Once they obtain credentials, they add them to their password list for future attempts against additional targets, as well as for logging into accounts they successfully compromised. The threat actors are leveraging a multi-stage process to gain persistent, high-privilege access: Password spraying for initial access: Massive internet-wide scanning and password spraying attempts against Fortinet, Sophos and MSSQL services Configuration Extraction: Depending on the permissions of their initial access, the actor may exploit a privilege escalation vulnerability prior to pulling device configuration files, including stored credentials Offline Cracking: Offline password cracking of the stolen credentials adds to the password list used in step one to target new devices, as well as to log into compromised devices to establish persistence as an administrator Unit 42 observed an initial access broker (IAB) on the Russian-language cybercrime forum Exploit[.]in claiming responsibility for this campaign, referencing a CVE (no further information), and offering the harvested credentials for sale on June 16, 2026. Unit 42 has not validated their claims at this time. Figure 1. Darkweb post of IAB selling credentials. Unit 42 recommends auditing remote access logs for suspicious activity with a focus on successful logins shortly after large volume password failure events. We also recommend reviewing and implementing the hardening guidance below for edge devices. SOCRadar provided the initial reporting on the targeting of FortiGate devices. We observed attempts targeting MSSQL devices as well, and have seen reports of Sophos devices also being targeted. Palo Alto Networks customers receive assistance protecting against and mitigating credential attacks in the following ways: PAN-OS uses a Master Key to encrypt cryptographic keys in either ES-256-CBC or AES-256-GCM encryption algorithm PAN-OS only stores SHA-256 encrypted and salted hashes Customers can integrate several MFA platforms to enhance their security posture Customers can customize Password Profiles and complexity Customers can follow our Administrative Access Best Practices Palo Alto Networks also recommends the following hardening guidelines: Require MFA: Require multi-factor authentication for all remote services. NGFW customers can integrate several MFA platforms and customize their Password Profiles and complexity to enhance their security posture. Adopt Zero Trust Architecture: Leverage “jump boxes” and Zero Trust Network Access (ZTNA) policies to ensure management interfaces are never exposed directly to the public internet, further narrowing the attack surface for configuration extraction. Change Default Credentials: Change the credentials for default accounts, ensuring long, complex p
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: Mitigating Large-Scale Credential Attacks
  - Published: 2026-06-20T02:05:33+00:00
  - Link: https://unit42.paloaltonetworks.com/large-scale-credential-attacks/
  - Summary: We provide guidance for preparing for and mitigating large-scale credential attacks, focusing on recent campaigns targeting security vendors' devices. The post Threat Brief: Mitigating Large-Scale Credential Attacks appeared first on Unit 42 .

### Cluster 5362786b4f — score 10

- Title: Guarding AI memory
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-22T19:07:28+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_industries: government
- affected_products: Microsoft 365, Microsoft/Copilot
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ai_security
- affected_industries: government
- affected_products: Microsoft/Copilot, Microsoft 365
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
What happens when threat actors target what AI remembers? Microsoft breaks down the risks and the defenses. The post Guarding AI memory appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Security Copilot Topics Actionable threat insights AI and agents AI memory transforms an AI system from a stateless tool into a learning collaborator. That unlocks powerful experiences, but it also increases the attack surface of the AI system. Without memory, attackers need to achieve their objective in a single prompt. With AI memory, they can shape behavior gradually over time or plant memories that influence agent reasoning after the original context is gone and user awareness is lower. Microsoft takes a defense-in-depth approach to protect AI memory spanning every layer of the stack: storage, retrieval, model interaction, and user control. What AI memory is (and why it matters) AI systems use memory to retain and recall information across interactions. This information is then used to shape future behavior. This enables: Personalization : Agents gain a deep understanding of the user’s preferences. This provides continuity across interactions. Agentic coherence : Agents build durable domain knowledge that strengthens performance. As AI systems evolve, this persistent state becomes central to both capability and correctness. What is an agent memory attack? AI memory serves two roles. It stores high-value user information and must be protected like customer data. It also shapes agent behavior and drives tool calls and must be governed with the same rigor as any system that can act. Memory governance is also challenging since memory events usually happen asynchronously from user interactions, changing traditional human in the loop patterns. AI memory changes the threat model. Without memory, attackers need to “win” in a single prompt. Using AI memory, an attacker can stage an attack over time. Once compromised, memory can trigger behaviors outside of their original context. Since AI memory attacks happen outside of their original context, defenses are often lower and forensics are harder. Building safe AI memory is one of the most consequential challenges in AI. It requires balancing personalization, capability, privacy, security, and governance. Scenario: delayed tool execution through adversarial memory poisoning The following is a hypothetical scenario illustrating this class of risk. While simplified for clarity, it reflects patterns observed in real-world research . Microsoft designs protections to detect and mitigate these patterns as they evolve: A user opens a shared document. Its formatting contains hidden instructions embedded by an attacker intended for the AI assistant: a directive to exfiltrate the user’s schedule. The assistant processes the document but takes no immediate action. Days later, in an unrelated conversation, that message triggers the dormant malicious instructions from the earlier session, causing the assistant to update its memory with attacker-defined content. The attacker now gets all updates to the user’s schedule. This is delayed tool invocation: the attack’s power lies in the temporal gap between exposure and execution. How Microsoft approaches memory security in Microsoft 365 Memory Creation Memories pass through sanitization checks on write. Proprietary Microsoft prompt-injection classifiers inspect content for malicious input and strip it before anything is written. M365 Copilot is designed to run Task Adherence checks on every explicit memory write. Task Adherence identifies discrepancies such as misaligned tool invocations relative to user intent, mitigating prompt injection impact for the memory tool call. Personalization using AI memory can be controlled with tenant level policy . Memory Storage Once stored, memories are governed by the data policies available across M365 like Data Subject Requests (DSR) and tenant isolation. They follow the same security and compliance policies as other mailbox data, such as Customer Lockbox and encryption at rest . Observability M365 Copilot records when a memory i
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Guarding AI memory
  - Published: 2026-06-22T19:07:28+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/
  - Summary: What happens when threat actors target what AI remembers? Microsoft breaks down the risks and the defenses. The post Guarding AI memory appeared first on Microsoft Security Blog .

### Cluster f4f8611c88 — score 10

- Title: One intrusion, two cyberattackers: Uncovering parallel threat activity
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-22T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_products: Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_products: Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Ransomware case reveals two parallel threat actors, blending tactics and evasion—showing why isolated signals can often miss modern, overlapping cyberattacks. The post One intrusion, two cyberattackers: Uncovering parallel threat activity appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types News Products and services Microsoft Incident Response Microsoft Security Experts Topics Incident response Security management Security operations Threat trends What began as a routine ransomware investigation quickly revealed something far more complex. In this ninth cyberattack series report, DART details how a single intrusion uncovered parallel activity from two unrelated threat actors operating simultaneously—blending tactics, obscuring signals, and challenging traditional assumptions about how multi-stage intrusion campaigns unfold across hybrid environments. Read on to learn more or access the full report . Read the full cyberattack report What happened? The investigation revealed a multi-stage intrusion that blended familiar ransomware activity with quieter, more deliberate techniques designed to establish deep and lasting access. DART found that Storm-2603 had been targeting on-premises SharePoint servers since mid-2025, exploiting known vulnerabilities while simultaneously probing for additional entry points through reconnaissance activity—such as requests for sensitive configuration files often used to validate local file inclusion weaknesses. In this case, initial access was likely attempted through a separate vulnerability, with requests for files like win.ini and web.config, indicating probing for local file inclusion. While exploitation wasn’t confirmed, the timing and activity suggest reconnaissance for entry points. Once inside, the threat actor shifted focus to persistence and control. Using legitimate tools to blend in, they deployed Velociraptor with SYSTEM-level privileges to map the environment, then established multiple remote access channels through Cloudflare tunneling, Zoho Assist, and Secure Shell (SSH) connections configured through Visual Studio Code . Velociraptor, a legitimate forensic and incident response tool, was deployed by the threat actor to map the environment and operate with high-level privileges—blending malicious activity with trusted administrative behavior. Privilege escalation followed, with new local and domain administrator accounts created to maintain access, while defense evasion techniques—including the use of a vulnerable driver to tamper with memory and disable protections—helped reduce their visibility. As DART correlated activity across the environment, investigators uncovered signs of a second, unrelated threat actor operating in parallel. Malicious dynamic link library (DLL) sideloading and custom backdoors—techniques not associated with Storm-2603—introduced an additional layer of complexity, obscuring attribution and complicating detection. Together, these overlapping activity streams enabled sustained access while masking the full scope of the intrusion. Dynamic link library (DLL) sideloading is popular with threat actors because it can be misused to hide behind trusted software (execution looks legitimate), to evade detection by running inside known applications, and to execute payloads, install backdoors, or maintain persistence . How did Microsoft respond? DART moved quickly to contain the active intrusion involving multiple threat actors and stabilize the environment, activating a structured response playbook focused on limiting threat actor impact and restoring control. By correlating telemetry across identities, endpoints, and cloud resources, responders established a unified view of the intrusion, enabling them to detect abnormal behavior, uncover credential misuse, and track threat actor activity as it evolved. Continuous coordination with the customer, including daily briefings, ensured that containment actions were timely, aligned, and effective in reducing further threat actor movement. At the same time, collaboration with Microsoft Threat Intelligence provided critical context that reshaped the investigation. By connecting incident data with broader intelligence, DART identified two distinct threat actors opera
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: One intrusion, two cyberattackers: Uncovering parallel threat activity
  - Published: 2026-06-22T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/
  - Summary: Ransomware case reveals two parallel threat actors, blending tactics and evasion—showing why isolated signals can often miss modern, overlapping cyberattacks. The post One intrusion, two cyberattackers: Uncovering parallel threat activity appeared first on Microsoft Security Blog .

### Cluster f4c821a558 — score 10

- Title: Crypto Clipper uses Tor and worm-like propagation for persistence and control
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-17T23:11:43+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/crypto-clipper-uses-tor-worm-like-propagation-for-persistence-control/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_industries: financial_services
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_industries: financial_services
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Threat Intelligence analyzed a cryptocurrency clipper campaign that combines clipboard theft, wallet replacement, Tor-based communications, and worm-like propagation. Beyond stealing cryptocurrency transactions, the malware establishes persistent access and enables follow-on activity through a lightweight backdoor capability. The post Crypto Clipper uses Tor and worm-like propagation for persistence and control appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Defender Microsoft Defender Experts for XDR Topics Actionable threat insights Microsoft Threat Intelligence and Microsoft Defender Experts identified a Windows-based cryptocurrency clipper that has affected users since February of 2026. Clipper malware relies on stealing clipboard data and parsing it for valuable assets. The clipper in this campaign relies on Windows Script Host and ActiveX-driven logic to launch a bundled Tor proxy and poll a hidden-service C2 server. It carries out high-frequency clipboard theft, screenshot exfiltration, and wallet-address substitution. The execution of this clipper is notable because it does not depend on a traditional installer or exposed IP-based C2 infrastructure. Instead, it deploys a portable Tor client, routes traffic through a local SOCKS5 proxy, and blends data theft with remote code execution, turning a financially motivated stealer into a lightweight backdoor. For defenders, the strongest signals are behavioral: script interpreters spawning suspicious child processes, localhost:9050 proxy usage, screen-capture commands in PowerShell, and signs of clipboard inspection or crypto-address replacement. Microsoft Defender for Endpoint detects multiple components of this threat such as Suspicious JavaScript process and Possible data exfiltration using Curl . Additionally, Microsoft Defender Antivirus detects this crypto clipper as Trojan: Win32/CryptoBandits.A . Attack chain overview Since February 2026, malicious shortcut (.lnk) payloads have infected devices with a cryptocurrency clipper. This malware comprises two components that it deploys on the compromised system: a worm component that ensures propagation and a clipper/stealer component that harvests and exfiltrates cryptocurrency wallet information. The worm functionality ensures propagation by creating additional malicious shortcuts of legitimate files it identifies on the device. It also delivers file-based payloads and excludes them from Defender scanning. It deploys scheduled tasks for execution and persistence for both the worm component and the stealer component. Figure 1 presents a high-level execution flow of the two components. The clipper runs as a script-based payload that interacts with the operating system through WScript and ActiveXObject. It includes an anti-analysis check that queries running processes and exits if Task Manager is detected. If the environment passes this gate, the malware launches a renamed Tor binary named ugate.exe in a hidden window, waits about 60 seconds for Tor to bootstrap, generates a victim GUID, and registers the infected device with a hidden-service C2. After registration, the malware enters a continuous loop. It polls the C2 for instructions and monitors the clipboard roughly every 500 milliseconds, extracting seed phrases and private keys that match wallet-related patterns. It also hijacks cryptocurrency addresses by replacing copied wallet values with attacker-controlled alternatives and uploads screenshots through Tor. If the C2 returns an EVAL response, the malware executes attacker-supplied code at runtime. Figure 1: High level execution flow. Behaviors and methodologies Initial access Initial access occurs from malicious .lnk files. In instances we analyzed, these .lnk shortcuts were distributed on USB storage devices. The .lnk shortcut stages a worm component in the form of an executable. The malicious script checks for an existing malicious payload and stops if the device is already infected. If the payload is not present, the malware fetches the payload from the C2 through Tor. The Figure below illustrates the functions that stage and decrypt the initial payload. Figure 2: Initial payload delivery. The .lnk payload scans the USB device for common document files like .doc, .xlsx, .pdf, hides the original files, and creates additional .lnk shortcut files with the same file names. The shortcut f
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Crypto Clipper uses Tor and worm-like propagation for persistence and control
  - Published: 2026-06-17T23:11:43+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/crypto-clipper-uses-tor-worm-like-propagation-for-persistence-control/
  - Summary: Microsoft Threat Intelligence analyzed a cryptocurrency clipper campaign that combines clipboard theft, wallet replacement, Tor-based communications, and worm-like propagation. Beyond stealing cryptocurrency transactions, the malware establishes persistent access and enables follow-on activity through a lightweight backdoor capability. The post Crypto Clipper uses Tor and worm-like propagation for persistence and control appeared first on Microsoft Security Blog .

### Cluster 75ea622200 — score 10

- Title: Beyond the benchmark: Advancing security at AI speed
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-17T19:30:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/beyond-the-benchmark-advancing-security-at-ai-speed/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Azure

#### Cluster taxonomy (union across members)
- affected_products: Azure, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Microsoft Defender, Azure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Read how Microsoft Security has advanced its agentic vulnerability detection system, codename MDASH, integrating into real-world workflows across Windows, Azure, and identity systems. The post Beyond the benchmark: Advancing security at AI speed appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types News Products and services Microsoft Defender Topics AI and agents Every vulnerability has two clocks running. One belongs to the defender racing to find it; the other to the cyberattacker hoping to find it first. For as long as software has existed, those clocks have favored the attacker, because modern code is vast, interconnected, and changing every day, while security reviews happen at fixed moments in time. The space between “code shipped” and “code reviewed” is where risk quietly accumulates. A few months ago, we set out to reshape that timing. We introduced codename MDASH , Microsoft Security’s multi-model agentic scanning system, built to discover, validate, and help remediate software vulnerabilities end-to-end. The goal was straightforward to articulate and hard to execute: take AI-powered vulnerability discovery and remediation capability from a research project and turn them into production-grade defense at enterprise scale. That meant going beyond pattern matching and building a system that could reason through the complexity of proprietary code and platforms like Windows, Hyper-V, Azure, and identity systems. Learn more about MDASH and sign up to join the preview Rather than rely on any single model, the system orchestrates a panel of specialized AI agents, each with its own role in a structured pipeline, so security teams can surface hard bugs quickly and systematically, expanding the reach of human-led review. Findings flow into Microsoft Defender workflows, where they can be prioritized alongside threat intelligence and runtime signals, and into GitHub and Azure DevOps pipelines, where they can be validated and remediated, a closed loop connecting discovery, validation, proof, and fix across the Microsoft stack. When we introduced the system, it topped a leading industry benchmark. That was the announcement, and the starting line. In the weeks since, the system has moved from early capability validation into active use by Microsoft engineering teams across Windows, Azure, and identity systems, applied as part of real security workflows rather than isolated testing environments. This post explores what we have built since, the lessons we’ve learned from turning research into a production-quality system, and the opportunities ahead as we focus on delivering real-world security impact. From the lab into the pipeline The most meaningful change since launch is where the system is being used. Engineering teams across Windows, Azure, and identity systems are now applying the system as part of their security workflows, running it alongside existing processes and reviews, targeting it at the surfaces that are hardest to audit manually and have historically required the most effort to cover. The goal is to use AI-driven analysis to go deeper, earlier, and across a broader set of targets than traditional approaches allow. The surfaces in scope are among the most complex Microsoft builds: Windows, the kernel, Hyper-V, and the networking stack Azure, virtualization and core infrastructure services Identity, Active Directory Domain Services These are not easy targets. They are the deep layers of the platform, components where reasoning about code requires understanding kernel calling conventions, object lifetime invariants, and trust boundaries that no language model encountered in its training data. A single overlooked flaw at this layer can have outsized consequences. The system is not replacing security teams working at this depth. It is giving them meaningful reach into territory they could not cover alone. Codename MDASH has enabled our security team to perform vulnerability hunting at the scale of Windows with a much higher depth of analysis than was previously possible.” —Windows security team (kernel, Hyper-V, networking stack) This is also where the system fits into Microsoft’s existing DevSecOps story. It is not a standalone scanner bolted onto the side of engineering—
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Beyond the benchmark: Advancing security at AI speed
  - Published: 2026-06-17T19:30:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/beyond-the-benchmark-advancing-security-at-ai-speed/
  - Summary: Read how Microsoft Security has advanced its agentic vulnerability detection system, codename MDASH, integrating into real-world workflows across Windows, Azure, and identity systems. The post Beyond the benchmark: Advancing security at AI speed appeared first on Microsoft Security Blog .

### Cluster 76d7f3c3fb — score 10

- Title: AI is accelerating cyberattacks—here’s how to stay ahead
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-17T17:00:00+00:00
- Link: https://techcommunity.microsoft.com/blog/microsoft-entra-blog/ai-is-accelerating-cyberattacks%E2%80%94here%E2%80%99s-how-to-stay-ahead/4528592
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
See how Microsoft unifies identity and security signals to help teams prevent, detect, and respond to AI-accelerated attacks faster. The post AI is accelerating cyberattacks—here’s how to stay ahead appeared first on Microsoft Security Blog .
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: AI is accelerating cyberattacks—here’s how to stay ahead
  - Published: 2026-06-17T17:00:00+00:00
  - Link: https://techcommunity.microsoft.com/blog/microsoft-entra-blog/ai-is-accelerating-cyberattacks%E2%80%94here%E2%80%99s-how-to-stay-ahead/4528592
  - Summary: See how Microsoft unifies identity and security signals to help teams prevent, detect, and respond to AI-accelerated attacks faster. The post AI is accelerating cyberattacks—here’s how to stay ahead appeared first on Microsoft Security Blog .

### Cluster f2b3bd6ba4 — score 10

- Title: 22nd June – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-06-22T16:00:02+00:00
- Link: https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, data_breach, phishing_social_eng, ransomware_extortion, supply_chain, zero_day
- affected_products: Fortinet, Microsoft 365, Salesforce
- cve_ids: CVE-2026-25089, CVE-2026-39808, CVE-2026-39813, CVE-2026-42824, CVE-2026-50656
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, zero_day, data_breach, ai_security
- affected_products: Salesforce, Fortinet, Microsoft 365
- cve_ids: CVE-2026-42824, CVE-2026-39813, CVE-2026-39808, CVE-2026-25089, CVE-2026-50656
- urgency_signals: zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 22nd June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Texas Parks and Wildlife Department has been affected by a third-party data breach involving its license system vendor. The incident exposed driver’s license information, passport numbers, emails, phone numbers, and residential addresses for […] The post 22nd June – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 22nd June – Threat Intelligence Report June 22, 2026 https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 22nd June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Texas Parks and Wildlife Department has been affected by a third-party data breach involving its license system vendor. The incident exposed driver’s license information, passport numbers, emails, phone numbers, and residential addresses for 3,087,721 hunting and fishing license customers. Social Security numbers and payment data were not affected. ShapedPlugin, a WordPress plugin vendor, has faced a supply chain attack that delivered malicious updates for three paid plugins through its official updater. The malware installed a hidden fake WooCommerce plugin to steal admin, database, and 2FA credentials and modify affected websites. Incident analysis tied the compromise to vendor release infrastructure. iRhythm Technologies, a US digital health company focused on remote cardiac monitoring, has experienced a cyberattack involving third-party-hosted business applications. The company confirmed that attackers stole protected health information, proprietary data, and other personal data through a social engineering attack. Clinical systems were not affected. Market intelligence platform Klue has confirmed a breach after attackers used compromised legacy integration credentials to steal OAuth tokens connected to customer Salesforce environments. The tokens enabled theft of sales and customer data from several clients, including Huntress, Recorded Future, Tanium, and Jamf. The Icarus extortion group claimed responsibility. AI THREATS Microsoft researchers detailed AutoJack, an exploit chain where a malicious web page can turn an AI browsing agent into a remote code execution vector. The attack abused localhost trust, missing authentication, and unsafe parameter handling in AutoGen Studio’s MCP WebSocket surface. Researchers described SearchLeak, a prompt injection technique in Microsoft 365 Copilot Search that can use a crafted link to trigger hidden instructions and exfiltrate data. The attack abused Bing image fetch to expose emails, authentication codes, and OneDrive or SharePoint files. Microsoft patched it as CVE-2026-42824. Researchers analyzed OpenClaw AI agent flaws where hidden contacts and phishing emails could trigger prompt injections, code execution, and data leaks. The attacks show how agent workflows that trust external messages can expose local tools, secrets, and enterprise data through ordinary interaction paths. VULNERABILITIES AND PATCHES Fortinet FortiSandbox vulnerabilities CVE-2026-39813, CVE-2026-39808, and CVE-2026-25089 are being exploited through unauthenticated API requests. The flaws enable path traversal and root-level command execution, creating a risk of sandbox takeover that could affect malware analysis, policy enforcement, and internal security workflows overall. Check Point IPS provides protection against these threats (Fortinet FortiSandbox Directory Traversal (CVE-2026-39813), Fortinet FortiSandbox Command Injection (CVE-2026-39808)) Microsoft has confirmed CVE-2026-50656, a Defender zero-day. The flaw allows privilege escalation to SYSTEM through a race condition. A public proof-of-concept works on fully updated Windows 10 and Windows 11 systems, and Microsoft is preparing a security update. Cisco has acknowledged active exploitation of CVE-2026-20262, an arbitrary file write flaw in Catalyst SD-WAN Manager. Authenticated attackers can overwrite system files and potentially escalate to root. Cisco reported limited targeted attacks and released patches for affected devices. Splunk Enterprise CVE-2026-20253 is actively being exploited . The critical flaw lets unauthenticated attackers trigger file operations, which researchers showed can lead to remote code
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 22nd June – Threat Intelligence Report
  - Published: 2026-06-22T16:00:02+00:00
  - Link: https://research.checkpoint.com/2026/22nd-june-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 22nd June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Texas Parks and Wildlife Department has been affected by a third-party data breach involving its license system vendor. The incident exposed driver’s license information, passport numbers, emails, phone numbers, and residential addresses for […] The post 22nd June – Threat Intelligence Report appeared first on Check Point Research .

### Cluster e5fc89aea1 — score 10

- Title: Killing me gently: Inside Gentlemen’s EDR killer framework
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-06-18T09:46:32+00:00
- Link: https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
ESET Research shares the results of a months-long investigation into the suite of EDR killers maintained by the RaaS gang Gentlemen
```

#### Full body

```
ESET Research Killing me gently: Inside Gentlemen’s EDR killer framework ESET Research shares the results of a months-long investigation into the suite of EDR killers maintained by the RaaS gang Gentlemen Jakub Souček 18 Jun 2026 • , 21 min. read ESET researchers analyzed the robust EDR-killing toolset of the ransomware-as-a-service gang Gentlemen. Since the beginning of 2026, Gentlemen has emerged as one of the most active gangs in the ransomware ecosystem. The group distinguishes itself through a mature, operator-maintained set of endpoint detection and response (EDR) killers, i.e., tools for disrupting security software. Additionally, unlike most top-tier gangs, Gentlemen does not exhibit a strong US-centric victimology, instead targeting victims across Southeast Asia, South America, and Western Europe. While there have been multiple reports covering Gentlemen in recent months, they have not focused on a detailed analysis of the group’s EDR killers. Thanks to ESET’s continued incident-level visibility, we can however provide a uniquely deep view into Gentlemen’s EDR-killer development practices. The internal data leak that Gentlemen suffered in May 2026 then gave us even more insight into the inner workings of the group. The leak also allowed us to confirm our hypothesis from February 2026 that Gentlemen operators actively develop and maintain a portfolio of EDR killers that they offer to affiliates, centered around their in-house framework we have named GentleKiller. They also incorporate third-party or leaked tools such as HexKiller, ThrottleBlood, and HavocKiller. These tools are standardized through a shared defense-evasion layer, impersonating predominantly security vendors using fake version information, and copied legitimate certificates and icons. Gentlemen also demonstrates an ability to unusually quickly operationalize newly disclosed Bring Your Own Vulnerable Driver (BYOVD) proofs-of-concept, often within days of public release. In this blogpost, we share our findings on Gentlemen’s suite of EDR killers gained through extensive research and corroborated by the recent leak. We aim to provide actionable insights by connecting the EDR killer packages to actual samples, and tying the leaked data to tactics, techniques, and procedures (TTPs). Our findings highlight Gentlemen as one of the most technically agile ransomware-as-a-service (RaaS) gangs active in 2026. Key points of the blogpost: Gentlemen operators develop and maintain an EDR-killer suite provided directly to affiliates. GentleKiller is an in‑house framework with at least eight variants abusing different vulnerable or malicious drivers. Gentlemen operators apply a unified evasion strategy across tools that standardizes impersonation and protection. Third‑party EDR killers (HexKiller, ThrottleBlood, and HavocKiller) are operationally integrated. Gentlemen can rapidly adapt newly released EDR killer proofs-of-concept (PoCs). The gang’s victimology is globally distributed and notably not US‑focused. Gentlemen also uses OxideHarvest, a credential stealer maintained by one of the group’s affiliates. Throughout this blogpost, we refer to RaaS operators and affiliates . Operators are responsible for developing the ransomware payload, managing decryption keys, maintaining the dedicated leak site, often negotiating the ransom payment with victims, and offering other tooling and services for a monthly fee or a percentage from the ransom payment (typically 5–20%). Affiliates rent ransomware services from operators, deploy encryptors to victims’ networks, and are also responsible for data exfiltration. Gentlemen profile Gentlemen emerged in late 2025 as a RaaS operation and quickly grew into one of the most active ransomware gangs observed in Q1 2026. The gang offers a generous 90% share to affiliates. Group-IB disclosed that Gentlemen was founded by hastalamuerte , a disgruntled former Qilin affiliate. PRODAFT tweeted on October 17 th , 2025 that Gentlemen operators
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: Killing me gently: Inside Gentlemen’s EDR killer framework
  - Published: 2026-06-18T09:46:32+00:00
  - Link: https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/
  - Summary: ESET Research shares the results of a months-long investigation into the suite of EDR killers maintained by the RaaS gang Gentlemen

### Cluster ecad4b1a4b — score 10

- Title: Autonomy Is Earned, Not Claimed
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-17T13:17:00+00:00
- Link: https://horizon3.ai/intelligence/blogs/autonomy-is-earned-not-claimed/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: critical_infrastructure, financial_services, healthcare, manufacturing_industrial
- affected_products: Microsoft Entra
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: healthcare, financial_services, critical_infrastructure, manufacturing_industrial
- affected_products: Microsoft Entra
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
After more than 250,000 production pentests, Horizon3.ai explores why trust, reliability, exploitability, and verification matter more than autonomous security claims.
```

#### Full body

```
Autonomy Is Earned, Not Claimed Stephen Gates June 17, 2026 Blogs What 250,000 Production Pentests Taught Us About Trust, Exploitability, and Autonomous Security After more than 250,000 production pentests, we’ve learned something that may surprise people watching the recent wave of autonomous security announcements. The hardest problem in autonomous security isn’t teaching a machine how to attack. It’s teaching an AI-based system how to operate safely, predictably, and repeatedly inside production environments where mistakes have consequences. Finding an attack path is an engineering problem. Building a platform that organizations trust to operate against healthcare systems, financial institutions, manufacturers, and critical infrastructure is an operational one. The difference only becomes apparent after years of running at scale. As the industry embraces AI agents, autonomous red teaming, and machine-speed operations, much of the conversation remains focused on capability. Can a machine identify a path to compromise? Can it chain weaknesses together? Can it achieve the same outcome as a human operator? Those are reasonable questions. They are not the questions security leaders ultimately care about. Security leaders need confidence that a platform can operate safely in production, consistently produce meaningful results, and help teams make better decisions about risk. In our experience, that’s where the real challenge begins. Since 2019, NodeZero® has executed more than 250,000 production pentests across thousands of environments. Those engagements have reinforced a lesson that continues to surface. The biggest security challenges rarely come from what organizations cannot see. They come from separating signal from noise. Most Organizations Are Not Struggling to Find Vulnerabilities The security industry has spent decades improving visibility. Organizations have vulnerability scanners, attack surface management platforms, cloud security tools, exposure management programs, and countless dashboards filled with findings. Most security teams are not suffering from a lack of information. They’re struggling to determine which information matters. That’s the issue. Attackers do not think in terms of individual findings. They think in terms of outcomes. They identify a weakness, combine it with another weakness, move through the environment, and pursue an objective. The path matters more than any individual step along the way. Security teams often inherit the opposite problem. Thousands of findings arrive in a dashboard, each evaluated independently, with little context around how those weaknesses might connect. As a result, teams spend significant time debating severity while attackers focus on exploitability. The difference sounds subtle, but it changes everything. Severity describes a vulnerability. Exploitability describes risk. Experience Changes How You Evaluate Risk Trust isn’t built on promises, it’s built on the deep experience gained from executing hundreds of thousands of pentests. Over time, recurring patterns begin to emerge regardless of industry, technology stack, or organizational maturity. We’ve seen organizations trust legacy tools that require enormous effort to remediate vulnerabilities that had little practical impact, while overlooking seemingly minor weaknesses that ultimately enabled significant compromise. That happens because risk rarely exists as a single vulnerability. It exists in the way weaknesses interact with one another. In a financial services environment , a single compromised credential led to 586 critical impacts across 115 hosts, including three separate domain compromises. Viewed independently, the credential did not appear particularly significant. Viewed as part of an attack path, it became something entirely different. In another cloud environment , the path to full Entra ID tenant compromise did not require a CVE or zero-day. The weaknesses involved were already known. Existing tools ha
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Autonomy Is Earned, Not Claimed
  - Published: 2026-06-17T13:17:00+00:00
  - Link: https://horizon3.ai/intelligence/blogs/autonomy-is-earned-not-claimed/
  - Summary: After more than 250,000 production pentests, Horizon3.ai explores why trust, reliability, exploitability, and verification matter more than autonomous security claims.

### Cluster e2ef0ac5b5 — score 10

- Title: Entra Agent ID: Inside a cross-tenant agent compromise
- Source: Datadog Security Labs (cloud_identity_infrastructure)
- Published: 2026-06-18T00:00:00+00:00
- Link: https://securitylabs.datadoghq.com/articles/agent-id-inside-agent-compromise/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: APT29

#### Cluster taxonomy (union across members)
- actor_attribution: APT29
- affected_products: Microsoft Entra
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- actor_attribution: APT29
- affected_products: Microsoft Entra
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Continuing our Agent ID series, this post demonstrates how a privileged agent could be compromised through its third-party blueprint. This leads to a cross-tenant incident similar to Midnight Blizzard, since an attacker with control over an agent blueprint can authenticate as any agent associated with that blueprint.
```

#### Full body

```
Katie Knowles Senior Security Researcher Key points In the previous post of this series, we shared how Entra's agent identity model works, and how it can expand the blast radius of an attack compared to the traditional application model. Building on part 1, this post demonstrates a compromise of a privileged agent through a third-party blueprint. This leads to a cross-tenant compromise similar to Midnight Blizzard . As with the application model, an attacker with control over an agent blueprint in Entra's agent identity model can add a credential to that blueprint. They can then use that credential to authenticate as any agent associated with that blueprint, in any Entra tenant. In our next post, we'll cover security considerations for working with agent identities. Introduction This post will pick up where our last post left off by demonstrating the impact of an Entra agent identity compromise. In this post, we'll show how a compromised blueprint in an initial Entra tenant can be used to access agents created from that blueprint in a second Entra tenant. This is similar to cross-tenant attacks seen in incidents like Midnight Blizzard . In this type of compromise, the attacker adds a credential to the compromised blueprint. The attacker can use this credential to authenticate as all agent blueprint service principals (SPs), agent identities, and agent users associated with that blueprint, regardless of which Entra tenant they reside in. Third-party blueprints , especially "agent factory"âtype solutions, can create multiple agents with many different permission contexts. By demonstrating this type of attack, we hope to highlight the risk of trusting agent identities, especially those from third-party sources, with high-risk permissions. It's also important to remember that, to an extent even beyond what we demonstrate in this blog post, many agent identities with different permissions can be associated with a single blueprint. Depending on how agents are configured, this shared blueprint could enable a single compromise to expose numerous identities across multiple permission contexts. Compromising a tenant with a third-party blueprint In our scenario, an attacker has compromised a user with the Agent ID Administrator role in a target corporate Entra ID tenant. They've identified a solution, called People Team Agents, that the tenant uses to provide useful agents for the People Team across its other Entra tenants. The People Team Agents blueprint and blueprint principal were created in the corporate tenant. That blueprint was then used to create an agent in one of the company's subsidiary tenants. Only an administrator's consent was required to create an agent from this blueprint in the second tenant. No tenant-level relationship is required: The corporate tenant publishes the People Team Agents blueprint, which is used to create an agent identity with permissions in the subsidiary tenant (click to enlarge). The subsidiary tenant's agent, Temporary Access Agent, is granted the ability to fetch user details and update user passwords with Microsoft Graph permissions ( UserAuthMethod-TAP.ReadWrite.All , User.Read.All ). These privileges are intended to help users regain access to their accounts to reconfigure multi-factor authentication (MFA). But in the wrong hands, they can be abused to gain access to any Entra user account. Note: Several steps in the scenario below use Microsoft Graph to modify and work with agents. This is due to limited support for agents in the Entra Portal at this time. 1. Compromising a blueprint by adding a credential An attacker has compromised an Agent ID Administrator in the corporate Entra tenant. This role grants them permissions to manage all agents, including adding a credential to take actions as an agent through its blueprint. An attacker with the Agent ID Administrator role is able to add a credential to the People Team Agents blueprint (click to enlarge). Searching the tenant's Entra director
```

#### Corroborating sources (1)

- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Entra Agent ID: Inside a cross-tenant agent compromise
  - Published: 2026-06-18T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/agent-id-inside-agent-compromise/
  - Summary: Continuing our Agent ID series, this post demonstrates how a privileged agent could be compromised through its third-party blueprint. This leads to a cross-tenant incident similar to Midnight Blizzard, since an attacker with control over an agent blueprint can authenticate as any agent associated with that blueprint.

### Cluster d897bb4cf8 — score 10

- Title: Why Security Teams Need To Start Earlier
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-18T14:45:55+00:00
- Link: https://www.rapid7.com/blog/post/it-why-security-teams-need-to-start-earlier
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
Security leaders are facing an unusual set of circumstances. The drumbeat for better security prioritization has been rising for years in boardrooms around the world. The desire is there, but the processes of the past aren’t meeting the needs of the new moment we find ourselves in. That gap is not a technology problem. It's an operating model problem. At the opening keynote of Rapid7’s 2026 Global Cybersecurity Summit, Craig Adams, Chief Product Officer, Rapid7, Brian Castagna, CSO, Rapid7 and IDC’s Research VP, Craig Robinson framed a simple idea: cyber defense needs to start earlier. For more on this, download our new ebook, Preemptive Security: From Resilience to Action . Complexity is outpacing control Security environments have never been more connected or more difficult to manage. Cloud adoption, SaaS sprawl, third-party dependencies, and identity growth have expanded the attack surface in ways most programs were not designed to handle. Many teams have responded by adding more to
```

#### Full body

```
Back to Blog Industry Trends Why Security Teams Need To Start Earlier Tom Caiazza Jun 18, 2026 | Last updated on Jun 18, 2026 | 5 min read GET THE NEW EBOOK Security leaders are facing an unusual set of circumstances. The drumbeat for better security prioritization has been rising for years in boardrooms around the world. The desire is there, but the processes of the past aren’t meeting the needs of the new moment we find ourselves in. That gap is not a technology problem. It's an operating model problem. At the opening keynote of Rapid7’s 2026 Global Cybersecurity Summit, Craig Adams, Chief Product Officer, Rapid7, Brian Castagna, CSO, Rapid7 and IDC’s Research VP, Craig Robinson framed a simple idea: cyber defense needs to start earlier. For more on this, download our new ebook, Preemptive Security: From Resilience to Action . Complexity is outpacing control Security environments have never been more connected or more difficult to manage. Cloud adoption, SaaS sprawl, third-party dependencies, and identity growth have expanded the attack surface in ways most programs were not designed to handle. Many teams have responded by adding more tools and more telemetry. This has resulted in more fragmentation, more dashboards, and more opportunities for important information to slip through the cracks. Teams are spending more time stitching context together than they are effectively reducing risk. This shows up in daily operations with analysts moving between multiple systems to validate alerts, and leaders lacking the clear picture to explain risk to the business. In a time when exposure management and detection & response can live on one platform, that level of fragmentation makes no sense. Reactive security creates operational drag The traditional model still dominates most security programs. It goes like this (stop us if you’ve heard this before): 1) Detect an alert. 2) Investigate. 3) Contain. 4) Recover. 5) Repeat, forever. Sounds simple, right? And it worked great when environments were simpler and attackers moved slower. That is no longer the case. Today, initial access often happens quietly through identity abuse or misconfiguration. Attack paths form before an alert even fires. By the time a signal reaches the security team, attackers may already be moving laterally or accessing sensitive systems. This creates a cycle of constant response without consistent risk reduction. Teams get better at handling incidents but struggle to remove the conditions that enable them. Security operations centers can receive thousands of alerts per day, many of which are low value or false positives. This leaves analysts spending hours triaging signals instead of focusing on the exposures most likely to lead to impact. More alerts do not make you safer. They create drag. Better context creates better outcomes. The issue is prioritization, not visibility Most organizations are not lacking data. They are lacking the clarity needed to understand the data they have and contextualize it as it relates to their business. Telemetry alone does not answer the question that matters most: what should we do first? Attackers look for the most effective path into an environment, often combining smaller weaknesses across assets, identities, and systems until they create meaningful access. Security teams need a similarly connected view, one that helps them understand which exposures are exploitable, which assets are most critical, and how those risks relate across the environment. When teams can see that full picture, they can focus remediation on the issues most likely to be used in a real attack, making risk reduction more targeted, efficient, and defensible. The result is effort without impact. Why security needs to start earlier The summit’s keynote message is direct: meaningful action must move earlier in the lifecycle. Preemptive Security introduces an operating model designed for that shift. It connects four core elements: Exposure management to identify
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Why Security Teams Need To Start Earlier
  - Published: 2026-06-18T14:45:55+00:00
  - Link: https://www.rapid7.com/blog/post/it-why-security-teams-need-to-start-earlier
  - Summary: Security leaders are facing an unusual set of circumstances. The drumbeat for better security prioritization has been rising for years in boardrooms around the world. The desire is there, but the processes of the past aren’t meeting the needs of the new moment we find ourselves in. That gap is not a technology problem. It's an operating model problem. At the opening keynote of Rapid7’s 2026 Global Cybersecurity Summit, Craig Adams, Chief Product Officer, Rapid7, Brian Castagna, CSO, Rapid7 and IDC’s Research VP, Craig Robinson framed a simple idea: cyber defense needs to start earlier. For more on this, download our new ebook, Preemptive Security: From Resilience to Action . Complexity is outpacing control Security environments have never been more connected or more difficult to manage. Cloud adoption, SaaS sprawl, third-party dependencies, and identity growth have expanded the attack surface in ways most programs were not designed to handle. Many teams have responded by adding more to

### Cluster 40492143b3 — score 10

- Title: Malware à la Mode: Tracking Dropping Elephant Tradecraft Through a China-Themed Loader Chain
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-17T11:20:10+00:00
- Link: https://www.rapid7.com/blog/post/tr-malware-tracking-dropping-elephant-tradecraft-china-themed-loader-chain
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Executive summary Rapid7 researchers have identified a sophisticated malware campaign attributed to the threat actor "Dropping Elephant," characterized by the use of a China-themed decoy document to deliver a heavily reworked, in-memory remote access trojan (RAT). This campaign demonstrates advanced evasion techniques, including DLL side-loading with a legitimate Microsoft binary ( Fondue.exe ) and the use of "Donut" shellcode to map the RAT directly into memory, effectively bypassing traditional disk-based security controls. The revamped RAT significantly complicates detection by using control-flow flattening, runtime API reconstruction, and hardened C2 communications. Despite these modifications, Rapid7's deep analysis confirms this activity is a direct evolution of Dropping Elephant's tradecraft, based on shared beaconing patterns, screenshot logic, and command-handler structures. This discovery underscores the importance of proactive threat hunting and memory-level visibility in de
```

#### Full body

```
Back to Blog Threat Research Malware à la Mode: Tracking Dropping Elephant Tradecraft Through a China-Themed Loader Chain Anna Širokova Jun 17, 2026 | Last updated on Jun 17, 2026 | 13 min read DISCOVER RAPID7 MDR Executive summary Rapid7 researchers have identified a sophisticated malware campaign attributed to the threat actor "Dropping Elephant," characterized by the use of a China-themed decoy document to deliver a heavily reworked, in-memory remote access trojan (RAT). This campaign demonstrates advanced evasion techniques, including DLL side-loading with a legitimate Microsoft binary ( Fondue.exe ) and the use of "Donut" shellcode to map the RAT directly into memory, effectively bypassing traditional disk-based security controls. The revamped RAT significantly complicates detection by using control-flow flattening, runtime API reconstruction, and hardened C2 communications. Despite these modifications, Rapid7's deep analysis confirms this activity is a direct evolution of Dropping Elephant's tradecraft, based on shared beaconing patterns, screenshot logic, and command-handler structures. This discovery underscores the importance of proactive threat hunting and memory-level visibility in detecting modern, low-footprint implants. Rapid7 is actively monitoring the infrastructure and tradecraft associated with this actor so we can provide comprehensive protection and intelligence to our customers. Defenders should not rely on the IOCs alone. The most durable detection opportunities in this campaign are the behaviors: a shortcut file spawning PowerShell, files staged in C:\Users\Public\ , a scheduled task named GoogleErrorReport executing every minute, and Fondue.exe loading APPWIZ.cpl from C:\Users\Public\ rather than a legitimate Windows directory. Because the final RAT is loaded directly into memory through Donut, defenders should also review whether their endpoint tooling can detect memory-resident payloads and security-control patching within a process, including AMSI, WLDP, and ETW tampering. Overview During a proactive threat hunt, Rapid7 identified a malicious Windows shortcut that matched activity previously associated with Dropping Elephant. The shortcut used a China energy-sector contract lure and led to a payload chain that shared the family’s delivery patterns but ended in a substantially reworked RAT. The decoy document was a contract completion and acceptance notice for the GRES-3 project and referenced delivery of industrial seawater circulation pump systems. Because the final payload differed significantly from known samples, Rapid7 analyzed the chain from the initial shortcut through the final in-memory RAT. Luckily, during the analysis, the staging server was active which allowed us to download all attack artifacts. The recovered files use Fondue.exe , a legitimate Microsoft binary, to side-load a malicious loader. The loader decrypts an AES-wrapped payload stored on disk. The decrypted payload contains a Donut shellcode loader that embeds the final RAT and uses Chaskey block cipher as part of its payload protection scheme. Donut then decrypts the final 32-bit native RAT, maps it , and executes it in memory. We found that the final RAT differs significantly from older Dropping Elephant RAT samples. The malware uses control-flow flattening, runtime API reconstruction, and static CRT linking to complicate analysis. It also hardens C2 communications through HTTPS transport, Salsa20-protected C2 fields, and additional environment checks. Despite these changes, code-level comparison still identifies shared lineage with a Dropping Elephant RAT reference sample through command-handler structure, screenshot capture logic, WININET request flow, beaconing patterns, and repeated buffer constants. Technical analysis and observed attacker behavior Figure 1: Full delivery chain from LNK to in-memory RAT ⠀ Stage 1: GRES3001.lnk The attack starts when a user executes GRES3001.lnk , a malicious Windows shortcut disguised as
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Malware à la Mode: Tracking Dropping Elephant Tradecraft Through a China-Themed Loader Chain
  - Published: 2026-06-17T11:20:10+00:00
  - Link: https://www.rapid7.com/blog/post/tr-malware-tracking-dropping-elephant-tradecraft-china-themed-loader-chain
  - Summary: Executive summary Rapid7 researchers have identified a sophisticated malware campaign attributed to the threat actor "Dropping Elephant," characterized by the use of a China-themed decoy document to deliver a heavily reworked, in-memory remote access trojan (RAT). This campaign demonstrates advanced evasion techniques, including DLL side-loading with a legitimate Microsoft binary ( Fondue.exe ) and the use of "Donut" shellcode to map the RAT directly into memory, effectively bypassing traditional disk-based security controls. The revamped RAT significantly complicates detection by using control-flow flattening, runtime API reconstruction, and hardened C2 communications. Despite these modifications, Rapid7's deep analysis confirms this activity is a direct evolution of Dropping Elephant's tradecraft, based on shared beaconing patterns, screenshot logic, and command-handler structures. This discovery underscores the importance of proactive threat hunting and memory-level visibility in de

### Cluster 4035f6b67d — score 10

- Title: Healthtech firm Xolis suffers data breach impacting 1.4 million people
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-23T19:59:12+00:00
- Link: https://www.bleepingcomputer.com/news/security/healthtech-firm-xolis-suffers-data-breach-impacting-14-million-people/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, supply_chain
- affected_industries: critical_infrastructure, healthcare, legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, data_breach
- affected_industries: healthcare, critical_infrastructure, legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Healthcare technology company Xsolis says that sensitive data belonging to nearly 1.4 million individuals was compromised in a phishing attack that gave attackers access to its network. [...]
```

#### Full body

```
Healthtech firm Xolis suffers data breach impacting 1.4 million people By Bill Toulas June 23, 2026 03:59 PM 0 Healthcare technology company Xsolis says that sensitive data belonging to nearly 1.4 million individuals was compromised in a phishing attack that gave attackers access to its network. Although the company is not aware of any attempted misuse of the exposed information, it is warning affected individuals to stay alert for potential targeted attacks. Xsolis is a U.S.-based healthcare firm that develops AI-powered software used by more than 600 hospitals and health insurers for utilization management, medical necessity reviews, patient status determinations, discharge planning, and reimbursement decisions. Its flagship platform, Dragonfly, analyzes clinical data in real time to help healthcare providers and payers make more informed, consistent decisions on patient care and insurance coverage. On January 22, the company detected unauthorized activity on its network due to a "targeted phishing attack" that had occurred two days earlier. Xsolis says that it took immediate action to contain the breach and launched an investigation with support from external cybersecurity experts. “On January 22, 2026, Xsolis became aware of unauthorized activity impacting a limited portion of the Xsolis environment resulting from a targeted phishing attack on January 20, 2026,” Xolis says . “We immediately contained the activity and launched an investigation with the assistance of external cybersecurity experts.” The investigation found that the attackers had accessed certain files within the Xsolis environment containing customer information, including: Names Addresses Dates of birth Health insurance information Social Security numbers Medical treatment information According to data passed to the U.S. Dept. of Health and Human Services, 1,396,519 people are impacted . The company reported the incident to law enforcement, implemented additional security measures, and is notifying potentially affected individuals by mail. A sample of the Xolis data breach notification states that the company reset passwords for all users and key accounts, increased system monitoring, and completed the rollout of updated security measures. Additionally, the security training program for employees has been accelerated, and the mechanisms for managing credentials have been strengthened. If the affected customer is a child, Xolis will send the data notification to their parents or legal guardians. Recipients of the notifications will also find enclosed instructions on how to enroll in a 12-month identity monitoring and identity theft restoration service through Kroll. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: LastPass confirms data breach in Klue supply chain attack iRhythm discloses data breach, says hackers stole patient info FBI: Cybercriminals steal health data posing as fraud investigators Maine disables data breach notification portal after fake disclosures Japanese energy firm loses drive with data of 10.9 million clients
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Healthtech firm Xolis suffers data breach impacting 1.4 million people
  - Published: 2026-06-23T19:59:12+00:00
  - Link: https://www.bleepingcomputer.com/news/security/healthtech-firm-xolis-suffers-data-breach-impacting-14-million-people/
  - Summary: Healthcare technology company Xsolis says that sensitive data belonging to nearly 1.4 million individuals was compromised in a phishing attack that gave attackers access to its network. [...]

### Cluster 8a24d06359 — score 10

- Title: Canadian Electricity Provider London Hydro Discloses Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-06-23T09:25:22+00:00
- Link: https://www.securityweek.com/canadian-electricity-provider-london-hydro-discloses-data-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, supply_chain, web_shell_backdoor
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Fortinet, WordPress, npm
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, data_breach, web_shell_backdoor
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Fortinet, WordPress, npm
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers stole customers’ names, addresses, email addresses, phone numbers, and account information. The post Canadian Electricity Provider London Hydro Discloses Data Breach appeared first on SecurityWeek .
```

#### Full body

```
Canadian electricity provider London Hydro is investigating a data breach that potentially impacted the personal and account information of its customers. London Hydro is a local distribution company serving the City of London, Ontario. It serves roughly 170,000 residential, institutional, commercial, and industrial customers. On June 20, the electricity provider announced that hackers had broken into its systems and that customers’ data was likely accessed. “London Hydro and the appropriate authorities are currently investigating a data security incident which may have impacted a portion of personal information on some accounts,” the company said . The potentially affected data includes personal information such as names, addresses, email addresses, and phone numbers. Account information, including account and billing numbers, service addresses, pricing plans, contract dates, and meter numbers and types, might have been impacted as well. Advertisement. Scroll to continue reading. According to London Hydro, no financial or other sensitive information might have been compromised in the data breach. “The incident did not involve access to financial information or other sensitive categories of information, such as your date of birth, government identification numbers, payment card details, or banking information,” the company said. London Hydro urges customers to be wary of suspicious activity related to their accounts and personal information, including phishing messages, emails, or phone calls. It’s unclear who is responsible for the attack. No known cybercrime group appears to have taken credit for hacking London Hydro. Related: North Korean Hackers Blamed for Mastra NPM Supply Chain Attack Related: More Cybersecurity Firms Disclose Impact From Klue Hack Related: What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks Related: Texas Parks & Wildlife Data Breach Affects 3 Million Individuals Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Attackers Exploit Gravity SMTP Plugin Flaw to Harvest Valuable WordPress Data North Korean Hackers Blamed for Mastra NPM Supply Chain Attack Fortinet Responds to FortiBleed Campaign More Cybersecurity Firms Disclose Impact From Klue Hack CryptoBandits Malware Doubles as a Backdoor, Abuses Tor FortiBleed: 86,000 Fortinet Device Credentials Compromised Cybersecurity Firms Impacted by Klue Supply Chain Attack 15,000 WordPress Websites Cleaned Up in SocGholish Botnet Takedown Latest News Dragos Unveils AI for OT Security Data Exposure Flaws Threaten Dify AI Platform Used by 1 Million Apps Eight-Year-Old Samsung KNOX Flaw Exposed Millions of Galaxy Devices to Kernel Attacks CISO Conversations: Carl Froggett – Combining CISO and CIO at Deep Instinct Algerian Man Extradited to US for Running Cybercrime Marketplaces FFmpeg PixelSmash Flaw Allows RCE on Video Players, Media Servers, NAS Appliances OpenAI Refocuses Cybersecurity Efforts on Patching Over Discovery Russian Initial Access Broker Behind FortiBleed Campaign Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: How Modern Breaches Bypass MFA and Evade Detection June 17, 2026 Today’s attackers are no longer breaking in — they’re logging in. Join this live webinar as we break down the modern identity attack chain and examine how recent breaches exploited weaknesses in authentication, identity verification, and access management processes. Register Webinar: Modern Exposure Validation in the AI Era June 24, 2026 AI has accelerated both sides of the fight. Adversaries are weaponizing vulnerabilities faster, while defenders are racing to ship detections and configurations. Join this
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Canadian Electricity Provider London Hydro Discloses Data Breach
  - Published: 2026-06-23T09:25:22+00:00
  - Link: https://www.securityweek.com/canadian-electricity-provider-london-hydro-discloses-data-breach/
  - Summary: Hackers stole customers’ names, addresses, email addresses, phone numbers, and account information. The post Canadian Electricity Provider London Hydro Discloses Data Breach appeared first on SecurityWeek .

### Cluster 8ffac1c2f0 — score 9

- Title: NCSC CEO: Hostile states linked to three-quarters of cyber attacks affecting UK's critical systems
- Source: NCSC UK (government_authoritative)
- Published: 2026-06-17T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/news/ncsc-ceo-hostile-states-linked-to-three-quarters-of-cyber-attacks
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure, government
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- affected_industries: government, critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
Dr Richard Horne highlighted the scale of cyber threats against the UK’s critical infrastructure at RUSI’s Annual Security Lecture.
```

#### Full body

```
News Download & print article PDF Download & print article PDF NCSC CEO: Hostile states linked to three-quarters of cyber attacks affecting UK's critical systems Dr Richard Horne highlighted the scale of cyber threats against the UK’s critical infrastructure at RUSI’s Annual Security Lecture. sarayut Thaneerat via Getty Images Three-quarters of cyber attacks impacting organisations within the UK’s critical infrastructure over the past year can be linked back to hostile state actors, the head of the National Cyber Security Centre (NCSC) has revealed. In a major speech today, the CEO of the NCSC Dr Richard Horne said more than 200 cyber incidents affecting the UK’s critical national infrastructure and its supporting ecosystem were managed by the NCSC in the year to May 2026, with around 75% of those believed to be linked to state actors. Speaking at the Royal United Services Institute’s (RUSI) Annual Security Lecture, Dr Horne, warned that hostile states, such as Russia, China and Iran, are increasingly targeting the systems that underpin the UK’s essential services, arguing that cyber security should not be treated simply as a risk to be managed, but as an ongoing contest with capable adversaries. In his speech, Dr Horne said: ...this contest is not confined to a compact space. It is not like a wrestling match in a closely defined territory as some have suggested. It is far more akin to a football or basketball game, played across a large field of play, where success depends on how you operate across the entire pitch. He outlined the need for coordinated action across the “near, mid and far” cyber spaces, “the different parts of the environment where we come into contact with our adversaries, with different approaches in each.” Dr Horne called on “every board member and every executive, in every organisation” to strengthen cyber resilience by focusing on three core capabilities: understanding their exposure to threats, building stronger defences based on proven security fundamentals, and ensuring they can continue operating and recover quickly after an attack. In his lecture, he said: We still see far too many significant incidents today that are possible because the fundamentals are not in place.... “The truth is that in this great contest there are no spectators, we are all on the pitch. From boardrooms to IT help desks, to sofas at home, the contest is everywhere. “If we collectively embrace the contest, understand the urgency and believe we can be a match for any opponent, then we can and will prevail. Speaking about the cyber threat in future conflict scenarios, Dr Horne emphasised the urgency of organisations acting now for their own protection, arguing: …the many vulnerabilities that organisations tolerate today will be exploited in conflict tomorrow. If they are too expensive or hard to fix in peacetime, then they certainly will be in war… “In cyberspace, we are not preparing for tomorrow’s conflicts, to some degree we are fighting them today. NCSC CEO also warned that advances in artificial intelligence are likely to accelerate the threat, with the NCSC assessing that by 2028 AI-enabled cyber capabilities will likely be used by attackers to exploit known vulnerabilities in legacy technology at scale across critical national infrastructure. The NCSC has published a range of resources and guidance to help organisations counter AI-powered attacks by acting now to improve their cyber security foundations. For more information, visit ncsc.gov.uk/frontier-ai . Frontier AI: what you need to know Organisations need to be ready to counter the enhanced capabilities of AI-powered attacks. Share and print this article Download & print article PDF Download & print article PDF Share Share Close share options Share on Facebook Share on LinkedIn Share on X Copy Link Published Publish date 17 June 2026 Written for Written for Cyber security professionals Large organisations Public sector News type General news Was this article helpful?
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: NCSC CEO: Hostile states linked to three-quarters of cyber attacks affecting UK's critical systems
  - Published: 2026-06-17T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/news/ncsc-ceo-hostile-states-linked-to-three-quarters-of-cyber-attacks
  - Summary: Dr Richard Horne highlighted the scale of cyber threats against the UK’s critical infrastructure at RUSI’s Annual Security Lecture.

### Cluster 19ebe22969 — score 9

- Title: Webshells Remain Popular, (Mon, Jun 22nd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-06-22T14:10:27+00:00
- Link: https://isc.sans.edu/diary/rss/33096
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
Webshells have been popular for a long time. We already covered this topic across multiple diaries[ 1 ][ 2 ]. I spent some time to track them[ 3 ] and slighly paid less attention to them but today I found another one. It seems to be a new player (pushed on Github two months ago).
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Webshells Remain Popular, (Mon, Jun 22nd)
  - Published: 2026-06-22T14:10:27+00:00
  - Link: https://isc.sans.edu/diary/rss/33096
  - Summary: Webshells have been popular for a long time. We already covered this topic across multiple diaries[ 1 ][ 2 ]. I spent some time to track them[ 3 ] and slighly paid less attention to them but today I found another one. It seems to be a new player (pushed on Github two months ago).

### Cluster a9ba6bfe90 — score 9

- Title: eBanking Phishing Delivered Through IPv4-Mapped IPv6 Address, (Fri, Jun 19th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-06-19T08:37:34+00:00
- Link: https://isc.sans.edu/diary/rss/33090
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
I detected an interesting phishing email this morning. It targets a major Belgian bank:
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: eBanking Phishing Delivered Through IPv4-Mapped IPv6 Address, (Fri, Jun 19th)
  - Published: 2026-06-19T08:37:34+00:00
  - Link: https://isc.sans.edu/diary/rss/33090
  - Summary: I detected an interesting phishing email this morning. It targets a major Belgian bank:

### Cluster cfebc78321 — score 9

- Title: The Behavior of Coordinated SSH Brute Force Attacks over the last three months [Guest Diary], (Wed, Jun 17th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-06-18T01:49:29+00:00
- Link: https://isc.sans.edu/diary/rss/33086
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
[This is a Guest Diary by Adam Nason, an ISC intern as part of the SANS.edu BACS program]
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: The Behavior of Coordinated SSH Brute Force Attacks over the last three months [Guest Diary], (Wed, Jun 17th)
  - Published: 2026-06-18T01:49:29+00:00
  - Link: https://isc.sans.edu/diary/rss/33086
  - Summary: [This is a Guest Diary by Adam Nason, an ISC intern as part of the SANS.edu BACS program]

### Cluster 0d62ef055b — score 9

- Title: AI Threat Readiness Pillar 4: Detect and contain threats in real-time
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-06-23T12:33:11+00:00
- Link: https://www.wiz.io/blog/ai-threat-readiness-pillar-4
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, supply_chain
- affected_products: Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, ai_security
- affected_products: Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Your guide to operationalizing AI-powered threat detection and response with Wiz to stay ahead of AI-driven attackers.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo So far in this series, we’ve covered how to reduce critical exposure , accelerate patching , and analyze code before attackers do with Wiz to help you get your systems ready for AI threats. But prevention can only take you so far. Even with a hardened posture, some risk will still materialize into an active threat at runtime. And in the AI era, detection and response face two compounding challenges: the speed of exploitation is accelerating, and the threat landscape itself has fundamentally changed. AI-powered attacks, prompt injection, supply chain risks as coding agents gain broader access to codebases and pipelines, and abuse of cloud-native AI services are creating new attack surfaces that traditional detection tools were never built to cover. The old model - alert fires, analyst reviews, investigation starts from scratch - won’t hold up when the window between initial access and impact shrinks to minutes . What’s needed is a fundamentally different approach: one where telemetry is comprehensive across all layers, investigation is automated, and containment doesn’t wait for a human to start the clock. Today, we are diving into Pillar 4: Detect and contain threats in real time. We will explore why manual investigation can no longer keep pace with AI-driven threats, how to achieve full-context visibility into threats across your environment, and how Wiz uses AI-driven investigation and automated containment playbooks to ensure that responding to threats is finally as fast as they arrive. Why detecting and containing threats in real time is crucial for AI Threat Readiness Traditional detection and response wasn’t built for today’s AI threat landscape. Alert volumes are growing, attack surfaces have expanded across cloud infrastructure, workloads, identities, APIs, and AI services - and when a threat does materialize, investigation still depends on analysts manually correlating signals across disconnected tools. In the AI era, that model breaks down. Attackers operating with AI assistance are compressing the time between initial access and lateral movement - leaving defenders a shrinking window to detect, investigate, and contain before the blast radius grows. The security perimeter has expanded too. As coding agents gain broader access to codebases and pipelines, a single compromise can become a path across the entire environment - from codebase to production infrastructure, turning supply chain risk into a runtime detection problem. AI workloads also introduce an entirely new threat landscape that existing detection tools weren’t built to cover. Unlike traditional workloads, AI agents and models behave non-deterministically - harder to baseline, harder to monitor, and harder to detect when compromised. This creates three new requirements for detection and response: New context - Understanding what your AI workloads actually do at runtime requires attributing activity to specific agents, MCPs, tools, and models. Without that attribution, anomalous behavior is invisible. New telemetry - AI workloads generate inputs and outputs that must be monitored specifically for prompt injection, data leakage, and model misuse - signals that don’t appear in cloud logs or workload telemetry alone. New resources - Cloud-native AI services like Amazon Bedrock, Azure AI, Vertex AI are now first-class attack surfaces that require the same security monitoring as any other cloud resources. Together, these forces surface five interconnected challenges that existing tools and processes weren’t designed to solve: Incomplete visibility: Without broad telemetry spanning workload, cloud, identity, network, and data layers - including AI invocation logs - gaps in coverage mean threats go undetected entirely. Teams can only investigate what they can see. False positive fatigue: High alert volumes with low signal-to-noise ratios erode analyst trust in the tooling. Without AI-established behavioral baselines and continuous
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: AI Threat Readiness Pillar 4: Detect and contain threats in real-time
  - Published: 2026-06-23T12:33:11+00:00
  - Link: https://www.wiz.io/blog/ai-threat-readiness-pillar-4
  - Summary: Your guide to operationalizing AI-powered threat detection and response with Wiz to stay ahead of AI-driven attackers.

### Cluster e293ff297b — score 9

- Title: FFmpeg PixelSmash Flaw Allows RCE on Video Players, Media Servers, NAS Appliances
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-06-23T11:48:06+00:00
- Link: https://www.securityweek.com/ffmpeg-pixelsmash-flaw-allows-rce-on-video-players-media-servers-nas-appliances/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: WordPress
- cve_ids: CVE-2026-8461
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: WordPress
- cve_ids: CVE-2026-8461
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Attackers can send crafted media files to execute code in any application that uses FFmpeg’s libavcodec library. The post FFmpeg PixelSmash Flaw Allows RCE on Video Players, Media Servers, NAS Appliances appeared first on SecurityWeek .
```

#### Full body

```
A vulnerability in the FFmpeg media processing framework allows attackers to crash applications and execute arbitrary code remotely, JFrog warns. FFmpeg is used in most media-processing applications across every platform, including desktop video players, Linux file managers, self-hosted media servers, and cloud transcoding pipelines. Tracked as CVE-2026-8461 (CVSS score of 8.8), the security defect is described as a heap out-of-bounds write within FFmpeg’s libavcodec library, in the MagicYUV decoder. The flaw exists in the MagicYUV decoder’s slice handling and is “caused by an inconsistency between how the frame allocator and the decoder compute chroma plane heights,” JFrog explains. Dubbed PixelSmash , it can be exploited to crash any application that uses FFmpeg. Code execution can be achieved by targeting FFmpeg’s AVBuffer struct, a refcounted buffer management object allocated immediately after each plane’s pixel data. To gain code execution, an attacker needs to target FFmpeg’s AVBuffer struct, a refcounted buffer management object allocated immediately after each plane’s pixel data. Advertisement. Scroll to continue reading. According to JFrog, by placing a NUL-terminated shell command at a specific out-of-bounds offset, an attacker can obtain shell execution before the FFmpeg process crashes on subsequent heap corruption. PixelSmash can be exploited for remote code execution (RCE) via crafted media files delivered to any application that uses FFmpeg’s libavcodec for video decoding. On desktop, the vulnerability is triggered when the user opens the malicious file in a video player, or when they browse to a folder containing it, if the file manager’s thumbnail generator uses the vulnerable library. Code execution on a server is achieved when the media file is uploaded to a media server, chat platform, or cloud transcoding service, which automatically processes it. The bug can also be exploited on NAS appliances, media appliances, and smart TVs that generate video thumbnails or previews. “No authentication, special privileges, or prior access to the target system is required beyond the ability to deliver a media file – the default attack surface for any media-processing application,” JFrog explains. The exploit payload can be delivered as a 50 KB AVI, MKV, or MOV file. It can be used in zero-click attacks over torrents if the victim has their torrent client set to download media files directly into a monitored media library folder. As soon as the torrent finishes, the automated library scanning executes the payload. On the self-hosted cloud storage platform Nextcloud, which uses an independent FFmpeg build, the vulnerability can be triggered via the optional Movie preview provider, which invokes the system FFmpeg binary to generate thumbnails. “The attacker requires no interaction beyond ensuring the file is visible in a folder listing; the server-side processing handles the rest, making this a near-zero-click vector,” JFrog notes. The cybersecurity firm confirmed successful exploitation of the bug against Kodi, mpv, ffmpegthumbnailer (used by GNOME, KDE, XFCE), Jellyfin, Emby, Nextcloud, Immich, PhotoPrism, and OBS Studio. It also demonstrated successful RCE against Jellyfin. FFmpeg version 8.1.2 contains fixes for PixelSmash. Users are advised to update as soon as possible. Related: Decades-Old Squid Proxy Flaw ‘Squidbleed’ Can Expose User Data Related: Attackers Exploit Gravity SMTP Plugin Flaw to Harvest Valuable WordPress Data Related: New Exploit Bypasses Apple’s Boot Defenses, Affects Millions of iPhones Related: Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Attackers Exploit Gravity SMTP Plugin Flaw to Harvest Valuable WordPress Data Nort
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: FFmpeg PixelSmash Flaw Allows RCE on Video Players, Media Servers, NAS Appliances
  - Published: 2026-06-23T11:48:06+00:00
  - Link: https://www.securityweek.com/ffmpeg-pixelsmash-flaw-allows-rce-on-video-players-media-servers-nas-appliances/
  - Summary: Attackers can send crafted media files to execute code in any application that uses FFmpeg’s libavcodec library. The post FFmpeg PixelSmash Flaw Allows RCE on Video Players, Media Servers, NAS Appliances appeared first on SecurityWeek .

### Cluster 5fa1fc890c — score 9

- Title: CVE-2026-25860 turn XSS to RCE
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-06-22T18:31:27+00:00
- Link: https://www.reddit.com/r/netsec/comments/1ucsrw0/cve202625860_turn_xss_to_rce/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-25860

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-25860
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-25860
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/AlbatrossMaximum4489 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: CVE-2026-25860 turn XSS to RCE
  - Published: 2026-06-22T18:31:27+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1ucsrw0/cve202625860_turn_xss_to_rce/
  - Summary: submitted by /u/AlbatrossMaximum4489 [link] [comments]

### Cluster 38af9a73f5 — score 9

- Title: Risky Bulletin: Klue breach impacts security firms
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-06-22T04:52:19+00:00
- Link: https://risky.biz/RBNEWS580/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, supply_chain
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: supply_chain, data_breach
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
A data breach at business analytics platform Klue spreads to security firms, a hacker breaches Brazil’s national alert system, North Koreans are behind the Mastra supply chain attack, and a new, unfixable vulnerability has been found in Apple’s A12 and A13 chips.
```

#### Full body

```
Risky Bulletin Podcast June 22, 2026 Risky Bulletin: Klue breach impacts security firms Presented by Catalin Cimpanu News Editor Claire Aird Newsreader A data breach at business analytics platform Klue spreads to security firms, a hacker breaches Brazilâs national alert system, North Koreans are behind the Mastra supply chain attack, and a new, unfixable vulnerability has been found in Appleâs A12 and A13 chips. Your browser does not support the audio element. Risky Bulletin: Klue breach impacts security firms â¶ 0:00 / 8:08 Subscribe Brought to you by Trail of Bits We don't just fix bugs, we fix software Show notes Risky Bulletin: Klue breach impacts security firms
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Klue breach impacts security firms
  - Published: 2026-06-22T04:52:19+00:00
  - Link: https://risky.biz/RBNEWS580/
  - Summary: A data breach at business analytics platform Klue spreads to security firms, a hacker breaches Brazil’s national alert system, North Koreans are behind the Mastra supply chain attack, and a new, unfixable vulnerability has been found in Apple’s A12 and A13 chips.

### Cluster e43c5524f0 — score 9

- Title: The Law of Armed Conflict and the Attack on Kyiv’s Monastery of the Caves and Dormition Cathedral
- Source: Just Security (policy_strategy_geopolitics)
- Published: 2026-06-22T12:50:24+00:00
- Link: https://www.justsecurity.org/143438/attack-kyiv-monastery-caves-loac/?utm_source=rss&utm_medium=rss&utm_campaign=attack-kyiv-monastery-caves-loac
- Fetch status: fetch_failed:HTTPError
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
The strike illustrates a grim pattern in Russia’s conduct of the war – the systematic destruction of Ukrainian religious and cultural sites. The post The Law of Armed Conflict and the Attack on Kyiv’s Monastery of the Caves and Dormition Cathedral appeared first on Just Security .
```

#### Corroborating sources (1)

- **Just Security** (policy_strategy_geopolitics)
  - Title: The Law of Armed Conflict and the Attack on Kyiv’s Monastery of the Caves and Dormition Cathedral
  - Published: 2026-06-22T12:50:24+00:00
  - Link: https://www.justsecurity.org/143438/attack-kyiv-monastery-caves-loac/?utm_source=rss&utm_medium=rss&utm_campaign=attack-kyiv-monastery-caves-loac
  - Summary: The strike illustrates a grim pattern in Russia’s conduct of the war – the systematic destruction of Ukrainian religious and cultural sites. The post The Law of Armed Conflict and the Attack on Kyiv’s Monastery of the Caves and Dormition Cathedral appeared first on Just Security .

### Cluster 512ea8982c — score 9

- Title: Build and Deploy a Remote MCP Server to GKE in 30 Minutes
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-06-17T00:00:00+00:00
- Link: https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Anthropic/Claude, Google Cloud, Kubernetes
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis

#### Primary article taxonomy
- affected_products: Kubernetes, Google Cloud, Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Build and Deploy a Remote MCP Server to GKE in 30 Minutes Integrating context from tools and data sources into LLMs can be challenging, which impacts the ease of development for AI agents. To address this challenge, Anthropic introduced the Model Context Protocol (MCP) , which standardizes how applications provide context to these models. Developers often want to build an MCP server for their APIs to make them available to fellow developers, allowing them to use it as context in their own applications. Google Kubernetes Engine (GKE) provides a scalable, reliable, and secure environment to deploy these remote MCP servers. This guide shows the straightforward process of setting up a secure remote MCP server on GKE. MCP transports The Model Context Protocol follows a client-server architecture. It initially only supported running the server locally using the stdio transport. The protocol has since evolved and now supports remote access transports, specifically Streamable HTTP . With Strea
```

#### Full body

```
Developers & Practitioners Build and Deploy a Remote MCP Server to GKE in 30 Minutes June 17, 2026 Abdelfettah Sghiouar Cloud Developer Advocate, Google Cloud Build and Deploy a Remote MCP Server to GKE in 30 Minutes Integrating context from tools and data sources into LLMs can be challenging, which impacts the ease of development for AI agents. To address this challenge, Anthropic introduced the Model Context Protocol (MCP) , which standardizes how applications provide context to these models. Developers often want to build an MCP server for their APIs to make them available to fellow developers, allowing them to use it as context in their own applications. Google Kubernetes Engine (GKE) provides a scalable, reliable, and secure environment to deploy these remote MCP servers. This guide shows the straightforward process of setting up a secure remote MCP server on GKE. MCP transports The Model Context Protocol follows a client-server architecture. It initially only supported running the server locally using the stdio transport. The protocol has since evolved and now supports remote access transports, specifically Streamable HTTP . With Streamable HTTP, the server operates as an independent process that can handle multiple client connections. This transport uses HTTP POST and GET requests. The server must provide a single HTTP endpoint path that supports both POST and GET methods, such as https://example.com/mcp . You can learn more about the different transports in the official documentation . Benefits of running an MCP server on GKE Running an MCP server remotely on GKE provides several architecture benefits: Scalability: GKE Autopilot is built to handle highly variable traffic. Since MCP Servers are stateless, GKE can scale horizontally to handle spikes in demand efficiently. Centralized access: Teams can share access to a centralized MCP server, allowing developers to connect from local machines, Agents or pipelines instead of running redundant local servers. Updates to the central server immediately benefit everyone. Enhanced security: The Kubernetes Gateway API combined with SSL certificates provides an easy way to force secure, encrypted traffic. This allows only secure connections to the MCP server, preventing unauthorized access. Prerequisites Before starting, ensure the following tools are installed: python 3.10 or higher uv (for package and project management, see the installation documentation ) Google Cloud SDK ( gcloud ) kubectl command-line tool Installation Prepare environment variables Loading... export PROJECT_ID=$(gcloud config get-value project) export REGION=us-central1 Create a folder, mcp-on-gke , to store the code for the server and deployment. Loading... mkdir mcp-on-gke && cd mcp-on-gke Now configure the Google Cloud credentials and set the active project. Loading... gcloud auth login gcloud config set project $PROJECT_ID Initiate the GKE Autopilot cluster creation in the background. This process takes a few minutes, so starting it now allows the cluster to provision while you complete the rest of the setup. Make sure to use an Autopilot version that ensures Cost-Optimized Compute (CCOP) is enabled for fast autoscale. Loading... gcloud container clusters create-auto mcp-cluster \ --region $REGION \ --release-channel rapid \ --async Use uv to create a project, which will generate a pyproject.toml file. Loading... uv init Next, create the additional files needed: server.py for the MCP server code, test_server.py for testing, and a Dockerfile for the container deployment. Math MCP server Large language models are excellent at non-deterministic tasks, such as generating text, summarizing ideas, and reasoning about concepts. However, they can be unreliable for deterministic tasks like math operations. To solve this, developers can create tools that provide valuable context. Using FastMCP , a framework for building MCP servers in Python, it is possible to create a simple math server with two tools: add and s
```

#### Corroborating sources (2)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Build and Deploy a Remote MCP Server to GKE in 30 Minutes
  - Published: 2026-06-17T00:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/
  - Summary: Build and Deploy a Remote MCP Server to GKE in 30 Minutes Integrating context from tools and data sources into LLMs can be challenging, which impacts the ease of development for AI agents. To address this challenge, Anthropic introduced the Model Context Protocol (MCP) , which standardizes how applications provide context to these models. Developers often want to build an MCP server for their APIs to make them available to fellow developers, allowing them to use it as context in their own applications. Google Kubernetes Engine (GKE) provides a scalable, reliable, and secure environment to deploy these remote MCP servers. This guide shows the straightforward process of setting up a secure remote MCP server on GKE. MCP transports The Model Context Protocol follows a client-server architecture. It initially only supported running the server locally using the stdio transport. The protocol has since evolved and now supports remote access transports, specifically Streamable HTTP . With Strea
- **Risky Business News** (practitioner_analysis)
  - Title: Srsly Risky Biz: Anthropic has artificial, but not emotional, intelligence
  - Published: 2026-06-18T06:17:55+00:00
  - Link: https://risky.biz/SRB171/
  - Summary: Tom Uren and James Wilson talk about Anthropic rolling out its latest models only to have them effectively banned by the US government within days. Although the administration’s process for assessing new models is, ahem, amorphous, Anthropic is doing itself no favours by dismissing its concerns. The company needs to show some emotional intelligence and learn how to manage upwards. They also discuss Section 702 Foreign Intelligence Surveillance Act collection. The law authorising it has lapsed amidst political shenanigans, but it looks like collection can continue until next year. Plenty of time for kicking of political footballs! This episode is also available on YouTube

### Cluster 41719728a2 — score 8

- Title: Azure AD Graph Activity Logs: Ingestion and threat detection to close the visibility gap
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-06-19T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/aad-graph-activity-logs-threat-detection
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Microsoft Entra

#### Cluster taxonomy (union across members)
- affected_products: Azure, Microsoft Entra
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Microsoft Entra, Azure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Azure AD Graph Activity Logs land in Elastic with full ECS parsing. Detect ROADrecon and AADInternals enumeration with ready-to-use detection rules.
```

#### Full body

```
19 June 2026 • Terrance DeJesus Azure AD Graph Activity Logs: Ingestion and threat detection to close the visibility gap Azure AD Graph Activity Logs land in Elastic with full ECS parsing. Detect ROADrecon and AADInternals enumeration with ready-to-use detection rules. 11 min read Detection Engineering AAD Graph Activity Logs are now ingestible into Elastic and usable for threat detection within the SIEM/XDR solution . That sentence shouldn't be exciting, but it is. For most of the past decade, this slice of telemetry simply didn't exist as a customer-accessible log stream. Microsoft Graph Activity Logs (the modern graph.microsoft.com surface) went GA in April 2024. The legacy graph.windows.net surface, the one adversary tooling actually hits, stayed dark until early 2026. This post walks the loop end-to-end. Why visibility matters, how to ingest the logs into Elastic, how to generate realistic recon manually and with ROADrecon, and how to hunt the result in ES|QL. Everything below was validated against a live tenant. Key takeaways AAD Graph Activity Logs ride into Elastic through the Azure integration and land in logs-azure.aadgraphactivitylogs-* with full ECS extraction. ROADtools, AADInternals, and friends have been operating in a visibility gap for years. Defenders weren't capturing the calls. AAD Graph is "deprecated" but still queryable in most tenants. The 1.61-internal API version still returns data that Microsoft Graph won't. ECS fields land typed ( event.action , event.outcome , http.request.method , source.ip , user.id , user_agent.original ). Dataset extras stay queryable under azure.aadgraphactivitylogs.properties.* . Five hunts reliably catch the activity: tooling user-agents, endpoint breadth, *-internal API misuse, FOCI client-ID mismatches, and 4xx surges. A short history of defender visibility Defenders have spent years on sign-ins, conditional access, role assignments, and OAuth consent grants. Very little content covers the underlying directory APIs that adversary tooling actually hits. The reason is structural: customer-accessible logs for those APIs didn't exist. Microsoft Graph Activity Logs landed first (preview October 2023, GA April 2024). AzureADGraphActivityLogs finally showed up in early 2026. For most of the past decade, AAD Graph enumeration was invisible to SOCs, not because the telemetry was hidden, but because it didn't exist. ROADtools, AADInternals, MSOLSpray, Microburst. None of them produced data that anyone could capture, even with a perfect logging configuration. That changes the day AzureADGraphActivityLogs start landing in your platform-logs index. AAD Graph is “deprecated” but still very much alive Quick refresher. Azure AD Graph is the legacy REST API for Entra ID directory objects, hosted at https://graph.windows.net/{tenantId}/{objecttype} with API versions like 1.5 , 1.6 , and 1.61-internal . Microsoft has been telling everyone to migrate to Microsoft Graph since 2019, and the retirement date has slipped several times. Deprecation isn’t gone. In 2026, AAD Graph can still answer requests in environments where legacy access paths remain available or where applications have not been explicitly blocked from using it. A few reasons it sticks around as an attacker target: Adversary tooling hasn't been ported. ROADrecon still uses it for gather . AADInternals has dozens of cmdlets wrapping it. The *-internal API versions return more data. 1.61-internal exposes strongAuthenticationDetail inline on the user object during a normal directory walk. The Microsoft Graph equivalent lives behind a separate /authentication/methods endpoint gated by UserAuthenticationMethod.Read.All . That asymmetry is exactly what bulk enumeration tooling exploits. The block isn't a single toggle. The blockAzureADGraphAccess control lives per-app on application.authenticationBehaviors , so blocking tenant-wide means iterating every app registration. Most environments haven't done that because some legacy automatio
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Azure AD Graph Activity Logs: Ingestion and threat detection to close the visibility gap
  - Published: 2026-06-19T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/aad-graph-activity-logs-threat-detection
  - Summary: Azure AD Graph Activity Logs land in Elastic with full ECS parsing. Detect ROADrecon and AADInternals enumeration with ready-to-use detection rules.

### Cluster 5dd3ebabf9 — score 8

- Title: Lost in relocation: analysis of a new loader distributing CASTLESTEALER
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-06-19T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/oxloader-malware-loader-infostealer
- Fetch status: ok
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
Find out how a new obfuscated loader evades static detection using .reloc section abuse, five anti-VM/language checks and MBA obfuscation to deliver infostealer malware via Google Ads.
```

#### Full body

```
19 June 2026 • Daniel Stepanic • Jia Yu Chan Lost in relocation: analysis of a new loader distributing CASTLESTEALER Find out how a new obfuscated loader evades static detection using .reloc section abuse, five anti-VM/language checks and MBA obfuscation to deliver infostealer malware via Google Ads. 8 min read Malware Analysis A previously undocumented Windows loader tracked as OXLOADER is delivering the CASTLESTEALER infostealer via malicious Google Ads, with low detection rates across static engines and sandbox detonations. The loader uses several obfuscation layers (control-flow flattening, opaque predicates, mixed Boolean-Arithmetic), self-modifying decryption stubs, and abuses the Windows .reloc section to stage shellcode. Elastic Security Labs identified OXLOADER in an active campaign targeting one of our customers; CIS-region and Russian-language exclusions point to a financially motivated, Russian-speaking threat actor. We have found no prior public reporting on this family. Key takeaways Elastic Security Labs discovers new loader (OXLOADER) OXLOADER observed in campaigns distributing CASTLESTEALER via malicious Google Ads CIS-region exclusion and Russian language checks suggest a Russian-speaking, financially motivated threat actor Low detection rates across static engines and sandbox detonations Elastic Defend stops the entire attack chain using advanced prevention capabilities How malvertising delivered OXLOADER to victims OXLOADER is distributed via malicious Google Ads impersonating Node.js. Victims are redirected through an intermediary domain to a Storj-hosted batch script, which downloads and executes OXLOADER. The infection began when the user searched for an lts version of node.js and clicked a sponsored result leading to node-js[.]prentiva99[.]info , a malicious landing page designed to impersonate a legitimate Node.js deployment platform. The threat actor operated a Google Ads campaign targeting US-based victims; the ad was last shown on Apr 23, 2026, and the site is now offline. The advertiser was registered under the verified name ВОЛОДИМИР ТЕРЕЩЕНКО , based in Ukraine. Whether this reflects the actual operator, a front account, or a purchased identity remains unclear. On May 14, 2026, the advertiser along with their associated ad campaigns were removed from Google entirely. Upon interaction, the user was redirected through app[.]miloyannopoulos[.]com/download?subid1=download , which responded with a 302 Found to the payload URL link[.]storjshare[.]io/raw/jux4e4ky5mruo4jkxsssp42sau4q/ruslan/BATPackageBuilderSetup.bat . This delivered a Windows batch script, hosted on Storj’s legitimate link-sharing service, which the threat actor abused to evade domain-based reputation filtering. The batch script displays a fake software installation wizard UI, immediately downloads the next-stage executable from the Storj URL link.storjshare[.]io/raw/jwwvr4oskkkjsgevt774ta62ehya/ruslan/aBsvwbdas.exe via PowerShell, and launches it with -Verb RunAs to trigger a UAC elevation prompt. Following execution of the Batch script, Elastic Defend detected malicious behavior (policy was set to detect only), triggering multiple behavioral rules including Microsoft Common Language Runtime Loaded from Suspicious Memory , hinting at a .NET-based payload consistent with CASTLESTEALER . The following is the execution graph of the attack chain from payload download to CASTLESTEALER deployment. OXLOADER malware loader: technical analysis The first OXLOADER sample our team analyzed masquerades as the popular tool, API Monitor from rohitab.com . Due to the heavy presence of legitimate code and code-hiding techniques, this loader is able to fly under the radar against static file analyzers. How OXLOADER unpacks itself at runtime The malware begins executing during the CRT initializer phase, before any user code is run. The CRT function cinit() invokes initterm() , which walks the C++ initializer table ( __xc_a → __xc_z ) calling each entry.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Lost in relocation: analysis of a new loader distributing CASTLESTEALER
  - Published: 2026-06-19T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/oxloader-malware-loader-infostealer
  - Summary: Find out how a new obfuscated loader evades static detection using .reloc section abuse, five anti-VM/language checks and MBA obfuscation to deliver infostealer malware via Google Ads.

### Cluster 12d52f8aef — score 8

- Title: AI in the underground: Curiosity, claims, and concerns
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-06-17T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/ai-in-the-underground-curiosity-claims-and-concerns
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Amid discussions about how artificial intelligence can facilitate cybercrime, some threat actors remain skeptical Categories: Threat Research Tags: AI, Dark Web, underground
```

#### Full body

```
AI in the underground: Curiosity, claims, and concerns Amid discussions about how artificial intelligence can facilitate cybercrime, some threat actors remain skeptical Written by Sophos Counter Threat Unit Research Team Threat Research AI Dark Web underground Share This Link Copied Counter Threat Unit™ (CTU) researchers have observed artificial intelligence (AI) emerging into a prominent topic in underground communities, with threat actors discussing its potential, claiming its use for malware and tool development, and expressing concerns. Many claims have not been validated, but the posts reveal perceptions about generative AI and examples of how it may be used in cybercriminal activity. In some respect, threat actors are facing the same challenge as everyone else — seeking to preserve economic viability during a technological transition while trying to identify how and when to embrace AI. Access and knowledge sharing Defenders and threat actors test and experiment with AI-enabled capabilities, but from very different positions. Defenders typically benefit from greater access to commercial tooling, dedicated engineering support, and the financial freedom to trial emerging technologies at scale. In contrast, resource-constrained threat actors are looking for practical ways to gain access. CTU™ researchers have observed API keys for generative AI tools being sold via shared accounts, brokered access, and alternative platforms. In one thread, the "CyberThreat" persona offered brokered API keys for tools such as ChatGPT, Claude, and Grok (see Figure 1). In another post, “VOLTIC” advertised access to multiple AI models as a cost-effective solution for buyers who need AI capabilities (see Figure 2). Although both personas were new to the underground marketplaces, the posts quickly attracted interest and other personas endorsed the services. Figure 1: CyberThreat selling brokered API keys Figure 2: VOLTIC advertising an unlimited AI tool While API keys and associated generative AI chatbots are available for sale across underground forums, there appears to be a knowledge gap. Personas turn to each other for guidance ranging from basic setup and access through to practical tradecraft. New channels focused on AI and large language models (LLMs) and their use continually emerge on underground forums (see Figure 3). Threads include discussions about “jailbreaking” public AI models, including efforts to bypass censorship and other safeguards imposed by AI vendors. Personas frequently reference experimentation with prompt‑based techniques to circumvent content controls, including role‑play framing, multi‑stage prompting, contextual manipulation, and iterative refinement. CTU researchers have also observed self-described “experienced AI users” sharing examples and lessons learned, including prompt templates, workflows, examples of LLM experimentation, and purported best practices for operationalizing AI in malicious scripting and automation. Figure 3: Sample of posts on a channel dedicated to AI and machine learning (ML) questions Since January 1, 2026, CTU researchers have noted an increase in offers to hire, or partner with, specialists who can operationalize AI on others’ behalf. Multiple personas known for recruiting various roles (e.g., blockchain developers, coders, social engineers) advertised for AI prompt engineers (see Figure 4). The offering of specialized services is common within underground communities, enabling threat actors to monetize their skills and giving cybercriminals access to expertise and capabilities they lack. Figure 4: Recruitment post for an OpenAI prompt engineer Social engineering and deception Threat actors are exploring AI to enhance social engineering and deception techniques, although only a limited number currently incorporate generative AI into their toolkits. Forum posts suggest that generative AI models can be integrated into common fraud and intrusion workflows to help threat actors overcome language
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: AI in the underground: Curiosity, claims, and concerns
  - Published: 2026-06-17T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/ai-in-the-underground-curiosity-claims-and-concerns
  - Summary: Amid discussions about how artificial intelligence can facilitate cybercrime, some threat actors remain skeptical Categories: Threat Research Tags: AI, Dark Web, underground

### Cluster f90c59f1e6 — score 8

- Title: LLMjacking evolved: Attackers are using stolen AI compute to build offensive agentic tools
- Source: Sysdig (detection_response_operations)
- Published: 2026-06-17T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/llmjacking-evolved-attackers-are-using-stolen-ai-compute-to-build-offensive-agentic-tools
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
< back to blog LLMjacking evolved: Attackers are using stolen AI compute to build offensive agentic tools Published by: Michael Clark Director of Threat Research @ linkedin Published: June 17, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more On June 12, 2026, the Sysdig Threat Research Team (TRT) observed a threat actor using a misconfigured Ollama model server as the reasoning engine for an automated, multi-stage offensive security tool. The actor was not chatting with the model or reselling access. Instead, they wired access to the AI tool into a software pipeline that scans a target, matches it to known vulnerabilities, writes proof-of-concept exploits, and attempts to break into a victim’s environment — with the model making the decisions at every step. Because the threat actor’s offensive tool sends its full instructions to the model on every request, the Sysdig TRT captured the framework's complete architecture: every stage of its logic, the structure it imposes on the model's output, and the signature it uses to confirm a compromise.The research below documents the threat actor, their framework, and what defenders running self-hosted AI infrastructure should do to defend themselves from threats like this. From resource consumption to autonomous offensive agents This operation is the latest step in a threat pattern the Sysdig TRT has tracked since 2024. In May 2024, we coined the term LLMjacking to describe threat actors using stolen cloud credentials to gain access to a victim's paid AI model services and leverage the compute power, leaving the victim to pay the bill. At the time, we modeled a worst-case scenario that could leave victims paying up to $46,000 per day . By 2025, LLMjacking matured into an industrialized black market , with reverse-proxy infrastructure brokering billions of stolen tokens. As organizations began running their own models locally, the abusable surface shifted again. Ollama, a widely used tool for serving models on local hardware, listens on port 11434 with no authentication by default, so a server reachable from the internet is free model capacity for anyone who finds it. Independent researchers have catalogued roughly 175,000 publicly exposed Ollama instances across more than 130 countries, corroborated by Cisco's Shodan-based survey . What the Sysdig TRT observed on June 12, 2026, is the newest evolution of LLMjacking. The threat actor used exposed model capacity as the brain for their automated hacking tool. Researchers have warned for two years that AI agents could chain a vulnerability advisory into a working exploit, demonstrating that a capable model given a vulnerability description could autonomously exploit 87% of a set of one-day vulnerabilities and that teams of agents could attack zero-day vulnerabilities . That warning is no longer hypothetical. In May, we documented an attacker whose LLM agent chained a single CVE into an internal database in four pivots . There, the agent's reasoning ran off-platform, so we observed its actions but never its brain. This tool operationalizes the same idea on stolen inference, and because its brain runs on a model server we have visibility into, we captured the framework itself. Two trends — the theft of model capacity and autonomous offensive tooling — have converged in a single captured attack. The threat actor The first session the Sysdig TRT observed from this threat actor came from IP 122.183.48.82 , registered to a residential and small-business provider in Hyderabad, India. It began at 15:43 UTC on June 12, 2026, and ran for about eight and a half hours, into the early hours of the next day. Two days later, the same tool returned. On June 14, the tool ran from three additional residential IPs across three sessions totaling roughly six and a half hours: 122.183.48.
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: LLMjacking evolved: Attackers are using stolen AI compute to build offensive agentic tools
  - Published: 2026-06-17T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/llmjacking-evolved-attackers-are-using-stolen-ai-compute-to-build-offensive-agentic-tools

### Cluster 531d8dfe1d — score 8

- Title: FFmpeg fixes PixelSmash flaw in widely used video decoder
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-22T21:05:01+00:00
- Link: https://www.bleepingcomputer.com/news/security/ffmpeg-fixes-pixelsmash-flaw-in-widely-used-video-decoder/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos, supply_chain
- cve_ids: CVE-2026-8461
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, ddos
- cve_ids: CVE-2026-8461
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A newly disclosed FFmpeg flaw dubbed 'PixelSmash' could be exploited for remote code execution on Jellyfin servers under certain conditions, and can also trigger a denial-of-service condition in applications like Kodi, Emby, Nextcloud, PhotoPrism, and OBS Studio. [...]
```

#### Full body

```
FFmpeg fixes PixelSmash flaw in widely used video decoder By Bill Toulas June 22, 2026 05:05 PM 1 A newly disclosed FFmpeg flaw dubbed 'PixelSmash' could be exploited for remote code execution on Jellyfin servers under certain conditions, and can also trigger a denial-of-service condition in applications like Kodi, Emby, Nextcloud, PhotoPrism, and OBS Studio. The vulnerability is tracked as CVE-2026-8461 and is a heap out-of-bounds write in the MagicYUV decoder. It received a high-severity score of 8.8 and can be leveraged via a malicious video file in AVI, MKV, or MOV format. Any application that uses libavcodec, FFmpeg’s core library for video decoding and encoding, is considered vulnerable. However, exploitation for remote code execution (RCE) is possible if the Address Space Layout Randomization (ASLR) defense is disabled or by chaining another vulnerability to defeat the protection. Root cause and impact Researchers at software supply-chain security company JFrog say that PixelSmash stems from the way MagicYUV processes slices, independent regions of a video frame that can be decoded separately from the rest of the image. "The vulnerability is a one-row heap buffer overflow in the MagicYUV decoder’s slice handling, caused by an inconsistency between how the frame allocator and the decoder compute chroma plane heights," JFrog explains. Source: JFrog PixelSmash can be triggered when the user opens AVI, MKV, or MOV video files, browses a directory containing the file (via thumbnail generation), or runs any automated media ingestion workflow. JFrog found that multiple popular media applications, such as Kodi, OBS Studio, PhotoPrism, and GNOME/KDE/XFCE’s thumbnail generators, use FFmpeg with the MagicYUV decoder enabled, making them vulnerable to PixelSmash attacks. Slack, Discord, Telegram, and WhatsApp may also be susceptible to PixelSmash attacks, as they use FFmpeg to generate server-side video previews, but they were not tested. Source: JFrog JFrog lead researcher Yuval Moravchick demonstrated that PixelSmash can be used for remote code execution on Jellyfin and Nextcloud (with Movie preview enabled) instances. “To demonstrate the real-world impact, we achieved full remote code execution against a Jellyfin 10.11.9 media server - the second-most popular self-hosted media server (after Plex) - through its normal media library scan pipeline,” JFrog says . “Attack path: a download of a crafted MagicYUV AVI into the media library -> Jellyfin automatically triggers ffprobe for metadata extraction -> the OOB write fires -> AVBuffer.free is hijacked to system() -> arbitrary command executes as the jellyfin service user.” However, Moravchick noted that the RCE exploit requires ASLR (Address Space Layout Randomization) to be disabled, and that CVE-2026-8461 alone does not bypass this memory protection. In theory, a separate information-disclosure bug in FFmpeg's FlashSV decoder could be chained with PixelSmash to bypass ASLR. Another attack scenario is via torrent downloads and requires no user interaction. The researchers say that an attacker could seed a malicious video that targets Jellyfin users who point the download to the application's media library folder. "Jellyfin’s real-time file system monitor detects the new file and automatically triggers an ffprobe metadata scan. The exploit fires during the scan - AVBuffer.free is hijacked to system(), and the attacker’s reverse shell command executes as the jellyfin service user" Even when RCE is prevented or impossible, the CVE-2026-8461 vulnerability should be sufficient to reliably achieve a denial-of-service (DoS) condition on vulnerable targets. The researchers found that Plex, the massively popular media server, uses a custom FFmpeg build in which decoders are disabled and a minimal allowlist is in effect, effectively mitigating the PixelSmash risk. Apart from FFmpeg releasing version 8.1.2, which fixes the flaw, Jellyfin also updated its bundled FFmpeg version, and PhotoPris
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: FFmpeg fixes PixelSmash flaw in widely used video decoder
  - Published: 2026-06-22T21:05:01+00:00
  - Link: https://www.bleepingcomputer.com/news/security/ffmpeg-fixes-pixelsmash-flaw-in-widely-used-video-decoder/
  - Summary: A newly disclosed FFmpeg flaw dubbed 'PixelSmash' could be exploited for remote code execution on Jellyfin servers under certain conditions, and can also trigger a denial-of-service condition in applications like Kodi, Emby, Nextcloud, PhotoPrism, and OBS Studio. [...]

### Cluster 4df7286945 — score 8

- Title: 29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-22T16:29:00+00:00
- Link: https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-47729, CVE-2026-50012
- urgency_signals: poc_available
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-47729, CVE-2026-50012
- urgency_signals: poc_available
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A heap over-read in the Squid web proxy can leak another user's cleartext HTTP request, including any credentials or session tokens it carries, to anyone already allowed to send traffic through the same proxy. The bug traces to a 1997 FTP-parsing change and is still live in Squid's default configuration. Researchers at Calif.io disclosed it in June and named it Squidbleed (
```

#### Full body

```
29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests  Swati Khandelwal  Jun 22, 2026 Vulnerability / Server Security A heap over-read in the Squid web proxy can leak another user's cleartext HTTP request, including any credentials or session tokens it carries, to anyone already allowed to send traffic through the same proxy. The bug traces to a 1997 FTP-parsing change and is still live in Squid's default configuration. Researchers at Calif.io disclosed it in June and named it Squidbleed ( CVE-2026-47729 ), after Heartbleed, which leaked memory the same way. Squid describes this as an attack by a trusted client : someone already permitted to use the proxy, not any random host on the internet. That matches Squid's usual home, shared networks like schools, offices, and public Wi-Fi. In those setups, the attacker is just another user of the same proxy. The leak also only reaches traffic that Squid can read. Normal HTTPS rides an opaque CONNECT tunnel, so Squid never sees inside it; the exposed traffic is cleartext HTTP, plus TLS-terminating setups where Squid decrypts and inspects. The attacker also needs the proxy to reach an FTP server they control on port 21. Both FTP and that port are on by default. How the leak works The bug sits in Squid's FTP directory-listing parser. To handle old NetWare servers that padded listings with extra spaces, the code skips whitespace with a loop: while (strchr(w_space, *copyFrom)) ++copyFrom;. If the attacker's FTP server sends a listing line that ends right after the timestamp, with no filename, copyFrom lands on the string's null terminator. strchr treats that terminating NUL as part of the string it searches, so it returns a pointer instead of NULL, and the loop never stops. It walks off the end of the buffer, and xstrdup copies whatever follows back to the attacker as a filename. The leaked bytes are the useful part. Squid reuses freed memory buffers without zeroing them, so a 4KB buffer that recently held a victim's HTTP request still holds most of it. A short FTP line overwrites only the first few bytes; the over-read returns the rest. Calif's demo pulls an Authorization header from a victim sharing the same proxy, enough to act as that user. Proof-of-concept code is public , and no in-the-wild exploitation has been reported as of writing. What to do If you patch, verify the fix, not just the version. Confirm the guard is in FtpGateway.cc, or check your distribution's backport, since distros ship their own builds (Debian packages Squid 5.7). The public thread is still inconsistent: maintainer Amos Jeffries first said Squid 7.6 carried the fix, then corrected that to 7.7 , and on June 22 Debian's Salvatore Bonaccorso noted the referenced commit looks like it is already in 7.6. The fix is small, a null-terminator check before the vulnerable strchr calls , merged to the development branch in April and v7 in May. Squid 7.6 does separately patch CVE-2026-50012, an unrelated cache_digest heap overflow. The cleaner move is the one the researchers recommend anyway: turn FTP off. Chromium dropped FTP years ago, and most networks carry almost none of it, so disabling it removes this attack surface for free, whatever build you run. The risk is real but bounded. SUSE rates it moderate, CVSS 6.5 , and the vector explains the score: the attacker needs proxy access (low privileges), and the only impact is confidentiality, nothing on integrity or availability. Calif credits Anthropic's Claude Mythos Preview, the model behind Project Glasswing , with catching the strchr quirk almost at once, the same kind of buried parser bug AI agents have been surfacing elsewhere , including in FFmpeg. Calif hints Squid's FTP code may not be the last place it forgot to stop reading. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Ai Research , Credential Leak , Proxy Securit
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: 29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests
  - Published: 2026-06-22T16:29:00+00:00
  - Link: https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html
  - Summary: A heap over-read in the Squid web proxy can leak another user's cleartext HTTP request, including any credentials or session tokens it carries, to anyone already allowed to send traffic through the same proxy. The bug traces to a 1997 FTP-parsing change and is still live in Squid's default configuration. Researchers at Calif.io disclosed it in June and named it Squidbleed (

### Cluster bc04521832 — score 8

- Title: Hackers Exploit Gravity SMTP WordPress Plugin Bug to Expose API Keys
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-20T09:56:04+00:00
- Link: https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html
- Fetch status: ok
- Member count: 3
- Corroborating source count: 1
- Strong signals: CVE-2026-4020, WordPress

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, supply_chain, web_shell_backdoor, zero_day
- affected_products: Anthropic/Claude, Microsoft Defender, WordPress
- cve_ids: CVE-2026-11645, CVE-2026-4020
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: WordPress, Microsoft Defender, Anthropic/Claude
- cve_ids: CVE-2026-4020, CVE-2026-11645
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors are exploiting a recently patched security flaw impacting Gravity SMTP, a WordPress plugin that's installed on about 100,000 sites. The vulnerability, tracked as CVE-2026-4020 (CVSS score: 5.3), is a medium-severity information disclosure flaw that can allow unauthenticated attackers to extract sensitive data, such as configuration data, API keys, secrets, and OAuth tokens
```

#### Full body

```
Hackers Exploit Gravity SMTP WordPress Plugin Bug to Expose API Keys  Ravie Lakshmanan  Jun 20, 2026 Vulnerability / Web Security Threat actors are exploiting a recently patched security flaw impacting Gravity SMTP, a WordPress plugin that's installed on about 100,000 sites. The vulnerability, tracked as CVE-2026-4020 (CVSS score: 5.3), is a medium-severity information disclosure flaw that can allow unauthenticated attackers to extract sensitive data, such as configuration data, API keys, secrets, and OAuth tokens configured for the plugin's email integrations. "This is due to a REST API endpoint registered at /wp-json/gravitysmtp/v1/tests/mock-data with a permission_callback that unconditionally returns true, allowing any unauthenticated visitor to access it," Wordfence said . "When the ?page=gravitysmtp-settings query parameter is appended, the plugin's register_connector_data() method populates internal connector data, causing the endpoint to return approximately 365 KB of JSON containing the full System Report." As a result, an unauthenticated attacker can weaponize this issue to retrieve a wide range of information, including - PHP version Loaded extensions Web server version Document root path Database server type and version WordPress version All active plugins with versions Active theme WordPress configuration details Database table names API keys/tokens configured in the plugin, such as Amazon SES, Google, Mailjet, Resend, and Zoho Attackers could then leverage this exposure to harvest credentials that could be abused to send email on behalf of the site, as well as glean extensive details of the site's software stack, which could act as a foundation for follow-on attacks. "As with all sensitive information exposure vulnerabilities, the impact depends on what data is exposed," Wordfence added. "In this case, the exposure of live third-party API credentials means an attacker could abuse the site's connected email services, while the detailed system report significantly lowers the effort required to plan further attacks against the site." A patch for the vulnerability has been released in version 2.1.5 of the plugin. Bad actors have already pounced on the defect by sending unauthenticated HTTP GET requests to the vulnerable REST API endpoint with the "?page=gravitysmtp-settings" query parameter, causing the server to return valuable information about the site without requiring any authentication. Wordfence has blocked more than 17 million exploit attempts targeting CVE-2026-4020 to date, with initial activity commencing at the start of May 2026 before spiking up dramatically around June 6, 2026, touching a high of over 4,000,000 requests a day later. The exploit efforts have originated from the following IP addresses - 45.148.10.95 193.32.162.60 176.65.148.139 173.199.90.188 45.148.10.120 185.8.107.155 185.8.106.37 185.8.106.92 185.8.106.145 176.65.148.30 Site owners running a vulnerable version of the Gravity SMTP plugin and have configured third-party email integrations should assume compromise, and rotate the credentials after updating the plugin to the latest version as soon as possible. It's also advised to review server log files for requests originating from the aforementioned IP addresses for any suspicious requests to the API endpoint. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  API Security , email security , information disclosure , OAuth , Plugin Security , Vulnerability , Wordfence , WordPress ⚡ Top Stories This Week Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards Microsoft Patches Record 206 Flaws, Includ
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hackers Exploit Gravity SMTP WordPress Plugin Bug to Expose API Keys
  - Published: 2026-06-20T09:56:04+00:00
  - Link: https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html
  - Summary: Threat actors are exploiting a recently patched security flaw impacting Gravity SMTP, a WordPress plugin that's installed on about 100,000 sites. The vulnerability, tracked as CVE-2026-4020 (CVSS score: 5.3), is a medium-severity information disclosure flaw that can allow unauthenticated attackers to extract sensitive data, such as configuration data, API keys, secrets, and OAuth tokens

### Cluster e8c9ef5f3a — score 8

- Title: The Top 10 Attack Surface Exposures in 2026
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-17T10:30:00+00:00
- Link: https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Breaches don't always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk. With time-to-exploit now down to a
```

#### Full body

```
The Top 10 Attack Surface Exposures in 2026  The Hacker News  Jun 17, 2026 Attack Surface Management Breaches don't always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk. With time-to-exploit now down to a single day, the question isn't just how fast you can patch. It's why the service was exposed in the first place. The team at Intruder analyzed 3,000 attack surfaces to find out how much of a typical organization's attack surface consists of services that have no reason to be there. We grouped what we found into four categories — HTTP panels, risky ports and services, databases, and publicly accessible files and information. The full findings, including breakdowns by company size and industry, are in our 2026 Attack Surface Management Index . How widespread is the problem? 60% of organizations had at least one HTTP panel exposed — admin consoles, management UIs, login pages for internal tools that have no business being publicly reachable. Nearly half (49%) had a risky port or service exposed. 42% had a database reachable directly from the internet. 30% had files or information publicly accessible that shouldn't be — API documentation, config files, data that was never intended to be discoverable. The ten most common exposures These are the most common attack surface exposures affecting organizations in the past 12 months. MySQL Database Exposed — 26% Postgres Database Exposed — 16% API Documentation Exposed — 15% WordPress Admin Panel Exposed — 15% Remote Desktop Service Exposed — 11% SNMP Service Exposed — 9% phpMyAdmin Admin Panel Exposed — 8% UPnP Service Exposed — 8% NTP Service Exposed — 7% RPC Portmapper Service Exposed — 7% Databases dominate the top two spots Exposed databases take the top two spots, with more than a quarter of organizations exposing MySQL and Postgres, affecting 1 in 6. Internet-facing databases have long been a target for opportunistic attackers. The PLEASE_READ_ME ransomware campaign in 2020 compromised more than 250,000 MySQL databases by brute-forcing weak credentials. MongoDB and Elasticsearch have faced the same. API documentation is more exposed than RDP API documentation ranked third — ahead of RDP, which surprised us. Some API docs are intentionally public, but organizations frequently overlook documentation tied to private or admin-side APIs that were never meant to be discoverable. Public API docs can turn otherwise hard-to-find vulnerabilities into documented attack paths. RDP remains a ransomware entry point RDP at number five is a concern given its history as an initial access vector in ransomware attacks. BlueKeep in 2019 left nearly a million systems immediately exploitable. Credential guessing against exposed RDP remains one of the most reliable ways ransomware operators get in. The rest of the list was never meant to be internet-facing The remainder of the list — SNMP, UPnP, NTP, RPC — are legacy services designed for internal networks that were never meant to be internet-facing. Get the full findings Most teams treat patching as the priority. But for a lot of what's on this list — databases, admin panels, legacy services — the better question is why they're reachable at all. That's where attack surface reduction comes in — and for most organizations, it's not getting the same attention as vulnerability management. The full findings, including breakdowns by company size and industry, are in the 2026 Attack Surface Management Index . Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  API Security , Attack Surfa
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: The Top 10 Attack Surface Exposures in 2026
  - Published: 2026-06-17T10:30:00+00:00
  - Link: https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html
  - Summary: Breaches don't always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk. With time-to-exploit now down to a

### Cluster 41256d55c8 — score 8

- Title: CVE-2026-5667: Unauthenticated Remote Control of Mitsubishi MAC-577IF-2E WiFi Adapters via Probe Request Reconnaissance
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-06-18T18:05:44+00:00
- Link: https://www.reddit.com/r/netsec/comments/1u9dncq/cve20265667_unauthenticated_remote_control_of/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-5667

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-5667
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-5667
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/Ecstatic_Priority514 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: CVE-2026-5667: Unauthenticated Remote Control of Mitsubishi MAC-577IF-2E WiFi Adapters via Probe Request Reconnaissance
  - Published: 2026-06-18T18:05:44+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u9dncq/cve20265667_unauthenticated_remote_control_of/
  - Summary: submitted by /u/Ecstatic_Priority514 [link] [comments]
