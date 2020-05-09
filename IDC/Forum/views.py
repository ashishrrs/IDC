from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import Query
from .models import *
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
	if request.method=='GET':
		context= {
			 "queries":query.objects.all()
		 }
		return render(request,"Forum/index.html",context)
	else:
		username= request.user.username
		email = request.POST['email']
		content= request.POST['new_discussion_text']
		subject = request.POST['newdiscussiontitle']
		message= "subject :" +subject +"\n" + "content:" +content
		new_query = query(name= username, email= email, content= content, subject = subject)
		new_query.save()
		recipient_list= ['ced18i061@iiitdm.ac.in', 'ced18i048@iiitdm.ac.in', email]
		send_mail(subject='New Query on DIC website',from_email= 'dic.iiitdmk@gmail.com',recipient_list = recipient_list, message=message)
        

		context= {
			"queries": query.objects.all()
		}
		return render(request,"Forum/index.html", context)

def query_page(request,key):
	current_query= query.objects.get(pk= key)
	responses= current_query.replies.all()
	context= {
		"current_query": current_query,
		"responses": responses,
	}
	return render(request,"Forum/query.html", context)




		



