from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout  
from .models import *
def registeruser(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newuser = User.objects.create_user(username=name , email=email , password=password)
        newuser.save()
        return redirect("/")
    return render(request , 'register.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(username=username , password=password)
        if user:
            login(request,user)
            return redirect("/home")
        else:
            return redirect("/")
    return render(request , 'login.html')

def home(request):
    return render(request , 'home.html' )

def addevent(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        contact = request.POST.get('ucontact')
        event_type = request.POST.get('utype')
        guest = request.POST.get('uguest')
        event_date = request.POST.get('udate')
        obj = EventModel(name = name , email=email , contact = contact , event_type=event_type , guest = guest , event_date=event_date)
        obj.save()
        return redirect('/cart')
    return render(request , 'addevent.html')

def cartlist(request):
    obj = EventModel.objects.filter(name = request.user)
    print(obj)
    return render(request , 'cart.html' , {'obj':obj})
        
def addguest(request):
    if request.method == "POST":
        eventhead = request.POST.get('uname')
        guest1 = request.POST.get('uguestone')
        guest1age = request.POST.get('uguestoneage')
        guest1gender = request.POST.get('uguestonegender')
        guest2 = request.POST.get('uguesttwo')
        guest2age = request.POST.get('uguesttwoage')
        guest2gender = request.POST.get('uguesttwogender')
        guest3 = request.POST.get('uguestthree')
        guest3age = request.POST.get('uguestthreeage')
        guest3gender = request.POST.get('uguestthreegender')
        guest4 = request.POST.get('uguestfour')
        guest4age = request.POST.get('uguestfourage')
        guest4gender = request.POST.get('uguestfourgender')
        obj = Guest(eventhead=eventhead , guest1=guest1 , guest1age=guest1age , guest1gender=guest1gender , guest2=guest2 , guest2age=guest2age , guest2gender=guest2gender , guest3 = guest3 , guest3age = guest3age , guest3gender = guest3gender , guest4=guest4 , guest4age=guest4age , guest4gender=guest4gender)
        obj.save()
        return redirect('/home')
    return render(request , 'addguest.html')

def logoutuser(request):
    logout(request)
    return redirect('/')