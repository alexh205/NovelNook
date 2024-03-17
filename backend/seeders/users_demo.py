from . import User, engine, Session, select


session = Session(engine)


def seed_users():

    users = [
        {
            "username": "demo",
            "email": "demo1@booknook.io",
            "password": "password1",
            "first_name": "Jane",
            "last_name": "Doe",
            "is_author": False,
        },
        {
            "username": "author1",
            "email": "johnDoe@booknook.io",
            "password": "password2",
            "first_name": "John",
            "last_name": "Doe",
            "is_author": True,
        },
        {
            "username": "demo2",
            "email": "stephanKing@booknook.io",
            "password": "password3",
            "first_name": "Stephan",
            "last_name": "King",
            "is_author": False,
        },
         {
            "username": "rebecca",
            "email": "rebecca@booknook.io",
            "password": "password4",
            "first_name": "Rebecca",
            "last_name": "Kuang",
            "is_author": True,
        },
         {
            "username": "donna",
            "email": "donna@booknook.io",
            "password": "password5",
            "first_name": "Donna",
            "last_name": "Tartt",
            "is_author": True,
        },
         {
            "username": "kamala",
            "email": "kamala@booknook.io",
            "password": "password6",
            "first_name": "Kamala",
            "last_name": "Markandaya",
            "is_author": True,
        }
    ]

    for user_data in users:
        user = User(**user_data)
        session.add(user)
    session.commit()


def undo_users():
    users = session.exec(select(User)).all()
    for user in users:
        session.delete(user)
    session.commit()
