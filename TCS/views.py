from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def location1(request):
    return HttpResponse('<h1>location 1 is Quatar</h1>')

def location2(request):
    return HttpResponse('<h2>location 2 is Pune</h2>')