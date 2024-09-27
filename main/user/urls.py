from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('users/get', views.get_users, name='get_users'),
    path('users/create', views.create_user, name='create_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/update/<int:user_id>/', views.update_user, name='update_user'),
    path('users/update-user-roles/<int:user_id>/', views.update_user_role, name='update_user_roles'),
]