# Lab Solution: Manage Files with Linux Commands

<!-- GitHub strips <style> tags. Using callouts/details instead for highlighting. -->

This Google Cloud lab practices creating, removing, moving, and editing files and directories using core Linux commands. The steps below capture the commands executed and the expected results.

## Environment

- Platform: Google Cloud lab environment (Debian-based VM)
- Shell: Bash (`analyst` user)

## Commands executed

### Task 1 – Create a new directory

Create a dedicated `logs` subdirectory under `/home/analyst` and verify:

```bash
mkdir -p /home/analyst/logs
ls /home/analyst
```
Expected output includes the new directory:

```plaintext
logs  notes  reports  temp
```

### Task 2 – Remove a directory

Remove the obsolete `temp` directory and verify:

```bash
rmdir /home/analyst/temp
ls /home/analyst
```
Expected output no longer lists `temp`:

```plaintext
logs  notes  reports
```

### Task 3 – Move a file

Move `Q3patches.txt` from `notes` to `reports` and confirm:

```bash
cd /home/analyst/notes
mv Q3patches.txt ../reports/
ls ../reports
```
Expected listing:

```plaintext
Q1patches.txt  Q2patches.txt  Q3patches.txt
```

### Task 4 – Remove a file

Delete the unused `tempnotes.txt` file and confirm:

```bash
rm -f /home/analyst/notes/tempnotes.txt
ls -A /home/analyst/notes
```
Expected: empty output (no files listed in `notes`).

### Task 5 – Create a new file

Create `tasks.txt` in `notes` and confirm:

```bash
touch /home/analyst/notes/tasks.txt
ls /home/analyst/notes
```
Expected:

```plaintext
tasks.txt
```

### Task 6 – Edit a file (nano or non‑interactive alternative)

Open with nano and add two lines describing completed work:

```bash
nano /home/analyst/notes/tasks.txt
```

If you prefer a non‑interactive alternative (useful in automated environments):

```bash
printf "Completed tasks\n1. Managed file structure in /home/analyst\n" > /home/analyst/notes/tasks.txt
```

Verify file contents:

```bash
cat /home/analyst/notes/tasks.txt
```
Expected output:

```plaintext
Completed tasks
1. Managed file structure in /home/analyst
```

## Validation

- `ls /home/analyst` reflects the desired layout: `logs  notes  reports` (no `temp`).
- `ls /home/analyst/reports` shows `Q1patches.txt`, `Q2patches.txt`, and `Q3patches.txt`.
- `notes/tasks.txt` exists and contains the two expected lines.

## Notes

- Use `mkdir -p` and `rm -f` judiciously; they suppress errors and are helpful in idempotent scripts.
- When nano is unavailable or interactive editing is impractical, `printf > file` is a safe, repeatable alternative.
