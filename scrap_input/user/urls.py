from django.urls import path

from scrap_input.user.views import LoginView, CreateUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
]
