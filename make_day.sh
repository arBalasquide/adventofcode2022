#!/bin/bash

# Script to generate a template folder for a day's challenge. It also pulls in your specific input file
# if you're logged in through firefox and saves the prompt to a readable txt file.

DAY=$1
URL="https://adventofcode.com"
INPUT_URL="$URL/2022/day/$DAY/input"

mkdir "day$DAY"

cp template.py "day$DAY/main.py"
chmod +x "day$DAY/main.py"

# get cookies from firefox sql db
# 3rd party script
chmod +x "cookies.sh"
./cookies.sh | grep -i "adventofcode" > cookies.txt

# can probably just pipe wget output directly to html2text but 2lazy4me
wget "$URL/2022/day/$DAY" -O "tmp.txt"
html2text "tmp.txt" > "day$DAY/prompt.txt"
rm -f "tmp.txt"

wget --load-cookies cookies.txt "$INPUT_URL" -O "day$DAY/input.txt"
