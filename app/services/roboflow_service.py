from inference_sdk import InferenceHTTPClient
from tempfile import NamedTemporaryFile
import shutil

class RoboflowService:
    def __init__(self):
        self.client = InferenceHTTPClient(
            api_url="https://serverless.roboflow.com",
            api_key="PI30adxnYJwIM1J4euE6"
        )

    def analyze_image(self, image_content: bytes):
        with NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(image_content)
            tmp_file_path = tmp_file.name

        try:
            result = self.client.infer(tmp_file_path, model_id="santabarbara/3")
            return result
        finally:
            import os
            os.remove(tmp_file_path)