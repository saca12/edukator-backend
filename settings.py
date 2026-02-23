import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# --------------------------------------------------------------------------
#  DATABASE (priorité absolue à l'env var DATABASE_URL sur Render)
# --------------------------------------------------------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,           # obligatoire sur Render Postgres
    )
}

# Optionnel : log pour debug (à retirer plus tard)
print("DATABASE_URL utilisée :", os.environ.get('DATABASE_URL'))
print("Connexion configurée :", DATABASES['default'])