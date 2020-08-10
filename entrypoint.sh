#!/bin/bash
###
 # @Author: BobAnkh
 # @Github: https://github.com/BobAnkh
 # @Date: 2020-07-29 23:47:02
 # @LastEditors  : BobAnkh
 # @LastEditTime : 2020-08-10 15:59:48
 # @FilePath     : /auto-generate-changelog/entrypoint.sh
 # @Description: Entrypoint of Github Action
 # @Copyright 2020 BobAnkh
### 

set -e

python -m pip install --upgrade pip setuptools wheel
pip install -r /requirements.txt

python /main.py
