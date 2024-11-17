from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.mixins.int_id_pk import IntIdPkMixin
from .base import (
    Base,
    created_at,
    updated_at
)
from typing import Optional


class Balcony(Base, IntIdPkMixin):
    label: Mapped[str] = mapped_column(String)
    created_at: Mapped[created_at]
    updated_at: Mapped[Optional[updated_at]]

