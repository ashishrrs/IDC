from django.db import models
from Home.models import *

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 100, null = False)
    description = models.TextField()
    department = models.CharField(max_length = 100)
    displayImage = models.ImageField(default = "defaultProject.png",upload_to="images")
    project_lead = models.CharField(max_length = 100, blank = True)
    upcoming_events = models.ManyToManyField(Events, blank = True, related_name="Project")

    def __str__(self):
		    return self.name


class Faculties(models.Model):
	name = models.CharField(max_length = 100, null = False)
	department = models.CharField(max_length = 100)

	projects = models.ManyToManyField(Project, blank = True, related_name="Faculties")
	photo= models.ImageField(default= "defaultProject.png",upload_to="images")

	def __str__(self):
		return f"{self.name}"



class Students(models.Model):
	name = models.CharField(max_length = 100, null = False)
	roll_no = models.CharField(max_length = 9, null = False)
	photo= models.ImageField(default="defaultProject.png", upload_to="images")

	projects = models.ManyToManyField(Project, blank = True, related_name="Students")
	
	def __str__(self):
		return f"{self.name}"


	
class Image(models.Model):
	image = models.ImageField()

	projects = models.ManyToManyField(Project, blank = True, related_name="Image")

class carouselimages(models.Model):
	carouselimage =  models.ImageField(default = "defaultProject.png",upload_to="images/carousel",blank = False)
	carouseltitle = models.CharField(max_length = 100,null = False)
	carouseldesc = models.TextField()
		
	def __str__(self):
		return self.carouseltitle

	
	

class Sponsor(models.Model):
	name = models.CharField(max_length = 100)
	logo = models.ImageField(blank = True, upload_to="images")
	projects = models.ManyToManyField(Project, blank = True, related_name="Sponsor")

	def __str__(self):
		return self.name