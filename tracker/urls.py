from django.contrib import admin
from django.urls import path,include 
from Core.views import home

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',include('Core.urls')),
    path('',home, name='home'), 
    path('accounts/',include('account.urls')), 
    path('project/',include('Project_Management.urls')),
]
