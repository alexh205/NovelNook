from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from ..database.date_tool import get_current_utc
from base_class import Base
from datetime import datetime


class UserModel(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(index=True, unique=True)
    email: Mapped[str] = mapped_column(index=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]
    is_author: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(
        server_default=get_current_utc)
    updated_at: Mapped[datetime] = mapped_column(
        server_default=get_current_utc)
