# Create your views here.
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:23:31 2019

@author: admin
"""

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from sign1 import models
from django.views.decorators.csrf import csrf_exempt #表单数据传递装饰器
from django.contrib import messages

#注册数据写入
@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    
    if request.method == "POST":
        name = request.POST.get("name",None)
        email = request.POST.get("email",None)
        password = request.POST.get("password",None)
        password2 = request.POST.get("password2",None)
        identity = request.POST.get("identity",None)
        if password2 != password:
            return render(request,'register.html',{'script':"alert",'wrong':'密码输入不一致'})
        else:
            try:           
                if models.student_reg.objects.create(
                    name = name,
                    email = email,
                    passwords = password,
                    identity = identity
                ):
                    return render(request,'login.html',{'script':"alert",'wrong':'注册成功，返回登录'}) #12.30,返回路径改
 
            except:
                return render(request,'register.html',{'script':"alert",'wrong':'邮箱已注册'})

        
              

#界面登录
@csrf_exempt
def login(request):
    request.session['id'] = "暂无"
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":  
        email = request.POST.get("email",None)
        passwords = request.POST.get("password",None)
        try:
            users = models.student_reg.objects.get(email=email)
            if users:
                if users.passwords == passwords:
                    if users.identity == "Teacher":
                        # request.session.set_expiry(3600)  #session认证时间为10s，10s之后session认证失效
                        request.session['username']=users.name   #user的值发送给session里的username
                        request.session['is_login']=True 
                        request.session['id'] = users.id
                        user_id = users.id
                        return redirect("/indext")
                    else:
                        request.session.set_expiry(3600)  #session认证时间为10s，10s之后session认证失效
                        request.session['username']=users.name   #user的值发送给session里的username
                        request.session['is_login']=True 
                        request.session['id'] = users.id
                        return redirect("/indexs")
                else:
                    return render(request,'login.html',{'script':"alert",'wrong':'密码错误'})
            else:
                return render(request,'login.html',{'script':"alert",'wrong':'账号不存在'})

        except:
            return render(request,'login.html',{'script':"alert",'wrong':'网络错误'})
            
