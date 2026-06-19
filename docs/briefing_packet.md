# PHANTOMSignal Briefing Packet

- Generated: 2026-06-19T19:01:33.439536+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 307
- Total clusters raw: 132
- Total clusters in packet: 63
- Dropped low score: 69
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
  - In window count: 3
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
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 8
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 2
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
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
  - In window count: 3
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 9
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 3
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 7
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 4
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **The DFIR Report** (detection_response_operations)
  - URL: https://thedfirreport.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Active Countermeasures** (detection_response_operations)
  - URL: https://www.activecountermeasures.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 2
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 7
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 3
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 4
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
  - In window count: 1
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 20
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
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
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 1
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 23
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 7
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
- **Reddit r/netsecstudents** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsecstudents/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 46
- **Reddit r/AskNetsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/AskNetsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 27
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 15
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

### Google Cloud vulnerability activity
- Anchor signal: Google Cloud
- Theme key: google-cloud
- Cluster count: 5
- Article count: 18
- Cohesion: 0.228
- Shared strong signals: Google Cloud
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_industries: financial_services
  - affected_products: Google Cloud
  - urgency_signals: preauth_unauth
- Cluster IDs: 1b1b76f133, e90454cc0b, f6709feff6, f05cf21728, 512ea8982c
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-35273/
  - https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research/
  - https://www.securityweek.com/majority-of-internet-accessible-redcap-servers-outdated/
  - https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/
  - https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/
  - https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://aws.amazon.com/blogs/security/threat-tactic-spotlight-subdomain-takeover/
  - https://permiso.io/blog/gcp-servicedata-officially-deprecated-actively-dangerous
  - https://www.wiz.io/blog/red-agent-pov-ssrf
  - https://www.infosecurity-magazine.com/news/aws-continuum-ai-vulnerability/
  - https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/
  - https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything
  - https://risky.biz/SRB171/
  - https://www.reddit.com/r/netsec/comments/1u9ybfu/monitoring_the_claude_execution_layer_with/

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 5
- Article count: 11
- Cohesion: 0.309
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: ba048c19c8, 165b535ec0, 75ea622200, bfe56aaca6, f4c821a558
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
  - https://orca.security/resources/blog/mastra-npm-supply-chain-attack/
  - https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
  - https://cloud.google.com/blog/topics/developers-practitioners/how-i-learned-go-in-a-day-with-antigravity-20-and-how-you-can-do-the-same/
  - https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/
  - https://www.microsoft.com/en-us/security/blog/2026/06/17/beyond-the-benchmark-advancing-security-at-ai-speed/
  - https://securitylabs.datadoghq.com/articles/azure-blob-storage-ransomware-four-methods/
  - https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html
  - https://www.microsoft.com/en-us/security/blog/2026/06/17/crypto-clipper-uses-tor-worm-like-propagation-for-persistence-control/

### active exploitation targeting AWS
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 3
- Article count: 14
- Cohesion: 0.304
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: AWS
  - urgency_signals: preauth_unauth
- Cluster IDs: 643755a74a, f05cf21728, b6bc3df279
- Links:
  - https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20253/
  - https://www.helpnetsecurity.com/2026/06/19/splunk-vulnerability-cve-2026-20253-exploited/
  - https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure/
  - https://www.reddit.com/r/netsec/comments/1u46wbb/why_use_applevel_auth_when_every_database_has/
  - https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html
  - https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/
  - https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://aws.amazon.com/blogs/security/threat-tactic-spotlight-subdomain-takeover/
  - https://permiso.io/blog/gcp-servicedata-officially-deprecated-actively-dangerous
  - https://www.wiz.io/blog/red-agent-pov-ssrf
  - https://www.infosecurity-magazine.com/news/aws-continuum-ai-vulnerability/
  - https://webflow.sysdig.com/blog/how-attackers-are-jailbreaking-llms-with-ctf-framing-and-how-to-catch-them

### Microsoft Entra vulnerability activity
- Anchor signal: Microsoft Entra
- Theme key: microsoft-entra
- Cluster count: 4
- Article count: 4
- Cohesion: 0.248
- Shared strong signals: Microsoft Entra
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Entra
- Cluster IDs: 62e6b1535e, ecad4b1a4b, e2ef0ac5b5, 41719728a2
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48558/
  - https://horizon3.ai/intelligence/blogs/autonomy-is-earned-not-claimed/
  - https://securitylabs.datadoghq.com/articles/agent-id-inside-agent-compromise/
  - https://www.elastic.co/security-labs/aad-graph-activity-logs-threat-detection

### supply chain targeting WordPress
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 4
- Article count: 17
- Cohesion: 0.229
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, web_shell_backdoor, credential_theft
  - affected_industries: government, financial_services
  - affected_products: WordPress
  - urgency_signals: preauth_unauth
- Cluster IDs: d1df71d8fb, f05cf21728, 93df5bfc62, c220c2d05e
- Links:
  - https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html
  - https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/
  - https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://aws.amazon.com/blogs/security/threat-tactic-spotlight-subdomain-takeover/
  - https://permiso.io/blog/gcp-servicedata-officially-deprecated-actively-dangerous
  - https://www.wiz.io/blog/red-agent-pov-ssrf
  - https://www.infosecurity-magazine.com/news/aws-continuum-ai-vulnerability/
  - https://risky.biz/RBNEWS577/
  - https://www.bleepingcomputer.com/news/security/shapedplugin-update-flow-hacked-to-infect-wordpress-sites/
  - https://thehackernews.com/2026/06/operation-endgame-disrupts-socgholish.html
  - https://www.securityweek.com/15000-wordpress-websites-cleaned-up-in-socgholish-botnet-takedown/
  - https://www.infosecurity-magazine.com/news/wordpress-plugin-supply-chain/
  - https://www.securityweek.com/cryptobandits-malware-doubles-as-a-backdoor-abuses-tor/

### CVE-2026-20253 exploitation activity
- Anchor signal: CVE-2026-20253
- Theme key: cve-2026-20253
- Cluster count: 2
- Article count: 7
- Cohesion: 0.591
- Shared strong signals: CVE-2026-20253
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-20253
- Cluster IDs: 643755a74a, bffa610f21
- Links:
  - https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20253/
  - https://www.helpnetsecurity.com/2026/06/19/splunk-vulnerability-cve-2026-20253-exploited/
  - https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure/
  - https://www.reddit.com/r/netsec/comments/1u46wbb/why_use_applevel_auth_when_every_database_has/
  - https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html
  - https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/

### supply chain targeting Fortinet
- Anchor signal: Fortinet
- Theme key: fortinet
- Cluster count: 4
- Article count: 8
- Cohesion: 0.302
- Shared strong signals: Fortinet
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, data_breach
  - affected_industries: financial_services, healthcare, government, critical_infrastructure
  - affected_products: Fortinet
- Cluster IDs: 55705936f5, 6bc465fddb, c220c2d05e, 99669f5bd4
- Links:
  - https://risky.biz/RBNEWS579/
  - https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/
  - https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html
  - https://cyberscoop.com/fortinet-fortisandbox-vulnerabilities-exploits/
  - https://www.infosecurity-magazine.com/news/operation-escaneo-cloudsek-latam/
  - https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/
  - https://www.securityweek.com/cryptobandits-malware-doubles-as-a-backdoor-abuses-tor/
  - https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/

### Ivanti active exploitation
- Anchor signal: Ivanti
- Theme key: ivanti
- Cluster count: 3
- Article count: 7
- Cohesion: 0.2
- Shared strong signals: Ivanti
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Ivanti
  - urgency_signals: actively_exploited
- Cluster IDs: bffa610f21, 55705936f5, bfe56aaca6
- Links:
  - https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/
  - https://risky.biz/RBNEWS579/
  - https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/
  - https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html
  - https://cyberscoop.com/fortinet-fortisandbox-vulnerabilities-exploits/
  - https://www.infosecurity-magazine.com/news/operation-escaneo-cloudsek-latam/
  - https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html

### CVE-2026-48558 exploitation activity
- Anchor signal: CVE-2026-48558
- Theme key: cve-2026-48558
- Cluster count: 2
- Article count: 3
- Cohesion: 0.2
- Shared strong signals: CVE-2026-48558
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-48558
  - urgency_signals: preauth_unauth
- Cluster IDs: 1b1b76f133, 62e6b1535e
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-35273/
  - https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48558/

### ShinyHunters: ransomware extortion
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 2
- Article count: 7
- Cohesion: 0.2
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - actor_attribution: ShinyHunters
- Cluster IDs: 1b1b76f133, 20bb6721fd
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-35273/
  - https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - https://www.securityweek.com/cybersecurity-firms-impacted-by-klue-supply-chain-attack/
  - https://securitylabs.datadoghq.com/articles/mapping-out-your-unknown-threat-hunters-guide-to-salesforce/
  - https://www.helpnetsecurity.com/2026/06/19/klue-salesforce-data-breach-huntress/
  - https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
  - https://www.bleepingcomputer.com/news/security/klue-oauth-breach-linked-to-icarus-salesforce-data-theft-attacks/

### supply chain targeting npm
- Anchor signal: npm
- Theme key: npm
- Cluster count: 2
- Article count: 11
- Cohesion: 0.2
- Shared strong signals: npm
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain
  - affected_products: npm
- Cluster IDs: ba048c19c8, 20bb6721fd
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
  - https://orca.security/resources/blog/mastra-npm-supply-chain-attack/
  - https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
  - https://cloud.google.com/blog/topics/developers-practitioners/how-i-learned-go-in-a-day-with-antigravity-20-and-how-you-can-do-the-same/
  - https://www.securityweek.com/cybersecurity-firms-impacted-by-klue-supply-chain-attack/
  - https://securitylabs.datadoghq.com/articles/mapping-out-your-unknown-threat-hunters-guide-to-salesforce/
  - https://www.helpnetsecurity.com/2026/06/19/klue-salesforce-data-breach-huntress/
  - https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
  - https://www.bleepingcomputer.com/news/security/klue-oauth-breach-linked-to-icarus-salesforce-data-theft-attacks/

### credential theft targeting Palo Alto Networks
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 2
- Article count: 8
- Cohesion: 0.2
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: credential_theft
  - affected_industries: government
  - affected_products: Palo Alto Networks
- Cluster IDs: f05cf21728, 39e22586b8
- Links:
  - https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/
  - https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://aws.amazon.com/blogs/security/threat-tactic-spotlight-subdomain-takeover/
  - https://permiso.io/blog/gcp-servicedata-officially-deprecated-actively-dangerous
  - https://www.wiz.io/blog/red-agent-pov-ssrf
  - https://www.infosecurity-magazine.com/news/aws-continuum-ai-vulnerability/
  - https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html

## Forward signals

### Novelty
- Novel cves: 5
  - CVE-2026-34413 (first seen via Rapid7 at 2026-06-19T17:08:23+00:00, cluster 77122429c6)
  - CVE-2026-34414 (first seen via Rapid7 at 2026-06-19T17:08:23+00:00, cluster 77122429c6)
  - CVE-2026-34415 (first seen via Rapid7 at 2026-06-19T17:08:23+00:00, cluster 77122429c6)
  - CVE-2026-41459 (first seen via Rapid7 at 2026-06-19T17:08:23+00:00, cluster 77122429c6)
  - CVE-2026-41679 (first seen via Rapid7 at 2026-06-19T17:08:23+00:00, cluster 77122429c6)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (2)
- **Cybersecurity Firms Impacted by Klue Supply Chain Attack**
  - Cluster: 20bb6721fd
  - Sources in window: 3
  - Window hours: 3.9
  - Cohort count: 2
- **In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum**
  - Cluster: f05cf21728
  - Sources in window: 3
  - Window hours: 5.0
  - Cohort count: 2

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-20253 + AWS (cluster 643755a74a, first observation: True)
- Pair: CVE-2026-34413 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-34414 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-34415 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-41459 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-41679 + Linux kernel (cluster 77122429c6, first observation: True)
- Pair: CVE-2026-35273 + ShinyHunters (cluster 1b1b76f133, first observation: True)
- Pair: CVE-2026-35273 + UNC6240 (cluster 1b1b76f133, first observation: True)
- Pair: CVE-2026-35273 + Google Cloud (cluster 1b1b76f133, first observation: True)
- Pair: CVE-2026-48558 + ShinyHunters (cluster 1b1b76f133, first observation: True)
- Pair: CVE-2026-48558 + UNC6240 (cluster 1b1b76f133, first observation: True)
- Pair: CVE-2026-48558 + Google Cloud (cluster 1b1b76f133, first observation: True)
- Pair: ShinyHunters + Google Cloud (cluster 1b1b76f133, first observation: True)
- Pair: UNC6240 + Google Cloud (cluster 1b1b76f133, first observation: True)
- Pair: CVE-2026-48558 + Microsoft Entra (cluster 62e6b1535e, first observation: True)

### Drift (2)
- **ShinyHunters** (cluster 1b1b76f133)
  - New industries: financial_services
  - New products: Google Cloud
  - Prior top industries: education, government, telecommunications
  - Prior top products: Azure, Google/Gemini, npm
- **UNC6240** (cluster 1b1b76f133)
  - New industries: financial_services
  - New products: (none)
  - Prior top industries: education, government, telecommunications
  - Prior top products: Azure, Google Cloud, npm

### Persistence (5)
- actor_attribution: ShinyHunters (weeks observed: 3, cluster 1b1b76f133)
- cve_ids: CVE-2026-20245 (weeks observed: 3, cluster 2d5c32428f)
- cve_ids: CVE-2026-11645 (weeks observed: 3, cluster bfe56aaca6)
- cve_ids: CVE-2026-0257 (weeks observed: 3, cluster 39e22586b8)
- cve_ids: CVE-2026-42271 (weeks observed: 3, cluster b6bc3df279)

### Tier inversion (4)
- **LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers**
  - Cluster: 29fcf4633f
  - Primary source: The Hacker News
  - Strong signals: CVE-2026-40217, CVE-2026-47101, CVE-2026-47102
- **Squidbleed (CVE-2026-47729) - Heartbleed-style vulnerability that leaks internal memory from every version of Squid Proxy, in its default configuration**
  - Cluster: 5b5787f3bd
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-47729
- **OpenBSD MPLS kernel stack leaks remotely (CVE-2026-56099)**
  - Cluster: 5e1e9d778f
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-56099
- **CVE-2026-5667: Unauthenticated Remote Control of Mitsubishi MAC-577IF-2E WiFi Adapters via Probe Request Reconnaissance**
  - Cluster: 41256d55c8
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-5667

## Clusters

### Cluster 643755a74a — score 48

- Title: Why Use App-Level Auth When Every Database Has Auth? (Splunk Enterprise CVE-2026-20253 Pre-Auth RCE)
- Source: watchTowr Labs (offensive_vulnerability_research)
- Published: 2026-06-12T20:35:13+00:00
- Link: https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 6
- Strong signals: CVE-2026-20253

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: AWS
- cve_ids: CVE-2026-20253
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: AWS
- cve_ids: CVE-2026-20253
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Three posts? In three days? Are we insane? We're home alone, there's no one to stop us, and we're up past bedtime. So, we need to talk about Splunk. On June 10th, Splunk published this CVE-2026-20253 advisory : It has everything that we
```

#### Full body

```
Three posts? In three days? Are we insane? We're home alone, there's no one to stop us, and we're up past bedtime. So, we need to talk about Splunk. On June 10th, Splunk published this CVE-2026-20253 advisory : It has everything that we love: No authentication requirements, An almost full-mark CVSS score, Claims to be a security product, Vulnerability name longer than the average piece of spaghetti. We immediately had questions, though: No explicit mention of RCE, But a CVSS score of 9.8 suggests something is possible. Is this a default-install vulnerability, or does it require star/moon alignment? Only one way to find out? As always, watchTowr clients gain industry-first access to our research days before publication to validate their exposure, accompanied by Active Defense capabilities to autonomously mitigate exposure. This research is a glimpse into the capability that powers our Preemptive Exposure Management solution, and gets organizations ahead of inevitable in-the-wild exploitation: the watchTowr Platform. What Is A Splunk? We thought you’d never ask. Splunk Enterprise is a software platform for searching, monitoring, and analyzing machine-generated data at scale. It ingests logs, metrics, and event data from across an organization's IT environment - servers, applications, network devices, and security tools - and indexes it so it can be queried in near real time using Splunk's Search Processing Language (SPL). Teams use it to build dashboards, trigger alerts, and investigate operational or security issues from a single repository. Splunk Enterprise acts as the core engine of the wider Splunk ecosystem, supporting use cases from infrastructure monitoring to security information and event management (SIEM). So, now you know. Thanks, Mythos. So, Is It Vulnerable By Default? Well, friends, let’s take a look. As we can read in the advisory, the vulnerability exists in something called the “PostgreSQL Sidecar Service Endpoint”. We are not Splunk experts (thankfully, for those around us), but we have been forced to realize that Splunk comes in many shapes and forms. For example: Splunk Enterprise On-Premise (installed manually) on Windows - PostgreSQL Sidecar Service is not installed by default. Splunk Enterprise On-Premise (installed manually) on Windows - PostgreSQL Sidecar Service is installed, but not enabled by default. Splunk Enterprise on AWS - PostgreSQL Sidecar Service is installed and enabled by default. Tl;dr Splunk Enterprise on AWS is vulnerable out of the box. Going further through the advisory, we can see that the vulnerability affects Splunk versions 10 and above. Again, not experts, but we’re led to believe that the concept of a ‘Sidecar’ was introduced in Splunk version 10, so the stars are aligning and making sense. Below is a list of vulnerable and “different” versions from the official advisory: Splunk updated their advisory to clarify that Cloud instances are not affected. With that, we have enough information to begin our usual drama, and so we dug in. Finding The Vulnerable Service As discussed, the advisory has already provided us with a good selection of hints. The first (it’s in the title) indicates that the vulnerability exists within the PostgreSQL Sidecar Service. A quick Google search revealed that all the Sidecar Services should be deployed in the /opt/splunk/var/run/supervisor/pkg-run/ directory: The one with the postgres in its name felt like a good initial candidate: Knowing that it should be running by default, we quickly decided to confirm that this was the case, and whether it was exposing anything to a network interface: ss -tupln | grep -i splunk-postgres tcp LISTEN ... 127.0.0.1:5435 0.0.0.0:* users:(("splunk-postgres",pid=4067,fd=12)) tcp LISTEN ... 127.0.0.1:33669 0.0.0.0:* users:(("splunk-postgres",pid=4067,fd=3)) This was a promising start. We had a very large splunk-postgres binary to stare at, and we knew it was listening on several ports, including 5435 . There was one small p
```

#### Corroborating sources (6)

- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: Why Use App-Level Auth When Every Database Has Auth? (Splunk Enterprise CVE-2026-20253 Pre-Auth RCE)
  - Published: 2026-06-12T20:35:13+00:00
  - Link: https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/
  - Summary: Three posts? In three days? Are we insane? We're home alone, there's no one to stop us, and we're up past bedtime. So, we need to talk about Splunk. On June 10th, Splunk published this CVE-2026-20253 advisory : It has everything that we
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-20253 | Splunk Enterprise PostgreSQL Sidecar Service Arbitrary File Write Vulnerability
  - Published: 2026-06-16T15:23:54+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20253/
  - Summary: CVE-2026-20253 is a critical unauthenticated arbitrary file write vulnerability affecting Splunk Enterprise. The flaw may allow attackers to create or truncate files and potentially achieve remote code execution.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Unauthenticated RCE in Splunk Enterprise under active attack (CVE-2026-20253)
  - Published: 2026-06-19T10:50:33+00:00
  - Link: https://www.helpnetsecurity.com/2026/06/19/splunk-vulnerability-cve-2026-20253-exploited/
  - Summary: CISA has added CVE-2026-20253, a critical, remotely exploitable vulnerability in Splunk Enterprise, to its Known Exploited Vulnerabilities catalog, and ordered US federal civilian agencies to apply mitigations by June 21, 2026. In-the-wild exploitation has also been confirmed by the vendor and Resecurity, who said that its potential for full system compromise should push organizations to prioritize patching and review systems for indicators of compromise such as: Requests containing path traversal sequences (../) PostgreSQL connection parameters … More → The post Unauthenticated RCE in Splunk Enterprise under active attack (CVE-2026-20253) appeared first on Help Net Security .
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure
  - Published: 2026-06-19T04:10:34+00:00
  - Link: https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure/
  - Summary: CISA has given federal agencies only three days to patch CVE-2026-20253, which can be exploited for unauthenticated remote code execution. The post Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure appeared first on SecurityWeek .
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Why Use App-Level Auth When Every Database Has Auth? (Splunk Enterprise CVE-2026-20253 Pre-Auth RCE) - watchTowr Labs
  - Published: 2026-06-12T20:37:06+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u46wbb/why_use_applevel_auth_when_every_database_has/
  - Summary: submitted by /u/dx7r__ [link] [comments]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication
  - Published: 2026-06-13T13:23:03+00:00
  - Link: https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html
  - Summary: Splunk has released security updates to address a critical security flaw in Splunk Enterprise that could be exploited to conduct unauthenticated file operations and even remote code execution. The vulnerability, tracked as CVE-2026-20253, is rated 9.8 on the CVSS scoring system. "In Splunk Enterprise versions below 10.2.4 and 10.0.7, an unauthenticated user could create or truncate arbitrary

### Cluster 77122429c6 — score 40

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

### Cluster 1b1b76f133 — score 37

- Title: CVE-2026-35273 | Oracle PeopleSoft PeopleTools Unauthenticated Remote Code Execution Vulnerability | Active Exploitation
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-12T20:04:24+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-35273/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-35273, ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters, UNC6240
- affected_industries: education, financial_services
- affected_products: Google Cloud
- cve_ids: CVE-2026-35273, CVE-2026-48558
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- actor_attribution: ShinyHunters, UNC6240
- affected_industries: financial_services, education
- affected_products: Google Cloud
- cve_ids: CVE-2026-35273, CVE-2026-48558
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-35273 is a critical unauthenticated remote code execution vulnerability affecting Oracle PeopleSoft PeopleTools. Threat intelligence confirms active exploitation by ShinyHunters prior to disclosure.
```

#### Full body

