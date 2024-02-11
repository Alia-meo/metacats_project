from django.urls import path, include, re_path
from .views import *

app_name = 'blog'


urlpatterns = [
    path('', blog_all, name='blog'),
    path('<int:pk>', blog_single, name='blog_single'),


]
