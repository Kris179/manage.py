from django.urls import path
from . import views


app_name='catalogs'

urlpatterns = [
    path('', views.catalogs_home, name='catalogs_home')
]
