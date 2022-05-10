#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo -e "\n${YELLOW}A.D.A.M.S will require the following in order to run.${NC}\n"
echo -e "\n  ${RED}APT Packages\n"
echo -e "    ${GREEN}python3\n"
echo -e "    ${GREEN}python-pip\n"
echo -e "\n  ${RED}PIP Packages\n"
echo -e "    ${GREEN}pyinstaller\n"
echo -e "    ${GREEN}getch\n"

echo "\n Password requred to begin build process.\n"
sudo apt update

echo -e "\n ${GREEN}[+]${NC} Installing APT Dependencies:" 
sudo apt install -y python3 python3-pip

echo -e "\n ${GREEN}[+]${NC} Installing Python Dependencies:"
pip install -U pyinstaller
pip install getch
export PATH=~/.local/bin:$PATH

echo -e "\n ${GREEN}[+]${NC} Building A.D.A.M.S. binary..."
pyinstaller --name adams --distpath ./ -F modules/main.py