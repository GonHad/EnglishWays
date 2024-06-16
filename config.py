# config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env

def config():
    return {
        'database_url': os.getenv('DATABASE_URL')
    }


