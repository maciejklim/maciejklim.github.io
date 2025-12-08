---
title: "Your WiFi connection history, exposed"
date: "2025-12-07"
description: "Use NETSH to see every network you've connected to. Passwords in plain text. And even geolocation."
image: "banner4905.jpg"
categories: "Forensics"
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

```netsh wlan show profiles```

To see BSSID addresses:
```netsh wlan show networks mode=bsid```

To view the details, including the password for one of these networks, run:

```netsh wlan show profile name="SSID_NAME" key=clear```

Want to dump everything at once?

```netsh wlan export profile folder=C:\ key=clear```

## Here's the scary part

BSSID is a **physical device ID**. It's tied to real, physical router sitting in a real, physical location.

And here's where it gets wild:

Crowdsourced databases like https://wigle.net/ map millions of **BSSIDs** to real-world coordinates.

Anyone with access to your WiFi history can dump those BSSIDs. Plug the MAC addresses into a public database...

And instantly reconstruct a map of everywhere your laptop has been. 

Your office. Your home. That hotel you stayed at two years ago. The cafe you visited once and forgot.

A full location trail - without ever touching GPS.

## The good news: you can wipe this trail clean

If you want to purge your WiFi history, open an **elevated command prompt** and run:

```netsh wlan delete profile name=*```

Done. Your travel diary is gone.

If you're privacy-minded, take it a step further. Turn this into a **daily scheduled task** using Windows Task Scheduler so your laptop never accumulates a trail again.