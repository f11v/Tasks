FROM python:3.9-alpine

# Configura el directorio de trabajo
WORKDIR /app

# Copia las dependencias y el archivo requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    apk del gcc musl-dev
RUN pip install --upgrade pip

# Copia los archivos de la aplicación
COPY . .

# Ejecuta el microservicio con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]