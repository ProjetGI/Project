from django.shortcuts import render
from django.forms import modelformset_factory
from django.views.generic.edit import CreateView

from .models import Qcm
from .models import Question

# Create your views here.

def add_qcm(request):
    questionFormSet = modelformset_factory(Question, fields=('question','choice1','choice2'))
    formset = questionFormSet()
    return render(request, 'Qcm/add_qcm.html', {'formset': formset})


def show_qcm(request):
    qcm_objects = Qcm.objects.all()
    context = {
        'qcm_objects': qcm_objects
    }
    return render(request, "Qcm/qcm.html", context)

def show_question(request, id):
    question_objects = Question.objects.all().filter(qcm_id=id)
    context = {
        'qcm': Qcm.objects.all().filter(id=id)[0],
        'question_objects': question_objects
    }
    return render(request, "Qcm/question.html", context)