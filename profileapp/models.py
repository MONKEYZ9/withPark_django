from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    # 유저와 1대 1로 만들어야 해 연결하고자 하는 것을 가져와야 함
    # 회원탈퇴했을때 on_delete로 연결된 것을 CASCADE (종속) 걸겠다는 것,
    # models.CASCADE와 같이 삭제 정책을 사용하는 것이 있다.
    #  related_name='profile'는 1대1로 연결되어있는데 이거랑 연결된 객체에 하고 싶어 
    #  그때 profile.text로 profile 모델의 text 컬럼을 가져올 수 있게 한다는 거야
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # media 폴더 안에다가 profile이라는 폴더를 만들어 주고 이 안에 넣겠다는 거야
    # 이미지가 없어도 상관없이 가겠다는거야
    image = models.ImageField(upload_to='profile/', null=True)
    # 20자의 nickname을 만들고 unique로 해주자는 거야 null=True은 False가 맞는거 같은데 일다 이렇게 넘어가자
    nickname = models.CharField(max_length=20, unique=True, null=True)
    # 메세지 없다고 저장 안되는게 아닌 되게끔
    message = models.CharField(max_length=255, null=True)
    # class Meta:
