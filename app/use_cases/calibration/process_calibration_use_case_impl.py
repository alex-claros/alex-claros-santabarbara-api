from PIL import Image
import numpy as np
from domain.use_cases.calibration.process_calibration_use_case import ProcessCalibrationUseCase
from domain.models.calibration_model import Calibration
from domain.repositories.calibration_repository import CalibrationRepository
from core.minio_client import MinioClient
from uuid import uuid4
from datetime import datetime
import cv2

def calculate_color_deviation(reference_rgb: dict, detected_rgb: dict):
    """
    Calcula la desviación entre dos colores usando distancia euclidiana.
    Puedes usar Delta-E para precisión profesional más adelante.
    """
    ref = np.array([reference_rgb["r"], reference_rgb["g"], reference_rgb["b"]])
    det = np.array([detected_rgb["r"], detected_rgb["g"], detected_rgb["b"]])
    return float(np.linalg.norm(ref - det))

def average_color(image_bytes: bytes):
    """
    Detecta el color promedio en la imagen (idealmente una superficie plana de referencia).
    """
    image = Image.open(image_bytes).convert("RGB")
    img_array = np.array(image)
    avg_color = {
        "r": int(img_array[:, :, 0].mean()),
        "g": int(img_array[:, :, 1].mean()),
        "b": int(img_array[:, :, 2].mean())
    }
    return avg_color

class ProcessCalibrationUseCaseImpl(ProcessCalibrationUseCase):
    def __init__(self, repository: CalibrationRepository):
        self.repository = repository
        self.minio_client = MinioClient()

    def execute(self, image_content: bytes, expected_rgb: dict) -> Calibration:
        image_url = self.minio_client.upload_image(image_content)

        # Detectamos el color promedio de la imagen
        detected_color = average_color(image_content)

        # Calculamos la desviación
        deviation = calculate_color_deviation(expected_rgb, detected_color)

        # Determinamos estado según umbral
        status = "success" if deviation < 15 else "needs_adjustment"

        # Guardamos resultado
        calibration = Calibration(
            id=str(uuid4()),
            reference_color=expected_rgb,
            detected_color=detected_color,
            deviation=deviation,
            image_url=image_url,
            status=status,
            timestamp=datetime.now()
        )

        self.repository.save(calibration)

        return calibration