from django.http.response import Http404
from django.shortcuts import render

from eshop_order.forms import UserNewOrderForm
from .models import Product
from django.core.paginator import Paginator
from django.views.generic import ListView
from eshop_tag.models import Tag


# Create your views here.

# ==============================ProductsList===========================

class ProductsList(ListView):
    template_name = 'eshop_products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.get_active_products()


# ==============================product_detail===========================

def product_detail(request, *args, **kwargs):
    new_order_form = UserNewOrderForm(request.POST or None)

    product_id = kwargs['productId']
    product: Product = Product.objects.get_by_id(product_id)

    if product is None or not product.active:
        raise Http404('Product Not Found')

    product.visit_count += 1
    product.save()

    context = {
        'product': product,
        'new_order_form': new_order_form,
        'productId': kwargs['productId']
    }
    return render(request, 'eshop_products/product_detail.html', context)


# ==============================SearchProductsView===========================

class SearchProductsView(ListView):
    template_name = 'eshop_products/products_list.html'
    paginate_by = 50

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.filter(active=True, title__icontains=query)

        return Product.objects.get_active_products()

# def products(request):
#     products = Product.objects.get_active_products()
#     paginator = Paginator(products, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         "products" : products,
#         "page_obj" : page_obj,
#     }
#     return render(request, 'eshop_products/products_list.html', context)
