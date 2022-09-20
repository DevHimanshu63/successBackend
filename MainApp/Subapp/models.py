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
    marks=models.IntegerField()
    datetime=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.course_name


class Admission(models.Model):
    sno=models.AutoField(primary_key=True)
    fullName=models.CharField(max_length=250)
    stu_course=models.CharField(max_length=250)
    Email=models.CharField(max_length=250)
    Phone=models.CharField(max_length=250)
    query=models.TextField()
    datetime=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.fullName
    

class Team(models.Model):
    sno=models.AutoField(primary_key=True)
    MemberImg=models.ImageField(upload_to='static/img',default='')
    fullName=models.CharField(max_length=250)
    designation=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    Email=models.CharField(max_length=250)
    datetime=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.fullName
    

class Testimonials(models.Model):
    sno=models.AutoField(primary_key=True)
    StuImg=models.ImageField(upload_to='static/img')
    fullName=models.CharField(max_length=250)
    Message=models.TextField()
    datetime=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.fullName