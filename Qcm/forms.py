from django import forms 
from django.forms import modelformset_factory

from .models import Qcm, Question

class QcmModelForm(forms.ModelForm):
    class Meta:
        model = Qcm
        fields = ('title', 'description',)
        labels = {
            'title': 'Qcm Title',
            'description': 'Qcm description',
        }
        widgets = {
            'title': forms.TextInput(
                attrs ={
                    'class': 'form-control',
                    'placeholder': 'Entrer titre du qcm'
                }
            ),
            'description': forms.TextInput(
                attrs ={
                    'class': 'form-control',
                    'placeholder': 'Entrer la description du qcm'
                }
            ),
        }

QuestionFormset = modelformset_factory(
    Question,
    fields=('question','choice_1','choice_2','choice_3','choice_4', 'answer'),
    labels = {
        'question': 'question',
        'choice_1': 'choix 1',
        'choice_2': 'choix 2',
        'choice_3': 'choix 3',
        'choice_4': 'choix 4',
        'answer': 'answer',
    },
    extra=1,
    widgets = {
        'question': forms.TextInput(
            attrs ={
                'class': 'form-control',
                'placeholder': 'Entrer la question'
            }
        ),
        'choice_1': forms.TextInput(
            attrs ={
                'class': 'form-control',
                'placeholder': 'Entrer le choix 1'
            }
        ),
        'choice_2': forms.TextInput(
            attrs ={
                'class': 'form-control',
                'placeholder': 'Entrer le choix 2'
            }
        ),
        'choice_3': forms.TextInput(
            attrs ={
                'class': 'form-control',
                'placeholder': 'Entrer le choix 3'
            }
        ),
        'choice_4': forms.TextInput(
            attrs ={
                'class': 'form-control',
                'placeholder': 'Entrer le choix 4'
            }
        ),
        'answer': forms.TextInput(
            attrs ={
                'class': 'answer',
                'type': 'hidden',
            }
        ),
    }

)