```
CVE-2026-35273 Oracle PeopleSoft PeopleTools Unauthenticated Remote Code Execution Vulnerability | Active Exploitation SimpleHelp has released patches for CVE-2026-48558, an authentication bypass vulnerability affecting deployments configured to use OpenID Connect (OIDC) authentication. The issue stems from how SimpleHelp validates identity provider assertions, Oracle has disclosed CVE-2026-35273, a critical unauthenticated remote code execution vulnerability affecting Oracle PeopleSoft Enterprise PeopleTools versions 8.61 and 8.62. The flaw exists within the Updates Environment Management component and can be exploited remotely over HTTP without valid credentials. Successful exploitation may allow attackers to execute arbitrary code, take control of affected servers, access sensitive enterprise data, modify application logic, and disrupt critical business operations. Public reporting and threat intelligence indicate the vulnerability has already been exploited in the wild as a zero-day by the ShinyHunters threat group prior to Oracle’s advisory. Technical Details CVE-2026-35273 affects the Updates Environment Management component of Oracle PeopleSoft Enterprise PeopleTools. Key characteristics include: Unauthenticated remote code execution Network exploitable over HTTP No user interaction required Low attack complexity Affects PeopleTools 8.61 and 8.62 Can lead to complete server compromise According to Oracle and threat intelligence reporting, exploitation allows attackers to gain control of vulnerable PeopleSoft environments, potentially exposing HR, payroll, financial, student, and operational data. The vulnerability requires only network access to a reachable PeopleSoft endpoint. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this remote code execution vulnerability can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether vulnerable PeopleSoft endpoints can be exploited. Patch immediately: Apply Oracle’s recommended mitigations and security updates for supported PeopleTools versions. Re-run the test: Confirm the vulnerability is no longer exploitable after remediation. Indicators of Compromise Indicator Type Description 142.11.200[.]186-190 IP Address Known attacker infrastructure associated with observed exploitation activity 108.174.202[.]99 IP Address Known attacker infrastructure associated with observed exploitation activity 176.120.22[.]24 IP Address Known attacker infrastructure associated with observed exploitation activity UNC6240 (ShinyHunters) Threat Actor Group attributed to active exploitation campaign May 27 – June 9, 2026 Activity Window Period during which exploitation activity was observed Threat intelligence from Google Cloud and Mandiant identified active compromise and extortion campaigns targeting Oracle PeopleSoft environments. Researchers observed exploitation activity prior to Oracle’s June 10, 2026 disclosure, confirming zero-day exploitation in the wild. ShinyHunters reportedly targeted approximately 300 PeopleSoft instances across more than 100 organizations. A publicly acknowledged victim was the University of Nottingham. Affected versions & patch Affected: Oracle PeopleSoft Enterprise PeopleTools 8.61 Oracle PeopleSoft Enterprise PeopleTools 8.62 Patch: Apply Oracle’s security update and recommended mitigations immediately. Oracle advises customers running unsupported PeopleTools versions to upgrade to a supported release as soon as possible. Restrict access to Environment Management Hub (PSEMHUB) endpoints and ensure they are not exposed externally wherever possible. Timeline May 27, 2026 – Earliest observed exploitation activity attributed to UNC6240 (ShinyHunters). June 9, 2026 – Latest date
```

#### Corroborating sources (2)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-35273 | Oracle PeopleSoft PeopleTools Unauthenticated Remote Code Execution Vulnerability | Active Exploitation
  - Published: 2026-06-12T20:04:24+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-35273/
  - Summary: CVE-2026-35273 is a critical unauthenticated remote code execution vulnerability affecting Oracle PeopleSoft PeopleTools. Threat intelligence confirms active exploitation by ShinyHunters prior to disclosure.
- **Check Point Research** (threat_research_primary)
  - Title: 15th June – Threat Intelligence Report
  - Published: 2026-06-15T13:40:44+00:00
  - Link: https://research.checkpoint.com/2026/15th-june-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 15th June, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES The University of Nottingham, a UK research university, has suffered a data breach after ShinyHunters accessed its student records system. The incident affected about 454,600 current and former students and exposed contact details, […] The post 15th June – Threat Intelligence Report appeared first on Check Point Research .

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

### Cluster 62e6b1535e — score 27

- Title: CVE-2026-48558 | SimpleHelp OIDC Authentication Bypass Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-15T16:05:47+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48558/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48558

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Entra
- cve_ids: CVE-2026-48558
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_products: Microsoft Entra
- cve_ids: CVE-2026-48558
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-48558 is an authentication bypass vulnerability affecting SimpleHelp OIDC deployments. The flaw may allow attackers to create unauthorized Technician accounts and gain privileged access to managed endpoints.
```

#### Full body

```
CVE-2026-48558 SimpleHelp OIDC Authentication Bypass Vulnerability SimpleHelp has released patches for CVE-2026-48558, an authentication bypass vulnerability affecting deployments configured to use OpenID Connect (OIDC) authentication. The issue stems from how SimpleHelp validates identity provider assertions, allowing an unauthenticated attacker to create and authenticate as a new Technician account under certain configurations. Because Technician accounts can remotely access managed endpoints, execute scripts, and perform administrative actions, successful exploitation can lead to significant compromise of a managed environment. Horizon3.ai identified and responsibly disclosed the vulnerability to SimpleHelp. Technical Details The vulnerability affects SimpleHelp servers configured to use either generic OIDC or Azure AD OIDC authentication. An attacker can create and authenticate as a new Technician user when the following conditions exist: OIDC is enabled, and at least one OIDC authentication provider is configured on the SimpleHelp server. At least one TechnicianGroup is associated with the OIDC provider. “Allow group authenticated logins” is enabled on the TechnicianGroup. Successful exploitation allows an attacker to: Create a new Technician account. Bypass technician MFA enrollment requirements by registering their own MFA device during first login. Access managed endpoints through the SimpleHelp platform. Execute scripts and perform privileged technician actions. According to Horizon3.ai’s research, approximately 14,000 SimpleHelp servers were exposed to the internet at the time of disclosure, with roughly 7.2% of sampled servers configured to use the vulnerable OIDC authentication method. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this authentication bypass can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether unauthorized Technician account creation is possible. Patch immediately: Upgrade to a fixed SimpleHelp release and review OIDC authentication configurations. Re-run the test: Confirm the vulnerability is no longer exploitable after remediation. Indicators of Compromise Administrators should review all group-authenticated Technician accounts by navigating to: Administration → Technicians → Gear Icon → Show Group Authenticated Users Investigate any unfamiliar technician names or email addresses. Review server logs for evidence of unauthorized technician registration, including entries similar to: Registering technician login for rapidresponse-4b611bdd@horizon3.ai / (Technicians) Configuration save requested (Forged Attacker - rapidresponse-4b611bdd@horizon3.ai [(Technicians)] [New Anon]) Relevant log locations: Indicator Type Description /opt/SimpleHelp/logs/server.log Log File Primary SimpleHelp server log /opt/SimpleHelp/logs/<YYYYMMDD-HHMMSS>/server.log Log File Historical server logs Registering technician login for ... Log Entry Evidence of technician creation Configuration save requested ... [New Anon] Log Entry Potential unauthorized technician registration Affected Versions & Patch Affected: SimpleHelp deployments configured with OIDC authentication that meet the vulnerable configuration requirements described above. Patch: Upgrade to the patched versions (SimpleHelp 5.5.16 or SimpleHelp 6.0 RC2) per SimpleHelp’s security update. If patching cannot be performed immediately, restrict Technician authentication to approved source IP addresses per Horizon3.ai researchers’ recommendation: Administration → Login Security Timeline May 21, 2026 — Horizon3.ai discovered the authentication bypass vulnerability and it was assigned CVE-2026-48558. May 21, 2026 — Researchers validated exploitability in real-world
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-48558 | SimpleHelp OIDC Authentication Bypass Vulnerability
  - Published: 2026-06-15T16:05:47+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-48558/
  - Summary: CVE-2026-48558 is an authentication bypass vulnerability affecting SimpleHelp OIDC deployments. The flaw may allow attackers to create unauthorized Technician accounts and gain privileged access to managed endpoints.

### Cluster ba048c19c8 — score 23

- Title: From package to postinstall payload: Inside the Mastra npm supply chain compromise
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-18T03:43:04+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 4
- Strong signals: Microsoft Defender, npm

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, supply_chain, zero_day
- affected_industries: financial_services
- affected_products: Anthropic/Claude, Apple iOS/macOS, Microsoft Defender, npm
- cve_ids: CVE-2026-50656
- urgency_signals: zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: npm, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
A poisoned npm package infected 140+ projects with a hidden payload. This report highlights how to detect, hunt, and defend against supply chain attacks using Microsoft Defender and actionable threat intelligence. The post From package to postinstall payload: Inside the Mastra npm supply chain compromise appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Malware npm Content types Research Products and services Microsoft Defender Topics Actionable threat insights Microsoft Threat Intelligence observed a large-scale npm supply chain attack affecting 140+ packages across the mastra and @mastra scopes on the npm registry. Microsoft shared its findings with the npm security team, and the compromised packages have been removed and the attacker’s publish access to the @mastra scope has been revoked. The compromise originated from the takeover of the ehindero npm maintainer account, which had publish rights across the Mastra ecosystem and was used to publish poisoned package versions that introduced easy-day-js , a malicious typosquat of the popular dayjs library. Once installed, easy-day-js triggered a postinstall hook that executed an obfuscated dropper script, disabled Transport Layer Security (TLS) certificate verification, contacted attacker-controlled command-and-control (C2) infrastructure, downloaded a second-stage payload, and executed the payload as a detached hidden process. The activity followed a coordinated staged delivery pattern, with a clean bait version published first, followed by a weaponized version and rapid publication of the compromised Mastra packages. Because the payload executes during installation, any developer workstation or continuous integration and continuous delivery (CI/CD) pipeline that ran npm install or npm update after the compromised versions were published was potentially exposed, regardless of whether the package was imported in application code. This created risk to credentials, tokens, build environments, and downstream software integrity. Microsoft Defender Antivirus, Microsoft Defender for Endpoint, and Microsoft Defender XDR provide detections and hunting coverage for suspicious Node.js execution, malicious package behavior, reflective code loading, persistence activity and command-and-control communication. Attack chain overview Figure 1. End-to-end attack chain from npm account takeover through mass dependency injection to second-stage payload execution. At a high level, the attack progressed through six phases: Account compromise: The attacker gained control of the ehindero npm account , a listed maintainer with publish rights across the entire @mastra scope. Typosquat creation: The attacker published easy-day-js , a package impersonating the legitimate dayjs library (57M+ weekly downloads), using a coordinating anonymous email account ). Mass poisoning: Using the compromised account, the attacker published new versions of 140+packages across the @mastra scope, each injected with easy-day-js@^1.11.21 as a new dependency. All poisoned versions were tagged as latest. Delivery: Developers and CI/CD pipelines running npm install automatically resolved to the compromised versions. The semantic versioning (SemVer) range ^1.11.21 resolved to 1.11.22, the version containing the malicious postinstall hook. Execution: The postinstall hook executed an obfuscated 4,572-byte dropper that disabled TLS verification, dropped tracking markers, and contacted the C2 server. Second-stage payload: The dropper fetched executable code from the C2 server, wrote it as a randomly named .js file, and spawned it as a fully detached, window-hidden Node.js process. Discovery and initial indicators Microsoft Threat Intelligence identified the compromise through anomalous publishing patterns on the mastra package. All previous versions of mastra (through v1.13.0) were published through GitHub Actions OpenID Connect (OIDC), the legitimate CI/CD pipeline. Version 1.13.1 was manually published by ehindero using a Tutamail address, an anonymous email service. Figure 2. Publisher comparison across mastra versions showing the anomalous manual publish on v1.13.1. The only change between mastra@1.13.0 and mastra@1.13.1 was the addition of easy-day-js@^1.11.21 as a dependency. No corresponding code changes were present in the Mastra GitHub
```

#### Corroborating sources (4)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: From package to postinstall payload: Inside the Mastra npm supply chain compromise
  - Published: 2026-06-18T03:43:04+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
  - Summary: A poisoned npm package infected 140+ projects with a hidden payload. This report highlights how to detect, hunt, and defend against supply chain attacks using Microsoft Defender and actionable threat intelligence. The post From package to postinstall payload: Inside the Mastra npm supply chain compromise appeared first on Microsoft Security Blog .
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: 144 Mastra npm Packages Compromised via Supply Chain Attack
  - Published: 2026-06-17T15:31:39+00:00
  - Link: https://orca.security/resources/blog/mastra-npm-supply-chain-attack/
  - Summary: A critical supply chain attack was disclosed affecting the entire @mastra/* npm scope, allowing attackers to deploy a cross-platform infostealer on any system that installed affected packages. Due to the potential for credential theft, cryptocurrency wallet compromise, and full system persistence, immediate remediation is required for all affected environments. Technical Overview The issue originates from […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: 145 Mastra npm Packages Compromised via Hijacked Contributor Account
  - Published: 2026-06-17T07:38:24+00:00
  - Link: https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
  - Summary: As many as 145 npm packages associated with the Mastra namespace ("@mastra/*"), a popular open-source JavaScript and TypeScript framework for building artificial intelligence (AI) applications, have been compromised as part of a software supply chain attack codenamed easy-day-js, per findings from Endor Labs, JFrog, OX Security, SafeDep, Socket, StepSecurity, and Synk. "A single npm account (
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: How I learned Go in a Day with Antigravity 2.0 and How You Can Do the Same
  - Published: 2026-06-15T09:29:00+00:00
  - Link: https://cloud.google.com/blog/topics/developers-practitioners/how-i-learned-go-in-a-day-with-antigravity-20-and-how-you-can-do-the-same/
  - Summary: I have been exploring how to reclaim my software stack from NPM dependency overhead and replace my resource-intensive Node.js runtime with a compiled, single-binary Go CLI. The result of my efforts is skl , a fast tool we use for managing Agent Skills, that launches in 2ms and uses only 11MB of memory. But how exactly did I do it? Simply, I set the architectural goals and audited the logic, while Antigravity handled the mechanical work of code translation, test generation, and platform path mappings for us. This post describes the step-by-step walkthrough of our migration workflow to help you build yours. Step 0: Seed personal learning goals Before writing any code, you start by defining the boundaries of your project. In our case, I wanted a zero-dependency core that used minimal external packages. I decided that our CLI tool needs to be fast, and our security model had to be zero-trust wherever appropriate. In the process, my agent added specific constraints: sanitizing all of our in

### Cluster 2d5c32428f — score 22

- Title: Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-16T06:05:58+00:00
- Link: https://thehackernews.com/2026/06/cisco-releases-security-updates-for.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-20262

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-20122, CVE-2026-20127, CVE-2026-20182, CVE-2026-20245, CVE-2026-20262
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage, active_exploitation
- affected_industries: government
- affected_products: Cisco
- cve_ids: CVE-2026-20262, CVE-2026-20245, CVE-2026-20182, CVE-2026-20127, CVE-2026-20122
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cisco has released security updates for a medium-severity security flaw in Catalyst SD-WAN Manager that has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-20262, carries a CVSS score of 6.5 out of 10.0. "A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file or
```

#### Full body

```
Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw  Ravie Lakshmanan  Jun 16, 2026 Vulnerability / Network Security Cisco has released security updates for a medium-severity security flaw in Catalyst SD-WAN Manager that has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-20262 , carries a CVSS score of 6.5 out of 10.0. "A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file or overwrite any file on the filesystem of an affected system," Cisco said in an advisory. The issue, the networking equipment company added, stems from inadequate validation of user-supplied input during a file upload process. An attacker could exploit this behavior to create or overwrite any file on the underlying operating system by sending crafted HTTP requests to an affected API endpoint. This, in turn, could be weaponized to elevate to the root. However, successful exploitation hinges on the attacker already having valid credentials with at least write access. The vulnerability impacts the following products regardless of the deployment type - Cisco Catalyst SD-WAN Manager On-Prem Cisco SD-WAN Cloud-Pro Cisco SD-WAN Cloud (Cisco Managed) Cisco SD-WAN for Government (FedRAMP) Patches have been released to address the issue - Cisco Catalyst SD-WAN Release 20.9.9.1 and earlier - Fixed in 20.9.9.2 Cisco Catalyst SD-WAN Release 20.12.7.1 and earlier - Fixed in 20.12.7.2 Cisco Catalyst SD-WAN Release 20.15.4.4 and earlier - Fixed in 20.15.4.5 Cisco Catalyst SD-WAN Release 20.15.5.2 and earlier - Fixed in 20.15.5.3 Cisco Catalyst SD-WAN Release 20.18.3 - Fixed in 20.18.3.1 Cisco Catalyst SD-WAN Release 26.1.1.1 and earlier - Fixed in 26.1.1.2 Cisco said it "became aware of limited exploitation of this vulnerability" in June 2026, adding it was discovered during internal security testing. The company has also shared indicators of compromise associated with the malicious activity, urging customers to audit "/var/log/nms/vmanage-server.log" for suspicious WAR file uploads as below - 11-June-2026 03:53:37,310 EDT INFO [a66cdc5f-807d-4c23-944e-5c809a2ece6b] [server] [SdraAnyConnectFileUploadHandler] (default task-40704) |default| uploaded Remote Access Anyconnect profile file: ../../../../var/lib/wildfly/standalone/deployments/suspicious.war to vManage. Other indicators include attempts to deploy malicious code and interact with it, although Cisco has warned that they may not "consistently appear" in every incident log. The follow-on activities related to this vulnerability are - /var/log/nms/vmanage-appserver.log: 11-June-2026 07:52:55,275 UTC INFO [server] (DeploymentScanner-threads - 2) WFLYSRV0010: Deployed "suspicious.war" (runtime-name : "suspicious.war") /var/log/nms/containers/service-proxy/serviceproxy-access.log: [2026-06-11T07:57:33.635Z] "POST /suspicious/index.jsp HTTP/1.1" 200 - 267 76 17 - "1.1.1.54" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0" "d7336b83-422b-4000-93e1-0296f102bbed" "1.1.1.4:8443" "127.0.0.1:8080" CVE-2026-20262 is the eighth security flaw impacting Cisco SD-WAN to be flagged as actively exploited this year alone after CVE-2026-20245, CVE-2026-20182, CVE-2026-20127, CVE-2026-20122, CVE-2026-20128, CVE-2026-20133, and CVE-2022-20775. The exploitation of some of these flaws has been attributed to an advanced persistent threat (APT) actor named UAT-8616. The development has prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to add the flaw to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by June 29, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  CISA , cisco , KEV , network security , Patch Management , pri
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw
  - Published: 2026-06-16T06:05:58+00:00
  - Link: https://thehackernews.com/2026/06/cisco-releases-security-updates-for.html
  - Summary: Cisco has released security updates for a medium-severity security flaw in Catalyst SD-WAN Manager that has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-20262, carries a CVSS score of 6.5 out of 10.0. "A vulnerability in the web UI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, remote attacker to create a file or

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

### Cluster e90454cc0b — score 20

- Title: Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-06-15T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: UNC6508

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, web_shell_backdoor
- actor_attribution: UNC6508
- affected_industries: healthcare
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- actor_attribution: UNC6508
- affected_industries: healthcare
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Patrick Whitsell, John McGuiness Google Threat Intelligence Group (GTIG) has identified a sophisticated campaign attributed to UNC6508, a People's Republic of China (PRC)-nexus threat actor, targeting institutions in the North American academic, medical, and military research community. While remaining undetected for over a year, the threat actor compromised externally facing web applications, deployed bespoke malware, pivoted to sensitive internal systems, and abused enterprise administrative tools for covert data exfiltration. The threat actor had broad collection aspirations, including sensitive defense intelligence related to national security, Indo-Pacific command operations, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, and medical research. GTIG disrupted the malicious infrastructure associated with this threat actor. Working with Mandiant Consulting, we notified the affected organizations upon detection and offered our assistance with
```

#### Full body

```
Threat Intelligence Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research June 15, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Written by: Patrick Whitsell, John McGuiness Google Threat Intelligence Group (GTIG) has identified a sophisticated campaign attributed to UNC6508, a People's Republic of China (PRC)-nexus threat actor, targeting institutions in the North American academic, medical, and military research community. While remaining undetected for over a year, the threat actor compromised externally facing web applications, deployed bespoke malware, pivoted to sensitive internal systems, and abused enterprise administrative tools for covert data exfiltration. The threat actor had broad collection aspirations, including sensitive defense intelligence related to national security, Indo-Pacific command operations, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, and medical research. GTIG disrupted the malicious infrastructure associated with this threat actor. Working with Mandiant Consulting, we notified the affected organizations upon detection and offered our assistance with remediation. We have updated Google Security Operations (SecOps) with relevant intelligence, enabling defenders to identify indicators of compromise (IOCs) within their networks. We encourage all users and customers to follow recommended best practices for third-party Identity Providers (IdP) and ensure 2-Step Verification (2SV) is enabled across all accounts. Campaign Overview The campaign targeted a diverse set of national, state, and private medical entities. These organizations comprise world-renowned clinical providers, premier academic centers, North American military health institutions, professional advocacy groups, and health regulatory bodies. Their research areas span a broad spectrum of modern medicine, from molecular discovery and clinical drug trials to state-level public health policy and military readiness. They employ thousands of people with a combined research budget in the billions of dollars. The earliest known compromise occurred in September 2023, after which GTIG observed a consistent operational pattern. The threat actor exploited externally facing REDCap (Research Electronic Data Capture) servers and deployed custom malware named INFINITERED to capture legitimate REDCap login credentials. Then, after remaining undetected for more than a year, UNC6508 used the captured credentials to access the victim’s internal network. The threat actor was also observed using the novel technique of manipulating domain content compliance rules for data exfiltration. Lastly, UNC6508 used sophisticated operations security (OpSec) techniques to conceal and obfuscate their activity. GTIG collaborated closely with Mandiant Consulting, the FLARE team, and Workspace Security on this effort to combine our threat intelligence, incident response, and reverse engineering expertise across Google Cloud. This enabled us to develop a complete picture of the attack lifecycle from initial compromise to complete mission. GTIG also extends thanks to the affected organizations for their cooperation and the valuable post-exploitation insights they shared. Prevention, Detection, and Remediation GTIG recommends defenders implement the following security measures, across all Cloud enterprise platforms, to mitigate this threat: Secure Admin Accounts : Enforce phishing-resistant 2-Step Verification (2SV) for enterprise administrator accounts, including through third-party Identity Providers. Advanced Protection : Consider enrolling highly sensitive accounts in our Advanced Protection Program for additional safeguards against malware and phishing attacks. Prevent Cookie Theft : Enforce Device Bound Session Credentials (DBSC) with CAA for high
```

