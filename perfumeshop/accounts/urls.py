from django.urls import path

from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('signup/', SignUpView, name='signup')
]