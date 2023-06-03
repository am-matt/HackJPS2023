from django.shortcuts import render
from django.http import HttpResponse


def forum(request):
    return HttpResponse("Hello, world. You're looking at the forums.")

# Create your views here.
