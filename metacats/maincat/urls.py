from django.urls import path, include, re_path
from .views import *

app_name = 'maincat'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),

]


