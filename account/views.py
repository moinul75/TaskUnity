from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib.auth import authenticate,login
# Create your views here. 
def SignUp(request):  
    if request.user.is_authenticated: 
        return redirect('Project_Management:project-list') 
    if request.method == 'POST': 
        username = request.POST.get('username','') 
        email    = request.POST.get('email','') 
        password = request.POST.get('password','')  
        print("User required fields: ",username,email,password)
        user  = User(username=username,email=email)   
        user.set_password(password)
        print(user)
        user.save()  
        return redirect('account:login') 
    return render(request,'signup.html') 


def Login(request):   
    if request.user.is_authenticated: 
        return redirect('Project_Management:project-list') 
    if request.method == 'POST': 
        email    = request.POST.get('email','') 
        password = request.POST.get('password','')  
        user     = authenticate(request,email=email,password=password)  
        if not user: 
            return HttpResponse("User is not found") 
        else: 
            login(request,user)  
            return redirect('Project_Management:project-list') 
    next_param = request.GET.get('next', '') 
    if next_param:  
        print(next_param) 
        return render(request,'login.html',{'next_param':next_param})
            
         
    return render(request, 'login.html') 


