
from django.contrib import admin
from django.urls import path

from . import views
from .views import *
from django.core.mail import send_mail

urlpatterns = [
    path('', index, name='home'),
    path('details/', details, name='details'),
    path('content/', content, name='content'),
    path('level/', level, name='level'),
    path('about/', about, name='about'),
    path('article/', article, name='article'),
    path('addpage/', addpage, name='addpage'),
    path('login/', login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('post/<slug:post_slug>/', show_post, name='post')
]
