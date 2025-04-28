from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class IncubatorSchema(BaseModel):
    id: Optional[str] = None
    name: str
    capacity: int
    status: str
    temperature: str
    last_mant: str
    maple: Optional[list] = []
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None