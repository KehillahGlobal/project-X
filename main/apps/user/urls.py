from django.urls import path

from . import views

urlpatterns = [
    path("users.create", views.create_user, name="create_user"),
    path(
        "users.listForSuperAdmin",
        views.users_list_super_admin,
        name="users_list_super_admin",
    ),
    path("users.listForAdmin", views.users_list_admin, name="users_list_admin"),
    path("users.list", views.users_list, name="users_list"),
    path("users.info/<int:user_id>/", views.get_user, name="get_user"),
    path("users.delete/<int:user_id>/", views.delete_user, name="delete_user"),
    path("users.update/<int:user_id>/", views.update_user, name="update_user"),
    path(
        "users.roles.update/<int:user_id>/",
        views.update_user_role,
        name="update_user_roles",
    ),
    path("users.tags.update<int:user_id>/", views.create_tag, name="create_tag"),
]
