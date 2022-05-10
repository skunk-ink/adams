#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}[+]${NC} Installing APT Dependencies: python3, python-pip"
sleep 1
sudo apt install -y python3 python3-pip

echo -e "${GREEN}[+]${NC} Installing Python Dependencies: pyinstaller, getch"
sleep 1
pip install -U pyinstaller
pip install getch
export PATH=~/.local/bin:$PATH

echo -e "${GREEN}[+]${NC} Building A.D.A.M.S. binary..."
sleep 1
pyinstaller --name adams --distpath ./ -F modules/main.py