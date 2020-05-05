from django.db import models

# Create your models here.
class queries(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    message= models.TextField(max_length=500)
    response_message= models.TextField(max_length=500, blank=True)
    status= models.BooleanField(default= False)



