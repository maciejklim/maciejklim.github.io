---
title: "CVE 2013-3900: WinVerifyTrust Signature Validation"
date: "2025-05-09"
summary: "When signature validation is lax, detection breaks. See what defenders must do to close that gap."
categories:
    - Mitigation
    - Blue Team
---

## Threat Overview

CVE-2013-3900 allows attackers to **tamper with digitally signed Windows executables** without breaking their signature.

A file can appear properly signed and trusted by Windows, even though its contents have been maliciously modified.

This undermines one of Windows’ core trust mechanisms: code signing.

## Why This Happens

Windows uses the ```WinVerifyTrust``` API to validate digital signatures.

Prior to the remediation, Windows does not strictly enforce where a signature appears inside a file. As a result:

* An executable can be signed
* Extra malicious data can be appended afterward
* Windows still reports the file as validly signed

> Windows verifies the signature, but not the entire file it is supposed to protect.

## How Threat Actors Abuse It

The exploitation chain is simple and effective.

**1) Start with a legitimately signed executable**

This could be a trusted vendor binary or a stolen signed file.

**2) Append malicious content**

The attacker adds extra code or payload data to the end of the file after signing.

**3) Distribute the trojanized binary**

Email attachments, downloads, USB drops, or malware loaders.

**4) Bypass trust-based defenses**

At execution time, Windows sees:
* A valid digital signature
* A trusted publisher
* No obvious warnings

**5) Execute malicious code**

The payload runs while the file still appears legitimate.

## What Defenders Should Look For

This vulnerability is not detectable by file hash or signature status alone. Indicators include:

* Signed binaries with unexpected file size changes
* Signed executables containing overlay data
* Samples showing:
  * Valid signatures
  * Post-signing file modifications

On affected systems, Windows will report:

> “This digital signature is OK.”

even when the file has been altered.

## Remediation

Microsoft released an update that introduces strict signature validation. The issue is that it must often be explicitly enabled in legacy or unmanaged environments.

The solution is straightforward: **enable strict WinVerifyTrust validation** via registry configuration.

```powershell
New-Item -Path "HKLM:\Software\Microsoft\Cryptography\Wintrust\Config" -Force | Out-Null
New-ItemProperty -Path "HKLM:\Software\Microsoft\Cryptography\Wintrust\Config" -Name "EnableCertPaddingCheck" -PropertyType DWord -Value 1 -Force

New-Item -Path "HKLM:\Software\Wow6432Node\Microsoft\Cryptography\Wintrust\Config" -Force | Out-Null
New-ItemProperty -Path "HKLM:\Software\Wow6432Node\Microsoft\Cryptography\Wintrust\Config" -Name "EnableCertPaddingCheck" -PropertyType DWord -Value 1 -Force