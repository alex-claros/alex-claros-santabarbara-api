# alex-claros-santabarbara-api
API del aplicativo web santabarbara

# Crear y Activar el Entorno Virtual

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto.
Crear el entorno virtual:

python3 -m venv venv

    Nota: Si obtienes el error "ensurepip is not available", instala el paquete python3-venv en tu sistema. Por ejemplo, en Ubuntu:

    sudo apt install python3.10-venv

Activar el entorno virtual:

    En Linux/macOS:

source venv/bin/activate

En Windows:

    .\venv\Scripts\activate

# Instalar las Dependencias

Con el entorno virtual activado, instala las dependencias listadas en el archivo requirements.txt:

pip install -r requirements.txt

# Ejecutar el Servidor

Una vez instaladas las dependencias, inicia el servidor FastAPI con el siguiente comando:

uvicorn app.main:app --reload

Luego, abre tu navegador y accede a http://127.0.0.1:8000/docs para ver la documentación interactiva generada por FastAPI.


Este texto explica de forma detallada cómo clonar el repositorio, configurar el entorno v
