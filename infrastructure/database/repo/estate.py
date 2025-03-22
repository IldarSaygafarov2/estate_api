from sqlalchemy import delete, func, insert, select, update
from sqlalchemy.orm import selectinload

from infrastructure.database.models import Estate
from .base import BaseRepo


class EstateRepo(BaseRepo):
    async def get_all(self, limit: int = 10, offset: int = 0):
        stmt = (
            select(Estate)
            .options(selectinload(Estate.images))
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_filtered(self, **filters):
        price_min = filters.pop("price_min", None)
        price_max = filters.pop("price_max", None)

        stmt = select(Estate).options(selectinload(Estate.images)).filter_by(**filters)

        if price_min is not None and price_max is not None:
            stmt = stmt.where(Estate.price > price_min).where(Estate.price < price_max)

        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(
        self,
        name: str,
        description: str,
        price: int,
        owner_phone: str,
        realtor_phone: str,
        manager_phone: str,
        notes: str,
        balcony: str,
        condition: str,
        district: str,
        type: str,
        room: str,
        storey: str,
        floor: str,
    ):
        stmt = (
            insert(Estate)
            .values(
                name=name,
                description=description,
                price=price,
                owner_phone=owner_phone,
                realtor_phone=realtor_phone,
                balcony=balcony,
                condition=condition,
                district=district,
                type=type,
                room=room,
                storey=storey,
                floor=floor,
                manager_phone=manager_phone,
                notes=notes,
            )
            .returning(Estate)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_by_id(self, estate_id: int):
        stmt = (
            select(Estate)
            .where(Estate.id == estate_id)
            .options(selectinload(Estate.images))
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def delete(self, estate_id: int):
        stmt = delete(Estate).where(Estate.id == estate_id)
        await self.session.execute(stmt)
        await self.session.commit()

    async def update(self, estate_id: int, **kwargs):
        stmt = (
            update(Estate)
            .values(**kwargs)
            .where(Estate.id == estate_id)
            .options(selectinload(Estate.images))
            .returning(Estate)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_estates_by_ids(self, estates_ids: list[int]):
        stmt = (
            select(Estate)
            .where(Estate.id.in_(estates_ids))
            .options(selectinload(Estate.images))
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_total_estates(self):
        stmt = select(func.count(Estate.id))
        result = await self.session.execute(stmt)
        return result.scalar_one()
