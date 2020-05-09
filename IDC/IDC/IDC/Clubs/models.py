from django.db import models
from Home.models import *


# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length = 100)
    description= models.TextField(null= True)
    core = models.CharField(max_length = 100, blank = True)
    jointcore = models.CharField(max_length = 100, blank = True)
    core_email_id= models.EmailField(blank= True)
    insta_id= models.CharField(max_length=100)
    displayImage = models.ImageField(default="defaultProject.png",upload_to="images/clubs")
    upcoming_events = models.ManyToManyField(Events, blank = True, related_name="Club")

    def __str__(self):
        return self.insta_id