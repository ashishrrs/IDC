from django.db import models


class query(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(blank=True)
	content = models.TextField(max_length=500, blank= True)
	subject= models.CharField(max_length=100)

class reply(models.Model):
	response= models.TextField(max_length=500)
	admin_name= models.CharField(max_length=20) 
	query= models.ManyToManyField(query, blank= True, related_name="replies")   