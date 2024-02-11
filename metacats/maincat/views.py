from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{'title': "merch", 'url_name': 'merch:merch'},
        {'title': "collection", 'url_name': 'collection:collection'},
        {'title': "blog", 'url_name': 'blog:blog'},
]


def index(request):
    return render(request, 'maincat/index.html', {'title': 'Metacats', 'menu': menu, })


def about(request):
    return render(request, 'maincat/about.html', {'title': 'About', 'menu': menu, })


