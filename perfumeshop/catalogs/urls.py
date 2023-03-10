from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalogs_home, name='catalogs_home')
]
