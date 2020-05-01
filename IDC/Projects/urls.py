from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("projects/<str:key>/",views.project_display, name= "project_display"),
    path("project_add/",views.project_add, name = "project_display")
]