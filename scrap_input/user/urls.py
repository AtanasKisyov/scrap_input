from django.urls import path

from scrap_input.user.views import CreateUserView, EditUserView, ListUsersView, DeleteUserView, LoginView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('edit/int:<pk>', EditUserView.as_view(), name='edit_user'),
    path('delete/int:<pk>', DeleteUserView.as_view(), name='delete_user'),
    path('users/', ListUsersView.as_view(), name='list_users'),
    path('login/', LoginView.as_view(), name='login'),
]
