from django.urls import path, include
from merch import views

app_name = 'merch'

urlpatterns = [
    path('', views.catalog, name='merch'),
    path('product/<slug:product_slug>/', views.product, name='product'),

]
