from fastapi import APIRouter, Depends
from typing import Annotated
from backend.app.config import config
from backend.app.dependencies import get_repo
from infrastructure.database.repo.requests import RequestsRepo
from backend.core.interfaces.estate import EstateForChannelDTO

router = APIRouter(
    prefix=config.api_prefix.v1.telegram,
    tags=['Telegram'],
)


@router.post('/send_to_channel')
async def send_to_channel(
    estate_ids: list[int],
    repo: Annotated[RequestsRepo, Depends(get_repo)]
) -> list[EstateForChannelDTO]:
    estates = await repo.estate.get_estates_by_ids(estate_ids)
    return estates
