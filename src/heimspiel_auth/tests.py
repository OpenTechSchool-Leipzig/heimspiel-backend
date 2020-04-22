import uuid
from unittest.mock import patch

from rest_framework.authtoken.models import Token
from heimspiel_core.tests import APITestCase

from .serializers import UserSerializer

SAMPLE_UUID = uuid.uuid4()


class AuthTestCase(APITestCase):
    @patch("uuid.uuid4", lambda: SAMPLE_UUID)
    def test_create_user(self):
        """Creates a user with a new UUID and an authentication token."""
        user = UserSerializer().create({})
        self.assertEqual(SAMPLE_UUID, user.pk)  # also ensures it's persisted
        self.assertEqual(SAMPLE_UUID, user.username)
        self.assertEqual("", user.password)
        self.assertEqual(1, Token.objects.filter(user=user).count())

    def test_create_user_with_name(self):
        user = UserSerializer().create({"name": "Heimspiel"})
        self.assertEqual("Heimspiel", user.name)

    def test_post_user_id_gets_ignored(self):
        """IDs are always generated server-side."""
        our_id = uuid.uuid4()
        body = self.post("/users/", {"id": str(our_id), "name": "Heimspiel"})
        self.assertNotEqual(body["id"], our_id)

    def test_post_user_returns_token(self):
        response = self.client.post("/users/", {"name": "Heimspiel"})
        body = response.json()
        token = Token.objects.get(user_id=body["id"])
        self.assertEqual(body["token"], token.key)
        # we manipulate the response's content, just to be sure:
        self.assertEqual(response["content-length"], str(len(response.content)))

    def test_get_users_with_auth_returns_only_current_user(self):
        self.post("/users/", {"name": "Alice"})
        bob = self.post("/users/", {"name": "Bob"})
        with self.auth_token(bob["token"]):
            self.assertEquals(
                {
                    "count": 1,
                    "next": None,
                    "previous": None,
                    "results": [{"id": str(bob["id"]), "name": "Bob"},],
                },
                self.get("/users/"),
            )

    def test_get_users_without_auth_returns_no_users(self):
        self.assertEquals(
            {"count": 0, "next": None, "previous": None, "results": [],},
            self.get("/users/"),
        )
