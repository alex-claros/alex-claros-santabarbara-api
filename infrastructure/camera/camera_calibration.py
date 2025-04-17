from typing import List
import cv2
import numpy as np
from infrastructure.entities.calibration import ColorCalibrationParameters

class ColorCalibrationAdapter:
    def apply_calibration(self, image: np.ndarray, params: ColorCalibrationParameters) -> np.ndarray:
        # Aplicar balance de blancos
        if params.white_balance != 1.0:
            result = cv2.xphoto.createSimpleWB().balanceWhite(image)
        else:
            result = image

        # Aplicar corrección gamma
        if params.gamma_correction != 1.0:
            inv_gamma = 1.0 / params.gamma_correction
            table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
            result = cv2.LUT(result, table)

        if params.histogram_equalization:
            ycrcb = cv2.cvtColor(result, cv2.COLOR_BGR2YCrCb)
            channels = cv2.split(ycrcb)
            channels[0] = cv2.equalizeHist(channels[0])
            result = cv2.merge(channels)
            result = cv2.cvtColor(result, cv2.COLOR_YCrCb2BGR)

        return result