# Auto_Reconnaissance
The automated script designed for comprehensive security assessments and reconnaissance of web domains. This tool leverages multiple powerful security tools to find and enumerate subdomains, check for live hosts, identify open ports, discover hidden directories, and test for various vulnerabilities including XSS, LFI, open redirections, and more.

Here's how the script works:

The script takes a target website as an argument.
1)It creates acreates a directory for the output files with the target as the name.
2)The subdomain_enum method uses subfinder, assetfinder, and findomain to discover subdomains.
3)The live_subdomains method uses httpx to identify live subdomains.
4)The subdomain_takeover method uses subzy to check for potential subdomain takeovers.
5)The open_ports method uses naabu to find open ports.
6)The json_files_discovery method uses waybackurls to search for JSON files in the web archive.
7)The js_vulnerabilities method uses katana, subjs, httpx, and nuclei to identify potential vulnerabilities in JavaScript files.
8)The dir_enum method uses dirsearch to discover hidden directories.
9)The injection_vulnerabilities method uses gospider, qsreplace, and dalfox to find injection vulnerabilities like LFI, CRLF, SQLi, and more.
10)The xss_vulnerabilities method uses gospider, qsreplace, and dalfox to detect XSS vulnerabilities.
11)The open_redirection method uses uro to identify open redirection vulnerabilities.
12)The comprehensive_vulnerability_scanning method uses nuclei for detailed scanning of live subdomains.
13)The run_recon method runs all the reconnaissance methods in sequence.

Usage:

Clone the repository: git clone https://github.com/pavankumar143-coder/Auto_Reconnaissance.git
Change into the repository directory: cd Auto_Reconnaissance/Recon_ranger
pip install -r requirements.txt
chmod +x go_tools.sh
./go_tools.sh
Run the script: python recon_ranger.py <target_website>

Replace <target_website> with the website you want to scan.

Note:

This script is for educational purposes only and should not be used without permission from the target website's owner. Always respect the website's terms of service and robots.txt file.
