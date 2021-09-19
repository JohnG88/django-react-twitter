from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet

# Create your views here.

def home_view(request, *args, **kwargs):
    # printing args kwargs, shows something in django terminal
    # for kwargs it shows {'id': 1}, which is from urls.py root location, which has 'tweets/<int:id>'
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    hello = 'Hello World'
    context = {'hello': hello}
    return render(request, 'pages/index.html', context, status=200)

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by javasscript, swift, java or ios/Android
    return json data
    """

    qs = Tweet.objects.all()
    # pythonic list
    tweets_list = [{'id': x.id, 'content': x.content, 'created': x.created.strftime("%m-%d-%Y, %H:%M:%S")} for x in qs]
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
