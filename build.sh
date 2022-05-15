#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[94m'
NC='\033[0m'

echo -e "\n${YELLOW}The following dependencies will be required to build and run A.D.A.M.S.${NC}\n"
echo -e " ${GREEN}-- APT Packages --${NC}"
echo -e "\tpython3"
echo -e "\tpython-pip\n"
echo -e " ${GREEN}-- PIP Packages --${NC}"
echo -e "\tpyinstaller"
echo -e "\tgetch\n"

echo -e "\n ${GREEN}[+]${NC} Updating APT Repositories..." 
sudo apt update

echo -e "\n ${GREEN}[+]${NC} Installing APT Dependencies:" 
sudo apt install -y python3 python3-pip

echo -e "\n ${GREEN}[+]${NC} Installing Python Dependencies:"
pip install -U pyinstaller
pip install getch
export PATH=~/.local/bin:$PATH

echo -e "\n ${GREEN}[+]${NC} Building A.D.A.M.S. binary..."
pyinstaller --clean --name adams --distpath ./ -F modules/main.py

if [ "$1" == "--run" ] || [ "$1" == "-r" ]; then
    ./adams
elif [ "$1" == "--installer" ] || [ "$1" == "-i" ]; then
    python3 modules/installer.py
elif [ "$1" == "--manager" ] || [ "$1" == "-m" ]; then
    python3 modules/manager.py
fi