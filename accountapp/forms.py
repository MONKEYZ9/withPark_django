# UserCreationForm 이걸 상속받아서 커스터마이징을 해주자
from django.contrib.auth.forms import UserCreationForm


#  유저 네임의 칸을 비활성화해주는거야
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs): # 선택적 매개변수를 넣게 된다.
        super().__init__(*args, **kwargs) # super 메소드를 이용해서 UserCreationForm 부모클래스의 init를 가져온다.
        # 여기까지 다른 점은 부모에서 사용한걸 그대로 사용하고

        # 안에 있는 친구중에 username의 속성중에 disabled 속성을 True로 설정해서 안보이게끔 해준다는 거야
        self.fields['username'].disabled = True

