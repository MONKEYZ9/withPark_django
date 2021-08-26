from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


# 트랜젝션화 하려면
@transaction.atomic
def db_transaction(user, article):
    article.like += 1
    article.save()

    like_record = LikeRecord.objects.filter(user=user,
                                            article=article)
    # 좋아요가 눌러져있다면
    if like_record.exists():
    #     일부러 에러를 나게 해서 except로 가게끔 할 거다
        raise ValidationError('like already exist.')

    #  좋아요는 눌러
    LikeRecord(user=user, article=article).save()

# 로그인한 사람만 확인 하게
@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    # RedirectView 를 사용함으로 다시 이 페이지로 돌아오도록 하려고
    # 어디에든 붙여서 만들 수 있다.
    def get(self, request, *args, **kwargs):
        user = request.user
        # 'article_pk'를 확보한 객체의 pk를 가져와서 그것을 확인하겠다.
        article = Article.objects.get(pk=kwargs['article_pk'])

        try:
            # 좋아요 반영됨
            db_transaction(user, article)
            # messages.add_message(request, level=messages.SUCCESS, message='좋아요!')
            messages.add_message(request, messages.SUCCESS, '좋아요!')
        except ValidationError:
            #좋아요가 반영되지 않은 부분
            # messages.add_message(request, level=messages.ERROR, message='이미 눌려있습니다.')
            messages.add_message(request, messages.ERROR, '이미 눌려있습니다.')
            # def add_message(request: {_messages},
            #                 level: Any,
            #                 message: Any,
            #                 extra_tags: str = '',
            #                 fail_silently: bool = False) -> Any

            return HttpResponseRedirect(reverse('articleapp:detail',
                                                kwargs={'pk': kwargs['article_pk']}))


        return super().get(request, *args, **kwargs)

    # 리다이렉 할때 어디로 갈지
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})
