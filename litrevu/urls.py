"""
URL configuration for litrevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import authentication.views  # <--- On importe les vues de votre app authentication
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Page de connexion (Accueil)
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    
    # Page de déconnexion
    path('logout/', LogoutView.as_view(), name='logout'),

    # Page d'Inscription (C'est la ligne qui manquait !)
    path('signup/', authentication.views.signup_page, name='signup'),

    # Page du Flux
    path('feed/', reviews.views.feed, name='feed'),
]
