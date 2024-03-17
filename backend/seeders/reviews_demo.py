from . import Review, engine, Session, select

session = Session(engine)


def seed_reviews():
    reviews = [
        {
            "title": "Great read",
            "review_txt": "A must-read for anyone seeking wisdom and guidance in navigating life's challenges.",
            "rating": "4",
            "user_id": "1",
            "book_id": "4",
        },
        {
            "title": "It was okay",
            "review_txt": "An average read with moments of brilliance overshadowed by inconsistent pacing and underdeveloped characters.",
            "rating": "3",
            "user_id": "1",
            "book_id": "2",
        },
        {
            "title": "phenomenal",
            "review_txt": "A masterfully crafted story that lingers in the mind long after the final page",
            "rating": "4",
            "user_id": "2",
            "book_id": "1",
        },
        {
            "title": "The best book i read",
            "review_txt": "A captivating read from start to finish, with well-developed characters and an intricate plot.",
            "rating": "5",
            "user_id": "3",
            "book_id": "2",
        },
        {
            "title": "Could be better",
            "review_txt": "An average offering that may appeal to some, but ultimately left me feeling indifferent.",
            "rating": "2",
            "user_id": "4",
            "book_id": "3",
        },
    ]

    for review_data in reviews:
        review = Review(**review_data)
        session.add(review)
    session.commit()


def undo_reviews():
    reviews = session.exec(select(Review)).all()
    for review in reviews:
        session.delete(review)
    session.commit()
