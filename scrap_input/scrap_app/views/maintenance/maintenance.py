from django.urls import reverse_lazy
from django.views import generic as generic_views

from scrap_input.scrap_app.models import Production, Area


class CreateProductionView(generic_views.CreateView):
    template_name = 'cockpit/maintenance.html'
    model = Production
    fields = ('production_name',)
    success_url = reverse_lazy('cockpit')


class EditProductionView(generic_views.UpdateView):
    template_name = 'cockpit/maintenance.html'
    model = Production
    fields = ('production_name',)
    success_url = reverse_lazy('cockpit')


class CreateAreaView(generic_views.CreateView):
    template_name = 'cockpit/maintenance.html'
    model = Area
    fields = ('area_name', 'production')
    success_url = reverse_lazy('cockpit')


class EditAreaView(generic_views.UpdateView):
    template_name = 'cockpit/maintenance.html'
    model = Area
    fields = ('area_name', 'production')
    success_url = reverse_lazy('cockpit')
