from django.db import models

# Create your models here.
class  features (models.Model):
    name= models.CharField(max_length=100)
    details= models.CharField(max_length=1000)