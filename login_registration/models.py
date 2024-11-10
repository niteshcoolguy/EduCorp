from django.db import models
from django.utils import timezone

# Create your models here.
class createuser(models.Model):
    username = models.CharField(max_length=100,null=True,unique=True)
    password = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=255, null=True, unique=True)
    
    def __str__(self):
        return self.username


    
class course(models.Model):
    course_name = models.CharField(max_length=50,unique=True)
    course_description = models.TextField(max_length=200)
    complete = models.BooleanField(default=False,null=True)
    created_date = models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return self.course_name


class student(models.Model):
    username = models.CharField(max_length=100,null=True)
    surname = models.CharField(max_length=100,null=True)   
    email = models.EmailField(max_length=255, null=True, unique=True)
    phone_number = models.CharField(max_length=15)
    created_date = models.DateTimeField(default=timezone.now,null=True)
    student_course = models.ForeignKey(course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
    

class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True, null=True)
    company_location = models.CharField(max_length=200, null=True)
    company_website = models.URLField(max_length=200, null=True)
    company_created = models.DateTimeField(default=timezone.now,null=True)
    
    def __str__(self):
      return self.company_name
    


    