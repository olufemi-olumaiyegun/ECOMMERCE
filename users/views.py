from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterNewUser
from .models import User
from django.core.mail import send_mail

# Create your views here.
from django.core.exceptions import ValidationError
from django.db import models

def register(request):
    # saving form data to database

    if request.method=='POST':
        form = RegisterNewUser(request.POST)



        if form.is_valid():
         #automatically secures login data and saves new user
            #email = form.cleaned_data['email']


         #   send_mail(email, 'Use %s to confirm your email' %form.confirmation_key)
            # User gets email, passes the confirmation_key back to your server

          #  form.confirm_email(form.confirmation_key)
         #   form.is_confirmed()  # True
            form.save()
            messages.success(request, f'Account created! You can now login')

            return redirect('signin')

    #creating user form
    else:
        form=RegisterNewUser()
    return render(request,'register.html', {'form':form})


