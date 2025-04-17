from typing import Optional
from pydantic import BaseModel

class Egg(BaseModel):
    id: str
    position: int  # Posición dentro del maple
    viability: Optional[bool] = None  # True si es viable, False si no lo es
    image_data: Optional[str] = None  # Datos de la imagen codificados en base64
    colorimetry: Optional[float] = None  # Valor de colorimetría
    structural_defects: Optional[bool] = None  # Indica si tiene defectos estructurales

    def is_viable(self) -> bool:
        """Determina si el huevo es viable basado en reglas de negocio."""
        if self.structural_defects or (self.colorimetry and self.colorimetry < 0.5):
            return False
        return True