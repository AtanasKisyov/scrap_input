from django.urls import path

from scrap_input.scrap_app.views.cockpit import CockpitView
from scrap_input.scrap_app.views.input import InputView, ScanInputView
from scrap_input.scrap_app.views.maintenance.maintenance import CreateProductionView, EditProductionView,\
    CreateAreaView, EditAreaView

urlpatterns = [
    path('', CockpitView.as_view(), name='cockpit'),
    path('cockpit/maintenance/production', CreateProductionView.as_view(), name='create_production'),
    path('cockpit/maintenance/production/int:<pk>', EditProductionView.as_view(), name='edit_production'),
    path('cockpit/maintenance/area', CreateAreaView.as_view(), name='create_area'),
    path('cockpit/maintenance/area/int:<pk>', EditAreaView.as_view(), name='edit_area'),
    path('input/', InputView.as_view(), name='input'),
    path('input/scan/', ScanInputView.as_view(), name='scan_input'),
]
