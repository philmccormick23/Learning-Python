from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    banana = "placeholder to later display all the list of blogdfgldsjfgksdjfhg;sdkjfg"
    return HttpResponse(banana)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    response = "placeholder to display a new form to create a new blog"
    return redirect("/")

def number(request, number):
    response = number
    return HttpResponse(response)

def edit(request, number):
    response = 'placeholder to edit blog EDIT '+str(number)
    return HttpResponse(response)

def destroy(request, number):
    return HttpResponse('placeholder to edit blog DESTROY '+number)



