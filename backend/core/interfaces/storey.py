from datetime import datetime

from pydantic import BaseModel


class StoreyDTO(BaseModel):
    id: int
    label: str
    created_at: datetime
    updated_at: datetime


class StoreyCreateDTO(BaseModel):
    label: str