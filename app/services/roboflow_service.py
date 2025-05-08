from inference_sdk import InferenceHTTPClient

class RoboflowService:
    def __init__(self, api_url, api_key, model_id):
        self.client = InferenceHTTPClient(api_url=api_url, api_key=api_key)
        self.model_id = model_id

    def predict(self, image_content):
        """
        Realiza inferencias usando el modelo de Roboflow.
        """
        return self.client.infer(image_content, model_id=self.model_id)