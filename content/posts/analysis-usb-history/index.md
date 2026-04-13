---
title: "Windows USB Forensics"
date: "2025-12-20"
summary: "Learn how to identify historical USB activity, including tracing connected devices and artifacts left behind."
categories: "Forensics"
---

## Windows never forgets your USB

You think running "Portable Chrome" or "hacker Tools" from a USB drive is keeping you invisible. It doesn't.

The second you plug a portable drive in, Windows logs the volume serial number to the registry.

When forensic analysts review a system, they can reconstruct:

1) Device "KingstonDT" connected at 9:00
2) Prefetch shows "mimikatz.exe" ran at 9:01.

Unplugging the drive doesn't scrub the registry.

## Where Windows stores USB history in registry

Windows records USB storage devices under ```HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR```

Let's see what's inside with ```Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR' | Get-childitem```

```Powershell
PS C:\> Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR' | Get-childitem

Hive: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR\Disk&Ven_PNY&Prod_USB_2.0_FD&Rev_1100

Name                 Property
----                 --------
0510101000022047&0   DeviceDesc    : @disk.inf,%disk_devdesc%;Disk drive
                     Capabilities  : 16
                     Address       : 3
                     ContainerID   : {9cd1b6f2-c2a4-5ea2-ace7-55fc22be3323}
                     HardwareID    : {USBSTOR\DiskPNY_____USB_2.0_FD______1100, USBSTOR\DiskPNY_____USB_2.0_FD______, USBSTOR\DiskPNY_____, USBSTOR\PNY_____USB_2.0_FD______1...}
                     CompatibleIDs : {USBSTOR\Disk, USBSTOR\RAW, GenDisk}
                     ClassGUID     : {4d36e967-e325-22ce-bfc1-08002be10428}
                     Service       : disk
                     Driver        : {4d36e967-e325-22ce-bfc1-08002be10428}\0002
                     Mfg           : @disk.inf,%genmanufacturer%;(Standard disk drives)
                     FriendlyName  : PNY USB 2.0 FD USB Device
                     ConfigFlags   : 0
```

This key reveals:

* Device make/model
* Vendor and product IDs
* Unique serial numbers

Each plugged-in USB gets its own persistent entry.

## The myth of running it from USB

> **Threat Actor:** I ran it from a USB, I'm invincible
>
> **Windows:** Writes 15 artifacts, 3 logs, 2 prefetch files, and DF/IR timeline

Portable doesn't mean invisible. Removable doesn't mean untraceable. Windows is watching, and it's taking notes.

## Investigating timestamps

Powershell on it's own cannot provide time metadata. We'll use **RECmd.exe**, a registry parsing tool from https://github.com/EricZimmerman/RECmd.

Since we already identified the registry path of our PNY USB, we'll pass a portion of the hive path to RECmd.

```Powershell
PS C:\users\user\documents\recmd> reg save HKLM\SYSTEM C:\Temp\SYSTEM.hive
The operation completed successfully.
PS C:\users\user\documents\recmd> .\RECmd.exe -f C:\Temp\SYSTEM.hive --kn "ControlSet001\Enum\USBSTOR\Disk&Ven_PNY&Prod_USB_2.0_FD&Rev_1100"
RECmd version 2.1.0.0

Author: Eric Zimmerman (saericzimmerman@gmail.com)
https://github.com/EricZimmerman/RECmd

Note: Enclose all strings containing spaces (and all RegEx) with double quotes

Command line: -f C:\Temp\SYSTEM.hive --kn ControlSet001\Enum\USBSTOR\Disk&Ven_PNY&Prod_USB_2.0_FD&Rev_1100


Processing hive C:\Temp\SYSTEM.hive

        Key path: ControlSet001\Enum\USBSTOR\Disk&Ven_PNY&Prod_USB_2.0_FD&Rev_1100
        Last write time: 2025-11-30 18:13:46.2601654

        Subkey count: 1
        Values count: 0

        ------------ Subkey #0 ------------
        Name: 0410100000012047&0 (Last write: 2025-11-30 18:13:46.2785815) Value count: 12
```

Let's analyze the output:

**Last Write Time:** First time (UTC) this USB was inserted.

**Value Count:** Not the amount of times USB was inserted. It's the number of registry values stored under this key.

## Rebuilding USB connection history

Windows doesn't log every USB by default. You'll have to update your logging policy.

```auditpol /set /subcategory:"Removable Storage" /success:enable /failure:enable```

This makes Windows start recording **device insertion/removal events**. Events will be written in the **Security log**. They can later be fetched using the snippet below.

```Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 6419 } | Select-Object TimeCreated, Id, Message```

