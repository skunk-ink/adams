#!/bin/bash

echo "Installing APT Dependencies: python3, python-pip"
sudo apt -qqq install -y python3 python3-pip
sleep 1

echo "Installing Python Dependencies: pyinstaller, getch"
pip install -qq -U pyinstaller
pip install -qq  getch
export PATH=~/.local/bin:$PATH
sleep 1

echo "Building A.D.A.M.S. binary..."
pyinstaller --name adams --distpath ./ -F modules/main.py
sleep 1