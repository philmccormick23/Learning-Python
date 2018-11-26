from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string
import random
from .models import Course
# the index function is called when root is visited

def index(request):
    dictionary = {
        'courses' : Course.objects.all()
    }
    return render(request, 'index.html', dictionary)

def process(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
        'course' : Course.objects.get(id=id)
    }
    return render(request, 'destroy.html', context)

def delete(request, id):
    b=Course.objects.get(id=id)
    b.delete()
    return redirect('/')