from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CustomLoginRequiredMixin(LoginRequiredMixin):

    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get_login_url(self):
        return reverse_lazy('login')
