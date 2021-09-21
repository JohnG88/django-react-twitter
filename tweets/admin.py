from django.contrib import admin
from .models import Tweet
# Register your models here.

# This created searchbox in Tweets in django Admin(searches for username and email)
class TweetAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email']
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetAdmin)