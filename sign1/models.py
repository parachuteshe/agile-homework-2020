from django.db import models

#运行 python manage.py makemigrations 为模型的改变生成迁移文件。
#运行 python manage.py migrate 来应用数据库迁移。
#setting 的install 中注册 app

# Create your models here.
class student_reg(models.Model):
    name = models.CharField(max_length=15,null=False )
    passwords = models.CharField(max_length=20,null=False)
    email = models.EmailField(unique = True,null=False)
    identity = models.CharField(max_length = 10, default="Student",null=False)
    student_number = models.CharField(max_length = 20,default = "",null=False)
    def __str__(self):
        return self.name

