from django.http.response import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.conf import settings

from .models import Tweet
from .forms import TweetForm
from .serializers import TweetSerializer

import random

# Create your views here.

def home_view(request, *args, **kwargs):
    print(request.user or None)
    # printing args kwargs, shows something in django terminal
    # for kwargs it shows {'id': 1}, which is from urls.py root location, which has 'tweets/<int:id>'
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    hello = 'Hello World'
    context = {'hello': hello}
    return render(request, 'pages/index.html', context, status=200)

def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST or None)
    if serializer.is_valid():
        obj = serializer.save(user=request.user)
        return JsonResponse(serializer.data, status=201)

    return JsonResponse({}, status=400)


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

def tweet_list_view(request, *args, **kwargs):
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

def tweet_detail_view(request, id, *args, **kwargs):
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
