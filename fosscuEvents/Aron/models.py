from django.db import models

# Create your models here.
class Core(models.Model):
    first_name=models.CharField(max_length=200, null=True)
    last_name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class User(models.Model):
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name=models.CharField(max_length=200, null=True)
    Date=models.DateTimeField(auto_now_add=True, null=True)
    Description=models.CharField(max_length=1000, null=True)
    Attendee=models.IntegerField(blank=True)
    eventImage=models.ImageField(default="FOSSCUlogo.png", blank=True, null=True)
    
    
    def __str__(self) -> str:
        return self.name