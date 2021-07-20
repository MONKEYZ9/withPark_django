from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.

# 1. 간단히 뷰를 먼저 만드는데
# 1-1 함수를 만들자
# 응답을 되돌려 주는 건데 그냥 응답을 되돌려준거 뿐이야
# 2. 라우팅을 해줘야지 -> 어떻게 만드냐 -> urls에서 한다는 거야


#  get post 방식에 따라 다르게 해야 하니까 if로 할 것이다.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(req):
    # 로그인이 되어있는지 안되어있는지 확인하고 post가 되었는지를 보자는 거야
    if req.user.is_authenticated:

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
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):  # CreateView는 알아볼 필요가 있다.
    # 뭘 만들거냐 모델을 만들건데 장고에서 제공해주는 것이 있어 => User 
    model = User  # class AbstractUser(AbstractBaseUser, PermissionsMixin): 여기 함 들어가서 어떻게 되있나 봐봐라
    form_class = UserCreationForm  # 다 일일히 부르자
    success_url = reverse_lazy('accountapp:hello world')
    # 예전에 리다이렉 했을때랑 동일하게 reverse를 이용해서 주소를 적어줬어 그거랑 동일하게 하면 된다.
    # 근데 reverse를 바로 사용하면 안된다. 메소드에서 reverse를 부르는 것과 class에서 부르는 것은 엄연히 다르다는 거야
    template_name = 'accountapp/create.html'  # 회원가입 페이지 이름을 뭐로 할건지를 정해주는거
    #  우리는 로직을 만들고 라우팅을 했어
    # 이걸 우리는 urls.py에서 했었어


# 회원정보
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'  # 우리가 템플릿에서 사용하는 유저의 객체를 보는 것이다.
    template_name = 'accountapp/detail.html'


# 회원정보 업데이트
class AccountUpdateView(UpdateView):
    model = User  # class AbstractUser(AbstractBaseUser, PermissionsMixin): 여기 함 들어가서 어떻게 되있나 봐봐라
    # form_class = UserCreationForm # 업데이트 폼은 이전에 우리가 회원가입때 썼던 것을 쓸거야라고 했는데
    # 문제가 있어 ==> 그럼 아이디까지 바뀐다는 거야
    form_class = AccountUpdateForm  # 새롭게 만든 폼.py를 만들어서 옮겼어
    context_object_name = 'target_user'  # 우리가 템플릿에서 사용하는 유저의 객체를 보는 것이다.
    success_url = reverse_lazy('accountapp:hello world')  # detail로 가면 좋은데 detail에 갈 때
    # 지금 urls에서 path('update/<int:pk>', 로 pk를 받아야 하는 상황이야
    template_name = 'accountapp/update.html'

    #     로그인이 되어있는지 확인하자
    #     get과 post를 하는 것을 막기 위해서 하는 것니까
    def get(self, request, *args, **kwargs):
        # return super().get(request, *args, **kwargs) 현재는 지금 부모메소드를 사용한거야
        # 인증과정 추가한 것을 리턴해주자
        # 현재 로그인 중인지, 동일 인물인지
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            # 잘못된 곳으로 갔는 것을 확인해주는 것
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()


# 회원탈퇴
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    #     로그인이 되어있는지 확인하자
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
