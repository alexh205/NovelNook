from . import (
    UserRead,
    UserCreate,
    UserUpdate,
    User,
    engine,
    APIRouter,
    HTTPException,
    Session,
    set_password,
    check_password,
)


router = APIRouter(prefix="/users")


@router.get("/{id}", response_model=UserRead)
def get_user(id: int):
    with Session(engine) as session:
        user = session.get(User, id)
        if not user or not user.is_active:
            raise HTTPException(status_code=404, detail="User not found")

        return user


@router.post("/new", response_model=UserRead)
def create_user(user: UserCreate):
    with Session(engine) as session:
        user_data = User.model_validate(user)
        if not user_data:
            raise HTTPException(status_code=400, detail="Invalid data")
        user_data.hashed_password = set_password(user.hashed_password)
        session.add(user_data)
        session.commit()
        session.refresh(user_data)
    return user_data


@router.patch("/{id}", response_model=UserRead)
def update_user(id: int, user: UserUpdate):
    with Session(engine) as session:
        db_user = session.get(User, id)
        if not db_user or not db_user.is_active:
            raise HTTPException(status_code=404, detail="User not found")

        user_data = user.model_dump(exclude_unset=True)
        extra_data = {}

        if user.new_password and user.old_password:
            if not check_password(user.old_password, db_user.hashed_password):
                raise HTTPException(status_code=400, detail="Invalid password")

            extra_data["hashed_password"] = set_password(user_data["new_password"])

        db_user.sqlmodel_update(user_data, update=extra_data)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user


@router.patch("/remove/{id}")
def remove_user(id: int):
    with Session(engine) as session:
        user = session.get(User, id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.sqlmodel_update({"is_active": False})
        session.commit()
    return {"message": "User removed successfully"}
