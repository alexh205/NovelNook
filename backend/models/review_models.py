from . import Field, SQLModel, datetime


class Review(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str | None
    review_txt: str
    rating: int
    created_at: datetime | None
    updated_at: datetime | None

    user_id: int | None = Field(default=None, foreign_key="user.id")
    book_id: int | None = Field(default=None, foreign_key="book.id")
