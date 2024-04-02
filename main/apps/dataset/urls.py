from django.urls import path

from . import views

urlpatterns = [
    path(
        "datasets.create/<int:user_id>/",
        views.create_dataset,
        name="create_dataset",
    ),
    path("datasets.list/", views.read_all_datasets, name="read_all_datasets"),
    path(
        "datasets.info/<int:dataset_id>", views.get_dataset, name="get_dataset"
    ),
    path(
        "datasets.delete/<int:dataset_id>",
        views.delete_dataset,
        name="delete_dataset",
    ),
    path(
        "datasets.update/<int:dataset_id>",
        views.update_dataset,
        name="update_dataset",
    ),
    path(
        "datasets.metadata.update/<int:dataset_id>",
        views.update_dataset_metadata,
        name="update_dataset",
    ),
    path(
        "datasets.files.create/<int:user_id>",
        views.add_dataset_file,
        name="add_dataset_file",
    ),
    path(
        "datasets.files.delete/<int:user_id>/<int:file_id>",
        views.delete_dataset_file,
        name="delete_dataset_file",
    ),
    # * For now, pass both the user_id and dataset_id as path params
    path(
        "datasets.comments.create/<int:dataset_id>/<int:user_id>",
        views.create_comment,
        name="create_comment",
    ),
    path(
        "datasets.comments.update/<int:comment_id>",
        views.update_comment,
        name="update_comment",
    ),
    path(
        "datasets.comments.delete", views.delete_comment, name="delete_comment"
    ),
    path(
        "datasets.likes.create/<int:user_id>",
        views.create_like,
        name="create_like",
    ),
    path(
        "datasets.likes.delete/<int:user_id>",
        views.delete_like,
        name="delete_like",
    ),
    path(
        "datasets.bookmarks.create/<int:user_id>/",
        views.create_bookmark,
        name="create_bookmark",
    ),
    path(
        "datasets.bookmarks.delete/<int:user_id>/",
        views.delete_bookmark,
        name="delete_bookmark",
    ),
]

# /datasets.create
# /datasets.update
# /datasets.delete
# /datasets.archive
# /datasets.info
# /datasets.list
# /datasets.download
# /datasets.approve
# /datasets.publish
# /datasets.unPublish
# /datasets.removeApproval
# /datasets.listForAdmin
# /datasets.listForSuperAdmin
