from django.urls import path
from TCS.views import *

urlpatterns = [
    path('location1/',location1,name='location1'),
    path('location2/',location2,name='location2'),
]
