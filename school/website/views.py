from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.mail import send_mail,BadHeaderError
from .forms import ContactForm




# Home page

def index(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("the form is send")
            return render ('index.html')

    else:
        form = ContactForm
    return render(request, 'index.html', {'form': form})


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
    return HttpResponse("add page")


# Contact

def contact(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cmessage = request.POST['cmessage']

        return render(request,'base.html',{'cmessage':cmessage,'cemail':cemail,'cname':cname})


    else:
        return HttpResponse('base.html')


def login(request):
    return HttpResponse('login.html')

# to show post by clickin on "read" button


def show_post(request, post_slug):
    post = get_object_or_404(Article, slug=post_slug)

    context = {
        'post' : post,
        #'menu' : menu,
        'title': post.title,
        'cat_selected' : post.cat_id,
    }
    return render(request, 'post.html', context=context)