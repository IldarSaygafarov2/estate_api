from typing import Annotated, Optional, List

from fastapi import APIRouter, Body, Depends, File, UploadFile, Query

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.filters.estate import EstateFilter
from backend.core.interfaces.estate import (
    EstateCreateDTO,
    EstateDTO,
    EstateUpdateDTO,
    PaginatedEstateDTO,
)
from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.utils.file import create_estate_directory

router = APIRouter(
    prefix=config.api_prefix.v1.estates,
    tags=["Estate"],
)


@router.get("/")
async def get_estates(
    filters: Annotated[EstateFilter, Query()],
    repo: Annotated[RequestsRepo, Depends(get_repo)],
) -> list[EstateDTO]:
    filters = {k: v for k, v in filters.model_dump().items() if v is not None}
    if not filters:
        items = await repo.estate.get_all()
    else:
        items = await repo.estate.get_filtered(**filters)

    items = [EstateDTO.model_validate(estate, from_attributes=True) for estate in items]
    return items


@router.post("/")
async def create_estate(
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    estate_create: EstateCreateDTO = Body(...),
    files: list[UploadFile] = File(...),
):
    try:
        estate_data = estate_create.model_dump()
        new_estate = await repo.estate.create(**estate_data)

        estate_directory = create_estate_directory(new_estate.id)
        images = []
        for file in files:
            file_name = file.filename
            path = estate_directory / file_name
            with open(path, "wb") as f:
                f.write(await file.read())
            image = await repo.estate_image.create(
                estate_id=new_estate.id, url=str(path)
            )
            images.append(
                {
                    "id": image.id,
                    "url": image.url,
                    "created_at": image.created_at,
                    "updated_at": image.updated_at,
                }
            )

        estate = await repo.estate.get_by_id(new_estate.id)
        return EstateDTO.model_validate(estate, from_attributes=True)
    except Exception as e:
        raise e


@router.delete("/{real_estate_id}", status_code=204)
async def delete_estate(
    real_estate_id: int,
    repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    await repo.estate.delete(real_estate_id)


@router.get("/{real_estate_id}", response_model=EstateDTO)
async def get_estate(
    real_estate_id: int,
    repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    estate = await repo.estate.get_by_id(real_estate_id)
    return EstateDTO.model_validate(estate, from_attributes=True)


@router.patch("/{real_estate_id}")
async def update_estate(
    real_estate_id: int,
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    estate_update: EstateUpdateDTO = Body(...),
    files: Optional[list[UploadFile]] = File(None),
):
    data = estate_update.model_dump()

    image_ids = data.get("images_ids", None)

    estate_images = await repo.estate_image.get_estate_images(estate_id=real_estate_id)
    estate_images_ids = [
        image.id for image in estate_images if image.id not in image_ids
    ]

    for image_id in estate_images_ids:
        await repo.estate_image.delete(estate_image_id=image_id)

    estate_directory = create_estate_directory(real_estate_id)

    if files is not None:
        for idx, file in enumerate(files):
            file_name = file.filename
            path = estate_directory / file_name
            with open(path, "wb") as f:
                f.write(await file.read())

            try:
                await repo.estate_image.update(
                    image_estate_id=image_ids[idx], url=str(path)
                )
            except IndexError:
                if len(files) > len(image_ids):
                    await repo.estate_image.create(
                        estate_id=real_estate_id, url=str(path)
                    )

    if image_ids is not None:
        data.pop("images_ids")

    data = dict([(x, y) for x, y in data.items() if y is not None])
    updated_estate = await repo.estate.update(real_estate_id, **data)

    return updated_estate
