from django.shortcuts import render
from django.http import HttpResponse


def cours(request):
    return render(request,'Media/cours.html')

def cours_page(request):
    return render(request,'Media/cours_page.html')

