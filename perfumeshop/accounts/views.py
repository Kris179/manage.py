from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import UserCreationForm
from .models import User


# class LoginView(LoginView):
#     template_name = 'accounts/auth/login.html'
#     def post(self, request):
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 return HttpResponseRedirect(reverse('main:index'))

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = AuthenticationForm
    context = {
        'form': form
    }
    return render(request, 'accounts/auth/login.html', context)


def SignUpView(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/auth/signup.html', context)
