from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.interfaces.type import (
    TypeDTO,
    TypeCreateDTO
)
from infrastructure.database.repo.requests import RequestsRepo

router = APIRouter(
    prefix=config.api_prefix.v1.types,
    tags=['Types']
)


@router.get('/', response_model=list[TypeDTO])
async def get_types(
        repo: Annotated[RequestsRepo, Depends(get_repo)]
):
    types = await repo.type.get_all()
    return types


@router.post('/', response_model=TypeDTO)
async def create_type(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        type_data: TypeCreateDTO
):
    new_type = await repo.type.create(type_data.label)
    return TypeDTO.model_validate(new_type, from_attributes=True)


@router.delete('/{type_id}', status_code=204)
async def delete_type(
        type_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    await repo.type.delete(type_id)


@router.patch('/{type_id}', response_model=TypeDTO)
async def update_type(
        type_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        type_data: TypeCreateDTO
):
    updated = await repo.type.update(type_id, type_data.label)
    return TypeDTO.model_validate(updated, from_attributes=True)
