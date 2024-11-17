from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.interfaces.room import (
    RoomDTO,
    RoomCreateDTO
)
from infrastructure.database.repo.requests import RequestsRepo

router = APIRouter(
    prefix=config.api_prefix.v1.rooms,
    tags=['Rooms']
)


@router.get('/', response_model=list[RoomDTO])
async def get_rooms(
        repo: Annotated[RequestsRepo, Depends(get_repo)]
):
    rooms = await repo.room.get_all()
    return rooms


@router.post('/', response_model=RoomDTO)
async def create_room(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        room: RoomCreateDTO
):
    new_room = await repo.room.create(room.label)
    return RoomDTO.model_validate(new_room, from_attributes=True)


@router.delete('/{room_id}', status_code=204)
async def delete_room(
        room_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    await repo.room.delete(room_id)


@router.patch('/{room_id}', response_model=RoomDTO)
async def update_room(
        room_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        room: RoomCreateDTO
):
    updated_room = await repo.room.update(room_id, room.label)
    return RoomDTO.model_validate(updated_room, from_attributes=True)
