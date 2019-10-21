from django.db import models
class Client(models.Model):
    Name = models.CharField(max_length=20,default="")
    Email = models.CharField(max_length=30,default="")
    Address = models.CharField(max_length=40,default="")
    Dob = models.CharField(max_length=10,default="")
    Mobile = models.CharField(max_length=10,default="")

    
    def __str__(self):
        return self.Name