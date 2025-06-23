from django.http import HttpResponse, HttpRequest

from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Product

# Create your views here.


def shop_index(request: HttpRequest):
    products = [('laptop', 2000), ('desktop', 1999), ('place', 322)]
    context = {
        "title": "Index",
        "products": products,
    }
    return render(request, "shopapp/shop-index.html", context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def product_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/product-list.html', context)
