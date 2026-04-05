from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(primary_key=True,max_length=10)
    ename=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
