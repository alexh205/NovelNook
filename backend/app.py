from db import schemas
from api import users_router
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from db.database import Base, engine, get_db
from models.booksModel import Book, BookCreate, BookSchema
# from models.usersModel import UserSchema, UserCreateSchema, UserDBModel

# FASTAPI
app = FastAPI()

book_router = SQLAlchemyCRUDRouter(
    schema=BookSchema,
    create_schema=BookCreate, 
    db_model=Book,
    db=get_db
)

# user_router = SQLAlchemyCRUDRouter(
#     schema=UserSchema,
#     create_schema=UserCreateSchema,
#     db_model=UserDBModel,
#     db=get_db
# )

app.include_router(book_router)
# app.include_router(user_router)

# Creating SQL Tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def front_page():
    return {"Hello": "World!"}

@app.post("/users/", response_model=schemas.UserBase)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = users_router.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users_router.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users_router.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
