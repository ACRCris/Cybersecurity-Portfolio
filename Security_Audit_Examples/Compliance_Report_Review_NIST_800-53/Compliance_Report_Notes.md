# Compliance report notes

| Security control | Severity | Findings | Recommendations |
| :---- | :---- | :---- | :---- |
| AC-6 Least privilege | Medium | Instances with the default service account which has full access to all cloud APIs were found - contrary to the principle of least privilege. One affected account: cymbal-apps@appspot.gserviceaccount.com | Review of user privileges, restrict privileged accounts on the system to the company needs and prevent the execution of high-privileged code from less privileged accounts |
| CA-3 information exchange | High | VMs with public IP addresses were found,contrary to the requirement for information exchange based on agreed-upon protocols. Two affected virtual machines: instance-1, instance-2 | Prohibit the use of public IP addresses in the internal system of the cloud environment and only allow the network communication traffic necessary for business operations. |
| SC-7 Boundary protection | High |Two VMs instances 1 and 2 with public IP addresses were found which violate the boundary protection requirements. | Public connection should be accesible from components separated from internal components and only through interfaces consisting of boundary protection devices to isolate the internal components |
| IA-2 IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS) | High | Five org accounts were found without MFA enabled, this configuration violates the policy for identification and authentication | Implement MFA for access to privileged and non privileged for all users organization users and uniquely identify organizational users and associate that unique id with the process acting on behalf of those users. |

