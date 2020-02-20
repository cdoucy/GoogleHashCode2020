#!/usr/bin/bash

for file in ./sample/*.txt
do
    python3 src/parser.py $file > "${file}.out"
done