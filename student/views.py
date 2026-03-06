# from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from student import models
from django.views.decorators.csrf import csrf_exempt #表单数据传递装饰器
from teachers.models import Course
# Create your views here.
def indexs(request):
    return render(request, 'indexs.html')

def student_index(request):
    sid = request.session['id']
    courses = models.student.objects.filter(student_id=sid)
    codes = []
    for item in courses:
        codes.append(item.courses_code)
    courses_added = Course.objects.filter(code__in=codes)
    context = {}
    context['courses'] = courses_added     
    if request.method == "POST":
        course_code = request.POST.get("course_code",None)
        student_id = request.POST.get("student_id",None)
        # models.student.objects.create(courses_code = course_code,student_id = student_id)
        add_student = models.student(courses_code = course_code,student_id = student_id) 
        add_student.save()   
    return render(request, "student_index.html",context)

def indexs(request):
    sid = request.session['id']
    courses = models.student.objects.filter(student_id=sid)
    codes = []
    for item in courses:
        codes.append(item.courses_code)
    courses_added = Course.objects.filter(code__in=codes)
    context = {}
    context['courses'] = courses_added  
    return render(request, "indexs.html",context)   


def course_template_student(request):
    course_id = request.GET.get('id')
    course_name = Course.objects.get(id=course_id)
    context = {}
    context['course_name'] = course_name
    request.session['course_id'] = course_id
    return render(request, 'course_template_student.html',context)


def queryCourses1(request):
    courses = models.student.objects.all()
    return render(request, "student_template.html",context={"courses":courses})

