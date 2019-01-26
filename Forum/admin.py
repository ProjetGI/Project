from django.contrib import admin

# Register your models here.
from .forms import PublicationForm
from .models import Publication, Reponse



class PublicationFormAdmin(admin.ModelAdmin):
   form = PublicationForm
   # class Meta:
   # 	   model = Publication
   	   

admin.site.register(Reponse)
admin.site.register(Publication, PublicationFormAdmin)