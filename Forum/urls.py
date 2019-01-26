from django.urls import path
from django.conf.urls import url
from . import views
from .views import PublicationCreateView, PublicationDeleteView

urlpatterns = [
    path('', views.forum, name='forum'),
    path('create/', PublicationCreateView.as_view(), name='create'),
    # path('confirm_delete_pub/', PublicationDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/confirm_delete_pub/$', PublicationDeleteView.as_view(), name='delete'),
    # path('reponse/', views.reponse, name='reponse'),
    url(r'^(?P<pk>\d+)/$', views.publication, name='publication'),
    url(r'^reponse/(?P<pk>\d+)/$', views.reponse, name='reponse'),

]