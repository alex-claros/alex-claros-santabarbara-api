from typing import List, Optional
from pydantic import BaseModel
import uuid
from datetime import datetime

class Egg:
    def __init__(
        self,
        position: str,
        viability: bool,
        image_url: str,
        colorometry: str,
        cracks: bool,
        deformities: bool,
        defects: str,
        confidence: float,
        id: str = None,
        analyzed_at: Optional[datetime] = None,
    ):
        
        self.id = id if id else str(uuid.uuid4())
        self.position = position
        self.viability = viability
        self.image_url = image_url
        self.colorometry = colorometry
        self.cracks = cracks
        self.deformities = deformities
        self.defects = defects
        self.confidence = confidence
        self.analyzed_at = analyzed_at

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
            "cracks": self.cracks,
            "deformities": self.deformities,
            "defects": self.defects,
            "confidence": self.confidence,
            "analyzed_at": self.analyzed_at.isoformat() if self.analyzed_at else None,
        }