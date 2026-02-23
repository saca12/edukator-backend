#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt #

# Collecte des fichiers statiques
python manage.py collectstatic --no-input #

# Migration de la base de données
# Cette commande échouera si DATABASE_URL n'est pas dans l'onglet Environment de Render
python manage.py migrate --no-input #