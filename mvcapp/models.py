from django.db import models

# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    fullname = models.CharField(max_length=200)
    student_number = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    classname = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname