from django.urls import path  
from .views import * 

app_name = 'Project_Management'

urlpatterns = [
    path('project-list',projectList, name='project-list'), 
    path('project-details',projectDetails,name='details-prjects')
]
