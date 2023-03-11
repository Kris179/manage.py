from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import UserCreationForm
from .models import User


class LoginView(LoginView):
    template_name = 'accounts/auth/login.html'
    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                return HttpResponseRedirect(reverse('main:index'))


class SignUpView(CreateView):
    template_name = 'accounts/auth/signup.html'
    form_class = UserCreationForm

    def post(self, request):
        if self.form_class.is_valid():
            return HttpResponseRedirect(reverse('accounts:login'))


