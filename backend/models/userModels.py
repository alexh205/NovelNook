from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    # Primary keys are automatically indexed by the database
    id: Optional[int] = Field(default=None, primary_key=True)
    # username: str = Field(index=True)
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    is_author: bool
    is_active: bool = Field(default=True)
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
