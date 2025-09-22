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
<!-- Source: MaterialDeApoyo/FindFilesWithLinuxCommands.md (Task 1) -->
<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">What is your current working directory?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task1-pwd" value="/home/analyst/logs" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">/home/analyst/logs</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-pwd" value="/home/analyst" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">/home/analyst</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-pwd" value="/home" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">/home</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-pwd" value="/var/logs" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">/var/logs</span>
        </label>
      </form>
    </div>
  </div>
</div>

```
ls
```
This command lists:

```plaintext
logs  projects  reports  temp
```
Four directories are contained in `/home/analyst`. 
<!-- Source: MaterialDeApoyo/FindFilesWithLinuxCommands.md (Task 1 count) -->
<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">How many directories are in the current working directory?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task1-count" value="Five" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Five</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-count" value="Four" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Four</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-count" value="One" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">One</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-count" value="Two" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Two</span>
        </label>
      </form>
    </div>
  </div>
</div>

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
<!-- Source: MaterialDeApoyo/FindFilesWithLinuxCommands.md (Task 2) -->
<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">What is the name of the subdirectory inside <code>/home/analyst/reports</code>?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task2-subdir" value="analyst" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">analyst</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-subdir" value="projects" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">projects</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-subdir" value="logs" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">logs</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-subdir" value="users" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">users</span>
        </label>
      </form>
    </div>
  </div>
</div>



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
<!-- Source: MaterialDeApoyo/FindFilesWithLinuxCommands.md (Task 3) -->
<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">In which department does the employee with username <code>aezra</code> work?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task3-aezra" value="Human Resources" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Human Resources</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-aezra" value="Sales" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Sales</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-aezra" value="Information Technology" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Information Technology</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-aezra" value="Finance" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Finance</span>
        </label>
      </form>
    </div>
  </div>
</div>

<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">What is the <code>employee_id</code> of user <code>mreed</code> in the Information Technology department?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task3-mreed" value="1188" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">1188</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-mreed" value="1177" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">1177</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-mreed" value="1001" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">1001</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-mreed" value="1104" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">1104</span>
        </label>
      </form>
    </div>
  </div>
</div>

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
<!-- Source: MaterialDeApoyo/FindFilesWithLinuxCommands.md (Task 4) -->
<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">How many warning messages are in the first 10 lines of <code>server_logs.txt</code>?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task4-warnings" value="Two" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Two</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task4-warnings" value="One" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">One</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task4-warnings" value="Six" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Six</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task4-warnings" value="Three" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Three</span>
        </label>
      </form>
    </div>
  </div>
</div>

## Validation

- `pwd` confirms each directory change (`/home/analyst`, `/home/analyst/reports`, `/home/analyst/reports/users`, `/home/analyst/logs`).
- `cat` and `head` output match the expected questions in the lab (department for `aezra`, employee_id for `mreed`, number of warnings, etc.).
- `ls` at each step lists the files/directories referenced in the instructions.

## Notes

- `cd -` can be used to jump back to the previous directory if needed.
- `head` defaults to 10 lines; using `head -n <count>` customizes the output.
