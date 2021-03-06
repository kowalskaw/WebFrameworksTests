from flask import Flask, render_template, request, jsonify, make_response, Response
import json
import uuid

app = Flask(__name__)


books = json.load(open('./../../data/books.json'))


def build_response(data={}, status_code=204):
    return make_response(
        jsonify(
            {
                'data': data,
                'mimetype': 'application/json'
            }
        ), status_code
    )


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/books', methods=['POST'])
def add_book():
    global books
    book_dict = request.get_json()
    book_dict['id'] = str(uuid.uuid4())
    books += [book_dict]
    print(book_dict)
    return build_response(book_dict, 201)


@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    global books
    body = request.get_json()
    for i, book in enumerate(books):
        if book['id'] == book_id:
            books[i] = body
            books[i]['id'] = book_id
            return build_response(books[i], 200)
    return Response(status=204)


@app.route('/books', methods=['GET'])
def read_books():
    return build_response(books, 200)


@app.route('/books/<book_id>', methods=['GET'])
def read_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return build_response(book, 200)
    return Response(status=204)


@app.route('/books/<book_id>', methods=['DELETE'])
def delte_book(book_id):
    global books
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            return Response(status=200)
    return Response(status=204)
