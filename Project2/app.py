from fastapi import FastAPI, HTTPException, Path, Query
from models.book import Book
from requests.book_request import BookRequest
from starlette import status

app = FastAPI()

BOOKS = [
    Book(id=1, title="Book 1", author="Author 1"),
    Book(id=2, title="Book 2", author="Author 2"),
    Book(id=3, title="Book 3", author="Author 3"),
    Book(id=4, title="Book 4", author="Author 1"),
    Book(id=5, title="Book 5", author="Author 1"),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books(
    author=Query(
        None,
        regex="^[a-zA-Z\\s]+$",
        min_length=4,
        max_length=50,
        description="Filter books by author name",
    ),
):
    if author:
        return list(filter(lambda x: x.author.lower() == author.lower(), BOOKS))
    return BOOKS


@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def get_book(id: int = Path(gt=0)):
    book = next((book for book in BOOKS if book.id == id), None)

    if not (book):
        raise HTTPException(status_code=404, detail="Book not found")

    return book


# Post a new book
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def add_book(book_request: BookRequest):
    book_request.id = get_book_id()
    BOOKS.append(Book(**book_request.model_dump()))
    return book_request


def get_book_id():
    return len(BOOKS) == 0 and 1 or BOOKS[-1].id + 1
