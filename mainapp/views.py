from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from vendors.models import *
from .models import *
# Create your views here.
def registeruser(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newuser = myreg(username=name , email=email , password=password)
        newuser.save()
        return redirect("/adminpage")
    return render(request , 'main_reg.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        obj = myreg.objects.all().filter(username__icontains = username)
        if obj:
            return redirect("/adminpage/home")
        else:
            return redirect("/adminpage")
    return render(request , 'main_login.html')

def adminhome(request):
    user_obj = User.objects.all()
    vendor_obj = VendorReg.objects.all()
    return render(request , 'adminhome.html' , {'user_obj':user_obj , 'vendor_obj':vendor_obj})

