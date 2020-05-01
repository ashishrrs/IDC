from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    projects = Project.objects.all() 
    context = {
        "projects": projects,
    }
    return render(request,"Projects/index.html", context)


def project_display(request,key):
    project = Project.objects.get(id = key)
    context = {
        "project": project,
    }   
    return render(request,"Projects/project.html",context) 

