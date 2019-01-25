from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

from django import forms
from django.views.generic import CreateView

from .models import Cours
from .models import CasCliniques

from Connexion.models import stagiare


def cours(request):
   if request.user.username :
        cours_list = Cours.objects.all()
        context = {'cours_list': cours_list}
        return render(request,'Media/cours.html',context)
   else :
        return redirect("/accueil/login/")

def cours_page(request):
     if request.user.username :
         cours = Cours.objects.get(id=cours_id)
         context = {'cours':cours}
         return render(request, 'Media/cours_page.html',context)
     else : 
        return redirect("/accueil/login/")

def cas_cliniques(request):
   if request.user.username :
         cas_cliniques_list = CasCliniques.objects.all()
         context = {'cours_list': cas_cliniques_list}
         return render(request, 'Media/cas_cliniques.html',context)
   else : 
        return redirect("/accueil/login/")

def cas_clinique_page(request,cas_clinique_id):
   if request.user.username :
         cas_clinique = CasCliniques.objects.get(id=cas_clinique_id)
         context = {'cours':cas_clinique}
         return render(request, 'Media/cas_clinique_page.html',context)
   else : 
        return redirect("/accueil/login/")
        

class CoursCreateView(CreateView):
    model= Cours
    fields = ['title','description','category','support_pdf','video_src']
   
def get_success_url(self):
            return reverse('cours-page', kwargs={'cours_id' : self.object.pk})
        

class CasCliniquesCreateView(CreateView):
    model= CasCliniques
    fields = ['title','description','category','support_pdf','corrige_src','video_src']

    def get_success_url(self):
        return reverse('cas-clinique-page', kwargs={'cas_clinique_id' : self.object.pk})



def removeCours(request,cours_id):
    Cours.objects.filter(id=cours_id).delete()
    return cours(request)

def removeCasCliniques(request,cours_id):
    CasCliniques.objects.filter(id=cours_id).delete()
    return cas_cliniques(request)
