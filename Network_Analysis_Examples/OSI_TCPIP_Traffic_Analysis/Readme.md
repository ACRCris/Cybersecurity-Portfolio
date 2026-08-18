# Activity Summary

Portfolio Activity: **OSI / TCP-IP packet analysis with Wireshark**, Lab 1 from the "Network Fundamentals" module of the BeTek / MAKAIA Cybersecurity Bootcamp.

Packet-level traffic analysis reinforcing the OSI and TCP/IP models, using Wireshark to capture and inspect ICMP traffic and to diagnose a connectivity problem.

## Objectives accomplished

- Obtained host and virtual-machine network configuration (`ipconfig /all`, `ifconfig`): IPv4, MAC, gateway, DHCP.
- Captured **ICMP traffic in Wireshark** and filtered by protocol and address.
- Diagnosed a failed ping to the host machine, determining the cause was the host firewall **blocking inbound ICMP**, and resolved it by enabling the rule.
- Inspected captured frames **layer by layer in hexadecimal**, relating each field to the OSI and TCP/IP models.

## Folder Structure and Status

- `OSI_TCPIP_Wireshark_Lab.pdf`: full lab report with captures, filtering, firewall diagnosis, and frame-level analysis.

## Tools

Wireshark, ICMP, `ipconfig`/`ifconfig`, OSI and TCP/IP models.
