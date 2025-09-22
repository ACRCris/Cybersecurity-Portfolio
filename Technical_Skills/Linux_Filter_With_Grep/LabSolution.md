# Lab Solution: Filter with grep

<style>
.mc-card{background:#0f172a;border:1px solid #334155;border-radius:8px;padding:12px;margin:12px 0}
.mc-question code{background:#111827;border-radius:4px;padding:2px 6px}
</style>
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

<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">How many error lines are there in the <code>server_logs.txt</code> file?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task1-errors" value="Six" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Six</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-errors" value="Three" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Three</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-errors" value="Eight" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Eight</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task1-errors" value="Two" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Two</span>
        </label>
      </form>
    </div>
  </div>
</div>



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

<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">How many files in the <code>/home/analyst/reports/users</code> subdirectory contain “Q1” in their names?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task2-q1" value="Three" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Three</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-q1" value="One" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">One</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-q1" value="Five" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Five</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-q1" value="Two" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Two</span>
        </label>
      </form>
  </div>
</div>

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

<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">How many files in the <code>/home/analyst/reports/users</code> directory contain “access” in their names?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task2-access" value="Four" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Four</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-access" value="None" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">None</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-access" value="Five" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Five</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task2-access" value="Three" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Three</span>
        </label>
      </form>
    </div>
  </div>
</div>

### Task 3 - Inspect quarterly user records with `grep`

```bash
grep "jhill" Q2_deleted_users.txt
```

Result:

```plaintext
1025         jhill     Sales
```

The username `jhill` appears in the quarter 2 deletion report, confirming removal.

<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">Did you find the username <code>jhill</code> in the <code>Q2_deleted_users.txt</code> file?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task3-jhill" value="Yes" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Yes</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-jhill" value="No" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">No</span>
        </label>
      </form>
  </div>
</div>

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

<div class="mc-wrapper">
  <div class="mc-card">
    <div class="mc-rail" aria-hidden="true">
      <span class="mc-rail__dot"></span>
    </div>
    <div class="mc-content">
      <p class="mc-question">How many users were added to the Human Resources department in quarter 4?</p>
      <form class="mc-options">
        <label class="mc-option">
          <input type="radio" name="task3-hr" value="Two" checked />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Two</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-hr" value="One" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">One</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-hr" value="Three" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Three</span>
        </label>
        <label class="mc-option">
          <input type="radio" name="task3-hr" value="Five" />
          <span class="mc-option__radio"></span>
          <span class="mc-option__text">Five</span>
        </label>
      </form>
  </div>
</div>

## Validation

- Directory changes verified with `pwd` at each pivot (`/home/analyst/logs` and `/home/analyst/reports/users`).
- `grep` output counts align with the multiple-choice checks in the lab interface.
- Command history documents exact syntax for reuse in future investigations.

## Notes

- Quoting multi-word search strings such as `"Human Resources"` prevents `grep` from treating the words separately.
- Piping `ls` into `grep` is a quick triage technique; 
