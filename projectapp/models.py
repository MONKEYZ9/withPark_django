from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    # 설명없어도 된다는 거 안적어도 작성할 수 있게
    decription = models.CharField(max_length=200, null=True, blank=True)
    # media 에 폴더를 생성하고 만들어지게끔
    image = models.ImageField(upload_to='project/', null=False)
    # auto_now_add 생성되는 순간을 찍어줌
    created_at = models.DateTimeField(auto_now_add=True)