## <a name="step4"></a>Task 1: Make sure APT is installed

- Ran the command to verify that APT is installed:

```bash
apt
```

- Received APT help output, confirming installation. Example output:

```plaintext
apt 1.8.2.3 (amd64)
Usage: apt [options] command
...
```


## <a name="step5"></a>Task 2: Install and uninstall the Suricata application


- Ran the command to install Suricata:

```bash
sudo apt install suricata
```

- Verified the installation by running `suricata`, seeing a header like:

```plaintext
Suricata 4.1.2
USAGE: suricata [OPTIONS] [BPF FILTER]
...
```

- Uninstalled Suricata:

```bash
sudo apt remove suricata
```

- Verified the uninstallation by running `suricata` again:

```plaintext
-bash: /usr/bin/suricata: No such file or directory
```

## <a name="step6"></a>Task 3: Install the tcpdump application

- Ran the command to install `tcpdump`:

```bash
sudo apt install tcpdump
```

- Its presence will be verified in Task 4 by listing installed packages.



## <a name="step7"></a>Task 4: Generate a list of installed applications

- Ran the command to list installed packages:

```bash
apt list --installed
```

- Verified that `tcpdump` appears in the list (optionally filter):

```bash
apt list --installed | grep -E '^(tcpdump|suricata)/'
```

Example output:

```plaintext
tcpdump/oldstable,now 4.9.3-1~deb10u2 amd64 [installed]
```

## <a name="step8"></a>Task 5: Reinstall the Suricata application
1. Reinstall Suricata:

```bash
sudo apt install suricata
```

2. List installed packages again:

```bash
apt list --installed
```

Verify that both programs appear:

```plaintext
...
suricata/oldstable,now 1:4.1.2-2+deb10u1 amd64 [installed]
tcpdump/oldstable,now 4.9.3-1~deb10u2 amd64 [installed]
...
```

- Ran the command to reinstall Suricata:

```bash
sudo apt install suricata
```

- Verified that `suricata` and `tcpdump` are installed by listing packages:

```bash
apt list --installed | grep -E '^(suricata|tcpdump)/'
```

Example output:

```plaintext
suricata/oldstable,now 1:4.1.2-2+deb10u1 amd64 [installed]
tcpdump/oldstable,now 4.9.3-1~deb10u2 amd64 [installed]
```


## Validation

- `apt` command displays usage details, confirming the package manager is present.
- Running `suricata` after installation shows the version banner; after removal it returns “No such file or directory.”
- `apt list --installed` (optionally filtered with `grep`) confirms `suricata` and `tcpdump` are installed at the end of the lab.

## Notes

- `sudo` is required for `apt install` and `apt remove` operations.
- Re-running `apt install <package>` is idempotent; it reinstalls or confirms the package is already present.
- Sample outputs in this solution come from the Google Cloud Debian-based VM; versions may vary slightly in other environments.
