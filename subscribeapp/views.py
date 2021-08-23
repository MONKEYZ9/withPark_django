from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, 'get') # get은 들어가면 안된다.
class SubscriptionView(RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])

        subscription = Subscription.objects.filter(user=user,
                                                    project=project)
        if subscription.exists():
            subscription.delete()
        else:
            # new_hello_world = HelloWorld()
            # new_hello_world.text = temp
            # new_hello_world.save()
            # 이걸 짧게 해놓은거야
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk':kwargs['project_pk']})


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    # 글을 아티클 글을 가져올거니까
    model = Article # 이렇게 하면 내가 구독한 거 말고도 다 보여줘
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    # def get_context_data(self, *, object_list=None, **kwargs):
    # 이걸 안쓰는 이유는 모든 것을 가져오는 것이다.
    # 아래는 원하는 것만 골라서 쓸 수 있다.
    def get_queryset(self):
        # Subscription이 유저와 프로젝트를 연결해놨어               project만 리스트로 저장하겠다.
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
        # 구독중인 리스트 안에 있는 글을 필터링을 해준다는 거야
        article_list = Article.objects.filter(project__in=project_list)
        return article_list