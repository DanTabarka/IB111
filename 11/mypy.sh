#!/bin/bash

for file in p*.py
do
    echo "I'm running: mypy --strict $file"
    echo "________________________________________________________________________________"
    mypy --strict "$file"
    echo ""
done
