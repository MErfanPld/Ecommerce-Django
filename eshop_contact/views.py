from django.shortcuts import render
from .models import ContactUs, Discription

# Create your views here.
from eshop_contact.forms import CreateContactForm


def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        # todo : show user a success message
        contact_form = CreateContactForm()

    context = {
        'contact_form': contact_form
    }

    return render(request, 'eshop_contact/contact_us.html', context)


def Discriptions(request):
    contacts = Discription.objects.all()
    context = {
        "contacts" : contacts
    }
    return render(request, 'eshop_contact/contact_us.html' , context)