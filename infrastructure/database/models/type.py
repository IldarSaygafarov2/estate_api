from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, created_at, updated_at
from .mixins.int_id_pk import IntIdPkMixin


class Type(Base, IntIdPkMixin):
    label: Mapped[str] = mapped_column(String)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    estate = relationship('Estate', back_populates='type')