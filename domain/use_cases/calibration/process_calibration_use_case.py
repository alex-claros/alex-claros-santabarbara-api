from abc import ABC, abstractmethod
from domain.models.calibration_model import Calibration

class ProcessCalibrationUseCase(ABC):
    @abstractmethod
    def execute(self, image_content: bytes, expected_rgb: dict) -> Calibration:
        pass