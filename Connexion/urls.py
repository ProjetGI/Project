#from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from . import views


urlpatterns = [
    
    path('', views.accueil),
    path('login/', views.logIn),
    path('signUp/', views.signup),
    path('logout/', views.deconnexion),

]