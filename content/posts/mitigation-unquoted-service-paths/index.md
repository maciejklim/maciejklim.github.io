---
title: "CVE-2023-3438: Unquoted Service Path"
date: "2025-05-09"
summary: "Windows doesn’t forgive sloppy service paths. Learn how a single missing quote lets attackers hijack execution flow and escalate straight to SYSTEM."
categories:
    - Mitigation
    - Blue Team
---

| Base Score | Base Severity | CVSS Vector | Exploitability Score | Impact Score | Total Score | Source |
|------------|---------------|-------------|--------------------|--------------|-------------|--------|
| <span style="background-color:red; color:white; padding:2px 6px; border-radius:6px;">7.8</span> | HIGH | CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | HIGH | 1.8 | 5.9 | NIST |
| <span style="background-color:orange; color:white; padding:2px 6px; border-radius:6px;">4.4</span> | MEDIUM | CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H | MEDIUM | 0.8 | 3.6 | Trellix |


## Threat: Unquoted Service Path

On Windows, services often start executables automatically with **SYSTEM** privileges.

If a service’s executable path _contains spaces_ and is _not wrapped in quotes_, Windows may interpret the path incorrectly.

This allows an attacker to place a _malicious executable earlier in the path_, which Windows may run instead of the intended service binary.

## Why This Happens

When Windows sees a service path like:

```C:\Program Files\Mozilla Firefox\Updater.exe```

And it is _not quoted_, Windows tries to execute the path in this order:

1) ```C:\Program.exe```
2) ```C:\Program Files\Mozilla.exe```
3) ```C:\Program Files\Mozilla Firefox\Updater.exe``` (the legitimate binary)

The attacker can write a file to one of those earlier locations. Windows will execute the attackers file first, often as SYSTEM.

## Attacker Workflow

An attacker would typically follow these steps

**1) Identify vulnerable services**
   
```powershell
Get-WmiObject win32_service | select Name,PathName,StartMode,StartName | where {$_.StartMode -ne "Disabled" -and $_.StartName -eq "LocalSystem" -and $_.PathName -notmatch "`"" -and $_.PathName -notmatch "C:\\Windows"} | Format-List
```

**2) Verify write permissions**

```powershell
icacls C:\Windows\Mozilla Firefox
```

**3) Plant a malicious binary**

```c:\Program Files\Mozilla.exe```

**4) Trigger a service restart or system reboot.**

When a a restart occurs, Windows executes the attackers binary _instead of_ the legitimate service binary.

**5) Privileged escalation achieved**

Because services often run as SYSTEM, the attackers code now runs with _full system privileges_.

## Identification

A quick way to identify unquoted service paths is to run the following Powershell command:

```ps1
Get-WmiObject win32_service | select Name,PathName,StartMode,StartName | where {$_.StartMode -ne "Disabled" -and $_.StartName -eq "LocalSystem" -and $_.PathName -notmatch "`"" -and $_.PathName -notmatch "C:\\Windows"} | Format-List
```

## Remediation

The fix is simple: *always wrap service executable paths in quotes*.

Example (secure):
```"C:\Program Files\Mozilla Firefox\Updater.exe"```

This forces Windows to interpret the full path correctly and prevent path hijacking.