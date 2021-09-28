from django.shortcuts import render, redirect
# for formModel add authenticate below
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def login_view(request, *args, **kwargs):
    # built in django auth form
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect('/')

    context = {'form': form, 'btn_label': 'Login', 'title': 'Login'}
    return render(request, 'accounts/auth.html', context)

    '''
    FOR FORM MODEL
    form = MyModelForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        user_ = authenticate(username, password)
        login(request, user_)
        return redirect('/')

    return render(request, 'form.html', {'form': form})
    '''

def logout_view(request, *args, **kwargs):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    context = {'form': None, 'description': 'Are you sure you want to logout?', 'btn_label': 'Click to Confirm', 'title': 'Logout'} 
    return render(request, 'accounts/auth.html', context)

def register_view(request, *args, **kwargs):
    # built in django create user form
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get('password1'))
        #  can send verification email to user
        login(request, user)
        return redirect('/')
        # print(form.cleaned_data)
        # username = form.cleaned_data.get('username')
        # can also use User.objects.create(username=username)
    context = {'form': form, 'btn_label': 'Register', 'title': 'Register'}
    return render(request, 'accounts/auth.html', context)