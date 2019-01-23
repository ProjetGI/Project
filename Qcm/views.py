from django.shortcuts import render

from .models import Qcm
from .models import Question

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")