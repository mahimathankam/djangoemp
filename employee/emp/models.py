from django.db import models

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    eemail=models.EmailField()
    eno=models.IntegerField()
