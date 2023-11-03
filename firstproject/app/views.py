from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,("index.html"))

def ragistration(request):
    if request.method == 'POST':
        name =  request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            return HttpResponse("email alredy exists")
        elif User.objects.filter(phone=phone).exists():
            return HttpResponse("phone Number already exits")
        else:
            User.objects.create(name = name, email = email, phone = phone, password = password)
            return HttpResponse("User Created")
def table(request):
    data = User.objects.all()
    return render(request,"table.html",{"data":data})

def  userdelete(request,pk):
    User.objects.get(id=pk).delete()
    return redirect('/table/')

def table(request):
    data = User.objects.all()
    return render(request,"sing_up.html",{"data":data})



