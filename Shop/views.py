import itertools

from django.shortcuts import render

from eshop_products.models import Product


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    most_visit_products = Product.objects.order_by('-visit_count').all()[:3]
    latest_products = Product.objects.order_by('-id').all()[:3]
    context = {
        "most_visit": my_grouper(3, most_visit_products),
        "latest_products": my_grouper(3, latest_products),
    }
    return render(request, 'index.html', context)


def handel_404_error(request, exception):
    return render(request, '404.html', {})
