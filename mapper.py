#!/usr/bin/env python3
import sys
import os
from datetime import datetime

# Preparar variables
fuera_conteo = 0
dentro_conteo = 0
fuera_lineas = []
dentro_lineas = []

# Leer y procesar líneas
for line in sys.stdin:
    try:
        line = line.strip()
        if not line:
            continue

        partes = line.split()
        if len(partes) != 3:
            continue

        fecha, hora, usuario_raw = partes
        hora_dt = datetime.strptime(hora, "%H:%M:%S").time()
        usuario = usuario_raw.split(":")[1] if usuario_raw.startswith("usuario:") else "desconocido"

        if hora_dt < datetime.strptime("08:00:00", "%H:%M:%S").time() or hora_dt > datetime.strptime("18:00:00", "%H:%M:%S").time():
            fuera_lineas.append(f"{fecha} {hora} usuario:{usuario}")
            print(f"{usuario}\t1")
            fuera_conteo += 1
        else:
            dentro_lineas.append(f"{fecha} {hora} usuario:{usuario}")
            dentro_conteo += 1
    except:
        continue

# Crear carpetas
os.makedirs("output_usuarios", exist_ok=True)

# Escribir archivos con encabezado
with open("output_usuarios/usuarios_fuera_horario.txt", "w", encoding="utf-8") as f:
    f.write(f"🔹 Usuarios FUERA del horario laboral: {fuera_conteo} accesos\n")
    f.write("\n".join(fuera_lineas))

with open("output_usuarios/usuarios_dentro_horario.txt", "w", encoding="utf-8") as f:
    f.write(f"🔹 Usuarios DENTRO del horario laboral: {dentro_conteo} accesos\n")
    f.write("\n".join(dentro_lineas))
