import falcon
import json
import uuid


class Books:
    def __init__(self):
        self.books = json.load(open('./../data/books.json'))

    def on_get_index(self, req, resp):
        resp.status = falcon.HTTP_200
        with open('./templates/index.html', 'r') as f:
            resp.body = f.read()

    def on_post(self, req, resp):
        data = req.stream.read()
        book_dict = json.loads(data)
        book_dict['id'] = str(uuid.uuid4)
        self.books += [book_dict]
        resp.status = falcon.HTTP_201
        resp.text = json.dumps({"data": book_dict})

    # put

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.text = json.dumps({"data": self.books})

    # cannot return other response when invalid
    def on_get_by_id(self, req, resp, book_id):
        for book in self.books:
            if book['id'] == book_id:
                resp.body = json.dumps({"data": book})
                resp.status = falcon.HTTP_200

    # delete
