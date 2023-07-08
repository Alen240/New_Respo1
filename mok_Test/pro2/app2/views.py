from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from app2.models import product

# Create your views here.
def home(request):
    k=product.objects.all()
    return render(request,'home.html',{"k":k})
def usersignup(request):
    # if request.user.authenticated:
    #     return home(request)
    # else:
    #     if request.method=='POST':
    #         name=request.POST.get('username')
    return render(request,'usersignup.html')
def userlogin(request):
    return render(request,'userlogin.html')
def productview(request,pk):
    k=product.objects.filter(id=pk)
    return render(request,'productview.html',{"k":k})
def cart(request):
    return render(request,'cart.html')
