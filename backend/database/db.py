from sqlmodel import create_engine, SQLModel

"""Python executes all the code creating the classes inheriting from SQLModel and registering them in the SQLModel.metadata"""
from models import User, Book
from decouple import config

DATABASE_URL = config("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)


# Creating SQL Tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
