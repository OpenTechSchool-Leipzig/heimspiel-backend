import json

import django
from rest_framework.test import APIClient


class APITestCase(django.test.TestCase):
    def setUp(self):
        self.client = APIClient()

    def get(self, url):
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        return response.json()

    def post(self, url, data):
        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(
            201, response.status_code, response.content,
        )
        return response.json()
