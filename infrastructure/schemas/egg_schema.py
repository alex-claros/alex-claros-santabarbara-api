from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class EggSchema(BaseModel):
    """
    Esquema para representar un huevo en el sistema.
    """
    id: Optional[str] = Field(None, description="Identificador único del huevo.")
    size: float = Field(..., description="Tamaño del huevo en unidades apropiadas (ej., gramos).")
    texture: str = Field(..., description="Descripción de la textura de la cáscara (ej., 'Lisa', 'Irregular').")
    color: str = Field(..., description="Color predominante de la cáscara (ej., 'Blanco', 'Marrón').")
    anomalies: List[str] = Field(default_factory=list, description="Lista de anomalías detectadas (ej., 'Grietas', 'Manchas').")
    image_url: Optional[str] = Field(None, description="URL de la imagen digital del huevo.")
    viability: Optional[str] = Field(None, description="Viabilidad del huevo ('Viable' o 'No viable').")
    confidence_score: Optional[float] = Field(None, description="Puntuación de confianza del modelo CNN (entre 0 y 1).")
    analysis_date: Optional[datetime] = Field(None, description="Fecha y hora del análisis realizado.")
    maple_id: Optional[str] = Field(None, description="ID del maple al que pertenece el huevo.")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "egg-12345",
                "size": 60.5,
                "texture": "Lisa",
                "color": "Blanco",
                "anomalies": ["Grieta pequeña"],
                "image_url": "http://example.com/images/egg-12345.jpg",
                "viability": "Viable",
                "confidence_score": 0.95,
                "analysis_date": "2023-10-01T12:34:56Z",
                "maple_id": "maple-67890"
            }
        }