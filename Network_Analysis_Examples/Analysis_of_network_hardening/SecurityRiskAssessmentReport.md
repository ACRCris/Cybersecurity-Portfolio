# Security risk assessment report 

| Part 1: Select up to three hardening tools and methods to implement |
| :---- |
|Three hardening tools to be implemented with highly priority are: |
|1. Multi Factoring Authentication (MFA): A security measure which requires a user to verify identify in two o more ways to access a system or network. MFA options include for example: a password, pin number, badge, one time password.(OPT), fingerprint.|
|2. Password Policies: The National Institute of Standards and Technology's (NIST) latest recommendations for password policies focuses on using methods to salt and hash passwords, rather than requiring overly complex password or enforcing frequent changes to password.|
|3. Port filtering: A firewall function that blocks or allows certain port numbers to limit unwanted communication| 

| Part 2: Explain your recommendations ||
| :---- | :---- |
|There are two main possible attacks that let attackers filtering data: brute force attack and route attack, this due to the lack of  a password policy, firewall configuration and multi factor authentication. The following table shows the hardening tools and methods to implement to mitigate these risks. |
|Hardening tool|Periodicity |
| 1. MFA can help protect against brute force attacks and similar security events. MFA can be implemented at any time, and is mostly a technique that is set up once then maintained. |MFA should be enforced regularly.|
|2. Policies password are used to prevent attackers from easily guessing user password, either manually or by using a script attempt thousand of stolen passwords.|password policy will need to be enforced regularly|
|3. Port filtering is used to control network traffic and can prevent potential attacks from entering a private network. |Firewall rules should be updated whenever a security event occurs,|

