from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from domain.entities.maple import Maple

@dataclass
class Incubator:
    id: int
    location: str
    capacity: int
    temperature: float
    humidity: float
    maples: List[Maple] = field(default_factory=list)

    def add_maple(self, maple: Maple):
        """Agrega un maple a la incubadora y establece la asociación."""
        maple.assign_incubator(self)
        self.maples.append(maple)
