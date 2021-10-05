from django.urls import path
from .views import product_detail, SearchProductsView, ProductsList

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
]
