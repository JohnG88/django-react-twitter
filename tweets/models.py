import random

from django.db import models

# Create your models here.

class Tweet (models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # reverse ascending order to descending order by id, created, etc...
    # makemigrations and migrate when doing anything with class
    class Meta:
        ordering = ['-created']

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'created': self.created.strftime("%m-%d-%Y, %H:%M:%S"),
            'likes': random.randint(0, 1000),
        }