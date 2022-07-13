import unittest
import json
import sys
import requests
import logging


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestApi(unittest.TestCase):
    def setUp(self):
        self.uri_rest = "http://127.0.0.1:5000/books"
        self.base_body = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "author": "Rowling J.K."
        }
        self.full_body = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "author": "Rowling J.K.",
            "description": "Lil harry goes",
            "number_of_pages": 461,
            "publishment_year": "2014",
            "publishment_language": "english",
            "publisher": "Bloomsbury Publishing",
            "avaliability": False
        }

    def test_add_book_without_optional_arguments(self):
        response = requests.post(self.uri_rest, json=self.base_body)
        data = json.loads(response.text)['data']
        logging.getLogger().info(data)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(data['id'], str)
        self.assertIsNotNone(data['id'])
        self.assertEqual(data['title'], self.base_body['title'])
        self.assertEqual(data['author'], self.base_body['author'])

    def test_add_book_with_optional_arguments(self):
        response = requests.post(self.uri_rest, json=self.full_body)
        data = json.loads(response.text)['data']
        logging.getLogger().info(data)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(data['id'], str)
        self.assertIsNotNone(data['id'])
        del data['id']
        self.assertEqual(data, self.full_body)

    def test_update_book(self):
        post_response = requests.post(self.uri_rest, json=self.base_body)
        post_data = json.loads(post_response.text)['data']
        post_data['title'] = "Harry Potter 4 and the Goblet of Fire"
        put_response = requests.put(
            self.uri_rest+'/{}'.format(post_data['id']), json=post_data)
        logging.getLogger().info(put_response.text)
        put_data = json.loads(put_response.text)['data']
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(post_data['id'], put_data['id'])
        self.assertEqual(post_data['title'], put_data['title'])
        self.assertEqual(post_data['author'], put_data['author'])

    def test_get_book_by_id(self):
        post_response = requests.post(self.uri_rest, json=self.base_body)
        post_data = json.loads(post_response.text)['data']
        book_id = post_data['id']
        get_response = requests.get(self.uri_rest+'/{}'.format(book_id))
        get_data = json.loads(get_response.text)['data']
        self.base_body['id'] = book_id
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(book_id, get_data['id'])
        self.assertEqual(get_data['title'], self.base_body['title'])
        self.assertEqual(get_data['author'], self.base_body['author'])

    def test_get_all_books(self):
        get_response = requests.get(self.uri_rest)
        self.assertEqual(get_response.status_code, 200)
        get_data = json.loads(get_response.text)['data']
        self.assertIsNotNone(get_data)

    def test_delete_existing_book(self):
        post_response = requests.post(self.uri_rest, json=self.base_body)
        post_data = json.loads(post_response.text)['data']
        book_id = post_data['id']
        delete_response = requests.delete(self.uri_rest+'/{}'.format(book_id))
        self.assertEqual(delete_response.status_code, 200)
        get_response = requests.get(self.uri_rest+'/{}'.format(book_id))
        self.assertEqual(get_response.status_code, 204)
