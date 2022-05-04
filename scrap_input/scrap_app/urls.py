from django.urls import path

from scrap_input.scrap_app.views.cockpit import CockpitView
from scrap_input.scrap_app.views.input import InputView, ScanInputView

urlpatterns = [
    path('cockpit/', CockpitView.as_view(), name='cockpit'),
    path('input/', InputView.as_view(), name='input'),
    path('input/scan/', ScanInputView.as_view(), name='scan_input'),
]
