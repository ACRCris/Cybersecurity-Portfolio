# Activity Summary

Portfolio Activity: **Review and update a risk management policy**, from the "Strategies for Cloud Security Risk Management" course of the Google Cloud Cybersecurity Certificate.

I reviewed an organization's risk management policy (fictitious **Cymbal Bank**) against **NIST SP 800-53** controls and identified **nine compliance gaps**, writing the proposed change and its normative justification for each.

## Objectives accomplished

Documented nine gaps by policy section, each with the recommended change and the specific control it satisfies:

- **Access Control** — AC-11: automatic session lock on inactivity until re-authentication.
- **Access Control** — AC-6(10): prohibit non-privileged users from executing privileged functions.
- **Awareness & Training** — AT-3 a.: role-based training delivered before granting system access.
- **Awareness & Training** — AT-3 b. / AT-2 c.: update training content periodically and after defined events.
- **Configuration Management** — CM-11 / CM-11(2): control which software users may install; restrict to explicitly privileged users.
- **Identification & Authentication** — IA-5(1)(f): allow long passwords and passphrases with spaces and all printable characters.
- **Physical & Environmental Protection** — PE-2: remove individuals from the facility access list when no longer required, and review it periodically.
- **Risk Assessment** — RA-5: define scan frequency and require analysis, remediation within defined times, and sharing of findings.
- **System & Information Integrity** — SI-5: identify external alert sources, disseminate to all affected roles, and implement directives within set time frames.

## Folder Structure and Status

- `Risk_Management_Policy_Notes.md`: completed policy-review notes — the nine gaps with recommended change and reasoning, mapped to their NIST SP 800-53 controls.

## Note

A key insight captured in the work (on RA-5): *scanning without a defined frequency or a remediation obligation identifies risk without reducing it.*

## Frameworks

NIST SP 800-53 (AC-11, AC-6(10), AT-2, AT-3, CM-11, IA-5(1)(f), PE-2, RA-5, SI-5); policy gap analysis and remediation.
