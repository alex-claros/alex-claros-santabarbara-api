from app.use_cases.calibration.process_calibration_use_case_impl import ProcessCalibrationUseCaseImpl
from infrastructure.persistence.repositories.calibration_repository_impl import CalibrationRepositoryImpl

class CalibrationController:
    def __init__(self):
        self.repository = CalibrationRepositoryImpl()
        self.process_use_case = ProcessCalibrationUseCaseImpl(self.repository)

    def process_calibration(self, image_content: bytes, expected_rgb: dict):
        return self.process_use_case.execute(image_content, expected_rgb)