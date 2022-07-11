from locust import HttpUser, task, between
import time
import json


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/")

    @task
    def get_book_by_id(self):
        ids = [1, 2]
        for i in range(len(ids)):
            self.client.get(f"/books/{ids[i]}", name="/books")

    @task
    def get_all_books(self):
        self.client.get(f"/books")

    @task
    def post_book(self):
        self.client.post(
            f"/books", json={'title': 'Another book', 'author': 'anonymous'})

    @task
    def update_book(self):
        available_books = json.loads(
            self.client.get(f"/books").content.decode('utf-8'))['data']
        print(available_books)
        if(available_books):
            book_id = available_books[0]['id']
            body = {'title': 'new title {}'.format(
                book_id), 'author': 'new author {}'.format(book_id)}
            self.client.put(f"/books/{book_id}", name="/books", json=body)

    @task
    def delete_book(self):
        available_books = json.loads(
            self.client.get(f"/books").content.decode('utf-8'))['data']
        print(available_books)
        if(available_books):
            book_id = available_books[0]['id']
            self.client.delete(f"/books/{book_id}", name='/books')
