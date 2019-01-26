from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class stagiare(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    faculte = models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return self.user.username
        
class administrateur(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
   
def __str__(self):
        return self.user.username

class formateur(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    
    
    def __str__(self):
        
        return self.user.username













#username: nom utilisateur 30 caractères maximum (lettres, chiffres et les caractères spéciaux _, @, +, . et -) ;

#first_name: prénom, optionnel, 30 caractères maximum ;

#last_name: nom de famille, optionnel, 30 caractères maximum ;

#email: adresse e-mail ;

#password: un hash du mot de passe. Django enregistre pas les mots de passe en clair dans la base de données, nous y reviendrons plus tard ;

#is_staff: booléen, permet indiquer si lutilisateur a accès à ladministration de Django ;

#is_active: booléen, par défaut mis àTrue. Si mis àFalse, lutilisateur est considéré comme désactivé et ne peut plus se connecter. Au lieu de supprimer un utilisateur, il est conseillé de le désactiver afin de ne pas devoir supprimer d'éventuels modèles liés à l'utilisateur (avec uneForeignKeypar exemple) ;

#is_superuser: booléen, si mis àTrue, lutilisateur obtient toutes les permissions (nous y reviendrons plus tard également) ;

#last_login:datetime, représente la date/lheure à laquelle lutilisateur sest connecté la dernière fois ;

#date_joined:datetime, représente la date/l heure à laquelle l utilisateur s est inscrit ;

#user_permissions: une relationManyToManyvers les permissions ;

#groups: une relationManyToManyvers les groupes . #}
