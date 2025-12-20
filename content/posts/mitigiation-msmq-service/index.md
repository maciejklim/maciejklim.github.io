---
title: "CVE 2024-30080: Microsoft Message Queueing (MSMQ) Remote Code Execution"
date: "2025-05-09"
summary: "Unused Windows features can quietly become RCE's. See how exposed MSMQ services listening on port 1801 put defenders at risk."
categories:
    - Mitigation
    - Blue Team
---

| Base Score                                                                                       | Base Severity | CVSS Vector                                      | Exploitability Score                                                                             | Impact Score                                                                                     | Score Source          |
| ------------------------------------------------------------------------------------------------ | ------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | --------------------- |
| <span style="background-color:#ff4d4d;color:white;padding:2px 6px;border-radius:4px;">9.8</span> | **CRITICAL**  | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H     | <span style="background-color:#90ee90;color:black;padding:2px 6px;border-radius:4px;">3.9</span> | <span style="background-color:#fff59d;color:black;padding:2px 6px;border-radius:4px;">5.9</span> | Microsoft Corporation |
| <span style="background-color:#ff4d4d;color:white;padding:2px 6px;border-radius:4px;">9.8</span> | **CRITICAL**  | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/... | N/A                                                                                              | N/A                                                                                              | MS-CVE-2024-30080     |


## Threat

CVE‑2024‑30080 is a **remote code execution (RCE)** vulnerability in **Microsoft Message Queueing (MSMQ)**.
If MSMQ is enabled, an unauthenticated attacker can send a specially crafted network request and execute code on the target system.

No credentials. No user interaction. Just network access.

## Why This Happens

MSMQ listens on **TCP port 1801** to receive and process queued messages.

The vulnerability exists in how MSMQ **parses incoming messages**, allowing malformed data to trigger memory corruption and code execution.

* MSMQ is often installed but unused
* The service listens by default
* Systems inherit risk simply by having the feature enabled

## Attacker Workflow

From an attacker’s perspective, exploitation is straightforward:

**1) Scan for exposed MSMQ hosts**

Identify systems with port 1801/TCP open

**2) Send a crafted MSMQ packet**

Exploits the vulnerable message parsing logic

**3) Achieve remote code execution**

Code executes in the context of the MSMQ service

**4) Post‑exploitation**

* Lateral movement
* Persistence
* Credential access

This vulnerability is *wormable in nature* when exposed across a network segment.

## Identification

Blue teams should focus on **exposure**, not just patch state.

### Key Checks:
* Is MSMQ Installed?
* Is TCP 1801 listening?
* Is MSMQ actually required by the business?

### Quick Validation (Powershell)

```Powershell
Get-WindowsFeature MSMQ*
```

```Powershell
netstat -ano | findstr :1801
```

If MSMQ is installed and port 1801 is listening, the system is **in scope**.

## Remediation

If MSMQ is **not required by the  business**, the strongest mitigation is remove the feature entirely.

```Powershell
Remove-WindowsFeature MSMQ
```

### Defense In Depth

If MSMQ must remain installed:
* Restrict network access to **TCP 1801**
* Verify port 1801 is **blocked at the host and network level**
* Monitor for unexpected MSMQ traffic.

## Verification
After remediation:
* Confirm MSMQ Feature is removed
* Validate port 1801 is no longer listening
* Document business justification if MSMQ must remain enabled