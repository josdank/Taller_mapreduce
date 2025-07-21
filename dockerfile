# Imagen base con Python 3.9

FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . /app


# Comando por defecto al iniciar el contenedor
CMD ["bash"]