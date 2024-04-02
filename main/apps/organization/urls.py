from django.urls import path

from . import views

urlpatterns = [
    path("orgs.create/<int:admin_id>/", views.create_org, name="create_org"),
    path("orgs.info/<int:org_id>/", views.get_org, name="get_org"),
    path("orgs.delete/<int:org_id>/", views.delete_org, name="delete_org"),
    path("orgs/update/<int:org_id>/", views.update_org, name="update_org"),
    path(
        "orgs/add-org-member/<int:admin_id>/",
        views.add_org_member,
        name="add_org_member",
    ),
    path(
        "orgs/remove-org-member/<int:admin_id>/",
        views.remove_org_member,
        name="remove_org_member",
    ),
]
