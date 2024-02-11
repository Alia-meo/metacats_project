from django.shortcuts import render
from maincat.views import menu
from merch.models import *


def catalog(request):
    goods = Products.objects.all()
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    return render(request, 'merch/catalog.html', {'menu': menu, 'goods': goods, })


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
        'menu': menu
    }

    return render(request, 'merch/product.html', context=context)
