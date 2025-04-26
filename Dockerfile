# 1. Usar una imagen base oficial de Python
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar los archivos necesarios al contenedor
COPY requirements.txt requirements.txt

# 4. Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código de la aplicación
COPY . .

# 6. Exponer el puerto en el que corre la aplicación
EXPOSE 8000

# 7. Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]