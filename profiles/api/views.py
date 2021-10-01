from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponse
from django.http.response import Http404, JsonResponse
from django.shortcuts import render, redirect


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


from ..models import Profile
import random

User = get_user_model()
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

# @api_view(['POST'])
# @permission_classes(([IsAuthenticated]))
# def user_profile_view(request, *args, **kwargs):
#     current_user = request.user
#     to_follow_user = 

#     return Response({}, status=200)

@api_view(['GET', 'POST'])
@permission_classes(([IsAuthenticated]))
def user_follow_view(request, username, *args, **kwargs):
    me = request.user
    other_user_qs = User.objects.filter(username=username)
    
    # to not follow yourself, and if user tries to follow themselves then just return user's followers
    if me.username == username:
        my_followers = me.profile.followers.all()
        return Response({'count': my_followers.count()}, status=200)

    # can also use line below for same qs
    # profile = Profile.objects.filter(user__username=username).first()
    if not other_user_qs.exists():
        return Response({}, status=404)
    other = other_user_qs.first()
    profile = other.profile
    # simple toggle, if me in profile.followers then remove else if not add
    # if me in profile.followers.all():
    #     profile.followers.remove(me)
    # else:
    #     profile.followers.add(me)

    # adjusting above in case a server is interruption, and a user clicks button multiple times, we want the button to designate the action, same as we did with like button with tweets
    data = request.data or {}
    # instead of using try block you can also use line above
    # try:
    #     data = request.data
    # except:
    #     pass
    print(data)
    action = data.get('action')
    if action == 'follow':
        profile.followers.add(me)
    elif action == 'unfollow':
        profile.followers.remove(me)
    else:
        pass
    current_followers_qs = profile.followers.all()
    return Response({'count': current_followers_qs.count()}, status=200)

