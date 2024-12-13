from django.urls import path
from .views import index,course_by_student

urlpatterns = [
    path('',index,name="home"),
    path('course/<course_id>/',course_by_student,name='course_by_student'),
]
