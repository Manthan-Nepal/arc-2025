from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List

app = FastAPI()

BOOKS = [{"id": i, "title": f"Book {i}"} for i in range(1, 100)]

class Book(BaseModel):
    id: int
    title: str

class PaginatedBooks(BaseModel):
    total: int
    page: int
    size: int
    pages: int
    books: List[Book]

@app.get("/books", response_model=PaginatedBooks)
def get_books(
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=20)
):
    total = len(BOOKS)
    pages = (total + size - 1) // size
    start = (page - 1) * size
    end = start + size
    return {
        "total": total,
        "page": page,
        "size": size,
        "pages": pages,
        "books": BOOKS[start:end]
    }
