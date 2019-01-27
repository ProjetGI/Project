from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView,
    CreateView,DeleteView )
from .forms import PublicationForm, ReponseForm
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


class ReponseCreateView(CreateView):
    queryset = Reponse.objects.all()
    form_class = ReponseForm
    template_name = 'Forum/create_reponse.html'
    success_url = reverse_lazy('forum')
    # fields = [
    #         "rep_publication",
    #         "reponse"
    #     ]

class ReponseDeleteView(DeleteView):
    model = Reponse
    template_name = 'Forum/confirm_delete_rep.html'
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
    liste_reponses = Reponse.objects.all().filter(rep_publication=pk)
    context = {
    "object":obj,
    "liste_reponses":liste_reponses
    }
    return render(request,'Forum/publication.html',context)
    # return render(request,'Forum/reponse.html')

class Counter:
    numReponse = 1

    def increment(self):
        self.numReponse += 1
        return ''