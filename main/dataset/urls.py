from django.urls import path
from . import views

urlpatterns = [

    path('datasets/<int:user_id>/', views.create_dataset, name = "create_dataset"),
    path('datasets/get/<int:dataset_id>/', views.get_dataset, name = "get_dataset"),
    path('datasets/delete/<int:dataset_id>/', views.delete_dataset, name = "delete_dataset"),
    path('datasets/update/<int:dataset_id>/', views.update_dataset, name = "update_dataset"),
    path('datasets/', views.get_all_datasets, name = "get_all_datasets"),
    path('files/delete/<int:user_id>/', views.delete_file, name = "delete_file"),
    path('files/<int:user_id>/', views.create_file, name = "create_file"),
    path('comments/delete/<int:user_id>/', views.delete_comment, name = "delete_comment"),
    path('comments/<int:user_id>/', views.create_comment, name = "create_comment"),
    path('likes/delete/<int:user_id>/', views.delete_like, name = "delete_like"),
    path('likes/<int:user_id>/', views.create_like, name = "create_like"),
    path('bookmarks/delete/<int:user_id>/', views.delete_bookmark, name = "delete_bookmark"),
    path('bookmarks/<int:user_id>/', views.create_bookmark, name = "create_bookmark"),
]