#!/bin/bash

sudo apt install python3-pip
pip install -U pyinstaller
pip install getch
export PATH=~/.local/bin:$PATH

pyinstaller --name adams --distpath ./ -F modules/main.py