import enum
from typing import Optional

from sqlalchemy import String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from .base import Base, created_at
from .mixins.int_id_pk import IntIdPkMixin


class UserType(str, enum.Enum):
    CEO = 'CEO'
    EMPLOYEE = 'EMPLOYEE'


class User(Base, IntIdPkMixin):
    username: Mapped[str] = mapped_column(String(64))
    hashed_password: Mapped[str] = mapped_column(String(1024))
    registered_at: Mapped[created_at]
    user_type: Mapped[UserType] = mapped_column(
        postgresql.ENUM(UserType),
        default=UserType.EMPLOYEE
    )


