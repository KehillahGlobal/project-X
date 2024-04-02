import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import apps.user.crud as crud
from utils.response import error_response, success_response


# Test endpoint
def home(request):
    return render(request, "pages/homepage.html")


# User Management Endpoints
@csrf_exempt
def update_user_role(request, user_id):
    """
    Endpoint to update user roles
    """
    data = json.loads(request.body)
    user_roles = crud.update_user_role(user_id, data)

    if not user_roles:
        return

    return JsonResponse(user_roles)


@csrf_exempt
def create_user(request):
    """
    Endpoint to create user
    """
    data = json.loads(request.body)

    # perform validation
    user = crud.create_user(data)

    if not user:
        return error_response("Failed to create user")

    return success_response(user.serialize())


@csrf_exempt
def users_list(request):
    """
    Get all users
    """
    users = crud.get_users()
    return success_response(users)


@csrf_exempt
def users_list_admin(request):
    """
    Get all users
    """
    users = crud.get_users()
    return success_response(users)


@csrf_exempt
def users_list_super_admin(request):
    """
    Get all users
    """
    users = crud.get_users()

    return success_response(users)


@csrf_exempt
def delete_user(request, user_id):
    """
    Endpoint to delete user by id
    """
    user = crud.delete_user(user_id)

    if not deleted:
        return error_response("Failed to delete user")

    return success_response(user.serialize())


@csrf_exempt
def update_user(request, user_id):
    """
    Endpoint to update user by id
    """
    data = json.loads(request.body)
    updated, user = crud.update_user(user_id, data)

    if not updated:
        return error_response("Failed to update user")

    return success_response(user.serialize())


@csrf_exempt
def get_user(request, user_id):
    """
    Endpoint to get user by id
    """
    if not user_id:
        return error_response("Invalid user ID.")

    user = crud.get_user(user_id=user_id)
    if not user:
        return error_response("Failed to get user")

    return success_response(user.serialize())


@csrf_exempt
def user_login(request):
    """
    Endpoint to login user
    """


@csrf_exempt
def user_logout(request):
    """
    Endpoint to logout user
    """


@csrf_exempt
def create_tag(request, user_id):
    """
    Endpoint to delete tag
    """
    tag_data = json.loads(request.body)
    tag = user_dao.create_tag(user_id, tag_data)
    return JsonResponse(tag.serialize())


# Data Submission Endpoints
# Visualization Endpoints
# Data Download and Export Endpoints

# Data Submission Endpoints
# Visualization Endpoints
# Data Download and Export Endpoints
# Search and Filtering Endpoints
