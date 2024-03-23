from database import engine
from utils import set_password
from sqlmodel import Session, select
from models import User, Book, Review
from seeders.users_demo import seed_users, undo_users, session, select, User
from seeders.books_demo import seed_books, undo_books
from seeders.reviews_demo import seed_reviews, undo_reviews


# Seed database
def seed_all():
    seed_users()
    seed_books()
    seed_reviews()


# Un-seed database
def undo_seed_all():
    undo_users()
    undo_books()
    undo_reviews()
