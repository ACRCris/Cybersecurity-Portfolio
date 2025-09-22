# Lab Solution: Find Files with Linux Commands

<!-- GitHub strips <style> tags. Using callouts/details instead for highlighting. -->

This Google Cloud lab practices navigating the Linux filesystem and locating files using core shell commands. The steps below capture the commands executed and the expected results.

## Environment

- Platform: Google Cloud lab environment (Debian-based VM)
- Shell: Bash (`analyst` user)

## Commands executed

### Task 1 – Inspect current directory

```bash
pwd
```
This command prints:

```plaintext
/home/analyst
```
> [!NOTE] Question
> What is your current working directory?
> - [ ] `/home/analyst/logs`
> - [x] `/home/analyst`
> - [ ] `/home`
> - [ ] `/var/logs`

```
ls
```
This command lists:

```plaintext
logs  projects  reports  temp
```
Four directories are contained in `/home/analyst`. 
> [!NOTE] Question
> How many directories are in the current working directory?
> - [ ] Five
> - [x] Four
> - [ ] One
> - [ ] Two

### Task 2 – Change directories and list subdirectories

```bash
cd /home/analyst/reports
ls
```
First, `cd` navigates to the `reports` directory. Then, `ls` lists:

```plaintext
users
```

users is the name of the subdirectory.
> [!NOTE] Question
> What is the name of the subdirectory inside `/home/analyst/reports`?
> - [ ] analyst
> - [ ] projects
> - [ ] logs
> - [x] users



### Task 3 – Locate and read a file

```bash
cd users
ls
cat Q1_added_users.txt
```
First, `cd` changes to the `users` directory. Then, `ls` lists:

```plaintext
Q1_added_users.txt  Q1_deleted_users.txt
```
Finally, `cat Q1_added_users.txt` displays the contents of the file, which includes lines like:

```plaintext
employee_id  username  department
1001         bmoreno   Marketing
1026         apatel    Human Resources
1041         cgriffin  Sales
1104         mreed     Information Technology
1177         aezra     Human Resources
1188         noshiro   Finance
```
From this, we can answer:
- The department for user `aezra` is **Human Resources**
- The `employee_id` for user `mreed` in Information Technology is **1104**
> [!NOTE] Question
> In which department does the employee with username `aezra` work?
> - [x] Human Resources
> - [ ] Sales
> - [ ] Information Technology
> - [ ] Finance

> [!NOTE] Question
> What is the `employee_id` of user `mreed` in the Information Technology department?
> - [ ] 1188
> - [ ] 1177
> - [ ] 1001
> - [x] 1104

### Task 4 – Examine log file contents

```bash
cd ../../logs/
ls
head server_logs.txt
```

First, `cd ../../logs/` moves up two directories to `/home/analyst` and then into `logs`. Then, `ls` lists:

```plaintext
server_logs.txt
```
Finally, `head server_logs.txt` shows the first 10 lines of the log file, which include entries like:

```plaintext
2022-09-28 13:55:55 info    User logged on successfully
2022-09-28 13:56:22 error   The password is incorrect
2022-09-28 13:56:48 warning The file storage is 75% full
2022-09-28 15:55:55 info    User logged on successfully
2022-09-28 15:56:22 error   The username is incorrect
2022-09-28 15:56:48 warning The file storage is 90% full
2022-09-28 16:55:55 info    User navigated to settings page
2022-09-28 16:56:22 error   The password is incorrect
2022-09-28 16:56:48 warning The current user’s password expires in 15 days
2022-09-29 13:55:55 info    User logged on successfully
```
From this, we can answer:
- There are **3** warning messages in the first 10 lines of `server_logs.txt`.
> [!NOTE] Question
> How many warning messages are in the first 10 lines of `server_logs.txt`?
> - [ ] Two
> - [ ] One
> - [ ] Six
> - [x] Three

## Validation

- `pwd` confirms each directory change (`/home/analyst`, `/home/analyst/reports`, `/home/analyst/reports/users`, `/home/analyst/logs`).
- `cat` and `head` output match the expected questions in the lab (department for `aezra`, employee_id for `mreed`, number of warnings, etc.).
- `ls` at each step lists the files/directories referenced in the instructions.

## Notes

- `cd -` can be used to jump back to the previous directory if needed.
- `head` defaults to 10 lines; using `head -n <count>` customizes the output.
