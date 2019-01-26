from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.show_qcm, name='show qcm'),
    path('add', views.add_qcm, name='add qcm'),
    url(r'^id=(?P<id>\d+)$',views.show_question, name='show question'),
]