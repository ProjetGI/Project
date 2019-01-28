from django.db import models

from django.forms import ModelForm

class Qcm(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    dateCreated = models.DateField(editable=False, auto_now_add=True)
    dateEdited = models.DateField((""), auto_now=True)
    
class Question(models.Model):
    id_qcm = models.ForeignKey(Qcm, on_delete="CASCADE")
    question = models.TextField()
    choice_1 = models.CharField(max_length=150)
    choice_2 = models.CharField(max_length=150)
    choice_3 = models.CharField(max_length=150, blank=True)
    choice_4 = models.CharField(max_length=150, blank=True)
    answer = models.CharField(max_length=4)