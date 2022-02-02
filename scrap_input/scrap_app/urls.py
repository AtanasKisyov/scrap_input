from django.urls import path
from .views import home_page, login_page, input_page, overview_page

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('input/', input_page, name='input'),
    path('overview/', overview_page, name='overview'),
]
