from . import Field, SQLModel, datetime


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    publication_year: str
    genre: str
    description: str
    cover_image: str
    created_at: datetime | None
    updated_at: datetime | None

    author_id: int | None = Field(default=None, foreign_key="user.id")
