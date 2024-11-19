from fastapi import APIRouter, Depends
from typing import Annotated
from backend.app.config import config
from backend.core.interfaces.floor import (
    FloorDTO,
    FloorCreateDTO
)
from infrastructure.database.repo.requests import RequestsRepo
from backend.app.dependencies import get_repo


router = APIRouter(
    prefix=config.api_prefix.v1.floors,
    tags=['Floors']
)


@router.get('/', response_model=list[FloorDTO])
async def get_floors(
        repo: Annotated[RequestsRepo, Depends(get_repo)]
):
    floors = await repo.floor.get_all()
    return floors


@router.post('/')
async def create_floor(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        floor_create: FloorCreateDTO
):
    new_floor = await repo.floor.create(label=floor_create.label)
    return FloorDTO.model_validate(new_floor, from_attributes=True)


@router.get('/{floor_id}', response_model=FloorDTO)
async def get_floor(
        floor_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    floor = await repo.floor.get_floor(floor_id)
    return FloorDTO.model_validate(floor, from_attributes=True)

@router.delete('/{floor_id}', status_code=204)
async def delete_floor(
        floor_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    await repo.floor.delete(floor_id)


@router.patch('/{floor_id}', response_model=FloorDTO)
async def update_floor(
        floor_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        floor_data: FloorCreateDTO
):
    updated_floor = await repo.floor.update(floor_id, label=floor_data.label)
    return FloorDTO.model_validate(updated_floor, from_attributes=True)
