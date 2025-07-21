#!/usr/bin/env python3
import sys
import os
from datetime import datetime

# Asegurar que los directorios existen
os.makedirs("output_usuarios", exist_ok=True)

fuera = open("output_usuarios/usuarios_fuera_horario.txt", "a")
dentro = open("output_usuarios/usuarios_dentro_horario.txt", "a")

for line in sys.stdin:
    try:
        line = line.strip()
        if not line:
            continue

        partes = line.split()

        # Verifica que tenga 3 partes
        if len(partes) != 3:
            print(f"Línea inválida: {line}", file=sys.stderr)
            continue

        fecha, hora, usuario_raw = partes

        # Formato de hora correcto
        hora_dt = datetime.strptime(hora, "%H:%M:%S").time()

        # Extraer el nombre del usuario
        if not usuario_raw.startswith("usuario:"):
            print(f"Formato de usuario inválido: {line}", file=sys.stderr)
            continue

        usuario = usuario_raw.split(":")[1]

        # Clasificar horario
        inicio = datetime.strptime("08:00:00", "%H:%M:%S").time()
        fin = datetime.strptime("18:00:00", "%H:%M:%S").time()

        if hora_dt < inicio or hora_dt > fin:
            fuera.write(f"{fecha} {hora} usuario:{usuario}\n")
            print(f"{usuario}\t1")
        else:
            dentro.write(f"{fecha} {hora} usuario:{usuario}\n")

    except Exception as e:
        print(f"Error procesando línea: {line} - {e}", file=sys.stderr)

fuera.close()
dentro.close()
