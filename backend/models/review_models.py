from . import Field, SQLModel, datetime, Column, DateTime, func


class Review(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str | None
    review_txt: str
    rating: int
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
        ),
    )

    user_id: int | None = Field(default=None, foreign_key="user.id")
    book_id: int | None = Field(default=None, foreign_key="book.id")
