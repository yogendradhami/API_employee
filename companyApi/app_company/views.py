from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("This is homepage")