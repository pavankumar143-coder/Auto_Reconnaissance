import os
import subprocess
import requests
import json
from colorama import Fore, Style, init
import pyfiglet



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
