from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string

# the index function is called when root is visited

def index(request):
    response="Hello World"

    return HttpResponse(response)
