from sqlmodel import create_engine, SQLModel

"""Python executes all the code creating the classes inheriting from SQLModel and registering them in the SQLModel.metadata"""
from models import User

sqlite_url = f"sqlite:///database/database.db"

engine = create_engine(sqlite_url, echo=True)


# Creating SQL Tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
