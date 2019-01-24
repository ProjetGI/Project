from django.shortcuts import render
from django.http import HttpResponse


def cours(request):
    return render(request,'Media/cours.html')

