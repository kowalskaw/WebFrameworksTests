from fastapi import FastAPI
from pydantic import BaseModel
import json
import uuid

app = FastAPI()

books = json.load(open('./../../data/books.json'))


class Book(BaseModel):
    id: str = None
    title: str
    author: str
    description: str = None
    number_of_pages: int = None
    publishment_year: str = None
    publishment_language: str = None
    publisher: str = None
    avaliability: bool = None


@app.get("/")
def hello_world():
    return {"Hello": "World"}  # TODO return html page


@app.post("/books")
def add_book(book: Book):
    global books
    book_dict = book.dict()
    book_dict['id'] = uuid.uuid4()
    books += [book_dict]
    return {"data": book_dict}


@app.put("/books/{book_id}")
def update_book(book_id: str, book: Book):
    global books
    book_dict = book.dict()
    for i, book in enumerate(books):
        if str(book['id']) == book_id:
            books[i] = book_dict
            books[i]['id'] = book_id
            return {"data": books[i]}


@app.get("/books/{book_id}")
def read_book(book_id: str):
    for book in books:
        if book['id'] == book_id:
            return {"data": book}


@app.get("/books")
def read_books():
    return {"data": books}


@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    global books
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            return book
