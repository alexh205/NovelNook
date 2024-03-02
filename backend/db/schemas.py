from pydantic import BaseModel
from datetime import datetime
from typing import Optional

############ ? User Schema #####################


class UserBase(BaseModel):
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int
    is_author: bool = False
    is_active: bool = False
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


############ ! Book Schema #####################

class BookBase(BaseModel):
    title: str
    authorId: Optional[int] = None
    publication_year: Optional[datetime] = None
    genres: str
    description: Optional[str] = None
    cover_image: str


class CreateBook(BookBase):
    pass


class UpdateBook(BookBase):
    pass


class BookInDBBase(BookBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


############ * Review Schema #####################

class ReviewBase(BaseModel):
    title: str
    userId: int
    bookId: int
    review_txt: Optional[str] = None
    rating: int


class CreateReview(ReviewBase):
    pass


class UpdateReview(ReviewBase):
    pass


class ReviewInDBBase(ReviewBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
