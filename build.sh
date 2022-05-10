#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo -e "\n${YELLOW}The following dependencies will be required to build and run A.D.A.M.S.${NC}\n"
echo -e "  APT Packages\n"
echo -e "    - python3"
echo -e "    - python-pip\n"
echo -e "  PIP Packages\n"
echo -e "    - pyinstaller"
echo -e "    - getch\n"

sudo apt update

echo -e "\n ${GREEN}[+]${NC} Installing APT Dependencies:" 
sudo apt install -y python3 python3-pip

echo -e "\n ${GREEN}[+]${NC} Installing Python Dependencies:"
pip install -U pyinstaller
pip install getch
export PATH=~/.local/bin:$PATH

echo -e "\n ${GREEN}[+]${NC} Building A.D.A.M.S. binary..."
pyinstaller --name adams --distpath ./ -F modules/main.py