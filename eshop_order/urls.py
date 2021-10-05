from django.urls import path
from .views import add_user_order, user_open_order, remove_order_detail

urlpatterns = [
    path('add-user-order', add_user_order),
    path('remove-order-detail/<detail_id>', remove_order_detail),
    path('open-order', user_open_order),
]