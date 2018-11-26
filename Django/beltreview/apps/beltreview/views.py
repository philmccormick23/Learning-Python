from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string
import random
from .models import *

def index(request):
    dictionary = {
        'users' :  User.objects.all()
    }
    #for u in User.objects.all():
        #u.delete()
    
    return render(request, 'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        u= User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=request.POST['password'])
        request.session['id']=u.id
        request.session['name']=u.name
        return redirect('/books')

def login(request):
    users = User.objects.all()
    for thing in users: 
        if request.POST['email'] == thing.email and request.POST['password'] == thing.password:
            u=User.objects.get(email=request.POST['email'])
            request.session['id']=u.id
            request.session['name']=u.name
    return redirect('/books')


def success(request):
    dictionary  = {
        'books' : Book.objects.all(),
        'reviews' : Review.objects.all()
    }
    return render(request,'success.html', dictionary)

def add(request):
    return render(request,'add.html')


def addBook(request):
    u=Book.objects.create(title=request.POST['title'], author=request.POST['author'], review=request.POST['review'], rating=request.POST['rating'], user=User.objects.get(id=request.session['id']))
    return redirect('/books/'+str(u.id))

def number(request, id):
    dictionary  = {
        'books' : Book.objects.get(id=id),
        'reviews': Review.objects.filter(book=id)
    }
    return render(request,'newBook.html', dictionary)

def addReview(request):
    print(request.POST['id'])
    Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user=User.objects.get(id=request.session['id']), book=Book.objects.get(id=request.POST['id']))
    return redirect('/books/'+str(request.POST['id']))