# Lab Solution: Filter with grep

This Google Cloud lab reinforces the use of `grep` and shell pipelines to spot key strings in log files and quarterly user reports. The steps below capture the commands executed and the expected investigative findings.

## Environment

- Platform: Google Cloud lab environment (Debian-based VM)
- Shell: Bash (`analyst` user)

## Commands executed

### Task 1 - Filter error entries from `server_logs.txt`

```bash
cd /home/analyst/logs
grep "error" server_logs.txt
```

Sample output:

```plaintext
2022-09-28 13:56:22 error   The password is incorrect
2022-09-28 15:56:22 error   The username is incorrect
2022-09-28 16:56:22 error   The password is incorrect
```

The command returns three error lines, confirming the volume of failed authentication events in the log.

### Task 2 - Filter filenames by keyword in `/home/analyst/reports/users`

```bash
cd /home/analyst/reports/users
ls | grep "Q1"
```

Output lists the two quarterly reports that match:

```plaintext
Q1_added_users.txt
Q1_deleted_users.txt
```

```bash
ls | grep "access"
```

The access audit files returned by the pipeline:

```plaintext
Q1_access.txt
Q2_access.txt
Q3_access.txt
```

Three files in the directory contain the word `access` in their names.

### Task 3 - Inspect quarterly user records with `grep`

```bash
ls
grep "jhill" Q2_deleted_users.txt
```

Result:

```plaintext
jhill,Jordan Hill,Customer Support
```

The username `jhill` appears in the quarter 2 deletion report, confirming removal.

```bash
grep "Human Resources" Q4_added_users.txt
```

Output confirms the new hires for Human Resources in quarter 4:

```plaintext
1250,mrobles,Human Resources
1324,ehughes,Human Resources
```

Two users were added to the Human Resources department during Q4.

## Validation

- Directory changes verified with `pwd` at each pivot (`/home/analyst/logs` and `/home/analyst/reports/users`).
- `grep` output counts align with the multiple-choice checks in the lab interface.
- Command history documents exact syntax for reuse in future investigations.

## Notes

- Quoting multi-word search strings such as `"Human Resources"` prevents `grep` from treating the words separately.
- Piping `ls` into `grep` is a quick triage technique; for more complex patterns consider `find` or `rg`.
- Redirect the `grep` output to a file if the results must be preserved outside the ephemeral lab environment.
