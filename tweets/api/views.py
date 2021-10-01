from django.http.response import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from ..models import Tweet
from ..forms import TweetForm
from ..serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer

import random

# Create your views here.

@api_view(['POST']) #http method the client == POST
@permission_classes(([IsAuthenticated]))
#@authentication_classes([SessionAuthentication])
def tweet_create_view(request, *args, **kwargs):
    # data = request.data used to be data=request.POST, is changed now that react has been integrated
    # print(request.data)
    serializer = TweetCreateSerializer(data=request.data)
    # raise_exception=True, will send back what error is
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)

    return Response({}, status=400)

@api_view(['GET'])
def tweet_detail_view(request, id, *args, **kwargs):
    qs = Tweet.objects.filter(id=id)
    #print('QS', qs)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['DELETE', 'POST'])
@permission_classes(([IsAuthenticated]))
def tweet_delete_view(request, id, *args, **kwargs):
    qs = Tweet.objects.filter(id=id)
    #print('QS', qs)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    # if doesn't exist then, it is forbidden to delete
    if not qs.exists():
        return Response({'message': 'You cannot delete this tweet.'}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({'message': 'Tweet removed'}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    '''
        id is required
        Action options are: like, unlike, retweet
    '''
    # print(request.POST, request.data)
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        id = data.get('id')
        action = data.get('action')
        content = data.get('content')
    qs = Tweet.objects.filter(id=id)
    #print('QS', qs)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    if action == 'like':
        obj.likes.add(request.user)
        serializer = TweetSerializer(obj)
        return Response(serializer.data, status=200)
    elif action == 'unlike':
        obj.likes.remove(request.user)
        serializer = TweetSerializer(obj)
        return Response(serializer.data, status=200)
    elif action == 'retweet':
        new_tweet = Tweet.objects.create(user=request.user, parent=obj, content=content)
        serializer = TweetSerializer(new_tweet)
        return Response(serializer.data, status=201)
    return Response({}, status=200)   

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tweet_feed_view(request, *args, **kwargs):
    user = request.user
    profiles = user.following.all()
    followed_users_id = []
    if profiles.exists():
        # line below not very efficient
        followed_users_id = [x.user.id for x in profiles]
        followed_users_id.append(user.id)
    # using user__id__in will allow to view all objects in a list and find all related
    qs = Tweet.objects.filter(user__id__in=followed_users_id).order_by('-created')
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    # below is lookin for parameter ?username=john
    username = request.GET.get('username')
    if username != None:
        qs = qs.filter(user__username__iexact=username)
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)
    


"""
    To create safe urls, first in settings.py in ALLOWED_HOSTS, in [] add host first ['127.0.0.1], then add domain name, ['127.0.0.1', '.mydomain.com']

    Then n views.py on top, from django.utils.http import is_safe_url, from django.conf import settings, ALLOWED_HOSTS = settings.ALLOWED_HOSTS

    In tweet_create_view under obj.save, rewrite line if next_url != None: into if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
"""

def tweet_create_view_pure_django(request, *args, **kwargs):
    user = request.user
    # if user is not authenticated then user = None(can't be anonymous)
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        # LOGIN_URL has default route of '/accounts/login/', to change it in setttings.py under ALLOWED_HOSTS add, LOGIN_URL = '/login' 
        return redirect(settings.LOGIN_URL)
    # print('ajax', request.is_ajax())
    # TweetForm can be initiated with data or none
    form = TweetForm(request.POST or None)
    # print('post data is', request.POST)
    next_url = request.POST.get('next') or None
    # print('next_url', next_url)
    # form won't do anything if not valid
    if form.is_valid():
        # if form is valid it will save it
        # commit false does something, i have notes in other projects
        obj = form.save(commit=False)
        obj.user = user # Annon User
        # save data to database
        obj.save()
        if request.is_ajax():
            # can also call serializer function from models.py
            return JsonResponse(obj.serialize(), status=201) # 201=created items

        if next_url != None:
            return redirect(next_url)
        # clear form
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)

    context = {'form': form}
    return render(request, 'components/form.html', context)

def tweet_list_view_pure_django(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by javasscript, swift, java or ios/Android
    return json data
    """

    qs = Tweet.objects.all()
    # pythonic list, turning python object into python dictionary
    # tweets_list = [{'id': x.id, 'content': x.content, 'likes': random.randint(0, 1000), 'created': x.created.strftime("%m-%d-%Y, %H:%M:%S")} for x in qs]

    # since created def serialize in models.py can modify line above, it is sti;; converting python object into python dictionary
    tweets_list = [x.serialize() for x in qs]
    data = {
        'isUser': False,
        'response': tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view_pure_django(request, id, *args, **kwargs):
    """
    REST API VIEW
    Consume by javasscript, swift, java or ios/Android
    return json data
    """

    data = {
        'id': id,
    }
    status = 200
    # try to find object, if object found pass in data, if not raise 404
    try:
        obj = Tweet.objects.get(id=id)
        data['content'] = obj.content
        data['created'] = obj.created.strftime("%m-%d-%Y, %H:%M:%S")
    except:
        data['message'] = 'Not found'
        status = 404
    
    # remember to add f in front of strings to pass in objects
    # return HttpResponse(f"<h1>Hello {id} - {obj.content}</h1>")

    # same as json.dumps content_type='application/json'
    return JsonResponse(data, status=status) 
