import bcrypt
from . import Field, SQLModel, datetime, Column, DateTime, func


class User(SQLModel, table=True):
    # Primary keys are automatically indexed by the database
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password_hash: str | None
    first_name: str
    last_name: str
    is_author: bool
    is_active: bool = Field(default=True)
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
        ),
    )

    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            onupdate=func.now(),
        ),
    )

    def __init__(self, *args, **kwargs):
        """
        Method that is called with each class instance creation for password hashing functionality
        """
        super().__init__(*args, **kwargs)
        if "password" in kwargs:
            self.set_password(kwargs["password"])  # Hash and set the password

    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)

    def check_password(self, password):
        return bcrypt.checkpw(
            password.encode("utf-8"), self.password_hash.encode("utf-8")
        )
