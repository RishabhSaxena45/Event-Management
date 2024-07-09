from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import authenticate , login , logout  
from .models import *
# Create your views here.

def registeruser(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newuser = VendorReg(username=name , email=email , password=password)
        newuser.save()
        return redirect("/vendor")
    return render(request , 'register.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        obj = VendorReg.objects.all().filter(username__icontains = username)
        if obj:
            return redirect("/vendor/home")
        else:
            return redirect("/vendor")
    return render(request , 'login.html')

def home(request):
    return render(request , 'vendorhome.html')

def addproduct(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        price = request.POST.get('uprice')
        desc = request.POST.get('udesc')
        obj = VendorItem(name=name , price=price , desc=desc)
        obj.save()
        return redirect('/vendor/checkitem')
    return render(request , 'add.html')

def checkitem(request):
    obj = VendorItem.objects.all()
    return render(request , 'checkitem.html' , {'obj':obj})

def logoutvendor(request):
    return redirect('/vendor')