from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name= "index"),
    path('login/', views.login, name= "login")
]