# Activity Summary

Portfolio Activity: **Reverse-shell proof of concept**, a lab experiment from the BeTek / MAKAIA Cybersecurity Bootcamp studying command-and-control (C2) behavior.

A minimal Python script demonstrating how a reverse shell is established from a Windows host back to an attacker-controlled Kali machine, for the purpose of understanding the mechanics defenders must detect.

## Ethical and safety note

This is a **controlled-laboratory proof of concept**, executed only between virtual machines under my own control. It is included to demonstrate understanding of C2 mechanics from a defensive standpoint — recognizing the network and host indicators a reverse shell produces (outbound connection to an unusual port, `nc`/`netcat` execution, process spawning `cmd.exe`). It is not intended for use against any system without explicit authorization.

## What it demonstrates

- How an outbound connection is used to bypass inbound firewall rules.
- The host indicators of a reverse shell (download of `netcat`, execution of `nc64.exe`, binding of `cmd.exe`).
- Why egress filtering and process monitoring matter for detection.

## Folder Structure and Status

- `reverse_shell.py`: the proof-of-concept script (downloads netcat and connects back to a listener on port 4444).
