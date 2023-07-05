# Imagen base de Python
FROM python:3.11.4-slim-bullseye

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el código fuente de la aplicación al contenedor
COPY . .

# Instalar los requerimientos de Python
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]