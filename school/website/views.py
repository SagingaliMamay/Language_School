from django.shortcuts import render, HttpResponse


# Home page

def index(request):
    return render(request, 'index.html',{})

def details(request):
    return render (request, 'details.html',{})

def content(request):
    return render (request,'content.html',{})

def level(request):
    return render (request, 'level.html',{})
