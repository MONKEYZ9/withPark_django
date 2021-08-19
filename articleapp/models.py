from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               # 외래키 개념으로 간다. user랑 연결된게 있으면
                               # user.ariticle 이런식으로
                               related_name='article', null=True)

    # 프로젝트를 연결했어
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)

    title = models.CharField(max_length=200, null=True) # 제목 없어도 된다.
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True) # Text는 varchar2보다 큰 개념

    # 디비 내에서 자동으로 날짜를 입력해줄 수 있는거
    create_at = models.DateField(auto_now_add=True)
