#!/bin/bash
wget https://www.dropbox.com/s/85fbd4l8s52f7to/dict;
cat $1 | tr 'A-Z' 'a-z' | \
tr -cs 'a-zA-Z0-9' '[\n*]' | sort | uniq > input1.txt
comm -13 <(cat dict | tr 'A-Z' 'a-z' | sort ) input1.txt > input2.txt
cat input2.txt
wc -w input2.txt

rm input1.txt input2.txt dict
