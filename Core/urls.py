from django.urls import path  
from .views import * 

app_name = 'Core'

urlpatterns = [
    path('about/',about, name='about')
]
