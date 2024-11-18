from typing import Annotated, List

from fastapi import APIRouter, Depends, Response, status

from backend.app.auth import get_current_user
from backend.app.config import config
from backend.app.dependencies import get_repo

from backend.core.interfaces.balcony import (
    BalconyDTO,
    BalconyCreateDTO
)
from infrastructure.database.models import User
from infrastructure.database.repo.requests import RequestsRepo


router = APIRouter(
    prefix=config.api_prefix.v1.balconies,
    tags=['Balconies']
)


@router.get('/', response_model=List[BalconyDTO])
async def get_balconies(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    balconies = await repo.balcony.get_balconies()
    return balconies


@router.post('/', response_model=BalconyDTO)
async def create_balcony(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        balcony_data: BalconyCreateDTO
):
    new_balcony = await repo.balcony.create_balcony(balcony_data.label)
    return BalconyDTO.model_validate(new_balcony, from_attributes=True)


@router.delete('/{balcony_id}')
async def delete_balcony(
        balcony_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    await repo.balcony.delete_balcony(balcony_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch('/{balcony_id}', response_model=BalconyDTO)
async def update_balcony(
        balcony_id: int,
        data: BalconyCreateDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    updated_balcony = await repo.balcony.update_balcony(
        balcony_id=balcony_id,
        label=data.label
    )
    return BalconyDTO.model_validate(updated_balcony, from_attributes=True)
