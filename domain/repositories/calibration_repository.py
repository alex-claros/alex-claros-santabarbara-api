from abc import ABC, abstractmethod
from typing import List
from domain.models.calibration_model import Calibration

class CalibrationRepository(ABC):
    @abstractmethod
    def save(self, calibration: Calibration):
        pass

    @abstractmethod
    def get_all(self) -> List[Calibration]:
        pass

    @abstractmethod
    def find_by_status(self, status: str) -> List[Calibration]:
        pass