#!/usr/bin/env bash

command="python3 run_python_script.py pipeline"

./run_tests.sh

echo "$command"
eval "$command"
