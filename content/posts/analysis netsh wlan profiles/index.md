---
title: "Your WiFi connection history, exposed"
date: "2025-12-07"
summary: "Use NETSH to see every network you've connected to. Passwords in plain text. And even geolocation."
categories: "Forensics"
image: "banner4905.jpg"
showTableOfContents: true

---

## You probably weren't told this, but...

Your Windows laptop is keeping a **five-year diary** of everywhere you've ever taken it.

Every time you connect to WiFi, Windows quietly logs three things:
- SSID (network MAC)
- BSSID (router MAC)
- And yes... the **plain-text WiFi password**

All of it can be revealed with a single built-in command.

### How to see the data

Open an **elevated command prompt** and run:

**See every network your machine has ever connected to:**

```netsh wlan show profiles```

**Scope out every access point in range right now:**

```netsh wlan show networks mode=bsid```

**See the wireless password keys:**

```netsh wlan show profile name="SSID_NAME" key=clear```

**Want to dump everything at once?**

```netsh wlan export profile folder=C:\ key=clear```

The catch: Windows doesn't store BSSIDs for past connections. Only the SSID names and keys live in memory. Want to track connection BSSID history? You'll need to use third-party tools.

## Mapping BSSID using Wigle.net
Found a BSSID? You can look it up on Wigle.net and see where that access point has been spotted in the real world.

How to check it:
1. Go to wigle.net and login.
2. Search > WiFi network search
3. Drop the BSSID (aa:bb:cc:dd:ee:ff)

If it's in their crowdsourced database, you'll get its **last known GPS location**, ssid, channel, and timestamps. It's quick, it's OSINT, and it turns a simple MAC address into geo-intel.


## Want to disable Window's access to BSSID's? 
Turn off Windows privacy-location sharing.
```powershell
start ms-settings:privacylocation
```
## The good news: you can wipe this trail clean

If you want to purge your WiFi history, open an **elevated command prompt** and run:

```netsh wlan delete profile name=*```

Done. Your travel diary is gone.

If you're privacy-minded, take it a step further. Turn this into a scheduled task using **Windows Task Scheduler** so your laptop never accumulates a trail again.