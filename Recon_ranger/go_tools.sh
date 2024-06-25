#!/bin/bash

# Set GO111MODULE environment variable
export GO111MODULE=on

# Install Go repositories
go get -u github.com/tomnomnom/assetfinder
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/LukaSikic/subzy@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install github.com/tomnomnom/waybackurls@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go get -u -v github.com/lc/subjs@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install github.com/jaeles-project/gospider@latest
go install github.com/tomnomnom/qsreplace@latest
go install github.com/hahwul/dalfox/v2@latest
go get -u github.com/tomnomnom/gf