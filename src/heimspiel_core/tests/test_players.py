from . import APITestCase


class PlayersTestCase(APITestCase):
    def test_get_players(self):
        # Alice plays with Bob
        alice_bob = self.post("/users/", {"name": "Alice & Bob"})
        self.client.credentials(HTTP_AUTHORIZATION="Token " + alice_bob["token"])
        self.post("/players/", {"name": "Alice"})
        self.post("/players/", {"name": "Bob"})

        # Charlie plays alone
        charlie = self.post("/users/", {"name": "Charlie"})
        self.client.credentials(HTTP_AUTHORIZATION="Token " + charlie["token"])
        self.post("/players/", {"name": "Charlie"})

        # A subsequent GET for Alice & Bob returns only their two players:
        self.client.credentials(HTTP_AUTHORIZATION="Token " + alice_bob["token"])
        self.assertEqual(
            {
                "count": 2,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "attributes": [],
                        "background_story": "",
                        "id": 1,
                        "name": "Alice",
                        "score": 0,
                    },
                    {
                        "attributes": [],
                        "background_story": "",
                        "id": 2,
                        "name": "Bob",
                        "score": 0,
                    },
                ],
            },
            self.get("/players/"),
        )
