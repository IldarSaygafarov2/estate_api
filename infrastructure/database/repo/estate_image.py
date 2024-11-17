from .base import BaseRepo

from sqlalchemy import (
    insert
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
