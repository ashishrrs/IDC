from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.views.generic.list import ListView


#Create your views here.
def index(request):
    projects = Project.objects.all()
    carouselimg = carouselimages.objects.all() 
    context = {
        "projects": projects,
        "images": carouselimg ,
    }
    return render(request,"Projects/index.html", context)
# class IndexView(ListView):
#     context_object_name = "projects"    
#     template_name = 'Projects/index.html'
#     queryset = Project.objects.all()

#     def get_context_data(self, **kwargs):
#         context['projects'] = Project.objects.all()
#         context['images'] = carouselimages.objects.all()
#         return context

def project_display(request,key):
    project = Project.objects.get(pk=key)
    context = {
        "project": project,
        "faculties": project.Faculties.all(),
        "students" : project.Students.all(),
        "sponsors" : project.Sponsor.all(),
        "images" : project.Image.all()
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