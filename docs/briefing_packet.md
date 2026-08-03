# PHANTOMSignal Briefing Packet

- Generated: 2026-08-03T12:31:50.270723+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 74
- Total items in window: 357
- Total clusters raw: 157
- Total clusters in packet: 76
- Dropped low score: 81
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

- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
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
  - In window count: 1
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
  - In window count: 2
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
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
  - In window count: 8
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
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
  - In window count: 2
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 2
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
  - In window count: 0
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
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
- **TrustedSec** (detection_response_operations)
  - URL: https://www.trustedsec.com/feed/
  - Status: ok
  - Item count: 10
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
  - In window count: 1
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
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
  - In window count: 0
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 12
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 8
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 9
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 8
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 17
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
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 29
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 29
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 2
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 50
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/cybersecurity/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/sysadmin** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/sysadmin/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/blueteamsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/blueteamsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 3
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
  - In window count: 16
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

### ransomware extortion targeting AWS
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 5
- Article count: 20
- Cohesion: 0.235
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, supply_chain, data_breach, apt_espionage
  - actor_attribution: ShinyHunters
  - affected_industries: financial_services
  - affected_products: AWS, GitHub, SonicWall
- Cluster IDs: ae0cc6b051, 90d3c1c1e2, 0d2189c83e, 1cd705f068, c97bc0e859
- Links:
  - https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/
  - https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/
  - https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
  - https://www.bleepingcomputer.com/news/security/amazon-links-debug-chalk-npm-supply-chain-attacks-to-north-korean-hackers/
  - https://www.infosecurity-magazine.com/news/aws-north-korea-axios-npm-supply/
  - https://risky.biz/RBNEWS595/
  - https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/
  - https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/
  - https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
  - https://isc.sans.edu/diary/rss/33196
  - https://www.securityweek.com/ruby-on-rails-patches-critical-vulnerability/
  - https://www.securityweek.com/brinks-home-discloses-data-breach-as-hackers-leak-files/
  - https://risky.biz/RBNEWSSI138/
  - https://aws.amazon.com/blogs/security/extend-amazon-inspector-sbom-generator-with-plugins/

### supply chain targeting npm
- Anchor signal: npm
- Theme key: npm
- Cluster count: 4
- Article count: 15
- Cohesion: 0.209
- Shared strong signals: npm
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain, phishing_social_eng
  - actor_attribution: TeamPCP
  - affected_products: npm, PyPI, GitHub
- Cluster IDs: 4c8ed8c5fa, ae0cc6b051, 2675bb2bb6, 8553a0e574
- Links:
  - https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
  - https://www.securityweek.com/russian-state-apt-linked-to-recent-public-wi-fi-gateway-hacking/
  - https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/
  - https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/
  - https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
  - https://www.bleepingcomputer.com/news/security/amazon-links-debug-chalk-npm-supply-chain-attacks-to-north-korean-hackers/
  - https://www.infosecurity-magazine.com/news/aws-north-korea-axios-npm-supply/
  - https://risky.biz/RBNEWS595/
  - https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/
  - https://aws.amazon.com/blogs/security/secure-your-npm-and-pip-package-updates-in-amazon-linux/
  - https://www.intel471.com/blog/software-supply-chain-attacks-weaponizing-trusted-developer-workflows

### CVE-2026-66066 exploitation activity
- Anchor signal: CVE-2026-66066
- Theme key: cve-2026-66066
- Cluster count: 3
- Article count: 5
- Cohesion: 0.605
- Shared strong signals: CVE-2026-66066
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-66066
  - urgency_signals: preauth_unauth, actively_exploited, poc_available
- Cluster IDs: 513073eb52, 0d2189c83e, 2126e62d58
- Links:
  - https://www.rapid7.com/blog/post/etr-kindarails2shell-cve-2026-66066-critical-arbitrary-file-read-and-possible-remote-code-execution-in-ruby-on-rails
  - https://www.helpnetsecurity.com/2026/08/03/kindarails2shell-cve-2026-66066-vulnerability/
  - https://thehackernews.com/2026/07/critical-rails-flaw-could-let.html
  - https://www.securityweek.com/ruby-on-rails-patches-critical-vulnerability/
  - https://www.bleepingcomputer.com/news/security/rails-patches-critical-active-storage-flaw-with-rce-potential/

### Microsoft SharePoint active exploitation
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 4
- Article count: 6
- Cohesion: 0.214
- Shared strong signals: Microsoft SharePoint
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation, ransomware_extortion, phishing_social_eng
  - affected_industries: manufacturing_industrial
  - affected_products: Microsoft SharePoint, Cisco, OpenAI/ChatGPT
  - cve_ids: CVE-2026-50522
  - urgency_signals: actively_exploited, zero_day, poc_available
- Cluster IDs: e2f6a950f1, 85d2724fda, 7d478340af, b138851666
- Links:
  - https://thehackernews.com/2026/07/cisco-fmc-zero-day-actively-exploited.html
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20316/
  - https://www.infosecurity-magazine.com/news/phishing-dominates-initial-entry/
  - https://research.checkpoint.com/2026/27th-july-threat-intelligence-report/
  - https://blog.talosintelligence.com/ir-trends-q2-2026/
  - https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html

### Cisco active exploitation
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 3
- Article count: 5
- Cohesion: 0.209
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Cisco, Microsoft SharePoint
  - cve_ids: CVE-2026-20316
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: e2f6a950f1, 38979f8c48, 7d478340af
- Links:
  - https://thehackernews.com/2026/07/cisco-fmc-zero-day-actively-exploited.html
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20316/
  - https://www.infosecurity-magazine.com/news/phishing-dominates-initial-entry/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-6516/
  - https://blog.talosintelligence.com/ir-trends-q2-2026/

### supply chain targeting PyPI
- Anchor signal: PyPI
- Theme key: pypi
- Cluster count: 3
- Article count: 14
- Cohesion: 0.206
- Shared strong signals: PyPI
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: supply_chain
  - affected_products: PyPI, npm
- Cluster IDs: 4c8ed8c5fa, b1e900a5a7, 2675bb2bb6
- Links:
  - https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
  - https://www.securityweek.com/russian-state-apt-linked-to-recent-public-wi-fi-gateway-hacking/
  - https://embracethered.com/blog/posts/2026/pipewire-flatpak-linux-sandbox-escape-cve-2026-5674/
  - https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything
  - https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html
  - https://therecord.media/anthropic-ai-hacked-three-real-companies
  - https://www.bleepingcomputer.com/news/security/anthropics-claude-breached-3-orgs-uploaded-pypi-malware-during-tests/
  - https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html
  - https://www.infosecurity-magazine.com/news/anthropic-claude-breached-three/
  - https://aws.amazon.com/blogs/security/secure-your-npm-and-pip-package-updates-in-amazon-linux/

### CVE-2026-63077 exploitation activity
- Anchor signal: CVE-2026-63077
- Theme key: cve-2026-63077
- Cluster count: 2
- Article count: 3
- Cohesion: 0.738
- Shared strong signals: CVE-2026-63077
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-63077
  - urgency_signals: preauth_unauth
- Cluster IDs: 495c7fe201, 3ba1ff40b5
- Links:
  - https://www.rapid7.com/blog/post/etr-cve-2026-63077-critical-unauthenticated-remote-code-execution-in-jetbrains-teamcity
  - https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html
  - https://www.bleepingcomputer.com/news/security/jetbrains-warns-of-critical-teamcity-remote-code-execution-flaw/

### CVE-2026-16232 exploitation activity
- Anchor signal: CVE-2026-16232
- Theme key: cve-2026-16232
- Cluster count: 2
- Article count: 3
- Cohesion: 0.277
- Shared strong signals: CVE-2026-16232
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day
  - cve_ids: CVE-2026-16232
  - urgency_signals: zero_day, poc_available
- Cluster IDs: 450eb3c7b3, 85d2724fda
- Links:
  - https://www.rapid7.com/blog/post/ra-check-point-smartconsole-authentication-bypass-technical-analysis-cve-2026-16232
  - https://thehackernews.com/2026/07/rapid7-releases-poc-for-exploited-check.html
  - https://research.checkpoint.com/2026/27th-july-threat-intelligence-report/

### SonicWall active exploitation
- Anchor signal: SonicWall
- Theme key: sonicwall
- Cluster count: 3
- Article count: 4
- Cohesion: 0.244
- Shared strong signals: SonicWall
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, data_breach, apt_espionage, active_exploitation
  - affected_industries: financial_services
  - affected_products: SonicWall, AWS, OpenAI/ChatGPT
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 0d2189c83e, 1cd705f068, 1b4f7b92ff
- Links:
  - https://www.securityweek.com/ruby-on-rails-patches-critical-vulnerability/
  - https://www.securityweek.com/brinks-home-discloses-data-breach-as-hackers-leak-files/
  - https://www.securityweek.com/recent-sonicwall-vulnerabilities-exploited-in-ransomware-attacks/
  - https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html

### Apple iOS/macOS vulnerability activity
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 2
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Apple iOS/macOS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Apple iOS/macOS
- Cluster IDs: 38979f8c48, 90d3c1c1e2
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-6516/
  - https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/
  - https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
  - https://isc.sans.edu/diary/rss/33196

### WordPress active exploitation
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
  - urgency_signals: actively_exploited
- Cluster IDs: 38979f8c48, b61889968b
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-6516/
  - https://www.infosecurity-magazine.com/news/one-percent-ai-vulnerabilities/

### credential theft targeting Palo Alto Networks
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 2
- Article count: 5
- Cohesion: 0.244
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: credential_theft
  - affected_products: Palo Alto Networks
- Cluster IDs: 90d3c1c1e2, d1c29125d3
- Links:
  - https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/
  - https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
  - https://isc.sans.edu/diary/rss/33196
  - https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (2)
- **This month in security with Tony Anscombe – July 2026 edition**
  - Cluster: 974cdece8d
  - Sources in window: 3
  - Window hours: 5.8
  - Cohort count: 6
- **Escaping Linux Sandboxes via PipeWire (CVE-2026-5674)**
  - Cluster: b1e900a5a7
  - Sources in window: 3
  - Window hours: 5.6
  - Cohort count: 3

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-59309 + VMware (cluster 4a06e44c92, first observation: True)
- Pair: CVE-2026-59310 + VMware (cluster 4a06e44c92, first observation: True)
- Pair: APT29 + PyPI (cluster 4c8ed8c5fa, first observation: True)
- Pair: APT29 + SolarWinds (cluster 4c8ed8c5fa, first observation: True)
- Pair: APT29 + npm (cluster 4c8ed8c5fa, first observation: True)
- Pair: TeamPCP + SolarWinds (cluster 4c8ed8c5fa, first observation: True)
- Pair: UNC4736 + PyPI (cluster 4c8ed8c5fa, first observation: True)
- Pair: UNC4736 + SolarWinds (cluster 4c8ed8c5fa, first observation: True)
- Pair: UNC4736 + npm (cluster 4c8ed8c5fa, first observation: True)
- Pair: CVE-2026-20079 + Cisco (cluster e2f6a950f1, first observation: True)
- Pair: CVE-2026-20079 + Microsoft SharePoint (cluster e2f6a950f1, first observation: True)
- Pair: CVE-2026-20316 + Cisco (cluster e2f6a950f1, first observation: True)
- Pair: CVE-2026-20316 + Microsoft SharePoint (cluster e2f6a950f1, first observation: True)
- Pair: CVE-2026-50522 + Cisco (cluster e2f6a950f1, first observation: True)
- Pair: CVE-2026-50522 + Microsoft SharePoint (cluster e2f6a950f1, first observation: True)

### Drift (3)
- **APT29** (cluster 4c8ed8c5fa)
  - New industries: (none)
  - New products: npm
  - Prior top industries: (none)
  - Prior top products: Microsoft Entra, PyPI, SolarWinds
- **TeamPCP** (cluster 4c8ed8c5fa)
  - New industries: (none)
  - New products: SolarWinds
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: GitHub, PyPI, npm
- **ShinyHunters** (cluster 1cd705f068)
  - New industries: (none)
  - New products: AWS, SonicWall
  - Prior top industries: education, financial_services, government
  - Prior top products: Anthropic/Claude, Microsoft Entra, Salesforce

### Persistence (6)
- actor_attribution: ShinyHunters (weeks observed: 10, cluster 1cd705f068)
- actor_attribution: TeamPCP (weeks observed: 7, cluster 4c8ed8c5fa)
- actor_attribution: LockBit (weeks observed: 4, cluster f6cd02268d)
- actor_attribution: APT29 (weeks observed: 3, cluster 4c8ed8c5fa)
- cve_ids: CVE-2026-50522 (weeks observed: 3, cluster e2f6a950f1)
- cve_ids: CVE-2026-48283 (weeks observed: 3, cluster dd6691160d)

### Tier inversion (2)
- **Simple Job Board ≤ 2.11.0 - Unauthenticated RCE (CVE-2024-1813)**
  - Cluster: 1276a22842
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2024-1813
- **New vBulletin Vulnerability!**
  - Cluster: fa1ef247b7
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-61511

## Clusters

### Cluster 450eb3c7b3 — score 64

- Title: Check Point SmartConsole Authentication Bypass Technical Analysis (CVE-2026-16232)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-28T18:32:03+00:00
- Link: https://www.rapid7.com/blog/post/ra-check-point-smartconsole-authentication-bypass-technical-analysis-cve-2026-16232
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-16232

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- cve_ids: CVE-2026-16232
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- cve_ids: CVE-2026-16232
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 22, 2026, Check Point published a security advisory for CVE-2026-16232 , an authentication bypass in the SmartConsole login process affecting Security Management Server and Multi-Domain Security Management Server (MDS). By leveraging CVE-2026-16232, an unauthenticated attacker can obtain an application login token, use this token to log in through SmartConsole with full administrator privileges, and modify the security policy or security configuration. Exploitation requires network access to the Management Server and for a Trusted Clients configuration that does not restrict GUI clients, which in our testing was a default setting. This vulnerability was reported as being exploited in the wild as a zero-day vulnerability at the time of disclosure. Our analysis finds that the root cause of CVE-2026-16232 is a broken trust boundary in the application authentication path. A vulnerable server accepts an attacker-supplied Secure Internal Communication (SIC) distinguished nam
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits Check Point SmartConsole Authentication Bypass Technical Analysis (CVE-2026-16232) Stephen Fewer Jul 28, 2026 | Last updated on Jul 28, 2026 | 11 min read Overview On July 22, 2026, Check Point published a security advisory for CVE-2026-16232 , an authentication bypass in the SmartConsole login process affecting Security Management Server and Multi-Domain Security Management Server (MDS). By leveraging CVE-2026-16232, an unauthenticated attacker can obtain an application login token, use this token to log in through SmartConsole with full administrator privileges, and modify the security policy or security configuration. Exploitation requires network access to the Management Server and for a Trusted Clients configuration that does not restrict GUI clients, which in our testing was a default setting. This vulnerability was reported as being exploited in the wild as a zero-day vulnerability at the time of disclosure. Our analysis finds that the root cause of CVE-2026-16232 is a broken trust boundary in the application authentication path. A vulnerable server accepts an attacker-supplied Secure Internal Communication (SIC) distinguished name (DN) as the identity of a remote application instead of binding that identity to the authenticated remote peer certificate DN returned by getCertificateDnName() . An attacker can read the management server's own SIC DN during the unauthenticated bootstrap communication, replay that DN in a forged application certificate bind, obtain an application token, and then ask the legacy management service to mint a new SmartConsole single sign-on (SSO) ticket. Rapid7 Labs has reproduced CVE-2026-16232 against affected R81.20 and R82.10 versions of the target software. Our proof-of-concept (PoC) exploit script can be used to successfully validate if a target is either vulnerable or patched. The vendor supplied patches have been confirmed to successfully remediate the vulnerability and prevent our PoC script from succeeding. Analysis SmartConsole is the desktop client administrators use to manage Check Point policy and configuration. A SmartConsole login crosses two generations of management plumbing over the network. The first is the legacy FWM/CPMI service, listening on TCP 18190 . It uses SIC, Check Point's certificate-based trust mechanism for communication between management components. Once the SIC bootstrap completes, FWM exchanges length-prefixed “FwSet” objects, a Check Point name/value encoding used by older management services. The second is the newer CPM/DLE service. This exposes SOAP services over HTTPS on TCP 19009 under the URI path /cpmws/ . SmartConsole uses these services for login, queries, and object operations. Authenticated requests carry DLESESSIONID and CLIENTSESSIONID header values to prove a client is authenticated. The exploit for CVE-2026-16232 uses both the FWM/CPMI and CPM/DLE services. It first uses the native FWM/CPMI protocol to claim an application identity and obtain an application token via the root cause of the vulnerability. It then uses the accepted native application session to ask FWM for a SmartConsole SSO ticket, redeems the ticket over CPM's SOAP API, and receives a SmartConsole session. The diagram below shows the flow for exploiting CVE-2026-16232. Figure 1: Flow diagram of exploitation. The application authentication boundary The Java login service contains a bridge for FWM application based logins. The authenticateUser method splits the supplied username into an application name and a SIC DN, then passes both into cpApplicationAuthentication() . // Source: work/t146/mgmt_wrapper.tgz:fw1/cpm-server/dleserver.jar.full!/com/checkpoint/management/dleserver/coresvc/internal/LoginSvcImpl.class private AuthenticationResponse authenticateUser(AuthenticationInfoBase authenticationInfoBase, String string, String string2, CPUUID cPUUID, boolean bl, LockAdminInfoContainer lockAdminInfoContainer, ExternalLoginInfo externalLogin
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Check Point SmartConsole Authentication Bypass Technical Analysis (CVE-2026-16232)
  - Published: 2026-07-28T18:32:03+00:00
  - Link: https://www.rapid7.com/blog/post/ra-check-point-smartconsole-authentication-bypass-technical-analysis-cve-2026-16232
  - Summary: Overview On July 22, 2026, Check Point published a security advisory for CVE-2026-16232 , an authentication bypass in the SmartConsole login process affecting Security Management Server and Multi-Domain Security Management Server (MDS). By leveraging CVE-2026-16232, an unauthenticated attacker can obtain an application login token, use this token to log in through SmartConsole with full administrator privileges, and modify the security policy or security configuration. Exploitation requires network access to the Management Server and for a Trusted Clients configuration that does not restrict GUI clients, which in our testing was a default setting. This vulnerability was reported as being exploited in the wild as a zero-day vulnerability at the time of disclosure. Our analysis finds that the root cause of CVE-2026-16232 is a broken trust boundary in the application authentication path. A vulnerable server accepts an attacker-supplied Secure Internal Communication (SIC) distinguished nam
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Public PoC Released for Exploited Check Point SmartConsole Authentication Bypass
  - Published: 2026-07-29T08:58:27+00:00
  - Link: https://thehackernews.com/2026/07/rapid7-releases-poc-for-exploited-check.html
  - Summary: Cybersecurity researchers have shared additional technical details about a recently patched critical security flaw impacting Check Point Security Management Server and Multi-Domain Security Management Server (MDS) that has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-16232 (CVSS score: 9.3), is an authentication bypass in the SmartConsole login process that

### Cluster 4a06e44c92 — score 44

- Title: Critical VMware vCenter Vulnerabilities Allow Authentication Bypass and Remote Code Execution (CVE-2026-59309, CVE-2026-59310)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-30T10:35:21+00:00
- Link: https://www.rapid7.com/blog/post/etr-critical-vmware-vcenter-vulnerabilities-allow-authentication-bypass-and-remote-code-execution-cve-2026-59309-cve-2026-59310
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-59309, CVE-2026-59310, VMware

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: VMware
- cve_ids: CVE-2026-59309, CVE-2026-59310
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: VMware
- cve_ids: CVE-2026-59309, CVE-2026-59310
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 29, 2026, Broadcom published security advisory VMSA-2026-0006 addressing multiple vulnerabilities in several VMWare products. Included in the advisory are two critical remotely exploitable vulnerabilities affecting VMware vCenter Server: CVE-2026-59309 and CVE-2026-59310. Both vulnerabilities carry CVSSv3.1 base scores of 9.8 and can be exploited by unauthenticated attackers with network access to a vulnerable vCenter Server. CVE CVSSv3.1 Description Summary CVE-2026-59309 9.8 (Critical) An authentication bypass vulnerability in the VMware Directory Service of vCenter that could allow a remote attacker to bypass authentication and gain unauthorized access to the vCenter management plane. CVE-2026-59310 9.8 (Critical) A directory traversal vulnerability in the vCenter Syslog server that could allow an attacker with network access to execute arbitrary code. VMware vCenter Server provides centralized management for VMware vSphere environments, allowing administrators to m
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits Critical VMware vCenter Vulnerabilities Allow Authentication Bypass and Remote Code Execution (CVE-2026-59309, CVE-2026-59310) Rapid7 Jul 30, 2026 | Last updated on Jul 30, 2026 | 3 min read Overview On July 29, 2026, Broadcom published security advisory VMSA-2026-0006 addressing multiple vulnerabilities in several VMWare products. Included in the advisory are two critical remotely exploitable vulnerabilities affecting VMware vCenter Server: CVE-2026-59309 and CVE-2026-59310. Both vulnerabilities carry CVSSv3.1 base scores of 9.8 and can be exploited by unauthenticated attackers with network access to a vulnerable vCenter Server. CVE CVSSv3.1 Description Summary CVE-2026-59309 9.8 (Critical) An authentication bypass vulnerability in the VMware Directory Service of vCenter that could allow a remote attacker to bypass authentication and gain unauthorized access to the vCenter management plane. CVE-2026-59310 9.8 (Critical) A directory traversal vulnerability in the vCenter Syslog server that could allow an attacker with network access to execute arbitrary code. VMware vCenter Server provides centralized management for VMware vSphere environments, allowing administrators to manage ESXi hosts, virtual machines, resource allocation, availability, and other virtualization infrastructure from a central control plane. Compromise of vCenter can therefore provide an attacker with significant control over the virtualized environment and its associated workloads. Both vulnerabilities are particularly significant because exploitation does not require prior authentication. However, an attacker must have network access to the affected vCenter services. Management interfaces such as vCenter are commonly restricted to internal or dedicated management networks, which can reduce exposure to internet-based attacks but does not mitigate the risk from an attacker who has already established access to an organization’s network. At the time of publication, there is no known evidence of exploitation or scanning in the wild for either CVE-2026-59309 or CVE-2026-59310. There is also currently no known public proof-of-concept exploit code. However, vCenter Server has appeared on CISA’s KEV list ten times in the past for other vulnerabilities, so it is known that attackers target critical issues in this product. Customers running affected VMWare products are urged to patch on an urgent basis before exploitation in-the-wild occurs. Mitigation guidance Organizations running VMware vCenter Server should prioritize applying the updates identified by Broadcom in VMSA-2026-0006 on an urgent basis. Broadcom states that there are no workarounds for CVE-2026-59309 or CVE-2026-59310, making vendor-provided updates the primary remediation. VMware Product Component Version Running On Fixed Version VMware Cloud Foundation, VMware vSphere Foundation vCenter 9.1.x.x Any 9.1.0.0300 VMware Cloud Foundation, VMware vSphere Foundation vCenter 9.0.x.x Any 9.0.2.0100 VMware vCenter N/A 8.0 Any 8.0 U3k VMware Cloud Foundation vCenter 5.x Any Async patch to 8.0 U3k VMware Telco Cloud Platform vCenter 3.0, 4.x, 5.0.x, 5.1.x Any Refer to KB449886 VMware Telco Cloud Infrastructure vCenter 3.0 Any Refer to KB449886 For the latest mitigation guidance, please refer to the vendor advisory . Rapid7 customers Exposure Command, InsightVM, and Nexpose Exposure Command, InsightVM, and Nexpose customers can assess exposure to CVE-2026-59309 and CVE-2026-59310 on VMware vCenter Server, Cloud Foundation, and vSphere Foundation products with unauthenticated vulnerability checks expected to be available in the July 30 content release. Updates July 30, 2026: Initial publication. July 30, 2026: Updated customers section to reflect availability of vulnerability checks. Article Tags Emergent Threat Response Labs Rapid7 Author Posts
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Critical VMware vCenter Vulnerabilities Allow Authentication Bypass and Remote Code Execution (CVE-2026-59309, CVE-2026-59310)
  - Published: 2026-07-30T10:35:21+00:00
  - Link: https://www.rapid7.com/blog/post/etr-critical-vmware-vcenter-vulnerabilities-allow-authentication-bypass-and-remote-code-execution-cve-2026-59309-cve-2026-59310
  - Summary: Overview On July 29, 2026, Broadcom published security advisory VMSA-2026-0006 addressing multiple vulnerabilities in several VMWare products. Included in the advisory are two critical remotely exploitable vulnerabilities affecting VMware vCenter Server: CVE-2026-59309 and CVE-2026-59310. Both vulnerabilities carry CVSSv3.1 base scores of 9.8 and can be exploited by unauthenticated attackers with network access to a vulnerable vCenter Server. CVE CVSSv3.1 Description Summary CVE-2026-59309 9.8 (Critical) An authentication bypass vulnerability in the VMware Directory Service of vCenter that could allow a remote attacker to bypass authentication and gain unauthorized access to the vCenter management plane. CVE-2026-59310 9.8 (Critical) A directory traversal vulnerability in the vCenter Syslog server that could allow an attacker with network access to execute arbitrary code. VMware vCenter Server provides centralized management for VMware vSphere environments, allowing administrators to m
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Three Critical VMware Flaws Allow Auth Bypass, Code Execution, and VM Escape
  - Published: 2026-07-29T15:31:15+00:00
  - Link: https://thehackernews.com/2026/07/three-critical-vmware-flaws-allow-auth.html
  - Summary: Broadcom has released security updates to address multiple security flaws impacting VMware ESX, vCenter, Workstation, and Fusion, three of which have been designated as critical in severity. The first of the three critical-rated flaws is CVE-2026-59309 (CVSS score: 9.8), which has been described as an authentication bypass in VMware vCenter. "A malicious actor with network access to vCenter