#### Corroborating sources (3)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research
  - Published: 2026-06-15T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research/
  - Summary: Written by: Patrick Whitsell, John McGuiness Google Threat Intelligence Group (GTIG) has identified a sophisticated campaign attributed to UNC6508, a People's Republic of China (PRC)-nexus threat actor, targeting institutions in the North American academic, medical, and military research community. While remaining undetected for over a year, the threat actor compromised externally facing web applications, deployed bespoke malware, pivoted to sensitive internal systems, and abused enterprise administrative tools for covert data exfiltration. The threat actor had broad collection aspirations, including sensitive defense intelligence related to national security, Indo-Pacific command operations, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, and medical research. GTIG disrupted the malicious infrastructure associated with this threat actor. Working with Mandiant Consulting, we notified the affected organizations upon detection and offered our assistance with
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research
  - Published: 2026-06-15T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research/
  - Summary: Written by: Patrick Whitsell, John McGuiness Google Threat Intelligence Group (GTIG) has identified a sophisticated campaign attributed to UNC6508, a People's Republic of China (PRC)-nexus threat actor, targeting institutions in the North American academic, medical, and military research community. While remaining undetected for over a year, the threat actor compromised externally facing web applications, deployed bespoke malware, pivoted to sensitive internal systems, and abused enterprise administrative tools for covert data exfiltration. The threat actor had broad collection aspirations, including sensitive defense intelligence related to national security, Indo-Pacific command operations, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, and medical research. GTIG disrupted the malicious infrastructure associated with this threat actor. Working with Mandiant Consulting, we notified the affected organizations upon detection and offered our assistance with
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Majority of Internet-Accessible REDCap Servers Outdated
  - Published: 2026-06-18T17:07:48+00:00
  - Link: https://www.securityweek.com/majority-of-internet-accessible-redcap-servers-outdated/
  - Summary: These servers are regularly targeted by China-linked UNC6508 for initial access and backdoor deployment. The post Majority of Internet-Accessible REDCap Servers Outdated appeared first on SecurityWeek .

### Cluster 165b535ec0 — score 18

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

### Cluster f6709feff6 — score 17

- Title: Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE
- Source: Unit 42 (threat_research_primary)
- Published: 2026-06-16T10:00:29+00:00
- Link: https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 discovered a Vertex AI Python SDK vulnerability that allows remote code execution via bucket squatting. Read the article for more. The post Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Cloud Cybersecurity Research Cloud Cybersecurity Research Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE 11 min read Related Products Cortex Cortex Cloud Unit 42 AI Security Assessment Unit 42 Incident Response By: Ori Hadad Published: June 16, 2026 Categories: Cloud Cybersecurity Research Threat Research Tags: Bucket squatting Google Cloud Joblib Python RCE SDKs Vertex AI Vulnerability Share Executive Summary We discovered a vulnerability in the Google Cloud Vertex AI software development kit (SDK) for Python, and responsibly disclosed it to Google. Before Google’s fix, the vulnerability would have allowed an attacker operating entirely from their own Google Cloud project to hijack a victim's model upload and poison it. By exploiting this flaw in vulnerable versions of the SDK, an attacker can achieve remote code execution (RCE) within a target’s Vertex AI serving infrastructure, with zero initial access to the victim's project. The root enabler of this attack is a predictable default bucket name, combined with a missing ownership check in the SDK's staging logic. When a Vertex AI user uploads a model without specifying a custom staging bucket, the SDK constructs a bucket name using a deterministic pattern based on the project ID and region. An attacker who knows the victim's project ID can preemptively create this bucket in their own project, a technique known as bucket squatting. The SDK then silently uploads the victim's model artifacts to the attacker-controlled bucket. Subsequently, within a narrow window of opportunity, the attacker replaces the legitimate model with one that carries a malicious payload. Once the victim deploys the compromised model, the attacker's code executes. In vulnerable SDK versions, this can lead to data exfiltration, lateral movement and further compromise of the victim's cloud environment. We refer to the process of exploiting this vulnerability as Pickle in the Middle because it relies in part on deserializing a built-in module called pickle , as explained below in Pickle Deserialization as Attack Vector. We reported the vulnerability to the Google security team, and they accepted our findings. The issue affected google-cloud-aiplatform SDK versions 1.139.0 and 1.140.0, which was the latest at the time of testing. Google completed the fixes to address this issue in v1.148.0, which was released April 15, 2026. We recommend that developers upgrade to fixed versions of the SDK. Cortex Cloud Cortex AI-SPM The Unit 42 AI Security Assessment and Unit 42 Frontier AI Defense service can help identify and mitigate complex AI-specific risks. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Vertex AI , RCE , Google Cloud , SDKs, Python Background and Terminology Vertex AI is a machine learning platform for training and deploying ML models and AI applications. The Vertex AI SDK for Python is the primary client library that developers use to interact with the platform programmatically. We focused our research on the Vertex AI SDK for Python ( google-cloud-aiplatform ), as many enterprises rely on it to create and manage their AI/ML pipelines, applications and models. The Vertex AI Model Registry is a centralized repository within Vertex AI where users store, version and manage their ML models. When a user uploads a model to the Model Registry via the SDK, the SDK first stages the model artifacts in a Google Cloud Service (GCS) bucket before registering them with the service. The Model Registry then references these staged artifacts. When the model is deployed to an endpoint, Google's internal infrastructure (specifically, a Per-Product, Per-Project Service Account or P4SA) loads them into a serving container. Figure 1 shows the intended model upload flow. Figure 1. Uploading a model to Model Registry. Bucket Squatting Bucket squatting is a class of
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE
  - Published: 2026-06-16T10:00:29+00:00
  - Link: https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/
  - Summary: Unit 42 discovered a Vertex AI Python SDK vulnerability that allows remote code execution via bucket squatting. Read the article for more. The post Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE appeared first on Unit 42 .

### Cluster bffa610f21 — score 17

- Title: CISA: Splunk Enterprise flaw actively exploited, patch by Sunday
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-19T10:39:58+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Ivanti, cPanel
- cve_ids: CVE-2026-20253
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Ivanti, cPanel
- cve_ids: CVE-2026-20253
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
CISA has urged U.S. federal agencies to secure their systems by Sunday against a critical Splunk Enterprise vulnerability that is being exploited in attacks. [...]
```

#### Full body

```
CISA: Splunk Enterprise flaw actively exploited, patch by Sunday By Sergiu Gatlan June 19, 2026 06:39 AM 0 The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has urged federal agencies to secure their systems by Sunday against a critical Splunk Enterprise vulnerability that is being exploited in attacks. Tracked as CVE-2026-20253 , this security flaw affects Splunk Enterprise (versions 10.2.0 to 10.2.3 and 10.0.0 to 10.0.6) and allows remote attackers without privileges to create or truncate arbitrary files on vulnerable devices via a PostgreSQL sidecar service endpoint. "The vulnerability exists because the PostgreSQL sidecar service endpoint lacks authentication controls, allowing any network-reachable user to invoke file operations without credentials," the Splunk security team said in a security advisory published last week. On June 12, days after Splunk released security patches, WatchTowr published a technical write-up, shared proof-of-concept exploit code , and warned that the flaw can be abused for remote code execution attacks. On Wednesday, June 18, Splunk updated its advisory, urging customers to patch their systems as soon as possible due to evidence of in-the-wild exploitation. "In June 2026, the Splunk Product Security Incident Response Team (PSIRT) became aware of limited exploitation of this vulnerability. Splunk strongly recommends that customers upgrade to a fixed software release to remediate this vulnerability," it said. Internet security watchdog group Shadowserver tracks over 1,400 Internet-exposed Splunk instances , most of them from North America (952) and Europe (223). However, there is no information on how many of them are vulnerable to ongoing attacks targeting the CVE-2026-20253 flaw. Splunk instances exposed online (Shadowserver) On Thursday, CISA confirmed that threat actors are now actively abusing the CVE-2026-20253 vulnerability in attacks and ordered Federal Civilian Executive Branch (FCEB) agencies to patch their Splunk instances by Sunday, as mandated by Binding Operational Directive (BOD) 26-04. Issued last week , CISA's BOD 26-04 requires U.S. government agencies to prioritize patching based on each vulnerability's risk of exploitation. "This type of vulnerability is a frequent attack vector for malicious cyber actors and poses significant risks to the federal enterprise," the cybersecurity agency said yesterday. "Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines." Splunk also shared mitigation measures for admins who can't immediately patch vulnerable systems, advising them to disable the PostgreSQL sidecar service to remove the attack surface. However, it also warned that disabling PostgreSQL would break Edge Processor, OpAmp, or SPL2 data pipelines on affected instances. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: CISA orders feds to patch max severity Joomla plugin flaw by Friday CISA warns of another cPanel plugin flaw exploited in attacks CISA orders feds to patch actively exploited Ivanti flaw by Sunday CISA orders feds to patch exploited Ivanti EPMM flaw by Saturday CISA flags new SD-WAN flaw as actively exploited in attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA: Splunk Enterprise flaw actively exploited, patch by Sunday
  - Published: 2026-06-19T10:39:58+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/
  - Summary: CISA has urged U.S. federal agencies to secure their systems by Sunday against a critical Splunk Enterprise vulnerability that is being exploited in attacks. [...]

### Cluster 55705936f5 — score 16

- Title: Risky Bulletin: Creds for 74,000 Fortinet devices leaked
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-06-19T05:23:40+00:00
- Link: https://risky.biz/RBNEWS579/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, supply_chain
- affected_products: Fortinet, Ivanti
- cve_ids: CVE-2026-25089, CVE-2026-39808, CVE-2026-39813
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

#### Corroborating sources (5)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Creds for 74,000 Fortinet devices leaked
  - Published: 2026-06-19T05:23:40+00:00
  - Link: https://risky.biz/RBNEWS579/
  - Summary: A LOT of Fortinet creds have leaked online, Canada’s spy agency allowed to remove a botnet from Canadian devices, a supply chain attack hits the Mastra AI framework, and Europol disrupts SocGolish.
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: FortiBleed: 86,000 Fortinet Device Credentials Compromised
  - Published: 2026-06-19T10:48:08+00:00
  - Link: https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/
  - Summary: The large-scale credential theft campaign hit roughly half of the internet-accessible Fortinet firewalls and VPNs. The post FortiBleed: 86,000 Fortinet Device Credentials Compromised appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Three Fortinet FortiSandbox Flaws, One Patched Last Week
  - Published: 2026-06-16T10:30:41+00:00
  - Link: https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html
  - Summary: Bad actors are exploiting multiple security vulnerabilities in Fortinet FortiSandbox, according to threat intelligence firm Defused Cyber. In a post shared on X, the company said it has observed exploitation of CVE-2026-39813, CVE-2026-39808, and CVE-2026-25089 over the past 24 hours. CVE-2026-39813 (CVSS score: 9.1) refers to a path traversal vulnerability in FortiSandbox JRPC API that could
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Attackers hit pair of critical Fortinet vulnerabilities the vendor disclosed in April
  - Published: 2026-06-17T15:42:46+00:00
  - Link: https://cyberscoop.com/fortinet-fortisandbox-vulnerabilities-exploits/
  - Summary: Multiple firms have observed active exploitation of the FortiSandbox defects, and warn that the attacks originate from multiple sources, not a single campaign. The post Attackers hit pair of critical Fortinet vulnerabilities the vendor disclosed in April appeared first on CyberScoop .
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: LATAM Infrastructure Hit by Fortinet and Ivanti Exploits
  - Published: 2026-06-18T11:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/operation-escaneo-cloudsek-latam/
  - Summary: CloudSEK maps Operation Escaneo, a campaign hitting Latin American infrastructure via perimeter bugs

### Cluster 75ea622200 — score 16

- Title: Beyond the benchmark: Advancing security at AI speed
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-06-17T19:30:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/beyond-the-benchmark-advancing-security-at-ai-speed/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Azure

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_products: Azure, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

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

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Beyond the benchmark: Advancing security at AI speed
  - Published: 2026-06-17T19:30:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/06/17/beyond-the-benchmark-advancing-security-at-ai-speed/
  - Summary: Read how Microsoft Security has advanced its agentic vulnerability detection system, codename MDASH, integrating into real-world workflows across Windows, Azure, and identity systems. The post Beyond the benchmark: Advancing security at AI speed appeared first on Microsoft Security Blog .
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Holding blobs for ransom: Four methods for Azure Storage ransomware
  - Published: 2026-06-15T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/azure-blob-storage-ransomware-four-methods/
  - Summary: This post explores four vectors for threat actors to abuse Azure Storage to maliciously encrypt victim blobs, including step-by-step explanations and event codes for detection.

### Cluster f05cf21728 — score 14

- Title: In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-06-19T15:23:36+00:00
- Link: https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 7
- Strong signals: AWS, Google Cloud

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, supply_chain, vulnerability_disclosure, web_shell_backdoor
- affected_industries: aviation_defense, critical_infrastructure, financial_services, government
- affected_products: AWS, Google Cloud, Palo Alto Networks, WordPress
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report, vendor_announcement
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft, web_shell_backdoor, vulnerability_disclosure
- affected_industries: financial_services, government, critical_infrastructure, aviation_defense
- affected_products: AWS, Google Cloud, WordPress
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Other noteworthy stories that might have slipped under the radar: Android TV botnet Popa linked to Israeli firm, Velvet Ant maintained decade-long stealth, unpatched GCP Config Connector flaw enables takeover. The post In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum appeared first on SecurityWeek .
```

#### Full body

```
SecurityWeek’s weekly cybersecurity news roundup offers a concise overview of important developments that may not receive full standalone coverage but remain relevant to the broader threat landscape. This curated summary highlights key stories across vulnerability disclosures, emerging attack methods, policy updates, industry reports, and other noteworthy events to help readers maintain a well-rounded awareness of the evolving cybersecurity environment. Here are this week’s highlights: 10-year-old phpBB flaw enables session hijacking Researchers uncovered a critical authentication bypass in phpBB versions up to 3.3.16 and 4.0.0-a2. A single unauthenticated HTTP request can impersonate any user, including admins, exposing private messages and forum content, and providing full administrative control. phpBB users should upgrade immediately to 3.3.17 or the latest master branch. The issue, reported via HackerOne, received a patch within days, but thousands of active forums remain exposed. Advertisement. Scroll to continue reading. Velvet Ant maintained decade-long stealth in air-gapped critical infrastructure China-nexus actor Velvet Ant compromised an organization’s segregated network starting around 2016. It chained internet-facing footholds, Nginx/FastCGI proxies, and backdoored PAM/OpenSSH components for credential theft and persistent access. The group deployed variants of GS-Netcat, SOCKS5 proxies, and nine pam_unix.so backdoors across hosts. Remediation proved complex. MaXSS and Spyder flaws expose 10 million Chrome users to hacking Critical vulnerabilities in SiderAI (Spyder) and MaxAI (MaXSS) agentic side-panel Chrome extensions can allow malicious websites to trigger arbitrary extension actions, including hidden tab screenshots, AI memory dumps, and potential file access. With over 10 million combined installs and no vendor response, the issues enable full browser session compromise and account takeovers without user interaction. Users should remove the extensions until fixed. AWS unveils Continuum AWS has announced a new AI-powered tool designed to help organizations discover, prioritize, validate, and resolve vulnerabilities. Available in gated preview, Continuum takes findings from existing tools and its own scanning, prioritizing them based on exploitability in the user’s own environment. 1.2 million WordPress sites compromised in OptinMonster supply chain attack Attackers injected malicious JavaScript into Awesome Motive’s OptinMonster, TrustPulse, and PushEngage WordPress plugin CDN scripts. The payload activates for logged-in admins, creating rogue administrator accounts and a hidden backdoor plugin. The breach stemmed from a compromised UpdraftPlus instance and CDN key. The supply chain attack is believed to have hit more than 1.2 million WordPress sites. FTC says imposter scams cost Americans $3.5 billion in 2025 The FTC reported imposter scams as the most common fraud category, with losses nearly tripling since 2020. Bank and government impersonation schemes drove the bulk of the damage, often via fake security alerts urging money transfers. Overall fraud losses hit a record $16 billion. The agency continues enforcement under its Impersonation Rule and supports public awareness campaigns. US DOT closes investigation into Delta’s 2024 CrowdStrike outage response The Department of Transportation ended its probe into Delta’s prolonged recovery from the global CrowdStrike incident without penalties. Investigators found the airline provided adequate refunds, baggage help, and support for passengers with disabilities. This aligns with the current administration’s shift away from certain Biden-era consumer protection enforcement approaches. JetBrains Marketplace plugins steal developer AI keys At least 15 malicious AI coding assistant plugins , published in the JetBrains Marketplace under various vendor accounts, exfiltrate OpenAI, DeepSeek, and similar API keys. The plugins have racked up nearly 70,000 installs while
```

#### Corroborating sources (7)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum
  - Published: 2026-06-19T15:23:36+00:00
  - Link: https://www.securityweek.com/in-other-news-apple-patches-beats-eavesdropping-flaw-dot-closes-delta-crowdstrike-probe-aws-continuum/
  - Summary: Other noteworthy stories that might have slipped under the radar: Android TV botnet Popa linked to Israeli firm, Velvet Ant maintained decade-long stealth, unpatched GCP Config Connector flaw enables takeover. The post In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Google Vertex AI SDK Flaw Let Attackers Hijack Model Uploads via Bucket Squatting
  - Published: 2026-06-16T19:05:41+00:00
  - Link: https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
  - Summary: A flaw in the Google Cloud Vertex AI SDK for Python let an attacker with no access to a victim's project hijack the victim's machine learning model upload and run code inside Google's serving infrastructure. Palo Alto Networks Unit 42, which found and reported the bug through Google's bug bounty program, calls the technique "Pickle in the Middle" and said it saw no exploitation in the wild.
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: What’s new with Google Cloud
  - Published: 2026-06-19T16:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - Summary: Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Jun 15 - Jun 19 Join us for a deep dive into agentic AI control with AppyThings Your integrations aren’t failing—they are evolving. When users interact with AI agents, they no longer arrive directly at your site, resulting in experiences stripped of your context, expertise, and intended experience. Join us on Thursday, June 25, for a community tech talk in partnership with AppyThings to learn how to solve this new gateway challenge. We will explore how MTN laid an integration foundation with the Model Context Protocol (MCP) to deliver accurate, consistent experiences. Our technical experts will demonstrate how to l
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Threat tactic spotlight: Subdomain takeover
  - Published: 2026-06-16T17:53:20+00:00
  - Link: https://aws.amazon.com/blogs/security/threat-tactic-spotlight-subdomain-takeover/
  - Summary: In this blog post you’ll learn how to detect and prevent subdomain takeover – a tactic where threat actors exploit dangling DNS records to redirect traffic to attacker-controlled resources. We’ll explain the issue, how the situation arises, and how you can use various AWS features and services to help mitigate the impact of this tactic. […]
- **Permiso Security** (cloud_identity_infrastructure)
  - Title: Mind the Gap: GCP serviceData in Logs Explorer vs. Exported Logs
  - Published: 2026-06-16T12:46:59+00:00
  - Link: https://permiso.io/blog/gcp-servicedata-officially-deprecated-actively-dangerous
  - Summary: Cloud audit logs are the backbone of detection engineering in cloud environments. They provide the raw telemetry that security teams depend on to identify suspicious behavior, build detection rules and reconstruct attacker activity after an incident. In cloud platforms like GCP, every meaningful administrative action leaves a trace in the form of an audit log entry and the quality of that trace directly affects the reliability of these investigative and detection efforts.
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: The Red Agent POV: How it Reasoned its Way to SSRF
  - Published: 2026-06-17T14:33:51+00:00
  - Link: https://www.wiz.io/blog/red-agent-pov-ssrf
  - Summary: Part 1: How the Red Agent uncovered a multi-step attack chain allowing SSRF-to-Local-File-Read on a GCP Cloud Run API
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: AWS Unveils 'Continuum,' an AI-Powered Vulnerability Management Platform
  - Published: 2026-06-19T11:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/aws-continuum-ai-vulnerability/
  - Summary: Working with frontier AI models, this new platform aims to help discovering, prioritizing, validating and remediating code vulnerabilities

### Cluster 2ae6e90456 — score 12

- Title: AI Infrastructure Security: Pentesting MCP & Agentic Systems
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-19T09:20:11+00:00
- Link: https://horizon3.ai/intelligence/blogs/ai-infrastructure-pentesting-and-security/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, web_shell_backdoor, zero_day
- affected_products: Anthropic/Claude
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day, ai_security, web_shell_backdoor
- affected_products: Anthropic/Claude
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Autonomous pentesting discovers MCP servers, inference endpoints, and agentic systems. It verifies exploitable paths before attackers reach your infrastructure.
```

#### Full body

