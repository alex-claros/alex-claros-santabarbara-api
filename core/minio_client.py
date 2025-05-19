import io
from minio import Minio
from minio.error import S3Error
from uuid import uuid4

class MinioClient:
    def __init__(self):
        self.client = Minio(
            "localhost:9000",
            access_key="minioadmin",
            secret_key="minioadmin",
            secure=False
        )
        self.bucket_name = "egg-images"
        self._create_bucket()

    def _create_bucket(self):
        """Crea el bucket si no existe."""
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)

    def upload_image(self, image_content: bytes) -> str:
        """
        Sube una imagen a MinIO y devuelve su URL.
        """
        object_name = f"eggs/{uuid4()}.jpg"
        self.client.put_object(
            self.bucket_name,
            object_name,
            io.BytesIO(image_content),
            length=len(image_content),
            content_type="image/jpeg"
        )
        return self.client.presigned_get_object(self.bucket_name, object_name)