from django.urls import path
from . import views

#from Projects.views import IndexView

urlpatterns = [
    path("projects/", views.index,name ="index" ),
    path("projects/<str:key>/",views.project_display, name= "project_display"),
    path("project_add/",views.project_add, name = "project_display"),
    # path("carousel/",views.carousel,name = "carousel_display")
]