from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.balcony import Balcony
from infrastructure.database.models.condition import Condition
from infrastructure.database.models.district import District
from infrastructure.database.models.floor import Floor
from infrastructure.database.models.room import Room
from infrastructure.database.models.storey import Storey
from infrastructure.database.models.type import Type

from .base import Base, created_at, updated_at
from .mixins.int_id_pk import IntIdPkMixin


class Estate(Base, IntIdPkMixin):
    name: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    price: Mapped[Optional[str]]
    owner_phone: Mapped[Optional[str]]
    realtor_phone: Mapped[Optional[str]]
    manager_phone: Mapped[Optional[str]]
    notes: Mapped[Optional[str]]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    balcony_id: Mapped[Optional[int]] = mapped_column(ForeignKey('balconies.id'))
    condition_id: Mapped[Optional[int]] = mapped_column(ForeignKey('conditions.id'))
    district_id: Mapped[Optional[int]] = mapped_column(ForeignKey('districts.id'))
    type_id: Mapped[Optional[int]] = mapped_column(ForeignKey('types.id'))
    room_id: Mapped[Optional[int]] = mapped_column(ForeignKey('rooms.id'))
    storey_id: Mapped[Optional[int]] = mapped_column(ForeignKey('storeys.id'))
    floor_id: Mapped[Optional[int]] = mapped_column(ForeignKey('floors.id'))

    images: Mapped[list["Image"]] = relationship(back_populates='estate')
    
    balcony: Mapped["Balcony"] = relationship(back_populates='estate')
    condition: Mapped["Condition"] = relationship(back_populates='estate')
    district: Mapped["District"] = relationship(back_populates='estate')
    room: Mapped["Room"] = relationship(back_populates='estate')
    floor: Mapped["Floor"] = relationship(back_populates='estate')
    storey: Mapped["Storey"] = relationship(back_populates='estate')
    type: Mapped["Type"] = relationship(back_populates='estate')


class Image(Base, IntIdPkMixin):
    url: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    estate_id: Mapped[int] = mapped_column(ForeignKey('estates.id', ondelete='CASCADE'))
    estate: Mapped['Estate'] = relationship(back_populates='images')
