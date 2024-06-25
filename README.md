# Auto_Reconnaissance
The automated script designed for comprehensive security assessments and reconnaissance of web domains. This tool leverages multiple powerful security tools to find and enumerate subdomains, check for live hosts, identify open ports, discover hidden directories, and test for various vulnerabilities including XSS, LFI, open redirections, and more.

Here's how the script works:

The script takes a target website as an argument. <br>
1)It creates acreates a directory for the output files with the target as the name. <br>
2)The subdomain_enum method uses subfinder, assetfinder, and findomain to discover subdomains. <br>
3)The live_subdomains method uses httpx to identify live subdomains. <br>
4)The subdomain_takeover method uses subzy to check for potential subdomain takeovers. <br>
5)The open_ports method uses naabu to find open ports. <br>
6)The json_files_discovery method uses waybackurls to search for JSON files in the web archive. <br>
7)The js_vulnerabilities method uses katana, subjs, httpx, and nuclei to identify potential vulnerabilities in JavaScript files. <br>
8)The dir_enum method uses dirsearch to discover hidden directories. <br>
9)The injection_vulnerabilities method uses gospider, qsreplace, and dalfox to find injection vulnerabilities like LFI, CRLF, SQLi, and more. <br>
10)The xss_vulnerabilities method uses gospider, qsreplace, and dalfox to detect XSS vulnerabilities. <br>
11)The open_redirection method uses uro to identify open redirection vulnerabilities. <br>
12)The comprehensive_vulnerability_scanning method uses nuclei for detailed scanning of live subdomains. <br>
13)The run_recon method runs all the reconnaissance methods in sequence. <br>

Usage: <br>
Open the Kali Terminal Type this command:sudo su <br>
install naabu : apt install naabu <br>
Clone the repository: git clone https://github.com/pavankumar143-coder/Auto_Reconnaissance.git <br>
Change into the repository directory: cd Auto_Reconnaissance/Recon_ranger <br>
pip install -r requirements.txt <br>
chmod +x go_tools.sh <br>
./go_tools.sh <br>
Run the script: python recon_ranger.py <target_website> <br>

Replace <target_website> with the website you want to scan. <br>

Note: <br>

This script is for educational purposes only and should not be used without permission from the target website's owner. Always respect the website's terms of service and robots.txt file. <br>
