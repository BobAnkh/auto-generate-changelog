#!/bin/bash
set -e
sudo apt install -y git
python -m pip install --upgrade pip setuptools wheel
pip install -r /requirements.txt

python /main.py
