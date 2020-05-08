from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('home/', views.index, name= "index"),
    path('login/', views.login, name= "login")
]