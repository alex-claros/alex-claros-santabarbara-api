from datetime import datetime
from domain.models.egg_model import Egg
from domain.repositories.egg_repository import EggRepository
from app.services.roboflow_service import RoboflowService
from core.minio_client import MinioClient
from uuid import uuid4

class CreateEggUseCaseImpl:
    def __init__(self, repository: EggRepository, roboflow_service: RoboflowService):
        self.repository = repository
        self.roboflow_service = roboflow_service
        self.minio_client = MinioClient()

    def execute(self, image_content: bytes):
        """
        Procesa una imagen y guarda los huevos detectados en el maple correspondiente.
        """
        image_url = self.minio_client.upload_image(image_content)

        print(f"Image uploaded to MinIO: {image_url}")

        roboflow_response = self.roboflow_service.analyze_image(image_content)
        detected_eggs = roboflow_response.get("predictions", [])
        print(f"Detected eggs: {detected_eggs}")

        # Crear objetos Egg y guardar en MongoDB
        for egg_data in detected_eggs:
            egg = Egg(
                id=str(uuid4()),
                position="Individual",  # Coordenadas como posición
                viability=egg_data["class"] == "Healthy",  # Viabilidad según clase
                image_url=image_url,
                colorometry="#DD12D",  # Valor por defecto
                cracks=egg_data["class"] == "Damage",  # Asumimos que "Damage" implica grietas
                deformities=False,  # No detectado por el modelo
                defects=egg_data.get("defects", "unknown"),  # Campo no proporcionado
                confidence=egg_data["confidence"],
                analyzed_at=datetime.now()
            )
            self.repository.save(egg)

        return egg
