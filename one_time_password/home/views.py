from django.shortcuts import render
from django.conf import settings 
from django.core.mail import send_mail
import random
def home(request):
    return render(request,'home.html')
def email(request):
    global m
    email=request.POST['email']
    subject='donotreply'
    n=random.randint(1000,9999)
    m=str(n)
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,m,email_from,recipient_list)
    return render(request,'login.html')
def login(request):
    if request.method=="POST":
        otp=request.POST['otp']
        print(otp)
        print(m)
        if m==otp:
            return render(request,'welcome.html')
    else:
        return render(request,'login.html')



