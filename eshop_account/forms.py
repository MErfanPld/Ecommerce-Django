from django import forms
from django.contrib.auth.models import User
from django.core import validators


class EditUserForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        label='username'
    )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', "class": "form-control"}),
        label='Username'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', "class": "form-control"}),
        label='Password'
    )


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', "class": "form-control"}),
        label='Username',
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Email', "class": "form-control"}),
        label='Email',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', "class": "form-control"}),
        label='Password'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Re_Password', "class": "form-control"}),
        label='Re_Password'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('The entered email is duplicate')

        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('This user has already registered')

        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError('Passwords are different')

        return password
