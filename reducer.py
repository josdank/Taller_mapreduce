#!/usr/bin/env python3
import sys
import os
from collections import defaultdict

# Crear carpeta si no existe
os.makedirs("output_mapreduce", exist_ok=True)

conteo = defaultdict(int)

for line in sys.stdin:
    try:
        user, val = line.strip().split('\t')
        conteo[user] += int(val)
    except:
        continue

with open("output_mapreduce/salida.out", "w") as out:
    for user, total in conteo.items():
        print(f"{user} {total}")
        out.write(f"{user} {total}\n")
