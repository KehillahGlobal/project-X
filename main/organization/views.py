from django.shortcuts import render
from django.http import HttpResponse
import organization.organization_dao as organization_dao
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

def success_response(data):
    return JsonResponse(data)

def failure_response(message):
    return JsonResponse({"message" : message})

# Organization Management endpoints
@csrf_exempt
def create_org(request, admin_id):
    """
    Endpoint to create organization
    """
    data = json.loads(request.body)

    # perform validation
    success, org = organization_dao.create_org(data, admin_id)

    if not success_response:
        return failure_response("Failed to create organization")
    
    return success_response(org.serialize())


@csrf_exempt
def delete_org(request, org_id):
    """
    Endpoint to delete organization by id
    """
    deleted, org = organization_dao.delete_org(org_id)

    if not deleted: #TODO:only admin/super admin can delete it 
        return failure_response("Failed to delete organization")

    return success_response(org.serialize())


@csrf_exempt
def update_org(request, org_id):
    """
    Endpoint to update organization by id
    """
    data = json.loads(request.body)
    updated, org = organization_dao.update_org(org_id, data)

    if not updated:
        return failure_response("Failed to update organization")

    return success_response(org.serialize())


@csrf_exempt
def get_org(request, org_id):
    """
    Endpoint to get organization by id
    """
    success, org = organization_dao.get_org(org_id)

    if not success:
        return failure_response("Failed to get organization")
    
    return success_response(org.serialize())


@csrf_exempt
def add_org_member(request, admin_id):
    """
    Endpoint to get organization by id
    """
    org_data = json.loads(request.data)
    success, member = organization_dao.add_org_member(admin_id, org_data)

    if not success:
        return failure_response("Failed to add member")
    return success_response(member.serialize())


@csrf_exempt
def remove_org_member(request, admin_id):
    """
    Endpoint to get organization by id
    """
    org_data = json.loads(request.data)

    success, member = organization_dao.remove_org_member(admin_id, org_data)

    if not success:
        return failure_response("Failed to remove member")
    
    return success_response(member.serialize())


