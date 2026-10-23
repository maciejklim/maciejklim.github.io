---
title: "Windows Active Directory Checkup"
date: "2026-04-12"
summary: "A practical Active Directory health checklist covering user accounts, domain controllers, replication, Group Policy, and security best practices."
categories: ["Identity and Access"]
tags: ["Active Directory", "Hardening", "Blue Team"]
draft: true
slug: "Windows Active Directory Checkup"
---


## What you should be doing

## Review AD computers
* Anything deprecated to delete?
* Anything not logged in a long time that should not be?

## Review Authentication
* Are any deprecated employees still listed?
* Any users with **password never expires** besides service accounts?
* Any stale privleged accounts (domain admins)?
* Are legacy protocols enabled (NTLMv1, SMBv1)?

## Group Policy Review
* Any unused or stale GPOs?
* Any GPOs linked at wrong OU levels?
* Any recent changes to:
  * Password policy
  * Account lockout policy
  * Audit policy
* Are users in correct OU's?
* Are users in correct groups?


## Review Replication

* ```repadmin /replsum```
* Are all replications healthy?
*
## Review Dianogstics

* ```Dcdiag```
* Are all checks passing?

## Review Time Server

* Run ```w32tm``. is it accurate?
* Are you using custom NTP servers? (pool.ntp.org)
*

