from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

# 1. 간단히 뷰를 먼저 만드는데
# 1-1 함수를 만들자
# 응답을 되돌려 주는 건데 그냥 응답을 되돌려준거 뿐이야
# 2. 라우팅을 해줘야지 -> 어떻게 만드냐 -> urls에서 한다는 거야


#  get post 방식에 따라 다르게 해야 하니까 if로 할 것이다.
from accountapp.models import HelloWorld


def hello_world(req):
    if req.method == 'POST':
        temp = req.POST.get("input_text")
        new_hello_world = HelloWorld() # 모델에서 가져왔어
        new_hello_world.text = temp
        new_hello_world.save() # 새로운 헬로 월드라는게 만들어 졌는데 이걸 객체를 보내줄거라는거야


        return render(req, 'accountapp/hello_world.html',
                    context={'new_hello_world': new_hello_world})
    else:
        # 홈페이지에 접근할때는 보통 get 방식을 쓴다.
        return render(req, 'accountapp/hello_world.html',
                    context={'text':'GET METHOD'})

