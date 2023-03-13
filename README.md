# OpenClassRoom - Projet 12 - Epic Events

# Utilisation

## Environnement virtuel

Pour mettre en place l'environnement virtuel nécessaire pour faire fonctionner le script, procéder comme suit :

Dans un terminal ouvert dans le dossier où vous avez cloné le repository, installez poetry :

```bash
python -m pip install poetry
```

Activez l'environnement, il se créera automatiquement dans votre dossier racine :

Windows / Mac / Linux

```bash
poetry shell
```

Si l'environnement c'est bien activé, le nom de l'environnement s'affichera à gauche de l'indicateur de position
dans le terminal

Installez tout les packages dans votre environnement virtuel :

```bash
poetry install
```

## Base de donnée

Lancer le container docker contenant postgres

```bash
docker compose -f "docker-compose.yml" up -d --build
```

## Serveur

Avant de lancer le serveur, effectuer les migrations :

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Pour lancer le serveur, entrez cette commande dans un invite de commande :

```bash
python manage.py runserver 8000
```

Dans votre navigateur, entrez l'adresse : 127.0.0.1:8000/admin pour arriver sur le site
