# Lab Solution: Examine Shell Inputs and Outputs

This Google Cloud lab focuses on observing how the Linux Bash shell handles user input and displays output. The solution below captures the key commands executed and the expected results.

## Environment

- Platform: Google Cloud lab environment (Debian-based VM)
- Shell: Bash (`analyst` user)

## Commands executed

### Task 1 – Output text with `echo`

```bash
echo hello
echo "hello"
echo "<your_name>"
```

Expected output:

```plaintext
hello
hello
<your_name>
```

### Task 2 – Perform calculations with `expr`

```bash
expr 32 - 8
expr 3500 * 12
```

Expected output:

```plaintext
24
42000
```

Optional exploration:

```bash
expr 25 + 15
expr 100 / 4
```

Expected output:

```plaintext
40
25
```

### Task 3 – Clear the shell

```bash
clear
```

The command clears the terminal window and places the cursor at the top.

## Validation

- `echo` displays the exact string supplied, confirming how Bash echoes input.
- `expr` returns integer math results when operators and numbers are separated by spaces.
- `clear` removes previous commands and output from the visible buffer.

## Notes

- `expr` works with integer arithmetic only; decimals are truncated.
- Quotes around strings ensure Bash treats the text as a single argument, useful when spaces or special characters are involved.
- Screenshots from the lab are stored in `MaterialDeApoyo/` for reference.
