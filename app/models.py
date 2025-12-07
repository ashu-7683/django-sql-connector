from django.db import models

# Create your models here.
class Student(models.Model):
    stid=models.CharField(max_length=100)
    stname=models.CharField(max_length=100)
    stage=models.IntegerField(max_length=100)
    
