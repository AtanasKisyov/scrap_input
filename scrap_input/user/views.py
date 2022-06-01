from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.contrib.auth import views as auth_views, get_user_model

from scrap_input.common_logic.mixins import CustomLoginRequiredMixin
from scrap_input.scrap_app.models import Area, Production
from scrap_input.user.models import UserProfile


AuthUser = get_user_model()


class LoginView(auth_views.LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('cockpit')

    def get_success_url(self):
        return reverse_lazy('cockpit')


class CreateUserView(generic_views.CreateView):
    template_name = 'user/create_user.html'
    model = UserProfile
    fields = ('employee_id', 'first_name', 'last_name', 'area', 'production')
    success_url = reverse_lazy('cockpit')

    def post(self, request, *args, **kwargs):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        employee_id = request.POST['employee_id']
        area_id = request.POST['area']
        area = Area.objects.get(id=area_id)
        production_id = request.POST['production']
        production = Production.objects.get(id=production_id)
        username = employee_id
        user = AuthUser(
            username=username,
        )
        user.set_password('1234qwer')
        user.save()
        profile = UserProfile(
            first_name=first_name,
            last_name=last_name,
            employee_id=employee_id,
            area=area,
            production=production,
            user=user,
        )
        profile.save()
        return redirect('cockpit')


class EditUserView(CustomLoginRequiredMixin, generic_views.UpdateView):
    template_name = 'user/update_user.html'
    model = UserProfile
    fields = ('employee_id', 'first_name', 'last_name', 'user_role', 'area', 'production')
    success_url = reverse_lazy('list_users')


class DeleteUserView(CustomLoginRequiredMixin, generic_views.DeleteView):
    template_name = 'user/delete_user.html'
    model = UserProfile
    success_url = reverse_lazy('list_users')

    def post(self, request, *args, **kwargs):
        path = request.path
        user_id = path.split(":")[1]
        profile = UserProfile.objects.get(id=user_id)
        user = AuthUser.objects.get(id=profile.user_id)
        user.delete()
        return redirect('list_users')


class ListUsersView(CustomLoginRequiredMixin, generic_views.ListView):
    template_name = 'user/list_users.html'
    model = UserProfile

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'employees':
                UserProfile.objects.order_by('employee_id')
        }
