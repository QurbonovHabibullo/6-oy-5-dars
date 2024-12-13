from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50,unique=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    
class Student(models.Model):
    name = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=70,blank=True,null=True)
    enrolled_at = models.DateTimeField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    