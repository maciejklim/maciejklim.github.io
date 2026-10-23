---
title: '{{ replaceRE `^\d{4}-\d{2}-\d{2}-` "" .File.ContentBaseName | replaceRE "-" " " | title }}'
date: {{ .Date | time.Format "2006-01-02" }}
summary: ""
# One category per post. It picks the thumbnail automatically:
#   Incident Response | Digital Forensics | Identity and Access | Mitigation | Industry Trends
categories: ["Digital Forensics"]
tags: []
slug: ""
draft: true
---

## TL;DR

## Scenario

## Investigation

## Findings

## Detection and Hardening

## Identity Angle

## Key Takeaways
