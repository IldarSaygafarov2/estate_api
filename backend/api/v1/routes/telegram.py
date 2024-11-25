from io import BytesIO
from typing import Annotated
import json

import aiohttp
from fastapi import APIRouter, Depends, Request

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.interfaces.estate import EstateForChannelDTO
from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.utils.telegram import (
    compress_image,
    create_telegram_message,
    send_message_to_channel,
)

router = APIRouter(
    prefix=config.api_prefix.v1.telegram,
    tags=["Telegram"],
)

TELEGRAM_API_URL = f"https://api.telegram.org/bot{config.telegram.token}/sendMediaGroup"
params = {
    "chat_id": f"@{config.telegram.channel_username}",
}


@router.post("/send_to_channel")
async def send_to_channel(
    estate_ids: list[int],
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    req: Request,
):
    print(req.base_url)
    estates = await repo.estate.get_estates_by_ids(estate_ids)

    # estate_images = []

    # for estate in estates:
    #     for image in estate.images:
    #         estate_images.append(image.url)

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
            realtor_phone=estate.realtor_phone,
            manager_phone=estate.manager_phone,
        )
        data = []
        for idx, image_url in enumerate(estate.images):
            obj = {
                "filename": image_url.url.split("/")[-1],
                "type": "photo",
                "media": f"{req.base_url}{image_url.url}",
            }
            if idx == 0:
                obj["caption"] = message
            data.append(obj)

        print(data)
        async with aiohttp.ClientSession() as session:
            # form_data = aiohttp.FormData()
            # for media in data:
            #     form_data.add_field(
            #         "media",
            #         media["media"],  # Файл как объект
            #         filename=media["filename"],  # Можно указать имя файла
            #         content_type="image/jpeg",  # Указание типа контента
            #     )
            # params["caption"] = message
            async with session.post(
                TELEGRAM_API_URL,
                params=params,
                json={"media": data},
            ) as response:
                # Проверка статуса ответа
                if response.status == 200:
                    return {
                        "status": "success",
                        "message": "Media group sent successfully.",
                    }
                else:
                    error_data = await response.json()
                    return {"status": "error", "message": error_data}
