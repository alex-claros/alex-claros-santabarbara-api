from domain.use_cases.base_use_case import BaseUseCase
from domain.repositories.egg_repository import EggRepository
from infrastructure.recognition.recognition import EggRecognitionModule

class DetectEggViabilityUseCase(BaseUseCase):
    def __init__(self, egg_repository: EggRepository, cnn_model: EggRecognitionModule):
        self.egg_repository = egg_repository
        self.cnn_model = cnn_model

    def execute(self, egg_id: str):
        # Obtener el huevo desde el repositorio
        egg = self.egg_repository.find_by_id(egg_id)
        if not egg:
            raise ValueError("Huevo no encontrado")
        
        # Usar el modelo CNN para predecir la viabilidad
        viability = self.cnn_model.predict(egg.image_data)
        
        # Actualizar la viabilidad del huevo
        egg.viability = viability
        self.egg_repository.save(egg)
        
        return {"egg_id": egg.id, "viability": viability}