import cv2

class CameraAdapter:
    def __init__(self, camera_id=0):
        """
        Inicializa el adaptador de cámara.
        
        Args:
            camera_id (int): ID de la cámara a usar (por defecto 0 para la cámara predeterminada).
        """
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(self.camera_id)
        if not self.cap.isOpened():
            raise Exception(f"No se pudo abrir la cámara con ID {self.camera_id}")

    def capture_image(self):
        """
        Captura una imagen desde la cámara.
        
        Returns:
            frame: La imagen capturada en formato BGR.
            
        Raises:
            Exception: Si no se logra capturar la imagen.
        """
        ret, frame = self.cap.read()
        if not ret or frame is None:
            raise Exception("No se pudo capturar la imagen de la cámara.")
        return frame

    def release(self):
        """
        Libera la cámara.
        """
        if self.cap.isOpened():
            self.cap.release()


if __name__ == "__main__":
    # Ejemplo de uso del adaptador de cámara
    try:
        adapter = CameraAdapter()
        image = adapter.capture_image()
        cv2.imshow("Imagen Capturada", image)
        cv2.waitKey(0)
    except Exception as e:
        print("Error:", e)
    finally:
        if 'adapter' in locals():
            adapter.release()
        cv2.destroyAllWindows()
