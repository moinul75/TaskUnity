from django.shortcuts import render

# Create your views here. 
def home(request): 
    return render(request,'front-page.html')

def about(request): 
    return render(request, 'about-page.html') 
