  # Cybersecurity Incident Report

## Section 1: Identify the type of attack that may have caused 

Looking at the Wireshark TCP/HTTP traffic log, there are too many SYN packets from the IP address 203.0.113.0.  This indicates a potential SYN flood attack, which is a type of Denial of Service (DoS) attack. In a SYN flood attack, an attacker sends a large number of SYN requests to a target server, often using spoofed IP addresses. The server, upon receiving these requests, allocates resources to establish connections with the seemingly legitimate clients. However, since the source IP addresses are spoofed, the server never receives the expected ACK responses, leading to resource exhaustion.

---
## Section 2: Explain how the attack is causing the website to malfunction

The SYN flood attack is causing the website to malfunction by overwhelming the server with a high volume of SYN packets. This results in the server being unable to process legitimate requests, as it is busy trying to handle the flood of incoming SYN requests. The server's resources, such as memory and processing power, are consumed by these half-open connections, leading to a situation where it cannot respond to genuine user requests. Consequently, users experience delays or are unable to access the website altogether.

## Section 3: Describe the actions taken by the IT team to prevent further attacks
The IT team took the following actions to mitigate the SYN flood attack:
1. **Encrypted the traffic**: The team implemented encryption protocols to secure the data being transmitted, using a VPN or TLS/SSL to protect against eavesdropping and tampering.

2. **Using a NGFW (Next-Generation Firewall)**: The team deployed a next-generation firewall to filter and monitor network traffic, allowing them to block malicious traffic and prevent further SYN flood attacks.
3. **Blocking the IP address**: The team identified the source IP address.

4. **Subnetting**:
   The team implemented subnetting to segment the network, which helps in isolating the attack and preventing it from affecting the entire network. This also allows for better traffic management and security.

---

