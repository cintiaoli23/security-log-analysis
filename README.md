# Security Log Analysis with Python

Project focused on analyzing security logs to identify suspicious authentication activity.

---

##  Objective

Analyze authentication logs to detect suspicious login behavior, such as repeated failed login attempts that may indicate brute-force attacks.

---

##  Tools Used

- Python 3
- Simulated Linux authentication logs

---

##  Project Overview

This project parses authentication log files and counts failed login attempts per IP address.  
IP addresses with **three or more failed attempts** are flagged as suspicious and highlighted for further investigation.

---

##  Key Learnings

- Understanding Linux authentication log structures
- Identifying common security events related to login failures
- Implementing basic detection logic for suspicious activity
- Applying Python for security log analysis
