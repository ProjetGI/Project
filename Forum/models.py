from django.db import models
from django.conf import settings

class Publication(models.Model):
    titre = models.CharField(max_length=100)
    sujet = models.CharField(max_length=20)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    # auteur = models.CharField(max_length=20)
    redaction = models.TextField()
    nb_replies = models.IntegerField(default=0)
    date_poste = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titre

class Reponse(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    # auteur = models.CharField(max_length=20)
    rep_publication = models.IntegerField(default=1)
    reponse = models.TextField()
    date_reponse = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.reponse