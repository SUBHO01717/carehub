from django.shortcuts import render, redirect

from .forms import *

# Create your views here.

def home(request):
    
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=AppointmentForm()
    context = {

            'form': form,
        }

    return render(request, 'index.html', context)

def about (request):
    return render( request, 'about.html')

def nurses (request):
    return render( request, 'nurses.html')

def assistants (request):
    return render( request, 'assistants.html')

def agency (request):
    return render( request, 'agency.html')

def recruitment (request):
    return render( request, 'recruitment.html')

def training (request):
    return render( request, 'training.html')

def compliance (request):
    return render( request, 'compliance.html')

def registration(request):
    if request.method == "POST":
        form = RegistrationFrom(request.POST,request.FILES )
        if form.is_valid():
            form.save()
           
            return redirect('/registration/')
    form=RegistrationFrom()
    context = {

            'form': form,
        }
    return render(request, 'registration.html', context)


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('/home/')
    form=AppointmentForm()
    context = {

            'form': form,
        }
    return render(request, 'index.html', context)


def contact (request):
    if request.method =="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/contact/')
        
    form=ContactForm()
    context = {

            'form': form,
        }
    return render( request, 'contact.html', context)