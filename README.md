# LITRevu

LITRevu est une application web Django de partage de critiques littéraires. Elle permet aux utilisateurs de solliciter des avis sur des ouvrages via un système de tickets, et de publier des critiques notées. L'application intègre un système d'abonnements générant un flux d'actualité personnalisé.

## Fonctionnalités

* Authentification : Gestion des inscriptions et des sessions utilisateurs.
* Réseau : Système d'abonnement unidirectionnel entre les membres.
* Publications : Création, modification et suppression de tickets (demandes d'avis) et de critiques.
* Flux d'actualité : Affichage antéchronologique des posts de l'utilisateur et de ses abonnements.

## Installation et exécution

### Prérequis
* Python 3.8+
* Git

### Déploiement local

1. Clonez le dépôt :
    git clone <URL_DU_REPO>
    cd projet_9

2. Créez et activez l'environnement virtuel :
    # macOS/Linux
    python3 -m venv env
    source env/bin/activate

    # Windows
    python -m venv env
    env\Scripts\activate

3. Installez les dépendances :
    pip install -r requirements.txt

4. Démarrez le serveur :
    python manage.py runserver

L'interface est accessible à l'adresse : http://127.0.0.1:8000/

## Environnement de test

Une base de données SQLite (db.sqlite3) pré-remplie est incluse pour faciliter les tests fonctionnels en environnement de développement. Elle contient un jeu de données initial comprenant des utilisateurs, des relations d'abonnement et des publications.

Comptes de test disponibles :
* Compte 1 : Identifiant : <identifiant_1> | Mot de passe : <mdp_1>
* Compte 2 : Identifiant : <identifiant_2> | Mot de passe : <mdp_2>

## Linting et normes

Le code source est conforme à la norme PEP 8. L'analyse statique est configurée avec Flake8 (les exclusions standards des environnements virtuels et migrations sont définies dans setup.cfg).

Pour exécuter l'analyseur :
    flake8
