from fastapi import HTTPException
from domain.use_cases.detect_egg_viability_use_case import DetectEggViabilityUseCase
from domain.use_cases.add_egg_to_maple_use_case import AddEggToMapleUseCase
from infrastructure.persistence.repositories.egg_repository import SqlAlchemyEggRepository
from infrastructure.persistence.repositories.maple_repository import SqlAlchemyMapleRepository
from infrastructure.persistence.repositories.image_repository import ImageRepository
from infrastructure.recognition.recognition import EggRecognitionModule
from sqlalchemy.orm import sessionmaker
from infrastructure.entities.egg import EggEntity

class EggController:
    def __init__(self, session: sessionmaker):
        self.session = session
        self.image_repository = ImageRepository()

    def detect_viability(self, egg_id: str):
        egg_repository = SqlAlchemyEggRepository(self.session)
        cnn_model = EggRecognitionModule("path/to/model.h5")
        use_case = DetectEggViabilityUseCase(egg_repository, cnn_model)
        
        try:
            result = use_case.execute(egg_id)
            return result
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def add_egg_to_maple(self, egg_id: str, maple_id: str, position: int, image_path: str):
        egg_repository = SqlAlchemyEggRepository(self.session)
        maple_repository = SqlAlchemyMapleRepository(self.session)
        use_case = AddEggToMapleUseCase(egg_repository, maple_repository)
        
        try:
            image_url = self.image_repository.upload_image(image_path, f"{egg_id}.jpg")
            
            egg = EggEntity(id=egg_id, position=position, image_url=image_url)
            result = use_case.execute(egg, maple_id)
            return result
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))