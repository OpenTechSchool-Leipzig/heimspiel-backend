import json
from contextlib import contextmanager

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

    def set_auth_token(self, token):
        if token:
            self.client.credentials(HTTP_AUTHORIZATION="Token " + token)
        else:
            self.client.credentials()

    @contextmanager
    def auth_token(self, token):
        self.set_auth_token(token)
        yield
        self.set_auth_token(None)
