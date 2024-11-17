from fastapi import APIRouter
from backend.app.config import config

router = APIRouter(
    prefix=config.api_prefix.v1.rooms,
    tags=['Rooms']
)


@router.post('/')
async def create_room():
    return ''


@router.delete('/{id}')
async def delete_room(id: int):
    return ''
