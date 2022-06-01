from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import generic as generic_views

from scrap_input.common_logic.mixins import CustomLoginRequiredMixin
from scrap_input.scrap_app.models import ScrapTable, Material
from scrap_input.scrap_app.utils import update_user_scrap_weight


class InputView(CustomLoginRequiredMixin, generic_views.CreateView):

    VALIDATION_ERROR_MESSAGE = 'Material does not exist!'
    template_name = 'inputs/input.html'
    model = ScrapTable
    fields = ('material_number', 'scrap_quantity')

    def post(self, request, *args, **kwargs):

        try:

            material_number = request.POST['material_number']
            material = Material.objects.get(material_number=material_number)

            scrapper_id = request.user.id
            material_description = material.material_description
            quantity = int(request.POST.get('scrap_quantity', 1))
            material_price = material.material_price * quantity
            material_weight = material.material_weight * quantity

            scrap = ScrapTable(
                material_number=material_number,
                material_description=material_description,
                scrap_quantity=quantity,
                scrap_price=material_price,
                scrap_weight=material_weight,
                scrapper_id=scrapper_id
            )

            scrap.save()
            update_user_scrap_weight(scrapper_id, material, quantity)

        except ObjectDoesNotExist:

            context = {
                'form': self.get_form(),
                'error': self.VALIDATION_ERROR_MESSAGE,
            }
            return render(request, template_name=self.template_name, context=context)

        return redirect('input')


class ScanInputView(CustomLoginRequiredMixin, generic_views.CreateView):

    VALIDATION_ERROR_MESSAGE = 'Material Does Not Exist!'
    SCAN_QUANTITY_VALUE = 1
    template_name = 'inputs/scan_input.html'
    model = ScrapTable
    fields = ('material_number', )

    def post(self, request, *args, **kwargs):

        try:
            material_number = request.POST['material_number']
            material = Material.objects.get(material_number=material_number)

            scrapper_id = request.user.id
            material_description = material.material_description
            quantity = ScanInputView.SCAN_QUANTITY_VALUE
            material_price = material.material_price * quantity
            material_weight = material.material_weight * quantity

            scrap = ScrapTable(
                material_number=material_number,
                material_description=material_description,
                scrap_quantity=quantity,
                scrap_price=material_price,
                scrap_weight=material_weight,
                scrapper_id=scrapper_id,
            )

            scrap.save()
            update_user_scrap_weight(request.user, material, quantity)

        except ObjectDoesNotExist:

            context = {
                'form': self.get_form(),
                'error': self.VALIDATION_ERROR_MESSAGE,
            }
            return render(request, template_name=self.template_name, context=context)

        return redirect('scan_input')
