from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# 1. 간단히 뷰를 먼저 만드는데
# 1-1 함수를 만들자
# 응답을 되돌려 주는 건데 그냥 응답을 되돌려준거 뿐이야
# 2. 라우팅을 해줘야지 -> 어떻게 만드냐 -> urls에서 한다는 거야


#  get post 방식에 따라 다르게 해야 하니까 if로 할 것이다.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(req):
    if req.method == 'POST':
        temp = req.POST.get("input_text")
        new_hello_world = HelloWorld()  # 모델에서 가져왔어
        new_hello_world.text = temp
        new_hello_world.save()  # 새로운 헬로 월드라는게 만들어 졌는데 이걸 객체를 보내줄거라는거야

        # new_hello_world_list = HelloWorld.objects.all()  # 여러가지가 있다. objects를 가져와야 하는데 여러가지가 있는 편이다.
        # # 이걸 다 보내주는 거야

        # 리다이렉을 하게 되면 get에서 하고 있는 걸 다 받아내기에 굳이 할 필요가 없어

        # 리다이렉을 할거라는 거야
        # 렌더로 매번 주소를 적어서 보내는게 아니라 해당 라우팅으로 가게끔해서 get으로 보여주도록 한다
        # reverse 매소드를 가져와야 하는데 장고에서 제공하는 걸 가져오도록 한다.
        return HttpResponseRedirect(reverse('accountapp:hello world'))
        # return render(req, 'accountapp/hello_world.html',
        #               context={'new_hello_world': new_hello_world, 'new_hello_world_list': new_hello_world_list})
    else:
        new_hello_world_list = HelloWorld.objects.all()  # 여러가지가 있다. objects를 가져와야 하는데 여러가지가 있는 편이다.
        # post와 똑같이 리스트로 받아서 보여주도록 하자

        # 홈페이지에 접근할때는 보통 get 방식을 쓴다.
        return render(req, 'accountapp/hello_world.html',
                      context={'new_hello_world_list': new_hello_world_list})
