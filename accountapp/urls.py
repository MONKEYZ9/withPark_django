from django.urls import path, include

from accountapp.views import hello_world, AccountCreateView

# 나중에 라우팅을 편하게 해주는 것을 하는 것
app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello world'),
    #   회원가입으로 가는 페이지로 가는 경로
    path('create/', AccountCreateView.as_view(), name='create')
    # as_view 를 사용하게 되면 클래스를 부를 수 있다
]
