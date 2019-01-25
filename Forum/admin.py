from django.contrib import admin

# Register your models here.

from .models import Publication, Reponse

admin.site.register(Publication)
admin.site.register(Reponse)
