from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def location1(request):
    return HttpResponse('<h1>Location 1 is Banglore</h1>')

def location2(request):
    return HttpResponse('<h2>Location 2 is Hyderabad</h2>')