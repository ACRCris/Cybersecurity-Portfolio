## Access controls worksheet

---

|  | Note(s) | Issue(s) | Recommendation(s) |
| :---- | :---- | :---- | :---- |
| **Authorization /authentication** | 1. Although the user is identified as legal/admin, cross-checking the Event Log with the employee directory you can note that source IP address 152.207.255.255 does not coincide with any of the IP address of the employees' main device <br>  2. This event was occurred in 10th May 2023 at 8:29:57 am. <br> 3. The device use in this incident was a computer Up2-NoGud|  1. The level of access of this user is Admin although this user is not in the employee directory. <br> 2. This account should not be active because again the user is not in the employee directory| 1. An important technical control to be implemented is multi factor authentication (MFA).<br> 2. An operational control to address the risk is the segregation of function and the application of the least privilege. <br> 3. For the last it is very important stablish policies about the password creation and apply the NIST SP 800-63B.|

