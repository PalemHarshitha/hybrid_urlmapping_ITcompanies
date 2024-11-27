from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def place1(request):
    return HttpResponse('<h1>Location 1 is Chennai</h1>')

def place2(request):
    return HttpResponse('<h2>Location 2 is Mumbai</h2>')