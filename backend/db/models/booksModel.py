from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import functions
import sqlalchemy
from db.database import Base
from datetime import datetime


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=functions.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=True,
        server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True),
    )
