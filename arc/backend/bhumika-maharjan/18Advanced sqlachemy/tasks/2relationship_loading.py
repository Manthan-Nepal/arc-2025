from sqlalchemy import create_engine, ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    books: Mapped[List["Book"]] = relationship(back_populates="author", lazy="joined") 
    # "select", "joined", "noload"


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="books")

engine = create_engine("postgresql://postgres:postgrespassword@localhost/test3")

Base.metadata.create_all(engine)


# with Session(engine) as session:
#     author1 = Author(name="Author A", books=[
#         Book(title="Book A1"), Book(title="Book A2")
#     ])
#     author2 = Author(name="Author B", books=[
#         Book(title="Book B1"), Book(title="Book B2")
#     ])
#     session.add_all([author1, author2])
# session.commit()


with Session(engine) as session:
    authors = session.query(Author).all()
    for author in authors:
        print(f"\nAuthor: {author.name}")
        for book in author.books:
            print(f"  Book: {book.title}")
