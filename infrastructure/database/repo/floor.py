from sqlalchemy import (
    select,
    update,
    delete,
    insert
)

from infrastructure.database.models import Floor
from .base import BaseRepo


class FloorRepo(BaseRepo):
    async def create(self, label: str):
        stmt = (
            insert(Floor)
            .values(label=label)
            .returning(Floor)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_floor(self, floor_id: int):
        stmt = select(Floor).where(Floor.id == floor_id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def update(self, floor_id: int, label: str):
        stmt = (
            update(Floor)
            .values(label=label)
            .where(Floor.id == floor_id)
            .returning(Floor)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, floor_id: int):
        stmt = (
            delete(Floor)
            .where(Floor.id == floor_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_all(self):
        stmt = select(Floor)
        result = await self.session.execute(stmt)
        return result.scalars().all()
