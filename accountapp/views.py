from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

# 1. 간단히 뷰를 먼저 만드는데
# 1-1 함수를 만들자
# 응답을 되돌려 주는 건데 그냥 응답을 되돌려준거 뿐이야
# 2. 라우팅을 해줘야지 -> 어떻게 만드냐 -> urls에서 한다는 거야

def hello_world(request):
    return render(request, 'accountapp/hello_world.html')

