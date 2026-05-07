------------------------------
Auto_Reconnaissance
Auto_Reconnaissance is a powerful automated script designed for comprehensive security assessments and web domain reconnaissance. It integrates industry-standard security tools into a single workflow to help bug hunters and security researchers identify vulnerabilities and infrastructure protections efficiently.
------------------------------
Key Features
This tool leverages a suite of powerful security utilities to perform:
WAF Detection: Automatically identifies if a target is protected by a Web Application Firewall.
Subdomain Discovery: Enumeration using subfinder, assetfinder, and findomain.
Live Host Probing: Identifying active subdomains via httpx.
Vulnerability Scanning: Detecting XSS, LFI, SQLi, and Open Redirections.
Asset Analysis: Finding open ports, hidden directories, and sensitive JSON files.
JS Analysis: Hunting for vulnerabilities in JavaScript files using nuclei and katana.
------------------------------
How It Works
The script follows a structured reconnaissance pipeline:

1)Subdomain Enum (subfinder, assetfinder, findomain): Discovers all possible subdomains.Live 
2)Check (httpx): Filters for active hosts and detects WAF.Takeover Check 
3)(subzy): Checks for potential subdomain takeovers.
4)Port Scanning (naabu): Identifies open ports on target hosts.Archive 
5)Search (waybackurls): Discovers JSON files from web archives.JS Inspection 
6)(katana, subjs, nuclei): Scans JS files for security flaws.Directory Brute 
7)(dirsearch): Finds hidden files and directories.Injections (gospider, qsreplace, dalfox): Tests for LFI, CRLF, and SQLi.XSS and Redirect 
8)(dalfox, uro): Specifically targets XSS and Open Redirections.Full Scan 
9)(nuclei): Comprehensive vulnerability scan on live targets.
------------------------------
Installation & Setup
Ensure you are using Kali Linux for the best compatibility.

   1. Prerequisites

sudo su
apt install naabu -y


   1. Clone & Install

git clone https://github.com
cd Auto_Reconnaissance/Recon_ranger
pip install -r requirements.txt


   1. Permissions & Tool Setup

chmod +x go_tools.sh
./go_tools.sh

------------------------------
Usage
To start a scan, run the following command:

python recon_ranger.py <target_website>

Replace <target_website> with your target domain (e.g., example.com).
------------------------------
Disclaimer
Important: This script is for educational purposes only. Do not use it on targets without explicit, written permission from the owner. Always adhere to the website's Terms of Service and robots.txt guidelines.
------------------------------

