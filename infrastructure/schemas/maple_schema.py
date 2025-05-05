from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class MapleSchema(BaseModel):
    id: Optional[str] = None
    name: str
    capacity: int
    status: str
    level: str
    eggs: Optional[list] = list
    load_date: datetime
    responsible: Optional[str]
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None