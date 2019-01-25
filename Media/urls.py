from django.urls import path

from . import views

urlpatterns = [
    path('', views.cours, name='cours-list'),
    path('<int:cours_id>/', views.cours_page, name='cours-page'),
    path('cas-cliniques/', views.cas_cliniques, name='cas-clinique-list'),
    path('cas-cliniques/<int:cas_clinique_id>/', views.cas_clinique_page, name='cas-clinique-page'),
    path('add/', views.addCours, name='cours-add'),
    path('cas-cliniques/add/', views.addCasCliniques, name='cas-clinique-add'),
    path('delete/<int:cours_id>/', views.removeCours, name='cours-delete'),
    path('cas-cliniques/delete/<int:cours_id>/', views.removeCasCliniques, name='cas-clinique-delete'),

]