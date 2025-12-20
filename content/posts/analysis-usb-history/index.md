---
title: "Windows is saving every USB storage device you plug in"
date: "2025-12-20"
summary: "Learn how to analyze the registry for USB storage history."
categories: "Forensics"
---

## Windows Never Forgets Your USB

You think running "Portable Chrome" or "hacker Tools" from a USB drive is keeping you invisible. It doesn't.

The second you plug that drive in, Windows logs the Volume serial number to the registry.

When forensics analysis audit the machine, they see:

1) Device "KingstonDT" connected at 9:00
2) Prefetch shows "mimikatz.exe" ran at 9:01.

Unplugging the drive doesn't scrub the registry.

## Where Windows Stores USB History In Registry

Windows records USB storage devices under:

```HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR```

![USBSTOR Registry](regedit_6LeRlKqUrq.png)

This key reveals:

* Device make/model
* Vendor and product IDs
* Unique serial numbers

Each plugged-in USB gets its own persistent entry.

## The Myth Of Running It From USB

> **Threat Actor:** I ran it from a USB, I'm invincible

> **Windows:** Writes 15 artifacts, 3 logs, 2 prefetch files, and DF/IR timeline

Portable doesn't mean invisible. Removable doesn't mean untraceable. Windows is watching, and it's taking notes.