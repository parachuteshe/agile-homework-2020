"""Homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teachers import views
from django.urls import include
from student.views import indexs,student_index,queryCourses1,course_template_student



urlpatterns = [
#    path('admin/', admin.site.urls),
    path('indext/', views.indext),
    path('indexs/', indexs),
    path('indext/teacher_index/', views.teacher_index),
    path('indext/course_template/', views.course_template),
    path('indext/week_template/',views.week_template),
    path('indexs/student_template',views.student_template),
    path('', include('sign1.urls')),
    path('indexs/student_index/',student_index),
    path('indexs/student_template/',queryCourses1),
    # path('indexs/get_into_course/',get_into_course),
    path('indexs/course_template_student/',course_template_student)
]
