"""
URL configuration for ITcompanies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from DELL.views import *
from HCL.views import *

import IBM,TCS

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('location1/',location1,name='location1'),
    path('location2/',location2,name='location2'),
    path('place1/',place1,name='place1'),
    path('place2/',place2,name='place2'),
    
    path('IBM/',include('IBM.urls')),
    path('TCS/',include('TCS.urls')),
]
