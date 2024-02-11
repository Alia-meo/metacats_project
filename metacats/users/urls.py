from django.urls import path, include, re_path
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logoutuser, name='logout'),

]
