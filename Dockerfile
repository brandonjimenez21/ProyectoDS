# Usamos una imagen oficial de Python
FROM python:3.10

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app/backend

# Copiamos los archivos del proyecto al contenedor
COPY . /app

# Instalamos dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exponemos el puerto 8000
EXPOSE 8000

# Comando por defecto para ejecutar Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
