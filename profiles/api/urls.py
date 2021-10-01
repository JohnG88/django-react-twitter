from django.urls import path

from .views import user_follow_view

'''
    CLIENT
    Base ENDPOOINT /api/profiles/ 
'''

urlpatterns = [
    path('', user_follow_view),
]

urlpatterns = [
    path('<str:username>/follow/', user_follow_view),
]