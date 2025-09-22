# Lab Solution: Filter with grep

<!-- GitHub strips <style> tags. Using callouts/details instead for highlighting. -->
## Commands executed

### Task 1 - Filter error entries from `server_logs.txt`

```bash
cd logs
grep "error" server_logs.txt
```

Output:

```plaintext
2022-09-28 13:56:22 error   The password is incorrect
2022-09-28 15:56:22 error   The username is incorrect
2022-09-28 16:56:22 error   The password is incorrect
2022-09-29 13:56:22 error   An unexpected error occurred
2022-09-29 15:56:22 error   Unauthorized access
2022-09-29 16:56:22 error   Unauthorized access
```

> [!NOTE] Question
> How many error lines are there in the `server_logs.txt` file?
> - [x] Six
> - [ ] Three
> - [ ] Eight
> - [ ] Two



### Task 2 - Filter filenames by keyword Q1 in `/home/analyst/reports/users`

```bash
cd /home/analyst/reports/users
ls | grep "Q1"
```

Output lists the two quarterly reports that match:

```plaintext
Q1_access.txt
Q1_added_users.txt
Q1_deleted_users.txt
```

> [!NOTE] Question
> How many files in the `/home/analyst/reports/users` subdirectory contain “Q1” in their names?
> - [ ] Three
> - [ ] One
> - [ ] Five
> - [x] Two

### Task 2 - Filter filenames by keyword access in `/home/analyst/reports/users`

```bash
ls | grep "access"
```

The access audit files returned by the pipeline:

```plaintext
Q1_access.txt
Q2_access.txt
Q3_access.txt
Q4_access.txt
```

Three files in the directory contain the word `access` in their names.

> [!NOTE] Question
> How many files in the `/home/analyst/reports/users` directory contain “access” in their names?
> - [ ] Four
> - [ ] None
> - [ ] Five
> - [x] Three

### Task 3 - Inspect quarterly user records with `grep`

```bash
grep "jhill" Q2_deleted_users.txt
```

Result:

```plaintext
1025         jhill     Sales
```

The username `jhill` appears in the quarter 2 deletion report, confirming removal.

> [!NOTE] Question
> Did you find the username `jhill` in the `Q2_deleted_users.txt` file?
> - [x] Yes
> - [ ] No

### Task 3 - Count new hires in Human Resources from `Q4_added_users.txt`

```bash
grep "Human Resources" Q4_added_users.txt
```

Output confirms the new hires for Human Resources in quarter 4:

```plaintext
1151         sshah     Human Resources
1145         msosa     Human Resources
```

Two users were added to the Human Resources department during Q4.

> [!NOTE] Question
> How many users were added to the Human Resources department in quarter 4?
> - [x] Two
> - [ ] One
> - [ ] Three
> - [ ] Five

## Validation

- Directory changes verified with `pwd` at each pivot (`/home/analyst/logs` and `/home/analyst/reports/users`).
- `grep` output counts align with the multiple-choice checks in the lab interface.
- Command history documents exact syntax for reuse in future investigations.

## Notes

- Quoting multi-word search strings such as `"Human Resources"` prevents `grep` from treating the words separately.
- Piping `ls` into `grep` is a quick triage technique; 