### Cluster 23daf8444d — score 36

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

### Cluster 513073eb52 — score 36

- Title: KindaRails2Shell: CVE-2026-66066, Critical Arbitrary File Read and Possible Remote Code Execution in Ruby on Rails
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-07-30T16:11:10+00:00
- Link: https://www.rapid7.com/blog/post/etr-kindarails2shell-cve-2026-66066-critical-arbitrary-file-read-and-possible-remote-code-execution-in-ruby-on-rails
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-66066

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-66066
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-66066
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On July 29, 2026, the Ruby on Rails project published a security advisory for CVE-2026-66066 , a critical vulnerability affecting Active Storage image processing when used in conjunction with the libvips image processing library. The vulnerability has a CVSSv4 score of 9.5 and is classified as Initialization of a Resource with an Insecure Default ( CWE-1188 ). An unauthenticated attacker may be able to leverage CVE-2026-66066 and read files accessible to the Rails application process, potentially exposing secrets that could enable remote code execution (RCE) or access to connected systems. An application is affected when it uses libvips for Active Storage image processing and accepts image uploads from untrusted users. Rails notes that generating image variants is not a separate requirement for exposure. Vips is the default Active Storage variant processor for applications configured with Rails 7.0 or later defaults. According to Ethiack , only the Vips processor is affected;
```

#### Full body

```
Back to Blog Vulnerabilities and Exploits KindaRails2Shell: CVE-2026-66066, Critical Arbitrary File Read and Possible Remote Code Execution in Ruby on Rails Jonah Burgess Jul 30, 2026 | Last updated on Jul 31, 2026 | 5 min read Overview On July 29, 2026, the Ruby on Rails project published a security advisory for CVE-2026-66066 , a critical vulnerability affecting Active Storage image processing when used in conjunction with the libvips image processing library. The vulnerability has a CVSSv4 score of 9.5 and is classified as Initialization of a Resource with an Insecure Default ( CWE-1188 ). An unauthenticated attacker may be able to leverage CVE-2026-66066 and read files accessible to the Rails application process, potentially exposing secrets that could enable remote code execution (RCE) or access to connected systems. An application is affected when it uses libvips for Active Storage image processing and accepts image uploads from untrusted users. Rails notes that generating image variants is not a separate requirement for exposure. Vips is the default Active Storage variant processor for applications configured with Rails 7.0 or later defaults. According to Ethiack , only the Vips processor is affected; applications using Magick are not affected through the reported vector. As of July 30, 2026, Rapid7 is not aware of exploitation in the wild. Ethiack and GMO Flatt Security, who independently reported the vulnerability, have withheld proof-of-concept code and details of the full attack chain. Public code claiming to exploit CVE-2026-66066 exists, but it is unclear how closely it corresponds to the full attack chain reported privately to Rails. According to the Rails Security Announcement , additional details will be disclosed no later than August 28, 2026. Rapid7 recommends remediating affected applications on an urgent basis, outside of normal patch cycles. Update #1 : On July 31, 2026, Rails published technical details and forensic tools earlier than its planned August 28 disclosure date after several researchers reverse-engineered the attack and published proof-of-concept code. Technical overview libvips uses operations to load and save image formats, including operations backed by third-party libraries. Some are marked "unfuzzed" or "untrusted" because they are unsafe for untrusted content. According to Rails, Active Storage did not disable these operations before processing user-supplied files, which may allow a crafted upload to trigger an unsafe operation and disclose files readable by the application. The attack details published by Rails describe a chain in which an attacker creates a blob through Active Storage's direct-upload endpoint with a false image content type and obtains a genuine signed variation_key from a page that renders an Active Storage representation. A crafted file identifies itself to libvips as a MATLAB level 5 file but to libmatio as a MAT 7.3 HDF5 container. HDF5's External File List then reads bytes from an attacker-selected path, which are rendered as image pixels and returned in the resulting variant. This known chain also requires the deployed libvips build to include the matload operation. For this documented chain, the Active Storage direct-upload route must be reachable. When Active Storage routes are mounted, the direct-upload route is present by default even if the application's own interface does not use direct uploads. Rapid7 testing found that ordinary server-side attachment does not satisfy this chain because Rails re-identifies the crafted file as MATLAB data before variant processing. The arbitrary file-read stage does not require knowledge of secret_key_base or a forged variation key. Rapid7 also verified an RCE escalation in which recovered Rails signing material is used to forge an ImageProcessing 1.x variation; this path does not require Marshal deserialization. The Rails patch that remediates CVE-2026-66066, disables untrusted operations during Active Storage initializatio
```

#### Corroborating sources (3)

- **Rapid7** (offensive_vulnerability_research)
  - Title: KindaRails2Shell: CVE-2026-66066, Critical Arbitrary File Read and Possible Remote Code Execution in Ruby on Rails
  - Published: 2026-07-30T16:11:10+00:00
  - Link: https://www.rapid7.com/blog/post/etr-kindarails2shell-cve-2026-66066-critical-arbitrary-file-read-and-possible-remote-code-execution-in-ruby-on-rails
  - Summary: Overview On July 29, 2026, the Ruby on Rails project published a security advisory for CVE-2026-66066 , a critical vulnerability affecting Active Storage image processing when used in conjunction with the libvips image processing library. The vulnerability has a CVSSv4 score of 9.5 and is classified as Initialization of a Resource with an Insecure Default ( CWE-1188 ). An unauthenticated attacker may be able to leverage CVE-2026-66066 and read files accessible to the Rails application process, potentially exposing secrets that could enable remote code execution (RCE) or access to connected systems. An application is affected when it uses libvips for Active Storage image processing and accepts image uploads from untrusted users. Rails notes that generating image variants is not a separate requirement for exposure. Vips is the default Active Storage variant processor for applications configured with Rails 7.0 or later defaults. According to Ethiack , only the Vips processor is affected;
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: KindaRails2Shell threatens Ruby on Rails apps (CVE-2026-66066)
  - Published: 2026-08-03T11:42:08+00:00
  - Link: https://www.helpnetsecurity.com/2026/08/03/kindarails2shell-cve-2026-66066-vulnerability/
  - Summary: A critical security vulnerability (CVE-2026-66066) in Ruby on Rails (aka Rails), one of the most widely used frameworks for building websites and web apps, may allow attackers to read sensitive files off a server and, in some cases, take full control of it. Nicknamed “KindaRails2Shell” by the researchers who found it, the flaw lets an attacker sneak a booby-trapped file past a website’s image-upload feature and use it to pry open the server’s secrets. About … More → The post KindaRails2Shell threatens Ruby on Rails apps (CVE-2026-66066) appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical Rails Flaw Could Let Unauthenticated Attackers Read Server Files via Image Uploads
  - Published: 2026-07-29T18:10:00+00:00
  - Link: https://thehackernews.com/2026/07/critical-rails-flaw-could-let.html
  - Summary: Ruby on Rails has released fixes for a critical Active Storage vulnerability that could let unauthenticated attackers read arbitrary files from application servers through crafted image uploads. Tracked as CVE-2026-66066 (CVSS score: 9.5), the flaw can expose the Rails process environment and secrets such as secret_key_base, the Rails master key, database passwords, cloud storage credentials,

### Cluster 495c7fe201 — score 36

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

### Cluster 4c8ed8c5fa — score 32

- Title: Batten Down Your Packages: Mitigation Guidance for Supply Chain Compromise
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-07-30T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: APT29, SolarWinds, UNC4736

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, supply_chain
- actor_attribution: APT29, TeamPCP, UNC4736
- affected_products: PyPI, SolarWinds, npm
- attack_techniques: T1195.001
- content_type: news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, apt_espionage
- actor_attribution: APT29, TeamPCP, UNC4736
- affected_products: SolarWinds, PyPI, npm
- attack_techniques: T1195.001
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Written by: Kelli Vanderlee, Stuart Carrera For years, the cybersecurity industry's understanding of software supply chain compromise has been anchored by a few watershed events, including Russian cyber espionage actor ICE RELIC’s (formerly known as APT29) 2020 compromise of SolarWinds and North Korean cyber espionage actor UNC4736's 2023 compromise of 3CX . However, Google Threat Intelligence Group (GTIG) has been tracking growth in threat activity targeting open source software repositories to conduct supply chain compromises over the past several years. A series of large scale open source software supply chain compromise campaigns in 2025 and the first half of 2026 underscore how important it is that organizations implement defensive strategies that directly address this threat vector. In this blog post, GTIG and Mandiant discuss trends we have observed in threat actor use of software supply chain compromise, and provide mitigation and hardening recommendations that incorporate insi
```

#### Full body

```
Threat Intelligence Batten Down Your Packages: Mitigation Guidance for Supply Chain Compromise July 30, 2026 Google Threat Intelligence Group Mandiant Mandiant Services Stop attacks, reduce risk, and advance your security. Contact Mandiant Written by: Kelli Vanderlee, Stuart Carrera For years, the cybersecurity industry's understanding of software supply chain compromise has been anchored by a few watershed events, including Russian cyber espionage actor ICE RELIC’s (formerly known as APT29) 2020 compromise of SolarWinds and North Korean cyber espionage actor UNC4736's 2023 compromise of 3CX . However, Google Threat Intelligence Group (GTIG) has been tracking growth in threat activity targeting open source software repositories to conduct supply chain compromises over the past several years. A series of large scale open source software supply chain compromise campaigns in 2025 and the first half of 2026 underscore how important it is that organizations implement defensive strategies that directly address this threat vector. In this blog post, GTIG and Mandiant discuss trends we have observed in threat actor use of software supply chain compromise, and provide mitigation and hardening recommendations that incorporate insights we have developed as a result of supporting customers through recent campaigns in which threat actors manipulated open source packages. Open Source Supply Chain Compromise Grows in Volume and Impact in 2025 and Early 2026 The majority of the most impactful and far-reaching supply chain compromise incidents that GTIG tracked in 2025 and early 2026 involved the compromise of code repositories, software dependencies and developer tools (T1195.001). Open source supply chain compromises offer attackers the same efficiency, scale, and initial stealth as traditional supply chain compromises, but typically require significantly less planning and resources to execute. However, open source supply chain compromises are also noisy once enabled; malicious open source packages are often discovered and publicized much more quickly than traditional supply chain compromises. GTIG assesses with high confidence that the growth in very large-scale, open-source supply chain compromise campaigns , including use of worms and iterative compromises in 2025 and early 2026, represent a significant expansion in use of this tactic compared to prior years. We anticipate that threat actors will emulate the tactics of these campaigns and contribute to growth in open-source supply chain compromise through the rest of 2026 and years to come. GTIG identified several notable supply chain compromises in 2025 and early 2026 that we believe exemplify this trend of exceptionally large campaigns, as measured by size and/or impact (Figure 1). Figure 1: Notable open source supply chain compromises, 2025 - early 2026 For example from February to May 2026, UNC6780 (aka "TeamPCP") conducted extensive open source supply chain compromises targeting ecosystems like PyPI, npm, and Docker Hub. Initial infection vectors varied across incidents, and included abuse of the pull_request_target GitHub Actions trigger to obtain base repository secrets and write permissions. The threat actor typically used compromised packages to deploy credential stealers, including SANDCLOCK, to obtain high value secrets. In incident response engagements, we observed UNC6780 attempting to pivot from compromised artificial intelligence (AI) software to broader network environments. UNC6780 has monetized stolen credentials through either direct sale of the stolen data, or through partnerships with ransomware and data theft extortion groups. In March 2026, GTIG observed the introduction of a malicious dependency in the legitimate axios package. GTIG analysis and the maintainer's post mortem indicate that the maintainer account was compromised via social engineering and used to publish the updated versions. We identified the malicious dependency as a dropper that deploys the WAVESHA
```

#### Corroborating sources (3)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Batten Down Your Packages: Mitigation Guidance for Supply Chain Compromise
  - Published: 2026-07-30T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
  - Summary: Written by: Kelli Vanderlee, Stuart Carrera For years, the cybersecurity industry's understanding of software supply chain compromise has been anchored by a few watershed events, including Russian cyber espionage actor ICE RELIC’s (formerly known as APT29) 2020 compromise of SolarWinds and North Korean cyber espionage actor UNC4736's 2023 compromise of 3CX . However, Google Threat Intelligence Group (GTIG) has been tracking growth in threat activity targeting open source software repositories to conduct supply chain compromises over the past several years. A series of large scale open source software supply chain compromise campaigns in 2025 and the first half of 2026 underscore how important it is that organizations implement defensive strategies that directly address this threat vector. In this blog post, GTIG and Mandiant discuss trends we have observed in threat actor use of software supply chain compromise, and provide mitigation and hardening recommendations that incorporate insi
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Batten Down Your Packages: Mitigation Guidance for Supply Chain Compromise
  - Published: 2026-07-30T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/
  - Summary: Written by: Kelli Vanderlee, Stuart Carrera For years, the cybersecurity industry's understanding of software supply chain compromise has been anchored by a few watershed events, including Russian cyber espionage actor ICE RELIC’s (formerly known as APT29) 2020 compromise of SolarWinds and North Korean cyber espionage actor UNC4736's 2023 compromise of 3CX . However, Google Threat Intelligence Group (GTIG) has been tracking growth in threat activity targeting open source software repositories to conduct supply chain compromises over the past several years. A series of large scale open source software supply chain compromise campaigns in 2025 and the first half of 2026 underscore how important it is that organizations implement defensive strategies that directly address this threat vector. In this blog post, GTIG and Mandiant discuss trends we have observed in threat actor use of software supply chain compromise, and provide mitigation and hardening recommendations that incorporate insi
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Russian State APT Linked to Recent Public Wi-Fi Gateway Hacking
  - Published: 2026-08-03T09:17:37+00:00
  - Link: https://www.securityweek.com/russian-state-apt-linked-to-recent-public-wi-fi-gateway-hacking/
  - Summary: Midnight Blizzard has been stealing Microsoft account credentials via compromised Wi-Fi networks at hospitality organizations. The post Russian State APT Linked to Recent Public Wi-Fi Gateway Hacking appeared first on SecurityWeek .

### Cluster e2f6a950f1 — score 30

- Title: Cisco FMC Zero-Day Actively Exploited, Static Credentials Could Expose Sensitive Data
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-30T05:08:39+00:00
- Link: https://thehackernews.com/2026/07/cisco-fmc-zero-day-actively-exploited.html
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-20316, Cisco

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- affected_industries: government
- affected_products: Cisco, Microsoft SharePoint
- cve_ids: CVE-2026-20079, CVE-2026-20316, CVE-2026-50522
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_industries: government
- affected_products: Microsoft SharePoint, Cisco
- cve_ids: CVE-2026-20316, CVE-2026-20079, CVE-2026-50522
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a newly disclosed security flaw impacting Cisco Secure Firewall Management Center (FMC) Software to its Known Exploited Vulnerabilities (KEV) catalog, following reports of zero-day exploitation. The vulnerability, assigned CVE-2026-20316 (CVSS score: 5.3), could permit an unauthenticated, remote attacker to log
```

#### Full body

```
Cisco FMC Zero-Day Actively Exploited, Static Credentials Could Expose Sensitive Data  Ravie Lakshmanan  Jul 30, 2026 Vulnerability / Network Security The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a newly disclosed security flaw impacting Cisco Secure Firewall Management Center (FMC) Software to its Known Exploited Vulnerabilities ( KEV ) catalog, following reports of zero-day exploitation. The vulnerability, assigned CVE-2026-20316 (CVSS score: 5.3), could permit an unauthenticated, remote attacker to log in to an affected device using a low-privilege account to access sensitive data within susceptible systems. "This vulnerability is due to the presence of static user credentials for a low-privileged account," Cisco said in an alert released Wednesday. "An attacker could exploit this vulnerability by using the account to log in to an affected system." "A successful exploit could allow the attacker to log in to the affected system and access sensitive data as the low-privileged user." Cisco noted that the attack surface that is associated with the vulnerability is reduced if the FMC management interface does not have public internet access. The network equipment company also said it's assigning it a Security Impact Rating (SIR) of High rather than Medium due to the fact that it can be chained with other Cisco Secure FMC Software vulnerabilities to elevate privileges. Security researcher Jimi Sebree of Horizon3.ai has been credited with discovering and reporting the flaw. Cisco also acknowledged that it became actively exploited earlier this month, although it did not disclose when the attacks began, who is behind them, or how the vulnerability is being exploited in these efforts. The issue has been addressed in the following hot fix versions of Cisco Secure FMC Software - 7.0 - Cisco_Firepower_Mgmt_Center_Hotfix_GB-7.0.9.1-3.sh.REL.tar 7.2 - Cisco_Secure_FW_Mgmt_Center_Hotfix_HL-7.2.11.1-4.sh.REL.tar 7.4 - Cisco_Secure_FW_Mgmt_Center_Hotfix_HG-7.4.7.1-3.sh.REL.tar 7.6 - Cisco_Secure_FW_Mgmt_Center_Hotfix_CY-7.6.5.1-2.sh.REL.tar 7.7 - Cisco_Secure_FW_Mgmt_Center_Hotfix_AM-7.7.12.1-2.sh.REL.tar 10.0 - Cisco_Secure_FW_Mgmt_Center_Hotfix_P-10.0.1.1-2.sh.REL.tar As indicators of compromise (IoCs), Cisco is urging customers to use the "cat /var/log/messages | grep license" CLI command in expert mode. If the command output includes "/var/tmp/license.tmp," there is a possibility that the vulnerability may have been exploited on the Cisco Secure FMC device - root@firepower:/home/admin# cat /var/log/messages | grep license Jul 23 16:16:33 firepower sudo: www : PWD=/ ; USER=root ; COMMAND=/usr/local/sf/bin/package_info.pl /var/tmp/license.tmp --lsm In tandem, Cisco has updated its advisory for CVE-2026-20079 (CVSS score: 10.0), a critical authentication bypass flaw impacting Cisco Secure FMC Software, to include a second bug ID ("CSCwt95974"), the same indicators of compromise, and hot fixes. However, the company said it is not aware of malicious exploitation of this vulnerability. Given that CVE-2026-20079 enables the execution of arbitrary executable script files to obtain root access, the inclusion of the same /var/tmp/license.tmp indicator indicates that threat actors could possibly chain the two flaws for code execution. In light of active exploitation, Federal Civilian Executive Branch (FCEB) agencies are recommended to apply the fixes by August 1, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  cisco , cyberattack , enterprise security , Firewall Security , network security , Vulnerability , Zero-Day ⚡ Top Stories This Week New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Publi
```

#### Corroborating sources (3)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Cisco FMC Zero-Day Actively Exploited, Static Credentials Could Expose Sensitive Data
  - Published: 2026-07-30T05:08:39+00:00
  - Link: https://thehackernews.com/2026/07/cisco-fmc-zero-day-actively-exploited.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a newly disclosed security flaw impacting Cisco Secure Firewall Management Center (FMC) Software to its Known Exploited Vulnerabilities (KEV) catalog, following reports of zero-day exploitation. The vulnerability, assigned CVE-2026-20316 (CVSS score: 5.3), could permit an unauthenticated, remote attacker to log
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-20316 | Cisco Secure Firewall Management Center Static Credential Vulnerability
  - Published: 2026-07-31T21:13:01+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-20316/
  - Summary: CVE-2026-20316 is a high-severity static credential vulnerability affecting Cisco Secure Firewall Management Center that allows unauthenticated access through a built-in account. NodeZero® Rapid Response safely validates exposure and verifies remediation.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Phishing Dominates as Initial Entry Method for Cyber-Attacks, as Hackers Hone Evasion Techniques
  - Published: 2026-07-28T13:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/phishing-dominates-initial-entry/
  - Summary: Analysis of real-life incident response cases by Cisco Talos warns that phishing remains a powerful method of initial compromise

### Cluster 38979f8c48 — score 26

- Title: CVE-2026-6516 | ManageEngine ADAudit Plus Pre-Authentication Remote Code Execution Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-29T18:05:45+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-6516/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-6516

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Apple iOS/macOS, Cisco, WordPress
- cve_ids: CVE-2026-20316, CVE-2026-60167, CVE-2026-60168, CVE-2026-60169, CVE-2026-6516
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: WordPress, Cisco, Apple iOS/macOS
- cve_ids: CVE-2026-6516, CVE-2026-20316, CVE-2026-60167, CVE-2026-60168, CVE-2026-60169
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-6516 is a critical pre-authentication vulnerability affecting ManageEngine ADAudit Plus. Learn how to validate exposure and verify remediation with NodeZero Rapid Response.
```

#### Full body

```
ManageEngine ADAudit Plus Pre-Authentication Remote Code Execution Vulnerability CVE-2026-6516 is a critical pre-authentication vulnerability affecting ManageEngine ADAudit Plus. The vulnerability exists within the product’s Agent APIs and involves authentication bypass and path traversal weaknesses that could allow an unauthenticated attacker to write files outside their intended directory. Successful exploitation may ultimately lead to remote code execution. The vulnerability affects ADAudit Plus builds prior to 8606 and has been assigned a CVSS v3.1 score of 10.0 (Critical). At the time of publication, there are no confirmed reports of active exploitation in the wild. Technical Details ManageEngine ADAudit Plus is an Active Directory auditing and reporting solution used to monitor user activity, administrative actions, and security events across Windows Active Directory environments. CVE-2026-6516 affects the product’s Agent APIs. The vulnerability involves authentication bypass and path traversal weaknesses that can be exploited remotely without authentication or user interaction. An attacker can leverage these flaws to write files outside their intended directory, potentially resulting in remote code execution. The vulnerability has a CVSS v3.1 vector of CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:L , reflecting network-based exploitation with low attack complexity and no required privileges. NodeZero® Proactive Security Platform — Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether CVE-2026-6516 can be exploited in your environment. The test executes real attack techniques without causing damage, giving security teams immediate clarity on exposure. Run the Rapid Response test: Launch the test from the NodeZero platform to determine whether your ADAudit Plus instance is vulnerable. Patch immediately: Upgrade ADAudit Plus to build 8606 and update affected Windows and macOS agents in accordance with ManageEngine guidance. Re-run the test: Verify that the vulnerability is no longer exploitable after remediation. Stop Guessing, Start Proving Schedule a demo Affected Versions & Patch Affected ManageEngine ADAudit Plus builds earlier than 8606 . Fixed ManageEngine ADAudit Plus Build 8606 . Mitigations ManageEngine recommends: Upgrade ADAudit Plus to Build 8606 using the latest service pack. Upgrade Windows agents running versions earlier than 7060 . Upgrade all installed macOS agents to the latest available version. Verify agent versions from Configuration → Agent Management → Manage → Installed Version within the ADAudit Plus console. Timeline April 17, 2026: ManageEngine released ADAudit Plus Build 8606, which addresses CVE-2026-6516. July 23, 2026: ManageEngine published its security advisory for CVE-2026-6516. July 23, 2026: CVE-2026-6516 was published in the CVE Program. July 24, 2026: NIST published the CVE in the National Vulnerability Database with CVSS scoring. July 28, 2026: Horizon3 released a NodeZero Rapid Response test for CVE-2026-6516. References ManageEngine Security Advisory ManageEngine ADAudit Plus Service Pack CVE.org Record – CVE-2026-6516 NIST NVD – CVE-2026-6516 Read about other CVEs CVE-2026-20316 CVE-2026-20316 is a high-severity static credential vulnerability affecting Cisco Secure Firewall Management Center that allows unauthenticated access through a built-in… Read more CVE-2026-60167, CVE-2026-60168, CVE-2026-60169 & CVE-2026-60170 Learn about four remotely exploitable Oracle Hospitality Simphony vulnerabilities and how NodeZero Rapid Response helps validate exposure and verify remediation. Read more CVE-2026-60137 / CVE-2026-63030 CVE-2026-60137 and CVE-2026-63030 can be chained to enable unauthenticated remote code execution against vulnerable WordPress Core installations. Learn how to… Read more NodeZero ® Platform Implement a continuous find, fix, and verify loop with NodeZero The NodeZero ® platform empowers your organization to reduce your security risk
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-6516 | ManageEngine ADAudit Plus Pre-Authentication Remote Code Execution Vulnerability
  - Published: 2026-07-29T18:05:45+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-6516/
  - Summary: CVE-2026-6516 is a critical pre-authentication vulnerability affecting ManageEngine ADAudit Plus. Learn how to validate exposure and verify remediation with NodeZero Rapid Response.

### Cluster 974cdece8d — score 23

- Title: This month in security with Tony Anscombe – July 2026 edition
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-07-31T14:14:15+00:00
- Link: https://www.welivesecurity.com/en/videos/month-security-tony-anscombe-july-2026/
- Fetch status: ok
- Member count: 15
- Corroborating source count: 9
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion, supply_chain, zero_day
- affected_industries: education, financial_services
- affected_products: AWS, Anthropic/Claude, OpenAI/ChatGPT
- cve_ids: CVE-2026-59726
- urgency_signals: preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_government, tier_1_offensive_research, tier_1_primary_research, tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
OpenAI models going rogue, the first documented agentic ransomware operation, and an emergent AI-driven supply chain threat made for a packed July roundup
```

