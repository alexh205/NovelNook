from . import Field, SQLModel, datetime


class Book(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    title: str = Field(max_length=50, nullable=False)
    publication_year: str
    genre: str
    description: str = Field(max_length=180)
    cover_image: str
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    author_id: int = Field(default=None, foreign_key="user.id")

    class Config:
        from_attributes = True


# engine = create_engine("sqlite:///database.db")

# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(book_1)
#     session.add(book_2)
#     session.add(book_3)
#     session.commit()