```
AI Infrastructure Security: Pentesting MCP & Agentic Systems Horizon3.ai June 19, 2026 Blogs AI infrastructure has a new attack surface, and most security teams are not testing it. Model Context Protocol (MCP) servers, LLM inference endpoints, and agentic AI systems are being deployed into production environments at speed. Each one introduces a new class of exposure: not just the model itself, but the infrastructure it can reach, the credentials it can access, and the actions it can take. The boundary that matters is not where the model runs. It is where the agent acts. Horizon3.ai’s research into AI system pentesting frames the core problem precisely: prompt injection and jailbreaking are not the interesting boundary. The real boundary is where agents take action. That reframe changes everything about how security teams should approach AI infrastructure testing. How Attackers Move Through AI Systems AI systems are not isolated. They connect to internal networks, identity stores, and data repositories. An attacker who reaches an AI inference endpoint does not stop at the model. The Webapp-to-Infrastructure Kill Chain A documented attack chain against an Anthropic-hosted environment illustrates the full path. Claude discovered a Server-Side Request Forgery (SSRF) vulnerability in a web application. It then escalated privileges and mapped the internal network. From there, it attacked internal infrastructure and created a persistent backdoor user account. The kill chain ran: webapp to identity to infrastructure. This is the pattern that matters. The AI system became the pivot point. The SSRF was the entry. The backdoor was the outcome. Why Agentic Automation Changes the Defender’s Window Ninety percent of that entire attack campaign was executed by a series of agents. Human-speed response assumptions do not apply when the attacker is automated. Agentic systems compress the time between initial access and persistent compromise to a window that most detection and response workflows cannot close. Vulnerability scanners produce a list of CVEs. Autonomous pentesting finds the exploitable path through an AI system before an attacker does. The Specific Risk from MCP Servers MCP servers are a new and largely untested attack surface in most enterprise environments. Horizon3.ai’s AI pentesting initiative targets MCP servers directly. The approach covers discovery of AI inference and chatbot endpoints, discovery of AI-related data, credentials, and hosts, and targeted testing of those endpoints to find paths to data, credentials, or connected infrastructure. The goal is not to evaluate model behavior in isolation. It is to determine what an attacker can reach through the model. MCP servers sit between AI agents and the tools, APIs, and data sources those agents call. A misconfigured MCP server can expose internal credentials, allow unauthorized tool invocation, or provide a pivot point into backend infrastructure. These are infrastructure risks, not model risks. They require infrastructure-class testing. Traditional pentest firms test what they can schedule. Autonomous pentesting discovers and tests MCP servers as part of continuous infrastructure assessment. NodeZero’s Technical Approach to AI Infrastructure Testing NodeZero extends existing infrastructure testing to cover the AI attack surface. The approach combines production-safe autonomous pentesting with AI and ML workflows for narrow reasoning tasks including zero-day vulnerability discovery, advanced exploitation, and evasion. Discovery and Fingerprinting NodeZero discovers AI inference endpoints and MCP servers as part of network discovery and fingerprinting. AI-related data, credentials, and hosts are identified alongside traditional infrastructure assets. This means AI systems are not tested in isolation. They are tested as part of the full attack surface. Exploit-Led Validation NodeZero’s technical stack covers credential harvesting and validation, implant and post-exploitation,
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: AI Infrastructure Security: Pentesting MCP & Agentic Systems
  - Published: 2026-06-19T09:20:11+00:00
  - Link: https://horizon3.ai/intelligence/blogs/ai-infrastructure-pentesting-and-security/
  - Summary: Autonomous pentesting discovers MCP servers, inference endpoints, and agentic systems. It verifies exploitable paths before attackers reach your infrastructure.

### Cluster a9ba6bfe90 — score 11

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

### Cluster 254cc405b8 — score 11

- Title: From a VHDX File to a Remcos RAT, (Tue, Jun 16th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-06-16T07:09:13+00:00
- Link: https://isc.sans.edu/diary/rss/33080
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
Yesterday, a reader reported to us a malicious ZIP archive (SHA256: a0104921a2d37ab87482ac9a9f5c3713479c118846c3e999178e75b81620c094[ 1 ]). Once unzipped, it contains a VHDX file that discloses a malicious JavaScript after being mounted (which is automatic on modern Windows OSs):
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: From a VHDX File to a Remcos RAT, (Tue, Jun 16th)
  - Published: 2026-06-16T07:09:13+00:00
  - Link: https://isc.sans.edu/diary/rss/33080
  - Summary: Yesterday, a reader reported to us a malicious ZIP archive (SHA256: a0104921a2d37ab87482ac9a9f5c3713479c118846c3e999178e75b81620c094[ 1 ]). Once unzipped, it contains a VHDX file that discloses a malicious JavaScript after being mounted (which is automatic on modern Windows OSs):

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

### Cluster bfe56aaca6 — score 11

- Title: F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-18T17:32:14+00:00
- Link: https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-42530

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- affected_products: Anthropic/Claude, Ivanti, Microsoft Defender
- cve_ids: CVE-2026-11645, CVE-2026-42055, CVE-2026-42530, CVE-2026-42945
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- affected_products: Anthropic/Claude, Ivanti, Microsoft Defender
- cve_ids: CVE-2026-42530, CVE-2026-42055, CVE-2026-42945, CVE-2026-11645
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems. The vulnerabilities are listed below - CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is
```

#### Full body

```
F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution  Ravie Lakshmanan  Jun 18, 2026 Vulnerability / Cloud Security F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems. The vulnerabilities are listed below - CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is configured to use the HTTP/3 QUIC module to reopen a QPACK encoder stream by means of a specially crafted HTTP/3 session, and execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. CVE-2026-42055 (CVSS v4 score: 9.2) - A heap-based buffer overflow vulnerability in the ngx_http_proxy_v2_module and ngx_http_grpc_module modules that could be triggered by a remote unauthenticated attacker when the proxy_http_version to 2 or grpc_pass directives are used to proxy HTTP/2 traffic, the ignore_invalid_headers directive is set to off, and the large_client_header_buffers directive size is larger than 2 MB, and execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Both shortcomings have been patched in the following versions - CVE-2026-42530 - NGINX Open Source 1.31.0 - 1.31.1 (Fixed in 1.31.2) NGINX Gateway Fabric 2.0.0 - 2.6.3 (Fixed in 2.6.4) NGINX Gateway Fabric 1.3.0 - 1.6.2 NGINX Instance Manager 2.17.0 - 2.22.0 NGINX Ingress Controller 5.0.0 - 5.5.0 NGINX Ingress Controller 4.0.0 - 4.0.1 NGINX Ingress Controller 3.5.0 - 3.7.2 CVE-2026-42055 - NGINX Plus 37.0.0 - 37.0.1 (Fixed in 37.0.2.1) NGINX Plus R33 - R36 (Fixed in R36 P6) NGINX Open Source 1.31.1 (Fixed in 1.31.2) NGINX Open Source 1.30.0 - 1.30.2 (Fixed in 1.30.3) NGINX Instance Manager 2.17.0 - 2.22.0 F5 WAF for NGINX 5.9.0 - 5.13.1 NGINX App Protect WAF 5.2.0 - 5.8.0 NGINX App Protect WAF 4.10.0 - 4.16.0 F5 DoS for NGINX 4.9.0 NGINX App Protect DoS 4.3.0 - 4.7.0 NGINX Gateway Fabric 2.0.0 - 2.6.3 (Fixed in 2.6.4) NGINX Gateway Fabric 1.3.0 - 1.6.2 NGINX Ingress Controller 5.0.0 - 5.5.0 NGINX Ingress Controller 4.0.0 - 4.0.1 NGINX Ingress Controller 3.5.0 - 3.7.2 As mitigations, F5 has outlined the following actions - CVE-2026-42530 - Disable HTTP/3 CVE-2026-42055 - Remove the ignore_invalid_headers off directive from the configuration, or reduce the large_client_header_buffers directive size below 2 MB Although F5 makes no mention of the vulnerabilities being exploited in the wild, security flaws in F5 products have been repeatedly exploited by bad actors. As recently as last month, another critical security defect in NGINX Plus and NGINX Open Source ( CVE-2026-42945 , CVSS score: 9.2), also called NGINX Rift, came under active exploitation within days after public disclosure. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Cloud security , F5 Networks , HTTP/2 , HTTP/3 , NGINX , remote code execution , Vulnerability , Web Server ⚡ Top Stories This Week Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities Cybersecurity Stars Awards 2026: Winners Announced Across 95 Categories ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories New GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files Agentjacking Attack Tricks AI Cod
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: F5 Patches Two Critical NGINX Open Source Flaws Enabling Remote Code Execution
  - Published: 2026-06-18T17:32:14+00:00
  - Link: https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html
  - Summary: F5 has released security updates to address two critical security flaws in NGINX Open Source that could be exploited to achieve code execution on affected systems. The vulnerabilities are listed below - CVE-2026-42530 (CVSS v4 score: 9.2) - A use-after-free vulnerability in the ngx_http_v3_module that could be triggered by a remote unauthenticated attacker when NGINX Open Source is

### Cluster 20bb6721fd — score 11

- Title: Cybersecurity Firms Impacted by Klue Supply Chain Attack
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-06-19T09:19:06+00:00
- Link: https://www.securityweek.com/cybersecurity-firms-impacted-by-klue-supply-chain-attack/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 5
- Strong signals: Salesforce

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- actor_attribution: ShinyHunters, UNC6395
- affected_products: Microsoft SharePoint, Salesforce, npm
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- actor_attribution: ShinyHunters, UNC6395
- affected_products: Salesforce, Microsoft SharePoint, npm
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The hackers exfiltrated data from Salesforce instances of Klue customers, such as Huntress and Recorded Future. The post Cybersecurity Firms Impacted by Klue Supply Chain Attack appeared first on SecurityWeek .
```

#### Full body

```
Cybersecurity firms Huntress and Recorded Future have disclosed the impact of a supply chain attack that hit market intelligence platform Klue. The attack started on June 11 and affected systems associated with software platform integrations. The hackers connected to Klue’s backend servers and executed unauthorized commands, pushing a code update to harvest OAuth tokens for customers’ Klue integrations. Klue notified customers of the incident on June 12, warning that it had deactivated OAuth tokens for all customers and disabled integrations with Salesforce, HubSpot, SharePoint, Zoom, Gong, Chorus, Clari, Google Drive, and Slack. According to ReliaQuest , the hackers abused the Salesforce REST API to exfiltrate large volumes of customer relationship management (CRM) data over a 24-hour window, “including a concentrated burst of nearly a thousand queries in 15 minutes and sustained extraction windows lasting over 6 hours”. On June 17, Salesforce disabled the Klue Battlecards app integration, warning that it “detected unusual activity involving the app that may have resulted in unauthorized access to a subset of customer data via the app’s connection to Salesforce”. On Thursday, both Huntress and Recorded Future confirmed that they were among the companies affected by the supply chain attack. Advertisement. Scroll to continue reading. “The data that was copied from our Salesforce account includes business contacts, price quotes, and other sales-related data and messaging. No threat data, passwords, payment card information, or engineering data relating to the Huntress agent or telemetry we collect was affected,” Huntress said. Recorded Future noted, “While our investigation is ongoing, we believe the impact was limited to business data fields stored in our Salesforce database, such as client contact names and email addresses. Certain business contract information may also have been potentially included in the impacted data.” The incident was limited to the Klue-Salesforce integration and the attackers did not access any systems belonging to or maintained by the two cybersecurity firms. Huntress noted that several other cybersecurity companies use Klue, but no other firm appears to have publicly disclosed impact from the attack. The attack follows the same pattern observed in previous Salesforce , Salesloft Drift , and Gainsight incidents, which have been attributed to ShinyHunters and UNC6395 , but appears to have been mounted by a new threat actor. Huntress said it received attempted extortion communication from a threat actor calling itself “Mr Brean”, who pointed to a Session Messenger ID associated with Icarus, an extortion group that emerged in April 2026. Icarus’ leak site has one entry from early May, with the data allegedly stolen from the victim already published (albeit no longer available), and another from June 16, which points to data stolen from Salesforce. “With those matching data points, we have high confidence that the Icarus actor is responsible for the Klue compromise and this supply chain attack,” Huntress says. While it has shared details of the attack with its customers, Klue has not made a public announcement on the matter. SecurityWeek has emailed the company for a statement and will update this article if it responds. Related: Atomic Arch Supply Chain Attack Hits 1,500 AUR Packages Related: Over 100 NPM, PyPI Packages Hit in New Shai-Hulud Supply Chain Attacks Related: Maine Disables Data Breach Portal Due to Fake Submissions Related: White House Issues Memo to Bolster NSS Cybersecurity Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Dream Raises $260 Million at $3 Billion Valuation Atlassian, Splunk Patch Critical Vulnerabilities Critical Command Execution Vulnerability Patched in Cisco ISE F5 Patches
```

#### Corroborating sources (5)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Cybersecurity Firms Impacted by Klue Supply Chain Attack
  - Published: 2026-06-19T09:19:06+00:00
  - Link: https://www.securityweek.com/cybersecurity-firms-impacted-by-klue-supply-chain-attack/
  - Summary: The hackers exfiltrated data from Salesforce instances of Klue customers, such as Huntress and Recorded Future. The post Cybersecurity Firms Impacted by Klue Supply Chain Attack appeared first on SecurityWeek .
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Mapping out your unknown: A threat hunter’s guide to Salesforce
  - Published: 2026-06-16T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/mapping-out-your-unknown-threat-hunters-guide-to-salesforce/
  - Summary: In this post, we walk through different threats to Salesforce and how to detect them.
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Klue breach lead to Salesforce data theft, Huntress affected
  - Published: 2026-06-19T12:57:39+00:00
  - Link: https://www.helpnetsecurity.com/2026/06/19/klue-salesforce-data-breach-huntress/
  - Summary: Cybersecurity vendor Huntress was among multiple companies hit by a breach originating at Klue, a market intelligence platform used to integrate CRM and sales data across various business tools. Huntress published a detailed account of the incident on June 18, framing it as a “security domino effect” that began with one compromised integration credential and cascaded into theft of customer data across several connected platforms, including Salesforce. Attack timeline According to Huntress’s writeup, the attackers … More → The post Klue breach lead to Salesforce data theft, Huntress affected appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Salesforce Disables Klue App Integration After OAuth Token Abuse Exposes Customer Data
  - Published: 2026-06-19T09:03:57+00:00
  - Link: https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
  - Summary: Salesforce has revealed that it disabled the Klue Battlecards app integration within its platform in response to a security incident impacting the competitive intelligence company on June 11, 2026. To that end, organizations will be unable to connect to Salesforce via the app until further notice, the American cloud-based software company noted in an alert published this week. "Salesforce took
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Klue OAuth breach linked to 'Icarus' Salesforce data theft attacks
  - Published: 2026-06-18T14:19:50+00:00
  - Link: https://www.bleepingcomputer.com/news/security/klue-oauth-breach-linked-to-icarus-salesforce-data-theft-attacks/
  - Summary: Market intelligence platform Klue suffered a OAuth breach that enabled the "Icarus" threat actors to steal Salesforce CRM data from multiple organizations in an ongoing extortion campaign. [...]

### Cluster 93df5bfc62 — score 11

- Title: Risky Bulletin: Arch Linux supply chain attack hits 1,900 packages
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-06-15T05:53:18+00:00
- Link: https://risky.biz/RBNEWS577/
- Fetch status: ok
- Member count: 8
- Corroborating source count: 5
- Strong signals: WordPress

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain
- affected_industries: financial_services
- affected_products: GitHub, WordPress
- content_type: news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng
- affected_products: WordPress
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Almost 2,000 Arch Linux packages have been infected with malware in a supply chain attack, FISA surveillance powers expire for the first time since 2008, the FBI takes down a Chinese phishing service, and a major supply chain attack hits the WordPress ecosystem.
```

#### Full body

```
Risky Bulletin Podcast June 15, 2026 Risky Bulletin: Arch Linux supply chain attack hits 1,900 packages Presented by Catalin Cimpanu News Editor Claire Aird Newsreader Almost 2,000 Arch Linux packages have been infected with malware in a supply chain attack, FISA surveillance powers expire for the first time since 2008, the FBI takes down a Chinese phishing service, and a major supply chain attack hits the WordPress ecosystem. Your browser does not support the audio element. Risky Bulletin: Arch Linux supply chain attack hits 1,900 packages â¶ 0:00 / 11:14 Subscribe Brought to you by Ent AI Protect the people, secure the system. Show notes Risky Bulletin: Arch Linux supply chain attack spreads to 1,900+ AUR packages
```

#### Corroborating sources (5)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Arch Linux supply chain attack hits 1,900 packages
  - Published: 2026-06-15T05:53:18+00:00
  - Link: https://risky.biz/RBNEWS577/
  - Summary: Almost 2,000 Arch Linux packages have been infected with malware in a supply chain attack, FISA surveillance powers expire for the first time since 2008, the FBI takes down a Chinese phishing service, and a major supply chain attack hits the WordPress ecosystem.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: ShapedPlugin update flow hacked to infect WordPress sites
  - Published: 2026-06-18T12:55:36+00:00
  - Link: https://www.bleepingcomputer.com/news/security/shapedplugin-update-flow-hacked-to-infect-wordpress-sites/
  - Summary: Multiple WordPress plugins from ShapedPlugin were compromised in a supply chain attack that distributed infected releases to paying customers via the vendor's official update system. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Operation Endgame Disrupts SocGholish Servers, Cleans 14,971 WordPress Sites
  - Published: 2026-06-19T15:07:54+00:00
  - Link: https://thehackernews.com/2026/06/operation-endgame-disrupts-socgholish.html
  - Summary: Dutch law enforcement authorities, along with counterparts from Canada , Germany, and the U.S., have disrupted malicious infrastructure associated with SocGholish and cleaned up nearly 15,000 infected WordPress websites. "With these actions we deprive cybercriminals of access to infected computer systems," Maikel Rollman of the Netherlands National High Tech Crime Unit said. "This prevents
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 15,000 WordPress Websites Cleaned Up in SocGholish Botnet Takedown
  - Published: 2026-06-19T06:46:44+00:00
  - Link: https://www.securityweek.com/15000-wordpress-websites-cleaned-up-in-socgholish-botnet-takedown/
  - Summary: Law enforcement and private partners took down 106 SocGholish C&C servers and domains as part of Operation Endgame. The post 15,000 WordPress Websites Cleaned Up in SocGholish Botnet Takedown appeared first on SecurityWeek .
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Attackers Hijack Popular WordPress Plugins to Deploy Backdoors
  - Published: 2026-06-15T17:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/wordpress-plugin-supply-chain/
  - Summary: Tampered OptinMonster and sister plugins plant hidden backdoors on 1.2 million WordPress sites

### Cluster 512ea8982c — score 11

- Title: Build and Deploy a Remote MCP Server to GKE in 30 Minutes
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-06-17T00:00:00+00:00
- Link: https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 4
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Anthropic/Claude, Google Cloud, Kubernetes
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis, tier_5_chatter

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

#### Corroborating sources (4)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Build and Deploy a Remote MCP Server to GKE in 30 Minutes
  - Published: 2026-06-17T00:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-gke-in-30-minutes/
  - Summary: Build and Deploy a Remote MCP Server to GKE in 30 Minutes Integrating context from tools and data sources into LLMs can be challenging, which impacts the ease of development for AI agents. To address this challenge, Anthropic introduced the Model Context Protocol (MCP) , which standardizes how applications provide context to these models. Developers often want to build an MCP server for their APIs to make them available to fellow developers, allowing them to use it as context in their own applications. Google Kubernetes Engine (GKE) provides a scalable, reliable, and secure environment to deploy these remote MCP servers. This guide shows the straightforward process of setting up a secure remote MCP server on GKE. MCP transports The Model Context Protocol follows a client-server architecture. It initially only supported running the server locally using the stdio transport. The protocol has since evolved and now supports remote access transports, specifically Streamable HTTP . With Strea
- **Simon Willison** (ai_security_agentic_risk)
  - Title: "They screwed us": Personality clashes sent Anthropic's models offline
  - Published: 2026-06-15T14:57:33+00:00
  - Link: https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything
  - Summary: "They screwed us": Personality clashes sent Anthropic's models offline Lots of "source familiar with the administration's thinking" and "source close to Anthropic" in this Axios piece, which is the best collection of behind-the-scenes gossip I've seen about the US government export control Mythos/Fable story so far. Logan Graham ( I lead the Frontier Red Team at Anthropic ), Dave Orr (Head of Safeguards, previously a Director of Engineering at Google DeepMind), and blog favorite Nicholas Carlini are reported to be meeting with the Commerce Department today in D.C. Good luck to them! (I just noticed Logan was "Special Adviser to the Prime Minister" in the Boris Johnson era, covering AI, science, and technology policy - so significant political experience.) This closing note doesn't give me much optimism that we'll be getting Fable back any time soon: The bottom line : One option is to make sure Anthropic's models can't be jailbroken — though perfect jailbreak resistance may be impossibl
- **Risky Business News** (practitioner_analysis)
  - Title: Srsly Risky Biz: Anthropic has artificial, but not emotional, intelligence
  - Published: 2026-06-18T06:17:55+00:00
  - Link: https://risky.biz/SRB171/
  - Summary: Tom Uren and James Wilson talk about Anthropic rolling out its latest models only to have them effectively banned by the US government within days. Although the administration’s process for assessing new models is, ahem, amorphous, Anthropic is doing itself no favours by dismissing its concerns. The company needs to show some emotional intelligence and learn how to manage upwards. They also discuss Section 702 Foreign Intelligence Surveillance Act collection. The law authorising it has lapsed amidst political shenanigans, but it looks like collection can continue until next year. Plenty of time for kicking of political footballs! This episode is also available on YouTube
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Monitoring the Claude execution layer with OpenTelemetry
  - Published: 2026-06-19T10:27:05+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u9ybfu/monitoring_the_claude_execution_layer_with/
  - Summary: submitted by /u/TheAlphaBravo [link] [comments]

### Cluster 18615ddbf5 — score 10

- Title: Inside the Modern SOC: The 72-Minute Race
- Source: Unit 42 (threat_research_primary)
- Published: 2026-06-15T23:00:19+00:00
- Link: https://unit42.paloaltonetworks.com/soc-72-minute-race/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: RansomHub, Scattered Spider
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: Scattered Spider, RansomHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Attackers can move from access to exfiltration in 72 minutes. Learn how modern SOC teams close the speed gap with Unit 42's AI-driven automation, threat hunting, MDR and Managed XSIAM. The post Inside the Modern SOC: The 72-Minute Race appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Insights Inside the Modern SOC Inside the Modern SOC Inside the Modern SOC: The 72-Minute Race 4 min read Related Products Cortex Cortex XSIAM Managed Threat Hunting Unit 42 Incident Response By: Sharon Maydar Published: June 15, 2026 Categories: Inside the Modern SOC Insights Tags: Identity Operation security Unit 42 Incident Response Report Share The Speed Gap: Where Strategy Meets Reality This marks the beginning of our series, Inside the Modern SOC: Trends and Insights from Unit 42 Managed Services . This series draws directly from Unit 42 customer environments, security operations center (SOC) assessments, threat hunting engagements and frontline investigation experience to highlight the operational patterns shaping modern security operations. Through our work helping organizations detect, investigate and respond to threats, one theme continues to surface: The speed gap has become one of the defining operational challenges facing today's SOC. Drawing on findings from the 2026 Unit 42 Global Incident Response Report , we can see that attack timelines have compressed dramatically as adversaries use AI to move faster and automate more of the attack lifecycle. In the fastest cases, attackers moved from initial access to confirmed data exfiltration in just over an hour (72 minutes), representing a 4X year-over-year acceleration. When security operations still rely on manual triage and fragmented workflows, defenders are forced to operate on a timeline modern attackers have already outpaced. This is not a personnel problem; it’s a process problem. By the time an alert is validated through manual steps, the adversary has often already achieved their objective. Anatomy of a Modern Identity-Driven Attack Across recent Unit 42 investigations, we continue to see a consistent pattern: attackers leveraging compromised credentials, identity manipulation, privilege escalation and rapid lateral movement to compress attacks that once unfolded over days into hours, or even minutes. Threat actors such as Muddled Libra (aka Scattered Spider) and Spoiled Scorpius, distributors of RansomHub ransomware, exemplify this broader trend. The Attacker's Playbook in Action The Social Entry: Initial access is often gained through compromised credentials, MFA manipulation, help-desk impersonation or other identity-based tactics. This pattern appeared across many of the investigations we handled over the past year. According to the 2026 Unit 42 Global Incident Response Report, 65% of initial access is driven by identity-based techniques. The Rapid Escalation: Once inside, attackers frequently attempt privilege escalation and administrative account abuse within minutes or hours of gaining access. Unit 42 has observed suspicious identity activity quickly escalating into abnormal administrative behavior and signs of privilege escalation. The Multi-Surface Pivot: Attackers increasingly move across identity, endpoint, cloud and Software as a Service (SaaS) environments. Once elevated privileges are obtained, they may provision cloud resources, create rogue virtual machines, mount virtual drives or establish persistence to support data staging and exfiltration. The Rapid Impact: Unit 42 investigations continue to show attackers compressing the time between initial access and business impact. In some cases, threat actors such as Spoiled Scorpius have exfiltrated hundreds of gigabytes of data within hours of gaining access through improperly secured remote access infrastructure. From a tooling perspective, the warning signs were often already present across the organization's identity and endpoint security controls. Multiple alerts had been generated, but without automated correlation, each appeared low priority in isolation. Connecting these signals manually takes time, a luxury attackers no longer allow. How Our Unit 42 Managed Services Team Responds In investigations involving identity-driven attacks, our analysts use the Cortex SecOps
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Inside the Modern SOC: The 72-Minute Race
  - Published: 2026-06-15T23:00:19+00:00
  - Link: https://unit42.paloaltonetworks.com/soc-72-minute-race/
  - Summary: Attackers can move from access to exfiltration in 72 minutes. Learn how modern SOC teams close the speed gap with Unit 42's AI-driven automation, threat hunting, MDR and Managed XSIAM. The post Inside the Modern SOC: The 72-Minute Race appeared first on Unit 42 .

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

### Cluster d4997a90c8 — score 10

- Title: Dozens of malicious wallpapers found on Steam Workshop: gamers’ accounts at risk
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-06-16T09:00:11+00:00
- Link: https://securelist.com/dozens-of-malicious-wallpapers-found-on-steam-workshop/120186/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: financial_services
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Since late 2025, malware has been spreading rapidly through the Steam Workshop, the gaming platform's built-in service for players to create and share custom content. The attackers are primarily targeting gamers in China and Russia.
```

