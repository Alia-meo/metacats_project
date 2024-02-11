from django.shortcuts import render
from maincat.views import menu

app_name = 'collection'


def collection(request):

    return render(request, 'collection/collection.html', {'menu': menu})




