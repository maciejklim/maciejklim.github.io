---
title: "CVE 2013-3900: WinVerifyTrust Signature Validation"
date: "2025-05-09"
summary: "When signature validation is lax, detection breaks. See what defenders must do to close that gap."
categories:
    - Mitigation
    - Blue Team
---

| Base Score | Base Severity | CVSS Vector | Exploitability Score | Impact Score | Score Source |
|------------|---------------|-------------|--------------------|--------------|--------------|
| <span style="background-color:red; color:white; padding:2px 6px; border-radius:6px;">7.6</span> | HIGH | AV:N/AC:H/Au:N/C:C/I:C/A:C | <span style="background-color:green; color:white; padding:2px 6px; border-radius:6px;">4.9</span> | <span style="background-color:red; color:white; padding:2px 6px; border-radius:6px;">10.0</span> | NIST |
| <span style="background-color:red; color:white; padding:2px 6px; border-radius:6px;">8.8</span> | HIGH | CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | <span style="background-color:green; color:white; padding:2px 6px; border-radius:6px;">2.8</span> | <span style="background-color:orange; color:white; padding:2px 6px; border-radius:6px;">5.9</span> | 134c704f-9b21-4f2e-91b3-4a467353bcc0 |
| <span style="background-color:red; color:white; padding:2px 6px; border-radius:6px;">8.8</span> | HIGH | CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | <span style="background-color:green; color:white; padding:2px 6px; border-radius:6px;">2.8</span> | <span style="background-color:orange; color:white; padding:2px 6px; border-radius:6px;">5.9</span> | NIST |
| <span style="background-color:orange; color:white; padding:2px 6px; border-radius:6px;">5.5</span> | MEDIUM | CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N | <span style="background-color:yellow; color:black; padding:2px 6px; border-radius:6px;">1.8</span> | <span style="background-color:yellow; color:black; padding:2px 6px; border-radius:6px;">3.6</span> | Microsoft Corporation |
| <span style="background-color:red; color:white; padding:2px 6px; border-radius:6px;">7.4</span> | HIGH | CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:N/I:H/A:N | <span style="background-color:green; color:white; padding:2px 6px; border-radius:6px;">2.8</span> | <span style="background-color:orange; color:white; padding:2px 6px; border-radius:6px;">4.0</span> | Microsoft Corporation |


## Threat

CVE-2013-3900 allows attackers to *tamper with digitally signed Windows executables* without breaking their signature.
A file can appear properly signed and trusted by Windows, even though its contents have been maliciously modified.

This undermines one of Windows’ core trust mechanisms: *code signing*.

## Why This Happens

Windows uses the ```WinVerifyTrust``` API to validate digital signatures.

Prior to the fix, Windows does not strictly enforce where a signature must appear inside a file. As a result:

* An executable could be signed
* Then extra malicious data appended
* And Windows would still report the file as validly signed

In short:

> Windows verified the signature, but didn’t verify everything the signature was supposed to protect.

## Attacker Workflow

A typical attacker would abuse this flaw as follows:

**1) Start with a legitimately signed executable**

This could be a trusted vendor binary or a stolen signed file.

**2) Append malicious content**

The attacker adds extra code or payload data to the end of the file after it has been signed.

**3) Distribute the trojanized binary**

Email attachments, downloads, USB drops, or malware loaders.

**4) Bypass trust-based defenses**

Windows, users, and some security products see:
* A valid digital signature
* A trusted publisher
* No obvious warnings

**5) Execute malicious code**

The payload runs while the file still appears legitimate.

## Identification

This vulnerability is not detectable by file hash or signature status alone. Indicators include:

* Signed binaries with unexpected file size changes
* Signed executables containing overlay data
* Malware samples that show:
  *  Valid signatures
  * Post-signing file modifications

On affected systems, Windows will report:

> “This digital signature is OK.”

even when the file has been altered.

## Remediation

Microsoft released an update that introduces strict signature validation. The problem is you have to manually apply it in most cases.

The solution is easy. *Enable strict WinVerifyTrust validation* via registry setting. 

```Powershell
New-Item -Path "HKLM:\Software\Microsoft\Cryptography\Wintrust\Config" -Force | Out-Null
New-ItemProperty -Path "HKLM:\Software\Microsoft\Cryptography\Wintrust\Config" -Name "EnableCertPaddingCheck" -PropertyType DWord -Value 1 -Force

New-Item -Path "HKLM:\Software\Wow6432Node\Microsoft\Cryptography\Wintrust\Config" -Force | Out-Null
New-ItemProperty -Path "HKLM:\Software\Wow6432Node\Microsoft\Cryptography\Wintrust\Config" -Name "EnableCertPaddingCheck" -PropertyType DWord -Value 1 -Force
```

### What This Does
**Before**: Windows checks the signature, not the entire file.

**After**: Windows checks the signature *and* ensures nothing was added or modified.