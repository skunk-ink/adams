#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

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
pyreverse -o png main ../modules/main.py

echo -e "\n ${GREEN}[+]${NC} Generating diagram '$DIR/classes_installer.py'."
pyreverse -o png installer ../modules/installer.py

echo -e "\n ${GREEN}[+]${NC} Generating diagram '$DIR/classes_manager.py'."
pyreverse -o png manager ../modules/manager.py

echo -e "\n ${GREEN}[+]${NC} Generating diagram '$DIR/classes_splash.py'."
pyreverse -o png splash ../modules/splash.py

echo -e "\n ${GREEN}[+]${NC} Generating diagram '$DIR/classes_colours.py'."
pyreverse -o png colours ../modules/colours.py