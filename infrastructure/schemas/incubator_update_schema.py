from pydantic import BaseModel
from typing import Optional

class IncubatorUpdateSchema(BaseModel):
    name: Optional[str] = None
    capacity: Optional[int] = None
    status: Optional[str] = None
    temperature: Optional[str] = None
    last_mant: Optional[str] = None
    maples: Optional[list] = None 

    class Config:
        orm_mode = True