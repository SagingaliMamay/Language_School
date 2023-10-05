
from django.contrib import admin
from django.urls import path
from .views import *
from django.core.mail import send_mail

urlpatterns = [
    path('', index, name='index'),
    path('details/', details, name='details'),
    path('content/', content, name= 'content'),
    path('level/', level, name='level'),
]
