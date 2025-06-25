from typing import Dict
import uuid
from datetime import datetime

class Calibration:
    def __init__(
        self,
        reference_color: Dict[str, int],
        detected_color: Dict[str, int],
        deviation: float,
        image_url: str,
        status: str = "success",
        id: str = None,
        timestamp: datetime = None
    ):
        self.id = id if id else str(uuid.uuid4())
        self.reference_color = reference_color
        self.detected_color = detected_color
        self.deviation = deviation
        self.image_url = image_url
        self.status = status
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "reference_color": self.reference_color,
            "detected_color": self.detected_color,
            "deviation": self.deviation,
            "image_url": self.image_url,
            "status": self.status,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None
        }