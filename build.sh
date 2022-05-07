#!/bin/bash

sudo apt install python3-pip
pip install -U pyinstaller

pyinstaller --name adams --distpath ./ -F modules/main.py