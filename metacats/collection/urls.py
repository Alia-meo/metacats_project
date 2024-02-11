from django.urls import path, include, re_path
from .views import *


app_name = 'collection'
urlpatterns = [
    path('', collection, name='collection'),

]
