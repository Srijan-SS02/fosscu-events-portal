from django.db import models

# Create your models here.

    
    
class Core(models.Model):
    first_name=models.CharField(max_length=200, null=True)
    last_name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    
    
class User(models.Model):
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)



# class Events(models.Model):
#     ...
