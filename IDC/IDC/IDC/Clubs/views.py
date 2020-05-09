from django.shortcuts import render
from .models import Club

# All projects
def index(request):
	clubs= Club.objects.all()
	context= {"clubs": clubs}
	return render(request,"Clubs/index.html", context)

 
	#create index route for displaying all clubs through carboard or whatever . . . 
def insta_profile(request, instagram_profile_name):
	return render(request,"Clubs/insta.html", {"instagram_profile_name": instagram_profile_name})