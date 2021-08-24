from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord

# 로그인한 사람만 확인 하게
@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    # RedirectView 를 사용함으로 다시 이 페이지로 돌아오도록 하려고
    # 어디에든 붙여서 만들 수 있다.
    def get(self, request, *args, **kwargs):
        user = request.user
        # 'article_pk'를 확보한 객체의 pk를 가져와서 그것을 확인하겠다.
        article = Article.objects.get(pk=kwargs['article_pk'])

        like_record = LikeRecord.objects.filter(user=user,
                                                article=article)
        # 좋아요가 눌러져있다면
        if like_record.exists():
            return HttpResponseRedirect(reverse('articleapp:detail',
                                                kwargs={'pk': kwargs['article_pk']}))

        # 좋아요 누르고 db에 바로 저장
        LikeRecord(user=user, article=article).save()
        # article의 like 컬럼의 로우에도 적용 하고 저장
        article.like += 1
        article.save()
        return super().get(request, *args, **kwargs)

    # 리다이렉 할때 어디로 갈지
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})
