from sqlalchemy.orm import Mapped, mapped_column
from ..database.date_tool import get_current_utc
from base_class import Base
from datetime import datetime


class BookModel(Base):
    __tablename__ = "books"

    created_at: Mapped[datetime] = mapped_column(
        server_default=get_current_utc)
    updated_at: Mapped[datetime] = mapped_column(
        server_default=get_current_utc)
