from django.shortcuts import render
from .models import About

# Create your views here.

def about_page(request):
    about_list = About.objects.all()
    context = {
        'about_list': about_list
    }
    return render(request, 'eshop_about/about.html', context)

