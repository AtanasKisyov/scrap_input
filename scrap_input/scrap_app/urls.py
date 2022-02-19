from django.urls import path
from .views import home_page, input_page, overview_page

urlpatterns = [
    path('', home_page, name='home'),
    path('input/', input_page, name='input'),
    path('overview/', overview_page, name='overview'),
]
