from django.shortcuts import render

# Create your views here.


def profile_detail_view(request, username,  *args, **kwargs):
    # get profile of passed username
    
    context = {'username': username}
    return render(request, 'profiles/detail.html', context)