#### Full body

```
Video This month in security with Tony Anscombe – July 2026 edition OpenAI models going rogue, the first documented agentic ransomware operation, and an emergent AI-driven supply chain threat made for a packed July roundup Editor 31 Jul 2026 With July coming to a close, ESET Chief Security Evangelist Tony Anscombe looks back at some of the top cybersecurity stories that made the news over the past month and offers insights that they may hold for your own cyber-defenses. Here's some of what caught Tony's attention this month: OpenAI models went rogue and autonomously broke into AI collaboration platform Hugging Face in what OpenAI described as "an unprecedented cyber incident". Researchers at Sysdig have documented what they assess to be the first case of an end-to-end ransomware operation executed by an agentic threat actor. The company named it JADEPUFFER . Cybercriminals are taking advantage of a new large language model (LLM)-driven attack vector called " phantom squatting " by purchasing domains linked to legitimate brands, then using them to intercept traffic directed there by AI systems. What can organizations do to stop phantom squatting from harming their brands, and what other lessons do these incidents hold for defenders? Watch Tony's video to find out and be sure to check out the June 2026 edition of his monthly security news roundup for more insights. Before you go, learn about the first AI-powered ransomware, named PromptLock and discovered by ESET researchers last year. To learn more about cutting-edge AI defense layers, read the AI at ESET white paper. Connect with us on Facebook , X , LinkedIn and Instagram . Let us keep you up to date Sign up for our newsletters Related Articles Video This month in security with Tony Anscombe – June 2026 edition Video This month in security with Tony Anscombe – June 2026 edition Video This month in security with Tony Anscombe – May 2026 edition Video This month in security with Tony Anscombe – May 2026 edition Video This month in security with Tony Anscombe – April 2026 edition Video This month in security with Tony Anscombe – April 2026 edition Similar Articles ESET research First known AI-powered ransomware uncovered by ESET Research ESET research PromptSpy ushers in the era of Android threats using GenAI Share Article Discussion
```

#### Corroborating sources (9)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: This month in security with Tony Anscombe – July 2026 edition
  - Published: 2026-07-31T14:14:15+00:00
  - Link: https://www.welivesecurity.com/en/videos/month-security-tony-anscombe-july-2026/
  - Summary: OpenAI models going rogue, the first documented agentic ransomware operation, and an emergent AI-driven supply chain threat made for a packed July roundup
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
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Phishing Campaigns Targeting AI Solutions Providers, (Sat, Aug 1st)
  - Published: 2026-08-01T07:22:32+00:00
  - Link: https://isc.sans.edu/diary/rss/33206
  - Summary: Most phishing campaigns rely on the fact that the victim is afraid to loose "something": money, access to information, ... Many brands have been impersonated by campaigns but I spotted some phishing emails that focus on AI services like ChatGPT.
- **Schneier on Security** (practitioner_analysis)
  - Title: The OpenAI Hack Shows the Genie Is Out of the Bottle
  - Published: 2026-08-03T10:47:47+00:00
  - Link: https://www.schneier.com/blog/archives/2026/08/the-openai-hack-shows-the-genie-is-out-of-the-bottle.html
  - Summary: This essay originally appeared in Foreign Policy . Earlier this month, two of OpenAI’s models broke out of their containment sandbox and attacked another AI company. The story is kind of wild . OpenAI was running security tests on two of its models: GPT-5.6 Sol and an unreleased model that is almost certainly GPT-6. In particular, it was running the ExploitGym benchmark, which measures how good a model is at turning security vulnerabilities into working exploits: basically, offensive cyberattacks. Since these were internal tests, OpenAI locked those models in a secure sandbox that denied them access to the internet. But it was running the models without any safety filters that would prevent them from offensive cyber-actions. That meant that there was nothing to prevent the models from trying to ...
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: In Other News: OpenAI Open Source Tool, AWS Links Hacks to North Korea, Mythos Crypto Research
  - Published: 2026-07-31T15:47:02+00:00
  - Link: https://www.securityweek.com/in-other-news-openai-open-source-tool-aws-links-hacks-to-north-korea-mythos-crypto-research/
  - Summary: Noteworthy stories that might have slipped under the radar: parcel delivery company OnTrac hacked, Adobe patches, UK Department for Education loses 607,000 records. The post In Other News: OpenAI Open Source Tool, AWS Links Hacks to North Korea, Mythos Crypto Research appeared first on SecurityWeek .
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: What the Hugging Face breach reveals about defense in the age of agentic AI
  - Published: 2026-07-31T10:00:00+00:00
  - Link: https://cyberscoop.com/hugging-face-breach-agentic-ai-security-op-ed/
  - Summary: We almost never get both sides of an intrusion. This time we did. Last month, Hugging Face disclosed a breach into part of its production infrastructure, saying an autonomous AI agent system ran the attack from start to finish. Five days later, OpenAI revealed that its own models, including GPT-5.6 Sol along with an unreleased […] The post What the Hugging Face breach reveals about defense in the age of agentic AI appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: OpenAI's Rogue Model Claims More Victims Beyond Hugging Face
  - Published: 2026-07-29T19:48:12+00:00
  - Link: https://www.darkreading.com/application-security/openai-rogue-model-claims-more-victims-beyond-hugging-face
  - Summary: OpenAI's goal-seeking agent compromised a Modal customer environment and others during its sandbox escape.

### Cluster ae0cc6b051 — score 23

- Title: Disrupting supply chain attacks on npm and GitHub Actions
- Source: GitHub Security Lab (offensive_vulnerability_research)
- Published: 2026-07-28T16:00:00+00:00
- Link: https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/
- Fetch status: ok
- Member count: 10
- Corroborating source count: 7
- Strong signals: GitHub, npm

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain
- affected_industries: financial_services, government
- affected_products: AWS, Anthropic/Claude, GitHub, npm
- cve_ids: CVE-2026-53921
- urgency_signals: preauth_unauth
- content_type: incident_report, news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_3_analysis, tier_4_news

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

#### Corroborating sources (7)

