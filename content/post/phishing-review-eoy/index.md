---
title: "Phishing Trends: End of 2025 Review"
date: 2025-12-06
image: terracotta-soldiers.jpg
description: Exploring the top phishing trends of 2025. From fake M365 login pages to QR-code scams, and learn practical defenses to protect your organization.
categories:
    - Phishing
---


## Hackers Are Outperforming Your Security Training
Phishing attacks used to be a laughable Nigerian prince scam. Today? Not so much. The game has changed, the attackers have leveled up, and the average user is still relying on outdated “look for spelling errors” advice that hasn’t mattered in years.

Modern phishing isn’t sloppy. It’s smart and engineered to convert. Right now, threat actors have better sales funnels than most companies. The most common phishing attacks have one thing in common: they look exactly like the real thing. 

---

## EOY Trends Observed
With AI and automation at attacker fingertips, phishing campaigns are hitting faster, smarter, and at a growing scale. The FBI reported over $262 million in phishing-related losses this year, and that’s just what was reported. As attackers continue to automate, more under-protected businesses are getting swept up.

Here are the major phishing trends we’ve seen unfold:

- **Fake M365 Login Pages**  
  - Designed to look like real email & SaaS solution login portals
- **QR Code Phishing**  
  - Bypasses most email spam filter solutions
- **Business Email Compromise**  
  - Attackers are scraping your LinkedIn to better target your organization’s employees.

---

## Fake M365 Login Pages
There’s a huge uptick in fake login portals that mimic Microsoft 365, Google Workspace, Docusign, and all the tools your employees trust. Hackers build these sites like a landing page designed to close million-dollar deals.  

What’s making it even harder to spot is these campaigns are hosted behind legitimate services. Instead of shady URLs, they are OneDrive links, and real-looking domains. Threat actors monitor these attacks in real-time, and act within minutes to start hurting businesses.

In many cases, once attackers gain access to an employee’s inbox, they immediately search for company-branded documents, invoices, signatures, or vendor communications. They then use that information to craft highly targeted invoice fraud schemes that can quietly drain organizations of substantial funds before anyone realizes something is wrong.

---

## QR-Code Phishing
Another trend that is exploding is QR-code phishing (quishing). The attacker sends a clean email, maybe an invoice or an invitation. Instead of a link, they will throw in a QR code image. Users pull out their phone, scan it in a hurry, and are funneled into bad sites. No malicious link for the email filtering solution to catch.

---

## Business Email Compromise
The apex predator of phishing. These attacks impersonate your CEO asking for a quick favor, a vendor checking on a late payment, or HR requesting urgent information. They mimic real communication patterns to slip past your instinctive defenses.  

Threat actors are scraping your LinkedIn and company website to identify employee names & job titles. Easily a targeted email is created to look like it came from Jane Doe, your HR director.

---

## Let’s Talk Defense
You need layered protection that assumes attackers will get past the first line. MFA compliance is essential, but even that isn’t bulletproof (see: MFA fatigue). Consider implementing strategies such as:

- Strong identity controls
- Conditional access policies
- Web filtering to identify newly registered domains
- Tackle ‘shadow IT’ tools your employees are using outside of IT department’s scope

Awareness training needs a full makeover too. Stop showing users 2008-era Phish Sim emails. Train your staff in what is seen in the wild. Cybersecurity analysis and IT departments know what these phishing websites look like from exposure, but employees don’t know.  

Create awareness campaigns on what these phishing campaigns look like, and how they can be identified. Further critical to employee education, is having users motivated to report suspicious emails to the proper internal department, rather than asking their office-buddy “does this email look legit”.

---

## Defensive Controls
Let’s talk about practical advice you can implement to harden your environment:

- **Require phishing-resistant MFA in Entra & audit your MFA enrollment**  
  A chain is only as strong as its weakest link. And in most organizations, that link is an unprotected user account. Do you know whether every user in your tenant is enrolled in MFA? Do you have a recurring audit process? Do you have the Entra policy to enforce it?

- **Block sign-ins from new countries & unauthorized VPNs**  
  Conditional access policies are mandatory. Threat actors almost always operate using proxies and VPNs originating from unusual geographical locations, like Kenya. By enforcing location-based and risk-based policies, you can automatically block a sign-in that doesn’t match a user’s normal behavior. Even if credentials are compromised, these controls make it harder for attackers to move forward.

- **Detect QR codes with Microsoft Defender for Office 365 license**  
  Microsoft Defender for Office 365 Plan 1 and Plan 2 include native QR-code inspection. Microsoft uses image extraction to isolate the QR code, analyze the encoded URL, and run it through the same detonation and URL reputation engine used for standard links. Users should never be the first line of defense against malicious QR codes.

- **Block newly registered domains on the DNS level**  
  Tools like DNSFilter and Zorus (now newly acquired by DNSFilter) provide protection against domains that attackers spin up only hours before their phishing campaigns. These services maintain threat feeds, classify suspicious and newly registered domains, and allow you to enforce policies that automatically block them. When combined with email filtering and endpoint protection, DNS filtering stops entire categories of attacks before they ever reach the user.

---

## In Closing
As phishing campaigns evolve, so must our defenses. Organizations that treat awareness training as a checkbox will continue to fall behind, while those that invest in modern identity controls, stronger detection, and real-world user education will stay resilient.  

My goal with this post is to break down these trends and help businesses understand what’s actually happening in the field.
