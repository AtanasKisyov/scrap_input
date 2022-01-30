from django.contrib import admin
from django.urls import path
from .scrap_app.views import home_page, login_page, input_page, scan_page, overview_page

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('login/', login_page),
    path('input/', input_page),
    path('scan/', scan_page),
    path('overview/', overview_page),
]
