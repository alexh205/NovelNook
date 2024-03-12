# class Book(Base):
#     __tablename__ = "books"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
#     title: Mapped[str] = mapped_column(String(50), nullable=False)
#     publication_year: Mapped[datetime] = mapped_column()
#     genre: Mapped[str] = mapped_column()
#     description: Mapped[str] = mapped_column(String(180))
#     cover_image: Mapped[str]
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now()
#     )
#     updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
