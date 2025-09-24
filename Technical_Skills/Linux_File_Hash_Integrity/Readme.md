# Activity Summary

Module 2 lab 2 of the course **Assets, Threats, and Vulnerabilities** of the Google Cybersecurity Certificate

![alt text](ActivityResult.png)

I generated SHA-256 hash values for two nominally similar files, redirected the hashes into separate files, and performed a byte-wise comparison to prove that subtle differences in file content produce completely different digests. This exercise demonstrates manual integrity verification using core Linux utilities.

## Objectives accomplished

- Listed and inspected two text files containing test (EICAR-like) content.
- Produced SHA-256 digests with `sha256sum` for each file.
- Persisted hashes into separate output files for later reference.
- Compared hash files using `cmp` to identify divergence at the first differing byte.
- Interpreted why visually similar file contents can yield distinct cryptographic hashes.

## Folder Structure and Status

- Readme.md: Activity narrative, objectives, structure.
- LabSolution.md: Task-by-task commands with actual shell outputs and validation.


