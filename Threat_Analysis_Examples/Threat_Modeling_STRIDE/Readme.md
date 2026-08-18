# Activity Summary

Portfolio Activity: **STRIDE threat modeling of an e-commerce payment platform**, from the "Security Architecture Strategies" module of the BeTek / MAKAIA Cybersecurity Bootcamp.

A complete threat model of an e-commerce architecture with a transactional payment portal, applying **STRIDE** (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) across six data flows: authentication, catalog, orders, payments, administrative operation, and backup/keys.

## Objectives accomplished

- Identified and classified threats by criticality — **six critical, four high** — across the six flows. Critical threats included payment-provider spoofing, in-transit amount tampering, SQL injection against the databases, private-key extraction from the vault, ransomware on backups, and PAN/CVV disclosure in logs.
- Proposed **eleven architecture controls**: end-to-end TLS, mutual TLS with the banking gateway, trust-zone network segmentation, API Gateway as the single entry point, rate limiting and DDoS mitigation, callback IP whitelisting, database isolation in a private VPC, high-availability secrets management, WORM storage for backups, AES-256 encryption at rest, and SSO + MFA + RBAC for admin access.
- Proposed **six development controls**: parameterized statements/ORM, JSON schema validation, backend amount recalculation, webhook signature validation, application-layer payload encryption, and tokenization (never storing PAN/CVV).
- Documented **STRIDE exclusion justifications** flow by flow — arguing which threat categories do not apply and why.

## Folder Structure and Status

- `STRIDE_Threat_Model.pdf`: final threat model with critical/high threats, associated risk, and the architecture and development controls.
- `STRIDE_Exclusion_Justifications.pdf`: per-flow justification of excluded STRIDE categories.

## Frameworks

STRIDE threat modeling; defense in depth; secure architecture and secure development controls.
