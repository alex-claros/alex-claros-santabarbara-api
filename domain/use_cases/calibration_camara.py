from typing import List
from infrastructure.camera.camera_calibration import ColorCalibrationAdapter
from infrastructure.entities.calibration import ColorCalibrationParameters
import cv2
import numpy as np

class CalibrateColorUseCase:
    def __init__(self, calibration_adapter: ColorCalibrationAdapter):
        self.calibration_adapter = calibration_adapter

    def execute(self, images: List[np.ndarray], params: ColorCalibrationParameters) -> List[np.ndarray]:
        calibrated_images = []
        for image in images:
            calibrated_image = self.calibration_adapter.apply_calibration(image, params)
            calibrated_images.append(calibrated_image)
        return calibrated_images