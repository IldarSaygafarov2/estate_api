from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.mixins.int_id_pk import IntIdPkMixin
from .base import Base, created_at, updated_at


class Estate(Base, IntIdPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[str]
    owner_phone: Mapped[str]
    realtor_phone: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    balcony_id: Mapped[int] = mapped_column(ForeignKey('balconies.id'))
    condition_id: Mapped[int] = mapped_column(ForeignKey('conditions.id'))
    district_id: Mapped[int] = mapped_column(ForeignKey('districts.id'))
    type_id: Mapped[int] = mapped_column(ForeignKey('types.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
    storey_id: Mapped[int] = mapped_column(ForeignKey('storeys.id'))

    images: Mapped[list["Image"]] = relationship(back_populates='estate')


class Image(Base, IntIdPkMixin):
    url: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    estate_id: Mapped[int] = mapped_column(ForeignKey('estates.id', ondelete='CASCADE'))
    estate: Mapped['Estate'] = relationship(back_populates='images')
