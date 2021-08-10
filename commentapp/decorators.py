from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *arg, **kwargs):
#      댓글 작성자와 요청을 보낸 유저를 둘다 있어야 함
                                            # kwargs가 딕셔너리이니까 값을 가져오려면 키를 가지고
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        if target_comment.writer == request.user:
            return func(request, *arg, **kwargs)
        else:
            return HttpResponseForbidden()
    return  decorated
