import unittest
import json
import requests


class TestApi(unittest.TestCase):
    def __init__(self):
        self.uri = "http://127.0.0.1:5000"

    def test_add_book_without_optional_arguments(self):
        body = {}
        response = requests.post(self.uri+'', json=body)
        # czy id jest stringiem, czy istnieje, czy niepuste
        # czy body odp jest równe body req
        self.assertEqual(response.status_code, 200)

    def test_add_book_with_optional_arguments(self):
        body = {}
        response = requests.post(self.uri+'', json=body)
        data = json.loads(response.content)
        # czy id jest stringiem, czy istnieje, czy niepuste
        # czy body odp jest równe body req

    # TODO
