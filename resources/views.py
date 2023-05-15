from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import Organization,Individual
from django.http import HttpResponse
from .models import Book,Clothes,Miscellaneous,BookReq,ClothesReq,MiscReq
from django.contrib import messages

# Create your views here.

@login_required(login_url='/user/loginpage')
def DonateBook(request):
    if request.method=='POST':
        title = request.POST['title']
        desc = request.POST['desc']
        rating = request.POST['rating']
        image = request.POST.get('image')
        classno = request.POST['classno']
        orgn = False
        address=""
        helperid=""

        org = Organization.objects.filter(orgn = request.user)
        if len(org)!=0:
            orgn = True
            address = org[0].address
            helperid = org[0].uid
        else:
            ind = Individual.objects.get(user=request.user)
            address = ind.address
            helperid = ind.uid  

        donation = Book(title=title,desc=desc,rating=rating,image=image,classno=classno,orgn=orgn,address=address,helperid=helperid)
        donation.save()

        messages.success(request,"That is a great work you just did buddy :)")
        return redirect('/')

    else:
        return HttpResponse("Invalid Request. Access Denied")


@login_required(login_url='/user/loginpage')
def DonateClothes(request):
    if request.method=='POST':
        title = request.POST['title']
        desc = request.POST['desc']
        rating = request.POST['rating']
        image = request.POST.get('image')
        orgn = False
        address=""
        helperid=""

        org = Organization.objects.filter(orgn = request.user)
        if len(org)!=0:
            orgn = True
            address = org[0].address
            helperid = org[0].uid
        else:
            ind = Individual.objects.get(user=request.user)
            address = ind.address
            helperid = ind.uid  

        donation = Clothes(title=title,desc=desc,rating=rating,image=image,orgn=orgn,address=address,helperid=helperid)
        donation.save()

        messages.success(request,"That is a great work you just did buddy :)")
        return redirect('/')

    else:
        return HttpResponse("Invalid Request. Access Denied")
    

@login_required(login_url='/user/loginpage')
def DonateMisc(request):
    if request.method=='POST':
        title = request.POST['title']
        desc = request.POST['desc']
        rating = request.POST['rating']
        image = request.POST.get('image')
        orgn = False
        address=""
        helperid=""

        org = Organization.objects.filter(orgn = request.user)
        if len(org)!=0:
            orgn = True
            address = org[0].address
            helperid = org[0].uid
        else:
            ind = Individual.objects.get(user=request.user)
            address = ind.address
            helperid = ind.uid  

        donation = Miscellaneous(title=title,desc=desc,rating=rating,image=image,orgn=orgn,address=address,helperid=helperid)
        donation.save()

        messages.success(request,"That is a great work you just did buddy :)")
        return redirect('/')

    else:
        return HttpResponse("Invalid Request. Access Denied")
    

