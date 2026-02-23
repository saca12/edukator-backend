import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# On ne charge python-dotenv QUE si on n'est pas sur Render
# Sur Render, les variables sont injectées directement dans l'OS
if not os.environ.get('RENDER'):
    from dotenv import load_dotenv
    load_dotenv(os.path.join(BASE_DIR, '.env'))

# --- CONFIGURATION BASE DE DONNÉES EXCLUSIVE RENDER/PROD ---
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # Si DATABASE_URL est absente sur Render, l'app doit crash immédiatement 
    # avec une erreur explicite plutôt que de chercher localhost
    raise ValueError("L'environnement DATABASE_URL n'est pas configuré sur Render.")

# --- CONFIGURATION STATIQUE (WhiteNoise) ---
# Assurez-vous que ces lignes sont présentes pour collectstatic
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"