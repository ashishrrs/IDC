from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    start = models.DateTimeField(null = True)


#username and password
#recent events of design in IIITDM