from django.shortcuts import render 
from django.contrib.auth.decorators import login_required 

# Create your views here. 
@login_required
def projectList(request): 
    return render(request,'project-list.html')  

@login_required 
def projectDetails(request): 
    return render(request,'project-details.html') 


