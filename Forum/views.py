from django.shortcuts import render
from .models import Publication, Reponse
# Create your views here.


def reponse(request):
    # obj = Reponse.objects.get(id=1)
    # context = {
    # "object":obj
    # }
    # return render(request,'Forum/reponse.html',context)
    return render(request,'Forum/reponse.html')

def forum(request):
    liste_publications = Publication.objects.all()
    context = {
    "liste_publications":liste_publications
    }
    return render(request,'Forum/forum.html',context)