#### Full body

```
Table of Contents What is Wallpaper Engine? Application wallpapers: a built-in security risk Inside an infected game wallpaper Attribution and victims How to stay safe Indicators of compromise Update, June 17 Authors Maxim Starodubov Denis Brylev Since late 2025, malware has been spreading rapidly through the Steam Workshop, the gaming platform’s built-in service for players to create and share custom content. The attackers are primarily targeting gamers in China and Russia, aiming to hijack their accounts. To pull this off, they are exploiting Wallpaper Engine – a popular live wallpaper app available on Steam – specifically leveraging its Workshop sharing feature. The malware is hidden inside the wallpaper packages users share with one another. Running one of these compromised wallpapers can lead to a stolen Steam account or leave the victim’s system infected with backdoors or crypto miners. What is Wallpaper Engine? Wallpaper Engine is an app that allows you to put animated wallpapers on your desktop. It’s available for both Windows and Android, though our investigation focused strictly on the Windows version. Thanks to a massive Steam community, the app is quite popular , boasting around 100,000 daily active users and nearly a million reviews. It comes with a built-in editor so users can create their own designs, and it supports a few different wallpaper types: Videos: MP4, WebM, and other common video formats Scenes: interactive wallpapers built inside the app’s own editor Web pages: HTML pages powered by JavaScript and CSS, which can also include audio and video elements Applications: active windows from third-party Windows-compatible software that Wallpaper Engine sets as the user’s desktop background That last type, application wallpapers, is where things get risky, because these are essentially standalone programs. They can be anything from mini-games you play right on your desktop, to planners, calendars, system monitors, or widgets tracking your CPU or GPU usage. Application wallpapers: a built-in security risk The whole concept of “application wallpapers” essentially allows foreign code to be run directly on your computer. Cybercriminals took note of this feature and started embedding malware right into these types of wallpapers. Because Wallpaper Engine relies on Steam Workshop for content sharing, anyone can create a wallpaper and publish it for the community to download and install for free. Naturally, this setup is a magnet for bad actors. We discovered dozens of these malicious application wallpapers floating around Steam Workshop, and each one had already been downloaded thousands – or even tens of thousands – of times. When we analyzed them, we caught two different methods the attackers were using to spread their malware: An archive containing the executable wallpaper alongside the malicious files. This payload usually consisted of compromised EXE files, DLLs, or malicious scripts. In other cases, attackers threw a curveball by hiding the malware inside a password-protected archive. Either the victim was tricked into typing the password, or a script handled it automatically. The attackers would hide the password in plain sight – either right in the archive’s name or inside a JSON configuration installed along with other wallpaper files. For all the other variations, the payload triggered automatically when the user selected and applied the wallpaper. Inside an infected game wallpaper Main screen of the wallpaper application On the surface, this wallpaper sample (above) we uncovered in December 2025 looks completely harmless. Once launched, there’s absolutely nothing to trigger your suspicion. The built-in game boots up flawlessly, runs smoothly, and the desktop controls work exactly as they should. But behind the scenes, a full-blown infection is underway. Within just a few minutes, a user might suddenly realize their Steam account has been hijacked, or find their computer crippled by malware, with their file
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Dozens of malicious wallpapers found on Steam Workshop: gamers’ accounts at risk
  - Published: 2026-06-16T09:00:11+00:00
  - Link: https://securelist.com/dozens-of-malicious-wallpapers-found-on-steam-workshop/120186/
  - Summary: Since late 2025, malware has been spreading rapidly through the Steam Workshop, the gaming platform's built-in service for players to create and share custom content. The attackers are primarily targeting gamers in China and Russia.

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

### Cluster 13400d1a7f — score 10

- Title: AI-Accelerated Exploitation: The Mythos-Era Threat Model
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-06-13T08:00:03+00:00
- Link: https://horizon3.ai/intelligence/blogs/ai-accelerated-exploitation-mythos-era-threat-model/
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
AI models like Mythos collapse the gap between discovery and exploitation. Learn how to rethink your threat model before attackers do.
```

#### Full body

```
AI-Accelerated Exploitation: The Mythos-Era Threat Model Horizon3.ai June 13, 2026 Blogs The gap between vulnerability discovery and real-world exploitation is collapsing. Mythos is an AI model that demonstrates the ability to identify vulnerabilities and generate working exploits much faster than traditional approaches. While security analysts have debated the model’s capabilities, one thing is clear: Mythos doesn’t introduce new vulnerability classes. It compresses the timeline from discovery to impact. For security teams still running annual pentests and triaging scanner findings by hand, that compression is the threat model that matters. What Does Mythos Actually Change About Exploitation? Mythos changes the economics of exploitation, not the taxonomy of vulnerabilities. The conversation around Mythos has focused on how AI can find vulnerabilities and generate exploits faster than it has ever been done before. The practical consequence is that vulnerability discovery now operates at scale. The underlying weaknesses aren’t changing. Most organizations are already exposed through identity weaknesses, overly permissive access, misconfigurations, and gaps in security controls. Mythos accelerates the path to those exposures, but it doesn’t create them. Vulnerability scanners produce a list of findings. Mythos-era attackers produce a verified exploit chain. Why Does the Discovery-to-Exploitation Gap Matter for Risk Prioritization? The discovery-to-exploitation gap matters because risk is not defined by a single vulnerability in isolation; it’s defined by impact. When that gap collapses, the window for remediation shrinks. Vulnerabilities can be identified faster, exploits generated faster, and weaknesses chained together more efficiently. That puts direct pressure on how security teams prioritize. The volume trend compounds the problem. Total vulnerabilities are up. Exploitable vulnerabilities are up. A team triaging by CVSS score alone will spend time on findings that cannot be reached in their environment while a chained attack path through an identity misconfiguration goes unaddressed. Exploitability means prioritization. Everything else is noise. The question boards are now asking — what do we do about Mythos? — has a direct answer: reduce that noise through the lens of exploitability. Vulnerability counts measure exposure. Exploitable attack paths measure real risk. How Are Attackers Operationalizing AI-Accelerated Techniques? AI-accelerated offensive operations are already moving beyond single-vulnerability exploitation. The shift in attacker behavior mirrors what Mythos demonstrates: the ability to move from a hypothesis about a weakness to a working exploit with reduced effort. When that capability is applied to real infrastructure, the result is disruption at the domain level. A compromised domain controller isn’t a scanner finding; it’s real business impact. What Does the Mythos Threat Model Mean for Security Teams Right Now? The Mythos threat model reframes the central security question. The challenge goes from identifying vulnerabilities to determining which ones can actually be exploited, how they chain into attack paths, and what the downstream impacts are. That reframe has direct consequences for every team running a vulnerability management program. Single vulnerabilities or chained vulnerabilities only matter if they’re tested in a specific environment. Where a scanner result is only a hypothesis, an autonomous pentest is confirmation. NodeZero operates from the attacker’s perspective, validating exploitability in the actual environment rather than scoring theoretical severity. Boards ask, “Are we exposed to this?” when a new technique or Known Exploited Vulnerability (KEV) surfaces, but the answer needs to be grounded in their specific environment as opposed to a vendor advisory. NodeZero does exactly this — by using real attacker TTPs safely in production, validating exploitability and understanding real attac
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: AI-Accelerated Exploitation: The Mythos-Era Threat Model
  - Published: 2026-06-13T08:00:03+00:00
  - Link: https://horizon3.ai/intelligence/blogs/ai-accelerated-exploitation-mythos-era-threat-model/
  - Summary: AI models like Mythos collapse the gap between discovery and exploitation. Learn how to rethink your threat model before attackers do.

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

### Cluster 81b6680cce — score 10

- Title: FishMonger’s arsenal upgraded: SprySOCKS for Windows
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-06-16T08:54:04+00:00
- Link: https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: education, government
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: government, education
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
ESET researchers have discovered SprySOCKS for Windows, FishMonger’s backdoor weaponizing a kernel driver for advanced stealthiness
```

#### Full body

```
ESET Research FishMonger’s arsenal upgraded: SprySOCKS for Windows ESET researchers have discovered SprySOCKS for Windows, FishMonger’s backdoor weaponizing a kernel driver for advanced stealthiness ESET Research 16 Jun 2026 • , 30 min. read ESET researchers have discovered two as-yet undocumented Windows variants of SprySOCKS , a previously Linux-only backdoor reportedly used by FishMonger, the group believed to be operated by a Chinese contractor named I‑SOON. While we initially discovered the malware samples on VirusTotal, ESET telemetry shows real activity between 2023 and 2024, with several victims in Honduras, Taiwan, Thailand, and Pakistan, targeting mostly government organizations. The Windows variants discovered are internally marked as WIN_DRV and WIN_PLUS . Both come with a hardcoded C&C configuration and support communication over TCP, UDP, and WebSocket protocols. The core backdoor functionality for both includes support for over 30 C&C commands, covering various functionalities including system information collection, process enumeration, as well as service management and file management functions such as listing, creating, deleting, and transferring files. In addition to the core backdoor functionality, the WIN_DRV version utilizes kernel drivers to hide the malware’s network connections, processes, files, and registry keys, and enables TCP traffic diversion allowing the malware operators to send commands to the backdoor through a random TCP port on the victim’s device without exposing the backdoor's real listening port in the network traffic. Based on ESET telemetry, there are limited indications that some SprySOCKS attack scenarios may involve a UEFI bootkit component, possibly exploiting CVE‑2023‑24932. The analysis provided in this report leads us to attribute these new, Windows variants to FishMonger with high confidence. Key points of this blogpost: We discovered two previously undocumented Windows variants of FishMonger’s SprySOCKS backdoor. ESET telemetry shows activity between 2023 and 2024, primarily targeting government organizations in Honduras, Taiwan, Thailand, and Pakistan. Both Windows variants support communication over TCP, UDP, and WebSocket protocols, and implement over 30 commands. The WIN_DRV variant creates a stealthy passive TCP backdoor, relying on a kernel driver to redirect traffic to the backdoor’s hidden TCP port whenever specially crafted data is detected inside a received TCP packet. FishMonger profile FishMonger – believed to be operated by a Chinese contractor named I‑SOON (see our Q4 2023–Q1 2024 APT Activity Report ) – is a cyberespionage group that falls under the Winnti Group umbrella and is most likely operating out of China, from the city of Chengdu. It is also known as Earth Lusca, TAG-22, Aquatic Panda, or Red Dev 10. We published an analysis of FishMonger in early 2020 when it heavily targeted universities in Hong Kong during the civic protests that started in June 2019. The group is also known to operate watering-hole attacks, as reported by Trend Micro . FishMonger’s toolset includes ShadowPad, Spyder, Cobalt Strike, FunnySwitch, SprySOCKS, and the BIOPASS RAT. Technical analysis In this section, we provide a technical analysis of these new, Windows variants of FishMonger’s SprySOCKS backdoor. The archive that led us to this discovery was uploaded to VirusTotal in April 2024 under the name klelam00007.zip ; its contents are shown in Figure 1. Figure 1. Contents of klelam00007.zip as displayed on VirusTotal This archive contains various files, including legitimate ones used to host DLL side-loading, and three suspicious-looking, encrypted files with .dat extensions. Our subsequent analysis revealed that these encrypted files contain a new, previously undocumented Windows variant of FishMonger’s SprySOCKS backdoor, labeled WIN_DRV by its developers. Further investigation revealed an additional backdoor version, labeled WIN_PLUS , in ESET Telemetry. Initial access FishMon
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: FishMonger’s arsenal upgraded: SprySOCKS for Windows
  - Published: 2026-06-16T08:54:04+00:00
  - Link: https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/
  - Summary: ESET researchers have discovered SprySOCKS for Windows, FishMonger’s backdoor weaponizing a kernel driver for advanced stealthiness

### Cluster 24585c22c2 — score 10

- Title: EvilTokens: A phishing attack that doesn’t steal your password
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-06-15T08:55:00+00:00
- Link: https://www.welivesecurity.com/en/cybercrime/eviltokens-phishing-doesnt-steal-password/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- affected_products: Microsoft 365, Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services
- affected_products: Microsoft 365, Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
A phishing kit subverting Microsoft’s legitimate authentication flow lets attackers break into accounts without stealing passwords or creating fake login pages
```

#### Full body

```
Cybercrime EvilTokens: A phishing attack that doesn’t steal your password A phishing kit subverting Microsoft’s legitimate authentication flow lets attackers break into accounts without stealing passwords or creating fake login pages Christian Ali Bravo 15 Jun 2026 • , 5 min. read Much has been written about how the days of phishing emails laden with broken grammar and crude design are numbered, largely thanks to AI. Meanwhile, EvilTokens offers a somewhat different example of how far the phishing craft has moved. EvilTokens is a phishing-as-a-service (PhaaS) kit built to compromise Microsoft 365 accounts by abusing the OAuth 2.0 device authorization grant flow . As attacks that use the kit rely on device code phishing, they sidestep the need for convincing replicas of genuine login pages where the victims would hand over their passwords. Instead, attackers get the victim to complete a legitimate authentication process – including two-factor authentication (2FA) – on a real Microsoft login page. The toolkit has been advertised via Telegram channels and spotted in active attacks since at least February 2026. As documented by Sekoia and others, the kit appears to have been quickly adopted by cybercriminals and deployed in a number of account takeover and business email compromise (BEC) attacks, including for a campaign targeting more than 340 organizations in several countries in March 2026. Microsoft itself has also described an AI-enabled campaign that used dynamic device-code generation and bespoke lures to increase the success rate of EvilTokens attacks. The inner workings of EvilTokens Here’s a brief overview of how attacks leveraging EvilTokens unfold: The attack itself is preceded by ‘reconnaissance’ where the ne’er-do-wells first verify that the target account is active. Microsoft has seen this reconnaissance run 10 to 15 days ahead of the actual phishing attempt. The victim receives an email or message that’s often dressed up as an invoice, shared document, calendar invite, or SharePoint access request. The lure involves a decoy page impersonating a trusted brand or service, along with simple wording such as “Verify to view” or “Signature required.” When the victim clicks through, the page requests a device code from Microsoft. The code is valid only for 15 minutes, hence time and timing are of the essence here. The page shows the victim the code along and points them to Microsoft’s genuine microsoft.com/devicelogin login portal. The catch is that the code belongs to the attacker’s session, hence the victim unknowingly authorizes the attacker’s device, not their own. Seeing a valid sign-in, Microsoft issues access and refresh tokens to the session opened by the attacker. Once inside, the criminals can access corporate email, files, Teams, SharePoint, OneDrive, and other Microsoft 365 resources and exfiltrate data or prepare BEC attacks, which is why finance, HR, logistics, and sales accounts draw much of the attackers’ interest. What makes EvilTokens dangerous The OAuth device code flow was designed for devices that may be awkward to sign into directly, such as smart TVs or printers. The device displays a short code that the user enters on a Microsoft page on another device, often a smartphone, and completes authentication there. Microsoft then issues access tokens to the device that requested access. That separation is useful, but it leaves room for abuse. Attackers can generate the code and dupe the victim into entering it – all while Microsoft only sees a valid authentication flow. The company does warn users at the moment of sign-in via on-screen text telling them not to enter codes from sources that they don’t trust. However, a convincing decoy is sometimes enough to get the victim to read past any warnings. Speaking of which, EvilTokens strips out many of the red flags that people have been taught to notice over the years, including misspelled domain names and fake login pages. The login page is real and, from the
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: EvilTokens: A phishing attack that doesn’t steal your password
  - Published: 2026-06-15T08:55:00+00:00
  - Link: https://www.welivesecurity.com/en/cybercrime/eviltokens-phishing-doesnt-steal-password/
  - Summary: A phishing kit subverting Microsoft’s legitimate authentication flow lets attackers break into accounts without stealing passwords or creating fake login pages

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

### Cluster 5af9a64c84 — score 10

- Title: Beyond the Score: Using AI to Translate CVEs into Real-World Business Risk
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-15T14:44:28+00:00
- Link: https://www.rapid7.com/blog/post/ai-beyond-the-score-translating-cves-into-real-business-risk
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: legal_professional
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: legal_professional
- urgency_signals: critical_cvss
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Security leaders rarely struggle to gather data, but they often struggle to turn that data into something clear and meaningful for the business. In a typical week, a CISO might receive a report listing hundreds or even thousands of vulnerabilities, most of them accompanied by CVSS scores that make the entire list look urgent, while also managing the wider set of operational, regulatory, and strategic demands that already come with the role. That difficulty becomes more obvious when the same information has to be carried into the boardroom, where the questions are rarely about CVE IDs or exploit counts in isolation. What leadership wants to understand is whether the organization’s revenue, uptime, legal exposure, or broader resilience could be affected, and how quickly those risks need to be addressed. This is where many security programs lose momentum, because the technical view of severity does not always line up neatly with the business view of consequence. Bridging that gap has trad
```

#### Full body

```
Back to Blog Artificial Intelligence Beyond the Score: Using AI to Translate CVEs into Real-World Business Risk Rapid7 Jun 15, 2026 | Last updated on Jun 15, 2026 | 7 min read DISCOVER RAPID7 MDR Security leaders rarely struggle to gather data, but they often struggle to turn that data into something clear and meaningful for the business. In a typical week, a CISO might receive a report listing hundreds or even thousands of vulnerabilities, most of them accompanied by CVSS scores that make the entire list look urgent, while also managing the wider set of operational, regulatory, and strategic demands that already come with the role. That difficulty becomes more obvious when the same information has to be carried into the boardroom, where the questions are rarely about CVE IDs or exploit counts in isolation. What leadership wants to understand is whether the organization’s revenue, uptime, legal exposure, or broader resilience could be affected, and how quickly those risks need to be addressed. This is where many security programs lose momentum, because the technical view of severity does not always line up neatly with the business view of consequence. Bridging that gap has traditionally been slow, manual work, which is one reason AI is starting to matter more in vulnerability management: it can help translate technical findings into business context that is clearer, faster to act on, and easier for leadership to understand. Why CVSS alone does not reflect real-world business risk For years, the industry has relied on CVSS as a quick way to judge urgency, and while the framework does account for factors such as attack vector, attack complexity, and other attack requirements, the score is still calculated in isolation and often misses the conditions that shape real risk inside an organization. A CVSS 9.8 vulnerability affecting a legacy printer in a segmented branch office may look critical on paper, but it is unlikely to carry the same business impact as a 7.5 vulnerability affecting an internet-facing database that holds sensitive customer data. One of the long-standing weaknesses of static scoring is that it tells you how severe a flaw may be in theory, but not how much disruption it could cause in your own environment, how exposed the affected asset is, or how closely it is tied to a revenue-generating or business-critical process. That is where AI becomes more useful, because it can add the missing context that helps security teams judge not just how serious a vulnerability looks, but how much it matters in practice. Machine learning models can now process a much broader set of inputs, including attacker activity, exploit availability, internal network topology, and the business value attached to the asset or process involved. Rather than leaving teams with a static queue of scores, that creates a live view of risk shaped by reachability, exposure, and business consequence, making it easier to separate technical severity from actual organizational risk. How AI helps connect vulnerabilities to business impact One of the more practical ways AI can improve vulnerability management is by helping security teams connect technical findings to the parts of the business they actually affect. A vulnerability tied to an obscure IP address may not mean much on its own, but the picture changes quickly when that asset is identified as part of a regional payment system, a customer-facing portal, or a supply chain application the business depends on. That kind of asset attribution has traditionally taken time, context, and manual investigation. AI can help shorten that process by linking technical findings to business function much more quickly. Instead of relying only on severity scores or yesterday’s alerts, AI can weigh a broader set of signals, including exploit activity, attacker behavior, asset exposure, and internal topology, which gives security teams a more grounded way to judge where risk is most likely to become operationally si
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Beyond the Score: Using AI to Translate CVEs into Real-World Business Risk
  - Published: 2026-06-15T14:44:28+00:00
  - Link: https://www.rapid7.com/blog/post/ai-beyond-the-score-translating-cves-into-real-business-risk
  - Summary: Security leaders rarely struggle to gather data, but they often struggle to turn that data into something clear and meaningful for the business. In a typical week, a CISO might receive a report listing hundreds or even thousands of vulnerabilities, most of them accompanied by CVSS scores that make the entire list look urgent, while also managing the wider set of operational, regulatory, and strategic demands that already come with the role. That difficulty becomes more obvious when the same information has to be carried into the boardroom, where the questions are rarely about CVE IDs or exploit counts in isolation. What leadership wants to understand is whether the organization’s revenue, uptime, legal exposure, or broader resilience could be affected, and how quickly those risks need to be addressed. This is where many security programs lose momentum, because the technical view of severity does not always line up neatly with the business view of consequence. Bridging that gap has trad

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

### Cluster d8706917f4 — score 10

- Title: Texas govt data breach exposes over 3 million driver’s licenses
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-19T16:12:41+00:00
- Link: https://www.bleepingcomputer.com/news/security/texas-govt-data-breach-exposes-over-3-million-drivers-licenses/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng
- affected_industries: financial_services, government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, data_breach
- affected_industries: financial_services, government
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The Texas Parks and Wildlife Department (TPWD) disclosed a data breach at its license system vendor that exposed personal information for more than three million individuals. [...]
```

