from django.http.response import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# Check out REST API course from CodingEntrepreneurs

def home_view(request, *args, **kwargs):
    # print(request.user or None)
    # printing args kwargs, shows something in django terminal
    # for kwargs it shows {'id': 1}, which is from urls.py root location, which has 'tweets/<int:id>'
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    # hello = 'Hello World'
    # context = {'hello': hello}
    # return render(request, 'pages/index.html', context, status=200)
    # username = None
    # if request.user.is_authenticated:
    #     username = request.user.username
    return render(request, "pages/feed.html", status=200)

def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets/list.html")

def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "tweets/detail.html", context={"tweet_id": tweet_id})

# def tweets_profile_view(request, username, *args, **kwargs):
    
#     return render(request, "tweets/profile.html", context={"profile_username": username})

