# Cybersecurity Incident Report: Network Traffic Analysis

## Part 1: Provide a summary of the problem found in the DNS and ICMP traffic log.

**The UDP protocol reveals that:** the client was attempting to enter the website "yummyrecipesforme.com", but the DNS server did not respond with the correct IP address. This is due to the DNS server was unable to process the request due to a port issue.    
<!-- instead the ICMP protocol returned an "upd port 53 unreachable length 254" error message.  -->
  

**This is based on the results of the network analysis, which show that the ICMP echo reply returned the error message:** upd port 53 unreachable length 254.

**The port noted in the error message is used for:** the DNS protocol in the application layer, it is used to translate domain names into IP addresses using the UDP protocol.

**The most likely issue is:** due to a possible DoS attack, the internal control message protocol (ICMP) flood, because the DNS server was unable to process the request due the port was unreachable, but the protocol and port used is correct.

---

## Part 2: Explain your analysis of the data and provide at least one cause of the incident.

**Time incident occurred:** 13:24:32.192571 (1:24 p.m with 32.192571 seconds)

**Explain how the IT team became aware of the incident:** The IT team was alerted to the incident because several customers reported that they were unable to access the website "yummyrecipesforme.com" and they seen the error message "destination port unreachable". 

**Explain the actions taken by the IT department to investigate the incident**:

The IT team executed the following steps to identify and resolve the accessibility issue with the website:

1. The IT team thoroughly reviewed the website to ascertain its accessibility.
2. Utilizing the tcpdump command tool, the IT team reloaded the website to conducted packet sniffing tests.
3. Subsequently, the IT team analyzed the captured traffic meticulously to pinpoint the root cause of the accessibility problem.
4. In the tcpdump's results, the IT team identified a DNS request for the domain "yummyrecipesforme.com" that was not answered by the DNS server due to the error "upd port 53 unreachable length 254".
5. In the same results, the IT team observed that the ICMP protocol returned that error message in several packets.


**Note key findings of the IT department's investigation (i.e., details related to the port affected, DNS server, etc.):**

**Note a likely cause of the incident:** The most likely cause of the incident is a DoS attack, specifically an ICMP flood, which caused the DNS server to be unable to process the request due to the port being unreachable. The DNS server was unable to respond to the client's request for the IP address of "yummyrecipesforme.com" because it was overwhelmed by ICMP packets, leading to the error message "upd port 53 unreachable length 254". 
