from models import User


user1 = User(
    username="demo",
    email="demo1@booknook.io",
    first_name="Jane",
    last_name="Doe",
    password="password1",
)

author1 = User(
    username="author1",
    email="johnDoe@booknook.io",
    first_name="John",
    last_name="Doe",
    password="password2",
    is_author=True,
)

user1 = User(
    username="nonAuthor",
    email="stephanKing@booknook.io",
    first_name="Stephan",
    last_name="King",
    password="password2",
)
