from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from .models import Course,Student

# Create your views here.

def index(request:WSGIRequest):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        "courses":courses, 
        "students":students 
    }
    return render(request,"index.html",context)

def course_by_student(request,course_id):
    courses = Course.objects.all()
    students = Student.objects.filter(course_id= course_id)
    context = {
        "courses":courses,
        "students":students
    }
    return render(request,"index.html",context)