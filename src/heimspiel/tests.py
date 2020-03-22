import json

from django.test import Client, TestCase
from rest_framework.authtoken.models import Token


class StoryTestCase(TestCase):
    fixtures = ['sample-data.json']

    def setUp(self):
        self.client = Client()

    def test_default_story(self):
        """Covers the intended use if the API in a narrative way."""
        self.maxDiff = None

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
        self.assertEqual(4, attributes['count'])
        self.assertEqual({
            'name': 'Sportskanone',
            'url': 'http://testserver/playerattributes/1/',
        } , attributes['results'][0])

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
        self.assertEqual({
            'url': 'http://testserver/quests/1/',
            'category': 'http://testserver/questcategories/chores/',
            'title': 'Es war der Gärtner',
            'text': ('Gieße heimlich alle eure Pflanzen. Gib dich erst als '
                     'der geheime Gärtner zu erkennen,wenn es dir unendeckt '
                     'gelungen ist.'),
            'flavor_text': '',
            'score': 3,
            'image': 'http://testserver/media/filer_public/25/37/25376126-e33e-46ca-b2b4-ea124c279d48/gardener.jpg',
        }, quests['results'][0])

        # After a hard day of doing chores, the group returns and submits a
        # score report to find out which badges they've earned. In order to do
        # that, they need to enter their score in each quest category. The
        # quest categories can be queried like this:
        categories = self.get('/questcategories/')
        self.assertEqual(6, categories['count'])
        self.assertEqual({
            'url': 'http://testserver/questcategories/activity/',
            'title': 'Beschäftigung',
            'image': 'http://testserver/media/filer_public/c3/1f/c31f700d-fb3d-45d3-b293-ca35ca324b5f/activity.jpg',
        }, categories['results'][0])

        result = self.post('/scorereports/', {
            'user': user['url'],
            'date': '2020-03-22T17:00:00Z',
            'report': [
                {
                    'player': alice['url'],
                    'category_scores': [
                        { 'category': categories['results'][0]['url'],
                          'score': 42 },
                        { 'category': categories['results'][3]['url'],
                          'score': 2 },
                    ]
                },
                {
                    'player': bob['url'],
                    'category_scores': [
                        { 'category': categories['results'][0]['url'],
                          'score': 10 },
                    ]
                },
            ],
        })
        self.assertEqual(54, result['new_scores']['user'])
        self.assertEqual([], result['earned_badges']['user'])

    def get(self, url):
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        return response.json()

    def post(self, url, data):
        response = self.client.post(url, json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(201, response.status_code)
        return response.json()
