from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request=None):
    return HttpResponse("<h1>Hello, world</h1>")
