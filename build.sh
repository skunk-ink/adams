#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}[+]${NC} Installing APT Dependencies: python3, python-pip"
sudo apt -qqq install -y python3 python3-pip
sleep 1

echo -e "${GREEN}[+]${NC} Installing Python Dependencies: pyinstaller, getch"
pip install -qq -U pyinstaller
pip install -qq getch
export PATH=~/.local/bin:$PATH
sleep 1

echo -e "${GREEN}[+]${NC} Building A.D.A.M.S. binary..."
pyinstaller --name adams --distpath ./ -F modules/main.py
sleep 1