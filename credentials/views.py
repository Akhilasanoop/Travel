from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('login')
        else:
            messages.info(request,"invalid")
            return redirect('/')
    return render(request,"login.html")

def register (request):
    if request.method=='POST':
        username1=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username1).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(username=email).exits():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username1,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                return redirect('/')

    else:
        messages.info(request, 'password not matching')
    return  render(request,"register.html")

def logout(request):
    auth.logout(request)
    return render('/')