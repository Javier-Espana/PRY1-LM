# Definición de patrones de expresiones regulares para análisis de dataset CSV
# Este módulo contiene todos los patrones regex utilizados para validar y extraer
# información específica de cada columna del dataset BL-Flickr-Images-Book.csv
# 
# Los patrones están organizados por campo y incluyen:
# - pattern: expresión regular específica para el campo
# - description: explicación del propósito del patrón
# - example_valid: ejemplo que debe coincidir con el patrón
# - example_invalid: ejemplo que debe ser rechazado por el patrón

import re

# Diccionario que contiene todos los patrones regex para validación de campos del CSV
# Cada entrada define las reglas de validación para una columna específica

PATTERNS = {
    'Identifier': {
        'pattern': r'^\d+',
        'description': 'Número entero positivo que identifica de manera única cada registro en el dataset',
        'example_valid': '12345',
        'example_invalid': 'ABC123'
    },
    'Edition Statement': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Declaración de edición del libro, captura texto libre hasta encontrar una coma o final de línea',
        'example_valid': 'First edition',
        'example_invalid': ''
    },
    'Place of Publication': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Lugar geográfico de publicación, extrae texto hasta la primera coma',
        'example_valid': 'London',
        'example_invalid': ''
    },
    'Date of Publication': {
        'pattern': r'^([^,]*\d{4}[^,]*)(?=,|$)',
        'description': 'Fecha de publicación que debe contener un año de exactamente 4 dígitos, permite texto adicional',
        'example_valid': '1879 [1878]',
        'example_invalid': 'No date'
    },
    'Publisher': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Nombre del editor/publisher',
        'example_valid': 'S. Tinsley & Co.',
        'example_invalid': ''
    },
    'Title': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Título del libro, texto hasta la primera coma',
        'example_valid': 'Walter Forbes. [A novel.] By A. A',
        'example_invalid': ''
    },
    'Author': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Nombre del autor, puede contener iniciales y apellidos',
        'example_valid': 'A. A.',
        'example_invalid': ''
    },
    'Contributors': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Contribuidores del libro',
        'example_valid': 'FORBES, Walter.',
        'example_invalid': ''
    },
    'Corporate Author': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Autor corporativo si aplica',
        'example_valid': 'British Library',
        'example_invalid': ''
    },
    'Corporate Contributors': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Contribuidores corporativos',
        'example_valid': 'Oxford University Press',
        'example_invalid': ''
    },
    'Former owner': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Propietario anterior del libro',
        'example_valid': 'John Smith Collection',
        'example_invalid': ''
    },
    'Engraver': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Grabador si aplica',
        'example_valid': 'William Hogarth',
        'example_invalid': ''
    },
    'Issuance type': {
        'pattern': r'^(monographic|serial|integrating resource|continuing)(?=,|$)',
        'description': 'Tipo de publicación: monográfica, serie, recurso integrado o continuo',
        'example_valid': 'monographic',
        'example_invalid': 'unknown'
    },
    'Flickr URL': {
        'pattern': r'^(https?://[^\s,]*flickr\.com[^\s,]*)(?=,|$)',
        'description': 'URL válida del sitio Flickr que debe comenzar con protocolo HTTP/HTTPS y contener el dominio flickr.com',
        'example_valid': 'http://www.flickr.com/photos/britishlibrary/tags/sysnum000000206',
        'example_invalid': 'http://invalid.url'
    },
    'Shelfmarks': {
        'pattern': r'^([^,]*?)(?=,|$)',
        'description': 'Códigos de ubicación física del libro en la biblioteca, sistema de clasificación interno',
        'example_valid': 'British Library HMNTS 12641.b.30.',
        'example_invalid': ''
    }
}

# Patrón regex para validar la estructura completa de los encabezados del CSV
# Asegura que el archivo tenga exactamente las 15 columnas esperadas en el orden correcto
HEADER_PATTERN = r'^Identifier,Edition Statement,Place of Publication,Date of Publication,Publisher,Title,Author,Contributors,Corporate Author,Corporate Contributors,Former owner,Engraver,Issuance type,Flickr URL,Shelfmarks$'

def validate_patterns(): # Valida que todos los patrones regex estén correctamente definidos y sean compilables
    """
    Valida que todos los patrones regex estén correctamente definidos y sean compilables.
    
    Esta función realiza una verificación de sintaxis de todas las expresiones regulares
    definidas en el diccionario PATTERNS, incluyendo el patrón de encabezados.
    
    Raises:
        ValueError: Si algún patrón tiene sintaxis inválida o no puede ser compilado
    """
    # Iterar sobre todos los patrones definidos para cada campo del CSV
    # Iterar sobre todos los patrones definidos para cada campo del CSV
    for field, config in PATTERNS.items(): # Verifica cada patrón regex
        try:
            # Intentar compilar cada expresión regular para verificar su sintaxis
            re.compile(config['pattern'])
        except re.error as e:
            raise ValueError(f"Patrón inválido para '{field}': {str(e)}")
    
    try:
        # Validar también el patrón de encabezados del CSV
        re.compile(HEADER_PATTERN) # Verifica el patrón de encabezados
    except re.error as e:
        raise ValueError(f"Patrón de encabezado inválido: {str(e)}") 