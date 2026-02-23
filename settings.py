import dj_database_url
import os

# ...

# 1. On tente d'abord de lire DATABASE_URL (Standard sur Render)
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
    # 2. Sinon, on utilise la config locale (Variables séparées)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB", "tuteur_ia"),
            "USER": os.getenv("POSTGRES_USER", "tuteur_ia"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", "tuteur_ia"),
            "HOST": os.getenv("POSTGRES_HOST", "localhost"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
        }
    }