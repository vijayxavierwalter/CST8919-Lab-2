# CST8919 Lab 2 - Azure Monitoring and Alerting

## YouTube video demo

https://youtu.be/mqREpxEZPp8

## Overview

In this lab, I deployed a Python Flask application to Azure App Service and configured Azure Monitor to collect application logs. I used Log Analytics and KQL queries to detect failed login attempts and created an alert rule to identify potential brute-force attacks.

## KQL Query

```kusto
AppServiceConsoleLogs
| where ResultDescription contains "LOGIN_FAILED"
| summarize FailedAttempts=count() by bin(TimeGenerated, 5m)
| where FailedAttempts >= 5
```

### Explanation

* Filters failed login attempts.
* Counts failed login events within a 5-minute period.
* Returns results when 5 or more failed attempts are detected.

## What I Learned

* How to deploy a Flask application to Azure App Service.
* How to configure Diagnostic Settings and Log Analytics.
* How to use KQL to analyze application logs.
* How to create Azure Monitor Alert Rules and Action Groups.

## Challenges Faced

* Troubleshooting Azure App Service deployment issues.
* Configuring log collection and diagnostic settings.
* Understanding Azure Monitor alert configuration.

## Real-World Improvements

In a production environment, I would:

* Track failed logins by username and source IP address.
* Implement account lockout policies.
* Integrate alerts with Microsoft Sentinel.
* Use threat intelligence and geolocation analysis for improved detection.


## Author

Vijay Xavier Walter
