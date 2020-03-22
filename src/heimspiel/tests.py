from django.test import Client, TestCase
from rest_framework.authtoken.models import Token


class StoryTestCase(TestCase):
    fixtures = ['sample-data.json']

    def setUp(self):
        self.client = Client()

    def test_default_story(self):
        """Covers the intended use if the API in a narrative way."""
        # A new family / group of friends "registers" on the website to start
        # playing. They provide a name for their team and receive a user id and
        # an authentication token, which will be encoded in a URL they can used
        # to play:
        user = self.post('/users/', {'name': 'Heimspiel'})
        self.assertTrue('url' in user)
        self.assertTrue('token' in user)

        # In order to add players, the client needs to know about available
        # attributes:
        attributes = self.get('/playerattributes/')
        self.assertEqual(2, attributes['count'])
        self.assertEqual([
            {
                'name': 'Haven of tranquility',
                'url': 'http://testserver/playerattributes/1/',
            },
            {
                'name': 'Need for movement',
                'url': 'http://testserver/playerattributes/2/',
            },
        ], attributes['results'])

        # The group consists of two players: Alice and Bob. For each player the
        # clients post its name and attributes:
        alice = self.post('/players/', {
            'user': user['url'],
            'name': 'Alice',
            'attributes': [attributes['results'][0]['url']],
        })
        bob = self.post('/players/', {
            'user': user['url'],
            'name': 'Bob',
            'attributes': [attributes['results'][1]['url']],
        })

        # Let the game begin! The client will show available quests to the
        # group. The decision who will tackle which quest is left to them in
        # the analogue world.
        quests = self.get('/quests/')
        self.assertEqual(2, quests['count'])
        self.assertEqual([
            {
                'url': 'http://testserver/quests/1/',
                'category': 'http://testserver/questcategories/relationships/',
                'title': 'Call a friend',
                'text': '',
                'flavor_text': '',
                'score': 1,
            },
            {
                'url': 'http://testserver/quests/2/',
                'category': 'http://testserver/questcategories/health/',
                'title': 'Run!',
                'text': 'Go running for 20 minutes (alone).',
                'flavor_text': '',
                'score': 3,
            }], quests['results'])

    def get(self, url):
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        return response.json()

    def post(self, url, data):
        response = self.client.post(url, data)
        self.assertEqual(201, response.status_code)
        return response.json()
