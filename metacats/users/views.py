from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from maincat.views import menu
from .forms import *


def signup(request):

    if request.method == 'POST':
        form = UsersignupForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse('successfully signup')
    else:
        form = UsersignupForm()
    return render(request, 'users/signup.html', {'form': form, 'menu': menu,})


def signin(request):
    if request.method == 'POST':
        form = UsersigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home:home'))
    else:
        form = UsersigninForm()
    return render(request, 'users/signin.html', {'form': form, 'menu': menu,})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponseRedirect(reverse('home:home'))



