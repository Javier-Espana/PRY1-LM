# Configuraciones del proyecto
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas de archivos
DATA_PATH = os.path.join(BASE_DIR, 'data', 'BL-Flickr-Images-Book.csv')
OUTPUT_PATH = os.path.join(BASE_DIR, 'output', 'datos_procesados.csv')

# Configuración de logging
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'output', 'processing.log'),
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }
}