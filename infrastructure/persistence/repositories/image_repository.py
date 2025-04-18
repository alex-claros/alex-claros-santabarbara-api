from core.minio_client import MinioClient

class ImageRepository:
    def __init__(self):
        self.minio_client = MinioClient()
        self.bucket_name = "egg-images"  # Nombre del bucket para imágenes de huevos
        self.minio_client.create_bucket(self.bucket_name)

    def upload_image(self, file_path, object_name):
        """Sube una imagen a MinIO y devuelve su URL."""
        file_path_in_minio = self.minio_client.upload_file(self.bucket_name, file_path, object_name)
        if file_path_in_minio:
            return self.minio_client.get_file_url(self.bucket_name, object_name)
        return None