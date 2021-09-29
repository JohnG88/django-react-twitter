from django import forms
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

class UserForm(forms.ModelForm):
    # these fields related to user
    location = forms.CharField(required=False)
    bio = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    # these fields related to user
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = ['location', 'bio']

class ProfileBasicForm(forms.Form):
    # these fields related to user
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    location = forms.CharField(required=False)
    bio = forms.CharField(required=False)