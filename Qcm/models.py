from django.db import models

# Create your models here.

class Qcm(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    qcmId = models.ForeignKey(Qcm, on_delete=models.CASCADE)
    num =  models.AutoField(primary_key=True)
    question = models.TextField()
    choiceA = models.CharField(max_length=150)
    choiceB = models.CharField(max_length=150)
    choiceC = models.CharField(max_length=150,blank=True)
    choiceD = models.CharField(max_length=150,blank=True)
    answer = models.CharField(max_length=4)
    


    class Meta:
        unique_together = (("qcmId", "num"),)
