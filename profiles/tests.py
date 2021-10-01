from django.test import TestCase

# Create your tests here.
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe', password='somepassword')
        self.userb = User.objects.create_user(username='cfe-2', password='somepassword2')
    
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
