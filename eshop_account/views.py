from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from eshop_account.forms import LoginForm, RegisterForm, EditUserForm


# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'UserName is not Found')

    context = {
        'login_form': login_form
    }
    return render(request, 'eshop_account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'eshop_account/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_account(request):
    context = {}
    return render(request, "eshop_account/profile.html", context)


@login_required(login_url='/login')
def user_edit_account(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('User not found')

    edit_user_form = EditUserForm(request.POST or None, initial={"username": user.username})
    if edit_user_form.is_valid():
        username = edit_user_form.cleaned_data.get('username')
        user.username = username
        user.save()

    context = {
        "edit_user_form": edit_user_form
    }
    return render(request, "eshop_account/edit_account.html", context)
