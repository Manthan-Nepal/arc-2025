from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI()

BOOKS = [{"id": i, "title": f"Book {i}"} for i in range(1, 100)]
AUTHORS = [{"id": i, "name": f"Author {i}"} for i in range(1, 50)]

class Book(BaseModel):
    id: int
    title: str
    
class Author(BaseModel):
    id: int
    name: str

class PaginatedBooks(BaseModel):
    total: int
    page: int
    size: int
    pages: int
    books: List[Book]

class PaginatedAuthors(BaseModel):
    total: int
    page: int
    size: int
    pages: int
    authors: List[Author]

class Pagination:
    def __init__(
        self,
        page: int = Query(1, ge=1),
        size: int = Query(5, ge=1, le=20),
    ):
        self.page = page
        self.size = size


@app.get("/books", response_model=PaginatedBooks)
def get_books(   pagination: Pagination = Depends()):
    total = len(BOOKS)
    pages = (total + pagination.size - 1) // pagination.size
    start = (pagination.page - 1) * pagination.size
    end = start + pagination.size
    return {
        "total": total,
        "page": pagination.page,
        "size": pagination.size,
        "pages": pages,
        "books": BOOKS[start:end]
    }

@app.get("/authors", response_model=PaginatedAuthors)
def get_authors(pagination: Pagination = Depends()):
    total = len(AUTHORS)
    pages = (total + pagination.size - 1) // pagination.size
    start = (pagination.page - 1) * pagination.size
    end = start + pagination.size
    return {
        "total": total,
        "page": pagination.page,
        "size": pagination.size,
        "pages": pages,
        "authors": AUTHORS[start:end]
    }
