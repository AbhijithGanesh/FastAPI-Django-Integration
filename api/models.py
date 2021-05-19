import os
from django.db import models

class EmployeeTable(models.Model):
    Name = models.CharField(max_length = 40 )
    Group = models.CharField(max_length = 50)
    Salary = models.IntegerField()
    UniqueID = models.CharField(max_length = 60, primary_key=True)
    Description = models.TextField()