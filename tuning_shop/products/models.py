from django.db import models

# Create your models here.
class Brands(models.Model):
    brand = models.CharField()
    logo = models.ImageField()
    
class Products(models.Model):
    pass


    