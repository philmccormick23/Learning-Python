from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string

# the index function is called when root is visited

def index(request):
    if 'count' not in request.session:
        request.session['count']=0

    return render(request, 'survey_form/page.html')

def process(request, methods=['POST']):
    request.session['name']=request.POST['name']
    request.session['email']=request.POST['email']
    request.session['Location']=request.POST['Location']
    request.session['Language']=request.POST['Language']
    request.session['count'] +=1
    return redirect('/result')

def result(request):

    return render(request, 'survey_form/create.html')
