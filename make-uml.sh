#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[94m'
NC='\033[0m'

echo -e "\n${YELLOW}The following dependencies will be required to build and run A.D.A.M.S.${NC}\n"
echo -e " ${GREEN}-- APT Packages --${NC}"
echo -e "\tgraphviz\n"
echo -e " ${GREEN}-- PIP Packages --${NC}"
echo -e "\tpylint\n"

echo -e "\n ${GREEN}[+]${NC} Updating APT Repositories..." 
sudo apt update

echo -e "\n ${GREEN}[+]${NC} Installing APT Dependencies:" 
sudo apt install -y graphviz

echo -e "\n ${GREEN}[+]${NC} Installing Python Dependencies:"
sudo pip install pylint

DIR="./uml-diagrams"

if [ -d $DIR ];
then
    echo -e "\n ${YELLOW}[!]${NC} Directory '$DIR' found."
    cd $DIR
else
    echo -e "\n ${GREEN}[+]${NC} Creating directory '$DIR'."
    mkdir $DIR
    cd $DIR
fi

echo -e "\n ${GREEN}[+]${NC} Generating diagram '$DIR/classes_main.py'."
pyreverse -o png -p main ../modules/main.py

echo -e "\n ${GREEN}[+]${NC} Generating diagram '$DIR/classes_installer.py'."
pyreverse -o png -p installer ../modules/installer.py

echo -e "\n ${GREEN}[+]${NC} Generating diagram '$DIR/classes_manager.py'."
pyreverse -o png -p manager ../modules/manager.py