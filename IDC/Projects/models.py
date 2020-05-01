from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 100, null = False)
    description = models.TextField()
    department = models.CharField(max_length = 100)

    project_lead = models.CharField(max_length = 100, blank = True)

  


class Faculties(models.Model):
    name = models.CharField(max_length = 100, null = False)
    department = models.CharField(max_length = 100)

    projects = models.ManyToManyField(Project, blank = True, related_name="Faculties")



class Students(models.Model):
     name = models.CharField(max_length = 100, null = False)
     roll_no = models.CharField(max_length = 9, null = False)

     projects = models.ManyToManyField(Project, blank = True, related_name="Students")

    
class Image(models.Model):
    image = models.ImageField("static")

    projects = models.ManyToManyField(Project, blank = True, related_name="Image")

    

class Sponsor(models.Model):
    name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)

    projects = models.ManyToManyField(Project, blank = True, related_name="Sponsor")
