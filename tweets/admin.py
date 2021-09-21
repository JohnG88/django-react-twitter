from django.contrib import admin
from .models import Tweet
# Register your models here.

# This created searchbox in Tweets in django Admin(searches for username and email)
class TweetAdmin(admin.ModelAdmin):
    # Line below creates a display for user and content in Tweet in django admin
    # __str__ is showing in Tweet in django admin Tweet object(37), in models.py can change __str__ to something else( check out def __str__ in models.py) aka string representation of object
    list_display = ['__str__', 'user', 'content']
    search_fields = ['user__username', 'user__email']
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetAdmin)