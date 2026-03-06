from django.db import models

# Create your models here.

class student(models.Model):
    student_id = models.CharField(max_length=20)
    courses_code = models.CharField(max_length=8,default="")
    status = models.BooleanField(default="False")
    def __str__(self):
        return self.student_id

class assignment(models.Model):
    upload_time = models.DateTimeField(auto_now="false")
    files = models.FileField(upload_to='uploads/assignment/')#学生上传的文件
    annotation = models.TextField()#老师对学生的批注
    comment =  models.TextField()#学生对老师批注的反馈
    feedback =  models.TextField()#总反馈
    score = models.CharField(max_length=10)#学生作业评分
    status = models.BooleanField(default="False")#学生是否已阅批改
    assignment_id = models.CharField(max_length=20)#连接老师的assignment
    def __str__(self):
        return self.upload_time

