import random

from django.db import models

# Another approach of getting User model
from django.conf import settings


# Create your models here.

# Then get User model
User = settings.AUTH_USER_MODEL

# In shell to check for queries of user's username, use __(double underscore) ex.) qs = Tweet.objects.filter(user__username__iexact='John'), (username is the field name), (iexact means John and JOHN are the same)

class Tweet (models.Model):
    # setting null=True and on_delete=models.SET_NULL, will still have data, have history, backup in database
    # learn how to backup database 
    user = models.ForeignKey(User, on_delete=models.CASCADE)# many users can have many tweets
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