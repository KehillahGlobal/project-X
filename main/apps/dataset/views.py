import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import apps.dataset.crud as dataset_crud
from utils.errors import DatasetDoesNotExist, UserDoesNotExist
from utils.response import error_response


@csrf_exempt
def create_dataset(request, user_id):
    """
    Endpoint to create dataset
    """
    data = json.loads(request.body)
    try:
        dataset = dataset_crud.create_dataset(data, user_id)
        return JsonResponse(dataset)
    except UserDoesNotExist:
        return error_response("User does not exist.")


@csrf_exempt
def get_dataset(request, dataset_id):
    """
    Endpoint to get dataset by id
    """
    try:
        return JsonResponse(
            {"dataset": dataset_crud.read_dataset(dataset_id=dataset_id)},
        )
    except DatasetDoesNotExist:
        return error_response("Dataset does not exists")


@csrf_exempt
def update_dataset(request, dataset_id):
    """
    Endpoint to update dataset by id
    """
    data = json.loads(request.body)
    dataset = dataset_crud.update_dataset(dataset_id, data)

    return JsonResponse(dataset.serialize())


@csrf_exempt
def delete_dataset(request, dataset_id):
    """
    Endpoint to delete dataset by id
    """
    dataset = dataset_crud.delete_dataset(dataset_id)
    return JsonResponse(dataset.serialize())


@csrf_exempt
def update_dataset_metadata(request, dataset_id):
    """
    Endpoint to update dataset by id
    """
    data = json.loads(request.body)
    dataset = dataset_crud.update_dataset_metadata(dataset_id, data)

    return JsonResponse(dataset.serialize())


@csrf_exempt
def read_all_datasets(request):
    """
    Endpoint to get all datasets
    """
    all_datasets = dataset_crud.read_all_datasets()
    return render(request, "pages/data/catalog.html", all_datasets)


@csrf_exempt
def add_dataset_file(request, user_id, dataset_id):
    """
    Endpoint to delete file
    """
    file_data = json.loads(request.body)
    return JsonResponse(dataset_crud.create_file(user_id, dataset_id, file_data))


@csrf_exempt
def delete_dataset_file(request, file_id, user_id):
    """
    Endpoint to delete file
    """
    body = json.loads(request.body)
    return JsonResponse(dataset_crud.delete_dataset_file(body, file_id, user_id))


# Search and Filtering Endpoints
@csrf_exempt
def search_dataset_by_category(request):
    """
    Endpoint to search datasets by category
    """
    ...


@csrf_exempt
def filter_dataset_by_source(request):
    """
    Endpoint to filter datasets by source
    """


@csrf_exempt
def filter_dataset_by_date_range(request):
    """
    Endpoint to filter datasets by date range
    """


@csrf_exempt
def create_comment(request, dataset_id, user_id):
    """
    Endpoint to create comment
    """
    data = json.loads(request.body)
    comment = dataset_crud.create_comment(dataset_id, user_id, data)

    return JsonResponse(comment)


@csrf_exempt
def update_comment(request, comment_id):
    """
    Endpoint to update comment
    """
    data = json.loads(request.body)
    comment = dataset_crud.update_comment(comment_id, data)

    return JsonResponse(comment)


@csrf_exempt
def delete_comment(request, user_id):
    """
    Endpoint to delete file
    """
    comment_id = json.loads(request.body).get("comment_id")
    return JsonResponse(dataset_crud.delete_comment(user_id, comment_id))


# Like endpoints


@csrf_exempt
def create_like(request, user_id):
    """
    Endpoint to create like
    """
    data = json.loads(request.body)
    like = dataset_crud.create_like(user_id, data)
    return JsonResponse(like.serialize())


@csrf_exempt
def delete_like(request, user_id):
    """
    Endpoint to delete file
    """
    like_id = json.loads(request.body).get("like_id")
    return JsonResponse(dataset_crud.delete_like(user_id, like_id))


# Bookmark endpoints


@csrf_exempt
def create_bookmark(request, user_id):
    """
    Endpoint to create bookmark
    """
    data = json.loads(request.body)
    bookmark = dataset_crud.create_bookmark(user_id, data)
    return JsonResponse(bookmark.serialize())


@csrf_exempt
def delete_bookmark(request, user_id):
    """
    Endpoint to delete file
    """
    bookmark_id = json.loads(request.body).get("bookmark_id")
    return JsonResponse(dataset_crud.delete_bookmark(user_id, bookmark_id))


# TODO: Data Submission Endpoints
# TODO: Visualization Endpoints
# TODO: Data Download and Export Endpoints

# TODO: Data Submission Endpoints
# TODO: Visualization Endpoints
# TODO: Data Download and Export Endpoints
# TODO: Search and Filtering Endpoints
