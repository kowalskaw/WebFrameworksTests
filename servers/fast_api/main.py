import json
import uuid

from fastapi import FastAPI, Response, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_201_CREATED
from pydantic import BaseModel


app = FastAPI()

books = json.load(open('./../../data/books.json'))
templates = Jinja2Templates(directory="templates/")


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
def hello_world(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request}, status_code=HTTP_200_OK)


@app.post("/books")
def add_book(book: Book):
    global books
    book_dict = book.dict()
    book_dict['id'] = str(uuid.uuid4())
    books += [book_dict]
    return JSONResponse(content={"data": book_dict}, status_code=HTTP_201_CREATED)


@app.put("/books/{book_id}")
def update_book(book_id: str, book: Book):
    global books
    book_dict = book.dict()
    for i, book in enumerate(books):
        if book['id'] == book_id:
            books[i] = book_dict
            books[i]['id'] = book_id
            return JSONResponse(content={"data": books[i]}, status_code=HTTP_200_OK)
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.get("/books/{book_id}", status_code=200)
def read_book(book_id: str):
    for book in books:
        if book['id'] == book_id:
            return JSONResponse(content={"data": book}, status_code=HTTP_200_OK)
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.get("/books")
def read_books():
    return JSONResponse(content={"data": books}, status_code=HTTP_200_OK)


@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    global books
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            return Response(status_code=HTTP_200_OK)
    return Response(status_code=HTTP_204_NO_CONTENT)
