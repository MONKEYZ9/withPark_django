from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                # 댓글에 접근할때 related_name으로 접근한다. null이여도 상관없게
                                related_name='comment', null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)
    # 댓글 내용은 있게끔
    content = models.TextField(null=False)
    # 댓글 날짜를 찍어주려고 auto_now_add를 True로 해서 자동으로 찍히게끔
    created_at = models.DateTimeField(auto_now_add=True)
