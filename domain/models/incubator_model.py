from typing import List, Optional
from pydantic import BaseModel
from domain.models.maple_model import Maple

class Incubator(BaseModel):
    id: str
    capacity: int  # Número máximo de maples
    maples: List[Maple] = []  # Lista de maples en la incubadora

    def add_maple(self, maple: Maple):
        """Añade un maple a la incubadora si hay espacio."""
        if len(self.maples) < self.capacity:
            self.maples.append(maple)
        else:
            raise ValueError("La incubadora está llena.")

    def get_maple_by_id(self, maple_id: str) -> Optional[Maple]:
        """Obtiene un maple por su ID."""
        for maple in self.maples:
            if maple.id == maple_id:
                return maple
        return None