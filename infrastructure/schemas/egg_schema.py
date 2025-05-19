from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class EggSchema(BaseModel):
    """
    Esquema para representar un huevo en el sistema.
    """
    id: Optional[str] = None
    position: str
    viability: bool
    image_url: str
    colorometry: str
    cracks: bool
    deformities: bool
    defects: str
    confidence: float
    analyzed_at: datetime