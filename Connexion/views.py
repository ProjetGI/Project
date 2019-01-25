from django.shortcuts import render,redirect
from .loginform import ConnexionForm
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate, login,logout
from Connexion.models import administrateur,stagiare,formateur


def accueil(request):
    return render(request,'Connexion/templates/index.html',locals())

def logIn(request):
    profil='walo'
    error=False
    if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
                if user:  # Si l'objet renvoye n'est pas None
                    login(request,user)  # nous connectons l'utilisateur
                    id_user = request.user.id
                    stag = stagiare.objects.filter(user_id=id_user)
                    forma = formateur.objects.filter(user_id=id_user)
                    admin = administrateur.objects.filter(user_id=id_user)

                    if stag :
                        profil='stagiare'
                    elif forma:
                        profil='formateur'
                    elif admin:
                        profil='administrateur'
                    else:
                        profil='super_user'
                    request.session['profil_type'] = profil
                    return redirect('/cours/')
                   # it's possible that  lost the request
                else:
                        error = True
                        return render(request,'Connexion/templates/login.html',{'form': form,'error':error})
            else :
                 error=True
                 return render(request,'Connexion/templates/login.html',{'form': form,'error':error})
    else:
            form=ConnexionForm()
            return render(request,'Connexion/templates/login.html',{'form': form,'error':error})

           

def view_dashboard(request):
     return render(request,'Base/UserBaseTemplate.html',locals())
    

def deconnexion(request):
    if request.user :
         logout(request)
         return redirect("/accueil/login/")
    else :
        return redirect("/accueil/login/")


def signup(request):
    return render(request,'Connexion/templates/signUp.html',locals())

def about(request):
    return render(request,'Connexion/templates/about.html',locals())

def contact(request):
    return render(request,'Connexion/templates/contact.html',locals())

