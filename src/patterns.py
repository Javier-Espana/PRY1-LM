# Definición de patrones regex para cada columna
import re

PATTERNS = {
    'Identifier': {
        'pattern': r'^\d+',
        'description': 'Número entero positivo que identifica el registro',
        'example_valid': '12345',
        'example_invalid': 'ABC123'
    },
    'Edition Statement': {
        'pattern': r'^(.*?)(?=\t|$)',
        'description': 'Texto libre que describe la edición',
        'example_valid': 'First edition',
        'example_invalid': ''
    },
    'Place of Publication': {
        'pattern': r'^(.*?)(?=\t|$)',
        'description': 'Lugar de publicación, puede contener comas y otros caracteres',
        'example_valid': 'London, UK',
        'example_invalid': ''
    },
    'Date of Publication': {
        'pattern': r'^(\d{4}(-\d{2}(-\d{2})?)?|\[\d{4}\])?(?=\t|$)',
        'description': 'Año de publicación (YYYY), opcionalmente con mes y día (YYYY-MM-DD)',
        'example_valid': '1892-05-15',
        'example_invalid': 'May 15, 1892'
    },
    'Publisher': {
        'pattern': r'^(.*?)(?=\t|$)',
        'description': 'Nombre del editor/publisher',
        'example_valid': 'Macmillan Publishers',
        'example_invalid': ''
    },
    'Title': {
        'pattern': r'^(.*?)(?=\t|$)',
        'description': 'Título del libro, puede contener caracteres especiales',
        'example_valid': 'The Complete Works of William Shakespeare',
        'example_invalid': ''
    },
    'Author': {
        'pattern': r'^(.*?)(?=\t|$)',
        'description': 'Nombre del autor, puede contener iniciales y apellidos',
        'example_valid': 'Shakespeare, William',
        'example_invalid': ''
    },
    'Flickr URL': {
        'pattern': r'^((https?://)?(www\.)?flickr\.com/[^\s\t]+)?(?=\t|$)',
        'description': 'URL válida de Flickr (opcional)',
        'example_valid': 'https://www.flickr.com/photos/britishlibrary/12345',
        'example_invalid': 'http://invalid.url'
    },
    # Patrones para las demás columnas...
}

HEADER_PATTERN = r'^Identifier\tEdition Statement\tPlace of Publication\tDate of Publication\tPublisher\tTitle\tAuthor\tContributors\tCorporate Author\tCorporate Contributors\tFormer owner\tEngraver\tIssuance type\tFlickr URL\tShelfmarks$'

def validate_patterns():
    """Valida que los patrones estén correctamente definidos"""
    for field, config in PATTERNS.items():
        try:
            re.compile(config['pattern'])
        except re.error as e:
            raise ValueError(f"Patrón inválido para '{field}': {str(e)}")
    
    try:
        re.compile(HEADER_PATTERN)
    except re.error as e:
        raise ValueError(f"Patrón de encabezado inválido: {str(e)}")