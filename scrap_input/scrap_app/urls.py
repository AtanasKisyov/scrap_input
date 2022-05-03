from django.urls import path

from scrap_input.scrap_app.views import OverviewView, InputView

urlpatterns = [
    path('cockpit/', OverviewView.as_view(), name='cockpit'),
    path('input/', InputView.as_view(), name='input'),
]
