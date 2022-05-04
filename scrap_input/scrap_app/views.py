from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.views import generic as generic_views

from scrap_input.scrap_app.models import ScrapTable, Material


class OverviewView(generic_views.TemplateView):
    template_name = 'cockpit/cockpit.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InputView(LoginRequiredMixin, generic_views.CreateView):
    template_name = 'input.html'
    model = ScrapTable
    fields = ('material_number', 'scrap_quantity')

    def post(self, request, *args, **kwargs):
        material_number = request.POST['material_number']
        material = Material.objects.get(material_number=material_number)

        if not material:
            raise ValidationError('Material does not exist!')

        material_description = material.description
        quantity = int(request.POST['quantity'])
        material_price = material.material_price * quantity
        material_weight = material.material_weight * quantity
        scrap = ScrapTable(
            material_number=material_number,
            material_description=material_description,
            quantity=quantity,
            material_price=material_price,
            material_weight=material_weight,
        )

        scrap.save()

        return redirect('input')
