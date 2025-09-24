# Activity: Create and compare hash values (Lab Solution)

### Task 1. Generate hashes for files
List directory contents:
```bash
ls
```
Output:
```plaintext
file1.txt  file2.txt
```
Display both files:
```bash
cat file1.txt
cat file2.txt
```
Outputs:
```plaintext
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
9sxa5Yq20R
```
> [!NOTE] Question
> Do the contents of the two files appear identical when you use the `cat` command?
> - [x] Yes
> - [ ] No

Compute SHA-256 hashes:

```bash
sha256sum file1.txt
sha256sum file2.txt
```
Outputs:
```plaintext
131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267  file1.txt
2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b  file2.txt
```
> [!NOTE] Question
> Do both files produce the same generated hash value?
> - [ ] Yes
> - [x] No

Persist hashes into separate files (append operator used once each):
```bash
sha256sum file1.txt >> file1hash
sha256sum file2.txt >> file2hash
```
Review stored hashes:
```bash
cat file1hash
cat file2hash
```
Outputs:
```plaintext
131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267  file1.txt
2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b  file2.txt
```

### Task 2. Compare hash files
Byte-wise comparison:
```bash
cmp file1hash file2hash
```
Output:
```plaintext
file1hash file2hash differ: char 1, line 1
```
Interpretation: The very first byte differs, confirming the files are not identical at the hash level (expected since `file2.txt` contains an additional line segment `9sxa5Yq20R`).
> [!NOTE] Question
> Based on the hash values, is `file1.txt` different from `file2.txt`?
> - [x] Yes
> - [ ] No

### Validation
- Both original text files displayed; second includes an extra string line.
- Distinct SHA-256 digests generated (no collision, strong differentiation).
- Hashes saved to separate files and compared; `cmp` reports difference at first character.

### Notes
- Even a single character difference drastically changes the hash (avalanche effect).
- Use `>` instead of `>>` if regenerating hashes to avoid accidental multiple entries.
- For automation, a checksum file format (e.g., `sha256sum file1.txt file2.txt > manifest.sha256`) plus `sha256sum -c manifest.sha256` is recommended.
