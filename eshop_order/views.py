from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from eshop_order.forms import UserNewOrderForm
from eshop_order.models import Order, OrderDetail
from eshop_products.models import Product

# Create your views here.

@login_required(login_url="/login")
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = new_order_form.cleaned_data.get('productId')
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.objects.get(pk=product_id)
        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        # todo: redirect user to user panel
        # return redirect('/user/orders')
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')
    else:
        print(new_order_form.errors)
    return redirect('/')


@login_required(login_url='/login')
def user_open_order(request):
    context = {
        'order': None,
        'details': None
    }

    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()

    return render(request, 'order/user_open_order.html', context)


@login_required(login_url='/login')
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/open-order')
    raise Http404()

