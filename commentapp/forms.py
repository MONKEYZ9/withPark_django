from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        # 왜 필드가 이거뿐이냐면 나머지는 외래키로 다 받아올 수 있으니까
        fields = ['content']