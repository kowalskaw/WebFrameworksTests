import falcon

from .books import Books
from .home import Home


def create_app():
    books = Books()
    home = Home()
    app = falcon.App()
    app.add_route('/', home)
    app.add_route('/books/{book_id}', books, suffix='by_id')
    app.add_route('/books', books)

    return app
