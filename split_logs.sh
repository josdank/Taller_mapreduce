#!/bin/bash
mkdir -p splits
split -l $(( $(wc -l < logs.txt) / 4 + 1 )) logs.txt splits/split_
