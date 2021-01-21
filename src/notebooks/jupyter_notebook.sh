#!/bin/bash

source ../../bin/modify_python_path.sh

python_path_append "../lib" "../apps"

"$HOME"/opt/anaconda3/bin/jupyter notebook .
