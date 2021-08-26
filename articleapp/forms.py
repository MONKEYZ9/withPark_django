from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    # 장고안의 폼을 들고와야 한다.
    # CharField가 어떤 형식으로 뽑아줄 것인지
    # Textarea(attrs= 로 속성을 지정할건데 그게
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'min-height:10rem;'
                                                                    'text-align:left'}))

    class Meta:
        model = Article
        # 입력 받을 것을 정리해주자
        fields = ['title', 'image', 'project', 'content']
