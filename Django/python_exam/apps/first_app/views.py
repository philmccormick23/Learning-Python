from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string
import random
from .models import User
# the index function is called when root is visited

def index(request):
    dictionary = {
        'users' : User.objects.all()
    }
    
    return render(request, 'index.html', dictionary)

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        u=User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=request.POST['password'])
        request.session['id']=u.id
        request.session['name']=u.name
        request.session['count']=0
        
        return redirect('/pokes')

def success(request):
    dictionary = {
        'users' : User.objects.all(), 

    }
    return render(request,'success.html', dictionary)

def login(request):
    users=User.objects.all()
    for thing in users:
        if request.POST['email'] == thing.email and request.POST['password'] == thing.password:
            u=User.objects.get(email=request.POST['email'])
            request.session['id']=u.id
            request.session['name']=u.name 
    return redirect('/pokes')

def poke(request, id):
    x = Poke.objects.create(poker=User.objects.get(id=request.session['id']), poked=User.objects.get(id=id))
    x.counter+=1
    x.save()
    return redirect('/pokes')