from dataclasses import dataclass

@dataclass
class ViabilityResult:
    is_viable: bool
    confidence: float  
    details: str = "" 
