from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('home', views.home, name='home'),
    path('delete/<int:id>', views.delete, name='delete'),
]