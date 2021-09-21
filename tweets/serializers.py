from rest_framework import serializers
from .models import Tweet
# to get max_length from settings.py(we added it to settings.py)
from django.conf import settings
MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']
        # fields = ['id', 'user', 'content', 'image', 'created']

    # to validate data
    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError('This tweet is too long')
        return value