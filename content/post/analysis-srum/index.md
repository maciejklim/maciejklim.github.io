---
title: "Your computer knows exactly how much data every single app has sent to the internet"
date: "2025-12-07"
description: "Learn how to analyze the SRUBD.dat file."
categories: "Forensics"
image: banner934.jpg
draft: false
---

## Here's something wild

Your Windows device knows exactly how much data every single app has sent to the internet.

It's called **System Resoruce Usage Monitor** (SRUM).

Windows logs the network usage of every process for the last 30-60d to a database located ```C:\Windows\System32\sru\SRUDB.dat```. Forensics teams use this to prove exfiltration. It can also be analyzed to see what applications are sending data, how much data, and at what time the data was sent.

The suspect: "I didn't steal the company data!"

The SRUM: "Then why did Edge.exe upload 20Gb of data at 1am on a Saturday?

SRUM is a reminder that transparency isn't optional on centralized systems...it's built in. The device becomes an investigator long before any investigator arrives. Even if you wipe the footprints, the terrain still shows where you ran.

## Accessing the SRUM database

You can use open-source tool srum-dump https://github.com/MarkBaggett/srum-dump. As the tool suggests, it extracts all records from the SRUM database file, and exports them into an Excel spreadsheet. 

Download the binary and run it as an administrator. Follow the prompts to select your ```srubd.dat``` file and wait for the application to generate your report.

*This utility also supports CLI commands, which can be found documented on the vendor's Github.*

Here's an example of the generated output:

![srum-dump report](EXCEL_OQc6vgmBO6.png)

From here, the *Application/Process* column becomes one of the most valuable fields. It allows you to quickly identify unusual or suspicious binaries that may not align with normal workstation activity.

### Common next steps

- Sorting by *Total Bytes* to identify processes consuming unexpected amounts of network bandwidth.
- Filtering timestamps to show activity occurring outside normal business hours.
- Using Excel formulas or pivot tables to highlight anomalies, correlate processes, or enrich findings with other telemetry sources.

This forms the foundation for spotting persistence mechanisms, unauthorized data transfers, or binaries that simply don’t belong on the system.