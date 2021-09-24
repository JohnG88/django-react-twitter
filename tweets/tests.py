from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Tweet

from rest_framework.test import APIClient
# Create your tests here.

User = get_user_model()

# this is like main database
class TweetTestCase(TestCase):
    # setUp is built into tests
    def setUp(self):
        # Below are some user instances(created users)
        self.user = User.objects.create_user(username='cfe', password='somepassword')
        Tweet.objects.create(content='my first tweet', user=self.user)
        Tweet.objects.create(content='my first tweet', user=self.user)
        Tweet.objects.create(content='my first tweet', user=self.user)

    #def test_user_exists(self):
        # get user of username of cfe
        # user = User.objects.get(username='cfe')

        # check to see if username of user is cfe
        #self.assertEqual(self.user.username, 'cfe')
        
        # run for an error
        # self.assertEqual(1, 2)

    def test_tweet_created(self):
        tweet_obj = Tweet.objects.create(content='my fourth tweet', user=self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_tweet_list(self):
        # get client function above
        client = self.get_client()
        # get client from api tweets url
        response = client.get('/api/tweets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        # prints Tweet created from TweetCaseTest
        # print(response.json())

        # print(response)  is for below
        # in terminal, .<Response status_code=200, "application/json">

    def test_tweet_list(self):
        # get client function above
        client = self.get_client()
        # get client from api tweets url
        response = client.get('/api/tweets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_action_like(self):
        # get client function above
        client = self.get_client()
        # get client from api tweets url
        response = client.post('/api/tweets/action/', {'id': 1, 'action': 'like'})
        self.assertEqual(response.status_code, 200)
        print(response.json())
        # self.assertEqual(len(response.json()), 1)

    # run in terminal, py manage.py test