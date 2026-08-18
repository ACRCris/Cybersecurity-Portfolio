# Activity Summary

Portfolio Activity: **Review a compliance report (control mapping against NIST SP 800-53)**, from the "Strategies for Cloud Security Risk Management" course of the Google Cloud Cybersecurity Certificate.

I reviewed a compliance report for a cloud environment (fictitious **Cymbal Bank**) and mapped findings to specific **NIST SP 800-53** controls, documenting each finding control by control with its severity, affected asset, and a concrete remediation recommendation.

## Objectives accomplished

Documented four controls, each with severity, findings, and recommendations:

- **AC-6 (Least Privilege) — Medium**: instances using the default service account with full access to all cloud APIs (affected account named). Recommended restricting privileged accounts and preventing high-privilege code execution from lower-privileged accounts.
- **CA-3 (Information Exchange) — High**: VMs with public IP addresses (two instances named). Recommended prohibiting public IPs on the internal system and allowing only necessary traffic.
- **SC-7 (Boundary Protection) — High**: the same public-IP VMs violating boundary protection. Recommended isolating internal components behind boundary-protection interfaces.
- **IA-2 (Identification & Authentication) — High**: five organizational accounts without MFA. Recommended enforcing MFA for all users and uniquely identifying each user.

## Folder Structure and Status

- `Compliance_Report_Notes.md`: completed compliance report notes — the four mapped controls with severity, findings (including named affected assets), and remediation recommendations.

## Frameworks

NIST SP 800-53 (AC-6, CA-3, SC-7, IA-2); cloud security control mapping and compliance reporting.
