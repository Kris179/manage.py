from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

from accounts.forms import UserCreationForm
from accounts.models import User


class LoginView(LoginView):
    template_name = 'accounts/auth/login.html'


class SignUpView(CreateView):
    template_name = 'accounts/auth/signup.html'
    form_class = UserCreationForm