from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=200)
    def __str__(self):
        return '{} {}'.format(self.username, self.password)


class Student(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    rule=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    login=models.ForeignKey(Login,on_delete=models.CASCADE)
    def __str__(self):
        return '{} {} {} {} {} '.format(self.name,self.contact,self.email,self.username,self.password)

class apiData(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.CharField(max_length=200)

