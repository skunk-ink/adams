#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "\n ${GREEN}[+] Updating APT Repositories..."
sleep 1
sudo apt update

echo -e "\n ${GREEN}[+] Installing APT Dependencies:${NC} python3, python-pip"
sleep 1
sudo apt install -y python3 python3-pip

echo -e "\n ${GREEN}[+] Installing Python Dependencies:${NC} pyinstaller, getch"
sleep 1
pip install -U pyinstaller
pip install getch
export PATH=~/.local/bin:$PATH

echo -e "\n ${GREEN}[+] Building A.D.A.M.S. binary...${NC}"
sleep 1
pyinstaller --name adams --distpath ./ -F modules/main.py