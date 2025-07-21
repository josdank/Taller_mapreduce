#!/bin/bash
mkdir -p splits
split -l $(( $(wc -l < logs.txt) / 4 + 1 )) logs.txt splits/split_
chmod +x split_logs.sh
./split_logs.sh
