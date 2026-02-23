import os
from django.core.wsgi import get_wsgi_application

# Remplacez 'settings' par le nom de votre fichier settings s'il est différent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()