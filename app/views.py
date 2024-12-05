from django.shortcuts import render,redirect
from .models import *
   
# Create your views here.

def user_index(request):

    e=Contact_Details.objects.all()

    return render(request,'index.html',{"e":e})

def user_contact(request):
    if request.method=='POST':
        a=request.POST.get("f_name")
        b=request.POST.get("l_name")
        c=request.POST.get("number")
        d=request.POST.get("address")

        Contact_Details.objects.create(
            first_name=a,
            last_name=b,
            mobile_number=c,
            address=d
        )

        return redirect("index_link")

    return render(request,'contact.html')