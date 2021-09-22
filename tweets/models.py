import random

from django.db import models

# Another approach of getting User model
from django.conf import settings


# Create your models here.

# Then get User model
User = settings.AUTH_USER_MODEL

# historical measure like
# createred a new table of TweetLike
# this through table is created just to be able to use timestamp
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Have to use 'Tweet', because tweet model is below TweetLike
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# In shell to check for queries of user's username, use __(double underscore) ex.) qs = Tweet.objects.filter(user__username__iexact='John'), (username is the field name), (iexact means John and JOHN are the same)

class Tweet (models.Model):
    # setting null=True and on_delete=models.SET_NULL, will still have data, have history, backup in database
    # learn how to backup database 
    user = models.ForeignKey(User, on_delete=models.CASCADE)# many users can have many tweets
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through='TweetLike' )
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # reverse ascending order to descending order by id, created, etc...
    # makemigrations and migrate when doing anything with class
    class Meta:
        ordering = ['-created']

    # def __str__(self):
        # return self.content

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'created': self.created.strftime("%m-%d-%Y, %H:%M:%S"),
            'likes': random.randint(0, 1000),
        }

    '''
        When adding user model and then creating superuser, python gives me, "Trying to add a non-nullable field 'user', can add null=True, or in our case can add 1, since we are only user create so far, need to learn how to do this better"
    '''

'''
    In shell created:
        obj = Tweet.objects.first()
        - can use this because of many to many field
        obj.likes.all()
        - gives a queryset of []

    - To get User
        >>> from django.contrib.auth import get_user_model
        >>> User = get_user_model()
        >>> User.objects.all()
        <QuerySet [<User: John>]>

    - To add a User to obj.likes
        >>> me = User.objects.first()
        >>> me
        <User: John>
        >>> obj.likes.add(me)
        >>> obj.likes.all()
        <QuerySet [<User: John>]>

    - To remove User from obj.likes
        obj.likes.remove(me)

        obj.likes.all()
        QuerySet = []

    - Add multiple User's that liked
        >>> qs = User.objects.all()
        >>> obj.likes.set(qs)
        >>> obj.likes.all()
        <QuerySet [<User: John>]>

    - To add data to user and tweet fields in TweetLike
        >>> TweetLike.objects.create(user=me, tweet=obj)
        <TweetLike: TweetLike object (5)>
        >>> obj.likes.all()
        <QuerySet [<User: John>]>

    - To remove users
        >>> obj.likes.add(me)
        >>> obj.likes.all()
        <QuerySet [<User: John>]>
        >>> empty_users = User.objects.none()
        >>> empty_users
        <QuerySet []>
        >>> obj.likes.set(empty_users)
        >>> obj.likes.all()
        <QuerySet []>
'''