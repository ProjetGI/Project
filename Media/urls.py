from django.urls import path

from . import views

urlpatterns = [
    path('', views.cours, name='cours'),
    path('1', views.cours_page, name='cours_page'),
]