from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world , how are u! Are you fine?")
