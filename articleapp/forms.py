from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # 입력 받을 것을 정리해주자
        fields = ['title', 'image', 'content']
        
