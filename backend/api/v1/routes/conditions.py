from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.interfaces.condition import (
    ConditionDTO,
    ConditionCreateDTO
)
from infrastructure.database.repo.requests import RequestsRepo

router = APIRouter(
    prefix=config.api_prefix.v1.conditions,
    tags=['Conditions']
)


@router.get('/', response_model=list[ConditionDTO])
async def get_conditions(
        repo: Annotated[RequestsRepo, Depends(get_repo)]
):
    conditions = await repo.condition.get_conditions()
    return conditions


@router.post('/', response_model=ConditionDTO)
async def create_condition(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        data: ConditionCreateDTO,
):
    new_condition = await repo.condition.create_condition(label=data.label)
    return ConditionDTO.model_validate(new_condition, from_attributes=True)


@router.delete('/{condition_id}', status_code=204)
async def delete_condition(
        condition_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)]
):
    await repo.condition.delete_condition(condition_id)


@router.patch('/{condition_id}', response_model=ConditionDTO)
async def update_condition(
        condition_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        data: ConditionCreateDTO,
):
    updated_condition = await repo.condition.update_condition(condition_id, label=data.label)
    return ConditionDTO.model_validate(updated_condition, from_attributes=True)
