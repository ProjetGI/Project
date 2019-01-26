from django.contrib import admin
from .models import administrateur,stagiare,formateur

admin.site.register(formateur)

class StagiareAdmin(admin.ModelAdmin):
   list_display   = ('id', 'user_id', 'faculte')
   list_filter    = ('id', 'user_id', 'faculte')
   

admin.site.register(stagiare, StagiareAdmin)

class AdministrateureAdmin(admin.ModelAdmin):
   list_display   = ('id','user_id' )
   list_filter    = ('id','user_id' )
   

admin.site.register(administrateur, AdministrateureAdmin)