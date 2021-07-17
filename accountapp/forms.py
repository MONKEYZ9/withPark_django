# UserCreationForm 이걸 상속받아서 커스터마이징을 해주자
from django.contrib.auth.forms import UserCreationForm


#  유저 네임의 칸을 비활성화해주는거야
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