def RequestBook(request):
    if request.method=='POST':
        id = request.POST['id']
        book = Book.objects.get(id=id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        whyneed = request.POST['whyneed']
        address = request.POST['address']

        req = BookReq(book=book,name=name,email=email,phone=phone,whyneed=whyneed,address=address)
        req.save()

        return HttpResponse("We have received and transfered your request. Kindly wait for an email regarding confirmation from the owner")
    
    else:
        return HttpResponse("Invalid Request. Access Denied")
    

def RequestClothes(request):
    if request.method=='POST':
        id = request.POST['id']
        clothes = Clothes.objects.get(id=id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        whyneed = request.POST['whyneed']
        address = request.POST['address']

        req = ClothesReq(clothes=clothes,name=name,email=email,phone=phone,whyneed=whyneed,address=address)
        req.save()

        return HttpResponse("We have received and transfered your request. Kindly wait for an email regarding confirmation from the owner")
    
    else:
        return HttpResponse("Invalid Request. Access Denied")
    

def RequestMisc(request):
    if request.method=='POST':
        id = request.POST['id']
        item = Miscellaneous.objects.get(id=id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        whyneed = request.POST['whyneed']
        address = request.POST['address']

        req = MiscReq(item=item,name=name,email=email,phone=phone,whyneed=whyneed,address=address)
        req.save()

        return HttpResponse("We have received and transfered your request. Kindly wait for an email regarding confirmation from the owner")
    
    else:
        return HttpResponse("Invalid Request. Access Denied")
    

def AllResources(request):
    books = Book.objects.filter(donated=False)
    clothes = Clothes.objects.filter(donated=False)
    misc = Miscellaneous.objects.filter(donated=False)

    # Filtering for closer to location can be done as well

    return render(request,'request.html',{'books':books,'clothes':clothes,'misc':misc})


@login_required(login_url='/user/loginpage')
def ResRequests(request):
    requests = []
    helperid = ""
    ind = Individual.objects.filter(user = request.user)
    is_orgn = False

    if len(ind)!=0:
        helperid = ind[0].uid
    else:
        orgn = Organization.objects.get(orgn = request.user)
        helperid = orgn.uid
        is_orgn = True
    
    books = Book.objects.filter(orgn=is_orgn,helperid=helperid)
    clothes = Clothes.objects.filter(orgn=is_orgn,helperid=helperid)
    misc = Miscellaneous.objects.filter(orgn=is_orgn,helperid=helperid)

    for book in books:
        bookreqs = BookReq.objects.filter(book=book).order_by('accepted')
        requests += [req for req in bookreqs]

    for clothe in clothes:
        clothereqs = ClothesReq.objects.filter(clothes=clothe).order_by('accepted')
        requests += [req for req in clothereqs]
    
    for mis in misc:
        misreqs = MiscReq.objects.filter(item=mis).order_by('accepted')
        requests += [req for req in misreqs]

    return render(request,'resources/allrequests.html',{'requests':requests})


@login_required(login_url='/user/loginpage')
def AcceptReq(request,rtype,id):

    userid = ""
    org = Organization.objects.filter(orgn = request.user)
    if len(org)!=0:
        helperid = org[0].uid
    else:
        ind = Individual.objects.get(user=request.user)
        helperid = ind.uid

    if rtype=="book":
        res = BookReq.objects.filter(id=id,book__helperid=helperid)
        if len(res)==0:
            return HttpResponse("Either no such item exists Or you do not have the ownership.")
        res[0].accepted = True
        res[0].save()
    elif rtype=="clothes":
        res = ClothesReq.objects.filter(id=id,clothes__helperid=helperid)
        if len(res)==0:
            return HttpResponse("Either no such item exists Or you do not have the ownership.")
        res[0].accepted = True
        res[0].save()
    elif rtype=="misc":
        res = MiscReq.objects.filter(id=id,item__helperid=helperid)
        if len(res)==0:
            return HttpResponse("Either no such item exists Or you do not have the ownership.")
        res[0].accepted = True
        res[0].save()
    else:
        return HttpResponse("Invalid Type Of Resource")
    
    messages.success(request,"The request has beena accepted. You may now share the item with the needy")
    return redirect('/')


@login_required(login_url='/user/loginpage')
def Donated(request,rtype,id):

    userid = ""
    org = Organization.objects.filter(orgn = request.user)
    if len(org)!=0:
        helperid = org[0].uid
    else:
        ind = Individual.objects.get(user=request.user)
        helperid = ind.uid

    if rtype=="book":
        res = BookReq.objects.filter(id=id,book__helperid=helperid)
        if len(res)==0:
            return HttpResponse("Either no such item exists Or you do not have the ownership.")
        res[0].sent = True
        res[0].book.donated = True
        res[0].save()
    elif rtype=="clothes":
        res = ClothesReq.objects.filter(id=id,clothes__helperid=helperid)
        if len(res)==0:
            return HttpResponse("Either no such item exists Or you do not have the ownership.")
        res[0].sent = True
        res[0].clothes.donated = True
        res[0].save()
    elif rtype=="misc":
        res = MiscReq.objects.filter(id=id,item__helperid=helperid)
        if len(res)==0:
            return HttpResponse("Either no such item exists Or you do not have the ownership.")
        res[0].sent = True
        res[0].item.donated = True
        res[0].save()
    else:
        return HttpResponse("Invalid Type Of Resource")
    
    messages.success(request,"The request has beena accepted. You may now share the item with the needy")
    return redirect('/')