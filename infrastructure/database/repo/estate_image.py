from .base import BaseRepo

from sqlalchemy import (
    insert,
    update, select, delete
)
from infrastructure.database.models.estate import Image


class EstateImageRepo(BaseRepo):
    async def create(self, estate_id: int, url: str):
        stmt = (
            insert(Image)
            .values(
                estate_id=estate_id,
                url=url
            )
            .returning(Image)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def update(self, image_estate_id: int, url: str):
        stmt = (
            update(Image)
            .values(url=url)
            .where(Image.id == image_estate_id)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_estate_images(self, estate_id: int):
        stmt = (
            select(Image)
            .where(Image.estate_id == estate_id)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def delete(self, estate_image_id: int):
        stmt = (
            delete(Image)
            .where(Image.id == estate_image_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()

