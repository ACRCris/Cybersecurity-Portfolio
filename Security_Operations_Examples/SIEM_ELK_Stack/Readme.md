# Activity Summary

Portfolio Activity: **SIEM implementation with the Elastic Stack (ELK)** from the "SOC Operations and Monitoring" module of the BeTek / MAKAIA Cybersecurity Bootcamp. *Team activity.*

I built a functional Security Information and Event Management (SIEM) system end to end in a virtualized lab, ingesting security telemetry from Windows and Linux hosts, visualizing it in Kibana, and validating detection by generating controlled events.

## Objectives accomplished

- Designed a three-VM lab environment (Kali, Windows, Ubuntu) with working connectivity, including diagnosing and resolving an ICMP block in Windows Defender Firewall.
- Installed and configured **Elasticsearch** and **Kibana** on Kali Linux.
- Ingested **Windows event logs with Winlogbeat**, classifying system, security, application, PowerShell, logon, service, and local administrative-change events.
- Collected **Linux host metrics with Metricbeat** from Ubuntu.
- Built **dashboards and visualizations** in Kibana and compared Windows logs against Linux metrics.
- Performed **controlled event generation** (CPU, memory, network, service start/stop, process review) to confirm detection, closing with a security-analysis phase over the collected data.

## Folder Structure and Status

- `SIEM_Implementation_Report.pdf`: complete report documenting the eight phases, from environment design to security analysis, with configuration steps and screenshots. (Compressed for repository size; full-resolution version available on request.)

## Tools

Elasticsearch, Kibana, Winlogbeat, Metricbeat, Kali Linux, Windows, Ubuntu, VirtualBox.
