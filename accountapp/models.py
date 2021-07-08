from django.db import models

# Create your models here.

# models.Model 상속을 받을 거임
# 새로운 디비안에 내용을 만들거야
class HelloWorld(models.Model):
    text = models.CharField(max_length=255) #이게 varchar랑 같은 거
