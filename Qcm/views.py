from django.shortcuts import render,redirect
from django import forms

from .models import Qcm
from .models import Question
from .forms import QcmModelForm
from .forms import QuestionFormset

# Create your views here.

def add_qcm(request):
    if request.method == 'GET':
        qcmform = QcmModelForm(request.GET or None)
        formset = QuestionFormset(queryset=Question.objects.none())
    elif request.method =='POST':
        qcmform = QcmModelForm(request.POST)
        formset = QuestionFormset(request.POST)
        if qcmform.is_valid() and formset.is_valid():
            qcm = qcmform.save()
            for form in formset:
                question = form.save(commit=False)
                question.id_qcm = qcm
                question.save()
            return redirect('/qcm')
    return render(request, 'qcm/add_qcm.html', {
        'qcmform': qcmform,
        'formset': formset,
    })


def show_qcm(request):
    qcm_objects = Qcm.objects.all()
    context = {
        'qcm_objects': qcm_objects
    }
    return render(request, "Qcm/qcm.html", context)

def show_question(request, id):
    question_objects = Question.objects.all().filter(id_qcm=id)
    context = {
        'qcm': Qcm.objects.all().filter(id=id)[0],
        'question_objects': question_objects
    }
    return render(request, "Qcm/question.html", context)

