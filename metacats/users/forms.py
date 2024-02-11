from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import *


# class LoginUserForm(forms.Form):
#     username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UsersignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UsersigninForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())


class CommentForm(forms.Form):
    class Meta:
        model = CommentPost
        fields = ('text',)
