from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView
from likeapp.views import LikeArticleView

app_name = 'likeapp'

urlpatterns = [
    path('article/<int:article_pk>', LikeArticleView.as_view(), name='article_like'),
]