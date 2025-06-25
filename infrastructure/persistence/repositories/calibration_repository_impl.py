from typing import List
from domain.repositories.calibration_repository import CalibrationRepository
from domain.models.calibration_model import Calibration
from infrastructure.entities.calibration_entity import CalibrationEntity

class CalibrationRepositoryImpl(CalibrationRepository):
    def save(self, calibration: Calibration):
        entity = CalibrationEntity(
            id=calibration.id,
            reference_color=calibration.reference_color,
            detected_color=calibration.detected_color,
            deviation=calibration.deviation,
            image_url=calibration.image_url,
            status=calibration.status,
            timestamp=calibration.timestamp
        )
        entity.save()

    def get_all(self) -> List[Calibration]:
        entities = CalibrationEntity.objects()
        return [self._to_domain(entity) for entity in entities]

    def find_by_status(self, status: str) -> List[Calibration]:
        entities = CalibrationEntity.objects(status=status)
        return [self._to_domain(entity) for entity in entities]

    def _to_domain(self, entity: CalibrationEntity) -> Calibration:
        return Calibration(
            id=entity.id,
            reference_color=entity.reference_color.to_mongo(),
            detected_color=entity.detected_color.to_mongo(),
            deviation=entity.deviation,
            image_url=entity.image_url,
            status=entity.status,
            timestamp=entity.timestamp
        )