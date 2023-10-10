from django.shortcuts import render
from .models import *


# Home page

def index(request):
    return render(request, 'index.html', {})


def details(request):
    return render(request, 'details.html', {})


def content(request):
    return render(request, 'content.html', {})


def level(request):
    return render(request, 'level.html', {})


# About us

def about(request):
    return render(request, 'about.html', {})


# Articles

def article(request):
    # Here I render all articles from db
    posts = Article.objects.all()
    return render(request, 'article.html', {'posts': posts})

# Add Page/articles

def addpage(request):
    return render(request,'addpage.html',{})


# Contact

def contact(request):
    return render(request,'contact.html',{})


def login(request):
    return render(request,'login.html',{})