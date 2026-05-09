---
title: "TeamView Forensics Challenge"
date: "2026-04-22"
summary: "Lets investigate a compromised endpoint"
categories: "Forensics"
image: "feature.jpg"
showTableOfContents: true
draft: true
# https://stumblesec.com/letsdefend-teamviewer-forensics-challenge-walkthrough-652049d9b863
# https://curiosidadesdehackers.com/analisis-dfir-de-acceso-remoto-exfiltracion-de-datos-y-eliminacion-de-evidencias/
---

## Intro

You've likely heard or seen this one before. A threat-actor used software like TeamViewer to perform unauthorized access and exfiltrate data. How would you investigate this scenario if it happened to your organization?

We will investigate a simulated event and examine the actions taken by the attacker after they've gained access to the system. By analyzing the artifacts of the file system, we'll determine when and how the attacker accessed the system, and what data was compromised.

## DF/IR Software Used

We'll use well known tools to conduct this investigation.

* Eric Zimmerman's MFTECmd (https://ericzimmerman.github.io/)
* Powershell
* Notepad

## Scenario

> During the workday, an employee noticed strange unauthorized activity on his computer, with applications opening and the mouse moving. Quickly realizing that someone was accessing his machine via TeamViewer, the employee acted quickly, changing his TeamViewer password and alerting the security team. However, the employee must still clarify how the breach occurred and how far the threat actor has gone.

## 1 Analyze TeamViewer Connections

## 2 Analyze TeamViewer Log File

## 3 Identify Attackers First Access

## 4 Identify Main Session of Attack

## 5 End of Remote Session

## 6 Total Duration of Intrusion

## 7 Powershell Forensic Analysis

### 7.1 Compression of Confidential Information

### 7.2 Data Exfiltration

## 8 Analyze the USN Journal

## 9 Reconstruct Activity

## 10 File Deletion by Attacker

## 11 Attack Timeline

## Conclusion

