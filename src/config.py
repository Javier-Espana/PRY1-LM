# Configuraciones del proyecto
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas de archivos
DATA_PATH = os.path.join(BASE_DIR, 'data', 'BL-Flickr-Images-Book.csv')
OUTPUT_PATH = os.path.join(BASE_DIR, 'output', 'datos_procesados.csv')