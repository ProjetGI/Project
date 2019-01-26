from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('reponse/', views.reponse, name='reponse'),
]