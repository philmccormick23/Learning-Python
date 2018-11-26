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
    
    return render(request,'index.html', dictionary)
    
def user(request, id):
    context = {
        'user' : User.objects.get(id=id)
    }

    return render(request,'user.html', context)

def process(request, methods=['POST']):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], tags=request.POST['tags'])
    return redirect('/')

def new(request):
    dictionary = {
        'users' : User.objects.all()
    }
    return render(request,'new.html', dictionary)

def edit(request, id):
    context = {
        'user' : User.objects.get(id=id)
    }
    return render(request,'edit.html', context)

def update(request, id):
    b=User.objects.get(id=id)
    b.first_name=request.POST['first_name']
    b.last_name=request.POST['last_name']
    b.email=request.POST['email']
    b.save()
    print(b.tags.all())
    return redirect('/')

def tag(request, id):
    x=User.objects.get(id=id)
    #for i in range(10):

    tags='hello world'
    splitTags=tags.split()
    x.tags.add(str(splitTags)) ####Result = ['hello', 'world']
    x.save()
    userTags=x.tags.all()
    for tags in userTags:
        print(tags)
    return redirect('/')

def delete(request, id):
    b=User.objects.get(id=id)
    b.delete()
    return redirect('/')