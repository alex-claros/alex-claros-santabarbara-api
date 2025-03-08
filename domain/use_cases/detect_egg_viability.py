import cv2
import json
from infrastructure.recognition.recognition import EggRecognitionModule
from infrastructure.persistence.db import insert_result
from core.config import MODEL_PATH, CONF_THRESHOLD

def detect_egg_viability(image_path: str) -> dict:
    """
    Caso de uso para detectar la viabilidad de un huevo a partir de una imagen.
    Lee la imagen, ejecuta el reconocimiento y almacena el resultado en la base de datos.
    
    Retorna:
        dict: Conteniendo el número de huevos detectados y los detalles de cada detección.
    """
    recognition_module = EggRecognitionModule(model_path=MODEL_PATH, conf_threshold=CONF_THRESHOLD)
    
    image = cv2.imread(image_path)
    if image is None:
        raise Exception(f"No se pudo cargar la imagen en {image_path}")
    
    # Realizar la detección de huevos
    count, detections = recognition_module.detect_eggs(image)
    
    # Construir el diccionario de resultados
    result = {
        "eggs_detected": count,
        "detections": [
            {"x1": int(d[0]), "y1": int(d[1]), "x2": int(d[2]), "y2": int(d[3]), "confidence": float(d[4])}
            for d in detections
        ]
    }
    
    insert_result(count, json.dumps(result["detections"]))
    
    return result
