from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import Query
from .models import queries
from django.contrib.auth.decorators import login_required

# Create your views here.
# def index(request):
#     if (request.method=='GET'):
#         form= Query()
#         return render(request,"Forum/index.html", {'form':form})

#     elif (request.method=='POST'):
#         form= Query(request.POST)
#         if form.is_valid():
#             name= form.cleaned_data['name']
#             email= form.cleaned_data['email']
#             display= form.cleaned_data['display']
#             message= form.cleaned_data['message']
#             recipient_list= ['ced18i061@iiitdm.ac.in', 'ced18i048@iiitdm.ac.in', email]
#             send_mail(subject='New Query on DIC website',from_email= 'iiitdm.dic@gmail.com',recipient_list = recipient_list,message=message)


#             if(display=='public'):
#                 new_query = queries(name= name, email= email, message= message)
#                 new_query.save()
			
#             context= {
#                 'queries' : queries.objects.all()
#                      }
#             return render(request,"Forum/index.html",context )
@login_required(login_url="/login/")
def index(request):
	return render(request,"Forum/index.html");

