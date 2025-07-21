#!/usr/bin/env python3
import sys
import os
from datetime import datetime

# Crear carpeta si no existe
os.makedirs("output_usuarios", exist_ok=True)

fuera = open("output_usuarios/usuarios_fuera_horario.txt", "a")
dentro = open("output_usuarios/usuarios_dentro_horario.txt", "a")

for line in sys.stdin:
    try:
        date, time, user_tag = line.strip().split()
        user = user_tag.split(":")[1] if ":" in user_tag else "desconocido"
        time_obj = datetime.strptime(time, "%H:%M:%S").time()

        if time_obj < datetime.strptime("08:00:00", "%H:%M:%S").time() or time_obj > datetime.strptime("18:00:00", "%H:%M:%S").time():
            fuera.write(f"{date} {time} usuario:{user}\n")
            print(f"{user}\t1")  # salida estándar va a mapX.txt
        else:
            dentro.write(f"{date} {time} usuario:{user}\n")
    except:
        continue

fuera.close()
dentro.close()
