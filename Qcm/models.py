from django.db import models
from django.forms.widgets import CheckboxSelectMultiple

from django.forms import ModelForm

# Create your models here.

class Qcm(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    dateCreated = models.DateField(editable=False, auto_now_add=True)
    dateEdited = models.DateField((""), auto_now=True)
    
class Question(ModelForm):
    id_qcm = models.ForeignKey(Qcm, on_delete="CASCADE")
    question = models.TextField()
   
class Choice(ModelForm):
    id_question = models.ForeignKey(Question, on_delete="CASCADE")
    choice = models.CharField(max_length=150)
    answer = models.BooleanField()