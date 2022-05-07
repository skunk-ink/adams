#!/bin/bash

sudo apt -qqq install python3-pip
pip -q install -U pyinstaller
pip -q install getch
export PATH=~/.local/bin:$PATH

pyinstaller --name adams --distpath ./ -F modules/main.py