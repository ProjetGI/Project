from django.urls import path

from . import views

urlpatterns = [
    path('', views.cours, name='cours-list'),
    path('<int:cours_id>/', views.cours_page, name='cours-page'),
    path('cas-cliniques/', views.cas_cliniques, name='cas-clinique-list'),
    path('cas-cliniques/<int:cas_clinique_id>/', views.cas_clinique_page, name='cas-clinique-page'),
    path('add/', views.CoursCreateView.as_view(), name='cours-add'),
    path('cas-cliniques/add/', views.CasCliniquesCreateView.as_view(), name='cas-clinique-add'),
]