from typing import Annotated

import aiohttp
from fastapi import APIRouter, Depends, Request

from backend.app.config import config
from backend.app.dependencies import get_repo
from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.utils.telegram import create_telegram_message

router = APIRouter(
    prefix=config.api_prefix.v1.telegram,
    tags=["Telegram"],
)

TELEGRAM_API_URL = f"https://api.telegram.org/bot{config.telegram.token}/sendMediaGroup"
params = {
    "chat_id": "-1002343123218",
}


@router.post("/send_to_channel")
async def send_to_channel(
    estate_ids: list[int],
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    req: Request,
):
    estates = await repo.estate.get_estates_by_ids(estate_ids)

    errors = []
    for estate in estates:
        message = create_telegram_message(
            name=estate.name,
            description=estate.description,
            balcony=estate.balcony,
            condition=estate.condition,
            district=estate.district,
            floor=estate.floor,
            room=estate.room,
            storey=estate.storey,
            type=estate.type,
            price=estate.price,
            realtor_phone=estate.realtor_phone,
            manager_phone=estate.manager_phone,
        )
        data = []
        for idx, image_url in enumerate(estate.images):
            print()
            url = f"{req.base_url}{image_url.url}"
            url = url.replace("\\", "/")

            obj = {
                "filename": url.split("/")[-1],
                "type": "photo",
                "media": url,
            }
            if idx == 0:
                obj["caption"] = message
            data.append(obj)

        print(data)
        async with aiohttp.ClientSession() as session:
            async with session.post(
                TELEGRAM_API_URL,
                params=params,
                json={"media": data},
            ) as response:
                # Проверка статуса ответа
                errors.append(await response.json())
    return errors
