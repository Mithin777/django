from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField()
    roll_no=models.CharField(max_length=20)
    course=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"