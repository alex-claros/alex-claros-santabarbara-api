from pydantic import BaseModel

class IncubatorSchema(BaseModel):
    id: str
    name: str
    capacity: int
    status: str
    temperature: str
    last_mant: str