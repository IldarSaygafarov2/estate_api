from datetime import datetime

from pydantic import BaseModel


class FloorDTO(BaseModel):
    id: int
    label: str
    created_at: datetime
    updated_at: datetime


class FloorCreateDTO(BaseModel):
    label: str
