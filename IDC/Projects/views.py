from django.shortcuts import render, redirect
from .models import *
from .forms import *


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


def project_add(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }
    return render(request,"Projects/addProject.html", context)


