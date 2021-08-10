from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

@method_decorator(login_required, 'get') # get은 들어가면 안된다.
@method_decorator(login_required, 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    # Models의 서버에서 받아와야하는것들을 받아오자
    def form_valid(self, form):
        form.instance.writer = self.request.user
        # 서버에서 받아온 것을 가져올 수 있게끔 해줬어
        # pk의 숫자만 가지고 할 수 있게
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)


    def get_success_url(self):
        #  성공했을때 어디로 할지 정해주자
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        #  성공했을때 어디로 할지 정해주자
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