#### Full body

```
Texas govt data breach exposes over 3 million driver’s licenses By Bill Toulas June 19, 2026 12:12 PM 0 The Texas Parks and Wildlife Department (TPWD) disclosed a data breach at its license system vendor that exposed personal information for more than three million individuals. The Texas Cyber Command discovered the intrusion and launched an investigation to determine the extent and impact of the unauthorized access. The state authority found that Social Security Numbers (SSNs), dates of birth, or any financial information, such as credit cards, have not been impacted. However, the threat actor may have obtained personally identifiable information that includes the following data types associated with 3,087,721 Texas hunting and fishing license customers: Driver’s license information Passport numbers Email addresses Phone numbers Residential addresses The exposed data set is sufficient for hackers to target impacted individuals in phishing and social engineering attacks that lead to web pages distributing malware or seeking more sensitive information. "There is no evidence that customers under the age of 18 were involved or that any specific group was targeted," TPWD says in the data breach notification . TPWD is the Texas state agency responsible for managing wildlife and fisheries, state parks, conservation programs, hunting and fishing regulations, boating registration, and enforcement by Texas Game Wardens. The Texas state agency also issues hunting and fishing licenses and permits, which are sold through an external vendor. BleepingComputer contacted TPWD for more information about the incident and the name of the third-party service provider, but we have not yet received a statement. The agency says that it is "working closely with the license system vendor to implement new safeguards and enhanced monitoring services." TPWD advises customers to monitor their credit reports and financial statements. Impacted individuals are eligible for one year of free credit monitoring and should consider placing a credit freeze or fraud alert with major credit bureaus as an added protection against identity thieves. It is also strongly recommended to remain vigilant for phishing and impersonation scams, as threat actors may try to send communication posing as a company or an official. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Nintendo confirms data stolen in WebMD subsidiary cyberattack SoFi confirms third-party data breach at Hong Kong subsidiary 15-year-old detained over French govt agency data breach French govt agency confirms breach as hacker offers to sell data Video service Vimeo confirms Anodot breach exposed user data
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Texas govt data breach exposes over 3 million driver’s licenses
  - Published: 2026-06-19T16:12:41+00:00
  - Link: https://www.bleepingcomputer.com/news/security/texas-govt-data-breach-exposes-over-3-million-drivers-licenses/
  - Summary: The Texas Parks and Wildlife Department (TPWD) disclosed a data breach at its license system vendor that exposed personal information for more than three million individuals. [...]

### Cluster 39e22586b8 — score 10

- Title: Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-15T06:17:32+00:00
- Link: https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-0257, Palo Alto Networks

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, phishing_social_eng, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, Palo Alto Networks, Ubiquiti UniFi
- cve_ids: CVE-2026-0257, CVE-2026-11645
- urgency_signals: actively_exploited, poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, zero_day, active_exploitation
- affected_industries: government
- affected_products: Palo Alto Networks, Anthropic/Claude, Ubiquiti UniFi
- cve_ids: CVE-2026-0257, CVE-2026-11645
- urgency_signals: actively_exploited, zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Palo Alto Networks has revealed that it has observed "active exploitation" of a recently disclosed PAN-OS vulnerability by an unknown threat actor to obtain unauthorized access to GlobalProtect portals. The vulnerability in question is CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway components of PAN-OS software that could be exploited by bad
```

#### Full body

```
Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw  Ravie Lakshmanan  Jun 15, 2026 Vulnerability / VPN Security Palo Alto Networks has revealed that it has observed "active exploitation" of a recently disclosed PAN-OS vulnerability by an unknown threat actor to obtain unauthorized access to GlobalProtect portals. The vulnerability in question is CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway components of PAN-OS software that could be exploited by bad actors to set up VPN connections. According to the network security company, the security defect could be exploited by a bad actor to bypass security controls and initiate VPN connections. The vulnerability has been exploited in the wild in limited attacks, with initial activity observed on May 17, 2026. It's currently unknown who is behind the exploitation efforts. "No post-access behavior or lateral movement has been identified as of this time," Palo Alto Networks said . "Only a small portion of the probed devices actually established VPN sessions, resulting in gateway-connected events." The company has also released indicators of compromise (IoCs) associated with the activity - IP addresses - 23.128.228[.]6 104.207.144[.]154 146.19.216[.]119 146.19.216[.]120 146.19.216[.]125 179.43.172[.]213 185.195.232[.]139 198.12.106[.]60 202.144.192[.]47 Host Names and MAC Addresses - aa:bb:cc:dd:ee:ff 00:11:22:33:44:55 WINDOWS-LAPTOP-001 DESKTOP-GP01 GP-CLIENT Palo Alto Networks is also urging customers to search GlobalProtect logs for successful gateway-connected events that match the following hard-coded client configuration values from a proof-of-concept (PoC) exploit - endpoint_os_version : Microsoft Windows 10 Pro 64-bit source_user_info.domain : empty Late last month, the U.S. Cybersecurity and Infrastructure Security Agency (CSIA) added CVE-2026-0257 to its Known Exploited Vulnerabilities (KEV) catalog, ordering Federal Civilian Executive Branch (FCEB) agencies to mitigate the flaw by June 1, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Authentication bypass , CISA , cybersecurity , GlobalProtect , network security , Palo Alto Networks , PAN-OS , VPN Security , Vulnerability ⚡ Top Stories This Week Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities Cybersecurity Stars Awards 2026: Winners Announced Across 95 Categories ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories New GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files Agentjacking Attack Tricks AI Coding Agents Into Running Malicious Code China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade Critical Splunk Enterprise Flaw Lets Attackers Run Code Without Authentication U.S. Orders Anthropic to Suspend Fable 5 and Mythos 5 Access for Foreign Nationals Over 400 Arch Linux AUR Packages Hijacked to Deploy Infostealer and eBPF Rootkit Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw ⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More ⭐ Featured Resources Get the 2026 Guide to Govern and Secure Enterprise AI Agents at Scale [Watch Demo] See Which Security Gaps Attackers Could Exploit First AI Can’t Stop Every Attack. Learn How Zero Trust Can Block What’s Unknown Have You Outgrown Your MDR? 7 Warning Signs Every CISO Should Check
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw
  - Published: 2026-06-15T06:17:32+00:00
  - Link: https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html
  - Summary: Palo Alto Networks has revealed that it has observed "active exploitation" of a recently disclosed PAN-OS vulnerability by an unknown threat actor to obtain unauthorized access to GlobalProtect portals. The vulnerability in question is CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway components of PAN-OS software that could be exploited by bad

### Cluster 29fcf4633f — score 10

- Title: LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-15T16:39:01+00:00
- Link: https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-40217, CVE-2026-47101, CVE-2026-47102
- urgency_signals: critical_cvss
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: ai_security
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-47101, CVE-2026-47102, CVE-2026-40217
- urgency_signals: critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
A default low-privilege account on a LiteLLM proxy can climb to full admin and run code on the server by chaining three vulnerabilities, researchers at Obsidian Security disclosed LiteLLM is a widely deployed open-source AI gateway that brokers calls to more than 100 model providers behind one OpenAI-compatible interface. A server takeover exposes every provider key it holds, the secrets that
```

#### Full body

```
LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers  Swati Khandelwal  Jun 15, 2026 Artificial Intelligence / Vulnerability A default low-privilege account on a LiteLLM proxy can climb to full admin and run code on the server by chaining three vulnerabilities, researchers at Obsidian Security disclosed LiteLLM is a widely deployed open-source AI gateway that brokers calls to more than 100 model providers behind one OpenAI-compatible interface. A server takeover exposes every provider key it holds, the secrets that decrypt its stored credentials, and every prompt and response passing through it. Obsidian rates the full chain CVSS 9.9, in the Critical range. BerriAI , the maintainer, included the complete fix set in LiteLLM v1.83.14-stable, which GitHub lists as released May 2. Upgrade to that release or later to close the three-CVE chain. The three bugs The first link is CVE-2026-47101 , an authorization bypass. When a regular user (an internal_user) generates a virtual API key, LiteLLM stores the caller-supplied allowed_routes field without checking it against the user's role. The field is supposed to narrow what a key can do. Instead, the proxy also treats it as a fallback grant, so a non-admin can mint a key with allowed_routes: ["/*"], a wildcard that reaches every route, including admin-only ones. The same unchecked write shows up on the other key-management endpoints, which is why the fix took three pull requests to land. With the route gate bypassed, the handlers behind it become reachable. Several of them assume the gate has already done the screening, which opens two paths. One is CVE-2026-47102 , privilege escalation. The /user/update endpoint lets a user edit their own record, but does not restrict which fields they can write. A self-update with user_role: "proxy_admin" is accepted and saved, promoting the caller to full proxy admin. An org_admin can hit this endpoint through a legitimate, intended code path with no bypass required; a default internal_user reaches it after CVE-2026-47101. VulnCheck, which assigned the CVE, scores it 8.7 under CVSS 4.0, 8.8 under 3.1. The other is CVE-2026-40217 , a sandbox escape in the Custom Code Guardrail, which compiles and runs admin-supplied Python. The production endpoints ran the code through exec() with no source-level filtering. When exec() gets a globals dict without __builtins__, Python silently injects the full builtins module, which hands the code __import__, open, and eval. A plain payload calling os.system was then enough for a reverse shell. A separate path on the /guardrails/test_custom_code playground endpoint, found independently by X41 D-Sec , defeated a regex deny-list through runtime bytecode rewriting. Both ended in server-side code execution. What an attacker gets LiteLLM sits at a chokepoint, so the reach is wide. A full chain exposes the master key, the salt key that decrypts stored credentials, and the database URL. It also exposes every configured provider key, for OpenAI, Anthropic, Gemini, Bedrock, Azure, and the rest. Keys in config or environment are plaintext; keys in the database are encrypted but recoverable with the salt key. Everything sent through the gateway, prompts and responses, becomes readable, which in real deployments is where PII, source code, internal tickets, and pasted secrets end up. If the proxy also runs as a Model Context Protocol (MCP) or agent gateway, OAuth tokens and tool credentials are in scope too. The sharper risk is not what an attacker reads but what they can rewrite. The gateway sits on the wire between an AI agent and the model, so a compromise lets it alter responses in transit. Obsidian demonstrated this against Claude Code routed through a compromised proxy. This is not prompt injection . Instead of persuading the model to misbehave, the attacker uses LiteLLM's built-in callback mechanism, an extension point that fires on every request and never shows up in the admin UI. The callback
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers
  - Published: 2026-06-15T16:39:01+00:00
  - Link: https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html
  - Summary: A default low-privilege account on a LiteLLM proxy can climb to full admin and run code on the server by chaining three vulnerabilities, researchers at Obsidian Security disclosed LiteLLM is a widely deployed open-source AI gateway that brokers calls to more than 100 model providers behind one OpenAI-compatible interface. A server takeover exposes every provider key it holds, the secrets that
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: PromptSnatcher: AdBlocker stealing Ai Chats - 90k installs
  - Published: 2026-06-13T22:11:13+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u53o6l/promptsnatcher_adblocker_stealing_ai_chats_90k/
  - Summary: Two Chrome extensions presenting as adblockers also intercept every prompt and response on ChatGPT, Claude, Gemini, Copilot, Grok, Perplexity, DeepSeek, and Meta AI, exfiltrating them to operator-controlled servers. They also check whether you're a paid user on 5 of the 8 platforms (ChatGPT, Claude, Perplexity, Copilot, Gemini). Both share the same capture engine, payload format, and partnerId. Two brands, one operation . Smart Adblocker - Chrome Web Store ` iojpcjjdfhlcbgjnpngcmaojmlokmeii `, 80k users Adblock for Browser - Chrome Web Store ` jcbjcocinigpbgfpnhlpagidbmlngnnn `, 10k users Report covers the IOCs, live remote config, reproduction curl, and full target breakdown. Full write-up: MalExt Sentry - Malicious Browser Extension Tracker Chrome Web Store abuse reports filed. submitted by /u/Huge-Skirt-6990 [link] [comments]

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

### Cluster 41719728a2 — score 9

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

### Cluster 5dd3ebabf9 — score 9

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

### Cluster f99fcc5f45 — score 9

- Title: NIS2 is raising the bar. Here’s how to turn readiness into resilience.
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-06-15T17:29:15+00:00
- Link: https://www.rapid7.com/blog/post/so-nis2-compliance-turn-readiness-into-resilience
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
The NIS2 directive asks covered organizations to take a more structured approach to risk management, governance, supply chain security, and incident reporting. It expands the scope of who may be covered, raises expectations around management body accountability, introduces clearer and more enforceable requirements, and increases pressure on organizations to show that security is being managed in a consistent, defensible way. Reporting timelines are one of the most visible parts of that shift, with early warning required within 24 hours of awareness for significant incidents, incident notification within 72 hours, and a final report within one month. It also arrived in a landscape that is still uneven, with member states continuing to implement the directive in different ways across the EU. That combination has created a familiar challenge for CISOs and security teams, as the questions coming from boards and leadership are no longer just about whether the organization understands the re
```

#### Full body

```
Back to Blog Security Operations NIS2 is raising the bar. Here’s how to turn readiness into resilience. Sabeen Malik Jun 15, 2026 | Last updated on Jun 15, 2026 | 4 min read DISCOVER RAPID7 MDR The NIS2 directive asks covered organizations to take a more structured approach to risk management, governance, supply chain security, and incident reporting. It expands the scope of who may be covered, raises expectations around management body accountability, introduces clearer and more enforceable requirements, and increases pressure on organizations to show that security is being managed in a consistent, defensible way. Reporting timelines are one of the most visible parts of that shift, with early warning required within 24 hours of awareness for significant incidents, incident notification within 72 hours, and a final report within one month. It also arrived in a landscape that is still uneven, with member states continuing to implement the directive in different ways across the EU. That combination has created a familiar challenge for CISOs and security teams, as the questions coming from boards and leadership are no longer just about whether the organization understands the regulation, but whether it can meet the requirements in practice. NIS2 reaches into risk management, reporting, governance, and supply chain oversight, which means readiness depends on how well security works across the business, not just on how well a policy is written. That is why the most useful way to think about NIS2 is as an operational resilience exercise. Compliance still matters, of course, and teams need to know what the directive requires. What tends to make the difference over time is whether security leaders can connect those requirements to the real conditions of the environment: what is exposed, where ownership sits, how incident response works in practice, how supply chain risk is monitored, and how quickly the organization can move when something material happens. Regulations are easier to absorb than operating model changes. A team may understand that NIS2 raises expectations around governance and incident handling, while still finding it difficult to answer basic questions quickly when pressure rises. Which business services are most critical? Which third parties matter most? Who owns the decision when a serious issue lands? How prepared are we to investigate, communicate, and report inside the timelines the directive expects? Those are the questions that separate a compliance project from a resilience program. That is also why we have been building practical content to help teams move from interpretation to action. Our ebook is the best place to start if you want the wider context. It is designed to help security leaders understand what NIS2 means in practical terms, how to think about the directive beyond a narrow checklist, and how to connect compliance obligations to a broader resilience strategy. If your team needs a stronger narrative for internal stakeholders, or a clearer way to explain why NIS2 should influence operational priorities, the ebook is the most useful first read. Next, our NIS2 Readiness Toolkit is built for teams that want to assess where they are and what to do next. iIt is as a way to bridge the gap between NIS2 requirements and operational reality, with a focus on risk, reporting, and governance. It is designed to help teams spot gaps, focus effort, and simplify the path from regulatory complexity to a more defensible security strategy. In other words, it gives you a practical framework for understanding where readiness is strong, where it is uneven, and what deserves attention first. Our infographic, seen below, is the quickest asset to use when you need to communicate one of the most tangible parts of NIS2: the 24-hour reporting requirement. Some stakeholders need the long-form explanation. Others need a practical view of what has to happen between incident awareness and early notification. The infographic helps
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: NIS2 is raising the bar. Here’s how to turn readiness into resilience.
  - Published: 2026-06-15T17:29:15+00:00
  - Link: https://www.rapid7.com/blog/post/so-nis2-compliance-turn-readiness-into-resilience
  - Summary: The NIS2 directive asks covered organizations to take a more structured approach to risk management, governance, supply chain security, and incident reporting. It expands the scope of who may be covered, raises expectations around management body accountability, introduces clearer and more enforceable requirements, and increases pressure on organizations to show that security is being managed in a consistent, defensible way. Reporting timelines are one of the most visible parts of that shift, with early warning required within 24 hours of awareness for significant incidents, incident notification within 72 hours, and a final report within one month. It also arrived in a landscape that is still uneven, with member states continuing to implement the directive in different ways across the EU. That combination has created a familiar challenge for CISOs and security teams, as the questions coming from boards and leadership are no longer just about whether the organization understands the re

### Cluster f5a9f96db5 — score 9

- Title: What Is Container Runtime Security? A Practical Guide 2026
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-06-19T18:50:00+00:00
- Link: https://orca.security/resources/blog/what-is-container-runtime-security/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Kubernetes

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, supply_chain
- affected_products: Kubernetes
- attack_techniques: T1552, T1610, T1611
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft
- affected_products: Kubernetes
- attack_techniques: T1552, T1610, T1611
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Key takeaways Container runtime security is the practice of detecting and limiting attacks against containerized workloads while they run. Runtime controls monitor process activity, file access, and network connections, then enforce policies when workloads deviate from expected behavior. In Kubernetes environments, runtime security also depends on controls such as admission policies, network segmentation, and API […]
```

#### Full body

```
Table of contents Key takeaways What Is Container Runtime Security Most Prevalent Threats at Runtime Who Is Responsible for Runtime Security Developers’ Role Runtime Security and Kubernetes Security Policies and Best Practices How to Discover Runtime Risks in Your Environment Runtime Signal Types and Their Purpose Continuous Real-Time Scanning Snapshot Scanning Behavioral Analytics Unifying Container Security From Code to Runtime Frequently asked questions about Container Runtime Security Key takeaways Container runtime security protects workloads while they execute, after deployment. Common runtime threats include privilege abuse, container escape, lateral movement, and malicious process activity. Responsibility spans developers, platform teams, and security operations, especially in Kubernetes environments. Runtime security combines telemetry, behavioral analysis, snapshots, and contextual risk signals to detect active threats. Container runtime security is the practice of detecting and limiting attacks against containerized workloads while they run. Runtime controls monitor process activity, file access, and network connections, then enforce policies when workloads deviate from expected behavior. In Kubernetes environments, runtime security also depends on controls such as admission policies, network segmentation, and API server security. It helps detect attacks that build-time scanning cannot predict, including in-memory techniques, credential abuse, and novel malware. Container security and container security best practices cover broader topics such as image security, supply-chain risk, cluster hardening, and deployment controls. This guide focuses specifically on runtime behavior after workloads are deployed and running in production. What Is Container Runtime Security Container runtime security combines preventive controls with live detection to protect workloads while they run. Unlike static image scanning, which identifies known vulnerabilities in packages and images, runtime security focuses on how containers actually behave on hosts and within clusters. NIST SP 800-190 frames container risks across both the image lifecycle and the execution environment. Runtime controls address that execution layer through technologies such as syscall filtering, mandatory access control profiles, monitoring agents, and eBPF-based sensors. These controls observe behavior rather than relying solely on known signatures. They can detect activity that never maps to a published CVE, including living-off-the-land techniques and other forms of post-exploitation behavior inside a container. Most Prevalent Threats at Runtime Common runtime threats include: Container escape: Breaking isolation between a container and its host. Credential theft: Stealing cloud metadata credentials, service account tokens, or other secrets. Cryptomining: Hijacking compute resources for unauthorized mining activity. Reverse shells: Establishing remote command execution from compromised workloads. MITRE ATT&CK for Containers maps techniques such as T1610 (Deploy Container), T1611 (Escape to Host), and T1552 (Unsecured Credentials) to container and orchestrator contexts. The CISA Known Exploited Vulnerabilities catalog lists CVEs under active exploitation. When a workload mounts a sensitive host path or runs with excessive capabilities, those CVEs become reachable even if the base image passed a scan last week. Runtime tooling prioritizes signals that indicate live exploitation rather than latent patch debt. It also surfaces insider-style abuse where credentials are valid but behavior is wrong. Who Is Responsible for Runtime Security Runtime security is a shared obligation. Product teams own application behavior and dependency choices. Platform engineering owns node configuration, runtime classes, and cluster upgrades. Security operations owns detection content, incident response playbooks, and tuning to reduce false positives. No single role “finishes” runtime sec
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: What Is Container Runtime Security? A Practical Guide 2026
  - Published: 2026-06-19T18:50:00+00:00
  - Link: https://orca.security/resources/blog/what-is-container-runtime-security/
  - Summary: Key takeaways Container runtime security is the practice of detecting and limiting attacks against containerized workloads while they run. Runtime controls monitor process activity, file access, and network connections, then enforce policies when workloads deviate from expected behavior. In Kubernetes environments, runtime security also depends on controls such as admission policies, network segmentation, and API […]

### Cluster 5fb153b4fa — score 9

- Title: What Is Application Security Testing? Tools and Types
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-06-19T15:50:00+00:00
- Link: https://orca.security/resources/blog/what-is-application-security-testing/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Key takeaways Application security testing (AST) is how organizations identify security weaknesses before attackers can exploit them. It includes activities such as threat modeling and automated techniques like SAST, SCA, DAST, and IAST. AST belongs in the same program as shift-left security, while DevSecOps practices help route findings to the right owners for remediation. AST […]
```

