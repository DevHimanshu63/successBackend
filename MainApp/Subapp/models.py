from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=100)
    content=models.TextField()
    datetime=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name +"-"+ self.email


class Course(models.Model):
    sno=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=250)
    about_course=models.TextField()
    courseImg=models.ImageField(upload_to='static/img')
    datetime=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.course_name


class Campus(models.Model):
    sno=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=250)
    course_name=models.TextField()
    studentImg=models.ImageField(upload_to='static/img')
    marks=models.IntegerField(max_length=200)
    datetime=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.course_name