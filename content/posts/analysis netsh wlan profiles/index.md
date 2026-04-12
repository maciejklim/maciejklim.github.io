---
title: "Windows WiFi Forensics"
date: "2025-12-07"
summary: "Use netsh to analyze saved WiFi profiles and reconstruct wifi connection history."
categories: "Forensics"
image: "featured.jpg"
showTableOfContents: true

---

## Windows records every WiFi network you joined

Your Windows laptop is keeping a **five-year diary** of everywhere you've ever taken it. Every time you connect to WiFi, Windows quietly logs three things:

- SSID (network MAC)
- BSSID (router MAC)
- And yes... the plain-text WiFi password

All of it can be revealed with a single built-in command.

## How to see the data

Open an **elevated command prompt** and run:


```powershell
# See every network your machine has ever connected to:
netsh wlan show profiles
```

```powershell
# Scope out every access point in range right now:
netsh wlan show networks mode=bssid
```

```powershell
# See the wireless password keys
netsh wlan show profile name="SSID_NAME" key=clear
```

```powershell
# Want to dump everything at once?
netsh wlan export profile folder=C:\ key=clear
```

## Investigating BSSIDs (access points)

WAPs can be analyzed using their BSSID (MAC address).

They can sometimes be correlated to external datasets such as https://wigle.net.

Wigle is a crowdsourced wireless geolocation database that contains:

* SSID
* BSSID
* GPS coordinates
* Observed timestamp

How to check it:
* Go to https://wigle.net and login.
* Click Search > WiFi network search
* Enter the BSSID (aa:bb:cc:dd:ee:ff)

If it's in their crowdsourced database, you'll see the **last known GPS location**, SSID, channel, and timestamps.

It's quick, it's OSINT, and it turns a simple MAC address into geo-intel.


## Disabling Windows access to BSSID metadata
Turn off Windows privacy-location sharing.

```powershell
start ms-settings:privacylocation
```
## Removing stored WiFi profiles

If you want to purge your WiFi history, open an **elevated command prompt** and run:

```powershell
netsh wlan delete profile name=*
```

Done. Your travel diary is gone.

If you're privacy-minded, take it a step further. Turn this into a scheduled task using **Windows Task Scheduler** so your laptop never accumulates a trail again.

## Closing insight

Windows wireless artifacts are not designed as forensic logs. But they still form a record of network interactions.

Even when users forget networks, the system retains enough data to reconstruct their connectivity history.

In forensic investigations, WiFi profiles often become a supporting artifact in broader timeline reconstruction.