from django.urls import path, include
from .views import about_page

urlpatterns = [
    path('about-us/', about_page),
]