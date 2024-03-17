from . import Field, SQLModel, datetime, Column, DateTime, func


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    publication_year: str
    genre: str
    description: str
    cover_image: str
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now()),
    )

    author_id: int | None = Field(default=None, foreign_key="user.id")
