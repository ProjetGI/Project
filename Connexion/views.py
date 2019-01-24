from django.shortcuts import render

from django.http import HttpResponse,Http404

def accueil(request):
    return render(request,'Connexion/templates/index.html',locals())

def login(request):
    return render(request,'Connexion/templates/login.html',locals())

def signup(request):
    return render(request,'Connexion/templates/signUp.html',locals())

def about(request):
    return render(request,'Connexion/templates/about.html',locals())

def contact(request):
    return render(request,'Connexion/templates/contact.html',locals())

