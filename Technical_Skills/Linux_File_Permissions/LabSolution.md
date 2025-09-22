# Activity: Manage authorization (Lab Solution)

### Task 1. Check file and directory details

List the long format (permissions, ownership, size) of the target directory:
```bash
ls -l projects
```
This command lists:
```plaintext
total 20
drwx--x--- 2 researcher2 research_team 4096 Sep 22 17:52 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Sep 22 17:52 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Sep 22 17:52 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Sep 22 17:52 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Sep 22 17:52 project_t.txt
```
All entries share the same group owner.
> [!NOTE] Question
> What is the name of the group that owns the files in the `projects` directory?
> - [x] `research_team`
> - [ ] `other_users`
> - [ ] `security_team`
> - [ ] `researcher2`

Now include hidden files:
```bash
ls -la projects
```
This command prints (excerpt focusing on the hidden file):
```plaintext
. .project_x.txt project_k.txt project_r.txt
.. drafts project_m.txt project_t.txt
```
> [!NOTE] Question
> Which file is hidden in the `projects` directory?
> - [x] `.project_x.txt`
> - [ ] There are no hidden files
> - [ ] `.project_m.txt`
> - [ ] `.project_r.txt`

### Task 2. Change file permissions

Change into the directory and review file permissions:
```bash
cd projects
ls -l
```
`project_k.txt` shows mode `-rw-rw-rw-`.
> [!NOTE] Question
> Which file grants other users write permissions?
> - [x] `project_k.txt`
> - [ ] `project_m.txt`
> - [ ] `project_t.txt`

Remove write permission for others:
```bash
chmod o-w project_k.txt
ls -l project_k.txt
```
Now it becomes:
```plaintext
-rw-rw-r-- 1 researcher2 research_team 46 ... project_k.txt
```

Check the restricted file:
```bash
ls -l project_m.txt
```
Initial state:
```plaintext
-rw-r----- 1 researcher2 research_team 46 ... project_m.txt
```
The group has read permission.
> [!NOTE] Question
> What are the group permissions on the `project_m.txt` file (before tightening)?
> - [x] Read only
> - [ ] Read and write
> - [ ] Read, write, and execute

Harden it so only the user can read/write:
```bash
chmod g-r project_m.txt
ls -l project_m.txt
```
Final state:
```plaintext
-rw------- 1 researcher2 research_team 46 ... project_m.txt
```

### Task 3. Change file permissions on a hidden file

Inspect the hidden file:
```bash
ls -l .project_x.txt
```
Intermediate original state:
```plaintext
-rw--w---- 1 researcher2 research_team 46 ... .project_x.txt
```
Both user and group had write access (should be read-only).
> [!NOTE] Question
> Which owner type(s) had incorrect write permissions on `.project_x.txt`?
> - [x] The user and the group
> - [ ] Just the user
> - [ ] Just the group

Apply correction:
```bash
chmod gu-w .project_x.txt
ls -l .project_x.txt
```
Result:
```plaintext
-r--r----- 1 researcher2 research_team 46 ... .project_x.txt
```

### Task 4. Change directory permissions

Check directory permissions:
```bash
ls -ld drafts
```
Initial output:
```plaintext
drwx--x--- 2 researcher2 research_team 4096 ... drafts
```
Group has execute (`x`) permission.
> [!NOTE] Question
> Does the group have permissions to access (traverse) the `drafts` directory initially?
> - [x] Yes
> - [ ] No

Remove group execute:
```bash
chmod g-x drafts/
ls -ld drafts
```
New state:
```plaintext
drwx------ 2 researcher2 research_team 4096 ... drafts
```

## Validation

- No file grants write permission to others.
- `project_m.txt` restricted to the user only (`rw-------`).
- Hidden file `.project_x.txt` is read-only for user & group (`r--r-----`).
- `drafts` directory traversal limited to the user (`drwx------`).

## Notes

- Apply least privilege: remove unneeded write/execute rights promptly.
- Verify after each `chmod` with `ls -l` to ensure intended effect.
- Use hidden files (prefixed with `.`) for archived or reference material requiring minimal access.


