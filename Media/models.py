from django.db import models
from django.urls import reverse


class Cours(models.Model):
    title = models.CharField(max_length=150)
    description= models.TextField()
    category = models.CharField(max_length=150)
    author = models.CharField(max_length=200)
    #support_pdf = models.CharField(max_length=100)
    #video_src = models.CharField(max_length=100,blank=True,null=True)
    support_pdf=models.FileField(upload_to='cours/pdfs/')
    video_src=models.FileField(upload_to='cours/videos/',null=True,blank=True)
    def __str__(self):
        return self.title

    def hasVideo(self):
        return bool(self.video_src)




class CasCliniques(models.Model):
    title = models.CharField(max_length=150)
    description= models.TextField()
    category = models.CharField(max_length=150)
    author = models.CharField(max_length=200)
    support_pdf = models.FileField(upload_to='cas-clinique/pdfs/')
    corrige_src = models.FileField(upload_to='cas-clinique/corriges/')
    video_src = models.FileField(upload_to='cas-clinique/videos/',null=True,blank=True)

    def __str__(self):
        return self.title

    def hasVideo(self):
        return bool(self.video_src)