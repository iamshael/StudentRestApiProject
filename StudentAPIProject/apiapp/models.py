from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    marks = models.FloatField()
    addr = models.CharField(max_length=100)

    def __str__(self):
        return self.name
