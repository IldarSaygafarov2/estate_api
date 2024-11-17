from fastapi import APIRouter
from backend.app.config import config

router = APIRouter(
    prefix=config.api_prefix.v1.storeys,
    tags=['Storeys']
)


@router.post('/')
async def create_storey():
    return ''


@router.delete('/{id}')
async def delete_storey(id: int):
    return ''
