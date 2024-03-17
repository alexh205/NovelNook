from fastapi import FastAPI
from seeders import seed_all, undo_seed_all, session, select, User

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

@app.get("/ping")
async def ping():
    return {"test": "acknowledged!"}

@app.get("/")
def front_page():
    return {"Hello": "World!"}

def start_up():
    users = session.exec(select(User)).all()
    if users:
        undo_seed_all()
    seed_all()


if __name__ == "__main__":
    # Calling start_up function only if this script is directly run
    start_up()
