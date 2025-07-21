#!/usr/bin/env python3
import sys
import os
from collections import defaultdict

conteo = defaultdict(int)

for line in sys.stdin:
    try:
        user, val = line.strip().split('\t')
        conteo[user] += int(val)
    except:
        continue

total_accesos = sum(conteo.values())

os.makedirs("output_mapreduce", exist_ok=True)

with open("output_mapreduce/salida.out", "w", encoding="utf-8") as out:
    out.write(f"🔹 Consolidado final de accesos fuera de horario por usuario: {total_accesos} accesos\n")
    for user, total in conteo.items():
        out.write(f"{user} {total}\n")
