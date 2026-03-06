from django.db import models

# Create your models here.
#编辑 models.py 文件，改变模型。
#运行 python manage.py makemigrations 为模型的改变生成迁移文件。
#运行 python manage.py migrate 来应用数据库迁移。

class Course(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(default="No description yet.")
    notification = models.TextField(default="No notification yet.")
    history_notification = models.TextField(default="No notification yet.")
    reference = models.TextField(default="No reference yet.")
    code = models.CharField(max_length=8,unique=True,default="")
    user = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.name

def upload_to(instance, filename):
    # return '/'.join([MEDIA_ROOT/upload, instance.user_name, filename])
    # return 'user_{0}/{1}'.format(instance.user.id, filename)
    # return '/'.join([MEDIA_ROOT, instance.course_id, instance.name])
    return 'course_{0}/{1}'.format(instance.course_id, instance.name)

class week(models.Model):
    name = models.CharField(max_length=20)#自定义的项目名称
    description = models.TextField(default="No description yet.")#周任务描述
    # files = models.FileField(upload_to='uploads/week/')#周课件路径
    files = models.FileField(upload_to=upload_to)
    status = models.BooleanField(default="False")#布尔值，是否隐藏的状态
    release_time = models.DateTimeField(auto_now="true")#发布时间
    # course_id = models.CharField(max_length=8,unique=True,default="")#课程表id
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default="")
    def __str__(self):
            return self.name

class assignment(models.Model):
    name = models.CharField(max_length=20,default="")#自定义的任务名称
    description = models.TextField(default="No description yet.") #任务详情
    due_time = models.DateTimeField(auto_now="false")#任务截止时间
    release_time = models.DateTimeField(auto_now="true")#任务发布时间
    files = models.FileField(upload_to='uploads/assignment/')#任务相关附件
    week_id = models.CharField(default="",max_length=20)#发布时间
    def __str__(self):
            return self.week_id
    
