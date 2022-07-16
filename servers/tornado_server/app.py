import asyncio
import tornado.web
import json
import uuid

books = json.load(open('./../../data/books.json'))


class BooksHandler(tornado.web.RequestHandler):
    def post(self):
        # create book
        global books
        book_dict = json.loads(self.request.body)
        book_dict['id'] = str(uuid.uuid4())
        books += [book_dict]
        self.set_status(201)
        self.write({"data": book_dict})

    def put(self):
        global books
        book_id = self.request.path.split(sep='/')[2]
        book_dict = json.loads(self.request.body)
        for i, book in enumerate(books):
            if book['id'] == book_id:
                books[i] = book_dict
                books[i]['id'] = book_id
                self.set_status(200)
                self.write({"data": book_dict})

    def get(self):
        if(len(self.request.path.split(sep='/')) < 3):
            # all books
            self.set_status(200)
            self.write({"data": books})
        else:
            # one book
            book_id = self.request.path.split(sep='/')[2]
            for book in books:
                if book['id'] == book_id:
                    self.set_status(200)
                    self.write({"data": book})

    def delete(self):
        global books
        found = False
        book_id = self.request.path.split(sep='/')[2]
        for i, book in enumerate(books):
            if book['id'] == book_id:
                found = True
                del books[i]
        self.set_status(200) if found else self.set_status(204)


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html")
        self.render('templates/index.html')


def make_app():
    return tornado.web.Application([
        (r"/", HomeHandler),
        (r"/books", BooksHandler),
        (r"/books/[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}", BooksHandler)
    ])


async def main():
    app = make_app()
    app.listen(8000)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
