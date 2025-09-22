# Activity Summary

Module 2, Lab 4 from Tools of the Trade: Linux and SQL (Google Cybersecurity Certificate): Google Cloud lab focused on hardening Linux file permissions.


![alt text](image.png)

In this Google Cloud activity, I audited and corrected file and directory permission settings on regular, hidden, and directory objects. I enforced least privilege by removing world write, stripping unnecessary group access, and tightening traversal rights using `ls -l`, `ls -la`, and targeted `chmod` operations.

## Objectives accomplished

- Audited file and directory metadata with long listings (including hidden files).
- Identified and removed world write on `project_k.txt` (`chmod o-w`).
- Restricted `project_m.txt` to the owner only (`rw-------`).
- Removed unintended write permissions for user and group on hidden `.project_x.txt` (result `r--r-----`).
- Eliminated group traversal on the `drafts` directory by removing execute (`chmod g-x drafts/`).
- Interpreted symbolic permission strings (e.g., `-rw-rw-r--`) to decide corrective actions.
- Applied the principle of least privilege across mixed file types.

## Folder Structure and Status

- `LabSolution.md`: Step-by-step solution with commands, outputs, and validation notes.




