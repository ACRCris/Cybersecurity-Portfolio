# Answers to the questions
## 1. What are the biggest risks to the organization?

The main risks, based on the [risk assessment](Material_de_Apoyo/Botium%20Toys_%20Risk%20assessment.pdf), stem from inadequate asset management, missing security controls, and potential fines or sanctions for non‑compliance with U.S. and international regulations. Key risks include:

- Financial: Fines and penalties due to regulatory non‑compliance.
- Identity theft: Exposure of customers’ personal data caused by insufficient security controls and poor asset management.
- Impact on confidentiality, integrity, and availability due to inadequate asset management.

## 2. Which controls should be implemented immediately versus later?

<!-- Since the company already has some technical and physical controls (e.g., firewalls, accounting systems, endpoint detection, IDS, SIEM), prioritize the following: -->

Recommended technical controls and priorities:

- Antivirus (very high priority): Protect endpoints against malware and viruses.
- Multi‑factor authentication (very high priority): Prevent unauthorized access to systems and data.
- Encryption (high priority): Protect sensitive data at rest and in transit.
- Backups (very high priority): Ensure data availability and rapid recovery.

Recommended administrative controls and priorities:

- Improve asset classification (high priority): Ensure sensitive data receives appropriate protection.
- Separation of duties (medium priority): Reduce fraud and error by segregating critical tasks.

## 3. Which compliance standards should Botium Toys follow to protect data, avoid fines, and meet obligations?

Alongside applying the five NIST CSF functions, Botium Toys should address the following:

- **General Data Protection Regulation (GDPR)**: Protects EU residents’ data and privacy inside and outside EU territory.
- **Payment Card Industry Data Security Standard (PCI DSS)**: Ensures organizations storing, processing, and transmitting credit‑card data do so securely.
- **ISO/IEC 27001**: International standard for an Information Security Management System (ISMS) covering financial data, intellectual property, personnel data, and third‑party information.

### Explanation

- **GDPR**: Required because the company does business in the EU and collects personal information from EU residents.
- **PCI DSS**: Required because the company stores, accepts, processes, and transmits credit‑card information online.
- **ISO/IEC 27001**: Recommended to establish and maintain an ISMS that governs security controls across the organization, including international operations.
