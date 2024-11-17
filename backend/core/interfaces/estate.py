from datetime import datetime
from fastapi import UploadFile

from pydantic import BaseModel


class EstateImageDTO(BaseModel):
    id: int
    url: str
    created_at: datetime
    updated_at: datetime


class EstateDTO(BaseModel):
    id: int
    name: str
    description: str
    price: str
    owner_phone: str
    realtor_phone: str
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
    description: str
    price: str
    owner_phone: str
    realtor_phone: str

    balcony_id: int
    condition_id: int
    district_id: int
    type_id: int
    room_id: int
    storey_id: int
