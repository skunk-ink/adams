#!/bin/bash

YELLOW='\033[0;33m'
NC='\033[0m'

echo -e "${YELLOW}[+]${NC} Installing APT Dependencies: python3, python-pip"
sleep 1
sudo apt install -y python3 python3-pip

echo -e "${YELLOW}Installing Python Dependencies: pyinstaller, getch${NC}"
sleep 1
pip install -U pyinstaller
pip install getch
export PATH=~/.local/bin:$PATH

echo -e "${YELLOW}[+]${NC} Building A.D.A.M.S. binary..."
sleep 1
pyinstaller --name adams --distpath ./ -F modules/main.py