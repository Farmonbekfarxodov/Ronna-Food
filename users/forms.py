from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

Usermodel = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = Usermodel
        fields = ['first_name','last_name','username','email','password1','password2']


class LoginForm(forms.Form):
    email_or_username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)
    