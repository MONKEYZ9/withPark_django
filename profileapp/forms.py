from django.forms import ModelForm



# ModelForm 이라는 걸 받아오고
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    # Meta는 이미지같은걸 실제로 픽셀로 되어있는 데이터인데
    # 외적인 요소를 표현하는 것이 Meta
    # 어떻게 구성이 된다는 것을 이야기하는 것
    class Meta:
        model = Profile
        #  3가지 필드를 입력을 받을 거임
        #user같은 경우 이미 있는 것을 가지고 오는 것 foriegn 키랑 같다
        fields = ['image', 'nickname', 'message']

        
