import json
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, model_validator


class EstateImageDTO(BaseModel):
    id: int
    url: str
    created_at: datetime
    updated_at: datetime


class EstateDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: str
    owner_phone: Optional[str] = None
    realtor_phone: Optional[str] = None
    manager_phone: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    balcony_id: int
    condition_id: int
    district_id: int
    type_id: int
    room_id: int
    storey_id: int
    images: list[EstateImageDTO]


class EstateCreateDTO(BaseModel):
    name: str
    price: str
    description: Optional[str] = None
    owner_phone: Optional[str] = None
    realtor_phone: Optional[str] = None
    manager_phone: Optional[str] = None
    notes: Optional[str] = None

    balcony_id: int
    condition_id: int
    district_id: int
    type_id: int
    room_id: int
    storey_id: int
    floor_id: int

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class EstateUpdateDTO(BaseModel):
    name: Optional[str] = None
    price: Optional[str] = None
    description: Optional[str] = None
    owner_phone: Optional[str] = None
    realtor_phone: Optional[str] = None
    manager_phone: Optional[str] = None
    notes: Optional[str] = None

    balcony_id: Optional[int] = None
    condition_id: Optional[int] = None
    district_id: Optional[int] = None
    type_id: Optional[int] = None
    room_id: Optional[int] = None
    storey_id: Optional[int] = None
    floor_id: Optional[int] = None

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value