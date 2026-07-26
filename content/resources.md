---
title: "OSINT & Security Resources"
date: 2026-06-15T20:55:37+01:00
draft: false
layout: "simple"
showDate: false
showTableOfContents: true
maxWidth: "full"
---

A curated collection of frequently used tools.

---

> Table of Contents

- [Threat Intelligence](#threat-intelligence)
- [Domain \& DNS Intelligence](#domain--dns-intelligence)
- [IP \& Infrastructure Intelligence](#ip--infrastructure-intelligence)
- [Malware Analysis](#malware-analysis)
- [Malware Samples \& IOC Feeds](#malware-samples--ioc-feeds)
- [Threat Maps](#threat-maps)
- [Vulnerability Research](#vulnerability-research)
- [Email Analysis](#email-analysis)
- [Utilities \& Investigative Tools](#utilities--investigative-tools)
- [Red Team Resources](#red-team-resources)

---

# Threat Intelligence

| Tool                                                                             | Description                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [GreyNoise](https://viz.greynoise.io/)                                           | Analyze internet-wide scanning activity and identify known scanners. |
| [ThreatFeeds.io](https://threatfeeds.io/)                                        | Free threat intelligence feeds and indicators.                       |
| [AlienVault OTX](https://otx.alienvault.com/)                                    | Community-driven threat intelligence exchange.                       |
| [ThreatFox](https://threatfox.abuse.ch/)                                         | IOC repository focused on malware indicators.                        |
| [Cisco Talos Reputation Center](https://talosintelligence.com/reputation_center) | Domain, IP, and reputation intelligence.                             |
| [Sophos Intelix](https://intelix.sophos.com/)                                    | File, URL, and IOC reputation analysis.                              |
| [FireHOL IP Lists](https://iplists.firehol.org/)                                 | Aggregated IP blocklists and threat feeds.                           |

# Domain & DNS Intelligence

| Tool                                                        | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| [DNSTwist](https://dnstwist.it/)                            | Detect phishing, typo-squatting, and impersonation domains. |
| [MXToolbox](https://mxtoolbox.com/supertool.aspx)           | DNS, MX, blacklist, and mail infrastructure diagnostics.    |
| [DNSDumpster](https://dnsdumpster.com/)                     | DNS reconnaissance and domain mapping.                      |
| [SSL Labs SSL Test](https://ssllabs.com/ssltest/index.html) | Analyze SSL/TLS configurations and security posture.        |

# IP & Infrastructure Intelligence

| Tool                                                                        | Description                                               |
| --------------------------------------------------------------------------- | --------------------------------------------------------- |
| [Shodan](https://www.shodan.io/)                                            | Search internet-connected devices and services.           |
| [Censys](https://search.censys.io/)                                         | Internet asset discovery and attack surface intelligence. |
| [Netlas](https://app.netlas.io/host/)                                       | Infrastructure search engine and reconnaissance platform. |
| [LeakIX](https://leakix.net/graph)                                          | Exposure and infrastructure visualization.                |
| [URLScan](https://urlscan.io/)                                              | Website scanning and analysis.                            |
| [URLVoid](https://www.urlvoid.com/)                                         | Website reputation and blacklist checks.                  |
| [AbuseIPDB](https://www.abuseipdb.com/)                                     | IP reputation and abuse reporting.                        |
| [Sophos IP Lookup](https://www.sophos.com/en-us/support/ip-address-lookup/) | Sophos IP reputation and classification lookup.           |
| [GrayHatWarfare](https://buckets.grayhatwarfare.com/)                       | Public cloud bucket discovery and investigation.          |


# Malware Analysis

| Tool                                          | Description                                          |
| --------------------------------------------- | ---------------------------------------------------- |
| [ANY.RUN](https://app.any.run/)               | Interactive malware sandbox and behavioral analysis. |
| [VirusTotal](https://www.virustotal.com/)     | File, URL, domain, and IP reputation scanning.       |
| [IOC Parser](https://iocparser.com/)          | Extract indicators from threat reports and text.     |
| [Sophos Intelix](https://intelix.sophos.com/) | File and malware reputation analysis.                |


# Malware Samples & IOC Feeds

| Tool                                             | Description                                                 |
| ------------------------------------------------ | ----------------------------------------------------------- |
| [MalwareBazaar](https://bazaar.abuse.ch/browse/) | Malware sample repository.                                  |
| [URLHaus](https://urlhaus.abuse.ch/browse/)      | Malicious URL repository and malware distribution tracking. |
| [ThreatFox](https://threatfox.abuse.ch/)         | IOC collection and malware indicators.                      |

# Threat Maps

| Tool                                                                                  | Description                                           |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [Bitdefender Threat Map](https://threatmap.bitdefender.com/)                          | Global cyberattack visualization.                     |
| [Check Point Live Cyber Threat Map](https://threatmap.checkpoint.com/)                | Real-time attack monitoring.                          |
| [OpenText Threat Map](https://threatmap.zix.com/)                                     | Worldwide threat activity dashboard.                  |
| [SonicWall Threat Map](https://securitycenter.sonicwall.com/m/page/worldwide-attacks) | Live attack telemetry.                                |
| [Shadowserver Dashboard](https://dashboard.shadowserver.org/)                         | Internet exposure and threat intelligence dashboards. |
| [Ransomware Map](https://statescoop.com/ransomware-map/)                              | Tracking ransomware activity geographically.          |

# Vulnerability Research

| Tool                                            | Description                                       |
| ----------------------------------------------- | ------------------------------------------------- |
| [Vulners](https://vulners.com/search)           | CVE, exploit, and vulnerability intelligence.     |
| [Ransomware.Live](https://www.ransomware.live/) | Current ransomware incidents and victim tracking. |


# Email Analysis

| Tool                                                                       | Description                          |
| -------------------------------------------------------------------------- | ------------------------------------ |
| [Microsoft Message Header Analyzer](https://mha.azurewebsites.net/)        | Decode and analyze email headers.    |
| [MXToolbox Email Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx) | Email routing and header inspection. |
| [EmailRep](https://emailrep.io/)                                           | Email reputation intelligence.       |

# Utilities & Investigative Tools

| Tool                                                                       | Description                                               |
| -------------------------------------------------------------------------- | --------------------------------------------------------- |
| [CyberChef](https://gchq.github.io/CyberChef/)                             | Encoding, decoding, encryption, and data transformations. |
| [Dencode](https://dencode.com/)                                            | Multi-purpose encoding and decoding toolkit.              |
| [Intelligence X](https://intelx.io/)                                       | Leak, breach, and OSINT search engine.                    |
| [Grep.app](https://grep.app/)                                              | Search public source code repositories.                   |
| [DorkSearch](https://dorksearch.com/)                                      | Search engine dork discovery.                             |
| [BadFiles](https://badfiles.ch/)                                           | File extension and malware-related file reference.        |
| [User-Agent Parser](https://explore.whatismybrowser.com/useragents/parse/) | Decode browser user-agent strings.                        |
| [Should I Block It?](https://www.shouldiblockit.com/)                      | Process and application reputation lookup.                |
| [IPLogger](https://iplogger.org/)                                          | URL shortening and visitor tracking analysis.             |

# Red Team Resources

| Tool                                            | Description                                          |
| ----------------------------------------------- | ---------------------------------------------------- |
| [Exploit Database](https://www.exploit-db.com/) | Public exploit archive and vulnerability references. |
