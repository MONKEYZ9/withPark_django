from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/create.html'

    # form을 보냈을때 하는거
    def form_valid(self, form):
        # 정상적으로 되는 걸 확인해주고 그대로 보내주자
        #
        form.instance.writer = self.request.user
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    # 어떻게 접근할지를 보는것
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    # 업데이트하면 원래 자기꺼로 돌아가야지
    def get_success_url(self):
        # kwargs는 딕셔너리고
        # pk를 받아온다.
        return reverse('articleapp:detail', kwargs={'pk' : self.object.pk})

class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'