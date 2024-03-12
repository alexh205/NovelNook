from fastapi import FastAPI
from sqlmodel import SQLModel

from database import engine

# FASTAPI
app = FastAPI()


# Creating SQL Tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()
