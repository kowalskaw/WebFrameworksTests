import falcon
import json
import uuid


class Books:
    def __init__(self):
        self.books = json.load(open('./../data/books.json'))

    def on_post(self, req, resp):
        data = req.stream.read()
        book_dict = json.loads(data)
        book_dict['id'] = str(uuid.uuid4)
        self.books += [book_dict]
        resp.status = falcon.HTTP_201
        resp.text = json.dumps({"data": book_dict})

    def on_put_by_id(self, req, resp, book_id):
        data = req.stream.read()
        book_dict = json.loads(data)
        for i, book in enumerate(self.books):
            if book['id'] == book_id:
                self.books[i] = book_dict
                self.books[i]['id'] = book_id
                resp.text = json.dumps({"data": self.books[i]})
                resp.status = falcon.HTTP_200

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.text = json.dumps({"data": self.books})

    # cannot return other response when invalid
    def on_get_by_id(self, req, resp, book_id):
        for book in self.books:
            if book['id'] == book_id:
                resp.text = json.dumps({"data": book})
                resp.status = falcon.HTTP_200

    def on_delete_by_id(self, req, resp, book_id):
        for i, book in enumerate(self.books):
            if book['id'] == book_id:
                del self.books[i]
                resp.status = falcon.HTTP_200
