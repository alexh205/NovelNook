from fastapi import FastAPI
from seeders import seed_all, undo_seed_all, session, select, User

# FASTAPI
app = FastAPI()


@app.get("/ping")
async def ping():
    return {"test": "acknowledged!"}


def start_up():
    users = session.exec(select(User)).all()
    if users:
        undo_seed_all()
    seed_all()


if __name__ == "__main__":
    # Calling start_up function only if this script is directly run
    start_up()
