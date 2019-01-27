from django import forms

from .models import Publication,Reponse

class PublicationForm(forms.ModelForm):
	class Meta:
		model = Publication
		fields = '__all__'

class ReponseForm(forms.ModelForm):
	class Meta:
		model = Reponse
		fields = '__all__'