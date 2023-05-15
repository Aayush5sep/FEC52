from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from users.models import Organization
from .models import Camp,Donations,Receivings,Donor,Receiver

# Create your views here.

def NewCampPage(request):
    return render(request,'camp/newcamp.html')

@login_required(login_url='/user/loginpage')
def NewCamp(request):
    if request.method=='POST':
        orgn = Organization.objects.filter(orgn=request.user)
        if len(orgn)==0:
            return HttpResponse("Only Organizations can setup a Camp")
        title = request.POST['title']
        start = request.POST['start']
        end = request.POST['end']
        contact = request.POST['contact']
        address = request.POST['address']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        image = request.POST.get('image')

        camp = Camp(title=title,orgn=orgn[0],start=start,end=end,contact=contact,address=address,latitude=latitude,longitude=longitude,image=image)
        camp.save()

        messages.success(request,"Camp at the specified location has been setup successfully")
        return redirect('/')
    
    else:
        return HttpResponse("Invalid Request. Access Denied")