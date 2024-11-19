from sqlalchemy import (
    insert,
    delete,
    select, update
)

from infrastructure.database.models import Balcony
from .base import BaseRepo


class BalconyRepo(BaseRepo):
    async def get_balconies(self):
        stmt = (
            select(Balcony)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_balcony(self, balcony_id: int):
        stmt = (
            select(Balcony)
            .where(Balcony.id == balcony_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def create_balcony(self, label: str):
        stmt = (
            insert(Balcony)
            .values(label=label)
            .returning(Balcony)
        )

        result = await self.session.execute(statement=stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete_balcony(self, balcony_id: int):
        stmt = (
          delete(Balcony)
          .where(Balcony.id == balcony_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def update_balcony(self, balcony_id: int, label: str):
        stmt = (
            update(Balcony)
            .values(label=label)
            .where(Balcony.id == balcony_id)
            .returning(Balcony)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()
