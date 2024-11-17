from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.interfaces.storey import (
    StoreyCreateDTO,
    StoreyDTO
)
from infrastructure.database.repo.requests import RequestsRepo

router = APIRouter(
    prefix=config.api_prefix.v1.storeys,
    tags=['Storeys']
)


@router.get('/', response_model=list[StoreyDTO])
async def get_storeys(
        repo: Annotated[RequestsRepo, Depends(get_repo)]
):
    storeys = await repo.storey.get_all()
    return storeys


@router.post('/', response_model=StoreyDTO)
async def create_storey(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        storey: StoreyCreateDTO
):
    new_storey = await repo.storey.create(storey.label)
    return StoreyDTO.model_validate(new_storey, from_attributes=True)


@router.delete('/{storey_id}', status_code=204)
async def delete_storey(
        storey_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    await repo.storey.delete(storey_id)


@router.patch('/{storey_id}', response_model=StoreyDTO)
async def update_storey(
        storey_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        storey: StoreyCreateDTO,
):
    updated = await repo.storey.update(storey_id, storey.label)
    return StoreyDTO.model_validate(updated, from_attributes=True)
