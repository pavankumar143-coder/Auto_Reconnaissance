import os
import subprocess
import requests
import json
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init()

# Define the text
main_title = "AUTOMATED_RECON"
sub_title = "                Created By Pavan Kumar Tule"

# Use pyfiglet to create the large text
main_title_fig = pyfiglet.figlet_format(main_title)
sub_title_fig = pyfiglet.figlet_format(sub_title)

# Print the text with green color
print(f"{Fore.GREEN}{main_title_fig}{Style.RESET_ALL}")
print(f"{Fore.GREEN}{sub_title_fig}{Style.RESET_ALL}")

# Keep the script running so the text remains visible
#input("Press Enter to exit...")

class ReconRanger:
    def __init__(self, target):
        self.target = target
        self.output_dir = f"recon_results/{target}"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    #Subdomain Enumeration
    def subdomain_enum(self):
        print("Performing Subdomain Enumeration...")
        subprocess.run(f"subfinder -d {self.target} -o {self.output_dir}/subdomains.txt", shell=True)
        subprocess.run(f"assetfinder -d {self.target} -o {self.output_dir}/assetfinder.txt", shell=True)
        subprocess.run(f"findomain -t {self.target} -o {self.output_dir}/findomain.txt", shell=True)

    #Live Subdomains
    def live_subdomains(self):
        print("Identifying Live Subdomains...")
        subprocess.run(f"httpx -l -o {self.output_dir}/live_subdomains.txt {self.output_dir}/subdomains.txt", shell=True)

    #Subdomain Takeovers
    def subdomain_takeover(self):
        print("Checking for Subdomain Takeovers...")
        subprocess.run(f"subzy -d {self.target} -o {self.output_dir}/subdomain_takeover.txt", shell=True)

    #Finding Open Ports
    def open_ports(self):
        print("Finding Open Ports...")
        subprocess.run(f"naabu -host {self.target} -o {self.output_dir}/open_ports.txt", shell=True)

