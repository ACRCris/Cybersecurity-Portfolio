# Activity Summary 
Module 2, activity 1 from Tools of the Trade: Linux and SQL (Google Cybersecurity Certificate): Google Cloud lab focused on hardening Linux file permissions.

In this activity, I examined and hardened file and directory permissions inside the `/home/researcher2/projects` directory. I identified insecure write access for other users, removed unnecessary group privileges, corrected a hidden file's permissions, and restricted traversal of a sensitive subdirectory. I practiced interpreting the 10-character permission string and applying targeted changes with `chmod`, validating each adjustment with `ls -l` and `ls -la`.

## Objectives accomplished

- Verified file and directory data (including hidden entries) as a baseline.
- Described the 10-character permission string structure for a sample file.
- Changed file permissions to remove improper write access for others.
- Changed permissions on a hidden file to enforce least privilege.
- Changed directory permissions to restrict access to the owner only.
- Finalized documentation confirming all corrected permission states.

## Folder Structure and Status

- `FilePermissionsInLinux.md`: Narrative walk-through describing context and step rationale.
- `CurrentFilePermissions.md`: Baseline state of the directory prior to modifications.
- `InstructionsIncludingLinuxCommands.md`: Guidance template for documenting commands or screenshots.

