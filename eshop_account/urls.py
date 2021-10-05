from django.urls import path

from .views import login_user, register, log_out, user_account, user_edit_account

urlpatterns = [
    path('login/', login_user),
    path('register/', register),
    path('logout/', log_out),
    path('account/profile/', user_account),
    path('account/profile/edit', user_edit_account),
]
