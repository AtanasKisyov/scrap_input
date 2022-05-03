from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.contrib.auth import views as auth_views, get_user_model

from scrap_input.user.models import Profile


AuthUser = get_user_model()


class LoginView(auth_views.LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('cockpit')

    def get_success_url(self):
        return reverse_lazy('cockpit')


class CreateUserView(LoginRequiredMixin, generic_views.CreateView):
    template_name = 'user/create_user.html'
    model = Profile
    fields = ('employee_id', 'first_name', 'last_name', 'user_role')
    success_url = reverse_lazy('cockpit')

    def post(self, request, *args, **kwargs):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        employee_id = request.POST['employee_id']
        username = f'{first_name}_{last_name}'
        user = AuthUser(
            username=username,
        )
        user.set_password('1234qwer')
        user.save()
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            employee_id=employee_id,
            user=user,
        )
        profile.save()
        return redirect('cockpit')
