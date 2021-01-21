#!/bin/bash

source ../../bin/modify_python_path.sh

python_path_append "../lib"

python3 prime_number_cli.py --number 5
