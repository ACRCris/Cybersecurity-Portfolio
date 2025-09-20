# Security incident report

| Section 1: Identify the network protocol involved in the incident 
| :---- 
|  The main protocol involved in the incident is the HTTP protocol which is used for the attacker to force to the user for download a malicious file. After that |


| Section 2: Document the incident |
| :---- |
|  The incident was reported by the user of the website yummyrecipesforme.com, who received a message from the website asking them to download a file to update their browser. After downloading the file the users was redirected to a fake website greatrecipesforme.com, where the recipes are available for free, and then the user noticed that their computer was behaving more slowly than usual.  
Also the owner of the website yummyrecipesforme.com try to access to the admin panel of the website but he was unable to do it, and he contacted the hosting provider for assistance.
A sandbox was used to analyze the incident occurred in the application layer in the model TCP/IP of the company's network.  In this secure isolated environment through the use of the tcpdump command tool, it was possible to capture the DNS and HTTP traffic logs, which revealed an anomalous change in the HTTP and DNS traffic after downloading the file, the traffic was routed to a different IP address related to the fake website greatrecipesforme.com. together with a change in the por used to stablish the connection with the website. Furthermore, an high level analyst found in the website's code that a JavaScript code was added to the website that forced the user to download a malicious file, this script redirected the user to the fake website greatrecipesforme.com.
By another hand the IT team was able to determined that the web server was compromised by an brute force attack, which allowed the attacker to gain access to the website's code and modify it to include the malicious JavaScript code. It was possible to determine the password because the admin never changed the default password and no hardening measures, like MFA or 2FA, were implemented.
|

| Section 3: Recommend one remediation for brute force attacks |
| :---- |
| To avoid simple brute force attacks, the main and more urgent recommendation to avoid brute force attacks is to implement a password policy which includes guidelines for creating strong passwords, such as using a combination of uppercase and lowercase letters, numbers, and special characters. This is also useful to avoid dictionary attacks by fixing a limit on the number of failed login attempts. 
To avoid dictionary attacks, it is also recommended to implement MFA or 2FA, which adds an extra layer of security by requiring a second form of authentication.
|

