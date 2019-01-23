from django.urls import path

from . import views

urlpatterns = [
    path('', views.Qcm, name='Qcm'),
]