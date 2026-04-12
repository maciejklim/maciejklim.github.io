---
title: "CVE 2024-30080: Microsoft Message Queueing (MSMQ) Remote Code Execution"
date: "2025-05-09"
summary: "Unused Windows features can quietly become RCE's. See how exposed MSMQ services listening on port 1801 put defenders at risk."
categories:
    - Mitigation
    - Blue Team
---

## Threat Overview

CVE‑2024‑30080 is a **remote code execution (RCE)** vulnerability in Microsoft Message Queueing (MSMQ).

If MSMQ is enabled, an unauthenticated attacker can send a specially crafted network request and execute code on the target system.

No credentials. No user interaction. Just network access.

## Why This Happens

MSMQ listens on **TCP port 1801** to receive and process queued messages.

The vulnerability exists in how MSMQ parses incoming messages, allowing malformed data to trigger memory corruption and code execution.

* MSMQ is often installed but not used
* The service listens by default
* Systems inherit risk simply by having the feature enabled

## How Threat Actors Abuse It

From an attacker’s perspective, exploitation is straightforward:

**1) Scan for exposed MSMQ hosts**

Identify systems with port 1801/TCP open

**2) Send a crafted MSMQ packet**

Exploits the vulnerable message parsing logic

**3) Achieve remote code execution**

Code executes in the context of the MSMQ service

**4) Post‑exploitation**

Once inside, attackers typically move quickly to:

* Credential access
* Lateral movement
* Persistence

This vulnerability is **wormable in nature** when exposed across a network segment.

## Identification

Blue teams should focus on **exposure first**, not just patch status.

### Key Checks:
* Is MSMQ Installed?
* Is TCP 1801 listening?
* Is MSMQ actually required by the business?

### Quick Validation

```Powershell
# MSMQ Service Enabled?
Get-WindowsFeature MSMQ*
```

```Powershell
# Port 1801 Listening?
netstat -ano | findstr :1801
```

If MSMQ is installed and port 1801 is listening, the system is **in scope** for review.

## Remediation

If MSMQ is not required, the best mitigation is remove the feature entirely.

```Powershell
# Disable MSMQ Service
Remove-WindowsFeature MSMQ
```

### Defense In Depth

If MSMQ must remain installed:
* Restrict access to TCP 1801 at host and network level
* Verify port 1801 is blocked at the host and network level
* Monitor for unexpected or anomalous MSMQ traffic.

## Verification

After remediation:

* Confirm MSMQ Feature is removed (if not required)
* Validate port 1801 is no longer listening
* Document business justification if MSMQ must remain enabled