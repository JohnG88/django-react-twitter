from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Tweet
from .forms import TweetForm

import random

# Create your views here.

def home_view(request, *args, **kwargs):
    # printing args kwargs, shows something in django terminal
    # for kwargs it shows {'id': 1}, which is from urls.py root location, which has 'tweets/<int:id>'
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    hello = 'Hello World'
    context = {'hello': hello}
    return render(request, 'pages/index.html', context, status=200)

def tweet_create_view(request, *args, **kwargs):
    # TweetForm can be initiated with data or none
    form = TweetForm(request.POST or None)
    print('post data is', request.POST)
    # form won't do anything if not valid
    if form.is_valid():
        # if form is valid it will save it
        # commit false does something, i have notes in other projects
        obj = form.save(commit=False)
        # save data to database
        obj.save()
        # clear form
        form = TweetForm()

    context = {'form': form}
    return render(request, 'components/form.html', context)

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by javasscript, swift, java or ios/Android
    return json data
    """

    qs = Tweet.objects.all()
    # pythonic list
    tweets_list = [{'id': x.id, 'content': x.content, 'likes': random.randint(0, 1000), 'created': x.created.strftime("%m-%d-%Y, %H:%M:%S")} for x in qs]
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
