from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 12.99,
        "category": "Fiction",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "price": 14.99,
        "category": "Fiction",
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "price": 11.99,
        "category": "Science Fiction",
    },
    {
        "id": 4,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "price": 15.99,
        "category": "Fantasy",
    },
    {
        "id": 5,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "price": 9.99,
        "category": "Romance",
    },
    {
        "id": 6,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "price": 10.99,
        "category": "Fiction",
    },
    {
        "id": 7,
        "title": "Dune",
        "author": "Frank Herbert",
        "price": 18.99,
        "category": "Science Fiction",
    },
    {
        "id": 8,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "price": 13.99,
        "category": "Philosophical Fiction",
    },
    {
        "id": 9,
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "price": 16.99,
        "category": "Non-Fiction",
    },
    {
        "id": 10,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "price": 19.99,
        "category": "Fantasy",
    },
]


@app.get("/")
async def root():
    return {"message": "Hello World updated"}


@app.get("/books")
async def get_books(category: str = ""):
    if category == "":
        return BOOKS

    return [book for book in BOOKS if book.get("category").lower() == category.lower()]


@app.get("/books/{id}")
async def get_book(id: int):
    for book in BOOKS:
        if book.get("id") == id:
            return book
    return {"message": "Book not found"}


@app.post("/books")
async def add_book(book: dict):
    BOOKS.append(book)
    return {"message": "Book added"}


@app.put("/books/{id}")
async def update_book(id: int, book: dict):
    for i, b in enumerate(BOOKS):
        if b.get("id") == id:
            BOOKS[i] = book
            return {"message": "Book updated"}
    return {"message": "Book not found"}


@app.delete("/books/{id}")
async def delete_book(id: int):
    for i, b in enumerate(BOOKS):
        if b.get("id") == id:
            del BOOKS[i]
            return {"message": "Book deleted"}
    return {"message": "Book not found"}
