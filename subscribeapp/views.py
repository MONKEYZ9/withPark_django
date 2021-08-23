from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, 'get') # get은 들어가면 안된다.
class SubscriptionView(RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])

        subscription = Subscription.objects.filter(user=user,
                                                    project=project)
        if subscription.exists():
            subscription.delete()
        else:
            # new_hello_world = HelloWorld()
            # new_hello_world.text = temp
            # new_hello_world.save()
            # 이걸 짧게 해놓은거야
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk':kwargs['project_pk']})
