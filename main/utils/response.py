from django.http import JsonResponse


def success_response(data):
    return JsonResponse(data)


def error_response(message):
    return JsonResponse({"error": message})
