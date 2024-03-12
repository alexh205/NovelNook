# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
#     username: Mapped[str] = mapped_column(String(30), index=True, unique=True)
#     email: Mapped[str] = mapped_column(index=True, unique=True)
#     first_name: Mapped[str] = mapped_column(String(20), nullable=False)
#     last_name: Mapped[str] = mapped_column(String(20), nullable=False)
#     password: Mapped[str] = mapped_column(nullable=False)
#     is_author: Mapped[bool] = mapped_column(default=False)
#     is_active: Mapped[bool] = mapped_column(default=False)
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now()
#     )
#     updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
