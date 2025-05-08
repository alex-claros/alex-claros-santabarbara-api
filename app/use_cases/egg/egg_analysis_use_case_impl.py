from domain.models.egg_model import Egg
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl
from app.services.roboflow_service import RoboflowService
from uuid import uuid4
from core.minio_client import MinioClient

class ImageClassificationUseCaseImpl:
    def __init__(self, repository, roboflow_service):
        self.repository = EggRepositoryImpl
        self.roboflow_service = RoboflowService
        self.minio_client = MinioClient()

    def execute(self, image_content, position: str):
        """
        Procesa una imagen para clasificar huevos y guardar los resultados.
        :param image_content: Contenido binario de la imagen.
        :param position: Posición del huevo en el maple (por ejemplo, "Maple_1_Hueco_1").
        :return: Predicciones generadas por el modelo.
        """
        bucket_name = "egg-images"
        object_name = f"{uuid4()}.jpg"
        with open("/tmp/temp_image.jpg", "wb") as temp_file:
            temp_file.write(image_content)
        self.minio_client.upload_file(bucket_name, "/tmp/temp_image.jpg", object_name)
        image_url = self.minio_client.get_file_url(bucket_name, object_name)

        predictions = self.roboflow_service.predict(image_content)

        for prediction in predictions.get("predictions", []):
            viability = prediction["class"] == "Healthy"  # True si es viable, False si no
            colorometry = prediction.get("color", "normal")  # Color detectado
            defects = ", ".join(prediction.get("defects", []))  # Defectos detectados
            confidence = prediction.get("confidence", 0.0)

            egg = Egg(
                position=position,
                viability=viability,
                image_url=image_url,
                colorometry=colorometry,
                defects=defects,
                confidence=confidence
            )

            self.repository.save(egg)

        return predictions