#!/bin/bash

echo "Installing Dependencies... Please wait."
sudo apt -qqq install -y python3 python3-pip
pip install -qq -U pyinstaller
pip install -qq  getch
export PATH=~/.local/bin:$PATH

pyinstaller --name adams --distpath ./ -F modules/main.py