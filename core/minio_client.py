from minio import Minio
from minio.error import S3Error

class MinioClient:
    def __init__(self):
        self.client = Minio(
            "localhost:9000",  # Dirección del servidor MinIO
            access_key="minioadmin",  # Usuario
            secret_key="minioadmin",  # Contraseña
            secure=False  # Cambia a True si usas HTTPS
        )

    def create_bucket(self, bucket_name):
        """Crea un bucket si no existe."""
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)

    def upload_file(self, bucket_name, file_path, object_name):
        """Sube un archivo al bucket."""
        try:
            self.client.fput_object(bucket_name, object_name, file_path)
            return f"{bucket_name}/{object_name}"
        except S3Error as e:
            print(f"Error al subir archivo: {e}")
            return None

    def get_file_url(self, bucket_name, object_name):
        """Obtiene la URL pública de un archivo."""
        try:
            url = self.client.presigned_get_object(bucket_name, object_name)
            return url
        except S3Error as e:
            print(f"Error al obtener URL: {e}")
            return None