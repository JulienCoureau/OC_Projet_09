from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', )


class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d’utilisateur', max_length=63)
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
