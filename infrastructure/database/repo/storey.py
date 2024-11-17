from sqlalchemy import (
    select,
    update,
    delete,
    insert
)

from infrastructure.database.models import Storey
from .base import BaseRepo


class StoreyRepo(BaseRepo):
    async def create(self, label: str):
        stmt = (
            insert(Storey)
            .values(label=label)
            .returning(Storey)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def update(self, storey_id: int, label: str):
        stmt = (
            update(Storey)
            .values(label=label)
            .where(Storey.id == storey_id)
            .returning(Storey)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, storey_id: int):
        stmt = (
            delete(Storey)
            .where(Storey.id == storey_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_all(self):
        stmt = select(Storey)
        result = await self.session.execute(stmt)
        return result.scalars().all()
