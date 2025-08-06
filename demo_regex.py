#!/usr/bin/env python3
"""
Script para demostrar y probar las expresiones regulares
Genera capturas de pantalla de las ejecuciones para documentación
"""

import re
import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from patterns import PATTERNS, HEADER_PATTERN

def test_pattern(field_name, pattern_config, test_strings): # Hace una prueba de un patrón con una lista de strings de prueba
    """Prueba un patrón con una lista de strings de prueba"""
    print(f"\n{'='*60}")
    print(f"PROBANDO PATRÓN: {field_name}")
    print(f"{'='*60}")
    print(f"Expresión Regular: {pattern_config['pattern']}")
    print(f"Descripción: {pattern_config['description']}")
    print(f"{'_'*60}")
    
    pattern = re.compile(pattern_config['pattern'])
    
    for test_string in test_strings:
        match = pattern.match(test_string)
        status = "COINCIDE" if match else "NO COINCIDE"
        print(f"{status:15} | '{test_string}'")
        if match:
            print(f"               | Grupo capturado: '{match.group(1) if match.groups() else match.group(0)}'")
    
    print(f"{'_'*60}")

def demo_regex_patterns(): # Demuestra todos los patrones de expresiones regulares
    """Demuestra todos los patrones de expresiones regulares"""
    print("DEMOSTRACIÓN DE EXPRESIONES REGULARES")
    print("Proyecto: Análisis de Dataset BL-Flickr-Images-Book.csv")
    print("Materia: Lógica Matemática")
    print("="*80)
    
    # Probar patrón de encabezados
    header_test = "Identifier,Edition Statement,Place of Publication,Date of Publication,Publisher,Title,Author,Contributors,Corporate Author,Corporate Contributors,Former owner,Engraver,Issuance type,Flickr URL,Shelfmarks"
    print(f"\nPROBANDO ENCABEZADOS:")
    print(f"Patrón: {HEADER_PATTERN}")
    header_match = re.match(HEADER_PATTERN, header_test)
    print(f"Resultado: {'VÁLIDO' if header_match else 'INVÁLIDO'}")
    
    # Datos de prueba específicos del dataset
    test_data = {
        'Identifier': ['000000206', '123456', 'ABC123', '', '0'],
        
        'Date of Publication': [
            '1879 [1878]', 
            '1851', 
            'pp. 40. G. Bryan & Co: Oxford, 1898',
            '1676',
            'No date',
            'May 15, 1892'
        ],
        
        'Flickr URL': [
            'http://www.flickr.com/photos/britishlibrary/tags/sysnum000000206',
            'https://flickr.com/photos/123',
            'http://google.com',
            'flickr.com/photos/123',
            ''
        ],
        
        'Issuance type': [
            'monographic',
            'serial', 
            'integrating resource',
            'book',
            'magazine',
            ''
        ],
        
        'Title': [
            'Walter Forbes. [A novel.] By A. A',
            'All for Greed. [A novel. The dedication signed: A. A. A., i.e. Marie Pauline Rose, Baroness Blaze de Bury.]',
            'Love the Avenger. By the author of "All for Greed."',
            ''
        ],
        
        'Author': [
            'A. A.',
            'A., A. A.',
            'A., E. S.',
            'Shakespeare, William',
            ''
        ]
    }
    
    # Probar patrones seleccionados
    key_patterns = ['Identifier', 'Date of Publication', 'Flickr URL', 'Issuance type', 'Title', 'Author']
    
    for field in key_patterns:
        if field in PATTERNS and field in test_data:
            test_pattern(field, PATTERNS[field], test_data[field])
    
    print(f"\n{'='*80}")
    print("DEMOSTRACIÓN COMPLETADA")
    print("Todos los patrones han sido probados con datos reales del dataset.")
    print(f"{'='*80}")

if __name__ == "__main__":
    demo_regex_patterns()
