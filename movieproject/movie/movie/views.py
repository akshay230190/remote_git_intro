from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from random import randint
from django.conf import settings



def index(request):
    #return HttpResponse("welcome to home page")
    return render(request,"index.html")

