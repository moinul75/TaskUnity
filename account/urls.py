from django.urls import path 
from .views import *

app_name = 'account'

urlpatterns = [
    path('sign-up',SignUp,name='sign-up'), 
    path('login/',Login,name='login'),
]
