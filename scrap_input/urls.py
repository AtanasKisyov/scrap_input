from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scrap_input.scrap_app.urls')),
    path('auth/', include('scrap_input.user.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
