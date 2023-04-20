from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.

# this method for few api using JsonResponse
def Home(request):
    library= [
        "book",
        "copy",
        "novel",
        "litrature",
    ]
    return JsonResponse(library, safe=False)