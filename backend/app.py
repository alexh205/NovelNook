from fastapi import FastAPI
from database import create_db_and_tables, engine
from seeders import seed_users


# FASTAPI
app = FastAPI()


def main():
    create_db_and_tables()
    seed_users()


if __name__ == "__main__":
    main()
