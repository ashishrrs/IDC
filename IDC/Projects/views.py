from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    projects = Project.objects.all() 
    context = {
        "projects": projects,
    }
    return render(request,"Projects/index.html", context)

