from django.urls import path, include

from accountapp.views import hello_world

# 나중에 라우팅을 편하게 해주는 것을 하는 것
app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello world'),
]
