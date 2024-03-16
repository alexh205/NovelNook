from sqlalchemy import Select
from models import Book
from database import engine
from sqlmodel import Session, select


session = Session(engine)


def seed_books():

    books = [
        {
            "title": "Unleash Your Potential: A Guide to Self-Discovery and Growth",
            "publication_year": "2013",
            "genre": "Self-help",
            "description": "Guide to unlocking your potential",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
        {
            "title": "Software Architecture Patterns: Building Scalable and Maintainable Systems",
            "publication_year": "2018",
            "genre": "Non-fiction",
            "description": "Building patterns to manage scalable and maintainable systems",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
        {
            "title": "Test-Driven Development: By Example",
            "publication_year": "2021",
            "genre": "Non-fiction",
            "description": "Test to perfection",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
        {
            "title": "The Art of Self-Confidence: Overcoming Doubt and Embracing Your True Self",
            "publication_year": "2023",
            "genre": "Self-help",
            "description": "Embracing Your Authenticity: The Mastery of Self-Confidence Through Overcoming Doubt and Nurturing Your True Self",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
        {
            "title": "Refactoring: Improving the Design of Existing Code",
            "publication_year": "2022",
            "genre": "Non-fiction",
            "description": "Revitalizing Software Design: A Comprehensive Guide to Enhancing Existing Code through the Art of Refactoring",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
        {
            "title": "Financial Freedom: Strategies for Building Wealth and Security",
            "publication_year": "2019",
            "genre": "Self-help",
            "description": "Build a life long wealth",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        },
    ]

    for book_data in books:
        book = Book(**book_data)
        session.add(book)
    session.commit()


def undo_books():
    books = session.exec(select(Book)).all()
    for book in books:
        session.delete(book)
    session.commit()
