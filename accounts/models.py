from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class myUser(AbstractUser):
    name=models.CharField(max_length=100,default=False)
    contact=models.CharField(max_length=50,default=False)
    status=models.CharField(max_length=10,default="active")
    rule=models.CharField(max_length=10,default=False)
