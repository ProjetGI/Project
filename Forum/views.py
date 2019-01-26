from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView,
    CreateView,DeleteView )
from .forms import PublicationForm
from .models import Publication, Reponse
from django.urls import reverse_lazy

# Create your views here.


class PublicationCreateView(CreateView):
    queryset = Publication.objects.all()
    form_class = PublicationForm
    template_name = 'Forum/create_publication.html'
    success_url = reverse_lazy('forum')
    # fields = [
    #         "titre",
    #         "sujet"
    #     ]

class PublicationDeleteView(DeleteView):
    model = Publication
    template_name = 'Forum/confirm_delete_pub.html'
    success_url = reverse_lazy('forum')
    # fields = [
    #         "titre",
    #         "sujet"
    #     ]

def reponse(request, pk=4):
    obj = Reponse.objects.get(pk=pk)
    context = {
    "object":obj
    }
    return render(request,'Forum/reponse.html',context)
    # return render(request,'Forum/reponse.html')

def forum(request):
    liste_publications = Publication.objects.all()
    context = {
    "liste_publications":liste_publications
    }
    return render(request,'Forum/forum.html',context)

# def create_publication(request):

def publication(request, pk=4):
    obj = Publication.objects.get(pk=pk)
    context = {
    "object":obj
    }
    return render(request,'Forum/publication.html',context)
    # return render(request,'Forum/reponse.html')
