from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    x_class = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    created_at = models.DateField(auto_created=True)

