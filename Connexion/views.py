from django.shortcuts import render,redirect
from .loginform import ConnexionFormLog,ConnexionFormSign
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate, login,logout
from Connexion.models import administrateur,stagiare,formateur
from django.contrib.auth.models import User

def accueil(request):
    return render(request,'Connexion/templates/index.html',locals())

def logIn(request):
    profil=''
    error=False
    if request.method == "POST":
            form = ConnexionFormLog(request.POST)
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
                        return render(request,'Connexion/templates/login.html',{'form': form,'error':error,'signin':False})
            else :
                 error=True
                 return render(request,'Connexion/templates/login.html',{'form': form,'error':error,'signin':False})
    
    else :
        return render(request,'Connexion/templates/login.html',{'form':ConnexionFormLog(),'error':False,'signin':False})

def logInAfterSignIn(request,int)  :
        return render(request,'Connexion/templates/login.html',{'form':ConnexionFormLog(),'error':False,'signin':True})   
    

def view_dashboard(request):
     return render(request,'Base/UserBaseTemplate.html',locals())
    

def deconnexion(request):
    if request.user.username :
         logout(request)
         return redirect("/accueil/login/")
    else :
        return redirect("/accueil/login/")


def signup(request):
    error=False
    if request.method == "POST":
            form = ConnexionFormSign(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                re_password = form.cleaned_data["re_password"]
                last_name = form.cleaned_data["last_name"]
                faculte = form.cleaned_data["faculte"]
                first_name = form.cleaned_data["first_name"]
                email = form.cleaned_data["email"]
                
                if password == re_password :
                    if len(password) <  8 :
                        error=True
                        text ="Utilisez un password plus long."
                        return render(request,'Connexion/templates/signUp.html',{'form': form,'error':error,'error_text':text})

                    if User.objects.filter(username=username) :
                        error=True
                        text ="Username déja utilisé."
                        return render(request,'Connexion/templates/signUp.html',{'form': form,'error':error,'error_text':text})
                    elif  User.objects.filter(email=email) :
                        error=True
                        text="Email déja utilisé"
                        return render(request,'Connexion/templates/signUp.html',{'form': form,'error':error,'error_text':text})
                    #other case to treat password ...
                    else :
                        user = User.objects.create_user(username,email, password)
                        user.first_name = first_name
                        user.last_name = last_name
                        stagiare(user=user,faculte=faculte).save()
                        return redirect("/accueil/login/1")

                else:
                    error = True
                    text = "La répitition du password n'est pas validé."
                    return render(request,'Connexion/templates/signUp.html',{'form': form,'error':error,'error_text':text})
            else:
                  error = True
                  text= "form is not valid"
                  return render(request,'Connexion/templates/signUp.html',{'form': form,'error':error,'error_text':text})
    else:
            form=ConnexionFormSign()
            return render(request,'Connexion/templates/signUp.html',{'form': form,'error':error})



def about(request):
    return render(request,'Connexion/templates/about.html',locals())

def contact(request):
    return render(request,'Connexion/templates/contact.html',locals())

