from . import Field, SQLModel, datetime, Column, DateTime, func


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(max_length=16, nullable=False, unique=True)
    email: str = Field(unique=True)
    hashed_password: str = Field(max_length=24, nullable=False)
    first_name: str = Field(max_length=18, nullable=False)
    last_name: str = Field(max_length=28, nullable=False)
    profile_img: str | None = Field(default=None)
    is_author: bool | None = Field(default=False)
    is_active: bool = Field(default=True)
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
        ),
    )

    # ! Relationships
    # books: List["Book"] = Relationship(back_populates="author")


class UserRead(SQLModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    profile_img: str | None
    is_author: bool


class UserCreate(SQLModel):
    username: str
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    profile_img: str | None


class UserUpdate(SQLModel):
    username: str | None = None
    email: str | None = None
    old_password: str | None = None
    new_password: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    profile_img: str | None = None
    is_author: bool | None = None
