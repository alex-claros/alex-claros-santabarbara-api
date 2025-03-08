import torch
import cv2
import sys

class EggRecognitionModule:
    def __init__(self, model_path='yolov7_egg.pt', device=None, conf_threshold=0.5):
        """
        Inicializa el módulo de reconocimiento:
          - model_path: Ruta al archivo de pesos del modelo YOLOv7 entrenado.
          - device: Dispositivo ('cuda' o 'cpu'). Se detecta automáticamente si no se especifica.
          - conf_threshold: Umbral de confianza para filtrar detecciones.
        """
        if device is None:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.device = device
        
        try:
            # Carga el modelo personalizado desde el repositorio de YOLOv7
            self.model = torch.hub.load('WongKinYiu/yolov7', 'custom', path=model_path, force_reload=True)
        except Exception as e:
            print("Error al cargar el modelo:", e)
            sys.exit(1)
        
        self.model.to(self.device)
        self.model.eval()
        self.conf_threshold = conf_threshold
        self.egg_class = 0

    def detect_eggs(self, image):
        """
        Realiza la detección de huevos en una imagen.
          - image: Imagen en formato BGR (por ejemplo, leída con cv2.imread)
        Retorna:
          - count: Número de huevos detectados.
          - egg_boxes: Lista con las coordenadas y el nivel de confianza de cada detección.
        """
        # Convertir imagen de BGR a RGB
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.model(img_rgb)
        # Extraer las detecciones; cada detección es [x1, y1, x2, y2, conf, class]
        detections = results.xyxy[0].cpu().numpy()  
        egg_boxes = []
        for det in detections:
            x1, y1, x2, y2, conf, cls = det
            if conf >= self.conf_threshold and int(cls) == self.egg_class:
                egg_boxes.append((int(x1), int(y1), int(x2), int(y2), float(conf)))
        return len(egg_boxes), egg_boxes
