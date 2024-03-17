from . import Book, engine, Session, select

session = Session(engine)

def seed_books():

    books = [
        {
            "title": "Unleash Your Potential: A Guide to Self-Discovery and Growth",
            "publication_year": "2013",
            "genre": "Self-help",
            "description": "Guide to unlocking your potential",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "author_id": "1",
        },
        {
            "title": "Software Architecture Patterns: Building Scalable and Maintainable Systems",
            "publication_year": "2018",
            "genre": "Non-fiction",
            "description": "Building patterns to manage scalable and maintainable systems",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "author_id": "2",
        },
        {
            "title": "Test-Driven Development: By Example",
            "publication_year": "2021",
            "genre": "Non-fiction",
            "description": "Test to perfection",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "author_id": "3",
        },
        {
            "title": "The Art of Self-Confidence: Overcoming Doubt and Embracing Your True Self",
            "publication_year": "2023",
            "genre": "Self-help",
            "description": "Embracing Your Authenticity: The Mastery of Self-Confidence Through Overcoming Doubt and Nurturing Your True Self",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "author_id": "2",
        },
        {
            "title": "Refactoring: Improving the Design of Existing Code",
            "publication_year": "2022",
            "genre": "Non-fiction",
            "description": "Revitalizing Software Design: A Comprehensive Guide to Enhancing Existing Code through the Art of Refactoring",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "author_id": "1",
        },
        {
            "title": "Financial Freedom: Strategies for Building Wealth and Security",
            "publication_year": "2019",
            "genre": "Self-help",
            "description": "Build a life long wealth",
            "cover_image": "https://plus.unsplash.com/premium_photo-1674727219390-5953cefb3cd9?q=80&w=2389&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "author_id": "3",
        },
        {
            "title": "Babel",
            "publication_year": "2022",
            "genre": "Fantasy fiction",
            "description": "From award-winning author R. F. Kuang comes Babel, a historical fantasy epic that grapples with student revolutions, colonial resistance, and the use of language and translation as the dominating tool of the British Empire.",
            "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1677361825i/57945316.jpg",
            "author_id": "4"
        },
        {
            "title": "The Goldfinch",
            "publication_year": "2013",
            "genre": "Literary fiction",
            "description": "Winner of the Pulitzer Prize for Fiction 2014. Aged thirteen, Theo Decker, son of a devoted mother and a reckless, largely absent father, survives an accident that otherwise tears his life apart. Alone and rudderless in New York, he is taken in by the family of a wealthy friend. He is tormented by an unbearable longing for his mother, and down the years clings to the thing that most reminds him of her: a small, strangely captivating painting that ultimately draws him into the criminal underworld. As he grows up, Theo learns to glide between the drawing rooms of the rich and the dusty antiques store where he works. He is alienated and in love - and his talisman, the painting, places him at the centre of a narrowing, ever more dangerous circle. The Goldfinch is a haunted odyssey through present-day America and a drama of enthralling power. Combining unforgettably vivid characters and thrilling suspense, it is a beautiful, addictive triumph - a sweeping story of loss and obsession, of survival and self-invention, of the deepest mysteries of love, identity and fate.",
            "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1378710146i/17333223.jpg",
            "author_id": "5"
        },
        {
            "title": "Nectar in a Sieve",
            "publication_year": "1954",
            "genre": "Semi-autobiographical",
            "description": "Married as a child bride to a tenant farmer she never met, Rukmani works side by side in the field with her husband to wrest a living from a land ravaged by droughts, monsoons, and insects. With remarkable fortitude and courage, she meets changing times and fights poverty and disaster.",
            "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1348811536i/101509.jpg",
            "author_id": "6"
        }
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
