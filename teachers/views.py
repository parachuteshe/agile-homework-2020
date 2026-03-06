from django.shortcuts import render
from teachers.models import Course,week
from django.template import Context
import random,string
from random import shuffle
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
codes =  list(Course.objects.values_list('code'))
def generateCode():
    num = random.sample(string.digits,1) 
    lower = random.sample(string.ascii_lowercase,1) 
    upper = random.sample(string.ascii_uppercase,1) 
    other = random.sample(string.ascii_letters+string.digits,5) 
    res = num+lower+upper+other 
    res = ''.join(res)
    str_list = list(res)
    shuffle(str_list)
    res = ''.join(str_list)
    if res not in codes:
        codes.append(res)
        return res
    else:
        return 0

def indext(request):
    course_id = request.GET.get('course_id')
    uid = request.session['id']
    course = Course.objects.filter(user=uid)
    context = {}
    context['course'] = course
    weeks = week.objects.all()
    context['weeks'] = weeks
    if request.GET.get('week_delete'):   
        week_delete_id = request.GET.get('week_delete')
        week.objects.filter(id=week_delete_id).delete()
    if request.method == "POST": 
        if request.POST.get('course_id'):
            course_id = request.POST.get('course_id') 
            week_name = request.POST.get('week_name') 
            add_week = week(name=week_name,course_id=course_id) 
            add_week.save()
    return render(request, 'indext.html',context)

def teacher_index(request):
    uid = request.session['id']
    course = Course.objects.filter(user=uid)
    # user_id = request.GET.get('id')
    # course = Course.objects.filter(user=user_id)
    context = {}
    context['course'] = course     
    randomCode = generateCode()
    if request.GET.get('delete'):   
        delete_id = request.GET.get('delete')
        Course.objects.filter(id=delete_id).delete()
    while randomCode == 0:
        randomCode = generateCode() 
    if request.method == "POST": 
        if request.POST.get('name') :
            name = request.POST.get('name')
            if Course.objects.filter(name=name):
                message = "exist"   
                context['message'] = "The course name has already existed！" 
            else:
                message = "You have successfully created the course！"
                context['message'] = message
                description = request.POST.get('description') 
                user_id = request.POST.get('user_id') 
                add_course = Course(name=name, user=user_id,description=description,code=randomCode) 
                add_course.save()
#            print(codes)
        if request.POST.get('new_description'):
            new_description = request.POST.get('new_description')
            edit_course_id = request.POST.get('edit_course_id')
            course_description = Course.objects.get(id=edit_course_id)
            course_description.description=new_description
            course_description.save()
    return render(request, 'teacher_index.html',context)


def course_template(request):
    course_id = request.GET.get('course_id')
    course_name = Course.objects.get(id=course_id)
    context = {}
    context['course_name'] = course_name
    request.session['course_id'] = course_id
    if request.method == "POST": 
#        name = request.POST.get('course_id')
        notification = request.POST.get('notification')
        reference = request.POST.get('reference')
#        print(course_name)
        if notification:
            course_name.notification=notification
            course_name.save()
        if reference:
            course_name.reference=reference
            course_name.save()
    return render(request, 'course_template.html',context)

def week_template(request):
    course_id = request.session['course_id']
    course_name = Course.objects.get(id=course_id)
    context = {}
    context['course_name'] = course_name
    if request.method == "POST": 
        class_description = request.POST.get('class_description')
        course_id = request.POST.get('course_id')
        week_name = request.POST.get('week')
        week_id = Course.objects.get(week=week_name).id
        homework_name = request.POST.get('homework_name')
        homework_requirement = request.POST.get('homework_requirement')
        # modify_time = request.POST.get('modify_time')
        due_date = request.POST.get('due_date')
        if course_description:
            add_week = Class(course_id=course_id,week=week_name,class_description=class_description) 
            add_week.save()
        if homework_name:
            add_homework = Assignment(class_id=week_id,homework_name=homework_name,homework_requirement=homework_requirement,modify_time=modify_time,due_date=due_date)
            add_homework.save()
    return render(request, 'week_template.html',context)


def student_template(request):
    return render(request, 'student_template.html')
    

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")