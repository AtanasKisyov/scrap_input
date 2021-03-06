from django.views import generic as generic_views

from scrap_input.common_logic.mixins import CustomLoginRequiredMixin


class CockpitView(CustomLoginRequiredMixin, generic_views.TemplateView):
    template_name = 'cockpit/cockpit.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
