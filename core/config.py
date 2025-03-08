import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde un archivo .env, si existe

DATABASE_URL = os.getenv("DATABASE_URL", "database.db")
MODEL_PATH = os.getenv("MODEL_PATH", "yolov7_egg.pt")
CONF_THRESHOLD = float(os.getenv("CONF_THRESHOLD", 0.5))
