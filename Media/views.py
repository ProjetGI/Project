from django.shortcuts import render,redirect
from django.http import HttpResponse


def cours(request):
   if request.user.username :
        return render(request,'Media/cours.html',locals())
   else :
        return redirect("/accueil/login/")

def cours_page(request):
     if request.user.username :
        return render(request,'Media/cours_page.html')
     else : 
        return redirect("/accueil/login/")

