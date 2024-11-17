from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, File, Form

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.interfaces.estate import (
    EstateDTO
)
from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.utils.file import create_estate_directory

router = APIRouter(
    prefix=config.api_prefix.v1.estates,
    tags=["Estate"],
)


@router.post('/', response_model=EstateDTO)
async def create_estate(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        name: str = Form(...),
        description: str = Form(...),
        price: str = Form(...),
        owner_phone: str = Form(...),
        realtor_phone: str = Form(...),
        balcony_id: int = Form(...),
        district_id: int = Form(...),
        room_id: int = Form(...),
        type_id: int = Form(...),
        storey_id: int = Form(...),
        condition_id: int = Form(...),
        files: list[UploadFile] = File(...),

):
    new_estate = await repo.estate.create(
        name=name,
        description=description,
        price=price,
        owner_phone=owner_phone,
        realtor_phone=realtor_phone,
        balcony_id=balcony_id,
        district_id=district_id,
        room_id=room_id,
        type_id=type_id,
        storey_id=storey_id,
        condition_id=condition_id,
    )

    estate_directory = create_estate_directory(new_estate.id)

    images = []

    for file in files:
        file_name = file.filename
        path = estate_directory / file_name

        with open(path, 'wb') as f:
            f.write(await file.read())

        image = await repo.estate_image.create(estate_id=new_estate.id, url=str(path))
        images.append({
            'id': image.id,
            'url': image.url,
            'created_at': image.created_at,
            'updated_at': image.updated_at,
        })

    result = dict(
        id=new_estate.id,
        name=name,
        description=description,
        price=price,
        owner_phone=owner_phone,
        realtor_phone=realtor_phone,
        balcony_id=balcony_id,
        district_id=district_id,
        room_id=room_id,
        type_id=type_id,
        storey_id=storey_id,
        condition_id=condition_id,
        created_at=new_estate.created_at,
        updated_at=new_estate.updated_at,
        images=images,
    )

    return EstateDTO.model_validate(result, from_attributes=True)


"""

{
  "type_id": 1,
  "owner_phone": "string",
  "storey_id": 1,
  "realtor_phone": "string",
  "price": "string",
  "name": "string",
  "district_id": 1,
  "balcony_id": 1,
  "description": "string",
  "condition_id": 1,
  "room_id": 1
}
"""
