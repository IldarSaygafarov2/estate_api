from datetime import datetime

from pydantic import BaseModel


class TypeDTO(BaseModel):
    id: int
    label: str
    created_at: datetime
    updated_at: datetime


class TypeCreateDTO(BaseModel):
    label: str

