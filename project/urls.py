#test
from django.contrib import admin
from Connexion import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    #path admin
    path('admin/', admin.site.urls),

    #paths connexion
    path('accueil/', include('Connexion.urls')),
    path('about/',views.about),
    path('contact/',views.contact),

    #path cours
    path('qcm/', include('Qcm.urls')),
    path('cours/', include('Media.urls')),
    path('forum/', include('Forum.urls')),
]
