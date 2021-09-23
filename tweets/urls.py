from django.urls import path

from .views import home_view, tweet_detail_view, tweet_list_view, tweet_create_view, tweet_delete_view, tweet_action_view

'''
    CLIENT
    Base ENDPOOINT /api/tweets/ (how url will start off, then add the paths below to find which path you want to reference)
    Ex. http://127.0.0.1:8000/api/tweets/30/delete/
'''

urlpatterns = [
    path('', tweet_list_view),
    path('action/', tweet_action_view),
    path('create/', tweet_create_view),
    path('<int:id>/', tweet_detail_view),
    path('<int:id>/delete/', tweet_delete_view),
]
