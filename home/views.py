from django.shortcuts import render

from products.models import Product
from lessons.models import Subscription


def index(request):
    products = Product.objects.filter(old_price__isnull=False)
    products_amount = products.count()
    if products_amount > 4:
        products = Product.objects.filter(old_price__isnull=False).order_by('?')[:4]
    context = {
        'products': products,
    }

    return render(request, "home/index.html", context)
