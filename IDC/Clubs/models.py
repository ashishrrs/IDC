from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length = 100)
    core = models.CharField(max_length = 100)
    jointCore = models.CharField(max_length = 100)
