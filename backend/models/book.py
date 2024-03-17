from typing import Optional
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine


class Book(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    title: str = Field(max_length=50, nullable=False)
    publication_year: str
    genre: str
    description: str = Field(max_length=180)
    cover_image: str
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    # author_id ?

    class Config:
        from_attributes = True


book_1 = Book(title="Babel", publication_year="2022", genre="Fantasy fiction", description="From award-winning author R. F. Kuang comes Babel, a historical fantasy epic that grapples with student revolutions, colonial resistance, and the use of language and translation as the dominating tool of the British Empire.", cover_image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1677361825i/57945316.jpg")
book_2 = Book(title="The Goldfinch", publication_year="2013", genre="Literary fiction", description="Winner of the Pulitzer Prize for Fiction 2014. Aged thirteen, Theo Decker, son of a devoted mother and a reckless, largely absent father, survives an accident that otherwise tears his life apart. Alone and rudderless in New York, he is taken in by the family of a wealthy friend. He is tormented by an unbearable longing for his mother, and down the years clings to the thing that most reminds him of her: a small, strangely captivating painting that ultimately draws him into the criminal underworld. As he grows up, Theo learns to glide between the drawing rooms of the rich and the dusty antiques store where he works. He is alienated and in love - and his talisman, the painting, places him at the centre of a narrowing, ever more dangerous circle. The Goldfinch is a haunted odyssey through present-day America and a drama of enthralling power. Combining unforgettably vivid characters and thrilling suspense, it is a beautiful, addictive triumph - a sweeping story of loss and obsession, of survival and self-invention, of the deepest mysteries of love, identity and fate.", cover_image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1378710146i/17333223.jpg")
book_3 = Book(title="Nectar in a Sieve", publication_year="1954", genre="Semi-autobiographical", description="Married as a child bride to a tenant farmer she never met, Rukmani works side by side in the field with her husband to wrest a living from a land ravaged by droughts, monsoons, and insects. With remarkable fortitude and courage, she meets changing times and fights poverty and disaster.", cover_image="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1348811536i/101509.jpg")


engine = create_engine("sqlite:///database.db")


SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(book_1)
    session.add(book_2)
    session.add(book_3)
    session.commit()