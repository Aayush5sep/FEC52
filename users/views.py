from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Individual,Organization
from django.contrib.auth.decorators import login_required

# Create your views here.

def signuppage(request):
    return render(request,'signup.html')

def orgnsignuppage(request):
    return render(request,'signuporg.html')

def signupuser(request):
    if request.method=='POST':
        # Obtaining Data From The HTML Form
        username=request.POST['username']
        password=request.POST['password']
        cfpassword=request.POST['cfpassword']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone = request.POST['phone']
        age = request.POST['age']
        address = request.POST['address']
        town = request.POST['town']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']

        if password != cfpassword:
            messages.error(request,"Passwords do not match")
            return redirect("/user/signuppage")

        # Default User Auth Save
        newuser = User.objects.create_user(username,email,password)
        newuser.first_name=fname
        newuser.last_name=lname
        newuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)

        # Saving Extra Details About User
        userd=Individual(user=user,name=fname + " " + lname,phone=phone,age=age,address=address,town=town,zipcode=zipcode,country=country,latitude=latitude,longitude=longitude)
        userd.save()

        messages.success(request,"User Account Created Successfully")
        return redirect("/")
    else:
        return HttpResponse("Creating new user account failed !")
    
def signuporgn(request):
    if request.method=='POST':
        # Obtaining Data From The HTML Form
        username=request.POST['username']
        password=request.POST['password']
        cfpassword=request.POST['cfpassword']
        email=request.POST['email']
        name=request.POST['name']
        desc=request.POST['desc']
        contact = request.POST['contact']
        alt_contact=request.POST['alt_contact']
        address = request.POST['address']
        town = request.POST['town']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']

        if password != cfpassword:
            messages.error(request,"Passwords do not match")
            return redirect("/user/signuppage")

        # Default User Auth Save
        newuser = User.objects.create_user(username,email,password)
        newuser.first_name=name
        newuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)

        # Saving Extra Details About User
        userd=Organization(user=user,name=name,desc=desc,contact=contact,alt_contact=alt_contact,address=address,town=town,zipcode=zipcode,country=country,latitude=latitude,longitude=longitude)
        userd.save()

        messages.success(request,"Organization Account Created Successfully")
        return redirect("/")
    else:
        return HttpResponse("Creating new organization account failed ! Kindly try again after refreshing the website.")

def loginpage(request):
    return render(request,'login.html')

def loginuser(request):
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect("/")
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")

@login_required(login_url='user/login/')
def logoutuser(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect("/")