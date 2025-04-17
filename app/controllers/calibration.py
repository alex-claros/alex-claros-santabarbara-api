from fastapi import APIRouter, UploadFile, File
from typing import List
from domain.use_cases.calibration_camara import CalibrateColorUseCase
from infrastructure.camera.camera_calibration import ColorCalibrationAdapter
from infrastructure.entities.calibration import ColorCalibrationParameters
import cv2
import numpy as np

router = APIRouter()

@router.post("/calibrate-color")
async def calibrate_color(
    files: List[UploadFile] = File(...),
    white_balance: float = 1.0,
    gamma_correction: float = 1.0,
    histogram_equalization: bool = False
):
    # Leer imágenes desde los archivos subidos
    images = [cv2.imdecode(np.frombuffer(await file.read(), np.uint8), cv2.IMREAD_COLOR) for file in files]

    # Configurar parámetros de calibración
    params = ColorCalibrationParameters(
        white_balance=white_balance,
        gamma_correction=gamma_correction,
        histogram_equalization=histogram_equalization
    )

    # Configurar el caso de uso y el adaptador
    adapter = ColorCalibrationAdapter()
    use_case = CalibrateColorUseCase(adapter)

    # Aplicar la calibración de color
    calibrated_images = use_case.execute(images, params)

    # Devolver respuesta
    return {"message": "Calibración de color aplicada", "image_count": len(calibrated_images)}