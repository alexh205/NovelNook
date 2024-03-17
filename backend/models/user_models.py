from . import Field, SQLModel, datetime


class User(SQLModel, table=True):
    # Primary keys are automatically indexed by the database
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    is_author: bool
    is_active: bool = Field(default=True)
    created_at: datetime | None
    updated_at: datetime | None
