from django.http import HttpResponse, HttpRequest

from django.shortcuts import render

# Create your views here.


def shop_index(request: HttpRequest):
    products = [('laptop', 2000), ('desktop', 1999), ('place', 322)]
    context = {
        "title": "Index",
        "products": products,
    }
    return render(request, "shopapp/shop-index.html", context)
