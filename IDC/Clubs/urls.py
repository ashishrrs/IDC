from django.urls import path,include
from . import views
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    path('clubs/<str:instagram_profile_name>',TemplateView.as_view(template_name= 'Clubs/insta.html'), name= "insta_profile"),
    path('clubs/', views.index, name= "index"),
]
