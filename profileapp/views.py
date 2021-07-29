from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello world')
    template_name = 'profileapp/create.html'

    # @login_required 이거는 클래스에서만 되는거여서 안된다.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'
    # detail로 가고 싶으나, pk가 없어 어떻게 해야 하나?
    # 메소드 하나를 오버라이드를 해줄거임
    # success_url = reverse_lazy('accountapp:hello world')

    # reverse와 reverse_lazy의 차이
    def get_success_url(self):
        # 'pk' : self.object.user.pk 이게 target_profile과 같다.
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