#### Full body

```
Table of contents Key takeaways Why AST Matters: The Importance of Shift Left Security Threat Modeling Static Application Security Testing (SAST) Software Composition Analysis (SCA) Dynamic Application Security Testing (DAST) Interactive Application Security Testing (IAST) How Orca Security Fits Application Security Testing Programs Adding Cloud Context to AST Findings Operationalizing AST in Cloud Environments Application Security Testing Frequently Asked Questions Key takeaways Application security testing (AST) is the set of processes and tools used to find and fix security defects throughout the software development lifecycle. Common AST techniques include threat modeling, SAST, SCA, DAST, and IAST. Each identifies different classes of risk. Shift-left AST helps teams find issues earlier, when fixes are faster and less disruptive. Combining AST findings with cloud and runtime context helps teams prioritize the vulnerabilities that present real business risk. Application security testing (AST) is how organizations identify security weaknesses before attackers can exploit them. It includes activities such as threat modeling and automated techniques like SAST, SCA, DAST, and IAST. AST belongs in the same program as shift-left security , while DevSecOps practices help route findings to the right owners for remediation. AST is not a single tool. It is a program that combines testing, remediation workflows, and governance across the software development lifecycle. The goal is to reduce the chance that design flaws, vulnerable dependencies, or insecure defaults reach production. NIST SP 800-218 (Secure Software Development Framework) provides a widely used framework for integrating security into software delivery. Organizations do not need every control on day one, but they should define a clear scope covering languages, pipelines, environments, and risk owners. Why AST Matters: The Importance of Shift Left Security Fix issues earlier. Fixing a defect after release costs more than fixing it during design or code review. That is the core idea behind shift-left security: finding issues when developers still have context and remediation is straightforward. Security does not stop at deployment. Runtime abuse, supply-chain incidents, and cloud misconfigurations still emerge after release. Programs that only scan repositories can miss exposed admin interfaces, unsafe cloud defaults, and risks introduced during deployment. Pair AST with application security governance so scope covers APIs, batch jobs, and integrations, not only user-facing web apps. Modern APIs also expand the attack surface, making API security testing an important part of AST. Support secure software delivery. Supply-chain incidents highlight the importance of composition analysis and software integrity. AST programs that include SCA and dependency governance are better equipped to identify risk when upstream packages change. OWASP maintains testing guidance that maps closely to AST programs. The Application Security Verification Standard helps teams translate security requirements into practical test cases for SAST, DAST, and manual review. Types of Application Security Testing AST types differ by what they analyze (source, binaries, running systems), when they run (build, test, prod), and what classes of bugs they target. Teams combine them because no single technique finds everything. The table below summarizes common differences. Your toolchain labels may vary by vendor. Technique Typical inputs Strengths Blind spots Threat modeling Architecture, data flows Finds design flaws early Depends on accurate diagrams SAST Source or bytecode Fast feedback in CI False positives; needs tuning SCA Manifests, lockfiles, images Supply-chain and license risk Transitive dependency noise DAST Running app URLs Realistic HTTP attack surface Auth and workflow coverage IAST Instrumented runtime + code paths Taint-style precision Operational cost and support Penetration testing and re
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: What Is Application Security Testing? Tools and Types
  - Published: 2026-06-19T15:50:00+00:00
  - Link: https://orca.security/resources/blog/what-is-application-security-testing/
  - Summary: Key takeaways Application security testing (AST) is how organizations identify security weaknesses before attackers can exploit them. It includes activities such as threat modeling and automated techniques like SAST, SCA, DAST, and IAST. AST belongs in the same program as shift-left security, while DevSecOps practices help route findings to the right owners for remediation. AST […]

### Cluster bebf48718b — score 9

- Title: What Is Managed Cloud Security? A Practical Guide
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-06-19T12:50:00+00:00
- Link: https://orca.security/resources/blog/what-is-managed-cloud-security/
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
Key Takeaways Managed cloud security is contracted operations work: a provider runs all or part of monitoring, triage, incident coordination, vulnerability workflows, compliance reporting, and sometimes architecture review using your cloud accounts and tools. You keep ownership of accounts, data, and policy. The vendor supplies staffing, runbooks, and integrations so alerts and posture gaps are […]
```

#### Full body

```
Table of contents Key Takeaways What Is Managed Cloud Security? Core Functions of Managed Cloud Security 24/7 Threat Detection and Response Vulnerability and Patch Management Compliance and Reporting Security Architecture Design and Hardening Toolchain Integration and Platform Coverage MDR vs. CNAPP vs. Managed Cloud Security Fully Managed vs. Co-Managed Security Models Who Should Use Which Model? Fully Managed Model Co-Managed Model Evaluating and Selecting a Managed Security Provider How Orca Security Supports Managed Cloud Security Frequently asked questions about Managed Cloud Security Key Takeaways Managed cloud security is an operating model where you contract a provider to run parts of cloud detection, response, posture management, and compliance workflows against your accounts and workloads. Core delivery patterns include 24/7 monitoring, vulnerability and patch coordination, compliance evidence collection, architecture hardening guidance, and integration with your existing CNAPP, CSPM, and DevSecOps toolchain. MDR, CNAPP, and managed cloud security solve different problems; the right stack often combines platform visibility with human-led operations where your risk and staffing gaps require it. Choosing a provider requires clear SLAs, transparency into how alerts are triaged, multi-cloud coverage that matches your estate, and honest limits on what outsourced teams can see without your IAM and logging foundations. Managed cloud security is contracted operations work: a provider runs all or part of monitoring, triage, incident coordination, vulnerability workflows, compliance reporting, and sometimes architecture review using your cloud accounts and tools. You keep ownership of accounts, data, and policy. The vendor supplies staffing, runbooks, and integrations so alerts and posture gaps are not limited to business hours. This guide explains the core functions of managed cloud security, compares MDR and CNAPP to managed services, contrasts fully managed and co-managed models, and outlines key evaluation criteria. Organizations often adopt the model when footprint, alert volume, or regulatory requirements outpace the team’s ability to maintain 24/7 coverage across AWS, Azure, GCP, and Kubernetes. What Is Managed Cloud Security? Managed cloud security is contracted security operations and posture work for public and hybrid cloud environments. The scope typically includes continuous monitoring of control-plane and workload signals, coordination with your identity and logging pipelines, and reporting aligned to frameworks such as CIS Benchmarks and NIST SP 800-53 controls. It is not a single product category. Rather, it is a service layer that sits on top of cloud security posture management (CSPM) , workload and vulnerability data, and often a cloud-native application protection platform (CNAPP) that unifies those views. Core Functions of Managed Cloud Security Core functions span detection and response, vulnerability and patch management, compliance and reporting, architecture and hardening guidance, and toolchain integration. Each function should have a written scope: which clouds, which log sources, which severity thresholds trigger human action, and which actions sit with the vendor versus your internal team. 24/7 Threat Detection and Response 24/7 threat detection and response means analysts and automation review alerts from your SIEM, CNAPP, CSPM, identity systems, and cloud provider APIs outside business hours. Effective programs map alerts to MITRE ATT&CK® tactics where possible, tune noisy rules with your change calendar, and document escalation paths to your incident commander. The CISA Known Exploited Vulnerabilities catalog lists CVEs under active exploitation; findings that overlap with KEV should rank high in prioritization. Vulnerability and Patch Management Vulnerability and patch management in this context is workflow coordination. Teams validate scanner output from agent-based or agentless security approa
```

#### Corroborating sources (1)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: What Is Managed Cloud Security? A Practical Guide
  - Published: 2026-06-19T12:50:00+00:00
  - Link: https://orca.security/resources/blog/what-is-managed-cloud-security/
  - Summary: Key Takeaways Managed cloud security is contracted operations work: a provider runs all or part of monitoring, triage, incident coordination, vulnerability workflows, compliance reporting, and sometimes architecture review using your cloud accounts and tools. You keep ownership of accounts, data, and policy. The vendor supplies staffing, runbooks, and integrations so alerts and posture gaps are […]

### Cluster 6bc465fddb — score 9

- Title: CISA warns Fortinet users to secure devices after FortiBleed leak
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-19T06:47:55+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- affected_products: Fortinet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, data_breach
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- affected_products: Fortinet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) urged Fortinet customers to secure their devices after nearly 74,000 firewall and VPN credentials were exposed in a data leak dubbed "FortiBleed." [...]
```

#### Full body

```
CISA warns Fortinet users to secure devices after FortiBleed leak By Sergiu Gatlan June 19, 2026 02:47 AM 0 The U.S. Cybersecurity and Infrastructure Security Agency (CISA) urged Fortinet customers to secure their devices after nearly 74,000 firewall and VPN credentials were exposed in a data leak dubbed "FortiBleed." This warning comes after threat actors used compromised credentials to target internet-accessible Fortinet devices across government and private-sector organizations worldwide. "CISA is aware of global reports that malicious cyber actors have targeted internet-accessible Fortinet devices across government and private sector organizations using compromised credentials," it said . "This activity, referred to as FortiBleed, involves the exposure of leaked credentials associated with approximately 74,000 Fortinet devices, including firewalls and virtual private network (VPN) gateways." The agency called on affected FortiGate appliance owners to terminate all SSL VPN and administrative sessions, reset all VPN and administrative passwords, enable phishing-resistant multifactor authentication, and review logs for signs of unauthorized access or lateral movement. CISA also advised Fortinet customers to store admin credentials using the modern Password-Based Key Derivation Function 2 (PBKDF2) hashing algorithm, and to restrict firewall management interfaces from public internet access and remove any unauthorized accounts to reduce the attack surface as much as possible. Credentials for over 73K firewalls exposed The FortiBleed data leak was uncovered by security researcher Volodymyr "Bob" Diachenko, who discovered a server containing what appeared to be valid Fortinet VPN credentials, including usernames, email addresses, and plaintext passwords for 73,932 firewall URLs worldwide. The exposed data also includes each organization's industry, revenue, and employee count, which Diachenko said appeared to be compiled to assist in planning future attacks. Threat intelligence company Hudson Rock, which also analyzed the dataset , described it as one of the largest known collections of compromised Fortinet credentials, spanning 21,632 unique domains and 194 countries. ​Among the organizations represented in the dataset are Samsung, Mercedes-Benz, Foxconn, Chevron, Comcast, AT&T, and Toyota, along with many government agencies and critical infrastructure operators across telecommunications, healthcare, financial services, and manufacturing industry sectors. The highest number of affected devices were from India, the United States, Taiwan, Mexico, Turkey, Thailand, Colombia, Malaysia, Chile, and the United Arab Emirates. Fortinet credentials found on an exposed server (Volodymyr Diachenko) Data leak linked to Russian-speaking threat group Diachenko also said the operation was conducted by a Russian-speaking threat group that allegedly carried out approximately 1.16 billion credential attempts against more than 320,000 FortiGate targets to intercept SSL VPN authentication hashes. The source of the configuration data remains unknown. Cybersecurity expert Kevin Beaumont has also independently confirmed the authenticity of some credentials and noted that most affected devices remain online. "The data is legit. It is around 75k devices. Almost all are still online, and Fortinet devices. It appears to be recent data," Beaumont said , adding that the leaked data appears to have originated from Fortinet configuration files. However, the source of the data remains unknown, and it is unclear whether it was stolen through exploitation of previously disclosed Fortinet vulnerabilities, a newly discovered security flaw, or another method. Hudson Rock has also created a free FortiBleed lookup tool to help organizations check whether they are affected. On Monday, threat intelligence company Defused also reported that several critical vulnerabilities in Fortinet's FortiSandbox cyber threat detection platform are now exploited in attacks. In total,
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA warns Fortinet users to secure devices after FortiBleed leak
  - Published: 2026-06-19T06:47:55+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) urged Fortinet customers to secure their devices after nearly 74,000 firewall and VPN credentials were exposed in a data leak dubbed "FortiBleed." [...]

### Cluster c220c2d05e — score 9

- Title: CryptoBandits Malware Doubles as a Backdoor, Abuses Tor
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-06-19T11:19:41+00:00
- Link: https://www.securityweek.com/cryptobandits-malware-doubles-as-a-backdoor-abuses-tor/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, ransomware_extortion, supply_chain, web_shell_backdoor, zero_day
- affected_industries: financial_services
- affected_products: Fortinet, LiteSpeed, WordPress
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, credential_theft, zero_day, web_shell_backdoor
- affected_industries: financial_services
- affected_products: LiteSpeed, Fortinet, WordPress
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
CryptoBandits uses a local SOCKS5 proxy for traffic routing, blending data theft with remote code execution. The post CryptoBandits Malware Doubles as a Backdoor, Abuses Tor appeared first on SecurityWeek .
```

#### Full body

```
Microsoft warns of a Windows-based cryptocurrency clipper that establishes a lightweight backdoor blending data exfiltration and remote code execution (RCE) capabilities. Dubbed CryptoBandits , the malware has been used in attacks since February 2026, deploying a portable Tor client on the infected systems and routing traffic through a local SOCKS5 proxy. “The clipper in this campaign relies on Windows Script Host and ActiveX-driven logic to launch a bundled Tor proxy and poll a hidden-service C&C server. It carries out high-frequency clipboard theft, screenshot exfiltration, and wallet-address substitution,” Microsoft explains. CryptoBandits is distributed through malicious shortcut (.lnk) payloads. On the infected systems, it deploys two components: a worm for propagation and a clipper/stealer to steal cryptocurrency wallet information. For propagation, the malware scans connected USB devices and creates additional malicious shortcuts of legitimate files. It can also deliver file-based payloads that it excludes from Defender scanning. The clipper is a script that interacts with the system via WScript and ActiveXObject, and checks whether Task Manager is running as an anti-analysis defense. Persistence is achieved through scheduled tasks. Advertisement. Scroll to continue reading. CryptoBandits launches a renamed Tor binary to establish command-and-control (C&C) communication and register the victim device, and then enters a continuous loop, polling the C&C for instructions every 500 milliseconds. The malware can extract seed phrases and private keys associated with cryptocurrency wallets, and can replace cryptocurrency addresses in the clipboard with attacker-provided ones to hijack them. According to Microsoft, the malware employs multi-layered obfuscation, decrypting all components at runtime. Both the Python script that handles installation and its JavaScript payloads are also obfuscated. The central component of the threat is the bundled Tor client, which routes communication over localhost:9050 and resolves destination domains to reduce DNS visibility and hide its C&C location. “This malware family shows how lightweight, script-based stealers can deliver outsized impact when paired with anonymized communications and runtime tasking. Organizations should focus on hardening script execution paths, monitoring local SOCKS proxy abuse, and using behavioral hunting to connect script activity with network, clipboard, and process signals,” Microsoft notes. Related: Rokarolla Banking Trojan Targets 200 Applications Related: Microsoft Teams Relay Servers Abused in DragonForce Ransomware Attack Related: OnyxC2 Stealer Offers Cybercriminals Enterprise-Grade Theft for $250 a Month Related: Infostealers Turn Millions of Devices Into Credential Theft Machines Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Dream Raises $260 Million at $3 Billion Valuation Atlassian, Splunk Patch Critical Vulnerabilities Critical Command Execution Vulnerability Patched in Cisco ISE F5 Patches Critical, High-Severity NGINX Vulnerabilities Microsoft Teams Relay Servers Abused in DragonForce Ransomware Attack Microsoft Working on Patch for ‘RoguePlanet’ Zero-Day Chrome and Firefox Updated to Patch Critical, High-Severity Vulnerabilities Joomla, LiteSpeed Vulnerabilities Exploited in Attacks Latest News In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum FortiBleed: 86,000 Fortinet Device Credentials Compromised Cybersecurity Firms Impacted by Klue Supply Chain Attack Cisco to Acquire WideField Security to Boost Splunk’s Agentic SOC 15,000 WordPress Websites Cleaned Up in SocGholish Botnet Takedown Splunk Enterprise Vulnerability Exploited in Attacks Days After Disclosure Majority of Internet-Accessible
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: CryptoBandits Malware Doubles as a Backdoor, Abuses Tor
  - Published: 2026-06-19T11:19:41+00:00
  - Link: https://www.securityweek.com/cryptobandits-malware-doubles-as-a-backdoor-abuses-tor/
  - Summary: CryptoBandits uses a local SOCKS5 proxy for traffic routing, blending data theft with remote code execution. The post CryptoBandits Malware Doubles as a Backdoor, Abuses Tor appeared first on SecurityWeek .

### Cluster e95ce78b9a — score 9

- Title: Maine forced to take down data breach portal after fake notices filed with authorities
- Source: Graham Cluley (practitioner_analysis)
- Published: 2026-06-15T13:23:44+00:00
- Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/maine-take-down-data-breach-portal
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: data_breach
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
The US state of Maine has taken its public data breach notification portal offline after someone submitted fraudulent breach disclosures impersonating two well-known technology companies. Read more in my article on the Hot for Security blog.
```

#### Full body

```
Industry News Data Breach 2 min read Maine forced to take down data breach portal after fake notices filed with authorities Graham CLULEY June 15, 2026 The US state of Maine has taken its public data breach notification portal offline after someone submitted fraudulent breach disclosures impersonating two well-known technology companies. As Bleeping Computer reported last week, fraudulent data breach disclosures were submitted to Maine's official breach portal and publicly posted before their legitimacy could be verified, prompting the named companies to deny the claims. The first fake notification targeted the popular messaging platform Discord, used by hundreds of millions of people worldwide. The notification, which claimed that 10 million people had been impacted by a data breach, was riddled with clues that should have made anyone question its legitimacy: it included a Gmail contact address, a placeholder phone number, and a consumer notification date of January 1st, 2000. Furthermore, it lacked an example notification letter to affected customers - something that is standard practice in legitimate breach filings. However, somewhat more convincing was a fake breach notice that targeted the multiplayer social virtual reality platform VRChat. The filing claimed that hackers had gained access to the company's cloud environment in May, and the data of more than 2.4 million users had been exposed. The fabricated VRChat breach notification listed compromised data including usernames, email addresses, VRChat+ subscription status, login history, device identifiers, IP addresses, and linked Steam or Meta account IDs, according to Bleeping Computer . However, that notification was submitted under the fake name "Scott Caruso" using the email address scaruso(at)vrchat.com. Charles Tupper, Head of Community at VRChat, confirmed to BleepingComputer that the notification was fraudulent: "VRChat did not submit this Notice of Data Incident, and the employee/email cited does not exist. We have no reason to believe that our data or systems have been compromised." In a statement, the office of the Maine Attorney General confirmed that it had "no knowledge of any recent legitimate data breach reports from either VRChat or Discord." So, what had gone wrong? It appears that the abuse of the system was possible because the Maine data breach reporting system lacked a proper verification mechanism. Anyone could submit a breach notification form and have it added to the portal website without verification. Which means that anybody who wanted to cause reputational damage to a company could submit a convincing-looking breach notice and have it published. The portal has temporarily disabled public access to the breach notification database while it reviews its procedures to reduce the chances of similar abuse in the future. And, of course, the false reports of breaches at VRChat and Discord have now been removed. It is not currently known who was behind the false submissions, and whether the targets were chosen deliberately or not. Perhaps worryingly, it also remains unclear how many (if any) other fraudulent breach notices may have been submitted through the portal before public access to it was suspended. Hopefully when the portal is brought back online its security will have been tightened, as many journalists do rely upon services like this to notify the general public about data breaches which occur and companies and organisations. tags Industry News Data Breach Author Graham CLULEY Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s. View all posts You might also like Bookmarks
```

#### Corroborating sources (1)

- **Graham Cluley** (practitioner_analysis)
  - Title: Maine forced to take down data breach portal after fake notices filed with authorities
  - Published: 2026-06-15T13:23:44+00:00
  - Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/maine-take-down-data-breach-portal
  - Summary: The US state of Maine has taken its public data breach notification portal offline after someone submitted fraudulent breach disclosures impersonating two well-known technology companies. Read more in my article on the Hot for Security blog.

### Cluster e25a84a74c — score 9

- Title: AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-19T15:30:47+00:00
- Link: https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security, supply_chain
- affected_products: GitHub, PyPI
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, ai_security, active_exploitation
- affected_products: PyPI, GitHub
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Microsoft researchers have detailed an exploit chain, named AutoJack, that turns an AI browsing agent into a delivery vehicle for remote code execution. Steer the agent to load an attacker's web page, and that page's JavaScript can reach a privileged local service on the same machine and spawn a process on the host. No credentials, no sign-in screen, and no further user interaction once
```

#### Full body

