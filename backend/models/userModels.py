from datetime import datetime
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, table


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    is_author: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime
