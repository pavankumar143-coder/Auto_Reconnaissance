#!/bin/bash

# Set GOBIN and GOPATH environment variables
export GOBIN=/root/go/bin
export GOPATH=/root/go
export PATH=$GOBIN:$PATH

# Create Go directory and navigate to it
mkdir -p $GOPATH
cd $GOPATH

# Clone and install each repository
repos=(
    "https://github.com/tomnomnom/assetfinder.git"
    "https://github.com/Findomain/Findomain.git"
    "https://github.com/projectdiscovery/httpx.git"
    "https://github.com/PentestPad/subzy.git"
    "https://github.com/projectdiscovery/naabu.git"
    "https://github.com/tomnomnom/waybackurls.git"
    "https://github.com/projectdiscovery/katana.git"
    "https://github.com/lc/subjs.git"
    "https://github.com/projectdiscovery/nuclei.git"
    "https://github.com/maurosoria/dirsearch.git"
    "https://github.com/jaeles-project/gospider.git"
    "https://github.com/tomnomnom/qsreplace.git"
    "https://github.com/hahwul/dalfox.git"
    "https://github.com/s0md3v/uro.git"
    "https://github.com/tomnomnom/gf.git"
)

for repo in "${repos[@]}"; do
    repo_name=$(basename "$repo" | cut -d '.' -f1)
    git clone "$repo"
    cd "$repo_name"
    go build .
    go install .
    cd ..
done

# Add Go bin to PATH in /root/.zshrc
echo "export PATH=$GOBIN:$PATH" >> /root/.zshrc
