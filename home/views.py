from django.shortcuts import render

from products.models import Product
from lessons.models import Subscription


def index(request):
    products = Product.objects.filter(old_price__isnull=False)
    products_amount = products.count()
    if products_amount > 3:
        products = Product.objects.filter(old_price__isnull=False).order_by('?')[:3]
    subscriptions = Subscription.objects.filter(promotional_price__isnull=False)
    context = {
        'products': products,
        'subscriptions': subscriptions,
    }

    return render(request, "home/index.html", context)
