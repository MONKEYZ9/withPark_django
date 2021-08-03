from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

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
