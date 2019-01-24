from django.shortcuts import render,redirect
from .loginform import ConnexionForm
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate, login


def accueil(request):
    return render(request,'Connexion/templates/index.html',locals())

def logIn(request):
        error=False
        if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
                if user:  # Si l'objet renvoye n'est pas None
                    login(request,user)  # nous connectons l'utilisateur
                    #return render(request,'/cours/',locals())
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
    






def signup(request):
    return render(request,'Connexion/templates/signUp.html',locals())

def about(request):
    return render(request,'Connexion/templates/about.html',locals())

def contact(request):
    return render(request,'Connexion/templates/contact.html',locals())

