from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *
import bcrypt


# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def registration_process(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags='reg')
        print(errors)
        return redirect('/')
    new_user = User(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=bcrypt.hashpw(request.POST['password'].encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8')
        #Password.objects.create(pwd = password.decode('utf-8') 
        #user = User.objects.get(id = new_user.id)
    )
    new_user.save()
    request.session['id'] = new_user.id 
    request.session['first_name']= new_user.first_name
    return redirect('/')

def login_process(request):
    login_errors = User.objects.login_validator(request.POST)
    if len(login_errors):
        for key, value in login_errors.items():
            messages.error(request, value, extra_tags='login')
        return redirect('/')
    #request.POST['password'].encode('utf-8')
    
    request.session['id'] = User.objects.filter(email=request.POST['email'])[0].id
    request.session['first_name']= User.objects.get(email=request.POST['email']).first_name 
    return redirect('/packages')

def packages(request):
    the_packages = Packages.objects.all()
    context = {
       'packages': the_packages
    }
    print(len(the_packages))
    return render(request, 'app1/packages.html', context)

def new(request):
    return render(request, 'app1/new.html')
    

def create(request):
    if request.method=='POST':
        Packages.objects.create(
        package_name=request.POST['package_name'], 
        package_cost=request.POST['package_cost'])
    return redirect('/packages')

def edit(request, package_id):
    the_packages = Packages.objects.get(id=package_id)
    context = {
        'package': the_packages
    }
    return render(request, 'app1/edit.html', context)

def update(request, package_id):
    x = Packages.objects.get(id=package_id)
    x.package_cost = request.POST['cost']
    x.save()
    return redirect('/packages')

def delete(request, package_id):
    Packages.objects.get(id=package_id).delete()
    return redirect('/packages') 
