from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 100)
    present = models.BooleanField()
    roll= models.CharField(max_length=10)
    
    