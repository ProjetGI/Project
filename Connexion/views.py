from django.shortcuts import render

from django.http import HttpResponse,Http404

def accueil(request):
    return render(request,'Connexion/templates/index.html',locals())


