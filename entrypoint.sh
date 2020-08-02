#!/bin/bash
###
 # @Author: BobAnkh
 # @Github: https://github.com/BobAnkh
 # @Date: 2020-07-29 23:47:02
 # @LastEditors: BobAnkh
 # @LastEditTime: 2020-08-02 22:29:08
 # @FilePath: /auto-generate-changelog/entrypoint.sh
 # @Description: 
 # @Copyright 2020 BobAnkh
### 

set -e

python -m pip install --upgrade pip setuptools wheel
pip install -r /requirements.txt

python /main.py
