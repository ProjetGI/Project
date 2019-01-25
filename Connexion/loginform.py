
from django import forms
class ConnexionFormLog(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", widget=forms.PasswordInput)

class ConnexionFormSign(forms.Form):
    last_name = forms.CharField(label="last_name", max_length=50)
    first_name = forms.CharField(label="first_name", max_length=50)
    email = forms.CharField(label="email", max_length=50)
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    re_password = forms.CharField(label="re_password", widget=forms.PasswordInput)
    faculte = forms.CharField(label="faculte", max_length=50)
