from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def signup(req):
    if req.method == 'POST':

        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password1 = req.POST['password1']
        password2 = req.POST['password2']
    # return HttpResponse("Hello")
        if User.objects.filter(username=username).exists():
            messages.info(req,"username's already taken")
            return redirect('/accounts/register/')
        elif User.objects.filter(email=email).exists():
            messages.info(req,"email id already exists with different user")
            return redirect('/accounts/register/')
        elif password1 != password2:
            messages.info(req,"password does not match")
            return redirect('/accounts/register/')
        else:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password2,email=email)
            return redirect('/')

def login(req):
    username = req.POST['username']
    password = req.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(req,user)
        return redirect('/')
    else:
        messages.info(req,'incorrect user credentials')
        return redirect('/accounts/login/')


def showRegistrationForm(req):
        return render(req,'register.html')


def showLoginPage(req):
    return render(req,'login.html')

def logout(req):
    auth.logout(req)
    print("new feature implemented")
    return redirect('/')