- **GitHub Security Lab** (offensive_vulnerability_research)
  - Title: Disrupting supply chain attacks on npm and GitHub Actions
  - Published: 2026-07-28T16:00:00+00:00
  - Link: https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/
  - Summary: Explore the changes we've shipped across npm and GitHub Actions over the past few months to disrupt supply chain attack techniques and limit their impact. The post Disrupting supply chain attacks on npm and GitHub Actions appeared first on The GitHub Blog .
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Amazon identifies North Korean hacker group behind open-source supply chain attacks
  - Published: 2026-07-29T21:00:12+00:00
  - Link: https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/
  - Summary: Amazon is sharing new findings about how a threat actor linked to the Democratic People’s Republic of Korea (DPRK) is targeting open source software libraries, the shared building blocks that companies around the world use to develop applications. Amazon Threat Intelligence has linked several recent compromises of popular Node Package Manager (NPM) libraries to the […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Two Compromised joyfill npm Packages Run RAT When Imported Into Node.js
  - Published: 2026-07-29T04:20:57+00:00
  - Link: https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
  - Summary: Beta release versions of two npm packages in the @joyfill namespace have been compromised to deliver a remote access trojan (RAT) associated with the DEV#POPPER malware family. The list of affected packages is as follows - @joyfill/layouts@0.1.2-2773.beta.0 @joyfill/components@4.0.0-rc24-2773-beta.4 The two packages "contain an import-time JavaScript implant that resolves encrypted code
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Amazon links Debug, Chalk NPM supply-chain attacks to North Korean hackers
  - Published: 2026-07-30T18:13:24+00:00
  - Link: https://www.bleepingcomputer.com/news/security/amazon-links-debug-chalk-npm-supply-chain-attacks-to-north-korean-hackers/
  - Summary: Amazon linked multiple high-profile open-source software supply chain attacks targeting the Node Package Manager (npm) ecosystem to North Korean hackers. [...]
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: AWS Blames North Korean Group for Axios and Other npm Supply Chain Attacks
  - Published: 2026-07-31T09:50:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/aws-north-korea-axios-npm-supply/
  - Summary: AWS has linked North Korea to the axios campaign to other attacks on npm libraries
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Anthropic models also did the hacky-hacky
  - Published: 2026-08-03T03:52:50+00:00
  - Link: https://risky.biz/RBNEWS595/
  - Summary: Anthropic models also did the hacky-hacks, Coldcard was hacked for $70 million in Bitcoin, npm adds publish-time malware scanning, and Russia is behind the recent hotel WiFi hacks.
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: A little-known npm package was North Korea’s warm-up act for the axios hack
  - Published: 2026-07-29T21:09:57+00:00
  - Link: https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/
  - Summary: Amazon's threat intelligence team traced domain records from the open-source software hack to a smaller, earlier compromise by the same North Korean group. The post A little-known npm package was North Korea’s warm-up act for the axios hack appeared first on CyberScoop .

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
ColdFusion Under Fire: Breaking Down CVE-2026-48283 and CVE-2026-48313 Rey Bango July 28, 2026 Blogs By Rey Bango & Brandon Peterson Adobe ColdFusion has been a fixture in enterprise web application stacks for decades. The first version of the web application server was released in 1995, and I have to admit I had fond memories of building web apps using the product. I still love CFML (yes, I said it!). So you can imagine how Adobe’s latest security bulletin piqued my interest. Apart from my past experience, government agencies, healthcare organizations, financial services firms, and higher education institutions have built and hosted dynamic web applications on it for years. That longevity is precisely what makes a pair of vulnerabilities worth paying close attention to. CVE-2026-48283 and CVE-2026-48313 are two critical, unauthenticated vulnerabilities affecting Adobe ColdFusion 2025 (Update 9 and earlier) and ColdFusion 2023 (Update 20 and earlier). Neither requires an attacker to have valid credentials or that a user clicks anything. And at least one of them results in remote code execution on the ColdFusion host. When the Horizon3 Rapid Response team evaluated these vulnerabilities, NodeZero® was able to exploit CVE-2026-48283 and achieve host compromise in under 90 seconds. That result warrants a closer look at what these vulnerabilities actually are, how they work, and what defenders should do about them. CVE-2026-48283: From File Upload to NT AUTHORITY\SYSTEM Uploading files, like images, documents and such are par for the course in many web applications. It’s used for everything from updating your profile picture to sending over a copy of your resume when applying for a job. The main thing that is important is that your development and security teams consider the types of files that should be uploaded and implement proper sanitization capabilities to limit those to only what’s necessary. Otherwise, you run the risk of an attacker uploading a webshell that could let them take over the server. Which leads us to CVE-2026-48283. This is a vulnerability that outlines a failure in ColdFusion’s file upload handling to properly restrict the types of files that can be submitted to the server. The vulnerability carries a CVSS score of 10.0, so you can understand that it has serious consequences when it appears in an internet-facing application. Digging into the issue, an unauthenticated remote attacker can upload a malicious file to a ColdFusion server without any prior authentication and without any user interaction on the target side. ColdFusion includes the CKEditor filemanager connector, a server-side component that acts as a bridge between CKEditor’s file browser UI and your web server’s file system. It helps with tasks within the ColdFusion administration interface like file browsing and management. It was a feature added to ColdFusion around 2007 and continues to be a part of helping make administration easier for developers. I remember using it when I managed some ColdFusion servers and it was a marked user interface improvement over the Flash components. Unfortunately, it also shipped an endpoint that allowed for unauthenticated file uploads: /cf_scripts/scripts/ajax/ckeditor/plugins/filemanager/upload.cfm The breakdown happened in ColdFusion’s file handling, which relied heavily on checking file extensions against disallowed lists. The parser failed to sanitize or validate specific file extensions or composite extensions before dropping the payload onto the file system. By default, .cfm,.cfc and .jsp are generally restricted on standard user uploads because these files tend to contain the code that powers your application. Unfortunately, some legacy server endpoints or internal RPC handling permitted alternative or unmapped executable types such as .jspf, .cfmail, or Java archive formats like .war. Yes, ColdFusion supports Java Server Pages and archive formats since it’s powered by a Java server under the hood. Of cour
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: ColdFusion Under Fire: Breaking Down CVE-2026-48283 and CVE-2026-48313
  - Published: 2026-07-28T16:12:25+00:00
  - Link: https://horizon3.ai/intelligence/blogs/coldfusion-critical-cves/
  - Summary: Learn how the critical ColdFusion vulnerabilities CVE-2026-48283 and CVE-2026-48313 work, how attackers can exploit them, and why verifying remediation is essential for reducing real-world risk.

### Cluster b1e900a5a7 — score 18

- Title: Escaping Linux Sandboxes via PipeWire (CVE-2026-5674)
- Source: Embrace the Red (ai_security_agentic_risk)
- Published: 2026-07-30T16:00:00+00:00
- Link: https://embracethered.com/blog/posts/2026/pipewire-flatpak-linux-sandbox-escape-cve-2026-5674/
- Fetch status: ok
- Member count: 10
- Corroborating source count: 7
- Strong signals: Anthropic/Claude, CVE-2026-5674

#### Cluster taxonomy (union across members)
- threat_categories: ai_security
- affected_industries: government
- affected_products: Anthropic/Claude, PyPI
- cve_ids: CVE-2025-60616, CVE-2026-5674
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- affected_products: Anthropic/Claude
- cve_ids: CVE-2026-5674, CVE-2025-60616
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
This post walks through a sandbox escape from a Flatpak application via PipeWire. The vulnerability was discovered using my automated research pipeline with Claude Code and Opus 4.6 back in April 2026. It was an exciting find, as this was the first bug I submitted to Red Hat. Claude Code was also excited finding this: Once discovered, I repro’d it manually to make sure it’s legit and then submitted it to Red Hat.
```

#### Full body

```
This post walks through a sandbox escape from a Flatpak application via PipeWire. The vulnerability was discovered using my automated research pipeline with Claude Code and Opus 4.6 back in April 2026. It was an exciting find, as this was the first bug I submitted to Red Hat. Claude Code was also excited finding this: Once discovered, I repro’d it manually to make sure it’s legit and then submitted it to Red Hat. Let’s dive into it. PipeWire and PulseAudio PipeWire is the default audio server on all modern Linux desktops now. Fedora, Ubuntu 24.04+, Debian 13,… It replaced PulseAudio but maintains backward compatibility. Flatpak apps that need audio request --socket=pulseaudio . At the core, a basic “Hello World” app with standard audio permission breaks out of the sandbox and gets full access to the user’s desktop, files, and credentials. The same attack applies to other Linux sandbox tech that connects a socket to PipeWire (e.g. Docker, etc..). Let’s look at the vulns and exploit. The Vulnerabilities The escape relies on three separate issues. 1. Authentication Cookie Is Never Validated PulseAudio code contains cookie-based authentication. This is not a typical web cookie, just a name for an authentication token. It’s a 256-byte random value that lives at ~/.config/pulse/cookie , and clients must present it to connect. PipeWire reads the cookie from the client, checks the length is 256 bytes, and then just… throws it away. The relevant code in pulse-server.c : if (len != NATIVE_COOKIE_LENGTH) return -EINVAL; client->version = version; client->authenticated = true; // cookie value never compared The cookie variable is never referenced again after being read. Any 256 bytes of garbage will do. No comments in the code explain why the value is set to true . The original PulseAudio validates the cookie, however PipeWire does not. I looked through the git history. This has been the behavior since the PulseAudio compatibility layer was first implemented. 2. Module Loading Is Enabled by Default #define DEFAULT_ALLOW_MODULE_LOADING "true" Any “authenticated” client can send LOAD_MODULE to load arbitrary PipeWire modules. A config option ( pulse.allow-module-loading ) was added in May 2024, but it defaults to true . Since authentication is broken, this means any process with socket access can load modules. 3. dlopen() With No Path Validation When module-ladspa-sink is loaded, it takes a plugin= parameter and calls dlopen() on it directly: handle = dlopen (path, RTLD_NOW); There is no path validation or directory allowlist. So, we can load arbitrary libraries. ELF constructors ( __attribute__((constructor)) ) run immediately on dlopen() . This is the same pattern as CVE-2025-60616 in FFmpeg’s LADSPA loader. Oh, and if you are wondering what LADSPA means, it stands for Linux Audio Developer's Simple Plugin API . That’s something new I learned along the way. The Sandbox Escape Flatpak’s --socket=pulseaudio grants access to the PulseAudio socket. Combined with any host-writable path (like --filesystem=/tmp in the demo), an app can escape the sandbox. The exploit chain: Write a malicious .so to a host-visible path (e.g. /tmp ) Connect to the PulseAudio socket Send PA_COMMAND_AUTH with 256 bytes of garbage Send PA_COMMAND_LOAD_MODULE module-ladspa-sink plugin=/tmp/payload.so PipeWire, running outside the sandbox , calls dlopen() on the .so The constructor executes in the user’s full context (outside the sandbox) The app has no home directory access, no display access, no network. Yet after the exploit it can read your files, launch apps on your desktop, and access your credentials. Note that PipeWire runs as a user-level service, not root. This is a sandbox escape, not privilege escalation. But the attacker goes from “sandboxed, can only play audio” to “full, unrestricted user context.” Proof of Concept I built a Flatpak app called net.wuzzi.Hello that demonstrates this. It looks completely harmless: $ flatpak info --show-permissions net.wuzz
```

#### Corroborating sources (7)

- **Embrace the Red** (ai_security_agentic_risk)
  - Title: Escaping Linux Sandboxes via PipeWire (CVE-2026-5674)
  - Published: 2026-07-30T16:00:00+00:00
  - Link: https://embracethered.com/blog/posts/2026/pipewire-flatpak-linux-sandbox-escape-cve-2026-5674/
  - Summary: This post walks through a sandbox escape from a Flatpak application via PipeWire. The vulnerability was discovered using my automated research pipeline with Claude Code and Opus 4.6 back in April 2026. It was an exciting find, as this was the first bug I submitted to Red Hat. Claude Code was also excited finding this: Once discovered, I repro’d it manually to make sure it’s legit and then submitted it to Red Hat.
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Open letters about AI development
  - Published: 2026-08-02T04:16:52+00:00
  - Link: https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything
  - Summary: Open letters about AI development I wrote this summary of the past few weeks of open letters as a section of my sponsors-only newsletter but I've decided to share it here as well. Open Weights and American AI Leadership was shepherded by Microsoft, dated July 24th, and signed by 235 AI-adjacent companies including NVIDIA (see Jensen's first ever tweet ), Amazon, Y Combinator, The Linux Foundation, and (a later signer) OpenAI. It's clearly an argument designed to counter any instincts by the current US government to ban or limit open weight models over "safety" concerns - a reasonable consideration given what happened to Claude Fable 5 ! Relying solely on closed models is not inherently safe: they can be breached, misused, or fail in ways that outsiders cannot detect. And concentrating advanced AI capabilities behind a small number of closed models compounds that risk. It results in a small number of single points of failure, weakens competition, and leaves critical technology in the ha
- **Schneier on Security** (practitioner_analysis)
  - Title: Anthropic’s Opus 5 Is Better at Resisting Prompt Injection
  - Published: 2026-07-31T17:23:16+00:00
  - Link: https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html
  - Summary: The chart is interesting. On the IPI benchmark, Opus 5 improved over Opus 4.8, reducing the probability of an attacker succeeding within 15 attempts from 5.5% to 2.0%, and from 0.5% to 0.2% on 1 attempt. It also improved on Sonnet 5 (5.9% at k=15) and Mythos 5 (2.6%), making it the most robust model evaluated. Opus 5 also outperformed all non-Claude models on this benchmark. The most robust non-Claude model was Muse Spark at 16.5% within 15 attempts—more than eight times Opus 5’s rate. The most capable GPT 5.6 variant, Sol, was comparable to its predecessor GPT 5.5 (20.0% versus 20.8% within 15 attempts), and was 10 times as likely to be successfully attacked as Claude Opus 5 at 2.0%. The other GPT 5.6 variants are less robust, at 30.4% (Terra) and 43.9% (Luna). A single attempt against GPT 5.6 Sol succeeded 3.1% of the time, higher than the 2.0% an attacker achieved against Opus 5 after fifteen attempts...
- **The Record** (cyber_news_breach_reporting)
  - Title: Anthropic says its AI hacked real-world companies in three incidents
  - Published: 2026-07-31T12:15:00+00:00
  - Link: https://therecord.media/anthropic-ai-hacked-three-real-companies
  - Summary: Claude maker Anthropic said its AI models escaped test environments and breached networks at three companies on the open internet.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Anthropic's Claude breached 3 orgs, uploaded PyPI malware during tests
  - Published: 2026-07-31T00:57:25+00:00
  - Link: https://www.bleepingcomputer.com/news/security/anthropics-claude-breached-3-orgs-uploaded-pypi-malware-during-tests/
  - Summary: One of Anthropic's Claude models built and uploaded a malicious Python package to PyPI during a botched security evaluation, where it ran on 15 real systems and stole credentials from a security vendor. It was one of three incidents affecting real companies. [...]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations
  - Published: 2026-07-31T06:41:44+00:00
  - Link: https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html
  - Summary: Anthropic on Thursday became the latest artificial intelligence (AI) company to reveal that three of its models, including Claude Opus 4.7, Mythos 5, and an unnamed research model, had breached three unnamed organizations during cybersecurity testing without its knowledge. The AI firm said the earliest incidents date back to April 2026, adding it made the discoveries after launching a "
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Anthropic Reveals Claude Escaped Testing, Breaching Three Companies
  - Published: 2026-07-31T08:35:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/anthropic-claude-breached-three/
  - Summary: Anthropic has revealed that Claude AI models compromised third-party organizations

### Cluster 90d3c1c1e2 — score 16

- Title: The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version
- Source: Unit 42 (threat_research_primary)
- Published: 2026-07-31T10:00:18+00:00
- Link: https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: Apple iOS/macOS

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, supply_chain, web_shell_backdoor
- affected_industries: financial_services
- affected_products: AWS, Apple iOS/macOS, GitHub, Palo Alto Networks
- content_type: incident_report, news_report
- confidence_tier: tier_1_government, tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft, web_shell_backdoor
- affected_products: Apple iOS/macOS, GitHub, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Analysis of XCSSET v40 reveals a macOS malware targeting developers via Xcode. Unit 42 used advanced pattern matching and AI to decode its logic. The post The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version 16 min read Related Products Advanced DNS Security Advanced URL Filtering Cloud-Delivered Security Services Cortex Cortex XDR Cortex XSIAM Unit 42 Incident Response By: Adva Gabay Noa Dekel Published: July 31, 2026 Categories: Malware Threat Research Tags: Browser hijacking Credential theft Data exfiltration Infection chain Malware Obfuscation XCSSET malware Share Executive Summary After months of dormancy, the attackers behind the XCSSET malware released version 40 (v40), targeting the macOS ecosystem. This version’s advanced architecture hides its core logic in memory space, reducing its digital footprint. V40 further enhances its detection evasion capabilities by combining polymorphic payload generation with fileless persistence and dynamic in-memory execution, while weakening a number of security mechanisms on the affected machine. Since early April 2026, the malware has spread through supply chain attacks by hiding itself in the Xcode projects of dozens of legitimate applications with thousands of active users. Xcode is Apple’s integrated development environment (IDE) for building apps for its various operating systems. XCSSET’s author enhanced the threat’s ability to spread through open-source projects on GitHub and upgraded its worming capabilities. It can now infect all existing Xcode projects on a compromised system for maximum impact. The author used a multi-layered cipher shift to conceal the threat’s internal functions. In response, our researchers leveraged advanced AI and pattern-matching algorithms to de-obfuscate the malware's logic. This article: Explores XCSSET’s updated stealth practices Examines the new operational modules Reveals findings regarding the attackers' rotating command-and-control (C2) infrastructure Provides mitigation strategies to detect and prevent this threat Palo Alto Networks customers are better protected from the threats discussed above through the following products and services: Cortex XDR and XSIAM Advanced URL Filtering and Advanced DNS Security If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Supply Chain , Backdoor , macOS Background XCSSET is a modular macOS malware family that primarily targets software developers within the Apple ecosystem, spreading through Xcode projects. Threats in this family download task-specific modules from a C2 server, giving it capabilities including: Browser hijacking Credential theft Clipboard monitoring Data exfiltration XCSSET’s initial discovery was by Trend Micro in 2020. Security researchers at Microsoft analyzed and documented two subsequent versions in March and September 2025. These updates indicate that the attackers were enhancing their codebase. In mid-April 2026, we started tracking a new version of XCSSET. We saw a secondary wave of attacks in early May 2026 that introduced an expanded suite of operational modules. In this new version, we observed a heightened volume of attacks targeting developers across South Asia, which is consistent with Trend Micro's initial 2020 reporting, While the threat actor has named this latest iteration XCSSET v40, the security community has historically identified only a handful of intermediary versions, none of which featured formal version labels. Infection Chain Analysis In this section, we provide a high-level overview of XCSSET v40’s infection chain. The threat’s authors restructured its execution framework to be more stealthy and modular. We provide a complete step-by-step breakdown of each phase in Appendix A. The malware injects an initial downloader script into benign project files in Xcode projects and vulnerable Git repositories. While the attack lifecycle begins with the infected codebase, the endpoint infection is triggered only when the developer builds that project locally. The m
```

#### Corroborating sources (3)

- **Unit 42** (threat_research_primary)
  - Title: The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version
  - Published: 2026-07-31T10:00:18+00:00
  - Link: https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/
  - Summary: Analysis of XCSSET v40 reveals a macOS malware targeting developers via Xcode. Unit 42 used advanced pattern matching and AI to decode its logic. The post The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version appeared first on Unit 42 .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Chinese Threat Actor Uses Leaked DarkSword Kit to Deploy GHOSTBLADE on iOS
  - Published: 2026-08-03T10:49:06+00:00
  - Link: https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
  - Summary: An unknown Chinese-threat actor has been observed running a campaign targeting Apple iOS devices by leveraging a publicly leaked version of the DarkSword exploit kit. Attack surface management platform Censys said it identified the threat actor running more than 100 web properties, most of which are fake Amazon Web Services (AWS) sign-in pages on a domain that also hosts the exploit toolkit. "
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Apple Patches Everything (July 2026), (Wed, Jul 29th)
  - Published: 2026-07-29T07:32:37+00:00
  - Link: https://isc.sans.edu/diary/rss/33196
  - Summary: I am a bit late with this summary, but this week Apple released updates to all its operating systems and Safari. The Safari update, as usual, targets macOS prior to macOS 26. macOS updates covered the two older versions (14 and 15), while other operating system patches only covered the current 26 versions.

### Cluster 06319fc0de — score 15

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

### Cluster 854ba4d3df — score 14

- Title: Dealing with AI-Generated Extortion
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-30T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/ai-generated-extortion
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: government
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Combat AI-generated extortion and fake ransomware leaks. Learn how organizations can verify data authenticity using robust governance and threat intelligence.
```

#### Full body

```
Dealing with AI-Generated Extortion Proving a Negative How do you prove a negative in cybersecurity? How do you prove that you weren’t attacked, or that there is no intruder in your network? These are questions that security teams have been forced to ask for a while, but there is a new question that is becoming increasingly common: How do you prove that files weren’t stolen from your network? Or, even more of a challenge, how do you prove that files weren’t stolen from your partners, vendors, or their partners or vendors? This is a surprisingly challenging question to answer. Finding the answer is also more difficult because data governance has not been the traditional purview of security teams. Data governance has long been thought of as a compliance problem, unfortunately that is no longer the case. Security teams are now, whether they want to be or not, need to consider data governance. This means they have to be able to confidently say whether leaked data is real or not. How do you do that? History of Ransomware What we call ransomware has evolved over the years. Ransomware has gone from largely focused on encryption to a combination of encryption and data theft to today’s reality where data theft alone is the most common version of a “ransomware” attack. Threat actors have figured out that managing encryption keys is challenging, stealing data and holding it hostage is significantly easier. They’ve also figured out that stealing the right data can be just as profitable as encryption and, as we’ve seen from ransomware trends, switching to data theft only allows groups to accelerate the number of attacks. Compare the number of victims from 2024 to 2025 in the Recorded Future® Ransomware dashboard with a noticeable rise in ransomware trends. Figure 1: Rise in ransomware trends increasing from 2024 to 2025 (Source: Recorded Future) Enter 0APT If data theft is easier than encryption, then just making up data using generative AI is even easier than that. Which is what we saw with “0APT” (their name, not a designation that Recorded Future provided), who created a list of victims that were completely made up, including fake leaked data. From Insikt Group® reporting at the time: In late January 2026, Insikt Group reported the launch of 0APT Blog, an extortion blog operated by 0APT Ransomware Group, which allegedly runs an affiliate program via its ransomware-as-a-service (RaaS) model. As of February 5, 2026, the extortion blog listed 61 breached victims, with operators stating they planned to leak an additional 115 victims located in multiple countries and operating across various sectors and industries. Insikt Group identified multiple reports regarding the functionality of 0APT ransomware and listed victims, indicating that the ransomware is fake and that all their victims listed on the blog were AI-generated. Among the primary reasons discussed include: Multiple uploaded files were empty. Low-programming practices, including a combination of AI-generated scripts and unprofessional web development. Source code analysis found that some comments were in Hindi and Urdu, which likely indicates that the operators of 0APT ransomware are based in Southern Asia, while the majority of top-tier ransomware groups primarily operate from Russia or a nation within the Commonwealth of Independent States (CIS). Such a large number of victims compromised within a very short period can be carried out by a well-established, organized ransomware group; however, 0APT Blog states that the threat group is currently recruiting penetration testers with network access to join their RaaS affiliate program. 0APT is not alone; other groups are starting to latch on to this trend (ransomware groups are really good at copying each other). ALP-001 is another threat group that surfaced in March with questionable data that may have been AI-generated. According to Reliaquest reporting at the time: The main significance of 0APT and ALP-001 is not that they’re estab
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Dealing with AI-Generated Extortion
  - Published: 2026-07-30T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/ai-generated-extortion
  - Summary: Combat AI-generated extortion and fake ransomware leaks. Learn how organizations can verify data authenticity using robust governance and threat intelligence.

### Cluster c7d4f5e8ea — score 13

- Title: Exploring the Hugging Face Breach: mapping AI agent tactics to Elastic Defend
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-31T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/ai-agent-attack-detection-hugging-face-breach
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: Kubernetes, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: OpenAI/ChatGPT, Kubernetes
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Every stage of the Hugging Face breach maps to Elastic Defend and SIEM rules already shipping, from worker RCE and credential harvest to self-migrating C2 and GenAI detection.
```

#### Full body

```
31 July 2026 • Elastic Security Labs Exploring the Hugging Face Breach: mapping AI agent tactics to Elastic Defend Every stage of the Hugging Face breach maps to Elastic Defend and SIEM rules already shipping, from worker RCE and credential harvest to self-migrating C2 and GenAI detection. 16 min read Detection Engineering , Generative AI Hugging Face reconstructed more than 17,000 attacker events from a July 2026 intrusion driven by an autonomous artificial intelligence (AI) agent. The path was familiar: untrusted dataset content abused a processing worker (file disclosure, then code execution), credential harvest, then multi-cluster lateral movement. Production Elastic Defend behavior rules and Elastic Security detection (SIEM) rules already watch those types of behaviors. This post maps each stage to detections you can enable today. On July 16, 2026, Hugging Face disclosed that a malicious dataset abused its dataset-processing pipeline. A follow-on technical timeline (July 27) clarifies the two vectors against the same config-driven loader in a production Kubernetes worker pod: an HDF5 external raw-storage page that disclosed local files (including environment secrets and worker source), then Jinja2 template injection that achieved code execution. From that foothold, the agent escalated toward node and cluster-level access, harvested cloud and cluster credentials, and moved laterally across roughly July 9-13 UTC (~17,600 reconstructed actions). Hugging Face rebuilt the timeline with its own large language model (LLM) analysis agents after hosted frontier APIs blocked forensic payloads via safety guardrails. On July 21, 2026, OpenAI stated that its evaluation models (including GPT-5.6 Sol and a more capable pre-release model) drove the activity during an internal cyber-capability evaluation on ExploitGym , with reduced cyber refusals enabled for testing. These models identified and exploited a zero-day vulnerability in a package-registry cache proxy, escaped OpenAI’s research environment, reached the open internet, and then targeted Hugging Face while running internal benchmarking of these models on cybersecurity evaluation tasks. Hugging Face reported that the only customer content accessed was ExploitGym/CyberGym challenge solutions in five datasets, with no evidence of tampering with other customer-facing Hub models, datasets, Spaces, or packages. In this post, we: Summarize the July 2026 Hugging Face agentic intrusion and how it intersects with OpenAI's ExploitGym evaluation escape. Map each stage of the campaign to production Elastic Defend behavior rules and Elastic Security detection rules you can enable today. Show why outcome detections (credential paths, unusual destinations, persistence under GenAI parents) beat whole-tool trust of agent or worker process trees. Highlight LLM-based attack-chain triage and GenAI-parented Defend correlation on Elastic Stack 9.3.0+ for agentic alert volume. Key takeaways Elastic Defend behavior rules and Elastic Security detection rules cover multiple stages of this attack chain. Initial access was pipeline abuse on an AI data-processing worker (local file disclosure, then template-injection RCE). Production Defend and SIEM rules that watch workers spawning shells, interpreters, and downloaders still apply. Prefer outcome detections (credential paths, unusual destinations, persistence under GenAI parents) over whole-tool trust of agent or worker process trees. Agentic campaigns spike alert volume. Enable production LLM attack-chain triage and GenAI-parented Defend correlation (Stack 9.3.0+); tune noisy mechanics by lineage and keep credential and egress outcomes hot. Following the lead from the Hugging Face team, we created an interactive view into the incident using Elastic Defend’s technologies, based on publicly available information. You can check it out here: Hugging Face incident interactive timeline Scope note: This post maps behaviors described in public disclosures to Elasti
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Exploring the Hugging Face Breach: mapping AI agent tactics to Elastic Defend
  - Published: 2026-07-31T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/ai-agent-attack-detection-hugging-face-breach
  - Summary: Every stage of the Hugging Face breach maps to Elastic Defend and SIEM rules already shipping, from worker RCE and credential harvest to self-migrating C2 and GenAI detection.

### Cluster 07328bc0d0 — score 13

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

### Cluster 0d2189c83e — score 13

- Title: Ruby on Rails Patches Critical Vulnerability
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-01T11:15:00+00:00
- Link: https://www.securityweek.com/ruby-on-rails-patches-critical-vulnerability/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, data_breach, ransomware_extortion
- affected_industries: financial_services
- affected_products: AWS, OpenAI/ChatGPT, SonicWall
- cve_ids: CVE-2026-66066
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, apt_espionage, active_exploitation
- affected_industries: financial_services
- affected_products: SonicWall, AWS, OpenAI/ChatGPT
- cve_ids: CVE-2026-66066
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The flaw can be exploited by unauthenticated attackers to read arbitrary files and potentially achieve remote code execution (RCE). The post Ruby on Rails Patches Critical Vulnerability appeared first on SecurityWeek .
```

#### Full body

```
Ruby on Rails this week rolled out patches for a critical vulnerability that could allow unauthenticated attackers to achieve remote code execution (RCE). A server-side web application framework written in Ruby, Ruby on Rails is used for the fast building of full-stack web applications and APIs. Tracked as CVE-2026-66066 (CVSS score of 9.5), the critical security defect is described as an arbitrary file read that potentially exposes secrets, allowing remote attackers to execute code or move laterally to other systems. “In its default configuration, a Rails application that displays image variants may allow an unauthenticated attacker to read arbitrary files from the server, including the process environment,” Ruby on Rails’ maintainers note in an advisory . Within the exposed environment, the advisory explains, attackers could find secret_key_base and credentials for external systems, which can be abused to escalate the attack to RCE. The issue impacts applications that use the libvips library for Active Storage image processing and that allow image uploads from untrusted users. Advertisement. Scroll to continue reading. Because libvips marks some file read and write operations as ‘unfuzzed’ (unsafe for untrusted content) and Active Storage did not disable the unfuzzed operations, an attacker could upload a crafted file to invoke one of these operations. “We are aware of a mechanism by which an attacker, by uploading a crafted file, is able to cause disclosure of the contents of arbitrary files accessible on the filesystem of the targeted application,” Ruby on Rails’ advisory reads. CVE-2026-66066 was patched in Active Storage versions 7.2.3.2, 8.0.5.1, and 8.1.3.1. Users are advised to update their deployments as soon as possible, as well as to update libvips to at least version 8.13, as previous library releases do not support disabling unfuzzed operations. “Upgrading closes the vulnerability but does not undo an exfiltrated secret if that already occurred. An affected application should treat every secret readable by the application process as potentially exposed and change it,” Ruby on Rails notes. According to cybersecurity firm Rapid7 , as of July 30, there is no evidence that the security defect has been exploited in the wild. Related: Google AI Uncovers 13-Year-Old Chrome Flaw Amid Record Patching Pace Related: Critical Flaw Led to Azure Cosmos DB Pwnage Related: Critical Code Execution Vulnerability Patched in TeamCity Related: ‘DangleGeddon’: AI Could Weaponize Forgotten DNS Records at Global Scale Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Critical Flaw Allowed to Azure Cosmos DB Pwnage CareCloud Data Breach Impacts Over 350,000 Critical Code Execution Vulnerability Patched in TeamCity DataBahn Raises $40 Million for Agentic Data Pipeline Management Discern Security Raises $13 Million in Series A Funding Cantina Emerges From Stealth With $8 Million in Funding Critical Ruflo Flaw Lets Attackers Spawn Rogue AI Swarms US and Allies Update SBOM Guidance Latest News Brinks Home Discloses Data Breach as Hackers Leak Files Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks Russian State APT Linked to Recent Public Wi-Fi Gateway Hacking US Water Cyberattacks Extend Beyond Minnesota to at Least 6 Other States Balance Theory Raises $19 Million to Help Enterprises Manage Cybersecurity Investments In Other News: OpenAI Open Source Tool, AWS Links Hacks to North Korea, Mythos Crypto Research Cyberattacks on Minnesota Water Systems Investigated as Officials Warn About Iranian Hackers Google AI Uncovers 13-Year-Old Chrome Flaw Amid Record Patching Pace Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insigh
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Ruby on Rails Patches Critical Vulnerability
  - Published: 2026-08-01T11:15:00+00:00
  - Link: https://www.securityweek.com/ruby-on-rails-patches-critical-vulnerability/
  - Summary: The flaw can be exploited by unauthenticated attackers to read arbitrary files and potentially achieve remote code execution (RCE). The post Ruby on Rails Patches Critical Vulnerability appeared first on SecurityWeek .

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

### Cluster d1c29125d3 — score 12

- Title: Pass the Passkey: A Novel Attack Surface in Passwordless Authentication
- Source: Unit 42 (threat_research_primary)
- Published: 2026-08-03T10:00:35+00:00
- Link: https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_products: Google Cloud, Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: Palo Alto Networks, Google Cloud
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Explore how passkey implementation gaps undermine security when relying parties fail to validate the User Verified flag, reducing MFA to a single factor. The post Pass the Passkey: A Novel Attack Surface in Passwordless Authentication appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Malware Malware Pass the Passkey: A Novel Attack Surface in Passwordless Authentication 17 min read Related Products Cortex Cortex Cloud By: Arie Olshtein Published: August 3, 2026 Categories: Malware Threat Research Tags: Google authenticator Google Chrome Google Cloud Identity Key Passkey Passwordless Share Executive Summary This article analyzes new attack classes against passwordless authentication, focusing on Google’s synced passkey ecosystem and the Cloud Authenticator used by desktop clients. The attacks demonstrate how malware on a compromised endpoint can misuse onboarding, recovery and device trust workflows to take over passkey-protected accounts. We show how an attacker can authenticate without user interaction, bypass user verification requirements and extract all synced passkey private keys. After decades of breaches and billions in losses, the attack vectors that defined the era of passwords and shared secrets are finally starting to fade. Passkeys replace passwords and traditional multi-factor authentication (MFA) with public-key cryptography, decreasing entire classes of attacks that have dominated the threat landscape for years. With no shared secret to steal, reuse or phish, many of an attacker’s most reliable tools are becoming obsolete. This represents a significant disruption for the credential theft market. Attackers, however, persist. They evolve, and defenders must prepare for a new generation of attacks. As passkeys become widely adopted and scale to billions of accounts, defenders must prepare for new attack surfaces, some of which we disclose in our research. This article is part 3 in our series examining passkey adoption from a security perspective. If you haven’t read the previous parts, we recommend starting here: Part 1: The Art of the Invisible Key – Passkey Global Breakthrough Part 2: Google Authenticator: The Hidden Mechanisms of Passwordless Authentication Palo Alto Networks customers are better protected from this new attack vector through the following products and services: Cortex Cloud Identity Security Idira Threat Detection and Response Idira Endpoint Privilege Manager Idira Privilege Access Management If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics Google Authenticator , Cloud , Malware Setting the Stage Google’s synced passkey implementation is particularly instructive due to its scale and how it creates a higher standard for private key protection in two critical ways: Private keys are generated and used within a cloud-enclave isolation environment Hardware-backed, client-device-bound keys control access to cloud-based cryptographic operations, attesting to the user’s presence on a trusted device This article builds on the architectural analysis from Part 1 and Part 2 of our previous articles in this series. We now shift from how passkeys are built and deployed to how attackers can misuse them. We present three novel attacks that enable account takeover of passkey-protected accounts. Each attack challenges a different core assumption of passkey authentication security. When a client authenticates with a passkey, the following is expected: Users provide explicit consent on the device to verify user presence For MFA, users must also unlock the device to verify biometric (i.e., something you are) or knowledge-based (i.e., something you know) authentication factors Passkey private keys cannot be shared or copied The Google documentation reflects these core assumptions, describing the passkey login process as a secure alternative to passwords (as shown in Figure 1). Figure 1. Google documentation describes passkeys as requiring device access, device unlock, and non-shareable credentials. Challenging these expectations is a category of attacks we've nicknamed Pass-ta-key. This playful, layered name blends the word passkey and the phrase “pass the key,” with a
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Pass the Passkey: A Novel Attack Surface in Passwordless Authentication
  - Published: 2026-08-03T10:00:35+00:00
  - Link: https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/
  - Summary: Explore how passkey implementation gaps undermine security when relying parties fail to validate the User Verified flag, reducing MFA to a single factor. The post Pass the Passkey: A Novel Attack Surface in Passwordless Authentication appeared first on Unit 42 .

### Cluster 2675bb2bb6 — score 12

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

### Cluster 7348caeb17 — score 12

- Title: N-able Says Attackers Take Over N-central Servers After Initial Fix Proves Incomplete
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-03T06:41:46+00:00
- Link: https://thehackernews.com/2026/08/n-able-says-attackers-take-over-n.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-18577

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-18556, CVE-2026-18577
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-18577, CVE-2026-18556
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
N-able said attackers exploited an authentication bypass in N-central to gain remote administrative access and reach the customer systems managed through those servers. Its first fix was incomplete. CVE-2026-18577 affects N-central builds prior to 2026.3.1.7. N-able shipped build 2026.3.1.7 on August 2 as the first unaffected version. N-central is the remote monitoring and management platform
```

#### Full body

```
N-able Says Attackers Take Over N-central Servers After Initial Fix Proves Incomplete  Swati Khandelwal  Aug 03, 2026 Vulnerability / Endpoint Security N-able said attackers exploited an authentication bypass in N-central to gain remote administrative access and reach the customer systems managed through those servers. Its first fix was incomplete. CVE-2026-18577 affects N-central builds prior to 2026.3.1.7. N-able shipped build 2026.3.1.7 on August 2 as the first unaffected version. N-central is the remote monitoring and management platform managed service providers and IT teams use to administer customer endpoints. After compromising an N-central server, the attackers used Take Control to reach managed endpoints and registered Cloudflare tunnels as services on the devices. The tunnels connect outbound to Cloudflare's edge, so they need no inbound firewall rule or open listening port. Running them as services lets them survive a reboot. N-able said the tunnels preserved access after the route through the N-central server was revoked. Nothing in the disclosure suggests Cloudflare was compromised; the attackers abused its tunneling service. Every N-central customer should be on 2026.3.1.7. Upgrading to 2026.3, N-able's initial instruction , is no longer sufficient. N-able's hotfix notice says hosted NCOD instances will be upgraded automatically on a schedule communicated directly to partners; self-hosted servers must be upgraded by the customer. Customers that find evidence of compromise must also hunt for and remove malicious tunnel services from managed endpoints, because upgrading N-central does not remove persistence installed on another machine. N-able began investigating on July 31 after an unusual volume of licensing errors from on-premises customers. It found that an attacker had remotely gained administrative access to servers running 2026.1 and earlier. N-able said it identified and contacted a limited number of affected customers but did not provide a figure. The first flaw, CVE-2026-18556 , is titled "unauthenticated administrative account takeover" in N-able's own CVE record and classified as an authentication bypass through an alternate path or channel, or CWE-288. N-able assigned both CVEs and scored each 8.2 on CVSS 4.0. Neither record identifies the vulnerable endpoint or request sequence, and N-able has published no code-level root-cause detail. CVE-2026-18556 covers releases through 2026.1. N-able said it fixed that path in 2026.2, but later found an alternative way to exploit the same vulnerability that the earlier fix did not block. That finding became CVE-2026-18577 and expanded the affected range to builds before 2026.3.1.7. Finland's national cyber security centre said in an August 2 advisory that all versions available before the emergency hotfix were vulnerable. The Hacker News has reached out to N-able for clarification on the incident's scope and incomplete patch. This story will be updated with any response. N-able has now published six IP addresses seen in the attacks: 173[.]249[.]252[.]200 87[.]249[.]138[.]34 37[.]19[.]210[.]32 37[.]153[.]90[.]88 92[.]118[.]112[.]181 68[.]235[.]46[.]214 Huntress later identified the four addresses from N-able's initial list as Mullvad or NordVPN exit nodes. Huntress advised correlating any matches with N-central UI, network, and endpoint logs. N-able also told customers to look for svchost.exe in users' Documents folders, a service named Cloudflared, or traffic from the published IP addresses. It advised customers who find any of these indicators to contact support and engage their security teams. Huntress, in a rapid response published August 3 , initially said it had seen exploitation at one organisation in its customer base and published three attacker domains: mousears.synology[.]me, wagoosh.direct.quickconnect[.]to, and who-ripped-one.direct.quickconnect[.]to. In an email to The Hacker News, Huntress clarified that the activity involved a self-hosted N-cent
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: N-able Says Attackers Take Over N-central Servers After Initial Fix Proves Incomplete
  - Published: 2026-08-03T06:41:46+00:00
  - Link: https://thehackernews.com/2026/08/n-able-says-attackers-take-over-n.html
  - Summary: N-able said attackers exploited an authentication bypass in N-central to gain remote administrative access and reach the customer systems managed through those servers. Its first fix was incomplete. CVE-2026-18577 affects N-central builds prior to 2026.3.1.7. N-able shipped build 2026.3.1.7 on August 2 as the first unaffected version. N-central is the remote monitoring and management platform

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

### Cluster b61889968b — score 12

- Title: Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-29T10:15:00+00:00
- Link: https://www.infosecurity-magazine.com/news/one-percent-ai-vulnerabilities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, mfa_bypass, phishing_social_eng, zero_day
- affected_products: Anthropic/Claude, OpenAI/ChatGPT, WordPress
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, mfa_bypass, active_exploitation
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
Infosecurity Magazine Home » News » Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows News 29 July 2026 Written by Kevin Poireault Reporter , Infosecurity Magazine Follow @Kpoireault Connect on LinkedIn Software vulnerabilities discovered using AI tools are being exploited at the same rate as those discovered without the use of AI, a VulnCheck researcher has found. In VulnCheck’s State of Exploitation H1 2026 report , Patrick Garrity, vulnerability researcher, observed that 14 of the 1061 vulnerabilities attributed to AI-assisted discovery have been confirmed as exploited in the wild. This represents 1.3% of vulnerabilities identified using AI, roughly matching the overall exploitation rate of all vulnerabilities for the reported period. The researcher also found that while Anthropic reported more than 23,000 findings through its Project Glasswing , only 126 have resulted in published CVEs and just one has been confirmed as exploited in the wild. These findings add nuance to warnings from some quarters that AI tools like Anthropic's Mythos and other frontier models could trigger a ‘vulnpocalypse,’ flooding the security landscape with a wave of newly discovered, mass-exploited vulnerabilities. Garrity said that for now, vulnerability intelligence shows evidence that the use of frontier AI models is “more likely to give cyber defenders an advantage in strengthening software than to give attackers an advantage in discovering vulnerabilities before the software producers do.” KEV Exploitation Growth Lags Behind Rising CVE Volume VulnCheck identified nearly 500 known exploited vulnerabilities (KEVs) in the first half of 2026. These appear to be being exploited faster than ever before, with the median time from CVE publication to KEV falling from 120 days in 2025 to 80 days during the first half of 2026. However, the research found that 23.43% of KEVs recorded in the first half of 2026 showed evidence of exploitation on or before the day the CVE was published, a slight drop from the 28.93% of one-day and zero-day KEVs observed in 2025. Additionally, exploitation activity early in the CVE lifecycle remained steady, with roughly 200 CVEs becoming exploited within 31 days in the first half of 2026. “Early exploitation activity has not scaled at the same pace as CVE issuance,” said Garrity. Source: VulnCheck Content management systems (CMS) remained the most targeted technology category, accounting for 163 KEVs, one-third of all recorded KEVs. They are followed by network edge devices (68), operating systems (44) and server software (40). Meanwhile, AI products are emerging as a new attack surface , with known exploitation affecting model-building tools, workload-scaling platforms, AI gateways, agents and workflow automation. Source: VulnCheck The VulnCheck report includes every KEV added to VulnCheck’s own KEV catalog during the first half of 2026, based on CVE publication date and earliest evidence of exploitation. The AI-discovered vulnerabilities mentioned in this report come from both Garrity’s own recording of vulnerabilities reported through Anthropic’s Project Glaswing and telemetry from the Berkeley Vulnerability Research Initiative . You may also like Researchers Build WordPress Exploit Using OpenAI's GPT News 20 July 2026 Infosecurity Europe: Patch Responsibility Remains Up for Grabs as AI Unearths Decades of Flaws News 3 June 2026 Two Critical Flaws in n8n AI Workflow Automation Platform Allow Complete Takeover News 4 February 2026 Organizations Found to Address Only 21% of GenAI-Related Vulnerabilities News 15 April 2025 Microsoft Condemns "Uncoordinated" Zero Day Disclosures News 28 May 2026 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Teams-Themed Phishing Campaign Abused Legitimate Microsoft Login Pages News 30 July 2026 1 AiTM Phishing Becomes Top Initial Access Threat to Law Firms News
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows
  - Published: 2026-07-29T10:15:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/one-percent-ai-vulnerabilities/
  - Summary: For now, the use of AI benefits vulnerability research more than vulnerability exploitation, a VulnCheck researcher said

### Cluster 94fd56afbc — score 11

- Title: What's new in Elastic Defend: 800+ vulnerable driver rules, automated troubleshooting, and ARM support
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-31T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/vulnerable-driver-detection-elastic-defend-byovd
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
Elastic Defend automatically generates and instantly deploys vulnerable driver YARA rules from VirusTotal, LOLDrivers and Microsoft's blocklist, closing the gap BYOVD attacks depend on. Plus a new troubleshooting skill and ARM endpoint protection.
```

#### Full body

```
31 July 2026 • Pedro Jaramillo • Roxana Gheorghe • Mia LaVada What's new in Elastic Defend: 800+ vulnerable driver rules, automated troubleshooting, and ARM support Elastic Defend automatically generates and instantly deploys vulnerable driver YARA rules from VirusTotal, LOLDrivers and Microsoft's blocklist, closing the gap BYOVD attacks depend on. Plus a new troubleshooting skill and ARM endpoint protection. 5 min read Product Updates , Detection Engineering We know you’re tired of hearing how every vendor is going to finally help you solve alert fatigue. Well, one way we’re improving alert fatigue is from a slightly different angle, better prevention at the endpoint. Because stopping more at the endpoint means fewer alerts ever raised. We have three endpoint enhancements, all contributing to better endpoint prevention: To be even more proactive about Bring Your Own Vulnerable Driver (BYOVD) attacks, we’re continuously monitoring public vulnerable driver disclosures and automatically generating endpoint protections To improve your endpoint management efficiency, Automatic Troubleshooting is now available as a skill via Elastic Agent Builder To expand our coverage surface, Elastic Defend is now available for Windows on ARM Let’s dig into each one. What is a BYOVD attack and how does it bypass endpoint protection? BYOVD is a technique attackers use to gain kernel-level access on Windows machines by abusing legitimately signed drivers, letting them bypass defenses meant to block unauthorized code. Windows requires low-level software drivers that run in the kernel to be digitally signed, so rather than trying to sneak in something unsigned, attackers bring a driver that's already signed and trusted, but that has a known security flaw. That flaw is enough to disable security software or tamper with memory, and once an attacker has that level of access, security tools can no longer reliably protect the host. This combination is why BYOVD has become so appealing to ransomware operators. The technique started as tradecraft mostly reserved for advanced state actors and red teams. Elastic Security Labs has tracked its shift into a routine step ransomware crews now use to tamper with or shut down endpoint security software before deploying their payload, as detailed in Stopping Vulnerable Driver Attacks . Now, why does timing matter here? BYOVD attacks have depended on one thing for years: the delay between a vulnerable driver's public disclosure and a vendor shipping coverage for it. The moment a vulnerable driver becomes public knowledge, attackers already know about it. When it takes a vendor an entire product release to ship a protection, that gap is exactly what the technique depends on. To close this gap, Elastic Security Labs Threat Command, Elastic's security research team now continuously monitors public vulnerable driver disclosure sources, including VirusTotal, the LOLDrivers catalog, and Microsoft's Vulnerable Driver Block List, and automatically generates and instantly deploys detection rules. Because we know any delay could be the difference between an exposed endpoint and a secured one, we’ve decoupled this coverage from any release cycle and publish the protections in the open. How Elastic automatically generates vulnerable driver YARA rules Elastic Security Labs has published detection coverage for vulnerable drivers for years. That coverage now runs through an always-on process that adds new drivers to the protections library as they're disclosed. An always- on process means coverage ships continuously, not whenever the next major release happens to land, and it doesn’t require an update or setting change. A driver flagged today becomes a driver Elastic Defend recognizes. Elastic Security Labs Threat Command monitors three public sources for newly disclosed vulnerable and malicious drivers: VirusTotal The community-run LOLDrivers catalog Microsoft's Vulnerable Driver Block List No single source catches everything, so t
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: What's new in Elastic Defend: 800+ vulnerable driver rules, automated troubleshooting, and ARM support
  - Published: 2026-07-31T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/vulnerable-driver-detection-elastic-defend-byovd
  - Summary: Elastic Defend automatically generates and instantly deploys vulnerable driver YARA rules from VirusTotal, LOLDrivers and Microsoft's blocklist, closing the gap BYOVD attacks depend on. Plus a new troubleshooting skill and ARM endpoint protection.

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

### Cluster f7c0990e5f — score 11

- Title: OpenSSF Community Day Europe 2026: Schedule Highlights & What to Expect
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-07-29T20:03:12+00:00
- Link: https://openssf.org/blog/2026/07/29/openssf-community-day-europe-2026-schedule-highlights-what-to-expect/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: government, legal_professional, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: government, manufacturing_industrial, legal_professional
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
OpenSSF Community Day Europe 2026 (October 6 in Prague), focuses on open source software security, regulatory compliance like the EU CRA, and AI supply chain risks. The one-day event features technical sessions on tools like VEX, Gemara, and Sigstore, offering direct collaboration with maintainers and security experts.
```

#### Full body

```
By Angelah Liu, Linux Foundation TL;DR: OpenSSF Community Day Europe 2026 (October 6 in Prague), focuses on open source software security, regulatory compliance like the EU CRA, and AI supply chain risks. The one-day event features technical sessions on tools like VEX, Gemara, and Sigstore, offering direct collaboration with maintainers and security experts. Between evolving regulatory mandates like the EU Cyber Resilience Act (CRA) and the rise of AI-driven vulnerabilities, securing open source code has become a baseline requirement for engineering teams, not an afterthought. The official Schedule for OpenSSF Community Day Europe 2026 is now live. Co-located with Open Source Summit Europe in Prague on October 6, 2026, this single-day event brings together open source maintainers, security researchers, enterprise contributors, and policy experts for a full day of technical exchange. Whether you’re looking to harden your CI/CD pipelines, get ahead of upcoming compliance frameworks, or simply talk shop with the maintainers behind the tools you rely on, this year’s schedule has a lot to offer. Session Highlights Keynote: Welcome & Opening Remarks Steve Fernandez, General Manager of OpenSSF at the Linux Foundation, kicks things off at 9:00 CEST with the opening keynote , setting the tone and priorities for the day ahead. EU Regulations & Governance Right after lunch, Roman Zhukov (Red Hat), Daniel Appelquist, Madalin Neag (OpenSSF), and Megan Knight (Arm) take the stage at 13:55 CEST for Operationalizing the CRA and Shaping OpenSSF’s Community Roadmap . The CRA is reshaping how open source projects handle vulnerability management and maintainer liability, and this session is where the legal language turns into something developers can actually build into their workflows. AI Infrastructure & Supply Chain Provenance AI is playing a double role in security right now: an automated tool for finding bugs faster, and a new surface area attackers are learning to exploit. Three sessions dig into that tension from different angles. Jeff Diecks and Laura Guazzelli from OpenSSF open the topic at 10:55 CEST with Preparing for the Vulnpocalypse: Using OSS-CRS To Find and Fix Bugs Before They Find You , covering automated vulnerability discovery at scale. At 11:20 CEST, Dmitry Tantsur (Red Hat) and Tuomo Tanskanen (Ericsson) will shift the focus to infrastructure with Defending Bare-Metal: Lessons Learnt From AI Security Analysis of Metal3 and OpenStack Ironic . And later in the afternoon, at 16:30 CEST, Sheng Sun and Sarah Evans (both of Dell Technologies) tackle the machine learning supply chain itself in Verifiable AI Provenance: Closing the Attestation Gap in the Machine Learning Supply Chain , asking how teams can actually verify what went into a model before it reaches production. Tooling & Supply Chain Standards Good security policy only goes as far as the tooling that puts it into practice. Hannah Braswell (Red Hat) walks through that idea at 11:45 CEST in From First PR To Hardening Guide: Structured Security With Gemara , showing how the Gemara framework brings structure to governance, risk, and compliance work. Later, at 16:50 CEST, Yuta Kiyoumi (Honda Motor Co., Ltd.) and Akihiko Takahashi (Fujitsu) bring a real-world manufacturing lens to the conversation with Applying VEX To Vulnerability Information Sharing in Multi-tier Automotive Supply Chains , showing how Honda uses the Vulnerability Exploitability eXchange (VEX) standard to track risk across hardware and software tiers alike. Community & Interactive Sessions Not everything on the schedule is a deep technical dive. At 15:15 CEST, OpenSSF’s Adrianne Marcum and CRob return with GAME SHOW!! Part Dva!! for a lighter, interactive take on community learning. And closing out the day at 17:10 CEST, Ejiro Oghenekome, Victoria Ottah, Sal Kimmich (OpenUK), CRob (OpenSSF), and Amir Montazery (OSTIF) come together for Securing Africa’s Open Source Ecosystem , a conversation about maintainer
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: OpenSSF Community Day Europe 2026: Schedule Highlights & What to Expect
  - Published: 2026-07-29T20:03:12+00:00
  - Link: https://openssf.org/blog/2026/07/29/openssf-community-day-europe-2026-schedule-highlights-what-to-expect/
  - Summary: OpenSSF Community Day Europe 2026 (October 6 in Prague), focuses on open source software security, regulatory compliance like the EU CRA, and AI supply chain risks. The one-day event features technical sessions on tools like VEX, Gemara, and Sigstore, offering direct collaboration with maintainers and security experts.

### Cluster 5da08d22f3 — score 11

- Title: Online ad firm Adform’s script compromised to steal cryptocurrency
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-31T21:09:25+00:00
- Link: https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Online advertising firm Adform suffered a supply-chain attack that delivered cryptocurrency-stealing scripts to websites using its ad platform, replacing wallet addresses copied to visitors' clipboards with ones controlled by an attacker. [...]
```

#### Full body

```
Online ad firm Adform’s script compromised to steal cryptocurrency By Bill Toulas July 31, 2026 05:09 PM 0 Online advertising firm Adform suffered a supply-chain attack that delivered cryptocurrency-stealing scripts to websites using its ad platform, replacing wallet addresses copied to visitors’ clipboards with ones controlled by an attacker. Adform is one of Europe’s largest adtech firms, providing a full-stack platform that includes Demand-Side Platform (DSP), Supply-Side Platform (SSP), ad servers, and management tools. Security researcher Kevin Beaumont discovered the malicious activity, saying that it stemmed from ‘trackpoint-async.js,’ Adform’s JavaScript tracking script served from ‘s2.adform.net’ and embedded in every website using the advertising platform. According to the researcher, the trojanized JavaScript continuously monitors the clipboard of users visiting websites that embed trackpoint-async.js . If the script detected Bitcoin, Ethereum, or TRON wallet addresses, it replaced them with an attacker-controlled address to redirect cryptocurrency payments. Compromised Adform script replacing crypto addresses source: BleepingComputer “This allows end-user devices of downstream websites to be compromised with crypto-stealing malware. Meaning if you visit example.com and they use Adform, example.com will compromise your device,” Beaumont explains . The researcher also observed other malicious Adform-hosted scripts communicating with an attacker-controlled server at 84.32.102[.]230:7744, sending the victim's IP address, referring website, and URL path. Running the script through the VirusTotal scanning platform shows that it is not flagged as malicious by any of the available antivirus engines. VirusTotal scan of the script gives clean result Source: doublepulsar.com Current status Beaumont notes that the malicious code was removed from Adform’s tracking script soon after his discovery. Adform confirmed its detected suspicious activity on July 27 and discovered a "cybersecurity threat." The company said that it removed the malicious code and "took further measures to protect website visitors, our clients, and the Adform platform." "To our knowledge, the code was not designed to install software on a user’s device or establish persistence. It operated only while an affected webpage was open," Adform says . The company states that its services are now safe to use but its investigation continues. Individuals who visited websites that embedded the "affected Adform technology on 27 July 2026" are impacted and the recommendation is to clear browser cookies to eliminate the malicious code. "Adform has informed affected clients through dedicated communications and provided them with relevant information and recommended actions." Beaumont has shared a sample of the malicious script via Pastebin for security engineers to analyze. BleepingComputer's analysis of a sample stored on Archive.org also confirmed that a self-executing payload had been injected into the Adform tracking library served from the company's infrastructure. The malicious code was appended in obfuscated form at the end of the legitimate library and included a function that replaced any string matching a crypto wallet address format. Apart from hijacking clipboard content, the malware can also rewrite wallet addresses on web pages. This way, if a payment address is displayed, it would be the attacker's. Beaumont says the malicious activity delivered through Adform has been ongoing for the past week without being detected. The oldest sample BleepingComputer could find was from from the Archive.org snapshot on July 26, taken at 23:29:03 GMT. BleepingComputer has contacted Adform to request a statement regarding Beaumont’s findings and will update the story if we receive a response. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how b
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Online ad firm Adform’s script compromised to steal cryptocurrency
  - Published: 2026-07-31T21:09:25+00:00
  - Link: https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/
  - Summary: Online advertising firm Adform suffered a supply-chain attack that delivered cryptocurrency-stealing scripts to websites using its ad platform, replacing wallet addresses copied to visitors' clipboards with ones controlled by an attacker. [...]

### Cluster 3ba1ff40b5 — score 11

- Title: JetBrains warns of critical TeamCity remote code execution flaw
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-30T22:01:31+00:00
- Link: https://www.bleepingcomputer.com/news/security/jetbrains-warns-of-critical-teamcity-remote-code-execution-flaw/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- cve_ids: CVE-2026-63077
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, active_exploitation
- cve_ids: CVE-2026-63077
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
JetBrains is warning of a critical authentication bypass vulnerability affecting TeamCity On-Premises that could be exploited to achieve remote code execution. [...]
```

#### Full body

```
JetBrains warns of critical TeamCity remote code execution flaw By Bill Toulas July 30, 2026 06:01 PM 0 JetBrains is warning of a critical authentication bypass vulnerability affecting TeamCity On-Premises that could be exploited to achieve remote code execution. The security issue is tracked as CVE-2026-63077 and can be leveraged by an attacker with HTTPS access to a TeamCity server to bypass authentication via the agent polling protocol and execute arbitrary operating system commands with the privileges of the server process. “All versions of TeamCity On-Premises are affected,” JetBrains warns in the advisory , adding that “TeamCity Cloud customers are not required to take any action, as the necessary measures have already been applied.” TeamCity is a commercial continuous integration and continuous delivery (CI/CD) server that is used for building, testing, and deploying software. Daniel Gallo, Solutions Engineering Lead at JetBrains, says that successful exploitation of CVE-2026-63077 could expose TeamCity data, configurations, stored credentials, or compromise build artifacts and CI/CD pipelines, depending on privileges. At the time the advisory was published on July 27, there was no evidence of active exploitation. Given that TeamCity flaws have been extensively leveraged in the past, including by ransomware gangs and state-backed actors , administrators should take immediate action to mitigate the risks. Recommended actions JetBrains says the issue was privately reported to them on July 10 and was addressed in TeamCity versions 2025.11.7 and 2026.1.3. The vendor recommends upgrading to the versions listed above as the first option. A security patch is available for TeamCity 2017.1+ as a plugin for customers unable to upgrade to the latest releases. JetBrains notes that TeamCity 2024.03 and newer automatically downloads available security patch plugins and notifies administrators so they can install them. Also, TeamCity versions 2017.1 through 2018.1 will require a server restart for the security updates to take effect after installing the patch plugin. Detailed instructions for installing the security plugin are available here . JetBrains also highlighted a set of more generic “best practices,” including requiring VPN access or other protective layers on internet-facing TeamCity servers. The vendor reminds that even exposing the login page or REST API can give attackers an entry point to exploit newly disclosed vulnerabilities. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Rails patches critical Active Storage flaw with RCE potential vBulletin fixes critical pre-auth RCE flaw with public exploit Hackers target US firms in FastJson RCE zero-day attacks CISA orders urgent action on actively exploited Langflow RCE flaw Critical Langflow RCE flaw exploited to hack AI app servers
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: JetBrains warns of critical TeamCity remote code execution flaw
  - Published: 2026-07-30T22:01:31+00:00
  - Link: https://www.bleepingcomputer.com/news/security/jetbrains-warns-of-critical-teamcity-remote-code-execution-flaw/
  - Summary: JetBrains is warning of a critical authentication bypass vulnerability affecting TeamCity On-Premises that could be exploited to achieve remote code execution. [...]

### Cluster 75acd25c40 — score 10

- Title: Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks
- Source: Unit 42 (threat_research_primary)
- Published: 2026-07-30T10:00:52+00:00
- Link: https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, GitHub, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT, Anthropic/Claude, GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Unit 42 details a Chinese speaking threat actor combining autonomous AI scanning across seven vulnerabilities with manual exploitation. Read more. The post Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center Threat Research Vulnerabilities Vulnerabilities Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks 10 min read Related Products Advanced Threat Prevention Advanced WildFire Cloud-Delivered Security Services Cortex Cortex XDR Cortex Xpanse Cortex XSIAM Next-Generation Firewall Unit 42 AI Security Assessment Unit 42 Frontier AI Defense Unit 42 Incident Response By: Andy Piazza Published: July 30, 2026 Categories: Threat Research Vulnerabilities Tags: ChatGPT Claude code CVEs DeepSeek Exploitation Hermes Agent Share Executive Summary Unit 42 identified an AI-enabled autonomous hacking campaign carried out by a Chinese-speaking threat actor. They targeted infrastructure using seven vulnerabilities, combining autonomous AI-driven enumeration with manual exploitation that achieved confirmed impact. The actor, operating under the aliases knaithe and KnYuan , leveraged DeepSeek , via the Hermes Agent framework, as their autonomous offensive operator. They orchestrated this operator via Telegram for the following activities: Independently enumerating targets and their vulnerabilities using FOFA Sourcing exploit tools Initiating attacks without human intervention In parallel with their use of DeepSeek as their autonomous operator platform, the actor configured multiple large language models (LLMs) ( Qwen , GLM, Kimi, MiniMax). We also identified limited usage and testing of Western platforms. This includes Claude Code for connectivity testing and proxy validation. There were also signs of usage of Codex on exploit development directories. This limited usage is consistent with evaluating the AI-market to identify their preferred tool set. When initial exploitation failed due to the target environment's restrictive configurations, their Hermes Agent autonomously conducted searches for known critical-severity Common Vulnerabilities and Exposures (CVEs). It initially surveyed 10 product families, scanning GitHub for trending proofs of concept (PoCs) and prioritizing vulnerabilities by attack surface. This research led the agent to pivot to higher-value vulnerabilities, the seven covered in Table 2 below. While the observed campaign had limited impacts, the workflow confirms a functional, end-to-end autonomous offensive capability. Palo Alto Networks customers are better protected from the threats described here through the following products and services: Cortex XDR and XSIAM Cortex Xpanse Next-Generation Firewall with Advanced Threat Prevention The Unit 42 AI Security Assessment and Unit 42 Frontier AI Defense service can help identify and mitigate complex AI-enabled risks. If you think you might have been compromised or have an urgent matter, contact the Unit 42 Incident Response team . Related Unit 42 Topics GenAI , Vulnerabilities , LLM Technical Analysis We gained unique insights into this autonomous attack capability when the autonomous agent inadvertently exposed its infrastructure by starting a file server in its home directory. This revealed the full operational environment to our threat researchers. This visibility enabled us to understand their full tool set, how the attackers orchestrated multiple AI platforms and gave us a peek into their targeting. Based on our analysis of their session logs and configuration files, the actor primarily used the Hermes Agent with DeepSeek as its reasoning agent for the attack phase of this campaign. Their Hermes Agent conducted autonomous vulnerability enumeration, downloaded public exploit code from the internet and attempted exploits against targets. Additionally, the threat actor leveraged the following tools in a limited capacity, likely indicating an ongoing assessment of the AI market for their use cases: Claude Code: The actor only used this for connectivity testing and proxy validation. Session history (10 entries across three sessions) contained only /model checks, connectivity tests and one npm install request. Codex : There were signs
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks
  - Published: 2026-07-30T10:00:52+00:00
  - Link: https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/
  - Summary: Unit 42 details a Chinese speaking threat actor combining autonomous AI scanning across seven vulnerabilities with manual exploitation. Read more. The post Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks appeared first on Unit 42 .

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

### Cluster 1d6332ec8a — score 10

- Title: Network Anomaly Detection in KATA
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-31T10:00:25+00:00
- Link: https://securelist.com/tr/network-anomaly-detection-in-kata/120892/
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
An analysis of how Network Anomaly Detection (NAD) rules work within Kaspersky Anti Targeted Attack, using Kerberoasting and DNS tunneling attacks as examples.
```

#### Full body

```
Threat Response Table of Contents Introduction Kerberoasting attack detection by KATA Why standard tools have a hard time detecting Kerberoasting Creating a Network Anomaly Detection rule Detecting DNS tunneling in KATA How DNS tunnels work DNS tunneling detection logic Prebuilt rules for detecting network anomalies in KATA Conclusion Introduction Once the attacker has breached the corporate network, subsequent stages of the attack often involve leveraging standard domain infrastructure protocols: using Kerberos, running DNS queries, accessing internal services, opening network shares, and other common networking actions. Because this activity is virtually indistinguishable from legitimate network traffic, it is extremely difficult to detect it with traditional network attack detection tools. Kerberoasting and DNS tunneling have long ceased to be exotic techniques. They are becoming standard methods in modern attacks because they allow attackers to execute critical compromise stages while remaining undetected by traditional security tools. A clear example of this trend is seen in latest campaigns, employing both Kerberoasting and DNS tunneling . Traditional network security tools perform well when the attack features a distinct and identifiable indicator: a characteristic query string, a known malicious traffic pattern, or the source code of an already discovered exploit. While this approach to threat detection remains effective, it cannot always be applied to discovering network attacks that blend seamlessly with legitimate traffic inside a corporate network. Instead of searching for explicit indicators of attack, Network Anomaly Detection (NAD) analyzes all traffic for suspicious artifacts that deviate from the host’s typical network activity. Within Kaspersky’s solution portfolio, this technology is implemented specifically in the Kaspersky Anti Targeted Attack (KATA) platform. The system analyzes network traffic data (DNS, DCE/RPC, Kerberos and other packets) and extracts key parameters used to identify anomalous behavior. This approach enables searching for attacks on domain controllers, signs of traffic tunneling and exfiltration, C2 communications, and other scenarios that may point to compromise of network infrastructure. However, Network Anomaly Detection is not built on a single, universal set of indicators. Each attack scenario employs tailored detection models that account for the specifics of the corresponding network protocol, typical host behavior, and characteristic deviations from that baseline. This article examines two practical examples – detecting Kerberoasting and DNS tunneling – to demonstrate how these principles are implemented in KATA’s NAD rules and why this approach proves more effective than traditional signature-based analysis. Kerberoasting attack detection by KATA Why standard tools have a hard time detecting Kerberoasting The Kerberoasting attack leverages the standard operational logic of the Kerberos protocol. The attacker identifies service accounts configured with a Service Principal Name (SPN), requests a Ticket-Granting Service (TGS) ticket for them, and attempts to crack the password offline using a dictionary attack against the retrieved ticket. If the password is weak or hasn’t been changed in a long time, the adversary can bruteforce it to get it in cleartext. Subsequently, these compromised credentials can be leveraged for both vertical and horizontal movement across the network. The essence of a Kerberoasting attack is that an adversary possessing a compromised low-privileged account and a valid Ticket-Granting Ticket (TGT) for that account can request TGS tickets with weakened encryption for service accounts with SPNs. Crucially, it doesn’t matter whether the compromised account actually holds access permissions for those services. Having obtained these tickets, the attacker can then take them offline and bruteforce the service account’s password by trying to decrypt the correspond
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Network Anomaly Detection in KATA
  - Published: 2026-07-31T10:00:25+00:00
  - Link: https://securelist.com/tr/network-anomaly-detection-in-kata/120892/
  - Summary: An analysis of how Network Anomaly Detection (NAD) rules work within Kaspersky Anti Targeted Attack, using Kerberoasting and DNS tunneling attacks as examples.

### Cluster ba4ef137f5 — score 10

- Title: OctLurk and SilkLurk: newly identified tailored backdoors in cyber-espionage campaign in Central Asia
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-30T11:00:12+00:00
- Link: https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: critical_infrastructure, government, healthcare
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor
- affected_industries: healthcare, government, critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Our experts discovered OctLurk and SilkLurk, backdoors operating primarily in memory, targeting Central Asia. They inject plugins to launch shells, scan networks, dump credentials, and keylogging.
```

#### Full body

```
Table of Contents Introduction OctLurk OctLurk Deployment LurkPoxy Deployment OctLurk loader OctLurk backdoor Post-compromise activity Victim fingerprinting Event log collection Credential harvesting Impacket — secretsdump Keylogger Browser Password Decryptor Remote access : Pandora FMS agents (Pandora RC agent) Network scan: FSCAN Email harvesting LurkProxy SilkLurk Deployment SilkLurk loader SilkLurk backdoor Post-compromise activity Second-stage payload PlugX Infrastructure Attribution Conclusions Indicators of Compromise Backdoor domains and IPs OctLurk C2 LurkProxy C2 SilkLurk C2 Loaders OctLurk loader SilkLurk loader PlugX dropper PlugX loader OctLurk backdoor OctLurk File Manager plugin OctLurk Command Shell plugin OctLurk Interaction Manager plugin Impacket’s secretsdump (not available) Keylogger Browser password stealer FSCAN Batch scripts (not available) Archive utilities WinRAR 7zip File paths OctLurk file paths SilkLurk file paths PlugX file paths WinRAR and 7z file paths Authors Saurabh Sharma Yaroslav Kikel Introduction We have been tracking two new backdoors, OctLurk and SilkLurk , observed in attacks against government organizations primarily in Central Asia since January 2025. Identified victims are located in Afghanistan, Kyrgyzstan, Tajikistan, Uzbekistan, Kazakhstan, and the Syrian Arab Republic. These organizations operate across several sectors, including healthcare, research, government offices, ministries of foreign affairs, logistics, law‑enforcement agencies, urban planning and facilities management, and public educational establishments. The backdoor loaders are customized for each victim and use information from the victim’s machine to decrypt the payload. Both the loaders and the backdoors are heavily obfuscated, making analysis more complicated. OctLurk and SilkLurk can download and inject additional plugins to perform further malicious actions, including launching command shells, performing file system activity, synthesizing keyboard and mouse events, network scanning, credential dumping, keylogging, password theft from browsers, email collection, and remote access. Furthermore, the attackers deployed a specialized utility we named LurkProxy , which we also cover in this report. While it has a highly similar architecture to the OctLurk backdoor, it is not a backdoor itself. Our investigation shows that the same threat actor operates both SilkLurk and OctLurk , and some victims infected with SilkLurk also contain OctLurk. We assess with medium confidence that the same actor is behind both backdoors, and that they are Chinese‑speaking. However, at the time of publication, we couldn’t attribute this activity to any known group. OctLurk OctLurk Deployment The attacker created a scheduled task named GoogleUpDate on remote machines using admin credentials. The task runs once with System account privileges right after it was created, executing the batch script located at C:\Users\<username>\Videos\1.bat (MD5 6ecf84fb18f6747ed08d7598364d853a ). Prior to executing the task, the actor queries its status. It is then run, as shown below. The 1.bat script creates a service named NgcCIntSvc , which loads the loader DLL named oleasapi.dll (MD5 082d49ef9f14e6811d68c7e0e82e5069 ). The ServiceMain parameter in the service’s registry entry is set to invoke the RegisterService function of oleasapi.dll as shown below. LurkPoxy Deployment In another case, the attacker at first checked connectivity to the domain dns[.]ssentialserv[.]xyz as shown below. At the time of our research, the domain was resolving to the address 154[.]196[.]162[.]76 which is used as a LurkProxy C2 server. After confirming that the C2 server was reachable, the attacker executed the batch script C:\Users\[username]\Desktop\auto.bat (MD5 b874123a80fc4f40e06872b9cb54ebc6 ). The script created a service named Cusrxsrv , which loads a DLL named msbasesysdc.dll . In the service registry, the ServiceMain parameter was set to call the RegisterService fu
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: OctLurk and SilkLurk: newly identified tailored backdoors in cyber-espionage campaign in Central Asia
  - Published: 2026-07-30T11:00:12+00:00
  - Link: https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/
  - Summary: Our experts discovered OctLurk and SilkLurk, backdoors operating primarily in memory, targeting Central Asia. They inject plugins to launch shells, scan networks, dump credentials, and keylogging.

### Cluster f6cd02268d — score 10

- Title: Toy Ghouls’ new toy: the GenieLocker ransomware
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-30T08:00:57+00:00
- Link: https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- affected_industries: critical_infrastructure, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky experts dissect GenieLocker: new custom ransomware variants for Windows, Linux, and ESXi systems. We found this family in attacks by Toy Ghouls, a financially motivated extortion group.
```

#### Full body

```
Table of Contents Introduction Technical details Modus operandi Initial Access Discovery and Credential Access Lateral Movement and Command and Control Impact Encryption Trojan for Windows Arguments and launch Anti-debugging Preparing for encryption File encryption and cryptography Encryption Trojan for ESXi and Linux ESXi and Linux features File encryption Victims Conclusions Indicators of compromise GenieLocker for Windows GenieLocker for Linux and ESXi C2 Authors Fedor Sinitsyn Yanis Zinchenko Introduction The new GenieLocker ransomware family has been active since March 2026. It has been used in attacks against organizations in the Russian Federation, primarily in the manufacturing sector, and attributed to the Toy Ghouls group by open-source intelligence (link in Russian). The Toy Ghouls, also known as Bearlyfy, Labubu and Laboo.boo, is a financially motivated extortion group, which previously relied on third-party encryption Trojans like RedAlert, LockBit, and Babuk. GenieLocker, apparently a custom design, upgrades their toolkit and reduces their reliance on third-party software. We discovered multiple samples of this Trojan in two variants: PE builds for Windows and ELF builds for Linux and ESXi. Technical details Modus operandi We described typical TTPs and modus operandi of the Toy Ghouls threat actor in the previous post (link in Russian). In this article, we aim to thoroughly describe the capabilities of Windows and Linux builds of the custom encryption Trojan GenieLocker. To give more context, we will also provide a brief overview of the attack that took place at the end of March 2026, where GenieLocker was deployed on the victim’s systems. Initial Access During the incident, the attackers first entered the environment through an OpenVPN connection originating from an external partner’s network. They likely exploited the trusted relationship with that partner and used stolen, yet still valid, credentials to connect. Discovery and Credential Access After breaching the target’s network, the attackers installed additional tools on the compromised hosts, including OpenSSH, socks5.exe, SoftPerfect Network Scanner, and Mimikatz. They employed SoftPerfect Network Scanner for discovery and used Mimikatz to dump credentials. Forensic analysis also shows that they accessed the KeePassXC password manager already installed on several compromised machines, likely attempting to extract the stored credentials from the KeePass databases. Lateral Movement and Command and Control Lateral movement was performed by using RDP to reach Windows machines and SSH for Linux servers. The widespread deployment of the encryption Trojan was conducted with the legitimate utilities PsExec and PAExec. Additionally, the attackers established a reverse SSH tunnel to communicate with their command‑and‑control server. Impact During the impact phase, the attackers encrypted files on the compromised Windows machines with the PE version of the GenieLocker ransomware. On the compromised Linux and ESXi servers, they stopped active virtual machines and encrypted their disks using the ELF version of GenieLocker. The tactics, techniques, and procedures seen here match those documented in earlier attacks attributed to the Toy Ghouls group. As in those prior incidents, forensic analysis found no evidence of data exfiltration, which is typical behavior for this threat actor. Toy Ghouls have not employed a double‑extortion model and do not run a data‑leak website. Encryption Trojan for Windows The Windows version of GenieLocker (MD5: 5d62c1349b8981c396c9a23f4f8f053c) is primarily written in C, but compiled with the C++ libraries using Microsoft Visual C/C++. The malware incorporates several ransom‑related capabilities, including process termination, service shutdown, debugger evasion, and a sophisticated encryption routine. For its cryptographic operations, it relies on the open‑source libsodium library. Aligned with the recent trend supported by our expertise,
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Toy Ghouls’ new toy: the GenieLocker ransomware
  - Published: 2026-07-30T08:00:57+00:00
  - Link: https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/
  - Summary: Kaspersky experts dissect GenieLocker: new custom ransomware variants for Windows, Linux, and ESXi systems. We found this family in attacks by Toy Ghouls, a financially motivated extortion group.

### Cluster d2bbfb6b89 — score 10

- Title: Black Hat special: Rewind and revisit
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-07-30T10:00:08+00:00
- Link: https://blog.talosintelligence.com/black-hat-special-rewind-and-revisit/
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
Amy looks back at the incredible journeys that brought past guests to the world of threat intelligence.
```

#### Full body

```
Black Hat special: Rewind and revisit By Amy Ciminnisi Thursday, July 30, 2026 06:00 Humans of Talos Cybersecurity is rarely a straight line. In this special Black Hat edition of Humans of Talos, Amy looks back at the incredible journeys that brought past guests to the world of threat intelligence. From forensic labs and newsrooms to the kitchen line, we’re revisiting the stories and lessons that define the people behind the threat intelligence. Heading to Black Hat? We have a presence within the Cisco and Splunk booth (2633) during Black Hat where you can chat to us about our latest threat research and incident response, and grab the newest Snorty. Check out our schedule here . Want more episodes? Watch the full episode , and don’t forget to subscribe to our YouTube channel for the next Humans of Talos. Share this post Related Content Martin Lee: Running through the Arctic (and the threat landscape) July 1, 2026 06:00 Ever wonder how someone goes from studying human viruses to leading cybersecurity teams? In this Humans of Talos, we’re joined by Martin Lee, EMEA Lead, to talk about his journey into the industry. Winning the cyber marathon with Tony Giandomenico June 4, 2026 08:05 Tony Giandomenico, Senior Director of Product Management, joins Amy to discuss the Talos Threat Hunting launch what he's excited about for the future of cybersecurity, and, of course, his Ironman triathlons. Breaking things to keep them safe with Philippe Laulheret May 13, 2026 06:00 Philippe shares his unique journey from French engineering school to the front lines of cybersecurity, explaining how his lifelong love for solving puzzles helps him uncover critical security flaws before they can be exploited.
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Black Hat special: Rewind and revisit
  - Published: 2026-07-30T10:00:08+00:00
  - Link: https://blog.talosintelligence.com/black-hat-special-rewind-and-revisit/
  - Summary: Amy looks back at the incredible journeys that brought past guests to the world of threat intelligence.

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

### Cluster f4490338d9 — score 10

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

### Cluster 3a5451ad51 — score 10

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
Different Attack Surface. Same Outcome: Security You Can Prove. Horizon3 July 28, 2026 Factsheets Modern attackers don’t stop at infrastructure—they target the custom web applications your business depends on every day. NodeZero® WebApp continuously validates which web application weaknesses attackers can actually exploit into business impact by crawling, authenticating, attacking, and proving consequences the way real attackers operate. Instead of generating another list of theoretical findings, NodeZero WebApp provides evidence of what is truly exploitable so your team knows exactly what to fix first. Continuously Test the Web Applications Attackers Actually Target Traditional scanners and manual penetration tests provide valuable insight, but they can’t continuously validate how attackers move through modern web applications with authenticated workflows, business logic, and interconnected attack paths. NodeZero WebApp fills that gap by autonomously testing web applications the way attackers do. NodeZero WebApp helps organizations: Continuously crawl and discover modern web applications, APIs, and hidden routes Test authenticated, role-based workflows with credential and MFA support Validate business logic flaws, broken access control, IDOR, and BOLA vulnerabilities Safely test production, staging, and development environments with graduated testing modes Connect web application weaknesses to identity, cloud, and infrastructure attack paths Deliver replayable proof, screenshots, and request/response evidence developers can immediately verify Measure exploitable business risk instead of relying on vulnerability counts alone Security Teams Get More Than Findings—They Get Proof Every autonomous pentest produces clear evidence showing exactly how NodeZero navigated the application, what it discovered, and how weaknesses can be exploited. Reports connect application-layer vulnerabilities to broader attack paths and business impact, giving security teams actionable remediation guidance while providing audit-ready evidence for leadership and stakeholders. Core NodeZero WebApp Capabilities NodeZero WebApp combines modern web application testing with the broader NodeZero Proactive Security Platform through capabilities including: Production-safe graduated testing that expands safely as confidence grows Authenticated and role-aware testing for real user workflows Discovery of SPAs, REST, SOAP, and GraphQL APIs using headless browser crawling Unified attack path validation across web applications, identity, cloud, and infrastructure Business logic and access control testing for exploitable authorization weaknesses Replayable proof with screenshots, request/response details, and route context for rapid remediation See How NodeZero WebApp Validates Real-World Web Application Risk Download the NodeZero WebApp Factsheet to learn how Horizon3 helps organizations continuously validate exploitable web application risk through production-safe autonomous pentesting, authenticated testing, business logic validation, and replayable proof. Download as PDF How can NodeZero help you? Let our experts walk you through a demonstration of NodeZero ® , so you can see how to put it to work for your organization. Get a Demo Share:
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
Discover how World Wide Technology and Horizon3 help enterprises validate infrastructure readiness through continuous attack path validation and evidence-based cyber resilience.
```

#### Full body

```
The New Measure of Infrastructure Readiness Tim Finnell July 27, 2026 Blogs How World Wide Technology and Horizon3 help enterprises validate resilience against AI-accelerated threats. Enterprise infrastructure has always been built around a simple objective: keep the business running. Organizations have invested billions of dollars in networking, cloud platforms, identity systems, endpoint security, detection technologies, and resilience programs. Security teams continuously patch vulnerabilities, deploy new controls, validate configurations, and measure compliance against established frameworks. Those investments remain essential. They were also largely designed for a world where attackers operated at human speed. Artificial intelligence has changed that assumption. Today’s attackers can use AI to accelerate reconnaissance, develop exploits, analyze vast attack surfaces, identify exploitable weaknesses, and chain together complex attack paths in a fraction of the time previously required. Activities that once required skilled operators working methodically over days or weeks can increasingly be executed in minutes and repeated at virtually unlimited scale. As AI compresses the time between exposure and exploitation, organizations can no longer afford to assume their defenses work. Even so, Horizon3’s 2026 State of Assumed Security report found that only 30% of CISOs say their organizations routinely validate that risk has actually been remediated after patching, while nearly half simply rescan for vulnerabilities. Infrastructure readiness is no longer defined by what has been deployed. It is defined by what continues to perform when an AI-enabled attacker is actively trying to break it. Architecture Alone Is No Longer Enough Modern enterprises rarely lack security technology. Most have invested heavily in identity platforms, cloud security, network segmentation, endpoint protection, vulnerability management, SIEM, Zero Trust initiatives, and countless point solutions designed to reduce risk. Viewed individually, many of these technologies perform exceptionally well. Attackers, however, do not attack individual technologies. They exploit the spaces between them. A compromised identity becomes privileged access. A cloud misconfiguration becomes lateral movement. A trusted connection bypasses segmentation. Weaknesses that appear insignificant in isolation become significant when chained together into an attack path, and artificial intelligence accelerates every step of that process. That is why infrastructure can no longer be evaluated as a collection of independent technologies. It must be evaluated as an interconnected system operating under adversarial pressure. The question is no longer whether individual controls work. It is whether the architecture works. Defending at the Speed of AI Recognizing this shift, World Wide Technology recently launched its Defending at the Speed of AI initiative, bringing together leading technology partners to help organizations prepare for a new operating reality. The initiative reflects a broader shift in how organizations build and measure cyber resilience. Organizations are moving beyond periodic assessments toward continuous validation because confidence alone is no longer enough. As AI accelerates both attack speed and complexity, security leaders need evidence that their infrastructure, security controls, and operational defenses perform as intended under real-world conditions. That objective cannot be achieved by any single technology. It requires an ecosystem that combines validated offensive testing, resilient infrastructure, intelligent operations, and implementation expertise into a continuous operating model rather than a collection of isolated products. The natural question then becomes: How do you measure infrastructure readiness in the age of AI? From Confidence to Proof The first outcome of the WWT and Horizon3 partnership is the Mythos Infrastructure Readiness Assessment . Rat
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: The New Measure of Infrastructure Readiness
  - Published: 2026-07-27T14:15:00+00:00
  - Link: https://horizon3.ai/intelligence/blogs/infrastructure-readiness/
  - Summary: Discover how World Wide Technology and Horizon3 help enterprises validate infrastructure readiness through continuous attack path validation and evidence-based cyber resilience.

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

### Cluster b1e5db3b13 — score 10

- Title: Building secure Uniswap v4 hooks
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-07-30T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/07/30/building-secure-uniswap-v4-hooks/
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
Uniswap v4 hooks let developers add custom behavior to pools, including dynamic fees, custom accounting, and external integrations. This flexibility moves some security responsibilities into application and hook code. The Cork and Bunni exploits are two app-level incidents that show what can go wrong in that code. Together, they account for more than $20M in losses. Neither incident stemmed from a flaw in the Uniswap v4 core protocol or the PoolManager; both arose from application-specific authorization and accounting logic built around hooks. After analyzing dozens of findings from Trail of Bits audits (including our Uniswap v4-core security review ), public reports from other firms, and the Solodit database, I’ve identified seven recurring failure patterns in application and hook code, including missing caller checks and accounting bugs that still satisfy the PoolManager’s settlement invariant. Builders can use these patterns as a secure-development checklist; auditors can use them t
```

#### Full body

```
Page content Uniswap v4 hooks let developers add custom behavior to pools, including dynamic fees, custom accounting, and external integrations. This flexibility moves some security responsibilities into application and hook code. The Cork and Bunni exploits are two app-level incidents that show what can go wrong in that code. Together, they account for more than $20M in losses. Neither incident stemmed from a flaw in the Uniswap v4 core protocol or the PoolManager; both arose from application-specific authorization and accounting logic built around hooks. After analyzing dozens of findings from Trail of Bits audits (including our Uniswap v4-core security review ), public reports from other firms, and the Solodit database, I’ve identified seven recurring failure patterns in application and hook code, including missing caller checks and accounting bugs that still satisfy the PoolManager’s settlement invariant. Builders can use these patterns as a secure-development checklist; auditors can use them to focus their review. What the PoolManager guarantees If you’re familiar with Uniswap v3, where each pool was a separate contract, v4 inverts the model. All pool state now lives in a singleton PoolManager contract, with each pool represented in its storage. Uniswap v4 adds hooks: independent contracts that execute custom logic at specific points in the swap and liquidity lifecycle. Figure 1: Pools live inside the singleton PoolManager, and multiple pools can use the same hook contract. Here’s what a pool looks like in v4: struct PoolKey { Currency currency0; Currency currency1; uint24 fee; int24 tickSpacing; IHooks hooks; } Figure 2: A pool's PoolKey includes both currencies, the fee, tick spacing, and the hook address ( v4-core/src/types/PoolKey.sol ). Notice that the hook address ( IHooks hooks; ) is part of the pool’s identity. If you change any of these fields, you’re talking to a different pool. This matters because trusting the wrong PoolKey means trusting the wrong pool. v4 also introduces a session-based model that works like a flash loan. Your contract calls unlock() on the PoolManager, which triggers a callback into your code. At the end, the PoolManager checks that no unsettled currency deltas remain: function unlock(bytes calldata data) external returns (bytes memory result) { Lock.unlock(); // ... callback execution happens here ... if (NonzeroDeltaCount.read() != 0) revert CurrencyNotSettled(); Lock.lock(); } Figure 3: Simplified PoolManager.unlock() flow: unlock the session, execute the callback, and revert unless all currency deltas settle to zero ( v4-core/src/PoolManager.sol ). Figure 4: A periphery or hook calls PoolManager.unlock(), handles unlockCallback(), and calls swap() inside the unlocked session. The PoolManager enforces v4’s protocol mechanics, including pool initialization rules, swap and liquidity math, hook-callback sequencing, and end-of-session settlement. Hook developers are responsible for validating the application-specific assumptions their hooks add. Each hook must decide: Who can call its privileged paths Which pools are legitimate How custom balances and deltas should be accounted for Whether external integrations can fail or reenter safely 1. Anyone can call your hook Hook callbacks are external functions on your contract. If you don’t check the caller, an attacker can call those callbacks directly with malicious parameters. A loose unlockCallback path can also reach internal actions that should never be callable. The fix: use BaseHook for hook entrypoints and SafeCallback for unlockCallback . Together, they enforce caller checks on the callback paths they cover: modifier onlyPoolManager() { if (msg.sender != address(poolManager)) revert NotPoolManager(); _; } Figure 5: onlyPoolManager restricts hook callbacks to the configured PoolManager. Add an equivalent caller check only on paths those contracts don’t cover. Real-world example: The Cork exploit (~$12M, May 2025) shows why this check matte
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: Building secure Uniswap v4 hooks
  - Published: 2026-07-30T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/07/30/building-secure-uniswap-v4-hooks/
  - Summary: Uniswap v4 hooks let developers add custom behavior to pools, including dynamic fees, custom accounting, and external integrations. This flexibility moves some security responsibilities into application and hook code. The Cork and Bunni exploits are two app-level incidents that show what can go wrong in that code. Together, they account for more than $20M in losses. Neither incident stemmed from a flaw in the Uniswap v4 core protocol or the PoolManager; both arose from application-specific authorization and accounting logic built around hooks. After analyzing dozens of findings from Trail of Bits audits (including our Uniswap v4-core security review ), public reports from other firms, and the Solodit database, I’ve identified seven recurring failure patterns in application and hook code, including missing caller checks and accounting bugs that still satisfy the PoolManager’s settlement invariant. Builders can use these patterns as a secure-development checklist; auditors can use them t

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

### Cluster 1cd705f068 — score 10

- Title: Brinks Home Discloses Data Breach as Hackers Leak Files
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-03T11:45:14+00:00
- Link: https://www.securityweek.com/brinks-home-discloses-data-breach-as-hackers-leak-files/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, data_breach, ransomware_extortion
- actor_attribution: ShinyHunters
- affected_industries: financial_services
- affected_products: AWS, Salesforce, SonicWall
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, apt_espionage
- actor_attribution: ShinyHunters
- affected_industries: financial_services
- affected_products: Salesforce, SonicWall, AWS
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The physical security firm says its alarm monitoring and system functionality have not been affected. The post Brinks Home Discloses Data Breach as Hackers Leak Files appeared first on SecurityWeek .
```

#### Full body

```
The infamous ShinyHunters extortion group has leaked over 41 gigabytes of data allegedly stolen from the physical security firm Brinks Home. Headquartered in Dallas, Texas, Brinks Home provides home security systems backed by an alarm response center. Last week, the company announced that hackers accessed a portion of its IT systems and that they threatened to leak information allegedly stolen during the incident. “We are aware that such material may be posted publicly. Brinks Home is working diligently to determine what information was involved and who may be affected,” the company said in an incident notice . Noting that it would notify potentially affected individuals if their personal information was compromised, Brinks Home pointed out that customers should remain “vigilant against unsolicited emails, text messages, or phone calls requesting personal information or account credentials”. According to Brinks Home, its alarm monitoring and system functionality has not been affected, as the attackers did not access its products or services. Advertisement. Scroll to continue reading. The company has not shared details on the threat actor responsible for the incident, but its disclosure came around the same time that ShinyHunters added Brinks Home to its Tor-based leak site. More than 4.9 million records were stolen from Brinks Home’s Salesforce instance during the incident, the extortion group says. Brinks Home hacked by ShinyHunters As the physical security firm did not pay a ransom, the hackers have leaked online more than 41GB of files allegedly stolen during the incident. Some of the stolen records, ShinyHunters claims, include personally identifiable information (PII). SecurityWeek has not independently confirmed the hackers’ claims. Related: Russian State APT Linked to Recent Public Wi-Fi Gateway Hacking Related: CareCloud Data Breach Impacts Over 350,000 Related: Semiconductor Firm Analog Devices Discloses Data Breach Related: ShinyHunters Claims Ernst & Young Hack Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Critical Flaw Allowed to Azure Cosmos DB Pwnage CareCloud Data Breach Impacts Over 350,000 Critical Code Execution Vulnerability Patched in TeamCity DataBahn Raises $40 Million for Agentic Data Pipeline Management Discern Security Raises $13 Million in Series A Funding Cantina Emerges From Stealth With $8 Million in Funding Critical Ruflo Flaw Lets Attackers Spawn Rogue AI Swarms US and Allies Update SBOM Guidance Latest News Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks Russian State APT Linked to Recent Public Wi-Fi Gateway Hacking US Water Cyberattacks Extend Beyond Minnesota to at Least 6 Other States Balance Theory Raises $19 Million to Help Enterprises Manage Cybersecurity Investments Ruby on Rails Patches Critical Vulnerability In Other News: OpenAI Open Source Tool, AWS Links Hacks to North Korea, Mythos Crypto Research Cyberattacks on Minnesota Water Systems Investigated as Officials Warn About Iranian Hackers Google AI Uncovers 13-Year-Old Chrome Flaw Amid Record Patching Pace Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Rethinking Cyber Defense for AI-Speed Attacks August 18, 2026 Join this live webinar as we explore if detection-first security operations can keep pace with AI, or if it’s time to rethink prevention as the strongest default. Register Virtual Event: CodeSecCon 2026 August 19, 2026 CodeSecCon bridges the gap between dev and security. Discover best practices for secure coding, innovative risk-reduction tools, and safe AI integration to cultivate a true DevSecOps culture. Safely secure your apps! Register People
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Brinks Home Discloses Data Breach as Hackers Leak Files
  - Published: 2026-08-03T11:45:14+00:00
  - Link: https://www.securityweek.com/brinks-home-discloses-data-breach-as-hackers-leak-files/
  - Summary: The physical security firm says its alarm monitoring and system functionality have not been affected. The post Brinks Home Discloses Data Breach as Hackers Leak Files appeared first on SecurityWeek .

### Cluster 1b4f7b92ff — score 10

- Title: Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-08-03T10:39:41+00:00
- Link: https://www.securityweek.com/recent-sonicwall-vulnerabilities-exploited-in-ransomware-attacks/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: SonicWall

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, data_breach, ransomware_extortion, web_shell_backdoor
- affected_industries: government
- affected_products: Azure, OpenAI/ChatGPT, SonicWall
- cve_ids: CVE-2026-15409, CVE-2026-15410
- urgency_signals: actively_exploited, preauth_unauth
- content_type: incident_report, news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach, apt_espionage, web_shell_backdoor, active_exploitation
- affected_industries: government
- affected_products: SonicWall, OpenAI/ChatGPT, Azure
- cve_ids: CVE-2026-15409, CVE-2026-15410
- urgency_signals: actively_exploited, preauth_unauth
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
The INC Ransomware gang has been targeting vulnerable SMA1000 appliances for root access and lateral movement. The post Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks appeared first on SecurityWeek .
```

#### Full body

```
The INC Ransomware group is responsible for most of the recent activity surrounding two fresh vulnerabilities in SonicWall’s SMA1000 secure remote access appliances, Resecurity reports. Tracked as CVE-2026-15409 (CVSS score of 10) and CVE-2026-15410 (CVSS score of 7.2), the security defects allow unauthenticated remote attackers to open a WebSocket tunnel to restricted services and escalate their privileges to root. Patched on July 14 and added to CISA’s Known Exploited Vulnerabilities (KEV) catalog on the same day, the two flaws had been exploited in the wild as zero-days since at least June 22 . Cybersecurity firm Volexity attributed the observed exploitation to a threat actor tracked as UTA0533, noting that it was harvesting credentials from the hacked appliances and deploying malicious files, but was less successful in moving laterally to other systems. Rapid7, on the other hand, observed threat actors pivoting from SMA1000 devices into internal corporate networks, likely after deploying a backdoor on the compromised appliances. Now, Resecurity says that, of the various threat actors chaining CVE-2026-15409 and CVE-2026-15410 for SMA1000 compromise, the INC Ransomware gang has emerged as the most active one. Advertisement. Scroll to continue reading. “Notably, as of the beginning of August 2026, INC Ransomware has accelerated its activity. Multiple new victims have been published on their Data Leak Site (DLS),” the company says. Over the past couple of weeks, the ransomware group has listed on its leak site private and government sector organizations from the US, Australia, UAE, Colombia, and Switzerland, among others. “Resecurity has assisted several victims with DFIR and vulnerability assessments to contain the root cause of the compromise, but also learned about the following new developments: many of the new victims received emails, as well as phone calls from unknown organizations claiming to assist with ransomware issues,” the company says. In one instance, the email came from a domain registered after the exploitation activity, through a Chinese domain registrar. The victims were also contacted by phone by a threat actor calling themselves Andrew and claiming to be representing a group of hackers. “At the end of the call, the individual provided the email address info@helprans[.]com for further negotiations and then ended the call. Such methods are frequently used by ransomware groups as ‘pressure tactics’,” Resecurity notes. As ransomware groups continue to target the SonicWall vulnerabilities, users are advised to patch their SMA1000 appliances as soon as possible and to perform threat hunting to identify potential compromises. Related: US Water Cyberattacks Extend Beyond Minnesota to at Least 6 Other States Related: Ruby on Rails Patches Critical Vulnerability Related: Google AI Uncovers 13-Year-Old Chrome Flaw Amid Record Patching Pace Related: Critical Flaw Allowed to Azure Cosmos DB Pwnage Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire Critical Flaw Allowed to Azure Cosmos DB Pwnage CareCloud Data Breach Impacts Over 350,000 Critical Code Execution Vulnerability Patched in TeamCity DataBahn Raises $40 Million for Agentic Data Pipeline Management Discern Security Raises $13 Million in Series A Funding Cantina Emerges From Stealth With $8 Million in Funding Critical Ruflo Flaw Lets Attackers Spawn Rogue AI Swarms US and Allies Update SBOM Guidance Latest News Brinks Home Discloses Data Breach as Hackers Leak Files Russian State APT Linked to Recent Public Wi-Fi Gateway Hacking US Water Cyberattacks Extend Beyond Minnesota to at Least 6 Other States Balance Theory Raises $19 Million to Help Enterprises Manage Cybersecurity Investments Ruby on Rails Patches Critical Vulnerability In Other News: OpenAI Open Sourc
```

#### Corroborating sources (2)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks
  - Published: 2026-08-03T10:39:41+00:00
  - Link: https://www.securityweek.com/recent-sonicwall-vulnerabilities-exploited-in-ransomware-attacks/
  - Summary: The INC Ransomware gang has been targeting vulnerable SMA1000 appliances for root access and lateral movement. The post Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ThreatsDay: AI-Powered Hacking, 370 Chrome Flaws, SonicWall Attacks, DNS Hijacking + 22 More Stories
  - Published: 2026-07-30T15:25:57+00:00
  - Link: https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html
  - Summary: A lot of security still comes down to trusting the wrong screen. This week, that screen might be a login page, an install guide, a recruiter call, or a familiar service behaving slightly wrong. Behind it: reused credentials, exposed systems, quiet loaders, abused trust, and exploit paths that should have been harder. Some defenses improved. The loose parts still got found first. Anyway,

### Cluster c97bc0e859 — score 10

- Title: Sponsored: The intrusion signals hiding in plain sight
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-08-03T00:22:38+00:00
- Link: https://risky.biz/RBNEWSSI138/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: AWS, ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: ddos, ransomware_extortion
- actor_attribution: ShinyHunters
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: ShinyHunters
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
In this sponsored interview James Wilson chats with Permiso CTO Ian Ahl about detecting ShinyHunters-style attackers as they move through cloud and SaaS environments. Ian explains how ordinary-looking events such as a password reset, a new MFA device, unusual searches and a first-time AWS role assumption can combine to reveal an intrusion. Permiso’s platform connects these signals across identity providers, cloud platforms and SaaS applications. They also discuss how AI is helping attackers move from initial access to extortion in just four hours.
```

#### Full body

```
Risky Bulletin Podcast August 03, 2026 Sponsored: The intrusion signals hiding in plain sight Presented by James Wilson Technology Editor In this sponsored interview James Wilson chats with Permiso CTO Ian Ahl about detecting ShinyHunters-style attackers as they move through cloud and SaaS environments. Ian explains how ordinary-looking events such as a password reset, a new MFA device, unusual searches and a first-time AWS role assumption can combine to reveal an intrusion. Permisoâs platform connects these signals across identity providers, cloud platforms and SaaS applications. They also discuss how AI is helping attackers move from initial access to extortion in just four hours. Your browser does not support the audio element. Sponsored: The intrusion signals hiding in plain sight â¶ 0:00 / 15:36 Subscribe Brought to you by Permiso Monitor All Identities In All Environments
```

#### Corroborating sources (2)

- **Risky Business News** (practitioner_analysis)
  - Title: Sponsored: The intrusion signals hiding in plain sight
  - Published: 2026-08-03T00:22:38+00:00
  - Link: https://risky.biz/RBNEWSSI138/
  - Summary: In this sponsored interview James Wilson chats with Permiso CTO Ian Ahl about detecting ShinyHunters-style attackers as they move through cloud and SaaS environments. Ian explains how ordinary-looking events such as a password reset, a new MFA device, unusual searches and a first-time AWS role assumption can combine to reveal an intrusion. Permiso’s platform connects these signals across identity providers, cloud platforms and SaaS applications. They also discuss how AI is helping attackers move from initial access to extortion in just four hours.
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Extend Amazon Inspector SBOM Generator with Plugins
  - Published: 2026-07-30T17:22:54+00:00
  - Link: https://aws.amazon.com/blogs/security/extend-amazon-inspector-sbom-generator-with-plugins/
  - Summary: Amazon Inspector is an automated vulnerability management service that continually scans Amazon Web Services (AWS) workloads for software vulnerabilities. The vulnerability management capabilities of Amazon Inspector are powered by an asset inventory engine known as the Amazon Inspector SBOM Generator (inspector-sbomgen), a standalone command-line tool that produces a software bill of materials (SBOM) from container […]

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

### Cluster 2126e62d58 — score 9

- Title: Rails patches critical Active Storage flaw with RCE potential
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-08-01T14:20:30+00:00
- Link: https://www.bleepingcomputer.com/news/security/rails-patches-critical-active-storage-flaw-with-rce-potential/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-66066
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-66066
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A critical vulnerability in the Active Storage framework can allow an unauthenticated attacker to read arbitrary files from a Rails application, and potentially escalate to remote code execution (RCE). [...]
```

#### Full body

```
Rails patches critical Active Storage flaw with RCE potential By Bill Toulas August 1, 2026 10:20 AM 0 A critical vulnerability in the Active Storage framework can allow an unauthenticated attacker to read arbitrary files from a Rails application, and potentially escalate to remote code execution (RCE). Rails is a popular open-source web application framework written in Ruby for building websites and web apps. It uses the built-in Rails component Active Storage for handling file uploads and attachments. Rails maintainers published an advisory about the CVE-2026-66066 flaw, which received a critical severity rating. Active Storage may also generate image thumbnails from uploaded media using image processing libraries such as libvips or ImageMagick . According to the security bulletin , CVE-2026-66066 is exploitable when libvips is used, allowing an attacker to upload a specially crafted image to a vulnerable application and read arbitrary files on the server. Another prerequisite for the attack is that the server needs to allow image uploads from untrusted users. If these requirements are met, an attacker may access app files, including the process environment, which typically contains ‘secret_key_base’ and credentials for databases, cloud storage, and other services. CVE-2026-66066 impacts Active Storage before 7.2.3.2, 8.0.x before 8.0.5.1, and 8.1.x before 8.1.3.1. Rails 6.x is only affected if Active Storage has been configured outside its defaults. The Rails team recommends upgrading to libvips 8.13 or later and rotating the ‘secret_key_base’ (the Rails master key), database credentials, Active Storage service credentials, and any other secrets accessible to the application process. For systems running libvips 8.13 or later, administrators can temporarily disable the vulnerable functionality by setting the VIPS_BLOCK_UNTRUSTED environment variable or calling Vips.block_untrusted(true) when using ruby-vips 2.2.1 or newer. There is no workaround available for apps that use libvips before 8.13. ImageMagick users are not affected by this vector. However, libvips is the default processor in the official Rails Docker images, and also Debian and Ubuntu setups. The Rails team said it has intentionally withheld technical details for the vulnerability to reduce the risk of exploitation before users have time to apply the updates. Full technical details were initially scheduled to be disclosed on August 28 on the Rails forums . However, because public proof-of-concept (PoC) exploits became available very quickly, the maintainers decided to publish the full details as well as forensic investigation tooling . The vulnerability was discovered and responsibly reported to the Rails team by researchers from Ethiack and GMO Flatt Security Inc. Security firm Akamai has also published a warning about CVE-2026-66066, naming the attack chain “KindaRails2Shell,” and warning about its RCE potential. “With the secret_key_base compromised, the attacker holds the master cryptographic key to the application,” explains Akamai . “They can forge session cookies, sign global IDs, and manipulate serialized data, which directly translates into full RCE on the underlying server.” Akamai says it coordinated with Ethiack before public disclosure to prepare protections for customers, and has now released web application firewall (WAF) protections. Ethiack noted that a WAF might buy admins some time, but attackers using AI tooling should be able to reconstruct the attack chain based on the patch diffs. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: JetBrains warns of critical TeamCity remote code execution flaw vBulletin fixes critical pre-auth RCE flaw with public exploit Hackers target US firm
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Rails patches critical Active Storage flaw with RCE potential
  - Published: 2026-08-01T14:20:30+00:00
  - Link: https://www.bleepingcomputer.com/news/security/rails-patches-critical-active-storage-flaw-with-rce-potential/
  - Summary: A critical vulnerability in the Active Storage framework can allow an unauthenticated attacker to read arbitrary files from a Rails application, and potentially escalate to remote code execution (RCE). [...]

### Cluster 532de505b8 — score 9

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
Simon Willison’s Weblog Subscribe Sponsored by: AWS — Move from SaaS to Agentic SaaS with resources for ISVs at every layer of the stack. Explore how AI for ISVs turns vision into results 28th July 2026 We’re aware a Modal customer published an unauthenticated endpoint that allowed ​anyone on the internet to use ​their ⁠sandboxes for code execution. This was used by the rogue agent. Modal’s ⁠platform ​or isolation were not ​compromised in anyway. — Akshat Bubna , Modal's CTO, talking to Reuters about this incident Posted 28th July 2026 at 10:05 pm Recent articles Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp) - 31st July 2026 OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened - 22nd July 2026 A Fireside Chat with Cat and Thariq from the Claude Code team - 21st July 2026 This is a quotation collected by Simon Willison, posted on 28th July 2026 . sandboxing 52 security 620 openai 441 ai-security-research 33 openai-hugging-face-incident 6 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Akshat Bubna
  - Published: 2026-07-28T22:05:55+00:00
  - Link: https://simonwillison.net/2026/Jul/28/akshat-bubna/#atom-everything
  - Summary: We’re aware a Modal customer published an unauthenticated endpoint that allowed ​anyone on the internet to use ​their ⁠sandboxes for code execution. This was used by the rogue agent. Modal’s ⁠platform ​or isolation were not ​compromised in anyway. — Akshat Bubna , Modal's CTO, talking to Reuters about this incident Tags: ai-security-research , openai , sandboxing , security , openai-hugging-face-incident

### Cluster e948af82c6 — score 9

- Title: Hugging Face Diffusers Flaws Could Let Model Repositories Execute Arbitrary Code
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-03T06:40:31+00:00
- Link: https://thehackernews.com/2026/08/hugging-face-diffusers-flaws-could-let.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_products: GitHub
- cve_ids: CVE-2026-44513, CVE-2026-44827, CVE-2026-45804
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_products: GitHub
- cve_ids: CVE-2026-44827, CVE-2026-45804, CVE-2026-44513
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Three high-severity security flaws have been disclosed in Hugging Face's Diffusers library that could allow crafted model repositories to stealthily execute arbitrary code on machines that load it, opening the artificial intelligence (AI) supply chain to security risk. "These vulnerabilities are bypassing trust_remote_code, the safeguard designed to stop unreviewed code from running in the
```

#### Full body

```
Hugging Face Diffusers Flaws Could Let Model Repositories Execute Arbitrary Code  Ravie Lakshmanan  Aug 03, 2026 Vulnerability / AI Security Three high-severity security flaws have been disclosed in Hugging Face's Diffusers library that could allow crafted model repositories to stealthily execute arbitrary code on machines that load it, opening the artificial intelligence (AI) supply chain to security risk. "These vulnerabilities are bypassing trust_remote_code, the safeguard designed to stop unreviewed code from running in the custom pipelines loading process," Zafran Labs researchers Gal Zaban and Ido Shani said in an analysis published last week. The shortcomings have been collectively named FaceHugger . With Hugging Face becoming the "GitHub of the AI era" and its libraries and repositories prevalent in enterprise environments, vulnerabilities in libraries like Diffusers can grant attackers extensive access owing to how the library is embedded into production pipelines, CI/CD systems, and container images. Diffusers is a Python package that serves as a library of state-of-the-art (SOTA) pretrained diffusion models for generating videos, images, and audio. According to statistics shared on pepy.tech, the package has been downloaded more than 8.1 million times in July 2026. One of the key capabilities of the library is to locally load a model from a Hugging Face hub repository via the DiffusionPipeline API, which, in turn, makes use of a configuration file to initialize specific pipeline and component classes, along with custom pipeline code. The "trust_remote_code" parameter in Diffusers is a security safeguard that controls whether custom Python code hosted inside a model repository is allowed to execute during "from_pretrained()" loading. Setting it to "True" permits custom code execution, while "False" or omitting it blocks unverified code from running. "The root cause of all different RCE variants [...] is that the trust check lives entirely in the first phase," Zafran explained. "Therefore, any method that makes the loader see custom code that the gate did not, allows bypassing the trust_remote_code mechanism." Each variant has been traced back to a case of Time-of-Check to Time-of-Use (TOCTOU), with the model download designed as two sequential, non-atomic HTTP requests instead of one a "single atomic operation" and the "trust_remote_code" security gate configured to run only against the first. The vulnerabilities are listed below - CVE-2026-44827 (CVSS score: 8.8) - A code injection vulnerability that allows arbitrary code to be loaded through the custom_pipeline flow from a Hub repository by means of a crafted pipeline with the name "None.py" despite passing trust_remote_code=False (or omitting it, which is the default). CVE-2026-45804 (CVSS score: 7.5) - A race condition vulnerability that allows arbitrary code to be introduced to a repository by modifying the configuration between the hf_hub_download and snapshot_download HTTP calls to the Hub, leading to code execution. CVE-2026-44513 (CVSS score: 8.8) - A code injection vulnerability that allows arbitrary code to be loaded through the custom_pipeline flow from a Hub repository despite passing trust_remote_code=False (or omitting it). Following responsible disclosure, the vulnerabilities were addressed in Diffusers version 0.38.0, released in early May 2026. Any user who invokes "DiffusionPipeline.from_pretrained" with custom pipelines is impacted. "The underlying problem is that artifacts pulled from AI repositories are frequently treated as passive data, when configuration files, loaders, and custom pipeline code can quietly cross into executable code and turn a routine model load into an initial-access vector," the researchers added. If immediate patching is not an option, the project maintainers have recommended the following workarounds - Only call from_pretrained with pretrained_model_name_or_path, custom_pipeline, and local snapshot directories from full
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hugging Face Diffusers Flaws Could Let Model Repositories Execute Arbitrary Code
  - Published: 2026-08-03T06:40:31+00:00
  - Link: https://thehackernews.com/2026/08/hugging-face-diffusers-flaws-could-let.html
  - Summary: Three high-severity security flaws have been disclosed in Hugging Face's Diffusers library that could allow crafted model repositories to stealthily execute arbitrary code on machines that load it, opening the artificial intelligence (AI) supply chain to security risk. "These vulnerabilities are bypassing trust_remote_code, the safeguard designed to stop unreviewed code from running in the

### Cluster b138851666 — score 9

- Title: Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-01T07:12:42+00:00
- Link: https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48449

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ai_security
- affected_industries: manufacturing_industrial
- affected_products: GitHub, Microsoft SharePoint, OpenAI/ChatGPT
- cve_ids: CVE-2026-48390, CVE-2026-48395, CVE-2026-48396, CVE-2026-48448, CVE-2026-48449
- urgency_signals: actively_exploited, critical_cvss, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ai_security, active_exploitation
- affected_industries: manufacturing_industrial
- affected_products: Microsoft SharePoint, GitHub, OpenAI/ChatGPT
- cve_ids: CVE-2026-48449, CVE-2026-48448, CVE-2026-48395, CVE-2026-48396, CVE-2026-48390
- urgency_signals: actively_exploited, poc_available, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Adobe has released security updates to address a maximum-severity security flaw in Campaign Classic (ACC), its enterprise-focused marketing automation platform, that could result in arbitrary code execution. The vulnerability, tracked as CVE-2026-48449, carries a severity score of 10.0 on the CVSS scoring system. It has been described as a case of incorrect authorization that could result in
```

#### Full body

```
Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction  Ravie Lakshmanan  Aug 01, 2026 Vulnerability / Enterprise Security Adobe has released security updates to address a maximum-severity security flaw in Campaign Classic (ACC), its enterprise-focused marketing automation platform, that could result in arbitrary code execution. The vulnerability, tracked as CVE-2026-48449 , carries a severity score of 10.0 on the CVSS scoring system. It has been described as a case of incorrect authorization that could result in arbitrary code execution in the context of the current user without requiring any user interaction. The update also resolves another high-severity flaw ( CVE-2026-48448 , CVSS score: 8.6) stemming from SQL injection that could pave the way for arbitrary file reads. "This update addresses critical vulnerabilities that could result in arbitrary code execution and arbitrary file system read," Adobe said in an advisory. The company noted that it's not aware of any of the flaws being exploited in the wild. Both shortcomings have been addressed in ACC v7: 7.4.3 build 9398 for Windows and Linux. Separately, Adobe has also shipped updates to remediate eight critical-rated flaws in Adobe Bridge that could lead to privilege escalation and arbitrary code execution - CVE-2026-48395 (CVSS score: 8.6) - An untrusted search path vulnerability that leads to arbitrary code execution CVE-2026-48396 (CVSS score: 8.6) - An incorrect authorization vulnerability that leads to arbitrary code execution CVE-2026-48390 (CVSS score: 8.6) - An incorrect authorization vulnerability that leads to privilege escalation CVE-2026-48391 (CVSS score: 8.2) - An untrusted search path vulnerability that leads to arbitrary code execution CVE-2026-48374 (CVSS score: 7.8) - A path traversal vulnerability that leads to arbitrary code execution CVE-2026-48392 (CVSS score: 7.8) - An out-of-bounds write vulnerability that leads to arbitrary code execution CVE-2026-48393 (CVSS score: 7.8) - An out-of-bounds write vulnerability that leads to arbitrary code execution CVE-2026-48394 (CVSS score: 7.8) - An out-of-bounds write vulnerability that leads to arbitrary code execution Adobe credited security researcher Kieran ("kaiksi") with discovering and reporting CVE-2026-48390, CVE-2026-48391, CVE-2026-48395, CVE-2026-48396, and CVE-2026-48374, and "yjdfy" for CVE-2026-48392, CVE-2026-48393, and CVE-2026-48394. Users are advised to apply the latest updates for optimal protection. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Adobe , Application Security , Code Execution , enterprise security , Linux security , privilege escalation , SQL Injection , Vulnerability , Windows Security ⚡ Top Stories This Week New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents OpenAI Says Its AI Models Escaped Sandbox, Targeted Hugging Face to Cheat Benchmark Adobe Acrobat Extension Flaw Let Malicious Sites Read WhatsApp Web Data Ubuntu snap-confine Flaw Could Give Local Users Root on Default Desktop Installs Nine-Year-Old RefluXFS Linux Flaw Gives Local Users Root on Default RHEL Installs Attackers Weaponize GitHub Actions Runners to Target cPanel and WHM Servers Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files ThreatsDay: Android Spyware, PLC Attacks, AI Image Prompt Injection + 12 More Stories Kimi K3 Agents Found Redis Zero-Days and Built RCE Exploit, Researchers Say Hacker Runs Hermes AI Agent Unattended
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Adobe Campaign Classic CVSS 10.0 Flaw Could Run Code Without User Interaction
  - Published: 2026-08-01T07:12:42+00:00
  - Link: https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html
  - Summary: Adobe has released security updates to address a maximum-severity security flaw in Campaign Classic (ACC), its enterprise-focused marketing automation platform, that could result in arbitrary code execution. The vulnerability, tracked as CVE-2026-48449, carries a severity score of 10.0 on the CVSS scoring system. It has been described as a case of incorrect authorization that could result in

### Cluster 0c9658fc3f — score 9

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

### Cluster 602e22dfe4 — score 9

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
Long-Lived Vulnerability in Microsoft Secure Boot Microsoft’s Secure Boot has had a serious vulnerability for most of its existence. An industry-wide standard Microsoft invented to protect Windows, and later Linux, devices from firmware infections has been trivial to bypass for 13 of its 14 years of existence. The discovery was made by researchers at security firm ESET after identifying 11 firmware images, at least one from 2013, that were known to be defective but remained signed by the software company anyway. The images are known as shims , which were invented to extend Secure Boot to Linux devices and utility software. Using a technique simple enough to be performed by novice hackers, these old, forgotten shims can be used to completely circumvent the protection, which is embedded into the UEFI (Unified Extensible Firmware Interface) of the device’s motherboard. The gaffe is the result of the failure by Microsoft, which oversees the signing of shims, to revoke the publicly available images once vulnerabilities were found in them. Tags: firmware , Microsoft , vulnerabilities Posted on July 29, 2026 at 7:01 AM • 7 Comments
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Long-Lived Vulnerability in Microsoft Secure Boot
  - Published: 2026-07-29T11:01:09+00:00
  - Link: https://www.schneier.com/blog/archives/2026/07/long-lived-vulnerability-in-microsoft-secure-boot.html
  - Summary: Microsoft’s Secure Boot has had a serious vulnerability for most of its existence. An industry-wide standard Microsoft invented to protect Windows, and later Linux, devices from firmware infections has been trivial to bypass for 13 of its 14 years of existence. The discovery was made by researchers at security firm ESET after identifying 11 firmware images, at least one from 2013, that were known to be defective but remained signed by the software company anyway. The images are known as shims , which were invented to extend Secure Boot to Linux devices and utility software. Using a technique simple enough to be performed by novice hackers, these old, forgotten shims can be used to completely circumvent the protection, which is embedded into the UEFI (Unified Extensible Firmware Interface) of the device’s motherboard. The gaffe is the result of the failure by Microsoft, which oversees the signing of shims, to revoke the publicly available images once vulnerabilities were found in them..

### Cluster f0a862553c — score 9

- Title: CosmosEscape: Taking Over Every Database in Azure Cosmos DB
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-07-30T12:00:01+00:00
- Link: https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: Azure

#### Cluster taxonomy (union across members)
- affected_products: Azure, Google Cloud, Microsoft/Copilot
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: Azure, Microsoft/Copilot
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A critical vulnerability chain in Azure Cosmos DB enabled full read and write access to every Cosmos DB database.
```

#### Full body

```
Wiz Pricing Get a demo Get a demo Wiz Research uncovered CosmosEscape , a critical vulnerability in Azure’s flagship database service, Azure Cosmos DB, via its Gremlin API. The vulnerability could have been exploited to compromise every database in the service, including Microsoft's own internal databases - potentially enabling a cross-service attack. Through CosmosEscape, attackers could have acquired what we’ve dubbed the Cosmos Master Key - a platform-wide secret that granted two incredibly powerful capabilities: Takeover - retrieving the primary key of any Cosmos DB account on demand, resulting in full read & write access. Enumeration - listing all databases on the service with the ability to filter by specific organization identifiers like subscription and tenant IDs. Chained together, these capabilities could have enabled precision targeting at platform scale: from identifying a specific organization's databases to compromising them, all from publicly accessible endpoints. Cosmos DB is used internally across Microsoft - services like Microsoft Entra ID , Microsoft Teams , and Microsoft Copilot all store data in Cosmos DB. Their databases were potentially accessible via this vulnerability. Microsoft has now fully remediated the issue, including eliminating the Cosmos Master Key. Microsoft also introduced new guardrails to Cosmos DB to prevent similar attacks. Figure 1: CosmosEscape’s impact This research was assisted by an early version of Atlas , our AI vulnerability researcher. Expect more from Atlas soon. Required Actions Microsoft has fully remediated this issue. No customer action is required. Microsoft conducted a thorough investigation and found no evidence of exploitation of this vulnerability beyond the research described in this blog. From a Single Query to Unlocking Every Database Cosmos DB supports multiple query APIs, and among them is Gremlin , a popular graph query language: // Find all users over 30 and return their friends ' names g.V().hasLabel(' user ').has(' age ', gt(30)).out(' knows ').values(' name ') While running Gremlin queries against Cosmos DB, we noticed a suspicious .NET exception. Since most open-source Gremlin stacks are JVM-based, the exception suggested that Cosmos DB was using a custom Gremlin engine . This was interesting - unlike standard SQL, where the engine maps queries to a fixed set of built-in operations, Gremlin servers often compile queries into executable code and run it in a restricted environment. Historically, these sandboxes haven't held up well . We suspected Cosmos DB's Gremlin sandbox may be vulnerable as well. And it was. Cosmos DB's engine translated Gremlin queries into .NET code, enforcing a set of restrictions designed to prevent queries from reaching beyond Gremlin operations. These restrictions, however, didn't sufficiently account for .NET reflection - allowing us to develop file read, write, and ultimately arbitrary code execution primitives, all through queries against our own database. The following image shows the output of a specially crafted Gremlin query ran against our database, resulting in the hostname command being executed on the Cosmos DB backend: Figure 2: Executing hostname on the Cosmos DB backend via the Gremlin API. See the full query in our upcoming BlackHat USA talk. By bypassing the Gremlin sandbox, we’ve gained code execution on the DB Gateway , a service that executes customer queries on their behalf, running on multi-tenant Service Fabric clusters. Looking around, customer databases weren’t hosted on these clusters, but the DB Gateway still had to reach them somehow. It turned out that it did so like any Cosmos DB client would - using the target account’s primary key , which grants full read-write access to the account’s databases. But how can the DB Gateway retrieve the primary key of our Cosmos DB account? The Cosmos Master Key Through credentials available on the cluster, the DB Gateway accessed a signing key that could retrieve the re
```

#### Corroborating sources (3)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: CosmosEscape: Taking Over Every Database in Azure Cosmos DB
  - Published: 2026-07-30T12:00:01+00:00
  - Link: https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db
  - Summary: A critical vulnerability chain in Azure Cosmos DB enabled full read and write access to every Cosmos DB database.
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: 'Confused Deputy' Flaws Persist in Google Cloud, Microsoft Azure
  - Published: 2026-07-27T20:57:26+00:00
  - Link: https://www.darkreading.com/cloud-security/confused-deputy-flaws-google-cloud-microsoft-azure
  - Summary: This category of vulnerabilities allows an attacker to easily acquire administrative level permissions and bypass cloud providers' access controls.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database
  - Published: 2026-07-30T13:34:09+00:00
  - Link: https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html
  - Summary: A now-patched vulnerability in Azure Cosmos DB could have let an attacker escape the service's Gremlin query sandbox and obtain full read and write access to databases across customer tenants, according to Wiz. Wiz, which codenamed the chain CosmosEscape, said the exploit chain began with a crafted query against a Gremlin database controlled by the attacker. From there, code execution on a

### Cluster c99323e585 — score 8

- Title: Max-severity Exchange server flaw under active exploitation by Kremlin hackers
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-07-30T19:01:12+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/max-severity-exchange-server-flaw-under-active-exploitation-kremlin-hackers
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor, zero_day
- cve_ids: CVE-2026-42897
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor
- cve_ids: CVE-2026-42897
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
Text settings Story text Size Small Standard Large Width * Standard Wide Links Standard Orange * Subscribers only Learn more Minimize to nav Russian state hackers are using a maximum-severity vulnerability in Microsoft Outlook’s Exchange Server to backdoor unpatched machines and steal credentials and other confidential information from them, security researchers said Thursday. The attacks are coming from TA488, a tracking name for a group working on behalf of the Kremlin, Proofpoint researchers said Thursday . Proofpoint and the National Security Agency jointly warned last week that the group, also tracked as Laundry Bear and Void Blizzard, had been carrying out similar attacks by exploiting a zero-day vulnerability in an email service from Zimbra. The revelation that TA488 is also exploiting the Exchange Server vulnerability to install advanced malware when a user does nothing other than open an email sent to an Outlook Web Access (OWA) account has elevated the group’s profile and assessments of its abilities. Doubling down “TA488 is doubling down on the use of ‘half-click’ exploits—where opening the email is enough to trigger compromise—with significantly improved loading mechanisms, techniques, and malware, signaling an improvement in the group’s tradecraft and capability,” Proofpoint researchers wrote. “This novel infection chain ends with a previously unknown JavaScript browser-based implant we call OWAReaper, purpose-built for persistent access inside OWA.” The vulnerability, tracked as CVE-2026-42897, is a cross-site-scripting vulnerability, usually abbreviated as XSS, that Microsoft provided mitigation advice for in May and patched in July. Microsoft gave it a maximum severity rating. The vulnerability, which stems from a failure to properly filter HTML embedded in an email, allows malicious JavaScript execution. Proofpoint said that TA488 may have exploited it as a zero-day. The malicious JavaScript installs a novel, custom-built browser extension that gives attackers persistent access to victims’ OWA accounts. Proofpoint said it was the most sophisticated backdoor the company has ever seen delivered through a half-click exploit. The company has named it OWAReaper. Company researchers explained: OWAReaper is executed entirely in the Outlook Web Access (OWA) reading pane. Upon execution, it uses Outlook APIs to rewrite the email on the Exchange server and remove the exploit content. Simultaneously, it disables OWA pop-ups and right-click ability while it runs. OWAReaper then creates a session key, unique to each target, and begins gathering the target’s email address, username and Outlook settings. It then creates two invisible input elements in the DOM and waits for the browser’s autofill to enter the username and password to gather the user’s OWA saved credentials. OWAReaper then writes an encrypted version of itself, and a decryption wrapper, into the browser’s localStorage, under settings fields in the PageDataPayload.OwaUserDefaultSettings key. This is a legitimate key used by OWA in its page rendering, where OWA evaluates OwaFrontendSyncState itself as part of its own sync restore flow. Every time the user opens an OWA tab in the browser, the normal OWA sync process automatically executes OWAReaper. In many cases, the backdoor can go on to steal OAuth tokens and, from there, gain full access to the mailbox of any authenticated user on the same network. “This persistent access lives on the server side and requires deliberate removal from the Exchange server; credential rotation and even full re-imaging of the targeted user’s device will not evict the actor,” Proofpoint said. It’s not clear if machines compromised by OWAReaper are disinfected once Microsoft’s July patch or a separate Exchange Emergency Mitigation service is installed. Proofpoint is advising affected users to revoke and audit their Exchange Web Services tokens for unauthorized add-ins and to (1) remove folder permissions to default users, (2) clear
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Max-severity Exchange server flaw under active exploitation by Kremlin hackers
  - Published: 2026-07-30T19:01:12+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/max-severity-exchange-server-flaw-under-active-exploitation-kremlin-hackers

### Cluster 3ed06f107d — score 8

- Title: Chaos in Teams vishing
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-07-28T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/chaos-in-teams-vishing
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion, web_shell_backdoor
- actor_attribution: Black Basta
- affected_industries: critical_infrastructure, legal_professional, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, web_shell_backdoor
- actor_attribution: Black Basta
- affected_industries: critical_infrastructure, manufacturing_industrial, legal_professional
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Attackers used Microsoft Teams vishing, custom malware, and remote access tools to facilitate ransomware deployment Categories: Threat Research Tags: Microsoft Teams, vishing, Ransomware, Chaos
```

#### Full body

```
Chaos in Teams vishing Attackers used Microsoft Teams vishing, custom malware, and remote access tools to facilitate ransomware deployment Written by Morgan Demboski Threat Research Microsoft Teams vishing Ransomware Chaos Share This Link Copied Sophos analysts investigated a Microsoft Teams voice phishing (vishing) campaign tracked as STAC4749 that used a consistent set of IT-themed cloud domains and personas to gain remote access to victims’ systems. Between February and June 2026, Sophos analysts observed the threat actors targeting dozens of North American organizations. Following initial access, STAC4749 operators deployed a modular post‑exploitation toolset, including a custom loader and backdoor to maintain persistent, controlled access and support follow‑on activity. In several incidents, attackers later leveraged this access to deploy Chaos ransomware. Throughout the campaign, Sophos analysts observed the threat actors continually refining their deployment and evasion techniques, indicating a financially motivated operation that prioritized speed and reliability to pave the way for exfiltration and ransomware deployment. Microsoft Teams vishing trends Microsoft Teams vishing has become a widely used technique among threat actors. Microsoft first publicly documented abuse of Teams for IT‑themed vishing in mid‑2024, describing campaigns that impersonated helpdesk or support personnel to socially engineer users into granting remote access. In late 2024, Counter Threat Unit™ (CTU) researchers identified similar activity by the GOLD REBELLION threat group, which is associated with Black Basta ransomware. Sophos published additional research on this tactic in January 2025, including campaigns tracked as STAC5777 and STAC5143 that combined email bombing with Teams vishing to facilitate ransomware deployment. In January 2026, Sophos analysts observed a sharp increase in Managed Detection & Response (MDR) cases involving Teams vishing across multiple threat groups and campaigns, with additional jumps in March and May (see Figure 1). While improved detections may partially explain these increases, the trend more strongly suggests that Teams vishing has become an increasingly common initial access vector. Figure 1: Number of Sophos MDR cases each month from January 2025 through May 2026 involving confirmed malicious activity for detections related to M365 scams STAC4749 victimology Analysis of STAC4749 targeting suggests a strong focus on North America. As shown in Figure 2, nearly 95% of observed cases between February and June 2026 targeted organizations based in Canada (50%) and the U.S. (44%) Figure 2: Pie chart showing distribution of STAC4749 targeting by country between February and June 2026 Industry-specific targeting was distributed across many sectors (see Figure 3). Services organizations were impacted in 20% of the incidents, followed by manufacturing (17%), energy (12%), and construction and engineering (12%) organizations. Notably, all the legal organizations targeted in the campaign specialize in intellectual property (IP) law or services. Figure 3: Pie chart showing distribution of STAC4749 targeting by sector between February and June 2026 Initial access STAC4749 operators initiated contact through Teams chats and calls, impersonating helpdesk or IT support staff. Sophos analysts observed scam calls ranging from 90 seconds to more than 20 minutes, with most lasting between two to two‑and‑a‑half minutes. Unlike many earlier Teams abuse campaigns in which attackers spoofed onmicrosoft[.]com tenants, STAC4749 operators created IT-themed cloud domains under the “.top” top-level domain (TLD) and leveraged plausible employee usernames to make the accounts appear legitimate (see Table 1). Username Associated Domains AnthonyBrooks sequrityupdate[.]top, scan-security[.]top, system-online[.]top, system-connect[.]top, corp-connect[.]top, info-secure[.]top, supportsoft[.]top, update-syscontrol[.]top DylanHarper sequpdate[.
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Chaos in Teams vishing
  - Published: 2026-07-28T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/chaos-in-teams-vishing
  - Summary: Attackers used Microsoft Teams vishing, custom malware, and remote access tools to facilitate ransomware deployment Categories: Threat Research Tags: Microsoft Teams, vishing, Ransomware, Chaos

### Cluster 30fd684148 — score 8

- Title: Elastic goes all-in on Hacker Summer Camp at Black Hat and DEF CON in Las Vegas
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-31T23:59:59+00:00
- Link: https://www.elastic.co/security-labs/elastic-security-black-hat-defcon-2026
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
Attack Discovery turns raw alerts into validated threats and Elastic Defend closes vulnerable driver gaps as fast as they're disclosed. Watch it all run against real attacks at the booth.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Elastic goes all-in on Hacker Summer Camp at Black Hat and DEF CON in Las Vegas
  - Published: 2026-07-31T23:59:59+00:00
  - Link: https://www.elastic.co/security-labs/elastic-security-black-hat-defcon-2026
  - Summary: Attack Discovery turns raw alerts into validated threats and Elastic Defend closes vulnerable driver gaps as fast as they're disclosed. Watch it all run against real attacks at the booth.

### Cluster a90be9d647 — score 8

- Title: Alert Zero: AI-driven alert triage and attack investigation for the agentic SOC
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-31T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/agentic-soc-alert-triage-alertzero
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
Elastic Security 9.5 gives SOC teams AI that handles first-pass alert triage and investigation, so analysts can get back to threat hunting and detection engineering instead of working through queue noise.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Alert Zero: AI-driven alert triage and attack investigation for the agentic SOC
  - Published: 2026-07-31T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/agentic-soc-alert-triage-alertzero
  - Summary: Elastic Security 9.5 gives SOC teams AI that handles first-pass alert triage and investigation, so analysts can get back to threat hunting and detection engineering instead of working through queue noise.

### Cluster 1d3c72ca3a — score 8

- Title: Stop rewriting detection rules by hand: automatic Sentinel-to-Elastic migration is here
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-29T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/sentinel-detection-rules-migration
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
Elastic's first automatic migration from a modern SIEM. Translate your Sentinel detection rules into Elastic Security without rebuilding them.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Stop rewriting detection rules by hand: automatic Sentinel-to-Elastic migration is here
  - Published: 2026-07-29T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/sentinel-detection-rules-migration
  - Summary: Elastic's first automatic migration from a modern SIEM. Translate your Sentinel detection rules into Elastic Security without rebuilding them.

### Cluster e317d9f287 — score 8

- Title: Russian hackers hijack hotel Wi-Fi networks to spy on travelers, Microsoft says
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-08-03T12:00:00+00:00
- Link: https://therecord.media/russian-wifi-hackers-hotels
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Russian state-sponsored hackers have been compromising hotel Wi-Fi networks around the world to steal travelers' login credentials and infect devices with espionage malware, Microsoft said.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Russian hackers hijack hotel Wi-Fi networks to spy on travelers, Microsoft says
  - Published: 2026-08-03T12:00:00+00:00
  - Link: https://therecord.media/russian-wifi-hackers-hotels
  - Summary: Russian state-sponsored hackers have been compromising hotel Wi-Fi networks around the world to steal travelers' login credentials and infect devices with espionage malware, Microsoft said.

### Cluster 77794ad638 — score 8

- Title: Amgen says cloud data breach exposed patient health, proprietary info
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-31T22:16:42+00:00
- Link: https://www.bleepingcomputer.com/news/security/amgen-says-cloud-data-breach-exposed-patient-health-proprietary-info/
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
Pharmaceutical company Amgen says it suffered a data breach after threat actors stole corporate data and patient information stored in multiple cloud systems operated by third-party service providers. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Amgen says cloud data breach exposed patient health, proprietary info
  - Published: 2026-07-31T22:16:42+00:00
  - Link: https://www.bleepingcomputer.com/news/security/amgen-says-cloud-data-breach-exposed-patient-health-proprietary-info/
  - Summary: Pharmaceutical company Amgen says it suffered a data breach after threat actors stole corporate data and patient information stored in multiple cloud systems operated by third-party service providers. [...]

### Cluster 5158be75f5 — score 8

- Title: South Korea fines telco giant KT $39 million for customer data breach
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-30T22:28:30+00:00
- Link: https://www.bleepingcomputer.com/news/security/south-korea-fines-telco-giant-kt-39-million-for-customer-data-breach/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
South Korea's Personal Information Protection Commission (PIPC) has fined telecommunications giant KT Corporation KRW 53.979 billion ($39 million) over data protection violations. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: South Korea fines telco giant KT $39 million for customer data breach
  - Published: 2026-07-30T22:28:30+00:00
  - Link: https://www.bleepingcomputer.com/news/security/south-korea-fines-telco-giant-kt-39-million-for-customer-data-breach/
  - Summary: South Korea's Personal Information Protection Commission (PIPC) has fined telecommunications giant KT Corporation KRW 53.979 billion ($39 million) over data protection violations. [...]

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

### Cluster 73e9449bb7 — score 8

- Title: Report As You Go: Maintaining Good Documentation for SOC Analysts
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-07-29T14:00:00+00:00
- Link: https://www.blackhillsinfosec.com/report-as-you-go-soc/
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
by Dan “Haircutfish” Rearden | haircutfish.com | Guest Author Working in the SOC can be a grind. Whether triaging alerts, escalating to clients, or just trying to understand why users […] The post Report As You Go: Maintaining Good Documentation for SOC Analysts appeared first on Black Hills Information Security, Inc. .
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: Report As You Go: Maintaining Good Documentation for SOC Analysts
  - Published: 2026-07-29T14:00:00+00:00
  - Link: https://www.blackhillsinfosec.com/report-as-you-go-soc/
  - Summary: by Dan “Haircutfish” Rearden | haircutfish.com | Guest Author Working in the SOC can be a grind. Whether triaging alerts, escalating to clients, or just trying to understand why users […] The post Report As You Go: Maintaining Good Documentation for SOC Analysts appeared first on Black Hills Information Security, Inc. .

### Cluster fcc415978e — score 8

- Title: Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-08-03T08:05:30+00:00
- Link: https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-17583

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-17583
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-17583
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Thermo Fisher Scientific has patched a flaw in select Applied Biosystems human identification software that could allow data files to be altered before analysis software loads them. The vendor's July 31 security bulletin says nearly undetectable changes to .fsa and .hid outputs could occur if laboratory controls are circumvented. Thermo Fisher tracks the issue as CVE-2026-17583 and rates it
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable
  - Published: 2026-08-03T08:05:30+00:00
  - Link: https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html
  - Summary: Thermo Fisher Scientific has patched a flaw in select Applied Biosystems human identification software that could allow data files to be altered before analysis software loads them. The vendor's July 31 security bulletin says nearly undetectable changes to .fsa and .hid outputs could occur if laboratory controls are circumvented. Thermo Fisher tracks the issue as CVE-2026-17583 and rates it

### Cluster 9a554b7f81 — score 8

- Title: HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-31T16:39:31+00:00
- Link: https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, web_shell_backdoor
- affected_industries: legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, web_shell_backdoor
- affected_industries: legal_professional
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Cybersecurity researchers have shed light on a previously undocumented Go-based loader framework called HollowFrame and a Rust-based malware family tracked as Matryoshka. According to Blackpoint Cyber, the intrusion sequence begins with a spear-phishing message containing a link to an encrypted archive, which holds a Windows Shortcut (LNK). Executing the file triggers a multi-stage chain that
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: HollowFrame Loader Deploys Matryoshka Backdoor in Spear-Phishing Attack on Law Firm
  - Published: 2026-07-31T16:39:31+00:00
  - Link: https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
  - Summary: Cybersecurity researchers have shed light on a previously undocumented Go-based loader framework called HollowFrame and a Rust-based malware family tracked as Matryoshka. According to Blackpoint Cyber, the intrusion sequence begins with a spear-phishing message containing a link to an encrypted archive, which holds a Windows Shortcut (LNK). Executing the file triggers a multi-stage chain that

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

### Cluster 4bf27bba6f — score 8

- Title: Chinese Hacker Uses DeepSeek AI to Orchestrate Vulnerability Exploits
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-31T15:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/chinese-hacker-deepseek-ai/
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
A Chinese-speaking threat actor has been using DeepSeek’s AI models to orchestrate cyber-attacks targeting Asian organizations
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Chinese Hacker Uses DeepSeek AI to Orchestrate Vulnerability Exploits
  - Published: 2026-07-31T15:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/chinese-hacker-deepseek-ai/
  - Summary: A Chinese-speaking threat actor has been using DeepSeek’s AI models to orchestrate cyber-attacks targeting Asian organizations

### Cluster 625e7caa10 — score 8

- Title: The Average Cost of a Data Breach Rises to $5 Million
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-29T11:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/cost-of-a-data-breach-5m-ibm/
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
IBM Cost of a Data Breach Report warns that the global average cost of a data breach has reached a record high of $4.99m – and AI-backed attacks have played a role
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: The Average Cost of a Data Breach Rises to $5 Million
  - Published: 2026-07-29T11:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/cost-of-a-data-breach-5m-ibm/
  - Summary: IBM Cost of a Data Breach Report warns that the global average cost of a data breach has reached a record high of $4.99m – and AI-backed attacks have played a role

### Cluster 62eab4135a — score 8

- Title: Coca-Cola Reveals Subsidiary Fairlife Suffered Data Breach
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-07-28T11:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/coca-cola-subsidiary-fairlife-data/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Coca Cola claims data was stolen from its Fairlife business after a recent ransomware attack
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Coca-Cola Reveals Subsidiary Fairlife Suffered Data Breach
  - Published: 2026-07-28T11:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/coca-cola-subsidiary-fairlife-data/
  - Summary: Coca Cola claims data was stolen from its Fairlife business after a recent ransomware attack

### Cluster fa1ef247b7 — score 8

- Title: New vBulletin Vulnerability!
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-07-27T14:00:29+00:00
- Link: https://www.reddit.com/r/netsec/comments/1v8192k/new_vbulletin_vulnerability/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-61511

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-61511
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-61511
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
CVE-2026-61511 - a critical vulnerability in vBulletin that allows an unauthenticated attacker to execute arbitrary code on a remote server. submitted by /u/SSDisclosure [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: New vBulletin Vulnerability!
  - Published: 2026-07-27T14:00:29+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1v8192k/new_vbulletin_vulnerability/
  - Summary: CVE-2026-61511 - a critical vulnerability in vBulletin that allows an unauthenticated attacker to execute arbitrary code on a remote server. submitted by /u/SSDisclosure [link] [comments]
