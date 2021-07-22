from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk']) # 우리가 사용한 유저 객체에서
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden() # HttpResponseForbidden을 호출함으로
    return decorated # 함수 자체를 되돌리는 것이니까 ()를 함으로 호출하면 안된다
