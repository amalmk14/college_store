from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect



# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('base')
        else:
            messages.info(request,'Invalid Details. Please enter the correct Username and Password.')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,)
                user.save();

        else:
            messages.info(request,'Password not matched')
            return redirect('register')
        return redirect('login')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')