from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('forms/', views.index, name="forms"),
    path("forms/<str:key>/", views.query_page,name="query")
]
