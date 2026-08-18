# Cybersecurity Portfolio

This repository gathers activities, reports, and practices developed during my cybersecurity training. It combines exercises from the **Google Cybersecurity Professional Certificate** and hands-on deliverables from the **BeTek / MAKAIA Cybersecurity Analysis Bootcamp** (232 hours), demonstrating competencies across security operations, threat analysis, offensive security, network analysis, security auditing and governance, asset management, and technical skills.

## Primary Structure

- `declaracion_profesional.md`: personal statement describing professional interests and the application of the CIA triad.
- `Professional_Statement/`: supporting materials and working drafts used to refine the professional statement.
- `Security_Operations_Examples/`: SOC work — a functional **SIEM built on the Elastic Stack** (Winlogbeat/Metricbeat, Kibana dashboards) and a **SANS PICERL incident response plan** for a ransomware scenario.
- `Threat_Analysis_Examples/`: **STRIDE threat modeling** of a payment platform, **APT and social-engineering** analysis of real cases (SolarWinds, WannaCry, Twitter 2020), **malware analysis with YARA and SSDEEP**, and phishing analysis.
- `Offensive_Security_Examples/`: **CTF pentesting HackLabs** (OSINT, Nmap, Hydra, Wireshark, NTLM cracking) and a reverse-shell proof of concept — all in controlled labs, framed for defensive understanding.
- `Network_Analysis_Examples/`: network hardening, DNS/ICMP traffic analysis and incident reviews with Wireshark, plus a **Packet Tracer services design** (DHCP/DNS/HTTP) and an **OSI/TCP-IP packet-analysis lab**.
- `Security_Audit_Examples/`: internal audits aligned to the NIST CSF with compliance checklists and stakeholder memorandums, plus a full **ISO/IEC 27001:2022 ISMS (SGSI)** built for a regulated company.
- `System_Operative_Examples/`: investigation of a brute-force compromise and hardening recommendations based on DNS and HTTP logs.
- `Asset_Management_Examples/`: asset inventory with sensitivity classification, and an access-control audit that detected an unregistered administrator account.
- `Technical_Skills/`: hands-on labs reinforcing Linux commands (permissions, file search, input/output) and SQL (filters and joins).

## Featured Deliverables

- `Security_Operations_Examples/SIEM_ELK_Stack/`: end-to-end SIEM build ingesting Windows and Linux telemetry, with dashboards and controlled event generation for detection testing.
- `Security_Operations_Examples/Incident_Response_PICERL/`: six-phase incident response plan (Preparation → Lessons Learned) for a ransomware scenario.
- `Threat_Analysis_Examples/Threat_Modeling_STRIDE/`: STRIDE model of an e-commerce payment platform with 10 prioritized threats and 17 architecture and development controls.
- `Security_Audit_Examples/SGSI_ISO27001_Servientrega/`: ISO 27001:2022 ISMS documentation — context, asset inventory with CIA valuation, 20-scenario risk matrix, policy, and Statement of Applicability.
- `Threat_Analysis_Examples/Malware_Analysis_YARA_SSDEEP/`: real-sample malware detection combining YARA rules and SSDEEP fuzzy hashing in Python.
- `Security_Audit_Examples/Conduct_Security_AuditP1/`: internal audit of Botium Toys with risk assessment and a GDPR / PCI DSS / ISO 27001 compliance checklist.
- `Asset_Management_Examples/Access_Control_Audit/`: access-control audit detecting an unregistered admin account operating from a non-corporate IP.

## How to Use This Repository

1. Review the "Primary Structure" section to locate the topic of interest.
2. Open each folder's `Readme.md` for an activity summary, then the `.pdf` / `.md` deliverables.
3. Check `MaterialApoyo`, `MaterialDeApoyo`, or `Supplementary_Materials` folders for templates, supporting data, or reference screenshots.

## Tools and Frameworks Covered

- **Security operations**: Elastic Stack (Elasticsearch, Kibana, Winlogbeat, Metricbeat), SIEM dashboards, log analysis, SANS PICERL.
- **Threat analysis**: STRIDE threat modeling, MITRE ATT&CK awareness, YARA, SSDEEP, phishing and APT analysis.
- **Offensive security (lab)**: Nmap, THC-Hydra, Wireshark, hash cracking, OSINT — for defensive understanding.
- **Governance, risk & compliance**: NIST CSF, NIST SP 800-53, ISO/IEC 27001:2022 and 27005, GDPR, PCI DSS, SOC 2; audits, Statements of Applicability, risk matrices.
- **Networking**: Cisco Packet Tracer, DHCP/DNS/HTTP, OSI and TCP/IP, ICMP/ARP, tcpdump.
- **Technical**: Linux command line, SQL, Python (detection tooling and automation).

## Note on Collaborative Work

Several bootcamp deliverables were produced in teams (noted in each folder's `Readme.md`). Individual contributions and reviewer roles are stated where applicable. Company scenarios such as Botium Toys, Cymbal Bank, and the Servientrega ISMS exercise are case studies, not real client engagements.
