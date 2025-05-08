from typing import List, Optional
from pydantic import BaseModel
import uuid

class Egg:
    def __init__(
        self,
        position: str,
        viability: bool,
        image_url: str,
        colorometry: str,
        defects: str,
        confidence: float,
        id: str = None,
    ):
        
        self.id = id if id else str(uuid.uuid4())
        self.position = position
        self.viability = viability
        self.image_url = image_url
        self.colorometry = colorometry
        self.defects = defects
        self.confidence = confidence

    def to_dict(self):
        """
        Convierte el objeto de dominio en un diccionario.
        """
        return {
            "id": self.id,
            "position": self.position,
            "viability": self.viability,
            "image_url": self.image_url,
            "colorometry": self.colorometry,
            "defects": self.defects,
            "confidence": self.confidence,
        }