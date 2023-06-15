from django.urls import path

from . import views

utlpatterns = [
    path('', views.index, name='index')
]