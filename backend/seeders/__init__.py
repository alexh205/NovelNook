from seeders.users_demo import seed_users, undo_users, session, select, User
from seeders.books_demo import seed_books, undo_books


# Seed database
def seed_all():
    seed_users()
    seed_books()


# Un-seed database
def undo_seed_all():
    undo_users()
    undo_books()
