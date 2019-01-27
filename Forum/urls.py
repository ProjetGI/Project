from django.urls import path
from django.conf.urls import url
from . import views
from .views import PublicationCreateView, PublicationDeleteView
from .views import ReponseCreateView, ReponseDeleteView
urlpatterns = [
    path('', views.forum, name='forum'),
    path('create/', PublicationCreateView.as_view(), name='createPub'),
    # path('confirm_delete_pub/', PublicationDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/confirm_delete_pub/$', PublicationDeleteView.as_view(), name='deletePub'),
    # path('reponse/', views.reponse, name='reponse'),
    url(r'^(?P<pk>\d+)/$', views.publication, name='publication'),
     # 
    # url(r'^reponse/$', views.reponse, name='AllReponse'),
    # 
    url(r'^reponse/(?P<pk>\d+)/$', views.reponse, name='reponse'),
    # path('reponse/create/', ReponseCreateView.as_view(), name='createRep'),
    url(r'^reponse/create/$', ReponseCreateView.as_view(), name='createRep'),
    url(r'^reponse/(?P<pk>\d+)/confirm_delete_rep/$', ReponseDeleteView.as_view(), name='deleteRep'),

]