from django.db import models


class Cours(models.Model):
    title = models.CharField(max_length=150)
    description= models.TextField()
    category = models.CharField(max_length=150)
    professeur = models.CharField(max_length=200)
    support_pdf = models.CharField(max_length=100)
    video_src = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title

