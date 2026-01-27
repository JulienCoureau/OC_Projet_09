from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from . import forms # On va créer ce fichier juste après

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            # 👇 C'est cette ligne qui va nous sauver
            print("ERREURS FORMULAIRE :", form.errors)
            
    return render(request, 'authentication/signup.html', context={'form': form})