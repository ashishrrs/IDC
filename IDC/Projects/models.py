from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 100, null = False)
    description = models.TextField()
    department = models.CharField(max_length = 100)

    project_lead = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.name


class Faculties(models.Model):
    name = models.CharField(max_length = 100, null = False)
    department = models.CharField(max_length = 100)

    projects = models.ManyToManyField(Project, blank = True, related_name="Faculties")

    def __str__(self):
        return f"{self.name}"



class Students(models.Model):
     name = models.CharField(max_length = 100, null = False)
     roll_no = models.CharField(max_length = 9, null = False)

     projects = models.ManyToManyField(Project, blank = True, related_name="Students")
     
     def __str__(self):
        return f"{self.name}" 


    
class Image(models.Model):
    image = models.ImageField()

    projects = models.ManyToManyField(Project, blank = True, related_name="Image", onDelete = 'CASCADE')

    
    

class Sponsor(models.Model):
    name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)

    projects = models.ManyToManyField(Project, blank = True, related_name="Sponsor")

    def __str__(self):
        return self.name