```
AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution  Swati Khandelwal  Jun 19, 2026 Vulnerability / Software Supply Chain Microsoft researchers have detailed an exploit chain, named AutoJack , that turns an AI browsing agent into a delivery vehicle for remote code execution. Steer the agent to load an attacker's web page, and that page's JavaScript can reach a privileged local service on the same machine and spawn a process on the host. No credentials, no sign-in screen, and no further user interaction once the agent loads the page. The attacker only has to get the agent to open it, and a planted link, a URL field, or a prompt injection will do. The flaw sits in AutoGen Studio , the open-source prototyping interface for Microsoft Research's AutoGen multi-agent framework. This is not a bug that hits everyone who installs the package, and the packaging detail is worth getting right. A plain pip install autogenstudio pulls the current stable release, 0.4.2.2, the build Microsoft inspected, and it has no Model Context Protocol (MCP) route at all. That is the basis for Microsoft's statement that the vulnerable MCP WebSocket surface "was never included in a PyPI release." It holds for the stable build. But the vulnerable handler did ship to PyPI, in two pre-release builds, 0.4.3.dev1 and 0.4.3.dev2. The Hacker News downloaded and inspected both. The MCP WebSocket route is present, the handler takes the command to run straight from the request, and it does not authenticate the caller. Neither build has been yanked. pip does not install pre-releases unless you pass --pre or pin the version, so a plain install was never exposed. Anyone who installed one of those pre-releases was. There is still no PyPI build carrying the main-branch hardening for them; the fixed code is in GitHub main at commit b047730. How the chain works AutoJack chains three weaknesses in the MCP WebSocket. First, the socket trusted localhost, a check meant to block a normal browser pointed at a malicious site. But a browsing agent running on the same box is localhost, so anything it loads inherits that localhost identity and passes the check. Second, the authentication middleware skipped MCP paths on the assumption that the handler would verify tokens itself. It never did, so the socket accepted unauthenticated connections regardless of the configured auth mode. Third, the endpoint took a command straight from a request parameter and ran it, with no allowlist on which executable could launch. Put together, a page on the open internet, rendered by a local agent, could run an attacker-chosen command under the account running AutoGen Studio. Microsoft describes this as research, not an active campaign, and reported no exploitation in the wild. The proof of concept used a "Web Content Summarizer" agent that, when fed an attacker URL, pops calc.exe on the developer's desktop, launched by the AutoGen Studio process. Microsoft reported the behavior to the Microsoft Security Response Center, and the maintainers hardened the main branch in commit b047730 (PR #7362). The fixed handler no longer reads the command from the URL; parameters are stored server-side behind a one-time session ID, and unknown IDs are refused. MCP routes now run through the normal authentication path. That hardening has not landed in a PyPI release yet. What to do A plain pip install autogenstudio gives you 0.4.2.2, which has no MCP route, so you are not affected. If you installed a pre-release, you have the vulnerable handler and no patched PyPI build to move to. Pull from GitHub main at or after commit b047730. That is the real fix. Until there is a release, separate the pieces the attack needs. Do not run AutoGen Studio on the same machine as a browsing or code-execution agent that touches untrusted content, because the chain only works when both share the same localhost. If they have to run together, isolate them in separate containers or VMs and run AutoGen Studio under a
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution
  - Published: 2026-06-19T15:30:47+00:00
  - Link: https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html
  - Summary: Microsoft researchers have detailed an exploit chain, named AutoJack, that turns an AI browsing agent into a delivery vehicle for remote code execution. Steer the agent to load an attacker's web page, and that page's JavaScript can reach a privileged local service on the same machine and spawn a process on the host. No credentials, no sign-in screen, and no further user interaction once

### Cluster 5b5787f3bd — score 9

- Title: Squidbleed (CVE-2026-47729) - Heartbleed-style vulnerability that leaks internal memory from every version of Squid Proxy, in its default configuration
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-06-19T10:21:41+00:00
- Link: https://www.reddit.com/r/netsec/comments/1u9y7yw/squidbleed_cve202647729_heartbleedstyle/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-47729

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-47729
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-47729
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/qwerty0x41 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Squidbleed (CVE-2026-47729) - Heartbleed-style vulnerability that leaks internal memory from every version of Squid Proxy, in its default configuration
  - Published: 2026-06-19T10:21:41+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1u9y7yw/squidbleed_cve202647729_heartbleedstyle/
  - Summary: submitted by /u/qwerty0x41 [link] [comments]

### Cluster 5e1e9d778f — score 9

- Title: OpenBSD MPLS kernel stack leaks remotely (CVE-2026-56099)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-06-19T13:27:18+00:00
- Link: https://www.reddit.com/r/netsec/comments/1ua20fg/openbsd_mpls_kernel_stack_leaks_remotely/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-56099

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-56099
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-56099
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
A crafted MPLS packet can trigger an out-of-bounds read in mpls_do_error, leaking 4 bytes of adjacent kernel stack memory back in an ICMP/MPLS error response. It requires MPLS enabled, but the leak is remote and repeatable. Fixed in OpenBSD-current on 2026-06-18. submitted by /u/Emergency_Stable_923 [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: OpenBSD MPLS kernel stack leaks remotely (CVE-2026-56099)
  - Published: 2026-06-19T13:27:18+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1ua20fg/openbsd_mpls_kernel_stack_leaks_remotely/
  - Summary: A crafted MPLS packet can trigger an out-of-bounds read in mpls_do_error, leaking 4 bytes of adjacent kernel stack memory back in an ICMP/MPLS error response. It requires MPLS enabled, but the leak is remote and repeatable. Fixed in OpenBSD-current on 2026-06-18. submitted by /u/Emergency_Stable_923 [link] [comments]

### Cluster 33472b1f9c — score 8

- Title: Modern Web Application Content Discovery
- Source: TrustedSec (detection_response_operations)
- Published: 2026-06-18T04:00:00+00:00
- Link: https://trustedsec.com/blog/modern-web-application-content-discovery
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>When testing web applications, discovering what functionality is available is key to finding vulnerabilities. Ideally you want to find as many application pages as possible. You can do this by using web‑crawling or…</p>
```

#### Full body

```
Blog Modern Web Application Content Discovery June 18, 2026 Modern Web Application Content Discovery Written by Luke Bremer Application Security Assessment Table of contents FORCED BROWSING WEB CRAWLERS OSINT GOOGLE OSINT GITHUB WRAP-UP PREVENTION When testing web applications, discovering what functionality is available is key to finding vulnerabilities. Ideally you want to find as many application pages as possible. You can do this by using web‑crawling or spidering tools to uncover indexed pages, as well as employing forced‑browsing techniques. When doing forced browsing you are looking for pages that are not indexed on the site but still available. Forced-browsing is more useful when the applications user interface (UI) is limited, but even on applications with a large UI, forced-browsing can return webpages that would otherwise not be known. Recently, I got this question: "I found a URL that is returning a default homepage, but it has no links or navigation. How do I find out if the application has functionality?” So, I figured I would write up a quick guide on how I find content in modern web applications. FORCED BROWSING To start we can try to guess page names that are present in an application. A common way to browse for un-indexed pages is to run though a list of common page names. For example, we can grab a HTTP request with a proxy like Burp Suite and send the request to intruder which makes repeated requests with different page names. Figure 1 - Burp Suite Intruder Then, we can review the results to see what response codes are returned by the application. Figure 2 - Intruder Results If a page exists, the application could return a 200 response code or sometimes a redirect code like a 302. Forced browsing typically sends a lot of requests, and the results depends on how good of a wordlist you use. Seclists is still a pretty good baseline to get common lists: https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content But a lot of tools, such as Burp Suite , have common lists built in as well. Burp Suite does restrict how fast requests can be sent in the community version, so using command line tools such as FFuF is also common and in some cases can return results faster. Figure 3 - FFuF Output It is important to note that by default FFuF sends 40 requests at a time where Burp Suite only sends 10 requests at a time. The -t parameter in FFuF can set the number of requests send each iteration. To ensure you don't overwhelm a site, or get blocked by rate limits, you may want to decrease the threads being used. Typically, if a page returns a response code that is not a 404 (Not found) that page might be part of a valid URL path and we can then start re-searching any paths that seem to get a valid response code like a 200. If we find a valid page, we can then navigate to the page in our browser and review what functionality is available. Figure 4 - FFuF Recursive Output It should be noted that depending on the website, the application may require pages to contain an extension such as .html , or .php . So, when looking for a URL path like /blog different sites will return different response codes for example.com/blog and example.com/blog.html Figure 5 - FFuF Output With File Extensions To make forced browsing a little more targeted, we can review application response headers or common fingerprinting tools like Wappalyzer to identify what server or software is being used in the application. Figure 6a - Wappalyzer Output Figure 6b - Server Response Header Then, we can ask an AI model to create a list of common URL paths, or common file paths that you can use with FFuF or Burp Suite . Figure 7 - AI Generated List for Forced Browsing WEB CRAWLERS It's worth mentioning there may not be many un-indexed pages on a site. In those cases, web crawling would be better suited for enumeration. You can use Burp Suite ’s Content Discovery function by right clicking a target and selecting Engagement Tools/Discover Content
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: Modern Web Application Content Discovery
  - Published: 2026-06-18T04:00:00+00:00
  - Link: https://trustedsec.com/blog/modern-web-application-content-discovery
  - Summary: <p>When testing web applications, discovering what functionality is available is key to finding vulnerabilities. Ideally you want to find as many application pages as possible. You can do this by using web‑crawling or…</p>

### Cluster 551a871c9b — score 8

- Title: JQ for Hackers
- Source: TrustedSec (detection_response_operations)
- Published: 2026-06-16T04:00:00+00:00
- Link: https://trustedsec.com/blog/jq-for-hackers
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: education
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: education
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>When I was first introduced to jq, it was overwhelming and confusing. I tried to just wing it, not realizing it was a very complex and powerful program. With more and more tools outputting JSON, I figured it was time to…</p>
```

#### Full body

```
Blog JQ for Hackers June 16, 2026 JQ for Hackers Written by Justin Bollinger Penetration Testing Training Table of contents Some JSON to Play With Pretty Printing With jq A Quick JSON Primer Extracting Specific Fields Filtering With select A Real-World Example: Parsing ldapdomaindump Output The Mental Model When I was first introduced to jq , it was overwhelming and confusing. I tried to just wing it, not realizing it was a very complex and powerful program. With more and more tools outputting JSON, I figured it was time to actually learn it. Turns out, it's pretty easy once you get the hang of it. This blog is for the hackers, sysadmins, and anyone who wasn't forced to learn JavaScript by some sadistic college professor. It's an attempt to convince you, the grey-bearded hacker, to stop using CSV files and cut and embrace JSON. If you're familiar with Python dictionaries, this should come naturally. Some JSON to Play With Lucky for us, httpx from ProjectDiscovery is a perfect tool to use as a simple example. Run the following to get a JSON object back: echo www.trustedsec.com | httpx -j The output will look something like this: That's hard to read ‚ it's a lot of data, and it's all on a single line. Without word wrap, you wouldn't even be able to see the whole thing. You also can't grep cleanly through it. Pretty Printing With jq Pipe the same command to jq . and the output becomes legible: echo www.trustedsec.com | httpx -j | jq . { "timestamp": "2025-03-14T17:19:03.813358-04:00", "cdn_name": "cloudflare", "cdn_type": "waf", "port": "443", "url": "https://www.trustedsec.com", "input": "https://www.trustedsec.com", "title": "TrustedSec | Your Trusted Cybersecurity Partner | Protecting What‚Ä¶", "scheme": "https", "webserver": "cloudflare", "content_type": "text/html", "method": "GET", "host": "172.67.70.133", "path": "/", "time": "762.046417ms", "a": [ "172.67.70.133", "104.26.15.63", "104.26.14.63" ], "aaaa": [ "2606:4700:20::ac43:4685", "2606:4700:20::681a:f3f", "2606:4700:20::681a:e3f" ], "tech": [ "Alpine.js", "Cloudflare", "Craft CMS", "Google Tag Manager", "HSTS", "SEOmatic" ], "words": 22245, "lines": 779, "status_code": 200, "content_length": 258423, "failed": false, "cdn": true, "knowledgebase": { "PageType": "other", "pHash": 0 }, "resolvers": [ "8.8.4.4:53", "1.1.1.1:53" ] } That's better, but it's still a lot of information that I don’t need right now. How do I use jq to limit the output? A Quick JSON Primer Before we go further, you need to understand a little bit about JSON. If you want the full spec, see the JSON Schema: core definitions and terminology . We’ll go over the bare minimum for our purposes today. JSON has seven primitive types: array , boolean , integer , number , NULL , object , and string . We're going to focus on objects and arrays . An object is denoted with curly braces {} and contains properties (keys) mapped to values: { "Name": "John" } This object has the property, Name with the string value, John . The value of a property can also be an array , denoted with [] : { "Names": ["John", "Jane", "Jason"] } That's all you need to follow along for now. Extracting Specific Fields Say, for example, I only want the host value from the httpx output. With jq , you reference a property by prefixing it with a period: echo www.trustedsec.com | httpx -j | jq '.host' "172.67.70.133" Don’t want those double quotes? No worries. Just add -r . echo www.trustedsec.com | httpx -j | jq -r '.host' 172.67.70.133 Want multiple fields? Build a new object on the fly: echo www.trustedsec.com | httpx -j | jq '{url: .url, ip: .host_ip, tech: .tech}' { "url": "https://www.trustedsec.com", "ip": "172.67.70.133", "tech": ["Alpine.js", "Cloudflare", "Craft CMS", "Google Tag Manager", "HSTS", "SEOmatic"] } To grab a single value out of an array, index it like Python: echo www.trustedsec.com | httpx -j | jq '.a[0]' "94.247.142.1" To iterate through every value in an array, use .[] : echo www.trustedsec.com | httpx -j | jq -r '.
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: JQ for Hackers
  - Published: 2026-06-16T04:00:00+00:00
  - Link: https://trustedsec.com/blog/jq-for-hackers
  - Summary: <p>When I was first introduced to jq, it was overwhelming and confusing. I tried to just wing it, not realizing it was a very complex and powerful program. With more and more tools outputting JSON, I figured it was time to…</p>

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

### Cluster b6bc3df279 — score 8

- Title: How attackers are jailbreaking LLMs with CTF framing and how to catch them
- Source: Sysdig (detection_response_operations)
- Published: 2026-06-15T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/how-attackers-are-jailbreaking-llms-with-ctf-framing-and-how-to-catch-them
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: AWS
- cve_ids: CVE-2026-42271, CVE-2026-42589, CVE-2026-44336
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: AWS
- cve_ids: CVE-2026-42589, CVE-2026-42271, CVE-2026-44336
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
< back to blog How attackers are jailbreaking LLMs with CTF framing and how to catch them Published by: Michael Clark Director of Threat Research @ linkedin Published: June 15, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more AI models are trained to refuse user requests that lead them to generate malicious code. But as it turns out, circumventing those guardrails is often easier than many thought. The Sysdig Threat Research Team (TRT) has observed threat actors getting around that guardrail with a simple disguise: framing their exploit requests as legitimate security research. By presenting an attack as a capture-the-flag (CTF) challenge or CVE-hunting exercise (i.e., “I’m working on a CTF challenge on CVE-X. Write me a probe.”), operators coax their own upstream LLMs into producing working exploit code. Then, they can deploy that output nearly verbatim against real targets. The framing isn’t only meant to fool defenders. It’s meant to fool the attacker’s own AI assistant. To the Sysdig TRT’s knowledge, this jailbreak-to-deploy pattern has not been fully documented in the wild until now. The campaigns that we identified targeted five separate applications — PraisonAI , LiteLLM , FastGPT , Open-WebUI , and Gotenberg — with known CVE exploits. The first four are LLM platform components: agent orchestration, model gateway, agent sandbox, and chat frontend. Gotenberg, on the other hand, is an unrelated Chromium-based document converter. That spread across application categories is significant, and is a topic we explore further below. The artifact that first exposed the technique was a CVE-templated User-Agent (for example, ctf-litellm-cve42271-mcp-stdio/1.0 ), but the CVE/CTF label is not confined to the User-Agent (UA). The same string leaks into every field the LLM generated for itself, including the password field, the AWS roleSessionName , and account-creation aliases, because the model bakes its prompt framing into each output. Notably, the same strings appeared against the same target from two operators we tracked separately. That conversation is strong evidence that both are prompting upstream LLMs with similar CTF framing and then shipping the results unchanged. The CTF framing is not only an attempt to evade detection, as it had no effect on our telemetry classification. It exists to manipulate the operator’s own LLM, getting past safety training that would otherwise decline to write an unsanctioned exploit. This is the jailbreak. What the Sysdig TRT observed In early June, Source IP 38.181.81.164 (Cogent Communications, US) hit five applications in quick succession. Each hit carried a UA template that identified the application and the CVE the operator was targeting. The rows below are in the order they arrived: Target User-Agent Gotenberg (CVE-2026-42589 ExifTool argument injection) Mozilla/5.0 ctf-gotenberg-cve42589-akia-grep PraisonAI (GHSA-xcmw-grxf-wjhj recipe RCE) cve-hunt FastGPT agent sandbox ctf-fastgpt-cve42302-authnone/1.0 LiteLLM (CVE-2026-42271 MCP stdio RCE) ctf-litellm-cve42271-mcp-stdio/1.0 Open-WebUI signup (account staging) (no User-Agent; password: MioCtf!<random>) PraisonAI (CVE-2026-44336 MCP path traversal) cve-hunt-praisonai-cve44336 The PraisonAI campaign sent many weaponized /mcp POST requests carrying the path-traversal payload from GHSA-9mqq-jqxf-grvw (CVE-2026-44336). The Open-WebUI activity created six accounts via POST /api/v1/auths/signup using the email address mio<12-hex>@example.com and passwords matching MioCtf!<random> , with the CTF prefix baked into the password generator. Several AWS API calls followed from the same source against an access key extracted in-session: an sts:GetCallerIdentity identity check, then repeated bedrock:InvokeModel and bedrock:PutUseCaseForModelAccess attempts as the operator tried
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: How attackers are jailbreaking LLMs with CTF framing and how to catch them
  - Published: 2026-06-15T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/how-attackers-are-jailbreaking-llms-with-ctf-framing-and-how-to-catch-them

### Cluster 99669f5bd4 — score 8

- Title: FortiBleed leak exposes Fortinet VPN credentials for 73,000 devices.
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-06-18T12:54:39+00:00
- Link: https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- affected_products: Fortinet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- affected_products: Fortinet
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A newly discovered data leak dubbed "FortiBleed" has exposed what appears to be a collection of Fortinet and FortiGate VPN credentials for 73,932 firewall URLs at organizations worldwide. [...]
```

#### Full body

```
FortiBleed leak exposes Fortinet VPN credentials for 73,000 devices. By Lawrence Abrams June 18, 2026 08:54 AM 3 A newly discovered data leak dubbed "FortiBleed" has exposed what appears to be a collection of Fortinet and FortiGate VPN credentials for 73,932 firewall URLs at organizations worldwide. The exposed data was first discovered by security researcher Bob Diachenko, who says he found a server containing what appeared to be valid Fortinet VPN credentials, including usernames, email addresses, and plaintext passwords. According to screenshots and information shared by Diachenko, the database contains entries for Chevron, Samsung, Foxconn, Comcast, AT&T, Mercedes-Benz, Toyota, Sinopec, State Grid, and many others. "Massive Fortinet/FortiGate bruteforce/active exploitation campaign uncovered in action," Diachenko posted on LinkedIn . "Thousands of top vendors instances are listed in the files like this (see screenshot). This one alone has 21,634 domain names - from Chevron to Fortinet itself. All - with potentially working passwords to the FortiGate appliances obtained through various menas." The exposed data also included comments listing each organization's industry, revenue, and number of employees, likely for planning attacks. Fortinet credentials found on an exposed server Source: Diachenko Diachenko later shared additional information that claimed the operation was conducted by a Russian-speaking multi-operator threat group that harvested credentials for FortiGate SSL VPN devices. According to Diachenko's investigation, the attackers allegedly conducted approximately 1.16 billion credential attempts against 320,777 FortiGate targets and an additional 2.1 billion attempts against 163,650 Microsoft SQL Server systems. He further claimed the threat actors intercepted SSL VPN authentication hashes, cracked them using a 45-GPU cluster managed through Hashtopolis, and used the recovered credentials to move laterally into internal Active Directory environments. Diachenko told BleepingComputer he obtained these details after analyzing additional files inadvertently exposed on the same server. "They accidentally left an open directory with artefacts, connection strings, tooling, scripts and data online. Analytics obtained via their cron jobs, bash histories, logs etc," Diachenko explained. The researcher also stated that multiple organizations across Japan, Taiwan, Vietnam, Iraq, and Turkey were fully compromised, including a Turkish NATO defense contractor from which classified documents were allegedly stolen. Threat intelligence company Hudson Rock has since published its own analysis of the exposed data after receiving the dataset from Diachenko. The company described the collection as one of the largest known troves of compromised Fortinet-related credentials. According to Hudson Rock, the dataset contains 73,932 unique firewall URLs across 194 countries and impacts 21,632 unique domains. The company says the attackers maintained detailed logs of successful compromises and assembled a database containing verified credentials for organizations across nearly every major industry sector. Among the organizations Hudson Rock says appear in the dataset are Foxconn, Samsung, Comcast, Siemens, Lenovo, PwC, Accenture, Oracle, and numerous government agencies and critical infrastructure operators. The company also released statistics showing that the highest number of affected devices was in India, the United States, Taiwan, Mexico, Turkey, Thailand, Colombia, Malaysia, Chile, and the United Arab Emirates. The most common sectors for the listed companies are telecommunications, IT services, financial services, government organizations, healthcare providers, educational institutions, and manufacturing. One strange aspect of the leak is that many of the exposed credentials were long, complex passwords that would ordinarily be considered difficult to crack. Believed to be extracted from Fortinet configs Cybersecurity researcher Kevin
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: FortiBleed leak exposes Fortinet VPN credentials for 73,000 devices.
  - Published: 2026-06-18T12:54:39+00:00
  - Link: https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/
  - Summary: A newly discovered data leak dubbed "FortiBleed" has exposed what appears to be a collection of Fortinet and FortiGate VPN credentials for 73,932 firewall URLs at organizations worldwide. [...]

### Cluster e8c9ef5f3a — score 8

- Title: The Top 10 Attack Surface Exposures in 2026
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-17T10:30:00+00:00
- Link: https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html
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
Breaches don't always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk. With time-to-exploit now down to a
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: The Top 10 Attack Surface Exposures in 2026
  - Published: 2026-06-17T10:30:00+00:00
  - Link: https://thehackernews.com/2026/06/the-top-10-attack-surface-exposures-in.html
  - Summary: Breaches don't always start with a zero-day. An exposed admin panel can get brute-forced, or credentials reused from a previous attack. But when a vulnerability does drop — like MongoBleed earlier this year, which let attackers pull credentials and session tokens from server memory without authentication — anything internet-facing is immediately at risk. With time-to-exploit now down to a

### Cluster a536754c57 — score 8

- Title: Fake Microsoft Alerts Used to Deploy North Korean NarwhalRAT Malware
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-06-16T08:14:55+00:00
- Link: https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: APT37

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng
- actor_attribution: APT37
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- actor_attribution: APT37
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The North Korean state-sponsored hacking group known as ScarCruft (aka APT37) has been observed using spear-phishing messages impersonating Microsoft Account security notifications to deliver a new malware called NarwhalRAT. "The attack email contained a message impersonating an MS account security alert," the Genians Security Center (GSC) said. "It was designed to create concern over possible
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Fake Microsoft Alerts Used to Deploy North Korean NarwhalRAT Malware
  - Published: 2026-06-16T08:14:55+00:00
  - Link: https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html
  - Summary: The North Korean state-sponsored hacking group known as ScarCruft (aka APT37) has been observed using spear-phishing messages impersonating Microsoft Account security notifications to deliver a new malware called NarwhalRAT. "The attack email contained a message impersonating an MS account security alert," the Genians Security Center (GSC) said. "It was designed to create concern over possible

### Cluster 41256d55c8 — score 8

- Title: CVE-2026-5667: Unauthenticated Remote Control of Mitsubishi MAC-577IF-2E WiFi Adapters via Probe Request Reconnaissance
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-06-18T18:05:44+00:00
- Link: https://www.reddit.com/r/netsec/comments/1u9dncq/cve20265667_unauthenticated_remote_control_of/
- Fetch status: not_attempted
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
