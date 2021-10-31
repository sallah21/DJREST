from django.db import models

# Create your models here.
class Brewery(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    owner = models.CharField(max_length=50)
class Beer(models.Model):
    name = models.CharField(max_length=50)
    alc = models.FloatField(default=5)
    ibu = models.FloatField(default=10)
    type = models.CharField(max_length=30)
    brewery = models.ForeignKey(Brewery, on_delete=models.SET_NULL,null=True)    
    description= models.CharField(max_length=256)


