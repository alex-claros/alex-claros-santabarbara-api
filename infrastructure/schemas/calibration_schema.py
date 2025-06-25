from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class CalibrationSchema(BaseModel):
    id: Optional[str] = None
    reference_color: Dict[str, int]
    detected_color: Dict[str, int]
    deviation: float
    image_url: str
    status: str
    timestamp: Optional[datetime] = None