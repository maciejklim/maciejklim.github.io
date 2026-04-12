---
title: "CVE-2023-3438: Unquoted Service Path"
date: "2025-05-09"
summary: "Windows doesn’t forgive sloppy service paths. Learn how a single missing quote lets attackers hijack execution flow and escalate to SYSTEM."
categories:
    - Mitigation
    - Blue Team
---

## Threat Overview

On Windows, services often start executables automatically with **SYSTEM** privileges.

If a service’s executable path contains spaces and is not wrapped in quotes, Windows may interpret the path incorrectly.

This creates an opportunity for attackers to place a malicious executable earlier in the resolved path chain.

## Why This Happens

When Windows sees a service path like:

```C:\Program Files\Mozilla Firefox\Updater.exe```

And it is not quoted, Windows tries to execute the path in this order:

1) ```C:\Program.exe```
2) ```C:\Program Files\Mozilla.exe```
3) ```C:\Program Files\Mozilla Firefox\Updater.exe``` (the legitimate binary)

The attacker can write a file to one of those earlier locations. Windows will execute the attackers file first, often as SYSTEM.

## Threat Actor Workflow

An attacker would typically follow these steps:

**1) Identify vulnerable services**

```powershell
Get-WmiObject win32_service |
Select-Object Name, PathName, StartMode, StartName |
Where-Object {
    $_.StartMode -ne "Disabled" -and
    $_.StartName -eq "LocalSystem" -and
    $_.PathName -notmatch "`"" -and
    $_.PathName -notmatch "C:\\Windows"
} | Format-List
```

**2) Verify write permissions**

```icacls C:\Windows\Mozilla Firefox```

**3) Plant a malicious binary**

Example: ```c:\Program Files\Mozilla.exe```

**4) Trigger a service restart or system reboot.**

On restart, Windows executes the attacker-controlled binary instead of the real one.

**5) Privileged escalation achieved**

Because services often run as SYSTEM, the attackers code now runs with full system privileges.

## What Defenders Should Look For

You can quickly enumerate potentially vulnerable services the same way a threat actor would.

```ps1
Get-WmiObject win32_service |
Select-Object Name, PathName, StartMode, StartName |
Where-Object {
    $_.StartMode -ne "Disabled" -and
    $_.StartName -eq "LocalSystem" -and
    $_.PathName -notmatch "`"" -and
    $_.PathName -notmatch "C:\\Windows"
} | Format-List
```

Look specifically for:
* Paths containing spaces
* Missing quotation marks
* Services running as LocalSystem

## Remediation

The fix is simple: **always wrap service executable paths in quotes**.

* Secure:
```"C:\Program Files\Mozilla Firefox\Updater.exe"```


* Not secure:
```C:\Program Files\Mozilla Firefox\Updater.exe```


This forces Windows to interpret the full path, and prevent path hijacking.