from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Full Name', 'class': 'form-control'}),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email', 'class': 'form-control'}),
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Subject', 'class': 'form-control'}),
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Text', 'class': 'form-control', 'rows': '8',
                   'cols': '20'}),
    )
