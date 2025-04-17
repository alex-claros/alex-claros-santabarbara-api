from pydantic import BaseModel

class ColorCalibrationParameters(BaseModel):
    white_balance: float = 1.0
    gamma_correction: float = 1.0
    histogram_equalization: bool = False