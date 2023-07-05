# Imagen base de Python
FROM python:3.11.4-slim-bullseye

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instalar los requerimientos de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación al contenedor
COPY . .

EXPOSE 8001

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]
