from django.shortcuts import render

from .models import Qcm
from .models import Question

# Create your views here.

def qcm(request):
    return render(request,'Qcm/qcm.html')
