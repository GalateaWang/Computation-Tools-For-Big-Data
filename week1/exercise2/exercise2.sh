#!/bin/bash
wget  https://www.dropbox.com/s/d5c4x905w4jelbu/cars.txt 0;
awk '$5 <= 10000 { print }' cars.txt > cheap_cars.txt
