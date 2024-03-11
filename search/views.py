from django.shortcuts import render
from django.http import JsonResponse
from .search_client import make_microservice_request

def search_books(request):
    author = request.GET.get('author', '')
    title = request.GET.get('title', '')

    # Make a request to the microservice
    response_data = make_microservice_request(author, title)

    return JsonResponse(response_data)
