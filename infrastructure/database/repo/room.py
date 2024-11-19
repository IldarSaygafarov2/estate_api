from .base import BaseRepo
from sqlalchemy import (
    select, update, delete, insert
)

from infrastructure.database.models import Room


class RoomRepo(BaseRepo):
    async def create(self, label: str):
        stmt = (
            insert(Room)
            .values(label=label)
            .returning(Room)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_room(self, room_id: int):
        stmt = (
            select(Room)
            .where(Room.id == room_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def delete(self, room_id: int):
        stmt = (
            delete(Room)
            .where(Room.id == room_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def update(self, room_id: int, label: str):
        stmt = (
            update(Room)
            .where(Room.id == room_id)
            .values(label=label)
            .returning(Room)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_all(self):
        stmt = select(Room)
        result = await self.session.execute(stmt)
        return result.scalars().all()

