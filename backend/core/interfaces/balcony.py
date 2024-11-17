from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BalconyDTO(BaseModel):
    id: int
    label: str
    created_at: datetime
    updated_at: Optional[datetime]


class BalconyCreateDTO(BaseModel):
    label: str


