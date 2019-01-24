from django.contrib import admin
from .models import administrateur,stagiare,formateur
admin.site.register(administrateur)
#admin.site.register(stagiare)
admin.site.register(formateur)

class StagiareAdmin(admin.ModelAdmin):
   list_display   = ('id', 'user_id', 'faculte')
   list_filter    = ('id', 'user_id', 'faculte')
   

admin.site.register(stagiare, StagiareAdmin)