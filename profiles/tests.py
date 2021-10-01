from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
from .models import Profile
from django.contrib.auth import get_user_model

# if you get this error in testing just text, check url
# ValueError: Content-Type header is "text/html; charset=utf-8", not "application/json"

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe', password='somepassword')
        self.userb = User.objects.create_user(username='cfe-2', password='somepassword2')

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client
    
    # checking to see how many profiles are created
    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_following(self):
        first = self.user
        second = self.userb
        # add second profile into followers field
        first.profile.followers.add(second)
        second_user_following_whom = second.following.all()
        # checking to see if user is being followed
        qs = second.following.filter(user=first)
        self.assertTrue(qs.exists())
        # first user should follow no one
        first_user_following_no_one = first.following.all()
        self.assertFalse(first_user_following_no_one.exists())

    def test_follow_api_endpoint(self):
        # get client function above
        client = self.get_client()
        # get client from api tweets url
        response = client.post(f"/api/profiles/{self.userb.username}/follow/", {"action": "follow"})
        count = response.json().get("count")
        # r_data = response.json()
        # count = r_data.get("count")
        self.assertEqual(count, 1)

    def test_unfollow_api_endpoint(self):
        first = self.user
        second = self.userb
        # add second profile into followers field
        first.profile.followers.add(second)

        # get client function above
        client = self.get_client()
        # get client from api tweets url
        response = client.post(f"/api/profiles/{self.userb.username}/follow/", {"action": "unfollow"})
        count = response.json().get("count")
        # r_data = response.json()
        # count = r_data.get("count")
        self.assertEqual(count, 0)

    def test_cannot_follow_api_endpoint(self):
        # get client function above
        client = self.get_client()
        # get client from api tweets url
        response = client.post(f"/api/profiles/{self.user.username}/follow/", {"action": "follow"})
        count = response.json().get("count")
        # r_data = response.json()
        # count = r_data.get("count")
        self.assertEqual(count, 0)