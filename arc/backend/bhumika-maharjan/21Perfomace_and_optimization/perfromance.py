from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy.orm import joinedload, selectinload, load_only
import time
from sqlalchemy import Index


DATABASE_URL = "postgresql://postgres:postgrespassword@localhost/test"


engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0, echo=False) #poolclass=QueuePool,NullPool
Base = declarative_base()


from sqlalchemy import Index

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)  
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True) 
    author_id = Column(Integer, ForeignKey("authors.id"), index=True)
    author = relationship("Author", back_populates="books")



Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


with Session(engine) as session:
    author1 = Author(name="Alice")
    author2 = Author(name="Bob")
    author3 = Author(name="Charlie")

    books = [
        Book(title="Python Basics", author=author1),
        Book(title="Advanced Python", author=author1),
        Book(title="Data Science 101", author=author2),
        Book(title="Machine Learning", author=author3),
        Book(title="Python for Data Analysis", author=author3),
    ]

    session.add_all([author1, author2, author3] + books)
    session.commit()

with Session(engine) as session:
    print("\n Filter books by author name and title containing 'Python':\n")
 #solved n+1 query problem, join for filtering, uses index for title and name, done in database
    query = session.query(Book).join(Book.author).options(selectinload(Book.author)).filter(
        Author.name == "Alice",
        Book.title.ilike("%Python%")
    )

    results = query.all()

    for book in results:
        print(f"{book.title} by {book.author.name}")